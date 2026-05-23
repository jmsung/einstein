---
type: source
kind: paper
title: When the sieve works
authors: Andrew Granville, Dimitris Koukoulopoulos, Kaisa Matomäki
year: 2012
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/1205.0413v2
source_local: ../raw/2012-granville-when-sieve-works.pdf
topic: general-knowledge
cites:
---

arXiv:1205.0413v2[math.NT]19Oct2015

WHEN THE SIEVE WORKS

ANDREW GRANVILLE, DIMITRIS KOUKOULOPOULOS, AND KAISA MATOMAKI¨

Abstract. We are interested in classifying those sets of primes P such that when we sieve out the integers up to x by the primes in Pc we are left with roughly the expected number of unsieved integers. In particular, we obtain the ﬁrst general results for sieving an interval of length x with primes including some in (√x,x], using methods motivated by additive combinatorics.

![image 1](<2012-granville-when-sieve-works_images/imageFile1.png>)

1. Introduction and motivation

Let E be a given subset of the primes ≤ x. The simplest sieve problem asks for estimates of S(T, T + x; E), the number of integers n in an interval (T, T + x] which have no prime factors in the set E (we write (n, E) = 1 for convenience). By a simple inclusion-exclusion argument one expects that the number of such integers is about

1 p

x

1 −

.

![image 2](<2012-granville-when-sieve-works_images/imageFile2.png>)

p∈E

This is provably always an upper bound, up to a constant: S(T, T + x; E) ≪ x

1 p

,

1 −

![image 3](<2012-granville-when-sieve-works_images/imageFile3.png>)

p∈E

and one gets the analogous lower bound S(T, T + x; E) ≫ x

1 p

,

1 −

![image 4](<2012-granville-when-sieve-works_images/imageFile4.png>)

p∈E

if E is a subset of the primes up to x1/2−o(1) (see [4, Theorem 11.13] noticing that the sieving limit β = 2 for κ = 1). There seems to be little hope, in this generality, of increasing the exponent “1/2” without major new ideas. Moreover, one needs to have careful hypotheses: if, for instance, E = {p ≤

√x}∪{x/ log x < p ≤ x} then S(0, x; E) = π(x/ log x)−π(√x)+1 ∼ x/ log2 x, whereas our prediction was ≍ x/ log x.

![image 5](<2012-granville-when-sieve-works_images/imageFile5.png>)

![image 6](<2012-granville-when-sieve-works_images/imageFile6.png>)

In this article we will prove lower bounds on S(0, x; E) in certain cases not covered by classical sieve theory, and use this evidence to guess at lower bounds in more generality. Let us ﬁrst introduce some notation. Let P be a given subset of the primes ≤ x, and E = {p ≤ x : p  ∈ P}, so that E ∪ P is a partition of the primes ≤ x. Let Ψ(x; P) denote the number of integers up to x all of whose prime factors are in P, that is

Ψ(x; P) :=

1 =

1 = S(0, x; E).

n≤x p|n =⇒ p∈P

n≤x (n,E)=1

![image 7](<2012-granville-when-sieve-works_images/imageFile7.png>)

Date: October 30, 2018. Partially supported by NSERC. Supported by the Academy of Finland grant no. 137883.

1

The inclusion-exclusion argument predicts that

−1

1 p

.

Ψ(x; P) ≈ x/uP, where uP :=

1 −

![image 8](<2012-granville-when-sieve-works_images/imageFile8.png>)

p∈E

Hall [6] proved that Ψ(x; P) (eγ/uP) x, where γ = 0.5772156649 . . . is the Euler-Mascheroni constant. Subsequently, the authors of [5] improved this to Ψ(x; P) (eγ/uP −1/uP2+o(1)) x, and showed that this is “best possible” other than being more precise than the “o(1)” (which tends to 0 when uP → ∞). However, in this paper, we are interested in lower bounds on Ψ(x; P).

Hildebrand [7] showed that, Ψ(x; P) Ψ(x; P′) where P′ is the set of primes up to x1/u

P

(note that here uP′ ∼ uP). Speciﬁcally, he showed that

Ψ(x; P) x

ρ(uP);

![image 9](<2012-granville-when-sieve-works_images/imageFile9.png>)

here ρ(u) is the Dickman–de Bruijn function, deﬁned by ρ(u) = 1 for 0 ≤ u ≤ 1, and uρ′(u) = −ρ(u−1) for all u ≥ 1. One can show that ρ(u) = 1/uu+o(u), which is a lot smaller than the expected 1/u. (See [5] for a diﬀerent proof of Hildebrand’s result.)

This last example is very special in that P contains no large primes, and it is expected that other than for certain other extraordinary sets P one has

1 p

1 −

Ψ(x; P) ≍ x

.

![image 10](<2012-granville-when-sieve-works_images/imageFile10.png>)

p∈E

However this question has not really been studied in detail and there are other examples that must be taken into account: Let

- (1.1) {p prime : xm/(N+1) < p < xm/N}.

Any product ≤ x of primes in these intervals lies in some interval of the same form. If now n = p1p2 · · ·pk ≤ x, where xm

j/(N+1) < pj < xm

j/N, then m1 + · · · + mk ≤ N. The number of such integers n with m1 + · · · + mk ≤ N − 1 is ≤ x1−1/N. On the other hand, if m1+· · ·+mk = N, then k ≥ 2 (since each mj ≤ N−1) and therefore Ψ(x; P) ≪N x/(log x)2, far smaller than the expected x/uP ≍ x/ log x. A key thing to notice is that, in this example,

p∈P

1 p ∼ (N − 1) log(1 + 1/N) = 1 −

![image 11](<2012-granville-when-sieve-works_images/imageFile11.png>)

3/2 + o(1) N

![image 12](<2012-granville-when-sieve-works_images/imageFile12.png>)

< 1,

by the prime number theorem, as N → ∞. Hence we see that we can obtain a very small Ψ(x; P) when p∈P 1p < 1. One might guess that the issue in the last example is that there are no small primes in P. However, if we let P = {p prime : p ≤ x1/N

![image 13](<2012-granville-when-sieve-works_images/imageFile13.png>)

2

} ∪

1≤m≤N−1

- (1.2) {p prime : xm/(N+1) < p < xm/N},


P =

1≤m≤N−1

then we would also ﬁnd that Ψ(x; P) is far smaller than expected if N → ∞ slowly enough.

One might also guess that the main issue in the above examples is that there are no large primes in P. However if we let

P = {p prime : x1/v < p ≤ x1/u} ∪ {p prime : x1−1/v < p ≤ x},

then Ψ(x; P) = Ψ(x; Q) + π(x) − π(x1−1/v) where Q = {p : x1/v < p ≤ x1/u}. Friedlander [3] established that Ψ(x; Q) ∼ σ(u, v)x/ log(x1/v) where σ(u, v) = e−γρ(u) + O(1/v log v). Hence if v > u(1+ǫ)u then Ψ(x; P) ∼ e−γvρ(u)x/ log x as u → ∞, whereas the “expected” value is

e−γv2 u(v − 1) ·

1 p ∼

x log x

x

1 −

.

![image 14](<2012-granville-when-sieve-works_images/imageFile14.png>)

![image 15](<2012-granville-when-sieve-works_images/imageFile15.png>)

![image 16](<2012-granville-when-sieve-works_images/imageFile16.png>)

p∈E

Hence the ratio Ψ(x; P)/“expected value” is asymptotic to uρ(u)(1 − 1/v), which goes to 0 rapidly as u → ∞.

So we see that the size of the primes in P does not seem to determine whether Ψ(x; P) is close to its “expected value”. Rather, we believe that the most important quantity in determining whether the sieve will work somewhat as expected is the largest y for which

1

p > 1.

![image 17](<2012-granville-when-sieve-works_images/imageFile17.png>)

p∈P, p≥y

Conjecture 1. Fix ǫ > 0. There exists a positive constant c such that if P is a subset of the primes ≤ x for which there is some v ≤ c√log x with

![image 18](<2012-granville-when-sieve-works_images/imageFile18.png>)

1 p ≥ 1 + ǫ,

![image 19](<2012-granville-when-sieve-works_images/imageFile19.png>)

p∈P x1/ev<p≤x

then

1 p

Ψ(x; P) x ≥ Av

,

1 −

![image 20](<2012-granville-when-sieve-works_images/imageFile20.png>)

![image 21](<2012-granville-when-sieve-works_images/imageFile21.png>)

p∈E

where Av is a constant with Av = v−v(1+oǫ(1)) as v → ∞.

- Remark 1.1. Note that if P = {p ≤ x1/u}, then Ψ(x; P)/x ∼ ρ(u). Also, taking v ∼ u in the above conjecture yields Ψ(x; P)/x Av/u and so Av uρ(u) = v−v(1+o(1)). One can even make the bolder guess that Av ∼ vρ(v).
- Remark 1.2. Proposition 2.6 below implies that if


1

κ :=

![image 22](<2012-granville-when-sieve-works_images/imageFile22.png>)

- (1.3) p


p∈P x1/u<p≤x

is very small, then Ψ(t; P) is indeed substantially smaller than expected for some t ∈ [√x, x]. If, in addition, P ⊂ [1, x1−ǫ], then we can take t = x. Hence it is certainly true that the size of κ is important consideration. It would be interesting to obtain the strongest possible uniform version of Proposition 2.6.

![image 23](<2012-granville-when-sieve-works_images/imageFile23.png>)

On the other hand, Corollary 2.3 below implies that as soon as κ > ǫ for some positive constant ǫ, then there is a point t ∈ [x1/u, x] for which Ψ(t; P) is of the expected size. It turns out to be a combinatorial problem to see if t = x works and, in light of Bleichenbacher’s theorem below, we believe that combinatorial obstructions, such the ones occurring for the sets P given by (1.1) and by (1.2), disappear as soon as κ ≥ 1 + ǫ.

The main result in this paper is a weak form of Conjecture 1:

Theorem 1. There exist positive constants λ and c such that if P is a subset of the primes ≤ x for which there is some v ≤ c√log x with

![image 24](<2012-granville-when-sieve-works_images/imageFile24.png>)

1 p ≥ 1 + λ,

![image 25](<2012-granville-when-sieve-works_images/imageFile25.png>)

p∈P x1/ev<p≤x

then

Ψ(x; P) x ≫

1 p

1 vO(v) p∈E

.

1 −

![image 26](<2012-granville-when-sieve-works_images/imageFile26.png>)

![image 27](<2012-granville-when-sieve-works_images/imageFile27.png>)

![image 28](<2012-granville-when-sieve-works_images/imageFile28.png>)

- Remark 1.3. One can superﬁcially make Theorem 1 appear stronger. For, if the “O(v)” in our lower bound is short for “Cv”, then, for any ǫ ∈ (0, C), we can replace λ in the hypothesis by Λ := λ + ln(C/ǫ) so that

p∈P xC/ǫev<p≤x

1 p ≥

![image 29](<2012-granville-when-sieve-works_images/imageFile29.png>)

p∈P x1/ev<p≤x

1 p −

![image 30](<2012-granville-when-sieve-works_images/imageFile30.png>)

p∈P x1/ev<p≤xC/ǫev

1 p ≥ 1 + Λ − ln(C/ǫ) = 1 + λ,

![image 31](<2012-granville-when-sieve-works_images/imageFile31.png>)

and hence Theorem 1 implies, for V = ǫv/C, that Ψ(x; P) x ≫

![image 32](<2012-granville-when-sieve-works_images/imageFile32.png>)

1 V CV p∈E

![image 33](<2012-granville-when-sieve-works_images/imageFile33.png>)

1 −

1 p ≥

![image 34](<2012-granville-when-sieve-works_images/imageFile34.png>)

1 vǫv p∈E

![image 35](<2012-granville-when-sieve-works_images/imageFile35.png>)

1 −

1 p

![image 36](<2012-granville-when-sieve-works_images/imageFile36.png>)

.

- Remark 1.4. It will be clear from the proof of Theorem 1 that, under the same assumptions, one gets also the stronger conclusion


Ψ(x; P) − Ψ(x − y; P) y ≫

1 vO(v) p∈E

1 p

1 −

![image 37](<2012-granville-when-sieve-works_images/imageFile37.png>)

![image 38](<2012-granville-when-sieve-works_images/imageFile38.png>)

![image 39](<2012-granville-when-sieve-works_images/imageFile39.png>)

for every y > x1−1/(3ev). Furthermore the conclusion of Theorem 1 continues to hold if, more generally,

1 + λ u

1 p ≥

![image 40](<2012-granville-when-sieve-works_images/imageFile40.png>)

![image 41](<2012-granville-when-sieve-works_images/imageFile41.png>)

p∈P x1/ev<p≤x1/u

for some 1 ≤ u ≤ v ≤ c√log x, where λ and c are absolute constants.

![image 42](<2012-granville-when-sieve-works_images/imageFile42.png>)

The proof of our theorem involves a hodge-podge of techniques, from classical analytic number theory and sieve theory (as one might expect) to additive combinatorics, which seems to be new in this context (though [10] contains some related work as will be explained in Remark 3.1). Our starting point is the following result of Bleichenbacher [1] (see [10, Section 9] for the proof) which may be viewed as a result in continuous additive combinatorics:

Bleichenbacher’s Theorem. If u ≥ 1 and T is an open subset of (0, u1) for which

![image 43](<2012-granville-when-sieve-works_images/imageFile43.png>)

dt t

1 u

, then there exist t1, t2, . . ., tk ∈ T for which t1 + t2 + · · · + tk = 1.

>

![image 44](<2012-granville-when-sieve-works_images/imageFile44.png>)

![image 45](<2012-granville-when-sieve-works_images/imageFile45.png>)

t∈T

Note that this is “best possible” since for the set TN = Nj=1(Nj+1, Nj ) there is no solution to t1 + t2 + · · · + tk = 1 (as any sum of elements in intervals of the form (Nj+1, Nj ) is also in an interval of this form), yet T

![image 46](<2012-granville-when-sieve-works_images/imageFile46.png>)

![image 47](<2012-granville-when-sieve-works_images/imageFile47.png>)

![image 48](<2012-granville-when-sieve-works_images/imageFile48.png>)

![image 49](<2012-granville-when-sieve-works_images/imageFile49.png>)

dt

t ≥ [N/u] log(1 + 1/N) > 1/u − 2/N, which tends

![image 50](<2012-granville-when-sieve-works_images/imageFile50.png>)

N∩(0,1/u)

to 1/u from below as N → ∞. One sees an analogy between this example and the ﬁrst sieve example that we gave above.

The key idea in this paper is to reduce estimates for Ψ(x; P) to quantitative questions of the type addressed in Bleichenbacher’s theorem. Accordingly we make the following conjecture: Hypothesis T. There exists a constant λ3 > 0 such that if 1 ≤ u ≤ v and T is an open subset of (ev1 , u1) for which

![image 51](<2012-granville-when-sieve-works_images/imageFile51.png>)

![image 52](<2012-granville-when-sieve-works_images/imageFile52.png>)

1 + λ3 u

dt t ≥

, then there exists an integer k ∈ [u, ev] and an absolute constant τv > 0 such that

![image 53](<2012-granville-when-sieve-works_images/imageFile53.png>)

![image 54](<2012-granville-when-sieve-works_images/imageFile54.png>)

t∈T

k

dt1dt2 · · ·dtk−1 t1t2 · · ·tk ≥ τv

dt t

. . .

.

![image 55](<2012-granville-when-sieve-works_images/imageFile55.png>)

![image 56](<2012-granville-when-sieve-works_images/imageFile56.png>)

t1+t2+···+tk=1 t1,t2,...,tk∈T

t∈T

By analogy with Bleichenbacher’s Theorem, we conjecture that Hypothesis T holds for any choice of λ3 > 0. The importance of Hypothesis T can be seen in the following consequence, which will be proven in Section 4.

- Proposition 1. If Hypothesis T is true for any ﬁxed λ3 > 0 and τv = v−O(v), then Conjecture 1 holds for any ﬁxed ǫ > 0 with κv = v−O(v).


Actually we will formulate Hypotheses P and A which are analogous to Hypothesis T but Hypothesis P concerns counting primes p1, . . ., pk ∈ P ⊆ P ∩ [x1/ev, x1/u] for which log p1 + . . . + log pk = x + O(1) and Hypothesis A concerns counting integers a1, . . ., ak ∈ A ⊆ N ∩ (N/ev, N/u] for which a1 + . . . + ak = N + O(k). We will show that all the three hypotheses are equivalent and that hypothesis P implies Conjecture 1.

We will use additive combinatorial tools to prove Hypothesis A for some suﬃciently large counterpart of λ3 (see Theorem 6.1) which allows us to deduce Theorem 1 as desired. The value of λ3 can be determined explicitly from the proof, but it will certainly not yield Hypothesis T for every λ3 > 0. See also Remark 6.2 for more discussion about attainable λ-values.

Our results leave us wondering whether Conjecture 1 and Theorem 1 might be an indication of the truth for the more general problem of sieving intervals. Could it be that when we sieve an arbitrary interval of length x, with a not-too-large subset of the primes up to x, then the number of integers left unsieved is predictable? There are only two types of examples known where we can do accurate calculations to better understand sieving: random intervals and intervals where most of the progressions sieved are 0 (mod p), and as far as we know the latter are where most extreme examples come from. Since we have now obtained some understanding of this usual source of extreme examples, we can speculate that this sort of criteria is the main issue, in general.

We conclude by mentioning that, aside from the theoretical interest of understanding the limitations of traditional heuristics in sieve methods, the generality of our results have applications beyond this subject. Indeed, in [9], the third author discovered a rather unexpected application of these methods to counting real zeroes of holomorphic cusp forms.

Overview of the paper. The paper is organized as follows: In Section 2 we explore what happens when κ deﬁned by (1.3) is rather small. In particular, we show that as soon as κ > ǫ, the quantity Ψ(t; P) has the expected size for some t ∈ [x1/u, x]. Conversely, if κ = o(1) as u → ∞, then the size of Ψ(t; P) is much smaller than expected for a certain

t ∈ [√x, x]. This makes it evident that in order for the sieve to work as expected, we need κ to have some size. As Bleichenbacher’s Theorem and the examples given in (1.1) and in (1.2) indicate, we should have that κ > 1. However, traditional sieve methods are incapable of handling this problem. Enter additive combinatorics. Indeed, as the results of Section 3 show, after some technical manipulations we can reduce the problem of bounding Ψ(x; P) from below to counting k-tuples of primes (p1, . . ., pk) ∈ (P ∩ [x1/u, x])k such that log p1+· · ·+log pk = log x+O(1), for some appropriate k. This reformulation of the problem, which we call Hypothesis P in analogy with Hypothesis T, makes clear the connection with additive combinatorics. In order to crystallize this connection even further and open the door to the use of additive combinatorial tools, in Section 4 we formulate the Hypothesis A, which is a purely combinatorial analogue of Hypothesis P and can be viewed as the discrete version of Hypothesis T. All these diﬀerence hypotheses are, in fact, equivalent as we show in Section 4. It is Hypothesis A that we will eventually prove in Section 6, using some tools of discrete additive combinatorics developed in Section 5. Finally, in Section 8, we explore further the connections between our three diﬀerence hypotheses, A, P and T.

![image 57](<2012-granville-when-sieve-works_images/imageFile57.png>)

2. Sieving with logarithmic weights

If we introduce the weight 1/n at each integer n (the so-called “logarithmic weights”), then we simplify the problem enormously: Lemma 2.1. If P is a subset of the primes ≤ x and E = {p ≤ x} \ P, then

1 p

1 n

1 log x n≤x

1 p

eγ

1 −

,

1 −

![image 58](<2012-granville-when-sieve-works_images/imageFile58.png>)

![image 59](<2012-granville-when-sieve-works_images/imageFile59.png>)

![image 60](<2012-granville-when-sieve-works_images/imageFile60.png>)

![image 61](<2012-granville-when-sieve-works_images/imageFile61.png>)

p∈E

p∈E

p|n =⇒ p∈P

where γ is the Euler-Mascheroni constant. Proof. Let us ﬁrst prove the lower bound. We have

−1

1 p

1 ℓ

1 −

,

≥

![image 62](<2012-granville-when-sieve-works_images/imageFile62.png>)

![image 63](<2012-granville-when-sieve-works_images/imageFile63.png>)

p∈E

ℓ≤x p|ℓ =⇒ p∈E

so that

1 m ≥

1 m ≥

1 ℓ m≤x

1 n

1 p ℓ≤x

1 p n≤x

1 −

1 −

,

![image 64](<2012-granville-when-sieve-works_images/imageFile64.png>)

![image 65](<2012-granville-when-sieve-works_images/imageFile65.png>)

![image 66](<2012-granville-when-sieve-works_images/imageFile66.png>)

![image 67](<2012-granville-when-sieve-works_images/imageFile67.png>)

![image 68](<2012-granville-when-sieve-works_images/imageFile68.png>)

![image 69](<2012-granville-when-sieve-works_images/imageFile69.png>)

m≤x p|m =⇒ p∈P

p∈E

p∈E

p|m =⇒ p∈P

p|ℓ =⇒ p∈E

since every integer n ≤ x may be written as ℓm. On the other hand we have the upper bound

−1

−1

1 p

1 p

1 p ∼ eγ log x

1 p

1 n ≤

1 −

,

1 −

1 −

=

1 −

![image 70](<2012-granville-when-sieve-works_images/imageFile70.png>)

![image 71](<2012-granville-when-sieve-works_images/imageFile71.png>)

![image 72](<2012-granville-when-sieve-works_images/imageFile72.png>)

![image 73](<2012-granville-when-sieve-works_images/imageFile73.png>)

![image 74](<2012-granville-when-sieve-works_images/imageFile74.png>)

p≤x

n≤x p|n =⇒ p∈P

p∈E

p∈P

p∈E

by Mertens’ theorem. Remark 2.2. Note that

x

1 n

Ψ(x; P) x

Ψ(t; P) t2

=

+

dt,

![image 75](<2012-granville-when-sieve-works_images/imageFile75.png>)

![image 76](<2012-granville-when-sieve-works_images/imageFile76.png>)

![image 77](<2012-granville-when-sieve-works_images/imageFile77.png>)

- (2.1)


1

n≤x p|n =⇒ p∈P

so that Lemma 2.1 can be re-phrased as a weighted mean of Ψ(t; P)-values:

x

x

1 p

1 p

Ψ(t; P) t ·

dt t

dt t

eγ

1 −

1 −

,

![image 78](<2012-granville-when-sieve-works_images/imageFile78.png>)

![image 79](<2012-granville-when-sieve-works_images/imageFile79.png>)

![image 80](<2012-granville-when-sieve-works_images/imageFile80.png>)

![image 81](<2012-granville-when-sieve-works_images/imageFile81.png>)

![image 82](<2012-granville-when-sieve-works_images/imageFile82.png>)

1

1

p∈E

p∈E

since Ψ(x; P)/x ≪ p∈E 1 − 1p by classical sieve theory (as discussed in the introduction).

![image 83](<2012-granville-when-sieve-works_images/imageFile83.png>)

We can use Lemma 2.1 to prove a ﬁrst lower bound in the direction of Theorem 1, though with a diﬀerent emphasis: We show that as soon as x1/u<p≤x,p∈P

1

p is at least ǫ, there is

![image 84](<2012-granville-when-sieve-works_images/imageFile84.png>)

some t ∈ [x1/u, x] for which Ψ(t; P) is of expected size. Corollary 2.3. Fix ǫ ∈ (0, 1). Suppose that P is a subset of the primes ≤ x, and u ∈ [1, log x] is such that

1 p

> ǫ.

![image 85](<2012-granville-when-sieve-works_images/imageFile85.png>)

p∈P x1/u<p≤x

Then there exists t ∈ [x1/u, x] such that Ψ(t; P) t ≫

ǫmin{1, ǫu} log u p∈E

![image 86](<2012-granville-when-sieve-works_images/imageFile86.png>)

![image 87](<2012-granville-when-sieve-works_images/imageFile87.png>)

- (2.2)


p≤t

1 p

1 −

![image 88](<2012-granville-when-sieve-works_images/imageFile88.png>)

.

Proof. By (2.1)

x

Ψ(t; P) t2

dt ≥

![image 89](<2012-granville-when-sieve-works_images/imageFile89.png>)

x1/u

x1/u≤n≤x p|n =⇒ p∈P

1 n −

1 x ≥

![image 90](<2012-granville-when-sieve-works_images/imageFile90.png>)

![image 91](<2012-granville-when-sieve-works_images/imageFile91.png>)

1 n

- 1

![image 92](<2012-granville-when-sieve-works_images/imageFile92.png>)

- 2


.

![image 93](<2012-granville-when-sieve-works_images/imageFile93.png>)

x1/u≤n≤x/2 p|n =⇒ p∈P

Writing here n = ab, where prime factors of a are ≤ x1/u and prime factors of b are > x1/u, and discarding some n, we see that

x

Ψ(t; P) t2

- 1

![image 94](<2012-granville-when-sieve-works_images/imageFile94.png>)

- 2


dt ≥

![image 95](<2012-granville-when-sieve-works_images/imageFile95.png>)

x1/u

Here

S :=

1<b≤x1−ǫ/2 p|b =⇒ p∈P∩(x1/u,x1−ǫ/2]

hence S ≥ 8ǫ(1 + S) and so

![image 96](<2012-granville-when-sieve-works_images/imageFile96.png>)

x

ǫ 8

Ψ(t; P) t2

dt ≥

![image 97](<2012-granville-when-sieve-works_images/imageFile97.png>)

![image 98](<2012-granville-when-sieve-works_images/imageFile98.png>)

x1/u

1 a

a≤xǫ/2/2 p|a =⇒ p∈P∩[1,x1/u]

1 b

.

![image 99](<2012-granville-when-sieve-works_images/imageFile99.png>)

![image 100](<2012-granville-when-sieve-works_images/imageFile100.png>)

1<b≤x1−ǫ/2 p|b =⇒ p∈P∩(x1/u,x1−ǫ/2]

1 p

1 b ≥

![image 101](<2012-granville-when-sieve-works_images/imageFile101.png>)

![image 102](<2012-granville-when-sieve-works_images/imageFile102.png>)

p∈P x1/u<p≤x1−ǫ/2

ǫ 4

> ǫ + log(1 − ǫ/2) + o(1) ≥

,

![image 103](<2012-granville-when-sieve-works_images/imageFile103.png>)

1 a

a≤xǫ/2/2 p|a =⇒ p∈P∩[1,x1/u]

1 b

.

![image 104](<2012-granville-when-sieve-works_images/imageFile104.png>)

![image 105](<2012-granville-when-sieve-works_images/imageFile105.png>)

b≤x1−ǫ/2 p|b =⇒ p∈P∩(x1/u,x1−ǫ/2]

Consequently, Lemma 2.1 implies that

x

1 p

1 p

Ψ(t; P) t2

1 +

1 +

dt ≫ ǫ

![image 106](<2012-granville-when-sieve-works_images/imageFile106.png>)

![image 107](<2012-granville-when-sieve-works_images/imageFile107.png>)

![image 108](<2012-granville-when-sieve-works_images/imageFile108.png>)

x1/u

p≤xǫ/2 p∈P∩[1,x1/u]

p∈P∩(x1/u,x1−ǫ/2]

1 p ≍ ǫmin{1, ǫu} logx

1 p

≫ ǫmin{1, ǫu}

1 +

1 −

.

![image 109](<2012-granville-when-sieve-works_images/imageFile109.png>)

![image 110](<2012-granville-when-sieve-works_images/imageFile110.png>)

p∈P

p∈E

If now for every t ∈ [x1/u, x] we have that Ψ(t; P) t ≤ η ·

1 p ≪ η ·

ǫmin{1, ǫu} log u

1 p

ǫmin{1, ǫu} log u p∈E

log x log t p∈E

1 −

1 −

,

![image 111](<2012-granville-when-sieve-works_images/imageFile111.png>)

![image 112](<2012-granville-when-sieve-works_images/imageFile112.png>)

![image 113](<2012-granville-when-sieve-works_images/imageFile113.png>)

![image 114](<2012-granville-when-sieve-works_images/imageFile114.png>)

![image 115](<2012-granville-when-sieve-works_images/imageFile115.png>)

![image 116](<2012-granville-when-sieve-works_images/imageFile116.png>)

p≤t

then

x

x

Ψ(t; P) t2 ≪ η ·

dt tlog t

ǫmin{1, ǫu} log u

1 p

log x

1 −

![image 117](<2012-granville-when-sieve-works_images/imageFile117.png>)

![image 118](<2012-granville-when-sieve-works_images/imageFile118.png>)

![image 119](<2012-granville-when-sieve-works_images/imageFile119.png>)

![image 120](<2012-granville-when-sieve-works_images/imageFile120.png>)

x1/u

x1/u

p∈E

1 p

.

≪ η · ǫmin{1, ǫu} log x

1 −

![image 121](<2012-granville-when-sieve-works_images/imageFile121.png>)

p∈E

Choosing η small enough, we arrive at a contradiction. So the claimed result follows.

- Remark 2.4. Let T be the set of t ∈ [x1/u, x] for which (2.2) holds. By the same proof, and the usual sieve upper bound, we obtain t∈T dt/(tlog t) ≫ ǫmin{1, ǫu}


The lower bound (2.2) obtained here is much better than the lower bound in Theorem 1, but it only works for some values of t. One cannot essentially improve Corollary 2.3 in general, at least when 1/ǫ ≪ u ≪

√log x: Take a prime q ≍ (log u)/ǫ and let P be the set of primes which are ≡ 1 (mod q). Then the classical sieve yields

![image 122](<2012-granville-when-sieve-works_images/imageFile122.png>)

Ψ(t, P) t

1 t|{n = qk + 1 ≤ t: p | n =⇒ p  ∈ E \ {q}}|

=

![image 123](<2012-granville-when-sieve-works_images/imageFile123.png>)

![image 124](<2012-granville-when-sieve-works_images/imageFile124.png>)

1 p

1 p ≍

ǫ log u

1 q

1 −

1 −

≪

![image 125](<2012-granville-when-sieve-works_images/imageFile125.png>)

![image 126](<2012-granville-when-sieve-works_images/imageFile126.png>)

![image 127](<2012-granville-when-sieve-works_images/imageFile127.png>)

![image 128](<2012-granville-when-sieve-works_images/imageFile128.png>)

p∈E p≤t

p∈E\{q} p≤(t/q)1/2

for every t ∈ [x1/u, x].

Next, we prove a converse result to Corollary 2.3, but ﬁrst we need an estimate which belongs to the theory of smooth numbers. Its proof is an application of Rankin’s method, together with an additional averaging which recovers a logarithmic loss that occurs in the original version of Rankin’s method. It can be found, for example, in Kevin Ford’s notes [2, Theorem Ψ], though it is possible that it has appeared before in the literature. We give the full proof for completeness.

- Proposition 2.5. Let x ≥ 3 and u ≥ 1 such that u ≤ (1/2 − ǫ) log x/ log log x, for some ﬁxed ǫ ∈ (0, 1/3). If P is a subset of the primes ≤ x1/u, then


eO(u) (u log u)u p∈E

1 p

Ψ(x; P) x ≪ǫ

1 −

.

![image 129](<2012-granville-when-sieve-works_images/imageFile129.png>)

![image 130](<2012-granville-when-sieve-works_images/imageFile130.png>)

![image 131](<2012-granville-when-sieve-works_images/imageFile131.png>)

p≤x

Proof. Without loss of generality, we may assume that u is large enough. Set y = x1/u and note that u ≤ y1/2−ǫ/ log y by our assumption that u ≤ (1/2 − ǫ) log x/ log log x. In particular, we may assume that y is large too.

Our starting point is the identity

- (2.3)

Fix some δ ∈ [1/ log y, 1/2 − ǫ] and note that, for 1 ≤ n ≤ x, log x = log n + log(x/n) ≤ log n +

1 1 − δ ·

![image 132](<2012-granville-when-sieve-works_images/imageFile132.png>)

x1−δ n1−δ ≤ log n +

![image 133](<2012-granville-when-sieve-works_images/imageFile133.png>)

6x1−δ

![image 134](<2012-granville-when-sieve-works_images/imageFile134.png>)

n1−δ . Together with (2.3), this implies that

(log x)Ψ(x; P) ≪

n≤x p|n =⇒ p∈P

x1−δ n1−δ +

![image 135](<2012-granville-when-sieve-works_images/imageFile135.png>)

m≤x p|m =⇒ p∈P

d≤x/m p|d =⇒ p∈P

Λ(d).

- (2.4)

Next, note that

d≤x/m p|d =⇒ p∈P

Λ(d) ≤

p≤min{y,x/m}

(log p)

ν≥1 pν≤x/m

1 ≪

p≤min{y,x/m}

log(x/m),

by our assumption that P ⊂ {p ≤ y}. So, if x/y < m ≤ x, then we ﬁnd that

d≤x/m p|d =⇒ p∈P

Λ(d) ≪

x m ≤

![image 136](<2012-granville-when-sieve-works_images/imageFile136.png>)

yδx1−δ m1−δ ,

![image 137](<2012-granville-when-sieve-works_images/imageFile137.png>)

- (2.5)


log n =

n≤x p|n =⇒ p∈P

m≤x p|m =⇒ p∈P

Λ(d).

d≤x/m p|d =⇒ p∈P

whereas, if 1 ≤ m ≤ x/y, then

yδ(x/m)1−δ log(yδ(x/m)1−δ)

yδx1−δ m1−δ .

y log y

log(x/m) ≪

log(x/m) ≪

Λ(d) ≪

![image 138](<2012-granville-when-sieve-works_images/imageFile138.png>)

![image 139](<2012-granville-when-sieve-works_images/imageFile139.png>)

![image 140](<2012-granville-when-sieve-works_images/imageFile140.png>)

d≤x/m p|d =⇒ p∈P

In any case, the estimate (2.5) does hold. Combining it with (2.4), we deduce that Ψ(x; P) ≪

−1

yδx1−δ log x n≤x

yδx1−δ log x p∈P

1 n1−δ ≤

1 p1−δ

1 −

![image 141](<2012-granville-when-sieve-works_images/imageFile141.png>)

![image 142](<2012-granville-when-sieve-works_images/imageFile142.png>)

![image 143](<2012-granville-when-sieve-works_images/imageFile143.png>)

![image 144](<2012-granville-when-sieve-works_images/imageFile144.png>)

p|n =⇒ p∈P

pδ − 1 p p∈E

1 p

≪ǫ yδx1−δ exp

1 −

,

![image 145](<2012-granville-when-sieve-works_images/imageFile145.png>)

![image 146](<2012-granville-when-sieve-works_images/imageFile146.png>)

p∈P

p≤x

by our assumption that δ ≤ 1/2 − ǫ. Finally, note that

pδ − 1 p ≪

eδlogy δ log y

pδ − 1 p ≤

![image 147](<2012-granville-when-sieve-works_images/imageFile147.png>)

![image 148](<2012-granville-when-sieve-works_images/imageFile148.png>)

![image 149](<2012-granville-when-sieve-works_images/imageFile149.png>)

p≤y

p∈P

by the Brun-Titchmarsch inequality. So writing δ = v/ logy, we arrive to the estimate Ψ(x; P) x ≪

eO(ev/v) euv

.

![image 150](<2012-granville-when-sieve-works_images/imageFile150.png>)

![image 151](<2012-granville-when-sieve-works_images/imageFile151.png>)

We choose v such that ev/v = u. This produces a value of δ in the interval [1/ log y, 1/2− ǫ] as long as u = eδlogy/(δ log y) is in the interval [e, y1/2−ǫ/((1/2 − ǫ) log y)], which does hold. Since v = log u + log log u + O(1), the proposition follows.

Proposition 2.6. Suppose that P is a subset of the primes ≤ x, and u ∈ [1, log x] is such that

1 p

:= κ ≪ 1.

![image 152](<2012-granville-when-sieve-works_images/imageFile152.png>)

p∈P x1/u<p≤x

There exists t ∈ [x1/2, x] such that Ψ(t; P) t ≪ κ + x−1/6 + u−u/4

1 p

1 −

.

![image 153](<2012-granville-when-sieve-works_images/imageFile153.png>)

![image 154](<2012-granville-when-sieve-works_images/imageFile154.png>)

p∈E p≤t

If, in addition, P ⊂ [1, x1−ǫ], then we can take t = x provided we replace κ by κ/ǫ. In either case, if κ = o(1) as u → ∞ and x → ∞, then Ψ(t; P)/t is much smaller than expected.

Proof. First, we show the second claim because its proof is simpler. Note that Ψ(x; P) ≤ Ψ(x; P ∩ [1, x1/u]) +

1.

n≤x p|n =⇒ p∈P

p|n x1/u<p≤x

The ﬁrst sum is ≪ x(u−u + x−1/3) p∈E∩[1,x](1 − 1/p), by Proposition 2.5 applied with min{u, (logx)/(2.5 log log x)} in place of u. The second sum equals

1 p

1 p ≪

κx ǫlog x p∈P

x p log(x/p)

1 +

1 +

,

1 ≪

![image 155](<2012-granville-when-sieve-works_images/imageFile155.png>)

![image 156](<2012-granville-when-sieve-works_images/imageFile156.png>)

![image 157](<2012-granville-when-sieve-works_images/imageFile157.png>)

![image 158](<2012-granville-when-sieve-works_images/imageFile158.png>)

p∈P x1/u<p≤x

p∈P x1/u<p≤x

p∈P∩[1,x/p]

m≤x/p p|m =⇒ p∈P

by our assumption that P ⊂ [1, x1−ǫ]. Therefore Ψ(x; P) x ≪ u−u + x−1/3 + κ/ǫ

1 p

1 −

,

![image 159](<2012-granville-when-sieve-works_images/imageFile159.png>)

![image 160](<2012-granville-when-sieve-works_images/imageFile160.png>)

p∈E p≤x

as claimed.

Finally, we show the ﬁrst part of the proposition. We may assume that u is large enough and u = o(log x). Our starting point is the relation

Ψ(√x; P) √x

x

![image 161](<2012-granville-when-sieve-works_images/imageFile161.png>)

Ψ(t; P) t

1 n

Ψ(x; P) x

dt t

+

=

+

,

![image 162](<2012-granville-when-sieve-works_images/imageFile162.png>)

![image 163](<2012-granville-when-sieve-works_images/imageFile163.png>)

![image 164](<2012-granville-when-sieve-works_images/imageFile164.png>)

![image 165](<2012-granville-when-sieve-works_images/imageFile165.png>)

![image 166](<2012-granville-when-sieve-works_images/imageFile166.png>)

- (2.6)


√x

![image 167](<2012-granville-when-sieve-works_images/imageFile167.png>)

√x<n≤x p|n =⇒ p∈P

![image 168](<2012-granville-when-sieve-works_images/imageFile168.png>)

![image 169](<2012-granville-when-sieve-works_images/imageFile169.png>)

which follows by integration by parts. If we show that each term on the right hand side of

- (2.6) is


1 p

(κ + x−1/6 + u−u/4) log x,

1 −

≪

![image 170](<2012-granville-when-sieve-works_images/imageFile170.png>)

p≤x p∈E

then the claimed result follows, by taking the minimum of Ψ(t; P)/t on the left side of (2.6).

First, we bound the sum over n. Let v = min{u, (log x)/(2.5 log log x)} and set y = x1/v ≥ max{x1/u, (log x)2.5}. Notice that

−1

1 p

1 b ≤

≤ eO(κ) ≪ 1.

1 −

![image 171](<2012-granville-when-sieve-works_images/imageFile171.png>)

![image 172](<2012-granville-when-sieve-works_images/imageFile172.png>)

y<p≤x p∈P

b≥1 p|b =⇒ p∈P∩(y,x]

So, writing n = ab with a having prime factors ≤ y and b having prime factors > y, and adding some extra ab, we see that

1 a ·

1 b

1 b

1 n ≤

1 a b≥1

+

![image 173](<2012-granville-when-sieve-works_images/imageFile173.png>)

![image 174](<2012-granville-when-sieve-works_images/imageFile174.png>)

![image 175](<2012-granville-when-sieve-works_images/imageFile175.png>)

![image 176](<2012-granville-when-sieve-works_images/imageFile176.png>)

![image 177](<2012-granville-when-sieve-works_images/imageFile177.png>)

√x<n≤x p|n =⇒ p∈P

√x<a≤x p|a =⇒ p∈P∩[1,y]

√x p|a =⇒ p∈P∩[1,y]

b>1 p|b =⇒ p∈P∩(y,x]

![image 178](<2012-granville-when-sieve-works_images/imageFile178.png>)

![image 179](<2012-granville-when-sieve-works_images/imageFile179.png>)

![image 180](<2012-granville-when-sieve-works_images/imageFile180.png>)

a≤

p|b =⇒ p∈P∩(y,x]

1 a · eO(κ)

1 a · (eO(κ) − 1) +

≤

![image 181](<2012-granville-when-sieve-works_images/imageFile181.png>)

![image 182](<2012-granville-when-sieve-works_images/imageFile182.png>)

√x<a≤x p|a =⇒ p∈P∩[1,y]

a≥1 p|a =⇒ p∈P∩[1,y]

![image 183](<2012-granville-when-sieve-works_images/imageFile183.png>)

−1

eO(v) (v log v)v/2 p≤x

1 p

1 p

1 −

1 −

+ (log x)

≪ κ

![image 184](<2012-granville-when-sieve-works_images/imageFile184.png>)

![image 185](<2012-granville-when-sieve-works_images/imageFile185.png>)

![image 186](<2012-granville-when-sieve-works_images/imageFile186.png>)

p≤y p∈P

p∈E

1 p

≪ (log x)(κ + x−1/3 + (2u)−u/2)

1 −

- (2.7) ,

by Proposition 2.5 and partial summation. We deduce that

Ψ(x; P) ≤

√x +

![image 187](<2012-granville-when-sieve-works_images/imageFile187.png>)

√x<n≤x p|n =⇒ p∈P

![image 188](<2012-granville-when-sieve-works_images/imageFile188.png>)

x n ≪ x

![image 189](<2012-granville-when-sieve-works_images/imageFile189.png>)

p≤x p∈E

1 −

1 p

![image 190](<2012-granville-when-sieve-works_images/imageFile190.png>)

κ + x−1/3 + (2u)−u/2 log x.

Since (√x1/(u/2), √x] ⊂ (x1/u, x], applying the above relation with x and u replaced by √x and u/2, respectively, we see that

![image 191](<2012-granville-when-sieve-works_images/imageFile191.png>)

![image 192](<2012-granville-when-sieve-works_images/imageFile192.png>)

![image 193](<2012-granville-when-sieve-works_images/imageFile193.png>)

Ψ(√x; P) √x ≪

![image 194](<2012-granville-when-sieve-works_images/imageFile194.png>)

![image 195](<2012-granville-when-sieve-works_images/imageFile195.png>)

![image 196](<2012-granville-when-sieve-works_images/imageFile196.png>)

p≤x p∈E

1 −

1 p

![image 197](<2012-granville-when-sieve-works_images/imageFile197.png>)

κ + x−1/6 + u−u/4 log x.

- (2.8)


![image 198](<2012-granville-when-sieve-works_images/imageFile198.png>)

p≤x p∈E

Inserting relations (2.7) and (2.8) into (2.6) completes the proof of the proposition.

This last estimate is much smaller than one might have guessed given Lemma 2.1. We have now seen that if there are very few large primes in P then one can improve the sieve upper bounds for some values of t. Finally, note that the assumption that P ⊂ [1, x1−ǫ] is essential in the second part of Proposition 2.6. Indeed, if P = {p ≤ xǫ} ∪ {p : x1−ǫ < p ≤ x}, then Ψ(x, P) contains all integers of the form mp where p is a prime in the range x1−ǫ < p ≤ x, and m ≤ x/p. Hence

1 p

x p ≫ ǫx ≍ x

1 −

.

Ψ(x; P) ≥

![image 199](<2012-granville-when-sieve-works_images/imageFile199.png>)

![image 200](<2012-granville-when-sieve-works_images/imageFile200.png>)

x1−ǫ<p≤x

p∈E p≤x

3. Technical reductions

The hypothesis in Theorem 1 relies on there being a reasonable density of “large” primes in P. More generally, we may ask what happens when some interval (x1/ev, x1/u] contains lots of primes of P. Reducing to the analogous problem where P is now restricted to be a subset of the primes in this interval, we formulate

Hypothesis P. There exist constants λ1 > 0 and C1 > 1 such that if v2 ≤ λ1 log x/C1, 1 ≤ u ≤ v and P is a subset of the primes in (x1/ev, x1/u] for which

1 p ≥

1 + λ1 u

- (3.1) ,


![image 201](<2012-granville-when-sieve-works_images/imageFile201.png>)

![image 202](<2012-granville-when-sieve-works_images/imageFile202.png>)

p∈P

then for any δ ∈ [x−1/(3ev), 1/2] there exists an integer k ∈ [u, ev] and an absolute constant πv > 0 such that

k

1 p

δπv log x ·

1 p1 · · ·pk ≥

.

![image 203](<2012-granville-when-sieve-works_images/imageFile203.png>)

![image 204](<2012-granville-when-sieve-works_images/imageFile204.png>)

![image 205](<2012-granville-when-sieve-works_images/imageFile205.png>)

p∈P

(p1,...,pk)∈Pk (1−δ)x<p1···pk<x

- Remark 3.1. In [10] Bleichenbacher’s theorem is used to prove a result like Hypothesis P but with a logarithmic loss (log x)−O(v) in the obtained lower bound — see Theorem 4 and Proposition 10.1 there.


![image 206](<2012-granville-when-sieve-works_images/imageFile206.png>)

Proof that Hypothesis P with πv = v−O(v) implies Theorem 1 with λ = λ1 + ǫ and c = λ1/(2C1). Set η = min{ǫ, 1}/3. Let A = P ∩ [1, x1/ev] and B = P ∩ (x1/ev, x] so that

Ψ(x; P) ≥

Ψ(x/a; B),

a≤xη p|a =⇒ p∈A

since we can write any n composed only of prime factors from P as n = ab where a and b are composed only of prime factors from A and B, respectively. For each a ≤ xη, we have that

1 p ≥

1 p

η 1 − η

+ log(1 − η) + o(1) ≥ 1 + λ1 + ǫ −

+ o(1) > 1 + λ1,

![image 207](<2012-granville-when-sieve-works_images/imageFile207.png>)

![image 208](<2012-granville-when-sieve-works_images/imageFile208.png>)

![image 209](<2012-granville-when-sieve-works_images/imageFile209.png>)

p∈B (x/a)1/ev<p≤x/a

p∈P x1/ev<p≤x

as x → ∞. Applying Hypothesis P with u = 1 and δ = 1/2 to the set B yields Ψ(x/a; B) ≥

x/2a n ≫

1 vO(v) ·

x alog x

![image 210](<2012-granville-when-sieve-works_images/imageFile210.png>)

![image 211](<2012-granville-when-sieve-works_images/imageFile211.png>)

![image 212](<2012-granville-when-sieve-works_images/imageFile212.png>)

x/2a<n≤x/a p|n =⇒ p∈B

and consequently Ψ(x; P) x ≫

1 p ≫

1 a ≫

η vO(v) p∈E

1 vO(v)

η vO(v) p≤x

1 p

1 log x a≤x

1 −

,

1 −

![image 213](<2012-granville-when-sieve-works_images/imageFile213.png>)

![image 214](<2012-granville-when-sieve-works_images/imageFile214.png>)

![image 215](<2012-granville-when-sieve-works_images/imageFile215.png>)

![image 216](<2012-granville-when-sieve-works_images/imageFile216.png>)

![image 217](<2012-granville-when-sieve-works_images/imageFile217.png>)

![image 218](<2012-granville-when-sieve-works_images/imageFile218.png>)

![image 219](<2012-granville-when-sieve-works_images/imageFile219.png>)

![image 220](<2012-granville-when-sieve-works_images/imageFile220.png>)

η

η

p∈E

p|a =⇒ p∈A

by Lemma 2.1, which completes the proof of Theorem 1.

So we have shown that in order to prove Theorem 1 it suﬃces to prove the more convenient Hypothesis P with certain choices of the parameters therein.

4. Equivalent problems in combinatorics

In our sieve question we are seeking to sieve the integers up to x by a given set of primes E which is, as discussed in the introduction, the same thing as counting the number of integers up to x that are composed of primes from a given set P. This makes this a rather special case of sieving an interval, since the problem can now be approached as a question of counting lattice points: If p1 · · ·pk ≤ x, then

log p1 + log p2 + · · · + log pk ≤ log x and there are various techniques for attacking this problem. However they are not really eﬀective, since here we have an enormous dimension compared to the volume of our region, even when restricting the primes in P to an interval [x1/ev, x1/u). We can however cut the dimension of the problem signiﬁcantly by taking approximations that do not greatly eﬀect the answer. For example, if we replace each log p by [log p] and take N to be an integer close to log x, then we can count integer solutions to a1 + a2 + · · · + am ≤ N, and weight each ai by the number of primes p in P for which [log p] = a. However even this problem is of rather high dimension to directly use lattice point counting results, so instead we attack this as a question in combinatorics.

Hypothesis A. There exist constants λ2 > 0 and C2 > 1 such that if v2 ≤ λ2N/C2, 1 ≤ u ≤ v and A is a subset of the integers in (evN , Nu ] such that

![image 221](<2012-granville-when-sieve-works_images/imageFile221.png>)

![image 222](<2012-granville-when-sieve-works_images/imageFile222.png>)

1 a ≥

1 + λ2 u

,

![image 223](<2012-granville-when-sieve-works_images/imageFile223.png>)

![image 224](<2012-granville-when-sieve-works_images/imageFile224.png>)

a∈A

then there exists an integer k ∈ [u, ev], an absolute constant αv > 0 and an integer n ∈ [N − k, N] such that

k

αv N a∈A

1 a

1 a1 · · ·ak ≥

.

![image 225](<2012-granville-when-sieve-works_images/imageFile225.png>)

![image 226](<2012-granville-when-sieve-works_images/imageFile226.png>)

![image 227](<2012-granville-when-sieve-works_images/imageFile227.png>)

(a1,...,ak)∈Ak a1+···+ak=n

- Proposition 4.1. (i) Hypotheses P and A are equivalent, with λ2 ≍ λ1 and αveO(v) ≫ πv ≫ αv min{1, λv1}v−O(v).


We will prove this at the end of this section. We ﬁrst note reasons for some of the conditions in Hypothesis A:

- • If A is the set of integers in (N/(k+1), N/k−1) then there are no sums of elements of

A in the interval [N −k, N] and n∈A 1/n ∼ log(1+1/k) = 1/k+O(1/k2). Hence we must have λ2 ≥ 0. However, we do believe that Hypothesis A holds for any λ2 > 0.

- • If A is the set of integers ≡ 0 (mod d) in (evN , Nv ], then a∈A 1/a ∼ 1/d as N → ∞, and there are no solutions to a1 + · · · + ak = n for any n in an interval md < n < (m + 1)d. Hence n must be chosen from an interval of length ≥ d. This explains the length of the interval for n in Hypothesis A.


![image 228](<2012-granville-when-sieve-works_images/imageFile228.png>)

![image 229](<2012-granville-when-sieve-works_images/imageFile229.png>)

We will eventually prove Hypothesis A with αv = 1/vO(v) and big enough constant λ2. By Proposition 4.1(i), this yields Hypothesis P with πv = 1/vO(v), and therefore Theorem 1 as was shown in Section 3.

Since Hypothesis A involves so many integers, one might think to approximate the set of integers A by a continuous variable; for instance, by considering very short intervals around each a/N, so as to obtain Hypothesis T (which is stated in the introduction):

- Proposition 4.1. (ii) Hypotheses A and T are equivalent, with λ2 ≍ λ3 and τveO(v) ≫ αv ≫ τv/eO(v).


Combining this with Proposition 4.1(i) and the result from Section 3, we can deduce Proposition 1. Proof of Proposition 4.1. We conclude this section with the proof that our three hypotheses, A, P and T, are equivalent. Proof that Hypothesis A implies Hypothesis T. Assume that T is an open subset of (1/ev, 1/u)

such that T dt/t ≥ (1 + λ3)/u. An open subset of the reals is a union of disjoint open intervals, and the number of intervals in the union is countable (as may be seen by labelling

each interval with some rational it contains). Hence we may write T = i≥1(αi, βi). But then there exists an integer m such that if S = mi=1(αi, βi), then t∈S dt/t ≥ (1 + 2λ3/3)/u. By replacing T in our assumption by S and λ3 by 2λ3/3, we may assume that T is a ﬁnite union of open intervals. We select N to be much larger than maxi{v/|αi −βi|}, mv3/λ3 and mv4. Let

m

A =

{a ∈ Z : αiN + 2ev < a < βiN − 2ev}.

i=1

Since t (=aa/N+1)/N dt/t = 1/a + O(1/a2), we deduce that

mv3 N t∈T

mv2 N

1 a

1 + λ3/2 u

dt t ≥

dt t

= 1 + O

=

+ O

.

![image 230](<2012-granville-when-sieve-works_images/imageFile230.png>)

![image 231](<2012-granville-when-sieve-works_images/imageFile231.png>)

![image 232](<2012-granville-when-sieve-works_images/imageFile232.png>)

![image 233](<2012-granville-when-sieve-works_images/imageFile233.png>)

![image 234](<2012-granville-when-sieve-works_images/imageFile234.png>)

![image 235](<2012-granville-when-sieve-works_images/imageFile235.png>)

t∈T

a∈A

Now, if λ3 ≥ 2λ2, then Hypothesis A implies that there exists an integer k ∈ [u, ev] and an integer n ∈ [N − k, N] such that

k

k

αve−O(k) N t∈T

dt t

αv N a∈A

1 a

1 a1 · · ·ak ≥

≥

.

![image 236](<2012-granville-when-sieve-works_images/imageFile236.png>)

![image 237](<2012-granville-when-sieve-works_images/imageFile237.png>)

![image 238](<2012-granville-when-sieve-works_images/imageFile238.png>)

![image 239](<2012-granville-when-sieve-works_images/imageFile239.png>)

![image 240](<2012-granville-when-sieve-works_images/imageFile240.png>)

(a1,...,ak)∈Ak a1+···+ak=n

For each k-tuple (a1, . . ., ak) ∈ Ak with a1+· · ·+ak = n, consider ti ∈ (ai/N, (ai+1)/N) ⊂ T for 1 ≤ i ≤ k − 1 and deﬁne tk = 1 − (t1 + · · · + tk−1). Then we have that

k−1

N − n N

2ev N and consequently tk ∈ T. Hence

2k − 1 N ≤

ai N − ti ≤

ak N

=

+

tk −

![image 241](<2012-granville-when-sieve-works_images/imageFile241.png>)

![image 242](<2012-granville-when-sieve-works_images/imageFile242.png>)

![image 243](<2012-granville-when-sieve-works_images/imageFile243.png>)

![image 244](<2012-granville-when-sieve-works_images/imageFile244.png>)

![image 245](<2012-granville-when-sieve-works_images/imageFile245.png>)

i=1

dt1dt2 · · ·dtk−1 t1t2 · · ·tk ≫

dt1 · · ·dtk−1 t1 · · ·tk−1

N ak ai/N<ti<(ai+1)/N

. . .

![image 246](<2012-granville-when-sieve-works_images/imageFile246.png>)

![image 247](<2012-granville-when-sieve-works_images/imageFile247.png>)

![image 248](<2012-granville-when-sieve-works_images/imageFile248.png>)

t1+t2+···+tk=1 t1,t2,...,tk∈T

(a1,...,ak)∈Ak a1+···+ak=n

1≤i≤k−1

k

αv eO(v) t∈T

dt t

N a1 · · ·ak ≥

1 eO(k)

,

≫

![image 249](<2012-granville-when-sieve-works_images/imageFile249.png>)

![image 250](<2012-granville-when-sieve-works_images/imageFile250.png>)

![image 251](<2012-granville-when-sieve-works_images/imageFile251.png>)

![image 252](<2012-granville-when-sieve-works_images/imageFile252.png>)

(a1,...,ak)∈Ak a1+···+ak=n

as desired. Hence we can take λ3 = 3λ2 and τv ≫ αve−O(v).

Proof that Hypothesis T implies Hypothesis A. Let N ≥ C2v2/λ2 and A ⊂ (N/ev, N/u] with a∈A 1/a ≥ (1 + λ2)/u. Set T = a∈A(a/N, (a + 1)/N), so that

v2 N a∈A

dt t

1 a ≥

1 a

1 + λ2/2 u

1 N/v

= 1 + O

=

+ O

,

![image 253](<2012-granville-when-sieve-works_images/imageFile253.png>)

![image 254](<2012-granville-when-sieve-works_images/imageFile254.png>)

![image 255](<2012-granville-when-sieve-works_images/imageFile255.png>)

![image 256](<2012-granville-when-sieve-works_images/imageFile256.png>)

![image 257](<2012-granville-when-sieve-works_images/imageFile257.png>)

![image 258](<2012-granville-when-sieve-works_images/imageFile258.png>)

T

a∈A

provided that C2 is large enough. If t1 + t2 + · · · + tk = 1 and ai = [Nti], then N − k ≤

- a1 + · · · + ak ≤ N. Now, we have that 1


dt1dt2 · · ·dtk−1 t1t2 · · ·tk−1 · (Ntk)

a1 · · ·ak ≥ · · ·

,

![image 259](<2012-granville-when-sieve-works_images/imageFile259.png>)

![image 260](<2012-granville-when-sieve-works_images/imageFile260.png>)

ai/N<ti<(ai+1)/N ∀i

and so

k

dt t

τv N t∈T

1 a1 · · ·ak ≥ · · · t1+t2+···+tk=1

dt1dt2 · · ·dtk−1 Nt1t2 · · ·tk ≫

,

![image 261](<2012-granville-when-sieve-works_images/imageFile261.png>)

![image 262](<2012-granville-when-sieve-works_images/imageFile262.png>)

![image 263](<2012-granville-when-sieve-works_images/imageFile263.png>)

![image 264](<2012-granville-when-sieve-works_images/imageFile264.png>)

t1,t2,...,tk∈T

(a1,...,ak)∈Ak N−k≤a1+···+ak≤N

provided that λ2 ≥ 2λ3. The result follows by averaging over the subsums with a1+· · ·+ak = n for each integer n in the interval N − k ≤ n ≤ N. Hence we can take λ2 = 2λ3 and αv ≫ τv/eO(v).

Proof that Hypothesis P implies Hypothesis A. Given our set A, let P be the set of primes in a∈A(ea, ea+1), and let x = e[N]+1. Then

v2 N a∈A

1 p

1 a ≥

1 a

1 + λ2/2 u

1 N/v

= 1 + O

=

+ O

,

![image 265](<2012-granville-when-sieve-works_images/imageFile265.png>)

![image 266](<2012-granville-when-sieve-works_images/imageFile266.png>)

![image 267](<2012-granville-when-sieve-works_images/imageFile267.png>)

![image 268](<2012-granville-when-sieve-works_images/imageFile268.png>)

![image 269](<2012-granville-when-sieve-works_images/imageFile269.png>)

![image 270](<2012-granville-when-sieve-works_images/imageFile270.png>)

p∈P

a∈A

provided that C2 is large enough. So, if we choose λ2 = 2λ1, then we can apply Hypothesis P. Now for each k-tuple of primes (p1, . . ., pk) ∈ Pk such that x/2 < p1 · · ·pk < x, let aj = [log pj] for all j, so that

k

k

aj >

(log pj − 1) ≥ log(x/2) − k = [N] + 1 − log 2 − k

j=1

j=1

and

k

aj ≤

j=1

k

log pj < log x = [N] + 1.

j=1

Since aj are integers, this implies that N − k ≤ kj=1 aj ≤ N. Hence, noticing that 1/a ∼ ea≤p≤ea+1 1/p, we deduce that

1 p1 · · ·pk

1 a1 · · ·ak ≫ e−O(k)

![image 271](<2012-granville-when-sieve-works_images/imageFile271.png>)

![image 272](<2012-granville-when-sieve-works_images/imageFile272.png>)

(p1,...,pk)∈Pk x/2<p1···pk<x

(a1,...,ak)∈Ak N−k≤a1+···+ak≤N

k

k

e−O(k)πv log x ·

1 p

1 N a∈A

πv eO(k) ·

1 a

≫

≫

.

![image 273](<2012-granville-when-sieve-works_images/imageFile273.png>)

![image 274](<2012-granville-when-sieve-works_images/imageFile274.png>)

![image 275](<2012-granville-when-sieve-works_images/imageFile275.png>)

![image 276](<2012-granville-when-sieve-works_images/imageFile276.png>)

![image 277](<2012-granville-when-sieve-works_images/imageFile277.png>)

p∈P

Hence we can take λ2 = 2λ1 and αv ≫ πve−O(v).

Proof that Hypothesis A implies Hypothesis P. Let ρ = 1+δ/(2ev), η = min{1, λ2} and N = logρ x − ev. For each integer a ∈ [N/ev + 1, N/u] deﬁne

1 p

Sa =

.

![image 278](<2012-granville-when-sieve-works_images/imageFile278.png>)

p∈P ρa≤p<ρa+1

Huxley’s prime number theorem for short intervals (see Theorem 10.5 in [8] and the subsequent discussion) yields |{y ≤ p ≤ y + h}| ∼ h/ log y for y7/12+ǫ ≤ h ≤ y. This implies that

1 + η/10 a ≪

δ log x when C1, and thus x1/ev, is large enough.

v N ≍

- (4.1)


Sa ≤

![image 279](<2012-granville-when-sieve-works_images/imageFile279.png>)

![image 280](<2012-granville-when-sieve-works_images/imageFile280.png>)

![image 281](<2012-granville-when-sieve-works_images/imageFile281.png>)

Let A be the set of integers a for which Sa ≥ 4alog(η ev) p∈P

1

p. Then

![image 282](<2012-granville-when-sieve-works_images/imageFile282.png>)

![image 283](<2012-granville-when-sieve-works_images/imageFile283.png>)

1 p

η 4alog(ev) p∈P

1 p ≤

δ log x

η 4

δv log x p∈P

1 p ≤ O

+

+ O

![image 284](<2012-granville-when-sieve-works_images/imageFile284.png>)

![image 285](<2012-granville-when-sieve-works_images/imageFile285.png>)

![image 286](<2012-granville-when-sieve-works_images/imageFile286.png>)

![image 287](<2012-granville-when-sieve-works_images/imageFile287.png>)

![image 288](<2012-granville-when-sieve-works_images/imageFile288.png>)

![image 289](<2012-granville-when-sieve-works_images/imageFile289.png>)

![image 290](<2012-granville-when-sieve-works_images/imageFile290.png>)

p∈P [logρ p] ∈A

a ∈A

N ev +1≤a≤Nu

![image 291](<2012-granville-when-sieve-works_images/imageFile291.png>)

![image 292](<2012-granville-when-sieve-works_images/imageFile292.png>)

1 p

η 3 p∈P

≤

,

![image 293](<2012-granville-when-sieve-works_images/imageFile293.png>)

![image 294](<2012-granville-when-sieve-works_images/imageFile294.png>)

provided that C1 is large enough and λ1 ≤ 100λ2. Using (4.1) we ﬁnd that

1 p

1 p ≥ 1 −

η 10 p∈P

η 10 a∈A

η 2 p∈P

1 a ≥ 1 −

Sa = 1 −

.

![image 295](<2012-granville-when-sieve-works_images/imageFile295.png>)

![image 296](<2012-granville-when-sieve-works_images/imageFile296.png>)

![image 297](<2012-granville-when-sieve-works_images/imageFile297.png>)

![image 298](<2012-granville-when-sieve-works_images/imageFile298.png>)

![image 299](<2012-granville-when-sieve-works_images/imageFile299.png>)

![image 300](<2012-granville-when-sieve-works_images/imageFile300.png>)

a∈A

[logρ p]∈A

So setting λ1 = 4λ2 allows us to apply Hypothesis A. Now for each solution to a1+· · ·+ak = n ∈ [N − k, N] with a1, . . ., ak ∈ A, consider the primes pj ∈ P with [logρ pj] = aj. Note that aj ≤ logρ pj < aj + 1 and so logρ x − ev − k ≤ n ≤ logρ(p1p2 · · ·pk) < n + k ≤ logρ x, which implies that x > p1 · · ·pk > xρ−2ev = x(1 + δ/(2ev))−2ev ≥ (1 − δ)x. Hence

1 p1 · · ·pk ≥

Sa

1 · · ·Sa

![image 301](<2012-granville-when-sieve-works_images/imageFile301.png>)

k

(p1,...,pk)∈Pk (1−δ)x<p1···pk<x

(a1,...,ak)∈Ak a1+···+ak=n

k

1 p

1 a1 · · ·ak

η 4 log(ev) p∈P

≥

![image 302](<2012-granville-when-sieve-works_images/imageFile302.png>)

![image 303](<2012-granville-when-sieve-works_images/imageFile303.png>)

![image 304](<2012-granville-when-sieve-works_images/imageFile304.png>)

(a1,...,ak)∈Ak a1+···+ak=n

k

k

k

ηvαv vO(v) ·

1 p

δ log x p∈P

αv N a∈A

1 a

η(1 + λ1) 4u log(ev)

≫

,

·

≥

![image 305](<2012-granville-when-sieve-works_images/imageFile305.png>)

![image 306](<2012-granville-when-sieve-works_images/imageFile306.png>)

![image 307](<2012-granville-when-sieve-works_images/imageFile307.png>)

![image 308](<2012-granville-when-sieve-works_images/imageFile308.png>)

![image 309](<2012-granville-when-sieve-works_images/imageFile309.png>)

![image 310](<2012-granville-when-sieve-works_images/imageFile310.png>)

which proves the desired result.

5. Lemmas in additive combinatorics

Let us ﬁrst introduce some notation. Given two additive sets A and B, deﬁne the sum set A + B = {a + b : a ∈ A, b ∈ B}, the k-fold sum set kA = {a1 + · · · + ak : ai ∈ A}, and for

any E ⊆ A × B deﬁne the restricted sum set

A+EB = {a + b : (a, b) ∈ E}. Write also

rkA(n) = #{(a1, . . ., ak) ∈ Ak : a1 + · · · + ak = n} for the number of representations. Finally, a set of the form

P = {x0 + l1x1 + · · · + ldxd : 0 ≤ lj ≤ Lj for all j} is called a generalized arithmetic progression of rank d.

We need three lemmas from additive combinatorics. The ﬁrst one lets us pass from a restricted sum set to a regular sum set.

- Lemma 5.1. Let (G, +) be an abelian group. If E ⊆ A × A satisﬁes

|E| ≥ (1 − δ2)|A|2 and |A+EA| ≤ K|A|, then there exists a set A′ ⊆ A such that

|A′| ≥ (1 − δ)|A| and |A′ − A′| ≤

K2 1 − 2δ|A|.

![image 311](<2012-granville-when-sieve-works_images/imageFile311.png>)

Proof. This is a variant of the Balog-Szemer´edi-Gowers theorem (see [12, Theorem 2.29]) which can be proved by incorporating the hint for [12, Exercise 2.5.4] to the proof of the Balog-Szemer´edi-Gowers theorem in [12, Section 6.4]. We provide a proof for completeness.

Choose

A′ = {a ∈ A | (a, b) ∈ E for at least (1 − δ)|A| of b ∈ A}. Now

(1 − δ2)|A|2 ≤ |E| ≤ |A′||A| + (|A| − |A′|)(1 − δ)|A| =⇒ |A′| ≥ (1 − δ)|A|.

Fix a pair (a1, a2) ∈ A′ × A′ and note that (a1, b) ∈ E for at least (1 − δ)|A| of b ∈ A and (a2, b) ∈ E for at least (1 − δ)|A| of b ∈ A. Hence there are at least (1 − 2δ)|A| elements b ∈ A for which both (a1, b) ∈ E and (a2, b) ∈ E. Since a1 − a2 = (a1 + b) − (a2 + b), writing x = a1 + b and y = a2 + b, we have

|{(x, y) ∈ (A+EA)2 | x − y = a1 − a2}| ≥ (1 − 2δ)|A|.

Since the total number of triples (x, y) ∈ (A+EA)2 is at most K2|A|2, the claim follows by summing over elements of A′ − A′.

The second lemma shows that if 3A is small, then we can ﬁnd a popular large generalized arithmetic progression inside it.

- Lemma 5.2. Let K ≥ 1 and let A be a ﬁnite subset of the integers such that |3A| ≤ K|A|. Then there is a generalized arithmetic progression P ⊆ 3A of rank OK(1) such that |P| ≫K |A| and r3A(n) ≫K |A|2 for all n ∈ P.


Proof. This is a variant of the Ruzsa-Chang theorem (see [12, Theorem 5.30]). Similarly to that theorem, this can be reduced to the following similar result in ZN := Z/NZ through theory of Freiman morphisms.

- Lemma 5.2*. Let K, N ≥ 1 with 3 ∤ N, δ > 0 and let A be a ﬁnite subset of ZN such that |3A| ≤ K|A| and |A| ≥ δN. Then there is a generalized arithmetic progression P ⊆ 3A of rank OK,δ(1) such that |P| ≫K,δ |A| and r3A(n) ≫K,δ |A|2 for all n ∈ P.

Proof. This is a consequence of [12, Theorem 4.43], except we have added the requirement r3A(n) ≫K |A|2 for all n ∈ P which the proof easily gives. For completeness we sketch the proof.

Let us consider r3A(n) = 1A ∗ 1A ∗ 1A(n). One has x∈Z

N

r3A(x) = |A|3 whereas r3A is supported on the set 3A of cardinality at most K|A|. Hence there is x0 such that r3A(x0) ≥

- |A|2/K. By translating A by x0/3, we can assume x0 = 0.


Now, writing g(k) = x∈Z

N

g(x)e(−kxN ) for the Fourier transform,

![image 312](<2012-granville-when-sieve-works_images/imageFile312.png>)

|r3A(x) − r3A(0)| =

1 N ξ∈Z

![image 313](<2012-granville-when-sieve-works_images/imageFile313.png>)

N

1A(ξ)3(e(ξxN ) − 1)

![image 314](<2012-granville-when-sieve-works_images/imageFile314.png>)

≤ sup

ξ∈ZN

| 1A(ξ)||(e(ξxN ) − 1)| ·

![image 315](<2012-granville-when-sieve-works_images/imageFile315.png>)

1 N ξ∈Z

![image 316](<2012-granville-when-sieve-works_images/imageFile316.png>)

N

| 1A(ξ)|2 ≤ 2π|A| sup

ξ∈ZN

| 1A(ξ)|

ξx N

![image 317](<2012-granville-when-sieve-works_images/imageFile317.png>)

,

by Parseval’s identity and where we write y for the distance from the nearest integer. Hence r3A(x) ≥ |A|2/(2K) for every x in the set

x ∈ ZN : sup

ξ∈ZN

| 1A(ξ)|

ξx N

![image 318](<2012-granville-when-sieve-works_images/imageFile318.png>)

< |A| 4πK ⊇

![image 319](<2012-granville-when-sieve-works_images/imageFile319.png>)

 



x ∈ ZN : sup

ξ∈ZN | 1A(ξ)|≥|A|/(4πK)

ξx N

![image 320](<2012-granville-when-sieve-works_images/imageFile320.png>)

<

1 4πK

![image 321](<2012-granville-when-sieve-works_images/imageFile321.png>)

 



.

By the Fourier concentration lemma [12, Lemma 4.36], there is d = OK,δ(1) and a set S = {η1, . . ., ηd} ⊂ ZN such that

{ξ ∈ ZN : | 1A(ξ)| ≥ |A|/(4πK)} ⊆

d

j=1

αjηj : αj ∈ {−1, 0, 1} ,

and hence by the triangle inequality r3A(x) ≥ |A|2/(2K) for every x in the set x ∈ ZN : sup

ξ∈S

ξx N

![image 322](<2012-granville-when-sieve-works_images/imageFile322.png>)

<

1 4πdK

![image 323](<2012-granville-when-sieve-works_images/imageFile323.png>)

.

This is a so-called Bohr set which contains the claimed arithmetic progression by [12, Proposition 4.23], the proof of which uses Minskowski’s second theorem.

The third lemma shows that sum sets of generalized arithmetic progressions have large popular subsets.

- Lemma 5.3. Let Lj be positive integers for j = 1, . . ., d and let P = {x0 + l1x1 + · · · + ldxd : |lj| ≤ Lj for all j}


be a generalized arithmetic progression. Let k ∈ N, δ ∈ (0, 1/6d), ρ = 1 − 3δ1/d ≥ 1/2 and

Qk = {kx0 + l1x1 + · · · + ldxd : |lj| ≤ ρkLj for all j}. Then, for any n ∈ Qk, one has rkP(n) ≥ (δ|P|)k−1.

Proof. We proceed by induction on k. The case k = 1 is trivial, so we assume that the claim holds for some k ∈ N. Let n ∈ Qk+1, so that n = (k + 1)x0 + l1x1 + · · · + ldxd with |lj| ≤ ρ(k + 1)Lj for all j. Now

r(k+1)P(n) =

rkP(kx0 + (l1 − i1)x1 + · · · + (ld − id)xd)

|ij|≤Lj ∀j

≥ (δ|P|)k−1 · #{(i1, . . ., id) : |ij| ≤ Lj and |lj − ij| ≤ ρkLj for all j}.

The right hand side is smallest when lj = [ρ(k + 1)Lj] for all j ∈ {1, . . ., d}, in which case

#{ij ∈ [−Lj, Lj] : |lj − ij| ≤ ρkLj}

= #{ij : [ρ(k + 1)Lj] − ρkLj ≤ ij ≤ min{Lj, [ρ(k + 1)Lj] + ρkLj}}.

Since 2ρk ≥ 2ρ ≥ 1, the minimum above is Lj and hence the number of counted ij is at least (1 − ρ)Lj. Hence, since |P| ≤ dj=1(2Lj + 1) ≤ dj=1(3Lj), we have that

r(k+1)P(n) ≥ (δ|P|)k−1(1 − ρ)d

d

Lj = (δ|P|)k−1δ

j=1

d

(3Lj) ≥ (δ|P|)k.

j=1

6. The proof of Hypothesis A

Our additive combinatorial tools do not involve logarithmic weights, so instead of Hypothesis A we apply them to prove the following variant. Theorem 6.1. There exists a constant c0 > 1 such that if 1 ≤ u ≤ v and B is a subset of the integers in (evN , Nu ] for which

![image 324](<2012-granville-when-sieve-works_images/imageFile324.png>)

![image 325](<2012-granville-when-sieve-works_images/imageFile325.png>)

c0N u2

,

|B| >

![image 326](<2012-granville-when-sieve-works_images/imageFile326.png>)

then there is an integer k ∈ [u, ev] such that

|B|k N

1 eO(k)kk

|{(b1, . . ., bk) ∈ Bk : N − k ≤ b1 + · · · + bk ≤ N}| ≫

.

![image 327](<2012-granville-when-sieve-works_images/imageFile327.png>)

![image 328](<2012-granville-when-sieve-works_images/imageFile328.png>)

Proof that Theorem 6.1 implies Hypothesis A with λ2 = 2c0 − 1 and αv = v−4v. Let A ⊂ [N/(ev), N/u] as in Hypothesis A. We claim that there must exist t ∈ [u, ev] such that

c0N t2

. (6.1)

1 ≥

![image 329](<2012-granville-when-sieve-works_images/imageFile329.png>)

a∈A N/(ev)<a≤N/t

Indeed, if this is not the case, then

  

ev

1 a

t N

= −

d

![image 330](<2012-granville-when-sieve-works_images/imageFile330.png>)

![image 331](<2012-granville-when-sieve-works_images/imageFile331.png>)

u

a∈A N/(ev)<a≤N/u

a∈A N/(ev)<a≤N/t

  

ev

u N

1 +

=

![image 332](<2012-granville-when-sieve-works_images/imageFile332.png>)

u

a∈A N/(ev)<a≤N/u

ev

u N ·

1 t2

c0N u2

<

+ c0

dt < 2 ·

![image 333](<2012-granville-when-sieve-works_images/imageFile333.png>)

![image 334](<2012-granville-when-sieve-works_images/imageFile334.png>)

![image 335](<2012-granville-when-sieve-works_images/imageFile335.png>)

u

  

1

  

dt N

1

![image 336](<2012-granville-when-sieve-works_images/imageFile336.png>)

a∈A N/(ev)<a≤N/t

c0 u

1 + λ2 u

=

![image 337](<2012-granville-when-sieve-works_images/imageFile337.png>)

![image 338](<2012-granville-when-sieve-works_images/imageFile338.png>)

which is a contradiction. So there is some t ∈ [u, ev] for which (6.1) holds.

Now, set B = A ∩ (N/(ev), N/t], so that the hypothesis of Theorem 6.1 is satisﬁed with t in place of u. Let k be as in the conclusion of Theorem 6.1, which necessarily lies in [u, ev]. Let n be an integer in [N −k, N] whose number of representations as b1+· · ·+bk is maximal. So n has at least ≫ e−O(k)k−k|B|k/N such representations by Theorem 6.1. Since each b ∈ B satisﬁes 1/b ≥ u/N ≥ 1/N, and as |B| ≥ c0N/t2 ≥ c0N/(ev)2, we deduce that

k

k

e−O(v) v3v · N ≥

e−O(1)|B| Nk

αv N a∈A

1 a

1 N

1 b1 · · ·bk ≫

≫

![image 339](<2012-granville-when-sieve-works_images/imageFile339.png>)

![image 340](<2012-granville-when-sieve-works_images/imageFile340.png>)

![image 341](<2012-granville-when-sieve-works_images/imageFile341.png>)

![image 342](<2012-granville-when-sieve-works_images/imageFile342.png>)

![image 343](<2012-granville-when-sieve-works_images/imageFile343.png>)

![image 344](<2012-granville-when-sieve-works_images/imageFile344.png>)

(b1,...,bk)∈Bk b1+···+bk=n

with αv ≫ v−4v, since a∈A a1 ≪ log(ev).

![image 345](<2012-granville-when-sieve-works_images/imageFile345.png>)

Proof of Theorem 6.1. Let c0 be a large positive constant to be determined later. Notice ﬁrst that if |B| ≤ c0, then we only need to ﬁnd one sum in the interval [N − k, N]. In this case the elements of B have size ≤ N/u ≤ u by the lower bound for |B|, so the claim follows trivially.

From now on we can assume that |B| > c0. We claim that if |B| > c0N/u2, then there exists k such that

δ2k|B|k Nkk

|{(b1, . . ., bk) ∈ Bk : N − k ≤ b1 + · · · + bk ≤ N}| ≥ c

![image 346](<2012-granville-when-sieve-works_images/imageFile346.png>)

for some appropriate small positive constants c and δ. If 1 ≤ u ≤ c0, our claim is trivial, since there are no sets B ⊂ (N/ev, N/u] with |B| > c0N/u2.

Now we prove that if the claim holds when 2j−1c0 ≤ u ≤ 2jc0 for some j ≥ 0, then it holds when 2jc0 ≤ u ≤ 2j+1c0. Take

E = (b1, b2) ∈ B × B : r2B(b1 + b2) ≥ δ2 |B|2 |2B|

, so that

![image 347](<2012-granville-when-sieve-works_images/imageFile347.png>)

|E| ≥ |B|2 − |2B| · δ2 |B|2 |2B|

= (1 − δ2)|B|2.

![image 348](<2012-granville-when-sieve-works_images/imageFile348.png>)

Write C = B+EB ⊆ (2N/(ev), 2N/u]. We split the rest of the argument into two cases according to whether |C| > 4|B| or not.

Consider ﬁrst the case |C| > 4|B|. Then

c0N (u/2)2

|C| >

,

![image 349](<2012-granville-when-sieve-works_images/imageFile349.png>)

and by induction hypothesis there is an integer k/2 ∈ [u/2, ev/2] such that

δk|C|k/2 N(k/2)k/2

|{(c1, . . ., ck/2) ∈ Ck/2 : N − k/2 ≤ c1 + · · · + ck/2 ≤ N}| ≥ c

.

![image 350](<2012-granville-when-sieve-works_images/imageFile350.png>)

Hence by the deﬁnition of C we have |{(b1, . . ., bk) ∈ Bk : N − k/2 ≤ b1 + · · · + bk ≤ N}| ≥ c

k/2

k/2

δk|C|k/2 N(k/2)k/2 · δ2 |B|2 |2B|

δ2k|B|k Nkk/2 ·

2|C| |2B|

= c

.

![image 351](<2012-granville-when-sieve-works_images/imageFile351.png>)

![image 352](<2012-granville-when-sieve-works_images/imageFile352.png>)

![image 353](<2012-granville-when-sieve-works_images/imageFile353.png>)

![image 354](<2012-granville-when-sieve-works_images/imageFile354.png>)

The claim now follows if |C| > |2B|/2k; this easily follows, since |C| > 4|B| and |2B| ≤ 2N/u ≤ 2|B|u/c0 ≤ 2|B|k.

On the other hand, if |C| ≤ 4|B|, then by Lemma 5.1 there is B′ ⊆ B such that |B′| ≥

- |B|/2 and |B′ − B′| ≤ 20|B′|. Then by [12, Proposition 2.26] we have |3B′| ≪ |B′| and hence Lemma 5.2 implies that there is a generalized arithmetic progression P ⊆ 3B′ ⊆ 3B


of rank d ≪ 1 such that |P| ≫ |B| and r3B(n) ≫ |B|2 for all n ∈ P. “Centralizing” P we can assume that it is of form

P = {x0 + l1x1 + · · · + ldxd : |lj| ≤ Lj for all j}

for some positive integers Lj (doing this reduces the size of P at most by a factor of 1/3d ≫ 1). Set ρ = 1 − (3δ)1/d and

Q = {x0 + l1x1 + · · · + ldxd : |lj| ≤ ρLj for all j} ⊂ P.

If δ < 1/(6d), then Lemma 5.3 implies that rkP(n) ≥ (δ|P|)k−1 for all k ≥ 1 and n ∈ kQ. Moreover, if δ is small enough, then |Q| ≥ |P|/3d ≫ |B| > c0N/u2, so that if c0 is large enough, then |Q| ≥ 15N/u2 and, because

Q ⊆ P ⊆ 3B ⊆ (3N/(ev), 3N/u], we have

15N u2 ·

u 3N ≥

5 u

1 q ≥

.

![image 355](<2012-granville-when-sieve-works_images/imageFile355.png>)

![image 356](<2012-granville-when-sieve-works_images/imageFile356.png>)

![image 357](<2012-granville-when-sieve-works_images/imageFile357.png>)

![image 358](<2012-granville-when-sieve-works_images/imageFile358.png>)

q∈Q

From here we argue much as in the proof of Proposition 4.1(ii). We begin by removing [3N/u] from Q if it is an element so that Q ⊆ (3N/(ev), 3N/u−1]. Let T = q∈Q N q , qN+1 ⊆ (ev3 , u3), so that

![image 359](<2012-granville-when-sieve-works_images/imageFile359.png>)

![image 360](<2012-granville-when-sieve-works_images/imageFile360.png>)

![image 361](<2012-granville-when-sieve-works_images/imageFile361.png>)

![image 362](<2012-granville-when-sieve-works_images/imageFile362.png>)

dt t ≥

1 q

1 q ≥

1 q ≥

- 2

![image 363](<2012-granville-when-sieve-works_images/imageFile363.png>)

- 3 q∈Q


3 u

1 −

![image 364](<2012-granville-when-sieve-works_images/imageFile364.png>)

![image 365](<2012-granville-when-sieve-works_images/imageFile365.png>)

![image 366](<2012-granville-when-sieve-works_images/imageFile366.png>)

![image 367](<2012-granville-when-sieve-works_images/imageFile367.png>)

![image 368](<2012-granville-when-sieve-works_images/imageFile368.png>)

T

q∈Q

since q ≥ 3 for every q ∈ Q ⊆ 3B. Hence, Bleichenbacher’s theorem implies that there exists an integer k/3 ∈ [u/3, ev/3] and t1, . . ., tk/3 ∈ T for which t1+. . .+tk/3 = 1. If ti ∈ q

N , q

i+1 N

i

![image 369](<2012-granville-when-sieve-works_images/imageFile369.png>)

![image 370](<2012-granville-when-sieve-works_images/imageFile370.png>)

for each i then n := q1 + . . . + qk/3 ∈ k3Q ∩ [N − k/3, N]. Recalling that r3B(m) ≫ |B|2 for every m ∈ P and rk

![image 371](<2012-granville-when-sieve-works_images/imageFile371.png>)

3P(ℓ) ≥ (δ|P|)k/3−1 for every ℓ ∈ k3Q, we get that

![image 372](<2012-granville-when-sieve-works_images/imageFile372.png>)

![image 373](<2012-granville-when-sieve-works_images/imageFile373.png>)

#{(b1, . . ., bk) ∈ Bk : N − k/3 ≤ b1 + · · · + bk ≤ N} ≥ #{(b1, . . ., bk) ∈ Bk : b1 + · · · + bk = n}

k/3

3·P(n) · (e−O(1)|B|2)k/3 ≥ (δ|P|)k/3−1 · e−O(k)|B|2k/3

r3B(mj) ≥ rk

≥

![image 374](<2012-granville-when-sieve-works_images/imageFile374.png>)

m1+...+mk/3=n m1,...,mk/3∈P

j=1

≥ e−O(k)(δ|B|)k−1 ≥ ue−O(k)(δ|B|)k/N,

as P ⊆ 3B. The result follows, since the right hand side is ≫ e−O(k)|B|k/N for every ﬁxed δ > 0.

Remark 6.2. One could compute the constant c0 explicitly and thereby the constants λi in Hypotheses P, A and T and, eventually, λ in Theorem 1. However, c0 will be relatively large, since the implied constants in Lemma 5.2 are rather large. If one is interested in optimizing λ, one could, instead of Lemma 5.2, use a result of Lev [11] to show that if the number of “popular” elements in |2A| is at most K|A| for some K < (3 + √5)/2, then 2A contains a “popular” arithmetic progression (of rank 1). Modifying the above arguments, this would lead to Theorem 1 with a smaller and more easily calculable λ < 21. However, this argument would not yield Hypotheses P, A and T when u is not close to 1 and, in particular, not the latter conclusion in Remark 1.4. By applying Bleichenbacher’s theorem in a diﬀerent way one could probably improve λ further, but not to an arbitrarily small constant, as desired.

![image 375](<2012-granville-when-sieve-works_images/imageFile375.png>)

7. Some combinatorial lemmas

We devote this section to proving some combinatorial lemmas we will need in next section where we investigate some further consequences of Hypotheses A, P and T.

Lemma 7.1. Let B be a ﬁnite subset of the numbers in (y, z] and associate to each b ∈ B a positive weight w(b). For any x ≥ z there exists a positive integer k ≤ x/y such that

1 x/y b∈B

w(b1)w(b2) · · ·w(bk) ≥

w(b)

![image 376](<2012-granville-when-sieve-works_images/imageFile376.png>)

b1,...,bk∈B b1+···+bk∈(x−z,x]

k

.

In particular, letting w(b) = 1 for all b ∈ B yields: Let B be a ﬁnite subset of the numbers in (y, z]. For any x ≥ z there exists a positive integer k such that the number of k-tuples b1, . . ., bk ∈ B for which b1 + · · · + bk ∈ (x − z, x] is ≥ |B|k/(x/y).

Proof. Note that if b1+· · ·+bk ∈ (x−z, x] for some b1, . . ., bk ∈ B, then ky < b1+· · ·+bk ≤ x and so 1 ≤ k < x/y. Therefore if we let K = [x/y], then

k

w(b1)w(b2) · · ·w(bk)

βk :=

b1,...,bk∈B b1+···+bk∈(x−z,x]

w(b1)w(b2) · · ·w(bK)

=

b1,...,bK∈B b1+···+bk∈(x−z,x]

Consequently, we ﬁnd that

w(b)

b∈B

w(b)

b∈B

K

.

K

βk =

k=1

w(b)

b∈B

−K

w(b1)w(b2) · · ·w(bK)

1 ≥ 1,

b1,...,bK∈B

1≤k≤K b1+···+bk∈(x−z,x]

since the diﬀerences in each sequence b1, b1+b2, . . ., b1+· · ·+bK are ≤ z, whereas b1 ≤ z ≤ x and b1 + · · · + bK > yK > x − y > x − z. Taking the maximum of the βk then yields the desired result.

- Corollary 7.2. Let P be a subset of the primes in (x1/ev, x1/u] for some 1 ≤ u ≤ v ≤ (log x)/e. For any X ≥ x1/u there exists a positive integer ℓ ≤ K := evloglogxX such that


![image 377](<2012-granville-when-sieve-works_images/imageFile377.png>)

1 q

1 K q∈P

1 q1q2 · · ·qℓ ≥

![image 378](<2012-granville-when-sieve-works_images/imageFile378.png>)

![image 379](<2012-granville-when-sieve-works_images/imageFile379.png>)

![image 380](<2012-granville-when-sieve-works_images/imageFile380.png>)

q1,...,qℓ∈P Xx−1/u<q1q2···qℓ≤X

ℓ

.

Proof. Apply Lemma 7.1 with B = {log q : q ∈ P} ⊂ ((1/ev) log x, (1/u) logx] and w(b) = e−b = 1/q, and then take ℓ = k as obtained in that lemma.

8. Further remarks on Hypotheses P, A and T

We conclude our paper with an investigation of some other consequences of Hypotheses P,A and T. Proposition 8.1. Suppose Hypothesis P holds with πv = 1/vO(v). If ǫ > 0, v2 ≤ λ1 log x/C1,

- v ≥ 1 and P is a subset of the primes in (x1/ev, x1/v] for which σ := p∈P p1 ≥ 1+λ

![image 381](<2012-granville-when-sieve-works_images/imageFile381.png>)

1+ǫ

![image 382](<2012-granville-when-sieve-works_images/imageFile382.png>)

v , then there exists an integer k ∈ [v, ev] such that

Ψ(x; P) ≫ǫ

x log x ·

![image 383](<2012-granville-when-sieve-works_images/imageFile383.png>)

σk+O(1/σ) k · k!

![image 384](<2012-granville-when-sieve-works_images/imageFile384.png>)

.

Proof. We can clearly assume that ǫ is small. Also, since Ψ(x; P) ≥ 1, we may assume that x is large. If v < 2 or 1+λ

1

![image 385](<2012-granville-when-sieve-works_images/imageFile385.png>)

v−1 > σ ≥ 1+λ

1+ǫ

![image 386](<2012-granville-when-sieve-works_images/imageFile386.png>)

v , then v < max{2, 1+λ

1+ǫ

![image 387](<2012-granville-when-sieve-works_images/imageFile387.png>)

ǫ } = 1+λ

1+ǫ

![image 388](<2012-granville-when-sieve-works_images/imageFile388.png>)

ǫ and the proposition follows by Hypothesis P. So we may impose the additional assumptions that

- v ≥ 2 and σ ≥ 1+λ


v−1 .

1

![image 389](<2012-granville-when-sieve-works_images/imageFile389.png>)

Select w = (1 + λ1)/σ and note that w ∈ [1, v − 1], since σ ≤ x1/(ev)<p≤x1/v 1/p 1. We begin by applying Corollary 7.2 with X = x1−

w

v ≥ x1/v. So there is ℓ ≪ v such that

![image 390](<2012-granville-when-sieve-works_images/imageFile390.png>)

σℓ v

1 q1q2 · · ·qℓ ≫

.

![image 391](<2012-granville-when-sieve-works_images/imageFile391.png>)

![image 392](<2012-granville-when-sieve-works_images/imageFile392.png>)

q1,...,qℓ∈P x1−

w+1

v <q1q2···qℓ≤x1−wv

![image 393](<2012-granville-when-sieve-works_images/imageFile393.png>)

![image 394](<2012-granville-when-sieve-works_images/imageFile394.png>)

For each q1 · · ·qℓ in the above sum we apply Hypothesis P with x replaced by x/(q1 · · ·qℓ), and both u and v replaced by V = log(x/(q1 · · ·qℓ))/ log(x1/v), which is possible since V ∈ [w, w + 1]. Consequently,

Finally, note that

σℓ+m wO(w)v log x

1 q1 · · ·qℓp1 · · ·pm ≫

.

![image 395](<2012-granville-when-sieve-works_images/imageFile395.png>)

![image 396](<2012-granville-when-sieve-works_images/imageFile396.png>)

(q1,...,qℓ,p1,...,pm)∈Pℓ+m x/2<q1···qℓp1···pm<x

1 (ℓ + m)!

1

Ψ(x; P) ≥

![image 397](<2012-granville-when-sieve-works_images/imageFile397.png>)

(q1,...,qℓ,p1,...,pm)∈Pℓ+m q1···qℓp1···pm≤x

x 2(ℓ + m)!

1 q1 · · ·qℓp1 · · ·pm

≥

![image 398](<2012-granville-when-sieve-works_images/imageFile398.png>)

![image 399](<2012-granville-when-sieve-works_images/imageFile399.png>)

(q1,...,qℓ,p1,...,pm)∈Pℓ+m x/2<q1···qℓp1···pm<x

σℓ+m wO(w)v(ℓ + m)!

x log x ·

.

≫

![image 400](<2012-granville-when-sieve-works_images/imageFile400.png>)

![image 401](<2012-granville-when-sieve-works_images/imageFile401.png>)

Letting k = ℓ + m and observing that, necessarily, k ∈ [v, ev] and w log w ≪ σ−1 log(1/σ) completes the proof of the proposition.

- Corollary 8.2. There exist constants c > 1 and c′ > 0 such that if 1 ≤ v ≤ c′√log x and P is a subset of the primes in (x1/ev, x1/v] for which


![image 402](<2012-granville-when-sieve-works_images/imageFile402.png>)

1 p ≥

max{c, log v} v

,

![image 403](<2012-granville-when-sieve-works_images/imageFile403.png>)

![image 404](<2012-granville-when-sieve-works_images/imageFile404.png>)

p∈P

then there exists an integer k ∈ [v, ev] such that

k

1 p

x log x

1 k!

e−O(1)

,

·

Ψ(x; P) ≥ Ψk(x; P) ≥

![image 405](<2012-granville-when-sieve-works_images/imageFile405.png>)

![image 406](<2012-granville-when-sieve-works_images/imageFile406.png>)

![image 407](<2012-granville-when-sieve-works_images/imageFile407.png>)

p∈P

as x → ∞, where Ψk(x; P) denotes the number of integers n ≤ x such that n is squarefree, n has exactly k prime factors, and all of the prime factors of n come from P.

We conjecture that Corollary 8.2 holds under the weaker assumption that p∈P p1 ≥ c/v for any c > 1, with the implied constant depending at most on c.

![image 408](<2012-granville-when-sieve-works_images/imageFile408.png>)

Consider more generally Ψk(x, P) for any P ⊂ {p ≤ x}. If n ∈ (√x, x] is counted by Ψk(x; P), then we can uniquely write n = mp with p prime and m composed of primes < p. Note that pk ≥ n ≥

![image 409](<2012-granville-when-sieve-works_images/imageFile409.png>)

√x. So m has k − 1 prime factors and it is ≤ x1−1/(2k). Now for each m

![image 410](<2012-granville-when-sieve-works_images/imageFile410.png>)

the number of such primes p is (x/m)/ log(x/m) as x → ∞, and therefore

k−1

µ2(m) m ≤

Ψk(x; P) √x +

√x +

1 p

x log x

2kx log x p|m =⇒ p∈P

2k (k − 1)! p∈P

![image 411](<2012-granville-when-sieve-works_images/imageFile411.png>)

![image 412](<2012-granville-when-sieve-works_images/imageFile412.png>)

,

·

![image 413](<2012-granville-when-sieve-works_images/imageFile413.png>)

![image 414](<2012-granville-when-sieve-works_images/imageFile414.png>)

![image 415](<2012-granville-when-sieve-works_images/imageFile415.png>)

![image 416](<2012-granville-when-sieve-works_images/imageFile416.png>)

![image 417](<2012-granville-when-sieve-works_images/imageFile417.png>)

ω(m)=k−1

as x → ∞. In particular one cannot signiﬁcantly improve the lower bound in Corollary 8.2.

It is not diﬃcult to prove corollaries of Hypotheses A and T that are analogous to Proposition 8.1. Thus we have

- Proposition 8.3. Suppose that Hypothesis A holds for some λ2 > 0 and C2 > 1 with αv = 1/vO(v). If ǫ > 0, v2 ≤ λ2N/C2, v ≥ 1 and A is a subset of the integers in (evN , Nv ] such

![image 418](<2012-granville-when-sieve-works_images/imageFile418.png>)

![image 419](<2012-granville-when-sieve-works_images/imageFile419.png>)

that α := a∈A 1/a ≥ (1 + λ2 + ǫ)/v, then there exists an integer k ∈ [v, ev], and an integer n in the range N − k ≤ n ≤ N, such that

(a1,...,ak)∈Ak a1+···+ak=n

1 a1 · · ·ak ≫ǫ

![image 420](<2012-granville-when-sieve-works_images/imageFile420.png>)

1 N ·

![image 421](<2012-granville-when-sieve-works_images/imageFile421.png>)

αk+O(1/α) k

![image 422](<2012-granville-when-sieve-works_images/imageFile422.png>)

.

Similarly, we have the following result.

- Proposition 8.4. Suppose that Hypothesis T holds for some λ3 > 0 with τv = 1/vO(v). If


ǫ > 0, v ≥ 1 and T is an open subset of (ev1 , 1v] for which τ := t∈T dt/t ≥ (1 + λ3 + ǫ)/v, then there exists an integer k ∈ [v, ev] such that

![image 423](<2012-granville-when-sieve-works_images/imageFile423.png>)

![image 424](<2012-granville-when-sieve-works_images/imageFile424.png>)

τk+O(1/τ) k

dt1dt2 · · ·dtk−1 t1t2 · · ·tk ≫ǫ

.

. . .

![image 425](<2012-granville-when-sieve-works_images/imageFile425.png>)

![image 426](<2012-granville-when-sieve-works_images/imageFile426.png>)

t1+t2+···+tk=1 t1,t2,...,tk∈T

In the proofs of Propositions 8.3 and 8.4 we need appropriate analogues to Corollary 7.2. The needed result for the proof of Proposition 8.3 follows in a straightforward way from

- Lemma 7.1. For the proof of Proposition 8.4 we make note, without proof, of the appropriate result:
- Lemma 8.5. Let T be an open subset of (ev1 , u1]. For any w ≥ 1/v there exists a positive integer ℓ ≤ evw such that


![image 427](<2012-granville-when-sieve-works_images/imageFile427.png>)

![image 428](<2012-granville-when-sieve-works_images/imageFile428.png>)

ℓ

dt t

1 evw t∈T

dt1dt2 · · ·dtℓ t1t2 · · ·tℓ ≥

.

. . .

![image 429](<2012-granville-when-sieve-works_images/imageFile429.png>)

![image 430](<2012-granville-when-sieve-works_images/imageFile430.png>)

![image 431](<2012-granville-when-sieve-works_images/imageFile431.png>)

w−1/v<t1+t2+···+tℓ≤w t1,t2,...,tℓ∈T

References

- [1] D. Bleichenbacher, The continuous postage stamp problem. Unpublished manuscript, 2003.
- [2] K. Ford, Sieve methods class notes, part 4. Available at http://www.math.uiuc.edu/~ford/Sieve_methods_notes_part4.pdf.
- [3] J. B. Friedlander, Integers free from large and small primes. Proc. London Math. Soc., Vol. 33, pp 565–576, 1976.
- [4] J. B. Friedlander and H. Iwaniec, Opera de Cribro. (American Mathematical Society Colloqium Publications), Vol. 57, American Mathematical Society, Providence, RI, 2010.
- [5] A. Granville and K. Soundararajan, The number of unsieved integers up to x. Acta Arith., Vol. 115, 2004, pp. 305–328.
- [6] R.R. Hall, Halving an estimate obtained from Selberg’s upper bound method. Acta Arith., Vol. 25, 1974, pp. 347–351.
- [7] A. Hildebrand, Quantitative mean value theorems for nonnegative multiplicative functions II. Acta Arith., Vol. 48, 1987, pp. 209–260.


- [8] H. Iwaniec and E. Kowalski, Analytic Number Theory. (American Mathematical Society Colloqium Publications), Vol. 53, American Mathematical Society, Providence, RI, 2004.
- [9] K. Matoma¨ki, Real zeros of holomorphic Hecke cusp forms and sieving short intervals. Preprint available at http://users.utu.fi/ksmato/papers/RealZerosCuspForms.pdf.
- [10] H. W. Lenstra jr. and C. Pomerance, Primality testing with Gaussian periods. To appear. Preprint available at http://www.math.dartmouth.edu/~carlp/aks041411.pdf.
- [11] V. F. Lev, Restricted set addition in groups. III. Integer sumsets with generic restrictions. Period. Math. Hungar., Vol. 42, 2001, 89–98.
- [12] T. Tao and V. H. Vu, Additive combinatorics, (Cambridge Studies in Advanced Mathematics), Vol. 105, Cambridge University Press, 2006.


D´epartement de math´ematiques et de statistique, Universit´e de Montr´eal, CP 6128 succ.

Centre-Ville, Montr´eal, QC H3C 3J7, Canada E-mail address: andrew@dms.umontreal.ca D´epartement de math´ematiques et de statistique, Universit´e de Montr´eal, CP 6128 succ.

Centre-Ville, Montr´eal, QC H3C 3J7, Canada E-mail address: koukoulo@dms.umontreal.ca Department of Mathematics, University of Turku, 20014 Turku, Finland E-mail address: ksmato@utu.fi

