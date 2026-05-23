arXiv:1302.2299v2[math.NT]25Jan2014

ON IMPROVING ROTH’S THEOREM IN THE PRIMES

ERIC NASLUND

Abstract. Let A ⊂ {1,...,N} be a set of prime numbers containing no non-trivial arithmetic progressions. Suppose that A has relative density α = |A|/π(N), where π(N) denotes the number of primes in the set {1,...,N}. By modifying Helfgott and De Roton’s work [8], we improve their bound and show that

(log log log N)6 log log N

.

α ≪

![image 1](<2013-naslund-improving-roth-theorem-primes_images/imageFile1.png>)

1. Introduction

In 1936, Erdös and Turán [3] conjectured that if a set A ⊂ N = {1, 2, 3 . . .} contains no k term arithmetic progressions, then it cannot be “too large.” We say that A ⊂ N has positive (upper) density if for some ǫ > 0

1 x n≤x

1A(x) ≥ ǫ,

limsup

![image 2](<2013-naslund-improving-roth-theorem-primes_images/imageFile2.png>)

x→∞

and throughout this section we will exclude those trivial arithmetic progressions whose diﬀerence is 0. In 1953, Roth [10] proved that if a set A ⊂ N = {1, 2, 3 . . .} contains no non-trivial arithmetic progressions, then A has density 0. Quantitatively he showed that any progression free set of integers A satisﬁes

N log log N

|A ∩ {1, 2, . . ., N}| ≪

.

![image 3](<2013-naslund-improving-roth-theorem-primes_images/imageFile3.png>)

Roth’s Theorem has been improved signiﬁcantly over the last 60 years by Heath-Brown, Szemerédi, Bourgain, [7, 12, 1, 2] and most recently Sanders [11], who obtained

N (log log N)5 log N

.

|A ∩ {1, 2, . . ., N} | ≪

![image 4](<2013-naslund-improving-roth-theorem-primes_images/imageFile4.png>)

Moving to the set of prime numbers, which we will denote P, we deﬁne the relative density of a set A ⊂ P up to N to be

|A ∩ {1, 2, . . ., N} | |P ∩ {1, 2, . . .N} |

- (1.1) α(N) =


.

![image 5](<2013-naslund-improving-roth-theorem-primes_images/imageFile5.png>)

In 1939, Van Der Corput [13] showed that P contains inﬁnitely many non-trivial three term arithmetic progressions. Green [4] proved an analogue of Roth’s Theorem inside

![image 6](<2013-naslund-improving-roth-theorem-primes_images/imageFile6.png>)

Date: December 6th, 2013.

1

the primes, showing that if A ⊂ P contains no non-trivial arithmetic progressions, then

α(N) ≪

log log log log log N log log log log N

![image 7](<2013-naslund-improving-roth-theorem-primes_images/imageFile7.png>)

- 1

![image 8](<2013-naslund-improving-roth-theorem-primes_images/imageFile8.png>)

- 2


,

where the notation f(N) ≪ g(N) means that there exists an absolute constant C such that f(N) ≤ Cg(N) for all N ≥ 1. Helfgott and De Roton [8] improved this density bound, removing two log’s from the denominator to obtain

- (1.2) α(N) ≪

log log log N (log log N)

![image 9](<2013-naslund-improving-roth-theorem-primes_images/imageFile9.png>)

1 3

![image 10](<2013-naslund-improving-roth-theorem-primes_images/imageFile10.png>)

.

Their result implicitly uses the best quantitative bound on Roth’s Theorem in the integers, and when the proof is run through again with Sander’s bound, the density recovered is

- (1.3) α(N) ≪


5 2

(log log log N)

![image 11](<2013-naslund-improving-roth-theorem-primes_images/imageFile11.png>)

.

![image 12](<2013-naslund-improving-roth-theorem-primes_images/imageFile12.png>)

- 1

![image 13](<2013-naslund-improving-roth-theorem-primes_images/imageFile13.png>)

- 2


(log log N)

Our main result is the following: Theorem 1. Suppose that A ⊂ P ∩ [1, N] has relative density α and contains no non-trivial arithmetic progressions. Then

(log log log N)6 log log N

α ≪

.

![image 14](<2013-naslund-improving-roth-theorem-primes_images/imageFile14.png>)

Our proof parallels that of Helfgott and De Roton, and we look at the convolution of the indicator function of the set of primes and the indicator function of a set Σ. We gain a factor of two in the exponent by using the L2k norm, where k is a slowly growing function of N, rather than the L2 norm. Using this higher norm introduces several combinatorial diﬃculties which are dealt with in section 2 and in the proof of proposition 2. This L2k norm bound gives greater control over the outliers, and allows us to choose a larger subset on which the convolution is uniformly bounded from below. As in Helfgott and De Roton, the bound on Roth’s Theorem yields a lower bound on the size of the three term progression operator applied to this uniform set. If the set Σ is chosen correctly, the three term progression operator of the convolution cannot be too far from that of the indicator function of the primes, which gives the desired density bound for the primes.

- 1.1. Preliminaries and Notation. For two functions f, g : N → R, we write f ≪ g, or f(x) = O(g(x)) if there exists a constant C > 0 such that |f(n)| ≤ Cg(n) for all positive integers n. Often we will look at when f ≪ g for suﬃciently large n, which means that there exists N0, C > 0 with |f(n)| ≤ Cg(n) for all n ≥ N0.


To denote |S1| x∈S f(x), the expectation of f over the set S, we write Ex∈Sf(x). Given a function f : Z/NZ → C, where N is a prime, we deﬁne the Fourier transform to be

![image 15](<2013-naslund-improving-roth-theorem-primes_images/imageFile15.png>)

fˆ(t) = Ex∈Z/NZf(x)e2πixt/N.

The convolution operation is given by

- (1.4) (f ∗ g)(x) = Ey∈Z/NZf(y)g(x − y), which is suitably normalized so that
- (1.5) f ∗ g(t) = fˆ(t)ˆg(t). The Lk and ℓk norms are deﬁned to be

f Lk(Z/NZ) = Ex∈Z/NZ|f(x)|k

1 k

![image 16](<2013-naslund-improving-roth-theorem-primes_images/imageFile16.png>)

, and

f ˆ ℓk(Z/NZ) =

 

x∈Z/NZ

|fˆ(x)|k

 

1 k

![image 17](<2013-naslund-improving-roth-theorem-primes_images/imageFile17.png>)

.

When there is no ambiguity, we will omit the notation ℓk(Z/NZ) and Lk(Z/NZ), and simply write   · k. We will make use of the fact that the inner product f, g L2(Z/NZ) = Ex∈Z/NZf(x)g(x), satisﬁes Plancherel’s identity

![image 18](<2013-naslund-improving-roth-theorem-primes_images/imageFile18.png>)

- (1.6) Ex∈Z/NZf(x)g(x) =


![image 19](<2013-naslund-improving-roth-theorem-primes_images/imageFile19.png>)

![image 20](<2013-naslund-improving-roth-theorem-primes_images/imageFile20.png>)

f(t)gˆ(t),

t∈Z/NZ

from which we obtain f L2(G) = f ˆ ℓ2(G). Given functions f, g, h : Z/NZ → C, we let Λ(f, g, h) denote the three term arithmetic progression operator deﬁned by

Λ (f, g, h) = Ex,d∈Z/NZf(x)g(x + d)h(x + 2d).

If 1A is the indicator function of a set A ⊂ Z/NZ, then Λ (1A, 1A, 1A) counts the total number of three term progressions in A, including the trivial progressions. For a set

Σ ⊂ Z/NZ, we let |Σ| denote the cardinality of Σ, and µ(Σ) = |NΣ| denote the relative measure.

![image 21](<2013-naslund-improving-roth-theorem-primes_images/imageFile21.png>)

2. Sieving the Primes

Let A ⊂ [1, N] be a subset of the primes with |A| = αlogNN , and suppose that α ≥ (log N)−

![image 22](<2013-naslund-improving-roth-theorem-primes_images/imageFile22.png>)

1

4. We will remove the small primes using the “W trick,” which allows us to eﬀectively apply certain sieve results later on. Let W = p≤z p be the product of the primes less than z. Splitting into the diﬀerent arithmetic progressions modulo W, there will be exactly φ(W) nontrivial residue classes. By the pigeon hole principle there exists an arithmetic progression AP(b) = b + nW : 1 ≤ n ≤ WN with

![image 23](<2013-naslund-improving-roth-theorem-primes_images/imageFile23.png>)

![image 24](<2013-naslund-improving-roth-theorem-primes_images/imageFile24.png>)

W φ(W)

1 φ(W)

N log N

- (2.1) |AP(b) ∩ A| ≥ α


−

![image 25](<2013-naslund-improving-roth-theorem-primes_images/imageFile25.png>)

![image 26](<2013-naslund-improving-roth-theorem-primes_images/imageFile26.png>)

![image 27](<2013-naslund-improving-roth-theorem-primes_images/imageFile27.png>)

where the W/φ(W) on the right hand side appears since we are not including the primes up to W. Let P be the least prime larger than 3WN , so that 3WN < P ≤ 6WN , and let A0 ⊂ [1, P] be the set

![image 28](<2013-naslund-improving-roth-theorem-primes_images/imageFile28.png>)

![image 29](<2013-naslund-improving-roth-theorem-primes_images/imageFile29.png>)

![image 30](<2013-naslund-improving-roth-theorem-primes_images/imageFile30.png>)

m − b W

A0 = n =

: m ∈ AP(b) ∩ A ,

![image 31](<2013-naslund-improving-roth-theorem-primes_images/imageFile31.png>)

noting that an arithmetic progression in A0 can be lifted to a progression in A. Using equation (2.1) along with some basic asymptotics for the number of primes, we can ﬁnd

- a lower bound for the size of A0. Notice that


- (2.2) log W =

p≤z

log p = θ(z) ∼ z,

so that W ≈ ez, and

W φ(W)

![image 32](<2013-naslund-improving-roth-theorem-primes_images/imageFile32.png>)

=

p≤z

1 −

1 p

![image 33](<2013-naslund-improving-roth-theorem-primes_images/imageFile33.png>)

−1

∼ eγ log z

where γ = limx→∞ n≤x n1 − log x ≈ 0.577 is the Euler-Mascheroni constant. Choosing z = 14 log N, and N suﬃciently large, we may assume that

![image 34](<2013-naslund-improving-roth-theorem-primes_images/imageFile34.png>)

![image 35](<2013-naslund-improving-roth-theorem-primes_images/imageFile35.png>)

- 4

![image 36](<2013-naslund-improving-roth-theorem-primes_images/imageFile36.png>)

- 5


z ≤ log W ≤

4 3

![image 37](<2013-naslund-improving-roth-theorem-primes_images/imageFile37.png>)

z,

which means that the modulus has size N

1

![image 38](<2013-naslund-improving-roth-theorem-primes_images/imageFile38.png>)

5 ≤ W ≤ N

1

![image 39](<2013-naslund-improving-roth-theorem-primes_images/imageFile39.png>)

3, and

- (2.3) log z ≤

W φ(W)

![image 40](<2013-naslund-improving-roth-theorem-primes_images/imageFile40.png>)

≤ 2 log z.

Equation (2.3) along with the inequality P6 ≤ WN implies that and P log6 z ≤ φ(NW), and so by (2.1) we have that

![image 41](<2013-naslund-improving-roth-theorem-primes_images/imageFile41.png>)

![image 42](<2013-naslund-improving-roth-theorem-primes_images/imageFile42.png>)

![image 43](<2013-naslund-improving-roth-theorem-primes_images/imageFile43.png>)

![image 44](<2013-naslund-improving-roth-theorem-primes_images/imageFile44.png>)

|A0| ≥ αP

log z 6 log N

![image 45](<2013-naslund-improving-roth-theorem-primes_images/imageFile45.png>)

− 2 logz

≥ αP

log z 10 log N

![image 46](<2013-naslund-improving-roth-theorem-primes_images/imageFile46.png>)

for N suﬃciently large. Each arithmetic progression inside A0 corresponds to an arithmetic progression in A, and so if A0 contains a three term arithmetic progression, then A must as well. With this in mind, we shift our attention to the progressions inside A0. Deﬁne a = loglogNz 1A

![image 47](<2013-naslund-improving-roth-theorem-primes_images/imageFile47.png>)

0

to be the normalized indicator function for the set A0, which is supported on 0, P3 since we chose P > 3WN . This function satisﬁes

![image 48](<2013-naslund-improving-roth-theorem-primes_images/imageFile48.png>)

![image 49](<2013-naslund-improving-roth-theorem-primes_images/imageFile49.png>)

- (2.4) a 1 = En∈Z/PZa(n) ≥


α 10

, and

![image 50](<2013-naslund-improving-roth-theorem-primes_images/imageFile50.png>)

log N log z

log N log z

a 22 = En∈Z/PZa(n)2 =

En∈Z/PZa(n) =

![image 51](<2013-naslund-improving-roth-theorem-primes_images/imageFile51.png>)

![image 52](<2013-naslund-improving-roth-theorem-primes_images/imageFile52.png>)

a 1.

In section 3 we will examine the key quantity Λ(a, a, a) in detail, and show that it cannot be too small when α is large. To do this, we will need a bound on the L2k norm of the convolution of a and an indicator function 1Σ, which is discussed in the following section.

- 2.1. Bounding the L2k norm of the convolution. Our goal is to provide bounds on the L2k norm of a ∗ σ where σ is the indicator function of a set Σ. Proposition 2. Given z, N, P and a(n) as above,let k be an integer in the range 1 ≤


1

3 z. Suppose that σ = 1

k ≤ 21 log

µ(Σ) is the normalized indicator function of a set Σ ⊂ −P3 , P3 ⊂ Z/PZ. Then for N greater than some ﬁxed N0, we have the bound

Σ

![image 53](<2013-naslund-improving-roth-theorem-primes_images/imageFile53.png>)

![image 54](<2013-naslund-improving-roth-theorem-primes_images/imageFile54.png>)

![image 55](<2013-naslund-improving-roth-theorem-primes_images/imageFile55.png>)

![image 56](<2013-naslund-improving-roth-theorem-primes_images/imageFile56.png>)

![image 57](<2013-naslund-improving-roth-theorem-primes_images/imageFile57.png>)

a ∗ σ 2k ≪ k +

log N log z

![image 58](<2013-naslund-improving-roth-theorem-primes_images/imageFile58.png>)

1−21k

![image 59](<2013-naslund-improving-roth-theorem-primes_images/imageFile59.png>)

- 1

![image 60](<2013-naslund-improving-roth-theorem-primes_images/imageFile60.png>)

- 2k.


|Σ|−

We will make use of a theorem of Klimov on the Selberg sieve. Theorem 3 of [9] states Theorem 3. (Klimov) Let 1 ≤ i ≤ k, 1 ≤ n ≤ M, v0 ≤ v ≤

√

![image 61](<2013-naslund-improving-roth-theorem-primes_images/imageFile61.png>)

M

log2k M , for a ﬁxed v0, and deﬁne Mv (qi, li) to be the number of integers n for which p ∤ qin + li, for each p ≤ v, and each 1 ≤ i ≤ k. Then if u0 = O exp logB v for a ﬁxed constant B > 0, for k ≥ 2, we have

![image 62](<2013-naslund-improving-roth-theorem-primes_images/imageFile62.png>)

M logk v

Mv (qi, li) ≤

k!

![image 63](<2013-naslund-improving-roth-theorem-primes_images/imageFile63.png>)

p

ρ(p) p

1 −

![image 64](<2013-naslund-improving-roth-theorem-primes_images/imageFile64.png>)

1 p

1 −

![image 65](<2013-naslund-improving-roth-theorem-primes_images/imageFile65.png>)

−k

1 + O

log log u0 log v

![image 66](<2013-naslund-improving-roth-theorem-primes_images/imageFile66.png>)

,

where u0 = max(qi, ui,j), ui,j = |liqj − ljqi| (1 ≤ j ≤ k), and ρ(p) is the number of n ∈ {1, . . ., p} such that

k

(qin + li) ≡ 0 mod p.

i=1

We elect to reference the above theorem, rather than theorem 5.7 from Halberstam and Richert [6], as Klimov’s result allows us to make the dependence on the number variables explicit. As a direct corollary, we have that

- Lemma 4. Let k ≥ 2, and let W and b satisfy log b ≤ 2 log P and log W ≤ 2 log P, where P ≥ P0 for some ﬁxed P0. Suppose that we have k pairwise distinct bi, all relatively prime to W, such that bi ≤ b for 1 ≤ i ≤ k, and that k ≤ 12 log loglogP P . Then


![image 67](<2013-naslund-improving-roth-theorem-primes_images/imageFile67.png>)

3kk! logk P p

|{n ≤ P : b1 + nW, . . ., bk + nW all prime}| ≪ P

![image 68](<2013-naslund-improving-roth-theorem-primes_images/imageFile68.png>)

ρ(p) p

1 −

![image 69](<2013-naslund-improving-roth-theorem-primes_images/imageFile69.png>)

1 p

1 −

![image 70](<2013-naslund-improving-roth-theorem-primes_images/imageFile70.png>)

−k

,

where the constant does not depend on k. Proof. In Theorem 3, let qi = W, li = bi, M = P, v = P1/3, and so that u0 ≤ 2bW. To apply Klimov’s theorem, we must have v ≤

√

![image 71](<2013-naslund-improving-roth-theorem-primes_images/imageFile71.png>)

log2k(P), and u0 = O exp logB v . The

P

![image 72](<2013-naslund-improving-roth-theorem-primes_images/imageFile72.png>)

ﬁrst condition follows from the assumption that k ≤ 121 log loglogPP . The upper bound from u0 is satisﬁed with B = 15 since log(2bW) ≤ 5 log P ≤ 15 log v by the hypothesis of the lemma. It follows that

![image 73](<2013-naslund-improving-roth-theorem-primes_images/imageFile73.png>)

![image 74](<2013-naslund-improving-roth-theorem-primes_images/imageFile74.png>)

log log u0 log v

log log N log N

,

= O

![image 75](<2013-naslund-improving-roth-theorem-primes_images/imageFile75.png>)

![image 76](<2013-naslund-improving-roth-theorem-primes_images/imageFile76.png>)

and so

−k

3kk! logk P p

ρ(p) p

1 p

1 −

1 −

, as desired.

Mv (W, bi) ≪ P

![image 77](<2013-naslund-improving-roth-theorem-primes_images/imageFile77.png>)

![image 78](<2013-naslund-improving-roth-theorem-primes_images/imageFile78.png>)

![image 79](<2013-naslund-improving-roth-theorem-primes_images/imageFile79.png>)

We note that if k > 12 log loglogP P , the term log3kk!

kP will be large than 1, and so the bound is weaker than the trivial upper of P. Using this lemma, we prove proposition 2. Proof. By the deﬁnition of the L2k norm and the convolution, we have that

![image 80](<2013-naslund-improving-roth-theorem-primes_images/imageFile80.png>)

![image 81](<2013-naslund-improving-roth-theorem-primes_images/imageFile81.png>)

a ∗ σ 22kk = Ex| (a ∗ σ) (x)|2k = Ex |Eyσ(y)a(x − y)|2k . Expanding the sum, a ∗ σ 22kk is bounded above by

Ey

1,...,y2k|σ(y1)| · · ·|σ(y2k)|Exa(x − y1) · · ·a(x − y2k).

Since a is supported on 0, P3 , and σ is supported on −P3 , P3 , there can be no wrap around inside Z/PZ, and we have the upper bound

![image 82](<2013-naslund-improving-roth-theorem-primes_images/imageFile82.png>)

![image 83](<2013-naslund-improving-roth-theorem-primes_images/imageFile83.png>)

![image 84](<2013-naslund-improving-roth-theorem-primes_images/imageFile84.png>)

- (2.5) Exa(x − y1) · · ·a(x − y2k) ≤

1 P

![image 85](<2013-naslund-improving-roth-theorem-primes_images/imageFile85.png>)

log N log z

![image 86](<2013-naslund-improving-roth-theorem-primes_images/imageFile86.png>)

2k

|A (y1, y2, . . ., y2k)| where

A (y1, y2, . . ., y2k) = {n ≤ P : b + (n − y1)W, . . ., b + (n − y2k) W all prime} . The size of this set of primes is bounded above by the number of n ≤ P such that

- b + (n − y1) W is prime, and so by the Brun-Titchmarsh inequality


|A (y1, y2, . . ., y2k)| ≤

2PW φ(W) log(P/W)

![image 87](<2013-naslund-improving-roth-theorem-primes_images/imageFile87.png>)

,

which we combine with the inequalities P/W ≥ N1/3 and φ(WW) ≤ 2 log z to obtain

![image 88](<2013-naslund-improving-roth-theorem-primes_images/imageFile88.png>)

- (2.6) |A (y1, y2, . . ., y2k)| ≤

12P log z log N

![image 89](<2013-naslund-improving-roth-theorem-primes_images/imageFile89.png>)

.

However we will need our sieving lemma in the case where each of the yi is distinct. Let

Il = (y1, . . ., y2k) : yi ≤

P 2

![image 90](<2013-naslund-improving-roth-theorem-primes_images/imageFile90.png>)

, with l or less distinct coordinates yi ,

Jl = (y1, . . ., y2k) : yi ≤

P 2

![image 91](<2013-naslund-improving-roth-theorem-primes_images/imageFile91.png>)

, with exactly l distinct coordinates yi ,

so that we may bound our quantity from above by a sum from r = 1 to 2k, and over (y1, . . ., y2k) ∈ Ir or Jr. We split this into two cases. When r < 2k, we will bound above by the sum over Ir, and when r = 2k, we will use a sum over elements in the set J2k. For r < 2k, we are looking at

- (2.7)


2k−1

1 P2k+1

|σ(y1)| · · ·|σ(y2k)|

![image 92](<2013-naslund-improving-roth-theorem-primes_images/imageFile92.png>)

r=1 (y1,...,y2k)∈Ir

x

a(x − y1) · · ·a(x − y2k)

which by (2.5) and (2.6) is

≪

log N log z

![image 93](<2013-naslund-improving-roth-theorem-primes_images/imageFile93.png>)

2k−1 2k−1

1 P2k

r=1

|σ(y1)| · · ·|σ(y2k)|.

![image 94](<2013-naslund-improving-roth-theorem-primes_images/imageFile94.png>)

(y1,...,y2k)∈Ir

Each term in the sum over r on the right hand side may be bounded above by 1/|Σ|2k−r since

1 P2k

1 |Σ|2k−r (Ey

|σ(y1)| · · ·|σ(y2k)| =

1,...,yrσ (y1) · · ·σ (yr))

![image 95](<2013-naslund-improving-roth-theorem-primes_images/imageFile95.png>)

![image 96](<2013-naslund-improving-roth-theorem-primes_images/imageFile96.png>)

(y1,...,y2k)∈Ir

1 |Σ|2k−r. If |Σ| = 1, the lemma is trivial, and if |Σ| ≥ 2 we have

=

![image 97](<2013-naslund-improving-roth-theorem-primes_images/imageFile97.png>)

2k−1

1 |Σ| − 1

1 |Σ|2k−r ≤

≤

![image 98](<2013-naslund-improving-roth-theorem-primes_images/imageFile98.png>)

![image 99](<2013-naslund-improving-roth-theorem-primes_images/imageFile99.png>)

r=1

2 |Σ|

,

![image 100](<2013-naslund-improving-roth-theorem-primes_images/imageFile100.png>)

which implies that the quantity in (2.7) is

≪

log N log z

![image 101](<2013-naslund-improving-roth-theorem-primes_images/imageFile101.png>)

2k−1 2 |Σ|

.

![image 102](<2013-naslund-improving-roth-theorem-primes_images/imageFile102.png>)

To bound the cardinality of A (y1, . . ., y2k) for (y1, . . ., y2k) ∈ J2k, we apply Lemma 4. The conditions of the lemma are satisﬁed as b, W ≤ N1/3 and k ≤ 12 log loglogP P since k ≤ 12 log1/3 z. Thus for any 2k-tuple (y1, . . ., y2k) ∈ J2k,

![image 103](<2013-naslund-improving-roth-theorem-primes_images/imageFile103.png>)

![image 104](<2013-naslund-improving-roth-theorem-primes_images/imageFile104.png>)

32k(2k)!P (log P)2k p

- (2.8) |A (y1, y2, . . ., y2k)| ≪


![image 105](<2013-naslund-improving-roth-theorem-primes_images/imageFile105.png>)

ρ(p) p

1 −

![image 106](<2013-naslund-improving-roth-theorem-primes_images/imageFile106.png>)

1 p

1 −

![image 107](<2013-naslund-improving-roth-theorem-primes_images/imageFile107.png>)

−2k

.

On the right hand side of equation (2.8) ρ is deﬁned so that ρ(p) = 0 if p ≤ z, ρ(p) = 2k if p > z and p ∤ (yi − yj) for all i = j. The product over all p > z where ρ(p) = 2k is extremely well behaved, and we have that

p>z

2k p

1 −

![image 108](<2013-naslund-improving-roth-theorem-primes_images/imageFile108.png>)

1 p

1 −

![image 109](<2013-naslund-improving-roth-theorem-primes_images/imageFile109.png>)

−2k

is bounded from above and below by absolute constants. To see why, notice that

log

p>z

2k p

1 −

![image 110](<2013-naslund-improving-roth-theorem-primes_images/imageFile110.png>)

1 p

1 −

![image 111](<2013-naslund-improving-roth-theorem-primes_images/imageFile111.png>)

−2k

∞

1 j

= 2k

![image 112](<2013-naslund-improving-roth-theorem-primes_images/imageFile112.png>)

p>z

j=1

1 p

![image 113](<2013-naslund-improving-roth-theorem-primes_images/imageFile113.png>)

∞

j

1 j

−

![image 114](<2013-naslund-improving-roth-theorem-primes_images/imageFile114.png>)

p>z

j=1

=

∞

1 j

![image 115](<2013-naslund-improving-roth-theorem-primes_images/imageFile115.png>)

p>z

j=2

2k

1 p

![image 116](<2013-naslund-improving-roth-theorem-primes_images/imageFile116.png>)

j

−

2k p

![image 117](<2013-naslund-improving-roth-theorem-primes_images/imageFile117.png>)

j

2k p

![image 118](<2013-naslund-improving-roth-theorem-primes_images/imageFile118.png>)

j

,

and as k ≤ 21 log z, we have the lower bound

![image 119](<2013-naslund-improving-roth-theorem-primes_images/imageFile119.png>)

∞

∞

j

j

1 j

1 p

2k p

1 j

1 pj

(log z)j

2k

≥ −

−

![image 120](<2013-naslund-improving-roth-theorem-primes_images/imageFile120.png>)

![image 121](<2013-naslund-improving-roth-theorem-primes_images/imageFile121.png>)

![image 122](<2013-naslund-improving-roth-theorem-primes_images/imageFile122.png>)

![image 123](<2013-naslund-improving-roth-theorem-primes_images/imageFile123.png>)

![image 124](<2013-naslund-improving-roth-theorem-primes_images/imageFile124.png>)

p>z

p>z

j=2

j=2

∞

1 nj

1 j

(log z)j

≥ −

![image 125](<2013-naslund-improving-roth-theorem-primes_images/imageFile125.png>)

![image 126](<2013-naslund-improving-roth-theorem-primes_images/imageFile126.png>)

n>z

j=2

log2 z z

≫ −

, and similarly we have the upper bound

![image 127](<2013-naslund-improving-roth-theorem-primes_images/imageFile127.png>)

∞

1 j

![image 128](<2013-naslund-improving-roth-theorem-primes_images/imageFile128.png>)

j=2

p>z

2k

1 p

![image 129](<2013-naslund-improving-roth-theorem-primes_images/imageFile129.png>)

j

−

2k p

![image 130](<2013-naslund-improving-roth-theorem-primes_images/imageFile130.png>)

j

≤ 0

j

j

as 2k p 1

≤ 2pk

for all j. From these bounds, it follows that for a constant independent of k,

![image 131](<2013-naslund-improving-roth-theorem-primes_images/imageFile131.png>)

![image 132](<2013-naslund-improving-roth-theorem-primes_images/imageFile132.png>)

p

ρ(p) p

1 −

![image 133](<2013-naslund-improving-roth-theorem-primes_images/imageFile133.png>)

1 p

1 −

![image 134](<2013-naslund-improving-roth-theorem-primes_images/imageFile134.png>)

−2k

≪ (log z)2k

p > z p|yi − yj

ρ(p) p

1 −

![image 135](<2013-naslund-improving-roth-theorem-primes_images/imageFile135.png>)

1 p

1 −

![image 136](<2013-naslund-improving-roth-theorem-primes_images/imageFile136.png>)

−2k

.

Since |yi − yj| ≤ P, and any integer y ≤ P can have at most logz P prime factors greater than z, we see that there are at most (2k)2 loglogPz primes greater than z which could divide some diﬀerence yi − yj. For each p that divides yi − yj for some i, j, the worst case is whenρ(p) = 1, and we may assume that this is the case to obtain an upper

![image 137](<2013-naslund-improving-roth-theorem-primes_images/imageFile137.png>)

−1

bound. As 1 − p1

≤ z−z1 for p > z, we have

![image 138](<2013-naslund-improving-roth-theorem-primes_images/imageFile138.png>)

![image 139](<2013-naslund-improving-roth-theorem-primes_images/imageFile139.png>)

p > z p|yi − yj

ρ(p) p

1 −

![image 140](<2013-naslund-improving-roth-theorem-primes_images/imageFile140.png>)

1 p

1 −

![image 141](<2013-naslund-improving-roth-theorem-primes_images/imageFile141.png>)

−2k

≤

z z − 1

![image 142](<2013-naslund-improving-roth-theorem-primes_images/imageFile142.png>)

(4k2)(2k−1)loglogPz

![image 143](<2013-naslund-improving-roth-theorem-primes_images/imageFile143.png>)

.

Recall that log P ≤ log N ≤ 4z since z = 14 log N. The exponent is bounded above by 4k2 (2k − 1)

![image 144](<2013-naslund-improving-roth-theorem-primes_images/imageFile144.png>)

log P log z

log P log z

≤ 8k3

![image 145](<2013-naslund-improving-roth-theorem-primes_images/imageFile145.png>)

![image 146](<2013-naslund-improving-roth-theorem-primes_images/imageFile146.png>)

32k3 log z

z ≤ 4z,

≤

![image 147](<2013-naslund-improving-roth-theorem-primes_images/imageFile147.png>)

1

where the ﬁnal inequality follows from the assumption that k ≤ 21 (log z)

3. Since z z − 1

![image 148](<2013-naslund-improving-roth-theorem-primes_images/imageFile148.png>)

![image 149](<2013-naslund-improving-roth-theorem-primes_images/imageFile149.png>)

4z

≤ 5e4

![image 150](<2013-naslund-improving-roth-theorem-primes_images/imageFile150.png>)

for z ≥ 2, we obtain the inequality

p > z p|yi − yj

ρ(p) p

1 −

![image 151](<2013-naslund-improving-roth-theorem-primes_images/imageFile151.png>)

1 p

1 −

![image 152](<2013-naslund-improving-roth-theorem-primes_images/imageFile152.png>)

−2k

≤ 5e4,

and so equation (2.8) becomes

(log z)2k (log P)2k

|A (y1, y2, . . ., y2k)| ≤ C32k(2k)!P

,

![image 153](<2013-naslund-improving-roth-theorem-primes_images/imageFile153.png>)

for an absolute constant C. Thus, for any (y1, . . ., y2k) ∈ J2k,

Exa(x − y1) · · ·a(x − y2k) ≤ C32k(2k)!. Since

1 P2k

|σ(y1)| · · ·|σ(y2k)| ≤ Ey

1,...,y2k|σ(y1)| · · ·|σ(y2k)| = 1,

![image 154](<2013-naslund-improving-roth-theorem-primes_images/imageFile154.png>)

(y1,...,y2k)∈J2k

the sum over all the 2k-tuples in J2k is ≤ 1. Combining the work done so far, we have proven that

2k−1

2k |Σ|

log N log z

a ∗ σ 22kk ≪ 32k(2k)! +

.

![image 155](<2013-naslund-improving-roth-theorem-primes_images/imageFile155.png>)

![image 156](<2013-naslund-improving-roth-theorem-primes_images/imageFile156.png>)

- 1

![image 157](<2013-naslund-improving-roth-theorem-primes_images/imageFile157.png>)

- 2k ≤ n


- 1

![image 158](<2013-naslund-improving-roth-theorem-primes_images/imageFile158.png>)

- 2k for n, m, k ≥ 1,


- 1

![image 159](<2013-naslund-improving-roth-theorem-primes_images/imageFile159.png>)

- 2k +m


The stated result then follows from the fact that (n + m) and since

- 1

![image 160](<2013-naslund-improving-roth-theorem-primes_images/imageFile160.png>)

- 2k


- 1

![image 161](<2013-naslund-improving-roth-theorem-primes_images/imageFile161.png>)

- 2k ≤ e


3

32k(2k)!

≤ 4k, and (3k)

2e ≤ 2.

![image 162](<2013-naslund-improving-roth-theorem-primes_images/imageFile162.png>)

3. Main Theorem Let a, N, W, P and z be deﬁned as in section 2. Following [8], we deﬁne

R = Specδ (a) ∪ {1} = {x ∈ Z/PZ : | a(x)| ≥ δ} ∪ {1}, and

nx P

B = B (R, ǫ) = n ∈ Z/PZ : ∀x ∈ R,

≤ ǫ ,

![image 163](<2013-naslund-improving-roth-theorem-primes_images/imageFile163.png>)

where x denotes the distance from x to the nearest integer. The set B is called a Bohr set with radius ǫ and frequency set R. Set σ = µ(1B)1B to be the normalized indicator function of the Bohr set B. By including the element 1 in the set R, it follows that σ will be supported on −P4 , P4 inside Z/PZ when ǫ < 41. Let h = a ∗ σ be our prime indicator smoothed out by the Bohr set B. Notice that

![image 164](<2013-naslund-improving-roth-theorem-primes_images/imageFile164.png>)

![image 165](<2013-naslund-improving-roth-theorem-primes_images/imageFile165.png>)

![image 166](<2013-naslund-improving-roth-theorem-primes_images/imageFile166.png>)

![image 167](<2013-naslund-improving-roth-theorem-primes_images/imageFile167.png>)

1 µ(B)

Ex∈Z/PZ1B = 1, and

σ 1 =

![image 168](<2013-naslund-improving-roth-theorem-primes_images/imageFile168.png>)

1B(y) µ(B)

h 1 = Ex∈Z/PZEy∈Z/PZ

a(x − y)

![image 169](<2013-naslund-improving-roth-theorem-primes_images/imageFile169.png>)

= σ 1 a 1,

so that by (2.4), which gave the bound a 1 ≥ 10α , we have

![image 170](<2013-naslund-improving-roth-theorem-primes_images/imageFile170.png>)

- (3.1) h1 ≥

α 10

![image 171](<2013-naslund-improving-roth-theorem-primes_images/imageFile171.png>)

.

Our goal is to show that there is little diﬀerence between the three term arithmetic progression operator applied to a and h, and then prove that Λ(h, h, h) is large. Let

∆ = |Λ (a, a, a) − Λ (h, h, h)|

where Λ is the three term arithmetic progression operator. In Helfgott and De Roton’s paper [8], equation (2.6) on page 7 states that

Lemma 5. For the above deﬁnition of ∆, ǫ, δ we have ∆ ≪ ǫ + δ3/5.

The proof of this lemma makes use of Green and Tao’s results on the restriction theory of the Selberg sieve [5]. Applying proposition 2 with σ = a, we ﬁnd that

a ∗ a 2 ≪ 1,

and so a ˆ 4 ≪ 1 since a ∗ a 22 = a ˆ 44 by (1.6) and (1.5). This yields the bound |R| ≤ C4δ−4, on the size of the dimension of the Bohr set B, for an absolute constant C4, as

|R|δ4 ≤

t

|aˆ(t)|4 ≤ C4, A well known pigeon hole argument tells us that |B (R, ǫ) | ≥ Nǫ|R|, and so

log |B| ≥ log N − |R|| logǫ| ≥ log N − C4δ−4| log ǫ|. We note that an equation nearly identical to the above appears on page 9 of [8]. We chose to deduce it again since the bound on a ˆ 4 was obtained in a diﬀerent way. From now on, we will assume that ǫ, δ satisfy

- (3.2) C4δ−4| log ǫ| ≤


- 1

![image 172](<2013-naslund-improving-roth-theorem-primes_images/imageFile172.png>)

- 2


log N, so that

- 1

![image 173](<2013-naslund-improving-roth-theorem-primes_images/imageFile173.png>)

- 2.


|B| ≥ N For k ≤ 12 (log z)

1

3, proposition 2 allows us to bound the ℓ2k norm of h. Using the inequality

![image 174](<2013-naslund-improving-roth-theorem-primes_images/imageFile174.png>)

![image 175](<2013-naslund-improving-roth-theorem-primes_images/imageFile175.png>)

- 1

![image 176](<2013-naslund-improving-roth-theorem-primes_images/imageFile176.png>)

- 2


4

3 , which holds for all N ≥ 2, along with the fact that

log N ≥ (log log N)

![image 177](<2013-naslund-improving-roth-theorem-primes_images/imageFile177.png>)

- 1

![image 178](<2013-naslund-improving-roth-theorem-primes_images/imageFile178.png>)

- 2


- 1

![image 179](<2013-naslund-improving-roth-theorem-primes_images/imageFile179.png>)

- 2


1

1

k ≤

3 , we see that

3 ≤

(log z)

(log log N)

![image 180](<2013-naslund-improving-roth-theorem-primes_images/imageFile180.png>)

![image 181](<2013-naslund-improving-roth-theorem-primes_images/imageFile181.png>)

2k

log N log z

- 1

![image 182](<2013-naslund-improving-roth-theorem-primes_images/imageFile182.png>)

- 2 ≥ (log N)2k ≥


N

,

![image 183](<2013-naslund-improving-roth-theorem-primes_images/imageFile183.png>)

and consequently

2k

log N log z

- 1

![image 184](<2013-naslund-improving-roth-theorem-primes_images/imageFile184.png>)

- 2 ≥


|B| ≥ N

. Proposition 2 then implies that

![image 185](<2013-naslund-improving-roth-theorem-primes_images/imageFile185.png>)

- (3.3) h 2k = a ∗ σ 2k ≪ k.

Using this bound L2k norm of h = a ∗σ, along with Sanders bound on Roth’s theorem, we are able to show that Λ(h, h, h) must be large.

Proposition 6. There exists positive constants c1, N0 > 0 such that if N ≥ N0, for any 1 ≤ k ≤ 12 (log z)

![image 186](<2013-naslund-improving-roth-theorem-primes_images/imageFile186.png>)

1

![image 187](<2013-naslund-improving-roth-theorem-primes_images/imageFile187.png>)

3 we have

Λ (h, h, h) ≫ exp −c1

α k

![image 188](<2013-naslund-improving-roth-theorem-primes_images/imageFile188.png>)

−q2k

log

1 α

![image 189](<2013-naslund-improving-roth-theorem-primes_images/imageFile189.png>)

5

where q2k = 1 − 21k −1 .

![image 190](<2013-naslund-improving-roth-theorem-primes_images/imageFile190.png>)

To prove this proposition, we will make use of the following lemma which allows us to ﬁnd a large subset where the function h is bounded below uniformly.

Lemma 7. Let q, p > 1 be such that 1q + 1p = 1, and let f : Z/PZ → R+ be a function with f 1 ≥ α, and f p ≤ C for some C. Then there exists a subset L ⊂ Z/PZ such for all n ∈ L f(n) ≥ α2, and

![image 191](<2013-naslund-improving-roth-theorem-primes_images/imageFile191.png>)

![image 192](<2013-naslund-improving-roth-theorem-primes_images/imageFile192.png>)

![image 193](<2013-naslund-improving-roth-theorem-primes_images/imageFile193.png>)

α 2C

![image 194](<2013-naslund-improving-roth-theorem-primes_images/imageFile194.png>)

q

≤ µ(L).

Proof. Deﬁne L = n : f(n) ≥ α2 , so that L is the largest possible set satisfying the ﬁrst condition. Then, if 1L(n) is the indicator function for L we have that

![image 195](<2013-naslund-improving-roth-theorem-primes_images/imageFile195.png>)

α ≤ En∈Z/PZf(n) ≤

α 2

![image 196](<2013-naslund-improving-roth-theorem-primes_images/imageFile196.png>)

+ En∈Z/PZf(n)1L(n). Applying Hölder’s inequality yields

En∈Z/PZf(n)1L(n) ≤ 1L q f p ≤ C (µ(L))

1 q

![image 197](<2013-naslund-improving-roth-theorem-primes_images/imageFile197.png>)

by our assumption that f p ≤ C. The lemma then follows from the resulting inequality

α

![image 198](<2013-naslund-improving-roth-theorem-primes_images/imageFile198.png>)

2 ≤ C (µ(L))1/q .

Sanders improvement to Roth’s theorem [11] states that if Ξ ⊂ [1, N] with density ξ, then

- (3.4) Λ (1Ξ, 1Ξ, 1Ξ) ≫ exp −cξ−1 log


1 ξ

![image 199](<2013-naslund-improving-roth-theorem-primes_images/imageFile199.png>)

5

.

Using this result along with (3.3) and lemma 7, we are ready to ﬁnish the proof of proposition 6.

Proof. By equation (3.3), it follows that h 2k ≪ k. Applying lemma 7 to the function h, we obtain a subset L ⊂ Z/PZ with

α k

q2k

, and h(n) ≥ 20α for all n ∈ L, where q1

µ (L) ≫

![image 200](<2013-naslund-improving-roth-theorem-primes_images/imageFile200.png>)

= 1 − 21k. Restricting h to this subset L, we obtain the lower bound

![image 201](<2013-naslund-improving-roth-theorem-primes_images/imageFile201.png>)

![image 202](<2013-naslund-improving-roth-theorem-primes_images/imageFile202.png>)

![image 203](<2013-naslund-improving-roth-theorem-primes_images/imageFile203.png>)

2k

- (3.5) Λ (h, h, h) ≥

α3 203

![image 204](<2013-naslund-improving-roth-theorem-primes_images/imageFile204.png>)

Λ (1L, 1L, 1L) . Applying the bound in (3.4) to our set L, we have that

Λ (1L, 1L, 1L) ≫ exp −c

α k

![image 205](<2013-naslund-improving-roth-theorem-primes_images/imageFile205.png>)

−q2k

log

1 α

![image 206](<2013-naslund-improving-roth-theorem-primes_images/imageFile206.png>)

5

for some constant c, since the density of L is ≫ αk q2k. By equation (3.5) it follows that there is a constant c1 such that

![image 207](<2013-naslund-improving-roth-theorem-primes_images/imageFile207.png>)

Λ (h, h, h) ≫ exp −c1

α k

![image 208](<2013-naslund-improving-roth-theorem-primes_images/imageFile208.png>)

−q2k

log

1 α

![image 209](<2013-naslund-improving-roth-theorem-primes_images/imageFile209.png>)

5

, as desired.

Lemma 5 tells us that

|Λ(h, h, h) − Λ(a, a, a)| ≪ ǫ + δ

3

![image 210](<2013-naslund-improving-roth-theorem-primes_images/imageFile210.png>)

5,

and Proposition 6 implies that Λ(h, h, h) must be very large. Recalling equation (3.2), the requirement that ǫ, δ satisfy C4δ−4| log ǫ| ≤ 12 log N, we are ready to put everything together and give a precise lower bound for the size of Λ(a, a, a). We now prove Theorem 1.

![image 211](<2013-naslund-improving-roth-theorem-primes_images/imageFile211.png>)

Proof. Suppose that A ⊂ P contains no nontrivial arithmetic progressions. Then A0 contains only the trivial 3 term arithmetic progressions, and we have that the three term arithmetic progression operator is bounded above by

- (3.6) Λ (a, a, a) ≪

1 P

![image 212](<2013-naslund-improving-roth-theorem-primes_images/imageFile212.png>)

log N log z

![image 213](<2013-naslund-improving-roth-theorem-primes_images/imageFile213.png>)

2

. By equation (3.6), lemma 5 and proposition 6 , we must have

- (3.7)


2

log N log z

1 P

3

+ ǫ + δ

5 ≫ exp −c1

![image 214](<2013-naslund-improving-roth-theorem-primes_images/imageFile214.png>)

![image 215](<2013-naslund-improving-roth-theorem-primes_images/imageFile215.png>)

![image 216](<2013-naslund-improving-roth-theorem-primes_images/imageFile216.png>)

α k

![image 217](<2013-naslund-improving-roth-theorem-primes_images/imageFile217.png>)

−q2k

1 α

log

![image 218](<2013-naslund-improving-roth-theorem-primes_images/imageFile218.png>)

5

.

2

In the above, for N suﬃciently large, the term P1 loglogNz

will be negligible compared

![image 219](<2013-naslund-improving-roth-theorem-primes_images/imageFile219.png>)

![image 220](<2013-naslund-improving-roth-theorem-primes_images/imageFile220.png>)

to the right hand side as we assumed that α > (log N)−1/4. Choosing ǫ and δ small enough will lead us to a contradiction. In particular, there exists a ﬁxed postie constant η > 0, independent of N and k, such that choosing

3

5 = η exp −c1

ǫ = δ

![image 221](<2013-naslund-improving-roth-theorem-primes_images/imageFile221.png>)

α k

![image 222](<2013-naslund-improving-roth-theorem-primes_images/imageFile222.png>)

−q2k

1 α

log

![image 223](<2013-naslund-improving-roth-theorem-primes_images/imageFile223.png>)

5

,

makes inequality (3.7) impossible. These values of ǫ, δ satisfy the necessary constraint C4 |log ǫ|δ−4 ≤ 21 log N as long as

![image 224](<2013-naslund-improving-roth-theorem-primes_images/imageFile224.png>)

- (3.8) exp c2


α k

![image 225](<2013-naslund-improving-roth-theorem-primes_images/imageFile225.png>)

−q2k

1 α

log

![image 226](<2013-naslund-improving-roth-theorem-primes_images/imageFile226.png>)

5

- 1

![image 227](<2013-naslund-improving-roth-theorem-primes_images/imageFile227.png>)

- 2


≪

log N

for some new constant c2, where the ≪ has consumed η. When

1 q2k

α ≥ k (2c2)

![image 228](<2013-naslund-improving-roth-theorem-primes_images/imageFile228.png>)

5 q2k

(log log log N)

![image 229](<2013-naslund-improving-roth-theorem-primes_images/imageFile229.png>)

,

![image 230](<2013-naslund-improving-roth-theorem-primes_images/imageFile230.png>)

1 q2k

(log log N)

![image 231](<2013-naslund-improving-roth-theorem-primes_images/imageFile231.png>)

we have that

exp c2

α k

![image 232](<2013-naslund-improving-roth-theorem-primes_images/imageFile232.png>)

−q2k

1 α

log

![image 233](<2013-naslund-improving-roth-theorem-primes_images/imageFile233.png>)

5

![image 234](<2013-naslund-improving-roth-theorem-primes_images/imageFile234.png>)

≤ log N,

and so inequality (3.8) holds for suﬃciently large N. Letting 2k = [log log log N], which satisﬁes the necessary bound k ≤ 21 (log z)

1

3, we have that log log N log log log N

![image 235](<2013-naslund-improving-roth-theorem-primes_images/imageFile235.png>)

![image 236](<2013-naslund-improving-roth-theorem-primes_images/imageFile236.png>)

1 2k

![image 237](<2013-naslund-improving-roth-theorem-primes_images/imageFile237.png>)

∼ e,

![image 238](<2013-naslund-improving-roth-theorem-primes_images/imageFile238.png>)

and so

1 q2k

k (2c2)

![image 239](<2013-naslund-improving-roth-theorem-primes_images/imageFile239.png>)

5 q2k

(log log log N)

![image 240](<2013-naslund-improving-roth-theorem-primes_images/imageFile240.png>)

![image 241](<2013-naslund-improving-roth-theorem-primes_images/imageFile241.png>)

1 q2k

(log log N)

![image 242](<2013-naslund-improving-roth-theorem-primes_images/imageFile242.png>)

(log log log N)6 log log N

,

≥ C

![image 243](<2013-naslund-improving-roth-theorem-primes_images/imageFile243.png>)

for some constant C. This means that we will have a contradiction when N is suﬃciently large and the density α satisﬁes

(log log log N)6 log log N

α ≥ C

![image 244](<2013-naslund-improving-roth-theorem-primes_images/imageFile244.png>)

for some absolute constant C, which proves the desired result.

Remark 8. The proof suggests that we might need the condition N ≥ N0 for some ﬁxed constant N0 in the main theorem. Note however that this is not necessary given how the result is phrased, as the constant in the ≪ will be so large that it accounts for this.

Acknowledgments

I am very grateful to Julia Wolf for her support, encouragement, and generous help. I am especially thankful for her patience during our conversations on the Selberg sieve. I would like to thank Greg Martin for his helpful comments, and Daniel Fiorilli for leading me to the paper of Klimov, as well as the anonymous referee for his many useful suggestions.

References

- [1] J. Bourgain. On triples in arithmetic progression. Geom. Funct. Anal., 9(5):968–984, 1999.
- [2] Jean Bourgain. Roth’s theorem on progressions revisited. J. Anal. Math., 104:155–192, 2008.
- [3] Paul Erdös and Paul Turán. On Some Sequences of Integers. J. London Math. Soc., S1-11(4):261.
- [4] Ben Green. Roth’s theorem in the primes. Ann. of Math. (2), 161(3):1609–1636, 2005.
- [5] Ben Green and Terence Tao. Restriction theory of the Selberg sieve, with applications. J. Théor. Nombres Bordeaux, 18(1):147–182, 2006.
- [6] H. Halberstam and H.-E. Richert. Sieve methods. Academic Press [A subsidiary of Harcourt Brace Jovanovich, Publishers], London-New York, 1974. London Mathematical Society Monographs, No. 4.
- [7] D. R. Heath-Brown. Integer sets containing no arithmetic progressions. J. London Math. Soc. (2), 35(3):385–394, 1987.
- [8] Harald Andrés Helfgott and Anne de Roton. Improving Roth’s theorem in the primes. Int. Math. Res. Not. IMRN, (4):767–783, 2011.
- [9] N. I. Klimov. Combination of elementary and analytic methods in the theory of numbers. Uspehi Mat. Nauk (N.S.), 13(3 (81)):145–164, 1958.
- [10] K. F. Roth. On certain sets of integers. J. London Math. Soc., 28:104–109, 1953.
- [11] Tom Sanders. On Roth’s theorem on progressions. Ann. of Math. (2), 174(1):619–636, 2011.
- [12] E. Szemerédi. Integer sets containing no arithmetic progressions. Acta Math. Hungar., 56(1-2):155– 158, 1990.
- [13] J. G. van der Corput. Über Summen von Primzahlen und Primzahlquadraten. Math. Ann., 116(1):1–50, 1939.


Princeton University Mathematics Department, Fine Hall Room 304, Princeton NJ 08544-1044

E-mail address: naslund@math.princeton.edu

