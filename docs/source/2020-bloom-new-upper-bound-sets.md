---
type: source
kind: paper
title: A new upper bound for sets with no square differences
authors: Thomas F. Bloom, James Maynard
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2011.13266v2
source_local: ../raw/2020-bloom-new-upper-bound-sets.pdf
topic: general-knowledge
cites:
---

arXiv:2011.13266v2[math.NT]24Feb2021

A NEW UPPER BOUND FOR SETS WITH NO SQUARE DIFFERENCES

THOMAS F. BLOOM AND JAMES MAYNARD

Abstract. We show that if A ⊂ {1, . . . , N} has no solutions to a − b = n2 with a, b ∈ A and n ≥ 1 then

N (log N)clog loglog N for some absolute constant c > 0. This improves upon a result of Pintz-SteigerSzemer´edi.

|A| ≪

![image 1](<2020-bloom-new-upper-bound-sets_images/imageFile1.png>)

1. Introduction

Answering a question of Lov´asz, Sa´rk¨ozy [14] and Furstenberg [5] independently showed that any set of integers whose diﬀerence set contains no non-zero squares must have asymptotic density zero. Sa´rk¨ozy’s proof was based on the circle method, and actually gave the quantitative bound that if A ⊆ {1,...,N} has no non-zero square diﬀerences then |A| ≤ N/(log N)1/3+o(1), whereas Furstenberg’s result relied on ergodic theory. There have since been a variety of proofs of the qualitative result |A| = o(N); we refer the reader to the introduction of [11] for more details.

Sa´rk¨ozy’s argument was reﬁned by Pintz, Steiger, and Szemer´edi [10] who improved the upper bound on the size of A ⊆ {1,...,N} with no non-zero square diﬀerences to

N (log N)clog loglog logN

(1) |A| ≪

![image 2](<2020-bloom-new-upper-bound-sets_images/imageFile2.png>)

for some absolute constant c > 0. (Here we use Vinogradov’s notation X ≪ Y to mean that X ≤ CY for some absolute constant C > 0.) One interesting feature of

- (1) is that it is a noticeably stronger bound than what is currently known for Roth’s Theorem on three term arithmetic progressions [3], despite both proofs following a Fourier-analytic density increment argument.


In this paper we improve the upper bound (1) for the size of sets of integers with no square diﬀerences.

- Theorem 1. Let N be suﬃciently large. If A ⊂ {1,...,N} has no solutions to a − b = n2 with a,b ∈ A and n ≥ 1, then


N (log N)clog log logN for some absolute constant c > 0.

|A| ≪

![image 3](<2020-bloom-new-upper-bound-sets_images/imageFile3.png>)

Our proof of Theorem 1 follows a Fourier-analytic density increment argument

- as with previous approaches, but is actually more direct (and, we hope, simpler) than the approach of Pintz-Steiger-Szemer´edi. The key new tool in our work is an upper bound for the additive energy of sets of rationals with small denominator,


1

which may be of independent interest. To state this we recall that the 2m-fold additive energy of a set B is given by

E2m(B) := |{(b1,...,b2m) ∈ B2m : b1 + ··· + bm = bm+1 + ··· + b2m}|. We also introduce the notation

a q

∈ [0,1] : 1 ≤ a ≤ q and gcd(a,q) = 1 ,

Q=q :=

![image 4](<2020-bloom-new-upper-bound-sets_images/imageFile4.png>)

Q≤Q :=

Q=q,

1≤q≤Q

to denote the set of reduced rationals in [0,1] with denominator precisely q, and for the set of all rationals with denominator at most Q. Our additive energy result is then the following.

- Theorem 2. Let Q ≥ 4 and m ≥ 2. Suppose that B ⊂ Q≤Q is such that there is n ≥ 1 with |B ∩ Q=q| ≤ n for any 1 ≤ q ≤ Q. Then we have


m

(Qn)m for some absolute constant C > 0.

E2m(B) ≤ (log Q)C

We note that there is a trivial lower bound E2m(B) ≥ |B|m from diagonal solutions where bi = bi+m for 1 ≤ i ≤ m. If B contains n rationals with denominator q for each q ∈ [Q/2,Q] then |B| ≫ nQ and we see that Theorem 2 gives an upper bound of the form |B|m(log |B|)C

m

, and so the contribution from the diagonal terms is comparable to the whole contribution. Thus sets of rationals with small distinct denominators have similar additive energy estimates to dissociated sets where the only solutions to b1 + ··· + bm = bm+1 + ··· + b2m are the diagonal ones.

Dissociated sets have been used in additive combinatorics since at least the work of Chang [4], and Theorem 2 allows one to extend Chang’s ideas to sets whose large Fourier coeﬃcients are close to rationals with small denominators, as is the situation in the Furstenberg-Sa´rk¨ozy problem. The original argument of PintzSteiger-Szemer´edi can be viewed as showing that there is a lack of additive structure in the rationals which make up the large Fourier coeﬃcients, but Theorem 2 allows for a more eﬃcient and direct use of this idea. Indeed, the original argument of

- [10] proves (implicitly) a lower bound for the size of the m-fold sumset, namely


something of the strength of |mB| ≫m,ǫ |B|m−ǫ, which follows from Theorem 2 and |mB| ≫ |B|2m/E2m(B). An important feature of Theorem 2 for our work is that it remains non-trivial even with m as large as a small multiple of log log Q.

Clearly one can have sets B ⊂ Q≤Q with large additive energy if many elements of B have the same denominator, and so the restriction |B ∩ Q=q| ≤ n is natural for this problem.

Other results and generalizations. For comparison, the best known lower bound for the size r(N) of the largest set A ⊂ {1,...,N} with no non-zero square diﬀerences is much smaller than the upper bound in Theorem 1. Ruzsa [12] gives a construction that shows in particular that r(N) ≫ N0.73. The constant in the exponent here has been slightly improved by Lewko [7], but even whether r(N) ≫ N3/4 is open. We do not know where the truth lies, and whether the true order of magnitude of r(N) is N1−o(1) or N1−c for some absolute constant c > 0 remains a fascinating open problem.

For the analogous problem in the function ﬁeld case, where Z is replaced by the polynomial ring Fq[t] over some ﬁnite ﬁeld Fq, much stronger quantitative bounds are known. Using the polynomial method, Green [6] has recently shown that if

- A ⊂ Fq[t]deg<n contains no non-zero square diﬀerences then


- (2) |A| ≪ q(1−c(q))n,


where c(q) > 0 is some constant depending only on q. Since Fq[t]deg<n has size qn, this bound is analogous to a bound of the shape r(N) ≪ N1−c in the integer case. The polynomial method used by Green is very diﬀerent to the analytic arguments used in this paper, and depends in a fundamental way on the bounded characteristic of Fq[t].

The method of Pintz, Steiger, and Szemer´edi [10] has been generalised to yield a similar bound for related problems. This was done for sets without diﬀerences of the form nk for any ﬁxed k ≥ 3 by Balog, Pelikan, Pintz, and Szemer´edi [1], and then recently by Rice [11] to diﬀerences of the form f(n) where f ∈ Z[x] is any intersective polynomial1 of degree at least 2. These proofs directly extend the method of [10], and as such it seems likely that one could combine the ideas of [1] and

- [11] with those in this paper to obtain a quantitative bound of strength comparable to Theorem 1 for these generalisations; we do not address these questions here.


Recent work of the second author [8] showed that any system of polynomials simultaneously attain values with small fractional parts. There are various similarities with this work (a density increment argument enhanced by there being few solutions to linear equations involving rationals with small denominator), but there the problem was more structured which allowed for an almost optimal bound of the form x1−c, whereas in this situation we are forced to consider much more arbitrary sets A.

An upper bound for the additive energy of sets of well-distributed rationals similar (qualitatively) to Theorem 2 has also been applied within theoretical computer science, where it was used by Bourgain, Dilworth, Ford, Konyagin, and Kutzarova [2] to construct matrices satisfying the Restricted Isometry Property. It follows from their Lemma 5, for example, that if B ⊂ Q≤Q is such that for any 1 ≤ q ≤ Q we have |B ∩ Q=q| ≤ 1, then, for any ǫ > 0, we have E2m(B) ≪m,ǫ Qǫ |B|m, where the dependence on m and ǫ is unspeciﬁed. It is vital for our purposes that we explicitly control the dependence on m and ǫ.

Acknowledgements. T.B. would like to thank Julia Wolf for many helpful discussions regarding the original proof of Pintz, Steiger, and Szemer´edi (and recommends the ﬁrst chapter of [15] for a very readable exposition), and would also like to thank Alex Rice for pointing out an error in an earlier draft of this paper. J.M. would like to thank Ben Green for introducing him to this question. T.B. was supported by a postdoctoral grant funded by the Royal Society. J.M. was supported by a Royal Society Wolfson Merit Award, and funding from the European Research Council (ERC) under the European Union’s Horizon 2020 research and innovation programme (grant agreement No 851318).

![image 5](<2020-bloom-new-upper-bound-sets_images/imageFile5.png>)

1A polynomial f ∈ Z[x] is intersective if it is non-zero and for every q ∈ N there is n ∈ Z such that q | f(n).

2. Outline

In this section we sketch how Theorem 2 can be used to give Theorem 1. As mentioned in the introduction, our proof is similar to the original work of Sa´rk¨ozy [14] (and its later reﬁnements) in that we base our argument on a density increment argument coming out of the circle method. Our Theorem 2 allows us to show that no set A can have many large Fourier coeﬃcients which are rationals with small distinct denominators, and this is the key which allows us to have a more eﬃcient density increment argument than that of [10].

First we recall the basic setup. If A ⊂ {1,...,N} has no non-zero square diﬀerences and density α = |A|/N, then by the circle method

0 = |{(a1,a2,n) : a1 − a2 = n2, a1,a2 ∈ A, 1 ≤ n ≤ N1/2}|

1

| 1A(γ)|2 1 (γ)dγ,

=

0

where 1A(γ) = a∈A e(aγ) is the Fourier transform of the set A, and similarly 1 is the Fourier transform of squares in [1,N]. Comparing this to α2N3/2, which is the expected count of solutions in a random set of density α, we ﬁnd

1

| gA(γ)|2| 1 (γ)|dγ ≫ α2N3/2,

0

where gA = 1A − α1[N] is the balanced function of A. If γ ≈ a/q then | 1 (γ)| ≈ N1/2/q1/2, and so by the pigeonhole principle there must be some Q for which

α2NQ1/2 (log Q)2

| gA(γ)|2dγ ≫

,

![image 6](<2020-bloom-new-upper-bound-sets_images/imageFile6.png>)

γ≈a/q Q≤q≤2Q

In particular there must be some parameter B such that there are ‘many’ (≫ Q1/2B2/(log Q)3) rationals of a/q with q ∈ [Q,2Q] for which gA(a/q) is large (≫ |A|/B). Parseval’s bound implies that this can only happen if Q ≤ α−O(1), and so these rationals have small denominators. The basic density increment strategy is then to deduce that this implies that there is a large arithmetic progression on which A has density α + ρα (for some suitable ρ > 0), so this argument can then be iterated.

If there were at least ρ2B2 diﬀerent rationals γ with the same denominator q where | gA(γ)| ≫ |A|/B, then the existence of such an arithmetic progression follows from

ρ2|A|2 q

2

2

|A| q

c q

1 q

|{a ∈ A : a ≡ b (mod q)}| −

gA

=

≫

.

![image 7](<2020-bloom-new-upper-bound-sets_images/imageFile7.png>)

![image 8](<2020-bloom-new-upper-bound-sets_images/imageFile8.png>)

![image 9](<2020-bloom-new-upper-bound-sets_images/imageFile9.png>)

![image 10](<2020-bloom-new-upper-bound-sets_images/imageFile10.png>)

b (mod q)

c (mod q)

Thus we may assume that for any q ∈ [Q,2Q] there are O(ρ2B2) rationals γ with denominator q where | gA(γ)| ≫ |A|/B. So far our approach has followed previous works, but now we note that if B is this set of rationals with | gA(b)| ≫ |A|/B, then a variation of the proof of Chang’s lemma shows roughly that for any choice of m ≥ 1

|A| · |B| B

≪

![image 11](<2020-bloom-new-upper-bound-sets_images/imageFile11.png>)

| gA(b)| ≤ |A|1−1/2mN1/2mE2m(B)1/2m.

b∈B

In particular, there cannot be a large set B with very small additive energy whilst also having the Fourier transform gA of A large on all elements of B. We can now apply Theorem 2 to bound E2m(B), since B is a set of rationals of small denominator with O(ρ2B2) elements having any given denominator. This rearranges to give (for any choice of m)

m

Q1/2B2. This contradicts the lower bound |B| ≫ Q1/2B2/(log Q)3 if

|B| ≪ ρα−1/2m(log Q)C

α1/2m (log Q)Cm+3

ρ ≈

.

![image 12](<2020-bloom-new-upper-bound-sets_images/imageFile12.png>)

Choosing m = c log log(1/α) for some suitably small constant c > 0 and recalling Q ≪ α−O(1), this implies that there is an arithmetic progression P ⊆ {1,...,N} with |P| ≥ αO(1)N on which A has density α(1 + ρ), where

log 1/α log log 1/α

ρ ≈ exp −C

![image 13](<2020-bloom-new-upper-bound-sets_images/imageFile13.png>)

for some absolute constant C > 0. Iterating this statement then gives Theorem 1.

Theorem 2 is established using a quite separate argument. Although it can be deduced from a direct combinatorial approach based on splitting according to suitable greatest common divisors we use an iterative argument which we hope is cleaner.

3. Notation

We begin by establishing the basic notation that we will use. For any N ≥ 1 we use [N] to denote the set {1,...,N}. We ﬁx throughout our proof some large integer N (large enough in particular such that log log log N ≥ 4, say). For functions f : Z → C we deﬁne the Fourier transform f : [0,1] → C by

f(γ) =

f(n)e(γn),

n∈Z

where e(x) = e2πix. We deﬁne the convolution of two functions f,g : Z → C by (f ∗ g)(n) =

f(m)g(n − m)

m∈Z

and use f(∗m)(x) = (f ∗ ··· ∗ f)(x) to denote the m-fold iterated convolution of f. Without subscript, the notation γ denote the distance of γ ∈ R from the nearest integer, while f 2 = ( x∈Z |f(x)|2)1/2 and f ∞ = supx∈Z |f(x)| denotes the usual L2 and L∞ norms.

We write τ3(n) to denote the ternary divisor function abc=n 1.

4. Addition of rational numbers and the proof of Theorem 2

In this section we prove Theorem 2. This section is essentially self-contained and can be read independently of the rest of the paper.

Theorem 2 follows quickly from the more technical Proposition 1. To state this we require some more notation. For any function ω : N → R we deﬁne the maximal average function of ω by

1 x n≤x

ω(n),

- (3) M(ω;X) := max 1≤x≤X


![image 14](<2020-bloom-new-upper-bound-sets_images/imageFile14.png>)

and the logarithmic maximal average by

ω(n) n

1 log x n≤x

.

- (4) Mlog(ω;X) := max 2≤x≤X


![image 15](<2020-bloom-new-upper-bound-sets_images/imageFile15.png>)

![image 16](<2020-bloom-new-upper-bound-sets_images/imageFile16.png>)

We recall that τ3(n) is the ternary divisor function abc=n 1. Our technical bound on the additive energy is the following.

Proposition 1 (Rationals with small denominators have small additive energy). Let m ≥ 2. Suppose that B ⊂ Q≤Q and n ≥ 1 is such that for any 1 ≤ q ≤ Q we have |B ∩ Q=q| ≤ n. Then we have the upper bound

E2m(B) ≤ (mlog QMlog(τ32m;Q))O(m)M(τ32m−2;Q)(Qn)m.

Proof of Theorem 2 assuming Proposition 1. By Rankin’s trick, we have the standard divisor function bound

−3k

1 p

k

M(τ3k;X) ≪ (log X)Mlog(τ3k;X) ≪

≪ (log X)3

1 −

.

![image 17](<2020-bloom-new-upper-bound-sets_images/imageFile17.png>)

p≤x

Therefore Proposition 1 gives E2m(B) ≪ mO(m)(log Q)O(m9

m)(Qn)m. Simplifying the exponents gives Theorem 2.

Proposition 1 will be proved via an iterative application of the following lemma. Roughly speaking, it says that if B ⊂ Q≤L is spread evenly between diﬀerent denominators, then for any sets A,C we have 1A, 1B ∗ 1C ≪ (|A||B||C|)1/2. This should be compared to the trivial bound of (|A||C|)1/2 |B|. To attain the quantitative strength of Theorem 1 we will take care to prove an explicit weighted form of this inequality. To state this lemma precisely we make the following deﬁnition.

Deﬁnition 1. An arithmetic function ω : N → R≥0 is sub-multiplicative if ω(ab) ≤ ω(a)ω(b) for all a,b ∈ N and whenever d | n we have ω(d) ≤ ω(n).

- Lemma 1 ((Few solutions to linear equations in rationals with small denominators)). Let Z ≥ 1 be some integer. Let A ⊂ Q ∩ (0,Z] and C ⊂ Q. Suppose that


- B ⊂ Q≤Q is such that, for any 1 ≤ ℓ ≤ Q, we have |B ∩ Q=ℓ| ≤ n. Let ω : N → R≥0 be some sub-multiplicative function. Then


 

 QnZ(logQ)Mlog(ωτ3;Q)

1/2

′

′

′

ω(q)τ3(q)2

ω(k)

ω(k) ≪

.

a/k−b/ℓ=c/q a/k∈A, b/ℓ∈B, c/q∈C

a/k∈A

c/q∈C

Here we use ′ to indicate that the fractions a/k,b/ℓ,c/q are all reduced (i.e.

- gcd(a,k) = gcd(b,ℓ) = gcd(c,q) = 1).


We note that the summation on the left hand side in Lemma 1 can also be

written as x∈C( ω1A ∗ 1−B)(x), where ω(a/q) = ω(q) for gcd(a,q) = 1. If ω ≈ 1 and |B| ≈ Qn then since τ3 is typically quite small the bound on the right hand side is roughly of size (|A||B||C|)1/2.

Proof. Throughout the proof we use ′ to indicate that the fractions in the summation are reduced.

We claim that for any choice of parameter T > 0, there is a decomposition of

- A × B into two sets E1 and E2 such that, if we let


′

Fi(x) :=

ω(k)1a/k−b/ℓ=x,

(a/k,b/ℓ)∈Ei

then we have

- (5)

′

c/q∈C

F1

c q

![image 18](<2020-bloom-new-upper-bound-sets_images/imageFile18.png>)

≤

QnZ log Q T

![image 19](<2020-bloom-new-upper-bound-sets_images/imageFile19.png>)

Mlog(ωτ3;Q)

′

c/q∈C

ω(q)τ3(q)2

and

- (6)


′

F2

c/q∈C

c q

![image 20](<2020-bloom-new-upper-bound-sets_images/imageFile20.png>)

′

ω(k).

≤ T

a/k∈A

The lemma now follows from this claim by choosing

  

  

1/2

′

ω(q)τ3(q)2 ′

QnZ(logQ)Mlog(ωτ3;Q)

c/q∈C

,

T =

![image 21](<2020-bloom-new-upper-bound-sets_images/imageFile21.png>)

ω(k)

a/k∈A

since

ω(k) = ′ c/q∈C

′

(F1(c/q) + F2(c/q)) .

a/k−b/ℓ=c/q a/k∈A, b/ℓ∈B, c/q∈C

Thus we are left to establish the claim by constructing the sets E1 and E2. We consider the complete bipartite graph G with vertex sets A and B. We ﬁrst colour the edges of G by giving the edge (a/k,b/ℓ) ∈ A × B the colour C(a/k,b/ℓ) = (d,f) ∈ Z2, where

d = gcd(k,ℓ) and f = gcd

aℓ − bk d

,d .

![image 22](<2020-bloom-new-upper-bound-sets_images/imageFile22.png>)

We then say that the colour (d,f) is ‘popular at a/k’ if |{b/ℓ ∈ B : C(a/k,b/ℓ) = (d,f)}| ≥

T τ3(k)

.

![image 23](<2020-bloom-new-upper-bound-sets_images/imageFile23.png>)

We say that an edge (a/k,b/ℓ) ∈ A × B is ‘popular’ if its colour is popular at a/k, then let E1 ⊂ A × B be the set of all popular edges, and let E2 be the remaining edges (A × B)\E1.

The bound in (6) now follows easily. Indeed, if a/k ∈ A has an edge coloured (d,f) connected to a/k then f|d|k, so there are at most τ3(k) possible diﬀerent colours of edges connected to a/k. Since E2 only consists of the edges which are not popular, for any colour (d,f) there are at most T/τ3(k) vertices b/ℓ connected to a/k by an edge of colour (d,k). Thus there are at most T vertices b/ℓ in B connected to any given vertex in A by an edge in E2, and so

ω(k) ′ b/ℓ∈B

F2(c/q) ≤ ′

′

1(a/k,b/ℓ)∈E

2

a/k∈A

c/q∈C

≤ T ′

ω(k).

a/k∈A

This gives (6).

It remains to establish (5). Given a choice of d,f and k, let Rd,f,k count the number of distinct possibilities for a (mod f) such that the colour (d,f) is popular

- at some a/k ∈ A. We will ﬁrst show that, for any pair (d,f) and k, we have


- (7) Rd,f,k ≤

Qn dT

![image 24](<2020-bloom-new-upper-bound-sets_images/imageFile24.png>)

τ3(k).

Let Ad,f,k ⊂ A be some subset representing the Rd,f,k diﬀerent possibilities. Therefore

- (1) The colour (d,f) is popular at each a/k ∈ Ad,f,k.
- (2) If a/k,a′/k ∈ Ad,f,k then a  ≡ a′ (mod f).
- (3) For each a′/k ∈ A such that (d,f) is popular at a′/k, there is a/k ∈ Ad,f,k such that a ≡ a′ (mod f).
- (4) Rd,f,k = |Ad,f,k|.


By the deﬁnition of edges being popular at a/k, we have

Rd,f,k

T τ3(k)

![image 25](<2020-bloom-new-upper-bound-sets_images/imageFile25.png>)

≤ ′

a/k∈Ad,f,k

′

b/ℓ∈B C( ak , bℓ )=(d,f)

![image 26](<2020-bloom-new-upper-bound-sets_images/imageFile26.png>)

![image 27](<2020-bloom-new-upper-bound-sets_images/imageFile27.png>)

1.

The key observation is that each b/ℓ ∈ B appears at most once in total on the right-hand side, since if C(a1/k,b/ℓ) = C(a2/k,b/ℓ) = (d,f), then we must have

gcd

a1ℓ − bk d

![image 28](<2020-bloom-new-upper-bound-sets_images/imageFile28.png>)

,d = gcd

a2ℓ − bk d

![image 29](<2020-bloom-new-upper-bound-sets_images/imageFile29.png>)

,d = f, gcd(k,ℓ) = d.

In particular a1ℓ/d ≡ a2ℓ/d (mod f). Since gcd(ℓ,k) = d, we see that gcd(ℓ/d,f) = 1, and so a1 ≡ a2 (mod f). It follows that

Rd,f,k

T τ3(k)

![image 30](<2020-bloom-new-upper-bound-sets_images/imageFile30.png>)

≤

ℓ≤Q d|l

|B ∩ Q=ℓ| ≤

nQ d

![image 31](<2020-bloom-new-upper-bound-sets_images/imageFile31.png>)

,

and the estimate (7) follows immediately.

We now establish (5) by bounding F1(c/q) for each c/q separately. Given a choice of c/q (with gcd(c,q) = 1) we see that if a,k,b,ℓ are such that gcd(a,k) =

- gcd(b,ℓ) = 1 and c


![image 32](<2020-bloom-new-upper-bound-sets_images/imageFile32.png>)

q

=

a k

![image 33](<2020-bloom-new-upper-bound-sets_images/imageFile33.png>)

−

b ℓ

![image 34](<2020-bloom-new-upper-bound-sets_images/imageFile34.png>)

, then q = ℓ′k′e and c = (aℓ′ − bk′)/f, where

k′ =

k gcd(k,ℓ)

![image 35](<2020-bloom-new-upper-bound-sets_images/imageFile35.png>)

, ℓ′ =

ℓ gcd(k,ℓ)

![image 36](<2020-bloom-new-upper-bound-sets_images/imageFile36.png>)

, gcd(k,ℓ) = ef, f = gcd(aℓ′ − bk′,gcd(k,ℓ)).

Thus, given a choice of c,k′,ℓ′,e,f with k′ℓ′e = q and 1 ≤ f ≤ Q, there is a unique choice of k = k′ef and ℓ = ℓ′ef. Moreover, aℓ′ ≡ cf (mod k′), so a is ﬁxed modulo k′. There are at most e choices of a (mod e) and at most Ref,f,k′ef choices of a (mod f), so at most eRef,f,k′ef choices of a (mod k). If we then ﬁx the integer part of a/k, of which there are at most Z choices, then we have determined a. Given such a choice of a, b is uniquely determined since b = ℓ(c/q−a/k). It follows that

- (8) F1(c/q) ≤ Z k′ℓ′e=q 1≤f≤L


ω(k′ef)eRef,f,k′ef.

Using (7) and the sub-multiplicativity of ω and τ3, this is bounded above by QnZ T k

QnZ log Q T

ω(f)τ3(f) f

Mlog(ωτ3;Q)ω(q)τ3(q)2.

ω(k′e)τ3(k′e)

≤

![image 37](<2020-bloom-new-upper-bound-sets_images/imageFile37.png>)

![image 38](<2020-bloom-new-upper-bound-sets_images/imageFile38.png>)

![image 39](<2020-bloom-new-upper-bound-sets_images/imageFile39.png>)

′ℓ′e=q

1≤f≤Q

Summing this over c/q ∈ C then gives (5), and so completes the proof.

We will actually use a weighted version of Lemma 1, which follows immediately by a dyadic decomposition of the support of the weights.

- Lemma 2. Let Z ≥ 1 be some integer. Let f : Q → Z≥0 and g : Q∩(0,Z] → Z≥0 be


functions with ﬁnite support such that f ∞ , g ∞ ≤ X. Suppose that B ⊂ Q≤Q is such that, for any 1 ≤ ℓ ≤ Q, we have |B ∩ Q=ℓ| ≤ n. Then, for any submultiplicative function ω : N → R≥0,

′

ω(k)g

a/k−b/ℓ=c/q b/ℓ∈B

a k

![image 40](<2020-bloom-new-upper-bound-sets_images/imageFile40.png>)

f

c q

![image 41](<2020-bloom-new-upper-bound-sets_images/imageFile41.png>)

≪ C

′

ω(q)τ3(q)2f

c/q∈C

c q

![image 42](<2020-bloom-new-upper-bound-sets_images/imageFile42.png>)

2

1/2

′

ω(k)g

a/k∈A

a k

![image 43](<2020-bloom-new-upper-bound-sets_images/imageFile43.png>)

2

1/2

,

where

C := (log X) QnZ(logQ)Mlog(ωτ3;Q)

1/2

.

Here we use ′ to indicate that the fractions a/k,b/ℓ,c/q are all reduced (i.e. gcd(a,k) = gcd(b,ℓ) = gcd(c,q) = 1).

Proof of Lemma 2. We decompose the support of f into Cj for j ≥ 0, where Cj = {x : 2j ≤ f(x) < 2j+1},

and similarly decompose the support of g into Ai. Using this decomposition we have

a k

c q

′

′

2i+j

ω(k)g

ω(k).

f

≪

![image 44](<2020-bloom-new-upper-bound-sets_images/imageFile44.png>)

![image 45](<2020-bloom-new-upper-bound-sets_images/imageFile45.png>)

0≤i,j≤log X

a/k−b/ℓ=c/q b/ℓ∈B

a/k−b/ℓ=c/q a/k∈Ai, b/ℓ∈B, c/q∈Cj

Applying Lemma 1 to each summand gives the upper bound

 QnZ(logQ)Mlog(ωτ3;Q)

 

1/2

′

′

2i+j

ω(q)τ3(q)2

≪

ω(k)

.

0≤i,j≤log X

c/q∈Cj

a/k∈Ai

- Lemma 2 now follows by the Cauchy-Schwarz inequality. The proof of Proposition 1 may now proceed via induction.


Proof of Proposition 1. Again, we use ′ to indicate that the summation is restricted to reduced fractions. We will show that, for any t ≥ 0 and 1 ≤ j ≤ m, we have

τ3(q)2t1(B∗j)(c/q)2 ≪ (mlog Q)3(QnM2t+1) ′ c/q∈Q

- (9) ′


τ3(q)2t+21(B∗j−1)(c/q)2,

c/q∈Q

where we recall 1B(∗m)(x) = x

1+···+xm=x 1B(x1)···1B(xm) is the m-fold convolution of 1B, and where

Mt := Mlog(τ3t;Q).

Repeatedly applying (9) m − 1 times gives E2m(B) =

′

1B(∗m)(c/q)2

c/q∈Q

≪ (mlog Q)3(m−1)(Qn)m−1(M1 ···M2m−3)

c/q∈Q

′

τ3(q)2m−21B(c/q)2.

Since |B ∩ Q=q| ≤ n, we have

′

τ3(q)2m−21B(c/q)2 ≤ n

c/q∈Q

τ3(q)2m−2 = nQM(τ32m−2;Q).

1≤q≤Q

Noting that Mt ≤ M2m = Mlog(τ32m;Q) for each t ≤ 2m, this completes the proof of Proposition 1. Thus we are left to establish (9).

We ﬁrst observe that, since 1(B∗j)(c/q) = b/ℓ∈B 1(B∗j−1)(c/q − b/ℓ), we have

′

′

τ3(q)2t1(B∗j)(c/q)1(B∗j−1)(c′/q′).

τ3(q)2t1(B∗j)(c/q)2 =

c/q=c′/q′+b/ℓ b/ℓ∈B

c/q∈Q

We let f(x) := 1(B∗j−1)(x) and g(x) := 1(B∗j)(x), so that in particular g is supported on jB. Since B ⊂ (0,1] we know that g is supported on (0,j]. Furthermore, since

- B ⊂ Q≤Q we have |B| ≤ Q2 so f ∞, g ∞ ≤ Q2j. We now apply Lemma 2 with ω(q) = τ3(q)2t. This gives the upper bound


τ3(q)2t1(B∗j)(c/q)2 = ′

′

ω(q)g(c/q)f(c′/q′)

c/q=c′/q′+b/ℓ b/ℓ∈B

c/q∈Q

  ′

 

 

1/2 

1/2

c′ q′

2

2

c q

 ′ c/q∈Q

τ3(q′)2t+2f

≪ (mlog Q)3/2(QnM2t+1)1/2

τ3(q)2tg

.

![image 46](<2020-bloom-new-upper-bound-sets_images/imageFile46.png>)

![image 47](<2020-bloom-new-upper-bound-sets_images/imageFile47.png>)

c′/q′∈Q

The left hand side is c/q∈Q τ3(q)2tg(c/q)2, so this rearranges to give the claimed bound (9).

5. Basic density Increment

In this section we establish a simple L2 density increment lemma, which says that if there are many large Fourier coeﬃcients which are close to rationals with the same denominator, then one can ﬁnd a large arithmetic progression on which the set has increased density. Statements of this type are standard, and our lemma only diﬀers cosmetically from similar statements used in [10] or [13]. It may be helpful to bear in mind that this will be applied with some q,K ≪ α−O(1) and ν ≫ αo(1) (where the o(1) → 0 as α → 0).

We introduce the notation

M(aq;N,K) := {γ ∈ (0,1] : γ − a/q ≤ K/qN} to denote the major arcs which appear in the circle method. Note that these major arcs are disjoint for distinct a/q ∈ Q=q provided K < N/2.

![image 48](<2020-bloom-new-upper-bound-sets_images/imageFile48.png>)

- Lemma 3 (Large Fourier coeﬃcents with the same denominator give density increment). Let ν,α ∈ (0,1] and let N,K,q ≥ 1 be such that K < N/2 and ναN/(Kq2) is suﬃciently large. Let A ⊂ [N] be a set with no non-zero square diﬀerences and density α = |A|/N, and


a q ∈Q=q M( aq ;N,K)

![image 49](<2020-bloom-new-upper-bound-sets_images/imageFile49.png>)

![image 50](<2020-bloom-new-upper-bound-sets_images/imageFile50.png>)

2

1A(γ) − α 1[N](γ)

dγ ≥ να |A|.

Then there exists N′ ≫ ναN/(Kq2) and a set A′ ⊂ [N′] with no non-zero square diﬀerences such that the density α′ = |A′|/N′ satisﬁes

α′ ≥ (1 + ν/5)α.

Proof. Let P = (q2) · [N′] be an arithmetic progression of diﬀerence q2 and length N′, for some N′ to be chosen later. If γ ∈ M(a/q;N,K) for some a/q then for any

- 1 ≤ n′ ≤ N′ we have


q2N′K qN

1 − e(γq2n′) ≪ γq2n′ ≤ γq2n′ − aqn′ = q2n′ |γ − a/q| ≤

.

![image 51](<2020-bloom-new-upper-bound-sets_images/imageFile51.png>)

(We recall that  ·  is the distance to the nearest integer.) In particular we can ensure that 1 − e(γq2k) ≤ 1/2 provided we have

cN qK

- (10) N′ ≤


![image 52](<2020-bloom-new-upper-bound-sets_images/imageFile52.png>)

for some suﬃciently small absolute constant c > 0. Thus if γ ∈ M(a/q;N,K) and

- (10) holds,

1P(γ) − N′ ≤

1≤n′≤N′

1 − e(γq2n′) ≤ N′/2,

and so | 1P(γ)| ≥ N′/2. Let g = 1A − α1[N] be the balanced function of A. It follows that (using the assumption of the lemma)

x∈Z

(1P ∗ g)(x)2 =

1

0

| 1P(γ)|2 | g(γ)|2 dγ ≥

(N′)2 4

![image 53](<2020-bloom-new-upper-bound-sets_images/imageFile53.png>)

a q ∈Q=q M( aq ;N,K)

![image 54](<2020-bloom-new-upper-bound-sets_images/imageFile54.png>)

![image 55](<2020-bloom-new-upper-bound-sets_images/imageFile55.png>)

| g(γ)|2 dγ

≥

να(N′)2 |A| 4

![image 56](<2020-bloom-new-upper-bound-sets_images/imageFile56.png>)

- (11) . On the other hand, recalling that g = 1A − α1[N], the left-hand side is equal to
- (12) 1P ∗ 1A 22 − 2α x∈Z

(1P ∗ 1A)(x) · (1P ∗ 1[N])(x) + α2 1P ∗ 1[N] 22 . The third term of (12) trivially satisﬁes

- (13) α2 1P ∗ 1[N] 22 ≤ α2N |P|2 = α|A| (N′)2. For the second term of (12), we note that


(1P ∗ 1−P ∗ 1[N])(x) − (N′)21[N](x) ≤

x∈Z

(1P ∗ 1−P)(y)

y∈Z

x∈Z

1[N](x − y) − 1[N](x)

≪

(1P ∗ 1−P)(y)|y|

y∈Z

≪ q2(N′)3.

In particular,

(1P ∗ 1A)(x) · (1P ∗ 1[N])(x) =

1P ∗ 1−P ∗ 1[N](y)

x∈Z

y∈A

- (14) = |A|(N′)2 + O(q2(N′)3). By substituting (13) and (14) into (12), we have

1P ∗ 1A 22 ≥ 2α |A| (N′)2 + O(q2(N′)3) − α |A|(N′)2 +

να(N′)2 |A| 4

![image 57](<2020-bloom-new-upper-bound-sets_images/imageFile57.png>)

. Provided we have

- (15) N′ ≤


cναN q2

![image 58](<2020-bloom-new-upper-bound-sets_images/imageFile58.png>)

for some suﬃciently small constant c > 0, we see that the O(q2(N′)3) term contributes at most να |A|(N′)2/100 in total, and so

ν 5

1P ∗ 1−A 22 = 1P ∗ 1A 22 ≥ 1 +

α |A|(N′)2.

![image 59](<2020-bloom-new-upper-bound-sets_images/imageFile59.png>)

Since 1P ∗ 1−A 1 = N′ |A| there exists some x ∈ Z such that (q2 · [N′]) ∩ (A + x) = 1P ∗ 1−A(x) ≥ 1 +

ν 5

αN′. Therefore, if we set

![image 60](<2020-bloom-new-upper-bound-sets_images/imageFile60.png>)

1 q2

A′ :=

· ((q2 · [N′]) ∩ (A + x)),

![image 61](<2020-bloom-new-upper-bound-sets_images/imageFile61.png>)

then A′ ⊂ [N′], A′ has density α′ ≥ (1 + ν/5)α and A′ has no non-zero square diﬀerences since translating a set by a constant or dilating a set by a square doesn’t change the number of non-zero square diﬀerences. This therefore gives the result with N′ = ⌊cναN/(Kq2)⌋ for a suitably small absolute constant c > 0 (since this choice satisﬁes (10) and (15) and N′ ≫ ναN/(Kq2)).

6. Large Fourier coefficients at rationals with small denominators

In this section we show how to ﬁnd many rationals with small denominator in the large spectrum of A (that is, the set of frequencies with large Fourier coeﬃcient). This follows standard lines, combining the circle method with classical bounds for Weyl sums.

- Lemma 4 (Bounds for exponential sums over squares). Let 1 ≤ a ≤ q with gcd(a,q) = 1 and


M(aq;N,K) := {γ ∈ (0,1] : γ − a/q ≤ K/qN}, W(n) :=

![image 62](<2020-bloom-new-upper-bound-sets_images/imageFile62.png>)

2m N1/2, if n = m2 ≤ N, 0, otherwise.

![image 63](<2020-bloom-new-upper-bound-sets_images/imageFile63.png>)

Then we have the following bounds:

- (1) For all β ∈ R we have


N1/2 q1/2

| W(a/q + β)| ≪

![image 64](<2020-bloom-new-upper-bound-sets_images/imageFile64.png>)

+ (q log q)1/2(1 + |β|N).

- (2) If Kq log q ≪ N and K3 log q ≪ qN then


1 q

| W(γ)|2 dγ ≪

.

![image 65](<2020-bloom-new-upper-bound-sets_images/imageFile65.png>)

a q ;N,K)

M(

![image 66](<2020-bloom-new-upper-bound-sets_images/imageFile66.png>)

Proof. This is standard. By [10, equation 8] (or partial summation) we have W(a/q + β) =

S(a;q) q

W(β) + O (q log q)1/2(1 + |β|N) ,

![image 67](<2020-bloom-new-upper-bound-sets_images/imageFile67.png>)

where S(a;q) := 1≤n≤q e(an2/q) is the complete Gauss sum. The classical estimate S(a;q) ≪ q1/2 for gcd(a,q) = 1 now gives (1). Using this estimate again, we ﬁnd

K/qN

K/qN

1 q

K log q N

| W(γ)|2 dγ ≪

+(q log q)N2

| W(β)|2 dβ+

β2 dβ.

![image 68](<2020-bloom-new-upper-bound-sets_images/imageFile68.png>)

![image 69](<2020-bloom-new-upper-bound-sets_images/imageFile69.png>)

a q ;N,K)

M(

0

0

![image 70](<2020-bloom-new-upper-bound-sets_images/imageFile70.png>)

The second and third summands contribute ≪

K3 q3N3

K log q N

+ (q log q)N2

≪

![image 71](<2020-bloom-new-upper-bound-sets_images/imageFile71.png>)

![image 72](<2020-bloom-new-upper-bound-sets_images/imageFile72.png>)

K log q N

![image 73](<2020-bloom-new-upper-bound-sets_images/imageFile73.png>)

K3 log q q2N

1 q

+

≪

![image 74](<2020-bloom-new-upper-bound-sets_images/imageFile74.png>)

![image 75](<2020-bloom-new-upper-bound-sets_images/imageFile75.png>)

by our assumptions on q and K. By [10, equation 10] and the trivial bound, if β ≤ N−7/8 then

β−1 N1/2

| W(β)| ≪ min N1/2,

.

![image 76](<2020-bloom-new-upper-bound-sets_images/imageFile76.png>)

(Note that this bound is slightly better than what one gets with the unweighted sum, but could be improved further with more smoothing.) This gives

- as required.


1 q

![image 77](<2020-bloom-new-upper-bound-sets_images/imageFile77.png>)

K/qN

1 q

| W(β)|2 dβ ≪

![image 78](<2020-bloom-new-upper-bound-sets_images/imageFile78.png>)

0

1 qN

+

![image 79](<2020-bloom-new-upper-bound-sets_images/imageFile79.png>)

K/qN

1 q

β−2 dβ ≪

,

![image 80](<2020-bloom-new-upper-bound-sets_images/imageFile80.png>)

1/10N

- Lemma 5. Let A ⊂ [N] be a set of density α = |A|/N ≥ N−1/8 with no square diﬀerences. Then there exist quantities B,Q,K with αO(1) ≪ B,Q,K ≪ α−O(1) and a set B ⊂ Q≤Q such that


- (1) For each a/q ∈ B there exists γa/q ∈ (0,1] with γa/q − a/q ≪ α−O(1)/N and

a q ∈B

![image 81](<2020-bloom-new-upper-bound-sets_images/imageFile81.png>)

| 1A(γa/q)| ≫ B

|A|Q1/2 log(1/α)2

![image 82](<2020-bloom-new-upper-bound-sets_images/imageFile82.png>)

.

- (2) For each a/q ∈ B we have, if g = 1A − α1[N],


α|A| B2

| g(γ)|2 dγ ≫

.

![image 83](<2020-bloom-new-upper-bound-sets_images/imageFile83.png>)

a q ;N,K)

M(

![image 84](<2020-bloom-new-upper-bound-sets_images/imageFile84.png>)

Proof. We ﬁrst note that, by the estimate of [14], say, we may assume that α ≪ 1/(logN)1/4 since A has no non-zero square diﬀerences. (This is not essential to the method, but allows for cleaner bounds in the ﬁnal statements.) Let

W(n) :=

2m N1/2 if n = m2 ≤ N and 0 otherwise.

![image 85](<2020-bloom-new-upper-bound-sets_images/imageFile85.png>)

By orthogonality and the fact that A has no non-zero square diﬀerences, we have

1

![image 86](<2020-bloom-new-upper-bound-sets_images/imageFile86.png>)

W(n2)

- 0
- 1A(γ) 1A(γ) W(γ)dγ = a,b∈A 1≤n≤N1/2


1

e(γ(a − b + n2))dγ

0

W(n2)1b−a=n2

=

a,b∈A 1≤n≤N1/2

= 0.

Suppose ﬁrst that |A ∩ (N/2,N]| ≥ |A|/2. In this case, if we let g = 1A − α1[N], then

1

1

![image 87](<2020-bloom-new-upper-bound-sets_images/imageFile87.png>)

e(γ(y − a + n2))dγ

W(n2)

g(γ) 1A(γ) W(γ)dγ = −α

0

0

a∈A 1≤y≤N 1≤n≤N1/2

W(n2)11≤a−n2≤N

= −α

a∈A 1≤n≤N1/2

≤ −18α|A| N1/2,

![image 88](<2020-bloom-new-upper-bound-sets_images/imageFile88.png>)

say, since certainly all a ∈ A∩(N/2,N] and n ≤ (N/2)1/2 will satisfy 1 ≤ a−n2 ≤ N. If |A ∩ [1,N/2]| ≥ |A|/2, then arguing similarly, we have

1

g(γ) 1A(γ) W(γ)dγ ≤ −18α|A|N1/2. Thus in either case, we have

![image 89](<2020-bloom-new-upper-bound-sets_images/imageFile89.png>)

![image 90](<2020-bloom-new-upper-bound-sets_images/imageFile90.png>)

0

- (16)

1

0

| g(γ) 1A(γ) W(γ)|dγ ≥ 81α |A|N1/2.

![image 91](<2020-bloom-new-upper-bound-sets_images/imageFile91.png>)

By Dirichlet’s theorem on Diophantine approximation, given any choice of K ≥ 1, every γ ∈ [0,1] satisﬁes γ − a/q < K/(Nq) for some 1 ≤ q ≤ N/K and 1 ≤ a ≤ q with gcd(a,q) = 1. If this holds for some q > K and K ≤ N1/2, say, then by Lemma 4,

| W(γ)| ≪

N(log N) K

![image 92](<2020-bloom-new-upper-bound-sets_images/imageFile92.png>)

1/2

. If we choose

- (17) K := ⌈Cα−2 log N⌉

for some suitably large absolute constant C > 0, then we see that | W(γ)| ≤ αN1/2/32 for such γ. The contribution to (16) from these γ is thus at most

αN1/2 32

![image 93](<2020-bloom-new-upper-bound-sets_images/imageFile93.png>)

1

0

| g(γ) 1A(γ)|dγ ≤

αN1/2 32

![image 94](<2020-bloom-new-upper-bound-sets_images/imageFile94.png>)

1

0

| 1A(γ)|2 dγ +

1

0

α 1[N](γ) 1A(γ) dγ

≤

α|A|N1/2 16

![image 95](<2020-bloom-new-upper-bound-sets_images/imageFile95.png>)

- (18) .


(Here we used the triangle inequality in the ﬁrst line, and the Cauchy-Schwarz inequality and Parseval’s identity in the second.) We recall that for gcd(a,q) = 1

M(a/q) = M(a/q;N,K) := {γ ∈ (0,1] : γ − a/q ≤ K/qN},

and note that with our choice K = ⌈Cα−2 log N⌉ these sets are distinct for q ≤ K and gcd(a,q) = 1 since α ≥ N−1/3 and N is suﬃciently large. Therefore, combining (16) and (18), we ﬁnd

- (19) a q ∈Q≤K

![image 96](<2020-bloom-new-upper-bound-sets_images/imageFile96.png>)

M(

a q )

![image 97](<2020-bloom-new-upper-bound-sets_images/imageFile97.png>)

| g(γ) 1A(γ) W(γ)|dγ ≥

α|A|N1/2 16

![image 98](<2020-bloom-new-upper-bound-sets_images/imageFile98.png>)

.

By the Cauchy-Schwarz inequality and Lemma 4, we have

M(

a q )

![image 99](<2020-bloom-new-upper-bound-sets_images/imageFile99.png>)

| g(γ) 1A(γ) W(γ)|dγ

≪

M( aq )

![image 100](<2020-bloom-new-upper-bound-sets_images/imageFile100.png>)

| g(γ)|2 dγ

1/2

M( aq )

![image 101](<2020-bloom-new-upper-bound-sets_images/imageFile101.png>)

W(γ)

2

dγ

1/2

sup

γ∈M(

a q )

![image 102](<2020-bloom-new-upper-bound-sets_images/imageFile102.png>)

1A(γ)

≪

1 q1/2 M(a

![image 103](<2020-bloom-new-upper-bound-sets_images/imageFile103.png>)

![image 104](<2020-bloom-new-upper-bound-sets_images/imageFile104.png>)

q )

| g(γ)|2 dγ

1/2

sup

γ∈M(

a q )

![image 105](<2020-bloom-new-upper-bound-sets_images/imageFile105.png>)

1A(γ) .

Therefore

- (20) a q ∈Q≤K

![image 106](<2020-bloom-new-upper-bound-sets_images/imageFile106.png>)

1 q1/2 M(a

![image 107](<2020-bloom-new-upper-bound-sets_images/imageFile107.png>)

![image 108](<2020-bloom-new-upper-bound-sets_images/imageFile108.png>)

q )

| g(γ)|2 dγ

1/2

sup

γ∈M(

a q )

![image 109](<2020-bloom-new-upper-bound-sets_images/imageFile109.png>)

1A(γ) ≫ α|A| N1/2.

Let Γ1 be the set of a/q ∈ Q≤K for which

- (21)

M(

a q )

![image 110](<2020-bloom-new-upper-bound-sets_images/imageFile110.png>)

| g(γ)|2 dγ ≤

N K5

![image 111](<2020-bloom-new-upper-bound-sets_images/imageFile111.png>)

.

Since |Γ1| ≤ |Q≤K| ≤ K2 and | 1A(γ)| ≤ |A|, the contribution to (20) from γ ∈ Γ1 is

≪

a q ∈Q≤K

![image 112](<2020-bloom-new-upper-bound-sets_images/imageFile112.png>)

1 q1/2

![image 113](<2020-bloom-new-upper-bound-sets_images/imageFile113.png>)

·

N1/2 K5/2

![image 114](<2020-bloom-new-upper-bound-sets_images/imageFile114.png>)

· |A| ≪

α |A|N1/2 (log N)1/2

![image 115](<2020-bloom-new-upper-bound-sets_images/imageFile115.png>)

.

Thus we may restrict our attention to the set Γ2 = Q≤K\Γ1 of a/q ∈ Q≤K for which (21) does not hold. Indeed, we have

- (22)


1 q1/2 M(a

| g(γ)|2 dγ

![image 116](<2020-bloom-new-upper-bound-sets_images/imageFile116.png>)

q )

a q ∈Γ2

![image 117](<2020-bloom-new-upper-bound-sets_images/imageFile117.png>)

![image 118](<2020-bloom-new-upper-bound-sets_images/imageFile118.png>)

1/2

sup

a q )

γ∈M(

![image 119](<2020-bloom-new-upper-bound-sets_images/imageFile119.png>)

1A(γ) ≫ α|A|N1/2.

Since | g(γ)| ≤ 2 |A| ≤ 2N and meas(M(a/q)) ≪ K/N, we see that for any γ ∈ Q≤K

| g(γ)|2 dγ

a q )

M(

![image 120](<2020-bloom-new-upper-bound-sets_images/imageFile120.png>)

1/2

≪ K1/2N1/2,

and so, comparing to (21), for γ ∈ Γ2 the quantity on the left-hand side is N1/2KO(1). Therefore, by dyadic pigeonholing, there are some quantities B,Q with α−1K−1/2 ≪ B ≪ α−1K5/2 and 1 ≤ Q ≤ K, together with a set B ⊂ Γ2, such that

- (1) If a/q ∈ B with gcd(a,q) = 1 then q ∈ [Q,2Q].
- (2) For all γ ∈ B we have


αN1/2 B

≤

![image 121](<2020-bloom-new-upper-bound-sets_images/imageFile121.png>)

| g(γ)|2 dγ

a q )

M(

![image 122](<2020-bloom-new-upper-bound-sets_images/imageFile122.png>)

2αN1/2 B

1/2

≤

.

![image 123](<2020-bloom-new-upper-bound-sets_images/imageFile123.png>)

- (3) We have


1 q1/2 M(a

| g(γ)|2 dγ

![image 124](<2020-bloom-new-upper-bound-sets_images/imageFile124.png>)

q )

a q ∈B

![image 125](<2020-bloom-new-upper-bound-sets_images/imageFile125.png>)

![image 126](<2020-bloom-new-upper-bound-sets_images/imageFile126.png>)

1/2

sup

a q )

γ∈M(

![image 127](<2020-bloom-new-upper-bound-sets_images/imageFile127.png>)

α|A|N1/2 (log K)2

1A(γ) ≫

.

![image 128](<2020-bloom-new-upper-bound-sets_images/imageFile128.png>)

Recalling that K ≪ α−O(1) (since we are assuming that α ≤ 1/(logN)1/4), and letting γa/q be the point in M(a/q) where | 1A(γ)| attains its maximum, we see that this gives the result.

Combining Lemma 5 with Lemma 3 gives the following

- Lemma 6. Let ν > 0. Let A ⊂ [N] be a set of density α = |A|/N with no square diﬀerences. Then at least one of the following holds:


- (1) (A is sparse) log(1/α) ≫ log N.
- (2) (There is a density increment) There is some N′ ≫ ναO(1)N and A′ ⊂ [N′] with no non-zero square diﬀerences, which has density

α′ ≥ (1 + ν/5)α.

- (3) (There are many large Fourier coeﬃcients close to rationals of diﬀerent


denominators) There are B,Q ≪ α−O(1) and a set B ⊂ Q≤Q such that both of the following hold:

- (a) For each a/q ∈ B there exists γa/q ∈ (0,1] such that γa/q − a/q ≪ α−O(1)/N and

a q ∈B

![image 129](<2020-bloom-new-upper-bound-sets_images/imageFile129.png>)

| 1A(γa/q)| ≫

B |A|Q1/2 log(1/α)O(1)

![image 130](<2020-bloom-new-upper-bound-sets_images/imageFile130.png>)

.

- (b) For every 1 ≤ q ≤ Q we have |B ∩ Q=q| ≤ νB2.


Proof. Assume that neither (1) nor (2) hold, so we wish to establish (3). Since (2) does not hold, by Lemma 3, we have that for any q

| g(γ)|2 dγ ≤ να |A|.

a q ∈Q=q M( aq :N,K)

![image 131](<2020-bloom-new-upper-bound-sets_images/imageFile131.png>)

![image 132](<2020-bloom-new-upper-bound-sets_images/imageFile132.png>)

for any K ≪ α−O(1). Since (1) does not hold, we have α ≥ N−1/8 and so A satisﬁes the conditions of Lemma 5. Thus, by Lemma 5 there are B,Q,K ≪ α−O(1) and B ⊂ Q≤Q such that for all a/q ∈ B there exists γa/q such that γa/q − a/q ≪ α−O(1)/N and

|A|Q1/2 log(1/α)O(1)

,

| 1A(γa/q)| ≫ B

![image 133](<2020-bloom-new-upper-bound-sets_images/imageFile133.png>)

a q ∈B

![image 134](<2020-bloom-new-upper-bound-sets_images/imageFile134.png>)

and for all a/q ∈ B

α|A| B2

| g(γ)|2 dγ ≫

.

![image 135](<2020-bloom-new-upper-bound-sets_images/imageFile135.png>)

a q ;N,K)

M(

![image 136](<2020-bloom-new-upper-bound-sets_images/imageFile136.png>)

Summing this second inequality over a/q ∈ B ∩ Q=q we see that

α|A| B2

|B ∩ Q=q| ≪

![image 137](<2020-bloom-new-upper-bound-sets_images/imageFile137.png>)

a q ∈B∩Q=q

![image 138](<2020-bloom-new-upper-bound-sets_images/imageFile138.png>)

| g(γ)|2 dγ ≪ να |A|.

a q ;N,K)

M(

![image 139](<2020-bloom-new-upper-bound-sets_images/imageFile139.png>)

Thus |B ∩ Q=q| ≪ νB2, as required.

7. Refined density increment and proof of Theorem 1

We will now show that there cannot be a large set of rationals with distinct denominators each of which has a large Fourier coeﬃcient. This relies on Theorem

- 2 which shows that there is a lack of additive structure amongst such rationals, and a variant of Chang’s lemma [4] (or its predecessors such as the MontgomeryHala´sz method [9]) which shows that any large set of frequencies with large Fourier coeﬃcients must have some additive structure, and is the key way in which our argument diﬀers from previous approaches. Ultimately this will show that for a suitable choice of parameter ν, the third possibility in Lemma 6 cannot occur, and


- Lemma 6 can be reﬁned to give a density increment. An iterative application of this density increment then proves our main result, Theorem 1.
- Lemma 7 (Variant of Chang’s Lemma). Let η > 0, let A ⊂ [N] be a set of density α = |A|/N and let B ⊂ (0,1]. Then, for each m ≥ 1,


| 1A(b)| ≪ |A|α−1/2mE2m(B;1/2N)1/2m,

b∈B

where the approximate additive energy E2m(C;δ) is given by

E2m(C;δ) := |{b1,...,b2m ∈ C : b1 + ··· + bm − bm+1 ··· − b2m ≤ δ}| (where we recall that · denotes the distance to the nearest integer). Proof. Let θb ∈ R be a phase such that e(θb) 1A(b) = | 1A(b)| ∈ R>0. Then, by Ho¨lder’s inequality, we have

| 1A(b)| =

e(θb)

e(ab)

b∈B

b∈B

a∈A

1−1/2m

2m 1/2m

≤

1

e(θb + ba)

- (23) .


a∈A

a∈A b∈B

Let ψ(t) := sin(πt)2/(πt)2 so that ψ(ξ) = −∞ ∞ ψ(t)e−2πiξt dt satisﬁes ψ(ξ) = 1−|ξ| for |ξ| ≤ 1 and ψ(ξ) = 0 for |ξ| > 1. Since ψ(t) ≥ 0 and ψ(t) ≥ 4/π2 ≥ 1/3 on [0,1/2] we see that

e(θb + ba)

a∈A b∈B

2m

≤ 3

≤ 3

ψ

b1,...,b2m∈B n∈Z

2m

n 2N b∈B

e(θb + ba)

ψ

![image 140](<2020-bloom-new-upper-bound-sets_images/imageFile140.png>)

n∈Z

n 2N

e n(b1 + ··· + bm − bm+1 ··· − b2m)

![image 141](<2020-bloom-new-upper-bound-sets_images/imageFile141.png>)

Applying Poisson summation to the inner sum, and recalling that ψˆ is supported on [−1,1], we see that this is equal to

ψˆ 2N(b1 + ··· + bm − bm+1 ··· − b2m − h)

6

N

b1,...,b2m∈B

h∈Z

≪ N|{b1,...,b2m ∈ B : b1 + ··· + bm − bm+1 ··· − b2m ≤ 1/2N}|. Substituting this into (23) and rearranging then gives the result.

- Lemma 8. Let A ⊂ [N] be a set of density α = |A|/N with no non-zero square diﬀerences. There exists an absolute constant c > 0 such that if


log(1/α) loglog(1/α) then either

ν = exp −c

![image 142](<2020-bloom-new-upper-bound-sets_images/imageFile142.png>)

- (1) log(1/α) ≫ log N/ loglog N, or
- (2) there are N′ ≫ αO(1)N and A′ ⊂ [N′] with no non-zero square diﬀerences, which has density


α′ ≥ (1 + ν/5)α.

Proof. As before, we may assume that log N ≪ α−O(1), by the result of [14]. We assume that (1) and (2) do not hold, and hope to arrive at a contradiction, for a suitable choice of ν.

We apply Lemma 6, and ﬁnd that we must be in the third case since otherwise

(1) or (2) would hold. Thus there are B,Q ≪ α−O(1) and a set B ⊂ Q≤Q such that for each a/q ∈ B there exists γa/q = a/q + O(α−O(1)/N) satisfying

B |A|Q1/2 log(1/α)O(1)

| 1A(γa/q)| ≫

,

![image 143](<2020-bloom-new-upper-bound-sets_images/imageFile143.png>)

a q ∈B

![image 144](<2020-bloom-new-upper-bound-sets_images/imageFile144.png>)

and for every 1 ≤ q ≤ Q we have |B ∩ Q=q| ≤ νB2. By the pigeonhole principle, there must exist some B′ ⊂ B which is contained in an interval of width at most 1/8m such that

B |A| Q1/2 mlog(1/α)O(1)

.

| 1A(γa/q)| ≫

![image 145](<2020-bloom-new-upper-bound-sets_images/imageFile145.png>)

a q ∈B′

![image 146](<2020-bloom-new-upper-bound-sets_images/imageFile146.png>)

Let m ≥ 2 be some integer to be chosen later. We now apply Lemma 7, which shows that for Γ := {γb : b ∈ B′}

B |A|Q1/2 mlog(1/α)O(1)

≪ |A|α−1/2mE2m(Γ;1/2N)1/2m.

![image 147](<2020-bloom-new-upper-bound-sets_images/imageFile147.png>)

Since B′ is contained in an interval of width at most 1/8m we know that b1 + ··· − b2m ∈ [−1/4,1/4]. In particular, since |γb − b| ≪ α−O(1)/N for b ∈ B, provided mα−O(1) < cN for some suﬃciently small c > 0, we have γb

∈ (−1/2,1/2), and so

+ ··· − γb

2m

1

E2m(Γ;1/2N) = |{b1,...,b2m ∈ B′ : |γb

| ≤ 1/2N}|. Furthermore, since B ⊂ Q≤Q, b1 + ··· − b2m is always a rational of denominator

+ ··· − γb

2m

1

- at most Q2m for b1,...,b2m ∈ B. Therefore if b1 + ··· − b2m is not zero then it is at least Q−2m in absolute value. As before, since |γb − b| ≪ α−O(1)/N, provided mQO(m)α−O(1) < cN for some small constant c > 0, it follows that for any


| ≥ Q−2m/2 or b1 + ··· − b2m = 0. Therefore, provided mQO(m)α−O(1) < cN for suﬃciently small c > 0, the approximate additive energy E2m(Γ;1/N) actually only counts the times when the corresponding sum of rationals is zero, so

+ ··· − γb

∈ Γ either |γb

,...,γb

γb

2m

2m

1

1

E2m(Γ;1/2N) = E2m(B′).

Recalling that Q ≪ α−O(1), we have shown that either α−O(m) ≫ N or

- (24) E2m(B′) ≫ α

BQ1/2 mlog(1/α)O(1)

![image 148](<2020-bloom-new-upper-bound-sets_images/imageFile148.png>)

2m

.

We impose the condition m ≪ log log(1/α), so that α−O(m) = o(N) since we are assuming that (1) does not hold, so we have (24). We now apply Theorem 2 to bound E2m(B′) from above, which shows that for some absolute constant C > 0 we have

- (25) mO(m)(log Q)C


m

(νB2Q)m ≫ α

BQ1/2 log(1/α)O(1)

![image 149](<2020-bloom-new-upper-bound-sets_images/imageFile149.png>)

2m

.

Here we used the assumption that |B′ ∩ Q=q| ≤ |B ∩ Q=q| ≤ νB2 for all q since (2) does not hold.

The key feature of this bound is that the powers of B and Q exactly cancel, and in particular the lower bound on ν in terms of α is only of order α−O(1/m) log(1/α)O(1). We will derive a contradiction from this bound with a suitable choice of ν, thereby proving the lemma. First note that we can rewrite (25) as

α1/m mO(1) log(1/α)O(1)

log log Q m

exp −Cm

ν ≫

![image 150](<2020-bloom-new-upper-bound-sets_images/imageFile150.png>)

![image 151](<2020-bloom-new-upper-bound-sets_images/imageFile151.png>)

.

Since Q ≪ α−O(1), if we choose m = ⌈c′ log log(1/α)⌉, for some suﬃciently small constant c′ > 0, then this gives

ν ≫ exp −O

log(1/α) log log(1/α)

![image 152](<2020-bloom-new-upper-bound-sets_images/imageFile152.png>)

,

which gives a contradiction for a suitable choice of the constant c in our deﬁnition of ν. This completes the proof.

We may now ﬁnish the proof of our main theorem with an iterative application of Lemma 8. Proof of Theorem 1. Suppose that A ⊂ [N] has density α = |A|/N and has no square diﬀerences. We wish to show that

log(1/α) ≫ (log log N)(log log log N). Let

log(1/α) log log(1/α)

ν := exp −c

![image 153](<2020-bloom-new-upper-bound-sets_images/imageFile153.png>)

be as in Lemma 8. If log(1/α) ≫ log N/ loglog N then we are done. Otherwise, by Lemma 8, there are N′ ≥ αO(1)N and A′ ⊂ [N′] which has no square diﬀerences, with density

α′ ≥ (1 + ν/5)α.

Repeatedly applying Lemma 8, we obtain some sequence N1,...,Nt of integers and associated sets At ⊂ [Nt] such that

- (1) Each set At has no non-zero square diﬀerences.
- (2) At ⊂ [Nt] has density αt = |At|/Nt ≥ (1 + ν/5)tα.
- (3) We have Nt ≥ αO(t)N.


This process can only terminate if Nt < N1/2, since otherwise all conditions of Lemma 8 remain satisﬁed. However, the density of any set can never exceed 1, so we must have α(1 + ν/20)t ≤ αt ≤ 1, which implies that

t ≪ ν−1 log(1/α). Therefore

N1/2 > Nt ≥ αO(t)N ≫ N exp −O ν−1 log(1/α)2 . Thus

log N ≪ ν−1(log 1/α)2. Recalling that log(1/ν) ≪ log(1/α)/ log log(1/α), taking logarithms of both sides and rearranging yields

log(1/α) log log(1/α)

≫ log log N. This implies log(1/α) ≫ (log log N)(log log log N), which gives the result. References

![image 154](<2020-bloom-new-upper-bound-sets_images/imageFile154.png>)

- [1] A. Balog, J. Pelikan, J. Pintz, and E. Szemer´edi, Diﬀerence sets without kth powers, Acta. Math. Hungar. 65 (2) (1994), 165–187.
- [2] J. Bourgain, S. J. Dilworth, K. Ford, S. V. Konyagin, and D. Kutzarova. Breaking the k2 barrier for explicit RIP matrices, STOC’11 – Proceedings of the 43rd ACM Symposium on Theory of Computing (2011), 637–644.
- [3] T. F. Bloom and O. Sisask, Breaking the logarithmic barrier in Roth’s theorem on arithmetic progressions, Arxiv preprint available at https://arxiv.org/abs/2007.03528.
- [4] M.-C. Chang, A polynomial bound in Freiman’s theorem, Duke Math. J. 113 (3) (2002), 399–419.
- [5] H. Furstenberg, Ergodic behavior of diagonal measures and a theorem of Szemere´di on arithmetic progressions, J. Analyse Math. 31 (1977), 204–256.
- [6] B. Green, Sa´rkz¨ozy’s theorem in function ﬁelds, Q. J. Math. 68 (2017), no. 1, 237–242.
- [7] M. Lewko, An improved lower bound related to the Furstenberg-S´ark¨ozy theorem, Electron. J. Combin. 22 (2015), Paper 1.32, 6.
- [8] J. Maynard, Fractional parts of polynomials, Arxiv preprint available at https://arxiv.org/abs/2011.12275.
- [9] H. L. Montgomery, Mean and large values of Dirichlet polynomials, Invent. Math. 8 (1969), 334–345.
- [10] J. Pintz, W. L. Steiger, and E. Szemer´edi, On sets of natural numbers whose diﬀerence set contains no squares, J. London Math. Soc. (2) 37 (1988), 219–231.
- [11] A. Rice, A maximal extension of the best-known bounds for the Furstenberg-S´ark¨ozy theorem, Acta Arith. 187 (2019), 1–41.
- [12] I. Ruzsa, Diﬀerence sets without squares, Period. Math. Hungar. 15 (1984), 205–209.
- [13] I. Ruzsa and T. Sanders, Diﬀerence sets and the primes, Acta Arith. 131 (3) (2008) 281–301.
- [14] A. S´ark¨zy, On diﬀerence sets of sequences of integers. I, Acta Math. Acad. Sci. Hungar. 31

(1978), 125–149.

- [15] J. Wolf, Arithmetic structure in sets of integers, Doctoral thesis, University of Cambridge,


2008. https://doi.org/10.17863/CAM.16214.

