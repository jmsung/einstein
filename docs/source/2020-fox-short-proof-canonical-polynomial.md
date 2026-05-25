---
type: source
kind: paper
title: A short proof of the canonical polynomial van der Waerden theorem
authors: Jacob Fox, Yuval Wigderson, Yufei Zhao
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2005.04135v1
source_local: ../raw/2020-fox-short-proof-canonical-polynomial.pdf
topic: general-knowledge
cites:
---

arXiv:2005.04135v1[math.CO]8May2020

A SHORT PROOF OF THE CANONICAL POLYNOMIAL VAN DER WAERDEN THEOREM

JACOB FOX, YUVAL WIGDERSON, AND YUFEI ZHAO

Abstract. We present a short new proof of the canonical polynomial van der Waerden theorem, recently established by Gira˜o.

Gira˜o [3] recently proved the following canonical version of the polynomial van der Waerden theorem. Here a set is rainbow if all elements have distinct colors. We write [N] := {1,... ,N}.

- Theorem 1 ([3]). Let p1,... ,pk be distinct polynomials with integer coeﬃcients and pi(0) = 0 for each i. For all suﬃciently large N, every coloring of [N] contains a sequence x+p1(y),... ,x+pk(y) (for some x,y ∈ N) that is monochromatic or rainbow.

Gira˜o’s proof uses a color-focusing argument. Here we give a new short proof of Theorem 1, deducing it from the polynomial Szemere´di’s theorem of Bergelson and Leibman [1].

- Theorem 2 ([1]). Let p1,... ,pk be distinct polynomials with integer coeﬃcients and pi(0) = 0 for each i. Let ε > 0. For all N suﬃciently large, every A ⊂ [N] with |A| ≥ εN contains x + p1(y),... ,x + pk(y) for some x,y ∈ N.

Our proof of Theorem 1 follows the strategy of Erd˝os and Graham [2], who deduced a canonical van der Waerden theorem (i.e., for arithmetic progressions) using Szemere´di’s theorem [6].

We quote the following result, proved by Linnik [5] in his elementary solution of Waring’s problem (see [4, Theorem 19.7.2]). Note the left-hand side below counts the number of solutions f(x1) + ··· + f(xs/2) = f(xs/2+1) + ··· + f(xs) with x1,... ,xs ∈ [n].

- Theorem 3 ([5]). Fix a polynomial f of degree d ≥ 2 with integer coeﬃcients. Let s = 8d−1. Then


1

0

n

e2πiθf(x)

x=1

s

dθ = O(ns−d).

- Lemma 4. Fix a polynomial f of degree d ≥ 2 with integer coeﬃcients. For every A ⊂ Z and


1

s n1−ds ), where s = 8d−1. Proof. We write

n ∈ N, the number of pairs (x,y) ∈ A × [n] with x + f(y) ∈ A is O(|A|1+

![image 1](<2020-fox-short-proof-canonical-polynomial_images/imageFile1.png>)

![image 2](<2020-fox-short-proof-canonical-polynomial_images/imageFile2.png>)

1A(θ) =

e2πiθx and F(θ) =

x∈A

n

e2πiθf(y).

y=1

![image 3](<2020-fox-short-proof-canonical-polynomial_images/imageFile3.png>)

Fox is supported by a Packard Fellowship and by NSF award DMS-1855635. Wigderson is supported by NSF GRFP grant DGE-1656518. Zhao is supported by NSF award DMS-1764176, the MIT Solomon Buchsbaum Fund, and a Sloan Research Fellowship.

Then the number of solutions to z = x + f(y) with x,z ∈ A and y ∈ [n] is

1

| 1A(θ)|2F(θ)dθ ≤

0

1

0

≤ |A|

= |A|

1−1s 1

1 s

![image 4](<2020-fox-short-proof-canonical-polynomial_images/imageFile4.png>)

![image 5](<2020-fox-short-proof-canonical-polynomial_images/imageFile5.png>)

2s s−1

|F(θ)|s dθ

dθ

| 1A(θ)|

[H¨older]

![image 6](<2020-fox-short-proof-canonical-polynomial_images/imageFile6.png>)

0

1−1s

1

![image 7](<2020-fox-short-proof-canonical-polynomial_images/imageFile7.png>)

2 s−1

· O(n1−ds ) [| 1A(θ)| ≤ |A| and Theorem 3]

| 1A(θ)|2 dθ

![image 8](<2020-fox-short-proof-canonical-polynomial_images/imageFile8.png>)

![image 9](<2020-fox-short-proof-canonical-polynomial_images/imageFile9.png>)

0

1−1s

2 s−1

· O(n1−ds ) [Parseval]

![image 10](<2020-fox-short-proof-canonical-polynomial_images/imageFile10.png>)

|A|

![image 11](<2020-fox-short-proof-canonical-polynomial_images/imageFile11.png>)

![image 12](<2020-fox-short-proof-canonical-polynomial_images/imageFile12.png>)

1

s n1−ds ).

= O(|A|1+

![image 13](<2020-fox-short-proof-canonical-polynomial_images/imageFile13.png>)

![image 14](<2020-fox-short-proof-canonical-polynomial_images/imageFile14.png>)

- Lemma 5. Fix a polynomial f of degree d ≥ 1 with integer coeﬃcients. Let A ⊂ Z. Suppose that |A ∩ [x,x + L)| ≤ εL for every L ≥ nd and x. Then the number of pairs (x,y) ∈ A × [n] with x + f(y) ∈ A is O(ε1/s |A|n), where s = 8d−1.


Proof. If d = 1, then for every x ∈ A, the number of y ∈ [n] so that x + f(y) ∈ A is O(εn) by the local density condition on A. Summing over all x ∈ A yields the desired bound O(ε|A|n) on the number of pairs. From now on assume d ≥ 2.

Let m = O(nd) so that |f(y)| ≤ m for all y ∈ [n]. Let Ai = A∩[im,(i+2)m). Then |Ai| = O(εm). Every pair x,x + f(y) ∈ A with y ∈ [n] is contained in some Ai, and, by Lemma 4, the number of pairs contained in each Ai is O(|Ai|1+1sn1−ds ) = O((εm)1s|Ai|n1−ds ) = O(ε1/s|Ai|n). Summing over all integers i yields the lemma (each element of A lies in precisely two diﬀerent Ai’s).

![image 15](<2020-fox-short-proof-canonical-polynomial_images/imageFile15.png>)

![image 16](<2020-fox-short-proof-canonical-polynomial_images/imageFile16.png>)

![image 17](<2020-fox-short-proof-canonical-polynomial_images/imageFile17.png>)

![image 18](<2020-fox-short-proof-canonical-polynomial_images/imageFile18.png>)

Proof of Theorem 1. Choose a suﬃciently small ε > 0 (depending on p1,... ,pk). Consider a coloring of [N] without monochromatic progressions x + p1(y),... ,x + pk(y). By Theorem 2, every color class has density at most ε on every suﬃciently long interval.

Let D = maxi =j deg(pi −pj). Let n be an integer on the order of N1/D so that x+p1(y),... ,x+ pk(y) ∈ [N] only if y ∈ [n]. For each color class A, applying Lemma 5 to f = pi − pj and summing over all i = j, we see that the number of pairs (x,y) ∈ Z × [n] where at least two of

x + p1(y),... ,x + pk(y) lie in A is O(ε1/8D−1|A|n). Summing over all color classes A, we see that the number of non-rainbow progressions x + p1(y),... ,x + pk(y) ∈ [N] is O(ε1/8D−1Nn). Since the total number of sequences x+p1(y),... ,x+pk(y) ∈ [N] is on the order of Nn, some such sequence must be rainbow, as long as ε > 0 is small enough and N is large enough.

References

- [1] V. Bergelson and A. Leibman, Polynomial extensions of van der Waerden’s and Szemer´edi’s theorems, J. Amer. Math. Soc. 9 (1996), 725–753.
- [2] P. Erd˝s and R. L. Graham, Old and new problems and results in combinatorial number theory, vol. 28, Universite´ de Gene`ve, L’Enseignement Mathe´matique, Geneva, 1980.
- [3] A. Gira˜o, A canonical polynomial van der Waerden’s theorem, arXiv:2004.07766.
- [4] L. K. Hua, Introduction to number theory, Springer-Verlag, Berlin-New York, 1982.
- [5] U. V. Linnik, An elementary solution of the problem of Waring by Schnirelman’s method, Rec. Math. [Mat. Sbornik] N.S. 12(54) (1943), 225–230.
- [6] E. Szemere´di, On sets of integers containing no k elements in arithmetic progression, Acta Arith. 27 (1975), 199–245.


Fox, Wigderson: Department of Mathematics, Stanford University, Stanford, CA, USA E-mail address: {jacobfox,yuvalwig}@stanford.edu

Zhao: Department of Mathematics, Massachusetts Institute of Technology, Cambridge, MA, USA E-mail address: yufeiz@mit.edu

