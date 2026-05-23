---
type: source
kind: paper
title: Almost all entries in the character table of the symmetric group are multiples of any given prime
authors: Sarah Peluse, Kannan Soundararajan
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2010.12410v2
source_local: ../raw/2020-peluse-almost-all-entries-character.pdf
topic: general-knowledge
cites:
---

arXiv:2010.12410v2[math.CO]5Jan2023

ALMOST ALL ENTRIES IN THE CHARACTER TABLE OF THE SYMMETRIC GROUP ARE MULTIPLES OF ANY GIVEN PRIME

SARAH PELUSE AND KANNAN SOUNDARARAJAN

Abstract. We show that almost every entry in the character table of SN is divisible by any ﬁxed prime as N → ∞. This proves a conjecture of Miller.

1. Introduction

In [11], Miller computed the character table of SN for all N up to 38, and noticed that the proportion of entries not divisible by 2, 3, or 5 seemed to tend to zero. Based on this, he conjectured that, for every ﬁxed prime q, almost every entry in the character table of SN is divisible by q as N → ∞. It has been known for a long time, due to work of McKay [9], that almost every character of SN has even degree. Recently, Gluck [5] showed that the proportion of odd entries in a sparse but inﬁnite set of columns of the character table tends to zero (see also the results of Malik, Stan, and Zaharescu [8] on zeros in certain columns of the character table), and Morotti [12] made further progress on Miller’s conjecture for each ﬁxed prime q. Even more recently, the ﬁrst author [14] proved Miller’s conjecture for q = 2, 3, 5, 7, 11, and 13.

In this paper, we completely resolve Miller’s conjecture, proving it for all primes. We also give an explicit bound, uniform in q almost up to log N, for the number of entries in the character table not divisible by q.

Theorem 1. Let p(N) denote the number of unrestricted partitions of N, so that p(N)2 denotes the number entries in the character table for SN. Let N be large, and let q be a prime with q ≤ (log N)/(log log N)2. The number of entries in the character table of SN that are not divisible by q is at most

1

O p(N)2N−

12q . In particular, almost all entries in the character table for SN are multiples of

![image 1](<2020-peluse-almost-all-entries-character_images/imageFile1.png>)

q.

q≤(log N)/(log log N)2

Miller [11] also computed the density of entries in the character table of SN divisible by 4, 8, 9, 25, 27, and 125, as well as the density of zeros in the character table. From this, it looks like the density of entries divisible by any ﬁxed prime power may go to 1, while the density of zeros may be approaching a positive constant less than 1. Our arguments do not apply to the problem of divisibility by higher prime powers. Regarding the number of zeros

1

in the character table, Proposition 1 below combined with the distribution of the largest part of a random partition yields that at least a proportion C/ log N (for some positive constant C) of the character values must be zero, and it is unclear whether a positive proportion of the entries are zero. However, in the related setting of ﬁnite simple groups of Lie type with rank going to inﬁnity, Larsen and Miller [6] have shown that almost every entry of the character table is zero.

When χ is chosen uniformly at random from the set of irreducible characters of SN and σ is a uniformly random permutation, Miller [10] showed that χ(σ) almost always vanishes. Another natural variant is to choose the character χ randomly according to the Plancherel measure (which assigns to the irreducible representation ρ the weight dim(ρ)2/N!). If a conjugacy class C of SN is chosen at random (with uniform measure from the p(N) possibilities) then χ(C) = 0 almost always. We give a brief indication of these results in §3.

Acknowledgments. The ﬁrst author is partially supported by the NSF Mathematical Sciences Postdoctoral Research Fellowship Program under Grant No. DMS-1903038 and by the Oswald Veblen Fund. The second author is partially supported by a grant from the National Science Foundation, and a Simons Investigator Grant from the Simons Foundation. We thank the referees for their careful reading.

2. Plan of the proof

For any two partitions λ and µ of N, let χλµ denote the value of the character of SN corresponding to the partition λ on the congruence class of permutations with cycle type µ. The basic idea of the proof of Theorem 1 is the same as that used in [14] to prove Miller’s conjecture for q ≤ 13: we will show that, for most partitions µ of N, one has χλµ ≡ χ µλ (mod q) for some partition µ of N that possesses a part so large that χλ µ is forced to be zero for most partitions λ of N. To that end, our ﬁrst proposition, which is a quantiﬁcation of an argument in [12], states that if the partition µ of N has a large part, then for most partitions λ of N one has χλµ = 0.

- Proposition 1. Let 1 ≤ A ≤ log N/ log log N be a real number. Suppose that µ is a partition of N such that the largest part of µ is


√6 2π

√

![image 2](<2020-peluse-almost-all-entries-character_images/imageFile2.png>)

1 A

![image 3](<2020-peluse-almost-all-entries-character_images/imageFile3.png>)

≥

. Then the number of partitions λ of N with χλµ = 0 is at most O p(N)

N(log N) 1 +

![image 4](<2020-peluse-almost-all-entries-character_images/imageFile4.png>)

![image 5](<2020-peluse-almost-all-entries-character_images/imageFile5.png>)

log N N 21A

.

![image 6](<2020-peluse-almost-all-entries-character_images/imageFile6.png>)

![image 7](<2020-peluse-almost-all-entries-character_images/imageFile7.png>)

√ Erd˝os and Lehner [2] showed that a random partition of N has largest part of size

√N log N + O(√N), so that the partitions µ considered in Proposition 1 are just a little bit atypical.

![image 8](<2020-peluse-almost-all-entries-character_images/imageFile8.png>)

6 2π

![image 9](<2020-peluse-almost-all-entries-character_images/imageFile9.png>)

![image 10](<2020-peluse-almost-all-entries-character_images/imageFile10.png>)

![image 11](<2020-peluse-almost-all-entries-character_images/imageFile11.png>)

We will, as in [14], use repeated applications of the following lemma to move from our original partition µ to the partition µ that we aim to show has a large part.

- Lemma 1. Let q be a prime. Suppose µ is a partition of N, and that ν is another partition of N obtained from µ by replacing q parts of the same size m by one part of size qm. Then for all partitions λ of N we have


χλµ ≡ χλν (mod q).

This is a simple consequence of Frobenius’s formula for computing character values, see for example Section 3 of [13], or Proposition 1 of [11].

Our second proposition says that, for a typical partition µ, the partition µ obtained by repeatedly applying the procedure described in Lemma 1 until no part appears more than q − 1 times has a part signiﬁcantly larger than

√N log N.

√6 2π

![image 12](<2020-peluse-almost-all-entries-character_images/imageFile12.png>)

![image 13](<2020-peluse-almost-all-entries-character_images/imageFile13.png>)

![image 14](<2020-peluse-almost-all-entries-character_images/imageFile14.png>)

- Proposition 2. Let q ≤ (log N)/(log log N)2 be a prime. Starting with a partition µ of N, we repeatedly replace every occurrence of q parts of the same size m by one part of size qm until we arrive at a partition µ where no part appears more than q − 1 times. Then the


largest part of µ exceeds √6 2π

√

![image 15](<2020-peluse-almost-all-entries-character_images/imageFile15.png>)

1 5q

![image 16](<2020-peluse-almost-all-entries-character_images/imageFile16.png>)

, except for at most

N(log N) 1 +

![image 17](<2020-peluse-almost-all-entries-character_images/imageFile17.png>)

![image 18](<2020-peluse-almost-all-entries-character_images/imageFile18.png>)

1 15q

O p(N) exp − N

![image 19](<2020-peluse-almost-all-entries-character_images/imageFile19.png>)

partitions µ.

If we consider only partitions of N where no part appears more than q − 1 times, then a small variation of the Erd˝os–Lehner argument shows that such partitions typically have a largest part of size about

√6N 2π

√q

![image 20](<2020-peluse-almost-all-entries-character_images/imageFile20.png>)

![image 21](<2020-peluse-almost-all-entries-character_images/imageFile21.png>)

√q−1 log N. This suggests why a result like Proposition 2 may be expected. However, some care is needed, since the partitions µ that are the result of our procedure may not look like a typical partition with no part appearing more than q − 1 times (for example, the largest part in µ will very likely be a multiple of q).

![image 22](<2020-peluse-almost-all-entries-character_images/imageFile22.png>)

![image 23](<2020-peluse-almost-all-entries-character_images/imageFile23.png>)

![image 24](<2020-peluse-almost-all-entries-character_images/imageFile24.png>)

Theorem 1 is now a straightforward consequence of Propositions 1 and 2, which we will prove in Sections 3 and 5, respectively.

Deducing Theorem 1. We are given a prime q ≤ (log N)/(log log N)2, and wish to bound the number of partitions λ, µ with χλµ  ≡ 0 (mod q). Let µ be as in Proposition 2. If the largest part of µ is below

√6N

![image 25](<2020-peluse-almost-all-entries-character_images/imageFile25.png>)

2π (log N)(1 + 51q) then Proposition 2 tells us that there are at most O p(N) exp(−N

![image 26](<2020-peluse-almost-all-entries-character_images/imageFile26.png>)

![image 27](<2020-peluse-almost-all-entries-character_images/imageFile27.png>)

1

1

15q ) × p(N) = O p(N)2 exp(−N

15q) choices for µ and λ.

![image 28](<2020-peluse-almost-all-entries-character_images/imageFile28.png>)

![image 29](<2020-peluse-almost-all-entries-character_images/imageFile29.png>)

√6N

![image 30](<2020-peluse-almost-all-entries-character_images/imageFile30.png>)

2π (log N)(1+51q), then by Proposition 1 χλ µ = 0 for at most O(p(N)(log N)N−

On the other hand, if the largest part of µ exceeds

![image 31](<2020-peluse-almost-all-entries-character_images/imageFile31.png>)

![image 32](<2020-peluse-almost-all-entries-character_images/imageFile32.png>)

1

10q) partitions λ. Thus, in this situation, since χλµ ≡ χ µλ (mod q) by Lemma 1, the number of partitions µ and λ with χλµ  ≡ 0 (mod q) is at most

![image 33](<2020-peluse-almost-all-entries-character_images/imageFile33.png>)

log N N

1

= O p(N)2N−

O p(N) × p(N)

12q .

![image 34](<2020-peluse-almost-all-entries-character_images/imageFile34.png>)

![image 35](<2020-peluse-almost-all-entries-character_images/imageFile35.png>)

1 10q

![image 36](<2020-peluse-almost-all-entries-character_images/imageFile36.png>)

Combining this (which is the bottleneck to improving Theorem 1 quantitatively) with our earlier bound, we conclude that there are at most

1 12q

O p(N)2N−

![image 37](<2020-peluse-almost-all-entries-character_images/imageFile37.png>)

pairs µ, λ with q ∤ χλµ. This establishes the ﬁrst assertion of the theorem, and the second assertion follows upon summing this bound over all q ≤ (log N)/(log log N)2.

3. Proof of Proposition 1

To prove Proposition 1, we will need the notion of a t-core partition. For any box b in the Young diagram of a partition, the hook-length of b is 1 plus the number of boxes directly to the right of b plus the number of boxes directly below b. For example, the Young diagram of λ = (4, 2, 1) below has each box labeled with its hook-length.

![image 38](<2020-peluse-almost-all-entries-character_images/imageFile38.png>)

![image 39](<2020-peluse-almost-all-entries-character_images/imageFile39.png>)

![image 40](<2020-peluse-almost-all-entries-character_images/imageFile40.png>)

![image 41](<2020-peluse-almost-all-entries-character_images/imageFile41.png>)

![image 42](<2020-peluse-almost-all-entries-character_images/imageFile42.png>)

![image 43](<2020-peluse-almost-all-entries-character_images/imageFile43.png>)

![image 44](<2020-peluse-almost-all-entries-character_images/imageFile44.png>)

![image 45](<2020-peluse-almost-all-entries-character_images/imageFile45.png>)

![image 46](<2020-peluse-almost-all-entries-character_images/imageFile46.png>)

![image 47](<2020-peluse-almost-all-entries-character_images/imageFile47.png>)

![image 48](<2020-peluse-almost-all-entries-character_images/imageFile48.png>)

![image 49](<2020-peluse-almost-all-entries-character_images/imageFile49.png>)

6 4 2 1 3 1 1

![image 50](<2020-peluse-almost-all-entries-character_images/imageFile50.png>)

![image 51](<2020-peluse-almost-all-entries-character_images/imageFile51.png>)

![image 52](<2020-peluse-almost-all-entries-character_images/imageFile52.png>)

![image 53](<2020-peluse-almost-all-entries-character_images/imageFile53.png>)

![image 54](<2020-peluse-almost-all-entries-character_images/imageFile54.png>)

![image 55](<2020-peluse-almost-all-entries-character_images/imageFile55.png>)

![image 56](<2020-peluse-almost-all-entries-character_images/imageFile56.png>)

![image 57](<2020-peluse-almost-all-entries-character_images/imageFile57.png>)

![image 58](<2020-peluse-almost-all-entries-character_images/imageFile58.png>)

![image 59](<2020-peluse-almost-all-entries-character_images/imageFile59.png>)

![image 60](<2020-peluse-almost-all-entries-character_images/imageFile60.png>)

![image 61](<2020-peluse-almost-all-entries-character_images/imageFile61.png>)

![image 62](<2020-peluse-almost-all-entries-character_images/imageFile62.png>)

![image 63](<2020-peluse-almost-all-entries-character_images/imageFile63.png>)

![image 64](<2020-peluse-almost-all-entries-character_images/imageFile64.png>)

![image 65](<2020-peluse-almost-all-entries-character_images/imageFile65.png>)

Figure 1. Hook-lengths for λ = (4, 2, 1).

A partition is called a t-core if none of the hook lengths of its Young diagram are divisible by t. For example, from Figure 1 one can see that (4, 2, 1) is a 5-core.

√6N

![image 66](<2020-peluse-almost-all-entries-character_images/imageFile66.png>)

- Proof of Proposition 1. Let t denote the largest part of µ, so that t ≥


2π (log N)(1 + 1/A) by assumption. If the partition λ is a t-core, then it follows from the Murnaghan–Nakayama rule (see Subsection 4.3 of [4]) that χλµ = 0. Now, from Lemma 5 of [12], we know that there are at most (t+1)p(N − t) partitions λ that are not t-cores. Therefore, the number of partitions λ with χλµ = 0 is at most

![image 67](<2020-peluse-almost-all-entries-character_images/imageFile67.png>)

√

√

2π √6

2π √6

t + 1 N − t + 1

t + 1 N − t + 1

πt √

![image 68](<2020-peluse-almost-all-entries-character_images/imageFile68.png>)

![image 69](<2020-peluse-almost-all-entries-character_images/imageFile69.png>)

(t + 1)p(N − t) ≪

N − t ≤

N −

exp

exp

, where in the ﬁrst inequality we have used the famous Hardy–Ramanujan asymptotic formula p(N) ∼

![image 70](<2020-peluse-almost-all-entries-character_images/imageFile70.png>)

![image 71](<2020-peluse-almost-all-entries-character_images/imageFile71.png>)

![image 72](<2020-peluse-almost-all-entries-character_images/imageFile72.png>)

![image 73](<2020-peluse-almost-all-entries-character_images/imageFile73.png>)

![image 74](<2020-peluse-almost-all-entries-character_images/imageFile74.png>)

![image 75](<2020-peluse-almost-all-entries-character_images/imageFile75.png>)

![image 76](<2020-peluse-almost-all-entries-character_images/imageFile76.png>)

![image 77](<2020-peluse-almost-all-entries-character_images/imageFile77.png>)

6N

√

2π √6

1 4N√3

![image 78](<2020-peluse-almost-all-entries-character_images/imageFile78.png>)

exp

N (see [15] for even more precise asymptotics).

![image 79](<2020-peluse-almost-all-entries-character_images/imageFile79.png>)

![image 80](<2020-peluse-almost-all-entries-character_images/imageFile80.png>)

![image 81](<2020-peluse-almost-all-entries-character_images/imageFile81.png>)

![image 82](<2020-peluse-almost-all-entries-character_images/imageFile82.png>)

√6N

![image 83](<2020-peluse-almost-all-entries-character_images/imageFile83.png>)

For N ≥ t ≥

2π (log N)(1 + 1/A), the right side above is maximized at the lower end point t =

![image 84](<2020-peluse-almost-all-entries-character_images/imageFile84.png>)

√6N

![image 85](<2020-peluse-almost-all-entries-character_images/imageFile85.png>)

2π (log N)(1 + 1/A), yielding the bound ≪

![image 86](<2020-peluse-almost-all-entries-character_images/imageFile86.png>)

√

√

![image 87](<2020-peluse-almost-all-entries-character_images/imageFile87.png>)

N log N N

2π √6

log N N

- 1

![image 88](<2020-peluse-almost-all-entries-character_images/imageFile88.png>)

- 2(1+A1 ) exp


![image 89](<2020-peluse-almost-all-entries-character_images/imageFile89.png>)

N−

N ≪ p(N)

.

![image 90](<2020-peluse-almost-all-entries-character_images/imageFile90.png>)

![image 91](<2020-peluse-almost-all-entries-character_images/imageFile91.png>)

![image 92](<2020-peluse-almost-all-entries-character_images/imageFile92.png>)

![image 93](<2020-peluse-almost-all-entries-character_images/imageFile93.png>)

- 1

![image 94](<2020-peluse-almost-all-entries-character_images/imageFile94.png>)

- 2A


![image 95](<2020-peluse-almost-all-entries-character_images/imageFile95.png>)

This establishes Proposition 1.

This may be a convenient juncture to elaborate on the comments at the end of our Introduction on variations of our problem. If the representation corresponding to λ is chosen at random (with the uniform measure on all irreducible representations), then we have seen that λ almost surely a t-core if t ≥

√6N

![image 96](<2020-peluse-almost-all-entries-character_images/imageFile96.png>)

2π (log N)(1 + 1/A). A random element (chosen uniformly) σ of the group SN will have a cycle of length ≥ N/ log N with very high probability. This is the basis of Miller’s result [10] that χλ(σ) = 0 almost always.

![image 97](<2020-peluse-almost-all-entries-character_images/imageFile97.png>)

If the representation corresponding to λ is chosen with the Plancherel measure, then from the work of Vershik and Kerov [16] it follows that almost surely the largest part of λ and the total number of parts in λ are ∼ 2√N, so that the maximal possible hook length is ≤ (4 + ǫ)√N. On the other hand, by Erd˝os–Lehner the largest part of a typical partition µ is about

![image 98](<2020-peluse-almost-all-entries-character_images/imageFile98.png>)

![image 99](<2020-peluse-almost-all-entries-character_images/imageFile99.png>)

√6N

![image 100](<2020-peluse-almost-all-entries-character_images/imageFile100.png>)

2π log N. It follows that if λ is chosen randomly according to the Plancherel measure and the conjugacy class corresponding to µ is chosen uniformly, then χλµ = 0 almost always.

![image 101](<2020-peluse-almost-all-entries-character_images/imageFile101.png>)

4. Preliminaries for the proof of Proposition 2

Let p(j) denote the number of partitions of j ≥ 0 into powers of q, with the convention that p(0) = 1. We deﬁne the generating function Fq(x) of p(j) by

Fq(x) :=

∞

p(j)e−j/x =

j=0

∞

j/x)−1

(1 − e−q

j=0

for a real number x > 0. Both p(j) and the generating function Fq(x) have been studied extensively for ﬁxed primes q, beginning with work of Mahler [7] and de Bruijn [1]. In our work we need only some simple estimates for these objects, but with uniformity in q.

- Lemma 2. In the range 0 < x ≤ 1, we have Fq(x) = O(1). When x ≥ 1 we have


- (1)


(log x)2 2 log q

+

![image 102](<2020-peluse-almost-all-entries-character_images/imageFile102.png>)

(log x)2 2 log q

- 1

![image 103](<2020-peluse-almost-all-entries-character_images/imageFile103.png>)

- 2


log x + O(1) ≤ log Fq(x) ≤

+

![image 104](<2020-peluse-almost-all-entries-character_images/imageFile104.png>)

- 1

![image 105](<2020-peluse-almost-all-entries-character_images/imageFile105.png>)

- 2


log x +

1 8

log q + O(1).

![image 106](<2020-peluse-almost-all-entries-character_images/imageFile106.png>)

Proof. When x ≤ 1, note that Fq(x) ≤ ∞j=0(1 − e−qj)−1 ≤ ∞j=0(1 − e−2j)−1, so that Fq(x) = O(1). Now suppose x ≥ 1. Note that the terms in the product ∞j=0(1 − e−qj/x)−1 with qj > x multiply out to a quantity bounded by ∞j=0(1 − e−qj)−1, so that they are bounded by an absolute constant. For the terms with qj ≤ x, note that log(1 − e−qj/x)−1 =

log(x/qj) + O(qj/x), so that log

∞

j/x)−1 =

(1 − e−q

j=0

0≤j≤log x/ log q

= (log x) 1 +

x qj

log

+ O(1)

![image 107](<2020-peluse-almost-all-entries-character_images/imageFile107.png>)

log x log q −

log q 2

![image 108](<2020-peluse-almost-all-entries-character_images/imageFile108.png>)

![image 109](<2020-peluse-almost-all-entries-character_images/imageFile109.png>)

log x log q

![image 110](<2020-peluse-almost-all-entries-character_images/imageFile110.png>)

1 +

log x log q

![image 111](<2020-peluse-almost-all-entries-character_images/imageFile111.png>)

+ O(1).

The estimates in (1) follow at once. In the second lemma of this section, we will record some basic properties of p.

- Lemma 3. The function p(k) is monotone non-decreasing in k. For all r ≥ 2 we have


qr(r−1)/2 (r − 1)r−1.

p(qr) ≥

![image 112](<2020-peluse-almost-all-entries-character_images/imageFile112.png>)

Proof. Appending 1 to a partition of k into powers of q produces a partition of k + 1 into powers of q. This shows that p(k) is monotone non-decreasing in k.

Suppose r ≥ 2. For each 1 ≤ j ≤ r − 1, pick a non-negative integer kj with 0 ≤ kj ≤ qr−j/(r − 1). Each choice for the kj’s gives a partition counted in p(qr) by using kj copies of qj, and then using qr − j r=1−1 kjqj copies of 1. Therefore

r−1

qr(r−1)/2

qr−j (r − 1)

p(qr) ≥

=

(r − 1)(r−1), as desired.

![image 113](<2020-peluse-almost-all-entries-character_images/imageFile113.png>)

![image 114](<2020-peluse-almost-all-entries-character_images/imageFile114.png>)

j=1

5. Proof of Proposition 2

Let us analyze the process of transforming a partition µ to a partition µ as in Proposition 2. Consider an integer k coprime to q, and all parts in µ of the form kqj with j ≥ 0. If these parts sum to kℓ, then in the partition µ we would have corresponding parts of the form kqj also summing to kℓ with the additional property that no part appears more than q−1 times. But this simply means that the number of parts of size kqj in µ equals the coeﬃcient (or ‘digit’) of qj in the base q expansion of ℓ. In particular, if ℓ ≥ qr, then the partition µ must have a part kqj with some j ≥ r (since ℓ must have more than r digits in base q).

Next, suppose µ has parts of the form kqj summing to kℓ with no part appearing more than q − 1 times. From how many partitions µ could this µ have arisen? Restricting our attention to these parts of the form kqj, note that µ could have had any collection of parts kqj that sum to kℓ; or in other words there are p(ℓ) (the number of partitions of ℓ into powers of q) choices for parts of the form kqj in µ.

Let K be a set of integers k with (k, q) = 1. We wish to count the number of partitions µ such that for k ∈ K the parts of the form kqj in µ sum to kℓ with ℓ < qr; call this quantity p(N; K, r). In other words, these are the partitions µ for which µ does not have a part kqj

with j ≥ r for all k ∈ K. By our remarks above, the count of such partitions µ is the coeﬃcient of zN in the generating function

- (2)

(k,q)=1 k/∈K

(1+ p(1)zk+ p(2)z2k+. . .)

k∈K

qr−1

ℓ=0

p(ℓ)zkℓ =

(k,q)=1 k/∈K

∞

j=0

(1−zkq

j

)−1

k∈K

qr−1

ℓ=0

p(ℓ)zkℓ .

For example, if K = ∅ then we are just counting all partitions of N, and the above generating function may be seen to be ∞n=1(1 − zn)−1.

Since the coeﬃcients in the expansion of the generating function (2) are all positive, for any 0 < z < 1 we have

p(N; K, r) ≤ z−N

(k,q)=1 k/∈K

∞

j=0

(1 − zkq

j

)−1

k∈K

qr−1

ℓ=0

p(ℓ)zkℓ

= z−N

∞

n=1

(1 − zn)−1

k∈K

qr−1

ℓ=0 p(ℓ)zkℓ

![image 115](<2020-peluse-almost-all-entries-character_images/imageFile115.png>)

∞

ℓ=0 p(ℓ)zkℓ

- (3) .

Here we shall take z = e−1/x with x = √N/ ζ(2) = √6N/π. This choice of z is motivated by the fact that the asymptotic for the unrestricted partitions p(N) arises from a contour integral computation integrating z over a circle with approximately this radius. For this choice of z, one has

![image 116](<2020-peluse-almost-all-entries-character_images/imageFile116.png>)

![image 117](<2020-peluse-almost-all-entries-character_images/imageFile117.png>)

![image 118](<2020-peluse-almost-all-entries-character_images/imageFile118.png>)

z−N

∞

n=1

(1 − zn)−1 ∼ exp 2 Nζ(2) −

![image 119](<2020-peluse-almost-all-entries-character_images/imageFile119.png>)

- 1

![image 120](<2020-peluse-almost-all-entries-character_images/imageFile120.png>)

- 2


log(

√

![image 121](<2020-peluse-almost-all-entries-character_images/imageFile121.png>)

24N) ≪ N

- 3

![image 122](<2020-peluse-almost-all-entries-character_images/imageFile122.png>)

- 4p(N)


(see Section VIII.6 of [3]). Thus, with this choice of x, we have

- (4) p(N; K, r) ≪ N


qr−1

ℓ=0 p(ℓ)e−kℓ/x

- 3

![image 123](<2020-peluse-almost-all-entries-character_images/imageFile123.png>)

- 4p(N)


ℓ=0 p(ℓ)e−kℓ/x . We are now ready for the proof of Proposition 2.

∞

![image 124](<2020-peluse-almost-all-entries-character_images/imageFile124.png>)

k∈K

- Proof of Proposition 2. We apply the above considerations, taking


r =

log N 2eq

![image 125](<2020-peluse-almost-all-entries-character_images/imageFile125.png>)

and K to be the set of integers k ≥ K with (k, q) = 1 where

√6N 2πqr

![image 126](<2020-peluse-almost-all-entries-character_images/imageFile126.png>)

1 5q

.

(log N) 1 +

K =

![image 127](<2020-peluse-almost-all-entries-character_images/imageFile127.png>)

![image 128](<2020-peluse-almost-all-entries-character_images/imageFile128.png>)

Then p(N; K, r) gives an upper bound for the number of partitions µ for which µ has largest part below Kqr =

√6N

![image 129](<2020-peluse-almost-all-entries-character_images/imageFile129.png>)

- 2π (log N)(1 + 1/(5q)), which is the quantity we desire to bound. Thus


![image 130](<2020-peluse-almost-all-entries-character_images/imageFile130.png>)

- (4) furnishes here the upper bound
- (5) ≪ N

- 3

![image 131](<2020-peluse-almost-all-entries-character_images/imageFile131.png>)

- 4p(N) exp −


k≥K (k,q)=1

ℓ≥qr

p(ℓ)e−ℓk/x Fq(x/k)

![image 132](<2020-peluse-almost-all-entries-character_images/imageFile132.png>)

= N

- 3

![image 133](<2020-peluse-almost-all-entries-character_images/imageFile133.png>)

- 4p(N) exp(−∆),


say, for this quantity.

It remains to show that ∆ is suitably large. Since p(ℓ) ≥ p(qr) for ℓ ≥ qr, and Fq(x/k) ≤ Fq(x/K) ≤ Fq(2qr/ log N) for k ≥ K, we obtain

∆ ≥

p(qr) Fq(2qr/ log N) k≥K

![image 134](<2020-peluse-almost-all-entries-character_images/imageFile134.png>)

(k,q)=1

ℓ≥qr

e−ℓk/x =

p(qr) Fq(2qr/ log N) k≥K

![image 135](<2020-peluse-almost-all-entries-character_images/imageFile135.png>)

(k,q)=1

e−qrk/x (1 − e−k/x)

![image 136](<2020-peluse-almost-all-entries-character_images/imageFile136.png>)

≥

p(qr) Fq(2qr/ log N) k≥K

![image 137](<2020-peluse-almost-all-entries-character_images/imageFile137.png>)

(k,q)=1

e−q

rk/xx k

![image 138](<2020-peluse-almost-all-entries-character_images/imageFile138.png>)

- (6) .

Restricting just to the terms K ≤ k ≤ K + x/qr(≤ 2K) the sum over k above is

- (7) ≥


x K

x qr

1 20

x 2K

−1

1

r/x−1

r/x ≥ 20N

e−Kq

e−Kq

1 ≥

10q log N

![image 139](<2020-peluse-almost-all-entries-character_images/imageFile139.png>)

![image 140](<2020-peluse-almost-all-entries-character_images/imageFile140.png>)

![image 141](<2020-peluse-almost-all-entries-character_images/imageFile141.png>)

![image 142](<2020-peluse-almost-all-entries-character_images/imageFile142.png>)

![image 143](<2020-peluse-almost-all-entries-character_images/imageFile143.png>)

K≤k≤K+x/qr (k,q)=1

after a small calculation. Further, by Lemma 2 we have log Fq(2qr/ log N) ≤

qr log √N

qr log √N

- 1

![image 144](<2020-peluse-almost-all-entries-character_images/imageFile144.png>)

- 2


- 1

![image 145](<2020-peluse-almost-all-entries-character_images/imageFile145.png>)

- 2 log q


2

+

+

log

log

![image 146](<2020-peluse-almost-all-entries-character_images/imageFile146.png>)

![image 147](<2020-peluse-almost-all-entries-character_images/imageFile147.png>)

![image 148](<2020-peluse-almost-all-entries-character_images/imageFile148.png>)

![image 149](<2020-peluse-almost-all-entries-character_images/imageFile149.png>)

qr log

- 1

![image 150](<2020-peluse-almost-all-entries-character_images/imageFile150.png>)

- 2 log q


r 2

2

√

≤

log

log q + O(1), and combining this with the lower bound of Lemma 3 we obtain

+

![image 151](<2020-peluse-almost-all-entries-character_images/imageFile151.png>)

![image 152](<2020-peluse-almost-all-entries-character_images/imageFile152.png>)

![image 153](<2020-peluse-almost-all-entries-character_images/imageFile153.png>)

N

1 8

log q + O(1)

![image 154](<2020-peluse-almost-all-entries-character_images/imageFile154.png>)

p(qr) Fq(2qr/ log N) ≥

qr log

r2 2

- 1

![image 155](<2020-peluse-almost-all-entries-character_images/imageFile155.png>)

- 2 log q


2

√

− r log(qr) + O(1)

log q −

log

log

![image 156](<2020-peluse-almost-all-entries-character_images/imageFile156.png>)

![image 157](<2020-peluse-almost-all-entries-character_images/imageFile157.png>)

![image 158](<2020-peluse-almost-all-entries-character_images/imageFile158.png>)

![image 159](<2020-peluse-almost-all-entries-character_images/imageFile159.png>)

N

log √N qr −

√

![image 160](<2020-peluse-almost-all-entries-character_images/imageFile160.png>)

- 1

![image 161](<2020-peluse-almost-all-entries-character_images/imageFile161.png>)

- 2 log q


![image 162](<2020-peluse-almost-all-entries-character_images/imageFile162.png>)

N)2 + O(1). Using this and (7) in (6), and recalling that r = ⌊(log √N)/(eq)⌋, we conclude that ∆ ≫ N

(log log

= r log

![image 163](<2020-peluse-almost-all-entries-character_images/imageFile163.png>)

![image 164](<2020-peluse-almost-all-entries-character_images/imageFile164.png>)

√

- 1

![image 165](<2020-peluse-almost-all-entries-character_images/imageFile165.png>)

- 2 log q


- 1

![image 166](<2020-peluse-almost-all-entries-character_images/imageFile166.png>)

- 2eq−101q exp −


1

![image 167](<2020-peluse-almost-all-entries-character_images/imageFile167.png>)

N)2 − log log N ≫ N

12q.

(log log

![image 168](<2020-peluse-almost-all-entries-character_images/imageFile168.png>)

![image 169](<2020-peluse-almost-all-entries-character_images/imageFile169.png>)

Using this in (5), we conclude that the number of partitions µ for which µ has largest part below

√6N

![image 170](<2020-peluse-almost-all-entries-character_images/imageFile170.png>)

2π (log N)(1 + 1/(5q)) is ≪ p(N)N

![image 171](<2020-peluse-almost-all-entries-character_images/imageFile171.png>)

1

- 3

![image 172](<2020-peluse-almost-all-entries-character_images/imageFile172.png>)

- 4 exp(−∆) ≤ p(N) exp − N


15q , establishing Proposition 2.

![image 173](<2020-peluse-almost-all-entries-character_images/imageFile173.png>)

References

- [1] N. G. de Bruijn. On Mahler’s partition problem. Nederl. Akad. Wetensch., Proc., 51:659–669 = Indagationes Math. 10, 210–220 (1948), 1948.
- [2] P. Erdo˝s and J. Lehner. The distribution of the number of summands in the partitions of a positive integer. Duke Math. J., 8:335–345, 1941.
- [3] P. Flajolet and R. Sedgewick. Analytic combinatorics. Cambridge University Press, Cambridge, 2009.
- [4] W. Fulton and J. Harris. Representation theory, volume 129 of Graduate Texts in Mathematics. SpringerVerlag, New York, 1991. A ﬁrst course, Readings in Mathematics.
- [5] D. Gluck. Parity in columns of the character table of Sn. Proc. Amer. Math. Soc., 147(3):1005–1011,

- 2019.

[6] M. Larsen and A. R. Miller. The sparsity of character tables of high rank groups of Lie type. preprint,

- 2020. arXiv:2006.00847.


- [7] K. Mahler. On a special functional equation. J. London Math. Soc., 15:115–123, 1940.
- [8] A. Malik, F. Stan, and A. Zaharescu. The Siegel norm, the length function and character values of ﬁnite groups. Indag. Math. (N.S.), 25(3):475–486, 2014.
- [9] J. McKay. Irreducible representations of odd degree. J. Algebra, 20:416–418, 1972.
- [10] A. R. Miller. The probability that a character value is zero for the symmetric group. Math. Z., 277(34):1011–1015, 2014.
- [11] A. R. Miller. On parity and characters of symmetric groups. J. Combin. Theory Ser. A, 162:231–240, 2019.
- [12] L. Morotti. On divisibility by primes in columns of character tables of symmetric groups. Arch. Math. (Basel), 114(4):361–365, 2020.
- [13] A. M. Odlyzko and E. M. Rains. On longest increasing subsequences in random permutations. In Analysis, geometry, number theory: the mathematics of Leon Ehrenpreis (Philadelphia, PA, 1998), volume 251 of Contemp. Math., pages 439–451. Amer. Math. Soc., Providence, RI, 2000.
- [14] S. Peluse. On even entries in the character table of the symmetric group. preprint, 2020. arXiv:2007.06652.
- [15] H. Rademacher. On the Partition Function p(n). Proc. London Math. Soc. (2), 43(4):241–254, 1937.
- [16] A. M. Vershik and S. V. Kerov. Asymptotic behavior of the maximum and generic dimensions of irreducible representations of the symmetric group. Funktsional. Anal. i Prilozhen., 19(1):25–36, 96, 1985.


School of Mathematics, Institute for Advanced Study, Princeton, NJ 08540, USA Department of Mathematics, Princeton University, Princeton, NJ 08540, USA Email address: speluse@princeton.edu Department of Mathematics, Stanford University, Stanford, CA 94305, USA Email address: ksound@stanford.edu

