# arXiv:2002.05816v2[math.CO]7Apr2021

## HIGH POWERS OF HAMILTONIAN CYCLES IN RANDOMLY AUGMENTED GRAPHS

SYLWIA ANTONIUK, ANDRZEJ DUDEK, CHRISTIAN REIHER, ANDRZEJ RUCIŃSKI, AND MATHIAS SCHACHT

Abstract. We investigate the existence of powers of Hamiltonian cycles in graphs with large minimum degree to which some additional edges have been added in a random manner. For all integers k ě 1, r ě 0, and ě pr ` 1qr, and for any α ą k`k1 we show that adding Opn2´2{ q random edges to an n-vertex graph G with minimum degree at least αn yields, with probability close to one, the existence of the pk  ` rq-th power of a Hamiltonian cycle. In particular, for r “ 1 and “ 2 this implies that adding Opnq random edges to such a graph G already ensures the p2k ` 1q-st power of a Hamiltonian cycle (proved independently by Nenadov and Trujić). In this instance and for several other choices of k, , and r we can show that our result is asymptotically optimal.

§1. Introduction

All graphs we consider are ﬁnite. For m P N the m-th power Fm of a graph F is deﬁned as the graph on the same vertex set whose edges join distinct vertices at distance at most m in F. A Hamiltonian cycle in a graph G is a cycle which passes through all vertices of G. The m-th power of an s-vertex path Ps or cycle Cs will be often called the m-path or, respectively, the m-cycle.

For integers m ě 1 and n ě m ` 2, let us consider the set Cnm of all n-vertex graphs G that contain the m-th power Cnm of a Hamiltonian cycle Cn. Clearly, Cnm is a monotone graph property, as powers of Hamiltonian cycles cannot disappear as a result of adding more edges (without new vertices).

The classical theorem of Dirac [4] asserts that every graph of order n ě 3 and minimum degree δpGq ě n{2 is Hamiltonian. Furthermore, the resolution of the Pósa–Seymour conjecture [6,12] (for large n), proved by Komlós, Sarközy, and Szemerédi [9], yields the following extension: for each k ě 2 every n-vertex graph G with n ě n0 and δpGq ě k`k1n possesses property Cnk.

The second author was supported in part by Simons Foundation Grant #522400. The fourth author was supported in part by the Polish NSC grant 2018/29/B/ST1/00426. The ﬁfth author was supported by the European Research Council (PEPCo 724903).

1

Suppose that a graph G has large minimum degree which, however, falls short from the above bound. Would adding a few random edges to G help to create the desired power of a Hamiltonian cycle? Bohman, Frieze, and Martin [2] were the ﬁrst to study this question. They showed that, for any ε ą 0, randomly sprinkling Opnq additional edges onto a graph G with δpGq ě εn forces, with high probability, a Hamiltonian cycle Cn. This result was extended in [5] to all k ě 1: for every graph G with n ě n0 and δpGq ě pk`k1 ` εqn adding Opnq random edges yields, with high probability, the pk ` 1q-st power of a Hamiltonian cycle Cnk`1. Note that the result in [9] guarantees only the existence of Cnk in G. In this paper we substantially generalize the result in [5].

We investigate the probability that a given n-vertex graph G with minimum degree high enough to yield, by the Pósa–Seymour conjecture, Cnk in G, augmented by a binomial random graph Gpn,pq, p “ ppnq, spans the m-th power of a Hamiltonian cycle Cnm. In other words we are interested in PpG Y Gpn,pq P Cnmq. To this end, we introduce the following deﬁnition.

Deﬁnition 1.1. Given integers k ě 0 and m ě 1, we say that a sequence dpnq is a pk,mq-Dirac threshold if

(a) for every α ą k`k1 there is C ą 0 such that for all ppnq ě Cdpnq

˘ “ 1, where the minimum is taken over all n-vertex graphs G with δpGq ě αn, while

`

nlimÑ8min

G Y Gpn,ppnqq P Cnm

P

G

(b) there exists α0 ą k`k1 such that for all k`k1 ă α ă α0 there is c ą 0 and a sequence of n-vertex graphs Gα “ Gαpnq such that δpGαq ě αn and for all p ď cdpnq

`

˘ “ 0.

nlimÑ8P

Gα Y Gpn,ppnqq P Cnm

We denote any function dpnq satisfying both conditions (a) and (b) by dk,mpnq.

In view of this deﬁnition, for any dpnq satisfying condition (a) alone we have dk,mpnq ď dpnq, while for any dpnq satisfying condition (b) alone we have dk,mpnq ě dpnq. Also dk,m`1pnq ě dk,mpnq, as Cnm Ă Cnm`1.

- A careful reader will notice that the above deﬁnition assumes that the dependence on α


in the threshold dk,m appears only in a multiplicative constant. This is suﬃcient for our main result, however, there are instances of k and m for which this is not the case (see Section 9).

The result in [2] can be now restated as d0,1 “ n´1. Our main result establishes an upper bound on the Dirac threshold dk,mpnq for inﬁnitely many values of m for each k P N.

- Theorem 1.2. For all integers k ě 1, r ě 0, ě rpr ` 1q, and for m “ k  ` r dk,mpnq ď n´2{ .

Notice that the largest r “ rp q for which ě rpr`1q is r “ t

?4 `1´1

2 u. Thus, Theorem 1.2 implies that dk,mpnq ď n´2{ for any m ď k  `

?4 `1´1

2 . Furthermore, for many choices of k and m we can provide a matching lower bound on dk,mpnq, thus, determining the pk,mq-Dirac threshold altogether.

- Theorem 1.3. For all positive integers k, , and m satisfying the inequalities


?4 ` 1 ´ 1 2

pk ` 1qp ´ 1q ď m ď k  `

, we have

dk,mpnq “ n´2{ .

In particular, for each “ 2,3,4,5,6 and inﬁnitely many k, we list all values of m for which dk,mpnq has been determined in Theorem 1.3. Corollary 1.4. The following holds:

- (i) For k ě 1 and k ` 1 ď m ď 2k ` 1 we have dk,mpnq “ n´1.
- (ii) For k ě 1 and 2k ` 2 ď m ď 3k ` 1 we have dk,mpnq “ n´2{3.
- (iii) For k ě 2 and 3k ` 3 ď m ď 4k ` 1 we have dk,mpnq “ n´1{2.
- (iv) For k ě 3 and 4k ` 4 ď m ď 5k ` 1 we have dk,mpnq “ n´2{5.
- (v) For k ě 3 and 5k ` 5 ď m ď 6k ` 2 we have dk,mpnq “ n´1{3.


Part (i) of Corollary 1.4 was independently proved by Nenadov and Trujić in [10].

We also show that the threshold from the last case of Corollary 1.4 can be extended to k P t1,2u.

- Theorem 1.5. For every integer k ě 1, dk,6k`2pnq “ n´1{3.


Observe that in view of Corollary 1.4 the ﬁrst open case is k “ 1 and m “ 5. We will comment on this in Section 9.

§2. Random graphs

There are two basic models of random graphs, the binomial one, Gpn,pq, and the uniform one, Gpn,Mq, which are asymptotically equivalent under some mild assumptions whenever M „ `n

˘

p (see Section 1.4 in [8]). In this paper we chose to state and prove our results in the binomial model, yet they can be translated to the uniform model if there is such a

2

need. For instance, Theorem 1.2 asserts that under the assumptions given there it suﬃces to add Opn2´2{ q random edges to ensure a copy of Cnm.

In this section we collect some results on Gpn,pq which we use later. For a graph property P, we say that P holds asymptotically almost surely (a.a.s.) if PpGpn,pq P Pq Ñ 1 as n Ñ 8. In our proofs we are going to use the following consequence of Chebyshev’s inequality (see Remark 3.7. in [8]).

Fact 2.1. For every ě 3 and γ ą 0, there is a constant c “ cp ,γq such that if p ď cn´2{ , then a.a.s. there are fewer than γn copies of the clique K in Gpn,pq.

We will also apply two versions of Janson’s inequality. The most general one is given in [8, Theorem 2.14]. For the proof of Theorem 1.2 we will need a strengthening of Theorem 3.9 in [8] (the R-H-S inequality only), which is a version of Theorem 2.14 in the context of subgraphs of random graphs. For a graph G with at least one edge, set

ΨF, where ΨF “ nv

ΦG “ min

FĎG,eF ą0

F, and vF, eF denote, respectively, the number of vertices and the number of edges of graph F.

pe

F

- Theorem 2.2. Let τ ą 0 and G be a graph with at least one edge and let G be a family of


copies of G in Kn with |G| ě τnv

G. Further, let X be the number of copies of G belonging to G which are present in Gpn,pq. Then,

PpX ď τΨG{2q ď expt´τ24´eGΦG{8u.

Proof. We follow the lines of the proof of Theorem 3.9 in [8]. The main diﬀerence is that we rely on Theorem 2.14 from [8], and not on Theorem 2.18(ii). Moreover, instead of deﬁning the indicators IG1 for all copies of G in Kn, we deﬁne them for G1 P G only.

We have

“ τΨG. By Theorem 2.14 from [8],

λ :“ EX “ |G|pe

ě τnv

pe

G

G

G

PpX ď τΨG{2q ď PpX ď λ{2q ď expt´λ2{p8∆¯qu, (2.1) where ∆¯ is deﬁned in Theorem 2.14 [8]. In our case,

∆¯ “ ÿ

ÿ

ÿ

p2e

G´eH,

G1

G2

H

ř

ř

where

G1 – over all copies G1 of G in G, while

H is taken over all subgraphs H of G with eH ą 0,

ř

G2 – over all copies G2 of G in G with G1 X G2 “ H. This can be upper

bounded, estimating crudely the number of copies of H in G by 2eG, as follows: ÿ

Ψ2G ΦG

Ψ2G ΨH ď 4eG

G´eH ď ÿ

G´vHp2e

G2eG

2eG

nv

nv

.

H

H

Plugging this bound into (2.1) completes the proof.

§3. Lower bounds

Here we deduce Theorems 1.3 and 1.5 from Theorem 1.2 by complementing it with lower bounds on the corresponding pk,mq-Dirac thresholds. Proof of Theorem 1.3. In view of Theorem 1.2, it suﬃces to show that if pk`1qp ´1q ď m, then dk,mpnq ě n´2{ .

By monotonicity of dk,mpnq as a function of m, we may assume that m “ pk ` 1qp ´ 1q. Set ε0 “ p2pm ` 1qpk ` 1qq´1 and ﬁx α “ k`k1 ` ε for some ε ď ε0. Consider the following construction of a graph Gα. For n ě 4pk ` 2qpm ` 1q let rns “ V1 ¨Y ... ¨Y Vk`1 be a vertex partition with each part of size n{pk ` 1q (for simplicity, we assume that n is divisible by k ` 1). Moreover, for every i “ 1,...,k ` 1, ﬁx a subset Wi Ď Vi of size |Wi| “ rεns. Let G “ Gα be the n-vertex graph consisting of the union of the complete pk ` 1q-partite graph with vertex partition V1 ¨Y... ¨YVk`1 and k `1 complete bipartite graphs with vertex classes Wi and Vi Wi for i “ 1,...,k ` 1. Clearly, δpGq ě pk`k1 ` εqn. Set W “ Ťk`1

i“1 Wi, for convenience.

Let p ď cn´2{ , where c “ cp ,γq is deﬁned in Fact 2.1 with γ “ p4pm ` 1qq´1. We are going to show that a.a.s. H “ G Y Gpn,pq does not contain any copy of Cnm. Note that any Cnm Ă H contains tn{pm ` 1qu vertex-disjoint copies of Km`1 and only at most ˇWˇ “ pk ` 1qrεns of them have a vertex in W.

Consider a copy K of Km`1 which is disjoint from W. Since rmk``11s “ , by Pigeonhole Principle, K must contain a copy K1 of K that lies entirely in some set Vi and thus K1 must be a subgraph of Gpn,pq. In conclusion, if Cnm Ă H, then the random graph Gpn,pq must contain at least

Z

^ ´ pk ` 1qrεns ě

n m ` 1

n m ` 1 ´ 1 ´ pk ` 1qpε0n ` 1q “

n 2pm ` 1q

´ k ´ 2 ě γn

copies of K . However, by Fact 2.1, for p ď cn´2{ , a.a.s. there are fewer than γn copies of K in Gpn,pq. This establishes part (b) of Deﬁnition 1.1 with α0 “ pk`k1 ` ε0q.

Proof of Theorem 1.5. Let m “ 6k ` 2 and k “ 1,2. (For k ě 3, Theorem 1.5 follows from Corollary 1.4(v).) Theorem 1.2, applied with “ 6 and r “ 2, yields that dk,m ď n´1{3. We will show that also dk,m ě n´1{3. For ε1 “ 1{288 and ε2 “ 1{105, ﬁx αk “ k`k1 ` εk,

k “ 1,2, and consider the graph Gα

constructed in the proof of Theorem 1.3. Further, take p ď cn´1{3, where c “ cp6,εkq is deﬁned in Fact 2.1. Consequently, there are a.a.s. no more than εkn copies of K6 in Gpn,pq.

k

Assume that H “ G Y Gpn,pq contains a copy C of Cnm. After removing from H all vertices in W as well as at least one vertex from each copy of K6 in Gpn,pq, we obtain a K6-free subgraph H1 Ă H on n1 ě n ´ pk ` 2qεkn vertices such that H1rVjs Ă Gpn,pq for 1 ď j ď k ` 1. Observe that H1 X C contains an m-path P with

1 pk ` 2qεk ´ 1 ě

1 pk ` 3qεk

n1 pk ` 2qεkn ě

|V pPq| ě

.

Now, consider separately the cases k “ 2 and k “ 1. The former one is a bit easier. We have m “ 14 and H1 is tripartite. For each 1 ď j ď 3, the subgraph Qj “ PrVjs contains a spanning 4-path in Gpn,pq. Indeed, let v1,...,v5 be ﬁve consecutive vertices of Qj (in the linear order determined by P). Since there are no copies of K6 in H1, there are at most 3 ` 2 ¨ 5 vertices between v1 and v5 on P. Therefore, vs and vt, 1 ď s ă t ď 5, are adjacent in P and thus in Qj.

Let q “ maxt|V pQ1q|,|V pQ2q|,|V pQ3q|u. Then, Gpn,pq contains a 4-path with

1

1 3|V pPq| ě

15ε2 “ 7 vertices and 4q ´ p1 ` 2 ` 3q “ 4q ´ 6 edges. However, the expected number of such subgraphs in Gpn,pq with p “ Opn´1{3q is smaller than

q ě

nqp4q´6 “ Opn´q{3`2q “ Opn´7{3`2q “ op1q,

which by Markov’s inequality implies that a.a.s. there are not such copies at all.

For k “ 1, we have m “ 8 and H1 is bipartite. Now, we can only claim that each Qj contains a spanning 3-path Pj in Gpn,pq. Indeed, let v1,...,v4 be four consecutive vertices of Qj. Similarly to the case k “ 2, v1,...,v4 form a clique in Gpn,pq. Fortunately, there are more edges in Qj. To see it, divide V pPq into t|V pPq|{9u consecutive copies of K9. Each of them contributes a copy of K5 to either Q1 or Q2 and thus an extra edge which is not present in Pj. Without loss of generality, suppose that Q1 contains at least 12t|V pPq|{9u copies of K5. Then Q1 is a subgraph of Gpn,pq with q vertices and at least

- 1

- 2 ě 3q ´ 3 `


1 72ε1 ´

- 1

- 2 “ 3q `


- 1

- 2


|V pPq| 18 ´

|P1| `

edges. Again, with p “ Opn´1{3q, by Markov’s inequality, there are no such subgraphs in Gpn,pq.

§4. Outline of the proof of Theorem 1.2

The proof of Theorem 1.2 is based on the absorption method and follows the general outline of the proof in [5]. It relies on four lemmas, the Connecting Lemma, the Reservoir Lemma, the Absorbing Lemma, and the Covering Lemma. The last three of these lemmas will be stated here and proved in the forthcoming sections. At the end of this section we provide a short proof of Theorem 1.2 based on these lemmas. The Connecting Lemma is used only in the proof of Absorbing Lemma and will be stated and proved in Section 6. Each of these lemmas provides the existence of some m-paths in H “ G Y Gpn,pq, so the proofs involve mixed techniques from extremal graph theory and random graphs.

Throughout the rest of the paper we assume that m “ k  ` r and ě rpr ` 1q, where k,  P N and r ě 0. Observe that if “ 1, then necessarily r “ 0 and so m “ k. This case, however, follows deterministically from [9], since δpGq ě kn{pk ` 1q. Therefore, from now on we will be assuming that ě 2. Note that by the monotonicity of dk,mpnq as a function of m, it is enough to consider only the largest r satisfying ě rpr ` 1q. In particular, in view of ě 2, we may also assume that r ě 1.

Given an m-path P “ pv1,...,vtq, the sequences pv1,...,vmq and pvt,...,vt´m`1q are called the ends of P. We say that P connects its ends and the vertices of P not belonging to its ends are called internal. As every segment of consecutive m`1 vertices of an m-path forms a clique Km`1, the ends span m-cliques. If K and K1 are the ordered cliques induced by the ends of an m-path P, we may also say that P connects K and K1 .

- Deﬁnition 4.1. Given ξ ą 0, an m-tuple xá “ px1,x2,...,xmq of vertices of an n-vertex graph G is ξ-connectable if there exist ξnk`1 (ordered) copies py1,y2,...,yk`1q of Kk`1 in G with the property that for each i “ 1,2,...,k ` 1, yi P NGpxpi´1q `1,...,xmq. An m-path in H is ξ-connectable if both its ends are ξ-connectable m-tuples in G.


Note that for 0 ă ξ1 ă ξ2, if an m-tuple is ξ2-connectable, then is is also ξ1-connectable.

We may now state the Reservoir Lemma which is proved in Section 6. Here and below V always stands for the vertex set of the graphs G, Gpn,pq, and H.

- Lemma 4.2 (Reservoir Lemma). For all ε ą 0 and ξ ą 0 there exists γ ą 0 such that for all suﬃciently large C “ Cpξ,γq ě 1 and for every n-vertex graph G with


δpGq ě pk`k1 ` εqn there exists a set of vertices R Ď V of size 12γ2n ď |R| ď 2γ2n such that for p “ ppnq ě Cn´2{ a.a.s. H “ G Y Gpn,pq has the following property.

?γ|R| and for every pair of disjoint, ordered ξ-connectable m-tuples x,á xá1 in G ´ R, there exists an m-path in H connecting xá and xá1 with pk ` 1q2k`1 internal vertices, all from R S.

For every S Ď R with |S| ď

The next result (proved in Section 7) yields the existence of an m-path A, called absorbing, which can absorb any small set of vertices. This enables us to reduce our goal to an easier problem of ﬁnding an almost spanning m-cycle containing A.

- Lemma 4.3 (Absorbing Lemma). For every ε ą 0 there exists ξ ą 0 such that for suﬃciently small γ “ γpε,ξq ą 0 and suﬃciently large C “ Cpε,ξq ě 1, every n-vertex graph G with δpGq ě pk`k1 ` εqn, and every p “ ppnq ě Cn´2{ , a.a.s. H “ G Y Gpn,pq has the following property.

For every set of vertices R Ď V with |R| ď 2γ2n the graph H´R contains a ξ-connectable m-path A with |V pAq| ď γn{2 such that for every U Ď V V pAq with |U| ď 3γ2n there exists an m-path AU with V pAUq “ V pAq Y U having the same ends as A.

The last lemma below states that almost the whole graph under consideration can be covered by a linear in n number of m-paths. These paths will be eventually connected together with the absorbing path A, to produce the desired m-th power of an almost spanning cycle. We shall prove the Covering Lemma in Section 8.

- Lemma 4.4 (Covering Lemma). For every ε ą 0 there exist ξ ą 0 and γ ą 0 such that


for suﬃciently large C “ Cpξ,γq ě 1, for every n-vertex graph G with δpGq ě pk`k1 ` εqn and every p “ ppnq ě Cn´2{ , a.a.s. H “ G Y Gpn,pq has the following property.

For every subset Q Ă V with |Q| ď γn there exists a family P of at most γ3n vertexdisjoint ξ-connectable m-paths in H with vertices in V Q covering all but at most γ2n vertices of V Q.

We conclude the present section with a proof of our main result assuming the three lemmas stated above. Although the statements of Lemmas 4.2 - 4.4 are not monotone in γ, it follows from the three proofs (see Sections 6-8) that whenever they are true for some γ0 ą 0, they are also true for any 0 ă γ ă γ0.

Proof of Theorem 1.2. We begin by ﬁxing the constants. During this process we adopt the convention that a constant coming from Lemma 4.x receives a subscript x. Let k P N and α P `k`k1,1

˘

be given and set ε “ α ´ k`k1. Plugging ε into Lemmas 4.3 and 4.4 we obtain, respectively, constants ξ3, γ3, C3 and ξ4, γ4, C4. Plugging ξ “ mintξ3,ξ4u into Lemma 4.2 we obtain γ2 and C2. Finally, we set

γ “ min "γ2,γ3,γ4,

*

1 4

` pk ` 1q2k`2˘´2

,

and C “ maxtC2,C3,C4u.

Let an n-vertex graph G with δpGq ě pk`k1 ` εqn and p ě Cn´2{ be given. We need to check that a.a.s. the graph H “ G Y Gpn,pq contains a copy of Cnm. For this purpose

it suﬃces to prove that a graph H satisfying the conclusions of all three lemmas above contains a copy of Cnm.

By Lemma 4.2 there is a reservoir set R Ď V of size 12γ2n ď |R| ď 2γ2n. By Lemma 4.3 there exists an absorbing m-path A Ď H ´ R. Since |R| ` |V pAq| ď p2γ2 ` γ{2qn ă γn, we can apply Lemma 4.4 to Q “ R Y V pAq and obtain a collection P of at most γ3n vertex-disjoint ξ-connectable m-paths in H ´ Q whose vertices cover the set V Q except for a small subset U1 Ď V Q with |U1| ď γ2n. Next, we want to create the m-th power of a long cycle in H by connecting together all paths in P Y tAu.

To this end, we make |P| ` 1 successive applications of Lemma 4.2. In each of them we let xá and xá1 be the ends of the m-paths we wish to connect and let S Ď R be the set of vertices that were used as internal vertices in previous applications. When arriving at the last step of this process, that is, when closing the m-cycle, the set S of vertices we need to avoid has size

?γ|R|, which justiﬁes repeated applications of Lemma 4.2.

|S| “ pk ` 1q2k`1|P| ď pk ` 1q2k`1γ3n ď pk ` 1q2k`2γ|R| ď

Let F be the obtained m-cycle. The complement U “ V V pFq satisﬁes |U| “ |U1| ` |R V pFq| ď 3γ2n,

whence, by Lemma 4.3, there exists an m-path AU with V pAUq “ V pAq Y U having the same ends as A. Therefore, we can replace A by AU in F and obtain the desired m-th power of a Hamiltonian cycle in H.

§5. Preliminaries

In this section we present results which serve as tools in the proofs of the lemmas stated in the previous section.

## 5.1. Neighbourhoods in graphs of large minimum degree. We recall the following

`Vj˘

standard notation. For a set V and an integer j P N we write

for the family of all

- j-element subsets of V . Given a graph G “ pV,Eq we write NGpuq for the neighbourhood of a vertex u P V in G. More generally, for a subset U Ď V we set


NGpUq “ č

Npuq

uPU

for the joint neighbourhood of U. For simplicity we may suppress G in the subscript and for sets tu1,...,uru we may write Npu1,...,urq instead of Nptu1,...,uruq. We will use the following result from [5, Lemma 3.1].

Proposition 5.1. For every integer k ě 0 and ε ą 0 the following holds for every n-vertex graph G “ pV,Eq with δpGq ě pk`k1 `εqn. For every j P rk `1s and every J P `Vj˘

we have

k ` 1 ` jε˙n. (5.1) Furthermore, for j P rks the induced subgraph GrNpJqs satisﬁes

|NpJq| ě ˆ

k ` 1 ´ j

k ´ j ` 1 ` ε˙|NpJq| (5.2) for every J P `Vj˘

δpGrNpJqsq ě ˆ

k ´ j

.

- 5.2. The decomposition. We begin with a crucial decomposition of the m-path into two subgraphs.


- Deﬁnition 5.2. For r ě 2, two sequences of vertices áv “ pv1,v2,...,vrq and uá “


- pu1,u2,...,urq of a graph G are said to be r-bridged if each vi is adjacent in G to all u1,u2,...,ui, i “ 1,2,...,r, or, equivalently, if each ui is adjacent in G to all vi,vi`1,...,vr, i “ 1,2,...,r. We then also say that the two sequences form an r-bridge, or just a bridge if the value of r is clear from the context.


The ﬁrst ingredient of the decomposition consists of a number of cliques tied together by bridges to form a linear structure resembling a braid.

- Deﬁnition 5.3. For t ě 1, ě 2, and 1 ď r ď , let Bp ,r,tq be the braid graph consisting of t vertex-disjoint -cliques Kp1q ,Kp2q ,...,Kptq , with vertices ordered arbitrarily, where for each i “ 1,...,t ´ 1, the last r vertices of Kpiq and the ﬁrst r vertices of Kpi`1q are r-bridged. For any s ě 1, we denote by sBp ,r,tq, the union of s vertex disjoint copies of Bp ,r,tq.

Note that Bp ,r,tq has t  vertices and t

`

2

˘ ` pt ´ 1q`r`1

2

˘

edges. Also, for r P t ´ 1, u,

Bp ,r,tq “ Pt r, while Bp ,1,tq consists of t cliques K connected together by t ´ 1 disjoint edges.

The second component of the decomposition involves the notion of the blow-up.

- Deﬁnition 5.4. For a graph F “ pV,Eq with V “ tv1,...,vhu, the pt1,...,thq-blow-up of F is a graph Fpt1,...,thq obtained from F by replacing each vertex vi by a set Ui of


ti vertices and each edge tvi,vju by the complete bipartite graph Kt

i,tj on Ui Y Uj. If t1 “ ... “ th “ t then we call such a graph the t-blow-up of F and denote it by Fptq.

Throughout we will use the convention that if a k-path Phk has its vertex set listed as a sequence pv1,...,vhq, then we list the vertices of its blow-up Phkptq so that all vertices of U1 precede (in any order) all vertices of U2, which precede all vertices of U3, etc.

uá1 uá2 uá3 uá4 uá5 uá6 uá7 uá8 uá9

uá1

uá4

uá7

uá2

uá5

uá8

uá3

uá6

uá9

Figure 5.1. For k “ 2, “ 3, r “ 2, t “ 3, m “ 8, an 8-path on 27 vertices P278 can be embedded into the union of a 3-blow-up of a 2-path P92p3q and three copies of the braid graph Bp3,2,3q.

We are now ready to describe the decomposition, or, in fact, an embedding of an m-path into the union of two edge-disjoint subgraphs. Proposition 5.5. Let k,t ě 1, and m “ k  ` r, with 1 ď r ď . For any copy P of

Ppkk`1qtp q, there exists a copy B of pk `1qBp ,r,tq on V pPq, which is edge-disjoint from P, and such that one can ﬁnd a copy of the m-path Pm pk`1qt in the union of P and B, whose vertices inherit the ordering of vertices of P, i.e.

Pm pk`1qt Ď Ppkk`1qtp q Y¨ pk ` 1qBp ,r,tq. (5.3)

Moreover, for t even and C “ C2kk`2p t{2q, one can ﬁnd a copy P of Ppkk`1qtp q in C and then a copy B of pk ` 1qBp ,r,tq on V pPq, which is edge-disjoint from C and such that

C YB contains a copy of the m-path Pm pk`1qt, whose vertices inherit the ordering of vertices of P, i.e.

Pm pk`1qt Ď C2kk`2p t{2q Y¨ pk ` 1qBp ,r,tq. (5.4)

- Remark 5.6. For r P t ´ 1, u, the embedding in (5.3) is an actual decomposition, while for 1 ď r ď ´ 2, the embedding omits some of the edges of Ppkk`1qtp q.
- Remark 5.7. Observe that for two paths P and P1, there might be the same copy of B satisfying the conditions of Proposition 5.5. However, this cannot happen if the paths have diﬀerent vertex sets.


Proof of Proposition 5.5. Let áv “ pv1,v2,...,v pk`1qtq be the vertices of P “ Ppkk`1qtp q. Consider the decomposition of áv of the form áv “ puá1,uá2,...,uápk`1qtq, where each uái, i “ 1,2,...,pk ` 1qt, is a segment of áv of length . With a small abuse of notation we will treat uái either as a sequence, or as a set, depending on the context.

Now, for each i “ 1,2...,k`1, consider a subsequence ávpiq “ puái,uái`pk`1q,...,uái`pt´1qpk`1qq

of áv. Let Bi be the copy of Bp ,r,tq on ávpiq in that ordering. In particular, each segment uáj induces a copy of K in Bi and any two segments uáj and uáj`pk`1q in Bi are r-bridged. Note also that the vertices of ávpiq form an independent set in P, hence the graph Bi is edge-disjoint from P. Now put B “ B1 Y ... Y Bk`1. Since for any 1 ď i ă i1 ď k ` 1, ávpiq and ávpi1q are disjoint, the graphs Bi and Bi1 are vertex-disjoint and B is a copy of pk ` 1qBp ,r,tq, which is edge-disjoint from P.

In order to ﬁnish the proof of (5.3) it is enough to show that any vertex in áv is connected in P ¨YB with m consecutive vertices. To this end, take a vertex vi `j, where 0 ď i ď pk`1qt´1 and 1 ď j ď , and note that vi `j P uái`1. Then vi `j is connected in B with ´ j vertices vi `j`1,...,vi ` P uái`1, as uái`1 induces in B a clique K . Moreover, since in P the sets uái`1,uái`2,...,uái`k`1 induce a complete pk ` 1q-partite graph, vi `j P uái`1 is connected in P with k  vertices from uái`2,...,uái`k`1, that is with vpi`1q `1,vpi`1q `2,...,vpi`kq ` . If ´ j ě r, then the above two groups of vertices give us ´ j ` k  ě m consecutive neigbours. Otherwise, for the last m ´ k  ´ p ´ jq vertices, the connections are given by the edges of the r-bridge between uái`1 and uái`k`2 in B. For an illustration of (5.3) see Fig.5.1.

- To prove (5.4), let W1,W2,...,W2k`2 be the partition classes of C. Split each Wi,


i “ 1,2,...,2k ` 2, into t{2 subsets of size and order them arbitrarily into segments uái,uái`2k`2,...,uái`pt{2´1qp2k`2q. Put áv “ puá1,uá2,...,uátpk`1qq and note that this gives us the ordering of the desired graph P. Indeed, each of the segments uái is an independent set in C of size . Moreover, for any two segments uái and uáj, with 1 ď i ă j ď tpk `1q, j ´i ď k, uái and uáj induce in C a complete bipartite graph. As for the rest of the proof, one can repeat the construction of B as in the case (5.3). Note that for each i “ 1,2...,k ` 1, the subsequence ávpiq “ puái,uái`pk`1q,...,uái`pt´1qpk`1qq forms an independent set in C, since it contains only the vertices of “antipodal” partition sets of C, i.e. of Wi and Wi`k`1. Thus,

- B and C are edge-disjoint and the rest of the proof goes along the same line as the proof of (5.3). For an illustration of inclusion (5.4) see Fig.5.2 and Fig.5.3.


## 5.3. An application of Janson’s Inequality. Here we apply Theorem 2.2 to the graph

pk ` 1qBp ,r,tq deﬁned in the previous subsection. Recall that functions ΨG and ΦG are deﬁned in Section 2.

W6

- W4
- W5


- W1
- W2


W3

W6

- W4
- W5


- W1
- W2


W3

- Figure 5.2. For k “ 2,  “ 3,r “ 1,t “ 6,m “ 7, the blow-up C62p9q (on the left) contains a copy of a path P182 p3q (on the right) which is rolled up around the cycle.

W4 uá4 uá10 uá16 uá13 uá7 uá1 W1

- Figure 5.3. Between any two “antipodal” partition classes of C62p9q there is a copy of the braid graph Bp3,1,6q.


Proposition 5.8. Let τ ą 0, ě rpr ` 1q ě 2 and p ě Cn´2{ , where C ě 1. Further, let B “ pk ` 1qBp ,r,tq, F be a subgraph of B containing K , and F be a family of at least τnv

F copies of F in Kn. Let X be the number of copies of F belonging to F which are present in Gpn,pq. There exists a constant c “ cF such that

PpX ď τΨF{2q ď expt´τ2cCnu.

Proof of Proposition 5.8. We are going to show that ΦF ě ΦB ě Cn, where the ﬁrst inequality is trivial. This, in view of Theorem 2.2, implies Proposition 5.8 with c “ p8¨4eF

q´1. We begin with a purely structural result.

Given a graph G with eG ě 2, let dG “ e

1 “ 0. Then, deﬁne mG “ max

vG´1 and set dK

G

dH. We claim that under the assumption ě rpr ` 1q,

HĎG

. (5.5)

mB “ dK “ 2

- To prove (5.5), let B1 have the largest number of vertices among all subgraphs of B which achieve the maximum in the deﬁnition of mB. It is easy to check that B1 is connected and thus B1 Ď Bp ,r,tq. Indeed, in general, if G1 and G2 are two vertex-disjoint graphs, then


1 ` eG

1 ` eG

eG

eG

eG

2 ´ 2 ď max

i ´ 1 “ max

2

2

1YG2 “

2 ´ 1 ă

i

dG

dG

.

1 ` vG

1 ` vG

1ďiď2

1ďiď2

i

vG

vG

vG

Let Kp1q,...,Kptq Ď be the -cliques of Bp ,r,tq as deﬁned in Deﬁnition 5.3. Let B1 intersect some t1 of them, respectively, in si

vertices. Our goal is to show that

,...,si

1

t1

dB1 ď {2, or equivalently, eB1´ 2pvB1´1q ď 0. Note that B1 intersects at most t1´1 bridges, each in at most

`r`1

˘

j ď and rpr ` 1q ď , implies that

edges. This, together with inequalities si

2

˜

¸

˙ ` pt1 ´ 1qˆ

˙ ´ 2

ˆ

ÿt1

ÿt1

r ` 1 2

si

eB1 ´ 2pvB1 ´ 1q ď

j ´ 1q ` pt1 ´ 1q

ď 0,

psi

j

2

j“1

j“1

which proves (5.5). Finally,

´np

¯v

H´1

eH vH´1

H´1pe

q ě C {2n ě Cn,

ΦB “ min

ΨH “ nmin

“ nmin

nv

ě npnpm

H

B

HĎB,eHą0

H

H

eH vH´1

ě C {2 ě 1.

where the ﬁrst inequality uses the bounds vH ě 2 and np

ě npm

B

- 5.4. Subgraphs in dense graphs and hypergraphs. In this subsection we quote several extremal results which guarantee the presence of copies of a given subgraph in a dense graph or hypergraph. The ﬁrst of them is the following supersaturation result of Erdős and Simonovits from [7]. Recall that χpFq denotes the chromatic number of a graph F.


- Lemma 5.9 ([7]). Let k ě 3 and F be a graph with chromatic number χpFq “ k. For every ε ą 0 there exist β ą 0 and n0 such that if a graph G with n ě n0 vertices has at


least ˆ

k ´ 2 k ´ 1 ` ε˙ˆ

˙

n 2

- edges, then G contains at least βnv


F copies of F.

A related result we are going to use in Section 8 was proved by Alon and Yuster in [1]. For graphs G and F, we say that G has an F-factor if G contains tvG{vFu vertex-disjoint copies of F.

Theorem 5.10. For every ε ą 0 and for every graph F there exists a T0 “ T0pε,Fq such that for every T ě T0, any graph G with T vertices and with minimum degree δpGq ě p1 ´ 1{χpFq ` εqT has an F-factor.

As our proof of Covering Lemma 4.4 is based on the Regularity Method, we need the following two well-known results. The ﬁrst of them is a version of Szemerédi’s Regularity Lemma [13] (see also Section 7.2 in [5]). For two real numbers δ ą 0 and d P r0,1s, given a graph G and two nonempty disjoint sets A,B Ď V pGq, we say that the pair pA,Bq is pδ,dq-quasirandom if for all X Ď A and Y Ď B the inequality

ˇepX,Y q ´ d|X||Y |ˇ ď δ|A||B|

holds, where epX,Y q is the number of edges with one endpoint in X and the other in Y . The pair pA,Bq is δ-quasirandom if it is pδ,dq-quasirandom for d “ epA,Bq{|A||B|. This last quantity is called the density of the pair pA,Bq in G. In Section 8 we will need the following simple observation the proof of which is left as an exercise.

Fact 5.11. If pA,Bq is a δ-quasirandom pair in G and A1 Ă A, B1 Ă B, with |A1| ě α|A|, |B1| ě β|B| for some α,β ą 0, then pA1,B1q is δ1-quasirandom in G with δ1 “ αβ2δ .

- Lemma 5.12 (Szemeredi’s Regularity Lemma, [13]). Given δ ą 0 and T0 P N there exists an integer T1 “ T1pδ,T0q such that every graph G “ pV,Eq on n ě T0 vertices admits a partition

V “ V0 ¨Y V1 ¨Y ... ¨Y VT of its vertex set such that

- (i) T P rT0,T1s, |V0| ď δ|V |, |V1| “ ... “ |VT|, and
- (ii) for every i P rTs the set tj P rTs tiu : pVi,Vjq is not δ-quasirandomu has size at most δT.


A partition guaranteed by the above lemma will be referred to as δ-quasirandom. Once a quasirandom partition is established, one can easily count copies of a given subgraph in it.

- Lemma 5.13 (Counting Lemma). Let F be a graph with vertex set rfs and let G be another graph with vertex partition V pGq “ V1 ¨Y ... ¨Y Vf such that pVi,Vjq is a δ-quasirandom pair


whenever ij P F. Then the number of ordered copies of F in G, i.e. the number of f-tuples

- pv1,...,vfq P V1 ˆ ... ˆ Vf such that vivj P G whenever ij P F, equals ˜


dij ˘ eFδ¸ f

ź

ź

|Vi|,

i“1

ijPF

where dij “ epVi,Vjq{|Vi||Vj|.

The last two results quoted in this section deal with h-uniform hypergraphs (or h-graphs, for short) which are collections of h-element sets on a given vertex set (for h “ 2 these are just graphs). The ﬁrst one comes from [6] (see Corollary on page 188). An h-graph H is h-partite if its vertex set can be partitioned into sets V1 Y ... Y Vh in such a way that for every edge e we have |e X Vi| “ 1 for each 1 ď i ď h. Let Khphqpqq denote the h-partite complete h-graph. Note that the number of edges of Khphqpqq is qh.

- Lemma 5.14 ([6]). For all h,q ě 2 and all w ě w0ph,qq, if H is an h-partite h-graph with each partition set of size w, and with at least

3hhh w1{qh´1 wh

edges, then H contains a copy of Khphqpqq with q vertices in each partition class.

In [11, Lemma 8] a counting extension of Lemma 5.14 has been deduced from the proofs in [6]. Here we quote this result with respect to unordered copies.

- Lemma 5.15 ([11]). For all integers h ě 2 and q ě h ` 1 and every d ą 0 there exist τ ą 0 and n0 such that for every h-graph H on n ě n0 vertices with eH ě dnh, there are at least τnhq copies of Khphqpqq in H.


This lemma has a very useful consequence for graphs. Recall Deﬁnition 5.4 and observe that for all ui P Ui, i “ 1,...,h, the subgraph of Fpt1,...,thq induced by tu1,...,uhu is isomorphic to F. If t1 “ ... “ th “: q, then we denote by FpFpqqq the family of all qh such subgraphs.

Corollary 5.16. For every integer q ě 2, real d ą 0, and a graph F there exist τ ą 0 and n0 such that the following holds. Let G be a graph on n ě n0 vertices and let F be a family of copies of F contained in G of size |F| ě dnv

F copies F1pqq of the q-blow-up Fpqq of F such that FpF1pqqq Ď F.

F. Then G contains at least τnqv

Proof. Let V pFq “ tv1,...,vhu. Consider an auxiliary h-uniform hypergraph H on the vertex set V pGq, where each edge corresponds to a copy F1 P F. Take a random partition Π “ V1 Y V2 Y ... Y Vh of V pGq, where each vertex chooses its vertex class independently

with probability 1{h. Let HΠ be the (random) h-partite subhypergraph of H consisting of only those edges of H which correspond to the copies of F P F with vi P Vi, i “ 1,...,h. Observe that Ep|HΠ|q “ h1h|H|, hence, there exists a partition Π0 for which |HΠ0| ě h1h|H|. Notice that |HΠ0| ě d1nh, where d1 “ h´hd. By Lemma 5.15 applied to H :“ HΠ0

, for some

τ ą 0 there are at least τnqh copies of Khphqpqq in H. Note that each such copy corresponds to a copy F1pqq of the q-blow-up Fpqq of F in G. By the construction of H, we do have FpF1pqqq Ď F.

- 5.5. Interlacing sequences. Here we prove a technical result which turns out to be crucial in establishing the existence of many connectable m-tuples when proving Lemmas 4.3 and 4.4.


- Deﬁnition 5.17. For a graph G, we say that a sequence px1,...,xk`1q P V pGqk`1 interlaces with a sequence py1,...,yk`1q P V pGqk`1, if


@i “ 1,...,k ` 1 : yi P NGpxi,...,xk`1,y1,...,yi´1q.

Remark 5.18. The above deﬁnition and Deﬁnition 4.1 are related via the notion of blow-up. Indeed, if each xi, i “ 1,...,k, from Deﬁnition 5.17 is blown-up to a set Xi1 “ txpi1q,...,xpi qu, while xk`1 to a set Xk1`1 “ txpk1`q1,...,xpkr`q1u, then each sequence consisting of one element from each set Xi1 interlaces with py1,...,yk`1q and, consequently, the sequences xá “ pxp11q,...,xp1 q,...,xpk1q,...,xkp q,xkp1`q1,...,xpkr`q1q and py1,...,yk`1q satisfy the condition in Deﬁnition 4.1. Hence, the subsequent technical result can be viewed as a tool for creating ξ-connectable m-tuples.

Proposition 5.19. For every k ě 1, ε ą 0, and s, there is t and ξ ą 0 such that the following holds. For every n-vertex graph G with δpGq ě `k`k1 ` ε

˘

n and for every sequence of disjoint sets X1,...,Xk`1 in V pGq of sizes |Xi| “ t, i “ 1,...,k ` 1, there exist subsets Xi1 Ă Xi of sizes |Xi1| “ s, i “ 1,...,k ` 1, and a set Y Ă V pGqk`1 of size |Y | “ ξnk`1 such that every px1,...,xk`1q P X11 ˆ ... ˆ Xk1`1 interlaces with every py1,...,yk`1q P Y . Consequently, every sequence of vertices consisting of elements of X11, followed by elements of X21, ..., followed by elements of Xk1, followed by r elements of

Xr1`1 is ξ-connectable in G.

Proof. Let us choose constants t,tp1q,...,tpkq satisfying

t " tp1q " ... " tpkq " tpk`1q :“ s.

We are going to prove by induction on j “ 1,...,k ` 1 the following statement: Dξj ą 0, Y pjq Ă V j, |Y pjq| ě ξjnj, DXipjq Ă Xi, |Xipjq| ě tpjq, i “ 1,...,k ` 1, such that @py1,...,yjq P Y pjq, px1,...,xk`1q P X1pjq ˆ ... ˆ Xkpj`q1 (5.6) @i “ 1,...,j : yi P Npxi,...,xk`1,y1,...,yi´1q.

Clearly, for j “ k ` 1 this is the statement of Proposition 5.19 with Xi1 “ Xipk`1q, i “ 1,...,k ` 1, Y “ Y pk`1q and ξ “ ξk`1.

We begin with j “ 1. Let T1 “ X1 ˆ ... ˆ Xk`1 and t1 “ |T1| “ tk`1. For any sequence px1,...,xk`1q P T1, using (5.1) with J “ tx1,...,xk`1u, there are at least εn vertices in NGpx1,...,xk`1q. Consider an auxiliary bipartite graph B between sequences xá “ px1,...,xk`1q P T1 and vertices y1 P V , where an edge is drawn if y1 P NGpx1,...,xk`1q. It is easy to show by a double counting argument that at least 12εn vertices y1 satisfy degBpy1q ě 12εt1. Indeed, otherwise, we would have

˘ “ εnt1, a contradiction. Denote the set of such vertices by Y1.

εt1n ď |B| ă `1

˘ ˆ t1 ` n ˆ `1

2εn

2εt1

By the Pigeonhole Principle, there exists a subset Y p1q Ă Y1, |Y p1q| ě ξ1n, where ξ1 “ 12ε{` t

˘

, and a family X1 Ď T1 of vectors xá, |X1| “ 12εt1, such that for all y1 P Y p1q and all xá P X1, we have y1 P NGpxáq.

1 εt1{2

The family X1 can be viewed as a pk ` 1q-partite pk ` 1q-uniform hypergraph. Now we are going to apply Lemma 5.14 to H :“ X1 with h :“ k ` 1, q :“ tp1q, and w :“ t. To this end we choose

t ě max #w0pk ` 1,tp1qq,ˆ

˙ptp1qqk+,

2p3pk ` 1qqk`1 ε

where the second parameter guarantees that X1 is large enough so as to satisfy the assumptions of Lemma 5.14. Hence, X1 contains a pk ` 1q-uniform clique Kkpk``11qptp1qq. Let Xip1q, i “ 1,...,k ` 1, be the vertex classes of that clique. This completes the proof of the base step j “ 1.

Now assume that (5.6) is true for some j, 1 ď j ď k. We will deduce that it is also true for j ` 1. For each sequence

yá “ py1,...,yjq P Y pjq, consider an auxiliary bipartite graph B :“ Bpyáq between sequences pxj`1,...,xk`1q P Tj`1, where Tj`1 “ Xjp`jq1 ˆ ... ˆ Xkpj`q1, and vertices yj`1 P V , where an edge is drawn if yj`1 P NGpxj`1,...,xk`1,y1,...,yjq. Set tj`1 “ |Tj`1| “ ptpjqqk`1´j.

Since, again by (5.1), |NGpxj`1,...,xk`1,y1,...,yjq| ě εn, for all xi P Xipjq, i “ j `

- 1,...,k ` 1, the degree of pxj`1,...,xk`1q in B is at least εn. Thus, by a similar double counting argument as in case j “ 1, there are at least 12εn vertices yj`1 P V with degBpyj`1q ě 12εtj`1. Denote the set of such vertices by Yj`1. Consequently, by the Pigeonhole Principle, there is a subset Yj1`1 Ă Yj`1, |Yj1`1| “ ξj1`1n, for some ξj1`1 ą 0, and a family Xj`1 Ď Tj`1 of vectors xá “ pxj`1,...,xk`1q, |Xj`1| “ 12εtj`1, such that for all yj`1 P Yj1`1 and all xá P Xj`1, we have yj`1 P NGpxj`1,...,xk`1,y1,...,yjq.


We apply Lemma 5.14 to Xj`1 with h :“ k ` 1 ´ j, q :“ tpj`1q and w :“ tpjq obtaining, for tpjq suﬃciently large with respect to tpj`1q, that Xj`1 contains a clique Kpyáq :“ Kkpk``11´´jjqptpj`1qq. (Note that for j “ k Lemma 5.14 degenerates to singletons and we just take Kpyáq “ Xk`1.) Recall that Kpyáq and Yj1`1 :“ Yj1`1pyáq depend on yá “ py1,...,yjq. Owing to the ﬁniteness of Xj`1, we can still select a subset Y˜pjq Ă Y pjq with |Y˜pjq| ě ξ˜jnj and a clique K Ď Xj`1 such that for all yá P Y˜pjq, we have Kpyáq “ K. Let Xjp`j`11q,...,Xkpj``11q be the partition classes of K. Additionally, let X1pj`1q “ X1pjq,...,Xjpj`1q “ Xjpjq. The sequence X1pj`1q,...,Xkpj``11q together with the set

Y pj`1q “ tpy1,...,yj`1q : py1,...,yjq P Y˜pjq, yj`1 P Yj1`1py1,...,yjqu

and constant ξj`1 “ ξ˜j ˆ ξj1`1, satisfy (5.6) for j ` 1. Note that |Y pj`1q| ě ξj`1nj`1. This completes the inductive proof of (5.6) and, thus, of Proposition 5.19.

§6. Connecting and Reservoir

Here we prove Lemma 4.2, but ﬁrst we formulate the Connecting Lemma which will be used inside the proof of Absorbing Lemma in the next section. Both lemmas proved in this section utilize yet another connecting lemma, Lemma 6.1 below, proved as Lemma 4.1 in [5], where, for convenience, k-walks instead of k-paths are considered. Formally, by a

- k-walk in a graph G we mean a sequence of not necessarily distinct vertices but such that any k ` 1 consecutive vertices are distinct and form a clique in G.


- Lemma 6.1 ([5]). For every integer k ě 1 and ε ą 0 there exists some ą 0 such that


every n-vertex graph G with δpGq ě pk`k1 ` εqn satisﬁes the following property.

For all pairs of disjoint k-tuples x,á xá1 which induce cliques in G, the number of k-walks connecting xá and xá1 with k internal vertices is at least  n

k, where k “ pk ` 1qp2k`1 ´ 2q. The Connecting Lemma is, in a sense, a simpler version of Lemma 4.2, where no reservoir

set R is put aside.

Lemma 6.2 (Connecting Lemma). For every ε ą 0 there exists ξ ą 0 such that for suﬃciently large C “ Cpε,ξq, every n-vertex graph G with δpGq ě `k`k1 ` ε

˘

n, and p “ ppnq ě Cn´2{ , a.a.s. H “ G Y Gpn,pq has the following property.

Let m “ k  ` r, with ě rpr ` 1q ě 2. For every subset Z Ď V with |Z| ď ξn{p2pk ` 1qq and every pair of disjoint ξ-connectable m-tuples x,á xá1 which induce cliques in G, there exists an m-path connecting xá and xá1 with pk ` 1q2k`1 internal vertices, all from V Z.

Proof. Let and k be as in Lemma 6.1. Choose ξ ď {p2p2k`1 ´2qq. Let xá “ px1,...,xmq, xá1 “ px11,...,x1mq be ξ-connectable m-tuples. Fix Z Ď V with |Z| ď ξn{p2pk ` 1qq and put L “ k `2pk `1q “ pk `1q2k`1. We will ﬁrst show that there are ΩpnLq k-walks in G with L internal vertices, all avoiding Z, that connect xá to xá1. (Formally, we connect the last k vertices of xá with the last k vertices of xá1, so, with some abuse of terminology, internal vertices are precisely those which are disjoint from the set tx1,...,xm,x11,...,x1mu.)

Indeed, consider ordered pk ` 1q-cliques yá “ py1,...,yk`1), yá1 “ py11,...,yk1`1q, as in Deﬁnition 4.1, corresponding, respectively, to xá, xá1 which are disjoint from Z. There are at least

1 4

`

˘2 ě

ξnk`1 ´ pk ` 1q|Z|nk

ξ2n2k`2, of them, since |Z| ď ξn{p2pk ` 1qq.

By Lemma 6.1, applied to the k-tuples yá´ “ py2,...,yk`1q and yá´1 “ py21,...,yk1`1q, there exist

- 1

- 2


k´1 ě

´ kp|Z| ` 2mqn

 n

 n

,

k

k

k-walks connecting yá´ and yá´1 , with k internal vertices, all omitting Z, xá, and xá1. Thus, altogether we have 18ξ2 nL k-walks connecting xá to xá1, with L internal vertices, all omitting Z. Consequently, at least

1 10

1 8

ξ2 nL ´ OpnL´1q ě

ξ2 nL

of them are k-paths. Let P be the family of all such k-paths and Pint the family of the sub-k-paths of the k-paths in P spanned by the L internal vertices.

By Corollary 5.16 with d “ 101 ξ2 , F “ PLk, G “ GrV Zs, and F “ Pint, for some τ1 “ τ1pdq ą 0, there are at least τ1n L copies P1p q of the -blow-up PLkp q with FpP1p qq Ď Pint. We select from them at least τn L copies which have mutually distinct vertex sets, where τ “ p Lτ1q!. Let us consider a sequence of vertices áv that begins with xá, ends with the reverse of xá1, and in between consists of the  L vertices of P1p q (the order in each -independent set obtained by the blow-up is ﬁxed arbitrarily).

Notice that due to the choice of yá and yá1, and the inclusion FpP1p qq Ď Pint, each vertex of xá is already connected to the m subsequent vertices of áv and the same is true for xá1. Indeed, split the vector xá into k blocks of length and one block of length r. Then, each xi

in the jth block, j “ 1,...,k ` 1, is adjacent to m ´ i ě m ´ j  elements lying in front of it in xá plus j  elements in the -blow-ups of the ﬁrst j elements of yá (see Def. 4.1). Thus, although the sequence áv does not yet induce a full m-path, the only missing edges have all their vertices in P1p q.

By Proposition 5.5, we need to complement P1p q with a copy of B “ pk `1qBp ,r,2k`1q in Gpn,pq. For each P1p q let BP1p q be the copy of B which complements P1p q to a graph containing an m-path and let B be the family of all such BP1p q. By Remark 5.7, we have |B| ě τn L. By Proposition 5.8, there exists c “ cB ą 0 such that with probability at least 1 ´ expt´τ2cCnu, at least one of them is present in Gpn,pq, which yields the existence of an m-path connecting xá and xá1 in G Y Gpn,pq which avoids Z. As there are at most nm possibilities for the choice of each of xá and xá1 and at most 2n for Z, applying the union bound and taking C “ Cpτ,cq large enough, we conclude that a.a.s. the same it true for all choices of Z, xá, and xá1.

For the proof of Lemma 4.2, we need a modiﬁcation of the notion of connectability.

- Deﬁnition 6.3. Given k ě 1 and ξ ą 0, and a set R, an m-tuple px1,x2,...,xmq of vertices of a graph G ´ R is pR,ξq-connectable if there exist ξ|R|k`1 (ordered) copies py1,y2,...,yk`1q of Kk`1 in GrRs with the property that for each i “ 1,2,...,k ` 1, yi P NGpxpi´1ql`1,...,xmq.


- Proof of Lemma 4.2. Fix ε ą 0 and 0 ă ξ ă 1 and let :“ pε{2q be given by Lemma 6.1. Choose


γ “ mintξ2{22k`6, 2{4u. (6.1) Consider a subset R Ď V chosen at random by including each element of V to R, independently, with probability γ2. It is easy to see that a.a.s. R satisﬁes the following three properties:

- (i) 12γ2n ď |R| ď 2γ2n,

- (ii) |NGpvq X R| ě `k`k1 ` 2ε

˘|R| for every v P V , and

- (iii) every ξ-connectable m-tuple in G becomes pR,ξ{2k`2q-connectable.


Indeed, X “ |R| is binomially distributed with EX “ γ2n, so the ﬁrst property follows from Chebyshev’s inequality. Since Xv “ |NGpvq X R| is also binomial with expectation γ2|NGpvq| ě γ2pk`k1 ` εqn, the second property holds, simultaneously for all v, from Chernoﬀ’s bound (see, e.g., [8, Theorem 2.1]).

To prove (iii), we employ a standard application of Janson’s inequality (see, e.g., [8, Theorem 2.14]). Given a ξ-connectable m-tuple xá in G, let K be the family of ξnk`1 ordered copies of Kk`1 which witness the ξ-connectability of xá. Let Y :“ Yáx be the

number of K P K which are contained in R. We apply the inequality in [8, Theorem

- 2.14] to Y with t :“ 31EY . Observe that EY “ ξnk`1γ2pk`1q, while ∆ “ Opn2k`1q. Hence, PpY ď 23EY q ď expt´Ωpnqu. This is so small that a.a.s. for all choices of xá we have


- 1

- 2k`2ξ|R|k`1,


- 2

- 3


ξγ2pk`1qnk`1 ě where we also used the R-H-S of (i).

Yáx ě

For the rest of the proof of Lemma 4.2 we ﬁx one set R Ď V having the above three properties. Let us now ﬁx two ordered ξ-connectable m-tuples x,á xá1 in G ´ R as well as a subset S Ď R with |S| ď

?γ|R|. We are going to show that with probability very close to one, there is an m-path in H connecting xá and xá1 with pk ` 1q2k`1 internal vertices, all from R S.

To this end, note that due to property (iii) of R, sequences xá and xá1 are pR,ξ{2k`2qconnectable. Hence, one can extend xá to an m-path xáyá, where yá is a pk ` 1q-tuple in GrR Ss which ‘witnesses’ the pR,ξq-connectability of xá, in at least

1

- 1

- 2k`2ξ|R|k`1 ´


p6.1q

?γ|R|k`1

2k`3ξ|R|k`1 ways. We extend xá1 to xá1yá1 in a similar way.

ě

In turn, by (ii), we are in position to apply Lemma 6.1. Recalling that k “ pk ` 1qp2k`1 ´ 2q, we obtain at least

- 1

- 2 |R|


p6.1q

?γ|R|

|R|

´

ě

k

k

k

k-walks connecting yá´ and yá´1 , with k internal vertices, all belonging to R S. Thus, altogether we have at least 2´p2k`7qξ2 |R|L k-walks connecting xá to xá1, with L “ pk`1q2k`1 internal vertices, all belonging to R S. Consequently, at least 2´p2k`8qξ2 |R|L of them are k-paths.

Let P be the family of all such k-paths and Pint – the family of the sub-k-paths of the k-paths in P spanned by the L internal vertices. Similarly as in the proof of Lemma

- 6.2, by Corollary 5.16 with d “ 2´p2k`8qξ2 , F “ PLk, G “ GrR Ss, and F “ Pint, for some τ “ τpdq ą 0, there are at least τ|R| L copies P1p q of the -blow-up PLkp q with FpP1p qq Ď Pint and mutually distinct vertex sets. As in the previous proof, each such copy misses a copy of B “ pk ` 1qBp ,r,2k`1q to close an m-path between xá and xá1.


By Proposition 5.8, using also the L-H-S of (i), there exists c “ cB ą 0 such that with probability at least

1 ´ expt´τ2cC|R|u ě 1 ´ expt´τ2cCγ2n{2u, at least one of them is present in Gpn,pq. This yields the existence in G Y Gpn,pq of an

- m-path connecting xá and xá1, with  L internal vertices, all from R S. As there are at


most nm possibilities for the choice of each of xá and xá1 and at most 2n for S, applying the union bound and taking C :“ Cpτ,γ,cq large enough, we conclude that a.a.s. the same is true for all choices of S Ď R, xá, and xá1.

§7. Absorbing Path We build the absorbing path A from small blocks, called absorbers.

- Deﬁnition 7.1. Given ξ ą 0, a graph G, and a vertex v P V :“ V pGq, a 2m-tuple pxm,xm´1,...,x1,x11,...,x1m´1,x1mq P V 2m is a half-pξ,vq-absorber in G if


- (i) x1,x2,...,xm,x11,x12,...,x1m P NGpvq;
- (ii) xá “ px1,x2,...,xmq, xá1 “ px11,x12,...,x1mq are ξ-connectable in G;
- (iii) pxm,xm´1,...,x1,x11,...,x1m´1,x1mq induces in G an pr, ,..., ,rq-blow-up of a P2kk`2.


If condition (iii) is replaced by (iii)1 pxm,xm´1,...,x1,x11,...,x1m´1,x1mq induces in H “ G Y Gpn,pq an m-path,

then we call the 2m-tuple pxm,xm´1,...,x1,x11,...,x1m´1,x1mq a (full) pξ,vq-absorber. A 2mtuple which is a pξ,vq-absorber for some v P V is called a ξ-absorber.

The key observation is that if pxm,xm´1,...,x1,x11,...,x1m´1,x1mq is a pξ,vq-absorber, then pxm,xm´1,...,x1,v,x11,...,x1m´1,x1mq is an m-path (here we just need properties (i) and (iii)1, not (ii)). This allows for including (or absorbing) v into a path or cycle which contains a pξ,vq-absorber as a segment. To absorb an entire subset U of vertices, we will need many disjoint pξ,uq-absorbers for each u P U. In fact, by a simply greedy argument, at least |U| disjoint pξ,uq-absorbers per each vertex u would suﬃce.

The next result asserts that for some ξ ą 0 there are many half-pξ,vq-absorbers for every v P V pGq.

- Proposition 7.2. For every ε ą 0 there exist ξ ą 0 and β1 ą 0 such that if G is an


- n-vertex graph with δpGq ě pk`k1 ` εqn, then, for every v P V pGq, there are at least β1n2m half-pξ,vq-absorbers.


Proof. Fix ε ą 0. Let β be given by Lemma 5.9. We are also going to apply Proposition 5.19 with s :“ ; let t and ξ be the resulting constants. Finally, let

β1 “ βpk`k1 ` εqp2k`2qt. By (5.2), for every v,

k ´ 1 k ` ε˙|Npvq|

δpGrNpvqsq ě ˆ

which implies that

epGrNpvqsq ě ˆ

k ´ 1 k ` ε˙ˆ|Npvq| 2

˙.

Since χpP2kk`2q “ k ` 1, we also have χpP2kk`2ptqq “ k ` 1, where P2kk`2ptq is the t-blow-up of the k-path P2kk`2 on 2k ` 2 vertices. Thus, by Lemma 5.9, GrNpvqs contains at least

β|Npvq|p2k`2qt ě β1np2k`2qt

copies of P2kk`2ptq. Fix one such copy and let Xk`1,...,X1,X¯1,...,X¯k`1 be its vertex classes. By two applications of Proposition 5.19 (with s “ ), one to Xk`1,...,X1, the other to X¯1,...,X¯k`1, we obtain subsets Xk1`1,...,X11,X¯11,...,X¯k1`1 Ď V and two sets of pk ` 1q-tuples Y,Y¯ Ď V k`1 such that

- (1) |Xi1| “ |X¯i1| “ for i “ 1,...,k while |Xk1`1| “ |X¯k1`1| “ r (we delete arbitrary ´r vertices from the pk ` 1q-st subset guaranteed by Proposition 5.19);
- (2) |Y |,|Y¯| ě ξnk`1;
- (3) every px1,...,xk`1q P X11 ˆ...ˆXk1`1 interlaces with every py1,...,yk`1q P Y as well as every px¯1,...,x¯k`1q P X¯11 ˆ ... ˆ X¯k1`1 interlaces with every py¯1,...,y¯k`1q P Y¯.


To ﬁnish the proof, consider ﬁrst an m-tuple xá consisting of all the vertices of X11,...,Xk1`1, in this order. By Proposition 5.19 (see also Remark 5.18), xá is ξ-connectable. By the same token, the sequence xá1 listing all the elements in sets X¯11,...,X¯k1`1 is a ξ-connectable m-tuple. Hence, pxáq´1xá1 is a half-pξ,vq-absorber. In summary, each of the β1np2k`2qt

t-blow-ups of P2kk`2 generates a half-pξ,vq-absorber. On the other hand, each of the halfpξ,vq-absorbers can be generated by at most np2k`2qt´2m such blow-ups. Thus, the assertion follows by taking the ratio of the two quantities.

Next, we analyze what is needed in order to get an m-path as in (iii)’ starting from a blow-up appearing in (iii). Let B :“ pk `1qBp ,r,2q and let B´ be the graph consisting of a copy of pk ´ 1qBp ,r,2q and two vertex disjoint copies of the disjoint union of K and Kr joined by an r-bridge, that is, B´ is obtained from B by removing ´ r vertices from two cliques K belonging to distinct copies of Bp ,r,2q. Given v and a half-pξ,vq-absorber xá, there is a copy of B´ which, if included in Gpn,pq, completes in H a pξ,vq-absorber on xá.

Let X be a random variable which counts the number of copies of B´ in Gpn,pq and, for any vertex v, let Xv be the number of those of them which turn a half-pξ,vq-absorber into a full pξ,vq-absorber. Notice that the number of vertices of B´ is 2m and the number of edges is 2k

`

˘ ` 2

`r

˘ ` pk ` 1q`r`1

˘

. Thus, putting

2

2

2

r`1

Ψ :“ ΨB´ “ n2mp2kp 2q`2p

2q`pk`1qp

2 q,

r

we have EX ď Ψ and EXv ě β1Ψ (cf. Proposition 7.2). Finally, let Y be the number of intersecting pairs of copies of B´ in Gpn,pq.

- Proposition 7.3. Let β1 be as in Proposition 7.2 and p “ ppnq ě Cn´2{ for suﬃciently large constant C ě 1. There exists a constant D :“ Dpk,r, q such that the following properties hold a.a.s.


- (i) X ď 2Ψ;
- (ii) Y ď DΨ2{n;
- (iii) for each v P V pGq, Xv ě 12β1Ψ.


Proof. Part (i): Since B´ is a subgraph of B containing K , by the proof of Proposition 5.8, ΦB´ “ ΨK “ n pp 2q ě Cn. By Chebyshev’s inequality

VarX pEXq2

“ Op1{ΦB´q “ op1q (see the proof of Theorem 3.4 in [8] and Remark 3.7 therein).

PpX ě 2Ψq ď PpX ě 2EXq ď Pp|X ´ EX| ě EXq ď

Part (ii) is also a consequence of Chebyshev’s inequality, but more technical as it applies to the numbers of copies of several non-isomorphic graphs (all possible unions F of pairs of intersecting copies of B´.) However, we can just quote inequality (3.22) from [8], page 76, which states that for every such F the number XF of copies of F in Gpn,pq a.a.s. satisﬁes the inequality XF ď DFΨ2{ΦvB´ for some constant DF, where ΦvB´ “ mintΦB´,nu (see also: Notes on Notation in [8, page 10]). Since ΦvB´ “ n, (ii) follows with D “ ř

F DF.

Part (iii) follows by Proposition 5.8 with τ “ β1, t “ 2, F :“ B´, and F – the family of all copies of B´ which turn a half-pξ,vq-absorber into a full pξ,vq-absorber. Then, there exists a constant c “ cB´ ą 0 such that

PˆXv ď

β1Ψ˙ ď expt´pβ1q2cCnu

- 1

- 2


and, taking C “ Cpβ1,cq large enough, (iii) follows by the union bound over all v.

Using the assumptions on p and , it can be easily checked that Ψ “ Ωpnk`1q. Thus,

- Proposition 7.3 (iii) guarantees a.a.s. ΩpΨq “ Ωpnk`1q ξ-absorbers in H. We now thin down this family to a linear size in n in a random fashion.
- Proposition 7.4. Let γ ď pβ1{24Dq2{3. Then there exists a family A1 of ξ-absorbers with the following properties:


- (i) |A1| ď 6γ3{2n;
- (ii) the number of pairs of intersecting elements in A1 is at most 81β1γ3{2n;

- (iii) for every v P V pGq, there are at least 41β1γ3{2n pξ,vq-absorbers in A1.


Proof. Put

q :“ γ3{2n{Ψ

and denote by Aq a random subfamily of ξ-absorbers which is obtained by selecting each one independently with probability q. By Proposition 7.3(i),

E|Aq| ď 2Ψq “ 2γ3{2n. Hence, by Markov’s inequality

1 3

Pp|Aq| ą 6γ3{2nq ď

.

Similarly, by Proposition 7.3(ii), the expected number of pairs of intersecting elements in Aq is at most DΨ2{n and thus the probability that their number is greater than 18β1γ3{2n can be bounded from above by

8Dγ3{2 β1 ď

1 3

pDΨ2{nqq2 β1γ3{2n{8 “

.

Finally, for a ﬁxed v P V , note that the number of pξ,vq-absorbers in Aq is binomially

distributed. Hence, by Proposition 7.3(iii), its expectation is Xvq ě 12β1Ψq “ 12β1γ3{2n. Thus, by Chernoﬀ’s bound (see, e.g., [8, Theorem 2.1]) and the union bound over all v, the probability of the opposite event to the one stated in (iii) is at most

nexpt´β1γ3{2n{8u “ nexpt´Ωpnqu ă 1{3,

for suﬃciently large n. In conclusion, the probability that properties (i)-(iii) hold for Aq is positive, and thus, there exists a family A1 of ξ-absorbers which satisﬁes all three of them.

- Proof of Lemma 4.3. Given ε ą 0, let β1 “ β1pεq be as in Proposition 7.2, and let ξ “


mintξ1,ξ2u, where ξ1 is as in Lemma 6.2, while ξ2 is as in Proposition 7.2. Further, let C be as in Lemma 6.2, D ą 0 – as in Proposition 7.3, and set

+. (7.1)

γ “ min #ˆ

˙2{3 ,

, ˆ

˙2 ,

1 p6 pk ` 1q2k`3q2

β1 40

β1 24D

ξ 2pk ` 1q

Finally, ﬁx any subset R Ă V pGq of size |R| ď 2γ2n.

In view of the discussion at the beginning of the section, it suﬃces to build an m-path containing at least 3γ2n pξ,vq-absorbers for every v P V .

Let A1 be as in Proposition 7.4. Upon removing from A1 one ξ-absorber from each intersecting pair, as well as all ξ-absorbers containing vertices from R, we obtain a family A which satisﬁes the following three conditions:

- (i) |A| ď 6γ3{2n;


- (ii) all ξ-absorbers in A are pairwise vertex disjoint;
- (iii) for every v P V pGq, there are at least 18β1γ3{2n ´ 2γ2n ě 3γ2n pξ,vq-absorbers in A1, where the last estimate follows from (7.1) and the fact that the absorbers in A1 are disjoint.


There is a routine way to create the desired absorbing m-path from A via repeated applications of Lemma 6.2. Using Lemma 6.2, we connect the ξ-absorbers in A, one by one, into one m-path A. Since each two consecutive ξ-absorbers on the m-path A are connected by a sub-m-path with pk ` 1q2k`1 internal vertices, by (7.1) and the inequality m ď pk ` 1q,

γn 2

|V pAq| ď |A| ¨ p2m ` pk ` 1q2k`1q ď 6γ3{2n pk ` 1q2k`2 ď

,

as required. In each step of the application of Lemma 6.2, the set Z of forbidden vertices consists of the initial set R, the vertices in the ξ-absorbers in A, and the vertices used for the connections so far. Hence, by (7.1), even in the last step

γn 2 ď γn ď

ξn 2pk ` 1q

|Z| ď |R| ` |V pAq| ď 2γ2n `

,

which legitimates repeated applications of Lemma 6.2. Note that the m-ends of the obtained m-path A are ξ-connectable, that is, A is ξ-connectable. Moreover, as stated in (iii), for every vertex v P V pGq the m-path A contains at least 3γ2n (disjoint) pξ,vq-absorbers. Consequently, for any set of vertices U of size |U| ď 3γ2n, one can absorb all the vertices from U into A obtaining an m-path AU with the same ends as A.

§8. Covering Lemma

Our approach is similar to the one in the proof of Proposition 2.4 in [5]. The main new diﬃculty is to secure ξ-connectable ends of the constructed m-paths. Here is an outline of the proof.

We work under the hierarchy of constants

ε " γ,ξ " T0´1,M´1,δ " T1´1," τ " C´1. (8.1)

In the ﬁrst step we will take a δ-quasirandom partition of the graph G ´ Q and show that the associated reduced graph Γ has a C2kk`2-factor (Claim 8.1 below). Then we will show that a.a.s. the subgraph of H “ G Y Gpn,pq corresponding to any copy of C2kk`2 in Γ can be almost covered by not too many vertex-disjoint ξ-connectable m-paths (Claim 8.3 below). The union of all these m-paths taken over all copies of C2kk`2 in a C2kk`2-factor of Γ will constitute the desired family of m-paths.

We begin with the deterministic part. Consider a δ-quasirandom partition

V Q “ V0 Y V1 Y ... Y VT of G ´ Q. Let Γ be the reduced graph with respect to the above partition, namely, the vertex set of Γ is rTs and, for 1 ď i ă j ď T, we include ti,ju into EpΓq whenever pVi,Vjq is a δ-quasirandom pair with density dij “ epVi,Vjq{|Vi||Vj| ě ε{3.

- Claim 8.1. For all ε,γ,δ ą 0 with γ ` δ ď ε{6, there is T0 such that for all T ě T0, there exists a C2kk`2-factor K in Γ.


Proof. Take any ε,γ,δ ą 0 with γ ` δ ď ε{6. Via Theorem 5.10 with ε :“ ε{3 and F :“ C2kk`2, choose T0 and let T ě T0. We ﬁrst show that

δpΓq ě ˆ

˙T.

ε 3

k k ` 1 `

Let us extend notation epU,Wq to intersecting sets U and W by counting twice the edges contained in U X W. In particular, for any i “ 1,...,T, epVi,V q “ ř

vPVi degGpvq. Thus, using the minimum degree condition imposed on G,

epVi,V q ě ˆ

k k ` 1 ` ε˙|Vi|n.

On the other hand, using the bound |Vi| ď n{T, the δ-quasirandomness of the partition gives that

3 ` δ¯|Vi|2 ď pγ ` δq|Vi|n `

epVi,V q ď epVi,Q Y V0q ` degΓpiq|Vi|2 ` pT ´ degΓpiqq´ε

3 ` δ¯|Vi|n. Combining these two estimates and assuming that γ`δ ď ε{6, we obtain, for all i “ 1,...,T, the lower bound

degΓpiq T |Vi|n ` ´ε

degΓpiq ě ˆ

˙T.

k k ` 1 `

ε 3

It is easy to check that χpC2kk`2q “ k ` 1. Hence, the existence of a C2kk`2-factor K in Γ follows by Theorem 5.10 applied with ε :“ ε{3, F :“ C2kk`2 and G :“ Γ, for suﬃciently large T.

Turning to the union H “ G Y Gpn,pq, we now describe an event E “ Epξ,M,τq and show that it holds for the random graph Gpn,pq a.a.s. Fix a sequence

á

X “ pX1,...,X2k`2q of disjoint subsets of V pGq and deﬁne a family Fp

á

Xq of copies of the graph B :“ pk ` 1qBp ,r,2Mq

as follows. Suppose that there is a copy of the  M-blow-up C2kk`2p Mq in G with each vertex class Ui Ď Xi, i “ 1,...,2k ` 2. Then, we include in Fp

Xq a copy B˜ of B which is given by decomposition (5.4) of Proposition 5.5 with t :“ 2M, provided that the ends of the resulting m-path Ppm2k`2q M are ξ-connectable.

á

For any τ ą 0, let J “ t

á

á

Xq| ě τnp2k`2q Mu. The event E holds if for every

X “ pX1,...,X2k`2q : |Fp

X P J there is a subgraph B˜ P Fp

Xq with B˜ Ď Gpn,pq.

á

á

- Claim 8.2. For every ξ,M,τ ą 0, there is C ě 1 such that for p ě Cn´2{ the event E holds a.a.s.

Proof. Let c “ cB˜ ą 0 be a constant resulting from Proposition 5.8 with t :“ 2M, F :“ B˜, F :“ Fp

á

Xq. Further, let C ě p2k ` 3q{pcτ2q. Suppose that J ‰ ∅, since otherwise E holds vacuously. For a given

á

X P J , let Y be the number of B˜ P Fp

á

Xq with B˜ Ď Gpn,pq. Then, by Proposition 5.8

PpY “ 0q ď PpY ď τΨB˜{2q ď expt´τ2cCnu “ op2´p2k`2qnq. Since |J | ď 2p2k`2qn, by the union bound,

Pp Eq ď 2p2k`2qn ˆ op2´p2k`2qnq “ op1q.

At the heart of the proof of Lemma 4.4 lies the following claim.

- Claim 8.3. For all ε ą 0, T, and M, there exists ξ ą 0, γ ą 0, and δ ą 0 such that for C “ Cpε,M,γq the following holds. If Γ is the reduced graph of a δ-quasirandom partition


of G ´ Q deﬁned above and K Ď V pΓq, |K| “ 2k ` 2, induces a copy of C2kk`2 in Γ, then, with VK “ Ť

iPK Vi, a.a.s. all but at most 12γ2|VK| vertices of HrVKs can be covered by vertex disjoint ξ-connectable m-paths on p2k ` 2q M vertices. Proof. Given ε ą 0, let γ,δ be as in Claim 8.1, i.e. γ ` δ ď ε{6. In addition, let δ ď

`ε

˘e

γ4

F

, (8.2)

3

16eF

and let M and T be arbitrary. Without loss of generality assume K “ r2k ` 2s. Let P be a largest collection of vertex-disjoint ξ-connectable m-paths in HrVKs, each on p2k ` 2q M vertices, with  M vertices in every Vi, i “ 1,...,2k ` 2. Let Xi Ď Vi, i P r2k ` 2s, be the subset of Vi consisting of all vertices not appearing on the m-paths in P. We have

|X1| “ ... “ |X2k`2| “ x

for some integer x. It suﬃces to prove that x ď 12γ2|Vi|. Assume that this is not the case. We will show that

á

X “ pX1,...,X2k`2q P J , which will further imply, using property E, the existence of a ξ-connectable p2k ` 2q M-vertex

- m-path with vertex set contained in X1 Y ... Y X2k`2, thus contradicting the maximality of P.


Since K “ r2k ` 2s induces a copy of C2kk`2 in Γ, each pair pVi,Vjq, with i,j lying at distance at most k on C2kk`2, is δ-quasirandom in G with density dij ě ε{3.

á

Xs with the property that each vertex is contained in distinct Xi, i P r2k ` 2s. By Fact 5.11, with α “ β “ γ2{2, the induced subgraph Gr

Let Ω1 be the family of copies of C2kk`2 in Gr

á

Xs is δ1-quasirandom with δ1 “ γ8δ4

. By Lemma 5.13 applied to F :“ C2kk`2 and G :“ Gr

á

Xs, it follows, using also (8.2), that

ě `ε

˘e

|Ω1| ě ´´ε 3¯e

´ eFδ1¯xv

F

F

3

pvFxqv

,

F

F

2vv

F

F

where eF “ p2k ` 2qk and vF “ 2k ` 2. We are about to apply Proposition 5.19 with s :“ . Let tpε, q and ξ be the resulting constants. Set t “ maxttpε, q, Mu. First we need to generate many copies of the t-blow-up of C2kk`2. By Corollary 5.16 with q :“ t,

d :“ `ε

˘e

F

3

,

2vv

F

F

á

F :“ C2kk`2, G :“ Gr

F copies of C2kk`2ptq with each vertex class contained in distinct Xi, i P r2k ` 2s. Let Ω2 be the family of all these copies. In particular, |Ω2| ě τ1pvFxqtv

Xs, and F :“ Ω1, there are, for some τ1 ą 0, at least τ1pvFxqtv

F.

Fix one member of Ω2 with vertex classes Y1,...,Y2k`2 and apply Proposition 5.19 with s :“ twice, to Y1,...,Yk`1 and to Yk`2,...,Y2k`2. This way we ﬁnd in C2kk`2ptq a copy of C2kk`2p q with vertex classes W1,...,W2k`2, Wi Ă Yi Ă Xi, i “ 1,...,2k `2, and such that the following property holds. For any m-tuple xá “ px1,...,xmq with tx1,...,xru Ď Wk`1, txr`1,...,xr` u “ Wk, ...,txm´ `1,...,xmu “ W1 and for any m-tuple xá1 “ px11,...,x1mq with tx11,...,x1ru Ď Wk`2, tx1r`1,...,x1r` u “ Wk`3, ..., tx1m´ `1,...,x1mu “ W2k`2, both xá and xá1 are ξ-connectable.

Let us extend arbitrarily this copy of C2kk`2p q to a copy of C2kk`2p Mq with vertex classes Ui such that Wi Ă Ui Ă Yi, i “ 1,...,2k ` 2 (this is possible as t ě  M). We order its vertices so that the associated copy of Ppm2k`2q M (see decomposition (5.4)) begins with

- W1,...,Wk`1 and ends with Wk`2,...,W2k`2, so that its ends are ξ-connectable.


á

X] as above. We just showed that every member of Ω2 gives rise to at least one member of Ω3. On the other hand, each member of Ω3 can be obtained from at most xv

Let Ω3 denote the family of all copies of C2kk`2p Mq in Gr

Fpt´ Mq members of Ω2. Thus, using the

bound |Vi| ě p1 ´ δqn{T ě n{p2Tq, the assumption x ě 12γ2|Vi|, and setting τT :“ τ1vtv

F pγ2{4Tqv

F M, (8.3)

F

we have

τ1pvFxqtv

F

|Ω3| ě

xvFpt´ Mq “ τ1vtv

F xv

F M ě τTnv

F M,

F

á

and so

X P J . Let C “ CpτTq be as in Claim 8.2. Then, a.a.s. the property E holds, meaning that there is at least one copy of B in Gpn,pq which, together with a copy of C2kk`2p Mq from Ω3, induces a ξ-connectable p2k ` 2q M-vertex m-path in

- X1 Y ... Y X2k`2.


- Proof of Lemma 4.4. We begin by choosing constants as required implicitly by the preceding claims. Given ε, let γ ď ε{12 and M be so large that


pp2k ` 2q Mq´1 ď γ3. (8.4)

Further, let ξ “ ξpε, q be as in Proposition 5.19. Next, choose an integer

*,

T0 “ max "T0pε{3,C2kk`2q,

4p2k ` 1q γ2

where T0pε{3,C2kk`2q is as in Theorem 5.10, and a constant δ ą 0 with δ ď γ2{4 satisfying (8.2). Let T1 “ T1pδ,T0q be given by Lemma 5.12. Finally, take τ “ τT

as in (8.3) and C “ Cpτq as in Claim 8.2.

1

Apply the Szemerédi Regularity Lemma (Lemma 5.12) to H Q with δ and T0 to obtain a partition V Q “ V0 ¨Y V1 ¨Y ... ¨Y VT, with T0 ď T ď T1. Let Γ be the reduced graph with respect to that partition. By Claim 8.1 there exists a C2kk`2-factor K covering all but at most 2k ` 1 vertices of Γ. Applying Claim 8.3 to each C2kk`2 in K, we obtain a global family P of vertex disjoint ξ-connectable m-paths in H Q, each having exactly p2k ` 2q M vertices, covering all but at most

ˆδ `

γ2˙n ď γ2n

2k ` 1 T0 `

- 1

- 2


vertices of V Q (Here we use our assumptions on δ and T0). Moreover, the number of the paths in P can be bounded from above by p2k`n2q M which, by (8.4), is at most γ3n.

§9. Concluding remarks

Recall that the ﬁrst case not covered by Corollary 1.4 is k “ 1 and m “ 5. We will see below that in this case the threshold, as deﬁned in Deﬁnition 1.1, does not exist. The reason is that the range of p “ ppnq depends on α not only through the constant C but also through the exponent of n. We believe that in many other cases the same is true as well. First, let us focus on the lower bound. For convenience, we switch from α to ε “ α ´ 12.

- Claim 9.1. For each 0 ă ε ă 1{9 there exists a constant c1 “ c1pεq ą 0 and a sequence of

n-vertex graphs Gε :“ Gεpnq such that δpGεq ě `1

2 ` ε

˘

n and for all p ď n´1{2´c1

nlimÑ8P

`

Gε Y Gpn,ppnqq P Cn5

˘ “ 0.

Proof. Fix 0 ă ε ă 1{9 and deﬁne c1 “ 2´918ε ε. Let p “ opn´1{2´c1q. Since p “ opn´1{2q, by Markov’s inequality the number of copies of K4 in Gpn,pq is a.a.s. opnq. Now consider the graph Gε :“ G1{2`ε as described in the proof of Theorem 1.3. Assume that H “ GεYGpn,pq contains a copy C of Cn5. After removing from H all vertices in W1 Y W2 as well as at least one vertex of each copy of K4 from Gpn,pq we obtain a subgraph H1 Ă H on n´2εn´opnq vertices. Observe that H1 X C contains a 5-path P of length n{p2εn ` opnqq ě 31ε. As in the proof of Theorem 1.3 one can show that Gpn,pq X P contains a 2-path Q on q ě 61ε vertices. Observe that Q has exactly 2q ´ 3 edges. Since

q 2q ´ 3 “

- 1

- 2 `


3

4q ´ 6 ď we have p “ opn´q{p2q´3qq and, hence, Markov’s inequality yields that a.a.s. Gpn,pq contains no 2-path on q vertices, a contradiction.

- 1

- 2 ` c1,


For the upper bound it only follows from Theorem 1.2 applied with k “ 1, “ 4 and r “ 1 that the threshold is Opn´1{2q. It turns out that representing m “ 5 diﬀerently (k “ 1, “ 3 and r “ 2) and taking a similar approach as in the proof of Theorem 1.2 one can show a better bound.

- Claim 9.2. For each ε ą 0 there exists a constant c2 “ c2pεq ą 0 such that for all p ě n´1{2´c2


˘ “ 1, where the minimum is taken over all n-vertex graphs G with δpGq ě `1 2 ` ε

`

G Y Gpn,ppnqq P Cn5

nlimÑ8min

P

G

˘

n.

Proof of Claim 9.2 (outline). The key to the improvement of the bound on p “ ppnq is a reformulation of Proposition 5.8 which yields the same bound PpX ď τΨF{2q ď expt´Ωpnqu under milder assumptions on p. This is because now mB “ dBp3,2,tq “ 63tt´´31 ă 2.

In fact, it is true in more generality that for ě 2 and r “ ´1 (in which case Bp ,r,tq “ Pvr, v “ t ), for any H Ď Bp ,  ´ 1,tq “ Pvr, setting v1 “ vH,

v1p ´ 1q ´ `

˘ v1 ´ 1 ď

vp ´ 1q ´ `

˘ v ´ 1 “ dP ´1

2

2

dH ď dP ´1

“

.

v1

v

This means that taking p “ Cn´1{m

“ Cn´1{2`1{p6p2t´1qq for suﬃciently large t (in fact, one should take t “ 2M, where M is deﬁned in Section 8) one can repeat every step of the proof of Theorem 1.2.

B

Determining the exact “threshold” for Cn5 is left for the future work.

Finally, let us emphasize that throughout this paper we have always assumed that k ě 1. There are some analogous results when k “ 0, i.e., assuming only that the minimum degree is a small fraction of n. It is known [2] that d0,1pnq “ n´1 and, in general, as it was shown in [3] that d0,m “ opn´1{mq for m ě 2. Determining the exact “threshold” for m ě 2 is still open.

Acknowledgments. We are very grateful to both referees for their valuable remarks which have led to a better presentation of our results.

References

- [1] N. Alon and R. Yuster, H-factors in dense graphs, J. Combin. Theory Ser. B 66 (1996), no. 2, 269–282, DOI10.1006/jctb.1996.0020. MR1376050 Ò5.4
- [2] T. Bohman, A. Frieze, and R. Martin, How many random edges make a dense graph Hamiltonian?, Random Structures Algorithms 22 (2003), no. 1, 33–42. MR1943857 Ò1, 1, 9
- [3] J. Böttcher, R. Montgomery, O. Parczyk, and Y. Person, Embedding spanning bounded degree graphs in randomly perturbed graphs, Mathematika 66 (2020), no. 2, 422–447, DOI10.1112/mtk.12005. MR4130332 Ò9
- [4] G. A. Dirac, Some theorems on abstract graphs, Proc. London Math. Soc. (3) 2 (1952), 69–81. MR0047308 Ò1
- [5] A. Dudek, Chr. Reiher, A. Ruciński, and M. Schacht, Powers of Hamiltonian cycles in randomly augmented graphs, Random Structures Algorithms 56 (2020), no. 1, 122–141. Ò1, 4, 5.1, 5.4, 6, 6.1, 8
- [6] P. Erdős, On extremal problems of graphs and generalized graphs, Israel J. Math. 2 (1964), 183–190, DOI10.1007/BF02759942. MR0183654 Ò1, 5.4, 5.14, 5.4
- [7] P. Erdős and M. Simonovits, Supersaturated graphs and hypergraphs, Combinatorica 3 (1983), 181–192. Ò5.4, 5.9
- [8] S. Janson, T. Łuczak, and A. Ruciński, Random graphs, Wiley-Interscience Series in Discrete Mathematics and Optimization, Wiley-Interscience, New York, 2000. MR1782847 Ò2, 2, 2, 2, 6, 7, 7
- [9] J. Komlós, G. N. Sárközy, and E. Szemerédi, On the Pósa-Seymour conjecture, J. Graph Theory 29 (1998), no. 3, 167–176, DOI10.1002/(SICI)1097-0118(199811)29:3<167::AID-JGT4>3.0.CO;2-O. MR1647806 Ò1, 4


- [10] R. Nenadov and M. Trujić, Sprinkling a few random edges doubles the power. To appear in SIAM Journal on Discrete Mathematics. Ò1
- [11] V. Rödl, A. Ruciński, and M. Schacht, Ramsey properties of random k-partite, k-uniform hypergraphs, SIAM J. Discrete Math. 21 (2007), no. 2, 442–460, DOI10.1137/060657492. MR2318677 Ò5.4, 5.15
- [12] P. D. Seymour, Problem Section, Problem 3, Combinatorics (Proc. British Combinatorial Conf., Univ. Coll. Wales, Aberystwyth, 1973), Cambridge Univ. Press, London, 1974, pp. 201–202. London Math. Soc. Lecture Note Ser., No. 13. MR0345829 Ò1
- [13] E. Szemerédi, Regular partitions of graphs, Problémes combinatoires et théorie des graphes (Colloq. Internat. CNRS, Univ. Orsay, Orsay, 1976), Colloq. Internat. CNRS, Vol. 260, CNRS, Paris, 1978, pp. 399–401. Ò5.4, 5.12


Department of Discrete Mathematics, Adam Mickiewicz University, Poznań, Poland Email address: antoniuk@amu.edu.pl

Department of Mathematics, Western Michigan University, Kalamazoo, MI, USA Email address: andrzej.dudek@wmich.edu

Fachbereich Mathematik, Universität Hamburg, Hamburg, Germany Email address: christian.reiher@uni-hamburg.de

Department of Discrete Mathematics, Adam Mickiewicz University, Poznań, Poland Email address: rucinski@amu.edu.pl

Fachbereich Mathematik, Universität Hamburg, Hamburg, Germany Email address: schacht@math.uni-hamburg.de

