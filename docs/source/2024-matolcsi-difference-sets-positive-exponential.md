---
type: source
kind: paper
title: "Difference sets and positive exponential sums II: cubic residues in cyclic groups"
authors: Mate Matolcsi, Imre Z. Ruzsa
year: 2024
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2406.00406v2
source_local: ../raw/2024-matolcsi-difference-sets-positive-exponential.pdf
topic: general-knowledge
cites:
---

arXiv:2406.00406v2[math.NT]22Apr2025

DIFFERENCE SETS AND POSITIVE EXPONENTIAL SUMS II: CUBIC RESIDUES IN CYCLIC GROUPS

MAT´ E´ MATOLCSI AND IMRE Z. RUZSA

Abstract. By constructing suitable nonnegative exponential sums we give upper bounds on the cardinality of any set Bq in cyclic groups Zq such that the diﬀerence set Bq − Bq avoids cubic residues modulo q.

1. Introduction

This paper is a follow-up to [3], where we described the general properties connecting positive exponential sums and diﬀerence sets. In this second part, we apply the techniques of [3] to investigate the intersective properties of cubic residues in cyclic groups Zq. That is, by constructing suitable nonnegative exponential sums we obtain upper bounds on the cardinality of any set Bq ⊂ Zq such that the diﬀerence set Bq −Bq avoids cubic residues modulo q. We will turn to the case of quadratic residues in a later publication, but let us mention here that Gabdullin [2] has recently achieved a non-trivial upper bound by a diﬀerent method.

The ultimate aim of this research is to extend these results to the case of integers, i.e. give a strong upper bound on the cardinality of a set B ⊂ {0, 1, . . ., N} such that B − B does not contain any cubes or, more generally, kth powers for some ﬁxed k.

In order to see the relation of the modular case to the integer case we introduce the following notions.

We use the standard notation e(x) = e2πix throughout the paper.

- Deﬁnition 1.1. A nonnegative function


- (1) f(n)(x) = a0 +

n−1

j=1

aj(e(jkx) + e(−jkx)) ≥ 0, x ∈ [0, 1], f(n)(0) = 1,

is called a kth power witness function of order n. Similarly, a nonnegative function

- (2) g(q)(y) = b0 +


q−1

j=1,q∤jk

bj(e(jky/q)+e(−jky/q)) ≥ 0, y = 0, 1, . . ., q −1, g(q)(0) = 1,

is called a kth power modular witness function, modulo q. (The dependence of aj on n, and bj on q will usually be suppressed in the notation.)

![image 1](<2024-matolcsi-difference-sets-positive-exponential_images/imageFile1.png>)

M. Matolcsi was supported by the NKFIH grant no. K132097 and K129335, I Z. Ruzsa was supported by NKFIH grant no. K129335.

1

The normalization f(n)(0) = g(q)(0) = 1 is only for convenience, and will be used throughout this note. We remark that the coeﬃcients aj are automatically real as they are the Fourier (cosine) coeﬃcients of the real valued function f(n). Also, we can assume without loss of generality (after averaging over j if necessary) that bj = bj′ whenever jk ≡ ±j′k mod q. This makes the coeﬃcients bj real (because g(q) is a real valued, even function, and bj are basically its Fourier coeﬃcients, so they must be conjugate symmetric bj = b−j, and they are also symmetric bj = b−j by the assumption above, so they are in fact real).

![image 2](<2024-matolcsi-difference-sets-positive-exponential_images/imageFile2.png>)

Let us clarify here the connection of these deﬁnitions to the results of [3]. Consider the cyclic group G = Zq of order q, and let R0(k) denote the set of kth power residues mod q (including 0). Let Rs(k) denote the symmetrized set Rs(k) = R0(k) ∪ −R0(k). We can think of the coeﬃcients bj as a function h : G → R, supported on Rs(k), deﬁned in the following way: for any r ∈ Rs(k) let h(r) = j3≡±r bj. The Fourier transform of h is then hˆ = g(q) ≥ 0. Therefore, the function h ﬁts into the class of functions used in the deﬁnition of λ(Rs(k)) in [3].

We will restrict our attention to the case k = 3 in this paper, the treatment of other odd values of k being similar. We will use the following notations in accordance with the ones introduced in [3].

- Deﬁnition 1.2. Let C(q) denote the set of non-zero cubic residues modulo q, and let C0(q) = C(q) ∪{0}. Recall from [3] that δ(C0(q)) denotes the maximal density (i.e. |Bq|/q)


of a set Bq ⊂ Zq such that (Bq − Bq) ∩ C(q) = ∅. Also, λ(C0(q)) denotes the minimal possible value of the constant term b0 in expression (2) for k = 3.

In this note we will be interested in upper bounds on δ(C0(q)), but let us also mention here what is known about lower bounds. For a prime q = 3k + 1, it is clear by the Ramsey number estimate R(s, s) ≤ 4s that one can ﬁnd a set B ⊂ Zq of size at least ⌊log4 q⌋ such that (Bq − Bq) ∩ C(q) = ∅. (After applying the Ramsey estimate, one can either ﬁnd a suitable set B, or a set B′ ⊂ Zq, |B′| ≥ ⌊log4 q⌋ such that B′−B′ ⊂ C0(q). In the latter case, it suﬃces to consider B = tB′ for any non-cubic residue t ∈ Zq.) Also, a construction of a set B′ such that B′−B′ ⊂ C0(q), log6 q |B|, not using Ramsey theory, appears in Theorem 3 of [1]. For a prime q = 3k+2 the problem is trivial as |B| ≤ 1. For

- a square-free integer q = s1s2 . . .sm, where si = 3ki+1, a straightforward direct product


construction (see Section 8 in [3]) gives a suitable set B with |B| ≥ mi=1⌊log4 si⌋. We are not aware of any stronger results, and numerical experiments seem to indicate that

the logarithmic size is not far from the truth for primes q = 3k + 1.

We will obtain upper bounds on λ(C0(q)), and these will automatically imply upper bounds on δ(C0(q)). In particular, according to Theorem 1.4 in [3], any modular witness function g(q) in equation (2) testiﬁes an upper bound |Bq| ≤ b0q for the cardinality of a set Bq ⊂ Zq such that Bq − Bq avoids the kth-power residues modulo q. Similarly, a kth power witness function f(n) will lead to an estimate |B0| a0nk for the cardinality of a set B0 ⊂ [1, . . .nk] such that B0 − B0 avoids the kth powers. Our aim, therefore, is to

minimize the values of a0 and b0 in equations (1) and (2). We will only be concerned with the modular case in this note.

Notice that f(n)(x) automatically induces a modular witness function modulo q = n by deﬁning g(n)(y) = f(n)(y/n), and if n is squarefree then f(n) and g(n) have the same constant terms a0 = b0. Therefore, constructing modular kth power witness functions g(q) is formally easier than constructing kth power witness functions f(n). Conversely, in later publications of this series of papers we hope to construct a family of witness

- functions f(n) assuming that we already have a family of self-compatible modular witness
- functions g(q) at our disposal. Self-compatibility is a natural property deﬁned here.


- Deﬁnition 1.3. A family of kth power modular witness functions g(q) (q = 1, 2, . . .) of


the form (2) is called self-compatible if g(q

1)(y1) = g(q

2)(y2) whenever y1/q1 = y2/q2.

This paper will be devoted entirely to constructing a self-compatible family of modular witness functions for k = 3, which is a very interesting problem in itself.

2. Cubic residues

Somewhat surprisingly, the case of cubic residues is considerably easier to handle than that of quadratic residues. This is due to the fact that k = 3 is an odd number and therefore -1 is automatically a cubic residue modulo q for any q. This implies that the set of cubic residues modulo q = pα

1 . . .pα

r is always symmetric to 0. Also, it is equal to the direct product of the sets of cubic residues modulo pα

1

r

1 , . . ., pα

r . Therefore the results on direct products in [3, Section 8] can be invoked, and the problem reduces to forming nonnegative exponential sums with cubic residue frequencies in cyclic groups Zpα of prime-power order. The self-compatibility property will be an automatic consequence of the construction.

1

r

We ﬁrst consider the case of squarefree moduli q, which is of independent interest in itself.

Theorem 2.1. Let q = p1p2 . . .prs1s2 . . .sm be a squarefree integer, where pi denote primes of the form 3k + 2, sl denote primes of the form 3k + 1, and if 3|q then we list the prime 3 among the pi. There exists a cubic witness function modulo q, g(q)(y) =

- b0 + j q=1−1 bj(e(j3y/q) + e(−j3y/q)) ≥ 0, y = 0, 1, . . ., q − 1, g(q)(0) = 1, such that


- (3) b0 ≤

r

i=1

1 pi

![image 3](<2024-matolcsi-difference-sets-positive-exponential_images/imageFile3.png>)

m

l=1

2 √sl ≤

![image 4](<2024-matolcsi-difference-sets-positive-exponential_images/imageFile4.png>)

![image 5](<2024-matolcsi-difference-sets-positive-exponential_images/imageFile5.png>)

2m √q

![image 6](<2024-matolcsi-difference-sets-positive-exponential_images/imageFile6.png>)

![image 7](<2024-matolcsi-difference-sets-positive-exponential_images/imageFile7.png>)

.

That is, with the notation of Deﬁnition 1.2, we have

- (4) λ(C0(q)) ≤


2m √q

![image 8](<2024-matolcsi-difference-sets-positive-exponential_images/imageFile8.png>)

for every ε > 0.

- 1

![image 9](<2024-matolcsi-difference-sets-positive-exponential_images/imageFile9.png>)

- 2+ε)


= Oε(q−

![image 10](<2024-matolcsi-difference-sets-positive-exponential_images/imageFile10.png>)

Proof. For a prime p = 3k + 2, all elements of Zp are cubic residues. Therefore, we can take the trivial witness function modulo p,

- (5) g(p)(y) =

1 p

![image 11](<2024-matolcsi-difference-sets-positive-exponential_images/imageFile11.png>)

p−1

j=0

e(j3y/p),

with the constant term being p1. That is, λ(C0(p)) ≤ p1 (in fact, equality holds). The same is true for p = 3, which is listed among the pi if 3|q.

![image 12](<2024-matolcsi-difference-sets-positive-exponential_images/imageFile12.png>)

![image 13](<2024-matolcsi-difference-sets-positive-exponential_images/imageFile13.png>)

For a prime s = 3k + 1 the set C(s) ⊂ Zs of non-zero cubic residues modulo s is

symmetric to zero, and consists of s−31 elements. Denoting the cubic multiplicative characters on Zs by χ0, χ1, χ2 (with χ0 being the principal character), we have

![image 14](<2024-matolcsi-difference-sets-positive-exponential_images/imageFile14.png>)

- (6)

s−1

j=1

e(j3y/s) =

s−1

l=1

e(ly/s)χ0(l) +

s−1

l=1

e(ly/s)χ1(l) +

s−1

l=1

e(ly/s)χ2(l) ≥ −1 − 2√s,

![image 15](<2024-matolcsi-difference-sets-positive-exponential_images/imageFile15.png>)

because the last two sums have absolute value √s (see [4, Lemma 4.3]). Therefore, after normalization, we may take

![image 16](<2024-matolcsi-difference-sets-positive-exponential_images/imageFile16.png>)

- (7) g(s)(y) =


2√s + 1 2√s + s

s−1

![image 17](<2024-matolcsi-difference-sets-positive-exponential_images/imageFile17.png>)

1 2√s + s

e(j3y/s) ≥ 0, (y = 0, . . ., s − 1), g(s)(0) = 1,

+

![image 18](<2024-matolcsi-difference-sets-positive-exponential_images/imageFile18.png>)

![image 19](<2024-matolcsi-difference-sets-positive-exponential_images/imageFile19.png>)

![image 20](<2024-matolcsi-difference-sets-positive-exponential_images/imageFile20.png>)

![image 21](<2024-matolcsi-difference-sets-positive-exponential_images/imageFile21.png>)

j=1

√s+1

2√s+s ≤ √2s. That is, λ(C0(s)) ≤ √2s Finally, the group Zq is the direct product of the groups Zp

![image 22](<2024-matolcsi-difference-sets-positive-exponential_images/imageFile22.png>)

and the constant term satisﬁes 2

![image 23](<2024-matolcsi-difference-sets-positive-exponential_images/imageFile23.png>)

![image 24](<2024-matolcsi-difference-sets-positive-exponential_images/imageFile24.png>)

![image 25](<2024-matolcsi-difference-sets-positive-exponential_images/imageFile25.png>)

![image 26](<2024-matolcsi-difference-sets-positive-exponential_images/imageFile26.png>)

![image 27](<2024-matolcsi-difference-sets-positive-exponential_images/imageFile27.png>)

![image 28](<2024-matolcsi-difference-sets-positive-exponential_images/imageFile28.png>)

, and the set of cubic residues C0(q) modulo q is symmetric to zero and equals the direct product of the sets C0(pi) and C(s

and Zs

i

l

l)

0 . Therefore, the direct product construction of [3, Theorem 8.1] can be applied, and equation (35) in [3] implies λ(C0(q)) = ri=1 λ(C0(pi)) ml=1 λ(C(s

l)

0 ) , and the bound given in (3) follows. Finally, estimate (4) follows from the fact that

- 2m = O(qε).


Remark 2.2. For primes of the form s = 3k + 1 the estimate λ(C0(s)) ≤ √2s is asymptotically optimal, and therefore the exponent in the bound λ(C0(q)) = O(q−21+ε) cannot be improved.

![image 29](<2024-matolcsi-difference-sets-positive-exponential_images/imageFile29.png>)

![image 30](<2024-matolcsi-difference-sets-positive-exponential_images/imageFile30.png>)

![image 31](<2024-matolcsi-difference-sets-positive-exponential_images/imageFile31.png>)

Via Theorem 1.4 in [3] the bound (4) above immediately implies the same upper bound for the density of sets avoiding cubic residues:

Corollary 2.3. For any ε > 0 and any square-free positive integer q, the density δ(Bq) of any set Bq ⊂ Zq such that the diﬀerence set Bq − Bq avoids cubic residues modulo q satisﬁes δ(Bq) = Oε(q−12+ε).

![image 32](<2024-matolcsi-difference-sets-positive-exponential_images/imageFile32.png>)

Now we turn to general (non-squarefree) moduli q. The direct product construction can still be applied in this case, but the construction of witness functions modulo primepowers is slightly more technical.

Lemma 2.4. Using the notation of Deﬁnition 1.2, we have

- (8) λ(C(p

m)

0 ) = λ(C0(p))[(m+2)/3] for any prime p = 3 and any integer m ≥ 1 (the notation [x] stands for the integer part of any number x). For p = 3 we have

- (9) λ(C(3

3m)

0 ) = λ(C0(27))m.

Proof. Let p = 3. We prove the lemma by induction on m. For m = 1 the statement is trivial. Let m ≥ 2, and let us identify the residue classes modulo pm with the numbers 0, 1, . . ., pm − 1.

The structure of the cubic residues modulo pm is the following: for 0 < t ≤ pm−1 − 1 and 0 ≤ l ≤ p − 1 we have t + lpm−1 ∈ Cpm if and only if t ∈ Cpm−1. For t = 0, we have two diﬀerent cases. If 3 does not divide m − 1 then lpm−1 ∈ Cpm if and only if l = 0. If

- 3|m − 1 then lpm−1 ∈ Cpm if and only if l ∈ C0(p).


Consider the subgroup H = {0, pm−1, . . ., (p − 1)(pm−1)} ⊂ Zpm. Then H ≡ Zp, Zpm/H ≡ Zpm−1 and we can apply the general result concerning subgroups and factor groups in Theorem 7.2 in [3]. Namely, by formula (29) in [3], and the structure of C(p

m)

0 described above, we obtain λ(C(p

m)

0 ) ≥ λ(C(p

m−1)

0 ) if 3 does not divide m−1, and λ(C(p

m)

0 ) ≥ λ(C(p

m−1)

0 )λ(C0(p)) if 3|m − 1. This proves the lower bound in the inductive step.

To prove the upper bound, we apply a simple construction. Let

- (10) g(p)(y) = b0(p) +

j∈C(p)

bj(p)e(jy/p)

be a witness function modulo p such that b0(p) is minimal, i.e. b0(p) = λ(C0(p)) (a simple compactness argument shows that the minimal value of b0(p) can indeed be attained). Similarly, let

- (11) g(p

m−1)(y) = b(p

m−1)

0 +

t∈C(pm−1)

b(p

m−1)

t e(ty/pm−1)

be a witness function modulo pm−1 such that b(p

m−1)

0 = λ(C(p

m−1)

0 ). Deﬁne

- (12) g(p

m)(z) =

t∈C(pm−1)

b(p

m−1) t

![image 33](<2024-matolcsi-difference-sets-positive-exponential_images/imageFile33.png>)

p

p−1

l=0

e((t + lpm−1)z/pm) + h0(z)

where h0(z) = b(p

m−1)

0 if 3 does not divide m−1, and h0(z) = b(p

m−1)

0 (b0(p)+ j∈C(p) bj(p)e(jz/p)) if 3|m − 1. It is clear that g(pm)(0) = 1 and the constant term of g(pm)(z) is equal to b(p

m−1)

0 = λ(C(p

m−1)

0 ) if 3 does not divide m−1, while it is b(p

m−1)

0 b0(p) = λ(C(p

m−1)

0 )λ(C0(p)) if 3|m−1. We claim that g(pm)(z) is indeed a witness function modulo pm, i.e. g(pm)(z) ≥ 0 for z = 0, 1, . . .pm − 1. If z = py then a substitution into the deﬁnitions shows that

- (13) g(p


m)(z) = g(p

m)(py) = g(p

m−1)(y) ≥ 0.

If z = py +j where j = 0, then for each t ∈ C(pm−1) we have pl=0−1 e((t+lpm−1)z/pm) = e(t(py + j)/pm) pl=0−1 e(lj/p) = 0, therefore

- (14) g(p

m)(z) = g(p

m)(py + j) = h0(py + j) = b(p

m−1)

0 g(p)(j) ≥ 0. This proves the upper bound in the inductive step and completes the proof of the Lemma for p = 3.

- For p = 3 the proof is similar. The structure of the cubic residues modulo 33m is the


following: for 0 < t ≤ 33(m−1) − 1 and 0 ≤ l ≤ 26 we have t + l33(m−1) ∈ C33m if and only if t ∈ C33(m−1). For t = 0, we have l33(m−1) ∈ C33m if and only if l ∈ C0(27).

Consider the subgroup H = {0, 33(m−1), . . ., 26(33(m−1))} ⊂ Z33m. Then H ≡ Z27, Z33m/H ≡ Z33(m−1), and formula (29) in [3] implies λ(C(3

3m)

0 ) ≥ λ(C(3

3(m−1))

0 )λ(C0(27)). This proves the lower bound in the inductive step.

To prove the upper bound we deﬁne

- (15)

g(3

3m)(z) =

t∈C(33(m−1))

b(3

3(m−1)) t

![image 34](<2024-matolcsi-difference-sets-positive-exponential_images/imageFile34.png>)

27

26

l=0

e((t+l33(m−1))z/33m)+b(3

3(m−1))

0 (b(27)0 +

j∈C(27)

b(27)j e(jz/27)),

and note that g(33m)(0) = 1, the constant term is λ(C(3

3(m−1))

0 )λ(C0(27)), and for z = 27y we have

- (16) g(3

3m)(z) = g(3

3m)(27y) = g(3

3(m−1))(y) ≥ 0, and for z = 27y + j where j = 0 we have

- (17) g(3

3m)(z) = g(3

3m)(27y + j) = b(3

3(m−1))

0 g(27)(j) ≥ 0.

This lemma enables us to prove our main result concerning cubic residues in cyclic groups. Theorem 2.5. For ε = −log

(1−2+cos(π/13)+sin(32 π/26))

![image 35](<2024-matolcsi-difference-sets-positive-exponential_images/imageFile35.png>)

![image 36](<2024-matolcsi-difference-sets-positive-exponential_images/imageFile36.png>)

3 log 13 ≈ 0.1195 there exists a self-compatible family g(q)(y) of cubic modular witness functions of the form (2) such that b0 ≤ q−ε. In particular,

- (18) λ(C0(q)) ≤ q−ε for every q ≥ 1. Proof. If q = 3 is a prime of the form 3k + 2 we deﬁne the modular witness function g(q)(y) by equation (5), and note that λ(C0(q)) = q−1. If q is a prime of the form 3k + 1 we deﬁne g(q)(y) = b(0q) + b(q) j q=1−1 e(j3y/q) such that b(0q) + (q − 1)b(q) = 1, g(q)(y) ≥ 0


for 0 ≤ y ≤ q − 1, and b(0q) is minimal possible, i.e. b(0q) = λ(C0(q)) (it is easy to see that all the coeﬃcients of e(j3y/q) can be assumed to be equal by averaging; cf. [3,

√q+1

Proposition 5.2]). By equation (7) we note that λ(C0(q)) ≤ 2

![image 37](<2024-matolcsi-difference-sets-positive-exponential_images/imageFile37.png>)

2√q+q ≤ q−0.36 for q ≥ 31.

![image 38](<2024-matolcsi-difference-sets-positive-exponential_images/imageFile38.png>)

![image 39](<2024-matolcsi-difference-sets-positive-exponential_images/imageFile39.png>)

- For q = 7, 13, and 19 direct computation shows that λ(C0(q)) ≤ q−3ε with equality for q = 13.


If q = pm is a power of a prime p = 3 then we deﬁne g(q)(y) by induction on m as

in Lemma 2.4. Equation (8) shows that λ(C0(q)) ≤ q−ε. The self-compatibility property follows from equation (13).

For q = 27 we deﬁne g(27)(y) = b(27)0 + b(27) j∈C(27) e(jy/27) such that g(27)(0) = 1, g(27)(y) ≥ 0 for y = 0, 1, . . ., 26, and b(27)0 = λ(C0(27)) (again, the non-leading coeﬃcients can be assumed to be equal by averaging). For q = 33m we deﬁne g(q)(y) by induction on m as in Lemma 2.4. For q = 33m−1 and q = 33m−2 we deﬁne g(q)(y) = g(3m)(3y) and g(q)(y) = g(3m)(9y), respectively. Self-compatibility follows from this deﬁnition and

equation (16). Direct computation of λ(C0(27)) and equation (9) shows that for any q = 3α we have λ(C0(q)) ≤ q−ε.

Finally, let q = pα

- 0

0 pα

1

- 1 . . .pα


r be the prime factorization of q, where p0 = 3 if it appears in q. The set of cubic residues C0(q) modulo q is symmetric to zero and equals the direct product of the sets C(p

r

α)

0 . Furthermore, as in the construction of [3, Theorem 8.1] we deﬁne the cubic witness function g(q)(y) = b(0q) + j∈C(q) b(jq)e(jy/q) as the direct product of the cubic modular witness functions g(pα). It is straightforward that the

self-compatibility property is preserved under direct products, and λ(C0(q)) ≤ b(0q) = b(3

αr i )

α0) 0

i=1 λ(C(p

r

0 ) ≤ q−ε.

Again, via Theorem 1.4 in [3] the bound (18) above immediately implies the same upper bound for the density of sets avoiding cubic residues:

(1−2+cos(π/13)+sin(32 π/26))

Corollary 2.6. For ε = −log

![image 40](<2024-matolcsi-difference-sets-positive-exponential_images/imageFile40.png>)

3 log 13 ≈ 0.1195 and any positive integer q, the density δ(Bq) of any set Bq ⊂ Zq such that the diﬀerence set Bq − Bq avoids cubic residues modulo q satisﬁes δ(Bq) ≤ q−ε.

![image 41](<2024-matolcsi-difference-sets-positive-exponential_images/imageFile41.png>)

Acknowledgement

The authors are grateful for the reviewer for his/her suggestions which have improved the presentation of the paper.

References

- [1] S. D. Cohen: Clique numbers of Paley graphs, Quaestiones Mathematicae, Vol 11, 225–231,

(1988).

- [2] M. R. Gabdullin: Sets in Zm whose diﬀerence sets avoid squares, Sb. Math., 209:11 (2018), 1603 – 1610.
- [3] M. Matolcsi, I. Z. Ruzsa: Diﬀerence sets and positive exponential sums I. General properties, J. Fourier Anal. Appl., Vol. 20, no. 1, 17–41, (2014).
- [4] R. C. Vaughan: The Hardy-Littlewood method, Cambridge tracts in mathematics 125, Second edition, Cambridge University Press, 1997.


Mat´ ´e Matolcsi: Budapest University of Technology and Economics (BME), H-1111, Egry J. u. 1, Budapest, Hungary, and Alfr´ed R´enyi Institute of Mathematics, POB 127 H-1364 Budapest, Hungary.

Email address: matomate@renyi.hu

I. Z. R.: Alfr´ed R´enyi Institute of Mathematics, Hungarian Academy of Sciences POB 127 H-1364 Budapest, Hungary

Email address: ruzsa@renyi.hu

