---
type: source
kind: paper
title: A model problem for multiplicative chaos in number theory
authors: Kannan Soundararajan, Asif Zaman
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2108.07264v1
source_local: ../raw/2021-soundararajan-model-problem-multiplicative-chaos.pdf
topic: general-knowledge
cites:
---

arXiv:2108.07264v1[math.NT]16Aug2021

A MODEL PROBLEM FOR MULTIPLICATIVE CHAOS IN NUMBER THEORY

KANNAN SOUNDARARAJAN AND ASIF ZAMAN

Abstract. Resolving a conjecture of Helson, Harper recently established that partial sums of random multiplicative functions typically exhibit more than square-root cancellation. Harper’s work gives an example of a problem in number theory that is closely linked to ideas in probability theory connected with multiplicative chaos; another such closely related problem is the Fyodorov–Hiary–Keating conjecture on the maximum size of the Riemann zeta function in intervals of bounded length on the critical line. In this paper we consider a problem that might be thought of as a simpliﬁed function ﬁeld version of Helson’s conjecture. We develop and simplify the ideas of Harper in this context, with the hope that the simpliﬁed proof would be of use to readers seeking a gentle entry-point to this fascinating area.

1. Introduction

The aim of this article is to describe, in a simple setting, some recent work of Harper [23] on the distribution of random multiplicative functions. The study of random multiplicative functions has been very active in recent years, and turns out to be closely related to problems of “multiplicative chaos” which have recently received attention in the probability literature. On the number theory side, the study of mean values of random multiplicative functions is closely related to problems involving the size of the Riemann zeta function in short intervals of the critical line, a line of investigation originating in the conjectures of Fyodorov, Hiary and Keating [13]. Let us begin by quickly describing the model problem that we study here, and then giving its connections with the problem of random multiplicative functions.

Consider a sequence (X(k))k 1 of independent standard complex Gaussians; thus the real and imaginary parts of X(k) are distributed like independent real Gaussian random variables with mean 0 and variance 12. Deﬁne a sequence of random variables (A(N))N 0 by the formal power series identity

![image 1](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile1.png>)

- (1.1) exp

∞

k=1

X(k) √k

![image 2](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile2.png>)

![image 3](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile3.png>)

zk =

∞

n=0

A(n)zn.

The random variables A(n) are naturally determined by the independent random variables X(k); for example, A(0) = 1, A(1) = X(1), A(2) = X(1)2/2 + X(2)/√2, and so on. With this notation, the main result that we wish to explain is the following.

![image 4](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile4.png>)

Corollary 1.1. For all N 1,

- (1.2) E[|A(N)|2] = 1. However there are positive constants C1 and C2 such that for N 2
- (1.3)


C2 (log N)

C1 (log N)

. In particular, E[|A(N)|] → 0 as N → ∞.

E[|A(N)|]

![image 5](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile5.png>)

![image 6](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile6.png>)

1 4

1 4

![image 7](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile7.png>)

![image 8](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile8.png>)

![image 9](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile9.png>)

Date: August 17, 2021.

1

As mentioned already, the result above is motivated by a breakthrough of Harper on the partial sums of random multiplicative functions. A random Steinhaus multiplicative function f : N → {|z| = 1} is obtained by picking independent random variables f(p) (for prime numbers p) distributed uniformly on the unit circle, and extending this to all natural numbers by (complete) multiplicativity. Thus if n = pα

1 · · ·pα

k then f(n) is the random variable f(p1)α

1

k

· · ·f(pk)αk. Given such a random multiplicative function, an important goal

1

![image 10](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile10.png>)

is to understand the partial sums n x f(n). Since E[f(m)f(n)] = 1 if m = n and 0 otherwise it follows that

- (1.4) E

n x

f(n)

2

= ⌊x⌋ = x + O(1).

Harper showed that even though the variance is about x, surprisingly the typical size of n x f(n) is smaller than √x:

![image 11](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile11.png>)

- (1.5) E


√x (log log x)

![image 12](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile12.png>)

.

f(n) ≍

![image 13](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile13.png>)

1 4

![image 14](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile14.png>)

n x

Here the relation A ≍ B means that C1B A C2B for some absolute positive constants C1 and C2. Harper’s result established the conjecture of Helson [25] that partial sums of random multiplicative functions typically exhibit more than square-root cancellation; the truth of Helson’s conjecture seemed far from clear at the time, and indeed earlier work of Harper, Nikeghbali and Radziwil l  [24] had suggested the opposite of Helson’s conjecture.

Identifying N with log x, we see a strong parallel between the variances given in (1.2) and

- (1.4), and the estimates for the ﬁrst moment in (1.3) and (1.5). For large k, the quantity


ek<p ek+1 f(p) behaves like a complex Gaussian with mean 0 and variance ek<p ek+1 1, which by the prime number theorem is on the scale of ek(e − 1)/k. After normalization, the sum over primes behaves analogously to X(k)/√k. Then the random variable A(N) is analogous to e−N/2 n eN f(n). The key relation of the generating functions (1.1) is paralleled by the Euler product formula

![image 15](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile15.png>)

∞

f(n) ns

=

![image 16](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile16.png>)

n=1

p

f(p) ps

1 −

![image 17](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile17.png>)

−1

= exp

pk

f(pk) kpks

![image 18](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile18.png>)

.

The analogy between our model problem and Harper’s work is perhaps clearer in the “function ﬁeld setting.” Consider the polynomial ring Fq[t] where q is a prime power, and Fq is a ﬁnite ﬁeld with q elements. Many problems in the integers have close parallels in this polynomial ring, and for example a study of multiplicative functions in this framework may be found in [16]. The role of positive integers is played by M, the set of monic polynomials. Let Mn denote the monic polynomials of degree n, so that |Mn| = qn, which mirrors integers of size about x. The role of primes is played by P, the set of irreducible monic polynomials. Letting Pn denote the monic irreducibles of degree n, there is also a well-known analogue of the prime number theorem (indeed of the Riemann hypothesis): |Pn| = qn/n + O(qn/2/n). We can model Steinhaus multiplicative functions in this setting by considering (for monic irreducibles P) independent random variables f(P) uniformly distributed on the unit circle, and then extending these to M by complete multiplicativity: if F = Pα

1 · · ·Pα

k then put f(F) = f(P1)α

1

k

· · ·f(Pk)αk.

1

In the function ﬁeld context, our goal is to understand F∈M

f(F). If we set A(n) = q−n/2 F∈M

N

f(F), then

n

∞

−1

- 1

![image 19](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile19.png>)

- 2z)deg(P)


1 − f(P)(q−

A(n)zn =

f(F)(q−1/2z)deg(F) =

.

n=0

F∈M

P

Writing

√k qk/2

![image 20](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile20.png>)

f(P)r r

,

X(k) =

![image 21](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile21.png>)

![image 22](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile22.png>)

deg(P)|k r=k/deg(P)

we may see that the generating function above equals exp

∞

∞

1 r

X(k) √k

- 1

![image 23](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile23.png>)

- 2z)deg(P


r) = exp

f(P)r(q−

zk .

![image 24](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile24.png>)

![image 25](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile25.png>)

![image 26](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile26.png>)

r=1

P

k=1

This relation mirrors (1.1). Moreover, note that if qk is large then X(k) is a (normalized) sum of about qk/k independent random variables uniformly distributed on the unit circle, so that X(k) is distributed very nearly like a standard complex Gaussian. In this manner we see that our model problem corresponds approximately to the study of Steinhaus multiplicative functions in the Fq[t] setting, and corresponds exactly to the limiting case when q → ∞.

Perhaps one of the earliest occurrences of the model (1.1) is in the work of Hughes, Keating, O’Connell [27] where it arises as a prototypical example of a log-correlated ﬁeld. Our interest arose in trying to simplify and understand Harper’s work, and while we lectured on these results earlier (see for example [7]), we have been slow with writing up this version. In the meantime, independent work of Najnudel, Paquette and Simm [30, (1.14) and Lemma 7.5] motivated by random matrix theory studies more general versions of this model (which they term “holomorphic multiplicative chaos”), establishing the upper bounds in Corollary 1.1 (and Theorem 2.1 below).

We conclude our introduction with a brief discussion of related work. In addition to the Steinhaus model of random multiplicative functions mentioned above, another natural model is the Rademacher class of random multiplicative functions taking values ±1 (independently and with equal probability) on the primes, and extended multiplicatively to all square-free numbers. Harper [23] also established the analogue of (1.5) in this class. Indeed as we shall discuss in the next section, Harper [23] determined the order of magnitude of the 2q-th moment of partial sums for all 0 q 1, with the key feature being that the low moments exhibit more cancellation than what would be obtained by using H¨older’s inequality with the second moment. The complementary range of high moments is studied by Harper in [20]. While the partial sums of random multiplicative functions are typically smaller than expected, there are variant problems where the behavior follows expected Gaussian laws. For example, the sums of random multiplicative functions over suitable short intervals or suitable arithmetic progressions [8], or when restricted to integers without too many prime factors [19], [26], exhibit Gaussian behavior.

Given a random Steinhaus multiplicative function f, one can ask whether almost surely one

has n x f(n) = O(√x) for all x. That is, here we are choosing the multiplicative function f at random, and asking about the behavior of partial sums as x varies, in contrast with our

![image 27](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile27.png>)

earlier discussion where x is ﬁrst ﬁxed and the random multiplicative function varies. This problem, which is an analogue of the law of the iterated logarithm, was raised by Hal´asz [17],

and investigated further in [18] and [28]. Recently Hal´asz’s problem was answered in the negative by Harper [22], who established that almost surely there are arbitrarily large x with

√x(log log x)14−ε for any ε > 0. The law of the iterated logarithm shows that sums of independent random variables (for example taking values ±1 with equal probability) attain values as large as √xlog log x occasionally, and Harper’s result diﬀers from this by about the same amount (log log x)−

![image 28](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile28.png>)

| n x f(n)|

![image 29](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile29.png>)

![image 30](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile30.png>)

1

4 that appears in (1.5). Harper’s result suggests that in our model problem, almost surely there exist arbitrarily large N with |A(N)| (log N)

![image 31](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile31.png>)

1

4−ε. It would be of interest to make this precise, and perhaps obtain a more accurate law of the iterated logarithm in this context.

![image 32](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile32.png>)

Another problem in number theory that is closely related to this circle of ideas concerns the distribution of the Riemann zeta function over typical intervals of length 1 on the critical line Re(s) = 1/2. One vague connection between these problems is that ζ(21 + it) may be thought of as n−

![image 33](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile33.png>)

- 1

![image 34](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile34.png>)

- 2−it for suitable ranges of n, and if t is chosen randomly, the function


nit behaves in some ways like a random Steinhaus multiplicative function. More precisely, a conjecture of Fyodorov, Hiary, and Keating (see [13], [14]) states that if t is chosen uniformly from [T, 2T] then

- (1.6) log log T − 43 log log log T − g(T) max

![image 35](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile35.png>)

t u t+1

log |ζ(12 + iu)| log log T − 34 log log log T + g(T), holds with probability tending to 1 as g(T) tends to inﬁnity with T. The key feature of this conjecture is the secondary term −34 log log log T, which is smaller than the answer −41 log log log T that may be suggested by a crude application of Selberg’s classical theorem that log |ζ(21 + it)| is distributed like a normal random variable with mean 0 and variance ∼ 21 log log T. Another closely related conjecture states that

![image 36](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile36.png>)

![image 37](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile37.png>)

![image 38](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile38.png>)

![image 39](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile39.png>)

![image 40](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile40.png>)

![image 41](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile41.png>)

- (1.7)


2T

1

- 1

![image 42](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile42.png>)

- 2 ≍


1 (log log T)

1 log T

1 T

|ζ(12 + it + ih)|2dh

.

![image 43](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile43.png>)

![image 44](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile44.png>)

![image 45](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile45.png>)

![image 46](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile46.png>)

1 4

![image 47](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile47.png>)

T

0

Since T 2T |ζ(12 + it)|2dt ∼ T log T, the Cauchy–Schwarz inequality shows that the above quantity is ≪ 1, and the interest above is that it is still smaller, and by a factor very similar to

![image 48](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile48.png>)

that arising in (1.5). Indeed there is a very strong analogy between (1.7) and Propositions 3.2 and 8.2 below. There has been a lot of recent progress towards the conjectures in (1.6) and

- (1.7) and other related questions, see [1], [2], [3], [4], [15], [22], [29]. Most notably, the upper bound portion of (1.7) has been established by Harper [21], who also established a slightly weaker version of the upper bound in (1.6). An even more precise version of the upper bound in (1.6) has been established by Arguin, Bourgade and Radziwi ll  [3]. For a recent comprehensive survey on this topic see [5].


The multiplication table problem (which asks for the number of integers n up to N2 that may be written as n = ab with a, b N) exhibits some features in common with these problems, although the link here is perhaps less clearly deﬁned. We content ourselves with referring the reader to [12], and pointing out also the interesting analogous problem of counting permutations in S2N that leave some N-element set ﬁxed (so that such permutations may be thought of as the product of two permutations on N element sets) [11].

Lastly, we mention that there is an extensive literature in probability where related problems are studied under “critical multiplicative chaos”; a few sample references are [6], [9], [10], [31].

Acknowledgments. K.S. is partially supported through a grant from the National Science Foundation, and a Simons Investigator Grant from the Simons Foundation. Part of this work was written while K.S. was a senior Fellow at the ETH Institute for Theoretical Studies, whom he thanks for their warm and generous hospitality. Part of this work was written while A.Z. was a postdoctoral fellow at Stanford University supported by an NSERC Postdoctoral Fellowship. A.Z. is grateful to both institutions for their ﬁnancial support and to the university for providing excellent working conditions. A.Z. also thanks Valeriya Kovaleva for helpful comments and sharing reference [30] with him.

2. Preliminaries

In this section we set up some convenient notation, and make preliminary observations for our analysis of A(N).

By a partition λ we mean a non-increasing sequence of non-negative integers λ1 λ2 . . ., with λn = 0 from some point onwards. We denote by |λ| the sum of the parts λ1 + λ2 + . . ., and for an integer k 1 we denote by mk = mk(λ) the number of parts in λ that are equal to k. Given a partition λ, deﬁne

- (2.1) a(λ) = a(λ; X) =


k

X(k) √k

![image 49](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile49.png>)

![image 50](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile50.png>)

mk 1 mk!

,

![image 51](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile51.png>)

where, as in the introduction, X(k) is a sequence of independent standard complex Gaussians. With this notation, we have

∞

X(k) √k

a(λ)z|λ|,

zk =

exp

![image 52](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile52.png>)

![image 53](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile53.png>)

λ

k=1

so that

- (2.2) A(N) =


a(λ).

|λ|=N

Recall that a standard complex Gaussian Z satisﬁes

E ZmZn =

![image 54](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile54.png>)

n! if m = n, 0 if m = n.

It follows that if λ and λ′ are two diﬀerent partitions then

- (2.3) E[a(λ)a(λ′)] = 0, while if λ = λ′ then

![image 55](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile55.png>)

- (2.4) E[|a(λ)|2] =


1 mk!2kmk

E[|X(k)|2m

] =

k

![image 56](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile56.png>)

k

k

1 mk!kmk

,

![image 57](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile57.png>)

where we again use the notation that the partition λ contains mk parts equal to k. We deduce that

1 mk! · kmk

E[|A(N)|2] =

E[|a(λ)|2] =

= 1,

![image 58](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile58.png>)

|λ|=N k

|λ|=N

where the last step follows from the familiar formula for the number of permutations in SN whose cycle decomposition corresponds to the partition λ. This establishes (1.2), and our main task is to bound the ﬁrst moment in (1.3).

In fact we will determine the order of magnitude of all low moments E[|A(N)|2q] for

- 0 q 1, following Harper who determined the order of magnitude for such moments for random multiplicative functions. Theorem 2.1. Uniformly for any integer N 1 and any 0 q 1,


1 (1 − q)√log N + 1

q

E |A(N)|2q ≍

. In particular (1.3) holds.

![image 59](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile59.png>)

![image 60](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile60.png>)

Naturally one can study A(N) through the generating function ∞n=0 A(n)zn, which converges almost surely for |z| < 1. For example, by Cauchy’s theorem we have for r < 1 the almost sure identity

∞

dz zN+1

- 1

![image 61](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile61.png>)

- 2πi |z|=r


A(n)zn

.

A(N) =

![image 62](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile62.png>)

n=0

Indeed since A(N) depends only on the random variables X(k) for k N, we can avoid all issues of convergence and write (for any K N and any r > 0)

- 1

![image 63](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile63.png>)

- 2πi |z|=r


A(N) =

exp

X(k) √k

zk

![image 64](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile64.png>)

![image 65](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile65.png>)

k K

dz zN+1

.

![image 66](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile66.png>)

We will not use this relation, but it motivates us to deﬁne (for any real number K 1)

- (2.5) FK(z) = exp

k K

X(k) √k

![image 67](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile67.png>)

![image 68](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile68.png>)

zk .

When the parameter K is clear from context, we shall abbreviate FK(z) to F(z). We shall relate the problem of bounding E[|A(N)|2q] to that of estimating

- (2.6) E

- 1

![image 69](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile69.png>)

- 2π


2π

0

|FK(reiθ)|2dθ

q

. Here K will be a parameter of size about N, and r will be a parameter close to 1.

- Lemma 2.2. For any K 1, any r > 0, and any θ ∈ R, we have


E[|FK(reiθ)|2] = exp

k K

r2k k

![image 70](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile70.png>)

.

Proof. Since the complex Gaussian is rotationally symmetric, the variables X(k) and X(k)eikθ are identically distributed and therefore |FK(reiθ)|2 is distributed identically as |FK(r)|2. Now Re k K X(k)rk/√k is a sum of independent Gaussians, and therefore is distributed like a real Gaussian with mean 0 and variance 21 k K r2k/k. The lemma follows upon recalling that if Z is a real Gaussian with mean zero and variance σ2 then E[etZ] = et2σ2/2.

![image 71](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile71.png>)

![image 72](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile72.png>)

From Lemma 2.2 and H¨older’s inequality it follows that

- (2.7) E


2π

- 1

![image 73](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile73.png>)

- 2π


- 1

![image 74](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile74.png>)

- 2π


q

|FK(reiθ)|2dθ

E

0

2π

|FK(reiθ)|2dθ

0

r2k k

q

= exp q

![image 75](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile75.png>)

k K

.

Thinking of r = 1 and K = N for simplicity (this is the most relevant range of the parameters) this furnishes an upper bound of size Nq above. The true size of the quantity on the

left side above turns out to be a little bit smaller, by a factor (1 + (1 − q)√log N)q exactly as in Theorem 2.1. We point out that there are close parallels between the moment in (2.7)

![image 76](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile76.png>)

(for q = 1/2) and the corresponding problem for |ζ(12 + it)| considered in (1.7).

![image 77](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile77.png>)

Ultimately the smaller size of the left side of (2.7) can be traced to the “ballot problem” in probability theory. We will borrow from Harper the following extension of classical results on Gaussian random walks.

- Lemma 2.3 (Harper). Let a 1. For any integer n 1, let G1, . . ., Gn be independent real


Gaussian random variables, each having mean zero and variance between 201 and 20, say. Let h be a function such that |h(j)| 10 log j. Then

![image 78](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile78.png>)

j

a √n

.

Gm a + h(j), ∀1 j n ≍ min 1,

P

![image 79](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile79.png>)

![image 80](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile80.png>)

m=1

Proof. This is [23, Probability Result 1, p. 29]. Harper states the result with a and n being large, but this may be relaxed by adjusting the implied constants suitably.

The term h(j) in Lemma 2.3 is needed, for example, in the upper bound part of our argument to obtain convergence of some sums. It should be thought of as largely harmless, since a sum of j independent Gaussian variables would typically exhibit ﬂuctuations on the scale of √j and h(j) is negligible in comparison to this natural scale.

![image 81](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile81.png>)

With the one exception of Lemma 2.3 above, we have kept the proof of Theorem 2.1 selfcontained. For convenience, we have split the paper into two parts, focussing ﬁrst on the upper bound implicit in Theorem 2.1 (see Sections 3 to 7) and then dealing with the lower bound (see Sections 8 to 11). Note that the relation A ≪ B means that A CB for some absolute positive constant C.

Part I: The upper bound of Theorem 2.1

3. Deducing the upper bound from two propositions

It is enough to prove the upper bound in the range 12 q 1, since by H¨older’s inequality the bound would then hold for all smaller q as well. As mentioned earlier, the problem of bounding E[|A(N)|2q] may be related to the problem of bounding moments of the generating function FK(reiθ) as in (2.6). We make this link precise here, and reduce the upper bound part of the main theorem to two propositions that will be established in the following sections.

![image 82](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile82.png>)

- Proposition 3.1. For 1/2 q 1 and any integer N 1, we have

E[|A(N)|2q]

- 1

![image 83](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile83.png>)

- 2q ≪


1 √N

![image 84](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile84.png>)

![image 85](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile85.png>)

J

j=1

E

- 1

![image 86](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile86.png>)

- 2π


2π

0

|FN/2j(exp(j/N + iθ))|2dθ

q 2 1q

![image 87](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile87.png>)

+

1 N

![image 88](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile88.png>)

,

where J = ⌈4 log log(4N)⌉.

- Proposition 3.2. Let K 1 be a real number and let F(z) = FK(z) be as in (2.5). Uniformly for 1/2 q 1 and 1 r e1/K we have


E

- 1

![image 89](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile89.png>)

- 2π


2π

|F(reiθ)|2dθ

0

q

≪

K (1 − q)√log K + 1

![image 90](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile90.png>)

![image 91](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile91.png>)

q

.

Applying the estimate of Proposition 3.2 in Proposition 3.1 it follows that for 1/2 q 1

J

N/2j (1 − q)√log N + 1

- 1

![image 92](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile92.png>)

- 2 +


- 1

![image 93](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile93.png>)

- 2q ≪


1 √N

1 N ≪

1 (1 − q)√log N + 1 This establishes the upper bound in Theorem 2.1 in the range 1/2 q 1.

E[|A(N)|2q]

![image 94](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile94.png>)

![image 95](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile95.png>)

![image 96](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile96.png>)

![image 97](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile97.png>)

![image 98](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile98.png>)

![image 99](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile99.png>)

![image 100](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile100.png>)

j=1

- 1

![image 101](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile101.png>)

- 2.


4. Proof of Proposition 3.1

Our starting point is the representation of A(N) as a sum over partitions λ of N, recall (2.1) and (2.2). Group these partitions according to the size of their largest part λ1. For

- 1 j J write


a(λ),

Aj(N) =

|λ|=N N/2j<λ1 N/2j−1

and put

a(λ),

AJ(N) =

|λ|=N λ1 N/2J

so that we have the natural decomposition

J

A(N) =

Aj(N) + AJ(n).

j=1

Minkowski’s inequality gives, for 1/2 q 1,

- (4.1) E[|A(N)|2q]

- 1

![image 102](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile102.png>)

- 2q


J

j=1

E[|Aj(N)|2q]

- 1

![image 103](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile103.png>)

- 2q + E[| AJ(N)|2q]


- 1

![image 104](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile104.png>)

- 2q.


We begin by estimating the last term in the right side of (4.1), showing that it is ≪ 1/N. By H¨older’s inequality, we ﬁnd that

- (4.2) E[| AJ(N)|2q]


1

![image 105](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile105.png>)

q E[| AJ(N)|2] =

|λ|=N λ1 N/2J

k

1 mk!kmk

.

![image 106](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile106.png>)

The right side of (4.2) is the proportion of elements in the symmetric group SN whose cycle decomposition has largest cycle N/2J in length, and it is a familiar fact that such permutations are rare (corresponding to the rarity of integers all of whose prime factors are small). We may supply a quick bound (corresponding to Rankin’s trick with Dirichlet series) on this quantity as follows. The right side of (4.2) is the coeﬃcient of zN in the generating function exp( k N/2J zk/k). Since the coeﬃcients of this generating function are all non-negative, for any r > 0 we conclude that the right side of (4.2) is

r−N exp

rk k ≪ exp(−2J)

N 2J ≪

1 N2

,

![image 107](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile107.png>)

![image 108](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile108.png>)

![image 109](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile109.png>)

k N/2J

upon choosing r = exp(2J/N). Inserting this into (4.2) we conclude that the last term in

- (4.1) is ≪ 1/N. We now focus on bounding the contribution of the j-th term of the sum in (4.1). Recall


that the term Aj(N) sums over partitions λ of N with largest part λ1 lying between N/2j

and N/2j−1. Decompose the partition λ into ρ and σ, where ρ consists of those non-zero parts in λ that lie between N/2j and N/2j−1, and σ consists of those non-zero parts of λ that are N/2j; note that ρ must have at least one non-zero term. It follows from (2.1) that a(λ) = a(ρ)a(σ). Thus, with the above understanding,

Aj(N) =

a(ρ)a(σ).

ρ,σ |ρ|+|σ|=N |ρ|>0

Observe that a(σ) depends only on the random variables X(k) for k N/2j, while a(ρ) depends only on the random variables X(k) with N/2j < k N/2j−1.

We shall bound the expected value of |Aj(N)| by ﬁrst conditioning on the variables X(k) for k N/2j (so that a(σ) is ﬁxed in the notation above), and then bounding the expectation over these small variables X(k). Let Ej denote the conditional expectation when the variables X(k) for k N/2j are ﬁxed. We shall show that

- (4.3) Ej |Aj(N)|2q ≪

1 2πN

![image 110](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile110.png>)

2π

0

|FN/2j(exp(j/N + iθ))|2dθ

q

,

so that, upon now taking the expectation over the variables X(k) with k N/2j, we may conclude that

E |Aj(N)|2q ≪ E

- 1

![image 111](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile111.png>)

- 2πN


2π

0

|FN/2j(exp(j/N + iθ))|2dθ

q

. This would complete the proof of our proposition.

It remains now to establish (4.3). By H¨older’s inequality, Ej |Aj(N)|2q Ej |Aj(N)|2

q

, so that (4.3) follows from the estimate

- (4.4) Ej |Aj(N)|2 ≪

- 1

![image 112](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile112.png>)

- 2πN


2π

0

|FN/2j(exp(j/N + iθ))|2dθ . Expanding out the expression for Aj(N) in terms of a(ρ) and a(σ), we ﬁnd Ej |Aj(N)|2 =

ρ1,σ1 |ρ1|+|σ1|=N |ρ1|>0

ρ2,σ2 |ρ2|+|σ2|=N |ρ2|>0

a(σ1)a(σ2)Ej a(ρ1)a(ρ2) .

![image 113](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile113.png>)

![image 114](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile114.png>)

Now note (2.3) implies that Ej[a(ρ1)a(ρ2)] = 0 unless ρ1 = ρ2. Thus, writing n = |ρ1| = |ρ2| with N/2j < n N (and so |σ1| = |σ2| = N − n), we obtain

![image 115](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile115.png>)

- (4.5) Ej |Aj(N)|2 =


a(σ)

N/2j<n N |σ|=N−n

2

Ej |a(ρ)|2 .

|ρ|=n

To proceed further, we must estimate the sum over the partitions ρ above. Recall that all parts of ρ must be between N/2j and N/2j−1, and denote (as before) by mk the number of parts of size k in ρ (so N/2j < k N/2j−1). Then by (2.4), we have that

1 mk!kmk

Ej |a(ρ)|2 =

![image 116](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile116.png>)

N/2j<k N/2j−1

2j N

![image 117](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile117.png>)

r

,

where r denotes the number of parts in ρ (so that 2j−1n/N r < 2jn/N). Thus

Ej |a(ρ)|2

|ρ|=n

#{ρ : |ρ| = n, ρ has r parts}

2j−1n/N r<2jn/N

2j N

![image 118](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile118.png>)

r

.

The number of partitions ρ of n with r parts (all between N/2j and N/2j−1) is at most

[N/2j]+r

r−1 , since r − 1 parts may be freely chosen among the integers in (N/2j, N/2j−1] and the ﬁnal part has at most one possibility. Thus, using r 2j N/2j for large N,

Ej |a(ρ)|2

|ρ|=n

2j−1n/N r<2jn/N

2j N

![image 119](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile119.png>)

r(N/2j + r)r−1 (r − 1)!

![image 120](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile120.png>)

2j N

2r−1 (r − 1)!

.

![image 121](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile121.png>)

![image 122](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile122.png>)

2j−1n/N r<2jn/N

If n N/2 then the sum over r above is ≪ 1, while if n > N/2 we may bound the sum over r above by ≪ 2−j. Thus in both cases we may conclude that

1 N

N − n N

Ej |a(ρ)|2 ≪

.

exp 2j

![image 123](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile123.png>)

![image 124](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile124.png>)

|ρ|=n

Inserting the above in (4.5) it follows that

Ej |Aj(N)|2 ≪

1 N

a(σ)

![image 125](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile125.png>)

N/2j<n N |σ|=N−n

Now

and so by Parseval

FN/2j(z) =

a(σ) zr,

r |σ|=r

1 N

a(σ)

![image 126](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile126.png>)

N/2j<n N |σ|=N−n

N − n N

2

exp 2j

![image 127](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile127.png>)

- 1

![image 128](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile128.png>)

- 2πN


N − n N

2

exp 2j

![image 129](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile129.png>)

.

2π

|FN/2j(exp(j/N + iθ))|2dθ.

0

This establishes (4.4) and completes the proof of the proposition.

5. Plan for the proof of Proposition 3.2

The proof of the upper bound portion of Theorem 2.1 has now been reduced to establishing Proposition 3.2. By Lemma 2.2 we conclude that for 1 r e1/K,

- (5.1) E


- 1

![image 130](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile130.png>)

- 2π


2π

|F(reiθ)|2dθ = exp

0

r2k k ≍ K.

![image 131](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile131.png>)

k K

By H¨older’s inequality it follows that for 0 < q 1 and 1 r e1/K,

E

- 1

![image 132](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile132.png>)

- 2π


2π

|F(reiθ)|2dθ

0

q

≪ Kq,

so that in Proposition 3.2 we are looking for a small improvement over this easy upper bound. As mentioned earlier, the source of this improvement is connected to the ballot problem in probability.

Deﬁnition 5.1. Let K 3. Suppose 1 r e1/K and 1 A √log K. Deﬁne Gr(A, θ; K) to be the following event: for each 1 n log K, one has

![image 133](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile133.png>)

k<en

r2k k

X(k)rkeikθ √k −

Re

![image 134](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile134.png>)

![image 135](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile135.png>)

![image 136](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile136.png>)

A + 10 log n.

Further, deﬁne Gr(A; K) to be the event where Gr(A, θ; K) holds for all θ ∈ [0, 2π). We shall deduce Proposition 3.2 from the following two propositions concerning Gr(A; K).

- Proposition 5.2. For all 1 r e1/K and all 1 A √log K we have P[Gr(A; K) fails] ≪ exp(−A).

![image 137](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile137.png>)

Thus the event Gr(A; K) is very likely for large A. The crucial point is that on this large set, we can improve upon the upper bound (5.1) for the mean square of F(reiθ).

- Proposition 5.3. With notations as above, we have


A √log K

r(A,θ;K)|F(reiθ)|2 ≍

K, and therefore

E 1G

![image 138](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile138.png>)

![image 139](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile139.png>)

2π

A √log K

|F(reiθ)|2dθ ≪

K.

E 1G

r(A;K)

![image 140](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile140.png>)

![image 141](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile141.png>)

0

Deducing Proposition 3.2 from Propositions 5.2 and 5.3. Assume without loss that K e4. Partition the whole probability space into the events Gr(1; K), Gr(2j; K)\Gr(2j−1; K) for 1 j J := ⌊(log log K)/(2 log 2)⌋, and Gr(2J; K)c. Proposition 5.3 and H¨older’s inequality give

E 1G

r(1;K)

2π

|F(reiθ)|2dθ

0

q

E 1G

r(1;K)

2π

|F(reiθ)|2dθ

0

q

≪

K √log K

![image 142](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile142.png>)

![image 143](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile143.png>)

q

.

For 1 j J, the event Gr(2j; K)\Gr(2j−1; K) means that Gr(2j; K) holds but Gr(2j−1; K) fails. Thus H¨older’s inequality gives

2π

q

|F(reiθ)|2dθ

E 1G

r(2j;K)\Gr(2j−1;K)

0

2π

q

1−q

|F(reiθ)|2dθ

P Gr(2j−1; K) fails

. Using Propositions 5.2 and 5.3, we see that this is

E 1G

r(2j;K)

0

2jK √log K

q K √log K

q

≪ exp(−(1 − q)2j−1)

2j exp(−(1 − q)2j−1) . Similarly we ﬁnd that

![image 144](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile144.png>)

![image 145](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile145.png>)

![image 146](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile146.png>)

![image 147](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile147.png>)

2π

q

≪ Kq exp − (1 − q)2J . Adding up these estimates, we deduce Proposition 3.2.

|F(reiθ)|2dθ

E 1G

r(2J;K)c

0

6. Proof of Proposition 5.2

We prove that the event Gr(A; K) is very likely by showing that k<en ReX(k)rkeikθ/√k is unlikely to exceed the stated barrier for any single 1 n log K and any single θ ∈ [0, 2π].

![image 148](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile148.png>)

From Deﬁnition 5.1, the union bound gives

P[Gr(A; K) fails]

P max

θ

k<en

n log K

X(k)rkeikθ √k

Re

![image 149](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile149.png>)

![image 150](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile150.png>)

r2k k

A + 10 log n +

![image 151](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile151.png>)

k<en

- (6.1) Pn.


=:

n log K

To estimate Pn we discretize the possible values of θ ∈ [0, 2π), setting θj = 2πj/⌈nen⌉ for 0 j < ⌈nen⌉. If the maximum over θ in the deﬁnition of Pn satisﬁes the corresponding inequality, then we must have either

- (6.2)

k<en

Re

X(k)rkeikθ

j

![image 152](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile152.png>)

√k

![image 153](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile153.png>)

A 2

![image 154](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile154.png>)

+ 5 log n +

k<en

r2k k

![image 155](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile155.png>)

, for some 0 j < ⌈nen⌉,

or for some 0 j < ⌈nen⌉, and some θj < θ θj+1 we must have Re

θ

θj k<en

X(k)rk(i

√

![image 156](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile156.png>)

keiky)dy = Re

k<en

X(k)rk √k

![image 157](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile157.png>)

![image 158](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile158.png>)

(eiθk − eiθ

jk)

A 2

![image 159](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile159.png>)

+ 5 log n.

This second case only happens if

- (6.3)

θj+1

θj k<en

X(k)rk

√

![image 160](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile160.png>)

keiky dy

A 2

![image 161](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile161.png>)

+ 5 log n, for some 0 j < ⌈nen⌉.

Since the random variables X(k) are independent and rotationally invariant, it follows that

- (6.4) Pn nen P

′

n + P

′′

n ,

where Pn′ is the probability that the inequality in (6.2) holds for j = 0, and Pn′′ is the probability that the inequality in (6.3) holds for j = 0.

Since Re k<en X(k)rk/√k is a real Gaussian with mean 0 and variance 12 k<en r2k/k, it follows that

![image 162](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile162.png>)

![image 163](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile163.png>)

P

′

n ≪ exp −

k<en

r2k k

![image 164](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile164.png>)

+

A 2

![image 165](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile165.png>)

+ 5 log n

2

k<en

r2k k

![image 166](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile166.png>)

exp −

k<en

r2k k − A − 10 log n ,

![image 167](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile167.png>)

where we used that t ∞ e−x2/2dx ≪ e−t2/2 for t 0. Thus, as 1 r e1/K,

- (6.5) P


e−n−A n10

′

.

n ≪

![image 168](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile168.png>)

Now we turn to the task of estimating Pn′′. By H¨older’s inequality, it follows that if (6.3) holds (with j = 0 there) then for any integer ℓ 1 we must have

θ12ℓ−1

θ1

X(k)rk

0 k<en

√

2ℓ

![image 169](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile169.png>)

keiky

dy

A 2

+ 5 log n

![image 170](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile170.png>)

2ℓ

.

Therefore, by Chebyshev’s inequality, P

√

θ1

A 2

2ℓ

−2ℓ

![image 171](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile171.png>)

′′

keiky

X(k)rk

θ12ℓ−1

dy

+ 5 log n

# E

![image 172](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile172.png>)

n

0

k<en

A 2

−2ℓ

ℓ

kr2k

θ12ℓℓ!

=

+ 5 log n

,

![image 173](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile173.png>)

k<en

since k<en X(k)rk√keiky is distributed like a complex Gaussian with variance k<en kr2k. Since ℓ! ℓℓ, θ1 2π/(nen) and k en kr2k e2+2n (as r e1/K) it follows that

![image 174](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile174.png>)

A 2

2πe n

2ℓ

−2ℓ

′′

ℓℓ

P

+ 5 log n

.

![image 175](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile175.png>)

![image 176](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile176.png>)

n

Upon choosing ℓ to be an integer around n(A/2 + 5 log n), we see that Pn′′ ≪ e−n−A/n10; indeed Pn′′ is much smaller than this, but we have just matched our earlier bound in (6.5). Combining this with (6.4) and (6.5), it follows that Pn ≪ e−A/n9, which when inserted in (6.1) yields Proposition 5.2. Note that the factor 1/n9 ensures that the sum in (6.1) converges, and it is for this reason that the “safety valve” term 10 logn was introduced in Deﬁnition 5.1 (and one of the reasons why Lemma 2.3 has the ﬂexible term h(j)).

7. Proof of Proposition 5.3

The proof of the upper bound in Theorem 2.1 has ﬁnally been reduced to Proposition 5.3, which we shall now obtain as an application of Lemma 2.3. We focus on showing that

A √log K

r(A,θ;K)|F(reiθ)|2 ≍

K. Since Gr(A; K) is the event where Gr(A, θ; K) holds for all θ, it then follows that E 1G

- (7.1) E 1G


![image 177](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile177.png>)

![image 178](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile178.png>)

2π

2π

A √log K

|F(reiθ)|2dθ

r(A,θ;K)|F(reiθ)|2 dθ ≪

K, completing the proof of the proposition. By rotational symmetry it is enough to establish

E 1G

r(A;K)

![image 179](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile179.png>)

![image 180](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile180.png>)

0

0

- (7.1) in the case θ = 0.

Put xk = Re(X(k)) so that the xk are independent real normal variables with mean 0 and variance 1/2. Then we may write

- (7.2) E 1G


2xkrk √k − x2k dx1dx2 · · ·dx⌊K⌋,

1 π⌊K⌋/2 · · ·

r(A,0;K)|F(r)|2 =

exp

![image 181](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile181.png>)

![image 182](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile182.png>)

![image 183](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile183.png>)

k K

R

where R ⊆ R⌊K⌋ is the region given by (xk)⌊kK=1⌋ ∈ R⌊K⌋ satisfying

r2k k

xkrk √k −

A + 10 logn

![image 184](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile184.png>)

![image 185](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile185.png>)

![image 186](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile186.png>)

k<en

for all 1 n log K. Write yk = xk − rk/√k, which completes the square and allows us to express the integral in (7.2) as

![image 187](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile187.png>)

exp

r2k k

![image 188](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile188.png>)

k K

1 π⌊K⌋/2 · · ·

![image 189](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile189.png>)

R′

yk2 dy1 · · ·dy⌊K⌋,

exp −

k K

where R′ ⊆ R⌊K⌋ is the region given by k<en ykrk/√k A+10 logn for all 1 n log K. Since 1 r e1/K, it follows that

![image 190](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile190.png>)

- (7.3) E 1G

r(A,0;K)|F(r)|2 = exp

k K

r2k k

![image 191](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile191.png>)

P[B] ≍ KP[B],

where B is the event that, for all 1 n log K, one has

- (7.4)


ykrk √k

![image 192](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile192.png>)

![image 193](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile193.png>)

k<en

A + 10 logn,

for independent normal random variables yk with mean 0 and variance 12.

![image 194](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile194.png>)

To complete the proof, we are now ready to apply Lemma 2.3 with the random variables Gm = em−1 k<em ykrk/√k for 1 m log K. Note that the variables Gm are Gaussians with variance 12 em−1 k<em r2k/k which lies between 1/20 and 20 as required in Lemma 2.3. Thus, we deduce that P[B] ≍ A/√log K. Using this estimate in (7.3) now ﬁnishes the proof of (7.1) in the case θ = 0. This completes the proof of the proposition, and hence the upper bound of Theorem 2.1.

![image 195](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile195.png>)

![image 196](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile196.png>)

![image 197](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile197.png>)

Part II: The lower bound of Theorem 2.1 8. Deducing the lower bound from two propositions

Now, we turn our focus to the lower bound portion of Theorem 2.1. If 0 q 2 1 then by H¨older’s inequality it follows that

![image 198](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile198.png>)

- 2−4q

![image 199](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile199.png>)

- 3−4q E |A(N)|2q


1 3−4q

E |A(N)| E |A(N)|3/2

![image 200](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile200.png>)

.

The upper bound E[|A(N)|3/2] ≪ (log N)−3/4 in Theorem 2.1 has already been established. If we knew the lower bound E[|A(N)|] ≫ (log N)−1/4, then the desired lower bound for E[|A(N)|2q] would follow. Thus, it is enough to prove the lower bound in the range 21 q 1.

![image 201](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile201.png>)

Here we shall reduce the lower bound part of the main theorem to propositions involving bounds for the second moment of FK(z) deﬁned by (2.1) for any real number K 1.

- Proposition 8.1. For 21 q 1 and 0 < r < 1 we have

![image 202](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile202.png>)

E[|A(N)|2q]

1 4

![image 203](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile203.png>)

E

1 2πN

![image 204](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile204.png>)

2π

0

|FN/2(reiθ)|2dθ

q

− E

rN 2πN

![image 205](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile205.png>)

2π

0

|FN/2(eiθ)|2dθ

q

.

- Proposition 8.2. Let K 10 be a real number, and let F(z) = FK(z) be as in (2.5). Uniformly for 21 q 1 and e−1/40 r < 1 we have


![image 206](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile206.png>)

2π

Kr (1 − q)√log Kr + 1

q

q

|FK(reiθ)|2dθ

≫

,

E

![image 207](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile207.png>)

![image 208](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile208.png>)

0

where log Kr is the largest integer such that Kr min{4log−1r, K}. With r = e−N/V for a suitably large, but ﬁxed, constant V , Proposition 8.2 gives

![image 209](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile209.png>)

E

- 1

![image 210](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile210.png>)

- 2πN


2π

|FN/2(reiθ)|2dθ

0

q

≫

1 V (1 + (1 − q)√log N)

![image 211](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile211.png>)

![image 212](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile212.png>)

q

,

while Proposition 3.2 gives E

2π

rN 2πN

e−V 1 + (1 − q)√log N

q

q

|FN/2(eiθ)|2dθ

.

≪

![image 213](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile213.png>)

![image 214](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile214.png>)

![image 215](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile215.png>)

0

Combining these estimates with Proposition 8.1, and choosing V to be a large enough constant, we obtain the lower bound in Theorem 2.1 in the range 12 q 1.

![image 216](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile216.png>)

9. Proof of Proposition 8.1

As with the upper bound in Section 4, we begin by decomposing the deﬁnition of A(N) in terms of a(λ) for partitions λ (see (2.1) and (2.2)), grouping terms according to the size of the largest part λ1. Deﬁne

A1(N) =

a(λ) =

|λ|=N N/2<λ1 N

N/2<n N

X(n) √n

A(N − n) and A1(N) =

a(λ),

![image 217](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile217.png>)

![image 218](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile218.png>)

|λ|=N λ1 N/2

so that A(N) = A1(N) + A1(N). Using that X(n) is distributed identically to −X(n) for N/2 < n N, we see that

- (9.1) E[|A(N)|2q] =

1 2

![image 219](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile219.png>)

E |A1(N) + A1(N)|2q + | − A1(N) + A1(N)|2q

1 2

![image 220](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile220.png>)

E[|A1(N)|2q],

where the last inequality holds because max(| − z + w|, |z + w|) |z| for any two complex numbers z and w.

To obtain a lower bound on E[|A1(N)|2q], we ﬁrst condition on the variables X(k) for all k N/2. Note that A(N − n) is then determined for all N/2 < n N. Therefore

A1(N) =

N/2<n N

X(n) √n

![image 221](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile221.png>)

![image 222](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile222.png>)

A(N − n),

being a linear combination of the independent standard complex Gaussians X(n), is distributed like a complex Gaussian with mean 0 and variance N/2<n N |A(N −n)|2/n. With E1 denoting the conditional expectation (ﬁxing X(k) for k N/2), it follows that

E1 |A1(N)|2q = Cq

N/2<n N

|A(N − n)|2 n

![image 223](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile223.png>)

q

,

where Cq = E[|Z|2q] is the 2q-th moment of a standard complex Gaussian Z with mean 0 and variance 1. H¨older’s inequality gives

E[|Z|2q]

(E[|Z|2])2−q (E[|Z|4])1−q

![image 224](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile224.png>)

=

1 21−q

![image 225](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile225.png>)

, and so we obtain

E1 |A1(N)|2q

1 21−q

![image 226](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile226.png>)

N/2<n N

|A(N − n)|2 n

![image 227](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile227.png>)

q 1 2

![image 228](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile228.png>)

1 N

![image 229](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile229.png>)

n<N/2

|A(n)|2

q

.

Now taking the full expectation and using (9.1), we deduce that

- (9.2) E |A(N)|2q


1 4

E

![image 230](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile230.png>)

1 N

|A(n)|2

![image 231](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile231.png>)

n<N/2

q

.

Write

FN/2(z) = exp

∞

X(k) √k

A1(n)zn,

zk =

![image 232](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile232.png>)

![image 233](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile233.png>)

n=0

k N/2

and note that A1(n) = A(n) for n N/2. Note that Parseval’s identity gives, for any 0 < r 1,

∞

∞

| A1(n)|2

|A(n)|2 =

| A1(n)|2

| A1(n)|2r2n − rN

n=0

n=0

n<N/2

n<N/2

2π

2π

rN 2π

1 2π

|FN/2(eiθ)|2dθ. Since |z + w|q |z|q + |w|q for q 1, it follows that

|FN/2(reiθ)|2dθ −

=

![image 234](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile234.png>)

![image 235](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile235.png>)

0

0

2π

2π

rN 2π

q 1 2π

q

|A(n)|2

|FN/2(reiθ)|2dθ

|FN/2(eiθ)|2dθ

−

![image 236](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile236.png>)

![image 237](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile237.png>)

0

0

n<N/2

q

,

and inserting this in (9.2), we obtain Proposition 8.1.

10. Plan for the proof of Proposition 8.2

The proof of the lower bound in Theorem 2.1 has now been reduced to establishing Proposition 8.2. Let L = L(X) denote any (random) subset of θ ∈ [0, 2π) with the random subset depending possibly on the instantiation of the random variables X. Using H¨older’s inequality, we obtain

2π

1 2π L(X) |F(reiθ)|2dθ

- 1

![image 238](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile238.png>)

- 2π


q

q

|F(reiθ)|2dθ

E

E

![image 239](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile239.png>)

0

- 1

![image 240](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile240.png>)

- 2π L(X) |F(reiθ)|2dθ


2−q

E

- (10.1) 2 1−q.


![image 241](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile241.png>)

- 1

![image 242](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile242.png>)

- 2π L(X) |F(reiθ)|2dθ


E

We apply this idea to a carefully chosen random subset L(X) where the second and fourth moments will be of comparable size so that there is no loss involved in applying H¨older’s inequality in (10.1). The random set L(X) is deﬁned similarly to Deﬁnition 5.1, keeping once again the ballot problem in mind.

Deﬁnition 10.1. Let K 10. Suppose e−1/40 r < 1 and deﬁne log Kr to be the largest integer such that Kr min 4 log −1r, K . Let A be a real number with 1 A √log Kr. Deﬁne L(θ) = Lr(A, θ; K) to be the following event: For each 1 n log Kr one has

![image 243](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile243.png>)

![image 244](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile244.png>)

X(k)rkeikθ √k −

r2k k

Re

A − 5 log n.

![image 245](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile245.png>)

![image 246](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile246.png>)

![image 247](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile247.png>)

k<en

Deﬁne L = Lr(A; K) to be the random subset of θ ∈ [0, 2π] such that L(θ) holds.

With this choice of the random subset L, we seek a lower bound for the numerator in

- (10.1) and an upper bound for the denominator there. We start with the easier case of the lower bound. Since L denotes the subset of θ for which L(θ) holds, we ﬁnd that

E

- 1

![image 248](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile248.png>)

- 2π L |F(reiθ)|2dθ = E


- 1

![image 249](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile249.png>)

- 2π


2π

0

1L(θ)|F(reiθ)|2dθ =

1 2π

![image 250](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile250.png>)

2π

0

E 1L(θ)|F(reiθ)|2 dθ, and by the rotational symmetry of the random variables X, this equals

E 1L(0)|F(r)|2 . Arguing as in Section 7 we may see that

E 1L(0)|F(r)|2 = exp

k K

r2k k

![image 251](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile251.png>)

P[B],

where B is the event that, for all 1 n log Kr, one has

k<en

ykrk √k

![image 252](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile252.png>)

![image 253](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile253.png>)

A − 5 log n,

for independent normal random variables yk with mean 0 and variance 12. We now invoke Lemma 2.3 with the random variables Gm = em−1 k<em ykrk/√k for 1 m log Kr. Note that these variables Gm are Gaussian with variance 21 em−1 k<em r2k/k which lies between 1/20 and 20 as required in Lemma 2.3. Therefore it follows that P(B) ≍ A/√log Kr, and we conclude that

![image 254](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile254.png>)

![image 255](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile255.png>)

![image 256](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile256.png>)

![image 257](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile257.png>)

- (10.2) E


r2k k ≫

A √log Kr

AKr √log Kr

- 1

![image 258](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile258.png>)

- 2π L |F(reiθ)|2dθ ≫


exp

.

![image 259](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile259.png>)

![image 260](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile260.png>)

![image 261](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile261.png>)

![image 262](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile262.png>)

![image 263](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile263.png>)

k K

Now we turn to the harder problem of obtaining satisfactory upper bounds for the denominator in (10.1). Expanding out we see that

E

- 1

![image 264](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile264.png>)

- 2π L |F(reiθ)|2dθ


2

1 (2π)2

=

E

![image 265](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile265.png>)

2π

0

2π

1)|F(reiθ

)|21L(θ

2)|F(reiθ

)|2dθ1dθ2 ,

1L(θ

1

2

0

and upon writing θ = θ2 −θ1 (and taking θ to be in [−π, π)) and using rotational symmetry this equals

π

1 2π

E 1L(0)|F(r)|21L(θ)|F(reiθ)|2 dθ. Proposition 10.2. With notations as above, and any θ ∈ [−π, π) we have E 1L(0)|F(r)|21L(θ)|F(reiθ)|2 ≪ A2e2A

![image 266](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile266.png>)

−π

Kr2 log Kr

min(Kr, 2π/|θ|) (log min(Kr, 2π/|θ|))8

.

![image 267](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile267.png>)

![image 268](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile268.png>)

We postpone the proof of Proposition 10.2 to the next section, and assuming this bound now ﬁnish our proof of Proposition 8.2. Applying Proposition 10.2 we obtain

E

- 1

![image 269](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile269.png>)

- 2π L |F(reiθ)|2dθ


2

Kr2 log Kr

≪ A2e2A

![image 270](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile270.png>)

π

Kr2 log Kr

min(Kr, 2π/|θ|) (log min(Kr, 2π/|θ|))8

dθ ≪ A2e2A

.

![image 271](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile271.png>)

![image 272](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile272.png>)

−π

Using this upper bound for the denominator in (10.1) together with the lower bound for the numerator (given in (10.2)) we conclude that

2π

AKr √log Kr

- 1

![image 273](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile273.png>)

- 2π


q

q

|F(reiθ)|2dθ

≫ e−2A(1−q)

.

E

![image 274](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile274.png>)

![image 275](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile275.png>)

0

Selecting A = √log Kr/((1 − q)√log Kr + 1) completes the proof of Proposition 8.2.

![image 276](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile276.png>)

![image 277](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile277.png>)

11. Proof of Proposition 10.2 Given θ ∈ [−π, π), deﬁne M = M(r, θ) to be the smallest integer such that

- (11.1) eM min{103/|θ|, Kr/e}. Note that log Kr 2 in Deﬁnition 10.1, and so M 1. Set


- (11.2) A0(M) = Re

k<eM

X(k)rk √k −

![image 278](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile278.png>)

![image 279](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile279.png>)

r2k k

![image 280](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile280.png>)

, Aθ(M) = Re

k<eM

X(k)rkeikθ √k −

![image 281](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile281.png>)

![image 282](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile282.png>)

r2k k

![image 283](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile283.png>)

,

and deﬁne for M + 1 m log Kr,

- (11.3) Z0(m) = Re

em−1 k<em

X(k) √k

![image 284](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile284.png>)

![image 285](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile285.png>)

rk, Zθ(m) = Re

em−1 k<em

X(k) √k

![image 286](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile286.png>)

![image 287](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile287.png>)

rkeikθ.

Our goal is to bound the expected value of |F(r)|2|F(reiθ)|2 when restricted to the event L(0) ∩ L(θ). Recall that L(0) ∩ L(θ) is the event satisfying the inequalities (for 1 n log Kr)

k<en

Re

X(k) √k

![image 288](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile288.png>)

![image 289](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile289.png>)

rk −

r2k k

![image 290](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile290.png>)

A − 5 log n,

k<en

Re

X(k) √k

![image 291](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile291.png>)

![image 292](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile292.png>)

rkeikθ −

r2k k

![image 293](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile293.png>)

A − 5 log n.

Since our goal is to obtain upper bounds, we replace the event L(0) ∩ L(θ) with a less restrictive event which is easier to handle. This less restrictive event L is deﬁned by the constraints

- (11.4) A0(M), Aθ(M) A − 5 logM, together with, for M + 1 m log Kr
- (11.5)


r2k k

r2k k

X(k) √k

X(k) √k

rk−

rkeikθ−

Re

,

Re

![image 294](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile294.png>)

![image 295](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile295.png>)

![image 296](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile296.png>)

![image 297](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile297.png>)

![image 298](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile298.png>)

![image 299](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile299.png>)

eM k<em

eM k<em

A−min(A0(M), Aθ(M), 0).

Before entering into the details, let us give a loose description of the argument. The values k below eM are thought of as small, and here eikθ may be thought of as close to 1. The constraints imposed by L(0) and L(θ) are strongly correlated for such k, and so are the quantities A0(M) and Aθ(M). The “barrier events” in (11.4) prevent the contribution of these small k from getting too large. In the range eM k Kr, the oscillation of eikθ becomes signiﬁcant, and the terms Z0(m) and Zθ(m) behave almost independently of each other. This allows us to think of the constraints in (11.5) as corresponding to two independent applications of the ballot problem, leading eventually to the saving of log Kr in

- Proposition 10.2. Lastly the terms with K k > Kr contribute a negligible amount as they are weighted down by the factor rk which is small in this range.


Returning to the proof, in the notation just introduced, we have E 1L(0)∩L(θ)|F(r)F(reiθ)|2 exp 4

r2k k

E 1 L exp(2A0(M) + 2Aθ(M))

![image 300](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile300.png>)

k<eM

rk √k

Re (X(k) + X(k)eikθ) .

exp(2Z0(m) + 2Zθ(m)) exp 2

![image 301](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile301.png>)

![image 302](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile302.png>)

M+1 m log Kr

Kr k K

We make a few initial simpliﬁcations to this quantity, before getting to the crux of the proof. Note that the terms involving X(k) with Kr k K are independent of the random variables with k < Kr, and are not constrained by (11.4) or (11.5). So we may separate these terms from our expression above, and they contribute

rk √k

rk √k

r2k k

- 1

![image 303](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile303.png>)

- 2


Re(X(k)eikθ)

+exp 4

= exp 4

,

E exp 4

ReX(k)

![image 304](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile304.png>)

![image 305](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile305.png>)

![image 306](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile306.png>)

![image 307](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile307.png>)

![image 308](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile308.png>)

Kr k K

Kr k K

Kr k K

r k K Re(X(k))rk√k and K

r k K Re (X(k)eikθ)rk/√k are distributed like Gaussian random variables with mean 0 and variance 12 K

![image 309](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile309.png>)

![image 310](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile310.png>)

since K

r k K r2k/k (compare with Lemma 2.2). Noting that

![image 311](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile311.png>)

r2k k

r2k k

1 k

= M + O(1), and

= O(1),

![image 312](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile312.png>)

![image 313](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile313.png>)

![image 314](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile314.png>)

Kr k K

k<eM

k<eM

we conclude that E 1L(0)∩L(θ)|F(r)F(reiθ)|2 ≪ e4ME 1 L exp(2A0(M) + 2Aθ(M))

- (11.6) exp(2Z0(m) + 2Zθ(m)) .

We now state a proposition (to be proved in the next section) which amounts to two applications of the ballot problem, and granting this proposition, we will be able to ﬁnish the proof of Proposition 10.2.

- Proposition 11.1. Keep notations as above. Given a real number B, let E denote the following event: for all M + 1 m log Kr one has


- (11.7)


M+1 m log Kr

r2k k

r2k k

X(k) √k

X(k) √k

rk −

rkeikθ −

Re

,

B.

Re

![image 315](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile315.png>)

![image 316](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile316.png>)

![image 317](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile317.png>)

![image 318](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile318.png>)

![image 319](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile319.png>)

![image 320](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile320.png>)

eM k<em

eM k<em

Then

Kr2 e2M

exp(2Z0(m) + 2Zθ(m)) ≪

E 1E

![image 321](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile321.png>)

M+1 m log Kr

1 + max(0, B) 1 + log(Kr/eM)

![image 322](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile322.png>)

![image 323](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile323.png>)

2

.

Assuming this proposition, we now resume the proof of Proposition 10.2, starting from

- (11.6). Applying Proposition 11.1 with B = A − min(A0(M), Aθ(M), 0) we obtain E 1L(0)∩L(θ)|F(r)F(reiθ)|2


Kr2e2M 1 + log(Kr/eM)

E 1 L exp(2A0(M) + 2Aθ(M)) A + max(−A0(M), −Aθ(M), 0) 2 .

≪

![image 324](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile324.png>)

Here we have abused notation a little, and the event L refers now only to the constraint (11.4) on the variables X(k) with k < eM. Notice also that we have used Proposition 11.1 treating

X(k) for k < eM as ﬁxed. By rotational symmetry, we may assume that A0(M) Aθ(M); the other case contributes an identical amount. Then bounding Aθ(M) by A − 5 log M, we conclude that

E 1L(0)∩L(θ)|F(r)F(reiθ)|2 ≪

Kr2e2M 1 + log(Kr/eM)

e2A M10

- (11.8) 0(M) A−5 logM exp(2A0(M)) A + max(−A0(M), 0) 2 .


E 1A

![image 325](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile325.png>)

![image 326](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile326.png>)

Now Re k<eM X(k)rk/√k is a real Gaussian with mean 0 and variance 12 k<eM r2k/k. Therefore, using also that k<eM r2k/k = M + O(1),

![image 327](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile327.png>)

![image 328](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile328.png>)

0(M) A−5 logM exp(2A0(M)) A + max(−A0(M), 0) 2

E 1A

A−5 log M

(x + k<eM r2k/k)2 k<eM r2k/k

1 π k<eM r2k/k

e2x(A + max(−x, 0))2 exp −

=

dx ≪ (A2 + M)e−M.

![image 329](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile329.png>)

![image 330](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile330.png>)

![image 331](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile331.png>)

−∞

Inserting this in (11.8), we conclude that

Kr2eM 1 + log(Kr/eM)

E 1L(0)∩L(θ)|F(r)F(reiθ)|2 ≪

![image 332](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile332.png>)

e2A M10

Kr2eM 1 + log(Kr/eM)

A2e2A M9

(A2 + M) ≪

.

![image 333](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile333.png>)

![image 334](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile334.png>)

![image 335](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile335.png>)

Upon recalling the deﬁnition of M in (11.1), and noting that M(1 + log(Kr/eM)) log Kr, this completes the proof of Proposition 10.2.

12. Proof of Proposition 11.1

The proof of the lower bound for Theorem 2.1 has been reduced to Proposition 11.1. Here we are focussing on the range eM K Kr where there is substantial oscillation in the terms eikθ, and we shall see that the variables Z0(m) and Zθ(m) for M + 1 m log Kr are largely uncorrelated (or more precisely, very weakly correlated). By exploiting properties of bivariate Gaussian vectors, these weakly correlated Gaussians may be replaced with independent Gaussians. Thus, the expectation in Proposition 11.1 will essentially split into two independent Gaussian random walks where an analysis similar to Section 7 will ultimately carry over.

We ﬁrst dispense with the case when log(Kr/eM) 10. Note that E 1E

exp(2Z0(m) + 2Zθ(m))

M+1 m log Kr

- 1

![image 336](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile336.png>)

- 2


exp(4Zθ(m))

exp(4Z0(m)) + E

E

M+1 m log Kr

M+1 m log Kr

X(k)rk √k

exp(4Z0(m)) = E exp 4Re

= E

,

![image 337](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile337.png>)

![image 338](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile338.png>)

M+1 m log Kr

eM k<Kr

by rotational symmetry. Now eM k<Kr Re (X(k)rk/√k) is distributed like a Gaussian random variable with mean 0 and variance 21 eM k<Kr r2k/k, and this variance is bounded by our assumption that log(Kr/eM) 10. It follows that in this case, our desired quantity is bounded by an absolute constant, and the proposition follows at once.

![image 339](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile339.png>)

![image 340](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile340.png>)

Therefore we may assume that Kr > eM+10 below. Upon recalling the deﬁnition of M (see

- (11.1)) we may thus assume that θ ∈ (−π, π] satisﬁes 103/|θ| > Kr/e and that eM|θ| 103.

With this easy case out of the way, we now embark on the proof proper.

For M+1 m log Kr note that the variables Z0(m) and Zθ(m) depend only on X(k) for em−1 k < em, and so these variables Z0(m) and Zθ(m) are independent for diﬀerent values of m. We therefore begin by discussing, for a given M + 1 m log Kr, the probability that Z0(m) and Zθ(m) satisfy some event, and then by combining those results for diﬀerent m we will obtain Proposition 11.1.

We recall that a pair of real random variables (Y1, Y2) is said to have a bivariate normal distribution if every linear combination a1Y1 + a2Y2 with a1, a2 ∈ R is a univariate normal random variable. The bivariate normal distribution is determined by the means µ1 = E[Y1] and µ2 = E[Y2] together with the 2×2 (symmetric) covariance matrix E[YiYj] for 1 i, j 2. Denote by σi2 = E[Yi2] for i = 1, 2, and by ρσ1σ2 the covariance E[Y1Y2] so that |ρ| 1. For a bivariate normal vector (Y1, Y2) with these parameters, the probability density at (x1, x2) ∈ R2 is given by

- (12.1)


1 2πσ1σ2 1 − ρ2

x1 − µ1 σ1

x2 − µ2 σ2

x2 − µ2 σ2

x1 − µ1 σ1

1 2(1 − ρ2)

2

2

+

−2ρ

exp −

.

![image 341](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile341.png>)

![image 342](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile342.png>)

![image 343](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile343.png>)

![image 344](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile344.png>)

![image 345](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile345.png>)

![image 346](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile346.png>)

![image 347](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile347.png>)

Here we ignore the degenerate case when |ρ| = 1.

If (Y1, Y2) is a bivariate normal vector, then in general Y1 and Y2 need not be independent, and indeed the case when they are independent corresponds to requiring the covariance E[Y1Y2] to be 0 (equivalently ρ = 0 above). We next observe that even in the general case, we can upper bound the probability density in (12.1) by replacing (Y1, Y2) by a suitable pair of independent normal variables. This is especially useful when the covariance parameter ρ is small, which will be the case for us.

Suppose (Y1, Y2) is a bivariate normal vector, with probability density as in (2.1). Since 2ρ

x2 − µ2 σ2 |ρ|

x1 − µ1 σ1

x2 − µ2 σ2

x1 − µ1 σ1

2

2

, we see that the probability density in (12.1) is bounded above by

+

![image 348](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile348.png>)

![image 349](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile349.png>)

![image 350](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile350.png>)

![image 351](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile351.png>)

![image 352](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile352.png>)

1 + |ρ| 1 − |ρ|

1 2πσ1σ2(1 + |ρ|)

x1 − µ1 σ1

1 2(1 + |ρ|)

x2 − µ2 σ2

2

2

- (12.2)


.

exp −

+

![image 353](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile353.png>)

![image 354](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile354.png>)

![image 355](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile355.png>)

![image 356](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile356.png>)

![image 357](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile357.png>)

![image 358](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile358.png>)

![image 359](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile359.png>)

Apart from the factor (1 + |ρ|)/(1 − |ρ|), the quantity above is the probability density of a pair of independent normal variables ( Y1, Y2) with means µ1, µ2, and variances σ12(1+|ρ|), σ22(1+|ρ|). Thus given any event B (thought of as a Borel measurable subset of R2) we have

![image 360](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile360.png>)

1 + |ρ| 1 − |ρ|

P[( Y1, Y2) ∈ B].

- (12.3) P[(Y1, Y2) ∈ B]


![image 361](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile361.png>)

![image 362](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile362.png>)

With this preliminary discussion in place, we are now ready to handle Proposition 11.1. Since Re(X(k)) and Im(X(k)) are independent normal variables, it follows that

(Re(X(k), Re(X(k)eikθ)) = (Re(X(k)), cos(kθ)Re(X(k)) − sin(kθ)Im(X(k))) is a bivariate normal vector. Being a linear combination of independent such vectors we see that (Z0(m), Zθ(m)) is also a bivariate normal vector. Note that both Z0(m) and Zθ(m)

have mean 0, variance

- (12.4) E[|Z0(m)|2] = E[|Zθ(m)|2] = σm2 =

em−1 k<em

r2k 2k

![image 363](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile363.png>)

and covariance

- (12.5) E[Z0(m)Zθ(m)] = ρm(θ)σm2 =

em−1 k<em

r2k 2k

![image 364](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile364.png>)

cos(kθ).

In the range M + 1 m log Kr,

- (12.6)

1 4

![image 365](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile365.png>)

em−1 k em

1 4k

![image 366](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile366.png>)

σm2

em−1 k<em

1 2k

![image 367](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile367.png>)

1 2

![image 368](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile368.png>)

+

- 1

![image 369](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile369.png>)

- 2em−1


.

because 12 r2k 1 for k Kr. Further the covariance satisﬁes

![image 370](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile370.png>)

- (12.7) |ρm(θ)σm2 | =

em−1 k<em

r2k

cos(kθ) 2k

![image 371](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile371.png>)

=

r

0 em−1 k<em

t2k−1eikθdt

π |θ|em−1

![image 372](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile372.png>)

,

since by summing the geometric series, and using |1 − teiθ| | sin(θ/2)| |θ|/π (for all 0 t 1 and θ ∈ (−π, π]), we may see that

em−1 k<em

t2k−1eikθ

2t2⌈em−1⌉−1 |1 − teiθ|

![image 373](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile373.png>)

π |θ|

![image 374](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile374.png>)

2t2⌈e

m−1⌉−1.

Thus in this range |ρm| 4π/(|θ|em−1) is small, being always 4π/103 < 1/10. Now deﬁne independent normal random variables Z0(m) and Zθ(m) distributed identically

with mean 0 and variance σm2 (1 + |ρm(θ)|). As noted in (12.2) and (12.3) we obtain that for any event B (thought of as a Borel measurable subset of R2) we have

E 1B exp(2(Z0(m) + Zθ(m))

![image 375](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile375.png>)

1 + |ρm(θ)| 1 − |ρm(θ)|

![image 376](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile376.png>)

![image 377](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile377.png>)

E 1B exp(2( Z0(m) + Zθ(m)) .

Applying this to all M + 1 m log Kr (and recalling that Z0(m) and Zθ(m) are independent for diﬀerent values of m) we conclude that

E 1E

M+1 m log Kr

exp(2(Z0(m) + Zθ(m))

M+1 m log Kr

![image 378](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile378.png>)

1 + |ρm(θ)| 1 − |ρm(θ)|

![image 379](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile379.png>)

![image 380](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile380.png>)

× E 1E

M+1 m log Kr

exp(2( Z0(m) + Zθ(m))

≪ E 1E

M+1 m log Kr

- (12.8) exp(2( Z0(m) + Zθ(m)) .

Here we estimated M+1 m logK

r

![image 381](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile381.png>)

(1 + |ρm(θ)|/ (1 − |ρm(θ)|) as ≪ 1 using (12.6), (12.7), and our assumption that eM|θ| 103. Let us also clarify that the event E denotes (on the left side of (12.8)) the inequalities given in (11.7), and on the right side of (12.8) these inequalities amount to, for all M + 1 m log Kr

![image 382](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile382.png>)

- (12.9)


r2k k

2σℓ2.

Z0(ℓ),

Zθ(ℓ) B +

= B +

![image 383](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile383.png>)

M+1 ℓ m

M+1 ℓ m

M ℓ m

eM k<em

Since Z0(m) and Zθ(m) are independent, the right side of (12.8) equals E 1E

2

exp(2 Z0(m))

,

M+1 m log Kr

where now by E we understand the constraints in (12.9) holding just for Z0(m). If we put Ym = Z0(m) − 2σm2 (1 + |ρm(θ)|) then (completing the square as in Section 7) we obtain

2σm2 (1 + |ρm(θ)|)

exp(2 Z0(m)) = exp

E 1E

M+1 m log Kr

M+1 m log Kr

Ym2 2σm2 (1 + |ρm(θ)|) M+1 m logK

dYm 2πσm2 (1 + |ρm(θ)|)

× · · ·

exp −

,

![image 384](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile384.png>)

![image 385](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile385.png>)

![image 386](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile386.png>)

M+1 m log Kr

r

E′

where E′ now denotes the constraint

2σℓ2|ρℓ(θ)|. We conclude that

2σℓ2 − 2σℓ2(1 + |ρℓ(θ)|) = B −

Ym B +

M+1 ℓ m

M+1 ℓ m

M+1 ℓ m

exp(2 Z0(m)) exp

E 1E

M+1 m log Kr

2σm2 (1 + |ρm(θ)|)

M+1 m log Kr

× P

Ym B for all M + 1 m log Kr

M+1 ℓ m

1 + max(0, B) 1 + log(Kr/eM)

2σm2 (1 + |ρm(θ)|)

≪ exp

,

![image 387](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile387.png>)

![image 388](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile388.png>)

M+1 m log Kr

upon appealing to Lemma 2.3. Finally recalling (12.4) and (12.7) we have

r2k k

2σm2 (1 + |ρm(θ)|) =

![image 389](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile389.png>)

M+1 m log Kr

eM k<Kr

+ O(1) = log Kr − M + O(1).

This establishes Proposition 11.1, and hence the lower bound in Theorem 2.1. References

- [1] Louis-Pierre Arguin, David Belius, Paul Bourgade, Maksym Radziwil l , and Kannan Soundararajan. Maximum of the Riemann zeta function on a short interval of the critical line. Comm. Pure Appl. Math., 72(3):500–535, 2019.
- [2] Louis-Pierre Arguin, David Belius, and Adam J. Harper. Maxima of a randomized Riemann zeta function, and branching random walks. Ann. Appl. Probab., 27(1):178–215, 2017.
- [3] Louis-Pierre Arguin, Paul Bourgade, and Maksym Radziwil l . The Fyodorov-Hiary-Keating conjecture.

I. arXiv preprint arXiv:2007.00988, 2020.

- [4] Louis-Pierre Arguin, Fr´ed´eric Ouimet, and Maksym Radziwil l . Moments of the Riemann zeta function on short intervals of the critical line. arXiv preprint arXiv:1901.04061, 2019.
- [5] Emma C. Bailey and Jonathan P. Keating. Maxima of log-correlated ﬁelds: some recent developments. arXiv preprint arXiv:2106.15141, 2021.
- [6] Nathana¨el Berestycki. An elementary approach to Gaussian multiplicative chaos. Electron. Commun. Probab., 22:Paper No. 27, 12, 2017.
- [7] J¨org Br¨udern, Kaisa Matoma¨ki, Robert Vaughan, and Trevor Wooley. Analytic number theory. Oberwolfach Reports, 16(4):3141–3205, Nov 2020.
- [8] Sourav Chatterjee and Kannan Soundararajan. Random multiplicative functions in short intervals. Int. Math. Res. Not. IMRN, (3):479–492, 2012.


- [9] Reda Chhaibi and Joseph Najnudel. On the circle GMCγ = lim

←−

CβEn for γ = β2, (γ 1). arXiv preprint arXiv:1904.00578, 2019.

![image 390](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile390.png>)

![image 391](<2021-soundararajan-model-problem-multiplicative-chaos_images/imageFile391.png>)

- [10] Bertrand Duplantier, R´emi Rhodes, Scott Sheﬃeld, and Vincent Vargas. Renormalization of critical Gaussian multiplicative chaos and KPZ relation. Comm. Math. Phys., 330(1):283–330, 2014.
- [11] Sean Eberhard, Kevin Ford, and Ben Green. Permutations ﬁxing a k-set. Int. Math. Res. Not. IMRN,

(21):6713–6731, 2016.

- [12] Kevin Ford. The distribution of integers with a divisor in a given interval. Ann. of Math. (2), 168(2):367– 433, 2008.
- [13] Yan V. Fyodorov, Ghaith A. Hiary, and Jonathan P. Keating. Freezing transition, characteristic polynomials of random matrices, and the Riemann zeta function. Physical review letters, 108(17):170601, 2012.
- [14] Yan V. Fyodorov and Jonathan P. Keating. Freezing transitions and extreme values: random matrix theory, and disordered landscapes. Philosophical Transactions of the Royal Society A: Mathematical, Physical and Engineering Sciences, 372(2007):20120503, 2014.
- [15] Maxim Gerspach. Low Pseudomoments of the Riemann Zeta Function and Its Powers. International Mathematics Research Notices, 07 2020. rnaa159.
- [16] Andrew Granville, Adam J. Harper, and Kannan Soundararajan. Mean values of multiplicative functions over function ﬁelds. Res. Number Theory, 1:Art. 25, 18, 2015.
- [17] G´bor Hala´sz. On random multiplicative functions. In Hubert Delange colloquium (Orsay, 1982), volume 83 of Publ. Math. Orsay, pages 74–96. Univ. Paris XI, Orsay, 1983.
- [18] Adam J. Harper. Bounds on the suprema of Gaussian processes, and omega results for the sum of a random multiplicative function. Ann. Appl. Probab., 23(2):584–616, 2013.
- [19] Adam J. Harper. On the limit distributions of some sums of a random multiplicative function. J. Reine Angew. Math., 678:95–124, 2013.
- [20] Adam J. Harper. Moments of random multiplicative functions, II: High moments. Algebra Number Theory, 13(10):2277–2321, 2019.
- [21] Adam J. Harper. On the partition function of the Riemann zeta function, and the Fyodorov–Hiary– Keating conjecture. arXiv preprint arXiv:1906.05783, 2019.
- [22] Adam J. Harper. Almost sure large ﬂuctuations of random multiplicative functions. arXiv preprint arXiv:2012.15809, 2020.
- [23] Adam J. Harper. Moments of random multiplicative functions, I: Low moments, better than squareroot cancellation, and critical multiplicative chaos. Forum Math. Pi, 8:e1, 95, 2020.
- [24] Adam J. Harper, Ashkan Nikeghbali, and Maksym Radziwil l . A note on Helson’s conjecture on moments of random multiplicative functions. In Analytic number theory, pages 145–169. Springer, Cham, 2015.
- [25] Henry Helson. Hankel forms. Studia Math., 198(1):79–84, 2010.
- [26] Bob Hough. Summation of a random multiplicative function on numbers having few prime factors. Math. Proc. Cambridge Philos. Soc., 150(2):193–214, 2011.
- [27] Christopher P. Hughes, Jonathan P. Keating, and Neil O’Connell. On the characteristic polynomial of a random unitary matrix. Comm. Math. Phys., 220(2):429–451, 2001.
- [28] Yuk-Kam Lau, G´erald Tenenbaum, and Jie Wu. On mean values of random multiplicative functions. Proc. Amer. Math. Soc., 141(2):409–420, 2013.
- [29] Joseph Najnudel. On the extreme values of the Riemann zeta function on random intervals of the critical line. Probab. Theory Related Fields, 172(1-2):387–452, 2018.
- [30] Joseph Najnudel, Elliot Paquette, and Nick Simm. Secular coeﬃcients and the holomorphic multiplicative chaos. arXiv preprint arXiv:2011.01823, 2020.
- [31] R´emi Rhodes and Vincent Vargas. Gaussian multiplicative chaos and applications: a review. Probab. Surv., 11:315–392, 2014.


Department of Mathematics, Stanford University, 450 Serra Mall, Building 380, Stan-

ford, CA, USA, 94305 Email address: ksound@stanford.edu Department of Mathematics, University of Toronto, 40 St. George Street, Room 6290,

Toronto, ON, CANADA, M5S 2E4 Email address: zaman@math.toronto.edu

