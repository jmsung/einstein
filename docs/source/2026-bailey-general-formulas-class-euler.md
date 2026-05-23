---
type: source
kind: paper
title: General formulas for a class of Euler sums
authors: David H Bailey, Ross McPhedran, Bruno Salvy
year: 2026
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2604.02384v1
source_local: ../raw/2026-bailey-general-formulas-class-euler.pdf
topic: general-knowledge
cites:
---

# arXiv:2604.02384v1[math.NT]1Apr2026

## General formulas for a class of Euler sums

David H. Bailey, Lawrence Berkeley National Laboratory, USA, dhbailey@lbl.gov Ross McPhedran, School of Physics, University of Sydney 2006, Australia, ross.mcphedran@sydney.edu.au and Bruno Salvy, Institut National de Recherche en Sciences et Technologies du Num´erique (INRIA), bruno.salvy@inria.fr

April 6, 2026

Abstract

Let Hk = 1 + 1/2 + 1/3 + · · · + 1/k denote the kth harmonic number. We present an easy-toimplement algorithm for the computation of explicit closed-form evaluations, in terms of the digamma and polygamma functions, for Euler sums of the form

∞

R(k)Hk, (1)

k=1

where R(k) is a rational function (quotient of two polynomials) whose denominator degree is at least two larger than the numerator degree. We apply the same method to show how the computation of a general formula for Euler sums of the form

∞

Hk (m1k + n1)p1(m2k + n2)p2

· · · (mrk + nr)pr

k=1

reduces to partial fraction decomposition. We present explicit formulae for sums with one or two terms in the denominator, with powers pi ranging up to 3, and with multipliers mi ranging up to 4. We also include results for related Euler sums such as

∞

kqHk (mk + n)p

.

k=1

Computation of Euler sums directly to very high precision enables us to rigorously check the abovementioned formulas in many specific cases.

### 1 Introduction

An Euler sum (also termed Euler-Zagier sum or merely harmonic sum) is an infinite series involving the harmonic numbers Hk = 1 + 1/2 + 1/3 + ··· + 1/k. A few simple examples include ∞k=1 Hk/k2,

∞ k=1 Hk2/k3, ∞k=1 Hk/(3k + 2)3 and ∞k=1 kj=1 ji=1 1/(ijk). Such sums arise in mathematical

physics, in the study of the Riemann hypothesis and in numerous other contexts. They have been

studied since the time of Euler, and more recently in [1, 2, 5, 8, 10, 12, 16, 17]. One notable feature of these sums is that many have surprisingly elegant analytic evaluations, for example:

∞

Hk k3

=

k=1

∞

Hk (k + 1)5

=

k=1

∞

Hk3 k4

=

k=1

∞

Hk (k + 1)7

=

k=1

5 4

1 72

π4

ζ(4) =

1 4

1 1260

3ζ(6) − 2ζ(3)2 =

π6 − 630ζ(3)2

693 48

51 4

ζ(7) + 2ζ(5)ζ(2) −

1 4

(5ζ(8) − 4ζ(3)ζ(5)) =

ζ(4)ζ(3)

1 4

π8 1890 − 4ζ(3)ζ(5) .

In an earlier study [7], we presented results for mixed-denominator Euler sums of the form

∞

Hkm kn0(k + 1)n1(k + 2)n2

, (2)

···(k + t)nt

k=1

for nonnegative integers m and (ni), with m ≥ 1 and n0 + n1 + ··· + nt ≥ 2. We showed that these have closed-form evaluations in terms of the Riemann zeta function, at least when m+n0 +···+nt ≤ 12. We also presented a catalog of several hundred formulas, produced using high-precision numerical methods.

In this article, we illustrate a general approach, based on residues, to evaluate sums of the form

∞

R(k)Hk,

k=1

where R(k) is any rational function with denominator degree at least two larger than the numerator degree, and no poles at integers except possibly at 0. This leads to explicit formulas and techniques for sums such as

∞

Hk (m1k + n1)p1(m2k + n2)p2

···(mrk + nr)pr

k=1

and

∞

kqHk (m1k + n1)p1

k=1

for arbitrary (mi,ni,pi,q), provided the sum is convergent. We present explicit formulae, expressed in terms of the digamma and polygamma functions, for sums with one or two terms in the denominator, with powers pi ranging up to 3, and with multipliers mi ranging up to 4.

### 2 Formulas by residue computation

#### 2.1 Background on the ψ function

The ψ function (also known as the digamma function) is the logarithmic derivative of the gamma function: ψ(z) = Γ′(z)/Γ(z). Many formulas for ψ follow by differentiation from the recurrence formula Γ(s + 1) = sΓ(s), the reflection formula Γ(s)Γ(1 − s) = π/sin(πs) and the duplication formula Γ(2s) = π−1/222s−1Γ(s)Γ(s + 1/2), as well as its generalization known as Gauss’ multiplication formula, see [11, ch. 5]. In particular, this last formula gives values of ψ(p/q) at rational points [11, 5.4.19].

The ψ function is meromorphic (i.e., analytic except for a discrete set of poles), with simple poles at nonpositive integers. In a neighborhood of s = 0, it possesses the expansion [11, 5.5.2 and 5.7.4]

1 s −

ψ(−s) + γ =

ζ(k)sk−1, (3)

k≥2

where γ = 0.5772156649... is Euler’s constant and ζ(k) = 1 + 1/2k + 1/3k + ··· is the Riemann zeta function. The ψ function is closely related to the harmonic numbers: A direct consequence of the recurrence formula for Γ is that for n a positive integer, ψ(n + 1) = Hn − γ.

The polygamma function is merely the n-th derivative of the digamma function: ψ(n)(z), also denoted ψn(z) or ψ(n,z); note that ψ(z) = ψ0(z) = ψ(0,z). For positive integer n, the polygamma function can be written in terms of the Hurwitz zeta function as ψ(n)(z) = (−1)n+1n!ζ(n + 1,z).

Some interesting special values of the digamma and polygamma functions include [9]: ψ(1/2) = −γ − 2log 2 ψ(1/4) = −γ − 3log(2) − π/2

- ψ(1)(1) = π2/6 ψ(1)(1/2) = π2/2
- ψ(2)(1) = −2ζ(3) ψ(2)(1/2) = −14ζ(3)


ψ(2)(1/4) = −2π3 − 56ζ(3) ψ(3)(1/2) = π4 (4)

- 2.2 Harmonic sums by residue computation An interesting consequence of the behavior of ψ in the neighborhood of negative integers is the following:


Proposition 1. Let R(z) be a rational function (quotient of two polynomials) that is O(z−2) at infinity with no poles at integers except possibly at 0. Then

∞

- 1

- 2 α pole of R(s)


Res R′(s)(ψ(−s) + γ) − R(s)(ψ(−s) + γ)2 s=α , (5)

R(k)Hk =

k=1

where Res[Q(s)]s=α denotes the residue, in the complex analysis sense, of the function Q(s) at s = α. Proof. This is a direct corollary of [12, Eqs. (2-6) and (2-9)]:

∞

2

r(k)Hk +

k=1

∞

r(k) = −R[r(s)(ψ(−s) + γ)],

k=1

∞

r′(k) = −R[r(s)(ψ(−s) + γ)2],

k=1

where R[r(s)ξ(s)] with ξ ∈ {ψ(−s) + γ,(ψ(−s) + γ)2} denotes the sum of the residues of r(s)ξ(s) at the poles of r(s) and at 0.

Combining these two formulas gives the sum in the proposition. With this combination, the pole at 0 does not need to be considered separately: if R(s) does not have a pole at 0, then from Eq. (3) and its derivative, we get

−R(s)(ψ(0,−s) + γ)2 = −R(0)/s2 − R′(0)/s + O(1),

R′(s)(ψ(0,−s) + γ) = R′(0)/s + O(1). Thus the residue at 0, namely the coefficient of 1/s, is 0.

| |
|---|


- Example 1. We first illustrate the algorithm that follows from Proposition 1 for the rational function R(s) = 1/(2s − 1)2. Its only pole is at α = 1/2. At this point, we use the expansion


π2 2

+ 4 (s − 1/2) + (8 − 7ζ(3))(s − 1/2)2 + O((s − 1/2)3).

ψ(−s) + γ = 2(1 − ln2) −

It follows that the residues of −R(s)(ψ(−s) + γ)2 and R′(s)(ψ(−s) + γ) at s = 1/2 are

π2 2

7 2

(1 − ln2)

ζ(3) − 4,

+ 4 and

Algorithm HarmonicSum: Sum harmonic number times rational function Input: R = P/Q a rational function

with P,Q in Q[s], gcd(P,Q) = 1, deg Q − deg P ≥ 2 and 0 ̸∈ Q(N \ {0})

Output: k≥1 R(k)Hk, where Hk is the kth harnomic number qe

mm := factor(Q) // ei > 0, qi ∈ Q[s] irreducible for i := 1 to m do // loop over factors

1 ···qe

1

r := Rqe

i

i // rest of the fraction q := (qi(s) − qi(α))/(s − α) ∈ Q(α)[s] // α stands for the pole S := Taylor(r/q,s = α,ei + 1) // Taylor expansion modulo O((s − α)e

i+1) S := Laurent(S/(s − α)e

,s = α,1) // Laurent expansion of R modulo O(s − α) S := Laurent((ψ(−s) + γ)S′ − (ψ(−s) + γ)2S,s = α,0) // expansion modulo O((s − α)0) c := coeff(S,s − α,−1) // residue from Proposition 1

i

vi := 21 α|q

i(α)=0 c // sum over conjugate roots of qi return mi=1 vi. // sum the contributions from all poles

which gives

∞

Hk (2k − 1)2

=

k=1

π2 4 − 2ln2 −

π2 ln2 4

+

7 4

ζ(3).

#### 2.3 Algorithm

When turning Proposition 1 into an algorithm suitable for implementation in a computer algebra system, it is important to observe that exact or approximate expressions of the poles of R(s) are not needed for the computation of the residues; they can be obtained in a purely symbolic way. Assume that R(s) = P(s)/Q(s) with P,Q polynomials that are relatively prime (this can ensured by reducing the fraction to a common denominator and dividing numerator and denominator by their gcd). If α is a root of Q of multiplicity p ∈ N, then the Taylor expansion of Q(s) as s → α factors as

Q(p)(α) p!

Q(p+1)(α) (p + 1)!

Q(s) = (s − α)p

(s − α) + ··· .

+

Then computing the Taylor expansions of P(s), ψ(−s) + γ and the reciprocal of the second term in the product above, all at precision O((s − α)p+1) is sufficient to recover the residues required by the lemma.

From the computer algebra point of view, a natural strategy is to start from a square-free factor-

ization of Q, ie, a factorization of the form Q = Q1Q22 ···Qrr where the polynomials Qi do not have multiple roots and are relatively prime. Such a factorization can be computed efficiently using only gcd

computations [13, §14.6]. Then, for each p = 1,...,r, one computes a residue as described above for Qp and sums the result symbolically over all roots of Qp. This approach completely avoids factorization and is usually the preferred one in computer algebra algorithms.

However, for users whose rational functions R(s) have simple expressions in Q(s), more explicit formulas are obtained by first factoring the denominator into irreducible factors in Q[s] and then proceeding as above. This is the choice made in our implementation presented in Appendix A and results in Algorithm HarmonicSum.

- Example 2. With our Maple implementation, the previous example is obtained as > expand(harmonicsum(1/(2*k-1)^2,k));


7ζ(3) 4

+

π2 4 − 2ln(2) −

ln(2)π2 4

- Example 3. Here is an example with multiple poles ∞

k=1

Hk (2k + 1)3(3k + 1)2

.

Our implementation provides the following nice expression > expand(harmonicsum(1/(2*k+1)^3/(3*k+1)^2,k));

π4 16

+ 42ζ(3) +

27π2 2 − 7ln(2)ζ(3) − 6ln(2)π2 − 108ln(2)2

+ 27 −

π√3 6 −

3ln(3) 2

2

+ −27 −

π√3 2 −

9ln(3) 2

ψ′

1 3 −

3 2

ψ′′

1 3

- Example 4. An example that would be more involved by hand is ∞


Hk (k2 + 3k + 1)2

k=1

which is obtained as > harmonicsum(1/(k^2+3*k+1)^2,k);

2√5γψ 32 +

√5ψ 2 3 +

√5 2

√5 2

√5

√5 2

2

2 ψ 32 +

ψ′ 32 +

25 −

−

+

25

5

√5ψ −

2√5γψ −

√5

√5

√5

√5

2

2 + 32

2 + 23 25

2 + 23 ψ −

2 + 23 5

ψ′ −

+

+

+

25

√5

√5 2

2 + 23 10 −

ψ′′ 32 +

ψ′′ −

−

10

√5 25

√5 2

√5 25

γ 5

3 2

γ 5

ψ′ −

ψ′

+ −

+

+

+

+

√5 2

3 2

+

### 3 General formulas

Algorithm HarmonicSum can deal with an arbitrary rational function R(s) ∈ Q(s), provided the sum converges. It can easily be extended to parameterized rational functions in, say, Q(a1,...,am)(s) for parameters a1,...,am. While it cannot handle poles whose order is a parameter, the method used by the algorithm can be “run by hand” and produce similar formulas in that case. But for relatively simple R(s), useful general formulas can be derived, as we will show in the following.

#### 3.1 Simple poles

The computation of the contribution of a simple pole of R to the sum in Eq. (5) is straightforward. If R(s) = P(s)/Q(s) with P,Q polynomials that are relatively prime (this can be checked by a gcd computation), then as s → α,

cα (s − α)2

cα s − α

+ O(1), R′(s) = −

+ O(1), ψ(−s) + γ = ψ(−α) + γ − ψ′(−α)(s − α) + O((s − α)2),

R(s) =

with cα = P(α)/Q′(α). As a consequence,

Res R′(s)(ψ(−s) + γ) − R(s)(ψ(−s) + γ)2 s=α = cα(ψ′(−α) − (ψ(−α) + γ)2). Using partial fraction decomposition then gives the following.

- Theorem 1. For t not an integer, define

T(t,1) =

- 1

- 2


ψ′(t) − 2γψ(t) − ψ(t)2 . (6)

Let (t1,t2,··· ,tr), with r ≥ 2, be distinct nonintegers, and let (C1,C2,··· ,Cr) be complex numbers that satisfy C1 + C2 + ··· + Cr = 0 (necessary for convergence). Then

∞

k=1

Hk

C1 k + t1

+

C2 k + t2

+ ··· +

Cr k + tr

=

r

j=1

CjT(tj,1). (7)

Proof. The discussion above gives the result with (ψ′(t) − (ψ(t) + γ)2)/2 in place of T(t,1). The disappearance of the term γ2 comes from the sum of the Cj being 0.

| |
|---|


Example 5. In this example, the denominator has complex roots:

∞

k=1

Hk k3 + 1

. (8)

Let −1 and c± = (1 ± i√3)/2 be the cubic roots of −1, so that (k + 1)(k − c+)(k − c−) = k3 + 1. A partial fraction decomposition yields

1 k3 + 1

=

1 3(k + 1) −

c+ 3(k − c+) −

c− 3(k − c−)

. (9)

Recall that ψ(1) = −γ and ψ′(1) = π2/6. Then

∞

k=1

Hk k3 + 1

=

1 3

T(1,1) −

c+ 3

T(−c+,1) −

c− 3

T(−c−,1)

=

1 6

 π2

6

+ γ2 −

ϵ∈{+,−}

cϵ(ψ′(−cϵ) − 2γψ(−cϵ) − ψ(−cϵ)2)

 

= 0.828902143400992508742....

3.2 A unique pole of higher order

The next theorem is a variant of a formula that we initially discovered experimentally, using a combination of Wolfram Mathematica, the Online Encyclopedia of Integer Sequences [15] and high-precision numerical computing.

- Theorem 2. For t not an integer, and integer p ≥ 1, define


p−1

(−1)p−1 2(p − 1)!

ψ(p)(t) − 2γψ(p−1)(t) −

T(t,p) =

k=0

p − 1 k

ψ(k)(t)ψ(p−1−k)(t) . (10)

Then, for p ≥ 2,

∞

Hk (k + t)p

= T(t,p). (11)

k=1

Note that the value of T(t,p) in Eq. (10) is consistent with the value of T(t,1) in Theorem 1. Proof. We apply Proposition 1 to R(s) = 1/(s + t)p, whose only pole is at s = −t.

From R′(s) = −p/(s + t)p+1 and the Taylor expansion at s = −t

ψ(k)(t) k!

(−1)k

(s + t)k (12)

ψ(−s) + γ = ψ(t) + γ +

k≥1

it follows that

ψ(p)(t) (p − 1)!

Res[R′(s)(ψ(−s) + γ)]s=−t = (−1)p−1

. Next, squaring the expansion above and extracting the coefficient of (s + t)p−1 gives

(−1)p−1 (p − 1)!

Res[R(s)(ψ(−s) + γ)2]s=−t =

Summing both contributions gives the result.

p−1

2γψ(p−1)(t) +

k=0

p − 1 k

ψ(k)(t)ψ(p−1−k)(t) .

| |
|---|


Note that the summation in the last line of Eq. (5) is symmetric. Thus it suffices to sum it only halfway, doubling each summand except possibly the middle one.

One direct consequence of Theorem 2 is the following:

- Corollary 1. For integers m,n ≥ 1,gcd(m,n) = 1,p ≥ 2,

∞

k=1

Hk (mk + n)p

=

(−1)p−1 2mp(p − 1)!

ψ(p)

n m − 2γψ(p−1)

n m −

p−1

k=0

p − 1 k

ψ(k)

n m

ψ(p−1−k)

n m

.

(13) Proof. This follows from Theorem 2 after setting t = n/m.

| |
|---|


Numerous examples of Theorem 2 and Corollary 1 are presented in Appendix B.

3.3 Mixed denominators

Combining the residues at each pole finally gives the following general result. Theorem 3. Let Ci,j be the coefficients of the partial fraction decomposition

R(k) =

r

j=1

pj

i=1

Ci,j (k + tj)i

, (14)

with distinct tj, Cp

j,j ̸= 0 and integers pj ≥ 1 whose sum is at least 2. Then

∞

k=1

R(k)Hk =

r

j=1

pj

i=1

Ci,jT(tj,i), (15)

with T the function from Eq. (10). As a typical illustration, here is an extension of Theorem 3.

- Corollary 2. For integers m,n ≥ 1,gcd(m,n) = 1,q ≥ 1 and p ≥ q + 2, and for the T notation as defined in Eq. (10),


∞

kqHk (mk + n)p

=

k=1

q

1 mp

(−1)j

j=0

q j

n m

j

T

n m

,p − q + j .

Proof. By Theorem 3, it is sufficient to compute the coefficients of the partial fraction decomposition of kq/(mk + n)p with respect to k. The result then follows from

kq (mk + n)p

m−pkq (k + n/m)p

=

=

m−p (k + n/m)p−q 1 −

n/m k + n/m

q

q

= m−p

(−1)j

j=0

q j

(n/m)j (k + n/m)p−q+j .

| |
|---|


- Example 6. Example 3 can be computed by hand from the partial fraction decomposition


1 (2k + 1)3(3k + 1)2

4 (2k + 1)3

=

24 (2k + 1)2

+

+

108 2k + 1

+

162 3k + 1

27 (3k + 1)2 −

,

which is easy to compute and even easier to check. Numerous other examples of Theorem 3 are presented in Appendix B.

### 4 Numerical computation of mixed-denominator Euler sums

The research leading to the results in the previous section relied on direct high-precision numerical evaluations of specific Euler sums, combined with an integer relation computation to produce the coefficients of the right-hand side terms. Also, even with the above results in hand, we have found that it is often easier to use numerical methods to obtain the formulas. In fact, the catalog of formulas in Appendix B was obtained by this process, after checking in each case that the numerical value matches the result given by the above theorems to high precision.

The numerical scheme we employed here is a variation of a scheme described in [7]. In very brief summary, the overall strategy is to compute a large number (108) terms of the Euler sum explicitly to high precision, then employ the Euler-Maclaurin summation formula [3, pg. 285] twice to sum the tail of the series. The specific algorithm we employed resulted in an approximation correct to within roughly 10−290. In our implementation, computed results were typically accurate to roughly 280 digits.

Once a high-precision numerical value was obtained, we employed the multipair PSLQ integer relation algorithm [6], applied to the numerical values of the sum and the hypothesized right-hand side constants, to obtain the rational coefficients in the catalogued formulas below.

### 5 Computing digamma and polygamma

The formulas given above involve Euler’s constant, the digamma function and the polygamma function. Maple and Mathematica can evaluate these to arbitrary precision, but not all researchers have access to this commercial software, and others may wish to explore these relations with custom code.

In our computations, we employed formulas and algorithms presented in [4], to which the reader is referred for full details. In very brief summary, we employed this scheme for digamma: For a modest value of x, first apply the recursion ψ(x+1) = ψ(x)+1/x, repeating 0.45B times, where B is the working precision in bits, to shift the argument to a larger value. Then employ this formula [11, 5.11.2]:

n

- 1

- 2x −


ψ(x) ≈ log(x) −

k=1

B2k 2kx2k

, (16)

where n = 2D, D is the precision in digits, and {B2k} is a set of precomputed even Bernoulli numbers.

A similar scheme for polygamma is the following: For ψ(q)(z) with integer q ≥ 1, first reduce z to the range (0,1] by applying the recurrence ψ(q)(z) = ψ(q)(z + 1) − (−1)qq!z−q−1. Then polygamma can be evaluated from the Hurwitz zeta function via the formula [14] ψ(q)(z) = (−1)q+1q!ζ(q + 1,z). To

compute the Hurwitz zeta function, select an integer q > 0.6D, where D is the precision in digits. Let n = 2D as above. Then

q−1

ζ(s,a) ≈

k=0

1 (a + k)s

+

1 (s − 1)(a + q)s−1 +

1 2(a + q)s

n

B2k s(s + 1)···(s + 2k − 2) (2k)!(a + q)s+2k−1 . (17)

+

k=1

The above algorithms require a precomputed set of even Bernoulli numbers B2k of size n. These can be computed efficiently by a scheme presented in [4].

### 6 Conclusion

In this paper, we have presented explicit formulas and techniques for analytically evaluating Euler sums of a general class, namely sums of the form ∞k=1 R(k)Hk, where R(k) is any rational function whose denominator degree is at least two greater than the numerator degree. We have also briefly presented computational techniques to compute these sums numerically to very high precision, which enabled us to confirm the analytic formulas in hundreds of specific cases.

One fair question here is whether the analytic formulas given by the above theorems truly add value: Don’t they just replace one summation (the left-hand side) with several more (one for each digamma and polygamma function evaluation)? The key fact here is that digamma and polygamma function evaluations, if performed using the fast algorithms mentioned in Section 5, are typically many times faster than evaluating Euler sums directly using the method given in Section 4. For example, we found that numerically evaluating the Euler sum ∞k=1 Hk/(3k+2)4 = 0.002220075526... to 280-digit precision using the fast digamma and polygamma formulas was approximately 30,000 times faster than using the direct scheme.

So there is value in these formulas beyond mere mathematical elegance. Also, the results presented here may be of use in accelerating sums with a leading term of logarithmic form in the summand numerator.

In any event, it is clear there is still much that can be done. For example, using other residue representations, one can obtain an algorithm along the lines of Algorithm HarmonicSum for many sums of the types

∞

Hk2 (mk + n)p

,

k=1

∞

(−1)kHk (mk + n)p

,

k=1

∞

H2k (mk + n)p

, (18)

k=1

for positive integers m ≥ 3,gcd(m,n) = 1 and p ≥ 2.

### References

- [1] J. Ablinger, “A computer algebra toolbox for harmonic sums related to particle physics,” Johannes Kepler University, 2009, available at https://inspirehep.net/literature/875721.
- [2] J. Ablinger, J. Bluemlein and C. Schneider, “Harmonic sums and polylogarithms generated by cyclotomic polynomials,” Journal of Mathematical Physics, 52 (2011), 102301.
- [3] Kendall E. Atkinson. 1990. An Introduction to Numerical Analysis, 2nd ed., John Wiley and Sons, New York.
- [4] D.H. Bailey, “MPFUN2020: A thread-safe arbitrary precision package with special functions,” 5 Dec 2025, available at https://www.davidhbailey.com/dhbpapers/mpfun2020.pdf.
- [5] D.H. Bailey, J.M. Borwein and R. Girgensohn, “Experimental evaluation of Euler sums,” Experimental Mathematics, 3 (1994), 17–30.


- [6] D.H. Bailey and D.J. Broadhurst, “Parallel integer relation detection: Techniques and applications,” Mathematics of Computation, 70 (2000), 1719–1736.
- [7] D.H. Bailey and R.C. McPhedran, “New results for Euler sums,” arXiv:2311.06294, Jul 2025, https: //arxiv.org/abs/2311.06294.
- [8] D. Borwein, J.M. Borwein and R. Girgenshon, “Explicit evaluation of Euler sums,” Proceedings of the Edinburgh Mathematical Society, 38 (1995), 277–294.
- [9] J. Choi and D. Cvijovi´c, “Values of the polygamma functions at rational arguments,” Journal of Physics A: Mathematical and Theoretical, 40 (2007), 15019.
- [10] J. Choi and H.M. Srivastava, “Some summation formulas involving harmonic numbers and generalised harmonic numbers,” Mathematical and Computer Modeling, 54 (2011), 220–2234.
- [11] “Digital library of mathematical functions,” National Institute of Standards and Technology, 2015, http://dlmf.nist.gov.
- [12] Philippe Flajolet and Bruno Salvy, “Euler sums and contour integral representations,” Experimental Mathematics, vol. 7 (1998), 15–35.
- [13] Joachim von zur Gathen and Ju¨rgen Gerhard, 2013. Modern Computer Algebra, 3rd ed., Cambridge University Press, New York.
- [14] “Polygamma function,” Wikipedia article, viewed 31 Dec 2025, https://en.wikipedia.org/wiki/ Polygamma function.

- [15] N.J.A. Sloane, The On-Line Encyclopedia of Integer Sequences (OEIS), viewed 13 Dec 2025, https: //oeis.org.
- [16] A. Sofo and J. Choi, “Linear harmonic Euler sums of even weight,” Journal of Mathematical Analysis and Applications, 553 (2026), 129926.
- [17] D-Y. Zheng, “Further summation formulae related to generalized harmonic numbers,” Journal of Mathematical Analysis and Applications, 335 (2007), 692–706.


### A Maple code for Algorithm HarmonicSum

The Maple code below has been successfully tested on the examples of this article. We have also translated this code into Mathematica, using one of the currently available large language models (LLMs), and found that the resulting code passed a similar set of tests. But in general one should be cautious with such translations, since the handling of algebraic numbers can be very different in different computer algebra systems, and, based on our experience, not all LLMs do this translation correctly.

# Input: # . R a rational function # . k its variable # Output: # $\sum_{k=1}^\infty{R(k)H_k}$, # where $H_k$ is the $k$th harnomic number $1+1/2+\dots+1/k$. harmonicsum:=proc(R,k) local r,numr,denr,ker,facts,factmult,fact,pole,rest,restfact,S,res,val,mult,expansionr,alpha;

r:=normal(R); # reduce to the same denominator numr:=numer(r); denr:=denom(r); if degree(denr,k)-degree(numr,k)<-2 then error "sum not convergent" fi; ker:=Psi(-k)+gamma; facts:=factors(denr)[2]; for factmult in facts do # deal with factors of the denominator one by one

fact,mult:=op(factmult); # factor and multiplicity pole:=RootOf(fact,k); if type(pole,posint) then error "infinite summand" fi; rest:=normal(r*fact^mult); # expansion of $r$ at the pole restfact:=subs(alpha=pole,series((fact-eval(fact,k=alpha))/(k-alpha),k=alpha,mult+1)); expansionr:=series(rest/restfact^mult/(k-pole)^mult,k=pole,mult+1); # simplify coefficients for nonrational poles if has(pole,RootOf) then expansionr:=map(evala,expansionr) fi; # expansion of $r’(k)(\psi(-k)+\gamma)-r(k)(\psi(-k)+\gamma)^2$ at this pole S:=series(diff(expansionr,k)*ker-expansionr*ker^2,k=pole,mult+1); # extract residue res:=coeff(S,k-pole,-1)/2; # sum over all conjugate roots of this factor if has(res,RootOf) then val[factmult]:=convert([allvalues(res)],‘+‘) else val[factmult]:=res fi

od; collect(add(val[factmult],factmult=facts),Psi,’distributed’)

end:

### B Catalog of formulas

We present here a selection of formulas that we have produced according to the above techniques. In each case, we computed the Euler sum numerically in two ways: (a) by applying the theorems of Section

- 3, together with the numerical algorithms given in Section 5, and (b) by the direct scheme described in Section 4. After verifying that the two numerical values were in agreement, the multipair PSLQ algorithm, applied to the computed value and the hypothesized right-hand side constants, then found the rational coefficients and generated the formulas below.


To guard against the possibility of transcription errors, the LaTeX code for these formulas was produced by a program directly from the computer output, and is included here without any alteration.

#### B.1 Theorem 2 (Corollary 1) formulas

∞

1 8

Hk (2k + 1)2

(−1ψ(2,1/2) + 2γψ(1,1/2) + 2ψ(0,1/2)ψ(1,1/2)) (19)

=

k=1

∞

1 16

Hk (2k + 1)3

(−1γψ(2,1/2) − 1ψ(0,1/2)ψ(2,1/2) + 1ψ(1,1/2)ψ(1,1/2)) (20)

=

k=1

∞

1 192

Hk (2k + 1)4

(−1ψ(4,1/2) + 2γψ(3,1/2) + 2ψ(0,1/2)ψ(3,1/2) + 6ψ(1,1/2)ψ(2,1/2)) (21)

=

k=1

∞

1 15360

Hk (2k + 1)6

(−1ψ(6,1/2) + 2γψ(5,1/2) + 2ψ(0,1/2)ψ(5,1/2) + 10ψ(1,1/2)ψ(4,1/2)

=

k=1

+20ψ(2,1/2)ψ(3,1/2)) (22)

∞

1 368640

Hk (2k + 1)7

(1ψ(7,1/2) − 4γψ(6,1/2) − 4ψ(0,1/2)ψ(6,1/2) − 60ψ(2,1/2)ψ(4,1/2)) (23)

=

k=1

∞

Hk (2k + 1)8

1 2580480

(−1ψ(8,1/2) + 2γψ(7,1/2) + 2ψ(0,1/2)ψ(7,1/2) + 14ψ(1,1/2)ψ(6,1/2)

=

k=1

+42ψ(2,1/2)ψ(5,1/2) + 70ψ(3,1/2)ψ(4,1/2)) (24)

∞

Hk (3k + 1)2

1 18

(−1ψ(2,1/3) + 2γψ(1,1/3) + 2ψ(0,1/3)ψ(1,1/3)) (25)

=

k=1

∞

Hk (3k + 1)3

1 108

(1ψ(3,1/3) − 2γψ(2,1/3) − 2ψ(0,1/3)ψ(2,1/3) − 2ψ(1,1/3)ψ(1,1/3)) (26)

=

k=1

∞

Hk (3k + 1)4

1 972

(−1ψ(4,1/3) + 2γψ(3,1/3) + 2ψ(0,1/3)ψ(3,1/3) + 6ψ(1,1/3)ψ(2,1/3)) (27)

=

k=1

∞

Hk (3k + 1)5

1 11664

(1ψ(5,1/3) − 2γψ(4,1/3) − 2ψ(0,1/3)ψ(4,1/3) − 8ψ(1,1/3)ψ(3,1/3)

=

k=1

−6ψ(2,1/3)ψ(2,1/3)) (28)

∞

Hk (3k + 1)6

1 174960

(−1ψ(6,1/3) + 2γψ(5,1/3) + 2ψ(0,1/3)ψ(5,1/3) + 10ψ(1,1/3)ψ(4,1/3)

=

k=1

+20ψ(2,1/3)ψ(3,1/3)) (29)

∞

Hk (3k + 1)7

1 3149280

(1ψ(7,1/3) − 2γψ(6,1/3) − 2ψ(0,1/3)ψ(6,1/3) − 12ψ(1,1/3)ψ(5,1/3)

=

k=1

−30ψ(2,1/3)ψ(4,1/3) − 20ψ(3,1/3)ψ(3,1/3)) (30)

∞

1 66134880

Hk (3k + 1)8

(−1ψ(8,1/3) + 2γψ(7,1/3) + 2ψ(0,1/3)ψ(7,1/3) + 14ψ(1,1/3)ψ(6,1/3)

=

k=1

+42ψ(2,1/3)ψ(5,1/3) + 70ψ(3,1/3)ψ(4,1/3)) (31)

1 18

Hk (3k + 2)2

(−1ψ(2,2/3) + 2γψ(1,2/3) + 2ψ(0,2/3)ψ(1,2/3)) (32)

=

k=1

∞

1 108

Hk (3k + 2)3

(1ψ(3,2/3) − 2γψ(2,2/3) − 2ψ(0,2/3)ψ(2,2/3) − 2ψ(1,2/3)ψ(1,2/3)) (33)

=

k=1

∞

1 972

Hk (3k + 2)4

(−1ψ(4,2/3) + 2γψ(3,2/3) + 2ψ(0,2/3)ψ(3,2/3) + 6ψ(1,2/3)ψ(2,2/3)) (34)

=

k=1

∞

1 11664

Hk (3k + 2)5

(1ψ(5,2/3) − 2γψ(4,2/3) − 2ψ(0,2/3)ψ(4,2/3) − 8ψ(1,2/3)ψ(3,2/3)

=

k=1

−6ψ(2,2/3)ψ(2,2/3)) (35)

∞

1 174960

Hk (3k + 2)6

(−1ψ(6,2/3) + 2γψ(5,2/3) + 2ψ(0,2/3)ψ(5,2/3) + 10ψ(1,2/3)ψ(4,2/3)

=

k=1

+20ψ(2,2/3)ψ(3,2/3)) (36)

∞

Hk (3k + 2)7

1 3149280

(1ψ(7,2/3) − 2γψ(6,2/3) − 2ψ(0,2/3)ψ(6,2/3) − 12ψ(1,2/3)ψ(5,2/3)

=

k=1

−30ψ(2,2/3)ψ(4,2/3) − 20ψ(3,2/3)ψ(3,2/3)) (37)

∞

Hk (3k + 2)8

1 66134880

(−1ψ(8,2/3) + 2γψ(7,2/3) + 2ψ(0,2/3)ψ(7,2/3) + 14ψ(1,2/3)ψ(6,2/3)

=

k=1

+42ψ(2,2/3)ψ(5,2/3) + 70ψ(3,2/3)ψ(4,2/3)) (38)

∞

Hk (4k + 1)2

1 32

(−1ψ(2,1/4) + 2γψ(1,1/4) + 2ψ(0,1/4)ψ(1,1/4)) (39)

=

k=1

∞

Hk (4k + 1)3

1 256

(1ψ(3,1/4) − 2γψ(2,1/4) − 2ψ(0,1/4)ψ(2,1/4) − 2ψ(1,1/4)ψ(1,1/4)) (40)

=

k=1

∞

Hk (4k + 1)4

1 3072

(−1ψ(4,1/4) + 2γψ(3,1/4) + 2ψ(0,1/4)ψ(3,1/4) + 6ψ(1,1/4)ψ(2,1/4)) (41)

=

k=1

∞

Hk (4k + 1)5

1 49152

(1ψ(5,1/4) − 2γψ(4,1/4) − 2ψ(0,1/4)ψ(4,1/4) − 8ψ(1,1/4)ψ(3,1/4)

=

k=1

−6ψ(2,1/4)ψ(2,1/4)) (42)

∞

1 983040

Hk (4k + 1)6

(−1ψ(6,1/4) + 2γψ(5,1/4) + 2ψ(0,1/4)ψ(5,1/4) + 10ψ(1,1/4)ψ(4,1/4)

=

k=1

+20ψ(2,1/4)ψ(3,1/4)) (43)

∞

Hk (4k + 1)7

1 23592960

(1ψ(7,1/4) − 2γψ(6,1/4) − 2ψ(0,1/4)ψ(6,1/4) − 12ψ(1,1/4)ψ(5,1/4)

=

k=1

−30ψ(2,1/4)ψ(4,1/4) − 20ψ(3,1/4)ψ(3,1/4)) (44)

1 660602880

Hk (4k + 1)8

(−1ψ(8,1/4) + 2γψ(7,1/4) + 2ψ(0,1/4)ψ(7,1/4) + 14ψ(1,1/4)ψ(6,1/4)

=

k=1

+42ψ(2,1/4)ψ(5,1/4) + 70ψ(3,1/4)ψ(4,1/4)) (45)

∞

1 32

Hk (4k + 3)2

(−1ψ(2,3/4) + 2γψ(1,3/4) + 2ψ(0,3/4)ψ(1,3/4)) (46)

=

k=1

∞

1 256

Hk (4k + 3)3

(1ψ(3,3/4) − 2γψ(2,3/4) − 2ψ(0,3/4)ψ(2,3/4) − 2ψ(1,3/4)ψ(1,3/4)) (47)

=

k=1

∞

1 3072

Hk (4k + 3)4

(−1ψ(4,3/4) + 2γψ(3,3/4) + 2ψ(0,3/4)ψ(3,3/4) + 6ψ(1,3/4)ψ(2,3/4)) (48)

=

k=1

∞

1 49152

Hk (4k + 3)5

(1ψ(5,3/4) − 2γψ(4,3/4) − 2ψ(0,3/4)ψ(4,3/4) − 8ψ(1,3/4)ψ(3,3/4)

=

k=1

−6ψ(2,3/4)ψ(2,3/4)) (49)

∞

Hk (4k + 3)6

1 983040

(−1ψ(6,3/4) + 2γψ(5,3/4) + 2ψ(0,3/4)ψ(5,3/4) + 10ψ(1,3/4)ψ(4,3/4)

=

k=1

+20ψ(2,3/4)ψ(3,3/4)) (50)

∞

Hk (4k + 3)7

1 23592960

(1ψ(7,3/4) − 2γψ(6,3/4) − 2ψ(0,3/4)ψ(6,3/4) − 12ψ(1,3/4)ψ(5,3/4)

=

k=1

−30ψ(2,3/4)ψ(4,3/4) − 20ψ(3,3/4)ψ(3,3/4)) (51)

∞

Hk (4k + 3)8

1 660602880

(−1ψ(8,3/4) + 2γψ(7,3/4) + 2ψ(0,3/4)ψ(7,3/4) + 14ψ(1,3/4)ψ(6,3/4)

=

k=1

+42ψ(2,3/4)ψ(5,3/4) + 70ψ(3,3/4)ψ(4,3/4)) (52)

#### B.2 Theorem 3 formulas

∞

Hk (2k + 1)(3k + 1)

k=1

∞

Hk (2k + 1)(3k + 1)2

k=1

∞

Hk (2k + 1)(3k + 1)3

k=1

∞

Hk (2k + 1)(3k + 2)

k=1

∞

Hk (2k + 1)(3k + 2)2

k=1

∞

Hk (2k + 1)(3k + 2)3

k=1

∞

Hk (2k + 1)(4k + 1)

k=1

∞

Hk (2k + 1)(4k + 1)2

k=1

∞

Hk (2k + 1)(4k + 1)3

k=1

∞

Hk (2k + 1)(4k + 3)

k=1

- 1

- 2


(−1ψ(1,1/2) + 2γψ(0,1/2) + 1ψ(0,1/2)ψ(0,1/2) + 1ψ(1,1/3) − 2γψ(0,1/3)

=

−1ψ(0,1/3)ψ(0,1/3)) (53)

= −1 6

(−6ψ(1,1/2) + 12γψ(0,1/2) + 6ψ(0,1/2)ψ(0,1/2) + 6ψ(1,1/3) − 12γψ(0,1/3)

−6ψ(0,1/3)ψ(0,1/3) + 1ψ(2,1/3) − 2γψ(1,1/3) − 2ψ(0,1/3)ψ(1,1/3)) (54)

= −1 36

(72ψ(1,1/2) − 144γψ(0,1/2) − 72ψ(0,1/2)ψ(0,1/2) − 72ψ(1,1/3) + 144γψ(0,1/3)

+72ψ(0,1/3)ψ(0,1/3) − 12ψ(2,1/3) + 24γψ(1,1/3) + 24ψ(0,1/3)ψ(1,1/3) −1ψ(3,1/3) + 2γψ(2,1/3) + 2ψ(0,1/3)ψ(2,1/3) + 2ψ(1,1/3)ψ(1,1/3)) (55)

- 1

- 2


(1ψ(1,1/2) − 2γψ(0,1/2) − 1ψ(0,1/2)ψ(0,1/2) − 1ψ(1,2/3) + 2γψ(0,2/3)

=

+1ψ(0,2/3)ψ(0,2/3)) (56)

= −1 6

(−6ψ(1,1/2) + 12γψ(0,1/2) + 6ψ(0,1/2)ψ(0,1/2) + 6ψ(1,2/3) − 12γψ(0,2/3)

−6ψ(0,2/3)ψ(0,2/3) − 1ψ(2,2/3) + 2γψ(1,2/3) + 2ψ(0,2/3)ψ(1,2/3)) (57)

= −1 36

(−72ψ(1,1/2) + 144γψ(0,1/2) + 72ψ(0,1/2)ψ(0,1/2) + 72ψ(1,2/3) − 144γψ(0,2/3)

−72ψ(0,2/3)ψ(0,2/3) − 12ψ(2,2/3) + 24γψ(1,2/3) + 24ψ(0,2/3)ψ(1,2/3)

+1ψ(3,2/3) − 2γψ(2,2/3) − 2ψ(0,2/3)ψ(2,2/3) − 2ψ(1,2/3)ψ(1,2/3)) (58)

= −1 4

(1ψ(1,1/2) − 2γψ(0,1/2) − 1ψ(0,1/2)ψ(0,1/2) − 1ψ(1,1/4) + 2γψ(0,1/4)

+1ψ(0,1/4)ψ(0,1/4)) (59)

= −1 16

(−4ψ(1,1/2) + 8γψ(0,1/2) + 4ψ(0,1/2)ψ(0,1/2) + 4ψ(1,1/4) − 8γψ(0,1/4)

−4ψ(0,1/4)ψ(0,1/4) + 1ψ(2,1/4) − 2γψ(1,1/4) − 2ψ(0,1/4)ψ(1,1/4)) (60)

= −1 128

(32ψ(1,1/2) − 64γψ(0,1/2) − 32ψ(0,1/2)ψ(0,1/2) − 32ψ(1,1/4) + 64γψ(0,1/4)

+32ψ(0,1/4)ψ(0,1/4) − 8ψ(2,1/4) + 16γψ(1,1/4) + 16ψ(0,1/4)ψ(1,1/4) −1ψ(3,1/4) + 2γψ(2,1/4) + 2ψ(0,1/4)ψ(2,1/4) + 2ψ(1,1/4)ψ(1,1/4)) (61)

= −1 4

(−1ψ(1,1/2) + 2γψ(0,1/2) + 1ψ(0,1/2)ψ(0,1/2) + 1ψ(1,3/4) − 2γψ(0,3/4)

−1ψ(0,3/4)ψ(0,3/4)) (62)

Hk (2k + 1)(4k + 3)2

k=1

∞

Hk (2k + 1)(4k + 3)3

k=1

∞

Hk (2k + 1)2(3k + 1)

k=1

∞

Hk (2k + 1)2(3k + 1)2

k=1

∞

Hk (2k + 1)2(3k + 1)3

k=1

∞

Hk (2k + 1)2(3k + 2)

k=1

∞

Hk (2k + 1)2(3k + 2)2

k=1

∞

Hk (2k + 1)2(3k + 2)3

k=1

∞

Hk (2k + 1)2(4k + 1)

k=1

1 16

(4ψ(1,1/2) − 8γψ(0,1/2) − 4ψ(0,1/2)ψ(0,1/2) − 4ψ(1,3/4) + 8γψ(0,3/4)

=

+4ψ(0,3/4)ψ(0,3/4) + 1ψ(2,3/4) − 2γψ(1,3/4) − 2ψ(0,3/4)ψ(1,3/4)) (63)

1 128

(32ψ(1,1/2) − 64γψ(0,1/2) − 32ψ(0,1/2)ψ(0,1/2) − 32ψ(1,3/4) + 64γψ(0,3/4)

=

+32ψ(0,3/4)ψ(0,3/4) + 8ψ(2,3/4) − 16γψ(1,3/4) − 16ψ(0,3/4)ψ(1,3/4) −1ψ(3,3/4) + 2γψ(2,3/4) + 2ψ(0,3/4)ψ(2,3/4) + 2ψ(1,3/4)ψ(1,3/4)) (64)

= −1 4

(6ψ(1,1/2) − 12γψ(0,1/2) − 6ψ(0,1/2)ψ(0,1/2) − 1ψ(2,1/2) + 2γψ(1,1/2)

+2ψ(0,1/2)ψ(1,1/2) − 6ψ(1,1/3) + 12γψ(0,1/3) + 6ψ(0,1/3)ψ(0,1/3)) (65)

= −1 2

(−12ψ(1,1/2) + 24γψ(0,1/2) + 12ψ(0,1/2)ψ(0,1/2) + 1ψ(2,1/2) − 2γψ(1,1/2)

−2ψ(0,1/2)ψ(1,1/2) + 12ψ(1,1/3) − 24γψ(0,1/3) − 12ψ(0,1/3)ψ(0,1/3)

+1ψ(2,1/3) − 2γψ(1,1/3) − 2ψ(0,1/3)ψ(1,1/3)) (66)

1 12

(−216ψ(1,1/2) + 432γψ(0,1/2) + 216ψ(0,1/2)ψ(0,1/2) + 12ψ(2,1/2)

=

−24γψ(1,1/2) − 24ψ(0,1/2)ψ(1,1/2) + 216ψ(1,1/3) − 432γψ(0,1/3) −216ψ(0,1/3)ψ(0,1/3) + 24ψ(2,1/3) − 48γψ(1,1/3) − 48ψ(0,1/3)ψ(1,1/3)

+1ψ(3,1/3) − 2γψ(2,1/3) − 2ψ(0,1/3)ψ(2,1/3) − 2ψ(1,1/3)ψ(1,1/3)) (67)

= −1 4

(6ψ(1,1/2) − 12γψ(0,1/2) − 6ψ(0,1/2)ψ(0,1/2) + 1ψ(2,1/2) − 2γψ(1,1/2)

−2ψ(0,1/2)ψ(1,1/2) − 6ψ(1,2/3) + 12γψ(0,2/3) + 6ψ(0,2/3)ψ(0,2/3)) (68)

- 1

- 2


(−12ψ(1,1/2) + 24γψ(0,1/2) + 12ψ(0,1/2)ψ(0,1/2) − 1ψ(2,1/2) + 2γψ(1,1/2)

=

+2ψ(0,1/2)ψ(1,1/2) + 12ψ(1,2/3) − 24γψ(0,2/3) − 12ψ(0,2/3)ψ(0,2/3) −1ψ(2,2/3) + 2γψ(1,2/3) + 2ψ(0,2/3)ψ(1,2/3)) (69)

1 12

(−216ψ(1,1/2) + 432γψ(0,1/2) + 216ψ(0,1/2)ψ(0,1/2) − 12ψ(2,1/2)

=

+24γψ(1,1/2) + 24ψ(0,1/2)ψ(1,1/2) + 216ψ(1,2/3) − 432γψ(0,2/3) −216ψ(0,2/3)ψ(0,2/3) − 24ψ(2,2/3) + 48γψ(1,2/3) + 48ψ(0,2/3)ψ(1,2/3)

+1ψ(3,2/3) − 2γψ(2,2/3) − 2ψ(0,2/3)ψ(2,2/3) − 2ψ(1,2/3)ψ(1,2/3)) (70)

1 8

(−4ψ(1,1/2) + 8γψ(0,1/2) + 4ψ(0,1/2)ψ(0,1/2) + 1ψ(2,1/2) − 2γψ(1,1/2)

=

−2ψ(0,1/2)ψ(1,1/2) + 4ψ(1,1/4) − 8γψ(0,1/4) − 4ψ(0,1/4)ψ(0,1/4)) (71)

(−8ψ(1,1/2) + 16γψ(0,1/2) + 8ψ(0,1/2)ψ(0,1/2) + 1ψ(2,1/2) − 2γψ(1,1/2)

(2k + 1)2(4k + 1)2

8

k=1

−2ψ(0,1/2)ψ(1,1/2) + 8ψ(1,1/4) − 16γψ(0,1/4) − 8ψ(0,1/4)ψ(0,1/4) + 1ψ(2,1/4) −2γψ(1,1/4) − 2ψ(0,1/4)ψ(1,1/4)) (72)

∞

1 64

Hk (2k + 1)2(4k + 1)3

(−96ψ(1,1/2) + 192γψ(0,1/2) + 96ψ(0,1/2)ψ(0,1/2) + 8ψ(2,1/2) − 16γψ(1,1/2)

=

k=1

−16ψ(0,1/2)ψ(1,1/2) + 96ψ(1,1/4) − 192γψ(0,1/4) − 96ψ(0,1/4)ψ(0,1/4)

+16ψ(2,1/4) − 32γψ(1,1/4) − 32ψ(0,1/4)ψ(1,1/4) + 1ψ(3,1/4) − 2γψ(2,1/4) −2ψ(0,1/4)ψ(2,1/4) − 2ψ(1,1/4)ψ(1,1/4)) (73)

∞

Hk (2k + 1)2(4k + 3)

1 8

(−4ψ(1,1/2) + 8γψ(0,1/2) + 4ψ(0,1/2)ψ(0,1/2) − 1ψ(2,1/2) + 2γψ(1,1/2)

=

k=1

+2ψ(0,1/2)ψ(1,1/2) + 4ψ(1,3/4) − 8γψ(0,3/4) − 4ψ(0,3/4)ψ(0,3/4)) (74)

∞

= −1 8

Hk (2k + 1)2(4k + 3)2

(8ψ(1,1/2) − 16γψ(0,1/2) − 8ψ(0,1/2)ψ(0,1/2) + 1ψ(2,1/2) − 2γψ(1,1/2)

k=1

−2ψ(0,1/2)ψ(1,1/2) − 8ψ(1,3/4) + 16γψ(0,3/4) + 8ψ(0,3/4)ψ(0,3/4) + 1ψ(2,3/4) −2γψ(1,3/4) − 2ψ(0,3/4)ψ(1,3/4)) (75)

∞

= −1 64

Hk (2k + 1)2(4k + 3)3

(96ψ(1,1/2) − 192γψ(0,1/2) − 96ψ(0,1/2)ψ(0,1/2) + 8ψ(2,1/2) − 16γψ(1,1/2)

k=1

−16ψ(0,1/2)ψ(1,1/2) − 96ψ(1,3/4) + 192γψ(0,3/4) + 96ψ(0,3/4)ψ(0,3/4)

+16ψ(2,3/4) − 32γψ(1,3/4) − 32ψ(0,3/4)ψ(1,3/4) − 1ψ(3,3/4) + 2γψ(2,3/4)

+2ψ(0,3/4)ψ(2,3/4) + 2ψ(1,3/4)ψ(1,3/4)) (76)

∞

Hk (2k + 1)3(3k + 1)

1 32

(−144ψ(1,1/2) + 288γψ(0,1/2) + 144ψ(0,1/2)ψ(0,1/2) + 24ψ(2,1/2) − 48γψ(1,1/2)

=

k=1

−48ψ(0,1/2)ψ(1,1/2) − 1ψ(3,1/2) + 4γψ(2,1/2) + 4ψ(0,1/2)ψ(2,1/2)

+144ψ(1,1/3) − 288γψ(0,1/3) − 144ψ(0,1/3)ψ(0,1/3)) (77)

∞

Hk (2k + 1)3(3k + 1)2

1 16

(432ψ(1,1/2) − 864γψ(0,1/2) − 432ψ(0,1/2)ψ(0,1/2) − 48ψ(2,1/2)

=

k=1

+96γψ(1,1/2) + 96ψ(0,1/2)ψ(1,1/2) + 1ψ(3,1/2) − 4γψ(2,1/2)

−4ψ(0,1/2)ψ(2,1/2) − 432ψ(1,1/3) + 864γψ(0,1/3) + 432ψ(0,1/3)ψ(0,1/3) −24ψ(2,1/3) + 48γψ(1,1/3) + 48ψ(0,1/3)ψ(1,1/3)) (78)

∞

Hk (2k + 1)3(3k + 1)3

1 8

(−864ψ(1,1/2) + 1728γψ(0,1/2) + 864ψ(0,1/2)ψ(0,1/2) + 72ψ(2,1/2)

=

k=1

−144γψ(1,1/2) − 144ψ(0,1/2)ψ(1,1/2) − 1ψ(3,1/2) + 4γψ(2,1/2)

+4ψ(0,1/2)ψ(2,1/2) + 864ψ(1,1/3) − 1728γψ(0,1/3) − 864ψ(0,1/3)ψ(0,1/3)

+72ψ(2,1/3) − 144γψ(1,1/3) − 144ψ(0,1/3)ψ(1,1/3) + 2ψ(3,1/3) − 4γψ(2,1/3) −4ψ(0,1/3)ψ(2,1/3) − 4ψ(1,1/3)ψ(1,1/3)) (79)

(2k + 1)3(3k + 2)

k=1

∞

Hk (2k + 1)3(3k + 2)2

k=1

∞

Hk (2k + 1)3(3k + 2)3

k=1

∞

Hk (2k + 1)3(4k + 1)

k=1

∞

Hk (2k + 1)3(4k + 1)2

k=1

∞

Hk (2k + 1)3(4k + 1)3

k=1

∞

Hk (2k + 1)3(4k + 3)

k=1

1 32

(144ψ(1,1/2) − 288γψ(0,1/2) − 144ψ(0,1/2)ψ(0,1/2) + 24ψ(2,1/2) − 48γψ(1,1/2)

=

−48ψ(0,1/2)ψ(1,1/2) + 1ψ(3,1/2) − 4γψ(2,1/2) − 4ψ(0,1/2)ψ(2,1/2) −144ψ(1,2/3) + 288γψ(0,2/3) + 144ψ(0,2/3)ψ(0,2/3)) (80)

= −1 16

(−432ψ(1,1/2) + 864γψ(0,1/2) + 432ψ(0,1/2)ψ(0,1/2) − 48ψ(2,1/2)

+96γψ(1,1/2) + 96ψ(0,1/2)ψ(1,1/2) − 1ψ(3,1/2) + 4γψ(2,1/2)

+4ψ(0,1/2)ψ(2,1/2) + 432ψ(1,2/3) − 864γψ(0,2/3) − 432ψ(0,2/3)ψ(0,2/3) −24ψ(2,2/3) + 48γψ(1,2/3) + 48ψ(0,2/3)ψ(1,2/3)) (81)

1 8

(864ψ(1,1/2) − 1728γψ(0,1/2) − 864ψ(0,1/2)ψ(0,1/2) + 72ψ(2,1/2)

=

−144γψ(1,1/2) − 144ψ(0,1/2)ψ(1,1/2) + 1ψ(3,1/2) − 4γψ(2,1/2) −4ψ(0,1/2)ψ(2,1/2) − 864ψ(1,2/3) + 1728γψ(0,2/3) + 864ψ(0,2/3)ψ(0,2/3)

+72ψ(2,2/3) − 144γψ(1,2/3) − 144ψ(0,2/3)ψ(1,2/3) − 2ψ(3,2/3) + 4γψ(2,2/3)

+4ψ(0,2/3)ψ(2,2/3) + 4ψ(1,2/3)ψ(1,2/3)) (82)

= −1 64

(64ψ(1,1/2) − 128γψ(0,1/2) − 64ψ(0,1/2)ψ(0,1/2) − 16ψ(2,1/2) + 32γψ(1,1/2)

+32ψ(0,1/2)ψ(1,1/2) + 1ψ(3,1/2) − 4γψ(2,1/2) − 4ψ(0,1/2)ψ(2,1/2) −64ψ(1,1/4) + 128γψ(0,1/4) + 64ψ(0,1/4)ψ(0,1/4)) (83)

1 64

(192ψ(1,1/2) − 384γψ(0,1/2) − 192ψ(0,1/2)ψ(0,1/2) − 32ψ(2,1/2)

=

+64γψ(1,1/2) + 64ψ(0,1/2)ψ(1,1/2) + 1ψ(3,1/2) − 4γψ(2,1/2) −4ψ(0,1/2)ψ(2,1/2) − 192ψ(1,1/4) + 384γψ(0,1/4) + 192ψ(0,1/4)ψ(0,1/4) −16ψ(2,1/4) + 32γψ(1,1/4) + 32ψ(0,1/4)ψ(1,1/4)) (84)

= −1 64

(384ψ(1,1/2) − 768γψ(0,1/2) − 384ψ(0,1/2)ψ(0,1/2) − 48ψ(2,1/2)

+96γψ(1,1/2) + 96ψ(0,1/2)ψ(1,1/2) + 1ψ(3,1/2) − 4γψ(2,1/2) −4ψ(0,1/2)ψ(2,1/2) − 384ψ(1,1/4) + 768γψ(0,1/4) + 384ψ(0,1/4)ψ(0,1/4) −48ψ(2,1/4) + 96γψ(1,1/4) + 96ψ(0,1/4)ψ(1,1/4) − 2ψ(3,1/4) + 4γψ(2,1/4) +4ψ(0,1/4)ψ(2,1/4) + 4ψ(1,1/4)ψ(1,1/4)) (85)

= −1 64

(−64ψ(1,1/2) + 128γψ(0,1/2) + 64ψ(0,1/2)ψ(0,1/2) − 16ψ(2,1/2) + 32γψ(1,1/2)

+32ψ(0,1/2)ψ(1,1/2) − 1ψ(3,1/2) + 4γψ(2,1/2) + 4ψ(0,1/2)ψ(2,1/2)

+64ψ(1,3/4) − 128γψ(0,3/4) − 64ψ(0,3/4)ψ(0,3/4)) (86)

(−192ψ(1,1/2) + 384γψ(0,1/2) + 192ψ(0,1/2)ψ(0,1/2) − 32ψ(2,1/2)

(2k + 1)3(4k + 3)2

64

k=1

+64γψ(1,1/2) + 64ψ(0,1/2)ψ(1,1/2) − 1ψ(3,1/2) + 4γψ(2,1/2)

+4ψ(0,1/2)ψ(2,1/2) + 192ψ(1,3/4) − 384γψ(0,3/4) − 192ψ(0,3/4)ψ(0,3/4) −16ψ(2,3/4) + 32γψ(1,3/4) + 32ψ(0,3/4)ψ(1,3/4)) (87)

∞

1 64

Hk (2k + 1)3(4k + 3)3

(384ψ(1,1/2) − 768γψ(0,1/2) − 384ψ(0,1/2)ψ(0,1/2) + 48ψ(2,1/2)

=

k=1

−96γψ(1,1/2) − 96ψ(0,1/2)ψ(1,1/2) + 1ψ(3,1/2) − 4γψ(2,1/2) −4ψ(0,1/2)ψ(2,1/2) − 384ψ(1,3/4) + 768γψ(0,3/4) + 384ψ(0,3/4)ψ(0,3/4)

+48ψ(2,3/4) − 96γψ(1,3/4) − 96ψ(0,3/4)ψ(1,3/4) − 2ψ(3,3/4) + 4γψ(2,3/4)

+4ψ(0,3/4)ψ(2,3/4) + 4ψ(1,3/4)ψ(1,3/4)) (88)

∞

Hk (3k + 1)(4k + 1)

- 1

- 2


(−1ψ(1,1/3) + 2γψ(0,1/3) + 1ψ(0,1/3)ψ(0,1/3) + 1ψ(1,1/4) − 2γψ(0,1/4)

=

k=1

−1ψ(0,1/4)ψ(0,1/4)) (89)

∞

= −1 8

Hk (3k + 1)(4k + 1)2

(−12ψ(1,1/3) + 24γψ(0,1/3) + 12ψ(0,1/3)ψ(0,1/3) + 12ψ(1,1/4) − 24γψ(0,1/4)

k=1

−12ψ(0,1/4)ψ(0,1/4) + 1ψ(2,1/4) − 2γψ(1,1/4) − 2ψ(0,1/4)ψ(1,1/4)) (90)

∞

Hk (3k + 1)(4k + 1)3

1 64

(−288ψ(1,1/3) + 576γψ(0,1/3) + 288ψ(0,1/3)ψ(0,1/3) + 288ψ(1,1/4)

=

k=1

−576γψ(0,1/4) − 288ψ(0,1/4)ψ(0,1/4) + 24ψ(2,1/4) − 48γψ(1,1/4) −48ψ(0,1/4)ψ(1,1/4) + 1ψ(3,1/4) − 2γψ(2,1/4) − 2ψ(0,1/4)ψ(2,1/4) −2ψ(1,1/4)ψ(1,1/4)) (91)

∞

Hk (3k + 1)(4k + 3)

1 10

(1ψ(1,1/3) − 2γψ(0,1/3) − 1ψ(0,1/3)ψ(0,1/3) − 1ψ(1,3/4) + 2γψ(0,3/4)

=

k=1

+1ψ(0,3/4)ψ(0,3/4)) (92)

∞

Hk (3k + 1)(4k + 3)2

1 200

(12ψ(1,1/3) − 24γψ(0,1/3) − 12ψ(0,1/3)ψ(0,1/3) − 12ψ(1,3/4) + 24γψ(0,3/4)

=

k=1

+12ψ(0,3/4)ψ(0,3/4) + 5ψ(2,3/4) − 10γψ(1,3/4) − 10ψ(0,3/4)ψ(1,3/4))

(93)

∞

= −1 8000

Hk (3k + 1)(4k + 3)3

(−288ψ(1,1/3) + 576γψ(0,1/3) + 288ψ(0,1/3)ψ(0,1/3) + 288ψ(1,3/4)

k=1

−576γψ(0,3/4) − 288ψ(0,3/4)ψ(0,3/4) − 120ψ(2,3/4) + 240γψ(1,3/4)

+240ψ(0,3/4)ψ(1,3/4) + 25ψ(3,3/4) − 50γψ(2,3/4) − 50ψ(0,3/4)ψ(2,3/4) −50ψ(1,3/4)ψ(1,3/4)) (94)

(−12ψ(1,1/3) + 24γψ(0,1/3) + 12ψ(0,1/3)ψ(0,1/3) + 1ψ(2,1/3) − 2γψ(1,1/3)

=

(3k + 1)2(4k + 1)

6

k=1

−2ψ(0,1/3)ψ(1,1/3) + 12ψ(1,1/4) − 24γψ(0,1/4) − 12ψ(0,1/4)ψ(0,1/4))

(95)

∞

- 1

- 2


Hk (3k + 1)2(4k + 1)2

(24ψ(1,1/3) − 48γψ(0,1/3) − 24ψ(0,1/3)ψ(0,1/3) − 1ψ(2,1/3) + 2γψ(1,1/3)

=

k=1

+2ψ(0,1/3)ψ(1,1/3) − 24ψ(1,1/4) + 48γψ(0,1/4) + 24ψ(0,1/4)ψ(0,1/4) −1ψ(2,1/4) + 2γψ(1,1/4) + 2ψ(0,1/4)ψ(1,1/4)) (96)

∞

= −1 16

Hk (3k + 1)2(4k + 1)3

(864ψ(1,1/3) − 1728γψ(0,1/3) − 864ψ(0,1/3)ψ(0,1/3) − 24ψ(2,1/3)

k=1

+48γψ(1,1/3) + 48ψ(0,1/3)ψ(1,1/3) − 864ψ(1,1/4) + 1728γψ(0,1/4)

+864ψ(0,1/4)ψ(0,1/4) − 48ψ(2,1/4) + 96γψ(1,1/4) + 96ψ(0,1/4)ψ(1,1/4) −1ψ(3,1/4) + 2γψ(2,1/4) + 2ψ(0,1/4)ψ(2,1/4) + 2ψ(1,1/4)ψ(1,1/4)) (97)

∞

= −1 150

Hk (3k + 1)2(4k + 3)

(12ψ(1,1/3) − 24γψ(0,1/3) − 12ψ(0,1/3)ψ(0,1/3) + 5ψ(2,1/3) − 10γψ(1,1/3)

k=1

−10ψ(0,1/3)ψ(1,1/3) − 12ψ(1,3/4) + 24γψ(0,3/4) + 12ψ(0,3/4)ψ(0,3/4))

(98)

∞

= −1 250

Hk (3k + 1)2(4k + 3)2

(24ψ(1,1/3) − 48γψ(0,1/3) − 24ψ(0,1/3)ψ(0,1/3) + 5ψ(2,1/3) − 10γψ(1,1/3)

k=1

−10ψ(0,1/3)ψ(1,1/3) − 24ψ(1,3/4) + 48γψ(0,3/4) + 24ψ(0,3/4)ψ(0,3/4)

+5ψ(2,3/4) − 10γψ(1,3/4) − 10ψ(0,3/4)ψ(1,3/4)) (99)

∞

= −1 10000

Hk (3k + 1)2(4k + 3)3

(864ψ(1,1/3) − 1728γψ(0,1/3) − 864ψ(0,1/3)ψ(0,1/3) + 120ψ(2,1/3)

k=1

−240γψ(1,1/3) − 240ψ(0,1/3)ψ(1,1/3) − 864ψ(1,3/4) + 1728γψ(0,3/4)

+864ψ(0,3/4)ψ(0,3/4) + 240ψ(2,3/4) − 480γψ(1,3/4) − 480ψ(0,3/4)ψ(1,3/4) −25ψ(3,3/4) + 50γψ(2,3/4) + 50ψ(0,3/4)ψ(2,3/4) + 50ψ(1,3/4)ψ(1,3/4))

(100)

∞

1 36

Hk (3k + 1)3(4k + 1)

(−288ψ(1,1/3) + 576γψ(0,1/3) + 288ψ(0,1/3)ψ(0,1/3) + 24ψ(2,1/3) − 48γψ(1,1/3)

=

k=1

−48ψ(0,1/3)ψ(1,1/3) − 1ψ(3,1/3) + 2γψ(2,1/3) + 2ψ(0,1/3)ψ(2,1/3)

+2ψ(1,1/3)ψ(1,1/3) + 288ψ(1,1/4) − 576γψ(0,1/4) − 288ψ(0,1/4)ψ(0,1/4))

(101)

∞

= −1 12

Hk (3k + 1)3(4k + 1)2

(−864ψ(1,1/3) + 1728γψ(0,1/3) + 864ψ(0,1/3)ψ(0,1/3) + 48ψ(2,1/3)

k=1

−96γψ(1,1/3) − 96ψ(0,1/3)ψ(1,1/3) − 1ψ(3,1/3) + 2γψ(2,1/3)

+2ψ(0,1/3)ψ(2,1/3) + 2ψ(1,1/3)ψ(1,1/3) + 864ψ(1,1/4) − 1728γψ(0,1/4) −864ψ(0,1/4)ψ(0,1/4) + 24ψ(2,1/4) − 48γψ(1,1/4) − 48ψ(0,1/4)ψ(1,1/4))

(102)

Hk (3k + 1)3(4k + 1)3

k=1

∞

Hk (3k + 1)3(4k + 3)

k=1

∞

Hk (3k + 1)3(4k + 3)2

k=1

∞

Hk (3k + 1)3(4k + 3)3

k=1

∞

Hk (3k + 2)(4k + 1)

k=1

∞

Hk (3k + 2)(4k + 1)2

k=1

∞

Hk (3k + 2)(4k + 1)3

k=1

1 4

(−1728ψ(1,1/3) + 3456γψ(0,1/3) + 1728ψ(0,1/3)ψ(0,1/3) + 72ψ(2,1/3)

=

−144γψ(1,1/3) − 144ψ(0,1/3)ψ(1,1/3) − 1ψ(3,1/3) + 2γψ(2,1/3)

+2ψ(0,1/3)ψ(2,1/3) + 2ψ(1,1/3)ψ(1,1/3) + 1728ψ(1,1/4) − 3456γψ(0,1/4) −1728ψ(0,1/4)ψ(0,1/4) + 72ψ(2,1/4) − 144γψ(1,1/4) − 144ψ(0,1/4)ψ(1,1/4)

+1ψ(3,1/4) − 2γψ(2,1/4) − 2ψ(0,1/4)ψ(2,1/4) − 2ψ(1,1/4)ψ(1,1/4)) (103)

= −1 4500

(−288ψ(1,1/3) + 576γψ(0,1/3) + 288ψ(0,1/3)ψ(0,1/3) − 120ψ(2,1/3)

+240γψ(1,1/3) + 240ψ(0,1/3)ψ(1,1/3) − 25ψ(3,1/3) + 50γψ(2,1/3)

+50ψ(0,1/3)ψ(2,1/3) + 50ψ(1,1/3)ψ(1,1/3) + 288ψ(1,3/4) − 576γψ(0,3/4) −288ψ(0,3/4)ψ(0,3/4)) (104)

= −1 7500

(−864ψ(1,1/3) + 1728γψ(0,1/3) + 864ψ(0,1/3)ψ(0,1/3) − 240ψ(2,1/3)

+480γψ(1,1/3) + 480ψ(0,1/3)ψ(1,1/3) − 25ψ(3,1/3) + 50γψ(2,1/3)

+50ψ(0,1/3)ψ(2,1/3) + 50ψ(1,1/3)ψ(1,1/3) + 864ψ(1,3/4) − 1728γψ(0,3/4) −864ψ(0,3/4)ψ(0,3/4) − 120ψ(2,3/4) + 240γψ(1,3/4)

+240ψ(0,3/4)ψ(1,3/4)) (105)

1 12500

(1728ψ(1,1/3) − 3456γψ(0,1/3) − 1728ψ(0,1/3)ψ(0,1/3) + 360ψ(2,1/3)

=

−720γψ(1,1/3) − 720ψ(0,1/3)ψ(1,1/3) + 25ψ(3,1/3) − 50γψ(2,1/3) −50ψ(0,1/3)ψ(2,1/3) − 50ψ(1,1/3)ψ(1,1/3) − 1728ψ(1,3/4) + 3456γψ(0,3/4)

+1728ψ(0,3/4)ψ(0,3/4) + 360ψ(2,3/4) − 720γψ(1,3/4) − 720ψ(0,3/4)ψ(1,3/4) −25ψ(3,3/4) + 50γψ(2,3/4) + 50ψ(0,3/4)ψ(2,3/4) + 50ψ(1,3/4)ψ(1,3/4))

(106)

= −1 10

(1ψ(1,2/3) − 2γψ(0,2/3) − 1ψ(0,2/3)ψ(0,2/3) − 1ψ(1,1/4) + 2γψ(0,1/4)

+1ψ(0,1/4)ψ(0,1/4)) (107)

1 200

(12ψ(1,2/3) − 24γψ(0,2/3) − 12ψ(0,2/3)ψ(0,2/3) − 12ψ(1,1/4) + 24γψ(0,1/4)

=

+12ψ(0,1/4)ψ(0,1/4) − 5ψ(2,1/4) + 10γψ(1,1/4) + 10ψ(0,1/4)ψ(1,1/4))

(108)

1 8000

(−288ψ(1,2/3) + 576γψ(0,2/3) + 288ψ(0,2/3)ψ(0,2/3) + 288ψ(1,1/4)

=

−576γψ(0,1/4) − 288ψ(0,1/4)ψ(0,1/4) + 120ψ(2,1/4) − 240γψ(1,1/4) −240ψ(0,1/4)ψ(1,1/4) + 25ψ(3,1/4) − 50γψ(2,1/4) − 50ψ(0,1/4)ψ(2,1/4) −50ψ(1,1/4)ψ(1,1/4)) (109)

(1ψ(1,2/3) − 2γψ(0,2/3) − 1ψ(0,2/3)ψ(0,2/3) − 1ψ(1,3/4) + 2γψ(0,3/4)

=

(3k + 2)(4k + 3)

2

k=1

+1ψ(0,3/4)ψ(0,3/4)) (110)

∞

1 8

Hk (3k + 2)(4k + 3)2

(12ψ(1,2/3) − 24γψ(0,2/3) − 12ψ(0,2/3)ψ(0,2/3) − 12ψ(1,3/4) + 24γψ(0,3/4)

=

k=1

+12ψ(0,3/4)ψ(0,3/4) + 1ψ(2,3/4) − 2γψ(1,3/4) − 2ψ(0,3/4)ψ(1,3/4))

(111)

∞

1 64

Hk (3k + 2)(4k + 3)3

(288ψ(1,2/3) − 576γψ(0,2/3) − 288ψ(0,2/3)ψ(0,2/3) − 288ψ(1,3/4)

=

k=1

+576γψ(0,3/4) + 288ψ(0,3/4)ψ(0,3/4) + 24ψ(2,3/4) − 48γψ(1,3/4) −48ψ(0,3/4)ψ(1,3/4) − 1ψ(3,3/4) + 2γψ(2,3/4) + 2ψ(0,3/4)ψ(2,3/4)

+2ψ(1,3/4)ψ(1,3/4)) (112)

∞

= −1 150

Hk (3k + 2)2(4k + 1)

(12ψ(1,2/3) − 24γψ(0,2/3) − 12ψ(0,2/3)ψ(0,2/3) − 5ψ(2,2/3) + 10γψ(1,2/3)

k=1

+10ψ(0,2/3)ψ(1,2/3) − 12ψ(1,1/4) + 24γψ(0,1/4) + 12ψ(0,1/4)ψ(0,1/4))

(113)

∞

Hk (3k + 2)2(4k + 1)2

1 250

(24ψ(1,2/3) − 48γψ(0,2/3) − 24ψ(0,2/3)ψ(0,2/3) − 5ψ(2,2/3) + 10γψ(1,2/3)

=

k=1

+10ψ(0,2/3)ψ(1,2/3) − 24ψ(1,1/4) + 48γψ(0,1/4) + 24ψ(0,1/4)ψ(0,1/4) −5ψ(2,1/4) + 10γψ(1,1/4) + 10ψ(0,1/4)ψ(1,1/4)) (114)

∞

= −1 10000

Hk (3k + 2)2(4k + 1)3

(864ψ(1,2/3) − 1728γψ(0,2/3) − 864ψ(0,2/3)ψ(0,2/3) − 120ψ(2,2/3)

k=1

+240γψ(1,2/3) + 240ψ(0,2/3)ψ(1,2/3) − 864ψ(1,1/4) + 1728γψ(0,1/4)

+864ψ(0,1/4)ψ(0,1/4) − 240ψ(2,1/4) + 480γψ(1,1/4) + 480ψ(0,1/4)ψ(1,1/4) −25ψ(3,1/4) + 50γψ(2,1/4) + 50ψ(0,1/4)ψ(2,1/4) + 50ψ(1,1/4)ψ(1,1/4))

(115)

∞

Hk (3k + 2)2(4k + 3)

1 6

(−12ψ(1,2/3) + 24γψ(0,2/3) + 12ψ(0,2/3)ψ(0,2/3) − 1ψ(2,2/3) + 2γψ(1,2/3)

=

k=1

+2ψ(0,2/3)ψ(1,2/3) + 12ψ(1,3/4) − 24γψ(0,3/4) − 12ψ(0,3/4)ψ(0,3/4))

(116)

∞

= −1 2

Hk (3k + 2)2(4k + 3)2

(24ψ(1,2/3) − 48γψ(0,2/3) − 24ψ(0,2/3)ψ(0,2/3) + 1ψ(2,2/3) − 2γψ(1,2/3)

k=1

−2ψ(0,2/3)ψ(1,2/3) − 24ψ(1,3/4) + 48γψ(0,3/4) + 24ψ(0,3/4)ψ(0,3/4)

+1ψ(2,3/4) − 2γψ(1,3/4) − 2ψ(0,3/4)ψ(1,3/4)) (117)

∞

= −1 16

Hk (3k + 2)2(4k + 3)3

(864ψ(1,2/3) − 1728γψ(0,2/3) − 864ψ(0,2/3)ψ(0,2/3) + 24ψ(2,2/3)

k=1

−48γψ(1,2/3) − 48ψ(0,2/3)ψ(1,2/3) − 864ψ(1,3/4) + 1728γψ(0,3/4)

+864ψ(0,3/4)ψ(0,3/4) + 48ψ(2,3/4) − 96γψ(1,3/4) − 96ψ(0,3/4)ψ(1,3/4) −1ψ(3,3/4) + 2γψ(2,3/4) + 2ψ(0,3/4)ψ(2,3/4) + 2ψ(1,3/4)ψ(1,3/4)) (118)

(3k + 2)3(4k + 1)

k=1

∞

Hk (3k + 2)3(4k + 1)2

k=1

∞

Hk (3k + 2)3(4k + 1)3

k=1

∞

Hk (3k + 2)3(4k + 3)

k=1

∞

Hk (3k + 2)3(4k + 3)2

k=1

∞

Hk (3k + 2)3(4k + 3)3

k=1

1 4500

(−288ψ(1,2/3) + 576γψ(0,2/3) + 288ψ(0,2/3)ψ(0,2/3) + 120ψ(2,2/3)

=

−240γψ(1,2/3) − 240ψ(0,2/3)ψ(1,2/3) − 25ψ(3,2/3) + 50γψ(2,2/3)

+50ψ(0,2/3)ψ(2,2/3) + 50ψ(1,2/3)ψ(1,2/3) + 288ψ(1,1/4) − 576γψ(0,1/4) −288ψ(0,1/4)ψ(0,1/4)) (119)

1 7500

(864ψ(1,2/3) − 1728γψ(0,2/3) − 864ψ(0,2/3)ψ(0,2/3) − 240ψ(2,2/3)

=

+480γψ(1,2/3) + 480ψ(0,2/3)ψ(1,2/3) + 25ψ(3,2/3) − 50γψ(2,2/3) −50ψ(0,2/3)ψ(2,2/3) − 50ψ(1,2/3)ψ(1,2/3) − 864ψ(1,1/4) + 1728γψ(0,1/4)

+864ψ(0,1/4)ψ(0,1/4) − 120ψ(2,1/4) + 240γψ(1,1/4)

+240ψ(0,1/4)ψ(1,1/4)) (120)

1 12500

(−1728ψ(1,2/3) + 3456γψ(0,2/3) + 1728ψ(0,2/3)ψ(0,2/3) + 360ψ(2,2/3)

=

−720γψ(1,2/3) − 720ψ(0,2/3)ψ(1,2/3) − 25ψ(3,2/3) + 50γψ(2,2/3)

+50ψ(0,2/3)ψ(2,2/3) + 50ψ(1,2/3)ψ(1,2/3) + 1728ψ(1,1/4) − 3456γψ(0,1/4) −1728ψ(0,1/4)ψ(0,1/4) + 360ψ(2,1/4) − 720γψ(1,1/4) − 720ψ(0,1/4)ψ(1,1/4)

+25ψ(3,1/4) − 50γψ(2,1/4) − 50ψ(0,1/4)ψ(2,1/4) − 50ψ(1,1/4)ψ(1,1/4))

(121)

1 36

(288ψ(1,2/3) − 576γψ(0,2/3) − 288ψ(0,2/3)ψ(0,2/3) + 24ψ(2,2/3) − 48γψ(1,2/3)

=

−48ψ(0,2/3)ψ(1,2/3) + 1ψ(3,2/3) − 2γψ(2,2/3) − 2ψ(0,2/3)ψ(2,2/3) −2ψ(1,2/3)ψ(1,2/3) − 288ψ(1,3/4) + 576γψ(0,3/4) + 288ψ(0,3/4)ψ(0,3/4))

(122)

1 12

(864ψ(1,2/3) − 1728γψ(0,2/3) − 864ψ(0,2/3)ψ(0,2/3) + 48ψ(2,2/3)

=

−96γψ(1,2/3) − 96ψ(0,2/3)ψ(1,2/3) + 1ψ(3,2/3) − 2γψ(2,2/3) −2ψ(0,2/3)ψ(2,2/3) − 2ψ(1,2/3)ψ(1,2/3) − 864ψ(1,3/4) + 1728γψ(0,3/4)

+864ψ(0,3/4)ψ(0,3/4) + 24ψ(2,3/4) − 48γψ(1,3/4) − 48ψ(0,3/4)ψ(1,3/4))

(123)

1 4

(1728ψ(1,2/3) − 3456γψ(0,2/3) − 1728ψ(0,2/3)ψ(0,2/3) + 72ψ(2,2/3)

=

−144γψ(1,2/3) − 144ψ(0,2/3)ψ(1,2/3) + 1ψ(3,2/3) − 2γψ(2,2/3) −2ψ(0,2/3)ψ(2,2/3) − 2ψ(1,2/3)ψ(1,2/3) − 1728ψ(1,3/4) + 3456γψ(0,3/4)

+1728ψ(0,3/4)ψ(0,3/4) + 72ψ(2,3/4) − 144γψ(1,3/4) − 144ψ(0,3/4)ψ(1,3/4) −1ψ(3,3/4) + 2γψ(2,3/4) + 2ψ(0,3/4)ψ(2,3/4) + 2ψ(1,3/4)ψ(1,3/4)) (124)

