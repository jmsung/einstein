---
type: source
kind: paper
title: Distribution of power residues over shifted subfields and maximal cliques in generalized Paley graphs
authors: Greg Martin, Chi Hoi Yip
year: 2024
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2403.04312v2
source_local: ../raw/2024-martin-distribution-power-residues-shifted.pdf
topic: general-knowledge
cites:
---

arXiv:2403.04312v2[math.NT]10Aug2024

DISTRIBUTION OF POWER RESIDUES OVER SHIFTED SUBFIELDS AND MAXIMAL CLIQUES IN GENERALIZED PALEY GRAPHS

GREG MARTIN AND CHI HOI YIP

ABSTRACT. We derive an asymptotic formula for the number of solutions in a given subﬁeld to certain system of equations over ﬁnite ﬁelds. As an application, we construct new families of maximal cliques in generalized Paley graphs. Given integers d ≥ 2 and q ≡ 1 (mod d), we show that for each positive integer m such that rad(m) | rad(d), there are maximal cliques of size approximately q/m in the d-Paley graph deﬁned on Fqd. We also conﬁrm a conjecture of Goryainov, Shalaginov, and Yip on the maximality of certain cliques in generalized Paley graphs, as well as an analogous conjecture of Goryainov for Peisert graphs.

1. INTRODUCTION

Throughout this paper, q will always denote a prime power and Fq the ﬁnite ﬁeld with q elements, and we write F∗q = Fq \ {0}.

Let d ≥ 2 be an integer, and let q ≡ 1 (mod d) be a sufﬁciently large prime power. It is well known that the set of d-th powers (of nonzero elements) in Fq behaves like a random set [19]. There are different ways to make this statement precise. One typical way to do so is to consider the following well-known lemma [13, Exercise 5.66], which follows from a standard application of Weil’s bound on complete character sums.

- Lemma 1.1. Let v1, . . ., vk be distinct elements of the ﬁnite ﬁeld Fq and let d | (q − 1), where


d ≥ 2. Let M be the number of solutions x ∈ Fq to the system of equations (x − vi)(q−1)/d = 1 (i = 1, . . ., k). Then |M − q/dk| ≤ k√q.

![image 1](<2024-martin-distribution-power-residues-shifted_images/imageFile1.png>)

In other words, the number of x ∈ Fq such that x − vi is a d-th power for all i is asymptotically equal to q/dk. Note that if we model the set of d-th powers as a random subset S of Fq with density 1/d, then the expected number of x ∈ Fq such that each x − vi ∈ S would also be q/dk; in this sense, the set of d-th powers in Fq behaves like a random set. Lemma 1.1 and its generalizations have plenty of applications in number theory, combinatorics, and ﬁnite geometry; we refer the reader to an excellent survey by Sz˝onyi [17].

While Lemma 1.1 states that globally the solutions behave randomly, it is desirable to obtain reﬁned information on the distribution of these solutions for various applications. In this paper, we aim to understand the “local distribution” of these solutions within a given subﬁeld, or equivalently the distribution of power residues in a shifted subﬁeld. More precisely, given a ﬁeld extension K/L of ﬁnite ﬁelds with |L| ≡ 1 (mod d), we want to count the number of solutions of (x−vi)(|K|−1)/d = 1 in the base ﬁeld L, where v1, . . ., vk ∈ K. Without loss of generality, assume that L = Fq and K = Fqn. Our ﬁrst main result gives an asymptotic formula for the number of solutions.

![image 2](<2024-martin-distribution-power-residues-shifted_images/imageFile2.png>)

2020 Mathematics Subject Classiﬁcation. 11T24, 11B30, 05C25. Key words and phrases. character sum, subﬁeld, maximal clique, Paley graph, Peisert graph.

Theorem 1.2. Let d ≥ 2 and q ≡ 1 (mod d). For 1 ≤ i ≤ k, let vi ∈ Fqn be of degree di over Fq, and let M be the number of solutions x in the base ﬁeld Fq to the system of k equations (x − vi)(qn−1)/d = 1. Suppose that vi and vj are not Galois conjugates with respect to the ﬁeld extension Fqn/Fq whenever i = j. Then

k

gcd(ddi, n) ddi ≤

M − q

![image 3](<2024-martin-distribution-power-residues-shifted_images/imageFile3.png>)

i=1

k

di − 1 √q.

![image 4](<2024-martin-distribution-power-residues-shifted_images/imageFile4.png>)

i=1

We remark that the assumption that no two vi are Galois conjugates is necessary. Indeed, if vi and vj are Galois conjugates, then for x ∈ Fq, it is easy to verify that (x − vi)(qn−1)/d = 1 if and only if (x − vj)(qn−1)/d = 1.

- Theorem 1.2 recovers a few known results in the literature. In particular, if n = 1, then di = 1

for all i and Theorem 1.2 recovers Lemma 1.1. Also, in the special case d = 2, k = 1, n even, and v1 ∈/ Fqn/2, Theorem 1.2 shows that the number of solutions is q/2+ O(n√q), which recovers a result of Hirschfeld and Sz˝onyi [12]; moreover, they showed this special case already has some nice applications in ﬁnite geometry.

![image 5](<2024-martin-distribution-power-residues-shifted_images/imageFile5.png>)

We also prove the following theorem, which complements Theorem 1.2 when n = 2 and q  ≡ 1 (mod d).

- Theorem 1.3. Let d ≥ 2 and let q2 ≡ 1 (mod d). Choose v1, v2, . . ., vk ∈ Fq2 \ Fq, no two of which are Galois conjugates. Let M be the number of solutions x in Fq to the system of equations (x − vi)(q2−1)/d = 1 for 1 ≤ i ≤ k. Then


q dk ≤ (2k − 1)√q.

M −

![image 6](<2024-martin-distribution-power-residues-shifted_images/imageFile6.png>)

![image 7](<2024-martin-distribution-power-residues-shifted_images/imageFile7.png>)

Note that if q ≡ −1 (mod d), then we always have (x−v)(q2−1)/d = 1 when v, x ∈ Fq and x = v. Also note that the condition that no two vi are Galois conjugates is necessary, for the same reason as in Theorem 1.2. We remark that some related results have appeared in [20, Corollaries 2.4 and 2.5]. However, the statements of those two corollaries omitted some necessary hypotheses1. In Section 3, we shall state and prove a corrected version for the sake of completeness. In particular, we will prove Theorem 3.2 and then deduce Theorem 1.3 as a consequence. One can use Theorem 3.2 to prove a more general result on the distribution of power residues over shifted subﬁelds.

Before discussing the applications of Theorem 1.2 and Theorem 1.3, we introduce some necessary terminology. Generalized Paley graphs are well-studied Cayley graphs, ﬁrst introduced by Cohen [5] in 1988 and reintroduced by several groups of authors since then. Let d ≥ 2 be an integer and q a prime power such that q ≡ 1 (mod 2d). The d-Paley graph on Fq, denoted GP(q, d), is the graph with vertex set Fq such that two vertices are adjacent if their difference is a d-th power in F∗q. Note that the condition q ≡ 1 (mod 2d) guarantees the graph is undirected and non-degenerate; see for example [5, Section 4]. The well-known Paley graphs are simply 2-Paley graphs. We refer to [2, 8, 9, 10, 21, 23] for extensive discussions on different constructions of maximal cliques in generalized Paley graphs; we also refer to [16, Proposition 2] for a nice connection between maximal cliques in Paley graphs and minimal blocking sets.

Recall that a clique C in a graph G is a subset of vertices of G such that every two distinct vertices in C are adjacent. A maximal clique is a clique that cannot be extended by adding a new

![image 8](<2024-martin-distribution-power-residues-shifted_images/imageFile8.png>)

1Private communication with Daqing Wan. For example, [20, Corollary 2.4] does not apply to the case m = 2,n = 1 and f1(T) = (T − a)(T − aq) for a ∈ Fq2 \ Fq.

vertex. Every maximum clique (a clique of highest cardinality) is a maximal clique, but there can be smaller maximal cliques as well. As an application of Theorem 1.2, we construct new families of maximal cliques in generalized Paley graphs of the form GP(qd, d), where q is an odd prime power such that q ≡ 1 (mod d). It is known that if q > (d − 1)2, then the subﬁeld Fq forms a maximal clique in such a graph [23, Theorem 1.2]. Our next result constructs many new maximal cliques with smaller sizes. To state the theorem, recall that for a positive integer m, its radical rad(m) is deﬁned to be the product of the distinct prime divisors of m. In particular, rad(m) | rad(d) if and only if every prime dividing m also divides d. We let logr denote the base-r logarithm.

- Theorem 1.4. Let d ≥ 2 and let r be the smallest prime divisor of d. Let m be a positive integer such that rad(m) | rad(d). If q ≡ 1 (mod d) is an odd prime power such that


q > (8 logr m + 4)d2m2,

then there is a maximal clique C in GP(qd, d) with size |C| = mq +O(d logm√q). More precisely, q m − d logr m ·

![image 9](<2024-martin-distribution-power-residues-shifted_images/imageFile9.png>)

![image 10](<2024-martin-distribution-power-residues-shifted_images/imageFile10.png>)

√q ≤ |C| ≤

+ d logr m · (√q + 1).

q m

![image 11](<2024-martin-distribution-power-residues-shifted_images/imageFile11.png>)

![image 12](<2024-martin-distribution-power-residues-shifted_images/imageFile12.png>)

![image 13](<2024-martin-distribution-power-residues-shifted_images/imageFile13.png>)

![image 14](<2024-martin-distribution-power-residues-shifted_images/imageFile14.png>)

In particular, if d ≥ 2 is ﬁxed and m is a positive integer such that rad(m) | rad(d), then there is a maximal clique of size approximately q/m in GP(qd, d), provided that q ≡ 1 (mod d) is sufﬁciently large. (We believe that these are the only possible approximate sizes of maximal cliques; see Conjecture 6.4 for a more precise statement.) When d = 2 and m is a power of 2, this recovers a result of Hirschfeld and Sz˝onyi on maximal cliques in Paley graphs of square order, which they did not state explicitly but is implicit in their constructions of minimal blocking sets [11, 16]. It would be interesting to see if Theorem 1.4 has some applications in ﬁnite geometry.

For our second application, we focus on generalized Paley graphs of the form GP(q2, d), where q is an odd prime power such that d | (q+1). Such generalized Paley graphs are of particular interest since the subﬁeld Fq forms a maximum clique, and it is known that the only maximum clique containing 0 and 1 is the subﬁeld Fq; see Blokhuis [3] for Paley graphs (that is, when d = 2) and Sziklai [18] for general d. This characterization of maximum cliques is also known as the Erd˝os– Ko–Rado (EKR) theorem for the graph GP(q2, d), in the sense that all maximum cliques are given by afﬁne translates of the subﬁeld Fq; see related discussions in [1, 24] and [7, Section 5.9].

Baker, Ebert, Hemmeter, and Woldar [2] constructed maximal cliques that are not maximum in the Paley graph GP(q2, 2) as the following. Pick an element α ∈ Fq2 \ Fq, and consider the clique C obtained by α and its Fq-neighborhood, that is,

C = {α} ∪ {x ∈ Fq : α − x ∈ (F∗q2)2}.

They showed that C is a maximal clique of size q+12 if q ≡ 1 (mod 4), and C ∪ {αq} is a maximal clique of size q+32 if q ≡ 3 (mod 4). Their construction is also known as the (Fq, α)-construction [8, 9]. Analogously, Goryainov, Shalaginov, and Yip [10] considered a similar construction of cliques in GP(q2, d), where d | (q + 1) and d ≥ 3. Let u ∈ Fq2 \ Fq and let N(u) be the Fqneighborhood of u in GP(q2, d). Let Cu = N(u) ∪ {u} if d ∤ q+12 , and Cu = N(u) ∪ {u, uq} if d | q+12 , which they described [10, Proposition 4.6] as a clique from the (Fq, α)-construction. They conjectured that such a clique Cu is maximal if 3 ≤ d ≤ q+13 and p ∤ (d − 1), where p is the characteristic of the ﬁeld Fq [10, Conjecture 4.7]; see [10, Corollary 3.4] and [10, Example 5.9] for the necessity of these two additional assumptions. Some partial progress of the conjecture can be found in [10, Section 5]. In particular, they proved the conjecture when gcd(q − 1, q+1d − 2) ∈

![image 15](<2024-martin-distribution-power-residues-shifted_images/imageFile15.png>)

![image 16](<2024-martin-distribution-power-residues-shifted_images/imageFile16.png>)

![image 17](<2024-martin-distribution-power-residues-shifted_images/imageFile17.png>)

![image 18](<2024-martin-distribution-power-residues-shifted_images/imageFile18.png>)

![image 19](<2024-martin-distribution-power-residues-shifted_images/imageFile19.png>)

![image 20](<2024-martin-distribution-power-residues-shifted_images/imageFile20.png>)

{1, 2} [10, Corollary 5.4]. We are able to conﬁrm their conjecture when q is sufﬁciently large compared to d.

- Theorem 1.5. Let d ≥ 3. If q ≡ −1 (mod d) is an odd prime power such that q > 10d4/(d − 1)2, then in GP(q2, d), cliques obtained from the (Fq, α)-construction are maximal. More precisely, if u ∈ Fq2 \ Fq and N(u) is the Fq-neighborhood of u in GP(q2, d), then the following statements hold:

- (a) If d ∤ q+12 , then N(u) ∪ {u} forms a maximal clique of size q+1d in GP(q2, d).

![image 21](<2024-martin-distribution-power-residues-shifted_images/imageFile21.png>)

![image 22](<2024-martin-distribution-power-residues-shifted_images/imageFile22.png>)

- (b) If d | q+12 , then N(u) ∪ {u, uq} forms a maximal clique of size q+dd+1 in GP(q2, d).


![image 23](<2024-martin-distribution-power-residues-shifted_images/imageFile23.png>)

![image 24](<2024-martin-distribution-power-residues-shifted_images/imageFile24.png>)

Our techniques extend to a larger family of Cayley graphs, and in particular to Peisert graphs. Let p ≡ 3 (mod 4) be a prime and q = pr with r even. The Peisert graph of order q = pr, denoted Pq∗, is deﬁned to be the graph with vertex set Fq such that two vertices are adjacent if their difference belongs to the set S = {gj : j ≡ 0, 1 (mod 4)}, where g is a primitive root of the ﬁeld Fq. Note the structure of the graph does not depend on the choice of the primitive root. Peisert [14] showed that the only self-complementary symmetric graphs are Paley graphs, Peisert graphs, and an exceptional graph of order 529. Asgarli and Yip [1, Theorem 1.4] showed an analgoue of the EKR theorem for the Peisert graph Pq∗2 with q ≡ 3 (mod 4); more precisely, the only maximum clique containing 0, 1 in Pq∗2 is the subﬁeld Fq if q = pn and p > 8.2n2, where p is the characteristic of Fq. Sergey Goryainov conjectured2 that (Fq, α)-constructions also give maximal cliques in Pq∗2 with q ≡ 3 (mod 4) and q ≥ 7, based on the similarity between Paley graphs and Peisert graphs. We conﬁrm his conjecture using a similar method.

- Theorem 1.6. Let q ≡ 3 (mod 4) be a prime power such that q ≥ 7. Let u ∈ Fq2 \Fq and let N(u) be the Fq-neighborhood of u in Pq∗2. Then N(u) ∪ {u} forms a maximal clique of size q+12 in Pq∗2.


![image 25](<2024-martin-distribution-power-residues-shifted_images/imageFile25.png>)

The paper is organized as follows. In Section 2, we prove Theorem 1.2. In Section 3, we establish some estimates on character sums over subﬁelds and prove Theorem 1.3. In Section 4, we construct new maximal cliques in generalized Paley graphs and prove Theorem 1.4. In Section 5, we study the maximality of cliques obtained from the (Fq, α)-construction and prove Theorem 1.5 as well as Theorem 1.6. We end the paper with some remarks and open questions in Section 6.

2. PROOF OF THEOREM 1.2 Consider the norm map NF

qn/Fq : Fqn → Fq of the ﬁeld extension Fqn/Fq; explicitly,

n−1

qn−1

j

xq

= x

qn/Fq(x) =

NF

q−1 .

![image 26](<2024-martin-distribution-power-residues-shifted_images/imageFile26.png>)

j=0

The next lemma provides a criterion to determine whether an element x in Fqn is a d-th power based on its norm NF

qn/Fq(x). To discuss d-th powers in the base ﬁeld Fq, we need to further assume d | (q − 1).

- Lemma 2.1. Assume d | (q − 1). Let x ∈ Fqn. Then x is a d-th power in Fqn if and only if


qn/Fq(x) is a d-th power in Fq. 2Private communication

NF

![image 27](<2024-martin-distribution-power-residues-shifted_images/imageFile27.png>)

Proof. The case x = 0 is trivial. Next, assume x = 0. Let g be a primitive root of Fqd. Let x = gk. Then x is a d-th power in Fqn if and only if d | k. Note that NF

qn−1

qn/Fq(g) = g

q−1 is a primitive root of Fq. Thus, NF

![image 28](<2024-martin-distribution-power-residues-shifted_images/imageFile28.png>)

qn−1

q−1 )k is a d-th power in Fq if and only if d | k, as claimed.

qn/Fq(x) = (g

![image 29](<2024-martin-distribution-power-residues-shifted_images/imageFile29.png>)

To prove Theorem 1.2, we also need the celebrated Weil bound; see for example [13, Theorem 5.41].

- Lemma 2.2 (Weil’s bound). Let χ be a multiplicative character of Fq of order d > 1, and let f ∈ Fq[z] be a monic polynomial of positive degree that is not a d-th power of a polynomial. Let m be the number of distinct roots of f in its splitting ﬁeld over Fq. Then for any a ∈ Fq,


χ af(z) ≤ (m − 1)√q .

![image 30](<2024-martin-distribution-power-residues-shifted_images/imageFile30.png>)

z∈Fq

Now we are ready to present the proof of Theorem 1.2.

- Proof of Theorem 1.2. Let gi(z) be the minimal polynomial of vi over Fq; then gi(z) has degree di and


di−1

j

(z − vq

gi(z) =

i ).

j=0

Let fi = gin/di. Then fi is of degree n, and each root of fi is a Galois conjugate of vi with multiplicity n/di.

di

Note that for each z ∈ Fq, since vq

i = vi, we have

di−1

n−1

n−1

j

j

j

(z − vq

(z − vq

(z − vi)q

i )n/d

qn/Fq(z − vi).

= NF

i ) =

=

fi(z) =

i

j=0

j=0

j=0

Let χ be a multiplicative character of Fq, with order d. If x ∈ Fq, then (x − vi)(qn−1)/d = 1 for each i if and only if x − vi is a d-th power in Fqn for each i, if and only if fi(x) = NF

qn/Fq(x − vi) is a d-th power in Fq for each i (by Lemma 2.1), if and only if χ(fi(x)) = 1 for each i.

By the orthogonality relations, d1 dj=0−1 χj is the indicator function of d-th powers in F∗q. Therefore, by the above discussion, the number of solutions to the given system of equations is

![image 31](<2024-martin-distribution-power-residues-shifted_images/imageFile31.png>)

k

M =

i=1

x∈Fq

d−1

1 d

1 dk 0≤j

χj(fi(x)) =

χ

![image 32](<2024-martin-distribution-power-residues-shifted_images/imageFile32.png>)

![image 33](<2024-martin-distribution-power-residues-shifted_images/imageFile33.png>)

j=0

1,j2,...,jk≤d−1 x∈Fq

k

i=1

fj

i (x) . (1)

i

Since vi and vj are not Galois conjugates whenever i = j, it follows that f1, f2, . . ., fk are pairwise coprime. It follows that ki=1 fj

i (z) is a d-th power of a polynomial if and only if d | ji · n/di for each i, or equivalently,

i

ddi gcd(ddi, n) | ji. Thus, the number of k-tuples (j1, j2, . . ., jk) such that 0 ≤ ji ≤ d − 1 and ki=1 fj

![image 34](<2024-martin-distribution-power-residues-shifted_images/imageFile34.png>)

i

i (z) is a d-th power of a polynomial is

k

k

gcd(ddi, n) di

d gcd(ddi, n) ddi

=

,

![image 35](<2024-martin-distribution-power-residues-shifted_images/imageFile35.png>)

![image 36](<2024-martin-distribution-power-residues-shifted_images/imageFile36.png>)

i=1

i=1

and the contribution of these k-tuples (corresponding to trivial character sums) to the sum (1) is q dk ·

k

k

gcd(ddi, n) ddi

gcd(ddi, n) di

= q ·

.

![image 37](<2024-martin-distribution-power-residues-shifted_images/imageFile37.png>)

![image 38](<2024-martin-distribution-power-residues-shifted_images/imageFile38.png>)

![image 39](<2024-martin-distribution-power-residues-shifted_images/imageFile39.png>)

i=1

i=1

When ki=1 fj

i (z) is not a d-th power of a polynomial, the number of distinct roots of the polyno-

i

mial ki=1 fi(z) in its splitting ﬁeld is at most ki=1 di, and thus Weil’s bound (Lemma 2.2) implies that

k

k

di − 1 √q.

fj

χ

i (x) ≤

i

![image 40](<2024-martin-distribution-power-residues-shifted_images/imageFile40.png>)

i=1

i=1

x∈Fq

We conclude that

k

M − q ·

i=1

gcd(ddi, n) ddi ≤

1 dk · dk ·

![image 41](<2024-martin-distribution-power-residues-shifted_images/imageFile41.png>)

![image 42](<2024-martin-distribution-power-residues-shifted_images/imageFile42.png>)

k

di − 1 √q =

![image 43](<2024-martin-distribution-power-residues-shifted_images/imageFile43.png>)

i=1

k

di − 1 √q

![image 44](<2024-martin-distribution-power-residues-shifted_images/imageFile44.png>)

i=1

as required.

3. PROOF OF THEOREM 1.3

Similar to the discussions in the previous section, the proof of Theorem 1.3 will be based on character sums. Clearly, we need to estimate character sums of the form x∈F

χ(f(x)), where χ

q

is a multiplicative character of Fq2. The key idea is to convert the desired character sum over ﬁnite ﬁelds to an equivalent character sum over function ﬁelds.

Let Fq[T] be the polynomial ring in variable T over Fq. Let f ∈ Fq[T] be a non-constant polynomial. A Dirichlet character modulo f, usually denoted by χf, is a character on the multiplicative group (Fq[T]/fFq[T])∗, which can be extended to a function on Fq[T] by setting χf(g) = χf(g mod f) if f and g are coprime, and χf(g) = 0 otherwise. We refer to [15, Section 4] for more background.

We need the following Weil bound on character sums over monic linear polynomials; see for example [20, Theorem 2.1].

- Lemma 3.1. Let f ∈ Fq[T] be a polynomial with degree n ≥ 1, and let χf be a non-trivial Dirichlet character modulo f. Then


χf(T − a) ≤ (n − 1)√q.

![image 45](<2024-martin-distribution-power-residues-shifted_images/imageFile45.png>)

a∈Fq

From this lemma, we can deduce the following theorem.

Theorem 3.2. Let f1, f2, . . ., fk be monic irreducible polynomials in Fqn[T], no two of which are Galois conjugates over Fq. Let χ1, χ2, . . ., χk be multiplicative character of Fqn. Assume that there exists 1 ≤ i ≤ k such that fi has a root ξi such that χi is not identically 1 on the set NF

(Fq[ξi])\{0}. Let bi be the degree of fi(T) and ci be the number of conjugates of fi(T) over Fq. Then

qn[ξi]/Fqn

k

k

bici − 1 √q .

χi fi(a) ≤

![image 46](<2024-martin-distribution-power-residues-shifted_images/imageFile46.png>)

i=1

i=1

a∈Fq

In particular, if m = ki=1 bi is the sum of the degree of the fi, then

a∈Fq

k

χi fi(a) ≤ (mn − 1)√q .

![image 47](<2024-martin-distribution-power-residues-shifted_images/imageFile47.png>)

i=1

Proof. For each 1 ≤ i ≤ k, let ξi be a root of fi. Since fi is a monic irreducible polynomial in Fqn[T], it follows that fi is the minimal polynomial of ξi over Fqn and thus

fi(a) = NF

qn[ξi]/Fqn(a − ξi) (2)

for a ∈ Fq. For each 1 ≤ i ≤ k, let Fi be the product of conjugates of fi(T) over Fq. Then, F1, F2, . . ., Fk are deﬁned and irreducible over Fq. Since no two of f1, f2, . . ., fk are Galois conjugates over Fq, it follows that F1, F2, . . ., Fk are coprime. Let F = ki=1 Fi. Since deg(Fi) = bici, it follows that deg(F) = ki=1 bici.

For g ∈ Fq[T], deﬁne

χF

(g) = χi(NF

(g(ξi))). (3) Note that χF

qn[ξi]/Fqn

i

is a Dirichlet character modulo Fi. Note also that, as g runs over Fq[T], g(ξi) runs over Fq[ξi], and thus the norm NF

i

(g(ξi)) runs over the set NF

(Fq[ξi]). Thus, if χi is not identically 1 on the set NF

qn[ξi]/Fqn

qn[ξi]/Fqn

(Fq[ξi]) \ {0}, then χF

is non-trivial by deﬁnition. Therefore, by the given assumption, at least one of the characters χF

qn[ξi]/Fqn

i

, χF

, . . ., χF

is non-trivial. Since F1, F2, . . ., Fk are irreducible coprime polynomials, by the Chinese remainder theorem, the product χF := ki=1 χF

k

1

2

is a non-trivial Dirichlet character modulo F. Therefore, by Lemma 3.1 and equations (2) and (3),

i

k

χi fi(a) =

i=1

a∈Fq

k

χF

(a − T) =

i

i=1

a∈Fq

χF(a − T) ≤

a∈Fq

k

bici − 1 √q,

![image 48](<2024-martin-distribution-power-residues-shifted_images/imageFile48.png>)

i=1

as required. Since ci ≤ n, we always have ki=1 bici ≤ n ki=1 bi = mn.

- Remark 3.3. From the above proof, we can infer that the assumption that “there exists 1 ≤ i ≤ k


such that fi has a root ξi such that χi is not identically 1 on the set NF

qn[ξi]/Fqn(Fq[ξi]) \ {0}” in Theorem 3.2 is equivalent to the character sum being non-trivial. In particular, if this condition does not hold, then the character sum in Theorem 3.2 is q.

Next, we use Theorem 3.2 to deduce Theorem 1.3.

- Proof of Theorem 1.3. For each 1 ≤ i ≤ k, let fi(T) = T − vi ∈ Fq2[T]. By the assumption, no two of f1, . . ., fk are Galois conjugates of each other. Note that for each 1 ≤ i ≤ k, we have


q2/Fq2(Fq2) = Fq2 since vi ∈ Fq2 \ Fq.

NF

- q2[vi]/Fq2(Fq[vi]) = NF


Let χ be a multiplicative character in Fq2, with order d. Similar to the proof of Theorem 1.2, the number of solutions to the given system of equations is

1 dk 0≤j

χ

M =

![image 49](<2024-martin-distribution-power-residues-shifted_images/imageFile49.png>)

1,j2,...,jk≤d−1 x∈Fq

k

fj

i (x) . (4)

i

i=1

When j1 = j2 = · · · = jk = 0, the character sum contributes to dq

to M. In all other cases, at least one of χj

![image 50](<2024-martin-distribution-power-residues-shifted_images/imageFile50.png>)

k

, . . ., χjk

, χj

is a nontrivial character since χ has order d, and Theorem 3.2 implies that

2

1

χ

x∈Fq

k

fj

i (x) =

i

i=1

k

i=1

x∈Fq

(fi(x)) ≤ (2k − 1)√q.

χj

![image 51](<2024-martin-distribution-power-residues-shifted_images/imageFile51.png>)

i

Therefore, summing over k-tuples (j1, j2, . . ., jk) in equation (4), we conclude that M −

q

dk ≤ (2k − 1)√q, as required.

![image 52](<2024-martin-distribution-power-residues-shifted_images/imageFile52.png>)

![image 53](<2024-martin-distribution-power-residues-shifted_images/imageFile53.png>)

- Remark 3.4. Our proof of Theorem 1.3 in this section employed character sums over ﬁnite ﬁelds. One can give another proof of Theorem 1.2 using Theorem 3.2 and Remark 3.3, which employ character sums over function ﬁelds. To see that, we again set fi(T) = T − vi ∈ Fqn[T] for each 1 ≤ i ≤ k, and equation (4) still applies. Since vi has degree di over Fq, the number of conjugates


qn[vi]/Fqn(Fq[vi])\{0} = F∗qd

of fi over Fq also is di. Note that we have NF

, and thus the main term q ki=1 gcd(dd

i

ddi in Theorem 1.2 follows from Remark 3.3, and the error term ( ki=1 di − 1)√q in Theorem 1.2 comes from Theorem 3.2. While the exact machinery of the two proofs are different, there are deﬁnite similarities and the two proofs are probably essentially equivalent.

i,n)

![image 54](<2024-martin-distribution-power-residues-shifted_images/imageFile54.png>)

![image 55](<2024-martin-distribution-power-residues-shifted_images/imageFile55.png>)

Next, we state and prove a corrected version of [20, Corollary 2.4]. Any monic polynomial f ∈ Fqn[T] with positive degree can be factorized as the product of monic irreducible polynomials in Fqn[T]:

s

ft

f =

i ,

i

i=1

where the fi are distinct irreducible polynomials. Let ξ be a root of f1. By relabelling, we may assume f1, f2, . . ., fr are the conjugates of f1 over Fq. Let σ: x  → xq be the Frobenius map deﬁned on Fqn; note that σ naturally induces a map on Fqn[T]. Then for each 1 ≤ i ≤ r, we can write fi = σα

(f1) for some 0 ≤ αi ≤ n − 1. We deﬁne the total multiplicity of ξ to be

i

r

tiqα

m =

,

i

i=1

which is the sum of weighted multiplicities among conjugates of ξ. Observe that if χ is a character over Fqn, then we have

s

χt

(fi(a)).

χ(f(a)) =

i

i=1

a∈Fq

a∈Fq

(f1))(a) = (f1(a))qαi. Thus, for a ∈ Fq, we have

Note that for 1 ≤ i ≤ r, and each a ∈ Fq, we have fi(a) = (σα

i

r

r

iqαi(f1(a)) = χm(f1(a)). Using this observation, Theorem 3.2 implies the following corollary immediately.

χt

χt

(fi(a)) =

i

i=1

i=1

Corollary 3.5. Let f1, f2, . . ., fk be monic polynomials in Fqn[T], no two of which share roots that are Galois conjugates over Fq. Let m be the degree of the largest squarefree divisor of ki=1 fi. Let χ1, χ2, . . ., χk be multiplicative characters of Fqn. Assume that there exists 1 ≤ i ≤ k such that fi has a root ξi of total multiplicity mi such that χm

i is not identically 1 on the set NF

(Fq[ξi])\ {0}. Then

i

qn[ξi]/Fqn

k

χi fi(a) ≤ (mn − 1)√q.

![image 56](<2024-martin-distribution-power-residues-shifted_images/imageFile56.png>)

i=1

a∈Fq

4. NEW CONSTRUCTIONS OF MAXIMAL CLIQUES IN GENERALIZED PALEY GRAPHS

To construct maximal cliques in GP(qd, d), we are led to consider the local behavior of the graph GP(qd, d) in a subﬁeld, equivalently, the structure of the subgraph induced by a subﬁeld.

- Lemma 4.1. Let d ≥ 2 and let q ≡ 1 (mod d) be an odd prime power. Let d′ be a divisor of d


that is greater than 1. Then the subgraph of GP(qd, d) induced by the subﬁeld Fqd′ is the same as GP(qd′, d′).

′−1) is a primitive root of Fqd′; moreover, since q ≡ 1 (mod d), it follows that

Proof. Let g be a primitive root of Fqd. Then g(qd−1)/(qd

d/d′−1

qd − 1 qd′ − 1

d d′

′j ≡

qd

=

(mod d).

![image 57](<2024-martin-distribution-power-residues-shifted_images/imageFile57.png>)

![image 58](<2024-martin-distribution-power-residues-shifted_images/imageFile58.png>)

j=0

d−1

Thus, gcd(d, q

qd′−1) = dd

d′. Then x is a d-th power in Fqd if and only if x is a d′-th power in Fqd′. The conclusion follows.

. Let x ∈ F∗q

![image 59](<2024-martin-distribution-power-residues-shifted_images/imageFile59.png>)

![image 60](<2024-martin-distribution-power-residues-shifted_images/imageFile60.png>)

′

As preparation for proving Theorem 1.4, in the next proposition, we establish the existence of cliques of small size with prescribed degrees.

Proposition 4.2. Let d ≥ 2 and let q ≡ 1 (mod d) be an odd prime power. Let r be the smallest prime divisor of d. Let d1, d2, . . ., dk be positive integers such that d1 > 1 and d1 | d2 | · · · | dk | d. Assume that

qr > max{(d + (k − 1)rk−1)2, e2(k−1)}. Then there is a clique C = {v1, v2, . . ., vk} in GP(qd, d) such that vi has degree di over Fq for

- each 1 ≤ i ≤ k, and no two vertices in C are Galois conjugates with respect to the ﬁeld extension Fqd/Fq.


Proof. We build such a clique inductively. We ﬁrst pick an arbitrary v1 ∈ Fqd1

such that v1 has degree d1 over Fq.

Given 2 ≤ j ≤ k, suppose we have constructed a clique Cj−1 = {v1, v2, . . ., vj−1} in GP(qd, d) such that vi has degree di over Fq for each 1 ≤ i ≤ j − 1, and no two vertices in Cj−1 are Galois conjugates with respect to the ﬁeld extension Fqd/Fq. We need to ﬁnd vj ∈ Fqdj

with degree dj, not a Galois conjugate of any of v1, v2, . . ., vj−1, such that Cj−1 ∪ {vj} forms a clique in GP(qd, d).

Note that v1, v2, . . ., vj−1, vj ∈ Fqdj

. Thus, by Lemma 4.1, Cj−1 ∪ {vj} forms a clique in GP(qd, d) if and only if Cj−1 ∪ {vj} forms a clique in GP(qd

, dj), or equivalently, if and only if (vj − vi)(q

j

dj−1)/dj = 1 for each 1 ≤ i ≤ j − 1. By Lemma 1.1, the number of such vj is at

/djj−1 − (j − 1) qdj. On the other hand, note that the number of elements in Fqdj

![image 61](<2024-martin-distribution-power-residues-shifted_images/imageFile61.png>)

least qd

that are Galois conjugates of one of v1, v2, . . ., vj−1 is at most (j − 1)dj. Therefore, if

j

qd

j

![image 62](<2024-martin-distribution-power-residues-shifted_images/imageFile62.png>)

> (j − 1) qdj + (j − 1)dj (5) holds, then we can ﬁnd a desired vj and achieve our goal.

![image 63](<2024-martin-distribution-power-residues-shifted_images/imageFile63.png>)

djj−1

It remains to show that the given assumption qr > max{(d+(k −1)rk−1)2, e2(k−1)} implies the inequality (5) for each 2 ≤ j ≤ k. Consider the function s(t) = tlog q − 2(k − 1) log t, where t ≥ r is a real number. Since qr > e2(k−1), it follows that s′(t) = log q − 2(k − 1)/t > 0 when

- t ≥ r. Therefore, s(t) ≥ s(r) when t ≥ r, or equivalently √qt/tk−1 ≥


√qr/rk−1 when t ≥ r. Therefore, given qr > (d + (k − 1)rk−1)2 where r is the smallest prime divisor of d, we have for

![image 64](<2024-martin-distribution-power-residues-shifted_images/imageFile64.png>)

![image 65](<2024-martin-distribution-power-residues-shifted_images/imageFile65.png>)

- each 2 ≤ j ≤ k that


qd

qd

j

j

![image 66](<2024-martin-distribution-power-residues-shifted_images/imageFile66.png>)

![image 67](<2024-martin-distribution-power-residues-shifted_images/imageFile67.png>)

djj−1 − (j − 1) qdj

djk−1 − (k − 1) qdj

− (j − 1)dj ≥

− (k − 1)d

![image 68](<2024-martin-distribution-power-residues-shifted_images/imageFile68.png>)

![image 69](<2024-martin-distribution-power-residues-shifted_images/imageFile69.png>)

![image 70](<2024-martin-distribution-power-residues-shifted_images/imageFile70.png>)

qdj

![image 71](<2024-martin-distribution-power-residues-shifted_images/imageFile71.png>)

= (k − 1) qdj

(k − 1)djk−1 − 1 − (k − 1)d ≥ (k − 1)√qr

![image 72](<2024-martin-distribution-power-residues-shifted_images/imageFile72.png>)

√qr

![image 73](<2024-martin-distribution-power-residues-shifted_images/imageFile73.png>)

![image 74](<2024-martin-distribution-power-residues-shifted_images/imageFile74.png>)

(k − 1)rk−1 − 1 − (k − 1)d > (k − 1)2rk−1

![image 75](<2024-martin-distribution-power-residues-shifted_images/imageFile75.png>)

d

(k − 1)rk−1 − (k − 1)d = 0, as required.

![image 76](<2024-martin-distribution-power-residues-shifted_images/imageFile76.png>)

After one ﬁnal elementary lemma, we will be ready to prove Theorem 1.4.

Lemma 4.3. Let m, d ≥ 2 be positive integers with rad(m) | rad(d), and let r be the smallest prime divisor of m. Then there exist positive integers k and d1, d2, . . ., dk ≥ r such that d1d2 · · ·dk = m and d1 | d2 | · · · | dk | d.

Proof. If we let k be the largest exponent of any prime in the prime factorization of m, it is easy to check that the integers di = pk+1−i|m p have the asserted properties.

- Proof of Theorem 1.4. Note that the assumption q ≡ 1 (mod d) guarantees that Fq forms a clique in GP(qd, d). If m = 1, the subﬁeld Fq forms a maximal clique in GP(qd, d) [23, Theorem 1.2] as mentioned in the introduction. Thus we may assume that m ≥ 2 in the following.


Since rad(m) | rad(d), Lemma 4.3 enables us to choose positive integers d1, d2, . . ., dk ≥ r so

that m = d1d2 · · ·dk and d1 | d2 | · · · | dk | d. Note that m ≥ rk and thus k ≤ logr m. It follows that

q > (8 logr m + 4)d2m2 ≥ (8k + 4)d2m2 ≥ (8k + 4)d2r2k > max{d + (k − 1)rk−1, ek−1}. To see the last inequality, note that (8k + 4)d2r2k > d + (k − 1)r2k > d + (k − 1)rk−1 and

- r2k ≥ 4k > ek−1. By Proposition 4.2, there exists a clique D = {v1, v2, . . ., vk} in GP(qd, d) such that vi has degree di over Fq for each 1 ≤ i ≤ k, and no two vertices in D are Galois conjugates with respect to the ﬁeld extension Fqd/Fq.


Recall that Fq is a clique. Observe that C = D ∪ D′ also forms a clique in GP(qd, d), where D′ = {x ∈ Fq : vi − x is a d-th power in Fqd for all 1 ≤ i ≤ k}.

Since m = d1d2 · · ·dk and ki=1 di ≤ kd, it follows from Theorem 1.2 that q m − kd√q ≤ |D′| ≤

q m

+ kd√q. (6)

![image 77](<2024-martin-distribution-power-residues-shifted_images/imageFile77.png>)

![image 78](<2024-martin-distribution-power-residues-shifted_images/imageFile78.png>)

![image 79](<2024-martin-distribution-power-residues-shifted_images/imageFile79.png>)

![image 80](<2024-martin-distribution-power-residues-shifted_images/imageFile80.png>)

By deﬁnition, C cannot be expanded to a larger clique by adding another vertex in Fq. Assume that there exists v ∈ Fqd \ Fq such that v is not a Galois conjugate of vi with respect to the ﬁeld extension Fqd/Fq for any 1 ≤ i ≤ k, and yet C ∪ {v} is still a clique. It would then follow that

D′ = D′ ∩ {x ∈ Fq : v − x is a d-th power in Fqd}. Theorem 1.2 then implies that

q mr

+ (k + 1)d√q. (7) Comparing inequality (7) with the lower bound on |D′| in inequality (6), we obtain

|D′| ≤

![image 81](<2024-martin-distribution-power-residues-shifted_images/imageFile81.png>)

![image 82](<2024-martin-distribution-power-residues-shifted_images/imageFile82.png>)

q m − kd√q ≤

+ (k + 1)d√q, which implies that

q mr

![image 83](<2024-martin-distribution-power-residues-shifted_images/imageFile83.png>)

![image 84](<2024-martin-distribution-power-residues-shifted_images/imageFile84.png>)

![image 85](<2024-martin-distribution-power-residues-shifted_images/imageFile85.png>)

![image 86](<2024-martin-distribution-power-residues-shifted_images/imageFile86.png>)

(2k + 1)d2m2

(1 − 1r)2 ≤ (8k + 4)d2m2 ≤ (8 logr m + 4)d2m2, violating the assumption that q > (8 logr m + 4)d2m2.

q ≤

![image 87](<2024-martin-distribution-power-residues-shifted_images/imageFile87.png>)

![image 88](<2024-martin-distribution-power-residues-shifted_images/imageFile88.png>)

Let C′ be a maximal clique in GP(qd, d) such that C ⊂ C′. Based on the above discussions, each element in C′ \C is a Galois conjugate of vi for some 1 ≤ i ≤ k. It follows that |C| ≤ |C′| ≤ |C| + k(d − 1), and thus inequality (6) implies that

q m − d logr m ·

+ d logr m · (√q + 1), as required.

√q ≤

q m − kd√q + k ≤ |C′| ≤

+ kd√q + kd ≤

q m

q m

![image 89](<2024-martin-distribution-power-residues-shifted_images/imageFile89.png>)

![image 90](<2024-martin-distribution-power-residues-shifted_images/imageFile90.png>)

![image 91](<2024-martin-distribution-power-residues-shifted_images/imageFile91.png>)

![image 92](<2024-martin-distribution-power-residues-shifted_images/imageFile92.png>)

![image 93](<2024-martin-distribution-power-residues-shifted_images/imageFile93.png>)

![image 94](<2024-martin-distribution-power-residues-shifted_images/imageFile94.png>)

![image 95](<2024-martin-distribution-power-residues-shifted_images/imageFile95.png>)

![image 96](<2024-martin-distribution-power-residues-shifted_images/imageFile96.png>)

5. MAXIMALITY OF THE (Fq, α)-CONSTRUCTION

In this section, we prove Theorem 1.5 and Theorem 1.6. We start by presenting the proof of Theorem 1.5.

- Proof of Theorem 1.5. Recall that for each vertex u ∈ Fq2, N(u) is the Fq-neighborhood of u in the d-Paley graph GP(q2, d), that is,


N(u) = {x ∈ Fq : u − x is a d-th power in Fq2}.

By [10, Proposition 4.6], |N(u)| = q+1d −1 if u ∈ Fq2 \Fq. Since d | (q+1), the subﬁeld Fq forms a clique. Since q > 10d4/(d − 1)2 > 10d2, we have

![image 97](<2024-martin-distribution-power-residues-shifted_images/imageFile97.png>)

6 √q

1 q

6 √10d

1 40

9 +

< 10. It follows that

+

< 9 +

+

![image 98](<2024-martin-distribution-power-residues-shifted_images/imageFile98.png>)

![image 99](<2024-martin-distribution-power-residues-shifted_images/imageFile99.png>)

![image 100](<2024-martin-distribution-power-residues-shifted_images/imageFile100.png>)

![image 101](<2024-martin-distribution-power-residues-shifted_images/imageFile101.png>)

![image 102](<2024-martin-distribution-power-residues-shifted_images/imageFile102.png>)

![image 103](<2024-martin-distribution-power-residues-shifted_images/imageFile103.png>)

2

1 d2

1 d −

(3√q + 1)2 = 9q + 6√q + 1 < 10q < q2

, and thus

![image 104](<2024-martin-distribution-power-residues-shifted_images/imageFile104.png>)

![image 105](<2024-martin-distribution-power-residues-shifted_images/imageFile105.png>)

![image 106](<2024-martin-distribution-power-residues-shifted_images/imageFile106.png>)

![image 107](<2024-martin-distribution-power-residues-shifted_images/imageFile107.png>)

+ 3√q <

q + 1 d − 1. (8)

q d2

![image 108](<2024-martin-distribution-power-residues-shifted_images/imageFile108.png>)

![image 109](<2024-martin-distribution-power-residues-shifted_images/imageFile109.png>)

![image 110](<2024-martin-distribution-power-residues-shifted_images/imageFile110.png>)

Let u ∈ Fq2 \ Fq. Then u and uq are Galois conjugates. Note that N(u) = N(uq). Indeed, if x ∈ Fq, then uq−x = uq−xq = (u−x)q is a d-th power in Fq2 if and only if u−x is a d-th power in

Fq2. We also claim that that u and uq are adjacent if and only if d | q+12 . Let β ∈ F∗q be a non-square in Fq, and let α ∈ Fq2 such that α2 = β. Then {1, α} forms a basis of Fq2 over Fq, and thus we can write u = x + yα for some x, y ∈ Fq with y = 0. Since uq = (x + yα)q = xq + yqαq = x − yα, we have u −uq = 2yα being a d-th power in Fq2 if and only if α is a d-th power in Fq2, if and only if d | q+12 . Thus, N(u) ∪ {u, uq} is a clique when d | q+12 , and N(u) ∪ {u, uq} is not a clique when d ∤ q+12 .

![image 111](<2024-martin-distribution-power-residues-shifted_images/imageFile111.png>)

![image 112](<2024-martin-distribution-power-residues-shifted_images/imageFile112.png>)

![image 113](<2024-martin-distribution-power-residues-shifted_images/imageFile113.png>)

![image 114](<2024-martin-distribution-power-residues-shifted_images/imageFile114.png>)

Let Cu = N(u)∪{u} when d ∤ q+12 , and Cu = N(u)∪{u, uq} when d | q+12 . Suppose that Cu is not a maximal clique. Then based on the above discussion, there is v ∈ Fq2 \ Fq such that v = uq, and N(u) ∪ {u, v} remains to be a clique. It follows that N(u) ∩ N(v) = N(u). By Theorem 1.3 and inequality (8), we have

![image 115](<2024-martin-distribution-power-residues-shifted_images/imageFile115.png>)

![image 116](<2024-martin-distribution-power-residues-shifted_images/imageFile116.png>)

q d2

+ 3√q <

q + 1

|N(u) ∩ N(v)| ≤

d − 1 = |N(u)|, a contradiction. We conclude that the desired clique Cu is maximal.

![image 117](<2024-martin-distribution-power-residues-shifted_images/imageFile117.png>)

![image 118](<2024-martin-distribution-power-residues-shifted_images/imageFile118.png>)

![image 119](<2024-martin-distribution-power-residues-shifted_images/imageFile119.png>)

Finally, we use a similar approach to show the maximality of cliques from (Fq, α)-constructions in Peisert graphs.

- Proof of Theorem 1.6. When 7 ≤ q ≤ 79, we have used SageMath to verify the statement of the theorem. In the following discussion, we assume that q ≥ 83.


Let g be a primitive root of Fq2 and let H be the subgroup of F∗q2 of index 4. Let S = H ∪ gH. Note that two vertices are adjacent in the Peisert graph Pq∗2 if and only if their difference is in S. Also, note that the 4-Paley graph GP(q2, 4) is a subgraph of the Peisert graph Pq∗2. Since 4 | (q+1), the subﬁeld Fq forms a clique in GP(q2, 4), and thus in Pq∗2. For each vertex u ∈ Fq2, let N(u) be the Fq-neighborhood of u in Pq∗2, that is,

N(u) = {x ∈ Fq : u−x ∈ S} = {x ∈ Fq : u−x ∈ H}∪{x ∈ Fq : u−x ∈ gH} := N1(u)∪N2(u). Note that N1(u) is exactly the Fq-neighborhood of u in GP(q2, 4), and thus |N1(u)| = q+14 − 1 if

![image 120](<2024-martin-distribution-power-residues-shifted_images/imageFile120.png>)

2−1

2−5

2−1

- u ∈/ Fq. On the other hand, it is known that Peisert graph Pq∗2 is a (q2, q


2 , q

4 , q

4 )-strongly regular graph with the smallest eigenvalue −12−q [14]. Thus, the subﬁeld Fq forms a maximum clique in Pq∗2 and |N(u)| = q+12 − 1 for each u ∈ Fq2 \ Fq by the Hoffman bound [4, Proposition 1.3.2].

![image 121](<2024-martin-distribution-power-residues-shifted_images/imageFile121.png>)

![image 122](<2024-martin-distribution-power-residues-shifted_images/imageFile122.png>)

![image 123](<2024-martin-distribution-power-residues-shifted_images/imageFile123.png>)

![image 124](<2024-martin-distribution-power-residues-shifted_images/imageFile124.png>)

![image 125](<2024-martin-distribution-power-residues-shifted_images/imageFile125.png>)

Let u ∈ Fq2 \ Fq. For the sake of contradiction, assume that N(u) ∪ {u} is not a maximal clique. Then u and uq are Galois conjugates. We claim that N(u) = N(uq). If x ∈ Fq, then uq − x = (u − x)q, thus u − x ∈ H if and only if uq − x ∈ H, and uq − x ∈ g3H if and only

if u − x ∈ gH. Thus, if N(u) = N(uq), then we must have N(u) = N1(u), which is impossible since |N(u)| > |N1(u)|. Since N(u) ∪ {u} is not maximal, there is v ∈ Fq2 \ Fq such that v = uq, and N(u) ∩ N(v) = N(u).

Next we estimate |N(u) ∩ N(v)| using Theorem 3.2. As a preparation, we need to express the

indicator function on S using characters. Let χ be the multiplicative character of Fq2 with order 4 such that χ(g) = i. It follows that

χ(x) + 1 χ(x) + i 2 =

8, if x ∈ H ∪ gH, 0, if x ∈ g2H ∪ g3H.

On the other hand, for x ∈ Fq2, we have χ(x) + 1 χ(x) + i 2 = 2 + χ(x) + χ(x) 2 + iχ(x) − iχ(x)

![image 126](<2024-martin-distribution-power-residues-shifted_images/imageFile126.png>)

![image 127](<2024-martin-distribution-power-residues-shifted_images/imageFile127.png>)

= 4 + (2i + 2)χ(x) + (2 − 2i)χ(x) + i(χ2(x) − χ2(x))

![image 128](<2024-martin-distribution-power-residues-shifted_images/imageFile128.png>)

![image 129](<2024-martin-distribution-power-residues-shifted_images/imageFile129.png>)

= 4 + (2i + 2)χ(x) + (2 − 2i)χ(x). Therefore, 1S : F∗q2 → C, the indicator function of S, can be expressed as

![image 130](<2024-martin-distribution-power-residues-shifted_images/imageFile130.png>)

4 · 1S = 2 + (i + 1)χ + (1 − i)χ. It follows that

![image 131](<2024-martin-distribution-power-residues-shifted_images/imageFile131.png>)

16|N(u) ∩ N(v)|

4 · 1S(u − a) · 4 · 1S(v − a)

=

a∈Fq

=

a∈Fq

2 + (1 + i)χ(u − a) + (1 − i)χ(u − a) 2 + (1 + i)χ(v − a) + (1 − i)χ(v − a)

![image 132](<2024-martin-distribution-power-residues-shifted_images/imageFile132.png>)

![image 133](<2024-martin-distribution-power-residues-shifted_images/imageFile133.png>)

= 4q + 2(1 + i)

a∈Fq

χ(v − a) + 2(1 − i)

![image 134](<2024-martin-distribution-power-residues-shifted_images/imageFile134.png>)

a∈Fq

χ(v − a)

+ 2(1 + i)

a∈Fq

χ(u − a) + 2i

![image 135](<2024-martin-distribution-power-residues-shifted_images/imageFile135.png>)

a∈Fq

χ(u − a)χ(v − a) + 2

![image 136](<2024-martin-distribution-power-residues-shifted_images/imageFile136.png>)

![image 137](<2024-martin-distribution-power-residues-shifted_images/imageFile137.png>)

a∈Fq

χ(u − a)χ(v − a)

![image 138](<2024-martin-distribution-power-residues-shifted_images/imageFile138.png>)

χ(u − a) + 2

+ 2(1 − i)

a∈Fq

a∈Fq

χ(u − a)χ(v − a) − 2i

![image 139](<2024-martin-distribution-power-residues-shifted_images/imageFile139.png>)

a∈Fq

χ(u − a)χ(v − a).

Since u, v ∈ Fq2 \ Fq are not Galois conjugates, we may apply Theorem 3.2 to bound these eight character sums: the four sums with one character value can be bounded by √q, while the four sums

![image 140](<2024-martin-distribution-power-residues-shifted_images/imageFile140.png>)

with two character values can be bounded by 3√q. Since |2(1 ± i)| = 2√2, we obtain 16|N(u) ∩ N(v)| ≤ 4q + 4(2

![image 141](<2024-martin-distribution-power-residues-shifted_images/imageFile141.png>)

![image 142](<2024-martin-distribution-power-residues-shifted_images/imageFile142.png>)

√

√

2 + 24)√q. Since q ≥ 83, we conclude that

√q) + 4(2 · 3√q) = 4q + (8

![image 143](<2024-martin-distribution-power-residues-shifted_images/imageFile143.png>)

![image 144](<2024-martin-distribution-power-residues-shifted_images/imageFile144.png>)

2 ·

![image 145](<2024-martin-distribution-power-residues-shifted_images/imageFile145.png>)

![image 146](<2024-martin-distribution-power-residues-shifted_images/imageFile146.png>)

![image 147](<2024-martin-distribution-power-residues-shifted_images/imageFile147.png>)

√2 + 3 2

![image 148](<2024-martin-distribution-power-residues-shifted_images/imageFile148.png>)

q 4

√q <

q − 1 2

|N(u) ∩ N(v)| ≤

= |N(u)|, a contradiction. Hence, N(u) ∪ {u} is a maximal clique.

+

![image 149](<2024-martin-distribution-power-residues-shifted_images/imageFile149.png>)

![image 150](<2024-martin-distribution-power-residues-shifted_images/imageFile150.png>)

![image 151](<2024-martin-distribution-power-residues-shifted_images/imageFile151.png>)

![image 152](<2024-martin-distribution-power-residues-shifted_images/imageFile152.png>)

6. REMARKS AND OPEN QUESTIONS We conclude this paper with some remarks and open questions.

- Remark 6.1. Peisert [14, Section 6] showed that the Paley graph Pq2 and the Peisert graph Pq∗2 of


the same order are not isomorphic when q ≥ 7 by showing that Aut(Pq2) = Aut(Pq∗2). While the fact that these two graphs are not isomorphic seems obvious (at least when q is sufﬁciently large),

to the best knowledge of the authors, there is no known simple proof. Peisert’s original proof relies on heavy machinery from group theory.

Here we sketch a new proof that Pq2 and Pq∗2 are not isomorphic when q ≡ 3 (mod 4) and q ≥ 7, using the structure of maximal cliques from (Fq, α)-constructions. Suppose otherwise that these two graphs are isomorphic. Then there is a graph isomorphism φ: Pq∗2 → Pq2 that maps the

subﬁeld Fq to Fq. Indeed, any graph isomorphism must map Fq, a maximum clique in Pq∗2, to some maximum clique in Pq2; while any maximum clique in Pq2 can be mapped to a maximum clique containing 0 and 1 via an automorphism of Pq2. But it is known [3] that the only maximum clique in Pq2 that contains 0 and 1 is Fq itself.

Choose any α∗ ∈ Fq2 \ Fq, and let C∗ be the clique in Pq∗2 containing α∗ and its neighbors in Fq. Note that C∗ is maximal in Pq∗2 by Theorem 1.6. Similarly, set α = φ(α∗) and let C be the clique in Pq2 containing α and its neighbors in Fq. However, C = φ(C∗) is not maximal in Pq2 since C ∪ {αq} is a maximal clique (as mentioned in the introduction), which contradicts the existence of the graph isomorphism φ.

- Remark 6.2. By combining the ideas in the proofs of Theorems 1.4 and Theorem 1.5, we can show the following: if d ≥ 2 is ﬁxed and k is a non-negative integer, then there is a maximal clique of size approximately q/dk in GP(q2, d), provided that q ≡ −1 (mod d) is sufﬁciently large. We can also prove the following by modifying the proof of Theorem 1.6: if k is a non-negative integer,

then there is a maximal clique of size approximately q/2k in Pq∗2, provided that q ≡ 3 (mod 4) is sufﬁciently large.

- Remark 6.3. Theorem 1.4 says that (for suitable values of d, q, and m) there are maximal cliques


in GP(qd, d) that are approximately m1 as large as the clique Fq itself, which is believed to be a maximum clique (essentially the only one, see [22] for a related discussion). These cliques have

![image 153](<2024-martin-distribution-power-residues-shifted_images/imageFile153.png>)

a speciﬁc structure, where we choose a small number of points outside of Fq and then add their common neighbors within Fq. We believe that this construction yields all large maximal cliques in GP(qd, d) up to automorphisms of the graph and certain induced subgraphs, and we formulate a conjecture intended to serve as a sort of converse to Theorem 1.4.

Conjecture 6.4. Fix an integer d ≥ 2. Consider all sequences {rq/q}, indexed by odd prime powers q ≡ 1 (mod d), such that rq is the cardinality of some maximal clique in the d-Paley graph GP(qd, d). Then the set of limit points of all such sequences equals {0} ∪ {m1 : rad(m) | rad(d)}. Theorem 1.4 implies that every element of {0} ∪ {m1 : rad(m) | rad(d)} is such a limit point; we conjecture that there are no others.

![image 154](<2024-martin-distribution-power-residues-shifted_images/imageFile154.png>)

![image 155](<2024-martin-distribution-power-residues-shifted_images/imageFile155.png>)

As an example, consider all sequences {rq/q} indexed by odd prime powers q such that rq is the cardinality of some maximal clique in the Paley graph GP(q2, 2). Theorem 1.4 implies that every element of the set L2 = {0} ∪ {1, 21, 41, 81, . . .} is a limit point of some such sequence, and we conjecture that every limit point of any such sequence is in L2.

![image 156](<2024-martin-distribution-power-residues-shifted_images/imageFile156.png>)

![image 157](<2024-martin-distribution-power-residues-shifted_images/imageFile157.png>)

![image 158](<2024-martin-distribution-power-residues-shifted_images/imageFile158.png>)

Baker, Ebert, Hemmeter, and Woldar [2] (see also [8, 9]) conjectured that the (Fq, α)-construction gives a second largest maximal clique in the Paley graph GP(q2, 2); equivalently, there is no maximal clique of size between q+2δq + 1 and q − 1, where δq = 1 if q ≡ 1 (mod 4) and δq = 3 if q ≡ 3 (mod 4). To the best of our knowledge, no progress has been made towards their conjecture. A consequence of their conjecture would be that there are no limit points of any sequence {rq/q} in the interval (21, 1). Our conjecture can thus be viewed as a further extension of their conjecture. It is likely that new insights towards this conjecture would also shed light on estimating the clique number of Paley graphs of non-square order, a major open problem in additive combinatorics and analytic number theory [6]. We refer to [22] and the references therein for recent progress towards the latter problem.

![image 159](<2024-martin-distribution-power-residues-shifted_images/imageFile159.png>)

![image 160](<2024-martin-distribution-power-residues-shifted_images/imageFile160.png>)

We similarly conjecture the analogous converses of the two statements in Remark 6.2: the analogous set of limit points for GP(q2, d) should be exactly Ld = {0} ∪ {1, d1, d1

, . . .}, while the analogous set of limit points for Pq∗2 should be exactly L2.

![image 161](<2024-martin-distribution-power-residues-shifted_images/imageFile161.png>)

![image 162](<2024-martin-distribution-power-residues-shifted_images/imageFile162.png>)

2

ACKNOWLEDGMENTS

The authors thank the anonymous referees for their valuable comments and suggestions. The authors thank Daqing Wan for the clariﬁcation of a result in [20] and Sergey Goryainov for sharing the conjecture related to Peisert graphs. The authors also thank Shamil Asgarli for helpful comments on a preliminary version of the manuscript. The ﬁrst author was supported in part by a Natural Sciences and Engineering Council of Canada Discovery Grant. The research of the second author was supported in part by an NSERC fellowship.

REFERENCES

- [1] S. Asgarli and C. H. Yip. Van Lint–MacWilliams’ conjecture and maximum cliques in Cayley graphs over ﬁnite ﬁelds. J. Combin. Theory Ser. A, 192:Paper No. 105667, 23, 2022.
- [2] R. D. Baker, G. L. Ebert, J. Hemmeter, and A. Woldar. Maximal cliques in the Paley graph of square order. J. Statist. Plann. Inference, 56(1):33–38, 1996.
- [3] A. Blokhuis. On subsets of GF(q2) with square differences. Nederl. Akad. Wetensch. Indag. Math., 46(4):369– 372, 1984.
- [4] A. E. Brouwer, A. M. Cohen, and A. Neumaier. Distance-regular graphs, volume 18 of Ergebnisse der Mathematik und ihrer Grenzgebiete (3) [Results in Mathematics and Related Areas (3)]. Springer-Verlag, Berlin, 1989.
- [5] S. D. Cohen. Clique numbers of Paley graphs. Quaestiones Math., 11(2):225–231, 1988.
- [6] E. S. Croot, III and V. F. Lev. Open problems in additive combinatorics. In Additive combinatorics, volume 43 of CRM Proc. Lecture Notes, pages 207–233. Amer. Math. Soc., Providence, RI, 2007.
- [7] C. Godsil and K. Meagher. Erdos-Ko-Rado˝ theorems: algebraic approaches, volume 149 of Cambridge Studies in Advanced Mathematics. Cambridge University Press, Cambridge, 2016.
- [8] S. Goryainov, V. V. Kabanov, L. Shalaginov, and A. Valyuzhenich. On eigenfunctions and maximal cliques of Paley graphs of square order. Finite Fields Appl., 52:361–369, 2018.
- [9] S. Goryainov, A. Masley, and L. Shalaginov. On a correspondence between maximal cliques in Paley graphs of square order. Discrete Math., 345(6):Paper No. 112853, 10, 2022.
- [10] S. Goryainov, L. Shalaginov, and C. H. Yip. On eigenfunctions and maximal cliques of generalised Paley graphs of square order. Finite Fields Appl., 87:Paper No. 102150, 2023.
- [11] J. W. P. Hirschfeld and T. Szo˝nyi. Constructions of large arcs and blocking sets in ﬁnite planes. European J. Combin., 12(6):499–511, 1991.
- [12] J. W. P. Hirschfeld and T. Szo˝nyi. A problem on squares in a ﬁnite ﬁeld and its application to geometry. In Advances in ﬁnite geometries and designs (Chelwood Gate, 1990), Oxford Sci. Publ., pages 169–176. Oxford Univ. Press, New York, 1991.
- [13] R. Lidl and H. Niederreiter. Finite ﬁelds, volume 20 of Encyclopedia of Mathematics and its Applications. Cambridge University Press, Cambridge, second edition, 1997.
- [14] W. Peisert. All self-complementary symmetric graphs. J. Algebra, 240(1):209–229, 2001.
- [15] M. Rosen. Number theory in function ﬁelds, volume 210 of Graduate Texts in Mathematics. Springer-Verlag, New York, 2002.
- [16] T. Szo˝nyi. Note on the existence of large minimal blocking sets in Galois planes. Combinatorica, 12(2):227–235, 1992.
- [17] T. Szo˝nyi. Some applications of algebraic curves in ﬁnite geometry and combinatorics. In Surveys in combinatorics, 1997 (London), volume 241 of London Math. Soc. Lecture Note Ser., pages 197–236. Cambridge Univ. Press, Cambridge, 1997.
- [18] P. Sziklai. On subsets of GF(q2) with dth power differences. Discrete Math., 208/209:547–555, 1999.
- [19] P. Sziklai. A lemma on the randomness of d-th powers in GF(q), d | q − 1. Bull. Belg. Math. Soc. Simon Stevin, 8(1):95–98, 2001.
- [20] D. Wan. Generators and irreducible polynomials over ﬁnite ﬁelds. Math. Comp., 66(219):1195–1212, 1997.
- [21] C. H. Yip. On maximal cliques of Cayley graphs over ﬁelds. J. Algebraic Combin., 56(2):323–333, 2022.
- [22] C. H. Yip. Exact values and improved bounds on the clique number of cyclotomic graphs, 2023. arXiv:2304.13213.


- [23] C. H. Yip. Maximality of subﬁelds as cliques in Cayley graphs over ﬁnite ﬁelds. Algebr. Comb., 6(4):901–905, 2023.
- [24] C. H. Yip. Erdo˝s–Ko–Rado theorem in Peisert-type graphs. Canad. Math. Bull., 67(1):176–187, 2024.


DEPARTMENT OF MATHEMATICS, UNIVERSITY OF BRITISH COLUMBIA, VANCOUVER V6T 1Z2, CANADA Email address: gerg@math.ubc.ca

SCHOOL OF MATHEMATICS, GEORGIA INSTITUTE OF TECHNOLOGY, GA 30332, UNITED STATES Email address: cyip30@gatech.edu

