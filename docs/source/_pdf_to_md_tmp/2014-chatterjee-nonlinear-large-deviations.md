arXiv:1401.3495v6[math.PR]29Apr2016

NONLINEAR LARGE DEVIATIONS

SOURAV CHATTERJEE AND AMIR DEMBO

Abstract. We present a general technique for computing large deviations of nonlinear functions of independent Bernoulli random variables. The method is applied to compute the large deviation rate functions for subgraph counts in sparse random graphs. Previous technology, based on Szemere´di’s regularity lemma, works only for dense graphs. Applications are also made to exponential random graphs and three-term arithmetic progressions in random sets of integers.

1. Introduction

- 1.1. A motivating example. Let G(N,p) be the Erd˝os–Re´nyi random graph on N vertices with edge probability p, that is, the classical model where any two vertices are connected by an edge with probability p, independent of all else. Let T denote the number of triangles in this graph. It has been an open question in the random graph literature for a long time [23] to determine the behavior of the upper tail of T, that is, probabilities of the type P(T ≥ (1 + δ)E(T)). The main diﬃculty with this problem, and the reason why it may be appealing to a probabilist, is that the standard tools from concentration of measure and other probability inequalities do not seem to work so well in this setting, in spite of the fact that the number of triangles in an Erd˝os–Re´nyi graph is simply a degree three polynomial of independent Bernoulli random variables.


After a series of successively improving suboptimal results by many authors over many years, a big advance was made by Kim and Vu [29] and simultaneously by Janson et al. [22] in 2004 who showed that if p ≥ N−1 log N, then

exp(−c1(δ)N2p2 log(1/p)) ≤ P(T ≥ (1 + δ)E(T)) ≤ exp(−c2(δ)N2p2), where c1(δ) and c2(δ) are constants depending on δ only.

Several years later, the logarithmic discrepancy between the exponents on the two sides was removed by Chatterjee [12] and independently by DeMarco and Kahn [18, 19], where it was shown that when p ≥ N−1 log N,

exp(−c1(δ)N2p2 log(1/p)) ≤ P(T ≥ (1 + δ)E(T)) ≤ exp(−c2(δ)N2p2 log(1/p)).

This still left open the question of determining the dependence of the exponent on δ. When p is ﬁxed and N tends to inﬁnity, the problem was solved in 2011 by Chatterjee and Varadhan [16], conﬁrming a conjecture from an unpublished manuscript of Bolthausen, Comets and Dembo [4]. In [16], it was shown that for ﬁxed p ∈ (0,1) and δ > 0,

P(T ≥ (1 + δ)E(T)) = exp(−c(δ,p)N2(1 − o(1))) (1.1)

![image 1](<2014-chatterjee-nonlinear-large-deviations_images/imageFile1.png>)

2010 Mathematics Subject Classiﬁcation. 60F10, 05C80, 60C05, 05A20. Key words and phrases. Large deviations, sparse random graphs, regularity lemma, arithmetic progressions, ex-

ponential random graph models, concentration of measure. Sourav Chatterjee’s research partially supported by NSF grant DMS-1441513. Amir Dembo’s research partially supported by NSF grant DMS-1106627.

1

as N → ∞, where

- 1

![image 2](<2014-chatterjee-nonlinear-large-deviations_images/imageFile2.png>)

- 2


{Ip(f) : T(f) ≥ (1 + δ)p3}, (1.2)

inf

c(δ,p) =

f

where f : [0,1]2 → [0,1] is any Lebesgue measurable function that satisﬁes f(x,y) = f(y,x) for all x and y,

1 − f(x,y) 1 − p

f(x,y) p

+ (1 − f(x,y))log

Ip(f) =

f(x,y)log

dxdy , and

![image 3](<2014-chatterjee-nonlinear-large-deviations_images/imageFile3.png>)

![image 4](<2014-chatterjee-nonlinear-large-deviations_images/imageFile4.png>)

[0,1]2

f(x,y)f(y,z)f(z,x)dxdy dz .

T(f) =

[0,1]3

Incidentally, the variational problem (1.2) has not yet yielded explicit solutions except in special ranges of δ and p [14, 16, 33, 32].

The above result was proved using Szemere´di’s regularity lemma [35] from graph theory. A well known problem with Szemere´di’s lemma is that it yields very poor quantitative bounds, which makes it virtually impossible to extend the arguments of [16] to the case where p is allowed to tend to 0 as N → ∞. One can show (e.g. in [32]) that a weaker version of Szemere´di’s lemma suﬃces for the proof in [16], which makes it possible to make the technique work when p tends to zero slower than a negative power of log N, but it seems safe to bet that a Szemere´di type argument cannot help when p goes to zero like a negative power of N.

The last problem mentioned in the previous paragraph, namely, computing c(δ,p) in (1.1) when p goes to zero like N−α for some α > 0, was the original motivation for this paper. What we accomplish in this article is the following: We build a general machinery for tackling large deviations of certain class of nonlinear functions of independent Bernoulli random variables, which in particular circumvents the use of Szemere´di’s lemma. Among other things, this approach yields a variational formula for c(δ,p), analogous to (1.2), which holds when p = p(N) → 0 slower than N−1/42. To see what its potential beneﬁts may be, we note that after the ﬁrst version of this paper was posted on arXiv, Lubetzky and Zhao [32] found a way to explicitly solve our variational problem when N−1 ≪ p ≪ 1. As a result of this additional exciting development, we now know that if p(N) → 0 slower than N−1/42, then

P(T ≥ (1 + δ)E(T)) = exp −(1 − o(1))min

δ2/3 2

,

![image 5](<2014-chatterjee-nonlinear-large-deviations_images/imageFile5.png>)

δ 3

![image 6](<2014-chatterjee-nonlinear-large-deviations_images/imageFile6.png>)

1 p

N2p2 log

![image 7](<2014-chatterjee-nonlinear-large-deviations_images/imageFile7.png>)

.

Therefore, the variational formula for c(δ,p) proved in this paper and its solution by Lubetzky and Zhao have completed the quest for understanding the behavior of the upper tail of triangle counts in Erd˝os–Re´nyi random graphs under the restriction that p ≫ N−1/42. It has been conjectured in [32] that the same formula should hold all the way down to p ≫ N−1/2. A strong evidence in favor of this conjecture is that the Lubetzky–Zhao solution of the variational formula for c(δ,p) holds whenever p ≫ N−1/2. The above result has been recently extended to more general subgraph counts by Bhattacharya et al. [2]. For a survey of these developments and a short overview of the emerging ﬁeld of large deviations for random graphs, see [13].

- 1.2. Goal of the paper. Suppose that f : [0,1]n → R is a function with some amount of smooth-


ness. Let p be a number in the open interval (0,1), and Y = (Y1,... ,Yn) be a vector of i.i.d. Bernoulli(p) random variables. For u ∈ [0,1] let

1 − u 1 − p

u p

+ (1 − u)log

, (1.3)

Ip(u) := ulog

![image 8](<2014-chatterjee-nonlinear-large-deviations_images/imageFile8.png>)

![image 9](<2014-chatterjee-nonlinear-large-deviations_images/imageFile9.png>)

and for each x = (x1,... ,xn) ∈ [0,1]n, deﬁne

n

Ip(xi). (1.4) For each t ∈ R, deﬁne

Ip(x) :=

i=1

φp(t) := inf{Ip(x) : x ∈ [0,1]n such that f(x) ≥ tn}. (1.5) We want to investigate conditions under which the following “upper tail approximation” is valid:

P(f(Y ) ≥ tn) = exp(−φp(t) + lower order terms). (1.6)

Analogous statements may be similarly formulated if the Yi’s have some distributions other than Bernoulli.

It is known that such an approximation is valid for continuous functions of the empirical measure of i.i.d. random variables. This fact forms the basis of a big part of modern large deviations theory; see [20] and the references therein. Since the empirical measure is a linear function of i.i.d. random objects (Dirac masses at the sample points), this is a class of linear examples. The main goal of this paper is to establish conditions under which this approximation holds in nonlinear settings.

One challenging example of a nonlinear result of the above type is the recent proof in [16] that the approximation holds for upper tails of subgraph counts in dense Erd˝os-Re´nyi random graphs, a result which was later generalized to random matrices [17] and exponential random graphs [15]. The proofs in [16, 17, 15] are, however, rather specialized to the random graph setting. The main tool in these papers is the regularity lemma of Szemere´di [35] and the graph limit theory of Lov´asz and coauthors [7, 8, 31] that builds on the regularity lemma. The unavailability of a suitable “sparse” version of Szemere´di’s lemma makes it impossible to extend the results of [16, 17, 15] to sparse graphs. Serious attempts have been made at formulating a sparse graph limit theory and sparse regularity lemmas [3, 5, 6], but it is unlikely that these will provide the precision required for large deviations. The reason is that in all existing formulations, there is always some assumption about the regularity of the graph structure, and it may not be true that random graphs obey such regularity conditions in the large deviations regime. In graph theoretic terminology, the absence of a “counting lemma” for sparse graphs is the main impediment to extending a Szemere´di type argument to the sparse case.

More importantly, ideally one should not need to resort to specialized graph theoretic tools to prove an approximation as simple and basic as (1.6) for an f that may be as uncomplicated as a polynomial of degree three (e.g. number of triangles).

Our main objective here is to give a general error bound for the approximation (1.6) directly in terms of properties of the function f (as elaborated in the sequel), with an error bound small enough to allow extension of the aforementioned graph theoretic large deviation results to sparse random graphs. Incidentally, there are several notable results on upper bounds for tail probabilities for nonlinear functions of independent Bernoulli random variables. The bounded diﬀerence inequality [34] has been available for a long time. Improved inequalities were discovered by Talagrand [36], Lata a [30], Kim and Vu [28] and Vu [39]. However, all these methods seem to fall short of proving an approximation such as (1.6).

- 1.3. The main result. Our main result is Theorem 1.1 which gives a suﬃcient condition for the validity of the approximation (1.6). This suﬃcient condition may be roughly described as follows: The approximation (1.6) is valid when, in addition to some minor smoothness conditions on the


function f, the gradient vector ∇f(x) = (∂f/∂x1,... ∂f/∂xn) may be approximately encoded by o(n) bits of information. One may call this the “low complexity gradient” condition.

To illustrate this, consider the simple case of

n−1

xixi+1 ,

f(x) =

i=1

where the approximation (1.6) is not valid. Indeed, large deviation probabilities for this function are related to the one-dimensional Ising model, and easily shown to not satisfy (1.6). For this function, ∂f/∂xi = xi−1 +xi+1 for 2 ≤ i ≤ n−1, ∂f/∂x1 = x2, and ∂f/∂xn = xn−1, so clearly this gradient vector cannot be approximately encoded by o(n) many bits; we eﬀectively need to know all the xi’s to encode the gradient vector of this function. On the other hand, if

1 n 1≤i<j≤n

xixj ,

f(x) =

![image 10](<2014-chatterjee-nonlinear-large-deviations_images/imageFile10.png>)

as in the Currie-Weiss model, then for each i,

n

xi n

1 n j =i

1 n

∂f ∂xi

xj = −

=

+

xj .

![image 11](<2014-chatterjee-nonlinear-large-deviations_images/imageFile11.png>)

![image 12](<2014-chatterjee-nonlinear-large-deviations_images/imageFile12.png>)

![image 13](<2014-chatterjee-nonlinear-large-deviations_images/imageFile13.png>)

![image 14](<2014-chatterjee-nonlinear-large-deviations_images/imageFile14.png>)

j=1

Thus, the gradient vector is approximately encoded by the single quantity n−1 xj, so the “low complexity gradient” condition holds and the large deviation probabilities (which in this trivial case are covered by the general theory of large deviations), satisfy (1.6).

Unfortunately, although its content matches very well the preceding description, the actual statement of the theorem is somewhat messier, and requires some additional notation which we introduce next.

Let f denote the supremum norm of f : [0,1]n → R. Suppose that f : [0,1]n → R is twice continuously diﬀerentiable in (0,1)n, such that f and all its ﬁrst and second order derivatives extend continuously to the boundary. For each i and j, let

∂f ∂xi

fi :=

![image 15](<2014-chatterjee-nonlinear-large-deviations_images/imageFile15.png>)

∂2f ∂xi∂xj

and fij :=

.

![image 16](<2014-chatterjee-nonlinear-large-deviations_images/imageFile16.png>)

Deﬁne

a := f , bi := fi and cij := fij . Given ǫ > 0, let D(ǫ) be a ﬁnite subset of Rn such that for all x ∈ {0,1}n, there exists d = (d1,... ,dn) ∈ D(ǫ) such that

n

(fi(x) − di)2 ≤ nǫ2. (1.7)

i=1

The following theorem gives an error bound for the approximation (1.6) in terms of the quantities a, bi, cij and the sizes of the sets D(ǫ).

Theorem 1.1. For f as above, p ∈ (0,1) and Y a vector of n i.i.d. Bernoulli(p) random variables, let φp be deﬁned as in (1.5). Then, for any δ > 0, ǫ > 0 and t ∈ R,

log P(f(Y ) ≥ tn) ≤ −φp(t − δ) + complexity term

+ smoothness term,

where with a, b, cij, D(ǫ) deﬁned above, and K := φp(t)/n, complexity term :=

n

4K(n1 ni=1 b2i )1/2 δǫ

1 4

1/2

![image 17](<2014-chatterjee-nonlinear-large-deviations_images/imageFile17.png>)

βi2

ǫ + 3nǫ + log

n

![image 18](<2014-chatterjee-nonlinear-large-deviations_images/imageFile18.png>)

![image 19](<2014-chatterjee-nonlinear-large-deviations_images/imageFile19.png>)

i=1

+ log |D((δǫ)/(4K))|, and

n

n

1 4

(αγii + βi2) +

αγij2 + βiβjγij + 4βiγij

smoothness term := 4

![image 20](<2014-chatterjee-nonlinear-large-deviations_images/imageFile20.png>)

i=1

i,j=1

n

n

n

1 4

1/2

1/2

γii2

βi2

γii + log 2,

+ 3

+

![image 21](<2014-chatterjee-nonlinear-large-deviations_images/imageFile21.png>)

i=1

i=1

i=1

for

1/2

α := nK + n|log p| + n|log(1 − p)|, βi :=

2Kbi δ

+ |log p| + |log(1 − p)|, and

![image 22](<2014-chatterjee-nonlinear-large-deviations_images/imageFile22.png>)

2Kcij δ

6Kbibj nδ2

γij :=

+

. Moreover,

![image 23](<2014-chatterjee-nonlinear-large-deviations_images/imageFile23.png>)

![image 24](<2014-chatterjee-nonlinear-large-deviations_images/imageFile24.png>)

log P(f(Y ) ≥ tn) ≥ −φp(t + δ0) − ǫ0n − log 2, where

1 √n

p 1 − p and

ǫ0 :=

4 + log

![image 25](<2014-chatterjee-nonlinear-large-deviations_images/imageFile25.png>)

![image 26](<2014-chatterjee-nonlinear-large-deviations_images/imageFile26.png>)

![image 27](<2014-chatterjee-nonlinear-large-deviations_images/imageFile27.png>)

n

1/2

2 n

(acii + b2i)

δ0 :=

.

![image 28](<2014-chatterjee-nonlinear-large-deviations_images/imageFile28.png>)

i=1

We do not attempt to produce a watered down cleaner error bound, since the full power of

- Theorem 1.1 is needed in our applications.


- 1.4. Application to subgraph counts. Let G = G(N,p) be an Erd˝os-Re´nyi random graph on N vertices, with edge probability p. Let H be a ﬁxed ﬁnite simple graph. Let hom(H,G) be the number of homomorphisms (edge-preserving maps) from the vertex set V (H) of H into the vertex set V (G) of G. This is slightly diﬀerent than the number of copies of H in G, but nicer to work with mathematically. The “homomorphism density” of H in G is deﬁned as


hom(H,G) |V (G)||V (H)|

.

t(H,G) :=

![image 29](<2014-chatterjee-nonlinear-large-deviations_images/imageFile29.png>)

Our object of interest is the large deviation rate function for the upper tail of t(H,G). Let P denote upper triangular arrays like x = (xij)1≤i<j≤N, where each xij ∈ [0,1]. For any x ∈ P, let Gx denote the undirected random graph whose edges are independent, and edge {i,j} is present with probability xij, and absent with probability 1 − xij. Let t(H,x) denote the expected value of t(H,Gx). Explicitly, if H has vertex set {1,2,... ,k} and edge set E(H), then

N

1 Nk

xqlql′ ,

t(H,x) =

![image 30](<2014-chatterjee-nonlinear-large-deviations_images/imageFile30.png>)

q1,...,qk=1 {l,l′}∈E(H)

where xii is interpreted as zero for each i and xji = xij. For x ∈ P, deﬁne Ip(x) :=

Ip(xij),

1≤i<j≤N

where Ip(xij) is deﬁned as in (1.3). For each u > 1 deﬁne

ψp(u) := inf{Ip(x) : x ∈ P such that t(H,x) ≥ uE(t(H,G))}. The following theorem shows that for any u > 1,

P t(H,G) ≥ uE(t(H,G)) = exp(−ψp(u) + lower order terms), (1.8) provided that N is large and p is not too small. This approximation was proved for ﬁxed p and N growing to inﬁnity in [16] using Szemere´di’s lemma. Various interesting consequences of this variational formula were proved in [16, 33].

- Theorem 1.2. Take any ﬁnite simple graph H and let t(H,G) and ψp be deﬁned as above. Let k be the number of vertices of H, m be the number of edges of H, and ∆ be the maximum degree of H. Let X := t(H,G). Suppose that m ≥ 1 and N−1/(m+3) ≤ p ≤ 1 − N−1. Then for any u > 1 and any N suﬃciently large (depending only on H and u),

1 −

c(log N)b1 Nb2pb3

![image 31](<2014-chatterjee-nonlinear-large-deviations_images/imageFile31.png>)

≤

ψp(u) −log P(X ≥ uE(X)) ≤ 1 +

![image 32](<2014-chatterjee-nonlinear-large-deviations_images/imageFile32.png>)

C(log N)B1 NB2pB3

![image 33](<2014-chatterjee-nonlinear-large-deviations_images/imageFile33.png>)

, where c and C are constants that depend only on H and u, and

b1 = 1, b2 =

- 1

![image 34](<2014-chatterjee-nonlinear-large-deviations_images/imageFile34.png>)

- 2m


, b3 = ∆, B1 =

9 + 8m 5 + 8m

![image 35](<2014-chatterjee-nonlinear-large-deviations_images/imageFile35.png>)

, B2 =

1 5 + 8m

![image 36](<2014-chatterjee-nonlinear-large-deviations_images/imageFile36.png>)

, B3 = ∆ −

16m k(5 + 8m)

![image 37](<2014-chatterjee-nonlinear-large-deviations_images/imageFile37.png>)

. For example, when H is a triangle, an explicit computation of the error terms shows that the

- approximation (1.8) holds whenever p goes to zero at a rate slower than N−1/42(log N)11/14. There is no reason to believe that this should be the optimal threshold for the validity of the approximation (1.8), but at least it allows a polynomial rate of decay for p.


Shortly after the ﬁrst draft of this paper was put up on arXiv, Lubetzky and Zhao [32] explicitly computed by a remarkably clever argument the limiting behavior of ψp(u) when H is a triangle and N−1 ≪ p ≪ 1. With the aid of Theorem 1.2, this completely solves the large deviation problem for triangle counts when N−1/42(log N)11/14 ≪ p ≪ 1. Combining the solution of Lubetzky and Zhao with Theorem 1.2 gives the following result:

- Theorem 1.3 (Lubetzky and Zhao [32]). Let T be the number of triangles in G(N,p). Then for any ﬁxed δ > 0,


P(T ≥ (1 + δ)E(T)) = exp −(1 + o(1))min

δ2/3 2

,

![image 38](<2014-chatterjee-nonlinear-large-deviations_images/imageFile38.png>)

δ 3

![image 39](<2014-chatterjee-nonlinear-large-deviations_images/imageFile39.png>)

1 p

N2p2 log

![image 40](<2014-chatterjee-nonlinear-large-deviations_images/imageFile40.png>)

when N → ∞ and p → 0, subject to the constraint that p ≥ N−1/42 log N.

As mentioned above, [32, Theorem 1.1] gives the explicit limiting behavior of ψp(u) whenever p goes to zero at a rate slower than N−1. Therefore if one can prove a version of Theorem 1.2 that allows p to decay like N−1+ǫ, that would solve the problem of large deviations for triangle counts in its entirety.

More recently, Theorem 1.3 has been generalized by Bhattacharya et al. [2], who got the following beautiful result by analyzing the variational formula of Theorem 1.2. Take any ﬁnite simple graph

H with maximum degree ∆. Let H∗ be the induced subgraph of H on all vertices whose degree in H is ∆. Recall that an independent set in a graph is a set of vertices such that no two are connected by an edge. Also, recall that a graph is called regular if all its vertices have the same degree, and irregular otherwise. Deﬁne a polynomial

PH∗(x) :=

k

iH∗(k)xk ,

where iH∗(k) is the number of k-element independent sets in H∗. The main result of [2] is the following.

- Theorem 1.4 (Bhattacharya et al. [2]). Let H be a connected ﬁnite simple graph on k vertices with maximum degree ∆ ≥ 2. Then for any δ > 0, there is a unique positive number θ = θ(H,δ) that solves PH∗(θ) = 1 + δ, where PH∗ is the polynomial deﬁned above. Let HN,p be the number of homomorphisms of H into a G(N,p) random graph. Then there is a constant αH > 0 depending only on H, such that if N → ∞ and p → 0 slower than N−αH, then for any δ > 0,


1 p

P(HN,p ≥ (1 + δ)E(HN,p)) = exp −(1 + o(1))c(δ)N2p∆ log

,

![image 41](<2014-chatterjee-nonlinear-large-deviations_images/imageFile41.png>)

where

c(δ) =

min{θ, 21δ2/k} if H is regular, θ if H is irregular.

![image 42](<2014-chatterjee-nonlinear-large-deviations_images/imageFile42.png>)

The formula given in Theorem 1.4 is more than just a formula. It gives a hint at the conditional structure of the graph, and at the nature of phase transitions as δ varies. Unlike the dense case, it is hard to give a precise meaning to claims about the conditional structure in the sparse setting due to the lack of an adequate sparse graph limit theory. For a detailed discussion, see [2, 13].

The paper [2] also gives a number of examples where the coeﬃcient c(δ) in Theorem 1.4 can be explicitly computed. For instance, if H = C4, the cycle of length four, then

√

- 1

![image 43](<2014-chatterjee-nonlinear-large-deviations_images/imageFile43.png>)

- 2


![image 44](<2014-chatterjee-nonlinear-large-deviations_images/imageFile44.png>)

δ if δ < 16, −1 + 1 + 21δ if δ ≥ 16.

c(δ) =

![image 45](<2014-chatterjee-nonlinear-large-deviations_images/imageFile45.png>)

![image 46](<2014-chatterjee-nonlinear-large-deviations_images/imageFile46.png>)

Theorem 1.3 is also a special case of Theorem 1.4.

The proof of Theorem 1.2 is a direct application of Theorem 1.1. The main challenge lies in verifying the low complexity gradient condition. In the case of dense graphs, the condition may be veriﬁed using Szemere´di’s lemma. But it turns out that Szemere´di’s lemma is not a strict requirement for proving the low complexity gradient condition for subgraph counts. One can bypass that and use a spectral argument instead. The spectral argument generalizes easily to the sparse case.

Incidentally, as already discussed in Subsection 1.1, the rough order of probability upper tails for subgraph counts drew signiﬁcant interest in the random graphs community for a long time (as indicated in [23]). It was eventually determined in a series of papers by Vu [38, 39], Kim and Vu [28, 29], Janson and Rucin´ski [24] and ﬁnally by Janson, Oleszkiewicz and Rucin´ski [22]. The upper and lower bounds obtained by these authors diﬀered by a logarithmic factor; they were matched in [12, 18] for triangle counts, and for counts of cliques in [19]. The techniques of all of these papers, however, are only suitable for getting the tail decay order and a ﬁrst-order approximation such as the one given in Theorem 1.2 is not achievable by these methods.

- 1.5. Application to arithmetic progressions. Fixing n ∈ N and p ∈ (0,1), let A be a random subset of Z/nZ, constructed by keeping each element with probability p, and dropping with probability 1 − p. In this subsection we apply Theorem 1.1 to compute large deviation probabilities for the number of three-term arithmetic progressions in A. One may be able to tackle longer arithmetic progressions via Theorem 1.1, but this would require ﬁnding a better upper bound on its complexity term.

- Theorem 1.5. Let A be a random subset of Z/nZ, constructed as above. Let X be the number of pairs (i,j) ∈ (Z/nZ)2 such that {i,i + j,i + 2j} ⊆ A. Let Ip be deﬁned as in (1.4) and deﬁne


θp(u) := inf Ip(x) : x ∈ [0,1]Z/nZ

such that

i,j∈Z/nZ

xixi+jxi+2j ≥ uE(X) .

Suppose that n−1/162 ≤ p ≤ 1 − n−1. Then for any u > 1, 1 − cn−1/6p−6 log n ≤

θp(u)

![image 47](<2014-chatterjee-nonlinear-large-deviations_images/imageFile47.png>)

−log P(X ≥ uE(X)) ≤ 1 + Cn−1/29p−162/29(log n)33/29 , where C and c are constants that may depend only on u.

This theorem gives an approximation for the upper tail of the number of three-term arithmetic progressions in random subsets of Z/nZ, even when the random subset is allowed to be somewhat sparse (p ≫ n−1/162(log n)33/162). Note that with p = 1/2, the upper tail probability is proportional to the number of subsets of Z/nZ that contain more than a given number of three-term progressions.

Again, the main challenge in the proof of Theorem 1.5 is in establishing the low complexity gradient condition. Discrete Fourier transform techniques are used to prove that this condition holds for the function f deﬁned above. We believe that the low complexity gradient condition should apply for longer arithmetic progressions, as it may be expected to hold in any situation where some kind of “averaging” is going on; if true, this would extend our solution to longer progressions.

The study of arithmetic progressions in subsets of integers has a long and storied history, most of which is concerned with questions of existence. An excellent survey of old and new results is available in Tao and Vu [37]. Counting the number of sets with a given number of arithmetic progressions, or understanding the typical structure of sets that contain lots of progressions, are challenges of a diﬀerent type, falling within the purview of large deviations theory. Recently a certain amount of interest has begun to grow around the resolution of such questions, quickly leading to the realization that conventional large deviations theory will not provide the answers. The most pertinent papers are the recent articles on probabilistic properties of the so-called “non-conventional averages” by Kifer [25], Kifer and Varadhan [26, 27] and Carinci et al. [9]. In particular, Carinci et al. [9] prove a large deviation principle for what they call “two-term arithmetic progressions”, which are sums of the type xix2i.

- 1.6. Approximation of normalizing constants. Let f be as in Subsection 1.3. Consider a probability measure on {0,1}n that puts mass proportional to ef(x) at each point x. The logarithm of the normalizing constant of this probability measure, sometimes called the “free energy”, is


ef(x) .

F := log

x∈{0,1}n

The free energy is an important object in statistical physics. In this context, the probability measure deﬁned above is called the “Gibbs measure” with Hamiltonian f. The free energy encodes useful information about the structure of the Gibbs measure: it is often used to compute the Gibbs averages of various quantities of interest by diﬀerentiating the free energy with respect to appropriate parameters. Computation of normalizing constants is also important in statistics because it is required for computing maximum likelihood estimates of unknown parameters.

For u ∈ [0,1], deﬁne

I(u) := ulog u + (1 − u)log(1 − u). For x = (x1,... ,xn) ∈ [0,1]n, let

n

I(xi). The goal of this subsection is to investigate conditions on f under which the approximation F = sup

I(x) :=

i=1

(f(x) − I(x)) + lower order terms

x∈[0,1]n

is valid. As expected from the general connection between large deviations and moment generating functions given by Varadhan’s lemma (see in [20]), the validity of the above approximation is closely related to that of (1.6). Incidentally, it is easy to verify that exact equality holds in the above display (without any lower order correction terms) if f is linear.

- Theorem 1.6. Let F be deﬁned as above, and a, bi, cij and D(ǫ) be as in Theorem 1.1. Then for any ǫ > 0,


(f(x) − I(x)) + complexity term + smoothness term, where

F ≤ sup

x∈[0,1]n

n

1 4

1/2

b2i

ǫ + 3nǫ + log |D(ǫ)|, and

n

complexity term =

![image 48](<2014-chatterjee-nonlinear-large-deviations_images/imageFile48.png>)

i=1

n

n

1/2

1 4

(acii + b2i ) +

ac2ij + bibjcij + 4bicij

smoothness term = 4

![image 49](<2014-chatterjee-nonlinear-large-deviations_images/imageFile49.png>)

i=1

i,j=1

n

n

n

1 4

1/2

1/2

c2ii

b2i

+

cii + log 2. Moreover, F satisﬁes the lower bound

+ 3

![image 50](<2014-chatterjee-nonlinear-large-deviations_images/imageFile50.png>)

i=1

i=1

i=1

n

- 1

![image 51](<2014-chatterjee-nonlinear-large-deviations_images/imageFile51.png>)

- 2


(f(x) − I(x)) −

F ≥ sup

cii .

x∈[0,1]n

i=1

Just like Theorem 1.1, it is unlikely that the error terms in Theorem 1.6 are sharp. Still, it is the ﬁrst result of its kind and good enough to be applicable in some examples of interest.

Actually, Theorem 1.1 is proved in this paper as a special application Theorem 1.6. To see how this is done, take a function g : [0,1]n → R and a threshold t ∈ R. Let f be a smooth function such that

0 if g(x) ≥ tn , a large negative number if g(x) < tn − a small quantity.

f(x) =

Then ef(x) is a smooth approximation to the function that is 1 when g(x) ≥ tn and 0 when g(x) < tn. One may now try to apply Theorem 1.6 with this f to ﬁnd an approximation to

P(g(Y ) ≥ tn). This strategy is similar to the one used in Bryc’s proof of the inverse Varadhan lemma (see [20, Section 4.4]).

The usual large deviation technique of obtaining optimal upper bounds using moment generating functions does not seem to work for sparse random graphs. This is the reason why the above scheme is needed for deriving Theorem 1.1 from Theorem 1.6. This is also the main reason why the error bound in Theorem 1.1 is somewhat lossy, leading to the suboptimal conditions on the decay rate of p in Theorems 1.3 and 1.4.

The above sketch indicates that Theorem 1.6 is much more general than Theorem 1.1. Indeed, using a similar tactic it may be used for computing joint large deviations for several functions simultaneously, although we will not pursue this direction here.

- 1.7. Application to exponential random graphs. In this section we will use the notation of


Subsection 1.4. Let l be a positive integer and H1,... ,Hl be ﬁnite simple graphs. Let β1,... ,βl be l real numbers. Let N be another positive integer. Given a simple graph G on N vertices, let t(H,G) denote, as in Subsection 1.4, the homomorphism density of H in G.

Consider the probability measure on the set of all simple graphs on N vertices that puts mass proportional to

exp N2(β1t(H1,G) + ··· + βlt(Hl,G))

on each graph G. This is an example of an exponential random graph model (ERGM). Such models are widely used in the statistical social networks community to understand the structure of networks. One of the key objectives of the practitioners is to compute estimates of the parameters β1,... ,βl from an observed graph, which they assume is drawn from this model. The most popular approach to estimation is the maximum likelihood method. To implement this method, however, one needs to know the normalizing constant of the probability measure.

Until recently, the only available techniques for approximating the normalizing constants of such probability measures all relied on Markov Chain Monte Carlo (MCMC) methods. There are some doubts about the accuracy of such approximations, as pointed out in [1]. The mathematical problem was solved in [15] where it was shown that if ZN is the normalizing constant, then as N goes to inﬁnity (keeping β1,... ,βl ﬁxed),

log ZN N2 ≈ sup

![image 52](<2014-chatterjee-nonlinear-large-deviations_images/imageFile52.png>)

x∈PN

I(x) N2

β1t(H1,x) + ··· + βlt(Hl,x) −

![image 53](<2014-chatterjee-nonlinear-large-deviations_images/imageFile53.png>)

=: LN ,

where PN denotes the set P deﬁned in Subsection 1.4, that is, the set of all x = (xij)1≤i<j≤N with xij ∈ [0,1] for all i,j. Here the approximation sign means that the diﬀerence between the two sides tends to zero. The proof of this theorem is based on the large deviation principle for Erd˝os-Re´nyi graphs from [16]. Since this argument is based on Szemere´di’s lemma, it does not give error bounds that are better than some negative power of log∗ N. Another problem is that this result does not allow varying the β’s with N, making it inapplicable for sparse exponential random graphs.

- Theorem 1.6 solves both problems to a certain extent, by giving a concrete error bound.
- Theorem 1.7. Let ZN and LN be as above. Let B := 1 + |β1| + ··· + |βl|. Then


log ZN N2 − LN

−cBN−1 ≤

![image 54](<2014-chatterjee-nonlinear-large-deviations_images/imageFile54.png>)

log B log N

+ CB2N−1/2 ,

≤ CB8/5N−1/5(log N)1/5 1 +

![image 55](<2014-chatterjee-nonlinear-large-deviations_images/imageFile55.png>)

where C and c are constants that may depend only on H1,... ,Hl.

As an example, consider the case where l = 2, H1 is a single edge, and H2 is a triangle. In this case the above theorem shows that the diﬀerence between N−2 log ZN and LN tends to zero as long as |β1|+|β2| grows slower than N1/8(log N)−1/8, thereby allowing a small degree of sparsity. When the β’s are ﬁxed, it provides an approximation error bound of order N−1/5(log N)1/5, substantially better than the negative powers of log∗ N given by Szemere´di’s lemma. However, the error bound is probably suboptimal. It is an interesting challenge to ﬁgure out a sharp error bound.

As mentioned in the previous subsection, it is in general not possible to pass from estimates for exponential random graphs to large deviations for Erd˝os–Re´nyi graphs by optimizing over the parameters. In fact, this is not possible even in the dense setting. The reason is that exponential random graphs have discontinuous phase transitions — as the parameters vary, the structure of the graph changes abruptly, missing out a range of intermediate structures. For details, see [15].

- 1.8. Open problems. The following is a partial list of questions that are currently beyond the reach of the theory presented in this manuscript, but may be solvable by a more reﬁned theory.


- (1) Improve Theorem 1.1, so that results like Theorem 1.3 and Theorem 1.4 can be proved when p tends to zero at an optimal rate.
- (2) As an example of the above, show that Theorem 1.3 holds when p → 0 slower than n−1/2.
- (3) Develop a sparse regularity lemma and a sparse graph limit theory that is powerful enough to prove results like Theorem 1.3. In fact, a reasonable test for the completeness of a sparse graph limit theory is whether it can lead to a solution of the large deviation question for sparse Erd˝os–Re´nyi random graphs. This is because analyzing the large deviation behavior of G(N,p) for small p requires a full understanding of all possible sparse graph structures rather than focusing a small subset of graphs with nice properties.
- (4) Extend the large deviation results for three-term arithmetic progressions (Theorem 1.5) to longer progressions. In this paper, discrete Fourier analysis is used for the analysis of three-term progressions. The method does not seem to extend easily to longer progressions. It is possible that higher order Fourier analysis (Gowers norms) or a sparse hypergraph regularity lemma may be needed for longer progressions.
- (5) Find explicit solutions to the variational problems coming from arithmetic progressions, in the spirit of Theorems 1.3 and 1.4.
- (6) Improve the result for exponential random graphs (Theorem 1.7) so that sparser graphs can be handled.


2. Proof sketch

In this section we give a sketch of the main ideas behind the proof of Theorem 1.6 and the main ideas behind the proof of the low complexity gradient condition for subgraph counts (which is the key ingredient in the proof of Theorem 1.2). Note that we have already sketched how Theorem 1.1 follows from Theorem 1.6 in Subsection 1.6.

We will generally denote the ith coordinate of a vector x ∈ Rn by xi. Similarly, the ith coordinate of a random vector X will be denoted by Xi.

Let X = (X1,... ,Xn) be a random vector that has probability density proportional to ef(x) on {0,1}n with respect to the counting measure. For each i, deﬁne a function xˆi : [0,1]n → [0,1] as

xˆi(x) = E(Xi | Xj = xj, 1 ≤ j ≤ n, j = i). Let xˆ : [0,1]n → [0,1]n be the vector-valued function whose ith coordinate function is xˆi.

Let Xˆ = xˆ(X). The ﬁrst step in the proof is to show that if the smoothness term in Theorem 1.6 is small, then

f(X) ≈ f(Xˆ) with high probability. (2.1) (We will not bother to make precise the meaning of ≈ in this sketch.) To show this, deﬁne D := f(X) − f(Xˆ) and

h(x) := f(x) − f(ˆx(x)), so that D = h(X). For t ∈ [0,1] and x ∈ [0,1]n, let

ui(t,x) := fi(tx + (1 − t)ˆx(x)), so that

n

1

(xi − xˆi(x))ui(t,x)dt. Thus,

h(x) =

0

i=1

E(D2) =

n

1

E((Xi − Xˆi)ui(t,X)D)dt. (2.2)

0

i=1

Let X(i) denote the random vector (X1,... ,Xi−1,0,Xi+1,... ,Xn). Let Di := h(X(i)). Then note that ui(t,X(i))Di is a function of the random variables (Xj)j =i only. Therefore by the deﬁnition of Xˆi,

E((Xi − Xˆi)ui(t,X(i))Di) = 0. Thus,

E((Xi − Xˆi)ui(t,X)D)

= E((Xi − Xˆi)ui(t,X)D) − E((Xi − Xˆi)ui(t,X(i))Di).

If the smoothness term is small, then one can show that ui(t,X) ≈ ui(t,X(i)) and D ≈ Di. Therefore, the left-hand side of the above identity is close to zero. By (2.2), this proves the

- approximation (2.1). Deﬁne a function g : [0,1]n × [0,1]n → R as


n

(xi log yi + (1 − xi)log(1 − yi)).

g(x,y) :=

i=1

By a similar argument as above, it is possible to show that if the smoothness term is small, then g(X,Xˆ) ≈ g(X,ˆ Xˆ) = I(Xˆ). (2.3)

Armed with (2.1) and (2.3), the proof of Theorem 1.6 may be completed as follows. Let A be the set of all x where f(x) ≈ f(ˆx(x)) and g(x,xˆ(x)) ≈ I(ˆx(x)). By (2.1) and (2.3), X ∈ A with high probability. That is,

x∈A ef(x)

x∈{0,1}n ef(x) ≈ 1. Therefore by the deﬁnition of the set A,

![image 56](<2014-chatterjee-nonlinear-large-deviations_images/imageFile56.png>)

ef(x) ≈ log

F = log

x∈{0,1}n

ef(x) ≈ log

x∈A

ef(ˆx(x))−I(ˆx(x))+g(x,xˆ(x)) . (2.4)

x∈A

The above display is the key to the proof of Theorem 1.6. It was pointed out to us by Alex Zhai that one way to understand this approximation is to see f(ˆx(x)) − I(ˆx(x)) + g(x,xˆ(x)) as an approximately piecewise linear proxy for f(x).

Now let ǫ be a small positive number, close to zero. Using the set D(ǫ), it is easy to produce a set D′(ǫ) ⊆ [0,1]n such that |D(ǫ)| = |D′(ǫ)|, and D′(ǫ) is an ǫ-net for the image of [0,1]n under the map xˆ. That is, for each x there exists p ∈ D′(ǫ) such that

n

(ˆxi(x) − pi)2 ≤ ǫ2n.

i=1

We will say that xˆ(x) ≈ p. For each p ∈ D′(ǫ) let P(p) be the set of all x ∈ {0,1}n such that xˆ(x) ≈ p. Then

ef(ˆx(x))−I(ˆx(x))+g(x,xˆ(x)) (2.5)

log

x∈A

ef(ˆx(x))−I(ˆx(x))+g(x,xˆ(x))

≤ log

p∈D′(ǫ) x∈P(p)

ef(p)−I(p)+g(x,p).

≈ log

p∈D′(ǫ) x∈P(p)

The crucial observation is that for any p ∈ [0,1]n,

eg(x,p) = 1.

x∈{0,1}n

Thus,

ef(p)−I(p)+g(x,p) ≤ log

ef(p)−I(p) (2.6)

log

p∈D′(ǫ) x∈P(p)

p∈D′(ǫ)

≤ log |D′(ǫ)| + sup

(f(p) − I(p)).

p∈[0,1]n

- Combining (2.4), (2.5) and (2.6) completes the proof sketch for the upper bound in Theorem 1.6. The proof of the lower bound may be sketched as follows. Take any y ∈ [0,1]n. Let Y =


(Y1,... ,Yn) be a random vector with independent components, where Yi is a Bernoulli(yi) random variable. Then by Jensen’s inequality,

ef(x) =

ef(x)−g(x,y)+g(x,y)

x∈{0,1}n

x∈{0,1}n

= E(ef(Y )−g(Y,y)) ≥ exp(E(f(Y ) − g(Y,y)))

= exp(E(f(Y )) − I(y)).

Then, by the same line of argument that is used to prove (2.1) and (2.3), one can prove that if the error term in the lower bound is small, then E(f(Y )) ≈ f(y). Since this is true for any y, this completes the sketch of the proof of the lower bound.

Our ﬁnal task in this section is to give a sketch of the proof of the low complexity gradient condition for subgraph counts. For simplicity of exposition, let us just consider the count of

triangles. Let n = N(N −1)/2 and let us agree to denote elements of Rn as x = (xij)1≤i<j≤N, with the convention that xii = 0 and xji = xij. Deﬁne a function f : Rn → R as

N

1 N

xijxjkxki .

f(x) =

![image 57](<2014-chatterjee-nonlinear-large-deviations_images/imageFile57.png>)

i,j,k=1

Then note that

N

∂f ∂xij

3 N

=

xikxjk =: 3aij(x).

![image 58](<2014-chatterjee-nonlinear-large-deviations_images/imageFile58.png>)

![image 59](<2014-chatterjee-nonlinear-large-deviations_images/imageFile59.png>)

k=1

We will now sketch why the numbers aij(x) may be encoded by o(N2) bits. For any x, let M(x) be the square matrix whose (i,j)th entry is xij. Note that for any x and y,

N

1 N2 i,j,k,l

(aij(x) − aij(y))2 =

(xikxjk − yikyjk)(xilxjl − yilyjl).

![image 60](<2014-chatterjee-nonlinear-large-deviations_images/imageFile60.png>)

i,j=1

Let us now expand out the right-hand side and consider one pair of terms: 1

(xikxjkxilxjl − xikxjkyilyjl).

![image 61](<2014-chatterjee-nonlinear-large-deviations_images/imageFile61.png>)

N2 i,j,k,l

This term may be written in a telescoping manner as 1

1 N2 i,j,k,l

xikxjkxil(xjl − yjl) +

xikxjk(xil − yil)yjl .

![image 62](<2014-chatterjee-nonlinear-large-deviations_images/imageFile62.png>)

![image 63](<2014-chatterjee-nonlinear-large-deviations_images/imageFile63.png>)

N2 i,j,k,l

Let us consider the ﬁrst term above. The crucial observation is that if i and k are ﬁxed, then the sum in j and l is a quadratic form of the matrix M(x) − M(y). Upon observing this, it is easy to see that this term is bounded above by

N M(x) − M(y) op ,

where M(x) − M(y) op is the L2 operator norm of the matrix M(x) − M(y). A similar bound may be obtained for all other terms, leading to the conclusion that

(aij(x) − aij(y))2 ≤ CN M(x) − M(y) op , (2.7)

i,j

where C is a universal constant.

Now take any x and let λ1,λ2,... ,λn be the eigenvalues of the symmetric matrix M(x), arranged in decreasing order of magnitude. Then

N

n

x2ij ≤ N2 ,

λ2i = Trace(M(x)2) =

i,j=1

i=1

which implies the important observation that λ2i ≤ N2/i for each i since |λ1| ≥ |λ2| ≥ ··· ≥ |λn|. As a result of this, if M′ is the matrix obtained from M(x) after throwing away the terms corresponding

the λi+1,... ,λn in its spectral decomposition, then M(x) − M′ op ≤

N √i + 1

.

![image 64](<2014-chatterjee-nonlinear-large-deviations_images/imageFile64.png>)

![image 65](<2014-chatterjee-nonlinear-large-deviations_images/imageFile65.png>)

In other words, M(x) may be approximated by a rank i matrix if we allow O(Ni−1/2) error of approximation in the operator norm. But we need only O(Nilog N) bits to encode a rank i matrix. Taking i = ǫ−4, and combining with the inequality (2.7), it is now easy to see how the quantities

aij(x) may be encoded by O(Nǫ−4 log N) bits with O(ǫ) error in approximation for a typical aij, on average. This proves the low complexity gradient condition for triangle counts. The proof for general subgraph counts is a messy but straightforward generalization of the above argument.

3. Proof of Theorem 1.6

In this section, we ﬁll out the gaps in the sketch given in the previous section and thereby produce a complete proof of Theorem 1.6.

Throughout this section, we will freely use the notation of Theorem 1.6. In particular, F, f, fi, fij, a, bi, cij and D(ǫ) are as in the statement of Theorem 1.6. Let us also deﬁne some additional notation, as follows. (Some of this has already been introduced in the previous section, but we will repeat the deﬁnitions here just in case the reader has skipped that part.)

We will generally denote the ith coordinate of a vector x ∈ Rn by xi. Similarly, the ith coordinate of a random vector X will be denoted by Xi. Given x ∈ [0,1]n, deﬁne x(i) to be the vector (x1,... ,xi−1,0,xi+1,... ,xn). For a random vector X deﬁne X(i) similarly. Given a function g : [0,1]n → R, deﬁne the discrete derivative ∆ig as

∆ig(x) := g(x1,... ,xi−1,1,xi+1,... ,xn) − g(x1,... ,xi−1,0,xi+1,... ,xn). For each i, deﬁne a function xˆi : [0,1]n → [0,1] as

1 1 + e−∆if(x).

xˆi(x) =

![image 66](<2014-chatterjee-nonlinear-large-deviations_images/imageFile66.png>)

Let xˆ : [0,1]n → [0,1]n be the vector-valued function whose ith coordinate function is xˆi. When the vector x is understood from the context, we will simply write xˆ and xˆi instead of xˆ(x) and xˆi(x). The proof of Theorem 1.6 requires two key lemmas.

- Lemma 3.1. Let X = (X1,... ,Xn) be a random vector that has probability density proportional to ef(x) on {0,1}n with respect to the counting measure. Let Xˆ = xˆ(X). Then


n

n

1 4

E (f(X) − f(Xˆ))2 ≤

(acii + b2i) +

ac2ij + bibjcij .

![image 67](<2014-chatterjee-nonlinear-large-deviations_images/imageFile67.png>)

i=1

i,j=1

Proof. It is easy to see that

xˆi(x) = E(Xi | Xj = xj, 1 ≤ j ≤ n, j = i). Let D := f(X) − f(Xˆ). Then clearly

|D| ≤ 2a. (3.1) Deﬁne

h(x) := f(x) − f(ˆx(x)), so that D = h(X). Note that for i = j,

∂xˆj ∂xi

=

![image 68](<2014-chatterjee-nonlinear-large-deviations_images/imageFile68.png>)

e−∆jf(x) (1 + e−∆jf(x))2

![image 69](<2014-chatterjee-nonlinear-large-deviations_images/imageFile69.png>)

1

fij(x1,... ,xj−1,t,xj+1,... ,xn)dt,

0

and for i = j, the above derivative is identically equal to zero. Since e−x/(1 + e−x)2 ≤ 1/4 for all x ∈ R, this shows that for all i and j,

cij 4

∂xˆj ∂xi ≤

. (3.2)

![image 70](<2014-chatterjee-nonlinear-large-deviations_images/imageFile70.png>)

![image 71](<2014-chatterjee-nonlinear-large-deviations_images/imageFile71.png>)

Thus,

n

∂h ∂xi ≤ fi +

fj

![image 72](<2014-chatterjee-nonlinear-large-deviations_images/imageFile72.png>)

j=1

n

1 4

≤ bi +

bjcij.

![image 73](<2014-chatterjee-nonlinear-large-deviations_images/imageFile73.png>)

j=1

∂xˆj ∂xi

![image 74](<2014-chatterjee-nonlinear-large-deviations_images/imageFile74.png>)

(3.3)

Consequently, if Di := h(X(i)), then

n

1 4

|D − Di| ≤ bi +

bjcij. (3.4)

![image 75](<2014-chatterjee-nonlinear-large-deviations_images/imageFile75.png>)

j=1

For t ∈ [0,1] and x ∈ [0,1]n deﬁne

ui(t,x) := fi(tx + (1 − t)ˆx), so that

n

1

(xi − xˆi)ui(t,x)dt. Thus,

h(x) =

0

i=1

n

1

E((Xi − Xˆi)ui(t,X)D)dt. (3.5) Now,

E(D2) =

0

i=1

ui ≤ bi, (3.6) and by (3.2),

n

∂xˆj ∂xi

∂ui ∂xi ≤ t fii + (1 − t)

fij

(3.7)

![image 76](<2014-chatterjee-nonlinear-large-deviations_images/imageFile76.png>)

![image 77](<2014-chatterjee-nonlinear-large-deviations_images/imageFile77.png>)

j=1

n

1 − t 4

c2ij.

≤ tcii +

![image 78](<2014-chatterjee-nonlinear-large-deviations_images/imageFile78.png>)

j=1

The bounds (3.1), (3.4), (3.6) and (3.7) imply that E((Xi − Xˆi)ui(t,X)D) − E((Xi − Xˆi)ui(t,X(i))Di) ≤ E ui(t,X) − ui(t,X(i)) D + E ui(t,X(i))(D − Di)

n

n

a(1 − t) 2

1 4

c2ij + b2i +

≤ 2atcii +

bibjcij.

![image 79](<2014-chatterjee-nonlinear-large-deviations_images/imageFile79.png>)

![image 80](<2014-chatterjee-nonlinear-large-deviations_images/imageFile80.png>)

j=1

j=1

But ui(t,X(i))Di is a function of the random variables (Xj)j =i only. Therefore by the deﬁnition of Xˆi,

E((Xi − Xˆi)ui(t,X(i))Di) = 0. Thus,

n

n

a(1 − t) 2

1 4

E((Xi − Xˆi)ui(t,X)D) ≤ 2atcii +

c2ij + b2i +

bibjcij.

![image 81](<2014-chatterjee-nonlinear-large-deviations_images/imageFile81.png>)

![image 82](<2014-chatterjee-nonlinear-large-deviations_images/imageFile82.png>)

j=1

j=1

Using this bound in (3.5) gives E(D2) ≤

n

n

1

a(1 − t) 2

1 4

c2ij + b2i +

2atcii +

![image 83](<2014-chatterjee-nonlinear-large-deviations_images/imageFile83.png>)

![image 84](<2014-chatterjee-nonlinear-large-deviations_images/imageFile84.png>)

0

j=1

i=1

n

n

1 4

(acii + b2i) +

ac2ij + bibjcij , completing the proof.

=

![image 85](<2014-chatterjee-nonlinear-large-deviations_images/imageFile85.png>)

i=1

i,j=1

n

bibjcij dt

j=1

- Lemma 3.2. Let all notation be as in Lemma 3.1. Then


n

n

2

1 4

(Xi − Xˆi)∆if(X)

b2i +

≤

E

![image 86](<2014-chatterjee-nonlinear-large-deviations_images/imageFile86.png>)

i=1

i=1

n

bi(bj + 4)cij.

i,j=1

Proof. Let gi denote the function ∆if, for notational simplicity. Note that gi(x) =

1

fi(x1,... ,xi−1,t,xi+1,... ,xn)dt, which shows that

0

gi ≤ fi = bi (3.8) and for all j,

∂gi ∂xj ≤ fij = cij. (3.9)

![image 87](<2014-chatterjee-nonlinear-large-deviations_images/imageFile87.png>)

Let

n

(xi − xˆi(x))gi(x). Then

G(x) :=

i=1

n

∂xˆj ∂xi

∂gj ∂xi

∂G ∂xi

1{j=i} −

gj(x) + (xj − xˆj)

=

![image 88](<2014-chatterjee-nonlinear-large-deviations_images/imageFile88.png>)

![image 89](<2014-chatterjee-nonlinear-large-deviations_images/imageFile89.png>)

![image 90](<2014-chatterjee-nonlinear-large-deviations_images/imageFile90.png>)

j=1

and therefore by (3.2), (3.8) and (3.9), ∂G ∂xi ≤ bi +

n

1 4

![image 91](<2014-chatterjee-nonlinear-large-deviations_images/imageFile91.png>)

![image 92](<2014-chatterjee-nonlinear-large-deviations_images/imageFile92.png>)

j=1

cijbj +

n

cij. (3.10)

j=1

Note that for any x,

∂G ∂xi

|G(x) − G(x(i))| ≤

. (3.11)

![image 93](<2014-chatterjee-nonlinear-large-deviations_images/imageFile93.png>)

Again, gi(X) and G(X(i)) are both functions of (Xj)j =i only. Therefore E((Xi − Xˆi)gi(X)G(X(i))) = 0. (3.12)

- Combining (3.10), (3.11) and (3.12) gives


n

E((Xi − Xˆi)gi(X)G(X))

E(G(X)2) =

i=1

n

n

n

1 4

≤

bi bi +

cij .

cijbj +

![image 94](<2014-chatterjee-nonlinear-large-deviations_images/imageFile94.png>)

i=1

j=1

j=1

This completes the proof of the lemma.

With the aid of Lemma 3.1 and 3.2, we are now ready to prove Theorem 1.6. Proof of the upper bound in Theorem 1.6. For x,y ∈ [0,1]n, let

n

(xi log yi + (1 − xi)log(1 − yi)).

g(x,y) :=

i=1

Note that

n

n

xˆi 1 − xˆi

(xi − xˆi)log

g(x,xˆ) − I(ˆx) =

(xi − xˆi)∆if(x). (3.13) Let

=

![image 95](<2014-chatterjee-nonlinear-large-deviations_images/imageFile95.png>)

i=1

i=1

n

n

1/2

1 4

(acii + b2i) +

ac2ij + bibjcij + 4bicij

.

B := 4

![image 96](<2014-chatterjee-nonlinear-large-deviations_images/imageFile96.png>)

i=1

i,j=1

Let

- A1 := {x ∈ {0,1}n : |I(ˆx) − g(x,xˆ)| ≤ B/2},

and

- A2 := x ∈ {0,1}n : |f(x) − f(ˆx)| ≤ B/2 .


Let A = A1 ∩ A2. By Lemma 3.2 and the identity (3.13), P(X  ∈ A1) ≤ 1/4. By Lemma 3.1, P(X  ∈ A2) ≤ 1/4. Thus,

- 1

![image 97](<2014-chatterjee-nonlinear-large-deviations_images/imageFile97.png>)

- 2


P(X ∈ A) ≥

. That is,

x∈A ef(x) x∈{0,1}n ef(x) ≥

- 1

![image 98](<2014-chatterjee-nonlinear-large-deviations_images/imageFile98.png>)

- 2


, and therefore by the deﬁnition of the set A,

![image 99](<2014-chatterjee-nonlinear-large-deviations_images/imageFile99.png>)

ef(x) ≤ log

F = log

x∈{0,1}n

ef(x) + log 2 (3.14)

x∈A

ef(ˆx)−I(ˆx)+g(x,xˆ) + log 2.

≤ B + log

x∈A

Now take some x ∈ [0,1]n and let d satisfy (1.7). Then by the Cauchy-Schwarz inequality,

n

|fi(x) − di| ≤ nǫ.

i=1

Fix such an x and d. Note that for each i,

1

|fi(x1,... ,xi−1,t,xi+1,... ,xn) − fi(x)|dt ≤ fii = cii.

|∆if(x) − fi(x)| ≤

0

By the last two inequalities and (1.7),

n

|∆if(x) − di| ≤ nǫ +

i=1

n

cii. (3.15)

i=1

and n

n

1/2

1/2

c2ii

≤ n1/2ǫ +

(∆if(x) − di)2

. (3.16) Let u(x) = 1/(1 + e−x). Note that for all x,

i=1

i=1

1 (ex/2 + e−x/2)2 ≤

1 4

|u′(x)| =

. Therefore if a vector p = p(d) is deﬁned as pi = u(di), then by (3.16),

![image 100](<2014-chatterjee-nonlinear-large-deviations_images/imageFile100.png>)

![image 101](<2014-chatterjee-nonlinear-large-deviations_images/imageFile101.png>)

n

n

1/2

1/2

1 16

(ˆxi − pi)2

(∆if(x) − di)2

≤

![image 102](<2014-chatterjee-nonlinear-large-deviations_images/imageFile102.png>)

i=1

i=1

n

n1/2ǫ 4

1 4

1/2

c2ii

≤

.

+

![image 103](<2014-chatterjee-nonlinear-large-deviations_images/imageFile103.png>)

![image 104](<2014-chatterjee-nonlinear-large-deviations_images/imageFile104.png>)

i=1

Thus, if

n

1/2

b2i

, then

L :=

i=1

n

1/2

(ˆxi − pi)2

|f(ˆx) − f(p)| ≤ L

(3.17)

i=1

n

Ln1/2ǫ 4

L 4

1/2

c2ii

≤

.

+

![image 105](<2014-chatterjee-nonlinear-large-deviations_images/imageFile105.png>)

![image 106](<2014-chatterjee-nonlinear-large-deviations_images/imageFile106.png>)

i=1

Next, let v(x) = log(1 + e−x). Then for all x, |v′(x)| =

e−x

1 + e−x ≤ 1. Consequently,

![image 107](<2014-chatterjee-nonlinear-large-deviations_images/imageFile107.png>)

|log xˆi − log pi| ≤ |∆if(x) − di| and

|log(1 − xˆi) − log(1 − pi)| ≤ |∆if(x) − di|. Therefore by (3.15),

n

n

|∆if(x) − di| ≤ 2nǫ + 2

|g(x,xˆ) − g(x,p)| ≤ 2

cii. (3.18) Finally, let w(x) = I(u(x)). Then

i=1

i=1

w′(x) = u′(x)I′(u(x))

e−x (1 + e−x)2

u(x) 1 − u(x)

=

log

![image 108](<2014-chatterjee-nonlinear-large-deviations_images/imageFile108.png>)

![image 109](<2014-chatterjee-nonlinear-large-deviations_images/imageFile109.png>)

xe−x (1 + e−x)2

. Thus, for all x,

=

![image 110](<2014-chatterjee-nonlinear-large-deviations_images/imageFile110.png>)

|x|e−x (1 + e−x)2 ≤ sup

1 e

xe−x =

|w′(x)| ≤ sup x∈R

.

![image 111](<2014-chatterjee-nonlinear-large-deviations_images/imageFile111.png>)

![image 112](<2014-chatterjee-nonlinear-large-deviations_images/imageFile112.png>)

x≥0

Thus,

1 e|∆if(x) − di|,

|I(ˆxi) − I(pi)| ≤

![image 113](<2014-chatterjee-nonlinear-large-deviations_images/imageFile113.png>)

and so by (3.15),

n

1 e

nǫ e

|I(ˆx) − I(p)| ≤

+

cii. (3.19)

![image 114](<2014-chatterjee-nonlinear-large-deviations_images/imageFile114.png>)

![image 115](<2014-chatterjee-nonlinear-large-deviations_images/imageFile115.png>)

i=1

For each d ∈ D(ǫ) let C(d) be the set of all x ∈ {0,1}n such that (1.7) holds, and let p(d) be the vector p deﬁned above. Then by (3.17), (3.18) and (3.19),

ef(ˆx)−I(ˆx)+g(x,xˆ) ≤ log

ef(ˆx)−I(ˆx)+g(x,xˆ) (3.20)

log

x∈A

d∈D(ǫ) x∈C(d)

n

n

n

Ln1/2ǫ 4

nǫ e

L 4

1 e

1/2

c2ii

≤

cii +

+ 2nǫ + 2

cii

+

+

![image 116](<2014-chatterjee-nonlinear-large-deviations_images/imageFile116.png>)

![image 117](<2014-chatterjee-nonlinear-large-deviations_images/imageFile117.png>)

![image 118](<2014-chatterjee-nonlinear-large-deviations_images/imageFile118.png>)

![image 119](<2014-chatterjee-nonlinear-large-deviations_images/imageFile119.png>)

i=1

i=1

i=1

ef(p(d))−I(p(d))+g(x,p(d)).

+ log

d∈D(ǫ) x∈C(d)

Now note that for any p ∈ [0,1]n,

Thus,

eg(x,p) = 1.

x∈{0,1}n

log

ef(p(d))−I(p(d))+g(x,p(d)) (3.21)

d∈D(ǫ) x∈C(d)

ef(p(d))−I(p(d))

≤ log

d∈D(ǫ)

≤ log |D(ǫ)| + sup

(f(p) − I(p)).

p∈[0,1]n

Combining (3.14), (3.20) and (3.21), the proof is complete.

Proof of the lower bound in Theorem 1.6. Fix some y ∈ [0,1]n. Let Y = (Y1,... ,Yn) be a random vector with independent components, where Yi is a Bernoulli(yi) random variable. Then by Jensen’s inequality,

ef(x) =

ef(x)−g(x,y)+g(x,y)

x∈{0,1}n

x∈{0,1}n

= E(ef(Y )−g(Y,y)) ≥ exp(E(f(Y ) − g(Y,y)))

= exp(E(f(Y )) − I(y)).

- Let S := f(Y ) − f(y). For t ∈ [0,1] and x ∈ [0,1]n deﬁne vi(t,x) := fi(tx + (1 − t)y),


so that

n

1

(Yi − yi)vi(t,Y )dt. (3.22)

S =

0

i=1

By the independence of Yi and Y (i), E((Yi − yi)vi(t,Y )) = E((Yi − yi)(vi(t,Y ) − vi(t,Y (i)))) ≤

∂vi ∂xi ≤ tcii .

![image 120](<2014-chatterjee-nonlinear-large-deviations_images/imageFile120.png>)

Using this bound in (3.22) gives

This completes the proof.

E(S) ≥ −

n

1

- 1

![image 121](<2014-chatterjee-nonlinear-large-deviations_images/imageFile121.png>)

- 2


tcii dt = −

0

i=1

n

cii .

i=1

4. Proof of Theorem 1.1 Throughout this section, we will use the notation of Theorem 1.1 without explicit mention.

Proof of the upper bound in Theorem 1.1. Let h : R → R be a function that is twice continuously diﬀerentiable, non-decreasing, and satisﬁes h(x) = −1 if x ≤ −1 and h(x) = 0 if x ≥ 0. Let L1 :=

h′ and L2 := h′′ . A speciﬁc choice of h is given by h(x) = 10(x+1)3 −15(x+1)4 +6(x+1)5 −1 for −1 ≤ x ≤ 0, which gives L1 ≤ 2 and L2 ≤ 6. Deﬁne

ψ(x) := Kh((x − t)/δ). Then clearly

L2K δ2

L1K δ

, ψ′′ ≤

ψ ≤ K, ψ′ ≤

. Let

![image 122](<2014-chatterjee-nonlinear-large-deviations_images/imageFile122.png>)

![image 123](<2014-chatterjee-nonlinear-large-deviations_images/imageFile123.png>)

n

(xi log p + (1 − xi)log(1 − p)).

g(x) := nψ(f(x)/n) +

i=1

The plan is to apply Theorem 1.6 to the function g instead of f. Note that ψ(x) = 0 if x ≥ t. Thus,

P(f(Y ) ≥ tn) ≤ E(enψ(f(Y )/n)) =

eg(x) .

x∈{0,1}n

Note also that for any x ∈ [0,1]n such that f(x) ≥ tn,

g(x) − I(x) = nψ(f(x)/n) − Ip(x) = −Ip(x) ≤ −φp(t). Again, if f(x) ≤ (t − δ)n, then (f(x)/n − t)/δ ≤ −1, and so

g(x) − I(x) = −nK − Ip(x) ≤ −nK = −φp(t). Finally, note that if f(x) = (t − δ′)n for some 0 < δ′ < δ, then

g(x) − I(x) ≤ −Ip(x) ≤ −φp(t − δ′) ≤ −φ(t − δ). Thus,

(g(x) − I(x)) ≤ −φp(t − δ). Let Cp := |log p| + |log(1 − p)|. Note that

sup

x

g ≤ nK + nCp = α,

and for any i,

2Kbi δ

∂g ∂xi ≤

+ Cp = βi , and for any i,j,

![image 124](<2014-chatterjee-nonlinear-large-deviations_images/imageFile124.png>)

![image 125](<2014-chatterjee-nonlinear-large-deviations_images/imageFile125.png>)

∂2g ∂xi∂xj ≤

2Kcij δ

6Kbibj nδ2

= γij . Next, ﬁx some ǫ > 0 and let D(ǫ) be as in Section 3. Let

+

![image 126](<2014-chatterjee-nonlinear-large-deviations_images/imageFile126.png>)

![image 127](<2014-chatterjee-nonlinear-large-deviations_images/imageFile127.png>)

![image 128](<2014-chatterjee-nonlinear-large-deviations_images/imageFile128.png>)

ǫ 2 n 1 ni=1 b2i 1/2

ǫ 2 ψ′

ǫ′ :=

, τ :=

.

![image 129](<2014-chatterjee-nonlinear-large-deviations_images/imageFile129.png>)

![image 130](<2014-chatterjee-nonlinear-large-deviations_images/imageFile130.png>)

![image 131](<2014-chatterjee-nonlinear-large-deviations_images/imageFile131.png>)

Let l ∈ Rn be the vector whose coordinates are all equal to log(p/(1 − p)) and deﬁne D′(ǫ) := {θd + l : d ∈ D(ǫ′), θ = jτ for some integer 0 ≤ j < ψ′ /τ}.

Let gi := ∂g/∂xi. Take any x ∈ [0,1]n, and choose d ∈ D(ǫ) satisfying (1.7). Choose an integer j between 0 and ψ′ /τ such that |ψ′(f(x)/n) − jτ| ≤ τ. Let d′ := jτd + l, so that d′ ∈ D′(ǫ). Then

n

n

(ψ′(f(x)/n)fi(x) − jτdi)2

(gi(x) − d′i)2 =

i=1

i=1

n

n

(fi(x) − di)2

fi(x)2 + 2 ψ′ 2

≤ 2(ψ′(f(x)/n) − jτ)2

i=1

i=1

n

b2i + 2 ψ′ 2nǫ′2 = nǫ2. This shows that D′(ǫ) plays the role of D(ǫ) for the function g. Note that |D′(ǫ)| ≤

≤ 2τ2

i=1

ψ′ τ |D(ǫ′)|.

![image 132](<2014-chatterjee-nonlinear-large-deviations_images/imageFile132.png>)

This gives the upper bound on the complexity term for the function g. The proof is completed by applying Theorem 1.6.

Proof of the lower bound in Theorem 1.1. Fix any z ∈ [0,1]n such that

f(z) ≥ (t + δ0)n. Let Z = (Z1,... ,Zn) be a random vector with independent components, where Zi ∼ Bernoulli(zi). Let A be the set of all x ∈ {0,1}n such that f(x) ≥ tn. Let A′ be the subset of A where |g(x,z) − g(x,p) − Ip(z)| ≤ ǫ0n. Then

eg(x,p) (4.1)

P(f(Y ) ≥ tn) =

x∈A

eg(x,p)−g(x,z)+g(x,z)

=

x∈A

eg(x,p)−g(x,z)+g(x,z) ≥ e−Ip(z)−ǫ0nP(Z ∈ A′).

≥

x∈A′

Note that

E(g(Z,z) − g(Z,p)) = Ip(z),

and

Var(g(Z,z) − g(Z,p))

n

Var(Zi log(zi/p) + (1 − Zi)log((1 − zi)/(1 − p)))

=

i=1

n

2

zi/p (1 − zi)/(1 − p)

zi(1 − zi) log

.

=

![image 133](<2014-chatterjee-nonlinear-large-deviations_images/imageFile133.png>)

i=1

√xlog x| ≤ 2/e ≤ 1 and x(1 − x) ≤ 1/4, we see that for any x ∈ [0,1],

Using the inequalities |

![image 134](<2014-chatterjee-nonlinear-large-deviations_images/imageFile134.png>)

2

x/p (1 − x)/(1 − p)

x(1 − x) log

![image 135](<2014-chatterjee-nonlinear-large-deviations_images/imageFile135.png>)

2

√1 − xlog(1 − x)| +

√xlog x| + |

p 1 − p

- 1

![image 136](<2014-chatterjee-nonlinear-large-deviations_images/imageFile136.png>)

- 2


![image 137](<2014-chatterjee-nonlinear-large-deviations_images/imageFile137.png>)

![image 138](<2014-chatterjee-nonlinear-large-deviations_images/imageFile138.png>)

≤ |

log

![image 139](<2014-chatterjee-nonlinear-large-deviations_images/imageFile139.png>)

2

- 1

![image 140](<2014-chatterjee-nonlinear-large-deviations_images/imageFile140.png>)

- 2


p 1 − p

≤ 2 +

. Combining the last three displays, we see that

log

![image 141](<2014-chatterjee-nonlinear-large-deviations_images/imageFile141.png>)

2

1 ǫ20n

p 1 − p

1 4

- 1

![image 142](<2014-chatterjee-nonlinear-large-deviations_images/imageFile142.png>)

- 2


P(|g(Z,z) − g(Z,p) − Ip(z)| > ǫ0n) ≤

. (4.2)

log

=

2 +

![image 143](<2014-chatterjee-nonlinear-large-deviations_images/imageFile143.png>)

![image 144](<2014-chatterjee-nonlinear-large-deviations_images/imageFile144.png>)

![image 145](<2014-chatterjee-nonlinear-large-deviations_images/imageFile145.png>)

- Let S := f(Z)−f(z) and vi(t,x) := fi(tZ +(1−t)z). Let Si := f(Z(i))−f(z), so that |S −Si| ≤ bi. Since


n

1

(Zi − zi)vi(t,Z)dt, we have

S =

0

i=1

n

1

E(S2) =

E((Zi − zi)vi(t,Z)S)dt. (4.3)

0

i=1

By the independence of Zi and the pair (Si,Z(i)), E((Zi − zi)vi(t,Z)S)

= E((Zi − zi)(vi(t,Z)S − vi(t,Z(i))Si)) ≤ S

∂vi ∂xi

+ vi S − Si ≤ 2atcii + b2i .

![image 146](<2014-chatterjee-nonlinear-large-deviations_images/imageFile146.png>)

By (4.3), this gives

n

(acii + b2i ). Therefore,

E(S2) ≤

i=1

1 δ02n2

P(f(Z) < tn) ≤

![image 147](<2014-chatterjee-nonlinear-large-deviations_images/imageFile147.png>)

n

(acii + b2i ) =

i=1

1 4

. (4.4)

![image 148](<2014-chatterjee-nonlinear-large-deviations_images/imageFile148.png>)

Inequalities (4.2) and (4.4) give

1 2

P(Z ∈ A′) ≥

. Plugging this into (4.1) and taking supremum over z completes the proof.

![image 149](<2014-chatterjee-nonlinear-large-deviations_images/imageFile149.png>)

5. Proof of Theorem 1.2 Let all notation be the same as in the statement of Theorem 1.2. Let n :=

N 2

. Throughout this section, we will index the elements of Rn as x = (xij)1≤i<j≤N ,

with the understanding that if i < j, then xji is the same as xij, and for all i, xii = 0. Let k be a positive integer, and let H be a ﬁnite simple graph on the vertex set [k] := {1,... ,k}. Let E be the set of edges of H and let m := |E|.

Deﬁne a function T : [0,1]n → R as T(x) :=

1 Nk−2

xqlql′ , (5.1)

![image 150](<2014-chatterjee-nonlinear-large-deviations_images/imageFile150.png>)

q∈[N]k {l,l′}∈E

so that t(H,Gx) = T(x)/N2. The plan is to apply Theorem 1.1 with f = T. We will now compute the required bounds for the function T.

- Lemma 5.1. For the function T on Rn deﬁned above, T ≤ N2, and for any i < j and i′ < j′, ∂T


∂xij ≤ 2m, and

![image 151](<2014-chatterjee-nonlinear-large-deviations_images/imageFile151.png>)

∂2T ∂xij∂xi′j′

- 4m(m − 1)N−1 if |{i,j,i′,j′}| = 2 or 3 ,
- 4m(m − 1)N−2 if |{i,j,i′,j′}| = 4 .


≤

![image 152](<2014-chatterjee-nonlinear-large-deviations_images/imageFile152.png>)

Proof. It is clear that T ≤ N2 since the xij’s are all in [0,1] and there are exactly Nk terms in the sum that deﬁnes T. Next, note that for any i < j,

1 Nk−2

∂T ∂xij

xqlql′ , (5.2)

=

![image 153](<2014-chatterjee-nonlinear-large-deviations_images/imageFile153.png>)

![image 154](<2014-chatterjee-nonlinear-large-deviations_images/imageFile154.png>)

{a,b}∈E q∈[N]k {qa,qb}={i,j}

{l,l′}∈E {l,l′} ={a,b}

and therefore

2mNk−2 Nk−2

∂T ∂xij ≤

= 2m. Next, for any i < j and i′ < j′,

![image 155](<2014-chatterjee-nonlinear-large-deviations_images/imageFile155.png>)

![image 156](<2014-chatterjee-nonlinear-large-deviations_images/imageFile156.png>)

∂2T ∂xij∂xi′j′

1 Nk−2

=

xqlql′ .

![image 157](<2014-chatterjee-nonlinear-large-deviations_images/imageFile157.png>)

![image 158](<2014-chatterjee-nonlinear-large-deviations_images/imageFile158.png>)

q∈[N]k {qa,qb}={i,j} {qc,qd}={i′,j′}

{l,l′}∈E {l,l′} ={a,b} {l,l′} ={c,d}

{a,b}∈E {c,d}∈E {c,d} ={a,b}

Take any two edges {a,b},{c,d} ∈ E such that {a,b} = {c,d}. Then the number of choices of q ∈ [N]k such that {qa,qb} = {i,j} and {qc,qd} = {i′,j′} is at most 4Nk−3 if |{i,j,i′,j′}| = 2 or 3 (since we are constraining qa, qb, qc and qd and |{a,b,c,d}| ≥ 3 always), and at most 4Nk−4 if

|{i,j,i′,j′}| = 4 (since |{a,b,c,d}| must be 4 if there is at least one possible choice of q for these i,j,i′,j′). This gives the upper bound for the second derivatives.

- Lemma 5.2. For the function T deﬁned above, one can produce sets D(ǫ) satisfying the criterion (1.7) (with f = T) such that

|D(ǫ)| ≤ exp

C1m4k4N ǫ4

![image 159](<2014-chatterjee-nonlinear-large-deviations_images/imageFile159.png>)

log

C2m4k4 ǫ4

![image 160](<2014-chatterjee-nonlinear-large-deviations_images/imageFile160.png>)

,

where C1 and C2 are universal constants.

The proof of Lemma 5.2 requires some preparation. We begin by introducing some special notation. For an N × N matrix M, recall the deﬁnition of the operator norm:

M op := max{ Mx : x ∈ RN , x = 1}.

For x = (xij)1≤i<j≤N ∈ Rn, let M(x) be the symmetric matrix whose (i,j)th entry is xij, with the convention that xij = xji and xii = 0. Deﬁne the operator norm on Rn as

x op := M(x) op. The following lemma estimates the entropy of the unit cube under this norm.

- Lemma 5.3. For any τ ∈ (0,1), there is a ﬁnite set of N × N matrices W(τ) such that |W(τ)| ≤ e34(N/τ2) log(51/τ2) ,


and for any N × N matrix M with entries in [0,1], there exists W ∈ W(τ) such that M − W op ≤ Nτ . In particular, for any x ∈ [0,1]n there exists W ∈ W(τ) such that M(x) − W op ≤ Nτ.

Proof. Let l be the integer part of 17/τ2 and δ = 1/l. Let A be a ﬁnite subset of the unit ball of RN such that any vector inside the ball is at Euclidean distance ≤ δ from some element of A. (In other words, A is a δ-net of the unit ball under the Euclidean metric.) The set A may be deﬁned as a maximal set of points in the unit ball such that any two are at a distance greater than δ from each other. Since the balls of radius δ/2 around these points are disjoint and their union is contained in the ball of radius 1 + δ/2 centered at zero, it follows that |A|C(δ/2)N ≤ C(1 + δ/2)N, where C is the volume of the unit ball. Therefore,

|A| ≤ (3/δ)N. (5.3) Take any x ∈ Rn. Suppose that M has singular value decomposition

n

λiuivit ,

M =

i=1

where λ1 ≥ λ2 ≥ ··· λn ≥ 0 are the singular values of M, and u1,... ,un and v1,... ,vn are singular vectors, and vit denotes the transpose of the column vector vi. Assume that the ui’s and vi’s are orthonormal systems. Since the elements of M all belong to the interval [0,1], it is easy to see that λ1 ≤ N and λ2i ≤ N2. Due to the second inequality, there exists y ∈ A such that

N

(N−1λi − yi)2 ≤ δ2. (5.4)

i=1

Let z1,... ,zN and w1,... ,wN be elements of A such that for each i,

N

N

(vij − wij)2 ≤ δ2 , (5.5)

(uij − zij)2 ≤ δ2 and

j=1

j=1

where uij denotes the jth component of the vector ui, etc. Deﬁne two matrices V and W as

l−1

λiuivit and W :=

V :=

i=1

l−1

Nyiziwit .

i=1

Note that since λ2i ≤ N2 and λi decreases with i, therefore for each i, λ2i ≤ N2/i. Thus, M − W op ≤ M − V op + V − W op ≤

N √

+ V − W op.

![image 161](<2014-chatterjee-nonlinear-large-deviations_images/imageFile161.png>)

![image 162](<2014-chatterjee-nonlinear-large-deviations_images/imageFile162.png>)

l

Next, note that by (5.5), the operator norms of the rank-one matrices (ui − zi)vit and zi(vi − wi)t are bounded by δ. And by (5.4), |λi − Nyi| ≤ Nδ for each i. Therefore

l−1

l−1

(λi − Nyi)uivit

Nyi(ui − zi)vit

V − W op ≤

+

op

op

i=1

i=1

l−1

Nyizi(vi − wi)t

+

op

i=1

l−1

N|yi|δ

≤ max

|λi − Nyi| + 2

1≤i≤l−1

i=1

l−1

1/2

√

3N √

yi2

![image 163](<2014-chatterjee-nonlinear-large-deviations_images/imageFile163.png>)

≤ Nδ + 2Nδ

≤ Nδ + 2Nδ (l − 1)

l − 1 ≤

.

![image 164](<2014-chatterjee-nonlinear-large-deviations_images/imageFile164.png>)

![image 165](<2014-chatterjee-nonlinear-large-deviations_images/imageFile165.png>)

l

i=1

Thus,

4N √

4N

4N

M − W op ≤

l ≤

≤

= Nτ.

![image 166](<2014-chatterjee-nonlinear-large-deviations_images/imageFile166.png>)

![image 167](<2014-chatterjee-nonlinear-large-deviations_images/imageFile167.png>)

![image 168](<2014-chatterjee-nonlinear-large-deviations_images/imageFile168.png>)

![image 169](<2014-chatterjee-nonlinear-large-deviations_images/imageFile169.png>)

![image 170](<2014-chatterjee-nonlinear-large-deviations_images/imageFile170.png>)

![image 171](<2014-chatterjee-nonlinear-large-deviations_images/imageFile171.png>)

17 τ2 − 1

16 τ2

![image 172](<2014-chatterjee-nonlinear-large-deviations_images/imageFile172.png>)

![image 173](<2014-chatterjee-nonlinear-large-deviations_images/imageFile173.png>)

Let W(τ) be the set of all possible W’s constructed in the above manner. Then W(τ) has the required property, and by (5.3),

|W(τ)| ≤ The number of ways of choosing y,z1,... ,zl−1,w1,... ,wl−1 ∈ A

= |A|2l−1 ≤ (3/δ)2Nl = e2Nllog(3l). This completes the proof of the lemma.

Let r be a positive integer. Let Kr be the complete graph on the vertex set {1,... ,r}. For any set of edges A of Kr, any q = (q1,... ,qr) ∈ [N]r, and any x ∈ [0,1]n, let

P(x,q,A) :=

xqaqb ,

{a,b}∈A

with the usual convention that the empty product is 1. Note that if qa = qb for some {a,b} ∈ A, the P(x,q,A) = 0 due to our convention that xii = 0 for each i. Next, note that if A and B are disjoint sets of edges, then

P(x,q,A ∪ B) = P(x,q,A)P(x,q,B). (5.6)

- Lemma 5.4. Let A and B be sets of edges of Kr, and let e = {α,β} be an edge that is neither in

- A nor in B. Then for any x,y ∈ [0,1]n,

q∈[N]r

P(x,q,A)P(y,q,B)(xqαqβ − yqαqβ) ≤ Nr−1 x − y op.

Proof. By relabeling the vertices of Kr and redeﬁning A and B, we may assume that α = 1 and β = 2.

Let A1 be the set of all edges in A that are incident to 1. Let A2 be the set of all edges in A that are incident to 2. Note that since {1,2}  ∈ A, therefore A1 and A2 must be disjoint. Similarly, let

- B1 be the set of all edges in B that are incident to 1 and let B2 be the set of all edges in B that are incident to 2. Let A3 = A\(A1 ∪ A2) and B3 = B\(B1 ∪ B2). By (5.6),


- P(x,q,A) = P(x,q,A1)P(x,q,A2)P(x,q,A3)

and

- P(y,q,B) = P(y,q,B1)P(y,q,B2)P(y,q,B3).


Thus,

q∈[N]r

P(x,q,A)P(y,q,B)(xq1q2 − yq1q2)

=

q3,...,qr

P(x,q,A3)P(y,q,B3)

q1,q2

Q(x,y,q)(xq1q2 − yq1q2) , where

Q(x,y,q) = P(x,q,A1)P(x,q,A2)P(y,q,B1)P(y,q,B2). Now ﬁx q3,... ,qr. Then P(x,q,A1)P(y,q,B1) is a function of q1 only, and does not depend on q2. Let g(q1) denote this function. Similarly, P(x,q,A2)P(y,q,B2) is a function of q2 only, and does not depend on q1. Let h(q2) denote this function. Both g and h are uniformly bounded by 1. Therefore

q1,q2

Q(x,y,q)(xq1q2 − yq1q2) =

q1,q2

g(q1)h(q2)(xq1q2 − yq1q2) ≤ N x − y op.

Since this is true for all choices of q3,... ,qr and P is also uniformly bounded by 1, this completes the proof of the lemma.

Let A and B be two sets of edges of Kr. For x,y ∈ [0,1]n, deﬁne R(x,y,A,B) :=

q∈[N]r

P(x,q,A)P(y,q,B).

- Lemma 5.5. Let A, B, A′ and B′ be sets of edges of Kr such that A ∩ B = A′ ∩ B′ = ∅ and A ∪ B = A′ ∪ B′. Then


- 1

![image 174](<2014-chatterjee-nonlinear-large-deviations_images/imageFile174.png>)

- 2


r(r − 1)Nr−1 x − y op.

|R(x,y,A,B) − R(x,y,A′,B′)| ≤

Proof. First, suppose that e = {α,β} is an edge such that e  ∈ A′ and A = A′ ∪ {e}. Since A ∪ B = A′ ∪ B′ and A ∩ B = A′ ∩ B′ = ∅, this implies that e  ∈ B and B′ = B ∪ {e}. Thus,

R(x,y,A,B) − R(x,y,A′,B′) =

P(x,q,A′)P(y,q,B)(xqαqβ − yqαqβ),

q∈[N]r

and the proof is completed using Lemma 5.4. For the general case, simply ‘move’ from the pair (A,B) to the pair (A′,B′) by ‘moving one edge at a time’ and apply Lemma 5.4 at each step.

- Lemma 5.6. Let gij denote the function ∂T/∂xij, where T is the function deﬁned in equation (5.1). Then for any x,y ∈ [0,1]n,


(gij(x) − gij(y))2 ≤ 8m2k2N x − y op .

1≤i<j≤N

Proof. Recall equation (5.2), that is, for any 1 ≤ i < j ≤ N,

1 Nk−2

∂T ∂xij

xqlql′ .

=

gij(x) =

![image 175](<2014-chatterjee-nonlinear-large-deviations_images/imageFile175.png>)

![image 176](<2014-chatterjee-nonlinear-large-deviations_images/imageFile176.png>)

{a,b}∈E q∈[N]k {qa,qb}={i,j}

{l,l′}∈E {l,l′} ={a,b}

Although diﬀerentiating with respect to xii does not make sense, let gii be the function deﬁned using the same formula as above. When i > j, let gij = gji. Fix x,y ∈ [0,1]n. Deﬁne for any q ∈ [N]k and {a,b} ∈ E

xqlql′ −

D(q,{a,b}) :=

yqlql′.

{l,l′}∈E {l,l′} ={a,b}

{l,l′}∈E {l,l′} ={a,b}

Deﬁne

θij :=

2 if i = j, 1/2 if i = j,

γij :=

2 if i = j, 1 if i = j.

Then note that

N

i,j=1

=

=

=

θij(gij(x) − gij(y))2

N

1 N2k−4

θij

![image 177](<2014-chatterjee-nonlinear-large-deviations_images/imageFile177.png>)

i,j=1

D(q,{a,b})

{a,b}∈E q∈[N]k {qa,qb}={i,j}

2

N

1 N2k−4

θijD(q,{a,b})D(s,{c,d})

![image 178](<2014-chatterjee-nonlinear-large-deviations_images/imageFile178.png>)

i,j=1 {a,b}∈E {c,d}∈E

q∈[N]k {qa,qb}={i,j}

s∈[N]k {sc,sd}={i,j}

1 N2k−4

γqaqbD(q,{a,b})D(s,{c,d}).

![image 179](<2014-chatterjee-nonlinear-large-deviations_images/imageFile179.png>)

q∈[N]k s∈[N]k {sc,sd}={qa,qb}

{a,b}∈E {c,d}∈E

Now ﬁx two edges {a,b} and {c,d} in E. Relabeling vertices if necessary, assume that c = k − 1 and d = k. Let r = 2k − 2. For any t ∈ [N]r, deﬁne two vectors q(t) and s(t) in [N]k as follows.

For i = 1,... ,k, let qi(t) = ti. For i = 1,... ,k −2, let si(t) = ti+k. Let sk−1(t) = ta and sk(t) = tb. With this deﬁnition, it is clear that

γqaqbD(q,{a,b})D(s,{c,d})

q∈[N]k s∈[N]k {sc,sd}={qa,qb}

D(q,{a,b})D(s,{c,d})

=

q∈[N]k s∈[N]k sc=qa, sd=qb

D(q,{a,b})D(s,{c,d}).

+

q∈[N]k s∈[N]k sc=qb, sd=qa

Note that the ﬁrst term on the right-hand side is exactly equal to

D(q(t),{a,b})D(s(t),{c,d}).

t∈[N]r

Below, we will get a bound on this term. The same upper bound will hold for the other term by symmetry.

Next, deﬁne two subsets of edges A and B of Kr as follows. Let A be the set of all edges {l,l′} such that {l,l′} ∈ E\{{a,b}}. Let B be the set of all edges {φ(l),φ(l′)} such that {l,l′} ∈ E\{{k−1,k}}, where φ : [k] → [r] is the map

 

x + k if x = k − 1 and x = k,

φ(x) =

- a if x = k − 1,
- b if x = k.




By the above construction, ql(t) = tl and sl(t) = tφ(l). Therefore it is easy to see, for instance, that

ysl(t)s

xql(t)q

l′(t)

l′(t)

t∈[N]r {l,l′}∈E {l,l′} ={a,b}

{l,l′}∈E {l,l′} ={k−1,k}

xtltl′

=

t∈[N]r {l,l′}∈E {l,l′} ={a,b}

ytφ(l)tφ(l′)

{l,l′}∈E {l,l′} ={k−1,k}

= R(x,y,A,B). Carrying out similar computations for the remaining terms in D(q(t),{a,b})D(s(t),{c,d}), we get

D(q(t),{a,b})D(s(t),{c,d})

t∈[N]r

= R(x,y,A ∪ B,∅) − R(x,y,B,A) − R(x,y,A,B) + R(x,y,∅,A ∪ B).

Lastly, note that A∩B = ∅ since for any {l,l′} ∈ E\{{k −1,k}}, at least one among φ(l) and φ(l′) must be strictly bigger than k and therefore {φ(l),φ(l′)} cannot be an element of A. The proof is now easily completed by applying Lemma 5.5.

With the help of Lemma 5.3 and Lemma 5.6, we are now ready to prove Lemma 5.2. Proof of Lemma 5.2. Take any ǫ > 0 and let

ǫ2 64m2k2

.

τ =

![image 180](<2014-chatterjee-nonlinear-large-deviations_images/imageFile180.png>)

Let W(τ) be as in Lemma 5.3. For each W ∈ W(τ), let y(W) ∈ [0,1]n be a vector such that

M(y) − W op ≤ Nτ. If for some W there does not exist any such y, leave y(W) undeﬁned. Let gij = ∂T/∂xij, as in Lemma 5.6. Let g : [0,1]n → Rn be the function whose (i,j)th coordinate is gij. Deﬁne

D(ǫ) := g(y) : y = y(W) for some W ∈ W(τ) . Then by Lemma 5.3

|D(ǫ)| ≤ |W(τ)| ≤ e34(N/τ2) log(51/τ2). We claim that the set D(ǫ) satisﬁes the requirements of Theorem 1.1. To see this, take any x ∈ [0,1]n. By Lemma 5.3, there exists W ∈ W(τ) such that M(x) − W op ≤ Nτ. In particular, this means that y := y(W) is deﬁned, and so

Therefore by Lemma 5.6,

x − y op = M(x) − M(y) op ≤ M(x) − W op + W − M(y) op ≤ 2Nτ .

(gij(x) − gij(y))2 ≤ 16m2k2N2τ .

1≤i<j≤N

Let z = g(x) and v = g(y). Then v ∈ D(ǫ), and by the above inequality,

N2ǫ2 4 ≤

N 2

(zij − vij)2 ≤ 16m2k2N2τ =

![image 181](<2014-chatterjee-nonlinear-large-deviations_images/imageFile181.png>)

1≤i<j≤N

ǫ2.

This proves the claim that D(ǫ) satisﬁes the requirements of Theorem 1.1. This completes the proof of Lemma 5.2.

The next step is to understand the properties of the rate function φp(t) corresponding to T. First, we need a simple lemma.

- Lemma 5.7. For any r and any a1,... ,ar,b ∈ [0,1], r


r

ai + br .

(ai + b(1 − ai)) ≥ (1 − br)

i=1

i=1

Proof. The proof is by induction on r. The inequality is an equality for r = 1. Suppose that it holds for r − 1. Then

r−1

r

ai + br−1 ((1 − b)ar + b)

(ai + b(1 − ai)) ≥ (1 − br−1)

i=1

i=1

r−1

r

ai + br

ai + br−1(1 − b)ar + (1 − br−1)b

= (1 − br−1)(1 − b)

i=1

i=1

r

ai + br

≥ ((1 − br−1)(1 − b) + br−1(1 − b) + (1 − br−1)b)

i=1

r

ai + br . This completes the induction.

= (1 − br)

i=1

- Lemma 5.8. Let φp(t) be deﬁned as in (1.5), with f = T and n = N(N −1)/2. Let l be the element of [0,1]n whose coordinates are all equal to 1, and let t0 := T(l)/n. Then for any 0 < δ < t < t0,

φp(t − δ) ≥ φp(t) −

δ t0 − t

![image 182](<2014-chatterjee-nonlinear-large-deviations_images/imageFile182.png>)

1/m

nlog(1/p).

Proof. Take any x ∈ [0,1]n such that T(x) ≥ (t−δ)n and x minimizes Ip(x) among all x satisfying this inequality. If T(x) ≥ tn, then we immediately have φp(t) ≤ Ip(x) = φp(t − δ), and there is nothing more to prove. So let us assume that T(x) < tn. Let

ǫ :=

tn − T(x) T(l) − T(x)

![image 183](<2014-chatterjee-nonlinear-large-deviations_images/imageFile183.png>)

1/m

. For each 1 ≤ i < j ≤ N, let

yij := xij + ǫ(1 − xij). Let yji = yij and yii = 0. Then y ∈ [0,1]n, and by Lemma 5.7,

T(y) ≥ (1 − ǫm)T(x) + ǫmT(l) = tn . Thus, by the convexity of Ip,

φp(t) ≤ Ip(y) = Ip((1 − ǫ)x + ǫl) ≤ (1 − ǫ)Ip(x) + ǫIp(l) ≤ Ip(x) + ǫnlog(1/p) = φp(t − δ) + ǫnlog(1/p).

Since T(x) ≥ (t − δ)n,

ǫm ≤

tn − (t − δ)n T(l) − (t − δ)n ≤

![image 184](<2014-chatterjee-nonlinear-large-deviations_images/imageFile184.png>)

δ t0 − t

![image 185](<2014-chatterjee-nonlinear-large-deviations_images/imageFile185.png>)

. This completes the proof of the lemma.

- Lemma 5.9. For any p and t,


1 2

(⌈t1/kN⌉ + k)2 log(1/p). Proof. Let r := ⌈t1/kN⌉ + k. Deﬁne x ∈ [0,1]n as

φp(t) ≤

![image 186](<2014-chatterjee-nonlinear-large-deviations_images/imageFile186.png>)

1 if 1 ≤ i < j ≤ r , p otherwise.

xij :=

Then

1 Nk−2

T(x) ≥

xqlql′

![image 187](<2014-chatterjee-nonlinear-large-deviations_images/imageFile187.png>)

q∈[r]k {l,l′}∈E

r(r − 1)··· (r − k + 1)

Nk−2 ≥ tN2 ≥ tn , and since Ip(p) = 0,

≥

![image 188](<2014-chatterjee-nonlinear-large-deviations_images/imageFile188.png>)

Ip(x) =

Ip(xij) ≤

i<j

- 1

![image 189](<2014-chatterjee-nonlinear-large-deviations_images/imageFile189.png>)

- 2


r2 log(1/p).

This proves the claim.

Proof of the upper bound in Theorem 1.2. The task now is to pull together all the information obtained above, for use in Theorem 1.1. As intended, we work with f = T. Take t = κpm for some ﬁxed κ > 0. Let δ and ǫ be two positive real numbers, both less than t, to be chosen later. Note that δ < t < κp2m/k since t = κpm and k > 2. Assume that δ and ǫ are bigger than N−1/2. Note that p is already assumed to be bigger than N−1/2 in the statement of the theorem.

Recall that the indexing set for quantities like bi and cij, instead of being {1,... ,n}, is now {(i,j) : 1 ≤ i < j ≤ N}. For simplicity, we will write (ij) instead of (i,j). Throughout, C will denote any constant that depends only on the graph H, the constant κ, and nothing else. From

- Lemma 5.1, we have the estimates a ≤ N2 , b(ij) ≤ C ,


and

c(ij)(i′j′) ≤

Let θ := δ−1p2m/k. By Lemma 5.9,

- CN−1 if |{i,j,i′,j′}| = 2 or 3 ,
- CN−2 if |{i,j,i′,j′}| = 4 .


K ≤ Cp2m/k log N . Using the above bounds, we get

α ≤ CN2 log N , β(ij) ≤ Cθ log N , and

γ(ij)(i′j′) ≤

Therefore, we have the estimates

CN−1θ log N if |{i,j,i′,j′}| = 2 or 3, CN−2δ−1θ log N if |{i,j,i′,j′}| = 4.

β(2ij) ≤ CN2θ2(log N)2 ,

(ij)

b2(ij) ≤ CN2 ,

(ij)

and by Lemma 5.2,

CNθ4 ǫ4

CK δǫ ≤

log |D((δǫ)/(4K))| ≤

log

![image 190](<2014-chatterjee-nonlinear-large-deviations_images/imageFile190.png>)

![image 191](<2014-chatterjee-nonlinear-large-deviations_images/imageFile191.png>)

CNθ4(log N)5 ǫ4

.

![image 192](<2014-chatterjee-nonlinear-large-deviations_images/imageFile192.png>)

Combining the last three estimates, we see that the complexity term in Theorem 1.1 is bounded above by

CNθ4(log N)5 ǫ4

CN2ǫθ log N +

.

![image 193](<2014-chatterjee-nonlinear-large-deviations_images/imageFile193.png>)

Taking ǫ = N−1/5θ3/5(log N)4/5, the above bound simpliﬁes to CN9/5θ8/5(log N)9/5 .

Next, note that by the bounds obtained above and the inequality δ > N−1/2,

αγ(ij)(ij) ≤ CN3θ(log N)2 ,

(ij)

αγ(2ij)(i′j′) ≤ CN3θ2(log N)3 ,

(ij),(i′j′)

β(ij)(β(i′j′) + 4)γ(ij)(i′j′) ≤ CN2δ−1θ3(log N)3 ,

(ij),(i′j′)

β(2ij)

(ij)

1/2

γ(2ij)(ij)

(ij)

1/2

≤ CNθ2(log N)2 ,

γ(ij)(ij) ≤ CNθ log N .

(ij)

The above estimates show that the smoothness term in Theorem 1.1 is bounded above by a constant times

N3/2θ(log N)3/2 + Nδ−1/2θ3/2(log N)3/2 + Nθ2(log N)2 .

Putting η := p2m/k, and recalling that N−1/(m+3) ≤ p ≤ 1 − N−1, we see that this is bounded by a constant times

N3/2δ−1η(log N)3/2 + Nδ−2η3/2(log N)2 . Since δ > N−1/2, we can further simplify this upper bound to

N3/2δ−1η(log N)2. Combining the bounds on the complexity term and the smoothness term, we get that log P(T(Y ) ≥ tn) ≤ −φp(t − δ) + CN9/5δ−8/5η8/5(log N)9/5

+ CN3/2δ−1η(log N)2 . By Lemma 5.8,

−φp(t − δ) ≤ −φp(t) + Cδ1/mN2 log N. Taking

δ = N−m/(5+8m)η8m/(5+8m)(log N)4m/(5+8m) gives

log P(T(Y ) ≥ tn) (5.7) ≤ −φp(t) + CN(9+16m)/(5+8m)η8/(5+8m)(log N)(9+8m)/(5+8m)

+ CN(15+26m)/(10+16m)η5/(5+8m)(log N)(10+12m)/(5+8m) . Now note that since p > N−1/2, therefore

N(9+16m)/(5+8m)η8/(5+8m) N(15+26m)/(10+16m)η5/(5+8m)

= N(3+6m)/(10+16m)p6m/k(5+8m) ≥ N(3+6m)/(10+16m)N−3m/(5+8m)

![image 194](<2014-chatterjee-nonlinear-large-deviations_images/imageFile194.png>)

= N3/(10+16m) .

This shows that the ﬁrst term on the right-hand side in (5.7) dominates the second when N is suﬃciently large. Therefore, when N is large enough,

log P(T(Y ) ≥ tn) ≤ −φp(t) + CN(9+16m)/(5+8m)p16m/k(5+8m)(log N)(9+8m)/(5+8m) .

Written diﬀerently, this is

φp(t) −log P(T(Y ) ≥ tn) ≤ 1 +

![image 195](<2014-chatterjee-nonlinear-large-deviations_images/imageFile195.png>)

CN(9+16m)/(5+8m)p16m/k(5+8m)(log N)(9+8m)/(5+8m) −log P(T(Y ) ≥ tn)

. By [22, Theorem 1.2 and Theorem 1.5],

![image 196](<2014-chatterjee-nonlinear-large-deviations_images/imageFile196.png>)

− log P(T(Y ) ≥ tn) ≥ CN2p∆ , (5.8)

where ∆ is the maximum degree of H, provided that p ≥ N−1/∆ and N is suﬃciently large. The lower bound on p is already assumed in the statement of the theorem. Therefore,

φp(t) −log P(T(Y ) ≥ tn) ≤ 1 + CN−1/(5+8m)p−∆+16m/k(5+8m)(log N)(9+8m)/(5+8m) .

![image 197](<2014-chatterjee-nonlinear-large-deviations_images/imageFile197.png>)

A minor veriﬁcation using the assumption p ≥ N−1/4 shows that the ǫ and δ chosen above are both bigger than N−1/2, as required. To complete the proof of the upper bound, notice that E(X) is asymptotic to pm since p ≥ N−1/(m+3).

Proof of the lower bound in Theorem 1.2. By Lemma 5.8, Lemma 5.1, and the lower bound in Theorem 1.1,

log P(T(Y ) ≥ tn) ≥ −φp(t) − CN−1/2mN2 log N . Therefore, again applying (5.8), we get

φp(t)

−log P(T(Y ) ≥ tn) ≥ 1 − CN−1/2mp−∆ log N . This completes the proof of the lower bound.

![image 198](<2014-chatterjee-nonlinear-large-deviations_images/imageFile198.png>)

6. Proof of Theorem 1.5

In this section, all indices range over Z/nZ, and all additions and subtractions of indices are modulo n. As usual, C will denote any universal constant.

Let Y = (Y0,... ,Yn−1) be a vector of i.i.d. Bernoulli(p) random variables. Deﬁne f : [0,1]Z/nZ → R as

1 n i,j

xixi+jxi+2j . Then

f(x) :=

![image 199](<2014-chatterjee-nonlinear-large-deviations_images/imageFile199.png>)

a := f ≤ n. (6.1) Let fi := ∂f/∂xi and fij := ∂2f/∂xi∂xj. Then

1 n j

fi(x) =

(xi+jxi+2j + xi−jxi+j + xi−2jxi−j).

![image 200](<2014-chatterjee-nonlinear-large-deviations_images/imageFile200.png>)

From this expression, it is clear that

bi := fi ≤ C , cij := fij ≤

C n

. (6.2)

![image 201](<2014-chatterjee-nonlinear-large-deviations_images/imageFile201.png>)

For each j, deﬁne the function ej : Z/nZ → C as

1 √n

ej(k) :=

![image 202](<2014-chatterjee-nonlinear-large-deviations_images/imageFile202.png>)

e2πijk/n ,

![image 203](<2014-chatterjee-nonlinear-large-deviations_images/imageFile203.png>)

where i = √

![image 204](<2014-chatterjee-nonlinear-large-deviations_images/imageFile204.png>)

−1. These functions form an orthonormal system, in the sense that

k

![image 205](<2014-chatterjee-nonlinear-large-deviations_images/imageFile205.png>)

ej(k)ej′(k) = δj−j′ ,

where δ is the Kronecker delta function, that is,

δj :=

1 if j = 0, 0 otherwise.

For any x ∈ RZ/nZ, deﬁne its discrete Fourier transform xˆ ∈ Cn as

xˆj :=

k

xkej(k).

The orthonormality of the ej’s implies the inversion formula

j

![image 206](<2014-chatterjee-nonlinear-large-deviations_images/imageFile206.png>)

xˆjek(j) =

=

j,l

![image 207](<2014-chatterjee-nonlinear-large-deviations_images/imageFile207.png>)

xlej(l)ek(j)

j,l

![image 208](<2014-chatterjee-nonlinear-large-deviations_images/imageFile208.png>)

xlel(j)ek(j) = xk .

Moreover, it also implies the Plancherel identity

j

|xˆj|2 =

![image 209](<2014-chatterjee-nonlinear-large-deviations_images/imageFile209.png>)

xkxlej(k)ej(l)

j,k,l

![image 210](<2014-chatterjee-nonlinear-large-deviations_images/imageFile210.png>)

xkxlek(j)el(j) =

=

j,k,l

k

x2k .

- Lemma 6.1. For any x,y ∈ [0,1]Z/nZ,


i

(fi(x) − fi(y))2 ≤ Cn1/2 max

|xˆi − yˆi|.

i

Proof. Note that for any x and y,

(fi(x) − fi(y))2 (6.3)

i

1 n2 i j

(xi+jxi+2j + xi−jxi+j + xi−2jxi−j

=

![image 211](<2014-chatterjee-nonlinear-large-deviations_images/imageFile211.png>)

2

− yi+jyi+2j − yi−jyi+j − yi−2jyi−j)

1 n2 i,j,k

=

(xi+jxi+2j + xi−jxi+j + xi−2jxi−j

![image 212](<2014-chatterjee-nonlinear-large-deviations_images/imageFile212.png>)

− yi+jyi+2j − yi−jyi+j − yi−2jyi−j) × (xi+kxi+2k + xi−kxi+k + xi−2kxi−k

− yi+kyi+2k − yi−kyi+k − yi−2kyi−k).

Let us now expand out the product in the above expression. There will be 36 terms, 18 of which are positive and 18 are negative. The positive terms will be products of fours x’s or four y’s, and the negative terms will be products of two x’s and two y’s. Match each positive term with a matching negative term. For example, match xi+jxi+2jxi−kxi+k with −xi+jxi+2jyi−kyi+k. Summing over i, j and k for this particular pair, we get the expression

1 n2 i,j,k

(xi+jxi+2jxi−kxi+k − xi+jxi+2jyi−kyi+k) (6.4)

![image 213](<2014-chatterjee-nonlinear-large-deviations_images/imageFile213.png>)

1 n2 i,j,k

(xi+jxi+2j(xi−k − yi−k)xi+k − xi+jxi+2jyi−k(xi+k − yi+k)).

=

![image 214](<2014-chatterjee-nonlinear-large-deviations_images/imageFile214.png>)

Now consider the ﬁrst term in the above expression. Let z = x−y. Then by the inversion formula, 1

xi+jxi+2jxi+kzi−k

![image 215](<2014-chatterjee-nonlinear-large-deviations_images/imageFile215.png>)

n2 i,j,k

1 n2 i,j,k a,b,c,d

![image 216](<2014-chatterjee-nonlinear-large-deviations_images/imageFile216.png>)

=

xˆaxˆbxˆczˆdei+j(a)ei+2j(b)ei+k(c)ei−k(d)

![image 217](<2014-chatterjee-nonlinear-large-deviations_images/imageFile217.png>)

1 n5/2 a,b,c,d i,j,k

![image 218](<2014-chatterjee-nonlinear-large-deviations_images/imageFile218.png>)

xˆaxˆbxˆczˆdea+b+c+d(i)ea+2b(j)ec−d(k)

=

![image 219](<2014-chatterjee-nonlinear-large-deviations_images/imageFile219.png>)

1 n a,b,c,d

1 n d

=

xˆaxˆbxˆczˆdδa+b+c+dδa+2bδc−d =

xˆ−4dxˆ2dxˆdzˆd .

![image 220](<2014-chatterjee-nonlinear-large-deviations_images/imageFile220.png>)

![image 221](<2014-chatterjee-nonlinear-large-deviations_images/imageFile221.png>)

√n

By the Plancherel identity and the fact that x ∈ [0,1]Z/nZ, j |xˆj|2 ≤ n. In particular, |xˆj| ≤

![image 222](<2014-chatterjee-nonlinear-large-deviations_images/imageFile222.png>)

for all j. Let M := maxi |zˆi|. Using these observations and H¨older’s inequality, we see that the above sum is bounded above by

M n d |xˆ−4d|3

|xˆd|3

|xˆ2d|3

![image 223](<2014-chatterjee-nonlinear-large-deviations_images/imageFile223.png>)

d

d

CM n d |xˆd|3 ≤ CMn1/2 .

≤

![image 224](<2014-chatterjee-nonlinear-large-deviations_images/imageFile224.png>)

1/3

This is a bound on the ﬁrst term in the right-hand side of (6.4). Similarly, it may be veriﬁed that the same bound holds for the second term in the right-hand side of (6.4), and also for all terms in the expansion of (6.3). This completes the proof of the lemma.

- Lemma 6.2. For the function f considered in this section, one can ﬁnd sets D(ǫ) satisfying (1.7) such that |D(ǫ)| ≤ C1(n/ǫ2)C2/ǫ4 where C1 and C2 are universal constants. Proof. Take any ǫ > 0. Let γ := cǫ2√n, where c is a universal constant that will be chosen later. Deﬁne a map R : Cn → Cn as follows: For each i, let the ith coordinate of y = R(x) be the complex number closest to xi whose real and imaginary parts are both integer multiples of γ. Clearly, |xi − yi| ≤ γ. Moreover, if |xi| < γ/2 then yi = 0.

![image 225](<2014-chatterjee-nonlinear-large-deviations_images/imageFile225.png>)

Let M be the set of all xˆ as x ranges over [0,1]n. Take any x ∈ [0,1]n and let y := R(ˆx). Let A be the set of all i such that |xˆi| ≥ γ/2. Then yi = 0 for each i  ∈ A. Given A, there are at most Cn/γ2 possible values of each yi, i ∈ A since |xˆi| ≤

√n. On the other hand by the Plancherel identity,

![image 226](<2014-chatterjee-nonlinear-large-deviations_images/imageFile226.png>)

|A| ≤

4 γ2

![image 227](<2014-chatterjee-nonlinear-large-deviations_images/imageFile227.png>)

n−1

i=0

|xˆi|2 ≤

4n γ2

![image 228](<2014-chatterjee-nonlinear-large-deviations_images/imageFile228.png>)

,

implying that there are at most n4n/γ2 possible candidates for the set A. Combining these observations, we realize that the number of possible values of y is at most

n4n/γ2(Cn/γ2)4n/γ2 . This, therefore, is a bound on the size of R(M).

Say that two points x and y in [0,1]n are equivalent if R(ˆx) = R(ˆy). Clearly, this is an equivalence relation. Suppose that x and y are equivalent. Let z = R(ˆx) = R(ˆy). Then for each i,

|xˆi − yˆi| ≤ |xˆi − zi| + |zi − yˆi| ≤ 2γ . Construct the set B by choosing one x from each equivalence class. Then clearly |B| ≤ |R(M)| ≤ n4n/γ2(Cn/γ2)4n/γ2 . By the bounds obtained above and Lemma 6.1, for any x ∈ [0,1]n, there exists y ∈ B such that

i

(fi(x) − fi(y))2 ≤ Cn1/2 max

i

|xˆi − yˆi| ≤ Cn1/2γ .

The right-hand side is less than ǫ2n if the constant c in the deﬁnition of γ is chosen suﬃciently small. Deﬁning D(ǫ) to be the set ∇f(B) completes the proof.

- Lemma 6.3. Let φp(t) be deﬁned as in (1.5). Then for any 0 < δ < t < 1,


1/3

δ 1 − t

φp(t − δ) ≥ φp(t) −

nlog(1/p).

![image 229](<2014-chatterjee-nonlinear-large-deviations_images/imageFile229.png>)

Proof. Take any x ∈ [0,1]n such that f(x) ≥ (t − δ)n and x minimizes Ip(x) among all x satisfying this inequality. If f(x) ≥ tn, then we immediately have φp(t) ≤ Ip(x) = φp(t − δ), and there is nothing more to prove. So let us assume that f(x) < tn. Let

1/3

tn − f(x) n − f(x)

. For each i, let

ǫ :=

![image 230](<2014-chatterjee-nonlinear-large-deviations_images/imageFile230.png>)

yi := xi + ǫ(1 − xi).

Then y ∈ [0,1]n, and by Lemma 5.7, we get

f(y) ≥ (1 − ǫ3)f(x) + ǫ3 = tn . Thus, by the convexity of Ip,

φp(t) ≤ Ip(y) ≤ (1 − ǫ)Ip(x) + ǫnlog(1/p)

≤ Ip(x) + ǫnlog(1/p) = φp(t − δ) + ǫnlog(1/p). Since f(x) ≥ (t − δ)n,

tn − (t − δ)n n − (t − δ)n ≤

δ 1 − t

ǫ3 ≤

.

![image 231](<2014-chatterjee-nonlinear-large-deviations_images/imageFile231.png>)

![image 232](<2014-chatterjee-nonlinear-large-deviations_images/imageFile232.png>)

This completes the proof of the lemma.

- Lemma 6.4. For any p ≥ n−1 and t > 0, φp(t) ≤ Ct1/2nlog n.

Proof. Deﬁne x ∈ [0,1]n as the vector whose ﬁrst 3t1/2n coordinates are equal to 1 and the rest are equal to p. Then

f(x) =

1 n i,j

![image 233](<2014-chatterjee-nonlinear-large-deviations_images/imageFile233.png>)

xixi+jxi+2j ≥ tn ,

and Ip(x) ≤ Ct1/2nlog n. This proves the claim.

- Lemma 6.5. Suppose that p ≥ n−1/6. Then for any κ > 1, P(f(Y ) ≥ κp3n) ≤ Ce−cnp6


where C and c depend only on κ.

Proof. Let κ′ := (1 + κ)/2, so that 1 < κ′ < κ. It is easy to see that if n is suﬃciently large (depending on κ), then E(f(Y )) ≤ κ′p3n. Again, (6.2) shows that f(Y ) changes at most by a bounded amount if one Yi changes value. Therefore a straightforward application of Hoeﬀding’s inequality [21] completes the proof of the lemma.

Proof of Theorem 1.5. Let 0 < δ < t < 1, where t = κp3 for some κ > 1 and δ is to be chosen later. Fix another small quantity ǫ, also to be chosen later. Assume that ǫ and δ are both bigger than n−1/3. Already from the statement of the theorem, recall that p ≥ n−1/162.

Throughout this proof C will denote any constant that may depend only on κ. Let K, α, βi and γij be deﬁned as in Theorem 1.1. By (6.1), (6.2), Lemma 6.4 and the assumption that n−1/162 ≤ p ≤ 1 − n−1,

Ct1/2 log n δ2n

Ct1/2 log n δ

K ≤ Ct1/2 log n, α ≤ Cnlog n, βi ≤

, γij ≤

.

![image 234](<2014-chatterjee-nonlinear-large-deviations_images/imageFile234.png>)

![image 235](<2014-chatterjee-nonlinear-large-deviations_images/imageFile235.png>)

These imply the bounds

i

i

i,j

i

Ct1/2n(log n)2 δ2 ≤

Ctn(log n)2 δ5/2

αγii ≤

,

![image 236](<2014-chatterjee-nonlinear-large-deviations_images/imageFile236.png>)

![image 237](<2014-chatterjee-nonlinear-large-deviations_images/imageFile237.png>)

Ctn(log n)2 δ2

Ctn(log n)3 δ4

βi2 ≤

αγij2 ≤

,

,

![image 238](<2014-chatterjee-nonlinear-large-deviations_images/imageFile238.png>)

![image 239](<2014-chatterjee-nonlinear-large-deviations_images/imageFile239.png>)

i,j

Ct3/2n(log n)3 δ4

βi(βj + 4)γij ≤

,

![image 240](<2014-chatterjee-nonlinear-large-deviations_images/imageFile240.png>)

Ct(log n)2 δ4n

γii2 ≤

,

![image 241](<2014-chatterjee-nonlinear-large-deviations_images/imageFile241.png>)

i

Ct1/2 log n δ2

γii ≤

.

![image 242](<2014-chatterjee-nonlinear-large-deviations_images/imageFile242.png>)

Combining these, we see that the smoothness term is bounded by

Ct1/2δ−2n1/2(log n)3/2 + Ctδ−3(log n)2 + Ct1/2δ−2 log n. Since δ > n−1/3, the above expression is bounded by

Ct1/2δ−2n1/2(log n)3/2 . (6.5) On the other hand by Lemma 6.2 and the assumption that ǫ > n−1/3,

C log(n/ǫ2) ǫ4 ≤

C log n ǫ4

log |D(ǫ)| ≤

. Therefore the complexity term is bounded above by

![image 243](<2014-chatterjee-nonlinear-large-deviations_images/imageFile243.png>)

![image 244](<2014-chatterjee-nonlinear-large-deviations_images/imageFile244.png>)

Ct2(log n)5 δ4ǫ4

Ct1/2 log n δǫ

Cǫt1/2δ−1nlog n + log

. Choosing

+

![image 245](<2014-chatterjee-nonlinear-large-deviations_images/imageFile245.png>)

![image 246](<2014-chatterjee-nonlinear-large-deviations_images/imageFile246.png>)

ǫ = t3/10δ−3/5n−1/5(log n)4/5

and recalling the assumed lower bounds on ǫ, δ and p, we see that the complexity term is bounded by

Ct4/5δ−8/5n4/5(log n)9/5 . (6.6)

By Theorem 1.1, Lemma 6.3, the bound (6.5) for the smoothness term, and the bound (6.6) for the complexity term, we get that

log P(f(Y ) ≥ tn) ≤ −φp(t) + Cδ1/3nlog n + Ct4/5δ−8/5n4/5(log n)9/5

+ Ct1/2δ−2n1/2(log n)3/2 . Now choose

δ = t12/29n−3/29(log n)12/29 . Recalling that t = κp3, this gives

log P(f(Y ) ≥ tn) ≤ −φp(t) + Cp12/29n28/29(log n)33/29

+ Cp−57/58n41/58(log n)39/58 .

By the assumed lower bound on p, it is easy to see that the second term on the right dominates the third if n is large enough. Together with an application of Lemma 6.5, this completes the proof of the upper bound in Theorem 1.5. For the lower bound, recall that

log P(f(Y ) ≥ tn) ≥ −φp(t + δ0) − ǫ0n − log 2

≥ −φp(t) − Cδ01/3nlog n − ǫ0n, where

p

1 √n

1 − p ≤ Cn−1/2 log n and

4 + log

ǫ0 =

![image 247](<2014-chatterjee-nonlinear-large-deviations_images/imageFile247.png>)

![image 248](<2014-chatterjee-nonlinear-large-deviations_images/imageFile248.png>)

![image 249](<2014-chatterjee-nonlinear-large-deviations_images/imageFile249.png>)

n

1/2

2 n

≤ Cn−1/2 .

(acii + b2i )

δ0 =

![image 250](<2014-chatterjee-nonlinear-large-deviations_images/imageFile250.png>)

i=1

An application of Lemma 6.5 completes the proof of the lower bound.

7. Proof of Theorem 1.7

Let all notational conventions be the same as in Section 5. However, instead of a single H, consider l graphs H1,... ,Hl, and deﬁne T1,... ,Tl accordingly.

Throughout this section, C will denote any constant that may depend only on the graphs H1,... ,Hl. Deﬁne

f(x) := β1T1(x) + ··· + βlTl(x).

Let B := 1 + |β1| + ··· + |βl|, as in the statement of the theorem. Let a, b(ij) and c(ij)(i′j′) be as in Theorem 1.6. Clearly,

l

|βr| ≤ CBN2 . By Lemma 5.1, we get the estimates

a ≤ N2

r=1

b(ij) ≤ CB and

- CBN−1 if |{i,j,i′,j′}| = 2 or 3 ,
- CBN−2 if |{i,j,i′,j′}| = 4 .


c(ij)(i′j′) ≤

Let D1(ǫ),... ,Dl(ǫ) be the D(ǫ)’s for T1,... ,Tl. Deﬁne D(ǫ) := {β1d1 + ··· + βldl : dr ∈ Di(ǫ/βrl), r = 1,... ,l}. Clearly, for any x ∈ [0,1]n, there exists d1 ∈ D1(ǫ/β1l), . .., dl ∈ Dl(ǫ/βll) such that

l

n

n

(fi(x) − (β1d1i + ··· + βldli))2 ≤ l

βr2(Tri(x) − dri)2 ≤ nǫ2 .

r=1

i=1

i=1

Therefore, D(ǫ) satisﬁes the requirement of Theorem 1.6. Also,

l

|Dr(ǫ/βrl)|. (7.1)

|D(ǫ)| ≤

r=1

By the bounds on a, b(ij) and c(ij)(i′j′) obtained above, the following estimates are easy:

ac(ij)(ij) ≤ CB2N3 ,

(ij)

b2(ij) ≤ CB2N2 ,

(ij)

ac2(ij)(i′j′) ≤ CB3N3 ,

(ij),(i′j′)

b(ij)(b(i′j′) + 4)c(ij)(i′j′) ≤ CB3N2 ,

(ij),(i′j′)

c2(ij)(ij) ≤ CB2 ,

(ij)

c(ij)(ij) ≤ CBN .

(ij)

Combining these estimates, we see that the smoothness term is bounded by CB2N3/2. Next, by (7.1) and Lemma 5.2,

l

log |Dr(ǫ/βrl)|

log |D(ǫ)| ≤

r=1

CB4 ǫ4

CB4N ǫ4

≤

. Therefore, the complexity term (of Theorem 1.6) is bounded by CBN2ǫ +

log

![image 251](<2014-chatterjee-nonlinear-large-deviations_images/imageFile251.png>)

![image 252](<2014-chatterjee-nonlinear-large-deviations_images/imageFile252.png>)

CB4 ǫ4

CB4N ǫ4

. Taking

log

![image 253](<2014-chatterjee-nonlinear-large-deviations_images/imageFile253.png>)

![image 254](<2014-chatterjee-nonlinear-large-deviations_images/imageFile254.png>)

1/5

B3 log N N

ǫ =

, this gives the bound

![image 255](<2014-chatterjee-nonlinear-large-deviations_images/imageFile255.png>)

log B log N

CB8/5N9/5(log N)1/5 1 +

.

![image 256](<2014-chatterjee-nonlinear-large-deviations_images/imageFile256.png>)

By Theorem 1.6, this completes the proof of the upper bound. The lower bound follows easily from Theorem 1.6 and the bound on c(ij)(ij) obtained above. This ﬁnishes the proof of Theorem 1.7.

Acknowledgments

The authors thank Van Vu, Alex Zhai, Yufei Zhao and the anonymous referee for a number of helpful comments.

References

- [1] Bhamidi, S., Bresler, G. and Sly, A. (2008). Mixing time of exponential random graphs. In 2008 IEEE 49th Annual IEEE Symposium on Foundations of Computer Science (FOCS), 803–12.
- [2] Bhattacharya, B. B., Ganguly, S., Lubetzky, E. and Zhao, Y. (2015). Upper tails and independence polynomials in random graphs. arXiv preprint arXiv:1507.04074
- [3] Bollobas´ B. and Riordan, O. (2009). Metrics for sparse graphs. In S. Huczynska, J. D. Mitchell, and C. M. Roney-Dougal, eds., Surveys in combinatorics 2009, pp. 211–287, London Math. Soc. Lecture Note Ser. 365, Cambridge University Press, Cambridge.
- [4] Bolthausen, E., Comets, F. and Dembo, A. (2003). Large deviations for random matrices and random graphs. Private communication.
- [5] Borgs, C., Chayes, J. T., Cohn, H. and Zhao, Y. (2014). An Lp theory of sparse graph convergence I: limits, sparse random graph models, and power law distributions. arXiv preprint arXiv:1401.2906


- [6] Borgs, C., Chayes, J. T., Cohn, H. and Zhao, Y. (2014). An Lp theory of sparse graph convergence II: LD convergence, quotients, and right convergence. arXiv preprint arXiv:1408.0744
- [7] Borgs, C., Chayes, J., Lovasz,´ L., Sos,´ V. T. and Vesztergombi, K. (2008). Convergent sequences of dense

- graphs. I. Subgraph frequencies, metric properties and testing. Adv. Math., 219 no. 6, 1801–1851.

[8] Borgs, C., Chayes, J., Lovasz,´ L., Sos,´ V. T. and Vesztergombi, K. (2012). Convergent sequences of dense

- graphs. II. Multiway cuts and statistical physics. Ann. Math. (2), 176 no. 1, 151-219.


- [9] Carinci, G., Chazottes, J.-R., Giardina,` C. and Redig, F. (2012). Nonconventional averages along arithmetic progressions and lattice spin systems. Indag. Math., 23 no. 3, 589–602.
- [10] Chatterjee, S. (2005). Concentration inequalities with exchangeable pairs. Ph.D. thesis, Stanford University.
- [11] Chatterjee, S. (2007). Estimation in spin glasses: a ﬁrst step. Ann. Statist., 35 no. 5, 1931–1946.
- [12] Chatterjee, S. (2012). The missing log in large deviations for triangle counts. Random Structures Algorithms, 40 no. 4, 437–451.
- [13] Chatterjee, S. (2016). An introduction to large deviations for random graphs. To appear in Bull. Amer. Math. Soc. Currently available as arXiv preprint arXiv:1604.06828
- [14] Chatterjee, S. and Dey, P. S. (2010). Applications of Stein’s method for concentration inequalities. Ann. Probab., 38 no. 6, 2443–2485.
- [15] Chatterjee, S. and Diaconis, P. (2013). Estimating and understanding exponential random graph models. Ann. Statist., 41 no. 5, 2428–2461.
- [16] Chatterjee, S. and Varadhan, S. R. S. (2011). The large deviation principle for the Erd˝s-Re´nyi random graph. European J. Combinatorics, 32 no. 7, 1000–1017.
- [17] Chatterjee, S. and Varadhan, S. R. S. (2012). Large deviations for random matrices. Commun. Stoch. Anal., 6 no. 1, 1–13.
- [18] DeMarco, B. and Kahn, J. (2012). Upper tails for triangles. Random Structures Algorithms, 40 no. 4, 452–459.
- [19] DeMarco, B. and Kahn, J. (2012). Tight upper tail bounds for cliques. Random Structures Algorithms, 41 no. 4, 469–487.
- [20] Dembo, A. and Zeitouni, O. (2010). Large deviations techniques and applications. Corrected reprint of the second (1998) edition. Springer-Verlag, Berlin.
- [21] Hoeffding, W. (1963). Probability inequalities for sums of bounded random variables. J. Amer. Stat. Assoc. 58 13–30.
- [22] Janson, S., Oleszkiewicz, K. and Rucinski,´ A. (2004). Upper tails for subgraph counts in random graphs. Israel J. Math., 142, 61–92.
- [23] Janson, S. and Rucinski,´ A. (2002). The infamous upper tail. Probabilistic methods in combinatorial optimization. Random Structures Algorithms, 20 no. 3, 317–342.
- [24] Janson, S. and Rucinski,´ A. (2004). The deletion method for upper tail estimates. Combinatorica, 24 no. 4, 615–640.
- [25] Kifer, Y. (2010). Nonconventional limit theorems. Prob. Theory Related Fields, 148, 71–106.
- [26] Kifer, Y. and Varadhan, S. R. S. (2014). Nonconventional limit theorems in discrete and continuous time via martingales. Ann. Probab., 42 no. 2, 649–688.
- [27] Kifer, Y. and Varadhan, S. R. S. (2014). Nonconventional large deviations theorems. Probab. Theory Related Fields, 158 no. 1-2, 197–224.
- [28] Kim, J. H. and Vu, V. H. (2000). Concentration of multivariate polynomials and its applications. Combinatorica, 20 no. 3, 417–434.
- [29] Kim, J. H. and Vu, V. H. (2004). Divide and conquer martingales and the number of triangles in a random graph. Random Structures Algorithms, 24 no. 2, 166–174.
- [30] Lata la, R. (1997). Estimation of moments of sums of independent real random variables. Ann. Probab., 25 no. 3, 1502–1513.
- [31] Lovasz,´ L. (2012). Large networks and graph limits. American Mathematical Society, Providence, RI.
- [32] Lubetzky E. and Zhao, Y. (2014). On the variational problem for upper tails of triangle counts in sparse random graphs. arXiv preprint arXiv:1402.6011
- [33] Lubetzky, E. and Zhao, Y. (2015). On replica symmetry of large deviations in random graphs. Random Structures Algorithms, 47 no. 1, 109–146.
- [34] McDiarmid, C. (1989). On the method of bounded diﬀerences. In Surveys in combinatorics, 148–188, London Math. Soc. Lecture Note Ser., 141, Cambridge Univ. Press, Cambridge.
- [35] Szemer´edi, E. (1978). Regular partitions of graphs. Probl`emes combinatoires et th´eorie des graphes (Colloq. Internat. CNRS, Univ. Orsay, Orsay, 1976), pp. 399–401, Colloq. Internat. CNRS, 260, CNRS, Paris.


- [36] Talagrand, M. (1995). Concentration of measure and isoperimetric inequalities in product spaces. Inst. Hautes Etudes´ Sci. Publ. Math. 81 73–205.
- [37] Tao, T. and Vu, V. H. (2006). Additive combinatorics. Cambridge University Press.
- [38] Vu, V. H. (2001). A large deviation result on the number of small subgraphs of a random graph. Combin. Probab. Comput., 10 no. 1, 79–94.
- [39] Vu, V. H. (2002). Concentration of non-Lipschitz functions and applications. Probabilistic methods in combinatorial optimization. Random Structures Algorithms, 20 no. 3, 262–316.


Department of Statistics Stanford University Sequoia Hall, 390 Serra Mall Stanford, CA 94305

souravc@stanford.edu adembo@stanford.edu

