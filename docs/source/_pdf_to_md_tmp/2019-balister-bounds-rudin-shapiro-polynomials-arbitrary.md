arXiv:1909.08777v1[math.CA]19Sep2019

BOUNDS ON RUDIN–SHAPIRO POLYNOMIALS OF ARBITRARY DEGREE

PAUL BALISTER

Abstract. Let P<n(z) be the Rudin–Shapiro polynomial of degree n − 1. We show that |P<n(z)| ≤

√6n − 2−1 for all n ≥ 0 and |z| = 1, conﬁrming a longstanding conjecture. This bound is sharp in the case when n = (2·4k+1)/3 and z = 1. We also show that for n ≥ m ≥ 0, |P<n(z) − P<m(z)| ≤ 10(n − m), which is asymptotically sharp in the sense that for any ε > 0 there exists n > m ≥ 0 and z with |z| = 1 and |P<n(z)−P<m(z)| ≥ (10 − ε)(n − m), contradicting a conjecture of Montgomery.

![image 1](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile1.png>)

![image 2](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile2.png>)

![image 3](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile3.png>)

1. Introduction

The Rudin–Shapiro polynomials Pt and Qt are deﬁned by setting P0(z) = Q0(z) = 1 and, for t ≥ 0, inductively deﬁning

t

Pt+1(z) = Pt(z) + z2

Qt(z), Qt+1(z) = Pt(z) − z2

t

Qt(z).

These polynomials were introduced independently in the 1950s by Shapiro [12, p.39] and Rudin [10] (although the sequence an of their coeﬃcients was also previously studied by Golay [6]), and have been extensively studied over the last few decades, see e.g. [1–5,7,9,11].

From the deﬁnition of Pt we see that the ﬁrst 2t terms of Pt+1 are the same as for Pt, and hence Pt can be thought of as the ﬁrst 2t terms of an inﬁnite power series

∞

anzn,

P∞(z) :=

n=0

where the coeﬃcients an ∈ {−1, 1} can also be deﬁned [2] by the relations

a0 = 1, a2n = an, and a2n+1 = (−1)nan. (1) Alternatively, writing n = i bi2i, bi ∈ {0, 1}, we have that [3]

an = (−1) ibibi+1, i.e., an is determined by the parity of the number of ‘11’s in the binary expansion of n. For n ≥ 0 write

n−1

aizi

P<n(z) :=

i=0

![image 4](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile4.png>)

The author was partially supported by NSF grants DMS 1600742 and DMS 1855745.

for the ﬁrst n terms of P∞(z) so that, for n > 0, P<n(z) is a polynomial of degree n−1, and Pt(z) = P<2t(z). For n ≥ m ≥ 0 write

n−1

aizi

P[m,n)(z) := P<n(z) − P<m(z) =

i=m

for the polynomial with n − m terms consisting of the terms of P∞(z) from zm to zn−1.

Shapiro [12] has shown that for |z| = 1, |P<n(z)| ≤ C√n for all n, where C = 2 + √2 ≈ 3.41, and Saﬀari [11] has sketched a proof that C = (2+√2) 3/5 ≈ 2.64 suﬃces. However, according to [8] it has ‘long been conjectured’ that C = √6 ≈ 2.45 is suﬃcient, and indeed it is known that this is the best possible constant as |P<n(1)| = 2k+1 − 1 = √6n − 2 − 1 when n = (2·4k +1)/3. In [1] it is claimed that Saﬀari proved this conjecture, but it appears that the proof is unpublished. In this paper we give a proof of this conjecture in the following strong form.

![image 5](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile5.png>)

![image 6](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile6.png>)

![image 7](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile7.png>)

![image 8](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile8.png>)

![image 9](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile9.png>)

![image 10](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile10.png>)

√6n − 2 − 1 for all n ≥ 1 and |z| = 1.

![image 11](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile11.png>)

Theorem 1. |P<n(z)| ≤

In [8] Montgomery made the following conjecture about the polynomials P[m,n). Conjecture 2. |P[m,n)(z)| ≤ 3√n − m for all n ≥ m ≥ 0 and |z| = 1.

![image 12](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile12.png>)

The basis for this conjecture was numerical evidence that suggested the worst case was when

5 · 4k + 1 3

8 · 4k + 1 3 and z = 1, in which case |P[m

mk :=

, nk :=

![image 13](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile13.png>)

![image 14](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile14.png>)

k,nk)(1)| = 3 · 2k − 2 = 3√nk − mk − 2.

![image 15](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile15.png>)

Unfortunately this conjecture turns out to be false. The example polynomial is correct, but for large k the largest value of |P[m

k,nk)(z)| no longer occurs at z = 1. Indeed, it is not hard to show that

k,nk)(e3πi/4) 2 nk − mk

P[m

= 5 + √72 ≈ 9.95, and even this is not the worst case when k is very large. Unfortunately the value of z that maximizes |P[m

lim

![image 16](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile16.png>)

![image 17](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile17.png>)

![image 18](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile18.png>)

k→∞

k,nk)(z)| appears to be a highly erratic function of k, and so we are unable to give an explicit sequence zk with |P[m

k,nk)(zk)|2/(nk − mk) → 10. Nevertheless we show (in Section 5) that

k,nk)(z)|2 nk − mk

sup|z|=1 |P[m

= 10. (2)

lim

![image 19](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile19.png>)

k→∞

We also prove that this is asymptotically the worst case. Theorem 3. |P[m,n)(z)| ≤ 10(n − m) for all n ≥ m ≥ 0 and all z with |z| = 1.

![image 20](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile20.png>)

We prove Theorem 1 in Section 3 and Theorem 3 in Section 4. Equation (2) follows from Theorem 7 below, which is a consequence of the proofs of the results of Rodgers [9] on the distribution of Pt(z)/2(t+1)/2. We prove Theorem 7 and equation (2) in Section 5.

2. The L-norm.

We list a few well-known properties of the polynomials Pt and Qt which easily follow by induction, and can be found in, for example, [8]. Proposition 4. We have the following identities.

- (a) |Pt(z)|2 + |Qt(z)|2 = 2t+1 for all |z| = 1. In particular |Pt(z)|, |Qt(z)| ≤ 2(t+1)/2.
- (b) Pt+k+1(z) = Pk(z)Pt(z2k+1) + z2kQk(z)Pt(−z2k+1). In particular Pt+1(z) = Pt(z2) + zPt(−z2).
- (c) Qt(z) = (−1)tz2t−1Pt(−z−1) and Pt(z) = (−1)t+1z2t−1Qt(−z−1).


Part (b) is particularly noteworthy as it shows that P∞(z) is made up of alternate ±Pk and ±Qk blocks, namely anzn2kPk(z) for n even and anzn2kQk(z) for n odd.

For P ∈ C[z, z−1], deﬁne

|P(z)| and1

P ∞ = sup

|z|=1

![image 21](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile21.png>)

|P(z)|2 + |P(−z)|2.

P L = sup

|z|=1

- Lemma 5. . L is a norm on the vector space C[z, z−1].

Proof. The fact that P L ≥ 0 with equality iﬀ P = 0 is clear, so it remains to prove that P + Q L ≤ P L + Q L for any P, Q ∈ C[z, z−1]. Now

|P(z) + Q(z)|2 + |P(−z) + Q(−z)|2 1/2 = (P(z) + Q(z), P(−z) + Q(−z)) 2 ≤ (P(z), P(−z)) 2 + (Q(z), Q(−z)) 2 ≤ P L + Q L,

where (u, v) 2 = |u|2 + |v|2 is the standard ℓ2 norm on C2 (here z is ﬁxed). The result now follows by taking the supremum over |z| = 1.

![image 22](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile22.png>)

The advantage of  · L is that, unlike  · ∞, it scales well on Rudin–Shapiro polynomials, and thus allows us to eﬀectively bound P[m,n) for arbitrarily large m and n.

- Lemma 6. For any n ≥ m ≥ 0, P[2m,2n) 2L = 2 P[m,n) 2L and P<2n 2L = 2 P<n 2L. Proof. By (1) (or Proposition 4(b)) we have


P[2m,2n)(z) = P[m,n)(z2) + zP[m,n)(−z2), and hence

P[2m,2n)(−z) = P[m,n)(z2) − zP[m,n)(−z2). Thus by the paralellogram rule

|P[2m,2n)(z)|2 + |P[2m,2n)(−z)|2 = 2 |P[m,n)(z2)|2 + |P[m,n)(−z2)|2 . 1The subscript L stands for ‘Limit’, see Theorem 7.

![image 23](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile23.png>)

The ﬁrst statement follows on taking supremums over |z| = 1. The second statement then follows by taking m = 0.

As an example, we see that Pt L = P<2t L = 2t/2 P<1 L = 2t/2 1 L = 2t/2 ·

√

![image 24](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile24.png>)

2 = 2(t+1)/2. (3) Clearly ± ztP(±zs) L = P(z) L for any s = 0, so Proposition 4(c) implies that

t−1Pt(−z−1) L = Pt L = 2(t+1)/2. (4) As we clearly have P ∞ ≤ P L ≤

Qt L = ± z2

√2 P ∞, we deduce from Lemma 6 that in general limsup k→∞

![image 25](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile25.png>)

P[2km,2kn) ∞

2k/2 ≤ P[m,n) L, and a natural question is how much do these quantities diﬀer. Indeed, they are equal. Theorem 7.

![image 26](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile26.png>)

P[2km,2kn) ∞ 2k/2

= P[m,n) L.

lim

![image 27](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile27.png>)

k→∞

We defer the proof of this result (which is not needed in the proofs of Theorems 1 or 3) to Section 5.

Finally we note that it is easy to see that there exists a constant C > 0 such that

P[m,n) L ≤ C√n − m (5) for all n ≥ m ≥ 0. Indeed, we may assume n > m and pick a maximal k such that

![image 28](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile28.png>)

- m ≤ 2kr ≤ n for some (necessarily odd) r ∈ N. As n < 2k(r + 1) = 2k+1r+12 we can write

![image 29](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile29.png>)

- n = 2kr + 2t


+ · · · + 2t

with k > t1 > t2 > · · · > tp. Now note that, by Proposition 4(b), P[2kr,n) can be decomposed into blocks of length 2t

p

1

each of which is (up to multiplication by a power of z) either ±Pt

i

i+1)/2 = O(2t

. Thus by (3) and (4) we have P[2kr,n) L ≤ i 2(t

or ±Qt

1/2) = O(√n − m). Similarly writing m = 2kr−2s

i

i

−· · ·−2s

![image 30](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile30.png>)

, k > s1 > s2 > · · · > sq, we see that P[m,2kr) can be decomposed into blocks ±Ps

q

1

i+1)/2 = O(2s

and P[m,2kr) L ≤ i 2(s

or ±Qs

1/2) = O(√n − m). The result then follows as P[m,n) L ≤ P[m,2kr) L + P[2kr,n) L. 3. Proof of Theorem 1 Deﬁne the function f by

i

i

![image 31](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile31.png>)

f(n) = P<n 2L for n ∈ N = {0, 1, 2, . . .}. Lemma 6 implies that f(2n) = 2f(n), and so allows us to consistently extend this deﬁnition to all non-negative dyadic rationals x = 2n

by deﬁning f(x) = 2−kf(2kx). (6)

![image 32](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile32.png>)

k

Now the triangle inequality, the observation that P<n(z) = P<m(z) + P[m,n)(z), and (5), imply that

|f(n)1/2 − f(m)1/2| ≤ C√n − m.

![image 33](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile33.png>)

By (6) this implies

|f(x)1/2 − f(y)1/2| ≤ C√y − x (7)

![image 34](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile34.png>)

for any dyadic rationals y ≥ x ≥ 0, and hence f can be extended by continuity to a continuous function f : [0, ∞) → R which satisﬁes

f(2x) = 2f(x) (8)

- for all x ≥ 0. A more reﬁned version of the continuity statement (7) can be given if y is suﬃciently close

to a simple dyadic rational x. Lemma 8. If 2kx ∈ N then

|f(y)1/2 − f(x)1/2| ≤ f(|y − x|)1/2

- for all y ≥ 0 with |y − x| ≤ 2−k−1.


Proof. It is enough by continuity to prove this for any dyadic rational y, so pick a t ∈ N such that 2k+ty is an integer. Writing n = 2kx and r = 2k+t|y − x|, we have r ≤ 2t−1 and 2k+ty = 2tn ± r. Now

tnP<r(z) and also

P<2tn+r(z) = P<2tn(z) ± z2

tn−1P<r(−z−1).

P<2tn−r(z) = P<2tn(z) ± z2

Indeed, these follow from Proposition 4(b) as P∞(z) can be decomposed into blocks of the form ±z2tmPt(z) when m is even and ±z2tmQt(z) when m is odd. The ﬁrst equality then follows as the ﬁrst r ≤ 2t−1 terms of either Pt or Qt forms a P<r. The second equality follows from Proposition 4(c) which implies the last r terms of Pt or Qt forms a ±z2t−1P<r(−z−1).

The triangle inequality now implies that P<2k+ty L − P<2k+tx L ≤ P<2k+t|y−x| L, from which we deduce from (6) that |f(y)1/2 − f(x)1/2| ≤ f(|x − y|)1/2.

We now prove a slightly weaker version of Theorem 1, which is nevertheless enough to imply P<n ∞ ≤

√6n. Theorem 9. We have the bounds

![image 35](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile35.png>)

f(x) ≤

- In particular, f(x) ≤ 6x for all x ≥ 0.


 

6x, if x ∈ [1, 34];

![image 36](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile36.png>)

- 8, if x ∈ [34, 1625];

![image 37](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile37.png>)

![image 38](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile38.png>)

- 9, if x ∈ [2516, 2].




![image 39](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile39.png>)

(9)

- 8
- 9


| | | | | |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |


6

4

- 1 4/3 3/2 83/48 2

0

- 2


Figure 1. Graph of f(x) with bounds proven in Theorem 9 (black) and (10) (red). Note that f(8348) > 8, so we are unable to prove a bound f(x) ≤ 8 on the whole interval [34, 2].

![image 40](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile40.png>)

![image 41](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile41.png>)

Proof. It is enough by continuity to prove these inequalities for a dyadic rational, and hence it is enough to prove the appropriately scaled inequalities for integers n = 2kx. We prove the result by induction on n. Clearly f(0) = 0 2L = 0 and f(1) = 1 2L = 2 satisfy these conditions.

First suppose 1 ≤ x ≤ 43. Write x = 1+y so that n = 2kx = 2k +r, r = 2ky < 2k−1. Then by induction f(r) ≤ 6r and so f(y) ≤ 6y. Now, by Lemma 8,

![image 42](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile42.png>)

√

f(x) ≤ f(1)1/2 + f(y)1/2 2 ≤

2 + 6y 2 = 2 + 4 3y + 6y ≤ 6 + 6y = 6x for all y ≤ 31.

![image 43](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile43.png>)

![image 44](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile44.png>)

![image 45](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile45.png>)

![image 46](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile46.png>)

Now suppose 43 ≤ x ≤ 118 . Again write x = 1 + y so that n = 2k + r, r = 2ky < 2k−1. Now 4y ∈ [43, 23], so by induction (r < n), f(y) = 14f(4y) ≤ 41 · 8 = 2. Hence

![image 47](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile47.png>)

![image 48](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile48.png>)

![image 49](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile49.png>)

![image 50](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile50.png>)

![image 51](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile51.png>)

![image 52](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile52.png>)

√

√

2 2 = 8, as required.

f(x) ≤ f(1)1/2 + f(y)1/2 2 ≤

![image 53](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile53.png>)

![image 54](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile54.png>)

2 +

It remains to prove the theorem in the case when x ∈ [118 , 2], the last statement then following from the fact that f(x) ≤ 6x for all x ∈ [1, 2], and f(2x) = 2f(x) for all x ≥ 0. In fact, it will help in the proof of Theorem 1 to prove the very slightly stronger bound

![image 55](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile55.png>)

f(x) ≤ 7.92 if x ∈ [118 , 2516]. (10)

![image 56](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile56.png>)

![image 57](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile57.png>)

The inequalities (9) and (10) however are never equalities on [118 , 2] (see Figure 1 for a plot of f(x)). As f(x) can be readily calculated by computer, Lemma 8 allows us to provide a

![image 58](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile58.png>)

computer assisted proof on an interval around any dyadic point. The result will then follow by exhibiting a collection of such intervals that cover [118 , 2].

![image 59](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile59.png>)

More speciﬁcally, we use the values of x in Table 1 to show that f(y) ≤ 7.92 for all

- y ∈ [118 , 1625], and the values of x in Table 2 to show that f(y) ≤ 9 for all y ∈ [1625, 2]. In each


![image 60](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile60.png>)

![image 61](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile61.png>)

![image 62](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile62.png>)

x (binary) x (decimal) f(x) Interval covered

1.011 1.375000 6.250000 [1.358355, 1.391645]1 1.01101 1.406250 6.491173 [1.390625, 1.421875]∗ 1.011011 1.421875 6.955324 [1.415772, 1.427978]2 1.0111 1.437500 6.625000 [1.427730, 1.447270]1 1.1 1.500000 5.000000 [1.437500, 1.562500]3

- Table 1. Values of f(x) used to bound f(x) ≤ 7.92 in [1.375, 1.5625] = [118 , 1625] along with the intervals where bound is proven. The index i on the interval indicates that the range [x − r, x + r] was limited in this case by a bound on f(r) corresponding to a scaled version of case i in (9). A star on the interval indicates r was limited by the restriction |y − x| ≤ r = 2−k−1 in Lemma 8.

![image 63](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile63.png>)

![image 64](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile64.png>)

x (binary) x (decimal) f(x) Interval covered

1.101 1.625000 5.971801 [1.562500, 1.687500]∗ 1.1011 1.687500 7.090947 [1.668559, 1.706441]1 1.10111 1.718750 7.284252 [1.703125, 1.734375]∗ 1.11 1.750000 6.500000 [1.716177, 1.783823]1 1.1101 1.812500 6.239011 [1.781250, 1.843750]∗ 10. 2.000000 4.000000 [1.833334, 2.166666]1

- Table 2. Values of f(x) used to bound f(x) ≤ 9 in [1.5625, 2] = [1625, 2] along with the intervals where bound is proven. The indices i on the intervals are as in Table 1.


![image 65](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile65.png>)

case we use Lemma 8 to bound f(y) in an interval [x − r, x + r] around x using induction and (9) (scaled appropriately using f(|y − x|) = 2−tf(2t|y − x|) with 2t|y − x| ∈ [1, 2]) to bound f(|y − x|) for |y − x| ≤ r.

Computer calculations of f(x) were performed by evaluating P<n(z) for n = 2kx on all 224th roots of unity. The maximum error bound in f(x) being easily seen to be less that 10−6 in all cases (e.g., by the argument on page 551 of [8]).

Proof of Theorem 1. Write nk = 34 ·2k + 31 and note that nk is only an integer when k is odd, and that √6nk − 2 − 1 = 2(k+3)/2 − 1.

![image 66](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile66.png>)

![image 67](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile67.png>)

![image 68](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile68.png>)

We shall prove by induction on k that P<n ∞ ≤

√6n − 2 − 1, for 1 ≤ n ≤ 2k+1; and (11) P<n ∞ ≤ 2(k+3)/2 − 1, for nk ≤ n ≤ 2516 · 2k; (12)

![image 69](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile69.png>)

![image 70](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile70.png>)

where we note that (12) implies (11) for nk ≤ n ≤ 1625 ·2k. It is easy to see that (11) and (12) hold for k = 0, 1, so assume k ≥ 2.

![image 71](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile71.png>)

Suppose 2k < n < nk and write n = 2k + r, where r < nk − 2k = nk−2. As 0 < r ≤ 2k−1 we have P<n(z) = Pk(z) + z2kP<r(z) and, by induction,

P<n ∞ ≤ Pk ∞ + P<r ∞ ≤ 2(k+1)/2 + √6r − 2 − 1. Now r ≤ nk−2 implies √6r − 2 ≤ 2(k−1)/2, so

![image 72](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile72.png>)

![image 73](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile73.png>)

(2(k+1)/2 + √6r − 2)2 = 2k+1 + 6r − 2 + 2(k+3)/2√6r − 2 ≤ 2k+1 + 6r − 2 + 2(k+3)/2 · 2(k−1)/2

![image 74](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile74.png>)

![image 75](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile75.png>)

= 6(2k + r) − 2 = 6n − 2. Hence P<n ∞ ≤

√6n − 2 − 1, as required.

![image 76](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile76.png>)

Now suppose nk ≤ n < 118 · 2k and write n = 2k + r with nk−2 ≤ r ≤ 23 · 2k−2 < 2516 · 2k−2. Again we have P<n(z) = Pk(z) + z2kP<r(z) and, by induction,

![image 77](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile77.png>)

![image 78](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile78.png>)

![image 79](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile79.png>)

P<n ∞ ≤ Pk ∞ + P<r ∞ ≤ 2(k+1)/2 + 2(k+1)/2 − 1 = 2(k+3)/2 − 1, as required.

Now for 118 · 2k ≤ n ≤ 2516 · 2k we simply use (10) to obtain P<n ∞ ≤ P<n L ≤

![image 80](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile80.png>)

![image 81](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile81.png>)

√

![image 82](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile82.png>)

7.92 · 2k/2 < 2(k+3)/2 − 1,

where the last inequality holds for k ≥ 13. For k ≤ 12 computer calculations show directly that P<n L < 2(k+3)/2 − 1 for this range of n.

Finally, for 1625 · 2k ≤ n ≤ 2k+1 we have P<n ∞ ≤ P<n L ≤ 3 · 2k/2 < 6 · 1625 · 2k − 2 − 1 ≤

![image 83](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile83.png>)

√6n − 2 − 1

![image 84](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile84.png>)

![image 85](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile85.png>)

![image 86](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile86.png>)

for k ≥ 7, and for k ≤ 6 computer calculations show directly that P<n L < √6n − 2 − 1 for this range of n.

![image 87](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile87.png>)

4. Proof of Theorem 3 We can deﬁne, in analogy to f(x) above, the function

f(m, n) := P[m,n) 2L and extend by Lemma 6 and then by continuity to a continuous function f(x, y) deﬁned for all 0 ≤ x ≤ y, x, y ∈ R, that satisﬁes

f(2x, 2y) = 2f(x, y).

Again the strategy is to use a computer to check most of the parameter space (x, y), which by scaling and translating can be assumed to be [0, 2]×[2, 4]. The main diﬃculty is that the P[m,n) corresponding to (x, y) near the extremal point (53, 38) does not exhibit such a simple decomposition as before. Thus we will need to deal with a more complicated version of our

![image 88](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile88.png>)

![image 89](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile89.png>)

· L norm.

Deﬁne the following function for any r, s ∈ N, g(r, s) = sup

P<s(z) + αz−1P<r(−z−1) 2L. Proposition 10. The function g satisﬁes the following properties.

|α|=1

- (a) For all r, s ≥ 0, g(s, r) = g(r, s).
- (b) For all r, s ≥ 0, g(2r, 2s) = 2g(r, s).
- (c) There exists a constant C > 0 such that for all r, s, r′, s′ ≥ 0, g(r, s)1/2 − g(r′, s′)1/2 ≤ C|r − r′|1/2 + C|s − s′|1/2.


Proof. The ﬁrst part follows immediately by simply substituting z  → −z−1 and α  → −α−1 in the deﬁnition of g(s, r). For the second part we note by Proposition 4(b) that

P<2s(z) + αz−1P<2r(−z−1) = P<s(z2) + zP<s(−z2) + αz−1P<r(z−2) − αz−2P<r(−z−2), and hence

P<2s(−z) − αz−1P<2r(z−1) = P<s(z2) − zP<s(−z2) − αz−1P<r(z−2) − αz−2P<r(−z−2). Thus by the parallelogram rule

P<2s(z) + αz−1P<2r(−z−1) 2 + P<2s(−z) − αz−1P<2r(z−1) 2

= 2 P<s(z2) − αz−2P<r(−z−2) 2 + 2 zP<s(−z2) + αz−1P<r(z−2) 2

= 2 P<s(z2) − αz−2P<r(−z−2) 2 + 2 P<s(−z2) + αz−2P<r(z−2) 2 ≤ 2 P<s(z2) − αz−2P<r(−z−2) 2L ≤ 2g(r, s).

The result now follows by taking the supremum over z and α. The last statement is immediate from the triangle inequality for  · L together with (5). As with the function f, we can now extend the deﬁnition of g to non-negative dyadic

rationals by setting

g(x, y) = 2−kg(2kx, 2ky), (13) where 2kx, 2ky ∈ N, and then extend the deﬁnition of g by continuity (Proposition 10(c)) to all real x, y ≥ 0. The following shows that we can use the function g to bound the function f in a (rather large) neighborhood of the critical point (53, 83).

![image 90](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile90.png>)

![image 91](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile91.png>)

Lemma 11. If 0 ≤ x, y ≤ 1 then

f(2 − x, 2 + y) ≤ g(x, y).

Proof. By continuity it is enough to prove this for dyadic rationals, and by scaling it is then enough to show that for integers r = 2k−1x and s = 2k−1y with 0 ≤ r, s ≤ 2k−1 we have

f(2k − r, 2k + s) ≤ g(r, s).

this however follows immediately from the deﬁnitions of f and g together with the fact that P[2k−r,2k+s)(z) = P[2k−r,2k)(z) + P[2k,2k+s)(z) = ±z2k−1P<r(−z−1) + z2kP<s(z).

Remark 12. The diﬀerence between g(r, s) and f(2k − r, 2k + s) is that we lose information on the phase diﬀerence of the P<r(−z−1) term and the P<s(z) term. This is important due to the rather strange way in which we will need to decompose our polynomials P[m,n) when (m, n) is close to (mk, nk). However, it is not enough to deﬁne g(r, s) more simply as  |P<s(z)| + |P<r(−z−1)| 2L as this quantity is too large near the critical values of (r, s). It is important that the same α is used for both the z and −z terms deﬁning the · L norm in the deﬁnition of g.

Although the deﬁnition of g(r, s) is easy to use in proofs, it does not look so easy to calculate numerically due to the fact that we are taking supremums over both z and α. However, one can rewrite g(r, s) in a form that avoids the supremum over α. The following was therefore used in the numerical calculations of g(r, s).

- Lemma 13. For non-negative integers r and s,


|P<r(z)|2 + |P<r(−z)|2 + |P<s(z)|2 + |P<s(−z)|2

g(r, s) = sup

|z|=1

+2|P<s(z)P<r(−z) − P<s(−z)P<r(z)| . Proof. Write the function g(r, s) as sup|α|=1 sup|z|=1 Sr,s(α, z), where

Sr,s(α, z) = |P<s(z) + αz−1P<r(−z−1)|2 + |P<s(−z) − αz−1P<r(z−1)|2

= P<s(z) + αzP¯ <r(−z¯) P<s(¯z) + αzP¯ <r(−z) + {z  → −z}

= |P<s(z)|2 + |P<r(−z)|2 + αzP¯ <r(−z¯)P<s(¯z) + αzP¯ <s(z)P<r(−z) + {z  → −z}

= |P<r(z)|2 + |P<r(−z)|2 + |P<s(z)|2 + |P<s(−z)|2

+ αz¯ P<s(z)P<r(−z) − P<s(−z)P<r(z)) + {cplx. conj.}. Clearly the sum of the last two terms in maximized when α is chosen so that

αz¯ P<s(z)P<r(−z) − P<s(−z)P<r(z)) is a positive real. Thus

Sr,s(α, z) = |P<r(z)|2 + |P<r(−z)|2 + |P<s(z)|2 + |P<s(−z)|2

sup

|α|=1

+ 2|P<s(z)P<r(−z) − P<s(−z)P<r(z)|. The result follows on taking the supremum over z.

The following are reﬁned versions of the continuity statements for f and g that we will need later in the computer assisted proofs.

- Lemma 14. If 2kx, 2ky ∈ N and |x − x′|, |y − y′| ≤ 2−k−1, then

- f(x′, y′)1/2 − f(x, y)1/2 ≤ f(|x′ − x|)1/2 + f(|y′ − y|)1/2 ≤ 3 · 2−k/2, (14)
- g(x′, y′)1/2 − g(x, y)1/2 ≤ f(|x′ − x|)1/2 + f(|y′ − y|)1/2 ≤ 3 · 2−k/2. (15)


Proof. Follows from the same proof as in Lemma 8. For the last inequality we note that if z ≤ 2−k−1 then f(z) ≤ 2−k−2f(2k+2z) ≤ 9 · 2−k−2. Hence f(|x′ − x|)1/2 + f(|y′ − y|)1/2 ≤ 2 · 3 · 2−(k+2)/2 = 3 · 2−k/2.

The following is the key inequality needed to bound g(x, y) near the critical point (43, 83).

![image 92](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile92.png>)

![image 93](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile93.png>)

- Lemma 15. For all x ∈ [0, 21] and y ∈ [0, 1],

![image 94](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile94.png>)

g(1 + x, 2 + y)1/2 ≤

√

![image 95](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile95.png>)

10 + g(x, y)1/2.

Proof. Writing r = 2k−1x and s = 2k−1y we have 0 ≤ r ≤ 2k−2 and 0 ≤ s ≤ 2k−1. Thus P<2k−1+r(z) = P<2k−1(z) + z2k−1P<r(z) and P<2k+s(z) = P2k(z) + z2kP<s(z). Clearly we may assume k ≥ 2, so that

g(2k−1 + r, 2k + s)1/2 = sup

α

P<2k(z) + z2

k

P<s(z) + αz−1P<2k−1(−z−1) + αz−1−2

k−1

P<r(−z−1) L ≤ sup

α

P<2k(z) + αz−1P<2k−1(−z−1) L + sup

α

z2

k

P<s(z) + αz−1−2

k−1

P<r(−z−1) L

= g(2k−1, 2k)1/2 + sup

β,z

P<s(z) + βz−1P<r(−z−1), P<s(−z) − βz−1P<r(z−1) 2

= g(2k−1, 2k)1/2 + sup

β

P<s(z) + βz−1P<r(−z−1) L

= g(2k−1, 2k)1/2 + g(r, s)1/2, where β = αz−3·2k−1 = α(−z)−3·2k−1. Hence after scaling we have

g(1 + x, 2 + y)1/2 ≤ g(1, 2)1/2 + g(x, y)1/2. Finally we observe that

g(1, 2) = sup

α,z

|1 + z + αz−1|2 + |1 − z − αz−1|2

= sup

α,z

2 |1|2 + |z + αz−1|2) = 2 · (12 + 22) = 10.

We now come to the key bound we need on g(x, y).

- Lemma 16. For x ∈ [0, 2], y ∈ [0, 4] we have g(x, y) ≤ min{10(x + y), 40}. (16)


- In particular, g(x, y) ≤ 10(x + y) for all x, y ≥ 0.


Proof. We use induction to bound g(r, s) for integers r, s, and scale using (13), however for ease of exposition we will write the proof in terms of x, y ∈ R, which by continuity may be considered dyadic rationals.

Firstly, we can reduce to the case when (x, y) lies inside the blue contour in Figure 2, namely

(x, y) ∈ B := ([0, 2] × [0, 4]) \ ([0, 1] × [0, 2]) \ ([0, 2] × [0, 1]). Indeed, for x ≥ y we have g(x, y) = g(y, x), and for x ≤ y, (x, y) ∈ [0, 1] × [0, 2], we have 2k(x, y) ∈ B for some k ≥ 1. Then

g(2kx, 2ky) ≤ min{10(x + y), 40 · 2−k} ≤ min{10(x + y), 40}.

g(x, y) = 21

![image 96](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile96.png>)

k

If x = 1 + x′ ∈ [1, 32] and y = 2 + y′ ∈ [2, 3] (inside red contour in Figure 1) induction (2kx′ < 2kx, 2ky′ < 2ky) implies that

![image 97](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile97.png>)

g(x′, y′) = 41g(4x′, 4y′) ≤ 14 min{10(4x′ + 4y′), 40} = min{10(x′ + y′), 10}. Thus by Lemma 15

![image 98](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile98.png>)

![image 99](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile99.png>)

√

√

![image 100](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile100.png>)

![image 101](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile101.png>)

![image 102](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile102.png>)

g(x, y)1/2 ≤

10 + min{ 10(x′ + y′),

10}, so for x + y ≤ 4 (x′ + y′ ≤ 1) we have

√

10 + 10(x′ + y′) 2 = 10 + 20 x′ + y′ + 10(x′ + y′) ≤ 30 + 10(x′ + y′) = 10(x + y),

![image 103](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile103.png>)

![image 104](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile104.png>)

![image 105](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile105.png>)

g(x, y) ≤

and for x + y ≥ 4 (x′ + y′ ≥ 1)

√

√

10 2 = 40.

![image 106](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile106.png>)

![image 107](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile107.png>)

g(x, y) ≤

10 +

In the remaining cases (between the red and blue contours) the inequality is strict, and so can be proved by computer. We divide up the region into dyadic squares Sr,s = [2−kr, 2−k(r+ 1)]×[2−ks, 2−k(s+1)] and evaluate g(x, y) numerically at each corner of Sr,s. We then divide Sr,s up into 4 smaller dyadic squares S′

r′,s′ = [2−k−1r′, 2−k−1(r′ +1)]×[2−k−1s′, 2−k−1(s′ +1)], r′ ∈ {2r, 2r + 1}, s′ ∈ {2s, 2s + 1}. Using Lemma 14 we try to prove the bound (16) for each of the four smaller squares S′

r′,s′ using the value of g(x, y) at the corresponding corner of Sr,s. Note that all points (x′, y′) ∈ S′

r′,s′ satisfy the conditions |x′ − x|, |y′ − x| ≤ 2−k−1. If this fails, we recursively subdivide each S′

r′,s′ in the same way. Once we get to squares of side length 2−6 we give up and mark the square as bad.

This procedure was applied to the whole of [0, 4]2 and the result is shown in Figure 2. The only bad squares that lie inside the blue contour also lie inside the red contour, so we are done.

Proof of Theorem 3. The result clearly holds for 0 ≤ m ≤ n < 2, so assume n ≥ 2 and ﬁx k ≥ 0 so that 2k+1 ≤ n < 2k+2. Now if m ≥ 2k+1 we can use the fact that Qk+1(z) = ±z2k+1−1Pk+1(−z−1) to deduce that P[m,n) L = P[2k+2−n,2k+2−m) L. But 2k+2 − m < n,

- 0
- 1
- 2
- 3
- 4


- 2
- 3
- 4


0 1 2 3 4

0 1 2

Figure 2. Bounding g(x, y) in Lemma 16 (left) and f(x, y) in Theorem 3 (right). Region between red and blue contours is divided recursively into squares in an attempt to prove bounds. The boundaries of the squares are shown only if the ﬁrst attempt to bound f or g on them failed (so they occur as an Sr,s square in the proofs). On the left, the dashed line indicates the line 10(x + y) = 40. The regions outside of the blue contours and inside the red contours are shown for illustration only and are not used in the proofs.

so we are done by induction on n. Thus we may assume that m = 2kx, n = 2ky, with (x, y) ∈ [0, 2] × [2, 4]. For (x, y) ∈ [1, 2] × [2, 3] we use Lemmas 11 and 16 to deduce that

f(x, y) ≤ g(2 − x, y − 2) ≤ 10(y − x).

In all other cases the bounds are strict, and so can be proved by computer in an exactly analogous way to Lemma 16.

5. Proof of Theorem 7

We ﬁrst describe the strategy used to prove Theorem 7. We apply Proposition 4(b) to deduce that

k+1

k

k+1

P[2k+1m,2k+1n)(w) = Pk(w)P[m,n)(w2

) + w2

Qk(w)P[m,n)(−w2

) = (Pk(w), Qk(w))T, (P[m,n)(¯z2), zP¯ [m,n)(−z¯2))T ,

where z = w2k and u, v = uTv¯ is the standard inner product on C2. To maximize this expression we pick z to be such that (P[m,n)(z2), P[m,n)(−z2)) 2 is maximized, so that then

(P[m,n)(¯z2), zP¯ [m,n)(−z¯2)) 2 = (P[m,n)(z2), P[m,n)(−z2)) 2 = P[m,n) L. We then wish to pick w so that (Pk(w), Qk(w)) is nearly parallel to (P[m,n)(¯z2), zP¯ [m,n)(−z¯2)) so as to maximize

the inner product. In this case we would have P[2k+1m,2k+1n)(w) = (Pk(w), Qk(w))T, (P[m,n)(¯z2), zP¯ [m,n)(−z¯2))T ≈ (Pk(w), Qk(w)) 2 · (P[m,n)(¯z2), zP¯ [m,n)(−z¯2)) 2

= 2(k+1)/2 P[m,n) L,

and so |P[2k+1m,2k+1n)(w)|/2(k+1)/2 ≈ P[m,n) L as required. Hence it is enough to show that, for large k, we can approximate any vector in the 3-sphere

S3 := {(α, β) ∈ C2 : |α|2 + |β|2 = 1} with (Pk(w)/2(k+1)/2, Qk(w)/2(k+1)/2) for an appropriately chosen w.

In [9] it was shown that for w taken uniformly at random from S1 := {w ∈ C : |w| = 1} we have that Pk(w)/2(k+1)/2 converges in distribution as k → ∞ to a uniform random variable in the unit disk D := {z ∈ C : z ≤ 1}. Indeed, a stronger theorem was proved. Let

and note that

1 √2

G(w) =

![image 108](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile108.png>)

![image 109](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile109.png>)

1 w 1 −w

Pk(w)/2(k+1)/2 Qk(w)/2(k+1)/2

k−1

= G(w2

k−2

)G(w2

) · · ·G(w2)G(w)

2−1/2 2−1/2

In [9] it is shown that if w is distributed uniformly on S1, then G(w2k−1) · · ·G(w) tends in distribution to the Haar measure on the compact Lie group U(2). This implies that (Pk(w)/2(k+1)/2, Qk(w)/2(k+1)/2) tends in distribution to a uniform random variable in S3, and in particular we can approximate any (α, β) ∈ S3 arbitrarily accurately as k → ∞.

However, we also need the condition that w2k = z, so we cannot take w to be uniform in S1. Fortunately the proof in [9] actually proves the following stronger statement.

Theorem 17. For each k, let w = wk be drawn from a distribution Dk supported on S1 with the property that E(wn) = 0 for all n such that 2k | n. Then G(w2k−1) · · ·G(w) tends in distribution to the Haar measure on U(2) as k → ∞.

Indeed, the proof in [9] follows by showing that, for any (ﬁnite dimensional) irreducible representation π of U(2),

k−1

E π(G(w2

)) . . .π(G(w)) → 0 as k → ∞. (17)

Convergence in distribution to the Haar measure then follows from standard results (see Theorem 2.1 of [9]).

For each ﬁxed π, the expression inside the expectation in (17) is a matrix with entries that are polynomials in w and w−1, and the proof in [9] proceeds by induction on k, keeping

only the terms wn with 2k | n at each stage. More speciﬁcally, assume π is of dimension d and let v ∈ Cd be ﬁxed. Then

)) · · ·π(G(w))v = p(1k)(w), . . ., p(dk)(w) T where each p(ik)(w) = 2

k−1

π(G(w2

kM

j=−2kN p(i,jk)wj ∈ C[w, w−1] for some ﬁxed N and M depending only on π. The coeﬃcients p(i,k2+1)

kj depend only on the coeﬃcients p(ℓ,k2)

km as the entries of the d ×d matrix π(G(w2k)) all lie in C[w2k, w−2k]. Thus by ignoring all terms wn with 2k | n in pi(k) and dropping terms with 2k+1 | n in p(ik+1) we obtain a linear map

kj i,j = p(i,k2+1)

S: Cd(N+M+1) → Cd(N+M+1); S p(i,k2)

k+1j i,j which is in fact easily seen to be independent of k. It is then shown that S = ρ < 1 and so p(i,k2)

kj → 0 as k → ∞ for all i, j.

In [9] it is enough that the j = 0 terms tend to 0 as for a uniform random variable on S1 we have E(wn) = 0 for all n = 0. However, the proof clearly shows that the whole vector

p(i,k2)

kj i,j ∈ Cd(N+M+1) tends to 0 as k → ∞. Thus if E(wn) = 0 for all n with 2k | n (and |E(wn)| ≤ 1 otherwise) we see that for any v ∈ Cd,

k−1

E π(G(w2

)) · · ·π(G(w))v 2 → 0 as k → ∞. Hence (17) holds and Theorem 17 follows. Proof of Theorem 7. As shown above, it is enough to show that for any (α, β) ∈ S3, ε > 0, and z ∈ S1 we can ﬁnd, for suﬃciently large k, a w satisfying w2k = z with

(Pk(w)/2(k+1)/2, Qk(w)/2(k+1)/2) − (α, β) 2 < ε

For each k we let w = wk be chosen uniformly at random from the solutions of w2k = z and note that E(wn) = 0 for all n with 2k | n. Thus we can apply Theorem 17 to deduce that

2−1/2 2−1/2

Pk(w)/2(k+1)/2 Qk(w)/2(k+1)/2

k−1

= G(w2

) · · ·G(w2)G(w)

tends in distribution to the uniform measure on S3 as k → ∞. Thus for suﬃciently large k, there is a positive probability that (Pk(w)/2(k+1)/2, Qk(w)/2(k+1)/2) lies in the ball of radius ε around (α, β) ∈ S3, and hence there exists a solution w of w2k = z with this property.

Finally we deduce (2) by estimating P[m

k,nk) L. Recall that mk :=

5 · 4k + 1 3

8 · 4k + 1 3

. Thus mk = 4mk−1 − 1 and nk = 4nk−1 − 1. Also it is easy to check that am

, nk :=

![image 110](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile110.png>)

![image 111](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile111.png>)

= 1 and an

k

= −1 for k ≥ 0. Hence, by Proposition 4(b), P[m

k

k,nk)(z4) + z2Q2(z)P[m

k,nk)(−z4) + am

zm

zn

k+1,nk+1)(z) = P2(z)P[m

− an

k+1

k+1

k+1

k+1

k,nk)(z4) + (z2 − z3)P[m

k,nk)(−z4) + zm

+ zn

= (1 + z)P[m

. (18)

k+1

k+1

0,n0)(z) = P[2,3)(z) = z2 = 1 and P[m

Taking z = ±1 we have P[m

k,nk)(−1) − 2. From this it follows by induction that

k+1,nk+1)(1) = 2P[m

k,nk)(1) + 2, and P[m

k+1,nk+1)(−1) = 2P[m

k,nk)(−1) = −2k + 2 (19) for all k ≥ 0. Thus

k,nk)(1) = 3 · 2k − 2 and P[m

P[m

2

k,nk)(1)2 + P[m

k,nk)(−1)2

P[m

L ≥ P[m

k,nk)

≥ (3 · 2k − 2)2 + (−2k + 2)2 = 10 · 22k − 16 · 2k + 8. Thus in particular (as nk − mk = 4k)

2 L

P[m

k,nk)

liminf

nk − mk ≥ 10. As the ratio is always at most 10 by Theorem 3, we deduce that (2) holds. To see an explicit case when |P[m

![image 112](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile112.png>)

k→∞

![image 113](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile113.png>)

k,nk)(z)| > 3 (nk − mk) we can take z = e3πi/4. Then

- z4 = −1 and so (18) and (19) imply


k+1,nk+1)(z) = (1 + z)(−2k + 2) + (z2 − z3)(3 · 2k − 2) + O(1)

P[m

= (−1 − z + 3z2 − 3z3)2k + O(1). Hence

k,nk(e3πi/4)|2 nk − mk

|P[m

1 4 − 1 − e3πi/4 + 3e6πi/4 − 3e9πi/4 2 + o(1) = 5 + √72 + o(1).

=

![image 114](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile114.png>)

![image 115](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile115.png>)

![image 116](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile116.png>)

![image 117](<2019-balister-bounds-rudin-shapiro-polynomials-arbitrary_images/imageFile117.png>)

References

- [1] H. Alzer, Note on an extremal property of the Rudin–Shapiro sequence. Abh. Math. Sem. Univ. Hamburg 65 (1995), 243–248.
- [2] J. Brillhart, On the Rudin–Shapiro polynomials, Duke Math. J., 40 (1973), 335–353.
- [3] J. Brillhart and L. Carlitz, Note on the Shapiro polynomials, Proc. Amer. Math. Soc., 25 (1970), 114–119.
- [4] J. Brillhart, J.S. Lomont and P. Morton, Cyclotomic properties of the Rudin–Shapiro polynomials, J. Rein. Angew. Math., 288 (1976), 37–65.
- [5] C. Doche and L. Habsieger, Moments of the Rudin-Shapiro polynomials, J. Fourier Anal. Appl., 10

(2004), 497–505.

- [6] M.J.E. Golay, Multislit spectrometry, J. Opt. Soc. Am. 39 (1949), 437–444.
- [7] C. Mauduit and J. Rivat, Prime numbers along Rudin–Shapiro sequences, J. Eur. Math. Soc., 17 (2015), 2595–2642.
- [8] H.L. Montgomery, Littlewood polynomials, In: Analytic Number Theory, Modular Forms and qhypergeometric Series, Springer Proc. Math. Stat., 221, Springer, Cham, 2017, pp. 533–553.
- [9] B. Rodgers, On the distribution of Rudin–Shapiro polynomials and lacunary walks on SU(2), Adv. Math., 320 (2017), 993–1008
- [10] W. Rudin, Some theorems on Fourier coeﬃcients, Proc. Amer. Math. Soc., 10 (1959), 855–859.
- [11] B. Saﬀari, Une fonction extr´emale li´ee ` la suite de Rudin–Shapiro, C. R. Acad. Sci. Paris Se´r. I Math, 303 (1986) 97–100.


- [12] H.S. Shapiro, Extremal problems for polynomials, Thesis for S.M. Degree, MIT, 1952, 102 pp. Avaliable at https://dspace.mit.edu/handle/1721.1/12247


Department of Mathematical Sciences, University of Memphis, Memphis, TN 38152, USA E-mail address: pbalistr@memphis.edu

