---
type: source
kind: paper
title: Additive decomposition of signed prime
authors: Imre Z. Ruzsa
year: 2022
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2204.14013v1
source_local: ../raw/2022-ruzsa-additive-decomposition-signed-prime.pdf
topic: general-knowledge
cites:
---

arXiv:2204.14013v1[math.NT]29Apr2022

ADDITIVE DECOMPOSITION OF SIGNED PRIMES

IMRE Z. RUZSA

Abstract. Under the prime-tuple hypothesis, the set of signed primes is a sumset.

In memoriam Andreae Schinzel, excellentis mathematici et optimi viri.

1. Introduction

Ostmann’s “inverse Goldbach” problem (this term is probably Wirsing’s) asks whether the set P of (positive) primes is asymptotically a sumset, that is, whether there are sets A, B (having more than 1 elements each) such that P△(A+B) is ﬁnite, with △ meaning symmetric diﬀerence.

Still unsolved, generally a negative answer is expected. See Elsholz[1, 2] for the best partial results.

The aim of this paper is to show that the situation changes if we admit negative primes.

- Theorem 1. Assuming the prime-tuple hypothesis there are inﬁnte sets A, B ⊂ Z such that A + B is exactly the collection of (positive and negative) primes satisfying |p| > 3; moreover, every prime p has exactly one representation as p = a + b, a ∈ A, b ∈ B.

It is easily seen that ±2, ±3 must be omitted, and that if the summands have more than 1 elements, they both must be inﬁnite.

Some details of the argument are easier written in terms of diﬀerences, so we reformulate the theorem as follows.

- Theorem 2 (Variant with diﬀerences). Assuming the prime-tuple hypothesis there are inﬁnite sets A, B of positive integers such that A − B is exactly the collection of (positive and negative) primes satisfying |p| > 3; moreover, every prime p has exactly one representaion as p = a − b, a ∈ A, b ∈ B.


2. The prime-tuple hypothesis

The prime-tuple hypothesis, generally assumed to be true but hopeless, expresses that linear forms can simultaneously represent primes unless there is a congruence obstacle. Conjecture (Prime-tuple hypothesis). Let ai, bi be integers, ai = 0. There are inﬁnitely many values of x such that all aix + bi are prime, unless there is a prime p such that for all x we have p|aix + bi for some i.

(Simplest case is the twin prime conjectue.) We shall apply the following special case.

![image 1](<2022-ruzsa-additive-decomposition-signed-prime_images/imageFile1.png>)

2020 Mathematics Subject Classiﬁcation. 11P32, 11N99. Supported by NKFI grants K-129335, K-119528, KKP-133819.

1

Corollary. Given di ∈ Z, q > 1 and t, the condition for the existence of inﬁnitely many x ≡ t (mod q) such that all x + di are primes is that for all primes p:

— if p|q, then p ∤ t + di for any i;

— if p ∤ q, then the di do not contain a complete system of residues modulo p. This is the preceeding applied to the forms qx + t + di.

3. The plan Assume we have ﬁnite sets A, B such that all elements of A−B are primes. We want

to represent a further prime r. How can we do it? Try A′ = A ∪ {x}, B′ = B ∪ {x − r}. This works if all elemens of B − x and A − x + r are prime. We ﬁnd such an x if B ∪ (A + r) is not a complete system modulo any prime. But: the inclusion of x and x−r may spoil this property; we may build a trap to kill

the plan after several steps.

Remedy: we will a priori restrict the possible residues mod p. We clearly cannot do this initially for all primes; we shall dynamically add more and more restricions, that is, new elements compatible with given restrictions and new restrictions compatible with given elements.

4. Prime-compatible sets of residues

Deﬁnition. Let p be a prime and U, V ⊂ Zp nonempty sets of residues. We say that U, V form a prime-compatible pair, if

(U \ V ) − (V \ U) = Z∗p.

The residues of A and B modulo p must have this property. Lemma. Let p be a prime.

(a) Let W ⊂ Zp be a nonempty set of residues. If

p − 1 2

log p log 4/3

- (4.1) |W| <


, then there are prime-compatible sets modulo p satisfying W ⊂ U, W ⊂ V .

−

![image 2](<2022-ruzsa-additive-decomposition-signed-prime_images/imageFile2.png>)

![image 3](<2022-ruzsa-additive-decomposition-signed-prime_images/imageFile3.png>)

(b) For p ≥ 7 there are prime-compatible sets modulo p such that 1, 11 ∈ U \ V , 6 ∈ V \ U and |U ∩ V | = 2.

Part (b) is motivated by the following consideration. By looking at the residues of A and B modulo 5 it is easy to see that the representations of 5 and −5 must have a common element; we set 1, 11 ∈ A and 6 ∈ B.

Proof. (a): Write |W| = n. We assign the p − n elements of Zp \ W randomly to U or V , and estimate the probability that a z ∈ Z∗p is represented as a diﬀerence of these new elements.

Consider the pairs (z, 2z), (3z, 4z), . . . , ((p−2)z, (p−1)z). From these (p−1)/2 pairs at most n contain an element of W, at least (p − 1)/2 − n remain.

- A pair represents z with probability 1/4, so


Pr(none is good ) ≤ (3/4)

p−1

2 −n.

![image 4](<2022-ruzsa-additive-decomposition-signed-prime_images/imageFile4.png>)

If this quantity is < 1/p, there is a choice that works for all z. This yields the condition

1 p

p−1

2 −n <

(3/4)

, which can be rearranged as

![image 5](<2022-ruzsa-additive-decomposition-signed-prime_images/imageFile5.png>)

![image 6](<2022-ruzsa-additive-decomposition-signed-prime_images/imageFile6.png>)

log p log 4/3

p − 1 2

, that is, (4.1).

− n >

![image 7](<2022-ruzsa-additive-decomposition-signed-prime_images/imageFile7.png>)

![image 8](<2022-ruzsa-additive-decomposition-signed-prime_images/imageFile8.png>)

(b): Let U′ = {0, 1, 2, p − 1}, V ′ = {0, 1, 3, 4, . . ., p − 2}. This is a prime-compatible pair modulo p. This property is preserved by linear transformations. Deﬁne α, β by

3α ≡ −10 (mod p), β = α + 11. The linear function αx + β maps 2 to 1, p − 1 to 11 and (p + 1)/2 to 6, so the sets

- U = α · U′ + β, V = α · V ′ + β are suitable. The bound could be improved with little eﬀort, but it is irrelevant for our application.

5. The construction

We prove the theorems. Let r1, r2, . . . be the sequence of signed primes ±p, |p| > 3, ordered by increasing

absolute value (p1 = 5, p2 = −5, etc.) We shall construct sequences of sets An, Bn of nonnegative integers such that

A1 ⊂ A2 ⊂ . . ., B1 ⊂ B2 ⊂ . . ., An − Bn ⊃ {r1, r2, . . ., rn}, |An| ≤ n, |Bn| ≤ n, |An| > |An−1|, |Bn| > |Bn−1| inﬁnitely often, and the numbers a−b, a ∈ An, b ∈ Bn are all distinct primes. Clearly the sets A = An, B = Bn will have the properties asserted in Theorem 2.

Let K be a constant such that

(5.1) 2n <

|rn| − 1 2

![image 9](<2022-ruzsa-additive-decomposition-signed-prime_images/imageFile9.png>)

−

log |rn| log 4/3

![image 10](<2022-ruzsa-additive-decomposition-signed-prime_images/imageFile10.png>)

holds whenever |rn| ≥ K/2. Such a constant exists since |rn| ∼ (nlog n)/2.

We construct the sets recursively. In Step n we will have sets An, Bn and sets Up, Vp ⊂ Zp for all primes p < max(K, |rn+1|) such that

An (mod p) ⊂ Up, Bn (mod p) ⊂ Vp, and Up, Vp form a prime-compatible pair.

The starting point is A2 = {1, 11}, B2 = {6}, U2 = {1}, V2 = {0}, U3 = {1, 2},

- V3 = {0}, U5 = {0, 1, 2}, V5 = {1, 3, 4}, and for 7 ≤ p < K the sets Up, Vp are given in part (b) of the Lemma.


Assume we have An−1, Bn−1 and Up, Vp ⊂ Zp for all primes p < max(K, |rn|). We construct An, Bn and Up, Vp for max(K, |rn|) ≤ p < max(K, |rn+1|). (This is either p = |rn|, or there is no such prime.)

If rn ∈ An−1 − Bn−1, we put An = An−1, Bn = Bn−1. Otherwise we will set An = An−1 ∪ {x}, Bn = Bn−1 ∪ {x − rn}

with some positive integer x. This x should have the following properties:

- (i) all elements of x − Bn−1 and An−1 − x + rn are prime;
- (ii) x (mod p) ∈ Up, x − rn (mod p) ∈ Vp for all primes p < max(K, |rn|);
- (iii) no coincidence. It is clear that condition (iii) excludes only ﬁnitely many values of x, hence if we ﬁnd


inﬁnitely many that satisfy (i) and (ii), we are done.

First we ﬁx x mod p for p < max(K, |rn|), p = |rn|. (p = |rn| is a possibility for the ﬁrst few primes.)

There are up ∈ Up \ Vp, vp ∈ Vp \ Up, such that

up − vp ≡ rn (mod p). Impose

x ≡ up (mod p), x − rn ≡ vp (mod p).

If p = |rn|, we must have up = vp. Now we use the 2 element of Up ∩ Vp, choosing diﬀerent ones for p and −p.

According to the Corollary to the prime-tuple hypothesis, the conditions for the existence of values of x that satisfy condition (i) above is the following:

— if p < max(K, |rn|), then p ∤ up − b for b ∈ Bn−1 and p ∤ up − (a + rn) = vp − a for a ∈ An−1;

— if p ≥ max(K, |rn|), then Bn−1 ∪ (An−1 + rn) does not contain a complete system of residues modulo p.

To check the ﬁrst, note that for p = |rn| we have b (mod p) ∈ Vp and up ∈/ Vp; similarly a (mod p) ∈ Up and vp ∈/ Up. For p = |rn| this means that An−1 ∪Bn−1 avoids the residue class of Up∩Vp assigned to rn. Indeed, in previous stepts for rj with |rj| = p we asigned elements of Up \ Vp and Vp \ Up to rj, and for |rj| = p (which may be the case for j = n − 1) we used the other element of Up ∩ Vp.

To check the second, observe that |Bn−1 ∪ (An−1 + rn)| < 2n and max(K, |rn|) > 2n by (5.1).

Finally we construct Up, Vp modulo p = |rn| (if necessary). The requirement is that they form a prime-compatible pair and contain the at most 2n residues of An ∪Bn. The existence of such sets follows from part (a) of the Lemma.

This ends the proof of the Theorems.

6. Remarks

We don’t need the full strength of the prime-tuple hypothesis; however, if the primes form a sumset, then some conﬁgurations must appear inﬁnitely many times.

- Problem 3. Can one prove, without resorting to the prime-tuple hypothesis, the existence of inﬁnite sets A, B ⊂ N such that A + B ⊂ P?

Recent advances related to the twin prime conjecture imly that we can ﬁnd inﬁnite A and arbitarily large ﬁnite B.

Granville[3] proved that under the prime-tuple hypothesis the set of primes contains very general sorts of sumsets.

- Problem 4. Can one prove, without resorting to the prime-tuple hypothesis, the existence of inﬁnite sets A, B ⊂ N such that no element of A + B is divisible by any prime of form 4k + 1?


For 4k − 1 we have an easy example.

References

- 1. Ch. Elsholtz, The inverse goldbach problem, Mathematika 48 (2001), 151–158.
- 2. , Additive decomposability of multiplicatively deﬁned sets, Funct. Approx. Comment. Math. 35 (2006), 61–67.

![image 11](<2022-ruzsa-additive-decomposition-signed-prime_images/imageFile11.png>)

- 3. A. Granville, A note on sums of primes, Canad. Math. Bull. 33 (1990), no. 4, 452–454.


Alfr´ed R´enyi Institute of Mathematics, Budapest, Pf. 127, H-1364 Hungary Email address: ruzsa@renyi.hu

