arXiv:1211.3487v1[math.CO]15Nov2012

Graph removal lemmas

David Conlon∗ Jacob Fox†

Abstract

The graph removal lemma states that any graph on n vertices with o(nv(H)) copies of a ﬁxed graph H may be made H-free by removing o(n2) edges. Despite its innocent appearance, this lemma and its extensions have several important consequences in number theory, discrete geometry, graph theory and computer science. In this survey we discuss these lemmas, focusing in particular on recent improvements to their quantitative aspects.

# 1 Introduction

The triangle removal lemma states that for all ǫ > 0 there exists δ > 0 such that any graph on n vertices with at most δn3 triangles may be made triangle-free by removing at most ǫn2 edges. This result, proved by Ruzsa and Szemere´di [93] in 1976, was originally stated in rather diﬀerent language. The original formulation was in terms of the (6,3)-problem.1 This asks for the maximum number of edges f(3)(n,6,3) in a 3-uniform hypergraph on n vertices such that no 6 vertices contain 3 edges. Answering a question of Brown, Erd˝os and So´s [19], Ruzsa and Szemere´di showed that f(3)(n,6,3) =

- o(n2). Their proof used several iterations of an early version of Szemere´di’s regularity lemma [110].

This result, developed by Szemere´di in his proof of the Erd˝os-Tura´n conjecture on arithmetic progressions in dense sets [109], states that every graph may be partitioned into a small number of vertex sets so that the graph between almost every pair of vertex sets is random-like. Though this result now

- occupies a central position in graph theory, its importance only emerged over time. The resolution of the (6,3)-problem was one of the ﬁrst indications of its strength.


The Ruzsa-Szemere´di theorem was generalized by Erd˝os, Frankl and Ro¨dl [32], who showed that f(r)(n,3r − 3,3) = o(n2), where f(r)(n,3r − 3,3) is the maximum number of edges in an r-uniform hypergraph such that no 3r − 3 vertices contain 3 edges. One of the tools used by Erd˝os, Frankl and Ro¨dl in their proof was a striking result stating that if a graph on n vertices contains no copy of a graph H then it may be made Kr-free, where r = χ(H) is the chromatic number of H, by removing o(n2) edges. The proof of this result used the modern formulation of Szemere´di’s regularity lemma and is already very close, both in proof and statement, to the following generalization of the triangle

![image 1](<2012-conlon-graph-removal-lemmas_images/imageFile1.png>)

∗Mathematical Institute, Oxford OX1 3LB, United Kingdom. Email: david.conlon@maths.ox.ac.uk. Supported by a Royal Society University Research Fellowship.

†Department of Mathematics, MIT, Cambridge, MA 02139-4307. Email: fox@math.mit.edu. Supported by a Simons Fellowship and NSF Grant DMS-1069197.

- 1The two results are not exactly equivalent, though the triangle removal lemma may be proved by their method.


A weak form of the triangle removal lemma, already suﬃcient for proving Roth’s theorem, is equivalent to the RuzsaSzemere´di theorem. This weaker form states that any graph on n vertices in which every edge is contained in exactly one triangle has o(n2) edges. This is also equivalent to another attractive formulation, known as the induced matching theorem. This states that any graph on n vertices which is the union of at most n induced matchings has o(n2) edges.

removal lemma, known as the graph removal lemma.2 This was ﬁrst stated explicitly in the literature by Alon, Duke, Lefmann, Ro¨dl and Yuster [4] and by Fu¨redi [47] in 1994.3 Note that we use v(H) to denote the number of vertices in a graph (or hypergraph) H.

- Theorem 1.1 For any graph H and any ǫ > 0, there exists δ > 0 such that any graph on n vertices which contains at most δnv(H) copies of H may be made H-free by removing at most ǫn2 edges.

It was already observed by Ruzsa and Szemere´di that the (6,3)-problem (and, thereby, the triangle removal lemma) is related to Roth’s theorem on arithmetic progressions [91]. This theorem states that for any δ > 0 there exists an n0 such that if n ≥ n0 then any subset of the set [n] := {1,2,... ,n} of size at least δn contains an arithmetic progression of length 3. Letting r3(n) be the largest integer such that there exists a subset of the set {1,2,... ,n} of size r3(n) containing no arithmetic progression of length 3, this is equivalent to saying that r3(n) = o(n). Ruzsa and Szemere´di observed that f(3)(n,6,3) = Ω(r3(n)n). In particular, since f(3)(n,6,3) = o(n2), this implies that r3(n) = o(n), yielding a proof of Roth’s theorem.

It was further noted by Solymosi [104] that the Ruzsa-Szemere´di theorem yields a stronger result of Ajtai and Szemere´di [1]. This result states that for any δ > 0 there exists an n0 such that if n ≥ n0 then any subset of the set [n]×[n] of size at least δn2 contains a set of the form {(a,b),(a+d,b),(a,b+d)}. That is, dense subsets of the 2-dimensional grid contain axis-parallel isosceles triangles. Roth’s theorem is a simple corollary of this statement.

Roth’s theorem is the ﬁrst case of a famous result known as Szemere´di’s theorem. This result, to which we alluded earlier, states that for any natural number k ≥ 3 and any δ > 0 there exists n0 such that if n ≥ n0 then any subset of the set [n] of size at least δn contains an arithmetic progression of length k. This was ﬁrst proved by Szemere´di [109] in the early seventies using combinatorial techniques and since then several further proofs have emerged. The most important of these are that by Furstenberg

- [48, 50] using ergodic theory and that by Gowers [53, 54], who found a way to extend Roth’s original Fourier analytic argument to general k. Both of these methods have been highly inﬂuential.


Yet another proof technique was suggested by Frankl and Ro¨dl [42]. They showed that Szemere´di’s theorem would follow from the following generalization of Theorem 1.1, referred to as the hypergraph removal lemma. They proved this theorem for the speciﬁc case of K4(3), the complete 3-uniform hypergraph with 4 vertices. This was then extended to all 3-uniform hypergraphs in [77] and to K5(4) in [89]. Finally, it was proved for all hypergraphs by Gowers [55, 56] and, independently, by Nagle, Ro¨dl, Schacht and Skokan [78, 88]. Both proofs rely on extending Szemere´di’s regularity lemma to hypergraphs in an appropriate fashion.

- Theorem 1.2 For any k-uniform hypergraph H and any ǫ > 0, there exists δ > 0 such that any k-uniform hypergraph on n vertices which contains at most δnv(H) copies of H may be made H-free by removing at most ǫnk edges.


![image 2](<2012-conlon-graph-removal-lemmas_images/imageFile2.png>)

- 2The phrase ‘removal lemma’ is a comparatively recent coinage. It seems to have come into vogue in about 2005 when

the hypergraph removal lemma was ﬁrst proved (see, for example, [67, 78, 106, 112]).

- 3This was also the ﬁrst time that the triangle removal lemma was stated explicitly, though the weaker version


concerning graphs where every edge is contained in exactly one triangle had already appeared in the literature. The Ruzsa-Szemere´di theorem was usually [40, 41, 46] phrased in the following suggestive form: if a 3-uniform hypergraph is linear, that is, no two edges intersect on more than a single vertex, and triangle-free, then it has o(n2) edges. A more explicit formulation may be found in [23].

As well as reproving Szemere´di’s theorem, the hypergraph removal lemma allows one to reprove the multidimensional Szemere´di theorem. This theorem, originally proved by Furstenberg and Katznelson

- [49], states that for any natural number r, any ﬁnite subset S of Zr and any δ > 0 there exists n0 such that if n ≥ n0 then any subset of [n]r of size at least δnr contains a subset of the form a · S + d, that is, a dilated and translated copy of S. That it follows from the hypergraph removal lemma was ﬁrst observed by Solymosi [105]. This was the ﬁrst non-ergodic proof of this theorem. A new proof of the special case S = {(0,0),(1,0),(0,1)}, corresponding to the Ajtai-Szemere´di theorem, was given by Shkredov [102] using a Fourier analytic argument. Recently, a combinatorial proof of the density Hales-Jewett theorem, which is an extension of the multidimensional Szemere´di theorem, was discovered as part of the polymath project [81].


As well as its implications in number theory, the removal lemma and its extensions are central to the area of computer science known as property testing. In this area, one would like to ﬁnd fast algorithms to distinguish between objects which satisfy a certain property and objects which are far from satisfying that property. This ﬁeld of study was initiated by Rubinﬁeld and Sudan [92] and, subsequently, Goldreich, Goldwasser and Ron [51] started the investigation of such property testers for combinatorial objects. Graph property testing has attracted a particular degree of interest.

A classic example of property testing is to decide whether a given graph G is ǫ-far from being trianglefree, that is, whether at least ǫn2 edges will have to removed in order to make it triangle-free. The triangle removal lemma tells us that if G is ǫ-far from being triangle free then it must contain at least δn3 triangles for some δ > 0 depending only on ǫ. This furnishes a simple probabilistic algorithm for deciding whether G is ǫ-far from being triangle-free. We choose t = 2δ−1 triples of points from the vertices of G uniformly at random. If G is ǫ-far from being triangle-free then the probability that none of these randomly chosen triples is a triangle is (1 − δ)t < e−tδ < 13. That is, if G is ǫ-far from being triangle-free we will ﬁnd a triangle with probability at least 32, whereas if G is triangle-free we will clearly ﬁnd no triangles. The graph removal lemma may be used to derive a similar test for deciding whether G is ǫ-far from being H-free for any ﬁxed graph H.

![image 3](<2012-conlon-graph-removal-lemmas_images/imageFile3.png>)

![image 4](<2012-conlon-graph-removal-lemmas_images/imageFile4.png>)

In property testing, it is often of interest to decide not only whether a graph is far from being H-free but also whether it is far from being induced H-free. A subgraph H′ of a graph G is said to be an induced copy of H if there is a one-to-one map f : V (H) → V (H′) such that (f(u),f(v)) is an edge of H′ if and only if (u,v) is an edge of H. A graph G is said to be induced H-free if it contains no induced copies of H and ǫ-far from being induced H-free if we have to add and/or delete at least ǫn2 edges to make it induced H-free. Note that it is not enough to delete edges since, for example, if H is the empty graph on two vertices and G is the complete graph minus an edge, then G contains only one induced copy of H, but one cannot simply delete edges from G to make it induced H-free.

By proving an appropriate strengthening of the regularity lemma, Alon, Fischer, Krivelevich and Szegedy [6] showed how to modify the graph removal lemma to this setting. This result, which allows one to test for induced H-freeness, is known as the induced removal lemma.

- Theorem 1.3 For any graph H and any ǫ > 0, there exists a δ > 0 such that any graph on n vertices which contains at most δnv(H) induced copies of H may be made induced H-free by adding and/or deleting at most ǫn2 edges.


A substantial generalization of this result, known as the inﬁnite removal lemma, was proved by Alon and Shapira [12] (see also [75]). They showed that for each (possibly inﬁnite) family H of graphs and ǫ > 0 there is δ = δH(ǫ) > 0 such that if a graph G on n vertices contains at most δnv(H) induced

copies of H for every graph H in H, then G may be made induced H-free, for every H ∈ H, by adding and/or deleting at most ǫn2 edges. They then used this result to show that every hereditary graph property is testable, where a graph property is hereditary if it is closed under removal of vertices. These results were extended to 3-uniform hypergraphs by Avart, R¨odl and Schacht [14] and to k-uniform hypergraphs by Ro¨dl and Schacht [86].

In this survey we will focus on recent developments, particularly with regard to the quantitative aspects of the removal lemma. In particular, we will discuss recent improvements on the bounds for the graph removal lemma, Theorem 1.1, and the induced graph removal lemma, Theorem 1.3, each of which bypasses a natural impediment.

The usual proof of the graph removal lemma makes use of the regularity lemma and gives bounds for the removal lemma which are of tower-type in ǫ. To be more speciﬁc, let T(1) = 2 and, for each i ≥ 1, T(i + 1) = 2T(i). The bounds that come out of applying the regularity lemma to removal then say that if δ−1 = T(ǫ−cH) then any graph with at most δnv(H) copies of H may be made H-free by removing at most ǫn2 edges. Moreover, this tower-type dependency is inherent in any proof employing regularity. This follows from an important result of Gowers [52] (see also [24]) which states that the bounds that arise in the regularity lemma are necessarily of tower type. We will discuss this in more detail in Section 2.1 below.

Despite this obstacle, the following improvement was made by Fox [38].

- Theorem 1.4 For any graph H, there exists a constant aH such that if δ−1 = T(aH log ǫ−1) then any graph on n vertices which contains at most δnv(H) copies of H may be made H-free by removing at most ǫn2 edges.


As is implicit in the bounds, the proof of this theorem does not make an explicit appeal to Szemere´di’s regularity lemma. However, many of the ideas used are similar to ideas used in the proof of the regularity lemma. The chief diﬀerence lies in the fact that the conditions of the removal lemma (containing few copies of a given graph H) allow us to say more about the structure of these partitions. A simpliﬁed proof of this theorem will be the main topic of Section 2.2.

Though still of tower-type, Theorem 1.4 improves substantially on the previous bound. However, it remains very far from the best known lower bound on δ−1. The observation of Ruzsa and Szemere´di [93] that f(3)(n,6,3) = Ω(r3(n)n) allows one to transfer lower bounds for r3(n) to a corresponding lower bound for the triangle removal lemma. The best construction of a set containing no arithmetic progression of length 3 is due to Behrend [16] and gives a subset of [n] with density e−c

√logn. Transferring this to the graph setting yields a graph containing ǫclogǫ−1n3 triangles which cannot be made triangle-free by removing fewer than ǫn2 edges. This quasi-polynomial lower bound, δ−1 ≥ ǫ−clogǫ−1, remains the best known.4

![image 5](<2012-conlon-graph-removal-lemmas_images/imageFile5.png>)

The standard proof of the induced removal lemma uses the strong regularity lemma of Alon, Fischer, Krivelevich and Szegedy [6]. We will speak at length about this result in Section 3.1. Here it will suﬃce to say that, like the ordinary regularity lemma, the bounds which an application of this theorem

![image 6](<2012-conlon-graph-removal-lemmas_images/imageFile6.png>)

4It is worth noting that the best known upper bound for Roth’s theorem, due to Sanders [95], is considerably better than the best upper bound for r3(n) that follows from triangle removal. This upper bound is r3(n) = O (loglogn)

5

logn n . A recent result of Schoen and Shkredov [99], building on further work of Sanders [96], shows that any subset of [n] of density e−c(

![image 7](<2012-conlon-graph-removal-lemmas_images/imageFile7.png>)

log n

loglogn)1/6 contains a solution to the equation x1 + · · · + x5 = 5x6. Since arithmetic progressions correspond to solutions of x1 + x2 = 2x3, this suggests that the answer should be closer to the Behrend bound. The bounds for triangle removal are unlikely to impinge on these upper bounds for some time, if at all.

![image 8](<2012-conlon-graph-removal-lemmas_images/imageFile8.png>)

gives for the induced removal lemma are necessarily very large. Let W(1) = 2 and, for i ≥ 1, W(i + 1) = T(W(i)). This is known as the wowzer function and its values dwarf those of the usual tower function.5 By using the strong regularity lemma, the standard proof shows that we may take δ−1 = W(aHǫ−c) in the induced removal lemma, Theorem 1.3. Moreover, as with the ordinary removal lemma, such a bound is inherent in the application of the strong regularity lemma. This follows from recent results of Conlon and Fox [24] and, independently, Kalyanasundaram and Shapira [61] showing that the bounds arising in strong regularity are necessarily of wowzer type.

In the other direction, Conlon and Fox [24] showed how to bypass this obstacle and prove that the bounds for δ−1 are at worst a tower in a power of ǫ−1.

- Theorem 1.5 There exists a constant c > 0 such that, for any graph H, there exists a constant aH such that if δ−1 = T(aHǫ−c) then any graph on n vertices which contains at most δnv(H) induced copies of H may be made induced H-free by adding and/or deleting at most ǫn2 edges.


A discussion of this theorem will form the subject of Section 3.2. The key observation here is that the strong regularity lemma is used to prove an intermediate statement (Lemma 3.2 below) which then implies the induced removal lemma. This intermediate statement may be proved without recourse to the full strength of the strong regularity lemma. There are also some strong parallels with the proof of Theorem 1.4 which we will draw attention to in due course.

In Section 3.3, we present the proof of Alon and Shapira’s inﬁnite removal lemma. In another paper, Alon and Shapira [11] showed that the dependence in the inﬁnite removal lemma can depend heavily on the family H. They proved that for every function δ : (0,1) → (0,1), there exists a family H of graphs such that any δH : (0,1) → (0,1) which satisﬁes the inﬁnite removal lemma for H satisﬁes δH = o(δ). However, such examples are rather unusual and the proof presented in Section 3.3 of the inﬁnite removal lemma implies that for many commonly studied families H of graphs the bound on δH−1 is only tower-type, improving the wowzer-type bound from the original proof.

Our discussions of the graph removal lemma and the induced removal lemma will occupy the bulk of this survey but we will also talk about some further recent developments in the study of removal lemmas. These include arithmetic removal lemmas (Section 4) and the recently developed sparse removal lemmas which hold for subgraphs of sparse random and pseudorandom graphs (Section 5). We will conclude with some further comments on related topics.

# 2 The graph removal lemma

In this section we will discuss the two proofs of the removal lemma, Theorem 1.1, at length. In Section 2.1, we will talk about the regularity lemma and the usual proof of the removal proof. Then, in Section 2.2, we will consider a simpliﬁed variant of the second author’s recent proof [38], showing how it connects to the weak regularity lemma of Frieze and Kannan [44, 45].

## 2.1 The standard proof

We begin with the proof of the regularity lemma and then deduce the removal lemma. For vertex subsets S,T of a graph G, we let eG(S,T) denote the number of pairs in S ×T that are edges of G and

![image 9](<2012-conlon-graph-removal-lemmas_images/imageFile9.png>)

5To give some indication, we note that W(2) = 4, W(3) = 65536 and W(4) is a tower of 2s of height 65536.

dG(S,T) = eG|S(||S,TT|) denote the fraction of pairs in S×T that are edges of G. For simplicity of notation, we drop the subscript if the graph G is clear from context. A pair (S,T) of subsets is ǫ-regular if, for all subsets S′ ⊂ S and T′ ⊂ T with |S′| ≥ ǫ|S| and |T′| ≥ ǫ|T|, we have |d(S′,T′) − d(S,T)| ≤ ǫ. Informally, a pair of subsets is ǫ-regular with a small ǫ if the edges between S and T are uniformly distributed among large subsets.

![image 10](<2012-conlon-graph-removal-lemmas_images/imageFile10.png>)

Let G = (V,E) be a graph and P : V = V1 ∪ ... ∪ Vk be a vertex partition of G. The partition of P is equitable if each pair of parts diﬀer in size by at most 1. The partition P is ǫ-regular if all but at most ǫk2 pairs of parts (Vi,Vj) are ǫ-regular. We next state Szemere´di’s regularity lemma.

- Lemma 2.1 For every ǫ > 0, there is K = K(ǫ) such that every graph G = (V,E) has an equitable, ǫ-regular vertex partition into at most K parts. Moreover, we may take K to be a tower of height O(ǫ−5).


Let q : [0,1] → R be a convex function. For vertex subsets S,T ⊂ V of a graph G, let q(S,T) = q(d(S,T))|S|V|||T2|. For partitions S : S = S1 ∪ ... ∪ Sa and T : T = T1 ∪ ... ∪ Tb, let q(S,T ) =

![image 11](<2012-conlon-graph-removal-lemmas_images/imageFile11.png>)

1≤i≤a,1≤j≤b q(Si,Tj). For a vertex partition P : V = V1 ∪... ∪ Vk of G, deﬁne the mean-q density to be

q(Vi,Vj).

q(P) = q(P,P) =

1≤i,j≤k

We next state some simple properties which follow from Jensen’s inequality using the convexity of q. A reﬁnement of a partition P of a vertex set V is another partition Q of V such that every part of Q is a subset of a part of P.

Proposition 2.1 1. For partitions S and T of vertex subsets S and T, we have q(S,T ) ≥ q(S,T).

- 2. If Q is a reﬁnement of P, then q(Q) ≥ q(P).
- 3. If d = d(G) = d(V,V ) is the edge density of G, then, for any vertex partition P, q(d) ≤ q(P) ≤ dq(1) + (1 − d)q(0).


The ﬁrst and second part of Proposition 2.1 show that by reﬁning a vertex partition the mean-q density cannot decrease, while the last part gives the range of possible values for q(P) if we only know the edge density d of G.

The convex function q(x) = x2 for x ∈ [0,1] is chosen in the standard proof of the graph regularity lemma and we will do the same for the rest of this subsection. The following lemma is the key claim for the proof of the regularity lemma. The set-up is that we have a partition P which is not ǫ-regular. For each pair (Vi,Vj) of parts of P which is not ǫ-regular, there are a pair of witness subsets Vij,Vji to the fact that the pair of parts is not ǫ-regular. We consider the coarsest reﬁnement Q of P so that each witness subset is the union of parts of Q. The lemma concludes that the number of parts of Q is at most exponential in the number of parts of P and, using a Cauchy-Schwarz defect inequality, that the mean-q density of the partition Q is substantially larger than the mean-q density of P. Because it simpliﬁes our calculations a little, we will assume, when we say a partition is equitable, that it is exactly equitable, that is, that all parts have precisely the same size. This does not aﬀect our results substantially but simpliﬁes the presentation.

### Lemma 2.2 If an equitable partition P : V = V1 ∪ ... ∪ Vk is not ǫ-regular then there is a reﬁnement Q of P into at most k2k parts for which q(Q) ≥ q(P) + ǫ5.

Proof: For each pair (Vi,Vj) which is not ǫ-regular, there are subsets Vij ⊂ Vi and Vji ⊂ Vj with |Vij| ≥ ǫ|Vi| and |Vji| ≥ ǫ|Vj| such that |d(Vij,Vji) − d(Vi,Vj)| ≥ ǫ. For each part Vj such that (Vi,Vj) is not ǫ-regular, we have a partiton Pij of Vi into two parts Vij and Vi \ Vij. Let Pi be the partition of Vi which is the common reﬁnement of these at most k − 1 partitions of Vi, so Pi has at most 2k−1 parts. We let Q be the partition of V which is the union of the k partitions of the form Pi, so Q has at most k2k−1 parts. We have

q(Q) − q(P) =

≥

≥

=

≥

i,j

(q(Pi,Pj) − q(Vi,Vj))

(q(Pi,Pj) − q(Vi,Vj))

(Vi,Vj) irregular

(q(Pij,Pji) − q(Vi,Vj))

(Vi,Vj) irregular

- |U||W|

![image 12](<2012-conlon-graph-removal-lemmas_images/imageFile12.png>)

- |V |2


(d(U,W) − d(Vi,Vj))2

(Vi,Vj) irregular U∈Pij,W∈Pji

|Vij||Vji| |V |2

(d(Vij,Vji) − d(Vi,Vj))2

![image 13](<2012-conlon-graph-removal-lemmas_images/imageFile13.png>)

(Vi,Vj) irregular

ǫ k

2

ǫ2

≥ ǫk2

![image 14](<2012-conlon-graph-removal-lemmas_images/imageFile14.png>)

= ǫ5,

where the ﬁrst and third inequalities are by noting that the summands are nonnegative and the second inequality follows from the ﬁrst part of Proposition 2.1, which shows that the mean-q density cannot decrease when taking a reﬁnement. In the fourth inequality, we used that |Vij| ≥ ǫ|Vi| ≥ kǫ|V | and similarly for |Vji|. Finally, the equality in the fourth line follows from the identity

![image 15](<2012-conlon-graph-removal-lemmas_images/imageFile15.png>)

|U||W|d(Vi,Vj) =

|U||W|d(U,W),

U∈Pij,W∈Pji

U∈Pij,W∈Pji

which counts e(Vi,Vj) in two diﬀerent ways. This completes the proof. ✷ The next lemma, which is rather standard, shows that for any vertex partition Q, there is a vertex equipartition P′ with a similar number of parts to Q and mean-square density not much smaller than the mean-square density of Q. It is useful in density increment arguments where at each stage one would like to work with an equipartition. It is proved by ﬁrst arbitrarily partitioning each part of Q into parts of order |V |/t, except possibly one additional remaining smaller part, and then arbitrarily partitioning the union of the smaller remaining parts into parts of order |V |/t.

### Lemma 2.3 Let G = (V,E) be a graph and Q : V = V1 ∪ ... ∪ Vℓ be a vertex partition into k parts. Then, for q(x) = x2, there is an equitable partition P′ of V into t parts such that q(P′) ≥ q(Q) − 2ℓt. Combining Lemmas 2.2 and 2.3 with t = 4ǫ−5|Q| ≤ ǫ−5k2k+2, we obtain the following corollary.

![image 16](<2012-conlon-graph-removal-lemmas_images/imageFile16.png>)

Corollary 2.1 If an equitable partition P : V = V1∪...∪Vk is not ǫ-regular then there is an equitable reﬁnement P′ of P into at most ǫ−5k2k+2 parts for which q(P′) ≥ q(P) + ǫ5/2.

We next show how Szemere´di’s regularity lemma, Lemma 2.1, can be quickly deduced from this result. Proof: To prove the regularity lemma, we start with the trivial partition P0 into one part, and iterate the above corollary to obtain a sequence P0,P1,... ,Ps of equitable partitions with q(Pi+1) ≥ q(Pi)+ǫ5/2 until we arrive at an equitable ǫ-regular partition Ps. As the mean-square density of each partition has to lie between 0 and 1, after at most 2ǫ−5 iterations we arrive at the equitable ǫ-regular partition Ps with s ≤ 2ǫ−5. The number of parts increases by one exponential in each iteration, giving the desired number of parts in the regularity partition. This completes the proof of Szemere´di’s regularity lemma. ✷ The constructions of Gowers [52] and the authors [24] show that the tower-type bound on the number of parts in Szemere´di’s regularity lemma is indeed necessary. In particular, the construction in [24] shows that K(ǫ) in Lemma 2.1 is at least a tower of twos of height Ω(ǫ−1). The constructions are formed by reverse engineering the upper bound proof. We construct a sequence P0,... ,Ps of partitions with s = Ω(ǫ−1). As in the upper bound proof, each partition in the sequence uses exponentially more parts than the previous partition in the sequence. We may choose the edges using these partitions and some randomness so as to guarantee that none of these partitions (except the last) are ǫ-regular. Furthermore, we can guarantee that any partition that is ǫ-regular must be close to being a reﬁnement of the last partition in this sequence. This implies that the number of parts must be at least roughly |Ps|.

We next prove the graph removal lemma, Theorem 1.1, from the regularity lemma.

Proof: Let m denote the number of edges of H, so m ≤ h2 . Let γ = 4ǫhh and δ = (2h)−2hǫmK−h, where K = K(γ) is as in the regularity lemma. We apply the regularity lemma to G and obtain an

![image 17](<2012-conlon-graph-removal-lemmas_images/imageFile17.png>)

equitable, γ-regular partition into k ≤ K parts. If the number n of vertices of G satisﬁes n < δ−1/h, then the number of copies of H in G is at most δnh < 1 and G is H-free, in which case there is nothing to prove. So we may assume n ≥ δ−1/h. We obtain a subgraph G′ of G by removing edges of

- G between all pairs of parts which are not γ-regular or which have edge density at most ǫ. As there are at most γk2 ordered pairs of parts which are not γ-regular and each part has order at most 2n/k, at most (γk2/2)(2n/k)2 = 2γn2 edges are deleted between pairs of parts which are not γ-regular. The number of edges between parts which have edge density at most ǫ is at most ǫn2/2. Hence, the number of edges of G deleted to obtain G′ is at most 2γn2 + ǫn2/2 < ǫn2. If G′ is H-free, then we are done.

Assume for contradiction that G′ is not H-free. A copy of H in G′ must have its edges going between pairs of parts which are both γ-regular and have density at least ǫ. Hence, there is a mapping from V (H) to the partition of V (G) so that each edge of H maps to a pair of parts which is both γ-regular and have edge density at least ǫ. But the following standard counting lemma (see, e.g., Lemma 3.2 in Alon, Fischer, Krivelevich and Szegedy [6] for a minor variant) shows that the number of labeled copies of H in G′ (and hence in G) is at least 2−hǫm(n/2k)h > h!δnh. This contradicts that G has at most δnh copies of H, completing the proof. ✷

Lemma 2.4 If H is a graph with vertices 1,... ,h and m edges and G is a graph with not necessarily disjoint vertex subsets W1,... ,Wh such that |Wi| ≥ γ−1 for 1 ≤ i ≤ h and, for every edge (i,j) of

- H, the pair (Wi,Wj) is γ-regular with density d(Wi,Wj) > ǫ and γ ≤ 4ǫhh, then G contains at least 2−hǫm|W1| × ··· × |Wh| labeled copies of H with the copy of vertex i in Wi.


![image 18](<2012-conlon-graph-removal-lemmas_images/imageFile18.png>)

The standard proof of this counting lemma uses a greedy embedding strategy. One considers embedding the vertices one at a time, using the regularity condition to maintain the property that at each step where vertex i of H is not yet embedded the set of vertices of G which could potentially be used to embed vertex i is large.

## 2.2 An improved bound

A partition P : V = V1 ∪ ... ∪ Vk of the vertex set of a graph G = (V,E) is weak ǫ-regular if, for all subsets S,T ⊂ V , we have

|S ∩ Vi||T ∩ Vj|d(Vi,Vj) ≤ ǫ|V |2.

e(S,T) −

1≤i,j≤k

That is, the density between two sets may be approximated by taking a weighted average over the densities between the sets which they intersect. The Frieze-Kannan weak regularity lemma [44, 45] states that any graph has such a weak regular partition.

- Lemma 2.5 Let R(ǫ) = 2cǫ−2, where c is an absolute constant. For every graph G = (V,E) and every equitable partition P of G into k parts, there is an equitable partition P′ which is a reﬁnement of P into at most kR(ǫ) parts which is weak ǫ-regular.

Unlike the usual regularity lemma, the bounds in Lemma 2.5 are quite reasonable.6 It is therefore natural to try to apply it to prove the removal lemma. However, it seems unlikely that this lemma is itself suﬃcient to prove the removal lemma, since it only gives control over edge densities of a global nature.

However, as noted by Tao [111] (see also [87]), one can prove a stronger theorem by simply iterating the Frieze-Kannan weak regularity lemma.7 Tao developed this lemma to give an alternative proof of the regularity lemma8 which extended more easily to hypergraphs [112]. Here we use it to improve the bounds for removal.

- Lemma 2.6 Let q : [0,1] → R be a convex function, G be a graph with d = d(G), f : N → [0,1] be a decreasing function and r = (dq(1) + (1 − d)q(0) − q(d)) /γ. Then there are equitable partitions P and Q with Q a reﬁnement of P satisfying q(Q) ≤ q(P) + γ, Q is weak f(|P|)-regular and |Q| ≤ tr, where t0 = 1, ti = ti−1R(f(ti−1)) for 1 ≤ i ≤ r and R(x) = 2cx−2 as in the Frieze-Kannan weak regularity lemma.


The proof of Lemma 2.6 is quite similar to the proof of Szemer´edi’s regularity lemma discussed in the previous subsection. One starts with the trivial partition P0 of V into one part. We then apply Lemma

![image 19](<2012-conlon-graph-removal-lemmas_images/imageFile19.png>)

6They are also sharp, that is, there are graphs for which the minimum number of parts in any weak ǫ-regular partition

is 2Ω(ǫ−2). This was proved in [24] (see also [5]). 7We will say more about this sort of iteration in Section 3.1 below. 8More recently, Conlon and Fox [24] showed that it is also closely related to the regular approximation lemma. This lemma, which arose in the study of graph limits by Lova´sz and Szegedy [74] and also in work on the hypergraph generalization of the regularity lemma by Ro¨dl and Schacht [85], says that by adding and/or deleting a small number of edges in a graph G, we may ﬁnd another graph G′ which admits very ﬁne regular partitions. We refer the reader to [24] and [87] for further details.

- 2.5 repeatedly to construct a sequence of partitions P0,P1,... so that Pi+1 is weak f(|Pi|)-regular. If q(Pi+1) > q(Pi) + γ, then we continue with this process. Otherwise, q(Pi+1) ≤ q(Pi) + γ, so we set Q = Pi+1 and P = Pi and stop the process. This process must stop within r iterations as the third part of Proposition 2.1 shows that the mean-q density lies in an interval of length rγ.


Rather than using the usual q(x) = x2, we will use the convex function q on [0,1] deﬁned by q(0) = 0 and q(x) = xlog x for x ∈ (0,1]. This entropy function is central to the proof since it captures the extra structural information coming from Lemma 2.8 below in a concise fashion. Note that the last part of Proposition 2.1 implies that dlog d ≤ q(P) ≤ 0 for every partition P.

The next lemma is a counting lemma that complements the Frieze-Kannan weak regularity lemma. As one might expect, this lemma gives a global count for the number of copies of H, whereas the counting lemma associated with the usual regularity lemma gives a means of counting copies of H between any v(H) parts of the partition which are pairwise regular. Its proof, which we omit, is by a simple telescoping sum argument.

- Lemma 2.7 ([18], Theorem 2.7 on page 1809) Let H be a graph on {1,... ,h} with m edges. Let

- G = (V,E) be a graph on n vertices and Q : V = V1 ∪ ... ∪ Vt be a vertex partition which is weak ǫ-regular. The number of homomorphisms from H to G is within ǫmnh of


1≤i1,...,ih≤t (r,s)∈E(H)

d(Vir,Vis)

h

a=1

|Via|.

Let P and Q be vertex partitions of a graph G with Q a reﬁnement of P. A pair (Vi,Vj) of parts of

- P is (α,c)-shattered by Q if at least a c-fraction of the pairs (u,v) ∈ Vi × Vj go between pairs of parts of Q with edge density between them less than α.


One of the key components of the proof is the following lemma, which says that if P and Q are vertex partitions like those given by Lemma 2.6, then there are many pairs of vertex sets in P which are shattered by Q.

- Lemma 2.8 Let H be a graph on {1,... ,h} with m edges and let α > 0. Suppose G is a graph on


n vertices for which there are less than δnh homomorphisms of H into G, where δ = 14αm(2k)−h. Suppose P and Q are equitable vertex partitions of G with |P| = k ≤ n and Q is a reﬁnement of P

![image 20](<2012-conlon-graph-removal-lemmas_images/imageFile20.png>)

which is weak f(k)-regular, where f(k) = 41mαm(2k)−h. For every h-tuple V1,... ,Vh of parts of P, there is an edge (i,j) of H for which the pair (Vi,Vj) is (α, 21m)-shattered by Q.

![image 21](<2012-conlon-graph-removal-lemmas_images/imageFile21.png>)

![image 22](<2012-conlon-graph-removal-lemmas_images/imageFile22.png>)

Proof: As |P| = k ≤ n, we have |Vi| ≥ 2nk for each i. Let Qi denote the partition of Vi which consists of the parts of Q which are subsets of Vi. Consider an h-tuple (v1,... ,vh) ∈ V1 × ··· × Vh picked uniformly at random. Also consider the event E that, for each edge (i,j) of H, the pair (vi,vj) goes between parts of Qi and Qj with density at least α. If E occurs with probability at least 1/2, as Q is weak f(k)-regular, Lemma 2.7 implies that the number of homomorphisms of H into G where the copy of vertex i is in Vi for 1 ≤ i ≤ h is at least

![image 23](<2012-conlon-graph-removal-lemmas_images/imageFile23.png>)

- h
- i=1


- 1

![image 24](<2012-conlon-graph-removal-lemmas_images/imageFile24.png>)

- 2


- 1

![image 25](<2012-conlon-graph-removal-lemmas_images/imageFile25.png>)

- 2


|Vi| − mf(k)nh ≥

αm

αm(2k)−h − mf(k) nh = δnh,

contradicting that there are less than δnh homomorphisms of H into G. So E occurs with probability less than 1/2. Hence, for at least 1/2 of the h-tuples (v1,... ,vh) ∈ V1 × ··· × Vh, there is an edge (i,j) of H such that the pair (vi,vj) goes between parts of Qi and Qj with density less than α. This implies that for at least one edge (i,j) of H, the pair (Vi,Vj) is (α, 21m)-shattered by Q. ✷ We will need the following lemma from [38] which tells us that if a pair of parts from P is shattered by Q then there is an increment in the mean-entropy density. Its proof is by a simple application of Jensen’s inequality.

![image 26](<2012-conlon-graph-removal-lemmas_images/imageFile26.png>)

- Lemma 2.9 ([38], Lemma 7 on page 570) Let q : [0,1] → R be the convex function given by q(0) = 0


and q(x) = xlog x for x > 0. Let ǫ1,... ,ǫr and d1,... ,dr be nonnegative real numbers with ri=1 ǫi = 1 and d = si=1 ǫidi. Suppose β < 1 and I ⊂ [r] is such that di ≤ βd for i ∈ I and let s = i∈I ǫi. Then r

ǫiq(di) ≥ q(d) + (1 − β + q(β))sd.

i=1

We are now ready to prove Theorem 1.4 in the following precise form.

- Theorem 2.1 Let H be a graph on {1,... ,h} with m edges. Let ǫ > 0 and δ−1 be a tower of twos of height 8h4 log ǫ−1. If G is a graph on n vertices in which at least ǫn2 edges need to be removed to make it H-free, then G contains at least δnh copies of H.


Proof: Suppose for contradiction that there is a graph G on n vertices in which at least ǫn2 edges need to be removed from G to delete all copies of H, but G contains fewer than δnh copies of H. If n ≤ δ−1/h, then the number of copies of H in G is less than δnh ≤ 1, so G is H-free, contradicting that at least ǫn2 edges need to be removed to make the graph H-free. Hence, n > δ−1/h. Note that the number of mappings from V (H) to V (G) which are not one-to-one is nh−h! nh ≤ h2nh−1 < h2δ1/hnh. Let δ′ = 2h2δ1/h, so the number of homomorphisms from H to G is at most δ′nh.

The graph G contains at least ǫn2/m edge-disjoint copies of H. Let G′ be the graph on the same vertex set which consists entirely of the at least ǫn2/m edge-disjoint copies of H. Then d(G′) ≥

′)

- m · ǫ/m = ǫ and G′ consists of d(G


m n2 edge-disjoint copies of H. We will show that there are at least δ′nh homomorphisms from H to G′ (and hence to G as well). For the rest of the argument, we will assume the underlying graph is G′. Let α = 8mǫ . Apply Lemma 2.6 to G′ with f(k) = 41mαm(2k)−h and γ = d(G

![image 27](<2012-conlon-graph-removal-lemmas_images/imageFile27.png>)

′)

2h4 . Note that r as in

![image 28](<2012-conlon-graph-removal-lemmas_images/imageFile28.png>)

![image 29](<2012-conlon-graph-removal-lemmas_images/imageFile29.png>)

![image 30](<2012-conlon-graph-removal-lemmas_images/imageFile30.png>)

- Lemma 2.6 is r = d(G′)log(1/d(G′))/γ = 2h4 log(1/d(G′)) ≤ 2h4 log ǫ−1.


Hence, we get a pair of equitable vertex partitions P and Q, with Q a reﬁnement of P, q(Q) ≤ q(P)+γ,

- Q is weak f(|P|)-regular and |Q| is at most a tower of twos of height 3r ≤ 6h4 log ǫ−1. Let V1,... ,Vk denote the parts of P and Qi denote the partition of Vi consisting of the parts of Q which are subsets of Vi.


Suppose that (Va,Vb) is a pair of parts of P with edge density d = d(Va,Vb) ≥ ǫ/m which is (α, 21m)shattered by Q. Note that α ≤ d/8. Arbitrarily order the pairs Ui×Wi ∈ Qa×Qb, letting di = d(Ui,Wi)

![image 31](<2012-conlon-graph-removal-lemmas_images/imageFile31.png>)

and ǫi = ||UVi||Wi|

a||Vb| , so that the conditions of Lemma 2.9 with β = 1/8 are satisﬁed. Applying Lemma

![image 32](<2012-conlon-graph-removal-lemmas_images/imageFile32.png>)

2.9, we get, since q(β) = −18 log 8 = −38, that

![image 33](<2012-conlon-graph-removal-lemmas_images/imageFile33.png>)

![image 34](<2012-conlon-graph-removal-lemmas_images/imageFile34.png>)

- 1

![image 35](<2012-conlon-graph-removal-lemmas_images/imageFile35.png>)

- 2m


q(Qa,Qb) − q(Va,Vb) ≥ (1 − β + q(β))

d(Va,Vb)|Va||Vb|/n2 ≥

1 4m

e(Va,Vb)/n2.

![image 36](<2012-conlon-graph-removal-lemmas_images/imageFile36.png>)

Note that

q(Q) − q(P) =

(q(Qa,Qb) − q(Va,Vb)),

1≤a,b≤k

which shows that q(Q) − q(P) is the sum of nonnegative summands.

There are at most mǫ n2/2 edges of G′ going between pairs of parts of P with density at most mǫ . Hence, at least 1/2 of the edge-disjoint copies of H making up G′ have all its edges going between pairs of

![image 37](<2012-conlon-graph-removal-lemmas_images/imageFile37.png>)

![image 38](<2012-conlon-graph-removal-lemmas_images/imageFile38.png>)

parts of P of density at least mǫ . By Lemma 2.8, for each copy of H, at least one of its edges goes between a pair of parts of P which is (α, 21m)-shattered by Q. Thus,

![image 39](<2012-conlon-graph-removal-lemmas_images/imageFile39.png>)

![image 40](<2012-conlon-graph-removal-lemmas_images/imageFile40.png>)

q(Q) − q(P) ≥

d(G′) 2m

1 4m

1 4m ·

e(Va,Vb)/n2 ≥

=

![image 41](<2012-conlon-graph-removal-lemmas_images/imageFile41.png>)

![image 42](<2012-conlon-graph-removal-lemmas_images/imageFile42.png>)

![image 43](<2012-conlon-graph-removal-lemmas_images/imageFile43.png>)

d(G′) 8m2

> γ,

![image 44](<2012-conlon-graph-removal-lemmas_images/imageFile44.png>)

where the sum is over all ordered pairs (Va,Vb) of parts of P which are (α, 21m)-shattered by Q and with d(Va,Vb) ≥ mǫ . This contradicts q(Q) ≤ q(P) + γ and completes the proof. ✷

![image 45](<2012-conlon-graph-removal-lemmas_images/imageFile45.png>)

![image 46](<2012-conlon-graph-removal-lemmas_images/imageFile46.png>)

# 3 The induced removal lemma

As in the last section, we will again discuss two diﬀerent proofs of the induced removal lemma, Theorem 1.3. In Section 3.1, we will discuss the proof of Alon, Fischer, Krivelevich and Szegedy [6], which uses their strong regularity lemma and gives a wowzer-type bound. In Section 3.2, we will examine the authors’ recent proof [24] of a tower-type bound. We will discuss Alon and Shapira’s generalization of the induced removal lemma, which applies to inﬁnite families of graphs, in Section 3.3.

## 3.1 The usual proof

For an equitable partition P = {Vi|1 ≤ i ≤ k} of V (G) and an equitable reﬁnement Q = {Vi,j|1 ≤ i ≤ k,1 ≤ j ≤ ℓ} of P, we say that Q is ǫ-close to P if the following is satisﬁed. All 1 ≤ i ≤ i′ ≤ k but at most ǫk2 of them are such that, for all 1 ≤ j,j′ ≤ ℓ but at most ǫℓ2 of them, |d(Vi,Vi′)−d(Vi,j,Vi′,j′)| < ǫ holds. This notion roughly says that Q is an approximation of P. The strong regularity lemma of Alon, Fischer, Krivelevich and Szegedy [6] is now as follows.

- Lemma 3.1 (Strong regularity lemma) For every function f : N → (0,1) there exists a number S = S(f) with the following property. For every graph G = (V,E), there is an equitable partition P of the vertex set V and an equitable reﬁnement Q of P with |Q| ≤ S such that the partition P is f(1)-regular, the partition Q is f(|P|)-regular and Q is f(1)-close to P.


That is, there is a regular partition P and a reﬁnement Q such that Q is very regular and yet the densities between parts (Vi,j,Vi′,j′) of Q are usually close to the densities between the parts (Vi,Vi′) of P containing them.

Let f(1) = ǫ. Here, and throughout this section, we let q(x) = x2 be the square function as in the proof of Szemere´di’s regularity lemma in the previous section. The condition that Q be ǫ-close to P

is equivalent, up to a polynomial change in ǫ, to q(Q) ≤ q(P) + ǫ. Indeed, if Q is ǫ-close to P, then q(Q) ≤ q(P)+O(ǫ), while if q(Q) ≤ q(P)+ǫ, then Q is O(ǫ1/4)-close to P. A version of this statement is present in Lemma 3.7 of [6]. As it is suﬃcient and more convenient to work with mean-square density instead of ǫ-closeness, we do so from now on. That is, we replace the third condition in the regularity lemma with the condition that q(Q) ≤ q(P) + ǫ.

With this observation, the proof of the strong removal lemma becomes quite straightforward. Note that we may assume that f is a decreasing function by replacing it, if necessary, with the function given by f′(i) = min1≤j≤i f(j). We consider a series of partitions P1,P2,... , where P1 is an f(1)-regular partition and Pi+1 is an f(|Pi|)-regular reﬁnement of the partition Pi. Since Pi+1 is a reﬁnement of Pi we know that the mean-square density must have increased, that is, q(Pi+1) ≥ q(Pi). If also q(Pi+1) ≤ q(Pi)+ǫ then, since f is decreasing and Pi+1 is f(|Pi|)-regular, we see that all three conditions of the theorem are satisﬁed with P = Pi and Q = Pi+1 as the required partitions. Otherwise, we have q(Pi+1) > q(Pi) + ǫ. However, since the mean-square density is bounded above by 1, this can happen at most ǫ−1 times, concluding the proof.

It is not hard to see why this proof results in wowzer-type bounds. At each step, we are applying the regularity lemma to ﬁnd a partition Pi+1 which is regular in the number of parts in the previous partition Pi. The bounds coming from the regularity lemma then imply that |Pi+1| = T(f(|Pi|)−O(1)). But this iterated tower-type bound is essentially how we deﬁne the wowzer function.

That this is the correct behaviour for the bounds in the strong regularity lemma was proved independently by Conlon and Fox [24] and by Kalyanasundaram and Shapira [61], though both proofs use slightly diﬀerent ideas and result in slightly diﬀerent bounds. With the function f : N → (0,1) taken to be f(n) = ǫ/n, the proof given in [24] shows that the number of parts in the smaller partition P may need to be as large as wowzer in a power of ǫ−1, while that given in [61] proves that it must be at least wowzer in log ǫ−1.

![image 47](<2012-conlon-graph-removal-lemmas_images/imageFile47.png>)

The following easy corollary of the strong regularity lemma [6] is the key to proving the induced graph removal lemma.

- Lemma 3.2 For each 0 < ǫ < 1/3 and decreasing function f : N → (0,1/3), there is δ′ = δ′(ǫ,f) such that every graph G = (V,E) with |V | ≥ δ′−1 has an equitable partition V = V1 ∪ ... ∪ Vk and vertex subsets Wi ⊂ Vi such that |Wi| ≥ δ′|V |, each pair (Wi,Wj) with 1 ≤ i ≤ j ≤ k is f(k)-regular and all but at most ǫk2 pairs 1 ≤ i ≤ j ≤ k satisfy |d(Vi,Vj) − d(Wi,Wj)| ≤ ǫ.


In fact, Lemma 3.2 is a little bit stronger than the original version in [6] in that each set Wi is f(k)-regular with itself.9 The original version follows from the strong regularity lemma, applied with

ǫ 4

- 1

![image 48](<2012-conlon-graph-removal-lemmas_images/imageFile48.png>)

- 2


f′(k) = min f(k),

,

![image 49](<2012-conlon-graph-removal-lemmas_images/imageFile49.png>)

k + 2 2

−1

,

by taking the partition V = V1 ∪ ... ∪ Vk to be the partition P in the strong regularity lemma and the subset Wi to be a random part Vi,p ⊂ Vi of the reﬁnement Q of P in the strong regularity lemma.

Since f′(k) ≤ 12 k+22 −1, it is straightforward to check that all pairs (Wi,Wj) are f(k)-regular with probability greater than 21. Moreover, the expected number of pairs with 1 ≤ i < j ≤ k for which

![image 50](<2012-conlon-graph-removal-lemmas_images/imageFile50.png>)

![image 51](<2012-conlon-graph-removal-lemmas_images/imageFile51.png>)

![image 52](<2012-conlon-graph-removal-lemmas_images/imageFile52.png>)

9This stronger version may be derived from an extra application of the regularity lemma within each of the pieces Wi, together with a suitable application of Ramsey’s theorem. This is essentially the process carried out in [6], though they do not state their ﬁnal result in the same form as Lemma 3.2.

|d(Vi,Vj) − d(Wi,Wj)| > ǫ is at most

ǫ 4

![image 53](<2012-conlon-graph-removal-lemmas_images/imageFile53.png>)

k 2

ǫ 4

+

![image 54](<2012-conlon-graph-removal-lemmas_images/imageFile54.png>)

k 2

ǫ 2

=

![image 55](<2012-conlon-graph-removal-lemmas_images/imageFile55.png>)

k 2

.

Here, the two 4ǫ factors come from the deﬁnition of f(1)-closeness. The ﬁrst factor comes from the fact that at most an 4ǫ-fraction of the pairs (Vi,Vj) do not have good approximations while the second factor comes from the fact that for all other pairs there are at most an 4ǫ fraction of pairs (Wi,Wj) which do not satisfy |d(Vi,Vj) − d(Wi,Wj)| ≤ ǫ. Therefore, by Markov’s inequality, the probability that the number of bad pairs is greater than ǫ k2 is less than 12. We therefore see that with positive probability there is a choice of Wi satisfying the required weaker version of Lemma 3.2.

![image 56](<2012-conlon-graph-removal-lemmas_images/imageFile56.png>)

![image 57](<2012-conlon-graph-removal-lemmas_images/imageFile57.png>)

![image 58](<2012-conlon-graph-removal-lemmas_images/imageFile58.png>)

![image 59](<2012-conlon-graph-removal-lemmas_images/imageFile59.png>)

If we assume the full strength of Lemma 3.2 as stated, that is, that each Wi is also f(k)-regular with itself, it is easy to deduce the induced removal lemma. Let h = |V (H)| and take f(k) = 4ǫhh. If there is a mapping φ : V (H) → {1,... ,k} such that for all adjacent vertices v,w of H, the edge density between Wφ(v) and Wφ(w) is at least ǫ and for all distinct nonadjacent vertices v,w of H, the edge density between Wφ(v) and Wφ(w) is at most 1 − ǫ, then the following standard counting lemma (see, e.g., Lemma 3.2 in Alon, Fischer, Krivelevich and Szegedy [6] for a minor variant) shows that G contains at least δnh induced copies of H, where δ = h1!(ǫ/4)(h2)δ′h. As with Lemma 2.4, the standard proof of this counting lemma uses a greedy embedding strategy.

![image 60](<2012-conlon-graph-removal-lemmas_images/imageFile60.png>)

![image 61](<2012-conlon-graph-removal-lemmas_images/imageFile61.png>)

- Lemma 3.3 If H is a graph with vertices 1,... ,h and G is a graph with not necessarily disjoint


vertex subsets W1,... ,Wh such that every pair (Wi,Wj) with 1 ≤ i < j ≤ h is γ-regular with γ ≤ η4hh, |Wi| ≥ γ−1 for 1 ≤ i ≤ h and, for 1 ≤ i < j ≤ k, d(Wi,Wj) > η if (i,j) is an edge of H and

![image 62](<2012-conlon-graph-removal-lemmas_images/imageFile62.png>)

d(Wi,Wj) < 1 − η otherwise, then G contains at least η4 (h2) |W1| × ··· × |Wh| induced copies of H with the copy of vertex i in Wi.

![image 63](<2012-conlon-graph-removal-lemmas_images/imageFile63.png>)

Hence, we may assume that there is no such mapping φ. We then delete the edges between Vi and Vj if the edge density between Wi and Wj is less than ǫ and add the edges between Vi and Vj if the density between Wi and Wj is more than 1 − ǫ. The total number of edges added or removed is at most 5ǫn2 and no induced copy of H remains. Replacing ǫ by ǫ/8 in the above argument gives the induced removal lemma.

## 3.2 An improved bound

The main goal of this section is to prove Theorem 1.5, which gives a bound on δ−1 which is a tower in h of height polynomial in ǫ−1. We in fact prove the key corollary of the strong regularity lemma,

- Lemma 3.2, with a tower-type bound. This is suﬃcient to prove the desired tower-type bound for the induced graph removal lemma.


As in Section 2.2, the key idea will be to take a weak variant of Szemere´di’s regularity lemma and iterate it. The particular variant we will use, due to Duke, Lefmann and Ro¨dl [28], was originally used by them to derive a fast approximation algorithm for the number of copies of a ﬁxed graph in a large graph.

A k-cylinder (or cylinder for short) in a graph G is a product of k vertex subsets. Given a k-partite graph G = (V,E) with k-partition V = V1 ∪ ... ∪ Vk, we will consider a partition K of the cylinder V1 × ··· × Vk into cylinders K = W1 × ··· × Wk, Wi ⊂ Vi for i = 1,... ,k and we let Vi(K) = Wi.

We say that a cylinder is ǫ-regular if all k2 pairs of subsets (Wi,Wj), 1 ≤ i < j ≤ k, are ǫ-regular. The partition K is ǫ-regular if all but an ǫ-fraction of the k-tuples (v1,... ,vk) ∈ V1 × ··· × Vk are in ǫ-regular cylinders in the partition K.

The weak regularity lemma of Duke, Lefmann and Ro¨dl [28] is now as follows. Note that, like the Frieze-Kannan weak regularity lemma, it has only a single-exponential bound on the number of parts. We will sometimes refer to this lemma as the cylinder regularity lemma.

- Lemma 3.4 Let 0 < ǫ < 1/2 and β = β(ǫ) = ǫk2ǫ−5. Suppose G = (V,E) is a k-partite graph with k-partition V = V1 ∪ ... ∪ Vk. Then there exists an ǫ-regular partition K of V1 × ··· × Vk into at most β−1 parts such that, for each K ∈ K and 1 ≤ i ≤ k, |Vi(K)| ≥ β|Vi|.

We would now like to iterate this lemma to get a stronger version, the strong cylinder regularity lemma. Like Lemmas 2.6 and 3.1, this will yield two closely related cylinder partitions P and Q with P regular and Q regular in a function of |P|. To state the lemma, we ﬁrst strengthen the deﬁnition of regular cylinders so that pieces are also regular with themselves.

A k-cylinder W1 ×··· × Wk is strongly ǫ-regular if all pairs (Wi,Wj) with 1 ≤ i,j ≤ k are ǫ-regular. A partition K of V1 ×···×Vk into cylinders is strongly ǫ-regular if all but ǫ|V1|×···×|Vk| of the k-tuples (v1,... ,vk) ∈ V1 × ··· × Vk are contained in strongly ǫ-regular cylinders K ∈ K.

We now state the strong cylinder regularity lemma. Here ti(x) is a variant of the tower function deﬁned by t0(x) = x and ti+1(x) = 2ti(x). Also, given a cylinder partition K, Q(K) is the coarsest vertex partition such that every set Vi(K) with i ∈ [k] and K ∈ K is the union of parts of Q(K).

- Lemma 3.5 For 0 < ǫ < 1/3, positive integer s, and decreasing function f : N → (0,ǫ], there is S = S(ǫ,s,f) such that the following holds. For every graph G, there is an integer s ≤ k ≤ S, an equitable

partition P : V = V1 ∪ ... ∪ Vk and a strongly f(k)-regular partition K of the cylinder V1 × ··· × Vk into cylinders satisfying that the partition Q = Q(K) of V has at most S parts and q(Q) ≤ q(P) + ǫ. Furthermore, there is an absolute constant c such that letting s1 = s and si+1 = t4 ((si/f(si))c), we may take S = sℓ with ℓ = 2ǫ−1 + 1.

To prove this lemma, we need to ﬁnd a way to guarantee that the parts of the cylinder partition are regular with themselves as required in the deﬁnition of strong cylinder regularity. For a graph

- G = (V,E), a vertex subset U ⊂ V is ǫ-regular if the pair (U,U) is ǫ-regular. The following lemma, which demonstrates that any graph contains a large vertex subset which is ǫ-regular, is the ﬁrst step.


- Lemma 3.6 For each 0 < ǫ < 1/2, let δ = δ(ǫ) = 2−ǫ−(10/ǫ)


4

. Every graph G = (V,E) contains an ǫ-regular vertex subset U with |U| ≥ δ|V |.

One way to prove this lemma is to ﬁrst ﬁnd a large collection C of disjoint subsets of equal order which are pairwise α-regular with α = (ǫ/3)2. This can be done by an application of Szemere´di’s regularity lemma and Tura´n’s theorem, but then the bounds are quite weak. Instead, one can easily deduce this from Lemma 3.4. A further application of Ramsey’s theorem allows one to get a subcollection C′ of size s ≥ 2α−1 such that the edge density between each pair of distinct subsets in C′ lies in an interval of length at most α. The union of the sets in C′ is then an ǫ-regular subset of the desired order.

It is crucial in this lemma that δ−1 be of bounded tower height in ǫ−1. While our bound gives a double exponential dependence, we suspect that the truth is more likely to be a single exponential. We leave this as an open problem.

Repeated applications of Lemma 3.6 allow us to pull out large, regular subsets until a small fraction of vertices remain. By distributing the remaining vertices amongst these subsets, we only slightly weaken their regularity, while giving a partition of any graph into large parts each of which is ǫ-regular with itself. This will be suﬃcient for our purposes.

- Lemma 3.7 For each 0 < ǫ < 1/2, let δ = δ(ǫ) = 2−ǫ−(20/ǫ)

4

. Every graph G = (V,E) has a vertex partition V = V1 ∪ ... ∪ Vk such that for each i, 1 ≤ i ≤ k, |Vi| ≥ δ|V | and Vi is an ǫ-regular set. We are now ready to prove the strong cylinder regularity lemma.

Proof of Lemma 3.5: We may assume |V | ≥ S, as otherwise we can let P and Q be the trivial partitions into singletons, and it is easy to see the lemma holds. We will deﬁne a sequence of partitions P1,P2,... of equitable partitions, with Pj+1 a reﬁnement of Pj and q(Pj+1) > q(Pj) + ǫ/2. Let P1 be an arbitrary equitable partition of V consisting of s1 = s parts. Suppose we have already found an equitable partition Pj : V = V1 ∪ ... ∪ Vk with k ≤ sj.

Let β(x,ℓ) = xℓ2x−5 as in Lemma 3.4 and δ(x) = 2−x−(20/x)

4

as in Lemma 3.7. We apply Lemma 3.7 to each part Vi of the partition Pj to get a partition of each part Vi = Vi1 ∪ ... ∪ Vihi of Pi into parts each of cardinality at least δ|Vi|, where δ = δ(γ) and γ = f(k) · β with β = β(f(k),k), such that each part Vih is γ-regular. Note that δ−1 is at most triple-exponential in a polynomial in k/f(k). For each k-tuple ℓ = (ℓ1,... ,ℓk) ∈ [h1] × ··· × [hk], by Lemma 3.4 there is an f(k)-regular partition Kℓ of the cylinder V1ℓ1 × ··· × Vkℓk into at most β−1 cylinders such that, for each K ∈ Kℓ, |Viℓi(K)| ≥ β|Viℓi|. The union of the Kℓ forms a partition K of V1 × ··· × Vk which is strongly f(k)-regular. Recall that Q = Q(K) is the partition of V which is the common reﬁnement of all parts Vi(K) with i ∈ [k] and K ∈ K. The number of parts of K is at most δ−kβ−1 and hence the number of parts of Q is at most k21/(δkβ). Thus, the number of parts of Q is at most quadruple-exponential in a polynomial in k/f(k). Let Pj+1 be an equitable partition into 4ǫ−1|Q| parts with q(Pj+1) ≥ q(Q)− 2ǫ, which exists by Lemma 2.3. Hence, there is an absolute constant c such that

![image 64](<2012-conlon-graph-removal-lemmas_images/imageFile64.png>)

|Pj+1| ≤ t4 ((k/f(k))c) ≤ sj+1.

If q(Q) ≤ q(Pj) + ǫ, then we may take P = Pj and Q = Q(K), and these partitions satisfy the desired properties. Otherwise, q(Pj+1) ≥ q(Q) − 2ǫ > q(Pj) + 2ǫ, and we continue the sequence of partitions. Since q(P1) ≥ 0 and the mean-square density goes up by more than ǫ/2 at each step and is always at most 1, this process must stop within 2/ǫ steps, and we obtain the desired partitions. ✷

![image 65](<2012-conlon-graph-removal-lemmas_images/imageFile65.png>)

![image 66](<2012-conlon-graph-removal-lemmas_images/imageFile66.png>)

Let G = (V,E), P : V = V1 ∪ ... ∪ Vk be an equipartition and K be a partition of the cylinder V1 ×···×Vk into cylinders. For K = W1 ×···×Wk ∈ K, deﬁne the density d(K) = |W|V1|×···×|Wk|

![image 67](<2012-conlon-graph-removal-lemmas_images/imageFile67.png>)

1|×···×|Vk| . The cylinder K is ǫ-close to P if |d(Wi,Wj) − d(Vi,Vj)| ≤ ǫ for all but at most ǫk2 pairs 1 ≤ i = j ≤ k. The cylinder partition K is ǫ-close to P if d(K) ≤ ǫ, where the sum is over all K ∈ K that are not ǫ-close to P. As with the deﬁnition of closeness used in the strong regularity lemma, this deﬁnition is closely related to the condition that q(Q) ≤ q(P) + ǫ, where here Q = Q(K).

The connection we shall need to prove Lemma 3.2 is contained in the following statement.

- Lemma 3.8 Let G = (V,E) and P : V = V1 ∪ ... ∪ Vk be an equipartition with k ≥ 2ǫ−1 and |V | ≥ 4kǫ−1. Let K be a partition of the cylinder V1 × ··· × Vk into cylinders. If Q = Q(K) satisﬁes q(Q) ≤ q(P) + ǫ, then K is (2ǫ)1/4-close to P.


Proof: It will be helpful to assume that all parts of the equipartition P have equal size - this aﬀects the calculations only slightly. It will also be helpful to introduce a slight variant of the mean-square density as follows. Let q′(P) = i<j d2(Vi,Vj)pij, where pij = |Vi||Vj|/ i<j |Vi||Vj|. Thus, q′(P) is the mean of the square densities between the pairs of distinct parts. It is easy to check that q′(P) is close to q(P). Indeed, we have q′(P)−q(P) = k1 (q′(P) − q¯), where q¯ = ki=1 d2(Vi)/k is the average of the square densities inside the parts. Hence, |q′(P)−q(P)| ≤ k1. We similarly have |q′(Q)−q(Q)| ≤ k1. Let

![image 68](<2012-conlon-graph-removal-lemmas_images/imageFile68.png>)

![image 69](<2012-conlon-graph-removal-lemmas_images/imageFile69.png>)

![image 70](<2012-conlon-graph-removal-lemmas_images/imageFile70.png>)

−1

k 2

d2(Vi(K),Vj(K))d(K).

q(K) =

i<j K∈K

We have the following equalities

q(K) − q′(P) =

=

k 2

k 2

−1

d2(Vi(K),Vj(K)) − d2(Vi,Vj) d(K)

i<j K∈K

−1

(d(Vi(K),Vj(K)) − d(Vi,Vj))2 d(K),

i<j K∈K

where the last equality uses the identity d(Vi,Vj) = K∈K d(Vi(K),Vj(K))d(K). This equality shows that q(K) ≥ q′(P) as it expresses their diﬀerence as a sum of nonnegative terms. Furthermore, it

shows that if K is not β-close to P, then q(K) ≥ q(P) + k2 −1 · βk22 · β2 · β ≥ q(P) + β4. In particular, if q(K) ≤ q′(P) +2ǫ, then K is (2ǫ)1/4-close to P. So assume for contradiction that q(K) > q′(P) +2ǫ.

![image 71](<2012-conlon-graph-removal-lemmas_images/imageFile71.png>)

A similar equality implies q′(Q) ≥ q(K). We therefore have q(Q) − q(P) = q(Q) − q′(Q) + q′(Q) − q(K) + q(K) − q′(P) + q′(P) − q(P) ≥ −

1 k

1 k

+ 0 + q(K) − q′(P) −

![image 72](<2012-conlon-graph-removal-lemmas_images/imageFile72.png>)

![image 73](<2012-conlon-graph-removal-lemmas_images/imageFile73.png>)

> ǫ, contradicting the assumption of Lemma 3.8 and completing the proof. ✷ With this in hand, we can readily deduce a tower-type bound for Lemma 3.2.

- Lemma 3.9 For each 0 < ǫ < 1/3 and decreasing function f : N → (0,ǫ], there is δ′ = δ′(ǫ,f) such that every graph G = (V,E) with |V | ≥ δ′−1 has an equitable partition V = V1 ∪ ... ∪ Vk and vertex subsets Wi ⊂ Vi such that |Wi| ≥ δ′|V |, each pair (Wi,Wj) with 1 ≤ i ≤ j ≤ k is f(k)-regular and all but at most ǫk2 pairs 1 ≤ i ≤ j ≤ k satisfy |d(Vi,Vj) − d(Wi,Wj)| ≤ ǫ. Furthermore, we may take δ′ = 8S12, where S = S(ǫ24,s,f) is deﬁned as in Lemma 3.5 and s = 2ǫ−1.


![image 74](<2012-conlon-graph-removal-lemmas_images/imageFile74.png>)

![image 75](<2012-conlon-graph-removal-lemmas_images/imageFile75.png>)

Proof: Let α = ǫ24, s = 2ǫ−1, and δ′ = 8S12, where S = S(α,s,f) is as in Lemma 3.5. We apply Lemma 3.5 with α in place of ǫ. We get an equipartition P : V = V1 ∪ ... ∪ Vk with s ≤ k ≤ S and a strongly f(k)-regular partition K of V1 × ··· × Vk into cylinders such that the reﬁnement Q = Q(K) of P has at most S = S(α,s,f) parts and satisﬁes q(Q) ≤ q(P) + α. Since |V | ≥ δ′−1 = 8S2, and

![image 76](<2012-conlon-graph-removal-lemmas_images/imageFile76.png>)

![image 77](<2012-conlon-graph-removal-lemmas_images/imageFile77.png>)

P is an equipartition into k ≤ S parts, the cardinality of each part Vi ∈ P satisﬁes |Vi| ≥ |2VS|. By Lemma 3.8, as (2α)1/4 = ǫ, the cylinder partition K is ǫ-close to P. Hence, at most an ǫ-fraction of

![image 78](<2012-conlon-graph-removal-lemmas_images/imageFile78.png>)

the k-tuples (v1,... ,vk) ∈ V1 × ··· × Vk belong to parts K = W1 × ··· × Wk of K that are not ǫ-close to P. Since Q(K) has at most S parts, the fraction of k-tuples (v1,... ,vk) ∈ V1 ×··· ×Vk that belong

to parts K = W1 × ··· × Wk of K with |Wi| < 41S|Vi| for at least one i ∈ [k] is at most 41S · S = 41. Therefore, at least a fraction 1 −f(k)−ǫ− 14 > 0 of the k-tuples (v1,... ,vk) ∈ V1 ×··· ×Vk belong to parts K = W1 × ··· × Wk of K satisfying K is strongly f(k)-regular, |Wi| ≥ 41S|Vi| ≥ δ′|V | for i ∈ [k] and K is ǫ-close to P. Since a positive fraction of the k-tuples belong to such K, there is at least one such K. This K has the desired properties. Indeed, the number of pairs 1 ≤ i = j ≤ k for which |d(Wi,Wj) − d(Vi,Vj)| > ǫ is at most ǫk2 and hence the number of pairs 1 ≤ i ≤ j ≤ k for which |d(Wi,Wj) − d(Vi,Vj)| > ǫ is at most ǫk2/2 + k ≤ ǫk2. This completes the proof. ✷

![image 79](<2012-conlon-graph-removal-lemmas_images/imageFile79.png>)

![image 80](<2012-conlon-graph-removal-lemmas_images/imageFile80.png>)

![image 81](<2012-conlon-graph-removal-lemmas_images/imageFile81.png>)

![image 82](<2012-conlon-graph-removal-lemmas_images/imageFile82.png>)

![image 83](<2012-conlon-graph-removal-lemmas_images/imageFile83.png>)

By using the induced counting lemma, Lemma 3.3, we may now conclude the proof as in Section 3.1 to obtain the following quantitative version of Theorem 1.3.

- Theorem 3.1 There exists a constant c such that, for any graph H on h vertices and 0 < ǫ < 1/2,


if δ−1 = tj(h), where j = cǫ−4, then any graph G on n vertices with at most δnh induced copies of H may be made induced H-free by adding and/or deleting at most ǫn2 edges.

## 3.3 Inﬁnite removal lemma

In order to characterize the natural graph properties which are testable, the induced removal lemma was extended by Alon and Shapira [12] to the following inﬁnite version. For a family H of graphs, a graph G is induced H-free if G does not contain any graph H in H.

- Theorem 3.2 For every (possibly inﬁnite) family of graphs H and ǫ > 0, there are n0, h0, and δ such that the following holds. If a graph G = (V,E) on n ≥ n0 vertices has at most δnh induced copies of each graph H ∈ H on h ≤ h0 vertices, then G can be made induced H-free by adding and/or deleting at most ǫn2 edges.


Proof: The proof is a natural extension of the proof of the induced removal lemma and similarly uses the key corollary, Lemma 3.2, of the strong regularity lemma. The main new idea is to pick an appropriate function f to apply Lemma 3.2. The choice of the function f will depend heavily on the family H.

For a graph H and an edge-coloring c of the edges of the complete graph with loops R on [k] with colors white, black and grey, we write H →c R if there is a mapping φ : V (H) → [k] such that for each edge (u,v) of H we have that c(φ(u),φ(v)) is black or grey and for each pair (u,v) of distinct vertices of H which do not form an edge we have that c(φ(u),φ(v)) is white or grey. We write H  →c R if

- H →c R does not hold.


Let P : V = V1 ∪ ... ∪ Vk be a vertex partition of G. A key observation is that if we round G by the partition P and the coloring c to obtain a graph G′ on the same vertex set as G by adding edges to make (Vi,Vj) complete if (i,j) is black, deleting edges to make (Vi,Vj) empty if (i,j) is white and we have that H  →c R, then G′ does not contain H as an induced subgraph.

For any (possibly inﬁnite) family of graphs H and any integer r, let Hr be the following set of colored complete graphs with loops: a colored complete graph with loops R belongs to Hr if and only if it has at most r vertices and there is at least one H ∈ H such that H →c R. For any family H of graphs and integer r for which Hr = ∅, let

|V (H)|.

min

ΨH(r) = max R∈Hr

H∈H:H→cR

If Hr = ∅, deﬁne ΨH(r) = 1. Note that ΨH(r) is a monotonically increasing function of r. Let

ǫΨH(r) 4ΨH(r)

f(r) =

.

![image 84](<2012-conlon-graph-removal-lemmas_images/imageFile84.png>)

Note that the function f only depends on ǫ and H. Let δ′ = δ′(ǫ,f) be as in Lemma 3.2, which only depends on ǫ and H. Also let k0 = 2δ′−1, h0 = ΨH(k0),

0!(ǫ/4)h20δ′h0. We have that k0, h0, n0 and δ > 0 only depend on ǫ and H. By assumption, G has n ≥ n0 vertices.

- n0 = 1/(δ′f(k0)) and δ = h1


![image 85](<2012-conlon-graph-removal-lemmas_images/imageFile85.png>)

We apply Lemma 3.2 to G. We get an equitable vertex partition P : V = V1∪...∪Vk of G and subsets Wi ⊂ Vi with |Wi| ≥ δ′|V | such that, for 1 ≤ i ≤ j ≤ k, the pair (Wi,Wj) is f(k)-regular and all but at most ǫk2 pairs 1 ≤ i ≤ j ≤ k satisfy |d(Vi,Vj) − d(Wi,Wj)| ≤ ǫ. As δ′|V | ≤ |Wi| ≤ |Vi| ≤ 2n/k, we have k ≤ 2δ′−1 ≤ k0.

Consider the coloring c of the complete graph with loops R on [k] where a pair (i,j) of vertices is black if d(Wi,Wj) ≥ 1 − ǫ, white if d(Wi,Wj) ≤ ǫ and grey if ǫ < d(Wi,Wj) < 1 − ǫ. Suppose, for the sake of contradiction, that there is a graph H with H →c R. From the deﬁnition of Ψ, there is a graph H on h ≤ ΨH(k) vertices with H →c R. As k ≤ k0, the number of vertices of H satisﬁes h ≤ h0. As each pair (Wi,Wj) is f(k)-regular and |Wi| ≥ δ′|V | ≥ f(k)−1, applying the induced counting lemma,

- Lemma 3.3, with γ = f(k), we get at least 1 h!

![image 86](<2012-conlon-graph-removal-lemmas_images/imageFile86.png>)

ǫ 4

![image 87](<2012-conlon-graph-removal-lemmas_images/imageFile87.png>)

(h2)

(δ′|V |)h ≥ δnh

induced copies of H in G, contradicting the supposition of the theorem. Thus, there is no graph H with H →c R. We round the graph G by the partition P and the coloring c as described earlier in the proof to obtain a graph G′. By the key observation, for each graph H with H  →c R, the graph G′ does not contain H as an induced subgraph. Hence, G′ is induced H-free.

Moreover, not many edges were changed from G to obtain G′. Indeed, as there are at most ǫk2 pairs 1 ≤ i ≤ j ≤ k which satisfy |d(Vi,Vj) − d(Wi,Wj)| > ǫ, the number of edge modiﬁcations made between such pairs is at most ǫk2 · (2n/k)2 = 4ǫn2. Between the other pairs we have made at most 2ǫ n2 ≤ ǫn2 edge modiﬁcations. In total, at most 5ǫn2 edge modiﬁcations were made to obtain G′ from G. Replacing ǫ by ǫ/5 in the above argument completes the proof. ✷

- 4 Arithmetic removal


The notion of arithmetic removal was introduced by Green [57]. By establishing an appropriate variant of the regularity lemma in the context of abelian groups, he proved the following result.

- Theorem 4.1 For any natural number k ≥ 3 and any ǫ > 0, there exists δ > 0 such that if G is an abelian group of order n and A1,... ,Ak are subsets of G such that there are at most δnk−1 solutions to the equation a1+a2+···+ak = 0 with ai ∈ Ai for all i then it is possible to remove at most ǫn elements from each set Ai to form sets A′i so that there are no solutions to the equation a′1 + a′2 + ··· + a′k = 0 with a′i ∈ A′i for all i.


It is an exercise to show that Green’s result implies Roth’s theorem. While Green’s proof of this result relied on Fourier analytic techniques, an alternative proof was found by Kra´l’, Serra, and Vena [70], who showed that the following more general result follows from an elegant reduction to the removal lemma in directed graphs.

- Theorem 4.2 For any natural number k ≥ 3 and any ǫ > 0, there exists δ > 0 such that if G is a group of order n, g ∈ G and A1,... ,Ak are subsets of G such that there are at most δnk−1 solutions to the equation a1a2 ··· ak = g with ai ∈ Ai for all i then it is possible to remove at most ǫn elements from each set Ai to form sets A′i so that there are no solutions to the equation a′1a′2 ··· a′k = g with a′i ∈ A′i for all i.


This is stronger than Theorem 4.1 in two ways. Firstly, it applies to all groups and not just to abelian groups. Secondly, it applies to non-homogeneous equations, that is, a1a2 ··· ak = g for a general g, whereas Green only treats the homogeneous case where g = 1. To give some idea of their proof, we will need the following deﬁnition.

A directed graph is a graph where each edge has been given a direction. Formally, the edge set may be thought of as a collection of ordered pairs. We will always assume that the directed graph has no loops and does not contain parallel directed edges, though we do allow anti-parallel edges, that is, both the edge u v and the edge v u. The following analogue of the graph removal lemma for directed graphs was proved by Alon and Shapira [9] as part of their study of property testing in directed graphs.

- Theorem 4.3 For any directed graph H and any ǫ > 0, there exists δ > 0 such that any directed graph on n vertices which contains at most δnv(H) copies of H may be made H-free by removing at most ǫn2 edges.


We will show how to prove Theorem 4.2 with g = 1 using Theorem 4.3. Suppose that G is a group of order n and A1,... ,Ak are subsets of G such that there are at most δnk−1 solutions to the equation a1a2 ··· ak = 1 with ai ∈ Ai for all i. Consider the auxiliary directed graph Γ whose vertex set is

- G ×{1,2,... ,k}. We place an edge from (x,i) to (y,i +1), where addition is taken modulo k, if there exists ai ∈ Ai such that xai = y. It is easy to see that any directed cycle in Γ corresponds to a solution of the equation a1a2 ··· ak = 1. Moreover, every such solution will result in n diﬀerent directed cycles in Γ, namely, those with vertices (x,1),(xa1,2),(xa1a2,3),... ,(xa1 ··· ak−1,k). Since G has at most δnk−1 solutions to a1a2 ··· ak = 1, this implies that there are at most δnk directed cycles in Γ. By Theorem 4.3, for an appropriately chosen δ, we may therefore remove at most kǫ n2 edges to make it free of directed cycles of length k. In Ai, we now remove the element ai if at least nk edges of the form (x,i)(xai,i+1) have been removed. Note that this results in us removing at most ǫn elements from each Ai. Suppose now that the remaining sets A′i are such that there is a solution a′1a′2 ... a′k = 1


![image 88](<2012-conlon-graph-removal-lemmas_images/imageFile88.png>)

![image 89](<2012-conlon-graph-removal-lemmas_images/imageFile89.png>)

with a′i ∈ A′i for all i. Then, as above, there are at least n cycles (x,1),(xa′1,2),... ,(xa′1 ··· a′k−1,k) corresponding to this solution. Since we must have removed one edge from each of these cycles, we

must have removed at least nk edges of the form (y,i)(ya′i,i + 1) for some i. But this implies that a′i  ∈ A′i, yielding the required contradiction.

![image 90](<2012-conlon-graph-removal-lemmas_images/imageFile90.png>)

It was observed by Fox [38] that δ−1 in Theorem 4.3 may, like the graph removal lemma, be taken to be at most a tower of twos of height logarithmic in ǫ−1. This may in turn be used to give a similar bound for δ−1 in Theorem 4.2.

In [70], Kra´l’, Serra and Vena also showed how to prove a removal lemma for systems of equations which are graph representable, in the sense that they can be put in a natural correspondence with a

directed graph. An example of such a system is

x1x2x−4 1x−3 1 = 1 x1x2x−5 1 = 1.

This idea of associating a system of linear equations with a directed graph representation was extended to hypergraphs independently by Kra´l’, Serra and Vena [71] and by Shapira [100, 101] in order to prove the following theorem (some partial results had been obtained earlier by Kra´l’, Serra and Vena [69], Szegedy [108] and Candela [20]).

- Theorem 4.4 For any natural numbers k and ℓ and any ǫ > 0, there exists δ > 0 such that if F is the ﬁeld of size n, M is an ℓ × k matrix with coeﬃcients in F, b ∈ Fℓ and A1,... ,Ak are subsets

- of F such that there are at most δnk−ℓ solutions a = (a1,... ,ak) of the system Ma = b then it is possible to remove at most ǫn elements from each set Ai to form sets A′i so that there are no solutions a′ = (a′1,... ,a′k) to the equation Ma′ = b with a′i ∈ A′i for all i.


An easy application of this result shows that a removal lemma for systems of linear equations holds in the set [n], conﬁrming a conjecture of Green [57]. We remark that this result easily implies Szemere´di’s theorem. Both proofs use a colored variant of the hypergraph removal lemma due to Austin and Tao [13], though the representations which they use to transfer the problem to hypergraphs are diﬀerent. It would be interesting to know whether an analogous statement holds for all groups. A partial extension of these results to abelian groups is proved in [72] (see also [108]) but already in this case there are technical diﬃculties which do not arise for ﬁnite ﬁelds.

- 5 Sparse removal


Given graphs Γ and H, let NH(Γ) be the number of copies of H in Γ. A possible generalization of the graph removal lemma, which corresponds to the case Γ = Kn, could state that if G is a subgraph of Γ with NH(G) ≤ δNH(Γ) then G may be made H-free by deleting at most ǫe(Γ) edges. Unfortunately, this is too much to hope in general. However, if the graph Γ is suﬃciently well-behaved, such an extension does hold. We will discuss two such results here.

## 5.1 Removal in random graphs

The binomial random graph Gn,p is formed by taking n vertices and considering each pair of vertices in turn, choosing each connecting edge to be in the graph independently with probability p. These graphs were introduced by Erd˝os and Re´nyi [33, 34] in the late ﬁfties10 and their study has grown enormously since then (see, for example, the monographs [17, 60]).

Usually, one is interested in ﬁnding a threshold function p∗ := p∗(n) where the probability that the random graph Gn,p has a particular property P changes from o(1) to 1−o(1) as we pass from random graphs chosen with probability p ≪ p∗ to those chosen with probability p ≫ p∗. For example, the threshold for the random graph to be connected is at p∗(n) = lnnn.

![image 91](<2012-conlon-graph-removal-lemmas_images/imageFile91.png>)

![image 92](<2012-conlon-graph-removal-lemmas_images/imageFile92.png>)

10The notion was also introduced independently by several other authors at about the same time but, quoting Bollob´s [17], “Erd˝os and Re´nyi introduced the methods which underlie the probabilistic treatment of random graphs. The other authors were all concerned with enumeration problems and their techniques were essentially deterministic.”

One theme that has received a lot of attention in recent years is the question of determining thresholds for the appearance of certain combinatorial properties. One well-studied example is the Ramsey property. Given a graph H and a natural number r ≥ 2, we say that a graph G is (H,r)-Ramsey if in any r-coloring of the edges of G there is guaranteed to be a monochromatic copy of H. Ramsey’s theorem [82] is itself the statement that Kn is (H,r)-Ramsey for n suﬃciently large. The following celebrated result of Ro¨dl and Rucin´ski [83, 84] from 1995 (see also [60], Chapter 8) determines the threshold for the appearance of the Ramsey property in random graphs.

- Theorem 5.1 For any graph H that is not a forest consisting of stars and paths of length 3 and every positive integer r ≥ 2, there exist constants c,C > 0 such that


lim

P Gn,p is (H,r)-Ramsey =

n→∞

- 0, if p < cn−1/m2(H),
- 1, if p > Cn−1/m2(H),


where

m2(H) = max

e(H′) − 1 v(H′) − 2

: H′ ⊆ H and v(H′) ≥ 3 .

![image 93](<2012-conlon-graph-removal-lemmas_images/imageFile93.png>)

The threshold occurs at the largest value of p∗ such that there is some subgraph H′ of H for which the number of copies of H′ is approximately the same as the number of edges. For p signiﬁcantly smaller than p∗, the number of copies of H′ will also be signiﬁcantly smaller than the number of edges. This property allows us (by a rather long and diﬃcult argument [83]) to show that the edges of the graph may be colored in such a way as to avoid any monochromatic copies of H′. For p signiﬁcantly larger than p∗, every edge of the random graph is contained in many copies of every subgraph of H. The intuition, which takes substantial eﬀort to make rigorous [84], is that these overlaps are enough to force the graph to be Ramsey.

Many related questions were studied in the late nineties. In particular, people were interested in determining the threshold for the following Tura´n property. Given a graph H and a real number ǫ > 0, we say that a graph G is (H,ǫ)-Tura´n if every subgraph of G with at least

1 χ(H) − 1

1 −

+ ǫ e(G)

![image 94](<2012-conlon-graph-removal-lemmas_images/imageFile94.png>)

edges contains a copy of H. The classical Erd˝os-Stone-Simonovits theorem [35, 36, 115] states that the graph Kn is (H,ǫ)-Tura´n for n suﬃciently large. Resolving a conjecture of Haxell, Kohayakawa,  Luczak and Ro¨dl [58, 65], Conlon and Gowers [25] and, independently, Schacht [98] proved the following theorem. It is worth noting that the result of Conlon and Gowers applies in the strictly balanced case, that is, when m2(H′) < m2(H) for all H′ ⊂ H, while Schacht’s result applies to all graphs. However, the class of strictly balanced graphs includes most of the graphs one would naturally consider, such

- as cliques or cycles.


- Theorem 5.2 For any graph H11 and any ǫ > 0, there exist positive constants c and C such that


lim

P Gn,p is (H,ǫ)-Tura´n =

n→∞

![image 95](<2012-conlon-graph-removal-lemmas_images/imageFile95.png>)

11Note that if H = K2, we take m2(H) = 12.

![image 96](<2012-conlon-graph-removal-lemmas_images/imageFile96.png>)

- 0, if p < cn−1/m2(H),
- 1, if p > Cn−1/m2(H).


The results of [25] and [98] (see also [43]) allow one to prove thresholds for the appearance of many diﬀerent combinatorial properties. For example, the results extend without diﬃculty to prove analogues of Theorems 5.1 and 5.2 for hypergraphs. The results also apply to give thresholds in diﬀerent contexts - one example is an extension of Szemere´di’s theorem to random subsets of the integers.

Perhaps surprisingly, the methods used in [25] and [98] are very diﬀerent and have diﬀerent strengths and weaknesses. We have already mentioned that Schacht’s results applied to all graphs while the results of Conlon and Gowers only applied to strictly balanced graphs. On the other hand, the results of [25] also allowed one to transfer structural statements to the sparse setting, including the stability version of the Erd˝os-Stone-Simonovits theorem [103] and the graph removal lemma. More recently, Samotij [94] modiﬁed Schacht’s method to extend this sparse stability theorem to all graphs. The result is the following theorem.

- Theorem 5.3 For any graph H and any ǫ > 0, there exist positive constants δ and C such that if p ≥ Cn−1/m2(H) then the following holds a.a.s. in Gn,p. Every H-free subgraph of Gn,p with at least

1 − χ(H1)−1 − δ p n2 edges may be made (χ(H) − 1)-partite by deleting at most ǫpn2 edges.

![image 97](<2012-conlon-graph-removal-lemmas_images/imageFile97.png>)

Recently, a third method was developed by Balogh, Morris and Samotij [15] and, simultaneously and independently, by Saxton and Thomason [97] for proving sparse random analogues of combinatorial theorems. One of the results of their research is a proof of the K LR conjecture of Kohayakawa,  Luczak and Ro¨dl [65]. This is a technical statement which allows one to prove an embedding lemma complementing the sparse regularity lemma of Kohayakawa [63] and Ro¨dl. A variant of this conjecture has also been proved by Conlon, Gowers, Samotij and Schacht [26] using the methods of [25, 98]. One of the applications of this latter result is the following sparse random analogue of the graph removal lemma (this was already proved for triangles in [64] and for strictly balanced graphs in [25]).

- Theorem 5.4 For any graph H and any ǫ > 0, there exist positive constants δ and C such that if


p ≥ Cn−1/m2(H) then the following holds a.a.s. in Gn,p. Every subgraph of Gn,p which contains at most δpe(H)nv(H) copies of H may be made H-free by removing at most ǫpn2 edges.

Note that for any ǫ there exists a positive constant c such that if p ≤ cn−1/m2(H), the removal lemma is trivial. This is because, for c suﬃciently small, the number of copies of the densest subgraph H′ of

- H will a.a.s. be smaller than ǫpn2. Theorem 5.4 shows that it also holds for p ≥ Cn−1/m2(H). This leaves a small intermediate range of p where it might also be expected that a sparse removal lemma a.a.s. holds. That this is so was conjectured by  Luczak [76].


For balanced graphs H, we may close the gap by letting δ be suﬃciently small depending on C,ǫ and H. Indeed, as p ≤ Cn−1/m2(H), the number of copies of H is a.a.s. on the order of pe(H)nv(H) ≤ Ce(H)pn2. Therefore, taking δ < ǫC−e(H), we see that the number of copies of H is a.a.s. less than ǫpn2. Deleting one edge from each copy of H in the graph then makes it H-free.

A sparse random analogue of the hypergraph removal lemma was proved in [25] when H = Kk(k+1) . This result also extends to cover all strictly balanced hypergraphs.12 It would be interesting to extend this

result to all hypergraphs.

It is worth noting that the sparse random version of the triangle removal lemma does not imply a sparse random version of Roth’s theorem. This is because the reduction which allows us to pass from

![image 98](<2012-conlon-graph-removal-lemmas_images/imageFile98.png>)

12We note that for k-uniform hypergraphs the relevant function is mk(H) = max v e((HH′′))−−1k , where the maximum is taken over all subgraphs H′ of H with at least k + 1 vertices.

![image 99](<2012-conlon-graph-removal-lemmas_images/imageFile99.png>)

a subset of the integers with no arithmetic progressions of length 3 to a graph containing few triangles gives us a graph with dependencies between its edges. This issue does not occur with pseudorandom graphs, which we discuss in the next section.

## 5.2 Removal in pseudorandom graphs

Though there have long been explicit examples of graphs which behave like the random graph Gn,p, the ﬁrst systematic study of what it means for a given graph to be like a random graph was initiated by Thomason [113, 114]. Following him,13 we say that a graph on vertex set V is (p,β)-jumbled if, for all vertex subsets X,Y ⊆ V ,

![image 100](<2012-conlon-graph-removal-lemmas_images/imageFile100.png>)

|e(X,Y ) − p|X||Y || ≤ β |X||Y |.

The random graph Gn,p is, with high probability, (p,β)-jumbled with β = O(√pn). This is also optimal in that a graph on n vertices with p ≤ 1/2 cannot be (p,β)-jumbled with β = o(√pn). The Paley graph is an example of an explicit graph which is optimally jumbled. This graph has vertex set Zp, where p ≡ 1(mod 4) is prime, and edge set given by connecting x and y if their diﬀerence is a quadratic residue. It is (p,β)-jumbled with p = 12 and β = O(√n). Many more examples are given in the excellent survey [73].

![image 101](<2012-conlon-graph-removal-lemmas_images/imageFile101.png>)

![image 102](<2012-conlon-graph-removal-lemmas_images/imageFile102.png>)

![image 103](<2012-conlon-graph-removal-lemmas_images/imageFile103.png>)

![image 104](<2012-conlon-graph-removal-lemmas_images/imageFile104.png>)

A fundamental result of Chung, Graham and Wilson [22] states that for graphs of density p, where p is a ﬁxed positive constant, the property of being (p,o(n))-jumbled is equivalent to a number of other properties that one would typically expect in a random graph. For example, if the number of cycles of length 4 is as one would expect in a binomial random graph then, surprisingly, this is enough to imply that the edges are very well-spread.

For sparser graphs, the equivalences are less clear cut, but the notion of jumbledness deﬁned above is a natural property to study. Given a graph property P that one would expect of a random graph, one can ask for the range of p and β for which a (p,β)-jumbled graph satisﬁes P.

To give an example, it is known that there is a constant c such that if β ≤ cp2n then any (p,β)-jumbled graph contains a triangle. It is also known that this is sharp, since an example of Alon [2] gives a triangle-free graph with p = Ω(n−1/3) which is optimally jumbled, so that β = O(√pn) = O(p2n).

![image 105](<2012-conlon-graph-removal-lemmas_images/imageFile105.png>)

As in the previous section, one can ask for conditions on p and β which guarantee that a (p,β)-jumbled graph satisﬁes certain combinatorial properties. For the property of being (K3,ǫ)-Tura´n, this question was addressed by Sudakov, Szabo´ and Vu [107] (see also [21]), who showed that it was enough that β ≤ cp2n for an appropriate c. This is clearly sharp, since for larger values of β we cannot even guarantee that the graph contains a triangle. More generally, they proved the following theorem.14

- Theorem 5.5 For any natural number t ≥ 3 and any ǫ > 0, there exists c > 0 such that if β ≤ cpt−1n then any (p,β)-jumbled graph is (Kt,ǫ)-Tura´n.


Except in the case of triangles, there are no known constructions which demonstrate that this theorem is tight. However, it is conjectured [107] that the bound on β in Theorem 5.5 is the correct condition for ﬁnding copies of Kt in a (p,β)-jumbled graph. This would in turn imply that Theorem 5.5 is tight.

![image 106](<2012-conlon-graph-removal-lemmas_images/imageFile106.png>)

- 13Strictly speaking, Thomason considered a slightly diﬀerent notion, namely, that |e(X)−p |X2| | ≤ β|X| for all X ⊆ V , but the two are closely related.
- 14Their results were only stated for the special class of (p, β)-jumbled graphs known as (n, d, λ)-graphs. These are graphs on n vertices which are d-regular and such that all eigenvalues of the adjacency matrix, save the largest, have absolute value at most λ. The expander mixing lemma implies that these graphs are (p, β)-jumbled with p = nd and β = λ. However, it is not hard to verify that their method applies in the more general case.


![image 107](<2012-conlon-graph-removal-lemmas_images/imageFile107.png>)

For the triangle removal lemma, the following pseudorandom analogue was recently proved by Kohayakawa, Ro¨dl, Schacht and Skokan [68].

- Theorem 5.6 For any ǫ > 0, there exist positive constants δ and c such that if β ≤ cp3n then any (p,β)-jumbled graph G on n vertices has the following property. Any subgraph of G containing at most δp3n3 triangles may be made triangle-free by removing at most ǫpn2 edges.

The condition on β in this theorem is stronger than that employed for triangles in Theorem 5.5. As a result, Alon’s construction does not apply and it is an open problem to determine whether the condition β ≤ cp3n is optimal or if it can be improved to β ≤ cp2n. Kohayakawa, Ro¨dl, Schacht and Skokan conjecture the latter, though we feel that the former is a genuine possibility.

In a recent paper, Conlon, Fox and Zhao [27] found a way to prove a counting lemma for embedding any ﬁxed small graph into a regular subgraph of a suﬃciently pseudorandom host graph. Like the K LR conjecture for random graphs, this serves to complement the sparse regularity lemma of Kohayakawa [63] and Ro¨dl in the pseudorandom context. As corollaries, they extended Theorems 5.5 and 5.6 to all graphs and proved sparse pseudorandom extensions of several other theorems, including Ramsey’s theorem and the Erd˝os-Simonovits stability theorem.

To state these theorems, we deﬁne the degeneracy d(H) of a graph H to be the smallest nonnegative integer d for which there exists an ordering of the vertices of H such that each vertex has at most d neighbors which appear earlier in the ordering. Equivalently, it may be deﬁned as d(H) = max{δ(H′) : H′ ⊆ H}, where δ(H) is the minimum degree of H.15

The pseudorandom analogue of the graph removal lemma proved in [27] is now as follows.16

- Theorem 5.7 For any graph H and any ǫ > 0, there exist positive constants δ and c such that if β ≤ cpd(H)+52n then any (p,β)-jumbled graph G on n vertices has the following property. Any subgraph


![image 108](<2012-conlon-graph-removal-lemmas_images/imageFile108.png>)

- of G containing at most δpe(H)nv(H) copies of H may be made H-free by removing at most ǫpn2 edges.


It is not hard to show, by using the random graph, that there are (p,β)-jumbled graphs with β = O(p(d(H)+2)/4n) which contain no copies of H. We therefore see that the exponent of p is sharp up to a multiplicative constant. However, in many cases, we expect it to be sharp up to an additive constant. For certain classes of graph, Theorem 5.7 can be improved. For example, if we know that the degeneracy of the graph is the same as the maximum degree, such as what happens for the complete graph Kt, it is suﬃcient that β ≤ cpd(H)+1n. In particular, for K3, we reprove Theorem 5.6. For cycles, the improvement is even more pronounced, since β ≤ cptℓn, where t3 = 3, t4 = 2, tℓ = 1 + ℓ−13 if ℓ ≥ 5 is odd and tℓ = 1 + ℓ−14 if ℓ ≥ 6 is even, is suﬃcient for removing the cycle Cℓ. By following the proof of Kra´l’, Serra and Vena [70], these bounds on the cycle removal lemma in pseudorandom graphs17 allow us to prove an analogue of Theorem 4.2 for pseudorandom subsets of any group G. The Cayley graph G(S) of a subset S of a group G has vertex set G and (x,y) is an edge of G if x−1y ∈ S. We say that a subset S of a group G is (p,β)-jumbled if the Cayley graph G(S) is

![image 109](<2012-conlon-graph-removal-lemmas_images/imageFile109.png>)

![image 110](<2012-conlon-graph-removal-lemmas_images/imageFile110.png>)

![image 111](<2012-conlon-graph-removal-lemmas_images/imageFile111.png>)

- 15In [27], a slightly diﬀerent parameter, the 2-degeneracy d2(H), is used. Though there are many cases in which this parameter is more appropriate, the degeneracy will be suﬃcient for the purposes of our discussion here.
- 16For other properties, such as that of being (H,r)-Ramsey or that of being (H,ǫ)-Tur´an, an exactly analogous theorem holds with the same condition β ≤ cpd(H)+52 n. Any of the improvements subsequently discussed for speciﬁc graphs H also apply for these properties.

![image 112](<2012-conlon-graph-removal-lemmas_images/imageFile112.png>)

- 17Rather, a colored or directed version of this theorem.


(p,β)-jumbled. When G is abelian, if x∈S χ(x) ≤ β for all nontrivial characters χ: G → C, then S is (||GS||,β)-jumbled (see [68, Lemma 16]).

![image 113](<2012-conlon-graph-removal-lemmas_images/imageFile113.png>)

- Theorem 5.8 For any natural number k ≥ 3 and any ǫ > 0, there exist positive constants δ and c such that the following holds. Suppose B1,... ,Bk are subsets of a group G of order n such that each Bi is (p,β)-jumbled with β ≤ cptkn. If subsets Ai ⊆ Bi for i = 1,... ,k are such that there are at most δ|B1|··· |Bk|/n solutions to the equation x1x2 ··· xk = 1 with xi ∈ Ai for all i, then it is possible to remove at most ǫ|Bi| elements from each set Ai so as to obtain sets A′i for which there are no solutions to x1x2 ··· xk = 1 with xi ∈ A′i for all i.


This result easily implies a Roth-type theorem in quite sparse pseudorandom subsets of a group. We say that a subset B of a group G is (ǫ,k)-Roth if, for all integers a1,... ,ak which satisfy a1+···+ak = 0 and gcd(ai,|G|) = 1 for 1 ≤ i ≤ k, every subset A ⊆ B which has no nontrivial solution to xa11xa22 ··· xakk = 1 has |A| ≤ ǫ|B|.

Corollary 5.1 For any natural number k ≥ 3 and any ǫ > 0, there exists c > 0 such that the following holds. If G is a group of order n and B is a (p,β)-jumbled subset of G with β ≤ cptkn, then B is (ǫ,k)-Roth.

Note that Roth’s theorem on 3-term arithmetic progressions in dense sets of integers follows from the special case of this result with B = G = Zn, k = 3 and a1 = a2 = 1, a3 = −2. The rather weak pseudorandomness condition in Corollary 5.1 shows that even quite sparse pseudorandom subsets of

- a group have the Roth property.


# 6 Further topics

## 6.1 The Erdo˝s-Rothschild problem

A problem of Erd˝os and Rothschild [30] asks one to estimate the maximum number h(n,c) such that every n-vertex graph with at least cn2 edges, each of which is contained in at least one triangle, must contain an edge that is in at least h(n,c) edges. Here, and throughout this subsection, we assume c > 0 is a ﬁxed absolute constant. The fact that h(n,c) tends to inﬁnity already follows from the triangle removal lemma.18

To see this, suppose that G is an n-vertex graph with cn2 edges such that every edge is in at least one and at most h := h(n,c) triangles. The total number of triangles in G is at most hcn2/3. Therefore, if h does not tend to inﬁnity, the triangle removal lemma tells us that there is a collection E of o(n2) edges such that every triangle contains at least one of them. Since each edge in G is in at least one triangle, we know that there are at least cn2/3 triangles. It follows that some edge in E is contained in at least ω(1) edges.

Using Fox’s bound [38] for the triangle removal lemma, this implies that h(n,c) ≥ ealog∗ n, where log∗ n is the iterated logarithm. This is deﬁned by log∗ x = 0 if x ≤ 1 and log∗ x = log∗(log x) + 1 otherwise. This improves on the bound h(n,c) ≥ (log∗ n)a which follows from Ruzsa and Szemere´di’s original proof of the triangle removal lemma.

![image 114](<2012-conlon-graph-removal-lemmas_images/imageFile114.png>)

18Even the statement that h(n, c) > 1 is already enough to imply Roth’s theorem.

On the other hand, Alon and Trotter (see [31]) showed that for any positive c < 14 there is c′ > 0 such that h(n,c) < c′√n. The condition c < 14 is easily seen to be best possible since any n-vertex graph with more than n2/4 edges contains an edge in at least n/6 triangles [29, 62]. Erd˝os conjectured that perhaps this behaviour is correct. That is, that for any positive c < 41 there exists ǫ > 0 such that h(n,c) > nǫ for all suﬃciently large n. This was recently disproved by Fox and Loh [39] as follows.

![image 115](<2012-conlon-graph-removal-lemmas_images/imageFile115.png>)

![image 116](<2012-conlon-graph-removal-lemmas_images/imageFile116.png>)

![image 117](<2012-conlon-graph-removal-lemmas_images/imageFile117.png>)

![image 118](<2012-conlon-graph-removal-lemmas_images/imageFile118.png>)

- Theorem 6.1 For n suﬃciently large, there is an n-vertex graph with n42(1 − e−(logn)1/6) edges such that every edge is in a triangle and no edge is in more than n14/log logn triangles.


![image 119](<2012-conlon-graph-removal-lemmas_images/imageFile119.png>)

To give some idea of the construction, consider a tripartite graph between sets A, B and C, each of which is a copy of a lattice cube with appropriate sidelength r and dimension d. We join points in A and B if their distance is close to the expected distance between random points in A and B. By concentration, this implies that the density of edges between A and B is close to 1. We join points in C to points in A or B if their distance is close to half the expected distance. It is not hard to see that every edge between A and B is then contained in few triangles. At the same time, every edge will be in at least one triangle, as can be seen by considering the midpoint of any two connected points a and

- b. This yields a construction with roughly n92 edges but the result of Fox and Loh may be obtained by shrinking the vertex set C (or blowing up A and B) in an appropriate fashion.


![image 120](<2012-conlon-graph-removal-lemmas_images/imageFile120.png>)

## 6.2 Induced matchings

Call a graph G = (V,E) an (r,t)-Ruzsa-Szemere´di graph ((r,t)-RS graph for short) if its edge set can be partitioned into t induced matchings in G, each of size r. The total number of edges of such a graph is rt. The most interesting problem concerns the existence of such graphs when r and t are both relatively large as a function of the number of vertices. The construction of Ruzsa and Szemere´di [93] using Behrend’s construction demonstrates that such a graph on n vertices exists with r = e−c

√lognn and t = n/3. The Ruzsa-Szemere´di result on the (6,3)-problem is equivalent to showing that no (r,t)-RS graph on n vertices exists with r and t linear in n.

![image 121](<2012-conlon-graph-removal-lemmas_images/imageFile121.png>)

For r linear in the number n of vertices, it is still an open problem if there exists an (r,t)-RS graph with t = nǫ. The best known construction in this case, due to Fischer et al. [37], is an example with r = n/3 and t = nc/log logn. However, for r = n1−o(1), substantial progress was made recently by Alon, Moitra and Sudakov [8] by extending ideas used in the construction of Fox and Loh [39] discussed in the previous subsection. They give a construction of n-vertex graphs with rt = (1 − o(1) n2 and r = n1−o(1). That is, there are nearly complete graphs, with edge density 1 − o(1), such that its edge set can be partitioned into large induced matchings, each of order n1−o(1). They give several applications of this construction to combinatorics, complexity theory and information theory.

## 6.3 Testing small graphs

A property of graphs is a family of graphs closed under isomorphism. A graph G on n vertices is ǫ-far from satisfying a property P if no graph which can be constructed from G by adding and/or removing

- at most ǫn2 edges satisﬁes P. An ǫ-tester for P is a randomized algorithm which, given the quantity n and the ability to make queries whether a desired pair of vertices spans an edge in G, distinguishes with probability at least 2/3 between the case that G satisﬁes P and the case that G is ǫ-far from satisfying P. Such an ǫ-tester is a one-sided ǫ-tester if when G satisﬁes P the ǫ-tester determines that


this is the case. The property P is called testable if, for every ﬁxed ǫ > 0, there exists a one-sided ǫ-tester for P whose total number of queries is bounded only by a function of ǫ which is independent of the size of the input graph. This means that the running time of the algorithm is also bounded by a function of ǫ only and is independent of the input size. We measure query-complexity by the number of vertices sampled, assuming we always examine all edges spanned by them. The inﬁnite removal lemma, Theorem 3.2, of Alon and Shapira [12] shows that every hereditary graph property, that is, a graph property closed under taking induced subgraphs, is testable. Many of the best studied graph properties are hereditary.

If the query complexity of an ǫ-tester is polynomial in ǫ−1, we say that the property is easily testable. It is an interesting open problem to characterize the easily testable hereditary properties. Alon [3] considered the case where P = PH is the property that the graph does not contain H as a subgraph. He showed that PH is easily testable if and only if H is bipartite. Alon and Shapira [10] considered the case where P = PH∗ is the property that the graph does not contain H as an induced subgraph. They showed that for any graph H except for the path with at most four vertices, the cycle of length four and their complements, the property PH∗ is not easily testable. The problem of determining whether the property PH∗ is easily testable for the path with four vertices or the cycle of length four (or equivalently its complement) was left open. The case where H is a path with four vertices was recently shown to be easily testable by Alon and Fox [7]. The case where H is a cycle of length four is still open. Alon and Fox also showed that if P is the family of perfect graphs, then P is not easily testable and, in a certain sense, testing for P is at least as hard as testing triangle-freeness.

## 6.4 Local repairability

The standard proof of the regularity lemma contains a procedure for turning a graph which is almost triangle-free into a graph which is triangle-free. We simply delete the edges between all vertex sets of low density and between all vertex sets which do not form a regular pair. This procedure can be made more explicit still by using an algorithmic version of the regularity lemma [4].

A surprising observation of Austin and Tao [13] is that this repair procedure can be determined in a local fashion. They show that for any graph H and any ǫ > 0 there exists δ > 0 and a natural number m such that if G is a graph containing at most δnv(H) copies of H then there exists a set A of size at most m such that G may be made H-free by removing at most ǫn2 edges and the decision of whether to delete a given edge uv may be determined solely by considering the restriction of G to the set A ∪ {u,v}.19

The key point, ﬁrst observed by Ishigami [59], is that the regular partition can be determined in a local fashion by randomly selecting vertex neighborhoods to create the partition. Since a ﬁnite set of points determine the partition, this may in turn be used to create a local modiﬁcation rule which results in an H-free graph.

Similar ideas may also be applied to show that any hereditary graph property, including the property of being induced H-free, is locally repairable in the same sense. This again follows from the observation that random neighborhoods can be used to construct the partitions arising in the strong regularity lemma.

Surprisingly, Austin and Tao show that, even though all hereditary hypergraph properties are testable,

![image 122](<2012-conlon-graph-removal-lemmas_images/imageFile122.png>)

19Strictly speaking, Austin and Tao [13] consider two forms of local repairability. Here we are considering only the weak version.

there are hereditary properties which are not locally repairable. On the other hand, they show that many natural hypergraph properties, including the property of being H-free, are locally repairable.

## 6.5 Linear hypergraphs

A linear hypergraph is a hypergraph where any pair of edges overlap in at most one vertex. For this special class of hypergraphs, it is not necessary to apply the full strength of hypergraph regularity to prove a corresponding removal lemma [66]. Instead, a straightforward analogue of the usual regularity lemma is suﬃcient. This results in bounds for δ−1 in the linear hypergraph removal lemma which are of tower-type in a power of ǫ−1.

While this is already a substantial improvement on general hypergraphs, where the best known bounds are Ackermannian,20 it can be improved further by using the ideas of [38]. This results in a bound of the form T(aH log ǫ−1).

A similar reduction does not exist for induced removal of linear hypergraphs. Because we need to consider all edges, whether present or not, between the vertices of the hypergraph, we must apply the full strength of the strong hypergraph regularity lemma. This results in Ackermannian bounds.

It is plausible that an extension of the methods of Section 2.2 could be used to give a primitive recursive, or even tower-type, bound for hypergraph removal. We believe that such an improvement would be of great interest, not least because it would give the ﬁrst primitive recursive bound for the multidimensional extension of Szemere´di’s theorem. Such an improvement would also be likely to lead to an analogous improvement of the bounds for induced hypergraph removal.

Acknowledgements. The authors would like to thank Noga Alon, Zoltan Fu¨redi, Vojta Ro¨dl and Terry Tao for helpful comments regarding the history of the removal lemma.

# References

- [1] M. Ajtai and E. Szemere´di, Sets of lattice points that form no squares, Stud. Sci. Math. Hungar. 9 (1974), 9–11.
- [2] N. Alon, Explicit Ramsey graphs and orthonormal labellings, Electron. J. Combin. 1 (1994), R12, 8pp.
- [3] N. Alon, Testing subgraphs in large graphs, Random Structures Algorithms 21 (2002), 359–370.
- [4] N. Alon, R. A. Duke, H. Lefmann, V. Ro¨dl and R. Yuster, The algorithmic aspects of the regularity lemma, J. Algorithms 16 (1994), 80–109.
- [5] N. Alon, W. Fernandez de la Vega, R. Kannan and M. Karpinski, Random sampling and approximation of MAX-CSPs, J. Comput. System Sci. 67 (2003), 212–243.
- [6] N. Alon, E. Fischer, M. Krivelevich and M. Szegedy, Eﬃcient testing of large graphs, Combinatorica 20 (2000), 451–476.


![image 123](<2012-conlon-graph-removal-lemmas_images/imageFile123.png>)

20We have already seen two levels of the Ackermann function, the tower function and the wowzer function. Generally, the kth level is deﬁned by Ak(1) = 2 and Ak(i + 1) = Ak−1(Ak(i)). Taking A1(i) = 2i, we see that A2(i) = T(i) and A3(i) = W(i). The upper bound on δ−1 in the k-uniform hypergraph removal lemma given by the hypergraph regularity proofs are of the form Ak(ǫ−O(1)) or worse.

- [7] N. Alon and J. Fox, Testing perfectness is hard, submitted.
- [8] N. Alon A. Moitra and B. Sudakov, Nearly complete graphs decomposable into large induced matchings and their applications, submitted.
- [9] N. Alon and A. Shapira, Testing subgraphs in directed graphs, J. Comput. System Sci. 69 (2004), 353–382.
- [10] N. Alon and A. Shapira, A characterization of easily testable induced subgraphs, Combin. Probab. Comput. 15 (2006), 791–805.
- [11] N. Alon and A. Shapira, Every monotone graph property is testable, in Proc. of STOC 2005, 128–137, SIAM J. Comput. (Special Issue of STOC’05) 38 (2008), 505–522.
- [12] N. Alon and A. Shapira, A characterization of the (natural) graph properties testable with onesided error, in Proc. of FOCS 2005, 429–438, SIAM J. Comput. (Special Issue on FOCS ’05) 37

(2008), 1703–1727.

- [13] T. Austin and T. Tao, Testability and repair of hereditary hypergraph properties, Random Structures Algorithms 36 (2010), 373–463.
- [14] C. Avart, V. Ro¨dl and M. Schacht, Every monotone 3-graph property is testable, SIAM J. Discrete Math. 21 (2007), 73–92.
- [15] J. Balogh, R. Morris and W. Samotij, Independent sets in hypergraphs, submitted.
- [16] F. Behrend, On sets of integers which contain no three terms in arithmetic progression, Proc. Nat. Acad. Sci. 32 (1946), 331–332.
- [17] B. Bollob´s, Random graphs, second edition, Cambridge Studies in Advanced Mathematics 73, Cambridge University Press, Cambridge, 2001.
- [18] C. Borgs, J. T. Chayes, L. Lov´asz, V. T. So´s and K. Vesztergombi, Convergent sequences of dense graphs I: subgraph frequencies, metric properties and testing, Adv. Math. 219 (2008), 1801–1851.
- [19] W. G. Brown, P. Erd˝os and V. T. So´s, On the existence of triangulated spheres in 3-graphs, and related problems, Period. Math. Hungar. 3 (1973), 221–228.
- [20] P. Candela, Developments at the interface between combinatorics and Fourier analysis, PhD thesis, University of Cambridge, 2009.
- [21] F. R. K. Chung, A spectral Tura´n theorem, Combin. Probab. Comput. 14 (2005), 755–767.
- [22] F. R. K. Chung, R. L. Graham and R. M. Wilson, Quasi-random graphs, Combinatorica 9 (1989), 345–362.
- [23] L. H. Clark, R. C. Entringer, J. E. McCanna and L. A. Sze´kely, Extremal problems for local properties of graphs, in Combinatorial mathematics and combinatorial computing (Palmerston North, 1990), Australas. J. Combin. 4 (1991), 25–31.
- [24] D. Conlon and J. Fox, Bounds for graph regularity and removal lemmas, Geom. Funct. Anal. 22


(2012), 1192–1256.

- [25] D. Conlon and W. T. Gowers, Combinatorial theorems in sparse random sets, submitted.
- [26] D. Conlon, W. T. Gowers, W. Samotij and M. Schacht, On the K LR conjecture in random graphs, submitted.
- [27] D. Conlon, J. Fox and Y. Zhao, Extremal results in sparse pseudorandom graphs, submitted.
- [28] R. A. Duke, H. Lefmann and V. Ro¨dl, A fast approximation algorithm for computing the frequencies of subgraphs in a given graph, SIAM J. Comput. 24 (1995), 598–620.
- [29] C. S. Edwards, A lower bound for the largest number of triangles with a common edge, 1977, unpublished manuscript.
- [30] P. Erd˝os, Some problems on ﬁnite and inﬁnite graphs, in Logic and combinatorics (Arcata, Calif., 1985), 223–228, Contemp. Math. 65, Amer. Math. Soc., Providence, RI, 1987.
- [31] P. Erd˝os, Some of my favourite problems in various branches of combinatorics, in Combinatorics 92 (Catania, 1992), Matematiche (Catania) 47 (1992), 231–240.
- [32] P. Erd˝os, P. Frankl and V. Ro¨dl, The asymptotic number of graphs not containing a ﬁxed subgraph and a problem for hypergraphs having no exponent, Graphs Combin. 2 (1986), 113–121.
- [33] P. Erd˝os and A. Re´nyi, On random graphs I, Publ. Math. Debrecen 6 (1959), 290–297.
- [34] P. Erd˝os and A. Re´nyi, On the evolution of random graphs, Magyar Tud. Akad. Mat. Kutato´ Int. K¨ozl. 5 (1960), 17–61.
- [35] P. Erd˝os and M. Simonovits, A limit theorem in graph theory, Studia Sci. Math. Hungar. 1 (1966), 51–57.
- [36] P. Erd˝os and A. H. Stone, On the structure of linear graphs, Bull. Amer. Math. Soc. 52 (1946), 1087–1091.
- [37] E. Fischer, I. Newman, S. Raskhodnikova, R. Rubinfeld and A. Samorodnitsky, Monotonicity testing over general poset domains, in Proceedings of the 2002 ACM Symposium on Theory of Computing, 474–483, ACM, New York, 2002.
- [38] J. Fox, A new proof of the graph removal lemma, Ann. of Math. 174 (2011), 561–579.
- [39] J. Fox and P. Loh, On a problem of Erd˝os and Rothschild on edges in triangles, to appear in Combinatorica.
- [40] P. Frankl and Z. Fu¨redi, Exact solution of some Tura´n-type problems, J. Combin. Theory Ser. A 45 (1987), 226–262.
- [41] P. Frankl, R. L. Graham and V. Ro¨dl, On subsets of abelian groups with no 3-term arithmetic progression, J. Combin. Theory Ser. A 45 (1987), 157–161.
- [42] P. Frankl and V. Ro¨dl, Extremal problems on set systems, Random Structures Algorithms 20

(2002), 131–164.

- [43] E. Friedgut, V. Ro¨dl and M. Schacht, Ramsey properties of discrete random structures, Random Structures Algorithms, 37 (2010), 407–436.


- [44] A. Frieze and R. Kannan, The regularity lemma and approximation schemes for dense problems, Proceedings of the 37th IEEE FOCS (1996), 12–20.
- [45] A. Frieze and R. Kannan, Quick approximation to matrices and applications, Combinatorica 19

(1999), 175–220.

- [46] Z. Fu¨redi, The maximum number of edges in a minimal graph of diameter 2, J. Graph Theory 16 (1992), 81–98.
- [47] Z. Fu¨redi, Extremal hypergraphs and combinatorial geometry, in Proceedings of the International Congress of Mathematicians, Vol. 1, 2 (Zu¨rich, 1994), 1343–1352, Birkh¨auser, Basel, 1995.
- [48] H. Furstenberg, Ergodic behavior of diagonal measures and a theorem of Szemere´di on arithmetic progressions, J. Analyse Math. 31 (1977), 204–256.
- [49] H. Furstenberg and Y. Katznelson, An ergodic Szemere´di theorem for commuting transformations, J. Analyse Math. 34 (1978), 275–291.
- [50] H. Furstenberg, Y. Katznelson and D. Ornstein, The ergodic theoretical proof of Szemere´di’s theorem, Bull. Amer. Math. Soc. 7 (1982), 527–552.
- [51] O. Goldreich, S. Goldwasser and D. Ron, Property testing and its applications to learning and approximation, J. ACM 45 (1998), 653–750.
- [52] W. T. Gowers, Lower bounds of tower type for Szemere´di’s uniformity lemma, Geom. Funct. Anal. 7 (1997), 322–337.
- [53] W. T. Gowers, A new proof of Szemere´di’s theorem for arithmetic progressions of length four, Geom. Funct. Anal. 8 (1998), 529–551.
- [54] W.T. Gowers, A new proof of Szemere´di’s theorem, Geom. Funct. Anal. 11 (2001), 465–588.
- [55] W.T. Gowers, Quasirandomness, counting and regularity for 3-uniform hypergraphs, Combin. Probab. Comput. 15 (2006), 143–184.
- [56] W.T. Gowers, Hypergraph regularity and the multidimensional Szemere´di theorem, Ann. of Math. 166 (2007), 897–946.
- [57] B. Green, A Szemere´di-type regularity lemma in abelian groups, with applications, Geom. Funct. Anal. 15 (2005), 340–376.
- [58] P. E. Haxell, Y. Kohayakawa and T.  Luczak, Tura´n’s extremal problem in random graphs: forbidding odd cycles, Combinatorica 16 (1996), 107–122.
- [59] Y. Ishigami, A simple regularization of hypergraphs, submitted.
- [60] S. Janson, T.  Luczak and A. Rucin´ski, Random graphs, Wiley-Interscience Series in Discrete Mathematics and Optimization, Wiley-Interscience, New York, 2000.
- [61] S. Kalyanasundaram and A. Shapira, A wowzer-type lower bound for the strong regularity lemma, Proc. London Math. Soc., to appear.


- [62] N. Khadzˇiivanov and V. Nikiforov, Solution of a problem of P. Erd˝os about the maximum number of triangles with a common edge in a graph, C. R. Acad. Bulgare Sci. 32 (1979), 1315–1318.
- [63] Y. Kohayakawa, Szemere´di’s regularity lemma for sparse graphs, in Foundations of computational mathematics (Rio de Janeiro, 1997), Springer, Berlin, 1997, 216–230.
- [64] Y. Kohayakawa, T.  Luczak and V. Ro¨dl, Arithmetic progressions of length three in subsets of a random set, Acta Arith. 75 (1996), 133–163.
- [65] Y. Kohayakawa, T.  Luczak and V. Ro¨dl, On K4-free subgraphs of random graphs, Combinatorica 17 (1997), 173–213.
- [66] Y. Kohayakawa, B. Nagle, V. Ro¨dl and M. Schacht, Weak regularity and linear hypergraphs, J. Combin. Theory Ser. B 100 (2010), 151–160.
- [67] Y. Kohayakawa, B. Nagle, V. Ro¨dl, J. Skokan and M. Schacht, The hypergraph regularity method and its applications, Proc. Natl. Acad. Sci. USA 102 (2005), 8109–8113.
- [68] Y. Kohayakawa, V. Ro¨dl, M. Schacht and J. Skokan, On the triangle removal lemma for subgraphs of sparse pseudorandom graphs, in An Irregular Mind (Szemere´di is 70), Bolyai Society Math. Studies 21, Springer, 2010, 359–404.
- [69] D. Kra´l’, O. Serra and L. Vena, A removal lemma for linear systems over ﬁnite ﬁelds, in Sixth conference on discrete mathematics and computer science (Spanish), 417–423, Univ. Lleida, Lleida, 2008.
- [70] D. Kra´l’, O. Serra and L. Vena, A combinatorial proof of the removal lemma for groups, J. Combin. Theory Ser. A 116 (2009), 971–978.
- [71] D. Kra´l’, O. Serra and L. Vena, A removal lemma for systems of linear equations over ﬁnite ﬁelds, Israel J. Math. 187 (2012), 193–207.
- [72] D. Kra´l’, O. Serra and L. Vena, On the removal lemma for linear systems over abelian groups, European J. Combin. 34 (2013), 248–259.
- [73] M. Krivelevich and B. Sudakov, Pseudo-random graphs, in More sets, graphs and numbers, Bolyai Soc. Math. Stud. 15, Springer, Berlin, 2006, 199–262.
- [74] L. Lov´asz and B. Szegedy, Szemere´di’s lemma for the analyst, Geom. Funct. Anal. 17 (2007), 252–270.
- [75] L. Lov´asz and B. Szegedy, Testing properties of graphs and functions, Israel J. Math. 178 (2010), 113–156.
- [76] T.  Luczak, Randomness and regularity, in International Congress of Mathematicians, Vol. III, 899–909, Eur. Math. Soc., Zu¨rich, 2006.
- [77] B. Nagle and V. Ro¨dl, Regularity properties for triple systems, Random Structures Algorithms 23 (2003), 264–332.
- [78] B. Nagle, V. Ro¨dl and M. Schacht, The counting lemma for regular k-uniform hypergraphs, Random Structures Algorithms 28 (2006), 113–179.


- [79] Y. Peng, V. Ro¨dl, and A. Rucin´ski, Holes in graphs, Electron. J. Combin. 9 (2002), R1, 18pp.
- [80] Y. Peng, V. Ro¨dl and J. Skokan, Counting small cliques in 3-uniform hypergraphs, Combin. Probab. Comput. 14 (2005), 371–413.
- [81] D. H. J. Polymath, A new proof of the density Hales-Jewett theorem, Ann. of Math. 175 (2012), 1283–1327.
- [82] F. P. Ramsey, On a problem of formal logic, Proc. London Math. Soc. 30 (1930), 264–286.
- [83] V. Ro¨dl and A. Rucin´ski, Lower bounds on probability thresholds for Ramsey properties, in Combinatorics, Paul Erd˝os is eighty, Vol. 1, 317–346, Bolyai Soc. Math. Stud., Ja´nos Bolyai Math. Soc., Budapest, 1993.
- [84] V. Ro¨dl and A. Rucin´ski, Threshold functions for Ramsey properties, J. Amer. Math. Soc. 8

(1995), 917–942.

- [85] V. Ro¨dl and M. Schacht, Regular partitions of hypergraphs: regularity lemmas, Combin. Probab. Comput. 16 (2007), 833–885.
- [86] V. Ro¨dl and M. Schacht, Generalizations of the removal lemma, Combinatorica 29 (2009), 467– 501.
- [87] V. Ro¨dl and M. Schacht, Regularity lemmas for graphs, in Fete of Combinatorics and Computer Science, Bolyai Soc. Math. Stud. 20, Springer, 2010, 287–325.
- [88] V. Ro¨dl and J. Skokan, Regularity lemma for uniform hypergraphs, Random Structures Algorithms 25 (2004), 1–42.
- [89] V. Ro¨dl and J. Skokan, Counting subgraphs in quasi-random 4-uniform hypergraphs, Random Structures Algorithms 26 (2005), 160–203.
- [90] V. Ro¨dl and J. Skokan, Applications of the regularity lemma for uniform hypergraphs, Random Structures Algorithms 28 (2006), 180–194.
- [91] K. F. Roth, On certain sets of integers, J. London Math. Soc. 28 (1953), 104–109.
- [92] R. Rubinﬁeld and M. Sudan, Robust characterization of polynomials with applications to program testing, SIAM J. Comput. 25 (1996), 252–271.
- [93] I. Z. Ruzsa and E. Szemere´di, Triple systems with no six points carrying three triangles, in Combinatorics (Keszthely, 1976), Coll. Math. Soc. J. Bolyai 18, Volume II, 939–945.
- [94] W. Samotij, Stability results for random discrete structures, to appear in Random Structures Algorithms.
- [95] T. Sanders, On Roth’s theorem on progressions, Ann. of Math. 174 (2011), 619–636.
- [96] T. Sanders, On the Bogolyubov-Ruzsa lemma, Anal. PDE, to appear.
- [97] D. Saxton and A. Thomason, Hypergraph containers, submitted.
- [98] M. Schacht, Extremal results for random discrete structures, submitted.


- [99] T. Schoen and I. Shkredov, Roth’s theorem in many variables, submitted.
- [100] A. Shapira, Green’s conjecture and testing linear-invariant properties, in Proceedings of the 2009 ACM International Symposium on Theory of Computing, 159–166, ACM, New York, 2009.
- [101] A. Shapira, A proof of Green’s conjecture regarding the removal properties of sets of linear equations, J. London Math. Soc. 81 (2010), 355–373.
- [102] I. Shkredov, On a generalization of Szemere´di’s theorem, Proc. London Math. Soc. 93 (2006), 723–760.
- [103] M. Simonovits, A method for solving extremal problems in graph theory, stability problems, in Theory of graphs (Proc. Colloq. Tihany,1966), Academic Press, New York, 1968, 279–319.
- [104] J. Solymosi, Note on a generalization of Roth’s theorem, in Discrete and computational geometry, Algorithms Combin. Vol. 25, Springer, 2003, 825–827.
- [105] J. Solymosi, A note on a question of Erd˝os and Graham, Combin. Probab. Comput. 13 (2004), 263–267.
- [106] J. Solymosi, Regularity, uniformity, and quasirandomness, Proc. Natl. Acad. Sci. USA 102

(2005), 8075–8076

- [107] B. Sudakov, T. Szabo´ and V.H. Vu, A generalization of Tura´n’s theorem, J. Graph Theory 49

(2005), 187–195.

- [108] B. Szegedy, The symmetry preserving removal lemma, Proc. Amer. Math. Soc. 138 (2010), 405–408.
- [109] E. Szemere´di, Integer sets containing no k elements in arithmetic progression, Acta Arith. 27

(1975), 299–345.

- [110] E. Szemere´di, Regular partitions of graphs, in Colloques Internationaux CNRS 260 - Proble`mes Combinatoires et The´orie des Graphes, Orsay, (1976), 399–401.
- [111] T. Tao, Szemere´di’s regularity lemma revisited, Contrib. Discrete Math. 1 (2006), 8–28.
- [112] T. Tao, A variant of the hypergraph removal lemma, J. Combin. Theory Ser. A 113 (2006), 1257–1280.
- [113] A. Thomason, Pseudorandom graphs, in Random graphs ’85 (Poznan´, 1985), 307–331, NorthHolland Math. Stud. 144, North-Holland, Amsterdam, 1987.
- [114] A. Thomason, Random graphs, strongly regular graphs and pseudorandom graphs, Surveys in combinatorics 1987 (New Cross, 1987), 173–195, London Math. Soc. Lecture Note Ser. 123, Cambridge Univ. Press, Cambridge, 1987.
- [115] P. Tura´n, Eine Extremalaufgabe aus der Graphentheorie, Mat. Fiz. Lapok 48 (1941), 436–452.


