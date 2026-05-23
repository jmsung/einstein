---
type: source
kind: paper
title: Rigorous high-precision computation of the Hurwitz zeta function and its derivatives
authors: Fredrik Johansson
year: 2013
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/1309.2877v1
source_local: ../raw/2013-johansson-rigorous-high-precision-computation-hurwitz.pdf
topic: general-knowledge
cites:
---

arXiv:1309.2877v1[cs.SC]11Sep2013

Rigorous high-precision computation of the Hurwitz zeta function and its derivatives

Fredrik Johansson ∗

RISC Johannes Kepler University 4040 Linz, Austria fredrik.johansson@risc.jku.at

Abstract

We study the use of the Euler-Maclaurin formula to numerically evaluate the Hurwitz zeta function ζ(s, a) for s, a ∈ C, along with an arbitrary number of derivatives with respect to s, to arbitrary precision with rigorous error bounds. Techniques that lead to a fast implementation are discussed. We present new record computations of Stieltjes constants, Keiper-Li coeﬃcients and the ﬁrst nontrivial zero of the Riemann zeta function, obtained using an open source implementation of the algorithms described in this paper.

# 1 Introduction

The Hurwitz zeta function ζ(s,a) is deﬁned for complex numbers s and a by analytic continuation of the sum

∞

1 (k + a)s

ζ(s,a) =

.

![image 1](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile1.png>)

k=0

The usual Riemann zeta function is given by ζ(s) = ζ(s,1).

In this work, we consider numerical computation of ζ(s,a) by the Euler-Maclaurin formula with rigorous error control. Error bounds for ζ(s) are classical (see for example [13], [6] and numerous references therein), but previous works have restricted to the case a = 1 or have not considered derivatives. Our main contribution is to give an eﬃciently computable error bound for ζ(s,a) valid for any complex s and a and for an arbitrary number of derivatives with respect to s (equivalently, we allow s to be a formal power series).

We also discuss implementation aspects, such as parallelization and use of fast polynomial arithmetic. An open source implementation of ζ(s,a) based on the algorithms described in this paper is available. In the last part of the paper, we present results from some new record computations done with this implementation.

Our interest is in evaluating ζ(s,a) to high precision (hundreds or thousands of digits) for a single s of moderate height, say with imaginary part less than 106. Investigations of zeros of large height typically use methods based on the Riemann-Siegel formula and fast multi-evaluation techniques such as the Odlyzko-Scho¨nhage algorithm [28] or the recent algorithm of Hiary [20].

This work is motivated by several applications. For example, recent work of Matiyasevich and Beliakov required values of thousands of nontrivial zeros ρn of ζ(s) to a precision of several

![image 2](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile2.png>)

∗Supported by the Austrian Science Fund (FWF) grant Y464-N18.

thousand digits [26, 27]. Investigations of quantities such as the Stieltjes constants γn(a) and the Keiper-Li coeﬃcients λn also call for high-precision values [22, 24]. The diﬃculty is not necessarily that the ﬁnal result needs to be known to very high accuracy, but that intermediate calculations may involve catastrophic cancellation.

More broadly, the Riemann and Hurwitz zeta functions are useful for numerical evaluation of various other special functions such as polygamma functions, polylogarithms, Dirichlet L-functions, generalized hypergeometric functions at singularities [4], and certain number-theoretical constants [14]. High-precision numerical values are of particular interest for guessing algebraic relations among special values of such functions (which subsequently may be proved rigorously by other means) or ruling out the existence of algebraic relations with small norm [1].

# 2 Evaluation using the Euler-Maclaurin formula

Assume that f is analytic on a domain containing [N,U] where N,U ∈ Z, and let M be a positive integer. Let Bn denote the n-th Bernoulli number and let B˜n(t) = Bn(t − ⌊t⌋) denote the n-th periodic Bernoulli polynomial. The Euler-Maclaurin summation formula (described in numerous works, such as [29]) states that

U

f(k) = I + T + R (1)

k=N

where

U

I =

f(t)dt, (2)

N

M

- 1

![image 3](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile3.png>)

- 2


B2k (2k)!

f(2k−1)(U) − f(2k−1)(N) , (3)

T =

(f(N) + f(U)) +

![image 4](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile4.png>)

k=1

B˜2M(t) (2M)!

U

f(2M)(t)dt. (4)

R = −

![image 5](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile5.png>)

N

If f decreases suﬃciently rapidly, (1)–(4) remain valid after letting U → ∞. To evaluate the Hurwitz zeta function, we set

1 (a + k)s

f(k) =

= exp(−s log(a + k))

![image 6](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile6.png>)

with the conventional logarithm branch cut on (−∞,0). The derivatives of f(k) are given by

(−1)r(s)r (a + k)s+r

f(r)(k) =

![image 7](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile7.png>)

where (s)r = s(s + 1)···(s + r − 1) denotes a rising factorial. The Euler-Maclaurin summation formula now gives, at least for ℜ(s) > 1 and a = 0,−1,−2,...,

N−1

∞

ζ(s,a) =

f(k) +

f(k) = S + I + T + R (5)

k=0

k=N

where

- S =

N−1

k=0

1 (a + k)s

![image 8](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile8.png>)

, (6)

I =

∞

N

1 (a + t)s

![image 9](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile9.png>)

dt =

(a + N)1−s s − 1

![image 10](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile10.png>)

, (7)

- T =


M

(s)2k−1 (a + N)2k−1

- 1

![image 11](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile11.png>)

- 2


B2k (2k)!

1 (a + N)s

, (8)

+

![image 12](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile12.png>)

![image 13](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile13.png>)

![image 14](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile14.png>)

k=1

B˜2M(t) (2M)!

∞

(s)2M (a + t)s+2M

R = −

dt. (9)

![image 15](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile15.png>)

![image 16](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile16.png>)

N

If we choose N and M such that ℜ(a + N) > 0 and ℜ(s + 2M − 1) > 0, the integrals in I and R are well-deﬁned, giving us the analytic continuation of ζ(s,a) to s ∈ C except for the pole at s = 1.

In order to evaluate derivatives with respect to s of ζ(s,a), we substitute s → s + x ∈ C[[x]] and evaluate (5)–(9) with the corresponding arithmetic operations done on formal power series (which may be truncated at some arbitrary ﬁnite order in an implementation). For example, the summand in (6) becomes

∞

(−1)i log(a + k)i (a + k)s

1 (a + k)s+x

xi ∈ C[[x]]. (10)

=

![image 17](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile17.png>)

![image 18](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile18.png>)

i=0

Note that we can evaluate ζ(S,a) for any formal power series S = s + s1x + s2x2 + ... by ﬁrst evaluating ζ(s + x,a) and then formally right-composing by S − s. We can also easily evaluate derivatives of ζ(s,a) − 1/(s − 1) at s = 1. The pole of ζ(s,a) only appears in the term I on the right hand side of (5), so we can remove the singularity as

lim

s→1

(a + N)1−(s+x) (s + x) − 1 −

1 (s + x) − 1

1 (s + x) − 1

I −

=

![image 19](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile19.png>)

![image 20](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile20.png>)

![image 21](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile21.png>)

∞

(−1)i+1 log(a + N)i+1 i!

xi ∈ C[[x]]. (11)

=

![image 22](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile22.png>)

i=0

For F = k fkxk ∈ C[[x]], deﬁne |F| = k |fk|xk ∈ R[[x]]. If it holds for all k that |fk| ≤ |gk|, we write |F| ≤ |G|. Clearly |F + G| ≤ |F| + |G| and |FG| ≤ |F||G|. With this notation, we wish

to bound |R(s + x)| where R(s) = R is the remainder integral given in (9). To express the error bound in a compact form, we introduce the sequence of integrals deﬁned for integers k ≥ 0 and real parameters A > 0,B > 1,C ≥ 0 by

∞

t−B(C + log t)kdt.

Jk(A,B,C) ≡

A

Using the binomial theorem, Jk(A,B,C) can be evaluated in closed form for any ﬁxed k. In fact, collecting factors gives

Lk (B − 1)k+1AB−1

Jk(A,B,C) =

![image 23](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile23.png>)

where L0 = 1, Lk = kLk−1 + Dk and D = (B − 1)(C + log A). This recurrence allows computing J0,J1,...,Jn easily, using O(n) arithmetic operations.

Theorem 1. Given complex numbers s = σ + τi, a = α + βi and positive integers N,M such that α + N > 1 and σ + 2M > 1, the error term (9) in the Euler-Maclaurin summation formula applied to ζ(s + x,a) ∈ C[[x]] satisﬁes

∞

4 |(s + x)2M| (2π)2M

Rkxk ∈ R[[x]] (12)

|R(s + x)| ≤

![image 24](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile24.png>)

k=0

where Rk ≤ (K/k!)Jk(N + α,σ + 2M,C), with C =

β2 (α + N)2

- 1

![image 25](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile25.png>)

- 2


log 1 +

![image 26](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile26.png>)

+ atan |β| α + N

![image 27](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile27.png>)

(13)

and

K = exp max 0,τ atan

β α + N

![image 28](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile28.png>)

. (14)

Proof. We have

|R(s + x)| =

B˜2M(t) (2M)!

∞

(s + x)2M (a + t)s+x+2M

dt

![image 29](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile29.png>)

![image 30](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile30.png>)

N

B ˜2M(t) (2M)!

∞

(s + x)2M (a + t)s+x+2M

≤

dt

![image 31](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile31.png>)

![image 32](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile32.png>)

N

∞

1 (a + t)s+x+2M

4 |(s + x)2M| (2π)2M

≤

![image 33](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile33.png>)

![image 34](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile34.png>)

N

dt

where the last step invokes the fact that

4(2M)! (2π)2M

|B˜2M(t)| <

.

![image 35](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile35.png>)

Thus it remains to bound the coeﬃcients Rk satisfying

∞

N

1 (a + t)s+x+2M

![image 36](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile36.png>)

dt =

k

Rkxk, Rk =

∞

1 k!

![image 37](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile37.png>)

N

log(a + t)k (a + t)s+2M

![image 38](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile38.png>)

dt.

By the assumption that α + t ≥ α + N ≥ 1, we have

βi α + t ≤ log(α + t) + log 1 +

|log(α + βi + t)| = log(α + t) + log 1 +

![image 39](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile39.png>)

βi α + t

![image 40](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile40.png>)

β2 (α + t)2

- 1

![image 41](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile41.png>)

- 2


β α + t ≤ log(α + t) + C

= log(α + t) +

+ i atan

log 1 +

![image 42](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile42.png>)

![image 43](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile43.png>)

where C is deﬁned as in (13). By the assumption that σ + 2M > 1, we have

K (α + t)σ+2M

exp(τ arg(α + βi + t)) |α + βi + t|σ+2M

1 |(α + βi + t)σ+τi+2M|

≤

=

![image 44](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile44.png>)

![image 45](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile45.png>)

![image 46](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile46.png>)

where K is deﬁned as in (14). Bounding the integrand in Rk in terms of the integrand in the deﬁnition of Jk now gives the result.

![image 47](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile47.png>)

![image 48](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile48.png>)

![image 49](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile49.png>)

![image 50](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile50.png>)

The bound given in Theorem 1 should generally approximate the exact remainder (9) quite well, even for derivatives of large order, if |a| is not too large. The quantity K is especially crude, however, as it does not decrease when |a + t|−τi decreases exponentially as a function of τ. We have made this simpliﬁcation in order to obtain a bound that is easy to evaluate for all s,a. In fact, assuming that a is small, we can simplify the bounds a bit further using

β2 2(α + N)2

+ |β| (α + N)

.

C ≤

![image 51](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile51.png>)

![image 52](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile52.png>)

In practice, the Hurwitz zeta function is usually only considered for 0 < a ≤ 1, unless s is an integer greater than 1 in which case it reduces to a polygamma function of a. It is easy to derive error bounds for polygamma functions that are accurate for large |a|, and we do not consider this special case further here.

# 3 Algorithmic matters

The evaluation of ζ(s + x,a) can be broken into three stages:

- 1. Choosing parameters M and N and bounding the remainder R.
- 2. Evaluating the power sum S.
- 3. Evaluating the tail T (and the trivial term I).


In this section, we describe some algorithmic techniques that are useful at each stage. We sketch the computational complexities, but do not attempt to prove strict complexity bounds.

We assume that arithmetic on real and complex numbers is done using ball arithmetic [33], which essentially is ﬂoating-point arithmetic with the added automatic propagation of error bounds. This is probably the most reasonable approach: a priori ﬂoating-point error analysis would be overwhelming to do in full generality (an analysis of the ﬂoating-point error when evaluating ζ(s) for real s, with a partial analysis of the complex case, is given in [30]).

Using algorithms based on the Fast Fourier Transform (FFT), arithmetic operations on b-bit approximations of real or complex numbers can be done in time O˜(b), where the O˜-notation suppresses logarithmic factors. This estimate also holds for division and evaluation of elementary functions.

Likewise, polynomials of degree n can be multiplied in O˜(n) coeﬃcient operations. Here some care is required: when doing arithmetic with polynomials that have approximate coeﬃcients, the accuracy of the result can be much lower than the working precision, depending on the shape of the polynomials and the multiplication algorithm. If the coeﬃcients vary in magnitude as 2±O˜(n), we may need O˜(n) bits of precision to get an accurate result, making the eﬀective complexity O˜(n2). This issue is discussed further in [32].

Many operations can be reduced to fast multiplication. In particular, we will need the binary splitting algorithm: if a sequence cn of integers (or polynomials) satisﬁes a suitable linear recurrence relation and its bit size (or degree) grows as O˜(n), then we can use a balanced product tree to evaluate cn using O˜(n) bit (or coeﬃcient) operations, versus O˜(n2) for repeated application of the recurrence relation [2, 17].

- 3.1 Evaluating the error bound


For a precision of P bits, we should choose N ∼ M ∼ P. A simple strategy is to do a binary search for an N that makes the error bound small enough when M = cN where c ≈ 1. This is suﬃcient for our present purposes, but more sophisticated approaches are possible. In particular, for evaluation at large heights in the critical strip, N should be larger than M.

Given complex balls for s and a, and integers N and M, we can evaluate the error bound (12) using ball arithmetic. The output is a power series with ball coeﬃcients. The absolute value of each coeﬃcient in this series should be added to the radius for the corresponding coeﬃcient in S+I +T ≈ ζ(s+x,a) at the end of the whole computation. If the assumptions that ℜ(a)+N > 1 and ℜ(s) + 2M > 1 are not satisﬁed for all points in the balls s and a, we set the error bounds for all coeﬃcients to +∞.

If we are computing D derivatives and D is large, the rising factorial |(s+x)2M| can be computed using binary splitting and the outer power series product in (12) can be done using fast polynomial multiplication, so that only O˜(D +M) real number operations are required. Or, if D is small and M is large, |(s + x)2M| can be computed via the gamma function in time independent of M

- 3.2 Evaluating the power sum


As a power series, the power sum S becomes Nk=0−1( i ci(k)xi) where the coeﬃcients ci(k) are given by (10). For i ≥ 1, the coeﬃcients can be computed using the recurrence

log(a + k) i + 1

ci+1(k) = −

ci(k).

![image 53](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile53.png>)

If we are computing D derivatives with a working precision of P bits, the complexity of evaluating the power sum is O˜(NPD), or O˜(N2D) if N ∼ P. The computation is easy to parallelize by assigning a range of k values to each thread (for large D, a more memory-eﬃcient method is to assign a range of i to each thread).

![image 54](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile54.png>)

- Algorithm 1 Sieved summation of a completely multiplicative function Input: A function f such that f(jk) = f(j)f(k) for j,k ∈ Z≥1, and an integer N ≥ 1 Output: Nk=1 f(k)


![image 55](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile55.png>)

- 1: p ← 2⌊log2 N⌋ (largest power of two such that p ≤ N)
- 2: h ← 1, z ← 0, u ← 0
- 3: D = [] ⊲ Build table of divisors
- 4: for k ← 1; k ≤ N; k ← k + 2 do
- 5: D[k] ← 0
- 6: for k ← 3; k ≤ ⌊

√N⌋; k ← k + 2 do

![image 56](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile56.png>)

- 7: if D[k] = 0 then
- 8: for j ← k2; j ≤ N; j ← j + 2k do
- 9: D[j] ← k
- 10: F = [] ⊲ Create initially empty cache of f(k) values
- 11: F[2] ← f(2)
- 12: for k ← 1; k ≤ N; k ← k + 2 do
- 13: if D[k] = 0 then ⊲ k is prime (or 1)
- 14: t ← f(k)
- 15: else
- 16: t ← F[D[k]]F[k/D[k]] ⊲ k is composite
- 17: if 3k ≤ N then
- 18: F[k] ← t ⊲ Store f(k) for future use
- 19: u ← u + t
- 20: while k = h and p = 1 do ⊲ Horner’s rule
- 21: z ← u + F[2]z
- 22: p ← p/2
- 23: h ← ⌊N/p⌋
- 24: if h is even then
- 25: h ← h − 1
- 26: return u + F[2]z


![image 57](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile57.png>)

When evaluating the ordinary Riemann zeta function, i.e. when a = 1, and we just want to compute a small number of derivatives, we can speed up the power sum a bit. Writing the sum as Nk=1 f(k), the terms f(k) = k−(s+x) are completely multiplicative, i.e. f(k1k2) = f(k1)f(k2). This means that we only need to evaluate f(k) from scratch when k is prime; when k is composite, a single multiplication is suﬃcient.

This method has two drawbacks: we have to store previously computed terms, which requires O(NPD) space, and the power series multiplication f(k1)f(k2) becomes more expensive than evaluating f(k1k2) from scratch for large D. For both reasons, this method is only useful when D is quite small (say D ≤ 4).

We can avoid some redundant work by collecting multiples of small primes. For example, if we

extract all powers of two, 10k=1 f(k) can be written as [f(1) + f(3) + f(5) + f(7) + f(9)]

+f(2) [f(1) + f(3) + f(5)]

+f(4) [f(1)]

+f(8) [f(1)].

This is a polynomial in f(2) and can be evaluated from bottom to top using Horner’s rule while progressively adding the terms in the brackets. Asymptotically, this reduces the number of multiplications and the size of the tables by half. Algorithm 1 implements this trick, and requires about π(N) ≈ N/ logN evaluations of f(k) and N/2 multiplications, at the expense of having to store about N/6 function values plus a table of divisors of about N/2 integers. Constructing the table of divisors using the sieve of Eratosthenes requires O(N log log N) integer operations, but this cost is negligible when multiplications and f(k) evaluations are expensive. One could also extract other powers besides 2 (for example powers of 3 and 5), but this gives diminishing returns.

Another trick that can save time at high precision is to avoid computing the logarithms of integers from scratch. If q and p are nearby integers (such as two consecutive primes) and we already know log(p), we can use the identity

log(q) = log(p) + 2 atanh

q − p q + p

![image 58](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile58.png>)

and evaluate the inverse hyperbolic tangent by applying binary splitting to its Taylor series. This is not an asymptotic improvement over the best known algorithm for computing the logarithm (which uses the arithmetic-geometric mean), but likely faster in practice.

- 3.3 Evaluating the tail

Except for the multiplication by Bernoulli numbers, the terms of the tail sum T satisfy a simple (hypergeometric) recurrence relation. If we are computing D derivatives with a working precision of P bits, the complexity of evaluating the tail by repeated application of the recurrence relation is O˜(MPD), or O˜(P2D) if M ∼ P. We can do better if D is large, using binary splitting (Algorithm 2).

If D ∼ M, the complexity with binary splitting is only O˜(PD), or softly optimal in the bit size of the output. A drawback is that the intermediate products increase the memory consumption.

The Bernoulli numbers can of course be cached for repeated evaluation of the zeta function, but computing them the ﬁrst time can be a bottleneck at high precision, at least if done naively. The ﬁrst 2M Bernoulli numbers can be computed in quasi-optimal time O˜(M2), for example by using Newton iteration and fast polynomial multiplication to invert the power series (ex − 1)/x. For most practical purposes, simpler algorithms with a time complexity of O˜(M3) are adequate, however. Various algorithms are discussed in [19]. An interesting alternative, used in unpublished work of Bloemen [3], is to compute Bn via ζ(n) by direct approximation of the sum ∞k=0 k−n, recycling the powers to process several n simultaneously.

- 4 Implementation and benchmarks


We have implemented the Hurwitz zeta function for s ∈ C[[x]] and a ∈ C with rigorous error bounds as part of the Arb library1. This library is written in C and is freely available under version 2 or later of the GNU General Public License. It uses the MPFR [15] library for evaluation

![image 59](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile59.png>)

1http://fredrikj.net/arb

![image 60](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile60.png>)

- Algorithm 2 Evaluation of the tail T using binary splitting Input: s,a ∈ C and N,M,D ∈ Z≥1


![image 61](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile61.png>)

M

1 (a + N)s+x

(s + x)2k−1 (a + N)2k−1 ∈ C[[x]]/ xD

- 1

![image 62](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile62.png>)

- 2


B2k (2k)!

Output: T =

+

![image 63](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile63.png>)

![image 64](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile64.png>)

![image 65](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile65.png>)

k=1

- 1: Let x denote the generator of C[[x]]/ xD
- 2: function BinSplit(j, k)
- 3: if j + 1 = k then
- 4: if j = 0 then
- 5: P ← (s + x)/(2(a + N))
- 6: else
- 7: P ←

(s + 2j − 1 + x)(s + 2j + x) (2j + 1)(2j + 2)(a + N)2

![image 66](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile66.png>)

- 8: return (P, B2j+2P)
- 9: else
- 10: (P1, R1) ← BinSplit(j, ⌊(j + k)/2⌋)
- 11: (P2, R2) ← BinSplit(⌊(j + k)/2⌋, k)
- 12: return (P1P2, R1 + P1R2) ⊲ Polynomial multiplications mod xD
- 13: (P, R) ← BinSplit(0,M)
- 14: T ← (a + N)−(s+x)(1/2 + R) ⊲ Polynomial multiplication mod xD
- 15: return T


![image 67](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile67.png>)

of some elementary functions, GMP [11] or MPIR [12] for integer arithmetic, and FLINT [18] for polynomial arithmetic.

Our implementation incorporates most of the techniques discussed in the previous section, including optional parallelization of the power sum. Bernoulli numbers are computed using the algorithm of Bloemen. Fast and numerically stable multiplication in R[x] and C[x] is implemented by rescaling polynomials and breaking them into segments with similarly-sized coeﬃcients and computing the subproducts exactly in Z[x] (a simpliﬁed version of van der Hoeven’s block multiplication algorithm [32]). Polynomial multiplication in Z[x] is done via FLINT which for large polynomials uses a Scho¨nhage-Strassen FFT implementation by William Hart.

- 4.1 Computing zeros to high precision


For n ≥ 1, let ρn denote the n-th smallest zero of ζ(s) with positive imaginary part. We assume that ρn is simple and has real part 1/2. Using Newton’s method, we can evaluate ρn to high precision nearly as fast as we can evaluate ζ(s) for s near ρn.

It is convenient to work with real numbers. The ordinate tn = ℑ(ρn) is a simple zero of the real-valued function Z(t) = eiθ(t)ζ(1/2 + it) where

log Γ 2it4+1 − log Γ −2it4+1 2i −

log π 2

![image 68](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile68.png>)

![image 69](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile69.png>)

t.

θ(t) =

![image 70](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile70.png>)

![image 71](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile71.png>)

We assume that we are given an isolating ball B0 = [m0 − ε0,m0 + ε0] such that tn ∈ B0 and tm  ∈ B0,m = n, and wish to compute tn to high precision (ﬁnding such a ball for a given n is an interesting problem, but we do not consider it here).

Newton’s method maps an approximation zn of a root of a real analytic function f(z) to a new approximation zn+1 via zn+1 = zn−f(zn)/f′(zn). Using Taylor’s theorem, the error can be shown to satisfy

|ǫn+1| = |f′′(ξn)| 2 |f′(zn)|

|ǫn|2 for some ξn between zn and the root.

![image 72](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile72.png>)

![image 73](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile73.png>)

![image 74](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile74.png>)

![image 75](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile75.png>)

![image 76](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile76.png>)

![image 77](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile77.png>)

![image 78](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile78.png>)

![image 79](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile79.png>)

![image 80](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile80.png>)

![image 81](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile81.png>)

Digits mpmath Mathematica Arb

![image 82](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile82.png>)

![image 83](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile83.png>)

![image 84](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile84.png>)

![image 85](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile85.png>)

![image 86](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile86.png>)

![image 87](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile87.png>)

ρ˜1 ζ(˜ρ1) ρ˜1 ζ(˜ρ1) ρ˜1 ζ(˜ρ1) 100 0.080 0.0031 0.044 0.012 0.012 0.0011 1000 7.1 0.24 11 1.6 0.18 0.05 10000 7035 252 5127 779 29 15 100000 - - - - 6930 3476 303000 - - - - 73225 31772

![image 88](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile88.png>)

![image 89](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile89.png>)

![image 90](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile90.png>)

![image 91](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile91.png>)

![image 92](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile92.png>)

![image 93](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile93.png>)

![image 94](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile94.png>)

![image 95](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile95.png>)

![image 96](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile96.png>)

![image 97](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile97.png>)

![image 98](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile98.png>)

![image 99](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile99.png>)

![image 100](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile100.png>)

![image 101](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile101.png>)

![image 102](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile102.png>)

![image 103](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile103.png>)

![image 104](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile104.png>)

![image 105](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile105.png>)

![image 106](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile106.png>)

![image 107](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile107.png>)

![image 108](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile108.png>)

![image 109](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile109.png>)

![image 110](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile110.png>)

![image 111](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile111.png>)

![image 112](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile112.png>)

![image 113](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile113.png>)

- Table 1: Time in seconds to compute an approximation ρ˜1 of the ﬁrst nontrivial zero ρ1 accurate to the speciﬁed number of decimal digits, and then to evaluate ζ(˜ρ1) at the same precision. Computations were done on a 64-bit Intel Xeon E5-2650 2.00 GHz CPU.


As a setup step, we evaluate Z(s),Z′(s),Z′′(s) (simultaneously using power series arithmetic) at s = B0, and compute

max|Z′′(B0)| 2 min|Z′(B0)|

.

C =

![image 114](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile114.png>)

This only needs to be done at low precision. Starting from an input ball Bk = [mk − εk,mk + εk], one step with Newton’s method gives an output ball Bk+1 = [mk+1 − εk+1,mk+1 + εk+1]. The updated midpoint is given by

Z(mk) Z′(mk)

(15)

mk+1 = mk −

![image 115](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile115.png>)

where we evaluate Z(mk) and Z′(mk) simultaneously using power series arithmetic. The updated radius is given by εk+1 = ε′k+1 + Cε2k where ε′k+1 is the numerical error (or a bound thereof) resulting from evaluating (15) using ﬁnite-precision arithmetic. The new ball is valid as long as Bk+1 ⊆ Bk (if this does not hold, the algorithm fails and we need to start with a better B0 or increase the working precision).

For best performance, the evaluation precision should be chosen so that ε′k+1 ≈ Cε2k. In other words, for a target accuracy of p bits, the evaluations should be done at ...,p/4,p/2,p bits, plus

some guard bits.

As a benchmark problem, we compute an approximation ρ˜1 of the ﬁrst nontrivial zero ρ1 ≈ 1/2+ 14.1347251417i and then evaluate ζ(˜ρ1) to the same precision. We compare our implementation of the zeta function and the root-reﬁnement algorithm described above (starting from a doubleprecision isolating ball) with the zetazero and zeta functions provided in mpmath version 0.17 in Sage 5.10 [31] and the ZetaZero and Zeta functions provided in Mathematica 9.0. The results of this benchmark are shown in Table 1. At 10000 digits, our code for computing the zero is about two orders of magnitude faster than the other systems, and the subsequent single zeta evaluation is about one order of magnitude faster.

We have computed ρ1 to 303000 digits, or slightly more than one million bits, which appears to be a record (a 20000-digit value is given in [27]). The computation used up to 62 GiB of memory for the sieved power sum and the storage of Bernoulli numbers up to B325328 (to attain even higher precision, the memory usage could be reduced by evaluating the power sum without sieving, perhaps using several CPUs in parallel, and not caching Bernoulli numbers).

- 4.2 Computing the Keiper-Li coeﬃcients


Riemann’s function ξ(s) = 21s(s − 1)π−s/2Γ(s/2)ζ(s) satisﬁes the symmetric functional equation ξ(s) = ξ(1 − s). The coeﬃcients {λn}∞n=1 deﬁned by

![image 116](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile116.png>)

∞

x x − 1

1 1 − x

λnxn

= log ξ

= − log2 +

log ξ

![image 117](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile117.png>)

![image 118](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile118.png>)

n=1

![image 119](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile119.png>)

![image 120](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile120.png>)

![image 121](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile121.png>)

![image 122](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile122.png>)

n = 1000 n = 10000 n = 100000 1: Error bound 0.017 1.0 97 1: Power sum 0.048 47 65402 (1: Power sum, CPU time) (0.65) (693) (1042210) 1: Bernoulli numbers 0.0020 0.19 59

![image 123](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile123.png>)

![image 124](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile124.png>)

![image 125](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile125.png>)

![image 126](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile126.png>)

![image 127](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile127.png>)

![image 128](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile128.png>)

![image 129](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile129.png>)

![image 130](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile130.png>)

![image 131](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile131.png>)

![image 132](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile132.png>)

![image 133](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile133.png>)

![image 134](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile134.png>)

![image 135](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile135.png>)

![image 136](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile136.png>)

- 1: Tail 0.058 11 1972

![image 137](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile137.png>)

![image 138](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile138.png>)

![image 139](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile139.png>)

![image 140](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile140.png>)

- 2: Series logarithm 0.047 8.5 1126

![image 141](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile141.png>)

![image 142](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile142.png>)

![image 143](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile143.png>)

- 3: log Γ(1 + x) series 0.019 3.0 1610

![image 144](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile144.png>)

![image 145](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile145.png>)

![image 146](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile146.png>)

- 4: Composition 0.022 4.1 593 Total wall time 0.23 84 71051 Peak RAM usage (MiB) 8 730 48700


![image 147](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile147.png>)

![image 148](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile148.png>)

![image 149](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile149.png>)

![image 150](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile150.png>)

![image 151](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile151.png>)

![image 152](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile152.png>)

![image 153](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile153.png>)

![image 154](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile154.png>)

![image 155](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile155.png>)

![image 156](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile156.png>)

![image 157](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile157.png>)

- Table 2: Elapsed time in seconds to evaluate the Keiper-Li coeﬃcients λ0 ...λn with a working precision of 1.1n + 50 bits, giving roughly 0.1n accurate bits. The computations were done on a multicore system with 64-bit Intel Xeon E7-8837 2.67 GHz CPUs (16 threads were used for the power sum, and all other parts were computed serially on a single core).


were introduced by Keiper [22], who noted that the truth of the Riemann hypothesis would imply that λn > 0 for all n > 0. In fact, Keiper observed that if one makes an assumption about the distribution of the zeros of ζ(s) that is even stronger than the Riemann hypothesis, the coeﬃcients λn should behave as

λn ≈ (1/2)(log n − log(2π) + γ − 1). (16)

Keiper presented numerical evidence for this conjecture by computing λn up to n = 7000, showing that the approximation error appears to ﬂuctuate increasingly close to zero. Some years later, Li proved [25] that the Riemann hypothesis actually is equivalent to the positivity of λn for all n > 0 (this reformulation of the Riemann hypothesis is known as Li’s criterion). Recently, Arias de Reyna has proved that a certain precise statement of (16) also is equivalent to the Riemann hypothesis [10].

![image 158](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile158.png>)

| | | | | |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |


Figure 1: Plot of n (λn − (log n − log(2π) + γ − 1)/2).

A computation of the Keiper-Li coeﬃcients up to n = 100000 shows agreement with Keiper’s conjecture (and the Riemann hypothesis), as illustrated in Figure 1. We obtain λ100000 = 4.62580782406902231409416038 ... (plus about 2900 more accurate digits), whereas (16) gives

λ100000 ≈ 4.626132. Empirically, we need a working precision of about n bits to determine λn accurately. A breakdown of the computation time to determine the signs of λn up to n = 1000, 10000 and 100000 is shown in Table 2.

Our computation of the Keiper-Li coeﬃcients uses the formula

s 2

log ξ(s) = log(−ζ(s)) + log Γ 1 +

![image 159](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile159.png>)

s log π 2

+ log(1 − s) −

![image 160](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile160.png>)

which we evaluate at s = x ∈ R[[x]]. This arrangement of the terms avoids singularities and branch cuts at the expansion point. We carry out the following steps (plus some more trivial operations):

- 1. Computing the series expansion of ζ(s) at s = 0.
- 2. Computing the logarithm of a power series, i.e. log f(x) = f′(x)/f(x)dx.
- 3. Computing the series expansion of log Γ(s) at s = 1, i.e. computing γ,ζ(2),ζ(3),ζ(4),....
- 4. Finally, right-composing by x/(x − 1) to obtain the Keiper-Li coeﬃcients.


Step 2 requires O(M(n)) arithmetic operations on real numbers. We use a hybrid algorithm to compute the integer zeta values in step 3; the details are beyond the scope of the present paper.

There is a very fast way to perform step 4. For f = ∞k=0 akxk ∈ C[[x]], the binomial (or Euler) transform T : C[[x]] → C[[x]] is deﬁned by

n

∞

n k

1 1 − x

x x − 1

ak xn.

(−1)k

T[f(x)] =

=

f

![image 161](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile161.png>)

![image 162](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile162.png>)

n=0

k=0

We have

a0 − f x

x x − 1

. If B: C[[x]] → C[[x]] denotes the Borel transform

= a0 + xT

f

![image 163](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile163.png>)

![image 164](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile164.png>)

∞

∞

ak k!

xk,

akxk =

B

![image 165](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile165.png>)

k=0

k=0

then (see [16]) T[f(x)] = B−1[exB[f(−x)]]. This identity gives an algorithm for evaluating the composition which requires only M(n) + O(n) coeﬃcient operations where M(n) = O˜(n) is the operation complexity of polynomial multiplication. Moreover, this algorithm is numerically stable (in the sense that it does not signiﬁcantly increase errors from the input when using ball arithmetic), provided that a numerically stable polynomial multiplication algorithm is used.

The composition could also be carried out using various generic algorithms for composition of power series. We tested three other algorithms, and found them to perform much worse:

- • Horner’s rule is slow (requiring about nM(n) operations) and is numerically unsatisfactory in the sense that it gives extremely poor error bounds with ball arithmetic.
- • The Brent-Kung algorithm based on matrix multiplication [8] turns out to give adequate error bounds, but uses about O(n1/2M(n)+n2) operations which still is expensive for large n.
- • We also tried binary splitting: to evaluate f(p/q) where f is a power series and p and q are polynomials, we recursively split the evaluation in half and keep numerator and denominator polynomials separated. In the end, we perform a single power series division. This only costs O(M(n)log n) operations, but turns out to be numerically unstable. It would be of independent interest to investigate whether this algorithm can be modiﬁed to avoid the stability problem.


- 4.3 Computing the Stieltjes constants


The generalized Stieltjes constants γn(a) are deﬁned by

1 s − 1

ζ(s,a) =

+

![image 166](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile166.png>)

∞

(−1)n n!

γn(a) (s − 1)n.

![image 167](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile167.png>)

n=0

The “usual” Stieltjes constants are γn(1) = γn, and γ0 = γ ≈ 0.577216 is Euler’s constant. The Stieltjes constants were ﬁrst studied over a century ago. Some historical notes and numerical values of γn for n ≤ 20 are given in [5]. Keiper [22] provides a method for computing the Stieltjes constants based on numerical integration and recurrence relations, and lists various γn up to n = 150. Keiper’s algorithm is implemented in Mathematica [21].

More recently, Kreminski [24] has given an algorithm for the Stieltjes constants, also based on numerical integration but diﬀerent from Keiper’s. He reports having computed γn to a few thousand digits for all n ≤ 10000, and provides further isolated values up to γ50000 (accurate to 1000 digits) as well as tables of γn(a) with various a = 1.

The best proven bounds for the Stieltjes constants appear to be very pessimistic. In a recent paper, Knessl and Coﬀey [23] give an asymptotic approximation formula for the Stieltjes constants that seems to be very accurate even for small n. Based on numerical computations done with Mathematica, they note that their approximation correctly predicts the sign of γn up to at least n = 35000 with the single exception of n = 137.

Our implementation immediately gives the generalized Stieltjes constants by computing the series expansion of ζ(s,a) − 1/(s − 1) at s = 1 using (11). The costs are similar to those for computing the Keiper-Li coeﬃcients: due to ill-conditioning, it appears that we need about n + p bits of precision to determine γn with p bits of accuracy. This makes our method somewhat unattractive for computing just a few digits of γn when n is large, but reasonably good if we want a large number of digits. Our method is also useful if we want to compute a table of all the values γ0,...,γn simultaneously.

For example, we can compute γn for all n ≤ 1000 to 1000-digit accuracy in just over 10 seconds on a single CPU. Computing the single coeﬃcient γ1000 to 1000-digit accuracy with Mathematica 9.0 takes 80 seconds, with an estimated 20 hours required for all n ≤ 1000. Thus our implementation is nearly four orders of magnitude faster. We can compute a table of accurate values of γn for all n ≤ 10000 in a few minutes on an ordinary workstation with around one GiB of memory.

We have computed all γn up to n = 100000 using a working precision of 125050 bits, resulting in an accuracy from about 37640 decimal digits for γ0 to about 10860 accurate digits for γ100000. The computation took 26 hours on a multicore system with 16 threads utilized for the power sum, with a peak memory consumption of about 80 GiB during the binary splitting evaluation of the tail. As shown in Figure 2, the accuracy of the Knessl-Coﬀey approximation approaches six digits on average. Our computation gives γ100000 = 1.991927306312541095658... × 1083432, while the Knessl-Coﬀey approximation gives γn ≈ 1.9919333 × 1083432. We are able to verify that n = 137 is the only instance for n ≤ 100000 where the Knessl-Coﬀey approximation has the wrong sign.

We emphasize that our implementation gives γn(a) with proved error bounds, while the other cited works and implementations (to our knowledge) depend on heuristic error estimates.

We have not yet implemented a function for computing isolated Stieltjes constants of large index; this would have roughly the same running time as the evaluation of the tail (since only a single derivative of the power sum would have to be computed). The memory consumption is highest when evaluating the tail, and would therefore remain the same.

![image 168](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile168.png>)

![image 169](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile169.png>)

![image 170](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile170.png>)

![image 171](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile171.png>)

![image 172](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile172.png>)

![image 173](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile173.png>)

![image 174](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile174.png>)

![image 175](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile175.png>)

![image 176](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile176.png>)

![image 177](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile177.png>)

![image 178](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile178.png>)

![image 179](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile179.png>)

![image 180](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile180.png>)

![image 181](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile181.png>)

![image 182](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile182.png>)

![image 183](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile183.png>)

![image 184](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile184.png>)

![image 185](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile185.png>)

![image 186](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile186.png>)

![image 187](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile187.png>)

![image 188](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile188.png>)

![image 189](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile189.png>)

![image 190](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile190.png>)

![image 191](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile191.png>)

![image 192](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile192.png>)

![image 193](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile193.png>)

![image 194](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile194.png>)

![image 195](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile195.png>)

![image 196](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile196.png>)

![image 197](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile197.png>)

![image 198](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile198.png>)

![image 199](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile199.png>)

![image 200](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile200.png>)

![image 201](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile201.png>)

![image 202](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile202.png>)

![image 203](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile203.png>)

![image 204](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile204.png>)

![image 205](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile205.png>)

![image 206](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile206.png>)

![image 207](<2013-johansson-rigorous-high-precision-computation-hurwitz_images/imageFile207.png>)

Figure 2: Plot of the relative error |γn − γ˜n|/|γn| of the Knessl-Coﬀey approximation for the Stieltjes constants. The error exhibits a complex oscillation pattern.

# 5 Discussion

One direction for further work would be to improve the error bounds for large |a| and to investigate strategies for selecting N and M optimally, particularly when the number of derivatives is large. It would also be interesting to investigate parallelization of the tail sum, or look for ways to evaluate a single derivative of high order of the tail in a memory-eﬃcient way. Further constant-factor improvements are possible in an implementation, for example by reducing the precision of terms that have small magnitude (rather than naively performing all operations at the same precision).

Finally, it would be interesting to compare the eﬃciency of the Euler-Maclaurin formula with other approaches to evaluating the Hurwitz zeta function such as the algorithms of Borwein [7], Vepˇstas [34] and Coﬀey [9].

# References

- [1] D. H. Bailey and J. M. Borwein. Experimental mathematics: recent developments and future outlook. In B. Engquist, W. Schmid, and P. W. Michor, editors, Mathematics Unlimited – 2001 and Beyond, pages 51–66. Springer, 2000.
- [2] D. J. Bernstein. Fast multiplication and its applications. Algorithmic Number Theory, 44:325– 384, 2008.


- [3] R. Bloemen. Even faster ζ(2n) calculation!, 2009. http://remcobloemen.nl/2009/11/ even-faster-zeta-calculation.html.
- [4] A. I. Bogolubsky and S. L. Skorokhodov. Fast evaluation of the hypergeometric function

pFp−1(a;b;z) at the singular point z = 1 by means of the Hurwitz zeta function ζ(α,s). Programming and Computer Software, 32(3):145–153, 2006.

- [5] J. Bohman and C-E. Fr¨oberg. The Stieltjes function – deﬁnition and properties. Mathematics of Computation, 51(183):281–289, 1988.
- [6] J. M. Borwein, D. M. Bradley, and R. E. Crandall. Computational strategies for the Riemann zeta function. Journal of Computational and Applied Mathematics, 121:247–296, 2000.
- [7] P. Borwein. An eﬃcient algorithm for the Riemann zeta function. Canadian Mathematical Society Conference Proceedings, 27:29–34, 2000.
- [8] R. P. Brent and H. T. Kung. Fast algorithms for manipulating formal power series. Journal of the ACM, 25(4):581–595, 1978.
- [9] M. W. Coﬀey. An eﬃcient algorithm for the Hurwitz zeta and related functions. Journal of Computational and Applied Mathematics, 225(2):338–346, 2009.
- [10] J. Arias de Reyna. Asymptotics of Keiper-Li coeﬃcients. Functiones et Approximatio Commentarii Mathematici, 45(1):7–21, 2011.
- [11] The GMP development team. GMP: The GNU multiple precision arithmetic library. http:// www.gmplib.org.
- [12] The MPIR development team. MPIR: Multiple Precision Integers and Rationals. http:// www.mpir.org.
- [13] H. M. Edwards. Riemann’s zeta function. Academic Press, 1974.
- [14] P. Flajolet and I. Vardi. Zeta function expansions of classical constants. Unpublished manuscript, http://algo.inria.fr/flajolet/Publications/landau.ps, 1996.
- [15] L. Fousse, G. Hanrot, V. Lef`evre, P. P´elissier, and P. Zimmermann. MPFR: A multipleprecision binary ﬂoating-point library with correct rounding. ACM Transactions on Mathematical Software, 33(2):13:1–13:15, June 2007. http://mpfr.org.
- [16] H. Gould. Series transformations for ﬁnding recurrences for sequences. Fibonacci Quarterly, 28:166–171, 1990.
- [17] B. Haible and T. Papanikolaou. Fast multiprecision evaluation of series of rational numbers. In J. P. Buhler, editor, Algorithmic Number Theory: Third International Symposium, volume 1423, pages 338–350. Springer, 1998.
- [18] W. B. Hart. Fast Library for Number Theory: An Introduction. In Proceedings of the Third international congress conference on Mathematical software, ICMS’10, pages 88–91, Berlin, Heidelberg, 2010. Springer-Verlag. http://flintlib.org.
- [19] D. Harvey and R. P. Brent. Fast computation of Bernoulli, tangent and secant numbers,

2011. http://arxiv.org/abs/1108.0286.

- [20] G. Hiary. Fast methods to compute the Riemann zeta function. Annals of mathematics, 174:891–946, 2011.
- [21] Wofram Research Inc. Some notes on internal implementation (section of the online documentation for Mathematica 9.0). http://reference.wolfram.com/mathematica/tutorial/ SomeNotesOnInternalImplementation.html, 2013.
- [22] J. B. Keiper. Power series expansions of Riemann’s ξ function. Mathematics of Computation, 58(198):765–773, 1992.


- [23] C. Knessl and M. Coﬀey. An eﬀective asymptotic formula for the Stieltjes constants. Mathematics of Computation, 80(273):379–386, 2011.
- [24] R. Kreminski. Newton-Cotes integration for approximating Stieltjes (generalized Euler) constants. Mathematics of Computation, 72(243):1379–1397, 2003.
- [25] X-J. Li. The positivity of a sequence of numbers and the Riemann Hypothesis. Journal of Number Theory, 65(2):325–333, 1997.
- [26] Y. Matiyasevich. An artless method for calculating approximate values of zeros of

Riemann’s zeta function, 2012. http://logic.pdmi.ras.ru/~yumat/personaljournal/ artlessmethod/.

- [27] Y. Matiyasevich and G. Beliakov. Zeroes of Riemann’s zeta function on the critical line with 20000 decimal digits accuracy, 2011. http://dro.deakin.edu.au/view/DU:30051725? print_friendly=true.
- [28] A. M. Odlyzko and A. Scho¨nhage. Fast algorithms for multiple evaluations of the Riemann zeta function. Transactions of the American Mathematical Society, 309(2):797–809, 1988.
- [29] F. W. J. Olver. Asymptotics and Special Functions. A K Peters, Wellesley, MA, 1997.
- [30] Y.-F.S P´etermann and J-L. R´emy. Arbitrary precision error analysis for computing ζ(s) with the Cohen-Olivier algorithm: complete description of the real case and preliminary report on the general case. Rapport de recherche RR-5852, INRIA, 2006.
- [31] W.A. Stein et al. Sage Mathematics Software. The Sage Development Team, 2013. http:// www.sagemath.org.
- [32] J. van der Hoeven. Making fast multiplication of polynomials numerically stable. Technical Report 2008-02, Universit´e Paris-Sud, Orsay, France, 2008.
- [33] J. van der Hoeven. Ball arithmetic. Technical report, HAL, 2009. http://hal. archives-ouvertes.fr/hal-00432152/fr/.
- [34] L. Vepˇstas. An eﬃcient algorithm for accelerating the convergence of oscillatory series, useful for computing the polylogarithm and Hurwitz zeta functions. Numerical Algorithms, 47(3):211–252, 2008.


