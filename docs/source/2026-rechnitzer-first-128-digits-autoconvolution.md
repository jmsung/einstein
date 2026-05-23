---
type: source
kind: paper
title: The first 128 digits of an autoconvolution inequality
authors: Andrew Rechnitzer
year: 2026
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2602.07292v1
source_local: ../raw/2026-rechnitzer-first-128-digits-autoconvolution.pdf
ingested_for_concept: mpmath-ulp-polish.md
cites:
  - ../wiki/concepts/mpmath-ulp-polish.md
  - ../wiki/problems/5-*.md
  - ../wiki/problems/6-*.md
  - ../wiki/problems/9-*.md
  - ../wiki/problems/10-*.md
  - ../wiki/problems/11-*.md
  - ../wiki/problems/14-*.md
  - ../wiki/problems/18-*.md
---

## arXiv:2602.07292v1[math.NT]7Feb2026

# The first 128 digits of an autoconvolution inequality

Andrew Rechnitzer∗ Department of Mathematics University of British Columbia

February 10, 2026

Abstract

Using rigorous high-precision floating point arithmetic we compute very tight rigorous bounds on the auto-convolution constant

1

(𝑓 ∗ 𝑓 )2

𝜈22 = inf

𝑓 ∗ 𝑓 22 = inf

𝑓

𝑓

−1

where the infimum is taken over all unit mass functions 𝑓 ∈ 𝐿1(−1/2, 1/2). This quantity arises in additive combinatorics, particularly in the study of Sidon sets. Our bounds give the first 128 digits of 𝜈22, and so substantially improve previous bounds on this quantity due to White, Green and Martin & O’Bryant.

### 1 Introduction

A subset 𝐴 ⊆ {1, 2, . . . , 𝑁} is a 𝐵2[𝑔]-set, when for any 𝑛 ∈ Z there are at most 𝑔 representations of the form 𝑛 = 𝑎1 + 𝑎2 where 𝑎1, 𝑎2 ∈ 𝐴, up to reordering the summands. When 𝑔 = 1 these are precisely the classical Sidon sets. A major problem in additive number theory is understanding the behaviour of the quantity 𝑅2[𝑔](𝑁), the size of the largest 𝐵2[𝑔]-set. This problem dates back to a question of Sidon [24] and work of Erdős and Turán [6]. The problem is readily generalised to ℎ summands giving 𝐵ℎ[𝑔]-sets and 𝑅ℎ[𝑔](𝑁), and we refer the reader to [19] for a survey of Sidon sets and their generalisations.

A counting argument gives an upper bound𝑅ℎ[𝑔](𝑁) ≤ 𝑔ℎℎ!𝑁, while the work of several authors [14, 2, 13] gives a lower bound 𝑅ℎ[𝑔](𝑁) ≥ (1 − 𝑜(1))(𝑔𝑁)1/ℎ. Estimating the limit

𝑅ℎ[𝑔](𝑁) (𝑔𝑁)1/ℎ

𝜎ℎ(𝑔) = lim

(1)

𝑁→∞

∗andrewr@math.ubc.ca

is an open problem. Indeed, the limit is only known to exist for classical Sidon sets where 𝜎2(1) = 1. Cilleruelo, Ruzsa & Vinuesa [3] have shown that lim

𝜎2(𝑔) exists and is expressed in terms of the quantity

𝑔→∞

𝜈∞ = inf 𝑓 ∈ 

𝑓 ∗ 𝑓 ∞ (2)

where the infimum is taken over all non-negative functions 𝑓 ∈ 𝐿1(−1/2, 1/2). This quantity was studied by Schinzel & Schmidt [22] and linked to Sidon sets by several authors [4, 16], but remains very stubbornly difficult to compute. It is a statement of just how difficult the underlying problem is, that the current¹ best lower bound [5] and upper bound [29] do not quite specify the second digit.

More generally, for any 1 < 𝑝 ≤ ∞ we then define

𝑝

1

1/2

𝜈𝑝𝑝 = inf 𝑓 ∈ 

𝑓 ∗ 𝑓 𝑝𝑝 =

𝑓 (𝑡)𝑓 (𝑥 − 𝑡)d𝑡

. (3)

−1/2

−1

𝑓 ∈ 

The question of computing this for any 𝑝 appears as Problem 35 in [10], and remains unsolved for any 𝑝 ≥ 2. When 𝑝 = 2, the subject of this work, the constant 𝜈2 connects, via work of Green [11] and White [27], to bounds for 𝜎2(𝑔) for small 𝑔 via

2 − 1/𝑔 𝜈2

. (4)

𝜎2(𝑔) ≤

Prior to this work, the strongest bounds on 𝜈22 are due to White [28], improving on previous bounds due to Green [11] and Martin & O’Bryant [15]:

0.574575 < 𝜈22 < 0.640733, 0.574636 < 𝜈22 < 0.574643. (5)

The first set of bounds are due to Green (lower) [11] and Martin & O’Bryant (upper) [15], while the second set of tighter bounds are due to White [28] — these bounds give the first 4 digits.

In this work we compute bounds that give the first 128 digits — see Theorem 1. In Section 2 we describe results of White [28] which converts the problem of minimising

𝑓 ∗ 𝑓 2 into a quadratic programming problem. By analysing the (near optimal) Fourier coefficients in White’s work we were led to a first ansatz. This allows us to translate the problem from one of minimising over a very large set of Fourier coefficients to one of minimising over a much smaller set of parameters. This results in much tighter numerical bounds but we were unable to make them completely rigorous. However, the resulting data led us to a second ansatz, described in Section 3 which we can then use, with some

¹There has been a succession of results in recent years giving upper bounds by constructing stepfunctions via machine learning methods — such as [9, 29]; there may be even newer results.

careful rigorous floating point summations, to obtain rigorous upper bounds. These are then leveraged in Section 4 to find rigorous lower bounds. Finally in Section 5 we give details of our rigorous floating point computations, state our main result Theorem 1, and explore our (near) optimal auto-convolution function.

### 2 A first ansatz

As above, let denote the set of non-negative functions in 𝐿1(−1/2, 1/2), then for 𝑓 ∈ we define its Fourier transform as

1/2

𝑒−2𝜋𝑖𝑘𝑥 𝑓 (𝑥)d𝑥 𝑘 ∈ Z. (6)

𝑓ˆ(𝑘) =

−1/2

White [28] shows that there is a unique optimal choice of 𝑓 giving 𝜈2 and that it be an even function, so that 𝑓ˆ(−𝑘) = 𝑓ˆ(𝑘). Then extend 𝑓 on (−1/2, 1/2) to a function 𝐹 defined on (−1, 1) and its transform 𝐹ˆ:

𝑓 (𝑥) 𝑥 ∈ (−1/2, 1/2) 0 otherwise

, and

𝐹(𝑥) =

1

1/2

- 1

- 2


- 1

- 2


𝐹ˆ(𝑘) =

𝑒−𝜋𝑖𝑘𝑥𝐹(𝑥)d𝑥 =

𝑒−𝜋𝑖𝑘𝑥 𝑓 (𝑥)d𝑥. (7)

−1

−1/2

White (see [28] Lemma 3.1) then establishes a relationship between 𝑓ˆ and 𝐹ˆ and rewrites 𝜈22 as

𝜈22 = inf

 (𝑓 ) where

𝑓

4

(−1)𝑘 𝑓ˆ(𝑘) 2𝑘 − (2𝑚 + 1)

8 𝜋4 𝑚∈Z 𝑘∈Z

- 1

- 2 𝑘∈Z


4

𝐹 ˆ(𝑘) 4 =

 (𝑓 ) = 𝐹 ∗ 𝐹 22 = 8

𝑓 ˆ(𝑘)

(8)

+

𝑘∈Z

By truncating the infinite sums in the above expression, White transforms the problem of minimising  (𝑓 ) into one of optimising a finite set of coefficients 𝑓 ˆ(1), 𝑓ˆ(2), . . . , 𝑓ˆ(𝑇) for some largebutfinite𝑇, implicitlysetting 𝑓ˆ(𝑘) = 0 when |𝑘| > 𝑇. The resulting optimisation problem can be written as a quadratically constrained linear program, and can be solved numerically using fairly standard software packages. That solution then gives rigorous upper and (with some extra work) lower bounds for 𝜈22.

We obtained the near optimal values 𝑓ˆ(𝑘) from White [26]. They are alternating and decrease in magnitude fairly rapidly with 𝑘. Some simple fitting shows that these coefficients lie very nearly on a curve of the form

𝑎 √

(−1)𝑘 𝑓ˆ(𝑘) =

, (9)

𝑘

where the constant 𝑎 is approximately 0.3. Some more careful numerics suggests that

1 √

(−1)𝑘 𝑓ˆ(𝑘) =

𝑘

𝑃−1

𝑎𝑗𝑘−𝑗, (10)

𝑗=0

for some modest value of 𝑃, will give an even better fit.

We use the above as an ansatz to replace the problem of optimising directly over the large set 𝑓 ˆ(1), . . . , 𝑓ˆ(𝑇) , with one of optimising over a much smaller set of coefficients 𝑎 = (𝑎0, 𝑎1, . . . , 𝑎𝑃). With this ansatz we compute  (𝑓 ) in two pieces. The first term

𝑃−1

- 1

- 2 +


| 𝑓ˆ(𝑘)|4 =

𝑎𝑖𝑎𝑗𝑎𝑘𝑎ℓ · 𝜁(2 + 𝑖 + 𝑗 + 𝑘 + ℓ), (11)

𝑖,𝑗,𝑘,ℓ=0

𝑘∈Z

where 𝜁(𝑠) can be computed to high precision, making this a simple polynomial in the 𝑎𝑗. Then

4

4

𝑚 𝑓ˆ(𝑘)(−1)𝑘 (2𝑚 − 1)2 − 4𝑘2

(−1)𝑘 𝑓ˆ(𝑘) 2𝑘 − (2𝑚 + 1)

8 𝜋4 𝑚∈Z 𝑘∈Z

16 𝜋4 𝑚≥1

1 2𝑚 − 1 + 2

=

𝑘≥1

4

16 𝜋4 𝑚∈Z

1 2𝑚 − 1 + 2

𝑎𝑝 · 𝐸𝑚,𝑝

=

𝑝

𝑚/𝑘𝑝 (2𝑚 − 1)2 − 4𝑘2

where 𝐸𝑚,𝑝 =

. (12)

𝑘≥1

Now, for any given 𝑚, 𝑝 one can compute 𝐸𝑚,𝑝 to high precision using Euler-Maclaurin summation. Then for fixed 𝑎, the sum over 𝑚 can be estimated to high precision using series acceleration methods such as the Levin transform (see, for example, [23]). In practice, these means that one needs to pre-compute a set of 𝐸𝑚,𝑝 for 𝑝 = 0, . . . , 𝑃 and 𝑚 = 1, 2, . . . , 𝑁 precise to many digits. We typically used something like 𝑃 = 32, 𝑁 = 4096 with computations to 1024 digits — not a small computation, but by no means an onerous one on modern hardware.

So, for a given fixed vector 𝑎 the above expressions allow us to estimate  ( 𝑎) to high precision. We note that by differentiating the above expressions, one can similarly estimate the partial derivatives 𝜕𝜕𝑎

, giving the gradient, and (in principle) the Hessian. This means that one can employ numerical methods to optimise over 𝑎. We did this using the BFGS quasi-Newton method (see, say, [7]). We made these computations using the mpmath package for python [17]. That library has many arbitrary precision numerical methods, rendering much of the computation quite easy to code.

𝑗

This lead us to very precise estimates of a near-optimal vector of coefficients 𝑎, and so a near-optimal 𝑓 -function. We found that the estimated 𝑎𝑗 were quite stable under

| | | | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |


- 1

- 1.5
- 2


- 2.5
- 3


−0.4 −0.2 0 0.2 0.4

| | | | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |


- 0

- 0.5
- 1

1.5

2

- 2.5




−0.4 −0.2 0 0.2 0.4

- Figure 1: The near-optimal 𝑓 (𝑥) as computed via the ansatz in equation (10). We also plot 1/𝑓 (𝑥)2 to show the nature of the singularity as 𝑥 → ±1/2. This second plot is strongly suggestive that 1/𝑓 (𝑥)2 ≈ const · (1 − 4𝑥2).


increasing 𝑃. We also examined the ansatz

𝑓ˆ(𝑘) = (−1)𝑘

𝑃−1

1 𝑘

1 √

𝑎𝑖𝑘−𝑖 +

𝑘

𝑖=0

𝑃−1

𝑏𝑖𝑘−𝑖 (13)

𝑖=0

giving both integer and half-integer powers of 𝑘. However, in that case we found that the 𝑏𝑖 in the above expression were extremely close to zero, especially as 𝑃 was increased.

We struggled for some time with the problem of taking a fixed (hopefully near-optimal) 𝑎 and turning that into a rigorously bounded value for  ( 𝑎). Unfortunately the doublesums involving the 𝐸𝑚,𝑝 made this rather challenging (to say the least). Eventually we gave up on this approach. However, examining the near-optimal 𝑓 -function led us to a simpler ansatz.

From the 𝑎 coefficients, we can compute the corresponding 𝑓 (𝑥)

𝑃−1

(−1)𝑘 𝑘𝑗+1/2 cos(2𝜋𝑘𝑥) (14)

𝑓ˆ(𝑘) · 𝑒2𝜋𝑖𝑘𝑥 = 1 + 2

𝑓 (𝑥) =

𝑎𝑗

𝑗=0

𝑘≥1

𝑘∈Z

𝑃−1

cos 𝑘𝜃 𝑘𝑝

= 1 + 2

𝑎𝑗 C(𝑗 + 1/2, 2𝜋𝑥 + 𝜋) with C(𝑝, 𝜃) =

, (15)

𝑗=0

𝑘≥1

where C(𝑝, 𝜃) is a Clausen cosine function. The mpmath package then allows us to estimate the near optimal 𝑓 (𝑥) at points in its domain, which we plot in Figure 1.

This function quite clearly diverges to +∞ as 𝑥 → ±1/2. We see strong evidence that this is an inverse square-root singularity by also plotting 1/𝑓 (𝑥)2; the resulting curve looks very much as though it is proportional to the parabola (1−4𝑥2). Indeed, this suggests that

0.65

0.645

0.64

0.635

0.63

0.625

0.62

−0.4 −0.2 0 0.2 0.4

0.001

| | | | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |


0.0005

0

−0.0005

−0.001

−0.4 −0.2 0 0.2 0.4

√1 − 4𝑥2 with a straight line at 𝑦 = 2/𝜋; note the vertical range is [0.62, 0.65]. In the second figure we plot 𝑓 (𝑥) − ℎ(𝑥) with ℎ(𝑥) given by equation (17) and find that it is very close to 0; note the vertical range is [−0.001, 0.001].

- Figure 2: A plot of 𝑓 (𝑥) ·


the near-optimal 𝑓 should be approximately ℎ(𝑥) =

1 √1 − 4𝑥2

2 𝜋

(16)

·

where√1 − 4𝑥the2 inmultiplicativeFigure 2, and constantsee that theensuresresultingthatcurvethe functionis not toohasfarmassfrom1.theWestraightplot 𝑓 (line𝑥) · 𝑦 = 2/𝜋. We note that this was observed by White [26, 27], who also credits O’Bryant for suggesting the family of functions (1 − 4𝑥2)𝑐. This observation helped prompt our explorations.

Some simple curve-fitting shows that 𝑓 (𝑥) ≈ ℎ(𝑥) given by ℎ(𝑥) =

√1 − 4𝑥2 · 0.014 (17)

2 𝜋

1 √1 − 4𝑥2

4 𝜋

· 0.986 +

Again, the multiplicative constants are chosen so ℎ = 1. In Figure 2 we also plot 𝑓 (𝑥) − ℎ(𝑥) and find that it is very close to 0.

Note that if we set ℎ(𝑥) = 2/𝜋 · (1 − 4𝑥2)−1/2 (as per (16)), then following equation (7) we obtain

- 1

- 2


𝜋𝑘 2

𝐻ˆ (𝑘) =

𝐽 0,

(18) where 𝐽 (𝑝, 𝑧) is the Bessel function of first kind of order 𝑝. Then by equation (8), we have

4

- 1

- 2 + 𝑘≥1


𝜋𝑘 2

𝐽 0,

≈ 0.574694862 . . . (19)

 (ℎ) =

This number constitutes an upper bound on 𝜈22 and is only slightly above White’s bound.

We note that the number quoted above is an approximation of the sum and not entirely rigorous. Below we will discuss how we can compute rigorous error-bars in such summations. We also note that although the summands are all positive, they have a strong period-4 behaviour (more on this below), and we found it advantageous to rewrite the sum as

4

4

4

𝜋(4𝑛 + 𝑗) 2

𝜋𝑘 2

𝐽 0,

𝐽 0,

(20)

###### =

𝑛≥0

𝑗=1

𝑘≥1

when doing numerical explorations — grouping this way makes the outer partial sums monotonic.

Now if we set ℎ(𝑥) by equation (17), then we have

1 2

4 𝜋𝑘 · 𝐽 1,

𝜋𝑘 2 · 0.986 +

𝜋𝑘

𝐻ˆ (𝑘) =

2 · 0.014 . (21) Again, using (8), we have

𝐽 0,

4

- 1

- 2 + 𝑘≥1


4 𝜋𝑘 · 𝐽 1,

𝜋𝑘 2 · 0.986 +

𝜋𝑘 2 · 0.014

𝐽 0,

≈ 0.5746396478 . . . (22)

 (ℎ) =

This is already inside the bounds computed by White and, if the above summation is made rigorous, would constitute a tighter upper bound.

### 3 A second ansatz and rigorous upper bounds

We can improve the above further by setting

which then gives

ℎ(𝑥) =

2 𝜋

1 √1 − 4𝑥2

· 𝑎 +

√1 − 4𝑥2 · (1 − 𝑎), (23)

4 𝜋

4

- 1

- 2 + 𝑘≥1


4 𝜋𝑘 · 𝐽 1,

𝜋𝑘 2 · 𝑎 +

𝜋𝑘 2 · (1 − 𝑎)

 (ℎ; 𝑎) =

𝐽 0,

(24)

≈ 0.07585490614𝑎4 − 0.1340881050𝑎3 + 0.2466255031𝑎2 − 0.3863025578𝑎 + 0.7726051152.

This quartic in 𝑎 is minimised when 𝑎 ≈ 0.9863131909 which gives  (ℎ) ≈ 0.5746396188 (25)

All the numbers in the above expressions can be computed to higher precision. We can improve the result much further by extending (23) to the ansatz

𝑃−1

𝑗 1/2 · (1 − 4𝑥2)𝑗−1/2 1 = 𝑎𝑗 (26)

𝑓 (𝑥) =

𝑎𝑗 ·

𝑗=0

where the multiplicative constants and the additional constraint ensure that 𝑓 = 1. This, in turn gives an ansatz for the Fourier coefficients

𝐹ˆ(𝑘) =

𝑃−1

- 1

- 2


𝜋𝑘 2 · 𝑗!

𝑎𝑗 · 𝐽 𝑗,

𝑗=0

4 𝜋𝑘

𝑗

. (27)

Accordingly we define

4 𝜋𝑘

𝑝

𝜋𝑘 2 · 𝑝!

, (28) and so we can write

(𝑝, 𝑘) = 𝐽 𝑝,

4

𝑃−1

- 1

- 2 + 𝑘≥1


𝜋𝑘 2

. (29)

 ( 𝑎) =

𝑎𝑗 · 𝑗,

𝑗=0

Our problem can now be restated as one of minimising the above multinomial with 𝑃+4

4 terms, subject to the constraint 𝑎𝑗 = 1.

For small values of 𝑃 it is feasible to pre-compute the 𝑃+4

4 sums of products of Bessel functions, and use Newton’s method with Lagrange multipliers to find a near-optimal 𝑎 and an upper bound on 𝜈22 — of course one still needs to bound any floating point errors in the final result. Wedidtry this approach, but foundthatthequarticgrowth inmultinomial terms became too prohibitive at modest values of 𝑃.

Instead we worked directly with equation (29). This shifts the problem to one of computing this sum (and its partial derivatives) extremely efficiently at any given fixed value of 𝑎. To do this we use Kummer’s series transform (see [1] p.16) and the asymptotics of Bessel functions. So start by writing our sum as = 𝑠𝑛 and then we find a similar, but summable series 𝐵 = 𝑏𝑛, so that the 𝑏𝑛 has the same dominant asymptotics as 𝑠𝑛. Then we can compute 𝐴 = 𝐵 + 𝑛(𝑠𝑛 − 𝑏𝑛). Since 𝑠𝑛 ∼ 𝑏𝑛, the summands (𝑠𝑛 − 𝑏𝑛) decay to zero faster and so the series converges more quickly. We can bounds |𝑠𝑛 − 𝑏𝑛| by terms of the form 𝑐𝑜𝑛𝑠𝑡𝑛𝐾 . To ensure that these terms are small, we will compute

∞

𝑁

𝑠𝑛 +

𝑠𝑛 =

𝑛=1

𝑛=1

and then bound

∞

(𝑠𝑛 − 𝑏𝑛) ≤ const ·

𝑛=𝑁+1

∞

𝑏𝑛 +

𝑛=𝑁+1

∞

(𝑠𝑛 − 𝑏𝑛) (30)

𝑛=𝑁+1

∞

𝑛−𝐾 = const · 𝜁(𝐾, 𝑁) ≤ const · 𝑁1−𝐾. (31)

𝑛=𝑁+1

In practice the above idea is complicated by the periodic behaviour of the asymptotics of Bessel functions. We use a standard large-argument expansion

𝑝! 𝑘𝑝+1/2 · cos 𝜔

22𝑝+1 𝜋𝑝+1 ·

𝑣2ℓ(𝑝) 𝑘2ℓ − sin 𝜔

𝜋𝑘 2 ∼

(−1)ℓ

(−1)ℓ

𝑝,

ℓ≥0

ℓ≥0

ℓ

𝑣ℓ(𝑝) = (−1)𝑝 4ℓ𝜋ℓℓ!

𝜋(𝑘 − 𝑝) 2 −

𝜋 4

(4𝑝2 − (2𝑗 − 1)2) and 𝜔 =

𝑗=1

𝑣2ℓ+1(𝑝) 𝑘2ℓ+1

(32)

(33)

where the error in this expansion is bounded by the magnitude of the first neglected term in both sums, provided the index of that term is at least 𝑝/2 and 𝑘 ≥ 1 (see, say, [20] or [21] (10.17.i)). For integer 𝑘, this expansion has a period-4 sign pattern, and so in practice we compute 4 separate expansions:

#####  

+𝑎0 − 𝑎04+𝜋16𝑘𝑎1 − 𝑂(𝑘−2) 𝑘 ≡ 0 +𝑎0 + 𝑎04+𝜋16𝑘𝑎1 − 𝑂(𝑘−2) 𝑘 ≡ 1 −𝑎0 + 𝑎04+𝜋16𝑘𝑎1 + 𝑂(𝑘−2) 𝑘 ≡ 2 −𝑎0 − 𝑎04+𝜋16𝑘𝑎1 + 𝑂(𝑘−2) 𝑘 ≡ 3

√2 𝜋

𝑃−1

𝜋𝑘 2 ∼

. (34)

𝑎𝑗 · 𝑗,

·

√

𝑘

𝑗=0

#####  

From those, we compute their 4th powers:

#####  

3 0(𝑎0+16𝑎1)

+𝑎04 − 𝑎

𝜋𝑘 − 𝑂(𝑘−2) 𝑘 ≡ 0

4

3 0(𝑎0+16𝑎1)

𝑃−1

+𝑎04 + 𝑎

𝜋𝑘 − 𝑂(𝑘−2) 𝑘 ≡ 1

4 𝜋4𝑘2 ·

𝜋𝑘 2

(35)

∼

𝑎𝑗 · 𝑗,

3 0(𝑎0+16𝑎1)

+𝑎04 − 𝑎

𝜋𝑘 − 𝑂(𝑘−2) 𝑘 ≡ 2

𝑗=0

#####  

3 0(𝑎0+16𝑎1)

+𝑎04 + 𝑎

𝜋𝑘 − 𝑂(𝑘−2) 𝑘 ≡ 3

We note that the 𝑂(·) term is rigorously bounded as a term of the form 𝑐𝑜𝑠𝑛𝑡𝑘2 . More generally we terminate these expansions at 𝑘−𝐾.

Since we have a bound on the 𝑂(·) we can sum the expansion in four parts and keep track of the error term. The sum of the four expansions splits into sums of the form

∞

1 (𝑛 + 𝑁 + 𝑗/4)𝑠

1 (4𝑛 + 𝑗)𝑠

= 4−𝑠

= 4−𝑠𝜁(𝑠, 𝑁 + 𝑗/4) (36)

𝑛≥0

𝑛=𝑁

and so expressed in terms of the Hurwitz zeta-function. So, for a given fixed 𝑎 we

- • Compute the four expansions in equation (34).
- • From those compute the four expansions in equation (35).
- • Sum the individual terms over 𝑘 > 𝑁 in the expansion using equation (36).


- • Similarly bound the error arising from truncating the asymptotic expansions as per equation (31).
- • Compute a finite sum of equation (29) for 1 ≤ 𝑘 ≤ 𝑁.
- • Add all of these contributions.


and so arrive at  ( 𝑎) with a bound on the error.

To control floating point errors we coded all of the above in c++ and made heavy use of the flint library [8]. This library has arbitrary precision floating point routines using ball-arithmetic [12]. This facilitates mathematically rigorous floating point computations, and allows us compute  ( 𝑎) with rigorous bounds on any floating point error.

To now minimise over 𝑎 we use Lagrange multipliers

 ( 𝑎, 𝜆) =  ( 𝑎) + 𝜆 1 −

𝑝

𝑎𝑝 (37)

and Newton-Raphson to solve ∇  = 0. This requires us to compute the first and second partial derivatives of  ( 𝑎):

3

𝑃−1

𝜋𝑘 2

𝜋𝑘 2

𝜕 𝜕𝑎ℓ  ( 𝑎, 𝜆) = 4

𝑎𝑗 · 𝑗,

− 𝜆,

ℓ,

𝑗=0

𝑘≥1

2

𝑃−1

𝜋𝑘 2

𝜋𝑘 2

𝜋𝑘 2

𝜕 𝜕𝑎𝑖

𝜕 𝜕𝑎ℓ  ( 𝑎, 𝜆) = 12

𝑎𝑗 · 𝑗,

𝑖,

,

ℓ,

𝑗=0

𝑘≥1

𝜕2 𝜕𝜆2 ( 𝑎, 𝜆) = 0. (38)

𝜕 𝜕𝜆 ( 𝑎, 𝜆) = −

𝜕 𝜕𝜆

𝜕 𝜕𝑎ℓ  ( 𝑎, 𝜆) = −1,

𝑎𝑝,

𝑝

We can compute similar expansions to those in equation (35), and then compute the sum via much the same procedure used to compute  ( 𝑎). From these quantities we can then perform Newton-Raphson iterations to converge towards the optimal 𝑎-value.

Since many 𝜁-function values are reused in each iteration, as well as the expansions of 𝑗, 𝜋2𝑘 , we pre-compute them. This speeds up the repeated computations considerably.

We parallelise the computation of the partial derivatives using a thread-pool provided by the flint library. All of this means that the bottle-neck of the computation is solving for the step direction 𝑠 via

= ∇2 𝑓 𝑠 = − −1∇𝑓 . (39)

Using this approach we computed near-optimal 𝑎 = (𝑎0, . . . , 𝑎𝑃−1), 𝜆, and the corresponding  ( 𝑎), for a range of different 𝑃. Each of these constitutes an upper bound for 𝜈22.

### 4 Lower bound

Following White (see [28] Lemma 3.2), we show how a precise upper bound can be leveraged to construct a similarly precise lower bound. Define a new 1-periodic function 𝑔 : (−1/2, 1/2) → R so that 𝑔 = 2 and then extend it to 𝐺 : [−1, 1] → R by

1 𝑥 ∈ [−1/2, 1/2] 1 − 𝑔(𝑥) otherwise

. (40)

𝐺(𝑥) =

This means that

1

1/2

𝑓 (𝑥)d𝑥 = 1. (41)

𝐹(𝑥)𝐺(𝑥)d𝑥 =

−1

−1/2

Observe that 𝐺ˆ(0) = 0 and then Plancherel’s theorem then implies that

1

𝐹ˆ(𝑘)𝐺ˆ(𝑘). (42)

1 =

𝐹(𝑥)𝐺(𝑥)d𝑥 = 2

−1

𝑘≠0

Applying Hölder’s inequality we get 1 16 ≤

3

4

𝐺 ˆ(𝑘) 4/3

𝐹( ˆ𝑘)

. (43)

𝑘≠0

𝑘≠0

Rearranging this inequality and substituting the optimal 𝐹 we have

1 2

1 2 +

𝜈22 ≥

𝑘≠0

𝐺 ˆ(𝑘) 4/3

−3

. (44)

Consequently to form a good lower bound we need to optimise 𝐺ˆ, so that Hölder’s inequality is as close to an equality as possible. It becomes an equality when 𝐺ˆ(𝑘) = 𝛼𝐹ˆ(𝑘)3 and so we seek a function 𝐺(𝑥) whose Fourier coefficients are proportional to the cube of those of 𝐹(𝑥).

We note that 𝐹ˆ(𝑘)3 is the Fourier transform of (𝐹 ∗ 𝐹 ∗ 𝐹)(𝑥), which is a function that arises naturally when proving the uniqueness of the optimising function (see Lemma 28 in [11] and Lemma 6 in [28]). For the optimal 𝐹(𝑥), the function (𝐹 ∗ 𝐹 ∗ 𝐹)(𝑥) is constant on (−1/2, 1/2) with value 𝜈22/4. That analysis also shows that the correct value of 𝛼 in the above equation is 𝛼 = 8/(2𝜈2 − 1) ≈ 53.8.

When we take a near-optimal 𝐹 we observe the result is nearly constant. For example, using equations (17) and (21), we compute the Fourier series of (𝐻 ∗ 𝐻 ∗ 𝐻)(𝑥) as the cube of 𝐻ˆ (𝑘) and multiply by 𝛼 = 53.8:

3

53.8 8

4 𝜋𝑘 · 1,

𝜋𝑘 2 · 0.986 +

𝜋𝑘 2 · 0.014

𝛼𝐻ˆ (𝑘)3 =

0,

. (45)

- 0.5
- 1


1.04

1.02

0

1

−0.5

0.98

−1

0.96

−1.5

−0.4 −0.2 0 0.2 0.4

−1 −0.5 0 0.5 1

- Figure 3: A plot of (𝐻 ∗ 𝐻 ∗ 𝐻)(𝑥) based on 𝐻(𝑥) from equation (17) for 𝑥 ∈ (−1/2, 1/2). Notice that the function is fairly constant on this range and takes a value close to 1. The second plot shows the same function but for 𝑥 ∈ (−1, 1).


Unfortunately these coefficients do not easily transform back to a simple function of 𝑥, however we can use it to construct an approximate plot of 𝛼(𝐻∗𝐻∗𝐻)(𝑥). We compute the first few hundred Fourier coefficients and then use those to construct a truncated Fouriercosine series for (𝐻 ∗ 𝐻 ∗ 𝐻)(𝑥) and then plot that in Figure 3. That quite clearly shows the function is nearly constant on (−1/2, 1/2) taking a value very nearly 𝜈22.

This indicates a problem, but does also help us towards a solution. If we have exactly the optimal 𝐹, then we can set 𝐺ˆ ∝ 𝐹ˆ3 and obtain a bound via Hölder’s inequality as above. However, we only have a near-optimal 𝐹, and if we use that to construct a 𝐺, then it will not satisfy the requirements of equation (40). We cannot guarantee that the 𝐺(𝑥) will be constant on (−1/2, 1/2) and so we cannot assert that 𝐹𝐺 = 1 as we require in

equation (41). Additionally, the correct constant 𝛼 requires a knowledge of 𝜈22 which is precisely the constant we are trying to compute!

In Figure 4 we shift the plot by 1 to highlight the non-constant region. Some simple least-squares curve fitting shows that the non-constant region is well approximated by a function of the form 1 + 𝑏1

√1 − 4𝑥2 + 𝑏2(1 − 4𝑥2)3/2. In particular 𝛼(𝐻 ∗ 𝐻 ∗ 𝐻)(𝑥 + 1) ≈ 1 − 2.044 ·

4 𝜋(1 − 4𝑥2)1/2 + 0.044 ·

16 3𝜋(1 − 4𝑥2)3/2, (46)

where we have used a similar expansion to that used in equation (17). Notice that the right-hand side of the above equation integrates to -1, as is required for equation (40). Additionally, the Fourier transform of the right-hand side is easily expressed in terms of

1, 𝜋2𝑘 , 2, 𝜋2𝑘 . Then notice that for large 𝑘 we have

- 1

- 2


- 1

- 2


𝜋𝑘 2 − 0.044 ·

𝜋𝑘 2 ≈ 𝛼𝐻ˆ (𝑘)3, (47)

(−1)𝑘 2.044 ·

1,

2,

1.5

| | | | | |
|---|---|---|---|---|
|−1.5<br><br>−1<br><br>−0.5<br><br>0<br><br>0.5<br>1<br>| | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |


−2

0 0.5 1 1.5 2

| | | | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |


- 0

0.5

- 1 approximation


−0.5

−1

−1.5

−0.4 −0.2 0 0.2 0.4

- Figure 4: A plot of (𝐻 ∗ 𝐻 ∗ 𝐻)(𝑥)from equation (17), but now shifted by 1 to highlight the non-constant region. The second plot shows that this function is well approximated by equation (46).


where the factor of (−1)𝑘 accounts for the shift 𝑥  → 𝑥 + 1. Summing the above (nonrigorously) gives

4/3

𝜋𝑘 2 − 0.022 · 2,

𝜋𝑘 2

≈ 1.885096418 . . . 𝜈22 ≥ 0.5746395994 . . .

1.022 · 1,

𝑘≠0

(48) Combining this with equation (25) gives

0.5746395995 · · · ≤ 𝜈22 ≤ 0.5746396188 . . . (49)

which are tighter than the bounds computed by White, but, at this stage we are yet to control for summation and floating-point errors.

We use this observation to formulate an ansatz for 𝐺(𝑥). We construct

𝑃

𝑝 1/2

𝑏𝑝(1 − 4𝑥2)𝑝−1/2 ·

. (50)

𝑔(𝑥) =

𝑝=1

We then satisfy 𝑔 = 2 by requiring that 𝑏𝑝 = 2. The Fourier coefficients of the corresponding 𝐺 are then

𝑃

- 1

- 2


𝜋𝑘 2

𝐺ˆ(𝑘) = (−1)𝑘

, (51)

𝑏𝑝 ·

𝑝,

𝑝=1

where the factor of (−1)𝑘 accounts for the shift required by equation (40). In order to determine the coefficients 𝑏𝑝, we require that the asymptotic expansion of 𝐺ˆ(𝑘) agrees with the expansion of 𝐹ˆ(𝑘)3.

More precisely we take our near-optimal 𝑎, and then compute an expansion in equation (34) and its cube. To leading order this is 𝑂(𝑛−3/2), and so can be matched to the leading order term of 1, 𝜋2𝑘 to compute the coefficient 𝑏1. We then determine 𝑏2 from the coefficient of 𝑛−5/2 which is a combination of the leading term of 2, 𝜋2𝑘 and the next-to-leading term of 1, 𝜋2𝑘 . We continue to the coefficient of 𝑛−7/2 to get 𝑏3 and so on. These 𝑏𝑖 give the right asymptotic behaviour of 𝐺ˆ(𝑘) up to a multiplicative constant. To set that multiplicative constant correctly, we normalise the (𝑏1, 𝑏2, . . . , 𝑏𝑝) by multiplying a constant so that 𝑏𝑖 = 2. In this way, our near-optimal 𝑎 can be used to compute a 𝑏 which, in turn, gives us a (hopefully near-optimal) 𝐺(𝑥) satisfying equation (40) and its Fourier coefficients 𝐺ˆ(𝑘).

Now, with a good candidate 𝐺ˆ(𝑘), it remains to compute 𝑘 𝐺 ˆ(𝑘) 4/3 that is required for equation (44). We proceed in much the same way we summed 𝐹ˆ(𝑘)4. We again use Kummer’s series transform. So we sum exactly for small 𝑛, and then for large 𝑛 we 𝐺ˆ(𝑘) as per equation (34), and then use that to compute the expansion of its 4/3-power. Again, these expansions exhibit the same period-4 behaviour, and so we really sum the large-n contributions in four parts. Putting this all together then gives us the required sum, with rigorous error bounds.

### 5 Results and explorations

The methods outlined above were programmed in c++ using ball-arithmetic facilitated by the flint library. There are some parameters in these calculations

- • the number of digits of precision for floating point calculations
- • 𝑃 being the number of coefficients in the ansatz (26)
- • 𝑁 being the cutoff between“small” and “large” 𝑛-values for the Kummers-transform summation (30)
- • 𝐾 being the number of terms in the expansions (34)


Since all the calculations were carried out multiple times for different values of the coefficients 𝑎 we found it helpful to pre-compute and store many parts of the computations:

- • the values of the Hurwitz-zeta functions in equation (36) — used to sum the asymptotic forms.
- • the values of 𝑁𝑘 for a large range of 𝑘-values — used to compute and track error terms from truncating expansions.
- • the values of 𝑝, 𝜋2𝑛 for 0 ≤ 𝑝 ≤ 𝑃 and 1 ≤ 𝑛 ≤ 𝑁 — for small-𝑛 summations.

- • the asymptotic expansions of 𝑝, 𝜋2𝑛 — used to build expansions such as (34).


#### 5.1 Main result

We started with a modest value of 𝑃 = 4, with 𝑁 = 1024 and 𝐾 = 64, 256 digits of floatingpoint precision, and then set 𝑎 = (1, 0, 0, 0), 𝜆 = 0.5. The code then uses precomputed expansions of Bessel functions to assemble the expansion of 𝐹ˆ(𝑘) and a bound on the truncation error using the assumption that 𝑛 ≥ 𝑁. This is then used to build expansions of 𝐹ˆ(𝑘)2, 𝐹ˆ(𝑘)3 and 𝐹ˆ(𝑘)4. We then compute the Lagrangian and the required partial derivatives using Kummers-transform and the pre-computed Bessel- and zeta-function values, while bounding the error and using ball-arithmetic to control rigorously the floating-point errors. Much of this can be parallelised and it typically only took a few seconds on a relatively modern laptop computer.

The first and second partial-derivatives are used to construct the gradient and Hessian, and then perform a Newton-Raphson iteration to compute a new value of 𝑎. We iterated this process until the norm of the gradient was sufficiently small — say, on the order of 10−40. For 𝑃 = 8 this was only a few tens of seconds. At this point, we used 𝑎 to compute 𝑏 as outlined above and summed 𝐺 ˆ(𝑘) 4/3 again using the Kummer-transform. This gives the following upper and lower bounds on 𝜈22:

0.5746396065 ≤ 𝜈22 ≤ 0.5746396072 (52)

where we have underlined the common digits and have rounded the last digit down and up respectively. We note that the above bounds are rigorous and any truncation errors or floating point errors are many orders of magnitude smaller than the rounding of the last stated digit.

Once we had a near-optimal 𝑎 for 𝑃 = 4, we increased 𝑃 to 8, and then appended 0’s to 𝑎 to make a new starting point for Newton-Raphson. We iterated until this had reasonably converged and then computed upper and lower bounds.

0.57463960715151947 ≤ 𝜈22 ≤ 0.57463960715151960 (53)

Again, we underline the common digits and round the last digit down and up respectively. Note that as 𝑃 is increased, the optimal 𝑎 changes very little; we observe that 𝑎𝑗(𝑃)−𝑎𝑗(𝑃+1) decays exponentially with 𝑃.

Then incremented 𝑃 again and repeated this process. We found that as 𝑃 became larger it was necessary to increase 𝑁 and 𝐾 and also the number of digits of precision. We finished with 𝑃 = 101, 𝑁 = 8192, 𝐾 = 128 and 384 digits of precision. This gives the first 128 digits of 𝜈22 which is the main result of the paper.

Theorem 1. The quantity 𝜈22 = inf 𝑓∈  𝑓 ∗ 𝑓 22, where the infimum is taken over all functions 𝑓 ∈ 𝐿1(−1/2, 1/2) with 𝑓 = 1, is bounded by

𝑐ℓ ≤ 𝜈22 ≤ 𝑐𝑢

| | | | |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |


10

8

6

4

2

0

−1 −0.5 0 0.5 1

| | | | |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |


- 0.8
- 1


0.6

0.4

0.2

0

−0.2

−1 −0.5 0 0.5 1

Figure 5: Plots of the very-nearly optimal 𝐹(𝑥) and 𝐺(𝑥) used to prove Theorem 1.

where |𝑐𝑢 − 𝑐ℓ| ≤ 1.2 × 10−129, and 𝑐ℓ = 0.574639607151519592727255427527052971437026369373156611630876 · · ·

7489255216181789888224078247557153295571660606473574241326386482067358 𝑐𝑢 = 0.574639607151519592727255427527052971437026369373156611630876 · · ·

7489255216181789888224078247557153295571660606473574241326386482067369 We have underlined first 128 digits that are common to the upper and lower bounds. Conse-

quently, if 𝑓 : [−1/2, 1/2] → R+ is a non-negative function with 𝑓 = 1, then 𝑓 ∗ 𝑓 22 ≥ 𝑐ℓ.

The 𝑎 and 𝑏 coefficients used to compute the bounds in this result are given in Appendix A. We also give python code in Appendix B that demonstrates how to use use (the first few of) these coefficients to compute upper and lower bounds — albeit nonrigorously. We note that while the 𝑎-coefficients are steadily decreasing in magnitude, the

𝑏-coefficients stabilise in magnitude at about 𝑏70. This suggests that fewer 𝑏-coefficients might be necessary to compute the lower bound to the given accuracy; we have not explored this possibility. In Figure 5 we plot the corresponding (very near) optimal 𝐹(𝑥) and 𝐺(𝑥) that are used to prove Theorem 1.

We note that there is no real technical impediment to extending these bounds to more digits, other than computer time and patience; the memory requirements were negligible. In Figure 6 we have plotted the width of the bound (i.e. upper minus lower) against 𝑃, the number of coefficients in the ansatz. We see that the logarithm of the width of the bound is quite linear against 𝑃. A simple rough linear fit gives log10 𝑤(𝑃) ≈ −7.6 − 1.2𝑃 and so we extrapolate that we would need about 𝑃 ≈ 160 to fix the first 200 digits and 𝑃 ≈ 830 to get the first 1000 digits.

| | | | | | | |
|---|---|---|---|---|---|---|
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |


log-width(P)

ﬁt line

−20

−40

−60

−80

−100

−120

0 20 40 60 80 100

- Figure 6: The decimal-logarithm of the width of the bound against 𝑃. We also show a simple linear fit of the data which shows that log10(𝑤(𝑃)) ≈ −7.5 − 1.2𝑃.


#### 5.2 Explorations

Part of the motivation of pushing the above calculations to this level of precision was the hope that we could find some underlying closed form expression for 𝜈2 or the corresponding minimising function. Unfortunately despite the precision with which we now know 𝜈22 we have not been able to guess a simple closed form using RIES [18], the Inverse Symbolic Calculator or Plouffe’s inverter [25].

We have also examined the 𝑎 coefficients, hoping to guess some closed forms. We do find that the coefficients converge quickly as 𝑃 increases, and we also observe that

𝑎𝑛 𝑎𝑛+1 ∼ −8 · (1 + 𝑛−1). (54)

This simple form seems to hold except for 𝑛-values close to 𝑃. Similar behaviour was observed for smaller values of 𝑃 and we expect that if 𝑃 were increased further, that the above functional form would continue to hold. This, in turn suggests that 𝑎𝑛 ∼ 𝐴(−8)−𝑛𝑛−1(1 + . . . ). Some rough fitting yielded

𝑛(−8)𝑛𝑎𝑛 ≈ 1.45 + 0.54𝑛−1, (55)

but could not find any particularly convincing values of the above constants, but we think that they give an indication of the magnitude of those terms. That said, the signal of (−8)−𝑛𝑛−1 in the coefficients is extremely robust.

−8

| | | | | |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |
| | | | | |


ratio ratio

−8.2

−8.4

−8.6

−8.8

−9

0 0.02 0.04 0.06 0.08 0.1

- Figure 7: A plot of the ratios 𝑎𝑛/𝑎𝑛+1 against 1/𝑛 obtained with 𝑃 = 101. We note that the data is extremely well fitted by the line 𝑦 = −8 · (1 + 1/𝑛) until 𝑛 is close to the final few coefficients.


We note that we see similar scaling of the 𝑏-coefficients used to compute the lower bound:

𝑏𝑛

𝑏𝑛+1 ∼ −8 · (1 + 2𝑛−1). (56) Again, while the signal of (−8)−𝑛𝑛−2 is very strong and robust, we did not arrive at any convincing fit of more detailed asymptotics. Very roughly we observe

𝑛2(−8)𝑛𝑏𝑛 ≈ 4.5 − 2.3𝑛−1, (57)

but this should be taken as an indication of the magnitude of those coefficients, not a reliable fit.

We are not entirely sure what to make of these asymptotic signals, other than that it suggests there is more structure in this problem waiting to be uncovered.

### Acknowledgements

The author thanks Michael Bennett, Tony Guttmann, Kevin O’Bryant, Jozsef Solymosi and Ethan White for their helpful discussions. I would also like to give credit to the developers of flint and mpmath for their excellent software; it was key both for numerical explorations and rigorous calculations. The author also acknowledges funding from NSERC via the Discovery Project program.

### References

- [1] Milton Abramowitz and Irene A Stegun. Handbook of mathematical functions with formulas, graphs, and mathematical tables. Vol. 55. US Government printing office, 1964.
- [2] Javier Cilleruelo and Jorge Jiménez-Urroz. “𝐵ℎ[𝑔] sequences”. In: Mathematika 47.1-2

(2000), pp. 109–115.

- [3] Javier Cilleruelo, Imre Ruzsa, and Carlos Vinuesa. “Generalized sidon sets”. In: Advances in Mathematics 225.5 (2010), pp. 2786–2807.
- [4] Javier Cilleruelo and Carlos Vinuesa. “𝐵2[𝑔] sets and a conjecture of Schinzel and Schmidt”. In: Combinatorics, Probability and Computing 17.6 (2008), pp. 741–747.
- [5] Alexander Cloninger and Stefan Steinerberger. “On suprema of autoconvolutions with an application to Sidon sets”. In: Proceedings of the American Mathematical Society 145.8 (2017), pp. 3191–3200.
- [6] Paul Erdős and Paul Turán. “On a problem of Sidon in additive number theory, and on some related problems.” In: 16 (4 1941), pp. 212–215.
- [7] Roger Fletcher. Practical methods of optimization. John Wiley & Sons, 2013.
- [8] The FLINT team. FLINT: Fast Library for Number Theory. Version 3.4.0, https://flintlib.org. 2025.
- [9] Bogdan Georgiev et al. “Mathematical exploration and discovery at scale”. In: arXiv: 2511.02864 (2025).
- [10] Ben Green. 100 open problems. manuscript, available on request to Professor Green.
- [11] Ben Green. “The number of squares and 𝐵ℎ[𝑔] sets”. In: Acta Arithmetica 100.4 (2001), pp. 365–390.
- [12] Fredrik Johansson. “Arb: Efficient arbitrary precision midpoint radius interval arithmetic”. In: IEEE Transactions on Computers 66.8 (2017), pp. 1281–1292.
- [13] Griffin Johnston, Michael Tait, and Craig Timmons. “Upper and lower bounds on

the size of 𝐵𝑘[𝑔] sets”. In: Australiasian Journal of Combinatorics 83.1 (2022), pp. 129– 140.

- [14] Bernt Lindström. “𝐵ℎ[𝑔]-sequences from 𝐵ℎ-sequences”. In: Proceedings of the American Mathematical Society (2000), pp. 657–659.
- [15] Greg Martin and Kevin O’Bryant. “The symmetric subset problem in continuous Ramsey theory”. In: Experimental Mathematics 16.2 (2007), pp. 145–165.
- [16] Greg Martin and Kevin O’Bryant. “The supremum of autoconvolutions, with applications to additive number theory”. In: Illinois Journal of Mathematics 53.1 (2009), pp. 219–235.
- [17] The mpmath development team. mpmath: a Python library for arbitrary precision floating point arithmetic (version 1.3.0). http://mpmath.org/. 2023.


- [18] Robert Munafo. Ries: Rilybot Inverse Equation Solver. https://www.mrob.com/pub/ ries/index.html. 2022.
- [19] Kevin O’Bryant. “A complete annotated bibliography of work related to Sidon sequences”. In: Electronic Journal of Combinatorics Dynamic surveys 11 (2004), pp. 1– 39.
- [20] Frank Olver. Asymptotics and special functions. AK Peters/CRC Press, 1997.
- [21] Frank W J Olver et al. Digital library of mathematical functions. https://dlmf.nist. gov/. 2019.
- [22] A Schinzel and WM Schmidt. “Comparison of 𝐿1- and 𝐿∞-norms of squares of polynomials”. In: Acta Arithmetica 104 (2002), pp. 283–296.
- [23] AvramSidi. Practicalextrapolationmethods:Theoryand applications.Vol.10.Cambridge university press, 2003.
- [24] Simon Sidon. “Ein Satz über trigonometrische Polynome und seine Anwendung in der Theorie der Fourier-Reihen”. In: Mathematische Annalen 106.1 (1932), pp. 536– 539.
- [25] David R Stoutemyer. “How to hunt wild constants”. In: arXiv: 2103.16720 (2021).
- [26] Ethan Patrick White. personal communication. 2024.
- [27] Ethan Patrick White. “An almost-tight 𝐿2 autoconvolution inequality”. In: arXiv: 2210.16437 (2022).
- [28] Ethan Patrick White. “An optimal autoconvolution inequality”. In: Canadian Mathematical Bulletin 67.1 (2024), pp. 108–121.
- [29] Mert Yuksekgonul et al. “Learning to Discover at Test Time”. In: arXiv: 2601.16175


(2026).

### AAnsatzcoefficients

WegivetheandcoefficientsthatareusedtocomputetheboundsinTheorem1.Wehavetruncatedtheseat128 𝑎 𝑏

digits.

|𝑎𝑝<br><br>0|.9860206557159394798198259740569729047977495016955157440817168533806412844365048663969595<br><br>0.01489770489081501391236554516465932337360037886185262531409922769587507544257885553721071292939933006377392624509980008292575019<br><br>-0.00100205147026116189707339482723743634634855852968990358063334091805583926892625550551551017653327044507577012139566932195157950<br><br>0.00009204407950297445359544529687886064943150128923593264098550129302924478408374955135440082953010229598917584177918942923344904<br><br>-0.00000922274904509772914881249306215878382678034496365492938748571679130161109502434346988480188665105871343249815026801667610920<br><br>0.00000096248293777695239529770940406980385573510172484739923996188253946427333183826276677870868029861653768632831444028178007925<br><br>-0.00000010308254667112377770352811050554776487355578124053305283669721149458702219139700107199486390915352511624730946494476325852<br><br>0.00000001125442999323010976782605876372232519419601097844133358508048774936750593188528772457877750953930068098950646291457515379<br><br>-0.00000000124752688834370157801836354986319635941999009201009510429123187129057108187123588457671365713289942497871930592821722596<br><br>0.00000000013999835706501306249491275040186120544384912063038540963472409378032308691716797472525682861221215931077648801243110953<br><br>-0.00000000001587108251776074784839022898212750147053313531428602050340190360631660966934550589405568798555200352106118884222032538<br><br>0.00000000000181457936724973745938016642332925399974993453212544266259390429885622289685497037488525637549662968871641547375478972<br><br>-0.00000000000020895936361219667407322629723937158854300531603277784230504175662574715902488555569213215274038232249436834427175533<br><br>0.00000000000002421093838520663620792232232117921974355045462840913540269329904943007360029724462855163906982593109397378696703991<br><br>-0.00000000000000282008054061566739367389444663724772159543038013815771878818399242827152032103549753349436868166270269801819363472<br><br>0.00000000000000033000131420654058434725678872629262934997700068966298963247713780231593921874957824445959306112754673467111387467<br><br>-0.00000000000000003877312975807208249544469859456112800747365135241934148282443154017384602330494086694938790432875367855607117426<br><br>0.00000000000000000457198691425878853747411301567813802192928752567789475706546885071732137722406542546999659597636047872144377889<br><br>-0.00000000000000000054083956779454257619021646503718481432293544952313528951804923049437792009155201232560572092281770582103834112<br><br>0.00000000000000000006416197485660862347940887486845107212042017100285527469759052073014019639801219350633648958205415722289264059<br><br>-0.00000000000000000000763150526231448395786846231154147604545362252211343391495743473317161110587576315905247644179588270741479441<br><br>0.00000000000000000000090983047251504819787197629681843879759005992127979856128680460179042780177735369732448841924593108178994189<br><br>-0.00000000000000000000010870191728598186414407822486181171595210052896685470598994002348238365199433796607771128381837768217912410<br><br>0.00000000000000000000001301250076075800810441815260661785624451441008797432775406046786444831381316526909774699990897544927610652<br><br>-0.00000000000000000000000156049130477462767383517075901464180143779239226022517349114356840077165476859649170862277620551175965633<br><br>0.00000000000000000000000018744653061723895081638820842105919591953375602299779714965620404571655662221458572173057040335037646517<br><br>-0.00000000000000000000000002255040723271186408025465369462058839681249458584143153990360285002830796325441774423267289774109646182<br><br>0.00000000000000000000000000271671294242622470411133487840687989946022016102614595674805919116951699405643831033233150955970035971<br><br>-0.00000000000000000000000000032771935591411601308066385942808429522025085672859175030664123613989878132858385226641230329614128915<br><br>0.00000000000000000000000000003958133665045999892178660686839121277569959248873313737614558281165992351168678903542940526815320742<br><br>-0.00000000000000000000000000000478601159937482790532105231810477017342000309129188325857890873035056021031286321243340010501132973<br><br>0.00000000000000000000000000000057932228794767412709441362326582287633563383939790182510297892574313694959864399612127172753341730<br><br>-0.00000000000000000000000000000007019418737404626005609577331569335732864594672763388689711123571815852534728551550610361359368438<br><br>0.00000000000000000000000000000000851315042656325612270758598959076419037368451980922296455814784658427453908722736741057688772015<br><br>-0.00000000000000000000000000000000103338896966892030571003062238739882733489585104515513691361635797928809560274284474059058823274<br><br>0.00000000000000000000000000000000012554512150951189429585281121201242465890427601060360317610528088904704412980452539092813718535<br><br>-0.00000000000000000000000000000000001526435031665054994534643884594676617003584343451307931585740959599905812727909767798748019287<br><br>0.00000000000000000000000000000000000185729480712076063363385226660885583492923010917134772323815446731339740028162825812204455558<br><br>-0.00000000000000000000000000000000000022614678667523558434996310714672335220277935561460879914156266652285326045728268389137715257<br><br>0.00000000000000000000000000000000000002755442635583815710739176959606588537226473609804094562343881209544923164259406997861163794|𝑎𝑝|
|---|---|---|
|𝑝|1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>23<br>24<br>25<br>26<br>27<br>28<br>29<br>30<br>31<br>32<br>33<br>34<br>35<br>36<br>37<br>38<br>39<br>|𝑝|


09838106504681745070718453265042295595

12939933006377392624509980008292575019

32953010229598917584177918942923344904

50868029861653768632831444028178007925

77877750953930068098950646291457515379

92525682861221215931077648801243110953

117488525637549662968871641547375478972

134462855163906982593109397378696703991

154957824445959306112754673467111387467

172406542546999659597636047872144377889

199801219350633648958205415722289264059

210177735369732448841924593108178994189

231381316526909774699990897544927610652

251655662221458572173057040335037646517

276951699405643831033233150955970035971

291165992351168678903542940526815320742

312574313694959864399612127172753341730

334784658427453908722736741057688772015

350528088904704412980452539092813718535

373815446731339740028162825812204455558

392343881209544923164259406997861163794

27653327044507577012139566932195157950

40188665105871343249815026801667610920

69486390915352511624730946494476325852

87671365713289942497871930592821722596

109405568798555200352106118884222032538

125569213215274038232249436834427175533

143549753349436868166270269801819363472

160494086694938790432875367855607117426

189155201232560572092281770582103834112

200587576315905247644179588270741479441

225199433796607771128381837768217912410

247165476859649170862277620551175965633

262830796325441774423267289774109646182

283989878132858385226641230329614128915

303035056021031286321243340010501132973

323571815852534728551550610361359368438

341635797928809560274284474059058823274

365740959599905812727909767798748019287

384156266652285326045728268389137715257

𝑝𝑎𝑝

𝑝𝑎𝑝

|𝑎𝑝|-0.0000000000000000000000000000000000000033594578181137269407485695681598558360268746184404<br><br>0.00000000000000000000000000000000000000040983630019698508285790704521302174787362386873246780547455289544119912211694645825592274<br><br>-0.00000000000000000000000000000000000000005002678186810020583539468276657847610853800940511256232735582198524246062313541324029721<br><br>0.00000000000000000000000000000000000000000610989849801212933800736986084777349075949075376896244314141085524033827057338656651215<br><br>-0.00000000000000000000000000000000000000000074661011576241763781149696564640636011206071363289428811286822317218436420886111916034<br><br>0.00000000000000000000000000000000000000000009127925136644309830243688356670379927578270041714958780758124317696714360299671667879<br><br>-0.00000000000000000000000000000000000000000001116501040130585035565237462382398547342129876462018316308073098317657749869089398504<br><br>0.00000000000000000000000000000000000000000000136630040314889418946084111095472357974241937838038854566595124021717476668282637379<br><br>-0.00000000000000000000000000000000000000000000016727265646568911299231591021763287414204923035851678693220709379767167768597450686<br><br>0.00000000000000000000000000000000000000000000002048743565445389116475451328962090191761415085063032706097210712842041946377730919<br><br>-0.00000000000000000000000000000000000000000000000251030682428190474968916660237616098011845620963629883553284804565875006775962962<br><br>0.00000000000000000000000000000000000000000000000030770578488894628208517329488323662091571197928212443912914206930105027858417610<br><br>-0.00000000000000000000000000000000000000000000000003773181161746214009070449857978871987483620956858431708996825918865849511269481<br><br>0.00000000000000000000000000000000000000000000000000462846149360105202002484177171659644203262883969784426174575427213517702165059<br><br>-0.00000000000000000000000000000000000000000000000000056795882600461820374531327015489786234964653194074467627260877757274923746785<br><br>0.00000000000000000000000000000000000000000000000000006971765417249870578431120081035902332169902580272201971670097651986761089733<br><br>-0.00000000000000000000000000000000000000000000000000000856069849426285765919176101721565535014743374907968143395936375000981364096<br><br>0.00000000000000000000000000000000000000000000000000000105150475428056475261872383226343216452461168333790566472181993704523484489<br><br>-0.00000000000000000000000000000000000000000000000000000012919455700619248916665905455588455130410838120521596875829801567317032934<br><br>0.00000000000000000000000000000000000000000000000000000001587828898393624011661993251009053574233906022872417385501389485525302844<br><br>-0.00000000000000000000000000000000000000000000000000000000195202549878205616820430361201020206702181094495096006654193338334890111<br><br>0.00000000000000000000000000000000000000000000000000000000024004107840376710474169451740849130355531835352818147826397737584550563<br><br>-0.00000000000000000000000000000000000000000000000000000000002952569583647896352995075016457509102074807989029557375349591707840394<br><br>0.00000000000000000000000000000000000000000000000000000000000363266689081628479448378028542451918607556164994539452242570579105826<br><br>-0.00000000000000000000000000000000000000000000000000000000000044705238245710279823577791099792192493580614814526490415429879814107<br><br>0.00000000000000000000000000000000000000000000000000000000000005502947340108063904373001898010057993913926859547534443917891125410<br><br>-0.00000000000000000000000000000000000000000000000000000000000000677537373390466410062613440224799220415853549235538350548111060287<br><br>0.00000000000000000000000000000000000000000000000000000000000000083439002422714847661370691263451003815932784444023177656577044147<br><br>-0.00000000000000000000000000000000000000000000000000000000000000010277796675991542873549909134179999472113333055760273964752408880<br><br>0.00000000000000000000000000000000000000000000000000000000000000001266261087869095894645063602792465850594025158906214580661149616<br><br>-0.00000000000000000000000000000000000000000000000000000000000000000156040088452232213271828091877736247139627119146804989306153944<br><br>0.00000000000000000000000000000000000000000000000000000000000000000019232523831051335348807208205304868932362345547978385313398376<br><br>-0.00000000000000000000000000000000000000000000000000000000000000000002370943026407117817636477802257088400739853564199485451725501<br><br>0.00000000000000000000000000000000000000000000000000000000000000000000292340096447487567327508866641171738267669130416855354393651<br><br>-0.00000000000000000000000000000000000000000000000000000000000000000000036052539253932852363452218059569604866043306342254080023117<br><br>0.00000000000000000000000000000000000000000000000000000000000000000000004446941331165304635929019689784462789499993745600082553745<br><br>-0.00000000000000000000000000000000000000000000000000000000000000000000000548609038770849939160083300295769952024471788809309455791<br><br>0.00000000000000000000000000000000000000000000000000000000000000000000000067692189743857336721825798685418520282524305563802493393<br><br>-0.00000000000000000000000000000000000000000000000000000000000000000000000008353843138161365245490941488596865498932467542025236714<br><br>0.00000000000000000000000000000000000000000000000000000000000000000000000001031108551154953722565775350131044229825405436427577762<br><br>-0.00000000000000000000000000000000000000000000000000000000000000000000000000127289036532278537174304773357456685108072477703753884<br><br>0.00000000000000000000000000000000000000000000000000000000000000000000000000015716084067912821226818145169287808062622907570359639<br><br>-0.00000000000000000000000000000000000000000000000000000000000000000000000000001940717446638463468610019274379634503406862702264311<br><br>0.00000000000000000000000000000000000000000000000000000000000000000000000000000239685326985640090722064041603253236123708795368800<br><br>-0.00000000000000000000000000000000000000000000000000000000000000000000000000000029605571640403838995092582416190811408531961256608<br><br>0.00000000000000000000000000000000000000000000000000000000000000000000000000000003657078619107130271227666881993110356454449313318<br><br>-0.00000000000000000000000000000000000000000000000000000000000000000000000000000000451704063474421387286818571796425847890279116776<br><br>|𝑎𝑝|
|---|---|---|
|𝑝|40<br>41<br>42<br>43<br>44<br>45<br>46<br>47<br>48<br>49<br>50<br>51<br>52<br>53<br>54<br>55<br>56<br>57<br>58<br>59<br>60<br>61<br>62<br>63<br>64<br>65<br>66<br>67<br>68<br>69<br>70<br>71<br>72<br>73<br>74<br>75<br>76<br>77<br>78<br>79<br>80<br>81<br>82<br>83<br>84<br>85<br>86<br>|𝑝|


0547455289544119912211694645825592274

6244314141085524033827057338656651215

4958780758124317696714360299671667879

8038854566595124021717476668282637379

5063032706097210712842041946377730919

7928212443912914206930105027858417610

2883969784426174575427213517702165059

9902580272201971670097651986761089733

2461168333790566472181993704523484489

4233906022872417385501389485525302844

0355531835352818147826397737584550563

1918607556164994539452242570579105826

0057993913926859547534443917891125410

3451003815932784444023177656577044147

2792465850594025158906214580661149616

8205304868932362345547978385313398376

8866641171738267669130416855354393651

9019689784462789499993745600082553745

1825798685418520282524305563802493393

2565775350131044229825405436427577762

1226818145169287808062622907570359639

0090722064041603253236123708795368800

7130271227666881993110356454449313318

1958670005067893881321666238027815746

6232735582198524246062313541324029721

9428811286822317218436420886111916034

2018316308073098317657749869089398504

5851678693220709379767167768597450686

0963629883553284804565875006775962962

0956858431708996825918865849511269481

4653194074467627260877757274923746785

4743374907968143395936375000981364096

0410838120521596875829801567317032934

6702181094495096006654193338334890111

9102074807989029557375349591707840394

2192493580614814526490415429879814107

4799220415853549235538350548111060287

4179999472113333055760273964752408880

1877736247139627119146804989306153944

7802257088400739853564199485451725501

2218059569604866043306342254080023117

0083300295769952024471788809309455791

5490941488596865498932467542025236714

7174304773357456685108072477703753884

3468610019274379634503406862702264311

3838995092582416190811408531961256608

4421387286818571796425847890279116776

𝑎𝑝

𝑎𝑝

|𝑎𝑝|0.00000000000000<br><br>-0.00000000000000000000000000000000000000000000000000000000000000000000000000000000006872615798301534950869865375959585368851772949<br><br>0.00000000000000000000000000000000000000000000000000000000000000000000000000000000000843593693224077402456720589251805983549672198<br><br>-0.00000000000000000000000000000000000000000000000000000000000000000000000000000000000102625981677427532379241020055915482302818245<br><br>0.00000000000000000000000000000000000000000000000000000000000000000000000000000000000012267176568283274837672614763384918773986133<br><br>-0.00000000000000000000000000000000000000000000000000000000000000000000000000000000000001421319507618214156346648325152478178549807<br><br>0.00000000000000000000000000000000000000000000000000000000000000000000000000000000000000156580949030229658683142149360551107251072<br><br>-0.00000000000000000000000000000000000000000000000000000000000000000000000000000000000000015995318062396177094521184759359302325079<br><br>0.00000000000000000000000000000000000000000000000000000000000000000000000000000000000000001468661860210306721310183054595937895505<br><br>-0.00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000116614925472654571330498298650548807495<br><br>0.00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000007614777707935875830049462101348949930<br><br>-0.00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000380292841621387853386840208666017802<br><br>0.00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000012827656144638619781338571732916502<br><br>-0.00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000218049257000709017436253012230237<br><br>|𝑎𝑝|
|---|---|---|
|𝑝|87<br>88<br>89<br>90<br>91<br>92<br>93<br>94<br>95<br>96<br>97<br>98<br>99<br>100<br>|𝑝|


|𝑏𝑝<br><br>43|22964659026731662286390654676909123899689166376832052239735<br><br>-0.02316346059073084765116552642720018104545001014596264722478965457659723311382886327186557407279722375919299170813555292706053273<br><br>0.00117055009738371923883586925558687165622850288142052568396302488019747209991589548600529080807443850935071498170077042683798424<br><br>-0.00007845159525437915038502792165832119901038961215248844398808658943694139861261149529979387302170261581669509813473783075755960<br><br>0.00000610178237044628533230298822268990953790262896190017750194403093348467248340832520887861010195294760869700709601084842958146<br><br>-0.00000052009749369734457624196511856182756842364965190922715873326904011722795939095756133213413459772421016866628709339695479837<br><br>0.00000004716048719323026016962146240115292301730419351360452195728031621509007487530119784377060607512711875733268720745381058157<br><br>-0.00000000447126480926096747352520489301311549059663732590268047760546569224386977254240244838688643305230022562630847483191266594<br><br>0.00000000043843194080269559182644754603387467792414053175117043821909145375871527823423317212393269059722078626700962663261736071<br><br>-0.00000000004413778800416697987488111621886316972971777963650253306012024129999288565136520457054049956121834345143245252834524094<br><br>0.00000000000453850435772300502954620138881926113395849977050079238233303792339074334569809196529392701461789312735380240119972256<br><br>-0.00000000000047486278974912034286589067491552878774479637193124576808690075176362156330115195535199055003415188530210905162180252<br><br>0.00000000000005041269366573337264284738549684527612711308685656056720785968677824796325858875903372436174310168374512545650535332<br><br>-0.00000000000000541841618794557231371070940216068718266116912845079186467540276563822875049011184703554378702570907294736853128573<br><br>0.00000000000000058858832900333091258330415756181530252816126430130927258440399742988060678786813627227959312721665247343200197643<br><br>-0.00000000000000006452865046019881690193229702423234394266581730429386093120750533882537148265525101956496103051609251347741235428<br><br>0.00000000000000000713184602745285983051433421344021465203851270055667989477399624009688486431914661536929826202761724811871840587<br><br>-0.00000000000000000079387568585334837070391092205296679510736843569182769646154851948665023095367011771242662073488945666936998953<br><br>0.00000000000000000008893321548244486214039081944855655945918195093438781586307498990499528098749606669065758926471710467540047864<br><br>-0.00000000000000000001001957549700270083508893225362985836632615526906939557708140345148409323539993515199249935730116780451406997<br><br>0.00000000000000000000113465531831668981697562638356703154556024045986347218789808664711742215819338248894742120026825744832313722<br><br>-0.00000000000000000000012909158102361956404235943698783179138024781235454548651727492369987543101334262582915647238742305585314009<br><br>0.00000000000000000000001474923829230891569573392420268330241574156683436172535947440264730427883175637259680058394418040445465534<br><br>-0.00000000000000000000000169169006107069139629791161738387615344718638919176357414660585878085398954275870491626263567271342893412<br><br>0.00000000000000000000000019472106989649246522258324010344258833344100105523240948613184828934792986360979817277966652468538217674<br><br>-0.00000000000000000000000002248660696695523188014261533893506417678074602881156248759550802280384621121670987985737153626023553731|𝑏𝑝|
|---|---|---|
|𝑝|2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>23<br>24<br>25<br>26<br>|𝑝|


000000000000000000000000000000000000000000000000000000000000000055762414595158347063192888926077011963403074360

000000000000000000000000000000000000000000000000000000000000000000843593693224077402456720589251805983549672198

000000000000000000000000000000000000000000000000000000000000000000012267176568283274837672614763384918773986133

000000000000000000000000000000000000000000000000000000000000000000000156580949030229658683142149360551107251072

000000000000000000000000000000000000000000000000000000000000000000000001468661860210306721310183054595937895505

000000000000000000000000000000000000000000000000000000000000000000000000007614777707935875830049462101348949930

000000000000000000000000000000000000000000000000000000000000000000000000000012827656144638619781338571732916502

11.02206573731609905553110386543900423140398430546973159699475880968

30.00117055009738371923883529080807443850935071498170077042683798424

50.00000610178237044628533887861010195294760869700709601084842958146

70.00000004716048719323026784377060607512711875733268720745381058157

90.00000000043843194080269317212393269059722078626700962663261736071

110.00000000000453850435772809196529392701461789312735380240119972256

130.00000000000005041269366858875903372436174310168374512545650535332

150.00000000000000058858832678786813627227959312721665247343200197643

170.00000000000000000713184486431914661536929826202761724811871840587

190.00000000000000000008893528098749606669065758926471710467540047864

210.00000000000000000000113742215819338248894742120026825744832313722

230.00000000000000000000001730427883175637259680058394418040445465534

250.00000000000000000000000828934792986360979817277966652468538217674

000000000000000000000000000000000000000000000000000000000000000006872615798301534950869865375959585368851772949

000000000000000000000000000000000000000000000000000000000000000000102625981677427532379241020055915482302818245

000000000000000000000000000000000000000000000000000000000000000000001421319507618214156346648325152478178549807

000000000000000000000000000000000000000000000000000000000000000000000015995318062396177094521184759359302325079

000000000000000000000000000000000000000000000000000000000000000000000000116614925472654571330498298650548807495

000000000000000000000000000000000000000000000000000000000000000000000000000380292841621387853386840208666017802

000000000000000000000000000000000000000000000000000000000000000000000000000000218049257000709017436253012230237

2-0.02316346059073084765116557407279722375919299170813555292706053273

4-0.00007845159525437915038979387302170261581669509813473783075755960

6-0.00000052009749369734457133213413459772421016866628709339695479837

8-0.00000000447126480926096244838688643305230022562630847483191266594

10-0.00000000004413778800416520457054049956121834345143245252834524094

12-0.00000000000047486278974115195535199055003415188530210905162180252

14-0.00000000000000541841618049011184703554378702570907294736853128573

16-0.00000000000000006452865148265525101956496103051609251347741235428

18-0.00000000000000000079387023095367011771242662073488945666936998953

20-0.00000000000000000001001409323539993515199249935730116780451406997

22-0.00000000000000000000012987543101334262582915647238742305585314009

24-0.00000000000000000000000878085398954275870491626263567271342893412

26-0.00000000000000000000000802280384621121670987985737153626023553731

𝑎𝑝

𝑎𝑝

𝑝𝑏𝑝

𝑝𝑏𝑝

|𝑏𝑝|0.0000000000000000000000000026046273546519375493934270133591364665705019612858547009716009<br><br>-0.00000000000000000000000000030253924485017718865960871236635856160042902739053621928855674487536279588648581836346115874581093123<br><br>0.00000000000000000000000000003523272909337653237779542395823859099308870029672548617048433030539547793520222875984603428230495978<br><br>-0.00000000000000000000000000000411303223137921622816749678238895201096694999113287940394757075059166303156268110629856365016520934<br><br>0.00000000000000000000000000000048123774047691143253802517132972575397282638184456385665934728886394624805178954746991056266709423<br><br>-0.00000000000000000000000000000005642559349469213203367668939112137942851003184997428253527781183666879008568436602935012970315863<br><br>0.00000000000000000000000000000000662909868573311871789588471291109933754192484601934454868859162683920749247481661582702308554391<br><br>-0.00000000000000000000000000000000078026633675040835701852286162686108717083549428914666313976341929943958384902663131936751812823<br><br>0.00000000000000000000000000000000009200130410329765264938462253338931973079948091781780377169263455277592349130986816224392341534<br><br>-0.00000000000000000000000000000000001086587088795343412248534254116285808847177753199971566014988266311228544350287691735277320142<br><br>0.00000000000000000000000000000000000128533058235929497049089952492775974975139938117167349848775072258580679482823863801885806732<br><br>-0.00000000000000000000000000000000000015226790894999180428671756131228272201703708773282754084747638362465157337376704629005005967<br><br>0.00000000000000000000000000000000000001806390041204563183044450205988022085553421135844580500614529801585302142501674671979207257<br><br>-0.00000000000000000000000000000000000000214581963070086979607000993486744927329290148261618641156268026953663199927729947014483562<br><br>0.00000000000000000000000000000000000000025522586505921162949136824540185120502549546450899750990168464760717663289547368606697893<br><br>-0.00000000000000000000000000000000000000003039339976397793471210448164934553750192373732833177466011430972211563321386531014706012<br><br>0.00000000000000000000000000000000000000000362353317531057898850627720443445721610579026548071159561650923261004232738730627611801<br><br>-0.00000000000000000000000000000000000000000043247450991141856737163055563821568362897913470041436822399776951815884914383355968842<br><br>0.00000000000000000000000000000000000000000005167049445197177381919496760235514626182986883177659857585900770340527432742853727039<br><br>-0.00000000000000000000000000000000000000000000617957330489485490032415101169389655647864765492672800562003867200892279845821312894<br><br>0.00000000000000000000000000000000000000000000073975748664476103535099888790133409563430535398366541775483950735578690106644027440<br><br>-0.00000000000000000000000000000000000000000000008863753948463911575245954680926253761937997338041899517984896295978772884259738918<br><br>0.00000000000000000000000000000000000000000000001062984621224640716318940995956490914693495781109767212517284433790115286550583921<br><br>-0.00000000000000000000000000000000000000000000000127585631090748460335848430470852384615778486097094289869491803958259876008973712<br><br>0.00000000000000000000000000000000000000000000000015325953316364338251976393341603765524212295949584887398909600348773564440122665<br><br>-0.00000000000000000000000000000000000000000000000001842427816163593516505308530593604446333112679410957856954037338130729231310612<br><br>0.00000000000000000000000000000000000000000000000000221655140079606131603702873412117410068161214605032572141466107747405482737792<br><br>-0.00000000000000000000000000000000000000000000000000026685619615272784141429265485048830685691060109087240779736517357315760098456<br><br>0.00000000000000000000000000000000000000000000000000003214973712363550244199448444032422240545996397390073265661769536183709113685<br><br>-0.00000000000000000000000000000000000000000000000000000387585327835244441098543216619581741739710274249376702318687193208162913564<br><br>0.00000000000000000000000000000000000000000000000000000046755929424754938169215207020422232023101579971140376456833241676591775007<br><br>-0.00000000000000000000000000000000000000000000000000000005643853879849716055792610516651871494725212852846988413720937526287923825<br><br>0.00000000000000000000000000000000000000000000000000000000681671706622268944664004713816863763326391262449156861756806499728842564<br><br>-0.00000000000000000000000000000000000000000000000000000000082380879646684289067620231937844894224228829618260088509451981960933605<br><br>0.00000000000000000000000000000000000000000000000000000000009961411403265835887411781837110664340902329075041693576559242917464528<br><br>-0.00000000000000000000000000000000000000000000000000000000001205176568507052529041691720167828605605177530275339794336283572721083<br><br>0.00000000000000000000000000000000000000000000000000000000000145884204447581481660582048048153974971515945684357636342943629684526<br><br>-0.00000000000000000000000000000000000000000000000000000000000017667961728170528000576792667621868411541660759849978590782632609593<br><br>0.00000000000000000000000000000000000000000000000000000000000002140811101251326040856439038824440240421444446232730304347414207885<br><br>-0.00000000000000000000000000000000000000000000000000000000000000259523933771640839395506227308797276439265244435789124567628998166<br><br>0.00000000000000000000000000000000000000000000000000000000000000031475844970368527207859988440756946780234602898258301523330011604<br><br>-0.00000000000000000000000000000000000000000000000000000000000000003819199275948086232250066986474409024788436219755205198795932355<br><br>0.00000000000000000000000000000000000000000000000000000000000000000463613921141885306633052587623577878432147020683041743030130178<br><br>-0.00000000000000000000000000000000000000000000000000000000000000000056302071895358497326551329253255067928964476053463704432078804<br><br>0.00000000000000000000000000000000000000000000000000000000000000000006840232492396395663308128089976226674456407391969807723301249<br><br>-0.00000000000000000000000000000000000000000000000000000000000000000000831361414863747302543682188983858540128315562437846855903945<br><br>0.00000000000000000000000000000000000000000000000000000000000000000000101087762475684690072626638918750137063439086931801825227150<br><br>|𝑏𝑝|
|---|---|---|
|𝑝|27<br>28<br>29<br>30<br>31<br>32<br>33<br>34<br>35<br>36<br>37<br>38<br>39<br>40<br>41<br>42<br>43<br>44<br>45<br>46<br>47<br>48<br>49<br>50<br>51<br>52<br>53<br>54<br>55<br>56<br>57<br>58<br>59<br>60<br>61<br>62<br>63<br>64<br>65<br>66<br>67<br>68<br>69<br>70<br>71<br>72<br>73<br>|𝑝|


5012169041977526170349037289687768861

0539547793520222875984603428230495978

8886394624805178954746991056266709423

9162683920749247481661582702308554391

9263455277592349130986816224392341534

8775072258580679482823863801885806732

0614529801585302142501674671979207257

0990168464760717663289547368606697893

1159561650923261004232738730627611801

7659857585900770340527432742853727039

8366541775483950735578690106644027440

1109767212517284433790115286550583921

5949584887398909600348773564440122665

1214605032572141466107747405482737792

5996397390073265661769536183709113685

3101579971140376456833241676591775007

3326391262449156861756806499728842564

4340902329075041693576559242917464528

3974971515945684357636342943629684526

4440240421444446232730304347414207885

0756946780234602898258301523330011604

7623577878432147020683041743030130178

8089976226674456407391969807723301249

6638918750137063439086931801825227150

7536279588648581836346115874581093123

5059166303156268110629856365016520934

1183666879008568436602935012970315863

6341929943958384902663131936751812823

4988266311228544350287691735277320142

4747638362465157337376704629005005967

1156268026953663199927729947014483562

7466011430972211563321386531014706012

1436822399776951815884914383355968842

2672800562003867200892279845821312894

8041899517984896295978772884259738918

6097094289869491803958259876008973712

2679410957856954037338130729231310612

1060109087240779736517357315760098456

9710274249376702318687193208162913564

4725212852846988413720937526287923825

4224228829618260088509451981960933605

8605605177530275339794336283572721083

1868411541660759849978590782632609593

8797276439265244435789124567628998166

6474409024788436219755205198795932355

9253255067928964476053463704432078804

2188983858540128315562437846855903945

𝑏𝑝

𝑏𝑝

|𝑏𝑝|-0.0000000000000000000000000000000000000000000<br><br>0.00000000000000000000000000000000000000000000000000000000000000000000001523094504376195525840058198589089909099106106553807071320<br><br>-0.00000000000000000000000000000000000000000000000000000000000000000000000117299039745586326404875273916993576491873683755772837791<br><br>0.00000000000000000000000000000000000000000000000000000000000000000000000174592008510384125277934069832205616241191670358249124656<br><br>0.00000000000000000000000000000000000000000000000000000000000000000000000349419675898782669372040249072202278479470709387245197289<br><br>0.00000000000000000000000000000000000000000000000000000000000000000000000799670625368605793111544759252532945626113982364236937884<br><br>0.00000000000000000000000000000000000000000000000000000000000000000000001783736086252667800700690586334884589640117941023274188714<br><br>0.00000000000000000000000000000000000000000000000000000000000000000000003914629772923365981969623359065939745500344906392471974273<br><br>0.00000000000000000000000000000000000000000000000000000000000000000000008451862719318529215558189995798248228386015610623753894175<br><br>0.00000000000000000000000000000000000000000000000000000000000000000000017959488730997370412819250470216213014764808997616858075849<br><br>0.00000000000000000000000000000000000000000000000000000000000000000000037573129823027411320438637897746148414417808350459988510191<br><br>0.00000000000000000000000000000000000000000000000000000000000000000000077421493364609642333947794718727741247348087249217298429214<br><br>0.00000000000000000000000000000000000000000000000000000000000000000000157181555687935344929847398330810280467371631725554948612501<br><br>0.00000000000000000000000000000000000000000000000000000000000000000000314520476093280876644811508736958575816347686854506891900222<br><br>0.00000000000000000000000000000000000000000000000000000000000000000000620513768424215799858556499474177582182607773184311918853263<br><br>0.00000000000000000000000000000000000000000000000000000000000000000001207406287495543277451628598395555346789389222171356692562722<br><br>0.00000000000000000000000000000000000000000000000000000000000000000002317906407517644807430502076115241195672454732221700657294525<br><br>0.00000000000000000000000000000000000000000000000000000000000000000004391535644933142572262434185505603203399456343798168972287851<br><br>0.00000000000000000000000000000000000000000000000000000000000000000008213898261760714205027379987554661751530583907334785461102139<br><br>0.00000000000000000000000000000000000000000000000000000000000000000015171403728662894570055491378016484782263596816769234952817404<br><br>0.00000000000000000000000000000000000000000000000000000000000000000027680490412828741154710809310842123167257343965385307676036850<br><br>0.00000000000000000000000000000000000000000000000000000000000000000049902044928126690148948862379411085268486828266377908190620281<br><br>0.00000000000000000000000000000000000000000000000000000000000000000088916314010515705566014683642516706025000215138127727366871509<br><br>0.00000000000000000000000000000000000000000000000000000000000000000156632610036345267314420852986615817614367561071128915960553046<br><br>0.00000000000000000000000000000000000000000000000000000000000000000272858050807521788889043076064881355400620297213673392963699625<br><br>0.00000000000000000000000000000000000000000000000000000000000000000470174044807231982937532481326520156804492073444884756225621778<br><br>0.00000000000000000000000000000000000000000000000000000000000000000801601513689780222612781336297434728778902276505467370784946042|𝑏𝑝|
|---|---|---|
|𝑝|74<br>75<br>76<br>77<br>78<br>79<br>80<br>81<br>82<br>83<br>84<br>85<br>86<br>87<br>88<br>89<br>90<br>91<br>92<br>93<br>94<br>95<br>96<br>97<br>98<br>99<br>100<br>|𝑝|


0000000000000000000000001523094504376195525840058198589089909099106106553807071320

0000000000000000000000000174592008510384125277934069832205616241191670358249124656

0000000000000000000000000349419675898782669372040249072202278479470709387245197289

0000000000000000000000000799670625368605793111544759252532945626113982364236937884

0000000000000000000000001783736086252667800700690586334884589640117941023274188714

0000000000000000000000003914629772923365981969623359065939745500344906392471974273

0000000000000000000000008451862719318529215558189995798248228386015610623753894175

0000000000000000000000017959488730997370412819250470216213014764808997616858075849

0000000000000000000000037573129823027411320438637897746148414417808350459988510191

0000000000000000000000077421493364609642333947794718727741247348087249217298429214

0000000000000000000000157181555687935344929847398330810280467371631725554948612501

0000000000000000000000314520476093280876644811508736958575816347686854506891900222

0000000000000000000000620513768424215799858556499474177582182607773184311918853263

0000000000000000000001207406287495543277451628598395555346789389222171356692562722

0000000000000000000002317906407517644807430502076115241195672454732221700657294525

0000000000000000000004391535644933142572262434185505603203399456343798168972287851

0000000000000000000008213898261760714205027379987554661751530583907334785461102139

0000000000000000000015171403728662894570055491378016484782263596816769234952817404

0000000000000000000027680490412828741154710809310842123167257343965385307676036850

0000000000000000000049902044928126690148948862379411085268486828266377908190620281

0000000000000000000088916314010515705566014683642516706025000215138127727366871509

0000000000000000000156632610036345267314420852986615817614367561071128915960553046

0000000000000000000272858050807521788889043076064881355400620297213673392963699625

0000000000000000000470174044807231982937532481326520156804492073444884756225621778

0000000000000000000801601513689780222612781336297434728778902276505467370784946042

0000000000000000000000012284024804151465169365011337828818556201671466330776051102

0000000000000000000000000117299039745586326404875273916993576491873683755772837791

𝑏𝑝

𝑏𝑝

### B Python code to compute upper and lower bounds

Given precomputed values for 𝑎 and 𝑏 it is relatively simple to compute (non-rigorous) upper and lower bounds for 𝜈22 using the python code and the mpmath package. Here is an examplethatuses16coefficients forboth 𝑎, 𝑏 and Richardsonextrapolation[23]toestimate the required infinite series. When run, the above script gives bounds on 𝜈22 precise to the first 32 digits.

⊳ ⊲

- 1 from mpmath import mp, besselj , fabs , factorial , inf , mpf, nstr , nsum, pi , power
- 2
- 3 mp. dps = 128 # d i g i t s of p r e c i s i o n f o r the computation
- 4 epsilon = mpf( ”1e−50” ) # t o l e r a n c e f o r s e r i e s e x t r a p o l a t i o n
- 5
- 6 half = mpf( ” 0.5 ” )
- 7 pi_on_two = pi ( ) / mpf(2)
- 8 four_on_pi = mpf(4) / pi ( )
- 9 four_on_three = mpf(4) / mpf(3)
- 10
- 11
- 12 a_raw = [
- 13 ”0.9860206557159394456200552925916864935048606984660867659294396429” ,
- 14 ”0.01489770489081501339564402620613813180180708471357153405253588246” ,
- 15 ” −0.0010020514702611618623176011272831244046954374945414171879461225” ,
- 16 ”0.00009204407950297445040292960936251992007718734943876628562920974158” ,
- 17 ” −0.000009222749045097728828924770054951562677689395741936839825232504163” ,
- 18 ”0.0000009624829377769523619143359767714486583855960157862298060806209062” ,
- 19 ” −0.0000001030825466711237741281471720057151615014390669675059116945030138” ,
- 20 ”0.00000001125442999323010937747021511295873118119894549766096679782964655” ,
- 21 ” −0.000000001247526888343701534748343542688166570551788621599324821760315743” ,
- 22 ”0.0000000001399983570650130576391202478311227452665491901794575795215352259” ,
- 23 ” −0.00000000001587108251776074729790745823335658801904906951652187759074734197” ,
- 24 ”0.000000000001814579367249737396442135781162248916865862480501175051507144029” ,
- 25 ” −0.0000000000002089593636121966668255461641156413600243015932298164695606951635” ,
- 26 ”0.00000000000002421093838520663536817465987901271450247981787657530210660769827” ,
- 27 ” −0.000000000000002820080540615667295860418397000186709552077272721342675500717904” ,
- 28 ”0.0000000000000003300013142065405729012802718842249459836838193432161048014012172” ,
- 29 ]
- 30 b_raw = [
- 31 ”1.02206573731609906209062285721046071122061035703720832517287196” ,
- 32 ” −0.02316346059073084779982636448754076645713917827003597676237278346” ,
- 33 ”0.001170550097383719246348345976716843011939144437093896137463616238” ,
- 34 ” −0.00007845159525437915088852263273588842719505793132135524091157766925” ,
- 35 ”0.000006101782370446285371463634245302883258983942949246427102319026463” ,
- 36 ” −0.0000005200974936973445795799002679008593946736768461635427163052152714” ,
- 37 ”0.00000004716048719323026047229288414394196590695665909728438524673409874” ,
- 38 ” −0.000000004471264809260967502221347731032458818596936687059973281105908718” ,
- 39 ”0.0000000004384319408026955946402611166292815653609028048460793198243935738” ,
- 40 ” −0.00000000004413778800416698015815314844080164423842416912926126118301283395” ,
- 41 ”0.000000000004538504357723005058673881111666831256023609333041237569856360479” ,
- 42 ” −0.0000000000004748627897491203459135138921486404308021033117402122537914927201” ,
- 43 ”0.00000000000005041269366573337296639115219231576962662698765250656699572447564” ,
- 44 ” −0.000000000000005418416187945572348485577704094735652600218337097929409831514064” ,
- 45 ”0.0000000000000005885883290033309163608068290402251544028088755111511925945235308” ,
- 46 ” −0.00000000000000006452865046019881731607090203710559895373215919872457713898102322” ,
- 47 ]
- 48
- 49 # cast the c o e f f i c i e n t s to mpf ’ s and then normalise them
- 50 tmp = [mpf( x ) for x in a_raw ]


- 51 s = sum(tmp)
- 52 a = [ x / s for x in tmp]
- 53
- 54 tmp = [mpf( x ) for x in b_raw ]
- 55 s = sum(tmp)
- 56 b = [ x / s for x in tmp] # we are using sum b = 1.
- 57
- 58
- 59 # We multiply the B e s s e l J functions by these amplitudes
- 60 j_amps = [ f a c t o r i a l (p) ∗ power( four_on_pi , p) for p in range ( len ( a ) + 2)]
- 61
- 62
- 63 def big_J (p , k ) :
- 64 return j_amps [p] ∗ besselj (p , k ∗ pi_on_two ) / power(k , p)
- 65
- 66
- 67 def big_F (k ) :
- 68 return power(sum( [ big_J (p , k) ∗ v for p , v in enumerate ( a ) ] ) , 4)
- 69
- 70
- 71 def big_G (k ) :
- 72 return power(
- 73 fabs (sum( [ big_J (p + 1 , k) ∗ v for p , v in enumerate (b ) ] ) ) , four_on_three
- 74 )
- 75
- 76
- 77 # group the summands in 4s l i k e t h i s so that t h e i r asymptotics are b e t t e r behaved .
- 78 # gives b e t t e r s e r i e s e x t r a p o l a t i o n s
- 79 def the_F_summand(n ) :
- 80 return big_F (4 ∗ n − 3) + big_F (4 ∗ n − 2) + big_F (4 ∗ n − 1) + big_F (4 ∗ n)
- 81
- 82
- 83 def the_G_summand(n ) :
- 84 return big_G (4 ∗ n − 3) + big_G (4 ∗ n − 2) + big_G (4 ∗ n − 1) + big_G (4 ∗ n)
- 85
- 86
- 87 # use richardson e x t r a p o l a t i o n s to estimate the i n f i n i t e s e r i e s
- 88 sum_F = nsum(the_F_summand , [1 , inf ] , method=”r” , tol=epsilon , verbose=True )
- 89 sum_G = 2 ∗ nsum(the_G_summand , [1 , inf ] , method=”r” , tol=epsilon , verbose=True )
- 90
- 91 print ( ”Sum␣of␣F(k)^4:\n\t ” , nstr (sum_F , 64))
- 92 print ( ”Sum␣of␣abs (G(k))^(4/3):\n\t ” , nstr (sum_G, 64))
- 93
- 94 nu_u = half + sum_F
- 95 nu_l = half + half / power(sum_G, 3)
- 96
- 97 print ( ”This␣gives␣bounds : ” )
- 98 print ( nstr ( nu_l , 36) , ”<=␣nu_2^2␣<=” )
- 99 print ( nstr (nu_u , 36))
- 100 print ( ” delta : ” , nstr (nu_u − nu_l , 4))


⊳ ⊲

−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−− Adding terms #0−#10

- Direct error : 0.000105053 Richardson error : 0.0746387 −−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−− Adding terms #10−#30
- Direct error : 1.10602e−5 Richardson error : 9.5303e−7


- −−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−− Adding terms #30−#60
- Direct error : 2.72974e−6 Richardson error : 4.77855e−22 −−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−− Adding terms #60−#100 Direct error : 9.77732e−7 Richardson error : 7.45014e−51 −−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−− Adding terms #0−#10 Direct error : 0.00132661

- Richardson error : 0.942536 −−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−− Adding terms #10−#30

- Direct error : 0.000139668

Richardson error : 1.20349e−5 −−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−− Adding terms #30−#60 Direct error : 3.44711e−5 Richardson error : 6.03435e−21 −−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−− Adding terms #60−#100

- Direct error : 1.23468e−5 Richardson error : 9.39307e−50 −−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−− Adding terms #100−#150 Direct error : 5.47363e−6


- Richardson error : 2.02238e−85 Sum of F(k)^4:




0.07463960715151959272725542752705485435561425481480583579118891616 Sum of abs (G(k ))^(4/3):

1.88509635262914968733569626740377511940895683024823141154615938 This gives bounds : 0.574639607151519592727255427527052952 <= nu_2^2 <= 0.574639607151519592727255427527054854 delta : 1.903e−33

⊳ ⊲

