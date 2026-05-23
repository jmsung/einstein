---
type: source
kind: paper
title: Stability of large cuts in random graphs
authors: Ilay Hoshen, Wojciech Samotij, Maksim Zhukovskii
year: 2024
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2402.14620v1
source_local: ../raw/2024-hoshen-stability-large-cuts-random.pdf
topic: general-knowledge
cites:
---

arXiv:2402.14620v1[math.CO]22Feb2024

STABILITY OF LARGE CUTS IN RANDOM GRAPHS

ILAY HOSHEN, WOJCIECH SAMOTIJ, AND MAKSIM ZHUKOVSKII

Abstract. We prove that the family of largest cuts in the binomial random graph exhibits the following stability property: If 1/n ≪ p = 1 − Ω(1), then, with high probability, there is a set of n − o(n) vertices that is partitioned in the same manner by all maximum cuts of Gn,p. Moreover, the analogous statement remains true when one replaces maximum cuts with nearly-maximum cuts.

We then demonstrate how one can use this statement as a tool for showing that certain properties of Gn,p that hold in a ﬁxed balanced cut hold simultaneously in all maximum cuts. We provide two example applications of this tool. First, we prove that maximum cuts in Gn,p typically partition the neighbourhood of every vertex into nearly equal parts; this resolves a conjecture of DeMarco and Kahn for all but a narrow range of densities p. Second, for all edge-critical, nonbipartite, and strictly 2-balanced graphs H, we prove a lower bound on the threshold density p above which every largest H-free subgraph of Gn,p is (χ(H) − 1)-partite. Our lower bound exactly matches the upper bound on this threshold recently obtained by the ﬁrst two authors.

1. Introduction

Let r 2 be an integer. An r-cut in a graph G is a partition of its vertex set into r subsets. The size of a cut is the number of edges of G with endpoints in diﬀerent parts of the cut. A maximum r-cut of G is an r-cut that has the largest size (among all r-cuts in G). Since the problem of determining the size of a maximum r-cut in a graph is NP-hard for every r 2, much eﬀort has been devoted to studying maximum cuts in random graphs, which can be viewed as the average-case variant of the general problem. In spite of this, we still know relatively little even about maximum 2-cuts in the binomial random graph Gn,p, except in the regime p = O(1/n), see [5, 8, 10, 11]. In particular, the state-of-the-art result [3] falls short of determining the precise asymptotics of the second-order term1 in the typical size of a maximum r-cut in Gn,p in the regime p ≫ 1/n, determining it only up to a multiplicative constant.

The main obstacle in studying properties of maximum cuts in random graphs is that, even if a given property holds with high probability2 for a ﬁxed cut, commonly this probability is not suﬃciently close to one to warrant a union bound over all (exponentially many in the number of vertices) choices of a cut. In an attempt to remedy this, Brightwell, Panagiotou, and Steger [2] proved that, if 1/n ≪ p 1/2, then whp any two

![image 1](<2024-hoshen-stability-large-cuts-random_images/imageFile1.png>)

This research was supported by: the Israel Science Foundation grant 2110/22; the grant 2019679 from the United States–Israel Binational Science Foundation (BSF) and the United States National Science Foundation (NSF); and the ERC Consolidator Grant 101044123 (RandomHypGra).

1It is easy to see that the ﬁrst-order term is (1 − 1/r)n2p/2. 2With probability approaching 1 as n → ∞; in what follows, we will write ‘whp’ for brevity.

1

maximum 2-cuts in Gn,p diﬀer in a small number of vertices. Although this implies that the number of maximum 2-cuts in Gn,p is typically subexponential in n, this is still not enough to treat a maximum cut as a ﬁxed cut. Brightwell, Panagiotou, and Steger also suggested that whp Gn,p has the following stronger property: There are disjoint vertex sets S1 and S2, each containing nearly n/2 vertices, that are contained in opposite parts of every maximum 2-cut in Gn,p. Intuitively, such property could prove useful in approximating a maximum cut by a ﬁxed cut. This is because additionally requiring that S1 and S2 are inclusion-maximal with the above property ensures that the pair {S1,S2} is unique.

In this paper, we not only conﬁrm the prediction of Brightwell, Panagiotou, and Steger but also show how one may exploit this ‘clustering’ property of maximum cuts while studying properties of Gn,p. Let br(G) denote the maximum size of an r-cut of

- G. The deﬁcit of an r-cut in G is the diﬀerence between br(G) and the size of the cut. Given integers d 0 and r 2 and a real α > 0, we say that a graph G admits a


(d,r,α)-core if there exist r pairwise-disjoint sets of vertices S1,... ,Sr of size exceeding (1/r − α) · |V (G)| each that are contained in diﬀerent parts of every r-cut of G with deﬁcit at most d. (We will give a precise deﬁnition of a core in Section 2.) The following statement is an abbreviated, qualitative version of our main result. We postpone the full, unabbreviated statement to Section 2.

- Theorem 1.1. The following hold for every integer r 2, real α > 0, and all p = p(n) satisfying 1/n ≪ p = 1 − Ω(1):


- (i) If d ≪

√np, then whp Gn,p admits a (d,r,α)-core.

![image 2](<2024-hoshen-stability-large-cuts-random_images/imageFile2.png>)

- (ii) There exists a C = C(α) > 0 such that, for every d C√np, whp no set of αn vertices is entirely contained in a single part of every r-cut with deﬁcit at most d.


![image 3](<2024-hoshen-stability-large-cuts-random_images/imageFile3.png>)

- Theorem 1.1 implies, in particular, that whp each maximum r-cut in Gn,p ‘respects’


a single partition of all but some o(n) vertices into r parts. The aforementioned unabbreviated version of the theorem replaces this o(n) with ω n/p, where ω is an arbitrary function that tends to inﬁnity with n. While we do believe that this is optimal, in the sense that whp the largest set of vertices that is partitioned the same way by all largest r-cuts has size n − Ω( n/p), currently we cannot even show that the probability that Gn,p has a unique largest 2-cut is bounded away from one. In order to support our belief, we will at least show that the expected number of vertices of Gn,p that lie outside of its core is Ω( n/p). We discuss this in more detail in Section 2.6.

![image 4](<2024-hoshen-stability-large-cuts-random_images/imageFile4.png>)

![image 5](<2024-hoshen-stability-large-cuts-random_images/imageFile5.png>)

![image 6](<2024-hoshen-stability-large-cuts-random_images/imageFile6.png>)

An important aspect of Theorem 1.1 is that the property of admitting a core is ‘stable’ under small perturbations of the edge set of a graph. More precisely, if a graph G admits a (d,r,α)-core, then any graph G′ that is obtained from G by adding/removing some t d edges to/from G still admits a (d − t,r,α)-core (moreover, the core of G′ contains the core of G in a sense that will be made precise by Corollary 2.7 below). We will be able to exploit this fact when analysing certain properties of Gn,p that concern the distribution of its edges relative to a maximum cut. Roughly speaking, the stability property of cores will allow one to change a small proportion of adjacencies in Gn,p while

keeping the set of maximum cuts essentially unchanged (and thus determined up to the locations of o(n) vertices).

In the second part of this work, we present two applications of Theorem 1.1. First, we resolve (almost fully) a conjecture of DeMarco and Kahn [6] stating that maximum cuts partition neighbourhoods of all vertices almost equally, see Section 1.1 below. Second, for every nonbipartite edge-critical and strictly 2-balanced graph H, we prove an optimal lower bound on the threshold probability for the property that every largest H-free subgraph of Gn,p is (χ(H)−1)-partite; a matching upper bound on this threshold probability was recently proved by the ﬁrst two authors [14]. This resolves another problem proposed by DeMarco and Kahn [6] and refutes their guess regarding the location of the said threshold. We present the relevant background, as well as our results, in Section 1.2.

- 1.1. Neighbourhoods in maximum cuts. It is easy to show that, as soon as p ≫

log n/n, a ﬁxed 2-cut of Gn,p into sets of size n/2+o(n) (we call such a cut balanced) whp divides the neighbourhood of every vertex into parts of size (1/2 + o(1))np. Obviously, this is not true for all balanced cuts, but is it true for all maximum cuts? It was conjectured by DeMarco and Kahn [6, Conjecture 13.2] that the answer is yes, for all p ≫ log n/n. In Section 3, we conﬁrm the conjecture for all p ≫ (log n)2/n. In fact, with only little extra work, we generalise this result to r-cuts and common neighbourhoods of sets of vertices of any constant size.

Theorem 1.2. Let k 1, r 2 be integers and let ε > 0. There exists C > 0 such that, for all p satisfying p C(log n/n)1/k and p ≫ (log n)2/n, whp every maximum r-cut of Gn,p partitions the common neighbourhood of every set of k vertices into parts of size (1/r ± ε)npk each.

It is not hard to see that the lower-bound assumption on p is optimal (up to the value of C) for all k 2 and r 2. While we do believe that the assumption p ≫ (log n)2/n (which comes in force only when k = 1) may be weakened to p ≫ log n/n, proving this would likely involve signiﬁcantly new ideas. The reason why we need this additional assumption is that, in order to overcome the union bound over the choice of the set of vertices whose neighbourhood we are analysing, we need to resample Θ(log n) edges of Gn,p; however, this seems to require good control over cuts with deﬁcit Θ(log n), which we do not have unless p ≫ (log n)2/n, see the second part of Theorem 1.1.

- 1.2. Sharp thresholds for Simonovits’s theorem in Gn,p. The well-known theorem of Tura´n [20] states that, for every r 2 and all n, the largest Kr+1-free subgraphs of the complete graph Kn are its largest r-partite subgraphs. Simonovits [19] proved that a similar result holds also for edge-critical graphs; we say that a graph H is edge-critical if χ(H \e) = χ(H) −1 for some edge e ∈ H, where χ(H) is the chromatic number of H.


- Theorem 1.3 ([19]). If a graph H is edge-critical and n is a suﬃciently large integer, then every largest H-free subgraph of Kn is (χ(H) − 1)-partite.


Let us call a graph H-Simonovits, if each of its largest H-free subgraphs is (χ(H)−1)partite. Note that the assumption that H is edge-critical in the above theorem is crucial. Indeed, adding one edge to a (χ(H)−1)-partite graph cannot introduce a copy of H unless

- H is edge-critical. Consequently, if H is not edge-critical, then no graph with chromatic


number at least χ(H) can be H-Simonovits (in particular, no Kn with n χ(H) is H-Simonovits).

To the best of our knowledge, the ﬁrst to study the question of when Gn,p is whp H-Simonovits were Babai, Simonovits, and Spencer [1]. They proved that, for every ℓ 1, Gn,p is whp C2ℓ+1-Simonovits as long as p 1/2 − εℓ for some (small) positive constant εℓ that depends only on ℓ. Answering a challenge raised by the authors of [1], Brightwell, Panagiotou, and Steger [2] proved that Gn,p is whp Kr+1-Simonovits, for every r 2, already when p n−cr for some (small) constant cr > 0.

It is not hard to see that as soon as the expected number of copies of some subgraph

- F ⊆ H in Gn,p becomes signiﬁcantly smaller than the expected number of edges, Gn,p cannot be H-Simonovits.3 This implies that Gn,p cannot be H-Simonovits whp, unless p = Ω(n−1/m2(H)), where (we write eF and vF for the numbers of edges and vertices of a graph F, respectively)


eF − 1 vF − 2

m2(H) := max

: F ⊆ H, eF 2

![image 7](<2024-hoshen-stability-large-cuts-random_images/imageFile7.png>)

is the 2-density of H. Kohayakawa,  Luczak, and Ro¨dl [16] conjectured that, for every nonbipartite graph H (not necessarily edge-critical), when p ≫ n−1/m2(H), then whp every largest H-free subgraph of Gn,p is close to being (χ(H) − 1)-partite (i.e., it can be made (χ(H) − 1)-partite by removing some o(n2p) edges). This was proved in the breakthrough work of Conlon and Gowers [4], under the technical assumption that H is also strictly 2-balanced (i.e., the maximum in the deﬁnition of the 2-density is achieved uniquely at F = H), which was later removed by the second author [17], using an adaptation of the argument of Schacht [18], who proved the slightly weaker assertion that whp every H-free subgraph of Gn,p has at most (1−1/(χ(H)−1)+o(1)) n2 p edges.

In another major development, DeMarco and Kahn [6, 7] showed that adding an extra polylogarithmic factor in the lower bound on p suﬃces to show that, when H is a clique, then whp Gn,p is H-Simonovits. Moreover, their lower-bound assumption on p is best possible up to a constant factor. This result was recently generalised by the ﬁrst two authors [14] to every nonbipartite, strictly 2-balanced, and edge-critical graph H.

In order to state the main result of [14], we need an additional deﬁnition. First, let us denote by Kr(m) the complete, balanced r-partite graph with parts of size m and let Kr(m)+ be the graph obtained from Kr(m) by adding a single edge contained in one of the parts. (Note that H is edge-critical if and only if H ⊆ Kχ(H)−1(m)+ for all m vH.) Letting Cop(H,G) be the number of copies of H in G, set

Cop H,Kχ(H)−1(m)+

πH := lim

mvH−2 > 0. (1) 3Unless p = O(1/n), since then χ(Gn,p) = O(1) whp and a more careful analysis is required.

![image 8](<2024-hoshen-stability-large-cuts-random_images/imageFile8.png>)

m→∞

![image 9](<2024-hoshen-stability-large-cuts-random_images/imageFile9.png>)

Finally, let θH be the positive real satisfying (χ(H) − 1)2−vH · πH · θHeH−1 = 2 −

1 m2(H)

. (2)

![image 10](<2024-hoshen-stability-large-cuts-random_images/imageFile10.png>)

- Theorem 1.4 ([14]). If H is a nonbipartite, edge-critical, strictly 2-balanced graph and p (θH + ε) · n−1/m2(H)(log n)1/(eH−1)

for some positive constant ε, then whp Gn,p is H-Simonovits.

In Section 4, we show that θHn−1/m2(H)(log n)1/(eH−1) is in fact a sharp threshold for the property of being H-Simonovits. This conﬁrms the prediction made in [14] (and refutes the suggestion of DeMarco and Kahn [6] in the case of when H is a complete graph).

- Theorem 1.5. If H is a nonbipartite, edge-critical, strictly 2-balanced graph and 1/n ≪ p (θH − ε) · n−1/m2(H)(log n)1/(eH−1)


for some positive constant ε, then whp Gn,p is not H-Simonovits.

It remains an interesting open problem to extend Theorems 1.4 and 1.5 to edgecritical graphs H that are not strictly 2-balanced. We note that the closely-related problem of describing the typical structure of H-free graphs with given order and size, for an arbitrary edge-critical graph H, was studied in [9].

- 1.3. Relation to previous works. The notions of cores and rigidity (deﬁned in Section 2), which play a central role in our arguments, were ﬁrst introduced by DeMarco and Kahn [6]. In fact, one can infer from the proof of [6, Lemma 12.3] that the random


graph Gn,p is typically close (up to adding/removing a small number of edges) to a graph that has a (0,r,o(1))-core. Finally, even though the result of Brightwell, Panagiotou, and Steger [2] does not imply the existence of a core, our proof of the fact that the random graph typically has a (0,r,o(1))-core (the case d = 0 in Theorem 1.1) was inspired by their arguments.

Organisation. The remainder of this paper is organised as follows. Section 2 is devoted to the proof of Theorem 1.1. In fact, the main results of this section are Theorem 2.1 and Corollary 2.2, the latter of which is a stronger, non-asymptotic version of Theorem 1.1. In the following two sections, we prove Theorems 1.2 and 1.5, respectively.

2. Rigidity

Recall the deﬁnitions of an r-cut and the size and the deﬁcit of a cut. In order to quantify the ‘clustering’ property of the family of cuts with a small deﬁcit in a graph G, we will count pairs of vertices of G that are never separated by such a cut. To make this precise, given integers r 2 and d 0, we say that two vertices are (d,r)-equivalent in G if they are in the same part of every r-cut in G with deﬁcit at most d. Further, we say that G is (d,r,ε)-rigid, for some ε > 0, if there are at least 1−rε n2 pairs of

![image 11](<2024-hoshen-stability-large-cuts-random_images/imageFile11.png>)

(d,r)-equivalent vertices. The following theorem, which is the main result of this work, provides a lower bound on the probability that the uniform random graph G(n,m) is (d,r,ε)-rigid for given d, r, and ε (that are allowed to depend on n and m).

- Theorem 2.1. There exists an absolute constant C such that, for all δ,ε ∈ (0,1) and all nonnegative integers d,m,n,r satisfying r 2 and 1 m (1 − δ) n2 ,


![image 12](<2024-hoshen-stability-large-cuts-random_images/imageFile12.png>)

![image 13](<2024-hoshen-stability-large-cuts-random_images/imageFile13.png>)

d + 1 δ

n m

n m

Cr ε ·

+ 4

+ r ·

.

P G(n,m) is not (d,r,ε)-rigid

![image 14](<2024-hoshen-stability-large-cuts-random_images/imageFile14.png>)

![image 15](<2024-hoshen-stability-large-cuts-random_images/imageFile15.png>)

![image 16](<2024-hoshen-stability-large-cuts-random_images/imageFile16.png>)

![image 17](<2024-hoshen-stability-large-cuts-random_images/imageFile17.png>)

Let us now relate the property of being rigid to the property of admitting a core from the statement of Theorem 1.1. To this end, note ﬁrst that (d,r)-equivalence is an equivalence relation on the vertex set of G; we shall call its equivalence classes the (d,r)-components of G. In the case when the r largest (d,r)-components C1,... ,Cr of

- G have strictly more than n/(r + 1) vertices each (and thus all remaining components


have fewer than n/(r + 1) vertices), we call the set corerd(G) := {C1,... ,Cr} the (d,r)core of G. We will show that, under mild assumptions on the distribution of edges of G (that G(n,m) fails to have with probability much smaller than the upper bound in Theorem 2.1), the fact that G is (d,r,ε)-rigid implies that it has a (d,r)-core whose each component has at least n/r −rεn vertices. In particular, letting CORErd(α) denote the set of all graphs on n that have a (d,r)-core whose each component has at least n/r − αn vertices, Theorem 2.1 will imply the following statement.

Corollary 2.2. There exists an absolute constant C such that, for all α,δ ∈ (0,1) and all nonnegative integers d,m,n,r satisfying r 2, α < 1/(r2 + r), and 1 m (1 − δ) n2 ,

Cr2 α ·

![image 18](<2024-hoshen-stability-large-cuts-random_images/imageFile18.png>)

![image 19](<2024-hoshen-stability-large-cuts-random_images/imageFile19.png>)

d + 1 δ

n m

n m

P G(n,m) ∈/ CORErd(α)

+ 4

+ r ·

.

![image 20](<2024-hoshen-stability-large-cuts-random_images/imageFile20.png>)

![image 21](<2024-hoshen-stability-large-cuts-random_images/imageFile21.png>)

![image 22](<2024-hoshen-stability-large-cuts-random_images/imageFile22.png>)

![image 23](<2024-hoshen-stability-large-cuts-random_images/imageFile23.png>)

Organisation. The remainder of this section is organised as follows. First, in Section 2.1, we establish two crucial properties of the dynamics of the sets of (d,r)-equivalent pairs of vertices with respect to addition/deletion of edges. Next, in Section 2.2, we derive several (standard) estimates regarding the concentration of the number of edges in various induced subgraphs of G(n,m) and sizes of the parts in cuts with small deﬁcit. In Section 2.3, we use the results established in the previous two subsections to prove Theorem 2.1 and in Section 2.4, we derive Corollary 2.2. Finally, in Section 2.5 we prove Theorem 1.1.

Notation. Given integers d 0 and r 2, the set of (d,r)-equivalent pairs in a graph G will be henceforth denoted by eqrd(G). For brevity, we will identify a graph with its set of edges; in particular, we will write |G| to denote the number of edges in a graph G. Following DeMarco and Kahn [6], we will use the following notational conventions: First, given a collection Π of pairwise-disjoint sets of vertices in a graph (e.g., a cut), we will denote the set of pairs of vertices contained in a single set of Π by int(Π) and the set of remaining pairs of vertices of Π by ext(Π); this way

br(G) = max{|ext(Π) ∩ G| : Π is an r-cut}.

Second, given an integer r 2, we will write critr(G) to denote the set of edges of G that cross all maximum r-cuts (the r-critical edges of G). Finally, given two families C and C′ of pairwise-disjoint sets of vertices, we will write C C′ if each element of C is contained in some element of C′. In other words,

C C′ ⇐⇒ ∀X ∈ C ∃X′ ∈ C′ X ⊆ X′ ⇐⇒ int(C) ⊆ int(C′).

- 2.1. Dynamics of equivalent pairs. Suppose that r 2 and that G is an arbitrary graph on n . The proof of Theorem 2.1 will exploit the following crucial property of the dynamics of the sequence (eqrd(G))d with respect to addition of edges. Lemma 2.3. The following holds for all integers r 2 and d 0 and every e ∈ Kn: If e ∈/ G ∪ eqrd+1(G), then e ∈/ eqrd(G ∪ e).


Before we prove the lemma, it will be useful to observe the following alternative deﬁnitions of the set of (0,r)-equivalent pairs. Fact 2.4. The following statements are equivalent for all e ∈ Kn \ G:

- • e ∈/ eqr0(G);
- • e ∈ ext(Π) for some maximum r-cut Π of G;
- • e ∈ ext(Π) for all maximum r-cuts Π of G ∪ e (that is, e ∈ critr(G ∪ e))
- • br(G ∪ e) = br(G) + 1.


Proof of Lemma 2.3. Suppose that e ∈/ G ∪ eqrd+1(G). Let Π be an r-cut in G such that e ∈ ext(Π) and whose deﬁcit de in G is the smallest possible. Note that de d + 1 as we assumed that e crosses some cut with deﬁcit at most d + 1. If de = 0, then Π is a maximum r-cut of G ∪ e, so in particular e ∈/ eqrd(G ∪ e), due to Fact 2.4. Otherwise, br(G ∪ e) = br(G) and, consequently, the deﬁcit of Π in G ∪ e equals

br(G ∪ e) − |ext(Π) ∩ (G ∪ e)| = br(G) − |ext(Π) ∩ G| − 1 = de − 1 d. In particular, Π is a cut witnessing that e ∈/ eqrd(G ∪ e).

Both of our applications of Corollary 2.2 will crucially use the fact that cores are ‘stable’ under small edge perturbations. Our next lemma, and its corollaries, formalise this notion of stability.

Lemma 2.5. For every integer d 0, graph G ⊆ Kn, and edge e ∈ Kn, we have eqd+1(G) ⊆ eqd(G△e).

Proof. We prove the equivalent statement Kn \ eqd(G△e) ⊆ Kn \ eqd+1(G). Observe ﬁrst that, for every ﬁxed r-cut Π, the function4

P(Kn) ∋ H  → defH(Π) = br(H) − H ∩ ext(Π) is the diﬀerence of two nondecreasing, 1-Lipshitz functions, and thus it is also 1-Lipshitz. In particular, for every graph G and edge e ∈ Kn, we have defG(Π) defG△e(Π) + 1. 4We write P(Kn) to denote the family of all subgraphs of Kn, i.e., the powerset of Kn, which we identify here with its set of edges.

![image 24](<2024-hoshen-stability-large-cuts-random_images/imageFile24.png>)

Now, suppose that f ∈ Kn\eqd(G△e), that is, f ∈ ext(Π) for some Π with defG△e(Π) d. Since defG(Π) defG△e(Π) + 1 d + 1, we have f ∈/ eqd+1(G).

- Corollary 2.6. For every integer d 0 and graphs G,T ⊆ Kn, we have eqd+eT (G) ⊆ eqd(G△T).
- Corollary 2.7. The following holds for every integer d 0 and all graphs G,T ⊆ Kn.


(G) corerd(G△T).

If G has a (d+eT,r)-core, then G△T has a (d,r)-core and corerd+e

T

- 2.2. Distribution of edges in G(n,m). Our arguments require various estimates of the number of edges in certain subgraphs of G(n,m). Luckily, all these estimates can be easily deduced from the following lower-tail estimate for the number of edges in G(n,m) induced by subsets of its vertices.


Lemma 2.8. Suppose that G ∼ G(n,m) for some m ∈ {0,... , n2 }. Then, letting p = m/ n2 ,

P ∃U |G[U]| < |U| 2

√np e−n.

p − 2|U|

![image 25](<2024-hoshen-stability-large-cuts-random_images/imageFile25.png>)

Proof. We may clearly assume that m 1. Fix a nonempty U ⊆ n . Standard estimates on lower tail probabilities of the binomial distribution yield5

4|U|2np p|U|2

P |G[U]| < |U| 2

√np ≤ exp −

= e−4n. The union bound over all U ﬁnishes the proof.

p − 2|U|

![image 26](<2024-hoshen-stability-large-cuts-random_images/imageFile26.png>)

![image 27](<2024-hoshen-stability-large-cuts-random_images/imageFile27.png>)

In fact, we will only use the following immediate corollary of Lemma 2.8.

Corollary 2.9. Suppose that G ∼ G(n,m) for some m ∈ {0,... , n2 }. With probability at least 1 − e−n, for every partition Π of n ,

|int(Π) ∩ G| |int(Π)| · p − 2n√np.

![image 28](<2024-hoshen-stability-large-cuts-random_images/imageFile28.png>)

One important consequence of Corollary 2.9 is that every cut of G(n,m) with small deﬁcit must be balanced.

Lemma 2.10. Suppose that G ∼ G(n,m) for some m ∈ {0,... , n2 }. With probability at least 1 − e−n, each part of every r-cut of G with deﬁcit at most d has at most n/r +

4max{(d/m)1/2,(n/m)1/4} · n vertices.

The proof of Lemma 2.10 uses the following straightforward estimate on the number of edges that cross a non-balanced cut. Fact 2.11. If Π = (A1,... ,Ar) is an r-cut in Kn with maxi |Ai| = n/r + εn for some ε 0, then

rε2 r − 1 ·

1 r −

n 2

n 2

|ext(Π)| 1 −

.

+

![image 29](<2024-hoshen-stability-large-cuts-random_images/imageFile29.png>)

![image 30](<2024-hoshen-stability-large-cuts-random_images/imageFile30.png>)

![image 31](<2024-hoshen-stability-large-cuts-random_images/imageFile31.png>)

![image 32](<2024-hoshen-stability-large-cuts-random_images/imageFile32.png>)

5See [13, Section 6], which argues that the hypergeometric distribution is at least as concentrated as the binomial distribution with the same parameters.

Proof. We may clearly assume that |A1| = maxi |Ai| = n/r + εn. By convexity of x  → x2 := x(x2−1),

![image 33](<2024-hoshen-stability-large-cuts-random_images/imageFile33.png>)

r

|Ai| 2

n/r − εn/(r − 1) 2

n 2 −

n 2 −

n/r + εn 2 − (r − 1) ·

|ext(Π)| =

.

i=1

Further, as for all nonnegative λ1,... ,λr with λ1 + ··· + λr = 1, we have

r

r

(1 − λi)λin 2

n 2

n 2 −

λin 2

λ2i

,

=

![image 34](<2024-hoshen-stability-large-cuts-random_images/imageFile34.png>)

![image 35](<2024-hoshen-stability-large-cuts-random_images/imageFile35.png>)

i=1

i=1

we may conclude that

2

1 r

1 r −

ε r − 1

|ext(Π)| 1 −

− (r − 1)

+ ε

![image 36](<2024-hoshen-stability-large-cuts-random_images/imageFile36.png>)

![image 37](<2024-hoshen-stability-large-cuts-random_images/imageFile37.png>)

![image 38](<2024-hoshen-stability-large-cuts-random_images/imageFile38.png>)

rε2 r − 1 ·

1 r −

n 2

n 2

= 1 −

, as claimed.

+

![image 39](<2024-hoshen-stability-large-cuts-random_images/imageFile39.png>)

![image 40](<2024-hoshen-stability-large-cuts-random_images/imageFile40.png>)

![image 41](<2024-hoshen-stability-large-cuts-random_images/imageFile41.png>)

2

·

n 2

n 2

+

![image 42](<2024-hoshen-stability-large-cuts-random_images/imageFile42.png>)

Proof of Lemma 2.10. Assume the assertion of Corollary 2.9, which holds with probability at least 1 −e−n. Let Π = (A1,... ,Ar) be an r-cut with deﬁcit at most d and let ε be the number satisfying maxi |Ai| = n/r + εn. On the one hand, since every graph G with m edges satisﬁes br(G) r−r1 · m (to see this, consider a uniformly random r-cut), the size of Π in G is at least r−r1 · m − d. On the other hand, by the assumed assertion of Corollary 2.9 and Fact 2.11, letting p := m/ n2 ,

![image 43](<2024-hoshen-stability-large-cuts-random_images/imageFile43.png>)

![image 44](<2024-hoshen-stability-large-cuts-random_images/imageFile44.png>)

rε2 r − 1 · m +

r − 1 r −

+ 2n√np. This yields

|ext(Π) ∩ G| |ext(Π)| · p + 2n√np

np 2

![image 45](<2024-hoshen-stability-large-cuts-random_images/imageFile45.png>)

![image 46](<2024-hoshen-stability-large-cuts-random_images/imageFile46.png>)

![image 47](<2024-hoshen-stability-large-cuts-random_images/imageFile47.png>)

![image 48](<2024-hoshen-stability-large-cuts-random_images/imageFile48.png>)

![image 49](<2024-hoshen-stability-large-cuts-random_images/imageFile49.png>)

5n√np 2

rε2m r − 1

d + 4√nm, which means that

+ 2n√np d +

np 2

![image 50](<2024-hoshen-stability-large-cuts-random_images/imageFile50.png>)

![image 51](<2024-hoshen-stability-large-cuts-random_images/imageFile51.png>)

d +

![image 52](<2024-hoshen-stability-large-cuts-random_images/imageFile52.png>)

![image 53](<2024-hoshen-stability-large-cuts-random_images/imageFile53.png>)

![image 54](<2024-hoshen-stability-large-cuts-random_images/imageFile54.png>)

![image 55](<2024-hoshen-stability-large-cuts-random_images/imageFile55.png>)

n r

|Ai| −

max

![image 56](<2024-hoshen-stability-large-cuts-random_images/imageFile56.png>)

i

= εn 2max

![image 57](<2024-hoshen-stability-large-cuts-random_images/imageFile57.png>)

d m

,

![image 58](<2024-hoshen-stability-large-cuts-random_images/imageFile58.png>)

16n m

![image 59](<2024-hoshen-stability-large-cuts-random_images/imageFile59.png>)

1/4

· n,

as desired.

- 2.3. Proof of Theorem 2.1. It will be convenient to deﬁne, for a graph G on n , eqr−1(G) := int(ΠG),


where ΠG is some (canonically chosen) maximum r-cut in G. By convexity of x  → x2 ,

n2 2r −

n/r 2

n 2

eqr−1(G) r ·

. (3)

=

![image 60](<2024-hoshen-stability-large-cuts-random_images/imageFile60.png>)

![image 61](<2024-hoshen-stability-large-cuts-random_images/imageFile61.png>)

The following lemma lies at the heart of the proof of Theorem 2.1. Throughout this section, we denote N := n2 .

Lemma 2.12. Let G1 ∼ G(n,m) and G2 ∼ G(n,m + 1) for some m ∈ {0,... ,N − 1}. For every r 2 and all d −1,

N − m m + 1 · E|eqrd(G2) ∩ G2| .

E eqrd+1(G1) \ G1

![image 62](<2024-hoshen-stability-large-cuts-random_images/imageFile62.png>)

Proof. We may clearly couple G1 and G2 so that G2 = G1 ∪ e and e is a uniformly random edge of each of Kn \ G1 and G2. Deﬁne, for every d −1,

qd := P e ∈/ eqrd(G1) and observe that

qd · (N − m) = E|(Kn \ G1) \ eqrd(G1)| = N − m − E|eqrd(G1) \ G1|. (4) On the other hand, Lemma 2.3 implies that, for every d 0,

qd+1 · (m + 1) P e ∈/ eqrd(G2) · (m + 1) = m + 1 − E|eqrd(G2) ∩ G2|. (5) This inequality remains valid also when d = −1 since, by Fact 2.4,

q0 · (m + 1) = E|critr(G2)| E[br(G2)] = m + 1 − E eqr−1(G2) ∩ G2 . The claimed inequality follows by combining (4), with d replaced by d + 1, and (5).

We now use Corollary 2.9 to derive the following cleaner statement.

Corollary 2.13. Let G1 ∼ G(n,m) and G2 ∼ G(n,m+1) for some m ∈ {0,... ,N −1}. For every r 2, all d −1, and all suﬃciently large n,

2n9/2 √m + 1 · (N − m)

E eqrd+1(G1) E|eqrd(G2)| −

.

![image 63](<2024-hoshen-stability-large-cuts-random_images/imageFile63.png>)

![image 64](<2024-hoshen-stability-large-cuts-random_images/imageFile64.png>)

Proof. Since, for all d, r, and G, the graph eqrd(G) is a union of cliques, Corollary 2.9 gives, letting p1 := m/N and p2 := (m + 1)/N,

E|eqrd(G2) ∩ G2| E|eqrd(G2)| · p2 − 2n√np2 − n2e−n E|eqrd(G2)| · p2 − 3n√np2, where the last inequality holds for all suﬃciently large n, and, similarly,

![image 65](<2024-hoshen-stability-large-cuts-random_images/imageFile65.png>)

![image 66](<2024-hoshen-stability-large-cuts-random_images/imageFile66.png>)

E eqrd+1(G1) \ G1 = E eqrd+1(G1) − E eqrd+1(G1) ∩ G1

E eqrd+1(G1) · (1 − p1) + 3n√np1. Consequently, Lemma 2.12 yields

![image 67](<2024-hoshen-stability-large-cuts-random_images/imageFile67.png>)

E eqrd+1(G1)

1 1 − p1 · E eqrd+1(G1) \ G1 − 3n√np1 1 1 − p1 ·

![image 68](<2024-hoshen-stability-large-cuts-random_images/imageFile68.png>)

![image 69](<2024-hoshen-stability-large-cuts-random_images/imageFile69.png>)

3n√np1 1 − p1 p2

N − m m + 1 · E|eqrd(G2) ∩ G2| −

![image 70](<2024-hoshen-stability-large-cuts-random_images/imageFile70.png>)

![image 71](<2024-hoshen-stability-large-cuts-random_images/imageFile71.png>)

![image 72](<2024-hoshen-stability-large-cuts-random_images/imageFile72.png>)

![image 73](<2024-hoshen-stability-large-cuts-random_images/imageFile73.png>)

3n√np2 p2 −

3n√np1 1 − p1

N − m m + 1 · E|eqrd(G2)| −

![image 74](<2024-hoshen-stability-large-cuts-random_images/imageFile74.png>)

![image 75](<2024-hoshen-stability-large-cuts-random_images/imageFile75.png>)

1 − p1 ·

![image 76](<2024-hoshen-stability-large-cuts-random_images/imageFile76.png>)

![image 77](<2024-hoshen-stability-large-cuts-random_images/imageFile77.png>)

![image 78](<2024-hoshen-stability-large-cuts-random_images/imageFile78.png>)

![image 79](<2024-hoshen-stability-large-cuts-random_images/imageFile79.png>)

√p1 1 − p1

1 √p2

![image 80](<2024-hoshen-stability-large-cuts-random_images/imageFile80.png>)

= E|eqrd(G2)| − 3n3/2 ·

+

.

![image 81](<2024-hoshen-stability-large-cuts-random_images/imageFile81.png>)

![image 82](<2024-hoshen-stability-large-cuts-random_images/imageFile82.png>)

![image 83](<2024-hoshen-stability-large-cuts-random_images/imageFile83.png>)

The claimed inequality follows as

√

√p1 1 − p1

√p2 1 − p1

![image 84](<2024-hoshen-stability-large-cuts-random_images/imageFile84.png>)

1 − p1 + p2 √p2 · (1 − p1)

N · (N + 1) √m + 1 · (N − m)

1 √p2

1 √p2

![image 85](<2024-hoshen-stability-large-cuts-random_images/imageFile85.png>)

![image 86](<2024-hoshen-stability-large-cuts-random_images/imageFile86.png>)

=

+

+

=

.

![image 87](<2024-hoshen-stability-large-cuts-random_images/imageFile87.png>)

![image 88](<2024-hoshen-stability-large-cuts-random_images/imageFile88.png>)

![image 89](<2024-hoshen-stability-large-cuts-random_images/imageFile89.png>)

![image 90](<2024-hoshen-stability-large-cuts-random_images/imageFile90.png>)

![image 91](<2024-hoshen-stability-large-cuts-random_images/imageFile91.png>)

![image 92](<2024-hoshen-stability-large-cuts-random_images/imageFile92.png>)

![image 93](<2024-hoshen-stability-large-cuts-random_images/imageFile93.png>)

![image 94](<2024-hoshen-stability-large-cuts-random_images/imageFile94.png>)

![image 95](<2024-hoshen-stability-large-cuts-random_images/imageFile95.png>)

![image 96](<2024-hoshen-stability-large-cuts-random_images/imageFile96.png>)

We conclude this subsection with the proof of Theorem 2.1, which now amounts to little more than summing the inequalities from the assertion of Corollary 2.13 over a range of d.

Proof of Theorem 2.1. Let δ,ε ∈ (0,1) be arbitrary and suppose that nonnegative integers d,m,n,r satisfy the assumptions of the theorem. Note that we may assume that

![image 97](<2024-hoshen-stability-large-cuts-random_images/imageFile97.png>)

- d m/n and that n is suﬃciently large, as otherwise the asserted upper bound on the probability is larger than one. Let G ∼ G(n,m) and let G′ ∼ G(n,m + d + 1). It follows from Corollary 2.13 that


d

2n9/2 √m + i + 1 · (N − m − i)

E|eqrd(G)| − E eqr−1(G′) −

![image 98](<2024-hoshen-stability-large-cuts-random_images/imageFile98.png>)

![image 99](<2024-hoshen-stability-large-cuts-random_images/imageFile99.png>)

i=0

2(d + 1)n9/2 √m · (δN − d) −

5(d + 1)n5/2 δ√m

−

. In particular, due to (3),

![image 100](<2024-hoshen-stability-large-cuts-random_images/imageFile100.png>)

![image 101](<2024-hoshen-stability-large-cuts-random_images/imageFile101.png>)

![image 102](<2024-hoshen-stability-large-cuts-random_images/imageFile102.png>)

![image 103](<2024-hoshen-stability-large-cuts-random_images/imageFile103.png>)

E|eqrd(G)|

5(d + 1)n5/2 δ√m

n 2 −

N r −

. (6)

![image 104](<2024-hoshen-stability-large-cuts-random_images/imageFile104.png>)

![image 105](<2024-hoshen-stability-large-cuts-random_images/imageFile105.png>)

![image 106](<2024-hoshen-stability-large-cuts-random_images/imageFile106.png>)

![image 107](<2024-hoshen-stability-large-cuts-random_images/imageFile107.png>)

On the other hand, since (d/m)1/2 (mn)−1/4 (n/m)1/4, Lemma 2.10 implies that, with probability at least 1 − e−n, each part of every r-cut with deﬁcit at most d has at most n/r + 4(n/m)1/4 · n vertices. Thus, letting a := 4(n/m)1/4 · n, we have

ra2 2

N r

a 2

n/r + a 2

n/r 2

n r

|eqrd(G)| r ·

r ·

+ r ·

a

+

+ na +

![image 108](<2024-hoshen-stability-large-cuts-random_images/imageFile108.png>)

![image 109](<2024-hoshen-stability-large-cuts-random_images/imageFile109.png>)

![image 110](<2024-hoshen-stability-large-cuts-random_images/imageFile110.png>)

![image 111](<2024-hoshen-stability-large-cuts-random_images/imageFile111.png>)

N r

+ 4(n/m)1/4 · n2 + 8r(n/m)1/2 · n2. with probability at least 1 − e−n. Finally, let

=

![image 112](<2024-hoshen-stability-large-cuts-random_images/imageFile112.png>)

P := P G is not (d,r,ε)-rigid = P eqrd(G) (1 − ε)N/r . We may conclude that, for some absolute constant C,

(1 − ε)N r

E|eqrd(G)| P ·

+ (1 − P) ·

![image 113](<2024-hoshen-stability-large-cuts-random_images/imageFile113.png>)

![image 114](<2024-hoshen-stability-large-cuts-random_images/imageFile114.png>)

1 r

n m

+ C 4

+ Cr

![image 115](<2024-hoshen-stability-large-cuts-random_images/imageFile115.png>)

![image 116](<2024-hoshen-stability-large-cuts-random_images/imageFile116.png>)

![image 117](<2024-hoshen-stability-large-cuts-random_images/imageFile117.png>)

n m · N + e−n · N. (7)

![image 118](<2024-hoshen-stability-large-cuts-random_images/imageFile118.png>)

Combining (6) and (7), we obtain

P

r ε ·

![image 119](<2024-hoshen-stability-large-cuts-random_images/imageFile119.png>)

5(d + 1)n5/2 δ√mN

+ C 4

![image 120](<2024-hoshen-stability-large-cuts-random_images/imageFile120.png>)

![image 121](<2024-hoshen-stability-large-cuts-random_images/imageFile121.png>)

![image 122](<2024-hoshen-stability-large-cuts-random_images/imageFile122.png>)

n m

+ Cr

![image 123](<2024-hoshen-stability-large-cuts-random_images/imageFile123.png>)

![image 124](<2024-hoshen-stability-large-cuts-random_images/imageFile124.png>)

n m

![image 125](<2024-hoshen-stability-large-cuts-random_images/imageFile125.png>)

,

provided that C is suﬃciently large, as claimed.

- 2.4. Derivation of Corollary 2.2. The following key lemma, which is a variant of [6, Proposition 10.1] (see also [14, Proposition 7.2]), implies that every graph that is


suﬃciently rigid must contain a core, provided that each of its cuts with small deﬁcit is balanced.

- Lemma 2.14. Suppose that r 2 and α ∈ (0,1/(r2 + r)) and let d 0 be an arbitrary integer. If an n-vertex graph G is (d,r,α/r)-rigid and each part of every r-cut of G with deﬁcit at most d has size at most (1 + α)n/r, then the r largest (d,r)-components of G have size at least n/r − αn each.

Proof. Suppose that each part of every r-cut of G with deﬁcit at most d has size at most (1 + α)n/r. If only at most r − 1 largest (d,r)-components of G had size at least n/r − αn, then it would follow from convexity of x  → x2 that

|eqrd(G)| (r − 1)

(1 + α)n/r 2

+

n/r − αn 2

+

αn/r 2 (r − 1) (1 + α)/r 2 + (1/r − α)2 + (α/r)2

n 2

=

1 − 2α/r + (r + 1)α2 r

![image 126](<2024-hoshen-stability-large-cuts-random_images/imageFile126.png>)

n 2

<

1 − α/r r

![image 127](<2024-hoshen-stability-large-cuts-random_images/imageFile127.png>)

n 2

, which means that G would not be (d,r,α/r)-rigid.

Proof of Corollary 2.2. Let α,δ ∈ (0,1) be arbitrary and suppose that nonnegative integers d,m,n,r satisfy the assumptions of the corollary. Note that we may assume that d m/n and 4r2/α < 4 m/n, as otherwise the asserted upper bound on the probability is larger than one. Since these assumptions imply that

![image 128](<2024-hoshen-stability-large-cuts-random_images/imageFile128.png>)

![image 129](<2024-hoshen-stability-large-cuts-random_images/imageFile129.png>)

αn r

![image 130](<2024-hoshen-stability-large-cuts-random_images/imageFile130.png>)

> 4 · 4

![image 131](<2024-hoshen-stability-large-cuts-random_images/imageFile131.png>)

n m · n = 4 · max

![image 132](<2024-hoshen-stability-large-cuts-random_images/imageFile132.png>)

![image 133](<2024-hoshen-stability-large-cuts-random_images/imageFile133.png>)

d m

![image 134](<2024-hoshen-stability-large-cuts-random_images/imageFile134.png>)

, 4

![image 135](<2024-hoshen-stability-large-cuts-random_images/imageFile135.png>)

n m · n,

![image 136](<2024-hoshen-stability-large-cuts-random_images/imageFile136.png>)

we may invoke Lemma 2.10 to conclude that, with probability 1 − e−n, each part of every r-cut in G(n,m) with deﬁcit at most d has no more than (1 + α)n/r vertices. Consequently, by Lemma 2.14,

P G(n,m) ∈/ CORErd(α) P G(n,m) is not (d,r,α/r)-rigid + e−n. The assertion of the corollary now follows immediately from Theorem 2.1.

2.5. Proof of Theorem 1.1. Since our assumption that pn ≫ 1 implies that whp Gn,p has (1 + o(1)) n2 p edges, the ﬁrst assertion of the theorem is a straightforward consequence of Corollary 2.2. It thus remains to prove the second assertion. The following observation is at the heart of the matter. Given a graph G, a vertex v ∈ V (G), and a set W ⊆ V (G), we write degG(v,W) to denote the number of neighbours of v in W.

- Lemma 2.15. Suppose that some largest r-cut Π = {V1,... ,Vr} in a graph G and a vertex v ∈ V1 satisfy


r − 1 r · d for some nonnegative integer d. Then v is not (d,r)-equivalent to any other vertex of G.

degG v r −

degG(v,V1)

![image 137](<2024-hoshen-stability-large-cuts-random_images/imageFile137.png>)

![image 138](<2024-hoshen-stability-large-cuts-random_images/imageFile138.png>)

Proof. For each i ∈ {2,... ,r}, denote by Πi the r-cut obtained from Π by moving the vertex v from V1 to Vi and observe that

|ext(Πi) ∩ G| = |ext(Π) ∩ G| + degG(v,V1) − degG(v,Vi)

= br(G) + degG(v,V1) − degG(v,Vi).

Consequently, writing defG(Πi) := br(G) − |ext(Πi) ∩ G| for the deﬁcit of Πi in G, we have

r

r

(degG(v,Vi) − degG(v,V1)) = degG v − r degG(v,V1) (r − 1)d.

defG(Πi) =

i=2

i=2

In particular, there must be some i ∈ {2,... ,r} for which defG(Πi) d. The assertion now follows as no vertex u = v shares with v the same part of both Π and Πi.

Suppose now that G ∼ Gn,p. Let Π be an arbitrary largest r-cut in G and deﬁne, for each nonnegative integer d,

r − 1 r · d .

degG v r −

Xd := v ∈ V (G) : v ∈ V ∈ Π and degG(v,V ) <

![image 139](<2024-hoshen-stability-large-cuts-random_images/imageFile139.png>)

![image 140](<2024-hoshen-stability-large-cuts-random_images/imageFile140.png>)

Since Lemma 2.15 implies that eqrd(G) ⊆ X2d , it suﬃces to show that whp |Xd| < αn when d C√pn for large enough C.

![image 141](<2024-hoshen-stability-large-cuts-random_images/imageFile141.png>)

The assumption that Π is a largest r-cut in G implies that degG(v,V ) (degG v)/r for each v ∈ V ∈ Π and therefore

r − 1 r · (2|G| + |Xd| · d)

(degG v − degG(v,V )) = 2|ext(Π) ∩ G| .

![image 142](<2024-hoshen-stability-large-cuts-random_images/imageFile142.png>)

v∈V ∈Π

This yields

2r · |ext(Π) ∩ G| − 2(r − 1) · |G| (r − 1) · d

2|G| − 2r · |int(Π) ∩ G| (r − 1) · d

|Xd|

=

.

![image 143](<2024-hoshen-stability-large-cuts-random_images/imageFile143.png>)

![image 144](<2024-hoshen-stability-large-cuts-random_images/imageFile144.png>)

In particular, it follows from Corollary 2.9 that, with probability at least 1 − e−n,

![image 145](<2024-hoshen-stability-large-cuts-random_images/imageFile145.png>)

2|G| − 2r · |int(Π)| · |G|/ n2 + 4r · n n|G|/ n2 (r − 1) · d

|Xd|

.

![image 146](<2024-hoshen-stability-large-cuts-random_images/imageFile146.png>)

Finally, since r · |int(Π)| r2 · n/r2 n2 − rn2 , by convexity of x  → x2 , and since whp we have |G| 2 n2 p and

![image 147](<2024-hoshen-stability-large-cuts-random_images/imageFile147.png>)

2rnp + 6rn√np (r − 1) · d

7rn√np (r − 1) · d

![image 148](<2024-hoshen-stability-large-cuts-random_images/imageFile148.png>)

![image 149](<2024-hoshen-stability-large-cuts-random_images/imageFile149.png>)

|Xd|

<

.

![image 150](<2024-hoshen-stability-large-cuts-random_images/imageFile150.png>)

![image 151](<2024-hoshen-stability-large-cuts-random_images/imageFile151.png>)

In particular, if d 14√np/α, then |Xd| < αn, as desired.

![image 152](<2024-hoshen-stability-large-cuts-random_images/imageFile152.png>)

- 2.6. Non-uniqueness of maximum cuts and vertices outside of the core. In this subsection, we present supporting evidence for our suspicion that whp G(n,m) does not have a unique maximum cut for all m satisfying n ≪ m N − Ω(N).6 By [3, Lemma 14], with probability very close to one, the maximum size of an r-cut in G(n,m) is r−r1 · m + Θ(√mn). It is reasonable to believe that the expectation of this random 6This is vacuously true when m n log n/2 − ω(n), since then whp G(n, m) has isolated vertices.


![image 153](<2024-hoshen-stability-large-cuts-random_images/imageFile153.png>)

![image 154](<2024-hoshen-stability-large-cuts-random_images/imageFile154.png>)

![image 155](<2024-hoshen-stability-large-cuts-random_images/imageFile155.png>)

variable grows ‘smoothly’ with m in the sense that E[br(G(n,m + 1)) − br(G(n,m))] = r−1

![image 156](<2024-hoshen-stability-large-cuts-random_images/imageFile156.png>)

r + Θ( n/m). If this estimate held conditionally on G(n,m), under the natural coupling for which G(n,m) ⊆ G(n,m + 1), that is, if

![image 157](<2024-hoshen-stability-large-cuts-random_images/imageFile157.png>)

r − 1 r

![image 158](<2024-hoshen-stability-large-cuts-random_images/imageFile158.png>)

∂br := E[br(G(n,m + 1)) | G(n,m)] − br(G(n,m))

+ Θ( n/m), (8)

![image 159](<2024-hoshen-stability-large-cuts-random_images/imageFile159.png>)

then G(n,m) would not have a unique maximum r-cut. Indeed, it follows from Fact 2.4 that, if Π is the unique maximum r-cut of G(n,m), then

∂br = |ext(Π) \ G(n,m)| n 2 − m

r − 1 r

.

![image 160](<2024-hoshen-stability-large-cuts-random_images/imageFile160.png>)

![image 161](<2024-hoshen-stability-large-cuts-random_images/imageFile161.png>)

Unfortunately, we do not even know how to prove that (8) holds with probability Ω(1). Instead, we show that the expected number of vertices that lie outside of the core is large in either G(n,m) or in G(n,m + 1), and thus also in Gn,p.

Given a graph G and an integer r 2, denote by Xr(G) the set of vertices not belonging to the (0,r)-core of G (so that Xr(G) = V (G) if G does not have a (0,r)core). Further, set xr(G) := |Xr(G)|. By the deﬁnition of the (0,r)-core, xr(G) = 0 if and only if G has a unique largest r-cut whose each part has more than |V (G)|/(r + 1) vertices.7 We show that our upper bound on E[xr(Gn,p)] provided by (6) is tight up to a constant factor.

Proposition 2.16. Let r 2 be an integer and let δ be a positive constant. If 1/n ≪ p 1 − δ, then

![image 162](<2024-hoshen-stability-large-cuts-random_images/imageFile162.png>)

E[xr(Gn,p)] = Ω n/p .

We postpone the proof of Proposition 2.16 to Appendix in order to avoid overloading this section with extra technical details since its proof method resembles the proof of Corollary 2.13.

3. Neighbourhood in maximum cuts

In this section, we prove Theorem 1.2. It will be convenient to ﬁrst introduce some notation. Given a graph G, a vertex v ∈ V (G), and a set of vertices S ⊆ V (G), we denote by NG(v) and NG(v;S) the sets of neighbours of v in V (G) and in S, respectively. Further, given a set W ⊆ V (G), we denote by NG(W) and by NG(W;S) the set of common neighbours of W in V (G) and in S, respectively; note that usually NG(W) denotes the union of NG(v) over v ∈ W, rather than their intersection. That is,

NG(W) :=

NG(v) and NG(W;S) :=

NG(v;S).

v∈W

v∈W

Finally, we will denote by Hyp(N,s,t) the size of the intersection of a random t-element subset of N with the set s (this is a hypergeometric random variable).

![image 163](<2024-hoshen-stability-large-cuts-random_images/imageFile163.png>)

7Lemma 2.10 implies that, for all m ≫ n, with probability at least 1−e−n, each part of every maximum r-cut of G(n, m) has n/r ± o(n) vertices.

Let us ﬁx integers k 1, r 2 and a small ε > 0. Further, assume that p satisﬁes

1/k

(log n)2 n for a suﬃciently large C > 0. Our aim is to prove that whp every maximum r-cut (V1,... ,Vr) of G ∼ Gn,p and every k-element W ⊆ V (G) satisfy

log n n

p 1 − ε and p ≫

C

![image 164](<2024-hoshen-stability-large-cuts-random_images/imageFile164.png>)

![image 165](<2024-hoshen-stability-large-cuts-random_images/imageFile165.png>)

1 r ± ε npk for all i ∈ r .

|NG(W;Vi)| =

![image 166](<2024-hoshen-stability-large-cuts-random_images/imageFile166.png>)

Denote by B the event that there exists a set W of k vertices and a maximum r-cut (V1,... ,Vr) of G such that, for some i ∈ r ,

1 − ε

|NG(W;Vi)|

r · |NG(W)|. Moreover, for a k-set W ⊆ V (G), denote by YW the event that |NG(W)| = (1 ± ε2)npk and set Y := W YW. Since on the event Bc ∩ Y, we have

![image 167](<2024-hoshen-stability-large-cuts-random_images/imageFile167.png>)

1 − ε r · 1 − ε2 npk |NG(W;Vi)| |NG(W)| −

1 r − ε npk

|NG(W;Vj)|

![image 168](<2024-hoshen-stability-large-cuts-random_images/imageFile168.png>)

![image 169](<2024-hoshen-stability-large-cuts-random_images/imageFile169.png>)

j =i

1 − ε r

1 r

1 + ε2 npk − (r − 1) ·

+ ε npk, in order to complete the proof of Theorem 1.2, it is suﬃcient to prove that

npk

![image 170](<2024-hoshen-stability-large-cuts-random_images/imageFile170.png>)

![image 171](<2024-hoshen-stability-large-cuts-random_images/imageFile171.png>)

P(Yc) + P(B) = o(1). (9)

By the Chernoﬀ bound and our assumption on p and the choice of C, for every kelement W ⊆ V (G),

P |NG(W)| = (1 ± ε2)npk exp −ε4npk/5 n−2k; the estimate P(Yc) = o(1) follows from a straightforward union bound over all W.

We now turn to bounding P(B). Let α be a small positive constant. Recall that G ∈ CORErd(α) means that G has a (d,r)-core whose each component has at least n/r − αn vertices and that corerd(G) denotes the set of the r components of the (d,r)core of G. (If G ∈/ CORErd(α), then we set corerd(G) = ∅.) For a k-set W ⊆ V (G), denote by AW the event that

1 − ε

r · |NG(W)| for some S ∈ corer0(G) (10) and let A := W AW. Set t := ⌈

|NG(W;S)|

![image 172](<2024-hoshen-stability-large-cuts-random_images/imageFile172.png>)

√

![image 173](<2024-hoshen-stability-large-cuts-random_images/imageFile173.png>)

C log n⌉ and let d := kt. The key observation is that, if G has a (0,r)-core and B holds, then A holds as well. Therefore,

P(B) (G ∈/ COREr2d(α)) + P(G ∈ COREr2d(α) ∧ A). The ﬁrst summand above is o(1), by Corollary 2.2, whereas

P(G ∈ COREr2d(α) ∧ A) P(Yc) +

W

P(G ∈ COREr2d(α) ∧ AW | YW). (11)

Since we have already shown that P(Yc) = o(1), it suﬃces to prove that each term in the sum is much smaller than n−k.

To this end, ﬁx a k-element set W and, assuming that YW holds, let R be a uniformly chosen t-element subset of NG(W) (clearly, YW implies that |NG(W)| t). Denote by AW,t the event that

1 − ε/2

r · t for some S ∈ corer0(G) (12) and observe that

|R ∩ S|

![image 174](<2024-hoshen-stability-large-cuts-random_images/imageFile174.png>)

P(G ∈ COREr2d(α) ∧ AW,t | YW) P(G ∈ COREr2d(α) ∧ AW | YW) · P(AW,t | G ∈ COREr2d(α) ∧ AW ∧ YW).

(13)

If YW holds (so that R is deﬁned) and G has a (0,r)-core, then, for every S ∈ corer0(G), the cardinality |R ∩ S| is distributed like Hyp(|NG(W)|,|NG(W;S)|,t). In particular, it follows from standard tail bounds for the hypergeometric distribution [13, Section 6] that whp (in the choice of R) (10) implies (12). Thus, the second factor in the right-hand side of (13) approaches 1, implying

P(G ∈ COREr2d(α) ∧ AW | YW) (1 + o(1)) · P(G ∈ COREr2d(α) ∧ AW,t | YW). (14) Now, if the distribution of R, conditioned on corer0(G), was the uniform distribution on t-element subsets of V \ W, then, for every S ∈ corer0(G), the cardinality |R ∩ S| would again have hypergeometric distribution, implying that AW,t has exponentially small probability. We will show something marginally weaker: The distribution of R is approximately uniform after we condition on the graph G∗ that is obtained from G by resampling all edges between W and R. Since G∗ satisﬁes corerd(G∗) corer0(G), by Corollary 2.7, this will allow us to prove the following estimate.

Claim 3.1. There exists a c = c(r,α,ε) > 0 such that, for every k-element set W, P(G ∈ COREr2d(α) ∧ AW,t | YW) e−ct. Given Claim 3.1, it is now easy to ﬁnish the proof of Theorem 1.2. Indeed, by (14), P(G ∈ COREr2d(α) ∧ AW | YW) (1 + o(1)) · e−ct ≪ n−k due to our choice of t. Substituting this bound into (11) completes the proof.

Proof of Claim 3.1. Fix some k-element set of vertices W, assume that YW holds, and let G∗ be the graph obtained from G by independently resampling each edge between W and R with probability p. We shall ﬁrst show that, conditioned on G∗, R is a nearlyuniformly random k-element subset of n \ W.

To see this, ﬁx some t-element R ⊆ n \ W and a graph G∗ such that G∗ = G∗ with nonzero probability. Writing G∗[W,R] for the induced bipartite subgraph of G∗ with parts W and R and [W,R] for the complete bipartite graph with parts W and R, we

have P(R = R ∧ G∗ = G∗) = P(G = G∗ ∪ [W,R]) · P(R = R | G = G∗ ∪ [W,R]) · P(G∗[W,R] = G∗[W,R] | G = G∗ ∪ [W,R] ∧ R = R)

−1

|NG∗∪[W,R](W)| t

= p|G∗∪[W,R]|(1 − p)(n2)−|G∗∪[W,R]| ·

· p|G∗[W,R]|(1 − p)|W||R|−|G∗[W,R]|

|NG∗(W)| − |NG∗(W) ∩ R| + t t

= p|G∗|+kt(1 − p)(n2)−|G∗| ·

−1

.

Since |NG∗(W)| |NG(W)| (1 + ε2)npk and

|NG∗(W)| − t |NG(W)| − 2t (1 − ε2)npk − 2t (1 − 2ε2)npk, we have, for any two t-element subsets R,R′ ⊆ n \ W,

t

|NG∗(W)|+t t

t 1 + ε2 1 − 2ε2

P(R = R | G∗ = G∗) P(R = R′ | G∗ = G∗)

|NG∗(W)| |NG∗(W)| − t

.

![image 175](<2024-hoshen-stability-large-cuts-random_images/imageFile175.png>)

![image 176](<2024-hoshen-stability-large-cuts-random_images/imageFile176.png>)

![image 177](<2024-hoshen-stability-large-cuts-random_images/imageFile177.png>)

![image 178](<2024-hoshen-stability-large-cuts-random_images/imageFile178.png>)

|NG∗(W)| t

In particular, for every X ⊆ n t \W , P(R ∈ X | G∗) |X| ·

−1

n − k t

· e4ε2t. (15)

Now, since |G△G∗| |R||W| = kt = d, Corollary 2.7 yields that G ∈ COREr2d(α) implies that G∗ ∈ CORErd(α) and that corerd(G∗) corer0(G). In particular, the event G ∈ COREr2d(α) ∧ AW,t implies the event

1 − ε/2

|R ∩ S∗|

r · t for some S∗ ∈ corerd(G∗), which we will denote by A∗W,t. To summarise, we have

![image 179](<2024-hoshen-stability-large-cuts-random_images/imageFile179.png>)

P(G ∈ COREr2d(α) ∧ AW,t | YW) P(G∗ ∈ CORErd(α) ∧ A∗W,t)

P(A∗W,t | G∗ ∈ CORErd(α)). Finally, we conclude from (15) that

P(A∗W,t | G∗ ∈ CORErd(α)) e4ε2t max

1 − ε/2 r · t

P Hyp(n − k,|S∗ \ W|,t)

![image 180](<2024-hoshen-stability-large-cuts-random_images/imageFile180.png>)

G∗∈CORErd(α)

S∗∈corerd(G∗)

1 − ε/2

e4ε2t · r · P Hyp(n − k,(1/r − α)n − k,t)

r · t e−ct, for some constant c = c(r,α,ε) > 0, provided that α ε/(4r).

![image 181](<2024-hoshen-stability-large-cuts-random_images/imageFile181.png>)

4. The threshold for Simonovits’s theorem in Gn,p

In this section, we prove Theorem 1.5. We start by setting some notational conventions. As in Section 2, given a collection Π of pairwise-disjoint sets of vertices of a graph,

we denote by int(Π) the set of pairs of vertices contained in a single set of Π and by ext(Π) the set of remaining pairs of vertices of Π. If Π is a collection of sets of vertices of Kn, we also deﬁne

ext∗(Π) := Kn \ int(Π) and note that ext∗(Π) ⊇ ext(Π) and that ext∗(Π) = ext(Π) whenever Π = Kn. Let H be a nonbipartite, edge-critical, strictly 2-balanced graph and denote r := χ(H) − 1. As in [14], we denote by H the collection of all copies of H in Kn, viewed as a hypergraph with vertex set Kn. Further, for each e ∈ Kn, let

∂eH := {K \ e : e ∈ K ∈ H} denote the copies of all proper, spanning subgraphs of H that form a copy of H together with the edge e. Finally, we write ∂eH[G′] to denote the subhypergraph of ∂eH that is induced by the subgraph G′ ⊆ Kn.

Let G ∼ Gn,p. Suppose ﬁrst that 1/n ≪ p ≪ n−1/m2(H). It follows from the deﬁnition of 2-density and Markov’s inequality that whp G contains only o(n2p) copies of H; consequently, whp G contains an H-free subgraph with (1 − o(1)) n2 p edges. On the other hand, Corollary 2.9 implies that whp the largest size of an r-cut in G is at most

|ext(Π)| · p + 3n√np = 1 −

n 2

1 r

max

+ o(1)

p. Therefore, G is whp not H-Simonovits. We may thus assume from now on that

![image 182](<2024-hoshen-stability-large-cuts-random_images/imageFile182.png>)

![image 183](<2024-hoshen-stability-large-cuts-random_images/imageFile183.png>)

Π:r-cut

εn−1/m2(H) p (θH − ε) · n−1/m2(H) · (log n)1/(eH−1) for some positive constant ε.

It is clearly suﬃcient to prove that, with high probability, for some largest r-cut Π of

- G and an edge e ∈ int(Π) ∩ G, the graph (ext(Π) ∩ G) ∪ e is H-free. We will prove a stronger statement.


Note that every largest r-cut Π of G satisﬁes

ext(Π) = Kn \ int(Π) ⊆ Kn \ int(corer0(G)) = ext∗(corer0(G)), provided that G has a (0,r)-core. The aforementioned stronger statement that implies Theorem 1.5 is that whp G has a (0,r)-core with minimum part size n/r − o(n) and there is an e ∈ int(corer0(G)) ∩ G such that ∂eH[ext∗(corer0(G)) ∩ G] is empty; note that this implies that (ext(Π) ∩ G) ∪ e is H-free for every largest r-cut Π of G. More precisely, set α := (1/log n)2 and deﬁne, for each e ∈ Kn, the event

Ye := G ∈ COREr0(α) : e ∈ int(corer0(G)) ∩ G ∧ ∂eH[ext∗(corer0(G)) ∩ G] = ∅ . Our goal is to prove that whp G ∈ Ye for some e ∈ Kn. Denoting by Z the number of

- e ∈ Kn satisfying G ∈ Ye, it will be enough to show that E[Z2] (1 + o(1)) · E[Z]2. (16)


Indeed, if (16) holds, then

E[Z]2 E[Z2]

P(G ∈ Ye for some e ∈ Kn) = P(Z = 0)

= 1 − o(1) by the Paley–Zygmund inequality.

![image 184](<2024-hoshen-stability-large-cuts-random_images/imageFile184.png>)

Proof outline. In order to establish (16), we separately prove a lower bound on E[Z] and an upper bound on E[Z2]. We obtain a lower bound on E[Z] using a delicate switching argument that (roughly speaking) goes as follows. We ﬁrst choose d ≫ log n so that whp G ∈ COREr2d(α); this is possible thanks to Corollary 2.2. Fix some e ∈ Kn and assume that e ∈ int(corer2d(G)) ∩ G. Our upper-bound assumption on p and the fact that H is strictly 2-balanced imply that whp ∂eH[G] is a matching of size O(log n), which in turn allows us to analyse the following ‘resampling’ process: Remove from G all the edges of ∂eH[G], denote the resulting graph by G∗, and consider the conditional distribution of G given G∗. The fact that ∂eH[G] is a matching with o(d) edges allows us to infer that G∗ ∈ CORErd(α) and to essentially couple the conditional distribution of ∂eH[G] given G∗ with a peH−1-random subset of ∂eH, giving

∗(corerd(G∗))]| .

P ∂eH[ext∗(corerd(G∗)) ∩ G] = ∅ | G∗ (1 − o(1)) · 1 − peH−1 |∂eH[ext

Since corerd(G∗) is a collection of r pairwise-disjoint sets of size at least n/r − αn each, we have

|∂eH[ext∗(corerd(G∗))]| (1 + O(α)) · Cop H,Kr(n/r)+ = (1 + O(α)) · πH · (n/r)vH−2. Further, since G and G∗ diﬀer in o(d) edges, we have corer0(G) corerd(G∗), by Corollary 2.7, and thus ext∗(corer0(G)) ⊆ ext∗(corerd(G∗)); consequently, since nvH−2peH−1 = O(log n) and α ≪ 1/log n,

P ∂eH[ext∗(corer0(G)) ∩ G] = ∅ | G ∈ COREr2d(α) ∧ e ∈ int(corer2d(G)) ∩ G

exp −πH · (n/r)vH−2 · peH−1 − o(1) . A lower bound on E[Z] now follows by multiplying the above inequality by the probability of the event in the conditioning and summing the result over all e ∈ Kn.

In order to prove an upper bound on E[Z2], we adapt an elegant argument of DeMarco– Kahn [6], which allows us to bound, for every pair e,f of edges of Kn, the conditional probability

P (∂eH ∪ ∂fH)[ext(corer0(G)) ∩ G] = ∅ | G ∈ COREr0(α) ∧ e,f ∈ int(corer0(G)) ∩ G

from above by the (unconditional) probability of the same event with corer0(G) replaced by a ﬁxed collection of r pairwise-disjoint sets of at least n/r−αn vertices each. The latter

probability can be easily shown, using Janson’s inequality, to be at most exp − 2πH · (n/r)vH−2·peH−1+o(1) . An upper bound on E[Z2] is then deduced in a straightforward manner by summing the above estimate over all pairs e,f.

Organisation. The remainder of this section is organised as follows. In Section 4.1, we recall the statement of Janson’s inequality, prove several useful estimates concerning the hypergraph ∂eH, and derive estimates on the moments of |int(corerd(G)) ∩ G| ·

G∈CORErd(α) from Corollary 2.2. In the remaining two sections, we prove the lower bound on E[Z] and the upper bound on E[Z2].

- 4.1. Preliminaries. Given a set V and a real p ∈ [0,1], we denote by Vp the random subset of V obtained by independently retaining each element of V with probability p. Further, given a hypergraph G with vertex set V , we deﬁne the following two quantities:


p|A∪B|,

p|A| and ∆p(G) :=

µp(G) :=

A∈G

A,B∈G A =B,A∩B =∅

where the second sum is over unordered pairs of edges; in other words, µp(G) is just the expected number of edges of G[Vp] and ∆p(G) is the expected number of pairs of distinct edges of G[Vp] that intersect. The following well-known inequality of Janson plays a key role in our proof of the upper bound on E[Z2].

Theorem 4.1 (Janson’s inequality [15]). Let G be a hypergraph on a ﬁnite vertex set V . For all p ∈ [0,1],

P(G[Vp] = ∅) exp − µp(G) + ∆p(G) .

We will now prove lower and upper bounds on the values of µp and ∆p on certain induced subhypergraphs of ∂eH and ∂eH ∪ ∂fH. We start with an estimate on the sizes of subhypergraphs of ∂eH induced by graphs that are close to a complete, balanced, r-partite graph.

- Lemma 4.2. Let α be a nonnegative real and suppose that C is a family of r pairwisedisjoint subsets of n such that |X| n/r − αn for each X ∈ C. There is a constant CH that depends only on H such that, for every e ∈ int(C),


|∂eH[ext(C)]| πH − CHα · (n/r)vH−2 − CHnvH−3, |∂eH[ext∗(C)]| πH + CHα · (n/r)vH−2.

Proof. Since ext(C) ⊇ Kr(n/r − αn) by our assumption on C, when e ∈ int(C), we have |∂eH[ext(C)]| Cop H,Kr(n/r − αn)+ πH · (n/r − αn)vH−2 − O(nvH−3), which implies the ﬁrst inequality. (The reason why we may write such explicit error term is that Cop(H,Kr(m)+) is a polynomial of degree vH − 2 in m.) Further, since8

ext∗(C) ⊆ Kr(n/r − αn) ∨ Krαn, every copy of H minus an edge in ext∗(C) that is not fully contained in Kr(n/r−αn) must have at least one vertex in Krαn. Consequently, there is a constant CH′ that depends

![image 185](<2024-hoshen-stability-large-cuts-random_images/imageFile185.png>)

8We write G1 ∨ G2 for the graph obtained from the disjoint union of G1 and G2 by adding all edges joining V (G1) and V (G2).

only on H such that, for each e ∈ int(C), |∂eH[ext∗(C)]| Cop H,Kr(n/r)+ + CH′ rαn · nvH−3 πH · (n/r)vH−2 + CH′ rαnvH−2, which implies the second inequality.

Our second lemma supplies an upper bound on ∆p(∂eH ∪ ∂fH), and thus also on ∆p(∂eH). Even though this upper bound is implicit in [14, Lemma 5.2], we include a (self-contained) proof here for completeness.

- Lemma 4.3. For every pair of distinct edges e,f ∈ Kn and all p εn−1/m2(H), ∆p(∂eH ∪ ∂fH) Cn−λ · nvH−2peH−1 2

for some positive λ = λ(H) and C = C(H,ε).

The following non-probabilistic inequality, which is [14, Lemma 4.1], encapsulates the key inequality in the proof of Lemma 4.3.

- Lemma 4.4 ([14]). Let H be a nonempty graph and suppose that p εn−1/m2(H) for some ε > 0. Then, nvH′−2peH′−1 εeH′−1 for every nonempty subgraph H′ ⊆ H. Moreover, if H is strictly 2-balanced, then there exists a λ > 0 that depends only on H such that nvH′−2peH′−1 εeH′−1nλ for every H′ ⊆ H with 1 < eH′ < eH.


Proof. Let H′ be a nonempty subgraph of H. Since the assertion of the lemma holds vacuously if eH′ = 1, we may assume that eH′ > 1. By our assumption on p,

1 m2(H)

nvH′−2peH′−1 nvH′−2 εn−

![image 186](<2024-hoshen-stability-large-cuts-random_images/imageFile186.png>)

eH′−1

H′ −1

e

= εeH′−1nvH′−2−

m2(H).

![image 187](<2024-hoshen-stability-large-cuts-random_images/imageFile187.png>)

Now, recall that the deﬁnition of m2(H) implies that vH′ − 2 m eH′−1

2(H) and that, when

![image 188](<2024-hoshen-stability-large-cuts-random_images/imageFile188.png>)

- H is strictly 2-balanced, this inequality is strict unless H′ = H. Thus, the exponent of n is nonnegative and it is positive if H is strictly 2-balanced and 1 < eH′ < eH. Proof of Lemma 4.3. Observe ﬁrst that


∆p(∂eH ∪ ∂fH) ∆p(∂eH) + ∆p(∂fH) + ∆p(∂eH,∂fH), where

pe(K∪K′).

∆p(∂eH,∂fH) :=

K∈∂eH K′∈∂fH K∩K′ =∅

Now, for some positive λ = λ(H), C′ = C′(H), and C = C(H,ε) 2∆p(∂eH) =

pe(K∪K′) =

p2eH−eJ−1

J⊆H 2 eJ<eH

K∈∂eH K′∈∂eH\{K} K∩K′ =∅

K∈∂eH K′∈∂eH\{K} (K∩K′)∪e∼=J

n2p nvJpeJ

· nvH−2peH−1 2

n2vH−vJ−2p2eH−eJ−1 = C′

C′

![image 189](<2024-hoshen-stability-large-cuts-random_images/imageFile189.png>)

J⊆H 2 eJ<eH

J⊆H 2 eJ<eH

Cn−λ · nvH−2peH−1 2 ,

where the last inequality follows from Lemma 4.4; this estimate clearly remains true when we replace e with f. Similarly, for some C′ = C′(H) and C = C(H,ε),

p2eH−eJ−2

∆p(∂eH,∂fH) =

K∈∂eH K′∈∂fH\{K} K∩K′∼=J

J⊆H 1 eJ<eH−1

n|e∩f| nvJpeJ

C np · nvH−2peH−1 2 ,

· nvH−2peH−1 2

C′

![image 190](<2024-hoshen-stability-large-cuts-random_images/imageFile190.png>)

![image 191](<2024-hoshen-stability-large-cuts-random_images/imageFile191.png>)

J⊆H 1 eJ<eH

where the last inequality again follows from Lemma 4.4. Since np εn1−1/m2(H) and m2(H) > 1, the claimed inequality follows.

- Lemma 4.5. Suppose that α,p ∈ (0,1/2) and a nonnegative integer d satisfy α ≪ 1 and pn ≫ max α−4,(d/α)2 .

Then, for all ﬁxed k 0 and r 2, the random graph G ∼ Gn,p satisﬁes

E |int(corerd(G)) ∩ G|k · G∈COREr

d(α) = (1 + o(1)) ·

n2p 2r

![image 192](<2024-hoshen-stability-large-cuts-random_images/imageFile192.png>)

k

.

Proof. Set m := n2 p and note that our assumption that np ≫ 1 guarantees that whp |G| ∈ [m/2,3m/2]. In particular, the assumed asymptotic relations between α, p, and

d allow us to conclude from Corollary 2.2 that whp G ∈ CORErd(α). Since for every G ∈ CORErd(α), the graph corerd(G) is a disjoint union of r complete graphs of order at least n/r − αn each, we have

|int(corerd(G))| =

n2 2r ± O(αn2)

![image 193](<2024-hoshen-stability-large-cuts-random_images/imageFile193.png>)

and further, by the Chernoﬀ bound and the union bound over the at most (r + 1)n possible graphs corerd(G),

P ∀G ∈ CORErd(α) |int(corerd(G)) ∩ G| −

n2p 2r

![image 194](<2024-hoshen-stability-large-cuts-random_images/imageFile194.png>)

= O α + (np)−1/2 · n2p 1−e−n.

The assertion of the lemma follows, as α + (np)−1/2 ≪ 1 by our assumptions.

4.2. Proof of the lower bound on E[Z]. The following lemma, which is the main technical step in the proof of the lower bound on E[Z], abstracts the essence of the ‘resampling’ procedure that we described in the proof outline presented above. Given a hypergraph G, we denote by I(G) the family of its independent sets.

- Lemma 4.6. Suppose that G is a k-uniform hypergraph on V , let t be a nonnegative integer, and deﬁne


M := {R ⊆ V : G[R] is a matching with t edges}.

Suppose further that p ∈ (0,1), let R ∼ Vp, and let R∗ := R \ G[R]. Then, for all A ⊆ I(G) and A: A → P(V ), letting

k

p 1 − p

q 1 − q

and a := max |G[A(R∗)]| : R∗ ∈ A , we have

:=

![image 195](<2024-hoshen-stability-large-cuts-random_images/imageFile195.png>)

![image 196](<2024-hoshen-stability-large-cuts-random_images/imageFile196.png>)

P R ∈ M ∧ R∗ ∈ A ∧ G[A(R∗) ∩ R] = ∅ (1 − q)a · P(R ∈ M ∧ R∗ ∈ A).

Proof. Deﬁne the map S : A → P(P(V )) by S(R∗) := S ⊆ V \ R∗ : G[S] is a matching spanning S and |G[R∗ ∪ S]| = |G[S]| t .

Since, for every R∗ ∈ A, the family S(R∗) comprises precisely those sets S ⊆ V \ R∗ that are unions of edges of G and satisfy R∗ ∪ S ∈ M, we have

|S|

k·|G[S]|

P(R = R∗ ∪ S ∧ R∗ = R∗) P(R ∈ M ∧ R∗ = R∗)

p 1 − p

p 1 − p

1 ZR∗

1 ZR∗

PR∗(S) :=

·

·

=

=

![image 197](<2024-hoshen-stability-large-cuts-random_images/imageFile197.png>)

![image 198](<2024-hoshen-stability-large-cuts-random_images/imageFile198.png>)

![image 199](<2024-hoshen-stability-large-cuts-random_images/imageFile199.png>)

![image 200](<2024-hoshen-stability-large-cuts-random_images/imageFile200.png>)

![image 201](<2024-hoshen-stability-large-cuts-random_images/imageFile201.png>)

for all S ∈ S(R∗), where

|S|

|G[S]|

|M|

p 1 − p

q 1 − q

q 1 − q

ZR∗ :=

=

=

.

![image 202](<2024-hoshen-stability-large-cuts-random_images/imageFile202.png>)

![image 203](<2024-hoshen-stability-large-cuts-random_images/imageFile203.png>)

![image 204](<2024-hoshen-stability-large-cuts-random_images/imageFile204.png>)

M⊆G M∈S(R∗)

S∈S(R∗)

S∈S(R∗)

In other words, letting M denote the q-random subset of G, we have PR∗(S) = P M = G[S] | M ∈ S(R∗) .

Since both M ⊆ G : M ∈ S(R∗) and M ⊆ G : M[A(R∗)] = ∅ are decreasing families of subsets of G, Harris’s inequality [12] gives

P(R ∈ M ∧ R∗ = R∗ ∧ G[A(R∗) ∩ R] = ∅) P(R ∈ M ∧ R∗ = R∗)

PR∗(S)

=

![image 205](<2024-hoshen-stability-large-cuts-random_images/imageFile205.png>)

S∈S(R∗) G[A(R∗)∩S]=∅

= P M[A(R∗)] = ∅ | M ∈ S(R∗) P M[A(R∗)] = ∅

= (1 − q)|G[A(R∗)]| (1 − q)a.

Multiplying the above inequality through by P(R ∈ M ∧ R∗ = R∗) and summing the result over all R∗ ∈ A gives the desired inequality.

Corollary 4.7. Suppose that p Cn−1/m2(H)(log n)1/(eH−1) for some constant C and let G ∼ Gn,p. For every e ∈ Kn and all α > 0, letting d := ⌈log n⌉2, we have

P(Ye) exp − πH + O(α + p) · (n/r)vH−2peH−1

· P G ∈ COREr2d(α) ∧ e ∈ int(corer2d(G)) ∩ G − o(p) . Proof. Let ω := N → R be an arbitrary function satisfying 1 ≪ ω(n) ≪ log n and let

t := ω(n) · E|∂eH[G]|.

It follows from our upper-bound assumption on p that, for some constants C1 = C1(H) and C2 = C2(H,C), we have

t ω(n) · C1nvH−2peH−1 C2ω(n)log n d/eH, (17) provided that n is suﬃciently large. As in Lemma 4.6, let

M := G ⊆ Kn : ∂eH[G] is a matching with t edges . Further, let G∗ := G \ ∂eH[G] and deﬁne

A := G∗ ⊆ Kn : G∗ ∈ CORErd(α) ∧ e ∈ int(corerd(G∗)) ∩ G∗ ∧ ∂eH[G∗] = ∅ and the function A: A → P(Kn) by A(G∗) := ext∗(corerd(G∗)) for every G∗ ∈ A. By

- Lemma 4.2, for some constant CH that depends only on H,


|∂eH[A(G∗)]| πH + CHα · (n/r)vH−2 =: a.

max

G∗∈A

Further, since 1 − x exp(−x/(1 − x)) for all x ∈ (0,1), Lemma 4.6 applied to the (eH − 1)-uniform hypergraph ∂eH with vertex set Kn yields

P G ∈ M ∧ G∗ ∈ A ∧ ∂eH[A(G∗) ∩ G] = ∅

eH−1

p 1 − p

· a · P G ∈ M ∧ G∗ ∈ A . (18)

exp −

![image 206](<2024-hoshen-stability-large-cuts-random_images/imageFile206.png>)

We now show that (18) implies the assertion of the corollary. First, since (1 − x)1−eH = 1 + (eH − 1)x + O(x2) as x → 0, we have

eH−1

p 1 − p

· a exp − πH + CHα · (1 + eHp) · (n/r)vH−2peH−1 .

exp −

![image 207](<2024-hoshen-stability-large-cuts-random_images/imageFile207.png>)

Second, observe that G ∈ M implies that |G∗| = |G| − (eH − 1) · |∂eH[G]| |G| − eHt |G| − d, (19)

see (17). Consequently, Corollary 2.7 implies that the event G ∈ COREr2d(α) ∩ M is contained in the event G∗ ∈ CORErd(α) and int(corer2d(G)) ⊆ int(corerd(G∗)). We thus have

P G ∈ M ∧ G∗ ∈ A P G ∈ COREr2d(α) ∩ M ∧ e ∈ int(corer2d(G)) ∩ G

P G ∈ COREr2d(α) ∧ e ∈ int(corer2d(G)) ∩ G − P(G ∈/ M ∧ e ∈ G). Since the events e ∈ G and G ∈/ M are independent, we further have

P(G ∈/ M ∧ e ∈ G) = p · P(G ∈/ M) p · P(|∂eH[G]| > t) + P ∆(∂eH[G]) 2 .

The ﬁrst probability in the right-hand side is at most 1/ω(n), by Markov’s inequality and the deﬁnition of t, whereas the second probability can be bounded using Lemma 4.3

as follows: P ∆(∂eH[G]) 2 E|{(K,K′) ∈ (∂eH[G])2 : K = K′,K ∩ K′ = ∅}|

= 2∆p(∂eH) Cn−λ · nvH−2peH−1 2 for some positive C = C(H,ε) and λ = λ(H); since nvH−2peH−1 = O(log n) under our upper-bound assumption on p, we may conclude that P ∆(∂eH[G]) 2 = o(1).

Finally, since G ∈ M implies that |G| |G∗|+d, see (19), Corollary 2.7 implies that the event G ∈ M ∧G∗ ∈ CORErd(α) is contained in the event that G ∈ COREr0(α) and int(corerd(G∗)) ⊆ int(corer0(G)) (equivalently, that ext∗(corer0(G)) ⊆ ext∗(corerd(G∗)) = A(G∗)). Further, since G∗ ∈ A implies that e ∈ int(corerd(G∗)) ∩ G∗, we conclude that P(Ye) P G ∈ M ∧ G∗ ∈ A ∧ ∂eH[A(G∗) ∩ G] = ∅ .

The assertion of the lemma follows by combining the above inequality with (18) and the lower bounds on the two terms in the right-hand side of (18).

We are ﬁnally ready to complete the derivation of the lower bound on E[Z]. Since nvH−2peH−1 = O(log n), we have

πH + O(α + p) · (n/r)vH−2peH−1 = πH · (n/r)vH−2peH−1 + o(1). Consequently, we may deduce from Corollary 4.7 that

E[Z] =

P(Ye) exp −πH · (n/r)vH−2peH−1 − o(1)

e∈Kn

2d(α) − o(n2p) , where d := ⌈log n⌉2. Finally, Lemma 4.5 allows us to conclude that

· E |int(corer2d(G)) ∩ G| · G∈COREr

n2p 2r

E[Z] (1 + o(1)) · exp −πH · (n/r)vH−2peH−1 ·

. (20)

![image 208](<2024-hoshen-stability-large-cuts-random_images/imageFile208.png>)

- 4.3. Proof of the upper bound on E[Z2]. Given distinct edges e,f ∈ Kn and a family C of r pairwise-disjoint subsets of n , deﬁne


Ie,f(C) := G ⊆ Kn : e,f ∈ int(C) ∩ G ,

Ee,f(C) := G ⊆ Kn : (∂eH ∪ ∂fH)[ext(C) ∩ G] = ∅ . and note that, for every graph G ⊆ Kn,

G ∈ Ye ∩ Yf =⇒ G ∈ COREr0(α) ∩ Ie,f(corer0(G)) ∩ Ee,f(corer0(G)), as ext(C) ⊆ ext∗(C) for every family C. We may thus conclude that

E[Z2] E[Z] +

P G ∈ COREr0(α) ∩ Ie,f(corer0(G)) ∩ Ee,f(corer0(G)) . (21)

e,f∈Kn e =f

Our next lemma, which is a variant of [6, Lemma 10.2], will allow us to bound from above the probabilities in the right-hand side of (21).

Lemma 4.8. Let α be a nonnegative real and let C be the collection of all r-element families C of pairwise-disjoint subsets of n satisfying |X| n/r − αn for all X ∈ C. Suppose that, for each C ∈ C, we have an event I(C) that is determined by int(C) and an event E(C) that is determined by ext(C) and decreasing, and satisﬁes P(G ∈ E(C)) ξ. Then,

P G ∈ COREr0(α)∩I(corer0(G))∩E(corer0(G)) ξ ·P G ∈ COREr0(α)∩I(corer0(G)) . Proof. For any C ∈ C, denote by CORE(C) the family of all G ⊆ Kn such that corer0(G) = C. We ﬁrst observe that CORE(C) is increasing in ext(C). Indeed, since adding to G an edge of ext(corer0(G)) does not change the set of largest r-cuts, the resulting graph has the same core as G. Let FC be the σ-algebra generated by (Kn \ext(C))∩G. Since I(C) is determined by int(C) ⊆ Kn \ ext(C), we have

P G ∈ CORE(C) ∩ I(C) ∩ E(C) | FC = P G ∈ CORE(C) ∩ E(C) | FC · G∈I(C). (22) Further, since CORE(C) is increasing in ext(C) and E(C) is decreasing in ext(C), Harris’s inequality [12] implies that

P G ∈ CORE(C) ∩ E(C) | FC P G ∈ CORE(C) | FC · P G ∈ E(C) | FC

(23)

= P G ∈ CORE(C) | FC · P G ∈ E(C) ,

where the equality holds as E(C) is determined by ext(C) and thus the event G ∈ E(C) is independent of FC. Substituting (23) into (22), and using our assumption, yields

P G ∈ CORE(C) ∩ I(C) ∩ E(C) | FC ξ · P G ∈ CORE(C) | FC · G∈I(C)

= ξ · P G ∈ CORE(C) ∩ I(C) | FC . Consequently, since {CORE(C) : C ∈ C} is a partition of COREr0(α),

P G ∈ COREr0(α) ∩ I(corer0(G)) ∩ E(corer0(G))

P G ∈ CORE(C) ∩ I(C) ∩ E(C) ξ ·

P G ∈ CORE(C) ∩ I(C)

=

C∈C

C∈C

= ξ · P G ∈ COREr0(α) ∩ I(corer0(G)) , as desired.

Returning to (21), since clearly Ie,f(C) is determined by int(C) whereas Ee,f(C) is determined by ext(C) and decreasing, Lemma 4.8 implies that

E[Z2] E[Z] + ξ ·

P G ∈ COREr0(α) ∩ Ie,f(corer0(G))

e,f∈Kn e =f

(24)

E[Z] + ξ · E |int(corer0(G)) ∩ G|2 · G∈COREr

0(α) ,

where (writing C for the collection of all r-element families C of pairwise-disjoint subsets of n satisfying |X| n/r − αn for all X ∈ C)

ξ := max

P G ∈ Ee,f(C) = max

P (∂eH ∪ ∂fH)[ext(C) ∩ G] = ∅ .

C∈C

C∈C

It follows from Lemma 4.2 that, for every C ∈ C,

µp (∂eH ∪ ∂fH)[ext(C)] = µp(∂eH[ext(C)]) + µp(∂fH[ext(C)]) 2 πH − O(α + n−1) · (n/r)vH−2peH−1 2πH · (n/r)vH−2peH−1 − o(1),

where we used that nvH−2peH−1 = O(log n) whereas α ≪ 1/log n. On the other hand,

- Lemma 4.3 gives that, for some λ = λ(H) > 0 and C = C(H,ε),


∆p (∂eH ∪ ∂fH)[ext(C)] ∆p(∂eH ∪ ∂fH)

max

C∈C

Cn−λ · nvH−2peH−1 2 = o(1). Applying Janson’s inequality (Theorem 4.1), we conclude that

ξ exp −2πH · (n/r)vH−2peH−1 + o(1) . Substituting this estimate into (24) and using Lemma 4.5, we obtain

n2p 2r

E[Z2] E[Z] + (1 + o(1)) · exp −πH · (n/r)vH−2peH−1 ·

![image 209](<2024-hoshen-stability-large-cuts-random_images/imageFile209.png>)

2

.

Finally, recalling (20), in order to get the desired conclusion that E[Z2] (1+o(1))·E[Z]2, it is enough to argue that

n2p

exp −πH · (n/r)vH−2peH−1 ·

2r ≫ 1. To see that this is the case, note that our upper-bound assumption on p and the assumption that H is 2-balanced, i.e., m2(H) = (eH − 1)/(vH − 2), gives

![image 210](<2024-hoshen-stability-large-cuts-random_images/imageFile210.png>)

ε

1 m2(H) −

πH · (n/r)vH−2peH−1 πH · r2−vH · (θH − ε)eH−1 · log n 2 −

θH · log n, whereas our lower-bound assumption on p is that n2p εn2−1/m2(H).

![image 211](<2024-hoshen-stability-large-cuts-random_images/imageFile211.png>)

![image 212](<2024-hoshen-stability-large-cuts-random_images/imageFile212.png>)

Appendix A. Proof of Proposition 2.16 Let N := n2 . We will show that, for all n ≪ m (1 − δ)N,

![image 213](<2024-hoshen-stability-large-cuts-random_images/imageFile213.png>)

E[xr(G(n,m)) + xr(G(n,m + 1))] = Ω n3/m , (25) which clearly implies the assertion of the proposition. As in the proof of Lemma 2.12, consider the coupling of G1 ∼ G(n,m) and G2 ∼ G(n,m+1) such that e ∈ Kn is an edge chosen uniformly at random among the non-edges of G1 and the edges of G2. Recall from Fact 2.4 that

P(e ∈ critr(G2)) = P(e ∈/ eqr0(G1)). (26)

Writing ∂G2(Xr(G2)) for the set of edges of G2 with at least one endpoint in Xr(G2), we have

|critr(G2)| |ext(corer0(G2)) ∩ G2| br(G2) − |∂G2(Xr(G2))|

and thus

br(G2) − |∂G2(Xr(G2))| m + 1

P(e ∈ critr(G2)) E

. On the other hand,

![image 214](<2024-hoshen-stability-large-cuts-random_images/imageFile214.png>)

P(e ∈ eqr0(G1)) P(e ∈ int(corer0(G1))) = E |int(corer0(G1)) \ G1|

![image 215](<2024-hoshen-stability-large-cuts-random_images/imageFile215.png>)

N − m while

|int(corer0(G1)) \ G1| = |int(corer0(G1))| − |int(corer0(G1)) ∩ G1| |int(corer0(G1))| −

(n − xr(G1))/r 2 −

m r

m r

r ·

![image 216](<2024-hoshen-stability-large-cuts-random_images/imageFile216.png>)

![image 217](<2024-hoshen-stability-large-cuts-random_images/imageFile217.png>)

(n − xr(G1))(n − xr(G1) − r) 2r −

m r

=

![image 218](<2024-hoshen-stability-large-cuts-random_images/imageFile218.png>)

![image 219](<2024-hoshen-stability-large-cuts-random_images/imageFile219.png>)

N − n · (xr(G1) + r) − m r

,

![image 220](<2024-hoshen-stability-large-cuts-random_images/imageFile220.png>)

where the ﬁrst inequality is true since the edges in int(corer0(G1)) ∩ G1 do not cross any maximum r-cut of G1 and br(G1) r−r1 · m with probability one. Hence,

![image 221](<2024-hoshen-stability-large-cuts-random_images/imageFile221.png>)

N − n · (E[xr(G1)] + r) − m r · (N − m)

P(e ∈/ eqr0(G1)) 1 −

![image 222](<2024-hoshen-stability-large-cuts-random_images/imageFile222.png>)

n · (E[xr(G1)] + r) r · (N − m)

r − 1 r

. Substituting the above bounds into (26) and taking expectation, we conclude that

+

=

![image 223](<2024-hoshen-stability-large-cuts-random_images/imageFile223.png>)

![image 224](<2024-hoshen-stability-large-cuts-random_images/imageFile224.png>)

E|∂G2(Xr(G2))| m + 1

r − 1 r

n · (E[xr(G1)] + r) r · (N − m)

E[br(G2)] m + 1 −

+

.

![image 225](<2024-hoshen-stability-large-cuts-random_images/imageFile225.png>)

![image 226](<2024-hoshen-stability-large-cuts-random_images/imageFile226.png>)

![image 227](<2024-hoshen-stability-large-cuts-random_images/imageFile227.png>)

![image 228](<2024-hoshen-stability-large-cuts-random_images/imageFile228.png>)

Since E[br(G2)] = r−r1 · m + Θ(√nm) when n ≪ m (1 − δ)N, by [3, Lemma 14],

![image 229](<2024-hoshen-stability-large-cuts-random_images/imageFile229.png>)

![image 230](<2024-hoshen-stability-large-cuts-random_images/imageFile230.png>)

![image 231](<2024-hoshen-stability-large-cuts-random_images/imageFile231.png>)

E|∂G2(Xr(G2))| m

n m

E[xr(G1)] n

c ·

+

, (27)

![image 232](<2024-hoshen-stability-large-cuts-random_images/imageFile232.png>)

![image 233](<2024-hoshen-stability-large-cuts-random_images/imageFile233.png>)

![image 234](<2024-hoshen-stability-large-cuts-random_images/imageFile234.png>)

for some c > 0 that depends only on r and δ. The following claim bounds the second summand in the left-hand side of (27) from above by an almost-linear function of E[xr(G2)].

Claim A.1. There exists a constant C such that

E|∂G2(Xr(G2))|

4m n · E[xr(G2)] + C

![image 235](<2024-hoshen-stability-large-cuts-random_images/imageFile235.png>)

![image 236](<2024-hoshen-stability-large-cuts-random_images/imageFile236.png>)

- m

![image 237](<2024-hoshen-stability-large-cuts-random_images/imageFile237.png>)

- n · E[xr(G2)]log


en E[xr(G2)]

![image 238](<2024-hoshen-stability-large-cuts-random_images/imageFile238.png>)

+ 1.

We ﬁrst show how (27) and Claim A.1 imply (25). Substituting the upper bound on E|∂G2(Xr(G2))| into (27), we obtain

![image 239](<2024-hoshen-stability-large-cuts-random_images/imageFile239.png>)

n3 m

![image 240](<2024-hoshen-stability-large-cuts-random_images/imageFile240.png>)

en E[xr(G2)]

n m · E[xr(G2)]log

c ˜·

(28)

E[xr(G1)] + E[xr(G2)] +

![image 241](<2024-hoshen-stability-large-cuts-random_images/imageFile241.png>)

![image 242](<2024-hoshen-stability-large-cuts-random_images/imageFile242.png>)

![image 243](<2024-hoshen-stability-large-cuts-random_images/imageFile243.png>)

![image 244](<2024-hoshen-stability-large-cuts-random_images/imageFile244.png>)

for some c˜ that depends only on r and δ. Suppose that E[xr(G2)] c/ ˜ 3 · n3/m ≪ n. Since the function x  → xlog enx is increasing on (0,n], we have

![image 245](<2024-hoshen-stability-large-cuts-random_images/imageFile245.png>)

![image 246](<2024-hoshen-stability-large-cuts-random_images/imageFile246.png>)

![image 247](<2024-hoshen-stability-large-cuts-random_images/imageFile247.png>)

![image 248](<2024-hoshen-stability-large-cuts-random_images/imageFile248.png>)

![image 249](<2024-hoshen-stability-large-cuts-random_images/imageFile249.png>)

![image 250](<2024-hoshen-stability-large-cuts-random_images/imageFile250.png>)

n3 m ·

n3 m

en E[xr(G2)]

3e c˜ ·

c ˜ 3 ·

c ˜ 3 ·

n m · E[xr(G2)]log

n m

- m

![image 251](<2024-hoshen-stability-large-cuts-random_images/imageFile251.png>)

- n


log

,

![image 252](<2024-hoshen-stability-large-cuts-random_images/imageFile252.png>)

![image 253](<2024-hoshen-stability-large-cuts-random_images/imageFile253.png>)

![image 254](<2024-hoshen-stability-large-cuts-random_images/imageFile254.png>)

![image 255](<2024-hoshen-stability-large-cuts-random_images/imageFile255.png>)

![image 256](<2024-hoshen-stability-large-cuts-random_images/imageFile256.png>)

![image 257](<2024-hoshen-stability-large-cuts-random_images/imageFile257.png>)

![image 258](<2024-hoshen-stability-large-cuts-random_images/imageFile258.png>)

![image 259](<2024-hoshen-stability-large-cuts-random_images/imageFile259.png>)

where the second inequality holds as m ≫ n and limx→0 xlog(1/x) = 0. This means, by (28), that E[xr(G1)] c/ ˜ 3 · n3/m, as desired. We now prove the claim.

![image 260](<2024-hoshen-stability-large-cuts-random_images/imageFile260.png>)

It suﬃces to show that, with probability at least 1 − 1/n2, for every nonempty set A ⊆ V (G2),

![image 261](<2024-hoshen-stability-large-cuts-random_images/imageFile261.png>)

m N · |A|n + C

en |A|

- m

![image 262](<2024-hoshen-stability-large-cuts-random_images/imageFile262.png>)

- n · |A|log


|∂G2(A)|

, (29) where C is a large constant. Indeed, this estimate yields

![image 263](<2024-hoshen-stability-large-cuts-random_images/imageFile263.png>)

![image 264](<2024-hoshen-stability-large-cuts-random_images/imageFile264.png>)

E|∂G2(Xr(G2))|

4m n · E[xr(G2)] + C

![image 265](<2024-hoshen-stability-large-cuts-random_images/imageFile265.png>)

4m n · E[xr(G2)] + C

![image 266](<2024-hoshen-stability-large-cuts-random_images/imageFile266.png>)

![image 267](<2024-hoshen-stability-large-cuts-random_images/imageFile267.png>)

- m

![image 268](<2024-hoshen-stability-large-cuts-random_images/imageFile268.png>)

- n · E xr(G2)log


![image 269](<2024-hoshen-stability-large-cuts-random_images/imageFile269.png>)

- m

![image 270](<2024-hoshen-stability-large-cuts-random_images/imageFile270.png>)

- n · E[xr(G2)]log


en xr(G2)

![image 271](<2024-hoshen-stability-large-cuts-random_images/imageFile271.png>)

en E[xr(G2)]

![image 272](<2024-hoshen-stability-large-cuts-random_images/imageFile272.png>)

1 n2

+

![image 273](<2024-hoshen-stability-large-cuts-random_images/imageFile273.png>)

+ 1,

n 2

where the second inequality follows from Jensen’s inequality applied to the concave function x  → xlog(en/x).

Note that, for every nonempty set A ⊆ V (G2), the random variable |∂G2(A)| has hypergeometric distribution with mean at most m/N · |A|n. In particular, standard tail estimates yield (writing p = m/N and |A| = k), for every t 0,

m N · |A|n + t P Bin(kn,p) p · kn + t exp −t2

P |∂G2(A)|

![image 274](<2024-hoshen-stability-large-cuts-random_images/imageFile274.png>)

![image 275](<2024-hoshen-stability-large-cuts-random_images/imageFile275.png>)

2knp + t exp −t2

t 2

+ exp −

.

![image 276](<2024-hoshen-stability-large-cuts-random_images/imageFile276.png>)

![image 277](<2024-hoshen-stability-large-cuts-random_images/imageFile277.png>)

4knp

![image 278](<2024-hoshen-stability-large-cuts-random_images/imageFile278.png>)

Invoking the above estimate with t := C m/n · |A|log(en/|A|), we conclude that the probability that (29) fails for some nonempty set A is at most

n

k=1

n k

C2kN log(en/k) 2 4n2

exp −

![image 279](<2024-hoshen-stability-large-cuts-random_images/imageFile279.png>)

+ exp −Ck log

en k

![image 280](<2024-hoshen-stability-large-cuts-random_images/imageFile280.png>)

n

2

k=1

where the last inequality is true whenever C is suﬃciently large.

en k

![image 281](<2024-hoshen-stability-large-cuts-random_images/imageFile281.png>)

k−Ck

n−2,

References

- [1] L. Babai, M. Simonovits, and J. Spencer. Extremal subgraphs of random graphs. J. Graph Theory, 14(5):599–622, 1990.
- [2] G. Brightwell, K. Panagiotou, and A. Steger. Extremal subgraphs of random graphs. Random Structures Algorithms, 41(2):147–178, 2012.
- [3] A. Coja-Oghlan, C. Moore, and V. Sanwalani. MAX k-CUT and approximating the chromatic number of random graphs. Random Structures Algorithms, 28(3):289–322, 2006.


- [4] D. Conlon and W. T. Gowers. Combinatorial theorems in sparse random sets. Ann. of Math. (2), 184(2):367–454, 2016.
- [5] D. Coppersmith, D. Gamarnik, M. T. Hajiaghayi, and G. B. Sorkin. Random MAX SAT, random MAX CUT, and their phase transitions. Random Structures Algorithms, 24(4):502–545, 2004.
- [6] B. DeMarco and J. Kahn. Tur´an’s theorem for random graphs. arXiv:1501.01340.
- [7] B. DeMarco and J. Kahn. Mantel’s theorem for random graphs. Random Structures Algorithms, 47(1):59–72, 2015.
- [8] A. Dembo, A. Montanari, and S. Sen. Extremal cuts of sparse random graphs. Ann. Probab., 45(2):1190–1217, 2017.
- [9] O. Engelberg, W. Samotij, and L. Warnke. On the typical structure of graphs not containing a ﬁxed vertex-critical subgraph. arXiv:2110.10931.
- [10] D. Gamarnik and Q. Li. On the max-cut of sparse random graphs. Random Structures Algorithms, 52(2):219–262, 2018.
- [11] L. Gishboliner, M. Krivelevich, and G. Kronenberg. On MAXCUT in strictly supercritical random graphs, and coloring of random graphs and random tournaments. Random Structures Algorithms, 52(4):545–559, 2018.
- [12] T. E. Harris. A lower bound for the critical probability in a certain percolation process. Proc. Cambridge Philos. Soc., 56:13–20, 1960.
- [13] W. Hoeﬀding. Probability inequalities for sums of bounded random variables. J. Amer. Statist. Assoc., 58:13–30, 1963.
- [14] I. Hoshen and W. Samotij. Simonovits’s theorem in random graphs. arXiv:2308.13455.
- [15] S. Janson. Poisson approximation for large deviations. Random Structures Algorithms, 1(2):221–229, 1990.
- [16] Y. Kohayakawa, T.  Luczak, and V. Ro¨dl. On K4-free subgraphs of random graphs. Combinatorica, 17(2):173–213, 1997.
- [17] W. Samotij. Stability results for random discrete structures. Random Structures Algorithms, 44(3):269–289, 2014.
- [18] M. Schacht. Extremal results for random discrete structures. Ann. of Math. (2), 184(2):333–365, 2016.
- [19] M. Simonovits. A method for solving extremal problems in graph theory, stability problems. In Theory of Graphs (Proc. Colloq., Tihany, 1966), pages 279–319. Academic Press, New York-London, 1968.
- [20] P. Tur´an. Eine Extremalaufgabe aus der Graphentheorie. Mat. Fiz. Lapok, 48:436–452, 1941.


School of Mathematical Sciences, Tel Aviv University, Tel Aviv 6997801, Israel Email address: ilayhoshen@gmail.com

School of Mathematical Sciences, Tel Aviv University, Tel Aviv 6997801, Israel Email address: samotij@tauex.tau.ac.il

Department of Computer Science, University of Sheffield, Sheffield S1 4DP, UK Email address: m.zhukovskii@sheffield.ac.uk

