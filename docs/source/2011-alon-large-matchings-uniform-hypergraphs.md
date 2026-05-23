---
type: source
kind: paper
title: Large matchings in uniform hypergraphs and the conjectures of Erdos and Samuels
authors: Noga Alon, Peter Frankl, Hao Huang, Vojtech Rodl, Andrzej Rucinski, Benny Sudakov
year: 2011
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/1107.1219v2
source_local: ../raw/2011-alon-large-matchings-uniform-hypergraphs.pdf
topic: general-knowledge
cites:
---

arXiv:1107.1219v2[math.CO]31Jan2012

Large matchings in uniform hypergraphs and the conjectures of Erd˝os and Samuels

Noga Alon ∗ Peter Frankl † Hao Huang ‡ Vojtech Ro¨dl § Andrzej Ruci´nski ¶ Benny Sudakov

Abstract

In this paper we study degree conditions which guarantee the existence of perfect matchings and perfect fractional matchings in uniform hypergraphs. We reduce this problem to an old conjecture by Erdo˝s on estimating the maximum number of edges in a hypergraph when the (fractional) matching number is given, which we are able to solve in some special cases using probabilistic techniques. Based on these results, we obtain some general theorems on the minimum d-degree ensuring the existence of perfect (fractional) matchings. In particular, we asymptotically determine the minimum vertex degree which guarantees a perfect matching in 4-uniform and 5-uniform hypergraphs. We also discuss an application to a problem of ﬁnding an optimal data allocation in a distributed storage system.

# 1 Introduction

A k-uniform hypergraph or a k-graph for short, is a pair H = (V,E), where V := V (H) is a ﬁnite set of vertices and E := E(H) ⊆ Vk is a family of k-element subsets of V called edges. Whenever convenient we will identify H with E(H). A matching in H is a set of disjoint edges of H. The number of edges in a matching is called the size of the matching. The size of the largest matching in a k-graph H is denoted by ν(H). A matching is perfect if its size equals |V |/k.

A fractional matching in a k-graph H = (V,E) is a function w : E → [0,1] such that for each v ∈ V we have e∋v w(e) ≤ 1. Then e∈E w(e) is the size of w. The size of the largest fractional

![image 1](<2011-alon-large-matchings-uniform-hypergraphs_images/imageFile1.png>)

∗Sackler School of Mathematics and Blavatnik School of Computer Science, Tel Aviv University, Tel Aviv 69978, Israel. Email: nogaa@tau.ac.il. Research supported in part by an ERC advanced grant, by a USA-Israeli BSF grant and by the Israeli I-Core program.

†Tokyo, Japan. Email: peter.frankl@gmail.com ‡Department of Mathematics, UCLA, Los Angeles, CA, 90095. Email: huanghao@math.ucla.edu. §Emory University, Atlanta, GA. Email: rodl@mathcs.emory.edu. Research supported by NSF grant DMS 080070. ¶A. Mickiewicz University, Poznan´, Poland. Email: rucinski@amu.edu.pl. Research supported by the National

Science Center grant N N201 604940, and the NSF grant DMS-1102086. Part of research performed at Emory University, Atlanta.

Department of Mathematics, UCLA, Los Angeles, CA 90095. Email: bsudakov@math.ucla.edu. Research supported in part by NSF grant DMS-1101185, NSF CAREER award DMS-0812005 and by USA-Israeli BSF grant.

matching in a k-graph H is denoted by ν∗(H). If ν∗(H) = n/k, or equivalently, for all v ∈ V we have e∋v w(e) = 1, then we call w perfect. The determination of ν∗(H) is a linear programming problem. Its dual problem is to ﬁnd a minimum fractional vertex cover τ∗(H) = v∈V w(v) over all functions w : V → [0,1] such that for each e ∈ E we have v∈e w(v) ≥ 1. Let τ(H) be the minimum number of vertices in a vertex cover of H. Then, for every k-graph H, by the Duality Theorem,

ν(H) ≤ ν∗(H) = τ∗(H) ≤ τ(H). (1)

Given a k-graph H and a set S ∈ Vd , 0 ≤ d ≤ k − 1, we denote by degH(S) the number of edges in H which contain S. Let δd := δd(H) be the minimum d-degree of H, which is the minimum

degH(S) over all S ∈ Vd . Note that δ0(H) = |E(H)|. In this paper we study the relation between the minimum d-degree δd(H) and the matching numbers ν(H) and ν∗(H).

Deﬁnition 1.1 Let integers d,k,s, and n satisfy 0 ≤ d ≤ k − 1, and 0 ≤ s ≤ n/k. We denote by msd(k,n) the minimum m so that for an n-vertex k-graph H, δd(H) ≥ m implies that ν(H) ≥ s. Equivalently,

msd(k,n) − 1 = max{δd(H) : |V (H)| = n and ν(H) ≤ s − 1}.

Furthermore, for a real number 0 ≤ s ≤ n/k, deﬁne fds(k,n) as the minimum m so that δd(H) ≥ m implies that ν∗(H) ≥ s. Equivalently,

fds(k,n) − 1 = max{δd(H) : |V (H)| = n and ν∗(H) < s}.

Observe that trivially, for ⌈s⌉ ≤ n/k,

fds(k,n) ≤ m⌈ds⌉(k,n). (2)

We are mostly interested in the case s = n/k (i.e. when matchings are perfect) in which we suppress the superscript in the notation mn/kd (k,n) and fdn/k(k,n). Thus, writing md(k,n), we implicitly require that n is divisible by k.

Problems of this type have a long history going back to Dirac [4] who in 1952 proved that minimum degree n/2 implies the existence of a Hamiltonian cycle in graphs. Therefore, for d ≥ 1, we refer to the extremal parameters md(k,n) and fd(k,n) as to Dirac-type thresholds. When k = 2, an easy argument shows that m1(2,n) = n/2. For k ≥ 3, an exact formula for mk−1(k,n) was obtained in [26]. For a ﬁxed k ≥ 3 and n → ∞ it yields the asymptotics mk−1(k,n) = n2 +O(1). As far as perfect fractional matchings are concerned, it was proved in [24] that fk−1(k,n) = ⌈n/k⌉ for k ≥ 2, which is a lot less than mk−1(k,n) when k ≥ 3. For more results on Dirac-type thresholds for matchings and Hamilton cycles see [23].

![image 2](<2011-alon-large-matchings-uniform-hypergraphs_images/imageFile2.png>)

In this paper, we focus on the asymptotic behavior of md(k,n) and fd(k,n) for general, but ﬁxed k and d, when n → ∞. For a lower bound on md(k,n) consider ﬁrst a k-graph H0 = H0(k,n)

(constructed in [26]) with vertex set split almost evenly, that is, V (H0) = A ∪ B, |A| − |B| ≤ 2, and with the edge set consisting of all k-element subsets of V (H0) intersecting A in an odd number of vertices. We choose the size of A so that |A| and nk have diﬀerent parity. Clearly, there is no perfect matching in H0 and for every 0 ≤ d ≤ k − 1 we have δd(H0) ∼ 12 nk−−dd .

![image 3](<2011-alon-large-matchings-uniform-hypergraphs_images/imageFile3.png>)

![image 4](<2011-alon-large-matchings-uniform-hypergraphs_images/imageFile4.png>)

Another lower bound on md(k,n) is given by the following well known construction. For integers n, k, and s, let H1(s) be a k-graph on n vertices consisting of all k-element subsets intersecting a given set of size s − 1, that is H1(s) = Kn(k) − Kn(k−)s+1. Observe that ν(H1(s)) = s − 1, while

δd(H1(n/k)) =

n − d k − d

−

n − d − n/k + 1 k − d

∼ 1 −

k − 1 k

![image 5](<2011-alon-large-matchings-uniform-hypergraphs_images/imageFile5.png>)

k−d n − d k − d

.

Assume that n is divisible by k. Putting s = nk and using the k-graphs H0 and H1(n/k), we obtain a lower bound

![image 6](<2011-alon-large-matchings-uniform-hypergraphs_images/imageFile6.png>)

md(k,n) ≥ max δd(H0),δd(H1(nk)) + 1 ∼ max

![image 7](<2011-alon-large-matchings-uniform-hypergraphs_images/imageFile7.png>)

- 1

![image 8](<2011-alon-large-matchings-uniform-hypergraphs_images/imageFile8.png>)

- 2


,1 −

k − 1 k

![image 9](<2011-alon-large-matchings-uniform-hypergraphs_images/imageFile9.png>)

k−d n − d k − d

. (3)

On the other hand, H1(⌈n/k⌉) alone yields a lower bound also on fd(k,n). Indeed, for a real s > 0 we have

ν∗(H1(⌈s⌉)) = τ∗(H1(⌈s⌉)) ≤ τ(H1(⌈s⌉)) = ⌈s⌉ − 1 < s, and so

fd(k,n) ≥ δd(H1(⌈nk⌉)) + 1 ∼ 1 −

![image 10](<2011-alon-large-matchings-uniform-hypergraphs_images/imageFile10.png>)

k − 1 k

![image 11](<2011-alon-large-matchings-uniform-hypergraphs_images/imageFile11.png>)

k−d n − d k − d

. (4)

It is easy to check that for d ≥ k/2 the maximum in the coeﬃcient in (3) equals 12. Pikhurko [22] proved, complementing the case d = k − 1, that indeed we have md(k,n) ∼ 21 nk−−dd also for k/2 ≤ d ≤ k − 2, k ≥ 4.

![image 12](<2011-alon-large-matchings-uniform-hypergraphs_images/imageFile12.png>)

![image 13](<2011-alon-large-matchings-uniform-hypergraphs_images/imageFile13.png>)

For d < k/2 the problem seems to be harder and we discuss below the cases d ≥ 1 and d = 0 separately. The ﬁrst result for the range 1 ≤ d < k/2, k ≥ 3, was obtained already in 1981 by Daykin and H¨aggkvist in [3] who proved that m1(k,n) ≤ k−k1 + o(1) nk−−11 . This was generalized to md(k,n) ≤ k−kd + o(1) nk−−dd for all 1 ≤ d < k/2 in [10], and, using the ideas from [10], slightly improved in [20] to md(k,n) ≤ k−kd − kk1−d + o(1) nk−−dd . For k = 4,d = 1 the latter coeﬃcient is 6447. In [20], the constant was further lowered to 4264, but there is still a gap between this upper bound and the lower bound of 3764. It has been conjectured in [15] and again in [10] that the lower bound (3) is achieved at least asymptotically.

![image 14](<2011-alon-large-matchings-uniform-hypergraphs_images/imageFile14.png>)

![image 15](<2011-alon-large-matchings-uniform-hypergraphs_images/imageFile15.png>)

![image 16](<2011-alon-large-matchings-uniform-hypergraphs_images/imageFile16.png>)

![image 17](<2011-alon-large-matchings-uniform-hypergraphs_images/imageFile17.png>)

![image 18](<2011-alon-large-matchings-uniform-hypergraphs_images/imageFile18.png>)

![image 19](<2011-alon-large-matchings-uniform-hypergraphs_images/imageFile19.png>)

![image 20](<2011-alon-large-matchings-uniform-hypergraphs_images/imageFile20.png>)

- Conjecture 1.1 For all 1 ≤ d ≤ k − 1,


md(k,n) ∼ max

- 1

![image 21](<2011-alon-large-matchings-uniform-hypergraphs_images/imageFile21.png>)

- 2


,1 −

k − 1 k

![image 22](<2011-alon-large-matchings-uniform-hypergraphs_images/imageFile22.png>)

k−d n − d k − d

.

H`an, Person, and Schacht in [10] proved Conjecture 1.1 in the case d = 1, k = 3 by showing that

- m1(3,n) is asymptotically equal to 59 n−21 . Ku¨hn, Osthus, and Treglown [16] and, independently, Khan [13], proved the exact result m1(3,n) = δ1(H1(n/3)) + 1. Recently Khan [14] announced that


![image 23](<2011-alon-large-matchings-uniform-hypergraphs_images/imageFile23.png>)

he veriﬁed the exact result m1(4,n) = δ1(H1(n/4)) + 1, while the asymptotic version, m1(4,n) ∼

n−1

37 64

3 follows also from a more general result by Lo and Markstr¨om [19].

![image 24](<2011-alon-large-matchings-uniform-hypergraphs_images/imageFile24.png>)

These exact results, together with (2) and (4), yield that f1(3,n) = m1(3,n) and f1(4,n) = m1(4,n). Remembering that, on the other hand, fk−1(k,n) is much smaller than mk−1(k,n), one can raise the question about a general relation between md(k,n) and its fractional counterpart fd(k,n). In this paper we answer this question by showing that md(k,n) and fd(k,n) are asymptotically equal whenever fd(k,n) ∼ c∗ nk−−dd for some constant c∗ > 21, and otherwise md(k,n) ∼ 12 nk−−dd .

![image 25](<2011-alon-large-matchings-uniform-hypergraphs_images/imageFile25.png>)

![image 26](<2011-alon-large-matchings-uniform-hypergraphs_images/imageFile26.png>)

- Theorem 1.1 For every 1 ≤ d ≤ k − 1 if there exists c∗ > 0 such that fd(k,n) ∼ c∗ nk−−dd then

md(k,n) ∼ max c∗, 21

![image 27](<2011-alon-large-matchings-uniform-hypergraphs_images/imageFile27.png>)

n − d k − d

. (5)

This result reduces the task of asymptotically calculating md(k,n) to a presumably simpler task of calculating fd(k,n). It seems that, similarly to the integral case, the lower bound in (4) determines asymptotically the actual value of the parameter fd(k,n).

Conjecture 1.2 For all 1 ≤ d ≤ k − 1,

fd(k,n) ∼ 1 −

k − 1 k

![image 28](<2011-alon-large-matchings-uniform-hypergraphs_images/imageFile28.png>)

k−d n − d k − d

.

Our next result conﬁrms Conjecture 1.2 asymptotically for all k and d such that 1 ≤ k−d ≤ 4. Note that the above mentioned result from [24] shows that Conjecture 1.2 is true for d = k − 1 exactly, that is, fk−1(k,n) = δk−1 H1 ⌈nk⌉ + 1. We include this case into the statement of Theorem 1.2 for completeness.

![image 29](<2011-alon-large-matchings-uniform-hypergraphs_images/imageFile29.png>)

- Theorem 1.2 For every k ≥ 3 and k − 4 ≤ d ≤ k − 1, we have


fd(k,n) ∼ 1 −

k − 1 k

![image 30](<2011-alon-large-matchings-uniform-hypergraphs_images/imageFile30.png>)

k−d n − d k − d

.

Theorems 1.2 and 1.1 together imply immediately the validity of Conjecture 1.1 in a couple of new instances (as discussed earlier, the ﬁrst of them has been recently also proved in [14] and [19]).

- Corollary 1.1 We have


m1(4,n) ∼ 6437 n−31 , m2(5,n) ∼ 12 n−32 , m1(5,n) ∼ 625369 n−41 m2(6,n) ∼ 1296671 n−42 , m3(7,n) ∼ 12 n−43 .

![image 31](<2011-alon-large-matchings-uniform-hypergraphs_images/imageFile31.png>)

![image 32](<2011-alon-large-matchings-uniform-hypergraphs_images/imageFile32.png>)

![image 33](<2011-alon-large-matchings-uniform-hypergraphs_images/imageFile33.png>)

![image 34](<2011-alon-large-matchings-uniform-hypergraphs_images/imageFile34.png>)

![image 35](<2011-alon-large-matchings-uniform-hypergraphs_images/imageFile35.png>)

We prove Theorem 1.2 utilizing the following connection between the parameters fds(k,n) and f0s(k− d,n − d).

- Proposition 1.1 For all k ≥ 3, 1 ≤ d ≤ k − 1, and n ≥ k,


fd(k,n) ≤ f0n/k(k − d,n − d).

In view of Proposition 1.1, in order to prove Theorem 1.2 we need to estimate f0s(k − d,n − d) with s = nk. This is trivial for d = k − 1 and so, from now on, we will be assuming that d ≤ k − 2. The integral version of this problem has almost as long history as the Dirac-type problem (d ≥ 1).

![image 36](<2011-alon-large-matchings-uniform-hypergraphs_images/imageFile36.png>)

Erd˝os and Gallai [6] determined ms0(k,n) for graphs (k = 2). In 1965, Erd˝os [5] conjectured the following hypergraph generalization of their result.

- Conjecture 1.3 For all k ≥ 2 and 1 ≤ s ≤ nk:

![image 37](<2011-alon-large-matchings-uniform-hypergraphs_images/imageFile37.png>)

ms0(k,n) = max

ks − 1 k

,

n k

−

n − s + 1 k

+ 1.

The lower bound comes from considering again the extremal k-graph H1(s) along with the k-uniform clique Kks(k−) 1 (complemented by n − ks + 1 isolated vertices) which, clearly, has no matching of size s. For more on Erd˝os’ conjecture we refer the reader to the survey paper [7] and a recent paper [9], where the conjecture is proved for k = 3 and n ≥ 4s. In its full generality, the conjecture is still wide open.

We now formulate the fractional version of Erd˝os’ Conjecture. For future references, we switch from

- k and n to l and m. Again, the lower bound is yielded by H1(⌈s⌉) and the complete l-graph on ⌈ls⌉ − 1 vertices, K⌈(lsl)⌉−1.

Conjecture 1.4 For all integers l ≥ 2 and an integer s such that 0 ≤ s ≤ m/l, we have

f0s(l,m) = max

⌈ls⌉ − 1 l

,

m l

−

m − ⌈s⌉ + 1 l

+ 1.

Note that Conjecture 1.4 implies that the bound is also asymptotically true for non-integer values of s, when m is large. In [18], there is an example showing that the stronger, precise version of the conjecture does not hold for fractional s.

As a consequence of the Erd˝os-Gallai theorem from [6], Conjecture 1.4 is asymptotically true for

- l = 2 and m goes to inﬁnity. In the next section we establish a result which conﬁrms Conjecture




- 1.4 asymptotically in the two smallest new instances, but limited to the range 0 ≤ s ≤ l+1m . In this range the case l = 3 follows also from the above mentioned result in [9]. It is easy to check that for s ≤ l+1m + O(1), the maximum in Conjecture 1.4 is achieved by the second term.


![image 38](<2011-alon-large-matchings-uniform-hypergraphs_images/imageFile38.png>)

![image 39](<2011-alon-large-matchings-uniform-hypergraphs_images/imageFile39.png>)

- Theorem 1.3 For l ∈ {3,4}, for all d ≥ 1, and s = ml++dd,


![image 40](<2011-alon-large-matchings-uniform-hypergraphs_images/imageFile40.png>)

l m

1 l + d

f0s(l,m) ∼ 1 − 1 −

![image 41](<2011-alon-large-matchings-uniform-hypergraphs_images/imageFile41.png>)

l where the asymptotics holds for m → ∞ with d ﬁxed.

- Theorem 1.3 together with Proposition 1.1 implies Theorem 1.2, which, in turn, together with


- Theorem 1.1 yields Corollary 1.1. To prove Conjecture 1.1 in full generality, one would need to prove Theorem 1.3 for all l.

The rest of this paper is organized as follows. In the next section, we prove Theorem 1.3 using as a main tool a probabilistic inequality of Samuels. A proof of Proposition 1.1, and consequently of

- Theorem 1.2, appears in Section 3. Section 4 contains a proof of Theorem 1.1. Finally, in Section


- 5, we discuss an application of the fractional version of the Erd¨os problem in distributed storage allocation. The last section contains concluding remarks and open problems.


# 2 Fractional matchings and probability of small deviations

In this section we prove Theorem 1.3 using a probabilistic approach from [1] based on a special case of an old probabilistic conjecture of Samuels [27]. In fact, we prove a little bit more – see Corollary

- 2.1 and Remark 2.1 below. For l reals µ1,... ,µl satisfying 0 ≤ µ1 ≤ µ2 ≤ ··· ≤ µl and li=1 µi < 1, let


P(µ1,µ2,... ,µl) = inf P(X1 + ... + Xl < 1),

where the inﬁmum is taken over all possible collections of l independent nonnegative random variables X1,... ,Xl, with expectations µ1,... ,µl, respectively. Deﬁne

l

Qt(µ1,... ,µl) =

i=t+1

µi 1 − tj=1 µj

1 −

![image 42](<2011-alon-large-matchings-uniform-hypergraphs_images/imageFile42.png>)

for each 0 ≤ t < l. Note that Qt(µ1,... ,µl) is exactly P(X1 +...+Xl < 1) when Xi is identically µi for all i ≤ t, while Xi attains the values 0 and 1 − i≤t µi (with its expectation being µi) for all i ≥ t + 1. The following conjecture was raised by Samuels in [27].

Conjecture 2.1 ([27]) For all admissible values of µ1,... ,µl, P(µ1,µ2,... ,µl) = min

Qt(µ1,µ2,... ,µl).

t=0,...,l−1

Note that for l = 1 this is Markov’s inequality. Samuels proved his conjecture for l ≤ 4 in [27, 28].

Lemma 2.1 ([27, 28]) The assertion of Conjecture 2.1 holds for all l ≤ 4.

We next show that for µ1 = µ2 = ··· = µl = x, where 0 < x ≤ l+11 , the minimum in Conjecture 2.1 is attained by Q0(µ1,... ,µl).

![image 43](<2011-alon-large-matchings-uniform-hypergraphs_images/imageFile43.png>)

- Proposition 2.1 For every integer l ≥ 2 and every real number x satisfying 0 < x ≤ l+11 , if µ1 = µ2 = ... = µl = x then


![image 44](<2011-alon-large-matchings-uniform-hypergraphs_images/imageFile44.png>)

Qt(µ1,µ2,... ,µl) = Q0(µ1,µ2,... ,µl) = (1 − x)l.

min

t=0,...,l−1

Proof: By deﬁnition

x 1 − tx

Qt(µ1,µ2,... ,µl) = 1 −

![image 45](<2011-alon-large-matchings-uniform-hypergraphs_images/imageFile45.png>)

l−t

=

1 − (t + 1)x 1 − tx

![image 46](<2011-alon-large-matchings-uniform-hypergraphs_images/imageFile46.png>)

l−t

.

We thus have to prove that for 0 < x ≤ l+11 and 1 ≤ t ≤ l − 1,

![image 47](<2011-alon-large-matchings-uniform-hypergraphs_images/imageFile47.png>)

(1 − x)l ≤

1 − (t + 1)x 1 − tx

![image 48](<2011-alon-large-matchings-uniform-hypergraphs_images/imageFile48.png>)

l−t

or equivalently that

1 − tx 1 − (t + 1)x

1 1 − x

l−t

l

. By the geometric-arithmetic means inequality applied to a set of l numbers, t of which are equal to 1 and the remaining l − t equal to the quantity 1−1(−t+1)tx x, we conclude that

≥

![image 49](<2011-alon-large-matchings-uniform-hypergraphs_images/imageFile49.png>)

![image 50](<2011-alon-large-matchings-uniform-hypergraphs_images/imageFile50.png>)

![image 51](<2011-alon-large-matchings-uniform-hypergraphs_images/imageFile51.png>)

1 − tx 1 − (t + 1)x

![image 52](<2011-alon-large-matchings-uniform-hypergraphs_images/imageFile52.png>)

l−t

· 1t ≤

1 l

·

![image 53](<2011-alon-large-matchings-uniform-hypergraphs_images/imageFile53.png>)

(1 − tx)(l − t) 1 − (t + 1)x

+ t

![image 54](<2011-alon-large-matchings-uniform-hypergraphs_images/imageFile54.png>)

Thus, it suﬃces to show that

l 1 − x

(1 − tx)(l − t) 1 − (t + 1)x

. This is equivalent to

+ t ≤

![image 55](<2011-alon-large-matchings-uniform-hypergraphs_images/imageFile55.png>)

![image 56](<2011-alon-large-matchings-uniform-hypergraphs_images/imageFile56.png>)

l

.

(1 − x)[(1 − tx)(l − t) + t − t(t + 1)x] ≤ l[1 − (t + 1)x], which is equivalent to

(1 − x)[l − t(l + 1)x] ≤ l − l(t + 1)x, or

l − t(l + 1)x − lx + t(l + 1)x2 ≤ l − l(t + 1)x.

After dividing by x, we see that this is equivalent to x ≤ l+11 , which holds by assumption, completing the proof.

![image 57](<2011-alon-large-matchings-uniform-hypergraphs_images/imageFile57.png>)

![image 58](<2011-alon-large-matchings-uniform-hypergraphs_images/imageFile58.png>)

Note that when s = xm and x ≤ l+11 , the maximum in Conjecture 1.4 is achieved by the second term. We now prove the following, in most part conditional, result, which shows how to deduce

![image 59](<2011-alon-large-matchings-uniform-hypergraphs_images/imageFile59.png>)

Conjecture 1.4 in this range from Conjecture 2.1.

- Theorem 2.1 For any l ≥ 3 and 0 < x ≤ l+11 , if Conjecture 2.1 holds for l and µ1 = µ2 = ... = µl = x then


![image 60](<2011-alon-large-matchings-uniform-hypergraphs_images/imageFile60.png>)

f0xm(l,m) ∼ 1 − (1 − x)l

m l

.

Combining Theorem 2.1 with Lemma 2.1, we obtain the following corollary which implies Theorem 1.3. (For d = 1, observe that f0s(l,m) ∼ f0s(l,m + 1).)

- Corollary 2.1 For l = 3, x ≤ 1/4 and for l = 4, x ≤ 1/5, the maximum number of edges in an l-uniform hypergraph H on m vertices with fractional matching number less than xm is


f0xm(l,m) ∼ 1 − (1 − x)l

m l

.

Proof of Theorem 2.1: Let H be an l-uniform hypergraph on a vertex set V , |V | = m, and suppose that ν∗(H) < xm. By duality, we also have τ∗(H) < xm, and hence there exists a weight function w : V → [0,1] such that v∈V w(v) < xm and, for every edge e of H, v∈e w(v) ≥ 1. By increasing the weights w(v) if needed, we may assume that

m

w(v) = xm.

v∈V

Let v1,... ,vl be a sequence of random vertices of H, chosen independently and uniformly at random from V . For each i = 1,... ,l we deﬁne a random variable Xi = w(vi). Note that X1,X2,... ,Xl are independent, identically distributed random variables, where every Xi attains each of the m values w(v) with probability 1/m. (The values of w for diﬀerent vertices can be equal, but this is of no importance for us.)

By deﬁnition, the expectation µi of each Xi is

µi =

v∈V

1 m

xm m

· w(v) =

= x.

![image 61](<2011-alon-large-matchings-uniform-hypergraphs_images/imageFile61.png>)

![image 62](<2011-alon-large-matchings-uniform-hypergraphs_images/imageFile62.png>)

Now we can estimate the number of edges of H as follows. Since for each edge of H we have

v∈e w(v) ≥ 1, the number N of all l-element subsets S of V with v∈S w(v) < 1 is a lower bound on the number of non-edges of H. Let N1 and N2 be the numbers of all l-element sequences of vertices of V and all l-element sequences of distinct vertices of V , respectively, with the sums of weights strictly smaller than 1. Note that N1 − N2 is at most the number of l-element sequences in which at least one vertex appears twice, thus it is bounded by 2 l ml−1 = O(ml−1). As the number of all l-element subsets of V is ml = (1 + o(1))ml/l! and N = N2/l!, we have

P

l

N1 ml

w(vi) < 1 =

![image 63](<2011-alon-large-matchings-uniform-hypergraphs_images/imageFile63.png>)

i=1

N2 + O(ml−1)

N

.

= (1 + o(1))

≤

![image 64](<2011-alon-large-matchings-uniform-hypergraphs_images/imageFile64.png>)

![image 65](<2011-alon-large-matchings-uniform-hypergraphs_images/imageFile65.png>)

m

m l

l l!

If Conjecture 2.1 holds for a given l then, by Lemma 2.1 and Proposition 2.1,

P

l

w(vi) < 1 = P

i=1

l

Xi < 1 ≥ (1 − x)l,

i=1

and, consequently,

N ≥ (1 + o(1))(1 − x)l

m l

.

It follows that the number of edges of H is at most (1 + o(1)) 1 − (1 − x)l ml , as needed.

![image 66](<2011-alon-large-matchings-uniform-hypergraphs_images/imageFile66.png>)

- Remark 2.1 Note that the above proof works as long as the conclusion of Proposition 2.1 holds. One can check using Mathematica that Proposition 2.1 holds for l = 3 and all 0 < x ≤ 0.277, as well as for l = 4 and all 0 < x ≤ 0.217. Therefore, Corollary 2.1 extends to these broader ranges of x. For bigger values of x, e.g., for x = 0.3 when l = 3, this is not the case anymore, and the above method does not suﬃce to determine the asymptotic behavior of f0xm(l,m). In fact, using Samuels conjecture in the higher range of x, one gets a bound on f0xm(l,m) which is larger than that in


Conjecture 1.4. However, in view of Proposition 1.1, for our main application the case x ≤ l+11 is just what we need.

![image 67](<2011-alon-large-matchings-uniform-hypergraphs_images/imageFile67.png>)

# 3 Thresholds for perfect fractional matchings

In this section we present a proof of Proposition 1.1 and then deduce quickly Theorem 1.2.

Proof of Proposition 1.1: The outline of the proof goes as follows. We will assume that there is no fractional perfect matching in a k-graph H on n vertices and then show that the neighborhood graph H(L) in H of a particular set L of size d satisﬁes ν∗(H(L)) < n/k. This will imply that δd(H) ≤ |H(L)| < f0n/k(k−d,n−d). In contrapositive, we will prove that if δd(H) ≥ f0n/k(k−d,n−d) then H has a fractional perfect matching, from which it follows, by deﬁnition, that fd(k,n) ≤ f0n/k(k − d,n − d).

Let an n-vertex k-graph H satisfy ν∗(H) < n/k, that is, have no fractional perfect matching. As τ∗(H) = ν∗(H), there is a function w : V → [0,1] such that v∈V w(v) < n/k and, for every e ∈ H, we have v∈e w(v) ≥ 1. We can replace H with the k-graph whose edge set consists of every k-tuple of vertices on which w totals to at least one.

Formally, for every weight function w : V → [0,1] deﬁne

Hw := e ∈

V k

:

w(v) ≥ 1 .

v∈e

For a given weight function w, suppose L is a set of d vertices with the smallest weights. Without loss of generality, we may assume that the d lowest values of w(x) are all equal to each other, since otherwise we could replace them by their average. (Obviously, this modiﬁcation would not

change v∈V w(v) nor the set L.) Note that the minimum d-degree δd(Hw) = minS⊂(Vd) degH(S) is achieved when S = L. Let H(L) be the neighborhood of L in Hw, that is a (k − d)-graph on the vertex set V \ L and with the edge set

S ∈

V − L k − d

: S ∪ L ∈ E(Hw) .

Then |H(L)| = δd(Hw) and it remains to prove that τ∗(H(L)) < n/k. Let w0 = minv∈V w(v) and observe that w0 < 1/k. If w0 > 0, apply to the weight function w the following linear map

w − w0 1 − kw0

w′ =

.

![image 68](<2011-alon-large-matchings-uniform-hypergraphs_images/imageFile68.png>)

Then, still v∈V w′(v) < n/k and Hw = Hw′. Moreover, for every v ∈ L, we have w′(v) = 0. It follows that the function w′ restricted to the set V \ L is a fractional vertex cover of H(L) and so ν∗(H(L)) = τ∗(H(L)) < n/k, which completes the proof of Proposition 1.1.

![image 69](<2011-alon-large-matchings-uniform-hypergraphs_images/imageFile69.png>)

Proof of Theorem 1.2: As explained earlier, f0n/k(k −d,n−d) = n/k holds trivially for d = k −1 and together with Proposition 1.1 implies the theorem in this case. For d = k − 2, we apply Proposition 1.1 together with the case l = 2 of the fractional Erd˝os Conjecture 1.4 (as mentioned earlier, it follows asymptotically from [6]). For d = k − 3 and d = k − 4, we use Proposition 1.1 and Corollary 1.3 proved in the previous section.

![image 70](<2011-alon-large-matchings-uniform-hypergraphs_images/imageFile70.png>)

- Remark 3.1 Consider a restricted version of Samuels’ problem to minimize P(X1 + ··· + Xl < 1) under the additional assumption that all random variables are identically distributed. Our proofs indicate that under this regime, for a given l ≥ 5 and µ1 = ··· = ml = x ≤ l+11 , if


![image 71](<2011-alon-large-matchings-uniform-hypergraphs_images/imageFile71.png>)

P(X1 + ··· + Xl < 1) ≥ (1 + o(1))(1 − x)l then Theorem 1.2 would hold for all k ≥ l + 1 and d = k − l.

# 4 Constructing integer matchings from fractional ones

In this section, we will prove Theorem 1.1. An indispensable tool in our proof is the Strong Absorbing Lemma 4.1 from [10] (see Lemma 10 therein). This lemma provides a suﬃcient condition on degrees and co-degrees of a hypergraph ensuring the existence of a small and powerful matching which, by “absorbing” vertices, creates a perfect matching from any nearly perfect matching.

- Lemma 4.1 For all γ > 0 and integers k > d > 0 there is an n0 such that for all n > n0 the


following holds: suppose that H is a k-graph on n vertices with δd(H) ≥ (1/2+2γ) nk−−dd , then there exists a matching M := Mabs in H such that

- (i) |M| < γkn/k, and


- (ii) for every set W ⊂ V \ V (M) of size at most |W| ≤ γ2kn and divisible by k there exists a matching in H covering exactly the vertices of V (M) ∪ W.


Equipped with this lemma we can practically reduce our task to ﬁnding an almost perfect matching in a suitable subhypergraph of H. Here is an outline of our proof of Theorem 1.1. Assume that there exists a constant 0 < c∗ < 1 such that fd(k,n) ∼ c∗ nk−−dd . For any α > 0 consider a k-graph H on n vertices, where n is suﬃciently large, with

δd(H) ≥ (c + α)

n − d k − d

,

where c = max{21,c∗}. Our goal is to show that H contains a perfect matching. Set γ = α/2 and ε = γ2k. The proof consists of three steps.

![image 72](<2011-alon-large-matchings-uniform-hypergraphs_images/imageFile72.png>)

- 1. Find an absorbing matching Mabs satisfying properties (i) and (ii) of Lemma 4.1. Set H′ = H \ V (Mabs) and note that when n is suﬃciently large,

δd(H′) ≥ δd(H) −

n − d k − d

−

n − d − εn k − d

≥ (c + α/2)

n − d k − d

= (c + γ)

n − d k − d

.

- 2. Find a matching Malm in H′ such that |V (Malm)| ≥ (1 − ε)|V (H′)|, and thus, |V (Malm ∪ Mabs)| ≥ (1 − ε)n.
- 3. Extend Malm ∪ Mabs to a perfect matching of H by using the absorbing property (ii) of Mabs with respect to W = V (H′) \ V (Malm).


Now come the details of the proof. The Strong Absorbing Lemma provides an absorbing matching Mabs, so Steps 1 and 3 are clear. Hence to complete the proof of Theorem 1.1 it remains to explain Step 2. One possible approach to ﬁnd an almost perfect matching in H′ is via the weak hypergraph regularity lemma. Our proof, however, is based on Theorem 1.1 in [8]. Recall that the 2-degree of a pair of vertices in a hypergraph is the number of edges containing this pair. An immediate corollary of that theorem asserts the existence of an almost perfect matching in any nearly regular k-graph in which all 2-degrees are much smaller than the vertex degrees. (See Remark after Theorem 1.1 in [8] or Chapter 4.7 of [2]). Here we formulate this corollary as the following lemma in which ∆2(H) denotes the maximum 2-degree in H.

- Lemma 4.2 For every integer k ≥ 2 and a real ε > 0, there exists τ = τ(k,ε), d0 = d0(k,ε) such that for every n ≥ D ≥ d0 the following holds. Every k-uniform hypergraph on a set V of n vertices which satisﬁes the following conditions:


- 1. (1 − τ)D < degH(v) < (1 + τ)D for all v ∈ V , and
- 2. ∆2(H) < τD


contains a matching Malm covering all but at most εn vertices.

Hence, Step 2 above reduces to ﬁnding a spanning subhypergraph H′′ of H′ satisfying the assumptions of Lemma 4.2 with ε = γ2k and other parameters τ,D,a to be suitably chosen. Indeed, the following claim is all we need to complete the proof of Theorem 1.1. For convenience, we set n := |V (H′)|. Recall that c = max{21,c∗} where c∗ comes from the threshold which guarantees the existence of fractional perfect matchings.

![image 73](<2011-alon-large-matchings-uniform-hypergraphs_images/imageFile73.png>)

Claim 4.1 For suﬃciently large n, any k-graph H′ on n vertices satisfying δd(H′) ≥ (c + γ) nk−−dd contains a spanning subhypergraph H′′, such that for all v ∈ V (H′′) we have degH′′(v) ∼ n0.2 while ∆2(H′′) ≤ n0.1.

Consequently for every k ≥ 2, ε > 0, the subhypergraph H′′ satisﬁes the assumptions of Lemma 4.2 with D = n0.2, and any τ > 0. We obtained the following result as an immediate corollary, which asserts the validity of Step 2 and completes our proof of Theorem 1.1.

Corollary 4.1 H′ contains an almost perfect matching covering at least (1 − ε)|V (H′)| vertices.

In the proof of Claim 4.1, the following well-known concentration results (see, for example [2], Appendix A, and Theorem 2.8, inequality (2.9) and (2.11) in [12]) will be used several times. We denote by Bi(n,p) a binomial random variable with parameters n and p.

- Lemma 4.3 (Chernoﬀ Inequality for small deviation) If X = ni=1 Xi, each random variable Xi has Bernoulli distribution with expectation pi, and α ≤ 3/2, then

P(|X − EX| ≥ αEX) ≤ 2e−α

- 2

![image 74](<2011-alon-large-matchings-uniform-hypergraphs_images/imageFile74.png>)

- 3 EX (6)


In particular, when X ∼ Bi(n,p) and λ < 32np, then P(|X − np| ≥ λ) ≤ e−Ω(λ2/(np)) (7)

![image 75](<2011-alon-large-matchings-uniform-hypergraphs_images/imageFile75.png>)

- Lemma 4.4 (Chernoﬀ Inequality for large deviation) If X = ni=1 Xi, each random variable Xi has Bernoulli distribution with expectation pi, and x ≥ 7 EX, then


P(X ≥ x) ≤ e−x (8)

Proof of Claim 4.1: The desired subhypergraph H′′ is obtained via two rounds of randomization. In the ﬁrst round, we ﬁnd edge-disjoint induced subhypergraphs with large minimum degrees which guarantees the existence of perfect fractional matchings. In the second round, we construct H′′ from these fractional matchings.

As a preparation toward the ﬁrst round, R is obtained by choosing every vertex randomly and independently with probability p = |V ′|−0.9 = n−0.9. Then |R| is a binomial random variable with expectation n0.1. By inequality (7), |R| ∼ n0.1 with probability 1 − e−Ω(n0.1).

Fix a subset D ⊆ V ′ of size d and let DEGD be the number of edges f ∈ H′ such that D ⊂ f and f \ D ⊆ R, which is the number of edges e in the link graph H[D] with all of its vertices in the

random set R. Therefore DEGD = e∈H[D] Xe, where Xe = 1 if e is in R and 0 otherwise. We have

E(DEGD) = degH′(D) × (n−0.9)k−d ≥ (c + α/2)

≥ (c + α/3)

|R| − d k − d

= Ω(n0.1(k−d))

n − d k − d

n−0.9(k−d)

For two distinct intersecting edges ei,ej with |ei ∩ ej| = l for 1 ≤ l ≤ k − d − 1, the probability that both of them are in R is

P(Xei = Xej = 1) = p2(k−d)−l

For ﬁxed l, there are at most nk−−dd choices for ei in the link graph H[D], k−l d ways to choose the intersection L = ei ∩ ej of size l, and (n−kd−)−d−(kl−d) options for ej\L. Therefore,

k−d−1

p2(k−d)−l

P(Xei = Xej = 1) ≤

∆ =

l=1

ei∩ej =∅

n − d k − d

k−d−l

p2(k−d)−lO(n2(k−d)−l) = O(n0.1(2(k−d)−1))

≤

l=1

By Janson’s inequality (see Theorem 8.7.2 in [2]),

- k − d
- l


n − k k − d − l

P(DEGD ≤ (1 − α/12)E(DEGD)) ≤ e−Ω((EX)2/∆) ∼ e−Ω(n0.1)

Therefore by the union bound, with probability 1 − nde−Ω(n0.1), for all subsets D ⊆ V ′ of size d, we have

|R| − d k − d

DEGD > (1 − α/12)E(DEGD)) ≥ (c + α/4)

.

Take n1.1 independent copies of R and denote them by Ri, 1 ≤ i ≤ n1.1, and the corresponding random variables by DEGD(i), where D ⊆ V ′, |D| = d, and i = 1,... ,n1.1. Since |Ri| ∼ n0.1 with probability 1−e−Ω(n0.1) for each i, the union bound ensures that |Ri| ∼ n0.1 for every i = 1,··· ,n1.1 with probability 1 − o(1). Now for a subset of vertices S ⊆ V ′, deﬁne the random variable

YS = |{i : S ⊆ Ri}|.

Note that the random variables YS have binomial distributions Bi(n1.1,n−0.9|S|) with expectations

- n1.1−0.9|S|. In particular, for every vertex v ∈ V ′, Y{v} ∼ Bi(n1.1,n−0.9) and EY{v} = n0.2. Hence, by inequality (7), taking λ = n0.15,


P(|Y{v} − n0.2| > n0.15) ≤ e−Ω((n0.15)2/n0.2) = e−Ω(n0.1) Therefore a.a.s |Y{v} − n0.2| ≤ n0.15 for every vertex v ∈ V ′.

Further, let

V ′ 2

: Y{u,v} ≥ 3 . Then

Z2 = {u,v} ∈

EZ2 < n2(n1.1)3(n−0.9)6 = n−0.1. Therefore by Markov’s inequality,

P(Z2 = 0) = 1 − P(Z2 ≥ 1) ≥ 1 − EZ2 > 1 − n−0.1 This implies that a.a.s every pair of vertices {u,v} is contained in at most two subhypergraphs Ri. Finally, for k ≥ 3, let

V ′ k

Zk = S ∈

: YS ≥ 2 . Then,

EZk < nk(n1.1)2(n−0.9)2k = nk+2.2−1.8k ≤ n−0.2 Similarly,

P(Zk = 0) > 1 − n−0.2

The latter implies that a.a.s. the induced subhypergraphs H[Ri], i = 1,... ,n1.1, are pairwise edge-disjoint. Summarizing, we can choose the sets Ri, 1 ≤ i ≤ n1.1 in such a way that

- (i) for every v ∈ V ′, Y{v} ∼ n0.2,
- (ii) every pair {u,v} ⊂ V ′ is contained in at most two sets Ri,
- (iii) every edge e ∈ H is contained in at most one set Ri,
- (iv) for all i = 1,... ,n1.1, we have |Ri| ∼ n0.1, and
- (v) for all i = 1,... ,n1.1 and all D ⊆ V ′, |D| = d, we have DEG(Di) ≥ (c + α/4) |Rki−|−dd .


Let us ﬁx a sequence Ri, 1 ≤ i ≤ n1.1, satisfying (i)-(v) above. Our assumption that fd(k,n) ∼ c∗ nk−−dd holds for all suﬃciently large values of n, in particular with n replaced by |Ri| ∼ n0.1. Thus, we have

fd(k,|Ri|) ∼ c∗

|Ri| − d k − d

,

and, by condition (v) above, we conclude that

δd(H[Ri]) ≥ (c + α/4)

|Ri| − d k − d

> fd(k,|Ri|).

Consequently, by the deﬁnition of fd, there exists a fractional perfect matchings wi in every subhypergraph H[Ri], i = 1,... ,n1.1.

Now comes the second round of randomization. Let H∗ = i H[Ri]. We select a generalized binomial subhypergraph H′′ of H∗ by independently choosing each edge e with probability wie(e),

where ie is the index i such that e ∈ H[Ri]. Recall that property (iii) ensures that every edge is contained in at most one hypergraph Ri, which guarantees the uniqueness of ie. We are going to verify our claim by showing degH′′(v) ∼ n0.2 for any vertex v, while ∆2(H′′) ≤ n0.1.

Let Iv = {i : v ∈ Ri} and recall that |Iv| = Y{v} ∼ n0.2 by (i). For every v ∈ V ′ the set Ev of edges e ∈ H∗ containing v can be partitioned into |Iv| parts Evi = {e ∈ Ev ∩ H[Ri]}. Recall that wi is a perfect matching, and thus e∈Ei

wi(e) = 1. For every v ∈ V ′ the random variable Dv = degH′′(v) is equal to i∈I

v

v e∈Evi Xe, where Xe are independent random variables having Bernoulli distribution with expectation wie(e). Therefore Dv is generalized binomial with expectation

EDv =

wie(e) =

wi(e) =

i∈Iv e∈Evi

e∈Ev

1 ∼ n0.2.

i∈Iv

Hence by Chernoﬀ’s inequality (6),

- 2

![image 76](<2011-alon-large-matchings-uniform-hypergraphs_images/imageFile76.png>)

- 3 n0.2


P(|Dv − n0.2| ≥ αn0.2) ≤ 2e−ε

Set α = n−0.05, then |Dv − n0.2| ≤ n0.15 with probability 1 − O(e−n0.1). Taking a union bound over all the n vertices, we conclude that a.a.s. for all v ∈ V ′ we have Dv ∼ n0.2.

Moreover, for all pairs u,v ∈ V ′ the random variable Du,v = degH′′(u,v) is also generalized binomial with expectation

wie(e) =

wi(e) ≤ |Iu ∩ Iv| ≤ 2

EDu,v =

i∈Iu∩Iv e∈Eui ∩Evi

e∈Eu∩Ev

by (ii). Hence, again by Chernoﬀ’s inequality (8) for large deviations, when n is suﬃciently large,

P(Du,v ≥ n0.1) ≤ e−n0.1

Once again taking the union bound ensures that a.a.s. for every pair of vertices u,v ∈ V ′, Du,v ≤ n0.1.

![image 77](<2011-alon-large-matchings-uniform-hypergraphs_images/imageFile77.png>)

# 5 An application in distributed storage allocation

The following model of distributed storage has been studied in information theory [17, 21, 29]. A ﬁle is split into multiple chunks, replicated redundantly and stored in a distributed storage system with n nodes. Suppose the amount of data to be stored in each node i is equal to xi, where the size of the whole ﬁle is normalized to 1. In reality, because there is limited storage space or transmission bandwidth, we require that the total amount of data stored does not exceed a given budget T, i.e. x1+···+xn ≤ T. At the time of retrieval, we attempt to recover the whole ﬁle by accessing only the data stored in a subset R of r nodes which is chosen uniformly at random. It is known that there

always exists a coding scheme such that we can recover the ﬁle whenever the total amount of data accessed is at least 1. Our goal is to ﬁnd an optimal allocation (x1,··· ,xn) in order to maximize the probability of successful recovery. This problem can be reformulated as follows.

Question 5.1 For a sequence of nonnegative numbers (x1,··· ,xn), let

Φ(x1,··· ,xn) = S ⊆ [n],|S| = r such that

xi ≥ 1 .

i∈S

Then the probability of successful recovery of the ﬁle equals

Φ(x1,··· ,xn) n r

.

![image 78](<2011-alon-large-matchings-uniform-hypergraphs_images/imageFile78.png>)

Given integers n ≥ r ≥ 1 and a real number T > 0, determine FT(r,n) = max

Φ(x1,··· ,xn).

xi=T, xi≥0 ∀i

and ﬁnd an allocation optimizing FT(r,n).

In this section, we always assume that T is integer-valued in order to avoid any rounding issues. If the total budget T is at least n/r then, by setting all xi = T/n ≥ 1/r for all i, we can recover the original ﬁle from any subset of size r. So, FT(r,n) = nr for T ≥ n/r. For T < n/r, let w(i) = xi be a weight function from V = [n] to R. Then by the deﬁnition of the threshold r-uniform hypergraph Hw1 from Section 3, the edges of Hw1 correspond to the r-subsets S such that i∈S xi ≥ 1. Thus, it is easy to see that the fractional matching number of Hw1 satisﬁes

ν∗(Hw1) = τ∗(Hw1) ≤

n

n

xi ≤ T

w(i) =

i=1

i=1

while

Φ(x1,··· ,xn) = |Hw1|. Therefore, FT(r,n) is the maximum number of edges in an r-uniform hypergraph on n vertices with fractional matching number at most T. As such FT(r,n) diﬀers from f0T(r,n) only in that the latter has the strict inequality ν∗(H) < T in its deﬁnition. But, of course, we have f0T(r,n) ≤ FT(r,n) ≤ f0T+1(r,n), and so FT(r,n) ∼ f0T(r,n) as n → ∞.

Hence, Question 5.1 is asymptotically equivalent to the fractional Erd˝os Conjecture 1.4. As mentioned in the introduction, it follows from the Erd˝os-Gallai theorem [6] that

FT(2,n) ∼ f0T(2,n) ∼ mT0 (2,n) ∼ max

2T 2

,

n 2

−

n − T 2

.

An easy calculation shows that the above maximum equals the ﬁrst term if 25n ≤ T ≤ 12n, and the corresponding optimal graph is a clique of size 2T. This means that, asymptotically, an optimal

![image 79](<2011-alon-large-matchings-uniform-hypergraphs_images/imageFile79.png>)

![image 80](<2011-alon-large-matchings-uniform-hypergraphs_images/imageFile80.png>)

allocation is x1 = ··· = x2T = 1/2 and x2T+1 = ··· = xn = 0. On the other hand, if T < 25n, an optimal allocation is x1 = ··· = xT = 1 and xT+1 = ··· = xn = 0.

![image 81](<2011-alon-large-matchings-uniform-hypergraphs_images/imageFile81.png>)

For general r ≥ 3, if Conjecture 1.4 is true, then

FT(r,n) ∼ max

rT r

,

n r

−

n − T r

.

The bounds are achieved when H is a clique or a complement of clique. A corresponding (asymptotically) optimal storage allocation is x1 = ··· = xrT = 1/r,xrT+1 = ··· = xn = 0 or x1 = ··· = xT = 1,xT+1 = ··· = xn = 0, respectively. Corollary 2.1 and Remark 2.1 assert that for r = 3 and T < 0.277 n, as well as for r = 4 and T < 0.217 n, the latter is an optimal allocation. Moreover, if Samuels’ conjecture 2.1 holds for all the remaining r ≥ 5, then x1 = ··· = xT = 1,xT+1 = ··· = xn = 0 is always an asymptotic optimal allocation whenever T < n/(r + 1). Erd˝os [5] proved Conjecture 1.3 for all T < n/(2r3). Recently, the authors of [11] extended the range for which this conjecture holds to T = O(n/r2). Therefore, in this range, FT(r,n) is achieved by the complement of a clique and an optimal allocation is also known to be x1 = ··· = xT = 1,xT+1 = ··· = xn = 0.

# 6 Concluding Remarks

- • We have studied suﬃcient conditions on the minimum d-degree which guarantee that a uniform hypergraph has a perfect matching or perfect fractional matching. We proved that if fd(k,n) ∼

c∗ nk , then md(k,n) ∼ max{c∗,1/2} nk . Therefore in order to determine the asymptotic behavior of the minimum d-degree ensuring existence of a perfect matching, we can instead study the

presumably easier question for fractional matchings. Using this approach we showed, in particular, that m1(5,n) ∼ 1 − 4544 n−41 .

![image 82](<2011-alon-large-matchings-uniform-hypergraphs_images/imageFile82.png>)

- • An intriguing problem which remains open is the conjecture by Erd˝os which states that the maximum number of edges in a k-uniform hypergraph H on n vertices with matching number smaller than s is exactly


max

ks − 1 k

,

n k

−

n − s + 1 k

.

The fractional version of Erd˝os conjecture is also very interesting. In its asymptotic form it says that if H is an l-uniform m-vertex hypergraph with fractional matching number ν∗(H) = xm, where 0 ≤ x < 1/l, then

|H| ≤ (1 + o(1))max (lx)l,1 − (1 − x)l

m l

.

In Section 2 we showed that the fractional Erd˝os conjecture is related to a probabilistic conjecture of Samuels. This conjecture, if proved, will provide a solution to the fractional version of Erd˝os problem for the range x ≤ l+11 . It will also lead to the asymptotics of md(k,n) and fd(k,n) for arbitrary k ≥ d + 1 and d ≥ 1.

![image 83](<2011-alon-large-matchings-uniform-hypergraphs_images/imageFile83.png>)

- • As it turns out, matchings and fractional matchings also have some interesting applications in information theory. In particular, the uniform model of distributed storage allocation considered in [29] leads to a question which is asymptotically equivalent to the fractional version of Erd˝os’ problem. In [17], the set of accessed nodes, R, is given by taking each node randomly and independently with probability p. It would be interesting to see if our techniques can be applied to study this binomial model too.


Acknowledgments The authors would like to thank Alex Dimakis for a discussion on the fractional Erd˝os conjecture, and an anonymous referee for many helpful comments.

# References

- [1] N. Alon, H. Huang, and B. Sudakov, Nonnegative k-sums, fractional covers, and probability of small deviations, J. Combin. Theory, Ser. B, to appear.
- [2] N. Alon and J. Spencer, The Probabilistic Method, John Wiley Inc., New York (2008).
- [3] D. E. Daykin and R. H¨aggkvist, Degrees giving independent edges in a hypergraph, Bull. Austral. Math. Soc. 23(1) (1981), 103–109.
- [4] G. A. Dirac, Some theorems of abstract graphs, Proc. London Math. Soc. 3 (1952), 69–81.
- [5] P. Erd˝os, A problem on independent r-tuples, Ann. Univ. Sci. Budapest. Eo˝tv˝os Sect. Math. 8 (1965), 93–95.
- [6] P. Erd˝os and T. Gallai, On maximal paths and circuits of graphs, Acta Math. Acad. Sci. Hungar. 10 (1959), 337–356.
- [7] P. Frankl, The shifting technique in extremal set theory, in: Surveys in Combinatorics, Lond. Math. Soc. Lect. Note Ser., 123 (1987), 81–110.
- [8] P. Frankl and V. Ro¨dl, Near perfect coverings in graphs and hypergraphs, European J. Combin., 6(4) (1985), 317–326
- [9] P. Frankl, V. Ro¨dl, and A. Rucin´ski, On the maximum number of edges in a triple system not containing a disjoint family of a given size, submitted.
- [10] H. H`an, Y. Person, and M. Schacht, On perfect matchings in uniform hypergraphs with large minimum vertex degree, SIAM J. Discrete Math. 23(2) (2009), 732–748.
- [11] H. Huang, P. Loh, and B. Sudakov, The size of a hypergraph and its matching number, Combin. Probab. Comput. , to appear.
- [12] S. Janson, T.  Luczak, and A. Rucin´ski, Random Graphs, John Wiley and Sons, New York


(2000).

- [13] I. Khan, Perfect matching in 3-uniform hypergraphs with large vertex degree, submitted.
- [14] I. Khan, Perfect matchings in 4-uniform hypergraphs, submitted.
- [15] D. Ku¨hn and D. Osthus, Embedding large subgraphs into dense graphs Surveys in Combinatorics (editors S. Huczynka, J. Mitchell, C. Roney-Dougal), London Math. Soc. Lecture Notes, Cambridge University Press 365 (2009), 137–167.
- [16] D. Ku¨hn, D. Osthus, and A. Treglown, Matchings in 3-uniform hypergraphs, submitted.
- [17] D. Leong, A. G. Dimakis, and T. Ho, Symmetric allocations for distributed storage, Proceedings of the IEEE Global Telecommunications Conference (GLOBECOM), (2010).
- [18] D. Leong, A. G. Dimakis, and T. Ho, Distributed storage allocations, available at http://arxiv.org/pdf/1011.5287v1.pdf.
- [19] A. Lo and K. Markstr¨om, F-factors in hypergraphs via absorption, submitted.
- [20] K. Markstr¨om and A. Rucin´ski, Perfect matchings and Hamilton cycles in hypergraphs with large degrees, Europ. J. Combin., 32(5) (2011), 677–687.
- [21] M. Naor and R. M. Roth, Optimal ﬁle sharing in distributed networks, SIAM J. Computing, 24 (1991), 158–183.
- [22] O. Pikhurko, Perfect matchings and K43-tilings in hypergraphs of large codegree, Graphs Combin. 24(4) (2008), 391–404.
- [23] V. Ro¨dl and A. Rucin´ski, Dirac-type questions for hypergraphs – a survey (or: more problems for Endre to solve), Bolyai Soc. Math. Studies 21 (2010), An Irregular Mind (Szemere´di is 70), Bolyai Soc. Math. Studies 21 (2010), 561–590.
- [24] V. Ro¨dl, A. Rucin´ski, and E. Szemere´di, Perfect matchings in uniform hypergraphs with large minimum degree, Europ. J. Combin. 27 (2006) 1333–1349.
- [25] V. Ro¨dl, A. Rucin´ski, and E. Szemere´di, An approximate Dirac-type theorem for k-uniform hypergraphs, Combinatorica 28(2) (2008), 229–260.
- [26] V. Ro¨dl, A. Rucin´ski, and E. Szemere´di, Perfect matchings in large uniform hypergraphs with large minimum collective degree, J. Combin. Theory, Ser. A 116 (2009), 613–636.
- [27] S. M. Samuels, On a Chebyshev-type inequality for sums of independent random variables, Ann. Math. Statist. 37 (1966), 248–259.
- [28] S. M. Samuels, More on a Chebyshev-type inequality for sums of independent random variables, Purdue Stat. Dept. Mimeo. Series no. 155 (1968).
- [29] M. Sardari, R. Restrepo, F. Fekri, and E. Soljanin, Memory allocation in distributed storage networks, Proceedings of IEEE International Symposium on Information Theory (ISIT), (2010).


