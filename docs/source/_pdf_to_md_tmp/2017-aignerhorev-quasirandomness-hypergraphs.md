# arXiv:1711.04750v2[math.CO]20Jul2018

## QUASIRANDOMNESS IN HYPERGRAPHS

ELAD AIGNER-HOREV, DAVID CONLON, HIÊ. P HÀN, YURY PERSON, AND MATHIAS SCHACHT

Abstract. An n-vertex graph G of edge density p is considered to be quasirandom if it shares several important properties with the random graph Gpn, pq. A well-known theorem of Chung, Graham and Wilson states that many such ‘typical’ properties are asymptotically equivalent and, thus, a graph G possessing one such property automatically satisﬁes the others.

In recent years, work in this area has focused on uncovering more quasirandom graph properties and on extending the known results to other discrete structures. In the context of hypergraphs, however, one may consider several diﬀerent notions of quasirandomness. A complete description of these notions has been provided recently by Towsner, who proved several central equivalences using an analytic framework. We give short and purely combinatorial proofs of the main equivalences in Towsner’s result.

§1. Introduction

Quasirandomness may be seen as the study of structures which share some of the typical properties of a random structure of the same size. This area has connections to and applications in several branches of pure mathematics and theoretical computer science. For further information, we refer the reader to the surveys [22,23,39]. We focus here on quasirandom graphs and hypergraphs.

Let pGnqnPN be a sequence of graphs, where Gn has n vertices. For a ﬁxed p P r0,1s, we say that pGnqnPN is p-quasirandom if the graphs Gn have a uniform edge distribution and density p, that is,

epGnrSsq “ pˆ|S| 2

˙ ` opn2q for every S Ď V pGnq, (1.1)

where epGnrSsq denotes the number of edges in the induced subgraph GnrSs. The property above is often referred to as discrepancy. Early results on quasirandom graphs implicitly appeared in [1,2,13,29] and the systematic study was initiated by Thomason [36,37] and Chung, Graham and Wilson [9]. The seminal result of Chung, Graham, and Wilson states that (1.1) is a quasirandom property in the sense that a sequence pGnqnPN satisfying property (1.1) will also satisfy several other properties typically expected (with high probability) of the random graph Gpn,pq. For

The second author was supported by a Royal Society University Research Fellowship and by ERC Starting Grant 676632.

The third author was supported by the FONDECYT Iniciación grant 11150913 and by Millenium Nucleus

Information and Coordination in Networks. The fourth author was supported by DFG grant PE 2299/1-1. The ﬁfth author was supported by ERC Consolidator Grant 724903. A strict subset of this work appeared in the EuroComb2017 conference proceedings as can be seen here.

1

example, having uniform edge distribution is asymptotically equivalent to the property that

˙ ` opn2q and NC4pGnq “ p4n4 ` opn4q, (1.2)

epGnq “ pˆ

n 2

where NC4pGnq denotes the number of labeled copies of C4, the cycle of length 4, in Gn. This is somewhat surprising, as (1.2) seems at ﬁrst glance to be a weaker condition. It is not diﬃcult to

show that any graph Gn on n vertices with edge density p contains at least p4n4 ` opn4q labeled copies of C4. Thus, a graph sequence pGnqnPN is quasirandom if and only if it is an asymptotic minimiser for the number of copies of C4.

Another quasirandom property asserts that for every ﬁxed graph F we have

NFpGnq “ pepFqnvpFq ` opnvpFqq, (1.3)

where again NFpGnq denotes the number of labeled copies of F and vpFq and epFq denote the number of vertices and edges in F, respectively. There are also many other quasirandom properties for graphs besides those mentioned above (see, e.g., [17,18,27,28,30–34,40] and the references therein).

Besides quasirandom graphs notions of quasirandomness have been explored for other discrete structures, including hypergraphs [3,5,16], subsets of Z{nZ [8], set systems [6], tournaments [7], and groups [15]. However, satisfactory generalisations to hypergraphs are surprisingly diﬃcult to pin down. For example, Rödl [29] observed that straightforward generalisations of (1.1) and (1.3) to hypergraphs are not equivalent, while a generalisation of (1.2) is anything but clear.

More formally, let pHnqnPN be a sequence of k-uniform hypergraphs, i.e., pairs pVn,Enq where the edge set En is a subset of all k-element subsets of Vn, which we denote by

`V

k ˘

, and suppose |Vn| “ n. The straightforward generalisation of (1.3) is

n

NFpHnq “ pepFqnvpFq ` opnvpFqq (1.4) for every ﬁxed k-uniform hypergraph F, while the obvious generalisation of (1.1) is

epHnrSsq “ pˆ|S| k

˙ ` opnkq for every S Ď V pHnq. (1.5)

However, (1.5) does not imply (1.4) when k ě 3. Instead, one needs to control the edges with respect to all pk ´ 1q-uniform hypergraphs G on the same vertex set. That is, we need to consider the property

epHnrGsq “ p|KkpGq| ` opnkq for every pk ´ 1q-uniform G on V pHnq, (1.6) where epHnrGsq denotes the number of edges e of Hn with

˘ Ď EpGq and KkpGq is the family of cliques on k vertices that are contained in G. For p “ 1{2, Chung and Graham [5] proved that (1.4) and (1.6) are equivalent and that the correct generalisation of C4 is the octahedron, i.e., the complete k-uniform k-partite hypergraph with classes of order 2. Later, Kohayakawa, Rödl and Skokan [21] generalised this result to arbitrary ﬁxed densities p.

`k´e1

More recently, it was shown by Kohayakawa, Nagle, Rödl and Schacht [20] that (1.5) implies (1.4) if one weakens the requirement of (1.4) to counting linear (or simple) hypergraphs F, that is, hypergraphs where any two edges intersect in at most one vertex. As there are (weak) regularity lemmas for hypergraphs [4,12,35] ‘compatible’ with (1.5), this often allows one to use conceptually simpler tools for studying problems that involve linear hypergraphs only. The reverse implication, (1.4)ùñ(1.5), was shown by Conlon, Hàn, Person and Schacht in [10], that is, provided (1.4) holds for all linear hypergraphs F, then (1.5) also holds. The same authors also described several other such weakly quasirandom properties, including an analogue of (1.2) where the rôle of C4 is ﬁlled by an appropriate linear hypergraph (see [10] for details). They also put forward a guess as to how one might introduce other discrepancy notions of intermediate strength and what the corresponding minimising hypergraphs should look like. Subsequently, Lenz and Mubayi [24–26] extended the results of [10] by adding a spectral property and providing additional equivalences between certain notions of hypergraph quasirandomness of intermediate strength.

Finally, Towsner [38] obtained a common generalisation of those earlier results on hypergraph quasirandomness, where the appropriate versions of (1.1), (1.2), and (1.3) are equivalent. This he accomplished by using the language of non-standard analysis and hypergraph limits. By generalising constructions of Lenz and Mubayi [25], he also showed that these notions of quasirandomness are all distinct, again using analytic language. Towsner remarks that it would be of interest to ﬁnitise his arguments. Here we do just that, providing short combinatorial proofs for the main equivalences in Towsner’s work.

§2. Definitions and the main result

⇀

- 2.1. Quasirandom properties for hypergraphs. For a ﬁnite set X, we write


X to denote the set of all orderings of the members of X and pXq for its powerset. For an integer k ě 1 and a set V , the set of all k-element subsets of V is denoted by

ă to denote   ⇀`Vk˘

`Vk˘

`Vk˘

and we write

.

Given a set (of indices) Q Ď rks, we write V Q for the set of all functions from V to Q. Clearly V Q is isomorphic to V |Q| and we refer to its members as Q-tuples. Unlike the members of

`Vk˘

ă, Q-tuples may contain non-distinct entries. By a Q-directed hypergraph, we mean a pair pV,Eq where E Ď V Q. For a common generalisation of the ‘witness sets’ in (1.5) and (1.6) the following notation will be useful.

- Deﬁnition 2.1. For Q Ď prksq, let G “ pGQqQPQ be a sequence of Q-directed hypergraphs GQ


on the same vertex set V . We say an ordered k-tuple v “ pv1,...,vkq P `Vk˘

ă is supported by G if, for every Q P Q,

vQ “ pvi: i P Qq P EpGQq. Moreover, we denote by KkpGq Ď `Vk˘

ă the set of all ordered k-tuples supported by G. Note that KkpGq “ `Sk˘

ă, when we set Q “ tt1u,...,tkuu “ `rks

˘

and let G consist of k copies of the set S Ď V (viewed as a 1-uniform hypergraph). Similarly, KkpGq “     ⇀KkpGq for Q “ `kr´ks1

1

˘ and G consists of k copies of a pk ´ 1q-uniform hypergraph G indexed by the elements of Q. In

other words, by making appropriate choices for Q we obtain (ordered) versions of the ‘witness sets’ from (1.5) and (1.6). Considering ordered versions simpliﬁes the presentation for families Q which are not subfamilies of a level of the Boolean lattice of subsets of rks. Below we deﬁne a version of discrepancy for hypergraphs for any family Q Ď prksq, which is the ﬁrst quasirandom property we consider here.

- Deﬁnition 2.2 (DISCQ,d). For an integer k ě 2, a set system Q Ď prksq, and reals ε ą 0 and d P r0,1s, we say that a k-uniform hypergraph H “ pV,Eq with |V | “ n satisﬁes DISCQ,dpεq if, for every sequence G “ pGQqQPQ of Q-directed hypergraphs with vertex set V ,

ˇˇE⇀ X KkpGqˇ ´ dˇKkpGqˇˇ ď εnk . We also consider the following weighted version of DISCQ,d, where the sequence of directed

- hypergraphs G is replaced by an ensemble of functions W “ `

wQ: V Q Ñ r´1,1s˘QPQ and the set of supported k-tuples KkpGq is replaced with the function W : V rks Ñ r´1,1s given by

Wpvq “ ź

QPQ

wQpvQq,

where we set wQpvQq to be zero whenever vQ is not a proper set, i.e., whenever it has any non-distinct entries.

Deﬁnition 2.3 (WDISCQ,d). For an integer k ě 2, a set system Q Ď prksq, and reals ε ą 0 and d P r0,1s, we say that a k-uniform hypergraph H “ pV,Eq with |V | “ n satisﬁes WDISCQ,dpεq if, for every ensemble of (weight) functions W “ pwQqQPQ with wQ: V Q Ñ r´1,1s for every Q P Q,

ˇ

ÿ

vPV rks

`

1⇀ Epvq ´ d

˘Wpvq

ˇ

ď εnk ,

where 1⇀ E : V rks Ñ t0,1u denotes the indicator function of

⇀

E. Letting wQ “ 1GQ for every Q P Q, we note that the quantities

ř

vPV rks

`

1⇀ Epvq ´ d

˘Wpvq and |

⇀

E X KkpGq| ´ d|KkpGq| diﬀer by d times the number of v P V rks which have some non-distinct entries, yet are supported by G. However, this diﬀerence has order of magnitude Okpnk´1q, so

- hypergraphs H satisfying WDISCQ,dpεq must also satisfy DISCQ,dp2εq for suﬃciently large n. The opposite implication follows by a simple averaging argument presented in Lemma 3.1 below.


- Deﬁnition 2.4 (Q-simple). We say that a k-uniform hypergraph F “ pVF,EFq is Q-simple for a set system Q Ď prksq, if there is an ordering EF “ tf1,...,fmu of its edges such that for every


In the introduction, we noted that if a graph sequence pGnqnPN with |Gn| “ n contains depFqnvpFq ` opnvpFqq copies of each ﬁxed graph F, then the sequence is d-quasirandom, that is, it satisﬁes the discrepancy condition (1.1) with p “ d. To state the ‘counting’ counterpart of DISCQ,d requires some notion of special hypergraphs.

i “ 1,...,m there is an ordering of the vertices of fi “ txi1,...,xiku with the property that for every h ă i there is a set Q P Q such that

tr: xir P fh X fiu Ď Q.

Here the orderings of the vertices for every edge of F can be chosen independently and might not be compatible with each other.

It is easy to see that the notion of linear hypergraphs coincides with Q-simple hypergraphs for the set system Q “ `rks

˘

`kr´ks1

˘

-simple. The correct analogue of (1.4) for hypergraphs having DISCQ,d is now the restriction to Q-simple hypergraphs F stated below.

, while every k-uniform hypergraph is

1

- Deﬁnition 2.5 (CLQ,d). For an integer k ě 2, a set system Q Ď prksq, reals ε ą 0, d P r0,1s, and a Q-simple k-uniform hypergraph F “ pVF,EFq, we say that a k-uniform hypergraph H “ pV,Eq with |V | “ n satisﬁes CLQ,dpF,εq if the number NFpHq of labeled copies of F in H satisﬁes


ˇNFpHq ´ depFqnvpFqˇ ď εnvpFq .

Next we consider the appropriate generalisation of (1.2) for our setting. Given a k-partite k-uniform hypergraph F with vertex partition V pFq “ X1 ¨Y ... ¨Y Xk and a set Q Ď rks, we deﬁne the Q-doubling of F to be the hypergraph dbQpFq obtained by taking two copies of F and identifying the vertex classes indexed by elements in Q. That is, the vertex set of the Q-doubling is

$ &

Xq if q P Q Xq ˆ t0,1u if q R Q

V pdbQpFqq “ Y1 ¨Y ... ¨Y Yk where Yq “

%

and the edge set of the Q-doubling is the collection of all k-element sets of the form txq : q P Qu Y¨ tpxr,aq: r P rks Qu,

where tx1,...,xku P EpFq and a P t0,1u. It is easy to check that for any two sets Q, R Ď rks and any k-partite k-uniform hypergraph F the ordering of the doubling operations does not matter, i.e.,

dbQpdbRpFqq “ dbRpdbQpFqq.

Hence, for Q Ď prksq trksu (the operation dbrks leaves the hypergraph unchanged), we may deﬁne the Q-simple k-partite k-uniform hypergraph MQ recursively by setting

M∅ “ Kkpkq , to be the k-partite k-uniform hypergraph consisting of one edge and, for any Q P Q, letting MQ “ dbQpMQ tQuq.

In the graph case k “ 2, we obtain MQ “ C4 for Q “ tt1u,t2uu and, for general k ě 2, the hypergraphs MQ for Q “ `rks

˘

were shown to be minimisers for DISCQ,d in [10]. Similarly, for Q “ `kr´ks1

1

˘

, the hypergraphs MQ are the k-uniform octahedra, i.e., complete k-partite k-uniform hypergraphs with vertex classes of size two, that appeared in the work of Chung and Graham [5] and Kohayakawa, Rödl, and Skokan [21].

řk i“1 2|Q|´deg

It follows from these deﬁnitions that MQ consists of 2|Q| hyperedges and

Qpiq vertices, where degQpiq denotes the number of sets of Q containing the element i. An appropriate

sequence of applications of the Cauchy–Schwarz inequality, one for each Q P Q, shows that every k-uniform hypergraph H on n vertices with density d ą 0 contains at least pdepMQq ´ op1qqnvpMQq labeled copies of MQ. The analogue of property (1.2) which we will show is equivalent to DISCQ,d is now as follows.

- Deﬁnition 2.6 (MINQ,d). For an integer k ě 2, a set system Q Ď prksq, and reals ε ą 0 and d P r0,1s, we say that a k-uniform hypergraph H “ pV,Eq with |V | “ n satisﬁes MINQ,dpεq if

- (i ) the density dpHq “ |E|{`nk˘

satisﬁes dpHq ě d ´ ε and

- (ii ) the number NMQpHq of labeled copies of MQ in H satisﬁes NMQpHq ď pdepMQq ` εqnvpMQq .


It is sometimes more convenient to work with the following weighted version of MINQ,d.

- Deﬁnition 2.7 (DEVQ,d). For an integer k ě 2, a set system Q Ď prksq, and reals ε ą 0 and


- d P r0,1s, we say that a k-uniform hypergraph H “ pV,Eq with |V | “ n satisﬁes DEVQ,dpεq if ÿ


ź

p1Epfq ´ dq ď εnvpMQq ,

fPEpMq

M

where the sum ranges over all labeled copies M of MQ in the complete k-uniform hypergraph KVpkq on the vertex set V .

- 2.2. Main results. For a property Px1,...,x pα1,...,αrq of k-uniform hypergraphs, we say a sequence of k-uniform hypergraphs pHnqnPN satisﬁes Px1,...,x if, for each choice of the parameters α1,...,αr all but ﬁnitely many hypergraphs Hn satisfy Px1,...,x pα1,...,αrq. Moreover, given two properties Px1,...,x and Qy1,...,yp, we say that Px1,...,x implies Qy1,...,yp and write


Px1,...,x ùñ Qy1,...,yp

if every sequence pHnqnPN that satisﬁes Px1,...,x also satisﬁes Qy1,...,yp. Our main result is then the following.

Theorem 2.8 (Main result). For every k ě 2, every set system Q Ď prksq trksu, and d P r0,1s, the properties DISCQ,d, WDISCQ,d, CLQ,d, and DEVQ,d are all equivalent. In Section 3, we will prove Theorem 2.8 by establishing the chain of implications

DISCQ,d ùñ WDISCQ,d ùñ CLQ,d ùñ DEVQ,d ùñ WDISCQ,d ùñ DISCQ,d, (2.1) where the last implication was already discussed after Deﬁnition 2.3 above. One could also add MINQ,d to the list of equivalent properties in our main result. Indeed, it is clear that CLQ,d ùñ MINQ,d. While the opposite implication also holds, we have chosen to omit the rather technical proof here. As well as the work of Towsner [38], where Theorem 2.8 ﬁrst appears, we refer the interested reader to [11, Lemma 5.8], where the equivalence between DEVQ,d and WDISCQ,d is also proven as part of a broad spectrum of results about equivalences between diﬀerent hypergraph norms.

While we will always work with general set systems, we follow Towsner in noting that antichains already capture the essence of the deﬁnitions above. We brieﬂy review this point. To begin, note that for any k ě 2 and Q Ď prksq, there is a unique antichain ApQq Ď Q with the property that

for each Q P Q there exists A P ApQq with Q Ď A. (2.2)

In fact, ApQq consists of the inclusion maximal elements from Q. Note now, by (2.2), that the set of ApQq-simple k-uniform hypergraphs coincides with the set of Q-simple k-uniform hypergraphs, so that CLApQq,d and CLQ,d deﬁne the same notion. Therefore, by Theorem 2.8, it follows that ApQq and Q deﬁne the same notion of quasirandomness.

Observation 2.9. For every k ě 2, d P r0,1s, and Q Ď prksq, we have DISCQ,d ðñ DISCApQq,d.

- Observation 2.9 is in fact a special case of a broader principle. Given two set systems A,

B Ď prksq, write A ď B if there exists a bijection ϕ: rks Ñ rks such that for every A P A the set ϕpAq “ tϕpaq: a P Au is contained in the downset generated by B. Note that if A ď B then the A-simple k-uniform hypergraphs are a subset of the B-simple k-uniform hypergraphs. This then yields the following observation.

- Observation 2.10. For every k ě 2, d P r0,1s, and A,B Ď prksq with A ď B, we have DISCB,d ùñ DISCA,d.


As previously mentioned, Towsner [38, Section 9], generalising ideas of Lenz and Mubayi [25], provided constructions of hypergraphs that distinguish the various notions of hypergraph quasirandomness deﬁned above. We do the same. Our construction is essentially that of Towsner, with the distinction between Towsner’s work and ours being in the analysis of the construction. In particular, our approach uses only some simple applications of the Chernoﬀ and Chebyshev inequalities.

For a simpler presentation we focus on the special case of distinguishing DISCQ,1{2 from DISCU,1{2, where both Q, U Ď `rkis˘

are comprised only of i-sets for some 1 ď i ă k and U Ĺ Q. The analysis for densities other than 1{2 and for more general set systems Q and U follows along similar lines, but would require somewhat more technical notation.

Proposition 2.11. For every 1 ď i ă k and U Ĺ Q Ď `rkis˘

there exists δ ą 0 such that for every ε ą 0 there is a sequence of hypergraphs H “ pHnqnPN which satisﬁes DISCU,1{2pεq, but fails to satisfy DISCQ,1{2pδq.

We present the proof of Proposition 2.11 in Section 4 and in the next section we give the details of the proof of Theorem 2.8.

§3. Equivalences of quasirandom properties In this section, we prove Theorem 2.8 by following the plan set out in (2.1).

- 3.1. DISCQ,d ùñ WDISCQ,d. Our proof of the implication DISCQ,d ùñ WDISCQ,d is an adaptation of an argument of Gowers [14, Section 3].


- Lemma 3.1. For every k ě 2, every set system Q Ď prksq trksu, every d P r0,1s, and every δ ą 0, there exists an ε ą 0 such that, for all suﬃciently large n, if H “ pV,Eq is an n-vertex k-uniform hypergraph satisfying DISCQ,dpεq, then H satisﬁes WDISCQ,dpδq. Proof. Given k, d, δ and Q “ tQ1,...,Q u, we set


δ 2|Q|`1

. (3.1)

ε “

Let H “ pV,Eq be an n-vertex k-uniform hypergraph satisfying DISCQ,dpεq and assume, for the sake of contradiction, that H does not satisfy WDISCQ,dpδq. Then there exists a collection of functions

`

wQ: V Q Ñ r´1,1s˘QPQ such that

´1⇀

Epvq ´ d¯ ź QPQ

ÿ

ą δnk .

wQpvQq

ˇ

ˇ

vPV rks

By writing wQ “ wQ` ´ wQ´ for each Q P Q, where wQ` and wQ´ are both of the form V Q Ñ r0,1s, we see that there are |Q| functions s1,...,s with si P twQ`

u for every i P r s, such that

,wQ´

i

i

´1⇀

Epvq ´ d¯ ź i“1

ÿ

ą 2´|Q|δnk (3.1“) 2εnk. (3.2)

sipvQiq

ˇ

ˇ

vPV rks

Let F “ pFQqQPQ “ pFQiqiPr s be the family of random directed hypergraphs where FQi is the random Qi-directed hypergraph where every possible edge f P V Qi is placed in FQi with probability sipfq (as usual, we take sipfq “ 0 if f has some identical entries). Let U Ď V rks denote the random subset of V rks where v is in U if the set vQ P EpFQq for all Q P Q. By the deﬁnition of F, the probability that v is in U is given by

ś

i“1 sipvQiq. The left-hand side of (3.2) under the absolute value is then the expectation of the random variable X “ ř

`

˘

. Therefore, by (3.2), there is a choice of set U˜ for which

1⇀ Epvq ´ d

vPU

´1⇀ Epvq ´ d¯

ÿ

ˇ ą 2εnk .

ˇ

vPU˜

Suppose now that G “ pGQqQPQ is the family of directed hypergraphs from which U˜ is derived, that is, U˜ consists exactly of those v such that vQ P EpGQq for every Q P Q. Then KkpGq Ď U˜ and U˜ KkpGq contains only k-tuples whose entries are not distinct. Since |U˜ KkpGq| “ Okpnk´1q, we see that, for n suﬃciently large,

ÿ

ˇˇE⇀ X KkpGqˇ ´ dˇKkpGqˇˇ “ ˇ

`

˘

1⇀ Epvq ´ d

ˇ

vPKkpGq

ÿ

`

˘

ˇ ´ Okpnk´1q ą 2εnk ´ Okpnk´1q ą εnk ,

1⇀ Epvq ´ d

“ ˇ

vPU˜

which contradicts our assumption that H satisﬁes DISCQ,dpεq.

3.2. WDISCQ,d ùñ CLQ,d. The following lemma shows that WDISCQ,d yields the appropriate counting result for Q-simple hypergraphs F.

- Lemma 3.2. For every k ě 2, every set system Q Ď prksq trksu, every d P r0,1s, every Q-simple k-uniform hypergraph F, and every δ ą 0, there exists an ε ą 0 such that, for all suﬃciently large n, if H “ pV,Eq is an n-vertex k-uniform hypergraph satisfying WDISCQ,dpεq, then H satisﬁes CLQ,dpF,δq. Proof. Given k,Q,d,F, and δ, we set


δ{2 p2epFq ´ 1q

δ 2

and ε1 “

ε “

and write hompF,Hq for the number of homomorphisms from F to H. Note that NFpHq, which is the number of injective homomorphisms, satisﬁes

NFpHq ď hompF,Hq ď NFpHq ` ε1nvpFq

for suﬃciently large n. Indeed, there are at most OvpFqpnvpFq´1q non-injective homomorphisms from F to H and this is at most ε1nvpFq for n suﬃciently large. It will therefore suﬃce to prove that

hompF,Hq “ depFqnvpFq ˘ ε1nvpFq. (3.3) We have

hompF,Hq “ ÿ

ź

1Epϕpfqq “ ÿ

ź

p1Epϕpfqq ´ d ` dq, (3.4)

ϕ: V pFqÑV

ϕ: V pFqÑV

fPEpFq

fPEpFq

where here the sum ranges over all functions V pFq Ñ V and not just over homomorphisms. For ś

- e P EpHq, write gpeq “ 1Epeq ´ d. Multiplying out the expression


fPEpFqpgpϕpfqq ` dq, we obtain 2epFq summands, one corresponding to each subhypergraph of F. These summands have the form

fPEpF1q gpϕpfqq˘

`ś

depFq´epF1q for some subhypergraph F1 Ď F. In particular, when F1 is empty, the corresponding summand is depFq. We may therefore rewrite (3.4) as

hompF,Hq “ depFqnvpFq ` ÿ

depFq´epF1q ÿ

ź

gpϕpfqq. (3.5)

ϕ: V pFqÑV

F1ĎF epF1qě1

fPEpF1q

We will argue that each of the sums

ÿ

ź

gpϕpfqq (3.6)

ϕ: V pFqÑV

fPEpF1q

is small. To make this precise, let F1 be ﬁxed and let tf1,...,fepF1qu be an ordering of the edges of F1 which certiﬁes its Q-simplicity. Let f1 denote fepF1q, the last edge in this ordering, and let x1,...,xk be the vertices of the edge f1, again ordered so as to certify Q-simplicity (see Deﬁnition 2.4). We may rewrite (3.6) as ÿ

ź

gpϕpfqq “ ÿ

ÿ

ź

gpϕpfqq (3.7)

ϕ: V pFqÑV

ϕ1 : V pFq f1ÑV

ϕ: V pFqÑV ϕ|V pFq f1”ϕ1

fPEpF1q

fPEpF1q

and, for each (ﬁxed) ϕ1, we may further rewrite the inner sum in (3.7) as ÿ

gpϕpf1qq ź

ź

gpϕpfqq “ ÿ

ÿ

gpϕpfqq. (3.8)

ϕ: V pFqÑV ϕ|V pFq f1”ϕ1

ϕ: V pFqÑV ϕpxiq“vi@iPrks ϕ|V pFq f1”ϕ1

fPEpF1q tf1u

fPEpF1q

v“pv1,...,vkqPV rks

Finally, we explain how one may apply WDISCQ,dpεq to estimate the right-hand side of (3.8). By Q-simplicity, for every f P EpF1q tf1u there exists a set Q P Q with ti: xi P fu Ď Q. Therefore, there exists a partition of EpF1q tf1u into (possibly empty) sets pEQqQPQ such that for every Q P Q and f P EQ, we have ti: xi P fu Ď Q. For f P EpF1q, let us write If “ ti: xi P f X f1u to denote the indices of the elements appearing in f X f1, noting that

Ť

fPEQ If Ď Q for all Q P Q.

For any f P EpFq, ϕpfq is composed of two parts: the images of the vertices in f X f1 Ď tx1,...,xku and the images of the vertices in f f1. In (3.8), the images of these latter vertices are already ﬁxed by ϕ1. With this in mind, we deﬁne functions

`

wQ: V Q Ñ r´1,1s˘QPQ by

´1E

`tyi: i P Ifu Y ϕ1pf f1q˘ ´ d¯. (3.9)

wQ pyq “ ź

fPEQ

That is, using y P V Q we pick images tyi: i P Ifu for the elements xi appearing in the indices speciﬁed by If. Hence, if ϕ is the extension of ϕ1 given by taking yi “ ϕpxiq for all i P Ť

fPEQ If Ď Q, the right-hand side of (3.9) corresponds exactly to

ś

fPEQ gpϕpfqq. Therefore, since, for any vector z “ pz1,...,zkq P V rks, we have

gpzq “ gptz1,...,zkuq “ 1Eptz1,...,zkuq ´ d “ 1⇀

Epzq ´ d, we may rewrite the right-hand side of (3.8) as

´1⇀

Epvq ´ d¯ ź QPQ

ÿ

ÿ

gpϕpf1qq ź

gpϕpfqq “ ÿ

wQpvQq.

ϕ: V pFqÑV ϕpxiq“vi@iPrks ϕ|V pFq f1”ϕ1

fPEpF1q tf1u

v“pv1,...,vkqPV rks

vPV rks

By WDISCQ,dpεq, the right-hand side of the identity above is at most εnk in absolute value. Thus, we may bound (3.7) (which is also (3.6)) by εnvpFq. This in turn allows us to write (3.5) as

hompF,Hq “ depFqnvpFq ˘ `

˘

δ 2

2epFq ´ 1

nvpFq,

εnvpFq “ depFqnvpFq ˘

which completes the proof of (3.3).

- 3.3. CLQ,d ùñ DEVQ,d. Recall that NFpHq denotes the number of labeled copies of F in H.


We also write NF˚1,FpHq for the number of labeled copies of F1 that are induced with respect to F in H, that is, the number of injections ϕ: V pFq Ñ V pHq such that for all f P EpFq we have ϕpfq P EpHq if and only if f P EpF1q. The following lemma, whose proof by the principle of inclusion and exclusion follows verbatim from Facts 8 and 9 in [10], provides the required implication. We include its short proof for completeness.

- Lemma 3.3. For every k ě 2, every set system Q Ă prksq trksu, every d P r0,1s, and every δ ą 0, there exists an ε ą 0 such that if H “ pV,Eq is an n-vertex k-uniform hypergraph that satisﬁes CLQ,dpF,εq for all F Ď MQ, then H satisﬁes DEVQ,dpδq.


ř

ś

fPEpMqp1Epfq ´ dq with M running over all copies of MQ in the complete hypergraph KVpkq on the vertex set V . By the inclusion-exclusion principle, we have for every spanning F1 Ď MQ

Proof. We shall bound

M

NF˚1,MQpHq “ ÿ

p´1qepFq´epF1qNFpHq.

F1ĎFĎMQ

Since CLQ,dpF,εq holds for all F Ď MQ, we see that ÿ

ź

p1Epfq ´ dq “ ÿ

NF˚1,MQpHqp1 ´ dqepF1qp´dqepMQq´epF1q

F1ĎMQ

fPEpMq

M

p1 ´ dqepF1qp´dqepMQq´epF1q ÿ

“ ÿ

p´1qepFq´epF1qNFpHq

F1ĎFĎMQ

F1ĎMQ

ÿ

p1 ´ dqepF1qp´dqepMQq´epF1q ÿ

p´1qepFq´epF1qdepFqnvpMQq

ď

ˇ

ˇ ` 22epMQqεnvpMQq

F1ĎMQ

F1ĎFĎMQ

“ δnvpMQq ,

where we chose ε “ δ{22epMQq and used the binomial theorem to show that ÿ

p1 ´ dqepF1qp´dqepMQq´epF1q ÿ

p´1qepFq´epF1qdepFq

F1ĎFĎMQ

F1ĎMQ

“ ÿ

p1 ´ dqepF1qp´dqepMQq´epF1qdepF1q ÿ

p´dqepFq´epF1q

F1ĎMQ

F1ĎFĎMQ

“ ÿ

p1 ´ dqepF1qp´dqepMQq´epF1qdepF1qp1 ´ dqepMQq´epF1q

F1ĎMQ

“ p1 ´ dqepMQq ÿ

p´dqepMQq´epF1qdepF1q

F1ĎMQ

“ 0.

- 3.4. DEVQ,d ùñ WDISCQ,d. Recall that MQ (for some Q Ă prksq) is the k-uniform hypergraph obtained from a sequence of doubling operations. Assume that Q Ă prksq consists of sets Q1,... ,Q for some ordering of the sets of Q. We set Qj “ tQ1,...,Qju and let MQj be the subhypergraph of MQ formed by the j doublings around Q1,...,Qj. We also set MQ0 “ M∅ “ Kkpkq. Given any k-partite k-uniform hypergraph M, we refer to the j-th vertex class of M by VjpMq


and we write VQpMq “ Ť

jPQ VjpMq for any Q Ď rks. The implication DEVQ,d ùñ WDISCQ,d is a consequence of the following lemma.

- Lemma 3.4. For every k ě 2, every set system Q “ tQ1,...,Q u Ă prksq trksu, every d P r0,1s, and every δ ą 0, there exists an ε ą 0 such that, for all suﬃciently large n, if H “ pV,Eq is an n-vertex k-uniform hypergraph that satisﬁes


´1⇀ E`

ϕpfq˘ ´ d¯

ÿ

ź

ď εnvpMQq , (3.10)

ˇ

ˇ

ϕ: V pMQqÑV

fPEpMQq

then H satisﬁes WDISCQ,dpδq.

It is easy to see that (3.10) is equivalent to DEVQ,d since all but OkpnvpMQq´1q functions ϕ are injective and thus correspond to labeled copies of MQ in the complete k-uniform hypergraph on V . Moreover, since the doubling dbrks leaves the k-uniform hypergraph unchanged, taking rks R Q is not a restriction.

ωQ: V Q Ñ r´1,1s˘QPQ be any collection of weight functions. With V pM∅q “ rks, we write

Proof of Lemma 3.4. Let W “ `

2

2

ÿ

ÿ

`

˘Wpvq

`

˘W`

ϕp1q,...,ϕpkq˘

1⇀ Epϕp1q,...,ϕpkqq´ d

. (3.11)

1⇀ Epvq´ d

“

ˇ

ˇ

ˇ

ˇ

ϕ: V pM∅qÑV

vPV rks

We shall apply the Cauchy–Schwarz inequality times to (3.11), each time separating a function ωQ (using the fact that 0 ď ωQ2 ď 1). Recalling that for Q Ď rks and f “ px1,...,xkq, fQ “ pxi: i P Qq, below we will show that for each j “ 0,...,  ´ 1 we have

2

ϕpfq˘ ´ d¯ˆ ź

˙

´1⇀ E`

ÿ

ź

`

ϕpfQq˘

ωQ

ˇ

ˇ

ϕ: V pMQjqÑV

QPQ Qj

fPEpMQjq

ϕpfq˘ ´ d¯ˆ ź

˙

´1⇀ E`

ÿ

ź

`

ϕpfQq˘

ď n|VQj`1pMQjq| ¨

. (3.12)

ωQ

ˇ

ˇ

ϕ: V pMQj`1qÑV

QPQ Qj`1

fPEpMQj`1q

In fact, to see (3.12), we rewrite the sum on the left-hand side of (3.12) as a double sum in which the ﬁrst sum is over all ψ: VQj`1pMQjq Ñ V and the second sum is over all extensions of ψ to ϕ: V pMQjq Ñ V . Since ϕ extends ψ we have ωQj`1pϕpfQj`1qq “ ωQj`1pψpfQj`1qq, where we view the edge f P EpMQjq as an ordered k-tuple (according to the k vertex classes of MQj), fQ as a Q-tuple and ϕpfq is the tuple of values of entries from f under ϕ. Thus, the left-hand side of (3.12) assumes the form

2

ϕpfq˘ ´ d¯ˆ ź

˙

´1⇀ E`

ÿ

ź

ψpfQj`1q˘ ÿ

ź

`

`

ϕpfQq˘

ωQj`1

,

ωQ

ˇ

ˇ

ϕ: V pMQjqÑV ϕ|VQj`1pMQjq”ψ

QPQ Qj`1

fPEpMQjq

fPEpMQjq

ψ

where the ﬁrst sum runs over all maps ψ: VQj`1pMQjq Ñ V .

We then apply the Cauchy–Schwarz inequality with the product after the ﬁrst sum forming the ﬁrst sequence and the second sum forming the second sequence. The term n|VQj`1pMQjq| on the righthand side of (3.12) comes from the ﬁrst sequence after applying the Cauchy–Schwarz inequality

and using ωQ2

ď 1. Summing over the squares of the terms in the second sequence corresponds exactly to performing the doubling operation dbQj`1 – the vertices outside of VQj`1pMQjq are doubled and all edges of MQj and their corresponding weight functions ωQ are doubled as well. But this is exactly the sum on the right-hand side of (3.12), as required.

j`1

Starting with (3.11) we apply (3.12) j “ 0,...,  ´ 1 and obtain

˜ ´1

¸

2

´n|VQj`1pMQjq|

¯2 ´j´1

´1⇀ E`

ϕpfq˘ ´ d¯

ź

ÿ

ÿ

ź

`

˘Wpvq

1⇀ Epvq´d

ď

¨

.

ˇ

ˇ

ˇ

ˇ

j“0

ϕ: V pMQqÑV

fPEpMQq

vPV rks

Owing to the assumption (3.10), we arrive at

2

ď ˆ ź ´1 j“0

˙ ¨ εnvpMQq . (3.13)

ÿ

`

˘Wpvq

n|VQj`1pMQjq|2 ´j´1

1⇀ Epvq ´ d

ˇ

ˇ

vPV rks

It remains to show that

ÿ ´1

2 ´j´1|VQj`1pMQjq| ` |V pMQq| “ k2 , (3.14)

j“0

since then the desired bound

ÿ

`

˘Wpvq

ď δnk .

1⇀ Epvq ´ d

ˇ

ˇ

vPV rks

follows for ε “ δ2 . For the proof of (3.14) we observe that for every i P rks and j “ 0,...,  we have

ˇVipMQjqˇ “ 2j´degQjpiq ,

since the i-th vertex of Kkpkq “ M∅ will be doubled for every edge of Q P Qj with i R Q. Since Q “ Q , we therefore obtain

ÿ ´1

ÿ ´1

ÿk

ÿ

2 ´1´degQjpiq `

2 ´j´1|VQj`1pMQjq| ` |V pMQq| “

2 ´degQpiq

j“0

j“0

i“1

iPQj`1

ÿ ´1

ÿk

ÿ

2 ´degQj`1piq `

2 ´degQpiq

“

j“0

i“1

iPQj`1

ÿk

“ ÿ

ÿ

2 ´degQjpiq `

2 ´degQpiq

j“1

i“1

iPQj

degÿQpiq

ÿk

“ ÿ

2 ´degQpiq .

2 ´t `

iPŤ Q

t“1

i“1

Viewing Q as a (possibly non-uniform) hypergraph with vertex set rks, we observe that every isolated vertex i P rks ŤQ is not considered in the ﬁrst double sum above and contributes 2 to the second sum. Moreover, every vertex i P ŤQ contributes

2 ´1 2 `

¯ ` 2

1 4 ` ¨¨¨ `

1 2deg

1 2deg

Qpiq “ 2

Qpiq

and, hence, (3.14) follows.

§4. Distinguishing notions of quasirandomness

In this section we prove Proposition 2.11, which roughly speaking asserts that the various notions of quasirandomness deﬁned are distinct. We shall use the following notation and setup. Let V “ rns and order V according to the natural ordering of rns. For v P `Vk˘

, we write vpnatq to denote the ordering of v induced by the natural ordering of rns. Then, given Q Ď rks, we write vpQnatq to denote pvpnatqqQ. Given 1 ď i ă k and a set B Ď `Vi ˘

, we write HpkqpBq to denote the k-uniform hypergraph whose vertex set is V and where a set v P `Vk˘

is taken to be an edge of HpkqpBq if the quantity pv “ |tvQpnatq P

⇀

B: Q P Qu| is odd. The following lemma will facilitate the construction used in the proof of Proposition 2.11 below.

Lemma 4.1. For every i P rk ´ 1s and η ą 0 there exists an n0 such that, for every n ě n0, there is a set system B Ď `Vi ˘

with the following properties:

- (i ) For every sequence G “ pGRqRPR of directed hypergraphs with R Ď prisq having the property that |R| ă i for every R P R,

ˇB⇀ X KipGqˇ “ 12|KipGq| ˘ ηni. (4.1)

- (ii ) The edge density of HpkqpBq is 1{2 ˘ η.
- (iii ) If F “ pFQqQPQ is the sequence of directed hypergraphs for Q Ď `rkis˘


with V pFQq “ rns and

⇀

B( for every Q P Q, then |KkpFq| “ p2´|Q| ˘ ηqnk.

EpFQq “ v P V Q: vpnatq R

Proof. We prove that a randomly chosen subset B Ď `Vi ˘

satisﬁes all of the above assertions with positive probability when n is suﬃciently large. Suppose then that B Ď `Vi ˘

is a random subset of the i-sets of V where each i-set is placed in B independently with probability 1{2.

To show that (i ) holds with probability 1 ´ op1q, ﬁx G “ pGRqRPR subject to the restriction on R in (i ). The random variable ˇB⇀ X KipGqˇ satisﬁes E

ˇB⇀ X KipGqˇ

‰ “ |KipGq|{2. As ˇB⇀ X KipGqˇ “ ÿ

“

1⇀ Bpvq

vPKipGq

⇀

is a sum of independent indicator random variables (that is, 1⇀ Bpvq is equal to 1 if v P

B and zero otherwise), it follows, by Chernoﬀ’s inequality (see, e.g., [19, Corollary 2.3]), that

P´

B X KipGq| ´ |KipGq|{2ˇ ě ηni¯ ď 2´Ωpniq.

⇀

ˇ|

As the number of possible sequences G is 2Opni´1q, it follows that B satisﬁes the ﬁrst property with probability 1 ´ op1q for n suﬃciently large.

We proceed to (ii ). Suppose HpkqpBq “ pV,Eq. For any v P `Vk˘

, we have

Ppv P Eq “ Pppv is oddq “ 21

`nk˘

. Writing epHpkqpBqq “ ř

and so Er|E|s “ 12

vPpVkq 1Epvq, we see, by Chebyshev’s inequality, that

ř

u,vPpVkq Covp1Epuq,1Epvqq

`nk˘¯ ď

P´

`nk˘

Er|E|s `

ˇ|E| ´ 21

ˇ ě η

2ηEr|E|s˘2 `

2ηEr|E|s˘2 ,

`

where the sum on the right-hand side ranges over k-sets u and v such that upQnatq “ vpQnatq for some Q P Q. The number of such pairs of sets is Opn2k´iq. As i ě 1 and pEr|E|sq2 “ Ωpn2kq, it follows that B satisﬁes the second property with probability 1 ´ op1q for n suﬃciently large.

⇀

For the third property (iii ), note that v P KkpFq if and only if vpQnatq R

B for every Q P Q. Therefore, Er|KkpFq|s “ 2´|Q|npn ´ 1q¨¨¨pn ´ k ` 1q. Concentration around this expectation may be established via the second moment method in a similar manner to the argument used for (ii ).

Next we derive Proposition 2.11 from Lemma 4.1.

Proof of Proposition 2.11. It suﬃces to verify the case when U and Q only diﬀer by one i-element set and, without loss of generality, we will assume that Q U “ tQ˚u for

Q˚ “ rk ´ i ` 1,ks “ tk ´ i ` 1,...,ku.

Set δ “ 2´|Q|´3 and, given ε ą 0, set η “ mintε{2|U|,2´|Q|´2u. With this i and η, let n0 be the integer whose existence is guaranteed by Lemma 4.1 and, for every n ě n0, let Bn Ď `Vi ˘

be a set system satisfying the properties stipulated in that lemma. We consider Hn “ HnpkqpBnq.

By (ii ) the density of Hn is as required. To see that H “ pHnqnPN does not satisfy DISCQ,1{2pδq, let F be as in (iii ). Then

⇀

EpHnq X KkpFq is the empty set, so ˇ|

⇀

EpHnq X KkpFq| ´ 2´1|KkpFq|ˇ “ 2´1|KkpFq| “ `

˘

2´|Q|´1 ˘ η

nk ě 2´|Q|´2nk ą δnk.

It remains to show that H satisﬁes DISCU,1{2pεq. To that end, ﬁx a sequence of directed hypergraphs G “ pGUqUPU. Our aim is to prove that

ˇE⇀pHnq X KkpGqˇ “ |KkpGq|{2 ˘ εnk.

Recall that Q˚ “ rk´i`1,ks. For P V rk´is and u P V Q˚, we write ˝u to denote the member of V rks satisfying p ˝ uqr1,k´is “ and p ˝ uqQ˚ “ u. Deﬁne

⇀

Extp q “ tu P V Q˚ : ˝ u P

EpHnq X KkpGqu to be the set of ways the pk ´ iq-tuple can be extended to a member of

⇀

EpHnq X KkpGq. Then ˇ

EpHnq X KkpGqˇ “ ÿ

⇀

|Extp q|.

PV rk´is

A tuple P V rk´is is said to have potential for extension if U P EpGUq for every U P U not meeting Q˚. Otherwise, we say has no potential. Observe that |Extp q| “ 0 if has no potential. In particular, we may write

EpHnq X KkpGqˇ “ ÿ PP

⇀

|Extp q|,

ˇ

where P Ď V rk´is denotes all tuples that have potential for extension. To say more about |Extp q| for P P, we require some further notation.

We write Rp q for the set of all u P V Q˚ such that p ˝ uqU P EpGUq for all U P UQ˚, where UQ˚ “ tU P U : U X Q˚ ­“ ∅u,

noting that u P V Q˚ cannot lie in Extp q unless it satisﬁes this condition. For each GU P G with U P UQ˚, we deﬁne two directed hypergraphs. The ﬁrst, GPU, , has V as its vertex set and

⇀

Bn( for its (directed) edge set. The second, GRU, , is deﬁned similarly with

vUXQ˚ : v P V rks with vr1,k´is “ and vU P EpGUq X

⇀

Bn replaced by its complement

⇀

Cn. That is, the vertex set of GRU, is V and its edge set is

⇀

Cn(

vUXQ˚ : v P V rks with vr1,k´is “ and vU P EpGUq X

. In order to determine whether (a ﬁxed) u P Rp q is in Extp q, we consider three parameters:

- (a ) The parity of the quantity |t U P

⇀

Bn: U P Uu|. We write p for this parity, treated as a residue modulo 2, and refer to it as the parity of .

- (b ) The parity of the quantity

ˇ p ˝ uqUXQ˚ P EpGPU, q: U P U and U X Q˚ ­“ ∅

(

ˇ “ ÿ

UPUQ˚

1EpGP

U, qpuUXQ˚q

This is the parity of the number of U P U meeting Q˚ for which p ˝ uqU is supported by both EpGUq and

⇀

Bn. We write p1u for this parity, again treated as a residue modulo 2, and refer to it as the parity of u.

- (c ) The value of (or, alternatively, 1⇀ Cnpuq).


Setting p ,u ” p ` p1u mod 2, we see that if P P and u P V Q˚, then

$ ’&

Bnpuq mod 2, 0, if u P Rp q and p ,u ” 1⇀

1, if u P Rp q and p ,u ı 1⇀

Bnpuq mod 2, 0, if u R Rp q.

1Extp qpuq “

’%

For instance, if P P has even parity and u P Rp q has odd parity (so that p ,u ” 1 mod 2), then, in order to have ˝ u P

⇀

Bnpuq “ 0 to attain the desired parity as per the deﬁnition of Hn. Therefore, for a ﬁxed P P,

EpHnq, one must have 1⇀

|Extp q| “ |tu P Rp q: p ,u ı 1⇀

Bnpuq mod 2u|. (4.2) The pairs pGPU, ,GRU, qUPUQ˚ give rise to 2|UQ˚| sequences of directed hypergraphs. Enumerate

these sequences arbitrarily and let Gj, “ pGpUjqqUPUQ˚ with GpUjq P tGPU, ,GRU, u, denote the j-th sequence in this enumeration. We shall refer to such sequences as signature sequences. We say a

signature sequence Gj, is odd if the number of its members appearing with the superscript P is odd. Otherwise, we say the sequence is even. In this way, each signature sequence is assigned a parity.

Note now that for each i-tuple u P Rp q with parity p1u there exists a unique signature sequence Gj, of the same parity such that u P KipGj, q, given by taking

$ &

GPU, , if uUXQ˚ P EpGPU, q, GRU, , if uUXQ˚ P EpGRU, q.

GpUjq “

%

`KipGj, q˘2|UQ˚|

Therefore, since KipGj, q Ď Rp q for each j, we see that the sets

j“1 form a partition of Rp q.

Given P P and a signature sequence Gj, of parity p, we set

$ &

⇀

Bn, if p ` p ” 0 mod 2

fp ,Gj, q “

⇀

%

Cn, if p ` p ” 1 mod 2. By the discussion above, we may then rewrite (4.2) as

2|UÿQ˚|

|Extp q| “

j“1 ˇfp ,Gj, q X KipGj, qˇ, which in turn yields

2|UÿQ˚|

EpHnq X KkpGq| “ ÿ PP

⇀

j“1 ˇfp ,Gj, q X KipGj, qˇ. (4.3) We now claim that

|

2|UÿQ˚|

|KkpGq| “ ÿ PP

|KipGj, q|. (4.4)

j“1

To see this, ﬁx v P KkpGq and write v “ ˝ u where vrk´i`1s “ and vQ˚ “ u. For such a v, we have vU P EpGUq for every U P U, so that P P and u P Rp q. The inclusion of the members of the sequence pvUqUPUQ˚ in

⇀

⇀

Cn deﬁnes a unique signature sequence (with respect to ), namely, Gj˚, for some appropriate j˚, such that u P KipGj˚, q. Indeed, vU “ p ˝ uqU P EpGUq for each U P UQ˚, so that p ˝ uqU P

Bn or

⇀

⇀

Cn implies that uUXQ˚ P EpGRU, q. Therefore, every v P KkpGq can be written as ˝ u with P P and u P KipGj˚, q for some j˚. Conversely, given P P and u P KipGj, q Ď Rp q for some j, the tuple ˝ u automatically satisﬁes p ˝ uqU P EpGUq for every U P U. The claim then follows.

Bn implies that uUXQ˚ P EpGPU, q and p ˝ uqU P

Returning to (4.3), we see that

2|UÿQ˚| j“1 ˇfp ,jq X KipGj, qˇ (4.1“) ÿ

2|UÿQ˚|

ˇE⇀pHnq X KkpGqˇ “ ÿ PP

`|KipGj, q|{2 ˘ ηni

˘

j“1

PP

2|UÿQ˚|

- 1

- 2 ÿ PP


|KipGj, q| ˘ 2|U|η ÿ

|KkpGq|

ni (4.4“)

2 ˘ εnk, as required.

“

j“1

PV k´i

Acknowledgements. We are indebted to the anonymous referee for their careful review.

References

- [1] N. Alon, Eigenvalues and expanders, Combinatorica 6 (1986), no. 2, 83–96. Theory of computing (Singer Island, Fla., 1984). Ò1
- [2] N. Alon and F. R. K. Chung, Explicit construction of linear sized tolerant networks, Proceedings of the First Japan Conference on Graph Theory and Applications (Hakone, 1986), 1988, pp. 15–19. Ò1
- [3] F. R. K. Chung, Quasi-random classes of hypergraphs, Random Structures Algorithms 1 (1990), no. 4, 363–382. Ò1
- [4] , Regularity lemmas for hypergraphs and quasi-randomness, Random Structures Algorithms 2 (1991), no. 2, 241–252. Ò1

- [5] F. R. K. Chung and R. L. Graham, Quasi-random hypergraphs, Random Structures Algorithms 1 (1990), no. 1, 105–124. Ò1, 1, 2.1
- [6] , Quasi-random set systems, J. Amer. Math. Soc. 4 (1991), no. 1, 151–196. Ò1

- [7] , Quasi-random tournaments, J. Graph Theory 15 (1991), no. 2, 173–198. Ò1

- [8] , Quasi-random subsets of Zn, J. Combin. Theory Ser. A 61 (1992), no. 1, 64–86. Ò1

- [9] F. R. K. Chung, R. L. Graham, and R. M. Wilson, Quasi-random graphs, Combinatorica 9 (1989), no. 4, 345–362. Ò1
- [10] D. Conlon, H. Hàn, Y. Person, and M. Schacht, Weak quasi-randomness for uniform hypergraphs, Random Structures Algorithms 40 (2012), no. 1, 1–38. Ò1, 2.1, 3.3
- [11] D. Conlon and J. Lee, Finite reﬂection groups and graph norms, Adv. Math. 315 (2017), 130–165. Ò2.2
- [12] P. Frankl and V. Rödl, The uniformity lemma for hypergraphs, Graphs Combin. 8 (1992), no. 4, 309–312. Ò1
- [13] P. Frankl, V. Rödl, and R. M. Wilson, The number of submatrices of a given type in a Hadamard matrix and related results, J. Combin. Theory Ser. B 44 (1988), no. 3, 317–328. Ò1
- [14] W. T. Gowers, Quasirandomness, counting and regularity for 3-uniform hypergraphs, Combin. Probab. Comput. 15 (2006), no. 1-2, 143–184. Ò3.1
- [15] , Quasirandom groups, Combin. Probab. Comput. 17 (2008), no. 3, 363–387. Ò1

- [16] J. Haviland and A. Thomason, Pseudo-random hypergraphs, Discrete Math. 75 (1989), no. 1-3, 255–278. Ò1
- [17] H. Huang and C. Lee, Quasi-randomness of graph balanced cut properties, Random Structures Algorithms 41

(2012), no. 1, 124–145. Ò1

- [18] S. Janson, Quasi-random graphs and graph limits, European J. Combin. 32 (2011), no. 7, 1054–1083. Ò1
- [19] S. Janson, T. Łuczak, and A. Ruciński, Random graphs, Wiley-Interscience, New York, 2000. Ò4
- [20] Y. Kohayakawa, B. Nagle, V. Rödl, and M. Schacht, Weak hypergraph regularity and linear hypergraphs, J. Combin. Theory Ser. B 100 (2010), no. 2, 151–160. Ò1
- [21] Y. Kohayakawa, V. Rödl, and J. Skokan, Quasi-randomness, hypergraphs, and conditions for regularity, J. Combin. Theory Ser. A 97 (2002), no. 2, 307–352. Ò1, 2.1
- [22] J. Komlós, A. Shokoufandeh, M. Simonovits, and E. Szemerédi, The regularity lemma and its applications in graph theory, Theoretical aspects of computer science (Tehran, 2000), 2002, pp. 84–112. Ò1
- [23] M. Krivelevich and B. Sudakov, Pseudo-random graphs, More sets, graphs and numbers, 2006, pp. 199–262. Ò1
- [24] J. Lenz and D. Mubayi, Eigenvalues and linear quasirandom hypergraphs, Forum Math. Sigma 3 (2015), e2, 26 pp. Ò1
- [25] , The poset of hypergraph quasirandomness, Random Structures Algorithms 46 (2015), no. 4, 762–800. Ò1, 2.2

- [26] , Eigenvalues of non-regular linear-quasirandom hypergraphs, Discrete Math. 340 (2017), no. 2, 145–153. Ò1


- [27] L. Lovász and V. T. Sós, Generalized quasirandom graphs, J. Combin. Theory Ser. B 98 (2008), no. 1, 146–163. Ò1
- [28] C. Reiher and M. Schacht, Forcing quasirandomness with triangles. submitted. Ò1
- [29] V. Rödl, On universality of graphs with uniformly distributed edges, Discrete Math. 59 (1986), no. 1-2, 125–134. Ò1, 1
- [30] A. Shapira, Quasi-randomness and the distribution of copies of a ﬁxed graph, Combinatorica 28 (2008), no. 6, 735–745. Ò1
- [31] A. Shapira and R. Yuster, The eﬀect of induced subgraphs on quasi-randomness, Random Structures Algorithms 36 (2010), no. 1, 90–109. Ò1
- [32] M. Simonovits and V. T. Sós, Szemerédi’s partition and quasirandomness, Random Structures Algorithms 2

(1991), no. 1, 1–10. Ò1

- [33] M. Simonovits and V. T. Sós, Hereditarily extended properties, quasi-random graphs and induced subgraphs, Combin. Probab. Comput. 12 (20035), 319–344. Ò1
- [34] J. Skokan and L. Thoma, Bipartite subgraphs and quasi-randomness, Graphs Combin. 20 (2004), no. 2, 255–262. Ò1
- [35] A. Steger, Die Kleitman–Rothschild Methode, Ph.D. Thesis, 1990. Ò1
- [36] A. Thomason, Pseudorandom graphs, Random graphs ’85 (Poznań, 1985), 1987, pp. 307–331. Ò1
- [37] , Random graphs, strongly regular graphs and pseudorandom graphs, Surveys in combinatorics 1987 (New Cross, 1987), 1987, pp. 173–195. Ò1

- [38] H. Towsner, σ-algebras for quasirandom hypergraphs, Random Structures Algorithms 50 (2017), no. 1, 114–139. Ò1, 2.2, 2.2
- [39] S. P. Vadhan, Pseudorandomness, Found. Trends Theor. Comput. Sci. 7 (2011), no. 1-3, 1–338. Ò1
- [40] R. Yuster, Quasi-randomness is determined by the distribution of copies of a ﬁxed graph in equicardinal large sets, Combinatorica 30 (2010), no. 2, 239–246. Ò1


Department of Mathematics and Computer Science, Ariel University, Ariel, Israel E-mail address: horev@ariel.ac.il

Mathematical Institute, University of Oxford, Oxford, United Kingdom E-mail address: David.Conlon@maths.ox.ac.uk

Departamento de Matemática y Ciencia de la Computación, Universidad de Santiago de Chile, Santiago, Chile

E-mail address: hiep.han@usach.cl

Institut für Mathematik, Goethe-Universität, Frankfurt am Main, Germany E-mail address: person@math.uni-frankfurt.de

Fachbereich Mathematik, Universität Hamburg, Hamburg, Germany E-mail address: schacht@math.uni-hamburg.de

