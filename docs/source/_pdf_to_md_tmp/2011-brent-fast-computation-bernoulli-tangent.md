arXiv:1108.0286v3[math.CO]5Sep2011

# Fast Computation of Bernoulli, Tangent and Secant Numbers

Richard P. Brent and David Harvey

Abstract We consider the computation of Bernoulli, Tangent (zag), and Secant (zig or Euler) numbers. In particular, we give asymptotically fast algorithms for computing the ﬁrst n such numbers in O(n2(logn)2+o(1)) bit-operations. We also give very short in-place algorithms for computing the ﬁrst n Tangent or Secant numbers in O(n2) integer operations. These algorithms are extremely simple, and fast for moderate values of n. They are faster and use less space than the algorithms of Atkinson (for Tangent and Secant numbers) and Akiyama and Tanigawa (for Bernoulli numbers).

## 1 Introduction

The Bernoulli numbers are rational numbers Bn deﬁned by the generating function

zn n!

z exp(z)−1

. (1)

Bn

=

![image 1](<2011-brent-fast-computation-bernoulli-tangent_images/imageFile1.png>)

![image 2](<2011-brent-fast-computation-bernoulli-tangent_images/imageFile2.png>)

n≥0

Bernoulli numbers are of interest in number theory and are related to special values of the Riemann zeta function (see §2). They also occur as coefﬁcients in the Euler-Maclaurin formula, so are relevant to high-precision computation of special functions [7, §4.5].

![image 3](<2011-brent-fast-computation-bernoulli-tangent_images/imageFile3.png>)

Richard P. Brent Mathematical Sciences Institute, Australian National University, Canberra, ACT 0200, Australia. e-mail: Tangent@rpbrent.com

David Harvey School of Mathematics and Statistics, University of New South Wales, Sydney, NSW 2052, Australia. e-mail: D.Harvey@unsw.edu.au

1

It is sometimes convenient to consider scaled Bernoulli numbers

B2n (2n)!

, (2)

Cn =

![image 4](<2011-brent-fast-computation-bernoulli-tangent_images/imageFile4.png>)

with generating function

z/2 tanh(z/2)

Cnz2n =

. (3)

![image 5](<2011-brent-fast-computation-bernoulli-tangent_images/imageFile5.png>)

n≥0

The generating functions (1) and (3) only differ by the single term B1z, since the other odd terms vanish.

The Tangent numbers Tn, and Secant numbers Sn, are deﬁned by

Tn

n>0

z2n−1 (2n−1)!

= tanz,

![image 6](<2011-brent-fast-computation-bernoulli-tangent_images/imageFile6.png>)

z2n (2n)!

= secz. (4)

Sn

![image 7](<2011-brent-fast-computation-bernoulli-tangent_images/imageFile7.png>)

n≥0

In this paper, which is based on an a talk given by the ﬁrst author at a workshop held to mark Jonathan Borwein’s sixtieth birthday, we consider some algorithms for computing Bernoulli, Tangent and Secant numbers. For background, combinatorial interpretations, and references, see Abramowitz and Stegun [1, Ch. 23] (where the notation differs from ours, e.g. (−1)nE2n is used for our Sn), and Sloane’s [29] sequences A000367, A000182, A000364.

Let M(n) be the number of bit-operations required for n-bit integer multiplication. The Scho¨nhage-Strassen algorithm [27] gives M(n) = O(nlognloglogn), and Fu¨rer [17] has recently given an improved bound M(n) = O(n(logn)2log∗n). For simplicity we merely assume that M(n) = O(n(logn)1+o(1)), where the o(1) term depends on the precise algorithm used for multiplication. For example, if the Scho¨nhage-Strassen algorithm is used, then the o(1) term can be replaced by logloglogn/loglogn.

In §§2–3 we mention some relevant and generally well-known facts concerning Bernoulli, Tangent and Secant numbers.

Recently, Harvey [20] showed that the single number Bn can be computed in

- O(n2(logn)2+o(1)) bit-operations using a modular algorithm. In this paper we show


that all the Bernoulli numbers B0,...,Bn can be computed with the same complexity bound (and similarly for Secant and Tangent numbers).

In §4 we give a relatively simple algorithm that achieves the slightly weaker bound O(n2(logn)3+o(1)). In §5 we describe the improvementto O(n2(logn)2+o(1)). The idea is similar to that espoused by Steel [31], although we reduce the problem to division rather than multiplication. It is an open question whether the single number B2n can be computed in o(n2) bit-operations.

In §6 we give very short in-place algorithms for computing the ﬁrst n Secant or Tangent numbers using O(n2) integer operations. These algorithms are extremely simple, and fast for moderate values of n (say n ≤ 1000), although asymptotically not as fast as the algorithms given in §§4–5. Bernoulli numbers can easily be deduced from the corresponding Tangent numbers using the relation (14) below.

## 2 Bernoulli Numbers

From the generating function (1) it is easy to see that the Bn are rational numbers, with B2n+1 = 0 if n > 0. The ﬁrst few nonzero Bn are: B0 = 1, B1 = −1/2, B2 = 1/6, B4 = −1/30, B6 = 1/42, B8 = −1/30, B10 = 5/66, B12 = −691/2730, B14 = 7/6.

The denominators of the Bernoulli numbers are given by the Von Staudt – Clausen Theorem [12, 30], which states that

1 p

B′2n := B2n +

![image 8](<2011-brent-fast-computation-bernoulli-tangent_images/imageFile8.png>)

(p−1)|2n

∈ Z.

Here the sum is over all primes p for which p−1 divides 2n.

Since the “correction” B′2n −B2n is easy to compute, it might be convenient in a program to store the integers B′2n instead of the rational numbers B2n or Cn.

Euler found that the Riemann zeta-function for even non-negative integer arguments can be expressed in terms of Bernoulli numbers – the relation is

B2n (2n)!

(−1)n−1

=

![image 9](<2011-brent-fast-computation-bernoulli-tangent_images/imageFile9.png>)

2 (2n) (2 )2n

![image 10](<2011-brent-fast-computation-bernoulli-tangent_images/imageFile10.png>)

Since (2n) = 1+O(4−n) as n → + , we see that

2(2n)! (2 )2n

.

|B2n| ∼

![image 11](<2011-brent-fast-computation-bernoulli-tangent_images/imageFile11.png>)

. (5)

From Stirling’s approximation to (2n)!, the number of bits in the integer part of B2n is 2nlgn+O(n) (we write lg for log2). Thus, it takes (n2logn) space to store

- B1,...,Bn. We can not expect any algorithm to compute B1,...,Bn in fewer than (n2logn) bit-operations.


Another connection between the Bernoulli numbers and the Riemann zetafunction is the identity

Bn+1 n+1

= − (−n) (6)

![image 12](<2011-brent-fast-computation-bernoulli-tangent_images/imageFile12.png>)

for n ∈ Z, n ≥ 1. This follows from (5) and the functional equation for the zetafunction, or directly from a contour integral representation of the zeta-function [33].

From the generating function (1), multiplying both sides by exp(z)−1 and equating coefﬁcients of z, we obtain the recurrence

k

j=0

k+1 j

Bj = 0 for k > 0. (7)

This recurrence has traditionally been used to compute B0,...,B2n with O(n2) arithmetic operations, for example in [22]. However, this is unsatisfactory if ﬂoatingpoint numbers are used, because the recurrence is numerically unstable: the relative

error in the computed B2n is of order 4n if the ﬂoating-point arithmetic has precision , i.e. lg(1/ ) bits.

Let Cn be deﬁned by (2). Then, multiplying each side of (3) by sinh(z/2)/(z/2) and equating coefﬁcients gives the recurrence

k

Cj (2k+1−2j)!4k−j

=

![image 13](<2011-brent-fast-computation-bernoulli-tangent_images/imageFile13.png>)

j=0

1 (2k)! 4k

. (8)

![image 14](<2011-brent-fast-computation-bernoulli-tangent_images/imageFile14.png>)

Using this recurrence to evaluate C0,C1,...,Cn, the relative error in the computed Cn is only O(n2 ), which is satisfactory from a numerical point of view.

Equation (5) can be used in several ways to compute Bernoulli numbers. If we want just one Bernoulli number B2n then (2n) on the right-hand-side of (5) can be evaluated to sufﬁcient accuracy using the Euler product: this is the “zeta-function” algorithm for computing Bernoulli numbers mentioned (with several references to earlier work) by Harvey [20]. On the other hand, if we want several Bernoulli numbers, then we can use the generating function

z tanh( z)

= −2

![image 15](<2011-brent-fast-computation-bernoulli-tangent_images/imageFile15.png>)

(−1)k (2k)z2k , (9)

k=0

computing the coefﬁcients of z2k, k ≤ n, to sufﬁcient accuracy, as mentioned in [3, 9, 10]. This is similar to the fast algorithm that we describe in §4. The similarity can be seen more clearly if we replace z by z in (9), giving

z tanh(z)

= −2

![image 16](<2011-brent-fast-computation-bernoulli-tangent_images/imageFile16.png>)

(2k) 2k z2k , (10)

(−1)k

![image 17](<2011-brent-fast-computation-bernoulli-tangent_images/imageFile17.png>)

k=0

since it is the rational number (2n)/ 2n that we need in order to compute B2n from (5). In fact, it is easy to see that (10) is equivalent to (3).

There is a vast literature on Bernoulli, Tangent and Secant numbers. For example, the bibliography of Dilcher and Slavutskii [15] contains more than 2000 items. Thus, we do not attempt to give a complete list of references to related work. However, we brieﬂy mention the problem of computing irregular primes [8, 11], which are odd primes p such that p divides the class number of the p-th cyclotomic ﬁeld. The algorithms that we present in §§4–5 below are not suitable for this task because they take too much memory. It is much more space-efﬁcient to use a modular algorithm where the computations are performed modulo a single prime (or maybe the product of a small number of primes), as in [8, 11, 14, 20]. Space can also be saved by the technique of “multisectioning”, which is described by Crandall [13, §3.2] and Hare [19].

## 3 Tangent and Secant Numbers

The Tangent numbers Tn (n > 0) (also called Zag numbers) are deﬁned by

Tn

n>0

z2n−1 (2n−1)!

sinz cosz

.

= tanz =

![image 18](<2011-brent-fast-computation-bernoulli-tangent_images/imageFile18.png>)

![image 19](<2011-brent-fast-computation-bernoulli-tangent_images/imageFile19.png>)

Similarly, the Secant numbers Sn (n ≥ 0) (also called Euler or Zig numbers) are deﬁned by

z2n (2n)!

1 cosz

.

= secz =

Sn

![image 20](<2011-brent-fast-computation-bernoulli-tangent_images/imageFile20.png>)

![image 21](<2011-brent-fast-computation-bernoulli-tangent_images/imageFile21.png>)

n≥0

Unlike the Bernoulli numbers, the Tangent and Secant numbersare positive integers. Because tanz and secz have poles at z = /2, we expect Tn to grow roughly like (2n−1)!(2/ )n and Sn like (2n)!(2/ )n. To obtain more precise estimates, let

0(s) = (1−2−s) (s) = 1+3−s+5−s+··· be the odd zeta-function. Then

Tn (2n−1)!

=

![image 22](<2011-brent-fast-computation-bernoulli-tangent_images/imageFile22.png>)

22n+1 0(2n) 2n ∼

22n+1 2n (11)

![image 23](<2011-brent-fast-computation-bernoulli-tangent_images/imageFile23.png>)

![image 24](<2011-brent-fast-computation-bernoulli-tangent_images/imageFile24.png>)

(this can be proved in the same way as Euler’s relation (5) for the Bernoulli numbers). We also have [1, (23.2.22)]

22n+2 (2n+1) 2n+1 ∼

22n+2 2n+1

Sn (2n)!

, (12)

=

![image 25](<2011-brent-fast-computation-bernoulli-tangent_images/imageFile25.png>)

![image 26](<2011-brent-fast-computation-bernoulli-tangent_images/imageFile26.png>)

![image 27](<2011-brent-fast-computation-bernoulli-tangent_images/imageFile27.png>)

where

(s) =

From (5) and (11), we see that

(−1)j(2j+1)−s. (13)

j=0

B2n 2n

Tn = (−1)n−122n(22n −1)

![image 28](<2011-brent-fast-computation-bernoulli-tangent_images/imageFile28.png>)

. (14)

This can also be proved directly, without involving the zeta-function, by using the identity

1 tanz

2 tan(2z)

.

tanz =

−

![image 29](<2011-brent-fast-computation-bernoulli-tangent_images/imageFile29.png>)

![image 30](<2011-brent-fast-computation-bernoulli-tangent_images/imageFile30.png>)

Since Tn ∈ Z, it follows from (14) that the odd primes in the denominator of B2n must divide 22n−1. This is compatible with the Von Staudt–Clausen theorem, since (p−1)|2n implies p|(22n −1) by Fermat’s little theorem.

Tn has about 4n more bits than ⌈B2n⌉, but both have 2nlgn+O(n) bits, so asymptotically there is not much difference between the sizes of Tn and ⌈B2n⌉. Thus, if our

aim is to compute B2n, we do not lose much by ﬁrst computing Tn, and this may be more convenient since Tn ∈ Z, B2n ∈ Q.

## 4 A Fast Algorithm for Bernoulli Numbers

Harvey [20] showed how Bn could be computed exactly, using a modular algorithm and the Chinese remainder theorem, in O(n2(logn)2+o(1)) bit-operations. The same complexity can be obtained using (5) and the Euler product for the zeta-function (see the discussion in Harvey [20, §1]).

In this section we show how to compute all of B0,...,Bn with almost the same complexity bound (only larger by a factor O(logn)). In §5 we give an even faster algorithm, which avoids the O(logn) factor.

Let A(z) = a0 + a1z+ a2z2 + ··· be a power series with coefﬁcients in R, with a0 = 0. Let B(z) = b0 +b1z+··· be the reciprocal power series, so A(z)B(z) = 1. Using the FFT, we can multiply polynomials of degree n− 1 with O(nlogn) real

operations. Using Newton’s method [24, 28], we can compute b0,...,bn−1 with the same complexity O(nlogn), up to a constant factor.

Taking A(z) = (exp(z) − 1)/z and working with N-bit ﬂoating-point numbers,

where N = nlg(n) + O(n), we get B0,...,Bn to sufﬁcient accuracy to deduce the exact (rational) result. (Alternatively, use (3) to avoid computing the terms

with odd subscripts, since these vanish except for B1.) The work involved is O(nlogn) ﬂoating-point operations, each of which can be done with N-bit accuracy in O(n(logn)2+o(1)) bit-operations. Thus, overall we get B0,...,Bn with

- O(n2(logn)3+o(1)) bit-operations. Similarly for Secant and Tangent numbers. We omit a precise speciﬁcation of N and a detailed error analysis of the algorithm, since it is improved in the following section.


## 5 A Faster Algorithm for Tangent and Bernoulli Numbers

To improve the algorithm of §4 for Bernoulli numbers, we use the “Kronecker– Scho¨nhage trick” [7, §1.9]. Instead of working with power series A(z) (or polynomials, which can be regarded as truncated power series), we work with binary numbers A(z) where z is a suitable (negative) power of 2.

The idea is to compute a single real number A which is deﬁned in such a way that the numbers that we want to compute are encoded in the binary representation of A . For example, consider the series

z(1+z) (1−z)3

k2zk =

, |z| < 1.

![image 31](<2011-brent-fast-computation-bernoulli-tangent_images/imageFile31.png>)

k>0

The right-hand side is an easily-computed rational function of z, say A(z). We use decimal rather than binary for expository purposes. With z = 10−3 we easily ﬁnd

1001000 997002999

A(10−3) =

= 0.001004009016025036049064081100 ···

![image 32](<2011-brent-fast-computation-bernoulli-tangent_images/imageFile32.png>)

![image 33](<2011-brent-fast-computation-bernoulli-tangent_images/imageFile33.png>)

![image 34](<2011-brent-fast-computation-bernoulli-tangent_images/imageFile34.png>)

![image 35](<2011-brent-fast-computation-bernoulli-tangent_images/imageFile35.png>)

![image 36](<2011-brent-fast-computation-bernoulli-tangent_images/imageFile36.png>)

![image 37](<2011-brent-fast-computation-bernoulli-tangent_images/imageFile37.png>)

![image 38](<2011-brent-fast-computation-bernoulli-tangent_images/imageFile38.png>)

![image 39](<2011-brent-fast-computation-bernoulli-tangent_images/imageFile39.png>)

![image 40](<2011-brent-fast-computation-bernoulli-tangent_images/imageFile40.png>)

![image 41](<2011-brent-fast-computation-bernoulli-tangent_images/imageFile41.png>)

![image 42](<2011-brent-fast-computation-bernoulli-tangent_images/imageFile42.png>)

Thus, if we are interested in the ﬁnite sequence of squares (12,22,32,...,102), it is sufﬁcient to compute A = A(10−3) correctly rounded to 30 decimal places, and we can then “read off” the squares from the decimal representation of A .

Of course, this example is purely for illustrative purposes, because it is easy to compute the sequence of squares directly. However, we use the same idea to compute Tangent numbers. Suppose we want the ﬁrst n Tangent numbers (T1,T2,...,Tn). The generating function

z2k−1 (2k−1)!

tanz =

Tk

![image 43](<2011-brent-fast-computation-bernoulli-tangent_images/imageFile43.png>)

k≥1

gives us almost what we need, but not quite, because the coefﬁcients are rationals, not integers. Instead, consider

(2n−1)!tanz =

n

Tk′,nz2k−1 +Rn(z), (15)

k=1

where

(2n−1)! (2k−1)!

Tk′,n =

Tk (16) is an integer for 1 ≤ k ≤ n, and

![image 44](<2011-brent-fast-computation-bernoulli-tangent_images/imageFile44.png>)

Tk′,n z2k−1 = (2n−1)!

Tk

Rn(z) =

k=n+1

k=n+1

z2k−1 (2k−1)!

![image 45](<2011-brent-fast-computation-bernoulli-tangent_images/imageFile45.png>)

(17)

is a remainder term which is small if z is sufﬁciently small. Thus, choosing z = 2−p with p sufﬁciently large, the ﬁrst 2np binary places of (2n−1)!tanz deﬁne T1′,n,T2′,n,...,Tn′,n. Once we have computed T1′,n,T2′,n,...,Tn′,n it is easy to deduce T1,T2,...,Tn from

Tk′,n (2n−1)!/(2k−1)!

.

Tk =

![image 46](<2011-brent-fast-computation-bernoulli-tangent_images/imageFile46.png>)

For this idea to work, two conditions must be satisﬁed. First, we need

0 ≤ Tk′,n < 1/z2 = 22p, 1 ≤ k ≤ n, (18)

so we can read off the Tk′,n from the binary representation of (2n−1)!tanz. Since we have a good asymptotic estimate for Tk, it is not hard to choose p sufﬁciently large for this condition to hold.

Second, we need the remainder term Rn(z) to be sufﬁciently small that it does not inﬂuence the estimation of Tn′,n. A sufﬁcient condition is

0 ≤ Rn(z) < z2n−1. (19)

Choosing z sufﬁciently small (i.e. p sufﬁciently large) guarantees that condition (19) holds, since Rn(z) is O(z2n+1) as z → 0 with n ﬁxed.

Lemmas 3 and 4 below give sufﬁcient conditions for (18) and (19) to hold.

- Lemma 1. Tk

![image 47](<2011-brent-fast-computation-bernoulli-tangent_images/imageFile47.png>)

(2k−1)!

≤

2 2(k−1)

![image 48](<2011-brent-fast-computation-bernoulli-tangent_images/imageFile48.png>)

for k ≥ 1.

Proof. From (11),

Tk (2k−1)!

![image 49](<2011-brent-fast-computation-bernoulli-tangent_images/imageFile49.png>)

= 2

2 2k

![image 50](<2011-brent-fast-computation-bernoulli-tangent_images/imageFile50.png>)

0(2k) ≤ 2

2 2k

![image 51](<2011-brent-fast-computation-bernoulli-tangent_images/imageFile51.png>)

0(2) ≤

2 2k 2 4

![image 52](<2011-brent-fast-computation-bernoulli-tangent_images/imageFile52.png>)

![image 53](<2011-brent-fast-computation-bernoulli-tangent_images/imageFile53.png>)

=

2 2(k−1)

![image 54](<2011-brent-fast-computation-bernoulli-tangent_images/imageFile54.png>)

⊓⊔

- Lemma 2. (2n−1)! ≤ n2n−1 for n ≥ 1. Proof.

(2n−1)! = n

n−1

j=1

(n− j)(n+ j) = n

n−1

j=1

(n2 − j2) ≤ n2n−1

with equality iff n = 1. ⊓⊔

- Lemma 3. If k ≥ 1, n ≥ 2, p = ⌈nlg(n)⌉, z = 2−p, and Tk′,n is as in (16), then z ≤ n−n and Tk′,n < 1/z2.

Proof. We have z = 2−p = 2−⌈nlg(n)⌉ ≤ 2−nlg(n) = n−n, which proves the ﬁrst part of the Lemma.

Assume k ≥ 1 and n ≥ 2. From Lemma 1, we have

Tk′,n ≤ (2n−1)!

2 2(k−1)

![image 55](<2011-brent-fast-computation-bernoulli-tangent_images/imageFile55.png>)

≤ (2n−1)!,

and from Lemma 2 it follows that

Tk′,n ≤ n2n−1 < n2n. From the ﬁrst part of the Lemma, n2n ≤ 1/z2, so the second part follows. ⊓⊔

- Lemma 4. If n ≥ 2, p = ⌈nlg(n)⌉, z = 2−p, and Rn(z) is as deﬁned in (17), then 0 < Rn(z) < 0.1z2n−1 .


Proof. Since all the terms in the sum deﬁning Rn(z) are positive, it is immediate that Rn(z) > 0.

Since n ≥ 2, we have p ≥ 2 and z ≤ 1/4. Now, using Lemma 1,

Tk′,nz2k−1

Rn(z) =

k=n+1

2 2(k−1)

z2k−1

≤ (2n−1)!

![image 56](<2011-brent-fast-computation-bernoulli-tangent_images/imageFile56.png>)

k=n+1

2 2n

2z 2

z2n+1 1+

≤ (2n−1)!

+

![image 57](<2011-brent-fast-computation-bernoulli-tangent_images/imageFile57.png>)

![image 58](<2011-brent-fast-computation-bernoulli-tangent_images/imageFile58.png>)

2z 4

+···

![image 59](<2011-brent-fast-computation-bernoulli-tangent_images/imageFile59.png>)

≤ (2n−1)!

2 2n

z2n+1 1−

![image 60](<2011-brent-fast-computation-bernoulli-tangent_images/imageFile60.png>)

2z 2

![image 61](<2011-brent-fast-computation-bernoulli-tangent_images/imageFile61.png>)

.

Since z ≤ 1/4, we have 1/(1−(2z/ )2) < 1.026. Also, from Lemma 2, (2n−1)! ≤ n2n−1. Thus, we have

Rn(z) z2n−1

< 1.026n2n−1

![image 62](<2011-brent-fast-computation-bernoulli-tangent_images/imageFile62.png>)

2 2n

z2.

![image 63](<2011-brent-fast-computation-bernoulli-tangent_images/imageFile63.png>)

Now z2 ≤ n−2n from the ﬁrst part of Lemma 3, so

1.026 n

Rn(z) z2n−1

<

![image 64](<2011-brent-fast-computation-bernoulli-tangent_images/imageFile64.png>)

![image 65](<2011-brent-fast-computation-bernoulli-tangent_images/imageFile65.png>)

2 2n

![image 66](<2011-brent-fast-computation-bernoulli-tangent_images/imageFile66.png>)

. (20)

The right-hand side is a monotonic decreasing function of n, so is bounded above by its value when n = 2, giving Rn(z)/z2n−1 < 0.1. ⊓⊔

A high-level description of the resulting Algorithm FastTangentNumbersis given in Figure 1. The algorithm computes the Tangent numbers T1,T2,...,Tn using the Kronecker-Scho¨nhage trick as described above, and deduces the Bernoulli numbers

- B2,B4,...,B2n from the relation (14).


Input: integer n ≥ 2 Output: Tangent numbers T1,...,Tn and (optional) Bernoulli numbers B2,B4,...,B2n

p ← ⌈nlg(n)⌉ z ← 2−p S ← 0≤k<n(−1)kz2k+1 ×(2n)!/(2k+1)! C ← 0≤k<n(−1)kz2k ×(2n)!/(2k)! V ← ⌊z1−2n ×(2n−1)!×S/C⌉ (here ⌊x⌉ means round x to nearest integer) Extract Tk′,n = Tk(2n−1)!/(2k−1)!, 1 ≤ k ≤ n, from the binary representation of V

Tk ← Tk′,n ×(2k−1)!/(2n−1)!, k = n,n−1,...,1 B2k ← (−1)k−1(k×Tk/22k−1)/(22k −1), k = 1,2,...,n (optional) return T1,T2,...,Tn and (optional) B2,B4,...,B2n

- Fig. 1 Algorithm FastTangentNumbers (also optionally computes Bernoulli numbers)


In order to achieve the best complexity, the algorithm must be implemented carefully using binary arithmetic. The computations of S (an approximation to (2n)!sinz) and C (an approximation to (2n)!cosz) involve computing ratios of factorials such as (2n)!/(2k)!, where 0 ≤ k ≤ n. This can be done in time O(n2(logn)2) by a straightforward algorithm. The N-bit division to compute S/C (an approximation to tanz) can be done in time O(N log(N)loglog(N)) by the Scho¨nhage–Strassen algorithm combined with Newton’s method [7, §4.2.2]. Here it is sufﬁcient to take N = 2np+2 = 2n2lg(n)+O(n). Note that

n

22(n−k)pTk′,n (21)

V =

k=1

is just the ﬁnite sum in (15) scaled by z1−2n (a power of two), and the integers Tk′,n can simply be “read off” from the binary representation of V in n blocks of 2p consecutive bits. The Tk′,n can then be scaled by ratios of factorials in time O(n2(logn)2+o(1)) to give the Tangent numbers T1,T2,...,Tn.

The correctness of the computed Tangent numbers follows from Lemmas 3–4, apart from possible errors introduced by S/C being only an approximation to tan(z).

- Lemma 5 shows that this error is sufﬁciently small.


Lemma 5. Suppose that n ≥ 2, z, S and C as in Algorithm FastTangentNumbers. Then

z1−2n(2n−1)!

S C

−tanz < 0.02. (22)

![image 67](<2011-brent-fast-computation-bernoulli-tangent_images/imageFile67.png>)

Proof. We use the inequality

- A′

![image 68](<2011-brent-fast-computation-bernoulli-tangent_images/imageFile68.png>)

- B′


- A

![image 69](<2011-brent-fast-computation-bernoulli-tangent_images/imageFile69.png>)

- B


−

|A|·|B−B′|+|B|·|A−A′| |B|·|B′|

. (23)

≤

![image 70](<2011-brent-fast-computation-bernoulli-tangent_images/imageFile70.png>)

Take A = sinz, B = cosz, A′ = S/(2n)!, B′ = C/(2n)! in (23). Since n ≥ 2 we have 0 < z ≤ 1/4. Then |A| = |sinz| < z. Also, |B| = |cosz| > 31/32 from the Taylor series cosz = 1 − z2/2 + ···, which has terms of alternating sign and decreasing magnitude. By similar arguments, |B′| ≥ 31/32, |B−B′| < z2n/(2n)!, and

|A−A′| < z2n+1/(2n+1)!. Combining these inequalities and using (23), we obtain

z2n+1 (2n)!

6·32·32 5·31·31

S C

−tanz <

<

![image 71](<2011-brent-fast-computation-bernoulli-tangent_images/imageFile71.png>)

![image 72](<2011-brent-fast-computation-bernoulli-tangent_images/imageFile72.png>)

![image 73](<2011-brent-fast-computation-bernoulli-tangent_images/imageFile73.png>)

1.28z2n+1 (2n)!

.

![image 74](<2011-brent-fast-computation-bernoulli-tangent_images/imageFile74.png>)

Multiplying both sides by z1−2n(2n−1)! and using 1.28z2/(2n) ≤ 0.02, we obtain the inequality (22). This completes the proof of Lemma 5. ⊓⊔

In view of the constant 0.02 in (22) and the constant 0.1 in Lemma 4, the effect of all sources of error in computing z1−2n(2n−1)!tanz is at most 0.12 < 1/2, which is

too small to change the computed integer V, that is to say, the computedV is indeed given by (21).

The computation of the Bernoulli numbers B2,B4,...,B2n from T1,...,Tn, is straightforward (details depending on exactly how rational numbers are to be represented). The entire computation takes time

O(N(logN)1+o(1)) = O(n2(logn)2+o(1)). Thus, we have proved: Theorem 1. The Tangent numbers T1,...,Tn and Bernoulli numbers B2,B4,...,B2n can be computed in O(n2(logn)2+o(1)) bit-operations using O(n2logn) space.

A small modiﬁcation of the above can be used to compute the Secant numbers S0,S1,...,Sn in O(n2(logn)2+o(1)) bit-operations and O(n2logn) space. The bound on Tangent numbers given by Lemma 1 can be replaced by the bound

Sn (2n)!

≤ 2

![image 75](<2011-brent-fast-computation-bernoulli-tangent_images/imageFile75.png>)

2 2n+1

![image 76](<2011-brent-fast-computation-bernoulli-tangent_images/imageFile76.png>)

which follows from (12) since (2n+1) < 1.

We remark that an efﬁcient implementation of Algorithm FastTangentNumbers in a high-level language such as Sage [32] or Magma [5] is nontrivial, because it requires access to the internal binary representation of high-precision integers. Everything can be done using (implicitly scaled) integer arithmetic – there is no need for ﬂoating-point – but for the sake of clarity we did not include the scaling in Figure 1. If ﬂoating-point arithmetic is used, a precision of N bits is sufﬁcient, where N = 2np+2.

Comparing our Algorithm FastTangentNumbers with Harvey’s modular algorithm [20], we see that there is a space-time trade-off: Harvey’s algorithm uses less space (by a factor of order n) to compute a single Bn, but more time (again by a factor of order n) to compute all of B1,...,Bn. Harvey’s algorithm has better locality and is readily parallelisable.

In the following section we give much simpler algorithms which are fast enough for most practical purposes, and are based on three-term recurrence relations.

## 6 Algorithms Based On Three-Term Recurrences

Akiyama and Tanigawa [21] gave an algorithm for computing Bernoulli numbers based on a three-term recurrence. However, it is only useful for exact computations, since it is numerically unstable if applied using ﬂoating-point arithmetic. It is faster to use a stable recurrence for computing Tangent numbers, and then deduce the Bernoulli numbers from (14).

## 6.1 Bernoulli and Tangent numbers

We now give a stable three-term recurrence and corresponding in-place algorithm for computing Tangent numbers. The algorithm is perfectly stable since all operations are on positive integers and there is no cancellation. Also, it involves less arithmetic than the Akiyama-Tanigawa algorithm. This is partly because the operations are on integers rather than rationals, and partly because there are fewer operations since we take advantage of zeros.

Bernoulli numbers can be computed using Algorithm TangentNumbers and the relation (14). The time required for the application of (14) is negligible.

The recurrence (24) that we use was given by Buckholtz and Knuth [23], but they did not give our in-place Algorithm TangentNumbers explicitly. Related recurrences with applications to parallel computation were considered by Hare [19].

Write t = tanx, D = d/dx, so Dt = 1+t2 and D(tn) = ntn−1(1+t2) for n ≥ 1. It is clear that Dnt is a polynomial in t, say Pn(t). Write Pn(t) = j≥0 pn,jt j. Then deg(Pn) = n+1 and, from the formula for D(tn),

pn,j = (j−1)pn−1,j−1+(j+1)pn−1,j+1. (24)

We are interested in Tk = (d/dx)2k−1tanx|x=0 = P2k−1(0) = p2k−1,0, which can be computed from the recurrence (24) in O(k2) operations using the obvious boundary conditions. We save work by noticing that pn,j = 0 if n + j is even. The resulting algorithm is given in Figure 2.

Input: positive integer n Output: Tangent numbers T1,...,Tn

T1 ← 1 for k from 2 to n

Tk ← (k−1)Tk−1 for k from 2 to n

### for j from k to n

Tj ← (j −k)Tj−1 +(j −k+2)Tj return T1,T2,...,Tn.

- Fig. 2 Algorithm TangentNumbers


The ﬁrst for loop initializes Tk = pk−1,k = (k −1)!. The variable Tk is then used to store pk,k−1, pk+1,k−2, ..., p2k−2,1, p2k−1,0 at successive iterations of the second for loop. Thus, when the algorithm terminates, Tk = p2k−1,0, as expected.

The process in the case n = 3 is illustrated in Figure 3, where Tk(m) denotes the value of the variable Tk at successive iterations m = 1,2,...,n. It is instructive to compare a similar Figure for the Akiyama-Tanigawa algorithm in [21].

Algorithm TangentNumbers takes (n2) operations on positive integers. The integers Tn have O(nlogn) bits, other integers have O(logn) bits. Thus, the overall

T1(1) = p0,1 ւ ց

- T1(1) = p1,0 T2(1) = p1,2 ց ւ ց

T2(2) = p2,1 T3(1) = p2,3 ւ ց ւ

- T2(2) = p3,0 T3(2) = p3,2 ց ւ

T3(3) = p4,1 ւ

- T3(3) = p5,0


- Fig. 3 Dataﬂow in Algorithm TangentNumbers for n = 3


complexity is O(n3(logn)1+o(1)) bit-operations, or O(n3logn) word-operations if n ﬁts in a single word.

The algorithm is not optimal, but it is good in practice for moderate values of n, and much simpler than asymptotically faster algorithms such as those described in §§4–5. For example, using a straightforward Magma implementation of Algorithm TangentNumbers, we computed the ﬁrst 1000 Tangent numbers in 1.50 sec on a 2.26 GHz Intel Core 2 Duo. For comparison, it takes 1.92 sec for a single N-bit division computing T in Algorithm FastTangentNumbers (where N = 19931568 corresponds to n = 1000). Thus, we expect the crossover point where Algorithm FastTangentNumbers actually becomes faster to be slightly larger than n = 1000 (but dependent on implementation details).

## 6.2 Secant numbers

A similar algorithm may be used to compute Secant numbers. Let s = secx, t = tanx, and D = d/dx. Then Ds = st, D2s = s(1+2t2), and in general Dns = sQn(t), where Qn(t) is a polynomialof degree n in t. The Secant numbersare given by Sk = Q2k(0). Let Qn(t) = k≥0qn,ktk. From

D(stk) = stk+1 +kstk−1(1+t2) we obtain the three-term recurrence

qn+1,k = kqn,k−1 +(k+1)qn,k+1 for 1 ≤ k ≤ n. (25)

By avoiding the computation of terms qn,k that are known to be zero (n+k odd), and ordering the computation in a manner analogous to that used for Algorithm TangentNumbers, we obtain Algorithm SecantNumbers (see Figure 4), which computes the Secant numbers in place using non-negative integer arithmetic.

Input: positive integer n Output: Secant numbers S0,S1...,Sn

S0 ← 1 for k from 1 to n

Sk ← kSk−1

for k from 1 to n for j from k+1 to n

Sj ← (j −k)Sj−1 +(j −k+1)Sj return S0,S1,...,Sn.

- Fig. 4 Algorithm SecantNumbers


## 6.3 Comparison with Atkinson’s algorithm

Atkinson [2] gave an elegant algorithm for computing both the Tangent numbers T1,T2,...,Tn and the Secant numbers S0,S1,...,Sn using a “Pascal’s triangle” style of algorithm that only involves additions of non-negative integers. Since a triangle with 2n+1 rows in involved, Atkinson’s algorithm requires 2n2 +O(n) integer additions. This can be compared with n2/2+O(n) additions and n2 +O(n) multiplications (by small integers) for our Algorithm TangentNumbers, and similarly for Algorithm SecantNumbers.

Thus, we might expect Atkinson’s algorithm to be slower than Algorithm TangentNumbers. Computational experiments conﬁrm this. With n = 1000, Algorithm TangentNumbers programmed in Magma takes 1.50 seconds on a 2.26 GHz Intel Core 2 Duo, algorithm SecantNumbers also takes 1.50 seconds, and Atkinson’s algorithm takes 4.51 seconds. Thus, even if both Tangent and Secant numbers are required, Atkinson’s algorithm is slightly slower. It also requires about twice as much memory.

Acknowledgements We thank Jon Borwein for encouraging the belief that high-precision computations are useful in “experimental” mathematics [4], e.g. in the PSLQ algorithm [16]. Ben F. “Tex” Logan, Jr. [25] suggested the use of Tangent numbers to compute Bernoulli numbers. Christian Reinsch [26] pointed out the numerical instability of the recurrence (7) and suggested the use of the numerically stable recurrence (8). Christopher Heckman kindly drew our attention to Atkinson’s algorithm [2]. We thank Paul Zimmermann for his comments. Some of the material presented here is drawn from the recent book Modern Computer Arithmetic [7] (and as-yet-unpublished solutions to exercises in the book). In particular, see [7, §4.7.2 and exercises 4.35–4.41]. Finally, we thank David Bailey, Richard Crandall, and two anonymous referees for suggestions and pointers to additional references.

## References

- 1. Milton Abramowitz and Irene A. Stegun, Handbook of Mathematical Functions, Dover, 1973.
- 2. M. D. Atkinson, How to compute the series expansions of sec x and tan x, Amer. Math. Monthly 93 (1986), 387–389.
- 3. David H. Bailey, Jonathan M. Borwein and Richard E. Crandall, On the Khintchine constant, Math. Comput. 66 (1997), 417–431.
- 4. Jonathan M. Borwein and R. M. Corless, Emerging tools for experimental mathematics, Am. Math. Mon. 106 (1999), 899–909.
- 5. Wieb Bosma, John Cannon and Catherine Playoust, The Magma algebra system. I. The user language, J. Symbolic Comput. 24 (1997), 235-265
- 6. Richard P. Brent, Unrestricted algorithms for elementary and special functions, in Information Processing 80, North-Holland, Amsterdam, 1980, 613–619. arXiv:1004.3621v1
- 7. Richard P. Brent and Paul Zimmermann, Modern Computer Arithmetic, Cambridge University Press, 2010, 237 pp. arXiv:1004.4710v1
- 8. Joe Buhler, Richard Crandall, Reijo Ernvall, Tauno Mets¨ankyla¨ and M. Amin Shokrollahi, Irregular primes and cyclotomic invariants to twelve million, J. Symbolic Computation 31

(2001), 89–96.

- 9. Joe Buhler, Richard Crandall, Reijo Ernvall and Tauno Metsa¨nkyla¨, Irregular primes to four million, Math. Comput. 61 (1993), 151–153.
- 10. Joe Buhler, Richard Crandall and R. Sompolski, Irregular primes to one million, Math. Comput. 59 (1992), 717–722.
- 11. Joe Buhler and David Harvey, Irregular primes to 163 million, Math. Comput. 80 (2011), 2435–2444.
- 12. Thomas Clausen, Theorem, Astron. Nachr. 17 (1840), cols. 351–352.
- 13. Richard E. Crandall, Topics in Advanced Scientiﬁc Computation, Springer-Verlag, 1996.
- 14. Richard E. Crandall and Carl Pomerance, Prime numbers: A Computational Perspective, Springer-Verlag, 2001.
- 15. Karl Dilcher and Ilja Sh. Slavutskii, A Bibliography of Bernoulli Numbers (last updated March 3, 2007), http://www.mscs.dal.ca/%7Edilcher/bernoulli.html.
- 16. Helaman R. P. Ferguson, David H. Bailey and Steve Arno, Analysis of PSLQ, an integer relation ﬁnding algorithm, Math. Comput. 68 (1999), 351–369.
- 17. Martin Fu¨rer, Faster integer multiplication, Proc. 39th Annual ACM Symposium on Theory of Computing (STOC), ACM, San Diego, California, 2007, 57–66.
- 18. Ronald L. Graham, Donald E. Knuth, and Oren Patashnik, Concrete Mathematics, third edition, Addison-Wesley, 1994.
- 19. Kevin Hare, Multisectioning, Rational Poly-Exponential Functions and Parallel Computation, M.Sc. thesis, Dept. of Mathematics and Statistics, Simon Fraser University, Canada, 2002.
- 20. David Harvey, A multimodular algorithm for computing Bernoulli numbers, Math. Comput. 79 (2010), 2361–2370.
- 21. Masanobu Kaneko, The Akiyama-Tanigawa algorithm for Bernoulli numbers, J. of Integer Sequences 3 (2000). Article 00.2.9, 6 pages. http://www.cs.uwaterloo.ca/journals/JIS/.
- 22. Donald E. Knuth, Euler’s constant to 1271 places, Math. Comput. 16 (1962), 275–281.
- 23. Donald E. Knuth and Thomas J. Buckholtz, Computation of Tangent, Euler, and Bernoulli numbers, Math. Comput. 21 (1967), 663–688.
- 24. H. T. Kung, On computing reciprocals of power series, Numer. Math. 22 (1974), 341–348.
- 25. B. F. Logan, unpublished observation, mentioned in [18, §6.5].
- 26. Christian Reinsch, personal communication to R. P. Brent, about 1979, acknowledged in [6].
- 27. Arnold Scho¨nhage and Volker Strassen, Schnelle Multiplikation großer Zahlen, Computing 7

(1971), 281–292.

- 28. Malte Sieveking, An algorithm for division of power series, Computing 10 (1972), 153–156.
- 29. Neil J. A. Sloane, The On-Line Encyclopedia of Integer Sequences, http://oeis.org.


- 30. Karl G. C. von Staudt, Beweis eines Lehrsatzes, die Bernoullischen Zahlen betreffend, J. Reine Angew. Math. 21 (1840), 372–374. http://gdz.sub.uni-goettingen.de.
- 31. Allan Steel, Reduce everything to multiplication, presented at Computing by the Numbers: Algorithms, Precision and Complexity, Workshop for Richard Brent’s 60th birthday, Berlin, 2006, http://www.mathematik.hu-berlin.de/%7Egaggle/EVENTS/2006/BRENT60/.
- 32. William Stein et al, Sage, http://www.sagemath.org/.
- 33. Edward C. Titchmarsh, The Theory of the Riemann Zeta-Function, second edition (revised by D. R. Heath-Brown), Clarendon Press, Oxford, 1986.


