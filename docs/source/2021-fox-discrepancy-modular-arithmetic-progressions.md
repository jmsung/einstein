---
type: source
kind: paper
title: Discrepancy in modular arithmetic progressions
authors: Jacob Fox, Max Wenqiang Xu, Yunkun Zhou
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2104.03929v1
source_local: ../raw/2021-fox-discrepancy-modular-arithmetic-progressions.pdf
topic: general-knowledge
cites:
---

DISCREPANCY IN MODULAR ARITHMETIC PROGRESSIONS

JACOB FOX, MAX WENQIANG XU, AND YUNKUN ZHOU

arXiv:2104.03929v1[math.CO]8Apr2021

Abstract. Celebrated theorems of Roth and of Matousˇek and Spencer together show that the discrepancy of arithmetic progressions in the ﬁrst n positive integers is Θ(n1/4). We study the analogous problem in the Zn setting. We asymptotically determine the logarithm of the discrepancy of arithmetic progressions in Zn for all positive integer n. We further determine up to a constant factor the discrepancy of arithmetic progressions in Zn for many n. For example, if n = pk is a prime power, then the discrepancy of arithmetic progressions in Zn is Θ(n1/3+rk/(6k)), where rk ∈ {0, 1, 2} is the remainder when k is divided by 3. This solves a problem of Hebbinghaus and Srivastav.

1. Introduction

Given a ﬁnite set Ω, a (two-)coloring of Ω is a map χ : Ω → {1,−1}, and a partial coloring is a map χ : Ω → {−1,0,1}. For A ⊆ Ω, let χ(A) = x∈A χ(x). For a family A of subsets of Ω, the discrepancy of A is deﬁned to be

disc(A) := min

|χ(A)|,

max

χ

A∈A

where the minimum is over all colorings of Ω. The discrepancy measures the guaranteed irregularity of colorings with respect to a set system. Discrepancy theory is a rich area of study, see the books [1,3,4,9]. In particular, the study of discrepancy of arithmetic progressions has a long history, including notable results of Weyl from 1916 [13] and Roth from 1964 [11]. Let [n] := {1,2,3,... ,n} and A be the set of arithmetic progressions in [n]. Using Fourier analysis, Roth [11] proved that there is an absolute constant c > 0 such that

disc(A) ≥ cn14.

![image 1](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile1.png>)

The exponent 1/4 was unexpected, as random colorings suggest that the best exponent might be 1/2. Later, improving on a result of Montgomery and Sa´rk¨ozy (see Problem 10 in [5]), Beck [2] proved that Roth’s lower bound is sharp up to a polylogarithmic factor. It was a big challenge to remove the polylogarithmic factor and show that Roth’s bound is sharp up to a constant factor, and it was ﬁnally done by Matousˇek and Spencer [10] via entropy and partial coloring methods.

The modular variant is also a very natural problem to study. For a positive integer n, an arithmetic progression in Zn is a set of the form {a + kd : 0 ≤ k < l} for any a,d ∈ Zn and l ≥ 0. To avoid repeated elements in the set, we may assume that l ≤ gcd(nn,d). Let An be the set of all arithmetic progressions in Zn. The quantity we are interested in is

![image 2](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile2.png>)

|χ(A)|.

disc(An) := min

max

A∈An

χ:Zn→{1,−1}

![image 3](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile3.png>)

Fox is supported by a Packard Fellowship and by NSF award DMS-1855635. Xu is supported by the Cuthbert C. Hurd Graduate Fellowship in the Mathematical Sciences, Stanford. Zhou is supported by NSF GRFP Grant DGE-1656518.

1

In the case where n = p is a prime, the following lower and upper bounds are proved by Hebbinghaus and Srivastav [7] and Alon and Spencer (Theorem 13.1.1 in [1]) respectively. There exist positive constants c1,c2 such that

c1√p ≤ disc(Ap) ≤ c2 plog p. Hebbinghaus and Srivastav [7] wrote that it seemed to be a diﬃcult open problem to close the O(√log p) multiplicative gap between the upper and lower bounds. As part of our results, we remove the √log p factor in the upper bound and resolve the problem of determining disc(Ap) up to a constant factor.

![image 4](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile4.png>)

![image 5](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile5.png>)

![image 6](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile6.png>)

![image 7](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile7.png>)

The problem for general Zn is more challenging and interesting. Note that any arithmetic progression in [n] is also an arithmetic progression in Zn, so Roth’s lower bound from the integer case also applies. As the number of sets in An is polynomial in n, considering a random coloring gives the following upper bound (see Theorem 13.1.1 in [1]). So there are c1,c2 > 0 such that

c1n14

≤ disc(An) ≤ c2n21(log n)21.

![image 8](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile8.png>)

![image 9](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile9.png>)

![image 10](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile10.png>)

Our main theorem asymptotically determines the logarithm of disc(An). It shows that disc(An) depends heavily on the arithmetic structure of n, and neither of the above bounds are sharp.

Let ω(n) be the number of distinct prime factors of n and d(n) be the number of divisors of n.

- Theorem 1.1. There exists an absolute constant c > 0 such that for any positive integer n, 1

![image 11](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile11.png>)

8 d(n) · min

![image 12](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile12.png>)

r|n

n r

![image 13](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile13.png>)

+ √r ≤ disc(An) ≤ min

![image 14](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile14.png>)

r|n

n r

![image 15](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile15.png>)

+ c√r · 2ω(r) .

![image 16](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile16.png>)

Note that we have 2ω(r) ≤ 2ω(n) ≤ d(n) = no(1) (see [6]). This implies that

disc(An) = n13+x+o(1), where x ≥ 0 is the largest real number such that there is no factor of n in the range (n32−x,n32+2x). Thus, our results determine the correct exponent of n for disc(An) up to o(1).

![image 17](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile17.png>)

![image 18](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile18.png>)

![image 19](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile19.png>)

Notice that when n has a bounded number of factors, Theorem 1.1 determines disc(An) up to a constant factor. In particular, when n is prime, we have disc(An) = Θ(n1/2), and this solves the problem of Hebbinghaus and Srivastav [7] discussed earlier.

We actually prove slightly stronger bounds, but we choose the formulation in Theorem 1.1 for simplicity. These stronger bounds give the following sharp bound for disc(An) when n is a prime power.

- Theorem 1.2. If n = pk for prime p and positive integer k, then


2 = Θ n31+r6kk , where rk ∈ {0,1,2} is the remainder when k is divided by 3.

k−⌊k/3⌋

disc(An) = Θ p

![image 20](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile20.png>)

![image 21](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile21.png>)

![image 22](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile22.png>)

Remark 1.3. It is also natural to study the discrepancy problem in the case where the coloring function χ is allowed to take any value in the unit circle in the complex plane {z ∈ C : |z| = 1}. For example, this choice of coloring functions is studied in Tao’s [12] remarkable solution to the Erd˝os discrepancy problem. By comparing the deﬁnitions of the coloring functions, we know that the discrepancy under the more general choice of χ is at most as large as the discrepancy under the choice χ : Zn → {1,−1}. We remark that our proof is robust enough to give the same lower bound on discrepancy when χ is under the above choice. See Remark 4.8 for details on how to extend the proof of the lower bound to the more general setting.

Notations. Throughout the paper, all logarithms are base e unless otherwise speciﬁed.

We use symbols c,c0,c1,c2, etc. to denote absolute constants. To avoid using too many symbols in diﬀerent parts of the paper, we reuse these symbols to denote diﬀerent constants. We make no attempt to optimize constant factors in our results.

We treat elements in Zn as if they are in Z in the following ways. For an element r ∈ Zn and integers a,b ∈ Z, we say a ≤ r ≤ b if there exists an element r′ ∈ Z such that a ≤ r′ ≤ b and r′ ≡ r (mod n). The notation is similar if either ≤ is replaced with <. We typically use it when 0 ≤ a ≤ b < n, so this notation should not cause any confusion. For any a ∈ Zn, we may also deﬁne gcd(a,n) = gcd(a′,n) for any a′ ∈ Z with a′ ≡ a (mod n). For two nonnegative integers a and b, we write a|b if a divides b. For any factor r of n and a ∈ Zn, we say that r|a if r|gcd(a,n).

Organization. In Section 2, we derive our ﬁrst upper bound on disc(An) (see Corollary 2.3). The upper bounds in Theorems 1.1 and 1.2 are proved in Section 3 (see Theorem 3.1). In Section 4, we prove the lower bounds in Theorem 1.1 (Corollary 4.9) and Theorem 1.2 (Corollary 4.10). We end with some concluding remarks and open problems in Section 5.

2. The First Step towards the Upper Bounds

We use the following version of a lemma of Matousˇek and Spencer [10] to show there is a partial coloring that colors a constant fraction of the elements of a set system with low discrepancy. The proof of this lemma uses the entropy method.

- Lemma 2.1 (Section 4.6 in [9]). Let (V,C) be a set system on n elements, and let a number ∆S ≥ 2 |S| be given for each set S ∈ C. If

![image 23](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile23.png>)

S∈C:S =∅

exp −

∆2S 4|S|

![image 24](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile24.png>)

≤

n 50

![image 25](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile25.png>)

, (2.1)

then there is a partial coloring χ that assigns ±1 to at least n/10 variables (and 0 to the rest) satisfying |χ(S)| ≤ ∆S for each S ∈ C.

The following lemma shows that there is a partial coloring of a constant fraction of any subset X of Zn such that modular arithmetic progressions have low discrepancy. The proof utilizes the previous lemma applied to a special family of intersections of X with modular arithmetic progressions. Each set in this special family has size a power of 2. We show that any set which is an intersection of X with a modular arithmetic progression can be written as the union of two sets, and each of them is a set diﬀerence of two sets that each has a canonical decomposition into sets of diﬀerent sizes from this special family. We obtain the lemma by putting these together and using the triangle inequality.

- Lemma 2.2. Let X ⊆ Zn be a set of size m > 0. There exists a partial coloring χ : X → {−1,0,1} that assigns ±1 to at least m/10 elements in X such that


- 1

![image 26](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile26.png>)

- 2 .


en m

|χ(A ∩ X)| ≤ 200m12 log

max

![image 27](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile27.png>)

![image 28](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile28.png>)

A∈An

Proof. Let APn(a,d,i,j) := {a + kd : i ≤ k ≤ j} where a,d ∈ Zn and i,j ∈ Z. By deﬁnition, An = APn(a,d,0,l − 1) : a,d ∈ Zn,0 ≤ l ≤

n gcd(n,d)

.

![image 29](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile29.png>)

Consider the following decomposition of sets in An. Let C1 = APn(a,d,i,j) : 1 ≤ d < n,0 ≤ a < gcd(n,d),0 ≤ i ≤ j <

n gcd(n,d)

![image 30](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile30.png>)

.

Now we show that any set A ∈ An can be written as the disjoint union of at most two sets in C1. For any set A = APn(a,d,0,l − 1) with a,d ∈ Zn and 0 ≤ l ≤ gcd(nn,d), we may assume that l > 0, or otherwise it is an empty set. If d = 0, then the set is the singleton {a}, which is also APn(0,1,a,a) ∈ C1 by choosing i,j to be the integer representative of a in the range [0,n). Now we may assume 1 ≤ d < n. Note that {kd : 0 ≤ k < gcd(nn,d)} splits Zn into gcd(nn,d) equal-sized intervals, so there is some 0 ≤ k < gcd(nn,d) such that 0 ≤ a − kd < gcd(n,d). Deﬁne a′ = a − kd, and we have

![image 31](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile31.png>)

![image 32](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile32.png>)

![image 33](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile33.png>)

![image 34](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile34.png>)

APn(a,d,0,l − 1) = APn(a′,d,k,k + l − 1).

Moreover we have k < gcd(nn,d) and l − 1 < gcd(nn,d), so 0 ≤ k + l − 1 < 2gcd(nn,d). If k + l − 1 < gcd(nn,d), then APn(a′,d,k,k + l − 1) ∈ C1. If k + l − 1 ≥ gcd(nn,d), then we may write

![image 35](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile35.png>)

![image 36](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile36.png>)

![image 37](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile37.png>)

![image 38](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile38.png>)

![image 39](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile39.png>)

n gcd(n,d) − 1 ∪ APn a′,d,0,k + l − 1 −

n gcd(n,d)

APn(a′,d,k,k + l − 1) = APn a′,d,k,

.

![image 40](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile40.png>)

![image 41](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile41.png>)

Hence we know that for any partial coloring χ : Zn → {−1,0,1}, we always have max

|χ(A ∩ X)| ≤ 2 max

|χ(A ∩ X)|. (2.2)

A∈C1

A∈An

Now we study the sets in CX := {A ∩ X : A ∈ C1}. By deﬁnition we have max

|χ(A ∩ X)| = max

|χ(B)|. (2.3)

A∈C1

B∈CX

For each 1 ≤ d < n and 0 ≤ a < gcd(n,d), we deﬁne Ad,a = a + kd : 0 ≤ k < gcd(nd,n) , and deﬁne Xd,a = Ad,a∩X. Since each element x in Xd,a is associated to an integer 0 ≤ k < gcd(nd,n) via the relation x = a+kd, we may order elements in Xd,a in ascending order of k. We write Xd,a = x(1)d,a,... ,xd,a(ld,a) , where ld,a = |Xd,a|. For integers i and j, we deﬁne Xd,a(i,j) = x(d,at) : i ≤ t ≤ j . For each d ∈ Zn, because each element of Zn is in exactly one Ad,a for 0 ≤ a < gcd(d,n), we have

![image 42](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile42.png>)

![image 43](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile43.png>)

gcd(d,n)−1

gcd(d,n)−1

|X ∩ Ad,a| = |X| = m. (2.4)

ld,a =

a=0

a=0

′)

For A = APn(a,d,i,j), if we take i′ to be the smallest index such that x(i

d,a = a + k1d with k1 ≥ i (or ld,a + 1 if no such index with 0 ≤ k1 < gcd(nd,n) exists), and j′ to be the largest index such that x(j

![image 44](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile44.png>)

′)

d,a = a + k2d with k2 ≤ j (or 0 if no such index with 0 ≤ k2 < gcd(nd,n) exists), then we have A ∩ X = Xd,a(i′,j′). Hence each nonempty set in CX is of the form Xd,a(i,j) with 1 ≤ i ≤ j ≤ ld,a. Therefore we may write

![image 45](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile45.png>)

CX = {Xd,a(i,j) : 1 ≤ d < n,0 ≤ a < gcd(n,d),1 ≤ i ≤ j ≤ ld,a} ∪ {∅}. Now we further decompose sets in CX into canonical sets. Formally,

C2 := Xd,a(1 + (t − 1)2i,t2i) : 1 ≤ d < n,0 ≤ a < gcd(n,d),0 ≤ i,1 ≤ t ≤

ld,a 2i

![image 46](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile46.png>)

. (2.5)

Notice that each set S ∈ CX can be written as U \ V with V ⊆ U where both U and V can be written as the disjoint union of sets in C2 of diﬀerent sizes. This is trivially true for the empty set. For S = Xd,a(i,j), we may take U = Xd,a(1,j) and V = Xd,a(1,i − 1). If we write j in binary form 2b1 + 2b2 + ··· + 2bs for b1 > b2 > ··· > bs, then U is the disjoint union of sets of the form Xd,a(1 + tk−=11 2bk, tk=1 2bk) for t = 1,... ,s. We can decompose V similarly.

Note that sets in C2 are all of size 2i for 2i ≤ m. If χ : X → {−1,0,1} is such that for all 0 ≤ i ≤ log2 m we have χ(S) ≤ ∆i for any set S ∈ C2 of size 2i, then by using the decomposition property above we have

|χ(B)| ≤ 2

max

∆i. (2.6)

B∈CX

0≤i≤log2 m

For each i, we upper bound the number of sets in C2 of size 2i as following. For each 1 ≤ d < n and 0 ≤ a < gcd(d,n), the number of choices of t in (2.5) is ⌊ld,a/2i⌋. By (2.4) the number of such sets is at most

gcd(d,n)−1

gcd(d,n)−1

n−1

n−1

ld,a 2i ≤

ld,a 2i

(n − 1)m 2i

=

. (2.7)

![image 47](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile47.png>)

![image 48](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile48.png>)

![image 49](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile49.png>)

a=0

a=0

d=1

d=1

Now we deﬁne b(0) = 0 and for 0 < s ≤ n,

b(s) = 5√s log

en s

1/2

![image 50](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile50.png>)

. (2.8)

![image 51](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile51.png>)

From the deﬁnition, we know that b(s) ≥ 2√s for all s ∈ N. We want to show that there exists a partial coloring χ that colors at least m/10 elements in X, and for any S ∈ C2,

![image 52](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile52.png>)

|χ(S)| ≤ b(|S|). (2.9) In order to apply Lemma 2.1 to X and C = C2, it remains to check that

b(|S|)2 4|S|

exp −

![image 53](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile53.png>)

S∈C2

From the deﬁnition of b(·) in (2.8), we know that

b(|S|)2 4|S|

e−254

exp −

·

=

![image 54](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile54.png>)

![image 55](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile55.png>)

S∈C2

S∈C2

Using the bound in (2.7), we have

≤ m/50. (2.10)

|S| n

![image 56](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile56.png>)

25 4

![image 57](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile57.png>)

≤ e−6 ·

S∈C2

|S| n

![image 58](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile58.png>)

2

. (2.11)

S∈C2

|S| n

![image 59](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile59.png>)

2

(n − 1)m 2i

≤

![image 60](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile60.png>)

0≤i≤log2 m

2i n

![image 61](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile61.png>)

2

≤ 2m.

Put this into (2.11). We get

b(|S|)2 4|S|

exp −

![image 62](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile62.png>)

S∈C2

≤ e−6 · 2m ≤ m/50.

This shows that (2.10) holds. By Lemma 2.1, we conclude that there exists a partial coloring χ : X → {−1,0,1} that assigns ±1 to at least m/10 elements, and (2.9) holds for any S ∈ C2. Thus in (2.6) we may take ∆i = b(2i) for 0 ≤ i ≤ log2 m.

It remains to show that χ satisﬁes the desired property. By (2.2), (2.3), and (2.6),

⌊log2 m⌋

en 2i

2i/2 log

b(2i) = 20

|χ(A ∩ X)| ≤ 4

max

![image 63](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile63.png>)

A∈An

i=0

0≤i≤log2 m

- 1

![image 64](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile64.png>)

- 2 ≤ 200 ·


√m log

en m

![image 65](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile65.png>)

![image 66](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile66.png>)

- 1

![image 67](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile67.png>)

- 2 .


To obtain the last inequality, observe that the sum is roughly a geometric series with ratio 21/2 (although there is an extra logarithmic factor that slightly complicates this) and can be bounded by a constant factor times the largest term. A careful analysis gives the claimed bound.

Hence the partial coloring χ satisﬁes the desired inequality. Corollary 2.3. Let X ⊆ Zn be a set of size m > 0. There exists an absolute constant c such that there is a coloring χ : X → {−1,1} satisfying

- 1

![image 68](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile68.png>)

- 2 .


en m

|χ(A ∩ X)| ≤ cm21 log

max

![image 69](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile69.png>)

![image 70](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile70.png>)

A∈An

In particular, for X = Zn, we have

disc(An) = O(√n). Proof. The main idea is to iteratively apply Lemma 2.2 to the set of uncolored elements of X until all elements of X are colored. Start with X0 = X. For each i ≥ 0, we apply Lemma 2.2 to Xi to get a partial coloring χi : Xi → {−1,0,1}, and we let Xi+1 = χ−i 1(0) ⊆ Xi to be the set of uncolored elements in i-th iteration. We continue this process until the k-th iteration where all elements are colored (i.e. Xk+1 = ∅). Let χ be the ﬁnal coloring given by χ(xi) = χi(xi) if xi ∈ Xi \ Xi+1 for 0 ≤ i ≤ k. We know that |Xi| ≤ 0.9|Xi−1| for all 1 ≤ i ≤ k, so |Xi| ≤ (0.9)i|X0| = (0.9)im. Moreover, we know that for any A ∈ An, noting that x1/2 · log enx

![image 71](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile71.png>)

- 1

![image 72](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile72.png>)

- 2 is monotonically increasing for real number x ∈ (0,n],


![image 73](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile73.png>)

- 1

![image 74](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile74.png>)

- 2


k

k

k

n e|Xi|

200 · |Xi|1

|χi(Xi ∩ A)| <

χi(Xi ∩ A) ≤

|χ(A ∩ X)| =

2 log

![image 75](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile75.png>)

![image 76](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile76.png>)

i=0

i=0

i=0

- 1

![image 77](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile77.png>)

- 2


k

- 1

![image 78](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile78.png>)

- 2


en m

en (0.9)im

(0.9)2i log

< cm12 log

≤ 200m12

·

![image 79](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile79.png>)

![image 80](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile80.png>)

![image 81](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile81.png>)

![image 82](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile82.png>)

![image 83](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile83.png>)

i=0

for some appropriate choice of the absolute constant c.

3. Upper Bounds

By Corollary 2.3, we have disc(An) = O(√n). In this section, we prove the following upper bound on the same quantity, which shows that the previous bound is not always tight, and that disc(An) depends on the factorization of n. Recall that ω(r) denotes the number of distinct prime factors of r.

![image 84](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile84.png>)

- Theorem 3.1. There exists an absolute constant c > 0 such that for any positive integer n, we have


+ c√r · 2ω(r) .

n r

![image 85](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile85.png>)

disc(An) ≤ min

![image 86](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile86.png>)

r|n

The proof of Theorem 3.1 consists of two steps. The ﬁrst key step is to establish an upper bound on disc(An) using a coloring of Zr where r divides n that simultaneously has low discrepancy with respect to two particular families of arithmetic progressions in Zr. This is achieved by Lemma 3.2. To accomplish this, we need to introduce a special type of arithmetic progression in Zn. Recall that An

is the set of all arithmetic progressions in Zn. We deﬁne A0n to be the set of all congruence classes of Zn. Formally, for any r,i ∈ Zn, let

C(r,i) := {x ∈ Zn : x ≡ i (mod r)} and

A0n := {C(r,i) : r,i ∈ Zn}. In particular we know that A0n ⊆ An. In Lemma 3.2 we obtain an upper bound on disc(An) if there is an r that divides n and a coloring χ of Zr that has low discrepancy over both Ar and A0r. The second step is to ﬁnd a coloring of Zr which has nearly optimal discrepancy over Ar and A0r simultaneously. Finally we will complete the proof by applying Lemma 3.2 with this coloring of Zr.

- Lemma 3.2. Let n be a positive integer and r be a positive factor of n. For any χ : Zr → {1,−1},


n r · max

|χ(A0)|.

|χ(A)| +

disc(An) ≤ max A∈Ar

![image 87](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile87.png>)

A0∈A0r

Proof. Let m = n/r. For the subgroup (m) ⊆ Zn, we have a quotient map τ : Zn → Zn/(m) = Zr given by τ(x) = x = x + (m). Suppose we are given an arbitrary χ : Zr → {1,−1}. Now we deﬁne χ′ = χ ◦ τ : Zn → {1,−1}. It suﬃces to show

![image 88](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile88.png>)

|χ′(A′)| ≤ max A∈Ar

|χ(A)| + m · max

|χ(A0)|. (3.1)

max

A′∈An

A0∈A0r

Let A′ = {a + kd : 0 ≤ k < L} for some a,d ∈ Zn be an arithmetic progression in Zn of length L. We may assume that L ≤ n/gcd(d,n) so that there is no repeated element in A′.

![image 89](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile89.png>)

![image 90](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile90.png>)

![image 91](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile91.png>)

Let L0 = r/gcd(r,d) where d = τ(d). For any integer t > 0, we know that {a + kd : t ≤ k < t + L0} is a set of size L0 in A0n, as it covers each element in the congruence class exactly once. For any 0 ≤ l < L0, as the set {a + kd : t ≤ k < t + l} has no repeated element, it is a set of size l in An.

![image 92](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile92.png>)

![image 93](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile93.png>)

![image 94](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile94.png>)

Now we may write L = qL0 + r for some integers q and 0 ≤ r < L0. We know that q ≤

L L0 ≤

n/gcd(d,n) r/gcd(r,d)

gcd(r,d) gcd(n,d) ≤ m.

= m ·

![image 95](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile95.png>)

![image 96](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile96.png>)

![image 97](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile97.png>)

![image 98](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile98.png>)

Applying the triangle inequality, we get

|χ′(A′)| =

L−1

χ′(a + kd) =

k=0

L−1

![image 99](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile99.png>)

χ(a + kd) =

![image 100](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile100.png>)

k=0

(t+1)L0−1

qL0+r−1

q−1

![image 101](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile101.png>)

![image 102](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile102.png>)

χ(a + kd) +

χ(a + kd)

![image 103](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile103.png>)

![image 104](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile104.png>)

t=0

k=qL0

k=tL0

q−1

≤

t=0

(t+1)L0−1

![image 105](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile105.png>)

χ(a + kd) +

![image 106](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile106.png>)

k=tL0

qL0+r−1

![image 107](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile107.png>)

χ(a + kd)

![image 108](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile108.png>)

k=qL0

|χ(A)|.

|χ(A0)| + max A∈Ar

|χ(A)| ≤ m · max

|χ(A0)| + max A∈Ar

≤ q · max

A0∈A0r

A0∈A0r

Since the bound is uniform for all A′ ∈ An, we conclude that (3.1) holds. After the above deduction, the second step is to ﬁnd a coloring χ : Zn → {1,−1} that has nearly optimal discrepancy over An and A0n simultaneously. Formally we have the following statement.

- Lemma 3.3. There exists an absolute constant c > 0 such that the following holds. Suppose that n is a positive integer with k distinct prime factors. Then there exists χ : Zn → {1,−1} such that


|χ(A)| ≤ c√n · 2k.

![image 109](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile109.png>)

|χ(A0)| ≤ 1 and max A∈An

max

A0∈A0n

We can now deduce Theorem 3.1 from the above two steps. Proof of Theorem 3.1 assuming Lemma 3.3. For any positive factor r of n, by Lemma 3.3, there is a coloring χ of Zr such that

|χ(A)| ≤ c√r · 2ω(r),

![image 110](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile110.png>)

|χ(A0)| ≤ 1 and max A∈Ar

max

A0∈A0r

where c is an absolute constant. Then applying Lemma 3.2, we conclude that disc(An) ≤

+ c√r · 2ω(r). As this holds for all positive factors r of n, the desired result follows. It remains to prove Lemma 3.3. We ﬁrst present a proof of the case that n is a prime power. The proof of this case is simpler and illustrates the main ideas in the proof of Lemma 3.3.

n r

![image 111](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile111.png>)

![image 112](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile112.png>)

- Lemma 3.4. There exists absolute constant c > 0 such that the following holds. Let n = pα for some prime p and positive integer α. Then there exists χ : Zn → {1,−1} such that

max

A0∈A0n

|χ(A0)| ≤ 1 and max A∈An

|χ(A)| ≤ c√n.

![image 113](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile113.png>)

To ﬁnd a coloring with low discrepancy over A0n, the main idea is to color simultaneously two disjoint subsets S1 and S2 of Zn that are translations of each other, and we hope that χ(S1∩A0) and χ(S2∩A0) cancel out for many A0 ∈ A0n. The c√n upper bound on the discrepancy over An in Lemma 3.4 is achieved via Corollary 2.3. We ﬁrst derive the following lemma that gives a desired coloring for a subset X of Zn, provided that X is an initial interval of some special length.

![image 114](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile114.png>)

- Lemma 3.5. There exists absolute constant c > 0 such that the following holds. Let n = pα for some


prime p and positive integer α. Suppose that X = {0,... ,m − 1} ⊆ Zn for some m ≤ n satisﬁes that m = spβ with s even and β being a nonnegative integer. Then there exists χ : X → {1,−1} such that

- 1

![image 115](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile115.png>)

- 2 ,


|χ(A ∩ X)| ≤ c√m log

en m

![image 116](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile116.png>)

max

![image 117](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile117.png>)

A∈An

and for any w ∈ Zn and r = pγ with 0 ≤ γ ≤ β, χ(C(r,w) ∩ X) = 0.

Proof. Let S = {0,... ,m/2 − 1}. By Corollary 2.3, there is χ0 : X → {1,−1} such that

- 1

![image 118](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile118.png>)

- 2


![image 119](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile119.png>)

m 2

2en m

|χ0(A ∩ S)| ≤ c0

,

log

![image 120](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile120.png>)

![image 121](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile121.png>)

holds for any A ∈ An, where c0 is an absolute constant. We know that X is the disjoint union of S and S + m2 , i.e. each element x ∈ X is of the form x = s + vm2 for some s ∈ S and v ∈ {0,1}. We deﬁne χ : X → {1,−1} given by χ(s + vm2 ) = (−1)v · χ0(s) for any s ∈ S and v ∈ {0,1}. For any A ∈ An, noting that A − m2 is also an arithmetic progression,

![image 122](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile122.png>)

![image 123](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile123.png>)

![image 124](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile124.png>)

![image 125](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile125.png>)

|χ(A ∩ X)| = |χ(A ∩ S) + χ(A ∩ (S + m/2))| = |χ0(A ∩ S) + (−1) · χ0((A − m/2) ∩ S)|

- 1

![image 126](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile126.png>)

- 2


- 1

![image 127](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile127.png>)

- 2 ,


≤ c√m log

![image 128](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile128.png>)

2en m

m 2

en m

![image 129](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile129.png>)

≤ |χ0(A ∩ S)| + |χ0((A − m/2) ∩ S)| ≤ 2 · c0

log

![image 130](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile130.png>)

![image 131](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile131.png>)

![image 132](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile132.png>)

where c is an absolute constant. Next we verify that for any r = pγ with γ ≤ β and any w ∈ Zn, χ(C(r,w) ∩ X) = 0. Note that m/2 is a multiple of r, so C(r,w) − m/2 = C(r,w). Hence we have χ(C(r,w)∩X) = χ0(C(r,w)∩S)+(−1)·χ0((C(r,w)−m/2)∩S) = χ0(C(r,w)∩S)−χ0(C(r,w)∩S) = 0. We have thus shown the existence of such a coloring χ with the desired properties. In the case n = pα, we partition Zn into a few sets, each being an interval of Zn of length an even number times a power of p as in Lemma 3.5. Proof of Lemma 3.4. Note that for any C(r,w) ∈ A0n, we have C(r,w) = C(gcd(r,n),w). Hence it suﬃces to check |χ(C(r,w))| ≤ 1 where r divides n = pα, i.e., r = pγ for some nonnegative γ ≤ α. Let c0 be the constant in Lemma 3.5. If p = 2, we can take m = n = 2 · 2α−1 in Lemma 3.5. Thus, there exists χ : Zn → {1,−1} such that

|χ(A)| ≤ c0√n,

![image 133](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile133.png>)

max

A∈An

and that for any w ∈ Zn and any r = 2γ with γ ≤ α − 1, χ(C(r,w)) = 0. This means that, for any r = 2γ, if γ ≤ α − 1, then χ(C(r,w)) = 0; if γ = α, then C(r,w) contains a single element w, so |χ(C(r,w))| = 1 in this case. We conclude that

|χ(A0)| ≤ 1.

max

A0∈A0n

If p > 2 is an odd prime, then we partition Zn into a few intervals: X0 = {0},Xi = {x : pi−1 ≤ x < pi} for 1 ≤ i ≤ α. Note that for each i ≥ 1, Xi is an interval of length (p−1)·pi−1. We would like to apply

- Lemma 3.5 to each Xi for i ≥ 1. It is applicable because the property is maintained by translation. Therefore for each 1 ≤ i ≤ α there is a coloring χi : Xi → {1,−1} such that


- 1

![image 134](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile134.png>)

- 2


pα (p − 1) · pi−1

![image 135](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile135.png>)

|χi(A ∩ Xi)| ≤ c0 (p − 1) · pi−1 1 + log

max

,

![image 136](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile136.png>)

A∈An

and for each w ∈ Zn and r = pγ with γ ≤ i − 1, we have χi(C(r,w) ∩ Xi) = 0. For X0 we may take any arbitrary χ0 : X0 → {1,−1}. Note that X0 = {0} contains only one element, so |χ0(A ∩ X0)| ≤ 1 for all A ⊆ Zn. Since X = αi=0 Xi, we deﬁne χ : X → {1,−1} such that χ(xi) = χi(xi) for all 0 ≤ i ≤ α and xi ∈ Xi. Consequently, we know that for each A ∈ An,

1 2

α

α

pα (p − 1) · pi−1

≤ c√n

![image 137](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile137.png>)

![image 138](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile138.png>)

c0 (p − 1) · pi−1 1 + log

![image 139](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile139.png>)

|χi(A ∩ Xi)| ≤ 1 +

|χ(A)| =

![image 140](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile140.png>)

i=1

i=0

for some appropriate constant c. Moreover, for each C(r,w) ∈ A0n, we may assume that r = pγ for some 0 ≤ γ ≤ α and it gives that

γ

α

χi(C(r,w) ∩ Xi).

χ(C(r,w)) = χ C(r,w) ∩

Xi +

i=γ+1

i=0

Now, for each i ≥ γ + 1, i.e. γ ≤ i − 1, we have χi(C(r,w) ∩ Xi) = 0. Also note that γi=0 Xi is {x : 0 ≤ x < pγ}, so there is exactly one element of C(r,w) in it. Hence

γ

|χ(C(r,w))| = χ C(r,w) ∩

Xi = 1.

i=0

Thus we may conclude that

|χ(A0)| ≤ 1. Hence for both p = 2 and p is odd, we can always ﬁnd such a coloring χ. Finally we extend the argument above to arbitrary n using Chinese remainder theorem. Notations. Suppose that number n has prime factorization n = pα11 ··· pαkk. By Chinese remainder theorem, we have an isomorphism

max

A0∈A0n

→ Zn.

ψn : Zpα1

× ··· × Zpαk

1

k

Again, we ﬁrst show the following analogue of Lemma 3.5. This shows that if X ⊆ Zn has some special structure, then we have a coloring of X with low discrepancy with respect to both An and A0n.

- Lemma 3.6. Let n be a positive integer with prime factorization n = pα11 ··· pαkk. For each 1 ≤ i ≤ k, let Ti ≤ pαi i be a positive integer. Let X = {ψn(t1,... ,tk) : 0 ≤ ti < Ti for all 1 ≤ i ≤ k}. Then X ⊆ Zn is a set of m = ki=1 Ti elements. Suppose that I ⊆ [k] is a subset of indices and (βi)i∈I is a sequence of nonnegative integers, such that for each i ∈ I, Ti = sipβi i for some even number si. Then there exists a coloring χ : X → {−1,1} such that the following holds. Its discrepancy over An satisﬁes that


- 1

![image 141](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile141.png>)

- 2 , (3.2)


√m |I| + 1 + log

n m

|I| 2

![image 142](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile142.png>)

·

|χ(A ∩ X)| ≤ c2

max

![image 143](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile143.png>)

![image 144](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile144.png>)

A∈An

and for any w ∈ Zn and any i ∈ I,

χ(C(n/pαi i−βi,w) ∩ X) = 0. (3.3)

Proof. Let L = |I|. Let Si = Ti/2 if i ∈ I, and Si = Ti otherwise. For each i ∈ I, from the condition that Ti/pβi i is even, we know that Si is a multiple of pβi i. We deﬁne

X0 = {ψn(t1,... ,tk) : 0 ≤ ti < Si for all 1 ≤ i ≤ k}.

We know that X0 ⊆ Zn is a set of size m/2L. Next we apply Corollary 2.3 to get the constant c0 > 0 and a partial coloring of χ0 : X0 → {−1,1} such that

- 1

![image 145](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile145.png>)

- 2


2Ln m

- 1

![image 146](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile146.png>)

- 2 ,


![image 147](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile147.png>)

![image 148](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile148.png>)

m 2L

m 2L

n m

|χ0(X0 ∩ A)| ≤ c0

≤ c

max

L + 1 + log

1 + log

![image 149](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile149.png>)

![image 150](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile150.png>)

![image 151](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile151.png>)

![image 152](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile152.png>)

A∈An

where c is another absolute constant. For each v = (vi)i∈I ∈ {0,1}I (binary tuples of length L indexed by I), we deﬁne sgn(v) = (−1) i∈I vi, and let uv ∈ Zn be the unique element, by the Chinese remainder theorem, such that

uv ≡ viSi (mod pαi i) for all i ∈ I and uv ≡ 0 (mod pαj j) for all j ∈/ I. Thus we have the decomposition of X into disjoint copies of translations of X0:

X =

Xv, where Xv := uv + X0.

v∈{0,1}I

This implies that each x ∈ X can be written in the form x = uv +x0 for some v ∈ {0,1}I and x0 ∈ X0. Now we deﬁne χ : X → {1,−1} by χ(uv + x0) = sgn(v) · χ(x0) for all v ∈ {0,1}I,x0 ∈ X0. For any

A ∈ An, noting that A − uv is also in An, so

|χ(X ∩ A)| =

χ(Xv ∩ A) =

v∈{0,1}I

sgn(v) · χ0(Xv ∩ A − uv)

v∈{0,1}I

|χ0(X0 ∩ (A − uv))| ≤ 2L max A∈An

≤

|χ0(X0 ∩ A)|

v∈{0,1}I

≤ 2L · c

![image 153](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile153.png>)

m 2L

![image 154](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile154.png>)

n m

L + 1 + log

![image 155](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile155.png>)

- 1

![image 156](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile156.png>)

- 2 = c2L2


![image 157](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile157.png>)

√m L + 1 + log

n m

![image 158](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile158.png>)

·

![image 159](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile159.png>)

- 1

![image 160](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile160.png>)

- 2 .


This shows that the coloring χ satisﬁes the condition (3.2) on the discrepancy over An.

It remains to show (3.3). For each i ∈ I, let ri = n/pαi i−βi = pα11 ··· pβi i ··· pαkk. For any i ∈ I and any w ∈ Zn, we know that C(ri,w) contains pαi−βi elements. If C(ri,w) ∩ X = ∅, then (3.3) trivially holds. It suﬃces to check χ(C(ri,w) ∩ X) = 0 for w = ψn(t1,... ,tk) ∈ Xv for some v ∈ {0,1}I. Since pαj j divides ri, each element in C(ri,w) is congruent to tj mod pαj j for j = i. This implies that C(ri,w) only has nonempty intersection with Xv and Xv′ where v,v′ ∈ {0,1}I diﬀer only at the entry indexed by i. Moreover by the deﬁnition of u, uv −uv′ is congruent to 0 mod pαj j for all j = i, and is congruent to ±s2ipβi i mod pαi i. Thus uv − uv′ is a multiple of ri, which implies C(ri,w) = C(ri,w) + (uv − uv′), or equivalently C(ri,w) − uv = C(ri,w) − uv′. Therefore we have

![image 161](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile161.png>)

χ(C(ri,w) ∩ X) = χ(C(ri,w) ∩ Xv) + χ(C(ri,w) ∩ Xv′)

= sgn(v) · χ0((C(ri,w) − uv) ∩ X0) + sgn(v′) · χ0((C(ri,w) − uv′) ∩ X0) = 0. This is true for all i ∈ I and w ∈ Zn, and thus we conclude that χ satisﬁes (3.3) as well.

We are now ready to prove Lemma 3.3. The idea is that, we partition Zn into a few subsets, one for each factor r of n, and for each of them we use Lemma 3.6 to get a coloring of this subset with low

discrepancy over An and nearly optimal discrepancy over A0n. Finally we show that the full coloring we get from combining these subset colorings satisﬁes the properties.

Proof of Lemma 3.3. Suppose that n has prime factorization n = pα11 ··· pαkk. For each 1 ≤ i ≤ k, we partition Zpαi

αi t=0

in the following way. If pi = 2, then we set Si(αi) = Zpαi

into αi + 1 intervals Si(t)

i

i

and Si(t) = {x : pti−1 ≤ x < pti}

and Si(t) = ∅ for all 0 ≤ t < αi. If pi > 2, then we set Si(0) = {0} ⊆ Zpαi

i

for 1 ≤ t ≤ αi. In particular we have |Si(t)| ≤ pti for all i and t. Moreover, for each i and t > 0, Si(t) is always an interval of length sipti−1 in Zpαi

for some even si. For each factor r = pδ11 ··· pδkk of n, we deﬁne Yr = S1(δ1) × ··· × Sk(δk) ⊆ Zpα1

i

× ··· × Zpαk

and Xr = ψn(Yr) ⊆ Zn. Since each Zpαi

1

k

is partitioned into Si(t) for 0 ≤ t ≤ αi, their product is partitioned into Yr for r divides n, so Zn is partitioned into Xr for r divides n. Because |Si(t)| ≤ pti for all i and t,

i

k

k

|Si(δi)| ≤

pδii = r. (3.4)

|Xr| = |Yr| =

i=1

i=1

For each nonempty Xr with r = pδ11 ··· pδkk, we would like to apply Lemma 3.6 to get a coloring of Xr with bounded discrepancy. Note that we can translate Yr so that all intervals Sj(δj) for 1 ≤ j ≤ k start at 0, and notice those properties from Lemma 3.6 are invariant under translation, so it is applicable to Xr. Let Ir = {i ∈ [k] : δi > 0} ⊆ [k]. We have that for each i ∈ Ir, Si(δi) is an interval of length sipβi i

for some even si and βi = δi − 1. This implies that we can ﬁnd a partial coloring χr : Xr → {−1,1} such that

- 1

![image 162](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile162.png>)

- 2


n |Xr|

|Ir| 2

![image 163](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile163.png>)

, (3.5)

|Xr| |Ir| + 1 + log

|χr(A ∩ Xr)| ≤ c02

max

![image 164](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile164.png>)

![image 165](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile165.png>)

A∈An

and for any i ∈ Ir and any w ∈ Zn, χr(C(n/pαi i−βi,w) ∩ Xr) = χr(C(n/piαi−δi+1,w) ∩ Xr) = 0. (3.6)

Having deﬁned χr as above for each nonempty Xr, we now construct χ by setting χ(xr) = χr(xr) for each xr ∈ Xr for all r that divides n. We ﬁrst show that χ has low discrepancy over An. By (3.4) we

- 1

![image 166](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile166.png>)

- 2 is increasing for


have |Xr| ≤ r. By deﬁnition we have |Ir| ≤ k. Also note that x1/2 · k + 1 + log nx x ∈ (0,n]. Combining these together, we know that for any nonempty Xr,

![image 167](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile167.png>)

1 2

- 1

![image 168](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile168.png>)

- 2 ≤ 2k2 (k + 1)21


- 1

![image 169](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile169.png>)

- 2 . (3.7)


√r k + 1 + log

√r log

n r

en r

n |Xr|

![image 170](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile170.png>)

|Ir| 2

≤ 2k2

![image 171](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile171.png>)

![image 172](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile172.png>)

![image 173](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile173.png>)

|Xr| |Ir| + 1 + log

2

![image 174](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile174.png>)

![image 175](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile175.png>)

![image 176](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile176.png>)

![image 177](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile177.png>)

![image 178](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile178.png>)

![image 179](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile179.png>)

![image 180](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile180.png>)

Combining (3.5) and (3.7), there exists an absolute constant c1 such that for each nonempty Xr, max

- 1

![image 181](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile181.png>)

- 2 ≤ c1234k ·


- 1

![image 182](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile182.png>)

- 2 . (3.8)


√r log

√r 1 + log

en r

n r

|χr(A ∩ Xr)| ≤ c02k2 (k + 1)12

![image 183](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile183.png>)

![image 184](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile184.png>)

·

![image 185](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile185.png>)

![image 186](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile186.png>)

![image 187](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile187.png>)

![image 188](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile188.png>)

![image 189](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile189.png>)

A∈An

This is also true for Xr = ∅. Moreover we know that for any r = pδ11 ··· pδkk,

- 1

![image 190](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile190.png>)

- 2


k

k

pαi i pδii

- 1

![image 191](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile191.png>)

- 2 ≤


√r 1 + log

= √n

n r

- 1

![image 192](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile192.png>)

- 2 .


pi−(αi−δi)/2 (1 + (αi − δi)log pi)

pδii/2 1 + log

![image 193](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile193.png>)

![image 194](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile194.png>)

![image 195](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile195.png>)

![image 196](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile196.png>)

i=1

i=1

Summing this over all factors r = pδ11 ··· pδkk for 0 ≤ δi ≤ αi, we have that if we set ti = αi − δi,

αk

α1

k

- 1

![image 197](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile197.png>)

- 2 ≤


√r 1 + log

√n ·

n r

- 1

![image 198](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile198.png>)

- 2


pi−(αi−δi)/2 (1 + (αi − δi)log pi)

![image 199](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile199.png>)

![image 200](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile200.png>)

···

![image 201](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile201.png>)

i=1

δ1=0

δk=0

r|n

k

= √n

![image 202](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile202.png>)

i=1

αi

p−i ti/2(1 + ti log pi)21

![image 203](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile203.png>)

ti=0

k

√n

![image 204](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile204.png>)

≤

i=1

∞

p−i ti/2(1 + ti log pi)12 .

![image 205](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile205.png>)

ti=0

Note that for p ≥ 2,

∞

p−t/2(1 + tlog p)12

f(p) :=

![image 206](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile206.png>)

t=0

is well-deﬁned and tends to 1 as p → ∞. Thus there exists an absolute constant P > 0 such that if p ≥ P, then f(p) < 214. Since there are only ﬁnitely many prime numbers less than P, we conclude that there exists an absolute constant c2 such that

![image 207](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile207.png>)

k

i=1

∞

p−i ti/2(1 + ti log pi)12 =

![image 208](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile208.png>)

ti=0

k

f(pi) ≤ c2 · 2k4 .

![image 209](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile209.png>)

i=1

Thus we have

√r 1 + log

n r

![image 210](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile210.png>)

![image 211](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile211.png>)

r|n

k

- 1

![image 212](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile212.png>)

- 2 ≤


√n

![image 213](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile213.png>)

i=1

∞

p−i ti/2(1 + ti log pi)21

![image 214](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile214.png>)

ti=0

√n. (3.9)

≤ c22k4

![image 215](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile215.png>)

![image 216](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile216.png>)

Thus for any A ∈ An, by (3.8) and (3.9),

|χ(A)| =

χr(A ∩ Xr) ≤

r|n

√r 1 + log

n r

c1243k ·

![image 217](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile217.png>)

![image 218](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile218.png>)

![image 219](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile219.png>)

r|n

- 1

![image 220](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile220.png>)

- 2 ≤ c1c22k√n.


![image 221](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile221.png>)

Here we set c = c1c2 to get the desired bound on the discrepancy over An.

Now we study the discrepancy of χ over A0n. Note that C(r′,w) = C(gcd(r′,n),w). We may only consider the set of C(r′,w) ∈ A0n for which r′ = pγ11 ··· pγkk is a factor of n. By deﬁnition of χ, we have the relation that

χ(C(r′,w)) =

χr(C(r′,w) ∩ Xr). (3.10)

r|n

If r′ is not a multiple of r = pδ11 ··· pδkk, then we know that there exists some 1 ≤ i ≤ k for which γi ≤ δi − 1. It follows that δi > 0, and i ∈ Ir. Since r′ is a factor of n and γi ≤ δi − 1, it is a factor of n/piαi−δi+1. Consequently, the congruence class C(r′,w) can be partitioned into congruence classes of the form C(n/piαi−δi+1,w′). Noting that (3.6) holds for any w′ ∈ Zn, we know that if r is not a factor of r′, then χr(C(r′,w) ∩ Xr) = 0. Thus we can remove all summands on the right hand side of (3.10) except those r that divides r′. We get

 

 C(r′,w) ∩

 

 .

χ(C(r′,w)) =

χr(C(r′,w) ∩ Xr) = χ

Xr

r|r′

r|r′

Note that we are taking union over all r = pδ11 ··· pδkk for which 0 ≤ δi ≤ γi for all 1 ≤ i ≤ k. We have

 

 

Yr

Xr = ψn

r|r′

r|r′

 

 

γk

γ1

S1(δ1) × ··· × Sk(δk)

···

= ψn

δk=0

δ1=0

 .

 

 

 

γi

n

Si(δi)

= ψn

i=1

δi=0

i=0 Si(δi) = ∅ if pi = 2 and γi < αi, and otherwise γi

From our construction, we know that γδi

Si(δi) = {x : 0 ≤ x < pγii} ⊆ Zpαi

.

i

δi=0

Thus we may conclude that

Xr ⊆ {ψn(t1,··· ,tk) : 0 ≤ ti < pγii for all 1 ≤ i ≤ k}. (3.11)

r|r′

Let Zr′ be the set on the right hand side of (3.11). Any two distinct elements of Zr′ diﬀer on some ti for 1 ≤ i ≤ k, i.e., they have diﬀerent remainders when divided by pγii for some i. Therefore their diﬀerence is not divisible by r′. Hence there is at most one element of C(r′,w) in r|r′ Xr ⊆ Zr′ for

any w ∈ Zn. We conclude that for any r′ that divides n and any w ∈ Zn,

 

 C(r′,w) ∩

 

  ≤ 1.

|χ(C(r′,w))| = χ

Xr

r|r′

This ﬁnishes our proof. Remark 3.7. By being a little more careful with bounds in the above proof, we may improve the latter inequality in Lemma 3.3 to

√n · 2(12+o(1))k,

![image 222](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile222.png>)

|χ(A)| ≤

max

![image 223](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile223.png>)

A∈An

where the o(1) term tends to 0 as k → ∞. This in turn improves the bound on disc(An) to minr|n nr + √r · 2(21+o(1))ω(r) in Theorem 3.1, where the o(1) term goes to 0 as ω(r) → ∞.

![image 224](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile224.png>)

![image 225](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile225.png>)

![image 226](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile226.png>)

4. Lower Bounds

In this section, we prove the lower bounds in Theorems 1.1 and 1.2. These proofs use Fourier analysis. We ﬁrst set up helpful notations and prove a consequence of the Plancherel theorem in Lemma 4.1.

Notations. Let f : Zn → C. Any coloring χ : Zn → {1,−1} is a special case. In this section, all summations are over Zn unless otherwise speciﬁed. We deﬁne the Fourier transform f : Zn → C by f(r) = x∈Z

f(x)e−2nπixr. For two functions f1,f2 : Zn → C, their convolution f1 ∗ f2 : Zn → C is given by f1 ∗ f2(a) =

![image 227](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile227.png>)

n

x f1(x)f2(a − x). We have the convolution identity f1 ∗ f2 = f1 · f2. For any r ∈ N that divides n, we say that x ≡ y (mod r) for x,y ∈ Zn if x = y + kr for some k ∈ Zn. We deﬁne, for any r ∈ N that divides n and a ∈ Zn,

r−1

|g(a,r)|2.

gf(a,r) :=

f(x) and Gf(r) :=

a=0

x∈Zn:x≡a(mod r)

We see that gf(a,r) = gf(a + kr,r), so gf(·,r) can be treated as a function on Zr.

Let M be a set or a multiset of elements in Zn. For a,r ∈ Zn, we deﬁne rM to be the multiset {rx : x ∈ M}, and a + M to be the multiset {a + x : x ∈ M}. We deﬁne mM to be the multiplicity function, i.e. mM(x) is the multiplicity of x in M. In particular, when M is a set, mM = 1M is the indicator function. We also deﬁne

f(M) =

f(x).

x∈M

- Lemma 4.1. For any f : Zn → C, let f be its Fourier transform. Let r ∈ N be a factor of n. Then r−1


n r

2

f k ·

= rGf(r).

![image 228](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile228.png>)

k=0

Proof. Let t = n/r. For each 0 ≤ k ≤ r − 1, we know that by deﬁnition

tr−1

r−1

n−1

f(x)e−2πir xk =

gf(a,r)e−2πir ak.

f(x)e−2nπix·kt =

f(kt) =

![image 229](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile229.png>)

![image 230](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile230.png>)

![image 231](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile231.png>)

x=0

a=0

x=0

Hence for g : Zr → C deﬁned by g(a) := gf(a,r), its Fourier transform is g(k) = f(kt). By the Plancherel theorem we have

r−1

k=0

n r

f k ·

![image 232](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile232.png>)

r−1

2

| g(k)|2 = r

=

k=0

r−1

|g(a)|2 = rGf(r).

a=0

In Lemmas 4.2 and 4.3, we prove lower and upper bounds on the same quantity respectively. Combining them we get Corollary 4.4. This corollary lower bounds the discrepancy of a function f over arithmetic progressions in Zn by the Fourier coeﬃcients of f. The next lemma lower bounds the quantity by a weighted L2 sum of Fourier coeﬃcients f. The weights depend on the arithmetic structure of n.

- Lemma 4.2. Let f : Zn → C, 1 ≤ m ≤ n be an integer, and M := {0,1... ,m − 1} ⊆ Zn. Then


m2 · gcd(r,n) n

| f(r)|2 · max

|f(a + bM)|2 ≥

,m . (4.1)

![image 233](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile233.png>)

a∈Zn b∈Zn

r∈Zn

Proof. We show some properties about the multiplicity function. For the set M, we have f(a + bM) =

f(x)m−bM(a − x) = f ∗ m−bM(a). (4.2)

f(x)ma+bM(x) =

f(a + bx) =

x

x

x∈M

For any u,v ∈ Zn, we have m−uM(v) =

m−uM(x)e−2nπivx =

![image 234](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile234.png>)

x

x∈−uM

![image 235](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile235.png>)

e−2nπivx =

e−2nπivuy = m−M(uv). (4.3)

![image 236](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile236.png>)

y∈−M

Applying (4.3) twice we have m−uM(v) = m−vM(u). We have

a b

1 n r

2

|f(a + bM)|2 =

|f ∗ m−bM(a)|2 =

f ∗ m−bM(r)

![image 237](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile237.png>)

b a

b

1 n b r | f(r)|2 · m−bM(r) 2 =

1 n b r | f(r)|2 m−rM(b) 2

=

![image 238](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile238.png>)

![image 239](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile239.png>)

(4.4)

=

r

| f(r)|2 ·

1 n b

![image 240](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile240.png>)

m−rM(b) 2 =

r

| f(r)|2 ·

s

|m−rM(s)|2,

where the ﬁrst equality uses (4.2), the second uses the Planchrel theorem, the third uses the Fourier identity of convolution, the fourth uses (4.3) twice, and the last uses the Plancherel theorem. Now we evaluate s |m−rM(s)|2. Let k = gcd(r,n). When km ≤ n, we know that rM contains m elements with multiplicity 1. Thus in this case we have

s

|m−rM(s)|2 = m.

Otherwise when km > n, we know that rM contains elements that are multiples of k. There are nk such elements in Zn. Therefore, by the Cauchy-Schwarz inequality, we have

![image 241](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile241.png>)

s

![image 242](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile242.png>)

|m−rM(s)|2 =

2

n k −1 t=0 |m−rM(tk)|

n k −1

![image 243](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile243.png>)

- m2k

![image 244](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile244.png>)

- n


|m−rM(tk)|2 ≥

=

.

![image 245](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile245.png>)

n/k

t=0

Hence we may conclude that for any r ∈ Zn,

|m−rM(s)|2 ≥ max

s

m2 · gcd(r,n) n

,m . (4.5)

![image 246](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile246.png>)

Combining this with (4.4), we obtain (4.1). The next lemma gives an upper bound on the quantity above. The upper bound involves the discrepancy of f over An and some arithmetic sums of f. Let φ(·) be Euler’s totient function.

- Lemma 4.3. Let f : Zn → C. Suppose that


|f(A)|. Let m ≤ n be a positive integer, and M := {0,1,... ,m − 1} ⊆ Zn. Then we have

Tf := max A∈An

φ(k) k

m2

|f(a + bM)|2 ≤ n2Tf2 +

Gf(n/k). (4.6)

![image 247](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile247.png>)

a∈Zn b∈Zn

0≤k<m:k|N

Proof. For each ﬁxed b ∈ Zn, we analyze the summation a |f(a + bM)|2. Let r = gcd(b,n) and k = n/r. There are two possibilities: rm ≤ n or rm > n.

If rm ≤ n, then each element in bM has multiplicity 1. Therefore a + bM is a set for all a ∈ Zn. Moreover from our deﬁnition of M = {0,1,... ,m − 1}, we know that a + bM ∈ An is an arithmetic progression in Zn. In this case, for any a, |f(a + bM)| ≤ Tf, so

Tf2 = nTf2. (4.7)

|f(a + bM)|2 ≤

a

a

If rm > n, i.e., m > k, then some elements in bM have multiplicity greater than 1. The bound in (4.7) no longer applies. Let K = {0,1,... ,k − 1} and it follows that each element in bK has multiplicity 1. Moreover, it covers each multiple of r in Zn exactly once. Hence

k−1

f(a + bt) = gf(a,r).

f(a + bK) =

t=0

Suppose that m = qk+s for integers q and 0 ≤ s < k. Then we may write mM = mS + j q=0−1 ms+jk+K where S = {0,1,... ,s − 1}. Thus, for any a ∈ Zn, we have

q−1

f(a + b · (s + jk) + bK)

f(a + bM) = f(a + bS) +

j=0

(4.8)

q−1

gf(a + b · (s + jk),r) = f(a + bS) + q · gf(a,r).

= f(a + bS) +

j=0

In the last step, we use the fact that b · (s + jk) is a multiple of r. Since s < k, each element in bS has multiplicity at most 1, and further a + bS ∈ An for all a. Thus

|f(a + bS)| ≤ Tf. (4.9) We now partition a ∈ Zn into congruence classes mod r. In particular, we have

r−1

|f(a + bM)|2. (4.10)

|f(a + bM)|2 =

a

i=0 a≡i(mod r)

For each a′ ≡ i (mod r), there are exactly s choices of a ≡ i (mod r) such that a′ ∈ a + bS. Thus,

k−1

f(a + bS) = s · gf(i,r). (4.11)

f(i + jr + bS) =

j=0

a≡i(mod r)

Consequently, we have

|f(a + bM)|2 =

a≡i(mod r)

k−1

|f(i + jr + bM)|2

j=0

- [by (4.8)] =

k−1

j=0

|f(i + jr + bS) + q · gf(i,r)|2

=

k−1

j=0

|f(i + jr + bS)|2 + 2Re q · f(i + jr + bS)gf(i,r) + q2|gf(i,r)|2

![image 248](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile248.png>)

- [by (4.9)] ≤ kTf2 + kq2|gf(i,r)|2 + 2q Re


 

 gf(i,r)

k−1

![image 249](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile249.png>)

f(i + jr + bS)

j=0

[by (4.11)] = kTf2 + kq2|gf(i,r)|2 + 2qs|gf(i,r)|2 ≤ kTf2 + |gf(i,r)|2 ·

k2q2 + 2kqs + s2 k [by m = kq + s] = kTf2 +

![image 250](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile250.png>)

m2 k |gf(i,r)|2. Put this into (4.10). We know that in the second case where rm > n, i.e., k < m,

![image 251](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile251.png>)

a

r−1

|f(a + bM)|2 ≤ nTf2 +

|f(a + bM)|2 =

i=0 a≡i(mod r)

m2 k

Gf(r) = nTf2 +

![image 252](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile252.png>)

m2 k

Gf(n/k). (4.12)

![image 253](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile253.png>)

The second case happens exactly when gcd(b,n) = n/k for some k < m which divides n. The number of such choices of b is exactly φ(k) for any ﬁxed k. Hence combining (4.7) and (4.12), we get (4.6).

Combining Lemma 4.2 and Lemma 4.3, we deduce the following general lower bounds. Corollary 4.4. Let f : Zn → C and f be its Fourier transform. Suppose that

|f(A)|. For any positive integer m ≤ n, we have

Tf := max A∈An

m2 · gcd(r,n) n

m2φ(k) k

| f(r)|2 · max

n2Tf2 +

Gf(n/k) ≥

,m . (4.13)

![image 254](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile254.png>)

![image 255](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile255.png>)

r∈Zn

1≤k<m:k|n

In Corollary 4.4, the inequality involves Gf and f besides Tf. We aim to get a lower bound on disc(An) that only depends on arithmetic structure of n (Proposition 4.7). To achieve that, we need two lemmas

(Lemma 4.5 and Lemma 4.6) to remove the dependency on f and Gf.

- Lemma 4.5. Let f : Zn → C and f be its Fourier transform and m ≤ n be a positive integer. Then


m2 · gcd(r,n) n

m2φ(k) k

| f(r)|2 ·

Gf(n/k) =

.

![image 256](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile256.png>)

![image 257](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile257.png>)

r∈Zn

1≤k≤n:k|n

Proof. By Lemma 4.1, we know that

n k

![image 258](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile258.png>)

| f(r)|2.

Gf(n/k) =

r∈Zn:k|r

Thus we have (noticing that k|l φ(k) = l for any positive integer l)

1≤k≤n:k|n

m2φ(k) k

m2φ(k) n

| f(r)|2 =

| f(r)|2 ·

Gf(n/k) =

![image 259](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile259.png>)

![image 260](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile260.png>)

r∈Zn

r∈Zn:k|r

1≤k≤n:k|n

- m2

![image 261](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile261.png>)

- n 1≤k≤n:k|gcd(n,r)


| f(r)|2 ·

=

φ(k) =

r∈Zn

r∈Zn

Hence we have the desired equality.

- m2

![image 262](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile262.png>)

- n 1≤k≤n:k|n,k|r


φ(k)

m2 n

| f(r)|2 ·

gcd(r,n).

![image 263](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile263.png>)

- Lemma 4.6. Let f : Zn → C and f be its Fourier transform. Let m,l ≤ n be positive integers. Then


m2 · gcd(r,n) n

m2φ(k) k

mn k

| f(r)|2 · min

,m ≤

Gf(n/k) +

Gf(n/k). (4.14)

![image 264](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile264.png>)

![image 265](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile265.png>)

![image 266](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile266.png>)

r∈Zn

1≤k≤l:k|n

l<k≤n:k|n

Proof. It suﬃces to compare the coeﬃcient of each | f(r)|2 on both sides after expanding all terms of Gf on the right hand side (4.14) using Lemma 4.1. By Lemma 4.1, for any k that divides n,

n k

| f(r)|2.

Gf(n/k) =

![image 267](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile267.png>)

r∈Zn:k|r

For each r ∈ Zn, the coeﬃcient tr of | f(r)|2 on the right hand side of (4.14) is given by

m2φ(k) n

- m2

![image 268](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile268.png>)

- n 1≤k≤l:k|gcd(r,n)


φ(k) + m

1.

tr =

m =

+

![image 269](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile269.png>)

1≤k≤l:k|gcd(r,n)

l<k≤n:k|gcd(r,n)

l<k≤n:k|gcd(r,n)

If gcd(r,n) ≤ l, then we know that the ﬁrst summation sums over all factors of gcd(r,n), and the second summation is zero. Hence we know that in this case,

- m2

![image 270](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile270.png>)

- n


gcd(r,n).

tr =

If gcd(r,n) > l, then in particular the second summation contains at least one term k = gcd(r,n), and the ﬁrst summation is nonnegative. Hence in this case,

tr > m. We may conclude that tr ≥ min m

2·gcd(r,n)

n ,m for all r ∈ Zn. This yields (4.14).

![image 271](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile271.png>)

Using the lemmas above, we prove a lower bound on disc(An) which depends only on the arithmetic structure of n.

Proposition 4.7. For any positive integers n and l ≤ n, 1 (disc(An))2 ≤

1 k2

8 n

φ(k) + 2

.

![image 272](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile272.png>)

![image 273](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile273.png>)

![image 274](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile274.png>)

1≤k≤l:k|n

l<k≤n:k|n

Proof. For simplicity let us denote S1 :=

1 k2

.

φ(k) and S2 :=

![image 275](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile275.png>)

1≤k≤l:k|n

l<k≤n:k|n

We aim to show

1

disc(An)2 ≥

. (4.15)

![image 276](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile276.png>)

8 nS1 + 2S2

![image 277](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile277.png>)

Because we always have disc(An) ≥ 1, we may assume that S1 < n8. Let χ : Zn → {1,−1} be any coloring of Zn, and let Tχ := maxA∈An |χ(A)|. Let m ≤ n be a positive integer to be determined later. By Corollary 4.4, we know that

![image 278](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile278.png>)

m2φ(k) k

n2Tχ2 +

Gχ(n/k) ≥

![image 279](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile279.png>)

1≤k<m:k|n

| χ(r)|2 · max

r∈Zn

m2 · gcd(r,n) n

,m . (4.16)

![image 280](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile280.png>)

By Lemma 4.5, we know that

m2φ(k) k

Gχ(n/k) =

![image 281](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile281.png>)

r∈Zn

1≤k≤n:k|n

m2 · gcd(r,n) n

| χ(r)|2 ·

.

![image 282](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile282.png>)

Subtract both sides from (4.16). We get

| χ(r)|2 · min

n2Tχ2 +

r∈Zn

m2 · gcd(r,n) n

,m ≥

![image 283](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile283.png>)

| χ(r)|2 · m +

r∈Zn

m≤k≤n:k|n

m2φ(k) k

Gχ(n/k). (4.17)

![image 284](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile284.png>)

Since χ takes value in {−1,1}, we know that

| χ(r)|2 = nGχ(n) = n2. (4.18)

r∈Zn

Note that each Gχ(·) is nonnegative. By (4.18), the right hand side of (4.17) is lower bounded by

m2φ(k) k

| χ(r)|2 · m +

Gχ(n/k) ≥ n2m. (4.19)

![image 285](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile285.png>)

r∈Zn

m≤k≤n:k|n

For the left hand side of (4.17), we apply Lemma 4.6 for m and l and get

| χ(r)|2 · min

r∈Zn

m2 · gcd(r,n) n

m2φ(k) k

,m ≤

Gχ(n/k) +

![image 286](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile286.png>)

![image 287](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile287.png>)

1≤k≤l:k|n

l<k≤n:k|n

mn k

Gχ(n/k). (4.20)

![image 288](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile288.png>)

Note that by deﬁnition, each single gχ(a,n/k) is the sum of k values of χ. Because χ takes value in {−1,1}, we have

n k · k2 = nk. (4.21)

Gχ(n/k) ≤

![image 289](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile289.png>)

Moreover, each gχ(a,n/k) is χ(A) for some A ∈ An, so |gχ(a,n/k)| ≤ Tχ. This means that for all k, Gχ(n/k) ≤

n k · Tχ2. (4.22)

![image 290](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile290.png>)

We bound the ﬁrst term on the right hand side of (4.20) using (4.21) and get

1≤k≤l:k|n

m2φ(k) k

Gχ(n/k) ≤ m2n

φ(k) = nm2 · S1. (4.23)

![image 291](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile291.png>)

1≤k≤l:k|n

On the other hand, we bound the second term on the right hand side of (4.20) using (4.22) and get

mn k

Gχ(n/k) ≤

![image 292](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile292.png>)

l<k≤n:k|n

l<k≤n:k|n

mn2 k2

Tχ2 = n2mTχ2 · S2. (4.24)

![image 293](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile293.png>)

Put (4.23) and (4.24) into (4.20). We get

| χ(r)|2 · min

r∈Zn

m2 · gcd(r,n) n

,m ≤ nm2 · S1 + Tχ2n2mS2. (4.25)

![image 294](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile294.png>)

Finally we put (4.19) and (4.25) into (4.17). We get

n2 + n2mS2 Tχ2 ≥ n2m − nm2S1. Dividing both sides by n2m, we get

1 m

+ S2 Tχ2 ≥ 1 −

![image 295](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile295.png>)

- m

![image 296](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile296.png>)

- n


S1. (4.26)

Now we pick m = ⌊n/(2S1)⌋. Note that S1 < n/8 from our assumption, so m ≥ 4Sn

![image 297](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile297.png>)

1

1 m ≤

4 n

- m

![image 298](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile298.png>)

- n


- 1

![image 299](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile299.png>)

- 2


S1 and 1 −

S1 ≥

. Put them into (4.26). We conclude that

![image 300](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile300.png>)

![image 301](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile301.png>)

. Therefore,

1 − mn S1 1 m + S2 ≥

1/2

1

![image 302](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile302.png>)

Tχ2 ≥

=

.

![image 303](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile303.png>)

![image 304](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile304.png>)

![image 305](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile305.png>)

4 nS1 + S2

8 nS1 + 2S2

![image 306](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile306.png>)

![image 307](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile307.png>)

![image 308](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile308.png>)

Since this bound applies to all Tχ2, it also applies to (disc(An))2 = minχ Tχ2. Hence we have (4.15).

Remark 4.8. As mentioned earlier in Remark 1.3, the proof above also applies to the case where χ takes value in the unit circle on the complex plane {z ∈ C : |z| = 1} (instead of {1,−1}). Just note that (4.18) and (4.21) hold in this more general case as well, and all other steps are identical.

Now we prove two corollaries. The ﬁrst shows that the upper bound in Theorem 3.1 is tight up to an no(1) factor.

- Corollary 4.9 (Lower bound in Theorem 1.1). There exists an absolute constant c > 0 such that, for any positive integer n,


+ √r , where d(n) is the number of factors of n.

n r

1 8 d(n) · min

![image 309](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile309.png>)

disc(An) ≥

![image 310](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile310.png>)

![image 311](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile311.png>)

![image 312](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile312.png>)

r|n

Proof. Let t1 be the minimum factor of n that is at least n23, and let t2 be the maximum factor of n less than n23. As

![image 313](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile313.png>)

![image 314](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile314.png>)

2 · min √t1,

n t2 ≥ min √t1 +

,√t2 +

+ √r , it suﬃces to show that

n t1

n t2

n r

![image 315](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile315.png>)

![image 316](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile316.png>)

![image 317](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile317.png>)

![image 318](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile318.png>)

= min

![image 319](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile319.png>)

![image 320](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile320.png>)

![image 321](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile321.png>)

![image 322](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile322.png>)

r|n

1 4 d(n) · min √t1,

n t2

![image 323](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile323.png>)

disc(An) ≥

![image 324](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile324.png>)

![image 325](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile325.png>)

![image 326](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile326.png>)

. (4.27)

Now we apply Proposition 4.7 to n and l = tn

. We bound the two summations as follows. We have

![image 327](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile327.png>)

1

n t1 · d(n). (4.28)

φ(k) ≤

k ≤

![image 328](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile328.png>)

1≤k≤tn

1≤k≤tn

:k|n

:k|n

![image 329](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile329.png>)

![image 330](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile330.png>)

1

1

Note that t2 is the largest factor of n less than t1, so the minimum k in {tn

< k ≤ n : k|n} is n/t2. Thus we have

![image 331](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile331.png>)

1

t22 n2 · d(n). (4.29)

1 k2 ≤

1 k2 ≤

![image 332](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile332.png>)

![image 333](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile333.png>)

![image 334](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile334.png>)

n t1

n t2

<k≤n:k|n

≤k≤n:k|n

![image 335](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile335.png>)

![image 336](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile336.png>)

Using above two bounds, we get

1

(disc(An))2 ≥

≥

![image 337](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile337.png>)

2 2

8 t1d(n) + 2 t

n2d(n)

![image 338](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile338.png>)

![image 339](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile339.png>)

n2 t22

1 16d(n)

min t1,

![image 340](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile340.png>)

![image 341](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile341.png>)

.

This is equivalent to (4.27), so we have the expected inequality. The second corollary proves the lower bound in Theorem 1.2. The main observation is that the factor d(n) can be removed in (4.28) and (4.29) when n is a prime power.

- Corollary 4.10 (Lower bound in Theorem 1.2). Let p be a prime number, and k be a positive integer. Then for n = pk,


1 4

k−⌊k/3⌋

disc(An) ≥

p

2 . (4.30)

![image 342](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile342.png>)

![image 343](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile343.png>)

Proof. In Proposition 4.7, we pick l = pt for some 1 ≤ t < n to be determined later. Note that the factors of n between 1 and l are given by s = pi for 0 ≤ i ≤ t, which are all factors of l. Hence we have

φ(s) = l = pt.

1≤s≤l:s|n

All factors of n larger than l are given by s = pi for t + 1 ≤ i ≤ k. Thus

k

1 s2

1 p2

1 p4

p−2i ≤ p−2t−2 · 1 +

+ ··· ≤ 2p−2t−2.

=

+

![image 344](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile344.png>)

![image 345](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile345.png>)

![image 346](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile346.png>)

i=t+1

l<s≤l:s|n

Therefore, by Proposition 4.7 we get

disc(An) ≥

![image 347](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile347.png>)

1 4 · min pk−2t,pt+1 =

1 4 · pmin(k−2t,t+1).

1 8pt−k + 4p−2t−2 ≥

![image 348](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile348.png>)

![image 349](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile349.png>)

![image 350](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile350.png>)

![image 351](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile351.png>)

![image 352](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile352.png>)

We pick t = ⌊k/3⌋ to get (4.30).

5. Concluding Remarks

In Theorem 1.1, the upper and lower bounds are oﬀ by a factor of O(d(n)3/2). We were not able to close this gap, and it seems that major improvement of either bound would require new observations.

- Problem 5.1. Determine disc(An) up to a constant factor for all n.


There are other notions of discrepancy besides the one studied in this paper. Among them there is the hereditary discrepancy, deﬁned for a system (Ω,A) as

herdisc(A) := max

disc(A|X)

X⊆Ω

where A|X = {A∩X : A ∈ A}. Clearly disc(A) ≤ herdisc(A). For the set A of arithmetic progressions in [n], Matousˇek and Spencer [10] proved a stronger statement that herdisc(A) = O(n41). This is because their partial coloring method works not just for A, but also for A|X for any X ⊆ [n].

![image 353](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile353.png>)

In contrast, our construction of the coloring in Section 3 is only valid for coloring the whole set Zn. While it can be adapted so that the same upper bound (possibly with a larger constant factor) applies to some special subsets of Zn, it does not work for all subsets X ⊆ Zn.

- Problem 5.2. Estimate the hereditary discrepancy of An.


By Corollary 2.3 we have herdisc(An) = O(n12). The method used in Section 2 can be adapted to give the following slightly stronger statement. Let φ(·) be Euler’s totient function.

![image 354](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile354.png>)

Theorem 5.1. There exists a constant c such that for all positive integers n, we have

en φ(n)

herdisc(An) ≤ cφ(n)12 log

![image 355](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile355.png>)

![image 356](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile356.png>)

3 2

![image 357](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile357.png>)

.

We leave the proof of this theorem to the Appendix. It shows that the upper bound O(n21) is not always tight. It would be interesting to determine if there is a matching lower bound of the form n12−o(1).

![image 358](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile358.png>)

![image 359](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile359.png>)

References

- [1] N. Alon and J. H. Spencer, The probabilistic method, 4th ed. Wiley, Hoboken, NJ, 2016.
- [2] J. Beck, Roth’s estimate of the discrepancy of integer sequences is nearly sharp, Combinatorica 1 (1981), 319-325.
- [3] J. Beck and W. W. L Chen, Irregularities of distribution, Cambridge Tracts in Mathematics, 89. Cambridge University Press, Cambridge, 1987.
- [4] B. Chazelle, (2000). The Discrepancy Method: Randomness and Complexity, Cambridge University Press, New York, 2000.
- [5] P. Erd˝s, and A. S´ark¨ozy, Some solved and unsolved problems in combinatorial number theory, Math. Slovaca 28

(1978), 407-421.

- [6] G. H. Hardy and E. M. Wright, An introduction to the theory of numbers, 6th ed. Oxford University Press, Oxford, 2008.
- [7] N. Hebbinghaus and A. Srivastav, Discrepancy of (centered) arithmetic progressions in Zp, European J. Combin. 35

(2014), 324-334.

- [8] E. Landau, Ueber die zahlentheoretische Funktion φ(n) und ihre Beziehung zum Goldbachschen Satz, Nachrichten von der Gesellschaft der Wissenschaften zu G¨ottingen, Mathematisch-Physikalische Klasse 1900 (1900), 177–186.
- [9] J. Matousˇek, Geometric Discrepancy: An Illustrated Guide, Algorithms Combin. 18, Springer, Berlin, 1999.
- [10] J. Matousˇek and J. Spencer, Discrepancy in arithmetic progressions, J. Amer. Math. Soc. 9 (1996), 195-204.
- [11] K. F. Roth, Remark concerning integer sequences, Acta Arith. 9 (1964), 257-260.
- [12] T. Tao, The Erd˝s discrepancy problem, Discrete Anal. 1 (2016), 27pp.
- [13] H. Weyl, Uber¨ die Gleichverteilung von Zahlen mod. Eins. (German) Math. Ann. 77 (1916), 313–352. Appendix A. Improved bound for hereditary discrepancy


In this appendix, we prove Theorem 5.1, an improved upper bound on the hereditary discrepancy of modular arithmetic progressions. We need the following lemma which gives a partial coloring bound.

- Lemma A.1. Let X ⊆ Zn be a set of size m > 0. There exists an absolute constant c such that there is a partial coloring χ : X → {−1,0,1} that assigns ±1 to at least m/10 elements in X such that

max

A∈An

|χ(A ∩ X)| ≤ cφ(n)12 log

![image 360](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile360.png>)

en φ(n)

![image 361](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile361.png>)

- 1

![image 362](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile362.png>)

- 2


.

Assuming this lemma, we may now prove Theorem 5.1.

Proof of Theorem 5.1 assuming A.1. Let X ⊆ Zn be a set of size m. We show that there exists a coloring χ : X → {1,−1} such that, for some absolute constant c,

max

A∈An

|χ(A ∩ X)| ≤ cφ(n)12 log

![image 363](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile363.png>)

en φ(n)

![image 364](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile364.png>)

3 2

![image 365](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile365.png>)

. (A.1)

The idea is that we iteratively apply Lemma A.1 to the set of uncolored elements until there are at most φ(n) elements left, and then apply Corollary 2.3 to color the remaining elements. Let c0,c1 be the constants in Lemma A.1 and Corollary 2.3.

Start with X0 = X. For each i ≥ 0, we apply Lemma A.1 to Xi to get a partial coloring χi : Xi → {−1,0,1}, and we let Xi+1 = χ−i 1(0) ⊆ Xi to be the set of uncolored elements in i-th iteration. We continue this process until the (k − 1)-th iteration where there are at most φ(n) elements left (i.e. |Xk| ≤ φ(n)). Then we apply Corollary 2.3 to get a coloring χk : Xk → {−1,1}. Let χ be the ﬁnal coloring given by χ(xi) = χi(xi) if xi ∈ Xi \ Xi+1 for 0 ≤ i ≤ k − 1, and χ(xk) = χk(xk). We know that |Xi| ≤ 0.9|Xi−1| for all 1 ≤ i ≤ k, so |Xk| ≤ (0.9)k|X0| = (0.9)km ≤ (0.9)kn. Because we stop when there are at most φ(n) elements left, we shall see that k ≤ 1 + log0.9 mn ≤ 10log enm . Applying the bounds on the discrepancy of χi from Lemma A.1 and Corollary 2.3, we conclude that for any A ∈ An,

![image 366](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile366.png>)

![image 367](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile367.png>)

|χ(A ∩ X)| =

k

i=0

χi(Xi ∩ A) ≤

k−1

i=0

|χi(Xi ∩ A)| + |χk(Xk ∩ A)|

≤ k · c0φ(n)21 log

![image 368](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile368.png>)

en φ(n)

![image 369](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile369.png>)

- 1

![image 370](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile370.png>)

- 2


+ c1|Xk|1

![image 371](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile371.png>)

2 log

en |Xk| < 10c0φ(n)12 log

![image 372](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile372.png>)

- 1

![image 373](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile373.png>)

- 2


![image 374](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile374.png>)

en m

![image 375](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile375.png>)

3

![image 376](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile376.png>)

2 + c1φ(n)12 log

![image 377](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile377.png>)

en m

![image 378](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile378.png>)

- 1

![image 379](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile379.png>)

- 2 ≤ cφ(n)12 log


![image 380](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile380.png>)

en m

![image 381](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile381.png>)

3 2

![image 382](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile382.png>)

for c = 10c0 + c1 being an absolute constant. Since it holds for all A ∈ An, we have (A.1). We are left to prove Lemma A.1. We ﬁrst need a slight generalization of the partial coloring lemma in Lemma 2.1. In Lemma 2.1 we require ∆S ≥ 2 |S|. Here we allow ∆S to take any positive value.

![image 383](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile383.png>)

- Lemma A.2 (Section 4.6 in [9]). Let (V,C) be a set system on n elements, and let a number ∆S > 0 be given for each set S ∈ C. Suppose that


n 5

∆S |S|

≤

(A.2)

g

![image 384](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile384.png>)

![image 385](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile385.png>)

![image 386](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile386.png>)

S∈C:S =∅

where

10e−λ2/4 if λ ≥ 2, 10log(1 + 2λ−1) if 0 < λ < 2.

(A.3)

g(λ) =

Then there exists a partial coloring χ that assigns ±1 to at least n/10 variables (and 0 to the rest), satisfying |χ(S)| ≤ ∆S for each S ∈ C.

We now prove Lemma A.1.

Proof of Lemma A.1. We use the same decomposition as in Lemma 2.2 to get the family C2 of nonempty subsets of X. From the argument in Lemma 2.2, we know that sets in C2 are of size 2i for 2i ≤ m. If χ : X → {−1,0,1} is such that for all 0 ≤ i ≤ log2 m we have χ(S) ≤ ∆i for any set S ∈ C2 of size 2i, then

|χ(A ∩ X)| ≤ 4

max

∆i. (A.4)

A∈An

0≤i≤log2 m

Then we apply a better bound on the number of sets in C2 of size 2i, which we shall denote as fi. The notations here are the same as in Lemma 2.2. For each 1 ≤ d < n and 0 ≤ a < gcd(d,n), the number

of choices of t in (2.5) is ⌊ld,a/2i⌋. Yet note that ld,a ≤ gcd(nd,n). Hence if gcd(d,n) > 2ni, then there are no such sets included in the set Xd,a. Therefore we have the following better bound on fi:

![image 387](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile387.png>)

![image 388](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile388.png>)

gcd(d,n)−1

fi ≤

1≤d≤n−1:gcd(d,n)≤2ni

a=0

![image 389](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile389.png>)

ld,a 2i

![image 390](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile390.png>)

=

![image 391](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile391.png>)

1≤d≤n−1:gcd(d,n)≤2ni

![image 392](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile392.png>)

m 2i ≤

m 2i

φ(n/l) ·

.

![image 393](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile393.png>)

1≤l≤2ni :l|n

![image 394](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile394.png>)

Because φ(ab) ≥ φ(a)φ(b) for all a,b ∈ N, we know that φ(n/l) ≤ φ(n)/φ(l) for all l that divides n. Also note that 0 < φ(n)/φ(l) for all l that does not divide n. By Landau [8, p. 184], for any x ≥ 1,

l≤x 1/φ(l) ≤ c0 log ex for some absolute constant c0. Hence we have fi ≤

m 2i

m 2i

m 2i

en 2i

1 φ(l) ≤ c0

φ(n/l) ≤

φ(n)

φ(n)log

. (A.5)

![image 395](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile395.png>)

![image 396](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile396.png>)

![image 397](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile397.png>)

![image 398](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile398.png>)

![image 399](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile399.png>)

1≤l≤2ni

1≤l≤2ni :l|n

![image 400](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile400.png>)

![image 401](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile401.png>)

For simplicity we denote M = φ(n)log φen(n). We deﬁne b : (0,n] → R, given by

![image 402](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile402.png>)

c1√s · M s −1 if s ≥ M, c1√s · M s −0.1 if s < M,

![image 403](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile403.png>)

![image 404](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile404.png>)

b(s) =

(A.6)

![image 405](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile405.png>)

![image 406](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile406.png>)

where c1 > 2 is an absolute constant to be determined later. We would like to show that there exists a partial coloring that colors at least m/10 elements in X, such that for any S ∈ C2,

|χ(S)| ≤ b(|S|). (A.7) In order to apply Lemma A.2, it suﬃces to verify that

⌊log2 m⌋

b(s) |S|

fi · g b(2i)2−i/2 ≤ m/5. (A.8)

=

g

![image 407](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile407.png>)

![image 408](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile408.png>)

S∈C2

i=0

For ﬁxed i, we denote τ = 2i/M, so 2i = τM ≥ τφ(n). Observe that

log τφen(n) log φen(n)

log en2i log φen(n) ≤ c0mτ−1

log τ−1 log φen(n)

![image 409](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile409.png>)

![image 410](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile410.png>)

fi ≤ c0m · τ−1 ·

= c0mτ−1 1 +

.

![image 411](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile411.png>)

![image 412](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile412.png>)

![image 413](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile413.png>)

![image 414](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile414.png>)

![image 415](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile415.png>)

![image 416](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile416.png>)

When τ < 1, we have b(2i)2−i/2 = c1τ−0.1 and

log τ−1 log φen(n) ≤ c0mτ−1(1 + log τ−1).

fi ≤ c0mτ−1 1 +

![image 417](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile417.png>)

![image 418](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile418.png>)

When τ ≥ 1, we have b(2i)2−i/2 = c1τ−1 and

log τ−1 log φen(n) ≤ c0mτ−1.

fi ≤ c0mτ−1 1 +

![image 419](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile419.png>)

![image 420](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile420.png>)

Therefore if we write the summation in (A.8) in terms of τ, we have

 , (A.9)

 

⌊log2 m⌋

τ−1g(c1τ−1) +

τ−1(1 + log τ−1)g(c1τ−0.1)

fi · g b(2i)2−i/2 = c0m

τ<1

τ≥1

i=0

where the summation of τ is over a geometric sequence with ratio 2. By deﬁnition of g in (A.3), g is monotonically decreasing. Let T be a large absolute constant to be determined later. We have

τ−1g(c1τ−1) ≤

τ≥T

τ−1g(2τ−1) =

τ≥T

τ−1 · 10log(1 + τ).

τ≥T

Since τ≥1 τ−1 · 10log(1 + τ) converges, there exists suﬃciently large constant T satisfying

1 20c0

τ−1g(c1τ−1) ≤

. (A.10)

![image 421](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile421.png>)

τ≥T

We bound the second term on the right hand side of (A.9) similarly. We have

τ−1(1+log τ−1)g(c1τ−0.1) ≤

τ<T−1

τ−1(1+log τ−1)g(2τ−0.1) =

τ<T−1

τ−1(1+log τ−1)·10e−τ−0.2.

τ<T−1

Since τ<1 τ−1(1 + log τ−1) · 10e−τ−0.2 converges, there exists suﬃciently large constant T satisfying

1 20c0

τ−1(1 + log τ−1)g(c1τ−0.1) ≤

. (A.11)

![image 422](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile422.png>)

τ<T−1

Hence, there exists constant T such that whenever c1 > 2, (A.10) and (A.11) hold. Note that there are at most (1 + log2 T) terms in each of the ranges 1 ≤ τ < T and T−1 ≤ τ < 1, and that g(x) is monotonically decreasing and tends to zero as x goes to inﬁnity. We can choose c1 > 2 suﬃciently large so that

1 20c0

τ−1g(c1τ−1) ≤ (1 + log2 T) · g(c1T−1) ≤

(A.12)

![image 423](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile423.png>)

1≤τ<T

and

τ−1(1 + log τ−1)g(c1τ−0.1) ≤ (1 + log2 T) · T(1 + log T)g(c1) ≤

T−1≤τ<1

1 20c0

. (A.13)

![image 424](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile424.png>)

Combining inequalities (A.10), (A.11), (A.12) and (A.13), there exists a constant c1 such that

τ−1(1 + log τ)g(c1τ−1) +

τ≥1

τ−1g(c1τ−0.1) ≤

τ<1

1 5c0

. (A.14)

![image 425](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile425.png>)

We use this constant c1 to deﬁne the function b(·) in (A.6). Combining (A.9) and (A.14), we have

⌊log2 m⌋

1 5c0

m 5

fi · g b(2i)2−i/2 ≤ c0m ·

.

=

![image 426](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile426.png>)

![image 427](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile427.png>)

i=0

Therefore (A.8) holds. By Lemma A.2, there exists a partial coloring χ : X → {−1,0,1} that assigns ±1 to at least m/10 elements in X such that (A.7) holds. For this coloring χ, we may choose ∆i = b(2i) in (A.4). Again we denote τ = 2i/M, or equivalently 2i = τM. We have

√

M · τ−0.5 if τ ≥ 1, c1

![image 428](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile428.png>)

c1

∆i = b(2i) =

√

M · τ0.4 if τ < 1. Put this in (A.4). We know that χ satisﬁes that

![image 429](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile429.png>)

 

 .

√

τ−0.5 +

τ0.4

![image 430](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile430.png>)

|χ(A ∩ X)| ≤ 4

M

max

∆i = 4c1

A∈An

τ<1

τ≥1

0≤i≤log2 m

Note that summation of τ is over a geometric sequence with ratio 2. Hence we have

1 1 − 2−0.4

1 1 − 2−0.5

τ−0.5 ≤

τ0.4 ≤

and

.

![image 431](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile431.png>)

![image 432](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile432.png>)

τ<1

τ≥1

Therefore we conclude that we can ﬁnd χ that assigns ±1 to at least m/10 elements in X and satisﬁes

- 1

![image 433](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile433.png>)

- 2


√

√

1 1 − 2−0.5

1 1 − 2−0.4 ≤ c

en φ(n) for some appropriate absolute constant c.

M = cφ(n)12 log

![image 434](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile434.png>)

![image 435](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile435.png>)

|χ(A ∩ X)| ≤ 4c1

M

+

max

![image 436](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile436.png>)

![image 437](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile437.png>)

![image 438](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile438.png>)

![image 439](<2021-fox-discrepancy-modular-arithmetic-progressions_images/imageFile439.png>)

A∈An

Department of Mathematics, Stanford University, Stanford, CA, USA Email address: {jacobfox,maxxu,yunkunzhou}@stanford.edu

