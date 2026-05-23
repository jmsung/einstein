---
type: source
kind: paper
title: Beurling integers with lacunarity
authors: Imre Z. Ruzsa
year: 2023
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2311.11127v1
source_local: ../raw/2023-ruzsa-beurling-integers-lacunarity.pdf
topic: general-knowledge
cites:
---

arXiv:2311.11127v1[math.NT]18Nov2023

BEURLING-INTEGERS WITH LACUNARITY

IMRE Z. RUZSA

Abstract. We present examples of multiplicative semigroups of positive reals (Beurling’s generalized integers) with gaps bounded from below.

1. Introduction

Let G = {g1, g2, . . .} be a sequence of real numbers, 1 < g1 ≤ g2 ≤ . . . (generators) and B = {b0, b1, . . .}, b0 = 1 < b1 ≤ b2 ≤ . . . the sequence of products formed by elements of G. If G is the set of primes, B will be the set of positive integers. The name honours Beurling, who was the ﬁrst to study analogs of the prime-number theorem for such systems.

If G is a set of multiplicatively independent integers, B will be a subset of positive integers, hence bi+1 − bi ≥ 1. If furthermore G contains all but ﬁnitely many primes, then bi+1−bi will also be bounded from above. Lagarias [3] proved that there is no other example consisting of integers, and asked whether there is another example made of reals. I conjecture that such a set does not exist. As a ﬁrst step towards this conjecture, we show that a certain simple

attempt to construct such a set must fail, namely we cannot omit a small set of primes and replace them by non-integers.

- Theorem 1. Let P be a set of primes such that


- (1.1)


1/p < ∞

p/∈P

and α ∈ R \ Z, α > 1. With G = P ∪ {α} we have liminf bi+1 − bi = 0.

On the other hand, we can add extra elements to a very thin set of primes.

![image 1](<2023-ruzsa-beurling-integers-lacunarity_images/imageFile1.png>)

2020 Mathematics Subject Classiﬁcation. 11P32, 11N99. Key words and phrases. Beurling, generalized integers. Supported by NKFI grants K-129335, K-119528, KKP-133819.

1

- Theorem 2. Let P be a set of primes such that

p∈P

1 √p

![image 2](<2023-ruzsa-beurling-integers-lacunarity_images/imageFile2.png>)

![image 3](<2023-ruzsa-beurling-integers-lacunarity_images/imageFile3.png>)

< ∞.

There exist numbers α ∈ R \ Z, α > 1 such that for G = P ∪ {α} we have bi+1 − bi ≥ 1. The set of such numbers α has positive measure.

The above theorem was stated as to form a contrast to Theorem 1, but in fact there is nothing special in the primes.

- Theorem 3. Let G′ be a set of reals such that

- (1.2)


g∈G′

1 √g

![image 4](<2023-ruzsa-beurling-integers-lacunarity_images/imageFile4.png>)

![image 5](<2023-ruzsa-beurling-integers-lacunarity_images/imageFile5.png>)

< ∞.

Let B′ be the sequence of products formed by elements of G′. Assume that b′i+1 − b′i ≥ δ > 0 for all i. There exist numbers α ∈ R \ Z, α > 1 such that for G = G′ ∪ {α} we have bi+1 − bi ≥ δ. The set of such numbers α has positive measure.

Unfortunately we cannot say much about sets of primes which are neither almost full nor very thin. The metric appoach of Theorem 3 cannot be substantially improved. We illustrate this by the example of squares, where conditon (1.2) “just” fails.

- Theorem 4. Let G′ = {p2} be the set of prime squares, B′ = {n2} the set of squares.

There exist inﬁnitely many numbers α ∈ R \ Z, α > 1 such that for G = G′∪{α} we have bi+1 −bi ≥ 1. The set of such numbers α has measure 0.

Call a set of Beurling-integers maximal lacunary, if inf bi+1 − bi > 0, but the inclusion of any number to G spoils this property. Problem. How thin can a maximal lacunary Beurling-set be? Is B(x) = O(√x) possible?

![image 6](<2023-ruzsa-beurling-integers-lacunarity_images/imageFile6.png>)

x1/2+ε is possible, as the following easy example shows.

- Theorem 5. Let 1 < c < 2, G = {pc} be the set of c-th powers of primes, B = {nc}. This set is maximal lacunary.


The densest example of a lacunary B we could construct which is diﬀerent from the integers is as follows.

- Theorem 6. There exists a set G of irrational numbers such that G(x) = |{g ∈ G, g ≤ x}| > cx/ log x


and bi+1 − bi ≥ 1.

2. Proof of Theorem 1

Let E be the set of primes missing from P, and R the set of integers composed only of primes from P. We show that for every δ > 0 there are integers x, y ∈ R such that

|αmx − y| < δ. Case 1. α is rational, say α = a/b. We want to ﬁnd x, y ∈ R with |amx − bmy| < δbm.

Fix k so that δbm > 2. Let d = 2 if ab is odd, d = 1 otherwise. Fix odd numbers u, v with amu − bmv = d. We will ﬁnd x, y in the form

x = u + 2zbm, y = v + 2zam.

With such a choice we have amx − bmy = d < δbm. We need that x, y be free of primes from E. We shall estimate the number of integers z < Z with this property.

For a prime p ∈ E, the divisibility p|u+2zbm excludes at most one residue class modulo p. (Exactly one if p ∤ b and none if p|b, since the assumption amu − bmv = d excludes p|(u, b).) For p = 2 this divisibility cannot hold. Similarly the divisibility p|v + 2zam may exclude a residue class, hence at least p − 2 remain.

Write

2 p

η =

1 −

![image 7](<2023-ruzsa-beurling-integers-lacunarity_images/imageFile7.png>)

p∈E,p>2

and select T so that

1/p < η/3.

p∈E,p>T

Let q = p∈E,2<p≤T p. In each interval of length q there are at least

(p − 2) ≥ ηq

p∈E,2<p≤T

integers that avoid the excluded residue classes for every p ≤ T. Up to Z this is at least ηZ integers if q|Z.

Any prime divisor p > T must be less than max(u + 2zbm, v + 2zam) < cz,

and excludes 2 residue classes which means at most 2(1 + z/p) integers. There remain at least

ηZ −

2(1 + z/p) > ηZ/3 − 2π(cZ) > 0

p∈E,T<p<cZ

for large Z.

Case 2. α is irrational. Consider two convergents from the continued fraction development of α , say

ak rk

ak+1 rk+1

. Any median

< α <

![image 8](<2023-ruzsa-beurling-integers-lacunarity_images/imageFile8.png>)

![image 9](<2023-ruzsa-beurling-integers-lacunarity_images/imageFile9.png>)

xak + yak+1 xrk + yrk+1

µ =

, x, y > 0 satisﬁes

![image 10](<2023-ruzsa-beurling-integers-lacunarity_images/imageFile10.png>)

ak rk

ak+1 rk+1

, hence

< µ <

![image 11](<2023-ruzsa-beurling-integers-lacunarity_images/imageFile11.png>)

![image 12](<2023-ruzsa-beurling-integers-lacunarity_images/imageFile12.png>)

ak+1 rk+1 −

ak rk

1 rkrk+1

|α − µ| <

=

.

![image 13](<2023-ruzsa-beurling-integers-lacunarity_images/imageFile13.png>)

![image 14](<2023-ruzsa-beurling-integers-lacunarity_images/imageFile14.png>)

![image 15](<2023-ruzsa-beurling-integers-lacunarity_images/imageFile15.png>)

We try to ﬁnd x, y so that the numerator and denominator of µ be free of primes from E and

- (2.1) |α(xrk + yrk+1) − (xak + yak+1)| <

xrk + yrk+1 rkrk+1

![image 16](<2023-ruzsa-beurling-integers-lacunarity_images/imageFile16.png>)

< δ. For the last inequality to hold we require

- (2.2) x < X = δrk+1/2, y < Y = δrk/2. First we ﬁx the parity of x and y to make the numerator and denominator


odd. If akrk is odd, we set 2|y, 2 ∤ x. If ak+1rk+1 is odd, we set 2 ∤ y, 2|x. If neither happens, then we set 2 ∤ y and 2 ∤ x. The fact that ak+1rk−akrk+1 = 1 ensures that this works.

Given y, for a prime p > 2 the divisibility p|xak + yak+1 means a single residue class modulo p if p ∤ ak. It is impossible if p|ak and p ∤ y, and it always holds if p|(y, ak). Similarly, the divisibility p|xrk + yrk+1 means a single residue class modulo p if p ∤ rk, it is impossible if p|rk and p ∤ y, and it always holds if p|(y, rk). That is, at most two residue classes are excluded modulo p unless p|(y, ak) or p|(y, rk). As we have little control over prime divisors of ak and rk, we will require that y be free of prime divisors from E up to a limit.

Write

- 1

![image 17](<2023-ruzsa-beurling-integers-lacunarity_images/imageFile17.png>)

- 2 p∈E,p>2


- 1

![image 18](<2023-ruzsa-beurling-integers-lacunarity_images/imageFile18.png>)

- 2 p∈E,p>2


2 p

1 p

, η′ =

η =

1 −

1 −

![image 19](<2023-ruzsa-beurling-integers-lacunarity_images/imageFile19.png>)

![image 20](<2023-ruzsa-beurling-integers-lacunarity_images/imageFile20.png>)

and select T so that

1/p < δηη′/10.

p∈E,p>T

Let q = 2 p∈E,2<p≤T p. In each interval of length q there are at least

(p − 1) ≥ η′q

p∈E,2<p≤T

integersfree of prime divisors p ∈ E, p ≤ T. Up to Y this is at least η′Y − q integers. For each such y, in each interval of length q there are at least

(p − 2) ≥ ηq

p∈E,2<p≤T

integers that avoid the excluded residue classes for every p ≤ T. Up to X this is at least ηX − q integers. This leaves us with at least

(ηX − q)(η′y − q) > δ2ηη′rkrk+1/5 possible pairs (x, y).

Consider prime divisors p > T. The integers, which should not be divisible by these primes, are all less than

Xak + Y ak+1 < (δ/2)(akrk+1 + rkak+1) < U = 2δrkrk+1; hence this is also a bound for p. The numbers xak + yak+1 are all distinct by the coprimality of ak and ak+1, and so are the numbes xrk + yrk+1, but we cannot exclude that the two kinds overlap. Hence an upper estimate for the number of pairs x, y with an illegal divisibility is 2(U/p + 1). Summing this for all p < U we obtain

1/p + 2π(U) < δ2ηη′rkrk+1/5

2(U/p + 1) < 2U

T<p<U

p∈E,p>T

if rk is large enough.

3. Proof of Theorems 3 and 2

We need to ﬁnd numbers α such that αkm − αjn ≥ δ for all m, n ∈ G′ and positive integers j < k. Since for j ≤ k we have

αkm − αjn = αj αk−jm − n ≥ αk−jm − n , it is suﬃcient to consider the case j = 0.

We will show that the measure of such α in the interval [et, e2t] is positive for suﬃciently large t.

The event we want to avoid is αkm − n < δ, which can be rewritten as αk

- m

![image 21](<2023-ruzsa-beurling-integers-lacunarity_images/imageFile21.png>)

- n ∈ 1 −


δ n

δ n

.

, 1 +

![image 22](<2023-ruzsa-beurling-integers-lacunarity_images/imageFile22.png>)

![image 23](<2023-ruzsa-beurling-integers-lacunarity_images/imageFile23.png>)

Note that αkm − n < δ implies n > αm − δ, whence n > 2δ and n > αm/2 > m, assuming that α > 3δ which holds for t > log 3δ.

We take logarithms to infer, with the notation β = log α, that

kβ + log m − log n ∈ (−2δ/n, δ/n), that is,

log n − log m k

δ kn

+ −2δ kn

β ∈

.

,

![image 24](<2023-ruzsa-beurling-integers-lacunarity_images/imageFile24.png>)

![image 25](<2023-ruzsa-beurling-integers-lacunarity_images/imageFile25.png>)

![image 26](<2023-ruzsa-beurling-integers-lacunarity_images/imageFile26.png>)

To estimate the measure of such numbers β we add 3δ/(kn) for all triplets m, n, k such that the above interval intersects the interval [t, 2t]. If t > 4δ, this intersection implies

log n − log m

k ∈ (t/2, 3t). Hence

![image 27](<2023-ruzsa-beurling-integers-lacunarity_images/imageFile27.png>)

log n − log m 3t

log n − log m t

< k < 2

.

![image 28](<2023-ruzsa-beurling-integers-lacunarity_images/imageFile28.png>)

![image 29](<2023-ruzsa-beurling-integers-lacunarity_images/imageFile29.png>)

The ratio of the upper and lower bounds is 6, hence the sum of 1/k in this interval is less thn c = 1 + log 6. Consequently the sum of 3δ/(kn) for all triplets m, n, k is at most the sum of 3cδ/n for all possible pairs m, n. These pairs staisfy n > αm/2 > etm/2, so

1 n

1 √mn

< 2e−t/2

= 2e−t/2

![image 30](<2023-ruzsa-beurling-integers-lacunarity_images/imageFile30.png>)

![image 31](<2023-ruzsa-beurling-integers-lacunarity_images/imageFile31.png>)

![image 32](<2023-ruzsa-beurling-integers-lacunarity_images/imageFile32.png>)

m,n

m,n∈B′

1 √m

![image 33](<2023-ruzsa-beurling-integers-lacunarity_images/imageFile33.png>)

![image 34](<2023-ruzsa-beurling-integers-lacunarity_images/imageFile34.png>)

m∈B′

2

.

This series is convergent, indeed

1 √g − 1

1 √m

1 +

< ∞

=

![image 35](<2023-ruzsa-beurling-integers-lacunarity_images/imageFile35.png>)

![image 36](<2023-ruzsa-beurling-integers-lacunarity_images/imageFile36.png>)

![image 37](<2023-ruzsa-beurling-integers-lacunarity_images/imageFile37.png>)

![image 38](<2023-ruzsa-beurling-integers-lacunarity_images/imageFile38.png>)

g∈G′

m∈B′

by assumption (1.2). The estimate we found for the measure of bad β is

2

1 √m

6cδe−t/2

,

![image 39](<2023-ruzsa-beurling-integers-lacunarity_images/imageFile39.png>)

![image 40](<2023-ruzsa-beurling-integers-lacunarity_images/imageFile40.png>)

m∈B′

which is less than t, the length of the interval for large enough t.

4. Proof of Theorem 4 Let q be a squarefree integer, a, b positive integers and α = a√q + b 2. We show that for these numbers B has the lacunarity property.

![image 41](<2023-ruzsa-beurling-integers-lacunarity_images/imageFile41.png>)

The elements of B are numbers of the form αkm2, and we need to show that

αkm2 − αjn2 ≥ 1.

Since for j ≤ k we have

αkm − αjn = αj αk−jm − n ≥ αk−jm − n , it is suﬃcient to consider the case j = 0.

Put β = a√q + b k. This number is of the form

![image 42](<2023-ruzsa-beurling-integers-lacunarity_images/imageFile42.png>)

β = u√q + v with positive integers u, v. Now we have

![image 43](<2023-ruzsa-beurling-integers-lacunarity_images/imageFile43.png>)

αkm2 − n2 = (βm)2 − n2 = vm + n + um√q vm − n + um√q

![image 44](<2023-ruzsa-beurling-integers-lacunarity_images/imageFile44.png>)

![image 45](<2023-ruzsa-beurling-integers-lacunarity_images/imageFile45.png>)

vm + n + um√q vm − n − um√q

![image 46](<2023-ruzsa-beurling-integers-lacunarity_images/imageFile46.png>)

(vm − n)2 − (um)2q .

=

![image 47](<2023-ruzsa-beurling-integers-lacunarity_images/imageFile47.png>)

![image 48](<2023-ruzsa-beurling-integers-lacunarity_images/imageFile48.png>)

The enumerator exceeds the absolute value of the denominator, and the second factor is a nonzero integer, so the absolute value of the expression is > 1.

Now we show that for such numbers √α are badly approximable. Assume that it is well approximable, that is, for every ε > 0 there are integers a, b such that

![image 49](<2023-ruzsa-beurling-integers-lacunarity_images/imageFile49.png>)

√α −

ε b2

- a

![image 50](<2023-ruzsa-beurling-integers-lacunarity_images/imageFile50.png>)

- b


![image 51](<2023-ruzsa-beurling-integers-lacunarity_images/imageFile51.png>)

<

. Clearly a < 2√αb and then

![image 52](<2023-ruzsa-beurling-integers-lacunarity_images/imageFile52.png>)

![image 53](<2023-ruzsa-beurling-integers-lacunarity_images/imageFile53.png>)

αb2 − a2 = (√αb − a)(√αb + a) < 3ε√α. Badly approximable numbers have measure 0 by a theorem of Hinchin [2].

![image 54](<2023-ruzsa-beurling-integers-lacunarity_images/imageFile54.png>)

![image 55](<2023-ruzsa-beurling-integers-lacunarity_images/imageFile55.png>)

![image 56](<2023-ruzsa-beurling-integers-lacunarity_images/imageFile56.png>)

5. Proof of Theorem 5 Try to include a number α. Take integers a, b such that α1/c −

1 b2

- a

![image 57](<2023-ruzsa-beurling-integers-lacunarity_images/imageFile57.png>)

- b


<

.

![image 58](<2023-ruzsa-beurling-integers-lacunarity_images/imageFile58.png>)

From the mean value theorem we see that αbc − ac α1/cb − a

= czc−1

![image 59](<2023-ruzsa-beurling-integers-lacunarity_images/imageFile59.png>)

with some z between α1/cb and a, so z = O(b). Hence

αbc − ac = O(bc−2) can be arbitrarily small.

6. Proof of Theorem 6

We give two examples, one with quadratic irrationals and the other with transcendental numbers. Both arise from a subset of primes through a transformation.

Example 1: quadratic. Take those odd primes that split in Q[√2]. They are the primes p ≡ ±1

![image 60](<2023-ruzsa-beurling-integers-lacunarity_images/imageFile60.png>)

(mod 8) (about half of the primes). For such a prime there are positive integers x, y such that

√

√

![image 61](<2023-ruzsa-beurling-integers-lacunarity_images/imageFile61.png>)

![image 62](<2023-ruzsa-beurling-integers-lacunarity_images/imageFile62.png>)

±p = x2 − 2y2 = (x − y

2)(x + y

2).

Put f(p) = min(x+y√2) over all such representations. This satisﬁes f(p) < C√p with some constant C. This can be seen by comparing the minimal representation with the one obtained by x′ = |x − 2y|, y′ = |y − x| which corresponds to a multiplication by the unit 1 −

![image 63](<2023-ruzsa-beurling-integers-lacunarity_images/imageFile63.png>)

![image 64](<2023-ruzsa-beurling-integers-lacunarity_images/imageFile64.png>)

√2 of Q[√2]. (It is not diﬃcult to calculate the best value of C, but not too important for this argument.) Extend f multiplicatively to all integers composed exclusively of primes p ≡ ±1 (mod 8). For every such integer n we have

![image 65](<2023-ruzsa-beurling-integers-lacunarity_images/imageFile65.png>)

![image 66](<2023-ruzsa-beurling-integers-lacunarity_images/imageFile66.png>)

√

![image 67](<2023-ruzsa-beurling-integers-lacunarity_images/imageFile67.png>)

2, x, y > 0, x2 − 2y2 = n.

f(n) = x + y

Put g(n) = f(n)2. Our generators will be the numbers g(p) for p prime, B will be the set of values of g(n) for the above described special n. As g(p) < C2p and half of the primes are used, G(x) > cx/ log x holds for large x with c = 1/(2C2).

Now we show that |g(m) − g(n)| > 1 for m = n. Let f(m) = u + v

√

√

![image 68](<2023-ruzsa-beurling-integers-lacunarity_images/imageFile68.png>)

![image 69](<2023-ruzsa-beurling-integers-lacunarity_images/imageFile69.png>)

2. We have

2, f(n) = x + y

√

√

![image 70](<2023-ruzsa-beurling-integers-lacunarity_images/imageFile70.png>)

![image 71](<2023-ruzsa-beurling-integers-lacunarity_images/imageFile71.png>)

f(m)2 − f(n)2 = (u + x) + (v + y)

2 (u − x) + (v − y)

2

(u + x) + (v + y)√2 (u − x) − (v − y)√2

![image 72](<2023-ruzsa-beurling-integers-lacunarity_images/imageFile72.png>)

(u − x)2 − 2(v − y)2 .

=

![image 73](<2023-ruzsa-beurling-integers-lacunarity_images/imageFile73.png>)

![image 74](<2023-ruzsa-beurling-integers-lacunarity_images/imageFile74.png>)

The enumerator exceeds the absolute value of the denominator, and the second factor is a nonzero integer, so the absolute value of the expression is > 1.

The similarity to the proof of Theorem 4 hints that the two arguments could be combined, and the above example can be extended by including squares of integers. However, this does not substantially increase the size of B(x) and G(x).

Example 2: transcendental.

Consider primes p ≡ 1 (mod 4). Write p = a2 + b2 with 0 < a < b and let

ρ(p) = ia + b = √peih(p), 0 < h(p) < π/2. Here ρ(p) is one of the Gaussian primes in the decomposition of p inthe ring of Gaussian integers. Extend ρ multiplicatively to the product of such primes, that is, odd integers that can be written as a sum of two squares.

![image 75](<2023-ruzsa-beurling-integers-lacunarity_images/imageFile75.png>)

Since together with a Gaussian prime its conjugate is never selected, the numbers ρ(n) for n = 1, and ρ(m)/ρ(n) for m = n will never be real. Indeed, ρ(m)/ρ(n) is a product of our selected primes with (positive and negative) exponents, and its conjugate can be obtained by taking the conjugate primes, and by the unicity of prime factorization these are diﬀerent numbers.

Given a prime p let f(p) = h(p) + 2kπ with the integer k chosen so that log p < f(p) < log p + 2π. Extend f additively. We will always have

ρ(n) √n

eif(n) =

. Finally we put

![image 76](<2023-ruzsa-beurling-integers-lacunarity_images/imageFile76.png>)

![image 77](<2023-ruzsa-beurling-integers-lacunarity_images/imageFile77.png>)

g(p) = ef(p) < e2πp. These numbers form the set G, and (since again half of the primes was used) G(x) > cx/ log x, c = e−2π/2

for large x. B is the set of values of the multiplicative extension of g. Since g(n) is one of the values of (ρ(n)/√n)−i, it is transcendental by the GelfondSchneider theorem, see for insance [1].

![image 78](<2023-ruzsa-beurling-integers-lacunarity_images/imageFile78.png>)

We show the lacunarity property. For m = n consider the triangle in the integer lattice with vertices 0, ρ(m), ρ(n). Since it is a nondegenerate triangle, its area is at least 1/2, on the other hand it is exactly

√mn|sin(f(m) − f(n))|. We infer that

- 1

![image 79](<2023-ruzsa-beurling-integers-lacunarity_images/imageFile79.png>)

- 2


![image 80](<2023-ruzsa-beurling-integers-lacunarity_images/imageFile80.png>)

1 √mn

. Finally

|sin(f(m) − f(n))| ≥

![image 81](<2023-ruzsa-beurling-integers-lacunarity_images/imageFile81.png>)

![image 82](<2023-ruzsa-beurling-integers-lacunarity_images/imageFile82.png>)

f(m)−f(n) 2

f(n)−f(m)

f(m)+f(n)

g(m) − g(n) = ef(m) − ef(n) = e

2 . The ﬁrst factor is

2 e

− e

![image 83](<2023-ruzsa-beurling-integers-lacunarity_images/imageFile83.png>)

![image 84](<2023-ruzsa-beurling-integers-lacunarity_images/imageFile84.png>)

![image 85](<2023-ruzsa-beurling-integers-lacunarity_images/imageFile85.png>)

√mn. To estimate the second note that

![image 86](<2023-ruzsa-beurling-integers-lacunarity_images/imageFile86.png>)

![image 87](<2023-ruzsa-beurling-integers-lacunarity_images/imageFile87.png>)

g(m)g(n) ≥

ex − e−x > 2|x| > | sin(2x)|,

so it exceeds |sin(f(m) − f(n))| which was shown to exceed 1/√mn.

![image 88](<2023-ruzsa-beurling-integers-lacunarity_images/imageFile88.png>)

Acknowledgement. This work was inspired by converstions with Szil´ard G. Re´ve´sz.

References

- [1] E. B. Burger and R. Tubbs, Making transcendence transparent, Springer, 2004.
- [2] A. Ya. Khintchine, Continued fractions, Noordhoﬀ, Groningen, 1963, English transi, by P. Wynn.
- [3] Jeﬀrey Lagarias, Beurling generalized integers with the Delone property, Forum Mathematicum 11 (1997).


Alfr´ed R´enyi Institute of Mathematics, Budapest, Pf. 127, H-1364 Hungary

Email address: ruzsa@renyi.hu

