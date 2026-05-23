---
type: source
kind: paper
title: Subset sums, completeness and colorings
authors: David Conlon, Jacob Fox, Huy Tuan Pham
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2104.14766v1
source_local: ../raw/2021-conlon-subset-sums-completeness-colorings.pdf
topic: general-knowledge
cites:
---

Subset sums, completeness and colorings

David Conlon∗ Jacob Fox† Huy Tuan Pham‡

arXiv:2104.14766v1[math.CO]30Apr2021

Abstract

We develop novel techniques which allow us to prove a diverse range of results relating to subset sums and complete sequences of positive integers, including solutions to several longstanding open problems. These include: solutions to the three problems of Burr and Erdős on Ramsey complete sequences, for which Erdős later oﬀered a combined total of $350; analogous results for the new notion of density complete sequences; the solution to a conjecture of Alon and Erdős on the minimum number of colors needed to color the positive integers less than n so that n cannot be written as a monochromatic sum; the exact determination of an extremal function introduced by Erdős and Graham on sets of integers avoiding a given subset sum; and, answering a question reiterated by several authors, a homogeneous strengthening of a seminal result of Szemerédi and Vu on long arithmetic progressions in subset sums.

# 1 Introduction

Many of the most famous problems and results in mathematics concern the representation of positive integers as the sum of elements from a sparse sequence. For example, the long open Goldbach conjecture states that every even integer at least four is the sum of two primes, while Vinogradov’s theorem states that every suﬃciently large odd integer is the sum of three primes (and was recently extended by Helfgott [28] to cover all odd integers at least seven). Some other notable results of this type include Lagrange’s foursquare theorem that every positive integer is the sum of four squares, Gauss’ Eureka theorem that every positive integer is the sum of three triangular numbers and the Hilbert–Waring theorem.

While these problems concern the representation of integers as the sum of a bounded number of terms from a particular sequence, there are many results and open problems which do not stipulate a bound on the number of terms. A prominent example of such a result is a theorem of Szemerédi and Vu [40], conﬁrming an old conjecture of Erdős [14], which says that there is a constant C such that if A = (an)∞n=1 is an inﬁnite increasing sequence of integers with |A∩[n]| ≥ C√n for all suﬃciently large n which intersects every inﬁnite arithmetic progression of integers, then we can represent any suﬃciently large integer as a sum of distinct terms from the sequence. In this paper, we develop general methods which solve many open problems of precisely this type.

![image 1](<2021-conlon-subset-sums-completeness-colorings_images/imageFile1.png>)

![image 2](<2021-conlon-subset-sums-completeness-colorings_images/imageFile2.png>)

∗Department of Mathematics, California Institute of Technology, Pasadena, CA 91125. Email: dconlon@caltech.edu. Research supported by NSF Award DMS-2054452.

†Department of Mathematics, Stanford University, Stanford, CA 94305. Email: jacobfox@stanford.edu. Research supported by a Packard Fellowship and by NSF Award DMS-1855635.

‡Department of Mathematics, Stanford University, Stanford, CA 94305. Email: huypham@stanford.edu.

To be more precise, given a set or a sequence A of integers, we deﬁne the set of subset sums Σ(A) to be the set of all integers representable as a sum of distinct elements from A. That is,

Σ(A) =

s : S ⊆ A .

s∈S

Our contribution then is to solve several open problems on conditions which guarantee that Σ(A) contains either a particular integer or all suﬃciently large integers. In particular, we answer several old questions of Burr and Erdős [9] on the density of so-called Ramsey complete sequences, for whose solution Erdős [19] later oﬀered $350. We also solve a conjecture of Alon and Erdős [2] on the minimum number of colors needed to color the positive integers less than n so that n cannot be written as a monochromatic sum and determine exactly the answer to an extremal question ﬁrst studied by Alon, Erdős and Graham [1, 18] on the maximum size of a set avoiding a particular subset sum. Finally, answering a question reiterated by several groups of authors, including Erdős and Sárközy [22], Sárközy [36] and Tran, Vu, and Wood [42], we prove a homogeneous strengthening of another result of Szemerédi and Vu [40] from which the Erdős conjecture mentioned above was derived.

What unites these seemingly disparate topics is a common proof framework that allows us to show the existence of a long interval in the set of subset sums of an integer set S. This framework has several steps:

- (i) We partition S into ℓ parts S1,... ,Sℓ of roughly equal size for an appropriate choice of ℓ.
- (ii) We further partition each part Si into two parts Si′ and Si′′ of appropriate size and show that, for any s ∈ Si′′, the set of subset sums of Si′ modulo s is large.
- (iii) Using step (ii), we show that Σ(Si) = Σ(Si′ ∪ Si′′) is dense in some long interval.
- (iv) Using step (iii), we show that Σ(S) = Σ(S1 ∪ ··· ∪ Sℓ) contains a long interval.


Step (ii) is the heart of the method and must be appropriately tailored to each application, drawing variously on the probabilistic method, on structural results from additive number theory and on estimates from analytic number theory. We will say more about our methods in Section 2. For now, we will focus on describing our main results, along with several extensions, variations and applications, in more detail.

## 1.1 Ramsey completeness and density completeness

We say that a sequence of positive integers A is complete if every suﬃciently large positive integer is in Σ(A) and entirely complete if every positive integer is in Σ(A). For example, the powers of two are entirely complete, while the powers of three are incomplete. A far less simple example, due to Birch [6], is that the sequence {piqj : i,j ≥ 0} is complete whenever p,q ≥ 2 are coprime integers. For more on the rich history of complete sequences (and some open problems), we refer the interested reader to [10, 21].

Our starting point here is with the observation that the completeness property can be surprisingly fragile. Indeed, removing any element from the powers of two turns an entirely complete sequence into an incomplete one. For this reason, Burr and Erdős [8, 9] began the study of more robust notions of completeness. We will be concerned with two such notions here, namely, robustness under partitioning,

known as Ramsey completeness in the literature, and robustness under taking subsets, a new concept which we refer to as density completeness.

- 1.1.1 Ramsey completeness


Following Burr and Erdős [9], we say that a sequence of positive integers A is r-Ramsey complete if, whenever the sequence is partitioned into r classes A1,A2,... ,Ar, every suﬃciently large positive integer is in ri=1 Σ(Ai) and entirely r-Ramsey complete if every positive integer is in ri=1 Σ(Ai). Equivalently, A is entirely r-Ramsey complete if, for any coloring of A using r colors, every positive integer can be written

- as a monochromatic subset sum. In their paper introducing these concepts, Burr and Erdős [9] constructed an entirely 2-Ramsey com-

plete sequence A with the property that |A ∩[n]| ≤ C log3 n for all n, where C is an absolute constant. In the other direction, they were able to show that there is a constant c > 0 for which there is no 2-Ramsey complete sequence with |A ∩ [n]| ≤ clog2 n for all suﬃciently large n. They also asked whether it might be possible to narrow the gap between these two estimates and Erdős [19] later oﬀered $100 for such an improvement.

For r ≥ 3, the results of Burr and Erdős clearly imply that there is no r-Ramsey complete sequence with |A ∩ [n]| ≤ clog2 n for all suﬃciently large n. However, even for r = 3, they were unable to construct an r-Ramsey complete sequence with |A∩[n]| = no(1). Given the lack of progress on this problem, Erdős [19] later oﬀered $250 for any non-trivial result. Our ﬁrst theorem solves both this problem and that above

- at once, by determining the growth rate of the sparsest possible r-Ramsey complete sequence up to an absolute constant factor.


- Theorem 1.1. There is a constant C such that, for every integer r ≥ 2, there is an r-Ramsey complete sequence A with |A ∩ [n]| ≤ Cr log2 n for all n. Furthermore, there is a constant c > 0 such that no sequence A with |A ∩ [n]| ≤ cr log2 n for all suﬃciently large n is r-Ramsey complete.


Note that the lower bound, that is, the statement that there is a constant c > 0 such that no sequence A with |A ∩ [n]| ≤ cr log2 n for all suﬃciently large n is r-Ramsey complete, already improves on Burr and Erdős’ result, which had no dependency on r. We note also that a standard compactness argument implies that if A is an r-Ramsey complete sequence, then there is n(A) such that, for every r-coloring of A, every positive integer at least n(A) can be written as a sum of distinct monochromatic elements. We may therefore enlarge the r-Ramsey complete sequence A constructed in Theorem 1.1 to an entirely r-Ramsey complete sequence by including all positive integers less than n(A).

The key to proving Theorem 1.1 is a density-type result, Lemma 2.8, saying that, with high probability, a random sequence of Cǫ−1 log x elements chosen from those elements of the interval [x,2x) with no small prime factor has the property that any subset of size C log x contains a particular long interval in its set of subset sums. This density statement already improves a result of Spencer [37] from 1981 by showing that, for any integers r ≥ 2 and n suﬃciently large in terms of r, there is a set of integers S of size Cr log n with the property that any r-coloring of S contains a monochromatic subset whose elements add to n. More to the point, by concatenating the sequences given by Lemma 2.8, one for each dyadic interval [x,2x), it is easy to construct the sparse r-Ramsey complete sequence A required by Theorem 1.1.

We also study Ramsey completeness for polynomial sequences. The study of ordinary completeness for polynomial sequences has a long history, with important contributions by Sprague [38], Roth and Szekeres [34] and Cassels [11]. These eﬀorts culminated in a result of Graham [26], who characterized all real polynomial sequences which are complete (where the deﬁnition of completeness extends to real-valued sequences without alteration). Graham ﬁrst observed the well-known fact that every real polynomial of degree k can be written as P(x) = ki=0 αi xi , where xi is the polynomial i1! ij−=01(x − j) and αi ∈ R with αk = 0. He then showed that (P(m))m≥1 is complete if and only if the following three properties hold:

![image 3](<2021-conlon-subset-sums-completeness-colorings_images/imageFile3.png>)

- (i) αk > 0,
- (ii) αi = pi/qi for each i, where pi and qi are relatively prime integers, and
- (iii) gcd(p0,p1,... ,pk) = 1.


Given this body of work, it was a natural step for Burr and Erdős [9] to ask which polynomial sequences are Ramsey complete. According to Erdős [19], Burr subsequently proved that the sequence of kth powers is r-Ramsey complete for all r ≥ 2, though this result was never published. Our next theorem subsumes this result, answering their question completely by showing that all complete polynomial sequences are r-Ramsey complete for all r ≥ 2. In fact, it gives much more, extending the upper bound in Theorem 1.1, which corresponds to the case P(x) = x, by showing that every complete polynomial sequence has a subsequence which is r-Ramsey complete and as sparse as possible. Note again that in this context we are allowing the sequence to be real-valued, rather than restricting to the integers. The deﬁnitions of completeness and Ramsey completeness should then be adjusted to facilitate this change.

- Theorem 1.2. For any positive integer k, there is a constant C(k) such that, for every polynomial P of degree k for which (P(m))m≥1 is complete and every r ≥ 2, there is an r-Ramsey complete subsequence A ⊂ (P(m))m≥1 with |A ∩ [n]| ≤ C(k)r log2 n for all n.


- 1.1.2 Density completeness


We say that a sequence of positive integers A is ǫ-complete if every subsequence A′ of A with the property that |A′ ∩ [n]| ≥ ǫ|A ∩ [n]| for all suﬃciently large n is complete. This is the natural density analogue of Ramsey completeness, though it is not at all obvious that such sequences actually exist. Indeed, since the even integers are not complete, the set of all positive integers is not (21 − δ)-complete for any δ > 0, an observation which might suggest that no ǫ-complete sequences exist when ǫ is small. However, by using the result of Szemerédi and Vu [40], which we will discuss in more detail in Section 1.3, that there is a constant C such that any subset of [n] of size at least C√n contains an arithmetic progression of length n in its set of subset sums, one can show that any sequence of primes A with |A ∩ [n]| ≥ 2Cǫ−1√n for all suﬃciently large n is ǫ-complete. Thus, the correct takeaway is that the property of being ǫ-complete is not monotone. More concretely, as in the example above where we looked at all positive integers, an ǫ-complete sequence cannot have an ǫ-proportion of its elements sharing a common divisor.

![image 4](<2021-conlon-subset-sums-completeness-colorings_images/imageFile4.png>)

![image 5](<2021-conlon-subset-sums-completeness-colorings_images/imageFile5.png>)

![image 6](<2021-conlon-subset-sums-completeness-colorings_images/imageFile6.png>)

In keeping with our results about Ramsey completeness, our main result regarding this new notion of ǫ-completeness is a determination of how sparse an ǫ-complete sequence can be. To state this result, we

need some notation. Let F = (fn)n≥1 be any sequence of positive integers for which fn = i≤ǫn fi for all suﬃciently large n. It is easy to see that any two such sequences are comparable, growing within a constant factor of each other which depends only on the initial terms. In Appendix A.1, we will show that any such F satisﬁes

1

2log(1/ǫ)+o(1) (log n)2

![image 7](<2021-conlon-subset-sums-completeness-colorings_images/imageFile7.png>)

fn = e

or, equivalently,

√

![image 8](<2021-conlon-subset-sums-completeness-colorings_images/imageFile8.png>)

(2 log(1/ǫ)+o(1)) logn. The promised result now says that the fastest-growing ǫ-complete sequence grows on the same order as F.

|F ∩ [n]| = e

- Theorem 1.3. Let F = (fn)n≥1 be any sequence of positive integers for which fn = i≤ǫn fi for all suﬃciently large n. Then every ǫ-complete sequence A = (an)n≥1 must satisfy an = O(fn) and there is an ǫ-complete sequence with an = Θ(fn).

Like with Ramsey completeness, we may also prove a generalization regarding ǫ-complete subsequences of complete polynomial sequences, though in this case we omit the details of the argument, only pointing to how ideas from the proofs of Theorems 1.2 and 1.3 can be combined to give the required conclusion.

- Theorem 1.4. Let P be a polynomial for which the sequence (P(m))m≥1 is complete. Then there is a subsequence A = (an)n≥1 of (P(m))m≥1 with an = Θ(fn) which is ǫ-complete. That is, any complete polynomial sequence has an ǫ-complete subsequence which is as sparse as an ǫ-complete sequence can be.


## 1.2 Ensuring a given subset sum

So far, we have discussed problems and results on notions of completeness, where we require that all suﬃciently large integers can be represented as subset sums. We now address the natural problem of ensuring that a particular integer is a subset sum, again looking at both a Ramsey variant and a density variant.

- 1.2.1 Monochromatic subset sums


Given a positive integer n, let f(n) be the minimum integer r for which there is an r-coloring of the positive integers less than n with the property that n cannot be written as a monochromatic sum of distinct integers. The problem of estimating f(n) was raised by Erdős many times [15, 16, 17], culminating in a problem paper [20] where he stated that he could show f(n) = o(n1/3) and asked whether f(n) = n1/3−o(1). Solving this problem, Alon and Erdős [2] showed that there are positive constants c1 and c2 such that

c1n1/3 log4/3 n

c2n1/3(log log n)1/3 (log n)1/3

, (1)

≤ f(n) ≤

![image 9](<2021-conlon-subset-sums-completeness-colorings_images/imageFile9.png>)

![image 10](<2021-conlon-subset-sums-completeness-colorings_images/imageFile10.png>)

adding that they suspect the upper bound is closer to the truth. Using his result with Szemerédi [40] on long arithmetic progressions in subset sums, Vu [43] later reﬁned the lower bound, showing that f(n) ≥ clog1n1n/3 for some positive c1.

![image 11](<2021-conlon-subset-sums-completeness-colorings_images/imageFile11.png>)

We improve these results further, determining f(n) up to an absolute constant factor and thereby conﬁrming Alon and Erdős’ conjecture that their upper bound is close to the true order of magnitude.

As is customary, we write φ(n) for the Euler totient function, the number of positive integers less than n which are coprime to n.

- Theorem 1.5. For every positive integer n, the minimum number of colors f(n) for which it is possible to color the positive integers less than n so that n cannot be written as a monochromatic sum of distinct integers satisﬁes


n1/3(n/φ(n)) (log n)1/3(log log n)2/3

f(n) = Θ

.

![image 12](<2021-conlon-subset-sums-completeness-colorings_images/imageFile12.png>)

Standard estimates imply that n/φ(n) ∈ (1,2log log n) for n suﬃciently large, with n/φ(n) large if and only if n is divisible by many small primes. As a result, f(n) is surprisingly far from being monotone, exhibiting local multiplicative ﬂuctuations on the order of log log n. Moreover, though f(n) is indeed close to the upper bound proved by Alon and Erdős, diﬀering by at most a log log n factor, their upper bound is only optimal up to a constant factor when n is divisible by many small primes.

To give some sense of where our improvement comes from, let us brieﬂy describe the coloring that Alon and Erdős use for their upper bound, using r colors in total. First, they use r/2 colors to color all integers in [n−1] larger than 2n/r, with all integers in [n/(j +1),n/j) getting color j. Since any j distinct integers of color j have sum less than n and any j + 1 distinct integers of color j have sum larger than n, we see that n is not a sum of distinct elements from any of these color classes. Second, for each of the ﬁrst r/4 primes p that are coprime to n, they place all remaining multiples of p in a color class. Since each sum of multiples of p is itself a multiple of p and each p is coprime to n, we see that n is again not a sum of elements from any of these color classes. To complete the construction, we group the few remaining uncolored integers into color classes so that the sum of the elements in any given color class is less than n. A careful analysis then shows that r can be taken to be the upper bound in (1).

As in the Alon–Erdős coloring, our coloring uses r/2 colors to color all integers in [n − 1] larger than 2n/r and then r/4 colors to color the multiples of each of the ﬁrst r/4 primes which are coprime to n. However, we then add an additional third step, which makes use of the non-uniform distribution of the remaining elements in congruence classes modulo d for an appropriate choice of d. Indeed, let d be as large as possible so that d is coprime to n and φ(d) < r/32, noting that the prime factors of d must be among the ﬁrst r/4 primes coprime to n and so the remaining uncolored integers are all coprime to d. For each congruence class t (mod d) with t coprime to d, let xt ∈ [d] be such that xt ≡ t−1n (mod d). If a sum of elements, each congruent to t (mod d), is equal to n, then the sum must involve either xt terms, d + xt terms or more than d + xt terms. Therefore, arguing as for the ﬁrst r/2 colors, neither the set of integers congruent to t (mod d) which are at least n/xt nor the set of integers congruent to t (mod d) which are at least n/(d + xt) and less than n/xt can contain a subset sum equal to n. Hence, using at most 2φ(d) < r/8 additional colors, we may color all integers in [n − 1] larger than n/d in such a way that n is not a monochromatic sum of distinct elements. To complete the coloring, we again group the remaining uncolored integers into color classes so that the sum of the elements in any given color class is less than n. Worked out carefully, this then returns the upper bound in Theorem 1.5. For a sketch of how we prove the matching lower bound, which is the more diﬃcult aspect of the proof, we refer the reader to Section 2.3.

In practice, since our methods allow it, we will prove a more general result. For the statement, we need some notation. For positive integers ρ and m, writing pi for the ith prime, we let W(ρ) = ρi=1 pi

and τ(ρ,m) = φ(W(ρ)m)/(W(ρ)m). For m ∈ [n, n2 ], we then let ρ(n,m) be the smallest positive integer ρ such that ρ/τ(ρ,m) ≥ n2/φ(m). Our generalization of Theorem 1.5 is now as follows.

- Theorem 1.6. For every positive integer n and any m ∈ [n, n2 ], the minimum number of colors f(n,m) for which it is possible to color the positive integers less than n so that m cannot be written as a monochromatic sum of distinct integers satisﬁes

f(n,m) = Θ min

m1/3(m/φ(m)) (log n)1/3(log log n)2/3

![image 13](<2021-conlon-subset-sums-completeness-colorings_images/imageFile13.png>)

,ρ(n,m) .

- 1.2.2 The largest set avoiding a given subset sum What is the maximum size g(n,m) of a subset of [n] which has no subset sum equal to m? Variants of


this natural extremal problem, interesting for any positive integers n < m ≤ n+12 , were originally raised by Erdős and Graham (see, for instance, [21, Page 59] and [18]), although, in the exact form mentioned here, the problem was ﬁrst studied in detail by Alon [1].

If we let snd(m) be the smallest positive integer that does not divide m, an easy lower bound for

- g(n,m) is ⌊sndn(m)⌋, since the set of all multiples of snd(m) below n does not have n as a subset sum. This simple observation of Alon [1] was later reﬁned by Alon and Freiman [3], who observed that g(n,m) ≥


![image 14](<2021-conlon-subset-sums-completeness-colorings_images/imageFile14.png>)

s(n,m) := ⌊sndn(m)⌋ + snd(m) − 2 by augmenting the example above with snd(m) − 2 additional elements, each congruent to either 1 or −1 modulo snd(m). Another simple lower bound, better than that above

![image 15](<2021-conlon-subset-sums-completeness-colorings_images/imageFile15.png>)

when m is close to n+12 , is g(n,m) ≥ ⌊

√2m − 1/2⌋, following from the fact that the sum of the ﬁrst ⌊

![image 16](<2021-conlon-subset-sums-completeness-colorings_images/imageFile16.png>)

√2m − 1/2⌋ positive integers is less than m.

![image 17](<2021-conlon-subset-sums-completeness-colorings_images/imageFile17.png>)

For the upper bound, Alon [1] ﬁrst showed that if n1+ǫ ≤ m ≤ n2/(log n)2, then g(n,m) = O(s(n,m)), where the implicit constant depends on ǫ. He also conjectured that g(n,m) = (1 + o(1))s(n,m) in roughly the same range. For Cn(log n)6 ≤ m ≤ n1.5−o(1), this conjecture was proved soon after by Lipkin [31]. Remarkably, around the same time, Alon and Freiman [3] determined the function exactly for n5/3+o(1) ≤ m < 20(logn2n)2, establishing that g(n,m) = s(n,m) in this range. More than twenty years then elapsed before Tran, Vu and Wood [42] proved Alon’s conjecture in full generality by showing that

![image 18](<2021-conlon-subset-sums-completeness-colorings_images/imageFile18.png>)

- g(n,m) = (1 + o(1))s(n,m) for n(log n)1+o(1) ≤ m ≤ 9(logn2n)2. We improve these results, determining the function exactly for all Cnlog n ≤ m ≤ (8+o(1))(logn2 n)2 and asymptotically for all Cnlog n ≤ m ≤ n+12 .


![image 19](<2021-conlon-subset-sums-completeness-colorings_images/imageFile19.png>)

![image 20](<2021-conlon-subset-sums-completeness-colorings_images/imageFile20.png>)

- Theorem 1.7. There is a constant C such that if n and m are positive integers and g(n,m) is the maximum size of a subset of [n] with no subset sum equal to m, then


g(n,m) = s(n,m) =

n snd(m)

![image 21](<2021-conlon-subset-sums-completeness-colorings_images/imageFile21.png>)

+ snd(m) − 2

for m ∈ Cnlog n, 12(logn2n)2 and

![image 22](<2021-conlon-subset-sums-completeness-colorings_images/imageFile22.png>)

√

![image 23](<2021-conlon-subset-sums-completeness-colorings_images/imageFile23.png>)

g(n,m) = max s(n,m),(1 + o(1))

2m

for m ∈ 12(log n2n)2, n+12 .

![image 24](<2021-conlon-subset-sums-completeness-colorings_images/imageFile24.png>)

Since snd(m) ≤ (1 + o(1))log m ≤ (2 + o(1))log n, the theorem in fact implies that g(n,m) =

- max s(n,m),(1 + o(1))√2m = s(n,m) for Cnlog n ≤ m ≤ (8+o(1))(logn2 n)2, as promised above. On the other hand, once m < cn log n for c suﬃciently small, we do not generally have the bound g(n,m) = (1 + o(1))s(n,m). Indeed, for 8n < m < n(log n)/8, we can show that there is a subset of [n] of size h = ⌊n2/(2m)⌋ with no subset sum equal to m, so if snd(m) ≥ (log n)/2, then g(n,m) ≥ h > (2−o(1))s(n,m). To show the existence of the required subset of size h, choose an integer n′ ∈ (h+3n/4,n] such that m ∈ [n′n/(2h),n′n/(2h) + n/4]. Note that n′ ∈ (h + 3n/4,n] as n′ ≤ 2mh/n ≤ n and, since n2/(2m) ≥ h ≥ n2/(2m) − 1, we can verify that, for m ∈ (8n,n(log n)/8) and n suﬃciently large,


![image 25](<2021-conlon-subset-sums-completeness-colorings_images/imageFile25.png>)

![image 26](<2021-conlon-subset-sums-completeness-colorings_images/imageFile26.png>)

n′ ≥ 2h(mn−n/4) > h + 3n/4. Observe now that the set of subset sums of the interval [n′ − h,n′] does not contain any element from the interval [n′n/(2h),n′n/(2h) + n/4], since any sum of at most n/(2h)

![image 27](<2021-conlon-subset-sums-completeness-colorings_images/imageFile27.png>)

elements from the interval is strictly smaller than n′n/(2h), while any sum of at least n/(2h)+1 elements from the interval is strictly larger than (n′ − h)(n/(2h) + 1) = n′n/(2h) + n′ − h − n/2 > n′n/(2h) + n/4. Therefore, the interval [n′ − h,n′] has size at least h and does not contain m as a subset sum, as required.

To say more about how we prove Theorem 1.7, we must ﬁrst discuss the main tool used in our proof, a strengthening of the subset sums result of Szemerédi and Vu [40] which is itself of independent interest.

## 1.3 Long homogeneous progressions in subset sums

We opened this paper by mentioning Szemerédi and Vu’s proof [40] of a longstanding conjecture of Erdős [14]. As shown by Folkman [24], this is itself a corollary of the statement that there is a constant C such that if A = (an)∞n=1 is an inﬁnite increasing sequence of integers with |A ∩ [n]| ≥ C√n for all suﬃciently large n, then Σ(A) contains an inﬁnite arithmetic progression. In proving this latter statement, Szemerédi and Vu ﬁrst proved the following ﬁnite analogue, which we have already mentioned several times. Note that this result is clearly best possible, as may be seen by considering the set of all positive integers up to ⌊

![image 28](<2021-conlon-subset-sums-completeness-colorings_images/imageFile28.png>)

√2n − 1/2⌋.

![image 29](<2021-conlon-subset-sums-completeness-colorings_images/imageFile29.png>)

- Theorem 1.8 (Szemerédi–Vu [40]). There is a constant C such that if A ⊂ [n] with |A| ≥ C√n, then Σ(A) contains an arithmetic progression of length n.

![image 30](<2021-conlon-subset-sums-completeness-colorings_images/imageFile30.png>)

This theorem improved on an earlier result obtained independently by Freiman [25] and Sárközy [35], who showed that there is a constant C such that if |A| ≥ C√nlog n, then Σ(A) contains an arithmetic progression of length at least n. However, it also loses something, because the Freiman–Sárközy result gives not only an arithmetic progression, but a homogeneous progression, an arithmetic progression a,a + d,... ,a + kd where the common diﬀerence d divides a and, hence, every other term in the progression. The natural question then, reiterated by several groups of authors, including Erdős and Sárközy [22], Sárközy [36] and Tran, Vu, and Wood [42], is whether there is a common strengthening of the Szemerédi– Vu and Freiman–Sárközy theorems. We answer this question in the aﬃrmative.

![image 31](<2021-conlon-subset-sums-completeness-colorings_images/imageFile31.png>)

- Theorem 1.9. There is a constant C such that if A ⊂ [n] with |A| ≥ C√n, then Σ(A) contains a homogeneous progression of length n.


![image 32](<2021-conlon-subset-sums-completeness-colorings_images/imageFile32.png>)

For the proof of Theorem 1.7, we need a slightly stronger version of Theorem 1.9. This result, Theorem 6.1, states that if A ⊂ [n] with |A| ≥ C√n, then there exists d (which is typically just 1) such that most elements in A are divisible by d and the set of subset sums formed from adding at most 250n/|A|

![image 33](<2021-conlon-subset-sums-completeness-colorings_images/imageFile33.png>)

elements of A which are divisible by d contains a homogeneous progression with length n and common diﬀerence d.

To prove Theorem 1.7, suppose now that A is a subset of [n] with s(n,m) + 1 elements and we wish to show that m ∈ Σ(A). Using Theorem 6.1, we may conclude that Σ(A) contains a homogeneous progression with length n and common diﬀerence d, where d divides most elements of A. Moreover, if d|m, this progression will contain m, so we may assume that d ≥ snd(m). A simple counting argument then implies that d must in fact equal snd(m), as otherwise there will not be enough elements in A. Since s(n,m) + 1 = ⌊sndn(m)⌋ + snd(m) − 1, there must also be at least snd(m) − 1 elements in A which are not divisible by snd(m). We complete the proof by using these additional elements to show that m ∈ Σ(A),

![image 34](<2021-conlon-subset-sums-completeness-colorings_images/imageFile34.png>)

- as required. As another corollary of Theorem 1.9, we also obtain an improved bound on an old question of Straus [39]


(see also [23]) regarding the maximum size of a non-averaging subset of [n], where a subset A of [n] is said to be non-averaging if no a ∈ A is the average of two or more other elements of A. If we write

- h(n) for the maximum size of a non-averaging subset of [n], an elegant construction of Bosznay [7] shows that h(n) = Ω(n1/4). On the other hand, if we write H(n) for the maximum integer for which there are two subsets of [n] of size H(n) whose sets of subset sums have no non-zero common element, then a result of Straus [39] says that h(n) ≤ 2H(n) + 2. Using the Freiman–Sárközy result on homogeneous progressions, Erdős and Sárközy [22] were able to show that H(n) = O(√nlog n), which, by Straus’ observation, also yields a similar upper bound on h(n). By following their method, but using Theorem 1.9 instead of the Freiman–Sárközy result, we improve their bound to H(n) = O(√n), which is tight up to the constant factor, as may be seen by considering the sets [1,c√n] and [n − c√n,n] for any c < √2. By Straus’ inequality, it also provides an improved upper bound h(n) = O(√n) for the size of the largest non-averaging subset of [n].


![image 35](<2021-conlon-subset-sums-completeness-colorings_images/imageFile35.png>)

![image 36](<2021-conlon-subset-sums-completeness-colorings_images/imageFile36.png>)

![image 37](<2021-conlon-subset-sums-completeness-colorings_images/imageFile37.png>)

![image 38](<2021-conlon-subset-sums-completeness-colorings_images/imageFile38.png>)

![image 39](<2021-conlon-subset-sums-completeness-colorings_images/imageFile39.png>)

![image 40](<2021-conlon-subset-sums-completeness-colorings_images/imageFile40.png>)

Corollary 1.10. There is a constant C such that H(n) ≤ C√n, where H(n) is the largest integer for which there are two subsets of [n] of size H(n) whose sets of subset sums have no non-zero common element, and

![image 41](<2021-conlon-subset-sums-completeness-colorings_images/imageFile41.png>)

- h(n) ≤ C√n, where h(n) is the size of the largest non-averaging subset of [n].


![image 42](<2021-conlon-subset-sums-completeness-colorings_images/imageFile42.png>)

## Organization of the paper

In the next section, we will elaborate on our methods by giving rough outlines of the proofs of some of our main results. We then proceed to the formal proofs, proving Theorems 1.1 and 1.2 on Ramsey completeness in Section 3, Theorem 1.3 on density completeness in Section 4 and Theorem 1.6 on monochromatic subset sums in Section 5. We turn to the proof of Theorem 1.9, our homogeneous strengthening of the Szemerédi–Vu theorem, and its consequence Corollary 1.10 in Section 6 and conclude in Section 7 by proving Theorem 1.7 on the largest set avoiding a particular subset sum. Several supplementary results are consigned to the appendices.

## Notation

For the sake of clarity of presentation, we omit ﬂoor and ceiling signs whenever they are not essential. We also maintain the convention that all logarithms are natural logarithms unless otherwise speciﬁed.

# 2 Overview of the proofs of the main results

The techniques used to prove Theorems 1.1, 1.2, 1.6 and 1.9 all share some similarities. In each case, we reduce a problem over Z to the corresponding problem over Zm. In the cyclic setting, considering the structure of the “almost periods”, i.e., those elements whose inclusion does not signiﬁcantly expand the subset sum, allows us to transform our questions about subset sums into problems about iterated sumsets. The literature on iterated sumsets is extensive, allowing us to reach our desired conclusions by combining existing results on these sumsets with novel arguments from probabilistic combinatorics. In this section, we say more about the speciﬁc ideas that go into the proofs of each of our main theorems. The detailed proofs of these theorems and the other results described in the introduction are then in subsequent sections.

## 2.1 Some useful tools

We will repeatedly use the following simple lemma, allowing us to extend intervals in the set of subset sums by adding new elements. It is essentially Lemma 1 of Graham [26].

- Lemma 2.1 (Graham [26]). Let A be a set such that Σ(A) contains all integers in the interval [x,x + y).

- (i) If a is a positive integer with a ≤ y and a ∈/ A, then Σ(A ∪ {a}) contains all integers in the interval [x,x + y + a).
- (ii) If a1,... ,as are positive integers such that ai ≤ y + j<i aj and ai ∈/ A for i = 1,... ,s, then Σ(A ∪ {a1,a2,... ,as}) contains all integers in the interval [x,x + y + si=1 ai).


Proof. For the proof of the ﬁrst part, note that if u ∈ [x,x + y), then u ∈ Σ(A) ⊂ Σ(A ∪ {a}). If u ∈ [x + y,x + y + a), then u − a ∈ [x,x + y) ⊂ Σ(A), so u = (u − a) + a ∈ Σ(A ∪ {a}). The second part follows from the ﬁrst part by induction on s.

![image 43](<2021-conlon-subset-sums-completeness-colorings_images/imageFile43.png>)

![image 44](<2021-conlon-subset-sums-completeness-colorings_images/imageFile44.png>)

![image 45](<2021-conlon-subset-sums-completeness-colorings_images/imageFile45.png>)

![image 46](<2021-conlon-subset-sums-completeness-colorings_images/imageFile46.png>)

We will also make repeated use of the following result of Lev [30]. The importance of this result is that it allows us to ﬁnd long intervals in a set of subset sums by ﬁrst ﬁnding several dense subsets of long intervals and then summing these sets. Several weaker versions of this result appeared earlier in the literature, many of which would also suﬃce for our purposes.

- Lemma 2.2 (Lev [30]). Suppose ℓ,q ≥ 1 and n ≥ 3 are integers with ℓ ≥ 2⌈(q −1)/(n −2)⌉. If S1,... ,Sℓ are integer sets each having at least n elements, each a subset of an interval of at most q + 1 integers

and none a subset of an arithmetic progression of common diﬀerence greater than one, then S1 + ··· + Sℓ contains an interval of length at least ℓ(n − 1) + 1.

In working with general cyclic groups, the following analogue of the Cauchy–Davenport theorem, a consequence of Theorem 1.1 from [12], will also be useful to us. Given subsets A and B of an abelian group G, we deﬁne A + B = {a + b : a ∈ A,b ∈ B} and A − B = {a − b : a ∈ A,b ∈ B}. For k ∈ N, we deﬁne the k-fold sumset kA = A + A + ··· + A

![image 47](<2021-conlon-subset-sums-completeness-colorings_images/imageFile47.png>)

![image 48](<2021-conlon-subset-sums-completeness-colorings_images/imageFile48.png>)

k times

.

- Lemma 2.3 (Cochrane, Ostergaard and Spencer [12]). If A is a subset of an abelian group G which is not contained in a coset of a proper subgroup of G and r,s are non-negative integers which are not both zero, then


(r + s + 1)|A| 2

|rA − sA| ≥ min |G|,

.

![image 49](<2021-conlon-subset-sums-completeness-colorings_images/imageFile49.png>)

We will also make use of the following result of Deshouillers and Freiman [13]. The following corrected statement of the result appears in [4], where it is also shown that the hypothesis |A + A| ≤ 2.04|A| can be weakened to |A + A| ≤ 2.1|A|.

- Lemma 2.4 (Deshouillers and Freiman [13]). There exists a positive constant ξ such that if A is a subset

of Zm of size at most ξm with |A + A| ≤ 2.04|A|, then there exists a proper subgroup H ⊆ Zm such that either

- (i) A is a subset of an arithmetic progression of H-cosets of length ℓ with (ℓ − 1)|H| ≤ |A + A| − |A|,
- (ii) A meets exactly three H-cosets and these three H-cosets are terms of an arithmetic progression of H-cosets of length ℓ with (min(ℓ,4) − 1)|H| ≤ |A + A| − |A| or
- (iii) A is a subset of an H-coset and |A| ≥ ξ|H|.


Here an arithmetic progression of H-cosets of length ℓ is a set of the form i∈[ℓ](x + id + H), where x,d ∈ Zm and d ∈/ H.

The following simple lemma is crucial in the proofs of most of our main results.

- Lemma 2.5. Let m be an integer. Let A be a set of integers such that m ∈/ A and the size of Σ(A) considered modulo m is at least h, then |Σ(A ∪ {m})| ≥ |Σ(A)| + h.

Proof. The lemma follows since each modulo m class containing an element of Σ(A) contributes at least one new element to (Σ(A) + {m}) \ Σ(A).

![image 50](<2021-conlon-subset-sums-completeness-colorings_images/imageFile50.png>)

![image 51](<2021-conlon-subset-sums-completeness-colorings_images/imageFile51.png>)

![image 52](<2021-conlon-subset-sums-completeness-colorings_images/imageFile52.png>)

![image 53](<2021-conlon-subset-sums-completeness-colorings_images/imageFile53.png>)

In showing that there are many subset sums over cyclic groups, we use the following lemma, which shows that the set of new elements whose inclusion do not expand the set of subset sums is small.

- Lemma 2.6. Suppose A ⊂ Zm with d < |A| < m and let Gd be the set of x ∈ Zm such that |(A+x)∪A| ≤

|A| + d. Then |Gd| ≤ |A|

2

![image 54](<2021-conlon-subset-sums-completeness-colorings_images/imageFile54.png>)

|A|−d.

Proof. For each x ∈ Zm, |(A + x) ∩ (Zm \ A)| ≤ |A + x| = |A|, while if x ∈ Gd, |(A + x) ∩ (Zm \ A)| ≤ d by deﬁnition. Furthermore,

x∈Zm

|(A + x) ∩ (Zm \ A)| =

a∈A

|{x ∈ Zm : a + x ∈ Zm \ A}| =

a∈A

(m − |A|) = |A|(m − |A|),

where the second equality follows since, for each a ∈ A, a + x is an element of Zm \ A for exactly |Zm \ A| = m − |A| values of x. Thus,

|A|(m − |A|) ≤ |Gd| · d + (m − |Gd|)|A|,

from which we get the desired inequality by rearranging. We will often use the lemma above in combination with the following simple result.

![image 55](<2021-conlon-subset-sums-completeness-colorings_images/imageFile55.png>)

![image 56](<2021-conlon-subset-sums-completeness-colorings_images/imageFile56.png>)

![image 57](<2021-conlon-subset-sums-completeness-colorings_images/imageFile57.png>)

![image 58](<2021-conlon-subset-sums-completeness-colorings_images/imageFile58.png>)

- Lemma 2.7. If A ⊂ Zm and x1,... ,xk ∈ Zm satisfy |(A + xi) ∪ A| ≤ |A| + d for all i ∈ [k], then |(A + x1 + ··· + xk) ∪ A| ≤ |A| + kd.


Proof. We will show, by induction on i, that |(A + x1 + ··· + xi) ∪ A| ≤ |A| + id for 1 ≤ i ≤ k. This is clearly true for i = 1. For the induction step, assume that |(A + x1 + ··· + xi−1) ∪ A| ≤ |A| + (i − 1)d. Then

|(A + x1 + ··· + xi) ∪ A| − |A| = |(A + x1 + ··· + xi) \ A| ≤ |(A + x1 + ··· + xi) \ (A + xi)| + |(A + xi) \ A|

= |(A + x1 + ··· + xi−1) \ A| + |(A + xi) \ A| ≤ (i − 1)d + d = id.

Thus, |(A + x1 + ··· + xi) ∪ A| ≤ |A| + id for 1 ≤ i ≤ k.

![image 59](<2021-conlon-subset-sums-completeness-colorings_images/imageFile59.png>)

![image 60](<2021-conlon-subset-sums-completeness-colorings_images/imageFile60.png>)

![image 61](<2021-conlon-subset-sums-completeness-colorings_images/imageFile61.png>)

![image 62](<2021-conlon-subset-sums-completeness-colorings_images/imageFile62.png>)

## 2.2 Outline of the proof of the upper bounds in Theorems 1.1 and 1.2

The upper bound in Theorem 1.1 states that there exists a constant C such that, for every r ≥ 2, there is an r-Ramsey complete sequence A with |A ∩ [n]| ≤ Cr log2 n for all n. The following density-type result is the key to the proof of this statement.

- Lemma 2.8. Let C = 3840 and ǫ ∈ (0,1/2]. Let x be a positive integer. Let X be the set of integers in [x,2x) with no prime divisor at most (log x)/2. If a sequence S of Cǫ−1 log x elements in X is chosen independently and uniformly at random, then, with high probability (as x → ∞), S has distinct terms and, for any subsequence S′ of S of size ǫ|S| = C log x, the set Σ(S′) contains all integers in the interval [Cxlog4 x, 7Cx8logx].


![image 63](<2021-conlon-subset-sums-completeness-colorings_images/imageFile63.png>)

![image 64](<2021-conlon-subset-sums-completeness-colorings_images/imageFile64.png>)

The upper bound in Theorem 1.1 can be easily deduced from Lemma 2.8 as follows. Proof of the upper bound in Theorem 1.1. Let ǫ = 1/r and let x0 be large enough that the conclusion of

- Lemma 2.8 holds with positive probability for this choice of ǫ and x ≥ x0. Let xi = 2ix0 and yi = Cxi log xi. By Lemma 2.8, for each dyadic interval [xi,xi+1) with i ≥ 0 we can pick a sequence Si of Cr log xi distinct elements in this interval such that the set of subset sums of any subset of Si of size at least |Si|/r contains the integers in Ii := [yi/4,7yi/8]. Note that every r-coloring of Si has a color class of size at least |Si|/r and so the set of monochromatic subset sums of Si contains the integers in Ii. We pick the sequence A to be the concatenation of the sequences Si for i ≥ 0. Observe that, for all n, we have


A(n) ≤ i:n≤xi+1 |Si| ≤ Cr(log n)2. Moreover, since yi+1/4 < 7yi/8, the intervals Ii cover all integers

- at least y0/4. Thus, for every r-coloring of A, every suﬃciently large integer can be represented as a monochromatic subset sum. That is, the sequence A is r-Ramsey complete.


![image 65](<2021-conlon-subset-sums-completeness-colorings_images/imageFile65.png>)

![image 66](<2021-conlon-subset-sums-completeness-colorings_images/imageFile66.png>)

![image 67](<2021-conlon-subset-sums-completeness-colorings_images/imageFile67.png>)

![image 68](<2021-conlon-subset-sums-completeness-colorings_images/imageFile68.png>)

We now give an informal sketch of the proof of Lemma 2.8, showing how it follows from an appropriate combination of the results of Section 2.1 with some further ideas. To begin, we observe that for any ﬁxed set I of C log x indices in [Cǫ−1 log x], the elements of the subsequence (si : i ∈ I) of S of size ǫ|S| are independently and uniformly distributed in X. By taking a union bound, it will therefore suﬃce to show that if S′ is a sequence of C log x elements chosen independently and uniformly from X, then the probability that Σ(S′) does not contain all integers in the interval [Cxlog4 x, 7Cx8logx] is suﬃciently small.

![image 69](<2021-conlon-subset-sums-completeness-colorings_images/imageFile69.png>)

![image 70](<2021-conlon-subset-sums-completeness-colorings_images/imageFile70.png>)

For this, for some ﬁxed ℓ, we take ℓ disjoint random subsets S1′′,... ,Sℓ′′ of S′, each of size |S′|/(8ℓ), with the aim being to show that, with appropriately high probability, the set of subset sums Σ(Sj′′)

is a dense subset of a long interval and is not contained in an arithmetic progression with common diﬀerence larger than 1. Lemma 2.2 then allows us to conclude that S′′ = S1′′ ∪ ··· ∪ Sℓ′′ is such that Σ(S′′) = Σ(S1′′) + ··· + Σ(Sℓ′′) contains a long interval. Note, moreover, that S′′ only has size |S′|/8, so there are at least 7|S′|/8 elements still remaining in S′. Using Graham’s lemma, Lemma 2.1, we can use these elements to extend the long interval in Σ(S′′) to a signiﬁcantly longer interval containing all of the required elements.

It only remains to show that Σ(Sj′′) is a dense subset of a long interval with appropriately high probability (showing that it is also not contained in an arithmetic progression with common diﬀerence larger than 1 is reasonably straightforward). For this, we split Sj′′ randomly into two disjoint pieces P1 and P2. The key remaining component is to show that for every m ∈ X, the set of integers in [x,2x) with no prime factor at most (log x)/2, the mod m set of subset sums Σm(P1) is large with very high probability. Very roughly, this follows by exposing the elements of P1 one at a time and showing that most elements expand the mod m set of subset sums signiﬁcantly. Though we will not give a more detailed description here, we note that this key step again relies on several results from the previous section, including the Cauchy–Davenport-type statement, Lemma 2.3, as well as Lemma 2.6, which bounds the number of almost periods, those x for which (A + x) \ A is small. Finally, once we know that |Σm(P1)| is, with high probability, large for each m ∈ X, we can apply Lemma 2.5 repeatedly to conclude that |Σ(Sj′′)| ≥ m∈P2 |Σm(P1)|, which yields the required lower bound for |Σ(Sj′′)|.

The proof of Theorem 1.2 follows a similar scheme. Let P be a complete polynomial. By the characterization due to Graham [26] discussed in the introduction, we can write P(x) = ki=0 αi xi with αk > 0 and αi = pqi

, where pi and qi are relatively prime integers, qi > 0 and gcd(p0,... ,pk) = 1. If L = lcm(q0,... ,qk), then the polynomial L · P has integer coeﬃcients in its binomial representation and satisﬁes Graham’s condition, so it is also complete. Furthermore, if ((L·P)(an))∞n=1 is r-Ramsey complete, then (P(an))∞n=1 is r-Ramsey complete, so it suﬃces to work with complete polynomials which have integer coeﬃcients in their binomial representations. From now on, we will assume that P is such a polynomial.

![image 71](<2021-conlon-subset-sums-completeness-colorings_images/imageFile71.png>)

i

To prove Theorem 1.2, we prove the following polynomial analogue of Lemma 2.8. For a polynomial

- P and a sequence T of integers, let P(T) be the sequence where we replace each term t in T by P(t).


- Lemma 2.9. Let P be a complete polynomial of degree k with integer coeﬃcients in its binomial representation and let C(k) = k2k+15. Let ǫ ∈ (0,1/2]. Let x be a positive integer. Let X be the set of elements y in [x,(1 + 1/k)x) such that P(y) has no prime divisor at most (log x)1/2. If a sequence S of C(k)ǫ−1 log x elements in X is chosen independently and uniformly at random, then, with high probability (as x → ∞), S has distinct terms and, for any subsequence S′ of S of size ǫ|S|, the set Σ(P(S′)) contains all integers in the interval [9eP(x)|S′|, 98P(x)|S′|].


![image 72](<2021-conlon-subset-sums-completeness-colorings_images/imageFile72.png>)

![image 73](<2021-conlon-subset-sums-completeness-colorings_images/imageFile73.png>)

We now show how Theorem 1.2 follows from Lemma 2.9, just as the upper bound in Theorem 1.1 follows from Lemma 2.8.

Proof of Theorem 1.2. Let ǫ = 1/r. For each positive integer i, let xi = (1 + 1/k)i, yi = C(k)P(xi)log xi and Ii = [eyi/9,8yi/9]. For i suﬃciently large in terms of P and r, Lemma 2.9 implies that we can pick a subsequence Si of C(k)r log xi distinct terms in [xi,(1 + 1/k)xi) such that any subsequence S′ of Si with |Si|/r terms has the property that Σ(P(S′)) contains all integers in the interval Ii. Therefore, since every r-coloring of Si has a color class of size at least |Si|/r, the set of monochromatic subset sums of P(Si)

contains the integers in Ii. We pick the sequence A to be the concatenation of the sequences P(Si) with

- i suﬃciently large. Then, for all n, we have A(n) ≤ i:P(xi)≤n |Si| = Ok (log n)2 . Moreover, as xi is suﬃciently large, P(x) is increasing for x ≥ xi and P(xi+1) = P((1 + 1/k)xi) ≤ eP(xi). It follows that, for i suﬃciently large, eyi+1/9 ≤ 8yi/9 and the intervals Ii and Ii+1 are overlapping. Hence, the intervals
- Ii cover all suﬃciently large integers. Thus, for every r-coloring of A, every suﬃciently large integer can be represented as a monochromatic subset sum. That is, the sequence A is r-Ramsey complete.


![image 74](<2021-conlon-subset-sums-completeness-colorings_images/imageFile74.png>)

![image 75](<2021-conlon-subset-sums-completeness-colorings_images/imageFile75.png>)

![image 76](<2021-conlon-subset-sums-completeness-colorings_images/imageFile76.png>)

![image 77](<2021-conlon-subset-sums-completeness-colorings_images/imageFile77.png>)

The proof of Lemma 2.9 itself follows along broadly similar lines to the proof of Lemma 2.8. The key additional input, arising in the analogue of the step where we showed that |Σm(P1)| is large with high probability for each m ∈ X, is the following result on iterated sumsets of a set of polynomial values, proved through a form of PET induction (see, for example, [5]). For further details, we refer the reader to Section 3, where the proofs of Lemmas 2.8 and 2.9 are given in full.

- Lemma 2.10. There exists a constant Ck, depending only on k, such that if P is a complete polynomial of degree k with integer coeﬃcients in its binomial representation, x is suﬃciently large depending on P, m is an integer in [x,2x), (log x)−1 < α < 1/2 and T is a subset of [x,2x) of size at least αx, then the iterated sumset 2k−1P(T) − 2k−1P(T) contains more than αCkP(m) residue classes modulo P(m).


## 2.3 Outline of the proof of the lower bound in Theorems 1.5 and 1.6

Recall that, for any n ≤ m ≤ n2 , f(n,m) is deﬁned as the minimum r for which there is an r-coloring of [n − 1] such that m cannot be written as a sum of distinct monochromatic elements. In this section, we sketch the main ideas behind the lower bound in Theorem 1.6, which asymptotically determines the value of f(n,m). For simplicity, we will focus on the case m = n corresponding to Theorem 1.5, where we wish to show that f(n) = f(n,n) = Θ n

1/3(n/φ(n))

(logn)1/3(log logn)2/3 . Theorem 1.6 follows from an appropriate elaboration of these ideas.

![image 78](<2021-conlon-subset-sums-completeness-colorings_images/imageFile78.png>)

We begin by sketching Vu’s argument [43] (itself building on an argument used by Alon and Erdős [2]), which yields the bound f(n) ≥ c1logn1/n3 for some positive constant c1. To this end, consider an arbitrary r-coloring of [n] for some r < c1logn1/n3 . We restrict our attention to the interval [n2/3,2n2/3) and focus on the color class containing the largest number of primes from this interval. Let Q be the set of primes in this color class, noting that r < c1logn1/n3 implies that |Q| ≥ Cn1/3 for a positive constant C (which can be made arbitrarily large by taking c1 to be suﬃciently small). Partition Q into three subsets Q1, Q2 and

![image 79](<2021-conlon-subset-sums-completeness-colorings_images/imageFile79.png>)

![image 80](<2021-conlon-subset-sums-completeness-colorings_images/imageFile80.png>)

![image 81](<2021-conlon-subset-sums-completeness-colorings_images/imageFile81.png>)

- Q3 of roughly equal size. Since |Q1| ≥ C3 n1/3, we can apply the Szemerédi–Vu theorem, Theorem 1.8, to Q1 to obtain an arithmetic progression of length at least 2n2/3 in Σ(Q1). We can then complete this arithmetic progression of common diﬀerence d, say, to a long interval by building a complete modulo d


![image 82](<2021-conlon-subset-sums-completeness-colorings_images/imageFile82.png>)

class using Q2. Provided the parameters have been chosen appropriately, this interval will have length at least 2n2/3 and the minimum number in the interval will be smaller than n. Therefore, by Lemma 2.1, adding each element of Q3 in turn will expand the interval and, since adding all elements in Q3 would exceed n, the resulting interval in Σ(Q1 ∪ Q2 ∪ Q3) must contain n.

To go further, we make two observations about this argument. First, note that we passed immediately to a subset of the primes. This was in order to avoid the situation where a color class consists entirely of numbers with a given divisor, as, otherwise, it would be impossible to write any n which is not a multiple of this divisor as a sum of elements from the color class. Second, the key tool in the proof, Theorem 1.8, is

√2n−1/2⌋ positive integers has size less than n. However, this naive application of Theorem 1.8 makes no use of the fact that our set consists entirely of primes. It is here that we are able to gain.

![image 83](<2021-conlon-subset-sums-completeness-colorings_images/imageFile83.png>)

tight up to the constant, since the set of subset sums of the set consisting of the ﬁrst ⌊

To illustrate the main ideas in our argument, we ﬁrst restrict to the case where n is prime. Suppose then that there is an r-coloring of [n − 1], where r satisﬁes n = λr3(log r)(log log r)2 for a suﬃciently large constant λ. If we let y = Θ(r2(log r)(log log r)), the number of primes in the interval [y,2y) is Θ(r2 log log r), so, by the pigeonhole principle, there is a monochromatic subset Q of the primes in [y,2y) with |Q| = Ω(r log log r). As in Vu’s argument, the plan from this point is to use a subset V of Q of size O(r log log r) to build a large interval and then to apply Lemma 2.1 to expand this interval using the remaining elements. To show that Σ(V ) contains the required interval, we partition V into a bounded number of sets V1,V2,... ,Vℓ of roughly equal size and show that, for each i, Σ(Vi) contains a dense subset of an interval. Given this crucial input, Lemma 2.2 then implies that Σ(V ) contains a long interval.

Quantitatively, for this argument to go through, we need Σ(V ) to contain an interval of length Ω(r2(log r)(log log r)). For this to follow from Lemma 2.2, we need to have |Σ(Vi)| = Ω(r2(log r)(log log r)) for each Vi, themselves satisfying |Vi| = O(r log log r). Thus, we need to show that |Σ(Vi)|/|Vi| ≥ r log r, say. For this, we prove an inverse result, that if |Σ(Vi)|/|Vi| < r log r, then a large subset of Vi must be additively structured, in the sense that this subset is contained in a set of size O(|Vi|(log r)/(log log r)) which can be written as a union of long arithmetic progressions. We then use the Selberg sieve to show that, since Vi consists of primes, it is impossible for a large subset of Vi to have this structure.

In practice, as in the proofs of Theorems 1.1 and 1.2, we do much of our work over cyclic groups. Indeed, to show that Σ(Vi) is large, we partition Vi into two sets Ai,1 and Ai,2 and show that, for each a2 ∈ Ai,2, |Σ(Ai,1) (mod a2)| is large. Lemma 2.5 then allows us to conclude that Σ(Vi) = Σ(Ai,1 ∪ Ai,2) is large.

To show that |Σ(Ai,1) (mod a2)| is large, we consider an iterative building process which grows the set of subset sums modulo a2 by picking elements in Ai,1 one at a time. We begin with T0 = Ai,1 and Σ(0) = {0} ⊆ Za2. In step j ≥ 1, we choose an element xj from Tj−1 which maximizes |(Σ(j −1)+xj)\Σ(j −1)|, where the set Σ(j −1) is viewed as a subset of Za2, and then set Σ(j) = (Σ(j −1)+xj)∪Σ(j−1) and Tj = Tj−1\{xj}. If, for each j ≤ |Ai,1|/2, there is a choice of xj such that |(Σ(j−1)+xj)\Σ(j−1)| is large, then |Σ(Ai,1) (mod a2)| will be large, as required. If, instead, there is a step j such that |(Σ(j−1)+x)\Σ(j−1)| is small for all x ∈ Tj−1, then, using Lemma 2.4 (or, rather, its corollary, Lemma 5.7), we can show that Tj−1 is additively structured, in the sense that it is contained in a small set which is a union of long arithmetic progressions. By a version of the Selberg sieve, Tj−1 cannot then contain too many primes, contradicting the fact that, as a subset of Q, Tj−1 consists entirely of primes.

Several additional ideas are needed to handle the case where n is not prime. For instance, in the prime case, we could build the required sum n using only primes, but now we must use integers of the form qu, where u is a small divisor of n and q is coprime to the ﬁrst r primes. As before, our ﬁrst step is to pass to a large monochromatic subset Q0 of this set, the goal being to show that n is contained in the set of subset sums of Q0. In the prime case, we took a subset V of Q = Q0, partitioned it into sets Vi and then partitioned each Vi into sets Ai,1 and Ai,2, before showing that |Σ(Ai,1) (mod a2)| is large for each

- a2 ∈ Ai,2. However, this argument may not go through in the general case, because, when a2 is not prime, we could have that Ai,1, and hence Σ(Ai,1), is contained in a small proper subgroup of Za2.


To overcome this issue, we ﬁrst apply a preprocessing step to the set Q0, our aim being to ﬁnd a closely related set Q which is k-diverse, by which we mean that, for any d ≥ 2, there are at least k elements of Q which are not divisible by d. We obtain such a set through a simple iteration. Indeed, if we have a set which is not k-diverse, then there is some d dividing all but k elements of the set, so we can remove these elements from the set and divide the remaining elements by d to form a new set. Repeating this procedure with an appropriate value of k, we eventually arrive at a large k-diverse set Q such that {vx : x ∈ Q} ⊆ Q0 for some v|n. Thus, in order to conclude that n is a sum of elements in Q0, we only need to show that n/v is a sum of elements in Q.

A crucial property of diverse sets is that random subsets of a diverse set are themselves diverse with high probability. Thus, by taking a random subset V of Q, randomly partitioning V into parts Vi and then randomly partitioning each Vi into Ai,1 and Ai,2, we have that, with high probability, all of the sets Ai,1 are diverse. We can also show that any common divisor of a large subset of Ai,1 must be a small divisor of n. Proceeding now along the same lines as the prime case, this reduces our task to showing that |Σ(Ai,1) (mod a2)| is large for any diverse subset Ai,1 of A with the additional property that any common divisor of a large subset of Ai,1 is small.

To show that |Σ(Ai,1) (mod a2)| is large, we consider a more reﬁned version of the iterative building process used in the prime case. The details of this key step are contained in Lemma 5.6. We again begin with T0 = Ai,1 and Σ(0) = {0} ⊆ Za2 and, in step j ≥ 1, we again choose an element xj from Tj−1 and set Σ(j) = (Σ(j − 1) + xj) ∪ Σ(j − 1) and Tj = Tj−1 \ {xj}, but the process for choosing xj is more complex. To describe it, we let dj be the greatest common divisor of the elements in Tj−1. The choice of xj depends on the sets Su = Σ(j − 1) ∩ (u + djZa2) with u ∈ Za2/djZa2. We refer to step j as a growth phase, an unsaturated phase or a saturated phase, depending on whether there exists u such that Su is non-empty and small, no non-empty Su is small and at least one is of intermediate size or all non-empty Su are large, respectively. If j is a growth phase, we choose xj from Tj−1 so as to maximize |Σ(dj,j)| − |Σ(dj,j − 1)|, where Σ(dj,t) = { h∈H xh (mod a2) : H ⊆ [t] ∩ {h : dj|xh}}. If j is an unsaturated or saturated phase, we choose xj from Tj−1 so as to maximize |(Σ(j − 1) + xj) \ Σ(j − 1)|.

If now there is a saturated phase j among the ﬁrst |Ai,1|/2 steps, we can show that |Σ(Ai,1) (mod a2)| ≥ |Σ(j − 1)| is large, as required. On the other hand, we can also show that there are only a small number of growth phases among the ﬁrst |Ai,1|/2 steps. Hence, we can assume that there are many unsaturated phases. Our aim now is to show that |Σ(j)|−|Σ(j −1)| is large for any unsaturated phase, since, together with the fact that there are many unsaturated phases, this will imply that |Σ(Ai,1) (mod a2)| is large, as required. As in the prime case, this ﬁnal step proceeds by ﬁrst showing that if |Σ(j)| − |Σ(j − 1)| is not large, then Tj−1 must be additively structured, again that it is contained in a small set which is a union of long arithmetic progressions, and then using the Selberg sieve to derive a contradiction, in this case that Tj−1 cannot contain many elements of the form qu, where u is a small divisor of n and q is coprime to the ﬁrst r primes.

## 2.4 Outline of the proof of Theorem 1.9

To prove Theorem 1.9, that there exists a constant C such that any A ⊂ [n] with |A| ≥ C√n has a homogeneous progression of length n in Σ(A), we use a variant of the ideas discussed in Subsection 2.3. As in that subsection, we apply a preprocessing step to the set A to ﬁnd a set A′ of size comparable to A

![image 84](<2021-conlon-subset-sums-completeness-colorings_images/imageFile84.png>)

which is k-diverse for an appropriate k and for which there exists an integer d such that {dx : x ∈ A′} ⊆ A. We also maintain a further property, that A′ intersects each dyadic interval in either the empty set or a large set. Having obtained the required set A′, we replace A with this set and consider a random partition of the set into parts X1,Y1,... ,Xℓ,Yℓ.

The key step in the proof is Lemma 6.2, which roughly says that if Xi satisﬁes an appropriate diversity condition, then |Σ(Xi) (mod b)| is large for all b ∈ Yi. But since Xi is part of a random partition of the diverse set A, we can, with high probability, guarantee that Xi is also diverse and, therefore, by Lemma 6.2, that |Σ(Xi) (mod b)| is large for all b ∈ Yi. Then, as in the previous outlines, we apply

- Lemma 2.5, in this case together with what we know about the distribution of A in dyadic intervals, to

show that Σ(Xi ∪ Yi) is large, followed by Lemma 2.2 to conclude that Σ(A) contains a long interval. Unwinding the preprocessing step, we see that this interval corresponds to a long homogeneous arithmetic progression in the set of subset sums of the original set, as required.

At ﬁrst glance, Lemma 6.2 seems to bear close resemblance to one of the key steps in the proofs of Theorems 1.5 and 1.6 described in the previous subsection (and formally encapsulated in Lemma 5.6). In both cases, we wish to show that if X is a suﬃciently diverse set, then |Σ(X) (mod b)| is large for all b in a certain set Y . The diﬀerence lies in the fact that the sets X considered in Theorems 1.5 and 1.6 are carefully chosen so that we can hope for a stronger guarantee on the size of Σ(X) (mod b) than in the typical case, whereas here we are concerned precisely with that typical case. The proof of Lemma 6.2 follows from a similar iterative building process to that used in the proof of Lemma 5.6, as described at the end of the last subsection.

Because we need it for the proof of Theorem 1.7, our result on the largest subset of [n] avoiding a particular subset sum, we will actually prove a strengthening of Theorem 1.9, saying that we can build the required homogeneous progression using short sums, that is, sums with only a small number of terms. This strengthening requires a somewhat more careful analysis than that described above. In particular, we must start with T0 equal to a large random subset of Xi and Σ(0) = Xi \ T0 (mod b).

3 Ramsey completeness

3.1 Proof of the upper bound in Theorem 1.1

The goal of this section is to prove the upper bound in Theorem 1.1, that there exists a constant C such that, for every r ≥ 2, there is an r-Ramsey complete sequence A with |A ∩ [n]| ≤ Cr log2 n for all n. As shown in Section 2.2, this theorem follows from another statement, Lemma 2.8, whose proof will occupy us in this subsection.

The next lemma, a mod m analogue of Lemma 2.8, is the key step in proving that lemma. Let Σm(S) be the set of subset sums of S taken modulo m.

- Lemma 3.1. Fix c ≥ 6 and assume that x is suﬃciently large. Let w = (log x)/2 and let X be the set of integers in [x,2x) with no prime divisor at most w. Let m ∈ X. If a sequence S of clog x integers is chosen uniformly and independently at random from X and viewed as a sequence of elements in Zm, then |Σm(S)| < x4 with probability less than (log x)−(c−5) logx. Proof. Let W = p≤w p, where the product is taken over primes, and τ = φ(W)/W. The prime number


![image 85](<2021-conlon-subset-sums-completeness-colorings_images/imageFile85.png>)

theorem implies that W = e(1+o(1))w = x1/2+o(1). In any interval of length W, there are exactly τW integers with no prime divisor at most w. By Merten’s third theorem, τ = (e−γ + o(1)) /log w, where γ is the Euler–Mascheroni constant. It follows that

x 2log log x

|X| ≥ τ(x − W) ≥

.

![image 86](<2021-conlon-subset-sums-completeness-colorings_images/imageFile86.png>)

Let q = clog x. Let S = (s1,s2,... ,sq) be a sequence of q random elements of X. Let Si = (s1,... ,si) denote the sequence consisting of the ﬁrst i elements of S. Let δ = log log x/log x. Call i ∈ [2,q] bad if

- • |Σm(Si)| ≤ 23|Σm(Si−1)| and |Σm(Si−1)| ≤ x/log x or

![image 87](<2021-conlon-subset-sums-completeness-colorings_images/imageFile87.png>)

- • |Σm(Si)| ≤ (1 + δ)|Σm(Si−1)| and x/log x < |Σm(Si−1)| < x/4.


The following two claims allow us to quickly complete the proof.

- Claim 1. The probability that i is bad conditioned on the choice of Si−1 is at most p := 4(log logx)

2

![image 88](<2021-conlon-subset-sums-completeness-colorings_images/imageFile88.png>)

logx .

- Claim 2. If |Σm(S)| < x/4, then the number of integers in [2,q] which are not bad is less than 4log x. Assuming Claim 1, for any B ⊂ [2,q], the probability that all elements in B are bad is at most p|B|.


From Claim 2, if |Σm(S)| < x/4, then there is a set B of q − 4log x integers i ∈ [2,q] which are bad. Taking a union bound over all such choices of B, the probability that |Σm(S)| < x/4 is at most

4(log log x)2 log x

q q − 4log x

q 4log x

p|B| =

p|B| < c4 logx

![image 89](<2021-conlon-subset-sums-completeness-colorings_images/imageFile89.png>)

To complete the proof, it remains to verify Claims 1 and 2.

(c−4) log x

< (log x)−(c−5) logx.

![image 90](<2021-conlon-subset-sums-completeness-colorings_images/imageFile90.png>)

![image 91](<2021-conlon-subset-sums-completeness-colorings_images/imageFile91.png>)

![image 92](<2021-conlon-subset-sums-completeness-colorings_images/imageFile92.png>)

![image 93](<2021-conlon-subset-sums-completeness-colorings_images/imageFile93.png>)

- Proof of Claim 1. Fix Si−1 = (s1,... ,si−1). Conditioned on this choice of Si−1, we bound the probability that i is bad. If |Σm(Si−1)| ≥ x/4, then i cannot be bad (so the event that i is bad has probability zero). We

may therefore restrict attention to the two cases |Σm(Si−1)| ≤ x/log x and x/log x < |Σm(Si−1)| < x/4.

For the ﬁrst case, note, by Lemma 2.6, that the number of s with |Σm(Si−1 ∪ {s})| ≤ 32|Σm(Si−1)| is at most |Σm(Si−1)|

![image 94](<2021-conlon-subset-sums-completeness-colorings_images/imageFile94.png>)

2

![image 95](<2021-conlon-subset-sums-completeness-colorings_images/imageFile95.png>)

|Σm(Si−1)|/2 = 2|Σm(Si−1)|. Therefore, if |Σm(Si−1)| ≤ x/log x, the probability that i is bad conditioned on Si−1 is at most 2|Σm|X(S|i−1)| ≤ |X|2logx x ≤ 4 log loglogx x < p.

![image 96](<2021-conlon-subset-sums-completeness-colorings_images/imageFile96.png>)

![image 97](<2021-conlon-subset-sums-completeness-colorings_images/imageFile97.png>)

![image 98](<2021-conlon-subset-sums-completeness-colorings_images/imageFile98.png>)

Suppose now that x/log x < |Σm(Si−1)| < x/4. For a positive integer D, let GD be the set of s such that |Σm(Si−1∪{s})| ≤ |Σm(Si−1)|+D. Let d = ⌊δ|Σm(Si−1)|⌋, so i is bad in this case if and only if si ∈ Gd. Let k = ⌊21δ⌋, so kd ≤ |Σm(Si−1)|/2. By Lemma 2.7, kGd ⊆ Gkd, so |kGd| ≤ |Gkd| ≤ 2|Σm(Si−1)| < x2, where the middle inequality is again by the consequence of Lemma 2.6 noted above.

![image 99](<2021-conlon-subset-sums-completeness-colorings_images/imageFile99.png>)

![image 100](<2021-conlon-subset-sums-completeness-colorings_images/imageFile100.png>)

If |Gd| ≤ mw , then |Gd| ≤ mw ≤ (log2xx)/2 < 2δx. Otherwise, |Gd| > mw . In this case, since m has no prime divisor at most w, no subgroup of Zm has size larger than mw . Thus, Gd cannot be contained in a coset of a non-trivial subgroup. By Lemma 2.3, since |kGd| ≤ x2 < m, we must have |kGd| ≥ (k + 1)|Gd|/2 ≥ |Gd|/(4δ). Hence, |Gd| ≤ 4δ|kGd| ≤ 4δx/2 = 2δx. Thus, in either case, conditioned on the choice of Si−1, the probability that i is bad, which is the same as the probability that si ∈ Gd, is at most ||GXd|| ≤ 2|Xδx| ≤ 4δ log log x = p.

![image 101](<2021-conlon-subset-sums-completeness-colorings_images/imageFile101.png>)

![image 102](<2021-conlon-subset-sums-completeness-colorings_images/imageFile102.png>)

![image 103](<2021-conlon-subset-sums-completeness-colorings_images/imageFile103.png>)

![image 104](<2021-conlon-subset-sums-completeness-colorings_images/imageFile104.png>)

![image 105](<2021-conlon-subset-sums-completeness-colorings_images/imageFile105.png>)

![image 106](<2021-conlon-subset-sums-completeness-colorings_images/imageFile106.png>)

![image 107](<2021-conlon-subset-sums-completeness-colorings_images/imageFile107.png>)

![image 108](<2021-conlon-subset-sums-completeness-colorings_images/imageFile108.png>)

![image 109](<2021-conlon-subset-sums-completeness-colorings_images/imageFile109.png>)

![image 110](<2021-conlon-subset-sums-completeness-colorings_images/imageFile110.png>)

![image 111](<2021-conlon-subset-sums-completeness-colorings_images/imageFile111.png>)

![image 112](<2021-conlon-subset-sums-completeness-colorings_images/imageFile112.png>)

- Proof of Claim 2. As Si−1 ⊂ Si for i ∈ [2,q], Σm(Si−1) ⊂ Σm(Si) and, hence, 1 ≤ |Σm(S1)| ≤ ··· ≤ |Σm(Sq)| = |Σm(S)| < x4. Therefore, the number of i which are not bad with |Σm(Si−1)| ≤ x/log x and


![image 113](<2021-conlon-subset-sums-completeness-colorings_images/imageFile113.png>)

|Σm(Si)| ≥ 23|Σm(Si−1)| is at most log3/2 x, as we get a factor of 3/2 for each such i. Moreover, since (1+δ)δ−1 log2 logx ≥ 2log2 logx = log x, the number of elements i which are not bad with x/4 > |Σm(Si−1)| > x/log x and |Σm(Si)| ≥ (1 + δ)|Σm(Si−1)| is at most δ−1 log2 log x = log2 x, as we get a factor of 1 + δ for each such i. Therefore, the number of i ∈ [2,q] which are not bad is at most log3/2 x+log2 x < 4log x.

![image 114](<2021-conlon-subset-sums-completeness-colorings_images/imageFile114.png>)

![image 115](<2021-conlon-subset-sums-completeness-colorings_images/imageFile115.png>)

![image 116](<2021-conlon-subset-sums-completeness-colorings_images/imageFile116.png>)

![image 117](<2021-conlon-subset-sums-completeness-colorings_images/imageFile117.png>)

![image 118](<2021-conlon-subset-sums-completeness-colorings_images/imageFile118.png>)

We next prove Lemma 2.8 using Lemma 3.1. Let C = 3840, ǫ ∈ (0,1/2] and X be the set of integers in [x,2x) with no prime divisor at most (log x)/2, as in Lemma 3.1. We wish to show that if a sequence S of Cǫ−1 log x elements in X is chosen independently and uniformly at random, then, with high probability, S has distinct terms and, for any subsequence S′ of S of size ǫ|S| = C log x, the set Σ(S′) contains all integers in the interval [Cxlog4 x, 7Cx8logx].

![image 119](<2021-conlon-subset-sums-completeness-colorings_images/imageFile119.png>)

![image 120](<2021-conlon-subset-sums-completeness-colorings_images/imageFile120.png>)

![image 121](<2021-conlon-subset-sums-completeness-colorings_images/imageFile121.png>)

- Proof of Lemma 2.8. By the birthday paradox, as |S| = o( |X|), S has distinct terms with high probability. Fix a choice of subset I′ of [Cǫ−1 log x] of size C log x and consider the subsequence S′ of S given by


- (si)i∈I′. Let I′′ be the smallest |S′|/8 elements in I′ and let S′′ be given by (si)i∈I′′. Let ℓ = 40. Arrange I′′ in increasing order and partition I′′ into ℓ sets I1′′,... ,Iℓ′′ of consecutive terms so that each set Ij′′ for


j ∈ [ℓ] has size |I′′|/ℓ. This gives a partition of S′′ into ℓ subsequences S1′′,... ,Sℓ′′, where Sj′′ = (si)i∈I′′

. Note that |Sj′′| = C log8ℓ x and Σ(Sj′′) ⊆ [0,2xC log8ℓ x]. We shall prove below that, with high probability, the sequence S has the property that, for all possible choices of I′ and j, |Σ(Sj′′)| ≥ Cxlog x/64ℓ. Assuming this, we can show that Σ(Sj′′) is not contained in an arithmetic progression with common diﬀerence larger than 1. Indeed, if Σ(Sj′′) is contained in an arithmetic progression with common diﬀerence d > 1, then d ≤ (Cx(2Cxloglogx)/x(64)/(8ℓ)ℓ−)1 ≤ 17. Moreover, if Σ(Sj′′) is contained in an arithmetic progression with common diﬀerence d > 1, then all elements in Σ(Sj′′) are congruent modulo d, from which it follows that all elements of Sj′′ are divisible by d. This contradicts the fact that no element of Sj′′ has a prime factor at most (log x)/2 > 17. Hence, for each j, Σ(Sj′′) is not contained in an arithmetic progression with common diﬀerence larger than 1. Therefore, by Lemma 2.2, as Σ(S′′) = Σ(S1′′) + ··· + Σ(Sℓ′′), the set Σ(S′′) contains the integers in an interval of length at least ℓ Cx64logℓ x − 1 + 1 > 2x. Finally, by Lemma 2.1, Σ(S′) = Σ(S′′ ∪ (S′ \ S′′)) contains all integers in the interval [Cxlog4 x, 7Cx8logx], where we used that all elements of S′ are at most 2x, the elements of Σ(S′′) are at most 2x|S′′| = Cx4logx and the sum of the elements in S′ \ S′′ is at least 87|S′|x = 7Cx8logx.

j

![image 122](<2021-conlon-subset-sums-completeness-colorings_images/imageFile122.png>)

![image 123](<2021-conlon-subset-sums-completeness-colorings_images/imageFile123.png>)

![image 124](<2021-conlon-subset-sums-completeness-colorings_images/imageFile124.png>)

![image 125](<2021-conlon-subset-sums-completeness-colorings_images/imageFile125.png>)

![image 126](<2021-conlon-subset-sums-completeness-colorings_images/imageFile126.png>)

![image 127](<2021-conlon-subset-sums-completeness-colorings_images/imageFile127.png>)

![image 128](<2021-conlon-subset-sums-completeness-colorings_images/imageFile128.png>)

![image 129](<2021-conlon-subset-sums-completeness-colorings_images/imageFile129.png>)

![image 130](<2021-conlon-subset-sums-completeness-colorings_images/imageFile130.png>)

It remains to show that, with high probability, the sequence S has the property that, for all possible choices of I′ and j, |Σ(Sj′′)| ≥ Cxlog x/64ℓ. Fix an index 1 ≤ j ≤ ℓ and partition the index set Ij′′

- of Sj′′ into two consecutive blocks J1 and J2 of equal size. Let P1 = (si)i∈J1 and P2 = (si)i∈J2, so


′′ j |

- |P1| = |P2| = |S


2 = C640logx = clog x for c = 640C = 6. Recall that X is the set of integers in [x,2x) with no prime divisor at most (log x)/2. Consider m ∈ X. We note that when we ﬁx the subset of indices I′ of [Cǫ−1 log x] of size C log x and the index j, then J1 is determined as a particular subsequence of I′. Moreover, each element in P1 is uniformly and independently distributed in X. Taking a union bound over all xℓ CǫC−log1logxx choices of I′, j ∈ [ℓ] and m ∈ X, Lemma 3.1 implies that the probability |Σm(P1)| < x4 for some I′, j ∈ [ℓ] and m ∈ X is at most

![image 131](<2021-conlon-subset-sums-completeness-colorings_images/imageFile131.png>)

![image 132](<2021-conlon-subset-sums-completeness-colorings_images/imageFile132.png>)

![image 133](<2021-conlon-subset-sums-completeness-colorings_images/imageFile133.png>)

![image 134](<2021-conlon-subset-sums-completeness-colorings_images/imageFile134.png>)

xℓ

Cǫ−1 log x C log x ·

1 log x

![image 135](<2021-conlon-subset-sums-completeness-colorings_images/imageFile135.png>)

(c−5)(log x)

≤ 50x(e/ǫ)3840logx ·

1 log x

![image 136](<2021-conlon-subset-sums-completeness-colorings_images/imageFile136.png>)

log x

= ox(1),

where ox(1) tends to 0 as x tends to inﬁnity. Thus, with high probability, the sequence S is such that

|Σm(P1)| ≥ x4 for all choices of I′, j ∈ [ℓ] and m ∈ X. In this case, by repeated application of Lemma 2.5, for all j ∈ [ℓ],

![image 137](<2021-conlon-subset-sums-completeness-colorings_images/imageFile137.png>)

|Sj′′| 2

x 4 ·

Cxlog x 64ℓ

x 4

|Σ(Sj′′)| ≥

=

=

.

![image 138](<2021-conlon-subset-sums-completeness-colorings_images/imageFile138.png>)

![image 139](<2021-conlon-subset-sums-completeness-colorings_images/imageFile139.png>)

![image 140](<2021-conlon-subset-sums-completeness-colorings_images/imageFile140.png>)

![image 141](<2021-conlon-subset-sums-completeness-colorings_images/imageFile141.png>)

m∈P2

Therefore, with high probability, the sequence S is such that |Σ(Sj′′)| ≥ Cxlog x/64ℓ for all possible choices of I′ and j, as required.

![image 142](<2021-conlon-subset-sums-completeness-colorings_images/imageFile142.png>)

![image 143](<2021-conlon-subset-sums-completeness-colorings_images/imageFile143.png>)

![image 144](<2021-conlon-subset-sums-completeness-colorings_images/imageFile144.png>)

![image 145](<2021-conlon-subset-sums-completeness-colorings_images/imageFile145.png>)

## 3.2 Proof of Theorem 1.2

Our aim in this section is to prove Theorem 1.2, our main result on the Ramsey completeness of complete polynomial sequences (P(m))m≥1, saying that there exists a constant C, depending only on the degree of P, such that, for every r ≥ 2, there is an r-Ramsey complete sequence A ⊂ (P(m))m≥1 with |A ∩ [n]| ≤ Cr log2 n for all n. As remarked in Section 2.2, we can and will assume that P is a complete polynomial which has integer coeﬃcients in its binomial representation. That is, we can write P(x) = ki=0 αi xi , with αk > 0, each αi an integer and gcd(α0,... ,αk) = 1.

Our ﬁrst goal will be to prove Lemma 2.10. To recall the statement, suppose that P is a complete polynomial of degree k with integer coeﬃcients in its binomial representation, m is an integer in [x,2x), (log x)−1 < α < 1/2 and T is a subset of [x,2x) of size at least αx. Then Lemma 2.10 asserts that there is a constant Ck depending only on k such that, for x suﬃciently large, the iterated sumset 2k−1P(T) − 2k−1P(T) contains more than αCkP(m) residue classes modulo P(m). Once this lemma is in place, we will follow a scheme similar to that of the previous subsection to complete the proof.

- Proof of Lemma 2.10. Let T = {x0,x1,... ,xℓ−1}, where x ≤ x0 < x1 < ··· < xℓ−1 < 2x and ℓ ≥ αx. Let x0,i = xi and ℓ0 = ℓ. Let ℓj = ℓj−1(ℓj−1 − 1)/4x for j = 1,... ,k. For each j ∈ [k], we recursively construct a subsequence xj,0 < xj,1 < ··· < xj,ℓj−1 of T with ℓj terms, as follows. For each j ∈ [k], note that at least (ℓj−1 − 1) /2 of the indices 0 ≤ i ≤ ℓj−1 − 2 satisfy xj−1,i+1 − xj−1,i ≤ 2x/ℓj−1. Thus, by the pigeonhole principle, there is yj ∈ [2x/ℓj−1] such that at least ((ℓj−1 − 1)/2)/ (2x/ℓj−1) = ℓj indices 0 ≤ i ≤ ℓj−1 − 2 satisfy xj−1,i+1 − xj−1,i = yj. Let xj,i = xj−1,ti for ℓj increasing indices t0,t1,... ,tℓj−1 such that xj−1,ti+1 − xj−1,ti = yj. As x/(ℓj + 1) ≤ (2x/(ℓj−1 + 1))2, by iterating we get


x ℓj + 1 ≤

![image 146](<2021-conlon-subset-sums-completeness-colorings_images/imageFile146.png>)

x ℓ0 + 1

![image 147](<2021-conlon-subset-sums-completeness-colorings_images/imageFile147.png>)

2j

22(1+2+···+2j−1) ≤ α−2j22j+1. (2)

In particular, by (2) and the assumption α ≥ (log x)−1, we obtain that, for 1 ≤ j ≤ k, yj is bounded above by a polynomial function of log x depending on k.

Let P0 = P and recursively deﬁne

Pj(x) = Pj−1(x + yj) − Pj−1(x),

which is a polynomial in x of degree k−j whose coeﬃcients are polynomials in y1,... ,yj. Let zj := ji=1 yi. Then zj and the coeﬃcients of Pj are bounded in absolute value by a polynomial function of log x which depends on k and the coeﬃcients of P. This observation brings the following simple claim into play.

Claim. Let Q(x) = ki=0 βixi and Q˜(x) = ki=0 β˜ixi, where βi and β˜i are allowed to depend on x. If the

βi and β˜i are at most a ﬁxed polynomial function of log x in absolute value and βk = β˜k is bounded below in absolute value by some positive constant depending only on k, then limx→∞ QQ˜((xx)) = 1.

![image 148](<2021-conlon-subset-sums-completeness-colorings_images/imageFile148.png>)

Recall that P is a complete polynomial with integer coeﬃcients in its binomial representation P(x) =

k

- i=0 αi xi and the leading coeﬃcient αk is a positive integer. The coeﬃcient of xk−j in Pj(x) is the


same as that in αkzj k− xj . To see this, note, by induction, that the coeﬃcient of xk−j in Pj(x) = Pj−1(x+yj)−Pj−1(x) is the same as the coeﬃcient of xk−j in αkzj−1 k x−+jy+1j − k− xj+1 and, hence, of αkzj−1yj k− xj = αkzj k− xj . It follows from the claim that the polynomial Pj(x) is asymptotically equal to αkzj k− xj .

Let c = 1/(k2k+2) and wk−1 = 1. For 0 ≤ j ≤ k − 2, let wj = 2k−jyj+1. We choose (not necessarily disjoint) sets I0,I1,... ,Ik−1 of indices such that Ij ⊆ [ℓj] and any two distinct indices in Ij diﬀer by at least wj. By partitioning [x,2x) into 1/c intervals of length cx each, we can further guarantee that {x0,i0 : i0 ∈ I0} is a subset of an interval [x′,x′ + cx) of length cx that is a subinterval of [x,2x). By greedily picking the elements, we can guarantee that |I0| ≥ cℓ0/w0 and |Ij| ≥ ℓj/wj for j > 0.

For a k-tuple t = (i0,... ,ik−1) ∈ I0 × ··· × Ik−1, let

k−1

Pj(xj,ij).

F(t) =

j=0

We claim that these numbers are distinct modulo P(m). This follows from showing that (as integers) these numbers lie in an interval of length less than P(m) and that they are ordered lexicographically. That is, if t = (ij) and t′ = (i′j) are distinct k-tuples, j0 is the smallest index such that ij0 = i′j

and ij0 > i′j

, then F(t) > F(t′).

0

0

We ﬁrst show that the numbers F(t) with t ∈ I0×···×Ik−1 lie in an interval of length less than P(m). As x is suﬃciently large, each Pj is positive and increasing in [x,2x). It follows that

We have that

P(x′) +

Pj(x) ≤ F(t) ≤ P(x′ + cx) +

1≤j≤k−1

Pj(2x). (3)

1≤j≤k−1

P(x′ + cx) − P(x′) ≤ αk

≤ αk

x′ + cx k −

x′ k

2x k −

2x − cx k

+

j<k

+

= (2k − (2 − c)k)P(x) + R(x),

|αj|(x′ + cx)j

|αj|(2x)j

j<k

where R is a polynomial with degree at most k − 1 depending only on P. Thus, the diﬀerence between the upper and lower bounds for F(t) in (3) is, for x suﬃciently large, at most

P(x′ + cx) − P(x′) +

Pj(2x)

1≤j≤k−1

≤ (2k − (2 − c)k)P(x) + R(x) +

Pj(2x)

1≤j≤k−1

≤ ck2k−1P(x) ≤

- 1

![image 149](<2021-conlon-subset-sums-completeness-colorings_images/imageFile149.png>)

- 2


P(x) ≤

- 1

![image 150](<2021-conlon-subset-sums-completeness-colorings_images/imageFile150.png>)

- 2


P(m),

where, in the second inequality, we used that 2k − (2 − c)k < ck2k−1, as well as the claim and the fact that R(x) + 1≤j≤k−1 Pj(2x) is a polynomial of degree at most k − 1 in x whose coeﬃcients are polynomials (depending only on P) in y1,... ,yk−1, where y1,... ,yk−1 are themselves bounded in absolute value by a polynomial function of log x. Hence, the integers F(t) all lie in an interval of length at most P(m)/2 < P(m), as desired.

We next show that the integers F(t) with t ∈ I0 × ··· × Ik−1 are lexicographically ordered. Indeed, suppose t = (ij) and t′ = (i′j) are distinct k-tuples, j0 is the smallest index such that ij0 = i′j

and ij0 > i′j

. Then

0

0

k−1

F(t) − F(t′) =

). (4)

Pj(xj,ij) − Pj(xj,i′

j

j=j0

≥ ij − i′j ≥ wj, the ﬁrst summand in (4), when j = j0, is asymptotically at least αkzj0wj0 k−j x

Since xj,ij − xj,i′

j

0−1 . If j0 = k−1, the rest of the sum is 0. Otherwise, j0 ≤ k−2 and, since x ≤ xj,ij,x′j,i′

< 2x and Pj(x) is increasing for x suﬃciently large, the rest of the sum in (4) is at least

j

k−1

Pj(x) − Pj(2x).

j=j0+1

By the claim, this sum is asymptotic to its ﬁrst summand (when j = j0 + 1). Therefore, this sum is asymptotically −αkzj0+1(2k−j0−1−1) k−j x

0−1 . As zj0+1 = yj0+1zj0, we have zj0wj0 > 2zj0+1(2k−j0−1−1). Hence, as x is suﬃciently large, the ﬁrst term in the sum in (4) is more than the absolute value of the sum of the other terms, so we conclude that F(t) > F(t′), as desired.

As the integers F(t) with t ∈ I0 × ··· × Ik−1 are distinct modulo P(m), the number of distinct residue classes F(t) (mod P(m)) is at least

k−1

k−1

ℓj/wj ≥ ckxk

|Ij| ≥ c

j=0

j=0

k−1

α2j+1 ≥ ckα2k+1xk,

j=0

where ck > 0 depends only on k. Here we used yj ≤ 2x/ℓj−1, wj = 2k−jyj+1 by the deﬁnition of wj and the bound (2) on ℓj.

Note now that P0(x0,i) = P(xi) ∈ P(T). We will show, inductively, that for j ≥ 1 we have Pj(xj,i) ∈ 2j−1P(T) − 2j−1P(T) for all 0 ≤ i ≤ ℓj − 1. Indeed,

Pj(xj,i) = Pj−1(xj,i + yj) − Pj−1(xj,i) = Pj−1(xj−1,ti+1) − Pj−1(xj−1,ti) ∈ 2j−1P(T) − 2j−1P(T),

recalling that there exist indices ti such that xj,i = xj−1,ti and xj,i + yj = xj−1,ti+1. As each F(t) is the sum of k terms in which the jth term is of the form Pj(xj,i), we have that each F(t) is in the set P(T) + j k=1−1(2j−1P(T) − 2j−1P(T)) = 2k−1P(T) − (2k−1 − 1)P(T). The set 2k−1P(T) − 2k−1P(T) = −P(T) + 2k−1P(T) − (2k−1 − 1)P(T) is the union of | − P(T)| translates of 2k−1P(T) − (2k−1 − 1)P(T). Hence,

2k−1P(T) − 2k−1P(T) ≥ ckα2k+1xk > αCkP(m)

for an appropriate constant Ck depending only on k, completing the proof.

![image 151](<2021-conlon-subset-sums-completeness-colorings_images/imageFile151.png>)

![image 152](<2021-conlon-subset-sums-completeness-colorings_images/imageFile152.png>)

![image 153](<2021-conlon-subset-sums-completeness-colorings_images/imageFile153.png>)

![image 154](<2021-conlon-subset-sums-completeness-colorings_images/imageFile154.png>)

Remark. A Hilbert cube of dimension k (or simply a k-cube) is a set H(a0,e1,... ,ek) of the form {a0 + i∈I ei : I ⊆ [k]} with a0 an integer and e1,... ,ek positive integers (see [27] for more on the long history of these objects). The ﬁrst step in the proof of Lemma 2.10 was to iteratively build many Hilbert cubes of dimension k consisting of elements of T, all with ej = yj and where we can take a0 to be any xk,i. An alternative approach to this step is to build many k-cubes in T with small e1,... ,ek and then to use the pigeonhole principle to show that one can pick out many such k-cubes with the same e1,... ,ek.

As in the previous subsection, we will deduce Lemma 2.9 from a modular analogue, which we now state. Recall that Σm(S) is the set of subset sums modulo m.

- Lemma 3.2. Let P be a complete polynomial of degree k with integer coeﬃcients in its binomial representation. Fix c ≥ k2k+4 and assume x is suﬃciently large (depending on P). Let w = (log x)1/2 and let X be the set of y ∈ [x,(1 + 1/k)x) such that P(y) has no prime divisor at most w. Let m ∈ X. If S = (s1,... ,sq) is a sequence of q = clog x elements chosen uniformly and independently at random from X and the sequence P(S) = (P(s1),... ,P(sq)) is viewed as a sequence of elements in ZP(m), then |ΣP(m)(P(S))| < P(m)/4 with probability at most (log x)−(c−k2k+3)(logx)/(8Ck), where Ck is the constant deﬁned in Lemma 2.10.

We will need the following estimate for the proof of Lemma 3.2.

- Lemma 3.3. For each positive integer k, there is ck > 0 such that the following holds. Suppose P is a complete polynomial of degree k with integer coeﬃcients in its binomial representation. If x is suﬃciently large and 1 < w < (log x)/2 is an integer, then the set X of y ∈ [x,(1 + 1/k)x) such that P(y) has no prime divisor at most w satisﬁes |X| ≥ ck(log w)−kx.


Proof. For each prime q ≤ k, let vq be the largest integer v such that qv | k!. For i ≤ k, we have i−1 j=0(q2vq + (x − j)) = ij−=01(x − j) + q2vqz for some integer z, so

x + q2vq i −

x i

- i−1
- j=0


1 i!

1 i!

(q2vq + (x − j)) −

=

![image 155](<2021-conlon-subset-sums-completeness-colorings_images/imageFile155.png>)

![image 156](<2021-conlon-subset-sums-completeness-colorings_images/imageFile156.png>)

- i−1
- j=0


q2vqz i!

(x − j) =

.

![image 157](<2021-conlon-subset-sums-completeness-colorings_images/imageFile157.png>)

Letting vq,i and ri be integers such that i! = qvq,iri and gcd(ri,q) = 1, we have, since x+qi2vq − xi is an integer, that ri | z. Moreover, vq,i ≤ vq, since i! | k!. Hence,

x + q2vq i −

x i

q2vqz i!

z ri ≡ 0 (mod qvq).

= qvq · qvq−vq,i

=

![image 158](<2021-conlon-subset-sums-completeness-colorings_images/imageFile158.png>)

![image 159](<2021-conlon-subset-sums-completeness-colorings_images/imageFile159.png>)

That is, xi (mod qvq) is periodic every q2vq and, therefore, P(x) (mod q) is periodic every q2vq. Since P is complete, for each prime q ≤ k, there exists an integer x ∈ [1,q2vq] such that P(x) is coprime to

q. Using that q≤k, q prime q2vq = k!2, we have, by the Chinese Remainder Theorem, that there exists an integer y ∈ [1,k!2] such that P(y) is coprime to all primes q ≤ k. We also have that P(x) (mod q) is

periodic every k!2 for all primes q ≤ k. Moreover, for each prime q > k ≥ i, xi (mod q) is periodic every q. Therefore, letting Rk,w = k!2 k<q≤w,q prime q, we have that P(x) (mod q≤w, q prime q) is periodic every Rk,w.

Let W be the set of positive integers y at most Rk,w such that P(y) is coprime to all primes at most w. Let mP,q be the number of roots of P(x) (mod q), which is at most k for each prime q, where we used that P has degree k and is nonzero modulo q by completeness. By the Chinese Remainder Theorem, the fraction of y ∈ [ k<q≤w,q prime q] such that P(y) is coprime to k<q≤w,q prime q is then

k<q≤w,q prime

mP,q q ≥ c′k(log w)−k

1 −

![image 160](<2021-conlon-subset-sums-completeness-colorings_images/imageFile160.png>)

for some constant c′k > 0, where we used the bound 1 − ε > e−ε−ε2 for 0 < ε < 1/2 and Merten’s second theorem, which implies that q≤w,q prime 1/q = log log w+O(1). Furthermore, as shown above, there exists y ∈ [k!2] such that P(y) is coprime to q≤k, q prime q. Since P(y) (mod q≤k, q prime q) is periodic every k!2 and gcd(k!2, k<q≤w,q prime q) = 1, the Chinese Remainder Theorem implies that the fraction of y ∈ [Rk,w] such that P(y) is coprime to Rk,w is at least (c′k/k!2)(log w)−k. Hence, |W| ≥ (c′k/k!2)(log w)−kRk,w. Since the integers y for which P(y) has no prime factor at most w are periodic every Rk,w and Rk,w ≤ x1/2+o(1) by the assumption w ≤ (log x)/2, we have that |X| ≥ (|W|/Rk,w)(x/k) − |W| ≥ ck(log w)−kx for an appropriate ck > 0 depending only on k, as required.

![image 161](<2021-conlon-subset-sums-completeness-colorings_images/imageFile161.png>)

![image 162](<2021-conlon-subset-sums-completeness-colorings_images/imageFile162.png>)

![image 163](<2021-conlon-subset-sums-completeness-colorings_images/imageFile163.png>)

![image 164](<2021-conlon-subset-sums-completeness-colorings_images/imageFile164.png>)

The proof of Lemma 3.2 now proceeds along broadly similar lines to the proof of Lemma 3.1.

- Proof of Lemma 3.2. Let Si = (s1,... ,si) denote the sequence consisting of the ﬁrst i terms of S and let Ti = (P(s1),P(s2),... ,P(si)). We also write T as a shorthand for Tq = P(S). Call i ∈ [2,q] bad if


- • |ΣP(m)(Ti)| ≤ (1 + 2−k−1)|ΣP(m)(Ti−1)| and |ΣP(m)(Ti−1)| < P2(wm) or

![image 165](<2021-conlon-subset-sums-completeness-colorings_images/imageFile165.png>)

- • |ΣP(m)(Ti)| ≤ 1 + 2k+11 w |ΣP(m)(Ti−1)| and P2(wm) ≤ |ΣP(m)(Ti−1)| < P(4m). The following claims are the key components in the proof. Here Ck is the constant from Lemma 2.10.


![image 166](<2021-conlon-subset-sums-completeness-colorings_images/imageFile166.png>)

![image 167](<2021-conlon-subset-sums-completeness-colorings_images/imageFile167.png>)

![image 168](<2021-conlon-subset-sums-completeness-colorings_images/imageFile168.png>)

- Claim 1. The probability that i is bad conditioned on the choice of Si−1 is at most p := (log x)−1/(4Ck).
- Claim 2. If |ΣP(m)(T)| < P(m)/4, then the number of integers in [2,q] which are not bad is less than k2k+3 log x.


By Claim 1, for any B ⊂ [2,q], the probability that all elements in B are bad is at most p|B|. By Claim 2, if |ΣP(m)(T)| < P(m)/4, then there is a set B of q − k2k+3 log x = (c − k2k+3)log x integers i ∈ [2,q] which are bad. Taking a union bound over all choices of B, the probability that |ΣP(m)(T)| < P(m)/4 is at most

q q − k2k+3 log x

q k2k+3 log x

p|B| =

p|B|

≤ (ec)k2k+3 logx(log x)−(c−k2k+3)(logx)/(4Ck) < (log x)−(c−k2k+3)(logx)/(8Ck).

![image 169](<2021-conlon-subset-sums-completeness-colorings_images/imageFile169.png>)

![image 170](<2021-conlon-subset-sums-completeness-colorings_images/imageFile170.png>)

![image 171](<2021-conlon-subset-sums-completeness-colorings_images/imageFile171.png>)

![image 172](<2021-conlon-subset-sums-completeness-colorings_images/imageFile172.png>)

Therefore, in order to complete the proof of the lemma, it suﬃces to prove Claims 1 and 2. It is here, in the proof of Claim 1, that Lemma 2.10 comes into play.

- Proof of Claim 1. Fix Si−1 = (s1,... ,si−1). Conditioned on this choice of Si−1, we bound the probability that i is bad. If |ΣP(m)(Ti−1)| ≥ P(m)/4, then i cannot be bad (so the probability that i is bad is zero). The proof now splits into two cases, when |ΣP(m)(Ti−1)| < P2(wm) and when P2(wm) ≤ |ΣP(m)(Ti−1)| < P(m)/4.


![image 173](<2021-conlon-subset-sums-completeness-colorings_images/imageFile173.png>)

![image 174](<2021-conlon-subset-sums-completeness-colorings_images/imageFile174.png>)

- Case 1. |ΣP(m)(Ti−1)| < P2(wm). Let

![image 175](<2021-conlon-subset-sums-completeness-colorings_images/imageFile175.png>)

V = t ∈ [x,(1 + 1/k)x) : |ΣP(m)(Ti−1 ∪ {P(t)})| ≤ 1 +

- 1

![image 176](<2021-conlon-subset-sums-completeness-colorings_images/imageFile176.png>)

- 2k+1 |ΣP(m)(Ti−1)| .


Observe that i is bad conditioned on Si−1 if and only if si ∈ V . We will show that |V | ≤ αx, where α = w−1/Ck and Ck is again the constant from Lemma 2.10.

Suppose, for the sake of contradiction, that |V | > αx. Lemma 2.10 then implies that

|2k−1P(V ) − 2k−1P(V )| > αCkP(m) = P(m)/w,

where P(V ) = {P(v) : v ∈ V }. Note now that if U ⊆ ZP(m) and u ∈ ZP(m), then |ΣP(m)(U ∪ {u})| = |ΣP(m)(U ∪ {−u})|. Thus, for each z ∈ P(V ) ∪ (−P(V )), we have

|ΣP(m)(Ti−1 ∪ {z})| ≤ 1 +

- 1

![image 177](<2021-conlon-subset-sums-completeness-colorings_images/imageFile177.png>)

- 2k+1 |ΣP(m)(Ti−1)|


and Lemma 2.7 implies that, for each y ∈ 2k−1P(V ) − 2k−1P(V ),

|ΣP(m)(Ti−1 ∪ {y})| ≤ 1 +

2k 2k+1 |ΣP(m)(Ti−1)| =

![image 178](<2021-conlon-subset-sums-completeness-colorings_images/imageFile178.png>)

3 2|ΣP(m)(Ti−1)|. (5)

![image 179](<2021-conlon-subset-sums-completeness-colorings_images/imageFile179.png>)

However, by Lemma 2.6, the number of y ∈ ZP(m) satisfying (5) is at most 2|ΣP(m)(Ti−1)| < P(m)/w. But this contradicts the bound |2k−1P(V )−2k−1P(V )| > P(m)/w, so we must indeed have that |V | ≤ αx.

- Case 2. P(m)/2w ≤ |ΣP(m)(Ti−1)| < P(m)/4. Let


- 1

![image 180](<2021-conlon-subset-sums-completeness-colorings_images/imageFile180.png>)

- 2k+1w |ΣP(m)(Ti−1)| .


V = t ∈ [x,(1 + 1/k)x) : |ΣP(m)(Ti−1 ∪ {P(t)})| ≤ 1 +

Observe again that i is bad conditioned on Si−1 if and only if si ∈ V . As in Case 1, we will show that |V | ≤ αx. Indeed, suppose, for the sake of contradiction, that |V | > αx. Then, by Lemma 2.10, we again have that |2k−1P(V ) − 2k−1P(V )| > P(m)/w. By our assumption that P(m) has no prime divisor at most w, 2k−1P(V ) − 2k−1P(V ) cannot be contained in a coset of a proper subgroup of ZP(m). Hence, by

- Lemma 2.3, |2k−1wP(V ) − 2k−1wP(V )| > P(m)/2.


However, again using Lemma 2.7, for all elements y ∈ 2k−1wP(V ) − 2k−1wP(V ), we have

2kw 2k+1w |ΣP(m)(Ti−1)| =

3 2|ΣP(m)(Ti−1)|.

|ΣP(m)(Ti−1 ∪ {y})| ≤ 1 +

![image 181](<2021-conlon-subset-sums-completeness-colorings_images/imageFile181.png>)

![image 182](<2021-conlon-subset-sums-completeness-colorings_images/imageFile182.png>)

But, by Lemma 2.6, the number of such elements is at most 2|ΣP(m)(Ti−1)| < P(m)/2, a contradiction.

Therefore, in either case, the set V of bad choices satisﬁes |V | ≤ αx. By using Lemma 3.3, which says that |X| ≥ ck(log w)−kx for an appropriate ck > 0, this implies that the probability i is bad conditioned on the choice of Si−1 is at most

|V |/|X| ≤ αx/ ck(log w)−kx = αc−k 1(log w)k = c−k 1(log x)−1/(2Ck)

- 1

![image 183](<2021-conlon-subset-sums-completeness-colorings_images/imageFile183.png>)

- 2


log log x

k

< (log x)−1/(4Ck) = p,

- as required.

![image 184](<2021-conlon-subset-sums-completeness-colorings_images/imageFile184.png>)

![image 185](<2021-conlon-subset-sums-completeness-colorings_images/imageFile185.png>)

![image 186](<2021-conlon-subset-sums-completeness-colorings_images/imageFile186.png>)

![image 187](<2021-conlon-subset-sums-completeness-colorings_images/imageFile187.png>)

Proof of Claim 2. As Si−1 ⊂ Si for i ∈ [2,q], ΣP(m)(Ti−1) ⊆ ΣP(m)(Ti) and, hence, 1 ≤ |ΣP(m)(T1)| ≤ ··· ≤ |ΣP(m)(Tq)| = |ΣP(m)(T)| < P(m)/4. Therefore, the number of i which are not bad with |ΣP(m)(Ti−1)| < P(m)/2w and |ΣP(m)(Ti)| ≥ (1 + 2−k−1)|ΣP(m)(Ti−1)| is at most log(log(1+2P(2x−)k/−2w1)) ≤ k2k+2 log x. Moreover, the number of i which are not bad with P(m)/2w ≤ |ΣP(m)(Ti−1)| < P(m)/4 and |ΣP(m)(Ti)| ≥

![image 188](<2021-conlon-subset-sums-completeness-colorings_images/imageFile188.png>)

1 + 2k+11 w |ΣP(m)(Ti−1)| is at most log(1+2log(2−kw−1)w−1) ≤ log x, where we used that w = (log x)1/2. Therefore, the number of i ∈ [2,q] which are not bad is at most k2k+2 log x + log x < k2k+3 log x.

![image 189](<2021-conlon-subset-sums-completeness-colorings_images/imageFile189.png>)

![image 190](<2021-conlon-subset-sums-completeness-colorings_images/imageFile190.png>)

![image 191](<2021-conlon-subset-sums-completeness-colorings_images/imageFile191.png>)

![image 192](<2021-conlon-subset-sums-completeness-colorings_images/imageFile192.png>)

![image 193](<2021-conlon-subset-sums-completeness-colorings_images/imageFile193.png>)

![image 194](<2021-conlon-subset-sums-completeness-colorings_images/imageFile194.png>)

We conclude this subsection and the proof of Theorem 1.2 by using Lemma 3.2 to prove Lemma 2.9. To this end, suppose that P is a complete polynomial of degree k with integer coeﬃcients in its binomial representation, C(k) = k2k+15, ǫ ∈ (0,1/2] and X is the set of y ∈ [x,(1 + 1/k)x) such that P(y) has no prime divisor at most (log x)1/2. Our aim is to show that if a sequence S of C(k)ǫ−1 log x elements in X is chosen independently and uniformly at random, then, with high probability, S has distinct terms and, for any subsequence S′ of S of size ǫ|S|, the set Σ(P(S′)) contains all integers in the interval [9eP(x)|S′|, 89P(x)|S′|].

![image 195](<2021-conlon-subset-sums-completeness-colorings_images/imageFile195.png>)

![image 196](<2021-conlon-subset-sums-completeness-colorings_images/imageFile196.png>)

Proof of Lemma 2.9. As P is a complete polynomial, its leading coeﬃcient is positive. Hence, for x suﬃciently large, P will be positive and strictly increasing on the interval [x,(1 + 1/k)x]. We may therefore assume that P is injective on the interval [x,(1 + 1/k)x) and, for any y in this interval, P(y) ∈ [P(x),P((1 + 1/k)x)) ⊂ [P(x),eP(x)).

By the birthday paradox, as |S| = o( |X|), P(S) has distinct terms with high probability. Fix a choice of subset I′ of [C(k)ǫ−1 log x] of size C(k)log x and consider the subsequence S′ of S given by (si)i∈I′. Let I′′ be the smallest |S′|/9 elements in I′ and let S′′ be given by (si)i∈I′′. Let ℓ = 64. Arrange I′′ in increasing order and partition I′′ into ℓ sets I1′′,... ,Iℓ′′ of consecutive terms so that each set Ij′′ for j ∈ [ℓ] has size |I′′|/ℓ. This gives a partition of S′′ into ℓ subsequences S1′′,... ,Sℓ′′, where Sj′′ = (si)i∈I′′

![image 197](<2021-conlon-subset-sums-completeness-colorings_images/imageFile197.png>)

j

.

Note that each element of Σ(P(Sj′′)) is nonnegative and at most P((1+1/k)x)|Sj′′| < eP(x)|Sj′′|. We shall prove below that, with high probability, the sequence S has the property that, for all possible choices

of I′ and j, |Σ(P(Sj′′))| ≥ P(x)|Sj′′|/8. Assuming this, we can show that Σ(P(Sj′′)) is not contained in an arithmetic progression with common diﬀerence larger than 1. Indeed, if Σ(P(Sj′′)) is contained in an arithmetic progression with common diﬀerence d > 1, then d ≤ P((1+1/k)x)|S

′′ j |

![image 198](<2021-conlon-subset-sums-completeness-colorings_images/imageFile198.png>)

P(x)|Sj′′|/8−1 ≤ 9e. Moreover, if Σ(P(Sj′′)) is contained in an arithmetic progression with common diﬀerence d > 1, then all elements in Σ(P(Sj′′)) are congruent modulo d, from which it follows that all elements of P(Sj′′) are divisible by d. This contradicts the fact that no element of P(Sj′′) has a prime factor at most (log x)1/2. Hence, for each j, Σ(P(Sj′′)) is not contained in an arithmetic progression with common diﬀerence larger than 1. Therefore, by Lemma 2.2, as Σ(S′′) = Σ(S1′′)+···+Σ(Sℓ′′), the set Σ(S′′) contains the integers in an interval of length

- at least ℓ P(x)|Sj′′|/8 − 1 + 1 > P((1 + 1/k)x). Finally, by Lemma 2.1, Σ(P(S′′) ∪ P(S′ \ S′′)) contains


all integers in the interval [eP(x)|S′|/9,8P(x)|S′|/9], where we used that all elements of S′ are at most P((1+1/k)x), the elements of Σ(S′′) are at most P((1+1/k)x)|S′′| = P((1+1/k)x)|S′|/9 < eP(x)|S′|/9 and the sum of the elements in S′ is at least P(x)|S′ \ S′′| = 8P(x)|S′|/9.

It remains to show that, with high probability, the sequence S has the property that, for all possible choices of I′ and j, |Σ(P(Sj′′))| ≥ P(x)|Sj′′|/8. Fix an index 1 ≤ j ≤ ℓ and partition the index set Ij′′

- of Sj′′ into two consecutive blocks J1 and J2 of equal size. Let Q1 = (si)i∈J1 and Q2 = (si)i∈J2, so


′′ j |

- |Q1| = |Q2| = |S


2 = C(k18) logℓ x > k2k+4 log x. Recall that X is the set of integers in [x,(1 + 1/k)x) such that P(x) has no prime divisor at most (log x)1/2. Consider m ∈ X. We note that when we ﬁx the subset of indices I′ of [C(k)ǫ−1 log x] of size C(k)log x and the index j, then J1 is determined as a particular subsequence of I′. Moreover, each element in Q1 is uniformly and independently distributed in X. Taking a union bound over all xℓ C(Ck()kǫ) log−1 logx x choices of I′, j ∈ [ℓ] and m ∈ X, Lemma 3.2 implies that the probability |ΣP(m)(P(Q1))| < P(4m) for some choice of I′, j ∈ [ℓ] and m ∈ X is at most

![image 199](<2021-conlon-subset-sums-completeness-colorings_images/imageFile199.png>)

![image 200](<2021-conlon-subset-sums-completeness-colorings_images/imageFile200.png>)

![image 201](<2021-conlon-subset-sums-completeness-colorings_images/imageFile201.png>)

xℓ

C(k)ǫ−1 log x C(k)log x · (log x)−k2kC

−1

−1

k logx ≤ xℓ(e/ǫ)C(k) logx · (log x)−k2kC

k logx = ox(1),

where ox(1) tends to 0 as x tends to inﬁnity. Thus, with high probability, the sequence S is such that |ΣP(m)(P(Q1))| ≥ P(4m) for all possible choices of I′, j ∈ [ℓ] and m ∈ X. In this case, by repeated application of Lemma 2.5, for all j ∈ [ℓ],

![image 202](<2021-conlon-subset-sums-completeness-colorings_images/imageFile202.png>)

|Σ(P(Sj′′))| ≥

P(m)/4 = |Q2|P(m)/4 = |Sj′′|P(m)/8 ≥ P(x)|Sj′′|/8.

m∈Q2

Therefore, with high probability, the sequence S is such that |Σ(P(Sj′′))| ≥ P(x)|Sj′′|/8 for all possible choices of I′ and j, as required.

![image 203](<2021-conlon-subset-sums-completeness-colorings_images/imageFile203.png>)

![image 204](<2021-conlon-subset-sums-completeness-colorings_images/imageFile204.png>)

![image 205](<2021-conlon-subset-sums-completeness-colorings_images/imageFile205.png>)

![image 206](<2021-conlon-subset-sums-completeness-colorings_images/imageFile206.png>)

## 3.3 Proof of the lower bound in Theorem 1.1 We ﬁrst prove a useful lemma.

- Lemma 3.4. Let S be a sequence of positive integers and m and q be positive integers. Then


1 + 2−a/q ≤ 2m/q exp   a∈S∩[m]

2−a/q

|Σ(S) ∩ [m]| ≤ 2m/q

.

a∈S∩[m]

Proof. Let rS(s) denote the number of ways of representing s as a sum of distinct elements from S. So if s ∈ Σ(S), then rS(s) ≥ 1, while rS(s) = 0 otherwise. For each s ∈ Σ(S)∩[m], we get a contribution of one to the leftmost expression. For the middle expression, by expanding the product, for each s ∈ Σ(S) ∩ [m] we get a contribution of rS(s) · 2m/q · 2−s/q ≥ 1, proving the desired inequality. We then get the last inequality by using 1 + z ≤ ez for z ≥ 0.

![image 207](<2021-conlon-subset-sums-completeness-colorings_images/imageFile207.png>)

![image 208](<2021-conlon-subset-sums-completeness-colorings_images/imageFile208.png>)

![image 209](<2021-conlon-subset-sums-completeness-colorings_images/imageFile209.png>)

![image 210](<2021-conlon-subset-sums-completeness-colorings_images/imageFile210.png>)

Using the above lemma, we prove the following theorem, giving the lower bound in Theorem 1.1.

- Theorem 3.5. Let r ≥ 2 be an integer. If a sequence of positive integers A satisﬁes A(n) ≤ r140−1(log2 n)2 for all suﬃcently large n, then A is not r-Ramsey complete.


![image 211](<2021-conlon-subset-sums-completeness-colorings_images/imageFile211.png>)

Proof. By replacing r by r − 1 if r is odd, it suﬃces to prove that, for r ≥ 2 even, a sequence of positive integers A with A(n) ≤ 70r (log2 n)2 for all suﬃciently large n is not r-Ramsey complete.

![image 212](<2021-conlon-subset-sums-completeness-colorings_images/imageFile212.png>)

By reordering, we may suppose that A = (ai)∞i=1 is in increasing order a1 ≤ a2 ≤ ··· . Deﬁne an r/2-coloring of A, which we call the hue coloring, by assigning aℓ hue h ∈ Zr/2 if ℓ ≡ h (mod r/2). For a positive integer j, deﬁne a red/blue-coloring Cj of A where Cj(a) is red if a ≤ 2j and blue otherwise. Let cj be the product coloring formed from the hue coloring and the red/blue-coloring Cj. That is, cj is an r-coloring of A given by the hue and whether or not the term is at most 2j.

The largest positive integer that can be written as a sum of red elements of the same hue in coloring cj is at most

2 r

2j +

a. (6)

![image 213](<2021-conlon-subset-sums-completeness-colorings_images/imageFile213.png>)

a∈A∩[2j]

This follows since, for any two hues h and h′, the elements of A ∩ [2j] with hue h and those with hue h′ interlace and are bounded by 2j, so the sum of elements of hue h is at most 2j more than the sum of elements of hue h′ and, therefore, at most 2j more than the average sum of elements taken over all hues.

Let the cost of a ∈ A ∩ [2j] for the coloring cj be a/2jj. Over all colorings cj with j ≥ 1, the total cost of a > 2 is j≥log

2 a a/2jj ≤ 2/log2 a, while the cost of each a ∈ {1,2} over all such cj is at most 2. If any number larger than 2j−1(j + 2) can be written as a sum of monochromatic red elements in coloring cj (so they are also of the same hue), then, by (6), we have

2j +

2 r

a > 2j−1(j + 2),

![image 214](<2021-conlon-subset-sums-completeness-colorings_images/imageFile214.png>)

a∈A∩[2j]

or, equivalently, a∈A∩[2j] a > r2j−2j, so the total cost of all elements in A ∩ [2j] for the coloring cj is at least r/4.

Let i be a suﬃciently large positive integer. The total cost of the elements a ∈ A∩[2i] for the colorings c1,... ,ci is at most

2 log2 a

ri 32

, (7)

O(1) +

<

![image 215](<2021-conlon-subset-sums-completeness-colorings_images/imageFile215.png>)

![image 216](<2021-conlon-subset-sums-completeness-colorings_images/imageFile216.png>)

a∈A∩(2,2i]

where the O(1) term comes from considering the cost of the terms a ∈ {1,2}. To prove inequality (7), we use Abel’s summation formula

tnf(n) = T(x)f(x) − T(x0)f(x0) −

x0<n≤x

x

T(y)f′(y)dy,

x0

where f is a continuously diﬀerentiable function on [x0,x] and T(y) = n≤y tn. Using Abel’s summation formula with tn = 1 if n ∈ A∩(2i0,2i] and tn = 0 otherwise, where i0 is chosen so that A(n) ≤ 140r (log2 n)2 for all n ≥ 2i0, and f(x) = log1

![image 217](<2021-conlon-subset-sums-completeness-colorings_images/imageFile217.png>)

2 x, we obtain

![image 218](<2021-conlon-subset-sums-completeness-colorings_images/imageFile218.png>)

1 log2 a

![image 219](<2021-conlon-subset-sums-completeness-colorings_images/imageFile219.png>)

a∈A∩(2,2i]

A(2i) i −

A(2i0) i0

= O(1) +

+

![image 220](<2021-conlon-subset-sums-completeness-colorings_images/imageFile220.png>)

![image 221](<2021-conlon-subset-sums-completeness-colorings_images/imageFile221.png>)

2i

2i0

A(x)log 2 x(log x)2

dx

![image 222](<2021-conlon-subset-sums-completeness-colorings_images/imageFile222.png>)

ri2 140i

≤ O(1) +

+

![image 223](<2021-conlon-subset-sums-completeness-colorings_images/imageFile223.png>)

2i

2i0

r(log2 x)2 log 2 140x(log x)2

dx

![image 224](<2021-conlon-subset-sums-completeness-colorings_images/imageFile224.png>)

2ri 140

≤ O(1) +

<

![image 225](<2021-conlon-subset-sums-completeness-colorings_images/imageFile225.png>)

ri 65

,

![image 226](<2021-conlon-subset-sums-completeness-colorings_images/imageFile226.png>)

where we assume in the last inequality that i is suﬃciently large.

Thus, fewer than (ri/32)/(r/4) = i/8 of the i colorings cj with 1 ≤ j ≤ i have the property that there is a number greater than 2j−1(j +2) that can be expressed as a sum of elements which are red of the same hue. We call j red-strong if there is a number greater than 2j−1(j + 2) that can be expressed as a sum of elements which are red of the same hue in the coloring cj.

For a non-negative integer j, deﬁne

2−a/2j+4.

g(j) =

a∈A,2j<a≤2jj

For each a ∈ A, the contribution of a to the various g(j) is

2−a/2j+4 ≤

j:2j<a≤2jj

2−2h−4 < 5,

h≥0

where we used the change of variables h = ⌊log2 a⌋ − j. Hence,

- i
- j=1


5 = 5A(i2i).

g(j) <

a∈A∩[2ii]

For s ∈ Zr/2, let As be the subset of A consisting of elements of hue s. Let As,>t = {a ∈ As : a > t}. Let b(j) denote the number of elements of [2jj] which can be written as a sum of blue elements in coloring cj of the same hue, so b(j) = | r/s=12 Σ(As,>2j) ∩ [2jj]| ≤ r/s=12 |Σ(As,>2j) ∩ [2jj]|. Applying Lemma 3.4 with S = As,>2j, m = 2jj and q = 2j+4, we have

  

   ≤ 2j/16 exp 1 +

2 r

2−a/2j+4

Σ(As,>2j) ∩ [2jj] ≤ 2j/16 exp

g(j) ,

![image 227](<2021-conlon-subset-sums-completeness-colorings_images/imageFile227.png>)

a∈As,>2j ∩[2jj]

where we have again used the fact that, for any two hues h and h′, the blue elements with hue h interlace the blue elements of hue h′ together with the observation that the function x  → 2−2x−4 is monotone and bounded above by 1. We thus have b(j) ≤ 2r2j/16 exp 1 + 2rg(j) . Hence, for i suﬃciently large,

![image 228](<2021-conlon-subset-sums-completeness-colorings_images/imageFile228.png>)

![image 229](<2021-conlon-subset-sums-completeness-colorings_images/imageFile229.png>)

g(j) ≤ ri2i2/31 exp 

g(j)

- i
- j=1


- i
- j=1


- i
- j=1


2 r

10 r

2 r

r 2

A(i2i) < 2i2/4.

 ≤ ri2i2/31 exp

2j/16exp 1 +

b(j) ≤

![image 230](<2021-conlon-subset-sums-completeness-colorings_images/imageFile230.png>)

![image 231](<2021-conlon-subset-sums-completeness-colorings_images/imageFile231.png>)

![image 232](<2021-conlon-subset-sums-completeness-colorings_images/imageFile232.png>)

![image 233](<2021-conlon-subset-sums-completeness-colorings_images/imageFile233.png>)

(8)

If at least 3i/4 of the i colorings cj for j = 1,... ,i have the property that at least 2j positive integers at most 2jj can be written as a sum of blue elements of the same hue, then the left hand side of (8) is at least j 3=1i/4 2j = 2(3i/24+1) > 2i2/4, contradicting (8). Hence, for at least i/4 of the colorings cj with

- j = 1,... ,i, we have that there are at most 2j positive integers at most 2jj which can be written as a


sum of blue elements of the same hue in A. Call j blue-strong if in coloring cj at least 2j positive integers at most 2jj can be written as a sum of blue elements of the same hue in A. Call j weak if it is neither

blue-strong nor red-strong. Hence, for i suﬃciently large, there are at least i − i/8 − 3i/4 = i/8 elements j ∈ [i] which are weak. Thus, there are inﬁnitely many weak j and we let J = {jh}h≥1 be an inﬁnite sequence of weak j so that jh ≥ 2rjh2−1.

We next deﬁne an r-coloring c of A for which there are inﬁnitely many integers which cannot be written as a sum of monochromatic elements from A. The coloring c is a product coloring of the hue coloring (which uses r/2 colors) and a red/blue-coloring of A. We color an integer in A blue if it is in one of the intervals (2j,2jj] with j ∈ J and red otherwise. We will prove that at least half the elements in (2j−1(j + 2),2jj], where j ∈ J is suﬃciently large, cannot be written as a monochromatic sum in the coloring c.

Suppose now that N ∈ (2j−1(j + 2),2jj] is a sum of red elements of the same hue. Since there are no red elements in (2j,2jj] in the coloring c, N can also be written as a sum of red elements of the same hue in cj, contradicting the assumption that j is weak. Hence, no element in (2j−1(j + 2),2jj] is a sum of red elements of the same hue in the coloring c.

As j = jh is weak, there are at most 2j elements at most 2jj that can be written as a monochromatic sum of blue elements of the same hue in (2j,2jj]. The number of remaining blue elements in [2jj] is at most

rjh2−1 2 ≤

r 140

log2 j 2

A(2jh−1jh−1) ≤

(log2(2jh−1jh−1))2 ≤

.

![image 234](<2021-conlon-subset-sums-completeness-colorings_images/imageFile234.png>)

![image 235](<2021-conlon-subset-sums-completeness-colorings_images/imageFile235.png>)

![image 236](<2021-conlon-subset-sums-completeness-colorings_images/imageFile236.png>)

Thus, the number of positive integers at most 2jj which can be written as a monochromatic sum of blue elements in the coloring c is at most 2(log2 j)/22j < 2jj/8. Hence, as 2jj/8 ≤ 21 2jj − 2j−1(j + 2) , at least half the elements in (2j−1(j + 2),2jj] cannot be written as a sum of blue elements of the same hue in the coloring c. As there are inﬁnitely many such j, there are inﬁnitely many positive integers which are not the monochromatic sum of elements in the coloring c. This completes the proof.

![image 237](<2021-conlon-subset-sums-completeness-colorings_images/imageFile237.png>)

![image 238](<2021-conlon-subset-sums-completeness-colorings_images/imageFile238.png>)

![image 239](<2021-conlon-subset-sums-completeness-colorings_images/imageFile239.png>)

![image 240](<2021-conlon-subset-sums-completeness-colorings_images/imageFile240.png>)

![image 241](<2021-conlon-subset-sums-completeness-colorings_images/imageFile241.png>)

Remark. In the proof above, for j = 1,... ,i, we made use of colorings Cj which color the positive integers up to 2j red and all larger integers blue. Alternatively, we could have picked a random coloring φx which colors all positive integers up to x red and all larger integers blue, where x ∈ [N] is chosen with probability

1 xH(N) with H(N) = Nx=1 x1. One can then do a similar analysis using elementary probability to get a better constant factor in Theorem 3.5.

![image 242](<2021-conlon-subset-sums-completeness-colorings_images/imageFile242.png>)

![image 243](<2021-conlon-subset-sums-completeness-colorings_images/imageFile243.png>)

# 4 Density completeness

In this section, we discuss Theorems 1.3 and 1.4, our results on density completeness. Since reordering a sequence does not change whether or not it is ǫ-complete, it will suﬃce to consider monotonically increasing sequences. We will begin with the following simple result, from which the ﬁrst part of Theorem 1.3 follows.

- Theorem 4.1. Let ǫ > 0. If A = (an)n≥1 is a monotonically increasing sequence of positive integers which is ǫ-complete, then there is C such that


holds for all positive integers n.

an ≤

ai

i≤ǫn+C

Proof. Suppose that there is no such C. Then there is a function g : N → N with limn→∞ g(n) = ∞ such that an > i≤ǫn+g(n) ai holds for inﬁnitely many n. Thus, we can pick an inﬁnite sequence of

j+g(nj) ai and g(nj) > nj−1. Pick a subsequence A′ of A by deleting all elements ai of A whose subscript i satisﬁes ǫnj + g(nj) < i ≤ nj for some positive integer j.

positive integers n1,n2,... such that, for all j, we have anj > i≤ǫn

We ﬁrst show that A′(x) ≥ ǫA(x) holds for all x. It suﬃces to check this when x = anj for some positive integer j. However, we have A′(anj) ≥ ǫnj + g(nj) − nj−1 > ǫnj = ǫA(anj), as required.

To see that A′ is not complete, we show that each integer anj is not the sum of elements from A′. Indeed, such elements must be at most anj and hence at most aǫnj+g(nj). However, i≤ǫn

j+g(nj) ai < anj, so anj is not in Σ(A′) and A′ is not complete.

![image 244](<2021-conlon-subset-sums-completeness-colorings_images/imageFile244.png>)

![image 245](<2021-conlon-subset-sums-completeness-colorings_images/imageFile245.png>)

![image 246](<2021-conlon-subset-sums-completeness-colorings_images/imageFile246.png>)

![image 247](<2021-conlon-subset-sums-completeness-colorings_images/imageFile247.png>)

This gives a necessary growth condition for a sequence to be ǫ-complete. Recall that it is also necessary for an ǫ-complete sequence to satisfy the divisibility condition that no prime is a factor of more than an ǫ-proportion of the elements in the sequence. In the proof of Theorem 4.3 below, we show that, apart from some mild additional assumptions, a random sequence satisfying both the growth condition from Theorem 4.1 and a suitable variant of this divisibility condition is likely to be ǫ-complete.

Recall that, for a sequence B = (bn)n≥1, the discrete derivative is deﬁned by ∆bn := bn+1 − bn. Fix

- 0 < ǫ < 1. A sequence B = (bn)n≥1 is called ǫ-friendly (or friendly) if it satisﬁes the following ﬁve growth conditions:


- (i) For some constant C and all n,

bn ≤

i≤ǫn+C

bi.

- (ii) limn→∞ ∆bn = ∞.
- (iii) limi→∞ B(2

i+1)−B(2i)

![image 248](<2021-conlon-subset-sums-completeness-colorings_images/imageFile248.png>)

i = ∞.

- (iv) There exists 0 < c < 1 such that c∆bi ≤ ∆bj for all i < j. Moreover, if bj < 2bi, then ∆bj ≤ 1c∆bi.

![image 249](<2021-conlon-subset-sums-completeness-colorings_images/imageFile249.png>)

- (v) B is strictly increasing.


By Theorem 4.1, condition (i) is necessary for an increasing sequence of positive integers to be ǫ-complete. The other growth conditions are mild assumptions that will be helpful in proving the existence of an ǫ-complete sequence A = (an)n≥1 which interlaces B, that is, for which bn ≤ an ≤ bn+1 for all n.

Let b1,b2,... ,bt be any ﬁnite strictly increasing sequence of positive integers. Let {x} = x−⌊x⌋ denote the fractional part of x. If we deﬁne B = (bn)n≥1 recursively by

bn = ⌊{ǫn}b⌈ǫn⌉⌋ +

bi

i≤ǫn

for n > t, then it is easy to check that such a sequence is friendly and satisﬁes bn = Θ(fn), where, following the introduction, F = (fn)n≥1 is any sequence of positive integers for which fn = i≤ǫn fi for all suﬃciently large n. We note that the term ⌊{ǫn}b⌈ǫn⌉⌋ is added as a “discrete interpolation” factor to guarantee conditions (ii) and (iv) of friendly sequences.

Claim 4.2. If B = (bn)n≥1 is a friendly sequence and n is a suﬃciently large positive integer, then b2n/c+1 ≥ 2bn+1, where c is the constant in condition (iv) of friendly sequences.

Proof. We have

and

bn+1 = b1 +

n

∆bi (9)

∆bi ≤ b1 + nmax

i≤n

i=1

2n/c

b2n/c+1 = bn+1 +

∆bi

i=n+1

≥ bn+1 + (2n/c − n)min j≥n

∆bj ≥ bn+1 + (n/c) · cmax

∆bi + (n/c − n)min j≥n

∆bj ≥ bn+1 + (n/c) · cmax

i≤n

∆bi + b1 ≥ 2bn+1.

i≤n

Here we used condition (iv) of friendly sequences to deduce the second inequality, the third inequality follows from (n/c − n)minj≥n ∆bj > b1 for n suﬃciently large and the last inequality is by (9).

![image 250](<2021-conlon-subset-sums-completeness-colorings_images/imageFile250.png>)

![image 251](<2021-conlon-subset-sums-completeness-colorings_images/imageFile251.png>)

![image 252](<2021-conlon-subset-sums-completeness-colorings_images/imageFile252.png>)

![image 253](<2021-conlon-subset-sums-completeness-colorings_images/imageFile253.png>)

The next theorem is our main result on ǫ-complete sequences and completes the proof of Theorem 1.3. We remark that since condition (i) of friendly sequences only gives an upper bound on bn, this result also allows us to ﬁnd sequences that are considerably denser than (fn)n≥1 that are ǫ-complete.

Theorem 4.3. Let 0 < ǫ < 1 and B = (bn)n≥1 be a friendly sequence as deﬁned above. Then there is a sequence A = (an)n≥1 of positive integers that interlaces B, i.e., bn ≤ an < bn+1 for all n, which is ǫ-complete.

Proof. Let ǫ0 > 0 be suﬃciently small. We pick the sequence A by taking, for j suﬃciently large, aj to be a uniform random integer in [bj,bj+1) which has no prime factor at most (max(1/ǫ,1/ǫ0))4000. For small j this might not be possible, as the interval [bj,bj+1) might not contain any integer with no prime factor at most (max(1/ǫ,1/ǫ0))4000, so we let aj be any integer in [bj,bj+1) in this case. This guarantees that A interlaces B.

For a positive integer i, let h(i) be the smallest integer for which bh(i) ≥ 2i. Note that bh(i+1)−1 is the largest element of B which is less than 2i+1. Let Ai := A ∩ [bh(i),bh(i+1)−1), so Ai consists of all but at most two elements of A∩[2i,2i+1). By condition (iii) of friendly sequences, for any C and for i suﬃciently large depending on C, |Ai| ≥ C max(1/ǫ,1/ǫ0)i. The following lemma is a close relative of Lemma 2.8. The proof of the lemma, which is an appropriate modiﬁcation of the proof of Lemma 2.8, is deferred to

- Appendix A.2.


- Lemma 4.4. There exist positive constants ǫ0, C1 and C2 such that the following holds. For i suﬃciently large, with positive probability, the set Ai has the property that, for any subset A′i ⊂ Ai with |A′i| ≥ (min(ǫ,ǫ0)/4)|Ai|, A′i contains a subset A′′i with |A′′i | ≤ C1i such that Σ(A′′i ) contains every integer in the interval [y,2y], where y = C22ii.


Since the choices of Ai for diﬀerent i are mutually independent, we can guarantee and will assume that Ai satisﬁes the conclusion of Lemma 4.4 for each suﬃciently large i.

Our goal now is to show that if A′ is any subsequence of A with |A′(n)| ≥ ǫ|A(n)| for all suﬃciently large n, then A′ is complete. We ﬁrst show that for each n0 there is n ≥ n0 such that A′ is complete or

A′ contains only roughly ǫn elements among the ﬁrst n elements of A. We then go through a very similar argument using this additional structure to conclude that A′ is complete.

Let i0 be a suﬃciently large positive integer and m = A(2i0). The number of elements in A which are at most 2i0 and not in any Ai is at most 2i0 ≤ 4ǫm. Let A′i = Ai ∩ A′. So the set i≤i

A′i of elements in A′ which are at most 2i0 and in some Ai has size at least ǫA(2i0) − 4ǫm ≥ 34ǫm. Let i1 ≤ i0 be the largest positive integer for which |A′i

![image 254](<2021-conlon-subset-sums-completeness-colorings_images/imageFile254.png>)

0

![image 255](<2021-conlon-subset-sums-completeness-colorings_images/imageFile255.png>)

![image 256](<2021-conlon-subset-sums-completeness-colorings_images/imageFile256.png>)

| ≥ 4ǫ|Ai1|, which exists by the observation just made. The set i

1<i≤i0 A′i has cardinality at most 4ǫ| i1<i≤i0 Ai| ≤ 4ǫm, so there are at least 34ǫm − 4ǫm = 2ǫm elements in i≤i

![image 257](<2021-conlon-subset-sums-completeness-colorings_images/imageFile257.png>)

1

A′i. In particular, A(2i1+1) ≥ A′(2i1+1) ≥ 2ǫm.

![image 258](<2021-conlon-subset-sums-completeness-colorings_images/imageFile258.png>)

![image 259](<2021-conlon-subset-sums-completeness-colorings_images/imageFile259.png>)

![image 260](<2021-conlon-subset-sums-completeness-colorings_images/imageFile260.png>)

![image 261](<2021-conlon-subset-sums-completeness-colorings_images/imageFile261.png>)

![image 262](<2021-conlon-subset-sums-completeness-colorings_images/imageFile262.png>)

1

![image 263](<2021-conlon-subset-sums-completeness-colorings_images/imageFile263.png>)

Since Ai1 satisﬁes the conclusion of Lemma 4.4 and |A′i

| ≥ (ǫ/4)|Ai1| ≥ (min(ǫ,ǫ0)/4)|Ai1|, there is A′′i

1

⊂ A′i

with |A′′i

| ≤ C1i1 such that Σ(A′′i

) contains every integer in the interval [y,2y] where

1

1

1

1

in increasing order as a′1,a′2,.... By Lemma 2.1, if, for each j, we have a′j ≤ 2y − y +a′1 +··· +a′j−1, then Σ(A′ \ A′′i

- y = C22i1i1. Label the elements in A′ \ A′′i


1

) +[y,2y) contains all integers at least y and, as Σ(A′) is a superset of Σ(A′ \ A′′i

1

) + [y,2y), A′ would be complete. So we may assume that there is some j for which

1

a′j > y + a′1 + ··· + a′j−1. (10)

2m ≥ 2ǫm, so that j can be made suﬃciently large by taking i0 and, hence, m suﬃciently large.

In particular, a′j ≥ 2i1+1 ≥ aǫ

![image 264](<2021-conlon-subset-sums-completeness-colorings_images/imageFile264.png>)

![image 265](<2021-conlon-subset-sums-completeness-colorings_images/imageFile265.png>)

⊂ A, there is a positive integer n for which a′j = an, where, again, n can be made suﬃciently large by taking i0 suﬃciently large. We have

As a′j ∈ A′ \ A′′i

1

a′i < an < bn+1 ≤

bi ≤

i≤j−1

i≤ǫ(n+1)+C

ai,

i≤ǫ(n+1)+C

where the ﬁrst inequality follows from (10), the second and fourth inequalities are by the fact that A interlaces B and the third inequality follows from condition (i) of friendly sequences. This implies that j − 1 ≤ ǫ(n + 1) + C, so

A′(an − 1) ≤ |A′′i1| + j − 1 ≤ C1i1 + ǫ(n + 1) + C < C1i0 + ǫn + C + 1. (11) That is, the number of elements of A′ amongst the ﬁrst n elements of A is roughly ǫn.

We next give a similar argument, but using the extra information that there are many elements

- as ∈ A\A′ with s ≤ n in order to conclude that A′ is complete. Let N = 8(n+1)/(ǫ2c). Let i2 be the least positive integer such that 2i2 ≥ aN and let m′ = A(2i2), so m′ ≥ N. As a2N/c+1 ≥ b2N/c+1 ≥ 2bN+1 > 2aN, where the middle inequality follows from Claim 4.2, there is a perfect power of two which is at least aN


2m, we have that n ≥ 2ǫm. Thus, N = 8(n + 1)/(ǫ2c) > m, so A(2i2) ≥ N > m = A(2i0). In particular, we obtain that i2 ≥ i0. Hence, N, i2 and m′ may be made suﬃciently large by taking i0 and, hence, n suﬃciently large.

and less than a2N/c+1, so m′ = A(2i2) ≤ 2N/c. Furthermore, since an = a′j ≥ aǫ

![image 266](<2021-conlon-subset-sums-completeness-colorings_images/imageFile266.png>)

![image 267](<2021-conlon-subset-sums-completeness-colorings_images/imageFile267.png>)

We also have A′(2i2) ≥ ǫA(2i2) = ǫm′, so A′ contains at least ǫm′ elements as ≤ 2i2. Let i3 ≤ i2 be the largest positive integer such that |A′i

| ≥ 4ǫ|Ai3|. Recall that, for each positive integer i, the number of elements of A in [2i,2i+1)\[bh(i),bh(i+1)−1) is at most two. It follows that A′ ∩[2i2]\ i<i2[bh(i),bh(i+1)−1) has cardinality at most 2i2 ≤ ǫm4 ′, where the last inequality follows from condition (iii) of friendly sequences

![image 268](<2021-conlon-subset-sums-completeness-colorings_images/imageFile268.png>)

3

![image 269](<2021-conlon-subset-sums-completeness-colorings_images/imageFile269.png>)

and the fact that i2 is suﬃciently large. Hence, at least a fraction ǫ − 4ǫ − 4ǫ = 2ǫ of the elements of A up to 2i2 are greater than aǫN/4 and in A′ ∩ i<i2[bh(i),bh(i+1)−1) and, therefore, i3 satisﬁes 2i3+1 > aǫN/4.

![image 270](<2021-conlon-subset-sums-completeness-colorings_images/imageFile270.png>)

![image 271](<2021-conlon-subset-sums-completeness-colorings_images/imageFile271.png>)

![image 272](<2021-conlon-subset-sums-completeness-colorings_images/imageFile272.png>)

Since Ai3 satisﬁes the conclusion of Lemma 4.4 and |A′i

| ≥ (min(ǫ,ǫ0)/4)|Ai3|, there is A′′i

⊂ A′i

with |A′′i

3

3

3

) contains every integer in the interval [y′,2y′] where y′ = C22i3i3. Label the elements in A′ \ A′′i

| ≤ C1i3 such that Σ(A′′i

3

3

in increasing order as a′1,a′2,..., noting that we have relabeled most of the elements in A′.

3

)+[y′,2y′) contains all integers at least y′ and, as Σ(A′) is a superset of Σ(A′ \ A′′i

Again, by Lemma 2.1, if, for each j, we have a′j ≤ 2y′ −y′ +a′1 +···+a′j−1, then Σ(A′ \A′′i

3

)+[y′,2y′), A′ would be complete. So we may assume that there is some j′ for which

3

a′j′ > y′ + a′1 + ··· + a′j′−1.

Note in particular that a′j′ ≥ y′ ≥ 2i3+1 ≥ aǫN/4. Let n′ be such that an′ = a′j′, so n′ ≥ ǫN/4. (12) By condition (i) of friendly sequences, we have a′j′ = an′ < bn′+1 ≤

bi ≤

ai.

i≤ǫ(n′+1)+C

i≤ǫ(n′+1)+C

Note also that, for i ≥ ǫn′, we have

ai ≥ aǫn′ ≥ bǫn′ ≥ 2bcǫn′/2 > 2acǫn′/2−1 ≥ 2acǫ2N/8−1 ≥ 2an. (13)

Here the ﬁrst inequality follows from A being increasing, the second and fourth inequalities follow from the fact that A interlaces B, the third inequality follows from Claim 4.2, the ﬁfth inequality follows from (12) and the last inequality follows from the choice of N and the fact that A is increasing.

Since A′ has at least ǫn′ elements up to an′, we have j′ ≥ ǫn′ − |A′′i

|. It follows that

3

a′k ≥ −

a +

ak

k<j′

k≤ǫn′−|A′′i3|−1+n−A′(an)

a∈[an]∩(A\A′)

≥ −an(n − A′(an)) +

ak

k≤ǫn′−|A′′i3|−1+n−A′(an)

- 1

![image 273](<2021-conlon-subset-sums-completeness-colorings_images/imageFile273.png>)

- 2


aǫn′(n − A′(an)) +

≥ −

ak

k≤ǫn′−|A′′i3|−1+n−A′(an)

≥

ak,

k≤ǫn′−|A′′i3|−1+21(n−A′(an))

![image 274](<2021-conlon-subset-sums-completeness-colorings_images/imageFile274.png>)

where the ﬁrst inequality uses that A is an increasing sequence and k<j′ a′k + a∈[a

n]∩(A\A′) a is a sum of at least ǫn′ − |A′′i

| − 1 + n − A′(an) distinct terms of A, which is at least the sum of the ﬁrst ǫn′ − |A′′i

3

| − 1 + n − A′(an) terms in A. The second inequality follows from A being increasing, the third inequality follows from using (13) and the last inequality follows from A being increasing and the following

3

estimate showing that 12(n − A′(an)) − |A′′i

| − 1 > 0. We have

![image 275](<2021-conlon-subset-sums-completeness-colorings_images/imageFile275.png>)

3

1 2

−|A′′i3|−1+

![image 276](<2021-conlon-subset-sums-completeness-colorings_images/imageFile276.png>)

1 2

n − A′(an) ≥ −C1i3−1+

![image 277](<2021-conlon-subset-sums-completeness-colorings_images/imageFile277.png>)

(n − (C1i0 + ǫn + C + 2)) ≥ −2C1i2+

1 2

C + 2 2

(1−ǫ)n−

![image 278](<2021-conlon-subset-sums-completeness-colorings_images/imageFile278.png>)

![image 279](<2021-conlon-subset-sums-completeness-colorings_images/imageFile279.png>)

> C+1,

where the ﬁrst inequality is by (11), the second inequality uses i0,i3 ≤ i2 and i2 is suﬃciently large, while the last inequality uses n ≥ ǫ2cN/10, N ≥ cm′/2, condition (i) of friendly sequences, the fact that A interlaces B, m′ = A(2i2), i2 is suﬃciently large and m′ ≥ 2

√

![image 280](<2021-conlon-subset-sums-completeness-colorings_images/imageFile280.png>)

(2 log2(1/ǫ)+o(1))i2 from Appendix A.1, from all of which it follows that i2 ≪ n. However, this implies that

bn′+1 > an′ = a′j′ >

a′k >

ak ≥

k<j′

k≤ǫn′+C+1

contradicting condition (i) of friendly sequences.

bk ≥

bk,

k≤ǫn′+C+1

k≤ǫ(n′+1)+C

![image 281](<2021-conlon-subset-sums-completeness-colorings_images/imageFile281.png>)

![image 282](<2021-conlon-subset-sums-completeness-colorings_images/imageFile282.png>)

![image 283](<2021-conlon-subset-sums-completeness-colorings_images/imageFile283.png>)

![image 284](<2021-conlon-subset-sums-completeness-colorings_images/imageFile284.png>)

Theorem 1.4 is obtained similarly, by replacing Lemma 4.4 in the above proof by an appropriate analogue of Lemma 2.9. As indicated in the introduction, we omit the details.

# 5 Monochromatic subset sums

- 5.1 Proof of the lower bound in Theorem 1.6 Throughout this section, we use the convention that products and sums indexed by p run over primes. Recall that pi is the ith prime, W(ρ) = ρi=1 pi and τ(ρ,m) = φ(W(ρ)m)/(W(ρ)m) = p|W(ρ)m(1−1/p).


We recall from the introduction that, for positive integers n and m with m ∈ [n, n2 ], we deﬁne ρ(n,m) to be the smallest positive integer ρ such that ρ/τ(ρ,m) ≥ n2/φ(m). Let ψ(n,m) = m

1/3(m/φ(m))

(logn)1/3(log logn)2/3 and R(n,m) = min(ψ(n,m),ρ(n,m)). By Claim B.3 in Appendix B.2, we note that R(n,m) = Θ(ψ(n,m)) when m = O n

![image 285](<2021-conlon-subset-sums-completeness-colorings_images/imageFile285.png>)

3/2(log log n)1/2

(logn)1/2 and R(m,n) = Θ(ρ(n,m)) otherwise.

![image 286](<2021-conlon-subset-sums-completeness-colorings_images/imageFile286.png>)

We aim to prove that f(n,m), the minimum r such that there exists an r-coloring of [n − 1] where m cannot be written as a sum of distinct monochromatic elements, is bounded below by R(n,m) up to a constant factor, giving the lower bound in Theorem 1.6. The main result of this subsection is the following lemma, from which the required lower bound easily follows.

- Lemma 5.1. There exist positive constants c and C such that the following holds. Let n be suﬃciently large and m ∈ [n, n2 ] be such that r = cR(n,m) is at least C. Let y < n/2 be such that


m ∈

y2(m/φ(m))τ(r,m) 25r

,

![image 287](<2021-conlon-subset-sums-completeness-colorings_images/imageFile287.png>)

y2(m/φ(m))τ(r,m) 15r

![image 288](<2021-conlon-subset-sums-completeness-colorings_images/imageFile288.png>)

and let Y be the set of integers in [y,2y) of the form qu, where u|m, u ≤ y1/16 and q is coprime to W(r)m. Then, in any r-coloring of Y , there exists a monochromatic subset sum which equals m.

By Claim B.4 in Appendix B.2, for any m ∈ [n, n2 ], there exists a choice of y ∈ [max(r2,n3/5),n/2) satisfying the required condition. We may therefore apply the lemma to conclude that if R(n,m) ≥ C/c, then f(n,m) ≥ cR(n,m). That is, the lower bound in Theorem 1.6 holds in this case. On the other hand, if R(n,m) < C/c, we have the trivial bound f(n,m) ≥ 1 ≥ C−1cR(n,m), so the lower bound in

Theorem 1.6 also holds in this case. For the same reason, we can and will assume throughout that r is suﬃciently large.

We will build towards the proof of Lemma 5.1 through a series of reductions and intermediate results. For convenience, we will often use objects and notation in the lemma statements without repeating their deﬁnitions from earlier. We begin with the following number-theoretic estimate, whose proof may be found in Appendix B.1.

- Lemma 5.2. Let r, n and m be positive integers such that m ∈ [n, n2 ], r ≤ n and r is suﬃciently large. For any interval I = [x,2x) with x ≥ n1/4, there are at most 8(m/φ(m))τ(r,m)x integers in I of

- the form qu, where u|m, u ≤ x1/16 and q is coprime to W(r)m. If also x ≥ r2, then there are at least


1 8(m/φ(m))τ(r,m)x integers in I of this form.

![image 289](<2021-conlon-subset-sums-completeness-colorings_images/imageFile289.png>)

By Lemma 5.2, the set Y deﬁned in Lemma 5.1 satisﬁes

|Y | ≥

1 8

![image 290](<2021-conlon-subset-sums-completeness-colorings_images/imageFile290.png>)

(m/φ(m))τ(r,m)y.

By the pigeonhole principle, in any r-coloring of Y , there is one color class whose size is at least

- 1 8(m/φ(m))τ(r,m)yr . Let Q0 be the elements of Y in this color class. We will prove that m ∈ Σ(Q0).


![image 291](<2021-conlon-subset-sums-completeness-colorings_images/imageFile291.png>)

![image 292](<2021-conlon-subset-sums-completeness-colorings_images/imageFile292.png>)

Call a set X of integers k-diverse if, for each v ≥ 2, there are at least k elements of X which are not divisible by v. If Q0 is not y1/4-diverse, there exists v0 ≥ 2 such that at most y1/4 elements of Q0 are not divisible by v0. We replace Q0 by Q1 = {a/v0 : a ∈ Q0,v0|a} ⊆ [y/v0,2y/v0). We then iterate this process. For i ≥ 1, if Qi is not y1/4-diverse, we can remove at most y1/4 elements of Qi so that the remaining elements are divisible by some vi ≥ 2. We then let Qi+1 = {x/vi : x ∈ Qi,vi|x}. We stop the process once we reach a set Qs which is y1/4-diverse. Note that there can be at most log2 n iterations, so there must be at least 81(m/φ(m))τ(r,m)yr − y1/4 log2 n elements in Qs.

![image 293](<2021-conlon-subset-sums-completeness-colorings_images/imageFile293.png>)

![image 294](<2021-conlon-subset-sums-completeness-colorings_images/imageFile294.png>)

By the process deﬁning Qs, there exists v such that Qs = {x/v : x ∈ Q0,v|x}. Let Q = Qs. Then Q is a subset of [y/v,2y/v) of size at least 81(m/φ(m))τ(r,m)yr − y1/4 log2 n which is y1/4-diverse. Let z = 81(m/φ(m))τ(r,m)yr − y1/4 log2 n. Note that

![image 295](<2021-conlon-subset-sums-completeness-colorings_images/imageFile295.png>)

![image 296](<2021-conlon-subset-sums-completeness-colorings_images/imageFile296.png>)

![image 297](<2021-conlon-subset-sums-completeness-colorings_images/imageFile297.png>)

![image 298](<2021-conlon-subset-sums-completeness-colorings_images/imageFile298.png>)

1 8

![image 299](<2021-conlon-subset-sums-completeness-colorings_images/imageFile299.png>)

(m/φ(m))τ(r,m)

y r ≥ z ≥

![image 300](<2021-conlon-subset-sums-completeness-colorings_images/imageFile300.png>)

1 10

![image 301](<2021-conlon-subset-sums-completeness-colorings_images/imageFile301.png>)

(m/φ(m))τ(r,m)

y r ≥

![image 302](<2021-conlon-subset-sums-completeness-colorings_images/imageFile302.png>)

1 10

![image 303](<2021-conlon-subset-sums-completeness-colorings_images/imageFile303.png>)

τ(r,m)√y > y1/3, (14)

![image 304](<2021-conlon-subset-sums-completeness-colorings_images/imageFile304.png>)

where we used that y ≥ max(r2,n3/5), which is inequality (35) of Claim B.4 in Appendix B.2, and τ(r,m) ≥ 1/(8log nlog log n) by inequality (33) in Appendix B.2. In particular, for r suﬃciently large,

|Q| = z ≥

1 10

![image 305](<2021-conlon-subset-sums-completeness-colorings_images/imageFile305.png>)

(m/φ(m))τ(r,m)

y r

![image 306](<2021-conlon-subset-sums-completeness-colorings_images/imageFile306.png>)

> 64(m/φ(m))τ(r,m)

y r log r

![image 307](<2021-conlon-subset-sums-completeness-colorings_images/imageFile307.png>)

.

The next lemma shows that v|m.

- Lemma 5.3. If there exist at least 64(m/φ(m))τ(r,m)r logy r elements in Y which are divisible by v, then v|m and v ≤ y1/16. Furthermore, all elements of Y which are divisible by v have the form qvu, where (vu)|m, vu ≤ y1/16 and gcd(q,W(r)m) = 1.


![image 308](<2021-conlon-subset-sums-completeness-colorings_images/imageFile308.png>)

Proof. Note that if gcd(q,W(r)m) = 1 and q = 1, then any prime factor of q is at least pr > r log r/8 for suﬃciently large r. Recall that elements of Y have the form qu, where u|m, u ≤ y1/16 and gcd(q,W(r)m) =

- 1. Assume that there exists v such that either v ∤ m or v > y1/16 and at least 64(m/φ(m))τ(r,m)r logy r elements in Y are divisible by v. We claim that v must have a prime factor p which is coprime to W(r)m. Indeed, if this were not the case, then v only has prime factors which are divisors of W(r)m, so gcd(v,q) = 1 for any q coprime to W(r)m. Thus, if an element of the form qu with u|m, u ≤ y1/16 and gcd(q,W(r)m) = 1 is divisible by v, then v|u, so v|m and v ≤ y1/16, contradicting our assumption. Thus, v has a prime factor p which is coprime to W(r)m. In particular, p ≥ pr > r(log r)/8.


![image 309](<2021-conlon-subset-sums-completeness-colorings_images/imageFile309.png>)

We have that at least 64(m/φ(m))τ(r,m)r logy r elements of Y are divisible by p. For each element qu of Y which is divisible by p, since p is coprime to W(r)m, we must have p|q, so q = q′p for q′ coprime to W(r)m. Hence, elements of Y which are divisible by p have the form pq′u where u|m, u ≤ y1/16 and gcd(q′,W(r)m) = 1. If y/p ≥ n1/4, Lemma 5.2 implies that the number of such elements is at most 8(m/φ(m))τ(r,m)yp < 64(m/φ(m))τ(r,m)r logy r. If y/p < n1/4, then the number of such elements is at most y/p < n1/4 < 64(m/φ(m))τ(r,m)r logy r, where the second inequality is veriﬁed as inequality (36) of Claim B.4 in Appendix B.2. In either case, we have a contradiction, so we must have that v|m and v ≤ y1/16.

![image 310](<2021-conlon-subset-sums-completeness-colorings_images/imageFile310.png>)

![image 311](<2021-conlon-subset-sums-completeness-colorings_images/imageFile311.png>)

![image 312](<2021-conlon-subset-sums-completeness-colorings_images/imageFile312.png>)

![image 313](<2021-conlon-subset-sums-completeness-colorings_images/imageFile313.png>)

Since v|m, we have gcd(v,W(r)m) = v, so each element of the form qu where u|m, u ≤ y1/16 and gcd(q,W(r)m) = 1 which is divisible by v must have v|u. Hence, qu = qvu′ where (vu′)|m, vu′ ≤ y1/16 and gcd(q,W(r)m) = 1, establishing the second claim in the lemma.

![image 314](<2021-conlon-subset-sums-completeness-colorings_images/imageFile314.png>)

![image 315](<2021-conlon-subset-sums-completeness-colorings_images/imageFile315.png>)

![image 316](<2021-conlon-subset-sums-completeness-colorings_images/imageFile316.png>)

![image 317](<2021-conlon-subset-sums-completeness-colorings_images/imageFile317.png>)

Since |Q| > 64(m/φ(m))τ(r,m)r logy r and {vx : x ∈ Q} is a subset of Y , Lemma 5.3 implies that each element of Q can be written in the form qu, where (vu)|m, vu ≤ y1/16 and gcd(q,W(r)m) = 1. Let

![image 318](<2021-conlon-subset-sums-completeness-colorings_images/imageFile318.png>)

Yv = {t ∈ [y/v,2y/v) : t = qu,u|(m/v),u ≤ y1/16/v,gcd(q,W(r)m) = 1}.

We have that vt ∈ Y for all t ∈ Yv and Q ⊆ Yv.

Let V be a random subset of Q of size z/8. The next lemma implies that V is y1/4/16-diverse with probability at least 1/2. From now, we ﬁx V to be a subset of Q of size z/8 which is y1/4/16-diverse.

- Lemma 5.4. Let k and h be positive integers with h = 1 and N = exp(k/16h). Let A be a set of t integers in [N] which is k-diverse. Let B be a uniformly random subset of A of size t/h. Then B is k/(2h)-diverse with probability at least 1 − 1/N.

Proof. For each d ∈ [N] with d > 1, let Xd be the set of elements in A which are not divisible by d. By our assumption, |Xd| ≥ k for each d. The number of elements in B∩Xd follows a hypergeometric distribution. As the hypergeometric distribution is at least as concentrated as the corresponding binomial distribution (for a proof, see Section 6 of [29]), we can apply the Chernoﬀ bound to obtain that the probability that |B ∩ Xd| < |Xd|/(2h) is at most exp(−|Xd|/8h) ≤ exp(−k/8h) = N−2. By taking a union bound over all d ∈ [N] with d > 1, we conclude that the probability B is not k/(2h)-diverse is at most N·N−2 = N−1.

![image 319](<2021-conlon-subset-sums-completeness-colorings_images/imageFile319.png>)

![image 320](<2021-conlon-subset-sums-completeness-colorings_images/imageFile320.png>)

![image 321](<2021-conlon-subset-sums-completeness-colorings_images/imageFile321.png>)

![image 322](<2021-conlon-subset-sums-completeness-colorings_images/imageFile322.png>)

The following lemma is the key to proving Lemma 5.1.

- Lemma 5.5. Let ℓ = ⌈32/ξ⌉, where ξ is the constant in Lemma 2.4. Let A be a subset of Yv of size z/(8ℓ) which is y1/4/(32ℓ)-diverse. Then |Σ(A)| ≥ yz/(ℓ2v) and Σ(A) is not a subset of an arithmetic progression with common diﬀerence greater than 1.


Before moving on to the proof of Lemma 5.5, we show how Lemma 5.1 follows from it.

Proof of Lemma 5.1 assuming Lemma 5.5. Recall that we have ﬁxed a subset V of Q of size z/8 which is

- y1/4/16-diverse. We will prove that Σ(V ) contains an interval J = [a,b] of length at least 2y/v. To see why this suﬃces, ﬁrst note that

vb ≤ v · maxΣ(V ) < 2y ·

z 8 ≤ 2y ·

![image 323](<2021-conlon-subset-sums-completeness-colorings_images/imageFile323.png>)

(m/φ(m))τ(r,m)y 8 · 8r

![image 324](<2021-conlon-subset-sums-completeness-colorings_images/imageFile324.png>)

< m,

where the third inequality follows from (14) and the last inequality follows since y2 ≤ (m/φ(25mrm))τ(r,m) by the choice of y. If now we can ﬁnd the required interval J, Lemma 5.1 follows since each element of Q

![image 325](<2021-conlon-subset-sums-completeness-colorings_images/imageFile325.png>)

is at most 2y/v and, hence, by Lemma 2.1, Σ(Q) = Σ(V ∪ (Q \ V )) contains an interval whose smallest element is a < m/v by the inequality above and whose largest element is

b +

i∈Q\V

i >

y v · z(1 − 1/8) ≥

![image 326](<2021-conlon-subset-sums-completeness-colorings_images/imageFile326.png>)

y v ·

![image 327](<2021-conlon-subset-sums-completeness-colorings_images/imageFile327.png>)

7(m/φ(m))τ(r,m)y 8 · 10r

![image 328](<2021-conlon-subset-sums-completeness-colorings_images/imageFile328.png>)

>

m v

![image 329](<2021-conlon-subset-sums-completeness-colorings_images/imageFile329.png>)

,

where the last inequality follows since y2 ≥ (m/φ(15mrm))τ(r,m) by the choice of y. Hence, Σ(Q0) contains the progression {va,v(a + 1),... ,v(m/v)}, which contains m.

![image 330](<2021-conlon-subset-sums-completeness-colorings_images/imageFile330.png>)

We partition V randomly into ℓ sets V1,V2,... ,Vℓ of size z/(8ℓ). By Lemma 5.4 and the union bound, the probability that Vi is y1/4/(32ℓ)-diverse for all i ∈ [ℓ] is at least 1/2. Hence, we can ﬁx a partition of V into ℓ sets V1,V2,... ,Vℓ of size z/(8ℓ), where Vi is y1/4/(32ℓ)-diverse for each i ∈ [ℓ].

For each i ∈ [ℓ], Σ(Vi) is a subset of the interval [0,z/(8ℓ) · 2y/v] = [0,yz/(4ℓv)]. By Lemma 5.5, |Σ(Vi)| ≥ yz/(ℓ2v) and Σ(Vi) is not a subset of an arithmetic progression with common diﬀerence greater than 1. Therefore, by Lemma 2.2, Σ(V1)+···+Σ(Vℓ) contains an interval of length at least yz/(2ℓv) > 2y/v for n suﬃciently large, as required.

![image 331](<2021-conlon-subset-sums-completeness-colorings_images/imageFile331.png>)

![image 332](<2021-conlon-subset-sums-completeness-colorings_images/imageFile332.png>)

![image 333](<2021-conlon-subset-sums-completeness-colorings_images/imageFile333.png>)

![image 334](<2021-conlon-subset-sums-completeness-colorings_images/imageFile334.png>)

We have therefore reduced the task of proving the lower bound in Theorem 1.6 to Lemma 5.5. The strategy for proving Lemma 5.5 is now as follows. We partition A into two subsets A1 and A2 of size

- z/(16ℓ), observing that we can choose A1 and A2 to be y1/4/(128ℓ)-diverse by Lemma 5.4. We then show that Σ(A1) contains elements in many diﬀerent congruence classes modulo t for all t in A2, allowing us to apply Lemma 2.5 repeatedly (as in the proofs of our results on completeness) to conclude that each


element of A2 introduces many new elements to the set of subset sums. The next lemma is the main step in the proof of Lemma 5.5. Recall that

Σt(A) =

x mod t : S ⊆ A

x∈S

and ξ is the absolute constant deﬁned in Lemma 2.4.

- Lemma 5.6. Let t ∈ [y/v,2y/v). Let A be a subset of Yv of size z/(16ℓ) which is y1/4/(128ℓ)-diverse. Then |Σt(A)| ≥ min(ξ,32/ℓ)t.


To show that the set of mod t subset sums is large, we prove the following structural lemma, stating that the set of elements whose inclusion does not expand the set of mod t subset sums must either be small or additively structured. We will then use this additive structure to show that the corresponding set in Z must contain a small number of integers of the form qu, which we will see is impossible.

- Lemma 5.7. Let t be an integer. Let A ⊆ Zt be such that 8d < |A| < ξt. Let Gd ⊆ Zt be the set of x such


that |(A + x) ∪ A| ≤ |A| + d. Then either Gd is contained in a proper subgroup of Zt, |Gd| ≤ (|A|20/2|dA)|1.02 or there is a subgroup H of Zt such that Gd is contained in a set of size at most 128d which is an arithmetic progression of H-cosets.

![image 335](<2021-conlon-subset-sums-completeness-colorings_images/imageFile335.png>)

Proof. By Lemma 2.7, kGd ⊆ Gkd, where kGd = {x1 + x2 + ··· + xk : x1,x2,... ,xk ∈ Gd}. Let

- i = ⌊log2(|A|/2d)⌋ and let k = 2i, noting that kd ≤ |A|/2. Therefore, applying Lemma 2.6 to Gkd, we get


|A|2

|A| − kd ≤ 2|A|. (15) Assume that Gd is not contained in a proper subgroup of Zt. Let j be such that 0 ≤ j < i. Since

|kGd| ≤ |Gkd| ≤

![image 336](<2021-conlon-subset-sums-completeness-colorings_images/imageFile336.png>)

- 0 ∈ Gd by deﬁnition, we have Gd ⊂ 2jGd, so 0 ∈ 2jGd and 2jGd is not contained in a proper subgroup of Zt. Thus, 2jGd is not contained in a coset of a proper subgroup of Zt. By Lemma 2.3, |2iGd| ≥ min{t,2i−j−1|2jGd|} = 2i−j−1|2jGd|, where we used that |2iGd| ≤ 2|A| < 2ξt < t from (15). Thus,


|2jGd| ≤ 21−i+j|2iGd| < 2ξt. (16)

Assume now that |2j+1Gd| = |2jGd + 2jGd| ≤ 2.04|2jGd| for some 2 ≤ j < i. By Lemma 2.4, there exists a proper subgroup H of Zt such that one of the following holds:

- (i) 2jGd is contained in a set of size at most ℓ−ℓ1 · 1.04|2jGd| which is an arithmetic progression of H-cosets of length ℓ ≥ 2,

![image 337](<2021-conlon-subset-sums-completeness-colorings_images/imageFile337.png>)

- (ii) 2jGd meets exactly three H-cosets which are terms of an arithmetic progression of H-cosets of length ℓ and (min(ℓ,4) − 1)|H| ≤ 1.04|2jGd| or
- (iii) 2jGd is contained in one H-coset.


We have already seen that the third case cannot happen, that is, that 2jGd is not contained in a coset of a proper subgroup of Zt.

Suppose that we are in the second case. Then 2jGd is contained in a union of three H-cosets, so 4Gd is contained in a union of three H-cosets. Since 0 ∈ Gd and Gd is not contained in an H-coset, the image of Gd in Zt/H is a subset S of Zt/H of size at least 2 such that 0 ∈ S and 4S has size at most 3. This can only happen if S is contained in a subgroup of Zt/H of size at most 3. In this case, Gd is contained in a subgroup of Zt of size at most 3|H|. Since |H| ≤ (min(ℓ,4) − 1)|H| ≤ 1.04|2jGd|, we have 3|H| ≤ 3.12|2jGd| < 6.24ξt < t, so Gd is contained in a proper subgroup of Zt, a contradiction. Thus, the second case cannot happen.

We now consider the ﬁrst case, where 2jGd is contained in a set of size at most ℓ−ℓ1 · 1.04|2jGd| ≤

![image 338](<2021-conlon-subset-sums-completeness-colorings_images/imageFile338.png>)

- 2.08|2jGd| which is an arithmetic progression of H-cosets of length ℓ. As 0 ∈ Gd, this progression of H-cosets contains 0. Let m be such that H = {x ∈ Zt : m|x}. Then the H-cosets can be identiﬁed with elements of Zm. The common diﬀerence of the progression of H-cosets must be coprime to m, as otherwise


- 2jGd would be contained in a proper subgroup of Zt. Thus, by rescaling if necessary, we may assume that the common diﬀerence of the progression of H-cosets is 1. Let Pj be the interval in Zm which corresponds to the H-cosets in the progression containing 2jGd. Note that 0 ∈ Gd, so that 2h−1Gd ⊆ 2hGd for all h.


Hence, for each h ≤ j, we can choose intervals Ph around 0 in Zm such that 2h(Gd/H) ⊆ Ph, Ph ⊆ Pj and

- 2j−hPh ⊆ Pj. The length ℓ of Pj is at most m/2, since otherwise |2jGd| ≥ 2t/.082 , contradicting (16). We can thus deduce that, for all h ≤ j, Ph is an interval of length at most 1 + 2h−j(|Pj| − 1) around 0 in Zm, since, for two intervals I, I′ around 0 of length |I| ≤ |I′| ≤ m/2 with 2I ⊆ I′, we have |I| ≤ (|I′| + 1)/2. Hence, Gd/H is a subset of an interval of length at most 1 + (|Pj| − 1)/2j. Since Gd is not contained in a proper subgroup of Zt, (|Pj| − 1)/2j ≥ 1. Thus, we have 1 + (|Pj| − 1)/2j ≤ |Pj|/2j−1. Therefore, Gd is contained in a union of H-cosets of size at most


![image 339](<2021-conlon-subset-sums-completeness-colorings_images/imageFile339.png>)

ℓ ℓ − 1 · 1.04|2jGd| · 21−j ≤

ℓ

|H||Pj|/2j−1 ≤

ℓ − 1 · 1.04 · 23−i|A| ≤ 128d, where, in the second inequality, we used (15) and (16) and, in the ﬁnal inequality, we used that i = ⌊log2(|A|/2d)⌋ and ℓ ≥ 2.

![image 340](<2021-conlon-subset-sums-completeness-colorings_images/imageFile340.png>)

![image 341](<2021-conlon-subset-sums-completeness-colorings_images/imageFile341.png>)

If there does not exist j ∈ [2,i) such that |2j+1Gd| ≤ 2.04|2jGd|, then

|2iGd| ≥ 2.04i−2|Gd| ≥ (|A|/2d)1.02|Gd|/10.

Combining this with (15), we deduce that |Gd| ≤ (|A|20/2|dA)|1.02 .

![image 342](<2021-conlon-subset-sums-completeness-colorings_images/imageFile342.png>)

![image 343](<2021-conlon-subset-sums-completeness-colorings_images/imageFile343.png>)

![image 344](<2021-conlon-subset-sums-completeness-colorings_images/imageFile344.png>)

![image 345](<2021-conlon-subset-sums-completeness-colorings_images/imageFile345.png>)

![image 346](<2021-conlon-subset-sums-completeness-colorings_images/imageFile346.png>)

Besides Lemma 5.7, we need several other ingredients for the proof of Lemma 5.6. We begin with the following result, which will also be useful to us in subsequent sections. For this section, the key corollary is that if A is k-diverse for k ≥ d − 1, then Σd(A) = Zd.

- Lemma 5.8. Let d be a positive integer. Let A be a set of integers such that, for each d′|d, at least d′ − 1 elements of A are not divisible by d′. Then Σd(A) = Zd. Furthermore, if A contains at least d−1 elements which are not divisible by d, then Σd(A) contains a non-zero subgroup of Zd. Proof. We will use the following simple claim.


Claim. If S is a subset of Zt and X ⊆ Zt is such that |(S + x) ∪ S| = |S| for all x ∈ X, then S is a union of cosets of the subgroup of Zt spanned by X.

Proof. If |(S + x) ∪ S| = |S|, then S + x = S. Thus, by induction, we have that S + x1 + ··· + xk = S for all k ∈ N and x1,... ,xk ∈ X. In particular, we have S + X = S, where X is the subgroup of Zt spanned by X. Since S + X is a union of cosets of X , we obtain the desired conclusion.

![image 347](<2021-conlon-subset-sums-completeness-colorings_images/imageFile347.png>)

![image 348](<2021-conlon-subset-sums-completeness-colorings_images/imageFile348.png>)

![image 349](<2021-conlon-subset-sums-completeness-colorings_images/imageFile349.png>)

![image 350](<2021-conlon-subset-sums-completeness-colorings_images/imageFile350.png>)

Note that Σt(S ∪ {x}) = Σt(S) ∪ (Σt(S) + x). From the claim, if S is a multiset in Zt and x ∈ Zt is coprime to t, then we have |Σt(S ∪ {x})| ≥ min(|Σt(S)| + 1,t), as either |Σt(S ∪ {x})| ≥ |Σt(S)| + 1 or Σt(S) is a union of cosets of xZt = Zt, so Σt(S) = Zt. Thus, if B = {b1,... ,bt−1} is a multiset of size t − 1 consisting of elements in Zt coprime to t, then Σt(B) = Zt. Indeed, this follows easily from the fact that Σt(∅) = {0} and, for each i ≥ 1, |Σt({b1,... ,bi})| ≥ min(|Σt({b1,... ,bi−1})| + 1,t).

Suppose now that A is a set of integers such that, for each d′|d, at least d′ − 1 elements of A are not

- divisible by d′. We will prove that Σd′(A) = Zd′ for all d′|d by induction on the number of prime factors (counted with repeats) of d′. When d′ is a prime, the conclusion follows from the observation above. Assume now that the conclusion holds whenever d′ has at most j prime factors, for some j ≥ 1.


Let d′ be a divisor of d with j + 1 prime factors. Let A0 be the multiset of elements in A not divisible by d′, considered modulo d′. By our assumption, A0 has size at least d′ − 1. Observe that

Σd′(A) = Σd′(A0). Assume that |Σd′(A0)| < d′. Let Σd′(0) = {0}. We consider the following iterative process. At step i ≥ 1, we choose ai ∈ Ai−1 so that |(Σd′(i − 1) + ai) \ Σd′(i − 1)| is maximized and let Σd′(i) = Σd′(i − 1) ∪ (Σd′(i − 1) + ai) and Ai = Ai−1 \ {ai}. Note that we consider the Ai as a multiset of elements of Zd′ and the Σd′(i) as subsets of Zd′.

Let i ≤ |A0| be the ﬁrst step where |Σd′(i)| ≤ |Σd′(i − 1)|. Note that i must exist since, otherwise, |Σd′(|A0|)| ≥ |Σd′(0)|+|A0| = 1+|A0| ≥ d′, contradicting our assumption that |Σd′(|A0|)| = |Σd′(A0)| < d′. Since i is the ﬁrst step with |Σd′(i)| ≤ |Σd′(i − 1)|, we must have that |Σd′(j)| ≥ |Σd′(j − 1)| + 1 for all

- j < i. Thus, |Σd′(i)| ≥ 1 + i − 1 = i. In step i, we have |(Σd′(i − 1) + a) ∪ Σd′(i − 1)| = |Σd′(i − 1)| for all a ∈ Ai−1, so, by the claim, Σd′(i − 1) is a union of cosets of the subgroup of Zd′ spanned by Ai−1. Let d′′ be the largest divisor of d′ which divides all elements in Ai−1. Then the subgroup of Zd′ spanned by Ai−1 is d′′Zd′ and we have that Σd′(i − 1) is a union of d′′Zd′-cosets. Note that d′′ = d′, since the elements of A0 are not divisible by d′ and Ai−1 contains at least one element in A0. Thus, d′′ < d′ and, hence, d′′ has at most j prime factors. By the induction hypothesis, Σd′′(A0) = Zd′′. Note that Σd′′(A0) = Σd′′({a1,... ,ai−1}), since all remaining elements of A0 are divisible by d′′. Thus, Σd′(i − 1) contains an element in each d′′Zd′-coset of Zd′. Since Σd′(i − 1) is a union of d′′Zd′-cosets and contains an element in each d′′Zd′-coset of Zd′, Σd′(i−1) contains all elements of Zd′. Thus, Σd′(A) = Σd′(i−1) = Zd′, completing the induction.


For the second statement, observe, by the claim, that if |Σd(S ∪ {x})| = |Σd(S)|, then Σd(S) is a union of cosets of xZd and, as 0 ∈ Σd(S), we have that Σd(S) contains the subgroup xZd of Zd. Thus, if A contains at least d − 1 integers a1,... ,ad−1 not divisible by d and Σd(A) does not contain a non-zero subgroup of Zd, then we must have |Σd({a1,... ,ai})| ≥ |Σd({a1,... ,ai−1})| + 1 for all i ≥ 1. But then |Σd(A)| ≥ 1 + (d − 1) = d, which means that Σd(A) equals Zd.

![image 351](<2021-conlon-subset-sums-completeness-colorings_images/imageFile351.png>)

![image 352](<2021-conlon-subset-sums-completeness-colorings_images/imageFile352.png>)

![image 353](<2021-conlon-subset-sums-completeness-colorings_images/imageFile353.png>)

![image 354](<2021-conlon-subset-sums-completeness-colorings_images/imageFile354.png>)

We remark that the condition in the above lemma is tight, since if d is prime and A consists of d − 2 elements congruent to 1 modulo d, then Σd(A) does not contain any non-zero subgroup of Zd.

The next lemma gives an upper bound on the number of integers coprime to W(r)/gcd(W(r),m) in an arithmetic progression. Note that all integers of the form qu where u|m and gcd(q,W(r)m) = 1 are coprime to W(r)/gcd(W(r),m). The proof of this lemma uses the Selberg sieve and may be found in

- Appendix B.1.


- Lemma 5.9. Let r and n be suﬃciently large positive integers and m ∈ [n, n2 ]. Let X be an arithmetic progression of size |X| ≥ r1/16 with common diﬀerence b ≤ n. Then the number of elements of X which are coprime to W(r)/gcd(W(r),m) is at most


256|X|log log n log r

.

![image 355](<2021-conlon-subset-sums-completeness-colorings_images/imageFile355.png>)

Furthermore, when b = 1, the number of elements of X which are coprime to W(r)/gcd(W(r),m) is at most

256|X|

(1 − 1/p).

p|W(r),p∤m

Given a cyclic group Zt and an interval of integers [x,x+t), we have a natural identiﬁcation ψt : Zt → [x,x+t), where ψt(u) is the unique integer in [x,x+t) which is congruent to u modulo t. The next lemma

shows that under this identiﬁcation, for a subgroup H of Zt, a progression of H-cosets is identiﬁed with a large subset of a union of long arithmetic progressions of integers. A variant of this lemma goes back at least to the proof of Roth’s Theorem [33].

- Lemma 5.10. Let H be a subgroup of Zt and let R be an arithmetic progression of H-cosets. Consider the image ψt(R) of R under the identiﬁcation ψt : Zt → [x,x + t). Then ψt(R) is contained in a set of size at most 3|R| which is a union of arithmetic progressions of integers, each of length at least |R|1/3.

Proof. First observe that the image under ψt of each H-coset is an arithmetic progression. Thus, if |H| ≥ |R|1/3, then ψt(R) is a union of arithmetic progressions, each of length at least |R|1/3.

Assume now that |H| < |R|1/3. Let H = dZt for some divisor d of t. Let ℓ = |R|/|H| ≥ |R|2/3. By deﬁnition, we can write R = i∈[ℓ](x+iy+H) for some x,y ∈ Zt and y ∈/ H. For each H-coset x+iy+H, we can choose a representative zi for the coset in [x,x + d). Let P = (z1,z2,... ,zℓ). We have that P (mod d) forms a progression of common diﬀerence u in Zd. We show that P is contained in a set of size at most 3ℓ which is a union of progressions of integers, each of length at least √

![image 356](<2021-conlon-subset-sums-completeness-colorings_images/imageFile356.png>)

ℓ = |R|/|H| ≥ |R|1/3. From this claim, the conclusion of the lemma easily follows.

![image 357](<2021-conlon-subset-sums-completeness-colorings_images/imageFile357.png>)

We claim that there exists s ∈ [1,⌊

√

![image 358](<2021-conlon-subset-sums-completeness-colorings_images/imageFile358.png>)

ℓ⌋] such that su is congruent to an integer in [−d/⌈

√

![image 359](<2021-conlon-subset-sums-completeness-colorings_images/imageFile359.png>)

ℓ⌉,d/⌈

√

![image 360](<2021-conlon-subset-sums-completeness-colorings_images/imageFile360.png>)

ℓ⌉] modulo d. Partition Zd into a union of intervals [kd/⌈

√

![image 361](<2021-conlon-subset-sums-completeness-colorings_images/imageFile361.png>)

ℓ⌉,(k + 1)d/⌈

√

![image 362](<2021-conlon-subset-sums-completeness-colorings_images/imageFile362.png>)

ℓ⌉) for k = 0,1,... ,⌈

√

![image 363](<2021-conlon-subset-sums-completeness-colorings_images/imageFile363.png>)

ℓ⌉ −

- 1. Suppose that there does not exist s ∈ [1,⌊

√

![image 364](<2021-conlon-subset-sums-completeness-colorings_images/imageFile364.png>)

ℓ⌋] such that su (mod d) ∈ [−d/⌈

√

![image 365](<2021-conlon-subset-sums-completeness-colorings_images/imageFile365.png>)

ℓ⌉,d/⌈

√

![image 366](<2021-conlon-subset-sums-completeness-colorings_images/imageFile366.png>)

ℓ⌉]. Then u,2u,... ,⌊

√

![image 367](<2021-conlon-subset-sums-completeness-colorings_images/imageFile367.png>)

ℓ⌋u (mod d) must be contained in the intervals [kd/⌈

√

![image 368](<2021-conlon-subset-sums-completeness-colorings_images/imageFile368.png>)

ℓ⌉,(k+1)d/⌈

√

![image 369](<2021-conlon-subset-sums-completeness-colorings_images/imageFile369.png>)

ℓ⌉) for k = 1,... ,⌈

√

![image 370](<2021-conlon-subset-sums-completeness-colorings_images/imageFile370.png>)

ℓ⌉−

- 2. Since ⌊


√

![image 371](<2021-conlon-subset-sums-completeness-colorings_images/imageFile371.png>)

ℓ⌋ ≥ ⌈

√

![image 372](<2021-conlon-subset-sums-completeness-colorings_images/imageFile372.png>)

ℓ⌉ − 1, the pigeonhole principle implies that there are 1 ≤ s′ < s′′ ≤ ⌊

√

![image 373](<2021-conlon-subset-sums-completeness-colorings_images/imageFile373.png>)

ℓ⌋ such that s′u (mod d) and s′′u (mod d) are in the same interval [kd/⌈

√

![image 374](<2021-conlon-subset-sums-completeness-colorings_images/imageFile374.png>)

ℓ⌉,(k + 1)d/⌈

√

![image 375](<2021-conlon-subset-sums-completeness-colorings_images/imageFile375.png>)

ℓ⌉). Then s′′ − s′ ∈ [1,⌊

√

![image 376](<2021-conlon-subset-sums-completeness-colorings_images/imageFile376.png>)

ℓ⌋] and (s′′ −s′)u is congruent to an integer v in [−d/⌈

√

![image 377](<2021-conlon-subset-sums-completeness-colorings_images/imageFile377.png>)

ℓ⌉,d/⌈

√

![image 378](<2021-conlon-subset-sums-completeness-colorings_images/imageFile378.png>)

ℓ⌉] modulo d, contradicting our assumption. Suppose now that s ∈ [1,⌊

√

![image 379](<2021-conlon-subset-sums-completeness-colorings_images/imageFile379.png>)

ℓ⌋] is such that su is congruent to an integer in [−d/⌈

√

![image 380](<2021-conlon-subset-sums-completeness-colorings_images/imageFile380.png>)

ℓ⌉,d/⌈

√

![image 381](<2021-conlon-subset-sums-completeness-colorings_images/imageFile381.png>)

ℓ⌉] modulo d. Since P (mod d) forms a progression of common diﬀerence u in Zd, we can partition P into s subsets P1,P2,... ,Ps such that Pi (mod d) is a progression with common diﬀerence su in Zd. Each set Pi can be greedily partitioned into progressions of integers with common diﬀerence v such that all of the progressions in the partition, except the ﬁrst and last ones, have length at least ⌈

√

![image 382](<2021-conlon-subset-sums-completeness-colorings_images/imageFile382.png>)

ℓ⌉. By extending arbitrarily the progressions with length less than ⌈

√

![image 383](<2021-conlon-subset-sums-completeness-colorings_images/imageFile383.png>)

ℓ⌉, we obtain that P is contained in a union of arithmetic progressions of integers, each of length at least ⌈

√

![image 384](<2021-conlon-subset-sums-completeness-colorings_images/imageFile384.png>)

ℓ⌉, where the size of the union is at most (⌈

√

![image 385](<2021-conlon-subset-sums-completeness-colorings_images/imageFile385.png>)

ℓ⌉−1)·2s+|P| ≤ 3|P|. This veriﬁes the desired claim.

![image 386](<2021-conlon-subset-sums-completeness-colorings_images/imageFile386.png>)

![image 387](<2021-conlon-subset-sums-completeness-colorings_images/imageFile387.png>)

![image 388](<2021-conlon-subset-sums-completeness-colorings_images/imageFile388.png>)

![image 389](<2021-conlon-subset-sums-completeness-colorings_images/imageFile389.png>)

We will also need the following simple lemma in the proof of Lemma 5.6.

- Lemma 5.11. Let A be a multiset of elements of Zt and let d be a divisor of t. Then, for any u ∈ Zt/dZt such that Σt(A) ∩ (u + dZt) = ∅,


|Σt(A) ∩ (u + dZt)| ≥ |Σt(A ∩ dZt)|.

Proof. Let Su = Σt(A) ∩ (u + dZt). For all non-zero u ∈ Zt/dZt, if Su = ∅, then we can ﬁnd an element x in Su which is a sum of distinct elements of A which are not in dZt. Thus, each element of x+Σt(A∩dZt) can be written a sum of distinct elements in A, so x + Σt(A ∩ dZt) ⊆ Σt(A). It is also clear that x + Σt(A ∩ dZt) ⊆ u + dZt, so x + Σt(A ∩ dZt) ⊆ Su. If u = 0 ∈ Zt/dZt, then letting x = 0, we have x + Σt(A ∩ dZt) = Σt(A ∩ dZt) ⊆ Su. Thus, if Su is non-empty, then |Su| ≥ |Σt(A ∩ dZt)|.

![image 390](<2021-conlon-subset-sums-completeness-colorings_images/imageFile390.png>)

![image 391](<2021-conlon-subset-sums-completeness-colorings_images/imageFile391.png>)

![image 392](<2021-conlon-subset-sums-completeness-colorings_images/imageFile392.png>)

![image 393](<2021-conlon-subset-sums-completeness-colorings_images/imageFile393.png>)

We can now prove Lemma 5.6. We recall the statement, that if t ∈ [y/v,2y/v) and A is a subset of Yv of size z/(16ℓ) which is y1/4/(128ℓ)-diverse, then |Σt(A)| ≥ min(ξ,32/ℓ)t.

Proof of Lemma 5.6. We consider the following iterative process. Let Σt(0) = {0} and A0 = A. At each step i ≥ 1, we pick an element ai in Ai−1 and let Σt(i) = Σt(i−1) ∪(Σt(i −1) +ai) and Ai = Ai−1 \{ai}. In particular, Σt(i) = Σt({a1,... ,ai}) ⊆ Σt(A) for all i ≤ |A|. Let di = gcd(Ai−1). For i ≤ |A|/2, Ai−1 is a subset of Yv of size at least |A2| ≥ 32zℓ > 64(m/φ(m))τ(r,m)r logy r, where we used (14) and assumed that r is suﬃciently large in terms of ℓ. Thus, {vx : x ∈ Ai−1} is a subset of Y of size larger than 64(m/φ(m))τ(r,m)r logy r whose elements are divisible by vdi. By Lemma 5.3, we obtain vdi ≤ y1/16 and all elements of Ai−1 have the form qu where u | (m/v), u ≤ y1/16/v ≤ y1/16, di|u and gcd(q,W(r)m) = 1. We will run the above process for at most |A|/2 steps, so we may assume that i ≤ |A|/2 and these conclusions hold throughout.

![image 394](<2021-conlon-subset-sums-completeness-colorings_images/imageFile394.png>)

![image 395](<2021-conlon-subset-sums-completeness-colorings_images/imageFile395.png>)

![image 396](<2021-conlon-subset-sums-completeness-colorings_images/imageFile396.png>)

![image 397](<2021-conlon-subset-sums-completeness-colorings_images/imageFile397.png>)

For each i, we say that step i is either a growth phase, an unsaturated phase or a saturated phase. Note that the cosets of diZt can be indexed by elements of Zdi. For each u ∈ Zdi, let Su = Σt(i−1)∩(u+diZt). We say that i is a growth phase if there exists u ∈ Zdi such that Su is non-empty and has size at most y3/4. We say that i is an unsaturated phase if it is not a growth phase and there exists u ∈ Zdi such that y3/4 < |Su| < dξt

. Finally, if step i is neither a growth phase nor an unsaturated phase, then it is a saturated phase.

![image 398](<2021-conlon-subset-sums-completeness-colorings_images/imageFile398.png>)

i

Next we describe how ai is chosen. Let Σ(d,i − 1) = { j∈S aj (mod t) : S ⊆ [i − 1] ∩ {j : d|aj}}. Then Σ(d,i − 1) is a subset of the subgroup dZt of Zt, which can be identiﬁed with Zt/d. We identify Σ(d,i − 1) with a subset of Zt/d. Similarly, we can identify Ai−1 with a subset of Zt/di. If i is a growth phase, we pick ai such that |Σ(di,i)| − |Σ(di,i − 1)| is maximized. Otherwise, if i is not a growth phase, we pick ai such that |Σt(i)| − |Σt(i − 1)| is maximized.

The following claims capture the key steps in the proof.

- Claim 1. The number of growth phases among the ﬁrst |A|/2 steps is at most (256ℓy3/4/z + log3/2 t + 2)(log2 y1/16 + 1).
- Claim 2. If i ≤ |A|/2 is an unsaturated phase, then |Σt(i)| − |Σt(i − 1)| > 212y/z.


Claim 2 is the most important step in the proof and will take up most of our time. However, before proving these claims, let us see how Lemma 5.6 follows from combining them.

First, suppose that there exists i ≤ |A|/2 such that i is a saturated phase. By Lemma 5.8, since A is

- y1/4/(128ℓ)-diverse and di < y1/4/(128ℓ), Σdi({a1,... ,ai−1}) = Σdi(A) = Zdi. Hence, Su is non-empty


for all u ∈ Zdi. Since i is a saturated phase, we have that |Su| ≥ dξt

for all u ∈ Zdi, so |Σt(i − 1)| = u∈Zdi |Su| ≥ ξt. Therefore, |Σt(A)| ≥ |Σt(i − 1)| ≥ ξt, as desired.

![image 399](<2021-conlon-subset-sums-completeness-colorings_images/imageFile399.png>)

i

Next, suppose that no i ≤ |A|/2 is a saturated phase. In this case, if i ≤ |A|/2 is not a growth phase, it must be an unsaturated phase and, by Claim 2, we have |Σt(i)| > |Σt(i − 1)| + 212y/z. Since Claim 1 implies that there are at least |A|/2 − (256ℓy3/4/z + log3/2 t + 2)(log2 y1/16 + 1) unsaturated phases in the ﬁrst |A|/2 steps and |A| = z/(16ℓ), we have

212y z ·

|Σt(A)| ≥ |Σt(|A|/2)| ≥

![image 400](<2021-conlon-subset-sums-completeness-colorings_images/imageFile400.png>)

212y 64ℓ ≥

32t ℓ

z 32ℓ − (256ℓy3/4/z + log3/2 t + 2)(log2 y1/16 + 1) ≥

,

![image 401](<2021-conlon-subset-sums-completeness-colorings_images/imageFile401.png>)

![image 402](<2021-conlon-subset-sums-completeness-colorings_images/imageFile402.png>)

![image 403](<2021-conlon-subset-sums-completeness-colorings_images/imageFile403.png>)

- as required.


![image 404](<2021-conlon-subset-sums-completeness-colorings_images/imageFile404.png>)

![image 405](<2021-conlon-subset-sums-completeness-colorings_images/imageFile405.png>)

![image 406](<2021-conlon-subset-sums-completeness-colorings_images/imageFile406.png>)

![image 407](<2021-conlon-subset-sums-completeness-colorings_images/imageFile407.png>)

We next give the proofs of Claims 1 and 2, beginning with the simpler of the two.

- Proof of Claim 1. First, we show that in each step i ≤ |A|/2, if |Σ(di,i − 1)| < |Ai−1|/2, then


|Σ(di,i)| − |Σ(di,i − 1)| ≥ max

a∈Ai−1

|(Σ(di,i − 1) + a) \ Σ(di,i − 1)| ≥ |Σ(di,i − 1)|/2, (17)

while if |Ai−1|/2 ≤ |Σ(di,i − 1)| ≤ y3/4, then

|Σ(di,i)| − |Σ(di,i − 1)| ≥ max

a∈Ai−1

|(Σ(di,i − 1) + a) \ Σ(di,i − 1)| ≥ |Ai−1|/8. (18)

The ﬁrst bound (17) follows directly from Lemma 2.6, since the set of elements a ∈ Zt/di for which

|(Σ(di,i − 1) + a) \ Σ(di,i − 1)| < |Σ(di,i − 1)|/2

has size at most 2|Σ(di,i − 1)| < |Ai−1|.

For the second bound (18), assume, for the sake of contradiction, that for some step i ≤ |A|/2 where |Ai−1|/2 ≤ |Σ(di,i − 1)| ≤ y3/4, |Σ(di,i)| − |Σ(di,i − 1)| < |Ai−1|/8. Then, for all a ∈ Ai−1, we have |(Σ(di,i − 1) + a) \ Σ(di,i − 1)| < |Ai−1|/8. Let k = 4|Σ(|Adi,i−1)|

i−1| and let

![image 408](<2021-conlon-subset-sums-completeness-colorings_images/imageFile408.png>)

T = {a ∈ Zt/di : |(Σ(di,i − 1) + a) \ Σ(di,i − 1)| < |Ai−1|/8}.

We have Ai−1 ⊆ T and 0 ∈ T. By Lemma 2.7, for any a ∈ kT,

|(Σ(di,i − 1) + a) \ Σ(di,i − 1)| < |Σ(di,i − 1)|/2.

Hence, by Lemma 2.6, we have |k(Ai−1 ∪ {0})| ≤ |kT| ≤ 2|Σ(di,i − 1)|. Using that vdi ≤ y1/16 and

- t ≥ y/v, we have |Σ(di,i − 1)| ≤ y3/4 < t/(2di), so |k(Ai−1 ∪ {0})| < t/di. Identiﬁed as a subset of Zt/di, Ai−1 is not a subset of any proper subgroup of Zt/di by the deﬁnition of di, so Ai−1 ∪{0} is not contained in any coset of a proper subgroup of Zt/di. Therefore, by Lemma 2.3, we have

|Ai−1 ∪ {0}| ≤

2 k + 1|k(Ai−1 ∪ {0})| ≤

![image 409](<2021-conlon-subset-sums-completeness-colorings_images/imageFile409.png>)

4|Σ(di,i − 1)| k + 1

![image 410](<2021-conlon-subset-sums-completeness-colorings_images/imageFile410.png>)

<

4|Σ(di,i − 1)| 4|Σ(di,i − 1)|/|Ai−1|

![image 411](<2021-conlon-subset-sums-completeness-colorings_images/imageFile411.png>)

= |Ai−1|,

a contradiction. Using (17) and (18), we may quickly complete the proof of Claim 1. Note that, by Lemma 5.11, for any

- u such that Su is non-empty, |Su| ≥ |Σ(di,i − 1)|. Thus, if i is a growth phase, then |Σ(di,i − 1)| ≤ y3/4. Note that di|di+1, so either di+1 = di or di+1 ≥ 2di. As di ≤ y1/16 for i ≤ |A|/2, di can change at most 1+log2 y1/16 times in the ﬁrst |A|/2 steps. By (17), if |Σ(di,i−1)| < |Ai−1|/2, then |Σ(di,i)|−|Σ(di,i−1)| ≥ |Σ(di,i − 1)|/2. Thus, for each period among the ﬁrst |A|/2 steps where di remains constant, the number of steps where |Σ(di,i−1)| < |Ai−1|/2 is at most 1+log3/2 t, since, in each such step, |Σ(di,i−1)| grows by a factor of at least 3/2. For the remaining steps in this period, where |Ai−1|/2 ≤ |Σ(di,i−1)| ≤ y3/4, (18) implies that |Σ(di,i)|−|Σ(di,i−1)| ≥ |Ai−1|/8 ≥ z/(256ℓ) in each step, so there are at most 1+256ℓy3/4/z more growth phases where di stays constant. Thus, the number of growth phases among the ﬁrst |A|/2 steps in each period where di stays constant is at most 256ℓy3/4/z + log3/2 t + 2. Since di can change at


most 1+log2 y1/16 times in the ﬁrst |A|/2 steps, there are at most (256ℓy3/4/z+log3/2 t+2)(log2 y1/16+1) growth phases in the ﬁrst |A|/2 steps.

![image 412](<2021-conlon-subset-sums-completeness-colorings_images/imageFile412.png>)

![image 413](<2021-conlon-subset-sums-completeness-colorings_images/imageFile413.png>)

![image 414](<2021-conlon-subset-sums-completeness-colorings_images/imageFile414.png>)

![image 415](<2021-conlon-subset-sums-completeness-colorings_images/imageFile415.png>)

Finally, we give the proof of Claim 2, thereby completing the proof of Lemma 5.6.

- Proof of Claim 2. Let i be an unsaturated phase with i ≤ |A|/2. Assume, for the sake of contradiction, that |Σt(i)| − |Σt(i − 1)| ≤ 212y/z. Since i is not a growth phase and not a saturated phase, there exists


- u ∈ Zdi such that y3/4 < |Su| < dξt


.

![image 416](<2021-conlon-subset-sums-completeness-colorings_images/imageFile416.png>)

i

We now view Su and Ai−1 as subsets of Zt/di. Note that, by the deﬁnition of di, Ai−1 is not a subset of any proper subgroup of Zt/di. Let B be the set of elements a of Zt/di such that |(Su +a)\Su| ≤ 212y/z. By our choice of ai and our assumption that |Σt(i)| − |Σt(i − 1)| ≤ 212y/z, we have Ai−1 ⊆ B. Since |Su| < dξt

and |Su| > y3/4 > 8·212y/z by (14), we can apply Lemma 5.7 to conclude that either the set B is contained in a proper subgroup of Zt/di, B has size at most 20(2

![image 417](<2021-conlon-subset-sums-completeness-colorings_images/imageFile417.png>)

i

13y/z)1.02

|Su|0.02 or there is a subgroup H of Zt/di such that B is contained in a set of size at most 220y/z which is an arithmetic progression of H-cosets. The ﬁrst possibility cannot hold, since B contains Ai−1 which is not a subset of any proper subgroup of Zt/di. The second possibility also cannot hold, since

![image 418](<2021-conlon-subset-sums-completeness-colorings_images/imageFile418.png>)

20(213y/z)1.02 |Su|0.02

≤

![image 419](<2021-conlon-subset-sums-completeness-colorings_images/imageFile419.png>)

25+13·1.02y1.005 z1.02

< |A|/2 ≤ |Ai−1| ≤ |B|,

![image 420](<2021-conlon-subset-sums-completeness-colorings_images/imageFile420.png>)

where we used the bound |Su| > y3/4. Therefore, there is a subgroup H of Zt/di such that Ai−1, identiﬁed

- as a subset of Zt/di, is contained in a set R of size at most 220y/z which is an arithmetic progression of H-cosets. We can identify the elements of Zt/di with elements in [y/v,y/v + t) ⊇ [y/v,2y/v) which are

divisible by di. Under this identiﬁcation, R is identiﬁed with a set of integers which contains Ai−1. By Lemma 5.10, under the above identiﬁcation, the image of R is contained in a set of integers of size

- at most 3|R| which is a union of arithmetic progressions Ps, s ∈ S, of integers, each of length at least |R|1/3. We have |R| ≥ |Ai−1| ≥ z/(32ℓ). Thus, Ai−1 is contained in a set of size at most 222y/z which is a union of arithmetic progressions Ps of integers, each of length at least (z/(32ℓ))1/3 ≥ r1/16, by (14) and


(35) from Appendix B.2. Recall that Ai−1 is a subset of [y/v,2y/v) consisting of elements of the form qu, where u|m, u ≤ y1/16, di|u and gcd(q,W(r)m) = 1. Note that each element of the form qu where u|m and gcd(q,W(r)m) = 1 is coprime to W(r)/gcd(W(r),m). Since each arithmetic progression Ps has length

- at least r1/16 and common diﬀerence at most n, Lemma 5.9 implies that the number of elements in Ps of

the form qu, where u|m, u ≤ y1/16 and gcd(q,W(r)m) = 1, is at most

256|Ps| ·

log log n log r

![image 421](<2021-conlon-subset-sums-completeness-colorings_images/imageFile421.png>)

.

Thus, the number of elements of R (identiﬁed with a subset of [y/v,y/v + t)) of the form qu, where u|m,

- u ≤ y1/16 and gcd(q,W(r)m) = 1, is at most


222y z ·

log log n log r

log log n log r ≤ 256 ·

|Ps|) ·

.

256(

![image 422](<2021-conlon-subset-sums-completeness-colorings_images/imageFile422.png>)

![image 423](<2021-conlon-subset-sums-completeness-colorings_images/imageFile423.png>)

![image 424](<2021-conlon-subset-sums-completeness-colorings_images/imageFile424.png>)

s∈S

We claim that

222y z ·

log log n log r

z 32l

256 ·

. This holds if r ≥ 10log m/log log m, since then, from (34) in Appendix B.2, τ(r,m) ≥ 1/(4log r) and ℓy log log n z2 log r ≤

<

![image 425](<2021-conlon-subset-sums-completeness-colorings_images/imageFile425.png>)

![image 426](<2021-conlon-subset-sums-completeness-colorings_images/imageFile426.png>)

![image 427](<2021-conlon-subset-sums-completeness-colorings_images/imageFile427.png>)

![image 428](<2021-conlon-subset-sums-completeness-colorings_images/imageFile428.png>)

100ℓyr2(log log n) (log r)(m/φ(m))2y2τ(r,m)2 ≤

100ℓr2(log log n) (log r)τ(r,m)2(m/φ(m))2 ·

τ(r,m)(m/φ(m)) 15mr

![image 429](<2021-conlon-subset-sums-completeness-colorings_images/imageFile429.png>)

![image 430](<2021-conlon-subset-sums-completeness-colorings_images/imageFile430.png>)

![image 431](<2021-conlon-subset-sums-completeness-colorings_images/imageFile431.png>)

![image 432](<2021-conlon-subset-sums-completeness-colorings_images/imageFile432.png>)

![image 433](<2021-conlon-subset-sums-completeness-colorings_images/imageFile433.png>)

√

64r3(log r)(log log n)2 m(m/φ(m))3 ≤ 100ℓ

![image 434](<2021-conlon-subset-sums-completeness-colorings_images/imageFile434.png>)

64c3 ≤ 2−40,

≤ 100ℓ

![image 435](<2021-conlon-subset-sums-completeness-colorings_images/imageFile435.png>)

where we used (14) in the ﬁrst inequality, the deﬁnition of y in the second inequality, the bound τ(r,m) ≥ 1/(4log r) in the third inequality, the bound r ≤ cψ(n,m) = c m

1/3(m/φ(m))

(logn)1/3(log logn)2/3 in the fourth inequality and, in the last inequality, we assumed a suﬃciently small choice of c (depending on ℓ). Next, assume that r < 10log m/log log m. In this case, we have that r = cR(n,m) = cρ(n,m). Furthermore, m ≥ (logn2n)2 as, for n

![image 436](<2021-conlon-subset-sums-completeness-colorings_images/imageFile436.png>)

![image 437](<2021-conlon-subset-sums-completeness-colorings_images/imageFile437.png>)

2/φ(m)

3/2(log log n)1/2

(logn)1/2 ≤ m ≤ (logn2n)2, r = cρ(n,m) = Θ n

log(n2/φ(m)) by Claim B.3, so r > 10log m/log log m for suﬃciently large n, contradicting our assumption. We also have that τ(r,m) ≥ (φ(m)/m)/(2log r) by

![image 438](<2021-conlon-subset-sums-completeness-colorings_images/imageFile438.png>)

![image 439](<2021-conlon-subset-sums-completeness-colorings_images/imageFile439.png>)

![image 440](<2021-conlon-subset-sums-completeness-colorings_images/imageFile440.png>)

(32) in Appendix B.2, so

![image 441](<2021-conlon-subset-sums-completeness-colorings_images/imageFile441.png>)

100ℓr2(log log n) (log r)τ(r,m)2(m/φ(m))2 ·

ℓy log log n z2 log r ≤

τ(r,m)(m/φ(m)) 15mr

![image 442](<2021-conlon-subset-sums-completeness-colorings_images/imageFile442.png>)

![image 443](<2021-conlon-subset-sums-completeness-colorings_images/imageFile443.png>)

![image 444](<2021-conlon-subset-sums-completeness-colorings_images/imageFile444.png>)

![image 445](<2021-conlon-subset-sums-completeness-colorings_images/imageFile445.png>)

![image 446](<2021-conlon-subset-sums-completeness-colorings_images/imageFile446.png>)

8r3(log r)(log log n)2 m ≤ 100ℓ

105(log n)3 n2/(log n)2 ≤ 2−40,

≤ 100ℓ

![image 447](<2021-conlon-subset-sums-completeness-colorings_images/imageFile447.png>)

![image 448](<2021-conlon-subset-sums-completeness-colorings_images/imageFile448.png>)

assuming that n is suﬃciently large, where in the third inequality we used r < 10log m/log log m < 20log n/log log n. Thus, in both cases,

222y z ·

log log n log r

256 ·

<

![image 449](<2021-conlon-subset-sums-completeness-colorings_images/imageFile449.png>)

![image 450](<2021-conlon-subset-sums-completeness-colorings_images/imageFile450.png>)

z 32ℓ

.

![image 451](<2021-conlon-subset-sums-completeness-colorings_images/imageFile451.png>)

This is a contradiction since there are at least 32zℓ integers of the form qu where u|m,u ≤ y1/16 and gcd(q,W(r)m) = 1 contained in R. Hence, in each step i ≤ |A|/2 which is an unsaturated phase, |Σt(i)| grows by at least 212y/z.

![image 452](<2021-conlon-subset-sums-completeness-colorings_images/imageFile452.png>)

![image 453](<2021-conlon-subset-sums-completeness-colorings_images/imageFile453.png>)

![image 454](<2021-conlon-subset-sums-completeness-colorings_images/imageFile454.png>)

![image 455](<2021-conlon-subset-sums-completeness-colorings_images/imageFile455.png>)

![image 456](<2021-conlon-subset-sums-completeness-colorings_images/imageFile456.png>)

Using Lemma 5.6, we can now give the proof of Lemma 5.5, thus completing our proof of the lower bound in Theorem 1.6. Again we recall the statement, that if ℓ = ⌈32/ξ⌉ and A is a subset of Yv of size

- z/(8ℓ) which is y1/4/(32ℓ)-diverse, then |Σ(A)| ≥ 3yz/(4ℓ2v) and Σ(A) is not a subset of an arithmetic progression with common diﬀerence greater than 1. Proof of Lemma 5.5. Using Lemma 5.4, we can partition A into two sets A1,A2 such that |A1| = |A2| =


- z/(16ℓ) and A1 is y1/4/(128ℓ)-diverse. By Lemma 5.6, for each t in A2, |Σt(A1)| ≥ min(ξ,32/ℓ)t. Recall that we chose ℓ = ⌈32/ξ⌉, so |Σt(A1)| ≥ 32t/ℓ. Therefore, by repeated applications of Lemma 2.5,


|Σ(A)| = |Σ(A1 ∪ A2)| ≥

t∈A2

32t ℓ ≥ |A2| ·

32y ℓv

>

![image 457](<2021-conlon-subset-sums-completeness-colorings_images/imageFile457.png>)

![image 458](<2021-conlon-subset-sums-completeness-colorings_images/imageFile458.png>)

yz ℓ2v

.

![image 459](<2021-conlon-subset-sums-completeness-colorings_images/imageFile459.png>)

Finally, we prove that Σ(A) is not contained in an arithmetic progression with common diﬀerence d larger than 1. Indeed, if Σ(A) were contained in an arithmetic progression with common diﬀerence d larger than 1, then all elements of Σ(A) would be in the same congruence class modulo d, which in turn implies that all elements of A would be divisible by d. But this is impossible since A is y1/4/(32ℓ)-diverse.

![image 460](<2021-conlon-subset-sums-completeness-colorings_images/imageFile460.png>)

![image 461](<2021-conlon-subset-sums-completeness-colorings_images/imageFile461.png>)

![image 462](<2021-conlon-subset-sums-completeness-colorings_images/imageFile462.png>)

![image 463](<2021-conlon-subset-sums-completeness-colorings_images/imageFile463.png>)

## 5.2 Proof of the upper bound in Theorem 1.6

In this section, we show how to improve on the construction of Alon and Erdős [2] described in the introduction. We begin with the following simple claim.

Claim 5.12. There exists a positive constant κ such that the following holds. For each positive integer m, let dm be the product of all the primes at most (log m)/64 which are not prime divisors of m, where dm = 1 if the product is over an empty set. Then, for m suﬃciently large, dm ≤ m1/32, gcd(dm,m) = 1 and φ(mm) · φ(ddm

m) ≥ κlog log m. Proof. It is easy to see that dm ≤ m1/32. Furthermore,

![image 464](<2021-conlon-subset-sums-completeness-colorings_images/imageFile464.png>)

![image 465](<2021-conlon-subset-sums-completeness-colorings_images/imageFile465.png>)

p p − 1 ≥ exp   p≤(logm)/64

 

1 p

dm φ(dm) ≥

m φ(m) ·

![image 466](<2021-conlon-subset-sums-completeness-colorings_images/imageFile466.png>)

![image 467](<2021-conlon-subset-sums-completeness-colorings_images/imageFile467.png>)

![image 468](<2021-conlon-subset-sums-completeness-colorings_images/imageFile468.png>)

![image 469](<2021-conlon-subset-sums-completeness-colorings_images/imageFile469.png>)

p≤(log m)/64

≥ exp(log log((log m)/64) − κ′) ≥ κlog log m,

for some absolute constants κ′,κ.

![image 470](<2021-conlon-subset-sums-completeness-colorings_images/imageFile470.png>)

![image 471](<2021-conlon-subset-sums-completeness-colorings_images/imageFile471.png>)

![image 472](<2021-conlon-subset-sums-completeness-colorings_images/imageFile472.png>)

![image 473](<2021-conlon-subset-sums-completeness-colorings_images/imageFile473.png>)

We are now ready to prove the upper bound in Theorem 1.6. For the sake of easy reference, we recall the statement, that, for all n suﬃciently large and m ∈ [n, n2 ],

f(n,m) = O (R(n,m)) ,

1/3(m/φ(m))

where R(n,m) = min (ψ(n,m),ρ(n,m)). Here ψ(n,m) = m

(logn)1/3(log logn)2/3 and ρ(n,m) is the smallest positive integer ρ such that ρ p|W(ρ)m(1 − 1/p)−1 ≥ n2/φ(m), where W(ρ) is the product of the ﬁrst ρ primes. We also recall from the previous subsection that when m = O n

![image 474](<2021-conlon-subset-sums-completeness-colorings_images/imageFile474.png>)

3/2(log log n)1/2

(logn)1/2 , we have R(n,m) = Θ(ψ(n,m)) and when m = Ω n

![image 475](<2021-conlon-subset-sums-completeness-colorings_images/imageFile475.png>)

3/2(log log n)1/2

(logn)1/2 , we have R(m,n) = Θ(ρ(n,m)). Proof of the upper bound in Theorem 1.6. We ﬁrst consider the case where m ≤ n

![image 476](<2021-conlon-subset-sums-completeness-colorings_images/imageFile476.png>)

3/2(log log n)1/2

(logn)1/2 . Let r = Cψ(n,m) = Cm

![image 477](<2021-conlon-subset-sums-completeness-colorings_images/imageFile477.png>)

1/3(m/φ(m))

(logn)1/3(log logn)2/3 for a suﬃciently large constant C. Note that r ≥ (logn1n/)32/3. Our aim is to construct an r-coloring of [1,n − 1] such that the set of subset sums of each color class does not contain m. We will do this in four steps.

![image 478](<2021-conlon-subset-sums-completeness-colorings_images/imageFile478.png>)

![image 479](<2021-conlon-subset-sums-completeness-colorings_images/imageFile479.png>)

- Step 1. For k = 2,3,... , 2r, we form a color class S1(k) = {⌈km+1⌉,⌈km+1⌉+1,... ,⌊mk ⌋}∩[n−1], while, for


![image 480](<2021-conlon-subset-sums-completeness-colorings_images/imageFile480.png>)

![image 481](<2021-conlon-subset-sums-completeness-colorings_images/imageFile481.png>)

![image 482](<2021-conlon-subset-sums-completeness-colorings_images/imageFile482.png>)

![image 483](<2021-conlon-subset-sums-completeness-colorings_images/imageFile483.png>)

- k = 1, we take S1(1) = {⌈m2 ⌉,⌈m2 ⌉ +1,... ,m −1} ∩[n−1]. As deﬁned, the color classes may overlap, but we can safely assign any element in the overlap to any color class that includes it. Crucially, no subset sum of S1(k) can contain m, since the sum of at most k elements from S1(k) is less than m, while any sum of k + 1 elements from S1(k) is larger than m. Let X1 = r/k=12 S1(k).


![image 484](<2021-conlon-subset-sums-completeness-colorings_images/imageFile484.png>)

![image 485](<2021-conlon-subset-sums-completeness-colorings_images/imageFile485.png>)

- Step 2. For each of the ﬁrst r/4 primes p which are coprime to m, we form a color class S2(p) = {kp : k ∈ N} ∩ [1,n − 1], noting that no subset sum of S2(p) can contain m, since each element of Σ(S2(p)) is a

multiple of p. Let X2 = p≤p

r/4,p∤m S2(p).

- Step 3. Let R = [1,n −1] \ (X1 ∪X2). The construction in [2] also uses color classes like those deﬁned in Steps 1 and 2. They then arbitrarily partition the remaining elements R so that the sum of the elements in each of the classes is smaller than m. For our improvement, we need to be more careful. Note that elements in the remainder set R are natural numbers t ≤ 2rm such that t is coprime to W(r/4)/gcd(W(r/4),m), that is, all prime divisors of t which are at most pr/4 are also prime divisors of m. In particular, t is coprime to the integer dm given by Claim 5.12, since dm has only prime factors at most (log m)/64 < r/4 which are not prime divisors of m.

![image 486](<2021-conlon-subset-sums-completeness-colorings_images/imageFile486.png>)

With κ also as in Claim 5.12, we next show that there exists a multiple d of dm such that

κ(φ(m)/m)r(log log n)/64 ≤ d ≤ κ(φ(m)/m)r(log log n)/32, (19)

gcd(d,m) = 1 and the largest prime factor of d is at most pr/4. Let x = κ(φ(m)/m50d)r log logn

![image 487](<2021-conlon-subset-sums-completeness-colorings_images/imageFile487.png>)

m

. Note that x ≥ 100d κr

![image 488](<2021-conlon-subset-sums-completeness-colorings_images/imageFile488.png>)

m log logn > n1/4, since r ≥ n1/3/(log n)2/3 and dm ≤ m1/32 ≤ n1/16. Since m has at most log m ≤ 2log n distinct prime factors, there exists a prime p < n1/100 such that p does not divide m. Let k be the smallest positive integer such that x/pk < n1/100. Then x/pk−1 ∈ [n1/100,n2/100] and, by the prime number theorem, the interval [(1−1/100)x/pk−1,(1+1/100)x/pk−1] has at least 10−3n1/100/(log n) primes for suﬃciently large n. Thus, there exists a prime p′ in this interval which does not divide m. Then p′pk−1 ∈ [(1−1/100)x,(1+1/100)x] and gcd(p′pk−1,m) = 1, since p′ and p are primes which do not divide m. We can now verify that d = p′pk−1dm satisﬁes (19), gcd(d,m) = 1 and the largest prime factor of d is at most 2n2/100 < pr/4 (noting that all prime factors of dm are at most (log m)/64 < 2n2/100). Since dm|d, we also have d/φ(d) ≥ dm/φ(dm). Furthermore, all elements of R are coprime to d, since any element in R is coprime to W(r/4)/gcd(W(r/4),m), whereas d is coprime to m and all prime factors of d are at most pr/4.

Fix s ∈ Z×d . Then there exist k integers congruent to s (mod d) that sum to m only if sk ≡ m (mod d). Let xs be the positive integer in [d] that is congruent to s−1m (mod d). Consider now the color classes

Ss,1 = t : t ∈ R,t ≡ s (mod d),t ≥

m xs

![image 489](<2021-conlon-subset-sums-completeness-colorings_images/imageFile489.png>)

,

Ss,2 = t : t ∈ R,t ≡ s (mod d),

m d + xs ≤ t <

![image 490](<2021-conlon-subset-sums-completeness-colorings_images/imageFile490.png>)

m xs

![image 491](<2021-conlon-subset-sums-completeness-colorings_images/imageFile491.png>)

.

If a sum of k elements in Ss,1 is equal to m (mod d), then k ≥ xs. But then the sum of the k elements is larger than m. Similarly, if a sum of k elements in Ss,2 is equal to m (mod d), then k = xs or k ≥ d + xs. But the sum of k elements is less than m if k = xs and larger than m if k ≥ d + xs. Thus, m ∈/ Σ(Ss,1) ∪ Σ(Ss,2). Note that in this step we have in total deﬁned 2φ(d) color classes of the form Ss,1 and Ss,2 for s ∈ Z×d .

- Step 4. Let R′ = R \ ( s∈Z×


(Ss,1 ∪ Ss,2)). Then all elements of R′ are less than m/d. Thus, if we arbitrarily partition R′ into sets of size at most d, then no set contains a subset sum which is equal to m. Hence, we need at most |R′|/d colors to color R′ so that no color class contains m as a subset sum. Recall

d

that any element in R′ is coprime to W(r/4)/gcd(W(r/4),m). By the second part of Lemma 5.9, applied to the interval [1,m/d], we have

|R′| ≤ 256(m/d)

(1 − 1/p)

p|W(r/4),p∤m

(1 − 1/p)−1

≤ 256(m/d)

(1 − 1/p)

p|W(r/4)

p|m,p≤r/4

500m(m/φ(m)) dlog r

<

,

![image 492](<2021-conlon-subset-sums-completeness-colorings_images/imageFile492.png>)

where we used that r is suﬃciently large, so that p|W(r/4)(1 − 1/p) ≤ 1.1/log r, and p|m,p≤r/4(1 − 1/p)−1 ≤ m/φ(m). Therefore, the number of color classes used in Step 4 is at most

642 · 500m(m/φ(m))3 κ2r2(log r)(log log n)2

500m(m/φ(m)) d2 log r ≤

![image 493](<2021-conlon-subset-sums-completeness-colorings_images/imageFile493.png>)

![image 494](<2021-conlon-subset-sums-completeness-colorings_images/imageFile494.png>)

r 16

,

<

![image 495](<2021-conlon-subset-sums-completeness-colorings_images/imageFile495.png>)

where the ﬁrst inequality follows from (19) and in the second inequality we have assumed that the constant C is chosen suﬃciently large.

Combining all four steps, the total number of colors we have used is at most

r 4

r 16 ≤

r 2

+

+ 2φ(d) +

![image 496](<2021-conlon-subset-sums-completeness-colorings_images/imageFile496.png>)

![image 497](<2021-conlon-subset-sums-completeness-colorings_images/imageFile497.png>)

![image 498](<2021-conlon-subset-sums-completeness-colorings_images/imageFile498.png>)

13r 16

+

![image 499](<2021-conlon-subset-sums-completeness-colorings_images/imageFile499.png>)

2md κφ(m)log log n ≤

- 7r

![image 500](<2021-conlon-subset-sums-completeness-colorings_images/imageFile500.png>)

- 8


,

![image 501](<2021-conlon-subset-sums-completeness-colorings_images/imageFile501.png>)

where we have used Claim 5.12, so that d/φ(d) ≥ dm/φ(dm) ≥ κ(log log m)φ(m)/m ≥ κ(log log n)φ(m)/m, and the bound (19). Thus, we can use at most r colors to color [1,n − 1] such that no monochromatic subset sum is equal to m, as required.

3/2(log log n)1/2

Next we consider the case m ∈ n

(logn)1/2 , n2 . Let r = Cρ(n,m), where C is a suﬃciently large absolute constant. We construct the coloring as follows.

![image 502](<2021-conlon-subset-sums-completeness-colorings_images/imageFile502.png>)

- Step 1. For each of the ﬁrst 7r/8 primes p that do not divide m, we construct a color class S1(p) = {kp :

k ∈ N}. Let X1 = p≤p

7r/8,p∤m S1(p).

- Step 2. Let R = [1,n − 1] \ X1. The set R consists of those integers less than n which are coprime to W(7r/8)/gcd(W(7r/8),m). By Lemma 5.9, the number of elements of R is at most


(1 − 1/p)−1

(1 − 1/p) ≤ 256n

(1 − 1/p) ·

256n

p|W(7r/8),p∤m

p|W(ρ(n,m))m

p| gcd(m,W(ρ(n,m)))

(1 − 1/p),

≤ 256n(m/φ(m))

p|W(ρ(n,m))m

where in the ﬁrst inequality we used that 7r/8 = 7Cρ(n,m)/8 > ρ(n,m), which holds by choosing the constant C to be suﬃciently large, and in the second inequality we used p|gcd(m,W(ρ(n,m)))(1 − 1/p)−1 ≤

p|m(1 − 1/p)−1 = m/φ(m). Since each element of R is less than n, if a color class contains at most m/n elements, then no sum of

elements from the color class can equal m. Thus, we can use at most |R| m/n ≤ 256n2/φ(m) ·

(1 − 1/p) ≤ 256ρ(n,m)

![image 503](<2021-conlon-subset-sums-completeness-colorings_images/imageFile503.png>)

p|W(ρ(n,m))m

colors to color the elements of R so that no monochromatic subset sum equals m. The second inequality follows from the deﬁnition of ρ(n,m), which is the smallest positive integer such that ρ(n,m) p|W(ρ(n,m))m(1− 1/p)−1 ≥ n2/φ(m). Hence, the total number of colors we used is at most

7r 8

+ 256ρ(n,m) ≤ r,

![image 504](<2021-conlon-subset-sums-completeness-colorings_images/imageFile504.png>)

assuming that C is a suﬃciently large absolute constant.

![image 505](<2021-conlon-subset-sums-completeness-colorings_images/imageFile505.png>)

![image 506](<2021-conlon-subset-sums-completeness-colorings_images/imageFile506.png>)

![image 507](<2021-conlon-subset-sums-completeness-colorings_images/imageFile507.png>)

![image 508](<2021-conlon-subset-sums-completeness-colorings_images/imageFile508.png>)

# 6 Long homogeneous progressions in subset sums

In this section, we prove Theorem 1.9, strengthening Theorem 1.8, Szemerédi and Vu’s result [40] on arithmetic progressions in subset sums, by showing that the progression may be taken to be homogeneous. For our application to the Erdős–Graham problem in Section 7, we will need a somewhat technical strengthening of this result, for which it will be useful to have the notation

Σ[h](A) =

s : S ⊆ A,|S| ≤ h .

s∈S

The main result of this section, which includes Theorem 1.9 as a special case, is now as follows. To gain some intuition, we remark that for a typical set A which is not dominated by multiples of an integer at least 2, we will simply have d = 1.

Theorem 6.1. There exists an absolute constant C > 0 such that the following holds. For any subset A of [n] of size m ≥ C√n, there exists d ≥ 1 such that, for A′ = {x/d : x ∈ A,d|x} and k = 250n/m, Σ[k](A′) contains an interval of length at least n. Furthermore,

![image 509](<2021-conlon-subset-sums-completeness-colorings_images/imageFile509.png>)

230n m

|A| − |A′| ≤ 230(log n)3 +

.

![image 510](<2021-conlon-subset-sums-completeness-colorings_images/imageFile510.png>)

Theorem 1.9 immediately follows from Theorem 6.1 by noticing that Σ(A) contains the set {dy : y ∈ Σ[k](A′)}, which is a homogeneous arithmetic progression with common diﬀerence d.

As a crucial step in the proof of Theorem 6.1, we ﬁrst show that subsets of Zb satisfying a diversity condition have a large set of subset sums. We will need to use the mod b analogue of Σ[h](A), namely,

Σ[bh](A) =

s mod b : S ⊆ A,|S| ≤ h .

s∈S

- Lemma 6.2. Let b be a positive integer. Let A be a subset of Zb of size m ∈ (80(log b)2,b] such that, for each d|b with d ∈ [2,4b/m], there are at least 64(log b)2 + 8d elements in A which are not divisible by d.


Let k = 1280b/m. Then

|Σ[bk+1](A)| ≥ min(m2/256,b/4). Proof. Let A′ be a uniformly random subset of A of size 3m/4 and A′′ = A \ A′. Let E1 be the event that for some d|b with d ∈ [2,4b/m], there are at most 8(log b)2 +d elements in A′ which are not divisible by d. Recall that for each d|b and d ∈ [2,4b/m], at least 64(log b)2 + 8d elements of A are not divisible by d. By the Chernoﬀ bound for hypergeometric distributions, the probability that there are at most 8(log b)2 + d elements in A′ which are not divisible by d is at most exp(−64(log b)2/32) ≤ 1/b2. By taking a union bound over all d|b, the probability that E1 happens is then at most 1/b < 1. We may therefore ﬁx a choice of A′ and A′′ so that E1 does not hold.

We consider the following iterative process. Let Σb(0) = A′′ and let A0 = A′. At each step i ≥ 1, we pick an element ai in Ai−1 and let Ai = Ai−1 \ {ai} and Σb(i) = Σb(i −1) ∪(Σb(i −1) +ai). Observe that the elements in Σb(i) can be written as the sum of one element in A′′ and a subset of A′ of size at most i, so Σb(i) ⊆ Σ[bi+1](A). Let di|b be such that Ai−1 = diZb ∼= Zb/di, where X denotes the subgroup generated by X. Note that, by deﬁnition, di|dj if i ≤ j. Furthermore, |Ai−1| ≤ b/di and |Ai−1| = 3m/4−i+1 ≥ m/4 for i ≤ m/2, so di ≤ 4b/m for i ≤ m/2. We will run the above process for at most m/2 steps, so we only consider i ≤ m/2 throughout.

For each i, we say that step i is either a growth phase, an unsaturated phase or a saturated phase. For each u ∈ Zb/diZb ∼= Zdi, let Su = Σb(i −1) ∩(u +diZb). We then say that step i is a growth phase if there exists u ∈ Zb/diZb ∼= Zdi such that Su is non-empty and has size at most |Ai−1|/4. We say that step i is an unsaturated phase if it is not a growth phase and there exists u ∈ Zb/diZb such that |Ai4−1| < |Su| < 4bd

. Finally, if step i is neither a growth phase nor an unsaturated phase, then it is a saturated phase. We remark that if di = d for all steps i in an interval [x,y], then the interval can be partitioned into three (possibly empty) intervals such that the steps in the ﬁrst interval are all growth phases, the steps in the second interval are all unsaturated phases and the steps in the third interval are all saturated phases.

![image 511](<2021-conlon-subset-sums-completeness-colorings_images/imageFile511.png>)

![image 512](<2021-conlon-subset-sums-completeness-colorings_images/imageFile512.png>)

i

We next discuss how to pick ai, which depends on the type of phase. For d|b, let Σ(d,i − 1) = Σb({a1,... ,ai−1} ∩dZb). If step i is a growth phase, we pick ai which maximizes |Σ(di,i)| −|Σ(di,i −1)|. If step i is an unsaturated or saturated phase, we pick ai which maximizes |Σb(i)| − |Σb(i − 1)|.

The following claims record important properties of the process we have deﬁned.

- Claim 1. The ﬁrst (log b)2 steps are not growth phases. Proof. Consider i ≤ (log b)2. Note that i ≤ m/2. Since, for each d|b with d ∈ [2,4b/m], there are more than 8(log b)2 elements in A′ which are not divisible by d, there must be at least 7(log b)2 elements in Ai−1 which are not divisible by d. Hence, di = 1. Thus, there is only one coset u of diZb in Zb and |Su| ≥ |Σb(0)| = m/4 ≥ |Ai−1|/4, so i is not a growth phase.

![image 513](<2021-conlon-subset-sums-completeness-colorings_images/imageFile513.png>)

![image 514](<2021-conlon-subset-sums-completeness-colorings_images/imageFile514.png>)

![image 515](<2021-conlon-subset-sums-completeness-colorings_images/imageFile515.png>)

![image 516](<2021-conlon-subset-sums-completeness-colorings_images/imageFile516.png>)

- Claim 2. There are at most 20(log b)(log(4b/m)) growth phases among the ﬁrst m/2 steps.


Proof. Suppose that step i is a growth phase. By Lemma 5.11, for u ∈ Zb/diZb, if Su is non-empty, then |Su| ≥ |Σ(di,i − 1)|. Since we are in a growth phase, there is some u such that Su is non-empty and |Su| ≤ |Ai−1|/4. This implies that |Σ(di,i − 1)| ≤ |Ai−1|/4. By Lemma 2.6, the set of a ∈ diZb such that |(Σ(di,i − 1) + a) \ Σ(di,i − 1)| ≤ 21|Σ(di,i − 1)| has size at most 2|Σ(di,i − 1)| ≤ |Ai−1|/2. Thus, there exists ai ∈ Ai−1 such that |Σ(di,i)| ≥ 23|Σ(di,i − 1)|. As |Σ(di,i)| ≤ b for all i, there can be at most

![image 517](<2021-conlon-subset-sums-completeness-colorings_images/imageFile517.png>)

![image 518](<2021-conlon-subset-sums-completeness-colorings_images/imageFile518.png>)

- 1 + log3/2 b successive growth phases with di = d. Since d1 ≤ d2 ≤ ··· ≤ dm/2 ≤ 4b/m and di+1 ≥ 2di


if di+1 = di, di can take at most 1 + log2(4b/m) distinct values. This shows that there can be at most (1 + log3/2 b)(1 + log2(4b/m)) < 20(log b)(log(4b/m)) growth phases among the ﬁrst m/2 steps.

![image 519](<2021-conlon-subset-sums-completeness-colorings_images/imageFile519.png>)

![image 520](<2021-conlon-subset-sums-completeness-colorings_images/imageFile520.png>)

![image 521](<2021-conlon-subset-sums-completeness-colorings_images/imageFile521.png>)

![image 522](<2021-conlon-subset-sums-completeness-colorings_images/imageFile522.png>)

- Claim 3. Let i be an unsaturated phase. Then |Σb(i)| − |Σb(i − 1)| ≥ |A16i−1|. Proof. Note that if a ∈ Ai−1, then a ∈ diZb, since Ai−1 ⊆ diZb. Thus, for each u ∈ Zb/diZb and x ∈ Zb, x + a ∈ u + diZb if and only if x ∈ u + diZb. Hence, (Σb(i − 1) + a) ∩ (u + diZb) = (Σb(i − 1) ∩ (u + diZb)) + a = Su + a and ((Σb(i − 1) + a) \ Σb(i − 1)) ∩ (u + diZb)) = (Su + a) \ Su. Let u0 be such that |Su0| = maxu:|Su|<b/4di |Su|. We have

![image 523](<2021-conlon-subset-sums-completeness-colorings_images/imageFile523.png>)

|(Σb(i − 1) + a) \ Σb(i − 1)| =

u∈Zb/diZb

|((Σb(i − 1) + a) \ Σb(i − 1)) ∩ (u + diZb)|

=

u∈Zb/diZb

|(Su + a) \ Su|

≥ |(Su0 + a) \ Su0|.

Let ki = 1 + | 4A|Su0|

![image 524](<2021-conlon-subset-sums-completeness-colorings_images/imageFile524.png>)

i−1| ∈ 2, |8A|Su0|

![image 525](<2021-conlon-subset-sums-completeness-colorings_images/imageFile525.png>)

i−1| , noting that |Su0| > |Ai−1|/4 since step i is not a growth phase. Let Pi−1 ⊆ diZb be the set of elements a ∈ diZb such that |(Su0 +a)\Su0| < 21k

![image 526](<2021-conlon-subset-sums-completeness-colorings_images/imageFile526.png>)

i

|Su0|. Note that 0 ∈ Pi−1 and, by Lemma 2.7, for any a ∈ kiPi−1, |(Su0 +a) \ Su0| < 21|Su0|. Therefore, by Lemma 2.6, |kiPi−1| ≤ 2|Su0|. Suppose now that Ai−1 ⊆ Pi−1. Since di is deﬁned so that Ai−1 = diZb ∼= Zb/di, Ai−1 is not a subset of a proper subgroup of Zb/di and, since 0 ∈ Pi−1, Pi−1 is not contained in a coset of a proper subgroup of Zb/di. Thus, by Lemma 2.3 and the fact that |kiPi−1| ≤ 2|Su0| < 2bd

![image 527](<2021-conlon-subset-sums-completeness-colorings_images/imageFile527.png>)

![image 528](<2021-conlon-subset-sums-completeness-colorings_images/imageFile528.png>)

i

< |Zb/di|, |Pi−1| ≤ 2|kikPi−1|

![image 529](<2021-conlon-subset-sums-completeness-colorings_images/imageFile529.png>)

i

≤ k4

![image 530](<2021-conlon-subset-sums-completeness-colorings_images/imageFile530.png>)

i

|Su0|. However, by our choice of ki, |Ai−1| > k4

![image 531](<2021-conlon-subset-sums-completeness-colorings_images/imageFile531.png>)

i

|Su0|, which is a contradiction. Therefore, Ai−1 ∩ Pic−1 = ∅ and, since ai is chosen so that |Σb(i)| − |Σb(i − 1)| = |(Σb(i − 1) + ai) \ Σb(i − 1)| is maximized,

|(Σb(i − 1) + ai) ∪ Σb(i − 1)| ≥ |Σb(i − 1)| +

- 1

![image 532](<2021-conlon-subset-sums-completeness-colorings_images/imageFile532.png>)

- 2ki|Su0|


≥ |Σb(i − 1)| + |Ai−1| 16|Su0|

![image 533](<2021-conlon-subset-sums-completeness-colorings_images/imageFile533.png>)

|Su0|

= |Σb(i − 1)| + |Ai−1| 16

![image 534](<2021-conlon-subset-sums-completeness-colorings_images/imageFile534.png>)

.

Thus, over any unsaturated phase i, |Σb(i)| − |Σb(i − 1)| ≥ |A16i−1|.

![image 535](<2021-conlon-subset-sums-completeness-colorings_images/imageFile535.png>)

![image 536](<2021-conlon-subset-sums-completeness-colorings_images/imageFile536.png>)

![image 537](<2021-conlon-subset-sums-completeness-colorings_images/imageFile537.png>)

![image 538](<2021-conlon-subset-sums-completeness-colorings_images/imageFile538.png>)

![image 539](<2021-conlon-subset-sums-completeness-colorings_images/imageFile539.png>)

- Claim 4. For each step i ≤ m/2, Su = Σb(i − 1) ∩ (u + diZb) is non-empty for every u ∈ Zb/diZb. Proof. The claim holds trivially if di = 1. Assume that di > 1. Since i ≤ m/2, we have di|b and di ≤ 4b/m. For each d|di with d > 1, we have d|b and d ∈ [2,4b/m], so A′ contains at least d − 1 elements which are not divisible by d. By Lemma 5.8,


Σdi({a1,... ,ai−1}) = Σdi(A′) = Zdi,

where we used that the elements of A′ \ {a1,... ,ai−1} are all divisible by di. The claim follows upon noting that we can identify Zb/diZb with Zdi and, under this identiﬁcation, Su is non-empty if and only if u ∈ Σdi({a1,... ,ai−1}).

![image 540](<2021-conlon-subset-sums-completeness-colorings_images/imageFile540.png>)

![image 541](<2021-conlon-subset-sums-completeness-colorings_images/imageFile541.png>)

![image 542](<2021-conlon-subset-sums-completeness-colorings_images/imageFile542.png>)

![image 543](<2021-conlon-subset-sums-completeness-colorings_images/imageFile543.png>)

We now complete the proof of the lemma using these claims. First, assume that there is no saturated

phase i with i ≤ min(m/2,k). Then, among the ﬁrst min(m/2,k) steps, from Claims 1 and 2, at least max(min(m/2,k) − 20(log b)(log(4b/m)),min((log b)2,k)) steps are unsaturated phases. Note that if k = 1280b/m ≤ 80(log b)2, then (log b)2 ≥ k/80 and

max(min(m/2,k) − 20(log b)(log(4b/m)),min((log b)2,k)) ≥ min((log b)2,k) ≥ k/80.

If k = 1280b/m ≥ 80(log b)2, then 20(log b)(log(4b/m)) ≤ k/2 and 20(log b)(log(4b/m)) ≤ m/4 by our assumption on m, so

max(min(m/2,k) − 20(log b)(log(4b/m)),min((log b)2,k)) ≥ min(m/2,k) − 20(log b)(log(4b/m)) ≥ min(m/4,k/2).

In either case, we have

max(min(m/2,k) − 20(log b)(log(4b/m)),min((log b)2,k)) ≥ min(m/4,k/80).

For each step i which is an unsaturated phase, we have, by Claim 3, that |Σb(i)|−|Σb(i−1)| ≥ |Ai−1|/16 ≥ m/64. Hence, recalling that k = 1280b/m, we get

|Σ[bk+1](A)| ≥ |Σb(min(m/2,k))| ≥ min

m 4

,

![image 544](<2021-conlon-subset-sums-completeness-colorings_images/imageFile544.png>)

k 80 ·

m 64

= min

![image 545](<2021-conlon-subset-sums-completeness-colorings_images/imageFile545.png>)

![image 546](<2021-conlon-subset-sums-completeness-colorings_images/imageFile546.png>)

m2 256

b 4

,

![image 547](<2021-conlon-subset-sums-completeness-colorings_images/imageFile547.png>)

![image 548](<2021-conlon-subset-sums-completeness-colorings_images/imageFile548.png>)

.

If, instead, there is a saturated phase i0 with i0 ≤ min(m/2,k), then, for each u ∈ Zb/di0Zb with Su = Σb(i0 − 1) ∩ (u + di0Zb) non-empty, |Su| ≥ 4db

. But Claim 4 implies that Su is non-empty for all

![image 549](<2021-conlon-subset-sums-completeness-colorings_images/imageFile549.png>)

i0

- u ∈ Zb/di0Zb, so that


b 4

b 4di0 · di0 =

|Σ[bk+1](A)| ≥ |Σb(i0)| ≥

|Su| ≥

.

![image 550](<2021-conlon-subset-sums-completeness-colorings_images/imageFile550.png>)

![image 551](<2021-conlon-subset-sums-completeness-colorings_images/imageFile551.png>)

u∈Zb/di0Zb

Hence, the desired conclusion holds in both cases. Let ℓ = 215. We say that a subset A of [n] of size m is nice if the following conditions hold:

![image 552](<2021-conlon-subset-sums-completeness-colorings_images/imageFile552.png>)

![image 553](<2021-conlon-subset-sums-completeness-colorings_images/imageFile553.png>)

![image 554](<2021-conlon-subset-sums-completeness-colorings_images/imageFile554.png>)

![image 555](<2021-conlon-subset-sums-completeness-colorings_images/imageFile555.png>)

- (i) There is no d ∈ [2,8ℓn/m] such that all but at most 512ℓ(log n)2 + 64ℓd elements of A are divisible by d.
- (ii) For each dyadic interval Ij = [2j−1,2j) ∩ [n], either |A ∩ Ij| = 0 or |A ∩ Ij| ≥ 64ℓ(log n).


The next lemma says that any large subset of [n] contains a multiple of a large nice set.

- Lemma 6.3. There exists a constant C > 0 such that the following holds. Let A be a subset of [n] of size m ≥ Cn1/2. Then there is an integer d and a set A′ of integers such that


- • A′ is nice,
- • {dx : x ∈ A′} ⊆ A and
- • |A| − |A′| ≤ 1000ℓ(log n)3 + 256mℓn.


![image 556](<2021-conlon-subset-sums-completeness-colorings_images/imageFile556.png>)

Proof. We consider the following iteration. Let A0 = A and n0 = n. Note that A0 ⊆ [n0]. For each i ≥ 0, if |Ai| < m/2, we stop. If Ai is nice, we let A′ = Ai and stop. Otherwise, Ai ⊆ [ni] is not nice and |Ai| ≥ m/2. If (i) does not hold, we let Ai+1 = {x/di : x ∈ Ai,di|x}, where di ∈ [2,8ℓn/|Ai|] is such that all but at most 512ℓ(log n)2 +64ℓdi elements of Ai are divisible by di. Note that di ≤ 8ℓn/|Ai| ≤ 16ℓn/m. Let ni+1 = ni/di. Then

|Ai+1| ≥ |Ai| − 512ℓ(log n)2 − 64ℓdi

and Ai+1 ⊆ [ni+1]. If (i) holds and (ii) does not hold, we remove all elements in Ai which are contained in dyadic intervals Ij with |A ∩ Ij| < 64ℓ(log n) and let Ai+1 be the resulting set. Let ni+1 = ni, so Ai+1 ⊆ [ni+1], and let di = 1. In this case, |Ai+1| ≥ |Ai| − 64ℓ(log n)(1 + log2 n).

We show that we will always stop and output a nice set with the required properties. Let s be the

step where we stop. Note that there can be at most log2 n steps where (i) does not hold. Furthermore, the number of steps where (ii) does not hold is at most one more than the number of steps where (i) does not hold. Thus, we have

|As| ≥ |A0| − (1 + log2 n)(512ℓ(log n)2 + 64ℓ(log n)(1 + log2 n)) − 64ℓ

i≤s−1:di>1

Furthermore, ns = n/( i≤s−1 di), so As ⊆ [n/( i≤s−1 di)]. We also have that

di. (20)

|As| ≥ |As−1| − max(64ℓ(log n)(1 + log2 n),512ℓ(log n)2 + 64ℓds−1) ≥ |As−1| − 512ℓ(log n)2 − 1024ℓ2n/m ≥ m/4,

where we used that ds−1 ≤ 16ℓn/m, |As−1| ≥ m/2, m ≥ C√n for a suﬃciently large constant C and n is suﬃciently large. Hence,

![image 557](<2021-conlon-subset-sums-completeness-colorings_images/imageFile557.png>)

di ≤ n/|As| ≤ 4n/m.

i≤s−1

i>1 di ≤ i≤s−1 di ≤ 4n/m. Hence, combining with (20),

Since di ≥ 2 for each i ≤ s−1 with di > 1, we have i≤s−1:d

4n m ≥ m−1000ℓ(log n)3−

256ℓn m ≥

m 2

|As| ≥ |A0|−(1+log2 n)(512ℓ(log n)2+64ℓ(log n)(1+log2 n))−64ℓ·

,

![image 558](<2021-conlon-subset-sums-completeness-colorings_images/imageFile558.png>)

![image 559](<2021-conlon-subset-sums-completeness-colorings_images/imageFile559.png>)

![image 560](<2021-conlon-subset-sums-completeness-colorings_images/imageFile560.png>)

assuming that m ≥ C√n for C suﬃciently large and n is suﬃciently large. This implies that the iteration stops at step s because As is nice. The set A′ = As then satisﬁes all of the required properties.

![image 561](<2021-conlon-subset-sums-completeness-colorings_images/imageFile561.png>)

![image 562](<2021-conlon-subset-sums-completeness-colorings_images/imageFile562.png>)

![image 563](<2021-conlon-subset-sums-completeness-colorings_images/imageFile563.png>)

![image 564](<2021-conlon-subset-sums-completeness-colorings_images/imageFile564.png>)

![image 565](<2021-conlon-subset-sums-completeness-colorings_images/imageFile565.png>)

We are now in a position to prove the main result of this section, Theorem 6.1.

Proof of Theorem 6.1. By Lemma 6.3, we can ﬁnd a nice set A′ and an integer d such that {dx : x ∈ A′} ⊆ A and

256ℓn m

|A| − |A′| ≤ 1000ℓ(log n)3 +

.

![image 566](<2021-conlon-subset-sums-completeness-colorings_images/imageFile566.png>)

In particular, |A′| ≥ 5|A|/8 for n suﬃciently large. Partition A′ into ℓ sets A′1,... ,A′ℓ as follows. Let

A′< be the set consisting of the 7|A′|/8 smallest elements in A′ and let A′> be the remaining elements. Partition A′< into ℓ sets A′<,1,... ,A′<,ℓ, each of size |A′<|/ℓ, and partition A′> into ℓ sets A′>,1,... ,A′>,ℓ, each of size |A′>|/ℓ, uniformly at random. Let A′i = A′<,i ∪ A′>,i.

>,i| be a uniformly random enumeration of A′>,i and we then deﬁne two sets Bi,1 = {bi,1,bi,2,... ,bi,|A′

Let bi,1,bi,2,... ,bi,|A′

>,i|}. Let k′ = 2560ℓn/m+1. Theorem 6.1 will follow easily from the next two claims.

>,i|/2} and Bi,2 = {bi,|A′

>,i|/2+1,... ,bi,|A′

- Claim 1. Suppose that C and n are suﬃciently large. Then, with probability at least 3/4, for all i ∈ [ℓ] and all j ∈ [|A′>,i|/2 + 1,|A′>,i|],

|Σ[k

′]

bi,j(A′<,i ∪ Bi,1)| ≥

bi,j 4

![image 567](<2021-conlon-subset-sums-completeness-colorings_images/imageFile567.png>)

.

- Claim 2. Let M(i) be the sum of the largest k′ elements in Bi,2, let M(i) be the sum of the largest 2k′


![image 568](<2021-conlon-subset-sums-completeness-colorings_images/imageFile568.png>)

elements in A′i and let M be the sum of the largest 2ℓk′ elements in A′. Then, with probability at least 3/4, for all i ∈ [ℓ],

M 8ℓ

M(i) ≥

![image 569](<2021-conlon-subset-sums-completeness-colorings_images/imageFile569.png>)

and

4M ℓ

![image 570](<2021-conlon-subset-sums-completeness-colorings_images/imageFile570.png>)

M(i) ≤

.

![image 571](<2021-conlon-subset-sums-completeness-colorings_images/imageFile571.png>)

Before proving these claims, we show how to complete the proof of Theorem 6.1 assuming that their conclusions both hold, which happens with probability at least 1/2. For any subset J of [|A′>,i|/2+1,|A′>,i|] of size k′, let J = {j1,j2,... ,jk′} for j1 < j2 < ··· < jk′. A straightforward adaptation of Lemma 2.5 shows that for any set of integers A and any integer m ∈/ A, we have |Σ[h+1](A ∪ {m})| ≥ |Σ[h](A)| + |Σ[mh](A)|. For each v ≤ k′, apply this statement with h = k′+v−1, m = bi,jv and A = A′<,i∪Bi,1∪{bi,j1,... ,bi,jv−1} to conclude that

|Σ[k′+v](A′<,i ∪ Bi,1 ∪ {bi,j1,... ,bi,jv})| ≥ |Σ[k′+v−1](A′<,i ∪ Bi,1 ∪ {bi,j1,... ,bi,jv−1})| + |Σ[k

′+v−1]

bi,jv (A′<,i ∪ Bi,1 ∪ {bi,j1,... ,bi,jv−1})| ≥ |Σ[k′+v−1](A′<,i ∪ Bi,1 ∪ {bi,j1,... ,bi,jv−1})| + |Σ[k

′]

bi,jv(A′<,i ∪ Bi,1)|. Thus,

|Σ[2k′](A′<,i ∪ Bi)| ≥ |Σ[2k′](A′<,i ∪ Bi,1 ∪ {bi,j1,... ,bi,jk′})| ≥

v≤k′

′]

|Σ[k

bi,jv(A′<,i ∪ Bi,1)|.

′]

By Claim 1, we have, for each v ≤ k′, that |Σ[k

bi,jv(A′<,i ∪ Bi,1)| ≥ bi,jv/4. Thus,

1 4 j∈J

1 4 v≤k′

|Σ[2k′](A′<,i ∪ Bi)| ≥

bi,j.

bi,jv =

![image 572](<2021-conlon-subset-sums-completeness-colorings_images/imageFile572.png>)

![image 573](<2021-conlon-subset-sums-completeness-colorings_images/imageFile573.png>)

By choosing J to be the set of indices of the k′ largest elements of Bi,2, we obtain that

|Σ[2k′](A′i)| ≥

1 4

M(i).

![image 574](<2021-conlon-subset-sums-completeness-colorings_images/imageFile574.png>)

Therefore, by Claim 2, we have that, for all i ∈ [ℓ],

M 32ℓ ≥

4M ℓ

1 128

|Σ[2k′](A′i)| ≥

.

![image 575](<2021-conlon-subset-sums-completeness-colorings_images/imageFile575.png>)

![image 576](<2021-conlon-subset-sums-completeness-colorings_images/imageFile576.png>)

![image 577](<2021-conlon-subset-sums-completeness-colorings_images/imageFile577.png>)

Also by Claim 2, Σ[2k′](A′i) ⊆ [M(i)] ⊆ [4M/ℓ]. Therefore, by Lemma 2.2 with q = 4M/ℓ and n = q/128, Σ[2k′](A′1) + ··· + Σ[2k′](A′ℓ) contains an interval of length at least

![image 578](<2021-conlon-subset-sums-completeness-colorings_images/imageFile578.png>)

4M ℓ · ℓ =

1 64

1 256 ·

M ≥

![image 579](<2021-conlon-subset-sums-completeness-colorings_images/imageFile579.png>)

![image 580](<2021-conlon-subset-sums-completeness-colorings_images/imageFile580.png>)

![image 581](<2021-conlon-subset-sums-completeness-colorings_images/imageFile581.png>)

1 128

ℓk′m > n,

![image 582](<2021-conlon-subset-sums-completeness-colorings_images/imageFile582.png>)

where we used that M is the sum of the largest 2ℓk′ < |A′|/2 elements of A′, so that M ≥ 2ℓk′|A′|/2 > ℓk′m/2, the bound k′ ≥ 2560mℓn and ℓ = 215. Thus, Σ[2ℓk′](A′) contains an interval of length at least n.

![image 583](<2021-conlon-subset-sums-completeness-colorings_images/imageFile583.png>)

![image 584](<2021-conlon-subset-sums-completeness-colorings_images/imageFile584.png>)

![image 585](<2021-conlon-subset-sums-completeness-colorings_images/imageFile585.png>)

![image 586](<2021-conlon-subset-sums-completeness-colorings_images/imageFile586.png>)

![image 587](<2021-conlon-subset-sums-completeness-colorings_images/imageFile587.png>)

- Proof of Claim 1. Assume that, for some i ∈ [ℓ] and j ∈ [|A′>,i|/2 + 1,|A′>,i|],

|Σ[k

′]

bi,j(A′<,i ∪ Bi,1)| < min

m2 1024ℓ2

![image 588](<2021-conlon-subset-sums-completeness-colorings_images/imageFile588.png>)

,

bi,j 4

![image 589](<2021-conlon-subset-sums-completeness-colorings_images/imageFile589.png>)

. (21)

Note that the size of the set A′<,i ∪ Bi,1, considered as a subset of Zbi,j, is at least 7|A

′|

![image 590](<2021-conlon-subset-sums-completeness-colorings_images/imageFile590.png>)

8ℓ > 2mℓ and at most |A′|

![image 591](<2021-conlon-subset-sums-completeness-colorings_images/imageFile591.png>)

![image 592](<2021-conlon-subset-sums-completeness-colorings_images/imageFile592.png>)

ℓ < mℓ , since all elements of A′

![image 593](<2021-conlon-subset-sums-completeness-colorings_images/imageFile593.png>)

<,i are smaller than bi,j and, hence, are distinct modulo bi,j. But then, since 2mℓ > 80(log bi,j)2, Lemma 6.2 with b = bi,j and A = A′<,i ∪Bi,1 implies that if (21) holds, there must be some d ∈ [2,8ℓn/m] such that all but at most 64(log n)2 +8d elements of A′<,i ∪Bi,1 are divisible by d.

![image 594](<2021-conlon-subset-sums-completeness-colorings_images/imageFile594.png>)

Since A′ is nice, for each d ∈ [2,8ℓn/m], at least 512ℓ(log n)2 + 64ℓd elements of A′ are not divisible

by d. By the pigeonhole principle, we obtain that, for each d ∈ [2,8ℓn/m], either A′> or A′< contains at least 256ℓ(log n)2 + 32ℓd elements not divisible by d.

Note that A′<,i is distributed as a uniformly random subset of A′< of size |A′<|/ℓ and Bi,1 is distributed as a uniformly random subset of A′> of size |A′>|/(2ℓ). Consider the event E(i) that, for some d ∈ [2,8ℓn/m], A′<,i ∪ Bi,1 contains at most 64(log n)2 + 8d elements which are not divisible by d. By the argument of Lemma 5.4 and a union bound over all d ≤ 8ℓn/m ≤ n, E(i) happens with probability at most nexp(−256ℓ(log n)2/(16ℓ)) < 1/n. Thus, by a union bound over all i ∈ [ℓ], for suﬃciently large n, the probability of the event i∈[ℓ] E(i) is at most 1/4.

By our earlier observations, (21) cannot hold under the complement of the event i∈[ℓ] E(i), so, provided

- m ≥ C√n for suﬃciently large C,


![image 595](<2021-conlon-subset-sums-completeness-colorings_images/imageFile595.png>)

|Σ[k

′]

bi,j(A′<,i ∪ Bi,1)| ≥ min

m2 1024ℓ2

![image 596](<2021-conlon-subset-sums-completeness-colorings_images/imageFile596.png>)

,

bi,j 4

![image 597](<2021-conlon-subset-sums-completeness-colorings_images/imageFile597.png>)

=

bi,j 4

![image 598](<2021-conlon-subset-sums-completeness-colorings_images/imageFile598.png>)

holds for all i ∈ [ℓ] and all j ∈ [|A′>,i|/2 + 1,|A′>,i|] with probability at least 3/4.

![image 599](<2021-conlon-subset-sums-completeness-colorings_images/imageFile599.png>)

![image 600](<2021-conlon-subset-sums-completeness-colorings_images/imageFile600.png>)

![image 601](<2021-conlon-subset-sums-completeness-colorings_images/imageFile601.png>)

![image 602](<2021-conlon-subset-sums-completeness-colorings_images/imageFile602.png>)

- Proof of Claim 2. Since A′ is nice, for each dyadic interval Ij in [n], either A′ is disjoint from Ij or A′ intersects Ij in at least 64ℓ(log n) elements. Note that there exists j0 such that the dyadic intervals Ij which intersect A′ have at least 64ℓ(log n) common elements with A′> for j > j0, |Ij0∩A′>| < 64ℓ(log n) and Ij∩A′> = ∅ for j < j0. As in the proof of Lemma 5.4, Chernoﬀ’s inequality for hypergeometric distributions implies that the probability |A′>,i ∩ Ij| > 2|A′> ∩ Ij|/ℓ is at most exp(−|A′> ∩ Ij|/(3ℓ)) ≤ exp(−2log n). Similarly, the probability that |Bi,2∩Ij| < |A′>∩Ij|/(4ℓ) is at most exp(−|A′>∩Ij|/(32ℓ)) ≤ exp(−2log n).


Thus, by a union bound, with probability at least 3/4, for each i ∈ [ℓ] and j > j0,

1

4ℓ|A′> ∩ Ij| (22) and

|Bi,2 ∩ Ij| ≥

![image 603](<2021-conlon-subset-sums-completeness-colorings_images/imageFile603.png>)

2 ℓ|A′> ∩ Ij|. (23)

|A′>,i ∩ Ij| ≤

![image 604](<2021-conlon-subset-sums-completeness-colorings_images/imageFile604.png>)

Assume now that (22) and (23) hold for all i ∈ [ℓ] and j > j0. Note that since k′ = 2560ℓn/m + 1 and

- m ≥ C√n, we have |A′>| > 2ℓk′ + 64ℓ(log n). Let X be the set consisting of the largest 2ℓk′ elements of A′>, which is the same as the set of the largest 2ℓk′ elements of A′. Observe that there is j1 > j0 such that, for all j > j1, X ⊇ A′> ∩ Ij and, for all j < j1, X ∩ Ij = ∅. Since, for each j ≥ j1 > j0 and i ∈ [ℓ], |Bi,2 ∩Ij| ≥ 41ℓ|A′> ∩ Ij| ≥ 41ℓ|X ∩Ij|, we have that Bi,2 contains a subset with 4 1ℓ|X ∩ Ij| elements in Ij


![image 605](<2021-conlon-subset-sums-completeness-colorings_images/imageFile605.png>)

![image 606](<2021-conlon-subset-sums-completeness-colorings_images/imageFile606.png>)

![image 607](<2021-conlon-subset-sums-completeness-colorings_images/imageFile607.png>)

![image 608](<2021-conlon-subset-sums-completeness-colorings_images/imageFile608.png>)

1 4ℓ|X ∩ Ij| < k′. Indeed, let t be the number of indices j ≥ j1

for each j ≥ j1. We next show that j≥j

![image 609](<2021-conlon-subset-sums-completeness-colorings_images/imageFile609.png>)

1

|X ∩Ij| = |X| = 2ℓk′ > 256ℓ and, for each j > j1 for which X ∩Ij is non-empty, |X ∩ Ij| = |A′> ∩ Ij| ≥ 64ℓ(log n). Thus,

such that X ∩Ij = ∅. Note that j≥j

1

t ≤ 1 + |X| 64ℓ(log n)

<

![image 610](<2021-conlon-subset-sums-completeness-colorings_images/imageFile610.png>)

k′ 16

. (24)

![image 611](<2021-conlon-subset-sums-completeness-colorings_images/imageFile611.png>)

Therefore,

k′ 16

k′ 2

1 4ℓ|X ∩ Ij| <

1 4ℓ|X ∩ Ij| ≤ t +

< k′.

+

![image 612](<2021-conlon-subset-sums-completeness-colorings_images/imageFile612.png>)

![image 613](<2021-conlon-subset-sums-completeness-colorings_images/imageFile613.png>)

![image 614](<2021-conlon-subset-sums-completeness-colorings_images/imageFile614.png>)

![image 615](<2021-conlon-subset-sums-completeness-colorings_images/imageFile615.png>)

j≥j1

j≥j1

Since Bi,2 contains a subset of size less than k′ with at least 4 1ℓ|X ∩ Ij| elements in Ij for each j ≥ j1 and M(i) is the sum of the k′ largest elements of Bi,2, one has

![image 616](<2021-conlon-subset-sums-completeness-colorings_images/imageFile616.png>)

M(i) ≥

j≥j1

1 4ℓ|X ∩ Ij| =

M 8ℓ

1 8ℓ j≥j

2j−1 ·

- 1
- 2j · |X ∩ Ij| ≥


.

![image 617](<2021-conlon-subset-sums-completeness-colorings_images/imageFile617.png>)

![image 618](<2021-conlon-subset-sums-completeness-colorings_images/imageFile618.png>)

![image 619](<2021-conlon-subset-sums-completeness-colorings_images/imageFile619.png>)

We also have |A′>,i ∩ Ij| ≤ 2ℓ|A′> ∩ Ij| = 2ℓ|X ∩ Ij| for all j > j1. Moreover,

![image 620](<2021-conlon-subset-sums-completeness-colorings_images/imageFile620.png>)

![image 621](<2021-conlon-subset-sums-completeness-colorings_images/imageFile621.png>)

j≥j1

2 ℓ|X ∩ Ij| ≥

![image 622](<2021-conlon-subset-sums-completeness-colorings_images/imageFile622.png>)

j≥j1

k′ 16

2 ℓ|X ∩ Ij| − t ≥ 4k′ −

![image 623](<2021-conlon-subset-sums-completeness-colorings_images/imageFile623.png>)

![image 624](<2021-conlon-subset-sums-completeness-colorings_images/imageFile624.png>)

> 2k′,

where we used the bound (24). Thus, there exists a set of size at least 2k′ containing 2ℓ|X ∩ Ij| elements in Ij for each j ≥ j1 such that the elements of this set dominate the 2k′ largest elements of A′>,i. Hence,

![image 625](<2021-conlon-subset-sums-completeness-colorings_images/imageFile625.png>)

2j ·

![image 626](<2021-conlon-subset-sums-completeness-colorings_images/imageFile626.png>)

M(i) ≤

j≥j1

2 ℓ|X ∩ Ij| ≤

4M ℓ

,

![image 627](<2021-conlon-subset-sums-completeness-colorings_images/imageFile627.png>)

![image 628](<2021-conlon-subset-sums-completeness-colorings_images/imageFile628.png>)

completing the proof of Claim 2. Both Sárközy [35] and Szemerédi and Vu [41] also state results which apply to

![image 629](<2021-conlon-subset-sums-completeness-colorings_images/imageFile629.png>)

![image 630](<2021-conlon-subset-sums-completeness-colorings_images/imageFile630.png>)

![image 631](<2021-conlon-subset-sums-completeness-colorings_images/imageFile631.png>)

![image 632](<2021-conlon-subset-sums-completeness-colorings_images/imageFile632.png>)

Σ(h)(A) =

s : S ⊆ A,|S| = h ,

s∈S

the set of subset sums formed by adding exactly h distinct elements from A. By a small modiﬁcation of our proof, we can also derive the following variant of Theorem 6.1 that applies in this context.

Theorem 6.4. There exists an absolute constant C > 0 such that the following holds. For any subset A of [n] of size m ≥ C√n, there exists d ≥ 1 and r ∈ [0,d−1] such that, for A′ = {(x−r)/d : x ∈ A,d|(x−r)} and k ≥ Cn/m, Σ(k)(A′) contains an interval of length at least n. Furthermore,

![image 633](<2021-conlon-subset-sums-completeness-colorings_images/imageFile633.png>)

|A| − |A′| ≤ C((log n)3 + n/m).

That is, if A ⊂ [n] has size m ≥ C√n and k ≥ Cn/m, then Σ(k)(A) contains an arithmetic progression of length at least n. Since we do not need this variant and the proof is rather similar to that of Theorem 6.1, we omit the details.

![image 634](<2021-conlon-subset-sums-completeness-colorings_images/imageFile634.png>)

Instead, we conclude the section by proving Corollary 1.10, that there is a constant C such that H(n) and h(n) are both at most C√n, where we recall that H(n) is the largest integer for which there are two subsets of [n] of size H(n) whose sets of subset sums have no non-zero common element and h(n) is the size of the largest non-averaging subset of [n].

![image 635](<2021-conlon-subset-sums-completeness-colorings_images/imageFile635.png>)

Proof of Corollary 1.10. For the bound on H(n), we need to show that for any two subsets S1,S2 ⊂ [n], each of size m ≥ C√n, there are non-empty subsets S1′ ⊂ S1 and S2′ ⊂ S2 such that s

2∈S2′ s2. To this end, order the elements of S1 ∪ S2 in increasing order and let M be the median. Without loss of generality, we may assume that the smallest m/2 elements from S1 are each at most M and the largest m/2 elements from S2 are each at least M. Let R1 ⊂ S1 consist of the smallest m/2 elements from S1 and R2 ⊂ S2 consist of the largest m/2 elements of S2.

![image 636](<2021-conlon-subset-sums-completeness-colorings_images/imageFile636.png>)

1∈S1′ s1 = s

Applying Theorem 6.1 to R1, we see that, provided C is suﬃciently large, Σ[k](R1) with k = 252n/m contains a homogeneous arithmetic progression P of common diﬀerence d ≤ 4M/m and length at least

- 2n whose minimum element is at most kM. Note now, by the pigeonhole principle, that any d element sequence contains a subsequence (consisting of consecutive terms) whose sum is divisible by d. We may therefore partition R2 greedily into subsets T1 ∪ ··· ∪ Ts, each of size at most d, such that for each i < s the sum of the elements in Ti is a multiple of d. Note that the sum of the elements in any Ti is at most dn, while the sum of all the elements in R2 \ Ts is at least (m/2 − d)M ≥ kM. It therefore follows that,


for some j, the sum ji=1 t∈T

t, which is a sum of elements from S2, lies in the homogeneous arithmetic progression P.

i

For the bound on h(n), we apply Straus’ inequality h(n) ≤ 2H(n)+2 (see [39]), whose proof we include for completeness. Indeed, suppose that we have a subset of [n] of size p = 2H(n) + 3, say {a1,a2,... ,ap} with a1 < a2 < ··· < ap. Writing q = H(n) + 2, we see that aq is the median element and the sets {aq − ai : 1 ≤ i < q} and {aj − aq : q < j ≤ p} are both subsets of [n] of size H(n) + 1. Therefore, by the deﬁnition of H(n), there must be sets I ⊂ [q−1] and J ⊂ [q+1,p] such that i∈I(aq−ai) = j∈J(aj−aq). Rearranging, we see that aq = |I|+1|J| i∈I∪J ai, so the set is not non-averaging.

![image 637](<2021-conlon-subset-sums-completeness-colorings_images/imageFile637.png>)

![image 638](<2021-conlon-subset-sums-completeness-colorings_images/imageFile638.png>)

![image 639](<2021-conlon-subset-sums-completeness-colorings_images/imageFile639.png>)

![image 640](<2021-conlon-subset-sums-completeness-colorings_images/imageFile640.png>)

![image 641](<2021-conlon-subset-sums-completeness-colorings_images/imageFile641.png>)

# 7 Subsets avoiding a given subset sum

Recall that g(n,m) is the maximum size of a subset of [n] with no subset sum equal to m. Using the results of Section 6, we now prove Theorem 1.7, giving the precise value of g(n,m). Theorem 1.7 states

that there is a constant C such that if m ∈ Cn(log n), 12(logn2n)2 , then

![image 642](<2021-conlon-subset-sums-completeness-colorings_images/imageFile642.png>)

g(n,m) = s(n,m) :=

n snd(m)

![image 643](<2021-conlon-subset-sums-completeness-colorings_images/imageFile643.png>)

+ snd(m) − 2,

where snd(m) is the smallest positive integer which is not a divisor of m. Moreover, if m ∈ 12(log n2n)2, n+12 , then g(n,m) = max s(n,m),(1 + o(1))√2m .

![image 644](<2021-conlon-subset-sums-completeness-colorings_images/imageFile644.png>)

![image 645](<2021-conlon-subset-sums-completeness-colorings_images/imageFile645.png>)

Proof of Theorem 1.7. We consider the cases m ≤ 12(logn2n)2 and m > 12(logn2n)2 separately.

![image 646](<2021-conlon-subset-sums-completeness-colorings_images/imageFile646.png>)

![image 647](<2021-conlon-subset-sums-completeness-colorings_images/imageFile647.png>)

- Case 1. Cn(log n) ≤ m ≤ 12(logn2n)2 for C suﬃciently large. Let A ⊆ [n] be such that m ∈/ Σ(A). Assume that |A| ≥ s(n,m)+1. We claim that snd(m) ≤ 1.01log m


![image 648](<2021-conlon-subset-sums-completeness-colorings_images/imageFile648.png>)

for m suﬃciently large. Indeed, if snd(m) > 1.01log m, then m ≥ lcm(1,2,... ,1.01log m). It is easy to see that lcm(1,2,... ,1.01log m) = exp x≤1.01 logm Λ(x) , where Λ is the von Mangoldt function given by Λ(x) = log p if x = pk is a prime power and Λ(x) = 0 otherwise. But, by the prime number theorem, x≤1.01 logm Λ(x) ≥ 1.005log m for m suﬃciently large, so that m ≥ lcm(1,2,... ,1.01log m) ≥ exp(1.005log m), a contradiction. Thus, snd(m) ≤ 1.01log m ≤ 2.02log n and, in particular, |A| ≥

n 2.02 logn.

![image 649](<2021-conlon-subset-sums-completeness-colorings_images/imageFile649.png>)

Let A∗ be a random subset of A where each element is chosen independently with probability 1/10. By Hoeﬀding’s inequality, |A|/9 ≥ |A∗| ≥ |A|/11 with high probability. Suppose that 2 ≤ d ≤ n is such that there are at least (log n)3 elements in A which are not divisible by d. Again by Hoeﬀding’s inequality, the probability that the number of elements in A which are not divisible by d is more than 20 times larger than the number of elements in A∗ which are not divisible by d is at most exp(−(log n)3/800). Thus, by the union bound, the probability that there exists d ∈ [2,n] such that there are at least (log n)3 elements in A which are not divisible by d and the number of elements in A which are not divisible by d is at least 20 times larger than the number of elements in A∗ which are not divisible by d is at most nexp(−(log n)3/800) < 1/4. Denote this latter event by E and assume from here on that A∗ has been chosen so that |A|/9 ≥ |A∗| ≥ |A|/11 and E does not hold.

By Theorem 6.1, there exists d such that, for A′ = {x/d : x ∈ A∗,d|x}, we have |A′| ≥ |A∗| − 230(log n)3 − 2|A30∗n| and Σ[k](A′) contains an interval I of length at least n for k = 250n/h, where h = |A∗|. Note that |A′| ≥ |A∗| − 230(log n)3 − 2|A30∗n| ≥ |A∗| − 240(log n)3, as |A∗| ≥ |11A| ≥ 22.22 logn n. Since E does not hold, there are at most 250(log n)3 elements in A which are not divisible by d.

![image 650](<2021-conlon-subset-sums-completeness-colorings_images/imageFile650.png>)

![image 651](<2021-conlon-subset-sums-completeness-colorings_images/imageFile651.png>)

![image 652](<2021-conlon-subset-sums-completeness-colorings_images/imageFile652.png>)

![image 653](<2021-conlon-subset-sums-completeness-colorings_images/imageFile653.png>)

Let A′′ = {x/d : x ∈ A \ A∗,d|x}. Since |A∗| ≤ |A|/9 and there are at most 250(log n)3 elements in A which are not divisible by d, the size of A′′ is at least |A|−|A∗|−250(log n)3 ≥ 8|A|/9−250(log n)3 ≥ 0.87|A|. Note that the smallest element of I is at most nk/d ≤ 250nh · nd and each element in A′′ is at most n/d ≤ n. Therefore, by Lemma 2.1, Σ[k+|A′′|](A′ ∪ A′′) contains the interval [250nh · nd, x∈A′′ x). We have

![image 654](<2021-conlon-subset-sums-completeness-colorings_images/imageFile654.png>)

![image 655](<2021-conlon-subset-sums-completeness-colorings_images/imageFile655.png>)

![image 656](<2021-conlon-subset-sums-completeness-colorings_images/imageFile656.png>)

![image 657](<2021-conlon-subset-sums-completeness-colorings_images/imageFile657.png>)

and

|A|2 2.7 ≥

n2 12(log n)2

|A′′|2 2 ≥

x ≥

![image 658](<2021-conlon-subset-sums-completeness-colorings_images/imageFile658.png>)

![image 659](<2021-conlon-subset-sums-completeness-colorings_images/imageFile659.png>)

![image 660](<2021-conlon-subset-sums-completeness-colorings_images/imageFile660.png>)

x∈A′′

n h · n ≤ 30n(log n).

![image 661](<2021-conlon-subset-sums-completeness-colorings_images/imageFile661.png>)

Hence, Σ(A) contains all multiples z of d with 260n(log n) ≤ z ≤ 12(logn2dn)2. In particular, if m ∈/ Σ(A), then d ∤ m. Thus, d ≥ snd(m). Recall that at most 250(log n)3 elements of A are not divisible by d.

![image 662](<2021-conlon-subset-sums-completeness-colorings_images/imageFile662.png>)

Therefore, if d ≥ snd(m) + 1, then

n d ≤ 250(log n)3 +

n snd(m) + 1

n snd(m) −

n 4snd(m)2

|A| ≤ 250(log n)3 +

<

< s(n,m),

![image 663](<2021-conlon-subset-sums-completeness-colorings_images/imageFile663.png>)

![image 664](<2021-conlon-subset-sums-completeness-colorings_images/imageFile664.png>)

![image 665](<2021-conlon-subset-sums-completeness-colorings_images/imageFile665.png>)

![image 666](<2021-conlon-subset-sums-completeness-colorings_images/imageFile666.png>)

a contradiction. Thus, d = snd(m).

Since |A| ≥ snd n(m) +snd(m)−1 and at most snd n(m) elements in A are divisible by d, there exist at least d − 1 elements in A which are not divisible by d. Let A¯ be a set of d − 1 such elements. Note that A¯ is disjoint from {dx : x ∈ A′ ∪A′′}. By Lemma 5.8, Σd(A¯) contains a non-zero subgroup d′Zd of Zd. Since d = snd(m), d′|m for any d′|d and d′ = d. Thus, there exists a subset of A¯ whose sum y is congruent to

![image 667](<2021-conlon-subset-sums-completeness-colorings_images/imageFile667.png>)

![image 668](<2021-conlon-subset-sums-completeness-colorings_images/imageFile668.png>)

- m modulo d. Furthermore, y is at most dn since |A¯| = d − 1 and all elements of A¯ are at most n. Noting that d ≤ 4log n, we have m − y ≥ Cn(log n) − nd ≥ 260n(log n) for suﬃciently large C. We also have


m−y ≤ m ≤ 12(logn2n)2. Hence, m−y ∈ Σ({dx : x ∈ A′ ∪A′′}), so m ∈ Σ({dx : x ∈ A′ ∪A′′}∪A¯). Thus, if |A| ≥ s(n,m) + 1, then m ∈ Σ(A). Hence, g(n,m) ≤ s(n,m). Since we already noted in the introduction

![image 669](<2021-conlon-subset-sums-completeness-colorings_images/imageFile669.png>)

that g(n,m) ≥ s(n,m), this completes the proof in this case.

- Case 2. 12(logn2n)2 ≤ m ≤ n+12 . Let A ⊆ [n] be such that m ∈/ Σ(A). Assume that


![image 670](<2021-conlon-subset-sums-completeness-colorings_images/imageFile670.png>)

√

2m(1 + 250(log n)2/n1/3) .

![image 671](<2021-conlon-subset-sums-completeness-colorings_images/imageFile671.png>)

|A| ≥ 1 + max s(n,m),

- Let A∗ be a random subset of A where each element is chosen independently with probability n−1/3. By Hoeﬀding’s inequality, 0.9|A|/n1/3 ≤ |A∗| ≤ 1.1|A|/n1/3 with high probability. As in the case above, we can again deﬁne an event E, in this case that there exists d ∈ [2,n] such that there are at least n1/3(log n)2 elements in A which are not divisible by d and the number of elements in A which are not divisible by d is at least 2n1/3 times larger than the number of elements in A∗ which are not divisible by d, and show that it happens with probability at most 1/4. We now ﬁx A∗ with 0.9|A|/n1/3 ≤ |A∗| ≤ 1.1|A|/n1/3 such that E does not hold.


By Theorem 6.1, there exists d such that, for A′ = {x/d : x ∈ A∗,d|x}, we have |A′| ≥ |A∗| − 230(log n)3− 2|A30∗n| and Σ(A′) contains an interval I of length at least n. Note that |A| > s(n,m) ≥ 2.02 logn n, so |A∗| ≥ 0n.91|/A3| ≥ 0.log4n2n/3 and |A′| ≥ |A∗| − 230(log n)3 − 2|A30∗n| ≥ |A∗| − 240n1/3(log n). Since E does not hold, there are at most 241n2/3(log n) elements of A which are not divisible by d.

![image 672](<2021-conlon-subset-sums-completeness-colorings_images/imageFile672.png>)

![image 673](<2021-conlon-subset-sums-completeness-colorings_images/imageFile673.png>)

![image 674](<2021-conlon-subset-sums-completeness-colorings_images/imageFile674.png>)

![image 675](<2021-conlon-subset-sums-completeness-colorings_images/imageFile675.png>)

![image 676](<2021-conlon-subset-sums-completeness-colorings_images/imageFile676.png>)

Since |A| ≥ s(n,m) + 1, we must again have d ≤ snd(m). If d = snd(m), then, as above, we can ﬁnd at most d − 1 elements of A which are not divisible by d and whose sum is congruent to m modulo d. If d < snd(m), then d|m. In either case, there is a (possibly empty) sum y of at most d − 1 elements of A not divisible by d such that d|(m − y). Therefore, to show that m ∈ Σ(A), it suﬃces to show that (m − y)/d ∈ Σ({x/d : x ∈ A,d|x}).

Note that Σ(A′) contains an interval I where the largest element of I is at most x∈A′ x ≤ 1.1n5/3/d and each element in {x/d : x ∈ A\A∗,d|x} is at most n/d. By Lemma 2.1, Σ({x/d : x ∈ A,d|x}) contains the interval [1.1n5/3/d, z∈A\A∗,d|z z/d]. The number of elements in A \ A∗ which are divisible by d is at least |A| − |A∗| − 241n2/3(log n) ≥ |A| − 1.1|A|/n1/3 − 241n2/3(log n) ≥ |A|(1 − 242n−1/3(log n)2) > √2m.

![image 677](<2021-conlon-subset-sums-completeness-colorings_images/imageFile677.png>)

Hence,

√2m⌉

![image 678](<2021-conlon-subset-sums-completeness-colorings_images/imageFile678.png>)

⌈

z/d ≥

i ≥ m.

i=1

z∈A\A∗,d|z

Thus, Σ({x/d : x ∈ A,d|x}) contains (m − y)/d, since (m − y)/d ≥ (m − dn)/d > 1.1n5/3/d and (m − y)/d < m.

Hence,

√

2m(1 + 250(log n)2/n1/3) . Since g(n,m) ≥ s(n,m) and g(n,m) ≥ ⌊

![image 679](<2021-conlon-subset-sums-completeness-colorings_images/imageFile679.png>)

g(n,m) ≤ max s(n,m),

√2m⌋ as the interval [⌊

√2m⌋ − 1] does not have a subset sum which equals m, we have

![image 680](<2021-conlon-subset-sums-completeness-colorings_images/imageFile680.png>)

![image 681](<2021-conlon-subset-sums-completeness-colorings_images/imageFile681.png>)

g(n,m) = max s(n,m),

√

2m(1 + O((log n)2/n1/3)) ,

![image 682](<2021-conlon-subset-sums-completeness-colorings_images/imageFile682.png>)

completing the proof.

![image 683](<2021-conlon-subset-sums-completeness-colorings_images/imageFile683.png>)

![image 684](<2021-conlon-subset-sums-completeness-colorings_images/imageFile684.png>)

![image 685](<2021-conlon-subset-sums-completeness-colorings_images/imageFile685.png>)

![image 686](<2021-conlon-subset-sums-completeness-colorings_images/imageFile686.png>)

# References

- [1] N. Alon, Subset sums, J. Number Theory 27 (1987), 196–205.
- [2] N. Alon and P. Erdős, Sure monochromatic subset sums, Acta Arith. 74 (1996), 269–272.
- [3] N. Alon and G. Freiman, On sums of subsets of a set of integers, Combinatorica 8 (1988), 297–306.
- [4] R. Balasubramanian and P. P. Pandey, On a theorem of Deshouillers and Freiman, European J. Combin. 70 (2018), 284–296.
- [5] V. Bergelson and A. Leibman, Polynomial extensions of van der Waerden’s and Szemerédi’s theorems, J. Amer. Math. Soc. 9 (1996), 725–753.
- [6] B. J. Birch, Note on a problem of Erdős, Proc. Cambridge Philos. Soc. 55 (1959), 370–373.
- [7] A. P. Bosznay, On the lower estimation of non-averaging sets, Acta Math. Hungar. 53 (1989), 155–157.
- [8] S. A. Burr and P. Erdős, Completeness properties of perturbed sequences, J. Number Theory 13

(1981), 446–455.

- [9] S. A. Burr and P. Erdős, A Ramsey-type property in additive number theory, Glasgow Math. J. 27

(1985), 5–10.

- [10] S. A. Burr, P. Erdős, R. L. Graham and W. Li, Complete sequences of sets of integer powers, Acta Arith. 77 (1996), 133–138.
- [11] J. W. S. Cassels, On the representation of integers as sums of distinct summands taken from a ﬁxed set, Acta Sci. Math. (Szeged) 21 (1960), 111–124.
- [12] T. Cochrane, M. Ostergaard and C. Spencer, Cauchy–Davenport theorem for abelian groups and diagonal congruences, Proc. Amer. Math. Soc. 147 (2019), 3339–3345.


- [13] J. M. Deshouillers and G. Freiman, A step beyond Kneser’s theorem for abelian ﬁnite groups, Proc. London Math. Soc. 86 (2003), 1–28.
- [14] P. Erdős, On the representation of large integers as sums of distinct summands taken from a ﬁxed set, Acta. Arith. 7 (1962), 345–354.
- [15] P. Erdős, Many old and on some new problems of mine in number theory, Congr. Numer. 30 (1981), 3–27.
- [16] P. Erdős, Miscellaneous problems in number theory, Congr. Numer. 34 (1982), 25–45.
- [17] P. Erdős, Some new problems and results in number theory, in Number theory (Mysore, 1981), 50–74, Lecture Notes in Math., 938, Springer, Berlin-New York, 1982.
- [18] P. Erdős, Some problems and results on combinatorial number theory, in Graph theory and its applications: East and West (Jinan, 1986), 132–145, Ann. New York Acad. Sci., 576, New York Acad. Sci., New York, 1989.
- [19] P. Erdős, Some of my favourite problems in number theory, combinatorics, and geometry, Resenhas 2 (1995), 165–186.
- [20] P. Erdős, Some of my recent problems in combinatorial number theory, geometry and combinatorics, in Graph theory, combinatorics, and algorithms, Vol. 1, 2 (Kalamazoo, MI, 1992), 335–349, WileyIntersci. Publ., Wiley, New York, 1995.
- [21] P. Erdős and R. L. Graham, Old and new problems and results in combinatorial number theory, Monographies de L’Enseignement Mathématique, 28, Université de Genève, L’Enseignement Mathématique, Geneva, 1980.
- [22] P. Erdős and A. Sárközy, On a problem of Straus, in Disorder in Physical Systems, 55–66, Oxford Univ. Press, New York, 1990.
- [23] P. Erdős and E. G. Straus, Nonaveraging sets II, in Combinatorial theory and its applications, II (Proc. Colloq., Balatonfüred, 1969), 405–411, North-Holland, Amsterdam, 1970.
- [24] J. Folkman, On the representation of integers as sums of distinct terms from a ﬁxed sequence, Canadian J. Math. 18 (1966), 643–655.
- [25] G. A. Freiman, New analytical results in subset-sum problem, Discrete Math. 114 (1993), 205–218.
- [26] R. L. Graham, Complete sequences of polynomial values, Duke Math. J. 31 (1964), 275–285.
- [27] D. S. Gunderson and V. Rödl, Extremal problems for aﬃne cubes of integers, Combin. Probab. Comput. 7 (1998), 65–79.
- [28] H. A. Helfgott, The ternary Goldbach problem, to appear in Ann. of Math. Stud.
- [29] W. Hoeﬀding, Probability inequalities for sums of bounded random variables, J. Amer. Statist. Assoc. 58 (1963), 13–30.


- [30] V. Lev, Consecutive integers in high-multiplicity sumsets, Acta Math. Hungar. 129 (2010), 245–253.
- [31] E. Lipkin, On representation of rth powers by subset sums, Acta Arith. 52 (1989), 353–365.
- [32] H. L. Montgomery and R. C. Vaughan, Multiplicative Number Theory I: Classical Theory, Cambridge Studies in Advanced Mathematics, 97, Cambridge University Press, Cambridge, 2007.
- [33] K. F. Roth, On certain sets of integers, J. London Math. Soc. 28 (1953), 104–109.
- [34] K. F. Roth and G. Szekeres, Some asymptotic formulae in the theory of partitions, Quart. J. Math. 5 (1954), 241–259.
- [35] A. Sárközy, Finite addition theorems II, J. Number Theory 48 (1994), 197–218.
- [36] A. Sárközy, On ﬁnite addition theorems, Astérisque 258 (1999), 109–127.
- [37] J. Spencer, Suresums, Combinatorica 1 (1981), 203–208.
- [38] R. Sprague, Über Zerlegungen in n-te Potenzen mit lauter verschiedenen Grundzahlen, Math. Z. 51

(1948), 466–468.

- [39] E. G. Straus, Nonaveraging sets, in Combinatorics (Proc. Sympos. Pure Math., Vol. XIX, Univ. California, Los Angeles, Calif., 1968), 215–222, Amer. Math. Soc., Providence, R.I., 1971.
- [40] E. Szemerédi and V. H. Vu, Finite and inﬁnite arithmetic progressions in sumsets, Ann. of Math. 163

(2006), 1–35.

- [41] E. Szemerédi and V. H. Vu, Long arithmetic progressions in sumsets: Thresholds and bounds, J. Amer. Math. Soc. 19 (2006), 119–169.
- [42] L. Tran, V. H. Vu and P. M. Wood, On a conjecture of Alon, J. Number Theory 129 (2009), 2801– 2807.
- [43] V. H. Vu, Some new results on subset sums, J. Number Theory 124 (2007), 229–233.


# A Supplementary results for Section 4

## A.1 The growth rate of F

In Section 4, we consider a sequence of positive integers F = (fn)n≥1 which satisﬁes fn = i≤ǫn fi for all

- n ≥ n0. Here we establish the asymptotic for F claimed in the introduction.


Claim A.1. Let F = (fn)n≥1 be a sequence of positive integers which satisﬁes fn = i≤ǫn fi for all

- n ≥ n0. Then fn = exp 2 log(1 1 /ǫ) + o(1) (log n)2 .


![image 687](<2021-conlon-subset-sums-completeness-colorings_images/imageFile687.png>)

Proof. We ﬁrst show by induction that there is a constant C for which fn ≤ exp 2 log(1 1 /ǫ)((log n)2 + C) for all positive integers n, which would imply the upper bound in the claim. We can choose C suﬃciently

![image 688](<2021-conlon-subset-sums-completeness-colorings_images/imageFile688.png>)

2+C

large so that this holds for all n ≤ max(n0,10/ǫ). Let m > max(n0,10/ǫ). If fn ≤ exp (logn)

2 log(1/ǫ) for all

![image 689](<2021-conlon-subset-sums-completeness-colorings_images/imageFile689.png>)

- n ≤ m − 1, then


1 2log(1/ǫ)

((log(ǫm))2 + C)

fi ≤ ǫm · exp

fm =

![image 690](<2021-conlon-subset-sums-completeness-colorings_images/imageFile690.png>)

i≤ǫm

1 2log(1/ǫ)

((log m − log(1/ǫ))2 + C + 2log(1/ǫ)log(ǫm))

= exp

![image 691](<2021-conlon-subset-sums-completeness-colorings_images/imageFile691.png>)

1 2log(1/ǫ)

((log m)2 + C) ,

≤ exp

![image 692](<2021-conlon-subset-sums-completeness-colorings_images/imageFile692.png>)

completing the induction proof of the desired upper bound on fn.

We now turn to proving the desired lower bound on fn in the claim. Let C′ = 100log(1/ǫ). Let g˜(x) = exp (logx)

2−C′ log xlog log x

2 log(1/ǫ) . Note that there is x0 > 0 depending only on ǫ such that (log x)2 − C′ log xlog log x is increasing for all x ≥ x0. Let m(ǫ) be the least positive integer such that, for all m ≥ m(ǫ),

![image 693](<2021-conlon-subset-sums-completeness-colorings_images/imageFile693.png>)

ǫg˜(m) ≤ g˜(m − 1/ǫ) − g˜(x0/ǫ). It is easy to verify that such m(ǫ) exists. Let g(x) = exp (logx)

2−C′ log xlog log x−C

2 log(1/ǫ) , where C is a suﬃciently large constant to be chosen later. We next show by induction that, for an appropriate choice of C, fn ≥ g(n) for all n ≥ 2. We choose C suﬃciently large that the above claim holds for all n ≤ max(n0,x0,m(ǫ)). Let m ≥ max(n0,x0,m(ǫ)). If fn ≥ g(n) for all n ≤ m − 1, then

![image 694](<2021-conlon-subset-sums-completeness-colorings_images/imageFile694.png>)

fi ≥

fm =

g(i)

i≤ǫm

i≤ǫm

ǫm−1

≥

g(x)dx =

x0

m−1/ǫ

ǫg(ǫy)dy,

x0/ǫ

where in the last step we used the change of variable y = x/ǫ. Note now that

2log y − C′ − C′ log log y 2y log(1/ǫ) ≤ exp

1 2log(1/ǫ)

g′(y) = exp

((log y)2 − C′ log y log log y − C) ·

![image 695](<2021-conlon-subset-sums-completeness-colorings_images/imageFile695.png>)

![image 696](<2021-conlon-subset-sums-completeness-colorings_images/imageFile696.png>)

1 2log(1/ǫ)

(log y)2 − C′ log y log log y − C − 2log(1/ǫ)log y + 2log(1/ǫ)log(log y/log(1/ǫ)) .

![image 697](<2021-conlon-subset-sums-completeness-colorings_images/imageFile697.png>)

Thus,

g′(y)/g(ǫy) ≤ exp

1 2log(1/ǫ)

(log y)2 − C′ log y log log y − C − 2log(1/ǫ)log y + 2log(1/ǫ)log(log y/log(1/ǫ))

![image 698](<2021-conlon-subset-sums-completeness-colorings_images/imageFile698.png>)

1

2log(1/ǫ) −(log(ǫy))2 + C′ log(ǫy)log log(ǫy) + C ≤ exp

· exp

![image 699](<2021-conlon-subset-sums-completeness-colorings_images/imageFile699.png>)

1 2log(1/ǫ)

2log(1/ǫ)log(log y/log(1/ǫ)) + C′ log(ǫ)log log y ≤ exp(−C′(log log y)/4) ≤ ǫ2,

![image 700](<2021-conlon-subset-sums-completeness-colorings_images/imageFile700.png>)

where in the last inequality we used the fact that C′ = 100log(1/ǫ). Then

fm ≥

m−1/ǫ

ǫg(ǫy)dy ≥

x0/ǫ

m−1/ǫ

x0/ǫ

g′(y) ǫ

g(m − 1/ǫ) − g(x0/ǫ) ǫ ≥ g(m),

dy ≥

![image 701](<2021-conlon-subset-sums-completeness-colorings_images/imageFile701.png>)

![image 702](<2021-conlon-subset-sums-completeness-colorings_images/imageFile702.png>)

where in the last inequality we used the deﬁnition of m(ǫ) and the fact that m ≥ m(ǫ). This completes the induction.

![image 703](<2021-conlon-subset-sums-completeness-colorings_images/imageFile703.png>)

![image 704](<2021-conlon-subset-sums-completeness-colorings_images/imageFile704.png>)

![image 705](<2021-conlon-subset-sums-completeness-colorings_images/imageFile705.png>)

![image 706](<2021-conlon-subset-sums-completeness-colorings_images/imageFile706.png>)

## A.2 Proof of Lemma 4.4

In this subsection, we give the proof of Lemma 4.4, which is a key component in the proof of Theorem 4.3. First, we recall the setting and the statement of the lemma. Let ǫ0 > 0 be a suﬃciently small constant.

- Let B = (bn)n≥1 be an ǫ-friendly sequence. For j suﬃciently large, we choose aj to be a uniform random integer in [bj,bj+1) which has no prime factor at most (max(1/ǫ,1/ǫ0))4000 and let A = (aj)j≥1. For small j, we choose aj to be an arbitrary integer in [bj,bj+1). We let h(i) be the smallest integer for which bh(i) ≥ 2i and Ai = A ∩ [bh(i),bh(i+1)−1).


- Lemma 4.4. There exist positive constants ǫ0, C1 and C2 such that the following holds. For i suﬃciently large, with positive probability, the set Ai has the property that, for any subset A′i ⊂ Ai with |A′i| ≥ (min(ǫ,ǫ0)/4)|Ai|, A′i contains a subset A′′i with |A′′i | ≤ C1i such that Σ(A′′i ) contains every integer in the interval [y,2y], where y = C22ii.


The proof of this lemma has been consigned to an appendix because of its similarity to the proof of Lemma 2.8. Indeed, the diﬀerence between the two proofs consists mainly of minor modiﬁcations to account for the non-uniformity in the distribution of the elements of Ai. However, for completeness, we give the proof in full, beginning with the following lemma, which is the analogue of Lemma 3.1 in this context.

- Lemma A.2. For a suﬃciently large positive constant C0, the following holds. Assume that ǫ > 0 is suﬃciently small. Let i be suﬃciently large and let m be an integer in [2i,2i+1) with no prime factor at


most ǫ−4000. If S is a uniformly chosen random subsequence of Ai of size C0i, then |Σm(S)| < 2i−2 with probability less than ǫ1000C0i.

Proof. Let w = ǫ−4000. Denote by X the set of integers [bh(i),bh(i+1)−1) with no prime divisor at most w. For each j ∈ [h(i),h(i + 1) − 1), let Xj be the set of integers in [bj,bj+1) with no prime divisor at most w. Let t = h(i + 1) − h(i) − 1, which is the number of intervals [bj,bj+1) in [bh(i),bh(i+1)−1). Note that for each interval I of integers of suﬃcient length, the number of elements in the interval which are coprime to all the primes at most w is (τ + o(1))|I|, where τ = φ(W)/W with W being the product of all primes at most w. Since B is a friendly sequence, we have bj+1 −bj ≤ (bj′+1 −bj′)/c for all j ∈ [h(i)−1,h(i+1)−1] and j′ ∈ [h(i),h(i + 1) − 2]. Thus,

2i ≤ bh(i+1) − bh(i)−1 ≤ (1 + 2/(ct))(bh(i+1)−1 − bh(i)).

Since t tends to inﬁnity as i tends to inﬁnity, we have that bh(i+1)−1 − bh(i) ≥ 872i for suﬃciently large i. Hence, for large i, we have that

![image 707](<2021-conlon-subset-sums-completeness-colorings_images/imageFile707.png>)

2iτ 2

. (25)

|X| ≥

![image 708](<2021-conlon-subset-sums-completeness-colorings_images/imageFile708.png>)

Again by properties of friendly sequences, the length of the intervals [bj,bj+1) for j ∈ [h(i),h(i+1)−1) are within a factor 1/c of each other and the minimum length of an interval [bj,bj+1) with j ∈ [h(i),h(i+1)−1) tends to inﬁnity as i tends to inﬁnity. We thus obtain that all |Xj| with j ∈ [h(i),h(i + 1) − 1) are within a factor 2/c of each other for i suﬃciently large. Hence,

|Xj| ≥

c|X| 2t

. (26)

![image 709](<2021-conlon-subset-sums-completeness-colorings_images/imageFile709.png>)

Let D be the distribution of a random integer in [bh(i),bh(i+1)−1), where the probability that an element a ∈ Xj is chosen is |X1

j|t. Observe that the random sequence S is a sequence of C0i random integers with distribution D, subject to the condition that no two elements come from the same interval [bj,bj+1).

![image 710](<2021-conlon-subset-sums-completeness-colorings_images/imageFile710.png>)

Let q = C0i. Let S = (s1,s2,... ,sq). Let Sj = (s1,s2,... ,sj) denote the sequence consisting of the ﬁrst j elements of S. Let δ = 1/w. Call j ∈ [2,q] bad if

- • |Σm(Sj)| ≤ 23|Σm(Sj−1)| and |Σm(Sj−1)| ≤ 2wi or

![image 711](<2021-conlon-subset-sums-completeness-colorings_images/imageFile711.png>)

![image 712](<2021-conlon-subset-sums-completeness-colorings_images/imageFile712.png>)

- • |Σm(Sj)| ≤ (1 + δ)|Σm(Sj−1)| and 2wi < |Σm(Sj−1)| < 2i−2.


![image 713](<2021-conlon-subset-sums-completeness-colorings_images/imageFile713.png>)

The following two claims will allow us to complete the proof of the lemma.

- Claim 1. The probability that j is bad conditioned on the choice of Sj−1 is at most p := cwτ16 .

![image 714](<2021-conlon-subset-sums-completeness-colorings_images/imageFile714.png>)

- Claim 2. If |Σm(S)| < 2i−2, then all but fewer than 2i integers in [2,q] are bad.


Assuming Claim 1, for any B ⊂ [2,q], the probability that all elements in B are bad is at most p|B|. By Merten’s third theorem, we have τ = (e−γ + o(1))/log w ≥ 1/(2log w) for suﬃciently small ǫ, so

32log w cw

. (27)

p ≤

![image 715](<2021-conlon-subset-sums-completeness-colorings_images/imageFile715.png>)

From Claim 2, if |Σm(S)| < 2i−2, then there is a set B of q − 2i integers i ∈ [2,q] which are bad. Taking a union bound over all such choices of B, the probability that |Σm(S)| < 2i−2 is at most

q q − 2i

p|B| =

q 2i

p|B| < (eC0)2i

32log w cw

![image 716](<2021-conlon-subset-sums-completeness-colorings_images/imageFile716.png>)

C0i−2i

< ǫ1000C0i,

where in the ﬁrst inequality we used (27) and in the second inequality we assume a suﬃciently large choice of C0 and note that w = ǫ−4000 with ǫ suﬃciently small.

![image 717](<2021-conlon-subset-sums-completeness-colorings_images/imageFile717.png>)

![image 718](<2021-conlon-subset-sums-completeness-colorings_images/imageFile718.png>)

![image 719](<2021-conlon-subset-sums-completeness-colorings_images/imageFile719.png>)

![image 720](<2021-conlon-subset-sums-completeness-colorings_images/imageFile720.png>)

To complete the proof, it remains to verify Claims 1 and 2.

- Proof of Claim 1. Fix Sj−1 = (s1,... ,sj−1). Conditioned on this choice of Sj−1, we bound the probability that j is bad. Let T be the set of k such that [bk,bk+1) contains at least one of s1,... ,sj−1. Observe that conditioned on s1,... ,sj−1, the distribution of sj is supported on k∈[h(i),h(i+1)−1)\T Xk and, for xk ∈ Xk with k ∈ [h(i),h(i + 1) − 1) \ T, the conditional probability that sj is equal to xk is


where we used (26).

2 |Xk|t ≤

4 c|X|

1 |Xk|(t − |T|) ≤

,

![image 721](<2021-conlon-subset-sums-completeness-colorings_images/imageFile721.png>)

![image 722](<2021-conlon-subset-sums-completeness-colorings_images/imageFile722.png>)

![image 723](<2021-conlon-subset-sums-completeness-colorings_images/imageFile723.png>)

If |Σm(Sj−1)| ≥ 2i−2, then j cannot be bad (so the event that j is bad has probability zero). We may therefore restrict attention to the two cases |Σm(Sj−1)| ≤ 2i/w and 2i/w < |Σm(Sj−1)| < 2i−2.

For the ﬁrst case, note, by Lemma 2.6, that the number of s with |Σm(Sj−1 ∪ {s})| ≤ 23|Σm(Sj−1)| is at most |Σm(Sj−1)|

![image 724](<2021-conlon-subset-sums-completeness-colorings_images/imageFile724.png>)

2

|Σm(Sj−1)|/2 = 2|Σm(Sj−1)|. Therefore, if |Σm(Sj−1)| ≤ 2i/w, the probability that j is bad conditioned on Sj−1 is at most

![image 725](<2021-conlon-subset-sums-completeness-colorings_images/imageFile725.png>)

16 cwτ

4 c|X|

≤

2|Σm(Sj−1)| ·

= p,

![image 726](<2021-conlon-subset-sums-completeness-colorings_images/imageFile726.png>)

![image 727](<2021-conlon-subset-sums-completeness-colorings_images/imageFile727.png>)

where in the inequality we used (25).

Suppose now that 2i/w < |Σm(Sj−1)| < 2i−2. For a positive integer D, let GD be the set of s such that |Σm(Sj−1 ∪{s})| ≤ |Σm(Sj−1)|+D. Let d = ⌊δ|Σm(Sj−1)|⌋, so j is bad in this case if and only if sj ∈ Gd. Let k = ⌊21δ⌋, so kd ≤ |Σm(Sj−1)|/2. By Lemma 2.7, kGd ⊆ Gkd, so |kGd| ≤ |Gkd| ≤ 2|Σm(Sj−1)| < 2i−1, where the middle inequality is again by the consequence of Lemma 2.6 noted above.

![image 728](<2021-conlon-subset-sums-completeness-colorings_images/imageFile728.png>)

If |Gd| ≤ mw , then |Gd| ≤ mw ≤ 2iw+1 = 2δ2i. Otherwise, |Gd| > mw . In this case, since m has no prime divisor at most w, no subgroup of Zm has size larger than mw . Thus, Gd cannot be contained in a coset of a non-trivial subgroup. By Lemma 2.3, since |kGd| ≤ 2i−1 < m, we must have |kGd| ≥ (k + 1)|Gd|/2 ≥ |Gd|/(4δ). Hence, |Gd| ≤ 4δ|kGd| ≤ 4δ2i−1 = 2δ2i. Thus, in either case, conditioned on the choice of Sj−1, the probability that j is bad, which is the same as the probability that sj ∈ Gd, is at most

![image 729](<2021-conlon-subset-sums-completeness-colorings_images/imageFile729.png>)

![image 730](<2021-conlon-subset-sums-completeness-colorings_images/imageFile730.png>)

![image 731](<2021-conlon-subset-sums-completeness-colorings_images/imageFile731.png>)

![image 732](<2021-conlon-subset-sums-completeness-colorings_images/imageFile732.png>)

![image 733](<2021-conlon-subset-sums-completeness-colorings_images/imageFile733.png>)

where we again used (25).

4 c|X|

≤

|Gd| ·

![image 734](<2021-conlon-subset-sums-completeness-colorings_images/imageFile734.png>)

16δ cτ

= p,

![image 735](<2021-conlon-subset-sums-completeness-colorings_images/imageFile735.png>)

![image 736](<2021-conlon-subset-sums-completeness-colorings_images/imageFile736.png>)

![image 737](<2021-conlon-subset-sums-completeness-colorings_images/imageFile737.png>)

![image 738](<2021-conlon-subset-sums-completeness-colorings_images/imageFile738.png>)

![image 739](<2021-conlon-subset-sums-completeness-colorings_images/imageFile739.png>)

- Proof of Claim 2. As Sj−1 ⊂ Sj for j ∈ [2,q], Σm(Sj−1) ⊂ Σm(Sj) and, hence, 1 ≤ |Σm(S1)| ≤ ··· ≤ |Σm(Sq)| = |Σm(S)| < 2i−2. Therefore, the number of j which are not bad with |Σm(Sj−1)| ≤ 2i/w and |Σm(Sj)| ≥ 32|Σm(Sj−1)| is at most log3/2 2i = ilog(3log 2/2), as we get a factor of 3/2 for each such


![image 740](<2021-conlon-subset-sums-completeness-colorings_images/imageFile740.png>)

![image 741](<2021-conlon-subset-sums-completeness-colorings_images/imageFile741.png>)

- j. Moreover, since (1 + δ)δ−1 log2 w ≥ 2log2 w = w, the number of elements j which are not bad with


2i−2 > |Σm(Sj−1)| > 2i/w and |Σm(Sj)| ≥ (1 + δ)|Σm(Sj−1)| is at most δ−1 log2 w = w log2 w, as we get a factor of 1 + δ for each such j. Therefore, the number of j ∈ [2,q] which are not bad is at most

ilog(3log 2/2) + w log2 w < 2i for suﬃciently large i. We are now ready to prove Lemma 4.4.

![image 742](<2021-conlon-subset-sums-completeness-colorings_images/imageFile742.png>)

![image 743](<2021-conlon-subset-sums-completeness-colorings_images/imageFile743.png>)

![image 744](<2021-conlon-subset-sums-completeness-colorings_images/imageFile744.png>)

![image 745](<2021-conlon-subset-sums-completeness-colorings_images/imageFile745.png>)

![image 746](<2021-conlon-subset-sums-completeness-colorings_images/imageFile746.png>)

Proof of Lemma 4.4. By replacing ǫ with min(ǫ,ǫ0), we only need to prove Lemma 4.4 for ǫ ≤ ǫ0. Thus, by choosing ǫ0 suﬃciently small, it suﬃces to prove that the following holds for suﬃciently small ǫ. If i is suﬃciently large, then any subset A′i of Ai with |A′i| ≥ (ǫ/4)|Ai| contains a subset A′′i with |A′′i | ≤ C1i such that Σ(A′′i ) contains every integer in the interval [y,2y], where y = C22ii.

For a given C1 and i suﬃciently large, we have that |Ai| ≥ 400ǫ−1C1i. Consider a random partition of Ai into subsets of size 4ǫ−1C1i and consider a uniform random ordering of each subset as a sequence of integers. Let the obtained sequences be Ai,1,... ,Ai,u.

We will show that for an appropriate choice of C1, there exists a positive constant C2 such that, with positive probability, the following event E holds. For all k ≤ u and all subsequences A′i,k of Ai,k of size (ǫ/4)|Ai,k|, Σ(A′i,k) contains the interval [y,2y] for y = C22ii.

Fix k ≤ u and ﬁx a subset I′ of [4ǫ−1C1i] of size C1i. Let A′i,k be the subsequence of Ai,k consisting

of elements with index in I′. Let ℓ be a constant to be chosen later. We partition I′ into a subset I′′ of size 7C1i/8 and ℓ subsets Ik,′′1,... ,Ik,ℓ′′ of equal size such that each subset in the partition consists of consecutive terms from I′. Let A′′i,k be the elements with index in I′′ and, for each j ∈ [ℓ], let Sk,j be the elements with index in Ik,j′′ . Let Jk,j′ be the ﬁrst |Ik,j′′ |/2 elements of Ik,j′′ and let Jk,j′′ be the remaining elements. Let Sk,j′ be the elements with index in Jk,j′ and let Sk,j′′ be the elements with index in Jk,j′′ . Then Sk,j′ has the same distribution as a random subsequence of Ai of length |Sk,j|/2. We choose C1 = 16ℓC0, so that |Sk,j′ | = C0i, where C0 is the constant deﬁned in Lemma A.2. By Lemma A.2 and a union bound, we have that |Σm(Sk,j′ )| ≥ 2i−2 for all m ∈ [2i,2i+1) with no prime factor at most ǫ−4000 with probability at least 1−2iǫ1000C0i > 1−ǫ800C0i, assuming that ǫ is suﬃciently small. Thus, by another union bound, with probability at least 1 − ℓǫ800C0i, |Σm(Sk,j′ )| ≥ 2i−2 for all j ≤ ℓ and all m ∈ Sk,j′′ . By repeated application of Lemma 2.5, we have that

- 1 16

![image 747](<2021-conlon-subset-sums-completeness-colorings_images/imageFile747.png>)

- 2i|A′i,k|/(4ℓ).


|Σ(Sk,j)| = |Σ(Sk,j′ ∪ Sk,j′′ )| ≥ |Sk,j′′ |2i−2 ≥

We also have that Σ(Sk,j) is a subset of the interval [0,2i|A′i,k|/(4ℓ)]. Furthermore, Σ(Sk,j) is not contained in any arithmetic progression with common diﬀerence greater than 1, as otherwise there exists 1 < d ≤ 16

such that all elements of Sk,j are divisible by d, contradicting the fact that elements of Ai do not have prime factors at most ǫ−4000. Thus, choosing ℓ = 33, by Lemma 2.2, we have that Sk,1+...+Sk,ℓ contains an interval of length at least 2i|A′i,k|/(4ℓ). Hence, Σ(A′i,k \A′′i,k) contains an interval [a,b] of length at least 2i|A′i,k|/(4ℓ) > 2i+1. Note that a < b ≤ 2i−2|A′i,k|. By Lemma 2.1, we then have that Σ(A′i,k) contains the interval [a,b + x∈A′′

x] ⊃ [y,2y] for y = 412i|A′i,k| = C412ii. Let C2 = C41.

![image 748](<2021-conlon-subset-sums-completeness-colorings_images/imageFile748.png>)

![image 749](<2021-conlon-subset-sums-completeness-colorings_images/imageFile749.png>)

![image 750](<2021-conlon-subset-sums-completeness-colorings_images/imageFile750.png>)

i,k

By taking a union bound over all possible choices of I′, the probability that there exists a subsequence A′i,k of Ai,k of size (ǫ/4)|Ai,k| such that Σ(A′i,k) does not contain the interval [y,2y] for y = C22ii is at most (ǫ/ |4)Ai,k|A|

i,k| ℓǫ800C0i. By a union bound over all k ≤ u, we then obtain that the event E holds with probability at least

1 − u |Ai,k| (ǫ/4)|Ai,k|

ℓǫ800C0i ≥ 1 − 2i+7(4e/ǫ)C1iǫ800C0i ≥ 1 − ǫ200C0i > 0,

where we used that ǫ is suﬃciently small, C1 = 16ℓC0 with C0 suﬃciently large, ℓ = 33 and u ≤ 2i+1. Assume now that the event E holds. For any subset A′i of Ai such that |A′i| ≥ (ǫ/4)|Ai|, there exists

- k ≤ u such that |A′i ∩ Ai,k| ≥ (ǫ/4)|Ai,k|. Thus, deﬁning A′′i to be an arbitrary subset of A′i ∩ Ai,k of size (ǫ/4)|Ai,k| = C1i, we have that Σ(A′′i ) contains the interval [y,2y] for y = C22ii, as required.


![image 751](<2021-conlon-subset-sums-completeness-colorings_images/imageFile751.png>)

![image 752](<2021-conlon-subset-sums-completeness-colorings_images/imageFile752.png>)

![image 753](<2021-conlon-subset-sums-completeness-colorings_images/imageFile753.png>)

![image 754](<2021-conlon-subset-sums-completeness-colorings_images/imageFile754.png>)

# B Supplementary results for Section 5

## B.1 Number-theoretic estimates

This short section contains the proofs of some number-theoretic estimates which were used in Section 5. We will need the following simple lemma.

- Lemma B.1. One has


m ζ(2)φ(m) ≤

![image 755](<2021-conlon-subset-sums-completeness-colorings_images/imageFile755.png>)

p|m

1 p ≤

1 u ≤

1 +

![image 756](<2021-conlon-subset-sums-completeness-colorings_images/imageFile756.png>)

![image 757](<2021-conlon-subset-sums-completeness-colorings_images/imageFile757.png>)

p|m

u|m

Proof. By considering the squarefree divisors of m, we have

1 p − 1

1 +

![image 758](<2021-conlon-subset-sums-completeness-colorings_images/imageFile758.png>)

m φ(m)

.

=

![image 759](<2021-conlon-subset-sums-completeness-colorings_images/imageFile759.png>)

On the other hand,

Furthermore,

1 u ≥

![image 760](<2021-conlon-subset-sums-completeness-colorings_images/imageFile760.png>)

u|m

p|m

1 p

1 +

![image 761](<2021-conlon-subset-sums-completeness-colorings_images/imageFile761.png>)

.

1 u ≤

![image 762](<2021-conlon-subset-sums-completeness-colorings_images/imageFile762.png>)

p|m

u|m

1 p

1 +

+

![image 763](<2021-conlon-subset-sums-completeness-colorings_images/imageFile763.png>)

1 p2

+ ··· =

![image 764](<2021-conlon-subset-sums-completeness-colorings_images/imageFile764.png>)

p|m

1 p − 1

1 +

![image 765](<2021-conlon-subset-sums-completeness-colorings_images/imageFile765.png>)

.

p|m

1 p

1 +

![image 766](<2021-conlon-subset-sums-completeness-colorings_images/imageFile766.png>)

=

p|m

1 p − 1 ·

1 +

![image 767](<2021-conlon-subset-sums-completeness-colorings_images/imageFile767.png>)

p|m

1 p2

1 −

![image 768](<2021-conlon-subset-sums-completeness-colorings_images/imageFile768.png>)

m φ(m)

=

![image 769](<2021-conlon-subset-sums-completeness-colorings_images/imageFile769.png>)

p|m

1 p2 ≥

m ζ(2)φ(m)

1 −

.

![image 770](<2021-conlon-subset-sums-completeness-colorings_images/imageFile770.png>)

![image 771](<2021-conlon-subset-sums-completeness-colorings_images/imageFile771.png>)

![image 772](<2021-conlon-subset-sums-completeness-colorings_images/imageFile772.png>)

![image 773](<2021-conlon-subset-sums-completeness-colorings_images/imageFile773.png>)

![image 774](<2021-conlon-subset-sums-completeness-colorings_images/imageFile774.png>)

![image 775](<2021-conlon-subset-sums-completeness-colorings_images/imageFile775.png>)

Our ﬁrst aim is to prove Lemma 5.2, which gives upper and lower bounds on the number of integers in an interval with certain number-theoretic properties. The following lemma, of a similar ﬂavor, is a key component in the proof. Recall that W(r) = ri=1 pi, where pi is the ith prime, and τ(r,m) = φ(W(r)m)/(W(r)m) = p|W(r)m(1 − 1/p).

Lemma B.2. Let r, n and m be positive integers such that m ∈ [n, n2 ], r ≤ n and r is suﬃciently large. For any interval I = [x,2x) with x ≥ n1/6, the number of integers in I which are coprime to W(r)m is at most 8τ(r,m)x. If also x ≥ r1.5, then the number of integers in I which are coprime to W(r)m is at least 1 4τ(r,m)x.

![image 776](<2021-conlon-subset-sums-completeness-colorings_images/imageFile776.png>)

Proof. By [32, Theorem 7.11], for each interval I = [x,2x) with x ≥ pr/2, the number of integers in I which are coprime to W(r) is at most (1+o(1))logxp

≤ 2τ(r,1)x, where we used that pr = (1+o(1))r log r and (31). For x < pr/2, the number of integers in I which are coprime to W(r) is 0 < 2τ(r,1)x. If also x ≥ r1.5 > pr, then the number of integers in I which are coprime to W(r) is at least 2 1 − o(1) log xp

![image 777](<2021-conlon-subset-sums-completeness-colorings_images/imageFile777.png>)

r

≥

![image 778](<2021-conlon-subset-sums-completeness-colorings_images/imageFile778.png>)

![image 779](<2021-conlon-subset-sums-completeness-colorings_images/imageFile779.png>)

r

- 1

![image 780](<2021-conlon-subset-sums-completeness-colorings_images/imageFile780.png>)

- 2τ(r,1)x, again using (31). Consider the case r ≥ (log m)/100. Then τ(r,1) ≤ 1/log r ≤ 4τ(r,m) by (31) and (34), so the number


of integers in I which are coprime to W(r)m is at most 8τ(r,m)x. For x ≥ r1.5, we have seen that there are at least 21τ(r,1)x integers in I which are coprime to W(r). For each prime factor p of m that is larger than pr > r, the number of integers in I divisible by p and coprime to W(r) is the same as the number of integers in [x/p,2x/p) coprime to W(r), which is at most 2τ(r,1)x/p. Since there are at most (log m)/(log r) such prime factors, the number of integers in I which are coprime to W(r)m is at least

![image 781](<2021-conlon-subset-sums-completeness-colorings_images/imageFile781.png>)

log m log r ·

2τ(r,1)x r ≥

200rτ(r,1)x r log r > τ(r,m)x/4,

- 1

![image 782](<2021-conlon-subset-sums-completeness-colorings_images/imageFile782.png>)

- 2


- 1

![image 783](<2021-conlon-subset-sums-completeness-colorings_images/imageFile783.png>)

- 2


τ(r,1)x −

τ(r,1)x −

![image 784](<2021-conlon-subset-sums-completeness-colorings_images/imageFile784.png>)

![image 785](<2021-conlon-subset-sums-completeness-colorings_images/imageFile785.png>)

![image 786](<2021-conlon-subset-sums-completeness-colorings_images/imageFile786.png>)

where, in the ﬁrst inequality, we used the assumption r ≥ (log m)/100 and, in the second inequailty, we

used that r is suﬃciently large and τ(r,m) ≤ τ(r,1) by (30).

Next, consider the case r < (log m)/100. By the inclusion-exclusion principle, the number of integers in I = [x,2x) which are coprime to W(r)m is

M

x p1p2 ··· pk

(−1)k

+ O(2M),

x +

![image 787](<2021-conlon-subset-sums-completeness-colorings_images/imageFile787.png>)

p1<p2<···<pk, p1,p2,...,pk|W(r)m

k=1

which is within an additive O(2M) of x p|W(r)m(1−1/p), where M is the number of distinct primes that divide W(r)m. Since M ≤ r + 2(log m)/(log log m) < (log n)/10 and x ≥ n1/6, the number of integers in

I coprime to W(r)m is at least 21τ(r,m)x and at most 2τ(r,m)x.

![image 788](<2021-conlon-subset-sums-completeness-colorings_images/imageFile788.png>)

![image 789](<2021-conlon-subset-sums-completeness-colorings_images/imageFile789.png>)

![image 790](<2021-conlon-subset-sums-completeness-colorings_images/imageFile790.png>)

![image 791](<2021-conlon-subset-sums-completeness-colorings_images/imageFile791.png>)

![image 792](<2021-conlon-subset-sums-completeness-colorings_images/imageFile792.png>)

- Lemma 5.2. Let r, n and m be positive integers such that m ∈ [n, n2 ], r ≤ n and r is suﬃciently large. For any interval I = [x,2x) with x ≥ n1/4, there are at most 8(m/φ(m))τ(r,m)x integers in I of the form qu, where u|m, u ≤ x1/16 and q is coprime to W(r)m. If also x ≥ r2, then there are at least


- 1 8(m/φ(m))τ(r,m)x integers in I of this form.


![image 793](<2021-conlon-subset-sums-completeness-colorings_images/imageFile793.png>)

Proof. Observe that for x ≥ n1/4 and each ﬁxed u|m with u ≤ x1/16, Lemma B.2 implies that the number of integers in I of the form qu where q is coprime to W(r)m, which is the same as the number of integers in [x/u,2x/u) which are coprime to W(r)m, is at most 8τ(r,m)x/u, where we used that x/u ≥ n1/6. If also x ≥ r2, then Lemma B.2 similarly implies that the number of integers in I of the form qu where q is coprime to W(r)m is at least 41τ(r,m)x/u, where we used that x/u ≥ r1.5.

![image 794](<2021-conlon-subset-sums-completeness-colorings_images/imageFile794.png>)

Hence, the number of integers in I of the form qu, where u|m, u ≤ x1/16 and q is coprime to W(r)m, is at least

1 4

x u ≥

τ(r,m)

![image 795](<2021-conlon-subset-sums-completeness-colorings_images/imageFile795.png>)

![image 796](<2021-conlon-subset-sums-completeness-colorings_images/imageFile796.png>)

u|m, u≤x1/16

 x

τ(r,m)  u|m

1 u −

1 4

σ(m) x1/16

![image 797](<2021-conlon-subset-sums-completeness-colorings_images/imageFile797.png>)

![image 798](<2021-conlon-subset-sums-completeness-colorings_images/imageFile798.png>)

![image 799](<2021-conlon-subset-sums-completeness-colorings_images/imageFile799.png>)

1 4

m 2φ(m)

≥

τ(r,m) ·

x

![image 800](<2021-conlon-subset-sums-completeness-colorings_images/imageFile800.png>)

![image 801](<2021-conlon-subset-sums-completeness-colorings_images/imageFile801.png>)

1 8

≥

(m/φ(m))τ(r,m)x,

![image 802](<2021-conlon-subset-sums-completeness-colorings_images/imageFile802.png>)

where σ(m) is the number of positive divisors of m, which is smaller than m1/100 for m suﬃciently large, and we used Lemma B.1 in the second inequality. Similarly, the number of integers in I of the form qu, where u|m, u ≤ x1/16 and q is coprime to W(r)m, is at most

x u ≤ 8(m/φ(m))τ(r,m)x,

8τ(r,m)

![image 803](<2021-conlon-subset-sums-completeness-colorings_images/imageFile803.png>)

u|m, u≤x1/16

where we again used Lemma B.1.

![image 804](<2021-conlon-subset-sums-completeness-colorings_images/imageFile804.png>)

![image 805](<2021-conlon-subset-sums-completeness-colorings_images/imageFile805.png>)

![image 806](<2021-conlon-subset-sums-completeness-colorings_images/imageFile806.png>)

![image 807](<2021-conlon-subset-sums-completeness-colorings_images/imageFile807.png>)

We now prove Lemma 5.9, which gives an upper bound on the number of integers in an arithmetic progression which are coprime to W(r)/gcd(W(r),m). The proof employs the Selberg sieve.

Lemma 5.9. Let r and n be suﬃciently large positive integers and m ∈ [n, n2 ]. Let X be an arithmetic progression of size |X| ≥ r1/16 with common diﬀerence b ≤ n. Then the number of elements of X which

are coprime to W(r)/gcd(W(r),m) is at most

256|X|log log n log r

.

![image 808](<2021-conlon-subset-sums-completeness-colorings_images/imageFile808.png>)

Furthermore, when b = 1, the number of elements of X which are coprime to W(r)/gcd(W(r),m) is at most

256|X|

(1 − 1/p).

p|W(r),p∤m

Proof. First, we prove the lemma in the case where the elements of the arithmetic progression are coprime to b. By the Selberg sieve [32, Theorem 3.8], applied with q = b and P = W(r)/gcd(W(r),bm), which is coprime to b, the number of integers coprime to W(r)/gcd(W(r),bm) contained in any arithmetic progression of length k ≥ r1/16 and common diﬀerence b is at most

p − 1 p ≤ 2k

p − 1 p

2k

.

![image 809](<2021-conlon-subset-sums-completeness-colorings_images/imageFile809.png>)

![image 810](<2021-conlon-subset-sums-completeness-colorings_images/imageFile810.png>)

√k

p|(W(r)/ gcd(W(r),bm)), p≤r1/32

![image 811](<2021-conlon-subset-sums-completeness-colorings_images/imageFile811.png>)

p|(W(r)/ gcd(W(r),bm)), p≤

Since each prime p ≤ r1/32 < r is either a divisor of gcd(W(r),bm) or a divisor of W(r)/gcd(W(r),bm), for r suﬃciently large, we have that



  ·

  ≤



p − 1 p

p − 1 p ≤

p − 1 p

32 log r

,

 p|(W(r)/gcd(W(r),bm)), p≤r1/32

 p|gcd(W(r),bm)

![image 812](<2021-conlon-subset-sums-completeness-colorings_images/imageFile812.png>)

![image 813](<2021-conlon-subset-sums-completeness-colorings_images/imageFile813.png>)

![image 814](<2021-conlon-subset-sums-completeness-colorings_images/imageFile814.png>)

![image 815](<2021-conlon-subset-sums-completeness-colorings_images/imageFile815.png>)

p≤r1/32

where we used Mertens’ third theorem. Since W(r)/gcd(W(r),bm)|W(r)/gcd(W(r),m), the number of integers coprime to W(r)/gcd(W(r),m) contained in any arithmetic progression of length k ≥ r1/16 and common diﬀerence b is at most



  ·

p p − 1

gcd(W(r),bm) φ(gcd(W(r),bm)) ·

64k log r

64k log r

, (28)

=

 p|gcd(W(r),bm)

![image 816](<2021-conlon-subset-sums-completeness-colorings_images/imageFile816.png>)

![image 817](<2021-conlon-subset-sums-completeness-colorings_images/imageFile817.png>)

![image 818](<2021-conlon-subset-sums-completeness-colorings_images/imageFile818.png>)

![image 819](<2021-conlon-subset-sums-completeness-colorings_images/imageFile819.png>)

assuming that the elements of the arithmetic progression are coprime to b.

If the elements of X are not coprime to b, let d be the greatest common divisor of b and the elements of X. Let Y = {x/d : x ∈ X}. Then Y is an arithmetic progression of size |X| and common diﬀerence b/d whose elements are coprime to b/d. Furthermore, the number of elements of X coprime to W(r)/gcd(W(r),m) is at most the number of elements of Y coprime to W(r)/gcd(W(r),m). By (28), the number of elements of Y coprime to W(r)/gcd(W(r),m) is at most

64|Y | log r ≤

gcd(W(r),bm/d) φ(gcd(W(r),bm/d)) ·

![image 820](<2021-conlon-subset-sums-completeness-colorings_images/imageFile820.png>)

![image 821](<2021-conlon-subset-sums-completeness-colorings_images/imageFile821.png>)

where we used that

gcd(W(r),bm/d) φ(gcd(W(r),bm/d))

![image 822](<2021-conlon-subset-sums-completeness-colorings_images/imageFile822.png>)

=

![image 823](<2021-conlon-subset-sums-completeness-colorings_images/imageFile823.png>)

p| gcd(W(r),bm/d)

64|X| log r

gcd(W(r),bm) φ(gcd(W(r),bm)) ·

,

![image 824](<2021-conlon-subset-sums-completeness-colorings_images/imageFile824.png>)

![image 825](<2021-conlon-subset-sums-completeness-colorings_images/imageFile825.png>)

p p − 1 ≤

p p − 1

=

![image 826](<2021-conlon-subset-sums-completeness-colorings_images/imageFile826.png>)

p| gcd(W(r),bm)

gcd(W(r),bm) φ(gcd(W(r),bm))

.

![image 827](<2021-conlon-subset-sums-completeness-colorings_images/imageFile827.png>)

Thus, for any arithmetic progression X with common diﬀerence b, the number of integers coprime to W(r)/gcd(W(r),m) in X is at most

gcd(W(r),bm) φ(gcd(W(r),bm)) ·

![image 828](<2021-conlon-subset-sums-completeness-colorings_images/imageFile828.png>)

64|X| log r

. (29)

![image 829](<2021-conlon-subset-sums-completeness-colorings_images/imageFile829.png>)

The ﬁrst claim in the lemma follows immediately upon noticing that bm ≤ n3, so φ(gcd(gcd(WW((rr)),bm,bm))) <

![image 830](<2021-conlon-subset-sums-completeness-colorings_images/imageFile830.png>)

- 2log log(bm) < 4log log n. The second claim in the lemma follows from (29) by observing that when b = 1,


p − 1 p ·

φ(gcd(W(r),bm)) gcd(W(r),bm) · log r ≥

1 2τ(r,1)

![image 831](<2021-conlon-subset-sums-completeness-colorings_images/imageFile831.png>)

![image 832](<2021-conlon-subset-sums-completeness-colorings_images/imageFile832.png>)

![image 833](<2021-conlon-subset-sums-completeness-colorings_images/imageFile833.png>)

p| gcd(W(r),m)

p − 1 p

1 2

p p − 1

=

![image 834](<2021-conlon-subset-sums-completeness-colorings_images/imageFile834.png>)

![image 835](<2021-conlon-subset-sums-completeness-colorings_images/imageFile835.png>)

![image 836](<2021-conlon-subset-sums-completeness-colorings_images/imageFile836.png>)

p| gcd(W(r),m)

p|W(r)

- 1

![image 837](<2021-conlon-subset-sums-completeness-colorings_images/imageFile837.png>)

- 2 p|W(r),p∤m


(1 − 1/p)−1,

=

where we used (31) in the ﬁrst inequality.

![image 838](<2021-conlon-subset-sums-completeness-colorings_images/imageFile838.png>)

![image 839](<2021-conlon-subset-sums-completeness-colorings_images/imageFile839.png>)

![image 840](<2021-conlon-subset-sums-completeness-colorings_images/imageFile840.png>)

![image 841](<2021-conlon-subset-sums-completeness-colorings_images/imageFile841.png>)

- B.2 Further estimates for Subsection 5.1 In this subsection, we collect several important estimates that are used throughout Subsection 5.1. To


this end, let n be a suﬃciently large positive integer and m ∈ [n, n2 ]. For a positive integer ρ, recall that W(ρ) = ρi=1 pi and τ(ρ,m) = φ(W(ρ)m)/(W(ρ)m) = p|W(ρ)m(1 − 1/p). We deﬁne ρ(n,m) to be the smallest positive integer ρ such that

ρ/τ(ρ,m) ≥ n2/φ(m). Note that ρ/τ(ρ,m) is increasing as a function of ρ and m

m φ(m)

W(ρ) φ(W(ρ)) ≥

1 τ(ρ,m) ≥ max

W(ρ) φ(W(ρ))

. (30)

φ(m) ·

,

![image 842](<2021-conlon-subset-sums-completeness-colorings_images/imageFile842.png>)

![image 843](<2021-conlon-subset-sums-completeness-colorings_images/imageFile843.png>)

![image 844](<2021-conlon-subset-sums-completeness-colorings_images/imageFile844.png>)

![image 845](<2021-conlon-subset-sums-completeness-colorings_images/imageFile845.png>)

![image 846](<2021-conlon-subset-sums-completeness-colorings_images/imageFile846.png>)

For suﬃciently large ρ, we have, by Mertens’ third theorem, that

W(ρ)

1 τ(ρ,1)

φ(W(ρ)) ∈ [1.6log ρ,1.8log ρ]. (31) Thus,

=

![image 847](<2021-conlon-subset-sums-completeness-colorings_images/imageFile847.png>)

![image 848](<2021-conlon-subset-sums-completeness-colorings_images/imageFile848.png>)

φ(m)/m 2log ρ

. (32) Hence, for ρ suﬃciently large with ρ ≤ n,

τ(ρ,m) ≥

![image 849](<2021-conlon-subset-sums-completeness-colorings_images/imageFile849.png>)

1 τ(ρ,m) ≤ 4log ρlog log m ≤ 8log nlog log n. (33)

![image 850](<2021-conlon-subset-sums-completeness-colorings_images/imageFile850.png>)

Furthermore, for ρ ≥ 10log m/log log m, noting that m has at most 2log m/log log m distinct prime factors larger than 10log m/log log m, we have

log log m 10log m

(1 − 1/p)−1 ≤ 1 −

![image 851](<2021-conlon-subset-sums-completeness-colorings_images/imageFile851.png>)

p|m,p>pρ

−2 log m/ log log m

≤ 2,

so

1

τ(ρ,m) ∈ [log ρ,4log ρ]. (34) The next claim gives the order of ρ(n,m) when m ≤ n2/(log n)2.

![image 852](<2021-conlon-subset-sums-completeness-colorings_images/imageFile852.png>)

- Claim B.3. For m ≤ n2/(log n)2,

ρ(n,m) = Θ

n2/φ(m) log(n2/φ(m))

![image 853](<2021-conlon-subset-sums-completeness-colorings_images/imageFile853.png>)

.

Proof. Since m ≤ n2/(log n)2, we have n2/φ(m) > n2/m ≥ (log n)2. Moreover, if ρ is a positive integer such that ρ < 10log m/log log m, then, by (33), we have that

ρ/τ(ρ,m) ≤

10log m log log m · 4log ρlog log m < (log n)2 < n2/φ(m).

![image 854](<2021-conlon-subset-sums-completeness-colorings_images/imageFile854.png>)

Thus, we must have ρ(n,m) ≥ 10log m/log log m. If now ρ is a positive integer such that ρ ≥ 10log m/log log m, we have τ(ρ,m)−1 ∈ [log ρ,4log ρ] by

(34). Therefore, if ρ ≥ 16 n

2/φ(m)

![image 855](<2021-conlon-subset-sums-completeness-colorings_images/imageFile855.png>)

log(n2/φ(m)), then, by monotonicity of ρ  → τ(ρ,mρ ),

![image 856](<2021-conlon-subset-sums-completeness-colorings_images/imageFile856.png>)

ρ τ(ρ,m) ≥

![image 857](<2021-conlon-subset-sums-completeness-colorings_images/imageFile857.png>)

16φn(m2 ) · log 16n

![image 858](<2021-conlon-subset-sums-completeness-colorings_images/imageFile858.png>)

2/φ(m) log(n2/φ(m))

![image 859](<2021-conlon-subset-sums-completeness-colorings_images/imageFile859.png>)

![image 860](<2021-conlon-subset-sums-completeness-colorings_images/imageFile860.png>)

log(n2/φ(m)) ≥ 8

n2 φ(m)

![image 861](<2021-conlon-subset-sums-completeness-colorings_images/imageFile861.png>)

and so ρ(n,m) ≤ 16 n

2/φ(m)

![image 862](<2021-conlon-subset-sums-completeness-colorings_images/imageFile862.png>)

log(n2/φ(m)). On the other hand, if 10log m/log log m ≤ ρ ≤ 161 n

![image 863](<2021-conlon-subset-sums-completeness-colorings_images/imageFile863.png>)

2/φ(m)

![image 864](<2021-conlon-subset-sums-completeness-colorings_images/imageFile864.png>)

log(n2/φ(m)), then

ρ τ(ρ,m) ≤

![image 865](<2021-conlon-subset-sums-completeness-colorings_images/imageFile865.png>)

n2

![image 866](<2021-conlon-subset-sums-completeness-colorings_images/imageFile866.png>)

φ(m) · 4log n

2/φ(m) 16 log(n2/φ(m))

![image 867](<2021-conlon-subset-sums-completeness-colorings_images/imageFile867.png>)

![image 868](<2021-conlon-subset-sums-completeness-colorings_images/imageFile868.png>)

16log(n2/φ(m)) ≤

1 4

![image 869](<2021-conlon-subset-sums-completeness-colorings_images/imageFile869.png>)

n2 φ(m)

![image 870](<2021-conlon-subset-sums-completeness-colorings_images/imageFile870.png>)

and so ρ(n,m) ≥ 161 n

![image 871](<2021-conlon-subset-sums-completeness-colorings_images/imageFile871.png>)

2/φ(m)

![image 872](<2021-conlon-subset-sums-completeness-colorings_images/imageFile872.png>)

log(n2/φ(m)), as required. Recall that ψ(n,m) = m

![image 873](<2021-conlon-subset-sums-completeness-colorings_images/imageFile873.png>)

![image 874](<2021-conlon-subset-sums-completeness-colorings_images/imageFile874.png>)

![image 875](<2021-conlon-subset-sums-completeness-colorings_images/imageFile875.png>)

![image 876](<2021-conlon-subset-sums-completeness-colorings_images/imageFile876.png>)

1/3(m/φ(m))

![image 877](<2021-conlon-subset-sums-completeness-colorings_images/imageFile877.png>)

(logn)1/3(log logn)2/3 and R(n,m) = min (ψ(n,m),ρ(n,m)). Using Claim B.3, it is easy to show that R(n,m) = Θ(ψ(n,m)) when m = O n

3/2(log log n)1/2

![image 878](<2021-conlon-subset-sums-completeness-colorings_images/imageFile878.png>)

(logn)1/2 and R(m,n) = Θ(ρ(n,m)) when m = Ω n

3/2(log log n)1/2

![image 879](<2021-conlon-subset-sums-completeness-colorings_images/imageFile879.png>)

(logn)1/2 .

Recall that in Subsection 5.1, we deﬁne r = cR(n,m) for a suﬃciently small absolute constant c. The next claim establishes the existence of the integer y used in Lemma 5.1.

- Claim B.4. Let n and m ∈ [n, n2 ] be positive integers such that n and ρ(n,m) are suﬃciently large. Let


r = cR(n,m), where c > 0 is suﬃciently small. Then there exists an integer y < n/2 with

m ∈

y2(m/φ(m))τ(r,m) 25r

,

![image 880](<2021-conlon-subset-sums-completeness-colorings_images/imageFile880.png>)

y2(m/φ(m))τ(r,m) 15r

![image 881](<2021-conlon-subset-sums-completeness-colorings_images/imageFile881.png>)

.

Moreover, one may choose y such that

y ≥ max(r2,n3/5) (35) and

y r log r

> n1/4. (36)

64(m/φ(m))τ(r,m)

![image 882](<2021-conlon-subset-sums-completeness-colorings_images/imageFile882.png>)

3/2(log log n)1/2

3/2(log log n)1/2

Proof. We consider the cases n ≤ m ≤ n

(logn)1/2 and n

(logn)1/2 < m ≤ n2 separately.

![image 883](<2021-conlon-subset-sums-completeness-colorings_images/imageFile883.png>)

![image 884](<2021-conlon-subset-sums-completeness-colorings_images/imageFile884.png>)

- Case 1: n ≤ m ≤ n

3/2(log log n)1/2

![image 885](<2021-conlon-subset-sums-completeness-colorings_images/imageFile885.png>)

(logn)1/2 . In this case, we have (logn1n/)32/3 ≤ r ≤ cCm

![image 886](<2021-conlon-subset-sums-completeness-colorings_images/imageFile886.png>)

1/3(m/φ(m))

![image 887](<2021-conlon-subset-sums-completeness-colorings_images/imageFile887.png>)

(logn)1/3(log logn)2/3, where C is some absolute constant independent of all other parameters. Since r ≥ (logn1n/)32/3, by (34), we have 1/τ(r,m) ∈ [log r,4log r]. We also have

![image 888](<2021-conlon-subset-sums-completeness-colorings_images/imageFile888.png>)

![image 889](<2021-conlon-subset-sums-completeness-colorings_images/imageFile889.png>)

mr log r m/φ(m) ≤

![image 890](<2021-conlon-subset-sums-completeness-colorings_images/imageFile890.png>)

![image 891](<2021-conlon-subset-sums-completeness-colorings_images/imageFile891.png>)

cCm4/3 log n (log n)1/3(log log n)2/3 ≤ n

![image 892](<2021-conlon-subset-sums-completeness-colorings_images/imageFile892.png>)

√

![image 893](<2021-conlon-subset-sums-completeness-colorings_images/imageFile893.png>)

cC.

Thus, for suﬃciently small c, there exists an integer y such that y < (m/φ(25mmr))τ(r,m) < n2 and y >

![image 894](<2021-conlon-subset-sums-completeness-colorings_images/imageFile894.png>)

![image 895](<2021-conlon-subset-sums-completeness-colorings_images/imageFile895.png>)

![image 896](<2021-conlon-subset-sums-completeness-colorings_images/imageFile896.png>)

![image 897](<2021-conlon-subset-sums-completeness-colorings_images/imageFile897.png>)

15mr

![image 898](<2021-conlon-subset-sums-completeness-colorings_images/imageFile898.png>)

(m/φ(m))τ(r,m). This integer y then satisﬁes y < n/2 and

m ∈

y2(m/φ(m))τ(r,m) 25r

![image 899](<2021-conlon-subset-sums-completeness-colorings_images/imageFile899.png>)

,

y2(m/φ(m))τ(r,m) 15r

![image 900](<2021-conlon-subset-sums-completeness-colorings_images/imageFile900.png>)

.

Furthermore, we have

r3(m/φ(m)) m(log n) ≤

![image 901](<2021-conlon-subset-sums-completeness-colorings_images/imageFile901.png>)

(cC)3m(m/φ(m))4 m(log n)2(log log n)2

![image 902](<2021-conlon-subset-sums-completeness-colorings_images/imageFile902.png>)

< 1/2. (37)

Since r ≥ (logn1n/)32/3 > n3/10, we also have

![image 903](<2021-conlon-subset-sums-completeness-colorings_images/imageFile903.png>)

y >

![image 904](<2021-conlon-subset-sums-completeness-colorings_images/imageFile904.png>)

15mr log r m/φ(m)

![image 905](<2021-conlon-subset-sums-completeness-colorings_images/imageFile905.png>)

>

![image 906](<2021-conlon-subset-sums-completeness-colorings_images/imageFile906.png>)

mr log n m/φ(m)

![image 907](<2021-conlon-subset-sums-completeness-colorings_images/imageFile907.png>)

> r2 > n3/5,

where we used (37) in the third inequality.

- Case 2: n


3/2(log log n)1/2

(logn)1/2 < m ≤ n2 .

![image 908](<2021-conlon-subset-sums-completeness-colorings_images/imageFile908.png>)

In this case, we have cC−1ρ(n,m) ≤ r ≤ cCρ(n,m), where C is again an absolute constant and we assume that ρ(n,m) is suﬃciently large. By the deﬁnition of ρ(n,m),

![image 909](<2021-conlon-subset-sums-completeness-colorings_images/imageFile909.png>)

mr/τ(r,m) m/φ(m) ≤

![image 910](<2021-conlon-subset-sums-completeness-colorings_images/imageFile910.png>)

![image 911](<2021-conlon-subset-sums-completeness-colorings_images/imageFile911.png>)

2cCmn2/φ(m) m/φ(m) ≤ n

![image 912](<2021-conlon-subset-sums-completeness-colorings_images/imageFile912.png>)

√

![image 913](<2021-conlon-subset-sums-completeness-colorings_images/imageFile913.png>)

2cC.

![image 914](<2021-conlon-subset-sums-completeness-colorings_images/imageFile914.png>)

Thus, for suﬃciently small c, there exists an integer y such that y < (m/φ(25mmr))τ(r,m) < n2 and y >

![image 915](<2021-conlon-subset-sums-completeness-colorings_images/imageFile915.png>)

![image 916](<2021-conlon-subset-sums-completeness-colorings_images/imageFile916.png>)

![image 917](<2021-conlon-subset-sums-completeness-colorings_images/imageFile917.png>)

15mr

(m/φ(m))τ(r,m). This integer y then satisﬁes y < n/2 and

![image 918](<2021-conlon-subset-sums-completeness-colorings_images/imageFile918.png>)

m ∈

y2(m/φ(m))τ(r,m) 25r

,

![image 919](<2021-conlon-subset-sums-completeness-colorings_images/imageFile919.png>)

y2(m/φ(m))τ(r,m) 15r

![image 920](<2021-conlon-subset-sums-completeness-colorings_images/imageFile920.png>)

.

3/2(log log n)1/2

If n

(logn)1/2 < m < n7/4, we have ρ(n,m) ≥ n1/8, so τ(ρ(n,m),m) ≤ 1/log ρ(n,m) ≤ 10/log n by (34). Using this, we obtain

![image 921](<2021-conlon-subset-sums-completeness-colorings_images/imageFile921.png>)

n3 16(log log n)(log n) ≥ 4τ(ρ(n,m),m)2n3.

m2 4(log log m)2 ≥

φ(m)2 ≥

![image 922](<2021-conlon-subset-sums-completeness-colorings_images/imageFile922.png>)

![image 923](<2021-conlon-subset-sums-completeness-colorings_images/imageFile923.png>)

If m ≥ n7/4, we also easily have

τ(ρ(n,m),m)2n3 ≤ n3 ≤

1 4

φ(m)2.

![image 924](<2021-conlon-subset-sums-completeness-colorings_images/imageFile924.png>)

Since τ(ρρ((n,mn,m)),m) ∈ [φn(m2 ), φ2(nm2)] by the deﬁnition of ρ(n,m), we obtain ρ(n,m) ≤

![image 925](<2021-conlon-subset-sums-completeness-colorings_images/imageFile925.png>)

![image 926](<2021-conlon-subset-sums-completeness-colorings_images/imageFile926.png>)

![image 927](<2021-conlon-subset-sums-completeness-colorings_images/imageFile927.png>)

n3/2(log log n)1/2

(logn)1/2 < m < n7/4 and n7/4 ≤ m ≤ n2 . Moreover, since r ≥ cC−1ρ(n,m),

![image 928](<2021-conlon-subset-sums-completeness-colorings_images/imageFile928.png>)

√n in both ranges

![image 929](<2021-conlon-subset-sums-completeness-colorings_images/imageFile929.png>)

1.8log ρ(n,m) 1.6log r

(1 − 1/pi)−1 ≤

τ(ρ(n,m),m) ≤ 25τ(ρ(n,m),m),

τ(r,m) = τ(ρ(n,m),m)

![image 930](<2021-conlon-subset-sums-completeness-colorings_images/imageFile930.png>)

i∈(r,ρ(n,m)],pi∤m

where we used that ρ(n,m) is suﬃciently large. Hence,

y ≥

√

![image 931](<2021-conlon-subset-sums-completeness-colorings_images/imageFile931.png>)

cC−1 25

mr 25(m/φ(m))τ(r,m) ≥

![image 932](<2021-conlon-subset-sums-completeness-colorings_images/imageFile932.png>)

![image 933](<2021-conlon-subset-sums-completeness-colorings_images/imageFile933.png>)

![image 934](<2021-conlon-subset-sums-completeness-colorings_images/imageFile934.png>)

√

![image 935](<2021-conlon-subset-sums-completeness-colorings_images/imageFile935.png>)

![image 936](<2021-conlon-subset-sums-completeness-colorings_images/imageFile936.png>)

cC−1 25 ≥ c2C2ρ(n,m)2 ≥ r2, (38)

n

mρ(n,m) (m/φ(m))τ(ρ(n,m),m) ≥

![image 937](<2021-conlon-subset-sums-completeness-colorings_images/imageFile937.png>)

![image 938](<2021-conlon-subset-sums-completeness-colorings_images/imageFile938.png>)

√n and assumed c is suﬃciently small. Furthermore, from (38), for n suﬃciently large, we have

where we used the deﬁnition of ρ(n,m), the bound ρ(n,m) ≤

![image 939](<2021-conlon-subset-sums-completeness-colorings_images/imageFile939.png>)

√

![image 940](<2021-conlon-subset-sums-completeness-colorings_images/imageFile940.png>)

cC−1 25

n

> n3/5.

y ≥

![image 941](<2021-conlon-subset-sums-completeness-colorings_images/imageFile941.png>)

Thus, in both Case 1 and Case 2, there exists a choice of y < n/2 with

y2(m/φ(m))τ(r,m) 25r

y2(m/φ(m))τ(r,m) 15r such that (35) also holds. Moreover, (36) holds, since

m ∈

,

![image 942](<2021-conlon-subset-sums-completeness-colorings_images/imageFile942.png>)

![image 943](<2021-conlon-subset-sums-completeness-colorings_images/imageFile943.png>)

32y1/2 (log n)2

y r log r ≥

> n1/4,

64(m/φ(m))τ(r,m)

![image 944](<2021-conlon-subset-sums-completeness-colorings_images/imageFile944.png>)

![image 945](<2021-conlon-subset-sums-completeness-colorings_images/imageFile945.png>)

where we used that y ≥ max(r2,n3/5), log r ≤ log n and, by (32), (m/φ(m))τ(r,m) ≥ 2 log1 r ≥ 2 log1 n.

![image 946](<2021-conlon-subset-sums-completeness-colorings_images/imageFile946.png>)

![image 947](<2021-conlon-subset-sums-completeness-colorings_images/imageFile947.png>)

![image 948](<2021-conlon-subset-sums-completeness-colorings_images/imageFile948.png>)

![image 949](<2021-conlon-subset-sums-completeness-colorings_images/imageFile949.png>)

![image 950](<2021-conlon-subset-sums-completeness-colorings_images/imageFile950.png>)

![image 951](<2021-conlon-subset-sums-completeness-colorings_images/imageFile951.png>)

