arXiv:1111.0253v2[math.CO]8Nov2011

Nearly Complete Graphs Decomposable into Large Induced Matchings and their Applications

Noga Alon ∗ Ankur Moitra † Benny Sudakov ‡ November 27, 2024

Abstract We describe two constructions of (very) dense graphs which are edge disjoint unions of large

induced matchings. The ﬁrst construction exhibits graphs on N vertices with N2 −o(N2) edges, which can be decomposed into pairwise disjoint induced matchings, each of size N1−o(1). The

second construction provides a covering of all edges of the complete graph KN by two graphs, each being the edge disjoint union of at most N2−δ induced matchings, where δ > 0.058. This disproves (in a strong form) a conjecture of Meshulam, substantially improves a result of Birk, Linial and Meshulam on communicating over a shared channel, and (slightly) extends the analysis of Ha˚stad and Wigderson of the graph test of Samorodnitsky and Trevisan for linearity. Additionally, our constructions settle a combinatorial question of Vempala regarding a candidate rounding scheme for the directed Steiner tree problem.

![image 1](<2011-alon-nearly-complete-graphs-decomposable_images/imageFile1.png>)

∗Sackler School of Mathematics and Blavatnik School of Computer Science, Tel Aviv University, Tel Aviv 69978, Israel and Institute for Advanced Study, Princeton, New Jersey, 08540, USA. Email: nogaa@tau.ac.il. Research supported in part by an ERC Advanced grant, by a USA-Israeli BSF grant and by NSF grant No. DMS-0835373.

†Institute for Advanced Study, Princeton, New Jersey, 08540, USA. Email: moitra@ias.edu. Research supported in part by NSF grant No. DMS-0835373 and by an NSF Computing and Innovation Fellowship.

‡Department of Mathematics, UCLA, Los Angeles, CA 90095. Email: bsudakov@math.ucla.edu. Research supported in part by NSF grant DMS-1101185, NSF CAREER award DMS-0812005 and by a USA-Israeli BSF grant.

# 1 Introduction

## 1.1 Background

Dense graphs consisting of large pairwise edge disjoint induced matchings have found several applications in Combinatorics, Complexity Theory and Information Theory. Call a graph G = (V,E) an (r,t)-Ruzsa-Szemere´di graph ((r,t)-RS graph, for short) if its set of edges consists of t pairwise disjoint induced matchings, each of size r. The total number of edges of such a graph is clearly rt. Graphs of this type are useful when both r and t are relatively large as a function of the number of vertices N. There are several known interesting constructions, relying on a variety of techniques.

The ﬁrst surprising construction was given by Ruzsa and Szemere´di [21], who applied a result of Behrend [7] about the existence of dense subsets of {1,2,...,Θ(N)} containing no 3-term arithmetic progressions to prove that there are (r,t)-RS graphs on N vertices with r = eO( N

√logN) and t = N/3. They applied this construction, together with the regularity lemma of Szemere´di [24], to settle an extremal problem of Brown, Erd˝os and So´s [8, 9], showing that the maximum possible number of edges in a 3-uniform hypergraph on N vertices which contains no 6 vertices spanning at least 3 edges is bigger than N2−ǫ and smaller than ǫN2, for any ǫ > 0, provided N > N0(ǫ). See also [13],[5] for more details about this problem, its extensions, and their connection to (r,t)-RS graphs.

![image 2](<2011-alon-nearly-complete-graphs-decomposable_images/imageFile2.png>)

![image 3](<2011-alon-nearly-complete-graphs-decomposable_images/imageFile3.png>)

Note that the above construction provides graphs with N vertices and eO(N2

√logN) edges, that is, rather dense graphs, but still ones in which the number of edges is o(N2). These graphs and some appropriate variants have been used by the ﬁrst author in [1], to show that the problem of testing H-freeness in graphs requires a super-polynomial (in 1/ǫ) number of queries if and only if H is not bipartite. The proof for one sided error algorithms is given in [1], and an extension for two sided algorithms is described in [3]. A similar application of these graphs for testing induced H-freeness appears in [4], and yet another very recent application showing that testing graph-perfectness requires a super polynomial number of queries appears in [2].

![image 4](<2011-alon-nearly-complete-graphs-decomposable_images/imageFile4.png>)

![image 5](<2011-alon-nearly-complete-graphs-decomposable_images/imageFile5.png>)

The above graphs have also been applied by Ha˚stad and Wigderson [19] to give an improved analysis of the graph test of Samorodnitsky and Trevisan for linearity and for PCP with low amortized complexity [22].

Another construction of (r,t)-RS graphs on N vertices, with r = N/3−o(N) and t = NΩ(1/log logN)

was given by Fischer et. al. in [14]. Note that the matchings here are of linear size, but their number is much smaller than in the original construction of Ruzsa and Szemere´di. The construction here is combinatorial, and Fischer et. al. use these graphs to establish an NΩ(1/log logN) lower bound for testing monotonicity in general posets.

Yet another construction was obtained by Birk, Linial and Meshulam [10], and in an improved form by Meshulam [20]. For the application in [10] it is crucial to obtain graphs with positive density. Indeed, the graphs here are (r,t)-graphs on N vertices with r = (log N)Ω(log logN/(log log logN)2)

and t roughly 24N2r. Thus, their number of edges is about N2/24. The method here relies on a construction of low degree representation of the OR function, due to Barrington, Beigel and

![image 6](<2011-alon-nearly-complete-graphs-decomposable_images/imageFile6.png>)

Rudich [6]. The application in [10] is in Information Theory, the graphs are applied to design an eﬃcient deterministic scheduling scheme for communicating over a shared directional multichannel.

Interestingly, none of these constructions address the question of whether or not an (r,t)-RS graph can simultaneously have positive density and yet be an edge disjoint union of polynomially large induced matchings. This range of parameters is important for some applications - especially ones in which there is a tradeoﬀ between the number of missing edges and the number of induced matchings needed to cover the graph. Indeed, Meshulam [20] conjecture that there are no such graphs. We are able to disprove this conjecture in the strongest possible sense: The density of our construction is 1 − o(1) and yet r is nearly linear in N. We also give a number of applications of

our constructions.

## 1.2 Our Results

We construct (r,t)-RS graphs on N vertices with rt = (1 − o(1)) N2 , and r = N1−o(1). Thus, not only can we have graphs with positive edge density which are edge disjoint union of induced

matchings of size NΩ(1), we can in fact have the edge density 1 − o(1), where the size of each matching is N1−o(1). We also describe another construction of a partition of the complete graph KN into two subgraphs, each being a union of at most N2−δ induced matchings, where δ > 0.058. The main diﬀerence between the new constructions presented here and the previous ones mentioned above, is that the graphs constructed here are of density 1 − o(1), that is, almost all edges of the complete graph KN are covered, and yet all these edges can be partitioned into large pairwise disjoint induced matchings. This surprising property turns out to be useful in various applications.

Our ﬁrst construction is geometric, and is inspired by the recent work of Fox and Loh [16] on dense graphs in which every edge is contained in at least one triangle and yet no edge is contained in too many triangles. The construction follows the basic approach of Fox and Loh (slightly modiﬁed according to the remark of the ﬁrst author, mentioned at the end of [16]) with diﬀerent parameters. An additional (simple) argument is required in decomposing sparse graphs into not too many induced matchings. Our second construction applies some basic tools from Coding Theory. Also we make us of the regularity lemma and some combinatorial and entropy based techniques to prove lower bounds for these questions.

It is worth noting that a general result of Frankl and Fu¨redi [17], implies that for any ﬁxed r,

there are (r,t)-RS graphs G on N vertices with rt = (1 − o(1)) N2 . This is proved by choosing the non-edges of G randomly and by applying the nibble technique to obtain the existence of the

desired matchings. Using this method, however, the induced matchings obtained are of constant size, whereas we are interested, crucially, in large matchings. The techniques of [17] cannot provide induced matchings of size exceeding Θ(log N).

We apply our results to signiﬁcantly improve the application in [10]. As mentioned earlier, Birk, Linial and Meshulam construct (r,t)-graphs on N vertices with r = (log N)Ω(log logN/(log log logN)2) and rt roughly N242. The authors then use these graphs to design a communication protocol over a shared directional multi-channel – it is critical for the application that these graphs have positive density. The communication protocol based on these graphs achieves a round complexity of O(Nr2) and this is a slightly better than poly-logarithmic improvement over the naive protocol for bus-based architectures.

![image 7](<2011-alon-nearly-complete-graphs-decomposable_images/imageFile7.png>)

![image 8](<2011-alon-nearly-complete-graphs-decomposable_images/imageFile8.png>)

We can use our construction to achieve a round complexity of O(N2−δ) over a shared directional multi-channel. This is the ﬁrst such protocol that is a polynomial improvement over the naive protocol. We can accomplish this using just two receivers per station (this corresponds to a partition of the edges of a complete bipartite graph into two graphs that can be decomposed into large induced matchings). In case we are allowed C = C(ǫ) receivers per station, we can achieve a round complexity that is O(N1+ǫ) for any ǫ > 0. Hence, previous protocols required nearly a quadratic number of rounds, and our protocols require only a nearly-linear number of rounds.

Our constructions also disprove the recent conjecture of Meshulam. Moreover, we can achieve a density approaching one while simultaneously being able to decompose the graph into at most a nearly-linear number of induced matchings.

Besides their applications to the problems of [10] and [20], our constructions can be plugged in the result of [19], extending it to a new range of the parameters that may be of interest. Lastly, we also answer a question of Vempala [25], showing that a certain rounding scheme for the directed Steiner tree problem is not eﬀective.

The rest of this paper is organized as follows. In the next section we describe the two new constructions. Lower bounds showing that these are not far from being tight are given in Section

- 3. In Section 4 we describe the applications of these graphs. The ﬁnal Section 5 contains some concluding remarks and open problems.


# 2 Constructions

## 2.1 A Geometric Construction

Here we construct nearly-complete graphs that can be covered by an almost linear number of induced matchings. These graphs will be based on a geometric construction inspired by a recent construction of Fox and Loh [16].

We ﬁrst describe a graph G = (V,E) and then prove that it can be slightly modiﬁed to yield a nearly complete (r,t)-RS graph. Set V = [C]n for some constant C to be chosen later. Let N = Cn be the number of vertices. Each vertex x ∈ V will be interpreted as an integer vector in n dimensions with coordinates in [C] = {1,2,... ,C}, where for technical reasons it is convenient to assume that n is even. Let µ = Ex,y[ x − y 22] where x and y are sampled uniformly at random from V . We could compute µ, but we will not need this exact value.

Next, we describe the set E of edges. A pair of vertices x and y are adjacent if and only if

x − y 22 − µ ≤ n.

This condition implies that the number of missing edges is small, by a standard application of Hoeﬀding’s Inequality:

- Claim 2.1. N2 − |E| ≤ N2 2e−n/2C4


Proof: The quantity x − y 22 = ni=1(xi − yi)2 and hence is the sum of independent random variables (when x and y are chosen uniformly at random from V ). Each variable is bounded in the range [0,C2] and hence we can apply Hoeﬀding’s Inequality to obtain

Pr[| x − y 22 − µ| > n] ≤ 2e−n/2C4 and this implies the Claim.

As a ﬁrst step, we will cover all the edges of G by a linear number of induced subgraphs of small (but super-constant) maximum degree. We will then use this covering to obtain a covering via an almost linear number of induced matchings. Next, we describe the (preliminary) induced subgraphs that we use to cover G.

We will deﬁne one subgraph Gz for each z ∈ V . Let Vz (the vertex set of Gz) be

Vz = x ∈ V : | x − z 22 − µ/4| ≤ 3n/4 .

The subgraph Gz is the induced graph on Vz. First, we prove that these subgraphs Gz do indeed cover the edges of G:

- Lemma 2.2. Let n ≥ 2C. For all (x,y) ∈ E, there is a z such that x,y ∈ Vz Proof: First we establish a simple Claim that will help us choose an appropriate z:


- Claim 2.3. Let a be a vector in which the absolute value of each entry is at most C. Then there is a vector w where each entry is ±1/2 such that |(a,w)| = | ni=1 aiwi| ≤ C/2 ≤ n/4


Proof: We can prove this by induction by considering the partial sum ri=1 aiwi which we will assume is at most C/2 in absolute value. We can choose wr+1 so that ar+1wr+1 has the opposite sign of this partial sum and this implies that the partial sum ri=1+1 aiwi is also at most C/2 in absolute value (although the sign may have changed). This completes the proof of the claim.

Let a be a vector deﬁned as follows: if yi − xi is even, set ai = 0 and otherwise set ai = yi − xi. We can apply Claim 2.3 to a, but furthermore change the values of w to be zero on indices on which a is zero. Then |(a,w)| is still at most C/2, and wi is ±1/2 whenever ai is non-zero, and zero whenever a is zero. Set z = y+2x +w. Note that z ∈ V because whenever yi+2xi is not an integer, ai must be non-zero and hence wi is ±1/2 and alternatively whenever yi+2xi is an integer, ai is zero and hence wi is zero. Consider the quantity

![image 9](<2011-alon-nearly-complete-graphs-decomposable_images/imageFile9.png>)

![image 10](<2011-alon-nearly-complete-graphs-decomposable_images/imageFile10.png>)

![image 11](<2011-alon-nearly-complete-graphs-decomposable_images/imageFile11.png>)

z − x 22 =

1 4

y − x 2

+ w 22 =

![image 12](<2011-alon-nearly-complete-graphs-decomposable_images/imageFile12.png>)

![image 13](<2011-alon-nearly-complete-graphs-decomposable_images/imageFile13.png>)

y − x 22 + (y − x,w) + w 22

Since x and y are adjacent in G, we have that | 14 y−x 22−µ/4 | ≤ n/4. Also, w 22 ≤ n/4. Finally, (y −x,w) = (a,w) since w is zero iﬀ a is zero. Hence | z −x 22 −µ/4 | ≤ n/4+C/2+n/4 ≤ 3n/4, and an identical argument holds for bounding | z −y 22 −µ/4 |. Thus x,y ∈ Vz and the edge (x,y) is covered by some induced subgraph Gz.

![image 14](<2011-alon-nearly-complete-graphs-decomposable_images/imageFile14.png>)

Next we establish that the maximum degree of any induced subgraph Gz is not too large:

- Lemma 2.4. For all z ∈ V , the maximum degree of Gz is at most (10.5)n.


Proof: Let x ∈ Vz and consider any neighbor y of x that satisﬁes y ∈ Vz. We ﬁrst establish that x and y are close to being antipodal in the ball centered at z, and hence we can bound the number of neighbors of x in Vz by bounding the number of points of V in some small spherical cap around the antipodal point to x.

Deﬁne the antipodal point x′ = 2z − x, this is the antipodal to x with respect to the ball centered at z.

Consider the parallelogram (x,z,y,x+y−z). By the Parallelogram Law, the sum of the squares of the four side lengths equals the sum of the squares of the lengths of the two diagonals. Therefore we obtain

- x − y 22 + x + y − 2z 22 = 2 x − z 22 + 2 y − z 22

Using the deﬁnition of x′, this gives

- x − y 22 + y − x′ 22 = 2 x − z 22 + 2 y − z 22


Hence y − x′ 22 = 2 x − z 22 + 2 y − z 22 − x − y 22 and as both x − z 22 and y − z 22 are approximately µ/4 (since x,y ∈ Vz) and x − y 22 is approximately µ because x is adjacent to y in G, this implies that y − x′ 22 ≤ 4n. Therefore we can bound the degree of x in Gz by the number lattice points in a ball of radius 2√n (centered at the lattice point x′.) The unit n-dimensional cubes centered at these lattice points are pairwise disjoint, each has volume 1, and they are all contained in a ball of radius 2√n + 0.5√n = 2.5√n. Therefore, the number of these points does not exceed the volume of an n dimensional ball of radius 2.5√n. Since n is even, the volume of this ball is

![image 15](<2011-alon-nearly-complete-graphs-decomposable_images/imageFile15.png>)

![image 16](<2011-alon-nearly-complete-graphs-decomposable_images/imageFile16.png>)

![image 17](<2011-alon-nearly-complete-graphs-decomposable_images/imageFile17.png>)

![image 18](<2011-alon-nearly-complete-graphs-decomposable_images/imageFile18.png>)

![image 19](<2011-alon-nearly-complete-graphs-decomposable_images/imageFile19.png>)

(2.5√n)n nn/2

πn/2(2.5√n)n (n/2)!

√

![image 20](<2011-alon-nearly-complete-graphs-decomposable_images/imageFile20.png>)

![image 21](<2011-alon-nearly-complete-graphs-decomposable_images/imageFile21.png>)

< (2πe)n/2

2πe)n < 10.5n,

![image 22](<2011-alon-nearly-complete-graphs-decomposable_images/imageFile22.png>)

= (2.5 ·

![image 23](<2011-alon-nearly-complete-graphs-decomposable_images/imageFile23.png>)

![image 24](<2011-alon-nearly-complete-graphs-decomposable_images/imageFile24.png>)

where here we have used the fact that b! > (b/e)b for any positive integer b. This completes the proof of the lemma.

- Lemma 2.5. Let H be a graph with maximum degree d. Then H can be covered by O(d2) induced matchings.


Proof: Call two edges e1,e2 of H in conﬂict if they either share a common end or there is an edge in H connecting an endpoint of e1 to an endpoint of e2. It is clear that any edge e of H can be in conﬂict with at most 2d − 2 + (2d − 2)(d − 1) < 2d2 other edges of H.

Thus we can initialize each member of a set of 2d2 induced matchings Mi to be the empty set, and for each edge e of H in its turn, add e to the ﬁrst Mi for which e is not in conﬂict with any edge currently in Mi. Since e is in conﬂict with less than 2d2 edges, it can added to some Mi. We can continue this procedure, obtaining a set of less than 2d2 induced matchings covering all edges of H.

It follows that we can decompose the edges of each induced subgraph Gz into at most O(d2) ≤ O((10.5)2n) induced matchings, and this yields a decomposition of G into O(Nd2) induced matchings. These matchings can additionally be made edge-disjoint, since, if any edge is multiply covered we can remove it from all but one of the induced matchings (and the result is still an induced matching). We have thus proved the following.

- Theorem 2.6. For every n,C with n ≥ 2C, n even, there is a graph G on N = Cn vertices that is missing at most Ng edges, for


1 2C4 ln C

+ o(1)

g = 2 −

![image 25](<2011-alon-nearly-complete-graphs-decomposable_images/imageFile25.png>)

and can be covered by Nf disjoint induced matchings, where

.

2ln 10.5 ln C

f = 1 +

+ o(1)

![image 26](<2011-alon-nearly-complete-graphs-decomposable_images/imageFile26.png>)

Hence, for any ǫ > 0 we can construct a graph G on N vertices missing at most N2−δ edges for δ = δ(ǫ) = e−O(1/ǫ), that can be covered by N1+ǫ pairwise disjoint induced matchings. Note that the number of matchings is nearly linear. Note also that by splitting each of these matchings M into ⌊|M|/r⌋ pairwise disjoint matchings, each of size exactly r = N1−ǫ−δ, omitting the remaining |M| − r⌊|M|/r⌋ < r edges, we get an (r,t)-RS graph, where r = N1−ǫ−δ and the number of missing edges is at most 2N2−δ. As ǫ (and hence δ < ǫ) can be chosen to be arbitrarily small, this gives, with the right choice of parameters, an (r,t)-RS graph on N vertices, with r = N1−o(1) and rt = N2 − o(N2).

## 2.2 A Construction Using Error Correcting Codes

Here we construct nearly-complete graphs with large induced matchings using error correcting codes. These constructions will be incomparable to those in the previous section - the number of missing edges will be much smaller (in fact, the number of missing edges can be made asymptotically optimal as we will demonstrate in Section 3.2), but the price we pay is that the average size of an induced matching will only be a small power of N as opposed to nearly-linear. As we will show, the construction in this section will be better tailored to the application in [10] (at least for some values of the relevant parameters) than the construction of the previous section.

Throughout this section, we will use codes over the binary alphabet as well as over a bigger alphabet. Let dH(x,y) be the Hamming distance between two binary strings x and y (of the same length). The Hamming weight of a binary string x is the number of non-zero entries - or equivalently the Hamming distance to the all zeros vector. We can similarly deﬁne the Hamming distance dH(x,y) between two vectors x and y over a larger alphabet [C] as the number of indices where these vectors disagree.

- Deﬁnition 2.7. A [n,k,d] linear code C is a subspace consisting of 2k length n binary vectors such

that for all x,y ∈ C and x = y, dH(x,y) ≥ d. We will call n the encoding length, k the dimension, and d the distance of the code.

An n×k matrix A of full column rank over GF(2) is the generating matrix of a code of dimension k and length n consisting of all linear combinations of its columns. The distance of this code is exactly the minimum Hamming weight of any non-zero code word. Throughout this section we will make use of a particular type of code:

- Deﬁnition 2.8. Call a linear code C proper if the all ones vector is a codeword.


It is well-known that there are linear codes that achieve the Gilbert-Varshamov Bound. In fact, proper codes also achieve this bound:

- Lemma 2.9. If di=0 ni < 2n−k, then there is a proper [n,k,d] code. Thus, there is such a code in which k = (1 − H(d/n))n, where H(x) = −xlog2 x − (1 − x)log2(1 − x) is the binary entropy function.


Proof: We can deﬁne a length n code by choosing an (n−k)×n parity check matrix as follows: for each of the ﬁrst n−1 columns, choose each vector uniformly at random. Choose the last column to be the parity of the preceding n − 1 columns. Let the matrix be B. Then the code C is deﬁned as C = {x ∈ {0,1}n|Bx = 0}. Clearly 1 ∈ C by construction. Since this code is linear, the minimum distance is exactly the minimum Hamming weight of any non-zero codeword. This quantity is exactly the smallest number of columns of B that sum to the all zeros vector.

- Claim 2.10. For any ﬁxed set S of columns of B, the probability that the sum is the all zeros vector is exactly 2−(n−k)

Proof: If this set S does not contain the last column, then the sum of the columns is distributed uniformly on {0,1}n−k. If the set S does contain the last column, then the sum of the columns is exactly the sum of the columns not in the set - i.e. [n]−S - and hence is also distributed uniformly on {0,1}n−k.

So the probability that any set of at most d columns sums to the all zero vector is at most

2−(n−k) di=0 ni , and if di=0 ni < 2n−k there is a parity check matrix B so that the code C has distance at least d + 1 > d. This code has dimension at least k because there are n − k constraints

imposed by the parity check matrix. If these constraints are linearly independent, then the code has dimension exactly k. If these constraints are not linearly independent, we can add additional constraints until the code has dimension exactly k and the distance of the code cannot decrease as we add these constraints.

- Claim 2.11. Let A be the generating matrix for a proper [n,k,d] code C with d > 1. Then deleting any row of A results in a generating matrix A′ for a proper [n − 1,k,d − 1] code.


Proof: Note that C′ = {A′x|x ∈ {0,1}k} and hence C′ (deﬁned by the generating matrix A′) has dimension k, as no nontrivial linear combination of the columns of A′ can be the zero vector, by the assumption d > 1. The all ones vector is still a codeword since Ax = 1 implies that A′x = 1. Finally, the minimum distance of C′ is the minimum Hamming weight of any non-zero code word, and the Hamming weight of any codeword in C decreases by at most one by deleting any index.

Throughout this section let C = Cn be an [n,k,d] code, and let Cn−1,Cn−2,...Cn−d+1 be proper [n − 1,k,d − 1], [n − 2,k,d − 2], ... and [n − d + 1,k,1] codes, respectively.

Next, we deﬁne a graph G = (V,E) that will be the focus of this section. Let V = [C]n and set N = |V | = Cn. Consider two vertices a,b ∈ V , where a = (a1,a2,...an) and b = (b1,b2,...bn) for ai,bi ∈ [C]. There is an edge between a and b if and only if dH(a,b) = ni=1 1ai =bi > n − d.

It is easy to count the number of missing edges. Indeed, in the complement of G each vertex a is connected to all vertices b so that ai = bi for at least d indices i. As the number of missing edges is half the sum of degrees in the complement this gives:

- Claim 2.12. N


n

- 1

![image 27](<2011-alon-nearly-complete-graphs-decomposable_images/imageFile27.png>)

- 2


CN

2 − |E| ≤

i=d

- Lemma 2.13. If nd ≥ C2−1 then


![image 28](<2011-alon-nearly-complete-graphs-decomposable_images/imageFile28.png>)

![image 29](<2011-alon-nearly-complete-graphs-decomposable_images/imageFile29.png>)

n

- 1

![image 30](<2011-alon-nearly-complete-graphs-decomposable_images/imageFile30.png>)

- 2


Cn

i=d

n i

(C − 1)n−i ≤

n i

(C − 1)n−i.

n d

Cn(C − 1)n−d.

Proof: Using the inequality ni ≤ (n/d)i−d nd we obtain a bound

n

i=d

n i

(C − 1)n−i ≤

n d

n−d

(n/d)j(C − 1)−j

(C − 1)n−d

j=0

which implies the Lemma.

Hence the number of missing edges in G is at most Ne for e = 1+ H(d/n)+(1log−d/n) log2(C−1)

2 C +o(1).

![image 31](<2011-alon-nearly-complete-graphs-decomposable_images/imageFile31.png>)

Next, we describe the induced matchings that are used to cover the edges in G. In order to do so, we will deﬁne an equivalence relation over edges of G. In particular, this will be an equivalence relation over ordered pairs (a,b), where a = (a1,a2,...an) and b = (b1,b2,...bn), under the condition that dH(a,b) > n − d.

- Deﬁnition 2.14. Let S ⊂ [n], |S| = r and let (a,b) be a pair of vertices in V where S = {i|ai = bi}. Let x be a {0,1}n−r vector. Let [n] − S = {i1,i2,...in−r} and i1 < i2,... < in−r. Then the x-ﬂip of (a,b) is a pair (c,d) such that for all i ∈ S, ci = ai = bi = di and for all i = ij ∈/ S (i.e. i is the jth smallest index not in S), ci = ai,di = bi if xj = 0 and otherwise ci = bi,di = ai.

Informally, the n − r indices not in S are mapped in order to the n − r bits in x and the corresponding locations in a and b are swapped if and only if the corresponding bit of x is one.

- Deﬁnition 2.15. We will deﬁne a pair (a,b) ∼ (a′,b′) iﬀ S = {i|ai = bi} = S′ = {i|a′i = b′i}, |S| < d and furthermore there is an x ∈ C such that (a′,b′) is the x-ﬂip of (a,b).


Next we will establish that this relation ∼ is indeed an equivalence relation, and that it is actually a relation on unordered pairs, that is (a,b) ∼ (b,a) for all a,b:

- Claim 2.16. (a,b) ∼ (b,a)

This follows because the code Cn−r is proper (for all r < d), and hence the all ones vector 1 lies in Cn−r and (b,a) is the 1-ﬂip of (a,b).

- Claim 2.17. (a,b) ∼ (c,d) iﬀ (c,d) ∼ (a,b)

Proof: By symmetry we only need to establish one direction. Suppose (a,b) ∼ (c,d). Then S = {i|ai = bi} = S′ = {i|ci = di}. Let (c,d) be an x-ﬂip of (a,b) (where x ∈ Cn−r). Then (a,b) is also the x-ﬂip of (c,d).

- Claim 2.18. (a,b) ∼ (c,d) and (c,d) ∼ (e,f) implies (a,b) ∼ (e,f)


Proof: Again note that S = {i|ai = bi} = S′ = {i|ci = di} = S′′ = {i|ei = fi}. Let x,y ∈ Cn−r be such that (c,d) is the x-ﬂip of (a,b) and (e,f) is the y-ﬂip of (c,d). Then x + y ∈ Cn−r since the code is linear, and (e,f) is the x + y-ﬂip of (a,b).

This immediately implies:

- Lemma 2.19. The relation ∼ is an equivalence relation over unordered pairs (a,b) which have Hamming distance > n − d.

Since each code Cn−r (for r < d) has dimension k, each equivalence class has size exactly 2k.

- Lemma 2.20. Each equivalence class is an induced matching consisting of 2k−1 edges.


Proof: Consider two edges (a,b) and (e,f) in the same equivalence class. Let S = {i|ai = bi} = {i|ei = fi} where |S| = r (< d). Let (e,f) be the x-ﬂip of (a,b) for x ∈ Cn−r. Since the code Cn−r has distance at least d − r, the Hamming weight of x is at least d − r. Consider the Hamming distance between a and f. Each index i ∈ S is an index at which a and f agree (i.e. ai = fi). Furthermore, there is a bijection between indices in x that are set to one and indices outside of the set S, for which a and f agree. So the vectors a and f agree on at least r +(d−r) = d indices, and hence af is not an edge in G. Since (e,f) and (f,e) are in the same equivalence class the above argument also shows that ae,be and bf are nonedges.

If we use one induced matching for each equivalence class, then each edge in G is covered exactly once and hence the number of induced matchings needed to cover G is 2|kE−|1 ≤ N2k2.

![image 32](<2011-alon-nearly-complete-graphs-decomposable_images/imageFile32.png>)

![image 33](<2011-alon-nearly-complete-graphs-decomposable_images/imageFile33.png>)

- Theorem 2.21. For every n,d,C such that nd ≥ C−2 1 , there is a graph G on N = Cn vertices that is missing at most Ne edges, for


![image 34](<2011-alon-nearly-complete-graphs-decomposable_images/imageFile34.png>)

![image 35](<2011-alon-nearly-complete-graphs-decomposable_images/imageFile35.png>)

H(d/n) + (1 − d/n)log2(C − 1) log2 C

e = 1 +

+ o(1)

![image 36](<2011-alon-nearly-complete-graphs-decomposable_images/imageFile36.png>)

and can be covered by Nf disjoint induced matchings, where

.

1 − H(d/n) log2 C

+ o(1)

f = 2 −

![image 37](<2011-alon-nearly-complete-graphs-decomposable_images/imageFile37.png>)

In particular, for any ǫ > 0, there is a graph G on N vertices missing at most N3/2+ǫ edges that can be covered by N2−cǫ3 induced matchings. This is obtained by choosing C for which log2 C = Θ(1/ǫ) and d/n = 21 − Θ(ǫ).

![image 38](<2011-alon-nearly-complete-graphs-decomposable_images/imageFile38.png>)

Also we can choose C = 34 and d = 0.19n, in which case e,f < 1.942. Thus we can cover the edges of a complete graph on 2N vertices by two graphs G1 (set to G with N replaced by 2N in the above construction) and G2 (set to the complement of G), where the number of induced matchings needed to cover the edges of G1 is O(N2−δ) for δ > 0.058, and the same holds for G2. For the applications we need that the above statement holds also for covering all edges of the complete bipartite graph KN,N by two such graphs G′1 and G′2-this clearly follows by splitting the vertices of K2N arbitrarily into two equal classes and by deﬁning G′i, for i = 1,2, to be the graph obtained from Gi by keeping only the edges that have one endpoint in each class.

# 3 Limits

## 3.1 Triangle Removal Lemma

The connection between the triangle removal lemma and the existence of (r,t)-RS graphs is well known since the work of Ruzsa and Szemere´di, for completeness we include the argument.

- Proposition 3.1. If there exists an (r,t)-RS graph on N vertices, then there exists a graph on N + t vertices with at least 3rt/2 edges, in which every edge is contained in exactly one triangle. Thus one has to delete at least rt/2 edges to destroy all triangles and yet the graph contains only rt/2 triangles.


Proof: Let G be an (r,t)-RS graph on N vertices. Then its number of edges is rt and hence, by a well known simple result, it contains a bipartite subgraph G′ = (U,V,E′) with at least rt/2 edges. Clearly, these edges can be covered by t induced matchings M1,M2,...Mt, and we can assume that these matchings are pairwise edge disjoint.

For each matching Mi, add an additional vertex wi and connect wi to the endpoints of all edges in Mi. The resulting graph H = (U,V,W,EH) is tripartite, has N + t vertices and contains |E′| triangles. The critical property of this construction is that each edge of H is in a unique triangle. Indeed, there is a natural set of |E′| triangles in H - each such triangle is speciﬁed by an edge (u,v) ∈ E′ and if this edge is contained in the matching Mi, this edge is mapped to the triangle (u,v,wi) in H. There are in fact no other triangles in H: Let T = (a,b,c) be a triangle in H. Since H is tripartite, there must be exactly one vertex from each set U,V and W in the set a,b,c. Suppose that a ∈ U and b ∈ V . Then let Mi be the unique matching containing the edge (a,b). Suppose c = wj = wi. This implies that the matching Mj covers both vertices a and b but does not contain the edge (a,b), and hence Mj is not an induced matching, contradiction. This completes the proof.

The triangle removal lemma of [21], which is one of the early major applications of the regularity lemma, asserts that for any ǫ > 0 there is a δ = δ(ǫ) > 0 so that for N > N(ǫ) any graph on N vertices from which one has to delete at least ǫN2 edges to destroy all triangles contains at least δN3 triangles. This and the above proposition implies that there are no (r,t)-RS graphs on N vertices with r = Ω(N) and t = Ω(N). The original proof of [21] provides a rather poor quantitative relation between ǫ and δ, but the improved recent proof of Fox [15] supplies better estimates (which are still very far from the known constructions). If the number of vertices is N and the graph is a pairwise disjoint union of t induced matching, each of size r = cN, then t is at most N/log(x) N, with x = O(log(1/c)), where log(x) N denotes the x-fold iterated logarithm. For more details, see [15].

## 3.2 Reconstruction Principle

Here we prove lower bounds on the number of edges that a graph must miss, if it can be covered by disjoint induced matchings of size r. These lower bounds establish that the results in Section 2.2 are essentially tight for an important range of the parameters. Indeed, as proved in that section there are graphs on N vertices missing N3/2+ǫ edges that can be covered by disjoint, induced matchings of polynomial size. Yet, as we show below, any graph that can be covered by disjoint, induced matchings of size two or more must miss at least N3/2 edges. We describe two proofs, The ﬁrst is based on entropy considerations, and the second is an elementary combinatorial proof, that in fact yields a somewhat stronger result, as it bounds the minimum degree in the graph of missing edges. We believe, however, that both methods are interesting and each may have further applications. We start with the entropy proof.

Let G = (V,E) be a graph on N vertices that can be covered by disjoint induced matchings

- M1,M2,...Mt each of size r ≥ 2. We will prove an upper bound on the number of edges |E| based on an application of the reconstruction principle (and through information theoretic inequalities).


To this end, we deﬁne a random variable A as follows:

- • Choose Mi uniformly at random
- • Choose an ordered set of two distinct edges e1,e2 from Mi


Set A = (e1,e2). Let e1 = (W,X) and e2 = (Y,Z). Here we use upper-case letters to denote that each of these choices W,X,Y and Z is a random variable and we will use lower case letters to denote speciﬁc choices of these random variables.

- Claim 3.2. H(A) = log |E| + log(r − 1)

Proof: Since we choose each matching Mi uniformly at random, and each matching is of the same size (r), the ﬁrst edge e1 is chosen uniformly at random from the set |E|. Conditioned on the choice of e1, the remaining edge e2 is chosen uniformly at random from the r − 1 other edges in Mi.

Let dv be the number of missing edges incident to v ∈ V . Let Dv be the set of non-neighbors of v, and let fv : Dv → [dv] be a function mapping each non-neighbor of v to a unique integer in the set [dv].

- • Choose A as above and let e1 = (w,x) and e2 = (y,z)
- • Choose S1 with probability 1/2 to be either w or x, and let S3 be the opposite choice
- • Choose S2 with probability 1/2 to be either y or z


We set the random variable B = [s1,fs1(s2),fs2(s3)].

- Lemma 3.3. H(B) ≥ H(A)


Proof: We prove that A can be computed as a deterministic function of B, and then we apply the Chain Rule for entropy to prove the Lemma.

- Claim 3.4. A can be computed as a deterministic function of B


Proof: Given B, we can compute s2 using s1 and fs1(s2), and using s2 and fs2(s3) we can compute s3. This in turn deﬁnes the edge e1 = (s1,s3) which uniquely determines Mi since the set of matchings disjointly covers the edges in G. From Mi and s2, we can compute the remaining edge e2: this is the unique edge incident to s2 in the matching Mi.

The Chain Rule for entropy yields the expansion H(B,A) = H(B)+H(A|B), but H(A|B) = 0 because A is a deterministic function of B. We can alternatively expand H(B,A) as H(A)+H(B|A). Since H(B|A) ≥ 0 we get H(B) = H(B,A) ≥ H(A), as desired.

Next, we give an upper bound for the entropy of B (based on the number of missing edges), and this combined with the Lemma above will imply a contradiction if the number of missing edges is too small.

Deﬁnition 3.5. We will call a random variable S on V degree-uniform if S chooses a random vertex proportional to the degree in G.

- Claim 3.6. S1 and S2 are degree-uniform random variables Note that these two random variables are not independent!


Proof: We can choose the random variable A by choosing an edge uniformly at random from E, setting this edge to be e1 and choosing e2 uniformly at random from the remaining edges in the matching Mi that contains e1. The distribution of S1 in this sampling procedure (for A) is clearly degree-uniform.

To prove the remainder of the Claim, we can slightly modify the sampling procedure for A. We could instead choose an edge uniformly at random from E and set this edge to be e2. Then choose an edge e1 uniformly at random from the other edges in the matching Mi that contains e2. This is an equivalent sampling procedure for generating A, and from this procedure it is clear that S2 is degree-uniform.

Let d¯ be the average degree in the complement of G.

- Lemma 3.7. H(B) ≤ log N + 2log d¯


Proof: We can decompose the random variable B into B1 = s1, B2 = fs1(s2) and B3 = fs2(s3). Again, using the Chain Rule for entropy we obtain that

H(B) = H(B1) + H(B2|B1) + H(B3|B2,B1) Since S2 is a deterministic function of the random variables B2 and B1, we get

H(B3|B2,B1) = H(B3|B2,B1,S2) ≤ H(B3|S2) We can upper bound H(B1) by log N, and H(B2|B1) =

Pr[S1 = s1]log ds1

Pr[S1 = s1]H(B2|S1 = s1) ≤

s1

s1

Using Claim 3.6, this is

H(B2|B1) =

s1

N − 1 − ds1 2|E|

log ds1 ≤

![image 39](<2011-alon-nearly-complete-graphs-decomposable_images/imageFile39.png>)

s1

N − 1 − d¯ 2|E|

log d¯= log d,¯

![image 40](<2011-alon-nearly-complete-graphs-decomposable_images/imageFile40.png>)

where here we have used Jensen’s Inequality and the concavity of the functions log x and −xlog x. An identical bound holds also for H(B3|S2) again using Claim 3.6 and thus we get H(B) ≤ log N + 2log d¯.

We can apply Lemma 3.3 and the bounds in Lemma 3.7 and Claim 3.2 to obtain the following theorem:

- Theorem 3.8. Let G = (V,E) be a graph on N vertices that can be covered by disjoint induced


- matchings of size r ≥ 2. Then the number of missing edges satisﬁes

N 2 − |E| ≥ (

- 1

![image 41](<2011-alon-nearly-complete-graphs-decomposable_images/imageFile41.png>)

- 2√2 − o(1))r1/2N3/2.


![image 42](<2011-alon-nearly-complete-graphs-decomposable_images/imageFile42.png>)

We can apply a nearly identical argument in the case in which G is a bipartite graph: Theorem 3.9. Let G = (U,V,E) be a bipartite graph that can be covered by disjoint induced

- matchings of size r ≥ 3. Then the number of missing edges satisﬁes |U| × |V | − |E| ≥ Ω(r2/3|U|2/3|V |2/3).


To prove this result, we choose A′ to be three distinct edges from the matching Mi, and we use a length three path through pairs in U × V that are not in E to deﬁne the corresponding random variable B′. Again, the proof uses information theoretic inequalities and the fact that (if appropriately deﬁned) A′ can be reconstructed as a deterministic function of B′. It is worth noting that for a bipartite graph with |U| = |V | = N and induced matchings of size 2, there is a simple construction missing only N edges.

We can also give a direct counting argument, which is somewhat stronger, as it yields a lower bound on the minimum degree in the graph of missing edges. This counting argument proceeds by estimating the size of an appropriately deﬁned set in two ways. Let G = (V,E) be an edge disjoint union of induced matchings M1,M2,...Mt each of size r. Again, let dv be the degree of v in the complement of G.

Set

F = {(v,e)|v ∈ V,e ∈ E,v ∈/ e,∃Mi s.t. e ∈ Mi and v is covered by Mi}

- Lemma 3.10. |F| ≤ v min d2v ,(N − 1 − dv)(r − 1)


Proof: For each v ∈ V , v appears in precisely (N − 1 − dv)(r − 1) elements of F since v belongs to exactly (N − 1 − dv) matchings and for each such matching there are exactly r − 1 choices of an edge (in the matching) that is not incident to v.

Alternatively, each v ∈ V also appears in at most d2v elements of F: if (v,e) ∈ F then v must

not be a neighbor of each endpoint of e because the matching is induced. As there are at most d2v choices of pairs of vertices that are not neighbors of v, the desired result follows.

We can also compute the size of F exactly: Lemma 3.11. |F| = v(r − 1)(N − 1 − dv)

Proof: For each edge e ∈ E, let Mi be the corresponding matching that covers e. There are exactly 2(r − 1) choices for a vertex (covered by Mi) but not incident to e. Hence each edge e appears in exactly 2(r − 1) elements of F. Thus

N 2 −

- 1

![image 43](<2011-alon-nearly-complete-graphs-decomposable_images/imageFile43.png>)

- 2 v


dv =

(r − 1)(N − 1 − dv)

dv = (r − 1) N(N − 1) −

|F| = 2(r − 1)

v

v

Combining the two estimates for |F| we conclude that

dv 2

(r − 1)(N − 1 − dv) ≤

min

,(N − 1 − dv)(r − 1) .

v

v

It follows that for every v, the minimum term in the right hand side should be (N −1 −dv)(r −1), since otherwise the inequality cannot hold. Therefore we have proved the following, which implies

- Theorem 3.8.


- Theorem 3.12. If G = (V,E) is a graph on N vertices that is the disjoint union of induced matchings of size r, then the minimum degree d in the complement of G satisﬁes


d 2 ≥ (r − 1)(N − 1 − d).

The assertion of Theorem 3.9 can be also proved by a counting argument. We omit the details.

# 4 Applications

## 4.1 Shared Communication Channels

We apply our results to signiﬁcantly improve the application in [10] of communicating over a shared directional multichannel. Roughly, when communicating over a shared channel we want the edges (corresponding to messages sent in some time step called a round) to form an induced matching. Otherwise, a receiver will hear messages sent from two diﬀerent sources and the messages will appear garbled. Birk, Linial and Meshulam construct graphs with positive density that can be covered by roughly 24N2r induced matchings where r = (log N)Ω(log logN/(log log logN)2). The authors then use these graphs to design a communication protocol for N stations over a shared directional multi-channel where the round complexity of this protocol is O(Nr2). This is a slightly better than poly-logarithmic improvement over the naive protocol for bus-based architectures.

![image 44](<2011-alon-nearly-complete-graphs-decomposable_images/imageFile44.png>)

![image 45](<2011-alon-nearly-complete-graphs-decomposable_images/imageFile45.png>)

We can use our constructions to achieve a round complexity of O(N2−δ) over a shared directional multi-channel. This is the ﬁrst such protocol that provides a polynomial improvement over the naive protocol. We accomplish this using just one transmitter and two receivers per station. This corresponds to a partition of the edges of a complete bipartite graph into two graphs each of which can be decomposed into a small number of induced matchings. If we allow C = C(ǫ) receivers per station, we can achieve a round complexity that is O(N1+ǫ) for any ǫ > 0 (here N is a trivial lower bound). Hence, while previous protocols required a nearly quadratic number of rounds with a constant number of receivers per station, our protocols require only a nearly-linear number of rounds.

Motivated by the application to communication over a shared channel, Meshulam [20] conjectured that any graph on N vertices with positive density cannot be covered by O(N2−δ) induced matchings. The constructions presented in Section 2.1 and in Section 2.2 disprove this conjecture in a strong sense.

First we explain the model considered in [10]. Roughly, the goal is to design a good communication protocol using a small number of shared communication channels. More precisely, suppose we have N stations, and each wants to send a (distinct) message to every other station. We further assume that each message is (roughly) the same size. In this context, it is often prohibitively expensive to build a point-to-point communication channel from each station to every other one.

Often, the proposed solution is to use some form of a shared communication channel. Indeed, the standard bus-based architecture connects all pairs of stations using a single connection in such a way that only one message can be sent on the channel per time step and hence a total of N2 rounds are needed to send all messages.

There are other architectures that can be implemented cheaply in hardware and can accomplish this task in a smaller number of rounds. One such architecture is the shared directional multichannel. The combinatorial abstraction is that we imagine the communication graph as a complete bipartite graph KN,N (with N vertices on the left, representing the transmitters of the stations, and N vertices on the right, representing the receivers). A directed multi-channel allows us to partition KN,N into C graphs G1,G2,...GC. These graphs correspond to allocating c receivers to each station. For each graph Gi, in each round we can exchange all messages corresponding to the edges in some induced matching in Gi in one time step. These matchings are required to be induced because otherwise messages would interfere in the underlying hardware.

Thus the problem of designing a communication protocol for this architecture that completes in a small number of rounds and does not use too many transmitters and receivers per station is exactly the problem of covering all the edges of a complete bipartite graph (using at most C graphs) so that the number of induced matchings needed to cover the edges in each graph is small. The number C represents the number of receivers that each station must be equipped with, assuming it has only one transmitter, and so our goal is not only to minimize the number of rounds, but also to do so for a small value of C.

- • For C = 2, we give a protocol that completes in O(N2−δ) rounds for δ > 0.058 and
- • For any ǫ > 0, we show that there is a C = C(ǫ) = 2O(1ǫ) so that there is a communication protocol that completes in O(N1+ǫ) rounds


![image 46](<2011-alon-nearly-complete-graphs-decomposable_images/imageFile46.png>)

Let KN,N be the complete bipartite graph with N vertices on the left and N on the right.

- Theorem 4.1. There is a partition of the edges of KN,N into two graphs G1 and G2 so that each of these graphs can be covered by at most O(N2−δ) induced matchings, for δ > 0.058.


Proof: This follows immediately from the construction given at the very end of Section 2.2: we can choose G′1 and G′2 that cover all edges of KN,N, where G′1 covers all edges of KN,N but at most N2−δ and yet it is a union of at most N2−δ induced matchings. The second graph G′2 consists of all these remaining edges. Since it contains at most N2−δ edges in total we can cover G′2 by trivial induced matchings – one for each edge in G′2. The total number of induced matchings in each graph is thus at most O(N2−δ).

- Theorem 4.2. For any ǫ > 0, there is a C = C(ǫ) = 2O(1ǫ) so that the edges of KN,N can be partitioned into G1,G2,..GC and each of these graphs can be covered by at most O(N1+ǫ) induced matchings.


![image 47](<2011-alon-nearly-complete-graphs-decomposable_images/imageFile47.png>)

Proof: To obtain this theorem, we can instead invoke the construction in Section 2.1 to obtain a bipartite graph G (obtained by splitting the vertices of the graph constructed in that section into two equal parts and by keeping all edges that join vertices in the two parts). For each i, we can take Gi to be a random shift of G - i.e. we construct Gi by permuting the labels of the vertices on the right randomly. G is missing less than N2−δ edges, for δ = 2−O(1ǫ), and hence if we take C = 2/δ random shifts the expected number of edges that are not covered in any Gi is less than one. Hence there is some choice of G1,G2,...GC that covers the edges in the complete bipartite graph and yet the edges in each Gi can be covered by at most O(N1+ǫ) induced matchings. We

![image 48](<2011-alon-nearly-complete-graphs-decomposable_images/imageFile48.png>)

note that the above proof can be derandomized using the method of conditional expectations, that is, the graphs Gi can be generated eﬃciently and deterministically.

Finally we mention a simple lower bound for the number of rounds needed, proved by Meshulam [20]. This shows that for any constant number of receivers a super-linear number of rounds is needed:

- Proposition 4.3 ([20]). For any partition of the edges of KN,N into G1,G2,...GC, the total number of induced matchings needed to cover G1,G2,...GC is at least b(C)N1+1/(2C−1).


Proof: We apply induction on C, the result for C = 1 is trivial. Consider the case C = 2. Without loss of generality, let G1 contain at least half of the edges from the complete bipartite graph and suppose that the minimum number of induced matchings needed to cover G1 is Nr. Then there is an induced matching (in this set) that contains at least 12N2−r edges and hence G2 contains a complete bipartite graph where the number of vertices on the left and on the right is at least 1 4N2−r. Hence the number of induced matchings needed to cover G2 is at least 161 N4−2r. Since the quantity max(Nr,N4−2r) is minimized for r = 4/3 the total number of induced matchings needed to cover G1 and G2 is at least Ω(N4/3).

![image 49](<2011-alon-nearly-complete-graphs-decomposable_images/imageFile49.png>)

![image 50](<2011-alon-nearly-complete-graphs-decomposable_images/imageFile50.png>)

![image 51](<2011-alon-nearly-complete-graphs-decomposable_images/imageFile51.png>)

We can iterate the above argument in the general case. Without loss of generality let G1

contain at least C1 N2 edges and suppose the minimum number of induced matchings needed to cover G1 is Nr. Then the union of G2,G3,...GC contains a complete bipartite graph where the

![image 52](<2011-alon-nearly-complete-graphs-decomposable_images/imageFile52.png>)

number of vertices on the left and on the right is at least 21C N2−r. We can assume by induction that the total number of induced matchings needed to cover G2,G3,...GC is at least some b′(C)N(2−r)(1+1/(2C−1−1)). The quantity

![image 53](<2011-alon-nearly-complete-graphs-decomposable_images/imageFile53.png>)

2C−1 2C−1 − 1

)

max(r,(2 − r) ×

![image 54](<2011-alon-nearly-complete-graphs-decomposable_images/imageFile54.png>)

is minimized for r = 2C2C−1 and this completes the proof.

![image 55](<2011-alon-nearly-complete-graphs-decomposable_images/imageFile55.png>)

Hence any protocol requires at least Ω(log 1ǫ) receivers per station to reduce the number of rounds to O(N1+ǫ). In contrast, the protocol in Theorem 4.2 uses 2O(1ǫ) receivers per station to complete this same task in O(N1+ǫ) rounds.

![image 56](<2011-alon-nearly-complete-graphs-decomposable_images/imageFile56.png>)

![image 57](<2011-alon-nearly-complete-graphs-decomposable_images/imageFile57.png>)

## 4.2 Linearity Testing

Here we observe that our graphs can be plugged in the analysis of Ha˚stad and Wigderson [19] of the graph test of Samorodnitsky and Trevisan [22] to provide a (modest) strengthening. We obtain slightly better bounds on the soundness of this test, which may be of interest for a particular range of the parameters.

The classical linearity test of Blum, Luby and Rubinfeld chooses a pair of points x and y uniformly at random from the domain of a function, and checks if f(x)+f(y) = f(x+y). The test accepts f if and only if this condition is met, and indeed this test always accepts a linear function and if f is not linear, the probability that this test accepts f can be bounded by 21 + d(2f), where d(f) is the maximum correlation of f with a linear function [11].

![image 58](<2011-alon-nearly-complete-graphs-decomposable_images/imageFile58.png>)

![image 59](<2011-alon-nearly-complete-graphs-decomposable_images/imageFile59.png>)

What if we want to reduce the probability that a function f that is not linear passes this test? We could perform r independent trials, in which case the probability that f is accepted is bounded by 2 1 + d(2f)

r

. However such a test queries the function f on 3r locations. Motivated by the problem of designing a PCP with optimal amortized query complexity and the related problem for linearity testing, Samorodnitsky and Trevisan introduced a graph-based linearity test: Associate

![image 60](<2011-alon-nearly-complete-graphs-decomposable_images/imageFile60.png>)

![image 61](<2011-alon-nearly-complete-graphs-decomposable_images/imageFile61.png>)

each vertex in an r-vertex complete graph with a randomly chosen element from the domain of f, and for each edge check if f(x) +f(y) = f(x + y) where x and y are the values associated with the endpoints of the edge. This test accepts if and only if all of these conditions are met.

This test queries the function f on r + 2 r locations and the hope is that the soundness should

behave approximately like 2 r independent trials of the original linearity test [11]. Samorodnitsky and Trevisan [22] showed that the soundness of this test is bounded by

- 1

![image 62](<2011-alon-nearly-complete-graphs-decomposable_images/imageFile62.png>)

- 2


(r2)

+ d(f).

This analysis was subsequently simpliﬁed and improved by H˚astad and Wigderson [19] - using the known existence of graphs that have many edges but can be covered by large (disjoint) induced matchings. The intuition behind this connection is that an induced matching corresponds to independent trials of the original Blum-Luby-Rubinfeld linearity test (althoug the formal analysis somewhat masks this intuition). Ha˚stad and Wigderson [19] proved:

- Theorem 4.4. If G = (V,E) is an (r,t)-RS graph, then the graph-test for G accepts a function f with probability at most


e−rt/8 + d(f)r/4.

Ha˚stad and Wigderson [19] used the construction of Ruzsa and Szemere´di [21] mentioned in the introduction, which shows that there are (r,t)-RS graphs on N vertices with r = eO( N

√logN) and t = N/3.

![image 63](<2011-alon-nearly-complete-graphs-decomposable_images/imageFile63.png>)

![image 64](<2011-alon-nearly-complete-graphs-decomposable_images/imageFile64.png>)

We can plug our constructions directly into this theorem to obtain slightly better bounds, for some special values of d(f). Our constructions are dense, and hence improve the ﬁrst term in the bound, but the second term is slightly worse (although we still have r = N1−o(1)). In general, the obtained bounds will be better than either of those in [22] or [19] for some values of d(f). Note that as the complete graph on N vertices contains every graph on N vertices, these bounds, like the ones of [22] and [19], provide an upper estimate for the probability that the complete graph linearity test on N vertices accepts a function f, showing that it is at most

′(1) ).

min( 2−(N2) + d(f),2−N2−o(1) + d(f)N1−o(1),2−Ω(N2) + d(f)N1−o

The ﬁrst term in the minimum is the bound of [22], the second is that of [19], and the third (in which the o′(1) term is a bit worse than the one in the second) follows from our graphs.

## 4.3 The Directed Steiner Tree Problem

In this short subsection we brieﬂy note the connection between our constructions and a candidate randomized rounding algorithm for the directed Steiner tree problem that motivated Vempala [25] to ask about the existence of certain (r,t)-RS graphs.

Giving a poly-logarithmic approximation algorithm for the directed Steiner tree problem is a famous open problem in approximation algorithms. A special case is the group Steiner tree problem (in an undirected graph), for which Garg, Konjevod and Ravi gave an elegant, poly-logarithmic approximation algorithm [18]. Charikar et al [12] give an approximation algorithm for the directed Steiner tree problem whose approximation guarantee is O˜(Nǫ) for any ǫ > 0, and this guarantee can be made poly-logarithmic at the cost of running in quasi-polynomial time.

Even our understanding of the naive linear programming relaxation is quite weak. Zosin and Khuller [26] give a Ω(

√

![image 65](<2011-alon-nearly-complete-graphs-decomposable_images/imageFile65.png>)

k) integrality gap (where k is the number of terminals), but this construction

has exponentially many (in k) vertices. Hence we could still hope that the naive relaxation has at most a poly-logarithmic (in N) integrality gap.

Rajaraman and Vempala considered a stronger relaxation and a candidate rounding algorithm. In the case in which the support of the solution to the linear program is a tree, they proved that their rounding algorithm achieves a poly-logarithmic approximation ratio and this analysis is reminiscent of the rounding procedure for the group Steiner tree problem [18].

However, even when ﬂow merges in one layer of a layered graph (i.e. when the fractional solution is not supported on a tree), attempting to analyze the behavior of the rounding algorithm led Vempala to a combinatorial conjecture:

Conjecture 1. [25] Let G = (U,V,E) be an N × k complete bipartite graph and N ≥ k. Let P be a partition of the edge set and for a part p ∈ P, let pi denote the degree of vertex i in p (i.e. the number of edges of p incident to i). Then

pipj |p|

min 1,

![image 66](<2011-alon-nearly-complete-graphs-decomposable_images/imageFile66.png>)

i∈U,j∈V

p∈P

Nk log N

≥ C

.

![image 67](<2011-alon-nearly-complete-graphs-decomposable_images/imageFile67.png>)

Our constructions yield a negative answer to the above conjecture. In our negative example we have N = k. To obtain this result, we can instead invoke the construction in Section 2.2 to obtain a bipartite graph H (obtained by duplicating the vertices of the graph constructed in that section). We can take P to be the induced matchings covering H and additionally we add a part in the partition (consisting of a single edge) for each edge across the bipartition missing from H.

We can upper bound the right hand side as:

pipj |p|

min 1,

![image 68](<2011-alon-nearly-complete-graphs-decomposable_images/imageFile68.png>)

i∈U,j∈V

p∈P

pipj |p|

≤

![image 69](<2011-alon-nearly-complete-graphs-decomposable_images/imageFile69.png>)

(i,j)∈H p∈P

+

1

(i,j)∈/H

H is an (r,t)-RS graph (and r = Ω(N2−f) in our construction) and so for each part p we have

pipj

|p| = 1 because p is an induced matching with respect to H. The number of parts in the partition (ignoring singletons, which are not in H anyways) is at most O(Nf) and so we can bound the contribution of the ﬁrst term by O(Nf). Also, the number of edges that H is missing (across the bipartition) is at most O(Ne) and hence we can bound the above sum by O(Ne + Nf) for e and f as in Theorem 2.21 (recall that N = k). Since we can have both e and f at most 1.942 it follows that the conjecture is false.

![image 70](<2011-alon-nearly-complete-graphs-decomposable_images/imageFile70.png>)

(i,j)∈H

# 5 Concluding Remarks and Open Questions

We have given two constructions of nearly complete graphs that can be decomposed into large pairwise edge disjoint induced matchings and described several applications of these graphs.

The main combinatorial open problem that remains is to determine or estimate more precisely the set of all pairs (r,t) so that there are (r,t)-RS graphs on N vertices. This is interesting for most values of the parameters, but is of special interest in some speciﬁc range. In particular, if for r = (logNN)g with g > 1, one can show that t = o(N), this will improve the best known upper bound for the maximum possible cardinality of a subset of {1,2,... ,N} with no 3-term arithmetic progressions-a problem that received a considerable amount of attention over the years (see [23] and its references).

![image 71](<2011-alon-nearly-complete-graphs-decomposable_images/imageFile71.png>)

The study of the combinatorial problem above seems to require a variety of techniques: the known constructions of [21], [14], [20] and the ones given here apply tools from Additive Number

Theory, Coding Theory, low degree representations of Boolean functions and Geometry, while the proofs of non-existence rely on the regularity lemma and on combinatorial and entropy based techniques. All of these, however, still leave a wide gap between the upper and lower bounds for at least some of the range, and it will be interesting to ﬁnd additional ideas that will help to study this problem.

In all the applications considered here there are still remaining open problems. The communication protocols over a shared directional multi-channel we suggest, while improving substantially the existing ones, are still not optimal, and the problem of deciding the best possible number of rounds for N stations, even with two receivers per station, is still not settled, although our results show that it is N2−δ for some δ between 0.058 and 2/3. The best possible upper bound for the probability of acceptance of a function f in the linearity graph test, using a complete graph of size

- N, is also not precisely determined as a function of N and d(f) (although here the gap between the upper bounds and the lower bounds is not large-see [19].) Finally, it will be interesting to decide if our graphs can be helpful in establishing new integrality gap results for the natural relaxation of the directed Steiner tree problem, rather than merely estimating the performance of speciﬁc rounding schemes. Acknowledgment We thank Roy Meshulam and Santosh Vempala for helpful comments.


# References

- [1] N. Alon. Testing subgraphs in large graphs. Proc. 42nd IEEE FOCS, IEEE (2001), 434–441. Also: Random Structures and Algorithms 21 (2002), 359–370. 1.1
- [2] N. Alon and J. Fox. Testing perfection is hard. To appear. 1.1
- [3] N. Alon and A. Shapira. Testing subgraphs in directed graphs. Proc. of the 35th ACM STOC, ACM Press (2003), 700–709. Also: JCSS 69 (2004), 354–382. 1.1
- [4] N. Alon and A. Shapira. A characterization of easily testable induced subgraphs. Proc. of the Fifteenth Annual ACM-SIAM SODA (2004), 935-944. Also: Combinatorics, Probability and Computing 15 (2006), 791-805. 1.1
- [5] N. Alon and A. Shapira. On an Extremal Hypergraph Problem of Brown, Erd˝os and So´s. Combinatorica 26 (2006), 627–645. 1.1
- [6] David A. Mix Barrington, Richard Beigel and Steven Rudich. Representing Boolean Functions as Polynomials Modulo Composite Numbers. Computational Complexity 4: 367–382 (1994). 1.1
- [7] F. A. Behrend. On sets of integers which contain no three terms in arithmetic progression. Proc. National Academy of Sciences USA 32 (1946), 331–332. 1.1
- [8] W. G. Brown, P. Erd˝os and V.T. So´s. Some extremal problems on r-graphs. in: New Directions in the Theory of Graphs, Proc. 3rd Ann Arbor Conference on Graph Theorey, Academic Press, New York, 1973, 55–63. 1.1
- [9] W. G. Brown, P. Erd˝os and V.T. So´s. On the existence of triangulated spheres in 3-graphs and related problems. Periodica Mathematica Hungaria 3 (1973), 221–228. 1.1
- [10] Y. Birk, N. Linial and R. Meshulam. On the Uniform-traﬃc Capacity of Single-hop Interconnections Employing Shared Directional Multichannels. IEEE Transactions on Information Theory, pp. 186–191, 1993. 1.1, 1.2, 2.2, 4.1
- [11] M. Blum, M. Luby and R. Rubinfeld. Self-testing/correcting with applications to numerical problems. Journal of Computer and Science Systems, pp. 549–595, 1993. 4.2
- [12] M. Charikar, C. Chekuri, T-Y. Cheung, Z. Dai, A. Goel, S. Guha and M. Li. Approximation algorithms for directed Steiner problems. Journal of Algorithms, pp. 73–91, 1999. 4.3
- [13] P. Erd˝os, P. Frankl and V. Ro¨dl. The asymptotic number of graphs not containing a ﬁxed subgraph and a problem for hypergraphs having no exponent. Graphs Combin. 2 (1986) 113–

121. 1.1

- [14] E. Fischer, I. Newman, S. Raskhodnikova, R. Rubinfeld and A. Samorodnitsky. Monotonicity Testing over General Poset Domains. Symposium on Theory of Computing, pp. 474–483, 2002. 1.1, 5
- [15] J. Fox. A New Proof of the Graph Removal Lemma. Annals of Mathematics, pp. 561–579,

2011. 3.1

- [16] J. Fox and P. Loh. On a Problem of Erd˝os and Rothschild on Edges in Triangles. Combinatorica, to appear. 1.2, 2.1


- [17] P. Frankl and Z. Fu¨redi. Colored packing of sets in combinatorial desgin theory. Annals of Discrete Math. 34 (1987), 165–178. 1.2
- [18] N. Garg, G. Konjevod and R. Ravi. A polylogarithmic approximation algorithm for the group Steiner tree problem. Journal of Algorithms, pp. 66–84, 2000. 4.3
- [19] J. Ha˚stad and A. Wigderson. Simple Analysis of Graph Tests for Linearity and PCP. Random Structures and Algorithms, pp. 139–160, 2003. 1.1, 1.2, 4.2, 4.2, 5
- [20] R. Meshulam. Private communication, 2011. 1.1, 1.2, 4.1, 4.1, 4.3, 5
- [21] I. Rusz´a and E. Szemere´di. Triple Systems with no Six Points Carrying Three Triangles. Colloquia Mathematica Societatis J´anos Bolyai, pp. 939–945, 1978. 1.1, 3.1, 4.2, 5
- [22] A. Samorodnitsky and L. Trevisan. A PCP Characterization of NP with Optimal Amortized Query Complexity. Symposium on Theory of Computing, pp. 191–199, 2000. 1.1, 4.2, 4.2
- [23] T. Sanders. On Roth’s Theorem on Progressions. Annals of Mathematics 174, (2011), 619-636. 5
- [24] E. Szemere´di. Regular partitions of graphs. In: Proc. Colloque Inter. CNRS (J. C. Bermond, J. C. Fournier, M. Las Vergnas and D. Sotteau, eds.), 1978, 399–401. 1.1
- [25] S. Vempala. Private communication, 2011. 1.2, 4.3, 1
- [26] L. Zosin and S. Khuller. On directed Steiner trees. SODA, pp. 59–63, 2002. 4.3


