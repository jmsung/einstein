arXiv:1501.02474v3[math.CO]10May2015

Recent developments in graph Ramsey theory

David Conlon∗ Jacob Fox† Benny Sudakov‡

Abstract

Given a graph H, the Ramsey number r(H) is the smallest natural number N such that any two-colouring of the edges of KN contains a monochromatic copy of H. The existence of these numbers has been known since 1930 but their quantitative behaviour is still not well understood. Even so, there has been a great deal of recent progress on the study of Ramsey numbers and their variants, spurred on by the many advances across extremal combinatorics. In this survey, we will describe some of this progress.

# 1 Introduction

In its broadest sense, the term Ramsey theory refers to any mathematical statement which says that a structure of a given kind is guaranteed to contain a large well-organised substructure. There are examples of such statements in many areas, including geometry, number theory, logic and analysis. For example, a key ingredient in the proof of the Bolzano–Weierstrass theorem in real analysis is a lemma showing that any inﬁnite sequence must contain an inﬁnite monotone subsequence.

A classic example from number theory, proved by van der Waerden [212] in 1927, says that if the natural numbers are coloured in any ﬁxed number of colours then one of the colour classes contains arbitrarily long arithmetic progressions. This result has many generalisations. The most famous, due to Szemere´di [206], says that any subset of the natural numbers of positive upper density contains arbitrarily long arithmetic progressions. Though proved in 1975, the inﬂuence of this result is still being felt today. For example, it was a key ingredient in Green and Tao’s proof [131] that the primes contain arbitrarily long arithmetic progressions.

Though there are many further examples from across mathematics, our focus in this survey will be on graph Ramsey theory. The classic theorem in this area, from which Ramsey theory as a whole derives its name, is Ramsey’s theorem [174]. This theorem says that for any graph H there exists a natural number N such that any two-colouring of the edges of KN contains a monochromatic copy of H. The smallest such N is known as the Ramsey number of H and is denoted r(H). When H = Kt, we simply write r(t).

![image 1](<2015-conlon-recent-developments-graph-ramsey_images/imageFile1.png>)

∗Mathematical Institute, Oxford OX2 6GG, United Kingdom. Email: david.conlon@maths.ox.ac.uk. Research supported by a Royal Society University Research Fellowship.

†Department of Mathematics, Stanford University, Stanford, CA 94305. Email: fox@math.mit.edu. Research supported by a Packard Fellowship, by NSF Career Award DMS-1352121 and by an Alfred P. Sloan Fellowship.

‡Department of Mathematics, ETH, 8092 Zurich, Switzerland. Email: benjamin.sudakov@math.ethz.ch. Research supported by SNSF grant 200021-149111.

Though Ramsey proved his theorem in 1930 and clearly holds precedence in the matter, it was a subsequent paper by Erd˝os and Szekeres [102] which brought the matter to a wider audience. Amongst other things, Erd˝os and Szekeres were the ﬁrst to give a reasonable estimate on Ramsey numbers.1 To describe their advance, we deﬁne the oﬀ-diagonal Ramsey number r(H1,H2) as the smallest natural number N such that any red/blue-colouring of the edges of KN contains either a red copy of H1 or a blue copy of H2. If we write r(s,t) for r(Ks,Kt), then what Erd˝os and Szekeres proved is the bound

s + t − 2 s − 1

r(s,t) ≤

.

For s = t, this yields r(t) = O(√4tt), while if s is ﬁxed, it gives r(s,t) ≤ ts−1. Over the years, much eﬀort has been expended on improving these bounds or showing that they are close to tight, with

![image 2](<2015-conlon-recent-developments-graph-ramsey_images/imageFile2.png>)

![image 3](<2015-conlon-recent-developments-graph-ramsey_images/imageFile3.png>)

only partial success. However, these problems have been remarkably inﬂuential in combinatorics, playing a key role in the development of random graphs and the probabilistic method, as well as the theory of quasirandomness (see [11]). We will highlight some of these connections in Section 2.1 when we discuss the current state of the art on estimating r(s,t).

If we move away from complete graphs, a number of interesting phenomena start to appear. For example, a famous result of Chv´atal, Ro¨dl, Szemere´di and Trotter [44] says that if H is a graph with n vertices and maximum degree ∆, then the Ramsey number r(H) is bounded by c(∆)n for some constant c(∆) depending only on ∆. That is, the Ramsey number of bounded-degree graphs grows linearly in the number of vertices. This and related developments will be discussed in Section 2.3, while other aspects of Ramsey numbers for general H will be explored in Sections 2.4, 2.5 and 2.6.

In full generality, Ramsey’s theorem applies not only to graphs but also to k-uniform hypergraphs. Formally, a k-uniform hypergraph is a pair H = (V,E), where V is a collection of vertices and E is a collection of subsets of V , each of order k. We write KN(k) for the complete k-uniform hypergraph on N vertices, that is, V has order N and E contains all subsets of V of order k.

The full statement of Ramsey’s theorem, which also allows for more than two colours, now says that for any natural number q ≥ 2 and any k-uniform hypergraphs H1,... ,Hq there exists a natural number N such that any q-colouring of the edges of KN(k) contains a copy of Hi in the ith colour for some i. The smallest such N is known as the Ramsey number of H1,... ,Hq and is denoted rk(H1,... ,Hq). If Hi = Kt(k)

for each i, we write rk(t1,... ,tq). Moreover, if H1 = ··· = Hq = H,

i

we simply write rk(H;q), which we refer to as the q-colour Ramsey number of H. If H = Kt(k), we write rk(t;q). If either k or q is equal to two, it is omitted.

Even for complete 3-uniform hypergraphs, the growth rate of the Ramsey number is not well understood. Indeed, it is only known that

2c′t2 ≤ r3(t) ≤ 22ct.

Determining the correct asymptotic for this function is of particular importance, since it is known that an accurate estimate for r3(t) would imply an accurate estimate on rk(t) for all k ≥ 4. This and related topics will be discussed in depth in Section 2.2, though we will make reference to hypergraph

![image 4](<2015-conlon-recent-developments-graph-ramsey_images/imageFile4.png>)

1Ramsey’s original paper mentions the bound r(t) ≤ t!, but he does not pursue the matter further. It is an amusing exercise to ﬁnd a natural proof that gives exactly this bound.

analogues of graph Ramsey problems throughout the survey. As we will see, these questions often throw up new and interesting behaviour which is strikingly diﬀerent from the graph case.

While our focus in Section 2 will be on the classical Ramsey function, we will move on to discussing a number of variants in Section 3. These variants include well-established topics such as induced Ramsey numbers and size Ramsey numbers, as well as a number of more recent themes such as ordered Ramsey numbers. We will not try to give a summary of these variants here, instead referring the reader to the individual sections, each of which is self-contained.

We should note that this paper is not intended to serve as an exhaustive survey of the subject. Instead, we have focused on those areas which are most closely related to our own interests. For the most part, this has meant that we have treated problems of an asymptotic nature rather than being concerned with the computation of exact Ramsey numbers.2 Even with this caveat, it has still been necessary to gloss over a number of interesting topics. We apologise in advance for any particularly glaring omissions.

We will maintain a number of conventions throughout the paper. For the sake of clarity of presentation, we will sometimes omit ﬂoor and ceiling signs when they are not crucial. Unless speciﬁed otherwise, we use log to denote the logarithm taken to the base two. We will use standard asymptotic notation with a subscript indicating that the implied constant may depend on that subscript. All other notation will be explained in the relevant sections.

# 2 The classical problem

## 2.1 Complete graphs

As already mentioned in the introduction, the classical bound on Ramsey numbers for complete graphs is the Erd˝os–Szekeres bound

s + t − 2 s − 1

r(s,t) ≤

.

In particular, for s = t, this gives r(t) = O(√4tt). The proof of the Erd˝os–Szekeres bound relies on the simple inequality

![image 5](<2015-conlon-recent-developments-graph-ramsey_images/imageFile5.png>)

![image 6](<2015-conlon-recent-developments-graph-ramsey_images/imageFile6.png>)

r(s,t) ≤ r(s,t − 1) + r(s − 1,t).

To prove this inequality, consider a red/blue-colouring of the edges of Kr(s,t)−1 containing no red copy of Ks and no blue copy of Kt. The critical observation is that the red degree of every vertex, that is, the number of neighbours in red, is at most r(s−1,t)−1. Indeed, if the red neighbourhood of any vertex v contained r(s − 1,t) vertices, it would contain either a blue Kt, which would contradict our choice of colouring, or a red Ks−1, which together with v would form a red Ks, again a contradiction. Similarly, the blue degree of every vertex is at most r(s,t−1)−1. Since the union of any particular vertex with its red and blue neighbourhoods is the entire vertex set, we see that

r(s,t) − 1 ≤ 1 + (r(s − 1,t) − 1) + (r(s,t − 1) − 1).

![image 7](<2015-conlon-recent-developments-graph-ramsey_images/imageFile7.png>)

2For this and more, we refer the reader to the excellent dynamic survey of Radziszowski [173].

The required inequality follows.

The key observation here, that in any graph containing neither a red Ks nor a blue Kt the red degree of any vertex is less than r(s − 1,t) and the blue degree is less than r(s,t − 1), may be generalised. Indeed, an argument almost exactly analogous to that above shows that in any graph containing neither a red Ks nor a blue Kt, any red edge must be contained in fewer than r(s−2,t) red triangles and any blue edge must be contained in fewer than r(s,t−2) blue triangles. Indeed, if a red edge uv were contained in at least r(s−2,t) red triangles, then the set W of vertices w joined to both u and v in red would have order at least r(s − 2,t). If this set contained a blue Kt, we would have a contradiction, so the set must contain a red Ks−2. But the union of this clique with u and v forms a Ks, again a contradiction. Together with Goodman’s formula [124] for the number of monochromatic triangles in a two-colouring of KN, this observation may be used to show that

r(t,t) ≤ 4r(t,t − 2) + 2. Using the idea behind this inequality, Thomason [210] was able to improve the upper bound for diagonal Ramsey numbers to r(t) = O(4tt), improving an earlier result of Ro¨dl [127], who was the ﬁrst to show that r(t) = o(√4tt).

![image 8](<2015-conlon-recent-developments-graph-ramsey_images/imageFile8.png>)

![image 9](<2015-conlon-recent-developments-graph-ramsey_images/imageFile9.png>)

![image 10](<2015-conlon-recent-developments-graph-ramsey_images/imageFile10.png>)

As the observant reader may already have noted, the argument of the previous paragraph is itself a special case of the following observation.

Observation 2.1. In any graph containing neither a red Ks nor a blue Kt, any red copy of Kp must be contained in fewer than r(s − p,t) red copies of Kp+1 and any blue copy of Kp must be contained in fewer than r(s,t − p) blue copies of Kp+1.

By using this additional information, Conlon [45] was able to give the following superpolynomial improvement on the Erd˝os–Szekeres bound. Theorem 2.2. There exists a positive constant c such that

r(t) ≤ t−clogt/log logt4t.

In broad outline, the proof of Theorem 2.2 proceeds by using the p = 1 and p = 2 cases of Observation 2.1 to show that any red/blue-colouring of the edges of a complete graph with at least t−clogt/log logt4t vertices which contains no monochromatic Kt is quasirandom. Through a delicate counting argument, this is then shown to contradict Observation 2.1 for p roughly log t/log log t.

The ﬁrst signiﬁcant lower bound for the diagonal Ramsey number r(t) was proved by Erd˝os [78] in 1947. This was one of the ﬁrst applications of the probabilistic method and most introductions to this beautiful subject begin with his simple argument. Though we run the risk of being repetitious, we will also include this argument.

Colour the edges of the complete graph KN randomly. That is, we colour each edge red with probability 1/2 and blue with probability 1/2. Since the probability that a given copy of Kt has all edges red is 2−(2t), the expected number of red copies of Kt in this graph is 2−(2t) N

t . Similarly, the expected number of blue copies of Kt is 2−(2t) N

t . Therefore, the expected number of monochromatic copies of Kt is

21−(2t) N t ≤ 21−t(t−1)/2

eN t

![image 11](<2015-conlon-recent-developments-graph-ramsey_images/imageFile11.png>)

t

.

For N = (1 − o(1))√t2e√2t, we see that this expectation is less than one. Therefore, there must be some colouring of KN for which there are no monochromatic copies of Kt. This bound,

![image 12](<2015-conlon-recent-developments-graph-ramsey_images/imageFile12.png>)

![image 13](<2015-conlon-recent-developments-graph-ramsey_images/imageFile13.png>)

![image 14](<2015-conlon-recent-developments-graph-ramsey_images/imageFile14.png>)

√

t √2e

2t,

![image 15](<2015-conlon-recent-developments-graph-ramsey_images/imageFile15.png>)

r(t) ≥ (1 − o(1))

![image 16](<2015-conlon-recent-developments-graph-ramsey_images/imageFile16.png>)

![image 17](<2015-conlon-recent-developments-graph-ramsey_images/imageFile17.png>)

has been astonishingly resilient to improvement. Since 1947, there has only been one noteworthy improvement. This was achieved by Spencer [198], who used the Lov´asz local lemma to show that

√2t e

√

![image 18](<2015-conlon-recent-developments-graph-ramsey_images/imageFile18.png>)

2t.

![image 19](<2015-conlon-recent-developments-graph-ramsey_images/imageFile19.png>)

r(t) ≥ (1 − o(1))

![image 20](<2015-conlon-recent-developments-graph-ramsey_images/imageFile20.png>)

That is, he improved Erd˝os’ bound by a factor of two! Any further improvement to this bound, no matter how tiny, would be of signiﬁcant interest.

Problem 2.3. Does there exist a positive constant ǫ such that

√2t e

√

![image 21](<2015-conlon-recent-developments-graph-ramsey_images/imageFile21.png>)

2t for all suﬃciently large t?

![image 22](<2015-conlon-recent-developments-graph-ramsey_images/imageFile22.png>)

r(t) ≥ (1 + ǫ)

![image 23](<2015-conlon-recent-developments-graph-ramsey_images/imageFile23.png>)

For oﬀ-diagonal Ramsey numbers, where s is ﬁxed and t tends to inﬁnity, the Erd˝os–Szekeres bound shows that r(s,t) ≤ ts−1. In 1980, this bound was improved by Ajtai, Komlo´s and Szemere´di [1], who proved that for any s there exists a constant cs such that

ts−1 (log t)s−2

r(s,t) ≤ cs

.

![image 24](<2015-conlon-recent-developments-graph-ramsey_images/imageFile24.png>)

When s = 3, this follows from the statement that any triangle-free graph on N vertices with average degree d contains an independent set of order Ω(Nd log d). Indeed, in a triangle-free graph, the neighbourhood of every vertex must form an independent set and so d < t. But then the graph must contain an independent set of order Ω(Nt log t) and, hence, for c suﬃciently large and N ≥ ct2/log t, the graph contains an independent set of order t.

![image 25](<2015-conlon-recent-developments-graph-ramsey_images/imageFile25.png>)

![image 26](<2015-conlon-recent-developments-graph-ramsey_images/imageFile26.png>)

For s = 3, this result was shown to be sharp up to the constant by Kim [141]. That is, he showed that there exists a positive constant c′ such that

t2 log t

r(3,t) ≥ c′

.

![image 27](<2015-conlon-recent-developments-graph-ramsey_images/imageFile27.png>)

This improved on earlier work of Erd˝os [79], who used an intricate probabilistic argument to show that r(3,t) ≥ c′(t/log t)2, a result which was subsequently reproved using the local lemma [199].

Kim’s proof of this bound was a landmark application of the so-called semi-random method. Recently, an alternative proof was found by Bohman [20] using the triangle-free process. This is a stochastic graph process where one starts with the empty graph on N vertices and adds one edge at a time to create a graph. At each step, we randomly select an edge which is not in the graph and add it to the graph if and only if it does not complete a triangle. The process runs until every non-edge is contained in a triangle. By analysing the independence number of the resulting graph, Bohman was able to reprove Kim’s bound. More recently, Bohman and Keevash [22] and, independently, Fiz Pontiveros, Griﬃths and Morris [104] gave more precise estimates for the running time of the triangle-free process and as a consequence proved the following result.

- Theorem 2.4.


r(3,t) ≥

1 4 − o(1)

![image 28](<2015-conlon-recent-developments-graph-ramsey_images/imageFile28.png>)

t2 log t

.

![image 29](<2015-conlon-recent-developments-graph-ramsey_images/imageFile29.png>)

This is within an asymptotic factor of 4 of the best upper bound, due to Shearer [190], who showed that

t2 log t

r(3,t) ≤ (1 + o(1))

.

![image 30](<2015-conlon-recent-developments-graph-ramsey_images/imageFile30.png>)

This is already a very satisfactory state of aﬀairs, though it would be of great interest to improve either bound further.

For general s, the best lower bound is due to Bohman and Keevash [21] and uses the analogous Ks-free process. Their analysis shows that for any s there exists a positive constant c′s such that

ts+12 (log t)

![image 31](<2015-conlon-recent-developments-graph-ramsey_images/imageFile31.png>)

r(s,t) ≥ c′s

2 −s−12 .

![image 32](<2015-conlon-recent-developments-graph-ramsey_images/imageFile32.png>)

s+1

![image 33](<2015-conlon-recent-developments-graph-ramsey_images/imageFile33.png>)

![image 34](<2015-conlon-recent-developments-graph-ramsey_images/imageFile34.png>)

Even for s = 4, there is a polynomial diﬀerence between the upper and lower bounds. Bringing these bounds closer together remains one of the most tantalising open problems in Ramsey theory.

Before concluding this section, we say a little about the multicolour generalisations of these problems. An easy extension of the Erd˝os–Szekeres argument gives an upper bound for the multicolour diagonal Ramsey number of the form r(t;q) ≤ qqt. On the other hand, an elementary product argument shows that, for any positive integers p and d, we have r(t;pd) > (r(t;p) − 1)d. In particular, taking p = 2, we see that r(t;q) > (r(t;2) − 1)q/2 > 2qt/4 for q even and t ≥ 3. To prove the bound, suppose that χ is a p-colouring of the edges of the complete graph on vertex set [r(t;p) − 1] = {1,2,... ,r(t;p) − 1} with no monochromatic Kt and consider the lexicographic dth power of χ. This is a pd-colouring of the edges of the complete graph with vertex set [r(t;p)−1]d such that the colour of the edge between two distinct vertices (u1,... ,ud) and (v1,... ,vd) is (i,χ(ui,vi)), where i is the ﬁrst coordinate for which ui = vi. It is easy to check that this colouring contains no monochromatic Kt. Since the set has (r(t;p) − 1)d vertices, the result follows.

The key question in the multicolour case is to determine the dependence on the number of colours. Even for t = 3, we only know that

2c′q ≤ r(3;q) ≤ cq!,

where c ≤ e and c′ ≥ 1 are constants whose values have each been improved a little over time. It is a major open problem to improve these bounds by a more signiﬁcant factor.

In the oﬀ-diagonal case, less seems to be known, but we would like to highlight one result. While it is easy to see that

Kt) = O(tq),

r(K3,... ,K3,

![image 35](<2015-conlon-recent-developments-graph-ramsey_images/imageFile35.png>)

![image 36](<2015-conlon-recent-developments-graph-ramsey_images/imageFile36.png>)

q−1

it was an open question for many years to even show that the ratio r(K3,K3,Kt)/r(K3,Kt) tends to inﬁnity with t. Alon and Ro¨dl [9] solved this problem in a strong form by showing that the bound quoted above is tight up to logarithmic factors for all q. Their elegant construction involves overlaying a collection of random shifts of a suﬃciently pseudorandom triangle-free graph.

## 2.2 Complete hypergraphs

Although there are already signiﬁcant gaps between the lower and upper bounds for graph Ramsey numbers, our knowledge of hypergraph Ramsey numbers is even weaker. Recall that rk(s,t) is the minimum N such that every red/blue-colouring of the k-tuples of an N-element set contains a red Ks(k) or a blue Kt(k). While a naive extension of the Erd˝os–Szekeres argument gives extremely poor bounds for hypergraph Ramsey numbers when k ≥ 3, a more careful induction, discovered by Erd˝os and Rado [99], allows one to bound Ramsey numbers for k-uniform hypergraphs using estimates for the Ramsey number of (k −1)-uniform hypergraphs. Quantitatively, their result says the following.

- Theorem 2.5. rk(s,t) ≤ 2(rk−1(s−1,t−1)


k−1 ) + k − 2.

Together with the standard exponential upper bound on r(t), this shows that r3(t) ≤ 22ct for some constant c. On the other hand, by considering a random two-colouring of the edges of KN(k), Erd˝os, Hajnal and Rado [98] showed that there is a positive constant c′ such that r3(t) ≥ 2c′t2. However, they conjectured that the upper bound is closer to the truth and Erd˝os later oﬀered a $500 reward for a proof.

Conjecture 2.6. There exists a positive constant c′ such that

′t.

r3(t) ≥ 22c

Fifty years after the work of Erd˝os, Hajnal and Rado, the bounds for r3(t) still diﬀer by an exponential. Similarly, for k ≥ 4, there is a diﬀerence of one exponential between the known upper and lower bounds for rk(t), our best bounds being

tk−1(c′t2) ≤ rk(t) ≤ tk(ct),

where the tower function tk(x) is deﬁned by t1(x) = x and ti+1(x) = 2ti(x). The upper bound here is a straightforward consequence of Theorem 2.5, while the lower bound follows from an ingenious construction of Erd˝os and Hajnal known as the stepping-up lemma (see, e.g., Chapter 4.7 in [130]). This allows one to construct lower bound colourings for uniformity k + 1 from colourings for uniformity k, eﬀectively gaining an extra exponential each time it is applied. Unfortunately, the smallest k for which it works is k = 3. However, if we could prove that r3(t) is double exponential in t, this would automatically close the gap between the upper and lower bounds for rk(t) for all uniformities k.

For more than two colours, the problem becomes easier and Erd˝os and Hajnal (see [130]) were able to construct a 4-colouring of the triples of a set of double-exponential size which does not contain a monochromatic clique of order t. By a standard extension of the Erd˝os–Rado upper bound to more than two colours, this result is sharp.

- Theorem 2.7. There exists a positive constant c′ such that


′t.

r3(t;4) ≥ 22c

We will now sketch this construction, since it is a good illustration of how the stepping-up lemma works. Let m = 2(t−1)/2 and suppose we are given a red/blue-colouring χ of the edges of Km with no monochromatic clique of order t − 1 (in Section 2.1, we showed that such a colouring exists). Let N = 2m and consider the set of all binary strings of length m, where each string corresponds to the binary representation of an integer between 0 and N − 1. For any two strings x and y, let δ(x,y) be the largest index in which they diﬀer. Note that if x < y < z (as numbers), then we have that δ(x,y) = δ(y,z) and δ(x,z) is the maximum of δ(x,y) and δ(y,z). More generally, if x1 < ··· < xt, then δ(x1,xt) = maxi δ(xi,xi+1). Given vertices x < y < z with δ1 = δ(x,y) and δ2 = δ(y,z), we let the colour of (x,y,z) be

- • A if δ1 < δ2 and χ(δ1,δ2) = red;
- • B if δ1 < δ2 and χ(δ1,δ2) = blue;
- • C if δ1 > δ2 and χ(δ1,δ2) = red;
- • D if δ1 > δ2 and χ(δ1,δ2) = blue.


Suppose now that x1 < ··· < xt is a monochromatic set in colour A (the other cases are similar) and let δi = δ(xi,xi+1). We claim that δ1,... ,δt−1 form a red clique in the original colouring of Km, which is a contradiction. Indeed, since (xi,xi+1,xi+2) has colour A, we must have that δi < δi+1 for all i. Therefore, δ1 < ··· < δt−1 and δ(xi+1,xj+1) = δ(xj,xj+1) = δj for all i < j. Since the colour of the triple (xi,xi+1,xj+1) is determined by the colour of (δi,δj), this now tells us that χ(δi,δj) is red for all i < j, as required.

For the intermediate case of three colours, Erd˝os and Hajnal [94] made a small improvement on the lower bound of 2c′t2, showing that r3(t;3) ≥ 2c′t2 log2 t. Extending the stepping-up approach described above, the authors [55] improved this bound as follows, giving a strong indication that r3(t;3) is indeed double exponential.

- Theorem 2.8. There exists a positive constant c′ such that


′ logt.

r3(t;3) ≥ 2tc

′t, he and Hajnal [94] discovered the following interesting fact which they thought might indicate the opposite. They proved that there are positive constants c and ǫ such that every two-colouring of the triples of an N-element set contains a subset S of order s ≥ c(log N)1/2 such that at least (1/2 + ǫ) 3 s triples of S have the same colour. That is, the density of each colour deviates from 1/2 by at least some ﬁxed positive constant.

Though Erd˝os [41, 85] believed that r3(t) is closer to 22c

In the graph case, a random colouring of the edges of KN has the property that every subset of order ω(log N) has roughly the same number of edges in both colours. That is, the Ramsey problem and the discrepancy problem have similar quantitative behaviour. Because of this, Erd˝os [87] remarked that he would begin to doubt that r3(t) is double exponential in t if one could prove that any two-colouring of the triples of an N-set contains some set of order s = c(ǫ)(log N)δ for which at least (1 − ǫ) 3 s triples have the same colour, where δ > 0 is an absolute constant and ǫ > 0 is

arbitrary. Erd˝os and Hajnal proposed [94] that such a statement may even be true with δ = 1/2, which would be tight up to the constant factor c. The following result, due to the authors [57], shows that this is indeed the case.

- Theorem 2.9. For each ǫ > 0, there is c = c(ǫ) > 0 such that every two-colouring of the triples of


an N-element set contains a subset S of order s = c√log N such that at least (1 − ǫ) 3 s triples of S have the same colour.

![image 37](<2015-conlon-recent-developments-graph-ramsey_images/imageFile37.png>)

Unlike Erd˝os, we do not feel that this result suggests that the growth of r3(t) is smaller than double exponential. Indeed, this theorem also holds for any ﬁxed number of colours q but, for q ≥ 4, the hypergraph Ramsey number does grow as a double exponential. That is, the q-colour analogue of Theorem 2.9 shows that the largest almost monochromatic subset in a q-colouring of the triples of an N-element set is much larger than the largest monochromatic subset. This is in striking constrast to graphs, where we have already remarked that the two quantities have the same order of magnitude.

It would be very interesting to extend Theorem 2.9 to higher uniformities. In [55], the authors proved that for all k,q and ǫ > 0 there is δ = δ(k,q,ǫ) > 0 such that every q-colouring of the ktuples of an N-element set contains a subset of order s = (log N)δ which contains at least (1−ǫ) k s k-tuples of the same colour. Unfortunately, δ here depends on ǫ. On the other hand, this result could hold with δ = 1/(k − 1) (which is the case for k = 3).

Problem 2.10. Is it true that for any k ≥ 4 and ǫ > 0 there exists c = c(k,ǫ) > 0 such that every two-colouring of the k-tuples of an N-element set contains a subset S of order s = c(log N)1/(k−1) such that at least (1 − ǫ) k s k-tuples of S have the same colour?

Another wide open problem is that of estimating oﬀ-diagonal Ramsey numbers for hypergraphs. Progress on this question was slow and for several decades the best known bound was that obtained by Erd˝os and Rado [99]. Combining their estimate from Theorem 2.5 with the best upper bound on r(s − 1,t − 1) shows that for ﬁxed s,

r3(s,t) ≤ 2(r(s−1,t−1)

2 ) + 1 ≤ 2ct2s−4/log2s−6 t.

Recently, the authors [55] discovered an interesting connection between the problem of bounding r3(s,t) and a new game-theoretic parameter. To describe this parameter, we start with the classical approach of Erd˝os and Rado and then indicate how it can be improved.

Let p = r(s − 1,t − 1),N = 2(p2) + 1 and consider a red/blue-colouring c of all triples on the vertex set [N] = {1,2,... ,N}. We will show how to ﬁnd vertices v1,... ,vp,vp+1 such that, for each i < j, all triples (vi,vj,vk) with k > j have the same colour, which we denote by χ(i,j). This will solve the problem, since, by the deﬁnition of p, the colouring χ of v1,... ,vp contains either a red Ks−1 or a blue Kt−1, which together with vp+1 would give a monochromatic set of triples of the correct order in the original colouring. We will pick the vertices vi in rounds. Suppose that we already have vertices v1,... ,vm with the required property as well as a set of vertices Sm such that for every vi,vj and every w ∈ Sm the colour of the triple (vi,vj,w) is given by χ(i,j) and so does not depend on w. Pick vm+1 ∈ Sm arbitrarily. For all other w in Sm, consider the colour vector (c1,... ,cm) such that ci = c(vi,vm+1,w), which are the only new triples we need worry about. Let

Sm+1 be the largest subset of Sm such that every vertex in this subset has the same colour vector (c1,... ,cm). Clearly, this set has order at least 2−m(|Sm| − 1). Notice that v1,... ,vm+1 and Sm+1 have the desired properties. We may therefore continue the algorithm, noting that we have lost a factor of 2m in the size of the remaining set of vertices, i.e., a factor of 2 for every edge coloured by χ.

To improve this approach, we note that the colouring χ does not need to colour every pair of vertices. This idea is captured nicely by the notion of vertex on-line Ramsey number. Consider the following game, played by two players, Builder and Painter: at step m + 1 a new vertex vm+1 is revealed; then, for every existing vertex vj, j = 1,··· ,m, the Builder decides, in order, whether to draw the edge vjvm+1; if he does expose such an edge, the Painter has to colour it either red or blue immediately. The vertex on-line Ramsey number r˜v(k,l) is then deﬁned as the minimum number of edges that Builder has to draw in order to force Painter to create a red Kk or a blue Kl. Using an approach similar to that described in the previous paragraph, one can bound the Ramsey number r3(s,t) roughly by an exponential in r˜v(s − 1,t − 1). By estimating r˜v(s − 1,t − 1), this observation, together with some additional ideas, allowed the authors to improve the Erd˝os–Rado estimate for oﬀ-diagonal hypergraph Ramsey numbers as follows.

- Theorem 2.11. For every natural number s ≥ 4, there exists a positive constant c such that r3(s,t) ≤ 2cts−2 logt.


A similar improvement for oﬀ-diagonal Ramsey numbers of higher uniformity follows from combining this result with Theorem 2.5.

How accurate is this estimate? For the ﬁrst non-trivial case, when s = 4, the problem was ﬁrst considered by Erd˝os and Hajnal [92] in 1972. Using the following clever construction, they showed that r3(4,t) is exponential in t. Consider a random tournament with vertex set [N]. This is a complete graph on N vertices whose edges are oriented uniformly at random. Colour a triple in [N] red if it forms a cyclic triangle and blue otherwise. Since it is well known and easy to show that every tournament on four vertices contains at most two cyclic triangles and a random tournament on N vertices with high probability does not contain a transitive subtournament of order clog N, the resulting colouring has neither a red subset of order 4 nor a blue subset of order clog N. In the same paper [92], Erd˝os and Hajnal conjectured that logr3t(4,t) → ∞. This was recently conﬁrmed in [55], where the authors obtained a more general result which in particular implies that r3(4,t) ≥ 2c′tlogt. This should be compared with the upper bound r3(4,t) ≤ 2ct2 logt obtained above.

![image 38](<2015-conlon-recent-developments-graph-ramsey_images/imageFile38.png>)

## 2.3 Sparse graphs

After the complete graph, the next most classical topic in graph Ramsey theory concerns the Ramsey numbers of sparse graphs, i.e., graphs with certain constraints on the degrees of the vertices. Burr and Erd˝os [30] initiated the study of these Ramsey numbers in 1975 and this topic has since placed a central role in graph Ramsey theory, leading to the development of many important techniques with broader applicability.

In their foundational paper, Burr and Erd˝os [30] conjectured that for every positive integer ∆ there is a constant c(∆) such that every graph H with n vertices and maximum degree ∆ satisﬁes r(H) ≤ c(∆)n. This conjecture was proved by Chv´atal, Ro¨dl, Szemere´di and Trotter [44] as an early application of Szemere´di’s regularity lemma [207]. We will now sketch their proof, ﬁrst reviewing the statement of the regularity lemma.

Roughly speaking, the regularity lemma says that the vertex set of any graph may be partitioned into a small number of parts such that the bipartite subgraph between almost every pair of parts is random-like. More formally, we say that a pair of disjoint vertex subsets (A,B) in a graph G is ǫ-regular if, for every A′ ⊆ A and B′ ⊆ B with |A′| ≥ ǫ|A| and |B′| ≥ ǫ|B|, the density d(A′,B′) of edges between A′ and B′ satisﬁes |d(A′,B′) − d(A,B)| ≤ ǫ. That is, the density between any two large subsets of A and B is close to the density between A and B. The regularity lemma then says that for every ǫ > 0 there exists M = M(ǫ) such that the vertex set of any graph G may be partitioned into m ≤ M parts V1,... ,Vm such that ||Vi| − |Vj|| ≤ 1 for all 1 ≤ i,j ≤ m and all but ǫ m2 pairs (Vi,Vj) are ǫ-regular.

Suppose now that N = c(∆)n and the edges of KN have been two-coloured. To begin, we apply the regularity lemma with approximation parameter ǫ = 4−∆ (since the colours are complementary, we may apply the regularity lemma to either the red or the blue subgraph, obtaining a regular partition for both). This gives a partition of the vertex set into m ≤ M parts of roughly equal size, where M depends only on ∆, such that all but ǫ m2 pairs of parts are ǫ-regular. By applying Tura´n’s theorem, we may ﬁnd 4∆ parts such that every pair of parts is ǫ-regular. Since r(∆ + 1) ≤ 4∆, an application of Ramsey’s theorem then implies that there are ∆ + 1 parts V1,... ,V∆+1 such that every pair is ǫ-regular and the graph between each pair has density at least 1/2 in one particular colour, say red. As χ(H) ≤ ∆ + 1, we can partition the vertex set of H into independent sets

- U1,... ,U∆+1. The regularity between the sets V1,... ,V∆+1 now allows us to greedily construct a red copy of H, embedding one vertex at a time and mapping Ui into Vi for each i. Throughout the embedding process, we must ensure that for any vertex u of Ui which is not yet embedded the set of potential vertices in Vi into which one may embed u is large (at step t, we guarantee that it has order at least 4−d(t,u)|Vi| − t, where d(t,u) ≤ ∆ is the number of neighbours of u among the ﬁrst t embedded vertices). Though an elegant application of the regularity lemma, this method gives a poor bound on c(∆), namely, a tower of 2s with height exponential in ∆.


Since this theorem was ﬁrst proved, the problem of determining the correct order of magnitude for c(∆) as a function of ∆ has received considerable attention from various researchers. The ﬁrst progress was made by Eaton [76], who showed that c(∆) ≤ 22c∆ for some ﬁxed c, the key observation being that the proof above does not need the full strength of the regularity lemma. Instead, one only needs to ﬁnd 4∆ large vertex subsets such that the graph between each pair is ǫ-regular. This may be achieved using a weak regularity lemma due to Duke, Lefmann and Ro¨dl [75].

A novel approach of Graham, Ro¨dl and Rucinski [128] was the ﬁrst to give a linear upper bound on Ramsey numbers of bounded-degree graphs without using any form of the regularity lemma. Their proof also gave good quantitative control, showing that one may take c(∆) ≤ 2c∆ log2 ∆. As in the regularity proof, they try to greedily construct a red copy of H one vertex at a time, at each step ensuring that the set of potential vertices into which one might embed any remaining vertex is large. If this process fails, we will ﬁnd two large vertex subsets such that the red graph between

- them has very low density. Put diﬀerently, this means that the blue graph between these vertex sets has very high density. We now iterate this procedure within each of the two subsets, trying to embed greedily in red and, if this fails, ﬁnding two large vertex subsets with high blue density between them. After log 8∆ iterations, we will either have found the required red copy of H or we will have 8∆ subsets of equal size with high blue density between all pairs of sets. If the constants are chosen appropriately, the union of these sets will have blue density at least 1 − 4∆1 and at least

![image 39](<2015-conlon-recent-developments-graph-ramsey_images/imageFile39.png>)

4n vertices. One can then greedily embed a blue copy of H one vertex at a time. Recently, the authors [58] improved this bound to c(∆) ≤ 2c∆log ∆.

Theorem 2.12. There exists a constant c such that any graph H on n vertices with maximum degree ∆ satisﬁes

r(H) ≤ 2c∆ log ∆n.

In the approach of Graham, Ro¨dl and Rucin´ski, the two colours play asymmetrical roles. Either we ﬁnd a set where the red graph has some reasonable density between any two large vertex subsets or a set which is almost complete in blue. In either case, a greedy embedding gives the required monochromatic copy of H. The approach we take in [58] is more symmetrical. The basic idea is that once we ﬁnd a pair of vertex subsets (V1,V2) such that the graph between them is almost complete in blue, we split H into two parts U1 and U2, each of which induces a subgraph of maximum degree at most ∆/2, and try to embed blue copies of H[Ui] into Vi for i = 1,2, using the high blue density between V1 and V2 to ensure that this gives a blue embedding of H. The gain comes from the fact that when we iterate the maximum degree of the graph we wish to embed shrinks. Unfortunately, while this gives some of the intuition behind the proof, the details are rather more involved.

Graham, Ro¨dl and Rucinski [129] observed that for bipartite graphs H on n vertices with maximum degree ∆ their technique could be used to prove a bound of the form r(H) ≤ 2c∆log ∆n. Indeed, if greedily embedding a red copy of H fails, then there will be two large vertex subsets V1 and V2 such that the graph between them is almost complete in blue. A blue copy of H can

- then be greedily embedded between these sets. In the other direction, they showed that there is a positive constant c′ such that for each ∆ and n suﬃciently large there is a bipartite graph H on n vertices with maximum degree ∆ for which r(H) ≥ 2c′∆n. Conlon [46] and, independently, Fox and Sudakov [116] showed that this bound is essentially tight, that is, there is a constant c such that r(H) ≤ 2c∆n for every bipartite graph H on n vertices with maximum degree ∆. Both proofs are quite similar, each relying on an application of dependent random choice and a hypergraph embedding lemma.


Dependent random choice is a powerful probabilistic technique which has recently led to a number of advances in extremal graph theory, additive combinatorics, Ramsey theory and combinatorial geometry. Early variants of this technique were developed by Gowers [125], Kostochka and Ro¨dl [147] and Sudakov [202]. In many applications, including that under discussion, the technique is used to prove the useful fact that every dense graph contains a large subset U in which almost every set of d vertices has many common neighbours. To prove this fact, we let R be a random set of vertices from our graph and take U to be the set of all common neighbours of R. Intuitively, it is clear that if some subset of U of order d has only a few common neighbours, then it is unlikely that all the members of R could have been chosen from this set of neighbours. It is therefore unlikely

that U contains many subsets of this type. For more information about dependent random choice and its applications, we refer the interested reader to the recent survey [118].

Using the Lov´asz local lemma, the authors [62] recently improved on the hypergraph embedding lemmas used in their earlier proofs to obtain a bound of the form r(H) ≤ c2∆n for every bipartite graph H on n vertices with maximum degree ∆. Like the earlier results, this follows from a more general density result which shows that the denser of the two colour classes will contain the required monochromatic copy of H.

By repeated application of the dependent random choice technique and an appropriate adaptation of the embedding technique, Fox and Sudakov [116] also proved that r(H) ≤ 24χ∆n for all graphs H on n vertices with chromatic number χ and maximum degree ∆. However, the dependency on χ is unlikely to be necessary here.

- Conjecture 2.13. There is a constant c such that every graph H on n vertices with maximum degree ∆ satisﬁes r(H) ≤ 2c∆n.

One particular family of bipartite graphs that has received signiﬁcant attention in Ramsey theory are hypercubes. The hypercube Qn is the n-regular graph on vertex set {0,1}n where two vertices are connected by an edge if and only if they diﬀer in exactly one coordinate. Burr and Erd˝os [30] conjectured that r(Qn) is linear in |Qn|.

- Conjecture 2.14. r(Qn) = O(2n).

After several improvements over the trivial bound r(Qn) ≤ r(|Qn|) ≤ 4|Qn| = 22n+1 by Beck [15], Graham, Ro¨dl and Rucin´ski [129], Shi [194, 195] and Fox and Sudakov [116], the authors [62] obtained the best known upper bound of r(H) = O(22n), which is quadratic in the number of vertices. This follows immediately from the general upper bound on Ramsey numbers of bipartite graphs with given maximum degree stated earlier.

Another natural notion of sparseness which has been studied extensively in the literature is that of degeneracy. A graph is said to be d-degenerate if every subgraph has a vertex of degree at most d. Equivalently, a graph is d-degenerate if there is an ordering of the vertices such that each vertex has at most d neighbours that precede it in the ordering. The degeneracy of a graph is the smallest d such that the graph is d-degenerate. Burr and Erd˝os [30] conjectured that every graph with bounded degeneracy has linear Ramsey number.

- Conjecture 2.15. For every natural number d, there is a constant c(d) such that every d-degenerate graph H on n vertices satisﬁes r(H) ≤ c(d)n.


This conjecture is one of the most important open problems in graph Ramsey theory. The ﬁrst signiﬁcant progress on the conjecture was made by Kostochka and Sudakov [149], who proved an almost linear upper bound. That is, for ﬁxed d, they showed that every d-degenerate graph H on n vertices satisﬁes r(H) = n1+o(1). This result was later reﬁned by Fox and Sudakov [117], who showed that every d-degenerate graph H on n vertices satisﬁes r(H) ≤ ec(d)

√lognn.

![image 40](<2015-conlon-recent-developments-graph-ramsey_images/imageFile40.png>)

Partial progress of a diﬀerent sort was made by Chen and Schelp [37], who considered a notion of sparseness which is intermediate between having bounded degree and having bounded degeneracy.

We say that a graph is p-arrangeable if there is an ordering v1,v2,... ,vn of its vertices such that for each vertex vi, its neighbours to the right of vi have together at most p neighbours to the left of vi (including vi). The arrangeability of a graph is the smallest p such that the graph is p-arrangeable. Extending the result of Chv´atal et al. [44], Chen and Schelp [37] proved that for every p there is a constant c(p) such that every p-arrangeable graph on n vertices has Ramsey number at most c(p)n. Graphs with bounded arrangeability include planar graphs and graphs embeddable on a ﬁxed surface. More generally, Ro¨dl and Thomas [185] proved that graphs which do not contain a subdivision of a ﬁxed graph have bounded arrangeability and hence have linear Ramsey number. Another application was given by Fox and Sudakov [117], who proved that for ﬁxed d the Erd˝os– Renyi random graph G(n,d/n) almost surely has arrangeability on the order of d2 and hence almost surely has linear Ramsey number.

In general, the Ramsey number of a graph appears to be intimately connected to its degeneracy. Indeed, if d(H) is the degeneracy of H, a random colouring easily implies that r(H) ≥ 2d(H)/2. Since it is also clear that r(H) ≥ n for any n-vertex graph, we see that log r(H) = Ω(d(H)+log n). We conjecture that this bound is tight up to the constant. It is even plausible that r(H) ≤ 2O(d)n for every d-degenerate graph H on n vertices. Since the degeneracy of a graph is easily computable, this would give a very satisfying approximation for the Ramsey number of a general graph.

- Conjecture 2.16. For every n-vertex graph H, log r(H) = Θ(d(H) + log n).

For graphs of bounded chromatic number, Conjecture 2.16 follows from a bound on Ramsey numbers due to Fox and Sudakov (Theorem 2.1 in [117]). Moreover, another result from the same paper (Theorem 3.1 in [117]) shows that Conjecture 2.16 always holds up to a factor of log2 d(H).

In graph Ramsey theory, it is natural to expect there should be no signiﬁcant qualitative diﬀerence between the bounds for two colours and the bounds for any ﬁxed number of colours. However, there are many well-known problems where this intuition has yet to be veriﬁed, the classic example being the bounds for hypergraph Ramsey numbers. Another important example is furnished by the results of this section. Indeed, the proof technique of Graham, Ro¨dl and Rucin´ski can be extended to work for more than two colours, but only gives the estimate r(H;q) ≤ 2∆q−1+o(1)n for the Ramsey number of graphs H with n vertices and maximum degree ∆. While dependent random choice does better, giving a bound of the form r(H;q) ≤ 2Oq(∆2)n, we believe that for a ﬁxed number of colours, the exponent of ∆ should still be 1. In particular, we conjecture that the following bound holds.

- Conjecture 2.17. For every graph H on n vertices with maximum degree ∆, the 3-colour Ramsey number of H satisﬁes


r(H,H,H) ≤ 2∆1+o(1)n, where the o(1) is a function of ∆ which tends to 0 as ∆ tends to inﬁnity.

With the development of the hypergraph regularity method [126, 164, 183], the result that bounded-degree graphs have linear Ramsey numbers was extended to 3-uniform hypergraphs by Cooley, Fountoulakis, Ku¨hn and Osthus [66] and Nagle, Olsen, Ro¨dl and Schacht [163] and to

k-uniform hypergraphs by Cooley et al. [67]. That is, for each k and ∆ there is c(∆,k) such that every k-uniform hypergraph H on n vertices with maximum degree ∆ satisﬁes r(H) ≤ c(∆,k)n. However, because they use the hypergraph regularity lemma, their proof only gives an enormous Ackermann-type upper bound on c(∆,k). In [54], the authors gave another shorter proof of this theorem which gives the right type of behaviour for c(∆,k). The proof relies on an appropriate generalisation of the dependent random choice technique to hypergraphs. As in Section 2.2, we write t1(x) = x and ti+1(x) = 2ti(x).

- Theorem 2.18. For any natural numbers k ≥ 3 and q ≥ 2, there exists a constant c = c(k,q) such that the q-colour Ramsey number of any k-uniform hypergraph H on n vertices with maximum degree ∆ satisﬁes

r3(H;q) ≤ 22c∆log∆n and, for k ≥ 4, rk(H;q) ≤ tk(c∆)n.

We say that a hypergraph is d-degenerate if every subgraph has a vertex of degree at most d. Equivalently, a hypergraph is d-degenerate if there is an ordering of the vertices v1,v2,... ,vn such that each vertex vi is the ﬁnal vertex in at most d edges in this ordering. Kostochka and Ro¨dl [148] showed that the hypergraph analogue of the Burr–Erdo˝s conjecture is false for uniformity k ≥ 4. In particular, they constructed a 4-uniform hypergraph on n vertices which is 1-degenerate but has Ramsey number at least 2Ω(n1/3).

- 2.4 Graphs with a given number of edges


In 1973, Erd˝os and Graham [89] conjectured that among all connected graphs with m = n2 edges, the complete graph has the largest Ramsey number. As this question seems unapproachable,

Erd˝os [84] asked whether one could at least show that the Ramsey number of any graph with m edges is not substantially larger than that of the complete graph with the same size. Since the number of vertices in a complete graph with m edges is a constant multiple of √m, he conjectured that there exists a constant c such that r(H) ≤ 2c

![image 41](<2015-conlon-recent-developments-graph-ramsey_images/imageFile41.png>)

√m for any graph H with m edges and no isolated vertices.

![image 42](<2015-conlon-recent-developments-graph-ramsey_images/imageFile42.png>)

The ﬁrst progress on this conjecture was made by Alon, Krivelevich and Sudakov [5], who showed that there exists a constant c such that r(H) ≤ 2c

√mlogm for any graph H with m edges and no isolated vertices. They also proved the conjecture in the special case where H is bipartite. Another proof of the same bound, though starting from a diﬀerent angle, was later given by Conlon [49]. This approach, which focused on estimating the Ramsey number of graphs with a given density, allowed one to show that graphs on n vertices with o(n2) edges have Ramsey number 2o(n). Soon after this work, Erd˝os’ conjecture was completely resolved by Sudakov [205], so that it may now be stated as a theorem.

![image 43](<2015-conlon-recent-developments-graph-ramsey_images/imageFile43.png>)

- Theorem 2.19. There exists a constant c such that any graph H with m edges and no isolated vertices satisﬁes


√m.

![image 44](<2015-conlon-recent-developments-graph-ramsey_images/imageFile44.png>)

r(H) ≤ 2c

The proof of this theorem relies upon several ingredients, including the machinery of Graham, Ro¨dl and Rucin´ski [128] mentioned in the previous section and a result of Erd˝os and Szemere´di [103]

which says that if a graph has low density then it contains a larger clique or independent set than would be guaranteed by Ramsey’s theorem alone.3 However, these techniques are very speciﬁc to two colours, so the following problem remains wide open.

√m for any graph H with m edges and no isolated vertices.

![image 45](<2015-conlon-recent-developments-graph-ramsey_images/imageFile45.png>)

- Problem 2.20. Show that for any q ≥ 3 there exists cq such that r(H;q) ≤ 2cq


If no vertex in the graph H has unusually high degree, it is often possible to improve on

- Theorem 2.19. For example, the following result [49, 53] implies that if a graph with n vertices and


- m edges has degeneracy at most 10m/n, say, then the Ramsey number is at most an exponential in mn log2(nm2). For m = o(n2), this is signiﬁcantly smaller than √m.


![image 46](<2015-conlon-recent-developments-graph-ramsey_images/imageFile46.png>)

![image 47](<2015-conlon-recent-developments-graph-ramsey_images/imageFile47.png>)

![image 48](<2015-conlon-recent-developments-graph-ramsey_images/imageFile48.png>)

- Theorem 2.21. There exists a constant c such that any graph H on n vertices with degeneracy at most d satisﬁes


r(H) ≤ 2cdlog2(2n/d).

The analogous question for hypergraphs was studied by the authors in [54]. Though the same rationale that led Erd˝os to conjecture Theorem 2.19 naturally leads one to conjecture that r3(H) ≤ 22cm

1/3

for all 3-uniform hypergraphs H with m edges and no isolated vertices, it turns out that there are connected 3-uniform hypergraphs H with m edges for which r3(H;4) ≥ 22c

′√m. This is also close to being sharp, since r3(H;q) ≤ 22cq

![image 49](<2015-conlon-recent-developments-graph-ramsey_images/imageFile49.png>)

√mlogm for any 3-uniform hypergraph H with

![image 50](<2015-conlon-recent-developments-graph-ramsey_images/imageFile50.png>)

- m edges and no isolated vertices and any q ≥ 2. For higher uniformities, k ≥ 4, one can do slightly better. Writing t1(x) = x and ti+1(x) = 2ti(x) as in Section 2.2, the authors showed that rk(H;q) ≤ tk(ck,q√m) for any k-uniform hypergraph H with m edges and no isolated vertices and any q ≥ 2. It would be interesting to improve the bound in the 3-uniform case to bring it in line with higher uniformities.


![image 51](<2015-conlon-recent-developments-graph-ramsey_images/imageFile51.png>)

√m for any

![image 52](<2015-conlon-recent-developments-graph-ramsey_images/imageFile52.png>)

- Problem 2.22. Show that for any q ≥ 2 there exists cq such that r3(H;q) ≤ 22cq


3-uniform hypergraph H with m edges and no isolated vertices. This would likely follow if the bound for the Ramsey number of 3-uniform hypergraphs with n vertices and maximum degree ∆ given in Theorem 2.18 could be improved to 22c∆n.

## 2.5 Ramsey goodness

If one tries to prove a lower bound for the oﬀ-diagonal Ramsey number r(G,H), one simple construction, usually attributed to Chv´atal and Harary [43], is to take χ(H) − 1 red cliques, each of order |G| − 1, and to colour all edges between these sets in blue. If G is connected, this colouring clearly contains no red copy of G and no blue copy of H and so r(G,H) ≥ (|G| − 1)(χ(H) −1) +1. If we write σ(H) for the order of the smallest colour class in any χ(H)-colouring of the vertices of

![image 53](<2015-conlon-recent-developments-graph-ramsey_images/imageFile53.png>)

3The Erd˝s–Szemere´di theorem is the starting point for another interesting topic which we have not had space to discuss, namely, the problem of determining what properties a graph with no clique or independent set of order c log n must satisfy. The Erd˝s–Szemere´di theorem shows that any such graph must have density bounded away from both 0 and 1 and there are numerous further papers (see, for example, [3, 27, 114] and their references) showing that these graphs must exhibit random-like behaviour.

H, we see, provided |G| ≥ σ(H), that we may add a further red clique of order σ(H) − 1 to our construction. This additional observation, due to Burr [28], allows us to improve our lower bound to

r(G,H) ≥ (|G| − 1)(χ(H) − 1) + σ(H), provided |G| ≥ σ(H). Following Burr and Erd˝os [28, 31], we will say that a graph G is H-good if this inequality is an equality, that is, if r(G,H) = (|G| − 1)(χ(H) − 1) + σ(H). Given a family of graphs G, we say that G is H-good if equality holds for all suﬃciently large graphs G ∈ G. In the particular case where H = Ks, we say that a graph or family of graphs is s-good.

The classical result on Ramsey goodness, which predates the deﬁnition, is the theorem of Chv´atal [42] showing that all trees are s-good for every s. However, the family of trees is not H-good for every graph H. For example [32], there is a constant c < 12 such that r(K1,t,K2,2) ≥ t+√t−tc for t suﬃciently large, whereas (|K1,t| − 1)(χ(K2,2) − 1) + σ(K2,2) = t + 2.

![image 54](<2015-conlon-recent-developments-graph-ramsey_images/imageFile54.png>)

![image 55](<2015-conlon-recent-developments-graph-ramsey_images/imageFile55.png>)

In an eﬀort to determine what properties contribute to being good, Burr and Erd˝os [29, 31] conjectured that if ∆ is ﬁxed then the family of graphs with maximum degree at most ∆ is s-good for every s. However, this conjecture was disproved by Brandt [26], who showed that if a graph is a good expander then it cannot be 3-good. In particular, his result implies that for ∆ ≥ ∆0 almost every ∆-regular graph on a suﬃciently large number of vertices is not 3-good.

On the other hand, graphs with poor expansion properties are often good. The ﬁrst such result, due to Burr and Erd˝os [31], states that for any ﬁxed ℓ the family of connected graphs with bandwidth at most ℓ is s-good for any s, where the bandwidth of a graph G is the smallest number ℓ for which there exists an ordering v1,v2,... ,vn of the vertices of G such that every edge vivj satisﬁes |i − j| ≤ ℓ. This result was recently extended by Allen, Brightwell and Skokan [2], who showed that the set of connected graphs with bandwidth at most ℓ is H-good for every H. Their result even allows the bandwidth ℓ to grow at a reasonable rate with the order of the graph G. If G is known to have bounded maximum degree, their results are particularly strong, their main theorem in this case being the following.

- Theorem 2.23. For any ∆ and any ﬁxed graph H, there exists c > 0 such that if G is a connected graph on n vertices with maximum degree ∆ and bandwidth at most cn then G is H-good.

Another result of this type, proved by Nikiforov and Rousseau [170], shows that graphs with small separators are s-good. Recall that the degeneracy d(G) of a graph G is the smallest natural number d such that every induced subgraph of G has a vertex of degree at most d. Furthermore, we say that a graph G has a (t,η)-separator if there exists a vertex subset T ⊆ V (G) such that |T| ≤ t and every connected component of V (G)\T has order at most η|V (G)|. The result of Nikiforov and Rousseau is now as follows.

- Theorem 2.24. For any s ≥ 3, d ≥ 1 and 0 < γ < 1, there exists η > 0 such that the class G of connected d-degenerate graphs G with a (|V (G)|1−γ,η)-separator is s-good.


Nikiforov and Rousseau used this result to resolve a number of outstanding questions of Burr and Erd˝os [31] regarding Ramsey goodness. For example, they showed that the 1-subdivision of Kn, the graph formed by adding an extra vertex to each edge of Kn, is s-good for n suﬃciently large. Moreover, using this result, it was shown in [50] that the family of connected planar graphs

is s-good for every s. This is a special case of a more general result. We say that a graph H is a minor of G if H can be obtained from a subgraph of G by contracting edges. By an H-minor of G, we mean a minor of G which is isomorphic to H. For a graph H, let GH be the family of connected graphs which do not contain an H-minor. Since the family of planar graphs consists precisely of those graphs which do not contain K5 or K3,3 as a minor, our claim about planar graphs is an immediate corollary of the following result. The proof is an easy corollary of Theorem 2.24, a result of Mader [158] which bounds the average degree of H-minor-free graphs and a separator theorem for H-minor-free graphs due to Alon, Seymour and Thomas [10].

- Theorem 2.25. For every ﬁxed graph H, the class GH of connected graphs G which do not contain an H-minor is s-good for every s ≥ 3.

One of the original problems of Burr and Erd˝os that was left open after the work of Nikiforov and Rousseau was to determine whether the family of hypercubes is s-good for every s. Recall that the hypercube Qn is the graph on vertex set {0,1}n where two vertices are connected by an edge if and only if they diﬀer in exactly one coordinate. Since Qn has 2n vertices, the problem asks whether r(Qn,Ks) = (s − 1)(2n − 1) + 1 for n suﬃciently large. The ﬁrst progress on this question was made by Conlon, Fox, Lee and Sudakov [50], who obtained an upper bound of the form cs2n, the main tool in the proof being a novel technique for embedding hypercubes. Using a variant of this embedding technique and a number of additional ingredients, the original question was subsequently resolved by Fiz Pontiveros, Griﬃths, Morris, Saxton and Skokan [105, 106].

- Theorem 2.26. The family of hypercubes is s-good for every s ≥ 3.


## 2.6 Ramsey multiplicity

For any ﬁxed graph H, Ramsey’s theorem tells us that when N is suﬃciently large, any twocolouring of the edges of KN contains a monochromatic copy of H. But how many monochromatic copies of H will this two-colouring contain? To be more precise, we let mH(G) be the number of copies of one graph H in another graph G and deﬁne

![image 56](<2015-conlon-recent-developments-graph-ramsey_images/imageFile56.png>)

mH(N) = min{mH(G) + mH(G) : |G| = N},

that is, mH(N) is the minimum number of monochromatic copies of H that occur in any twocolouring of KN. For the clique Kt, we simply write mt(N). We now deﬁne the Ramsey multiplicity constant4 to be

mH(N) mH(KN)

cH = lim

.

![image 57](<2015-conlon-recent-developments-graph-ramsey_images/imageFile57.png>)

N→∞

That is, we consider the minimum proportion of copies of H which are monochromatic, where the minimum is taken over all two-colourings of KN, and then take the limit as N tends to inﬁnity. Since one may show that the fractions mH(N)/mH(KN) are increasing in N and bounded above

![image 58](<2015-conlon-recent-developments-graph-ramsey_images/imageFile58.png>)

4We note that sometimes the term Ramsey multiplicity is used for the quantity mH(r(H)), that is, the minimum number of copies of H that must appear once one copy of H appears. For example, it is well known that every two-colouring of K6 contains not just one but at least two monochromatic copies of K3. In general, this quantity is rather intractable and we will not discuss it further.

by 1, this limit is well deﬁned. For cliques, we simply write ct := cKt = limN→∞ mt(N)/ Nt . We also write cH,q and ct,q for the analogous functions with q rather than two colours.

The earliest result on Ramsey multiplicity is the famous result of Goodman [124], which says that c3 ≥ 14. This result is sharp, as may be seen by considering a random two-colouring of the edges of KN. Erd˝os [80] conjectured that a similar phenomenon should hold for larger cliques, that is, that the Ramsey multiplicity should be asymptotically minimised by the graph GN,1/2. Quantitatively, this would imply that ct ≥ 21−(2t). This conjecture was later generalised by Burr and Rosta [34], who conjectured that cH ≥ 21−e(H) for all graphs H. Following standard practice, we will call a graph common if it satisﬁes the Burr–Rosta conjecture.

![image 59](<2015-conlon-recent-developments-graph-ramsey_images/imageFile59.png>)

The Burr–Rosta conjecture was disproved by Sidorenko [196], who showed that a triangle with a pendant edge is not common. Soon after, Thomason [211] disproved Erd˝os’ conjecture by showing that K4 is not common. Indeed, he showed that c4 < 331 , where Erd˝os’ conjecture would have implied that c4 ≥ 321 . More generally, Jagger, Sˇˇtovı´cˇek and Thomason [139] showed that any graph which contains K4 is not common. They also asked whether the conjecture holds for the 5-wheel, the graph formed by taking a cycle of length 5 and adding a central vertex connected to each of the vertices in the cycle. Determining whether this graph satisﬁes the Burr–Rosta conjecture was of particular interest because it is the smallest graph of chromatic number 4 which does not contain K4. Using ﬂag algebras [175], this question was answered positively by Hatami, Hladky´, Kra´l’, Norine and Razborov [136].

![image 60](<2015-conlon-recent-developments-graph-ramsey_images/imageFile60.png>)

![image 61](<2015-conlon-recent-developments-graph-ramsey_images/imageFile61.png>)

- Theorem 2.27. The 5-wheel is common.


Therefore, there exist 4-chromatic common graphs. The following question, whether there exist common graphs of any chromatic number, was stated explicitly in [136]. For example, is it the case that the graphs arising in Mycielski’s famous construction of triangle-free graphs with arbitrarily high chromatic number are common?

- Problem 2.28. Do there exist common graphs of all chromatic numbers?


For bipartite graphs (that is, graphs of chromatic number two), the question of whether the graph is common is closely related to a famous conjecture of Sidorenko [197] and Erd˝os– Simonovits [101]. This conjecture states that if H is a bipartite graph then the random graph with density p has in expectation asymptotically the minimum number of copies of H over all graphs of the same order and edge density. In particular, if this conjecture is true for a given bipartite graph H then so is the Burr–Rosta conjecture. Since Sidorenko’s conjecture is now known to hold for a number of large classes of graphs, we will not attempt an exhaustive summary here, instead referring the reader to some of the recent papers on the subject [56, 142, 155].

In general, the problem of estimating the constants cH seems to be diﬃcult. For complete graphs, the upper bound ct ≤ 21−(2t) has only ever been improved by small constant factors, while the best lower bound, due to Conlon [48], is ct ≥ C−(1+o(1))t2, where C ≈ 2.18 is an explicitly deﬁned constant. The argument that gives this bound may be seen as a multiplicity analogue of the usual Erd˝os–Szekeres argument that bounds Ramsey numbers. We accordingly expect that it will be diﬃcult to improve. For ﬁxed t, the ﬂag algebra method oﬀers some hope. For example, it

is now known [169, 201] that c4 > 351 . A more striking recent success of this method, by Cummings, Kra´l’, Pfender, Sperfeld, Treglown and Young [68], is an exact determination of c3,3 = 251 .

![image 62](<2015-conlon-recent-developments-graph-ramsey_images/imageFile62.png>)

![image 63](<2015-conlon-recent-developments-graph-ramsey_images/imageFile63.png>)

A strong quantitative counterexample to the Burr–Rosta conjecture was found by Fox [108]. Indeed, suppose that H is connected and split the vertex set of KN into χ(H) − 1 vertex sets, each of order χ(HN)−1, colouring the edges between any two sets blue and those within each set red. Since there are only χ(H) − 1 sets, there cannot be a blue copy of H. As every red copy of H must lie completely within one of the χ(H) − 1 vertex sets, a simple calculation then shows that cH ≤ (χ(H) − 1)1−v(H). Consider now the graph H consisting of a clique with t = √m vertices and an appended path with m − 2 t ≥ m2 edges. Since χ(H) = √m and v(H) ≥ m2 , we see that cH ≤ m−(1−o(1))m/4. Since e(H) = m, this gives a strong disproof of the conjecture that cH ≥ 21−m. However, the following conjecture [108] still remains plausible.

![image 64](<2015-conlon-recent-developments-graph-ramsey_images/imageFile64.png>)

![image 65](<2015-conlon-recent-developments-graph-ramsey_images/imageFile65.png>)

![image 66](<2015-conlon-recent-developments-graph-ramsey_images/imageFile66.png>)

![image 67](<2015-conlon-recent-developments-graph-ramsey_images/imageFile67.png>)

![image 68](<2015-conlon-recent-developments-graph-ramsey_images/imageFile68.png>)

- Conjecture 2.29. For any ǫ > 0, there exists m0 such that if H is a graph with at least m0 edges, then


cH ≥ 2−e(H)1+ǫ.

When q ≥ 3, the Ramsey multiplicity constants cH,q behave very diﬀerently. To see this, consider a two-colouring, in red and blue, of the complete graph on r(t)−1 vertices which contains no monochromatic copy of Kt. We now form a three-colouring of KN by blowing up each vertex in this two-colouring to have order r(tN)−1 and placing a green clique in each vertex set. This colouring contains no red or blue copies of Kt. Therefore, if H is the graph deﬁned above, that is, a clique with t = √m vertices and an appended path with m − 2 t ≥ m2 edges, it is easy to check that cH,3 ≤ (r(t)−1)1−v(H) ≤ 2−(1−o(1))m3/2/4, where we used that r(t) ≥ 2t/2. In particular,

![image 69](<2015-conlon-recent-developments-graph-ramsey_images/imageFile69.png>)

![image 70](<2015-conlon-recent-developments-graph-ramsey_images/imageFile70.png>)

![image 71](<2015-conlon-recent-developments-graph-ramsey_images/imageFile71.png>)

- Conjecture 2.29 is false for more than two colours. We hope to discuss this topic further in a forthcoming paper [62].


# 3 Variants

There are a huge number of interesting variants of the usual Ramsey function. In this section, we will consider only a few of these, focusing on those that we believe to be of the greatest importance.

## 3.1 Induced Ramsey numbers

A graph H is said to be an induced subgraph of H if V (H) ⊂ V (G) and two vertices of H are adjacent if and only if they are adjacent in G. The induced Ramsey number rind(H) is the smallest natural number N for which there is a graph G on N vertices such that every two-colouring of the edges of G contains an induced monochromatic copy of H. The existence of these numbers was proved independently by Deuber [70], Erd˝os, Hajnal and Po´sa [97] and Ro¨dl [176], though the bounds these proofs give on rind(H) are enormous. However, Erd˝os [81] conjectured the existence of a constant c such that every graph H with n vertices satisﬁes rind(H) ≤ 2cn. If true, this would clearly be best possible.

In a problem paper, Erd˝os [84] stated that he and Hajnal had proved a bound of the form rind(H) ≤ 22n

1+o(1)

. This remained the state of the art for some years until Kohayakawa, Pr¨omel

and Ro¨dl [144] proved that there is a constant c such that every graph H on n vertices satisﬁes rind(H) ≤ 2cnlog2 n. Using similar ideas to those used in the proof of Theorem 2.12, the authors [58] recently improved this bound, removing one of the logarithmic factors from the exponent.

- Theorem 3.1. There exists a constant c such that every graph H with n vertices satisﬁes rind(H) ≤ 2cnlogn.


The graph G used by Kohayakawa, Pr¨omel and Ro¨dl in their proof is a random graph constructed with projective planes. This graph is speciﬁcally designed so as to contain many copies of the target graph H. Subsequently, Fox and Sudakov [114] showed how to prove the same bounds

- as Kohayakawa, Pr¨omel and Ro¨dl using explicit pseudorandom graphs. The approach in [58] also uses pseudorandom graphs.


A graph is said to be pseudorandom if it imitates some of the properties of a random graph. One such property, introduced by Thomason [208, 209], is that of having approximately the same density between any pair of large disjoint vertex sets. More formally, we say that a graph G = (V,E) is (p,λ)-jumbled if, for all subsets A,B of V , the number of edges e(A,B) between A and B satisﬁes

![image 72](<2015-conlon-recent-developments-graph-ramsey_images/imageFile72.png>)

|e(A,B) − p|A||B|| ≤ λ |A||B|. The binomial random graph G(N,p), where each edge in an N-vertex graph is chosen independently with probability p, is itself a (p,λ)-jumbled graph with λ = O(√pN). An example of an explicit (21,√N)-jumbled graph is the Paley graph PN. This is the graph with vertex set ZN, where N is a prime which is congruent to 1 modulo 4 and two vertices x and y are adjacent if and only if x − y is a quadratic residue. For further examples, we refer the reader to [151]. We may now state the result that lies behind Theorem 3.1.

![image 73](<2015-conlon-recent-developments-graph-ramsey_images/imageFile73.png>)

![image 74](<2015-conlon-recent-developments-graph-ramsey_images/imageFile74.png>)

![image 75](<2015-conlon-recent-developments-graph-ramsey_images/imageFile75.png>)

- Theorem 3.2. There exists a constant c such that, for any n ∈ N and any (21,λ)-jumbled graph G on N vertices with λ ≤ 2−cnlognN, every graph on n vertices occurs as an induced monochromatic copy in all two-colourings of the edges of G. Moreover, all of these induced monochromatic copies can be found in the same colour. For graphs of bounded maximum degree, Trotter conjectured that the induced Ramsey number is at most polynomial in the number of vertices. That is, for each ∆ there should be d(∆) such that rind(H) ≤ nd(∆) for any n-vertex graph H with maximum degree ∆. This was proved by  Luczak and Ro¨dl [157], who gave an enormous upper bound for d(∆), namely, a tower of twos of height O(∆2). More recently, Fox and Sudakov [114] proved the much more reasonable bound d(∆) = O(∆log ∆). This was improved by Conlon, Fox and Zhao [63] as follows.
- Theorem 3.3. For every natural number ∆, there exists a constant c such that rind(H) ≤ cn2∆+8 for every n-vertex graph H of maximum degree ∆.


![image 76](<2015-conlon-recent-developments-graph-ramsey_images/imageFile76.png>)

Again, this is a special case of a much more general result. Like Theorem 3.2, it says that if a graph on N vertices is (p,λ)-jumbled for λ suﬃciently small in terms of p and N, then the graph has strong Ramsey properties.5

![image 77](<2015-conlon-recent-developments-graph-ramsey_images/imageFile77.png>)

5We note that this is itself a simple corollary of the main result in [63], which gives a counting lemma for subgraphs of sparse pseudorandom graphs and thereby a mechanism for transferring combinatorial theorems such as Ramsey’s theorem to the sparse context. For further details, we refer the interested reader to [63].

- Theorem 3.4. For every natural number ∆, there exists a constant c such that, for any n ∈ N


and any (n1,λ)-jumbled graph G on N vertices with λ ≤ cn−∆−29N, every graph on n vertices with maximum degree ∆ occurs as an induced monochromatic copy in all two-colourings of the edges of

![image 78](<2015-conlon-recent-developments-graph-ramsey_images/imageFile78.png>)

![image 79](<2015-conlon-recent-developments-graph-ramsey_images/imageFile79.png>)

- G. Moreover, all of these induced monochromatic copies can be found in the same colour.


In particular, this gives the stronger result that there are graphs G on cn2∆+8 vertices such that in every two-colouring of the edges of G there is a colour which contains induced monochromatic copies of every graph on n vertices with maximum degree ∆. The exponent of n in this result is best possible up to a multiplicative factor, since, even for the much weaker condition that G contains an induced copy of all graphs on n vertices with maximum degree ∆, G must contain Ω(n∆/2) vertices [35].

Theorems 3.3 and 3.4 easily extend to more than two colours. This is not the case for Theorems 3.1 and 3.2, where the following problem remains open. As usual, rind(H;q) denotes the q-colour analogue of the induced Ramsey number.

- Problem 3.5. Show that if H is a graph on n vertices and q ≥ 3 is a natural number, then rind(H;q) ≤ 2n1+o(1).


It also remains to decide whether Theorem 3.3 can be improved to show that the induced Ramsey number of every graph with n vertices and maximum degree ∆ is at most a polynomial in

- n whose exponent is independent of ∆.


- Problem 3.6. Does there exist a constant d such that rind(H) ≤ c(∆)nd for all graphs with n vertices and maximum degree ∆?


## 3.2 Folkman numbers

In the late sixties, Erd˝os and Hajnal [91] asked whether, for any positive integers t ≥ 3 and q ≥ 2, there exists a graph G which is Kt+1-free but such that any q-colouring of the edges of G contains a monochromatic copy of Kt. For two colours, this problem was solved in the aﬃrmative by Folkman [107]. However, his method did not generalise to more than two colours and it was several years before Nesˇetrˇil and Ro¨dl [166] found another proof which worked for any number of colours.

Once we know that these graphs exist, it is natural to try and estimate their size. To do this, we deﬁne the Folkman number f(t) to be the smallest natural number N for which there exists a Kt+1-free graph G on N vertices such that every two-colouring of the edges of G contains a monochromatic copy of Kt. The lower bound for f(t) is essentially the same as for the usual Ramsey function, that is, f(t) ≥ 2c′t. On the other hand, the proofs mentioned above (and some subsequent ones [167, 180]) use induction schemes which result in the required graphs G having enormous numbers of vertices.

Because of the diﬃculties involved in proving reasonable bounds for these numbers, a substantial amount of eﬀort has gone into understanding the bounds for f(3). In particular, Erd˝os asked for a proof that f(3) is smaller than 1010. This was subsequently given by Spencer [200], building on work of Frankl and Ro¨dl [119], but has since been improved further [73, 156]. The current best bound, due to Lange, Radziszowski and Xu [153], stands at f(3) ≤ 786.

The work of Frankl and Ro¨dl [119] and Spencer [200] relied upon analysing the Ramsey properties of random graphs. Recall that the binomial random graph Gn,p is a graph on n vertices where each of the n2 possible edges is chosen independently with probability p. Building on the work of Frankl and Ro¨dl, Ro¨dl and Rucin´ski [179, 180] determined the threshold for Ramsey’s theorem to hold in a binomial random graph and used it to give another proof of Folkman’s theorem. To state their theorem, let us say that a graph G is (H,q)-Ramsey if any q-colouring of the edges of

- G contains a monochromatic copy of H.


- Theorem 3.7. For any graph H that is not a forest consisting of stars and paths of length 3 and any positive integer q ≥ 2, there exist positive constants c and C such that

lim

n→∞

P[Gn,p is (H,q)-Ramsey] =

- 0 if p < cn−1/m2(H),
- 1 if p > Cn−1/m2(H),


where

m2(H) = max

e(H′) − 1 v(H′) − 2

![image 80](<2015-conlon-recent-developments-graph-ramsey_images/imageFile80.png>)

: H′ ⊆ H and v(H′) ≥ 3 .

Very recently, it was noted [65, 181] that some new methods for proving this theorem yield signiﬁcantly stronger bounds for Folkman numbers. As we have already remarked, the connection between these two topics is not a new one. However, in recent years, a number of very general methods have been developed for proving combinatorial theorems in random sets [13, 64, 121, 188, 189] and some of these methods return good quantitative estimates. In particular, the following result was proved by Ro¨dl, Rucin´ski and Schacht [181]. The proof relies heavily on the hypergraph container method of Balogh, Morris and Samotij [13] and Saxton and Thomason [188] and an observation of Nenadov and Steger [165] that allows one to apply this machinery to Ramsey problems.

- Theorem 3.8. There exists a constant c such that f(t) ≤ 2ct4 logt.


Their method also returns a comparable bound for the q-colour analogue f(t;q). Given how close these bounds now lie to the lower bound, we are willing to conjecture that, like the usual Ramsey number, the Folkman number is at most exponential in t.

- Conjecture 3.9. There exists a constant c such that f(t) ≤ 2ct.


## 3.3 The Erdo˝s–Hajnal conjecture

There are several results and conjectures saying that graphs which do not contain a ﬁxed induced subgraph are highly structured. The most famous conjecture of this type is due to Erd˝os and Hajnal [94] and asks whether any such graph must contain very large cliques or independent sets.6

![image 81](<2015-conlon-recent-developments-graph-ramsey_images/imageFile81.png>)

6Although their 1989 paper [94] is usually cited as the origin of this problem, the Erd˝s–Hajnal conjecture already appeared in a paper from 1977 [93].

- Conjecture 3.10. For every graph H, there exists a positive constant c(H) such that any graph on n vertices which does not contain an induced copy of H has a clique or an independent set of order at least nc(H).


This is in stark contrast with general graphs, since the probabilistic argument that gives the standard lower bound on Ramsey numbers shows that almost all graphs on n vertices contain no clique or independent set of order 2log n. Therefore, the Erd˝os–Hajnal conjecture may be seen as saying that the bound on Ramsey numbers can be improved from exponential to polynomial when one restricts to colourings that have a ﬁxed forbidden subcolouring.

The Erd˝os–Hajnal conjecture has been solved in some special cases. For example, the bounds for oﬀ-diagonal Ramsey numbers imply that it holds when H is itself a clique or an independent set. Moreover, Alon, Pach and Solymosi [8] observed that if the conjecture is true for two graphs

- H1 and H2, then it also holds for the graph H formed by blowing up a vertex of H1 and replacing it with a copy of H2. These results easily allow one to prove that the conjecture holds for all graphs on at most four vertices with the exception of P4, the path with 3 edges. However, this case follows from noting that any graph which contains no induced P4 is perfect. The conjecture remains open for a number of graphs on ﬁve vertices, including the cycle C5 and the path P5. However, Chudnovsky and Safra [39] recently proved the conjecture for the graph on ﬁve vertices known as the bull, consisting of a triangle with two pendant edges. We refer the reader to the survey by Chudnovsky [38] for further information on this and related results.


The best general bound, due to Erd˝os and Hajnal [94], is as follows. Theorem 3.11. For every graph H, there exists a positive constant c(H) such that any graph on

- n vertices which does not contain an induced copy of H has a clique or an independent set of order √logn.


![image 82](<2015-conlon-recent-developments-graph-ramsey_images/imageFile82.png>)

- at least ec(H)


Despite much attention, this bound has not been improved. However, an oﬀ-diagonal generalisation was proved by Fox and Sudakov [116] using dependent random choice. This says that for any graph

- H there exists a positive constant c(H) such that for every induced-H-free graph G on n vertices and any positive integers n1 and n2 satisfying (log n1)(log n2) ≤ c(H)log n, G contains either a clique of order n1 or an independent set of order n2.


Another result of this type, due to Promel and Ro¨dl [172], states that for each C there is c > 0 such that every graph on n vertices contains every graph on at most clog n vertices as an induced subgraph or has a clique or independent set of order at least C log n. That is, every graph contains all small graphs as induced subgraphs or has an unusually large clique or independent set. Fox and Sudakov [114] proved a result which implies both the Erd˝os–Hajnal result and the Promel–Ro¨dl result. It states that there are absolute constants c,c′ > 0 such that for all positive integers n and k every graph on n vertices contains every graph on at most k vertices as an induced subgraph or has a clique or independent set of order c2c

![image 83](<2015-conlon-recent-developments-graph-ramsey_images/imageFile83.png>)

′ log n

k log n. When k is constant, this gives the Erd˝os–Hajnal bound and when k is a small multiple of log n, we obtain the Promel–Ro¨dl result.

![image 84](<2015-conlon-recent-developments-graph-ramsey_images/imageFile84.png>)

It is also interesting to see what happens if one forbids not just one but many graphs as induced subgraphs. A family F of graphs is hereditary if it is closed under taking induced subgraphs. We say that it is proper if it does not contain all graphs. A family F of graphs has the Erdo˝s–Hajnal

property if there is c = c(F) > 0 such that every graph G ∈ F has a clique or an independent set of order |G|c. The Erd˝os–Hajnal conjecture is easily seen to be equivalent to the statement that every proper hereditary family of graphs has the Erd˝os–Hajnal property.

A family F of graphs has the strong Erdo˝s–Hajnal property if there is c′ = c′(F) > 0 such that for every graph G ∈ F on at least two vertices, G or its complement G¯ contains a complete bipartite subgraph with parts of order c′|G|. A simple induction argument (see [110]) shows that if a hereditary family of graphs has the strong Erd˝os–Hajnal property, then it also has the Erd˝os– Hajnal property. However, not every proper hereditary family of graphs has the strong Erd˝os– Hajnal property. For example, it is easy to see that the family of triangle-free graphs does not have the strong Erd˝os–Hajnal property. Even so, the strong Erd˝os–Hajnal property has been a useful way to deduce the Erd˝os–Hajnal property for some families of graphs. A good example is the recent result of Bousquet, Lagoutte and Thomasse´ [25] which states that for each positive integer t the family of graphs that excludes both the path Pt on t vertices and its complement as induced subgraphs has the strong Erd˝os–Hajnal property (using diﬀerent techniques, Chudnovsky and Seymour [40] had earlier proved that this family has the Erd˝os–Hajnal property when t = 6). Bonamy, Bousquet and Thomasse´ [24] later extended the result of [25], proving that for each t ≥ 3 the family of graphs that excludes all cycles on at least t vertices and their complements as induced subgraphs has the strong Erd˝os–Hajnal property.

This approach also applies quite well in combinatorial geometry, where a common problem is to show that arrangements of geometric objects have large crossing or disjoint patterns. This is usually proved by showing that the auxiliary intersection graph, with a vertex for each object and an edge between two vertices if the corresponding objects intersect, has a large clique or independent set. Larman, Matousˇek, Pach and To¨ro˝csik [154] proved that the family of intersection graphs of convex sets in the plane has the Erd˝os–Hajnal property. This was later strengthened by Fox, Pach and To´th [113], who proved that this family has the strong Erd˝os–Hajnal property. Alon, Pach, Pinchasi, Radoicˇic´ and Sharir [7] proved that the family of semi-algebraic graphs of bounded description complexity has the strong Erd˝os–Hajnal property. This implies the existence of large patterns in many graphs that arise naturally in discrete geometry.

String graphs are intersection graphs of curves in the plane. It is still an open problem to decide whether every family of n curves in the plane contains a subfamily of size nc whose elements are either pairwise intersecting or pairwise disjoint, i.e., whether the family S of string graphs has the Erd˝os–Hajnal property. The best known bound is nc/log logn, due to Fox and Pach [111]. This follows by ﬁrst proving that every string graph on n ≥ 2 vertices contains a complete or empty bipartite subgraph with parts of order Ω(n/log n). This latter result is tight up to the constant factor, so the family of string graphs does not have the strong Erd˝os–Hajnal property. On the other hand, Fox, Pach and To´th [113] proved that the family Sk of intersection graphs of curves where each pair of curves intersects at most k times does have the strong Erd˝os–Hajnal property.

We have already noted that the strong Erd˝os–Hajnal property does not always hold for inducedH-free graphs. However, Erd˝os, Hajnal and Pach [96] proved that a bipartite analogue of the Erd˝os-Hajnal conjecture does hold. That is, for every graph H there is a positive constant c(H) such that every induced-H-free graph on n ≥ 2 vertices contains a complete or empty bipartite graph with parts of order nc(H). Using dependent random choice, Fox and Sudakov [116] proved

a strengthening of this result, showing that every such graph contains a complete bipartite graph with parts of order nc(H) or an independent set of order nc(H).

In a slightly diﬀerent direction, Ro¨dl [177] showed that any graph with a forbidden induced subgraph contains a linear-sized subset which is close to being complete or empty. That is, for every graph H and every ǫ > 0, there is δ > 0 such that every induced-H-free graph on n vertices contains an induced subgraph on at least δn vertices with edge density at most ǫ or at least 1 − ǫ. Ro¨dl’s proof uses Szemere´di’s regularity lemma and consequently gives a tower-type bound on δ−1. Fox and Sudakov [114] proved the much better bound δ ≥ 2−c|H|(log 1/ǫ)2, which easily implies Theorem 3.11 as a corollary. They also conjectured that a polynomial dependency holds, which would in turn imply the Erd˝os–Hajnal conjecture.

Conjecture 3.12. For every graph H, there is a positive constant c(H) such that for every ǫ > 0 every induced-H-free graph on n vertices contains an induced subgraph on ǫc(H)n vertices with density at most ǫ or at least 1 − ǫ.

One of the key steps in proving Theorem 3.11 is to ﬁnd, in an induced-H-free graph on n vertices, two disjoint subsets of order at least ǫcn for some c = c(H) > 0 such that the edge density between them is at most ǫ or at least 1 − ǫ. We wonder whether this can be improved so that one part is of linear size.

- Problem 3.13. Is it true that for every graph H there is c = c(H) > 0 such that for every ǫ > 0 every induced-H-free graph on n vertices contains two disjoint subsets of orders cn and ǫcn such that the edge density between them is at most ǫ or at least 1 − ǫ?


A positive answer to this question would improve the bound on the Erd˝os–Hajnal conjecture to ec

√lognlog logn. However, we do not even know the answer when H is a triangle. A positive answer in this case would imply the following conjecture.

![image 85](<2015-conlon-recent-developments-graph-ramsey_images/imageFile85.png>)

- Conjecture 3.14. There is a positive constant c such that every triangle-free graph on n ≥ 2 vertices contains disjoint subsets of orders cn and nc with no edges between them.

Restated, this conjecture says that there exists a positive constant c such that the Ramsey number of a triangle versus a complete bipartite graph with parts of orders cn and nc is at most n.

There is also a multicolour generalisation of the Erd˝os–Hajnal conjecture.

- Conjecture 3.15. For every q-edge-coloured complete graph K, there exists a positive constant c(K) such that every q-edge-colouring of the complete graph on n vertices which does not contain a copy of K has an induced subgraph on nc(K) vertices which uses at most q − 1 colours.


The Erd˝os–Hajnal conjecture clearly corresponds to the case q = 2, as we can take the edges of our graph as one colour and the non-edges as the other colour. For q = 3, Fox, Grinshpun and Pach [109] proved that every rainbow-triangle-free 3-edge-colouring of the complete graph on n vertices contains a two-coloured subset with at least cn1/3 log2 n vertices. This bound is tight up to the constant factor and answers a question of Hajnal [134], the construction that demonstrates tightness being the lexicographic product of three two-colourings of the complete graph on n1/3 vertices, one for each pair of colours and each having no monochromatic clique of order log n.

Alon, Pach and Solymosi [8] observed that the Erd˝os–Hajnal conjecture is equivalent to the following variant for tournaments. For every tournament T, there is a positive constant c(T) such that every tournament on n vertices which does not contain T as a subtournament has a transitive subtournament of order nc(T). Recently, Berger, Choromanski and Chudnovsky [19] proved that this conjecture holds for every tournament T on at most ﬁve vertices, as well as for an inﬁnite family of tournaments that cannot be obtained through the tournament analogue of the substitution procedure of Alon, Pach and Solymosi.

Analogues of the Erd˝os–Hajnal conjecture have also been studied for hypergraphs. The authors [59] proved that for k ≥ 4 no analogue of the standard Erd˝os–Hajnal conjecture can hold in k-uniform hypergraphs. That is, there are k-uniform hypergraphs H and sequences of induced-Hfree hypergraphs which do not contain cliques or independent sets of order appreciably larger than is guaranteed by Ramsey’s theorem. The proof uses the fact that the stepping-up construction of Erd˝os and Hajnal has forbidden induced subgraphs.

Nevertheless, one can still show that 3-uniform hypergraphs with forbidden induced subgraphs contain some unusually large conﬁgurations. It is well known that every 3-uniform hypergraph on n vertices contains a complete or empty tripartite subgraph with parts of order c(log n)1/2 and a random 3-uniform hypergraph shows that this bound is tight up to the constant factor. Ro¨dl and Schacht [182] proved that this bound can be improved by any constant factor for suﬃciently large induced-H-free hypergraphs. This result was subsequently improved by the authors [59], who showed that for every 3-uniform hypergraph H there exists a positive constant δ(H) such that, for

- n suﬃciently large, every induced-H-free 3-uniform hypergraph on n vertices contains a complete or empty tripartite subgraph with parts of order (log n)1/2+δ(H). We believe that this bound can be improved further. If true, the following conjecture would be best possible.


- Conjecture 3.16. For every 3-uniform hypergraph H, any induced-H-free hypergraph on n vertices contains a complete or empty tripartite subgraph with parts of order (log n)1−o(1).


## 3.4 Size Ramsey numbers

Given a graph H, the size Ramsey number rˆ(H) is deﬁned to be the smallest m for which there exists a graph G with m edges such that G is Ramsey with respect to H, that is, such that any two-colouring of the edges of G contains a monochromatic copy of H. This concept was introduced by Erd˝os, Faudree, Rousseau and Schelp [88]. Since the complete graph on r(H) vertices is Ramsey with respect to H, it is clear that rˆ(H) ≤ r(2H) . Moreover, as observed by Chv´atal (see [88]), this inequality is tight when H is a complete graph. This follows easily from noting that any graph which is Ramsey with respect to Kt must have chromatic number at least r(t).

The most famous result in this area is the following rather surprising theorem of Beck [16], which says that the size Ramsey number of a path is linear in the number of vertices. Here Pn is the path with n vertices.

- Theorem 3.17. There exists a constant c such that rˆ(Pn) ≤ cn.


This result, which answered a question of Erd˝os, Faudree, Rousseau and Schelp [88] (see also [83]), was later extended to trees of bounded maximum degree [122] and to cycles [137]. For a

more general result on the size Ramsey number of trees, we refer the reader to the recent work of Dellamonica [69].

Beck [17] raised the question of whether this result could be generalised to graphs of bounded maximum degree. That is, he asked whether for any ∆ there exists a constant c, depending only on ∆, such that any graph on n vertices with maximum degree ∆ has size Ramsey number at most cn. This question was answered in the negative by Ro¨dl and Szemere´di [184], who proved that there are already graphs of maximum degree 3 with superlinear size Ramsey number.

- Theorem 3.18. There are positive constants c and α and, for every n, a graph H with n vertices and maximum degree 3 such that

rˆ(H) ≥ cn(log n)α.

On the other hand, a result of Kohayakawa, Ro¨dl, Schacht and Szemere´di [145] shows that the size Ramsey number of graphs with bounded maximum degree is subquadratic.

- Theorem 3.19. For every natural number ∆, there exists a constant c∆ such that any graph H on n vertices with maximum degree ∆ satisﬁes


rˆ(H) ≤ c∆n2−1/∆(log n)1/∆.

We are not sure where the truth lies, though it seems likely that Theorem 3.18 can be improved by a polynomial factor. This was formally conjectured by Ro¨dl and Szemere´di [184].

Conjecture 3.20. For every natural number ∆ ≥ 3, there exists a constant ǫ > 0 such that for all suﬃciently large n there is a graph H on n vertices with maximum degree ∆ for which rˆ(H) ≥ n1+ǫ.

More generally, given a real-valued graph parameter f, we may deﬁne the f-Ramsey number rf(H) of H to be the minimum value of f(G), taken over all graphs G which are Ramsey with respect to H. The usual Ramsey number is the case where f(G) = v(G), while the size Ramsey number is the case where f(G) = e(G). However, there have also been studies of other variants, such as the chromatic Ramsey number rχ(H), where f(G) = χ(G), and the degree Ramsey number r∆(H), where f(G) = ∆(G). We will point out one result concerning the ﬁrst parameter and a problem concerning the second.

The chromatic Ramsey number was introduced by Burr, Erd˝os and Lov´asz [33], who observed that any graph H with chromatic number t has rχ(H) ≥ (t − 1)2 + 1 and conjectured that there are graphs of chromatic number t for which this bound is sharp. In their paper, they outlined a proof of this conjecture based on the still unproven Hedetniemi conjecture, which concerns the chromatic number of the tensor product of graphs. Recently, Zhu [214] proved a fractional version of the Hedetniemi conjecture, which, by an observation of Paul and Tardif [171], was suﬃcient to establish the conjecture.

Theorem 3.21. For every natural number t, there exists a graph H of chromatic number t such that

rχ(H) = (t − 1)2 + 1.

The outstanding open problem concerning the degree Ramsey number is the following, which seems to have been ﬁrst noted by Kinnersley, Milans and West [143].

Problem 3.22. Is it true that for every ∆ ≥ 3, there exists a natural number ∆′ such that r∆(H) ≤ ∆′ for every graph H of maximum degree ∆?

We suspect that the answer is no, but the problem appears to be diﬃcult. For ∆ = 2, the answer is yes (see, for example, [138]).

An on-line variant of the size Ramsey number was introduced by Beck [18] and, independently, by Kurek and Rucin´ski [152]. It is best described as a game between two players, known as Builder and Painter. Builder draws a sequence of edges and, as each edge appears, Painter must colour it in either red or blue. Builder’s goal is to force Painter to draw a monochromatic copy of some ﬁxed graph H. The smallest number of turns needed by Builder to force Painter to draw a monochromatic copy of H is known as the on-line Ramsey number of H and denoted r˜(H). As usual, we write r˜(t) for r˜(Kt).

The basic question in this area, attributed to Ro¨dl (see [152]), is to show that limt→∞ r˜(t)/rˆ(t) =

- 0. Put diﬀerently, we would like to show that r˜(t) = o( r(2t) ). This conjecture remains open (and is probably diﬃcult), but the following result, due to Conlon [47], shows that the on-line Ramsey number r˜(t) is exponentially smaller than the size Ramsey number rˆ(t) for inﬁnitely many values of t.


- Theorem 3.23. There exists a constant c > 1 such that for inﬁnitely many t,


r˜(t) ≤ c−t

r(t) 2

.

On-line analogues of f-Ramsey numbers were considered by Grytczuk, Ha uszczak and Kierstead [132]. The most impressive result in this direction, proved by Grytczuk, Ha uszczak, Kierstead and Konjevod over two papers [132, 140], says that Builder may force Painter to draw a monochromatic copy of any graph with chromatic number t while only exposing a graph of chromatic number t herself. We also note that the on-line analogue of Problem 3.22 was studied in [36] but again seems likely to have a negative answer for ∆ ≥ 3 (though we refer the interested reader to [61] for a positive answer to the analogous question when maximum degree is replaced by degeneracy).

## 3.5 Generalised Ramsey numbers

In this section, we will consider two generalisations of the usual Ramsey function, both of which have been referred to in the literature as generalised Ramsey numbers.

- 3.5.1 The Erd˝s–Gya´rfa´s function


Let p and q be positive integers with 2 ≤ q ≤ p2 . An edge colouring of the complete graph Kn is said to be a (p,q)-colouring if every Kp receives at least q diﬀerent colours. The function f(n,p,q) is deﬁned to be the minimum number of colours that are needed for Kn to have a (p,q)-colouring. This function generalises the usual Ramsey function, as may be seen by noting that f(n,p,2) is the minimum number of colours needed to guarantee that no Kp is monochromatic. In particular, if we invert the bounds 2s ≤ r(3;s) ≤ es!, we get

log n log log n ≤ f(n,3,2) ≤ clog n.

c′

![image 86](<2015-conlon-recent-developments-graph-ramsey_images/imageFile86.png>)

This function was ﬁrst introduced by Erd˝os and Shelah [81, 82] and studied in depth by Erd˝os and Gy´arf´as [90], who proved a number of interesting results, demonstrating how the function falls

- oﬀ from being equal to n2 when q = p2 and p ≥ 4 to being at most logarithmic when q = 2. They also determined ranges of p and q where the function f(n,p,q) is linear in n, where it is


quadratic in n and where it is asymptotically equal to n2 . Many of these results were subsequently strengthened by Sa´rk¨ozy and Selkow [186, 187].

One simple observation of Erd˝os and Gy´arf´as is that f(n,p,p) is always polynomial in n. To see this, it is suﬃcient to show that a colouring with fewer than n1/(p−2) − 1 colours contains a Kp with at most p − 1 colours. For p = 3, this follows since one only needs that some vertex has at least two neighbours in the same colour. For p = 4, we have that any vertex will have at least n1/2 neighbours in some ﬁxed colour. But then there are fewer than n1/2 − 1 colours on this neighbourhood of order at least n1/2, so the p = 3 case implies that it contains a triangle with at most two colours. The general case follows similarly.

Erd˝os and Gy´arf´as [90] asked whether this result is best possible, that is, whether q = p is the smallest value of q for which f(n,p,q) is polynomial in n. For p = 3, this is certainly true, since we know that f(n,3,2) ≤ clog n. However, for general p, they were only able to show that f(n,p,⌈log p⌉) is subpolynomial. This left the question of determining whether f(n,p,p − 1) is subpolynomial wide open, even for p = 4.

The ﬁrst progress on this question was made by Mubayi [162], who found a (4,3)-colouring of Kn with only ec

√logn colours, thus showing that f(n,4,3) ≤ ec

√logn. Later, Eichhorn and Mubayi [77] showed that this colouring is also a (5,4)-colouring and, more generally, a (p,2⌈log p⌉−2)-colouring for all p ≥ 5. It will be instructive to describe this colouring (or rather a slight variant).

![image 87](<2015-conlon-recent-developments-graph-ramsey_images/imageFile87.png>)

![image 88](<2015-conlon-recent-developments-graph-ramsey_images/imageFile88.png>)

Given n, let t be the smallest integer such that n ≤ 2t2 and m = 2t. We consider the vertex set [n] as a subset of [m]t. For two vertices x = (x1,... ,xt) and y = (y1,... ,yt), let

cM(x,y) = {xi,yi},a1,... ,at ,

where i is the minimum index in which x and y diﬀer and aj = 0 or 1 depending on whether xj = yj or not. Since 2(t−1)2 < n, the total number of colours used is at most

√logn) ≤ 26

√logn.

![image 89](<2015-conlon-recent-developments-graph-ramsey_images/imageFile89.png>)

![image 90](<2015-conlon-recent-developments-graph-ramsey_images/imageFile90.png>)

m2 · 2t = 23t < 23(1+

√logn colours to colour the edge set of the complete graph Kn. The proof that cM is a (4,3)-colouring is a straightforward case analysis which we leave as an exercise. We have already noted that it is also a (5,4)-colouring. However, as observed in [51], it cannot be a (p,p − 1)-colouring for all p.

![image 91](<2015-conlon-recent-developments-graph-ramsey_images/imageFile91.png>)

Hence, cM uses at most 26

Nevertheless, in a recent paper, Conlon, Fox, Lee and Sudakov [51] found a way to extend this construction and answer the question of Erd˝os and Gy´arf´as for all p. Stated in a quantitative form (though one which we expect to be very far from best possible), this result is as follows.

- Theorem 3.24. For any natural number p ≥ 4, there exists a constant cp such that f(n,p,p − 1) ≤ 2cp(logn)1−1/(p−2).


Our quantitative understanding of these functions is poor, even for f(n,4,3). Improving a result of Kostochka and Mubayi [146], Fox and Sudakov [115] showed that f(n,4,3) ≥ c′ log n for some positive constant c′. Though a substantial improvement on the trivial bound f(n,4,3) ≥ f(n,4,2) ≥ c′ log n/log log n, it still remains very far from the upper bound of ec

√logn. We suspect that the upper bound may be closer to the truth. An answer to the following question would be a small step in the right direction.

![image 92](<2015-conlon-recent-developments-graph-ramsey_images/imageFile92.png>)

Problem 3.25. Show that f(n,4,3) = ω(log n).

For p ≥ k + 1 and 2 ≤ q ≤ k p , we deﬁne the natural hypergraph generalisation fk(n,p,q) as the minimum number of colours that are needed for Kn(k) to have a (p,q)-colouring, where here a (p,q)-colouring means that every Kp(k) receives at least q distinct colours. As in the graph case, it is comparatively straightforward to show that fk(n,p, k p−−11 + 1) is polynomial in n for all p ≥ k + 1. With Lee [52], we conjecture the following.

- Conjecture 3.26. fk(n,p, k p−−11 ) is subpolynomial for all p ≥ k + 1.


Theorem 3.24 addresses the k = 2 case, while the cases where k = 3 and p = 4 and 5 were addressed in [52]. These cases already require additional ideas beyond those used to resolve the graph case. The case where k = 3 and p = 4 is of particular interest, because it is closely related to Shelah’s famous primitive recursive bound for the Hales–Jewett theorem [192].

Shelah’s proof relied in a crucial way on a lemma now known as the Shelah cube lemma. The simplest case of this lemma concerns the grid graph Γm,n, the graph on vertex set [m] × [n] where two distinct vertices (i,j) and (i′,j′) are adjacent if and only if either i = i′ or j = j′. That is, Γm,n is the Cartesian product Km × Kn. A rectangle in Γm,n is a copy of K2 × K2, that is, an induced subgraph over a vertex subset of the form {(i,j),(i′,j),(i,j′),(i′,j′)} for some integers

- 1 ≤ i < i′ ≤ m and 1 ≤ j < j′ ≤ n. We will denote this rectangle by (i,j,i′,j′). For an edgecoloured grid graph, an alternating rectangle is a rectangle (i,j,i′,j′) such that the colour of the edges {(i,j),(i′,j)} and {(i,j′),(i′,j′)} are equal and the colour of the edges {(i,j),(i,j′)} and {(i′,j),(i′,j′)} are equal, that is, opposite sides of the rectangle receive the same colour. The basic case of Shelah’s lemma, which we refer to as the grid Ramsey problem, asks for an estimate on G(r), the smallest n such that every r-colouring of the edges of Γn,n contains an alternating rectangle.


It is easy to show that G(r) ≤ r(r+12 ) + 1. Indeed, let n = r(r+12 ) + 1 and suppose that an rcolouring of Γr+1,n is given. Since each column is a copy of Kr+1, there are at most r(r+12 ) ways to colour the edges of a ﬁxed column with r colours. Since n > r(r+12 ), the pigeonhole principle implies that there are two columns which are identically coloured. Let these columns be the j-th column and the j′-th column and consider the edges that connect these two columns. Since there are r + 1 rows, the pigeonhole principle implies that there are i and i′ such that the edges {(i,j),(i,j′)} and {(i′,j),(i′,j′)} have the same colour. Since the edges {(i,j),(i′,j)} and {(i,j′),(i′,j′)} also have the same colour, the rectangle (i,j,i′,j′) is alternating.

This argument is very asymmetrical and yet the resulting bound on G(r) remains essentially the best known. The only improvement, due to Gy´arf´as [133], is G(r) ≤ r(r+12 ) − r(r−1

2 )+1 + 1. Though it seems likely that G(r) is signiﬁcantly smaller than this, the following problem already appears to be diﬃcult.

Problem 3.27. Show that G(r) = o(r(r+12 )).

In the second edition of their book on Ramsey theory [130], Graham, Rothschild and Spencer suggested that G(r) may even be polynomial in r. This was recently disproved by Conlon, Fox, Lee and Sudakov [52], who showed the following.

Theorem 3.28. There exists a positive constant c such that G(r) > 2c(logr)5/2/

√log logr.

![image 93](<2015-conlon-recent-developments-graph-ramsey_images/imageFile93.png>)

To see how this relates back to estimating f3(n,4,3), we let g(n) be the inverse function of G(r), deﬁned as the minimum integer s for which there exists an s-colouring of the edges of Γn,n with no alternating rectangle. Letting K(3)(n,n) be the 3-uniform hypergraph with vertex set A∪B, where |A| = |B| = n, and edge set consisting of all those triples which intersect both A and B, we claim that g(n) is within a factor of two of the minimum integer r for which there exists an r-colouring of the edges of K(3)(n,n) such that any copy of K4(3) has at least three colours on its edges.

To prove this claim, we deﬁne a bijection between the edges of Γn,n and the edges of K(3)(n,n)

such that the rectangles of Γn,n are in one-to-one correspondence with the copies of K4(3) in K(3)(n,n). For i ∈ A and j,j′ ∈ B, we map the edge (i,j,j′) of K(3)(n,n) to the edge {(i,j),(i,j′)}

of Γn,n and, for i,i′ ∈ A and j ∈ B, we map the edge (i,i′,j) of K(3)(n,n) to the edge {(i,j),(i′,j)} of Γn,n. Given a colouring of K(3)(n,n) where every K4(3) receives at least three colours, this correspondence gives a colouring of Γn,n where every rectangle receives at least three colours, showing that g(n) ≤ r. Similarly, given a colouring of Γn,n with no alternating rectangles, we may double the number of colours to ensure that the set of colours used for row edges is disjoint from the set used for column edges. This gives a colouring where every K4(3) receives at least three colours, so r ≤ 2g(n).

Therefore, essentially the only diﬀerence between g(n) and f3(2n,4,3) is that the base hypergraph for g(n) is K(3)(n,n) rather than K2(3)n . This observation allows us to show that

g(n) ≤ f3(2n,4,3) ≤ 2⌈log n⌉2g(n). In particular, this allows us to establish a subpolynomial upper bound for f3(n,4,3). More generally, Shelah’s work on the Hales–Jewett theorem requires an estimate for the function

f2d−1(n,2d,d+1). If the growth rate of these functions was bounded below by, say, c′d log log log n, then it might be possible to give a tower-type bound for Hales–Jewett numbers. However, we expect that this is not the case.

- Problem 3.29. Show that for all s, there exist d and n0 such that


f2d−1 (n,2d,d + 1) ≤ log log ... log log

n

![image 94](<2015-conlon-recent-developments-graph-ramsey_images/imageFile94.png>)

![image 95](<2015-conlon-recent-developments-graph-ramsey_images/imageFile95.png>)

s

for all n ≥ n0.

We conclude this section with one further problem which arose in studying f(n,p,q) and its generalisations. Mubayi’s colouring cM was originally designed to have the property that the union

of any two colour classes contains no K4. However, in [52], it was shown to have the stronger property that the union of any two colour classes has chromatic number at most three. We suspect that this property can be generalised.

- Problem 3.30. Let p ≥ 5 be an integer. Does there exist an edge colouring of Kn with no(1) colours such that the union of every p − 1 colour classes has chromatic number at most p?


For p = 4, Mubayi’s colouring again has the desired property, though it is known that it cannot work for all p. However, it may be that the colourings used in the proof of Theorem 3.24 suﬃce.

- 3.5.2 The Erd˝s–Rogers function


Given an integer s ≥ 2, a set of vertices U in a graph G is said to be s-independent if G[U] contains

- no copy of Ks. When s = 2, this simply means that U is an independent set in G. We write αs(G) for the order of the largest s-independent subset in a graph G.


The problem of estimating Ramsey numbers can be rephrased as a problem about determining the minimum independence number over all Kt-free graphs with a given number of vertices. In 1962, Erd˝os and Rogers [100] initiated the study of the more general question obtained by replacing the notion of independence number with the s-independence number. Suppose 2 ≤ s ≤ t < n are integers. Erd˝os and Rogers deﬁned

fs,t(n) = min αs(G),

where the minimum is taken over all Kt-free graphs G on n vertices. In particular, for s = 2, we have f2,t(n) < ℓ if and only if the Ramsey number r(ℓ,t) satisﬁes r(ℓ,t) > n.

The ﬁrst lower bound for fs,t was given by Bollob´s and Hind [23], who proved that fs,t(n) ≥ n1/(t−s+1). Their proof is by induction on t. When t = s, the bound holds trivially, since the graph contains no Ks. Now suppose that G is an n-vertex graph with no Kt and let v be a vertex of maximum degree. If |N(v)| ≥ n

t−s

t−s+1, then we can apply induction to the subgraph of G induced by this set, since this subgraph is clearly Kt−1-free. Otherwise, by Brooks’ theorem, the independence number of G is at least n/|N(v)| ≥ n1/(t−s+1). The bound in this argument can be improved by a polylogarithmic factor using a result of Shearer [191] on the independence number of Kt-free graphs. As was pointed out by Bollob´s and Hind [23], this proof usually ﬁnds an independent set rather than an s-independent set. Another approach, which better utilises the fact that we are looking for an s-independent set, was proposed by Sudakov [203].

![image 96](<2015-conlon-recent-developments-graph-ramsey_images/imageFile96.png>)

To illustrate this approach, we show that f3,5(n) ≥ cn2/5 for some constant c > 0, improving on the bound of n1/3 given above. Let G be a K5-free graph on n vertices and assume that it does not contain a 3-independent subset of order n2/5. For every edge (u,v) of G, the set of common neighbours N(u,v) is triangle-free. Therefore, we may assume that it has order less than n2/5. Moreover, for any vertex v, its set of neighbours N(v) is K4-free. But, by the Bollob´s–Hind bound, N(v) contains a triangle-free subset of order |N(v)|1/2. Therefore, if there is a vertex v of degree at least n4/5, there will be a triangle-free subset of order |N(v)|1/2 ≥ n2/5. Hence, we may assume that all degrees in G are less than n4/5. This implies that every vertex in G is contained in at most n4/5 · n2/5 = n6/5 triangles.

We now consider the auxiliary 3-uniform hypergraph H on the same vertex set as G whose edges are the triangles in G. Crucially, an independent set in H is a 3-independent set in G. The number m of edges in H satisﬁes m ≤ n·n6/5 = n11/5. Therefore, using a well-known bound on the independence number of 3-uniform hypergraphs, we conclude that α3(G) = α(H) ≥ cn3/2/√m ≥ cn2/5. This bound can be further improved by combining the above argument with a variant of dependent random choice. Using this approach, Sudakov [204] showed that f3,5(n) is at least n5/12 times a polylogarithmic factor. For t > s + 1, he also proved that fs,t(n) = Ω(nat), where at(s) is roughly s/2t + Os(t−2). More precisely, he showed the following.

![image 97](<2015-conlon-recent-developments-graph-ramsey_images/imageFile97.png>)

- Theorem 3.31. For any s ≥ 3 and t > s + 1, fs,t(n) = Ω(nat), where 1

![image 98](<2015-conlon-recent-developments-graph-ramsey_images/imageFile98.png>)

at

= 1 +

1 s − 1

![image 99](<2015-conlon-recent-developments-graph-ramsey_images/imageFile99.png>)

s−1

i=1

1 at−i

![image 100](<2015-conlon-recent-developments-graph-ramsey_images/imageFile100.png>)

, as+1 =

3s − 4 5s − 6

![image 101](<2015-conlon-recent-developments-graph-ramsey_images/imageFile101.png>)

and a3 = ··· = as = 1.

The study of upper bounds for fs,t(n) goes back to the original paper of Erd˝os and Rogers [100]. They considered the case where s and t = s+1 are ﬁxed and n tends to inﬁnity, proving that there exists a positive constant ǫ(s) such that fs,s+1(n) ≤ n1−ǫ(s). That is, they found a Ks+1-free graph of order n such that every induced subgraph of order n1−ǫ(s) contains a copy of Ks. About thirty years later, Bollob´s and Hind [23] improved the estimate for ǫ(s). This bound was then improved again by Krivelevich [150], who showed that

fs,t(n) ≤ cn

- s

![image 102](<2015-conlon-recent-developments-graph-ramsey_images/imageFile102.png>)

- t+1(log n)


1

![image 103](<2015-conlon-recent-developments-graph-ramsey_images/imageFile103.png>)

s−1,

where c is some constant depending only on s and t. Note that this upper bound is roughly the square of the lower bound from [204]. We also note that all of the constructions mentioned above rely on applications of the probabilistic method, but explicit constructions showing that fs,s+1(n) ≤ n1−ǫ(s) were obtained by Alon and Krivelevich [4].

One of the most intriguing problems in this area concerned the case where t = s + 1. For many years, the best bounds for this question were very far apart, the lower bound being roughly n1/2 and the upper bound being n1−ǫ(s), with ǫ(s) tending to zero as s tends to inﬁnity. Both Krivelevich [150] and Sudakov [204] asked whether the upper bound is closer to the correct order of magnitude for fs,s+1(n). Quite surprisingly, this was recently disproved in a sequence of three papers. First, Dudek and Ro¨dl [74] proved that fs,s+1(n) = O(n2/3). Then Wolfovitz [213], building on their work but adding further ideas, managed to show that the lower bound for f3,4(n) is correct up to logarithmic factors. Finally, Dudek, Retter and Ro¨dl [72], extending the approach from [213], proved that fs,s+1(n) = n1/2+o(1). More explicitly, they proved the following.

- Theorem 3.32. For every s ≥ 3, there exists a constant cs such that fs,s+1(n) ≤ cs(log n)4s2√n.


![image 104](<2015-conlon-recent-developments-graph-ramsey_images/imageFile104.png>)

It would be interesting to close the gap between this and the best lower bound, observed by Dudek and Mubayi [71], which stands at

fs,s+1(n) ≥ c′s

nlog n log log n

![image 105](<2015-conlon-recent-developments-graph-ramsey_images/imageFile105.png>)

1/2

.

We will now sketch the neat construction from [74] showing that f3,4(n) = O(n2/3). Let p be a prime, n = p3 + p2 + p + 1 and let L1,... ,Ln be the lines of a generalised quadrangle. The reader not familiar with this concept may consult [123]. For our purposes, it will be suﬃcient to note that this is a collection of points and lines with the following two properties:

- • every line is a subset of [n] of order p + 1 and every vertex in [n] lies on p + 1 lines;
- • any two vertices belong to at most one line and every three lines with non-empty pairwise intersection have one point in common (i.e., every triangle of lines is degenerate).


We construct a random graph G on [n] as follows. Partition the vertex set of every line Li into three parts Li,j,1 ≤ j ≤ 3, uniformly at random. Take a complete 3-partite graph on these parts and let G be the union of all such graphs for 1 ≤ i ≤ n. Note that the second property above implies that the vertices of every triangle in G belong to some line. This easily implies that G is K4-free. Consider now an arbitrary subset X of G of order 6p2 and let xi = |Li ∩ X|. If X contains no triangles, then, for every i, there is an index j such that the set Li,j ∩ X is empty. The probability that this happens for a ﬁxed i is at most 3(2/3)xi. Therefore, since these events are independent for diﬀerent lines, the probability that X is triangle-free is at most 3n(2/3) xi. Since every vertex lies on p + 1 lines, we have that xi = (p + 1)|X| > 5n. Since the number of subsets X is at most

- 2n and 2n3n(2/3)5n ≪ 1, we conclude that with probability close to one every subset of G of order at least 10n2/3 > 6p2 contains a triangle.


There are many open problems remaining regarding the Erd˝os–Rogers function. For example, it follows from the work of Sudakov [204] and Dudek, Retter and Ro¨dl [72] that for any ǫ > 0 there exists s0 such that if s ≥ s0, then

c′n1/2−ǫ ≤ fs,s+2(n) ≤ cn1/2

for some positive constants c′ and c. It remains to decide if the upper bound can be improved for ﬁxed values of s. The following question was posed by Dudek, Retter and Ro¨dl [72].

Problem 3.33. For any s ≥ 3, is it true that fs,s+2(n) = o(√n)?

![image 106](<2015-conlon-recent-developments-graph-ramsey_images/imageFile106.png>)

The hypergraph generalisation of the Erd˝os–Rogers function was ﬁrst studied by Dudek and Mubayi [71]. For s ≤ t, let fs,t(k)(n) be given by

fs,t(k)(n) = min{max{|W| : W ⊆ V (G) and G[W] contains no Ks(k)}},

where the minimum is taken over all Kt(k)-free k-uniform hypergraphs G on n vertices. Dudek and Mubayi proved the following.

- Theorem 3.34. For any s ≥ 3 and t ≥ s + 1, fs−1,t−1(⌊ log n⌋) ≤ fs,t(3)(n) ≤ cs log n.


![image 107](<2015-conlon-recent-developments-graph-ramsey_images/imageFile107.png>)

In particular, for t = s + 1, this gives constants c1 and c2 depending only on s such that

c1(log n)1/4

log log n log log log n

![image 108](<2015-conlon-recent-developments-graph-ramsey_images/imageFile108.png>)

1/2

≤ fs,s(3)+1(n) ≤ c2 log n.

The lower bound was subsequently improved by the authors [61], using ideas on hypergraph Ramsey numbers developed in [55].

- Theorem 3.35. For any natural number s ≥ 3, there exists a positive constant c such that


1/3

log n log log log n

fs,s(3)+1(n) ≥ c

.

![image 109](<2015-conlon-recent-developments-graph-ramsey_images/imageFile109.png>)

This result easily extends to higher uniformities to give fs,s(k)+1(n) ≥ (log(k−2) n)1/3−o(1), where log(0) x = x and log(i+1) x = log(log(i) x). This improves an analogous result of Dudek and Mubayi [71] with a 1/4 in the exponent but remains far from their upper bound fs,s(k)+1(n) ≤ cs,k(log n)1/(k−2). It would be interesting to close the gap between the upper and lower bounds. In particular, we have the following problem.

Problem 3.36. Is it the case that

fs,s(4)+1(n) = (log n)o(1)?

## 3.6 Monochromatic cliques with additional structure

There are a number of variants of the classical Ramsey question which ask for further structure on the monochromatic cliques being found. The classic example of such a theorem is the Paris– Harrington theorem [135], which says that any for any t, k and q, there exists an N such that any q-colouring of the edges of the complete k-uniform hypergraph on the set {1,2,... ,N} contains a monochromatic Ks(k) with vertices a1 < ··· < as for which s ≥ max{t,a1}. That is, the clique is at least as large as its minimal element. This theorem, which follows easily from a compactness argument, is famous for being a natural statement which is not provable in Peano arithmetic (though we note that for graphs and two colours, the function is quite well behaved and grows as a double exponential in t [160]). In this section, we will discuss two decidedly less pathological strengthenings of Ramsey’s theorem.

3.6.1 Weighted cliques

In the early 1980s, Erd˝os considered the following variant of Ramsey’s theorem. For a ﬁnite set S of integers greater than one, deﬁne its weight w(S) by

1 log s

w(S) =

,

![image 110](<2015-conlon-recent-developments-graph-ramsey_images/imageFile110.png>)

s∈S

where, as usual, log is assumed to be base 2. For a red/blue-colouring c of the edges of the complete graph on [2,n] = {2,... ,n}, let f(c) be the maximum weight w(S) taken over all sets S ⊂ [2,n] which form a monochromatic clique in the colouring c. For each integer n ≥ 2, let f(n) be the minimum of f(c) over all red/blue-colourings c of the edges of the complete graph on {2,... ,n}.

Erd˝os [83] conjectured that f(n) tends to inﬁnity, choosing this particular weight function because the standard bound r(t) ≤ 22t only allows one to show that f(n) ≥ log2n · log1n = 12. Erd˝os’

![image 111](<2015-conlon-recent-developments-graph-ramsey_images/imageFile111.png>)

![image 112](<2015-conlon-recent-developments-graph-ramsey_images/imageFile112.png>)

![image 113](<2015-conlon-recent-developments-graph-ramsey_images/imageFile113.png>)

conjecture was veriﬁed by Ro¨dl [178], who proved that there exist positive constants c and c′ such that

log log log log n log log log log log n ≤ f(n) ≤ clog log log n.

c′

![image 114](<2015-conlon-recent-developments-graph-ramsey_images/imageFile114.png>)

To prove Ro¨dl’s upper bound, we cover the interval [2,n] by s = ⌊log log n⌋ + 1 intervals, where the ith interval is [22i−1,22i). Using the bound r(t) ≥ 2t/2, we can colour the edges of the complete graph on the ith interval so that the maximum monochromatic clique in this interval has order 2i+1. Since the log of any element in this interval is at least 2i−1, the maximum weight of any monochromatic clique is at most 4. If we again use the lower bound on r(t), we see that there is a red/blue-colouring of the edges of the complete graph on vertex set {1,2,... ,s} whose largest monochromatic clique is of order O(log s). Colour the edges of the complete bipartite graph between the ith and jth interval by the colour of edge (i,j) in this colouring. We get a red/bluecolouring of the edges of the complete graph on [2,n] such that any monochromatic clique in this colouring has a non-empty intersection with at most O(log s) intervals. Since every interval can contribute at most 4 to the weight of this clique, the total weight of any monochromatic clique is O(log s) = O(log log log n).

Answering a further question of Erd˝os, the authors [60] showed that this upper bound is tight up to a constant factor. The key idea behind the proof is to try to force the type of situation that arises in the upper bound construction. In practice, this means that we split our graph into intervals I1,... ,Is of the form [22i−1,22i) and, for each i = 1,... ,s, we ﬁnd a subset Ii′ ⊂ Ii such that Ii′ is the union of a red and a blue clique and all edges between Ii′ and Ij′ are monochromatic for each 1 ≤ i < j ≤ s. In broad outline, this was also the method used by Ro¨dl to prove his lower bound but our proof uses two additional ingredients, dependent random choice and a certain weighted version of Ramsey’s theorem.

- Theorem 3.37. For n suﬃciently large, every two-colouring of the edges of the complete graph on the interval {2,... ,n} contains a monochromatic clique with vertex set S such that


1 log s ≥ 2−8 log log log n.

![image 115](<2015-conlon-recent-developments-graph-ramsey_images/imageFile115.png>)

s∈S

Hence, f(n) = Θ(log log log n).

It also makes sense to consider the function fq(n), deﬁned now as the minimum over all qcolourings of the edges of the complete graph on {2,3,... ,n} of the maximum weight of a monochromatic clique. However, as observed by Ro¨dl, the analogue of Erd˝os’ conjecture for three colours does not hold. To see this, we again cover the interval [2,n] by s = ⌊log log n⌋ + 1 intervals of the form [22i−1,22i). The edges inside these intervals are coloured red and blue as in the previous construction, while the edges between the intervals are coloured green. But then the maximum weight of any red or blue clique is at most 4 and the maximum weight of any green clique is at most i≥1 2−i+1 = 2.

We may also ask whether there are other weight functions for which an analogue of Ro¨dl’s result holds. If w(i) is a weight function deﬁned on all positive integers n ≥ a, we let f(n,w) be the minimum over all red/blue-colourings of the edges of the complete graph on [a,n] of the

maximum weight of a monochromatic clique. In particular, if w1(i) = 1/log i and a = 2, then f(n,w1) = f(n).

The next interesting case is when w2(i) = 1/log ilog log log i, since, for any function u(i) which tends to inﬁnity with i, Theorem 3.37 implies that f(n,u′) → ∞, where u′(i) = u(i)/log ilog log log i. To derive a lower bound for f(n,w2), we colour the interval Ii = [22i−1,22i) so that the largest clique has order at most 2i+1. Then the contribution of the ith interval will be O(1/log i). If we now treat Ii as though it were a vertex of weight 1/log i, we may blow up Ro¨dl’s colouring and colour monochromatically between the Ii so that the weight of any monochromatic clique is O(log log log s) = O(log log log log log n). This bound is also sharp [60], that is, f(n,w2) = Θ(log log log log log n).

More generally, we have the following theorem, which determines the boundary below which f(n,·) converges. Here log(i)(x) is again the iterated logarithm given by log(0) x = x and log(i+1) x = log(log(i) x).

- Theorem 3.38. Let ws(i) = 1/ sj=1 log(2j−1) i. Then f(n,ws) = Θ(log(2s+1) n). However, if ws′ (i) = ws(i)/(log(2s−1) i)ǫ for any ﬁxed ǫ > 0, f(n,ws′ ) converges.

3.6.2 Cliques of ﬁxed order type

Motivated by an application in model theory, V¨a¨na¨nen [168] asked whether, for any positive integers t and q and any permutation π of [t − 1] = {1,2,... ,t − 1}, there is a positive integer R such that every q-colouring of the edges of the complete graph on vertex set [R] contains a monochromatic Kt with vertices a1 < ··· < at satisfying

aπ(1)+1 − aπ(1) > aπ(2)+1 − aπ(2) > ··· > aπ(t−1)+1 − aπ(t−1).

That is, we want the set of diﬀerences {ai+1 − ai : 1 ≤ i ≤ t − 1} to have a prescribed order. The least such positive integer R is denoted by Rπ(t;q) and we let R(t;q) = maxπ Rπ(t;q), where the maximum is over all permutations π of [t − 1].

V¨a¨na¨nen’s question was answered positively by Alon [168] and, independently, by Erd˝os, Hajnal and Pach [95]. Alon’s proof uses the Gallai–Witt theorem and so gives a weak bound on R(t;q), whereas the proof of Erd˝os, Hajnal and Pach uses a compactness argument and gives no bound at all. Later, Alon, Shelah and Stacey all found proofs giving tower-type bounds for R(t;q), but these were never published, since a double-exponential upper bound R(t;q) ≤ 2(q(t+1)3)qt was then found by Shelah [193].

A natural conjecture, made by Alon (see [193]), is that for any q there exists a constant cq such that R(t;q) ≤ 2cqt. For the trivial permutation, this was conﬁrmed by Alon and Spencer. For a general permutation, the best known bound, due to the authors [60], is as follows. Once again, dependent random choice plays a key role in the proof.

- Theorem 3.39. For any positive integers t and q and any permutation π of [t−1], every q-colouring of the edges of the complete graph on vertex set [R] with R = 2t20q contains a monochromatic Kt with vertices a1 < ··· < at satisfying


aπ(1)+1 − aπ(1) > aπ(2)+1 − aπ(2) > ··· > aπ(t−1)+1 − aπ(t−1).

That is, R(t;q) ≤ 2t20q.

There are several variants of V¨a¨na¨nen’s question which have negative answers. For example, the natural hypergraph analogue fails. To see this, we colour an edge (a1,a2,a3) with a1 < a2 < a3 red if a3 − a2 ≥ a2 − a1 and blue otherwise. Hence, if the subgraph with vertices a1 < ··· < at is monochromatic, the sequence a2 − a1,... ,at − at−1 must be monotone increasing or decreasing, depending on whether the subgraph is coloured red or blue.

## 3.7 Ordered Ramsey numbers

An ordered graph on n vertices is a graph whose vertices have been labelled with the vertex set [n] = {1,2,... ,n}. We say that an ordered graph G on vertex set [N] contains another ordered graph H on vertex set [n] if there exists a map φ : [n] → [N] such that φ(i) < φ(j) for all i < j and (φ(i),φ(j)) is an edge of G whenever (i,j) is an edge of H. Given an ordered graph H, we deﬁne the ordered Ramsey number r<(H) to be the smallest N such that every two-colouring of the complete graph on vertex set [N] contains a monochromatic ordered copy of H.

As a ﬁrst observation, we note the elementary inequalities,

r(H) ≤ r<(H) ≤ r(Kv(H)).

In particular, r<(Kt) = r(Kt). However, for sparse graphs, the ordered Ramsey number may diﬀer substantially from the usual Ramsey number. This was ﬁrst observed by Conlon, Fox, Lee and Sudakov [53] and by Balko, Cibulka, Kra´l and Kyncˇl [12], who proved the following result.

- Theorem 3.40. There exists a positive constant c such that, for every even n, there exists an ordered matching M on n vertices for which

r<(M) ≥ nclogn/log logn.

In [53], it was proved that this lower bound holds for almost all orderings of a matching. This diﬀers considerably from the usual Ramsey number, where it is trivial to show that r(M) is linear in the number of vertices. It is also close to best possible, since, for all matchings M, r<(M) ≤ n⌈logn⌉.

For general graphs, it was proved in [53] that the ordered Ramsey number cannot be too much larger than the usual Ramsey number. Recall, from Section 2.3, that a graph is d-degenerate if there is an ordering of the vertices, say v1,v2,... ,vn, such that every vertex vi has at most d neighbours vj preceding it in the ordering, that is, such that j < i. We stress that in the following theorems the degenerate ordering need not agree with the given ordering.

- Theorem 3.41. There exists a constant c such that for any ordered graph H on n vertices with degeneracy d,


r<(H) ≤ r(H)cγ(H), where γ(H) = min{log2(2n/d),dlog(2n/d)}.

An important role in ordered Ramsey theory is played by the concept of interval chromatic number. The interval chromatic number χ<(H) of an ordered graph H is deﬁned to be the minimum

number of intervals into which the vertex set of H may be partitioned so that each interval forms an independent set in the graph. This is similar to the usual chromatic number but with arbitrary vertex sets replaced by intervals. For an ordered graph H with bounded degeneracy and bounded interval chromatic number, the ordered Ramsey number is at most polynomial in the number of vertices. This is the content of the following theorem from [53] (we note that a weaker version was also proved in [12]).

- Theorem 3.42. There exists a constant c such that any ordered graph H on n vertices with degeneracy at most d and interval chromatic number at most χ satisﬁes

r<(H) ≤ ncdlogχ.

If H is an ordered graph with vertices {1,2,... ,n}, we deﬁne the bandwidth of H to be the smallest ℓ such that |i − j| ≤ ℓ for all edges ij ∈ E(H). Answering a question of Lee and the authors [53], Balko, Cibulka, Kra´l and Kyncˇl [12] showed that the ordered Ramsey number of ordered graphs with bounded bandwidth is at most polynomial in the number of vertices.

- Theorem 3.43. For any positive integer ℓ, there exists a constant cℓ such that any ordered graph on n vertices with bandwidth at most ℓ satisﬁes


r<(H) ≤ ncℓ.

In [12], it is shown that for n suﬃciently large in terms of ℓ one may take cℓ = O(ℓ). It is plausible that the correct value of cℓ is signiﬁcantly smaller than this.

A large number of questions about ordered Ramsey numbers remain open. Here we will discuss just one such problem, referring the reader to [53] for a more complete discussion. As usual, we deﬁne r<(G,H) to be the smallest N such that any red/blue-colouring of the edges of the complete graph on [N] contains a red ordered copy of G or a blue ordered copy of H. Given an ordered matching M on n vertices, it is easy to see that

r<(K3,M) ≤ r(3,n) = O

n2 log n

![image 116](<2015-conlon-recent-developments-graph-ramsey_images/imageFile116.png>)

.

In the other direction, it is known [53] that there exists a positive constant c such that, for all even n, there exists an ordered matching M on n vertices for which r<(K3,M) ≥ c(lognn)4/3. It remains to determine which bound is closer to the truth. In particular, we have the following problem.

![image 117](<2015-conlon-recent-developments-graph-ramsey_images/imageFile117.png>)

Problem 3.44. Does there exist an ǫ > 0 such that for any matching M on n vertices r(K3,M) = O(n2−ǫ)?

Finally, we note that for hypergraphs the diﬀerence between Ramsey numbers and their ordered counterparts is even more pronounced. If we write Pn(k) for the monotone k-uniform tight path on {1,2,... ,n}, where {i,i + 1,... ,i + k − 1} is an edge for 1 ≤ i ≤ n − k + 1, then results of Fox, Pach, Sudakov and Suk [112] and Moshkovitz and Shapira [161] (see also [159]) show that for k ≥ 3 the ordered Ramsey number r<(Pn(k)) grows as a (k − 2)-fold exponential in n. This is in stark contrast with the unordered problem, where r(Pn(k)) is known to grow linearly in n for all k.

# 4 Concluding remarks

Given the length of this survey, it is perhaps unnecessary to add any further remarks. However, we would like to highlight two further problems which we believe to be of signal importance but which did not ﬁt neatly in any of the sections above.

The ﬁrst problem we wish to mention, proposed by Erd˝os, Fajtlowicz and Staton [41, 86], asks for an estimate on the order of the largest regular induced subgraph in a graph on n vertices. Ramsey’s theorem tells us that any graph on n vertices contains a clique or an independent set of order at least 12 log n. Since cliques and independent sets are both regular, this shows that there is always a regular induced subgraph of order at least 12 log n. The infamous conjecture of Erd˝os, Fajtlowicz and Staton, which we now state, asks whether this simple bound can be improved.

![image 118](<2015-conlon-recent-developments-graph-ramsey_images/imageFile118.png>)

![image 119](<2015-conlon-recent-developments-graph-ramsey_images/imageFile119.png>)

- Conjecture 4.1. Any graph on n vertices contains a regular induced subgraph with ω(log n) vertices.


By using an inhomogeneous random graph, Bollob´s showed that for any ǫ > 0 and n suﬃciently large depending on ǫ there are graphs on n vertices for which the largest regular induced subgraph has order at most n1/2+ǫ. This result was sharpened slightly by Alon, Krivelevich and Sudakov [6], who showed that there is a constant c and graphs on n vertices with no regular induced subgraph of order at least cn1/2 log1/4 n. Any polynomial improvement on this upper bound would be of considerable interest.

The second problem is that of constructing explicit Ramsey graphs. Erd˝os’ famous probabilistic lower bound argument, discussed at length in Section 2.1, shows that almost all colourings of the complete graph on √2t vertices do not contain a monochromatic copy of Kt. While this proves that the Ramsey number r(t) is greater than √2t, it does not give any constructive procedure for producing a colouring which exhibits this fact.

![image 120](<2015-conlon-recent-developments-graph-ramsey_images/imageFile120.png>)

![image 121](<2015-conlon-recent-developments-graph-ramsey_images/imageFile121.png>)

For many years, the best explicit example of a Ramsey graph was the following remarkable construction due to Frankl and Wilson [120]. Let p be a prime and let r = p2 − 1. Let G be the graph whose vertices are all subsets of order r from the set [m] = {1,2,... ,m} and where two vertices are adjacent if and only if their corresponding sets have intersection of size congruent to −1 (mod p). This is a graph with mr vertices and may be shown to contain no clique or independent set of order larger than p m−1 . Taking m = p3 and t = p p−31 , this gives a graph on tclogt/log logt vertices with no clique or independent set of order t.

Recently, Barak, Rao, Shaltiel and Wigderson [14] found a construction which improves on the Frankl–Wilson bound, giving graphs on

1+ǫ

22(loglogt)

vertices with no clique or independent set of order t, where ǫ > 0 is a ﬁxed constant. Unfortunately, their construction does not have any simple description. Instead, it is constructive in the sense that given the labels of any two vertices in the graph, it is possible to decide whether they are connected in polynomial time. It would be very interesting to know whether the same bound, or any signiﬁcant improvement over the Frankl–Wilson bound, could be achieved by graphs with a simpler description. It still seems that we are a long way from resolving Erd˝os’ problem [41] of

constructing explicit graphs exhibiting r(t) > (1 + ǫ)t, but for those who do not believe that hard work is its own reward, Erd˝os has oﬀered the princely sum of $100 as an enticement.

Acknowledgements. The authors would like to thank the anonymous referee for a number of useful comments.

# References

- [1] M. Ajtai, J. Komlo´s, and E. Szemere´di, A note on Ramsey numbers, J. Combin. Theory Ser. A 29 (1980), 354–360.
- [2] P. Allen, G. Brightwell and J. Skokan, Ramsey-goodness – and otherwise, Combinatorica 33

(2013), 125–160.

- [3] N. Alon, J. Balogh, A. Kostochka and W. Samotij, Sizes of induced subgraphs of Ramsey graphs, Combin. Probab. Comput. 18 (2009), 459–476.
- [4] N. Alon and M. Krivelevich, Constructive bounds for a Ramsey-type problem, Graphs Combin. 13 (1997), 217–225.
- [5] N. Alon, M. Krivelevich and B. Sudakov, Tura´n numbers of bipartite graphs and related Ramsey-type questions, Combin. Probab. Comput. 12 (2003), 477–494.
- [6] N. Alon, M. Krivelevich and B. Sudakov, Large nearly regular induced subgraphs, SIAM J. Discrete Math. 22 (2008), 1325–1337.
- [7] N. Alon, J. Pach, R. Pinchasi, R. Radoicˇic´ and M. Sharir, Crossing patterns of semi-algebraic sets, J. Combin. Theory Ser. A 111 (2005), 310–326.
- [8] N. Alon, J. Pach and J. Solymosi, Ramsey-type theorems with forbidden subgraphs, Combinatorica 21 (2001), 155–170.
- [9] N. Alon and V. Ro¨dl, Sharp bounds for some multicolor Ramsey numbers, Combinatorica 25

(2005), 125–141.

- [10] N. Alon, P. Seymour and R. Thomas, A separator theorem for nonplanar graphs, J. Amer. Math. Soc. 3 (1990), 801–808.
- [11] N. Alon and J. H. Spencer, The Probabilistic Method, 3rd edition, Wiley, 2007.
- [12] M. Balko, J. Cibulka, K. Kra´l and J. Kyncˇl, Ramsey numbers of ordered graphs, preprint.
- [13] J. Balogh, R. Morris and W. Samotij, Independent sets in hypergraphs, to appear in J. Amer. Math. Soc.
- [14] B. Barak, A. Rao, R. Shaltiel and A. Wigderson, 2-source dispersers for no(1) entropy, and Ramsey graphs beating the Frankl–Wilson construction, Ann. of Math. 176 (2012), 1483–1543.


- [15] J. Beck, An upper bound for diagonal Ramsey numbers, Studia Sci. Math. Hungar. 18 (1983), 401–406.
- [16] J. Beck, On size Ramsey number of paths, trees and cycles I, J. Graph Theory 7 (1983), 115–130.
- [17] J. Beck, On size Ramsey number of paths, trees and cycles II, in Mathematics of Ramsey theory, Algorithms Combin., Vol. 5, 34–45, Springer, Berlin, 1990.
- [18] J. Beck, Achievement games and the probabilistic method, in Combinatorics, Paul Erd˝os is Eighty, Vol. 1, 51–78, Bolyai Soc. Math. Stud., Ja´nos Bolyai Math. Soc., Budapest, 1993.
- [19] E. Berger, K. Choromanski and M. Chudnovsky, Forcing large transitive subtournaments, to appear in J. Combin. Theory Ser. B.
- [20] T. Bohman, The triangle-free process, Adv. Math. 221 (2009), 1653–1677.
- [21] T. Bohman and P. Keevash, The early evolution of the H-free process, Invent. Math. 181

(2010), 291–336.

- [22] T. Bohman and P. Keevash, Dynamic concentration of the triangle-free process, preprint.
- [23] B. Bollob´s and H. R. Hind, Graphs without large triangle free subgraphs, Discrete Math. 87

(1991), 119–131.

- [24] M. Bonamy, N. Bousquet and S. Thomasse´, The Erd˝os–Hajnal conjecture for long holes and anti-holes, preprint.
- [25] N. Bousquet, A. Lagoutte and S. Thomasse´, The Erd˝os–Hajnal conjecture for paths and antipaths, to appear in J. Combin. Theory Ser. B.
- [26] S. Brandt, Expanding graphs and Ramsey numbers, available at Freie Universita¨t, Berlin preprint server, ftp://ftp.math.fu-berlin.de/pub/math/publ/pre/1996/pr-a-96-24.ps.
- [27] B. Bukh and B. Sudakov, Induced subgraphs of Ramsey graphs with many distinct degrees, J. Combin. Theory Ser. B 97 (2007), 612–619.
- [28] S. A. Burr, Ramsey numbers involving graphs with long suspended paths, J. London Math. Soc. 24 (1981), 405–413.
- [29] S. A. Burr, What can we hope to accomplish in generalized Ramsey theory?, Discrete Math. 67 (1987), 215–225.
- [30] S. A. Burr and P. Erd˝os, On the magnitude of generalized Ramsey numbers for graphs, in Inﬁnite and Finite Sets, Vol. 1 (Keszthely, 1973), 214–240, Colloq. Math. Soc. Ja´nos Bolyai, Vol. 10, North-Holland, Amsterdam, 1975.
- [31] S. A. Burr and P. Erd˝os, Generalizations of a Ramsey-theoretic result of Chv´atal, J. Graph Theory 7 (1983), 39–51.


- [32] S. A. Burr, P. Erd˝os, R. J. Faudree, C. C. Rousseau and R. H. Schelp, Some complete bipartite graph-tree Ramsey numbers, Ann. Discrete Math. 41 (1989), 79–90.
- [33] S. A. Burr, P. Erd˝os and L. Lov´asz, On graphs of Ramsey type, Ars Combin. 1 (1976), 167–190.
- [34] S. A. Burr and V. Rosta, On the Ramsey multiplicity of graphs – problems and recent results, J. Graph Theory 4 (1980), 347–361.
- [35] S. Butler, Induced-universal graphs for graphs with bounded maximum degree, Graphs Combin. 25 (2009), 461–468.
- [36] J. Butterﬁeld, T. Grauman, W. B. Kinnersley, K. G. Milans, C. Stocker and D. B. West, On-line Ramsey theory for bounded degree graphs, Electron. J. Combin. 18 (2011), P136.
- [37] G. Chen and R. H. Schelp, Graphs with linearly bounded Ramsey numbers, J. Combin. Theory Ser. B 57 (1993), 138–149.
- [38] M. Chudnovsky, The Erd˝os–Hajnal conjecture – a survey, J. Graph Theory 75 (2014), 178–190.
- [39] M. Chudnovsky and S. Safra, The Erd˝os–Hajnal conjecture for bull-free graphs, J. Combin. Theory Ser. B 98 (2008), 1301–1310.
- [40] M. Chudnovsky and P. Seymour, Excluding paths and antipaths, to appear in Combinatorica.
- [41] F. Chung and R. L. Graham, Erd˝s on Graphs. His Legacy of Unsolved Problems, A K Peters, Ltd., Wellesley, MA, 1998.
- [42] V. Chv´atal, Tree-complete graph Ramsey numbers, J. Graph Theory 1 (1977), 93.
- [43] V. Chv´atal and F. Harary, Generalized Ramsey theory for graphs. III. Small oﬀ-diagonal numbers, Paciﬁc J. Math. 41 (1972), 335–345.
- [44] V. Chv´atal, V. Ro¨dl, E. Szemere´di and W. T. Trotter Jr, The Ramsey number of a graph with bounded maximum degree, J. Combin. Theory Ser. B 34 (1983), 239–243.
- [45] D. Conlon, A new upper bound for diagonal Ramsey numbers, Ann. of Math. 170 (2009), 941–960.
- [46] D. Conlon, Hypergraph packing and sparse bipartite Ramsey numbers, Combin. Probab. Comput. 18 (2009), 913–923.
- [47] D. Conlon, On-line Ramsey numbers, SIAM J. Discrete Math. 23 (2009), 1954–1963.
- [48] D. Conlon, On the Ramsey multiplicity of complete graphs, Combinatorica 32 (2012), 171–186.
- [49] D. Conlon, The Ramsey number of dense graphs, Bull. Lond. Math. Soc. 45 (2013), 483–496.
- [50] D. Conlon, J. Fox, C. Lee and B. Sudakov, Ramsey numbers of cubes versus cliques, to appear in Combinatorica.


- [51] D. Conlon, J. Fox, C. Lee and B. Sudakov, The Erd˝os–Gy´rf´as problem on generalized Ramsey numbers, Proc. Lond. Math. Soc. 110 (2015), 1–18.
- [52] D. Conlon, J. Fox, C. Lee and B. Sudakov, On the grid Ramsey problem and related questions, to appear in Int. Math. Res. Not.
- [53] D. Conlon, J. Fox, C. Lee and B. Sudakov, Ordered Ramsey numbers, submitted.
- [54] D. Conlon, J. Fox and B. Sudakov, Ramsey numbers of sparse hypergraphs, Random Structures Algorithms 35 (2009), 1–14.
- [55] D. Conlon, J. Fox and B. Sudakov, Hypergraph Ramsey numbers, J. Amer. Math. Soc. 23

(2010), 247–266.

- [56] D. Conlon, J. Fox and B. Sudakov, An approximate version of Sidorenko’s conjecture, Geom. Funct. Anal. 20 (2010), 1354–1366.
- [57] D. Conlon, J. Fox and B. Sudakov, Large almost monochromatic subsets in hypergraphs, Israel J. Math. 181 (2011), 423–432.
- [58] D. Conlon, J. Fox and B. Sudakov, On two problems in graph Ramsey theory, Combinatorica 32 (2012), 513–535.
- [59] D. Conlon, J. Fox and B. Sudakov, Erd˝os–Hajnal-type theorems in hypergraphs, J. Combin. Theory Ser. B 102 (2012), 1142–1154.
- [60] D. Conlon, J. Fox and B. Sudakov, Two extensions of Ramsey’s theorem, Duke Math. J. 162

(2013), 2903–2927.

- [61] D. Conlon, J. Fox and B. Sudakov, Short proofs of some extremal results, Combin. Probab. Comput. 23 (2014), 8–28.
- [62] D. Conlon, J. Fox and B. Sudakov, Short proofs of some extremal results II, in preparation.
- [63] D. Conlon, J. Fox and Y. Zhao, Extremal results in sparse pseudorandom graphs, Adv. Math. 256 (2014), 206–290.
- [64] D. Conlon and W. T. Gowers, Combinatorial theorems in sparse random sets, submitted.
- [65] D. Conlon and W. T. Gowers, An upper bound for Folkman numbers, preprint.
- [66] O. Cooley, N. Fountoulakis, D. Ku¨hn and D. Osthus, 3-uniform hypergraphs of bounded degree have linear Ramsey numbers, J. Combin. Theory Ser. B 98 (2008), 484–505.
- [67] O. Cooley, N. Fountoulakis, D. Ku¨hn and D. Osthus, Embeddings and Ramsey numbers of sparse k-uniform hypergraphs, Combinatorica 28 (2009), 263–297.
- [68] J. Cummings, D. Kra´l’, F. Pfender, K. Sperfeld, A. Treglown and M. Young, Monochromatic triangles in three-coloured graphs, J. Combin. Theory Ser. B 103 (2013), 489–503.


- [69] D. Dellamonica, The size-Ramsey number of trees, Random Structures Algorithms 40 (2012), 49–73.
- [70] W. Deuber, A generalization of Ramsey’s theorem, in Inﬁnite and Finite Sets, Vol. 1 (Keszthely, 1973), 323–332, Colloq. Math. Soc. Ja´nos Bolyai, Vol. 10, North-Holland, Amsterdam, 1975.
- [71] A. Dudek and D. Mubayi, On generalized Ramsey numbers for 3-uniform hypergraphs, J. Graph Theory 76 (2014), 217–223.
- [72] A. Dudek, T. Retter and V. Ro¨dl, On generalized Ramsey numbers of Erd˝os and Rogers, J. Combin. Theory Ser. B 109 (2014), 213–227.
- [73] A. Dudek and V. Ro¨dl, On the Folkman number f(2,3,4), Exp. Math. 17 (2008), 63–67.
- [74] A. Dudek and V. Ro¨dl, On Ks-free subgraphs in Ks+k-free graphs and vertex Folkman numbers, Combinatorica 31 (2011), 39–53.
- [75] R. A. Duke, H. Lefmann, and V. Ro¨dl, A fast approximation algorithm for computing the frequencies of subgraphs in a given graph, SIAM J. Comput. 24 (1995), 598–620.
- [76] N. Eaton, Ramsey numbers for sparse graphs, Discrete Math. 185 (1998), 63–75.
- [77] D. Eichhorn and D. Mubayi, Edge-coloring cliques with many colors on subcliques, Combinatorica 20 (2000), 441–444.
- [78] P. Erd˝os, Some remarks on the theory of graphs, Bull. Amer. Math. Soc. 53 (1947), 292–294.
- [79] P. Erd˝os, Graph theory and probability II, Canad. J. Math. 13 (1961), 346–352.
- [80] P. Erd˝os, On the number of complete subgraphs contained in certain graphs, Magyar Tud. Akad. Mat. Kutat´ Int. K¨zl. 7 (1962), 459–464.
- [81] P. Erd˝os, Problems and results on ﬁnite and inﬁnite graphs, in Recent advances in graph theory (Proc. Second Czechoslovak Sympos., Prague, 1974), 183–192, Academia, Prague, 1975.
- [82] P. Erd˝os, Solved and unsolved problems in combinatorics and combinatorial number theory, in Proceedings of the Twelfth Southeastern Conference on Combinatorics, Graph Theory and Computing, Vol. I (Baton Rouge, La., 1981), Congr. Numer. 32 (1981), 49–62.
- [83] P. Erd˝os, On the combinatorial problems which I would most like to see solved, Combinatorica 1 (1981), 25–42.
- [84] P. Erd˝os, On some problems in graph theory, combinatorial analysis and combinatorial number theory, in Graph theory and combinatorics (Cambridge, 1983), 1–17, Academic Press, London, 1984.
- [85] P. Erd˝os, Problems and results on graphs and hypergraphs: similarities and diﬀerences, in Mathematics of Ramsey theory, 12–28, Algorithms Combin., 5, Springer, Berlin, 1990.


- [86] P. Erd˝os, On some of my favourite problems in various branches of combinatorics, in Proceedings of the Fourth Czechoslovakian Symposium on Combinatorics, Graphs and Complexity (Prachatice, 1990), 69–79, Ann. Discrete Math., 51, North-Holland, Amsterdam, 1992.
- [87] P. Erd˝os, Problems and results in discrete mathematics, Discrete Math. 136 (1994), 53–73.
- [88] P. Erd˝os, R. J. Faudree, C. C. Rousseau and R. H. Schelp, The size Ramsey number, Period. Math. Hungar. 9 (1978), 145–161.
- [89] P. Erd˝os and R. Graham, On partition theorems for ﬁnite graphs, in Inﬁnite and Finite Sets, Vol. 1 (Keszthely, 1973), 515–527, Colloq. Math. Soc. Ja´nos Bolyai, Vol. 10, North-Holland, Amsterdam, 1975.
- [90] P. Erd˝os and A. Gy´arf´as, A variant of the classical Ramsey problem, Combinatorica 17 (1997), 459–467.
- [91] P. Erd˝os and A. Hajnal, Research problems 2–3, J. Combin. Theory 2 (1967), 104–105.
- [92] P. Erd˝os and A. Hajnal, On Ramsey like theorems, problems and results, in Combinatorics (Proc. Conf. Combinatorial Math., Math. Inst., Oxford, 1972), 123–140, Inst. Math. Appl., Southend-on-Sea, 1972.
- [93] P. Erd˝os and A. Hajnal, On spanned subgraphs of graphs, in Contributions to graph theory and its applications (Internat. Colloq., Oberhof, 1977), 80–96, Tech. Hochschule Ilmenau, Ilmenau, 1977.
- [94] P. Erd˝os and A. Hajnal, Ramsey-type theorems, Discrete Appl. Math. 25 (1989), 37–52.
- [95] P. Erd˝os, A. Hajnal and J. Pach, On a metric generalization of Ramsey’s theorem, Israel J. Math. 102 (1997), 283–295.
- [96] P. Erd˝os, A. Hajnal and J. Pach, A Ramsey-type theorem for bipartite graphs, Geombinatorics 10 (2000), 64–68.
- [97] P. Erd˝os, A. Hajnal and L. Po´sa, Strong embeddings of graphs into colored graphs, in Inﬁnite and Finite Sets, Vol. 1 (Keszthely, 1973), 585–595, Colloq. Math. Soc. Ja´nos Bolyai, Vol. 10, North-Holland, Amsterdam, 1975.
- [98] P. Erd˝os, A. Hajnal and R. Rado, Partition relations for cardinal numbers, Acta Math. Acad. Sci. Hungar. 16 (1965), 93–196.
- [99] P. Erd˝os and R. Rado, Combinatorial theorems on classiﬁcations of subsets of a given set, Proc. London Math. Soc. 3 (1952), 417–439.
- [100] P. Erd˝os and C. A. Rogers, The construction of certain graphs, Canad. J. Math. 14 (1962), 702–707.
- [101] P. Erd˝os and M. Simonovits, Cube-supersaturated graphs and related problems, in Progress in graph theory (Waterloo, Ont., 1982), 203–218, Academic Press, Toronto, ON, 1984.


- [102] P. Erd˝os and G. Szekeres, A combinatorial problem in geometry, Compos. Math. 2 (1935), 463–470.
- [103] P. Erd˝os and E. Szemere´di, On a Ramsey type theorem, Period. Math. Hungar. 2 (1972), 295–299.
- [104] G. Fiz Pontiveros, S. Griﬃths and R. Morris, The triangle-free process and R(3,k), preprint.
- [105] G. Fiz Pontiveros, S. Griﬃths, R. Morris, D. Saxton and J. Skokan, On the Ramsey number of the triangle and the cube, to appear in Combinatorica.
- [106] G. Fiz Pontiveros, S. Griﬃths, R. Morris, D. Saxton and J. Skokan, The Ramsey number of the clique and the hypercube, J. Lond. Math. Soc. 89 (2014), 680–702.
- [107] J. Folkman, Graphs with monochromatic complete subgraphs in every edge coloring, SIAM J. Appl. Math. 18 (1970), 19–24.
- [108] J. Fox, There exist graphs with super-exponential Ramsey multiplicity constant, J. Graph Theory 57 (2008), 89–98.
- [109] J. Fox, A. Grinshpun and J. Pach, The Erd˝os–Hajnal conjecture for rainbow triangles, to appear in J. Combin. Theory Ser. B.
- [110] J. Fox and J. Pach, Erd˝os–Hajnal-type results on intersection patterns of geometric objects, in Horizons of combinatorics, 79–103, Bolyai Soc. Math. Stud., 17, Springer, Berlin, 2008.
- [111] J. Fox and J. Pach, Applications of a new separator theorem for string graphs, Combin. Probab. Comput. 23 (2014), 66–74.
- [112] J. Fox, J. Pach, B. Sudakov and A. Suk, Erd˝os–Szekeres-type theorems for monotone paths and convex bodies, Proc. Lond. Math. Soc. 105 (2012), 953–982.
- [113] J. Fox, J. Pach and Cs. D. To´th, Intersection patterns of curves, J. Lond. Math. Soc. 83

(2011), 389–406.

- [114] J. Fox and B. Sudakov, Induced Ramsey-type theorems, Adv. Math. 219 (2008), 1771–1800.
- [115] J. Fox and B. Sudakov, Ramsey-type problem for an almost monochromatic K4, SIAM J. Discrete Math. 23 (2008/09), 155–162.
- [116] J. Fox and B. Sudakov, Density theorems for bipartite graphs and related Ramsey-type results, Combinatorica 29 (2009), 153–196.
- [117] J. Fox and B. Sudakov, Two remarks on the Burr–Erdo˝s conjecture, European J. Combin. 30 (2009), 1630–1645.
- [118] J. Fox and B. Sudakov, Dependent Random Choice, Random Structures Algorithms 38 (2011), 68–99.


- [119] P. Frankl and V. Ro¨dl, Large triangle-free subgraphs in graphs without K4, Graphs Combin. 2 (1986), 135–144.
- [120] P. Frankl and R. M. Wilson, Intersection theorems with geometric consequences, Combinatorica 1 (1981), 357–368.
- [121] E. Friedgut, V. Ro¨dl and M. Schacht, Ramsey properties of discrete random structures, Random Structures Algorithms 37 (2010), 407–436.
- [122] J. Friedman and N. Pippenger, Expanding graphs contain all small trees, Combinatorica 7

(1987), 71–76.

- [123] C. Godsil and G. Royle, Algebraic Graph Theory, Springer, 2001.
- [124] A. W. Goodman, On sets of acquaintances and strangers at any party, Amer. Math. Monthly 66 (1959), 778–783.
- [125] W. T. Gowers, A new proof of Szemere´di’s theorem for arithmetic progressions of length four, Geom. Funct. Anal. 8 (1998), 529–551.
- [126] W. T. Gowers, Hypergraph regularity and the multidimensional Szemere´di theorem, Ann. of Math. 166 (2007), 897–946.
- [127] R. L. Graham and V. Ro¨dl, Numbers in Ramsey theory, in Surveys in Combinatorics 1987, 111–153, London Math. Soc. Lecture Note Ser., Vol. 123, Cambridge University Press, Cambridge, 1987.
- [128] R. L. Graham, V. Ro¨dl and A. Rucin´ski, On graphs with linear Ramsey numbers, J. Graph Theory 35 (2000), 176–192.
- [129] R. L. Graham, V. Ro¨dl and A. Rucin´ski, On bipartite graphs with linear Ramsey numbers, Combinatorica 21 (2001), 199–209.
- [130] R. L. Graham, B. L. Rothschild and J. H. Spencer, Ramsey theory, 2nd edition, Wiley, 1990.
- [131] B. Green and T. Tao, The primes contain arbitrarily long arithmetic progressions, Ann. of Math. 167 (2008), 481–547.
- [132] J. A. Grytczuk, M. Ha uszczak and H. A. Kierstead, On-line Ramsey theory, Electron. J. Combin. 11 (2004), Research Paper 60, 10pp.
- [133] A. Gy´arf´as, On a Ramsey type problem of Shelah, in Extremal problems for ﬁnite sets (Visegr´d, 1991), 283–287, Bolyai Soc. Math. Stud., 3, Ja´nos Bolyai Math. Soc., Budapest, 1994.
- [134] A. Hajnal, Rainbow Ramsey theorems for colorings establishing negative partition relations, Fund. Math. 198 (2008), 255–262.


- [135] L. Harrington and J. Paris, A mathematical incompleteness in Peano arithmetic, in Handbook of Mathematical Logic, 1133–1142, North-Holland, Amsterdam, 1977.
- [136] H. Hatami, J. Hladky´, D. Kra´l’, S. Norine and A. Razborov, Non-three-colorable common graphs exist, Combin. Probab. Comput. 21 (2012), 734–742.
- [137] P. E. Haxell, Y. Kohayakawa and T.  Luczak, The induced size-Ramsey number of cycles, Combin. Probab. Comput. 4 (1995), 217–239.
- [138] P. Horn, K. G. Milans and V. Ro¨dl, Degree Ramsey numbers of closed blowups of trees, Electron. J. Combin. 21 (2014), Paper 2.5, 6pp.
- [139] C. Jagger, P. Sˇˇtovı´cˇek and A. Thomason, Multiplicities of subgraphs, Combinatorica 16

(1996), 123–141.

- [140] H. A. Kierstead and G. Konjevod, Coloring number and on-line Ramsey theory for graphs and hypergraphs, Combinatorica, 29 (2009), 49–64.
- [141] J. H. Kim, The Ramsey number R(3,t) has order of magnitude t2/log t, Random Structures Algorithms 7 (1995), 173–207.
- [142] J. H. Kim, C. Lee and J. Lee, Two approaches to Sidorenko’s conjecture, to appear in Trans. Amer. Math. Soc.
- [143] W. B. Kinnersley, K. G. Milans and D. B. West, Degree Ramsey numbers of graphs, Combin. Probab. Comput. 21 (2012), 229–253.
- [144] Y. Kohayakawa, H. Pr¨omel and V. Ro¨dl, Induced Ramsey numbers, Combinatorica 18 (1998), 373–404.
- [145] Y. Kohayakawa, V. Ro¨dl, M. Schacht and E. Szemere´di, Sparse partition universal graphs for graphs of bounded degree, Adv. Math. 226 (2011), 5041–5065.
- [146] A. V. Kostochka and D. Mubayi, When is an almost monochromatic K4 guaranteed? Combin. Probab. Comput. 17 (2008), 823–830.
- [147] A. V. Kostochka and V. Ro¨dl, On graphs with small Ramsey numbers, J. Graph Theory 37

(2001), 198–204.

- [148] A. V. Kostochka and V. Ro¨dl, On Ramsey numbers of uniform hypergraphs with given maximum degree, J. Combin. Theory Ser. A 113 (2006), 1555–1564.
- [149] A. V. Kostochka and B. Sudakov, On Ramsey numbers of sparse graphs, Combin. Probab. Comput. 12 (2003), 627–641.
- [150] M. Krivelevich, Bounding Ramsey numbers through large deviation inequalities, Random Structures Algorithms 7 (1995), 145–155.


- [151] M. Krivelevich and B. Sudakov, Pseudo-random graphs, in More sets, graphs and numbers, 199–262, Bolyai Soc. Math. Stud., 15, Springer, Berlin, 2006.
- [152] A. Kurek and A. Rucin´ski, Two variants of the size Ramsey number, Discuss. Math. Graph Theory 25 (2005), 141–149.
- [153] A. R. Lange, S. P. Radziszowski and X. Xu, Use of MAX-CUT for Ramsey arrowing of triangles, J. Combin. Math. Combin. Comput. 88 (2014), 61–71.
- [154] D. Larman, J. Matousˇek, J. Pach and J. To¨ro˝csik, A Ramsey-type result for convex sets, Bull. London Math. Soc. 26 (1994), 132–136.
- [155] J. L. X. Li and B. Szegedy, On the logarithmic calculus and Sidorenko’s conjecture, to appear in Combinatorica.
- [156] L. Lu, Explicit construction of small Folkman graphs, SIAM J. Discrete Math. 21 (2007), 1053–1060.
- [157] T.  Luczak and V. Ro¨dl, On induced Ramsey numbers for graphs with bounded maximum degree, J. Combin. Theory Ser. B 66 (1996), 324–333.
- [158] W. Mader, Homomorphies¨atze fu¨r Graphen, Math. Ann. 178 (1968), 154–168.
- [159] K. G. Milans, D. Stolee and D. B. West, Ordered Ramsey theory and track representations of graphs, to appear in J. Combin.
- [160] G. Mills, Ramsey–Paris–Harrington numbers for graphs, J. Combin. Theory Ser. A 38 (1985), 30–37.
- [161] G. Moshkovitz and A. Shapira, Ramsey theory, integer partitions and a new proof of the Erd˝os–Szekeres theorem, Adv. Math. 262 (2014), 1107–1129.
- [162] D. Mubayi, Edge-coloring cliques with three colors on all 4-cliques, Combinatorica 18 (1998), 293–296.
- [163] B. Nagle, S. Olsen, V. Ro¨dl and M. Schacht, On the Ramsey number of sparse 3-graphs, Graphs Combin. 27 (2008), 205–228.
- [164] B. Nagle, V. Ro¨dl and M. Schacht, The counting lemma for regular k-uniform hypergraphs, Random Structures Algorithms 28 (2006), 113–179.
- [165] R. Nenadov and A. Steger, A short proof of the random Ramsey theorem, to appear in Combin. Probab. Comput.
- [166] J. Nesˇetrˇil and V. Ro¨dl, The Ramsey property for graphs with forbidden complete subgraphs, J. Combin. Theory Ser. B 20 (1976), 243–249.
- [167] J. Nesˇetrˇil and V. Ro¨dl, Simple proof of the existence of restricted Ramsey graphs by means of a partite construction, Combinatorica 1 (1981), 199–202.


- [168] J. Nesˇetrˇil and J. A. V¨a¨na¨nen, Combinatorics and quantiﬁers, Comment. Math. Univ. Carolin. 37 (1996), 433–443.
- [169] S. Nieß, Counting monochromatic copies of K4: a new lower bound for the Ramsey multiplicity problem, preprint.
- [170] V. Nikiforov and C. C. Rousseau, Ramsey goodness and beyond, Combinatorica 29 (2009), 227–262.
- [171] N. Paul and C. Tardif, The chromatic Ramsey number of odd wheels, J. Graph Theory 69

(2012), 198–205.

- [172] H. Pr¨omel and V. Ro¨dl, Non-Ramsey graphs are clog n-universal, J. Combin. Theory Ser. A 88 (1999), 379–384.
- [173] S. Radziszowski, Small Ramsey numbers, Electron. J. Combin. (2014), DS1.
- [174] F. P. Ramsey, On a problem of formal logic, Proc. London Math. Soc. 30 (1930), 264–286.
- [175] A. A. Razborov, Flag algebras, J. Symbolic Logic 72 (2007), 1239–1282.
- [176] V. Ro¨dl, The dimension of a graph and generalized Ramsey theorems, Master’s thesis, Charles University, 1973.
- [177] V. Ro¨dl, On universality of graphs with uniformly distributed edges, Discrete Math. 59

(1986), 125–134.

- [178] V. Ro¨dl, On homogeneous sets of positive integers, J. Combin. Theory Ser. A 102 (2003), 229–240.
- [179] V. Ro¨dl and A. Rucin´ski, Lower bounds on probability thresholds for Ramsey properties, in Combinatorics, Paul Erd˝os is eighty, Vol. 1, 317–346, Bolyai Soc. Math. Stud., Ja´nos Bolyai Math. Soc., Budapest, 1993.
- [180] V. Ro¨dl and A. Rucin´ski, Threshold functions for Ramsey properties, J. Amer. Math. Soc. 8

(1995), 917–942.

- [181] V. Ro¨dl, A. Rucin´ski and M. Schacht, An exponential-type upper bound for Folkman numbers, preprint.
- [182] V. Ro¨dl and M. Schacht, Complete partite subgraphs in dense hypergraphs, Random Structures Algorithms 41 (2012), 557–573.
- [183] V. Ro¨dl and J. Skokan, Regularity lemma for uniform hypergraphs, Random Structures Algorithms 25 (2004), 1–42.
- [184] V. Ro¨dl and E. Szemere´di, On size Ramsey numbers of graphs with bounded maximum degree, Combinatorica 20 (2000), 257–262.


- [185] V. Ro¨dl and R. Thomas, Arrangeability and clique subdivisions, in The mathematics of Paul Erd˝os, II, 236–239, Algorithms Combin., 14, Springer, Berlin, 1997.
- [186] G. N. Sa´rk¨ozy and S. M. Selkow, On edge colorings with at least q colors in every subset of p vertices, Electron. J. Combin. 8 (2001), Research Paper 9, 6pp.
- [187] G. N. Sa´rk¨ozy and S. M. Selkow, An application of the regularity lemma in generalized Ramsey theory, J. Graph Theory 44 (2003), 39–49.
- [188] D. Saxton and A. Thomason, Hypergraph containers, to appear in Invent. Math.
- [189] M. Schacht, Extremal results for discrete random structures, preprint.
- [190] J. Shearer, A note on the independence number of triangle-free graphs, Discrete Math. 46

(1983), 83–87.

- [191] J. Shearer, On the independence number of sparse graphs, Random Structures Algorithms 7

(1995), 269–271.

- [192] S. Shelah, Primitive recursive bounds for van der Waerden numbers, J. Amer. Math. Soc. 1

(1989), 683–697.

- [193] S. Shelah, A ﬁnite partition theorem with double exponential bound, in The mathematics of Paul Erd˝os, II, 240–246, Algorithms Combin., 14, Springer, Berlin, 1997.
- [194] L. Shi, Cube Ramsey numbers are polynomial, Random Structures Algorithms 19 (2001), 99–101.
- [195] L. Shi, The tail is cut for Ramsey numbers of cubes, Discrete Math. 307 (2007), 290–292.
- [196] A. F. Sidorenko, Cycles in graphs and functional inequalities, Math. Notes 46 (1989), 877–882.
- [197] A. F. Sidorenko, A correlation inequality for bipartite graphs, Graphs Combin. 9 (1993), 201–204.
- [198] J. H. Spencer, Ramsey’s theorem – a new lower bound, J. Combin. Theory Ser. A 18 (1975), 108–115.
- [199] J. H. Spencer, Asymptotic lower bounds for Ramsey functions, Discrete Math. 20 (1977/78), 69–76.
- [200] J. H. Spencer, Three hundred million points suﬃce, J. Combin. Theory Ser. A 49 (1988), 210–217.
- [201] K. Sperfeld, On the minimal monochromatic K4-density, preprint.
- [202] B. Sudakov, A few remarks on the Ramsey–Tura´n-type problems, J. Combin. Theory Ser. B 88 (2003), 99–106.


- [203] B. Sudakov, A new lower bound for a Ramsey-type problem, Combinatorica 25 (2005), 487– 498.
- [204] B. Sudakov, Large Kr-free subgraphs in Ks-free graphs and some other Ramsey-type problems, Random Structures Algorithms 26 (2005), 253–265.
- [205] B. Sudakov, A conjecture of Erd˝os on graph Ramsey numbers, Adv. Math. 227 (2011), 601– 609.
- [206] E. Szemere´di, On sets of integers containing no k elements in arithmetic progression, Acta Arith. 27 (1975), 199–245.
- [207] E. Szemere´di, Regular partitions of graphs, in Proble`mes Combinatoires et The´orie des Graphes (Orsay 1976), 399–401, Colloq. Internat. CNRS, 260, CNRS, Paris, 1978.
- [208] A. Thomason, Pseudorandom graphs, in Random graphs ’85 (Poznan´, 1985), 307–331, NorthHolland Math. Stud., Vol. 144, North-Holland, Amsterdam, 1987.
- [209] A. Thomason, Random graphs, strongly regular graphs and pseudorandom graphs, in Surveys in Combinatorics 1987, 173–195, London Math. Soc. Lecture Note Ser., Vol. 123, Cambridge University Press, Cambridge, 1987.
- [210] A. Thomason, An upper bound for some Ramsey numbers, J. Graph Theory 12 (1988), 509–517.
- [211] A. Thomason, A disproof of a conjecture of Erd˝os in Ramsey theory, J. London Math. Soc. 39 (1989), 246–255.
- [212] B. L. van der Waerden, Beweis einer Baudetschen Vermutung, Nieuw. Arch. Wisk. 15 (1927), 212–216.
- [213] G. Wolfovitz, K4-free graphs without large induced triangle-free subgraphs, Combinatorica 33 (2013), 623–631.
- [214] X. Zhu, The fractional version of Hedetniemi’s conjecture is true, European J. Combin. 32


(2011), 1168–1175.

