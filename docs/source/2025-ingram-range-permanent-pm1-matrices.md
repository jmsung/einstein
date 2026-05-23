---
type: source
kind: paper
title: On the Range of the Permanent of $(\pm1)$-Matrices
authors: DeVon Ingram, Alexander Razborov
year: 2025
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2507.09433v1
source_local: ../raw/2025-ingram-range-permanent-pm1-matrices.pdf
topic: general-knowledge
cites:
---

## arXiv:2507.09433v1[math.CO]13Jul2025

# On the Range of the Permanent of (±1)-Matrices

##### DeVon Ingram∗ Alexander Razborov† July 15, 2025

###### Abstract

We establish a superpolynomial lower bound on the range of the permanent function on the set of n × n matrices with ±1 entries.

### 1 Introduction

The determinant of an n × n matrix M is given by the following formula:

n

det(M) :=

sign(σ)

aiσ(i).

σ∈Sn

i=1

The permanent is defined similarly, but without the factor of sign(σ):

n

per(M) :=

aiσ(i)

σ∈Sn

i=1

This seemingly innocuous modification leads to stark differences between determinants and permanents, see e.g. [13].

A considerable amount of attention in the theory of permanents has been paid to 0-1 matrices and (±1)-matrices due to their importance in combinatorics, numerical analysis and many other areas. The theory of permanents of 0-1 matrices is rich and well developed, see e.g. [6] and the references cited therein. The investigation of the permanents of (±1)matrices, which is the subject of the current note, also has a long history starting with [12, 18, 17] and continued in [24, 7, 19, 8, 25, 5, 6, 4].

Much of this work, both for 0-1 and (±1)-matrices has concentrated on studying the range of the permanent function, i.e the set of values it can attain for a given n. As an example, the main result of [24] asserts certain divisibility conditions by powers of 2 that per(M) must satisfy for a (±1)-matrix M and [3] complemented this with non-divisibility conditions. Krauter’s conjecture concerning the minimum positive value of per(M) is still open, although it was confirmed for smaller values of n in [25].

∗University of Chicago, Department of Mathematics, dingram@math.uchicago.edu †University of Chicago, razborov@uchicago.edu and Steklov Mathematical Institute,

razborov@mi-ras.ru

One of the most basic questions one can ask in this direction is about the cardinality of the range or, in other words, “how many values are attained by the permanent on the set of (±1)-matrices?” Surprisingly, the only known lower bound on the cardinality of the aforementioned set seems to be n + 1 [8]. This is in sharp contrast with the situation for 0-1 matrices where the exponential lower bound n! had been known long ago [2]. Perhaps, one explanation of this remarkable difference is that while the permanent of a 0-1 matrix (or, for that matter, any matrix with non-negative entries) is monotone in its entries, for (±1)-matrices it is not true and local changes can bring about unpredictable results.

A better understanding of the range of the permanent function may yield insight on its study in various applications, such as combinatorial random matrix theory [21, 23, 9] and quantum computing [1]. Also, a description of the overall structure of the range may lead to progress towards answering questions concerning the existence of large generalized arithmetic progressions contained within the range, which in turn would yield results on the (anti)concentration of the permanent [15].

The main result of this note (Theorem 2) drastically improves Krauter’s lower bound to super-polynomial in n. The proof uses some concepts and simple ideas from additive combinatorics and Diophantine geometry.

### 2 Notation and the main results

- • Rk×n - the set of all real k × n matrices
- • Ωk,n ⊆ Rk×n - the set of all matrices with ±1 entries
- • Jk,n ∈ Ωk,n - the matrix in which all entries are equal to 1
- • A∗B ∈ R(k+ℓ)×n - the matrix obtained by row concatenation of A ∈ Rk×n and B ∈ Rℓ×n
- • For ⃗n = (n1,...,nk) with n1 + ... + nk ≤ n, we let B⃗n ∈ Ωk,n be the matrix in which every column has at most one entry that is equal to -1 and the ith row has ni such entries (and hence there are n0 def= n − (n1 + ... + nk) columns with all ones)
- • [n] def= {1,...,n} - the first n positive integers
- • Sk,n (for k ≤ n) - the set of all injective functions σ: [k] ↣ [n]
- • (n)k def= |Sk,n| = n(n − 1)···(n − k + 1) - the kth falling factorial of n
- • per(A) def=

σ∈Sk,n

A1σ(1) ···Akσ(k) - the permanent of A ∈ Rk,n

- • rk,n def= |{per(A)| A ∈ Ωk,n}| - the number of distinct values attained by the permanent of matrices in Ωk,n
- • eℓ(x1,...,xk) def=


xi - the ℓth elementary symmetric polynomial in k variables

) i∈S

[k] ℓ

S∈(

We will use lowercase letters to denote 1×n matrices (e.g. jn = (1,...,1) is the n-dimensional row vector with all entries equal to 1). We also write Ωn def= Ωn,n,Sn def= Sn,n, and rn def= rn,n.

Our main result is the following:

- Theorem 1 For every k ≥ 1 there exists a constant ϵk > 0 such that for all n ≥ k + 1 we have

rk+1,n ≥ ϵknk−2.

We remark that for 1 ≤ k ≤ ℓ ≤ n, per(A ∗ J(ℓ−k),n) = per(A) · (n − k)ℓ−k. Therefore, rk,n is increasing in k ≤ n,1 and in particular, rn ≥ rk,n.

The precise asymptotics in Theorem 1 can be made explicit, and we will do so in Section

5. Along with the remark above this will imply

- Theorem 2 rn ≥ nΩ(

log n log log n

).

- 3 Preliminaries


We briefly review some standard definitions.

#### 3.1 Generalized arithmetic progressions This material can be found e.g. in [22].

Definition 3 (Generalized Arithmetic Progression) A generalized arithmetic progression (GAP) of dimension d is defined to be a set of the form

{x0 + ℓ1x1 + ··· + ℓdxd : 0 ≤ ℓ1 < L1,...,0 ≤ ℓd < Ld} where x0,x1,...,xd,L1,...,Ld ∈ Z.

Equivalently, a GAP is the projection of a d-dimensional “box” in Zd to Z. Given a GAP as defined above, we call the product L1 ...Ld the size of the GAP. A GAP is proper if its cardinality equals its size, i.e. the corresponding projection is injective.

#### 3.2 Permanents

We now review several properties of permanents. Recall that the Laplace expansion (or rather its straightforward analogue for permanents) of an n × n matrix B along the ith row is given by

n

per(B) =

bijpij

j=1

1Remarkably, we have not been able to prove that rk,n is increasing in n.

where bij is the (i,j) entry of B and pij is the permanent of the submatrix obtained by removing the ith row and jth column of B. We note that this formula readily extends to rectangular k × n matrices, where k ≤ n.

We will also need the following explicit computation of the permanent of the matrices Bn

1,...,nk that will be the main building block in our construction.

- Lemma 4 For n1 + ··· + nk ≤ n,


per(Bn

1,...,nk) =

k

αℓ(n)eℓ(n1,...,nk),

ℓ=0

where

αℓ(n) def= (−2)ℓ(n − ℓ)k−ℓ

Proof. Each summand in the permanent of a k × n matrix can be identified with an injective function σ : [k] → [n] (given a row in [k] as an input, return a column in [n] as an output). Set I(σ) def= i ∈ [k] Bi,σ(i) = −1 , where B def= Bn

1,...,nk. That is, let ΓI def= {σ ∈ Sk,n | I(σ) = I }. Then

per(B) =

(−1)|I| · |ΓI|. (1)

I⊆[k]

Let Γ≥I def= J⊇I ΓJ. Then we can compute |ΓI| via M¨obius inversion [11] |ΓI| =

(−1)|J\I| · |Γ≥J|. (2)

J⊇I

One way to arrive at this equality is to note that every σ ∈ ΓI contributes 1 to both parts while every σ ∈ ΓJ with J ⊃ I contributes zero. After plugging (2) into (1) and swapping the order of summation, we see that

###### (−1)|J| · |Γ≥J| =

per(B) =

I⊆J⊆[k]

(−2)|J| · |Γ≥J|.

J⊆[k]

It only remains to note that |Γ≥J| = i∈J ni · (n − |J|)k−|J| (values σ(i) for i ̸∈ J can be assigned arbitrarily). Thus, splitting the sum according to |J|,

per(B) =

k

(−2)ℓ · (n − ℓ)k−ℓ ·

ℓ=0

J∈(

) i∈J

[k] ℓ

ni =

k

αℓ(n)eℓ(n1,...,nk).

ℓ=0

### 4 Proof of Theorem 1

Let k > 0. We fix a probability distribution µ = (µ1,...,µk) on [k], where µi are arbitrary positive distinct rationals summing to one. For example, we can set

µi def=

i

k+1 2

(1 ≤ i ≤ k) (3)

albeit the exact choice of µi will become important only in Section 5.

Let dk be the least common multiple of the denominators of µ1,...,µk, let n0 < dk be the remainder of n mod dk, and let

ni def= µi(n − n0). (4)

Then (provided n ≥ dk) ni are positive integers such that n1 +...+nk = n−n0 ≤ n. Hence we may consider the corresponding matrix B def= Bn

1,...,nk, and we are going to show that |{per(a ∗ B)| a ∈ {±1}n}| ≥ εknk−2,

(where εk will also be determined later), thus establishing Theorem 1. Our first observation is that |{per(a ∗ B)| a ∈ {±1}n}| = |{per(ε ∗ B)| ε ∈ {0,1}n}|. (5)

Indeed, for a ∈ {±1}n, let εa = 21(jn − a); εa ∈ {0,1}n. Then, since the permanent function is linear in every individual row,

per(εa ∗ B) =

- 1

- 2


(per(jn ∗ B) − per(a ∗ B)).

Hence the two sets featuring in (5) are obtained from each other by an invertible affine transformation and (5) follows.

Recall that n0 = n − (n1 + ... + nk). Assume without a loss of generality that the first n0 columns in B are all ones and let us restrict ourselves in (5) only to those ϵ for which ϵ1 = ... = ϵn

= 0. Then the value per(ε ∗ B) can be computed by Laplace’s expansion in the first row. Namely, let xi ∈ [0,ni] be the number of those j ∈ [n] for which εj = 1 and Bij = −1; thus, ε can be identified with the point x ∈ [0,n1] × ... ∈ [0,nk]. In addition, let

0

pi def= per(Bn

1,...,ni−1,ni−1,ni+1,...,nk). Then the Laplace expansion amounts to the formula

per(ε ∗ B) =

k

pixi.

i=1

In other words, the set of interest {per(ε ∗ B)| ε ∈ {0,1}n} is simply the generalized kdimensional arithmetic progression

Γ def=

k

pixi | 0 ≤ xi ≤ ni

i=1

with basis p1,...,pk. This set need not be proper, and the rest of the proof amounts to showing that it contains a sufficiently large proper sub-progression.

By Lemma 4,

pi =

=

k

αℓ(n − 1)eℓ(n1,...,ni−1,ni − 1,ni+1,...,nk)

ℓ=0

k

αℓ(n − 1)eℓ(µ1(n − n0),...,µi−1(n − n0),µi(n − n0) − 1,µi+1(n − n0),...,µk(n − n0));

ℓ=0

also note that αℓ(n − 1) is an integer polynomial in n of degree k − ℓ. This observation allows us to view pi as a polynomial of degree ≤ k in Q[n0,n] (recall that the µi are fixed throughout the argument).

The crucial part of the proof is the following result.

- Lemma 5 (main) For any integer n0, the resulting system of polynomials p¯1(n),...,p¯k(n) ∈ Q[n] has co-rank ≤ 2 over Q. In other words, these polynomials span a Q-linear space of dimension ≥ k − 2.


We will prove Lemma 5 in the next section. For now, we will show how it implies Theorem 1. Let Nk > 0 be an integer such that Nk · p1,...,Nk · pk are integer polynomials (say, Nk = dkk will do), and let Mk be the sum of absolute values of the coefficients of Nk · p¯1(n),...,Nk · p¯k(n), maximized over all choices of n0 = 0,1,...,dk − 1. Let

δk def= min (4Mk)−1,µ1,...,µk . (6)

Fix n0 ∈ {0,1,...,dk − 1} and pick any I ∈ k [−k]2 such that {p¯i(n)| i ∈ I } are linearly

independent. Consider the sub-cube Q ⊆ ki=1[0..ni] defined as follows: (x1,...,xk) ∈ Q iff ∀i ∈ I(xi ∈ [0..δkn]) and ∀i ̸∈ I(xi = 0). Clearly, |Q| ≥ (δkn)k−2. Then the following claim implies Theorem 1, with

ϵk def= δkk−2. (7) Claim 6 The restriction of Γ onto Q is proper.

Proof. Let x ̸= y ∈ Q; we have to prove that ki=1(yi − xi)pi ̸= 0. By our choice of

⃗µ and I, the integer univariate polynomial ki=1(yi − xi)Nkp¯i(n) is non-zero. Let d be its degree, thus

k

(yi − xi)Nkp¯i(n) = βdnd + βd−1nd−1 + ... + β1n,

i=1

where β1,...,βd ∈ Z and βd ̸= 0. Moreover, |βj| ≤ (2δkn)Nk ≤ n/2, where the second inequality follows from the definition (6) of δk. Hence

k

- 1

- 2 −


(yi − xi)Nkp¯i(n) ≥ nd 1 −

i=1

- 1

- 2n −


- 1

- 2n2 − ··· > 0.


The proof of Theorem 1 is now complete, modulo lemma 5.

#### 4.1 Proof of the main lemma

Recall that the permanental minor pi (where i ≥ 1) is given by

k

αℓ(n − 1)eℓ(n1,...,ni−1,ni − 1,ni+1,...,nk).

pi =

ℓ=0

We are actually going to prove that already the polynomials p¯1(n) − p¯i(n) (i > 1), for any pairwise distinct µ1,...,µk and any integer n0, span a subspace of dimension ≥ k − 2. To that end, we compute

k

p1 − pi =

αℓ(n − 1)[eℓ(n1 − 1,n2,...,nk) − eℓ(n1,...,ni−1,ni − 1,ni+1,...,nk)]

ℓ=0

k

αℓ(n − 1)[eℓ−1(n1,...,ni−1,ni+1,...,nk) − eℓ−1(n2,...,nk)]

=

ℓ=0

,

k

αℓ(n − 1)eℓ−2(n2,...,ni−1,ni+1,...,nk)

= (n1 − ni)

ℓ=2

k

αℓ(n − 1)(n − n0)ℓ−1eℓ−2(µ2,...,µi−1,µi+1,...,µk),

= (µ1 − µi)

ℓ=2

where in the last line we used the definition (4) of ni. Let

p1 − pi µ1 − µi ∈ Z[n].

pi(n) def=

Consider the (k − 1) × (k − 1) matrix M with Mij (2 ≤ i ≤ k,0 ≤ j ≤ k − 2) being the coefficient of the nk−j−1 in the ith polynomial pi(n). We would like to show that this matrix has rank ≥ k − 2 over Q. Let us compute its entries.

First, note that ((nn−−kℓ−−1)!1)!(n − n0)ℓ−1 is a polynomial of degree k − 1 in n, so we can expand this quotient as an alternating sum with coefficients given by elementary symmetric

polynomials in the values ℓ + 1,...,k and ℓ − 1 copies of n0:

(n − ℓ − 1)! (n − k − 1)!

(n − n0)ℓ−1 = (n − n0)(n − n0)...(n − n0)

(n − ℓ − 1)...(n − k)

ℓ−1 times

k−1

(−1)jnk−j−1ej(n0,...,n0

=

,ℓ + 1,...,k).

j=0

ℓ−1 times

Inserting this sum into the equation for p1 − pi, we obtain

k−1

k

,ℓ + 1,...,k)nk−j−1.

(−1)j(−2)ℓeℓ−2(µ2,...,µi−1,µi+1,...,µk)ej(n0,...,n0

pi(n) =

j=0

ℓ=2

ℓ−1 times

Switching the order of summation yields

k−1

(−1)jnk−j−1

pi(n) =

j=0

Thus

k

(−2)ℓeℓ−2(µ2,...,µi−1,µi+1,...,µk)ej(n0,...,n0

,ℓ + 1,...,k).

ℓ=2

ℓ−1 times

k

Mij = (−1)j

(−2)ℓeℓ−2(µ2,...,µi−1,µi+1,...,µk)ej(n0,...,n0

,ℓ + 1,...,k),

ℓ=2

ℓ−1 times

where 2 ≤ i ≤ k, 0 ≤ j ≤ k − 2.

We now interpret this computation in a matrix form. For that, let Rℓ ∈ Q[2...k] be given by

- (Rℓ)i def= eℓ−2(µ2,...,µi−1,µi+1,...,µk),

and let Sℓ ∈ Q[0..k−2] be given by

- (Sℓ)j def= (−1)j · ej(n0,...,n0


,ℓ + 1,...,k).

ℓ−1 times

Then

k

(−2)ℓ(RℓSℓ⊤).

M =

ℓ=2

The vectors Rℓ are linearly independent over Q since the determinant of the matrix comprised of these vectors can be viewed as the Jacobian matrix corresponding to the transformation

(µ2,...,µk)  → (ek−1(µ2,...,µk),...,e1(µ2,...,µk)),

which is nonsingular at every point (µ2,...,µk) with pairwise distinct coordinates [10]. In fact, the determinant is proportional to

∆ def=

(µi − µj).

2≤i<j≤k

Note that applying an invertible linear transformation on the left to the matrix M does not change its rank. Hence

rk(M) = dim(Span(Sℓ|2 ≤ ℓ ≤ k)).

To compute the dimension of this space, we need the following generalization: for a ≥ 1, 2 ≤ ℓ ≤ k + 1 − a, we let Sℓ,a ∈ Q[0...k−a−1] be given by

(Sℓ,a)j def= (−1)j · ej(n0,...,n0

,ℓ + a,ℓ + a + 1,...,k),

ℓ−1 times

so that Sℓ = Sℓ,1. Then we have the following recursion:

(Sℓ+1,a − Sℓ,a)0 = 0 (since (Sℓ,a)0 = 1 for all a,ℓ) (Sℓ+1,a − Sℓ,a)j = (ℓ + a − n0)(Sℓ,a+1)j−1, j ≥ 1.

Or, in the vector form,

(8)

Sℓ+1,a − Sℓ,a = (ℓ + a − n0)(0 ∗ Sℓ,a+1). Now, since Sk+1−a,a has 1 in the position j = 0, we have the recursion dim(Span(Sℓ,a| 2 ≤ ℓ ≤ k + 1 − a))

= dim(Span(Sk+1−a,a,(Sℓ+1,a − Sℓ,a | 2 ≤ ℓ ≤ k − a)))

= 1 + dim(Span((ℓ + a − n0) · Sℓ,a+1 | 2 ≤ ℓ ≤ k − a)),

and the only remaining problem is that the coefficient ℓ+a−n0 can be 0. But this is actually not a problem since if ℓ+a = n0 then Sℓ,a+1 = Sℓ−1,a+1 and hence this vector still appears in the set {(ℓ + a − n0) · Sℓ,a+1 | 2 ≤ ℓ ≤ k − a} with coefficient -1 and can be manually added to the right-hand side without changing its dimension unless ℓ = 2. By applying reverse induction on a, we prove that

dim(Span(Sℓ,a | 2 ≤ ℓ ≤ k + 1 − a)) ≥

for a = 1, we obtain the required bound.

k − 1 − a if a ≤ n0 − 2 k − a if a ≥ n0 − 1

### 5 Asymptotics

We first prove an estimate on δk. Recall that

δk = min (4Mk)−1,µ1,...,µk ,

where Mk is the sum of absolute values of the coefficients of dkk·p¯1(n),...,dkk·p¯k(n), maximized over all choices of n0 = 0,1,...,dk−1. Tasked with estimating δk, we will establish an upper bound on Mk.

k

Mk ≤ dkk

(−1)j(−2)ℓeℓ−2(µ2,...,µi−1,µi+1,...µk)ej(n0,...,n0,ℓ + 1,...,k)

ℓ=2

k

= dkk

2ℓeℓ−2(µ2,...,µi−1,µi+1,...µk)ej(n0,...,n0,ℓ + 1,...,k)

ℓ=2

k

k − 2 ℓ − 2

2ℓdkk−(ℓ−2)(dk − 1)···(dk − (ℓ − 2)) ·

≤ dkk

ej(n0,...,n0,ℓ + 1,...,k)

ℓ=2

k

k − 2 ℓ − 2

≤ dkk

2ℓdkk

ej(n0,...,n0,ℓ + 1,...,k)

ℓ=2

k

k − 2 ℓ − 2

k − 1 j

2ℓdkk+j

≤ dkk

ℓ=2

k

k − 1 j

k − 2 ℓ − 2

≤ 2kd2kk

ℓ=2

≤ (4d2kk)k

We now insist that µis are given by (3) so that dk = k+12 = k(k2+1) ≤ 2k2. We conclude that

Mk ≤ (16k5)k. Consequently,

1 4(16k5)k

1 4(16k5)k

δk ≥ min

µ1,µ2,...,µk =

.

Thus δk ≥ k−O(k) and (cf. (7)) ϵk ≥ k−O(k2). Therefore the quantitative version of Theorem 1 can be stated as

2) · nk−2.

rk+1,n ≥ k−O(k

Plugging in k def= ⌊ϵlog loglognn⌋ for a sufficiently small ϵ > 0 makes the first term ≥ n−k/2 and proves Theorem 2.

### 6 Open Questions

This work presents a superpolynomial lower bound on the cardinality of the range of the permanent of ±1 matrices. However, numerical evidence suggests that the true cardinality is much larger. It would thus be interesting to establish an exponential lower bound at the very least.

- Problem 1 Show that rn grows exponentially in n.


One can also consider the question of providing precise asymptotics on the range of the cardinality of the determinant of ±1 matrices. In this setting, there is an injective mapping between the set of determinants of normalized (i.e. scaled by a factor of 2−(n−1)) n × n ±1 matrices and the set of determinants of (n − 1) × (n − 1) 0-1 matrices under which the determinant is scaled by a factor of 2−(n−1) and possibly a minus sign [16]. A lower bound of Ω(2n/n) has been established [20] in the 0-1 setting. Improving the lower bound for ±1 matrices would imply a lower bound for 0-1 matrices, thus we have the following problem:

- Problem 2 Establish a lower bound of Ω(2n) on the cardinality of the range of the determinant of (normalized) ±1 n × n matrices.

One of the goals of this work was to improve our understanding of the structure of the range of the permanent. There are other seemingly innocuous structural questions that evaded all approaches thus far. The permanent of a ±1 matrix is always divisible by a certain power of two. It is open whether this value is always attained:

- Problem 3 (Krauter) Show that the minimum positive value attained by the permanent of a ±1 matrix is equal to 2n−⌊log2(n)⌋−1 if n = 2k − 1 for some k ∈ N, and it is equal to 2n−⌊log2(n)⌋ otherwise. This problem is listed as conjecture 34 in [14].

Numerical experiments also suggest that the family of matrices B⃗n considered in this work fails to produce every value attained by the permanent on ±1 matrices in general. It would be interesting to find a family of matrices which can reproduce every value while being “simpler”. A candidate family is the set of “upper triangular” matrices (in the sense that any −1 entry appears on or above the diagonal).

- Problem 4 Determine whether the range of the permanent on the subset of “upper triangular” ±1 n × n matrices coincides with the range of the permanent on Ωn,n.


#### Acknowledgements

We would like to thank Ilya Shkredov for answering our questions and providing useful references.

### References

- [1] Scott Aaronson and Alex Arkhipov. “The Computational Complexity of Linear Optics”. In: Proceedings of the forty-third annual ACM symposium on Theory of computing. 2011, pp. 333–342.
- [2] Richard A Brualdi and Herbert J Ryser. Combinatorial matrix theory. Vol. 39. Springer, 1991.


- [3] Michael V Budrevich, Alexander E Guterman, and Konstantin A Taranin. “On the Kra¨uter-Seifter Theorem on Permanent Divisibility.” In: Journal of Mathematical Sciences 232.6 (2018).
- [4] Mikhail V Budrevich and Alexander E Guterman. “Kr¨auter conjecture on permanents is true”. In: Journal of Combinatorial Theory, Series A 162 (2019), pp. 306–343.
- [5] Mikhail V Budrevich, Alexander E Guterman, and Konstantin A Taranin. “On divisibility for the permanents of (±1)-matrices”. In: Zapiski Nauchnykh Seminarov POMI 439 (2015), pp. 26–37.
- [6] Alexander E Guterman and Konstantin A Taranin. “On the values of the permanent of (0,1)-matrices”. In: Linear Algebra and its Applications 552 (2018), pp. 256–276.
- [7] Arnold R Krauter. “Permanenten - ein Kurzer Uberblick”. In: Se´minaire Lotharingien de Combinatoire 9 (1983), p. 34.
- [8] Arnold R Kra¨uter. “Permanents of (1,-1)-matrices”. In: Proceedings of the Topology and Geometry Research Center. Vol. 4. 1. 1993, pp. 151–204.
- [9] Matthew Kwan and Lisa Sauermann. “On the permanent of a random symmetric matrix”. In: Selecta Mathematica 28.1 (2022), p. 15.
- [10] Alain Lascoux and Piotr Pragacz. “Jacobians of symmetric polynomials”. In: Annals of Combinatorics 6.2 (2002), pp. 169–172.
- [11] La´szlo Lova´sz. Large Networks and Graph Limits. American Mathematical Society colloquium publications. American Mathematical Society, 2012.
- [12] Marvin Marcus and Morris Newman. “Inequalities for the permanent function”. In: Annals of Mathematics 75.1 (1962), pp. 47–62.
- [13] Henryk Minc. Permanents. Vol. 6. Cambridge University Press, 1984.
- [14] Henryk Minc. “Theory of permanents 1982–1985”. In: Linear and Multilinear Algebra 21.2 (1987), pp. 109–148. doi: 10.1080/03081088708817786. eprint: https: //doi.org/10.1080/03081088708817786. url: https://doi.org/10.1080/ 03081088708817786.
- [15] Hoi Nguyen and Van H Vu. “Optimal Inverse Littlewood-Offord theorems”. In: Advances in Mathematics 226.6 (2011), pp. 5298–5319.
- [16] Will Orrick (https://mathoverflow.net/users/484/will orrick). Maximum determinant of {0,1}-valued n×n-matrices. MathOverflow. URL:https://mathoverflow.net/q/39826 (version: 2019-01-16). eprint: https://mathoverflow.net/q/39826. url: https: //mathoverflow.net/q/39826.
- [17] Hazel Perfect. “Positive diagonals of ±1-matrices”. In: Monatshefte f¨ur Mathematik 77

(1973), pp. 225–240.

- [18] Simeon Reich. “Another solution of an old problem of Po´lya”. In: The American Mathematical Monthly 78.6 (1971), pp. 649–650.
- [19] Norbert Seifter. “Upper bounds for permanents of (1,- 1)-matrices”. In: Israel Journal of Mathematics 48 (1984), pp. 69–78.


- [20] Rikhav Shah. “Determinants of binary matrices achieve every integral value up to Ω(2n/n)”. In: Linear Algebra and its Applications 645 (2022), pp. 229–236.
- [21] Terence Tao and Van Vu. “On the permanent of random Bernoulli matrices”. In: Advances in Mathematics 220.3 (2009), pp. 657–669.
- [22] Terence Tao and Van H Vu. Additive combinatorics. Vol. 105. Cambridge University Press, 2006.
- [23] Van H Vu. Recent progress in combinatorial random matrix theory. 2020. arXiv: 2005. 02797 [math.CO]. url: https://arxiv.org/abs/2005.02797.
- [24] Edward T Wang. “On permanents of (1,- 1)-matrices”. In: Israel Journal of Mathematics 18 (1974), pp. 353–361.
- [25] Ian M Wanless. “Permanents of matrices of signed ones”. In: Linear and Multilinear Algebra 53.6 (2005), pp. 427–433.


