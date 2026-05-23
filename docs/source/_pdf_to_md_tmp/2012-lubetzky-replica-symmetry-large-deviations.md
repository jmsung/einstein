# arXiv:1210.7013v2[math.PR]4Feb2016

## ON REPLICA SYMMETRY OF LARGE DEVIATIONS IN RANDOM GRAPHS

EYAL LUBETZKY AND YUFEI ZHAO

Abstract. The following question is due to Chatterjee and Varadhan (2011). Fix 0 < p < r < 1 and take G ∼ G(n, p), the Erdo˝s-R´enyi random graph with edge density p, conditioned to have at least as many triangles as the typical G(n, r). Is G close in cut-distance to a typical G(n, r)? Via a beautiful new framework for large deviation principles in G(n, p), Chatterjee and Varadhan gave bounds on the replica symmetric phase, the region of (p, r) where the answer is positive. They further showed that for any small enough p there are at least two phase transitions as r varies.

We settle this question by identifying the replica symmetric phase for triangles and more generally for any ﬁxed d-regular graph. By analyzing the variational problem arising from the framework of Chatterjee and Varadhan we show that the replica symmetry phase consists of all (p, r) such that (rd, hp(r)) lies on the convex minorant of x  → hp(x1/d) where hp is the rate function of a binomial with parameter p. In particular, the answer for triangles involves hp(√x) rather than the natural guess of hp(x1/3) where symmetry was previously known. Analogous results are obtained for linear hypergraphs as well as the setting where the largest eigenvalue of G ∼ G(n, p) is conditioned to exceed the typical value of the largest eigenvalue of G(n, r). Building on the work of Chatterjee and Diaconis (2012) we obtain additional results on a class of exponential random graphs including a new range of parameters where symmetry breaking occurs. En route we give a short alternative proof of a graph homomorphism inequality due to Kahn (2001) and Galvin and Tetali (2004).

1. Introduction

The following question was raised by Chatterjee and Varadhan [8] concerning large deviations in G(n,p), the Erd˝s-R´enyi random graph on n vertices with edge density p.

Fix 0 < p < r < 1 and let Gn be an instance of G(n,p) conditioned on the rare event of having at least as many triangles as a typical instance of G(n,r). Is it the case that as n → ∞ the graph Gn is close in cut-distance to a typical G(n,r) graph?

(A more formal statement, including the deﬁnition of the graph cut-metric, is postponed to §1.1.) This amounts to asking whether the likely reason for too many triangles is an overwhelming number of edges, uniformly distributed, or some fewer edges arranged in a special structure, e.g., a clique. Dubbed replica symmetry and symmetry breaking, resp., the dichotomy between these scenarios turns out to depend on p and r. Intriguingly, it was known that for small enough p there are at least two phase transitions as r increases from p to 1, with symmetry replica near the two endpoints.

In this work we analyze the variational problems arising from the framework of Chatterjee and Varadhan and obtain a full answer for the question above, as depicted in Fig. 1. More generally, we identify the phase diagram for upper tails of any ﬁxed regular subgraph and derive related results in other random graph settings, e.g., exponential random graphs, random hypergraphs, etc.

1.1. Subgraph densities and spectral radii. Large deviations for subgraph densities in random graphs have been extensively studied (see, e.g., [28, 45, 31, 27, 29, 5, 13, 14] as well as [3, 26] and the references therein). A representing example which drew signiﬁcant attention is upper tails of triangle counts, i.e., estimating the probability that G(n,p) has at least n3 r3 triangles where r = (1 + η)p for ﬁxed η > 0 (allowing p to vary with n), a problem whose understanding is still incomplete. The order of the rate function (the normalized logarithm of this probability) when p → 0 was only very recently settled: Chatterjee [5] and DeMarco and Kahn [14] independently established it to be n2p2 log(1/p) when p log n/n, and yet the exact rate function remains unknown in this range of p. We now turn to what was known for ﬁxed p, our focus in this paper. 1

1.0

0.8

0.6

r

0.4

0.2

0.0

0.0 0.2 0.4 0.6 0.8 1.0

p

Figure 1. Phase diagram for the upper tail of triangle counts. Shaded region is the replica symmetric phase; the region to its left is the symmetry breaking phase. Previous results [6, 8] established replica symmetry to the right of the dashed curve.

Clearly, if the total number of edges in G(n,p) deviates to m ∼ n2 r then one will arrive at a random graph with m uniformly distributed edges featuring the desired number of triangles. Thus, the large deviation rate function for encountering n3 r3 triangles in G(n,p) is at most hp(r), where

1 − x 1 − p

x p

+ (1 − x)log

for p ∈ (0,1) and x ∈ [0,1] (1.1)

hp(x) := xlog

is the rate function associated to the binomial distribution with probability p. However, it is possible that other conﬁgurations with broken symmetry would give rise to lower rate functions.

As an application of Stein’s method for concentration inequalities, Chatterjee and Dey [6] found a range of (p,r) where the large deviation rate function for triangles is equal to hp(r), namely when p ≥ 2/(2 + e3/2) ≈ 0.31 or when r is suitably close either to p or to 1. This symmetry region was explicitly stated in [8, Theorem 4.3] as all pairs (p,r) where (r3,hp(r)) lies on the convex minorant of x  → hp(x1/3). The breakthrough work of Chatterjee and Varadhan [8] introduced a remarkable general framework for large deviation principles in G(n,p) via Szemer´edi’s regularity lemma [44] and the theory of graph limits by Lov´sz et al. [33, 34, 4]. It expressed the large deviation rate function, and moreover the structure of the random graph conditioned on the large deviation, in terms of a variational problem on graphons, the inﬁnite-dimensional limit objects for graph sequences.

Although often this variational problem is untractable, for triangles in the mentioned range of (p,r) it was shown in [8] to have a unique and symmetric solution. To formalize this symmetry, we say a graph G is close in cut-distance to a typical G(n,r) graph if all induced subgraphs on a linear number of vertices have edge density close to r. More precisely, for a graph G and r ∈ [0,1] let

1 |V (G)|2

eG(A,B) − r |A||B| ,

δ (G,r) := sup

A,B⊂V (G)

where eG(A,B) is the number of pairs (a,b) ∈ A × B with ab ∈ E(G). Chatterjee and Varadhan showed that, in the above range of (p,r), if Gn ∼ G(n,p) is conditioned to have at least n3 r3 triangles then δ (Gn,r) → 0 in probability as n → ∞. The function x  → hp(x1/3) governing that region is the natural candidate for the phase boundary as the cube-root accounts for the 3 edges of the triangle (see, e.g., [15, §4.5.2] for related literature), and indeed Chatterjee and Varadhan asked whether this precisely characterizes the full replica symmetric phase. As it turns out, however, the replica symmetric phase is strictly larger, being governed instead by x  → hp(√x). (See Fig. 1.)

1.0

d = 7

d = 6

0.8

d = 5

d = 4

d = 3

0.6

r d = 2

0.4

0.2

0.0

0.0 0.2 0.4 0.6 0.8 1.0

p

Figure 2. The phase boundary for counts of d-regular ﬁxed subgraphs in G(n,p).

For any graph G let e(G) = |E(G)|, and for any two graphs G and H let hom(H,G) denote the number of homomorphisms from H to G (i.e., maps V (H) → V (G) that carry edges to edges). Let

t(H,G) := |hom(H,G)|

|V (G)||V (H)| be the probability that a random map V (H) → V (G) is a graph homomorphism. We now state our main result on the phase diagram for large deviations in densities of d-regular subgraphs.

- Theorem 1.1. Fix 0 < p ≤ r < 1 and let H be a ﬁxed d-regular graph for some d ≥ 2. Let Gn ∼ G(n,p) be the Erd˝os-Re´nyi random graph on n vertices with edge probability p.


- (i) If the point (rd,hp(r)) lies on the convex minorant of the function x  → hp(x1/d) then

lim

n→∞

- 1 n

- 2


log P t(H,Gn) ≥ re(H) = −hp(r) and furthermore, for every ε > 0 there exists some C = C(H,ε,p,r) > 0 such that for all n, P δ (Gn,r) < ε t(H,Gn) ≥ re(H) ≥ 1 − e−Cn2 .

- (ii) If the point (rd,hp(r)) does not lie on the convex minorant of the function x  → hp(x1/d) then


- 1 n

- 2


log P t(H,Gn) ≥ re(H) > −hp(r) and furthermore, there exist ε,C > 0 such that for all n,

lim

n→∞

P inf δ (Gn,s) : 0 ≤ s ≤ 1 > ε t(H,Gn) ≥ re(H) ≥ 1 − e−Cn2 . In particular, when d = 2, case (ii) occurs if and only if p < 1 + (r−1 − 1)1/(1−2r) −1.

The boundary curves for various values of d are plotted in Fig. 2. It is easy to verify (Lemma A.1) that the rightmost point in the curve for d-regular subgraphs is (p,r) = d−1+ de−d/1(d−1), d−d1 .

We give an analogous result for large deviations of the spectral radius of an Erd˝s-R´enyi random graph. The phase boundary in this case coincides with that of triangles.

- Theorem 1.2. Fix 0 < p ≤ r < 1. Let Gn ∼ G(n,p) be an Erd˝os-Re´nyi random graph on n vertices with edge probability p, and let λ1(Gn) denote the largest eigenvalue of its adjacency matrix.


- (i) If p ≥ 1 + (r−1 − 1)1/(1−2r) −1 then

lim

n→∞

- 1 n

- 2


log P(λ1(Gn) ≥ nr) = −hp(r) and furthermore, for every ε > 0 there exists some C = C(ε,p,r) > 0 such that for all n, P(δ (Gn,r) < ε | λ1(Gn) ≥ nr) ≥ 1 − e−Cn2 .

- (ii) If p < 1 + (r−1 − 1)1/(1−2r) −1 then


- 1 n

- 2


log P(λ1(Gn) ≥ nr) > −hp(r) and furthermore, there exist ε,C > 0 such that for all n,

lim

n→∞

P inf δ (Gn,s) : 0 ≤ s ≤ 1 > ε λ1(Gn) ≥ nr ≥ 1 − e−Cn2.

Both theorems are proved through an analysis of the graphon variational problems rising from the framework of Chatterjee and Varadhan [8]. We show that throughout the replica symmetric region its unique solution is the symmetric one (a consequence of a generalized form of H¨lder’s inequality), whereas elsewhere one can construct graphons that outperform the symmetric candidate. Note that Theorem 1.2 addresses spectral large deviations, whereas the framework of [8] was tailored for subgraph densities (the recent work [9] broadens it to general random matrix properties with respect to an appropriately deﬁned spectral distance. Here we consider concretely large deviations in the spectral norm of random graphs). Fortunately, the results of [8] easily extend to a wide family of graph parameters with respect to the cut-metric, including the operator norm, the extension of the (normalized) spectral norm to the space of graphons. This generalization is detailed in §2.

- 1.2. Exponential random graphs. We now turn our attention to a diﬀerent random graph model, the basic setting of which assigns a probability pβ(G) to every graph G on n labeled vertices as a function of its edge density t(K2,G), its triangles density t(K3,G) and a weight vector β = (β1,β2) for these two quantities.1 Namely, the graph G appears with the following probability:


n 2

1 Zn

exp

(β1t(K2,G) + β2t(K3,G)) , (1.2)

pβ(G) =

where Zn is a normalizing factor (the partition function). When β2 > 0 the model favors graphs with more triangles whereas triangles are discouraged for β2 < 0. There is a rich literature on both ﬂavors of the model, motivated in part by applications in social networking: the reader is referred to [24, 36, 37, 43] as well as [2, 7] and the references therein.

As shown by Bhamidi, Bresler and Sly [2] and Chatterjee and Diaconis [7], when β2 ≥ 0 and n is large, a typical random graph drawn from the distribution has a trivial structure — essentially the same one as an Erd˝s-R´enyi random graph with a suitable edge density. This somewhat disappointing conclusion accounts for some of the practical diﬃculties with statistical parameter estimation for such models. It was further shown in [7] that if we allow β2 to be suﬃciently negative, then the model does behave appreciably diﬀerentially from an Erd˝s-R´enyi model. In this part of our work we focus on the case β2 > 0, and propose a natural generalization that will enable the model to exhibit a nontrivial structure instead of the previously observed Erd˝s-Re´nyi behavior.

1The general model allows for an arbitrary (ﬁxed) collection of subgraphs. While the majority of our arguments can be extended to the general setting, we focus on the two-term model for simplicity and clarity.

α = 0.5

α = 0.6

α = 0.65

- 0

- 1

- 2

- 3

- 4

- 5

- 6


- 0

- 1

- 2

- 3

- 4

- 5

- 6


- 0

- 1

- 2

- 3

- 4

- 5

- 6


Broken symmetry in the shaded region

Replica symmetric for β1 ≥ −2.

β2

β2

β2

4 3 2 1 0

4 3 2 1 0

4 3 2 1 0

β1

β1

β1

α = 2/3

α = 0.66

α = 1

- 0

- 1

- 2

- 3

- 4

- 5

- 6


- 0

- 1

- 2

- 3

- 4

- 5

- 6


- 0

- 1

- 2

- 3

- 4

- 5

- 6


u∗(β1, β2) is discontinuous across the curve Γ

Replica symmetric everywhere

β2

β2

β2

4 3 2 1 0

4 3 2 1 0

4 3 2 1 0

β1

β1

β1

Figure 3. The (β1,β2)-phase diagrams for the exponential random graph model in (1.3) with β2 ≥ 0 and various values of α > 0, as a special case of Theorem 1.3. When α < 2/3, symmetry breaking occurs in the shaded region (at least) and replica symmetry occurs for β1 ≥ −2. When α ≥ 2/3, replica symmetry always occurs.

Consider the exponential random graph model which includes an additional exponent α > 0 in the exponent of the triangle density term:

1 Zn

n 2

(β1t(K2,G) + β2t(K3,G)α) . (1.3)

pα,β(G) =

exp

We will show that this model exhibits a symmetry breaking phase transition even when β2 > 0. When α ≥ 2/3, the generalized model features the Erd˝s-R´enyi behavior, similar to the previously observed case of α = 1. However, for 0 < α < 2/3, there exist regions of values of (β1,β2) for which a typical random graph drawn from this distribution has symmetry breaking. As was the case for Theorems 1.1 and 1.2, rather than just triangles we prove this result for any d-regular graph H.

- Theorem 1.3. Let H be a d-regular graph for some ﬁxed d ≥ 2 and ﬁx β1 ∈ R and β2,α > 0. Let be Gn be an exponential random graph on n labeled vertices with law


n 2

1 Zn

(β1t(K2,Gn) + β2t(H,Gn)α) . (1.4)

exp

pα,β(Gn) =

- (a) Suppose α ≥ d/e(H). There exists a subset Γ = {(β1,ϕ(β1)) : β1 < log(e(H)α − 1) − e(eH(H)α)α−1} of R2 for some function ϕ : R → R such that for every (β1,β2) ∈ R × (0,∞) \ Γ there exists 0 < u∗ < 1 so that δ (Gn,u∗) → 0 almost surely as n → ∞, and for every (β1,β2) ∈ Γ there exist 0 < u∗1 < u∗2 < 1 such that min{δ (Gn,u∗1) , δ (Gn,u∗2)} → 0 almost surely as n → ∞.


![image 1](<2012-lubetzky-replica-symmetry-large-deviations_images/imageFile1.png>)

![image 2](<2012-lubetzky-replica-symmetry-large-deviations_images/imageFile2.png>)

![image 3](<2012-lubetzky-replica-symmetry-large-deviations_images/imageFile3.png>)

![image 4](<2012-lubetzky-replica-symmetry-large-deviations_images/imageFile4.png>)

![image 5](<2012-lubetzky-replica-symmetry-large-deviations_images/imageFile5.png>)

![image 6](<2012-lubetzky-replica-symmetry-large-deviations_images/imageFile6.png>)

![image 7](<2012-lubetzky-replica-symmetry-large-deviations_images/imageFile7.png>)

![image 8](<2012-lubetzky-replica-symmetry-large-deviations_images/imageFile8.png>)

![image 9](<2012-lubetzky-replica-symmetry-large-deviations_images/imageFile9.png>)

![image 10](<2012-lubetzky-replica-symmetry-large-deviations_images/imageFile10.png>)

![image 11](<2012-lubetzky-replica-symmetry-large-deviations_images/imageFile11.png>)

![image 12](<2012-lubetzky-replica-symmetry-large-deviations_images/imageFile12.png>)

![image 13](<2012-lubetzky-replica-symmetry-large-deviations_images/imageFile13.png>)

![image 14](<2012-lubetzky-replica-symmetry-large-deviations_images/imageFile14.png>)

![image 15](<2012-lubetzky-replica-symmetry-large-deviations_images/imageFile15.png>)

![image 16](<2012-lubetzky-replica-symmetry-large-deviations_images/imageFile16.png>)

![image 17](<2012-lubetzky-replica-symmetry-large-deviations_images/imageFile17.png>)

![image 18](<2012-lubetzky-replica-symmetry-large-deviations_images/imageFile18.png>)

![image 19](<2012-lubetzky-replica-symmetry-large-deviations_images/imageFile19.png>)

Figure 4. Linear d-regular hypergraphs: a cycle (d = 2) and the Fano plane (d = 3).

- (b) Suppose 0 < α < d/e(H) and β1 ≥ log(d − 1) − d/(d − 1). Then there exists 0 < u∗ < 1 such that for every ε > 0 there is a C > 0 such that δ (Gn,u∗) → 0 almost surely as n → ∞.
- (c) Suppose 0 < α < d/e(H) and β1 < log(d − 1) − d/(d − 1). Then there exists an open interval of values β2 > 0 with the property that there exist ε,C > 0 such that for all n,


P inf δ (Gn,s) : 0 ≤ s ≤ 1 > ε ≥ 1 − e−Cn2 .

Note that, as in the previous theorems, for the replica symmetric phase one can quantify the rate of convergence, e.g., when δ (Gn,u∗) → 0 almost surely we in fact have that for any ε > 0 there exists some C > 0 so that P(δ (Gn,u∗) ≤ ε) ≥ 1 − e−Cn2 for every n.

- 1.3. Linear hypergraphs. Theorem 5.1 (see §5) extends Theorem 1.1 to the setting of random hypergraphs. A k-uniform hypergraph G consists of a set V (G) of vertices and a set E(G) of hyperedges, where each hyperedges is a k-element subsets of V (G). It is said to be d-regular if every vertex is incident to exactly d edges, and linear if every two vertices are incident to at most one common hyperedge (see Fig. 4 for examples of d-regular 3-uniform linear hypergraphs). The random hypergraph G(k)(n,p) is formed by starting with n vertices and adding k-element subset of the vertices as a hyperedge independently with probability p.

In order to generalize our arguments to large deviations in the density of H, an arbitrary d-regular linear hypergraph, one must ﬁrst extend the theory developed by Chatterjee and Varadhan [8] to k-uniform hypergraphs. Thanks to the linearity of the hypergraph H there is a simple extension of Szemer´edi’s regularity lemma to hypergraphs that behaves well with respect to the density of H.

- 1.4. Graph homomorphisms. Alon [1] conjectured in 1991 that the number of independent sets in a d-regular graph G, denoted i(G), satisﬁes i(G) ≤ i(Kd,d)|V (G)|/(2d), i.e., it is maximized when


- G is a union of complete bipartite graphs Kd,d. Kahn [30] veriﬁed this when G is bipartite using an ingenious application of the entropy method (speciﬁcally, Shearer’s inequality). This result was thereafter extended by the second author [46] to all d-regular graphs via an elementary bijection. Using the entropy method of Kahn, Galvin and Tetali [21] extended [30] to graph homomorphisms:


- Theorem 1.4 (Galvin and Tetali [21], following Kahn [30]). Let G be a simple d-regular bipartite graph, and let H be a graph, possibly containing loops. We have


hom(G,H) ≤ hom(Kd,d,H)|V (G)|/(2d). (1.5)

Observe that this inequality generalizes the independent set result, since i(G) = hom(G, ). Previously, all the known proofs of these inequalities relied on entropy techniques. Regarding a more elementary proof, Kahn [30] wrote that “one would think that this simple and natural conjecture... would have a simple and natural proof.” As a related aside, in §6 we give a short new entropy-free proof for (1.5) as an immediate consequence of the generalized form of H¨lder’s inequality.

- 1.5. Organization. In §2 we review graph limits as well as the large deviation principle for random graphs developed by Chatterjee and Varadhan. In §3 we apply the machinery of Chatterjee and Varadhan to prove Theorems 1.1 and 1.2, determining the phase diagram for large deviations of subgraph densities and the largest eigenvalue in G(n,p), resp. Section 4 focuses on exponential random graphs and gives the proof of Theorem 1.3. In §5 we extend Theorem 1.1 to densities of linear hypergraphs in random hypergraphs. Section 6 contains the short new proof of the inequalities of Kahn and Galvin-Tetali (Theorem 1.4). Finally, in §7 we discuss some open problems.


2. Graph limits and the framework of Chatterjee-Varadhan

The theory of Chatterjee-Varadhan reduces the problem of determining the rate function for large deviations in dense random graphs to solving a prescribed variational problem in graph limits. We will review the required deﬁnitions from graph limit theory and then describe the results of [8] in the broader context of “nice” graph parameters, generalizing subgraph counts.

- 2.1. Graph limits. Let W be the space of all bounded measurable functions [0,1]2 → R that


are symmetric (i.e., f(x,y) = f(y,x) for all x,y ∈ [0,1]). Further let W0 denote all symmetric measurable functions [0,1]2 → [0,1], referred to as graphons or kernels (occasionally these are called labeled graphons since later we consider equivalence classes of W0 modulo measure-preserving bijections on [0,1]). Lov´sz and Szegedy [33] showed that the elements of W0 are limit objects for sequences of graphs w.r.t. all subgraph densities. Speciﬁcally, for any f ∈ W and any simple graph

- H with V (H) = [m] = {1,2,...,m}, deﬁne


f(xi,xj) dx1 ···dxm .

t(H,f) =

[0,1]m (i,j)∈E(H)

(We shall omit the domain of integration when there is no ambiguity.) Any simple graph G on vertices {1,2,...,n} can be represented as a graphon fG by

fG(x,y) =

1 if ( nx , ny ) is an edge of G, 0 otherwise.

In particular, t(H,G) = t(H,fG) for any two graphs H and G.

A sequence of graphs {Gn}n≥1 is said to converge if the sequence of subgraph densities t(H,Gn) converges for every ﬁxed ﬁnite simple graph H. It was shown in [33] that for any such convergent graph sequence there is a limit object f ∈ W0 such that t(H,Gn) → t(H,f) for every ﬁxed H. Conversely, any f ∈ W0 arises as a limit of a convergent graph sequence.

We will consider several norms on W, beginning with the standard Lp norm

1/p

f p := |f(x,y)|p dxdy

.

Each f ∈ W can be viewed as a Hilbert-Schmidt kernel operator Tf on L2([0,1]) by

1

f(x,y)u(y) dy for any u ∈ L2([0,1]),

(Tfu)(x) =

0

and the operator norm for f is then given by f op := min c ≥ 0 : Tfu 2 ≤ c u 2 for all u ∈ L2([0,1]) . As Tf is self-adjoint, its operator norm is equal to its spectral radius (see, e.g., [40, Thm. 12.25]).

The cut-norm on W is given by f := sup

f(x,y) dxdy

S,T⊂[0,1] S×T

= sup

f(x,y)u(x)v(y) dxdy ,

u,v: [0,1]→[0,1] [0,1]2

where the two suprema are equal since one only needs to consider {0,1}-valued u and v by the linearity of the integral. The second deﬁnition is useful for giving upper bounds using the cut-norm.

For any measure-preserving map σ: [0,1] → [0,1] and f ∈ W, deﬁne fσ ∈ W to be given by fσ(x,y) = f(σ(x),σ(y)). We deﬁne the cut-distance on W by

f − gσ

δ (f,g) = inf

σ

where σ ranges over all measure-preserving bijections on [0,1]. For the case of graphons this gives a pseudometric space (W0,δ ), which can be turned into a genuine metric space W0, equipped with the same cut-metric, by taking a quotient w.r.t. the equivalence relation f ∼ g iﬀ δ (f,g) = 0. The following theorem can be viewed as a topological interpretation of Szemere´di’s regularity lemma.

- Theorem 2.1 ([33]). The metric space ( W0,δ ) is compact.


It was shown in [4] that a sequence of graphs {Gn}n≥1 converges in the sense of subgraph densities if and only if the sequence of graphons fGn ∈ W0 converge in W0 w.r.t. the cut-distance. Equivalently, the topology on W0 induced by δ is the weakest topology that is continuous w.r.t. the subgraph densities t(H,·) for every H. This underlines one of the reasons making the cut-metric topology a natural choice for the space of graphons.

- 2.2. Graph parameters in the cut-metric topology. We shall focus on graph parameters whose extensions to the space of graphons behave well under the cut-metric topology. One example of such a graph parameter is the subgraph density t(H,·) for an arbitrary ﬁnite simple graph H, which was deﬁned in §2.1 directly on the full space of graphons such that t(H,G) = t(H,fG) for any graph G. A crucial feature of t(H,·) is being continuous w.r.t. the cut-metric ([4]), related to the existence of a “counting lemma” in the regularity lemma literature. This will be a prerequisite for applying the large deviations machinery of Chatterjee and Varadhan.


Deﬁnition 2.2. A nice graph parameter is a function τ : W0 → R that is continuous w.r.t. δ and such that every local extrema of τ w.r.t. L∞(W0) is necessarily a global extrema. We extend such a function τ to W0 in the obvious manner and further write τ(G) = τ(fG) for any graph G.

Another way to state the local extrema condition is that if f ∈ W0 is not a global maximum

(resp. minimum) of τ then for every ε > 0 there exists g ∈ W0 with f − g ∞ < ε and τ(g) > τ(f) (resp. τ(g) < τ(f)). This technical condition will later imply the continuity of the rate function.

Since the metric space ( W0,δ ) is compact and path-connected, the image of τ as above is a ﬁnite closed interval. In particular, its maximum is attained by a non-empty closed subset of W0.

- Example 2.3 (Subgraph density). For any ﬁxed ﬁnite simple graph H, the subgraph density t(H,·) is a nice graph parameter. As mentioned above, t(H,·) is continuous w.r.t. δ and in fact the map f  → t(H,f) is Lipschitz-continuous in the metric δ ([4, Theorem 3.7]). The local extrema condition is fulﬁlled since the function g+ = min{f + ε,1} satisﬁes t(H,g+) > t(H,f) unless t(H,f) = 1, and similarly g− = (1 − ε)f has t(H,g−) < t(H,f) unless t(H,f) = 0.


The next two examples are of graph parameters that do not meet the criteria of Deﬁnition 2.2.

- Example 2.4 (Frobenius norm). Let τ be the function that maps a weighted graph G on n vertices with adjacency matrix AG to the normalized Frobenius norm AG F /n. Then τ is discontinuous in ( W0,δ ) and therefore is not nice. Indeed, ﬁx 0 < p < 1 and let Gn ∼ G(n,p). The sequence Gn is known to converge in W0 almost surely to the constant graphon p (see [4, Theorem 4.5]), whose

Frobenius norm is p. In contrast to this limiting value, AGn F /n = fGn 2 →

√p almost surely.

- Example 2.5 (Max-cut). The function τ(G) = maxcut(G)/|V (G)|2 extends to W0 via


τ(f) = sup

f(x,y) dxdy .

U⊂[0,1] U×([0,1]\U)

Despite being continuous w.r.t. δ as well as monotone, the max-cut density is not nice. The continuity of τ follows from the fact |τ(f) − τ(g)| ≤ δ (f,g), as any cut for either f or g translates into a cut for the other with value diﬀering by at most δ (f,g). To see that τ does not satisfy the

local maxima condition, let f be the graphon deﬁned to be 1 on [0, 31] × [13,1] ∪ [31,1] × [0, 13] and 0 elsewhere. We have τ(f) = 29, induced by U = [0, 13]. This is not the global maximum for τ, which is 14 for the constant function 1. However, we claim that f is a local maximizer of τ with respect to the L∞-topology. By monotonicity, showing that τ(g) = 92 for the function g = min f + 12,1 will imply that τ(f0) ≤ τ(g) = τ(f) for any f0 with f0 − f ∞ ≤ 21. Indeed, if µ(U ∩ [0, 13]) = a and µ(U ∩ [13,1]) = b, where µ is Lebesgue measure, then the cut density induced by U for g is equal to

- 1

- 2a(13 −a)+ 12b(23 −b)+a(23 −b)+b(13 −a), which is maximized at (a,b) = (0, 23) and (a,b) = (31,0).


We will see in §3.2 (see Lemma 3.6) that, in contrast to the Frobenius norm, the spectral norm (the focus of Theorem 1.2) does behave well under the cut-metric topology, thus qualifying for an application of the large deviation theory of Chatterjee and Varadhan.

- 2.3. Large deviations for random graphs. A random graph Gn ∼ G(n,p) corresponds to the random point fGn ∈ W0, thus G(n,p) induces a probability distribution Pn,p on W0 supported on a ﬁnite set of points (graphs on n vertices). Recalling (1.1), we extend hp: [0,1] → R to W0 by


hp(f) :=

hp(f(x,y)) dxdy for any f ∈ W0.

[0,1]2

An important feature of hp is that it is a convex function on [0,1] and hence lower-semicontinuous on W0 with respect to the cut-metric topology ([8, Lem. 2.1]).

Using Szemere´di’s regularity lemma as well as tools from graph limits, Chatterjee and Varadhan [8] proved the following large deviation principle for random graphs.

- Theorem 2.6 ([8]). For each ﬁxed p ∈ (0,1), the sequence Pn,p obeys a large deviation principle in the space ( W0,δ ) with rate function hp. Explicitly, for any closed set F ⊆ W0,


- 1 n

- 2


log Pn,p(F) ≤ − inf f∈F

limsup

hp(f),

n→∞

and for any open U ⊆ W0,

- 1 n

- 2


log Pn,p(U) ≥ − inf f∈U

liminf

hp(f).

n→∞

The machinery developed by Chatterjee and Varadhan reduces the problem determining the large deviation rate function for dense random graphs to solving a variational problem on graphons. For any nice graph parameter τ : W0 → R, any p ∈ [0,1], and any t ∈ τ(W0), let

φτ(p,t) := inf {hp(f): f ∈ W0 , τ(f) ≥ t} . (2.1) Since hp is lower-semicontinuous on W0, the inﬁmum in (2.1) is always attained.

The following result was stated in [8, Thm 4.1 and Prop. 4.2] for the graph parameter τ = t(K3,·). We state its generalization to the class of nice graph parameters as per Deﬁnition 2.2.

- Theorem 2.7 (Variational problem). Let τ : W0 → R be a nice graph parameter and Gn ∼ G(n,p). Fix p ∈ (0,1) and t < max(τ). Let φτ(p,t) denote the solution to (2.1). Then


- 1 n

- 2


log P(τ(Gn) ≥ t) = −φτ(p,t). (2.2)

lim

n→∞

Let F∗ be the set of minimizers for (2.1) and let F∗ be its image in W0. Then F∗ is a non-empty compact subset of W0. Moreover, for each ε > 0 there exists C = C(τ,ε,p,t) > 0 so that for all n,

P δ (Gn, F∗) < ε τ(Gn) ≥ t ≥ 1 − e−Cn2 .

In particular, if F∗ = {f∗} for some f∗ ∈ W0 then the conditional distribution of Gn given the event τ(Gn) ≥ t converges to the point mass at f∗ as n → ∞.

Observe that by considering −τ (also a nice graph parameter) one obtains the same result for lower tail deviations. The intuition behind the second part of Theorem 2.7 is that the probability that δ (Gn, F∗) ≥ ε conditioned on τ(Gn) ≥ t can be again computed using Theorem 2.6 and shown to be exponentially smaller than that of the probability of the event τ(Gn) ≥ t.

The proof of Theorem 2.7 is a straightforward extension of the arguments of [8, Thm. 4.1] to nice graph parameters. A technical condition needed to complete the proof of Theorem 2.7 is given by the following lemma, key to which are the attributes of a nice graph parameter.

- Lemma 2.8. Let τ : W0 → R be a nice graph parameter. For any p ∈ (0,1), the map t  → φτ(p,t) is continuous on τ(W0).


Proof. Fix 0 < p < 1. By deﬁnition, t  → φτ(p,t) is non-decreasing. To prove left-continuity, consider a ∈ R. Since hp is lower-semicontinuous on W0, the set {f : hp(f) ≤ a} is closed in W0, thus also compact by the compactness of W0. Since τ is continuous on W0, the set {τ(f) : hp(f) ≤ a} is compact and in particular closed. Note that the latter is precisely the pre-image of (−∞,a] under the inverse of t  → φτ(p,t). As this pre-image is closed for any a ∈ R, left-continuity follows.

In order to prove right-continuity it suﬃces to show that for every t0 ∈ τ(W0) with t0 < max(τ) and every ε > 0 there exists some f ∈ W0 such that hp(f) < φτ(p,t0) + ε and τ(f) > t0. Indeed, since hp: [0,1] → R is uniformly continuous (for any ﬁxed p), there exists ε > 0 so that |hp(x) − hp(y)| < ε whenever |x − y| < ε . Let f0 be the minimizer of the variational problem (2.1) for t = t0. The local extrema condition in Deﬁnition 2.2 now implies that there is some f ∈ W0 with τ(f) > t0 and f − f0 ∞ < ε . Hence, hp(f) < hp(f0) + ε = φτ(p,t0) + ε, as desired.

3. The phase diagram for subgraph densities and the spectral radius

- 3.1. Subgraph density. In this section we prove Theorem 1.1, characterizing the phase diagram of upper tails (replica symmetry vs. symmetry breaking) of the density of a ﬁxed d-regular subgraph.


Establishing the replica symmetric phase will hinge on a generalized form of H¨lder’s inequality which appeared in [18]. We include its short proof for completeness.

- Theorem 3.1 (Generalized H¨lder’s inequality). Let µ1,...,µn be probability measures on Ω1,...,Ωn, resp., and let µ = ni=1 µi be the product measure on Ω = ni=1 Ωi. Let A1,...,Am be nonempty subsets of [n] = {1,...,n} and write ΩA = ∈A Ω and µA = ∈A µ . Let fi ∈ Lpi (ΩAi,µAi)


with pi ≥ 1 for each i ∈ [m] and suppose in addition that i: ∈A

### (1/pi) ≤ 1 for each ∈ [n]. Then m

i

m

1/pi

|fi|pi dµAi

|fi| dµ ≤

.

i=1

i=1

In particular, when pi = d for every i ∈ [m] we have mi=1 |fi| dµ ≤ |fi|d dµAi 1/d.

Proof. The proof carries by induction on n with the trivial base case of n = 0. By Fubini’s theorem,

m

|fi| dµ =

|fi|

|fi| dµ =

|fi| dµn

|fi| dµ[n−1] .

Ω

Ω i:n∈Ai

Ω[n−1] Ωn i:n∈Ai

i=1

i:n/∈Ai

i:n/∈Ai

where the argument of each fi is the restriction of x ∈ Ω to the coordinates of Ai, denoted by xAi. H¨lder’s inequality (along with Jensen’s inequality if i:n∈A

### (1/pi) is less than 1) implies that

i

1/pi

|fi|pi dµn

|fi| dµn ≤

,

Ωn i:n∈Ai

i:n∈Ai Ωn

1/pi

|fi|pi dµn

thus for each i with n ∈ Ai we can let fi∗ : Ω[n−1] → R denote the averaging map Ω

n

and obtain that

m

fi∗

|fi| dµ ≤

|fi| dµ[n−1] .

Ω

Ω[n−1] i:n∈Ai

i=1

i:n/∈Ai

Now, the functions fi∗ correspond to A∗i = Ai \ {n} and therefore, thanks to the assumption that i: ∈Ai(1/pi) ≤ 1 for each ∈ [n − 1] we can apply the induction hypothesis and infer that

m

1/pi

1/pi

(fi∗)pi dµ[n−1]

|fi|pi dµ[n−1]

|fi| dµ ≤

Ω

i:n∈Ai Ω[n−1]

i:n/∈Ai Ω[n−1]

i=1

m

1/pi

|fi|pi dµ

=

,

i=1 Ω

- as required.


It is helpful to compare Theorem 3.1 with the standard H¨lder’s inequality for the case where pi = d for all i. A direct application of H¨lder’s inequality produces the inequality fi 1 ≤

i fi m, whereas Theorem 3.1 exploits the extra assumption that #{i : ∈ Ai} ≤ d for all ∈ [n] and gives the stronger inequality fi 1 ≤ i fi d. For instance,

2

fi(x,y)2 dxdy .

≤

f1(x,y)f2(y,z)f3(x,z) dxdydz

i

Placing this in the context of subgraph densities, as an immediate corollary of Theorem 3.1 (in the special case that pi = d for all i) we have the following inequality.

- Corollary 3.2. Let H be a graph whose maximum degree is at most d, and let f ∈ W. Then


t(H,f) ≤ f ed(H) .

Recall that Theorem 2.7 reduces the problem of ﬁnding the phase boundary to determining whether the constant function r is a solution for the variational problem of minimizing hp(f) over f ∈ W0 subject to t(H,f) ≥ re(H), where H is some ﬁxed graph. In light of the above corollary, it is important to estimate hp(f) for functions f ∈ W0 with f d = r, as addressed next.

- Lemma 3.3. Let 0 < p < 1 and let f ∈ W0. Suppose that d ≥ 1 and 0 < r < 1 are such that the point (rd,hp(r)) lies on the convex minorant of x  → hp(x1/d). If in addition either


- (a) p < r < 1 and f d ≥ r, or
- (b) 0 < r < p and f d ≤ r, then hp(f) ≥ hp(r), with equality occurring if and only if f ≡ r.


1 − a − b I0

r

r1 r2

r a b

r r

I1 I2

hp(x1/d)

(1 − s) s  

r1d rd r2d

x

Figure 5. The construction in Lemma 3.4. Proof. Let ψ(x) = hp(x1/d) and let ψˆ be the convex minorant of ψ. By Jensen’s inequality, hp(f) = ψ(f(x,y)d) dxdy ≥ ψ ˆ(f(x,y)d) dxdy ≥ ψˆ f(x,y)d dxdy = ψˆ f dd = hp( f d).

The fact that hp(x) is decreasing along [0,p] and increasing along [p,1] (see §A) implies that under either of the assumptions in Part (a) and Part (b) we have hp( f d) ≥ hp(r), hence hp(f) ≥ hp(r). Since ψˆ is not linear in any neighborhood of rd, equality can occur if and only if f = r.

The ﬁnal element needed for the proof of Theorem 1.1 is a construction that outperforms the constant graphon in the symmetry breaking regime. This is achieved by the following lemma.

- Lemma 3.4. Let H be a d-regular graph. Fix 0 < p ≤ r < 1 so that (rd,hp(r)) is not on the convex minorant of x  → hp(x1/d). Then there exists f ∈ W0 with t(H,f) > re(H) and hp(f) < hp(r).


Proof. Since (rd,hp(r)) does not lie on the convex minorant of x  → hp(x1/d), there necessarily exist 0 ≤ r1 < r < r2 ≤ 1 such that the point (rd,hp(r)) lies strictly above the line segment joining (r1d,hp(r1)) and (r2d,hp(r2)). Letting s be such that

rd = sr1d + (1 − s)r2d , we therefore have

shp(r1) + (1 − s)hp(r2) < hp(r). (3.1) Let ε > 0 and deﬁne

a = sε2 , b = (1 − s)ε2 + ε3 ,

I0 = [a,1 − b], I1 = [0,a], I2 = [1 − b,1], noting that for a < 1 − b for any suﬃciently small ε. Deﬁne fε ∈ W0 by

 

- r1 if (x,y) ∈ (I0 × I1) ∪ (I1 × I0),
- r2 if (x,y) ∈ (I0 × I2) ∪ (I2 × I0), r otherwise.


fε(x,y) =

 (See Fig. 5 for an illustration of this construction.) We claim that t(H,fε) − re(H) = v(H) a(r1d − rd) + b(r2d − rd) re(H)−d + O(ε4). (3.2)

Indeed, the only embeddings of H that have values diﬀerent from re(H) are those where at least one vertex of H is mapped to I1 ∪I2. Since a and b are both O(ε2), in order to compute t(H,fε)−re(H)

up to an O(ε4) error we need only consider embeddings of H where precisely one vertex gets mapped to I1∪I2. Denote this vertex of H by u, and observe that if u is mapped to I1 then the contribution to t(H,fε) − re(H) is (r1d − rd)re(H)−d since H is d-regular. Similarly, if u is mapped to I2 then the contribution is (r2d − rd)re(H)−d. Putting everything together yields (3.2).

By deﬁnition of a,b and s we have a(r1d − rd) + b(r2d − rd) = sε2(r1d − rd) + ((1 − s)ε2 + ε3)(r2d − rd) = ε3(r2d − rd).

Recalling that r2 > r and plugging the last equation in (3.2) it now follows that t(H,fε) > re(H) for any suﬃciently small ε > 0. At the same time, we also have

hp(fε) − hp(r) = 2a(1 − a − b)(hp(r1) − hp(r)) + 2b(1 − a − b)(hp(r2) − hp(r)) = 2(1 − a − b)(ahp(r1) + bhp(r2) − (a + b)hp(r))

= 2(1 − a − b)ε2 (shp(r1) + (1 − s)hp(r2) − hp(r) + (hp(r2) − hp(r))ε) . Revisiting (3.1) we conclude that hp(fε) < hp(r) for any suﬃciently small ε > 0.

We now have all the ingredients needed for establishing the phase diagram of upper tail deviations for subgraph densities.

- Proof of Theorem 1.1. For Part (i), by applying Theorem 2.7 to the graph parameter t(H,·), it suﬃces to show that the constant function r is the unique element f ∈ W0 minimizing hp(f)


subject to t(H,F) ≥ re(H). Indeed, by Corollary 3.2, t(H,F) ≥ re(H) implies that f d ≥ r, and by Lemma 3.3 Part (a), hp(f) ≥ hp(r) with equality if and only if f is the constant function r.

To prove Part (ii), let F∗ ⊂ W0 be the set of minimizers for the variational problem (2.1) with the graph parameter t(H,·). Then F∗ does not contain the constant function r by Lemma 3.4, nor does it contain any constant function of value r = r (when r > r one has hp(r ) > hp(r), whereas if r < r then t(H,f) < re(H)). Let C ⊂ W0 be the set of constant graphons. Since F∗ and C are disjoint and both are compact, δ (F∗, C) > 0. The desired result follows from applying Theorem 2.7 with ε = δ (F∗, C)/2.

When d = 2, the phase boundary is explicitly given by Lemma A.2, thus concluding the proof. One can also ask what the phase diagram is for lower tail deviations of subgraph densities. We

next show that for certain bipartite graphs there is replica symmetry everywhere for lower tails.

- A beautiful conjecture of Erd˝s and Simonovits [42] and Sidorenko [41] (from here on referred


to as Sidorenko’s conjecture) states that every bipartite graph H satisﬁes t(H,G) ≥ t(K2,G)e(H) for every graph G. The conjecture was veriﬁed for various graphs H (e.g., trees, even cycles [41], hypercubes [25], bipartite graphs with one vertex complete to the other part [11]). As it turns out, for any such graph H the lower tail deviations are always replica symmetric (no phase transition).

Proposition 3.5. Fix 0 < r ≤ p < 1, let Gn ∼ G(n,p) be the Erd˝os-Re´nyi random graph and let H be a ﬁxed bipartite graph for which Sidorenko’s conjecture holds. Then

- 1 n

- 2


log P t(H,Gn) ≤ re(H) = −hp(r) and furthermore, for every ε > 0 there exists some constant C = C(H,ε,p,r) > 0 such that

lim

n→∞

P δ (Gn,r) < ε t(H,Gn) ≤ re(H) ≥ 1 − e−Cn2 . Proof. Applying Theorem 2.7 with −t(H,·), it suﬃces to show that the constant function r is the unique element f ∈ W0 minimizing hp(f) subject to t(H,f) ≤ re(H). Since H satisﬁes Sidorenko’s conjecture, t(H,f) ≥ f e1(H) for all f ∈ W0. Thus, if t(H,f) ≤ re(H) then f 1 ≤ r, and so by

- Lemma 3.3 Part (b) (applied to the case d = 1, noting that then hp(x1/d) is itself convex) we have hp(f) ≥ hp(r) with equality if and only if f is the constant function r.


- 3.2. Largest eigenvalue. In this section we prove Theorem 1.2, addressing the phase boundary for large deviations in the spectral norm. The proof will follow a similar route as the previous section, yet ﬁrst we must show that the spectral norm is a nice graph parameter.


For a graph G on n vertices, let λ1(G) be the largest eigenvalue of its adjacency matrix AG. Since AG is symmetric, λ1(G) = AG op, and therefore over W we have fG op ≥ λ1(G)/n. It is easy to verify (see Lemma 3.6 below) that in fact fG op = λ1(G)/n, thus the operator norm on W is the graphon extension of the (normalized) largest eigenvalue. Furthermore, as we show below,  · op is (uniformly) continuous w.r.t. the cut-metric, and the local extrema condition in Deﬁnition 2.2 is satisﬁed as well, thus  · op is a nice graph parameter.

- Lemma 3.6. The function  · op is a continuous extension of the normalized graph spectral norm, i.e., λ1(G)/n for a graph G on n vertices, to ( W0,δ ). Moreover,  · op is a nice graph parameter.


Proof. We ﬁrst show that f op = λ1(G)/n for any graph G on n vertices. Clearly, the largest eigenvector of AG, the adjacency matrix of G, can be turned into a step function u: [0,1] → R such that TfGu = (λ1(G)/n)u, and so fG op ≥ λ1(G)/n. Conversely, for any u: [0,1] → R we consider the step function un: [0,1] → R such that for any 1 ≤ i ≤ n, on the interval (i−n1, ni ] it is equal to the average of u over that interval. Let v ∈ Rn be the vector of values of un. Since fG is constant in every box (i−n1, ni ] × (j−n1, nj ], we have

Tfu 2 = Tfun 2 = AGv 2 /n2 ≤ λ1(G) v 2 /n2 = λ1(G) un 2 /n ≤ λ1(G) u 2 /n, where the last inequality is due to convexity. It follows that f op = λ1(G)/n.

Next, we will argue that

f 4op ≤ 4 f for any symmetric measurable f : [0,1]2 → [−1,1]. (3.3) Let u ∈ L2([0,1]) with u 2 = 1. By Cauchy-Schwarz we can infer that

2

2

2

Tfu 42 = f(x,y)u(y) dy

dx

= f(x,y)f(x,y )u(y)u(y ) dxdydy

≤ f(x,y)f(x,y ) dx

2

dydy u(y)2u(y )2 dydy .

= f(x,y)f(x,y )f(x ,y)f(x ,y ) dxdx dydy . For any ﬁxed x ,y we can let vy (x) = f(x,y ) and wx (y) = f(x ,y), thus rewriting the above as f(x,y)vy (x)wx (y) dxdy f(x ,y ) dx dy ≤ 4 f , with the last inequality justiﬁed by the fact that for any g ∈ W and v,w: [0,1] → [−1,1] we have

g(x,y)v(x)w(y) dxdy ≤ 4 g by the deﬁnition of the cut-norm, thereby establishing Eq. (3.3). (The factor of 4 above was due to splitting v,w into positive and negative parts. Indeed, for f : [0,1]2 → [0,1] the bound in (3.3) remains valid without the factor of 4 in the right-hand side.)

Consider f,g ∈ W0 and let σ vary over all measure-preserving bijections on [0,1]. We then have f op − g op ≤ inf

√

√

f − gσ 1/4 =

f − gσ op ≤

2δ (f,g)1/4 ,

2inf

σ

σ

thus implying that  · op is uniformly continuous in ( W0,δ ).

Finally, we need to verify the local extrema condition in Deﬁnition 2.2. Let f ∈ W0. There are no local non-global minima since (1 − ε)f op = (1−ε) f op < f op unless f op = 0 already. In addition, we claim that g = min{f + ε,1} satisﬁes g op > f op unless f op = 1 already. Indeed,

take some u ∈ L2([0,1]) which is nonzero (a.e.) and satisﬁes u ≥ 0 and Tfu = f op u. It suﬃces to show that Tgu > Tfu on some subset of [0,1] with positive measure. Let A = {x ∈ [0,1] : u(x) > 0} be the support of u, which by our choice has positive Lebesgue measure µ(A) > 0. If µ(A) < 1 then Tfu = u = 0 (a.e.) on Ac := [0,1] \ A, so that f = 0 on Ac × A. Hence, g = ε on Ac × A and Tgu = ε u 1 > 0 = Tfu on Ac, as desired. Suppose therefore that µ(A) = 1. If f op < 1 we must have g > f on a subset of positive measure, and hence also Tgu > Tfu on a subset of positive measure, as u has full support. This shows that f cannot be a local maximum unless f op = 1.

In light of the above lemma, the variational problem under consideration in Theorem 1.2 becomes

inf{hp(f) : f ∈ W0, f op ≥ r}. (3.4) We will need the following straightforward inequality relating the operator norm,  · 1 and  · 2.

- Lemma 3.7. For every f ∈ W0 we have f 1 ≤ f op ≤ f 2. Proof. For the left inequality, observe that since f ≥ 0 we have that

f 1 = Tf1 1 ≤ Tf1 2 ≤ f op . For the right inequality in the statement of the lemma, let u: [0,1] → R. By Cauchy-Schwarz,

Tfu 22 = f(x,y)u(y) dy

2

dx ≤ f(x,y)2 dydx u(y)2 dy = f 22 u 22 , and therefore f op ≤ f 2, as claimed.

The following lemma is the operator norm analogue of Lemma 3.4, providing a construction that beats the constant graphon in the symmetry breaking regime.

- Lemma 3.8. Let 0 < p ≤ r < 1 be such that (r2,hp(r)) does not lie on the convex minorant of x  → hp(√x). Then there exists some f ∈ W0 with f op > r and hp(f) < hp(r).


Proof. Let ε > 0. Let fε be the construction from the proof of Lemma 3.4 with d = 2, and deﬁne the parameters of that construction r1,r2,s,a,b,I0,I1,I2 as given there. Having already demonstrated that hp(fε) < hp(r) for any small enough ε > 0, it remains to show that fε op > r. To this end, it suﬃces to exhibit a function u ∈ L2([0,1]) such that (Tfεu)(x) > ru(x) for all x ∈ [0,1]. Let

 

- (1 − a − b)r1 if x ∈ I1 ,
- (1 − a − b)r2 if x ∈ I2 , r if x ∈ I0 .


u(x) =



Recall that fε(x,y) is r except when (x,y) ∈ (I0 × Ii) ∪ (Ii × I0) where it is ri for i = 1,2. It now follows that for every x ∈ I1 = [0,a]

(Tfεu)(x) = a(1 − a − b)r1r + b(1 − a − b)r2r + (1 − a − b)r1r > (1 − a − b)r1r = ru(x). Similarly, for any x ∈ I2 = [1 − b,1] we have

(Tfεu)(x) > (1 − a − b)r2r = ru(x). Finally, if x ∈ I0 = [a,1 − b] then

(Tfεu)(x) = a(1 − a − b)r12 + b(1 − a − b)r22 + (1 − a − b)r2 = (1 − a − b)(r2 + ar12 + br22). Plugging in the facts that r2 = sr12 + (1 − s)r22 while a = sε2 and b = (1 − s)ε2 + ε3, we get that

(Tfεu)(x) = (1 − ε2 − ε3)(r2 + r2ε2 + r22ε3) = r2 + (r22 − r2)ε3 + O(ε4) > r2 = ru(x), where the strict inequality is valid for any suﬃciently small ε > 0 since r2 > r.

Altogether, (Tfεu)(x) > ru(x) for all x ∈ [0,1] and so f op > r, as required.

- Proof of Theorem 1.2. To prove Part (i), by Theorem 2.7 applied to the graph parameter  · op it suﬃces to show that the constant function r is the unique element f ∈ W0 minimizing hp(f) subject to f op ≥ r. Indeed, by Lemma 3.7, f 2 ≥ f op ≥ r. By Lemma 3.3 Part (a) and Lemma A.2 we know that hp(f) ≥ hp(r), with equality if and only if f is the constant function r.


For Part (ii), similar to the proof of Part (ii) of Theorem 1.1 in §3.1, Lemma 3.8 implies that the set of minimizers of the variational problem (2.1) is disjoint from the set of constant graphons. We then apply Theorem 2.7 to conclude the proof, with the phase boundary given by Lemma A.2.

The behavior of the lower tails deviations in the spectral norm is similar to that of the subgraph densities in Proposition 3.5, where replica symmetry is exhibited everywhere (no phase transition). Proposition 3.9. Let 0 < r ≤ p < 1. Let Gn ∼ G(n,p) be the Erd˝os-Re´nyi random graph and let λ1(Gn) denote the largest eigenvalue of its adjacency matrix. Then

lim

n→∞

- 1 n

- 2


log P(λ1(Gn) ≤ r) = −hp(r)

and furthermore, for every ε > 0 there is some C = C(ε,p,r) > 0 such that for all n, P(δ (Gn,r) < ε | λ1(Gn) ≤ nr) ≥ 1 − e−Cn2 .

Proof. Applying Theorem 2.7 with τ = − · op, it suﬃces to show that the constant function r is the unique element f ∈ W0 minimizing hp(f) subject to f op ≤ r. By Lemma 3.7, if f ∈ W0 with f op ≤ r then f 1 ≤ f op ≤ r. It now follows from Lemma 3.3 Part (b) (used with d = 1 bearing in mind that hp(x) is convex) that hp(f) ≥ hp(r) with equality if and only if f ≡ r.

4. Exponential random graph models

Let us review the tools developed by Chatterjee and Diaconis [7] to analyze exponential random graphs. Deﬁne

h(x) := xlog x + (1 − x)log(1 − x) for x ∈ [0,1], and for any graphon f ∈ W0 let

h(f) :=

h(f(x,y)) dxdy .

[0,1]2

The following result from [7, Thm. 3.1 and Thm. 3.2] reduces the analysis of the exponential random graph model in the large n limit to a variational problem. It was proven with the help of the theory developed by Chatterjee and Varadhan [8] for large deviations in random graphs.

- Theorem 4.1 (Chatterjee and Diaconis [7]). Let τ : W0 → R be a bounded continuous function. Let Zn = G exp n2 τ(G) where the sum is taken over all 2(n2) simple graphs G on n labeled vertices. Let ψn = n2 −1 log Zn. Then


(τ(f) − h(f)), (4.1)

ψ := lim

ψn = sup

n→∞

f∈ W0

and the set F∗ ⊂ W0 of maximizers of this variational problem is nonempty and compact. Let Gn be a random graph on n vertices drawn from the exponential random graph model deﬁned

by τ, i.e., with distribution Zn−1 exp n2 τ(·) . Then for every η > 0 there exists C = C(τ,η) > 0 such that for all n,

P(δ (Gn,F∗) > η)) ≤ e−Cn2 .

We say that the exponential random graph model has replica symmetry if the set of maximizers F∗ for the variational problem τ(f)−h(f) contains only constant functions, and we say that it has replica symmetry breaking if no constant function is a maximizer. Intuitively, Theorem 4.1 implies that when there is replica symmetry, for large n, the random graph behaves like an Erd˝s-R´enyi random graph (or a mixture of Erd˝s-R´enyi random graphs), while this is not the case when there is broken symmetry. More precisely we have the following result (see [7, Thm. 6.2]).

- Corollary 4.2. Continuing with Theorem 4.1. Let C ⊂ W0 be the set of constant functions. If F∗ ∩ C = ∅ then there exist C,ε > 0 such that for all n,


P(δ (Gn, C) > ε) ≥ 1 − e−Cn2 . To prove Theorem 1.3 using the above tools, we need to analyze the following variational problem: sup

(β1t(K2,f) + β2t(H,f)α − h(f)). (4.2) Here is the main result of this section, from which Theorem 1.3 follows by the results above.

f∈ W0

- Theorem 4.3. Let H be a d-regular graph (d ≥ 2) and ﬁx β1 ∈ R and α,β2 > 0. Let E denote the corresponding exponential random graph model on n labeled vertices as speciﬁed in (1.4).


- (a) If α ≥ d/e(H), then E has replica symmetry. Moreover, there exists a set Γ ⊂ R2 of the form Γ = {(β1,ϕ(β1)) : β1 < log(e(H)α − 1) − e(eH(H)α)α−1} ⊂ R2 for some function ϕ : R → R

such that when (β1,β2) ∈ R × (0,∞) \ Γ the set of maximizers of the variational problem (4.2) is a single constant function, and when (β1,β2) ∈ Γ the set of maximizers consists of exactly two distinct constant functions.

- (b) If 0 < α < d/e(H) and β1 ≥ log(d−1)−d/(d−1) then E has replica symmetry. Moreover, the variational problem (4.2) is maximized by a unique constant function.
- (c) If 0 < α < d/e(H) and β1 < log(d − 1) − d/(d − 1) then there exists an open interval of values β2 > 0 for which E has broken symmetry, i.e., the set of maximizers of the variational problem (4.2) does not contain any constant function. Furthermore, this open interval can be taken to be (β2,β2) with β2 = u1−e(H)αh p(u)/(e(H)α) and β2 = u1−e(H)αh p(u)/(e(H)α), where (ud,hp(u)) and (ud,hp(u)) are the two points where the lower common tangent of x  → hp(x1/d) touches the curve for p = 1/(1 + e−β1).


When restricted only to constant functions in W0, the variational problem (4.2) becomes the one-dimensional optimization problem

(β1u + β2ue(H)α − h(u)). (4.3)

sup

0≤u≤1

Note that for both (4.2) and (4.3) the supremum is in fact a maximum due to compactness. Let u∗ be the maximizer for (4.3). When there is replica symmetry, the maximum values attained in (4.2) and (4.3) are equal, and the exponential random graph behaves like an Erd˝s-R´enyi random graph with edge density u∗. It is possible that there are two distinct maximizers u∗, in which case the model behaves like a (possibly trivial) distribution over two separate Erd˝s-Re´nyi models. In the work of Chatterjee and Diaconis [7], where the α = 1 case was considered, it was shown that u∗ as a function of (β1,β2) experiences a discontinuity across a curve in the parameter space. Radin and Yin [38] later showed that (when α = 1) the limiting free energy density ψ from (4.1), as a function in the parameter space (β1,β2), is analytic except on a ﬁrst order phase transition curve ending in a critical point with second order phase transition. (See Fig. 3 in §1 for a plot of the location of the discontinuity in the (β1,β2)-phase diagram.)

Here we focus less on the discontinuity of u∗ and more on symmetry breaking. Nevertheless we shall start our analysis by giving a simple geometric interpretation of the discontinuity of u∗.

hp(x1/(e(H)α))

((u∗)e(H)α,hp(u))

The critical slope β2 when there are two distinct u∗

β2

Figure 6. Discontinuity in the symmetric solution u∗ due to the geometry of x  → hp(x1/(e(H)α)).

By deﬁnition,

p

hp(x) = h(x) − xlog

1 − p − log(1 − p). Setting

1 1 + e−β1 ,

p =

so that β1 = log 1−pp, we absorb the linear term in (4.2) and (4.3) into the entropy term, at which point these two optimization problems respectively become

(β2t(H,f)α − hp(f) − log(1 − p)) (4.4)

sup

f∈ W0

and

(β2ue(H)α − hp(u) − log(1 − p)). (4.5) By a change of variables u = x1/(e(H)α) in (4.5) we get the equivalent optimization problem

sup

0≤u≤1

(β2x − hp(x1/(e(H)α)) − log(1 − p)). (4.6)

sup

0≤x≤1

Observe that x = x∗ maximizes (4.6) iﬀ the tangent to the curve deﬁned by x  → hp(x1/(e(H)α)) at x = x∗ has slope β2 and lies below the curve. Thanks to Lemma A.1 from the appendix, we know that x  → hp(x1/γ) is convex if 0 < γ ≤ 1 or if

γ − 1 γ − 1 + eγ/(γ−1) . (4.7)

γ > 1 and p ≥ p0(γ) :=

Otherwise, hp(x1/γ) has exactly two inﬂection points to the right of x = pγ, so that the curve starts convex, becomes concave, and ﬁnally turns convex again. In addition, hp(x1/γ) has an inﬁnite slope at both endpoints. For any β2 ∈ R, there is a unique lower tangent of slope β2 to the curve hp(x1/(e(H)α)), touching the curve at x = x∗ = (u∗)e(H)α. As β2 varies, u∗ increases continuously with β2, except in the situation where the curve of hp(x1/(e(H)α)) is not convex and β2 is the slope of the unique lower tangent that touches the curve at two points. In that case, (4.5) is optimized

- at two distinct values of u, denoted by 0 < u < u < 1, and as β2 increases through this critical point, u∗ jumps over the interval (u,u) corresponding to the part of the curve lying above the convex minorant, then increases continuously afterwards. When hp(x1/(e(H)α)) is convex, this jump


does not occur. See Fig. 6 for an illustration of this process (the function hp(x1/(e(H)α)) is plotted not-to-scale in order to highlight its features). The uniqueness of u∗ is stated below as a lemma.

H = K3, α = 1

H = K3, α = 0.6

- 0
- 1


- 0
- 1


B3

symmetry broken in the shaded region

#### u∗

#### u∗

trajectory of (p,u∗) as β2 , β1 ﬁxed

B1.8

0 p 1

0 p 1

Figure 7. Discontinuity in the symmetric solution u∗ as reﬂected in the (p,u)-phase diagram.

- Lemma 4.4. If 0 < e(H)α ≤ 1 or if e(H)α > 1 and p ≥ p0(e(H)α) as deﬁned in (4.7), then the optimization problem (4.3) is a maximized at a unique value of u. Otherwise, (4.3) is maximized at a unique u except for a single value of β2, where the maximum is attained at two distinct u’s.


We can also represent this jump of u∗ in the (p,u)-phase diagram as follows. For each γ > 0, consider the region Bγ ⊂ [0,1]2 containing all points (p,u) such that (uγ,hp(u)) does not lie on the convex minorant of x  → hp(x1/γ). When γ < 1 the region Bγ is empty, but otherwise it is nonempty. The geometric argument in the previous paragraph shows that u can never appear as a maximizer to (4.5) if (p,u) ∈ Be(H)α, but all other values of u can. Thus, for a ﬁxed p = 1/(1 + e−β1), as β2 increases from −∞ to ∞, the point (p,u∗) moves up continuously from 0 in the (p,u)-phase diagram, and jumps over Be(H)α as it reaches it. Thereafter it resumes moving up until hitting 1. This process is illustrated on the left of Fig. 7 when e(H)α = 3, e.g., when H = K3 and α = 1.

Turning to large deviations, we know from Lemma 3.4 that there is broken symmetry for the

density of copies of a d-regular graph H whenever we are in Bd. It turns out that the same is true for the corresponding exponential random graph model given in (1.4). As we just saw though,

one must remove Be(H)α from the possible solution space for (p,u∗). Whenever γ < γ we have

- Bγ ⊂ Bγ (see Lemma A.5), and consequently, if e(H)α ≥ d then Be(H)α covers Bd and so the entire symmetry breaking phase is removed, leaving replica symmetry everywhere. This agrees with the results of Chatterjee and Diaconis [7] for the case α = 1. However, when e(H)α < d it is possible to have (p,u∗) ∈ Bd, in which case the construction from Lemma 3.4 breaks the symmetry. This is shown on the right of Fig. 7 for the case d = 2 and e(H)α = 1.8, e.g., for H = K3 and α = 0.6.


- Proof of Theorem 4.3. The proof of Part (a) is essentially the same as the proof of Theorem 4.1 in the work of Chatterjee and Diaconis [7], except now we use the generalized H¨lder’s inequality (Theorem 3.1) instead of the usual H¨lder’s inequality.


Suppose that α ≥ d/e(H). We ﬁrst need to show that in this case the only maximizers for the variational problem (4.4) are constant functions. Applying Corollary 3.2, for any f ∈ W0 we have

β2t(H,f)α − hp(f) ≤ β2 f ed(H)α − hp(f) ≤ β2 f ee((HH))αα − hp(f), where the last inequality used the assumption on α. This in turn is equal to

(β2f(x,y)e(H)α − hp(f(x,y))) dxdy ≤ sup

0≤u≤1

β2ue(H)α − hp(u),

showing that the β2t(H,f) − hp(f) is indeed maximized at constant functions. Furthermore, when β2ue(H)α −hp(u) is maximized at a unique u∗, then equality holds in place of the above inequalities only for the constant function f = u∗. An additional argument is needed to treat the case when β2ue(H)α − hp(u) is maximized at two distinct values. Either by checking the equality conditions in the proof of Theorem 3.1, or by referring to [18], we know that equality in Corollary 3.2 occurs if and only if f(x,y) = g(x)g(y) for some function g: [0,1] → [0,∞). It can then be easily checked that equality in the above sequence of inequalities can only occur when f is a constant function. The value of this constant u∗ is given by the optimization problem (4.5) and its the uniqueness is addressed in Lemma 4.4.

We now turn to prove Part (b). Since β1 ≥ log(d − 1) − d/(d − 1), p =

d − 1 d − 1 + ed/(d−1) = p0(d).

1 1 + e−log(d−1)+d/(d−1) =

1 1 + e−β1 ≥

By Lemma A.1, x  → hp(x1/d) is convex for this value of p. Hence, hp(f) ≥ hp( f d) by Jensen’s inequality with equality if and only if f is a constant function. Since t(H,f) ≤ f d by Corollary 3.2,

β2t(H,f)α − hp(f) ≤ β2 f ed(H)α − hp( f d) ≤ sup

(β2ue(H)α − hp(u)),

0≤u≤1

with equality iﬀ f is the constant function equal to u∗, the unique maximizer of β2ue(H)α − hp(u). The uniqueness of u∗ follows from Lemma 4.4 together with noting that when e(H)α > 1 we have p ≥ p0(d) > p0(e(H)α) as d > e(H)α and p0(·) is increasing in [1,∞).

It remains to prove Part (c). We have 0 < p < p0(d). Let 0 < u < u < 1 be such that the lower common tangent to x  → hp(x1/d) touches the curve at x = ud and ud. Since e(H)α < d, Lemma A.5 implies that the points (ue(H)α,hp(u)) and (ue(H)α,hp(u)) both lie on the convex minorant of x  → hp(x1/(e(H)α))) and do not lie on the common lower tangent (if there is one). Let β2 and β2 be as in the theorem statement, observing that these are the values of the derivative of hp(x1/(e(H)α)) at x = ue(H)α and ue(H)α, respectively. Then for any β ∈ (β2,β2), using the slope interpretation of β2 given in the discussion proceeding this proof, we see that the optimization problem (4.5) is maximized for some u∗ ∈ (u,u). At the same time, by Lemma 3.4 there exists some f ∈ W0 such that t(H,f) > (u∗)e(H) and hp(f) < hp(u∗). It follows that

(β2t(H,f)α − hp(f)) > β2(u∗)e(H)α − hp(u∗) = sup

(β2ue(H)α − hp(u)),

sup

0≤u≤1

f∈ W0

and hence β2t(H,f)α − hp(f) is not maximized at any constant function.

5. Densities of linear hypergraphs in random hypergraphs

In this section, we extend our results to densities of linear hypergraphs in random hypergraphs. Homomorphisms and densities are deﬁned as in graphs. Similarly, for any r ∈ [0,1] let

1 |V (G)|k

eG(A1,...,Ak) − r |A1|···|Ak|

δ (G,r) := sup

A1,...,Ak⊂V (G)

where eG(A1,...,Ak) is the number of (ordered) hyperedges of the form (a1,...,ak) ∈ A1×···×Ak. The main result in this section is the following:

- Theorem 5.1. Fix d,k ≥ 2 and 0 < p ≤ r < 1. Let H be a d-regular k-uniform linear hypergraph. Let Gn ∼ G(k)(n,p) be the random k-uniform hypergraph on n vertices with hyperedge probability p.


- (i) If the point (rd,hp(r)) lies on the convex minorant of the function x  → hp(x1/d) then


1

log P t(H,Gn) ≥ re(H) = −hp(r)

lim

n k

n→∞

and furthermore, for every ε > 0 there exists some constant C = C(H,ε,p,r) > 0 such that P δ (Gn,r) < ε t(H,Gn) ≥ re(H) ≥ 1 − e−Cnk .

- (ii) If the point (rd,hp(r)) does not lie on the convex minorant of the function x  → hp(x1/d) then


1

log P t(H,Gn) ≥ re(H) > −hp(r)

lim

n k

n→∞

and furthermore, there exist ε,C > 0 such that P inf δ (Gn,s) : 0 ≤ s ≤ 1 > ε t(H,Gn) ≥ re(H) ≥ 1 − e−Cnk . In particular, when d = 2, case (ii) occurs if and only if p < 1 + (r−1 − 1)1/(1−2r) −1.

Let k ≥ 2 be an integer and let W(k) be the space of all bounded measurable functions [0,1]k → R that are symmetric (i.e., f(x1,x2,...,xk) = f(xπ(1),xπ(2),...,xπ(k)) for any permutation π of [k] = {1,2,...,k}). Let W0(k) denote all symmetric measurable functions [0,1]k → [0,1]. Every k-uniform hypergraph G corresponds to a point fG ∈ W0(k) similar to the case for graphs. As before, we can endow W with usual Lp-norm and in addition have the following cut norm:

f(x1,...,xk) dx1 ···dxk .

f := sup

S1,...,Sk⊂[0,1] S1×···×Sk

This gives rise to the cut distance: for any f,g ∈ W0(k), δ (f,g) := inf

f − gσ

σ

where σ ranges over all measure-preserving bijections on [0,1], and gσ ∈ W0(k) is deﬁned by gσ(x1,...,xk) = g(σ(x1),...,σ(xk)). Let W0(k) be the metric space formed by taking equivalences of points in W0(k) with zero cut-distance.

The space W0(k) is a straightforward generalization of the space W0 of graphons. Unfortunately, it does not fully capture the richness of the structure of hypergraphs. This notion is closely related to some initial attempts at generalizing Szemer´edi’s regularity lemma to hypergraphs (e.g., [10]). The main issue is that while the regularity lemma generalizes easily to this setting, there is no corresponding counting lemma for embedding a ﬁxed hypergraph H unless H is linear (recall that a hypergraph is linear if every pair of vertices is contained in at most one hyperedge). The diﬃculty in extending the results to general H is related to the intricacies of hypergraph regularity (see, e.g., Gowers [23] and Nagle, R¨dl, Schacht, and Skokan [35, 39], as well as the recent progress in this direction by Elek and Szegedy [16, 17]). Here we restrict ourselves to the basic setting above which suﬃces for controlling densities of linear hypergraphs.

For any f ∈ W(k) and any k-uniform hypergraph H, write V (H) = [m] and deﬁne t(H,f) =

f(xi1,...,xik) dx1 ···dxm .

[0,1]k {i1,...,ik}∈E(H)

The Chatterjee-Varadhan theory can be generalized to derive rate functions for large deviations of H-counts, where H is a ﬁxed linear hypergraph. We outline the modiﬁcations and omit the complete details, as the changes required in the original proofs are mostly straightforward.

We start with a statement generalizing the weak regularity lemma of Frieze and Kannan [19]. The analytic form of this statement for graphs can be found in Lov´sz and Szegedy [34, Lem. 3.1].

- Theorem 5.2. For every ε > 0 there exists some M(ε) > 0 such that for every f ∈ W0(k) there exist some m ≤ M(ε) and some g ∈ W0(k) with δ (f,g) ≤ ε, and such that g is constant in each box (i1m−1, mi1 ] × ··· × (ikm−1, mik].


Using Theorem 5.2, the proof of Lov´sz and Szegedy [34, Thm. 5.1] can be modiﬁed to give the following topological interpretation of this result.

- Theorem 5.3. For any integer k ≥ 2, the metric space ( W0(k),δ ) is compact. Theorems 5.2 and 5.3 allow us to generalize the framework of Chatterjee and Varadhan to

( W0(k),δ ). The random hypergraph graph G(k)(n,p) corresponds to a random point fG(k)(n,p) ∈ W(k), and therefore it induces a probability distribution Pn,p on W(k) supported on a ﬁnite set of points corresponding to hypergraphs on n vertices.

- Theorem 5.4. For each ﬁxed p ∈ (0,1), the sequence Pn,p obeys a large deviation principle in the space ( W0(k),δ ) with rate function hp. Explicitly, for any closed set F ⊆ W0(k),

limsup

n→∞

1

n k

log Pn,p(F) ≤ − inf f∈F

hp(f),

and for any open set U ⊆ W0(k), liminf

n→∞

1

n k

log Pn,p(U) ≥ − inf f∈U

hp(f).

To derive large deviation results for subgraph densities in random graphs, it was crucial that the subgraph densities t(H,·) behaved continuously with respect to the cut topology. The next result implies that the same is true when H is a linear hypergraph. The proof is a straightforward generalization of the proof for graphs (see [4, Thm. 3.7]).

- Theorem 5.5. Let H be a k-uniform linear hypergraph. Then for any f,g ∈ W0(k), |t(H,f) − t(H,g)| ≤ e(H)δ (f,g).

The rate function for large deviations in H-counts is then determined by the following variational problem.

- Theorem 5.6. Let H be a k-uniform linear hypergraph and let Gn ∼ G(k)(n,p) be the random k-uniform hypergraph on n vertices with hyperedge probability p. For any ﬁxed p,r ∈ (0,1),


1

log P t(H,Gn) ≥ re(H) = −inf hp(f): f ∈ W0(k),t(H,f) ≥ re(H) . (5.1)

lim

n k

n→∞

Let F∗ be the set of minimizers for (5.1) and let F∗ be its image in W0(k). Then F∗ is a non-empty compact set. Moreover, for each ε > 0 there exists some C(H,ε,p,r) > 0 so that for any n

P δ (Gn, F∗) ≥ ε t(H,Gn) ≥ re(H) ≤ e−Cnk .

In particular, if F∗ = {f∗} for some f∗ ∈ W0(k) then the conditional distribution of Gn given the event t(H,Gn) ≥ re(H) converges to the point mass at f∗ as n → ∞.

We now turn to study the variational problem (5.1) towards the proof of Theorem 5.1. The following inequality is an immediate consequence of Theorem 3.1.

- Lemma 5.7. Let H be a k-uniform hypergraph with maximum degree at most d, and let f ∈ W0(k). Then t(H,f) ≤ f ed(H).


The following lemma mirrors Lemma 3.4 for proving the symmetry breaking phase.

Lemma 5.8. Let H be linear d-regular k-uniform hypergraph. Let 0 < p ≤ r < 1 be such that (rd,hp(r)) does not lie on the convex minorant of x  → hp(x1/d). Then there exists f ∈ W0(k) with t(H,f) > re(H) and hp(f) < hp(r).

The proof of Lemma 5.8 is essentially the same as the proof of Lemma 3.4, with the following modiﬁcation. One needs to adjust fε into fε = r + (r1 − r) A + (r2 − r) B, where A ⊂ [0,1]k is the union of the box [0,a]×[a,1−b]k−1 along with the k −1 other boxes formed by permuting the coordinates. Similarly B is the union of [1 − b,1] × [a,1 − b]k−1 and its coordinate permutations.

- Proof of Theorem 5.1. Our starting point is an application of Theorem 5.6. Suppose f ∈ W0(k) satisﬁes t(H,f) ≥ re(H). By Lemma 5.7, f d ≥ r. For Part (i) of the theorem, Lemma 3.3


Part (a) (which is also valid for W0(k)) implies that hp(f) ≥ hp(r) with equality if and only if f is the constant function r, so the variational problem on the right-hand side of (5.1) has the

constant function r as the unique minimizer. For Part (ii) of the theorem, Lemma 5.8 implies that the constant function r is not in the set of minimizers of the variational problem (5.1), and the conclusion follows analogously to the proof of Part (ii) of Theorem 1.1.

6. Graph homomorphism inequalities

Our goal in this section is to present a short new proof of Theorem 1.4, stating that for any d-regular bipartite graph G and any graph H allowing loops one has

hom(G,H) ≤ hom(Kd,d,H)|V (G)|/(2d) . (6.1)

(This inequality is tight when G is a disjoint union of copies of the complete bipartite graph Kd,d.) Generalized to graphons, the inequality states that for any d-regular bipartite graph G and f ∈ W0

t(G,f) ≤ t(Kd,d,f)|V (G)|/(2d) (6.2) (the more general formulation follows from (6.1) via a standard limiting argument, e.g., see [21]). As mentioned in the introduction, all previously known proofs of this inequality involved entropy. In contrast, the following proof does not rely on entropy or limiting arguments and instead is an immediate consequence of the generalized H¨lder’s inequality (Theorem 3.1).

Proof of Theorem 1.4. Label the vertices on the left-bipartition of G by [n] = {1,...,n}, and let Ai ⊂ [n] be the neighborhood of the i-th vertex on the right-bipartition of G. Deﬁne

g(x1,...,xd) := f(x1,y)f(x2,y)···f(xd,y) dy for any x1,...,xd ∈ [0,1], and write g(xA) for x ∈ [0,1]n and A = {i1,...,id} to denote g(xi1,...,xid). With this notation, t(G,f) =

n

g(xA1)···g(xAn) dx ≤ g nd

f(xi,yj) dx1 ···dxndy1 ···dyn =

[0,1]n

j=1 i∈Aj

by the generalized H¨lder’s inequality (Theorem 3.1). The result follows from noting that

g dd =

d

d

f(xi,yj) dx1 ···dxddy1 ···dyd = t(Kd,d,f).

i=1

j=1

Remark. A natural question to ask is whether Theorem 1.4 can be extended to all d-regular graphs G, as in the case for independent sets [46]. Unfortunately, the answer to this question is negative. A simple counter-example is G = K3 and f being the graphon corresponding to the 2 × 2 identity matrix. The second author [47] extended Theorem 1.4 to non-bipartite G for certain families of f ∈ W0, e.g., {0,1}-valued graphons that are non-decreasing in both coordinates. Galvin [20] conjectured that if G is a simple d-regular graph and H is a graph allowing loops then hom(G,H) is at most the maximum of hom(Kd,d,H)|V (H)|/(2d) and hom(Kd+1,H)|V (H)|/(d+1).

7. Open problems

It is natural to ask for extensions of the Chatterjee-Varadhan [8] large deviations theory to sparse Erd˝s-R´enyi random graphs (i.e., G(n,p) where p(n) → 0 as n → ∞) or to densities of general (not necessarily linear) hypergraphs in random hypergraphs. These may require extensions of Szemer´edi’s regularity lemma to sparse graphs (see [32, 22, 12]) and hypergraphs [23, 35, 39]. Even for G(n,p) with ﬁxed p, various problems remain open, several of which we highlight below.

Minimizers of the variational problem. It was pointed out by Chatterjee and Varadhan [8] that no solutions of the variational problem in Theorem 2.7 are known anywhere in the symmetry breaking phase. This remains the case. In fact, there is not a single point (p,r) in the symmetry breaking phase where we can even compute the large deviation rate. It would be interesting to see whether the minimizers are always 2-step graphons, i.e., graphons which are constant on each of [0,w]2, [0,w] × (w,1] ∪ (w,1] × [0,w] and [w,1]2 for some w ∈ (0,1).

Phase boundary for non-regular graphs. In this paper, we identiﬁed the replica symmetric phase for upper tail deviations in the densities of d-regular graphs. The phase boundary for non-regular graphs remains unknown. We suspect that a modiﬁcation of the construction in Lemma 3.4 can be used to establish the symmetry breaking phase for some (perhaps all) subgraph density deviations. However, at present we do not have matching boundaries for the replica symmetric phase.

Lower-tail phase transition. Proposition 3.5 shows that if a bipartite graph H satisﬁes Sidorenko’s conjecture then there is replica symmetry everywhere in the lower tail deviation of H-densities. It is an open question whether all bipartite graphs satisfy Sidorenko’s conjecture, although it is possible that Proposition 3.5 can be proved without the full resolution of Sidorenko’s conjecture.

When H is not bipartite, the following argument shows that there exists symmetry breaking in the lower tail, at least for certain values of (p,r). Let f be the graphon taking the value 0 on [0, 21]2 ∪ [12,1]2 and the value p elsewhere, so that t(H,f) = 0 and hp(f) = hp(0)/2. Let r0 ∈ (0,p) be such that hp(0) = 2hp(r0). Then for any r ∈ (0,r0) we have hp(f) < hp(r), and so (p,r) is in the symmetry breaking phase, resulting in a nontrivial phase diagram. We currently do not know the complete lower tail phase diagram for any non-bipartite H.

Symmetry breaking in exponential random graphs. Fig. 3 showed several (β1,β2)-phase plots for the symmetry breaking region given in Part (c) of Theorem 4.3. However, unlike the situation for large deviations, we do not know if that is the full region of symmetry breaking. It would be interesting to characterize the full set of triples (α,β1,β2) for which there is replica symmetry in Theorem 1.3.

Appendix A. The convex minorant of hp(x1/γ)

This appendix contains some technical lemmas about the convex minorant of hp(x1/γ), which appears throughout the paper. Let us ﬁrst informally summarize the claims. It is well known that

1 − x 1 − p

x p

+ (1 − x)log

hp(x) = xlog

is a convex function of x. When γ > 1 (here we allow any real γ, not just integers), it turns out that there is some p0(γ) for which x  → hp(x1/γ) is still a convex function when p ≥ p0. However, when p < p0, the function x  → hp(x1/γ) is no longer convex: it has exactly two inﬂection points, both to the right of its minimum at x = pγ. The function is concave in the corresponding middle region, whereas it is convex in the two outer regions.

In the case when x  → hp(x1/γ) is not convex, it has a unique lower tangent, touching the plot of the function at the points (qγ,hp(q)) and (qγ,hp(q)). The convex minorant of x  → hp(x1/γ) is formed by replacing the middle segment x ∈ (qγ,qγ) by the lower common tangent, as shown in

hp(x1/γ)

x

pγ qγ qγ

Figure 8. Illustration of the convex minorant of x  → hp(x1γ).

Fig. 8. (The various not-to-scale plots of hp(x1/γ) are shown for illustrative purposes in order to highlight the features of the plots. In contrast, all the phase diagrams plots are drawn to scale.)

Let Bγ ⊂ [0,1]2 denote the set of all points (p,q) such that (qγ,h(q)) does not lie on the convex minorant of x  → hp(x1/γ). Each vertical section of Bγ is thus the interval (qγ,qγ) described in the previous paragraph. For example, B2 is the shaded region in Fig. 9, and the boundaries of Bγ for additional values of γ were plotted in Figure 2 (see Section 1).

We shall show that each Bγ resembles a rotated V-shape. More importantly, we show that Bγ strictly contains Bγ if γ > γ .

The ﬁrst lemma describes the shape of the function x  → hp(x1/γ).

- Lemma A.1. The function x  → hp(x1/γ) with domain (0,1) is convex for 0 < γ ≤ 1. If γ > 1, and


γ − 1 γ − 1 + eγ/(γ−1) ,

p ≥ p0(γ) :=

then the function is also convex. If γ > 1 and 0 < p < p0, then the function has exactly two inﬂection points (both to the right of x = pγ), with a region of concavity in the middle. Finally the function has inﬁnite derivatives at both endpoints of (0,1).

Proof. When 0 < γ ≤ 1, x  → x1/γ is convex. Since the composition of two convex functions is convex we deduce that x  → hp(x1/γ) is convex.

Next, assume d ≥ 1. We have

p 1 − p

1 x(1 − x)

x 1 − x − log

. Therefore,

, and h p(x) =

h p(x) = log

d dx

1 γ

x1/γ−1h p(x1/γ) and

hp(x1/γ) =

d2 dx2

1 γ − 1 x1/γ−2h p(x1/γ)

1 γ2

1 γ

x2/γ−2h (x1/γ) +

hp(x1/γ) =

x1/γ−2 γ2

x1/γh p(x1/γ) − (γ − 1)h p(x1/γ) .

=

1.0

0.8

0.6

B2

0.4

0.2

0.0

0.0 0.2 0.4 0.6 0.8 1.0

Figure 9. The region B2 consisting of all points (p,q) such that (q2,hp(q)) does not lie on the convex minorant of x  → hp(√x).

The claim on inﬁnite derivatives easily follows from the above formulas. Setting x = qγ, we have

q1−2γ γ2

d2 dx2

hp(x1/γ)

qh p(q) − (γ − 1)h p(q))

=

x=qγ

q1−2γ γ2

1 1 − q − (γ − 1)log

q 1 − q

p 1 − p

+ (γ − 1)log

=

. (A.1)

Hence, hp(x1/γ) is convex at x = qγ whenever 1−1q −(γ −1)log 1−qq ≥ −(γ −1)log 1−pp and concave otherwise. The fact that

γq − γ + 1 q(1 − q)2

d dq

1 1 − q − (γ − 1)log

q 1 − q

=

implies that 1−1q − (γ − 1)log 1−qq is decreasing until q = (γ − 1)/γ and then increasing afterwards. It diverges to +∞ at both endpoints of (0,1) and attains a minimum value of γ −(γ −1)log(γ −1)

at q = (γ − 1)/γ. The term (γ − 1)log 1−pp of Eq. (A.1) is increasing for p ∈ (0,1) and surjective onto the reals. Therefore, h p(x1/d) ≥ 0 for all x if γ − (γ − 1)log(γ − 1) + (γ − 1)log 1−pp ≥ 0, which is equivalent to having p ≥ γ−1+γe−γ/1(γ−1). Additionally, if p < γ−1+γe−γ/1(γ−1), then h p(x) starts as positive, becomes negative, then turns positive again.

We next give an explicit description of the region B2.

- Lemma A.2 (γ = 2 case). Let p,q ∈ (0,1). The point (q2,hp(q)) lies strictly above the convex minorant of x  → hp(√x) if and only if p < 1 + (q−1 − 1)1/(1−2q) −1.


Proof. We claim that the lower common tangent of x  → hp(√x) has slope log(1−pp). To show this, it suﬃces to check that hp(√x)−xlog(1−pp) has a horizontal common lower tangent, and it suﬃces to check the same thing for hp(x) − x2 log(1−pp). Observe that

1 − x 1 − p − x2 log

1 − p p

1 − p p

x p

hp(x) − x2 log

+ (1 − x)log

= xlog

p 1 − p − log(1 − p)

= xlog x + (1 − x)log(1 − x) − x(1 − x)log

hp(x1/γ)

x

qγ q1γ q2γ qγ

### Figure 10. Illustration of the convex minorant of x  → hp(x1/γ) in the setting of Lemma A.3.

x1/γ log pp(1 (1−−pp) )

hp (x1/γ)

hp(x1/γ)

x

x

x

q1γ q2γ

q1γ q2γ

q1γ q2γ

Figure 11. Illustration of the functions in Eq. (A.3).

is invariant under x  → 1 − x, so that its lower tangent must be horizontal by symmetry, and let it touch the curve at x = q,q, so that 0 < q < q < 1 are the zeros of the derivative, namely

x 1 − x − (1 − 2x)log

p 1 − p

log

. (A.2)

It follows that (q2,hp(q)) lies strictly above the convex minorant if and only if q < q < q, which is equivalent to having 1−12q log 1−qq ≤ log 1−pp. Rearranging the latter concludes the proof.

For γ > 1 and 0 < p < p0(γ), deﬁne q = q(γ,p) and q = q(γ,p) to be such that the lower common

tangent to x  → hp(x1/γ) touches the curve at points (qγ,hp(q) and (qγ,hp(q)). An examination of the geometry of the curve, as illustrated in Fig. 10, immediately leads to the following lemma:

- Lemma A.3. Let γ > 1 and 0 < p < p0(γ). Let 0 < q1 < q2 < 1. If the line segment joining points

(q1γ,hp(q1)) and (q2γ,hp(q2)) lies below the curve {(qγ,hp(q)) : 0 ≤ q ≤ 1} and is not tangent to the curve at one of the end points, then this segment lies strictly above the lower common tangent of

the curve. Consequently, q(γ,p) < q1 < q2 < q(γ,p). We now apply the above lemma to describe the shape of the regions Bγ.

- Lemma A.4. If γ > 1 and 0 < p < p < p0(γ), then q(γ,p) < q(γ,p ) < q(γ,p ) < q(γ,p). So Bγ is a rotated-V-shaped region.


Proof. Let q1 = q(γ,p ) and q2 = q(γ,p ). As illustrated in Fig. 11, we have hp(x1/γ) = hp (x1/γ) + x1/γ log

p (1 − p) p(1 − p )

1 − p 1 − p

+ log

. (A.3)

hp(u1/γ)

hp(x1/γ )

### −−−−−→x=uγ /γ

u

x

q1γ q2γ

q 1γ q 2γ

Figure 12. The plot of x  → hp(x1γ) following a change of variable x = uγ /γ.

The segment joining (q1γ,hp (q1)) and (q2γ,hp (q2)) lies below x  → hp (x1/γ) by deﬁnition. Since x  → x1/γ log pp(1 (1−−pp )) is concave, the segment joining x = q1γ and x = q2γ must also lie below the curve x  → hp(x1/γ), and it is not tangent to either endpoint due to the x1/γ term. The conclusion now follows from Lemma A.3.

- Lemma A.5. If γ > γ > 1 and 0 < p < pγ , then q(γ,p) < q(γ ,p) < q(γ ,p) < q(γ,p). So Bγ strictly contains Bγ .


Proof. Let q1 = q(γ ,p) and q2 = q(γ ,p). Let denote the line segment joining points (q 1γ ,hp(q1)) and (q 2γ ,hp(q2)), so that is tangent to the curve x  → hp(x1/γ ).

Consider a transformation of the plots induced by the change of variable x = uγ /γ. The plot of x  → hp(x1/γ ) becomes the plot of u  → hp(u1/γ) (see Fig. 12). Originally was a line segment of positive slope lying below the curve x  → hp(x1/γ ) and tangent to it at both endpoints. Following the transformation x = uγ /γ (recall that γ /γ < 1) we see that becomes a concave curve still lying below the new curve u  → hp(u1/γ) and tangent to it at both endpoints. This implies that the line segment joining the two endpoints of in the new frame lies below both curves and is tangent to neither at the endpoints. The conclusion then follows from Lemma A.3.

Acknowledgments

We thank Amir Dembo and Ofer Zeitouni for fruitful discussions. This work was initiated while Y. Z. was an intern at the Theory Group of Microsoft Research, and he thanks the Theory Group for its hospitality.

References

- [1] N. Alon. Independent sets in regular graphs and sum-free subsets of ﬁnite groups. Israel J. Math., 73(2):247–256, 1991.
- [2] S. Bhamidi, G. Bresler, and A. Sly. Mixing time of exponential random graphs. Ann. Appl. Probab., 21(6):2146– 2170, 2011.
- [3] B. Bolloba´s. Random graphs, volume 73 of Cambridge Studies in Advanced Mathematics. Cambridge University Press, Cambridge, second edition, 2001.
- [4] C. Borgs, J. T. Chayes, L. Lova´sz, V. T. So´s, and K. Vesztergombi. Convergent sequences of dense graphs. I. Subgraph frequencies, metric properties and testing. Adv. Math., 219(6):1801–1851, 2008.
- [5] S. Chatterjee. The missing log in large deviations for triangle counts. Random Structures Algorithms, 40(4):437– 451, 2012.


- [6] S. Chatterjee and P. S. Dey. Applications of Stein’s method for concentration inequalities. Ann. Probab., 38(6):2443–2485, 2010.
- [7] S. Chatterjee and P. Diaconis. Estimating and understanding exponential random graph models. Ann. Statist., to appear.
- [8] S. Chatterjee and S. R. S. Varadhan. The large deviation principle for the Erdo˝s-Re´nyi random graph. European J. Combin., 32(7):1000–1017, 2011.
- [9] S. Chatterjee and S. R. S. Varadhan. Large deviations for random matrices. Comm. Stoch. Analysis, 6(1):1–13, 2012.
- [10] F. R. K. Chung. Regularity lemmas for hypergraphs and quasi-randomness. Random Structures Algorithms, 2(2):241–252, 1991.
- [11] D. Conlon, J. Fox, and B. Sudakov. An approximate version of Sidorenko’s conjecture. Geom. Funct. Anal., 20(6):1354–1366, 2010.
- [12] D. Conlon, J. Fox, and Y. Zhao. Extremal results in sparse pseudorandom graphs. Preprint arXiv:1204.6645.
- [13] B. Demarco and J. Kahn. Tight upper tail bounds for cliques. Random Structures Algorithms.
- [14] B. DeMarco and J. Kahn. Upper tails for triangles. Random Structures Algorithms, 40(4):452–459, 2012.
- [15] A. Dembo and O. Zeitouni. Large deviations techniques and applications, volume 38 of Stochastic Modelling and Applied Probability. Springer-Verlag, Berlin, 2010. Corrected reprint of the second (1998) edition.
- [16] G. Elek and B. Szegedy. Limits of hypergraphs, removal and regularity lemmas. A non-standard approach. Preprint arxiv:0705.2179.
- [17] G. Elek and B. Szegedy. A measure-theoretic approach to the theory of dense hypergraphs. Preprint arXiv:0810.4062.
- [18] H. Finner. A generalization of Ho¨lder’s inequality and some probability inequalities. Ann. Probab., 20(4):1893– 1901, 1992.
- [19] A. Frieze and R. Kannan. Quick approximation to matrices and applications. Combinatorica, 19(2):175–220, 1999.
- [20] D. Galvin. Maximizing H-colorings of regular graphs. J. Graph Theory, to appear.
- [21] D. Galvin and P. Tetali. On weighted graph homomorphisms. In Graphs, morphisms and statistical physics, volume 63 of DIMACS Ser. Disc. Math. Theoret. Comput. Sci., pages 97–104. Amer. Math. Soc., Providence, RI, 2004.
- [22] S. Gerke and A. Steger. The sparse regularity lemma and its applications. In Surveys in combinatorics 2005, volume 327 of London Math. Soc. Lecture Note Ser., pages 227–258. Cambridge Univ. Press, Cambridge, 2005.
- [23] W. T. Gowers. Hypergraph regularity and the multidimensional Szemer´edi theorem. Ann. of Math. (2), 166(3):897–946, 2007.
- [24] O. Ha¨ggstr¨om and J. Jonasson. Phase transition in the random triangle model. J. Appl. Probab., 36(4):1101–1115, 1999.
- [25] H. Hatami. Graph norms and Sidorenko’s conjecture. Israel J. Math., 175:125–150, 2010.
- [26] S. Janson, T.  Luczak, and A. Rucinski. Random graphs. Wiley-Interscience Series in Discrete Mathematics and Optimization. Wiley-Interscience, New York, 2000.
- [27] S. Janson, K. Oleszkiewicz, and A. Rucin´ski. Upper tails for subgraph counts in random graphs. Israel J. Math., 142:61–92, 2004.
- [28] S. Janson and A. Rucin´ski. The infamous upper tail. Random Structures Algorithms, 20(3):317–342, 2002. Probabilistic methods in combinatorial optimization.
- [29] S. Janson and A. Ruci´nski. The deletion method for upper tail estimates. Combinatorica, 24(4):615–640, 2004.
- [30] J. Kahn. An entropy approach to the hard-core model on bipartite graphs. Combin. Probab. Comput., 10(3):219– 237, 2001.
- [31] J. H. Kim and V. H. Vu. Divide and conquer martingales and the number of triangles in a random graph. Random Structures Algorithms, 24(2):166–174, 2004.
- [32] Y. Kohayakawa. Szemere´di’s regularity lemma for sparse graphs. In Foundations of computational mathematics (Rio de Janeiro, 1997), pages 216–230. Springer, Berlin, 1997.
- [33] L. Lova´sz and B. Szegedy. Limits of dense graph sequences. J. Combin. Theory Ser. B, 96(6):933–957, 2006.
- [34] L. Lova´sz and B. Szegedy. Szemere´di’s lemma for the analyst. Geom. Funct. Anal., 17(1):252–270, 2007.
- [35] B. Nagle, V. Ro¨dl, and M. Schacht. The counting lemma for regular k-uniform hypergraphs. Random Structures Algorithms, 28(2):113–179, 2006.
- [36] J. Park and M. E. J. Newman. Solution of the two-star model of a network. Phys. Rev. E (3), 70(6):066146, 5,

- 2004.

[37] J. Park and M. E. J. Newman. Solution for the properties of a clustered network. Phys. Rev. E, 72:026136, Aug

- 2005.


- [38] C. Radin and M. Yin. Phase transitions in exponential random graphs. Preprint arXiv:1108.0649.


- [39] V. Ro¨dl and J. Skokan. Regularity lemma for k-uniform hypergraphs. Random Structures Algorithms, 25(1):1–42, 2004.
- [40] W. Rudin. Functional analysis. International Series in Pure and Applied Mathematics. McGraw-Hill Inc., New York, second edition, 1991.
- [41] A. Sidorenko. A correlation inequality for bipartite graphs. Graphs Combin., 9(2):201–204, 1993.
- [42] M. Simonovits. Extremal graph problems, degenerate extremal problems, and supersaturated graphs. In Progress in graph theory (Waterloo, Ont., 1982), pages 419–437. Academic Press, Toronto, ON, 1984.
- [43] D. Strauss. On a general class of models for interaction. SIAM Rev., 28(4):513–527, 1986.
- [44] E. Szemere´di. Regular partitions of graphs. In Probl`emes combinatoires et the´orie des graphes (Colloq. Internat. CNRS, Univ. Orsay, Orsay, 1976), volume 260 of Colloq. Internat. CNRS, pages 399–401. CNRS, Paris, 1978.
- [45] V. H. Vu. A large deviation result on the number of small subgraphs of a random graph. Combin. Probab. Comput., 10(1):79–94, 2001.
- [46] Y. Zhao. The number of independent sets in a regular graph. Combin. Probab. Comput., 19(2):315–320, 2010.
- [47] Y. Zhao. The bipartite swapping trick on graph homomorphisms. SIAM J. Discrete Math., 25(2):660–680, 2011.


E. Lubetzky

Microsoft Research, One Microsoft Way, Redmond, WA 98052-6399. E-mail address: eyal@microsoft.com Y. Zhao

Department of Mathematics, MIT, Cambridge, MA 02139-4307. E-mail address: yufeiz@math.mit.edu

