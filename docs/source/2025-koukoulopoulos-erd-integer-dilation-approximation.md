---
type: source
kind: paper
title: Erdős's integer dilation approximation problem and GCD graphs
authors: Dimitris Koukoulopoulos, Youness Lamzouri, Jared Duker Lichtman
year: 2025
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2502.09539v1
source_local: ../raw/2025-koukoulopoulos-erd-integer-dilation-approximation.pdf
topic: general-knowledge
cites:
---

arXiv:2502.09539v1[math.NT]13Feb2025

ERDOS’S˝ INTEGER DILATION APPROXIMATION PROBLEM AND GCD GRAPHS

DIMITRIS KOUKOULOPOULOS, YOUNESS LAMZOURI, AND JARED DUKER LICHTMAN

ABSTRACT. Let A ⊂ R 1 be a countable set such that limsupx→∞ log1x α∈A∩[1,x] α1 > 0. We prove that, for every ε > 0, there exist inﬁnitely many pairs (α,β) ∈ A2 such that α = β and |nα − β| < ε for some positive integer n. This resolves a problem of Erdo˝s from 1948. A critical role in the proof is played by the machinery of GCD graphs, which were introduced by the ﬁrst author and by James Maynard in their work on the Dufﬁn–Schaeffer conjecture in Diophantine approximation.

![image 1](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile1.png>)

![image 2](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile2.png>)

1. INTRODUCTION

Given a set A ⊂ R>0 and a positive number ε, let us consider the following approximation problem of a Diophantine nature: are there distinct α, β ∈ A and an integer n such that

- (1.1) |nα − β| < ε ?

Equivalently, we seek to ﬁnd a fraction β/α = 1 whose numerator and denominator both lie in A, and which has the property that β/α < ε/α, where · denotes the distance to the nearest integer.

Evidently, if A has an accumulation point in R, then (1.1) has inﬁnitely many solutions with distinct α, β ∈ A and with n = 1. So, we will be assuming throughout that A has no accumulation points, that is to say it is a discrete set. In particular, A is a countable set.

In 1948, Erd˝os [5, Page 692] asked whether it is possible to ﬁnd solutions to (1.1) if A is “large enough”. Motivated by his work [4] and that of Behrend [2] on integer primitive sequences (see Deﬁnition 1.1 below and the discussion following it), he proposed that this might indeed be possible if A satisﬁes one of the following conditions:

- (1.2)

α∈A, α 2

1 α log α

![image 3](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile3.png>)

= ∞

or

- (1.3) limsup


1 α

1 log x

> 0.

![image 4](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile4.png>)

![image 5](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile5.png>)

x→∞

α∈A∩[1,x]

We shall refer to this question as the integer dilation approximation problem. This problem was mentioned1 again in [6, 7, 8, 9, 10, 11, 12, 13, 14, 15]. In particular, Erd˝os, Sa´rk¨ozy and Szemere´di

![image 6](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile6.png>)

Date: February 14, 2025. 2020 Mathematics Subject Classiﬁcation. Primary: 11J25, 11B83. Secondary: 11A05, 05C40. Key words and phrases. Erdo˝s, integer dilation approximation problem, primitive sets of integers, GCD graphs,

Diophantine approximation, structure vs randomness.

1In [13], which was published in 1997, shortly after Paul Erdo˝s passed away, he wrote “I offer $500 for settling this annoying diophantine problem.”

1

[15] asked in 1968 whether one can prove the existence of inﬁnitely many solutions to (1.1) under the stronger assumption that

1 x

liminf

1 > 0.

![image 7](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile7.png>)

x→∞

α∈A∩[1,x]

In this paper, we resolve Erd˝os’s integer dilation approximation problem when A satisﬁes the second condition (1.3). Theorem 1. Let A ⊂ R>0 be a discrete set such that

1 α

1 log x

> 0.

limsup

![image 8](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile8.png>)

![image 9](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile9.png>)

x→∞

α∈A∩[1,x]

Then, for every ε > 0, there exists a pair (α, β) ∈ A2 such that α = β and |nα − β| < ε for some positive integer n.

Remark. In fact, the above theorem implies trivially that, for every ε > 0, there must exist inﬁnitely many pairs (α, β) as above. Indeed, once we locate the ﬁrst one, say (α1, β1), we apply the theorem to A′ := A \ {α1, β1} to locate a second suitable pair (α2, β2). Continuing this way, we may ﬁnd an inﬁnite number of such pairs.

It is worth noting that Erd˝os originally stated his problem in its contrapositive form; the above formulation of the problem appeared ﬁrst in a paper of Erd˝os and Sa´rk¨ozy [14], and subsequently in Haight’s 1988 work [17], who proved Theorem 1 in the special case when the ratios α/β with distinct α, β ∈ A are all irrational. As a matter of fact, under this assumption, Haight proved the stronger estimate

- (1.4) lim

x→∞

1 x

![image 10](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile10.png>)

a∈A∩[1,x]

1 = 0.

Erd˝os’s motivation for stating the problem in the contrapositive form comes from its connection to primitive sets of integers. Indeed, if A ⊂ N and ε ∈ (0, 1], then the only way to have a solution to

- (1.1) is if β = nα, that is to say, if α divides β. Let us now recall the deﬁnition of a primitive set:


- Deﬁnition 1.1 (primitive set). We say that a set A ⊂ N is primitive if a ∤ b for all distinct a, b ∈ A.


Early on, many experts, including Chowla, Davenport, and Erd˝os, believed that primitive sets all have natural density equal to zero. But to their great surprise, in 1934 Besicovitch [3] constructed primitive sets with upper natural density 12 − ε, for any ε > 0. (This is sharply different from the situation in Haight’s estimate (1.4).) On the other hand, in 1935 Behrend [2] and Erd˝os [4] proved that primitive sets of integers all have logarithmic density zero, and hence lower natural density zero. In fact, Erd˝os [4] showed the stronger result that

![image 11](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile11.png>)

- (1.5)

a∈A

1 alog a

![image 12](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile12.png>)

< ∞,

for any primitive set of integers A, while Behrend’s result [2] states that

- (1.6)


1 a ≪

![image 13](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile13.png>)

a∈A∩[1,x]

log x √log log x

,

![image 14](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile14.png>)

![image 15](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile15.png>)

for such sets. More recently, Ahlswede, Khachatrian and Sa´rk¨ozy [1] strengthened Behrend’s estimate by showing that

- (1.7)

a∈A∩[y,yx]

1 a ≪

![image 16](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile16.png>)

log x √log log x uniformly for all primitive sets A and all x 3 and y 1.

![image 17](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile17.png>)

![image 18](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile18.png>)

- 1.1. Notation. Given S ⊆ R and x ∈ R, we let S x := S ∩ (−∞, x] and S>x := S ∩ (x, ∞). For a positive integer n, we denote by P+(n) and P−(n) its largest and the smallest prime

factors respectively, with the standard conventions that P+(1) = 1 and P−(1) = ∞. In addition, we write ω(n) for the number of distinct prime factors of n.

Given k ∈ N, we let τk denote the k-th divisor function. We write f(x) g(x) (respectively f(x) g(x)) if f(x) (1 + o(1))g(x) (respectively

f(x) (1 + o(1))g(x)) as x → ∞.

Lastly, we write meas to denote the Lebesgue measure on R. In addition, given T > 0 and a Lebesgue-measurable set S, we let (1.8) PT(S) :=

meas(S ∩ [0, T]) T

![image 19](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile19.png>)

.

- 1.2. Ideas from the proof. The connection of Erd˝os’s problem to primitive sets of integers plays a crucial role in our proof, as does Haight’s work. In fact, one may view our proof as an instance of the structure versus randomness philosophy.


- (1.9)


Let us consider a discrete set A ⊂ R 1 and a number ε ∈ (0, 1] such that there are no solutions to the inequality |nα − β| < ε with distinct α, β ∈ A and with n ∈ N. In order to establish Theorem 1, we must prove that

1 α

= o(log x) (x → ∞).

![image 20](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile20.png>)

α∈A∩[1,x]

We have two extreme cases:

- • Structured sets: these are primitive sets or small “perturbations” of them. By this, we mean that A ⊆ γQ 1 := {γ̺ : ̺ ∈ Q 1} for some γ ∈ R 1, and that the set of denominators

Q = q ∈ N : ∃a ∈ N such that gcd(a, q) = 1 and γa/q ∈ A

is sparse. For each given q ∈ Q, the set {a ∈ N : gcd(a, q) = 1, a/q ∈ A} is primitive, so we may apply Behrend’s estimate (1.6) to it. If Q is sparse enough, then we deduce that (1.9) holds.

- • Random sets: these are sets A for which all ratios α/β are irrational, or perhaps rational numbers of large height2. We can expect to be able to handle such sets by a suitable variant of Haight’s proof and to prove that (1.9) holds for them too.


Roughly speaking, the strategy of the proof is to show that either A consists almost 100% of a random set, or that a positive proportion of A is structured.3

![image 21](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile21.png>)

- 2The correct notion of “large height” is with respect to the size of α and β. The crucial quantity to consider is [α,β] := H(α/β)/ max{α,β}, where H(·) is the height function; see Deﬁnition 2.4 below.
- 3An astute reader might have noticed that the notions of structured and random sets are not fully orthogonal to each other, because in the latter case we allow the ratios α/β to be rationals of large height. Consider for example the case of a set A = j 1{a/qj : a ∈ Sj, gcd(a,qj) = 1}, where (qj)∞j=1 is a sparse sequence of prime numbers and


Let us now provide some more concrete context. As in Haight’s work, the starting observation is that, for any choice A′ of a subset of A, the union

(nα − ε/2, nα + ε/2)

- (1.10)


α∈A′ n∈N

avoids all intervals (α − ε/2, α + ε/2) with α ∈ A \ A′. Indeed, this is a simple consequence of our assumption that there are no solutions to the inequality |nα − β| < ε with distinct α, β ∈ A and with n ∈ N. Thus, if we could show that the union in (1.10) covers ∼ 100% of the positive real numbers, we would deduce that #(A \ A′) ∩ [0, T] = o(T) as T → ∞.

To prove that the union in (1.10) has large measure, we use the second moment method (cf. Section 2.2). Suppose we are given certain events E1, E2, . . . in a probability space and we need to show that, with high probability, at least one of them occurs. The second moment method says that this is indeed true if the sum of the probabilities of the events Ei is large and the events Ei are negatively correlated on average (see Deﬁnition 2.2 and equation (2.10) below).

Our probability space is the interval space [0, T] with T a parameter tending fast to inﬁnity, and the probability measure is given by PT, which we deﬁned in (1.8). To construct the events Ei, we ﬁx a judicious choice of distinct elements α1, . . ., αJ of A; these will form the special set A′. Haight considered the events

(nαi − ε/2, nαi + ε/2)

Hi =

n∈N

and proved that if αi/αj is irrational, then PT(Hi ∩ Hj) ∼ PT(Hi)PT(Hj) as T → ∞. However, the events Hi could be highly correlated when αi/αj is a rational number of small height (see Section 2.3 below). For this reason, we borrow a key idea from the proof of Erd˝os’s estimate (1.5) and we take

(nαi − ε/2, nαi + ε/2).

Ei =

n∈N, P−(n)>αi

For these events too, Haight’s argument and inclusion-exclusion allows us to show that if αi/αj is irrational, then PT(Ei ∩ Ej) ∼ PT(Ei)PT(Ej) as T → ∞. In addition, we may use an elementary argument to calculate PT(Ei∩Ej) when αi/αj is a rational number. It turns out that PT(Ei∩Ej)

PT(Ei)PT(Ej), unless αi/αj has small height.

By the above discussion, we see that the only potentially problematic case is when there is a positive proportion of ratios αi/αj of small height. Our goal is then to prove that A′ contains a large structured subset to which we can apply Behrend’s estimate (1.6). In order to explain how to locate this subset, let us assume for simplicity that A ⊂ Q 1 (without necessarily knowing that the set of denominators is very sparse, meaning that A is structured). If we write αi = a/q and αj = b/r, it turns out that the corresponding events Ei and Ej are negatively correlated, unless the product gcd(a, b) gcd(q, r) is large. This is a generalization of the set-up that occurred in the work of the ﬁrst author and of James Maynard on the Dufﬁn–Schaeffer conjecture [21]. In that paper, a potential counterexample to the Dufﬁn–Schaeffer conjecture was a set of integers with many pairwise GCDs being large. Here, we work with a set of rational numbers and we must account for the product of the GCDs of the numerators and the denominators, but the methods of [21] can be adapted to this more general setting, without any serious difﬁculty. Hence, using the machinery of GCD graphs of [21], we show that the only way we can have lots of pairs (a/q, b/r) with large

![image 22](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile22.png>)

Sj ⊂ Z∩(qjxj−1,qjxj] is primitive for each j, with the sequence (xj)∞j=1 growing at some appropriate rate. This is a structured set, but it could also be a random set, unless there are elements in some Sj with a large GCD. This example is very useful to keep in mind for the discussion later on.

product gcd(a, b) gcd(q, r) is if there exist ﬁxed integers A, B, Q and R such that, for lots of pairs (a/q, b/r), we have a = Aa′, b = Bb′, q = Qq′ and r = Rr′, as well as gcd(a, b) = gcd(A, B) and gcd(q, r) = gcd(Q, R). In particular, gcd(A, B) gcd(Q, R) must be large.

However, when we use GCD graphs to produce the ﬁxed integers A, B, Q, R, we incur the loss of the Euler factors

1 p

1 p

−2

−2

1 −

1 −

.

![image 23](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile23.png>)

![image 24](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile24.png>)

p| gcd(A,B)

p| gcd(Q,R)

In the context of the Dufﬁn–Schaeffer conjecture, each integer n is weighted by ϕ(n)/n. These weights were used in [21] to counterbalance the lost Euler factors from the method of GCD graphs. Here, however, we do not possess such convenient weights, so we have to gain the missing Euler factors from certain coprimality considerations that allow us to sieve for them. Indeed, note that gcd(a, q) = gcd(b, r) = 1, and thus

gcd(a, Q) = gcd(b, R) = gcd(q, A) = gcd(r, B) = 1.

Hence, in principle, we should be able to win the needed Euler factors by sieving a′, b′, q′ and r′ by Q, R, A and B, respectively. However, this will only be true if the range of summation of a′, b′, q′, r′ is “long enough” with respect to the integers we are sieving with. It turns out that we

can arrange for the range of a′ and b′ to be long enough, and thus to gain the factors ϕ(QQ) · ϕ(RR). However, the range of q′ and r′ might not be long enough. In fact, it is possible that q′ = r′ = 1, a case that will occur if all elements of A have the same denominator. It thus seems we have reached an impasse.

![image 25](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile25.png>)

![image 26](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile26.png>)

To get around this issue, we observe that the range of summation of a′ and b′ is sufﬁciently long so that if we somehow knew that gcd(a′, A) = gcd(b′, B) = 1, then we would be able to gain the factors ϕ(AA) and ϕ(BB) from the a′ and b′ summations, respectively. This would be the case, for example, if we knew that all numerators a were square-free (if a is square-free and a = Aa′, we automatically have gcd(a′, A) = 1). But this assumption is too restrictive to prove Theorem

![image 27](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile27.png>)

![image 28](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile28.png>)

- 1 in full generality. Alternatively, we would be able to gain the needed Euler factors if we knew that, for every prime p|A, the p-adic valuation of A matches that of a (and similarly for the primes p|B). However, the method of GCD graphs does not guarantee this exact divisibility. Indeed, we have the required exact divisibility in the “ﬁrst iterative step” of the method of GCD graphs [21, Proposition 8.1], but not necessarily in the “second iterative step” [21, Proposition 8.2].


To get around this second obstacle, we use a variant of the method of GCD graphs that borrows a key idea from the recent paper of Hauke, Vazquez and Walker [19], in which they build on the work of Green–Walker [16] to give an alternative proof of the Dufﬁn–Schaeffer conjecture. In this variant, we only perform the second iterative step to fully determine the divisors Q and R of the denominators, but we do not fully determine ﬁxed divisors A and B for the numerators. Instead, after we perform fully the ﬁrst iterative step for the numerators, and both the ﬁrst and second iterative steps for the denominators, we arrive at a situation where we have fully determined Q and R, and we have few possibilities for A and B with the beneﬁt that, for each given possibility of A and B, we have the required exact divisibility. This gives us the advantage that we can gain

the factors ϕ(AA) and ϕ(BB) from the a′ and b′ summations. But it comes at the expense of having to execute a new summation over all possible values of A and B. It turns out that this summation is

![image 29](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile29.png>)

![image 30](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile30.png>)

too large (unlike in [19], where the savings ϕ(AA) · ϕ(BB) is enough to counterbalance the loss from the summation over A and B). Hence, we have reached a third important obstacle.

![image 31](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile31.png>)

![image 32](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile32.png>)

In order to get around this last obstacle, we use the extra savings provided to us from Behrend’s estimate (1.6) (in fact, we need a generalization of it - see Theorem 4.1 below). In this last step,

- a small miracle occurs: the savings from Behrend’s estimate is precisely what we need to balance the loss from the extra summation over all possible values of A and B. This feature of our proof is new and did not appear in the work on the Dufﬁn–Schaeffer conjecture [19, 21, 22]. It is also one of the main reasons why our theorem is “soft” and we do not prove quantitative estimates like


- (1.6).

Remark. A different reason why we cannot prove (1.6) is that we work with the events Ei, whose measure is too small. There is some hope though that our method can show (1.5), at least when A ⊂ {a/q ∈ Q 1 : a square-free}. The reason is that under this assumption we can avoid using the Hauke–Vazquez–Walker variation described above. Note however that there is a second important feature of our proof, stemming from the construction of the sets A′j in Section 2.5. We use this construction to guarantee that the events Ei and Ej can only be positively correlated when log αi ≍ log αj. This is an important technical feature of the proof that greatly simpliﬁes many details in Section 2. But it also appears to be essential, especially in Sections 6 and 8.

2. STRATEGY AND KEY INGREDIENTS OF THE PROOF OF THEOREM 1

- 2.1. Initial maneuvers. Let A ⊂ R 2 be a discrete set such that


- (2.1) limsup


1 α

1 log x α∈A∩[1,x]

> 0,

![image 33](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile33.png>)

![image 34](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile34.png>)

x→∞

and let ε ∈ (0, 1]. We seek to ﬁnd distinct α, β ∈ A and an integer n such that |nα − β| < ε. By dividing this inequality by ε, and by replacing A by the set {α/ε : α ∈ A}, which also satisﬁes

- (2.1), we may assume that ε = 1. In conclusion, we have reduced Theorem 1 to the following case: we are given a discrete set A ⊂ R 2 satisfying (2.1), and we wish to ﬁnd distinct α, β ∈ A and a positive integer n such that |nα − β| < 1. Let us assume for contradiction that
- (2.2) |nα − β| 1 for all α, β ∈ A with α = β, and for all n ∈ N. In particular, A is 1-spaced and satisﬁes the “primitivity condition”
- (2.3) α/β ∈/ N for all distinct α, β ∈ A. We will then show that
- (2.4) lim

T→∞

1 T

![image 35](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile35.png>)

α∈A∩[1,T]

1 = 0.

Clearly, if we can indeed prove this, we will contradict (2.1). We will have thus completed the proof of Theorem 1.

Now for each α ∈ A, let us deﬁne the sets Mα :=

n∈N

nα − 12, nα + 12 .

![image 36](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile36.png>)

![image 37](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile37.png>)

As Haight also observed, for any A′ ⊂ A, condition (2.2) implies that

- (2.5)


α − 21, α + 12 ∩

Mα = ∅.

![image 38](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile38.png>)

![image 39](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile39.png>)

α∈A′

α∈A\A′

Moreover, we have that

- (2.6) meas [0, T] ∩

α∈A\A′

α − 21, α + 12 = # A \ A′) ∩ [0, T] + O(1).

![image 40](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile40.png>)

![image 41](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile41.png>)

Assume now that, for every given ε > 0, we can show the existence of a ﬁnite set A′ = A′(ε) ⊂ A, and T0 = T0(A′, ε) such that

- (2.7) PT

α∈A′

Mα 1 − ε for all T T0.

We then deduce that #(A ∩ [1, T]) εT + Oε(1) for all T T0 by (2.5) and (2.6), which implies (2.4) since ε can be taken arbitrarily small.

2.2. The second moment method. In order to prove (2.7), we use the second moment method as in Haight’s paper [17]. To this end we record the following classical lemma which follows from an easy application of the Cauchy-Schwarz inequality (see for example [18, Lemma 2.3]).

Lemma 2.1. Let T be a positive real number, let k 1 be an integer, and let E1, . . ., Ek be measurable subsets of [0, T]. Then, we have

- (2.8) PT

k

j=1

Ej

k

- j=1 PT Ej 2

![image 42](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile42.png>)

k i=1

- k


j=1 PT Ei ∩ Ej

.

In view of the above lemma, if we are given measurable sets E1, . . ., Ek ⊂ [0, T] and we want to show that

- (2.9) PT

k

j=1

Ej (1 + o(1)), as T → ∞,

then it sufﬁces to prove that E1, . . ., Ek verify the following two conditions:

- 1. kj=1 PT Ej) → ∞ as T → ∞;
- 2. PT Ei ∩ Ej PT Ei)PT Ej) whenever 1 i < j k.


Motivated by the second condition, and in order to keep the exposition concise, we make the following deﬁnition.

Deﬁnition 2.2 (Negatively correlated sets). Let E1, E2 be measurable subsets of R 0. We say that

- E1 and E2 are negatively correlated4 if PT E1 ∩ E2 PT E1)PT E2) as T → ∞.

In order to obtain (2.9), one can of course weaken the second condition above to only require that the sets E1, . . ., Ek are pairwise negatively correlated on average, namely that (2.10)

1 i =j k

PT Ei ∩ Ej

1 j k

PT Ej

2

.

![image 43](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile43.png>)

4If we view [0,T] as a probability space equipped with the probability measure PT, then the condition PT E1 ∩

- E2 < PT E1)PT E2) is equivalent to saying the random variables E




and E

have negative correlation. With

1

2

this in mind, we ought to have deﬁned PT E1 ∩ E2 PT E1)PT E2) to mean that E1 and E2 are “asymptotically non-positively correlated”, but this would be rather cumbersome. For this reason, we resort to a less precise but cleaner terminology.

Note that PT Mα ∼ 1/α, and we might assume that α∈A 1/α = ∞ since otherwise (2.4) holds trivially. Therefore, if we can show that the sets {Mα}α∈A′ are pairwise negatively correlated on average, for some judicious choice of A′ such that α∈A′ 1/α is large, then we would deduce (2.7).

Haight [17, Lemma 1] proved that

- (2.11) PT Mα ∩ Mβ ∼ PT Mα)PT Mβ

if α/β is irrational. This implies that Mα and Mβ are asymptotically uncorrelated, which is even stronger than saying they are negatively correlated. Using (2.11), Haight deduced that (2.4) holds if α/β ∈/ Q for all distinct elements α, β ∈ A.

2.3. The problem with the sets Mα. Given the discussion in the previous section, a natural approach to prove (2.7) is to apply Lemma 2.1 with the events Ei being of the form Mα with α in our specially chosen set A′. However, this does not work in full generality. For instance, if A is a set of integers, then the events Mα and Mβ are positively correlated if gcd(α, β) > 1. Indeed if α, β ∈ N, then

PT Mα ∩ Mβ =

1 T

![image 44](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile44.png>)

# (m, n) ∈ N2 : mα = nβ, mα T ∼ gcd(α, β)PT Mα)PT Mβ .

As a matter of fact, one can construct easy examples of sets of integers A such that {Mα}α∈A are positively correlated on average, so there is no hope for the second moment method to work in this case.5 In fact, if it were to work, we would have an analogous result to Haight in the integer case, but we know from Besicovitch’s result [3] that there exist integer primitive sets with positive upper natural density.

By (2.11), we only need to focus on the case where α/β ∈ Q. In this case let us write α/β = s/t where s, t are positive coprime integers. Then we observe that

PT Mα ∩ Mβ

1 T

![image 45](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile45.png>)

# (m, n) ∈ N2 : mα = nβ, mα T ∼

1 αt ∼

![image 46](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile46.png>)

β t · PT Mα)PT Mβ .

![image 47](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile47.png>)

- (2.12)


Hence, if the quantity t/β = s/α is small, the sets Mα, Mβ will be positively correlated. It turns out that this quantity plays a central role in our proof of Theorem 1. We shall call it the bracket of α and β. To deﬁne this notion properly for all positive real numbers, we ﬁrst deﬁne the height of a real number.

- Deﬁnition 2.3 (Height of a real number). Let α > 0 be a real number. If α ∈/ Q, we deﬁne H(α) := ∞.


Otherwise, if α ∈ Q, then we write α = a/q with a, q ∈ N and gcd(a, q) = 1, and we deﬁne

H(α) := max{a, q}. We call H(α) the height of the number α.

5An easy example is to take A ⊂ j 1{a ∈ N ∩ [√xj,xj] : ω(a) = ⌊log log xj⌋} for a sparse sequence xj → ∞. We may ﬁnd such an example such that the factor gcd(a,b) has expected value equal to a power of log xj when a and

![image 48](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile48.png>)

![image 49](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile49.png>)

- b range over A ∩ [√xj,xj] and are weighted by PT(Ma) ∼ 1/a and PT(Mb) ∼ 1/b, respectively.


![image 50](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile50.png>)

- Deﬁnition 2.4 (Bracket of two real numbers). Given two real numbers α, β > 0, we deﬁne


H(α/β) max{α, β}

[α, β] :=

.

![image 51](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile51.png>)

We have the following basic properties of the bracket of two real numbers.

- Lemma 2.5. Let α, β > 0.


- (a) We have [α, β] = [β, α].
- (b) If α/β = s/t ∈ Q, where s/t is a reduced fraction, then

[α, β] =

s α

![image 52](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile52.png>)

=

t β

![image 53](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile53.png>)

.

- (c) If α = a/q and β = b/r, where a/q and b/r are both reduced fractions, then


qr gcd(q, r) gcd(a, b)

.

[α, β] =

![image 54](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile54.png>)

Proof. (a) This follows readily by the deﬁnition of [α, β].

- (b) Using part (a), we may assume that α β. Then, we have that α/β = s/t 1, and thus

H(α/β) = s. We thus ﬁnd that [α, β] = s/α. Lastly, we have that s/α = t/β by assumption.

- (c) If we let a1 = a/ gcd(a, b), b1 = b/ gcd(a, b), q1 = q/ gcd(q, r) and r1 = r/ gcd(q, r), then


we have α/β = a

1r1

b1q1 , and gcd(a1r1, b1q1) = 1. Hence, [α, β] = a

1r1

α by part (b). Inserting the deﬁnition of a1 and r1 in this expression, and using that α = a/q, completes the proof of this last part of the lemma.

![image 55](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile55.png>)

![image 56](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile56.png>)

It follows from (2.12) that Mα and Mβ are positively correlated if [α, β] < 1. To overcome this problem so that the second moment method works, we replace Mα by smaller sets, of the form

n∈Lα(nα−1/2, nα+1/2) for some Lα ⊂ N. Using an idea of Erd˝os [4] from his proof of (1.5), it turns out that a judicious choice for Lα is to take {n ∈ N : P−(n) > α}, meaning the set of α-rough numbers. Hence, for each α 1, we deﬁne the sets

for which we have

Nα :=

n∈N P−(n)>α

nα − 12, nα + 12 ,

![image 57](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile57.png>)

![image 58](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile58.png>)

- (2.13) PT(Nα) ∼

1 α p α

![image 59](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile59.png>)

1 −

1 p

![image 60](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile60.png>)

as T → ∞. Since Nα ⊂ Mα for all α 1, relation (2.7) will follow as long as we can show that

- (2.14) PT


Nα 1 − ε

α∈A′

for an appropriate choice of A′. We will use Lemma 2.1 to prove (2.14). To this end, we must understand the correlations of the sets Nα.

- 2.4. Correlation estimates. We ﬁrst show that if [α, β] 1, then the sets Nα, Nβ are not only negatively correlated, they are in fact disjoint!


- Lemma 2.6 (No overlap when [α, β] 1). Let α > β 1 be two real numbers such that α/β ∈/ N and [α, β] 1. Then

Nα ∩ Nβ = ∅.

To prove this result we ﬁrst need to take care of the diagonal solutions mα = nβ, when m is α-rough and n is β-rough.

- Lemma 2.7 (No diagonal solutions). Let α > β 1 be two real numbers such that α/β ∈/ N and [α, β] α/β. Then there are no solutions to the equation mα = nβ with m and n natural numbers such that P−(m) > α.

Proof. We have α/β ∈ Q; otherwise, [α, β] = ∞. Write α/β = s/t in reduced form. Suppose for contradiction that mα = nβ for some m, n ∈ N with P−(m) > α. Equivalently, ms = nt. Since gcd(s, t) = 1, we must have that t|m, in particular P−(t) > α. On the other hand, note that t/β = [α, β] α/β, and thus t α. But t α and P−(t) > α forces t = 1, which gives α/β = s ∈ N, a contradiction.

Proof of Lemma 2.6. As in Lemma 2.7, we may assume that α/β ∈ Q. Let us write α/β = s/t in reduced form. If Nα∩Nβ were non-empty, then there would exist m, n ∈ N such that P−(m) > α, P−(n) > β and |mα − nβ| < 1. Since [α, β] 1 < α/β, Lemma 2.7 forces mα = nβ. Thus ms − nt is a non-zero integer, and so

1 > |mα − nβ| = β|ms/t − n| =

β t · |ms − nt| = |ms − nt|

![image 61](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile61.png>)

![image 62](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile62.png>)

[α, β] |ms − nt| 1 using [α, β] 1. This gives a contradiction, and completes the proof.

In view of Lemma 2.6, we only need to investigate the correlations of Nα and Nβ when [α, β] >

- 1. Using inclusion-exclusion and Haight’s result (2.11) we ﬁrst show that Nα and Nβ are negatively correlated when [α, β] = ∞, that is to say, when α/β is irrational.


- Lemma 2.8. Let α, β ∈ R 1 be such that α/β is irrational. Then, as T → ∞, we have PT Nα ∩ Nβ ∼ PT Nα PT Nβ .


Proof. First, we note that

T

1 T

1 T

t∈Nα · t∈Nβ

PT Nα ∩ Nβ =

dt =

![image 63](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile63.png>)

![image 64](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile64.png>)

0

n T/β P−(n)>β

m T/α P−(m)>α

1 T

- (2.15) (1 − |nβ − mα|)+ ,


=

![image 65](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile65.png>)

n T/β P−(n)>β

m T/α P−(m)>α

T

0

|t−mα|<1 · |t−nβ|<1 dt

where x+ := max(0, x). Given z ∈ R 1, let Pz = p z p. Then the condition P−(m) > α is equivalent to gcd(m, Pα) = 1, and so by M¨obius inversion we have

2) 1 T

(1 − |nd2β − md1α|)+

(−1)ω(d

(−1)ω(d

1)

PT Nα ∩ Nβ =

![image 66](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile66.png>)

d2|Pβ

d1|Pα

n T/(d2β) m T/(d1α)

- (2.16) 2)PT Md1α ∩ Md2β .


(−1)ω(d

(−1)ω(d

1)

=

d2|Pβ

d1|Pα

Furthermore, note that α/β ∈/ Q if and only if d1α/(d2β) ∈/ Q for any pair of positive integers d1, d2. Therefore, by (2.11), (2.13) and (2.16) we get

1 d1αd2β

(−1)ω(d

2) ·

(−1)ω(d

1)

PT Nα ∩ Nβ ∼

![image 67](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile67.png>)

d2|Pβ

d1|Pα

1 αβ p α

=

![image 68](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile68.png>)

1 p p β

1 −

![image 69](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile69.png>)

1 p ∼ PT Nα PT Nβ

1 −

![image 70](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile70.png>)

when T → ∞, as desired.

It now remains to consider the case 1 < [α, β] < ∞, which we will split further in two cases. If [α, β] is large, we prove the following lemma, which we shall use to show that for such pairs (α, β), the sets Nα and Nβ are negatively correlated on average. Indeed, as Lemma 2.14 below shows, the error term log(2β)/(α/β) + 1/β is negligible on average.

- Lemma 2.9. Let α > β 2 be two real numbers with α/β ∈ Q \ N and [α, β] min{α2, 10β}. Then as T → ∞,


PT Nα ∩ Nβ PT Nα PT Nβ

1 β

log(2β) α/β

.

+

1 + O

![image 71](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile71.png>)

![image 72](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile72.png>)

![image 73](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile73.png>)

We shall construct our set A′ so that we can apply Lemma 2.9 to the vast majority of pairs (α, β) ∈ A′ ×A′. The remaining pairs are very few, but their treatment constitutes the hardest part of the proof. In particular, it is in this part that we need to use the machinery of GCD graphs from [21]. On the other hand, because the pairs (α, β) with 1 < [α, β] min{α2, 10β} will be arranged to be sparse, it sufﬁces to obtain less precise upper bounds for PT Nα ∩ Nβ . These are given in terms of the prime factors dividing the product of the numerator and denominator of the fraction α/β. To this end, we introduce the following useful concepts.

- Deﬁnition 2.10 (The prime numbers of a rational number). Given a prime p and a rational number ̺ > 0, we write p ∈ ̺ if we may write ̺ = a/q with gcd(a, q) = 1 and p|aq.
- Deﬁnition 2.11 (Two arithmetic functions on the rationals). Given ̺ ∈ Q>0 and z 1, we deﬁne


1 p

ω(̺; z) := #{p ∈ ̺ such that p z} and L(̺; z) :=

.

![image 74](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile74.png>)

p∈̺ p>z

Then we prove the following result:

- Lemma 2.12. Let α > β 2 be real numbers with α/β ∈ Q \ N and R := [α, β] > 1.


- (a) If L(α/β; R) 1, then as T → ∞, PT Nα ∩ Nβ


log β α/β

≪ 1 +

.

![image 75](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile75.png>)

![image 76](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile76.png>)

PT Nα PT Nβ

- (b) If L(α/β; R) > 1 and we let


z = max 2i : i ∈ Z 0, L(α/β; 2i) > 1 , then R < 2z and, as T → ∞, we have

PT Nα ∩ Nβ PT Nα PT Nβ

log β α/β

log(2z) log(2R)

≪

+

.

![image 77](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile77.png>)

![image 78](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile78.png>)

![image 79](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile79.png>)

Both Lemmas 2.9 and 2.12 will be consequences of Lemma 3.1 which we shall establish in Section 3 using an elementary sieving argument.

- 2.5. Constructing the set A′. Next, we explain how to construct a ﬁnite set A′ such that (2.14) holds. To simplify our notation, for each α > 0 we let


- (2.17) κ(α) :=

1 α p α

![image 80](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile80.png>)

1 −

1 p ≍

![image 81](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile81.png>)

1 α log(α + 2)

![image 82](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile82.png>)

,

and

λ(α) :=

1 α

![image 83](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile83.png>)

. In addition, for any ﬁnite sets B ⊂ R>0 and E ⊂ R2>0, and for µ : R>0 → R 0, we deﬁne

- (2.18) µ(B) :=

β∈B

µ(β), and µ(E) :=

(α,β)∈E

µ(α)µ(β).

By (2.1), there exists some constant c ∈ (0, 1/10) such that λ A ∩ [1, x] =

α∈A∩[1,x]

1 α

![image 84](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile84.png>)

4c log x

inﬁnitely often as x → ∞. Recall that A is 1-spaced by (2.2). This implies that α∈A∩[1,xc] 1/α 2c log x for all x sufﬁciently large. Hence, we ﬁnd that

- (2.19) λ A ∩ [xc, x] 2c log x inﬁnitely often as x → ∞.

Next, we construct a convenient sequence x1 < x2 < . . . such that xj > x1j−/c1 for all j 2, and certain sets

A′j ⊆ Aj := A ∩ [xcj, xj] j = 1, 2, . . . such that

- (2.20) λ(A′j) c log xj.


The reason we introduce the sets A′j is to guarantee Lemma 2.13(b) below. In turn, this will allow us to apply Lemma 2.9 for almost all pairs (α, β) ∈ A′ × A′.

In order to achieve the construction of A′, let us consider the following equivalence relation on A: we write α ≡ β if, and only, if α/β ∈ Q. We may then partition A into equivalence classes. For each α ∈ A, let us denote by γα the smallest element of A that lies in the same equivalence class as α. Moreover, let

Γ := {γα : α ∈ A}, which is the set of minimal representatives of the equivalent classes of A. Let us now construct the xj’s. Firstly, we take x1 to be the smallest integer e1/c for which

- (2.19) holds, and we let A′1 = A1 = A ∩ [xc1, x1]. In particular, (2.20) holds.


Next, assume we have constructed x1, . . ., xj and A′1, . . ., A′j such that xci > xi−1 and (2.20) holds for i = 2, . . ., j. Consider the quantities

1 γ

Qj = max 10ααH(α/γα) : α ∈ A1 ∪ · · · ∪ Aj and Sj = Q2j

.

![image 85](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile85.png>)

γ∈Γ∩[1,xj]

In addition, let Bj be the set of α ∈ A for which there exists γ ∈ Γ ∩ [1, xj] and a reduced fraction a/q such that q Qj and α = γa/q. For each given γ and q, the set {a ∈ N : γa/q ∈ A} is primitive. We may thus apply (1.7) to show that

log x √log log x

1 a ≪

.

![image 86](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile86.png>)

![image 87](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile87.png>)

![image 88](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile88.png>)

q a qx γa/q∈A

Consequently, λ Bj ∩ [1, x]

1 γ q Q

![image 89](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile89.png>)

γ∈Γ∩[1,xj]

j

1 a ≪

q

![image 90](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile90.png>)

q a qx γa/q∈A

1 γ q Q

![image 91](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile91.png>)

γ∈Γ∩[1,xj]

j

q ·

log x √log log x

Sj ·

. Therefore, there exists a constant yj such

![image 92](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile92.png>)

![image 93](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile93.png>)

log x √log log x

![image 94](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile94.png>)

![image 95](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile95.png>)

λ Bj ∩ [1, x] c log x for all x yj.

We then take xj+1 to be the smallest integer > max{yj, x1j/c} such that (2.19) holds. Hence, if we set

A′j+1 := Aj+1 \ Bj, then (2.20) holds. Fix J large and denote

J

A′ :=

A′j. This completes the construction of the set A′. We show that it satisﬁes the following properties.

j=1

- Lemma 2.13. Let A′ be as above.


- (a) We have cJ ≪

α∈A′

PT(Nα) ≪ J log(1/c).

- (b) If α, β ∈ A′ are such that α > β and [α, β] 10β, then there exists j ∈ {1, 2, . . ., J} such that α, β ∈ A′j.


Proof. (a) By (2.13) and Mertens’ theorem we have

- (2.21)

α∈A′

PT(Nα) ≍

J

j=1 α∈A′j

1 α log α

![image 96](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile96.png>)

.

Furthermore, by (2.20) and the fact that A is 1-spaced, we get

- (2.22) c ≪


α∈A′j

1 α log α α∈A

![image 97](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile97.png>)

j

1 α log α ≪ log(1/c).

![image 98](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile98.png>)

Inserting this estimate in (2.21) completes the proof of part (a).

(b) Since α > β there exists 1 j i J such that α ∈ A′i and β ∈ A′j. Assume for contradiction that i > j. Since [α, β] 10β, we must have α/β ∈ Q and hence there exists γ ∈ Γ such that α = γa/q and β = γb/r with a/q and b/r reduced fractions 1. In particular, γ β xj xi−1. Since α = γa/q ∈ A \ Bi−1, we must have that q > Qi−1 10ββH(β/γ).

Now, note that αβ = a

1r1

b1q1 , where a1 = a/ gcd(a, b), r1 = r/ gcd(q, r), b1 = b/ gcd(a, b) and q1 = q/ gcd(q, r). We have gcd(a1r1, b1q1) = 1. Hence,

![image 99](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile99.png>)

![image 100](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile100.png>)

q βr

q βH(β/γ)

b1q1 β

> 10β, which gives a contradiction. This completes the proof of part (b).

[α, β] =

![image 101](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile101.png>)

![image 102](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile102.png>)

![image 103](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile103.png>)

- 2.6. The last key result towards Theorem 1. Let us now explain how to put together all of the above ingredients. This will reduce Theorem 1 to the key Proposition 2.15 below.


Recall that Theorem 1 follows from (2.7), which in turn can be deduced from (2.14). To show this last relation, we apply Lemma 2.1 with the events Ei being the sets Nα with α ∈ A′. We have

PT(Nα) ∼ κ(A′) ≍c J

α∈A′

by Lemma 2.13(a), where κ(A′) is deﬁned in (2.17) and (2.18). Thus, it sufﬁces to show, as T → ∞,

- (2.23) PT Nα ∩ Nβ κ(A′)2 + Oc J ,

in which case we may conclude

PT

α∈A′

Nα

κ(A′)2 κ(A′)2 + Oc κ(A′)

![image 104](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile104.png>)

= 1 − Oc

1 J

![image 105](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile105.png>)

,

by Lemma 2.1. This will complete the proof of (2.14) (and thus of Theorem 1) if we take J to be suitably large.

Combining the estimates in Lemmas 2.6, 2.8, 2.9 and 2.12, we obtain that

α,β∈A′, α>β

PT Nα ∩ Nβ

α,β∈A′, α>β

- (2.24) PT Nα)PT Nβ + O E1 + E2 + E3


α,β∈A′ α =β

as T → ∞, where

- E1 :=

α,β∈A′, α>β

κ(α)κ(β) ·

1 β

![image 106](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile106.png>)

+

log β α/β

![image 107](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile107.png>)

,

- E2 :=

α,β∈A′, α>β 1<[α,β]<min{α2,10β}

κ(α)κ(β),

- E3 :=


i + 1 log(2[α, β])

κ(α)κ(β) ·

.

![image 108](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile108.png>)

i 0 α,β∈A′, α>β

1<[α,β]<min{α2,10β} 2i+1>[α,β], L(α/β;2i)>1

We ﬁrst show that the contribution of E1 is negligible. This follows from the following basic lemma.

- Lemma 2.14. If C ⊂ R 2 is 1-spaced, then


1 α log α ·

1 β log β ·

![image 109](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile109.png>)

![image 110](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile110.png>)

α,β∈C, α>β

log β α/β ≪ κ(C).

1 β

+

![image 111](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile111.png>)

![image 112](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile112.png>)

Proof. Indeed, the sum in question simpliﬁes as

1 β2 log β

1 α2 log α ≪

1 α log α β∈C

+

![image 113](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile113.png>)

![image 114](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile114.png>)

![image 115](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile115.png>)

β∈C α∈C α>β

α∈C

α∈C

β<α

1 α log α

![image 116](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile116.png>)

1 β log β ≍ κ(C),

+

![image 117](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile117.png>)

β∈C

since C is 1-spaced. This completes the proof. This result, together with Lemma 2.13(a), implies that

- (2.25) E1 ≪ κ(A′) ≍c J.

To bound E2, note that Lemma 2.13(b) and the condition [α, β] 10β in its range of summation imply that there exists j ∈ {1, 2, . . ., J} such that α, β ∈ A′j. Hence,

E2

J

j=1

κ(A′j)2 ≪c J by (2.22).

It remains to bound E3. As in the case of E2, there must exist some j ∈ {1, 2, . . ., J} such that α, β ∈ A′j ⊆ Aj. In particular, the condition [α, β] < α2 and the deﬁnition of [α, β] imply that H(α/β) < x3j. Since log α ≍c log xj for each α ∈ Aj, we also have that κ(α) ≪c λ(α)/ logxj (and similarly for β). Thus we conclude that

- (2.26) E3 ≪c


∞

i

J

i + 1 r + 1

1 (log xj)2

λ(α)λ(β).

![image 118](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile118.png>)

![image 119](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile119.png>)

r=0

i=0

j=1

(α,β)∈A2j H(α/β)<x3j, 2r<[α,β] 2r+1, L(α/β;2i)>1

We claim that we have the following key bound: Proposition 2.15. Let x 3, let y, z 1, and let B ⊆ [1, x] be a 1-spaced set such that α/β ∈/ N for all distinct α, β ∈ B. We have the uniform estimate

λ (α, β) ∈ B × B : H(α/β) x3, y < [α, β] 2y, L(α/β; z) > 1 ≪ ye−z(log x)2.

In view of (2.3) and (2.26), we may apply the above proposition with B = Aj, x = xj, y = 2r and z = 2i to ﬁnd that

∞

∞

J

i

i + 1 r + 1 · 2re−2

i

i

2ie−2

E3 ≪c

≍ J

≍ J.

![image 120](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile120.png>)

r=0

j=1

i=0

i=0

Therefore, to complete the proof of (2.14) (and hence of Theorem 1), it sufﬁces to prove Lemmas

- 2.9 and 2.12, as well as Proposition 2.15. The remainder of the paper is organized as follows:


- • We prove Lemmas 2.9 and 2.12 in Section 3.
- • We prove a generalization of Behrend’s estimate (1.6) in Section 4.
- • In Sections 5 and 6, we reduce Proposition 2.15 to the case when A is a set of rational numbers. This is the context of Proposition 6.2.
- • We introduce the language of GCD graphs and various results about them in Section 7. Then, in Section 8 we show how to deduce from them Proposition 6.2. The ﬁnal sections of the paper are devoted to proving the needed results about GCD graphs.


3. THE OVERLAP ESTIMATE FOR RATIONAL RATIOS

The purpose of this section is to establish the following result and deduce Lemmas 2.9 and 2.12 from it.

- Lemma 3.1. Let α > β 2 be two real numbers with α/β ∈ Q \ N, let y 100 be a parameter, and assume that R := [α, β] > 1. Then, as T → ∞, we have

PT Nα ∩ Nβ PT Nα PT Nβ

![image 121](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile121.png>)

3L(α/β;y) 1 + O(η) + O

log(2β) α/β

![image 122](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile122.png>)

(3.1)

with η = min 2βR−1/2, 3ω(α/β;y)(1 + log R)/R , as well as

- (3.2)


PT Nα ∩ Nβ PT Nα PT Nβ

![image 123](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile123.png>)

≪ eL(α/β;R) +

log(2β) α/β

![image 124](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile124.png>)

.

3.1. Auxiliary results. We shall make frequent use of the following basic estimate about averages of non-negative, divisor-bounded multiplicative functions.

- Lemma 3.2 (Bounds on multiplicative functions). Let k ∈ N and write τk for the k-th divisor function. If f is a multiplicative function such that 0 f τk, then

n x

f(n) ≪k

x log x · exp

![image 125](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile125.png>)

p x

f(p) p ≍k x · exp

![image 126](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile126.png>)

p x

f(p) − 1 p

![image 127](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile127.png>)

(x 2).

Moreover,

n x

f(n) n ≍k exp

![image 128](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile128.png>)

p x

f(p) p

![image 129](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile129.png>)

(x 2).

Proof. The ﬁrst part of the lemma follows readily from [20, Theorem 14.2, p. 145]. For the second part, see [20, Exercise 14.5, p. 154].

We also need the following elementary estimate.

- Lemma 3.3. Let t 1 be a real number and q ∈ N.


- (a) We have

1 |j| t

(1 − |j|/t) = t − 1 + O(1/t).

- (b) We have


1 p

+ O 2ω(q) .

1 −

(1 − |j|/t) = t

![image 130](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile130.png>)

1 |j| t (q,j)=1

p|q

- (c) We have


- p − 1

![image 131](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile131.png>)

- p − 2 ≪ t


p|q p t

1 |j| t (j,q)=1

p|j p>2

1 p

1 −

![image 132](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile132.png>)

.

Proof. (a) Using the Euler–Maclaurin summation formula [20, Theorem 1.10], we ﬁnd that

(1 − |j|/t) = 2

(1 − j/t) = 2

0<j t

1 |j| t

t

2 t

(1 − y/t) dy −

![image 133](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile133.png>)

0

t

{y} dy

0

We have 0 t(1 − y/t) dy = t/2 and 0 t{y} dy = t/2 + O(1), with the last estimate following by periodicity. This completes the proof.

- (b) By M¨obius inversion and part (a), we have

1 |j| t (q,j)=1

(1 − |j|/t) =

1 |j| t

(1 − |j|/t)

d|(q,j)

µ(d) j==di

d|q

µ(d)

1 |i| t/d

1 −

|i| t/d

![image 134](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile134.png>)

=

d|q

µ(d) t/d + O(1) = t

p|q

(1 − 1/p) + O(2ω(q)).

- (c) This follows from Lemma 3.2 above applied to f(n) = (n,q)=1 p|n,p>2 pp−−12, which is


![image 135](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile135.png>)

indeed a non-negative and divisor-bounded multiplicative function.

- 3.2. Proof of Lemma 3.1. Recall by (2.15) that


1 T

1 T

1 − |mα − nβ| + + O

P Nα ∩ Nβ =

- (3.3) .

Here we dropped the condition that mα T, since for all but O(1) values of n, it is a consequence of the condition |mα − nβ| < 1 that is implicit in the above double sum. In addition, note that |m − nt/s| = |m − nβ/α| < 1/α 1/2 for m and n as above. Hence, given a β-rough natural number n, there is at most one choice for m, which is given by the nearest integer to nt/s. This choice is admissible if, and only if, nt/s < 1/α and the resulting m is α-rough, in which case we have

|mα − nβ| = α|m − nt/s| = α nt/s . We must ﬁnd a convenient way to express all this data.

Since gcd(s, t) = 1, there exist integers u, v such that

- (3.4) ut = 1 + vs.


![image 136](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile136.png>)

![image 137](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile137.png>)

P−(m)>α

P−(n)>β nβ T

We must then have gcd(u, s) = 1, and so we may deﬁne the residue class nu (mod s). Choosing the unique representative j of this class lying in (−s/2, s/2], there exists a unique way to write

![image 138](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile138.png>)

n = ks + uj with − s/2 < j s/2, j, k ∈ Z. We then ﬁnd that

uj s

T βs −

uj s

0 < nβ T ⇐⇒ −

< k

.

![image 139](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile139.png>)

![image 140](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile140.png>)

![image 141](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile141.png>)

In addition,

- (3.5)

nt s

![image 142](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile142.png>)

= kt +

ujt s

![image 143](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile143.png>)

= kt + vj +

j s

![image 144](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile144.png>)

. Now, using (3.5), we ﬁnd readily that nt/s = |j|/s and so

- (3.6) |mα − nβ| = α nt/s = α|j|/s = |j|/R,

where we used that α > β to ﬁnd that R = [α, β] = H(α/β)/ max{α, β} = s/α. Since R = s/α, we also ﬁnd that

T βs

![image 145](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile145.png>)

=

T αβR

![image 146](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile146.png>)

.

Next, observe that (3.6) renders the condition |mα − nβ| < 1 equivalent to having |j| < R. Since R = s/α and α > 2, the condition |j| < R is stronger than our prior condition −s/2 < j s/2. In particular, we must have |j| < s/2, and thus relation (3.5) implies that the nearest integer to nt/s equals kt + vj = m. Lastly, note that if j = 0, then m = kt and n = ks. Consequently, k and t must be α-rough, s must be β-rough, and we must also have mα = nβ. Using Lemma 2.7, we deduce further that R = [α, β] > α/β in the case when j = 0.

In summary, we see that (3.3) becomes

- (3.7) P Nα ∩ Nβ =

1 T

![image 147](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile147.png>)

0 |j| R

1 −

|j| R · Sj + O

![image 148](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile148.png>)

1 T

![image 149](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile149.png>)

,

where

Sj :=

−uj/s<k αβR T −uj/s P−(kt+vj)>α, P−(ks+uj)>β

![image 150](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile150.png>)

1

for j = 0 and

S0 := P−(s)>β P−(t)>α R>α/β

k αβR T P−(k)>α

![image 151](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile151.png>)

1.

For S0, we use directly the fundamental lemma of sieve methods to ﬁnd that

k αβR T P−(k)>α

![image 152](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile152.png>)

1 ∼

T αβR p α

![image 153](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile153.png>)

1 −

1 p ∼

![image 154](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile154.png>)

T R

![image 155](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile155.png>)

PT Nα PT Nβ

p β

1 −

1 p

![image 156](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile156.png>)

−1

.

Using Mertens’ theorem and that we must have R > α/β for S0 to be non-zero, we conclude that

- (3.8) S0 ≪ T PT Nα PT Nβ


log(2β) α/β

.

![image 157](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile157.png>)

Let us now estimate Sj when j = 0. Note that if there exists a prime p β that divides j and st, then Sj = 0. Similarly, if there exists a prime p ∈ (β, α] that divides j and t, then Sj = 0. Lastly, note that if 2 ∤ jst, then ks + uj ≡ k + u (mod2) and kt + vj ≡ k + v (mod2). In addition, we have that u ≡ 1 + v (mod2) by (3.4). This implies that 2|(k + u)(k + v) for all k. In particular, there are no k with P−(ks + uj) > β and P−(kt + vj) > α, so that Sj = 0 again in this case.

In conclusion, if we let

p and Q2 :=

Q1 :=

p,

β<p α, p|t

p β, p|st

then we have that

- (3.9) Sj = 0 when gcd(j, Q1Q2) > 1 or when 2 ∤ jQ1. Finally, we estimate Sj when gcd(j, Q1Q2) = 1 and 2|jQ1. For any prime p β, we have

−uj/s<k αβR T −uj/s p|(ks+uj)(kt+vj)

![image 158](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile158.png>)

1 =

T αβR ·

![image 159](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile159.png>)

ν1(p) p

![image 160](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile160.png>)

+ O(ν1(p)),

where

ν1(p) := # k ∈ Z/pZ : (ks + uj)(kt + vj) ≡ 0 (modp) .

- If p|s, then p ∤ j by our assumption that gcd(j, Q1) = 1. In addition, p ∤ ut by (3.4). So ν1(p) = 1 for such primes. Similarly, if p|t, then ν1(p) = 1. Assume now that p ∤ st. Then, ν1(p) = 2, unless

jus ≡ jvt(modp) ⇐⇒ jut ≡ jvs (modp) ⇐⇒ j ≡ 0 (modp), where we used (3.4). In conclusion,

![image 161](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile161.png>)

![image 162](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile162.png>)

ν1(p) =

- 1 if p|jQ1,
- 2 otherwise.


In particular, ν1(2) = 1 because we have assumed that 2|jQ1. Similarly, for any prime p ∈ (β, α], we have

−uj/s<k αβR T −uj/s p|kt+vj

![image 163](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile163.png>)

1 =

T αβR ·

![image 164](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile164.png>)

ν2(p) p

![image 165](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile165.png>)

+ O(ν2(p)),

where

ν2(p) := # k ∈ Z/pZ : kt + vj ≡ 0 (modp) .

- If p|t, then p ∤ j by our assumption that gcd(j, Q2) = 1. In addition, we have p ∤ v by (3.4). So ν2(p) = 0 for such primes. On the other hand, if p ∤ t, then ν2(p) = 1. In conclusion,


ν2(p) =

- 0 if p|Q2,
- 1 otherwise.


Using the fundamental lemma of sieve methods [20, Theorem 18.11] and the fact that ν1(2) = 1, we ﬁnd that

Sj ∼

T αβR p β

![image 166](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile166.png>)

1 −

ν1(p) p β<p α

![image 167](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile167.png>)

1 −

ν2(p) p

![image 168](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile168.png>)

=

T 2αβR 3 p β

![image 169](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile169.png>)

p|jQ1

1 −

1 p 3 p β

![image 170](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile170.png>)

p∤jQ1

1 −

2 p β<p α

![image 171](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile171.png>)

p∤Q2

1 −

1 p

![image 172](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile172.png>)

=

T 2αβR

![image 173](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile173.png>)

p|jQ1, p>2

- p − 1

![image 174](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile174.png>)

- p − 2


p|Q2

p p − 1 3 p β

![image 175](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile175.png>)

1 −

2 p β<p α

![image 176](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile176.png>)

1 −

1 p

![image 177](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile177.png>)

- (3.10)


as T → ∞.

Lastly, note that PT Nα PT Nβ ∼ 4αβ1 3 p β(1−1/p)2 β<p α(1−1/p). Hence, combining

![image 178](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile178.png>)

- (3.7), (3.8), (3.9) and (3.10), we deduce that


PT Nα ∩ Nβ PT Nα PT Nβ

- p − 1

![image 179](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile179.png>)

- p − 2


p p − 1

log(2β) α/β

2CS R

∼

- (3.11) ,

where

C :=

3 p β

1 − 2/p (1 − 1/p)2

![image 180](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile180.png>)

and S :=

1 |j| R gcd(j,Q1Q2)=1, 2|jQ1

1 −

|j| R 3 p β

![image 181](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile181.png>)

p|j

- p − 1

![image 182](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile182.png>)

- p − 2


.

To prove (3.2), note that (3.11) implies that

lim

T→∞

PT Nα ∩ Nβ PT Nα PT Nβ

![image 183](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile183.png>)

≪

S R ·

![image 184](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile184.png>)

p|Q1Q2

1 +

1 p

![image 185](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile185.png>)

+

log(2β) α/β

![image 186](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile186.png>)

.

To bound S, we note that 0 1 − |j|/R 1 for |j| R and then apply Lemma 3.3(c). This completes the proof of (3.2).

Let us now prove (3.1). We wish to estimate S. Given y 100 as in the statement of Lemma 3.1, let Q = p|Q

1Q2, p y p. In addition, note that

3 p β p|j

- p − 1

![image 187](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile187.png>)

- p − 2


=

d|j, d|P

f(d) with P :=

3 p β

p and f(d) :=

p|d p>2

1 p − 2

![image 188](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile188.png>)

.

Hence,

S

1 |j| R gcd(j,Q)=1, 2|jQ1

1 −

|j| R 3 p β

![image 189](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile189.png>)

p|j

- p − 1

![image 190](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile190.png>)

- p − 2


j==di

d|P, d R gcd(d,Q)=1

f(d)

1 |i| R/d gcd(i,Q)=1, 2|diQ1

1 −

|i| R/d

![image 191](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile191.png>)

- (3.12) .

Fix d|P such that d R. We claim that

- (3.13)


+ O

![image 192](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile192.png>)

![image 193](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile193.png>)

![image 194](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile194.png>)

![image 195](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile195.png>)

p|Q1, p>2

p|Q2

|i| R/d

R 2d

1 p

+ O(2ω(Q)).

1 −

1 −

=

![image 196](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile196.png>)

![image 197](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile197.png>)

![image 198](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile198.png>)

1 |i| R/d gcd(i,Q)=1, 2|diQ1

p|Q,p>2

Indeed, if 2|Q1 (and thus 2|Q), then the condition 2|diQ1 holds for all i. Hence, using Lemma 3.3(b) with t = R/d establishes (3.13), since 2|Q here. On the other hand, if 2 ∤ Q1, then the condition 2|diQ1 implies that 2|i (note here that d is odd because it divides P). Writing i = 2i′, and applying Lemma 3.3(b) with t = R/(2d) proves (3.13) in this case too.

Combining (3.12) and (3.13), we conclude that S

1 p

R 2d

+ O(2ω(Q)) .

1 −

f(d) ·

![image 199](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile199.png>)

![image 200](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile200.png>)

p|Q,p>2

d|P, d R gcd(d,Q)=1

In addition, note that

f(d) d

f(d) d d|P

![image 201](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile201.png>)

![image 202](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile202.png>)

d|P, d R gcd(d,Q)=1

gcd(d,Q)=1

=

3 p β p∤Q

f(p) p

1 +

![image 203](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile203.png>)

p(p − 2) (p − 1)2

1 C p|Q

=

,

![image 204](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile204.png>)

![image 205](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile205.png>)

3 p β

since 1 + f(p)/p = (p − 1)2/(p(p − 2)) = (1 − 2/p)−1(1 − 1/p)2 for p > 2. Moreover, letting g(n) = n|P · nf(n), we deduce by the second part of Lemma 3.2 that

g(d)

d ≪ log(2R). Consequently,

f(d) =

![image 206](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile206.png>)

d R

d|P, d R

S

p − 2 p − 1

R 2C

![image 207](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile207.png>)

![image 208](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile208.png>)

p|Q 3 p β

p|Q p>β

p − 1 p

+ O 2ω(Q) log(2R)

![image 209](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile209.png>)

=

R 2C

+ O 3ω(Q) log(2R)

![image 210](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile210.png>)

p − 1 p

p − 2 p − 1

.

![image 211](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile211.png>)

![image 212](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile212.png>)

p|Q p>β

p|Q 3 p β

Since {p|Q : 3 p β} = {p|Q1 : 3 p y} and {p|Q : p > β} = {p|Q2 : p y}, we conclude that

p − 1 p

p − 2 p − 1

R 2C

+ O 3ω(Q) log(2R)

.

S

![image 213](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile213.png>)

![image 214](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile214.png>)

![image 215](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile215.png>)

p|Q2 p y

p|Q1 3 p y

Furthermore, note that p−p1 pp−−12 31/p for p y 100. Therefore, S

![image 216](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile216.png>)

![image 217](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile217.png>)

p − 1 p

p − 2 p − 1

R 2C

1 p

+ O 3ω(Q) log(2R) 3

.

![image 218](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile218.png>)

p|st, p>y

![image 219](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile219.png>)

![image 220](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile220.png>)

![image 221](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile221.png>)

- (3.14)


p|Q2

p|Q1 p>2

Finally, note that ω(Q) ω(st; y) = ω(α/β; y), as well as ω(Q) #{p β} + ω(t) 0.5β + 0.4 log t + O(1). Since t = Rβ, we conclude that

3ω(Q) log(2R) ≪ min 3ω(α/β;y) log(2R), 2βR1/2 R · η.

Inserting the above estimate into (3.14), and then combining the resulting inequality with (3.11) completes the proof of (3.1), and hence of Lemma 3.1.

3.3. Deduction of Lemmas 2.9 and 2.12 from Lemma 3.1.

Proof of Lemma 2.9. We use the estimate (3.1) in Lemma 3.1 with y = ∞. Let R = [α, β], and let us ﬁrst consider the case when R α2. Write α/β = s/t for coprime integers s, t. Since α > β, we have t < s = Rα R3/2, and thus ω(α/β; ∞) = ω(st) ≪ log R/ log log R. Hence,

1 α

1 β

1 + log R R ≪ R−1/2

3ω(α/β;∞)

. Hence, we have established the claimed estimate in the case when α/β ∈ Q and R α2. Finally, let us consider the case when α/β ∈ Q and R 10β. We then note that 2β R1/2 ≪

![image 222](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile222.png>)

![image 223](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile223.png>)

![image 224](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile224.png>)

1 β

.

![image 225](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile225.png>)

![image 226](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile226.png>)

Hence, Lemma 3.1, applied with y = ∞, completes the proof once again. Proof of Lemma 2.12. We apply estimate (3.2) in Lemma 3.1 to ﬁnd that

PT Nα ∩ Nβ PT Nα PT Nβ

log β α/β

≪ eL(α/β;R) +

- (3.15)


![image 227](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile227.png>)

![image 228](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile228.png>)

as T → ∞. Clearly, this proves part (a) of the lemma.

Let us now prove part (b), in which case L(α/β; R) > 1. By the deﬁnition of z, we have L(α/β; z) > 1 L(α/β; 2z). Since L(α/β; R) > 1 here, we must have R < 2z as claimed. In addition, we have

L(α/β; R)

1 p

![image 229](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile229.png>)

R<p 2z

+ L(α/β; 2z) log

log(2z) log(2R)

![image 230](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile230.png>)

+ O(1)

by Mertens’ theorem. Inserting this bound into (3.15) completes the proof.

4. A REFINEMENT OF BEHREND’S THEOREM

In order to prove Proposition 2.15, we shall need the following generalization of a result due to Behrend:

Theorem 4.1. Let z y 2, let A ⊂ N be a primitive set, and let f be a multiplicative function such that 0 f τk for some ﬁxed integer k. If we let L = p y f(pp), then we have the uniform estimate

![image 231](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile231.png>)

f(p) − 1 p

f(a) a ≪k

log y √L + 1 · exp

.

![image 232](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile232.png>)

![image 233](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile233.png>)

![image 234](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile234.png>)

![image 235](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile235.png>)

p z

a∈A∩[z/y,z]

Proof. Set A′ = A ∩ [z/y, z], and deﬁne r(n) :=

r(n) n

f(a)f(n/a) and R :=

.

![image 236](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile236.png>)

a∈A′, a|n n/a square-free

z/y n zy

Notice that

- (4.1) R


f(m) m ≫k

f(a) a m y

![image 237](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile237.png>)

![image 238](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile238.png>)

a∈A′

m square-free

f(a) a · eL,

![image 239](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile239.png>)

a∈A′

by the second part of Lemma 3.2. Next, we give an upper bound on R.

Let g be the multiplicative function deﬁned by g(pk) = max{f(pk), f(p)f(pk−1)}, so that g(p) = f(p). Note that f(a)f(n/a) g(n) whenever a|n and n/a is square-free. Hence,

- (4.2) r(n) g(n)#{a ∈ A′ : a|n, n/a square-free} =: g(n) r(n).


If n zy and a ∈ A′, then n/a y2 because a z/y. In particular, n/a divides the y2-smooth part of the radical of n. In addition, if a and b are distinct divisors of n from the set A′, then n/a does not divide n/b by our assumption that A is primitive. Hence, the integers counted by r(n) are in 1-1 correspondence with a set D consisting of integers that divide p y2, p|n p and that they do not divide each other. In particular, Sperner’s theorem [24] implies that

2)/ max{1, ω(n; y2)}.

![image 240](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile240.png>)

r(n) = |D| 2ω(n;y

Hence,

r(n)

2ω(n;y2)/√L + 1 if ω(n; y2) L + 1, 2L+1 otherwise.

![image 241](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile241.png>)

Together with (4.2), this implies that

R

g(n)2ω(n;y2) n

1 √L + 1 z/y n zy

![image 242](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile242.png>)

![image 243](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile243.png>)

![image 244](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile244.png>)

g(n) n

+ 2L+1

.

![image 245](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile245.png>)

z/y n zy

Using the ﬁrst part of Lemma 3.2 and partial summation, we ﬁnd that

g(n)2ω(n;y2) n ≪k

![image 246](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile246.png>)

z/y n zy

- log y

![image 247](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile247.png>)

- log z


exp

≍k e2L exp

2f(p) p

+

![image 248](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile248.png>)

p y2

f(p) − 1 p

![image 249](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile249.png>)

y<p z

f(p) p

![image 250](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile250.png>)

y2<p zy

,

as well as

g(n) n ≪k (2e)L exp

2L+1

![image 251](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile251.png>)

z/y n zy

f(p) − 1 p

![image 252](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile252.png>)

y<p z

.

In conclusion,

R ≪k

e2L √L + 1

exp

![image 253](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile253.png>)

![image 254](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile254.png>)

f(p) − 1 p

![image 255](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile255.png>)

y<p z

.

Comparing the above estimate with (4.1), and noticing that L = log log y + p y f(pp)−1 by Mertens’ theorem completes the proof.

![image 256](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile256.png>)

Corollary 4.2. Fix C 1. Let z y 3 and let q ∈ N ∩ [1, yC]. In addition, let A ⊂ N be a primitive set, and let f be a multiplicative function such that 1 f τk for some ﬁxed integer k. Then

f(p) − 1 p

f(a) a ≪k,C

log y √log log y · exp

ϕ(q) q ·

.

![image 257](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile257.png>)

![image 258](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile258.png>)

![image 259](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile259.png>)

![image 260](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile260.png>)

![image 261](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile261.png>)

p z

a∈A∩[z/y,z] gcd(a,q)=1

Proof. First of all, note that

- (4.3)


f(p) p

= Ok,C(1).

![image 262](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile262.png>)

p|q, p>y

Indeed, if p|q, then we have p q yC, and thus the above estimate follows by Mertens’ theorem and the fact that 0 f(p) k.

We are now ready to prove the corollary, which we will accomplish by applying Theorem 4.1 to the multiplicative function g(a) := f(a) · gcd(a,q)=1. Using (4.3) and our assumptions that z y and that f 1, we have

g(p) p

=

![image 263](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile263.png>)

p z

f(p) p −

![image 264](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile264.png>)

p z

p|q

f(p) p

+ Ok,C(1)

![image 265](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile265.png>)

f(p) p −

![image 266](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile266.png>)

p z

p|q

1 p

+ Ok,C(1).

![image 267](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile267.png>)

Thus, Theorem 4.1 implies that

- (4.4)


f(a) a ≪k,C

![image 268](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile268.png>)

a∈A∩[z/y,z] gcd(a,q)=1

ϕ(q) q ·

log y √L + 1 · exp

![image 269](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile269.png>)

![image 270](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile270.png>)

![image 271](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile271.png>)

f(p) − 1 p

![image 272](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile272.png>)

p z

with L = p y g(p)/p. Using (4.3) once again, as well as our assumption that 1 f τk, we ﬁnd that

f(p) p p y

k p

1 p −

f(p) p −

+ Ok,C(1).

L =

![image 273](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile273.png>)

![image 274](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile274.png>)

![image 275](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile275.png>)

![image 276](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile276.png>)

p y

p y, p|q

p|q

Moreover, p|q 1/p log log log y + OC(1) because q yC. As a consequence, we have L + 1 ≫k,C log log y. Together with (4.4), this completes the proof of the corollary.

5. WEIGHTED BIPARTITE GRAPHS

- Deﬁnition 5.1 (weight of a set). Let µ : S → R 0 be a weight function deﬁned on a set S. Given ﬁnite sets T ⊆ S and E ⊆ S2, we deﬁne their weight to be

µ(T ) :=

t∈T

µ(t) and µ(E) :=

(s,t)∈E

µ(s)µ(t).

- Deﬁnition 5.2 (weighted bipartite graph). Let G be a quadruple (µ, V, W, E) such that

- (a) µ : R>0 → R>0 is a positive weight function;
- (b) V and W are ﬁnite sets of positive real numbers;
- (c) E ⊆ V × W, that is to say (V, W, E) is a bipartite graph.


We then call G a weighted bipartite graph with sets of vertices (V, W) and set of edges E.

In addition, we say that G is non-trivial if E = ∅ or, equivalently, if µ(E) > 0. (We must then also have that µ(V), µ(W) > 0.)

- Deﬁnition 5.3 (edge density and θ-weight). Let G = (µ, V, W, E) be a weighted bipartite graph.


- (a) If G is non-trivial, the (weighted) edge density of G is deﬁned by

δ(G) =

µ(E) µ(V)µ(W)

![image 277](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile277.png>)

. Otherwise, we deﬁne δ(G) = 0.

- (b) Let θ 1. The θ-weight of G is deﬁned by µ(θ)(G) := δ(G)θµ(V)µ(W).


Remarks. (a) Since the edge density of a graph is always 1, we have

′)(G) µ(θ)(G) µ(E) for all θ′ θ 1. (b) If G is non-trivial, then we have that

- (5.1) µ(θ


µ(E)θ µ(V)θ−1µ(W)θ−1

- (5.2) µ(θ)(G) =


.

![image 278](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile278.png>)

- Deﬁnition 5.4 (Subgraph). Consider two weighted bipartite graphs G = (µ, V, W, E) and G′ = (µ′, V′, W′, E′). We say that G′ is a subgraph of G if

µ′ = µ, V′ ⊆ V, W′ ⊆ W, E′ ⊆ E.

We say that G′ is a non-trivial subgraph of G if µ(E′) > 0, that is to say if G′ is non-trivial as a weighted bipartite graph.

- Deﬁnition 5.5 (Maximal graph). Let G = (µ, V, W, E) be a weighted bipartite graph. We say that G is θ-maximal if for every subgraph G′ = (µ, V′, W′, E′) of G, we have that µ(θ)(G) µ(θ)(G′).


Remarks. (a) Hauke–Vazquez–Walker use a related notion in their work [19] – see the deﬁnition of E′ in Section 3 of their paper. They employed it to prove a result that is very similar to Lemma

- 5.9. The notion of maximal graphs also appears in [22, Deﬁnition 5].


(b) For any given graph G = (µ, V, W, E), since both the sets V and W are ﬁnite, there exists a maximal subgraph G′ of G. To see this, just list all subgraphs of G, and pick out one with the largest possible θ-weight. We will use this fact several times in the later sections without mentioning it again.

Lemma 5.6. Let θ 1, let G = (µ, V, W, E) be a non-trivial weighted bipartite graph and let G′ be a subgraph of G such that µ(θ)(G′) > µ(θ)(G). We then have that

δ(G′) > δ(G) and

µ(θ′)(G′) µ(θ′)(G)

![image 279](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile279.png>)

µ(θ)(G′) µ(θ)(G)

> 1 for all θ′ θ.

![image 280](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile280.png>)

Proof. We have µ(θ)(G) > 0 because G is non-trivial. Thus µ(θ)(G′) > µ(θ)(G) > 0, which implies that the graph G′ is also non-trivial.

Now, let G′ = (µ, V′, W′, E′). Since V′ ⊆ V and W′ ⊆ W, we have

µ(θ)(G′) δ(G′)θµ(V)µ(W). Together with our assumption that µ(θ)(G′) > µ(θ)(G), this implies that δ(G′) > δ(G), as needed.

Lastly, note that

θ′−θ

µ(θ′)(G′)/µ(θ′)(G) µ(θ)(G′)/µ(θ)(G)

δ(G′) δ(G)

1

=

![image 281](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile281.png>)

![image 282](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile282.png>)

for all θ′ θ, since we have already established that δ(G′)/δ(G) 1. This completes the proof of the lemma.

Remark. In virtue of Lemma 5.6, if G is θ-maximal for some θ 1, then it is θ′-maximal for all θ′ ∈ [1, θ]. Indeed, it this were false, then there would exist some θ′ ∈ [1, θ] and a subgraph G′ of G such that µ(θ′)(G′) > µ(θ′)(G). But then Lemma 5.6 (with the roles of θ′ and θ reversed) would imply that µ(θ)(G′) > µ(θ)(G), which contradicts the maximality of G.

- Deﬁnition 5.7 (Induced set of edges and subgraph). Let G = (µ, V, W, E) be a weighted bipartite graph. If V′ ⊆ V and W′ ⊆ W, we deﬁne

E(V′, W′) := E ∩ (V′ × W′)

and call it the set of edges induced by V′ and W′. Similarly, we call (µ, V′, W′, E(V′, W′)) the subgraph of G induced by V′ and W′.

- Deﬁnition 5.8 (Neighbourhood sets and connectivity). Let G = (µ, V, W, E) be a weighted bipartite graph.


- (a) We deﬁne the neighbourhood sets by

- ΓG(v) := {w ∈ W : (v, w) ∈ E} for any v ∈ V,

and

- ΓG(w) := {v ∈ V : (v, w) ∈ E} for any w ∈ W.


- (b) We say that G is η-connected if for all v ∈ V and all w ∈ W we have µ(ΓG(v)) η · µ(W) and µ(ΓG(w)) η · µ(V).


The notion of maximality implies good connectivity for all vertices.

- Lemma 5.9 (Maximality implies connectivity). Let G = (µ, V, W, E) be a weighted bipartite graph with edge density δ > 0. If G is θ-maximal for some θ > 1, then G is (θ−θ1 · δ)-connected. Proof. We use a simple modiﬁcation of the argument leading to [21, Lemma 10.1] and to [22, Lemma 10.1]. Assume for contradiction that there exists some v ∈ V with µ(ΓG(v)) < θ−θ1δµ(W), and set G′ = (µ, V \ {v}, W, E′) with E′ = E(V \ {v}, W). We claim that µ(θ)(G′) > µ(θ)(G). Equivalently, we need to show that

![image 283](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile283.png>)

![image 284](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile284.png>)

µ(E′) µ(E)

![image 285](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile285.png>)

θ

>

µ(V \ {v}) µ(V)

![image 286](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile286.png>)

θ−1

.

Note that µ(E′) > δµ(V)µ(W) − θ−θ1δµ(v)µ(W), because we have assumed that µ(ΓG(v)) <

![image 287](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile287.png>)

θ−1

![image 288](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile288.png>)

θ δµ(W) and because µ(v) > 0 (see part (a) of Deﬁnition 5.2). Hence, µ(E′)/µ(E) > 1 −

θ−1

![image 289](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile289.png>)

θ µ(v)/µ(V). Here θ−θ1 > 1, and thus (µ(E′)/µ(E))

![image 290](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile290.png>)

θ

![image 291](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile291.png>)

θ−1 > 1 − µ(v)/µ(V) = µ(V \ {v})/µ(V). This proves that µ(θ)(G′) > µ(θ)(G), in contradiction to the θ-maximality of G. We must thus have µ(ΓG(v)) θ−θ1δµ(W), as needed.

![image 292](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile292.png>)

Similarly, we may disprove the existence of w ∈ W with µ(ΓG(w)) < θ−θ1δµ(V). This completes the proof of the lemma.

![image 293](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile293.png>)

Next, we have the following important technical lemma, which is based on some ideas in [21] – see relations (7.4) and (7.5) there and the discussion around them.

- Lemma 5.10 (Subgraph where all vertices have a common neighbor, I). Let θ > 2, let G =


(µ, V, W, E) be a θ-maximal, non-trivial weighted bipartite graph, and let w0 ∈ W. There exists a subgraph G′ = (µ, V′, W′, E′) of G such that:

(a) (v, w0) ∈ E′ for all v ∈ V′; (b) for all w ∈ W′, there exists v ∈ V′ such that (v, w) ∈ E′; (c) µ(θ)(G) (1 − 1/θ)−θµ(θ−1)(G′).

Proof. Let δ := δ(G). Since G is non-trivial, we must have δ > 0. Moreover, since G is maximal,

- Lemma 5.9 implies that it is (θ−θ1 · δ)-connected. Let G1 = (µ, V1, W1, E1) with V1 = ΓG(w0), W1 = W, and E1 = E(V1, W1). We have that


![image 294](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile294.png>)

µ(E1) =

µ(v) · (1 − 1/θ)δ · µ(W)

µ(v)µ(ΓG(v))

v∈ΓG(w0)

v∈ΓG(w0)

= (1 − 1/θ)δ · µ(V1)µ(W1),

where we used that G is (θ−θ1 · δ)-connected. In particular, we have δ1 := δ(G1) (1 − 1/θ)δ. In addition, since µ(V1) = µ(ΓG(w0)) (1 − 1/θ)δ · µ(V) and W1 = W, we also ﬁnd that

![image 295](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile295.png>)

δθµ(V)µ(W) (1 − 1/θ)−1δθ−1µ(V1)µ(W1) (1 − 1/θ)−θδ1θ−1µ(V1)µ(W1).

We have thus proven that µ(θ)(G) (1 − 1/θ)−θµ(θ−1)(G1). To complete the proof, let G′ = (µ, V′, W′, E′) be a (θ − 1)-maximal subgraph of G1. We then have that

µ(θ)(G) (1 − 1/θ)−θµ(θ−1)(G1) (1 − 1/θ)−θµ(θ−1)(G′).

In addition, Lemma 5.9 implies that µ(ΓG′(w)) > 0 for all w ∈ W′; in particular, ΓG′(w) = ∅. Lastly, we have that (v, w0) ∈ E′ for all v ∈ V′ because G′ is a subgraph of G1. This completes the proof.

The symmetric version of Lemma 5.10 obviously also holds:

- Lemma 5.11 (Subgraph where all vertices have a common neighbor, II). Let θ > 2, let G =

(µ, V, W, E) be a θ-maximal, non-trivial weighted bipartite graph, and let v0 ∈ V. There exists a subgraph G′ = (µ, V′, W′, E′) of G such that:

- (a) (v0, w) ∈ E′ for all w ∈ W′;
- (b) for all v ∈ V′, there exists w ∈ W′ such that (v, w) ∈ E′;
- (c) µ(θ)(G) (1 − 1/θ)−θµ(θ−1)(G′).


- Lemma 5.12 (Few edges between small sets). Let G = (µ, V, W, E) be a θ-maximal weighted bipartite graph with edge density δ > 0, and let η ∈ (0, 1]. Then, for all sets A ⊆ V and B ⊆ W such that µ(A) η · µ(V) and µ(B) η · µ(W), we have µ(E(A, B)) η2−2/θ · µ(E).


Proof. The lemma follows by a simple modiﬁcation of the proof of [21, Lemma 11.5]: let η ∈ [0, 1], let A and B be as in the statement of the lemma, and let G′ be the subgraph of G induced by A and B. Then µ(θ)(G′) µ(θ)(G) by the maximality of G. On the other hand, (5.2) implies that µ(θ)(G′)/µ(θ)(G) (µ(E(A, B))/µ(E))θη2−2θ. Comparing the two inequalities completes the proof.

6. REDUCTION OF PROPOSITION 2.15 TO THE CASE OF RATIONAL SETS

In this section, we use the results of Section 5 to reduce Proposition 2.15 to the case of rational sets satisfying the following notion of primitivity:

- Deﬁnition 6.1 (Set of primitive numerators). Let R ⊂ Q>0. We say that R is a set of primitive numerators if, for each q ∈ N, the set {a ∈ N : a/q ∈ R, gcd(a, q) = 1} is primitive.


With this deﬁnition, we have the following special case of Proposition 2.15:

- Proposition 6.2. Let x 3 and y, z 1, let R, S ⊂ {α ∈ Q 1 : H(α) x} be two sets of primitive numerators, let λ : R>0 → R>0 be the weight function deﬁned by λ(α) = 1/α, and let


E ⊆ (̺, σ) ∈ R × S : y < [̺, σ] 2y, L(̺/σ; z) > 1 . Consider the weighted bipartite graph G = (λ, R, S, E). Then its 3-weight λ(3)(G) satisﬁes λ(3)(G) ≪ (y log x)2e−4z.

Deduction of Proposition 2.15 from Proposition 6.2. Let x 3 and y, z 1, and let B ⊂ [1, x] be 1-spaced and such that α/β ∈/ N for all distinct α, β ∈ B. In addition, set

E = (α, β) ∈ B × B : H(α/β) x3, y < [α, β] 2y, L(α/β; z) > 1

and consider the weighted bipartite graph G = (λ, B, B, E). Let us denote its density by δ. We may assume that δ > 0; otherwise Proposition 2.15 holds trivially.

We claim that it sufﬁces to prove that

λ(E)4 λ(B)6 ≪ (y log x)2e−4z.

- (6.1) λ(4)(G) =


![image 296](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile296.png>)

Indeed, we have λ(B) ≪ log x because B is 1-spaced. Hence, (6.1) would imply that

λ(E)4 ≪ y2(log x)8e−4z, whence Proposition 2.15 follows.

To prove (6.1), let G1 = (λ, V1, W1, E1) be a 4-maximal subgraph of G, and let

γ = min(V1 ∪ W1). Let us assume that γ ∈ W1; the case when γ ∈ V1 is treated very similarly. We then apply

- Lemma 5.10 with θ = 4, w0 = γ and GLemma 5.10 = G1. Hence, there exists a subgraph G2 = (λ, V2, W2, E2) of G1 (and hence of G) such that:


- (a) (v, γ) ∈ E2 for all v ∈ V2;
- (b) for all w ∈ W2, there exists v ∈ E2 such that (v, w) ∈ E2;
- (c) λ(4)(G1) ≪ λ(3)(G2).


- Since G1 is a 4-maximal subgraph of G, we ﬁnd that λ(4)(G) λ(4)(G1) ≪ λ(3)(G2). This reduces (6.1) to showing that


- (6.2) λ(3)(G2) ≪ (y log x)2e−4z. To prove this estimate, we shall use Proposition 6.2.


For each v ∈ V2 ⊆ V1, we know that (v, γ) ∈ E, and thus H(v/γ) x3. Hence, we may write v = ̺γ with H(̺) x3. By the minimality of γ, we have that ̺ 1. In addition, for each w ∈ W2, we know that there exists v ∈ V2 such that (v, w) ∈ E2 ⊆ E. Hence, H(v/w) x3. But we then ﬁnd that H(w/γ) H(w/v) · H(v/γ) x6. Hence, we may write w = γσ with H(σ) x6 and σ 1 (where we used the minimality of γ once again).

By the above discussion, there exist sets R, S ⊂ {α ∈ Q 1 : H(α) x6} such that V2 = γR = {γ̺ : ̺ ∈ R} and W2 = γS. In particular,

λ(R) γ

λ(S) γ

λ(V2) =

and λ(W2) =

.

![image 297](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile297.png>)

![image 298](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile298.png>)

Moreover, let E∗ = {(̺, σ) ∈ R × S : (γ̺, γσ) ∈ E2}, let G∗ = (λ, R, S, E∗), and let δ∗ be the density of G∗. We then have that

λ(E∗) γ2

λ(E2) =

and δ∗ = δ(G2). We thus ﬁnd that

![image 299](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile299.png>)

λ(3)(G∗) γ2

- (6.3) λ(3)(G2) =


.

![image 300](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile300.png>)

Next, we show that we may apply Proposition 6.2 to G∗.

Indeed, our assumption that α/β ∈/ N for all distinct α, β ∈ B implies that both R and S are sets of primitive numerators. In addition, we may check that [γ̺, γσ] = [̺, σ]/γ, and thus γy < [̺, σ] 2γy for every (̺, σ) ∈ E∗. Lastly, we obviously have that L(γσγ̺; z) = L(̺/σ; z). We may thus apply Proposition 6.2 with parameters yProposition 6.2 = γy and xProposition 6.2 = x6 to prove that λ(3)(G∗) ≪ (γy log x)2e−4z. Together with (6.3), this completes the proof of (6.2). We have thus established Proposition 2.15.

![image 301](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile301.png>)

7. GCD GRAPHS

In this section, we extend the theory of GCD graphs developed in [21, 22] to include the possibility of having vertices in Q. We will then state all the necessary results concerning these graphs in order to establish Proposition 6.2.

- 7.1. Deﬁnitions. We start with a series of deﬁnitions most of which are a simple adaptation of [21, Section 6] and [22, Section 8]. The only important differences lie in Deﬁnitions 7.9 and 7.10 that incorporate ideas from [16, 19].


- Deﬁnition 7.1 (p-adic valuation). Given a prime p, an integer k, and a rational number ̺ > 0, we write pk ̺ or, equivalently, ep(̺) = k, if we may write ̺ = pka/q with p ∤ aq.
- Deﬁnition 7.2 (Positive and negative parts of a function). Given a real-valued function f, we let f+ = max{f, 0} and f− = max{−f, 0}.
- Deﬁnition 7.3 (GCD graph). Let G be a septuple (µ, V, W, E, P, f, g) such that:

- (a) (µ, V, W, E) forms a weighted bipartite graph with V, W ⊂ Q>0;
- (b) P is a set of primes;
- (c) f and g are functions from P to Z such that for all p ∈ P and all (a/q, b/r) ∈ V × W with gcd(a, q) = gcd(b, r) = 1 we have:


- (i) pf+(p)|a and pg+(p)|b;
- (ii) pf−(p)|q and pg−(p)|r;
- (iii) if (a/q, b/r) ∈ E, then pmin{f+(p),g+(p)} gcd(a, b) and pmin{f−(p),g−(p)} gcd(q, r).


We then call G a GCD graph with multiplicative data (P, f, g). We will also refer to P as the set of primes of G. If P = ∅, we say that G has trivial set of primes and we view f = f∅ and g = g∅ as two copies of the empty function from ∅ to Z.

Lastly, we will say that G is non-trivial if the corresponding weighted bipartite graph from (a) is non-trivial, that is to say, if E = ∅, which is equivalent to having µ(E) > 0.

- Deﬁnition 7.4 (exact GCD graph). Given a GCD graph G = (µ, V, W, E, P, f, g), we deﬁne the following notions:


- (a) G is exact if pf(p) v and pg(p) w for all (v, w) ∈ V × W and p ∈ P;
- (b) G is numerator-exact if pf+(p) a and pg+(p) b for all p ∈ P and all (a/q, b/r) ∈ V × W in part (c)-(i) of Deﬁnition 7.3;
- (c) G is denominator-exact if pf−(p) q and pg−(p) r for all p ∈ P and all (a/q, b/r) ∈ V × W in part (c)-(ii) of Deﬁnition 7.3.


To each GCD graph G, and for each real number θ 1, we associate a θ-quality q(θ)(G). This will be deﬁned similarly to [22], but we omit the factors (1 − f(p)=g(p) =0/p)−2 from it since this will allow us to state more precise results. We also omit the factors (1 − 1/p

θ+2

4 )−3 that were inserted for mere convenience.

![image 302](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile302.png>)

- Deﬁnition 7.5 (quality). Let θ 1 and let G = (µ, V, W, E, P, f, g) be a GCD graph. The θ-quality of G is deﬁned by

q(θ)(G) := µ(θ)(G)

p∈P

p|f(p)−g(p)| = δ(G)θµ(V)µ(W)

p∈P

p|f(p)−g(p)|.

- Deﬁnition 7.6 (GCD subgraph). Consider two GCD graphs G = (µ, V, W, E, P, f, g) and G′ = (µ′, V′, W′, E′, P′, f′, g′).

- (a) We say that G′ is a GCD subgraph of G if µ′ = µ, V′ ⊆ V, W′ ⊆ W, E′ ⊆ E, P′ ⊇ P, f′ P = f, g′ P = g.
- (b) We say that G′ is a non-trivial GCD subgraph of G if µ(E′) > 0.
- (c) We say that G′ is an exact GCD subgraph of G if for every p ∈ P′ \ P and every (v, w) ∈ V × W, we have pf′(p) v and pg′(p) w. Similarly, we deﬁne the notions of numerator-exact and denominator-exact GCD subgraphs of G.


Remark. Note that an exact GCD subgraph G′ of a graph G is not necessarily exact as a graph, since the deﬁnition only addresses the p-adic valuation of the vertices of G′ with respect to the “new” primes p in P′ \P. On the other hand, if we know that G is an exact graph, then every exact GCD subgraph of it is an exact GCD graph itself.

Similar remarks hold for the notion of numerator-exact GCD subgraphs and denominator-exact GCD subgraphs.

We have the following important special vertex sets and GCD graphs Gpk,pℓ that are formed by restricting to elements with a given p-adic valuation. Note that each Gpk,pℓ is an example of an exact GCD subgraph of G.

- Deﬁnition 7.7. Let p be a prime number, and let k, ℓ ∈ Z.

- (a) If V ⊂ Q>0, we set Vpk = {v ∈ V : pk v}.
- (b) Let G = (V, W, E) be a bipartite graph. We write for brevity Epk,pℓ := E(Vpk, Wpℓ).
- (c) Let G = (µ, V, W, E, P, f, g) be a GCD graph such that p ∈/ P. We then deﬁne the septuple Gpk,pℓ = (µ, Vpk, Wpℓ, Epk,pℓ, P ∪ {p}, fpk, gpℓ)


where the functions fpk, gpℓ are deﬁned on P ∪ {p} by the relations fpk|P = f, gpℓ|P = g, fpk(p) = k and gpℓ(p) = ℓ.

- Deﬁnition 7.8. Let G = (µ, V, W, E, P, f, g) be a GCD graph. We let R(G) be given by R(G) := p ∈/ P : ∃ aq, rb ∈ E with gcd(a, q) = gcd(b, r) = 1 and p| gcd(a, b) gcd(q, r) .


![image 303](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile303.png>)

![image 304](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile304.png>)

Vpkp+1

Wpkp+1

Vpkp

Wpkp

Vpkp−1

Wpkp−1

FIGURE 1. Edges in a structured GCD graph.

That is to say R(G) is the set of primes occurring in a GCD which we haven’t yet accounted for. Given two parameters θ > 2 and M 2, we let C = 1013M/(θ − 2)3 and we split R(G) into two subsets:

- • The set R♯θ,M(G) of all primes p ∈ R(G) satisfying both of the following properties:

- – there exists k ∈ Z such that

µ(Vpk) µ(V)

![image 305](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile305.png>)

1 −

C p

![image 306](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile306.png>)

and

µ(Wpk) µ(W)

![image 307](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile307.png>)

1 −

C p

![image 308](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile308.png>)

;

- – q(Gpi,pj) < M · q(G) for all (i, j) ∈ Z2 with i = j.


- • The set R♭θ,M(G) := R(G) \ R♯θ,M(G).


- Deﬁnition 7.9 (Structured GCD graph).


- (a) Let G be a GCD graph with edge set E. We shall say that G is a structured GCD graph if, for each p ∈ R(G), there exists an integer kp such that

- (7.1) ep(v) − kp, ep(w) − kp ∈ (−1, 0), (0, −1), (0, 0), (0, 1), (1, 0) for all (v, w) ∈ E.


- (b) Let G and G′ be two GCD graphs. We shall say that G′ is a structured GCD subgraph of G if G′ is structured, and it is also a GCD subgraph of G.


- Remark 7.1. (a) The choice of kp might not be unique. For instance, if (ep(v), ep(w)) = (2, 1) for all (v, w) ∈ E, then (7.1) holds for any choice of kp ∈ {1, 2}.


- (b) Every GCD subgraph of a structured GCD graph is itself a structured GCD graph.


- (c) Let G, E and kp be as in Deﬁnition 7.9(a). Then we must have kp = 0. Indeed, by the


deﬁnition of R(G), there must exist some edge (a/q, b/r) ∈ E with gcd(a, q) = gcd(b, r) = 1 and p| gcd(a, b) gcd(q, r). However, note that (7.1) implies that p ∤ gcd(a, b) gcd(q, r) when kp = 0, which is a contradiction. This proves our claim that kp = 0. In particular, for a structured GCD graph G, each prime p ∈ R(G) has one of the following properties: either

- (7.2) ep(v) 0 and ep(w) 0 for all (v, w) ∈ E, or


- (7.3) ep(v) 0 and ep(w) 0 for all (v, w) ∈ E.

In addition, these properties are mutually exclusive, because we cannot have ep(v) = ep(w) = 0 if (v, w) ∈ E and p ∈ R(G).

Deﬁnition 7.10. Let G = (µ, V, W, E, P, f, g) be a structured GCD graph. We then deﬁne the sets R+(G) := {p ∈ R(G) : (7.2) holds} and R−(G) := {p ∈ R(G) : (7.3) holds}.

Remark 7.2. Let G be a structured GCD graph, p ∈ R(G) and kp be as in Deﬁnition 7.9(a). In view of Remark 7.1(c), we have

R+(G) = {p ∈ R(G) : kp > 0} and R−(G) = {p ∈ R(G) : kp < 0}, as well as

R(G) = R+(G) ⊔ R−(G). The reason we deﬁne the sets R+(G) and R−(G) in terms of conditions (7.2) and (7.3) is so that they do not depend on the choice of kp, which might not be unique (cf. Remark 7.1(a)).

- 7.2. Results on GCD graphs. Next, we state ﬁve key propositions that guarantee the existence of GCD subgraphs with nice properties. We will see in the next section how to deduce Proposition


6.2 (and hence Theorem 1) from them. In their statement, and for the remainder of the paper, we implicitly ﬁx a choice of parameters θ ∈ (2, 2.01) and M 2 (in the proof of Proposition 6.2, we shall take θ = 2.001 and M = e4), and we set for simplicity

µ(G) = µ(θ)(G) and q(G) = q(θ)(G), as well as

R♯(G) = R♯θ,M(G) and R♭(G) = R♭θ,M(G). Moreover, we shall say that G is maximal to mean that it is θ-maximal as a weighted bipartite graph.

In addition, it will be convenient to set τ := θ − 2 ∈ (0, 1/100)

and to introduce the quantities C1, . . ., C8 as follows: C1 = 104/τ, C2 = 10MC13, C3 = 103C13, C4 = 1010M2C22, C5 = max C3, (50 logC4)3 , C6 = max C4, 104MC2, C210/τ , C7 = CC

6

5 , C8 = 100MC2.

- (7.4)


Note that the constant C in Deﬁnition 7.8 equals C2.

With the abovenotational conventions, we are ready to state our ﬁve key propositionsabout GCD graphs. The ﬁrst two are simple modiﬁcations of Propositions 8.3 and 8.1 in [22], respectively. Similarly, the last two propositions will follow by adapting the proof of Proposition 8.2 in [22].

On the other hand, there is no version of Proposition 7.13 in [21, 22]. It should be noted though that the ideas leading to it are all contained in the proofs of Proposition 8.2 and Lemmas 8.4 and

- 8.5 in [22].


- Proposition 7.11 (Bounded quality loss for small primes). Let G be a non-trivial GCD graph with set of primes P. Then there is a non-trivial and exact GCD subgraph G′ of G with set of primes P′ such that


P′ ⊆ P ∪ R(G) ∩ {p C6} , R(G′) ⊆ {p > C6}, q(G′) q(G)/C7.

- Proposition 7.12 (Iteration when R♭(G) = ∅). Let G be a non-trivial GCD graph with set of primes P such that

R(G) ⊆ {p > C6} and R♭(G) = ∅. Then there is an exact GCD subgraph G′ of G with multiplicative data (P′, f′, g′) such that:

- (a) G′ is non-trivial and maximal as a weighted bipartite graph;
- (b) P P′ ⊆ P ∪ R(G);
- (c) R(G′) R(G);
- (d) q(G′) MUq(G) with U = #{p ∈ P′ \ P : f′(p) = g′(p)}.


- Proposition 7.13 (Structure when R♭(G) = ∅). Let G be a non-trivial and maximal GCD graph such that

R(G) ⊆ {p > C6} and R♭(G) = ∅.

In addition, for each prime p, let ap,1, . . ., ap,n be n non-negative weights. Then there is a structured GCD subgraph G′ of G with edge set E′ such that:

- (a) G′ is non-trivial and maximal as a weighted bipartite graph;
- (b) p∈v/w, p∈R(G) ap,i C8n p∈R(G) ap,ip for all i ∈ {1, . . ., n} and all (v, w) ∈ E′;

![image 309](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile309.png>)

- (c) q(G′) q(G)/2.


- Proposition 7.14 (Iteration when G is structured and R−(G) = ∅). Let G be a non-trivial and structured GCD graph with set of primes P such that

R(G) ⊆ {p > C6} and R−(G) = ∅. Then there is a numerator-exact GCD subgraph G′ of G with multiplicative data (P′, f′, g′) such that:

- (a) G′ is non-trivial and maximal as a weighted bipartite graph;
- (b) P P′ ⊆ P ∪ R−(G), R−(G′) R−(G), R+(G′) ⊆ R+(G);
- (c) f′(p) 0 and g′(p) 0 for all p ∈ P′ \ P;
- (d) q(G′) q(G) p∈P′\P(1 − f′(p)=g′(p)<0/p)2(1 − 1/p1+


τ

![image 310](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile310.png>)

4).

Finally, even though we do not need it in this paper, we also have the following iteration proposition that we state because it might be useful in future work.

- Proposition 7.15 (Iteration when G is structured and R+(G) = ∅). Let G be a non-trivial and structured GCD graph with multiplicative data (P′, f′, g′) such that


R(G) ⊆ {p > C6} and R+(G) = ∅.

Then there is a denominator-exact GCD subgraph G′ of G with set of primes P′ such that:

- (a) G′ is non-trivial and maximal as a weighted bipartite graph;
- (b) P P′ ⊆ P ∪ R+(G), R+(G′) R+(G), R−(G′) ⊆ R−(G);
- (c) f′(p) 0 and g′(p) 0 for all p ∈ P′ \ P;
- (d) q(G′) q(G) p∈P′\P(1 − f′(p)=g′(p)>0/p)2(1 − 1/p1+


τ

4).

![image 311](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile311.png>)

8. PROOF OF PROPOSITION 6.2 ASSUMING THE RESULTS OF SECTION 7

Here, we show how to deduce Proposition 6.2 from Propositions 7.11-7.14. Throughout, we take τ = 0.001, θ = 2 + τ = 2.001, and M = e4, and we adopt all notational conventions of Section 7.2. For instance, we will write λ(G) and q(G) instead of λ(2.001)(G) and q(2.001)(G), and we will say that G is maximal if it is 2.001-maximal as a weighted bipartite graph.

Let G = (λ, R, S, E) with R, S and E as in the statement of Proposition 6.2. With a slight abuse

of notation, we view G as the GCD graph (λ, R, S, E, ∅, f∅, g∅) with trivial multiplicative data. We then have that

λ(3)(G) λ(2.001)(G) = q(2.001)(G) = q(G) by relation (5.1) and by Deﬁnition 7.5. Hence, it sufﬁces to show that

- (8.1) q(G) ≪ (y log x)2e−4z.


We may assume that G is non-trivial; otherwise q(G) = 0, and thus (8.1) holds trivially.

It is now time to employ the results of Section 7. We ﬁrst use Proposition 7.11, and we then iterate Proposition 7.12 till we arrive at a GCD subgraph G1 = (λ, V1, W1, E1, P1, f1, g1) of G such that:

- (a) G1 is maximal as a weighted bipartite graph;
- (b) G1 is exact as a GCD graph;
- (c) R♭(G1) = ∅;
- (d) q(G1) ≫ e4Uq(G) with U = #{p ∈ P1 : p > C6, f1(p) = g1(p)}.


Next, we apply Proposition 7.13 with GProposition 7.13 = G1, with n = 1, and with ap,1 = p>z/p. Hence, we may locate a GCD subgraph G2 = (λ, V2, W2, E2, P2, f2, g2) of G1 with the same multiplicative data (P2, f2, g2) = (P1, f1, g1) and such that:

- (a) G2 is maximal as weighted bipartite graph;
- (b) G2 is exact and structured as a GCD graph;
- (c) p∈v/w, p∈R(G

1), p>z

1

![image 312](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile312.png>)

p C8 p>z p1

![image 313](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile313.png>)

2 ≪ 1z for all (v, w) ∈ E2;

![image 314](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile314.png>)

- (d) q(G2) q(G1)/2.


- Since G2 is structured, all of its subgraphs are also structured. Thus, we may iterate Proposition


- 7.14 till we arrive at a GCD subgraph G3 = (λ, V3, W3, E3, P3, f3, g3) of G2 such that:


- (a) G3 is maximal as a weighted bipartite graph;
- (b) G3 is structured and numerator-exact as a GCD graph;
- (c) R−(G3) = ∅;


3\P2(1 − f3(p)=g3(p)<0/p)2(1 − 1/p1+1/4000).

- (d) q(G3) q(G2) p∈P


In particular, since G3 is a structured GCD graph, for each p ∈ R(G3) there exists an integer kp ∈ Z such that

- (8.2) ep(v) − kp, ep(w) − kp ∈ (−1, 0), (0, −1), (0, 0), (0, 1), (1, 0) for all (v, w) ∈ E3.


In addition, kp > 0 by Remark 7.2 and the fact that R−(G3) = ∅. Let us deﬁne the integers

d± =

p∈P2

±

3 (p), e± =

pf

p∈P2

±

3 (p), j± = gcd(d±, e±),

pg

and

and

D± =

p∈P3\P2

±

3 (p), E± =

pf

p∈P3\P2

±

3 (p), J± = gcd(D±, E±),

pg

N =

pk

p∈R(G3)

, N∗ =

p

p.

p|N

The integer N has no prime factor in P3 by the deﬁnition of R(G3). Moreover, we have D+ = E+ = J+ = 1

because f3+(p) = g3+(p) = 0 for all p ∈ P3 \ P2 by property (c) of Proposition 7.14. In addition, note that

- (8.3)

p∈P3

p|f

3(p)−g3(p)| =

d+D+e+E+d−D−e−E− (j+J+j−J−)2

![image 315](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile315.png>)

=

d+e+d−D−e−E− (j+j−J−)2

![image 316](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile316.png>)

,

because |χ − ψ| = |χ+ − ψ+| + |χ− − ψ−| and |χ± − ψ±| = χ± + ψ± − 2 min{χ±, ψ±} for all χ, ψ ∈ R.

Given (v, w) ∈ V3 × W3, let A± = A±(v) =

p|N ep(v)=kp±1

p and B± = B±(w) =

p|N ep(w)=kp±1

p.

Note that if (v, w) ∈ E3, then (8.2) implies that the integers A+, A−, B+, B− are mutually coprime and that

- (8.4) ep(v) = ep(NA+/A−) and ep(w) = ep(NB+/B−) for all p ∈ R(G3).

In particular, ep(v), ep(w) kp − 1 0 for all p ∈ R(G3).

Now, given (v, w) ∈ E3, let us write v = a/q and w = b/r with gcd(a, q) = gcd(b, r) = 1. We then ﬁnd that

- (8.5) a = d+

NA+ A− · a′, b = e+

![image 317](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile317.png>)

NB+ B− · b′, q = d−D− · q′, r = e−E− · r′ for some integers a′, b′, r′, q′ such that gcd(a′, q′) = gcd(b′, r′) = 1. In addition, observe that

![image 318](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile318.png>)

- (8.6) p|a′q′b′r′ =⇒ p ∈/ R(G3),


- by (8.4) and the comment following it. Moreover, since all elements of V3 ⊆ R and W3 ⊆ S are rational numbers 1 of height x, we have that q a x and r b x. Together with (8.5), this implies
- (8.7)

NA+ A− · a′ x,

![image 319](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile319.png>)

NB+

![image 320](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile320.png>)

B− · b′ x and J− x. Furthermore, we have that:

- (a) A−A+B−B+|N∗ because A−, A+, B− and B+ are mutually coprime and square-free;
- (b) gcd(a′q′, N) = gcd(b′r′, N) = 1 by (8.6);
- (c) gcd(a′, d−D−) = gcd(b′, e−E−) = 1 because gcd(a, q) = gcd(b, r) = 1;
- (d) gcd(a′, d+) = gcd(b′, e+) = 1 because G2 is exact;
- (e) gcd(a, b) = j+N/(A−B−) and gcd(q, r) = j−J− because:


- • the deﬁnition of R(G3) implies that gcd(a, b) and gcd(q, r) are solely composed of primes in P3 ⊔ R(G3);
- • if p ∈ R(G3), then ep(v) = ep(NA+/A−) and ep(w) = ep(NB+/B−) by (8.4);
- • gcd(NA+/A−, NB+/B−) = N/(A−B−) by condition (a) above;
- • if p ∈ P3, then pmin{f

+

3 (p),g3+(p)} gcd(a, b) and pmin{f

−

3 (p),g3−(p)} gcd(q, r) by condition (c)-(iii) in Deﬁnition 7.3;

- • if p ∈ P3, then min{f3±(p), g3±(p)} = ep(j±J±) by the deﬁnition of j± and of J±;
- • J+ = 1.


Using property (e), equation (8.5) and Lemma 2.5, we ﬁnd that [v, w] =

qr gcd(a, b) gcd(q, r)

![image 321](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile321.png>)

=

d−D−e−E− j+j−J−N · q′A− · r′B−

![image 322](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile322.png>)

whenever (v, w) ∈ E3. But we also know that [v, w] ≍ y for all (v, w) ∈ E3 ⊆ E. Hence, we conclude that

- (8.8) q′A− · r′B− ≍ y ·

j+j−J−N d−D−e−E−

![image 323](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile323.png>)

for all (v, w) ∈ E3. Now, let h denote the multiplicative function

h(n) =

p|n p>z

e4z/p,

and let us note that

- (8.9)

p

|h(p) − 1| p

![image 324](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile324.png>)

= O(1)

because 1 h(p) e

p>z·4z/p 1 + p>z · e4z/p. We claim that

- (8.10) e4z ≪ e4Uh(A+)h(A−)h(B+)h(B−)h(a′)h(q′)h(b′)h(r′) for all (v, w) ∈ E3.

If z C6, this is clearly true because h 1. So assume that z > C6. We claim that it sufﬁces to show that

- (8.11)


1 p

1 p

U z

1 z

for all (v, w) ∈ E3.

+

+ O

![image 325](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile325.png>)

![image 326](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile326.png>)

![image 327](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile327.png>)

![image 328](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile328.png>)

n∈{A+,A−,B+,B−,a′,q′,b′,r′} p|n p>z

p∈v/w p>z

Indeed, we know that p∈v/w, p>z 1p = L(v/w; z) > 1 for all (v, w) ∈ E2 ⊆ E. Hence, if (8.11) is true, we may then multiply both sides by 4z and exponentiate them to deduce (8.10).

![image 329](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile329.png>)

Let us now prove (8.11). If p ∈ v/w and p > z > C6, we have the following four possibilities:

- • p ∈ P1 = P2. Since G1 is exact, we ﬁnd that f1(p) = g1(p). This implies that

p∈v/w, p∈P2, p>z

1 p

![image 330](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile330.png>)

U z

![image 331](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile331.png>)

.

- • p ∈ P3 \ P2. We then have p ∈ R(G2) ⊆ R(G1), and thus property (c) of G2 implies that

p∈v/w, p∈P3\P2, p>z

1 p ≪

![image 332](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile332.png>)

1 z

![image 333](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile333.png>)

.

- • p ∈ R(G3). Using (8.4), we ﬁnd that p ∈ NA

+/A−

![image 334](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile334.png>)

NB+/B− = AA+B−

![image 335](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile335.png>)

−B+, and thus that p|A+A−B+B−.

- • p ∈/ P3 ∪ R(G3). Using (8.5), we must then have that p|a′q′b′r′.


Putting together the above observations proves (8.11), and thus (8.10). Let us now pick an edge (v0, w0) = (a

q0, b

r0) ∈ E3 (it doesn’t matter which one) and let us set

0

0

![image 336](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile336.png>)

![image 337](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile337.png>)

- (8.12) X := q0′A−0 and Y := r0′B0−, where A−0 := A−(v0) and B0− := B−(w0). By (8.8), we have that
- (8.13) XY ≍ y ·

j+j−J−N d−D−e−E−

![image 338](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile338.png>)

.

We then apply Lemma 5.10 with GLemma 5.10 = (λ, V3, W3, E3), w0 as above, and θ = 2.001. This proves that there exists a GCD subgraph G4 = (λ, V4, W4, E4, P3, f3, g3) of G3 such that:

- (a) (v, w0) ∈ E4 for all v ∈ V4;
- (b) for all w ∈ W4, there exists v ∈ V4 such that (v, w) ∈ E4;
- (c) λ(G3) ≪ λ(1.001)(G4).


In particular, condition (a) and relations (8.8), (8.12) and (8.13) imply that

- (8.14) q′A− ≍

y r0′ B0− ·

![image 339](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile339.png>)

j+j−J−N d−D−e−E− ≍ X for all v ∈ V4.

![image 340](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile340.png>)

In addition, for every w ∈ W4, condition (b) implies that the existence of some v ∈ V4 such that (v, w) ∈ E4 ⊆ E3. Together with (8.8), (8.14) and (8.13), this implies that

- (8.15) r′B− ≍


j+j−J−N d−D−e−E− ≍ Y for all w ∈ W4. We proceed to bound q(G) in terms of λ(E4). By the properties of G1 and G2, we have

j+j−J−N d−D−e−E− ≍

y X ·

y q′A− ·

![image 341](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile341.png>)

![image 342](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile342.png>)

![image 343](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile343.png>)

![image 344](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile344.png>)

q(G) ≪ e−4Uq(G1) ≪ e−4Uq(G2). Next, note that if f3(p) = g3(p) < 0 and p ∈ P3 \ P2, then we must have p|J−. Moreover, we know that p(1 − 1/p1+1/4000) ≫ 1. Consequently, the properties of G3 and the deﬁnition of the quality q(·), imply that

−2

−2

1 p

1 p

p|f

3(p)−g3(p)|

= e−4Uλ(G3)

q(G) ≪ e−4Uq(G3)

1 −

1 −

.

![image 345](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile345.png>)

![image 346](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile346.png>)

p∈P3

p|J−

p|J−

Lastly, note that λ(G3) ≪ λ(1.001)(G4) λ(E4) by the properties of G4 and (5.1). Together with (8.3), this yields the estimate

- (8.16) q(G) ≪ e−4Uλ(E4) ·

d+e+d−D−e−E− (j+j−J−)2 ·

![image 347](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile347.png>)

p|J−

1 −

1 p

![image 348](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile348.png>)

−2

.

Now, consider the modiﬁed weight function µ(v) := λ(v)h(A+)h(A−)h(a′)h(q′).

In virtue of (8.10), we have that e4zλ(v)λ(w) ≪ e4Uµ(v)µ(w) for all (v, w) ∈ E3 ⊆ E4, and thus e−4Uλ(E4) ≪ e−4zµ(E4). Together with (8.16), this reduces the proof of (8.1), and thus of Proposition 6.2, to showing that

- (8.17) µ(E4) ≪ (y log x)2 ·


(j+j−J−)2 d+e+d−D−e−E− ·

![image 349](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile349.png>)

p|J−

1 p

1 −

![image 350](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile350.png>)

2

.

To prove (8.17), note that if (v, w) ∈ E4 ⊆ E3, then (8.5) and (8.14) imply that µ(v) =

d−D− d+N ·

A− A+ ·

q′ a′ · h(A+)h(A−)h(a′)h(q′)

![image 351](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile351.png>)

![image 352](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile352.png>)

![image 353](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile353.png>)

d−D− d+N ·

X

A+a′ · h(A+)h(A−)h(a′)h(q′). Similarly, from (8.5) and (8.15) we deduce that

≍

![image 354](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile354.png>)

![image 355](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile355.png>)

e−E− e+N ·

Y

B+b′ · h(B+)h(B−)h(b′)h(r′). Therefore, for all (v, w) ∈ E4 we have

µ(w) ≍

![image 356](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile356.png>)

![image 357](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile357.png>)

h(A+)h(A−)h(a′)h(q′) A+a′ ·

h(B+)h(B−)h(b′)h(r′) B+b′

d−D−e−E− d+e+ ·

XY N2 ·

µ(v)µ(w) ≍

. Moreover, we have

![image 358](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile358.png>)

![image 359](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile359.png>)

![image 360](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile360.png>)

![image 361](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile361.png>)

(j+j−J−)2 d+d−D−e+e−E− ·

d−D−e−E− d+e+ ·

1 XY by (8.13). We thus conclude that

XY N2 ≍ y2 ·

![image 362](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile362.png>)

![image 363](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile363.png>)

![image 364](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile364.png>)

![image 365](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile365.png>)

(j+j−J−)2 d+d−D−e+e−E− ·

S2 Y

S1 X ·

µ(E4) ≪ y2 ·

, where

![image 366](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile366.png>)

![image 367](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile367.png>)

![image 368](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile368.png>)

h(A+)h(A−)h(a′)h(q′) A+a′

S1 :=

![image 369](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile369.png>)

A+,A−,a′,q′∈N A−A+|N∗, NAA−+ ·a′ x, A−q′≍X gcd(a′q′,N)=gcd(a′,J−)=1

![image 370](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile370.png>)

a′d+NA+/A−

q′d−D− ∈R

![image 371](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile371.png>)

and

h(B+)h(B−)h(b′)h(r′) B+b′

S2 :=

,

![image 372](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile372.png>)

B−,B+,b′,r′∈N B−B+|N∗, NBB−+ ·b′ x, B−r′≍X gcd(b′r′,N)=gcd(b′,J−)=1

![image 373](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile373.png>)

b′e+NB+/B−

r′e−E− ∈S

![image 374](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile374.png>)

where we used (8.7). We have thus reduced the proof of (8.17), and hence of Proposition 6.2, to showing that

- (8.18) S1 ≪ X · (log x)

p|J−

1 −

1 p

![image 375](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile375.png>)

and S2 ≪ Y · (log x)

p|J−

1 −

1 p

![image 376](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile376.png>)

.

We proceed to prove the bound for S1; the sum S2 is treated similarly.

We ﬁx A± and q′ and apply Corollary 4.2 to bound the sum over a′. Notice that we do not know whether N xO(1). Hence, we will only use that gcd(a′, NAA +

![image 377](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile377.png>)

−

J−) = 1 because we do know that NA+/A− and J− are both x by (8.7). Therefore, for each ﬁxed choice of A± and q′, Corollary 4.2 together with our assumption that R is a set of primitive numerators and the estimate (8.9) imply that

a′

h(a′) a′ ≪

![image 378](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile378.png>)

log x √log log x ·

![image 379](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile379.png>)

![image 380](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile380.png>)

p|NAA−+ J−

![image 381](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile381.png>)

1 −

1 p

![image 382](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile382.png>)

.

Consequently, since gcd(N, J−) = 1, we obtain

S1 ≪

log x √log log x · S1′ ·

![image 383](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile383.png>)

![image 384](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile384.png>)

p|J−

1 −

1 p

![image 385](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile385.png>)

,

where

S1′ :=

A−A+|N∗

NA+ A− x, A−q′≍X gcd(q′,NAA−+ )=1

![image 386](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile386.png>)

![image 387](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile387.png>)

h(A+)h(A−)h(q′) A+

![image 388](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile388.png>)

p|NAA−+

![image 389](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile389.png>)

1 −

1 p

![image 390](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile390.png>)

.

To establish (8.18) for S1, it remains to prove that

- (8.19) S1′ ≪ X · log log x. Consider the cut-off parameter

![image 391](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile391.png>)

Z := exp log log x and note that

![image 392](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile392.png>)

- (8.20)


−1

−1

1 p

1 p

log log x log Z

![image 393](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile393.png>)

1 −

1 −

≪

≍

= log log x,

![image 394](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile394.png>)

![image 395](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile395.png>)

![image 396](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile396.png>)

p|NAA−+ p>Z

Z<p logx

![image 397](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile397.png>)

because an integer x has ≪ log x prime factors.

Now, we split S1′ = S1′,1 + S1′,2, where S1′,1 is the subsum with q′ > Z and S1′,2 is the remaining sum. To bound S1′,1, let us ﬁx A±. Since q′ ≍ X/A−, we must have Z ≪ X/A− for this subsum of S1′,1 to be non-empty. Hence, if we use Lemma 3.2 with f(n) = h(n) · gcd(n,NA+/A−)=1 and xLemma 3.2 ≍ X/A−, we ﬁnd that

h(p) · p∤NA+/A− − 1 p

X A−

h(q′) ≪

.

exp

![image 398](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile398.png>)

![image 399](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile399.png>)

p X/A−

q′≍AX− gcd(q′,NAA−+ )=1

![image 400](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile400.png>)

![image 401](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile401.png>)

We have h(p) · p∤NA+/A− − 1 |h(p) − 1| − p|NA+/A−. Together with (8.9) and our assumption that Z ≪ X/A−, this implies that

X A−

1 p

X A−

1 p ≪

h(q′) ≪

1 −

exp −

.

![image 402](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile402.png>)

![image 403](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile403.png>)

![image 404](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile404.png>)

![image 405](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile405.png>)

p X/A− p|NA+/A−

p|NAA−+ p Z

q′≍AX− gcd(q′,NAA−+ )=1

![image 406](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile406.png>)

![image 407](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile407.png>)

![image 408](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile408.png>)

Combining this estimate with (8.20), we ﬁnd that

h(A+)h(A−) A+A−

![image 409](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile409.png>)

S1′,1 ≪ X log log x

![image 410](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile410.png>)

p|NAA−+

A−A+|N∗

![image 411](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile411.png>)

1 p

1 −

![image 412](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile412.png>)

2

![image 413](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile413.png>)

X log log x · H(N),

where H is the multiplicative function deﬁned by

h(m)h(n) mn

H(N) :=

![image 414](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile414.png>)

p|mnN

mn| p|N p

![image 415](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile415.png>)

1 p

1 −

![image 416](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile416.png>)

2

.

Since m and n run over square-free divisors of N, and we have 1 h(p) e4 for all primes p, we get

2(h(p) − 1) p

1 p2

H(pℓ) = 1 +

,

+ O

![image 417](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile417.png>)

![image 418](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile418.png>)

for all primes p and all integers ℓ 1. Therefore, it follows from (8.9) that H(N) ≪ 1 uniformly in N 1 and hence

- (8.21) S1′,1 ≪ X log log x, as needed.

![image 419](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile419.png>)

Lastly, let us bound S1′,2. Here, we ﬁx A+ and q′ Z, and sum over A− ﬁrst. Note that

p|NAA−+

![image 420](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile420.png>)

1 −

1 p

![image 421](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile421.png>)

p|N

1 −

1 p

![image 422](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile422.png>)

p|A−

1 −

1 p

![image 423](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile423.png>)

−1

.

In addition,

A−≍Xq′

![image 424](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile424.png>)

h(A−)

p|A−

1 −

1 p

![image 425](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile425.png>)

−1

≪

X q′

![image 426](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile426.png>)

by Lemma 3.2 applied with f(n) = h(n)n/ϕ(n) and by (8.9). Consequently,

S1′,2 ≪ X ·

ϕ(N) N q

![image 427](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile427.png>)

′ Z

h(q′) q′

![image 428](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile428.png>)

A+|N

h(A+) A+

![image 429](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile429.png>)

.

The sum over q′ is ≪ log Z = √log log x by Lemma 3.2 and the sum over A+ is ≪ N/ϕ(N) by (8.9). This proves that

![image 430](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile430.png>)

- (8.22) S1′,2 ≪ X · log log x,


![image 431](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile431.png>)

as needed.

Combining (8.21) and (8.22) completes the proof of (8.19), and thus of Proposition 6.2. This, in turn, completes the proof of Theorem 1 modulo proving the results of Section 7.

9. LEMMAS ON GCD GRAPHS AND DEDUCTION OF PROPOSITIONS 7.11 AND 7.12

- Lemma 9.1 (Quality variation for special GCD subgraphs). Let G = (µ, V, W, E, P, f, g) be a non-trivial GCD graph, let p ∈ R(G) and let k, ℓ ∈ Z. If µ(Vpk), µ(Wpℓ) > 0, then

q(Gpk,pℓ) q(G)

![image 432](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile432.png>)

=

µ(Epk,pℓ) µ(E)

![image 433](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile433.png>)

2+τ µ(V) µ(Vpk)

![image 434](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile434.png>)

1+τ µ(W) µ(Wpℓ)

![image 435](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile435.png>)

1+τ

p|k−ℓ|.

Proof. This follows directly from the deﬁnitions. There is a small difference compared to Lemma 11.1 in [22] due to the modiﬁed deﬁnition of q(G).

- Lemma 9.2 (Few edges between unbalanced sets, I). Let G = (µ, V, W, E, P, f, g) be a non-trivial GCD graph. Let p ∈ R(G), r ∈ Z 1 and k ∈ Z be such that pr > C4 and6

µ(Wpk) µ(W)

![image 436](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile436.png>)

1 −

C2 p

![image 437](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile437.png>)

;

If we set Lk,r = {ℓ ∈ Z : |ℓ − k| r + 1}, then one of the following holds:

- (a) There exists ℓ ∈ Lk,r such that q(Gpk, pℓ) > M · q(G).
- (b) ℓ∈L


k,r

µ(Epk, pℓ) µ(E)/(4p1+τ/4).

Proof. This result is Lemma 11.3 in [22], with the only differences being the following ones: (i) k and ℓ are allowed to lie in Z and not just in Z 0 due to our more general deﬁnition of GCD graphs that allows rational vertices; (ii) the conclusion in (a) is slightly stronger than in [22, Lemma 11.3] due to the modiﬁed deﬁnition of q(·) used here, with the omission of the factors (1 − f(p)=g(p) =0/p)−2(1 − 1/p1+τ/4)−3. Note however that these factors are not used in the proof of [22, Lemma 11.3]; they are only exploited in [22, Lemma 15.1]. In conclusion, the argument of [22] goes through to our more general context with minimal changes.

We also need the symmetric version of Lemma 9.2:

- Lemma 9.3 (Few edges between unbalanced sets, II). Let G = (µ, V, W, E, P, f, g) be a nontrivial GCD graph. Let p ∈ R(G), r ∈ Z 1 and ℓ ∈ Z be such that pr > C4 and

µ(Vpℓ) µ(V)

![image 438](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile438.png>)

1 −

C2 p

![image 439](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile439.png>)

.

If we set Kℓ,r = {k ∈ Z : |ℓ − k| r + 1}, then one of the following holds:

- (a) There exists k ∈ Kℓ,r such that q(Gpk, pℓ) > M · q(G).
- (b) k∈K


ℓ,r

µ(Epk, pℓ) µ(E)/(4p1+τ/4).

- Lemma 9.4 (Quality increment unless a prime power divides almost all). Consider a non-trivial


GCD graph G = (µ, V, W, E, P, f, g) and a prime p ∈ R(G) with p > C2. Then one of the following holds:

- (a) There is a non-trivial, maximal and exact GCD subgraph G′ of G with multiplicative data (P′, f′, g′) such that


P′ = P ∪ {p}, R(G′) ⊆ R(G) \ {p}, q(G′) M f′(p) =g′(p)

· q(G).

![image 440](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile440.png>)

6If p C2, the last hypothesis is vacuous.

- (b) There exists k ∈ Z such that


µ(Wpk) µ(W)

µ(Vpk) µ(V)

C2 p

C2 p

1 −

1 −

.

and

![image 441](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile441.png>)

![image 442](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile442.png>)

![image 443](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile443.png>)

![image 444](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile444.png>)

- Proof. This result is Lemma 13.2 in [22], with the only differences being that we use the modiﬁed

deﬁnition of q(·) in part (a), and that in part (b) we allow k to lie in Z instead of Z 0. The argument of [22] goes through with minimal changes.

Deduction of Proposition 7.12. Using the above lemma, we readily establish Proposition 7.12. For more details, see the deduction of [22, Proposition 8.1] from [22, Lemma 13.2].

Lemma 9.5 (Small quality loss or a prime power divides a positive proportion). Consider a nontrivial GCD graph G = (µ, V, W, E, P, f, g) and a prime p ∈ R(G). Then one of the following holds:

(a) There is a non-trivial and exact GCD subgraph G′ of G with set of primes P′ such that P′ = P ∪ {p}, R(G′) ⊆ R(G) \ {p}, q(G′) q(G)/C3. (b) There is some k ∈ Z such that

µ(Vpk) µ(V)

![image 445](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile445.png>)

- 9

![image 446](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile446.png>)

- 10


and

µ(Wpk) µ(W)

![image 447](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile447.png>)

- 9

![image 448](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile448.png>)

- 10


.

- Proof. This result is Lemma 14.1 in [22], with the only differences being that we use the modiﬁed


deﬁnition of q(·) in part (a), and that in part (b) we allow k to lie in Z instead of Z 0. The argument of [22] goes through with minimal changes. Note that, even though Lemma 14.1 in [22] does not specify that G′ is an exact subgraph of G, this fact follows readily from the proof, because we end up taking G′ = Gpk,pℓ for some k, ℓ ∈ Z.

- Lemma 9.6 (Adding small primes to P). Let G = (µ, V, W, E, P, f, g) be a non-trivial GCD graph and let p ∈ R(G) be a prime. Then there is a non-trivial and exact GCD subgraph G′ of G with set of primes P′ such that


P′ = P ∪ {p}, R(G′) ⊆ R(G) \ {p}, q(G′) q(G)/C5.

Proof. This result is Lemma 14.2 in [22] adapted to our more general deﬁnition of GCD graphs with rational vertices. The argument of [22] goes through to this more general context with minimal changes, using Lemmas 9.4 and 9.5 above. Note that, even though Lemma 14.2 in [22] does not specify that G′ is an exact subgraph of G, this fact follows readily from the proof, because we

end up taking G′ = G(1)p

k,pℓ for some k, ℓ ∈ Z, where G(1) is a maximal GCD subgraph of G. Deduction of Proposition 7.11. Using the above lemma, we readily establish Proposition 7.11. For more details, see the deduction of [22, Proposition 8.3] from [22, Lemma 14.2].

10. PROOF OF PROPOSITION 7.13

As in the statement of Proposition 7.13, let G = (µ, V, W, E, P, f, g) be a non-trivial and maximal GCD graph such that

R(G) ⊆ {p > C6} and R♭(G) = ∅.

If R(G) = ∅, then G is structured for trivial reasons, so that Proposition 7.13 follows by taking G′ = G. Let us thus assume that R(G) = ∅.

Now, ﬁx for the moment a prime p ∈ R(G). Since R♭(G) = ∅, we must have that p ∈ R♯(G), and thus there exists some integer kp such that

µ(Wpkp) µ(W)

µ(Vpkp) µ(V)

C2 p

C2 p

1 −

1 −

.

and

- (10.1)


![image 449](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile449.png>)

![image 450](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile450.png>)

![image 451](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile451.png>)

![image 452](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile452.png>)

These inequalities, together with the maximality of G and Lemma 5.12, applied with θ = 2 + τ, η = C2/p, A = V \ Vpkp and B = W \ Wpkp, imply that

- (10.2) µ E V \ Vpkp, W \ Wpkp

C2 p

![image 453](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile453.png>)

1+2.τ01

![image 454](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile454.png>)

µ(E)

µ(E) 2p1+

![image 455](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile455.png>)

τ 4

![image 456](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile456.png>)

,

where we used that p > C6 C210/τ (cf. (7.4)) and that τ ∈ (0, 1/100). Moreover, using again the fact that p ∈ R♯(G), we ﬁnd that

- (10.3) q(Gpi,pj) < M · q(G) for all (i, j) ∈ Z2 with i = j. In particular, if we set

Vp∗ :=

kp+1

i=kp−1

Vpi and Wp∗ :=

kp+1

j=kp−1

Wpj,

then Lemmas 9.2 and 9.3 applied with r = 1 imply that

- (10.4) µ E V \ Vp∗, Wpkp =

i∈Z : |i−kp| 2

µ Epi,pkp

µ(E) 4p1+

![image 457](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile457.png>)

τ 4

![image 458](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile458.png>)

,

and

- (10.5) µ E Vpkp, W \ Wp∗ =

j∈Z : |j−kp| 2

µ Epkp,pj

µ(E) 4p1+

![image 459](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile459.png>)

τ 4

![image 460](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile460.png>)

.

Hence, if we let

Ep∗ := E Vpkp, Wp∗ ∪ E Vp∗, Wpkp , then (10.2), (10.4) and (10.5) imply that

- (10.6) µ(E \ Ep∗)

µ(E) p1+

![image 461](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile461.png>)

τ 4

![image 462](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile462.png>)

for all p ∈ R(G). Now, let us set

E∗ :=

p∈R(G)

Ep∗.

Using (10.6) and our assumption that R(G) ⊆ {p > C6}, we ﬁnd that

- (10.7) µ E \ E∗

p∈R(G)

µ(E \ Ep∗)

p>C6

µ(E) p1+

![image 463](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile463.png>)

τ 4

![image 464](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile464.png>)

10µ(E) τC6τ/4

![image 465](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile465.png>)

µ(E) 100

![image 466](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile466.png>)

,

since n>x n−1−c x−1−c + x ∞ y−1−c dy = c+1c x−1−c for all c > 0 and all x 1, and we have assumed that C6 C210/τ (105/τ)10/τ. Hence, if we let G∗ = (V, W, E∗, P, f, g), then

![image 467](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile467.png>)

- (10.8)


2+τ

q(G∗) q(G)

µ(E∗) µ(E)

0.992+τ > 0.98 for τ 0.01. We may easily check that G∗ is a structured GCD graph and a GCD subgraph of G.

=

![image 468](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile468.png>)

![image 469](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile469.png>)

Next, we show that condition (b) of Proposition 7.13 holds for some appropriate subgraph of G∗ by adapting the argument leading to [22, Corollary 11.8 and Lemmas 8.4-8.5]. To this end, ﬁx an index m ∈ {1, . . ., n} and recall the weights ap,m 0 from the statement of Proposition 7.13. Given ̺ ∈ Q>0, let us deﬁne Am(̺) = p∈̺, p∈R(G) ap,m. We then have that

- (10.9)

(v,w)∈E∗

µ(v)µ(w)Am(v/w) =

p∈R(G)

ap,m · µ (v, w) ∈ E∗ : p ∈ v/w .

Note that if p ∈ R(G) is a prime of v/w, then we must have that ep(v) = ep(w). Since we also know that (v, w) ∈ E∗ ⊆ Ep∗, we conclude that (v, w) lies in Epi,pj with (i, j) ∈ {(kp, kp + 1), (kp, kp − 1), (kp − 1, kp), (kp + 1, kp)}. For all these choices of (i, j), we may use relations

- (10.1) and (10.3) in conjunction with Lemma 9.1 to ﬁnd that

M >

q(Gpi,pj) q(G)

![image 470](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile470.png>)

=

µ(Epi,pj) µ(E)

![image 471](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile471.png>)

2+τ µ(V) µ(Vpi)

![image 472](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile472.png>)

1+τ µ(W) µ(Wpj)

![image 473](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile473.png>)

1+τ

p

µ(Epi,pj) µ(E)

![image 474](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile474.png>)

2+τ p2+τ C21+τ

![image 475](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile475.png>)

, whence

µ(Epi,pj) µ(E)

![image 476](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile476.png>)

<

MC21+τ p

- 1

![image 477](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile477.png>)

- 2+τ


![image 478](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile478.png>)

<

MC2 p

![image 479](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile479.png>)

=

C8 100p

![image 480](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile480.png>)

. Therefore,

µ (v, w) ∈ E∗ : p ∈ v/w < 4 ·

C8 100p · µ(E) <

![image 481](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile481.png>)

C8 20p · µ(E∗),

![image 482](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile482.png>)

in virtue of (10.7). Inserting this bound into (10.9), we conclude that (10.10)

(v,w)∈E∗

µ(v)µ(w)Am(v/w) <

C8 20

![image 483](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile483.png>)

p∈R(G)

ap,m

![image 484](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile484.png>)

p · µ(E∗) for m = 1, 2, . . ., n. Now, let

E∗∗ = (v, w) ∈ E∗ : Am(v/w) C8n

p∈R(G)

ap,m p

![image 485](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile485.png>)

for m = 1, 2, . . ., n .

Using the union bound, Markov’s inequality and (10.10), we ﬁnd that µ(E∗ \ E∗∗) 20 1 · µ(E∗). Hence, if we let G∗∗ = (V, W, E∗∗, P, f, g), then

![image 486](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile486.png>)

q(G∗∗) q(G∗)

![image 487](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile487.png>)

=

µ(E∗∗) µ(E∗)

![image 488](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile488.png>)

2+τ 19 20

![image 489](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile489.png>)

2+τ

> 0.9.

- Together with (10.8), this implies that q(G∗∗) q(G)/2. Clearly, G∗∗ is a structured GCD graph


and we also have that Am(v/w) C8n p∈R(G) ap,mp for all (v, w) in its edge set E∗∗ and for all m ∈ {1, . . ., n}. To complete the proof, we take G′ to be a maximal GCD subgraph of G∗∗.

![image 490](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile490.png>)

11. PROOF OF PROPOSITIONS 7.14 AND 7.15

Lemma 11.1 (Small quality loss in a structured graph). Consider a maximal, non-trivial and structured GCD graph G = (µ, V, W, E, P, f, g) and a prime p ∈ R(G) with p > C6, and let kp ∈ Z be such that

- (11.1) ep(v), ep(w) ∈ (kp − 1, kp), (kp, kp − 1), (kp, kp), (kp, kp + 1), (kp + 1, kp)




for all (v, w) ∈ E. Then there is a non-trivial and maximal GCD subgraph G′ of G with multiplicative data (P′, f′, g′) such that:

- (a) P′ = P ∪ {p};
- (b) R(G′) ⊆ R(G) \ {p};
- (c) f′(p), g′(p) ∈ {kp − 1, kp, kp + 1};
- (d) if kp > 0, then G′ is a denominator-exact subgraph of G, whereas if kp < 0, then G′ is a numerator-exact subgraph of G;
- (e) q(G′) q(G) 1 − f′(p)=g′(p)=kp/p 2 1 − 1/p1+


τ

4 .

![image 491](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile491.png>)

Proof. Before we begin, let us note that any non-trivial and exact subgraph G′ of G automatically satisﬁes property (c). Indeed, since G′ is non-trivial, it has at least one edge, which must satisfy

- (11.1). Since G′ is also an exact subgraph of G, we conclude that it must satisfy (c). In addition, note that any G′ satisfying (e) is non-trivial. Indeed, we have q(G) > 0 because G


is non-trivial. In virtue of (e), we must also have that q(G′) > 0. Thus, G′ is non-trivial. Let us now proceed to the main part of the proof. We shall separate various cases. Case 1: p ∈ R♭(G). We must then be in one of following two subcases:

- Case 1a: there exist distinct integers i, j such that q(Gpi,pj) M ·q(G). We then simply take G′

to be a maximal GCD subgraph of Gpi,pj. This completes the proof, since G′ is an exact subgraph of G and it satisﬁes q(G′) M · q(G) > q(G).

- Case 1b: for every k ∈ Z, we have min{µ(Vpk), µ(Wpk)} < 1 − C2/p. We then apply Lemma


9.4 (we must be in case (a) of the lemma by the above assumption) to locate a subgraph G′ of G satisfying all desired properties.

Case 2: p ∈ R♯(G). Hence, there exists k ∈ Z such that

- (11.2)

µ(Vpk) µ(V)

![image 492](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile492.png>)

1 −

C2 p

![image 493](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile493.png>)

and

µ(Wpk) µ(W)

![image 494](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile494.png>)

1 −

C2 p

![image 495](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile495.png>)

. To proceed further, we separate into four cases.

Case 2a: k = kp − 1. Let

E∗ := (v, w) ∈ E : ep(v), ep(w) ∈ (k − 1, k), (k, k − 1), (k, k), (k, k + 1), (k + 1, k) . On the one hand, using (11.1) and our assumption that k = kp − 1, we have that

- (11.3) E∗ = (v, w) ∈ E : ep(v), ep(w) ∈ {(k, k + 1), (k + 1, k) .


On the other hand, using (11.2) and arguing as in the proof of Proposition 7.13 in Section 10, with k playing the role of kp, we ﬁnd that µ(E \ E∗) µ(E)/p1+

τ

4, and thus µ(E∗) µ(E)/2.

![image 496](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile496.png>)

- Together with (11.3), this implies that either µ(Epk,pk+1) µ(E)/4 or µ(Epk+1,pk) µ(E)/4. In the former case, Lemma 9.1 yields that q(Gpk,pk+1)/q(G) 4−2−τp 1. In the latter case, we ﬁnd similarly that q(Gpk+1,pk) q(G). We then take G′ to be a maximal GCD subgraph of Gpk,pk+1 or of Gpk+1,pk, according to the subcase we are in. In particular, G′ is an exact GCD subgraph of G. We may then check easily that G′ satisﬁes all required properties.


- Case 2b: k = kp + 1. If E∗ is deﬁned as above, we have E∗ = {(v, w) ∈ E : (ep(v), ep(w) ∈

{(k − 1, k), (k, k − 1)}}. Hence, we may argue similarly to Case 2a to complete the proof.

- Case 2c: k = kp > 0. Let G+ = (µ, V+, W+, E+, P ∪ {p}, fpk, gpk), where: V+ = Vpk ∪ Vpk+1, W+ = Wpk ∪ Wpk+1, E+ = E V+, W+ ,


and fpk and gpk are as in Deﬁnition 7.7. It is easy to check that G+ is a GCD subgraph of G satisfying properties (a)-(d)7. Moreover, both Gpk,pk−1 and Gpk−1,pk are GCD subgraphs of G satisfying properties (a)-(d). Furthermore, if we follow the proof of Lemma 15.1 in [22] (see Case 2 there), we may show that at least one of the graphs G+, Gpk,pk−1 and Gpk−1,pk also satisﬁes property (e). Let us call G∗ this GCD subgraph of G. To complete the proof of the lemma, we take G′ to be a maximal subgraph of G∗.

Case 2d: k = kp < 0. Let G− = (µ, V−, W−, E−, P ∪ {p}, fpk, gpk), where:

V− = Vpk−1 ∪ Vpk, W− = Wpk−1 ∪ Wpk, E− = E V−, W− . This is a GCD subgraph of G satisfying properties (a)-(d). To complete the proof, we argue similarly to Case 2c, selecting G′ to be a maximal subgraph of one of the graphs G−, Gpk,pk+1 and Gpk+1,pk.

- Proof of Proposition 7.14. This follows almost immediately from Lemma 11.1. Our assumptions that G is structured, that R(G) ⊆ {p > C6} and that R−(G) = ∅ imply that there is a prime p > C6 lying in R(G) with kp < 0 (see Remark 7.2). Thus we can apply Lemma 11.1 with this choice of p and complete the proof.
- Proof of Proposition 7.15. As above, this follows almost immediately from Lemma 11.1.


ACKNOWLEDGMENTS

We would like to thank Andrew Granville and Manuel Hauke for useful discussions on Erd˝os’s integer dilation approximation problem. In particular, the name of the problem is due to the former.

DK is supported by the Courtois Chair II in fundamental research, by the Natural Sciences and Engineering Research Council of Canada (RGPIN-2018-05699 and RGPIN-2024-05850) and by the Fonds de recherche du Que´bec - Nature et technologies (2022-PR-300951 and 2025-PR345672).

YL is supported by a junior chair of the Institut Universitaire de France, and was supported by a Simons-CRM visiting professorship while an essential part of this work was carried. In particular, YL would like to thank the Centre de Recherches Mathe´matiques for its excellent working conditions.

JDL is supported by an NSF MSPRF fellowship, and would like to thank the Institut Elie´ Cartan de Lorraine and the Centre de Recherches Mathe´matiques for their hospitality.

REFERENCES

- [1] R. Ahlswede, L. Khachatrian, A. Sa´rko¨zy, On the density of primitive sets. J. Number Theory, (2004), 319–361.
- [2] F. Behrend, On sequences of numbers not divisible by another. J. Lond. Math. Soc. (1935), 42–45.
- [3] A. S. Besicovitch, On the density of certain sequences of integers, Math. Ann. 110 (1934), 336–341.
- [4] P. Erdo˝s, Note on sequences of integers no one of which is divisible by any other. J. London Math. Soc. (1935), 126–128.
- [5] , On the density of some sequences of integers. Bull. Amer. Math. Soc. 54 (1948), 685–692.

![image 497](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile497.png>)

- [6] , Some unsolved problems. Magyar Tud. Akad. Mat. Kutato´ Int. Ko¨zl. (1961), 221–254.

![image 498](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile498.png>)

- [7] , Quelques problemes` de theorie´ des nombres, Monographies de l’Enseignement Mathe´matique, No. 6 , pp. 81–135, L’Enseignement Mathe´matique, Universite´, Geneva, 1963.


![image 499](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile499.png>)

![image 500](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile500.png>)

7G+ is a denominator-exact subgraph of G because if (a/q,b/r) ∈ V+ × W+ with gcd(a,q) = gcd(b,r) = 1, then ep(a/q),ep(b/r) k > 0, and thus ep(q) = 0 = fp−

(p) and ep(r) = 0 = gp−

(p).

k

k

- [8] , Problems and results on combinatorial number theory. A survey of combinatorial theory (Proc. Internat. Sympos., Colorado State Univ., Fort Collins, Colo., 1971), pp. 117–138. North-Holland Publishing Co., Amsterdam-London, 1973.

![image 501](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile501.png>)

- [9] , Problems and results on Diophantine approximations, II. Lecture Notes in Math., 475 , pp. 89–99, Springer, Berlin, 1975.

![image 502](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile502.png>)

- [10] , Problemes` extremaux´ et combinatoires en theorie´ des nombres, Se´minaire Delange-Pisot-Poitou (17e anne´e: 1975/76), The´orie des nombres, Fasc. 2, Exp. No. 67 , 5 pp., Secre´tariat Mathe´matique, Paris, 1977.

![image 503](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile503.png>)

- [11] , A survey of problems in combinatorial number theory, Combinatorial mathematics, optimal designs and their applications Ann. Discrete Mathematics 6 (1980), 89–115.

![image 504](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile504.png>)

- [12] , Some of my forgotten problems in number theory. Hardy-Ramanujan J. 15 (1992), 34–50.

![image 505](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile505.png>)

- [13] , Some of my favorite problems and results. The mathematics of Paul Erdo˝s, I, 47–67. Algorithms Combin., 13, Springer-Verlag, Berlin, 1997.

![image 506](<2025-koukoulopoulos-erd-integer-dilation-approximation_images/imageFile506.png>)

- [14] P. Erdo˝s and A. Sa´rko¨zy, Some solved and unsolved problems in combinatorial number theory. Math. Slovaca 28

(1978) no. 4, 407–421

- [15] P. Erdo˝s, A. Sa´rko¨zi and E. Szemere´di, On divisibility properties of sequences of integers. Colloq. Math. Soc. Ja´nos Bolyai, 2 North-Holland Publishing Co., Amsterdam-London, 1968, pp. 35–49.
- [16] B. Green and A. Walker, Extremal problems for GCDs. Combin. Probab. Comput. 30 (2021), no. 6, 922–929.
- [17] A. J. Haight, On multiples of certain real sequences. Acta Arith. 49 (1988), no. 3, 303–306.
- [18] G. Harman, Metric number theory. London Math. Soc. Monogr. (N.S.), 18 The Clarendon Press, Oxford University Press, New York, 1998, xviii+297 pp.
- [19] M. Hauke, S. Vazquez Saez and A. Walker, Proving the Dufﬁn-Schaeffer conjecture without GCD graphs. Preprint (2024), 27 pages, arXiv:2404.15123.
- [20] D. Koukoulopoulos, The distribution of prime numbers. Graduate Studies in Mathematics, 203. American Mathematical Society, Providence, RI, 2019.
- [21] D. Koukoulopoulos and J. Maynard, On the Dufﬁn-Schaeffer conjecture. Ann. of Math. (2) 192 (2020), no. 1, 251–307.
- [22] D. Koukoulopoulos, J. Maynard and D. Yang, An almost sharp quantitative version of the Dufﬁn-Schaeffer conjecture. Duke Math. J., to appear. Preprint available (arXiv:2404.14628).
- [23] A. D. Pollington and R. C. Vaughan, R. C., The k-dimensional Dufﬁn and Schaeffer conjecture. Mathematika 37

(1990), no. 2, 190–200.

- [24] E. Sperner, Ein Satz uber¨ Untermengen einer endlichen Menge, Math. Z. 27 (1928) 544–548.


DEPARTEMENT´ DE MATHEMATIQUES´ ET DE STATISTIQUE, UNIVERSITE´ DE MONTREAL´ , CP 6128 SUCC.

CENTRE-VILLE, MONTREAL´ , QC H3C 3J7, CANADA Email address: dimitris.koukoulopoulos@umontreal.ca UNIVERSITE´ DE LORRAINE, CNRS, IECL, AND INSTITUT UNIVERSITAIRE DE FRANCE, F-54000 NANCY,

FRANCE Email address: youness.lamzouri@univ-lorraine.fr DEPARTMENT OF MATHEMATICS, STANFORD UNIVERSITY, STANFORD, CA, USA Email address: jared.d.lichtman@gmail.com

