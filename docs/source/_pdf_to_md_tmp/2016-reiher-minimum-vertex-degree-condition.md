# arXiv:1611.03118v2[math.CO]28Jan2019

### MINIMUM VERTEX DEGREE CONDITION FOR TIGHT HAMILTONIAN CYCLES IN 3-UNIFORM HYPERGRAPHS

CHRISTIAN REIHER, VOJTĚCH RÖDL, ANDRZEJ RUCIŃSKI, MATHIAS SCHACHT, AND ENDRE SZEMERÉDI

Dedicated to the memory of András Hajnal

Abstract. We show that every 3-uniform hypergraph with n vertices and minimum vertex degree at least p5{9 ` op1qq`n

˘

contains a tight Hamiltonian cycle. Known lower bound constructions show that this degree condition is asymptotically optimal.

2

§1. Introduction

G. A. Dirac [7] proved that every graph G “ pV,Eq on at least 3 vertices and with minimum vertex degree δpGq ě |V |{2 contains a Hamiltonian cycle. This result is best possible, as there are graphs G with minimum degree δpGq “ P|V |{2

T ´ 1 not containing a Hamiltonian cycle.

We continue the study to which extent Dirac’s theorem can be generalised to hypergraphs. Here we shall restrict to 3-uniform hypergraphs and if not mentioned otherwise by a hypergraph we will mean a 3-uniform hypergraph. Note that in this case there are at least two natural concepts of a minimum degree condition and several notions of cycle, and we brieﬂy introduce some of them below.

For a hypergraph H “ pV,Eq and a vertex v P V we denote by NHpvq the neighbourhood of v and by dHpvq the degree of v deﬁned as

NHpvq “ te P E: v P eu and dHpvq “ ˇNHpvqˇ.

Let δpHq “ min dHpvq be the minimum vertex degree of H taken over all v P V . Similarly, for any two vertices u, v P V we denote by NHpu,vq their pair neighbourhood and by dHpu,vq their pair degree deﬁned by

NHpu,vq “ te P E: u,v P eu and dHpu,vq “ ˇNHpu,vqˇ.

2010 Mathematics Subject Classiﬁcation. Primary: 05C65. Secondary: 05C45. Key words and phrases. hypergraphs, Hamiltonian cycles, Dirac’s theorem. The second author is supported by NSF grant DMS 1301698. The third author is supported by Polish NSC grant 2014/15/B/ST1/01688. The ﬁfth author is supported by ERC Advanced Grant 321104.

1

Let δ2pHq “ min dHpu,vq be the minimum pair degree over all pairs of vertices of H. We will sometimes skip the subscript and write dpvq, Npvq, dpu,vq, and Npu,vq instead.

An early notion of cycles in hypergraphs appeared in the work of Berge [1] (see also [2]) more than 40 years ago. More recently, Katona and Kierstead [14] considered the following types of paths and cycles. A hypergraph P is a tight path of length , if |V pPq| “ ` 2 and there is an ordering of the vertices V pPq “ tx1,...,x `2u such that a triple e forms a hyperedge of P if and only if e “ txi,xi`1,xi`2u for some i P r s. The ordered pairs px1,x2q and px `1,x `2q are the end-pairs of P and we say that P is a tight px1,x2q-px `1,x `2q path. This deﬁnition of end-pairs is not symmetric and implicitly ﬁxes a direction on P and the order of the end-pairs. Hence, we may refer to px1,x2q as the starting pair and to px `1,x `2q as the ending pair. All other vertices of P are called internal. We sometimes identify such a path P with the sequence of its vertices x1 ...x `2. Moreover, a tight cycle C of length ě 4 consists of a path x1 ...x of length ´ 2 and the two additional hyperedges tx ´1,x ,x1u and tx ,x1,x2u. In both cases the length of a tight cycle and of a tight path is measured by the number of hyperedges and we will use the same convention for the length of cycles, paths, and walks in graphs. For simplicity we denote edges and hyperedges by xy and xyz instead of tx,yu and tx,y,zu.

Roughly speaking, one may think of tight paths and cycles as ordered hypergraphs such that “consecutive” edges overlap in exactly two vertices. Similarly, one may consider so-called loose paths and cycles, where the overlap is restricted to one vertex only. Given a hypergraph H, a cycle, tight or loose, is called Hamiltonian if it is a subhypergraph of H passing through all the vertices of H. The optimal approximate minimum pair and vertex degree conditions for the existence of loose Hamiltonian cycles were obtained in [3,15] and precise versions for large hypergraphs appeared in [6, 12]. Results on pair degree conditions implying tight Hamiltonian cycles were obtained in [19, 20]. For minimum vertex degrees, p5{9´op1qqn2{2 provides a lower bound (see Examples 1.2(i)–(iii) below), which was conjectured to be optimal. So far only suboptimal upper bounds were obtained in [11,17,18]. We close this gap here, as the following result provides an asymptotically optimal minimum vertex degree condition for tight Hamiltonian cycles.

Theorem 1.1. For every α ą 0 there exists an integer n0 such that every 3-uniform hypergraph H with n ě n0 vertices and with minimum vertex degree δpHq ě `5

˘n

2

9 ` α

2

contains a tight Hamiltonian cycle.

A recent result of Cooley and Mycroft [5] establishes the existence of an almost spanning tight cycle under the same degree condition as in Theorem 1.1. Moreover, both these results are asymptotically best possible, as the following well known examples show.

Example 1.2. (i) Consider a partition X ¨Y Y “ V of a vertex set V of size n with |X| “ rpn ` 1q{3s and let H be the hypergraph containing all triples e P V p3q such that |eXX| ‰ 2. An averaging argument shows that a Hamiltonian cycle in H would need to contain an edge e with at least two vertices from X. Consequently e Ď X and the cycle could never “leave” X. Therefore, H contains no Hamiltonian cycle (see, e.g., [17]). Moreover, we have δpHq ě p5{9 ´ op1qqn2{2.

- (ii) Similarly, one may consider a partition X ¨Y Y “ V with |X| “ r2n{3s and let H be the hypergraph consisting of all triples e P V p3q such that |e X X| ‰ 2. Again H has δpHq ě p5{9 ´ op1qqn2{2 and it contains no tight Hamiltonian cycle.
- (iii) The last example utilises the fact that every tight Hamiltonian cycle contains a matching of size tn{3u. Again we consider a partition X ¨Y Y “ V this time with |X| “ tn{3u ´ 1 and let H consist of all triples having at least one vertex in X. Consequently, H contains no matching of size tn{3u and, hence, no tight Hamiltonian cycle. On the other hand, δpHq ě p5{9 ´ op1qqn2{2.


We also would like to mention that in addition to the results on Hamiltonian cycles in 3-uniform hypergraphs discussed here, quite a few extensions and related results for k-uniform hypergraphs already appeared in the literature and we refer to the surveys [16,22] (and the references therein) for a more detailed discussion.

Organisation. The proof of Theorem 1.1 is based on the absorption method developed in [19] and we discuss this approach in Section 2.1. In Section 2.2 we introduce the main concepts and lemmas for the proof of Theorem 1.1 and deduce the theorem based on the lemmas. Each of the subsequent Sections 3–7 is devoted to the proof of one of the main lemmas from Section 2.2.

§2. Building Hamiltonian cycles in hypergraphs

- 2.1. Absorption method. In [19] the absorption method was introduced, which turned out to be a very well suited approach for extremal degree-type problems forcing the existence of spanning subhypergraphs. Our proof is also guided by this strategy, which in the context of Hamiltonian cycles can be summarised as follows: Construct an almost


spanning cycle C that contains a special, so-called absorbing path PA. The absorbing path has the special property that it can absorb the vertices outside C in such a way that a Hamiltonian cycle is created.

For example, in the context of graphs a vertex v outside C could be easily added to C if it formed a triangle with some edge xy of C, i.e., we would replace the edge xy of C by the path x-v-y of length 2. Obviously, this would have no eﬀect on the remainder of C,

since xy and the path x-v-y have the same end vertices. However, in order to repeat such a procedure for m vertices outside C it would be convenient if each such vertex would form a triangle with at least m mutually disjoint edges in PA Ď C. Then we could absorb one vertex after another in a greedy manner into PA and its extensions. However, in the proof we may not have much control on the set of vertices left out by the almost spanning cycle C.

In order to prepare for such a scenario we ensure that PA can absorb any set of vertices, which is not too large. For this it would be desirable to know that for every vertex v there exist many edges that form a triangle with v, i.e., there are many v-absorbers. Let us remark that if one would like to prove an approximate version of Dirac’s theorem for n-vertex graphs G with δpGq ě p1{2 ` αqn, then these edges would exist. Indeed, one can observe that the degree assumption forces for every vertex v at least αn2{2 triangles containing it. Based on this fact one can show that εn edges selected independently at random will contain, with high probability, at least δn v-absorbers for any vertex v, for some suitably chosen constants satisfying α ą ε ą δ ą 0. Moreover, the degree condition allows us to put all these edges onto one path, an absorbing path PA with the desired property. Consequently, the problem of ﬁnding a Hamiltonian cycle reduces to ﬁnding an almost spanning cycle C containing PA and covering all but at most δn vertices of G.

In the context of Dirac’s theorem for graphs such a “reduction” seems to be somewhat going overboard, as much simpler proofs even of the exact result are known. However, for hypergraphs no such simple proof surfaced yet and the absorption method seems to provide an appropriate approach.

For tight cycles in 3-uniform hypergraphs, the following absorbers were considered in [20]: two hyperedges xyz and yzw (which themselves form a tight px,yq-pz,wq-path of length 2) are a v-absorber if v forms a hyperedge with each of the three consecutive pairs xy, yz, and zw. These three hyperedges allow us to insert v between y and z, leading to a tight path of length three with the same end-pairs px,yq and pz,wq. It is not hard to show that the minimum pair degree condition δ2pHq ě p1{2 ` αqn for an n-vertex hypergraph H guarantees the existence of Ωpn4q v-absorbers for any vertex v, which is a good starting point for building an absorbing path in this context. However, for building such a path (and for creating an almost spanning tight cycle C) we would also need to connect the end-pairs of absorbers (and eventually the end-pairs of paths to build up C). Again, the minimum pair degree assumption was utilised for these connections in [20] and it could be shown that any pair of pairs can be connected by a relatively short tight path.

For the proof of Theorem 1.1, however, we only have a minimum vertex degree condition at hand and this calls for more complex v-absorbers and a more complicated connecting

mechanism. In [17,18] this problem was addressed by removing hyperedges containing pairs with too small degree, which led to suboptimal minimum degree conditions. For the asymptotically optimal condition of

`5 9 ` op1q˘n

2

2 new ideas for the absorbers and the connectability were required.

Roughly speaking, the absorbers we shall use here consist of two parts. First, we show that there are Ωpnq vertices z for which there exist Ωpn4q tight paths Pz “ xyy1x1, which can absorb z in the way described above, and we call such vertices z absorbable (see Figure 6.1). Moreover, for every vertex v and every absorbable vertex z there are at least Ωpn4q quadruples pa,b,c,dq such that both vertices v and z form a hyperedge with all three pairs ab, bc, and cd. In particular, abvcd and abzcd form tight paths of length three in H. Consequently, the two-edge path Pz “ xyy1x1 together with the three-edge path abzcd can absorb v without changing the end pairs of Pz and of abzcd. Indeed, we may replace z in abzcd by v and then include z between y and y1 in Pz (see Deﬁnition 6.1 and Figure 6.1). Most importantly, for every vertex v such an argument would give rise to Ωpn9q absorbers consisting of a tight path abzcd of length three and a tight two-edge path Pz, which, in principle, would allow us to apply the absorption method in a similar manner as in [20].

However, connecting the end-pairs of paths arising in the proof requires more involved changes. In [20], the minimum pair degree assumption allows a Connecting Lemma which asserts that for every pair of disjoint pairs of vertices there exists a relatively short tight path connecting them.

A similar statement in the context of Theorem 1.1 fails to be true. In fact, there might be pairs of vertices that are not contained in any hyperedge at all. More interestingly, even when restricting to pairs of degree Ωpnq, a corresponding connecting lemma might fail, as the following example shows.

Similarly as in Examples 1.2(i) and (ii) consider a hypergraph H “ pV,Eq with partition X ¨Y Y “ V , where |X| “ ξn for some ξ ă 1{3, and with an edge set deﬁned by E “ te P V p3q: |X X e| ‰ 2u. For suﬃciently large n such a hypergraph H satisﬁes the degree condition in Theorem 1.1, but every tight path P starting with a pair of vertices in X is bound to stay in X, i.e., V pPq Ď X. Owing to such examples we will deﬁne a suitable notion of connectable pairs, i.e., pairs of vertices for which a restricted Connecting Lemma can be proved (see Deﬁnition 2.5 and Proposition 2.6 in the next subsection). On the other hand, this notion must be ﬂexible and general enough, so that we can show that all paths considered in the proof have such connectable pairs as ends. In fact, this adjustment led to a few, somewhat technical, problems that we had to address here. In

the next section we present the notion of connectable pairs and the main lemmas which lead to the proof of Theorem 1.1.

- 2.2. Outline of the proof. In this section we present the proof of Theorem 1.1 based on Propositions 2.3, 2.6, 2.7, 2.9, and 2.10. These propositions will be stated here and we defer their proofs to separate later sections. The interplay of these propositions makes use of some auxiliary constants. For a simpler presentation we will note their dependencies along the way by writing a " b to indicate that b will be chosen suﬃciently small depending on a (and other constants appearing to the left of b).


More precisely, we are ﬁrst given α ą 0 by Theorem 1.1 and without loss of generality we may assume that 1 " α. Then we ﬁx the following auxiliary constants β, ζ˚, ζ˚˚, ϑ˚, ϑ˚˚ ą 0 and integers , n P N obeying the following hierarchy

1

1 n

1 " α " β,

. (2.1)

,ζ˚ " ϑ˚ " ζ˚˚ " ϑ˚˚ "

These constants will be introduced together with the propositions and the quantiﬁcation of the propositions will allow us to ﬁx them under the hierarchy given in (2.1).

Theorem 1.1 concerns n-vertex hypergraphs H “ pV,Eq with minimum vertex degree δpHq ě `5

˘n

2

2 . This degree condition implies a corresponding edge density of the link graphs deﬁned below.

9 ` α

- Deﬁnition 2.1. For a 3-uniform hypergraph H “ pV,Eq and a vertex v P V we deﬁne the link graph Lv of v as the graph with vertex set V pLvq “ V and edge set

EpLvq “ tyz: vyz P EpHqu.

Observe that v is an isolated vertex in the link graph Lv and epLvq “ dHpvq ě δpHq. The minimum degree assumption of Theorem 1.1 implies that every link graph has density at least 5{9 ` α and in Section 3 we investigate structural properties of such graphs. In particular, we shall show that these link graphs contain a “well connected” large subgraph, which will allow us to build and connect tight paths in the hypergraph (see Proposition 2.6 below). More precisely, we consider subgraphs satisfying the following property.

- Deﬁnition 2.2. A graph R is said to be pβ, q-robust if for any two distinct vertices x and y of R the number of x-y-paths in R of length is at least β|V pRq| ´1.


The following proposition, which will be proved in Section 3, asserts that all link graphs contain a robust subgraph with many vertices and edges. For a graph G and A, B Ď V pGq, let eGpA,Bq be the number of edges of G with one vertex in A and one in B.

Proposition 2.3 (Robust subgraphs). For every α ą 0 there are β ą 0 and an odd integer ě 3 such that for suﬃciently large n every n-vertex graph L “ pV,Eq with |E| ě `5

˘ n

2

2 contains an induced subgraph R Ď L satisfying

9 ` α

- (i) |V pRq| ě `2

3 ` α2

˘

n,

- (ii) eL

`

V pRq,V V pRq˘ ď αn2{4 and epRq ě `5

9 ` α2

˘ n

2

2 ´ pn´|VpRq|q

2

2 ,

- (iii) and R is pβ, q-robust.


For the proof of Theorem 1.1 we ﬁx for every vertex v P V a pβ, q-robust subgraph Rv Ď Lv as guaranteed by Proposition 2.3. In other words, after α ą 0 was revealed in Theorem 1.1, we use Proposition 2.3 to deﬁne constants β ą 0 and P N. We indicate this dependency by

1

α " β,

.

Moreover, we may assume that n is suﬃciently large, as it will be the last constant to be chosen in the proof of Theorem 1.1. Consequently, for any given hypergraph H “ pV,Eq concerned in Theorem 1.1 we can appeal to Proposition 2.3 and this way we ﬁx a pβ, qrobust subgraph Rv Ď Lv for every vertex v P V . We summarise this in the following setup.

Setup 2.4. Suppose α, β ą 0, suppose ě 3 is an odd integer, and suppose H “ pV,Eq is a 3-uniform hypergraph with |V | “ n suﬃciently large, with δpHq ě `5

˘ n

2

2 , and with pβ, q-robust subgraphs Rv Ď Lv for every v P V given by Proposition 2.3.

9 ` α

As discussed in Section 2.1, under the degree assumption of Theorem 1.1 it is not necessarily true that any two pairs of vertices can be connected at all by a tight path, even if we only consider pairs of high degree. Still there is a reasonably large collection of pairs admitting such mutual connections. In fact, pairs that are contained in suﬃciently many robust subgraphs can be connected by tight paths in H. This will be made precise in the deﬁnition of connectable pairs and in the Connecting Lemma stated below.

- Deﬁnition 2.5. Given Setup 2.4 and ζ ą 0, an unordered pair xy of vertices in V is said to be ζ-connectable if the set


Uxy “ tv P V : xy P EpRvqu

of all vertices v having xy as an edge of their robust subgraph has size |Uxy| ě ζ|V |. The ordered pair px,yq is called ζ-connectable if xy is.

The Connecting Lemma below asserts that pairs of connectable pairs can be connected by many tight paths. Section 4 is devoted to the proof of Proposition 2.6.

- Proposition 2.6 (Connecting Lemma). Given Setup 2.4 and ζ ą 0, there exists ϑ ą 0 such that every two disjoint ζ-connectable ordered pairs px,yq and pz,wq are connected by at least ϑn3 `1 tight px,yq-pz,wq-paths of length 3p ` 1q in H.

The Connecting Lemma plays a crucial role in building an absorbing path PA (guaranteed by Proposition 2.9), as well as in building an almost spanning cycle C (see Proposition 2.10 below). For the former application we shall ﬁx ζ˚ with α " ζ˚ and the Connecting Lemma will yield some constant ϑ˚ with ζ˚ " ϑ˚. Given ϑ˚ we will then choose ζ˚˚ for the latter application, obtaining ϑ˚˚ with ζ˚˚ " ϑ˚˚. This gives rise to the hierarchy

α " ζ˚ " ϑ˚ " ζ˚˚ " ϑ˚˚ ,

- as declared in (2.1). The Connecting Lemma will allow us to connect tight paths that start and end with a


connectable pair. However, in the process of building longer paths, we must not interfere with already constructed subpaths. For that we put a small reservoir of vertices aside and in the proof of Proposition 2.10 connections will only be created by using new vertices from this reservoir. The existence of such a reservoir set is given by the following proposition and its probabilistic proof is given in Section 5.

- Proposition 2.7 (Reservoir Lemma). Given Setup 2.4 and, in addition, let ϑ˚, ζ˚˚ ą 0 and suppose that ϑ˚˚ “ ϑ˚˚pα,β, ,ζ˚˚q ą 0 is given by Proposition 2.6.


2 ˚

2 n ď |R| ď ϑ2˚n such that for all disjoint pairs of ζ˚˚-connectable pairs px,yq and pz,wq there are at least ϑ˚˚|R|3 `1{2 tight px,yq-pz,wqpaths of length 3p ` 1q in H whose internal vertices belong to R.

There exists a reservoir set R Ď V with ϑ

We summarise the situation by the following setup extending Setup 2.4.

Setup 2.8. Let Setup 2.4 and constants as stated in (2.1) be given, where ϑ˚“ϑ˚pα,β, ,ζ˚q and ϑ˚˚ “ ϑ˚˚pα,β, ,ζ˚˚q are given by Proposition 2.6. In addition, let R Ď V be a reservoir set given by Proposition 2.7.

After these preparatory propositions we are ready to build a Hamiltonian cycle. As outlined above, we ﬁrst create and put aside an absorbing path PA, which at the end of the proof will allow us to ‘absorb’ an arbitrary (but not too large) set X of leftover vertices into an almost spanning tight cycle, thus creating a tight Hamiltonian cycle.

- Proposition 2.9 (Absorbing path). Given Setup 2.8, there exists a tight (absorbing) path PA which is a subhypergraph of H ´ R and has the following properties.


- (i) |V pPAq| ď ϑ˚n,
- (ii) the end-pairs of PA are ζ˚-connectable, and


- (iii) for every set X Ď V V pPAq with |X| ď 2ϑ2˚n there is a tight path in H whose set of vertices is V pPAq Y X and whose end-pairs are the same as those of PA.


The proof of Proposition 2.9 is the content of Section 6. The last proposition (see Section 7 for its proof) establishes the existence of an almost spanning tight cycle containing PA and covering all but at most 2ϑ2˚n vertices of H.

- Proposition 2.10 (Almost spanning cycle). Given Setup 2.8 and a tight absorbing path PA Ď H ´ R from Proposition 2.9, there exists a tight cycle C Ď H containing PA and passing through at least p1 ´ 2ϑ2˚qn vertices.


Finally, we observe that combining Propositions 2.9 and 2.10 implies the existence of a Hamiltonian tight cycle in H.

Proof of Theorem 1.1. Given α ą 0 we choose all auxiliary constants as described above and assume Setup 2.8. Proposition 2.9 yields an absorbing path PA and then Proposition 2.10 guarantees the existence of an almost spanning cycle C which contains the absorbing path PA and covers all but at most 2ϑ2˚n vertices. Property (iii) of the absorbing path PA allows us to absorb the remaining vertices into the cycle. This concludes the proof of Theorem 1.1.

It is left to prove Propositions 2.3, 2.6, 2.7, 2.9, and 2.10, which is the content of Sections 3–7.

§3. Robust subgraphs

In this section we establish the existence of robust subgraphs within the link graphs of the given hypergraph H. The proof of Proposition 2.3 splits into two parts. In the ﬁrst part (rendered in Lemma 3.2 below) we establish the existence of a subgraph R satisfying properties (i) and (ii) of Proposition 2.3, and the following strong connectivity property.

- Deﬁnition 3.1. A graph R is said to be µ-inseparable if δpRq ě µ|V pRq| and for every partition X ¨Y Y “ V pRq into parts of size at least µ|V pRq| we have epX,Y q ě µ2|V pRq|2.


Lemma 3.2. For every α ą 0 and suﬃciently large n every n-vertex graph L “ pV,Eq with |E| ě `5

˘ n

2

- 2 contains an induced subgraph R Ď L satisfying

- (i) |V pRq| ě `2

3 ` α2

˘

n,

- (ii) eL

`

V pRq,V V pRq˘ ď αn2{4 and epRq ě `5

9 ` α2

˘ n

2

2 ´ pn´|VpRq|q

2

2 ,

- (iii) and R is pα{72q-inseparable.




9 ` α

In the second part of the proof we deduce Proposition 2.3 from Lemma 3.2 and for that we utilise the inseparability of R to deduce the robustness. We ﬁrst give the proof of the lemma.

Proof of Lemma 3.2. We may assume α P p0,4{9s, since otherwise no graph L satisfying the assumption exists. For convenience set

α 72

(3.1) and for suﬃciently large n let L “ pV,Eq be an n-vertex graph with epLq ě `5

µ “

˘n

2

2 . Deﬁning the subgraph R. We ﬁx the maximum t P N for which there exists a partition V1 ¨Y ... ¨Y Vt “ V with

9 ` α

- (a) |V1| ě ¨¨¨ ě |Vt| ě µn{2 and
- (b)


ř

1ďiăjďt eLpVi,Vjq ď 2pt ´ 1qµ2n2.

Since the trivial partition V1 “ V satisﬁes properties (a) and (b) we know t ě 1 and from (a) we infer that t ď 2{µ. Moreover, the upper bound on t combined with (b) implies

ÿ

eLpVi,Vjq ă 4µn2 . (3.2)

1ďiăjďt

Let η P p0,1s be given by

|V1| “ ηn. It is easy to check that η ą 1{3, as otherwise

|Vi|2 2 ` 4µn2

ÿt

eLpViq ` ÿ

ÿt

epLq “

eLpVi,Vjq ă

i“1

1ďiăjďt

i“1

|Vi| 2 ` 4µn2 “ ˆ

1 3 ` 8µ˙

5 9

n2 2

n2 2

ÿt

(3.1)

n 3

ď

ď

i“1

contradicts our assumption on epLq. However, below we even show η ą 2{3 and in the proof of that we will consider a quadratic inequality where the weak bound η ą 1{3 from above rules out one interval of possible solutions. In fact, we have

pn ´ |V1|q2 2 ´ 4µn2 ě ˆ

5 9 ` α ´ p1 ´ ηq2 ´ 8µ˙

η2n2 2 ě eLpV1q ą epLq ´

n2 2

. This leads to the quadratic inequality

5 9 ` α ´ p1 ´ ηq2 ´ 8µ ðñ ˆη ´

˙ˆη ´

˙ ě

1 3

- 2

- 3


α 2 ´ 4µ.

η2 ě

Since assuming that η P p31, 23 ` 23αq would yield ˆη ´

˙ˆη ´

˙ ă ˆη ´

˙ ¨

1 3

- 2

- 3


1 3

- 2

- 3


- 2

- 3 ¨


- 2

- 3


α 2 ´

α 18 “

α 2 ´ 4µ,

α ă

α “

we have

|V1| “ ηn ě ˆ

α˙n and eLpV1q ą

- 2

- 3 `


- 2

- 3


2 9

n2 ě µn2 . (3.3) Let W “ tw1,...,wmu Ď V1 be a maximal (ordered) subset such that

ˇNLpwiq X pV1 tw1,...,wi´1uqˇ ă µn

for every i P rms. Owing to the second part of (3.3) we have V1 W ‰ ∅. Moreover, by deﬁnition V1 W induces a subgraph of minimum degree at least µn in L and we set

U “ V1 W and R “ LrUs, and below we verify that R has the desired properties.

Verifying the properties of R. We ﬁrst observe that |W| ă µn{2. Suppose for a contradiction that there exists a subset W1 “ tw1,...,wrµn{2su Ď W. Then we can replace the set V1 in the partition V1 ¨Y ... ¨Y Vt “ V by W1 ¨Y pV1 W1q and obtain a partition into t ` 1 parts, which satisﬁes (a), as

|V1 W1| ě |V1 W| “ |U| ą δpRq ě µn. (3.4) Moreover, the ordering of the vertices in W yields

eLpW1,V1 W1q ď ÿ wiPW1 ˇNLpwiq X pV1 tw1,...,wi´1uqˇ ă µn ¨ |W1| ď µ2n2, (3.5)

which shows that the partition W1 ¨Y pV1 W1q ¨Y V2 ¨Y ... ¨Y Vt “ V also satisﬁes (b). Consequently, this partition would contradict the maximal choice of t and, hence, we have indeed |W| ă µn{2.

Property (i) of Lemma 3.2 then follows from |V pRq| “ |U| “ |V1 W| “ |V1| ´ |W|

ě ˆ

˙n

ě ˆ

˙n.

- 2

- 3 `


2α 3 ´

- 2

- 3 `


(3.3)

(3.1)

µ 2

µ 2

α 2

n “ pη ´ µ2qn

ą |V1| ´

For property (ii), note that

ÿt

`

˘ “

eLpU,Viq ` eLpU,Wq

eL

U,V U

i“2

ÿt

(b )

ď 2pt ´ 1qµ2n2 ` µ2n2 ă 4µn2,

ď

eLpV1,Viq ` µn|W|

i“2

where we used t ď 2{µ in the last inequality. Consequently, the ﬁrst inequality of property (ii) follows from the choice of µ in (3.1). The second inequality is a direct

consequence of the ﬁrst and the lower bound on epLq given by the assumption of the lemma

epRq “ epLq ´ eLpU,V Uq ´ eLpV Uq ě ˆ

5 9 ` α˙

n2 2 ´

n2 2 ´

pn ´ |U|q2 2

α 2

.

For property (iii) we ﬁrst note that we already observed the required minimum degree condition δpRq ě µ|U| in (3.4). For the second property in Deﬁnition 3.1 consider an arbitrary partition X ¨Y Y “ U with parts of size at least µ|U| ą 2µn{3. We appeal to the maximality of t and infer from (b) that

eLpX,V1 Xq ą 2µ2n2 . Consequently, since V1 X “ Y ¨Y W, we have eRpX,Y q “ eLpX,Y YWq´eLpX,Wq ě eLpX,V1 Xq´eLpU,Wq ě 2µ2n2´µ2n2 “ µ2n2, which implies that R is µ-inseparable and this concludes the proof of Lemma 3.2.

Next we deduce Proposition 2.3 from Lemma 3.2.

Proof of Proposition 2.3. For α P p0,4{9s set µ “ α{72. We set to be the smallest odd integer such that

2¯6 . (3.6) For suﬃciently large n let L “ pV,Eq be an n-vertex graph with epLq ě `5

1 72 ´µ

8 µ2 ` 1 and set β “

ą

˘n

2

2 . Moreover, let U Ď V and R “ LrUs be the induced subgraph guaranteed by Lemma 3.2. In particular, V pRq “ U,

9 ` α

˙n, epRq ě ˆ

˙

|U| ě ˆ

5 9 `

- 2

- 3 `


n2 2 ´

pn ´ |U|q2 2

α 2

α 2

, and δpRq ě µ|U|. (3.7)

It remains to show that R is pβ, q-robust for the choice of β and in (3.6). This proof will be carried out in three steps. First we show that for every pair of distinct vertices x, z P V pRq there exist at least Ωpns´1q x-z-walks in R of length s “ spx,zq ď (see (3.9) below). In the second step we ensure that spx,zq can be chosen to be odd (see (3.12)) and in the last step we show that we can insist that the walks have length independent of the pair x and z. Noting that most of these walks will indeed be paths then concludes the proof. Below we give the details of each of the three steps.

First step. For an arbitrary vertex x P U and for every integer i ě 1 we deﬁne Yxi “ ty P U : there are at least pµ4{4qs|U|s´1 x-y-walks of length s in R for some s ď iu. For every i ě 2 we have Yxi Ě Yxi´1 and, consequently,

|Yxi| ě |Yx1| ě |NRpxq| ě δpRq ě µ|U|.

Next we show that for every integer i with 1 ď i ď 2{µ2 at least one of the following holds:

µ2

ˇU Yxiˇ ă µ|U| or ˇYxi`1 Yxiˇ ě

2 |U|. (3.8) If |U Yxi| ě µ|U|, then the µ-inseparability of R implies

˘ ě µ2|U|2 .

`

Yxi,U Yxi

eL

This means however that at least µ2|U|{2 vertices U Yxi have at least µ2|U|{2 neighbours in Yxi. For every such vertex in U Yxi at least 1{i ě µ2{2 proportion of its neighbours in Yxi are connected to x by walks of the same length, which implies ˇYxi`1 Yxiˇ ě µ2|U|{2 and this establishes (3.8).

From (3.8) we infer that for j “ t2{µ2u we have |U Yxj| ă µ|U|. Since x P U was arbitrary, the same conclusion holds for every vertex z P U, i.e., we also have |U Yzj| ă µ|U|. Therefore, at least |U| ´ 2µ|U| ą |U|{2 vertices y are contained in the intersection Yxj X Yzj. Each of these vertices gives rise to constants s1, s2 ď j ď 2{µ2 such that there are at least pµ4{4qs

2´1 z-y-walks of length s2. Consequently, for sy “ s1 ` s2 ě 2 there are at least pµ4{4qs

1´1 x-y-walks of length s1 and there are at least pµ4{4qs

|U|s

|U|s

1

2

y´2 x-z-walks

|U|s

y

of length sy in R passing through y. Repeating this argument for all vertices y P Yxj X Yzj shows that there is a subset of at least |U|

2 {µ44

vertices yielding the same pair ps1,s2q and, hence, the same value sy. Consequently, for some spx,zq with 2 ď spx,zq ď 4{µ2 there are

- at least µ4


8 |U| ¨ ˆ

˙spx,zq |U|spx,zq´2 ě ´µ

2¯6spx,zq |U|spx,zq´1 (3.9) x-z-walks of length spx,zq in R. It will be convenient to deﬁne for every pair of vertices x, z P U the set

µ4 4

(

Sx,z “ s ě 2: there are at least pµ{2q6s|U|s´1 x-z-walks in R

(3.10)

and (3.9) asserts Sx,z X r2,4{µ2s ‰ ∅. This concludes the discussion of the ﬁrst step.

Second step. We elaborate on (3.9) and show that we can obtain a similar formula with the additional restriction that spx,zq is odd. For that let x P U be arbitrary and consider the disjoint sets

Yxodd ¨Y Yxeven Ď U deﬁned through the parity of the integers spx,yq for which the lower bound in (3.9) holds for the number of x-y-walks in R, i.e.,

(

Yxodd “ y P U : Sx,y X r2,4{µ2s contains only odd integers

and

(

Yxeven “ y P U : Sx,y X r2,4{µ2s contains only even integers

.

Moreover, we consider the set Yxﬂex of “parity-wise ﬂexible” vertices covering the remainder of U, i.e.,

(

Yxﬂex “ y P U : Sx,y X r2,4{µ2 ` 1s contains both odd and even integers

.

Owing to the additional “`1” in the deﬁnition, the set Yxﬂex may not be disjoint from Yxodd Y Yxeven. However, all three sets together cover U. More importantly, the vertices y P Yxﬂex connect to x by many odd and many even walks of short length, which will allow us to “ﬁx” the parity for every vertex z P U by ﬁrst connecting z with some y P Yxﬂex and then, depending on the parity of the z-y-walk, continuing by a walk of diﬀerent parity to x. Obviously, for such an approach it will be useful that Yxﬂex indeed contains many vertices and, therefore, below we show

|U| 36

n 36 ě

ˇYxﬂexˇ ě

. (3.11) For that we note that Yxodd Yxﬂex induces at most µ|U|2 edges, as otherwise some vertex in y P Yxodd Yxﬂex would have at least 2µ|U| neighbours in Yxodd. Any such a neighbour y1 and its odd x-y1-walks can be used to build even x-y-walks of length at most 4{µ2 ` 1 and at least a p2{µ2 `1q´1 proportion of these walks would have the same length. Consequently, there would be some even integer contained in Sx,y X r2,4{µ2 ` 1s, which contradicts y P Yxodd Yxﬂex. Applying the same argument to Yxeven Yxﬂex tells us

˘ ď 2µ|U|2 . Since, trivially, eR

`

˘ ` eR

`

Yxodd Yxﬂex

Yxeven Yxﬂex

eR

˘ ď |U|2{4 and all edges of R not counted so far are incident with a vertex in Yxﬂex, we have

`

Yxodd Yxﬂex,Yxeven Yxﬂex

epRq ď ˆ

- 1

- 2 ` 4µ˙ |U|2


2 ` ÿ

dRpvq.

vPYxﬂex

On the other hand, we have

˙

ě ˆ

5 9 `

n2 2 ´

pn ´ |U|q2 2

(3.7)

α 2

epRq

.

For deﬁned by |U| “  n these two estimates on epRq lead to 2 n|Yxﬂex| ě

dRpvq n ě ˆ

˙ ´ p1 ´ q2 ´ ˆ

- 1

- 2 ` 4µ˙


2 ě ˆ2 ´

˙ ´

2 n ÿ

5 9 `

3 2

4 9

α 2

,

vPYxﬂex

where we used the choice µ “ α{72 ă α{8 for the last inequality. Since P p2{3,1s, the right-hand side is minimised for “ 1 and (3.11) follows.

Having established (3.11) below we shall show that for every vertex z P U there exists some odd integer s1px,zq ď 8{µ2 ` 1 such that there are at least

1 36 ´µ 2¯6s1px,zq`4

1px,zq´1 (3.12)

|U|s

x-z-walks of length s1px,zq in R. In fact, for every vertex z and every y P Yxﬂex we appeal to (3.10) and obtain many z-y-walks of length spz,yq. Since y P Yxﬂex, there is some

spy,xq P Sy,x X r2,4{µ2 ` 1s of diﬀerent parity than spz,yq and connecting the corresponding walks gives us ´µ 2¯6spz,yq |U|spz,yq´1 ˆ ´µ 2¯6spy,xq |U|spy,xq´1 “ ´µ 2¯6spz,yq`6spy,xq |U|spz,yq`spy,xq´2

x-z-walks of odd length spz,yq ` spy,xq ď 8{µ2 ` 1 passing through y. Similarly as in the ﬁrst step we repeat this argument for all vertices y P Yxﬂex and conclude that there must be a subset of |U|

`

spz,yq,spy,xq˘

36 {µ84

vertices y leading to the same pair

with odd sum and

thus to odd walks of the same length s1px,zq. Hence, there are at least |U| 36 ¨

µ4 8 ¨ ´µ 2¯6s1px,zq

1px,zq´2

|U|s

x-z-walks of length s1px,zq in R and (3.12) follows.

Third step. In the last step we ﬁnally show that R is pβ, q-robust. So far we achieved in the second step that for every pair of vertices there are many short walks of odd length connecting them. However, so far the length may depend on the pair that is connected and below we extend many walks so that they all have the same length independent of the pair. In fact, we shall show that for every pair of distinct vertices x and z in R there are at least 2β|U| ´1 x-z-walks of length in R.

For an arbitrary vertex x P U we consider its neighbourhood NRpxq and let SRpxq be its second neighbourhood, i.e., the set of vertices connected by a walk of length two with x in R. In particular, NRpxq and SRpxq might not be disjoint. Since δpRq ě µ|U|, we have

- 1

- 2


µ2

`

NRpxq,SRpxq˘ ě

2 |U|2 , (3.13) where the factor 1{2 takes into account that NRpxq and SRpxq may not be disjoint. Consequently one can show that there are subsets Nx Ď NRpxq and Sx Ď SRpxq of size at least µ2|U|{4 such that for every vertex y P Nx we have

ˇNRpxqˇ ě µ|U| and eR

µ|U| ¨ ˇNRpxqˇ ě

µ2 4 |U|

ˇNRpyq X Sxˇ ě

and, similarly, ˇNRpy1q X Nxˇ ě µ2|U|{4 for every y1 P Sx. Indeed the sets Nx and Sx exist, as otherwise we could keep deleting edges incident to vertices of small degree in NRpxq

(resp. SRpxq). More precisely, we consider vertices one by one and if v P Nx (resp. Sx) has fewer than µ2|U|{4 neighbours in Sx (resp. Nx), then we remove the edges between v and its neighbourhood in Sx (resp. Nx). However, this way less than

µ2 4 |U| ď

µ2 2 |U|2

`

˘ ¨

ˇNRpxqˇ ` ˇSRpxqˇ

edges would be deleted altogether, which by (3.13) implies that the procedure ends with a non-empty subgraph with the required degree condition. Therefore, for every vertex y1 P Sx and every odd integer s2 there exist at least pµ2{4qs2|U|s2 walks of length s2 that start in y1 and end in Nx Ď NRpxq.

Let z P U be distinct from x. For every y1 P Sx there is an odd integer s1pz,y1q ď 8{µ2 `1 such that (3.12) holds for the vertex pair pz,y1q. Since and s1pz,y1q are odd and since s1pz,y1q ď 8{µ2 ` 1 ă , for the odd integer

s2 “ ´ s1pz,y1q ´ 1 ě 1

there are pµ2{4qs2|U|s2 walks of length s2 from y1 to some vertex y P Nx Ď NRpxq, which then extends to a z-x-walk of length . In other words for every y1 P Sx there are at least

1pz,y1q´1 ˆ ˆ

˙s2

1 36 ´µ 2¯6s1pz,y1q`4

1 36 ´µ 2¯6 ´2 |U| ´2

µ2 4

2

|U|s

|U|s

ě

x-z-walks of length in R passing through y1. Repeating this argument for every vertex y1 P Sx leads by our choice of β in (3.6) on ﬁrst sight to 2β |U| ´1 x-z-walks of length . However, each walk may be counted once for each of its interior vertices. Thus the total number of distinct x-z-walks arising this way is at least 2β|U| ´1 and for suﬃciently large n at least half of these walks are indeed paths of length . Since x and z were arbitrary this shows that R is pβ, q-robust and concludes the proof of Proposition 2.3.

We close this section with the observation that two graphs R and R1 on the same vertex set, obtained by applications of Proposition 2.3, must share quite a few edges. This will be essential in the proof of Theorem 1.1 as it asserts that any pair of robust subgraphs from two link graphs share some edges.

Proposition 3.3. Let V be a set of n vertices and let R “ pU,Eq and R1 “ pU1,E1q be graphs on vertex sets U, U1 Ď V . If for some α ą 0 we have

|U| ě ˆ

˙n and |E| ě ˆ

˙

2 3 `

5 9 `

pn ´ |U|q2 2 and

n2 2 ´

α 2

α 2

˙n and |E1| ě ˆ

˙

|U1| ě ˆ

5 9 `

- 2

- 3 `


pn ´ |U1|q2 2 then |E X E1| ě αn2{2.

n2 2 ´

α 2

α 2

Proof. Deﬁne the real numbers , 1, and η by |U| “  n, |U1| “ 1n, and |E X E1| “ η

n2 2

. The assumptions on the sizes of U and U1 assert

 , 1 P “2

‰

. (3.14) Similarly, the assumptions on |E| and |E1| and the sieve formula yield

3 ` α2,1

|E Y E1| ě ˆ

10 9 ` α ´ p1 ´ q2 ´ p1 ´ 1q2 ´ η˙

n2 2

. (3.15) On the other hand, we have

ˆ

˙ Y ˆ

˙

˙. Now |U X U1| ě p ` 1 ´ 1qn and by (3.14) the expression ` 1 ´ 1 is positive, so ˇE Y E1ˇ ď ` 2 ` p 1q2 ´ p ` 1 ´ 1q2˘ n2 2

ˇ “ ˆ|U|

˙ ` ˆ|U1| 2

˙ ´ ˆ|U X U1| 2

U1 2

U 2

|E Y E1| ď ˇ

2

. Together with (3.15) this gives

10

9 ` α ´ p1 ´ q2 ´ p1 ´ 1q2 ´ η , i.e.,

2 ` p 1q2 ´ p ` 1 ´ 1q2 ě

1 9 ` α .

p ´ 1q2 ` η ě

But (3.14) implies p ´ 1q2 ă 1{9, and thus we have indeed η ě α. Corollary 3.4. Given Setup 2.4 we have |EpRuq X EpRvq| ě αn2{2 for all u,v P V . Proof. By Proposition 2.3(i) and (ii) the graphs Ru and Rv satisfy the assumptions of Proposition 3.3.

§4. Connectable pairs

In this section we establish the Connecting Lemma (Proposition 2.6) and, therefore, justify the notion of connectable pairs from Deﬁnition 2.5 by showing that such pairs indeed can be connected by tight paths in H.

- Proof of Proposition 2.6. Let ζ ą 0 be given and set


ˆ

˙ 2´1 ˆ

˙ `1 . (4.1)

- 1

- 2


- 2

- 3


αβζ 2

ϑ “

Let px,yq and pz,wq be two disjoint ζ-connectable pairs of vertices. We recall Deﬁnition 2.5, set t “ rζns, and let

tup1q,...,uptqu Ď Uxy as well as tvp1q,...,vptqu Ď Uzw

be arbitrary t-subsets of Uxy and Uzw, respectively. Let us deﬁne

Iab “ i P rts: ab P EpRupiqq X EpRvpiqq( for any ordered pair pa,bq of vertices from V . Then double counting shows that ÿ

ÿt i“1ˇEpRupiqq X EpRvpiqqˇ ě

α 2

n2t, (4.2)

|Iab| “

pa,bqPV 2

where the last inequality follows from Corollary 3.4. We intend to estimate the number T of all tight px,yq-pz,wq-walks of the form

xyupi1qr1r2upi2q...r ´2r ´1upip `1q{2qqabvpj1qs1s2vpj2q...s ´2s ´1vpjp `1q{2qqzw , (4.3)

where tight walks are deﬁned similarly like tight paths, but vertices are allowed to repeat. Such walks can be represented by sextuples

`

˘ P rtsp `1q{2 ˆ rtsp `1q{2 ˆ V ´1 ˆ V ´1 ˆ V ˆ V.

áı,á,ár,ás,a,b

Intuitively, these walks connect px,yq to pz,wq via an arbitrary “middle pair” pa,bq (see Figure 4.1). The construction of such walks can be reduced to a 2-uniform problem in link graphs by demanding that for every k P rp ` 1q{2s we have:

- (a) ik,jk P Iab,
- (b) yr1 ...r ´1a is a path in Rupi

kq,

- (c) and bs1 ...s ´1z is a path in Rvpj


kq. In other words, if T˚ denotes the number of sextuples

`

˘

satisfying the conditions (a), (b), and (c), then T ě T˚. Note that the hyperedges xyupi1q and vpjp `1q{2qzw are not forced by (a) and (b), but are a direct consequence of upi1q P Uxy and vpjp `1q{2q P Uzw. Similarly, the required hyperedges upip `1q{2qab and abvpj1q are a consequence of (a). On the other hand, conditions (a)–(c) imply several additional hyperedges, which are not required for the px,yq-pz,wq-walk. Hence, indeed we have T ě T˚. Below we shall show

áı,á,ár,ás,a,b

T˚ ě 2ϑn3 `1 . (4.4)

Since at most Opn3 q of the corresponding walks (4.3) can fail to be a path (due to the presence of repeated vertices), this trivially implies Proposition 2.6.

As a ﬁrst step towards the proof of (4.4) we will ﬁx for a while the middle vertices a and b and study the number Tab of possibilities to complete a walk of the desired kind by an appropriate choice of the 3 ´ 1 remaining vertices. Evidently

Tab “ RabSab , (4.5)

- vpj1q
- vpj2q


upi `1

q

2

a b

Uxy

Uzw

r ´1 s1

upi2q

r ´2 s2

s3

q

vpj `1

r4

upi1q

2

s4

r3

r2 s ´2

r1 s ´1

x y

z w

Figure 4.1. Connecting the ζ-connectable pairs px,yq and pz,wq through middle pair pa,bq using vertices from the sets Uxy and Uzw.

where Rab denotes the number of possibilities to choose i1,...,ip `1q{2 P Iab and vertices r1,...,r ´1 P V such that (b) holds and Sab has a similar meaning with respect to the numbers jk, the vertices sk, and property (c). Given any sequence ár “ pr1,...,r ´1q P V ´1 of vertices, we set

(

Dpár q “ i P Iab: yára is a path in Rupiq

. Then

Rab “ ÿ

|Dpár q|p `1q{2

árPV ´1

and from the pβ, q-robustness of Rupiq combined with property (i) of Proposition 2.3 applied for every i P Iab, we infer by means of double counting that

|Dpár q| ě |Iab| ¨ β ˆ

n˙ ´1 .

- 2

- 3


ÿ

árPV ´1

Thus a standard convexity argument shows

Rab ě n ´1|Iab|p `1q{2βp `1q{2 ˆ

˙p 2´1q{2

- 2

- 3


.

Applying this argument also to Sab, using (4.5), and summing over all pa,bq P V 2 we deduce

Tab ě ˆ

˙ 2´1

- 2

- 3


T˚ “ ÿ

β `1n2p ´1q ˆ ÿ

|Iab| `1

pa,bqPV 2

pa,bqPV 2

˙ 2´1

ě ˆ

t¯ `1 n2 ,

β `1n2p ´1q ˆ ´α 2

- 2

- 3


(4.2)

where we used Jensen’s inequality in the last step. Recalling the choice of ϑ in (4.1) and that t “ rζns entails (4.4) and this concludes the proof.

We close this section with the following immediate consequence of Deﬁnition 2.5, which we shall use at several occasions in the subsequent sections. Fact 4.1. Given Setup 2.4 and ζ ą 0, there are at most ζn3 triples px,y,zq P V 3 with xy P EpRzq such that the pair xy fails to be ζ-connectable.

Proof. If an (unordered) pair xy fails to be ζ-connectable, then it follows from Deﬁnition 2.5 that |Uxy| ď ζn and, hence, xy is an edge in Rz for at most ζ|V | “ ζn vertices z P V . Since there are at most n2 ordered pairs px,yq P V 2, the fact follows.

§5. Reservoir

In this section we focus on the Reservoir lemma (Proposition 2.7). The existence of such a reservoir set is established by a standard probabilistic argument.

- Proof of Proposition 2.7. Consider a random subset R Ď V with elements included independently with probability


˙ϑ2˚ . Consequently, |R| is binomially distributed and we infer from Chernoﬀ’s inequality that P

p “ ˆ1 ´

1 10

˘ “ op1q. (5.1) Moreover, since ϑ2n ě p4{3q

`|R| ă ϑ2˚n{2

1 3 `1

pn ě p1 ` cqEr|R|s for some suﬃciently small c “ cp q ą 0, we also have

˘ ď P´|R| ą p4{3q

pn¯ “ op1q. (5.2)

`|R| ą ϑ2˚n

1 3 `1

P

Recall that for every disjoint pair px,yq and pz,wq of ζ˚˚-connectable pairs Proposition 2.6 ensures the existence of at least ϑ˚˚n3 `1 tight px,yq-pz,wq-paths of length 3p `1q (having 3 ` 5 vertices in total). Let X “ Xppx,yq,pz,wqq be a random variable counting the number of px,yq-pz,wq-paths with all 3 ` 1 internal vertices in R. Consequently

ErXs ě p3 `1 ¨ ϑ˚˚n3 `1 . (5.3)

Since including or not including a particular vertex into R aﬀects the random variable X by at most p3 ` 1qn3 , the Azuma–Hoeﬀding inequality (see, e.g., [13, Corollary 2.27]) asserts

X ď 23ϑ˚˚ppnq3 `1˘ (5.3)

X ď 23ErXs˘ ď expˆ´

`

`

ď P

P

˙ “ exp

ErXs2 18 ¨ n ¨ pp3 ` 1qn3 q2

` ´ Ωpnq˘

. (5.4)

Since there are at most n4 pairs of ζ˚˚-connectable pairs that we have to consider, in view of (5.2), the union bound combined with (5.4), implies that a.a.s. the set R has the property that for every pair of connectable pairs at least ϑ˚˚|R|3 `1{2 tight connecting paths have all internal vertices in R. In addition, due to (5.1) and (5.2) a.a.s. the set R also satisﬁes ϑ2˚n{2 ď |R| ď ϑ2˚n. Consequently, a reservoir set R with all required properties indeed exists.

In Section 7 we will frequently need to connect ζ˚˚-connectable pairs through the reservoir. Whenever such a connection is made, the part of the reservoir that may still be used for further connections shrinks by 3 ` 1 vertices. Although Ωpnq such connections are needed, we shall be able to keep the reservoir almost intact throughout this process, which in turn guarantees that there will always be some permissible connections left.

- Lemma 5.1. Given Setup 2.8 with a reservoir set R Ď V , let R1 Ď R be an arbitrary


subset of size at most 2ϑ2˚˚n. Then for all disjoint pairs of ζ˚˚-connectable pairs px,yq and pz,wq there is a tight px,yq-pz,wq-path of length 3p ` 1q in H whose internal vertices belong to R R1.

Proof. Recalling |R| ě ϑ2˚n{2 and the hierarchy (2.1) yields |R1| ď 2ϑ2˚˚n ď ϑ

8 |R|. Moreover, every given vertex in R1 is an internal vertex of at most p3 ` 1q|R|3 tight px,yq-pz,wq-paths of length 3p `1q in H whose internal vertices belong to R. Consequently, there are still at least

˚˚

ϑ˚˚ 2 |R|3 `1 ´ |R1| ¨ p3 ` 1q|R|3 ě

ϑ˚˚ 2 |R|3 `1 ´

ϑ˚˚

8 ¨ p3 ` 1q|R|3 `1 ą 0 such paths with all internal vertices in R R1.

§6. Absorbing path

In this section we prove Proposition 2.9, that is, we establish the existence of an absorbing path. The following special hypergraph (the so-called v-absorber, see Figure 6.1a) will allow us to absorb a given vertex v into a path containing a v-absorber (see Figure 6.1b).

Deﬁnition 6.1. Given Setup 2.8 and a vertex v P V , a 9-tuple pa,b,c,d,z,x,y,y1,x1q P pV tvuq9 of distinct vertices such that

- (i) zab,zbc,zcd,zxy,zyy1,zy1x1,xyy1,yy1x1 P E, and
- (ii) the pairs ab, cd, xy, and y1x1 are ζ˚-connectable


is called a v-absorber if, in addition, vab, vbc, vcd P E.

d

x

- b
- c


y

z

v

y1

x1

a

(a) v-absorber with all hyperedges

|v<br><br>a b c d z<br><br>x y y1 x1<br><br>v<br><br>a b c d<br><br>z<br><br>x y y1 x1|
|---|


(b) v-absorber before/after absorption

Figure 6.1. A v-absorber, where the ζ˚-connectable pairs are indicated in green, hyperedges used before absorption of v are dark red and hyperedges used after absorption of v are light red.

An important property of these conﬁgurations proved in Lemma 6.7 below asserts that for every vertex v P V there exist Ωpn9q such v-absorbers. For standard probabilistic reasons this will lead us to a family F of Ωpnq set-wise mutually disjoint 9-tuples containing for each v P V at least Ωpnq absorbers (see Lemma 6.8). Owing to condition (ii) of Deﬁnition 6.1, we may then use the Connecting Lemma (Proposition 2.6) for connecting

- them, i.e., for producing an absorbing path PA of length Ωpnq, which contains for every v-absorber pa,b,c,d,z,x,y,y1,x1q P F the subpaths abzcd and xyy1x1. If at the end of the


proof of Theorem 1.1 the need to absorb v arises, we shall simply replace in PA, for one such v-absorber, the subpaths abzcd and xyy1x1 by abvcd and xyzy1x1 (see Figure 6.1b).

Towards the goal of estimating the number of v-absorbers from below, we shall at ﬁrst only deal with conﬁgurations consisting of the ﬁve vertices z, x, y, y1, and x1. In the lemma that follows we do not pay attention to connectability demands yet. For potential future references we point out that its proof requires only a less restrictive minimum degree condition than the one provided by Theorem 1.1.

- Lemma 6.2. For every hypergraph H “ pV,Eq with n vertices and δpHq ě 116 ¨ n22 there exist at least n5{284 quintuples px,y,y1,x1,zq P V 5 with the following properties:


- (i) xyz,yy1z,x1y1z,xyy1,yy1x1 P E;
- (ii) dpy,zq ą 125 n.


Proof. We consider the function f : E Ñ R deﬁned by fpx,y,zq “

n dpy,zq and note that by double counting we have

n dpx,zq

n dpx,yq

`

`

n3 2

ÿ

, (6.1)

fpx,y,zq “ n ¨ |BH| ď

xyzPE

where BH denotes the set of those pairs in V p2q that are contained in at least one edge of H. An edge e P EpHq is said to be central if fpeq ď 285 . In view of (6.1) the set C of central edges satisﬁes 285 |E C| ď n23, i.e., |E C| ď 565 n3. On the other hand, the minimum degree condition imposed on H yields |E| ě 111 n3 and thus we have

5n3 56 “

n3 11 ´

n3 11 ¨ 56 ą

n3 282

. (6.2) Next we will show the following statement.

|C| “ |E| ´ |E C| ě

- Claim 6.3. If yy1z is a central edge with dpy,y1q ě dpy,zq ě dpy1,zq, (6.3)


- then


n 28

n 28

, (6.4) and (ii) of Lemma 6.2 holds.

|Npy,zq X Npy,y1q| ě

, |Npy1,zq X Npy,y1q| ě

Proof. Let yy1z be a central edge satisfying (6.3). Due to fpy,y1,zq ď 285 we have

2n dpy,y1q

28 5

n dpy1,zq

`

ď

. Moreover, the Cauchy–Schwarz inequality yields

ˆ

˙

29 5

2 dpy,y1q

1 dpy1,zq

?2 ` 1q2 ą

`

dpy,y1q ` dpy1,zq˘ ě p

`

.

Hence

dpy,y1q ` dpy,zq ě dpy,y1q ` dpy1,zq ą 2928n, which implies (6.4).

Finally, fpy,y1,zq ď 285 , dpy,y1q ď n, and (6.3) lead to 28 5 ě

2n dpy,zq

n dpy,y1q

n dpy,zq

n dpy1,zq

ě 1 `

`

`

,

which proves (ii) of Lemma 6.2.

z

x1

x

y y1

Figure 6.2. Quintuple px,y,y1,x1,zq from Lemma 6.2 with central edge zyy1.

Having thus established the above claim, we continue with the proof of Lemma 6.2 (see Figure 6.2). To this end we remark that for every central edge yy1z satisfying (6.3) the estimates (6.4) imply that there are at least 28n choices of x and at least 28n choices of x1 such that (i) of Lemma 6.2 holds. Applying this argument to all central edges and taking (6.2) into account we deduce the existence of at least 28n5

quintuples px,y,y1,x1,zq P V 5 with the desired properties.

4

Next we prove that there are Ωpnq vertices which are capable of playing the rôle of z in many absorbers. Deﬁnition 6.4. Given Setup 2.8, a vertex z P V is said to be absorbable if there exist at least 2n4

quadruples px,y,y1,x1q P V 4 such that

21

- (a) the ﬁve triples xyz, yzy1, zy1x1, xyy1, and yy1x1 belong to E,
- (b) and the pairs xy, y1x1 are ζ˚-connectable.


- Lemma 6.5. Given Setup 2.8, there exist at least 2n


21

absorbable vertices.

Proof. Let A Ď V 5 denote the set of all quintuples px,y,y1,x1,zq satisfying the conclusion of Lemma 6.2, which then states that

n5 284

|A| ě

.

We intend to show that for “most” of these quintuples the pairs xy and x1y1 are ζ˚-connectable. This will then imply Lemma 6.5 in view of an easy counting argument.

As we shall verify below, the following three sets of “exceptional” quintuples are small:

- Q1 “ tpx,y,y1,x1,zq P A: y R V pRzqu,
- Q2 “ tpx,y,y1,x1,zq P A: y P V pRzq but tx,x1,y1u Ę V pRzqu, and
- Q3 “ tpx,y,y1,x1,zq P A: xy,x1y1 P EpRzq but one of these pairs is not ζ˚-connectableu.


zpyq ě 512n “ `1

˘

3 ` 121

If px,y,y1,x1,zq P Q1, then by clause (ii) of Lemma 6.2 we have dL

n

and due to |V pRzq| ě 23n it follows that y is incident to at least 12n edges in the link graph Lz running from V V pRzq to V pRzq. Owing to condition (ii) from Proposition 2.3 there are for each z P V at most 3αn vertices y with this property and, consequently, we have

|Q1| ď 3αn5 .

Similarly if px,y,y1,x1,zq P Q2, then at least one of the pairs xy, yy1, or x1y1 connects V pRzq to its complement in the link graph Lz, which shows

- |Q2| ď 64αn5 .

Moreover, the case ζ “ ζ˚ of Fact 4.1 leads to

- |Q3| ď 2ζ˚n5 .


Finally, taking 1 " α,ζ˚ into account we get |A pQ1 Y Q2 Y Q3q| ě ˆ

α ´ 2ζ˚˙n5 ą

9 2

1 284 ´

n5 220

.

Deﬁnition 6.4 guarantees that for at most 2n5

of the quintuples

21

px,y,y1,x1,zq P A pQ1 Y Q2 Y Q3q the vertex z can fail to be absorbable. Conversely every absorbable vertex can account for at most n4 such quintuples. Thus there are indeed at least 2n

absorbable vertices.

21

It remains to consider the other part of our absorbers, i.e., the six hyperedges spanned by a, b, c, d together with v and z (see Figure 6.1).

- Lemma 6.6. Given Setup 2.8, for every vertex v P V there are at least α4n5 quintuples pa,b,c,d,zq P V 5 such that


- (i) vab,vbc,vcd,zab,zbc,zcd P E,
- (ii) ab and cd are ζ˚-connectable,
- (iii) and z is absorbable.


Proof. For every vertex v P V and every ﬁxed absorbable vertex z P V Corollary 3.4 tells us |EpRvq X EpRzq| ě αn22 and a result due to Blakley and Roy [4] (asserting the validity of Sidorenko’s conjecture [9,21] for paths) entails that there are at least α3n4 quadruples pa,b,c,dq P V 4 forming a three-edge walk in both graphs Rv and Rz. Together with

- Lemma 6.5 this shows that there are at least 2α3


n5 quintuples pa,b,c,d,zq P V 5 satisfying properties (i) and (iii) of Lemma 6.6, and ab,cd P EpRvq X EpRzq instead of property (ii). As a consequence of Fact 4.1, however, there are at most 2ζ˚n5 such quintuples for which one of these two pairs fails to be ζ˚-connectable. As 1 " α " ζ˚ implies 2α3

21

21 ´ 2ζ˚ ą α4, the lemma follows.

- Lemma 6.6 easily implies that there are Ωpn9q v-absorbers for every vertex v P V . In

addition we can also ensure that these absorbers are outside the reservoir R.

- Lemma 6.7. Given Setup 2.8, for every v P V the number of v-absorbers in pV Rq9 is at least α5n9.

Proof. Combining Lemma 6.6 with Deﬁnition 6.4, we learn that there are at least 2α4

21

n9 9-tuples meeting all requirements from that deﬁnition except that some of the 10 vertices v,a,...,x1 might coincide. However, there can be at most 45n8 such bad 9-tuples. Moreover, at most 9ϑ2˚n9 members of V 9 can use a vertex from the reservoir and, consequently, the number of desired v-absorbers is at least

` α

4

221 ´ 45n ´ 9ϑ2˚

˘

n ě α5n.

Having established that there are at least Ωpn9q v-absorbers with connectable pairs for every v P V we can build the absorbing path by a standard probabilistic argument. First we ﬁnd a suitable selection of Ωpnq disjoint 9-tuples that contain many v-absorbers for every v, which is rendered by the following lemma. In a second step we utilise the ζ˚-connectable pairs and connect these 9-tuples to the absorbing path avoiding the reservoir set R.

- Lemma 6.8. Given Setup 2.8, there is a set F Ď pV Rq9 with the following properties:


- (i) |F| ď 8α´5ϑ2˚n,
- (ii) all vertices of every 9-tuple in F are distinct and the 9-tuples in F are pairwise disjoint,
- (iii) if pa,b,c,d,z,x,y,y1,x1q P F, then abz,bzc,zcd,xyy1,yy1x1 P E and the pairs ab,cd,xy,x1y1 are ζ˚-connectable,
- (iv) and for every v P V there are at least 2ϑ2˚n many v-absorbers in F.


Proof. Set

4ϑ2˚ α5

γ “

and consider a random selection X Ď pV Rq9 containing each such 9-tuple independently with probability p “ γn´8. Since Er|X|s ď pn9 “ γn, Markov’s inequality yields

1 2

`|X| ą 2γn

˘ ď

. (6.5)

P

Let us call two distinct 9-tuples from V 9 overlapping if there is a vertex occurring in both. Evidently, there are at most 81n17 ordered pairs of overlapping 9-tuples. Hence the random variable P giving the number of such pairs both of whose components are in X satisﬁes

ErPs ď 81n17p2 “ 81γ2n. By α " ϑ˚ we have 18γ ď ϑ˚ and thus a further application of Markov’s inequality discloses

1 4

˘ ď

˘ ď P

`

`

P ą 324γ2n

P ą ϑ2˚n

. (6.6)

P

In view of Lemma 6.7 for each vertex v P V the set Av containing all v-absorbers from pV Rq9 has the property Er|Av X X|s ě α5n9p “ α5γn “ 4ϑ2˚n. Since |Av X X| is binomially distributed, Chernoﬀ’s inequality gives for every v P V

1 5n

`|Av X X| ď 3ϑ2˚n

˘ ď exp

` ´ Ωpnq˘ ă

. (6.7)

P

- Owing to (6.5), (6.6), and (6.7) there is an “instance” F˚ of X satisfying the following: ‚ |F˚| ď 2γn, ‚ F˚ contains at most ϑ2˚n overlapping pairs, ‚ and for every v P V the number of v-absorbers in F˚ is at least 3ϑ2˚n.


To obtain the desired set F we delete from F˚ all 9-tuples containing some vertex more than once, all 9-tuples belonging to an overlapping pair, and all 9-tuples violating (iii). Then (i) is immediate from |F| ď |F˚|, (ii) and (iii) hold by construction, and for (iv) we recall that v-absorbers satisfy (iii) by deﬁnition.

Finally, we are ready to build an absorbing path and thus establish Proposition 2.9.

- Proof of Proposition 2.9. Let F Ď pV Rq9 be as obtained in Lemma 6.8. By condition (iii) from this lemma for every pa,b,c,d,z,x,y,y1,x1q P F we may consider the tight paths abzcd and xyy1x1. By (ii) these paths are mutually vertex-disjoint and by (i) the set G of


all these paths satisﬁes |G| “ 2|F| ď 16α´5ϑ2˚n. Using the connecting lemma we will now prove that there is a path PA Ď H ´ R

- (a) containing all members of G as subpaths,
- (b) whose end-pairs are ζ˚-connectable,
- (c) and whose length is at most p3 ` 6q|G|.


Essentially, the reason why such a path exists is that starting with any member of G we can construct PA by |G| ´ 1 successive applications of the connecting lemma attaching one further path from |G| in each step. When carrying this plan out, we need to avoid entering the reservoir and we need to be careful not to use the same vertex multiple times.

To show that this is possible we consider a maximal subset G˚ Ď G such that some path PA˚ Ď H ´ R has the properties (a), (b), and (c) enumerated above with G replaced by G˚. As the end-pairs of members of G are by deﬁnition ζ˚-connectable we have PA˚ ‰ ∅. From (c) and 1 " α, ´1 " ϑ˚ we infer

|V pPA˚q| ď 2 ` p3 ` 6q|G˚| ď 4 |G| ď 64 α´5ϑ2˚n ď ϑ3˚{2n (6.8) and thus our upper bound on the size of the reservoir leads to

ϑ˚n 2p3 ` 1q

|V pPA˚q| ` |R| ď 2ϑ3˚{2n ď

. (6.9)

Assume for the sake of contradiction that G˚ ‰ G. Let pz,wq be the ending pair of PA˚ and let P be an arbitrary path from G G˚ with starting pair px,yq. Since both pz,wq

and px,yq are ζ˚-connectable, Proposition 2.6 tells us that there are at least ϑ˚n3 `1 tight pz,wq-px,yq-paths of length 3p ` 1q. By (6.9) at least half of these are internally disjoint from V pPA˚q Y R. In particular, there is at least one such connection giving rise to a path PA˚˚ Ď H ´ R starting with PA˚, ending with P and satisfying

|V pPA˚˚q| “ |V pPA˚q| ` p3 ` 1q ` |V pPq| ď |V pPA˚q| ` p3 ` 6q ď 2 ` p3 ` 6qp|G˚| ` 1q.

So PA˚˚ exempliﬁes that G˚ Y tPu contradicts the maximality of G˚ and this contradiction proves that we have indeed G˚ “ G, i.e., that a path PA with the properties (a), (b), and (c) promised above does really exist.

As proved in (6.8) this path satisﬁes in particular the above condition (i) of Proposition 2.9. Moreover, (ii) is the same as (b). To ﬁnally establish (iii) of Proposition 2.9 one absorbs the up to at most 2ϑ2˚n vertices from X one by one into PA. By the discussion after

- Deﬁnition 6.1 this is possible due to (a) combined with clause (iv) from Lemma 6.8.


§7. Almost spanning cycle This section is dedicated to the proof of Proposition 2.10. Most of the work we need

- to perform concerns the construction of a long path Q in the induced subhypergraph


Hp “ H ´ V pPAq that covers “almost all” vertices, but leaves the reservoir set R “almost intact.” Besides, the end-pairs of this path should be suﬃciently connectable so that it can easily be included into C. These properties of Q are made precise by the following statement.

- Lemma 7.1. Given Setup 2.8 as well as an absorbing path PA as provided by Proposition 2.9, there is a path Q Ď Hp “ H ´ V pPAq such that


- (i) |V pHpq `R Y V pQq˘| ď ϑ2˚n,
- (ii) |V pQq X R| ď ϑ2˚˚n,
- (iii) and the end-pairs of Q are ζ˚˚-connectable. Before we prove Lemma 7.1, we deduce Proposition 2.10 from the lemma.


- Proof of Proposition 2.10. Given the path Q Ď H ´ V pPAq by Lemma 7.1, one simply connects the end-pairs of PA with the end-pairs of Q through “free vertices” from the reservoir using Lemma 5.1. The connectability assumption of that lemma is satisﬁed by condition (ii) from Proposition 2.9 and by condition (iii) from Lemma 7.1. Each of these connections uses exactly 3 ` 1 vertices of R. Consequently, it follows from Lemma 7.1(ii) that at most ϑ2˚˚n ` p3 ` 1q ă 2ϑ2˚˚n vertices from R need to be avoided and Lemma 5.1 applies. The resulting tight cycle C contains all but at most ϑ2˚n vertices from V R (see Lemma 7.1(i)). Furthermore, since |R| ď ϑ2˚n (see Setup 2.8 and Proposition 2.7) it follows that C covers all but at most 2ϑ2˚n vertices as required by Proposition 2.10.


It remains to establish Lemma 7.1. This proof will occupy the remainder of this section and, as explained in Section 2, it completes the proof of our main result. In the proof we make use of the following extension of the Erdős–Gallai theorem [8] concerning the extremal problem for long paths. We state the result of Faudree and Schelp [10, page 151] in a form tailored for our application.

Theorem 7.2 (Faudree and Schelp). If G “ pV,Eq is a graph not containing a path of length λ|V | for λ ą 1{2, then |E| ď `

λ2 ` p1 ´ λq2˘|V |2{2. Proof of Lemma 7.1. We ﬁx an integer M satisfying the conditions ϑ˚˚ "

1 n

1 M "

and M ” 2 pmod 3q. (7.1)

The desired path Q will consist of many “segments” from Hp ´ R that are connected with each other through the reservoir R (see Figure 7.1a). For technical reasons it will be helpful to assume that every segment F satisﬁes

|V pFq| ” ´1 pmod M ` 1q

and that it has ζ˚˚-connectable end-pairs. The former property of these segments allows us to think of them as being composed of several “pieces” consisting of M vertices each, such that any two consecutive pieces are connected with each other through one further

## R

| | | | | |
|---|---|---|---|---|
| | | | | |


## Q

segments of Q

pieces of a segment

(a) Segments of Q connected through R

(b) Pieces with ζ˚˚-connectable ends

Figure 7.1. Segments and pieces of the tight path Q.

vertex (see Figure 7.1b). These pieces will be taken from the set P “ P Ď Hp ´ R: P is an M-vertex tight path whose end-pairs are ζ˚˚-connectable

(

.

Roughly speaking, the strategy of the proof below is to show that a path Q of the kind just described will satisfy the conclusion of Lemma 7.1 as soon as it is “maximal” in the sense we will make precise next. To formulate this maximality condition, it will be convenient to talk not only about the path Q itself but also about the set C Ď P of pieces used in its construction. We collect all properties that we require from the pair pC,Qq into the deﬁnition that follows.

Candidates. A pair pC,Qq consisting of a subset C Ď P whose members are mutually vertex-disjoint and a tight path Q Ď Hp is said to be a candidate if

- (a) every P P C is a subpath of Q,
- (b) if P1,P2 P C with P1 ‰ P2 lie on Q in such a way that no P P C lies between them, then between P1 and P2 there is

- (i) either a single vertex
- (ii) or there are only vertices from R,


- (c) provided C ‰ ∅, the path Q starts and ends with a path from C,
- (d) and |V pQq X R| ď 19α´1 |C|.


For instance, the pair consisting of the empty set and the empty path is a candidate. Now let pC,Qq be a candidate with |C| as large as possible. Suppose we know that the set

H ´ V pPAq ´ R ´ V pQq˘ of unused vertices outside the reservoir satisﬁes

U “ V pHpq `R Y V pQq˘ “ V

`

|U| ď ϑ2˚n. (7.2)

We claim that then Q would have all the desired properties. Indeed by (7.2) it would satisfy (i) of Lemma 7.1. Since the members of C are mutually disjoint, we have |C| ď Mn so from (d) and ϑ˚˚, ´1,α " M´1 we get (ii). Moreover (c) implies part (iii) of Lemma 7.1.

Hence, for the rest of the argument we assume that (7.2) is false and intend to derive a contradiction by constructing a “better” candidate pC1,Q1q with a larger family C1. Obviously, the path of such a candidate will need to contain some vertices from U and to prepare ourself for a later stage of the argument we will now deal with the connectability properties of the robust subgraphs of these vertices. More precisely, for each u P U we deﬁne a subgraph Ru Ď Ru with the same set of vertices by deleting all edges that are not ζ˚˚-connectable. Owing to Fact 4.1 we have, in particular,

ÿ

`

epRuq ´ epRuq˘ ď

ζ˚˚ 2

n3 .

uPU

Consequently, the set

(

Ubad “ u P U : epRuq ď epRuq ´ 81αn2

satisﬁes |Ubad| ď 8ζ˚˚α´1n and, by ϑ˚,α " ζ˚˚, this leads to |Ubad| ď

- 1

- 2


ϑ2˚n. (7.3) For each u P U Ubad we introduce the real number ηu P “2

‰

by ˇV

3 ` α2,1

`

˘

ˇ “ |V pRuq| “ ηun (7.4) and observe that part (ii) from Proposition 2.3 implies

Ru

α 4 ´ p1 ´ ηuq2˙

αn2 ě ˆ

1 8

5 9 `

n2 2

`

˘ ě e

`

˘ ´

. (7.5)

e

Ru

Ru

Useful societies. Let B1,...,B|C| be the vertex sets of the paths belonging to C and ﬁx an arbitrary partition

U “ B|C|`1 ¨Y ... ¨Y Bν ¨Y B1 , with

|B|C|`1| “ ¨¨¨ “ |Bν| “ M and |B1| ă M . The sets belonging to

B “ tB1,...,Bνu will be referred to as blocks. The size of their union

B “ B1 ¨Y B2 ¨Y ... ¨Y Bν, (7.6) in view of candidacy property (b), can be bounded from below by

|B| “ Mν ě n ´ |V pPAq| ´ |R| ´ |C| ´ |B1| ě p1 ´ ϑ˚ ´ ϑ2˚qn ´ ν ´ M,

where we used bounds on |V pPAq| and |R| from Propositions 2.9 and 2.7. Thus, observing that ν ď n{M and recalling that ϑ˚ " M´1, we obtain

|B| ě p1 ´ 2ϑ˚qn. (7.7) Consequently, by (7.4) and (7.5), recalling that α " ϑ˚, for every u P U Ubad

`

˘ X B| Mν ď

2α 9 ´ p1 ´ ηuq2, (7.8)

5 9 `

pBq M2

|V

eR

Ru

ηu 1 ´ 2ϑ˚ ď ηu `

α 36

and

˘ ě

`ν

u

2

where eGpAq stands for the number of edges in GrAs, the subgraph of G induced by a subset of vertices A Ď V pGq.

A society is a set of m blocks, where m “ 1 ` R

V . (7.9)

36 α

`mν˘

The collection of all

societies will be denoted by S.

- Deﬁnition 7.3. A society S P S is said to be useful for a vertex u P U Ubad if for its union S “ ŤS and the real number τ deﬁned by |S X V pRuq| “ τ|S|,


S X V pRuq˘ ě ˆ

α 9 ´ p1 ´ ηuqp1 ` ηu ´ 2τq˙ |S|2

5 9 `

u`

. The following claim may explain the terminology used in Deﬁnition 7.3.

eR

2

- Claim 7.4. If a society S P S is useful for a vertex u P U Ubad, then the graph Ru contains a graph path on 32pM ` 1qpm ` 6q vertices all of which belong to S “ ŤS.


Proof. Notice that by (7.1) the number 23pm ` 6qpM ` 1q is indeed an integer. Since αm ě 36 ` α, it follows from α " M´1 and (7.9) that

6pm ` 6q αm ´ 36 ď M ,

whence

˘ “ ˆ

˙Mm.

- 2

- 3pM ` 1qpm ` 6q ď


2 3

- 2

- 3 `


`pm ` 6q ` pαm ´ 36q{6

α 9

M

`2 3 ` α9

˘

Thus it suﬃces to ﬁnd a path in the graph Ru traversing

Mm vertices all of which belong to S “ ŤS. Let us deﬁne a real number by

pMmq2 2 “

|S|2 2

u`

S X V pRuq˘ “

. Clearly τ2 ě and the deﬁnitions of τ and yield

eR

|S X V pRuq|2 2

u`

S X V pRuq˘ “ τ2 ¨

. (7.10)

eR

Moreover, the usefulness of S implies

5 9 `

α 9 ´ p1 ´ ηuqp1 ` ηu ´ 2τq, (7.11)

τ2 ě ě

which may be reformulated as

˙ ě

α 9 ` ˆηu ´

˙ˆηu `

- 2

- 3 ´ 2τ˙ . (7.12)


τ ˆτ ´

- 2

- 3


- 2

- 3


We have deﬁned ηu in (7.4) so that ηu ě 23 ` α2. Consequently, if τ ă 23 ` α9, then α 9 ` ˆηu ´

˙ˆηu `

- 2

- 3 ´ 2τ˙ ą


α 9 ą τ ˆτ ´

˙ ,

- 2

- 3


- 2

- 3


a contradiction with (7.12). This proves that

2 3 `

α 9

. (7.13)

τ ě

The right-hand side of (7.11) rewrites as 59 ` α9 ´ p1 ´ τq2 ` pηu ´ τq2 and for this reason we have

5 9 `

α 9 ´ p1 ´ τq2 . (7.14)

ě

- Owing to (7.13), we deduce from Theorem 7.2 (applied with λ “ p2{3 ` α{9q{τ to the


induced subgraph of Ru on the set S X V pRuq of size τ|S| “ τmM) that the failure of our claim would imply

˜ˆ 2

˙2¸ |S X V pRuq|2 2

˙2 ` ˆ1 ´

- 2

- 3 ` α9 τ


|S X V pRuq|2 2

3 ` α9 τ

u`

S X V pRuq˘ ď

(7.10“ ) eR

τ2 ¨

.

Consequently, we arrive at ˆ

˙2 ` ˆτ ´

˙2 ě

- 2

- 3 `


- 2

- 3 ´


5 9 `

(7.14)

α 9

α 9

α 9 ´ p1 ´ τq2 ,

ě

whence

ˆ

˙2 ` ˆ

˙2 ě

- 2

- 3 `


1 3 ´

5 9 `

α 9

α 9

α 9

, i.e.,

2 27

2 81

1 9

α2 ě

α `

α , contrary to 1 " α. This completes the proof of Claim 7.4. A counting argument shows that there exists a society that is useful for many vertices.

Claim 7.5. There is a society S1 P S useful for at least 18α |U Ubad| vertices u P U Ubad.

Proof. The claim follows by double counting from the assertion that for every u P U Ubad the number of useful societies is at least 18α |S|, which we verify below. For that consider a vertex u P U Ubad. Suppose that γ

`mν˘

of all |S| “ `mν˘

societies are useful for u. For i P rνs set

|Bi X V pRuq| “ τiM and for all i and j with 1 ď i ă j ď ν set

Bi X V pRuq,Bj X V pRuq˘ “ ijM2 . By Deﬁnition 7.3, if the society S “ tB1,...,Bmu is not useful for u, then ÿ

u`

eR

α 9 ´ p1 ´ ηu2q˙

pS X V pRuqq M2 ă ˆ

5 9 `

m2 2 ` p1 ´ ηuqm ÿ

eR

ij ď

τi .

u

1ďiăjďm

1ďiďm

If S is useful we still have the trivial bound ÿ

˙.

ij ď ˆ

m 2

1ďiăjďm

Summing over all societies we infer ˆ

˙ ÿ

ij ď γˆ

˙ˆ

˙ ` ˆ

˙ˆ

α 9 ´ p1 ´ ηu2q˙

ν ´ 2 m ´ 2

5 9 `

m2 2

ν m

m 2

ν m

1ďiăjďν

˙ ÿ

` p1 ´ ηuqmˆ

ν ´ 1 m ´ 1

τi .

1ďiďν

`mν´´22

˘`ν

˘ “ `mν˘`m

˘

Dividing by

one learns that the set B introduced in (7.6) satisﬁes eR

2

2

pBq ´ ř

ˆ

α 9 ´ p1 ´ ηu2q˙`2p1´ηuq

5 9 `

pBiq M2

|V pRuq X B| Mν

1ďiďν eR

m m ´ 1

m m ´ 1

˘ ď γ`

`ν

.

u

u

2

Owing to

˘ M2

`M

ř

1 ν ´ 1 ď

2 ν “

2M |B|

3M n ď

pBiq M2

(7.7)

1ďiďν eR

ν

α 108

2

˘ ď

˘ ď

ď

`ν

`ν

u

2

2

and (7.8) this yields 5 9 `

α 36¯˙ ,

α 108 `ˆ1 `

˙ˆ

α 9 ´ p1 ´ ηu2q ` 2p1 ´ ηuq´ηu `

2α 9 ´p1´ηuq2 ď γ`

1 m ´ 1

5 9 `

whence

1 m ´ 1

α 9 ď γ `

α 108 `

α 18p1 ´ ηuq `

.

Hence, the choice of m in (7.9) and the bound ηu ą 23 yield indeed that γ ě 18α .

For the rest of the proof let S1 from Claim 7.5 be ﬁxed. By (7.3) and the purported falsity of (7.2) this means that the set

U1 “ tu P U Ubad: S1 is useful for uu satisﬁes |U1| ě αϑ

2 ˚

36 n. Now we apply Claim 7.4 to each u P U1. Each time the outcome may be regarded as a sequence of 23pM ` 1qpm ` 6q distinct vertices from the set S1 “ ŤS1. Due to |S1| “ Mm there are no more than pMmq! such sequences and thus there is a set U2 Ď U1 with

1 3pM ` 1qpm ` 6q ´ 1

αϑ2˚n 36pMmq! ě

|U2| ě

such that all graphs Ru with u P U2 contain a common path W on 23pM ` 1qpm ` 6q vertices.

Augmenting Q. Using the vertices of W and 13pM ` 1qpm ` 6q ´ 1 arbitrary vertices from U2 we obtain a tight path T Ď pHp ´ Rq with |V pTq| “ pM ` 1qpm ` 6q ´ 1 and every vertex of T with a position divisible by 3 is a vertex from U2 (see Figure 7.2).

## U2 T

## W

Figure 7.2. Tight path T on the graph path W of ζ˚˚-connectable pairs.

Next we split the path T into pm ` 6q tight paths P1,...,Pm`6 on M vertices each such that T “ P1x1P2x2 ...xm`5Pm`6 for some x1,...,xm`5 P V . In fact, owing to (7.1) the vertices x1,...,xm`5 have a position divisible by 3 on the path T and, therefore, they belong to U2. Consequently, the end-pairs of the paths P1,...,Pm`6 consist of consecutive vertices from W and, hence, they are ζ˚˚-connectable. (This is the reason why we passed from the graphs Ru to the graphs Ru in the beginning of the argument.) In other words,

P1,...,Pm`6 P P .

Now let C´ be the collection of those paths from C whose vertex sets belong to the society S1, i.e., the paths from C´ Ď C are blocks from the society S1, and put

C0 “ pC C´q Y tP1,...,Pm`6u.

Since |C´| ď |S1| “ m, we have |C0| ě |C|`6 and thus to derive the desired contradiction it is enough to construct a path Q0 such that pC0,Q0q is a candidate. The idea for doing so is to take the subpaths into which the removal of C´ splits Q as well as the path T and to connect all of them by means of Lemma 5.1. Of course we may also need to remove several vertices of the type mentioned in condition (b)(i) and in case C´ should contain the initial or terminal part of Q we might also need to disregard some R-vertices in order to achieve that Q0 satisﬁes (c). The things that remain to be checked are

- (1) that we still have enough space in the reservoir to create the desired connections by applications of Lemma 5.1
- (2) and that the new pair pC0,Q0q will again obey condition (d).


Since |C´| ď m at most m ` 1 successive applications of Lemma 5.1 are required to connect all pieces for building Q0. Since pC,Qq satisﬁes (d), we know

19 |C| α ď

19 n αM ď ϑ2˚˚n ´ p3 ` 1qm

|V pQq X R| ď

and, hence, there arises no problem with (1).

Utilising the same condition (d) more carefully we obtain |V pQ0q X R| ď |V pQq X R| ` p3 ` 1qpm ` 1q ď

19 |C|

α ` p3 ` 1qpm ` 1q. So our choice of m in (7.9) and 1 " α, ´1 lead to

19 |C| α ` p3 ` 1qˆ

36 α ` 3˙ ď

19 α p|C| ` 6q.

|V pQ0q X R| ď

In the light of |C0| ě |C|`6 this shows that pC0,Q0q obeys condition (d) and, hence, it is indeed a candidate. As it contradicts the maximality of pC0,Q0q we have thereby proved the validity of (7.2) and as said above Lemma 7.1 is thereby proved as well.

References

- [1] C. Berge, Graphs and hypergraphs, North-Holland Publishing Co., Amsterdam-London; American Elsevier Publishing Co., Inc., New York, 1973. Translated from the French by Edward Minieka; North-Holland Mathematical Library, Vol. 6. MR0357172 (50 #9640) Ò1
- [2] J.-C. Bermond, A. Germa, M.-C. Heydemann, and D. Sotteau, Hypergraphes hamiltoniens, Problèmes combinatoires et théorie des graphes (Colloq. Internat. CNRS, Univ. Orsay, Orsay, 1976), Colloq. Internat. CNRS, vol. 260, CNRS, Paris, 1978, pp. 39–43 (French, with English summary). MR539937 (80j:05093) Ò1
- [3] E. Buß, H. Hàn, and M. Schacht, Minimum vertex degree conditions for loose Hamilton cycles in 3-uniform hypergraphs, J. Combin. Theory Ser. B 103 (2013), no. 6, 658–678, DOI10.1016/j.jctb.2013.07.004. MR3127586 Ò1
- [4] G. R. Blakley and P. Roy, A Hölder type inequality for symmetric matrices with nonnegative entries, Proc. Amer. Math. Soc. 16 (1965), 1244–1245. MR0184950 Ò6


- [5] O. Cooley and R. Mycroft, The minimum vertex degree for an almost-spanning tight cycle in a 3-uniform hypergraph, Discrete Math. 340 (2017), no. 6, 1172–1179. MR3624602 Ò1
- [6] A. Czygrinow and T. Molla, Tight codegree condition for the existence of loose Hamilton cycles in 3-graphs, SIAM J. Discrete Math. 28 (2014), no. 1, 67–76, DOI10.1137/120890417. MR3150175 Ò1
- [7] G. A. Dirac, Some theorems on abstract graphs, Proc. London Math. Soc. (3) 2 (1952), 69–81. MR0047308 (13,856e) Ò1
- [8] P. Erdős and T. Gallai, On maximal paths and circuits of graphs, Acta Math. Acad. Sci. Hungar 10

(1959), 337–356 (English, with Russian summary). MR0114772 Ò7

- [9] P. Erdős and M. Simonovits, Cube-supersaturated graphs and related problems, Progress in graph theory (Waterloo, Ont., 1982), Academic Press, Toronto, ON, 1984, pp. 203–218. MR776802 Ò6
- [10] R. J. Faudree and R. H. Schelp, Path Ramsey numbers in multicolorings, J. Combinatorial Theory Ser. B 19 (1975), no. 2, 150–160. MR0412023 Ò7
- [11] R. Glebov, Y. Person, and W. Weps, On extremal hypergraphs for Hamiltonian cycles, European J. Combin. 33 (2012), no. 4, 544–555, DOI10.1016/j.ejc.2011.10.003. MR2864440 Ò1
- [12] J. Han and Y. Zhao, Minimum vertex degree threshold for loose Hamilton cycles in 3-uniform hypergraphs, J. Combin. Theory Ser. B 114 (2015), 70–96, DOI10.1016/j.jctb.2015.03.007. MR3354291 Ò1
- [13] S. Janson, T. Łuczak, and A. Ruciński, Random graphs, Wiley-Interscience Series in Discrete Mathematics and Optimization, Wiley-Interscience, New York, 2000. MR1782847 Ò5
- [14] Gy. Y. Katona and H. A. Kierstead, Hamiltonian chains in hypergraphs, J. Graph Theory 30 (1999), no. 3, 205–212, DOI10.1002/(SICI)1097-0118(199903)30:3<205::AID-JGT5>3.3.CO;2-F. MR1671170 (99k:05124) Ò1
- [15] D. Kühn and D. Osthus, Loose Hamilton cycles in 3-uniform hypergraphs of high minimum degree, J. Combin. Theory Ser. B 96 (2006), no. 6, 767–821, DOI10.1016/j.jctb.2006.02.004. MR2274077 (2007h:05115) Ò1
- [16] V. Rödl and A. Ruciński, Dirac-type questions for hypergraphs—a survey (or more problems for Endre to solve), An irregular mind, Bolyai Soc. Math. Stud., vol. 21, János Bolyai Math. Soc., Budapest, 2010, pp. 561–590, DOI10.1007/978-3-642-14444-8_16. MR2815614 (2012j:05008) Ò1
- [17] , Families of triples with high minimum degree are Hamiltonian, Discuss. Math. Graph Theory 34 (2014), no. 2, 361–381, DOI10.7151/dmgt.1743. MR3194042 Ò1, (i ), 2.1

- [18] V. Rödl, A. Ruciński, M. Schacht, and E. Szemerédi, On the Hamiltonicity of triple systems with high minimum degree, Ann. Comb. 21 (2017), no. 1, 95–117. MR3613447 Ò1, 2.1
- [19] V. Rödl, A. Ruciński, and E. Szemerédi, A Dirac-type theorem for 3-uniform hypergraphs, Combin. Probab. Comput. 15 (2006), no. 1-2, 229–251, DOI10.1017/S0963548305007042. MR2195584 (2006j:05144) Ò1, 1, 2.1
- [20] , Dirac-type conditions for Hamiltonian paths and cycles in 3-uniform hypergraphs, Adv. Math. 227 (2011), no. 3, 1225–1299, DOI10.1016/j.aim.2011.03.007. MR2799606 (2012d:05213) Ò1, 2.1

- [21] A. F. Sidorenko, Extremal problems in graph theory and functional-analytic inequalities, Proceedings of the All-Union seminar on discrete mathematics and its applications (Russian) (Moscow, 1984), Moskov. Gos. Univ., Mekh.-Mat. Fak., Moscow, 1986, pp. 99–105 (Russian). MR930303 Ò6
- [22] Y. Zhao, Recent advances on Dirac-type problems for hypergraphs, Recent trends in combinatorics, IMA Vol. Math. Appl., vol. 159, Springer, [Cham], 2016, pp. 145–165. MR3526407 Ò1


Fachbereich Mathematik, Universität Hamburg, Hamburg, Germany E-mail address: Christian.Reiher@uni-hamburg.de E-mail address: schacht@math.uni-hamburg.de

Department of Mathematics and Computer Science, Emory University, Atlanta, USA E-mail address: rodl@mathcs.emory.edu

A. Mickiewicz University, Department of Discrete Mathematics, Poznań, Poland E-mail address: rucinski@amu.edu.pl

Alfréd Rényi Institute of Mathematics, Hungarian Academy of Sciences, Budapest, Hungary

E-mail address: szemered@cs.rutgers.edu

