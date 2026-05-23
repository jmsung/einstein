arXiv:1611.02099v2[math.CO]22Dec2016

Hereditary quasirandomness without regularity

David Conlon∗ Jacob Fox† Benny Sudakov‡

Abstract

A result of Simonovits and So´s states that for any ﬁxed graph H and any ǫ > 0 there exists δ > 0 such that if G is an n-vertex graph with the property that every S ⊆ V (G) contains pe(H)|S|v(H) ±δnv(H) labeled copies of H, then G is quasirandom in the sense that every S ⊆ V (G) contains 12p|S|2 ± ǫn2 edges. The original proof of this result makes heavy use of the regularity lemma, resulting in a bound on δ−1 which is a tower of twos of height polynomial in ǫ−1. We give an alternative proof of this theorem which avoids the regularity lemma and shows that δ may be taken to be linear in ǫ when H is a clique and polynomial in ǫ for general H. This answers a problem raised by Simonovits and So´s.

![image 1](<2016-conlon-hereditary-quasirandomness-without-regularity_images/imageFile1.png>)

# 1 Introduction

What does it mean to say that a graph is random-like and how does one construct such graphs? Attempts to answer these questions have played a central role in mathematics over the last forty years, with connections to combinatorics, probability, number theory, theoretical computer science and more (see, for example, [8, 12]).

For dense graphs, there is a somewhat surprising answer to the ﬁrst question, in that many of the possible deﬁnitions for what it means to be random-like turn out to be equivalent, a fact ﬁrst observed by Chung, Graham and Wilson [1], building on earlier work of Thomason [24, 25]. To be more precise, let H be a ﬁxed graph with r vertices and m edges, 0 < p < 1 a ﬁxed constant and G an n-vertex graph. Consider the following properties that G might have:

PH,p(ǫ): The number of labeled copies of H in G is within ǫnr of pmnr. PH,p∗ (ǫ): For every subset S ⊆ V (G), the number of labeled copies of H in the induced subgraph

G[S] is within ǫnr of pm|S|r.

The property PH,p asks that the number of copies of H in G is close to what one would expect in the binomial random graph G(n,p), while the hereditary property PH,p∗ asks for a more robust version of this condition, saying that the copies of H are also uniformly distributed in G, again just as one would expect in G(n,p).

![image 2](<2016-conlon-hereditary-quasirandomness-without-regularity_images/imageFile2.png>)

∗Mathematical Institute, Oxford OX2 6GG, United Kingdom. Email: david.conlon@maths.ox.ac.uk. Research supported by a Royal Society University Research Fellowship and by ERC Starting Grant 676632.

†Department of Mathematics, Stanford University, Stanford, CA 94305. Email: jacobfox@stanford.edu. Research supported by a Packard Fellowship, by NSF Career Award DMS-1352121 and by an Alfred P. Sloan Fellowship.

‡Department of Mathematics, ETH, 8092 Zurich, Switzerland. Email: benjamin.sudakov@math.ethz.ch. Research supported by SNSF grant 200021-149111.

A sequence of graphs (Gn)∞n=1 with |Gn| = n is said to be p-quasirandom if it satisﬁes the property P2∗,p(ǫ) with ǫ = o(1), where, here and throughout the paper, we write Pr,p and Pr,p∗ for PH,p and PH,p∗ when H is the complete graph Kr. That is, a sequence of graphs is p-quasirandom if the density of Gn is asymptotic to p and the edges are uniformly distributed across subsets. Of the equivalent formulations discovered by Chung, Graham and Wilson [1], the most striking is perhaps the following.

Theorem (Chung–Graham–Wilson). For any ǫ > 0, there exists δ > 0 such that

- (a) if a graph satisﬁes P2,p(δ) and PC4,p(δ), then it also satisﬁes P2∗,p(ǫ);
- (b) if a graph satisﬁes P2∗,p(δ), then it also satisﬁes P2,p(ǫ) and PC4,p(ǫ).


It follows from part (a) that if the number of edges and the number of cycles of length four in a sequence of graphs (Gn)∞n=1 are both asymptotic to their expected values in the random graph G(n,p), then the sequence is p-quasirandom. What is striking about this conclusion is that a purely global property, that of having certain counts of edges and cycles of length four, is suﬃcient to imply a local property about the distribution of edges on small subsets. Moreover, by part (b), the converse also holds.

- A similar result is conjectured [4, 21] to hold when C4 is replaced by any bipartite graph H with at least one cycle. Known as the forcing conjecture, this conclusion is now known to hold for a wide range of bipartite graphs, with progress on the conjecture closely paralleling recent progress [4, 5, 11, 14, 22]


on Sidorenko’s conjecture. On the other hand, part (a) does not hold when C4 is replaced by a nonbipartite H. To see this for triangles, consider the graph G on n vertices consisting of four disjoint sets V1,V2,V3 and V4, each of order n/4, with V1 and V2 complete, V3 and V4 empty, a complete bipartite graph between V3 and V4 and a random bipartite graph with edge probability 1/2 between V1 ∪V2 and V3 ∪ V4. This graph has density 1/2 and asymptotically n3/8 labeled triangles. However, it is clearly not 1/2-quasirandom.

- A key result about quasirandom graphs, proved by Simonovits and So´s [20], says that such counterexamples can be avoided if we strengthen our assumption, asking that G satisﬁes the hereditary property


PH,p∗ rather than just PH,p. That is, a sequence of graphs (Gn)∞n=1 with |Gn| = n is p-quasirandom if every subset S ⊆ V (Gn) contains roughly the same number of copies of H as one would expect to ﬁnd in G(n,p).

Theorem (Simonovits–S´s). For any ǫ > 0, there exists δ > 0 such that if a graph satisﬁes PH,p∗ (δ), then it also satisﬁes P2∗,p(ǫ).

The original proof of this result makes heavy use of the regularity lemma [23], resulting in a bound on δ−1 which is a tower of twos of height polynomial in ǫ−1. The main aim of this paper is to give an alternative proof of this theorem which avoids the use of the regularity lemma, giving a much better bound for δ in terms of ǫ. This answers a problem raised by Simonovits and So´s in their paper. In reality, we prove two theorems, the ﬁrst showing that δ may be taken to be linear in ǫ when H is a clique, a result which is clearly optimal (consider the random graph with density p + ǫ), and the second showing that δ may be taken to be polynomial in ǫ for general H.

- Theorem 1.1. For every natural number r ≥ 3, there is a constant c(r) such that if p and ǫ are constants with 0 < ǫ,p < 1 and n is suﬃciently large depending on r, p and ǫ, then any n-vertex graph G that satisﬁes Pr,p∗ (δ) with δ = c(r)p2r2ǫ also satisﬁes P2∗,p(ǫ).


- Theorem 1.2. For every 0 < p < 1 and natural number r ≥ 3, there are constants c = c(p,r) and c′(p,r) such that if H is a graph with r vertices, 0 < ǫ < 1/2 and a graph G satisﬁes PH,p∗ (δ) with δ = c′(p,r)ǫc(p,r), then it also satisﬁes P2∗,p(ǫ).


We note that another alternative proof for a variant of the Simonovits–S´s theorem, also avoiding regularity, was found independently by Reiher and Schacht [18]. However, their result uses slightly stronger assumptions and gives weaker quantitative control than ours. As well as being interesting in its own right, our close attention to quantitative aspects was motivated by the possibility of application in extremal combinatorics. Indeed, the best bounds for a number of well-known theorems in this area, including Ramsey’s theorem [2] and Szemere´di’s theorem [7], rely crucially on the interplay between diﬀerent notions of quasirandomness. Our results bring the Simonovits–S´s theorem into a range where it could also be proﬁtably applied in this manner.

The rest of the paper will be laid out as follows: we study complete graphs in the next section, proving Theorem 1.1; we treat the general case in Section 3, proving Theorem 1.2; and we conclude with some further remarks and open problems in Section 4. For the sake of clarity of presentation, we systematically omit ﬂoor and ceiling signs whenever they are not crucial.

# 2 Complete graphs

- In this section, we prove Theorem 1.1. We will need several lemmas about graphs G that satisfy


- Pr,p∗ (δ), the ﬁrst of which estimates the number of r-cliques with exactly i vertices in one set X and r − i vertices in another set Y . The proof draws on ideas used by Shapira [19] when studying a related problem. Here and throughout this section, we will use big O notation, allowing the hidden constants to depend on the clique size r but not on the edge density p. In keeping with the statement of Theorem 1.1, we will always assume that n is taken suﬃciently large.


- Lemma 2.1. Let G be an n-vertex graph that satisﬁes Pr,p∗ (δ). Then, for all disjoint subsets X,Y of V (G), the number of labeled r-cliques with exactly i vertices in X and r−i vertices in Y deviates from


- i p(r2)|X|i|Y |r−i by at most O(δnr).


r

Proof. Let xi = ri p(r2)|X|i|Y |r−i and let x′i be the number of labeled r-cliques with exactly i vertices in X and r − i vertices in Y . Pick a random subset X′ ⊆ X of order q|X|. The expected number of

labeled cliques of order r in X′ ∪ Y is (up to lower order terms) i qix′i and this deviates from

p(r2)(q|X| + |Y |)r =

i

qip(r2) r i

|X|i|Y |r−i =

i

qixi

by at most O(δnr).

For j = 1,2,... ,r + 1, let qj = j/(r + 1) and let A be the (r + 1) × (r + 1) matrix with aji = qji. The matrix A is not singular, since it is a Vandermonde matrix and the qj are distinct. Let a be a maximum in absolute value entry of A−1, noting that this depends only on r. Let x = (x0,x1,... ,xr) and x′ = (x′0,x′1,... ,x′r). By the above discussion, we know that the coordinates of the vectors z = Ax and z′ = Ax′ diﬀer by at most O(δnr). Since x − x′ = A−1(z − z′), it follows that the coordinates of the vectors x and x′ diﬀer by at most O(r · |a| · δnr) = O(δnr), completing the proof. ✷

We will need a corollary of this lemma saying that for any subset U ⊆ V (G), most u ∈ U are contained in approximately the same number of r-cliques in U. The following deﬁnition helps capture this condition.

Deﬁnition. Given a subset U ⊆ V (G) and a vertex u ∈ U, let cU(u) denote the number of r-cliques in U containing u and discU(u) = cU(u) − p(r2)|U|r−1/(r − 1)! .

- Corollary 2.1. Let G be an n-vertex graph that satisﬁes Pr,p∗ (δ). Then u∈U discU(u) = O(δnr).


Proof. Partition U into two sets U′,U′′ such that U′ is the set of all vertices u ∈ U satisfying cU(u) ≥ p(r2)|U|r−1/(r − 1)!. Then we can write u∈U discU(u) = 1 + 2, where 1 = u∈U′ cU(u) − p(r2)|U|r−1/(r − 1)! and 2 = − u∈U′′ cU(u) − p(r2)|U|r−1/(r − 1)! . Note that 1 can be written as a sum of r terms, each estimating the deviation of i times the number of r-cliques in G[U] with exactly i vertices in U′ and r−i vertices in U′′. By Lemma 2.1, all these terms are bounded by O(δnr) and, therefore, 1 = O(δnr). A similar argument shows that 2 = O(δnr). ✷

Deﬁnition. Given two vertices u,v ∈ V (G), let c(u,v) denote the number of subsets S ⊂ V (G) of order r − 1 such that both {u} ∪ S and {v} ∪ S form an r-clique in G and write

disc(u,v) = c(u,v) − p(r2)dr−1(v)/(r − 1)! , where d(v) is the order of the neighborhood of v. Note that by deﬁnition c(u,v) = c(v,u). Therefore, by the triangle inequality, we have

disc(u,v) + disc(v,u) ≥ p(r2) dr−1(v) − dr−1(u) /(r − 1)!.

Using this inequality, we can prove the following lemma which shows that most pairs of vertices in G have comparable degree.

- Lemma 2.2. Let G be an n-vertex graph that satisﬁes Pr,p∗ (δ). Then


|dr−1(v) − dr−1(u)| = O(p−(r2)δnr+1).

u,v∈V (G)

Proof. By the above discussion, we have that

disc(v,u) =

u v =u

(disc(u,v) + disc(v,u)) ≥ p(r2)

{u,v}

{u,v}

dr−1(v) − dr−1(u) /(r − 1)!.

Therefore, to prove the statement, it is enough to show that v =u disc(v,u) = O(δnr) for each u. Let U be the set of neighbors of u in G and let W be the complement of U. Partition W further into W′,W′′, where W′ is the set of all vertices v such that c(v,u) ≥ p(r2)dr−1(u)/(r − 1)!. Then we can write v =u disc(v,u) = 1 + 2 + 3, where 1 = v∈W′ c(v,u) − p(r2)dr−1(u)/(r − 1)! ,

2 = − v∈W′′ c(v,u) − p(r2)dr−1(u)/(r − 1)! and 3 = v∈U discU(v). The ﬁrst (resp., second) sum estimates the deviation of the number of r-cliques with one vertex in W′ (resp., W′′) and the remaining r − 1 vertices in U. Thus, by Lemma 2.1, it is bounded by O(δnr). The third sum is bounded by O(δnr) by Corollary 2.1. ✷

We also need an elementary inequality, which follows as an easy corollary of the next result. Proposition 2.1. Let a1,... ,an and b1,... ,bn be two sets of n non-negative numbers. Then, for any positive integer s,

bjs−1 ·

|bsj − asi| ≥ n

bsj −

ai.

i,j

j

j

i

Proof. This follows since

i,j

|bsj − asi| =

≥

i,j

|bj − ai||bjs−1 + ··· + ais−1| ≥

i,j

|bj − ai|bjs−1

(bj − ai)bjs−1 = n

i,j

j

bsj −

j

bjs−1 ·

i

ai,

where in both inequalities we used the fact that the ai and bj are non-negative and in the second inequality we also used the reverse triangle inequality |x − y| ≥ |x| − |y|. ✷

- Corollary 2.2. Let a1,... ,an and b1,... ,bn be two sets of n non-negative numbers. Then, for any positive integer s, i,j |bsj − asi| ≥ j bjs−1 · ( j bj − i ai). Proof. Applying Jensen’s inequality twice, ﬁrst with the function xs/(s−1) and then with the function


s/(s−1)

1/(s−1)

xs−1, we obtain that n1 j bsj ≥ n 1 j bjs−1

and n 1 j bjs−1

≥ n1 j bj. Therefore,

![image 3](<2016-conlon-hereditary-quasirandomness-without-regularity_images/imageFile3.png>)

![image 4](<2016-conlon-hereditary-quasirandomness-without-regularity_images/imageFile4.png>)

![image 5](<2016-conlon-hereditary-quasirandomness-without-regularity_images/imageFile5.png>)

![image 6](<2016-conlon-hereditary-quasirandomness-without-regularity_images/imageFile6.png>)

- 1 n j bsj ≥ n1 j bjs−1 · n1 j bj. Together with Proposition 2.1, this proves the corollary. ✷


![image 7](<2016-conlon-hereditary-quasirandomness-without-regularity_images/imageFile7.png>)

![image 8](<2016-conlon-hereditary-quasirandomness-without-regularity_images/imageFile8.png>)

![image 9](<2016-conlon-hereditary-quasirandomness-without-regularity_images/imageFile9.png>)

We now consider a converse to our intended theorem, saying that if a graph satisﬁes P2∗,p(γ), then it also satisﬁes Pr,p∗ (r2γ). Versions of this counting lemma already appear in the literature, for example, in Section 10.5 of Lov´asz’ book on graph limits [16]. However, because this result is central to our estimates and not as well known as it should be, we include the proof.

- Lemma 2.3. If a graph G satisﬁes P2∗,p(γ), then it also satisﬁes Pr,p∗ (r2γ).


Proof. Given S,T ⊆ V (G), write e(S,T) = s∈S,t∈T 1G(s,t), where 1G is the indicator function for edges of G. In particular, when S = T, this counts the number of labeled edges in S. By assumption, e(S,S) = p|S|2 ± γn2 for all S ⊆ V (G). Therefore, using the identity

2e(S,T) = e(S ∪ T,S ∪ T) + e(S ∩ T,S ∩ T) − e(S \ T,S \ T) − e(T \ S,T \ S), we see that e(S,T) = p|S||T| ± 2γn2 for all S,T ⊆ V (G). Rewriting this conclusion, we see that |

(1G(s,t) − p)| ≤ 2γn2

s∈S,t∈T

for all S,T ⊆ V (G). In turn, this implies that for any functions u,v : V (G) → [0,1], |

(1G(x,y) − p)u(x)v(y)| ≤ 2γn2.

x,y∈V (G)

Indeed, since the function we wish to estimate is linear in u(x) and v(y) for each x and y, the value of the function is maximised when u and v take values in {0,1}. In this case, u and v correspond to indicator functions, so the inequality reduces to the previous special case.

For ease of notation, we spell out the rest of the proof for the case of triangles. By telescoping, the deviation between the number of labeled triangles in a set S ⊆ V (G) and its expected value is

(1G(x,y)1G(y,z)1G(z,x) − p3) =

x,y,z∈S

(1G(x,y) − p)1G(y,z)1G(z,x)+

x,y,z∈S

p2(1G(z,x) − p).

p(1G(y,z) − p)1G(z,x) +

x,y,z∈S

x,y,z∈S

Each term on the right-hand side of this equation may be written as a sum over terms of the form

x,y∈V (G)(1G(x,y) − p)u(x)v(y) for some appropriate u and v, thus implying that the deviation we are interested in is at most 6γn3. In general, we will be telescoping over 2 r terms, one for each edge in Kr, so the resulting deviation is 2 r 2γnr ≤ r2γnr, as required. ✷

We will also use some simple ingredients from other papers. The ﬁrst, taken from a paper of Erd˝os, Goldberg, Pach and Spencer [6], says that if an n-vertex graph contains a set which deviates from the expected density, then there is also a set of order n/2 which deviates from this density.

- Lemma 2.4. Let G be an n-vertex graph of density q. If there is a subset S ⊆ V (G) for which

- |e(S) − q |S2| | ≥ D, then there exists a set S′ of order n/2 such that |e(S′) − q |S2′| | ≥ 4 1 + o(1) D.

![image 10](<2016-conlon-hereditary-quasirandomness-without-regularity_images/imageFile10.png>)

We also need a special case of the Kruskal–Katona theorem [10, 13] giving an upper bound for the number of r-cliques in a graph with given density. The result we use is given as Exercise 31b in Chapter 13 of Lov´asz’ problem book [15]. Here the binomial coeﬃcient xr is extended to all real x in the obvious way.

Lemma 2.5. Let r ≥ 3 be an integer and x ≥ r a real number. Then a graph with exactly x2 edges contains at most xr cliques of order r.

Finally, we need the standard Azuma–Hoeﬀding inequality, which we apply in the following form (see Corollary 2.27 in [9]).

Lemma 2.6. Given positive real numbers λ,c1,... ,ck, let f : {0,1}k → R be a function satisfying the following Lipschitz condition: whenever two vectors z,z′ ∈ {0,1}k diﬀer only in the ith coordinate,

- |f(z)−f(z′)| ≤ ci. Then, if X1,... ,Xk are independent random variables, each taking values in {0,1}, the random variable Y = f(X1,... ,Xk) satisﬁes




λ2 2 i c2i

P[|Y − E[Y ]| ≥ λ] ≤ 2exp −

![image 11](<2016-conlon-hereditary-quasirandomness-without-regularity_images/imageFile11.png>)

.

- We are now ready to prove Theorem 1.1. We will do this by showing that if a suﬃciently large graph G satisﬁes Pr,p∗ (δ), then it also satisﬁes P2∗,p(ǫ) with ǫ = O(p−2r2δ).


- Proof of Theorem 1.1: Let G be an n-vertex graph satisfying the assertion of the theorem and let q = e(G)/ n2 be the edge density of G. By the Kruskal–Katona theorem, Lemma 2.5, G contains


O(qr/2nr) labeled r-cliques. Since the number of labeled r-cliques in G is also at least 12p(r2)nr, this implies that q = Ω(pr−1).

![image 12](<2016-conlon-hereditary-quasirandomness-without-regularity_images/imageFile12.png>)

Let γ = cq−(r−2)p−(r2)δ for some constant c which we choose later. If G does not satisfy P2∗,q(γ), then it contains a subset of vertices S such that e(S) deviates from q |S2| by at least γn2. Using Lemma 2.4,

we can assume that S has order n/2, allowing for the possibility that γ may change by a small constant factor.

Let A be a random subset of G, obtained by choosing every vertex independently with probability 1/2. Let X = S ∩A and let Y be a random subset of G\A, obtained by further choosing every vertex with probability 1/2. By linearity, the expected number of vertices in X is n/4 and the expected number of edges in X is e(S)/4. Moreover, both of these quantities are highly concentrated by the Azuma–Hoeﬀding inequality. Indeed, changing the choice for one vertex can change the number of vertices in X by at most one and the number of edges by at most n, so the sum of squares of these changes is at most O(n) for the number of vertices and O(n3) for the number of edges. These are much smaller than the square of the corresponding expectations. Similarly, the expected number of vertices and edges in Y are n/4 and e(G)/16, respectively, and they are also both concentrated. Therefore, we can ﬁnd two disjoint subsets X and Y , each of order n/4 + o(n), such that e(X) = e(S)/4 + o(n2) and e(Y ) = e(G)/16 + o(n2). Thus, by the discussion above, we have e(X) − e(Y ) = Ω(γn2) and we can delete o(n) vertices to make the orders of X and Y equal without changing this inequality.

Let U = X ∪ Y and let H = G[U] be the subgraph of G induced by U. Without loss of generality, we will assume that e(X) ≥ e(Y ). In particular, the edge density in X is at least q. Since x∈X dH(x) =

- 2e(X) + e(X,Y ) and y∈Y dH(y) = 2e(Y ) + e(X,Y ), we have x∈X dH(x) − y∈Y dH(y) = Ω(γn2). Therefore, using Corollary 2.2 (with s = r − 1) and |X| = n/4 + o(n), we deduce that


u,v∈H

dHr−1(u) − dHr−1(v) ≥

≥ |X|

x∈X,y∈Y

x∈X

dHr−2(x)

dHr−1(x) − dHr−1(y) ≥

dH(x) −



x∈X

x∈X

y∈Y

r−2

Ω(γn2) = Ω qr−2γnr+1 .

dH(x)/|X|

dH(y)



For a suﬃciently large constant c (in the deﬁnition of γ), this contradicts Lemma 2.2 and implies that

- G satisﬁes P2∗,q(γ). Finally, by Lemma 2.3, we have that any graph satisfying P2∗,q(γ) also satisﬁes


- Pr,q∗ (r2γ). Therefore, the number of labeled r-cliques in G deviates from q(r2)nr by at most r2γnr. On the other hand, the diﬀerence between (p±ǫ)(r2) and p(r2) has order of magnitude Ω p(r2)−1ǫ . Thus, if q diﬀers from p by ǫ = c′p−(r2)+1γ for suﬃciently large c′, we obtain the wrong count of r-cliques in G,


contradicting Pr,p∗ (δ). Therefore, G must satisfy P2∗,p(ǫ). Since q = Ω(pr−1), ǫ = cc′q−(r−2)p−2(r2)+1δ = O p−2r2δ , completing the proof. ✷

# 3 General graphs

- In this section, we prove Theorem 1.2. We will assume throughout that H does not have isolated vertices, as deleting such a vertex from H simply scales the number of labeled copies in S by a factor of |S| − r + 1. We say that an n-vertex graph G has property QH,p(ǫ) if, for every r disjoint subsets V1,... ,Vr ⊆ V (G),


the number of labeled copies of H with one vertex in each Vi is pmr! ri=1 |Vi| ± ǫnr. In other words, property QH,p(ǫ) says that if we average over all possible permutations π of [r] the number of copies of H with the copy of vertex i in Vπ(i), the result is at most ǫnr/r! from pm ri=1 |Vi|.

For a subset U ⊆ V (G), let NH(U) denote the number of labeled copies of H in G whose vertices lie in U. Let NH(V1,... ,Vr) denote the number of labeled copies of H in G with one vertex in each Vi.

For S ⊆ [r], let US = i∈S Vi. By the inclusion-exclusion principle, we have NH(V1,... ,Vr) =

(−1)r−|S|NH(US).

S⊆[r]

If G has property PH,p∗ (ǫ), it follows that NH(US) is within ǫnr of pm|US|r. Applying this to each of the 2r − 1 choices of S, we get that NH(V1,... ,Vr) is within (2r − 1)ǫnr of pmr! ri=1 |Vi|. Hence, we have the following lemma.

- Lemma 3.1. If G satisﬁes PH,p∗ (ǫ), then it also satisﬁes QH,p((2r − 1)ǫ).

We remark that the property studied by Reiher and Schacht [18] is a variant of QH,p. We say that a graph G on n vertices has property RH,p(ǫ) if for any r disjoint vertex subsets V1,... ,Vr of G and every one-to-one mapping π : V (H) → [r], the number of copies of H where the image of v is in Vπ(v) for each vertex v of H is within ǫnr of pm ri=1 |Vi|. Note that R is a stronger property than Q, since if a graph satisﬁes RH,p(ǫ), then it also satisﬁes QH,p(r!ǫ). It remains an open problem to ﬁnd a simple proof (i.e., without going through the methods developed here or through regularity methods) that shows the other direction, that Q implies R.

We say that a pair (A,B) of vertex subsets of a graph G is lower-(q,ǫ)-regular if, for all A′ ⊆ A and B′ ⊆ B,

e(A′,B′) ≥ q|A′||B′| − ǫ|A||B|.

That is, the density between all pairs of large subsets is at least q, up to an error depending on ǫ. As in the proof of Lemma 2.3, this is equivalent to saying that for all functions u : A → [0,1] and v : B → [0,1],

a∈A,b∈B

1G(a,b)u(a)v(b) ≥ q

a∈A,b∈B

u(a)v(b) − ǫ|A||B|.

Similarly, we say that (A,B) is upper-(q,ǫ)-regular if, for all subsets A′ ⊆ A and B′ ⊆ B, e(A′,B′) ≤ q|A′||B′| + ǫ|A||B|.

We note that if a pair of subsets is both lower-(q,ǫ)-regular and upper-(q,ǫ)-regular, it satisﬁes a notion of regularity introduced by Lov´asz and Szegedy [17] (though equivalent up to a polynomial change in ǫ to the original notion of regularity introduced by Szemere´di [23]).

The following counting lemma gives a lower bound for the number of copies of a graph H between a collection of sets with lower-regular pairs. We omit the proof, which follows by the same telescoping argument used for Lemma 2.3.

- Lemma 3.2. Let H be a graph on vertex set {1,2,... ,r}. Let G be a graph with vertex subsets V1,... ,Vr such that (Vi,Vj) is lower-(pij,ǫ)-regular for each edge (i,j) of H. Then the number of


homomorphisms from H to G with the copy of vertex i in Vi is at least  

pij − e(H)ǫ

r

|Vi|.



i=1

(i,j)∈E(H)

Note that a similar lemma also holds if lower is replaced by upper and − by +. It is also worth noting that we have not insisted that the vertex sets V1,... ,Vr be disjoint. In particular, we may take V1 = ··· = Vr to obtain a non-partite version of the lemma.

The next lemma shows that lower regularity implies upper regularity and vice versa.

- Lemma 3.3. If a pair (A,B) of vertex subsets of a graph is not lower-(d(A,B),ǫ)-regular, then it is also not upper-(d(A,B),ǫ/2)-regular. The same holds if lower and upper are switched.

Proof. By assumption, there are subsets A′ ⊂ A and B′ ⊂ B such that e(A′,B′) − d(A,B)|A′||B′| < −ǫ|A||B|. As

e(A′,B′) + e(A \ A′,B) + e(A′,B \ B′) = e(A,B)

= d(A,B)|A||B|

= d(A,B)|A′||B′| + d(A,B)|A \ A′||B| + d(A,B)|A′||B \ B′|,

it follows that at least one of the pairs (A \ A′,B) and (A′,B \ B′) demonstrates that (A,B) is not upper-(d(A,B),ǫ/2)-regular. The proof when lower and upper are switched is the same. ✷

We also need a simple lemma saying that we can always ﬁnd a pair of subsets of equal size which bear witness to irregularity.

- Lemma 3.4. Suppose (A,B) is a pair of vertex subsets of a graph which is not upper-(q,γ)-regular. Then there are subsets A′ ⊆ A and B′ ⊆ B with |A′| = |B′| and d(A′,B′) ≥ q + γ min{||AA′||, ||BB′||}. The same holds with upper replaced by lower, + by − and the inequality reversed.

![image 13](<2016-conlon-hereditary-quasirandomness-without-regularity_images/imageFile13.png>)

![image 14](<2016-conlon-hereditary-quasirandomness-without-regularity_images/imageFile14.png>)

Proof. As (A,B) is not upper-(q,γ)-regular, there are subsets A0 ⊆ A and B0 ⊆ B such that e(A0,B0) ≥ q|A0||B0| + γ|A||B|. Without loss of generality, we may assume that |A0| ≤ |B0|. Let B′ ⊆ B0 be the subset of |A0| vertices with the most neighbors in A0 and A′ = A0. Then

d(A′,B′) ≥ d(A0,B0) =

e(A0,B0) |A0||B0|

![image 15](<2016-conlon-hereditary-quasirandomness-without-regularity_images/imageFile15.png>)

≥ q + γ

|A||B| |A0||B0|

![image 16](<2016-conlon-hereditary-quasirandomness-without-regularity_images/imageFile16.png>)

≥ q + γ

|A| |A′|

![image 17](<2016-conlon-hereditary-quasirandomness-without-regularity_images/imageFile17.png>)

,

as required. ✷

The next lemma shows that if a graph satisﬁes QH,p but there are sets A and B for which the density d(A,B) deviates signiﬁcantly from the expected density, then there are sets A′ and B′ such that the density d(A′,B′) deviates by even more. This observation will allow us to run a density-increment argument in the proof of Theorem 1.2.

- Lemma 3.5. Let H be a graph with r vertices and m edges. Suppose G is a graph on n vertices that


satisﬁes QH,p(δ) and has disjoint subsets A and B with |A| = |B| such that δ ≤ 41rαmpmr−r(|A|/n)r and d(A,B) ≥ (1 + α)p or d(A,B) ≤ (1 − α)p with α ≤ 161mr. Then there are also disjoint subsets A′ and B′ with |A′| = |B′| and d(A′,B′) ≥ (1 + (1 + β)α)p or d(A′,B′) ≤ (1 − (1 + β)α)p where

![image 18](<2016-conlon-hereditary-quasirandomness-without-regularity_images/imageFile18.png>)

![image 19](<2016-conlon-hereditary-quasirandomness-without-regularity_images/imageFile19.png>)

β = p4mr−31 ||AA′||.

![image 20](<2016-conlon-hereditary-quasirandomness-without-regularity_images/imageFile20.png>)

![image 21](<2016-conlon-hereditary-quasirandomness-without-regularity_images/imageFile21.png>)

Proof. Suppose that we are in the case where d(A,B) ≥ (1+α)p. Let q = (1−α)p and υ = pmα/(4r). Take an arbitrary equitable partition of A into ⌊r/2⌋ subsets A1,... ,A⌊r/2⌋ and B into ⌈r/2⌉ subsets A⌊r/2⌋+1,... ,Ar.

First suppose that there is a pair (Ai,Aj) with 1 ≤ i ≤ ⌊r/2⌋ < j ≤ r which is not lower-(d(A,B),υ)regular. As Ai ⊂ A and Aj ⊂ B, (A,B) is not lower-(d(A,B),υ′)-regular, where υ′ = υ|A|Ai|||||BA|j| ≥ r22υ.

![image 22](<2016-conlon-hereditary-quasirandomness-without-regularity_images/imageFile22.png>)

![image 23](<2016-conlon-hereditary-quasirandomness-without-regularity_images/imageFile23.png>)

- By Lemma 3.3, (A,B) is also not upper-(d(A,B),υ′/2)-regular. Therefore, by Lemma 3.4, there are subsets A′ ⊆ A and B′ ⊆ B such that |A′| = |B′| and d(A′,B′) ≥ d(A,B) + υ2′ ||AA′|| ≥ d(A,B) + rυ2 ||AA′||.


![image 24](<2016-conlon-hereditary-quasirandomness-without-regularity_images/imageFile24.png>)

![image 25](<2016-conlon-hereditary-quasirandomness-without-regularity_images/imageFile25.png>)

![image 26](<2016-conlon-hereditary-quasirandomness-without-regularity_images/imageFile26.png>)

![image 27](<2016-conlon-hereditary-quasirandomness-without-regularity_images/imageFile27.png>)

Hence, since rυ2 ||AA′|| = αβp, we may suppose all pairs (Ai,Aj) with 1 ≤ i ≤ ⌊r/2⌋ < j ≤ r are lower-(d(A,B),υ)-regular.

![image 28](<2016-conlon-hereditary-quasirandomness-without-regularity_images/imageFile28.png>)

![image 29](<2016-conlon-hereditary-quasirandomness-without-regularity_images/imageFile29.png>)

Now suppose there is a pair (Ai,Aj) with 1 < i < j ≤ ⌊r/2⌋ which is not lower-(q,υ)-regular.

- By Lemma 3.4, there are subsets A′ ⊆ Ai and B′ ⊆ Aj with |A′| = |B′| and d(A′,B′) ≤ q −


υ min{||AAi′||, ||ABj′||} ≤ q − υr ||AA′|| ≤ (1 −(1 + β)α)p. Hence, we may suppose all pairs (Ai,Aj) with 1 < i <

![image 30](<2016-conlon-hereditary-quasirandomness-without-regularity_images/imageFile30.png>)

![image 31](<2016-conlon-hereditary-quasirandomness-without-regularity_images/imageFile31.png>)

![image 32](<2016-conlon-hereditary-quasirandomness-without-regularity_images/imageFile32.png>)

![image 33](<2016-conlon-hereditary-quasirandomness-without-regularity_images/imageFile33.png>)

- j ≤ ⌊r/2⌋ are lower-(q,υ)-regular. Similarly, we may suppose all pairs (Ai,Aj) with ⌊r/2⌋ < i < j ≤ r are lower-(q,υ)-regular.


Consider a bijection φ : V (H) → [r]. Let m1 denote the number of edges (v,w) of H for which φ(v),φ(w) ≤ ⌊r/2⌋ or φ(v),φ(w) > ⌊r/2⌋ and m2 denote the number of edges (v,w) of H for which φ(v) ≤ ⌊r/2⌋ < φ(w), so m = m1 + m2. By Lemma 3.2, the number of copies of H where v maps to Aφ(v) for each vertex v ∈ H is at least

r

(qm1d(A,B)m2 − mυ)

i=1

r

|Ai| ≥ ((1 − α)m1(1 + α)m2pm − mυ)

|Ai|

i=1

r

≥ ((1 − αm1)(1 + αm2)pm − mυ)

|Ai|

i=1

r

= (1 − αm1 + αm2 − α2m1m2)pm − mυ

|Ai|

i=1

r

≥ ((1 − αm1 + αm2 − αm/64r)pm − mυ)

|Ai|,

i=1

(1)

where in the last inequality we used m1m2 ≤ m2/4, which follows from m1+m2 = m and the AM–GM inequality, and α ≤ 1/16mr.

We average this lower bound over all choices of φ. Each edge (v,w) maps to a pair (i,j) with i < j and the probability this pair satisﬁes i ≤ ⌊r/2⌋ < j is ⌊r/2⌋⌈r/2⌉/ 2 r ≥ 14(r2 − 1)/ 2 r = 21 1 + 1r . Thus, by linearity of expectation, E[m2 − m1] ≥ m/r. Hence, the average value of (1) is at least

![image 34](<2016-conlon-hereditary-quasirandomness-without-regularity_images/imageFile34.png>)

![image 35](<2016-conlon-hereditary-quasirandomness-without-regularity_images/imageFile35.png>)

![image 36](<2016-conlon-hereditary-quasirandomness-without-regularity_images/imageFile36.png>)

r

((1 + αE[m2 − m1] − αm/64r) pm − mυ)

|Ai|

i=1

which is at least

((1 + αm/r − αm/64r) pm − mυ)

r

|Ai| ≥ 1 +

i=1

- 63

![image 37](<2016-conlon-hereditary-quasirandomness-without-regularity_images/imageFile37.png>)

- 64


αm/r pm − mυ

r

|Ai|.

i=1

This in turn is equal to

r

47 64r

αmpm

pm

|Ai| +

![image 38](<2016-conlon-hereditary-quasirandomness-without-regularity_images/imageFile38.png>)

i=1

r

|Ai| > pm

i=1

r

|Ai| +

i=1

1 4r

αmpmr−r(|A|/n)rnr ≥ pm

![image 39](<2016-conlon-hereditary-quasirandomness-without-regularity_images/imageFile39.png>)

r

|Ai| + δnr,

i=1

contradicting the assumption that G satisﬁes QH,p(δ) and completing the proof in this case. The case d(A,B) ≤ (1 − α)p follows similarly. ✷

A single vertex subset U of a graph is called ǫ-regular if, for each pair of subsets A′,B′ ⊂ U, we have |e(A′,B′) − d(U)|A′||B′|| ≤ ǫ|U|2. In [3], the ﬁrst two authors proved the following lemma with δ−1 having a double-exponential dependence on ǫ−1.

- Lemma 3.6. For each ǫ > 0, there is δ > 0 such that every graph on n vertices has an ǫ-regular subset on at least δn vertices.


- We are now ready to prove Theorem 1.2. That is, we will show that if G satisﬁes PH,p∗ (δ) with δ = c′(p,r)ǫc(p,r), then it also satisﬁes P2∗,p(ǫ), where r is the number of vertices in H.


- Proof of Theorem 1.2: Suppose for contradiction that G is a graph on n vertices which satisﬁes


property PH,p∗ (δ), but does not satisfy property P2∗,p(ǫ), where δ = c′(p,r)ǫc(p,r) with c(p,r) = 10r4p1−m and c′(p,r) > 0 will be chosen suﬃciently small depending only on p and r. By Lemma 3.1, G also

has property QH,p((2r − 1)δ). As G does not satisfy property P2∗,p(ǫ), there is S ⊆ V (G) with

2e(S) − p|S|2 > ǫn2. Averaging over all equitable partitions S = A ∪ B, we obtain that there are disjoint vertex subsets A0 and B0 with |A0| = |B0| and |e(A0,B0) − p|A0||B0|| > ǫn2/4. We have |A0|2 = |A0||B0| > ǫn2/4, so that |A0| ≥ ǫ1/2n/2 and also |d(A0,B0) − p| > ǫn2/(4|A0||B0|) ≥ ǫ.

We repeatedly apply Lemma 3.5, starting with A0 and B0, until we arrive at a pair of subsets (A′,B′) with |A′| = |B′| and d(A′,B′) = (1 + α)p or d(A′,B′) = (1 − α)p, for some α ≥ 161mr. As we will see below, the sets deﬁned during this process will always be suﬃciently large that we may continue applying Lemma 3.5 until this happens. Having already found disjoint sets Ai and Bi with

![image 40](<2016-conlon-hereditary-quasirandomness-without-regularity_images/imageFile40.png>)

d(Ai,Bi)

p − 1 := αi (so, in particular, α0 > ǫ/p), we apply Lemma 3.5 to obtain disjoint sets A′i and Bi′ with |A′i| = |Bi′| and |d(A

![image 41](<2016-conlon-hereditary-quasirandomness-without-regularity_images/imageFile41.png>)

′ i,Bi′)

p −1| ≥ (1+βi)αi, where βi = p4mr−31 ||AA′i|

i|. Let Ai+1 and Bi+1 be disjoint sets with |Ai+1| as large as possible such that |Ai+1| = |Bi+1| ≥ |A′i| and αi+1 := d(Ai+1p,Bi+1) − 1 ≥

![image 42](<2016-conlon-hereditary-quasirandomness-without-regularity_images/imageFile42.png>)

![image 43](<2016-conlon-hereditary-quasirandomness-without-regularity_images/imageFile43.png>)

![image 44](<2016-conlon-hereditary-quasirandomness-without-regularity_images/imageFile44.png>)

![image 45](<2016-conlon-hereditary-quasirandomness-without-regularity_images/imageFile45.png>)

d(A′i,Bi′)

p − 1 is as large as possible (such sets exist because A′i and Bi′ have the desired properties).

![image 46](<2016-conlon-hereditary-quasirandomness-without-regularity_images/imageFile46.png>)

Let ai = |Ai−1|/|Ai|. Note that ai ≥ 1, as otherwise we would have taken Ai and Bi for Ai−1 and Bi−1, respectively. Let γ = p4mr−31, so that αi+1 ≥ (1 + γai+1)αi. Let i0 be the last i for which we obtain an Ai and Bi, so that either αi0 ≥ 161mr or the sets A′ = Ai0 and B′ = Bi0 are too small for the hypotheses of Lemma 3.5 to hold. We have

![image 47](<2016-conlon-hereditary-quasirandomness-without-regularity_images/imageFile47.png>)

![image 48](<2016-conlon-hereditary-quasirandomness-without-regularity_images/imageFile48.png>)

i0

αi0 = α0

j=1

i0

αj αj−1

(1 + γaj).

≥ α0

![image 49](<2016-conlon-hereditary-quasirandomness-without-regularity_images/imageFile49.png>)

j=1

As also αi0 ≤ 1/p and α0 ≥ ǫ/p, we get ij0=1(1 + γaj) ≤ 1ǫ. Given this inequality, the maximum of i0 j=1 aj is attained when all the aj are equal; call this equal value a. Thus, we are interested in the maximum of ai0 given that (1 + γa)i0 ≤ 1ǫ. This is equivalent to maximizing ln(1+lnaγa). Let x = γa. For x ≤ 1.5, we have ln(1 + x) ≥ x/2 and so ln(1+lnaγa) ≤ 2lnxa = γ2 lnaa ≤ eγ2 . For x > 1.5, we have

![image 50](<2016-conlon-hereditary-quasirandomness-without-regularity_images/imageFile50.png>)

![image 51](<2016-conlon-hereditary-quasirandomness-without-regularity_images/imageFile51.png>)

![image 52](<2016-conlon-hereditary-quasirandomness-without-regularity_images/imageFile52.png>)

![image 53](<2016-conlon-hereditary-quasirandomness-without-regularity_images/imageFile53.png>)

![image 54](<2016-conlon-hereditary-quasirandomness-without-regularity_images/imageFile54.png>)

![image 55](<2016-conlon-hereditary-quasirandomness-without-regularity_images/imageFile55.png>)

![image 56](<2016-conlon-hereditary-quasirandomness-without-regularity_images/imageFile56.png>)

![image 57](<2016-conlon-hereditary-quasirandomness-without-regularity_images/imageFile57.png>)

ln a ln(1+γa) ≤ ln(lnγaa) = 1 + lnlnγ−x1 ≤ 3ln γ−1. As we may assume r ≥ 3 and m ≥ 2, γ is small enough that the ﬁrst bound is larger, so we have

![image 58](<2016-conlon-hereditary-quasirandomness-without-regularity_images/imageFile58.png>)

![image 59](<2016-conlon-hereditary-quasirandomness-without-regularity_images/imageFile59.png>)

![image 60](<2016-conlon-hereditary-quasirandomness-without-regularity_images/imageFile60.png>)

i0

|A′| = |A0|/

j=1

aj ≥ ǫ2/(eγ)|A0| ≥

- 1

![image 61](<2016-conlon-hereditary-quasirandomness-without-regularity_images/imageFile61.png>)

- 2


ǫ1/2+2/(eγ)n.

By the choice of c(p,r), |A′| = |Ai0| is large enough that Lemma 3.5 still applies at the next step if α := αi0 ≤ 161mr. Therefore, we must have α > 161mr.

![image 62](<2016-conlon-hereditary-quasirandomness-without-regularity_images/imageFile62.png>)

![image 63](<2016-conlon-hereditary-quasirandomness-without-regularity_images/imageFile63.png>)

The sets A′ and B′ have order at least ǫ5r3p1−mn. Suppose that d(A′,B′) = (1 + α)p with α > 161mr. The other case when d(A′,B′) < (1 − α)p is handled similarly. Let C be the subset of A′ with at

![image 64](<2016-conlon-hereditary-quasirandomness-without-regularity_images/imageFile64.png>)

least (1 + α/2)p|B′| neighbors in B′, so |C| ≥ |A′|αp/2. Let η := 10−5α2p2mm−2 and κ = 2mηp1−m. Apply Lemma 3.6 to the subgraph of G induced by C. We get a subset C1 ⊂ C which is η-regular with |C1| ≥ τ|C|, where τ only depends on p and r. If d(C1) < p − κ, then by the counting lemma, Lemma 3.2, the number of homomorphisms from H to C1 is at most

(p−κ)m|C1|r+mη|C1|r ≤ (1−

κ p

)pm|C1|r +mη|C|r = pm|C1|r−mη|C1|r ≤ pm|C1|r−a(p,r)ǫ8r4p1−mnr

![image 65](<2016-conlon-hereditary-quasirandomness-without-regularity_images/imageFile65.png>)

for an appropriate constant a(p,r). This contradicts PH,p∗ (δ) when c′(p,r) is suﬃciently small. Hence, d(C1) ≥ p−κ. Let D be the subset of B′ with at least (1+α/4)p|C1| neighbors in C1, so |D| ≥ |B′|αp/4.

Let D1 ⊂ D be a subset of order αp40mr−1|C1|.

![image 66](<2016-conlon-hereditary-quasirandomness-without-regularity_images/imageFile66.png>)

The rest of the proof is in showing that C1 ∪ D1 violates the property PH,p∗ (δ) as this subset contains too many labeled copies of H. Indeed, by Lemma 3.2, the number of homomorphisms from H to C1 is at least (p−κ)m|C1|r −mη|C1|r ≥ pm|C1|r −(mpm−1κ+mη)|C1|r. The number of homomorphisms from H to C1 which fail to be copies of H is at most the number of non-injective mappings from H to C1, which is less than r2|C1|r−1. Thus, we get at least pm|C1|r − (mpm−1κ + mη + r2|C1|−1)|C1|r copies of H in C1.

We next give a lower bound on the number of copies of H in C1 ∪ D1 with the copy of vertex i in D1 and the remaining r − 1 vertices in C1. Suppose vertex i has degree t in H. We have t ≥ 1 as H has no isolated vertices. Fix a vertex v ∈ D1 to map i to, and let C2 be the neighborhood of i in C1, so |C2| ≥ (1 + α/4)p|C1|. Since |C2| ≥ p|C1| and C1 is η-regular, we get that each of the pairs (C1,C1), (C1,C2), (C2,C2) is 2p−2η-regular. The number of homomorphisms of H with the copy of vertex i mapping to v and the remaining vertices of H mapping to C1 (so each of the t neighbors of i has to map to C2) is, by Lemma 3.2, at least

(p − κ)m−t − (m − t)2p−2η |C1|r−t−1|C2|t ≥ pm−t − (m − t)κpm−t−1 − (m − t)2p−2η |C1|r−t−1|C2|t ≥ (pm−t − αpm−t/8)|C1|r−t−1|C2|t ≥ (pm−1 − αpm−1/8)|C1|r−2|C2|1 ≥ (pm−1 − αpm−1/8)(1 + α/4)p|C1|r−1 ≥ (1 + α/10) pm|C1|r−1.

The number of mappings from H to C1 ∪D1 with vertex i going to v and the other r−1 vertices going to C1 which are not one-to-one is at most r2|C1|r−2. As |C1| ≥ 20r2α−1p−m, then we get at least (1 + α/20) pm|C1|r−1 labeled copies of H with vertex i mapping to v and the remaining vertices mapping to C1. Summing over all choices of v in D1, we get that there are at least (1 + α/20) pm|C1|r−1|D1| labeled copies of H with vertex i mapping to D1 and the remaining r − 1 vertices mapping to C1. Finally, summing over all r choices of i, we get at least r (1 + α/20) pm|C1|r−1|D1| labeled copies of

- H with one vertex mapping to D1 and the remaining r − 1 vertices mapping to C1. Finally, the number of possible mappings from H to C1 ∪ D1 with at least two vertices in D1 is at


most j≥2 rj |D1|j|C1|r−j ≤ r2|D1|2|C1|r−2. Putting the bounds together, we get that the number of labeled copies of H in C1 ∪ D1 is pm|C1 ∪ D1|r (this is the sum of the contributions of the main terms) plus at least

α 20

pm|C1|r−1|D1| − (mpm−1κ + mη + r2|C1|−1)|C1|r − r2|D1|2|C1|r−2,

r

![image 67](<2016-conlon-hereditary-quasirandomness-without-regularity_images/imageFile67.png>)

which, substituting in |D1| = αp40mr |C1|, is equal to

![image 68](<2016-conlon-hereditary-quasirandomness-without-regularity_images/imageFile68.png>)

α2 1600

p2m|C1|r − (mpm−1κ + mη + r2|C1|−1)|C1|r.

![image 69](<2016-conlon-hereditary-quasirandomness-without-regularity_images/imageFile69.png>)

Using |C1| ≥ r2η−1 (recall that η = 10−5α2p2mm−2) and substituting in κ = 2mηp1−m, we get that this is at least

α2 1600

p2m|C1|r − 4m2η|C1|r ≥ 10−5α2p2m|C1|r ≥ δnr, provided c′(p,r) is chosen suﬃciently small. This completes the proof. ✷

![image 70](<2016-conlon-hereditary-quasirandomness-without-regularity_images/imageFile70.png>)

# 4 Concluding remarks

It is plausible that Theorem 1.1 can be extended to all H, that is, that a graph G which satisﬁes PH,p∗ (δ) also satisﬁes P2∗,p(ǫ) with ǫ ≤ c(p,r)δ, where r is the number of vertices in H. However, it seems that new ideas will be needed to prove this in full generality. It would already be interesting to obtain a linear dependence in the special case H = C4. One might also ask about the quantitative aspects of other quasirandom equivalences. For example, we know that for any ǫ > 0, there exists δ > 0 such that if a graph G has density p and satisﬁes PC4,p(δ), then it also satisﬁes P2∗,p(ǫ). The forcing conjecture, which was already mentioned in the introduction, states that a similar result should hold when C4 is replaced by any bipartite graph H which contains a cycle. Somewhat tentatively, we are willing to venture that the following stronger quantitative version of this conjecture holds.

Conjecture 4.1. Let H be a ﬁxed bipartite graph of girth g and 0 < p < 1 a ﬁxed constant. For each ǫ > 0, there is δ = Ω(ǫg) such that any graph G with density p which satisﬁes PH,p(δ) also satisﬁes P2∗,p(ǫ).

To see that the girth dependence would be tight, consider a random graph with n vertices whose vertex set is partitioned into two parts V1 and V2, each of order n/2, with density p − ǫ inside parts and density p + ǫ between parts. Equivalently, consider the generalized random graph G on two vertices, where loops have weight p −ǫ and the edge between the two vertices has weight p +ǫ. By picking one vertex from G, we see that it does not satisfy P2∗,p(ǫ/2). Consider now a random mapping of the vertices of H to the two vertices of G. For an edge e of H, let Xe = −1 if both vertices of e map to the same vertex of G and Xe = 1 if the vertices of e map to diﬀerent vertices of G. The homomorphism density of H in G is then

E[

e

(p + Xeǫ)].

Suppose that e1,... ,ek are edges of H with k < g. Since these edges form a forest, it follows that E[Xe1Xe2 ... Xek] = E[Xe1]··· E[Xek].

In particular, since E[Xe] = 0, this implies that the coeﬃcient of ǫi is zero for i = 1,... ,g − 1 and, therefore, G satisﬁes PH,p(δ) with δ = O(ǫg).

It is not hard to verify that Conjecture 4.1 holds when H is an even cycle. Combining this observation with other known results allows us to prove the conjecture for some reasonably broad classes of graphs.

For example, Theorem 1.1 in [4] implies that if H is a bipartite graph with m edges which has two vertices in one part complete to the other part and minimum degree at least two in the ﬁrst part, then the homomorphism density tH(G) satisﬁes tH(G) ≥ tC4(G)m/4. Therefore, if tH(G) ≤ pm(1 + ǫ4), we have tC4(G) ≤ p4(1+ǫ4)4/m ≤ p4(1+ m8 ǫ4) and the required result for H follows from the C4 case. As with the forcing conjecture, similar arguments can likely prove Conjecture 4.1 for many of the graphs for which Sidorenko’s conjecture is known to hold. On the other hand, our second-order Sidorenko conjecture may be easier to disprove than the conjecture itself.

![image 71](<2016-conlon-hereditary-quasirandomness-without-regularity_images/imageFile71.png>)

# References

- [1] F. R. K. Chung, R. L. Graham and R. M. Wilson, Quasi-random graphs, Combinatorica 9 (1989), 345–362.
- [2] D. Conlon, A new upper bound for diagonal Ramsey numbers, Ann. of Math. 170 (2009), 941–960.
- [3] D. Conlon and J. Fox, Bounds for graph regularity and removal lemmas, Geom. Funct. Anal. 22

(2012), 1191–1256.

- [4] D. Conlon, J. Fox, and B. Sudakov, An approximate version of Sidorenko’s conjecture, Geom. Funct. Anal. 20 (2010), 1354–1366.
- [5] D. Conlon, J. H. Kim, C. Lee, and J. Lee, Some advances on Sidorenko’s conjecture, arXiv:1510.06533 [math.CO].
- [6] P. Erd˝os, M. Goldberg, J. Pach and J. Spencer, Cutting a graph into two dissimilar halves, J. Graph Theory 12 (1988), 121–131.
- [7] W. T. Gowers, A new proof of Szemere´di’s theorem, Geom. Funct. Anal. 11 (2001), 465–588.
- [8] S. Hoory, N. Linial and A. Wigderson, Expander graphs and their applications, Bull. Amer. Math. Soc. 43 (2006), 439–561.
- [9] S. Janson, T.  Luczak and A. Rucin´ski, Random graphs, Wiley, New York, 2000.
- [10] G. Katona, A theorem of ﬁnite sets, in Theory of graphs (Proc. Colloq., Tihany, 1966), 187–207, Academic Press, New York, 1968.
- [11] J. H. Kim, C. Lee and J. Lee, Two approaches to Sidorenko’s conjecture, Trans. Amer. Math. Soc. 368 (2016), 5057–5074.
- [12] M. Krivelevich and B. Sudakov, Pseudo-random graphs, in More sets, graphs and numbers, 199– 262, Bolyai Soc. Math. Stud. 15, Springer, Berlin, 2006.
- [13] J. B. Kruskal, The number of simplices in a complex, in Mathematical optimization techniques, 251–278, Univ. of California Press, Berkeley, Calif., 1963.
- [14] J. X. Li and B. Szegedy, On the logarithmic calculus and Sidorenko’s conjecture, to appear in Combinatorica.
- [15] L. Lov´asz, Combinatorial problems and exercises, 2nd edition. AMS Chelsea Publishing, Providence, RI, 2007.


- [16] L. Lov´asz, Large networks and graph limits, Amer. Math. Soc. Colloq. Publ., Vol. 60, Amer. Math. Soc., Providence, RI, 2012.
- [17] L. Lov´asz and B. Szegedy, Szemere´di’s lemma for the analyst, Geom. Funct. Anal. 17 (2007), 252–270.
- [18] C. Reiher and M. Schacht, in preparation.
- [19] A. Shapira, Quasi-randomness and the distribution of copies of a ﬁxed graph, Combinatorica 28

(2008), 735–745.

- [20] M. Simonovits and V. T. So´s, Hereditarily extended properties, quasi-random graphs and not necessarily induced subgraphs, Combinatorica 17 (1997), 577–596.
- [21] J. Skokan and L. Thoma, Bipartite subgraphs and quasi-randomness, Graphs Combin. 20 (2004), 255–262.
- [22] B. Szegedy, An information theoretic approach to Sidorenko’s conjecture, arXiv:1406.6738v3 [math.CO].
- [23] E. Szemere´di, Regular partitions of graphs, in Probl`emes combinatoires et the´orie des graphes (Colloq. Internat. CNRS, Univ. Orsay, Orsay, 1976), 399–401, Colloq. Internat. CNRS, Vol. 260, CNRS, Paris, 1978.
- [24] A. Thomason, Pseudorandom graphs, in Random graphs ’85 (Poznan´, 1985), 307–331, NorthHolland Math. Stud. 144, North-Holland, Amsterdam, 1987.
- [25] A. Thomason, Random graphs, strongly regular graphs and pseudorandom graphs, in Surveys in combinatorics 1987 (New Cross, 1987), 173–195, London Math. Soc. Lecture Note Ser. 123, Cambridge Univ. Press, Cambridge, 1987.


