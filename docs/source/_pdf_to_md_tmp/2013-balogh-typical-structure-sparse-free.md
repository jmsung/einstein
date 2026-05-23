arXiv:1307.5967v2[math.CO]26Aug2014

THE TYPICAL STRUCTURE OF SPARSE Kr+1-FREE GRAPHS

JOZSEF´ BALOGH, ROBERT MORRIS, WOJCIECH SAMOTIJ, AND LUTZ WARNKE

Abstract. Two central topics of study in combinatorics are the so-called evolution of random graphs, introduced by the seminal work of Erd˝s and Re´nyi, and the family of H-free graphs, that is, graphs which do not contain a subgraph isomorphic to a given (usually small) graph H. A widely studied problem that lies at the interface of these two areas is that of determining how the structure of a typical H-free graph with n vertices and m edges changes as m grows from 0 to ex(n, H). In this paper, we resolve this problem in the case when H is a clique, extending a classical result of Kolaitis, Pro¨mel, and Rothschild. In particular, we prove that for every r 2, there is an explicit constant θr such that, letting mr = θrn2−r+22 (log n)1/[(r+12 )−1], the following holds for every positive constant ε. If m (1 + ε)mr, then almost all Kr+1-free n-vertex graphs with m edges are r-partite, whereas if n ≪ m (1 − ε)mr, then almost all of them are not r-partite.

![image 1](<2013-balogh-typical-structure-sparse-free_images/imageFile1.png>)

1. Introduction

- 1.1. Background and motivation. Given integers n and m, let Gn,m be the uniformly chosen random element of the family Gn,m of all graphs on a ﬁxed vertex set of size n that have precisely m edges. The study of the evolvement of typical properties of Gn,m when we let m gradually increase


from 0 to n2 , known as the evolution of random graphs, which was initiated in the seminal work of Erd˝os and Re´nyi [21], is a central topic in graph theory. The behavior of many parameters

and properties during the evolution of Gn,m, such as connectivity, containment of small subgraphs, chromatic number, to name a few, is now fairly well understood [13, 28]. A natural problem is to consider such evolution when we restrict our attention to a certain subclass of graphs, i.e., when Gn,m is a random element of some proper subfamily of Gn,m.

In this paper, we consider the class of graphs that do not contain a clique of a given ﬁxed order. The study of H-free graphs, i.e., graphs which do not contain a subgraph isomorphic to a given ﬁxed graph H, is one of the cornerstones of extremal graph theory. The classical theorem of Tura´n [46] states that for every r 2, the largest number of edges in a Kr+1-free graph on n vertices, denoted ex(n,Kr+1), is equal to the number of edges in the balanced complete r-partite graph Tr(n), that is

n 2

1 r

ex(n,Kr+1) = e(Tr(n)) = 1 −

+ O(n).

![image 2](<2013-balogh-typical-structure-sparse-free_images/imageFile2.png>)

Moreover, it identiﬁes Tr(n) as the unique extremal graph, i.e., the unique Kr+1-free n-vertex graph with ex(n,Kr+1) edges. A famous result of Kolaitis, Pr¨omel, and Rothschild [31] determines the typical structure of Kr+1-free graphs. It states that for every r 2, almost all Kr+1-free graphs are r-partite (r-colorable); in the case r = 2, this was proved earlier by Erd˝os, Kleitman, and Rothschild [20].

![image 3](<2013-balogh-typical-structure-sparse-free_images/imageFile3.png>)

Date: June 6, 2018.

Research supported in part by: (JB) Marie Curie Fellowship IIF-327763, NSF CAREER Grant DMS-0745185, UIUC Campus Research Board Grants 11067 and 13039 (Arnold O. Beckman Research Award), and OTKA Grant K76099; (RM) CNPq bolsa de Produtividade em Pesquisa; (WS) ERC Advanced Grant DMMCA and Trinity College JRF; (LW) Peterhouse JRF.

1

In view of the above, one naturally arrives at the following question, ﬁrst considered by Pr¨omel and Steger [37] more than ﬁfteen years ago. Let Fn,m(Kr+1) denote the family of all Kr+1-free graphs on a ﬁxed set of n vertices (for concreteness, we let it be the set {1,... ,n}) that have exactly m edges. For which m are almost all graphs in Fn,m(Kr+1) r-partite? This is trivially true for very small m, as then almost all graphs in Gn,m are both Kr+1-free and r-colorable, and when m = ex(n,Kr+1), by Tura´n’s theorem. By the Kolaitis–Pr¨mel–Rothschild theorem, it must also be true for at least one value of m that is close to 12 ·ex(n,Kr+1), since almost all r-colorable graphs have roughly this many edges. On the other hand, it is not very hard to see that this statement is not true for m in some intermediate range. For example, if n ≪ m ≪ n4/3, then almost all graphs in Gn,m are both K4-free and not r-colorable for every ﬁxed r.

![image 4](<2013-balogh-typical-structure-sparse-free_images/imageFile4.png>)

In the case of triangle-free graphs, it turns out that as m grows from 0 to ex(n,K3), there are two critical points at which almost all graphs in Fn,m(K3) ﬁrst stop being and then become bipartite, as proved by Osthus, Pr¨omel, and Taraz [33], who improved an earlier result of Pr¨omel and Steger [37] (see also Steger [45] for a slightly weaker result). More precisely, the following was shown in [33]. Let ε be an arbitrary positive constant and let

√3 4

![image 5](<2013-balogh-typical-structure-sparse-free_images/imageFile5.png>)

n3/2 log n. (1)

![image 6](<2013-balogh-typical-structure-sparse-free_images/imageFile6.png>)

m2 = m2(n) =

![image 7](<2013-balogh-typical-structure-sparse-free_images/imageFile7.png>)

First, if m ≪ n, then almost all graphs in Fn,m(K3) are bipartite. Second, if n/2 m (1−ε)m2, then almost all these graphs are not bipartite. Third, if m (1 + ε)m2, then again almost all of

- them are bipartite. A corresponding result for r = 4 was obtained in the unpublished master’s thesis of the fourth author [47].


- 1.2. Main result. In this paper, we generalize the above result to all r. To this end, for each r 2, deﬁne


2 r+2

1 r−1

![image 8](<2013-balogh-typical-structure-sparse-free_images/imageFile8.png>)

r − 1 2r · r ·

2r + 2 r + 2

![image 9](<2013-balogh-typical-structure-sparse-free_images/imageFile9.png>)

(2) and

θr =

![image 10](<2013-balogh-typical-structure-sparse-free_images/imageFile10.png>)

![image 11](<2013-balogh-typical-structure-sparse-free_images/imageFile11.png>)

1

![image 12](<2013-balogh-typical-structure-sparse-free_images/imageFile12.png>)

(r+12 )−1. (3)

2

mr = mr(n) = θrn2−

r+2(log n)

![image 13](<2013-balogh-typical-structure-sparse-free_images/imageFile13.png>)

Here and throughout the paper, log denotes the natural logarithm. Note that the deﬁnitions of m2 given by (1) and by (3) coincide. Our main result is the following.

- Theorem 1.1. For every r 3, there exists a dr = dr(n) = Θ(n) such that the following holds for every ε > 0. If Fn,m is the uniformly chosen random element of Fn,m(Kr+1), then


 

1 m (1 − ε)dr,

P[Fn,m is r-partite] =

lim

- 0 (1 + ε)dr m (1 − ε)mr,
- 1 m (1 + ε)mr.


n→∞



The existence of the ﬁrst threshold and the function dr in Theorem 1.1 follows directly from the fact that for every r 3, the property of being r-colorable has a sharp threshold in Gn,m, as proved by Achlioptas and Friedgut [1], see also [24]. Indeed, if m ≪ n2−2/r, then almost all graphs in Gn,m are Kr+1-free and therefore almost every graph in Fn,m(Kr+1) is r-partite if and only if almost every graph in Gn,m is r-partite. Moreover, one immediately sees that the threshold function for the property of being r-colorable, which we denote by dr, satisﬁes dr(n) = Θ(n); for more precise estimates, with which we will not be concerned in this paper, we refer the reader to [2, 15]. Thus, the main business of this paper will be establishing the existence of the second

threshold at mr. Finally, we would like to point out that our arguments for m ≫ n, which really is the main case of interest for us, are also valid in the case r = 2. The only reason why in the statement of Theorem 1.1, we assume that r 3 is that the property of being bipartite does not have a sharp threshold in Gn,m and therefore in the case r = 2, there is no double sharp threshold phenomenon.

- 1.3. Approximate version. A closely related problem is that of determining for which m almost

every graph in Fn,m(Kr+1) is almost r-partite, i.e., becomes r-partite after deleting from it some small fraction of the edges. Fifteen years ago, this problem was ﬁrst considered by  Luczak [32], who proved that when m ≫ n3/2, then almost every graph in Fn,m(K3) can be made bipartite by deleting from it some o(m) edges. Furthermore,  Luczak showed that the so-called K LR conjecture [30] implies an analogous statement for arbitrary r 2, Theorem 1.2 below. This conjecture was only very recently veriﬁed by the ﬁrst three authors [10], and by Saxton and Thomason [42]; see also [17]. The following result was established by the ﬁrst three authors in [10] (the case r = 2 was proved much earlier in [32]). It may also be derived from the results of [42].

- Theorem 1.2 ([10, 42]). For every r 2 and every δ > 0, there exists a constant C such that if


m Cn2−2/(r+2), then almost every graph in Fn,m(Kr+1) can be made r-partite by removing from it at most δm edges.

As mentioned above, Theorem 1.2 was derived from the (then unproven) K LR conjecture in [32]. We remark here that in fact the proof of Theorem 1.2 in [10] yields that the proportion of graphs in Fn,m(Kr+1) that cannot be made r-partite by removing from them some δm edges is at most (1 − ε)m for some positive constant ε that depends solely on r and δ.

- 1.4. Related work. The main result of this paper, Theorem 1.1, may be also viewed in the context of the recent developments of ‘sparse random analogues’ of classical results in extremal combinatorics such as the aforementioned theorem of Tura´n. Here, we just give a very brief summary of these developments. For more information, we refer the interested reader to the survey of Ro¨dl and Schacht [40]. A long line of research, initiated in [5, 23, 29, 38, 39], has recently culminated in breakthroughs of Conlon and Gowers [16] and Schacht [43] (see also [10, 17, 25, 41, 42]), which developed a general theory for approaching such problems. In particular, these results imply that, asymptotically almost surely (a.a.s.), i.e., with probability tending to one as n → ∞, if p ≫ n−2/(r+2),


- then the number ex(G(n,p),Kr+1) of edges in a largest Kr+1-free subgraph of the binomial random graph G(n,p) satisﬁes


1 r

ex(G(n,p),Kr+1) = 1 −

![image 14](<2013-balogh-typical-structure-sparse-free_images/imageFile14.png>)

n 2

p + o(n2p).

This statement is usually referred to as the sparse random analogue of Tura´n’s theorem. Moreover, a.a.s. any Kr+1-free subgraph of G(n,p) with ex(G(n,p),Kr+1) − o(n2p) edges may be made rpartite by removing from it some o(n2p) edges. This is usually referred to as the sparse random analogue of the Erd˝os–Simonovits stability theorem [22, 44].

In fact, these random analogues of the theorems of Tura´n and Erd˝os and Simonovits are much more closely related to Theorem 1.2 rather than Theorem 1.1. A question somewhat closer in spirit to the latter would be deciding for which functions p = p(n) is, a.a.s., the largest Kr+1-free subgraph of G(n,p) exactly r-partite. Such a statement may be viewed as an exact sparse random analogue of Tura´n’s theorem. This problem also has a fairly long history. It was ﬁrst considered by Babai, Simonovits, and Spencer [5], who proved that the condition p > 1/2 is suﬃcient in the

case r = 2. Much later, Brightwell, Panagiotou, and Steger [14] showed that for every r, the exact random analogue of Tura´n’s theorem holds when p(n) n−c for some constant c that depends on r. Very recently, DeMarco and Kahn [18] showed that in the case r = 2 it is enough to assume that p(n) C log n/n, where C is some positive constant; this is best possible up to the value

![image 15](<2013-balogh-typical-structure-sparse-free_images/imageFile15.png>)

of C since, as pointed out in [14], the statement is false when p(n) 10 1 log n/n. Note that the threshold p(n) = log n/n for the above property (in the case r = 2) in G(n,p) coincides with the

![image 16](<2013-balogh-typical-structure-sparse-free_images/imageFile16.png>)

![image 17](<2013-balogh-typical-structure-sparse-free_images/imageFile17.png>)

![image 18](<2013-balogh-typical-structure-sparse-free_images/imageFile18.png>)

threshold m2(n) from Theorem 1.1; nevertheless, the diﬃculties encountered in the two problems are quite diﬀerent, and the proof in [18] has (not surprisingly) little in common with that given here. Even more recently, DeMarco and Kahn [19] showed that for every r 2, the exact random analogue of Tura´n’s theorem for Kr+1 holds under the assumption that p(n) Cmr(n)/n2, where C is a suﬃciently large constant and mr(n) is deﬁned in (3), see [18, Conjecture 1.2].

Finally, we remark that the family Fn(H) of n-vertex H-free graphs has been extensively studied for general graphs H. Extending [31], Pr¨omel and Steger [35] proved that if H contains an edge whose removal reduces the chromatic number of H (such graphs are called edge-color-critical), then almost all graphs in Fn(H) are (χ(H) − 1)-partite. Generalizing [31, 35] even further, Hundack, Pr¨omel, and Steger [27] proved that if H contains a color-critical vertex (one whose removal reduces the chromatic number), then almost every graph in Fn(H) admits a partition of its vertex set into χ(H) − 1 parts, each of which induces a subgraph whose maximum degree is bounded by an explicit constant dH (in particular, dH = 0 if H is edge-color-critical). It would be interesting

- to generalize these results in the same way that Theorem 1.1 generalizes the Kolaitis–Pr¨omel– Rothschild theorem. We expect the following statement to be true.


Conjecture 1.3. For every strictly 2-balanced, edge-color-critical graph H, there exists a constant C such that the following holds. If

m Cn2−1/m2(H)(log n)1/(e(H)−1), then almost all graphs in Fn,m(H) are (χ(H) − 1)-partite.

Let us remark here that a statement that is even stronger than Conjecture 1.3 was proved by Osthus, Pr¨omel, and Taraz [33] in the case when H is a cycle of odd length. More precisely, the following was shown in [33]. Let ℓ be an integer, let ε be an arbitrary positive constant, and let

1 ℓ−1

n 2

ℓ ℓ − 1 ·

ℓ

![image 19](<2013-balogh-typical-structure-sparse-free_images/imageFile19.png>)

log n

.

tℓ = tℓ(n) =

![image 20](<2013-balogh-typical-structure-sparse-free_images/imageFile20.png>)

![image 21](<2013-balogh-typical-structure-sparse-free_images/imageFile21.png>)

If n/2 m (1−ε)tℓ, then almost all graphs in Fn,m(C2ℓ+1) are not bipartite and if m (1+ε)tℓ, then almost all of them are bipartite.

Many (almost) sharp results describing the structure of almost all graphs in Fn(H) for a general graph H were proved in a series of papers by Balogh, Bollob´s, and Simonovits [6, 7, 8]. Although it is not explicitly stated there, one can read out from their proofs that almost all graphs in Fn,m(Kr+1) are r-partite when m = Ω(n2).

Precise structural descriptions of the families Fn(H) when H is a hypergraph are harder to obtain, and such results have so far been proved only for a few speciﬁc 3-uniform hypergraphs [11, 12, 34]. Finally, we remark that the typical structure of graphs with a forbidden induced subgraph has also been considered in the literature, see [3, 9].

- 1.5. Outline of the paper. The remainder of this paper is organised as follows. In Section 2, we give a fairly detailed outline of the strategy for proving Theorem 1.1. In Sections 3 and 4, we collect some auxiliary results needed for the proof. In Section 5, we establish the 0-statement in


- Theorem 1.1. Starting with Section 6, we turn to proving the second 1-statement in Theorem 1.1. Our argument is rather involved and we subdivide it into two diﬀerent cases, addressed in Sections 7 and 8, respectively.
- 1.6. Notation. For the sake of brevity, given an integer n, we will abbreviate {1,... ,n} by [n]. For concreteness, we assume that [n] is the common vertex set of all of the n-vertex graphs we consider in this paper. Let Gn,m(r) be the family of all graphs in Gn,m, i.e., graphs on the vertex set [n] with precisely m edges, that are r-colorable. Let Pn,r be the family of all r-colorings of [n], that is, all partitions of [n] into r parts. For the sake of brevity, we shall often identify a partition


Π ∈ Pn,r with the complete r-partite graph on the vertex set [n] whose color classes are the r parts of Π. In particular, if G is a graph on the vertex set [n], then G ⊆ Π means that G is a subgraph of the complete r-partite graph Π or, in other words, the partition Π is a proper coloring of G. Exploiting this convention, we will also write Πc to denote the complement of the graph Π, that is, the union of r complete graphs whose vertex sets are the color classes of Π.

Otherwise, we use fairly standard conventions. In particular, given a graph G, one of its vertices v, and a set A ⊆ V (G), we denote the number of edges in G, the degree of v in G, and the number of neighbors of v in the set A by e(G), degG(v), and degG(v,A), respectively. For a graph G and a set A ⊆ V (G), we shall write G − A to denote the subgraph of G induced by the set V (G) \ A. Perhaps less obviously, Kr−+1 denotes the graph obtained from the complete graph on r + 1 vertices by removing a single edge, which we refer to as the missing edge. For the sake of clarity of presentation, we will often assume that all large numbers are integers and use ﬂoor and ceiling symbols only when we feel that not writing them explicitly might be confusing. Our asymptotic notation is also standard; in particular, we write f(n) ≪ g(n) to denote the fact that f(n)/g(n) → 0 as n → ∞. Finally, we adapt the following notational convention. A subscript of the form X.Y refers to Claim/Lemma/Proposition/Theorem X.Y. For example, we write δ6.1(·) to denote the function implicitly deﬁned in the statement of Proposition 6.1.

2. Outline of the proof

In this section, we outline the proof of our main result, Theorem 1.1. The case m = O(n) was already extensively discussed in the paragraph following the statement of Theorem 1.1, so in the remainder of the paper, we will assume that m ≫ n. This leaves us with proving the following two statements, which we will do for every r 2. First, we will show that if m (1 − ε)mr, then almost all graphs in Fn,m(Kr+1) are not r-partite. Second, we will show that if m (1 + ε)mr, then almost all graphs are r-partite. For the sake of brevity, we will refer to these two assertions

- as the 0-statement and the 1-statement, respectively. We start by giving a heuristic argument that suggests that the function mr deﬁned in (3) is indeed the sharp threshold.


- 2.1. Why is mr the sharp threshold? For the sake of clarity of presentation, we shall introduce another parameter that is related to the threshold function mr. We let pr = pr(n) be the number satisfying


2 r + 2

n r

r−1

(r+12 )−1 r = 2 −

p

log n (4) and note that

![image 22](<2013-balogh-typical-structure-sparse-free_images/imageFile22.png>)

![image 23](<2013-balogh-typical-structure-sparse-free_images/imageFile23.png>)

n2 2 · pr ≈ ex(n,Kr+1) · pr. (5)

1 r

mr = 1 −

![image 24](<2013-balogh-typical-structure-sparse-free_images/imageFile24.png>)

![image 25](<2013-balogh-typical-structure-sparse-free_images/imageFile25.png>)

Although (4) might seem like a strange way of deﬁning pr, given that we also have (5), we shall see that considering (4) and (5) in the above order is the natural way of arriving at the threshold

mr. Recall that we are aiming to count all non-r-partite graphs in Fn,m(Kr+1). Consider a ﬁxed r-partition Π = {V1,... ,Vr} that is balanced, that is, such that |Vi| ≈ nr for all i. (As we shall show in Section 4, if m ≫ n, then almost all r-colorable graphs with m edges admit only balanced proper r-colorings.) Note that the assumption that Π is balanced implies that for every i,

![image 26](<2013-balogh-typical-structure-sparse-free_images/imageFile26.png>)

n2 2

1 r

n r

r−1

|Vj| ≈

e(Π) ≈ 1 −

. (6)

and

![image 27](<2013-balogh-typical-structure-sparse-free_images/imageFile27.png>)

![image 28](<2013-balogh-typical-structure-sparse-free_images/imageFile28.png>)

![image 29](<2013-balogh-typical-structure-sparse-free_images/imageFile29.png>)

j =i

Let us try to count the graphs in Fn,m(Kr+1) that are not r-partite, but for which Π is an almost proper r-coloring, i.e., graphs with exactly one monochromatic edge in the coloring Π. The presence

of a monochromatic edge {v,w} ⊆ Vi in some G ∈ Fn,m(Kr+1) implies that G has to avoid j =i |Vj| copies of Kr−+1 in Π, where {v,w} is the missing edge. More precisely, no such G can contain all

r+1

2 −1 edges in any such copy of Kr−+1. The proportion of subgraphs of Π with m−1 edges that avoid a single copy of Kr−+1 is about 1 − (e(Π)m )(r+12 )−1. Therefore, if not containing diﬀerent copies of Kr−+1 were independent events in the space of all subgraphs of Π, then, by (4), (5), and (6), if m ≈ mr, then the proportion P of subgraphs avoiding all copies supported on the edge {v,w} would satisfy, roughly,

![image 30](<2013-balogh-typical-structure-sparse-free_images/imageFile30.png>)

P ≈ 1 −

m e(Π)

![image 31](<2013-balogh-typical-structure-sparse-free_images/imageFile31.png>)

|Vj|

(r+12 )−1 j =i

≈ exp −

n r

![image 32](<2013-balogh-typical-structure-sparse-free_images/imageFile32.png>)

r−1

1 m

(r+12 )−1 r = n−2+

2 r+2

≈

p

.

![image 33](<2013-balogh-typical-structure-sparse-free_images/imageFile33.png>)

![image 34](<2013-balogh-typical-structure-sparse-free_images/imageFile34.png>)

This hints that m ≈ mr is a ‘critical point’ as the number of graphs in Fn,m(Kr+1) that have precisely one monochromatic edge in the coloring Π is

e(Πc) 1

e(Π) m − 1

P

,

which is of the same order as e(Π)m , the number of graphs in Gn,m which are properly colored by Π, exactly when P = Θ(m1 ).

![image 35](<2013-balogh-typical-structure-sparse-free_images/imageFile35.png>)

- 2.2. Sketch of the proof of the 0-statement. Here, we assume that (1+ε)dr m (1−ε)mr. As we have already mentioned in the introduction, if m ≪ n2−2/r, then almost all graphs in Gn,m are Kr+1-free and therefore the fact that almost every graph in Fn,m(Kr+1) is not r-partite follows from the fact that dr is the sharp threshold for the property of being r-colorable in Gn,m. The existence of such a sharp threshold (for r 3) was proved by Achlioptas and Friedgut [1], see also [24]. Moreover, a fairly straightforward counting argument employing the Hypergeometric FKG Inequality (Lemma 3.2) shows that if m ≪ n2−2/(r+2), then the number of graphs in Fn,m(Kr+1) is far greater than |Gn,m(r)|, the number of r-colorable graphs in Gn,m, see Section 5.1. Therefore, we focus our attention on the case when m = Ω(n2−2/(r+2)).


As already suggested in Section 2.1, the main idea is to count graphs in Fn,m(Kr+1) that are r-colorable except for one edge. This suﬃces for our purposes, as it turns out that the number of such graphs is already asymptotically greater than the number of graphs in Fn,m(Kr+1) that are r-colorable. To this end, we ﬁrst show, in Lemma 5.3, that for a ﬁxed r-coloring Π of [n] that is balanced, that is, each of its color classes has size n/r+o(n), the number of graphs G ∈ Fn,m(Kr+1) such that e(G ∩ Πc) = 1 is asymptotically greater than the number of graphs in Fn,m(Kr+1) which are properly colored by Π. Recall from the discussion above that a graph G with e(G ∩ Πc) = 1 is Kr+1-free precisely when none of the about (n/r)r−1 copies of Kr−+1 contained in Π, where the unique edge of G ∩ Πc is the missing edge, is completely contained in G ∩ Π. Using this simple observation, we obtain a lower bound on the number of such G using the Hypergeometric FKG

Inequality (Lemma 3.2). Our bound implies that for a ﬁxed balanced Π, the number of graphs G ∈ Fn,m(Kr+1) with exactly one edge in Πc is much larger than e(Π)m , the number of graphs which are properly colored by Π. Second, in Lemma 5.4, we show that almost every G ∈ Fn,m(Kr+1) that admits an r-coloring Π satisfying e(G ∩ Πc) = 1 admits a unique such Π. Consequently, the number of such G is almost as large as the sum over all balanced r-colorings Π of the lower bounds obtained earlier, and this is much larger than |Gn,m(r)|, the number of r-colorable graphs in Gn,m.

- 2.3. Sketch of the proof of the 1-statement. Here, we assume that m (1 + ε)mr for some


2

positive constant ε. Since in particular m ≫ n−

r+2, then Theorem 1.2 implies that almost every graph in Fn,m(Kr+1) admits an r-coloring of [n] such that:

![image 36](<2013-balogh-typical-structure-sparse-free_images/imageFile36.png>)

- (i) there are only o(m) monochromatic edges,
- (ii) each color class has size n/r + o(n),
- (iii) if a vertex v is colored i, then v has at least as many neighbors in every color j as in color i.


Therefore, it suﬃces to consider only Kr+1-free graphs that admit such a coloring.

As was proved in [36], almost every graph in Gn,m(r) admits a unique r-coloring. Moreover, the number of pairs (G,Π), where G ∈ Gn,m(r) and Π is a proper r-coloring of G is asymptotic to |Gn,m(r)|, see Theorem 4.2. Therefore, it suﬃces to prove that for a ﬁxed r-coloring Π satisfying (ii) above, the number of G ∈ Fn,m(Kr+1) that satisfy (i) and (iii) for this ﬁxed coloring Π is asymptotically equal to e(Π)m , the number of graphs in Gn,m that are properly colored by Π, see Theorem 6.3.

From now on, we ﬁx some Π satisfying (ii) and count graphs G ∈ Fn,m(Kr+1) that satisfy (i) and (iii) but are not properly colored by Π. We denote the family of all such graphs by F∗. The methods of enumerating these graphs will vary with m and the distribution of the monochromatic edges of G, that is, the edges of G ∩ Πc. For technical reasons, we require separate arguments to handle the cases m ex(n,Kr+1) − ξn2 and m > ex(n,Kr+1) −ξn2, where ξ is some ﬁxed positive constant, which we term the sparse case and the dense case, respectively. The argument used for the (much easier) dense case is somewhat ad hoc and we will not dwell on it here. Instead, we refer the interested reader directly to (the self-contained) Section 8. The main business of this paper is handling the sparse case, and hence from now on we assume that m ex(n,Kr+1) − ξn2.

Recall that Π is a ﬁxed r-coloring of [n] satisfying (ii). We use two diﬀerent methods of enumerating graphs G ∈ F∗, that is, graphs in Fn,m(Kr+1) that satisfy (i) and (iii) but are not properly colored by Π, depending on whether or not most edges of G ∩ Πc are incident to vertices whose degree in G∩Πc is somewhat high. More precisely, we partition the family T of all possible graphs G ∩ Πc, where G ranges over F∗, into two classes, denoted T L (here L stands for low degree) and T H (here H stands for high degree), according to the proportion of edges that are incident to vertices whose degree exceeds βm/n, where β is a small positive constant, see Section 7.2. We then separately enumerate graphs G such that G∩Πc ∈ T L and those satisfying G∩Πc ∈ T H. We term these two parts of the argument the low degree case (Section 7.6) and the high degree case (Sections 7.7–7.9), respectively.

In the (easier) low degree case, for each T ∈ T L, we give an upper bound on the number of graphs G ∈ F∗ such that G ∩ Πc = T. Our upper bound is a function of the number of edges in a canonically chosen subgraph U(T) of T, which we deﬁne in Section 7.2. The bound is proved in Lemma 7.3, which is the core of the argument in the low degree case. In Section 7.4, we separately enumerate all T ∈ T L with a certain value of e(U(T)). This is fairly straightforward. The proof of Lemma 7.3, which bounds the number of G with G∩Πc = T ∈ T in terms of e(U(T)), is a somewhat involved application of the Hypergeometric Janson Inequality (Lemma 3.1). Let us brieﬂy describe

the main idea. The presence of an edge {v,w} of T in G ∩ Πc and the fact that G is Kr+1-free imply that G ∩ Π avoids each of the (roughly) (n/r)r−1 copies of Kr−+1 in Π, where v and w are the endpoints of the missing edge of Kr−+1. That is, at least one edge from each such copy of Kr−+1 does not belong to G ∩ Π. Whereas it is quite easy to estimate the number of subgraphs of Π with

m − e(T) edges that avoid a single copy of Kr−+1 (there are about 1 − (e(Π)m )(r+12 )−1 · m e−(Π)e(T) of

![image 37](<2013-balogh-typical-structure-sparse-free_images/imageFile37.png>)

- them) bounding the number of subgraphs that avoid all such copies of Kr−+1 for all edges {v,w} of T simultaneously requires very careful computation. The main diﬃculty lies in controlling the


correlation between the families of subgraphs of Π that avoid two diﬀerent copies of Kr−+1.

In the high degree case, where we enumerate the graphs G ∈ F∗ such that G ∩ Πc ∈ T H, we focus our attention on vertices of high degree, that is, vertices whose degree in G ∩ Πc exceeds βm/n. We count such graphs by describing and analyzing a procedure that constructs all of them in two stages. This procedure ﬁrst selects one color class, Vi, chooses which of its vertices will have high degree and then picks their neighbors, in all color classes. Next, it chooses all the remaining edges of G. In the analysis, we bound the number of choices that this procedure can make, which translates into a bound on the number of graphs in F∗ that fall into the high degree case. Let us brieﬂy describe how we obtain this bound. Suppose that we want to construct a graph G ∈ F∗, where some v ∈ Vi has at least βm/n neighbors in Vi. By (iii) above, we must guarantee that deg(v,Vj) βm/n for all j. Hence, no matter how we choose the neighborhoods of v in V1,... ,Vr, there will be a collection of at least (βm/n)r forbidden copies of Kr in Π, none of which can be fully contained in G. For a typical choice of neighborhoods of some canonically chosen set of high degree vertices in Vi (in the ﬁrst stage of the procedure), these forbidden copies of Kr are uniformly distributed and hence, using the Hypergeometric Janson Inequality (Lemma 3.1), we can obtain a strong upper bound on the number of choices of a subgraph of Π that avoids them (in the second stage of our procedure). We will refer to this possibility as the regular case. On the other hand, using Lemma 3.6, we show that there are only very few choices of the neighborhoods of these high degree vertices in Vi (in the ﬁrst stage) for which the distribution of the forbidden copies of Kr is not suﬃciently uniform to yield a strong bound on the number of choices of the remaining edges (in the second stage), as in the regular case. We will refer to this possibility as the irregular case. The proportion of graphs that fall into either the regular or the irregular case is exponentially small in m/n.

3. Preliminaries

- 3.1. Tools. In this section, we collect several auxiliary results that will be later used in the proof of Theorem 1.1. We begin with one of our main tools, a version of the Janson Inequality for the hypergeometric distribution.


- Lemma 3.1 (Hypergeometric Janson Inequality). Suppose that {Bi}i∈I is a family of subsets of an n-element set Ω, let m ∈ {0,... ,n}, and let p = m/n. Let


p|Bi| and ∆ =

p|Bi∪Bj|,

µ =

i∼j

i∈I

where the second sum is over all ordered pairs (i,j) ∈ I2 such that i = j and Bi ∩Bj = ∅. Let R be the uniformly chosen random m-subset of Ω and let B denote the event that Bi R for all i ∈ I. Then for every q ∈ [0,1],

P(B) 2 · exp −qµ + q2∆/2 .

Our main tool in the proof of the 0-statement will be the following version of the FKG Inequality for the hypergeometric distribution, which gives a lower bound on the probability P(B) from the statement of Lemma 3.1. We postpone the easy deductions of Lemmas 3.1 and 3.2 from their standard ‘binomial’ versions to Appendix A.

- Lemma 3.2 (Hypergeometric FKG Inequality). Suppose that {Bi}i∈I is a family of subsets of an n-element set Ω. Let m ∈ {0,... ,⌊n/2⌋}, let R be the uniformly chosen random m-subset of Ω, and let B denote the event that Bi R for all i ∈ I. Then for every η ∈ (0,1),

P(B)

i∈I

1 −

(1 + η)m n

![image 38](<2013-balogh-typical-structure-sparse-free_images/imageFile38.png>)

|Bi|

− exp − η2m/4 .

Finally, in the proof of Theorem 1.1 in the case m = ex(n,Kr+1) − o(n2), we will need the following folklore result from extremal graph theory. As we were unable to ﬁnd a good reference, we give a proof of this result in Appendix A. Below, K(n1,... ,nr) denotes the complete r-partite graph whose r color classes have sizes n1,... ,nr, respectively.

- Lemma 3.3. For every integer r 2 and all integers n1,... ,nr satisfying n1 ... nr, ex K(n1,... ,nr),Kr = e K(n1,... ,nr) − n1n2.

We remark here that our proof of Lemma 3.3 shows that the unique extremal graph is obtained by removing all edges joining some two smallest classes.

3.2. Estimates for binomial coeﬃcients. Throughout the paper, we will often use various estimates for expressions involving binomial coeﬃcients. In this section, we collect some of them for future reference. We start with an easy corollary of Vandermonde’s identity.

- Lemma 3.4. For every a, b, c, and d with d c, a d

- b
- c − d


a + b c

.

Our next lemma estimates the ratio between ac and bc for a,b,c satisfying a > b > c > 0.

- Lemma 3.5. If a > b > c > 0, then

- a

![image 39](<2013-balogh-typical-structure-sparse-free_images/imageFile39.png>)

- b


c

·

- b
- c


a c

- a − c

![image 40](<2013-balogh-typical-structure-sparse-free_images/imageFile40.png>)

- b − c


c

·

- b
- c


.

3.3. Main tool. A crucial ingredient in the proof of Theorem 1.1 is an estimate of the upper tail of the distribution of the number of edges in a random subhypergraph of a sparse k-uniform k-partite hypergraph, Lemma 3.6 below. It formalizes the following statement: If some H ⊆ V1 × ... × Vk contains only a tiny proportion of all the k-tuples in V1 × ... × Vk, then the probability that, for a random choice of d-elements sets W1 ⊆ V1,... ,Wk ⊆ Vk, a much larger proportion of W1×...×Wk falls in H decays exponentially in d.

- Lemma 3.6. For every integer k and all positive α and λ, there exists a positive τ such that the following holds. Let V1,... ,Vk be ﬁnite sets and let d be an integer satisfying 2 d min{|V1|,... ,|Vk|}. Suppose that H ⊆ V1 × ... × Vk satisﬁes


k

|Vi|

|H| τ

i=1

and that W1,... ,Wk are uniformly chosen random d-subsets of V1,... ,Vk, respectively. Then, P |H ∩ (W1 × ... × Wk)| > λdk αd.

We prove Lemma 3.6 in Appendix A. We just remark here that our proof yields that one can take τ = (α/2)k2/λ · λk · d−k3/(dλ). (Although the above expression depends on d, this dependence is not crucial as d−1/d e−1/e for all d. We made the dependence on d above explicit only because d−k3/(dλ) e−1 when d/log d k3/λ.)

4. On r-colorable graphs

Recall that Gn,m(r) is the family of all r-partite (r-colorable) graphs on the vertex set [n] that have exactly m edges and that Pn,r is the collection of all r-colorings of [n] (partitions of [n] into

- at most r parts). Given a Π ∈ Pn,r, we deﬁne Gm(Π) to be the family of all G ∈ Gn,m(r) that are properly colored by Π, that is,


Gm(Π) = {G ∈ Gn,m(r): G ⊆ Π}. Note that |Gm(Π)| = e(Π)m . Trivially, we have

Gm(Π).

Gn,m(r) =

Π∈Pn,r

We will be particularly interested in balanced r-colorings, that is, ones where all the color classes have approximately n/r elements. More precisely, given a positive γ, we let Pn,r(γ) be the family of all partitions of [n] into r parts V1,... ,Vr such that

1 r

1 r − γ n |Vi|

+ γ n for all i ∈ [r]. (7) That is,

![image 41](<2013-balogh-typical-structure-sparse-free_images/imageFile41.png>)

![image 42](<2013-balogh-typical-structure-sparse-free_images/imageFile42.png>)

Pn,r(γ) = {V1,... ,Vr} ∈ Pn,r : (7) holds . We can easily neglect colorings that are not balanced in the above sense. The following proposition, originally proved in [36], shows that if m ≫ n, then almost every graph in Gn,m(r) admits only balanced r-colorings. The easy proof of Proposition 4.1 is given in Appendix A.

- Proposition 4.1. For every positive γ, there exists a constant c such that if m cn, then


|Gm(Π)| ≪

Π ∈Pn,r(γ)

ex(n,Kr+1) m |Gn,m(r)|.

Even though the collections Gm(Π) are generally not pairwise disjoint, there is not too much overlap between them. More precisely, if Π is not very unbalanced, then, for an overwhelming proportion of all G ∈ Gm(Π), the r-coloring Π is their unique proper r-coloring. The following rigorous version of this statement follows from the (much stronger) results proved in [36].

Theorem 4.2. For every integer r 2, every 0 < γ 1/2r, and every m ≫ nlog n,

e(Π) m

|Gn,m(r)| = (1 + o(1))

|Gm(Π)| = (1 + o(1))

.

Π∈Pn,r(γ)

Π∈Pn,r(γ)

We remark here that Theorem 4.2 is an easy consequence of Proposition 4.1, above, and Proposition 5.5 proved in the next section.

5. The 0-statement

Our aim here is to show that if (1+ε)dr m (1−ε)mr, then almost all graphs in Fn,m(Kr+1) are not r-colorable. As already discussed before, given the (diﬃcult and interesting) result establishing when almost all graphs in Gn,m stop being r-colorable [1], we may assume that m ≫ n. We ﬁrst give an easy argument that works in the case n ≪ m ≪ n2−2/(r+2) and then present a more complicated argument that works for all m satisfying nlog n ≪ m (1 − ε)mr.

- 5.1. Counting very sparse Kr+1-free graphs. In this section, generalizing a counting argument of Pr¨omel and Steger [37], we show that if m satisﬁes n ≪ m ≪ n2−2/(r+2), then in fact, almost


all graphs in Fn,m(Kr+1) have arbitrarily high chromatic number. For our purposes, we only need the statement of Lemma 5.1 in the case k = r.

Lemma 5.1. For every k 2, there exist c > 0 and d > 0 such that

|Fn,m(Kr+1)| ≫ |Gn,m(k)| for all m satisfying cn m dn2−2/(r+2). Proof. Let Gn,m be the uniformly selected random element of Gn,m. Clearly,

n 2

|Fn,m(Kr+1)| = P[Gn,m is Kr+1-free] ·

. (8)

m

By Lemma 3.5, we have that for suﬃciently large n,

n 2

m

n 2

![image 43](<2013-balogh-typical-structure-sparse-free_images/imageFile43.png>)

ex(n,Kk+1)

m

·

ex(n,Kk+1) m

m k+1

·

e

![image 44](<2013-balogh-typical-structure-sparse-free_images/imageFile44.png>)

ex(n,Kk+1) m

, (9)

where in the last inequality we used the fact that ex(n,Kk+1) = (1 − k1) n2 + O(n). Note that if m = n2−2/(r+2), then

![image 45](<2013-balogh-typical-structure-sparse-free_images/imageFile45.png>)

nr+1 ·

- m

![image 46](<2013-balogh-typical-structure-sparse-free_images/imageFile46.png>)

- n2


(r+12 )

= m.

Since there are fewer than nr+1 copies of Kr+1 in the complete graph on n vertices, the Hypergeometric FKG Inequality (Lemma 3.2, where we set η = 1/2) implies that if m dn2−2/(r+2) for some constant d, then

m 16

P[Gn,m is Kr+1-free] + exp −

![image 47](<2013-balogh-typical-structure-sparse-free_images/imageFile47.png>)

1 −

4m n2

![image 48](<2013-balogh-typical-structure-sparse-free_images/imageFile48.png>)

(r+12 ) nr+1

exp −5(r+12 )d(r+12 )−1m , (10)

provided that n is suﬃciently large. Therefore, if d is suﬃciently small (i.e., when the right-hand side of (10) is larger than e−m/16 + e−m/((k+1)(k+2))), then by (8), (9), and (10),

ex(n,Kk+1) m ≫ kn ·

ex(n,Kk+1)

m k+2

·

|Fn,m(Kr+1)| e

m |Gn,m(k)|, provided that m cn for a suﬃciently large constant c.

![image 49](<2013-balogh-typical-structure-sparse-free_images/imageFile49.png>)

- 5.2. Counting Kr+1-free graphs with one monochromatic edge. In this section, generalizing the approach of Osthus, Pr¨omel, and Taraz [33], we count graphs in Fn,m(Kr+1) that are r-colorable except for one edge. We show that if m satisﬁes nlog n ≪ m (1−ε)mr, then the number of such graphs is already much larger than Gn,m(r). In particular, we shall deduce the following.


- Proposition 5.2. For every r 2, every ε > 0, and every m satisfying nlog n ≪ m (1 − ε)mr, |Fn,m(Kr+1)| ≫ |Gn,m(r)|.


Recall the deﬁnitions of Pn,r(γ) and Gm(Π) given in Section 4. Given a Π ∈ Pn,r, and an edge e ∈ Πc, we deﬁne

Gm(Π,e) = {G + e: G ∈ Gm−1(Π)}.

Note that |Gm(Π,e)| = m e(Π)−1 and that Gm(Π,e) ∩ Gm(Π,f) = ∅ if e = f. We ﬁrst show that if Π is balanced, then for every edge e ∈ Πc, the family Gm(Π,e) contains many Kr+1-free graphs.

We ﬁrst set some parameters. Recall that a constant ε ∈ (0,1) is given. Let γ and η be small positive constants such that

(1 + η)(1 − ε) (1 − rγ)2

ε 2

ε 4

and (1 + γr)r−1 1 +

1 −

. (11) Note also that every Π ∈ Pn,r(γ) satisﬁes

![image 50](<2013-balogh-typical-structure-sparse-free_images/imageFile50.png>)

![image 51](<2013-balogh-typical-structure-sparse-free_images/imageFile51.png>)

![image 52](<2013-balogh-typical-structure-sparse-free_images/imageFile52.png>)

2

n2 2

r 2 ·

1 r − γ n

1 r

= (1 − rγ)2 1 −

. (12) We are now ready to state and prove our main lemma.

e(Π)

![image 53](<2013-balogh-typical-structure-sparse-free_images/imageFile53.png>)

![image 54](<2013-balogh-typical-structure-sparse-free_images/imageFile54.png>)

![image 55](<2013-balogh-typical-structure-sparse-free_images/imageFile55.png>)

- Lemma 5.3. For all Π ∈ Pn,r(γ) and m with n m (1 − ε)mr, we have


e(Π) m − 1

1 m ·

|Gm(Π,e) ∩ Fn,m(Kr+1)| ≫

.

![image 56](<2013-balogh-typical-structure-sparse-free_images/imageFile56.png>)

Proof. Suppose that Π = {V1,... ,Vr} and that e lies in Vi. Let K be the collection of (the edge sets of) all copies of Kr−+1 induced in Π by the two endpoints of the edge e and one vertex from each Vj with j = i. Let Gn,m−1 be the random element of Gm−1(Π) and note that

e(Π) m − 1

|Gm(Π,e) ∩ Fn,m(Kr+1)| = P(Gn,m−1 K for every K ∈ K) ·

. (13)

Denote the above probability by P. We need to show that P ≫ 1/m. By the Hypergeometric FKG Inequality (Lemma 3.2),

P 1 −

(1 + η)(m − 1) e(Π)

![image 57](<2013-balogh-typical-structure-sparse-free_images/imageFile57.png>)

(r+12 )−1

|K|

η2(m − 1) 4

− exp −

![image 58](<2013-balogh-typical-structure-sparse-free_images/imageFile58.png>)

. (14)

Observe that by (11), |K|

1 r

+ γ

![image 59](<2013-balogh-typical-structure-sparse-free_images/imageFile59.png>)

r−1

nr−1 = (1 + γr)r−1 ·

n r

![image 60](<2013-balogh-typical-structure-sparse-free_images/imageFile60.png>)

r−1

ε 4 ·

1 +

![image 61](<2013-balogh-typical-structure-sparse-free_images/imageFile61.png>)

n r

![image 62](<2013-balogh-typical-structure-sparse-free_images/imageFile62.png>)

r−1

.

Hence, if n m n2−2/(r+2), then P c for some positive constant c. Therefore, we may assume that n2−2/(r+2) m (1 − ε)mr. Recall that Π ∈ Pn,r(γ) and hence by (11) and (12), recalling the deﬁnition of pr from (5),

(1 + η)(m − 1) e(Π)

(1 + η)(1 − ε)mr (1 − rγ)2 1 − 1r n22

ε 2

1 −

pr.

![image 63](<2013-balogh-typical-structure-sparse-free_images/imageFile63.png>)

![image 64](<2013-balogh-typical-structure-sparse-free_images/imageFile64.png>)

![image 65](<2013-balogh-typical-structure-sparse-free_images/imageFile65.png>)

![image 66](<2013-balogh-typical-structure-sparse-free_images/imageFile66.png>)

![image 67](<2013-balogh-typical-structure-sparse-free_images/imageFile67.png>)

Therefore, recalling (4), using the fact that pr ≪ 1 and 1 − x exp(−x − x2) if x 12, we continue (14) as follows:

![image 68](<2013-balogh-typical-structure-sparse-free_images/imageFile68.png>)

η2(m − 1) 4

P + exp −

![image 69](<2013-balogh-typical-structure-sparse-free_images/imageFile69.png>)

ε 2

exp − 1 −

![image 70](<2013-balogh-typical-structure-sparse-free_images/imageFile70.png>)

(r+12 )−1 r

p

n r

![image 71](<2013-balogh-typical-structure-sparse-free_images/imageFile71.png>)

r−1

1 m

= n−(1−2ε)·(2−r+22 ) ≫

.

![image 72](<2013-balogh-typical-structure-sparse-free_images/imageFile72.png>)

![image 73](<2013-balogh-typical-structure-sparse-free_images/imageFile73.png>)

![image 74](<2013-balogh-typical-structure-sparse-free_images/imageFile74.png>)

Since

e(Π) m − 1

e(Π) m

m e(Π) ·

, it follows from Lemma 5.3 that if n is suﬃciently large, then

![image 75](<2013-balogh-typical-structure-sparse-free_images/imageFile75.png>)

e(Πc) e(Π) ·

|Gm(Π,e) ∩ Fn,m(Kr+1)| ≫

![image 76](<2013-balogh-typical-structure-sparse-free_images/imageFile76.png>)

Π∈Pn,r(γ) e∈Πc

Π∈Pn,r(γ)

e(Π) m

1 2r · |Gn,m(r)|, (15)

![image 77](<2013-balogh-typical-structure-sparse-free_images/imageFile77.png>)

where the last inequality follows from Theorem 4.2 and the fact that e(Πc)/e(Π) 1/(2r − 2) for every Π ∈ Pn,r, provided that n 2r. The left hand side of (15) counts the pairs (G,Π) such that G ∈ Gm(Π,e) ∩ Fn,m(Kr+1) for some e ∈ Πc. Therefore, in order to conclude that the number of graphs in Fn,m(Kr+1) with exactly one monochromatic edge is much larger than |Gn,m(r)|, it is enough to show that for every Π ∈ Pn,r(γ) and every e ∈ Πc, an overwhelming proportion of all G ∈ Gm(Π,e), and hence also an overwhelming proportion of all G ∈ Gm(Π,e) ∩ Fn,m(Kr+1), do not belong to any other Gm(Π′,f) with Π′ = Π and f ∈ (Π′)c.

To this end, given a Π ∈ Pn,r and e ∈ Πc, let Um(Π,e) be the family of all G ∈ Gm(Π,e) for which the pair (Π,e) is unique, that is, such that G  ∈ Gm(Π′,f) for any Π′ ∈ Pn,r and f ∈ (Π′)c with Π′ = Π. Our second key lemma in the proof of the 0-statement is the following.

- Lemma 5.4. For every positive a, there exists a constant c such that for all Π ∈ Pn,r(21r) and m cn log n we have


![image 78](<2013-balogh-typical-structure-sparse-free_images/imageFile78.png>)

|Gm(Π,e) \ Um(Π,e)| n−a · |Gm(Π,e)|.

In the proof of Lemma 5.4, we will need an estimate on the number of non-uniquely r-colorable graphs. Given a Π ∈ Pn,r, let Um(Π) be the family of all graphs in Gm(Π) for which Π is the unique proper r-coloring. The following result is implicit in the work of Pr¨omel and Steger [36]. For completeness, we give a proof of it in Appendix A.

- Proposition 5.5. For every positive a, there exists a constant c such that for every Π ∈ Pn,r(21r), if m cn log n, then


![image 79](<2013-balogh-typical-structure-sparse-free_images/imageFile79.png>)

|Gm(Π) \ Um(Π)| n−a · |Gm(Π)|.

Proof of Lemma 5.4. By deﬁnition, if G ∈ Gm(Π,e) \ Um(Π,e) then G ∈ Gm(Π,e) ∩ Gm(Π′,f) for some Π = Π′ and f ∈ (Π′)c. Considering the two cases e = f and e = f, we infer that either G − e ∈ Gm−1(Π) \ Um−1(Π) or G − {e,f} ∈ Gm−2(Π) \ Um−2(Π). Let a′ = a + 5 and recall that |Gm(Π,e)| = |Gm−1(Π)| = m e(Π)−1 . By Proposition 5.5, if m cn log n for a suﬃciently large constant c, then

|Gm(Π,e) \ Um(Π,e)| n−a′ · |Gm−1(Π)| + n2 · |Gm−2(Π)| 2n−a′+4 ·

where the last inequality holds since |Gm−2(Π)| = m e(Π)−2 n2 · m e(Π)−1 .

e(Π) m − 1

,

Proof of Proposition 5.2. Finally, if nlog n ≪ m (1 − ε)mr, then using Lemmas 5.3 and 5.4 we conclude that if n is suﬃciently large, then (below Π ranges over Pn,r(γ))

|Fn,m(Kr+1)|

Um(Π,e) ∩ Fn,m(Kr+1) =

Π e∈Πc

Π e∈Πc

Um(Π,e) ∩ Fn,m(Kr+1)

Π e∈Πc

≫

Π e∈Πc

Gm(Π,e) ∩ Fn,m(Kr+1) − Gm(Π,e) \ Um(Π,e)

1 m −

1 m2 ·

![image 80](<2013-balogh-typical-structure-sparse-free_images/imageFile80.png>)

![image 81](<2013-balogh-typical-structure-sparse-free_images/imageFile81.png>)

e(Π) m − 1

1 3r · |Gn,m(r)|,

![image 82](<2013-balogh-typical-structure-sparse-free_images/imageFile82.png>)

where the last inequality follows from Proposition 4.1, cf. (15). This completes the proof of the

- 0-statement.


6. The 1-statement In the remainder of the paper, we will show that if m (1 + ε)mr for some positive constant ε,

- then |Fn,m∗ (Kr+1)| ≪ |Fn,m(Kr+1)|, which implies that |Fn,m(Kr+1)| = (1+o(1))·|Gn,m(r)|. In this section, we set up some notation and parameters and show that, as already pointed out before, we


may restrict our attention to Kr+1-free graphs that admit a balanced r-coloring with few monochromatic edges. This leads to formulating Theorem 6.3, a technical statement formalizing the above claim that graphs which admit a balanced r-coloring with few monochromatic edges constitute the vast majority of Fn,m(Kr+1). We then show how Theorem 6.3, together with Theorem 1.2, implies the 1-statement of Theorem 1.1. We close the section by deﬁning the split into the sparse and the dense case, which are then handled in Sections 7 and 8, respectively.

- 6.1. Almost r-colorability. We begin with a fairly straightforward reﬁnement of Theorem 1.2,


- Proposition 6.1 below. Roughly speaking, it says that if m ≫ n2−2/(r+1), then not only does almost


every G ∈ Fn,m(Kr+1) admit an r-coloring Π that makes merely o(m) edges of G monochromatic, but moreover, for almost every such G, every Π with this property has r parts of size n/r + o(n).

Proposition 6.1. For every positive integer r and all positive γ and δ, there exists a C such that if m Cn2−

2

r+2, then almost every G ∈ Fn,m(Kr+1) admits a partition Π = {V1,... ,Vr} of [n] such that

![image 83](<2013-balogh-typical-structure-sparse-free_images/imageFile83.png>)

r

e(G \ Π) =

eG(Vi) δm. (16)

i=1

Moreover, if δ is suﬃciently small as a function of γ, then for almost all G ∈ Fn,m(Kr+1), every Π satisfying (16) also satisﬁes (7), that is, belongs to Pn,r(γ).

Proof. Without loss of generality, we may assume that δ is suﬃciently small as a function of γ. In particular, we may assume that it satisﬁes

γ2 2

4 γ2 − (1 − δ)

δ · log

![image 84](<2013-balogh-typical-structure-sparse-free_images/imageFile84.png>)

![image 85](<2013-balogh-typical-structure-sparse-free_images/imageFile85.png>)

γ2 3

< −

. (17)

![image 86](<2013-balogh-typical-structure-sparse-free_images/imageFile86.png>)

The existence of a partition Π ∈ Pn,r satisfying (16) for almost all G ∈ Fn,m(Kr+1) follows directly from Theorem 1.2. Therefore, it suﬃces to count graphs G ∈ Fn,m(Kr+1) that admit a partition that satisﬁes (16) but not (7). To this end, ﬁx an arbitrary partition Π ∈ Pn,r that does not

satisfy (7) and observe that e(Π) is maximized when one of the parts has size ⌊(1r + γ)n + 1⌋ or ⌈(1r − γ)n − 1⌉ and the sizes of the remaining parts are as equal as possible. Therefore,

![image 87](<2013-balogh-typical-structure-sparse-free_images/imageFile87.png>)

![image 88](<2013-balogh-typical-structure-sparse-free_images/imageFile88.png>)

 

2 − min  

1 r + r−γ1 n

1 r − r−γ1 n

1 r + γ n

1 r − γ n

n

![image 89](<2013-balogh-typical-structure-sparse-free_images/imageFile89.png>)

![image 90](<2013-balogh-typical-structure-sparse-free_images/imageFile90.png>)

![image 91](<2013-balogh-typical-structure-sparse-free_images/imageFile91.png>)

![image 92](<2013-balogh-typical-structure-sparse-free_images/imageFile92.png>)

![image 93](<2013-balogh-typical-structure-sparse-free_images/imageFile93.png>)

![image 94](<2013-balogh-typical-structure-sparse-free_images/imageFile94.png>)

+ (r − 1)

+ (r − 1)

,

2

2

2

2

 is an upper bound on e(Π). It follows that

n r

γ2r 2(r − 1)

γ2n2 2

n 2 − r

n2 ex(n,Kr+1) −

![image 95](<2013-balogh-typical-structure-sparse-free_images/imageFile95.png>)

2 −

e(Π)

. (18)

![image 96](<2013-balogh-typical-structure-sparse-free_images/imageFile96.png>)

![image 97](<2013-balogh-typical-structure-sparse-free_images/imageFile97.png>)

Note that the number NΠ of graphs G ∈ Fn,m(Kr+1) for which (16) holds for our ﬁxed partition Π satisﬁes

δm

n 2

n 2

e(Π) m − δm

e(Π) m − t

m ·

NΠ

, (19)

δm

t

t=0

where the second inequality holds because the summand in (19) is an increasing function of t on the interval [0,m/2]. Now, using our bound on e(Π) for Π that do not satisfy (7), we have

NΠ m ·

m ·

m ·

ex(n,Kr+1) − γ22n2 m − δm

n 2

![image 98](<2013-balogh-typical-structure-sparse-free_images/imageFile98.png>)

δm

δm γ2n2 4

n 2 − δm

![image 99](<2013-balogh-typical-structure-sparse-free_images/imageFile99.png>)

δm ·

![image 100](<2013-balogh-typical-structure-sparse-free_images/imageFile100.png>)

γ2n2

4 − δm

![image 101](<2013-balogh-typical-structure-sparse-free_images/imageFile101.png>)

(1−δ)m

δm

γ2 2

4 γ2

· 1 −

·

![image 102](<2013-balogh-typical-structure-sparse-free_images/imageFile102.png>)

![image 103](<2013-balogh-typical-structure-sparse-free_images/imageFile103.png>)

ex(n,Kr+1) − γ22n2 ex(n,Kr+1) − γ24n2

![image 104](<2013-balogh-typical-structure-sparse-free_images/imageFile104.png>)

![image 105](<2013-balogh-typical-structure-sparse-free_images/imageFile105.png>)

![image 106](<2013-balogh-typical-structure-sparse-free_images/imageFile106.png>)

ex(n,Kr+1) m

exp −

m−δm

ex(n,Kr+1) − γ24n2 m − δm

![image 107](<2013-balogh-typical-structure-sparse-free_images/imageFile107.png>)

γ2m 4 ·

ex(n,Kr+1) m

![image 108](<2013-balogh-typical-structure-sparse-free_images/imageFile108.png>)

,

(20)

where the second inequality follows from Lemma 3.5 (applied twice), the third inequality follows from Lemma 3.4, and the last inequality follows from (17), provided that n is suﬃciently large (and, consequently, m is suﬃciently large). Finally, the result follows from (20) since there are at

most rn partitions Π ∈ Pn,r and at least ex(n,Kmr+1) graphs in Fn,m(Kr+1).

In view of Proposition 6.1, for positive γ and δ, let Fn,m(Kr+1;δ,γ) be the collection of graphs G ∈ Fn,m(Kr+1) that satisfy (16) for some Π ∈ Pn,r(γ) and no Π  ∈ Pn,r(γ). In other words, Fn,m(Kr+1;δ,γ) is the collection of graphs G ∈ Fn,m(Kr+1) that are almost r-colorable (i.e., admit an r-coloring which makes only at most δm edges of G monochromatic) and such that every rcoloring Π that makes only at most δm edges of G monochromatic has color classes of sizes only between (1/r −γ)n and (1/r +γ)n. In this notation, Proposition 6.1 says that almost all graphs in Fn,m(Kr+1) belong to Fn,m(Kr+1;δ,γ) provided that δ is suﬃciently small as a function of γ and m C6.1(δ,γ) · n−

2

r+2.

![image 109](<2013-balogh-typical-structure-sparse-free_images/imageFile109.png>)

Claim 6.2. For every integer r and all positive γ and δ, every G ∈ Fn,m(Kr+1;δ,γ) admits a Π ∈ Pn,r(γ) that satisﬁes (16) and such that each vertex of G has at least as many neighbors in each color class of Π as in its own class, that is, letting Π = {V1,... ,Vr},

degG(v,Vj) for all i ∈ [r] and v ∈ Vi. (21)

degG(v,Vi) min

j =i

Proof. To see this, given such a G, let Π ∈ Pn,r be a partition that minimizes e(G\Π) and suppose that Π = {V1,... ,Vr}. The minimality of Π immediately implies (21). Indeed, if there were i,j ∈ [r] and v ∈ Vi such that degG(v,Vi) > degG(v,Vj), then the partition Π′ obtained from Π by moving

the vertex v from Vi to Vj would satisfy e(G \ Π′) < e(G \ Π), contradicting the minimality of Π. Moreover, since e(G \ Π) δm by the deﬁnition of Fn,m(Kr+1;δ,γ) and the minimality of Π, then Π ∈ Pn,r(γ), again by the deﬁnition of Fn,m(Kr+1;δ,γ).

In view of the above, given positive constants γ and δ and a balanced r-coloring Π ∈ Pn,r(γ), let

Fn,m(Kr+1;δ,γ,Π) = G ∈ Fn,m(Kr+1;δ,γ): (G,Π) satisfy (16) and (21) . By Claim 6.2, we have

Fn,m(Kr+1;δ,γ) =

Fn,m(Kr+1;δ,γ,Π). (22)

Π∈Pn,r(γ)

Next, let us break down the family Fn,m∗ (Kr+1) of non-r-colorable Kr+1-free graphs with respect

- to the above partition of Fn,m(Kr+1). First, let Fn,m∗ (Kr+1;δ,γ) = Fn,m(Kr+1;δ,γ) \ Gn,m(r),


then let

Fn,m∗ (Kr+1;δ,γ,Π) = G ∈ Fn,m(Kr+1;δ,γ,Π): e(G \ Π) > 0 , and note that, by (22),

Fn,m∗ (Kr+1;δ,γ) ⊆

Fn,m∗ (Kr+1;δ,γ,Π). (23)

Π∈Pn,r(γ)

(Note that we cannot write an equality in (23) since the fact that G ∈ Fn,m∗ (Kr+1;δ,γ,Π) for some Π does not mean that G is not r-colorable).

2

Finally, since under the assumption that m (1 + ε)mr ≫ n2−

r+2, Proposition 6.1 applies with arbitrarily small γ and δ, it is enough to prove the following theorem, which is the essence of the

![image 110](<2013-balogh-typical-structure-sparse-free_images/imageFile110.png>)

- 1-statement of Theorem 1.1.


Theorem 6.3. For every integer r and every positive ε, there exist a positive constant γ and a function ω satisfying ω(n) → ∞ as n → ∞ such that the following holds for all suﬃciently small positive δ. For every n, if m (1 + ε)mr, then

|Fn,m∗ (Kr+1;δ,γ,Π)|

1 ω(n) ·

![image 111](<2013-balogh-typical-structure-sparse-free_images/imageFile111.png>)

e(Π) m

for every Π ∈ Pn,r(γ). (24)

Indeed, Theorem 4.2 and Proposition 6.1 together with (23) and (24) imply that

|Fn,m∗ (Kr+1;δ,γ,Π)|

|Fn,m∗ (Kr+1)| |Fn,m(Kr+1) \ Fn,m(Kr+1;δ,γ)| +

Π∈Pn,r(γ)

e(Π) m

1 ω(n) ·

= o |Fn,m(Kr+1)| +

![image 112](<2013-balogh-typical-structure-sparse-free_images/imageFile112.png>)

Π∈Pn,r(γ)

1

ω(n) · (1 + o(1)) · |Gn,m(r)| ≪ |Fn,m(Kr+1)|. In the remainder of the paper, we will prove Theorem 6.3.

o |Fn,m(Kr+1)| +

![image 113](<2013-balogh-typical-structure-sparse-free_images/imageFile113.png>)

- 6.2. Parameters. We now choose some parameters. Recall that an integer r and a positive constant ε are given. We may clearly assume that ε 1. We ﬁrst deﬁne the split between the sparse and the dense cases, see Section 2.3. To this end, we let

ξ =

29e 3

![image 114](<2013-balogh-typical-structure-sparse-free_images/imageFile114.png>)

−30r3

. (25)

Next, we choose small positive ρ and γ with γ < 91r so that, letting ζ =

![image 115](<2013-balogh-typical-structure-sparse-free_images/imageFile115.png>)

1 + ε 1 − ρ ·

![image 116](<2013-balogh-typical-structure-sparse-free_images/imageFile116.png>)

1 1 − rγ

![image 117](<2013-balogh-typical-structure-sparse-free_images/imageFile117.png>)

r−1

, (26) we have

ζ 2r and 1 +

- 3ε

![image 118](<2013-balogh-typical-structure-sparse-free_images/imageFile118.png>)

- 4


(r+12 )−1

1 +

ε 3 · ζ. (27)

![image 119](<2013-balogh-typical-structure-sparse-free_images/imageFile119.png>)

For example, we may take ρ = 20ε and γ = 9rε+9. Our assumption that γ < 91r guarantees that for every Π ∈ Pn,r(γ),

![image 120](<2013-balogh-typical-structure-sparse-free_images/imageFile120.png>)

![image 121](<2013-balogh-typical-structure-sparse-free_images/imageFile121.png>)

![image 122](<2013-balogh-typical-structure-sparse-free_images/imageFile122.png>)

e(Π)

r 2 ·

1 r − γ n

![image 123](<2013-balogh-typical-structure-sparse-free_images/imageFile123.png>)

2 r 2 ·

8n 9r

![image 124](<2013-balogh-typical-structure-sparse-free_images/imageFile124.png>)

2 3n2 16

![image 125](<2013-balogh-typical-structure-sparse-free_images/imageFile125.png>)

. (28)

Finally, let us also assume that we have chosen a small positive constant δ. Since this constant will have to satisfy a series of inequalities that use parameters that have not yet been introduced (but all depend only on the quantities deﬁned so far), we will make this choice more speciﬁc somewhat later in the proof. In particular, we assume that δ δ6.1(γ).

- 6.3. Setup. For the remainder of the proof, let us ﬁx some Π = {V1,... ,Vr} ∈ Pn,r(γ), assume that m (1 + ε)mr, and let


F∗ = Fn,m∗ (Kr+1;δ,γ,Π). Recall that our goal is to prove Theorem 6.3, i.e., that

|F∗|

1 ω(n) ·

![image 126](<2013-balogh-typical-structure-sparse-free_images/imageFile126.png>)

e(Π) m

for some function ω satisfying ω(n) → ∞ that does not depend on Π. We need a few more pieces of notation. Given a G ∈ F∗, for each i ∈ [r], we let Ti(G) be the subgraph of G induced by Vi, the ith color class of Π. Moreover, we let T(G) be the subgraph of all monochromatic edges of G (in the coloring Π), that is, T(G) = T1(G) ∪ ... ∪ Tr(G). As we pointed out in Section 2.3, our general strategy will be to partition the family F∗ into several classes according to the distribution of edges in the graphs T(G), show that each of these classes is small, and then deduce that |F∗| is small.

Recall that Π ∈ Pn,r(γ) is ﬁxed. Let T denote the collection of all graphs consisting of at most δm monochromatic (in the coloring Π) edges. That is, let T be the set of all graphs T ⊆ Πc with at most δm edges. Given a T ∈ T , let

F∗(T) = {G ∈ F∗: T(G) = T}.

As pointed out in Section 2.3, we will use completely diﬀerent arguments to handle the cases m e(Π) − ξn2 (the sparse case) and m > e(Π) − ξn2 (the dense case). We begin with the main, much harder, case m e(Π) − ξn2. The other case is addressed in Section 8.

7. The sparse case (m e(Π) − ξn2)

- 7.1. More parameters. First, we need to deﬁne three more parameters that will play central roles in our proof. First, let


ρ (2r)2r+1

ν =

(29) and

![image 127](<2013-balogh-typical-structure-sparse-free_images/imageFile127.png>)

m nlog n

D = ν ·

. (30)

![image 128](<2013-balogh-typical-structure-sparse-free_images/imageFile128.png>)

For the sake of clarity of presentation, we will assume that D is an integer. Next, let β be a small positive constant satisfying

βm/n

2e ξβ

mD/2. (31)

![image 129](<2013-balogh-typical-structure-sparse-free_images/imageFile129.png>)

Note that choosing such β is possible, since mD = exp(Ω(m/n)) and (ξβ2e)β → 1 as β → 0. Also, observe that D ≪ βm/n.

![image 130](<2013-balogh-typical-structure-sparse-free_images/imageFile130.png>)

- 7.2. Setup. Recall the deﬁnition of T from Section 6.3. Let us ﬁx a T ∈ T . Let U(T) be some (canonically chosen) edge-maximal subgraph of T with maximum degree at most D. Let X(T) be the set of vertices that have the maximum allowed degree in U(T), that is, the set of all v whose degree in U(T) is D. Observe that


e(U(T)) e(T − X(T)) + |X(T)| · D/2, (32) since, by the maximality of U(T), every edge of T \ U(T) has at least one endpoint in X(T).

For every i ∈ [r], let Ui(T) be the subgraph of U(T) induced by the set Vi, the ith color class of Π, and let Xi(T) = X(T) ∩ Vi. Finally, let H(T) ⊆ X(T) denote the set of vertices v in X(T) whose degree in T is at least βm/n. We will refer to vertices in H(T) as the vertices with high degree in T. We split the family T according to whether the inequality

nlog m

εξ 6 ·

m · e(U(T)) (33) does or does not hold. More precisely, we let T L be the collection of all T ∈ T for which (33) holds and let T H = T \ T L. We will separately count the graphs in F∗(T) with T ∈ T L (we will refer to it as the low degree case) and T ∈ T H (this will be referred to as the high degree case).

|H(T)|

![image 131](<2013-balogh-typical-structure-sparse-free_images/imageFile131.png>)

![image 132](<2013-balogh-typical-structure-sparse-free_images/imageFile132.png>)

- 7.3. Recap of the proof outline. There will be four main ingredients in our proof. First, in Section 7.4, in Lemmas 7.1 and 7.2, we will count the graphs T ∈ T with particular values of e(T), e(T − X(T)), |X(T)|, and |H(T)|; this is relatively straightforward. Second, in Section 7.5, in Lemma 7.3, using the Hypergeometric Janson Inequality (Lemma 3.1), we will give an upper bound on the size of F∗(T) as a function of e(U(T)). These three lemmas will already be enough to prove that the number of graphs G ∈ F∗ that fall into the low degree case (i.e., T(G) ∈ T L)


is at most m−ε/4 e(Π)m , see Lemma 7.4 in Section 7.6. In order to count the graphs G ∈ F∗ that fall into the high degree case (i.e., T(G) ∈ T H), we will have to further split them into two classes,

which we term the regular and irregular cases, depending on the distribution of the neighborhoods of the vertices in H(T(G)). We will make this division precise in Section 7.7. The third ingredient in our proof, Lemmas 7.9 and 7.10, together with Lemmas 7.1 and 7.2, provides an upper bound on the number of graphs in T F∗(T), where the union is taken over all T that fall into the regular case, see Section 7.8. Finally, in Section 7.9, we will use Lemmas 3.6 and 7.1 to bound the number of graphs that fall into the irregular case. Counting the graphs that fall into the irregular case with the use of Lemma 3.6 is the main technical novelty of this paper.

- 7.4. Counting the graphs in T . For an integer t with 1 t δm, let Tt be the subfamily of T consisting of graphs with exactly t edges. Since we are going to treat diﬀerently graphs T ∈ T with


diﬀerent values of e(T), e(U(T)), |X(T)|, and |H(T)|, let us further subdivide the families Tt. Even though the forthcoming deﬁnitions might seem somewhat odd at ﬁrst, they will be very convenient to work with later in the proof. For integers t∗, x, and h, we let Tt(t∗,x,h) be the subfamily of Tt consisting of all graphs T for which there exist sets H,X ⊆ [n] with |H| = h, |X| = x, and H ⊆ X such that:

- (i) e(T − X) = t∗, that is, T has exactly t∗ edges which have no endpoint in X,
- (ii) degT(v) < βm/n for every v  ∈ H.

Moreover, let Tt′(t∗,x,h) be the subfamily of Tt(t∗,x,h) consisting of graphs that additionally satisfy

- (iii) degT(v) βm/n for every v ∈ H. Since every T ∈ T satisﬁes (i)–(iii) above with t∗ = E(T − X(T)), X = X(T), and H = H(T), it follows that


T ∈ Te(T) e(T − X(T)),|X(T)|,|H(T)| ⊆ Te(T).

We shall now prove upper bounds on the sizes of the families Tt and Tt(t∗,x,h). We remark that the somewhat strange-looking form of these bounds will be very convenient for their later applications.

- Lemma 7.1. If t δm, then

|Tt| ·

e(Π) m − t

e ξδ

![image 133](<2013-balogh-typical-structure-sparse-free_images/imageFile133.png>)

δm

·

e(Π) m

.

- Lemma 7.2. For all integers m′, t, t∗, x, and h with m′ m,


e(Π) m′ − t

2mh ξn ·

e(Π) m′

e1/ξ · mt∗+xD/2 · exp

|Tt(t∗,x,h)| ·

.

![image 134](<2013-balogh-typical-structure-sparse-free_images/imageFile134.png>)

- Proof of Lemma 7.1. We use the trivial bound

|Tt|

e(Πc) t

. (34) We then use the identity

e(Πc) t

e(Π) m−t

![image 135](<2013-balogh-typical-structure-sparse-free_images/imageFile135.png>)

e(Π) m

=

t−1

s=0

e(Πc) s+1

e(Π) m−s−1 e(Πc) s

![image 136](<2013-balogh-typical-structure-sparse-free_images/imageFile136.png>)

e(Π) m−s

=

t−1

s=0

e(Πc) − s s + 1 ·

![image 137](<2013-balogh-typical-structure-sparse-free_images/imageFile137.png>)

m − s e(Π) − m + s + 1 to deduce that, since m e(Π) − ξn2,

![image 138](<2013-balogh-typical-structure-sparse-free_images/imageFile138.png>)

e(Πc) t

e(Π) m−t

![image 139](<2013-balogh-typical-structure-sparse-free_images/imageFile139.png>)

e(Π) m

t−1

s=0

n2 s + 1 ·

![image 140](<2013-balogh-typical-structure-sparse-free_images/imageFile140.png>)

m ξn2

![image 141](<2013-balogh-typical-structure-sparse-free_images/imageFile141.png>)

=

1 t! ·

![image 142](<2013-balogh-typical-structure-sparse-free_images/imageFile142.png>)

m ξ

![image 143](<2013-balogh-typical-structure-sparse-free_images/imageFile143.png>)

t em ξt

![image 144](<2013-balogh-typical-structure-sparse-free_images/imageFile144.png>)

t e ξδ

![image 145](<2013-balogh-typical-structure-sparse-free_images/imageFile145.png>)

δm

, (35)

where we used the fact that t! (t/e)t and that the function t  → (emξt )t is increasing on the interval (0,δm], as δ,ξ 1.

![image 146](<2013-balogh-typical-structure-sparse-free_images/imageFile146.png>)

- Proof of Lemma 7.2. We prove the lemma by induction on x. For the induction base, the case x = 0, note that if x = 0, then (in order for the family Tt(t∗,x,h) to be non-empty) we must have h = 0 and t∗ = t. Since Tt(t∗,x,h) ⊆ Tt, it now follows from (34) and (35), with m replaced by m′, that


t∗

t em ξt

t

−1 em′ ξt

e ξt∗

e(Π) m′ − t ·

e(Π) m′

mt∗ e1/ξ · mt∗,

|Tt(t∗,x,h)| ·

=

![image 147](<2013-balogh-typical-structure-sparse-free_images/imageFile147.png>)

![image 148](<2013-balogh-typical-structure-sparse-free_images/imageFile148.png>)

![image 149](<2013-balogh-typical-structure-sparse-free_images/imageFile149.png>)

where the last inequality holds because the function t∗  → (ξte∗)t∗ is maximized when t∗ = 1/ξ.

![image 150](<2013-balogh-typical-structure-sparse-free_images/imageFile150.png>)

Assume now that x 1. Given a T ∈ Tt(t∗,x,h), we ﬁx some X and H from the deﬁnition of Tt(t∗,x,h), pick an arbitrary vertex v ∈ X. Next, let d = degT(v) and obtain a subgraph T′ ⊆ T by removing all d edges incident to v. Clearly, T′ lies in Tt−d(t∗,x−1,h)∪Tt−d(t∗,x−1,h−1). Moreover, if d > βm/n, then necessarily v ∈ H (but not vice versa!) and consequently T′ ∈ Tt−d(t∗,x−1,h−1). It follows that

βm/n

n

n d |Tt−d(t∗,x − 1,h)| +

n d |Tt−d(t∗,x − 1,h − 1)|. (36)

|Tt(t∗,x,h)|

n

n

d=0

d=0

Since t m′ m e(Π) − ξn2, then

e(Π) m′−t+d−s−1

n s+1

n

d−1

d−1

m′ − t + d − s e(Π) − m′ + t − d + s + 1 d−1

n − s s + 1 ·

- d

e(Π) m′−t

![image 151](<2013-balogh-typical-structure-sparse-free_images/imageFile151.png>)

- e(Π)


=

=

![image 152](<2013-balogh-typical-structure-sparse-free_images/imageFile152.png>)

![image 153](<2013-balogh-typical-structure-sparse-free_images/imageFile153.png>)

![image 154](<2013-balogh-typical-structure-sparse-free_images/imageFile154.png>)

e(Π) m′−t+d−s

n s

s=0

s=0

m′−t+d

(37)

d em ξnd

d

m′ ξn

m′ ξn2

n s + 1 ·

1 d! ·

,

=

![image 155](<2013-balogh-typical-structure-sparse-free_images/imageFile155.png>)

![image 156](<2013-balogh-typical-structure-sparse-free_images/imageFile156.png>)

![image 157](<2013-balogh-typical-structure-sparse-free_images/imageFile157.png>)

![image 158](<2013-balogh-typical-structure-sparse-free_images/imageFile158.png>)

![image 159](<2013-balogh-typical-structure-sparse-free_images/imageFile159.png>)

s=0

where we again used the fact that d! (d/e)d. Recall that for every positive a, the function x  → (a/x)x is increasing on the interval (0,a/e] and decreasing on the interval [a/e,∞). Hence, by (37),

βm/n

n

d=0

n d

e(Π) m′−t e(Π) m′−t+d

![image 160](<2013-balogh-typical-structure-sparse-free_images/imageFile160.png>)

βm/n

n

d=0

em ξnd

![image 161](<2013-balogh-typical-structure-sparse-free_images/imageFile161.png>)

d

n2

where the last inequality follows from (31), and

e ξβ

![image 162](<2013-balogh-typical-structure-sparse-free_images/imageFile162.png>)

βm/n 1 2

![image 163](<2013-balogh-typical-structure-sparse-free_images/imageFile163.png>)

2e ξβ

![image 164](<2013-balogh-typical-structure-sparse-free_images/imageFile164.png>)

βm/n 1 2

mD/2, (38)

![image 165](<2013-balogh-typical-structure-sparse-free_images/imageFile165.png>)

n

n

d=0

n d

e(Π) m′−t e(Π) m′−t+d

![image 166](<2013-balogh-typical-structure-sparse-free_images/imageFile166.png>)

n

n

d=0

em ξnd

![image 167](<2013-balogh-typical-structure-sparse-free_images/imageFile167.png>)

d

n2 · exp

m ξn

![image 168](<2013-balogh-typical-structure-sparse-free_images/imageFile168.png>)

- 1

![image 169](<2013-balogh-typical-structure-sparse-free_images/imageFile169.png>)

- 2


exp

2m ξn

![image 170](<2013-balogh-typical-structure-sparse-free_images/imageFile170.png>)

. (39)

The claimed bound follows easily from the inductive assumption, (36), (38), and (39).

- 7.5. Bounding |F∗(T)| in terms of e(U(T)). We shall now state and prove our main lemma for the low degree case. It provides an upper bound on the size of F∗(T) in terms of the number of edges in the graph U(T). The lemma follows the natural and simple idea described in Section 2.1,


which was already exploited in [33] in the case r = 2. If m (1 + ε)mr, then, at least under all the simplifying assumptions made in Section 2.1, the proportion P of graphs in F∗(T) with exactly

one monochromatic edge is asymptotically smaller than m1 . Unfortunately, the calculation that we used to estimate P is merely some intuition to keep in mind, as in reality things are considerably

![image 171](<2013-balogh-typical-structure-sparse-free_images/imageFile171.png>)

more complicated. Whereas the intuition that avoiding diﬀerent copies of Kr−+1 in Π, whose missing edges belong to T, can be treated as independent events is valid and can be made rigorous when the graph T is small, it is no longer right when T becomes large. In fact, it turns out that considering more copies of Kr−+1 when we apply the Hypergeometric Janson Inequality (Lemma 3.1) does not necessarily improve the bound, but can actually worsen it. This is why we work with the subgraph U(T) of T with bounded maximum degree. Still, our biggest problem is that the best bound for |F∗(T)| that we can obtain using the Hypergeometric Janson Inequality is not suﬃciently strong to compensate for having to sum it over all T ∈ T . This is why we split into the low degree and the high degree cases and are forced to use diﬀerent methods to handle the high degree case.

Our main lemma in the low degree case is the following.

- Lemma 7.3. For every T ∈ T ,


e(Π) m − e(T)

|F∗(T)| 2m−(1+ε)·e(U(T)) ·

.

In the next section, we show that Lemma 7.3, together with Lemmas 7.1 and 7.2, resolves the low degree case, that is, that it implies that

e(Π) m

|{G ∈ F∗: T(G) ∈ T L}| m−ε/4 ·

, cf. Theorem 6.3. In the remainder of this section, we prove the lemma.

- Proof of Lemma 7.3. In order to prove the lemma, given a T ∈ T , we will count the number of graphs G′ ⊆ Π with m − e(T) edges such that G = G′ ∪ T is Kr+1-free. The crucial observation is that for every such G′ and every edge {v,w} ∈ Ui(T), none of the j =i |Vj| copies of Kr−+1 in Π induced by v, w, and one vertex in each Vj with j = i can be fully contained in G′. In the remainder of the proof, we will use the Hypergeometric Janson Inequality to count graphs G′ satisfying this constraint. Note that


ρ (2r)2r+1 ·

m log n

m log n

e(U(T)) Dn = ν ·

, (40) since U(T) has maximum degree at most D.

=

![image 172](<2013-balogh-typical-structure-sparse-free_images/imageFile172.png>)

![image 173](<2013-balogh-typical-structure-sparse-free_images/imageFile173.png>)

![image 174](<2013-balogh-typical-structure-sparse-free_images/imageFile174.png>)

Let K be the collection of (the edge sets of) all copies of Kr−+1 induced in Π by the two endpoints of some edge in Ui(T) and one vertex in each Vj with j = i. Given (K1,K2) ∈ K2, we write K1 ∼ K2 to denote the fact that K1 and K2 share at least one edge but K1 = K2. Let p = me−(Π)e(T) and let

![image 175](<2013-balogh-typical-structure-sparse-free_images/imageFile175.png>)

pe(K1∪K2),

pe(K) and ∆ =

µ =

K∈K

K1∼K2

where the second sum above is over all ordered pairs (K1,K2) ∈ K2 such that K1 ∼ K2. By the Hypergeometric Janson Inequality, Lemma 3.1, for every q ∈ [0,1],

e(Π) m − e(T)

|F∗(T)| 2 · exp −qµ + q2∆/2 ·

. Therefore, it suﬃces to show that for some q ∈ [0,1], we have

qµ − q2∆/2 (1 + ε)log m · e(U(T)), (41) which we will do in the remainder of the proof of the lemma. Estimating µ and ∆. Recall that our ﬁxed partition Π lies in Pn,r(γ) and hence |Vi| = (1/r±γ)n for each i ∈ [r]. It follows that

r−1

1 r − γ

nr−1 · p(r+12 )−1. (42) With the aim of estimating ∆, for every s ∈ [r − 2], let

µ = |K| · p(r+12 )−1 e(U(T)) ·

![image 176](<2013-balogh-typical-structure-sparse-free_images/imageFile176.png>)

s

1 r

ns.

|Vi|: I ⊆ [r] with |I| = s

Ns = max

+ γ

![image 177](<2013-balogh-typical-structure-sparse-free_images/imageFile177.png>)

i∈I

Let us now ﬁx two edges v1w1 and v2w2 of U(T) and compute the contribution to ∆ of all ordered pairs (K1,K2) ∈ K such that K1 ∼ K2 and v1w1 and v2w2 are the missing edges in K1 and K2, respectively. We denote these contributions by:

- • ∆1 when v1w1 and v2w2 lie in the same color class and are disjoint,


- • ∆2 when v1w1 and v2w2 lie in the same color class and share exactly one endpoint,
- • ∆3 when v1w1 = v2w2, and
- • ∆4 when v1w1 and v2w2 lie in diﬀerent color classes.


A moment’s thought reveals that

- ∆1

- r−1
- s=2


- r − 1
- s


NsNr2−s−1p2(r+12 )−(2s)−2, (43)

- ∆2

- r−1
- s=1


- r − 1
- s


NsNr2−s−1p2(r+12 )−(s+12 )−2, (44)

- ∆3


- r−2
- s=1


- r − 1
- s


NsNr2−s−1p2(r+12 )−(s+22 )−1, (45)

where s is the number of common vertices that K1 and K2 share outside of the part containing their missing edges. Moreover, note that ∆3 = 0 if r < 3. Similarly,

- r−2
- s=2


- r − 2
- s


NsNr2−s−1p2(r+12 )−(2s)−2

∆4

- r−2
- s=1


- r − 2
- s


NsNr−s−1Nr−s−2p2(r+12 )−(s+12 )−2

+ 4

- r−2
- s=0


- r − 2
- s


NsNr2−s−2p2(r+12 )−(s+22 )−2,

+ 4

(46)

where the ﬁrst, second, and third lines above correspond to the pairs K1 ∼ K2 that share no, one, and two vertices in the two parts of Π that contain the missing edges of K1 and K2; similarly as above, s is the number of common vertices that K1 and K2 share outside of the two parts of Π that containing the missing edges.

Since the maximum degree of U(T) is at most D, it is now easy to see that

∆

r

e(Ui(T))2 · ∆1 +

degU(T)(v)2 · ∆2 + e(U(T)) · ∆3 +

i=1

v∈[n]

e(U(T))2 · max{∆1,∆4} + 2De(U(T)) · ∆2 + e(U(T)) · ∆3.

Recall that e(T) δm and that

e(Ui(T))e(Uj(T)) · ∆4

i =j

m − e(T) e(Π)

p =

![image 178](<2013-balogh-typical-structure-sparse-free_images/imageFile178.png>)

m 2e(Π)

![image 179](<2013-balogh-typical-structure-sparse-free_images/imageFile179.png>)

- m

![image 180](<2013-balogh-typical-structure-sparse-free_images/imageFile180.png>)

- n2 ≫ n−


2

r+2. (47)

![image 181](<2013-balogh-typical-structure-sparse-free_images/imageFile181.png>)

It follows from (47) that nsp(2s) ≫ n2p for every s ∈ {3,... ,r} and nsp(2s) ≫ n3p3 for every s ∈ {4,... ,r}. Therefore, the sums in the right-hand sides of (43), (44), and (45) are dominated

by the terms with s equal to 2, 1, and 1, respectively, and hence

- ∆1 (1 + o(1))

r − 1 2

1 r

![image 182](<2013-balogh-typical-structure-sparse-free_images/imageFile182.png>)

+ γ

2r−4

n2r−4p2(r+12 )−3,

- ∆2 (1 + o(1))

r − 1 1

1 r

![image 183](<2013-balogh-typical-structure-sparse-free_images/imageFile183.png>)

+ γ

2r−3

n2r−3p2(r+12 )−3,

- ∆3 (1 + o(1))


r − 1 1

1 r

+ γ

![image 184](<2013-balogh-typical-structure-sparse-free_images/imageFile184.png>)

2r−3

n2r−3p2(r+12 )−4 · 1[r 3].

Similarly, the three sums in the right-hand side of (46) are dominated by the terms with s equal to 2, 1, and 0, respectively, and hence

2r−4

r − 2 2

r − 2 1

r − 2 0

1 r

n2r−4p2(r+12 )−3. The (somewhat crude) estimates

∆4 (1 + o(1))

+ 4

+ 4

+ γ

![image 185](<2013-balogh-typical-structure-sparse-free_images/imageFile185.png>)

r − 1 2

r − 2 2

r − 2 1

r − 2 0

1 r

< 2r2 and

+ γ < 1 yield that for suﬃciently large n,

max

,

+ 4

+ 4

![image 186](<2013-balogh-typical-structure-sparse-free_images/imageFile186.png>)

∆ e(U(T)) · n2r−4p2(r+12 )−4 · 2r2e(U(T))p + 2rDnp + 1[r 3] · rn . (48)

Choosing the right value for q. Recall the deﬁnition of ζ from (26). With foresight, we let q =

ζrr−1 log m nr−1p(r+12 )−1

.

![image 187](<2013-balogh-typical-structure-sparse-free_images/imageFile187.png>)

First, let us check that q 1. Note that by our assumption on m and T, m − e(T) (1 − δ)m 1 −

ε 4(1 + ε)

ε 4(1 + ε)

- 3ε

![image 188](<2013-balogh-typical-structure-sparse-free_images/imageFile188.png>)

- 4


m 1 −

mr and therefore by (5),

(1 + ε)mr = 1 +

![image 189](<2013-balogh-typical-structure-sparse-free_images/imageFile189.png>)

![image 190](<2013-balogh-typical-structure-sparse-free_images/imageFile190.png>)

m − e(T) e(Π)

mr 1 − 1r n22

- 3ε

![image 191](<2013-balogh-typical-structure-sparse-free_images/imageFile191.png>)

- 4


- 3ε

![image 192](<2013-balogh-typical-structure-sparse-free_images/imageFile192.png>)

- 4


p =

1 +

= 1 +

![image 193](<2013-balogh-typical-structure-sparse-free_images/imageFile193.png>)

![image 194](<2013-balogh-typical-structure-sparse-free_images/imageFile194.png>)

![image 195](<2013-balogh-typical-structure-sparse-free_images/imageFile195.png>)

![image 196](<2013-balogh-typical-structure-sparse-free_images/imageFile196.png>)

It follows that (recalling the deﬁnition of pr from (4))

pr.

nr−1p(r+12 )−1 rr−1

![image 197](<2013-balogh-typical-structure-sparse-free_images/imageFile197.png>)

- 3ε

![image 198](<2013-balogh-typical-structure-sparse-free_images/imageFile198.png>)

- 4


1 +

ζ · 1 +

(r+12 )−1 n r

r−1

![image 199](<2013-balogh-typical-structure-sparse-free_images/imageFile199.png>)

ε 3

2 r + 2

2 −

![image 200](<2013-balogh-typical-structure-sparse-free_images/imageFile200.png>)

![image 201](<2013-balogh-typical-structure-sparse-free_images/imageFile201.png>)

- 3ε

![image 202](<2013-balogh-typical-structure-sparse-free_images/imageFile202.png>)

- 4


(r+12 )−1 r = 1 +

p

log n ζ · log m,

(r+12 )−1

2 r + 2

2 −

![image 203](<2013-balogh-typical-structure-sparse-free_images/imageFile203.png>)

log n

where the second inequality follows from (27), and hence q 1; to see the last inequality, note that if m ≫ mr, then we may assume that ε = 1.

With the aim of establishing (41), observe ﬁrst that, by (42), (48), and the inequality γ 2 1r,

![image 204](<2013-balogh-typical-structure-sparse-free_images/imageFile204.png>)

2r2e(U(T)) n2p

1[r 3] · r np2 (2r2)rζ · log n ·

q∆ µ

2rD np

(2r2)r−1ζ · log m ·

+

+

![image 205](<2013-balogh-typical-structure-sparse-free_images/imageFile205.png>)

![image 206](<2013-balogh-typical-structure-sparse-free_images/imageFile206.png>)

![image 207](<2013-balogh-typical-structure-sparse-free_images/imageFile207.png>)

![image 208](<2013-balogh-typical-structure-sparse-free_images/imageFile208.png>)

(49)

2Dn m

+ o n−1/5 2ρ,

![image 209](<2013-balogh-typical-structure-sparse-free_images/imageFile209.png>)

where the second inequality follows from the fact that n2p m, see (47), and the fact that e(U(T)) Dn, see (40), while the ﬁnal inequality follows from (40). Recall the deﬁnitions of q and ζ. It follows from (42) and (49) that

qµ − q2∆/2 (1 − ρ)qµ (1 − ρ)q · e(U(T)) ·

= e(U(T)) · (1 + ε) · log m. This implies (41), thus completing the proof.

1 r − γ

![image 210](<2013-balogh-typical-structure-sparse-free_images/imageFile210.png>)

r−1

nr−1p(r+12 )−1

- 7.6. The low degree case. In this section, we handle the low degree case, i.e., we count all graphs


- G in F∗ with T(G) ∈ T L. Our goal is to prove the following lemma, cf. Theorem 6.3.


- Lemma 7.4. If n is suﬃciently large, then


G ∈ F∗: T(G) ∈ T L m−ε/4 ·

e(Π) m

.

Proof. Let us ﬁrst further partition the family T L. For integers t and u, let Tt,uL be the collection of all T ∈ T L with e(T) = t and e(U(T)) = u and let

εξ 6 ·

nlog m m · u .

Iu = (t∗,x,h): t∗ + xD/2 u and h

![image 211](<2013-balogh-typical-structure-sparse-free_images/imageFile211.png>)

![image 212](<2013-balogh-typical-structure-sparse-free_images/imageFile212.png>)

Observe that |Iu| u3. It follows from the deﬁnition of T L, see (33), and (32) that Tt,uL ⊆

Tt(t∗,x,h).

(t∗,x,h)∈Iu

By Lemma 7.2, if n is suﬃciently large, then

|Tt,uL | ·

e(Π) m − t

e1/ξ · mt∗+xD/2 · exp

(t∗,x,h)∈Iu

2mh ξn ·

![image 213](<2013-balogh-typical-structure-sparse-free_images/imageFile213.png>)

e(Π) m

e1/ξ · mt∗+xD/2+εu/3 ·

(t∗,x,h)∈Iu

e(Π) m

u3 · e1/ξ · m(1+ε/3)u ·

e(Π) m

m(1+2ε/3)u ·

e(Π) m

.

(50)

Furthermore, since clearly e(U(T)) min{e(T),D} for all T, it follows from (50), and Lemma 7.3 that

δm

t

e(Π) m − t

|F∗(T)|

m−(1+ε)u · |Tt,uL | ·

t=1

T∈T L

u=min{t,D}

δm

t

e(Π) m

e(Π) m

m−εu/3 ·

m−ε/4 ·

,

t=1

u=min{t,D}

where in the last inequality we used the fact that D ≫ 1 and hence

D

δm

t

m−εu/3 + (δm)2 · m−εD/3 ≪ m−ε/4.

m−εu/3

u=1

t=1

u=min{t,D}

This completes the proof in the low degree case.

- 7.7. The high degree case. Recall the deﬁnition of T H, see (33). In this section, we shall enumerate graphs in the family FH deﬁned by


FH = {G ∈ F∗: T(G) ∈ T H} =

F∗(T).

T∈T H

Our goal will be proving the following lemma, which together with Lemma 7.4 readily implies Theorem 6.3.

- Lemma 7.5. If n is suﬃciently large, then


- m

![image 214](<2013-balogh-typical-structure-sparse-free_images/imageFile214.png>)

- n ·


FH = G ∈ F∗: T(G)  ∈ T L 3exp −

e(Π) m

.

We start with the following observation. Fix a T ∈ T H and suppose that for some i ∈ [r], a vertex v ∈ Vi satisﬁes degT(v) βm/n. Since every graph G ∈ F∗(T) satisﬁes

degG(v,Vj) degG(v,Vi) = degT(v) βm/n for every j ∈ [r],

see (21), and is Kr+1-free, no matter how we choose the edges of G that are incident to v, there will be at least (βm/n)r copies of Kr (those induced by one vertex from each NG(v) ∩ Vj with j ∈ [r]) that cannot be fully contained in the graph G ∩ Π.

Given an arbitrary vertex v, assuming that its neighbors in G have already been chosen, let Hv∗ be the collection of all rj=1 degG(v,Vj) such forbidden copies of Kr, that is, let

Hv∗ = (NG(v) ∩ V1) × ... × (NG(v) ∩ Vr). We furthermore let

βm 2n

D∗ =

. (51)

![image 215](<2013-balogh-typical-structure-sparse-free_images/imageFile215.png>)

Recall the deﬁnitions from Section 7.4. Fix some t, t∗, x, and h, pick an arbitrary T ∈ Tt′(t∗,x,h), and let

h 2r

b =

.

![image 216](<2013-balogh-typical-structure-sparse-free_images/imageFile216.png>)

Let us stress the fact that we select T from Tt′(t∗,x,h) and not from Tt(t∗,x,h), which means that T contains exactly (and not at most) h vertices with degree exceeding βm/n.

Claim 7.6. There is an i ∈ [r] and a set H′ ⊆ H(T) ∩ Vi of b vertices such that degT(v,Vi \ H′) D∗ for every v ∈ H′. (52)

Proof. Since T has h vertices with degree at least βm/n, some Vi contains at least h/r of them. This set Vi can be partitioned into two sets Vi′ and Vi′′ in such a way that degT(v,Vi′′) degT(v,Vi′) for each v ∈ Vi′ and, vice versa, degT(v,Vi′) degT(v,Vi′′) for each v ∈ Vi′′. For example, one may consider a maximum cut in T[Vi]. One of these two parts, Vi′ or Vi′′, contains at least h/2r vertices with degree at least βm/n in T. We let H′ be an arbitrary b-element subset of such a set. It is easily checked that H′ satisﬁes (52).

For every T ∈ Tt′(t∗,x,h), we choose some arbitrary set H′ as in Claim 7.6. Next, given a graph

- G ∈ F∗(T), for every v ∈ H′ and each j ∈ [r], let Wj(v) be a canonically chosen D∗-element subset of NG(v) ∩ (Vj \ H′). Given such G, consider the r-uniform hypergraph H′ deﬁned by


H′ =

W1(v) × ... × Wr(v).

v∈H′

Note that H′ ⊆ v∈H′ Hv∗, that is, every edge (r-tuple) in H′ represents a copy of Kr that is forbidden to appear in G. We will enumerate graphs in FH using two diﬀerent methods, depending on the number and the distribution of edges in the hypergraph H′ = H′(G). Before we make this precise, we need a few more deﬁnitions.

Given an arbitrary H ⊆ V1 × ... × Vr, an I ⊆ [r], and an L ∈ j∈I Vj, we deﬁne the degree of L in H, denoted degH(L), by

degH(L) = |{K ∈ H: L ⊆ K}|. For s ∈ [r], the maximum s-degree ∆s(H) of H is deﬁned by

∆s(H) = max degH(L): L ∈

Vj for some I ⊆ [r] with |I| = s .

j∈I

We will measure the uniformity of the distribution of the edges of H in terms of these maximum s-degrees. First, let us ﬁx several additional parameters. Let C1 be a constant satisfying

6 εξ

4 ξ

3βC1 2r

+ 3. (53) Next, let

+

![image 217](<2013-balogh-typical-structure-sparse-free_images/imageFile217.png>)

![image 218](<2013-balogh-typical-structure-sparse-free_images/imageFile218.png>)

![image 219](<2013-balogh-typical-structure-sparse-free_images/imageFile219.png>)

- 1

![image 220](<2013-balogh-typical-structure-sparse-free_images/imageFile220.png>)

- 2r+1


and α = exp(−6C1 − 1) (54) and let τ be a small positive constant such that Lemma 3.6 holds with τ and with α, λ, and each k ∈ {2,... ,r}, i.e.,

λ =

τ3.6(k,α,λ). (55) Finally,

τ = min

2 k r

(2r)r τ

τ (2r)r

and σ =

. (56) We are ﬁnally ready to partition the family FH into the regular and irregular cases, according

C2 =

![image 221](<2013-balogh-typical-structure-sparse-free_images/imageFile221.png>)

![image 222](<2013-balogh-typical-structure-sparse-free_images/imageFile222.png>)

to the edge distribution of the hypergraphs H′. First, we let F1R be the family of all G ∈ FH such that e(H′) σnr. Second, we let

βr 2r+3r

(57)

c2 =

![image 223](<2013-balogh-typical-structure-sparse-free_images/imageFile223.png>)

and deﬁne F2R to be the family of all G ∈ FH \ F1R such that H′ contains a subhypergraph H satisfying

(D∗)r 8r

- m

![image 224](<2013-balogh-typical-structure-sparse-free_images/imageFile224.png>)

- n


r

e(H) c2 · |H(T(G))| ·

= |H(T(G))| ·

(58) and

![image 225](<2013-balogh-typical-structure-sparse-free_images/imageFile225.png>)

e(H) ns

- m

![image 226](<2013-balogh-typical-structure-sparse-free_images/imageFile226.png>)

- n


r−s

,C2 ·

for every s ∈ {2,... ,r − 1}. (59)

∆s(H) max

![image 227](<2013-balogh-typical-structure-sparse-free_images/imageFile227.png>)

Finally, we let FI = FH \(F1R ∪F2R). Counting of graphs in F1R ∪F2R and FI will be referred to as the regular and irregular cases, respectively. In the next two sections, we will prove the following estimates, which readily imply Lemma 7.5.

- Lemma 7.7. If n is suﬃciently large, then

|F1R| exp −

σm 2r+3 ·

![image 228](<2013-balogh-typical-structure-sparse-free_images/imageFile228.png>)

e(Π) m

and |F2R| exp −

- m

![image 229](<2013-balogh-typical-structure-sparse-free_images/imageFile229.png>)

- n ·


e(Π) m

.

- Lemma 7.8. If n is suﬃciently large, then


- m

![image 230](<2013-balogh-typical-structure-sparse-free_images/imageFile230.png>)

- n ·


|FI| exp −

e(Π) m

.

- 7.8. The regular case. In this section, we bound the number of graphs that fall into the regular case, that is, we prove Lemma 7.7. Our main tool will be the following two lemmas that provide upper bounds on the number of subgraphs of Π that do not fully contain any member of a collection


of forbidden copies of Kr which is either very large (Lemma 7.9) or whose members are somewhat uniformly distributed (Lemma 7.10). The proof of both of these lemmas is another application of the Hypergeometric Janson Inequality (Lemma 3.1).

- Lemma 7.9. Suppose that H ⊆ V1 × ... × Vr satisﬁes e(H) σnr. Then for every m′ with m/2 m′ m, the number of subgraphs of Π with m′ edges that do not fully contain a copy of Kr whose vertex set is an edge of H is at most

2 · exp −

σ 2r+1 · m ·

![image 231](<2013-balogh-typical-structure-sparse-free_images/imageFile231.png>)

e(Π) m′

.

- Lemma 7.10. There exists a positive c such that the following holds. Suppose that H ⊆ V1×...×Vr satisﬁes e(H) B(m/n)r for some B and (59) holds, that is,


e(H) ns

- m

![image 232](<2013-balogh-typical-structure-sparse-free_images/imageFile232.png>)

- n


r−s

∆s(H) max

,C2 ·

for every s ∈ {2,... ,r − 1}.

![image 233](<2013-balogh-typical-structure-sparse-free_images/imageFile233.png>)

Then, for every m′ with m/2 m′ m, the number of subgraphs of Π with m′ edges that do not fully contain a copy of Kr whose vertex set is an edge of H is at most

e(Π) m′

B log n n

,1 · cm ·

2 · exp −min

.

![image 234](<2013-balogh-typical-structure-sparse-free_images/imageFile234.png>)

Proof of Lemmas 7.9 and 7.10. We use the Hypergeometric Janson Inequality to count graphs satisfying our constraint. Denote the number of them by N. Let K be the collection of (the edge sets

of) all copies of Kr whose vertex set belongs to H, let p = em(Π)′ , and let µ =

![image 235](<2013-balogh-typical-structure-sparse-free_images/imageFile235.png>)

p|K1∪K2|,

p|K| and ∆ =

K1∼K2

K∈K

where the second sum above is over all ordered pairs (K1,K2) ∈ K2 such that K1 and K2 share at least one edge but K1 = K2. By the Hypergeometric Janson Inequality, letting q = min{1, ∆µ }, we have

![image 236](<2013-balogh-typical-structure-sparse-free_images/imageFile236.png>)

µ2 2∆ ·

µ 2

e(Π) m′

N 2 · exp −min

,

. Hence, in order to establish Lemma 7.9, it suﬃces to show that if e(H) σnr, then min µ,

![image 237](<2013-balogh-typical-structure-sparse-free_images/imageFile237.png>)

![image 238](<2013-balogh-typical-structure-sparse-free_images/imageFile238.png>)

µ2 ∆

σ 2r · m (60)

![image 239](<2013-balogh-typical-structure-sparse-free_images/imageFile239.png>)

![image 240](<2013-balogh-typical-structure-sparse-free_images/imageFile240.png>)

and in order to establish Lemma 7.10, it suﬃces to show that under appropriate assumptions on

- H, there exists a positive c that depends only on r and C2 such that


µ2 ∆

B log n n

,1 · cm. (61) To this end, observe that

2 · min

min µ,

![image 241](<2013-balogh-typical-structure-sparse-free_images/imageFile241.png>)

![image 242](<2013-balogh-typical-structure-sparse-free_images/imageFile242.png>)

- r−1
- s=2


µ = e(H) · p(r2) and ∆ e(H) ·

- r
- s


∆s(H)p2(r2)−(2s),

where the sth term of the sum in the upper bound on ∆ estimates the contribution of pairs K1 ∼ K2 with |V (K1) ∩ V (K2)| = s. It follows from our assumptions, see (28), that

m′ e(Π)

m 2e(Π)

mr 2e(Π)

mr 1 − 1r n2 ≫ n−

m e(Π)

8m n2

2

p =

r+2 (62)

![image 243](<2013-balogh-typical-structure-sparse-free_images/imageFile243.png>)

![image 244](<2013-balogh-typical-structure-sparse-free_images/imageFile244.png>)

![image 245](<2013-balogh-typical-structure-sparse-free_images/imageFile245.png>)

![image 246](<2013-balogh-typical-structure-sparse-free_images/imageFile246.png>)

![image 247](<2013-balogh-typical-structure-sparse-free_images/imageFile247.png>)

![image 248](<2013-balogh-typical-structure-sparse-free_images/imageFile248.png>)

![image 249](<2013-balogh-typical-structure-sparse-free_images/imageFile249.png>)

![image 250](<2013-balogh-typical-structure-sparse-free_images/imageFile250.png>)

and hence for every s ∈ {2,... ,r}, nsp(2s) n2p = n2 ·

m′ e(Π)

m 2e(Π)

n2 ·

m, (63)

![image 251](<2013-balogh-typical-structure-sparse-free_images/imageFile251.png>)

![image 252](<2013-balogh-typical-structure-sparse-free_images/imageFile252.png>)

which implies, in particular, that under the assumptions of Lemma 7.9, we have µ σm. Moreover, it follows from (62) that for every s ∈ {2,... ,r}, recalling (5),

(s+12 )−1

- m

![image 253](<2013-balogh-typical-structure-sparse-free_images/imageFile253.png>)

- n


n 8

p(s+12 )−1 n 8

p(s2) n 8

mr 1 − 1r n2

s−1

s−1

s−1

s−1

p(2s)+s−1 =

·

![image 254](<2013-balogh-typical-structure-sparse-free_images/imageFile254.png>)

![image 255](<2013-balogh-typical-structure-sparse-free_images/imageFile255.png>)

![image 256](<2013-balogh-typical-structure-sparse-free_images/imageFile256.png>)

![image 257](<2013-balogh-typical-structure-sparse-free_images/imageFile257.png>)

(64)

![image 258](<2013-balogh-typical-structure-sparse-free_images/imageFile258.png>)

(s+12 )−1 rr−1 4r2 · log n.

pr 2

n 8

s−1

·

=

![image 259](<2013-balogh-typical-structure-sparse-free_images/imageFile259.png>)

![image 260](<2013-balogh-typical-structure-sparse-free_images/imageFile260.png>)

![image 261](<2013-balogh-typical-structure-sparse-free_images/imageFile261.png>)

To see the last inequality, note that if s = r, then it follows immediately from (4). On the other hand, if 2 s < r, then actually

(s+12 )−1

(s+12 )−1 r ≫ ns−1 n−

= n(s−1)(1−rs+2+2) ≫ log n. One now easily deduces from (64) that under the assumptions of Lemma 7.10,

2 r+2

ns−1p

![image 262](<2013-balogh-typical-structure-sparse-free_images/imageFile262.png>)

![image 263](<2013-balogh-typical-structure-sparse-free_images/imageFile263.png>)

rr−1 4r2 · m. (65)

p(r2) B log n n ·

- m

![image 264](<2013-balogh-typical-structure-sparse-free_images/imageFile264.png>)

- n


r

µ B

![image 265](<2013-balogh-typical-structure-sparse-free_images/imageFile265.png>)

![image 266](<2013-balogh-typical-structure-sparse-free_images/imageFile266.png>)

We now turn to estimating µ2/∆. In the context of Lemma 7.9, we simply use the trivial bound ∆s(H) nr−s and deduce that for each s ∈ {2,... ,r − 1},

∆s(H)p−(2s) nr−sp−(s2) nr m

, where the last inequality follows from (63). It follows that

![image 267](<2013-balogh-typical-structure-sparse-free_images/imageFile267.png>)

nr m · e(H)

∆ 2r · p2(r2) ·

![image 268](<2013-balogh-typical-structure-sparse-free_images/imageFile268.png>)

and hence

µ2 ∆

- 1

![image 269](<2013-balogh-typical-structure-sparse-free_images/imageFile269.png>)

- 2r · e(H) ·


m nr

σ 2r · m,

![image 270](<2013-balogh-typical-structure-sparse-free_images/imageFile270.png>)

![image 271](<2013-balogh-typical-structure-sparse-free_images/imageFile271.png>)

![image 272](<2013-balogh-typical-structure-sparse-free_images/imageFile272.png>)

which implies (60), as we have already seen that µ σm. In the context of Lemma 7.10, it follows from (63) and (64) that for each s ∈ {2,... ,r − 1},

4r2 rr−1 ·

- (m/n)r−1

![image 273](<2013-balogh-typical-structure-sparse-free_images/imageFile273.png>)

- (m/n)s−1p(s2)


(m/n)r−1 log n

e(H) nsp(2s)

e(H) m and therefore,

∆s(H)p−(2s) max

,C2 ·

,C2 ·

max

![image 274](<2013-balogh-typical-structure-sparse-free_images/imageFile274.png>)

![image 275](<2013-balogh-typical-structure-sparse-free_images/imageFile275.png>)

![image 276](<2013-balogh-typical-structure-sparse-free_images/imageFile276.png>)

![image 277](<2013-balogh-typical-structure-sparse-free_images/imageFile277.png>)

µ2 ∆

rr−1 4r2 ·

rr−1 4r2+r

e(H)log n (m/n)r−1

B log n n

- 1

![image 278](<2013-balogh-typical-structure-sparse-free_images/imageFile278.png>)

- 2rC2 · m,


- 1

![image 279](<2013-balogh-typical-structure-sparse-free_images/imageFile279.png>)

- 2r · min


m C2

,1 · min

, which, together with (65), implies (61), completing the proof.

,

min

![image 280](<2013-balogh-typical-structure-sparse-free_images/imageFile280.png>)

![image 281](<2013-balogh-typical-structure-sparse-free_images/imageFile281.png>)

![image 282](<2013-balogh-typical-structure-sparse-free_images/imageFile282.png>)

![image 283](<2013-balogh-typical-structure-sparse-free_images/imageFile283.png>)

![image 284](<2013-balogh-typical-structure-sparse-free_images/imageFile284.png>)

![image 285](<2013-balogh-typical-structure-sparse-free_images/imageFile285.png>)

- Proof of Lemma 7.7. Recall the deﬁnitions of F1R and F2R from Section 7.7. We ﬁrst show that the


family F1R is small. In order to construct a graph G ∈ F1R, we ﬁrst choose h and t and restrict our attention to graphs G satisfying t = e(T(G)) and h = |H(T(G))|. Clearly for each such G,

βm n v

h ·

degT(G)(v) = 2t 2δm. (66)

![image 286](<2013-balogh-typical-structure-sparse-free_images/imageFile286.png>)

Then, we choose the set H′ of b vertices from some Vi, see Claim 7.6, and for each v ∈ H′, we choose the sets W1(v),... ,Wr(v) of size D∗ each. After these are ﬁxed, we choose the remaining t′ = t − bD∗ edges of T(G) and the remaining m − t′ − brD∗ (that is, m − t − b(r − 1)D∗) edges of G∩Π in such a way that G∩Π contains no copy of Kr whose vertex set is an edge of the hypergraph

- H′ (deﬁned in the previous section). The main point is that the assumption that G ∈ F1R means that e(H′) σnr and hence we may use Lemma 7.9 to bound the number of choices for G ∩ Π.


The number Z1 of ways to choose the sets W1(v) ⊆ V1,... ,Wr(v) ⊆ Vr for each v satisﬁes

r

|Vj| D∗

|V1| + ... + |Vr| r · D∗

n rD∗

Z1

=

. (67)

j=1

It now follows from the deﬁnition of F1R and Lemma 7.9 that

b

e(Π) m − t′ − brD∗

σ 2r+1 · m ·

n b ·

n rD∗

|F1R|

· |Tt′| · 2 · exp −

.

![image 287](<2013-balogh-typical-structure-sparse-free_images/imageFile287.png>)

t,h

A computation along the lines of the proof of Lemmas 7.1 and 7.2, see (37) and (39), shows that

rD∗b

b e(Π) m − t′ − rbD∗

e(Π) m − t′ exp

n b

n rD∗

n b

em ξnrD∗

·

2

2

![image 288](<2013-balogh-typical-structure-sparse-free_images/imageFile288.png>)

(68)

2mb ξn ·

e(Π) m − t′

.

![image 289](<2013-balogh-typical-structure-sparse-free_images/imageFile289.png>)

To see the last inequality, recall that the value of the function x  → (a/x)x is maximized when x = a/e, which implies that (ξnrDem ∗)rD∗b exp(mbξn ). Hence, by Lemma 7.1, since b h,

![image 290](<2013-balogh-typical-structure-sparse-free_images/imageFile290.png>)

![image 291](<2013-balogh-typical-structure-sparse-free_images/imageFile291.png>)

|F1R|

exp

t,h

σm 2r+1 ·

2mh ξn −

![image 292](<2013-balogh-typical-structure-sparse-free_images/imageFile292.png>)

![image 293](<2013-balogh-typical-structure-sparse-free_images/imageFile293.png>)

e ξδ

![image 294](<2013-balogh-typical-structure-sparse-free_images/imageFile294.png>)

δm

·

e(Π) m

. (69)

Since

δ

σ 2r+4 for suﬃciently small δ, continuing (69), we have, by (66),

σ 2r+2

4δ βξ

e ξδ

exp

and

![image 295](<2013-balogh-typical-structure-sparse-free_images/imageFile295.png>)

![image 296](<2013-balogh-typical-structure-sparse-free_images/imageFile296.png>)

![image 297](<2013-balogh-typical-structure-sparse-free_images/imageFile297.png>)

![image 298](<2013-balogh-typical-structure-sparse-free_images/imageFile298.png>)

|F1R| m2 exp

4δm βξ −

σm 2r+1

+

![image 299](<2013-balogh-typical-structure-sparse-free_images/imageFile299.png>)

![image 300](<2013-balogh-typical-structure-sparse-free_images/imageFile300.png>)

σm 2r+2 ·

![image 301](<2013-balogh-typical-structure-sparse-free_images/imageFile301.png>)

e(Π) m

σm 2r+3 ·

exp −

![image 302](<2013-balogh-typical-structure-sparse-free_images/imageFile302.png>)

e(Π) m

.

In order to complete the proof, we still need to show that the family F2R is also small. We count the graphs in F2R almost the same way as we counted the graphs in F1R. That is, we ﬁrst choose h and t and consider only graphs G with t = e(T(G)) and h = |H(T(G))|. Then, with t and h

ﬁxed, we choose the set H′ of b vertices from some Vi and for each v ∈ H′, we select the sets

- W1(v),... ,Wr(v). Finally, we choose the remaining t′ = t − bD∗ edges of T(G) and the remaining


m − t′ − brD∗ edges of G ∩ Π. The assumption that G ∈ F2R means that we may use Lemma 7.10 with B = c2h to bound the number of choices for G ∩ Π.

The main diﬀerence in our treatment of F2R, compared to the argument for F1R given above, is that we now use a stronger bound on the number of choices of the t′ edges of T(G) that are selected in the second stage of the above procedure. To this end, we ﬁx some x and t∗ and further restrict our attention to graphs G that satisfy x = |X(T(G))| and t∗ = e(T(G) − X(T(G))). In particular, we are only counting graphs G ∈ F2R that satisfy T(G) ∈ Tt′(t∗,x,h). Let T′ be the graph consisting of the t′ edges of T(G) that we choose after selecting the bD∗ edges of T(G) that we ﬁxed while we were choosing Wi(v) for all v ∈ H′. Since T(G) ∈ Tt′(t∗,x,h) and all edges of T(G) \ T′ have an endpoint in H′, it is not hard to see that T′ must be in Tt′(t∗,x,h). Indeed, the set H(T(G)) contains all vertices whose degree in T(G) exceeds βm/n (and hence also all vertices whose degree in T′ exceeds βm/n), and we may obtain T′ from T(G) by deleting only edges incident to H′ ⊆ H(T(G)) ⊆ X(T(G)), which means that the number of edges that have no endpoints in the set X(T(G)) is t∗ in both T(G) and T′. With this additional information about T′, we may now appeal to Lemma 7.2 in place of Lemma 7.1 in order to get a stronger bound on the number of choices for T′. It now follows (cf. the calculation leading up to (69)) from the deﬁnition of F2R and Lemma 7.10 with B = c2h that, letting c be the constant from the statement of Lemma 7.10,

e(Π) m − t′

c2hlog n n

2mb ξn · |Tt′(t∗,x,h)| · exp −min

|F2R|

,1 · cm ·

. (70)

exp

![image 303](<2013-balogh-typical-structure-sparse-free_images/imageFile303.png>)

![image 304](<2013-balogh-typical-structure-sparse-free_images/imageFile304.png>)

t,t∗,x,h

- Let F2(t,t∗,x,h) denote the term in the sum in the right hand side of (70). If c2hlog n n, then we use the fact that Tt′(t∗,x,h) ⊆ Tt′ and t′ t δm and, using Lemma 7.1, we further estimate F2(t,t∗,x,h) as follows (recall that b h):


δm

2mh ξn − cm ·

e(Π) m exp

e ξδ

F2(t,t∗,x,h) exp

·

![image 305](<2013-balogh-typical-structure-sparse-free_images/imageFile305.png>)

![image 306](<2013-balogh-typical-structure-sparse-free_images/imageFile306.png>)

δm

e(Π) m

e(Π) m

e ξδ

4δm βξ − cm ·

cm 4 ·

·

exp −

, where we used (66) and the fact that

![image 307](<2013-balogh-typical-structure-sparse-free_images/imageFile307.png>)

![image 308](<2013-balogh-typical-structure-sparse-free_images/imageFile308.png>)

![image 309](<2013-balogh-typical-structure-sparse-free_images/imageFile309.png>)

e ξδ

![image 310](<2013-balogh-typical-structure-sparse-free_images/imageFile310.png>)

δ

< e2c and

![image 311](<2013-balogh-typical-structure-sparse-free_images/imageFile311.png>)

4δ βξ

c 4

<

,

![image 312](<2013-balogh-typical-structure-sparse-free_images/imageFile312.png>)

![image 313](<2013-balogh-typical-structure-sparse-free_images/imageFile313.png>)

provided that δ is suﬃciently small. Now, we recall from the deﬁnition of T H, see (32) and (33), that since T(G) ∈ T H and we have x = |X(T(G))| and t∗ = e(T(G) − X(T(G))), then

nlog m

εξ 6 ·

m · (t∗ + xD/2). (71) Hence, if c2hlog n < n, then by Lemma 7.2,

h = |H(T(G))| >

![image 314](<2013-balogh-typical-structure-sparse-free_images/imageFile314.png>)

![image 315](<2013-balogh-typical-structure-sparse-free_images/imageFile315.png>)

e(Π) m e1/ξ · exp

2 ξ − c2clog n ·

m(b + h) n

F2(t,t∗,x,h) e1/ξ · mt∗+xD/2 · exp

![image 316](<2013-balogh-typical-structure-sparse-free_images/imageFile316.png>)

![image 317](<2013-balogh-typical-structure-sparse-free_images/imageFile317.png>)

4 ξ

e(Π) m

mh n ·

6 εξ − c2clog n ·

2m n ·

exp −

+

![image 318](<2013-balogh-typical-structure-sparse-free_images/imageFile318.png>)

![image 319](<2013-balogh-typical-structure-sparse-free_images/imageFile319.png>)

![image 320](<2013-balogh-typical-structure-sparse-free_images/imageFile320.png>)

![image 321](<2013-balogh-typical-structure-sparse-free_images/imageFile321.png>)

e(Π) m

,

where in the second inequality, we used (71) and the fact that b h, and in the last inequality, we used the facts that h 1, which follows from (71) as h is an integer, and that n is suﬃciently large. It follows that

cm 4

|F2R| m2n2 · max exp −

![image 322](<2013-balogh-typical-structure-sparse-free_images/imageFile322.png>)

2m n ·

,exp −

![image 323](<2013-balogh-typical-structure-sparse-free_images/imageFile323.png>)

e(Π) m

- m

![image 324](<2013-balogh-typical-structure-sparse-free_images/imageFile324.png>)

- n ·


exp −

e(Π) m

,

provided that n is suﬃciently large. This completes the proof in the regular case.

- 7.9. The irregular case. In this section, we prove Lemma 7.8. In other words, we count those


graphs in FH for which the hypergraph H′ of forbidden copies of Kr deﬁned in Section 7.7 contains fewer than σnr edges and does not contain any subhypergraph H that satisﬁes (58) and (59). This is the core of the proof of Theorem 6.3, which makes this section the key section of the paper.

We will describe a procedure that, given a G ∈ FH \ F1R, constructs some canonical hypergraph

- H ⊆ H′ by examining the vertices in H′(T(G)) and their neighborhoods one by one. By not adding certain r-tuples of H′ to the constructed hypergraph, our procedure forces H to satisfy


the maximum degree constraints given in (59). For a vast majority of graphs G ∈ FH \ F1R, the hypergraph H will have many edges (i.e., it will satisfy (58)), implying that G ∈ F2R. The procedure fails to output a hypergraph with many edges only when the intersections of the neighborhoods of diﬀerent vertices in H′(T(G)) are very far from random-like. Using Lemma 3.6, we will obtain a bound on the number of graphs with such an atypical distribution of neighborhoods of the vertices in H′(T(G)). Since by deﬁnition, our procedure has to fail on every graph in FI, the obtained bound is also an upper bound on |FI|.

- Proof of Lemma 7.8. Fix some graph G ∈ FH \ F1R and recall the deﬁnitions of D∗, H′(T(G)), and Wj(v) from Section 7.7. Suppose that H′ = H′(T(G)) = {v1,... ,vb}, where v1 < ... < vb (we assume that the vertex set of G is labeled with {1,... ,n}). We now describe the aforementioned procedure which constructs a hypergraph H ⊆ H′.


Constructing H. Let H0 ⊆ V1 ×...×Vr be the empty hypergraph. For every ℓ = 1,... ,b, do the following:

- (1) For every j ∈ [r], let Wj = Wj(vℓ).
- (2) For every I ⊆ [r] with 2 |I| r − 1, let

MI =   

T ∈

j∈I

Vj : degHℓ−1(T) >

C2 2 ·

![image 325](<2013-balogh-typical-structure-sparse-free_images/imageFile325.png>)

e(Hℓ−1) n|I|

![image 326](<2013-balogh-typical-structure-sparse-free_images/imageFile326.png>)

 

and let M[r] = Hℓ−1. 

- (3) Let


Hℓ = Hℓ−1 ∪ K ∈ W1 × ... × Wr : K T for all T ∈

MI .

I

Finally, let H = Hb. Since |Wj(v)| = D∗ for every j ∈ [r] and v ∈ H′, then for every s ∈ {2,... ,r − 1}, ∆s(H)

e(H) ns

e(H) ns

e(H) ns

C2 2 ·

+ (D∗)r−s max C2 ·

,2(D∗)r−s max C2 ·

,

![image 327](<2013-balogh-typical-structure-sparse-free_images/imageFile327.png>)

![image 328](<2013-balogh-typical-structure-sparse-free_images/imageFile328.png>)

![image 329](<2013-balogh-typical-structure-sparse-free_images/imageFile329.png>)

![image 330](<2013-balogh-typical-structure-sparse-free_images/imageFile330.png>)

- m

![image 331](<2013-balogh-typical-structure-sparse-free_images/imageFile331.png>)

- n


r−s

,

that is, H satisﬁes (59). Recall from (54) that λ = 2−r−1. We say that the vertex vℓ is useful if in the ℓth iteration of the above algorithm, we have

MI ∩

Wj λ(D∗)|I| for all I with 2 |I| r.

j∈I

Note that if vℓ is useful, then e(Hℓ) − e(Hℓ−1) (D∗)r −

(D∗)r 2

λ(D∗)|I| · (D∗)r−|I| = (1 − 2rλ)(D∗)r =

.

![image 332](<2013-balogh-typical-structure-sparse-free_images/imageFile332.png>)

I⊆[r]

Therefore, if at least half of the vertices of H′ are useful, then (recall the deﬁnitions of D∗ and c2 from (51) and (57))

e(H)

(D∗)r 2

b 2 ·

![image 333](<2013-balogh-typical-structure-sparse-free_images/imageFile333.png>)

![image 334](<2013-balogh-typical-structure-sparse-free_images/imageFile334.png>)

h(D∗)r 8r

βrh 2r+3r ·

=

![image 335](<2013-balogh-typical-structure-sparse-free_images/imageFile335.png>)

![image 336](<2013-balogh-typical-structure-sparse-free_images/imageFile336.png>)

- m

![image 337](<2013-balogh-typical-structure-sparse-free_images/imageFile337.png>)

- n


r

= c2h

- m

![image 338](<2013-balogh-typical-structure-sparse-free_images/imageFile338.png>)

- n


r

,

that is, H satisﬁes (58). Hence, if for some G ∈ FH \ F1R, the above procedure encounters at least b/2 useful vertices, then G ∈ F2R. This implies that for every graph G ∈ FI, the above procedure encounters fewer than b/2 useful vertices. We now enumerate all graphs with this property.

As before, we ﬁrst ﬁx h and t and consider only graphs G with t = e(T(G)) and h = |H(T(G))|. We then choose the b vertices that form the set H′ and specify in advance which (at least b/2) of

- them our procedure will mark as not useful. Next, we choose the sets W1(v),... ,Wr(v) in turn for every v ∈ H′, from the one with the smallest label to the one with the largest label (as in the procedure constructing H). The main point is that for the vertices v that are not useful, we choose


the sets Wi(v) in such a way that our procedure will deem them not useful and this severely limits the number of choices for these sets. This is the only stage of the enumeration where we provide a nontrivial upper bound. Finally, we choose the remaining t′ = t − bD∗ edges of T(G) and the remaining m − t′ − brD∗ edges of G ∩ Π.

Let us elaborate on the only non-trivial stage of the enumeration described above. We choose the sets W1(v),... ,Wr(v) for vertices v ∈ H′ one by one, following the same order as in the procedure constructing H. More precisely, suppose that H′ = {v1,... ,vb}, where v1 < ... < vb, ﬁx some ℓ ∈ [b], and assume that Wj(vk) have already been chosen for all j ∈ [r] and k ∈ [ℓ − 1]. This means, in particular, that the hypergraph Hℓ−1 and the sets MI in the ℓth iteration of our procedure are already determined for all I ⊆ [r]. Clearly, there are at most rD n∗ ways to choose

- W1(vℓ) ⊆ V1,... ,Wr(vℓ) ⊆ Vr if vℓ is useful, see (67). Let us now estimate the number of ways to choose these sets in such a way that vℓ will not be useful, that is, letting Wj = Wj(vℓ), so that


Wj| > λd|I| for some I ⊆ [r] with 2 |I| r. (72)

|MI ∩

j∈I

Recall that Π ∈ Pn,r(γ) and hence |Vj| 2 nr. It follows from the deﬁnition of MI that for every

![image 339](<2013-balogh-typical-structure-sparse-free_images/imageFile339.png>)

- I ⊆ [r] with 2 |I| r − 1, we have


2|I|+1r|I| C2 ·

(2r)r C2 ·

2n|I| C2

|Vj|

|Vj| = τ ·

|Vj|, (73)

|MI| <

![image 340](<2013-balogh-typical-structure-sparse-free_images/imageFile340.png>)

![image 341](<2013-balogh-typical-structure-sparse-free_images/imageFile341.png>)

![image 342](<2013-balogh-typical-structure-sparse-free_images/imageFile342.png>)

j∈I

j∈I

j∈I

where the last inequality follows from (56). Since G ∈/ F1R, we also have

r

|M[r]| = e(Hℓ−1) e(H′) < σnr σ · (2r)r ·

|Vj| τ ·

j=1

r

|Vj|. (74)

j=1

Recalling the deﬁnition of λ from (54), inequalities (73) and (74) together with Lemma 3.6 imply that the number Z2 of ways to choose W1(vℓ),... ,Wr(vℓ) so that vℓ is not useful, and therefore (72) holds, satisﬁes

Z2

αD∗

j∈I

I⊆[r]

|Vj| D∗ ·

j ∈I

exp(−6C1D∗) ·

n rD∗

,

|Vj| D∗

2rαD∗ ·

|V1| + ... + |Vr| r · D∗

where the last inequality follows from (54), provided that D∗ r, which holds when n is suﬃciently large.

Summarizing the above discussion, similarly as in the proof of Lemma 7.7, we have |FI|

b

e(Π) m − t′ − rbD∗

n b · 2b · exp(−6C1D∗)b/2 ·

n rD∗

· |Tt′(t∗,x,h)| ·

. (75)

t,t∗,x,h

- Let F3(t,t∗,x,h) denote the term in the sum in the right hand side of (75). Recall that we are counting only graphs G ∈ FH and therefore we may assume that (71) holds; a graph G ∈ FH will


be counted by F3(t,t∗,x,h), where t = e(T(G)), t∗ = e(T(G) − X(T(G))), x = |X(T(G))|, and h = |H(T(G))|. It follows from Lemma 7.2, see (68), that

e(Π) m

4mh ξn · exp(−3C1D∗b) ·

|F3(t,t∗,x,h)| e1/ξ · 2b · mt∗+xD/2 · exp

. It follows from (71) that

![image 343](<2013-balogh-typical-structure-sparse-free_images/imageFile343.png>)

mh n ·

6 εξ

mt∗+xD/2 exp

,

![image 344](<2013-balogh-typical-structure-sparse-free_images/imageFile344.png>)

![image 345](<2013-balogh-typical-structure-sparse-free_images/imageFile345.png>)

which, recalling that b 2 hr and the deﬁnition of D∗ from (51), yields |F3(t,t∗,x,h)| e1/ξ · 2h · exp

![image 346](<2013-balogh-typical-structure-sparse-free_images/imageFile346.png>)

mh n ·

6 εξ

4 ξ −

3βC1 2r ·

e(Π) m e1/ξ · 2h · exp −

+

![image 347](<2013-balogh-typical-structure-sparse-free_images/imageFile347.png>)

![image 348](<2013-balogh-typical-structure-sparse-free_images/imageFile348.png>)

![image 349](<2013-balogh-typical-structure-sparse-free_images/imageFile349.png>)

![image 350](<2013-balogh-typical-structure-sparse-free_images/imageFile350.png>)

e(Π) m

e(Π) m

2m n ·

3mh n ·

exp −

,

![image 351](<2013-balogh-typical-structure-sparse-free_images/imageFile351.png>)

![image 352](<2013-balogh-typical-structure-sparse-free_images/imageFile352.png>)

where in the ﬁrst inequality we used (53) and in the last inequality, we used the fact that h 1, which follows from (71) as h is an integer, and that n is suﬃciently large. It follows that

e(Π) m

e(Π) m

- m

![image 353](<2013-balogh-typical-structure-sparse-free_images/imageFile353.png>)

- n ·


2m n ·

|FI| m2n2 · exp −

exp −

. This completes the proof in the irregular case.

![image 354](<2013-balogh-typical-structure-sparse-free_images/imageFile354.png>)

8. The dense case (m > e(Π) − ξn2)

Recall the deﬁnition of ξ given in (25). In this section, we prove Theorem 6.3 in the (easy) case m > e(Π) − ξn2. We begin with a brief sketch of the argument.

- 8.1. Outline of the proof. Recall the deﬁnition of T from Section 6.3. Our proof in the dense case has two main ingredients. In Section 8.4, in Lemma 8.4, we give an upper bound on |F∗(T)|, the number of G ∈ F∗ with T(G) = T, in terms of the size of a maximum matching in T. In Section 8.3, in Lemma 8.1, we enumerate graphs T ∈ T with a particular value of this parameter. Combining these two estimates yields the required upper bound on |F∗|.


The bound on the size of F∗(T) is obtained as follows. First, we note that the family F∗(T) is empty unless all vertices of T have degree at most βn, where β is some small positive constant. This is because by Claim 6.2, in every G ∈ F∗(T) the neighborhood of such a vertex would contain a large Kr-free graph, which, by Lemma 3.3, would contradict the assumption that e(G ∩ Π) (1 − δ)m > (1 − δ)(e(Π) − ξn2). Second, we observe that in every G ∈ F∗(T) the endpoints of every edge of T cannot have many common neighbors in every other (than its own) color class. This is because the set of common neighbors of such an edge induces a Kr−1-free graph and hence, by Lemma 3.3 and our assumption that e(G ∩ Π) (1 − δ)(e(Π) − ξn2), it cannot be very large. It follows that there are some i and j such that the density of edges between the vertex set of a

maximal matching in T[Vi] and Vj is bounded away from 1. Since by our assumption on m, e(G(Π)) is very close to e(Π), this restriction is suﬃciently strong to bound the number of choices for G∩Π.

- 8.2. Setup. For every T ∈ T , we ﬁx some canonically chosen maximal matching U(T) in T and let

X(T) be the set of endpoints of edges in U(T). It follows from the maximality of U(T) that every edge in T has at least one endpoint in X(T). Next, for every i ∈ [r], we let Ui(T) be the subgraph of U(T) induced by Vi, let Xi(T) = X(T) ∩ Vi, and let i(T) be the smallest index satisfying

|Xi(T)(T)| = max i∈[r]

|Xi(T)|

|X(T)| r

![image 355](<2013-balogh-typical-structure-sparse-free_images/imageFile355.png>)

. Let

β =

1 40r3

![image 356](<2013-balogh-typical-structure-sparse-free_images/imageFile356.png>)

.

In the argument below, we will use the following inequality, which is a trivial consequence of our choices of ξ and δ:

ξ + δ < min β2,

1 16r2

![image 357](<2013-balogh-typical-structure-sparse-free_images/imageFile357.png>)

. (76)

- 8.3. Counting the graphs in T . Let us partition the family T according to the size of the set

X(T). For an integer x, let T (x) consist of all T ∈ T that satisfy |X(T)| = x. We will use the following trivial upper bound on |T (x)|.

- Lemma 8.1. If n is suﬃciently large, then for every x, |T (x)| enx.

Proof. We may construct each T ∈ T (x) by selecting x vertices that form the set X(T) and, for each of those vertices, choosing which pairs of vertices intersecting X(T) are edges of T. It follows that

|T (x)|

n x

2(x2)+x(n−x) ex(logn+nlog 2) enx, provided that n is suﬃciently large.

8.4. Bounding |F∗(T)| in terms of |X(T)|. We ﬁrst deal with the case when T contains a vertex with large degree. To this end, let T H be the family of all T ∈ T that contain a vertex of degree at least βn and let T L = T \ T H. With our choice of parameters, estimating |F∗(T)| for T ∈ T H is extremely easy.

- Lemma 8.2. For every T ∈ T H, the family F∗(T) is empty.

Proof. Fix a T ∈ T H and let v be an arbitrary vertex with degT(v) βn. Suppose that F∗(T) is non-empty and ﬁx an arbitrary G ∈ F∗(T). By Claim 6.2 and the deﬁnition of T H, degG(v,Vi) βn for every i ∈ [r]. The (r-partite) subgraph of G ∩ Π induced by NG(v) is Kr-free and so by

- Lemma 3.3, e(Π \ G) min degG(v,Vi) · degG(v,Vj): i,j ∈ [r] β2n2.




On the other hand, by (76), e(Π \ G) = e(Π) − e(G) + e(T) e(Π) − m + δm ξn2 + δ

n 2

< β2n2, (77) a contradiction.

The following lemma is the key step in our proof. It says that for every G ∈ F∗(T), there is a

fairly large set X′ ⊆ Vi(T) such that the density of edges between X′ and some Vj with j = i(T) is at most 3/4, much lower than the average density of G∩Π, which by our assumptions is 1−O(ξ +δ).

- Lemma 8.3. For every T ∈ T and every G ∈ F∗(T), there is a set X′ ⊆ Xi(T) and a j = i(T) such that

|X′|

|Xi(T)(T)| r − 1

![image 358](<2013-balogh-typical-structure-sparse-free_images/imageFile358.png>)

and eG(X′,Vj)

- 3

![image 359](<2013-balogh-typical-structure-sparse-free_images/imageFile359.png>)

- 4|X′| · |Vj|.


Proof. Fix some T ∈ T and G ∈ F∗(T) and let i = i(T). For every edge {u,v} ∈ Ui(T) and every j = i, let Wjuv be the set of common neighbors of u and v in Vj. Suppose ﬁrst that for every {u,v}, there is a j = i such that |Wjuv| |Vj|/2, which implies that

eG({u,v},Vj) |Vj| + |Wjuv|

3 2|Vj|. (78) Let j be an index for which (78) holds for the largest number of edges {u,v} ∈ Ui(T) and let X′ ⊆ Xi(T) be the set of endpoints of these edges. This set X′ clearly satisﬁes the assertion of this lemma. Suppose now that there is a {u,v} ∈ Ui(T) such that |Wjuv| > |Vj|/2 for all j = i. Since G is Kr+1-free, the (r − 1)-partite subgraph of G ∩ Π induced by the sets Wjuv with j = i contains no copy of Kr−1. In other words, this subgraph of G ∩ Π is a Kr−1-free subgraph of the complete (r − 1)-partite graph with color classes Wjuv, where j = i. It follows from Lemma 3.3 that the graph Π \ G contains at least minj1 =j2 |Wjuv

![image 360](<2013-balogh-typical-structure-sparse-free_images/imageFile360.png>)

1

||Wjuv

2

| edges. This clearly cannot happen as

min

j1 =j2

|Wjuv1 ||Wjuv2 | min

j

|Vj|2 4

![image 361](<2013-balogh-typical-structure-sparse-free_images/imageFile361.png>)

n2 16r2 but, on the other hand, by (76) and (77),

![image 362](<2013-balogh-typical-structure-sparse-free_images/imageFile362.png>)

e(Π \ G) ξn2 + δ

n 2

<

n2 16r2

![image 363](<2013-balogh-typical-structure-sparse-free_images/imageFile363.png>)

, a contradiction.

Finally, we use Lemma 8.3 to derive an upper bound on |F∗(T)| for all T ∈ T L(x).

- Lemma 8.4. If n is suﬃciently large, then for every x and every T ∈ T L(x),


e(Π) m

|F∗(T)| e−2nx ·

.

Proof. By Lemma 8.3, we may construct each G ∈ F∗(T) by selecting a set X′ ⊆ Xi(T) of ⌈x/r2⌉ vertices, an index j = i(T), then choosing some m′, where m′ 4 3|X′||Vj|, edges between X′ and Vj, and ﬁnally choosing the remaining m−m′−e(T) edges from Π\(X′,Vj), where (X′,Vj) denotes the complete bipartite graph with color classes X′ and Vj. The reason why |F∗(T)| is so small is that the number Nj of ways to ﬁrst choose only at most 43|X′||Vj| edges between X′ and Vj and

![image 364](<2013-balogh-typical-structure-sparse-free_images/imageFile364.png>)

![image 365](<2013-balogh-typical-structure-sparse-free_images/imageFile365.png>)

- then the remaining edges from Π \ (X′,Vj) is much smaller than the number of ways to choose m − e(T) edges from Π. To quantify this, let t = e(T), let x′ = ⌈x/r2⌉, ﬁx some j = i(T), and let nj = |Vj|. Observe that t βnx due to our assumption that T ∈ T L(x) and therefore,


e(Π) − x′nj m − 34x′nj − βnx

e(Π) − x′nj m − 54x′nj

e(Π) − x′nj m − m′ − t

x′nj m′

2x′nj ·

2xn ·

, (79)

Nj

![image 366](<2013-balogh-typical-structure-sparse-free_images/imageFile366.png>)

![image 367](<2013-balogh-typical-structure-sparse-free_images/imageFile367.png>)

m′ 34x′nj

![image 368](<2013-balogh-typical-structure-sparse-free_images/imageFile368.png>)

where the last two inequalities hold since for each m′ with m′ 34x′nj,

![image 369](<2013-balogh-typical-structure-sparse-free_images/imageFile369.png>)

e(Π) − x′nj 2

- 4

![image 370](<2013-balogh-typical-structure-sparse-free_images/imageFile370.png>)

- 5


3 4

x′nj − βnx m − m′ − t. (80) To see the ﬁrst inequality in (80), recall that m e(Π) − ξn2 and observe that

x′nj m −

m −

![image 371](<2013-balogh-typical-structure-sparse-free_images/imageFile371.png>)

![image 372](<2013-balogh-typical-structure-sparse-free_images/imageFile372.png>)

x′nj |Vi(T)| 2 · |Vj|

e(Π) 2

. (81)

![image 373](<2013-balogh-typical-structure-sparse-free_images/imageFile373.png>)

![image 374](<2013-balogh-typical-structure-sparse-free_images/imageFile374.png>)

To see the second inequality in (80), recall that x′ x/r2, nj n/2r, and therefore βnx 2βr3x′nj = x′nj/20. With the view of further estimating Nj, we claim that for every j ∈ [r],

e(Π) − x′nj m − 54x′nj

e(Π) m

e−3xn ·

. (82)

![image 375](<2013-balogh-typical-structure-sparse-free_images/imageFile375.png>)

Assuming that (82) holds, (79) implies that

|F∗(T)|

j =i(T)

|Vj| x′ · Nj r · nx · 2xn · e−3xn ·

e(Π) m

e−2xn ·

e(Π) m

,

provided that n is suﬃciently large, as required. Thus, it remains to establish (82). To this end, using the trivial identity

- a − 5
- b − 4


b(b − 1)(b − 2)(b − 3)(a − b) a(a − 1)(a − 2)(a − 3)(a − 4) ·

a b

=

![image 376](<2013-balogh-typical-structure-sparse-free_images/imageFile376.png>)

and the assumption that m e(Π) − ξn2, we estimate

x′nj

x′nj 5

e(Π)−x′nj

x′nj/5

e(Π)−5z m−4z e(Π)−5z+5 m−4z+4

5 e(Π)4 · ξn2 (e(Π)/2)5

m4(e(Π) − m) (e(Π) − x′nj)5

![image 377](<2013-balogh-typical-structure-sparse-free_images/imageFile377.png>)

![image 378](<2013-balogh-typical-structure-sparse-free_images/imageFile378.png>)

m−54x′nj e(Π) m

![image 379](<2013-balogh-typical-structure-sparse-free_images/imageFile379.png>)

=

![image 380](<2013-balogh-typical-structure-sparse-free_images/imageFile380.png>)

![image 381](<2013-balogh-typical-structure-sparse-free_images/imageFile381.png>)

![image 382](<2013-balogh-typical-structure-sparse-free_images/imageFile382.png>)

![image 383](<2013-balogh-typical-structure-sparse-free_images/imageFile383.png>)

z=1

x′nj

xn

(25 · 16/3 · ξ)

5 (29ξ/3)

10r3 e−3xn,

![image 384](<2013-balogh-typical-structure-sparse-free_images/imageFile384.png>)

![image 385](<2013-balogh-typical-structure-sparse-free_images/imageFile385.png>)

where we used (25), (81), and the fact that e(Π) 3n2/16, see (28). This completes the proof of the lemma.

- 8.5. Summary. With Lemmas 8.1, 8.2, and 8.4 at our disposal, we can ﬁnally deduce an upper bound on |F∗|:


|F∗| =

|F∗(T)| =

|F∗(T)| =

|F∗(T)|

x 1 T∈T L(x)

T∈T

T∈T L

|T (x)| · e−2nx ·

x 1

e(Π) m x 1

e−nx ·

e(Π) m

2e−n ·

e(Π) m

.

This completes the proof of Theorem 6.3 in the dense case.

Appendix A. Omitted proofs

- A.1. Tools. In this section, we prove Lemmas 3.1–3.3. In the proofs of the ﬁrst two of them, we will use the so-called Local LYMB Inequality.


- Lemma A.1 (Local LYMB Inequality). Let H be a k-uniform hypergraph on a ﬁnite vertex set V . The shadow of H is the (k − 1)-uniform hypergraph ∂H deﬁned by


V k − 1

∂H = A ∈

: A ⊆ B for some B ∈ H . We have

e(H)

e(∂H)

.

![image 386](<2013-balogh-typical-structure-sparse-free_images/imageFile386.png>)

![image 387](<2013-balogh-typical-structure-sparse-free_images/imageFile387.png>)

|V | k−1

|V | k

- Proof of Lemma 3.1. For a set J ⊆ I, deﬁne

µ(J) =

i∈J

p|Bi| and ∆(J) =

i∼j

p|Bi∪Bj|,

where the second sum is over all ordered pairs (i,j) ∈ J2 such that i = j and Bi ∩ Bj = ∅. Let Iq ⊆ I be the q-random subset of I, that is, the random subset of I where each element of I is included with probability q, independently of all other elements, and ﬁx an arbitrary set J ⊆ I that satisﬁes

µ(J) − ∆(J)/2 E µ(Iq) − ∆(Iq)/2 = qµ − q2∆/2.

Let R′ be the p-random subset of Ω and let B′ denote the event that Bi R′ for all i ∈ I; one may think of R′ and B′ as ‘binomial’ analogues of R and B. By the Janson Inequality (see, e.g., [4, Theorem 8.1.1]),

P(B′) P(Bi R′ for all i ∈ J) exp (−µ(J) + ∆(J)/2) exp −qµ + q2∆/2 . (83)

It follows from the Local LYMB Inequality (Lemma A.1) that the function k  → P(B′ | |R′| = k) is decreasing and hence

P(B′) =

n

k=0

P(B′ | |R′| = k) · P(|R′| = k) P(B′ | |R′| = m) · P(|R′| m)

= P(B) · P(|R′| m) P(B)/2,

(84)

where the last inequality follows from the well-known fact that if np is an integer, then it is the median of the binomial distribution Bin(n,p). Inequalities (83) and (84) readily imply the claimed bound on P(B).

- Proof of Lemma 3.2. Set p = (1 + η)m/n and note that p 1 by our assumptions on m and η.


Let R′ be the p-random subset of Ω and let B′ denote the event that Bi R′ for all i ∈ I. By the FKG Inequality (see, e.g., [4, Chapter 6]),

P(B′)

i∈I

1 − p|Bi| . (85)

It follows from the Local LYMB Inequality (Lemma A.1) that the function k  → P(B′ | |R′| = k) is decreasing and hence

n

P(B′) =

P(B′ | |R′| = k) · P(|R′| = k) P(B′ | |R′| = m) + P(|R′| < m)

k=0

= P(B) + P(|R′| < m).

(86)

The claimed bound now easily follows from (85) and (86) as by Chernoﬀ’s Inequality (see, e.g., [4, Appendix A]),

η2m2 2(1 + η)m

η2m 4

P(|R′| < m) exp −

exp −

.

![image 388](<2013-balogh-typical-structure-sparse-free_images/imageFile388.png>)

![image 389](<2013-balogh-typical-structure-sparse-free_images/imageFile389.png>)

- Proof of Lemma 3.3. Let us denote the graph K(n1,... ,nr) by G. Let V1,... ,Vr be the color classes of G with n1,... ,nr elements, respectively. Clearly, deleting all edges between V1 and V2 removes all copies of Kr from G and hence ex(G,Kr) e(G) − n1n2. We prove the converse inequality by induction on r. The statement is trivial if r = 2, so let us assume that r 3. Let H be a Kr-free subgraph of G. Let ∆ = maxv∈Vr degH(v) and ﬁx an arbitrary v ∈ Vr with degH(v) = ∆. For each i ∈ [r −1], let di = degH(v,Vi). Since the subgraph of G induced by NH(v) is a Kr−1-free subgraph of K(d1,... ,dr−1), it follows from our inductive assumption that


e(G) − e(H) eG\H(V1 ∪ ... ∪ Vr−1,Vr) + eG\H(NH(v)) nr ·

r−1

nk − ∆ + min

didj.

i<j

k=1

Let {i,j}, where i < j, be a pair of indices for which didj attains its minimum value. Since d1 + ... + dr−1 = ∆ by our choice of v, then

r−1

e(G) − e(H) nr ·

(nk − dk) + didj nr · [(ni − di) + (nj − dj)] + didj

k=1

nj · [(ni − di) + (nj − dj)] + didj = ninj + (nj − dj)(nj − di) ninj n1n2, as claimed. It is not hard to verify that e(G) − e(H) > n1n2 unless H = G \ (Vi,Vj), where i and

- j are such that ninj = n1n2.


- A.2. Main tool. Lemma 3.6 is a straightforward consequence of the following somewhat technical (but tailored to facilitate an inductive proof) statement.


- Lemma A.2. Let α,λ ∈ (0,1), let V1,... ,Vk be ﬁnite sets, and let d be an integer satisfying 2 d min{|V1|,... ,|Vk|}. Suppose that H ⊆ V1 × ... × Vk satisﬁes

|H| (αλ)k

k

i=1

|Vi|.

Then for all but at most

dk − 1 2αλ d

k

i=1

|Vi| d choices of W1 ∈ Vd1 ,... ,Wk ∈ Vdk , we have

|H ∩ (W1 × ... × Wk)| kλdk. (87)

We will deduce this statement from the following one-sided version of Hoeﬀding’s inequality [26] for the hypergeometric distribution.

- Lemma A.3. Let d and n be integers and let X denote the uniformly chosen random d-subset of [n]. Then for every α,λ ∈ (0,1),


P X ∩ [αλn] λd 2αλ d. (88)

Proof. Denote the left-hand side of (88) by P. It follows from Hoeﬀding’s inequality [26, Theorem 1] that1

λ 1 − αλ 1 − λ

1−λ

1−λ

1 1 − λ

αλ λ

αλ

αλe1/e 2αλ,

P1/d

![image 390](<2013-balogh-typical-structure-sparse-free_images/imageFile390.png>)

![image 391](<2013-balogh-typical-structure-sparse-free_images/imageFile391.png>)

![image 392](<2013-balogh-typical-structure-sparse-free_images/imageFile392.png>)

where the third inequality follows from the fact that if a > 0, then the function x  → (a/x)x attains its maximum value at x = a/e.

Proof of Lemma A.2. We prove the statement by induction on k. The induction base (k = 1) follows directly from Lemma A.3 and the fact that d − 1 1. For the induction step, assume that

- k 2. For every v ∈ Vk, let Hv = {(v1,... ,vk−1) ∈ V1 × ... × Vk−1: (v1,... ,vk−1,v) ∈ H}.


One may think of Hv as the link hypergraph of the vertex v. Roughly speaking, we shall argue as follows. If W1 × ... × Wk contains many edges of H, then either

- (i) the set Wk contains many vertices whose degree in H is high or
- (ii) for some v ∈ Wk whose degree in H is low, the set W1 × ... × Wk−1 has a large intersection with the link hypergraph Hv.


The desired bound will then follow by applying Lemma A.3 (when (i) holds) and the induction hypothesis (when (ii) holds). The details now follow.

Let

k−1

Vk′ = v ∈ Vk : |Hv| > (αλ)k−1

|Vi| .

i=1

Intuitively, Vk′ is the set of all v ∈ Vk whose degree in H exceeds the assumed upper bound on the average degree of Vk in H by a factor of more than (αλ)−1. Note that our assumption on H implies that |Vk′| < αλ|Vk|. Furthermore, let

Vk d

: |W ∩ Vk′| λd

Wk = W ∈

and for each W ∈ Vdk \ Wk, deﬁne WW ⊆ Vd1 × ... × Vkd−1 by WW = (W1,... ,Wk−1): |Hv ∩ W1 × ... × Wk−1| (k − 1)λdk−1 for some v ∈ W \ Vk′ . Note that if W1 ∈ Vd1 ,... ,Wk ∈ Vdk are such that Wk  ∈ Wk and (W1,... ,Wk−1)  ∈ WWk, then |H ∩ W1 × ... × Wk| λd · dk−1 + d · (k − 1)λdk−1 kλdk. Hence, the number B of k-tuples (W1,... ,Wk) for which (87) does not hold satisﬁes

By Lemma A.3,

k−1

B |Wk| ·

i=1

|Vi| d

|WW|. (89)

+

W ∈Wk

|Wk| 2αλ)d |Vk| d

(90)

![image 393](<2013-balogh-typical-structure-sparse-free_images/imageFile393.png>)

1Even though [26, Theorem 1] applies to sums of independent random variables, the bound obtained there remains valid for the hypergeometric distribution, see the discussion in [26, Section 6].

and, since

k−1

|Hv| (αλ)k−1

|Vi|

i=1

for every v  ∈ Vk′, then by our inductive assumption, for every W  ∈ Wk,

k−1

k−1

|Vi| d

dk−1 − 1 2αλ d

dk − d 2αλ d

|WW|

v∈W\Vk′

i=1

i=1

Putting (89), (90), and (91) together yields

|Vi| d

. (91)

as claimed.

k

B 1 + dk − d 2αλ)d

i=1

|Vi| d

k

dk − 1 2αλ d

i=1

|Vi| d

,

- A.3. Non-uniquely colorable and unbalanced graphs. Finally, we present the proofs of Propositions 4.1 and 5.5.


- Proof of Proposition 4.1. Fix an arbitrary partition Π that does not satisfy (7) and observe that (see (18))

e(Π) ex(n,Kr+1) −

γ2n2 2

![image 394](<2013-balogh-typical-structure-sparse-free_images/imageFile394.png>)

. Consequently, by Lemma 3.5, we have that

|Gm(Π)| =

e(Π) m

ex(n,Kr+1) − γ22n2 ex(n,Kr+1)

![image 395](<2013-balogh-typical-structure-sparse-free_images/imageFile395.png>)

![image 396](<2013-balogh-typical-structure-sparse-free_images/imageFile396.png>)

m

·

ex(n,Kr+1) m

e−γ2m ·

ex(n,Kr+1) m

.

To complete the proof, we just observe that there are at most rn diﬀerent r-colorings and that rn eγ2m/2 if m cn for a suﬃciently large constant c.

- Proof of Proposition 5.5. Fix some Π ∈ Pn,r(21r) and Π′ ∈ Pn,r\{Π}. Suppose that Π = {V1,... ,Vr} and Π′ = {V1′,... ,Vr′} and for all i,j ∈ [r], let Vi,j = Vi ∩ Vj′. We will say that the vertices in Vi,j are moved from Vi to Vj′. For every i ∈ [r], deﬁne Li and Si as the largest and the second largest


![image 397](<2013-balogh-typical-structure-sparse-free_images/imageFile397.png>)

subclasses of Vi, respectively. Note that |Vi| 2 nr implies that |Li| 2 nr2. Set s = maxj∈[r] |Sj| and let S = Sj for the smallest j for which the maximum in the deﬁnition of s is achieved. Note that

![image 398](<2013-balogh-typical-structure-sparse-free_images/imageFile398.png>)

![image 399](<2013-balogh-typical-structure-sparse-free_images/imageFile399.png>)

1 s n/2, as s = 0 would imply that (V1,... ,Vr) is a permutation of (V1′,... ,Vr′), and therefore Π = Π′.

Observe that, by the pigeonhole principle, either some pair {Li,Lj} of largest subclasses, or some largest subclass Li and S, where S Vi, are moved to the same vertex class Vk′. Since Vk′ is an independent set in every G ∈ Gm(Π′), it follows that every G ∈ Gm(Π) ∩ Gm(Π′) has no edges between these sets Li and Lj or Li and S. Since,

min{|Li| · |Lj|,|Li| · |S|} ·min

n 2r2

![image 400](<2013-balogh-typical-structure-sparse-free_images/imageFile400.png>)

2

,

n 2r2 · s

![image 401](<2013-balogh-typical-structure-sparse-free_images/imageFile401.png>)

sn 2r4

,

![image 402](<2013-balogh-typical-structure-sparse-free_images/imageFile402.png>)

it follows from Lemma 3.5 and the inequality e(Π) n2/2 that, if m r6(a + 3)nlog n,

|Gm(Π) ∩ Gm(Π′)|

e(Π) − 2snr4 m

![image 403](<2013-balogh-typical-structure-sparse-free_images/imageFile403.png>)

s nr4

1 −

![image 404](<2013-balogh-typical-structure-sparse-free_images/imageFile404.png>)

m e(Π) m

n−(a+3)sr2 · |Gm(Π)|. (92)

Finally, observe that given a Π, we can describe any Π′ = Π by ﬁrst picking the partitions (Vi,j)j∈[r] for every i and then setting Vj′ = i∈[r] Vi,j. A moment’s thought reveals that for every s, there are at most nr2 · nsr2 ways to choose all Vi,j so that maxi∈[r] |Si| = s. Therefore, by (92),

n(s+1)r2 · n−s(a+3)r2 · |Gm(Π)| n−a · |Gm(Π)|,

|Gm(Π) \ Um(Π)|

s 1

which completes the proof.

Acknowledgments. We would like to thank the anonymous referee for a careful reading of the paper and several valuable comments and suggestions. Lutz Warnke would like to thank Angelika Steger for numerous insightful discussions on the topic of this paper.

References

- 1. D. Achlioptas and E. Friedgut, A sharp threshold for k-colorability, Random Structures Algorithms 14 (1999), 63–70.
- 2. D. Achlioptas and A. Naor, The two possible values of the chromatic number of a random graph, Ann. of Math.

(2) 162 (2005), 1335–1351.

- 3. N. Alon, J. Balogh, B. Bollob´s, and R. Morris, The structure of almost all graphs in a hereditary property, J. Combin. Theory Ser. B 101 (2011), 85–110.
- 4. N. Alon and J. H. Spencer, The probabilistic method, third ed., Wiley-Interscience Series in Discrete Math. and Optimization, John Wiley & Sons Inc., Hoboken, NJ, 2008.
- 5. L. Babai, M. Simonovits, and J. Spencer, Extremal subgraphs of random graphs, J. Graph Theory 14 (1990), 599–622.
- 6. J. Balogh, B. Bollob´s, and M. Simonovits, The number of graphs without forbidden subgraphs, J. Combin. Theory Ser. B 91 (2004), 1–24.
- 7. , The typical structure of graphs without given excluded subgraphs, Random Structures Algorithms 34

![image 405](<2013-balogh-typical-structure-sparse-free_images/imageFile405.png>)

(2009), 305–318.

- 8. , The ﬁne structure of octahedron-free graphs, J. Combin. Theory Ser. B 101 (2011), 67–84.

![image 406](<2013-balogh-typical-structure-sparse-free_images/imageFile406.png>)

- 9. J. Balogh and J. Butterﬁeld, Excluding induced subgraphs: critical graphs, Random Structures Algorithms 38

(2011), 100–120.

- 10. J. Balogh, R. Morris, and W. Samotij, Independent sets in hypergraphs, to appear in J. Amer. Math. Soc.
- 11. J. Balogh and D. Mubayi, Almost all triple systems with independent neighborhoods are semi-bipartite, J. Combin. Theory Ser. A 118 (2011), 1494–1518.
- 12. , Almost all triangle-free triple systems are tripartite, Combinatorica 32 (2012), 143–169.

![image 407](<2013-balogh-typical-structure-sparse-free_images/imageFile407.png>)

- 13. B. Bollob´s, Random graphs, second ed., Cambridge Studies in Advanced Mathematics, vol. 73, Cambridge University Press, Cambridge, 2001.
- 14. G. Brightwell, K. Panagiotou, and A. Steger, Extremal subgraphs of random graphs, Random Structures Algorithms 41 (2012), 147–178.
- 15. A. Coja-Oghlan and D. Vilenchik, Chasing the k-colorability threshold, arXiv:1304.1063 [cs.DM].
- 16. D. Conlon and T. Gowers, Combinatorial theorems in sparse random sets, arXiv:1011.4310v1 [math.CO].
- 17. D. Conlon, W. T. Gowers, W. Samotij, and M. Schacht, On the K LR conjecture in random graphs, to appear in Israel J. Math.
- 18. B. DeMarco and J. Kahn, Mantel’s theorem for random graphs, to appear in Random Structures Algorithms.
- 19. , Tur´an’s theorem for random graphs, in preparation.

![image 408](<2013-balogh-typical-structure-sparse-free_images/imageFile408.png>)

- 20. P. Erd˝s, D. J. Kleitman, and B. L. Rothschild, Asymptotic enumeration of Kn-free graphs, Colloquio Internazionale sulle Teorie Combinatorie (Rome, 1973), Tomo II, Accad. Naz. Lincei, Rome, 1976, pp. 19–27. Atti dei Convegni Lincei, No. 17.
- 21. P. Erd˝s and A. Re´nyi, On the evolution of random graphs, Magyar Tud. Akad. Mat. Kutato´ Int. K¨zl. 5 (1960), 17–61.
- 22. P. Erd˝s and M. Simonovits, A limit theorem in graph theory, Studia Sci. Math. Hungar. 1 (1966), 51–57.
- 23. P. Frankl and V. Ro¨dl, Large triangle-free subgraphs in graphs without K4, Graphs Combin. 2 (1986), 135–144.


- 24. E. Friedgut, Sharp thresholds of graph properties, and the k-sat problem, J. Amer. Math. Soc. 12 (1999), 1017– 1054, With an appendix by Jean Bourgain.
- 25. E. Friedgut, V. Ro¨dl, and M. Schacht, Ramsey properties of random discrete structures, Random Structures Algorithms 37 (2010), 407–436.
- 26. W. Hoeﬀding, Probability inequalities for sums of bounded random variables, J. Amer. Statist. Assoc. 58 (1963), 13–30.
- 27. C. Hundack, H. J. Pro¨mel, and A. Steger, Extremal graph problems for graphs with a color-critical vertex, Combin. Probab. Comput. 2 (1993), 465–477.
- 28. S. Janson, T.  Luczak, and A. Rucinski, Random graphs, Wiley-Interscience Series in Discrete Mathematics and Optimization, Wiley-Interscience, New York, 2000.
- 29. Y. Kohayakawa, T.  Luczak, and V. Ro¨dl, Arithmetic progressions of length three in subsets of a random set, Acta Arith. 75 (1996), 133–163.
- 30. , On K4-free subgraphs of random graphs, Combinatorica 17 (1997), 173–213.

![image 409](<2013-balogh-typical-structure-sparse-free_images/imageFile409.png>)

- 31. P. Kolaitis, H. J. Pro¨mel, and B. Rothschild, Kl+1-free graphs: asymptotic structure and a 0 − 1 law, Trans. Amer. Math. Soc. 303 (1987), 637–671.
- 32. T.  Luczak, On triangle-free random graphs, Random Structures Algorithms 16 (2000), 260–276.
- 33. D. Osthus, H. J. Pro¨mel, and A. Taraz, For which densities are random triangle-free graphs almost surely bipartite?, Combinatorica 23 (2003), 105–150.
- 34. Y. Person and M. Schacht, Almost all hypergraphs without Fano planes are bipartite, Proceedings of the Twentieth Annual ACM-SIAM Symposium on Discrete Algorithms (Philadelphia, PA), SIAM, 2009, pp. 217–226.
- 35. H. J. Pro¨mel and A. Steger, The asymptotic number of graphs not containing a ﬁxed color-critical subgraph, Combinatorica 12 (1992), 463–473.
- 36. , Random l-colorable graphs, Random Structures Algorithms 6 (1995), 21–37.

![image 410](<2013-balogh-typical-structure-sparse-free_images/imageFile410.png>)

- 37. , On the asymptotic structure of sparse triangle free graphs, J. Graph Theory (1996), no. 2, 137–151.

![image 411](<2013-balogh-typical-structure-sparse-free_images/imageFile411.png>)

- 38. V. Ro¨dl and A. Rucin´ski, Threshold functions for Ramsey properties, J. Amer. Math. Soc. 8 (1995), 917–942.
- 39. , Rado partition theorem for random subsets of integers, Proc. London Math. Soc. (3) 74 (1997), 481–502.

![image 412](<2013-balogh-typical-structure-sparse-free_images/imageFile412.png>)

- 40. V. Ro¨dl and M. Schacht, Extremal results in random graphs, Erd¨s centennial, Bolyai Soc. Math. Stud., vol. 25, J´anos Bolyai Math. Soc., Budapest, 2013, pp. 535–583.
- 41. W. Samotij, Stability results for random discrete structures, Random Structures Algorithms 44 (2014), 269–289.
- 42. D. Saxton and A. Thomason, Hypergraph containers, arXiv:1204.6595v2 [math.CO].
- 43. M. Schacht, Extremal results for random discrete structures, submitted.
- 44. M. Simonovits, A method for solving extremal problems in graph theory, stability problems, Theory of Graphs (Proc. Colloq., Tihany, 1966), Academic Press, New York, 1968, pp. 279–319.
- 45. A. Steger, On the evolution of triangle-free graphs, Combin. Probab. Comput. 14 (2005), 211–224.
- 46. P. Tur´an, Eine Extremalaufgabe aus der Graphentheorie, Mat. Fiz. Lapok 48 (1941), 436–452.
- 47. L. Warnke, On the evolution of K4-free graphs, Master’s thesis, ETH Zu¨rich, 2009.


Department of Mathematics, University of Illinois, 1409 W. Green Street, Urbana, IL 61801; and

Mathematical Institute, University of Szeged, Szeged, Hungary E-mail address: jobal@math.uiuc.edu IMPA, Estrada Dona Castorina 110, Jardim Botanico,ˆ Rio de Janeiro, RJ, Brasil E-mail address: rob@impa.br School of Mathematical Sciences, Tel Aviv University, Tel Aviv 69978, Israel; and Trinity College,

Cambridge CB2 1TQ, UK E-mail address: samotij@post.tau.ac.il Department of Pure Mathematics and Mathematical Statistics, University of Cambridge, Wilber-

force Road, Cambridge CB3 0WB, UK E-mail address: L.Warnke@dpmms.cam.ac.uk

