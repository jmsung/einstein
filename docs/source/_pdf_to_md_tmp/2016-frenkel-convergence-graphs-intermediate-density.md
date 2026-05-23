arXiv:1602.05937v5[math.CO]26Dec2017

CONVERGENCE OF GRAPHS WITH INTERMEDIATE DENSITY

PÉTER E. FRENKEL

Abstract. We propose a notion of graph convergence that interpolates between the Benjamini–Schramm convergence of bounded degree graphs and the dense graph convergence developed by László Lovász and his coauthors. We prove that spectra of graphs, and also some important graph parameters such as numbers of colorings or matchings, behave well in convergent graph sequences. Special attention is given to graph sequences of large essential girth, for which asymptotics of coloring numbers are explicitly calculated. We also treat numbers of matchings in approximately regular graphs.

We introduce tentative limit objects that we call graphonings because they are common generalizations of graphons and graphings. Special forms of these, called Hausdorﬀ and Euclidean graphonings, involve geometric measure theory. We construct Euclidean graphonings that provide limits of hypercubes and of ﬁnite projective planes, and, more generally, of a wide class of regular sequences of large essential girth. For any convergent sequence of large essential girth, we construct weaker limit objects: an involution invariant probability measure on the sub-Markov space of consistent measure sequences (this is unique), or an acyclic reversible sub-Markov kernel on a probability space (non-unique). We also pose some open problems.

Contents

- 1. Homomorphism densities and graph convergence 2

- 1.1. Injective homomorphism densities 4
- 1.2. Rooted homomorphism densities 6
- 1.3. Regular sequences 6
- 1.4. Sequences with large essential girth 8


- 2. Convergence of spectra 10
- 3. Graph polynomials 12

- 3.1. Number of proper colorings (large essential girth case) 14
- 3.2. Matching measure and graph convergence 15
- 3.3. Spectral measure rescaled (regular, large girth case) 18
- 4. Graphonings 19

- 4.1. Sub-Markov kernels and rooted homomorphism densities 20

- 4.2. Reversible kernels and unrooted homomorphism densities 23
- 4.3. Graph limits 25
- 4.4. Hausdorﬀ limits 26
- 4.5. Acyclicity and regularity 28
- 4.6. Hausdorﬀ limits of regular sequences of large essential girth 30


- 5. Sub-Markov spaces 35


- 5.1. Tree densities and kernel preserving maps 35




![image 1](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile1.png>)

This project has received funding from the European Research Council (ERC) under the European Union’s Horizon 2020 research and innovation program (grant agreement No. 648017), from the MTA Rényi Lendület Groups and Graphs research group, and from the Hungarian National Research, Development and Innovation Oﬃce – NKFIH, OTKA grants no. K104206 and K109684.

1

- 5.2. The space of consistent measure sequences 36
- 6. Regularity lemma? 39 Acknowledgements 40 References 40


Notations and terminology. Graphs are ﬁnite, simple, and undirected, unless otherwise speciﬁed. On k nodes, the complete graph, cycle, path, and path with a fork at one end is denoted by Kk, Ck, Pk, and Dk, respectively. For a graph G = (V (G), E(G)), we write v(G) = |V (G)| and e(G) = |E(G)|. A graph F has c(F) connected components, out of which c≥2(F) have at least two nodes. The neighborhood (i.e., set of neighbors) of a node o is written N(o).

The number of homomorphisms and injective homomorphisms from F to G is denoted by hom(F, G) and inj(F, G), respectively. The number of automorphisms of F is aut F. The symbols × and stand for the categorical (or weak) direct product and the Cartesian sum of graphs, respectively.

The product of σ-algebras is denoted by ⊗. We write a.e. for “almost every(where)” and a.s. for “almost surely”, i.e., “with probability 1”. The indicator of an event A is 1A.

1. Homomorphism densities and graph convergence

The two most developed graph limit theories are the Benjamini–Schramm limit theory of bounded degree graphs and the dense graph limit theory developed by Borgs, Chayes, Lovász, T. Sós, Szegedy, and Vesztergombi. The convergence of dense graphs is deﬁned in terms of homomorphism densities. The convergence of bounded degree graphs is deﬁned in terms of neighborhood statistics, but this easily translates into convergence of homomorphism frequencies. We now propose a common generalization that works for both cases and also for intermediate density.

Deﬁnition 1.1. An admissible pair is a pair (G, d), where d ≥ 1 and G is a graph with all degrees ≤ d. For a connected graph F and an admissible pair (G, d), we deﬁne the homomorphism density

hom(F, G) v(G)dv(F)−1 ∈ [0, 1].

t(F, G, d) =

![image 2](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile2.png>)

We extend this to arbitrary F by making it multiplicative: t(F, G, d) =

hom(F, G) v(G)c(F)d(v−c)(F) ∈ [0, 1].

![image 3](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile3.png>)

An admissible sequence is a sequence of admissible pairs. An admissible sequence (Gn, dn) is convergent if the number sequence t(F, Gn, dn) converges for any (or, equivalently, any connected) graph F.

- Remark 1.2. Note that


hom(F, G) v(G)v(F)

= t(F, G)

t(F, G, v(G)) =

![image 4](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile4.png>)

is the usual homomorphism density. Thus, a sequence of the form (Gn, v(Gn)) which is always admissible — is convergent precisely if (Gn) is a convergent dense graph sequence.

Note also that for connected F we have t(F, G, d) = t∗(F, G)/dv(F)−1,

where t∗(F, G) = hom(F, G)/ v(G) is the usual homomorphism frequency, so if dn = d does not depend on n, then an admissible sequence (Gn, d) is convergent precisely if (Gn) is a Benjamini–Schramm convergent graph sequence (alternatively called a locally convergent graph sequence).

When F is a forest, the normalization used in Deﬁniton 1.1 is similar to the one used by Bollobás and Riordan [6] and by Borgs, Chayes, Cohn, and Zhao [7, 8]. However, for general F, our normalization is quite diﬀerent. The goal in those papers was to generalize dense graph convergence to the sparse case, but no attempt was made to also include Benjamini–Schramm convergence in a uniﬁed treatment. In the present approach, both extremes are included as special cases. This is also reﬂected in the limit objects — generalized graphons —, which are Lp graphons in [7, 8] but graphonings in Section 4 of the present paper. Admittedly, the results presented in this paper are less conclusive.

- Remark 1.3. Let (G, d) be an admissible pair. Removing an edge from a connected graph F without destroying connectivity cannot decrease t(F, G, d). Removing a vertex of degree 1 from a connected graph F cannot either. Thus, we have t(F, G, d) ≤ t(F′, G, d) if F′ ⊆ F are connected graphs.


Proposition 1.4. Let (G, d) be an admissible pair. Let F be a graph. Then we have t(F, G, d) = 1 if and only if at least one of the following holds.

- (a) F is an edgeless graph, or
- (b) F is a forest and G is d-regular, or
- (c) F is bipartite and G is a disjoint union of complete bipartite graphs Kd,d.


Proof. We may assume that F and G are connected. If any of (a), (b), (c) holds, then an easy induction on v(F) shows that hom(F, G) =

v(G)dv(F)−1 and the claim follows. For the converse, assume that t(F, G, d) = 1. If (a) does not hold, then F contains K2 as a subgraph, thus 2 e(G)/(v(G)d) =

t(K2, G, d) ≥ t(F, G, d) = 1 and therefore G is d-regular.

If F contains an odd cycle C2k+1, then consider the path P2k+1 = C2k+1 − e for an edge e ∈ E(C2k+1). We have

t(C2k+1, G, d) = 1 = t(P2k+1, G, d), thus

hom(C2k+1, G) = hom(P2k+1, G).

But there exists a homomorphism φ : P2k+1 → G such that images of the two endnodes coincide. Such a φ does not extend to C2k+1 because G has no loops. This contradiction proves that F is bipartite.

If F contains an even cycle C2k for some k ≥ 2, then a similar argument shows that in G, the two endnodes of any walk of length 2k −1 are joined by an edge. It follows that this holds for 3 in place of 2k − 1, and thus for any odd length as well. But G has no loops, so it must be bipartite. It is connected, so it is a complete bipartite graph. It is d-regular, so G ≃ Kd,d.

Example 1.5. Let (Γi, δi) be admissible pairs (i = 1, 2, . . .). Set Gn = Γ1 × · · ·× Γn and dn = δ1 · · ·δn. Then the sequence (Gn, dn) is convergent. The homomorphism density t(F, Gn, dn) converges to ∞i=1 t(F, Γi, δi).

Proof. We have hom(F, Gn) = ni=1 hom(F, Γi) and v(Gn) = ni=1 v(Γi), whence t(F, Gn, dn) =

n

t(F, Γi, δi). This is decreasing and therefore convergent as n → ∞.

i=1

Corollary 1.6. Let (Γ, δ) be an admissible pair. Then the sequence (Γ×n, δn) is convergent. The homomorphism density t(F, Γ×n, δn) converges to 1 if t(F, Γ, δ) = 1 and to zero otherwise.

Example 1.7. If G is a disjoint union of graphs Gi (i = 1, . . ., v(G)/d) of size d, then

v(G)/d

d v(G)

t(F, Gi)

t(F, G, d) =

![image 5](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile5.png>)

i=1

for all connected F. We can think of each Gi as a point in the compact graphon space W0 of L. Lovász and B. Szegedy [26, 28], and consider the uniform probability measure on these v(G)/d points. We can think of W0 as sitting in [0, 1]∞, each graphon W being represented by its proﬁle of homomorphism densities t(F, W) with connected F. A sequence (Gn, dn), such that Gn is a disjoint union of graphs of size dn, is convergent if and only if the barycenters of the corresponding probability measures form a convergent sequence. This is strictly weaker than the weak convergence of the probability measures themselves. If (Gn, dn) converges, then the limit can be represented by the limiting barycenter (which is unique), or any subsequential weak limit measure (which is non-unique in general, but each one has the correct barycenter).

Further examples of convergent sequences are regular sequences of large essential girth, such as hypercube graphs, large grid graphs, incidence graphs of ﬁnite projective spaces, and suitable random nearly regular graphs. See Subsections 1.3 and 1.4.

- 1.1. Injective homomorphism densities. It is sometimes useful to count injective, rather than arbitrary, homomorphisms. We introduce injective homomorphism densities. Even in the dense case, our normalization deviates slightly from the standard one in Lovász’s monograph [26].


Deﬁnition 1.8. Let (G, d) be an admissible pair. For a connected graph F, we deﬁne the injective homomorphism density

inj(F, G) v(G)d(d − 1)v(F)−2 ∈ [0, 1]

tinj(F, G, d) =

![image 6](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile6.png>)

unless F is a single point, in which case tinj(F, G, d) = 1. We extend this to arbitrary F by making the denominator multiplicative:

inj(F, G) v(G)c(F)dc≥2(F)(d − 1)(v−c−c≥2)(F) ≤

tinj(F, G, d) =

tinj(Fi, G, d), where the Fi are the connected components of F.

![image 7](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile7.png>)

i

Remark 1.9. Let d > 1 and let (G, d) be an admissible pair. Removing an edge from a connected graph F without destroying connectivity cannot decrease tinj(F, G, d). Removing a vertex of degree 1 from a connected graph F cannot either. Thus, tinj(F, G, d) ≤ tinj(F′, G, d) if F′ ⊆ F are connected graphs.

Proposition 1.10. For any ﬁxed connected graph F, we have

t(F, G, d) − tinj(F, G, d) = O(1/d), where the constant in the O depends only on F. Proof. For F = K1, both densities are 1 and the claim is trivial. For v(F) ≥ 2, we have

v(F)−2

inj(F, G) v(G)dv(F)−1 = tinj(F, G, d) 1 −

1 d

t(F, G, d) ≥

, whence

![image 8](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile8.png>)

![image 9](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile9.png>)

1 d

tinj(F, G, d) − t(F, G, d) ≤ tinj(F, G, d) 1 − 1 −

![image 10](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile10.png>)

v(F)−2

v(F) − 2 d

≤

.

![image 11](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile11.png>)

On the other hand, we have the well-known formula hom(F, G) =

inj(F′, G),

F′

where F′ runs over the quotients of F. Note that quotients of connected graphs are connected, and proper quotients have fewer vertices than the original graph. Thus,

t(F, G, d) =

F′

inj(F′, G) v(G)dv(F)−1 ≤

![image 12](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile12.png>)

F′

tinj(F′, G, d) dv(F)−v(F′) = tinj(F, G, d) + O

![image 13](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile13.png>)

1 d

![image 14](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile14.png>)

.

Corollary 1.11. An admissible sequence (Gn, dn) with dn → ∞ is convergent precisely if the injective homomorphism density tinj(F, Gn, dn) converges for all connected graphs F. If this is the case, then

t(F, Gn, dn) for any connected F.

lim

tinj(F, Gn, dn) = lim

n→∞

n→∞

This is well known in the dense case: homomorphism and injective homomorphism densities are almost the same.

It will be useful to also compare injective and componentwise injective homomorphisms.

- Proposition 1.12. Let F have connected components Fi. Then we have


tinj(Fi, G, d) − tinj(F, G, d) ≤

0 ≤

i

1 v(G) F

1 v(G)2

tinj(F′, G, d) + O

≤

= O

![image 15](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile15.png>)

![image 16](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile16.png>)

′

1 v(G)

![image 17](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile17.png>)

,

where F′ runs over the quotients of F such that each Fi maps injectively to F′ and c(F′) = c(F) − 1. The constant in the O depends only on F.

Proof. We have

inj(F′, G),

inj(Fi, G) =

F′

i

where F′ runs over the quotients of F that arise by only identifying nodes from distinct components. We always have (v −c)(F′) ≤ (v −c)(F) and c≥2(F′) ≤ c≥2(F), hence

inj(F′, G) v(G)c(F)dc≥2(F)(d − 1)(v−c−c≥2)(F) ≤

tinj(F′, G, d) v(G)c(F)−c(F′) and the claim follows.

tinj(Fi, G, d) =

![image 18](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile18.png>)

![image 19](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile19.png>)

F′

F′

i

- 1.2. Rooted homomorphism densities.

Deﬁnition 1.13. Let (F, o) and (G, p) be rooted graphs, where F is connected. Let hom((F, o), (G, p)) be the number of homomorphisms of F into G that map o to p. If (G, d) is admissible, we deﬁne the rooted homomorphism density

t((F, o), (G, p), d) =

hom((F, o), (G, p))

![image 20](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile20.png>)

dv(F)−1 ∈ [0, 1]. Remark 1.14. For any connected rooted graph (F, o) and any admissible pair (G, d), we have

t(F, G, d) = Et((F, o), (G, p), d), where p is a uniform random node of G.

- 1.3. Regular sequences.


Deﬁnition 1.15. Let 0 ≤ α ≤ 1. The admissible sequence (Gn, dn) is α-regular if the degree of a uniform random vertex of Gn, divided by dn, tends stochastically to α.

If the graph Gn is αdn-regular for every n, then of course the sequence (Gn, dn) is α-regular. Let us look at less trivial examples.

- Example 1.16. Let Gn be the dn-dimensional grid graph with n × · · · × n points.

Then v(Gn) = nd

n

and

e(Gn) = dnnd

n−1(n − 1), so

t(K2, Gn, 2dn) = e(Gn)/(v(Gn)dn) = (n − 1)/n → 1, i.e., the sequence (Gn, 2dn) is 1-regular, cf. Proposition 1.20 below. If the sequence dn either stabilizes to some d or tends to ∞, then (Gn, 2dn) is convergent, cf. Subsection 1.4.

The case when dn → ∞ can be generalized as follows.

- Example 1.17. Consider a triangular array (Γni, δni) (1 ≤ i ≤ n) of admissible pairs with normalized average degree αni = t(K2, Γni, δni). Set Gn = Γn1 · · · Γnn and dn = δn1 + · · · + δnn. Assume that


- (1.1) max


δni/dn → 0 and the weighted average

1≤i≤n

n

1 dn

δniαni → α. Then the sequence (Gn, dn) is α-regular.

![image 21](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile21.png>)

i=1

Proof. Let Xni be the degree of a uniform random node in Γni, divided by δni. Then Xni is a random variable with range in [0, 1], and EXni = αni. The degree of a uniform random node in Gn, divided by dn, is

Xn = (δn1Xn1 + · · · + δnnXnn)/dn, where the Xni are independent. We have EXn → α and

n

1 d2n

D2Xn = (δn21D2Xn1 + · · · + δnn2 D2Xnn)/d2n ≤

δni2 → 0. Thus Xn → α stochastically as claimed, by Chebyshev’s inequality.

![image 22](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile22.png>)

i=1

Again we refer to Subsection 1.4 where it will be proved that such a sequence (Gn, dn) of Cartesian sums is always convergent. Corollary 1.18. Let (Γ, δ) be admissible with normalized average degree t(K2, Γ, δ) = α. Then the sequence Γ n, nδ is α-regular.

Regular sequences can be characterized in terms of homomorphism densities.

- Proposition 1.19. For an admissible sequence (Gn, dn), the following are equivalent.


- (a) The sequence (Gn, dn) is α-regular.
- (b) We have t(K2, Gn, dn) → α and t(P3, Gn, dn) → α2 as n → ∞.
- (c) For all forests F, we have t(F, Gn, dn) → αe(F) as n → ∞.
- (d) For all rooted trees (F, o), we have t((F, o), (Gn, pn), dn) → αe(F) stochastically, as n → ∞. Here pn is a uniform random node of Gn.


Note that the statement (d) for F = K2 is exactly the same as (a).

Proof. Let Xn be the degree of a uniform random node of Gn, divided by dn. Then Xn is a random variable with values in [0, 1]. The equivalence of (a) and (b) is clear since we have t(K2, Gn, dn) = EXn and t(P3, Gn, dn) = EXn2.

As (d) ⇒ (c) ⇒ (b) is trivial, it suﬃces to show that (a) implies (d). We use induction on v(F). The case v(F) = 1 is trivial. Let v(F) ≥ 2. Let oi (i = 1, . . ., k) be the neighbors of o in F, i.e., N(o) = {o1, . . ., ok}. Let Fi be the connected component of F − o containing oi.

Let ǫ > 0. By the induction hypothesis, for n ≥ n0(ǫ) there exists an Sn ⊂ V (Gn), with |Sn| < ǫ2 v(Gn), such that for all q ∈ V (Gn) − Sn and all i, we have

![image 23](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile23.png>)

e(Fi) t((Fi, oi), (Gn, q), dn) − α < ǫ.

Let Tn be the set of nodes in Gn that have at least ǫdn neighbors in Sn. Since all nodes in Sn have at most dn neighbors, we have |Tn| ≤ |Sn|/ǫ < ǫv(Gn). For all p ∈ V (Gn) − Tn, we have

0 ≤ hom((F, o), (Gn, p)) − hom((F, o, N(o)), (Gn, p, V (Gn) − Sn)) ≤ kǫdnv(F)−1. Let Un be the set of nodes in Gn whose degree divided by dn is not in (α − ǫ, α + ǫ). For n ≥ n0(ǫ), we have |Un| < ǫv(Gn) by (a). For all p ∈ V (Gn) − Tn − Un, we have

((α − 2ǫ)dn)e(F) ≤ hom((F, o, N(o)), (Gn, p, V (Gn) − Sn)) ≤ ((α + ǫ)dn)e(F) and therefore

(α − 2ǫ)e(F) ≤ t((F, o), (Gn, p), dn) ≤ (α + ǫ)e(F) + kǫ.

This is true for all ǫ > 0, n ≥ n0(ǫ), and p ∈ V (Gn) − Tn − Un, where |Tn| + |Un| < 2ǫv(Gn). Statement (d) follows.

- Proposition 1.20. For an admissible sequence (Gn, dn), the following are equivalent.


- (a) The sequence (Gn, dn) is 1-regular.
- (b) The average degree in Gn is asymptotically dn.
- (c) We have t(K2, Gn, dn) → 1 as n → ∞.
- (d) For all forests F, we have t(F, Gn, dn) → 1 as n → ∞.


Proof. The equivalence of (a) and (b) is clear since (Gn, dn) is admissible.

Observe that t(K2, G, d) is the average degree in G, divided by d. This shows the equivalence of (b) and (c).

Since trivially (d) ⇒ (c), it suﬃces to prove (a) ⇒ (d). This follows from Proposition 1.19 and Remark 1.14.

- 1.4. Sequences with large essential girth.


Deﬁnition 1.21. The graph sequence (Gn) has large girth if, for any k ≥ 3, we have inj(Ck, Gn) = 0 for n ≥ n0(k). The admissible sequence (Gn, dn) has large essential girth if, for all k ≥ 3, we have tinj(Ck, Gn, dn) → 0 as n → ∞.

- Remark 1.22. If (Gn, dn) has large essential girth and G′n is a spanning subgraph of Gn, then (G′n, dn) has large essential girth.
- Remark 1.23. The injective homomorphism density of a cycle in a graph G satisﬁes


N(G) v(G)d(d − 1)k−2,

- (1.2) tinj(Ck, G, d) ≤


![image 24](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile24.png>)

where N(G) is the number of non-backtracking walks of length k − 1 in G whose starting point and endpoint are adjacent. The fraction on the right hand side has the following interpretation in terms of random walks. Choose v0 ∈ V (G) uniformly at random. With probability deg(v0)/d, let v1 be a neighbor of v0 chosen uniformly at random. With probability 1−deg(v0)/d, do not deﬁne v1. If i ≥ 2 and vi−1 is deﬁned, then with probability (deg(vi−1) − 1)/(d − 1), let vi be a neighbor of vi−1, distinct from vi−2, chosen uniformly at random. With probability 1−(deg(vi−1)−1)/(d−1), do not deﬁne vi. Then the right hand side of (1.2) is the probability that vk−1 is deﬁned and adjacent to v0.

When G is d-regular, vi is almost surely deﬁned for every i. For example, we look at two classical examples of regular graphs with intermediate

density: hypercubes and projective planes (and their generalizations below). Let Qn = {0, 1}n be the hypercube graph.

- Proposition 1.24. (a) Let qn → ∞ and let Gn be the (bipartite) incidence graph of points and hyperplanes in a projective space of order qn and dimension rn. Let


dn = (qr

n − 1) /(qn − 1). Then Gn is dn-regular and (Gn, dn) has large essential girth.

n

(b) Consider a triangular array (Γni, δni) (1 ≤ i ≤ n) of admissible pairs. Let Gn be a subgraph of Γn1 · · · Γnn, and let dn = δn1 + · · · + δnn. As in Example 1.17, assume that (1.1) holds. Then the sequence (Gn, dn) has large essential girth.

In particular, if (G, d) is admissible, then the sequence G n, nd has large essential girth. For example, the sequence (Qn, n) has large essential girth. More generally, if

Gn is any ﬁnite subgraph of the n-dimensional grid Zn, then the sequence (Gn, 2n) has large essential girth.

Proof. (b) We make use of Remark 1.23. It suﬃces to prove that if we do in Gn the random walk deﬁned there, then for any ﬁxed k ≥ 3, the probability that vk−1 exists and is adjacent to v0 tends to 0 as n → ∞. Clearly, the Hamming distance of v0 and vk−1 will be k − 1 ≥ 2 with probability tending to 1 as n → ∞. Indeed, when doing (at most) k − 1 steps, the probability that there will be two steps in the same coordinate goes to zero as n → ∞, because of (1.1).

(a) We omit the subscript n for easier reading. The regularity claim is clear since any hyperplane has d points and any point is on d hyperplanes.

We have

k/2 qr−1 − 1 q − 1

k/2

qr+1 − 1 q − 1

inj(Ck, G) ≤

, whence

![image 25](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile25.png>)

![image 26](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile26.png>)

(qr+1 − 1)k/2−1(qr−1 − 1)k/2 2(qr − 1)k−1 ≤

qr−1 − 1 2(qr − 1)

- 1

![image 27](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile27.png>)

- 2q → 0


tinj(Ck, G, d) ≤

< as n → ∞.

![image 28](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile28.png>)

![image 29](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile29.png>)

Statement (a) is maybe a bit surprising since in a large girth 1-regular sequence

(Gn, dn), the number v(Gn) of nodes would have to be superpolynomial in dn, whereas for projective spaces we have d = (qr − 1)/(q − 1) and

v(G) = 2(qr+1 − 1)/(q − 1) = 2(qd + 1) < 2 dr/(r−1) + 1 .

This means in particular that we cannot delete o(v(Gn)dn) edges from Gn to make the sequence have large girth (if rn ≥ 2 for all n). This is in contrast to the bounded degree case. Thus, the word ‘essential’ is essential. Another instance of this will be Proposition 3.7.

In other words, v(Gn)/dn can go to ∞ arbitrarily slowly (compared to v(Gn) and dn) in a 1-regular sequence of large essential girth: the dimension r and thus the cardinality of the projective space can grow arbitrarily fast compared to the order q, while we have v(G)/d ∼ 2q. A sequence of large essential girth can thus be almost dense. It it easy to see, however, that it cannot be dense:

- Proposition 1.25. If (Gn, dn) is an admissible sequence with large essential girth, where v(Gn) → ∞ and dn = O(v(Gn)), then


dn v(Gn)

2 e(Gn) v2(Gn) → 0

t(K2, Gn, dn) =

![image 30](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile30.png>)

![image 31](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile31.png>)

as n → ∞. Proof. We have

2 e(Gn) v2(Gn)

![image 32](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile32.png>)

![image 33](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile33.png>)

= t(K2, Gn) ≤ 4 t(C4, Gn) = O 4 t(C4, Gn, dn) , where

![image 34](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile34.png>)

t(C4, Gn, dn) = tinj(C4, Gn, dn) + O(1/dn) and tinj(C4, Gn, dn) → 0 as n → ∞. Also,

dn v(Gn)

dn v(Gn)

t(K2, Gn, dn) ≤

.

![image 35](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile35.png>)

![image 36](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile36.png>)

The Proposition follows.

Further important examples of regular sequences of large essential girth are obtained by considering random graphs. Let G(n, d) be the random (almost) d-regular multigraph generated by the conﬁguration model: we take n nodes with d legs emanating from each node, and take a uniform random perfect matching on the dn legs (if dn is odd, leave out a leg). Let G(n, d)simp be the underlying simple graph.

- Proposition 1.26. Fix ǫ > 0. Let dn = O(n1−ǫ) and let the random graph Gn have the distribution of G(n, dn)simp. Then, for any joint distribution of the Gn, the sequence (Gn, dn) a.s. is 1-regular and has large essential girth.

Proof. Let L be the proportion of loops among the edges of G(n, dn). It is easy to see that EL2 = O(1/n2), whence L → 0 a.s.

Let r be so large that (dn/n)r < ∞. For easier reading, we omit the subscript n from dn and Gn. Let M be the proportion of edges in G(n, d) that have a parallel edge. We have

EMr = O((d/n)r), whence M → 0 a.s. Thus, the sequence is a.s. 1-regular. Let k ≥ 3. Using Proposition 1.12, we have

Etrinj(Ck, G, d) ≤ Etinj(Ckr, G, d) +

1 n F

![image 37](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile37.png>)

′

Etinj(F′, G, d) + O

1 n2

![image 38](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile38.png>)

,

where Ckr is the union of r pairwise disjoint k-cycles, and F′ runs over quotients of Ckr into which each component Ck maps injectively, such that F′ has r − 1 components. It is easy to see that Etinj(Ckr, G, d) = O((d/n)r) and Etinj(F′, G, d) = O((d/n)r−1) for each F′, whence Etrinj(Ck, G, d) < ∞ and therefore tinj(Ck, G, d) → 0 a.s.

This concludes our set of examples of sequences with large essential girth. Putting together Propositions 1.9, 1.10, and 1.19, we obtain

- Proposition 1.27. If dn → ∞ and (Gn, dn) is α-regular and has large essential girth, then


- (a) the homomorphism density t(F, Gn, dn) and the injective homomorphism density tinj(F, Gn, dn) converge to αe(F) for any tree F and to 0 for any other connected F;
- (b) the sequence (Gn, dn) is convergent.


In particular, hypercubes, or — more generally — Cartesian powers of a ﬁxed graph, or grids of size n × · · · × n where both n and the dimension tend to ∞, or point-hyperplane incidence graphs of projective spaces whose order tends to ∞, or the random graphs of Proposition 1.26, form convergent sequences.

2. Convergence of spectra

Let σG,d be the uniform probability measure on the v(G) numbers λ/d, where λ runs over the eigenvalues of G. If (G, d) is admissible, then all eigenvalues of G are in [−d, d], so σG,d is supported on [−1, 1]. We have

1

2 e(G) v(G)d2

t(K2, G, d) d ≤

1 d

ǫ2σG,d({x : |x| ≥ ǫ}) ≤

x2dσG,d(x) =

. This proves

=

![image 39](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile39.png>)

![image 40](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile40.png>)

![image 41](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile41.png>)

−1

- Proposition 2.1. Let (Gn, dn) be an admissible sequence with dn → ∞. Then the


n,dn converges weakly to the Dirac measure at 0. More precisely,

measure σn = σG

σn((−ǫ, ǫ)) ≥ 1 − 1/(ǫ2dn) for all n and all ǫ > 0.

This is probably well known but I couldn’t ﬁnd a reference. Up to now, we used only the second moment of σG,d, but to get more precise

results for convergent sequences, we shall need the other moments as well. The zeroth moment is 1, the ﬁrst moment is 0, and we have

hom(Ck, G) v(G)dk

xkdσG,d(x) =

=

![image 42](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile42.png>)

t(Ck, G, d) d

![image 43](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile43.png>)

for k ≥ 3. In fact, this formula holds for k ≥ 1 if we agree that C2 = K2 and C1 is a node with a loop. We infer

Lemma 2.2. Let (Gn, dn) be convergent and g : [−1, 1] → R be continuous. Then

1

x2g(x)dσG

dn

n,dn(x)

−1

converges as n → ∞. Proof. For g(x) = xk, k ≥ 0, the statement is clear from the preceding discussion. The general case follows by the Weierstrass approximation theorem.

For Benjamini–Schramm convergent graph sequences (dn independent of n), it is well known that the spectral measure converges weakly, to a nontrivial measure in general.

For convergent dense graph sequences, C. Borgs, J. T. Chayes, L. Lovász, V. T. Sós, and K. Vesztergombi (see [9, Subsection 6.3] and [26, Section 11.6]) have given a much more precise description of the limiting behavior of the spectrum than the one in Proposition 2.1. Namely, the k-th largest (resp. k-th smallest) eigenvalue, divided by the number of nodes, converges to the k-th largest (smallest) eigenvalue of the limiting graphon, which is nonnegative (nonpositive).

We shall now show that these two results (bounded degree and dense) carry over to intermediate density — at least partially: we don’t (yet) have limit objects, cf. Section 4.

Let G have all degrees ≤ d. Let 1 ≤ r ≤ v(G) be an integer. Let σG,d,r and σG,d,r′ be the uniform probability measures on the numbers λ/d, where λ runs over the r largest and r smallest eigenvalues of G, respectively. These measures are supported on [−1, 1]. Note that σG,d,v(G) = σG,d,′ v(G) = σG,d. For any r, the probability measures σG,d,r and σG,d,r′ are the restrictions of the measure (v(G)/r)σG,d to the intervals [λr/d, 1] and −1, λv(G)−r+1 , respectively.

- Theorem 2.3. Let (Gn, dn) be a convergent sequence with dn → ∞. Let 1 ≤ rn ≤ v(Gn) (n = 1, 2, . . .) be integers such that rndn/ v(Gn) converges to a positive limit α.


n,dn,rn and σn′ = σG′

n,dn,rn converge weakly to probability measures σ supported on [0, 1] and σ′ supported on [−1, 0], respectively. Proof. We only treat σn since everything works the same way for σn′ .

Then the measures σn = σG

Let λr be the r-th largest eigenvalue of the graph G with all degrees ≤ d. We have

v(G)

0 =

λi ≤ (v(G) − r)λr + rd, whence

i=1

r v(G) − r

λr d ≥ −

. Thus, the measure σn is supported on the halﬂine with left endpoint −

![image 44](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile44.png>)

![image 45](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile45.png>)

rn v(Gn) − rn → 0

![image 46](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile46.png>)

since rn/ v(Gn) ∼ α/dn → 0. Thus, it suﬃces to show that for any 0 < a < b < 1, we have

- (2.1) liminf σn([a, 1]) ≥ limsup σn([b, 1]). Let g : [−1, 1] → [0, 1] be continuous, nondecreasing, g(a) = 0, g(b) = 1.


For all n, either σn([a, 1]) = 1 or σn([a, 1]) = (v(Gn)/rn)σG

n,dn([a, 1]). Hence, liminf σn([a, 1]) = 1 or

1 α

dn α

n,dn =

liminf σn([a, 1]) ≥ liminf

n,dn . On the other hand, for all n, we have σn([b, 1]) ≤ 1 and

gdσG

lim dn gdσG

![image 47](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile47.png>)

![image 48](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile48.png>)

v(Gn) rn

σn([b, 1]) ≤ gdσn ≤

n,dn. Hence, limsup σn([b, 1]) ≤ 1 and

gdσG

![image 49](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile49.png>)

1 α

dn α

n,dn =

limsupσn([b, 1]) ≤ limsup

n,dn , and the inequality (2.1) follows.

gdσG

lim dn gdσG

![image 50](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile50.png>)

![image 51](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile51.png>)

3. Graph polynomials

The convergence of a sequence (Gn, dn) was deﬁned in Section 1 by the convergence of certain graph parameters, the homomorphism densities. This forces certain further parameters to converge (sometimes only under further conditions); such parameters are called estimable (some parameters are only estimable for a certain class of convergent sequences). Theorem 2.3 can be thought of as an estimability statement. In this section, we present some more estimable parameters.

Following the paper [11] by P. Csikvári and the present author, let f be an isomorphism-invariant monic multiplicative graph polynomial of linearly bounded exponential type. I.e.,

- • for every graph G, a monic polynomial f(G, x) ∈ C[x] of degree v(G) is given,
- • f(G1, x) = f(G2, x) if G1 ≃ G2,
- • f(G1 ∪ G2, x) = f(G1, x)f(G2, x) for any disjoint union,


•

f(G, x + y) =

f(G[S], x)f(G[V (G) − S], y)

S⊆V (G)

for all G, and ﬁnally

•

- (3.1) {|f′(G[S], 0)| : v ∈ S ⊆ V (G), |S| = t} ≤ (cd)t−1


for all G with maximal degree ≤ d, all v ∈ V (G), and all t ≥ 1, with a constant c depending only on f.

Examples include the chromatic, adjoint, and Laplacian characteristic polynomials, and also the modiﬁed matching polynomial deﬁned as

⌊v(G)/2⌋

(−1)kmk(G)xv(G)−k,

M(G, x) =

k=0

where mk(G) is the number of matchings in G that consist of k edges.

The characteristic polynomial f(G, x) = det(xI−AG) of the adjacency matrix of G is not a valid example because it is not of exponential type. Nevertheless everything that follows, including Theorem 3.1 below, applies to this case in a trivial way; in fact, much more is true, even without assuming graph convergence, as we have seen in Proposition 2.1.

We wish to study the distribution of roots of f(G, x). By [11, Theorem 1.6], we can choose a constant C depending only on f such that for any G, all roots have absolute value ≤ Cd. It is shown there that C = 7.04 · c is an appropriate choice if c is the constant in (3.1). For some of the speciﬁc graph polynomials mentioned above, smaller appropriate values of C are known.

Let pk(G) be the k-th power sum of the roots of f(G, x). By [11, Theorem 5.6.(b)], for each k ≥ 1, there exist constants ck(F) such that

- (3.2) pk(G) =

2≤v(F)≤k+1

ck(F) inj(F, G)

for all G, where F runs over the isomorphism classes of connected graphs. We also have

p0(G) = v(G) = c0(K1) inj(K1, G), where c0(K1) = 1.

Let νG,d be the uniform probability measure on the points λ/d, where λ runs over the roots of f(G, x). This measure is supported on the disc of radius C and has k-th holomorphic moment

- (3.3)


λk dk

1 v(G)

pk(G) v(G)dk

inj(F, G) v(G)dk

zkdνG,d(z) =

=

=

ck(F)

=

![image 52](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile52.png>)

![image 53](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile53.png>)

![image 54](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile54.png>)

![image 55](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile55.png>)

2≤v(F)≤k+1

f(G,λ)=0

(d − 1)v(F)−2

=

ck(F)

dk−1 tinj(F, G, d) for k ≥ 1.

![image 56](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile56.png>)

2≤v(F)≤k+1

- Theorem 3.1. Let dn → ∞. Let (Gn, dn) be a convergent sequence, or, more generally, an admissible sequence such that t(F, Gn, dn) converges whenever cv(F)−1(F) = 0. Write


t(F, Gn, dn) for the limiting homomorphism density. Set νn = νG

t(F) = lim

n→∞

n,dn.

- (1) For all k ≥ 0, we have

zkdνn(z) →

v(F)=k+1

ck(F)t(F) as n → ∞.

- (2) For any function g(z) that is continuous for |z| ≤ C and harmonic for |z| < C, the integral g(z)dνn(z) converges as n → ∞.
- (3) For any |ξ| > C, the normalized absolute value

v(Gn)

![image 57](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile57.png>)

|f(Gn, ξdn)|

![image 58](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile58.png>)

dn of f converges to a positive limit.

- (4) If f(Gn, x) has only real roots for all n, then νn converges weakly.


For the bounded degree case, the analogous theorem is [11, Theorem 1.10], which, in turn, was a generalization (with a simpler proof) of the result of M. Abért and T. Hubai [2, Theorems 1.1, 1.2], who ﬁrst discovered this phenomenon in the case of the chromatic polynomial. For the dense case, essentially the same was proved by P. Csikvári, J. Hladký, T. Hubai and the author in [12, Theorems 1.4, 1.5, 4.3], using the approach of [11]. The proof carries over to intermediate density almost unchanged.

Proof. (1) The 0-th moment is always 1. Let k ≥ 1. From (3.3), we have

(dn − 1)v(F)−2 dk−1 n

zkdνn(z) =

ck(F)

ck(F)t(F) as n → ∞.

tinj(F, Gn, dn) →

![image 59](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile59.png>)

2≤v(F)≤k+1

v(F)=k+1

- (2) The claim follows from (1) because g(z) can be uniformly approximated by real parts of polynomials.
- (3) For any G, d, and ξ, we have

log

v(G)

![image 60](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile60.png>)

|f(G, ξd)| d

![image 61](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile61.png>)

=

1 v(G)

![image 62](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile62.png>)

log |f(G, ξd)| dv(G)

![image 63](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile63.png>)

=

1 v(G)

![image 64](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile64.png>)

log

v(G)

i=1

ξ −

λi d

![image 65](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile65.png>)

,

where the λi are the roots of f(G, x). The last expression can be rewritten as

1 v(G)

![image 66](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile66.png>)

v(G)

i=1

log ξ −

λi d

![image 67](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile67.png>)

= g(z)dνG,d, where g(z) = log |ξ − z|. The claim now follows from the previous statement

(2).

- (4) The claim follows from (1) because each νn is supported on the interval [−C, C].


- 3.1. Number of proper colorings (large essential girth case). We now wish to prove, for intermediate density graph sequences of large essential girth, a qualitative variant of Abért and Hubai’s [2, Theorem 1.4] about the asymptotic number of proper colorings. They only treated the large girth case, but gave an explicit bound on the error in their formula.


Let ch(G, x) be the chromatic polynomial of the graph G. I.e., for integral q ≥ 0, ch(G, q) is the number of proper q-colorings of G.

Theorem 3.2. Let (Gn, dn) be a sequence of large essential girth, such that dn → ∞ and

2 e(Gn)

v(Gn)dn → t(K2) as n → ∞. Let |ξ| ≥ 8. Then

t(K2, Gn, dn) =

![image 68](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile68.png>)

- (3.4)

v(Gn)

![image 69](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile69.png>)

| ch(Gn, ξdn)|

![image 70](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile70.png>)

|ξ|dn → exp(−t(K2)ℜ(1/2ξ)). Proof. We have

- (3.5)


![image 71](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile71.png>)

v(G)

| ch(G, ξd)| |ξ|d

log

=

![image 72](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile72.png>)

= −

z ξ

log 1 −

![image 73](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile73.png>)

|z|≤C

∞

z ξ

1 kℜ

![image 74](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile74.png>)

![image 75](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile75.png>)

|z|≤C

k=1

dνG,d(z) =

k

dνG,d(z),

where νG,d is the uniform probability measure on the v(G) points λ/d for which ch(G, λ) = 0, and C < 8 is Sokal’s constant such that |λ| ≤ Cd for all λ. The series on the right hand side of (3.5) converges uniformly in G and d.

By [11, Theorem 6.6], in the formula (3.2) for the power sum pk(G) of the roots of ch(G, x), the coeﬃcient ck(F) is 0 unless F is 2-connected. On the other hand, tinj(F, Gn, dn) → 0 if F contains a cycle. Thus, ck(F)tinj(F, Gn, dn) → 0 unless F is a 2-connected tree, i.e., F = K2. Note also that c1(K2) = 1/2 because p1(G) = e(G) = inj(K2, G)/2. From formula (3.3), we see that zkdνn(z) tends to t(K2)/2 for k = 1 and to 0 for k ≥ 2.

Putting all this together, the logarithm of the left hand side of (3.4) tends to −ℜ(t(K2)/2ξ), as claimed.

- 3.2. Matching measure and graph convergence. In this subsection, we prove intermediate degree analogs of some results of the recent paper [1] by Abért, Csikvári, Kun and the author. Contrary to the bounded degree case treated there, large girth will not play any role in relation to matchings.


- Deﬁnition 3.3. Let G be a graph and let mk(G) denote the number of matchings of size k. Then the matching polynomial µ(G, x) is deﬁned as follows:


⌊v(G)/2⌋

(−1)kmk(G)xv(G)−2k.

µ(G, x) =

k=0

Note that m0(G) = 1. Let d > 0 be an upper bound on all degrees in G. The matching measure ρG,d is deﬁned to be the uniform probability distribution on the points λ/√d, where λ runs over the roots of µ(G, x) (with multiplicity).

![image 76](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile76.png>)

The fundamental theorem for the matching polynomial is the following. Theorem 3.4 (Heilmann and Lieb [23]). (a) The roots of the matching polynomial µ(G, x) are real. (b) If d ≥ 2 is an upper bound for all degrees in G, then all roots of µ(G, x) have absolute value ≤ 2√d − 1.

![image 77](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile77.png>)

Many graph parameters related to matchings can be read oﬀ from the matching measure, for example, the number

⌊v(G)/2⌋

M(G) =

mk(G)

k=0

of all matchings and the number pm(G) = mv(G)/2 of perfect matchings. The latter is zero if v(G) is odd.

Proposition 3.5.

- (3.6) log

M(G)2/v(G) d

![image 78](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile78.png>)

=

2

−2

log

1 d

![image 79](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile79.png>)

+ x2 dρG,d(x).

- (3.7) log


pm(G)2/v(G) d

2

= 2

log |x|dρG,d(x). Proof. (3.6) The number of matchings in G is

![image 80](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile80.png>)

−2

Thus,

⌊v(G)/2⌋

mk(G) = |µ(G, √

![image 81](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile81.png>)

M(G) =

−1)|.

k=0

=

2

log

−2

log |µ(G, √

![image 82](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile82.png>)

- 1

![image 83](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile83.png>)

- 2


- 1

![image 84](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile84.png>)

- 2


−1)| v(G) −

log M(G) v(G) −

log d =

log d =

![image 85](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile85.png>)

![image 86](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile86.png>)

√

2

![image 87](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile87.png>)

1 d

- 1

![image 88](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile88.png>)

- 2


−1 √d − x dρG,d(x) =

+ x2 dρG,d(x).

log

![image 89](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile89.png>)

![image 90](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile90.png>)

![image 91](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile91.png>)

−2

- (3.7) The number of perfect matchings in G is pm(G) = |µ(G, 0)|.


Thus,

log pm(G) v(G) −

![image 92](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile92.png>)

- 1

![image 93](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile93.png>)

- 2


log |µ(G, 0)| v(G) −

log d =

![image 94](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile94.png>)

- 1

![image 95](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile95.png>)

- 2


log d =

2

log |x|dρG,d(x).

−2

Let

√4 − x2 2π

![image 96](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile96.png>)

w(x) =

(−2 ≤ x ≤ 2)

![image 97](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile97.png>)

denote Wigner’s semicircle density function. The semicircle distribution on the interval [−2β, 2β] is the distribution of βX, where X is a random variable with density w.

Theorem 3.6. Let dn → ∞. Let (Gn, dn) be an admissible sequence with matching measures ρn = ρG

n,dn.

- (a) If t(F, Gn, dn) is convergent for any tree F, then the sequence of matching measures ρn converges weakly to a probability measure ρ on [−2, 2]. Moreover, we have


M(Gn)2/v(Gn) dn ≤ 2

2

limsup

log

log |x|dρ(x).

![image 98](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile98.png>)

n→∞

−2

- (b) If the sequence (Gn, dn) is α-regular, then ρ is the semicircle distribution on the interval [−2√α, 2√α], and we have


![image 99](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile99.png>)

![image 100](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile100.png>)

M(Gn)2/v(G

n)

α e

- (3.8) limsup


dn ≤

.

![image 101](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile101.png>)

![image 102](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile102.png>)

n→∞

For example, the matching polynomial of the complete graph Kn is the n-th Hermite polynomial, so (b) recovers the ancient fact that root distributions of Hermite polynomials converge to the semicircle law [19, 20, 24, 33]. Similarly, complete bipartite graphs Kn,n yield Laguerre polynomials.

When each graph Gn is dn-regular, the ﬁrst statement in (b) has been also independently obtained by Abért, Csikvári and Hubai with a diﬀerent proof (unpublished), and the inequality in (b) follows from the much stronger result of Davies, Jenssen, Perkins and Roberts [13, Theorem 4].

n) ∼ dn/e, which is well known to follow from classical results of Brègman (≤) and Schrijver (≥), see [27, pp. 311–312]. From the inequality in (b), we see that M(Gn)2/v(G

When each graph Gn is dn-regular and bipartite, pm(Gn)2/v(G

n) ∼ dn/e as well, and we only need Schrijver’s lower bound

(d − 1)d−1 dd−2 ∼

- d

![image 103](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile103.png>)

- e


pm(G)2/v(G) ≥

![image 104](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile104.png>)

(d → ∞)

on the number of perfect matchings to get this. Note that Propp’s 1999 survey on the enumeration of matchings cites [10] for the asymptotic formula for the number of perfect matchings of the hypercube, and asks for a formula for the number of all matchings [30, Problem 19].

Leaving regular graphs, note that statement (a) applies in particular to the special case when (Gn, dn) is convergent. The ﬁrst claim in (a), for the special case of convergent dense graph sequences, is [12, Theorem 4.3] of Csikvári, Hladký, Hubai and the author.

We prove Theorem 3.6.

Proof. By the Heilmann–Lieb Theorem, the measures ρn are all supported on [−2, 2]. We shall exploit the relation between the modiﬁed and the ordinary matching polynomial: M(G, x2) = xv(G)µ(G, x). Let νG,d be the uniform probability measure on the points λ/d, where λ runs over the roots of the modiﬁed matching polynomial M(G, x). This measure is supported on the interval [0, 4].

There is a very nice interpretation of the 2k-th power sum of the roots of the matching polynomial µ(G, x). It counts the number of closed tree-like walks of length 2k in the graph G [21, Chapter 6]. Note that for k ≥ 1, this is twice the k-th power sum of the roots of the modiﬁed matching polynomial M(G, x). Thus, in the formula

- (3.2) written for the graph polynomial M(G, x), the coeﬃcient ck(F) is half the number of tree-like walks of length 2k in F that use all edges of F, divided by aut F. Thus, cv(F)−1 = 0 unless F is a tree.


n,dn. By Theorem 3.1(4), νn converges weakly as n → ∞. But from νG,d we get ρG,d by decreasing the mass at 0 by 1/2 and then relocating the mass of any point x to both points ±

(a) Let νn = νG

√x, so as to get a probability measure again. This operation clearly preserves weak convergence. Thus, ρn also converges weakly to a measure ρ.

![image 105](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile105.png>)

Let u(x) = 2 log |x| and

1 k

+ x2 for k = 1, 2, . . .. Then

uk(x) = log

![image 106](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile106.png>)

M(G)2/v(G) d ≤

2

log

ukdρG,d if d ≥ k. Thus, for any k,

![image 107](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile107.png>)

−2

M(Gn)2/v(Gn) dn ≤ lim

2

2

limsup

log

ukdρn =

ukdρ,

![image 108](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile108.png>)

n→∞

n→∞

−2

−2

since the measures ρn are supported on the compact interval [−2, 2] not depending on n, and uk is continuous and bounded on [−2, 2].

Since uk ≥ uk+1 and uk → u pointwise, the claim follows using the Monotone Convergence Theorem.

(b) Matching measures are symmetric about 0, and so is the semicircle measure, so it suﬃces to show convergence of even moments of ρn to those of the semicircle law. Let k ≥ 1. By Theorem 3.1, we have

2

4

x2kdρn(x) = 2

xkdνn(x) →

- (3.9)


2ck(F)t(F),

−2

0

v(F)=k+1

where

t(F, Gn, dn) = αk

t(F) = lim

n→∞

by Proposition 1.19. So the limit in (3.9) is αk times the number of nonisomorphic pairs (F, γ), where F is a tree with k+1 nodes and γ is an Eulerian trail in the graph

- F˜ which is F with all edges doubled. These pairs (F, γ) correspond to Dyck words of length 2k, so their number is the Catalan number


2

1 k + 1

2k k

x2kw(x)dx = EX2k, where X has density w. Therefore

=

![image 109](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile109.png>)

−2

2

2

x2kdρn(x) = αkEX2k = E √αX 2k as claimed.

x2kdρ(x) = lim

![image 110](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile110.png>)

n→∞

−2

−2

The inequality (3.8) is immediate from statement (a) and the fact that

2

- 1

![image 111](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile111.png>)

- 2


, cf. [22, integral 4.241.9].

w(x) log|x|dx = −

−2

- 3.3. Spectral measure rescaled (regular, large girth case). We know from


- Proposition 2.1 that scaling down the spectrum by the degree bound d → ∞ leads to trivial behavior in terms of weak convergence. What happens if we only scale down by √d ?


![image 112](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile112.png>)

Let ΣG,d be the uniform probability measure on the v(G) points λ/√d, where λ runs over the eigenvalues of G. If all degrees in G are ≤ d, then ΣG,d is supported on the interval −

![image 113](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile113.png>)

√d, √d .

![image 114](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile114.png>)

![image 115](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile115.png>)

- Proposition 3.7. Let (Gn, dn) be an α-regular sequence of large girth, such that


n,dn. Then, for each k ≥ 0,

dn → ∞. Let Σn = ΣG

√

![image 116](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile116.png>)

d

2

√αx k w(x)dx

xkdΣn →

![image 117](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile117.png>)

- (3.10)


√

![image 118](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile118.png>)

−2

−

d

as n → ∞. Thus, Σn converges weakly to the semicircle distribution on the interval [−2√α, 2√α].

![image 119](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile119.png>)

![image 120](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile120.png>)

Note that the limit in (3.10) is 0 for k odd and is αk/2 times the Catalan number

k

1 k/2+1

k/2 for k even. Proof. We have

![image 121](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile121.png>)

√

![image 122](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile122.png>)

k

d

λ √dn

1 v(Gn)

hom(Ck, Gn) v(Gn)dk/n 2

xkdΣn =

.

=

![image 123](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile123.png>)

![image 124](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile124.png>)

![image 125](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile125.png>)

√

![image 126](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile126.png>)

![image 127](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile127.png>)

−

d

For n ≥ n0(k), all walks in Gn of length k are tree-like, whence

√

![image 128](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile128.png>)

2

2

d

√αx k w(x)dx

xkdΣn(x) =

xkdρn(x) →

![image 129](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile129.png>)

√

![image 130](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile130.png>)

−2

−2

−

d

as n → ∞, by Theorem 3.6. To deduce the weak convergence, we use that the semicircle measure is compactly supported.

A diﬀerent proof is possible based on the fact that Kesten–McKay measures converge to the semicircle law.

For random graphs, results similar to Proposition 3.7 have been proved by Dumitriu and Pal [15] and by Tran, Vu and Wang [34]. Those results are of course much deeper than Proposition 3.7.

- Proposition 3.7 fails for large essential girth, even if each Gn is exactly dn-regular.


Indeed, for the hypercube sequence (Qd, d), the measure Σd is the (binomial) distribution of

√

![image 131](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile131.png>)

(X1 + · · · + Xd)/

d,

where the Xi are i.i.d. random variables with P(X1 = 1) = P(X1 = −1) = 1/2, see [25, Exercise 11.9]. Thus, Σd converges weakly to the standard Gaussian distribution and not to the semicircle distribution, therefore its moments do not all converge to those of the semicircle law.

4. Graphonings We propose a common generalization of graphons and graphings.

- Deﬁnition 4.1. A graphoning is a tuple G = (X, B, λ, µ, W), where (X, B, λ) is a probability space, µ : B → [0, ∞] is a measure, and W : X2 → [0, 1] is a symmetric (B ⊗ B)-measurable function such that


- • (degree bound)


degX(x) def=

W(x, y)dµ(y) ≤ 1 for all x ∈ X,

X

- • (degree measurability)


- (4.1) degA(x) def=


W(x, y)dµ(y) is a measurable function of x ∈ X for all A ∈ B, and

A

• (measure preserving property)

- (4.2)


degB dλ =

degA dλ for all A, B ∈ B.

A

B

A graphoning with λ = µ is the same thing as a graphon, except that graphons are measurable only w.r.t. the completion of B ⊗ B, and thus their degrees are only almost measurable. A graphoning on a Borel probability space (X, B, λ), such that µ is the counting measure divided by d, and W only takes values in {0, 1}, is the same thing as a graphing.

For these two special cases of graphonings, it is known that degree measurability follows from the degree bound condition. It is unclear to the author whether this holds for general graphonings, maybe under the assumption that the σ-algebra B is Borel.

Note that µ is not in general σ-ﬁnite, so the Fubini Theorem is not applicable to the iterated integrals in (4.2).

- 4.1. Sub-Markov kernels and rooted homomorphism densities. We wish to generalize the homomorphism densities of graphons that play a fundamental role in the limit theory of dense graphs developed by László Lovász and his coauthors [9, 26, 28]. Technical diﬃculties are caused by the lack of the Fubini Theorem, but these can be dealt with. We treat rooted homomorphism densities ﬁrst. Even this requires some preparation. It will save work later on if we introduce structures even more general than graphonings. For this, let us recall a basic concept from the theory of Markov chains. Deﬁnition 4.2. A sub-Markov kernel on a measurable space (X, B) is a function


deg : X × B → [0, 1] (x, A)  → degA(x)

such that the function degA : x  → degA(x) is measurable for all A ∈ B and the set function deg(x) : A  → degA(x) is a measure for all x ∈ X.

Clearly, the degree function of a graphoning is a sub-Markov kernel. The measura-

bility of degA implies its seemingly stronger form below. This is probably well known but we prove it to be self-contained.

Lemma 4.3. Consider a sub-Markov kernel deg on the measurable space (X, B). If (Z, C) is a measurable space and f : X × X × Z → [0, 1] is measurable, then

degf(x, z) def=

f(x, y, z)ddeg(x)(y) is a measurable function of (x, z) ∈ X × Z, and takes values only in [0, 1]. Proof. We have

X

0 ≤ degf(x, z) ≤ degX(x) ≤ 1 for all x and z.

The function degf is measurable, by the deﬁnition of a sub-Markov kernel, when f is the indicator of a direct product of measurable sets. By linearity, it is measurable when f is the indicator of a ﬁnite union of such products. By the Monotone Convergence Theorem, it follows that the set of measurable functions f : X ×X ×Z → [0, 1] such that degf is measurable is closed under monotone pointwise limits and therefore contains all measurable indicator functions, thus all measurable stepfunctions.

Any measurable function to [0, 1] can be uniformly approximated by measurable stepfunctions. An error with uniform upper bound ǫ in f leads to an error with uniform upper bound ǫ in degf(x, z). This proves the Lemma because a uniform limit of measurable functions is measurable.

Corollary 4.4. If deg is a sub-Markov kernel on (X, B) and f : X → [0, 1] is measurable, then the function degf : X → [0, 1] deﬁned by

degf(x) def=

fddeg(x)

X

is measurable and takes values only in [0, 1]. Proof. Use Lemma 4.3 for F(x, y, z) = f(y), with Z = {z} being a single point.

- Deﬁnition 4.5. A sub-Markov kernel deg on a measurable space (X, B) is compatible with a (B ⊗ B)-measurable function W : X2 → [0, 1] if


- (4.3)


W(x2, y)ddeg(x1)(y) =

W(x1, y)ddeg(x2)(y)

A

A

for all x1, x2 ∈ X and all A ∈ B. Lemma 4.6. In a graphoning, deg is compatible with W. Proof. Both sides of (4.3) equal

W(x1, y)W(x2, y)dµ(y). Indeed, this is a special case of the well-known formula

A

dν dµ

f

fdν involving a Radon-Nikodym derivative.

dµ =

![image 132](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile132.png>)

A

A

To deﬁne rooted homomorphism densities, we will have to introduce labelings on the test graphs F. The compatibility discussed above will ensure that the density is independent of the labeling chosen.

Deﬁnition 4.7. An admissible labeling of a connected graph F is a bijection φ : V (F) → {0, 1, . . ., v(F) − 1}

such that for all 1 ≤ i ≤ v(F), the nodes with labels less than i span a connected subgraph. Two admissible labelings are adjacent if a transposition (i − 1, i) of labels takes one to the other. This turns the set of admissible labelings of F into a graph.

Lemma 4.8. (a) For any connected graph F, the graph of admissible labelings is connected. (b) The admissible labelings such that a ﬁxed node o gets label 0 span a connected subgraph.

Proof. (b) Consider two admissible labelings φ and ψ such that φ(o) = ψ(o) = 0. We prove that they are connected by a path. We use induction on the number of inversions between them, i.e., the number of pairs x, y ∈ V (F) such that

(φ(x) − φ(y))(ψ(x) − ψ(y)) < 0.

If there are no inversions, then φ = ψ. If there are inversions, then there are nodes x and y such that φ(x) = i, φ(y) = i + 1, ψ(x) > ψ(y). Choose such x and y so that i is largest possible. Since ψ is admissible, there is an edge in F from y to a node z with ψ(z) < ψ(y) and therefore φ(z) < i. Thus, composing φ with the transposition (i, i + 1) yields an admissible labeling φ′ that has less inversions when compared to ψ than φ does.

- (a) We may assume that F has at least two nodes. It suﬃces to show that for


any two adjacent nodes x and y in F, there exist adjacent admissible labelings φ and ψ such that φ(x) = ψ(y) = 0. Let φ be an admissible labeling with φ(x) = 0 and φ(y) = 1. Let ψ arise from φ by swapping the labels of x and y. Then ψ is admissible and adjacent to φ.

Deﬁnition 4.9. Let G = (X, B, W, deg) be a measurable space endowed with a symmetric measurable function W : X2 → [0, 1] and a sub-Markov kernel deg that is compatible with W. Let x0 ∈ X. Let (F, o) be a connected rooted graph. Fix any admissible labeling of V (F) such that o gets label 0. For any label i = 1, . . ., v(F)−1, let j(i) be a label such that j(i) < i and j is adjacent to i in F. Note that j(1) = 0. Let T be the spanning tree consisting of the edges (i, j(i)). We deﬁne the rooted homomorphism density

t((F, o), (X, x0)) =

· · ·

W(xk, xl)ddeg(xj(v(F)−1))(xv(F)−1) · · ·ddeg(xj(1))(x1).

=

X

X kl∈E(F)−E(T)

- Proposition 4.10. The rooted homomorphism density


- (a) is well deﬁned, is in [0, 1], is measurable as a function of x0, and
- (b) is independent of the admissible labeling and the function j chosen.
- (c) If F is a tree, then it is also independent of the function W.


Proof. (a) By repeated application of Proposition 4.3, we see that each integration yields a measurable function of the remaining variables, with values in [0, 1].

(b) For a given admissible labeling, the rooted homomorphism density does not depend on the function j because of the condition (4.3).

Let us assume that V (F) = {0, 1, . . ., v(F) − 1}, and the identity as well as the transposition (i−1, i) are admissible labelings, where i ≥ 2 is ﬁxed. Then j(i) < i−1 and we may apply the Fubini Theorem to swap the two factors

ddeg(xj(i))(xi)ddeg(xj(i−1))(xi−1), showing that the two admissible labelings in consideration deﬁne the same value of the rooted homomorphism density.

An application of Lemma 4.8(b) ﬁnishes the proof. (c) The product in Deﬁnition 4.9 is empty if F = T. Deﬁnition 4.9 may be frightening, but it becomes much nicer for graphonings. From

now on, we abbreviate dµ(xi) to dxi.

Remark 4.11. Consider a graphoning G = (X, B, λ, µ, W) with a speciﬁed point x0 ∈ X. Let (F, o) be a connected rooted graph. Then we have

t((F, o), (G, x0)) =

· · ·

W(xi, xj)dxv(F)−1 · · ·dx1

X

X ij∈E(F)

if V (F) is admissibly labeled by 0, 1, ..., v(F) − 1 so that o gets label 0. Note that the Fubini theorem is not directly applicable to the right hand side of this formula because µ is not in general σ-ﬁnite. Note also that λ plays no role here.

- 4.2. Reversible kernels and unrooted homomorphism densities. To deﬁne unrooted homomorphism densities, we will need the measure preserving property (4.2). Again it is worthwhile to generalize this ﬁrst. We recall another basic concept from Markov chain theory.


Deﬁnition 4.12. A sub-Markov kernel deg on a probability space (X, B, λ) is reversible w.r.t. λ if the measure preserving condition (4.2) holds.

In particular, the degree function of a graphoning is reversible. On a measurable space (X, B), there can be many probability measures that make a given sub-Markov kernel deg reversible. We call such measures λ involution-invariant w.r.t. deg because if we choose a λ-random point a ∈ X and then a point b ∈ X with conditional (sub-probability) distribution deg(a), then the pairs (a, b) and (b, a) have the same (sub-probability) distribution. Indeed, (4.2) precisely means the equality of these two measures on measurable product sets A × B ⊆ X2, and this implies equality on the entire σ-algebra B⊗B. This implies the following well-known, crucial fact.

Lemma 4.13. If deg is a reversible sub-Markov kernel on a probability space (X, B, λ), and f : X2 → [0, 1] is measurable, then

(f(x, y) − f(y, x))ddeg(x)(y)dλ(x) = 0.

X X

- Corollary 4.14. If deg is a reversible sub-Markov kernel on (X, B, λ) and f, g : X → [0, 1] are measurable functions, then

(4.4)

X

f · degg dλ =

X

g · degf dλ. Proof. Use Lemma 4.13 for F(x, y) = f(x)g(y).

- Corollary 4.15. If deg is a reversible sub-Markov kernel on (X, B, λ) and f : X2 → [0, 1] is a symmetric (B ⊗ B)-measurable function, then the sub-Markov kernel f deg deﬁned by


(f deg)A(x) =

f(x, y)ddeg(x)(y)

A

is again reversible. Proof. The fact that f deg is a sub-Markov kernel follows from Lemma 4.3. For reversibility, we need to show that the value

f(x, y)ddeg(x)(y)dλ(x) is symmetric w.r.t A and B. This is Lemma 4.13 for F(x, y) = 1A(x)f(x, y)1B(y).

(f deg)Bdλ =

A

A B

Deﬁnition 4.16. A pseudo-graphoning is a probability space (X, B, λ) endowed with a symmetric (B⊗B)-measurable function W : X2 → [0, 1] and a reversible sub-Markov kernel deg that is compatible with W.

Every graphoning is also a pseudo-graphoning. A pseudo-graphoning is a graphoning if and only if there exists a measure µ : B → [0, ∞] such that the equality (4.1) holds for all x ∈ X and A ∈ B.

Proposition 4.17. If G = (X, B, λ, W, deg) is a pseudo-graphoning and f : X2 → [0, 1] is symmetric and (B ⊗ B)-measurable, then fG = (X, B, λ, fW, f deg) is also a pseudo-graphoning.

Proof. The function fW is symmetric and measurable. By Corollary 4.15, f deg is a reversible sub-Markov kernel. It remains to check that f deg is compatible with fW, which is trivial.

Corollary 4.18. If G = (X, B, λ, µ, W) is a graphoning and f : X2 → [0, 1] is symmetric and (B⊗B)-measurable, then fG = (X, B, λ, µ, fW) is also a graphoning.

Proof. We have

(fW)(x, y)dµ(y) = (f deg)A(x), so the claim follows from the previous Proposition.

A

This is a generalization of [26, Lemma 18.19] from László Lovász’s monograph: a Borel subgraph of a graphing is a graphing.

Using reversibility, we can deﬁne unrooted homomorphism densities.

Deﬁnition 4.19. Consider a pseudo-graphoning G = (X, B, λ, W, deg). Let F be a connected graph. Choose a root o in F. Choose x0 ∈ X randomly with distribution λ. We deﬁne the homomorphism density

- (4.5) t(F, G) = Et((F, o), (G, x0)) =


t((F, o), (G, x0))dλ(x0).

X

Since the rooted homomorphism density is a measurable function of x0 and takes values in [0, 1] only, the expectation above exists and is in [0, 1]. Proposition 4.20. (a) The homomorphism density t(F, G) is independent of the

root o. (b) If F is a tree, then it is also independent of the function W.

Proof. (a) Given two adjacent nodes o0 and o1 in F, consider an admissible labeling such that o0 and o1 get labels 0 and 1 respectively. For each i ≥ 2, let j(i) < i be such that the nodes with labels i and j(i) are adjacent, and let T be the spanning tree given by the edges (i, j(i)) and (01). Consider the birooted homomorphism density

f(x0, x1) =

· · ·

W(xk, xl)ddeg(xj(v(F)−1))(xv(F)−1) · · ·ddeg(xj(2))(x2).

X

X kl∈E(F)−E(T)

This does not depend on the function j chosen because deg is compatible with W. We have

t((F, o0), (G, x0)) =

f(x0, x1)ddeg(x0)(x1)

X

and

t((F, o1), (G, x0)) =

f(x1, x0)ddeg(x0)(x1)

X

— note that the labeling that arises by swapping the labels 0 and 1 is also admissible. These two rooted densities have the same expectation by Lemma 4.13.

(b) Immediate from Proposition 4.10(c). Remark 4.21. Let F be a connected graph.

For a graphoning G = (X, B, λ, µ, W), we have t(F, G) =

W(xk, xl)dxv(F)−1 · · ·dx1dλ(x0)

· · ·

X X

X kl∈E(F)

if V (F) is admissibly labeled by 0, 1, ..., v(F) − 1. Note again that the Fubini theorem is not directly applicable to the right hand side of this formula because µ is not in general σ-ﬁnite.

For a graphon G — which is a graphoning with µ = λ — we recover the well-known homomorphism density

t(F, G) =

W(xk, xl)

dλ(xi).

XV (F) kl∈E(F)

i∈V (F)

For a graphing G — which is a graphoning with µ being (1/d) times the counting measure — we recover a normalized version of the the well-known homomorphism frequency:

t(F, G) = t∗(F, G)/dv(F)−1, where

t∗(F, G) =

hom((F, o), (G, x))dλ(x).

X

For a graph G with all degrees ≤ d, we can deﬁne a graphoning as follows. Let X = V (G) and B = P(X). Let λ be the uniform probability measure on X. Let µ = (v(G)/d)λ. Let W : X2 → {0, 1} be the adjacency matrix of G. This graphoning has the same (rooted and unrooted) homomorphism densities as (G, d).

- 4.3. Graph limits.


Deﬁnition 4.22. A limit for a convergent sequence (Gn, dn) is a pseudo-graphoning

- G such that t(F, Gn, dn) → t(F, G) for all connected F. In this case, we write (Gn, dn) → G. A true limit is a limit which is a graphoning.


In the rest of this paper, our main interest is in the existence of limits. Very little is known. We start with a very special example. Proposition 4.23. Let (Gn, dn) be a convergent sequence such that Gn is the disjoint union of graphs with dn nodes each. Then the sequence has a true limit. Proof. As explained in Example 1.7, there exists a Borel probability measure γ on the compact graphon space W0, such that

t(F, Gn, dn) →

t(F, U)dγ(U) for all connected graphs F.

W0

Let W0 be the space of labeled graphons endowed with the 1-norm — not the cut norm, which is used to deﬁne the topology in W0. I.e., W0 is the subset of the Banach space L1 ([0, 1]2) that consists of all symmetric functions with values in [0, 1]. By [32,

Theorem 1] of Orbanz and Szegedy, there exists a measurable map ξ : W0 → W0 which is a section (one-sided inverse) of the canonical quotient map W0 → W0. Note that for each U ∈ W0, the function ξ(U) ∈ W0 is deﬁned only almost everywhere, but for each f ∈ W0, we may use a variant of [3, Deﬁnition 2.2] to choose a canonical representative which is deﬁned everywhere:

x+ǫ

y+ǫ

1 4ǫ2

f¯(x, y) = limsup

fdλ2,

![image 133](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile133.png>)

ǫ→0

x−ǫ

y−ǫ

where λ2 stands for 2-dimensional Lebesgue measure, and undeﬁned values of f are taken to be zero. It is easy to see that the function

W0 × [0, 1]2 → [0, 1], (f, x, y)  → f¯(x, y) is Borel measurable; this was observed by Viktor Kiss (unpublished). It follows that the function

W0 × [0, 1]2 → [0, 1], (W, x, y)  → ξ(U)(x, y) is also Borel measurable.

![image 134](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile134.png>)

Let X = W0 × [0, 1] and deﬁne W : X2 → [0, 1] by putting

![image 135](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile135.png>)

W((U, x), (V, y)) = 1U=V ξ(U)(x, y). The function W is clearly symmetric and Borel measurable.

For all A ⊆ X, let AU = {x ∈ [0, 1] : (U, x) ∈ A} U ∈ W0 . Let B ⊂ P(X) be the σ-algebra of Borel sets. For all A ∈ B, deﬁne µ(A) =

λ1(AU).

U∈ W0

Let λ = γ × λ1, where λ1 stands for 1-dimensional Lebesgue measure. Let G = (X, B, λ, µ, W). It is straightforward to check that G is a graphoning and

t(F, G) =

t(F, Gn, dn) for all connected graphs F.

t(F, U)dγ(U) = lim

n→∞

W0

- 4.4. Hausdorﬀ limits. We now introduce special graphonings that involve geometric measure theory.


- Deﬁnition 4.24. A Hausdorﬀ graphoning is a graphoning of the form G = (X, B, λ, µ, W),


where X is a metric space, B is the σ-algebra of Borel sets, λ is 1-dimensional Hausdorﬀ measure, and µ is a Hausdorﬀ measure with some gauge function h. I.e., h ≥ 0 is a right-continuous nondecreasing function on a right neighborhood of 0 and

∞

∞

h(diamIi) : diamIi < δ for all i, and B ⊆

µ(B) = lim

inf

Ii for any Borel set B.

δ→0

i=1

i=1

A Euclidean graphoning is a Hausdorﬀ graphoning where X = [0, 1] with the Euclidean metric.

Note that if gauge functions h1 and h2 satisfy (1 − ǫ)h1(x) ≤ h2(x) ≤ (1 + ǫ)h1(x) for 0 ≤ x < δ(ǫ), then they deﬁne the same Hausdorﬀ measure.

The gauge function h(x) = x gives rise to the 1-dimensional Hausdorﬀ measure. For X = [0, 1], this is Lebesgue measure; the corresponding Euclidean graphonings are Borel measurable graphons. The constant gauge function h(x) = 1/d gives rise to the counting measure divided by d; in this case {0, 1}-valued Hausdorﬀ graphonings are graphings.

- Deﬁnition 4.25. A Hausdorﬀ (resp. Euclidean) limit for a convergent sequence (Gn, dn) is a limit which is a Hausdorﬀ (resp. Euclidean) graphoning with a gauge function h such that h(1/ v(Gn)) ∼ 1/dn as n → ∞.


Recall from Deﬁnition 1.1 that the homomorphism density t(F, G, d) involved a normalization by an appropriate power of d in order to be in [0, 1]. The role of the gauge function h is to encode in the limit object not only the limiting homomorphism densities, but also the growth rate of the degree bound dn.

For a convergent sequence (Gn) of dense graphs with v(Gn) = n, a Euclidean limit for the convergent sequence (Gn, n) is the same thing as a limiting (Borel measurable) graphon on [0, 1]. For a Benjamini–Schramm convergent sequence (Gn) with degree bound d and with v(Gn) → ∞, a {0, 1}-valued Euclidean limit for the convergent sequence (Gn, d) is the same thing as a limiting graphing on [0, 1].

Example 4.26. The sequence (Gn, dn) of Example 1.5, provided that v(Γi) ≥ 2 for all i, always has a Hausdorﬀ limit such that in the underlying metric space, all nonzero distances are of the form 1/ v(Gn), and W is {0, 1}-valued.

Proof. Let X = ∞i=1 V (Γi). The distance of two points in x, y ∈ X is deﬁned to be 1/ v(Gn) if n + 1 = inf{i : xi = yi}. The corresponding 1-dimensional Hausdorﬀ measure λ will be the product of the uniform probability measures λi on V (Γi). Set h(1/ v(Gn)) = 1/dn. This is well deﬁned since v(Gn) < v(Gn+1) for all n. The corresponding Hausdorﬀ measure µ will be the product of the measures µi = (v(Γi)/δi)λi. Let G = (X, B, λ, µ, W), where W(x, y) = 1 if xi and yi are adjacent in Γi for all i, and W(x, y) = 0 otherwise. This G is the direct product of the graphonings that correspond to the (Γi, δi) by the end of Remark 4.21. It is easy to see that G is a Hausdorﬀ limit of (Gn, dn).

The author is unable to answer the fundamental Problem 4.27. (a) Which convergent sequences have (true, Hausdorﬀ, Euclidean) limits? (b) Which pseudo-graphonings arise as (Hausdorﬀ) limits?

In the dense case, the Euclidean (i.e., graphon) versions of both questions have been answered by L. Lovász and B. Szegedy [26, 28]; the answer is “all”. In the bounded degree case, the graphing version of (a) was solved by D. Aldous and R. Lyons [4] and by G. Elek [16], see also [26, Theorem 18.37]; the answer is “all”; while the answer “all” for the graphing version of (b) is the Aldous–Lyons Conjecture. (In our setting, we should say “all simple graphings” because we are only allowing simple graphs.)

- 4.5. Acyclicity and regularity. In the remaining part of this paper, our main focus is on constructing limit objects for convergent sequences of large essential girth. First, we characterize when the cycle densities of a graphoning vanish.


- A sub-Markov kernel generates a sub-Markov chain in the usual way:


- Deﬁnition 4.28. Let deg be a sub-Markov kernel on the measurable space (X, B). For x ∈ X, let deg0(x) : B → {0, 1} be the Dirac measure at x. Let deg1 = deg. If i and j are positive integers summing to k, then deﬁne


degiA ddegj(x). This yields a well deﬁned sub-Markov kernel degk on (X, B).

- (4.6) degkA(x) =


X

- Proposition 4.29. Let k ≥ 2. For a graphoning G, the following are equivalent.


- (a) t(Ck+1, G) = 0;
- (b) The neighborhood N(x) = {y ∈ X : W(x, y) > 0} has degk(x)-measure zero for λ-a.e. x;
- (c) degk(x) ⊥ deg(x) (singular measures) for λ-a.e. x ∈ X.


Proof. (a) ⇔ (b): We have t(Ck+1, G) =

W(x, y)ddegk(x)(y)dλ(x). Statement (a) holds if and only if this is zero, i.e.,

X X

W(x, y)ddegk(x)(y) = 0 for λ-a.e. x, which is equivalent to (b).

X

- (b) ⇒ (c): The measure deg(x) is concentrated on the set N(x).
- (c) ⇒ (b): The formula (4.6) for i = 1, together with the deﬁnition (4.1) of deg in


a graphoning, show that degk(x) is absolutely continuous with respect to µ, for all

- x, if k ≥ 1. Assume that degk(x) ⊥ deg(x) for a ﬁxed x; we prove that the set N(x) has degk(x)-measure zero. The set N(x) can be written as a union A ∪ B, where


degkA(x) = degB(x) = 0, because X can be written as such a union, by the deﬁnition of singular measures. By the deﬁnition of the measure deg(x), we have µ(B) = 0,

whence degkB(x) = 0 and therefore degkN(x)(x) = degkA∪B(x) = 0 as claimed.

- Deﬁnition 4.30. Consider a probability space endowed with a sub-Markov kernel: G = (X, B, λ, deg). The space G (or the kernel deg) is acyclic if degk(x) ⊥ deg(x) for λ-a.e. x ∈ X and all 0 ≤ k = 1.

In particular, a graphoning is acyclic if and only if all cycle densities are zero. In the next subsection, we will be interested in limits of regular sequences (of large

essential girth). We now introduce the corresponding limit objects.

- Deﬁnition 4.31. Let 0 ≤ α ≤ 1. Consider a probability space endowed with a sub-Markov kernel: G = (X, B, λ, deg). The space G (or the kernel deg) is α-regular if for all k ≥ 0, and for λ-a.e. x ∈ X, we have degX(y) = α for degk(x)-a.e. y ∈ X.


In particular, a Markov kernel is 1-regular. Regular kernels can be characterized in terms of homomorphism densities of rooted trees. Note that rooted tree densities as in Deﬁnition 4.9 depend neither on the function W — cf. Proposition 4.10(c) —, nor on the probability measure λ, therefore

rooted tree densities of a measurable space endowed with a sub-Markov kernel make sense.

- Proposition 4.32. Consider a probability space endowed with a sub-Markov kernel: G = (X, B, λ, deg). The following are equivalent.


- (a) The space G is α-regular.
- (b) For λ-a.e. x ∈ X, we have

t((Pk+2, o), (G, x)) = αk+1 and

t((Dk+3, o), (G, x)) = αk+2 for all k ≥ 0, where o is a leaf (farthest from the trivalent node in the case of Dk+3, k ≥ 1), except in D3, where o is the non-leaf.

- (c) For all rooted trees (F, o), we have t((F, o), (G, x)) = αe(F) for λ-a.e. x ∈ X.


Proof. Assuming (a), we easily get (c) by induction on v(F). The implication (c) ⇒

- (b) is trivial. Assuming (b), we prove (a). We have


αk = t((Pk+1, o), (G, x)) =

ddegk(x)(y),

X

degX(y)ddegk(x)(y), and

αk+1 = t((Pk+2, o), (G, x)) =

X

(degX(y))2ddegk(x)(y)

αk+2 = t((Dk+3, o), (G, x)) =

X

for all k ≥ 0 and λ-a.e. x ∈ X; note that P1 ≃ K1. From the condition of equality in the Cauchy–Schwarz inequality, we see that for all k, there exists an αk such that for λ-a.e. x ∈ X, we have degX(y) = αk for degk(x)-a.e. y ∈ X. Then

α0 · · ·αk = t((Pk+2, o), (G, x)) = αk+1

for all k ≥ 0 and λ-a.e. x ∈ X. If α > 0, then this implies that αk = α for all k, and G is α-regular. If α = 0, then we get α0 = 0, i.e., degX(x) = 0 for λ-a.e. x ∈ X. But then degk(x) = 0 for λ-a.e. x ∈ X and all k ≥ 1, and therefore G is 0-regular.

For reversible kernels, the characterization of regularity becomes much nicer.

- Lemma 4.33. Let 0 ≤ α ≤ 1. Consider a probability space endowed with a reversible sub-Markov kernel: G = (X, B, λ, deg). The space G is α-regular if and only if for λ-a.e. x ∈ X, we have degX(x) = α.


Proof. If G is α-regular, then for λ-a.e. x ∈ X, we have degX(y) = α for deg0(x)-a.e.

- y ∈ X. But deg0 is Dirac measure at x, so we have degX(x) = α for λ-a.e. x ∈ X, as claimed.


Conversely, assume that the set A = {y ∈ X : degX(y) = α} has λ(A) = 0. What we want to prove is that degkA(x) = 0 for all k ≥ 0 and λ-a.e. x ∈ X. Let Ak = {x ∈ X : degkA(x) > 0}. We use induction on k to show that λ(Ak) = 0. For k = 0, this holds because A0 = A. If it holds for k−1, then it also holds for k because

degAk−1 ddeg(x) =

degAk−1 ddeg(x) = 0

degkA(x) =

X

Ak−1

for λ-a.e. x ∈ X. Indeed, degA

k−1

(x) = 0 for λ-a.e. x ∈ X because

degA

dλ =

degX dλ = 0 by reversibility of the kernel deg and by the induction hypothesis.

k−1

X

Ak−1

Regular reversible kernels can be characterized in terms of homomorphism densities of trees. Recall from Proposition 4.20(b) that tree densities of a pseudo-graphoning do not depend on the function W, therefore tree densities of a probability space endowed with a reversible sub-Markov kernel make sense.

- Proposition 4.34. Consider a probability space endowed with a reversible sub-Markov kernel: G = (X, B, λ, deg). The following are equivalent.


- (a) The space G is α-regular.
- (b) We have t(K2, G) = α and t(P3, G) = α2.
- (c) For all trees F, we have t(F, G) = αe(F).


Proof. Assuming (a), we get (c) from Proposition 4.32(c). The implication (c) ⇒ (b) is trivial. Assuming (b), we prove (a). The degree of a λ-random point x ∈ X has expectation t(K2, G) = α and variance t(P3, G)−t(K2, G)2 = α2 −α2 = 0, therefore it is a.s. α.

- 4.6. Hausdorﬀ limits of regular sequences of large essential girth.


- Lemma 4.35. If 0 ≤ α ≤ 1, and h ≥ 0 is a continuous non-decreasing function on a right neighborhood of 0, such that h(0) = 0 but h(x)/x → ∞ as x → 0, then


- (a) there exists an α-regular acyclic Hausdorﬀ graphoning G with gauge function h, such that W is {0, 1}-valued.
- (b) If, in addition, the gauge function h is concave, then G can be chosen to be Euclidean.


Proof. If α = 0, let X = [0, 1] with the Euclidean metric, and let W = 0 everywhere. This is a 0-regular acyclic Euclidean graphoning with gauge function h.

If α > 0, then we may, and do, assume that α = 1, since we may replace h by h/α. (a) For i = 1, 2, . . ., choose positive integers γi and δi such that δi is even and γi > δi

for all i, δi and γi/δi both tend to ∞ as i → ∞, and h(1/(γ1 · · ·γn)) ∼ 1/(δ1 · · ·δn) as n → ∞. Let V (Γi) = Z/γiZ, and join two nodes by an edge if their distance is ≤ δi/2 to get a δi-regular graph Γi. For all k ≥ 3, we have

limsup

t(Ck, Γi, δi) ≤ 3/4,

i→∞

so the 1-regular sequence (Gn, dn), where Gn = Γ1 × · · · × Γn and dn = δ1 · · ·δn, has large essential girth. The claim now follows from Example 4.26.

(b) For i = 1, 2, . . ., choose integers γi ≥ δi > 1 such that δi − 1|γi − 1 for all i, δi and γi/δi both tend to ∞ as i → ∞, and

|δ1 · · ·δnh(1/(γ1 · · ·γn)) − 1| < 1/2n for all n. Let

∞

an γ1 · · ·γn

S =

: 0 ≤ an < γn, an ≡ 0 mod (γn − 1)/(δn − 1) .

![image 136](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile136.png>)

n=1

I.e., S ⊂ [0, 1] is the set of numbers which, in the mixed radix system with base γ1, γ2, ..., have a representation such that the n-th digit is divisible by (γn −1)/(δn −1) for all n. In other words, S = ∞n=0 Sn, where

Ir,

Sn =

r∈Rn

Rn is the set of integer sequences (r1, . . ., rn) such that 0 ≤ ri ≤ δi − 1 for all i, I∅ = [0, 1], and Ir is a compact interval of length 1/(γ1 · · ·γn), such that the two intervals Ir

1,...,rn−1, and the midpoints of the δn intervals Ir

1,...,rn−1,0 and Ir

1,...,rn−1,δn−1 share a left, resp. right endpoint with Ir

1,...,rn−1,0, ..., Ir

1,...,rn−1,δn−1 form an arithmetic

progression. Since each Ir is compact, so is Sn, and therefore so is S. Let µ be the Hausdorﬀ measure with gauge function h. We shall now prove that

µ(S) = 1. This is closely related to [31, Theorem 1]. The basic idea is found already in [18, pp. 14–15].

We have S ⊂ Sn = Ir, where

h(diamIr) = δ1 · · ·δn · h(1/(γ1 · · ·γn)) → 1

r

and

diamIr = 1/(γ1 · · ·γn) → 0 as n → ∞, whence µ(S) ≤ 1.

max

r

For the converse inequality, assume that S ⊆ J∈J J, where J is countable and each diamJ is smaller than the length of a shortest component of [0, 1] − Sn for a given n. We show that

- 1

![image 137](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile137.png>)

- 2n−2.


h(diamJ) > 1 −

J∈J

We may assume (by taking convex hull and fattening a bit) that the sets J are open intervals with endpoints not in S. By compactness, we may assume that there are only ﬁnitely many of them. Now we may change our mind and assume (by cutting oﬀ superﬂuous bits) that each J is the convex hull of two intervals Ir, where r ∈ RN with a ﬁxed N, while each J is contained in some Ir with r ∈ Rn. We may also assume that the intervals J ∈ J are pairwise disjoint.

Let J ′ be the set of nonempty intervals arising by intersecting each J ∈ J with each connected component of Sn+1.

It suﬃces to show that

h(diamJ′) −

h(diamJ) ≤

J′∈J ′

J∈J

because the right hand side is

h(diamIr),

h(diam Ir′) −

r′∈Rn+1

r∈Rn

δ1 · · ·δnδn+1h(1/(γ1 · · ·γnγn+1)) − δ1 · · ·δnh(1/(γ1 · · ·γn)) < 3/2n+1. Let r ∈ Rn be ﬁxed. It suﬃces to show that

δn+1−1

h(diamJ′) −

h(diamJ) ≤

) − h(diamIr),

h(diamIr,r

n+1

J′∈J ′,J′⊂Ir

rn+1=0

J∈J ,J⊆Ir

because summation upon r gives our previous claim. The last inequality follows from the concavity of h. Indeed, if an in interval J ∈ J with J ⊆ Ir contains exactly s of the δn+1 − 1 connected components of Ir \ Sn+1, then

δn+1−1

s δn+1 − 1

h(diamJ′) − h(diamJ) ≤

) − h(diamIr) ,

h(diamIr,r

![image 138](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile138.png>)

n+1

J′∈J ′,J′⊆J

rn+1=0

and summation w.r.t. J yields our previous inequality. This proves that µ(S) = 1.

For x, y ∈ [0, 1], put W(x, y) = 1 if |x − y| ∈ S and W(x, y) = 0 otherwise. Let λ be Lebesgue measure on B = B[0, 1]. We must prove that the tuple

G = ([0, 1], B, λ, µ, W) is a 1-regular Euclidean graphoning with gauge function h. Firstly, the function W is semicontinuous and therefore Borel measurable. We have deg[0,1](x) = 1 for all x ∈ [0, 1]. When A is an interval, the function degA is continuous and therefore Borel measurable. When A is an open set, the function degA is still Borel measurable because A is a countable disjoint union of intervals, thus degA is Baire 1 (i.e., a pointwise limit of continuous functions). The class of Borel subsets A of [0, 1] such that degA is Borel measurable is closed under monotone sequential limits and contains all open sets, therefore contains all Borel sets, cf. [14, Section II.6].

It remains to check the measure preserving property (4.2). Observe that W is the indicator of a set that is a union of lines with slope 45◦ intersected with the unit square. Any union of such lines is symmetric w.r.t. any line of slope −45◦. We deduce (4.2) for intervals A, B ⊆ [0, 1] of equal length. Since any rectangle can be exhausted by squares, (4.2) holds for any intervals A and B by the Monotone Convergence Theorem. For a ﬁxed interval A, both sides of (4.2), as functions of the Borel set

- B, are ﬁnite measures that coincide on intervals, so coincide on all Borel sets. For a ﬁxed Borel set B, the two sides coincide on all intervals A, so on all Borel sets A. This proves that G is indeed a 1-regular Euclidean graphoning with gauge function


- h. We show that G is acyclic. Since S is symmetric w.r.t. 1/2, this amounts to


saying that for any k ≥ 2, the modulo 1 sum of k independent µ-random elements of S is a.s. not in S. But µ-random means that for each n, we choose a value from {0, 1, . . ., δn − 1} uniformly and multiply it by (γn − 1)/(δn − 1) to get the n-th digit in the mixed radix expansion; and we do this independently for all n. There will a.s. be inﬁnitely many indices n such that there is carrying from the n-th digit to the previous digit when we perform the k-fold addition, but there is no carrying from the (n + 1)-th digit to the n-th. If such an n is large enough, then in the k-fold modulo 1 sum the n-th digit an is not divisible by the corresponding (γn − 1)/(δn − 1).

- Theorem 4.36. If 0 ≤ α ≤ 1, and (Gn, dn) is an α-regular sequence of large essential girth, such that v(Gn) < v(Gn+1) and dn ≤ dn+1 for all n, then


- (a) (Gn, dn) has a Hausdorﬀ limit such that W is {0, 1}-valued.
- (b) If, in addition, the function 1/ v(Gn)  → 1/dn is concave, then (Gn, dn) has a Euclidean limit such that W is {0, 1}-valued.


Proof. Let h(1/ v(Gn)) = 1/dn, and let h be linear on each of the intervals [1/ v(Gn+1), 1/ v(Gn)] .

Put h(0) = lim(1/dn) to make h right-continuous. If h(0) > 0, then dn stabilizes to a value d. Then αd must be an integer, and Gn is Benjamini–Schramm convergent to

the αd-regular tree, which can be represented by a graphing on [0, 1]. From now on, we assume that dn → ∞, i.e., h(0) = 0.

If α = 0, let X = [0, 1] with the Euclidean metric, and let W = 0 everywhere. This is a Euclidean limit for (Gn, dn).

If α > 0, then, by Proposition 1.25, we have v(Gn)/dn → ∞ as n → ∞, and therefore h(x)/x → ∞ as x → 0. The Theorem now follows from Lemma 4.35.

The rest of this subsection is not logically necessary, it is only to illustrate Lemma

- 4.35 and Theorem 4.36. We work out two examples: we explicitly construct Euclidean limits of the sequence of hypercubes and the sequence of projective planes. Let µcube and µproj be the Hausdorﬀ measures on [0, 1] corresponding to the gauge functions


√

![image 139](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile139.png>)

hcube(x) = 1/ log2(1/x) and hproj =

2x, respectively. Note that these gauge functions have the right growth rate:

- (4.7) hcube(1/ v(Qd)) = 1/d and hproj(1/ v(G)) ∼ 1/(q + 1) if G is the incidence graph of a projective plane of order q → ∞. Observe also

that hcube is concave on [0, 1/e] and hproj is concave on [0, +∞). This will help us to calculate the Hausdorﬀ measures of carefully constructed sets. The following construction relies on a rather special property of these two functions h: the numbers 1/h−1(1/2) and h−1(1/2n)/h−1 (1/2n+1) (n = 1, 2, . . .) are integral powers of 2. Thus, we can get away with binary expansions instead of the mixed radix expansions above, and the inequalities involved in the proof of Lemma 4.35(b) become much simpler.

Let

- (4.8)

Scube =

∞

j=1

aj2−j : aj ∈ {0, 1}, a1 = a2, a3 = a4, a5 = · · · = a8, a9 = · · · = a16, . . . and

- (4.9) Sproj =

∞

j=1

aj2−j : aj ∈ {0, 1}, a1 = a2 = a3, a4 = a5, a6 = a7, a8 = a9, . . . .

- Proposition 4.37. (a) The sets Scube and Sproj are compact. (b) µcube(Scube) = µproj(Sproj) = 1.


For the ‘proj’ case, this is well known [18, page 15]; it is also a special case of [31, Theorem 1]. The ‘cube’ case can be proved by the same technique, or a proof can be extracted from that of Lemma 4.35(b). We include a proof for the convenience of the reader.

Proof. In both cases, we have S = ∞n=0 Sn, where Sn =

i∈{0,1}n

Ii,

and Ii is a compact interval with h(diamIi) = 1/2n for each i ∈ {0, 1}n, such that I∅ = [0, 1], and Ii,0 and Ii,1 share a left, resp. right endpoint with Ii.

(a) Since each Ii is compact, so is Sn, and therefore S. (b) We have S ⊂ Sn = Ii, where

- (4.10)


h(diamIi) = 2n · (1/2n) = 1

i∈{0,1}n

and maxi diamIi = h−1(1/2n) → 0 as n → ∞, whence µ(S) ≤ 1.

For the converse inequality, assume that S ⊆ J∈J J, where J is countable. We show that h(diamJ) ≥ 1. We may assume (by taking convex hull and fattening a bit) that the sets J are open intervals with endpoints not in S. By compactness, we may assume that there are only ﬁnitely many of them. Now we may change our mind and assume (by cutting oﬀ superﬂuous bits) that each J is the convex hull of two intervals Ii, where i ∈ {0, 1}n with a ﬁxed n.

In view of (4.10), it suﬃces to show that

- 1

![image 140](<2016-frenkel-convergence-graphs-intermediate-density_images/imageFile140.png>)

- 2n i∈{0,1}


- (4.11) h(diam J) ≥


h(diamIi) =

1

i∈{0,1}n,Ii⊆J

n,Ii⊆J

for any such J. We use induction on n. For n = 1, we have J = I0 or J = I1, when (4.11) holds with equality, or J = [0, 1], when it holds with strict inequality. Let n ≥ 2 and assume that (4.11) holds for n − 1 in place of n, whenever J is the convex hull of two intervals Ii, i ∈ {0, 1}n−1. Let us prove the same for n.

If the rightmost Ii contained in J has an index i ∈ {0, 1}n that ends on 0, then let

- i′ be the same i with the last digit modiﬁed to 1. Let J′ be the convex hull of J and
- Ii′. By concavity of h, we have h(diamJ′) − h(diamJ) ≤ 1/2n,


except, in the hypercube case, if diamJ′ > 1/e, but then we have diamJ > 1/2 and h(diamJ) > 1 trivially.

Thus, it suﬃces to prove (4.11) for J′ in place of J. We may perform a similar trick at the left end of J. After all, we may assume that that the leftmost interval Ii in J has i ending on 0 and the rightmost one has i ending on 1. But then J is the convex hull of two intervals Ii with i ∈ {0, 1}n−1 and we are done by the induction hypothesis.

We continue to treat the hypercube and the projective plane simultaneously. We omit the subscripts cube and proj. As in the proof of Lemma 4.35(b), we use S to construct a graphoning. For x, y ∈ [0, 1], put W(x, y) = 1 if |x − y| ∈ S and W(x, y) = 0 otherwise. Let λ be Lebesgue measure on B = B[0, 1]. The tuple G = ([0, 1], B, λ, µ, W) is an acyclic 1-regular Euclidean graphoning with gauge function h. Acyclicity means that for any k ≥ 2, the modulo 1 sum of k independent µ-random elements of S is a.s. not in S. Here µ-random means that for each block of binary digits in (4.8) or (4.9), we choose the common value 0 or 1 with equal probability, and we do this independently for all blocks. There will a.s. be a block where we choose 1 exactly twice for the common value, but for the following k blocks, we choose 0 all k2 times. In the k-fold modulo 1 sum this block will not consist of equal digits.

- Proposition 4.38. (a) (Qd, d) → Gcube as a Euclidean limit as d → ∞. (b) If Gn is the incidence graph of a projective plane of order qn, and qn → ∞,


then

(Gn, qn + 1) → Gproj as a Euclidean limit as n → ∞.

Proof. From Propositions 4.34 and 4.37, we have t(F, G) = 1 for any tree F. Since G is acyclic, we have t(F, G) = 0 if F contains a cycle. By Propositions 1.24 and 1.27, the convergence claims in the Proposition hold. By (4.7), the limiting graphonings are Hausdorﬀ, and therefore, Euclidean limits.

5. Sub-Markov spaces

In the previous subsection, we dealt with regular sequences of large essential girth. In this section, we shall construct limit objects for arbitrary sequences of large essential girth. Sadly, these limit objects will not be graphonings, they will be weaker structures: probability spaces with a reversible sub-Markov kernel — in other words, pseudo-graphonings with W = 0.

- 5.1. Tree densities and kernel preserving maps. In this subsection, we do the easy part of the preparations.


We only need to care about tree densities. Recall again that the rooted tree densities, as in Deﬁnition 4.9, depend only on the sub-Markov kernel deg, not on the function W — cf. Proposition 4.10(c) — or on the probability measure λ. They satisfy a simple recursion whose proof is trivial from Deﬁnition 4.9:

- Lemma 5.1. Let deg be a sub-Markov kernel on (X, B), and let x0 ∈ X. Let (F, o) be a rooted tree. We have


k

t((F, o), (X, x0)) =

t((Fi, oi), (X, xi))ddeg(x0)(xi)

i=1 X

if F − o is the disjoint union of trees F1, ..., Fk whose nodes adjacent to o in F are o1, ..., ok respectively.

- Deﬁnition 5.2. Let (X, A, deg) and (Y, B, deg) be spaces with sub-Markov kernels (by abuse of notation, both kernels are denoted by deg). A measurable map φ : X → Y is kernel preserving if φ∗(deg(x)) = deg(φ(x)) for all x ∈ X.


- Proposition 5.3. If φ : X → Y is kernel preserving, then t((F, o), (X, x0)) = t((F, o), (Y, φ(x0)))


for all rooted trees (F, o) and all x0 ∈ X.

Proof. We use induction on v(F). Assume that the Proposition is true for all rooted trees with less than v(F) nodes. Let F − o be the disjoint union of trees F1, ..., Fk whose nodes adjacent to o in F are o1, ..., ok respectively. We have

k

t((F, o), (Y, φ(x0))) =

i=1 Y

t((Fi, oi), (Y, yi))ddeg(φ(x0))(yi)

by Lemma 5.1. Here we may replace deg(φ(x0)) by φ∗(deg(x0)) because φ is kernel preserving. But

t((Fi, oi), (Y, yi))d(φ∗(deg(x0)))(yi) =

t((Fi, oi), (Y, φ(xi)))ddeg(x0)(xi)

Y

X

for all i by the deﬁnition of φ∗. By the induction hypothesis, we may replace t((Fi, oi), (Y, φ(xi))) by t((Fi, oi), (X, xi)). The Proposition follows by using Lemma 5.1 again.

The unrooted tree densities of a probability space with a reversible sub-Markov kernel are deﬁned by formula (4.5). By Proposition 4.20, they are well deﬁned. That proposition is about pseudo-graphonings, but we can always put W = 0 to get a pseudo-graphoning.

Simultaneously kernel preserving and measure preserving maps also preserve reversibility and unrooted tree densities:

- Proposition 5.4. If G = (X, A, κ, deg) and H = (Y, B, λ, deg) are probability spaces with sub-Markov kernels on each, φ : X → Y is measurable, kernel-preserving and measure-preserving, and the kernel on X is reversible, then


- (a) the kernel on Y is reversible, and
- (b) we have t(F, G) = t(F, H) for all trees F.


Proof. (a) For all A, B ∈ B, we have

degφ−1(B) dκ, which is symmetric w.r.t. A and B because the kernel on X is reversible. (b) We have t(F, G) =

degB dλ =

(degB ◦φ)dκ =

φ−1(A)

φ−1(A)

A

t((F, o), (G, x))dκ(x) =

t((F, o), (H, y))dλ(y) = t(F, H) for all rooted trees (F, o).

X

Y

5.2. The space of consistent measure sequences. We now wish to construct a compact metrizable space that, for sequences of large essential girth, will play a role analogous to that of the space of bounded-degree rooted graphs in the Benjamini– Schramm limit theory [26, Subsection 18.3].

Given a compact metric space K, let M(K) be the space of Borel measures on K whose total mass is ≤ 1 (i.e., sub-probability measures). This, endowed with the Lévy–Prokhorov metric, is again a compact metric space, where convergence is the weak convergence of measures. A continuous map f : K → L of compact metric spaces induces a continuous map f∗ : M(K) → M(L).

Let M0 be a point and let Mr = M(Mr−1). E.g., M1 ≃ [0, 1]. Let f0 : M1 → M0 be the unique map, and let fr = (fr−1)∗ : Mr+1 → Mr. A consistent sequence is a sequence

∞

σ = (σr)∞r=0 ∈

Mr

r=0

such that fr(σr+1) = σr for all r. Let M be the set of consistent sequences. This is the inverse limit of the spaces Mr with respect to the maps fr. It is closed in the above product space, and therefore compact. Let B be the σ-algebra of Borel sets in M.

There is a canonical sub-Markov kernel on (M, B). Let

A˜ = {σ ∈ M : σr ∈ A} whenever A ⊆ Mr is Borel. Let

A = {A˜ : A Borel in Mr, r = 0, 1, . . .}. This is an algebra of sets, and it generates B as a σ-algebra. Deﬁne degA˜(σ) = σr+1(A) whenever A ⊆ Mr is a Borel set and σ ∈ M. Then deg(σ) is a ﬁnite measure on A, therefore it extends to a unique measure on B by the Hahn–Kolmogorov Theorem [14, Section IV.4]. This deﬁnes deg : M × B → [0, 1]. The class of sets A ∈ B such that degA : M → [0, 1] is measurable contains A and is closed under monotone sequential limits, therefore equals B. Thus, deg is a sub-Markov kernel.

This sub-Markov kernel, when viewed as a map deg : M → M(M), is a homeomorphism. Indeed, its inverse is given by projecting a measure σ ∈ M(M) to each Mr to

get a consistent sequence of measures σr+1 ∈ M(Mr) = Mr+1 which we complete by the unique element σ0 of M0. This two-sided inverse map of deg is continuous and M(M) is compact, so deg is a homeomorphism.

A useful consequence of this is

- Lemma 5.5. If f : M → [0, 1] is continuous, then so is degf : M → [0, 1].

Proof. Let xn → x in M. Since deg is continuous, deg(xn) → deg(x) weakly. Since f is continuous,

degf(xn) =

M

fddeg(xn) →

M

fddeg(x) = degf(x).

We now have a sub-Markov kernel on M, so rooted tree homomorphism densities of M are deﬁned.

- Lemma 5.6. For a ﬁxed rooted tree (F, o) of radius ≤ r, the rooted homomorphism density


t((F, o), (M, σ)) = t((F, o), (Mr, σr)) depends only on σr, and this dependence is continuous. Proof. Induction on r, using Lemmas 5.1 and 5.5.

Let T • be the set of rooted trees such that the root has exactly one neighbor.

- Proposition 5.7. The map


•

t : M → [0, 1]T

σ  → (t((F, o), (M, σ)))(F,o)∈T• is a homeomorphism between M and its image t(M). Proof. Since M is compact and t is continuous, it suﬃces to prove that t is injective. Let

• ≤r

tr : Mr → [0, 1]T

σ  → (t((F, o), (M, σ)))(F,o)∈T•

,

≤r

where T≤•r is the set of rooted trees in T • with radius ≤ r. It suﬃces to prove that tr is injective for all r. For r = 0, this holds because M0 is a point. Assume that it holds for r. Let us prove it for r + 1. Suppose that tr+1(σr+1) = tr+1(σr′+1) for some σr+1, σr′+1 ∈ Mr+1 = M(Mr). We need to show that σr+1 = σr′+1. We have

• ≤r

(tr)∗σr+1 ∈ M [0, 1]T

,

and similarly for σr′+1. Since tr is injective, it suﬃces to prove that these two measures on the cube coincide, or, equivalently, their moments coincide. But a moment of

(tr)∗σr+1 is the same thing as a homomorphism density t((F, o), (Mr+1, σr+1)), where (F, o) ∈ T≤•r+1. Indeed, if we think of F − o as a family of elements of T≤•r that are glued together at their roots (the roots become the node adjacent to o in F), and each rooted tree (T, p) ∈ T≤•r occurs m(T, p) times in this family, then

t((T, p), (Mr, σr))m(T,p)dσr+1(σr).

t((F, o), (Mr+1, σr+1)) =

Mr (T,p)∈T≤•r

We now show that M is the terminal object in the category of sub-Markov spaces.

- Proposition 5.8. Any space with a sub-Markov kernel admits a unique kernel preserving map to M.

Proof. Uniqueness is immediate from Propositions 5.3 and 5.7.

To prove existence, let (X, B, deg) be a space with a sub-Markov kernel. We construct a kernel preserving map σ : X → M. Let σ0 : X → M0 be the unique map. If σr : X → Mr is already deﬁned, then put

σr+1(x) = (σr)∗(deg(x)) ∈ M(Mr) = Mr+1

for all x ∈ X. Let σ(x) = (σr(x))∞r=0. This is a consistent sequence, i.e., fr(σr+1(x)) = σr(x) for all r. We show this by induction on r. It is true for r = 0 because both sides are elements of the singleton M0. Let us assume it is true for r − 1. Then it is true for r because

fr(σr+1(x)) = (fr−1 ◦ σr)∗(deg(x)) = (σr−1)∗(deg(x)) = σr(x).

Thus, we have σ : X → M. We must prove that the map σ is kernel preserving, i.e., σ∗(deg(x)) = deg(σ(x)) for all x. It suﬃces to show that these two measures on

- M coincide when pushed down to Mr, for all r. Using the deﬁnition of deg(x) on the right hand side, this amounts to (σr)∗(deg(x)) = σr+1(x). This is true by the very deﬁnition of σr+1(x).


Let us now examine probability measures on (M, B) that make the canonical kernel deg reversible, i.e., involution-invariant measures. These are analogous to a basic concept in the Benjamini–Schramm graph limit theory: involution-invariant probability distributions on the space of rooted graphs with a degree bound.

- Proposition 5.9. The set of involution-invariant probability measures λ on (M, B) is closed under aﬃne combinations that are nonnegative measures, and is closed in the weak topology.


Proof. The measure preserving condition is linear in λ, hence remains true for aﬃne combinations.

To prove closedness under weak limits, let λn satisfy the measure preserving equation for n = 1, 2, . . ., and let λn → λ weakly. We prove the equality (4.4) for λ. Using Lemma 5.5, we get the equality for continuous f and g. For a ﬁxed continuous g, the class of measurable f : M → [0, 1] for which the equality holds is closed under monotone pointwise limits by the Monotone Convergence Theorem, thus this class contains all measurable f. The same argument for ﬁxed measurable f and varying g ﬁnishes the proof.

We are ready for the main result of this section.

- Theorem 5.10. Let (Gn, dn) be an admissible sequence such that t(F, Gn, dn) converges for all trees F. Then there is a unique involution-invariant Borel probabil-


ity measure λ on M such that t(F, Gn, dn) → t(F, (M, B, λ, deg)) for all trees F as n → ∞.

Proof. To prove uniqueness, observe that if λ and λ′ both have the desired property, then t(F, G) = t(F, G′) for all trees F, whence the measures

•

t∗λ, t∗λ′ ∈ M [0, 1]T

have the same moments, so they coincide. Thus, λ = λ′.

To prove existence, consider the graphoning Gn = (V (Gn), P(V (Gn)), λn, µn, Wn) corresponding to (Gn, dn) by Remark 4.21. Push λn forward to M using the unique degree preserving map Gn → M. Then push it further to [0, 1]T • using t. The resulting sequence of probability measures converges weakly because all moments converge. The weak limit is a probability measure λ concentrated on t(M) which, when pulled back to M using t−1 : t(M) → M, has the desired properties.

There is a corresponding version of the Aldous–Lyons Conjecture:

Problem 5.11. Is it true that for every involution-invariant Borel probability measure λ on M there exists a convergent sequence (Gn, dn) of large essential girth such that t(F, Gn, dn) → t(F, (M, B, λ, deg)) for all trees F as n → ∞ ?

In the Benjamini–Schramm case, the aﬃrmative answer was proved by G. Elek [17]. If (Gn, dn) is a convergent sequence of large essential girth, then the tree densities

carry all the information, so the pseudo-graphoning G = (M, B, λ, W = 0, deg),

where λ is given by Theorem 5.10, is a limit for the sequence. This may be unsatisfactory: we might want large essential girth to be reﬂected in the acyclicity of the kernel deg rather than only in the fact that W = 0 (because an acyclic deg would give us some hope of ﬁnding a diﬀerent W that would turn G into a true graphoning with unchanged homomorphism densities). This is easy to achieve, as we explain below. The price to pay is that the new probability measure and reversible sub-Markov kernel will not be on the space M, and we lose uniqueness.

If (X, A) and (Y, B) are two measurable spaces with a sub-Markov kernel on each one, then we get a sub-Markov kernel on (X × Y, A ⊗ B) by deﬁning the measure deg(x, y) to be the product of the measures deg(x) and deg(y). Then degk(x, y) is the product of the measures degk(x) and degk(y) for all k. Thus, if degk(x) ⊥ deg(x), then degk(x, y) ⊥ deg(x, y).

A product of reversible kernels given on two probability spaces is clearly reversible on the product space. The homomorphism density of any tree in the product will be the product of the densities in the factors.

Thus, we can multiply any probability space endowed with a reversible sub-Markov kernel by either one of the many acyclic 1-regular graphonings constructed in Subsection 4.6 to get an acyclic space with unchanged tree densities. This proves

Theorem 5.12. Let (Gn, dn) be an admissible sequence such that t(F, Gn, dn) converges for all trees F. Then there exists a probability space G endowed with an acyclic reversible sub-Markov kernel such that t(F, Gn, dn) → t(F, G) for all trees F.

6. Regularity lemma? To conclude, we brieﬂy speculate on one of the questions involved in Problem 4.27(a):

does every convergent sequence (Gn, dn) tend to a pseudo-graphoning G ? If (Gn, dn) has large essential girth, the answer is in the aﬃrmative by Theorem 5.10: choose W = 0. In general, the proof of an aﬃrmative answer might involve an appropriate version of Szemerédi’s Regularity Lemma. The very weak version below is unlikely to suﬃce.

- Proposition 6.1. For any family G of admissible pairs (G, d), and for any ǫ > 0, there exists an N such that for every (G, d) ∈ G there exists (G′, d′) ∈ G with v(G′) ≤


- N, d′ ≤ N, and |t(F, G, d) − t(F, G′, d′)| < ǫ


for all F with v(F) ≤ 1/ǫ.

In the Benjamini–Schramm setting, i.e., when G is the family of pairs (G, d) such that d is a ﬁxed degree bound, this is equivalent to [26, Proposition 19.10], which answered a question of L. Lovász. The very simple proof by Noga Alon carries over easily to Proposition 6.1.

Acknowledgements

Many thanks to Miklós Abért for believing in this project, and for stimulating discussions. I am grateful to Péter Csikvári, Viktor Kiss, Balázs Szegedy, and Gábor Tardos for useful comments.

References

- [1] M. Abért, P. Csikvári, P.E. Frenkel, G. Kun, Matchings in Benjamini-Schramm convergent graph sequences, Trans. AMS 368 (2016), no. 6, 4197–4218.
- [2] M. Abért and T. Hubai, Benjamini-Schramm convergence and the distribution of chromatic roots for sparse graphs, Combinatorica 35 (2015), no. 2, 127–151.
- [3] J.M. Aldaz and J. Pérez Lázaro, Functions of bounded variation, the derivative of the one dimensional maximal function, and applications to inequalities, Trans. Amer. Math. Soc. 359

(2007), no. 5, 2443–2461 (electronic).

- [4] D. Aldous and R. Lyons: Processes on unimodular random networks, Electr. J. of Probability 12, Paper 54 (2007), 1454–1508.
- [5] B. Bollobás and B. D. McKay: The number of matchings in random regular graphs and bipartite graphs, J. Combinatorial Theory, Series B 41 (1986), 80-91
- [6] B. Bollobás and O. Riordan: Metrics for sparse graphs, in: S. Huczynska, J.D. Mitchell, and C.M. Roney-Dougal, eds., Surveys in combinatorics 2009, pages 211–287, London Math. Soc. Lecture Note Ser. 365, Cambridge University Press, Cambridge, 2009. arXiv:0708.1919, MR2588543
- [7] C. Borgs, J.T. Chayes, H. Cohn, and Y. Zhao: An Lp theory of sparse graph convergence I: limits, sparse random graph models, and power law distributions, preprint, 2014. arXiv:1401.2906
- [8] C. Borgs, J.T. Chayes, H. Cohn, Y. Zhao: An Lp theory of sparse graph convergence II: LD convergence, quotients and right convergence preprint, 2014. arXiv: 1408.0744
- [9] C. Borgs, J.T. Chayes, L. Lovász, V.T. Sós, K. Vesztergombi: Convergent sequences of dense graphs II. Multiway cuts and statistical physics, Ann. Math. 176 (2012), 151–219.
- [10] L.H. Clark, J.C. George, and T.D. Porter: On the number of 1-factors in the n-cube, Congr. Numer. 127 (1997), 67–69.
- [11] P. Csikvári and P.E. Frenkel: Benjamini–Schramm continuity of root moments of graph polynomials, European J. Combin. 52 (2016), part B, 302–320.
- [12] P. Csikvári, P.E. Frenkel, J. Hladký, T. Hubai: Chromatic roots and limits of dense graphs, Discrete Math. 340 (2017), no. 5, 1129–1135. arXiv:1511.09429 [math.CO]
- [13] Ewan Davies, Matthew Jenssen, Will Perkins, Barnaby Roberts: Independent Sets, Matchings, and Occupancy Fractions, Journal of the London Mathematical Society 96 (2017), no. 1, 47–66. arXiv: 1508.04675
- [14] J.L. Doob: Measure theory, Graduate Texts in Mathematics, Springer, New York, 1994.
- [15] I. Dumitriu, S. Pal: Sparse regular random graphs: spectral density and eigenvectors, Ann. Probab. 40 (2012) no. 5, 2197–2235.
- [16] G. Elek: On limits of ﬁnite graphs, Combinatorica 27 (2007) 503–507.
- [17] G. Elek: On the limit of large girth graph sequences, Combinatorica 30 (5) (2010) 553–563.
- [18] K.J. Falconer: The geometry of fractal sets, Cambridge University Press, 1985.
- [19] G. Freud: Orthogonale Polynome, Akadémiai Kiadó, Budapest, 1969.
- [20] W. Gawronski, On the Asymptotic Distribution of the Zeros of Hermite, Laguerre, and Jonquière Polynomials, Journal of Approximation Theory 50 (1987), 214–231.


- [21] C. D. Godsil: Algebraic Combinatorics, Chapman and Hall, New York 1993
- [22] I.S. Gradshteyn and I.M. Ryzhik, Table of integrals, series and products, Corrected and enlarged edition, Academic Press, 1980.
- [23] O. J. Heilmann and E. H. Lieb: Theory of monomer-dimer systems, Commun. Math. Physics 25 (1972), pp. 190-232
- [24] M. Kornyik and Gy. Michaletzky, Wigner matrices, the moments of roots of Hermite polynomials and the semicircle law, J. Approx. Theory 211 (2016), 29–41, DOI 10.1016/j.jat.2016.07.006. MR3547630. arXiv: 1512.03724v2
- [25] L. Lovász: Combinatorial Problems and Exercises, 2nd edition, Akadémiai Kiadó, Budapest, 1993
- [26] L. Lovász: Large Networks and Graph Limits, AMS Colloquium Publications 60, American Mathematical Society, Providence, RI, 2012.
- [27] L. Lovász and M.D. Plummer: Matching theory, Elsevier, Amsterdam and New York, 1986.
- [28] L. Lovász and B. Szegedy: Limits of dense graph sequences, J. of Comb. Theory B 96 (2006), 933–957.
- [29] Brendan D. McKay: The expected eigenvalue distribution of a large regular graph, Linear Algebra and its Applications 40 (1981), pp. 203-216
- [30] J. Propp: Enumeration of Matchings, Problems and Progress, New Perspectives in Geometric Combinatorics, MSRI Publications, Volume 38, 1999
- [31] Cheng Qin Qu, Hui Rao, and Wei Yi Su: Hausdorﬀ measure of homogeneous Cantor set, Acta Math. Sin., English Series 17 (2001), no. 1, 15–20.
- [32] P. Orbanz, B. Szegedy, Borel lifting of graph limits, Electron. Commun. Probab. 21 (2016), Paper No. 65, 4, DOI 10.1214/16-ECP14. MR3548777. arXiv:1312.7351v1
- [33] G. Szegő: Orthogonal polynomials, American Mathematical Society, Colloquium Publications, Volume XXIII, 1939.
- [34] L.V. Tran, V.H. Vu and K. Wang: Sparse random graphs: eigenvalues and eigenvectors, Random Structures & Algorithms 42 (2013), no. 1, 110–134.


Alfréd Rényi Institute of Mathematics, Hungarian Academy of Sciences, 1053 Budapest, Hungary, Reáltanoda u. 13-15. & ELTE Eötvös Loránd University, Faculty of Science, Institute of Mathematics, 1117 Budapest, Hungary, Pázmány Péter sétány 1/C

E-mail address: frenkelp@cs.elte.hu

