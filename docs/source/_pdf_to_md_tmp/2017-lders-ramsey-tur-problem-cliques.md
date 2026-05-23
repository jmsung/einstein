# arXiv:1709.03352v2[math.CO]4May2018

## THE RAMSEY-TURÁN PROBLEM FOR CLIQUES

CLARA MARIE LÜDERS AND CHRISTIAN REIHER Dedicated to Vera T. Sós

Abstract. An important question in extremal graph theory raised by Vera T. Sós asks to determine for a given integer t ě 3 and a given positive real number δ the asymptotically supremal edge density ftpδq that an n-vertex graph can have provided it contains neither a complete graph Kt nor an independent set of size δn.

Building upon recent work of Fox, Loh, and Zhao [The critical window for the classical Ramsey-Turán problem, Combinatorica 35 (2015), 435–476], we prove that if δ is suﬃciently small (in a sense depending on t), then

$ &

3t´10 3t´4 ` δ ´ δ2 if t is even,

ftpδq “

t´3 t´1 ` δ if t is odd.

%

§1. Introduction

P. Turán [15] established a new subarea of extremal combinatorics nowadays bearing his name. In the context of graphs, the fundamental question he proposed is to determine, for a given positive number n and a given graph F, the maximum number expn,Fq of edges that a graph of order n can have provided that it does not contain F as a subgraph. Turán himself gave the complete answer if F is a clique, and an asymptotically satisfactory solution for all graphs F has been obtained by the work of Erdős, Stone, and Simonovits (see [4,6]). Curiously, the corresponding problem for hypergraphs is wide open, even in the 3-uniform case.

Another branch of combinatorics related to our discussion, called Ramsey theory, was initiated by F. P. Ramsey [11] and since then it has been developed into a coherent and successful body of results. A somewhat special yet typical case of Ramsey’s original theorem asserts that if n is large enough depending on k, then no matter how one colours the edges of a complete graph of order n using two colours, there will always be a monochromatic complete subgraph of order k.

Vera T. Sós discovered a beautiful way of combining Ramsey theory with Turán theory by asking and investigating the following question: Given a positive integer n, a positive

2010 Mathematics Subject Classiﬁcation. 05C35. Key words and phrases. Ramsey-Turán problem, cliques.

1

real number m, and a graph F, what is the maximum number RTpn,m,Fq of edges that a graph G of order n can have if it does not contain F as a subgraph and αpGq ă m, i.e., if any X Ď V pGq with |X| ě m spans at least one edge?

For example, if m “ n ` 1 and F has at least one edge, then the condition on independent sets becomes vacuous and one recovers Turán’s original problem, i.e., one has RTpn,n,Fq “ expn,Fq. On the other hand, if m is very small, then by Ramsey’s theorem each graph of order n contains either a clique of order vpFq (and hence, in particular, a subgraph isomorphic to F) or an independent set of order rms, meaning that the deﬁnition of RTpn,m,Fq degenerates to the “maximum of the empty set.” Using a quantitative version of Ramsey’s theorem, this can be seen to happen, e.g., if m ă n1{vpFq and n is large. So for ﬁxed n and F the problem of determining RTpn,m,Fq is mostly dominated by Ramsey theoretic phenomena for very small m and by Turán theory for very large m. If m is of medium size, however, the problem intriguingly combines the ﬂavours of both areas. For further information on Ramsey-Turán theory the reader is referred to the comprehensive survey [12] by Simonovits and Sós.

In this article we restrict our attention to the perhaps most classical case that m “ δn for some small δ ą 0 and F “ Kt is a clique. To eliminate minor ﬂuctuations arising from small values of n one usually focuses on the Ramsey-Turán density function ft: p0,1q ÝÑ R deﬁned by

RTpn,δn,Ktq n2{2

ftpδq “ nlimÑ8

.

It is well known and easy to conﬁrm that this limit does indeed exist. Since ft is evidently a nondecreasing function of δ, a further simpliﬁcation may be achieved by passing to the Ramsey-Turán density pKtq deﬁned by

pKtq “ lim

ftpδq.

δÑ0

Perhaps surprisingly at ﬁrst, the diﬃculty of determining the quantities just introduced depends signiﬁcantly on the parity of t. The ﬁrst case where something happens is t “ 3. One has RTpn,δn,K3q ď δn2{2 because if a graph G of order n has a vertex x whose degree is at least δn, then either the neighbourhood of x is independent, which gives αpGq ě δn, or this neighbourhood spans an edge yz, in which case xyz is a triangle. This simple observation implies f3pδq ď δ for all δ ą 0. Explicit examples described by Brandt [2] show that for δ ă 13 this bound is optimal (see Proposition 2.1 and also Corollary 2.2 below), i.e., that we have f3pδq “ δ for all δ P `

˘

0, 13

; in particular, pK3q “ 0. Concerning larger odd cliques, Erdős and Sós [5] proved pK2r`1q “ r´r1 for all positive integers r, and a

quantitative version of their argument yields r ´ 1 r ď f2r`1pδq ď

r ´ 1

r ` 2δ for all positive δ.

The ﬁrst result addressing an even clique was obtained by Szemerédi [13], who proved that

pK4q ď 14. At that moment it still seemed conceivable that the truth might be pK4q “ 0. But a few years later Bollobás and Erdős [1] ruled out this possibility by exhibiting a remarkable geometric construction demonstrating the optimality of Szemerédi’s bound; that is they completed the proof of pK4q “ 41. Still later the Ramsey-Turán densities of all even cliques were determined by Erdős, Hajnal, Sós, and Szemerédi [3], the answer being

pK2rq “ 33rr´´52 for all r ě 2. (1.1) The understanding as to how fast f4pδq converges to 14 developed as follows. Szemerédi’s

original argument yields

f4pδq ď 41 ` O ´`

˘´1{2`op1q¯ .

log log 1δ

Conlon and Schacht observed independently in unpublished work that the Frieze-Kannan regularity lemma from [7] can be used to improve this to

˘´1{2¯ . Signiﬁcant further progress is due to Fox, Loh, and Zhao [8], who obtained

f4pδq ď 14 ` O ´`

log 1δ

4 ` δ ´ δ2 ď f4pδq ď 14 ` 3δ (1.2) for suﬃciently small δ and asked

1

- (1) how this gap can be narrowed down further
- (2) and whether comparable results could be proved for larger even cliques and, in particular, whether f2rpδq “ pK2rq ` Θpδq holds for all r ě 2.


Our main result addresses both questions. Much to our own surprise, it turned out that at least for δ ! r´1 there is a precise formula for the values of the Ramsey-Turán density function.

- Theorem 1.1. If r ě 2 and δ ! r´1, then f2rpδq “ 33rr´´52 ` δ ´ δ2. The hard part of this result is the upper bound and we would like to restate it here in

an elementary form, i.e., without talking about the function f2r.

- Theorem 1.2. For every integer r ě 2 there exists a real number δ˚ ą 0 such that if δ ď δ˚, then every graph G on n vertices with


αpGq ă δn and epGq ą `3r´5

˘n

2

3r´2 ` δ ´ δ2

2

contains a K2r.

Incidentally, such an exact formula does also hold for odd cliques.

- Theorem 1.3. If r ě 1 and δ ! r´1, then f2r`1pδq “ r´r1 ` δ.


Organisation. The lower bound constructions establishing that ftpδq has at least the value claimed in Theorem 1.1 and Theorem 1.3 are given in Section 2. The upper bound for the Ramsey Turán density function of odd cliques is proved in Section 3. The proof of

- Theorem 1.2 constitutes the main part of this article and occupies the Sections 4–7.

§2. The lower bounds The goal of this section is to verify the lower bounds on ftpδq from Theorem 1.1 and

- Theorem 1.3 by means of explicit constructions. To this end, we just need to combine some results from [2] and [8].


We begin by recapitulating [2, Theorem 2.1]. This statement deals with the set Ω of all pairs pd,nq of natural numbers for which there exists a triangle-free, d-regular graph on n vertices with independence number d. Of course, if pd,nq P Ω, then RTpn,d`1,K3q “ 12dn is as large as possible.

A standard blow-up argument shows that if pd,nq P Ω, then all multiples of this pair belong to Ω as well, that is we have pad,anq P Ω for all a P N. This suggest that rather than studying Ω itself one may want to focus on the set of quotients

n : pd,nq P Ω). Brandt [2] discovered constructions which show the following. Proposition 2.1. The set SX`

S “ !

d

˘XQ are subsets of S.

˘

`

˘

`

˘XQ and

`1 4, 31

0, 13

0, 13

0, 307

is dense in

. Moreover,

The “moreover”-part is not going to be used in the sequel and it has been included here for the readers information only.

- Corollary 2.2. For ﬁxed r ě 1 and δ ă 31r we have


RTpn,δn,K2r`1q ě `r´r1 ` δ ´ op1q˘n

2

2 . Proof. Let η ą 0 be given. We need to show that RTpn,δn,K2r`1q ě `r´r1 `δ ´η

˘n

2

2 holds for all suﬃciently large integers n. By Proposition 2.1 there exists a pair pd˚,n˚q P Ω such that d˚

n˚ P `

˘

. Now it suﬃces to show that

rpδ ´ ηq,rδ

RTparn˚,ad˚ ` 1,K2r`1q ě ˆ

˙ parn˚q2 2

r ´ 1 r `

d˚ rn˚

(2.1)

holds for every a P N. This is because for suﬃciently large n we can add at most rn˚ isolated vertices to a graph establishing (2.1), thus obtaining the desired lower bound on RTpn,δn,K2r`1q.

To prove (2.1) we use pad˚,an˚q P Ω and take a triangle-free, pad˚q-regular graph H on an˚ vertices with αpHq “ ad˚. Now let V “ V1 ¨Y... ¨YVr be a disjoint union of r vertex classes each of which has size an˚, and construct a graph G on V

‚ inducing on each vertex class Vi a graph isomorphic to H, ‚ in which any two vertices from diﬀerent classes are adjacent.

From K3 Ę H and the box principle it follows that K2r`1 Ę G. Every subset of V which is independent in G needs to be contained in a single vertex class, whence

αpGq “ αpHq ă ad˚ ` 1. Finally, we have

epGq “ ˆ

˙pan˚q2 ` repHq “ ˆ

˙ parn˚q2 2

r ´ 1 r `

r 2

d˚ rn˚

. Therefore, G has all the properties necessary for witnessing (2.1).

Let us proceed with essentially extremal examples for even cliques. As mentioned in the introduction, Bollobás and Erdős [1] found a geometric construction showing that RTpn,opnq,K4q ě `1

4 ` op1q˘n

2

2 . The vertex set of their graph splits into two subsets of size n2 inducing triangle-free graphs with opn2q edges. Between those sets, called A and B from now on, there is a very special quasirandom bipartite graph of density 21 ´ op1q.

To aid the readers orientation we remark that the graphs induced by A and B are not only triangle-free. As a matter of fact, they are “locally bipartite” in the sense of having rather large odd-girth. In particular, they do not contain cycles of length 5 or 7. Such properties will also play an important rôle in our proof of the upper bound (see Fact 7.7.2 below).

It is not entirely straightforward to make the asymptotic expressions in the result of Bollobás and Erdős explicit. The best quantitative analysis we are aware of has been conducted by Fox, Loh, and Zhao [8, Corollary 8.9], who obtained the following.

- Theorem 2.3. If n is suﬃciently large and ξ “ 4plog log nq3{2{plog nq1{2, then


˘

RTpn,ξn,K4q ě `1

n2 .

8 ´ ξ

Let us proceed with a discussion of [8, Theorem 1.7] and the remark thereafter. Suppose that δ P `

˘

0, 12

is ﬁxed and that n is a suﬃciently large and (just for transparency) even natural number. Let G be a graph on n vertices as obtained by Theorem 2.3. Recall that there is a partition V pGq “ A ¨YB with |A| “ |B| “ n2 of its vertex set into two subsets not

inducing triangles. Let X Ď A and Y Ď B be two random sets of size |X| “ |Y | “ pδ ´ξqn, and let G˚ be the graph obtained from G by removing all edges incident with X Y Y and then adding all edges from X to B as well as all edges from Y to A. Surely, G˚ is K4-free and all its independent sets have size less than δn. Moreover, a short calculation displayed in the proof of [8, Lemma 9.1] shows that the expected number of edges of G˚ is at least `1

4 ` δ ´ δ2 ´ op1q˘n

2

2 . Therefore, we have indeed f4pδq ě 14 ` δ ´ δ2. This construction combines with [3, Theorem 5.4] in the following way.

˘

## Proposition 2.4. If r ě 2 and δ P `

0, 3r1´2

are ﬁxed, then

RTpn,δn,K2rq ě `3r´5

3r´2 ` δ ´ δ2 ´ op1q˘n

2

2 .

Proof. Let n be suﬃciently large and, without loss of generality, divisible by 3r ´ 2. Take a set V of n vertices as well as a partition

V “ V1 ¨Y V2 ¨Y ... ¨Y Vr (2.2)

with |Vi| “ 3r2´2n for i “ 1,2 and |Vi| “ 3r3´2n for i “ 3,...,r. Construct a graph G on V whose edges are as follows.

‚ The subgraph of G induced by V1 ¨Y V2 is the graph described above exemplifying the lower bound

˘ ě p3r´22q2n2 ` 3r2´2δn2 ´ 21δ2n2 ´ opn2q, the sets V1 and V2 here playing the rôles of A and B there.

` 4 3r´2n,δn,K4

RT

‚ For i P r3,rs the graph that G induces on Vi is obtained by Corollary 2.2 and demonstrates

` 3 3r´2n,δn,K3

˘ ě 2p3r3´2qδn2 ´ opn2q. ‚ If 1 ď i ă j ď r and pi,jq ‰ p1,2q, then all pairs uv with u P Vi and v P Vj are edges of G.

RT

Evidently, every clique in G can have at most three vertices in V1 ¨Y V2 and at most two vertices in each Vi with i P r3,rs, which proves that G is K2r-free. Moreover, each independent subset of V is either contained in V1 ¨YV2 or in one of the sets Vi with i P r3,rs. Consequently, we have αpGq ă δn. Finally, a quick computation shows

2epGq “ “`p3r´42q2 ` 3r4´2δ ´ δ2

˘ ` 33prr´´22qδ ` 9pr´2qppr3´r´3q`2q224pr´2q ´ op1q‰

n2 “ `3r´5

3r´2 ` δ ´ δ2 ´ op1q˘

n2 . So altogether G has all required properties.

§3. Odd cliques

- 3.1. Overview. This section deals with the proof of Theorem 1.3. As the lower bound has already been established in Corollary 2.2, it will suﬃce to prove the following result.

Theorem 3.1. Suppose that r is a positive integer and 0 ă δ ă 2891r5. If G is a K2r`1-free graph with n vertices and αpGq ă δn, then epGq ď `r´r1 ` δ

˘n

2

2 .

Before coming to the details we would like to give an informal description of the main idea occurring in the proof of Theorem 3.1. First of all, it suﬃces to prove this result, for a somewhat larger range of δ, under the minimum degree assumption δpGq ě r´r1, for then standard arguments allow us to infer the general statement (see Proposition 3.5 below). Next it can be proved in a rather precise sense that graphs fulﬁlling this minimum degree condition and the other assumptions of Theorem 3.1 need to look almost like the graphs presented in the proof of Corollary 2.2. In particular, the edges of such graphs can be coloured red and green in such a way that

the red graph is Kr`1-free and the green graph has maximum degree δn.

In the extremal construction, the red graph was actually an r-partite Turán graph, while the green graph was the disjoint union of r triangle-free graphs each of which had n{r vertices. Applying Turán’s theorem to the red part and the inequality epGq ď ∆pGqvpGq{2 to the green part one checks easily that every graph admitting an edge colouring with the two properties above has at most

`r´r1 ` δ

˘n

2

2 edges.

We are thus left with the task of colouring the edges of every graph G as in Theorem 3.1 and having large minimum degree in the the desired way. Now in the extremal case the joint neighbourhood of a red edge has size

`r´r2 ` 2δqn, which is considerably less than the corresponding value of about r´1

r n for green edges. For the general case this suggests to deﬁne an edge to be red if its joint neighbourhood is “small” and green otherwise, and in fact this is what we shall do later in the proof of Proposition 3.5.

- 3.2. Preparations. We begin with a result saying that among any r ` 1 large-degree vertices in a graph there is a always a pair whose joint neighbourhood is “large.” This will be used later for excluding red cliques of order r ` 1.


Lemma 3.2. Given a graph G “ pV,Eq on n vertices and a set Q Ď V with |Q| “ r`1 ě 2, there exist distinct x,y P Q with |Npxq X Npyq| ě r´r1`

dpxq ` dpyq˘ ´ rr´`11n. Proof. Notice that for every integer k with 0 ď k ď r ` 1 we have

kpr ´ 1q ´ `r

˘ “ `k

˘ ´ `r´k

˘ ď `k

˘

.

2

2

2

2

Thus writing Qp2q for the collection of all two-element subsets of Q and Wk for the set of all vertices in V with exactly k neighbours in Q we have

ÿ

˘ “ pr ´ 1q ÿ

`r´r1`

dpxq ` dpyq˘ ´ rr´`11n

dpxq ´ `r

˘

n

2

xyPQp2q

xPQ

rÿ`1

rÿ`1

˘|Qk| “ ÿ

`

kpr ´ 1q ´ `r

˘˘|Qk| ď

`k

“

|Npxq X Npyq|,

2

2

k“0

k“0

xyPQp2q

from which the desired result follows immediately. In view of Turán’s theorem, this has the following consequence.

- Corollary 3.3. If G is a graph on n vertices, then for every positive integer r there are at


2r n2 edges xy P EpGq with |Npxq X Npyq| ă r´r1`

dpxq ` dpyq˘ ´ rr´`11n. l

most r´1

The next lemma collects some facts about edge-maximal K2r`1-free graphs with large minimum degree and small independence number. Lemma 3.4. Let r ě 2 and 0 ă δ ă 21r. Suppose that G is an edge-maximal K2r`1-free graph on n vertices with αpGq ă δn and δpGq ě r´r1n.

- (i) We have ∆pGq ă `r´r1 ` 2rδ

˘

n.

- (ii) Every Q Ď V pGq with |Q| ě `2r´3

2r ` rδ

˘

n induces a K2r´2.

- (iii) If an edge xy of G satisﬁes Npxq Y Npyq ‰ V pGq, then


|Npxq X Npyq| ě dpxq ` dpyq ´ `r´r1 ` 8rδ

˘

n.

Proof. Notice that δn ą αpGq ě 1 and our upper bound on δ entail n ą 2r. Thus the maximality of G among K2r`1-free graphs on V pGq implies that every vertex of G is in a K2r.

For the proof of (i) we consider an arbitrary vertex x P V pGq and let T denote the vertex set of a K2r in G containing x. For every t P T the joint neighbourhood of T ttu is an independent set, since otherwise G would contain a K2r`1. Consequently, each of these joint neighbourhoods contains fewer than δn vertices, whence

ÿ

dptq ă p2r ´ 2qn ` 2rδn.

tPT

˘

Taking the minimum degree condition on G into account we deduce dpxq ă pr´r1 ` 2rδ

n and, as x was arbitrary, (i) follows.

For the proof of (ii) we remark that the subgraph of G induced by Q has minimum

degree at least |Q| ´ nr. Let s ě 2 be maximal such that this graph contains a Ks and let Z denote the vertex set of some Ks in G. By the same argument as above we obtain

sp|Q| ´ nrq ď ÿ

|Npzq X Q| ă ps ´ 2q|Q| ` sδn

zPZ

and thus

˘

`2rr´3 ` 2rδ

n ď 2|Q| ă rsn ` sδn, which is incompatible with s ď 2r ´ 3. In other words, Q contains indeed a K2r´2.

Preparing the proof of (iii) we show ﬁrst that if v and w are distinct vertices of G with vw R EpGq, then

|Npvq Npwq| ď `r´r1 ` 4rδ

˘

n ´ dpwq. (3.1)

To this end we use the edge-maximality of G, which gives us a K2r´1 in G whose joint neighbourhood contains v and w. Denote the vertex set on some such clique by A and let J be the set of all those vertices which have at most 2r ´ 3 neighbours in A. Exploiting that the joint neighbourhood of A can contain at most δn vertices we obtain

r n ď ÿ

p2r´1qpr´1q

dpaq ď p2r ´ 3qn ` |V pGq J| ` δn,

aPA

i.e., |J| ď `r´r1 ` δ

˘

n. Since A Y tvu induces a K2r, there can be at most p2r ´ 1qδn neighbours of v outside J. The same argument applies to w as well and thus we have

|Npvq J| ` |Npwq J| ď p4r ´ 2qδn. Putting everything together one obtains

|Npvq Npwq| ď |Npvq J| ` |J Npwq| ď |Npvq J| ` |Npwq J| ` |J| ´ dpwq ď p4r ´ 2qδn ` `r´r1 ` δ

˘

n ´ dpwq, which is slightly stronger than the estimate (3.1).

We are now ready to verify (iii). Let xy denote an arbitrary edge of G and suppose that Npxq Y Npyq ‰ V pGq. This means that there exists a further vertex z with xz,yz R EpGq and two applications of (3.1) reveal

|Npxq X Npyq| ě |Npzq| ´ |Npzq Npxq| ´ |Npzq Npyq| ě dpxq ` dpyq ` dpzq ´ 2

`r´r1 ` 4rδ

˘

n ě dpxq ` dpyq ´ `r´r1 ` 8rδ

˘

n, as desired.

- 3.3. Counting edges. Next we prove a version of our intended result for graphs satisfying a minimum degree condition.


- Proposition 3.5. Suppose that r is a positive integer and 0 ă δ ă 171r3. If G is a K2r`1-free


graph with n vertices, δpGq ě r´r1n, and αpGq ă δn, then epGq ď `r´r1 ` δ

˘n

2

2 .

Proof. Adding further edges to G may create a K2r`1 but cannot destroy any of the other assumptions and thus we may assume that G is actually an edge-maximal K2r`1-free graph. Let us colour an edge xy of G red if |Npxq X Npyq| ă r´r1`

dpxq ` dpyq˘ ´ rr´`11n and green otherwise. In view of Corollary 3.3 we know that at most r´1

2r n2 edges of G are red and thus it suﬃces to prove that at most δn2{2 edges of G are green. If this failed, then some vertex x would have more than δn green neighbours and, consequently, there would exist a triangle xyz such that xy and xz are green, while the colour of yz is unknown. The deﬁnition of xy being green leads to

dpxq ` dpyq˘ ` rr´`11n, by Lemma 3.4(i) it follows that

|Npxq Y Npyq| “ dpxq ` dpyq ´ |Npxq X Npyq| ď 1r`

|Npxq Y Npyq| ď `2prr´21q ` rr´`11 ` 4δ

˘

n ă n, and hence Lemma 3.4(iii) yields

|Npxq X Npyq| ě dpxq ` dpyq ´ `r´r1 ` 8rδ

˘

n. Proceeding similarly with the green edge xz one shows

|Npxq X Npzq| ě dpxq ` dpzq ´ `r´r1 ` 8rδ

˘

n, so that altogether

|Npxq X Npyq X Npzq| ě |Npxq X Npyq| ` |Npxq X Npzq| ´ |Npxq| ě dpxq ` dpyq ` dpzq ´ 2

˘

`r´r1 ` 8rδ

n ě `r´r1 ´ 16rδ

˘

n ě `2r´3

˘

2r ` rδ

n.

Now applying Lemma 3.4(ii) to the set Q “ Npxq X Npyq X Npzq we ﬁnd a K2r`1 in G, which is absurd. Proof of Theorem 3.1. For technical reasons it is more convenient to prove a slightly weaker upper bound ﬁrst, namely

r ´ 1 r ¨

n2 ` n 2 `

δn2 2

. (3.2)

epGq ď

Arguing indirectly, let G be a K2r`1-free graph on n vertices with αpGq ă δn violating (3.2). Let X Ď V pGq be minimal with the property

r ´ 1 r ¨

|X|2 ` |X| 2 `

δn2 2

, (3.3)

epXq ą

let G1 be the subgraph of G induced by X, and write n1 “ |X|. As X cannot be empty, we may deﬁne δ1 “ δn{n1. Now we would like to apply Proposition 3.5 to G1 and δ1.

Notice that the trivial bound epXq ď |X|2{2 and (3.3) lead to n12{r ą δn2, whence

rpδ1q2 ă δ ă 2891r5. Thus we have indeed δ1 ă 171r3. Moreover, for every x P X the minimality of X yields

r ´ 1 r ¨

|X|2 ´ |X| 2 `

δn2 2

epX txuq ď

and, therefore, dpxq “ epXq ´ epX txuq ą r´r1|X|. As x P X was arbitrary, this shows that X satisﬁes the required minimum degree condition. Finally, αpG1q ď αpGq “ δn “ δ1|X| is clear.

So Proposition 3.5 discloses epXq ď

r ´ 1 r ¨

r ´ 1 r ¨

pn1q2 2 `

|X|2 ` |X| 2 `

δ1n1 ¨ n1 2 ă

δn ¨ n 2

, contrary to (3.3). Thereby our weaker estimate (3.2) is proved.

Returning to the proof of Theorem 3.1 itself we consider any graph G as described there. For every t P N let Gt be the t-blow up of G, i.e., the graph obtained from G upon replacing every vertex by an independent set consisting of t new vertices. Of course Gt is still K2r`1-free and due to αpGtq “ tαpGq ă δ|Gt| we may apply (3.2) to Gt, thus learning

r ´ 1 r ¨

n2 ` n{t 2 `

δn2 2

epGtq t2 ď

epGq “

.

As t ÝÑ 8 this yields indeed epGq ď `r´r1 ` δ

˘n

2

2 . §4. Even cliques: Overview

The entire remainder of this article is concerned with the proof of Theorem 1.2 and in the present section we would like to give an informal discussion of the strategy we shall pursue in the sequel.

As in the case of odd cliques the ﬁrst observation is that it suﬃces to focus on graphs satisfying an appropriate minimum degree condition, which is this time going to be δpGq ě 33rr´´52n. Besides, by making further sacriﬁces as to the eventual value of δ˚, we can always assume that n is suﬃciently large. For these reasons, the main work goes into the proof of Proposition 7.8 below.

So let us suppose we have a suﬃciently large K2r-free graph G with δpGq ě 33rr´´52n and αpGq ă δn, where δ is extremely small. Our task is to prove the upper bound epGq ď `3r´5

˘n

2

2 on the number of its edges.

3r´2 ` δ ´ δ2

The argument starts similar to the proof of (1.1) given in [3]. That is we apply Szemerédi’s regularity lemma and try to ﬁnd one of several conﬁgurations in the regular partition, each of which would allow us to embed a K2r. In [3] this is done by applying some Turán theoretic result to the reduced graph (see [3, Lemma 3.3]) and the assumed absence of

˘n

these conﬁgurations leads to an upper bound of the form epGq ď `3r´5

2

2 with δ1 Ñ 0

3r´2 ` δ1

- as δ Ñ 0. However, since for a given δ we are aiming at a somewhat better estimate on epGq


than [3] does, it may happen to us that this argument does not lead to immediate success. Yet there is still something we can do in order to proceed. Namely, we can prove a stability version of [3, Lemma 3.3], apply it to the reduced graph, and transfer the information thus obtained back to the original graph. In this manner, it can be shown that, in an approximate sense, our graph G does almost look like the extremal graph described in the proof of Proposition 2.4. Speciﬁcally, we ﬁnd a partition

V pGq “ A1 ¨Y ... ¨Y Ar (4.1) such that each partition class spans at most opn2q edges and the edge density between A1 and A2 is, in a hereditary sense, at most 12 ` op1q (see Proposition 5.1 below for a precise statement). Utilising the lower bound epGq ě 33rr´´52 ¨ n22, which follows from the minimum degree assumption, one can prove that these two conditions imply that the partition classes A1,...,Ar have roughly the expected sizes and that, as long as ti,ju ‰ t1,2u, almost all possible edges between Ai and Aj are present in G (see Fact 6.2 below).

When one applies Proposition 5.1 to the essentially extremal graph constructed above, one ends up getting a partition which is to some extent similar to (2.2), but it does not necessarily agree with it. More precisely, one could show that, perhaps after an appropriate permutation of the indices, one has

řr

i“1 |Ai Vi| “ opnq. But the constant implied in the o-notation here could be extremely large in comparison to δ and thus it seems desirable to produce a better partition before one starts deriving the asymptotically optimal upper bound on epGq.

Constructing such an improved partition is the subject of Subsection 6.2. Its main result, Proposition 6.4, tells us that the graph G under consideration admits a so-called exact partition V pGq “ B1 ¨Y ... ¨Y Br satisfying a long list of properties enumerated in Deﬁnition 6.3. These conditions are rather restrictive and it might be helpful to imagine that, up to a relabeling of the indices, (2.2) is the only exact partition of the extremal graph. The proof of Proposition 6.4 starts from the partition (4.1) and is based on an iterative procedure that moves vertices around that do not properly ﬁt into the partition class they currently belong to.

Finally, in Section 7 we address the question how the knowledge of an exact partition allows us to prove an upper bound on epGq (see Proposition 7.2). The starting point there is the equation

ÿr

2epGq “

epBi,V q.

i“1

It turns out that one can separately show upper bounds for each of these terms, namely

epBi,V q ď |Bi|pn ´ |B1| ´ |B2|q ` 12|B1||B2| ` 21δnp|B1| ` |B2|q ´ 12δ2n2 (4.2) for i “ 1,2 (see Claim 7.7 below) and

epBi,V q ď |Bi|pn ´ |Bi|q ` δn|Bi| (4.3) for i “ 3,...,r (see Claim 7.5). By adding these estimates and optimising over

řr

i“1 |Bi| “ n one obtains the desired bound epGq ď `3r´5

˘n

2

2 .

3r´2 ` δ ´ δ2

Notice that there are two cases in which (4.3) is rather easy. First, if Bi happens to be triangle-free, we get epBiq ď 21δn|Bi| from αpGq ă δn and by adding the trivial upper bound epBi,V Biq ď |Bi|pn´|Bi|q the claim follows. Second, if it happens that Bi misses

- at least 2εn2 edges to V Bi for an appropriate (absolute) constant ε ą 0, then the weaker bound epBiq ď εn2, which exact partitions always satisfy, is enough to deduce (4.3). The general argument is a superposition of these two cases. That is, we will deﬁne a partition


of Bi into a triangle-free part Bi` to which the ﬁrst argument applies and another part Bi´ that misses suﬃciently many edges to V Bi to make the second approach useful.

The estimate (4.2) is much harder. Let us focus here on the case r “ 2 and i “ 1, in which many of the diﬃculties are already visible. To keep this overview simple we will also assume that every vertex in B1 sends at least 12|B2| ´ 601 n edges to B2. Recall that in the extremal example there is a set S Ď B1 of size close to δn whose members are complete to B2, whilst each vertex in B1 S sends a little bit less than 12p|B2| ` δnq edges to B2. Moreover, there is only a negligible number of edges within B1. To prove (4.2), we can deﬁne S to be set of all v P B1 that send at least, say, 167 n edges to B2 (recall that |B2| « 12n). But even if we knew that |S| « δn and were able to deal with epB1,B2q, it would still be hard to control epB1q. The key to this problem is to prove that, as in the extremal example, there are piq no edges at all from S to B1 (see Fact 7.7.3 below) and piiq no short odd cycles in B1 (see Fact 7.7.1). The latter fact helps us in the light of Lemma 7.1 below.

Needless to say, many arguments occurring in this proof are inspired by [8]. But even for r “ 2 several new ideas are needed for going beyond (1.2).

§5. Coarse structure

Now we start to analyse the structure of K2r-free graphs with huge minimum degree but without linear independent sets. The main result we shall obtain in this section reads as follows.

Proposition 5.1. Given an integer r ě 2 and a real η ą 0 there exist n0 P N and δ ą 0 such that for every K2r-free graph G on n ě n0 vertices with αpGq ă δn and δpGq ě 33rr´´52n there is a partition

V pGq “ A1 ¨Y A2 ¨Y ... ¨Y Ar with the following properties:

- (i) epAiq ď ηn2 for all i P rrs;
- (ii) if X1 Ď A1 and X2 Ď A2, then epX1,X2q ď 21|X1||X2| ` ηn2.


This will be shown by means of Szemerédi’s famous regularity lemma [14] and we commence by introducing some terminology. Given a graph G and two nonempty disjoint sets A,B Ď V pGq we say for two real numbers δ ą 0 and d P r0,1s that the pair pA,Bq is pδ,dq-quasirandom if for all X Ď A and Y Ď B the estimate ˇepX,Y q ´ d|X||Y |ˇ ď δ|A||B| holds. If we just say that the pair pA,Bq is δ-quasirandom we mean that it happens to be pδ,dq-quasirandom for d “ epA,Bq{|A||B|.

Theorem 5.2 (Szemerédi’s regularity lemma). Given ξ ą 0 and t0 P N there exists an integer T0 such that every graph G on n ě t0 vertices admits a partition

V pGq “ V0 ¨Y V1 ¨Y ... ¨Y Vt (5.1) of its vertex set such that

‚ t P rt0,T0s, |V0| ď ξ|V pGq|, and |V1| “ ... “ |Vt| ą 0, ‚ and for every i P rts the set

(

j P rts tiu: pVi,Vjq is not ξ-quasirandom

has size at most ξt.

In the literature one often ﬁnds other versions of the regularity lemma, where instead of the second bullet above it is just demanded that at most ξt2 pairs pVi,Vjq with distinct i,j P rts fail to be ξ-quasirandom. Applying such a regularity lemma to appropriate constants ξ1 ! ξ and t10 " maxpt0,ξ´1q and relocating partition classes with many irregular partners to V0 one can obtain the version stated here; this argument has been used before by Łuczak [9], who explains it in more detail.

Next we deal with certain conﬁgurations in regular partitions of graphs with small independence number which allow us to build cliques. The lemma that follows is implicit in [3, Section 4] but for reasons of self-containment we shall supply its short proof. In its formulation we work with a one-sided version of quasirandomness that is enough for our purposes: If G is a graph, a pair pA,Bq of disjoint subsets of V pGq is said to be pδ,dq-dense for δ ą 0 and d P r0,1s, if for all X Ď A and Y Ď B we have epX,Y q ě d|X||Y | ´ δ|A||B|.

Lemma 5.3. Suppose that integers a ě b ě 1 as well as a real number ϑ P p0,1s are given and set ξ “ `ϑ

˘a´1

˘a´1

, δ “ `ϑ

2

. Let H be a graph possessing a vertex partition

4

2

V pHq “ V1 ¨Y ... ¨Y Va into nonempty classes satisfying

- (a) if 1 ď i ă j ď a, then pVi,Vjq is pξ,dijq-dense for some dij P rϑ,1s;
- (b) if 1 ď i ă j ď b, then dij ě 21 ` ϑ;

- (c) if X Ď Vi and |X| ě δ|Vi| for some i P ras, then X spans at least one edge in H.


Then H contains a clique of order a ` b. Proof. We argue by induction on a ` b. In the base case, a “ b “ 1, we have δ “ 1 and by condition (c) applied to X “ V1 there is indeed an edge in H.

In the induction step we certainly have a ě 2 and we assume ﬁrst that a ą b. For every

- i P ra ´ 1s the set


Xpiq “ v P Va: |Npvq X Vi| ď ϑ2|Vi|( cannot be very large, as condition (a) yields

2|Vi||Xpiq| ě epVi,Xpiqq ě ϑ|Vi||Xpiq| ´ ξ|Vi||Va|. Together with ξ ď 2ϑa this leads to |Xpiq| ď a1|Va|. Now pick some v˚ P Va

ϑ

Ť

iPra´1s Xpiq and set Vi1 “ Npv˚q X Vi for i “ 1,...,a ´ 1. The deﬁnition of Xpiq gives |Vi1| ě ϑ2|Vi| for every i P ra ´ 1s and, hence, the sets V11,...,Va1´1 have the above properties (a), (b), and (c) for a ´ 1, ϑξ

2{4, and ϑδ{2 here in place of a, ξ, and δ there. So by the induction hypothesis the neighbourhood of v˚ contains a Ka`b´1, wherefore indeed Ka`b Ď H.

The case a “ b is similar, but instead of the sets Xpiq introduced above we consider Y piq “ v P Va: |Npvq X Vi| ď `1 2 ` ϑ2

˘|Vi|(

for i P ra´1s. Invoking condition (b) one can show |Y piq| ď a1|Va| in the same way as before and, hence, the set L “ Va

Ť

iPra´1s Y piq satisﬁes |L| ě a1|Va| ě δ|Va|. So by (c) there is an edge v˚w˚ both of whose endvertices belong to L. Since |Npv˚q X Npw˚q X Vi| ě ϑ|Vi| holds for each i P ra ´ 1s, the induction hypothesis allows us to ﬁnd a Ka`b´2 in the common neighbourhood of v˚w˚ and again we obtain Ka`b Ď H.

Suppose now that the regularity lemma has been applied, with a suﬃciently small accuracy parameter ξ, to some graph G of small independence number, meaning that for some large integer t we have a partition of V pGq such as (5.1). When one now attempts to ﬁnd a K2r in G by means of Lemma 5.3, it only matters which of the quasirandom pairs pVi,Vjq have their densities, for an appropriate ϑ ą 0, in the interval

“

˘

ϑ, 12 ` ϑ

or even in

“1 2 ` ϑ,1

‰

. We shall encode such information by the use of coloured edges in the

reduced graph, with green edges corresponding to pairs that are either irregular or too sparse to be useful, and blue (or red) edges corresponding to quasirandom pairs of medium (or large) density.

Let us say that a coloured graph is a complete graph all of whose edges have been coloured red, blue, or green. Associated with any coloured graph G, say with vertex set V , we have its so-called weight function w: V 2 ÝÑ t0,1,2u deﬁned by

$ ’&

- 0 if x “ y or xy is green,
- 1 if xy is blue,
- 2 if xy is red


wpx,yq “

’%

for all x,y P V . We will often identify G with the pair pV,wq. The degree of a vertex x of a coloured graph G “ pV,wq is deﬁned to be the sum

dpxq “ ÿ

wpx,yq

yPV

and by epGq we mean half of the sum of the degrees dpxq as x varies over V .

Two coloured graphs are said to be isomorphic if there is a colour-preserving bijection between their vertex sets. A coloured graph pV 1,w1q is a subgraph of a coloured graph pV,wq if V 1 Ď V and, additionally, w1px,yq ď wpx,yq holds for all x,y P V 1.

Next, we come to the coloured graphs which are relevant in connection with Lemma 5.3. For integers a ě b ě 1 the coloured graph on a vertices without green edges whose red edges form a clique of order b will be denoted by Ga`b,b. For every integer r ě 2 we set

- F2r “ tG2r,1,...,G2r,ru. A coloured graph is said to be F2r-free if none of its subgraphs is isomorphic to a member of F2r.


In their proof of (1.1), Erdős, Hajnal, Szemerédi, and Sós use a lemma saying that every

- F2r-free coloured graph on n vertices satisﬁes epGq ď 33rr´´52n2 (see [3, Lemma 3.3]). For the proof of Proposition 5.1 we will use a stability version of this lemma. There are various such statements, a rather strong one being the following.


- Proposition 5.4. Suppose that r ě 2 and that G is a F2r-free coloured graph on n vertices


with δpGq ą 147rr´´245 n. Then there is a partition V pGq “ W1 ¨Y ... ¨Y Wr such that all edges within the partition classes are green and there are no red edges between W1 and W2.

A somewhat lengthy proof of this result is given in [10]. For the purposes of the present work, however, it suﬃces to know only the weaker statement that follows. To keep this article as self-contained as possible, we will supply a quick sketch of its proof below.

- Proposition 5.5. Let r ě 2 and let α ą 0 be suﬃciently small. Then every F2r-free coloured graph G on n vertices with δpGq ě 2p33rr´´52q´αn admits a partition


V pGq “ W0 ¨Y W1 ¨Y ... ¨Y Wr

of its vertex set such that |W0| ď αn, all edges within the classes W1,...,Wr are green, and no edge from W1 to W2 is red.

We prepare the proof of this proposition by the following variant of [3, Lemma 3.3], which can be proved in the same way. Let RKr´1 denote a red clique of order r ´ 1 and set F2`r “ F2r Y tRKr´1u.

- Lemma 5.6. For r ě 2 every F2`r-free coloured graph G on n vertices satisﬁes epGq ď rr´´12n2 .


Proof. The case r “ 2 is clear, for a RK1 is nothing else than a vertex. So suppose r ě 3 from now on. As in [3], two consecutive applications of Zykov’s symmetrisation method [16] show that we may assume that there are is partition V pGq “ A1 ¨Y ... ¨Y Am and that for each i P rms there is a partition Ai “ Bi1 ¨Y ... ¨Y Bik

such that

i

- (i) for i P rms and j P rkis all edges within Bij are green;
- (ii) if i P rms and j,j1 P rkis are distinct, then all edges between Bij and Bij1 are blue;
- (iii) and for distinct i,i1 P rms all edges between Ai and Ai1 are red. Since G contains neither RKr´1 nor G2r,m, we have


1 ď m ď r ´ 2 and k1 ` ... ` km ď 2r ´ 1 ´ m. (5.2) Set αi “ |Ai|{n for i P rms and notice that

řm

i“1 αi “ 1. It is well known that (i) and (ii) imply epAiq ď k

i´1

2ki |Ai|2 and thus it remains to prove ÿ

ÿ

2ki αi2 ` 2

ki´1

αiαj ď rr´´21 .

1ďiďm

1ďiăjďm

`řm i“1 αi

˘2 “ 1 we get ÿm

Subtracting this from

2ki αi2 ě r´11 . The Cauchy-Schwarz inequality yields

ki`1

i“1

ÿm

ÿm

ki`1 ě `ÿm

˘2 “ 1

2ki αi2 ¨

ki`1

2ki

αi

i“1

i“1

i“1

and thus it suﬃces to show that

ÿm

ki`1 ď r´21 . (5.3)

ki

i“1

Since the estimate k`k1 ď k`62 holds for each positive integer k, it is enough to prove

ÿm

ki`2

6 ď r´21

i“1

instead and in view of (5.2) this is clear. Proof of Proposition 5.5. Since r´2

r´1 ă 33rr´´52 and α ! 1, we may suppose that epGq ą rr´´21. By Lemma 5.6 and the assumption that G be F2r-free it follows that G contains a RKr´1, say with vertex set K “ tv1,v3,...vru. The minimum degree condition and α ! 1 yield

ÿ

2r ´ 2 ´ dKpxq˘ “ ÿ

`

`

2n ´ dpvq˘ ď p6`3αrqp´r2´1qn ă 2n

vPK

xPV pGq

and, hence, there is a vertex v2 P V pGq with 2r ´ 2 ´ dKpv2q ď 1. As G contains no

- G2r,r “ RKr, it follows that v2 has exactly one blue neighbour in K and sends red edges to all other members of K. By symmetry we may suppose that v1v2 is blue. Set


‚ L “ tv1,...,vru “ K Y tv2u, ‚ Wi “ x P V pGq: if j P rrs, then wpx,vjq “ wpvi,vjq(

for i “ 1,...,r,

‚ W0 “ V pGq pW1 Y ... Y Wrq, ‚ and qpxq “ 2p3r´2q´2

`

wpv1,xq`wpv2,xq˘´3

`

wpv3,xq`...`wpvr,xq˘

for every x P V pGq.

Notice that the sets W1,...,Wr are mutually disjoint. Exploiting that G contains neither

- G2r,r nor G2r,r´1 one checks easily that ‚ all edges within one of the partition classes W1,...,Wr are green ‚ no edge from W1 to W2 is red, ‚ qpxq ě 6 for all x P V pGq, ‚ and that equality holds in the previous bullet if and only if x P W1 ¨Y ... ¨Y Wr.


It remains to show that |W0| ď αn. To this end we write |W0| ď ÿ

`

dpv1q ` dpv2q˘ ` 3

`

dpv3q ` ... ` dpvrq˘

pqpxq ´ 6q “ 2p3r ´ 5qn ´ 2

xPV pGq

and apply the minimum degree condition again.

Finally, we show the main result of this section. Proof of Proposition 5.1. Take appropriate constants

δ ! T0´1 ! t´0 1,ξ ! ϑ ! minpη,r´1q, where T0 is obtained by applying the regularity lemma to t0 and ξ, and set n0 “ t0. Consider a K2r-free graph G on n ě n0 vertices with αpGq ă δn and δpGq ě 33rr´´52n. The

regularity lemma yields for some integers t P rt0,T0s and m ě 1 a partition V pGq “ V0 ¨Y V1 ¨Y ... ¨Y Vt

- such that |V0| ď ξn, |V1| “ ... “ |Vt| “ m, and for every i P rts all but at most ξt indices

j P rts tiu have the property that pVi,Vjq is ξ-quasirandom.

Deﬁne a coloured graph H with vertex set rts by declaring a pair ij to be green if pVi,Vjq either fails to be ξ-quasirandom or has a density smaller than ϑ, blue if pVi,Vjq is ξ-quasirandom and has a density in

“

ξ, 12 ` ξ

˘

, and red otherwise. As a consequence of Lemma 5.3, H is F2r-free. Next, we will show that δpHq ě 2

`3r´5 3r´2 ´ 3ϑ

˘

t. (5.4)

To verify this, we consider an arbitrary vertex i of H and denote the numbers of its blue and red neighbours by a and b, respectively. The minimum degree condition on G yields

3r´5

3r´2mn ď

ÿt

j“0

epVi,Vjq.

On the right side of this estimate, the term corresponding to j “ 0 contributes at most ξmn, j “ i contributes at most m2, and the irregular pairs contribute at most ξtm2. Consequently we have

`3r´5 3r´2 ´ ξ

˘

mn ď m2 ` ξtm2 ` tϑm2 ` a

`1

2 ` ϑqm2 ` bm2. Using n ě mt and canceling m2 we infer

`3r´5 3r´2 ´ ξ

˘

t ď p2ϑ ` ξqt ` 1 ` 12dHpiq. So in view of t ě t0 " ϑ´1 and ξ ! ϑ we obtain dHpiq ě 2

`3r´5 3r´2 ´ 3ϑ

˘

t, which proves (5.4). By Proposition 5.5 and ϑ ! r´1 there exists a partition

rts “ W0 ¨Y W1 ¨Y ... ¨Y Wr

- such that |W0| ď 18ϑrt, all edges within W1,...,Wt are green, and no edge between W1 and W2 is red. For s P r0,rs we deﬁne


A˚s “ ď

Vi .

iPWs

Then V pGq “ V0 ¨Y A˚0 ¨Y A˚1 ¨Y ... ¨Y A˚r is a partition of V pGq and

|V0| ` |A˚0| ď ξn ` |W0|m ď pξ ` 18rϑqn ď 12ηn. This means that if we manage to show

- (a) epA˚sq ď 12ηn2 for all s P rrs,

- (b) and epX1,X2q ď 21|X1|X2| ` 12ηn2 for all X1 Ď A˚1 and X2 Ď A˚2,


then the partition V pGq “ A1 ¨Y ... ¨Y Ar deﬁned by A1 “ V0 ¨Y A˚0 ¨Y A˚1 and As “ A˚s for s P r2,rs has both desired properties.

To prove (a) we start for a given s P rrs from the decomposition

epA˚sq “ ÿ

epViq ` ÿ

epVi,Vjq.

ijPWsp2q

iPWs

Here, each of the at most t terms in the ﬁrst sum is at most m2{2. Besides, there are at most ξt2{2 terms corresponding to irregular pairs in the second sum, and each of them amounts to no more than m2. Finally, the remaining at most t2{2 terms in the second sum correspond to pairs whose density is at most ϑ. Thus we obtain

epA˚sq ď ` 1

˘

m2t2

2t ` 2ξ ` ϑ2

and due to t ě t0 and mt ď n an appropriate choice of our constants does indeed guarantee that epA˚sq ď 12ηn2.

Similarly, the proof of (b) employs

epX1,X2q “ ÿ

ÿ

epVi X X1,Vj X X2q.

iPW1

jPW2

Again the contribution caused by irregular pairs is at most ξn2{2. The remaining terms correspond to ξ-quasirandom pairs, which owing to the absence of red edges from W1 to W2 have density at most 21 ` ϑ. Consequently,

˘|Vi X X1||Vj X X2| ` ξ|Vi||Vj|ı ` 12ξn2 ď `1

”`1 2 ` ϑ

epX1,X2q ď ÿ

ÿ

iPW1

jPW2

˘|X1||X2| ` ξt2m2 ` 12ξn2 ď 12|X1||X2| ` `

2 ` ϑ

˘

n2 ď 21|X1||X2| ` 12ηn2 and the proof of Proposition 5.1 is complete.

ϑ ` 23ξ

§6. Exact partitions

- 6.1. More information. It turns out that the lower bound epGq ě 33rr´´52 ¨ n22, which follows from the minimum degree condition in Proposition 5.1, gives us further information on the sizes of the vertex classes of the partition obtained there and on the edge densities between these classes. This happens due to the following elementary inequality.


- Lemma 6.1. If for r ě 2 the real numbers a1,...,ar sum up to 1, then ÿ


aiaj ´ 12a1a2 ď 2p33rr´´52q .

1ďiăjďr

Moreover, if for some real ě 0 we have ÿ

aiaj ´ 12a1a2 ě 2p33rr´´52q ´  , (6.1)

1ďiăjďr

ˇ ď 2? for i “ 3,...,r. Proof. Deﬁne

ˇ ď 2? for i “ 1,2 and ˇai ´ 3r3´2

then ˇai ´ 3r2´2

$ &

- ai ´ 3r2´2 if i “ 1,2

- ai ´ 3r3´2 if i “ 3,...,r


αi “

% and observe that

6ai 3r ´ 2 `

4 ¨ 3 ` 9pr ´ 2q p3r ´ 2q2

3 3r ´ 2

ÿr

ÿr

ÿr

ÿr

αi2 ` α1α2 “

a2i ` a1a2 ´

a2i ` a1a2 ´

“

.

i“1

i“1

i“1

i“1

˘2 “ 1 this rewrites as

`řr

Due to

i“1 ai

αi2 ď 33rr´´52 ´ ´2

aiaj ´ a1a2¯,

ÿr

ÿ

- 1

- 2α12 ` 21α22 ` 12pα1 ` α2q2 `


i“3

iăj

which establishes the ﬁrst part of our claim. Moreover, if (6.1) holds for some ě 0 we obtain

ÿr

- 1

- 2α12 ` 21α22 ` 12pα1 ` α2q2 `


αi2 ď 2 , whence |αi| ď 2? holds for all i P rrs.

i“3

With this lemma at hand we may prove the following estimates.

- Fact 6.2. Suppose that a graph G and the partition V pGq “ A1 ¨Y ... ¨Y Ar


are as described and obtained in Proposition 5.1. Then

- ‚ ˇ|Ai| ´ 3r2´n2

ˇ ď 2 pr ` 1qη ¨ n for i “ 1,2,

- ‚ ˇ|Ai| ´ 3r3´n2


apr ` 1qη ¨ n for i “ 3,...,r,

ˇ ď 2

‚ epA1,A2q ě 21|Ai||Aj| ´ rηn2, ‚ and epAi,Ajq ě |Ai||Aj| ´ pr ` 1qηn2 whenever 1 ď i ă j ď n and pi,jq ‰ p1,2q.

Proof. The minimum degree condition δpGq ě 33rr´´52n yields epGq ě 33rr´´25 ¨ n22 and due to Proposition 5.1(i) it follows that

n2 ` ÿ

` 3r´5 2p3r´2q ´ pr ` 1qη

˘

“|Ai||Aj| ´ epAi,Ajq‰ ` “1

2|A1||A2| ` ηn2 ´ epA1,A2q‰

1ďiăjďr pi,jq‰p1,2q

ď ÿ

|Ai||Aj| ´ 21|A1||A2|. (6.2)

1ďiăjďr

The square brackets on the left side being positive we deduce ` 3r´5 2p3r´2q ´ pr ` 1qη

n2 ď ÿ

˘

|Ai||Aj| ´ 12|A1||A2|

1ďiăjďr

and the case “ pr ` 1qη of Lemma 6.1 leads to the ﬁrst two bullets. Furthermore, Lemma 6.1 provides an upper bound of 3r´5

3r´2 ¨ n22 on the right side of (6.2). Therefore we have

ÿ

“|Ai||Aj| ´ epAi,Ajq‰ ` “1

2|A1||A2| ` ηn2 ´ epA1,A2q‰ ď pr ` 1qηn2 .

1ďiăjďr pi,jq‰p1,2q

and the last two bullets follow as well.

6.2. Local minimum degree. Along the way leading from the partition provided by

- Proposition 5.1 to our main theorem we will need to make further eﬃcient uses of the

assumption K2r Ę G. It should be clear that building a K2r in G would be easier if we knew that certain minimum degree conditions hold between the partition classes and the goal of this section is to enforce several such conditions by moving a few vertices violating them to other classes into which they ﬁt better. For later reference we include the somewhat lengthy list of properties that we shall obtain into a deﬁnition.

Deﬁnition 6.3. Let an integer r ě 2, a real ε ą 0, an n-vertex graph G, and a partition V pGq “ B1 ¨Y ... ¨Y Br be given. Set dipvq “ dB

ipvq for all v P V pGq and i P rrs. We say that the above partition is pr,εq-exact if the following conditions hold.

(α) For i “ 1,2 one has ˇ|Bi| ´ 3r2´n2

ˇ ď εn. (β) For i “ 3,...,r one has ˇ|Bi| ´ 3r3´n2

ˇ ď εn.

(γ) If i P rrs, then epBiq ď εn2. (δ) If X1 Ď B1 and X2 Ď B2, then ˇepX1,X2q ´ 12|X1||X2|ˇ ď εn2. (ε) If 1 ď i ă j ď r and pi,jq ‰ p1,2q, then epBi,Bjq ě |Bi||Bj| ´ εn2. (ζ) If ti,ju “ t1,2u and v P Bi, then djpvq ě 31r{´32n. (η) If i P t1,2u, j P r3,rs, and v P Bi, then djpvq ě 35r{´32n. (ϑ) If i P r3,rs, j P t1,2u, and v P Bi, then djpvq ě 31r{´52n.

(ι) If i,j P r3,rs are distinct and v P Bi, then djpvq ě 3r1´2n. The main result of this subsection is the following.

- Proposition 6.4. For every r ě 2 and ε ą 0 there exist n0 P N and δ ą 0 such that every


K2r-free graph G on n ě n0 vertices, with δpGq ě 33rr´´52n and αpGq ă δn has an pr,εq-exact partition.

Proof. By monotonicity we may assume that ε is suﬃciently small so that all estimates to be performed below will hold. We commence be choosing a suﬃciently small η ! ε. With this number η we appeal to Proposition 5.1 and it answers with an integer n0 P N and with some δ ą 0. We claim that these two constants have the desired properties.

Let any K2r-free graph G on n ě n0 vertices with αpGq ă δn and δpGq ě 33rr´´52n be given and take a partition

V pGq “ A01 ¨Y A02 ¨Y ... ¨Y A0r (6.3) such that

- (i) epA0iq ď ηn2 for all i P rrs;
- (ii) if X1 Ď A01 and X2 Ď A02, then epX1,X2q ď 12|X1||X2| ` ηn2.

Due to Fact 6.2 and η ! ε we may suppose moreover that

- (iii) for i “ 1,2 we have ˇ|A0i| ´ 3r2´n2

ˇ ď 12εn;

- (iv) for i “ 3,...,r we have ˇ|A0i| ´ 3r3´n2

ˇ ď 12εn;

- (v) epA01,A02q ě 12|A01||A02| ´ 41εn2;

- (vi) and that epA0i,A0iq ě |A0i||A0j| ´ 12εn2 whenever 1 ď i ă j ď r and pi,jq ‰ p1,2q. We need to deﬁne an pr,εq-exact partition of G. To this end we perform a recursive


procedure, in the course of which a sequence of partitions of V pGq into r parts is constructed. The starting point is (6.3). In each step only one vertex is moved from one vertex class to another one, while all other vertices stay in the partition class they have belonged to before. Let

V pGq “ As1 ¨Y As2 ¨Y ... ¨Y Asr be the partition that we have after s steps and put

ÿr

Ωs “ 6epAs1q ` 6epAs2q `

epAsiq. When the sth step is to carried out, we ensure that

i“3

Ωs ď Ωs´1 ´ 31r{´42n (6.4)

holds. This condition guarantees inductively that Ωs ď Ω0 ´ 3sr{´42n and because of Ωs ě 0 this means that at some moment we will run out of permissible steps. When this happens we stop the procedure and we let

V pGq “ B1 ¨Y B2 ¨Y ... ¨Y Br (6.5) be the terminal partition. The remainder of this proof is dedicated to proving that this partition is pr,εq-exact. If the above procedure lasted for t steps, then

(i )

t{4

ď pr ` 10qηn2

3r´2n ď Ω0

informs us that

t ď 4p3r ´ 2qpr ` 10qηn ď 48r2ηn. (6.6)

In particular, η ! ε ! 1 allows us to conclude that t ď 12εn. Since only t vertices were moved during the process, it follows from this bound and from (iii) as well as (iv) that the clauses (α) and (β) of Deﬁnition 6.3 are satisﬁed.

For ﬁxed i P rrs the current value of epAiq can change by at most n in every step and thus we have

epBiq ď epA0iq ` tn ď 49r2ηn2 ď εn2 by (i) and (6.6), which shows the validity of (γ). The proof of (ε) is very similar but uses (vi) instead of (i). We leave the details to the reader. Proceeding similarly with (v) one can obtain

epB1,B2q ě 12|B1||B2| ´ 12εn2 . (6.7) Let us continue with (δ). For any two sets X1 Ď B1 and X2 Ď B2 we have

epX1,X2q ď epX1 X A01,X2,XA02q ` p|B1 A01| ` |B2 A02|qn

(ii )

ď 21|X1 X A01||X2,XA02| ` ηn2 ` tn and in view of (6.6) it follows that

epX1,X2q ď 21|X1||X2| ` 41εn2 . (6.8) We still need an estimate in the other direction and for this purpose we invoke (6.7) and make two applications of (6.8), thus getting

epX1,X2q “ epB1,B2q ´ epB1,B2 X2q ´ epB1 X1,X2q ě `1 2|B1||B2| ´ 21εn2

˘ ´ `1

˘ ´ `1

˘

2|B1||B2 X2| ` 14εn2

2|B1 X1||X2| ` 14εn2

“ 12|X1||X2| ´ εn2 . Altogether the pair pB1,B2q behaves indeed as demanded by (δ).

It remains to deal with the local minimum conditions (ζ), (η), (ϑ), and (ι). The proofs of all four of them are very similar and rely on the property (6.4) of the procedure that was used to generate the partition (6.5). We will only display the proof (η) here and leave the three other clauses to the reader.

Assume, for instance, that there is a vertex v P B1 with d3pvq ă 35r{´32n. Due to the minimum degree condition imposed on G we must have

d1pvq ě 33rr´´52n ´ |B2| ´ 35r{´32n ´

ÿr

|Bi|.

i“4

Because of (α) and (β) this implies

d1pvq ě 31r{´32n ´ pr ´ 2qεn, wherefore

6d1pvq ´ d3pvq ą 31r{´42n. Consequently we can perform a pt ` 1qst step of our procedure and move v from B1 to B3. This contradicts the supposed maximality of t, and thereby (η) is proved.

§7. Refined edge counting Let us start this section with an elementary lemma, the following.

- Lemma 7.1. Every graph G not containing a cycle of length 3, 5, or 7 satisﬁes epGq ď αpGq2 .


Proof. We construct recursively a sequence z1,...,zk of distinct vertices of G according to the following rules.

‚ Let z1 be any vertex of G whose degree is maximal. ‚ If at some moment the vertices z1,...,zi have already been selected, we ask ourselves

whether the set Qi of all vertices having a distance of at least four from all of them is empty or not.

‚ If Qi “ ∅, we set k “ i and terminate the procedure. ‚ Otherwise we take a vertex zi`1 P Qi whose degree is as large as possible.

Set Q0 “ V pGq and Wi “ Qi´1 Qi for i “ 1,...,k. Notice that V pGq “ W1 ¨Y ... ¨Y Wk

is indeed a partition, because Q0 Ě Q1 Ě ¨¨¨ Ě Qk “ ∅. Owing to the maximum degree conditions imposed on the vertices zi we have

2epGq “ ÿ

ÿk

|Wi| ¨ dpziq. (7.1)

dpxq ď

i“1

xPV pGq

We contend that for i P rks every vertex x P Wi has at most distance three from zi. To see this we remark that due to x R Qi there has to be an index j P ris such that x has distance at most three from zj. Moreover, j ă i would yield x R Qi´1, contrary to x P Wi. Thus we must have j “ i, as desired.

It follows that we can partition Wi into a set of vertices having distance 0 or 2 from zi and a set of vertices having distance 1 or 3 from zi. Both partition classes are independent sets, for otherwise G would contain an odd cycle of length 3, 5, or 7.

In particular, we have |Wi| ď 2αpGq for each i P rks and in view of (7.1) we obtain

ÿk

epGq ď αpGq

dpziq.

i“1

Due to their construction any two of the vertices z1,...,zk have a distance of at least four. Therefore, their neighbourhoods are mutually disjoint and taken together they form an independent set. Thus we have indeed epGq ď αpGq2.

After this little distraction we resume our task of proving Theorem 1.2. In the light of the work in the two previous sections, it seems desirable to deal with the case that G admits an exact partition, which will occupy the remainder of the present section.

- Proposition 7.2. Given an integer r ě 2, there exists a real ε ą 0 such that for every


δ ď ε every n-vertex graph G with K2r Ę G and αpGq ď δn admitting an pr,εq-exact partition of its vertex set has at most

`3r´5 3r´2 ` δ ´ δ2

˘n

2

2 edges.

Proof. Throughout the arguments that follow we will assume that ε has been chosen so small that all estimates encountered below hold. Now let δ ď ε, let G “ pV,Eq be a K2r-free graph on n vertices with αpGq ă δn and let

V “ B1 ¨Y ... ¨Y Br

be an pr,εq-exact partition of G. By lowercase greek letters enclosed in parentheses such as (α), ..., (ι) we shall always mean the corresponding clauses of Deﬁnition 6.3.

The statement that follows will often be useful in conjunction with the hypothesis that G be K2r-free.

- Claim 7.3. Suppose that I Ď rrs and that for every i P I we have a set Xi Ď Bi with


|Xi| ě 31r{´152n. Then the set X “ Ť

iPI Xi contains a clique of order 2|I| ´ 1.

Moreover, if I does not contain both of 1 and 2, than X does even contain a clique of order 2|I|.

Proof. Let us begin with the “moreover”-part. Intending to apply Lemma 5.3 with ϑ “ 12

- and a “ b “ |I| we need to check that for distinct i,j P I the pair pXi,Xjq is p16´r,1q-dense and that αpGq ă |Xi|{4r. The latter is an immediate consequence of δ ď ε ! 1. Moreover, if Yi Ď Xi and Yj Ď Xj, then

epYi,Yjq

(ε)

ě |Yi||Yj| ´ εn2 ě |Yi||Yj| ´ 16´r|Xi||Xj|, as desired. If 1,2 P I we can still apply Lemma 5.3 with ϑ “ 12, but this time with a “ |I|

- and b “ |I| ´ 1. This is because (δ) allows us to show, in the same way as above, that the pair pX1,X2q is p1{16r,1{2q-dense.


Next we explain how condition (γ) is utilised.

- Claim 7.4. If i P rrs and X Ď Bi, then epXq ď 3nr{´602|X|. Proof. If |X| ď 3nr{´602 this follows from the trivial bound epXq ď |X|2. On the other hand, if |X| ě 3nr{´602, then we have

epXq

(γ)

ď εn2 ď ` n{60

3r´2

˘2 ď 3nr{´602|X| due to ε ! 1.

- Claim 7.5. For each i P r3,rs we have epBi,V q ď pn ´ |Bi|q|Bi| ` δn|Bi|.


Proof. Look at the partition Bi “ Bi` ¨Y Bi´ deﬁned by

Bi` “ !x P Bi: |Npxq Bi| ě n ´ |Bi| ´ 3nr{´152) and Bi´ “ Bi Bi`. Clearly, we have

epBi,V Biq ď pn ´ |Bi|q|Bi| ´ 3nr{´152|Bi´| (7.2) and Claim 7.4 yields

epBi´q ď 3nr{´602|Bi´|. (7.3)

Now assume for the sake of contradiction that Bi contains a triangle uvw two of whose vertices, say v and w, belong to Bi`. Let X denote the common neighbourhood of u, v, and w. The deﬁnition of Bi` leads to

(ι)

|X X Bj| ě |Npuq X Bj| ´ 32r{´152n

ě 133r{´152n

for j P r3,rs tiu and, similarly, we have |X X Bj| ě 31r{´152n for j “ 1,2 due to (ϑ). Thus the assumptions of Claim 7.3 are satisﬁed by I “ rrs tiu and X, meaning that X contains

a K2r´3. But together with the triangle uvw this clique gives us a K2r in G, which is absurd.

This proves that there are no such triangles in Bi and due to αpGq ă δn it follows that no vertex in Bi can have more than δn neighbours in Bi`. Therefore we have epBi`,Bi´q ď δn|Bi´| and 2epBi`q ď δn|Bi`|. Taking (7.2) and (7.3) into account we can now deduce

epBi,V q “ epBi,V Biq ` 2epBi`q ` 2epBi`,Bi´q ` 2epBi´q ď pn ´ |Bi|q|Bi| ` δn|Bi| ` ` n{30 3r´2 ` δn ´ 3nr{´152

˘|Bi´|, and in view of δ ! 1 the desired estimate follows.

Before we proceed deriving similar upper bounds for epB1,V q and epB2,V q, we record some useful properties of the common neighbourhoods of edges in B1.

- Claim 7.6. Any two vertices u,v P B1 forming an edge have at least 4{15

3r´2n common neighbours in each of B3,...,Br, but less than 1{15

3r´2n common neighbours in B2. Proof. For each i P r3,rs we have

|Npuq X Npvq X Bi| ě |Npuq X Bi| ` |Npvq X Bi| ´ |Bi|, which due to (β) and (η) yields

|Npuq X Npvq X Bi| ě 310r´{32n ´ ` 3

3r´2 ` ε

˘

n ě 34r{´152n,

- as desired. If u and v had at least 1{15


3r´2n common neighbours in B2, we could use Claim 7.3 with I “ rrs t1u to ﬁnd a K2r´2 among the common neighbours of those two vertices, contrary to K2r Ę G.

- Claim 7.7. For i P t1,2u we have


epBi,V q ď |Bi|pn ´ |B1| ´ |B2|q ` 12|B1||B2| ` 12δnp|B1| ` |B2|q ´ 12δ2n2 . Proof. Due to symmetry it suﬃces to prove this for i “ 1 only. The vertices in

P “ !x P B1: |Npxq B1| ď n ´ |B1| ´ 21|B2| ´ 31r{´152n) (7.4) receive special treatment.

- Fact 7.7.1. There is no triangle in B1 two of whose vertices are outside P.


Proof. Arguing indirectly we assume that uvw is such a triangle. By Claim 7.6 no two of the three vertices u, v, and w can have 1{15

3r´2n common neighbours in B2, whence d2puq ` d2pvq ` d2pwq ă |B2| ` 31r{´52n.

On the other hand, by the deﬁnition of P we have d2pxq ą 21|B2|´31r{´152n for every x P B1 P and together with (ζ) this yields

˘ ` 31r{´32n “ |B2| ` 31r{´52n. This contradiction proves Fact 7.7.1.

`1 2|B2| ´ 31r{´152n

d2puq ` d2pvq ` d2pwq ą 2

Since αpGq ă δn, it follows that no vertex in P can have δn neighbours in B1 P, which

in turn reveals epP,B1 Pq ď δn|P|. Together with the estimate epPq ď 3nr{´602|P|, which follows from Claim 7.4, this gives

2epP,B1 Pq ` 2epPq ď `

˘

2δ ` 31r{´302

n|P| ď 31r{´152n|P|

and by adding the upper bound on epP,V B1q that trivially follows from (7.4) we arrive

- at epP,V q ` epP,B1 Pq ď |P|pn ´ |B1| ´ 12|B2|q. (7.5)


- Fact 7.7.2. There is no C3, C5, or C7 in G all of whose vertices are in B1 P.

Proof. Assume contrariwise that for some P t3,5,7u the vertices in C “ tv1,...,v u form such a cycle. If a vertex x P B2 is adjacent to q vertices in C, then the neighbourhood of x contains at least q ´ 12p ´ 1q edges of this cycle, whence

epC,B2q “ ÿ

xPB2

dCpxq ď 12p ´ 1q|B2| ` t,

where t denotes the number of triangles formed by a vertex in B2 and an edge of the cycle. Further, by the second part of Claim 7.6, each edge of the cycle can sit in at most 1{15

3r´2n such triangles, wherefore t ď 37r{´152n.

On the other hand, each v P C has at least 12|B2| ´ 31r{´152n neighbours in B2 due to C Ď B1 P and (7.4), whence

epC,B2q “ ÿ

k“1

d2pvkq ě 21 |B2| ´ 37r{´152n. By combining all these estimates we infer

|B2| ď 283r{´152n, which, however, violates (α). This concludes the proof of Fact 7.7.2. Now consider the partition

B1 P “ Q ¨Y R ¨Y S deﬁned by

- Q “ !x P B1 P : d2pxq ď 21p|B2| ` δnq),

- R “ !x P B1 P : 12p|B2| ` δnq ă d2pxq ď 37r{´42n),


and S “ !x P B1 P : 7{4

3r´2n ă d2pxq).

- Fact 7.7.3. There is no edge connecting a vertex in S with a vertex in B1.

Proof. By (ζ) and the deﬁnition of S the common neighbourhood of such an edge would intersect B2 in at least

7{4

3r´2n ` 31r{´32n ´ |B2|

(α)

ě 31r{´152n vertices, contrary to Claim 7.6.

- Fact 7.7.4. The set R Y S is independent.


Proof. Assume that we have an edge uv both of whose endvertices are in R YS. According to the deﬁnitions of R and S, the common neighbourhood J of u and v has at least δn vertices in B2 and by αpGq ă δn there exists an edge xy in B2 X J.

We will now try to construct a K2r´4 in the common neighbourhood J˚ Ď J of u, v, x, and y, which would give a contradiction to K2r Ę G. To this end we utilise Claim 7.3 with I “ rrs t1,2u and it remains to show that we have |Bj X J˚| ě 31r{´152n for every j P r3,rs.

Thanks to Claim 7.6 we already know that x and y have at least 4{15

3r´2n common neighbours in each Bj with j P r3,rs, so it suﬃces to prove |Bj X J| ě |Bj| ´ 31r{´52n instead. For this purpose it is enough to establish

|J pB1 Y B2q| ě n ´ p|B1| ` |B2|q ´ 31r{´52n. (‹) Now due to u,v P B1 P and (7.4) we have

˘ ´ pn ´ |B1|q “ n ´ |B1| ´ |B2| ´ 32r{´152n and Claim 7.6 tells us that

`

n ´ |B1| ´ 21|B2| ´ 31r{´152n

|J B1| ě 2

|J X B2| ď 31r{´152n. It is easily seen that the last two estimates imply p‹q.

We will now work towards an upper bound on epB1 P,B2q. Due to the deﬁnitions of Q, R, and S we have

epB1 P,B2q ď |Q| ¨ 12p|B2| ` δnq ` |R| ¨ 37r{´42n ` |S||B2|

(α)

ď p|Q| ` |R|q ¨ 21p|B2| ` δnq ` |R| ¨ 34r{´52n ` |S||B2|. According to Fact 7.7.4 and αpGq ă δn we have |R| ď δn ´ |S| and thus we arrive at

epB1 P,B2q ď 21|B1 P|p|B2| ` δnq ` pδn ´ |S|q34r{´52n ` 12|S|p|B2| ´ δnq “ 12|B1 P||B2| ` 21δnp|B1 P| ` |B2|q ´ 21δ2n2 ` pδn ´ |S|q` 4{5 3r´2n ` 12δn ´ 12|B2|˘

. Employing (α) we may weaken this to

epB1 P,B2q ď 12|B1 P||B2| ` 12δnp|B1| ` |B2|q ´ 21δ2n2 ´ 2δnpδn ´ |S|q. (7.6)

Next we learn from Lemma 7.1 and Fact 7.7.2 that epQYRq ď αpQYRq2, where αpQYRq, the size of the largest independent set in Q Y R, is at most δn ´ |S| due to Fact 7.7.3 and αpGq ă δn. So in other words we have epQ Y Rq ď pδn ´ |S|q2 ď δnpδn ´ |S|q. A further application of Fact 7.7.3 leads to the seemingly stronger inequality epB1 Pq ď δnpδn´|S|q and together with (7.6) this yields

epB1 P,B1 Y B2 Pq ď 21|B1 P||B2| ` 12δnp|B1| ` |B2|q ´ 12δ2n2 .

`

B1 P,V pB1 Y B2q˘

Adding the trivial upper bound for e

we obtain epB1 P,V Pq ď |B1 P|`

n ´ |B1| ´ 21|B2|˘ ` 12δnp|B1| ` |B2|q ´ 21δ2n2 . Combined with (7.5) this shows the desired estimate

epB1,V q ď |B1|`

n ´ |B1| ´ 12|B2|˘ ` 12δnp|B1| ` |B2|q ´ 12δ2n2 and the proof of Claim 7.7 is thereby complete.

Finally, the addition of the r inequalities provided by the Claims 7.5 and 7.7 reveals 2epGq “

ÿr

ÿ

ÿr

|Bi| ´ δ2n2

epBi,V q ď 2

|Bi||Bj| ´ |B1||B2| ` δn

i“1

1ďiăjďr

i“1

and Lemma 6.1 leads to

2epGq ď `3r´5

˘

n2 . Thereby Proposition 7.2 is proved.

3r´2 ` δ ´ δ2

Now the following should be clear.

- Proposition 7.8. For every integer r ě 2 there exist an integer n0 and a positive real number δ0 such that for every δ ď δ0 every graph G on n ě n0 vertices with K2r Ę G,


`3r´5 3r´2 ` δ ´ δ2

˘n

2

δpGq ě 33rr´´52n, and αpGq ă δn has at most

2 edges.

Proof. Let ε ą 0 be the number provided by Proposition 7.2. By plugging it into Proposition 6.4 we obtain some constants n0 P N and δ0 ą 0. Without loss of generality we may suppose that δ0 ď ε. To check that these two numbers have the desired property we consider any graph G on n ě n0 vertices satisfying the above conditions for some δ ď δ0 ď ε.

Now Proposition 6.4 informs us that G has an pr,εq-exact partition and Proposition 7.2 yields the desired upper bound on epGq.

The only things which are currently missing from a proof of Theorem 1.2 are that we still need to abolish the minimum degree condition and n0. Essentially this can be done in the same way as in Section 3, but for the sake of completeness we would like to include a sketch of the argument.

Proof of Theorem 1.2. Let n0 P N and δ0 P p0,1q be as obtained by Proposition 7.8 and set

`

˘

δ02,n´0 2

δ˚ “ 14 min

.

Due to the blow-up trick it suﬃces to show the apparently weaker statement that if δ ď δ˚ and a K2r-free graph G on n vertices satisﬁes αpGq ă δn, then

3r ´ 5 3r ´ 2 ¨

n2 ` n 2 `

pδ ´ δ2qn2 2

. (7.7)

epGq ď

Assuming again that this estimate fails we take a minimal set X Ď V pGq with epXq ą

3r ´ 5 3r ´ 2 ¨

|X|2 ` |X| 2 `

pδ ´ δ2qn2 2

(7.8) and denote the restriction of G to X by G1. Observe that X ‰ ∅ and put n1 “ |X| as well as δ1 “ δn{n1. Again the plan is to apply Proposition 7.8 to G1 and δ1 and the required estimates δpG1q ě 33rr´´25|X| as well as αpG1q ď δ1|X| hold for same reasons as above. Moreover, in view of

˘ ` pδ ´ δ2qn2 ą 33rr´´52pn1q2 ` 12δn2 we have, e.g.,

`pn1q2 ` n1

pn1q2 ě 2epXq ą 33rr´´52

?

δn{2. (7.9) Thus δ1 ă 2?

n1 ą

δ ď 2?δ˚ ď δ0, meaning that δ1 is indeed suﬃciently small. Moreover, since δn ą αpGq ě 1, the estimate (7.9) does also imply

- 1

- 2?


- 1

- 2?δ˚ ě n0 ,


n1 ą

δ ě or in other words that G1 is still suﬃciently large. So altogether Proposition 7.8 implies

3r ´ 5 3r ´ 2 ¨

3r ´ 5 3r ´ 2 ¨

|X|2 2 `

δ1n1 ¨ n1 ´ pδ1n1q2 2 ă

|X|2 ` |X| 2 `

δn ¨ n ´ pδnq2 2

epXq ď

, contrary to (7.8). This concludes the proof of (7.7) and, hence, the proof of Theorem 1.2.

References

- [1] B. Bollobás and P. Erdős, On a Ramsey-Turán type problem, J. Combinatorial Theory Ser. B 21

(1976), no. 2, 166–168. MR0424613 Ò1, 2

- [2] S. Brandt, Triangle-free graphs whose independence number equals the degree, Discrete Math. 310

(2010), no. 3, 662–669, DOI10.1016/j.disc.2009.05.021. MR2564822 Ò1, 2

- [3] P. Erdős, A. Hajnal, V. T. Sós, and E. Szemerédi, More results on Ramsey-Turán type problems, Combinatorica 3 (1983), no. 1, 69–81, DOI10.1007/BF02579342. MR716422 Ò1, 2, 4, 5, 5, 5, 5
- [4] P. Erdős and M. Simonovits, A limit theorem in graph theory, Studia Sci. Math. Hungar 1 (1966), 51–57. MR0205876 (34 #5702) Ò1
- [5] P. Erdős and V. T. Sós, Some remarks on Ramsey’s and Turán’s theorem, Combinatorial theory and its applications, II (Proc. Colloq., Balatonfüred, 1969), North-Holland, Amsterdam, 1970, pp. 395–404. MR0299512 Ò1
- [6] P. Erdős and A. H. Stone, On the structure of linear graphs, Bull. Amer. Math. Soc. 52 (1946), 1087–1091. MR0018807 (8,333b) Ò1
- [7] A. Frieze and R. Kannan, Quick approximation to matrices and applications, Combinatorica 19 (1999), no. 2, 175–220, DOI10.1007/s004930050052. MR1723039 Ò1
- [8] J. Fox, P.-S. Loh, and Y. Zhao, The critical window for the classical Ramsey-Turán problem, Combinatorica 35 (2015), no. 4, 435–476, DOI10.1007/s00493-014-3025-3. MR3386053 Ò1, 2, 2, 2, 4


- [9] T. Łuczak, On the structure of triangle-free graphs of large minimum degree, Combinatorica 26 (2006), no. 4, 489–493, DOI10.1007/s00493-006-0028-8. MR2260851 (2007e:05077) Ò5
- [10] C. M. Lüders and Chr. Reiher, Weighted variants of the Andrásfai-Erdős-Sós Theorem. Preprint. Ò5
- [11] F. P. Ramsey, On a Problem of Formal Logic, Proceedings London Mathematical Society 30 (1930), no. 1, 264–286, DOI10.1112/plms/s2-30.1.264. Ò1
- [12] M. Simonovits and V. T. Sós, Ramsey-Turán theory, Discrete Math. 229 (2001), no. 1-3, 293–340, DOI10.1016/S0012-365X(00)00214-4. Combinatorics, graph theory, algorithms and applications. MR1815611 Ò1
- [13] E. Szemerédi, On graphs containing no complete subgraph with 4 vertices, Mat. Lapok 23 (1972), 113–116 (1973) (Hungarian). MR0351897 Ò1
- [14] , Regular partitions of graphs, Problèmes combinatoires et théorie des graphes (Colloq. Internat. CNRS, Univ. Orsay, Orsay, 1976), Colloq. Internat. CNRS, vol. 260, CNRS, Paris, 1978, pp. 399–401 (English, with French summary). MR540024 Ò5

- [15] P. Turán, Eine Extremalaufgabe aus der Graphentheorie, Mat. Fiz. Lapok 48 (1941), 436–452 (Hungarian, with German summary). MR0018405 Ò1
- [16] A. A. Zykov, On some properties of linear complexes, Mat. Sbornik N.S. 24(66) (1949), 163–188 (Russian). MR0035428 Ò5


Fachbereich Mathematik, Universität Hamburg, Hamburg, Germany E-mail address: Christian.Reiher@uni-hamburg.de E-mail address: Clara.Marie.Lueders@gmail.com

