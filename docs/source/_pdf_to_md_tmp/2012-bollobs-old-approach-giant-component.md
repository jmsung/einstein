arXiv:1209.3691v2[math.PR]15Feb2015

An old approach to the giant component problem

B´ela Bolloba´s∗† Oliver Riordan‡ October 4, 2012; revised February 15, 2015

Abstract

In 1998, Molloy and Reed showed that, under suitable conditions, if a sequence dn of degree sequences converges to a probability distribution D, then the proportion of vertices in the largest component of the random graph associated to dn is asymptotically ρ(D), where ρ(D) is a constant deﬁned by the solution to certain equations that can be interpreted as the survival probability of a branching process associated to D. There have been a number of papers strengthening this result in various ways; here we prove a strong form of the result (with exponential bounds on the probability of large deviations) under minimal conditions.

# 1 Introduction and results

By a degree sequence d we mean a ﬁnite sequence (d1,...,dn) of non-negative integers with even sum. The length |d| of d = (di)ni=1 is the number n of terms, and the size m(d) = 21 i di is half the sum of the terms. We write Gd for the random (simple) graph with degree sequence d, i.e., a graph with vertex set [n] = {1,2,...,n} in which each vertex i has degree di, chosen uniformly at random from the set of all such graphs (assuming this set is non-empty). As usual, in studying Gd we also consider the corresponding random conﬁguration multigraph G∗d, introduced in [2], obtained by associating a set of di stubs to each vertex i, selecting a uniformly random pairing of the (disjoint) union of these sets, and interpreting each paired pair of stubs as leading to an edge in the natural way. Note that these graphs have |d| vertices and m(d) edges.

![image 1](<2012-bollobs-old-approach-giant-component_images/imageFile1.png>)

Let D denote the set of probability distributions D on the non-negative integers with 0 < E(D) < ∞. We usually write D ∈ D as D = (r0,r1,...), where, abusing notation by also writing D for a random variable with distribution D, ri = P(D = i). One of the basic questions concerning the random graph models

![image 2](<2012-bollobs-old-approach-giant-component_images/imageFile2.png>)

∗Department of Pure Mathematics and Mathematical Statistics, Wilberforce Road, Cambridge CB3 0WB, UK; and Department of Mathematical Sciences, University of Memphis, Memphis TN 38152, USA; and London Institute for Mathematical Sciences, 35a South St., Mayfair, London W1K 2XF, UK. E-mail: b.bollobas@dpmms.cam.ac.uk.

†Research supported in part by NSF grant DMS 1301614 and MULTIPLEX no. 317532. ‡Mathematical Institute, University of Oxford, 24–29 St Giles’, Oxford OX1 3LB, UK.

E-mail: riordan@maths.ox.ac.uk.

just described is the following: under what conditions does convergence of dn to D imply that the asymptotic behaviour of Gd

(or G∗d

) is captured by D? Here the behaviour we are interested in is the distribution of the component sizes, and most particularly the number L1 of vertices in the (a if there is a tie) largest component.

n

n

Let

ni(d) = {j : dj = i} denote the number of times a particular degree i occurs in d, so

m(d) =

|d|

- 1

![image 3](<2012-bollobs-old-approach-giant-component_images/imageFile3.png>)

- 2


- 1

![image 4](<2012-bollobs-old-approach-giant-component_images/imageFile4.png>)

- 2


dj =

j=1

∞

ini(d).

i=0

The basic assumptions made in all existing results of this type are that

ni(dn) |dn|

= ri (1)

lim

![image 5](<2012-bollobs-old-approach-giant-component_images/imageFile5.png>)

n→∞

for each i, that

m(dn) |dn|

E(D) 2

→

![image 6](<2012-bollobs-old-approach-giant-component_images/imageFile6.png>)

![image 7](<2012-bollobs-old-approach-giant-component_images/imageFile7.png>)

∞

- 1

![image 8](<2012-bollobs-old-approach-giant-component_images/imageFile8.png>)

- 2


iri (2)

=

i=0

as n → ∞, and of course that |dn| → ∞. (Often, one takes |dn| = n, which loses no generality.) We shall say that dn converges to D, and write dn → D, if these conditions hold.

Condition (1) ensures that D captures the asymptotic proportion of vertices of each ﬁxed degree, and condition (2) that the (rescaled) number of edges is related to D in the natural way. Note that if we write Dn for the distribution

- of a randomly chosen element of dn (i.e., the degree of a random vertex of


), then (1) asserts that Dn converges to D in distribution. Condition (2) asserts that E(Dn) → E(D) < ∞, which (given (1)) is equivalent to uniform integrability of the Dn.

Gd

n

To see why (2) is necessary, consider dn consisting of one vertex of degree n−1 and n−1 of degree 1, contrasted (for n even) with d′n in which all n degrees are equal to 1. In both cases (1) holds with r1 = 1 and all other ri = 0, but the component structures of Gd

and Gd′

are very diﬀerent – one is a star, and the other a matching. (There is a similar but less extreme diﬀerence between G∗d

n

n

n

and G∗d′

.)

n

As usual, we write Li(G) for the number of vertices in the ith largest component of a graph G. We also write Nk(G) for the number of vertices in k-vertex components. The next result involves constants ρk(D) and ρ(D) whose deﬁnitions we postpone to Section 2 (see (12)). In fact, ρ(D) is the same as the quantity εD appearing in [12], although our deﬁnition of it is diﬀerent. We write →p to denote convergence in probability.

- Theorem 1. Let D be a probability distribution on the non-negative integers with 0 < E(D) < ∞, and let dn be a sequence of degree sequences converging to D in the sense that (1) and (2) hold and |dn| → ∞. Then


)/|dn| →p ρk(D) for each ﬁxed k. If P(D 3) > 0, then we also have L1(Gd

Nk(Gd

n

)/|dn| →p ρ(D) and L2(Gd

n

)/|dn| →p 0. Furthermore, the same conclusions hold with Gd

n

n

replaced by G∗d

.

n

The ﬁrst result of this type was proved by Molloy and Reed [12], building on their work in [11]. This result required additional conditions: taking |dn| = n, they assumed in particular that the maximum degree in dn is o(n1/4−ε) for some ε > 0. Note that (2) implies only that the maximum degree is o(n): adding a single vertex with degree (approximately) n/ log log n, say, does not aﬀect convergence in our sense.

The results of [12] have been strengthened in a number of ways. One main direction is to improve, or even study the distribution of, the error term in the result L1 = ρ(D)n + op(n), sometimes imposing extra assumptions; see Kang and Seierstad [10], Pittel [13], Janson and Luczak [9], Riordan [15] and Hatami and Molloy [7], for example. In the other direction, one can ask for the same conclusion but with less restrictive assumptions; here Janson and Luczak [9] prove a version of Theorem 1 with the condition that the sum of the squares of the degrees is at most a constant times the number of vertices. They also prove the (easier) multigraph part of Theorem 1 under exactly our conditions (see their Remark 2.6), but using a very diﬀerent method.

We shall in fact prove a much stronger form of Theorem 1, Theorem 2 below; the reason for postponing the statement is that it is a little more awkward: instead of convergence, we need to work with neighbourhoods. Given D ∈ D and a degree sequence d, writing ri = P(D = i) as usual, set

∞

d0conf(d,D) =

i=1

ni(d) |d|

i

− iri , (3)

![image 9](<2012-bollobs-old-approach-giant-component_images/imageFile9.png>)

so d0conf is a form of the ℓ1 metric, and deﬁne the conﬁguration distance between d and D to be

dconf(d,D) = max{d0conf(d,D),1/|d|}. (4)

The 1/|d| term in (4) ensures that dconf(d,D) → 0 if and only if d0conf(d,D) → 0 and |d| → ∞, and avoids having to write ‘and |d| n0’ in many results below; this is a convenience rather than an essential part of the deﬁnition.

It is easy to check that, for D ∈ D, dn → D ⇐⇒ dconf(dn,D) → 0. (5)

Indeed, if dconf(dn,D) → 0, then certainly |dn| → ∞. Also, d0conf(dn,D) → 0, which trivially implies (1), and implies (2) by the triangle inequality. Conversely,

suppose that dn → D, and let ε > 0. Since i iri = E(D) < ∞, there is some C = C(ε) such that i<C iri E(D) − ε, and so

For n large enough, (1) gives

iri ε. (6)

i C

|ini(dn)/|dn| − iri| < ε/C (7) for all i < C. Hence

ini(dn)/|dn|

i<C

iri − ε E(D) − 2ε.

i<C

Using (2) it follows that i C ini(dn)/|dn| 3ε if n is large. This, (6) and (7) imply that d0conf(dn,D) 5ε. Since dn → D implies |dn| → ∞ by deﬁnition, and ε was arbitrary, it follows that dconf(dn,D) → 0.

Let us state for future reference a consequence of the argument just given: if dn → D then

∀ε > 0 ∃C ∀n

ini(dn) ε|dn|. (8)

i C

Writing dn = (d(1n),...,d(ℓn)

), (8) can be written as ∀ε > 0 ∃C ∀n

n

dj(n) ε|dn|.

j : dj(n) C

Informally, this condition says that a random edge has only a small probability of being attached to a vertex of very high degree. A rather trivial consequence of (8) is that, writing ∆(d) for the maximum degree appearing in a degree sequence d, if dn → D then ∆(dn) = o(|dn|). In terms of the metric, the equivalent of (8) is the observation that

∀D ∈ D,ε > 0 ∃C,δ : dconf(d,D) < δ =⇒

ini(d) ε|d|. (9)

i C

To see this, simply choose C such that i C iP(D = i) < ε/2, and take δ = ε/2.

- Theorem 2. Let D ∈ D, and let ε > 0. For each k 1 there exists δ > 0 (depending on D,ε and k) such that if dconf(d,D) < δ, then


P |Nk(Gd) − ρk(D)n| εn e−δn, (10)

where n = |d|. Moreover, if P(D 3) > 0, then there exists δ > 0 (depending on D and ε) such that if dconf(d,D) < δ then

P L1(Gd) − ρ(D)n εn e−δn

and

P L2(Gd) εn e−δn. Furthermore, the same conclusions hold if Gd is replaced by G∗d.

Using (5), it is easy to check that Theorem 2 does indeed strengthen Theorem 1. The main reason for proving the stronger bounds in Theorem 2 is that we need them for the conﬁguration multigraph model G∗d in order to prove even Theorem 1 for the simple random graph Gd. Of course, they are also nice to have!

Remark 3. The condition P(D 3) > 0 in Theorems 1 and 2 is necessary for the conclusions; see Janson and Luczak [9, Remark 2.7] for a discussion of the range of possible behaviours when P(D = 2) = 1 (or D is supported on {0,2}).

The basic idea of the proof of Theorem 1 is to use a (relatively) old method.

The ﬁrst ingredient is to understand the local structure of G∗d; this is very simple and can be expressed in a number of ways, most cleanly by comparison

with a branching process. This allows us to control the number of vertices in small components. Then we use a version of the original sprinkling argument of Erdo˝s and R´enyi [4] to show that almost all vertices in ‘large’ components are in a single giant component. Of course, sprinkling is more complicated in the present model than in the original context. Also, to obtain exponential error bounds we need a strong form of the branching process approximation, which introduces some additional complications. We shall show in Section 6 that this approximation carries over to the giant component: the number of vertices in the giant component with some ‘local’ property can be calculated in terms of the branching process.

Turning to the nitty-gritty, in the rest of the paper we use the following standard asymptotic notation: given a sequence En of events, we say that En holds with high probability or whp if P(En) → 1 as n → ∞. Given functions f and g of some parameter (usually n), f = O(g) means f is bounded by a constant times g, and f = o(g) means that f/g → 0 as the parameter (n) tends to inﬁnity.

Finally, before turning to the proofs, let us ﬁx our formal notation for the conﬁguration model: given a degree sequence d of length ℓ, we take disjoint sets F1,...,Fℓ with |Fi| = di, where Fi represents the ‘stubs’ associated to vertex i. Then we take a pairing (partition into 2-elements sets) π of F = ℓi=1 Fi chosen uniformly at random, and set G∗d = φd(π), where φd maps a pairing π to a multi-graph on [ℓ] = {1,2,...,ℓ} by replacing each pair {a,b} by an edge joining vertices i and j where a ∈ Fi and b ∈ Fj, noting that i = j is possible, in which case the edge is a loop.

# 2 Local approximation by a branching process

Let D = (r0,r1,...) ∈ D, so D is a probability distribution on the non-negative integers with 0 < E(D) < ∞, and ri = P(D = i). For i 1 let

iri i iri

qi =

=

![image 10](<2012-bollobs-old-approach-giant-component_images/imageFile10.png>)

iri E(D)

.

![image 11](<2012-bollobs-old-approach-giant-component_images/imageFile11.png>)

The distribution D∗ with P(D∗ = i) = qi is known as the size-biased distribution associated to D. In any graph G, if we pick a random edge and then choose one of its endvertices v at random, the distribution of the degree of v is the size-biased version of the degree distribution of G. Let ZD = D∗ − 1, so

(i + 1)ri+1 E(D)

P(ZD = i) = P(D∗ = i + 1) =

=

![image 12](<2012-bollobs-old-approach-giant-component_images/imageFile12.png>)

(i + 1)P(D = i + 1) E(D)

. (11)

![image 13](<2012-bollobs-old-approach-giant-component_images/imageFile13.png>)

Intuitively, ZD will correspond to the number of ‘new’ edges we get to when we follow a random edge to an endvertex.

Let T 1 = TD1 be the Galton–Watson branching process with oﬀspring distribution ZD, so T 1 is a random rooted tree in which the number of children of each vertex has distribution ZD, with these numbers independent. Finally, let T = TD be the random rooted tree in which the degree of the root has the distribution D, and, given the degree of the root, the branches, i.e., the subtrees rooted at the children of the root, form independent copies of T 1.

It is not hard to see that if dn → D, then G∗d

‘locally looks like’ TD; we shall make this precise in a moment. Let |TD| ∞ denote the total number of vertices of TD. Then the constants ρk and ρ appearing in Theorems 1 and 2 are

n

ρk(D) = P(|TD| = k) and ρ(D) = P(|TD| = ∞). (12)

Given a graph G, for v ∈ V (G) and t 0, let Γ t(v) = ΓG t(v) denote the subgraph of G induced by the vertices within (graph) distance t of v, regarded as a rooted graph with root v. Also, let TD|t be the subtree of TD induced by the vertices within distance t of the root. The following lemma is a variant of an idea that is by now very much standard, though perhaps not in exactly this form.

Lemma 4. Let D ∈ D and suppose that dn → D. Let v be a vertex of G = G∗d

n

chosen uniformly at random. Then we may couple the random graphs ΓG t(v) and TD|t so that they are isomorphic as rooted graphs with probability 1 − o(1) as n → ∞.

Proof. As the argument is straightforward and standard we give only an outline. The idea is to reveal Γ t(v) step-by-step in the natural way, coupling this process with revealing TD|t step-by-step so that for any ﬁxed j, the probability of the coupling failing at step j is o(1). Since, given any ε, there is some constant J such that with probability at least 1 − ε the ﬁnite tree TD|t has size at most J, this suﬃces to prove the lemma.

To reveal Γ t(v), ﬁrst pick the random vertex v, noting that by condition (1) of the convergence dn → D, the degree of v can be coupled to agree with the degree of the root of TD with probability 1 − o(1). Then go through the stubs associated to v one-by-one, revealing their partners, and thus the neighbours of v (as well as any loops at v). Then reveal the partners of the unpaired stubs associated to the neighbours of v, and so on. The key fact is that the jth time we reveal the partner of an unpaired stub, the probability that this is a ‘new’ (not so far reached in the exploration) vertex of degree i is exactly

i(ni(dn) − ui,j) 2m(dn) + 1 − 2j

,

![image 14](<2012-bollobs-old-approach-giant-component_images/imageFile14.png>)

where ui,j is the number of degree-i vertices revealed so far. For any ﬁxed j, since ui,j j = O(1), this probability is qi + o(1). Since qi is the probability that a vertex of TD other than the root has degree i (and hence i − 1 children), it follows that the coupling succeeds at step j with probability 1 − o(1), as required.

![image 15](<2012-bollobs-old-approach-giant-component_images/imageFile15.png>)

![image 16](<2012-bollobs-old-approach-giant-component_images/imageFile16.png>)

![image 17](<2012-bollobs-old-approach-giant-component_images/imageFile17.png>)

![image 18](<2012-bollobs-old-approach-giant-component_images/imageFile18.png>)

- Corollary 5. Let D ∈ D, suppose that dn → D, and let t 1 be constant.

Let v be a vertex of G = G∗d

n

chosen uniformly at random. Then whp the neighbourhood Γ t(v) of v in G is a tree.

Note that in many related situations, the equivalent of Corollary 5 is proved by considering the expected number of paths of length k ending in a vertex on a cycle of length ℓ, showing that this expectation is o(n) for k and ℓ ﬁxed. However, this requires some condition such as i d2i = n1+o(1), which need not hold here – it may be that G∗d contains many (more than n) short cycles, but these are all concentrated in the neighbourhoods of the few vertices with largest degrees, so most vertices are far from them.

Let P be a property of (locally ﬁnite) rooted graphs, i.e., a set of rooted graphs closed under isomorphism. Often we think of P as a property of vertices v of unrooted graphs G, by taking v as the root; in either case we write (G,v) ∈ P to mean that the graph G rooted at v has property P. We write NP(G) for the number of vertices of G with property P. Given t 1, we say that P is t-local if whether (G,v) has P depends only on the rooted graph ΓG t(v). We call P local if it is t-local for some t. Note that it makes sense to speak of our branching process TD having property P, since TD is a rooted tree. If P is t-local, then whether TD has P depends only on TD|t.

Lemma 4 immediately implies the following result, of which Corollary 5 is a special case.

- Corollary 6. Let P be a local property of rooted graphs, let D ∈ D, suppose


that dn → D, and let v be a vertex of G∗d

chosen uniformly at random. Then

n

P (G∗d

,v) ∈ P → P(TD ∈ P) as n → ∞. Equivalently, E(NP(G∗d

n

)) = P(TD ∈ P)|dn| + o(|dn|).

n

When we come to concentration, it will be convenient to work with a restatement of this last corollary.

- Corollary 7. Let P be a local property of rooted graphs, and let D ∈ D and ε > 0 be given. Then there exists δ > 0 such that if dconf(d,D) < δ then


E(NP(G∗d)) − P(TD ∈ P)n εn, (13) where n = |d|.

Proof. Suppose not. Then for each n there is a degree sequence dn with dconf(dn,D) 1/n for which (13) fails. Recalling (5), applying Corollary 6 to (dn)∞n=1 gives a contradiction.

![image 19](<2012-bollobs-old-approach-giant-component_images/imageFile19.png>)

![image 20](<2012-bollobs-old-approach-giant-component_images/imageFile20.png>)

![image 21](<2012-bollobs-old-approach-giant-component_images/imageFile21.png>)

![image 22](<2012-bollobs-old-approach-giant-component_images/imageFile22.png>)

The key property to which we shall apply this result is the property Pk that the component of the root contains exactly k vertices. Note that in this case

NP

(G) = Nk(G) and P(TD ∈ Pk) = ρk(D). (14)

k

We can easily use the second moment method (exploring from two random vertices v and w) to prove that NP(G∗d) is concentrated in the sense that NP(G∗d

)/n converges in probability when dn → D with |dn| = n. Instead we use the Hoeﬀding–Azuma inequality to prove a stronger result.

n

Two conﬁgurations (pairings) π1 and π2 are related by a switching if π2 can be obtained from π1 by deleting two pairs {a,b} and {c,d} and inserting the pairs {a,c} and {b,d}. A function f deﬁned on pairings of some ﬁxed set is CLipschitz if |f(π1) −f(π2)| C whenever π1 and π2 are related by a switching. We shall use the following standard simple lemma.

- Lemma 8. Let S be a set with size 2m, and let f be a C-Lipschitz function of pairings of S. If π is chosen uniformly at random from all pairings of S, then for any t 0 we have


P f(π) − E(f(π)) t 2 exp(−t2/(4C2m)).

Proof. Let S = {s1,...,s2m}. Let us condition on the partners of s1,...,si, writing Ω′ for the set of all pairings consistent with the information revealed so far. Now consider si+1. It may be that its partner is determined, since it is paired to one of s1,...,si. If not, for any possible partner b let Ω′b be the subset of Ω′ containing all pairings in which si+1 is paired with b. For distinct possible partners b and c, there is a bijection between Ω′b and Ω′c in which each π1 ∈ Ω′b is related to its image π2 by a switching: we simply switch the pairs {si+1,b} and {c,d} for {si+1,c} and {b,d}, where d is the partner of c in π1 (and hence

- of b in π2). Write Fi for the (ﬁnite) sigma-ﬁeld generated by the random variables listing


the partners of s1,...,si. The bijection just given and the Lipschitz property of f easily imply that E(f(π) | Fi+1) is always within C of E(f(π) | Fi). Thus the sequence (Xi)2i=0m with Xi = E(f(π) | Fi) is a martingale with diﬀerences bounded by C. The result now follows from the Hoeﬀding–Azuma inequality, noting that X0 = E(f(π)) and X2m = f(π).

![image 23](<2012-bollobs-old-approach-giant-component_images/imageFile23.png>)

![image 24](<2012-bollobs-old-approach-giant-component_images/imageFile24.png>)

![image 25](<2012-bollobs-old-approach-giant-component_images/imageFile25.png>)

![image 26](<2012-bollobs-old-approach-giant-component_images/imageFile26.png>)

Since Nk(G) changes by at most 2k when an edge is added to or deleted from a multigraph G, and a switching corresponds to deleting two edges and adding two edges, Nk(G∗d) is 8k-Lipschitz as a function of the pairing used to generate G∗d. (In fact, it is 4k-Lipschitz.) Thus Lemma 8 implies concentration of Nk(G∗d) = NP

(G∗d). Later we shall consider more general properties than Pk, and then we must work harder to obtain concentration results – in general for a local property P, there is no constant C = C(P) such that NP(G) is C-Lipschitz. So we need to modify our properties slightly, to ‘avoid high-degree vertices’.

k

For ∆ 2 and t 0, let M∆,t be the property that every vertex within graph distance t of the root has degree at most ∆. Note that M∆,t is (t + 1)local.

- Lemma 9. Let P be a t-local property, and let Q = P ∩ M∆,t. Then the number NQ(G) of vertices of a multigraph G with property Q changes by at most 4∆t if a single edge is added to or deleted from G. Furthermore, NQ(G) is 16∆t-Lipschitz.

Proof. The eﬀect of a switching on the corresponding conﬁguration multigraph is to delete two edges and then add two edges (perhaps between the same vertices). Thus it suﬃces to prove the ﬁrst statement.

Let v be a vertex of G such that one of (G,v) and (G+ e,v) has property Q but the other does not. Note that since M∆,t is monotone decreasing, (G,v) ∈ M∆,t. If e = xy, then the graph distance from v to {x,y} is the same in G and in G + e. Clearly, this distance is at most t; otherwise the presence of e would not aﬀect the property Q. Hence, in G, at least one endpoint of e is within distance t of v, so v is joined to an endpoint of e by a path in G of length at most t in which (since (G,v) ∈ M∆,t) each vertex has degree at most ∆. Each endpoint of e is the end of at most (1 + ∆ + ··· + ∆t) 2∆t such paths, so there can be at most 4∆t vertices v with the claimed property.

![image 27](<2012-bollobs-old-approach-giant-component_images/imageFile27.png>)

![image 28](<2012-bollobs-old-approach-giant-component_images/imageFile28.png>)

![image 29](<2012-bollobs-old-approach-giant-component_images/imageFile29.png>)

![image 30](<2012-bollobs-old-approach-giant-component_images/imageFile30.png>)

The next lemma shows that provided we choose ∆ large enough, there is no harm in considering only vertices whose local neighbourhoods contain only vertices with degree at most ∆.

- Lemma 10. Let D ∈ D, t 0 and ε > 0 be given. Then there exist δ > 0 and an integer ∆ such that


P(TD has M∆,t) 1 − ε/10 and

(G∗d) n − εn/2 e−δn (15) whenever dconf(d,D) < δ, where n = |d|.

P NM

∆,t

Thus for any given t and ε there is a ∆ such that with very high probability,

for dconf(d,D) small enough, at most εn/2 vertices of G∗d are within distance t of a vertex with degree larger than ∆.

Proof. The ﬁrst statement is immediate from the fact that the random variable M giving the maximum degree of any vertex of TD within distance t of the root is always ﬁnite, so there is some ∆ such that P(M > ∆) < ε/10. Corollary 7 implies that, if δ is small enough, then dconf(d,D) < δ implies that N = NM

(G∗d) has expectation within εn/10 of nP(TD ∈ M∆,t), so E(N) n − εn/5. By Lemma 9, applied with P the ‘trivial’ t-local property that always holds, as a function of the pairing used to generate G∗d, the quantity N is C-Lipschitz for some C. Now (15) follows by Lemma 8.

∆,t

![image 31](<2012-bollobs-old-approach-giant-component_images/imageFile31.png>)

![image 32](<2012-bollobs-old-approach-giant-component_images/imageFile32.png>)

![image 33](<2012-bollobs-old-approach-giant-component_images/imageFile33.png>)

![image 34](<2012-bollobs-old-approach-giant-component_images/imageFile34.png>)

We are now in a position to establish concentration of the number of vertices whose neighbourhoods have some local property. Theorem 11. Let P be a local property of rooted graphs, let D ∈ D and let ε > 0. There is some δ > 0 such that if dconf(d,D) < δ then

P NP(G∗d) − nP(TD ∈ P) εn e−δn, (16)

where n = |d|. Proof. Let D ∈ D, ε > 0 and a t-local property P be given, and let ∆ be

- as in Lemma 10. Let us say that an event holds with very high probability or wvhp if for some constant δ > 0 it has probability at least 1 − e−δn whenever dconf(d,D) < δ. So in particular, Lemma 10 tells us that wvhp all but at most


εn/2 vertices of G = G∗d have property M = M∆,t.

Let N = NP(G) be the number of vertices with property P, let B = n − NM(G) be the number of ‘bad’ vertices, i.e, ones not having property M, and let N′ = NP∩M be the number of ‘good’ vertices with property P. Then, wvhp,

|N − N′| B εn/2. By the ﬁrst part of Lemma 10, we have

|P(TD ∈ P) − P(TD ∈ P ∩ M)| P(TD ∈/ M) ε/10.

By Lemma 9, N′ is C-switching Lipschitz for some constant C, so by Corollary 7 and Lemma 8, we have that wvhp

|N′ − nP(TD ∈ P ∩ M)| εn/10, say. The last three displayed equations and the triangle inequality establish

(16). Corollary 12. Let D ∈ D, and let k 1 and ε > 0 be given. Then there exists δ > 0 such that if dconf(d,D) < δ then

![image 35](<2012-bollobs-old-approach-giant-component_images/imageFile35.png>)

![image 36](<2012-bollobs-old-approach-giant-component_images/imageFile36.png>)

![image 37](<2012-bollobs-old-approach-giant-component_images/imageFile37.png>)

![image 38](<2012-bollobs-old-approach-giant-component_images/imageFile38.png>)

P Nk − ρkn εn e−δn (17)

where n = |d|, Nk = Nk(G∗d) and ρk = P(|TD| = k).

Proof. Recall (14) and apply Theorem 11 to the property Pk.

![image 39](<2012-bollobs-old-approach-giant-component_images/imageFile39.png>)

![image 40](<2012-bollobs-old-approach-giant-component_images/imageFile40.png>)

![image 41](<2012-bollobs-old-approach-giant-component_images/imageFile41.png>)

![image 42](<2012-bollobs-old-approach-giant-component_images/imageFile42.png>)

This corollary proves the ﬁrst statement (10) of Theorem 2, and hence the corresponding statement in Theorem 1. One can obtain an explicit constant in the exponential error probability in (17) by using that Nk is 4k-Lipschitz, but there does not seem to be much point.

To conclude this section, we note that, as usual, summing over k′ < k and subtracting from n, bounds on Nk with k ﬁxed give bounds on N k as well, where N k(G) denotes the number of vertices of a graph G in components of order at least k.

Lemma 13. Let D ∈ D, ε > 0 and K be given. There exist k K and δ > 0 such that if dconf(d,D) < δ then

P N k − ρ(D)n εn e−δn, (18)

where n = |d|, N k = N k(G∗d) and ρ(D) = P(TD is inﬁnite).

Proof. Since k ρk(D) = P(|TD| < ∞) = 1 − ρ(D), there is some k K such that k k′−=11 ρk′ is within ε/2 of 1 − ρ(D). The result follows by applying Lemma 12 for each k′ k − 1, with ε/(2k) in place of ε.

![image 43](<2012-bollobs-old-approach-giant-component_images/imageFile43.png>)

![image 44](<2012-bollobs-old-approach-giant-component_images/imageFile44.png>)

![image 45](<2012-bollobs-old-approach-giant-component_images/imageFile45.png>)

![image 46](<2012-bollobs-old-approach-giant-component_images/imageFile46.png>)

As usual, the result for k ﬁxed extends to the case when k → ∞ slowly, showing, roughly speaking, that the probability that the branching process TD is inﬁnite gives the asymptotic proportion of vertices in ‘large’ components.

# 3 The survival probability ρ(D)

In this brief section we discuss the behaviour of the survival probability ρ(D) of the branching process TD. The result below is needed in the next section, but also helps to interpret Theorems 1 and 2.

Recall that from generation 1 onwards, TD behaves like the Galton–Watson branching process TD1 with oﬀspring distribution ZD deﬁned by (11), and that TD simply consists of a random number N of copies of TD1, with N having the distribution D.

Theorem 14. Let D be any distribution on the non-negative integers with P(D 3) > 0 and E(D) < ∞. Then ρ(D) > 0 if and only if E(D(D − 2)) > 0. Furthermore, writing x+ for the largest solution in [0,1] to

∞

x = 1 −

i=1

iri E(D)

(1 − x)i−1, (19)

![image 47](<2012-bollobs-old-approach-giant-component_images/imageFile47.png>)

where ri = P(D = i), we have

ρ(D) = 1 −

∞

ri(1 − x+)i. (20)

i=0

Finally, suppose that D1,D2,... are distributions on the non-negative integers such that Dn → D in distribution and E(Dn) → E(D). Then ρ(Dn) → ρ(D) as n → ∞.

Proof. Standard results on Galton–Watson processes tell us that the survival probability of TD1 is equal to x+, the largest solution in [0,1] to (19). Furthermore, since P(D 3) > 0 rules out the trivial case P(ZD = 1) = 1, we have x+ > 0 if and only if E(ZD) > 1. Conditioning on the number N of children of the root of TD gives (20) as an immediate consequence, and shows that ρ(D) > 0 if and only if x+ > 0, i.e., if and only if E(ZD) > 1. Since E(ZD) = i(i − 1)P(ZD = i − 1) = i i(i − 1)ri/ i iri, this condition is equivalent to i i(i − 2)ri > 0.

from Dn as in (11), i.e., by size-biasing and then subtracting 1. Since P(Dn = i) → ri and E(Dn) → E(D), we have P(ZD

For the last part, deﬁne ZD

n

= i) → P(ZD = i). Standard branching process results then imply that the survival probability of TD1

n

converges to that of TD1. Using (20), it follows easily that ρ(Dn) → ρ(D).

n

![image 48](<2012-bollobs-old-approach-giant-component_images/imageFile48.png>)

![image 49](<2012-bollobs-old-approach-giant-component_images/imageFile49.png>)

![image 50](<2012-bollobs-old-approach-giant-component_images/imageFile50.png>)

![image 51](<2012-bollobs-old-approach-giant-component_images/imageFile51.png>)

Remark 15. The formulae above coincide (as they must) with those given by Molloy and Reed [12] – one can check that x+ is equal to 1 − 1 − 2αD/K in their notation. They did not use the branching process interpretation, however. In the notation of Janson and Luczak [9], x+ is 1 − ξ, and ρ(D) is 1 − g(ξ).

![image 52](<2012-bollobs-old-approach-giant-component_images/imageFile52.png>)

# 4 Colouring and sprinkling

Our next task is to use ‘sprinkling’ to show that whp almost all vertices in ‘large’ components are in a single ‘giant’ component. In the original context of the random graphs G(n,p) and G(n,m), sprinkling is very simple to implement – ﬁrst include each edge independently with probability p1, then ‘sprinkle’ in extra edges by including each edge not already present independently with probability p2, where p1 +p2 −p1p1 = p. In the context of the conﬁguration model, there is no very simple analogue of this. Instead, we will ‘thin’ the random graph G∗d, and then put back the deleted edges.

Given 0 < p < 1, let G′ = G∗d[p] denote the random subgraph of G = G∗d obtained by retaining each edge independently with probability p, and let G′′ be the multigraph formed by the deleted edges, so V (G′′) = V (G′) = V (G) and E(G) is the disjoint union of E(G′) and E(G′′). Let d′ be the (random, of course) degree sequence of G′, and d′′ that of G′′, so d′i + d′′i = di for each vertex i ∈ V (G). The following simple observation is a key ingredient of the sprinkling argument.

Lemma 16. For any d and any 0 < p < 1, the random graphs G′ and G′′ are conditionally independent given d′, having the distributions of G∗d′ and G∗d′′ respectively.

Proof. This is essentially immediate from the deﬁnition of the conﬁguration model: recall that G is deﬁned from a pairing π of a set of 2m(d) stubs. Given

this pairing, colour each pair red with probability p and blue otherwise, independently of the others. Then we may take G′ to be given by the red pairs and G′′ by the blue pairs. Clearly, given the set of stubs in red pairs (which determines d′ and thus d′′), the pairing of these red stubs is uniformly random, and similarly for the blue stubs.

![image 53](<2012-bollobs-old-approach-giant-component_images/imageFile53.png>)

![image 54](<2012-bollobs-old-approach-giant-component_images/imageFile54.png>)

![image 55](<2012-bollobs-old-approach-giant-component_images/imageFile55.png>)

![image 56](<2012-bollobs-old-approach-giant-component_images/imageFile56.png>)

Our next aim is to extend the coupling result Theorem 11 to the pair (G′,G′′). First we need some deﬁnitions. We shall work with 2-coloured multigraphs (rather than coloured pairings as above). Given a degree sequence d and

- 0 < p < 1, let G∗d{p} denote the random coloured graph obtained by constructing G∗d and then colouring the edges independently, each red with probability p and blue otherwise. Thus G′ = G∗d[p] may be viewed as the red subgraph of G∗d{p}. Similarly, let TD{p} be the random coloured rooted tree obtained from TD by colouring each edge red with probability p and blue otherwise, independently of the others.


Given a probability distribution D on the non-negative integers, and 0 < p < 1, let Dp be the p-thinned version of D, which may be deﬁned by taking a random set X of size D and selecting elements of X independently with probability p. Then Dp is the (overall) distribution of the number of selected elements. To spell this out, and for later reference, writing ri = P(D = i) as usual, for 0 i j let

j i

pi(1 − p)j−i, (21) and let

rij = rj

ri′ =

rij. (22)

j i

Then

P(Dp = i) = ri′. (23) It is a simple exercise in basic probability to check that the operations of (i) p-thinning and (ii) size-biasing and then subtracting 1 commute. A simple consequence of this is that the component of the red subgraph of TD{p} containing the root has the same distribution as TD

.

p

The next result concerns ‘local properties of coloured rooted graphs’, which are deﬁned in the obvious way.

Theorem 17. Let P be a local property of coloured rooted graphs, let D ∈ D, let ε > 0 and let 0 < p < 1. There is some δ > 0 such that if dconf(d,D) < δ then

P NP(G∗d{p}) − nP(TD{p} ∈ P) εn e−δn, (24)

where n = |d|. Furthermore, if Q is a local property of rooted graphs, then there is some δ > 0 such that if dconf(d,D) < δ then

P NQ(G∗d[p]) − nP(TD

p

∈ Q) εn e−δn. (25)

Proof. From the remarks above, it suﬃces to prove the ﬁrst statement, (24). Then (25) may be deduced by applying (24) to the local property P that the component of the red graph containing the root has property Q. We give only an outline proof of (24), since the argument is a simple modiﬁcation of that of Theorem 11.

Firstly, the coloured analogue of Lemma 4 follows from Lemma 4: when the coupling as uncoloured graphs succeeds, we may apply the same (random) colouring to Γ t(v) as to TD|t. Arguing as before, we deduce the coloured analogue of Corollary 7. Now NP(G∗d{p}) depends not only on the conﬁguration, but also on the colouring. However, passing to a property Q = P ∩ M∆,t as in the proof of Theorem 17, by a variant of Lemma 9 we see that NQ changes by

- at most a constant (a) under a switching and (b) under changing the colour of a single edge. Now we can apply the Hoeﬀding–Azuma inequality to a martingale with 2m steps for the switchings and m for the colour choices, where m = m(d) is


the number of edges of G∗d, to deduce concentration of NP(G∗d{p}) and complete the proof.

![image 57](<2012-bollobs-old-approach-giant-component_images/imageFile57.png>)

![image 58](<2012-bollobs-old-approach-giant-component_images/imageFile58.png>)

![image 59](<2012-bollobs-old-approach-giant-component_images/imageFile59.png>)

![image 60](<2012-bollobs-old-approach-giant-component_images/imageFile60.png>)

Recall that ni = ni(d) is the number of vertices with degree i in G = G∗d. Let n′i be the number of vertices with degree i in the random subgraph G′ = G[p] deﬁned earlier. Also, for 0 i j, let nij be the number of vertices with degree i in G′ and degree j in G. Thus n′i = j i nij. Recall the deﬁnitions (21) and (22); at an intuitive level these formulae give the expected proportions of vertices of G′ having degree i (for ri′) and having degree i in G′ and degree j in G, ignoring the eﬀect of loops. Hence the next lemma comes as no surprise.

Lemma 18. Let D ∈ D and 0 < p < 1 be ﬁxed. Given 0 i j and ε > 0 there exists δ > 0 such that if dconf(d,D) < δ then

P |nij − rijn| εn e−δn and

P |n′i − ri′n| εn e−δn, where n = |d|.

Proof. Apply Theorem 17 to the 1-local coloured rooted graph properties ‘the root is incident with j edges in total of which i are red’ for the ﬁrst statement, and ‘the root is incident with i′ red edges’ for the second.

![image 61](<2012-bollobs-old-approach-giant-component_images/imageFile61.png>)

![image 62](<2012-bollobs-old-approach-giant-component_images/imageFile62.png>)

![image 63](<2012-bollobs-old-approach-giant-component_images/imageFile63.png>)

![image 64](<2012-bollobs-old-approach-giant-component_images/imageFile64.png>)

Recall that Dp, the p-thinned version of the probability distribution D, may be deﬁned by (23). Corollary 19. Given D ∈ D, 0 < p < 1 and ε > 0 there exists δ > 0 such that, if dconf(d,D) < δ, then

P dconf(d′,Dp) ε e−δn,

where d′ is the degree sequence of the random subgraph G[p] of G = G∗d and n = |d| = |d′| is the number of vertices.

Proof. Since E(D) < ∞ there is a constant C such that i C iri < ε/8. If δ is small enough, then dconf(d,D) < δ implies i C ini(d) < εn/4. Since D stochastically dominates Dp, and the degree of a vertex in our random subgraph G′ is at most its degree in G, the corresponding bounds for Dp and n′i = ni(d′n) follow. From the deﬁnition (3), (4) of dconf it thus suﬃces to prove that for each ﬁxed i < C we have |n′i − ri′n| ε/(2C2) with suﬃciently high probability; this follows from Lemma 18.

![image 65](<2012-bollobs-old-approach-giant-component_images/imageFile65.png>)

![image 66](<2012-bollobs-old-approach-giant-component_images/imageFile66.png>)

![image 67](<2012-bollobs-old-approach-giant-component_images/imageFile67.png>)

![image 68](<2012-bollobs-old-approach-giant-component_images/imageFile68.png>)

The next trivial lemma will be applied to the sprinkled edges.

- Lemma 20. Let A and B be disjoint sets of stubs in the conﬁguration model associated to G∗d. Then the probability that no stubs in A are paired to stubs in


- B is at most exp(−|A||B|/(8m)), where m = m(d).


Proof. Assume without loss of generality that |A| |B|. Perform a sequence of ⌈|A|/2⌉ experiments, each consisting of choosing an as-yet-unpaired stub in A and revealing its partner. In the ith experiment, there are at least |B| − (⌈|A|/2⌉ − 1) |B| − |A|/2 |B|/2 unpaired stubs in B, so the probability of ﬁnding the partner in B is at least (|B|/2)/(2m + 1 − 2i) |B|/(4m). Hence the probability that no partner in B is found is at most (1 − |B|/(4m))|A|/2 exp(−|A||B|/(8m)).

![image 69](<2012-bollobs-old-approach-giant-component_images/imageFile69.png>)

![image 70](<2012-bollobs-old-approach-giant-component_images/imageFile70.png>)

![image 71](<2012-bollobs-old-approach-giant-component_images/imageFile71.png>)

![image 72](<2012-bollobs-old-approach-giant-component_images/imageFile72.png>)

We are ﬁnally ready to prove the multigraph case of Theorem 2, where Gd is replaced by G∗d. Proof of Theorem 2 for G∗d. Let Li = Li(G∗d) be the number of vertices in the ith largest component of G∗d.

Fix D ∈ D and ε > 0. By Lemma 13 there are constants k and δ > 0 such that if dconf(d,D) < δ, then

P N k(G) (ρ(D) + ε/8)n e−δn.

Since L1 + L2 N k + 2k, if n is large enough (which we can ensure by taking δ small enough) it follows that

P L1 + L2 (ρ(D) + ε/4)n 1 − e−δn. (26) To complete the proof, it suﬃces to show that if dconf(d,D) < δ then

P L1 (ρ(D) − 3ε/4)n 1 − e−δn. (27)

Of course, this may require reducing δ. Indeed, (26) and (27) together give high probability upper and lower bounds on L1, and a high probability upper bound on L2. Since we have already proved (10) in Corollary 12, Theorem 2 then follows.

As p → 1, the probability distribution Dp deﬁned above converges to D, both in distribution and (since E(Dp) E(D) < ∞) in expectation. Hence, Theorem 14 tells us that ρ(Dp) → ρ(D) as p → 1. (This is the only place in the

argument where P(D 3) > 0 is used.) In particular, there is some p < 1 such that

ρ(Dp) ρ(D) − ε/8. Let us ﬁx such a p for the rest of the proof. Also, ﬁx an integer t 1 such that

pt ε/20, set

K = 1 + ∆ + ··· + ∆t−1 + 1, and let

α2 8E(D)

ε 40∆t

α =

and γ =

![image 73](<2012-bollobs-old-approach-giant-component_images/imageFile73.png>)

![image 74](<2012-bollobs-old-approach-giant-component_images/imageFile74.png>)

. (28)

We shall study the coloured random graph G∗d{p} deﬁned earlier, obtained from G∗d by colouring each edge red with probability p and blue otherwise, independently of the others. As before, we write G′ = G∗d[p] for the red subgraph and G′′ for the blue subgraph, and d′ and d′′ for the degree sequences of G′ and G′′. Recall that, by Lemma 16, given d′, we can view G′ and G′′ as independent conﬁguration multigraphs.

Applying Lemma 13 to G′, we ﬁnd that there exist k max{K,2/γ} and

- δ1 > 0 such that, writing S for the set of vertices in components of G′ with at least k vertices, we have


P |S| (ρ(D) − ε/4)n d′ P |S| (ρ(Dp) − ε/8)n d′ 1 − e−δ

1n

whenever dconf(d′,Dp) < δ1. By Corollary 19 there is a δ2 > 0 such that if dconf(d,D) < δ2, then

P dconf(d′,Dp) δ1 e−δ

2n.

Hence, reducing δ if necessary, it follows that if dconf(d,D) < δ then P |S| (ρ(D) − ε/4)n 1 − e−δ

1n − e−δ

2n 1 − e−δn. (29)

Note that in the argument above we could have sidestepped Corollary 19, using a coloured version of Theorem 13 and considering the coloured property ‘the red component of the root has size at least k’. However, the approach above seems more intuitive and we shall use Corollary 19 in Section 6.

Let us call a vertex v ∈ V (G) = V (G′) usable if it is incident with a blue edge, i.e., an edge of G′′. (These edges will be our ‘sprinkled’ edges.) Note that knowing d′ determines whether v is usable: we don’t know which edges are present in G′′, but we do know its degree sequence. Our next aim is to ﬁnd ‘enough’ usable vertices in S, for which we need some further deﬁnitions.

By the radius r(G) of a (locally ﬁnite) rooted graph G we mean the maximum distance of any vertex from the root, considering only vertices in the component

- C containing the root. Thus r(G) is inﬁnite if and only if C is inﬁnite.


Given a coloured rooted graph G, we write R(G) and B(G) for the red and blue subgraphs of G, respectively. Let Gt be the property of coloured rooted graphs G that either

- (i) r(R(G)) < t or
- (ii) some vertex of G within distance t of the root is incident with an edge


of B(G).

Note that, considering the shortest path to a blue edge, (ii) is equivalent to (ii’) some vertex of R(G) within distance t (in R(G)) of the root is incident with an edge of B(G). The property Gt is clearly (t + 1)-local.

Consider the case where G = TD{p} is a coloured rooted tree. Conditioning ﬁrst on the graph structure, if r(G) < t then (i) will certainly hold. Otherwise, there are at least t edges of G within distance t of the root, and if any one is blue (ii) holds. Thus

P(TD{p} ∈ Gt) 1 − pt 1 − ε/20. By Lemma 10 (with ε/2 in place of ε), there is some ∆ such that P(TD

∈ M∆,t) 1 − ε/20. Let H be the property

p

H = {R(G) ∈ M∆,t and G ∈ Gt}, noting that

P(TD{p} ∈ H) 1 − ε/10. (30)

We call a vertex v of our coloured conﬁguration model G = G∗d{p} helpful if (G,v) ∈ H, i.e., if G rooted at v has property H. Let H denote the set of

helpful vertices. From (30) and Theorem 17, if δ is chosen small enough, then if dconf(d,D) < δ we have

P |H| n − εn/5 e−δn. (31)

Since, as noted above, knowing d′ determines which vertices are usable (incident with edges of G′′), it is easy to check from the deﬁnition of H that knowing d (which is given), d′ and G′ determines which vertices of G are helpful.

From now on we condition on d′ and G′, assuming that |S| (ρ(D) − ε/4)n and |H| n − εn/5. (32)

This makes sense since S (the set of vertices in components of G′ with order at least k) and H are determined by d′ and G′, and (29) and (31) imply that the event (32) has probability at least 1 − e−δn.

Suppose that v ∈ S ∩ H. Then, since v is helpful, every vertex in the tneighbourhood ΓG

′

t(v) of v in G′ has degree at most ∆. Furthermore, from the deﬁnition of Gt (recalling (ii’) above), either (a) the radius of G′ rooted at v is at most t − 1, or (b) ΓG

′

t(v) meets an edge of G′′, i.e., contains a usable

vertex. In case (a), it follows that the component of v in G′ has at most

- 1 + ∆ + ··· + ∆t−1 < K vertices, contradicting v ∈ S. Thus case (b) holds and there is a path Pv = v0v1 ···vr in G′ of length at most t where v0 = v, each vi has degree at most ∆ in G′, and vr is usable.


At this point we are ﬁnally ready to apply the sprinkling strategy of Erdo˝s and R´enyi [4]. Let us call a partition (X,Y ) of S a potentially bad cut if |X|, |Y | εn/4 and there are no edges of G′ joining X to Y . We call (X,Y ) a bad cut if, in addition, no edge of G′′ joins X to Y . Since each component of G′ in S must lie either entirely in X or entirely in Y , there are at most

2|S|/k 2n/k en/k eγn/2 (33) potentially bad cuts, recalling that we chose k 2/γ.

Let (X,Y ) be a potentially bad cut, and recall that |H| n − εn/5. Thus X contains at least εn/20 helpful vertices v. From each there is a path Pv

- as described above ending at some usable vertex u. Because of the degree conditions, at most 1+∆+···+∆t 2∆t such paths can end at a given usable

vertex. Since Pv is a path in G′, and X is a union of components of G′, we conclude that X contains at least αn usable vertices, where α = ε/(40∆t) as in (28). Of course, the same applies to Y .

Recall that we have conditioned on d′ and G′, but not on G′′. In the conﬁguration model corresponding to G′′, each usable vertex has at least one stub, so X and Y each correspond to sets of at least αn stubs. Since (if δ is chosen small enough) G′′ has at most E(D)n edges, by Lemma 20

P G′′ contains no (X,Y ) edge | d′,G′ e−

α2n2

![image 75](<2012-bollobs-old-approach-giant-component_images/imageFile75.png>)

8E(D)n = e−γn. From (33) it follows that the expected number of bad cuts (given d′ and G′) is

- at most e−γn/2, so the probability that there are any bad cuts is at most e−γn/2.


When there are no bad cuts, it is easy to check that L1(G) |S| − 2εn/4 (ρ(D) − 3ε/4)n, completing the proof of (27) and hence of the multigraph case of Theorem 2.

![image 76](<2012-bollobs-old-approach-giant-component_images/imageFile76.png>)

![image 77](<2012-bollobs-old-approach-giant-component_images/imageFile77.png>)

![image 78](<2012-bollobs-old-approach-giant-component_images/imageFile78.png>)

![image 79](<2012-bollobs-old-approach-giant-component_images/imageFile79.png>)

# 5 Simple graphs

As noted in the introduction, Janson and Luczak [9] proved a result that is similar to the multigraph case of Theorem 2: the assumptions are identical, but the error bounds in the conclusions in [9] are much weaker. An advantage of our stronger error bounds is that they allow us to translate the result to random simple graphs without further restrictions on the degree sequences. For this we need a simple lemma.

- Lemma 21. Let D ∈ D. Then for any ε > 0 there exists a δ > 0 such that if dconf(d,D) < δ then


P G∗d is simple e−εn,

where n = |d|. Equivalently, if D ∈ D and dn → D in the sense that (1) and

(2) hold and |dn| → ∞, then P G∗d

is simple = e−o(|d

n|).

n

In particular, the degree sequences we consider here are (for large n) realizable by simple graphs. Proof. The equivalence of the two statements follows easily from (5); we prove the ﬁrst form.

Observe that there are constants K, M and α > 0 such that, if δ is chosen small enough, then dconf(d,D) < δ ensures that at least αn vertices of d have degree between 1 and K (inclusive), and m = m(d) Mn, where n = |d| as usual. Indeed, choose any K 1 such that P(D = K) > 0, let δ α = P(D = K)/2, and take M = E(D)/2+α, say. These properties and (8)/(9) are all that we need to know about d.

Let S denote the event that G∗d is simple, and ﬁx ε > 0. Pick η > 0 such that η log(4M/α) ε/2 and η α/2. By (9) there is a constant C, which we may take to be larger than K, such that if δ is small enough, then at most ηn stubs are attached to vertices of degree at least C. Let us call a vertex low degree if its degree is between 1 and K, and high degree if its degree is at least C. Let E be the event that the stubs attached to high degree vertices are paired with stubs attached to distinct low degree vertices.

To determine whether E holds, we test the at most ηn stubs attached to high degree vertices one-by-one. At each stage, there are at least αn − ηn αn/2 low-degree vertices none of whose stubs has yet been paired. Since each such vertex has degree at least one, and there are at most 2Mn unpaired stubs in total, it follows that

ηn

αn 4Mn

e−εn/2.

P(E)

![image 80](<2012-bollobs-old-approach-giant-component_images/imageFile80.png>)

When E holds, the graph G∗d is simple if and only if the graph G0 formed by the edges not incident with high-degree vertices is simple. But, after revealing

the partners of the stubs attached to the high-degree vertices, the conditional distribution of G0 is given by the conﬁguration model for some degree sequence in which all degrees are at most C, and at least αn/2 = Θ(n) degrees are positive. The original result of Bollob´s [2] (see also Bender and Canﬁeld [1]) thus gives P(S | E) = Θ(1), and the result follows.

![image 81](<2012-bollobs-old-approach-giant-component_images/imageFile81.png>)

![image 82](<2012-bollobs-old-approach-giant-component_images/imageFile82.png>)

![image 83](<2012-bollobs-old-approach-giant-component_images/imageFile83.png>)

![image 84](<2012-bollobs-old-approach-giant-component_images/imageFile84.png>)

Proof of Theorem 2 for Gd. Let P be any property of graphs. Since the distribution of G∗d conditioned on the event S that G∗d is simple is exactly that of Gd, we have

P(Gd ∈ P) = P(G∗d ∈ P | G∗d ∈ S)

P(G∗d ∈ P) P(G∗d ∈ S)

.

![image 85](<2012-bollobs-old-approach-giant-component_images/imageFile85.png>)

Fix D ∈ D. All statements about G∗d in Theorem 2 are of the form that for some property P, there exist γ,δ1 > 0 such that if dconf(d,D) < δ1, then

P(G∗d ∈ P) e−γn. (The theorem asserts this with δ1 = γ.) Lemma 21 gives us

- δ2 > 0 such that dconf(d,D) < δ2 implies P(G∗d ∈ S) e−γn/2. Hence, setting δ = min{δ1,δ2,γ/2}, if dconf(d,D) < δ then


P(Gd ∈ P) e−γn/e−γn/2 = e−γn/2 e−δn, completing the proof of Theorem 2.

![image 86](<2012-bollobs-old-approach-giant-component_images/imageFile86.png>)

![image 87](<2012-bollobs-old-approach-giant-component_images/imageFile87.png>)

![image 88](<2012-bollobs-old-approach-giant-component_images/imageFile88.png>)

![image 89](<2012-bollobs-old-approach-giant-component_images/imageFile89.png>)

As noted in the introduction, Theorem 2 implies Theorem 1.

# 6 Extensions

One of the motivations for studying the size of the largest component in the conﬁguration model Gd is to consider percolation in this random environment: given 0 < p < 1, when does the random subgraph Gd[p] of Gd obtained by selecting edges independently with probability p contain a giant component? For example, Goerdt [6] showed that when Gd is simply a random d-regular graph, then there is a ‘threshold’ at p = 1/(d − 1), above which a giant component appears. As is by now well known, for results of the present type this question turns out to be no more general than studying Gd directly (i.e., the case p = 1), since one can view a random subgraph of the conﬁguration model as another instance of the conﬁguration model. This is discussed in detail by Fountoulakis [5]; for a slightly diﬀerent approach see Janson [8]. We give the short argument since it is very easy with the ingredients we have to hand. In the next result we state only the most interesting part formally; Dp is the ‘pthinned’ version of the probability distribution D, deﬁned in (23) and appearing in Corollary 19.

Theorem 22. Let 0 < p < 1 be ﬁxed. The conclusions of Theorems 1 and 2 hold if G∗d or Gd is replaced by its random subgraph G∗d[p] or Gd[p], and ρ(D) and ρk(D) are replaced by ρ(Dp) and ρk(Dp).

In particular, given D ∈ D with P(D 3) > 0, 0 < p < 1 and ε > 0, there exists δ > 0 such that, if dconf(d,D) < δ, then

P L1(Gd[p]) − ρ(Dp)n εn e−δn and

P L1(G∗d[p]) − ρ(Dp)n εn e−δn, where n = |d|.

Proof. For G∗d[p], this is essentially trivial from Theorem 2 and Corollary 19. Indeed, by Theorem 2 there exists δ1 > 0 such that if dconf(d1,Dp) < δ1 then G∗d

has the desired property (L1 close to ρ(Dp)n) with probability at least 1− e−δ

1

1n. By Corollary 19 there is a δ such if dconf(d,D) < δ then P(dconf(d′,Dp) < δ1) 1 − e−δn, where d′ is the degree sequence of G∗d[p]. The result for G∗d[p] follows by noting that, conditional on d′, G∗d[p] has the distribution of G∗d′.

For Gd[p] we argue as in the last part of the previous section: note that

conditional on G∗d being simple, G∗d[p] has the same distribution as Gd[p]. Then use Lemma 21 as before. The key point is that we do not try to condition on

G∗d[p] being simple.

![image 90](<2012-bollobs-old-approach-giant-component_images/imageFile90.png>)

![image 91](<2012-bollobs-old-approach-giant-component_images/imageFile91.png>)

![image 92](<2012-bollobs-old-approach-giant-component_images/imageFile92.png>)

![image 93](<2012-bollobs-old-approach-giant-component_images/imageFile93.png>)

- Remark 23. Theorem 22 implies that there is a ‘critical’ pc such that G∗d[p] has a giant component if and only if p > pc. Indeed, pc = inf{p : ρ(Dp) = 0}. From basic branching process results, it is easy to see that pc = 1/E(ZD), where ZD is the distribution deﬁned in (11). Either from this, or from the fact that ρ(Dp) > 0 if and only if E(Dp(Dp − 2)) > 0 it is easy to see that

pc =

E(D) E(D(D − 1))

![image 94](<2012-bollobs-old-approach-giant-component_images/imageFile94.png>)

.

This is the same formula as given by Fountoulakis [5], for example, who proved a form of Theorem 22, with stronger assumptions on the degree sequences and weaker error bounds.

- Remark 24. Taking |dn| = n for notational simplicity, in the context of Theorems 1 and 2, the assumption that E(D) < ∞, corresponding to m(dn) = O(n), is very natural. Indeed, it is not hard to see that if m(dn)/n → ∞, then


G∗d

will with high probability contain a component with n − o(n) vertices. As soon as we consider percolation on G∗d

n

, however, it makes very good sense to allow m(dn)/n → ∞ and then study G∗d

n

[pn] with pn → 0 as n → ∞. All we shall say here is that in many situations, for appropriate pn, the (random) degree sequence of G∗d

n

[pn] will with high probability be such that Theorem 1 applies to it. For example, if all degrees are equal to kn with kn → ∞ and knpn → λ ∈ R, then the degree distribution of G∗d

n

[pn] will be asymptotically Poisson with mean λ. Hence Theorem 1 can be used to show that the threshold for percolation on G∗d

n

is at λ = 1, i.e., at pn = 1/kn.

n

Throughout the paper we have focussed on the number of vertices in the giant component. What can we say about other properties of the giant component, such as the number of vertices of given degree, or the total number of edges? Results for these are given (under diﬀerent conditions) by Janson and Luczak [9], for example. An often neglected beneﬁt of the branching-process viewpoint is that it typically gives results of this type essentially automatically, not just for these properties, but for any local property. (A version of this observation was made in a diﬀerent context by Bollob´s, Janson and Riordan [3, Lemma 11.11]; see also [14, Theorem 2.8].)

We state the following result in a form analogous to Theorem 2; this of course implies a version analogous to Theorem 1.

Theorem 25. Let P be a local property of rooted graphs, let D ∈ D and let ε > 0. There is some δ > 0 such that if dconf(d,D) < δ then the following hold, with n = |d| and G = G∗d or G = Gd:

P NP(G) − nP(TD has P) εn e−δn, (34)

and

P NP(C1) − nP(TD is inﬁnite and has P) εn e−δn, (35) where C1 is a component of G of maximal order. Proof. As usual, in the light of Lemma 21 we need only consider the case G = G∗d. In this case, we have proved (34) already in Theorem 11.

Turning to (35), let D ∈ D, ε > 0 and a local property P be given. Let Sk be the rooted-graph property ‘the component of the root contains at least k vertices’, and S∞ ‘the component of the root is inﬁnite’. (We only consider the latter in the context of TD; all our graphs here are ﬁnite.) Then, as k → ∞, the events {TD ∈ Sk} = {|TD| k} decrease to the event {TD ∈ S∞} = {TD is inﬁnite}. Hence P(TD ∈ Sk) → P(TD ∈ S∞), and there is a constant K such that for any k K we have

P(TD ∈ Sk \ S∞) < ε/10. (36)

As before, let us say that an event holds ‘wvhp’ if for some δ > 0 it holds with probability at least 1 − e−δn whenever dconf(d,D) < δ. By Lemma 13 there is some k K such that wvhp

N k(G∗d) − ρ(D)n εn/10. (37)

Let N = NP(C1) be the number of vertices we wish to count, i.e., those in the largest component C1 of G∗d having property P. Let N′ = NP∩S

(G∗d) count vertices with property P in components of size at least k. Then N and N′ diﬀer by at most N k −L1, which, by (37) and Theorem 2, is wvhp at most εn/5, say. Applying (34) to the local property P ∩ Sk, we deduce that wvhp N is within εn/4 of nP(TD ∈ P ∩Sk). But by (36) this is within εn/10 of nP(TD ∈ P ∩S∞), establishing (35).

k

![image 95](<2012-bollobs-old-approach-giant-component_images/imageFile95.png>)

![image 96](<2012-bollobs-old-approach-giant-component_images/imageFile96.png>)

![image 97](<2012-bollobs-old-approach-giant-component_images/imageFile97.png>)

![image 98](<2012-bollobs-old-approach-giant-component_images/imageFile98.png>)

For simple properties P, it is easy to give explicit formulae for the probability that TD is inﬁnite and has property P. For example, if P = Pd is the property that the root has degree d, then deﬁning x+ as in Section 3, the proof of Theorem 14 shows easily that

P(TD is inﬁnite and has Pd) = rd(1 − (1 − x+)d).

This gives an asymptotic formula for the number of degree-d vertices in the giant component C1 that coincides with that of Janson and Luczak [9].

Rather than counting vertices with some local property, what happens if we want to sum some ‘local function’ f(G,v) over vertices v ∈ C1? Can we show that

f(C1,v) →p E(f(TD))? (38)

n−1

v∈C1

If f is bounded then the answer is yes: simply express f in terms of indicator functions of local properties and apply Theorem 25. In general, (38) need not

hold: for example, if f(G,v) is the square of the degree of v then, since our assumptions give no control over i d2i, (38) can fail.

f(C1,v) is twice the number of edges in the giant component. Then, by (9), for any ε > 0 there is a C such that if dconf(d,D) is small enough, then

Suppose that f(G,v) is the degree of v, so v∈C

1

f(C1,v)

v∈C1:dC1(v) C

f(G,v) εn,

v∈G:dG(v) C

and considering the bounded function obtained by truncating f at C, we see that (38) holds in this case, even though f is unbounded. A similar argument can be applied to other unbounded f, leading to results concerning, for example, the number edges in the giant component between vertices of degree 2 and degree 3. We omit the details.

# References

- [1] E.A. Bender and R.E. Canﬁeld, The asymptotic number of labeled graphs with given degree sequences, J. Combinatorial Theory Ser. A 24 (1978), 296–307.
- [2] B. Bollob´as, A probabilistic proof of an asymptotic formula for the number of labelled regular graphs, European J. Combin. 1 (1980), 311–316.
- [3] B. Bollob´as, S. Janson and O. Riordan, The phase transition in inhomogeneous random graphs, Random Struct. Algorithms 31 (2007), 3–122.
- [4] P. Erdo˝s and A. R´enyi, On the evolution of random graphs, Magyar Tud. Akad. Mat. Kutato´ Int. K¨ozl 5 (1960), 17–61.
- [5] N. Fountoulakis, Percolation on sparse random graphs with given degree sequence, Internet Mathematics 4 (2007), 329–356.
- [6] A. Goerdt, The giant component threshold for random regular graphs with edge faults, Theoret. Comput. Sci. 259 (2001), 307–321.
- [7] H. Hatami and M. Molloy, The scaling window for a random graph with a given degree sequence, Random Struct. Algorithms 41 (2012), 99–123.
- [8] S. Janson, On percolation in random graphs with given vertex degrees, Electron. J. Probab. 14 (2009), 87–118.
- [9] S. Janson and M.J. Luczak, A new approach to the giant component problem, Random Struct. Algorithms 34 (2009), 197–216.
- [10] M. Kang and T.G. Seierstad, The critical phase for random graphs with a given degree sequence, Combin. Probab. Comput. 17 (2008), 67–86.


- [11] M. Molloy and B. Reed, A critical point for random graphs with a given degree sequence, Random Struct. Algorithms 6 (1995), 161–179.
- [12] M. Molloy and B. Reed, The size of the giant component of a random graph with a given degree sequence, Combin. Probab. Comput. 7 (1998), 295–305.
- [13] B. Pittel, Edge percolation on a random regular graph of low degree, Ann. Probab. 36 (2008) 1359–1389.
- [14] O. Riordan, The k-core and branching processes, Combin. Probab. Comput. 17 (2008), 111–136.
- [15] O. Riordan, The phase transition in the conﬁguration model, Combin. Probab. Comput. 21 (2012), 265–299.


