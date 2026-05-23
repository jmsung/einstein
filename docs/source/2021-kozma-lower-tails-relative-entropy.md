---
type: source
kind: paper
title: Lower tails via relative entropy
authors: Gady Kozma, Wojciech Samotij
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2104.04850v1
source_local: ../raw/2021-kozma-lower-tails-relative-entropy.pdf
topic: general-knowledge
cites:
---

arXiv:2104.04850v1[math.PR]10Apr2021

LOWER TAILS VIA RELATIVE ENTROPY

GADY KOZMA AND WOJCIECH SAMOTIJ

Abstract. We show that the naive mean-ﬁeld approximation correctly predicts the leading term of the logarithmic lower tail probabilities for the number of copies of a given subgraph in G(n, p) and of arithmetic progressions of a given length in random subsets of the integers in the entire range of densities where the mean-ﬁeld approximation is viable.

Our main technical result provides suﬃcient conditions on the maximum degrees of a uniform hypergraph H that guarantee that the logarithmic lower tail probabilities for the number of edges induced by a binomial random subset of the vertices of H can be well-approximated by considering only product distributions. This may be interpreted as a weak, probabilistic version of the hypergraph container lemma that is applicable to all sparser-than-average (and not only independent) sets.

1. Introduction

This paper is concerned with the phenomenon that, in many cases, conditioning on an atypical event leads to a mixture of product measures. An emblematic is the family of n-vertex graphs with no triangles. It is clear that if one divides n := {1,... ,n} into two parts and takes only edges with one endpoint in each part, the resulting graph has no triangles. The classical result of Erd˝os, Kleitman, and Rothschild [18] states that the vast majority of triangle-free graphs have such simple structure. In other words, if we condition the random graph G(n, 21) to have no triangles, the resulting measure can be approximated by the following process: First, choose a random partition of the vertices into two parts (according to a measure that strongly favours partitions into approximately equal parts). Then, choose the edges randomly and independently, with edges between the parts having probability 12 and edges inside the parts having probability 0. Since, conditioned on the partition, the measure becomes a product measure, the overall process is called a mixture of product measures.

![image 1](<2021-kozma-lower-tails-relative-entropy_images/imageFile1.png>)

![image 2](<2021-kozma-lower-tails-relative-entropy_images/imageFile2.png>)

The aim of this work is to establish suﬃcient conditions for such a phenomenon to occur in the context of large deviations for subgraph counts in the binomial random graph G(n,p). Here, the seminal work of Chatterjee and Varadhan [9] has clariﬁed that there are in fact two independent steps involved. The ﬁrst is to show that the distribution of the random graph conditioned on a tail event can be described by a (small) mixture of product measures. The second is to describe the relevant measures, which, as it turns out, are those among all product measures (essentially) supported on the relevant tail event that have the least entropic cost. The main result of [9] completes the ﬁrst of these two steps and can be summarised1 as follows: Denote by Xn the number of copies of a given graph in the binomial random graph G(n,p). If the edge probability p is ﬁxed and n tends to inﬁnity, then

− log P Xn (1 + δ)E[Xn] = (1 + o(1)) · Φn,p(δ), (1)

where Φn,p(δ) is the least entropic cost of a product measure supported on the upper tail event (we will give a formal deﬁnition below); the analogous result holds for the lower tail. As for the second step, the problem of calculating Φn,p(δ) turned out to be very diﬃcult. Even in the

![image 3](<2021-kozma-lower-tails-relative-entropy_images/imageFile3.png>)

This research was supported in part by the Jesselson Foundation and by Paul and Tina Gardner (GK) and by the Israel Science Foundation grant 1145/18 (WS).

1The setting of [9] is more general, but let us not state the full generality of that paper here.

1

seemingly simple case of triangle counts, only partial results are known [25, 30]. In this paper, we address only the ﬁrst step, namely, obtaining an identity akin to (1).

A substantial drawback of the approach taken by [9], which is based on Szemere´di’s regularity lemma, is that it does not extend to sparse random graphs. (One may instead use the so-called weak regularity lemma of Frieze and Kannan [19], but this allows one to extend (1) only to the regime p (log n)−c, for some small positive constant c, see [26].) This was ﬁrst rectiﬁed by the breakthrough work of Chatterjee and Dembo [8], who developed a general technique for computing large deviation probabilities of nonlinear functions of independent Bernoulli random variables, such as subgraph counts in G(n,p). In the context of subgraph counts in G(n,p), the general result of [8] implies that (1) continues to hold as long as p n−α for some α > 0 that depends only on the graph whose copies are counted.

The paper of Chatterjee and Dembo inspired a series of further developments. Their general technique was further simpliﬁed and strengthened by Eldan [17]. In the context of upper tails for subgraph counts in G(n,p), the range of validity of the approximation (1) was further extended by the works of Augeri [1] (for cycles), of Cook and Dembo [11] (for arbitrary graphs), and of Cook, Dembo, and Pham [12] (for arbitrary graphs and, more generally, arbitrary uniform hypergraphs). The expression Φn,p(δ) in the right-hand side of (1) was computed in the range n−1/∆ ≪ p ≪ 1, where ∆ is the maximum degree of the graph for cliques [26] and, subsequently, for arbitrary subgraphs [6]. A very diﬀerent, combinatorial technique for computing upper tail probabilities of polynomials of independent Bernoulli random variables was recently developed by Harel, Mousset, and Samotij [20]. This technique was used to resolve the upper tail problem completely for cliques [20] and, subsequently, for all regular graphs [5]. More precisely, these works showed that the approximation (1) is valid in the entire range of densities p where it was expected to hold.

Let us stress that all of the works on large deviations of subgraph counts in sparse random graphs mentioned above were primarily concerned with the upper tail. (In fact, the techniques developed in both [1] and [20] are inapplicable to the lower tail problem.) Historically, the upper tail problem is considered to be more diﬃcult of the two. Whereas Janson,  Luczak, and Rucin´ski [22] determined the logarithm of the lower tail probability up to a multiplicative constant, for every graph and all densities p, already in the late 1980s, the order of magnitude of the logarithm of the upper tail probability in the special case of triangle counts was determined only around ten years ago [7, 16].

In this paper, we oﬀer a new, entropy-based approach to the large deviation problem that is particularly eﬀective in estimating lower tails. The idea of using entropy estimates for studying nonlinear large deviations was ﬁrst used in [24] (that paper is a few years older than the current one, unlike what one might think by examining arXiv submission dates). Ultimately it stems from Avez’s entropy approach to study random walks and amenability, see [2]. A straightforward corollary of our main technical result is that the analogue of (1) holds for counts of arbitrary subgraphs in G(n,p) in the entire range where such an approximation was expected to be valid.

- 1.1. New results. We start with a special case of our result for triangles and p = 21. Of course, this case is mostly covered by [9], but we will get to values of p not covered by the literature in Theorem 2 below. We ﬁrst state the minimisation problem that formalises the phrase ‘least


![image 4](<2021-kozma-lower-tails-relative-entropy_images/imageFile4.png>)

entropic cost’ in this setting. Given a function q: n 2 → [0,1], let G(n,q) denote the random graph obtained by retaining each edge e of Kn independently with probability qe. For each t 0, deﬁne

Qt := q ∈ [0,1]( n 2 ) : E NK3 G(n,q) t ,

where NK3(G) is the number of triangles in G, and

 

 

Φn(t) := min

qe log qe + (1 − qe)log(1 − qe) + log 2 : q ∈ Qt

. (2)

 e∈



( n 2 )

Note that q log q + (1 − q)log(1 − q) + log 2 is the diﬀerence in entropies of Bernoulli random variables with success probabilities 12 and q.

![image 5](<2021-kozma-lower-tails-relative-entropy_images/imageFile5.png>)

- Theorem 1. Let Xn denote the number of triangles in G(n, 21). For every n and every t 0, log P(Xn t) −Φn(t + n23/8) + 2n15/8. (3)

![image 6](<2021-kozma-lower-tails-relative-entropy_images/imageFile6.png>)

Remark. Note that the two error terms in the above estimate are better than o(n3) and o(n2), respectively. In the remainder of this paper, we follow the literature and prove results with error terms in the corresponding estimates of the lower tail probabilities being inexplicit, but here we made an exception.

We now formulate a general result concerning the lower tail of subgraph counts in G(n,p). In order to phrase the minimisation problem in the case p = 21, it is convenient to ﬁrst deﬁne

![image 7](<2021-kozma-lower-tails-relative-entropy_images/imageFile7.png>)

ip(q) := q log

q p

![image 8](<2021-kozma-lower-tails-relative-entropy_images/imageFile8.png>)

+ (1 − q)log

1 − q 1 − p

![image 9](<2021-kozma-lower-tails-relative-entropy_images/imageFile9.png>)

.

Further, given graphs H and G, let NH(G) denote the number of copies of H in G. For every graph H, integer n, real p ∈ (0,1), and every η ∈ [0,1], let

ΦHn,p(η) := min

 

 e∈

( n 2 )

ip(qe) : E NH G(n,q) η · E NH G(n,p)

 



,

where the minimum is taken over all q ∈ [0,1]( n 2 ), of course. Recall that the 2-density of a graph H is the quantity m2(H) deﬁned as follows: If H has at least two edges, then

m2(H) := max

eF − 1 vF − 2

![image 10](<2021-kozma-lower-tails-relative-entropy_images/imageFile10.png>)

: F ⊆ H,eF 2 ;

otherwise, m2(H) := 21. The notation F ⊆ H here means that F is a subgraph of H. For example, m2( ) = 2 but m2( ) = 52 because the maximum is attained at the subgraph .

![image 11](<2021-kozma-lower-tails-relative-entropy_images/imageFile11.png>)

![image 12](<2021-kozma-lower-tails-relative-entropy_images/imageFile12.png>)

- Theorem 2. For every nonempty graph H, all p0 < 1, and every ε > 0, there exists a constant L such that the following holds: Suppose that Ln−1/m2(H) p p0 and let X := NH G(n,p) . Then, for every η ∈ [0,1],


(1 − ε) · ΦHn,p(η + ε) −log P X ηE[X] (1 + ε) · ΦHn,p (1 − ε)η .

A key feature of Theorem 2 is that the lower-bound assumption on p is optimal up to constants. To see this, note ﬁrst that, by Harris’s inequality, for every F ⊆ H,

P(X = 0) = P H G(n,p) P F G(n,p) (1 − peF )nvF exp(−2nvF peF ).

Moreover, m2(H) is deﬁned so that nvF peF = o(n2p) for some F ⊆ H precisely when p ≪ n−1/m2(H). On the other hand, for all H, n, p, and η < 1, we have ΦHn,p(η) cn2p for some positive c that depends only on H and η (see Lemma 22 below).

The boundary case η = 0 in Theorem 2, the probability that a random graph is H-free, has been extensively studied in the literature. In particular,  Luczak [27] computed the asymptotics of log P K3 G(n,p) for all p ≫ n−1/m2(K3) and derived an asymptotic formula for log P H G(n,p) , for every nonbipartite graph H and all p ≫ n−1/m2(H), from the so-called

- K LR conjecture [23], which was proved some ﬁfteen years later by Balogh, Morris, and Samotij [3] and by Saxton and Thomason [28]. In fact, the hypergraph container theorems proved in [3, 28]


can be used to compute the asymptotics of the logarithms of these probabilities directly, using simple, well-known results in extremal graph theory, see [3, §1.3].

Our methods allow us to generalise Theorem 2 to s-uniform hypergraphs in a straightforward way. Suppose that H is a nonempty s-uniform hypergraph. The s-density of H is the quantity ms(H) deﬁned as follows: If H has at least two edges, then

eF − 1 vF − s

ms(H) := max

: F ⊆ H,eF 2 ; (4)

![image 13](<2021-kozma-lower-tails-relative-entropy_images/imageFile13.png>)

otherwise, ms(H) := 1s. For every integer n, real p ∈ (0,1), and every η ∈ [0,1], we deﬁne ΦHn,p(η) analogously to the graph case:

![image 14](<2021-kozma-lower-tails-relative-entropy_images/imageFile14.png>)

 

 

ip(qe) : E NH G(s)(n,q) η · E NH G(s)(n,p)

ΦHn,p(η) := min

,



 e∈

( n s )

- where G(s)(n,q) is the binomial random s-uniform hypergraph with vertex set n .


- Theorem 3. For every nonempty s-uniform hypergraph H, all p0 < 1, and every ε > 0, there exists a constant L such that the following holds: Suppose that Ln−1/ms(H) p p0 and let X := NH G(s)(n,p) . Then, for every η ∈ [0,1],

(1 − ε) · ΦHn,p(η + ε) −log P X ηE[X] (1 + ε) · ΦHn,p (1 − ε)η .

As in Theorem 2, the lower-bound assumption on p in Theorem 3 is optimal and the asymptotics of log P(X = 0) can be derived from the hypergraph container theorems.

The ﬁnal application of our new entropy method is a solution to the lower tail problem for the number of arithmetic progression of a give length in a binomial random subset of n , which will demonstrate that symmetry is not crucial for our methods. Given a function q: n → [0,1], we denote by n q the random subset of n obtained by independently retaining each i ∈ n with probability qi. For a positive integer k and a set I ⊆ n , let Ak(I) denote the number of k-term arithmetic progressions in I.

- Theorem 4. For every positive integer k, all p0 < 1, and every ε > 0, there exists a constant L such that the following holds: Suppose that Ln−1/(k−1) p p0 and let X := Ak n p . Then, for every η ∈ [0,1],


(1 − ε) · Φkn,p(η + ε) −log P X ηE[X] (1 + ε) · Φkn,p (1 − ε)η .

As before, the lower-bound assumption on p in Theorem 4 is optimal and the asymptotics of log P(X = 0) can be derived from the hypergraph container theorems, see [3, Theorem 1.1].

- 1.2. The main technical result. A natural way to generalise Theorems 2, 3, and 4 is to represent the combinatorial objects we are counting as edges of an auxiliary hypergraph (no relation to the hypergraphs of Theorem 3). This way, each of the respective random variables counts the number of edges of such a hypergraph that are induced by random subset of its vertices. This idea is not new – the transference principles of Conlon and Gowers [10] and Schacht [29] and the hypergraph container theorems [3, 28] are prime examples of why taking such an abstract viewpoint may prove beneﬁcial in our context. For example, in order to express the number of triangles in G(n,p) this way, we consider the 3-uniform hypergraph with vertex


set n 2 , the edge set of the complete graph on n , whose hyperedges are the n3 triples of edges that form triangles in the complete graph on n .

We are thus led to ask the following general question: Given a hypergraph H and a p ∈ [0,1], what is the probability that a random subset of the vertices of H formed by independently retaining each vertex with probability p contains atypically few hyperedges? For extra generality, we allow the edges of the hypergraph to have positive weights.

Suppose that a hypergraph H is equipped with a weight function d: H → (0,∞). We shall

denote by e(H ) the sum A∈H dA of all edge weights and, for every set B ⊆ V (H ), we shall write

degH B :=

dA. (5) Moreover, for every s ∈ r , we deﬁne

B⊆A∈H

∆s(H ) := max {degH B : B ⊆ V and |B| = s}.

Note that when dA = 1 for every A ∈ H , then we may simply view H as a hypergraph; in this case, the above deﬁnitions give the usual notions of edge counts and degrees.

Let H be a hypergraph and denote V = V (H ) for brevity. Let Y = (Yv)v∈V be a sequence of i.i.d. Bernoulli random variables with success probability p, one for every vertex of the hypergraph H , and let R be the corresponding random subset of V , i.e., R := {v ∈ V : Yv = 1}. For a function q: V → [0,1], we let Y (q) = (Yv′)v∈V be a sequence of independent Bernoulli random variables such that Yv′ has success probability qv for each v ∈ V and let R(q) be the corresponding random subset of V . For every nonnegative real η, deﬁne

ΦHp (η) := min DKL Y (q) Y : q ∈ [0,1]V and E[e(H [R(q)])] η · E[e(H [R])] , (6) where DKL is the Kullback–Leibler divergence, so that,

1 − qv 1 − p

qv p

DKL Y (q) Y =

+ (1 − qv)log

.

ip(qv) =

qv log

![image 15](<2021-kozma-lower-tails-relative-entropy_images/imageFile15.png>)

![image 16](<2021-kozma-lower-tails-relative-entropy_images/imageFile16.png>)

v∈V

v∈V

Here and below, H [R] stands for the restriction of H to R, namely the hypergraph whose vertices are R and whose hyperedges are {A ∈ H : A ⊆ R}; thus e(H [R]) = A⊆R dA. Also, for W ⊆ V (H ), we write H − W in place of H [V (H ) \ W].

- Theorem 5. For every integer r and all p0 < 1, ε > 0, and K, there exists a positive λ and a C such that the following holds. Let V be a ﬁnite set and let H be a nonempty r-uniform hypergraph with vertex set V and weight function d: H → (0,∞). Let p ∈ (0,p0] and let R be the p-random subset of V . Suppose that, for every s ∈ r , the maximal degree ∆s(H ) satisﬁes


e(H ) v(H )

∆s(H ) K · (λp)s−1 ·

. (7)

![image 17](<2021-kozma-lower-tails-relative-entropy_images/imageFile17.png>)

- Then, letting X := e(H [R]), for every nonnegative real η, −log P X ηE[X] (1 − ε)ΦHp (η + ε) − C.


Remark. Our argument gives the following explicit dependence of λ and C on the parameters: λ 10−5K−2r−4ε9(1 − p0) and C 106K2r5ε−9(1 − p0)−1 log

1 1 − p0

.

![image 18](<2021-kozma-lower-tails-relative-entropy_images/imageFile18.png>)

The readers familiar with the hypergraph container method will likely notice striking similarities between the assumptions of Theorem 5 and the assumptions of the container lemmas proved in [3, 4]. This is not a coincidence – the boundary case η = 0 in Theorem 5 bounds the probability that the random set R is independent in H from above by ΦHp (ε), a minimum over all distributions q ∈ [0,1]V such that R(q) induces at most εe(H ) edges in H , in expectation (cf. the combinatorial notion of containers for independent sets in [3, 28]).

While it might be tempting to replace ΦHp (η + ε) in the assertion of Theorem 5 with ΦHp (η), or at least ΦHp ((1 + ε)η), this is not always possible for η very close to zero. To see this, observe ﬁrst that ΦHp (0) = (α(H ) − v(H )) · log(1 − p), where α(H ) is the largest size of an independent set in H . Suppose now that H is the union of two hypergraphs with the same vertex set V : a dense hypergraph H1 with α(H1) v(H )/2 and a very sparse hypergraph H2 with α(H2) v(H )/4. (For example, if M and v(H ) are suﬃciently large as a function of

the uniformity r only, then a random hypergraph with Mv(H ) edges will typically have this property). Now, on the one hand,

1 1 − p

3v(H ) 4 · log

ΦHp (0) α(H2) − v(H ) · log(1 − p)

![image 19](<2021-kozma-lower-tails-relative-entropy_images/imageFile19.png>)

![image 20](<2021-kozma-lower-tails-relative-entropy_images/imageFile20.png>)

but, on the other hand, by Harris’s inequality, the p-random subset of some largest independent set of H1 has probability at least (1 − pr)e(H2) to be independent also in H2 and thus, when p is suﬃciently small,

P(X = 0) (1 − p)v(H )−α(H1) · e−2pre(H2) (1 − p)2v(H )/3, showing that −log P(X = 0) is not close to ΦHp (0).

For easier comparison with the literature, let us reformulate Theorem 5 in the language of polynomials. We retain the notations V , Y , and Y (q) as above. We replace a weighted hypergraph H with a homogeneous polynomial f by turning each edge A of H with the monomial dA · v∈A yv. The deﬁnition of Φ thus becomes

Φfp(η) = min DKL(Y (q) Y ) : q ∈ [0,1]V ,E[f(Y (q))] η · E[f(Y )] . Moreover, the assumption (7) can be now expressed in terms of partial derivatives of f. Given a B = {v1,... ,vk} ⊆ V and a polynomial f in |V | variables, we denote

∂ ∂vk

∂ ∂v1 ···

∂Bf :=

f. The following statement is a reformulation of Theorem 5.

![image 21](<2021-kozma-lower-tails-relative-entropy_images/imageFile21.png>)

![image 22](<2021-kozma-lower-tails-relative-entropy_images/imageFile22.png>)

- Theorem 6. For every integer r and all p0 < 1, ε > 0, and K, there exists a positive λ and a C such that the following holds. Let V be a ﬁnite set and let f be an r-homogeneous V -variate

multilinear polynomial with nonnegative coeﬃcients. Let p ∈ (0,p0] and let Y = (Yv)v∈V be a sequence of i.i.d. Ber(p) random variables. Suppose that, for every nonempty B ⊆ V with |B| r,

∂Bf(1) K · (λp)|B|−1 ·

f(1) |V |

![image 23](<2021-kozma-lower-tails-relative-entropy_images/imageFile23.png>)

.

- Then, letting X := f(Y ), for every nonnegative real η, −log P X ηE[X] (1 − ε)Φfp(η + ε) − C.


When f is a linear function, the variable X from the statement of the theorem is a sum of independent random variables. In this case, our argument can be simpliﬁed tremendously. The special case f(y) = y1 + ··· + yn, which corresponds to the binomial distribution, is treated in §4.2, where a short, entropy-based proof of the optimal tail estimate

P Bin(n,p) nq exp − n · ip(q) is given.

1.3. Lower bounds on the lower tail. We end the results section with a lower bound on the lower tail probabilities from the statements of Theorems 5 and 6 that matches the upper bounds proved by these theorems. Since the proof of this lower bound is a relatively standard tilting argument, we relegate it to §6. Here is the exact formulation (in the language of Theorem 6).

- Theorem 7. For every p0 < 1 and ε > 0, there exists a C such that the following holds. Let V be a ﬁnite set, let Y = (Yv)v∈V be a sequence of i.i.d. Ber(p) random variables, let f : {0,1}V → [0,∞) be an arbitrary increasing function, and let X := f(Y ). Then, for every nonnegative real η,


−log P X ηE[X] (1 + ε)Φfp (1 − ε)η + C.

- 1.4. Organisation of the paper. The remainder of this paper is organised as follows. In Section 2, we outline of the proof of Theorem 1 and discuss some of the additional ideas required


in the proof of Theorem 2 in the case H = K3. In Section 3, which is merely three pages long, we present a complete proof of Theorem 1. In Section 4, we recall some basic properties of the Kullback–Leibler divergence and prove the key technical lemma (Lemma 16) that relates independence and conditional KL-divergence. Subsection 4.2 contains a short entropy-based proof of optimal tail bounds for binomial distributions, which might be of independent interest. Our main technical result, Theorem 5, is proved in Section 5. The matching lower bound for lower tail probabilities, Theorem 7, is proved in Section 6. Finally, Section 7 contains short derivations of Theorems 2, 3, and 4.

2. Proof outline

- 2.1. Triangle count in G(n, 21). Let us ﬁrst explain how to prove Theorem 1, i.e., the upper


![image 24](<2021-kozma-lower-tails-relative-entropy_images/imageFile24.png>)

bound on the lower tail of the number of triangles. Considering only G(n, 12), which is the uniform distribution on n-vertex graphs, allows us to phrase the argument in the familiar language

![image 25](<2021-kozma-lower-tails-relative-entropy_images/imageFile25.png>)

of entropy rather than using the Kullback–Leibler divergence. The argument sketched here is described in full in §3 and takes no more than three pages.

Let Y be the random graph G(n, 12) conditioned on having at most t triangles. Then log P(X t) = H(Y ) −

![image 26](<2021-kozma-lower-tails-relative-entropy_images/imageFile26.png>)

n 2

log 2, (8)

where H is the entropy of Y . Examine the distribution of the ﬁrst edge (i.e., of Y12) under the conditioning.2 For every integer r 0, let

hr := H(Y12 | edges with at least one endpoint larger than n − r),

- where H(· | ·) is the usual conditional entropy. Since conditional entropy is nonnegative and it decreases as one increases the conditioning, we have 0 hr+1 hr for every r. Since h0 = H(Y12) log 2, there must be some r √n such that hr − hr+1 C/√n, where C is an absolute constant.


![image 27](<2021-kozma-lower-tails-relative-entropy_images/imageFile27.png>)

![image 28](<2021-kozma-lower-tails-relative-entropy_images/imageFile28.png>)

Denote by Sr the edges from the deﬁnition of hr, so that hr = H(Y12 | Sr). Since both {1,n−r} and {2,n−r} belong to Sr+1\Sr, we may use the monotonicity of conditional entropy again to sandwich H(Y12 | Sr,Y1,n−r,Y2,n−r) between hr and hr+1:

hr+1 = H(Y12 | Sr+1) H(Y12 | Y1,n−r,Y2,n−r,Sr) H(Y12 | Sr) = hr. Hence, we also get the inequality

H(Y12 | Sr) − H(Y12 | Y1,n−r,Y2,n−r,Sr) C/√n. By symmetry, we may replace (1,2,n − r) in the above inequality with any three diﬀerent elements (i,j,k) of n − r and get

![image 29](<2021-kozma-lower-tails-relative-entropy_images/imageFile29.png>)

H(Yij | Sr) − H(Yij | Yik,Yjk,Sr) C/√n. We now apply Pinsker’s inequality, which states that, for any two variables T and U, if H(T)− H(T | U) is small, then T and U must be approximately independent. We apply this to the variables Yij conditioned on Sr to conclude that, conditioned on Sr, the three edges of every triangle are (typically) approximately independent.

![image 30](<2021-kozma-lower-tails-relative-entropy_images/imageFile30.png>)

Recall now the deﬁnition of Φn(t). It is the minimum of −H G(n,q) + n2 log 2 over all functions q: n 2 → [0,1] such that

T(q) := E #triangles in G(n,q) t.

![image 31](<2021-kozma-lower-tails-relative-entropy_images/imageFile31.png>)

2We assume that the vertex set of G(n, 12) is n and think of Y ∈ {0, 1}( n 2 ) as the characteristic vector of the edge set of the conditioned random graph.

![image 32](<2021-kozma-lower-tails-relative-entropy_images/imageFile32.png>)

Consider the function qij := E[Yij | Sr]. The approximate independence of the Yij gives that T(q) is (typically) approximately the expected number of triangles in Y , which is at most t, by the deﬁnition of Y . Hence, T(q) t + o(t), where the o(t) error term comes from the fact that the Yij are only approximately independent. We conclude that

H (Yij)i,j n−r | Sr

H(Yij | Sr) −Φn(t + o(t)) +

i,j n−r

n 2

Since Sr has only at most n3/2 edges, its entropy is negligible and we get

log 2.

H(Y ) = H(Sr) + H (Yij)i,j n−r | Sr (1 − o(1)) · Φn(t + o(t)) +

n 2

log 2,

as needed.

Examining the proof above, we see that the crucial step is that of proving conditional approximate independence. Why was the conditioning necessary? Because Y is not close to a product measure but rather a mixture of product measures. Heuristically, the conditioning chooses one product measure from the mixture.

- 2.2. Triangle count in G(n,p) and beyond. What is needed to prove Theorem 1 with G(n, 21) replaced by G(n,p)? Since the latter is no longer a uniform distribution, in order to phrase a suitable analogue of (8), we certainly have to replace entropy with entropy relative to a product of p-Bernoulli variables (relative entropy is also called the Kullback–Leibler divergence, though note that the sign of the Kullback–Leibler divergence is minus that of what a straightforward analogue of entropy would have) and we need an analogue of Pinsker’s inequality for (conditional) relative entropy. These two ideas would have been enough to solve the lower tail (as well as the upper tail) problem for triangles in G(n,p) for all p n−c, where c is an absolute positive constant.


![image 33](<2021-kozma-lower-tails-relative-entropy_images/imageFile33.png>)

In order to extend the argument to all p ≫ n−1/2, one needs to prove a version of Pinsker’s inequality that provides a stronger upper bound on the diﬀerence of probabilities that two measures assign to rare events (rather than arbitrary events, as measured by the total variation distance). Furthermore, in order to use this strengthening of Pinsker’s inequality, we also need to note that, when we condition our random graph on the lower tail event, the probability of every edge is at most p, even when we further condition on Sr. This follows from the Harris inequality (aka the FKG inequality). The use of Harris’s inequality is the main (but not the only) reason why our methods are not as eﬃcient for the upper tail problem.

The general setting of Theorem 5, which lacks symmetry, requires a serious overhaul of the argument. (Having said that, even in the setting of K4 counts in G(n,p), which still has a lot of symmetry, the argument sketched above does not work under the optimal assumption

- p ≫ n−2/5.) We no longer increase the conditioning in small steps (recall the deﬁnition of hr above) but rather in large chunks, which are chosen randomly. The crux of the matter is relating the decrease in entropy caused by conditioning on each such random chunk to approximate independence of the remaining variables. Here, the key role is played by Lemma 16, an improvement of Pinsker’s inequality that is inspired by the statement of Janson’s inequality [21].


3. The lower tail of triangle count in G(n, 21)

![image 34](<2021-kozma-lower-tails-relative-entropy_images/imageFile34.png>)

As explained above, our proof of Theorem 1 revolves around (information-theoretic) entropy. For convenience of the reader, we shall recall here the deﬁnitions of entropy and conditional entropy and list all of their properties required for our argument; for proofs of these properties, we refer the reader to [13, Chapter 2].

- 3.1. Preliminaries. The entropy of a random variable X taking values in a ﬁnite set X is the quantity H(X) deﬁned by


P(X = x)log P(X = x).

H(X) := −

x∈X

Further, given two random variables X and Y that take values in ﬁnite sets X and Y , respectively, and have a joint distribution, the (conditional) entropy of X conditioned on Y is the quantity H(X | Y ) deﬁned as follows:

P(Y = y)H X{Y =y} ,

H(X | Y ) :=

y∈Y

where X{Y =y} denotes X conditioned on the event that Y = y, so that, for every x ∈ X and every y ∈ Y with P(Y = y) = 0,

P(X = x, Y = y) P(Y = y)

P X{Y =y} = x =

.

![image 35](<2021-kozma-lower-tails-relative-entropy_images/imageFile35.png>)

The above deﬁnitions ensure that entropies and conditional entropies are always nonnegative. Moreover, it is easy to verify that

H(X | Y ) = H(X,Y ) − H(Y ). (9)

In the remainder of this section, a discrete random variable will mean a random variable taking values in some ﬁnite set. The following elementary inequalities should be familiar to readers who have encountered the notion of entropy.

- Lemma 8. Suppose that X, Y , and Z are discrete random variables and that X takes values in a ﬁnite set X . We have:

- (i) H(X) log |X | and equality holds iﬀ X is uniform on X ;
- (ii) H(X | Y ) H(X) and equality holds iﬀ X and Y are independent;
- (iii) H(X | Y,Z) H(X | Y );
- (iv) H(X,Y | Z) H(X | Z) + H(Y | Z).


The main ingredient in our proof is Pinsker’s inequality (see [15, Problem 3.18]), which, in our context, can be viewed as a ‘stability’ version of (ii) in Lemma 8. The statement requires the following notation: For two random variables X and Y , we denote by X × Y the random variable obtained by ﬁrst letting X˜ and Y˜ be two independent copies of X and Y , respectively, and then deﬁning X × Y = (X,˜ Y˜). In other words, L (X × Y ) = L (X) × L (Y ), where, as usual, L (X) stands for the law of X, i.e., the measure induced by X on its space of values.

- Lemma 9. Suppose that X and Y are discrete random variables. We have


![image 36](<2021-kozma-lower-tails-relative-entropy_images/imageFile36.png>)

dTV (X,Y ),X × Y 2 H(X) − H(X | Y ) , where dTV denotes the total variation distance.

- 3.2. The argument. Let Y denote the random graph G(n, 21) conditioned on having at most t triangles. In other words, Y is a uniformly chosen random graph with vertex set n := {1,... ,n} and at most t triangles. In particular, Lemma 8(i) implies that


![image 37](<2021-kozma-lower-tails-relative-entropy_images/imageFile37.png>)

log P(Xn t) = H(Y ) −

n 2

log 2. (10)

In order to bound the entropy of Y from above, it will be convenient to view Y as the random vector (Ye)e∈Kn, where Ye indicates whether e is an edge of Y . For a subvector S of Y and every e ∈ Kn, we will write YeS to denote the random variable whose (random) distribution is the distribution of Ye conditioned on S, so that P(YeS = 1) = E[Ye | S]. The following lemma captures the notion of conditional approximate independence (recall the proof sketch in §2.1).

- Lemma 10. There exists a subgraph F ⊆ Kn with at most n3/2 edges and such that, for every {i,j,k} ∈ n 3 , letting S := (Yf)f∈F and


dSijk := dTV (YijS,YikS,YjkS),YijS × YikS × YjkS , we have E[dSijk] 2n−1/4.

Proof. For a nonnegative integer r, let Fr be the subgraph of Kn comprising all edges {i,j} satisfying max{i,j} > n − r, let Sr := (Yf)f∈Fr and let hr := H(Y12 | Sr). By Lemma 8(iii), the function r  → hr is decreasing and hence, for some r √n, we must have

![image 38](<2021-kozma-lower-tails-relative-entropy_images/imageFile38.png>)

h0 − h√n √n

![image 39](<2021-kozma-lower-tails-relative-entropy_images/imageFile39.png>)

hr − hr+1

. Bounding the numerator is easy. On the one hand, we have

![image 40](<2021-kozma-lower-tails-relative-entropy_images/imageFile40.png>)

![image 41](<2021-kozma-lower-tails-relative-entropy_images/imageFile41.png>)

h0 = H(Y12) log 2, as Y12 takes only two values, see Lemma 8(i); on the other hand, hr 0 for every r, as conditional entropy is always nonnegative. Thus, there must be an r with 0 r √n − 1 such that hr − hr+1 (log 2)/√n. Fix one such r and let F = Fr and S = Sr; note that e(F) rn n3/2. Since F ⊆ F ∪ {1,n − r},{2,n − r} ⊆ Fr+1, Lemma 8(iii) implies that

![image 42](<2021-kozma-lower-tails-relative-entropy_images/imageFile42.png>)

![image 43](<2021-kozma-lower-tails-relative-entropy_images/imageFile43.png>)

hr+1 = H(Y12 | Sr+1) H(Y12 | S,Y1,n−r,Y2,n−r) H(Y12 | S) = hr and, consequently,

H(Y12 | S) − H(Y12 | S,Y1,n−r,Y2,n−r) (log 2)/√n. (11)

![image 44](<2021-kozma-lower-tails-relative-entropy_images/imageFile44.png>)

By symmetry (every permutation of n − r ﬁxes F), we may replace the triple of indices (1,2,n− r) in (11) with any ordered triple (i,j,k) of distinct elements of n − r . Using the deﬁnition of conditional entropy, we may rewrite this upgraded inequality as

(log 2)/√n,

E H(YijS) − H(YijS | YikS,YjkS)

![image 45](<2021-kozma-lower-tails-relative-entropy_images/imageFile45.png>)

![image 46](<2021-kozma-lower-tails-relative-entropy_images/imageFile46.png>)

![image 47](<2021-kozma-lower-tails-relative-entropy_images/imageFile47.png>)

λSijk

where E averages over the values of S.

Fix an arbitrary triple {i,j,k} ∈ n 3 . If max{i,j,k} > n − r, then at least two out of the three pairs ij, ik, jk belong to F; consequently, at least two out the three corresponding variables YijS, YikS, YjkS are trivial (for every evaluation of S), which implies that dSijk = 0. Therefore, we may assume that {i,j,k} ∈ n− 3r . For brevity, denote A = YijS, B = YikS, and C = YjkS, so that dSijk = dTV (A,B,C),A × B × C dTV (A,B,C),A × (B,C) + dTV A × (B,C),A × B × C

= dTV (A,B,C),A × (B,C)

+dTV (B,C),B × C

. Pinsker’s inequality (Lemma 9) implies that

![image 48](<2021-kozma-lower-tails-relative-entropy_images/imageFile48.png>)

![image 49](<2021-kozma-lower-tails-relative-entropy_images/imageFile49.png>)

![image 50](<2021-kozma-lower-tails-relative-entropy_images/imageFile50.png>)

![image 51](<2021-kozma-lower-tails-relative-entropy_images/imageFile51.png>)

d1

d2

![image 52](<2021-kozma-lower-tails-relative-entropy_images/imageFile52.png>)

![image 53](<2021-kozma-lower-tails-relative-entropy_images/imageFile53.png>)

d1 12 H(A) − H(A | B,C) = 12λSijk. Further,

![image 54](<2021-kozma-lower-tails-relative-entropy_images/imageFile54.png>)

![image 55](<2021-kozma-lower-tails-relative-entropy_images/imageFile55.png>)

![image 56](<2021-kozma-lower-tails-relative-entropy_images/imageFile56.png>)

![image 57](<2021-kozma-lower-tails-relative-entropy_images/imageFile57.png>)

d2 dTV (A,B,C),(A,B) × C 12 H(C) − H(C | A,B) = 12λSjki (the ﬁrst inequality is easy to check). We conclude that

![image 58](<2021-kozma-lower-tails-relative-entropy_images/imageFile58.png>)

![image 59](<2021-kozma-lower-tails-relative-entropy_images/imageFile59.png>)

![image 60](<2021-kozma-lower-tails-relative-entropy_images/imageFile60.png>)

![image 61](<2021-kozma-lower-tails-relative-entropy_images/imageFile61.png>)

![image 62](<2021-kozma-lower-tails-relative-entropy_images/imageFile62.png>)

![image 63](<2021-kozma-lower-tails-relative-entropy_images/imageFile63.png>)

E dSijk E 12λSijk + E 12λSjki 12E[λSijk] + 12E[λSijk] 2 (log 2)/(2√n) 2n−1/4, where the second inequality follows from the Cauchy–Schwarz inequality.

![image 64](<2021-kozma-lower-tails-relative-entropy_images/imageFile64.png>)

![image 65](<2021-kozma-lower-tails-relative-entropy_images/imageFile65.png>)

![image 66](<2021-kozma-lower-tails-relative-entropy_images/imageFile66.png>)

![image 67](<2021-kozma-lower-tails-relative-entropy_images/imageFile67.png>)

![image 68](<2021-kozma-lower-tails-relative-entropy_images/imageFile68.png>)

![image 69](<2021-kozma-lower-tails-relative-entropy_images/imageFile69.png>)

Let F be the graph from the statement of Lemma 10 and let S = (Yf)f∈F, as in the claim. The chain rule for conditional entropies, identity (9) above, and Lemma 8(iv) imply that

H(Y ) = H(S) + H (Ye)e∈Kn\F | S H(S) +

H(Ye | S).

e∈Kn\F

Since S takes at most 2e(F) diﬀerent values and e(F) n3/2, we further have, by Lemma 8(i), H(Y ) n3/2 log 2 +

H(Ye | S), (12)

e∈Kn

where we also used the fact that conditional entropies are nonnegative to extend the range of the sum from Kn \ F to Kn (in fact, H(Ye | S) = 0 for every e ∈ F).

Recall that our eventual goal is to compare the entropy of Y to Φn(t), which is deﬁned as the minimum over certain functions q. Deﬁne therefore the S-measurable random function

- q: n 2 → [0,1] by letting, for each e ∈ Kn, qe := E[Ye | S] = P(YeS = 1).


Letting h: [0,1] → [0,log 2] be the function deﬁned by h(x) = −xlog x − (1 − x)log(1 − x), we may now write

H(Ye | S) = E H(YeS) = E[h(qe)]. Let XS denote the number of triangles in Y conditioned on S, that is,

XS :=

YijSYikSYjkS

{i,j,k}∈( n 3 )

and let

X¯S :=

qijqikqjk = E NK3 G(n,q) .

{i,j,k}∈( n 3 )

Recall the deﬁnition of dSijk from the statement of Lemma 10 and observe that E YijSYikSYjkS − qijqikqjk dSijk; (13)

indeed, the two terms in the left-hand side are the probabilities of the event that YijS = YikS = YjkS = 1 under the two distributions whose total variation distance is dSijk.

Let

dSijk

∆ =

{i,j,k}∈( n 3 )

and note that, by Lemma 10,

E[∆]

n 3 · 2n−1/4 n11/4. (14)

Summing (13) over all triples {i,j,k}, we obtain X¯S E XS + ∆ t + ∆, since XS t with probability one. In particular, the deﬁnition of Φn, see (2), implies that

We may conclude that

e∈Kn

log 2 − h(eq) Φn(t + ∆).

n 2

H(Ye | S) = E

h(qe)

e∈Kn

e∈Kn

Since Φn is decreasing and nonnegative, E[Φn(t + ∆)] P(∆ n23/8) · Φn(t + n23/8)

log 2 − E[Φn(t + ∆)].

(14)

1 − n−1/8 · Φn(t + n23/8).

Recalling (10) and (12), this implies that

log P(Xn t) −(1 − n−1/8) · Φn(t + n23/8) + n3/2 −Φn(t + n23/8) + 2n15/8, as Φn(t) n2 log 2 for every t. This ﬁnishes the proof of Theorem 1.

4. The Kullback–Leibler divergence

For the proof of Theorem 5, we need the notion of Kullback–Leibler divergence, or relative entropy. Let P and Q be random variables taking values in a ﬁnite set X and suppose that

- L (P) ≪ L (Q), that is, that the distribution of P is absolutely continuous with respect to the distribution of Q. Denoting by p and q the densities of P and Q, respectively, the Kullback–


Leibler divergence of P from Q (also known as the relative entropy), denoted by DKL(P Q), is deﬁned as follows:

- p(x)

![image 70](<2021-kozma-lower-tails-relative-entropy_images/imageFile70.png>)

- q(x)


DKL(P Q) :=

,

p(x)log

x∈X

where we adopt the convention that 0log 0q = 0 for all q. The assumption that L (P) ≪ L (Q), which is a concise way of saying that p(x) = 0 whenever q(x) = 0, guarantees that DKL(P Q) is well-deﬁned. A fundamental property of the KL-divergence is that it is always nonnegative; indeed, since log x x − 1 for all positive x, we have, letting X ′ = {x ∈ X : p(x) > 0},

![image 71](<2021-kozma-lower-tails-relative-entropy_images/imageFile71.png>)

q(x) p(x) x∈X ′

p(x) − q(x) = 1 −

DKL(P Q) = −

q(x) 0.

p(x)log

![image 72](<2021-kozma-lower-tails-relative-entropy_images/imageFile72.png>)

x∈X ′

x∈X ′

One easily checks that, when Q is a uniformly chosen random element of X , then DKL(P Q) = log |X | − H(P),

where H(P) is the entropy of P (deﬁned in the previous section). In particular, if P is the uniformly chosen random element of a nonempty subset A ⊆ X , then, by Lemma 8(i),

DKL(P Q) = log |X | − log |A | = −log P(Q ∈ A ).

The following property of the KL-divergence, which generalises this identity, is the beginning of our approach.

- Proposition 11. Suppose that Q is a random variable taking values in a ﬁnite set X . Suppose that A ⊆ X satisﬁes P(Q ∈ A) = 0 and let QA be the random variable Q conditioned on the event {Q ∈ A}. Then


DKL(QA Q) = −log P(Q ∈ A).

Proof. Let q: X → [0,1] be the probability density function of Q and note that the probability density function of QA is the function qA: X → [0,1] deﬁned by

q(x) P(Q∈A) if x ∈ A, 0 otherwise.

![image 73](<2021-kozma-lower-tails-relative-entropy_images/imageFile73.png>)

qA(x) :=

It follows that DKL(QA Q) =

qA(x)log

x∈X

as claimed.

qA(x) q(x)

=

![image 74](<2021-kozma-lower-tails-relative-entropy_images/imageFile74.png>)

q(x) P(Q ∈ A)

log

![image 75](<2021-kozma-lower-tails-relative-entropy_images/imageFile75.png>)

x∈A

1 P(Q ∈ A)

1 P(Q ∈ A)

= log

,

![image 76](<2021-kozma-lower-tails-relative-entropy_images/imageFile76.png>)

![image 77](<2021-kozma-lower-tails-relative-entropy_images/imageFile77.png>)

The next property of the KL-divergence is a generalisation of the chain rule for entropies, identity (9), and Lemma 8(ii). In fact, the equality in (15) below is a special case of an even more general identity, the chain rule for relative entropies, see [13, Theorem 2.5.3].

- Proposition 12. Let Q1 and Q2 be random variables taking values in ﬁnite sets X1 and X2, respectively. Suppose that (P1,P2) is an X1 × X2-valued random variable such that L (Pi) ≪ L (Qi) for each i. Let Q1 × Q2 denote a random variable whose independent coordinates have marginals Q1 and Q2, respectively; that is, L (Q1 × Q2) = L (Q1) × L (Q2). Then


DKL (P1,P2) Q1 × Q2 − DKL(P2 Q2) DKL(P1 Q1), (15) where equality holds if and only if P1 and P2 are independent.

The proof of the proposition employs the following elementary inequality, whose proof we include for the sake of completeness. Lemma 13. Suppose that I is a ﬁnite set and, for each i ∈ I, let ai and bi be nonnegative reals such that ai = 0 whenever bi = 0. Then, letting a = i∈I ai and b = i∈I bi, we have

ai bi

- a

![image 78](<2021-kozma-lower-tails-relative-entropy_images/imageFile78.png>)

- b


ai log

.

alog

![image 79](<2021-kozma-lower-tails-relative-entropy_images/imageFile79.png>)

i∈I

Moreover, equality holds above if and only if aib = abi for every i ∈ I. Proof. Without loss of generality, we may assume that ai > 0 (and thus bi > 0) for each i ∈ I. Since the function x  → −log x is strictly convex, Jensen’s inequality implies that

ai a ·

- a

![image 80](<2021-kozma-lower-tails-relative-entropy_images/imageFile80.png>)

- b


abi aib −a · log

abi aib

ai a · − log

ai bi − alog

= −a · log 1 = 0

= a ·

ai log

![image 81](<2021-kozma-lower-tails-relative-entropy_images/imageFile81.png>)

![image 82](<2021-kozma-lower-tails-relative-entropy_images/imageFile82.png>)

![image 83](<2021-kozma-lower-tails-relative-entropy_images/imageFile83.png>)

![image 84](<2021-kozma-lower-tails-relative-entropy_images/imageFile84.png>)

![image 85](<2021-kozma-lower-tails-relative-entropy_images/imageFile85.png>)

i∈I

i∈I

i∈I

ib = j∈I aaj · aabj

and the inequality is strict unless aba i

jb = 1 for every i ∈ I, as claimed.

![image 86](<2021-kozma-lower-tails-relative-entropy_images/imageFile86.png>)

![image 87](<2021-kozma-lower-tails-relative-entropy_images/imageFile87.png>)

![image 88](<2021-kozma-lower-tails-relative-entropy_images/imageFile88.png>)

Proof of Proposition 12. Let p: X1 ×X2 → [0,1] be the probability density function of (P1,P2) and, for each i ∈ {1,2}, let qi: Xi → [0,1] be the probability density function of Qi. Without loss of generality, we may assume that qi(xi) > 0 for every i ∈ {1,2} and each xi ∈ Xi. The functions p1: X1 → [0,1] and p2: X2 → [0,1] deﬁned by

p1(x1) :=

p(x1,x2) and p2(x2) :=

p(x1,x2)

x2∈X2

x1∈X1

are the probability density functions of P1 and P2, respectively. Now, denoting by L the left-hand side of (15), we have

- p2(x2)

![image 89](<2021-kozma-lower-tails-relative-entropy_images/imageFile89.png>)

- q2(x2)


- p(x1,x2)

![image 90](<2021-kozma-lower-tails-relative-entropy_images/imageFile90.png>)

- q1(x1)q2(x2) − x2∈X2


p2(x2)log

p(x1,x2)log

L =

(x1,x2)∈X1×X2

- p(x1,x2)

![image 91](<2021-kozma-lower-tails-relative-entropy_images/imageFile91.png>)

- q1(x1)p2(x2)


(=∗)

p(x1,x2)log

x1∈X1 x2∈X2

p(x1,x2) x2∈X2 q1(x1)p2(x2)

(†)

p(x1,x2) log x2∈X2

![image 92](<2021-kozma-lower-tails-relative-entropy_images/imageFile92.png>)

x1∈X1 x2∈X2

- p1(x1)

![image 93](<2021-kozma-lower-tails-relative-entropy_images/imageFile93.png>)

- q1(x1)


=

= DKL(P1 Q1),

p1(x1)log

x1∈X1

1∈X1 p(x1,x2) to the second sum and (†) follows by applying Lemma 13 to the inner sum.

where (∗) follows by applying p2(x2) = x

- 4.1. Divergence from a vector of i.i.d. Bernoulli variables. Throughout this paper, we shall be estimating divergences of random variables from vectors of independent Ber(p) random variables. In view of this, it will be convenient for us to deﬁne, for a real p ∈ (0,1), an integer k 1, and a random variable X taking values in {0,1}k, the p-divergence Ip(X) of X by


Ip(X) := DKL X Ber(p)k 0. (16)

When X is Bernoulli itself, say with parameter q, then Ip(X) is a function of q which we will denote by ip. Namely,

1 − q 1 − p

q p

ip(q) := Ip Ber(q) = DKL Ber(q) Ber(p) = q log

+ (1 − q)log

. (17)

![image 94](<2021-kozma-lower-tails-relative-entropy_images/imageFile94.png>)

![image 95](<2021-kozma-lower-tails-relative-entropy_images/imageFile95.png>)

Let us record here, for future reference, that, for every q ∈ (0,1),

1 − q 1 − p

q p − log

1 q

1 1 − q

i′p(q) = log

and i′′p(q) =

+

. (18)

![image 96](<2021-kozma-lower-tails-relative-entropy_images/imageFile96.png>)

![image 97](<2021-kozma-lower-tails-relative-entropy_images/imageFile97.png>)

![image 98](<2021-kozma-lower-tails-relative-entropy_images/imageFile98.png>)

![image 99](<2021-kozma-lower-tails-relative-entropy_images/imageFile99.png>)

We also deﬁne a notion of conditional divergence. Given random variables X and Y that have a joint distribution and such that X takes values in {0,1}k for some integer k 1, we deﬁne the conditional p-divergence of X conditioned on Y

Ip(X | Y ) := E Ip XY = E DKL XY Ber(p)k ,

where XY denotes the random variable X conditioned on Y , cf. the deﬁnition of conditional entropy.

It is straightforward to verify that, when X takes values in {0,1}k,

I1/2(X) = k log 2 − H(X) and I1/2(X | Y ) = k log 2 − H(X | Y ) (19)

and therefore it should not come at a surprise that the divergence and the conditional divergence deﬁned above satisfy similar inequalities as entropy and conditional entropy, such as the ones presented in Lemma 8, only in reverse. In particular, Proposition 12 implies that3

Ip(X | Y ) Ip(X) (20)

and equality holds if and only if X and Y are independent, cf. Lemma 8(ii); moreover, if Y also takes values in {0,1}ℓ for some integer ℓ, then

Ip(X,Y ) = Ip(X | Y ) + Ip(Y ) Ip(X) + Ip(Y ), (21)

where, again, equality holds if and only if X and Y are independent, cf. the chain rule for entropies (identity (9)). Generalising this further, if Z is another random variable (deﬁned on the same probability space as X and Y ), then invoking the above inequality with X and Y replaced by XZ and Y Z and taking the expectation of both sides yields

Ip(X,Y | Z) Ip(X | Z) + Ip(Y | Z), (22) cf. Lemma 8(iv). One ﬁnal property that we shall require is the following fact. Proposition 14. Suppose that random variables X, Y , and Z have a joint distribution and that X takes values in {0,1}k for some integer k 1. Then, for every p ∈ (0,1),

Ip(X | Y,Z) = E Ip(XY | ZY )

Proof. The assertion follows from the deﬁnition of conditional p-divergence and the fact that L X(Y,Z) = L (XY )ZY almost surely.

![image 100](<2021-kozma-lower-tails-relative-entropy_images/imageFile100.png>)

3In order to see this, observe ﬁrst that Ip(X | Y ) = DKL (X, Y ) Ber(p)k × Y .

- 4.2. Interlude. As an illustration of the subadditivity property of the divergence Ip, we will give a short proof of optimal tail estimates for the binomial distribution (see [14] for generalisations). Theorem 15. For every positive integer n, every p ∈ (0,1), and all q ∈ [0,p],


P Bin(n,p) nq exp − n · ip(q) = exp −n · DKL Ber(q) Ber(p) .

Proof. Let Y = (Y1,... ,Yn) be a sequence of i.i.d. Ber(p) random variables, let A denote the event that Y1 + ··· + Yn nq, and let Y ′ = (Y1′,... ,Yn′) be Y conditioned on A . By Proposition 12,

(21) n

−log P Bin(n,p) nq = −log P(A ) = DKL(Y ′ Y ) = Ip(Y ′)

Ip(Yk′).

k=1

By symmetry, for every k ∈ n ,

E[Yk′] =

n

1 n

E[Yj′] q.

![image 101](<2021-kozma-lower-tails-relative-entropy_images/imageFile101.png>)

j=1

In particular, since ip is decreasing on [0,p] and q p, we have

Ip(Yk′) = ip E[Yk′] ip(q), which concludes the proof of the theorem.

- 4.3. The key lemma. The following is our key lemma. Its role in the proof of Theorem 5 will be analogous to the role that Pinsker’s inequality (Lemma 9) played in the proof of Theorem 1.


Lemma 16. Let Y be a {0,1}-valued random variable and let E1,... ,Em be a sequence of Zmeasurable events, for some random variable Z. Suppose that E[Y | Z] p′ for some p′ > 0. Then, letting µ = E[Y ] = P(Y = 1),

Ip(Y | Z) − Ip(Y )

m

1 2p′

![image 102](<2021-kozma-lower-tails-relative-entropy_images/imageFile102.png>)

i=1

p′ 2 1 i<j m

P(Y = 1 | Ei) − µ 2P(Ei) −

P(Ei ∩ Ej). (23)

![image 103](<2021-kozma-lower-tails-relative-entropy_images/imageFile103.png>)

Let us ﬁrst show that Lemma 16 generalises Pinsker’s inequality (Lemma 9) for {0,1}-valued random variables. More precisely, let Y ∈ {0,1} and Z be two random variables and let Y × Z be the random variable whose independent coordinates have marginals Y and Z. Let E1 be the Z-measurable event P(Y = 1 | Z) P(Y = 1) and let E2 be the complementary event. As P(Y = 1 | Z) − P(Y = 1) is nonpositive on E1 (respectively, nonnegative on E2), we have

2

(−1)i · P(Y = 1 | Ei) − P(Y = 1) · P(Ei).

dTV (Y,Z),Y × Z =

i=1

In particular, the Cauchy–Schwarz Inequality gives

dTV (Y,Z),Y × Z 2

2

i=1

P(Y = 1 | Ei) − P(Y = 1) 2 · P(Ei) · P(E1) + P(E2) .

It thus follows from Lemma 16, invoked with p = 1/2 and p′ = 1, that

dTV (Y,Z),Y × Z 2 2 · I1/2(Y | Z) − I1/2(Y ) (19=) 2 · H(Y ) − H(Y | Z) ; (24)

this is precisely Pinsker’s inequality (Lemma 9). In the proof of Theorem 5, we will use Lemma 16 with p′ = p, which will result in a much stronger bound.

Proof of Lemma 16. Observe ﬁrst that the case µ = 0 is trivial. Indeed, by (20), the left-hand side of (23) is always nonnegative and, when µ = 0, each term in the ﬁrst sum in the right-hand side of (23) vanishes, as Y = 0 almost surely. We will thus assume that µ > 0. For the sake of brevity, let g := E[Y | Z], so that

Ip(Y | Z) = E Ip(Y Z) = E[ip(g)],

where ip is the function deﬁned in (17). Expanding ip into a Taylor series of order two around µ with Lagrange remainder gives

(g − µ)2 2

ip(g) = ip(µ) + i′p(µ) · (g − µ) + i′′p(ξg) ·

(25)

![image 104](<2021-kozma-lower-tails-relative-entropy_images/imageFile104.png>)

for some ξg with 0 < ξg max{µ,g}. Recall from (17) and (18) that the ﬁrst term ip(µ) is Ip Ber(µ) = Ip(Y ) and that i′′p(ξ) = 1ξ + 1−1ξ. When we take expectations (over Z) of both sides of (25), the term i′p(µ) · (g − µ) disappears, as E[g] = E[Y ] = µ, and thus we end up with

![image 105](<2021-kozma-lower-tails-relative-entropy_images/imageFile105.png>)

![image 106](<2021-kozma-lower-tails-relative-entropy_images/imageFile106.png>)

(g − µ)2 2

1 1 − ξg ·

1 ξg

Ip(Y | Z) − Ip(Y ) = E

+

.

![image 107](<2021-kozma-lower-tails-relative-entropy_images/imageFile107.png>)

![image 108](<2021-kozma-lower-tails-relative-entropy_images/imageFile108.png>)

![image 109](<2021-kozma-lower-tails-relative-entropy_images/imageFile109.png>)

Since µ,g p′, we have

1 µ

1 g

1 1 − ξg

1 ξg

1 p′

1 ξg

,

+

min

![image 110](<2021-kozma-lower-tails-relative-entropy_images/imageFile110.png>)

![image 111](<2021-kozma-lower-tails-relative-entropy_images/imageFile111.png>)

![image 112](<2021-kozma-lower-tails-relative-entropy_images/imageFile112.png>)

![image 113](<2021-kozma-lower-tails-relative-entropy_images/imageFile113.png>)

![image 114](<2021-kozma-lower-tails-relative-entropy_images/imageFile114.png>)

![image 115](<2021-kozma-lower-tails-relative-entropy_images/imageFile115.png>)

and we conclude that Ip(Y | Z) − Ip(Y )

- 1

![image 116](<2021-kozma-lower-tails-relative-entropy_images/imageFile116.png>)

- 2p′ · E (g − µ)2


- 1

![image 117](<2021-kozma-lower-tails-relative-entropy_images/imageFile117.png>)

- 2p′ E1∪···∪Em


(g − µ)2 dP. (26)

It follows from Bonferroni’s inequality (inclusion-exclusion) that

(g − µ)2 dP

E1∪···∪Em

m

(g − µ)2 dP.

(g − µ)2 dP −

1 i<j m Ei∩Ej

i=1 Ei

Since 0 g,µ p′, then (g − µ)2 (p′)2. Applying the Cauchy–Schwarz Inequality to each of the terms of the ﬁrst sum above, we obtain

(g − µ)2 dP

E1∪···∪Em

=

m

i=1

m

i=1

1 P(Ei) Ei

g dP − µ

![image 118](<2021-kozma-lower-tails-relative-entropy_images/imageFile118.png>)

2

(p′)2 dP

P(Ei) −

1 i<j m Ei∩Ej

P(Y = 1 | Ei) − µ 2P(Ei) − (p′)2

P(Ei ∩ Ej),

1 i<j m

which, substituted into (26), yields the desired inequality (23).

5. Upper bounds for the lower tail

In this section, we prove Theorem 5. Recall that we are given a hypergraph H on a set V and that R denotes a random subset of V where every element is included independently with probability p.

- 5.1. First reductions. Let Y = (Yv)v∈V be the indicator of R conditioned on the lower tail event e(H [R]) ηpre(H ). Proposition 11 and the deﬁnition of Ip give


−log P e(H [R]) ηpre(H ) = Ip(Y ), so from now on Ip(Y ) will be our main focus. It will be convenient to deﬁne, for every W ⊆ V ,

H(W) :=

Ip Yv | (Yw)w∈W .

v∈V \W

The point of making this deﬁnition is that Ip Y (21=) Ip (Yv)v∈V \W | (Yw)w∈W + Ip (Yw)w∈W

(27)

(22)

(16)

Ip (Yv)v∈V \W | (Yw)w∈W

Ip Yv | (Yw)w∈W = H(W),

v∈V \W

and thus our goal becomes to ﬁnd a set W such that H(W) (1 − ε)ΦX(η + ε) − C.

We will relate H(W) to the quantity Φ(η + ε) in the following way. First, deﬁne the function f : [0,1]V → R by letting, for each q ∈ [0,1]V ,

f(q) :=

qv.

dA

v∈A

A∈H

In other words, f(q) is the expected number of edges of H induced by a random subset of V obtained by retaining each v ∈ V independently with probability qv. Note that f(Y ) = e(H [R]) and that

ip(qv) : q ∈ [0,1]V ,f(q) (η + ε)pre(H ) .

Φ(η + ε) = min

v∈V

Second, given a W ⊆ V , we deﬁne a random function qW : V → [0,1] by letting, for each v ∈ V ,

E[Yv | (Yw)w∈W] if v ∈/ W, p otherwise.

qvW :=

Finally, we write

(†)

H(W) (=∗)

ip(qvW)

P f(qW) (η + ε)pre(H ) · Φ(η + ε),

E[ip(qvW)] = E

v∈V

v∈V \W

where (∗) follows from the deﬁnitions of H, ip, and qW; and where (†) uses ip 0 and bounds the expectation from below by the probability of the event f(qW) (η + ε)pre(H ) times the

minimum of the sum v∈V ip(qvW) on that event. In particular, it suﬃces to produce a set W such that

P f(qW) (η + ε)pre(H ) 1 − ε. (28)

Conditioning on Yw w∈W for various W ⊆ V will repeat so much that it is better to have a shorthand for it. Deﬁne therefore

EW[·] := E[· | (Yw)w∈W] (29) (so that our qW can now be written as qvW = EW[Yv] for v ∈/ W). For similar reasons, given an

- A ⊆ V , deﬁne


YA :=

Ya.

a∈A

Since f(Y ) = e(H [R]) ηpre(H ) almost surely (and, consequently, EW[f(Y )] ηpre(H ) for every W ⊆ V ), we may obtain lower bounds on the probability in the left-hand side of (28) by bounding from above the right-hand side of the following inequality:

f(qW) − EW[f(Y )]

EW(Ya) − EW [YA] .

dA ·

a∈A

A∈H

In order to do so, we will quantify the diﬀerence between v∈A EW[Yv] and EW[ v∈A Yv] for a typical A ∈ H . This is related to conditioned almost independence of the variables {Yv}v∈A. However, we are not studying full independence, but only with respect to the event that all Yv are 1. To continue our analysis, we need a few preliminaries, which will be the topic of the next section.

- 5.2. Preliminaries. At various places we will need the following corollary of Harris’s inequality:


- Claim 17. EW[YA] p|A| for all W ⊆ V and all A ⊆ V \ W.

Proof. Fix some possible value y ∈ {0,1}W for (Yw)w∈W. Writing E for the event A ⊆ R and recalling that Y is the indicator of R conditioned on the lower tail event e(H [R]) ηpre(H ),

E YA | (Yw)w∈W = y =

P YA = 1,(Yw)w∈W = y P (Yw)w∈W = y

![image 119](<2021-kozma-lower-tails-relative-entropy_images/imageFile119.png>)

=

P E,(Rw)w∈W = y,e(H [R]) ηpre(H ) P (Rw)w∈W = y,e(H [R]) ηpre(H )

![image 120](<2021-kozma-lower-tails-relative-entropy_images/imageFile120.png>)

=

P E,e(H [R]) ηpre(H ) (Rw)w∈W = y P e(H [R]) ηpre(H ) | (Rw)w∈W = y

![image 121](<2021-kozma-lower-tails-relative-entropy_images/imageFile121.png>)

Since the elements of V are included in R independently, conditioning on (Rw)w∈W gives a product measure on (Rv)v∈V \W. Moreover, under the conditioned measure, the event E is increasing and the lower tail event e(H [R]) ηpre(H ) is decreasing. The claim follows from Harris’s inequality.

- Claim 18. For every nonempty, ﬁnite set A and every function F : P(A) → R,


1

F({a}).

· F(B) − F(B \ {b})F({b})

F({a}) =

F(A) −

![image 122](<2021-kozma-lower-tails-relative-entropy_images/imageFile122.png>)

- |A|
- |B| |B|


b∈B

B⊆A |B| 2

a∈A

a∈A\B

(As usual, P(A) denotes the power set of A.) Proof. The identity holds trivially when |A| = 1 and we may thus assume that |A| 2. Observe ﬁrst that the right-hand side is a linear combination of terms of the form

K∅ :=

F({a}) and KB := F(B) ·

F({a}),

a∈A

a∈A\B

where B ⊆ A satisﬁes |B| 2. The term K∅ appears only when |B| = 2 in the outer sum and it is easy to verify that its coeﬃcient is

|A| 2 · 2 ·

- 1

![image 123](<2021-kozma-lower-tails-relative-entropy_images/imageFile123.png>)

|A|

- 2 · 2


−

= −1.

Fix an arbitrary B ⊆ A with |B| 2. On the one hand, the term KB appears with a positive sign exactly |B| times (once for each b ∈ B) and the respective coeﬃcient is

1

;

![image 124](<2021-kozma-lower-tails-relative-entropy_images/imageFile124.png>)

- |A|
- |B| |B|


on the other hand, it appears with a negative sign (B is then in fact B \ {b}) exactly |A| − |B| times (once for each b ∈ A \ B) and the respective coeﬃcient is (note that |B| |A| − 1 in this case)

−1

![image 125](<2021-kozma-lower-tails-relative-entropy_images/imageFile125.png>)

- |A|
- |B|+1 (|B| + 1)


In particular, when B = A, then the positive and the negative contributions cancel, as |B| ·

1

1

1

= (|A| − |B|) ·

=

,

![image 126](<2021-kozma-lower-tails-relative-entropy_images/imageFile126.png>)

![image 127](<2021-kozma-lower-tails-relative-entropy_images/imageFile127.png>)

![image 128](<2021-kozma-lower-tails-relative-entropy_images/imageFile128.png>)

- |A|
- |B| |B|


- |A|
- |B|


- |A|
- |B|+1 (|B| + 1)


and it is easy to check that the sum of the coeﬃcients of KA is 1.

- 5.3. The argument. Fix an arbitrary nonempty A ⊆ V \W. Applying Claim 18 with F(B) = EW[YB] yields


EW[YA] −

EW[Ya] =

a∈A

B⊆A |B| 2

b∈B

1

· (EW[YB] − EW[YB\{b}]EW[Yb]

) ·

![image 129](<2021-kozma-lower-tails-relative-entropy_images/imageFile129.png>)

- |A|
- |B| |B|


![image 130](<2021-kozma-lower-tails-relative-entropy_images/imageFile130.png>)

![image 131](<2021-kozma-lower-tails-relative-entropy_images/imageFile131.png>)

DW (B,b)

EW[Ya]

a∈A\B

(this is the deﬁnition of DW). Consequently, by the triangle inequality,

EW[YA] −

EW[Ya]

a∈A

1

EW[Ya]

· |DW(B,b)| ·

![image 132](<2021-kozma-lower-tails-relative-entropy_images/imageFile132.png>)

- |A|
- |B| |B|


B⊆A |B| 2

b∈B

a∈A\B

(∗)

1

· |DW(B,b)| · p|A|−|B|,

![image 133](<2021-kozma-lower-tails-relative-entropy_images/imageFile133.png>)

- |A|
- |B| |B|


B⊆A |B| 2

b∈B

where (*) follows from Claim 17. We sum this inequality over all A ∈ H − W = H [V \ W], take expectation over Yv v∈W, and get (recall that our hypergraph is r-uniform, so |A| = r for every A ∈ H )

E

dA · EW[YA] −

A∈H −W

EW[Ya]

a∈A

E

A∈H −W B⊆A |B| 2

b∈B

dA r

· |DW(B,b)| · pr−|B| . (30)

![image 134](<2021-kozma-lower-tails-relative-entropy_images/imageFile134.png>)

|B| |B|

We now wish to apply the Cauchy–Schwarz Inequality to the right-hand side of (30). However, since the resulting expression would be too long, we ﬁrst deﬁne

E (W) := E

and then Cauchy–Schwarz yields

A∈H −W B⊆A |B| 2

b∈B

dA · DW(B,b)2

|B| |B| · p2|B| , (31)

![image 135](<2021-kozma-lower-tails-relative-entropy_images/imageFile135.png>)

r

E

dA · EW[YA] −

a∈A

A∈H −W

dAp2r

![image 136](<2021-kozma-lower-tails-relative-entropy_images/imageFile136.png>)

r

|B| |B|

A∈H −W B⊆A |B| 2

b∈B

EW[Ya]

1/2

· E (W)1/2 = pr (r − 1)e(H − W) 1/2 · E (W)1/2, (32)

where we used the identity B,b 1 (|Br|)|B| = r − 1, which holds because enumerating over all

![image 137](<2021-kozma-lower-tails-relative-entropy_images/imageFile137.png>)

- B ⊆ A of a given size and all b ∈ B cancels the denominator perfectly. Let us remark that most readers might be better oﬀ ignoring all these combinatorial factors. We chose to estimate them carefully in order to optimise the dependency of λ and C (from the statement of the theorem) on r. However, in most applications r will be an absolute constant.


The essence of our argument is establishing the following dichotomy: Either

- (i) E[EW] is quite small, or
- (ii) H(W ∪ W′) H(W) + Ω p|V | for some small W′ ⊆ V \ W.


If (i) holds, then, by (32), we will have that EW[YA] − a∈A EW[Ya] is small (on average), and a few simple manipulations (done at the end of the proof of Theorem 5, page 24) will show that

our candidate set W satisﬁes (28). Otherwise, (ii) holds and we replace W with W ∪ W′; this can happen only O(1) times since

(27)

Ip(Y ) = −log P e(H [R]) ηpre(H ) −log P(R = ∅) = |V | · log

H(W)

(33)

1 1 − p |V | ·

p 1 − p |V | ·

p 1 − p0

.

![image 138](<2021-kozma-lower-tails-relative-entropy_images/imageFile138.png>)

![image 139](<2021-kozma-lower-tails-relative-entropy_images/imageFile139.png>)

![image 140](<2021-kozma-lower-tails-relative-entropy_images/imageFile140.png>)

Lemma 19. For all positive α, β, and K, there exist λ and V0 such that the following holds: If |V | V0 and H satisﬁes (7) for every s ∈ r , then there exists a set W ⊆ V with at most α|V | elements that satisﬁes

E (W) β · e(H ).

Proof. Without loss of generality, we may assume that α < 1/2, β < 1, and K > 1. We ﬁrst deﬁne a few constants:

β2 300Kr

τ 2r

, and V0 := 8r2/τ. (34)

γ :=

, τ := αγ(1 − p0), λ :=

![image 141](<2021-kozma-lower-tails-relative-entropy_images/imageFile141.png>)

![image 142](<2021-kozma-lower-tails-relative-entropy_images/imageFile142.png>)

- A short calculation shows that the deﬁnition of V0 guarantees that


τ · V0/2 − r V0/2 − r

V0/2 V0/2 − 1

τ 21/r

21/(2r). (35)

and

![image 143](<2021-kozma-lower-tails-relative-entropy_images/imageFile143.png>)

![image 144](<2021-kozma-lower-tails-relative-entropy_images/imageFile144.png>)

![image 145](<2021-kozma-lower-tails-relative-entropy_images/imageFile145.png>)

As explained above, we shall build our set W in several rounds, starting with W being the empty set. In each round, we will use the following claim, which implements the dichotomy mentioned above.

Claim 20. Suppose that W ⊆ V satisﬁes E (W) > β · e(H ) and |V \ W| V0/2. Then there exists a set W′ ⊆ V \ W with at most τ|V | elements such that

H(W ∪ W′) H(W) + γp|V |. (36)

Proof of Claim 20. Let W′ be a uniformly chosen subset of V \ W with density τ, that is, with exactly ⌊τ · |V \ W|⌋ elements. We will show that, under the assumption that E (W) > βe(H ) and |V \ W| V0/2, we have

E H(W ∪ W′) (1 − τ) · H(W) + 2γp|V |. (37) Consequently, since

(33) τ

1 − p0 · p|V | (34=) αγp|V | < γp|V |, (38) the desired inequality (36) must hold for some W′.

τ · H(W)

![image 146](<2021-kozma-lower-tails-relative-entropy_images/imageFile146.png>)

We now write H(W ∪ W′) − H(W) =

Ip(Yv |(Yw)w∈W∪W′) −

Ip(Yv |(Yw)w∈W)

v∈V \(W∪W′)

v∈V \W

. (39)

Ip(Yv |(Yw)w∈W∪W′) − Ip(Yv |(Yw)w∈W)

−

Ip(Yv |(Yw)w∈W)

=

v∈W′

v∈V \(W∪W′)

![image 147](<2021-kozma-lower-tails-relative-entropy_images/imageFile147.png>)

![image 148](<2021-kozma-lower-tails-relative-entropy_images/imageFile148.png>)

![image 149](<2021-kozma-lower-tails-relative-entropy_images/imageFile149.png>)

![image 150](<2021-kozma-lower-tails-relative-entropy_images/imageFile150.png>)

II

I

By linearity of expectation, E[II] = ⌊τ · |V \ W|⌋ |V \ W|

· H(W) τ · H(W), and thus (37) will follow if we show that

![image 151](<2021-kozma-lower-tails-relative-entropy_images/imageFile151.png>)

J := E[I] 2γp|V |. (40)

In order to bound J from below, we will apply our main lemma (Lemma 16), conditionally on Yw : w ∈ W , with Z = Yw : w ∈ W′ and a careful choice of the sequence of Z-measurable events that we shall now deﬁne. To this end, for each v ∈ V \ W, let

H (v) := B ⊆ V \ W : |B| 2, v ∈ B, and B ⊆ A for some A ∈ H − W and let G (v) be the random subset of H (v) formed by including each B ∈ H (v) satisfying

- B \ {v} ⊆ W′ with probability σB, which we will specify later, independently for each such B.


Let S := Yw w∈W and, for every v ∈ V \ (W ∪ W′), let YvS denote Yv conditioned on S, that is, the random variable whose (random) distribution is the distribution of Yv conditioned on S. Deﬁne

JS(v) := Ip YvS | YwS w∈W′ − Ip YvS , The next step is to apply Lemma 16. Recall that we need to supply the lemma with a sequence of events. The number of events in our application will also be random, but it will depend only on W′ and G (v), so let us ﬁx their choice for the time being. For each B ∈ G (v), let EBS be the event that YBS\{v} = 1; note that EBS is (YwS)w∈W′-measurable, as B \ {v} ⊆ W′. Since E YvS | (YwS)w∈W′ = EW∪W′[Yv] p, by Claim 17, we may apply Lemma 16 with Y = YvS, Z = (YwS : w ∈ W′), the events EBS, and p′ = p to get (recall the deﬁnition of DW given at the start of § 5.3)

- 1

![image 152](<2021-kozma-lower-tails-relative-entropy_images/imageFile152.png>)

- 2p B∈G (v)


p 2

P(YvS = 1 | EBS) − E[YvS] 2P(EBS) −

JS(v)

P(EBS ∩ EBS′)

![image 153](<2021-kozma-lower-tails-relative-entropy_images/imageFile153.png>)

B,B′∈G (v) B =B′

DW(B,v)2 EW[YB\{v}] −

- 1

![image 154](<2021-kozma-lower-tails-relative-entropy_images/imageFile154.png>)

- 2p B∈G (v)


p 2

EW[YB\{v} · YB′\{v}].

=

![image 155](<2021-kozma-lower-tails-relative-entropy_images/imageFile155.png>)

![image 156](<2021-kozma-lower-tails-relative-entropy_images/imageFile156.png>)

B,B′∈G (v) B =B′

Since every edge of G (v) contains v and is disjoint from W, Claim 17 implies that EW[YB\{v}] p|B|−1 and EW[YB\{v} · YB′\{v}] p|B∪B′|−1 for all B,B′ ∈ G (v). This observation allows us to simplify our lower bound for JS(v) to

2 · JS(v)

DW(B,v)2 p|B| −

p|B∪B′| =: G(v) − L(v), (41)

![image 157](<2021-kozma-lower-tails-relative-entropy_images/imageFile157.png>)

B,B′∈G (v) B =B′

B∈G (v)

i.e., G(v) is the ﬁrst sum and L(v) is the second.

We now return to the J from (40). It is the expectation (over W′) of the sum I deﬁned in (39), each of whose summands is the expectation (over S) of JS(v), see Proposition 14. We wish to exchange the sum and expectation, but since the sum is over v  ∈ W′ (recall (39)) and this is an event, we need to condition on it. Hence we arrive at

J (40=)

P(v ∈/ W′) · E E JS(v) | v ∈/ W′

v∈V \W

(42)

E G(v) − L(v) | v ∈/ W′ 

(41) 1 − τ 2 · E   v∈V \W

,

![image 158](<2021-kozma-lower-tails-relative-entropy_images/imageFile158.png>)

where E and P denote the expectation and the probability over the random choice of the set W′ and the hypergraphs G (v) and over S. In the remainder of the proof, we shall estimate the right-hand side of (42).

We start with the estimate of the G terms. We deﬁne G′(v) := E G(v) | v ∈/ W′ =

DW(B,v)2 p|B|

P B ∈ G (v) | v ∈/ W′ ·

.

![image 159](<2021-kozma-lower-tails-relative-entropy_images/imageFile159.png>)

B∈H (v)

For every B ∈ H (v), we have (recall the assumption that |V \ W| V0/2) P B ∈ G (v) | v ∈/ W′ = P B \ {v} ⊆ W′ | v ∈/ W′ · σB

|B|−2

⌊τ|V \ W|⌋ − i |V \ W| − i − 1 · σB

=

![image 160](<2021-kozma-lower-tails-relative-entropy_images/imageFile160.png>)

i=0

|B|−1

(35) τ|B|−1

τ|V \ W| − r |V \ W| − r

2 · σB. We conclude that

· σB

![image 161](<2021-kozma-lower-tails-relative-entropy_images/imageFile161.png>)

![image 162](<2021-kozma-lower-tails-relative-entropy_images/imageFile162.png>)

τ|B| · σB · DW(B,v)2

1 2τ

G′(v)

p|B| . (43) Summing (43) over all v ∈ V \ W yields (recall the deﬁnition of degH −W given in (5))

![image 163](<2021-kozma-lower-tails-relative-entropy_images/imageFile163.png>)

![image 164](<2021-kozma-lower-tails-relative-entropy_images/imageFile164.png>)

B∈H (v)

τ|B| · σB · DW(B,v)2 p|B|

dA degH −W B ·

- 1

![image 165](<2021-kozma-lower-tails-relative-entropy_images/imageFile165.png>)

- 2τ A∈H −W B⊆A |B| 2


G′(v)

, (44)

![image 166](<2021-kozma-lower-tails-relative-entropy_images/imageFile166.png>)

![image 167](<2021-kozma-lower-tails-relative-entropy_images/imageFile167.png>)

v∈B

v∈V \W

cf. the deﬁnition of E (W) given in (31). This is a good moment to ﬁnally deﬁne the probabilities σB. We let

degH −W B r

σB := µ ·

|B| |B|(τp)|B|, (45) where

![image 168](<2021-kozma-lower-tails-relative-entropy_images/imageFile168.png>)

βτp|V | 16K(r − 1)e(H )

µ :=

. (46) Note that σB 1 as

![image 169](<2021-kozma-lower-tails-relative-entropy_images/imageFile169.png>)

(46) (τp)|B| µ

(34)

(7)

e(H ) |V |

e(H ) |V |

K · (λp)|B|−1 ·

K · (τp)|B|−1 ·

. Substituting (45) into (44) yields precisely

degH −W B ∆|B|(H )

![image 170](<2021-kozma-lower-tails-relative-entropy_images/imageFile170.png>)

![image 171](<2021-kozma-lower-tails-relative-entropy_images/imageFile171.png>)

![image 172](<2021-kozma-lower-tails-relative-entropy_images/imageFile172.png>)

dA · E[DW(B,v)2]

µ 2τ · E (W). (47)

µ

(31=)

G′(v)

E

![image 173](<2021-kozma-lower-tails-relative-entropy_images/imageFile173.png>)

![image 174](<2021-kozma-lower-tails-relative-entropy_images/imageFile174.png>)

![image 175](<2021-kozma-lower-tails-relative-entropy_images/imageFile175.png>)

r

|B| |B|p2|B|

2τ A∈H −W B⊆A |B| 2

v∈B

v∈V \W

This concludes our estimate of the G terms. The estimate of the L terms in (42) is similar, but somewhat more involved. We deﬁne

P B,B′ ∈ G (v) | v ∈/ W′ · p|B∪B′|.

L′(v) := E L(v) | v ∈/ W′ =

B,B′∈H (v) B =B′

Thus, we need a second moment estimate for the sum of indicators of B ∈ G (v) over all B ∈ H (v). Note ﬁrst that, for each B = B′,

P B,B′ ∈ G (v) | v ∈/ W′ = P (B ∪ B′) \ {v} ⊆ W′ | v ∈/ W′ · σBσB′

|B∪B′|−2

⌊τ|V \ W|⌋ − i |V \ W| − i − 1 · σBσB′

=

![image 176](<2021-kozma-lower-tails-relative-entropy_images/imageFile176.png>)

i=0

|B∪B′|−1

(35)

τ|V \ W| |V \ W| − 1

2τ|B∪B′|−1 · σBσB′. Hence

· σBσB′

![image 177](<2021-kozma-lower-tails-relative-entropy_images/imageFile177.png>)

2 τ

(τp)|B∪B′| · σBσB′. (48)

L′(v)

![image 178](<2021-kozma-lower-tails-relative-entropy_images/imageFile178.png>)

B,B′∈H (v) B =B′

Summing (48) over all v ∈ V \ W gives

dA degH −W B ·

dA′ degH −W B′ · (τp)|B∪B′| · σBσB′

2 τ A,A′∈H −W

L′(v)

![image 179](<2021-kozma-lower-tails-relative-entropy_images/imageFile179.png>)

![image 180](<2021-kozma-lower-tails-relative-entropy_images/imageFile180.png>)

![image 181](<2021-kozma-lower-tails-relative-entropy_images/imageFile181.png>)

v∈B∩B′

B⊆A,B′⊆A′ |B|,|B′| 2 B =B′

v∈V \W

|B ∩ B′| · dAdA′ r

2µ2 τ2p ·

(45=)

,

![image 182](<2021-kozma-lower-tails-relative-entropy_images/imageFile182.png>)

![image 183](<2021-kozma-lower-tails-relative-entropy_images/imageFile183.png>)

|B| |B| |B r′| |B′|(τp)|B∩B′|−1

A,A′∈H −W B⊆A,B′⊆A′

|B|,|B′| 2 B =B′

![image 184](<2021-kozma-lower-tails-relative-entropy_images/imageFile184.png>)

![image 185](<2021-kozma-lower-tails-relative-entropy_images/imageFile185.png>)

(∗)

where we used the identity |B ∪ B′| + |B ∩ B′| = |B| + |B′|. Rearranging gives

- r−1
- s=1


s

1

1

(∗) =

dA

.

dA′

![image 186](<2021-kozma-lower-tails-relative-entropy_images/imageFile186.png>)

![image 187](<2021-kozma-lower-tails-relative-entropy_images/imageFile187.png>)

![image 188](<2021-kozma-lower-tails-relative-entropy_images/imageFile188.png>)

r

r

(τp)s−1 C⊆B |C|=s

|B′| |B′|

|B| |B|

B′⊆A′ |B|′ 2 B∩B′=C

A′∈H −W C⊆A′

B⊆A |B| 2

A∈H −W

![image 189](<2021-kozma-lower-tails-relative-entropy_images/imageFile189.png>)

![image 190](<2021-kozma-lower-tails-relative-entropy_images/imageFile190.png>)

SB,s

Now, for every A′ ∈ H − W, every s 1, and every C ⊆ A′ with |C| = s,

b′−1 s−1

b′ s

r−s b′−s

r

r

r

1 s

1

1.

=

=

=

=

![image 191](<2021-kozma-lower-tails-relative-entropy_images/imageFile191.png>)

![image 192](<2021-kozma-lower-tails-relative-entropy_images/imageFile192.png>)

![image 193](<2021-kozma-lower-tails-relative-entropy_images/imageFile193.png>)

![image 194](<2021-kozma-lower-tails-relative-entropy_images/imageFile194.png>)

![image 195](<2021-kozma-lower-tails-relative-entropy_images/imageFile195.png>)

r

r b′ b′

- r
- s b′


- r
- s s


|B′| |B′|

b′=s

b′=s

b′=s

C⊆B′⊆A′

Hence, for every B with at most r elements and every s 1, SB,s

|B| s · ∆s(H ) = |B| s

|B| − 1 s − 1 · ∆s(H )

dA′

![image 196](<2021-kozma-lower-tails-relative-entropy_images/imageFile196.png>)

A′∈H −W C⊆A′

C⊆B |C|=s

(7) |B| s

|B| s · (rλp)s−1 · K ·

|B| − 1 s − 1 · (λp)s−1 · K ·

e(H ) |V |

e(H ) |V |

. Consequently,

![image 197](<2021-kozma-lower-tails-relative-entropy_images/imageFile197.png>)

![image 198](<2021-kozma-lower-tails-relative-entropy_images/imageFile198.png>)

![image 199](<2021-kozma-lower-tails-relative-entropy_images/imageFile199.png>)

![image 200](<2021-kozma-lower-tails-relative-entropy_images/imageFile200.png>)

- r−1
- s=1


1

(∗)

dA

![image 201](<2021-kozma-lower-tails-relative-entropy_images/imageFile201.png>)

r |B|

B⊆A |B| 2

A∈H −W

- r−1
- s=1


= e(H − W) · (r − 1) ·

Since rλ = τ/2, we conclude that

rλ τ

![image 202](<2021-kozma-lower-tails-relative-entropy_images/imageFile202.png>)

s−1

e(H ) |V |

· K ·

![image 203](<2021-kozma-lower-tails-relative-entropy_images/imageFile203.png>)

rλ τ

![image 204](<2021-kozma-lower-tails-relative-entropy_images/imageFile204.png>)

s−1

e(H ) |V |

· K ·

.

![image 205](<2021-kozma-lower-tails-relative-entropy_images/imageFile205.png>)

2µ2 τ2p · (r − 1) · 2K ·

e(H )2 |V |

µ τ ·

βe(H ) 4

(46=)

L′(v)

. (49)

![image 206](<2021-kozma-lower-tails-relative-entropy_images/imageFile206.png>)

![image 207](<2021-kozma-lower-tails-relative-entropy_images/imageFile207.png>)

![image 208](<2021-kozma-lower-tails-relative-entropy_images/imageFile208.png>)

![image 209](<2021-kozma-lower-tails-relative-entropy_images/imageFile209.png>)

v∈V \W

Combining this with the estimate (47) gives

G′(v) − L′(v)

(42) 1 − τ 2 · E   v∈V \W

 (47,49) (1 − τ) 2 ·

E (W) 2 −

µ τ ·

βe(H ) 4

J

![image 210](<2021-kozma-lower-tails-relative-entropy_images/imageFile210.png>)

![image 211](<2021-kozma-lower-tails-relative-entropy_images/imageFile211.png>)

![image 212](<2021-kozma-lower-tails-relative-entropy_images/imageFile212.png>)

![image 213](<2021-kozma-lower-tails-relative-entropy_images/imageFile213.png>)

![image 214](<2021-kozma-lower-tails-relative-entropy_images/imageFile214.png>)

(1 − τ)β2 128K(r − 1) · p|V |

(34)

(1 − τ) 2 ·

µ τ ·

βe(H ) 4

(∗)

(=46)

2γp|V |, where (∗) follows from our assumption that E (W) > βe(H ). The claim is thus proved.

>

![image 215](<2021-kozma-lower-tails-relative-entropy_images/imageFile215.png>)

![image 216](<2021-kozma-lower-tails-relative-entropy_images/imageFile216.png>)

![image 217](<2021-kozma-lower-tails-relative-entropy_images/imageFile217.png>)

![image 218](<2021-kozma-lower-tails-relative-entropy_images/imageFile218.png>)

Proof of Lemma 19, continued. Suppose that the assertion of the lemma is not true, that is, E (W) > β · e(H ) for every W ⊆ V with at most α|V | elements. We will construct a sequence W0,... ,Wj of subsets of V , where j = ⌊α/τ⌋ + 1, such that, for each i ∈ {0,... ,j},

- (i) |Wi| i · τ|V | and
- (ii) H(Wi) i · γp|V |.


If such a sequence existed, we would have

p 1 − p0

H(Wj) j · γp|V | > (α/τ) · γp|V | (=34) |V | ·

, which contradicts (33).

![image 219](<2021-kozma-lower-tails-relative-entropy_images/imageFile219.png>)

We start by letting W0 = ∅. Suppose that 0 i j −1 and that Wi has already been deﬁned so that (i) and (ii) hold. Since

|Wi| i · τ|V | ⌊α/τ⌋ · τ|V | α|V |,

we have E (Wi) > β · e(H ) by the contradictory assumption. We note also that |V \ Wi| (1 − α)|V | |V |/2 V0/2. In particular, Claim 20, invoked with W = Wi, supplies a W′ ⊆ V \ Wi with at most τ|V | elements that satisﬁes (36). We let Wi+1 = Wi ∪ W′ and note that

(i)

|Wi+1| = |Wi| + |W′|

i · τ|V | + τ|V | = (i + 1) · τ|V | and

(36)

(ii)

H(Wi+1) = H(Wi ∪ W′)

(i + 1) · γp|V |, so (i) and (ii) continue to hold with i replaced by i+1. This completes the proof of the existence of the sequence of W0,... ,Wj, which yields the desired contradiction.

H(Wi) + γp|V |

Proof of Theorem 5. Let λ and V0 be constants supplied by Lemma 19 invoked with α :=

ε4 4r

ε 2K

and β :=

.

![image 220](<2021-kozma-lower-tails-relative-entropy_images/imageFile220.png>)

![image 221](<2021-kozma-lower-tails-relative-entropy_images/imageFile221.png>)

(We note here that λ 2−15K−2r−4ε9(1−p0) and V0 = 4r/λ.) We ﬁrst handle the uninteresting case |V | < V0. Considering, in the deﬁnition of Φ(η), the function q: V → [0,1] that assigns zero to all elements of V shows that

Φ(η + ε) Φ(0) |V | · ip(0) = −|V | · log(1 − p) −V0 · log(1 − p0). In particular, setting C := −V0 · log(1 − p0) makes the assertion of the theorem hold vacuously.

We may thus assume that |V | V0, so that Lemma 19 supplies a set W ⊆ V with at most ε/(2K) · |V | elements such that E (W) ε4/(4r) · e(H ). Let qW : V → [0,1] be the random function deﬁned in the proof outline, that is, qvW := EW[Yv] for v ∈ V \ W and qvW := p for v ∈ W. We have

ε2 2 · pre(H ).

(32)

pr re(H ) 1/2 · E (W)1/2

qaW

E

dA · EW[YA] −

![image 222](<2021-kozma-lower-tails-relative-entropy_images/imageFile222.png>)

a∈A

A∈H −W

In particular, it follows from Markov’s inequality that, with probability at least 1 − ε,

ε 2 · pre(H ).

qaW

dA · EW[YA] +

dA

![image 223](<2021-kozma-lower-tails-relative-entropy_images/imageFile223.png>)

a∈A

A∈H −W

A∈H −W

However, the deﬁnition of Y implies that, deterministically,

dAYA

A∈H −W

A∈H

and thus, with probability at least 1 − ε,

dA

a∈A

A∈H −W

dAYA = e(H [R]) ηpre(H )

qaW (η + ε/2) · pre(H ).

The deﬁnition of qW and Claim 17 guarantee that qvW p for every v ∈ V and, therefore,

qaW pr · e(H ) − e(H − W) pr · |W| · ∆1(H )

dA

a∈A

A∈H \(H −W)

(7)

ε|V | 2K · K ·

e(H ) v(H )

ε 2 · pre(H ).

pr ·

=

![image 224](<2021-kozma-lower-tails-relative-entropy_images/imageFile224.png>)

![image 225](<2021-kozma-lower-tails-relative-entropy_images/imageFile225.png>)

![image 226](<2021-kozma-lower-tails-relative-entropy_images/imageFile226.png>)

Summarising, with probability at least 1 − ε, we have f(qW) =

qaW (η + ε) · pre(H ).

dA

a∈A

A∈H

Hence, we may conclude that H(W)

(28)

P f(qW) (η + ε)pre(H ) · Φ(η + ε) (1 − ε)Φ(η + ε), as needed.

6. Lower bounds for the lower tail In this section, we prove Theorem 7. We will need the following technical lemma.

- Lemma 21. For every p0 < 1, there exists a constant K such that the following holds. Suppose that 0 < p p0 and 0 q p, let Y ∼ Ber(q), and let


1 − q 1 − p

q p

X := Y log

+ (1 − Y )log

. Then,

![image 227](<2021-kozma-lower-tails-relative-entropy_images/imageFile227.png>)

![image 228](<2021-kozma-lower-tails-relative-entropy_images/imageFile228.png>)

Var(X) KE[X] = Kip(q). Proof. This is nothing but a calculus exercise, but let us do it in details anyway. Observe ﬁrst that the case q = 0 is trivial. Indeed, ip is nonnegative and Var(X) = 0 when q = 0. We will thus assume that q > 0. A direct computation shows that

2

1 − q 1 − p

q p − log

(18=) q(1 − q) i′p(q) 2 q · i′p(q) 2.

Var(X) = q(1 − q) log

![image 229](<2021-kozma-lower-tails-relative-entropy_images/imageFile229.png>)

![image 230](<2021-kozma-lower-tails-relative-entropy_images/imageFile230.png>)

Since ip(p) = i′p(p) = 0, expanding both ip(q) and i′p(q) in Taylor series around q = p with Lagrange remainder gives q1,q2 ∈ (q,p) such that

(q − p)2 2p

(q − p)2 2 ·

1 q1

1 1 − q1

+

, (50)

ip(q) =

![image 231](<2021-kozma-lower-tails-relative-entropy_images/imageFile231.png>)

![image 232](<2021-kozma-lower-tails-relative-entropy_images/imageFile232.png>)

![image 233](<2021-kozma-lower-tails-relative-entropy_images/imageFile233.png>)

![image 234](<2021-kozma-lower-tails-relative-entropy_images/imageFile234.png>)

1 q2

1 1 − q2

i′p(q) = (q − p) ·

+

.

![image 235](<2021-kozma-lower-tails-relative-entropy_images/imageFile235.png>)

![image 236](<2021-kozma-lower-tails-relative-entropy_images/imageFile236.png>)

Suppose ﬁrst that q p/2. Our assumption that p p0 implies that

1 1 − q2

1 q2

+

![image 237](<2021-kozma-lower-tails-relative-entropy_images/imageFile237.png>)

![image 238](<2021-kozma-lower-tails-relative-entropy_images/imageFile238.png>)

and, consequently,

1 q

1 1 − p

+

![image 239](<2021-kozma-lower-tails-relative-entropy_images/imageFile239.png>)

![image 240](<2021-kozma-lower-tails-relative-entropy_images/imageFile240.png>)

2 p

1 1 − p0

+

![image 241](<2021-kozma-lower-tails-relative-entropy_images/imageFile241.png>)

![image 242](<2021-kozma-lower-tails-relative-entropy_images/imageFile242.png>)

p0 1 − p0 ·

1 p

2 +

![image 243](<2021-kozma-lower-tails-relative-entropy_images/imageFile243.png>)

![image 244](<2021-kozma-lower-tails-relative-entropy_images/imageFile244.png>)

2 − p0 1 − p0 ·

1 p

=

![image 245](<2021-kozma-lower-tails-relative-entropy_images/imageFile245.png>)

![image 246](<2021-kozma-lower-tails-relative-entropy_images/imageFile246.png>)

2

2

q · (q − p)2 p2

2 − p0 1 − p0

2 − p0 1 − p0

Var(X) q · i′p(q) 2

· 2ip(q). If, on the other hand, q < p/2, then, using the inequality (a − b)2 2a2 + 2b2, we get

·

![image 247](<2021-kozma-lower-tails-relative-entropy_images/imageFile247.png>)

![image 248](<2021-kozma-lower-tails-relative-entropy_images/imageFile248.png>)

![image 249](<2021-kozma-lower-tails-relative-entropy_images/imageFile249.png>)

2 2q p

2

2

1 − q 1 − p

1 − q 1 − p

2q p

q p

q p − log

q p

Var(X) p

+

log

log

log

![image 250](<2021-kozma-lower-tails-relative-entropy_images/imageFile250.png>)

![image 251](<2021-kozma-lower-tails-relative-entropy_images/imageFile251.png>)

![image 252](<2021-kozma-lower-tails-relative-entropy_images/imageFile252.png>)

![image 253](<2021-kozma-lower-tails-relative-entropy_images/imageFile253.png>)

![image 254](<2021-kozma-lower-tails-relative-entropy_images/imageFile254.png>)

![image 255](<2021-kozma-lower-tails-relative-entropy_images/imageFile255.png>)

![image 256](<2021-kozma-lower-tails-relative-entropy_images/imageFile256.png>)

![image 257](<2021-kozma-lower-tails-relative-entropy_images/imageFile257.png>)

2

2 8 e2

1 1 − p

1 1 − p0

2x(log x)2 + log

sup

,

+ log

![image 258](<2021-kozma-lower-tails-relative-entropy_images/imageFile258.png>)

![image 259](<2021-kozma-lower-tails-relative-entropy_images/imageFile259.png>)

![image 260](<2021-kozma-lower-tails-relative-entropy_images/imageFile260.png>)

x∈(0,1/2)

whereas, since ip is decreasing in the interval [0,p],

ip(q) p

![image 261](<2021-kozma-lower-tails-relative-entropy_images/imageFile261.png>)

ip(p/2) p

![image 262](<2021-kozma-lower-tails-relative-entropy_images/imageFile262.png>)

(p/2)2 2p2

1 8

.

=

![image 263](<2021-kozma-lower-tails-relative-entropy_images/imageFile263.png>)

![image 264](<2021-kozma-lower-tails-relative-entropy_images/imageFile264.png>)

Proof of Theorem 7. We may assume without loss of generality that ε < 1. Let q: V → [0,1] be the minimiser in the deﬁnition of Φ (1−ε)η and let Y ′ = (Yv′)v∈V be a sequence of independent Bernoulli random variables with E[Yv′] = qv for each v ∈ V , so that

E[f(Y ′)] (1 − ε)ηE[f(Y )] and

ip(qv) = Φ (1 − ε)η .

v∈V

We claim that qv p for every v ∈ V . Indeed, otherwise ip(qv) > 0 = ip(p) and changing qv to p can only decrease E[f(Y ′)]. Let Y ⊆ {0,1}V be arbitrary and note that

P(Y ′ = y) P(Y = y) · P(Y = y) =

1 − qv 1 − p · P(Y = y)

qv p v:y

P Y ′ ∈ Y =

![image 265](<2021-kozma-lower-tails-relative-entropy_images/imageFile265.png>)

![image 266](<2021-kozma-lower-tails-relative-entropy_images/imageFile266.png>)

![image 267](<2021-kozma-lower-tails-relative-entropy_images/imageFile267.png>)

v=0

y∈Y v:yv=1

y∈Y

 

max  

  : y ∈ Y

exp   v:yv=1

1 − qv 1 − p

qv p

· P(Y ∈ Y ).

+

log

log

![image 268](<2021-kozma-lower-tails-relative-entropy_images/imageFile268.png>)

![image 269](<2021-kozma-lower-tails-relative-entropy_images/imageFile269.png>)



v:yv=0

In view of this, deﬁne, for each y ∈ {0,1}V , J(y) :=

1 − qv 1 − p

qv p

+

,

log

log

![image 270](<2021-kozma-lower-tails-relative-entropy_images/imageFile270.png>)

![image 271](<2021-kozma-lower-tails-relative-entropy_images/imageFile271.png>)

v:yv=0

v:yv=1

so that the above inequality may be rewritten as P(Y ′ ∈ Y ) max

exp J(y) · P(Y ∈ Y ). (51) Now, let K be the constant given by Lemma 21, let C′ := K/(2ε2), and deﬁne

y∈Y

- Y1 := y ∈ {0,1}V : f(y) ηE[f(Y )] ,
- Y2 := y ∈ {0,1}V : J(y) (1 + ε)Φ (1 − ε)η + C′ , (52)


It is immediate from these deﬁnitions that P X ηE[X] = P(Y ∈ Y1) P(Y ∈ Y1 ∩ Y2)

(51)

P(Y ′ ∈ Y1 ∩ Y2) · exp −max y∈Y2

J(y)

(52)

P(Y ′ ∈ Y1 ∩ Y2) · exp −(1 + ε)Φ (1 − ε)η − C′ .

We will show that P(Y ′ ∈ Y1 ∩ Y2) ε/2, which will yield the assertion of the theorem with C := C′ + log(2/ε).

Since f is nonnegative, Markov’s inequality gives

P f(Y ′) > ηE[f(Y )] 1 − ε and thus

P(Y ′ ∈ Y1) = P f(Y ′) ηE[f(Y )] ε; in particular, it is enough to show that P(Y ′ ∈/ Y2) ε/2. To this end, examine J(Y ′). It is a sum of independent variables (Xv)v∈V , where each Xv is distributed exactly like the X of Lemma 21, only with q replaced by qv. In particular,

and

E[J(Y ′)] =

Var(J(Y ′)) =

v∈V

E[Xv] =

v∈V

v∈V

ip(qv) = Φ (1 − ε)η

Var(Xv) K

v∈V

E[Xv] = KE[J(Y ′)].

Therefore, writing µ := E[J(Y ′)], Chebyshev’s inequality gives

Var(J(Y ′)) (εµ + C′)2

Kµ (εµ + C′)2 max x 0

P(Y ′ ∈/ Y2) = P J(Y ′) > (1 + ε)µ + C′

![image 272](<2021-kozma-lower-tails-relative-entropy_images/imageFile272.png>)

![image 273](<2021-kozma-lower-tails-relative-entropy_images/imageFile273.png>)

Kx (εx + C′)2

K 4C′ε

ε 2

K (εy + C′/y)2

, as desired.

= max

=

=

![image 274](<2021-kozma-lower-tails-relative-entropy_images/imageFile274.png>)

![image 275](<2021-kozma-lower-tails-relative-entropy_images/imageFile275.png>)

![image 276](<2021-kozma-lower-tails-relative-entropy_images/imageFile276.png>)

![image 277](<2021-kozma-lower-tails-relative-entropy_images/imageFile277.png>)

y>0

7. Applications

In this section, we derive Theorems 2, 3, and 4 from our main technical result, Theorem 5, and the general lower bound estimate for lower tail probabilities, Theorem 7. In order to do so, we just need to represent the number of copies of a given (hyper)graph H in subgraphs of the complete (hyper)graph (resp. the number of arithmetic progressions of a given length in subsets of positive integers) as the number of edges in some auxiliary hypergraph H and verify that H satisﬁes the assumptions of Theorem 5 when p ≫ n−1/mr(H). This is pretty straightforward, but we present the full details for the reader’s convenience.

The following easy lemma, which states that ΦHp , deﬁned in (6) above the statement of Theorem 5, satisﬁes ΦHp (η) = Θ v(H )p for every uniform hypergraph H whose maximum degree is comparable to its average degree, will be used to absorb the additive constant C from the assertions of Theorems 5 and 7 into the main term.

- Lemma 22. Suppose that H is an r-uniform hypergraph that satisﬁes


e(H ) v(H )

∆1(H ) K ·

![image 278](<2021-kozma-lower-tails-relative-entropy_images/imageFile278.png>)

for some K. Then, for all positive reals p and ε,

ΦHp (1 − ε)

ε2 2K2 · |V |p.

![image 279](<2021-kozma-lower-tails-relative-entropy_images/imageFile279.png>)

Proof. Let q: V → [0,1] be a function achieving the minimum in the deﬁnition of ΦHp and note that qv p for every v ∈ V . Indeed, otherwise ip(qv) > 0 = ip(p) and changing qv to p can only decrease E[e(H [R(q)])]. As qv p for every v ∈ V , it is easy to conclude that

p|A| −

(p − qv)p|A|−1 (53)

qv

v∈A

v∈A

for every A ⊆ V . We may thus conclude that

(⋆)

dA · p|A| −

εpre(H )

pre(H ) − E[e(H [R(q)])] =

qv

v∈A

A∈H

(53)

(p − qv)pr−1 =

(p − qv)pr−1 · degH v

dA ·

v∈A

v∈V

A∈H

(p − qv)pr−1 = pr−1∆1(H ) · p|V | −

∆1(H ) ·

qv ,

v∈V

v∈V

where (⋆) follows because q is the minimiser of Φ(1 − ε). Consequently, q¯ :=

εe(H ) |V | · ∆1(H )

1 |V | v∈V

ε K

qv p · 1 −

p · 1 −

. (54)

![image 280](<2021-kozma-lower-tails-relative-entropy_images/imageFile280.png>)

![image 281](<2021-kozma-lower-tails-relative-entropy_images/imageFile281.png>)

![image 282](<2021-kozma-lower-tails-relative-entropy_images/imageFile282.png>)

2

Since the function ip is convex and ip(q) (q−p)

2p when q p, see (50), we may conclude that

![image 283](<2021-kozma-lower-tails-relative-entropy_images/imageFile283.png>)

ΦHp (1 − ε) =

v∈V

(54) ε2 2K2 · |V |p,

(¯q − p)2 2p

ip(qv) |V | · ip(¯q) |V | ·

![image 284](<2021-kozma-lower-tails-relative-entropy_images/imageFile284.png>)

![image 285](<2021-kozma-lower-tails-relative-entropy_images/imageFile285.png>)

as claimed.

Proof of Theorems 2 and 3. Theorem 2 is merely the special case s = 2 in Theorem 3, so we focus on Theorem 3. Suppose that H is a nonempty s-uniform hypergraph and let H be the eH-uniform hypergraph with vertex set V := n s whose hyperedges are the edge sets of all

|Aut(H)| · v n

vH!

copies of H in the complete s-uniform hypergraph on n (we take dA = 1 for all A). By symmetry,

![image 286](<2021-kozma-lower-tails-relative-entropy_images/imageFile286.png>)

H

eH · e(H ) v(H )

.

∆1(H ) =

![image 287](<2021-kozma-lower-tails-relative-entropy_images/imageFile287.png>)

Suppose now that B ⊆ V has at least two elements and nonzero degree in H . Then B must be the edge set of some copy of a subhypergraph F ⊆ H, with eF = |B| 2, in the complete s-uniform hypergraph on n . Since ms(H) evF−1

F−s (recall the deﬁnition of ms given in (4)), we have

![image 288](<2021-kozma-lower-tails-relative-entropy_images/imageFile288.png>)

|B|−1

eF −1

−1 ms(H)

degH B nvH−vF = n−(vF−s) · nvH−s n−

· nvH−s. Since B was arbitrary, we may conclude that

ms(H) · nvH−s = n

![image 289](<2021-kozma-lower-tails-relative-entropy_images/imageFile289.png>)

![image 290](<2021-kozma-lower-tails-relative-entropy_images/imageFile290.png>)

u−1

1 ms(H)

∆u(H ) n−

· nvH−s (55) for every u 2.

![image 291](<2021-kozma-lower-tails-relative-entropy_images/imageFile291.png>)

Let λ be the constant given by Theorem 5 invoked with K = eH and εThm 5 = ε/2 and let C be the larger of the constants given by Theorems 5 and 7, also with εThm 7 = ε/2. Lastly, let L = L(ε,λ,C,H) be a suﬃciently large constant and suppose that Ln−1/ms(H) p p0.

By choosing L large, we guarantee that n is large as well and, consequently,

e(H ) v(H )

![image 292](<2021-kozma-lower-tails-relative-entropy_images/imageFile292.png>)

n vH n s

![image 293](<2021-kozma-lower-tails-relative-entropy_images/imageFile293.png>)

nvH−s 2vH!

.

![image 294](<2021-kozma-lower-tails-relative-entropy_images/imageFile294.png>)

Together with (55), this estimate implies that, for every u 2,

∆u(H ) 2vH! ·

p L

![image 295](<2021-kozma-lower-tails-relative-entropy_images/imageFile295.png>)

u−1

·

e(H ) v(H )

![image 296](<2021-kozma-lower-tails-relative-entropy_images/imageFile296.png>)

e(H ) v(H )

(λp)u−1 ·

,

![image 297](<2021-kozma-lower-tails-relative-entropy_images/imageFile297.png>)

where in the second inequality we used that L is suﬃciently large. By Theorems 5 and 7, for every η ∈ [0,1],

(1 − ε/2) · ΦHn,p(η + ε/2) − C −log P X ηE[X] (1 + ε/2) · ΦHn,p (1 − ε/2)η + C.

Finally, we show that we may absorb the additive constant C on both sides of the above inequality. To this end, we ﬁrst invoke Lemma 22 to get the following inequality:

ΦHn,p(1 − ε/2)

ε2 8e2H ·

![image 298](<2021-kozma-lower-tails-relative-entropy_images/imageFile298.png>)

n s

p

Lε2 16e2Hs!

![image 299](<2021-kozma-lower-tails-relative-entropy_images/imageFile299.png>)

2C ε

, (56)

![image 300](<2021-kozma-lower-tails-relative-entropy_images/imageFile300.png>)

where we used the assumptions that p Ln−1/ms(H) Ln−s and that L is suﬃciently large. To derive the claimed the upper bound on −log P(X ηE[X]), note that, since η 1 and the function η  → Φn,p(η) is decreasing, we have

(56)

(ε/2) · ΦHn,p (1 − ε/2)η and ΦHn,p (1 − ε/2)η ΦHn,p (1 − ε)η .

C

To derive the claimed lower bound, we may assume that η+ε 1, since otherwise ΦHn,p(η+ε) = 0. Therefore,

(56)

(ε/2) · ΦHn.p(η + ε/2) and ΦHn.p(η + ε/2) ΦHn,p(η + ε). This completes the proof of Theorems 2 and 3.

C

Proof of Theorems 4. Let k be a positive integer and let H be the k-uniform hypergraph with vertex set V := n whose hyperedges are the k-term arithmetic progressions in n , that is,

H := {x,x + d,... ,x + (k − 1)d} : x,d ∈ n ,x + (k − 1)d n . Since every number in n belongs to at most kn many k-term arithmetic progressions and every pair of numbers belongs to at most k2 such progressions, we have

∆1(H ) = kn and ∆k(H ) ··· ∆2(H )

k 2

.

Moreover, since n contains at least ckn2 many k-term progressions, for some constant ck > 0, provided that n k, we conclude that e(H ) ckn2 and hence

1 k−1

∆s(H ) K · n−

![image 301](<2021-kozma-lower-tails-relative-entropy_images/imageFile301.png>)

s−1

·

e(H ) v(H ) ∀s ∈ {1,... ,k}

![image 302](<2021-kozma-lower-tails-relative-entropy_images/imageFile302.png>)

for some constant K that depends only on k. Therefore, when Ln−1/(k−1) p p0 for a suﬃciently large constant L, we may apply Theorems 5 and 7 to derive (with a little help from Lemma 22) the claimed estimate on −log P(X ηE[X]) for every η ∈ [0,1], as in the previous proof. We leave the details to the reader.

References

- 1. Fanny Augeri, Nonlinear large deviation bounds with applications to Wigner matrices and sparse Erd˝os-R´enyi graphs, Ann. Probab. 48 (2020), no. 5, 2404–2448.
- 2. A. Avez, Harmonic functions on groups, Diﬀerential geometry and relativity, 1976, pp. 27–32. Mathematical Phys. and Appl. Math., Vol. 3.
- 3. J´ozsef Balogh, Robert Morris, and Wojciech Samotij, Independent sets in hypergraphs, J. Amer. Math. Soc. 28 (2015), no. 3, 669–709.
- 4. J´ozsef Balogh and Wojciech Samotij, An eﬃcient container lemma, Discrete Anal. (2020), Paper No. 17, 56.
- 5. Anirban Basak and Riddhipratim Basu, Upper tail large deviations of regular subgraph counts in Erd˝os–R´enyi graphs in the full localized regime, arXiv:1912.11410 [math.PR].
- 6. Bhaswar B. Bhattacharya, Shirshendu Ganguly, Eyal Lubetzky, and Yufei Zhao, Upper tails and independence polynomials in random graphs, Adv. Math. 319 (2017), 313–347.
- 7. Sourav Chatterjee, The missing log in large deviations for triangle counts, Random Structures Algorithms 40

(2012), no. 4, 437–451.

- 8. Sourav Chatterjee and Amir Dembo, Nonlinear large deviations, Adv. Math. 299 (2016), 396–450.
- 9. Sourav Chatterjee and S. R. S. Varadhan, The large deviation principle for the Erd˝os-R´enyi random graph, European J. Combin. 32 (2011), no. 7, 1000–1017.
- 10. David Conlon and William T. Gowers, Combinatorial theorems in sparse random sets, Ann. of Math. (2) 184

(2016), no. 2, 367–454.

- 11. Nicholas Cook and Amir Dembo, Large deviations of subgraph counts for sparse Erd˝os-R´enyi graphs, Adv. Math. 373 (2020), 107289, 53.
- 12. Nicholas Cook, Amir Dembo, and Huy Tuan Pham, Regularity method and large deviation principles for the Erd˝os–R´enyi hypergraph, arXiv:2102.09100 [math.PR].
- 13. Thomas M. Cover and Joy A. Thomas, Elements of information theory, second ed., Wiley-Interscience [John Wiley & Sons], Hoboken, NJ, 2006.
- 14. Imre Csisz´r, Sanov property, generalized I-projection and a conditional limit theorem, Ann. Probab. 12

(1984), no. 3, 768–793.

- 15. Imre Csisz´r and J´anos K¨rner, Information theory, second ed., Cambridge University Press, Cambridge, 2011, Coding theorems for discrete memoryless systems.
- 16. Bobby DeMarco and Jeﬀ Kahn, Upper tails for triangles, Random Structures Algorithms 40 (2012), no. 4, 452–459.
- 17. Ronen Eldan, Gaussian-width gradient complexity, reverse log-Sobolev inequalities and nonlinear large deviations, Geom. Funct. Anal. 28 (2018), no. 6, 1548–1596.
- 18. P. Erd˝s, D. J. Kleitman, and B. L. Rothschild, Asymptotic enumeration of Kn-free graphs, Colloquio Internazionale sulle Teorie Combinatorie (Rome, 1973), Tomo II, 1976, pp. 19–27. Atti dei Convegni Lincei, No. 17.


- 19. Alan Frieze and Ravi Kannan, Quick approximation to matrices and applications, Combinatorica 19 (1999), no. 2, 175–220.
- 20. Matan Harel, Frank Mousset, and Wojciech Samotij, Upper tails via high moments and entropic stability, arXiv:1904.08212 [math.PR].
- 21. Svante Janson, Poisson approximation for large deviations, Random Structures Algorithms 1 (1990), no. 2, 221–229.
- 22. Svante Janson, Tomasz  Luczak, and Andrzej Rucin´ski, An exponential bound for the probability of nonexistence of a speciﬁed subgraph in a random graph, Random graphs ’87 (Poznan´, 1987), Wiley, Chichester, 1990, pp. 73– 87.
- 23. Yoshiharu Kohayakawa, Tomasz  Luczak, and Vojteˇch Ro¨dl, On K4-free subgraphs of random graphs, Combinatorica 17 (1997), no. 2, 173–213.
- 24. Gady Kozma, Tom Meyerovitch, Ron Peled, and Wojciech Samotij, What does a typical metric space look like?, arXiv:2104.01689.
- 25. Eyal Lubetzky and Yufei Zhao, On replica symmetry of large deviations in random graphs, Random Structures Algorithms 47 (2015), no. 1, 109–146.
- 26. , On the variational problem for upper tails in sparse random graphs, Random Structures Algorithms 50 (2017), no. 3, 420–436.

![image 303](<2021-kozma-lower-tails-relative-entropy_images/imageFile303.png>)

- 27. Tomasz  Luczak, On triangle-free random graphs, Random Structures Algorithms 16 (2000), no. 3, 260–276.
- 28. David Saxton and Andrew Thomason, Hypergraph containers, Invent. Math. 201 (2015), no. 3, 925–992.
- 29. Mathias Schacht, Extremal results for random discrete structures, Ann. of Math. (2) 184 (2016), no. 2, 333– 365.
- 30. Yufei Zhao, On the lower tail variational problem for random graphs, Combin. Probab. Comput. 26 (2017), no. 2, 301–320.


Department of Mathematics, The Weizmann Institute of Science, Rehovot 7610001, Israel Email address: gady.kozma@weizmann.ac.il

School of Mathematical Sciences, Tel Aviv University, Tel Aviv 6997801, Israel Email address: samotij@tauex.tau.ac.il

