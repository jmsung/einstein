---
type: source
kind: paper
title: A note on the natural density of product sets
authors: Sandro Bettin, Dimitris Koukoulopoulos, Carlo Sanna
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2006.13356v1
source_local: ../raw/2020-bettin-note-natural-density-product.pdf
topic: general-knowledge
cites:
---

arXiv:2006.13356v1[math.NT]23Jun2020

A NOTE ON THE NATURAL DENSITY OF PRODUCT SETS

SANDRO BETTIN, DIMITRIS KOUKOULOPOULOS, AND CARLO SANNA

ABSTRACT. Given two sets of natural numbers A and B of natural density 1 we prove that their product set A · B := {ab : a ∈ A, b ∈ B} also has natural density 1. On the other hand, for any ε > 0, we show there are sets A of density > 1 − ε for which the product set A · A has density < ε. This answers two questions of Hegyva´ri, Hennecart and Pach.

1. INTRODUCTION

Given two sets of natural numbers A and B, let A · B := {ab : a ∈ A, b ∈ B} be their product set. Also, for any positive integer k, let Ak denote the k-fold product A · · ·A.

The problem of studying the cardinality of product sets has long been of interest in mathematics. The classic multiplication table problem due to Erd˝os [2, 3] asks for bounds on the cardinality Mn of the n × n multiplication table, i.e., of the set {1, . . ., n}2. Erd˝os showed that Mn = o(n2) and Ford [5], following earlier of Tenenbaum [10], determined the exact order of magnitude of Mn. More recently [7], the second author of the present paper provided uniform bounds for #({1, . . ., n1} · · ·{1, . . ., ns}) holding for a wide range of n1, . . ., ns ∈ N.

For more general sets A, the problem of estimating #(A ∩ [1, x])2 was studied by Cilleruelo, Ramana, and Ramare´ [1]. For example, they studied this problem when A is the set of shifted primes, the set of sums of two squares, and the set of shifted sums of two squares. Moreover, they computed the (almost sure) asymptotic behavior for #A2 when A is a random subset of {1, . . ., n} that contains each element of {1, . . ., n} independently with probability δ ∈ (0, 1). Sanna [9] extended this last result to the product of arbitrarily many sets.

Hegyva´ri, Hennecart and Pach [6] considered the analogous problem for inﬁnite sets of natural numbers. In this context, the role of the cardinality is played by the natural density d(A) of a set A, deﬁned as usual by

#A ∩ [1, x] x

d(A) = lim

. They asked the following questions (Questions 3 and 2 of [6], respectively):

![image 1](<2020-bettin-note-natural-density-product_images/imageFile1.png>)

x→∞

- Question 1. If A is a set of natural numbers of density 1, is it true that A2 also has density 1?
- Question 2. Is it true that infA⊂N: d(A)=α d(A2) = 0 for any α ∈ [0, 1), or at least for α ∈ [0, α0) for some α0 ∈ (0, 1)?


Clearly, Question 1 has an afﬁrmative answer if 1 ∈ A, and Hegyva´ri, Hennecart and Pach showed that it also sufﬁces that A contains an inﬁnite subset of mutually coprime integers a1 <

- a2 < · · · such that ∞i=1 a−i 1 = +∞. Here, we show that the answer is “yes” in full generality.


- Theorem 1. Let A, B ⊆ N. If d(A) = d(B) = 1, then d(A · B) = 1. Corollary. If A ⊂ N is such that d(A) = 1, then d(Ak) = 1 for each k = 2, 3, . . .


Remark. In fact, the case A = B of Theorem 1 implies easily the general case. Indeed, if d(A) = d(B) = 1, then d(A ∩ B) = 1. In addition, if (A ∩ B)2 has density 1, then so does A · B.

1

As it will be clear from the proof, the difference in the density of d(A2) with respect to Erd˝os’s multiplication table problem lies in the fact that many elements of A2 come from very “unbalanced” products, meaning products ab such that the sizes of a and b are completely different.

Let us now turn to Question 2. We will answer it in a strong form that shows, among other things, that the condition that d(A) = 1 in Theorem 1 cannot be relaxed.

- Theorem 2. For α ∈ [0, 1], we have


- 0 if α < 1,
- 1 if α = 1.


d(A2) =

inf

A ⊆ N: d(A) = α

Acknowledgements. The third author wishes to thank Paolo Leonetti for bringing the article of Hegyva´ri-Hennecart-Pach [6] to his attention. In addition, the ﬁrst two authors of the paper would like to thank the Mathematisches Forschungsinstitut Oberwolfach for the hospitality; the paper was partially written there while attending a workshop in November 2019.

S.B. is member of the INdAM group GNAMPA and his work is partially supported by PRIN 2017 “Geometric, algebraic and analytic methods in arithmetic” and by INdAM.

D.K. is partially supported by the Natural Sciences and Engineering Research Council of Canada (Discovery Grant 2018-05699) and by the Fonds de recherche du Que´bec - Nature et technologies (projet de recherche en e´quipe - 256442).

C.S. was supported by an INdAM postdoctoral fellowship and is a member of the INdAM group

GNSAGA, and of CrypTO, the Cryptography and Number Theory group of Politecnico di Torino. 2. PRELIMINARIES

Notation. Given an integer n, we write P−(n) and P+(n) for its smallest and largest prime factors, respectively, with the convention that P−(1) = ∞ and P+(1) = 1. If P+(n) ≤ y, we say that n is y-smooth, and if P−(n) > y, we say that it is y-rough. As usual, we let Φ(x, y) denote the number of y-rough numbers in [1, x]. Given any integer n, we may write it uniquely as n = ab with P+(a) ≤ y < P−(b). We then call a and b the y-smooth and y-rough part of n, respectively. Finally, we let Ω(n) denote the number of prime factors of n counted with multiplicity.

We need some standard lemmas. We give their proofs for the sake of completeness.

- Lemma 2.1. For x ≥ y > 1, we have Φ(x, y) ≪ x/ log y. Proof. This follows for example from Theorem 14.2 in [8] with f(n) = 1P−(n)>y.
- Lemma 2.2. Uniformly for x ≥ y2 ≥ 1 and u ≥ 1, we have #{n ≤ x : ∃d|n such that P+(d) ≤ y1/u and d > y} ≪ x · (e−u + y−1/3).


Proof. Without loss of generality, u ≥ 4. Let B denote the set of n ∈ Z ∩ [1, x] that have a y1/usmooth divisor d > y. Given n ∈ B, let p1 ≤ p2 ≤ · · · ≤ pk be the sequence of prime factors of n of size ≤ y1/u listed in increasing order and according to their multiplicity. By our assumption on n, we must have p1 · · ·pk > y. Let j be the smallest integer such that p1 · · ·pj > y. We must have j ≥ 5 because all factors pi are ≤ y1/u ≤ y1/4. We then set a = p1 · · ·pj−2, p = pj−1, and

√y, ap ≤ y, and P+(a) ≤ p ≤ P−(b). Consequently,

- b = n/(ap), so that a > y/(pj−1pj) ≥


![image 2](<2020-bettin-note-natural-density-product_images/imageFile2.png>)

x ap log p

1 ≪

(1) #B ≤

![image 3](<2020-bettin-note-natural-density-product_images/imageFile3.png>)

p≤y1/u P+(a)≤p a>√y

p≤y1/u P+(a)≤p √y<a≤y/p

b≤x/(ap) P−(b)≥p

![image 4](<2020-bettin-note-natural-density-product_images/imageFile4.png>)

![image 5](<2020-bettin-note-natural-density-product_images/imageFile5.png>)

by Lemma 2.1. If we let εp = min{2/3, 2/ logp}, then Rankin’s trick implies that #B x ≪

(a/√y)ε

y−ε

p/2

1 a1−εp .

![image 6](<2020-bettin-note-natural-density-product_images/imageFile6.png>)

p

=

![image 7](<2020-bettin-note-natural-density-product_images/imageFile7.png>)

![image 8](<2020-bettin-note-natural-density-product_images/imageFile8.png>)

![image 9](<2020-bettin-note-natural-density-product_images/imageFile9.png>)

![image 10](<2020-bettin-note-natural-density-product_images/imageFile10.png>)

ap log p

p log p

P+(a)≤p

p≤y1/u P+(a)≤p a>√y

p≤y1/u

![image 11](<2020-bettin-note-natural-density-product_images/imageFile11.png>)

The sum over a equals q≤p(1 − q−1+ε

)−1 with q denoting a prime number. Since qε

= 1 + O(log q/ log p) for q ≤ p, Mertens’ estimates [8, Theorem 3.4] imply that the sum over a is ≪ log p. We conclude that

p

p

e−logy/logp p ≤ y−1/3 +

e−ju p ≪ y−1/3 +

#B x ≪ y−1/3 +

![image 12](<2020-bettin-note-natural-density-product_images/imageFile12.png>)

![image 13](<2020-bettin-note-natural-density-product_images/imageFile13.png>)

![image 14](<2020-bettin-note-natural-density-product_images/imageFile14.png>)

j≥1 y1/(u(j+1))<p≤y1/(uj)

100<p≤y1/u

e−ju ≪ y−1/3 + e−u

j≥1

using Mertens’ estimates once again. This completes the proof.

- Lemma 2.3. Let y ≥ 2 and λ ∈ [0, 1.99], and set Q(λ) = λ log λ−λ+1 for λ > 0 and Q(0) = 0. If 0 ≤ λ ≤ 1, then

p≤y

1 −

1 p

![image 15](<2020-bettin-note-natural-density-product_images/imageFile15.png>)

P+(m)≤y Ω(m)≤λ log log y

1 m ≪ (log y)−Q(λ),

![image 16](<2020-bettin-note-natural-density-product_images/imageFile16.png>)

whereas if 1 ≤ λ ≤ 1.99, then

p≤y

1 −

1 p

![image 17](<2020-bettin-note-natural-density-product_images/imageFile17.png>)

P+(m)≤y Ω(m)≥λ log log y

1 m ≪ (log y)−Q(λ).

![image 18](<2020-bettin-note-natural-density-product_images/imageFile18.png>)

Proof. The result is trivial if λ = 0 by Mertens’ estimates [8, Theorem 3.4], so assume that λ > 0. If 0 < λ ≤ 1, then

P+(m)≤y Ω(m)≤λ log log y

1 m ≤

![image 19](<2020-bettin-note-natural-density-product_images/imageFile19.png>)

P+(m)≤y

λΩ(m)−λlog logy m

![image 20](<2020-bettin-note-natural-density-product_images/imageFile20.png>)

= (log y)−λlogλ

p≤y

1 −

λ p

![image 21](<2020-bettin-note-natural-density-product_images/imageFile21.png>)

−1

≍ (log y)−Q(λ)

p≤y

1 −

1 p

![image 22](<2020-bettin-note-natural-density-product_images/imageFile22.png>)

−1

where we used Mertens’ estimates once again. Similarly, if 1 ≤ λ ≤ 1.99, then

P+(m)≤y Ω(m)≥λ log log y

1 m ≤

![image 23](<2020-bettin-note-natural-density-product_images/imageFile23.png>)

P+(m)≤y

λΩ(m)−λlog logy m ≍ (log y)−Q(λ)

![image 24](<2020-bettin-note-natural-density-product_images/imageFile24.png>)

p≤y

1 −

1 p

![image 25](<2020-bettin-note-natural-density-product_images/imageFile25.png>)

−1

.

This completes the proof.

- Lemma 2.4. Let P be a set of primes such that p∈P 1/p < ∞. Then


1 p

d {n ∈ N : p|n ⇒ p ∈/ P} =

1 −

.

![image 26](<2020-bettin-note-natural-density-product_images/imageFile26.png>)

p∈P

Proof. The number of integers n ≤ x with a prime divisor p > log x from P is ≤

x p

= o(x) as x → ∞,

![image 27](<2020-bettin-note-natural-density-product_images/imageFile27.png>)

p>log x, p∈P

because p∈P 1/p converges. Hence, if we write P′ = P ∩ [1, log x], then #{n ≤ x : p|n ⇒ p ∈/ P} = #{n ≤ x : p|n ⇒ p ∈/ P′} + o(x) = x

1 p

1 −

+ o(x)

![image 28](<2020-bettin-note-natural-density-product_images/imageFile28.png>)

p∈P′

from the inclusion-exclusion principle that has ≤ 2#P′ ≤ 2logx = o(x) steps (e.g., see [8, Theorem 2.1]). Since p∈P\P′(1−1/p) ∼ 1 by our assumption that p∈P 1/p < ∞, the proof is complete.

3. PROOF OF THEOREM 1 Assume x is sufﬁciently large and let y = y(x) and u = u(x) to be chosen later, with y, u →

√x. In the following, for the sake of notation, we will often omit the dependence on x, y, u.

+∞ slowly as x → +∞. In particular, y ≤

![image 29](<2020-bettin-note-natural-density-product_images/imageFile29.png>)

With a small abuse of notation, given an integer n, let nsmooth denote its y1/u-smooth part and let nrough denote its y1/u-rough part. We then set

N = {n ≤ x : nsmooth ≤ y}. By Lemma 2.2, we have #N ∼ x as x → ∞. Therefore, in order to prove Theorem 1, it is enough to show that

#C = o(x), where C := N \ (A · B).

Let n ∈ C. Since n = nsmooth · nrough, we must have that either nsmooth ∈/ A or nrough ∈/ B. Consequently,

#C ≤ S1 + S2 with

S1 := #{n ∈ N : nsmooth ∈/ A} and S2 := #{n ∈ N : nrough ∈/ B}. Let us ﬁrst bound S1. Letting m = nsmooth, we have

1 m

ux log y

Φ(x/m, y1/u) ≪

S1 ≤

![image 30](<2020-bettin-note-natural-density-product_images/imageFile30.png>)

![image 31](<2020-bettin-note-natural-density-product_images/imageFile31.png>)

m≤y, m/∈A

m≤y, m/∈A

by Lemma 2.1. Since we have assumed that d(A) = 1, we must have that d(N \ A) = 0 and thus α(t) :=

1 m → 0 as t → ∞.

1 log t

![image 32](<2020-bettin-note-natural-density-product_images/imageFile32.png>)

![image 33](<2020-bettin-note-natural-density-product_images/imageFile33.png>)

m≤t, m/∈A

Hence, setting u = u(y) := α(y)−1/2, we have u → +∞ and S1 = o(x) as x → +∞. Let us now bound S2. Writing m′ = nrough, we have

#{m′ ≤ x/m : m′ ∈/ B}.

S2 ≤

m≤y

By hypothesis, we have d(B) = 1, so that d(N \ B) = 0. Thus β(t) := sup

# (N \ B) ∩ [1, s] s → 0 as t → ∞.

![image 34](<2020-bettin-note-natural-density-product_images/imageFile34.png>)

s ≥t

Hence, setting y := min x1/2, exp β(x1/2)−1/2 , we have y → +∞ as x → +∞ and

x d ≤ xβ(x/y)

1 d ≪ xβ(x1/2) log y ≤ xβ(x1/2)1/2 = o(x).

β(x/d) ·

S2 ≤

![image 35](<2020-bettin-note-natural-density-product_images/imageFile35.png>)

![image 36](<2020-bettin-note-natural-density-product_images/imageFile36.png>)

d ≤ y

d≤ y

In conclusion, #C = o(x), as desired. Remark. The proof of Theorem 1 can be made quantitative. For example, if one has #{n ≤ x : n ∈/ A}, #{n ≤ x : n ∈/ B} ≪ x(log x)−a for some ﬁxed 0 < a < 1, then taking y = exp (log x)

a 1+a

![image 37](<2020-bettin-note-natural-density-product_images/imageFile37.png>)

and u = log log x in the above argument yields #{n ≤ x : n ∈/ A · B} ≪ xe−u +

xlog y (log x)a ≪ x(log x)−

xu (log y)a

a2

1+a+o(1). An interesting question is to determine the optimal exponent of log x in this upper bound.

+

![image 38](<2020-bettin-note-natural-density-product_images/imageFile38.png>)

![image 39](<2020-bettin-note-natural-density-product_images/imageFile39.png>)

![image 40](<2020-bettin-note-natural-density-product_images/imageFile40.png>)

4. PROOF OF THEOREM 2

The case α = 1 follows from Theorem 1, whereas for the case α = 0 one can just observe that d(∅) = d(∅2) = 0. We may thus assume α ∈ (0, 1). Given any ε > 0, we need to construct a set A of density α such that the density of A2 exists and is smaller than ε.

Let k ∈ N, y ≥ 1 and a set of primes P ⊂ (y, +∞) with p∈P 1/p < ∞ to be chosen later. Using the notation Ωy(n) = pa|n,p≤y 1, let us consider the sets

By,k,P := n ∈ N : Ωy(n) ≥ k, (n, p) = 1 ∀p ∈ P . The key property these sets have is that By,k,2 P = By,2k,P.

Now, using Lemma 2.4 twice (once, with PLemma 2.4 = P∪{p ≤ y} and once with PLemma 2.4 = {p ≤ y}), we ﬁnd that

1 p

1 m

1 p p≤y

1 p

1 −

1 −

1 −

= d(By,k,∅)

d(By,k,P) =

.

![image 41](<2020-bettin-note-natural-density-product_images/imageFile41.png>)

![image 42](<2020-bettin-note-natural-density-product_images/imageFile42.png>)

![image 43](<2020-bettin-note-natural-density-product_images/imageFile43.png>)

![image 44](<2020-bettin-note-natural-density-product_images/imageFile44.png>)

P+(m)≤y Ω(m)≥k

p∈P

p∈P

Similarly,

1 p

d(By,k,2 P) = d(By,2k,P) =

d(By,2k,∅).

1 −

![image 45](<2020-bettin-note-natural-density-product_images/imageFile45.png>)

p∈P

Now, take y := exp(exp(4k/3)), so that k = 34 log log y. For any ﬁxed ε > 0, Lemma 2.3 implies that if k is sufﬁciently large in terms of α and ε, then d(By,k,∅) > α and d(By,2k,∅) < ε. Let us ﬁx for the remainder of the proof such a choice of k. We then construct P in the following way: we take p1 > y to be the smallest prime such that (1 − 1/p1)d(By,k,∅) > α, p2 > p1 the smallest prime such that (1 − 1/p1)(1 − 1/p2)d(By,k,∅) > α and so on. Taking P := {p1, p2, . . .} we clearly have d(By,k,∅) p∈P(1 − 1/p) = α. Thus, d(By,k,P) = α and d(By,k,2 P) < ε, as desired.

![image 46](<2020-bettin-note-natural-density-product_images/imageFile46.png>)

Remark. If d(A2) in Theorem 2 is replaced by the upper density d(A2), then one could just take A to be any density α subset of n ∈ N : Ωy(n) ≥ 43 log log y for y large enough. However, in general there is no guarantee that A2 has asymptotic density. For this reason, in order to prove Theorem 2, it is more convenient to construct explicit suitable sets A.

![image 47](<2020-bettin-note-natural-density-product_images/imageFile47.png>)

![image 48](<2020-bettin-note-natural-density-product_images/imageFile48.png>)

REFERENCES

- [1] J. Cilleruelo, D. S. Ramana, and O. Ramare´, Quotient and product sets of thin subsets of the positive integers, Proc. Steklov Inst. Math. 296 (2017), no. 1, 52–64.
- [2] P. Erdo˝s, Some remarks on number theory, Riveon Lematematika 9 (1955), 45–48.
- [3] , An asymptotic inequality in the theory of numbers, Vestnik Leningrad. Univ. 15 (1960), no. 13, 41–49.

![image 49](<2020-bettin-note-natural-density-product_images/imageFile49.png>)

- [4] , On some properties of prime factors of integers, Nagoya Math. J. 27 (1966), 617–623.

![image 50](<2020-bettin-note-natural-density-product_images/imageFile50.png>)

- [5] K. Ford, The distribution of integers with a divisor in a given interval, Ann. of Math. (2) 168 (2008), no. 2, 367–433.
- [6] N. Hegyva´ri, F. Hennecart, and P. P. Pach, On the density of sumsets and product sets, Australas. J. Combin. 74

(2019), 1–16.

- [7] D. Koukoulopoulos, On the number of integers in a generalized multiplication table, J. Reine Angew. Math. 689

(2014), 33–99.

- [8] , The distribution of prime numbers. Graduate Studies in Mathematics, 203. American Mathematical Society, Providence, RI, 2019.

![image 51](<2020-bettin-note-natural-density-product_images/imageFile51.png>)

- [9] C. Sanna, A note on product sets of random sets, Acta Math. Hungar., to appear.
- [10] G. Tenenbaum, Un probleme` de probabilite´ conditionnelle en arithmetique´ , Acta Arith. 49 (1987), no. 2, 165– 187.


DIPARTIMENTO DI MATEMATICA, UNIVERSITA` DI GENOVA, VIA DODECANESO 35, 16146 GENOVA, ITALY E-mail address: bettin@dima.unige.it

DEPARTEMENT´ DE MATHEMATIQUES´ ET DE STATISTIQUE, UNIVERSITE´ DE MONTREAL´ , CP 6128 SUCC.

CENTRE-VILLE, MONTREAL´ , QC H3C 3J7, CANADA E-mail address: koukoulo@dms.umontreal.ca DIPARTIMENTO DI SCIENZE MATEMATICHE, POLITECNICO DI TORINO, CORSO DUCA DEGLI ABRUZZI 24,

10129 TORINO, ITALY E-mail address: carlo.sanna.dev@gmail.com

