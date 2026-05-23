---
type: source
kind: paper
title: Sharp endpoint extension inequalities for the moment curve on finite fields
authors: Chandan Biswas, Emanuel Carneiro, Taryn C. Flock, Diogo Oliveira e Silva, Betsy Stovall, James Tautges
year: 2025
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2508.08377v1
source_local: ../raw/2025-biswas-sharp-endpoint-extension-inequalities.pdf
topic: general-knowledge
cites:
---

# arXiv:2508.08377v1[math.CA]11Aug2025

## SHARP ENDPOINT EXTENSION INEQUALITIES FOR THE MOMENT CURVE ON FINITE FIELDS

CHANDAN BISWAS, EMANUEL CARNEIRO, TARYN C. FLOCK, DIOGO OLIVEIRA E SILVA, BETSY STOVALL, AND JAMES TAUTGES

Abstract. We investigate the sharp endpoint extension inequality for the moment curve in finite fields. We determine the optimal constant and characterize the maximizers in two complementary regimes: (i) low dimensions d ≤ 20; (ii) large field cardinality q ≥ d2(dlog−1)6 + (2d−1)

3 . Our proof strategy relies on an intriguing interplay between analysis, algebra and combinatorics.

1. Introduction

1.1. Background. The moment curve {γ(t) := (t,t2,...,td) : t ∈ R} ⊂ Rd is a simple object with a large group of symmetries whose Fourier restriction problem was solved forty years ago: Drury [5] showed that the adjoint restriction, or extension, operator to the moment curve,

eix·γ(t)f(t)dt,

Ef(x) :=

R

2 and s = d(d2+1)r′, in all dimensions d ≥ 2. For every exponent pair (r,s) in this range, Biswas–Stovall [1] established the existence of maximizers, i.e., non-zero functions f for which ∥Ef∥s = ∥E∥r→s∥f∥r. However, the nature of these functions remains elusive, as it is not even clear what the candidates should be. For the state of the art in sharp restriction theory in Rd, we refer to the recent surveys [6, 16].

2+d+2

extends to a bounded linear operator from Lr(R) to Ls(Rd) if and only if s > d

The extension problem on finite fields was first considered in 2002 by Mockenhaupt–Tao [14], who established several extension inequalities on paraboloids and cones. Interestingly, they also provided a complete solution to the finite field extension problem for the moment curve Γ := {γ(ξ) = (ξ,ξ2,...,ξd), ξ ∈ Fq}, whenever the characteristic of the field Fq is strictly larger than d. More precisely, the authors of [14] showed that the operator norm RΓ∗(r → s) in the inequality

∥(fσΓ)∨∥Ls(Fdq,dx) ≤ RΓ∗(r → s)∥f∥Lr(Γ,dσ) can be bounded independently of the underlying field Fq if and only if s ≥ max{2d,dr′}. The crucial step turns out to be the endpoint estimate corresponding to RΓ∗(2 → 2d). The measures dx in the physical space and dσ along the curve Γ in the frequency space will be properly defined in §1.2 below.

2020 Mathematics Subject Classification. 42B10, 12E20, 05C70, 05B25, 26D15, 05E05. Key words and phrases. Sharp restriction theory, finite fields, moment curve, maximizers, Muirhead’s inequality, weighted graphs, fractional matching.

1

Sharp restriction theory and the finite field extension problem have received a great deal of attention in the last two decades, but they intersected only very recently: Gonz´lez-Riquelme and Oliveira e Silva [7] proved that constant functions maximize the extension inequality from the parabola P1 ⊂ F2q∗ and the paraboloid P2 ⊂ F3q∗ at the correspondent euclidean Stein–Tomas endpoints, and identified gaussians as the full set of maximizers for the L2 → L4 extension inequality from P2 whenever q is congruent to 1 modulo 4. They established further results on cones and hyperbolic paraboloids (i.e., saddles), but the higher codimensional case remained uncharted territory. On the other hand, (non-sharp) estimates for averaging operators for a few model cases, including the moment curve, have been considered in finite fields [4].

In the present paper, we establish the first sharp endpoint extension inequalities for the moment curve on finite fields.

The moment curve has featured prominently in other problems in analysis and number theory. One of the major advances in analytic number theory in the last decade has been the resolution by Bourgain, Demeter and Guth [3] of the general case of Vinogradov’s mean value conjecture, a key statement in the theory of Waring’s problem. This is implied by the sharp ℓ2 decoupling inequality for the moment curve, whose proof uses a multilinear variant of the decoupling inequality, which in turn crucially relies on multilinear Kakeya–Brascamp–Lieb type inequalities; see [8] for a short proof, which instead uses a bilinear variant of the decoupling inequality. Moment curves have also been used in applications to discrete geometry, e.g., cyclic polytopes [12, Lemma 5.4.2], the no-threein-line problem (credited to P. Erd¨s by K. Roth in [18]), and a geometric proof of the chromatic number of Kneser graphs [13, Section 3.5].

- 1.2. Setup. We generally follow the notation of Mockenhaupt–Tao [14] for the Fourier restriction/extension theory over finite fields. Throughout the text, we let p be an odd prime and let q = pn for some n ∈ N. We also let Fq denote the finite field with q elements.


Let us recall the basic definitions for Fourier analysis on the d-dimensional vector space Fdq. We denote by Fdq∗ the dual of Fdq. The spaces Fdq and Fdq∗ are isomorphic, but their underlying natural measures are different. We endow the physical space Fdq with the counting measure dx and the frequency space Fdq∗ with the normalized counting measure dξ so that Fdq∗ has total mass 1, i.e.,

1 qd

f(x)dx :=

f(x) and

g(ξ)dξ :=

g(ξ).

Fdq

Fdq∗

x∈Fdq

ξ∈Fdq∗

Given a function f : Fdq → C, its Fourier transform f : Fdq∗ → C is defined as f(ξ) :=

f(x)e(−x · ξ)dx =

f(x)e(−x · ξ),

Fdq

x∈Fdq

where e(y) := exp(2πiTr(y)/p) and the trace function Tr : Fq → Fp is defined by Tr(y) := y + yp + yp

2

n−1

+ ... + yp

. Here, as usual, x · ξ := di=1 xiξi if x = (x1,...,xd) and ξ = (ξ1,...,ξd). Given

g : Fdq∗ → C, its inverse Fourier transform g∨ : Fdq → C is defined as g∨(x) :=

1 qd

g(ξ)e(x · ξ)dξ =

g(ξ)e(x · ξ).

Fdq∗

ξ∈Fdq∗

With this setup, we have Plancherel’s identity

∥f∥L2(Fdq,dx) = ∥ f∥L2(Fdq∗,dξ) , and Fourier inversion reads

f(x) = ( f)∨(x) for each x ∈ Fdq. The Fourier transform interchanges convolution and multiplication by f1 f2 = f1 ∗ f2 and f1f2 = f1 ∗ f2.

Note here that convolution in Fdq is defined with respect to the counting measure dx, whereas convolution in Fdq∗ is defined with respect to the normalized counting measure dξ.

Given d ≥ 2, let γ : Fq → Fdq∗ be given by γ(ξ) = (ξ,ξ2,...,ξd), and Γ = {γ(ξ) : ξ ∈ Fq} ⊂ Fdq∗ be the moment curve . Let σ = σΓ be the normalized counting measure supported on Γ. Henceforth we assume the characteristic p of the underlying field to be strictly greater than the dimension d. Given f : Γ → C, the extension operator (fσ)∨ : Fdq → C is defined by

1 q ξ∈Γ

(fσ)∨(x) :=

f(ξ)e(x · ξ). (1.1)

We seek to find the sharp endpoint inequality

∥(fσ)∨∥L2d(Fdq,dx) ≤ RΓ∗(2 → 2d)∥f∥L2(Γ,dσ) , (1.2) identifying the optimal constant RΓ∗(2 → 2d) and its maximizers.

- 1.3. Main results. Our main results are closely related to certain combinatorial entities involving the classical problem of integer partitions. Let


Pd := {ℓ = (ℓ1,ℓ2,...,ℓd) ∈ Zd : ℓ1 ≥ ℓ2 ≥ ... ≥ ℓd ≥ 0 and ℓ1 + ℓ2 + ... + ℓd = d} denote the set of partitions of the integer d ≥ 2. For each ℓ ∈ Pd, let

b(ℓ) := (b0(ℓ),b1(ℓ),b2(ℓ),...,bd(ℓ)),

where bj(ℓ) := |{1 ≤ i ≤ d : ℓi = j}| for j ∈ {1,2,...,d} and b0(ℓ) is slightly different1, given by b0(ℓ) := |{1 ≤ i ≤ d : ℓi = 0}| + (q − d). Note that b(ℓ) is a (d + 1)-dimensional vector. We adopt the multinomial notation

d! ℓ1!ℓ2! ... ℓd!

q! b0(ℓ)!b1(ℓ)!b2(ℓ)! ... bd(ℓ)!

d ℓ

q b(ℓ)

:=

and

:=

.

- 1This is just a minor choice of notation: had we defined ℓd+1 = ℓd+2 = . . . = ℓq = 0, then b0 would be counting the number of zeros in this extended sequence. We opted to write our partitions as d-dimensional vectors in order to avoid an additional block of (q − d) zeros at the end.


We start by formulating the following conjecture. Conjecture 1. Let p > d. With notations as above, the inequality

- 1

- 2d


2 q

1 qd ℓ∈P

d ℓ

∥(fσ)∨∥L2d(Fdq,dx) ≤

∥f∥L2(Γ,dσ) (1.3)

b(ℓ)

d

holds and is sharp. Moreover, f is a maximizer of (1.3) if and only if |f| is constant.

We make progress towards this conjecture in two complementary directions, namely, in low dimensions d and in the regime of large field cardinality q. Our two main results are as follows.

- Theorem 2. Conjecture 1 holds for 2 ≤ d ≤ 20.
- Theorem 3. Conjecture 1 holds whenever


d(d − 1) 2log 6

(2d − 1) 3

+

q ≥

.

Remark: The case d = 2 of Theorem 2 has already been settled in the recent M.Sc. thesis of P. Ronda [17] under the supervision of the fourth author.

The strategy to prove these results relies on an interesting interplay between analysis, algebra and combinatorics, and can be divided into the following five main steps.

- Step 1. Counting solutions. The convolution structure of the problem allows for a reformulation in which one needs to understand the size of the preimage for each point in the support of the d-fold convolution of the normalized counting measure supported on the moment curve.
- Step 2. Symmetric sums and Muirhead’s inequality. The proposed inequality can then be rephrased as an inequality in terms of symmetric sums, with explicit but somewhat complicated weights. At this point, Muirhead’s inequality [15] emerges as the natural tool to be used.
- Step 3. Fractional matching. In order to appropriately use Muirhead’s inequality, one needs to verify a finite number of conditions in the spirit of a fractional matching version of Hall’s marriage theorem for bipartite graphs. The suitable result for our purposes is known as Strassen’s theorem [19].
- Step 4. Computational part. At this point we have reduced the problem to a finite, but potentially large, number of verifications for each given d and q. The case of large q is taken care of by Step 5. We run our algorithm to verify the remaining conditions in low dimensions and conclude the proof of Theorem 2. A subtle issue here is that, when d grows and q is close to d, the number of conditions to be verified grows rapidly; see §3.1.
- Step 5. Asymptotic methods. In arbitrary dimensions, an adequate lower bound on q allows for the use of asymptotic methods to show that we are placed in a favourable situation to use Muirhead’s inequality directly. This is the idea for the proof of Theorem 3.


We regard the conceptual part of this general strategy, and in particular the reduction of the original problem to a finite number of checks, as the main contribution of the paper. The implementation

of the computational part which, in particular, yields Conjecture 1 in low dimensions (d ≤ 20), is primarily intended as a proof of concept. Additional computational power will likely lead to the resolution of Conjecture 1 beyond d = 20.

2. Proofs

In order to simplify the notation, we will usually drop the star from the frequency space Fdq∗, and let C := RΓ∗(2 → 2d).

- 2.1. Counting solutions. We first observe that the extension inequality (1.2) is equivalent to the combinatorial inequality


2

≤ C2d 

 

d

d

|f(ξ)|2

f(ξi)

. (2.1)



i=1

ξ∈Γ

ζ∈Fdq ξ1+...+ξd=ζ ξi∈Γ

In fact, this is a specialization of [7, Proposition 2.1] to our situation and, for the convenience of the reader, we briefly reproduce the proof here. Using the definition (1.1), expanding the product, and reversing the order of summation, we get

2d

1 q2d

1 qd

∗ d

(fσ)∨(x) 2d =

f(ξ)e(x · ξ)

=

f(ξi)f(ηi),

i=1

x∈Fdq ξ∈Γ

x∈Fdq

∗

where the sum

runs over d-tuples (ξi)di=1,(ηi)di=1 ∈ Γd such that di=1 ξi = di=1 ηi. Note the use of the orthogonality relation

d

d

ηi = 0 (2.2)

e x ·

ξi −

i=1

i=1

x∈Fdq

unless di=1 ξi − di=1 ηi = 0, in which case the left-hand side of (2.2) equals qd. Finally, in order to arrive at (2.1), we note that

2

∗ d

d

f(ξi)f(ηi) =

f(ξi)

.

i=1

i=1

ζ∈Fdq ξ1+...+ξd=ζ ξi∈Γ

Let ζ = (ζ1,...,ζd) ∈ Fdq. Our next order of business is to count the number of solutions of

ξ1 + ... + ξd = ζ

with each ξi ∈ Γ. Writing ξi = (ti,t2i,...,tdi ), and taking into account permutations, this amounts to counting the number of solutions to the system

t1 + t2 + ... + td = ζ1 t21 + t22 + ... + t2d = ζ2 . td1 + td2 + ... + tdd = ζd.

(2.3)

Then each of the sums sk := i

is completely determined as a function of ζ = (ζ1,...,ζd), and conversely, by Newton’s power sum formulas [20, p. 81]. One sees that the set {t1,t2,...,td} must coincide with the set of roots of the polynomial

1<i2<...<ik ti

ti

...ti

1

2

k

Pζ(X) := Xd − s1Xd−1 + s2Xd−2 − s3Xd−3 + ... + (−1)dsd.

Therefore, the system (2.3) admits solutions if and only if the polynomial Pζ(X) factors completely over Fq. Moreover, if Pζ(X) factors as

Pζ(X) = (X − r1)ℓ1(X − r2)ℓ2

...(X − rk)ℓk

,

with r1,r2,...,rk ∈ Fq being distinct roots, respectively of multiplicity ℓ1 ≥ ℓ2 ≥ ... ≥ ℓk, we must count the number of ways to associate the ti’s to the rj’s. From the total of d available ti’s we can

- choose ℓ1 to be r1 in ℓ d

1

ways. After this choice, from the remaining (d − ℓ1) available ti’s we can

- choose ℓ2 to be r2 in d−ℓ1


ℓ2 ways, and so on. The total number of possibilities is then

d − ℓ1 ℓ2

d − ℓ1 − ℓ2 ℓ3

d − ℓ1 − ℓ2 − ... − ℓk−1 ℓk

d ℓ1

d ℓ

=

...

.

We can summarize this fact as follows. Let ℓ = (ℓ1,ℓ2,...,ℓd) ∈ Pd, and let Wℓ ⊂ Fdq be the set of ζ ∈ Fdq such that the polynomial Pζ(X) factors completely over Fq, having roots of multiplicity ℓ1 ≥ ℓ2 ≥ ... ≥ ℓd (notice that a potential string of zeros at the end of the partition is harmless). Then, if ζ ∈ Wℓ, the system (2.3) admits dℓ solutions.2

Our next order of business is to understand the cardinality of each set Wℓ. For this, recall that we defined bj(ℓ) := |{1 ≤ i ≤ d : ℓi = j}| for j ∈ {1,2,...,d}, and b0(ℓ) := |{1 ≤ i ≤ d : ℓi = 0}|+(q−d). Assume that ℓ1 ≥ ℓ2 ≥ ... ≥ ℓk ≥ 1 and ℓk+1 = ... = ℓd = 0. In this case, b0(ℓ) = q−k.

- 2This can be equivalently rewritten as σ∗d(ζ) = dℓ , where the d-fold convolution σ∗d is defined as


1 ,

δ(ζ − ξ1 − ξ2 − . . . − ξd) dσ(ξ1) dσ(ξ2) . . . dσ(ξd) =

σ∗d(ζ) :=

Γd

ξ1+...+ξd=ζ ξi∈Γ

and δ denotes the normalized Dirac delta in Fdq∗ (i.e., δ(0) = qd and δ(ξ) = 0 if ξ ̸= 0). Note that σ∗d may take as many values as the distinct values of ℓ!, and this large number of possibilities is generally regarded as an obstacle when investigating the sharp inequality. To put this in perspective, note that the corresponding k-fold convolutions of the corresponding measures for the paraboloids and cones studied in [7] take only two non-zero values in general (or three in one very particular instance).

We want to count the number of polynomials P ∈ Fq[X] of degree d that factor completely as

k

P(X) =

(X − ri)ℓi

.

i=1

We have q possibilities for root r1, then (q − 1) possibilities for root r2, and so on, up to (q − k + 1) possibilities for the root rk. We must, however, divide by b1(ℓ)!b2(ℓ)!...bd(ℓ)! to discount for permutations of roots that have the same multiplicity (after all, they yield the same polynomial). This leads us to conclude that

q(q − 1)...(q − k + 1) b1(ℓ)!b2(ℓ)!...bd(ℓ)!

q! b0(ℓ)!b1(ℓ)!b2(ℓ)!...bd(ℓ)!

q b(ℓ)

|Wℓ| =

=

=

. (2.4)

Note that in the sum on the left-hand side of (2.1) we only have to consider the points ζ that belong to the support of the d-fold convolution σ∗d, i.e. ζ ∈ ∪ℓ∈Pd

Wℓ. If ζ belongs to a particular Wℓ, note

that the product di=1 f(ξi) is constant over all the dℓ possibilities of ξi ∈ Γ with ξ1 + ... + ξd = ζ (since these possibilities are just certain permutations of each other); let us denote this product by

πζ(f). Hence, for the term on the left-hand side of (2.1), we have

2

2

d

d ℓ

=

f(ξi)

πζ(f)

.

i=1

ζ∈Fdq ξ1+...+ξd=ζ ξi∈Γ

ℓ∈Pd ζ∈Wℓ

Similarly, the combinatorics of expanding the d-th power in the right-hand side of (2.1) yields

 

 

d

d ℓ |πζ(f)|2 .

|f(ξ)|2

=

ξ∈Γ

ℓ∈Pd ζ∈Wℓ

Hence, our inequality (2.1) is equivalent to

2

d ℓ |πζ(f)|2 . (2.5)

d ℓ

≤ C2d

πζ(f)

ℓ∈Pd ζ∈Wℓ

ℓ∈Pd ζ∈Wℓ

We conclude this subsection with two remarks. Firstly, note that only |f| appears in (2.5). Secondly, if one believes that f ≡ 1 is a maximizer, then one can guess the value of the optimal constant C2d in (2.5). In fact, when f ≡ 1, recalling that the right-hand sides of (2.1) and (2.5) coincide, we find

d ℓ |Wℓ| = qd , (2.6)

ℓ∈Pd

and so the optimal constant C2d must then be equal to

2

1 qd ℓ∈P

d ℓ

A :=

|Wℓ|. (2.7)

d

Thus, by (2.4) we are led to Conjecture 1 (modulo the classification of maximizers).

- 2.2. Symmetric sums and Muirhead’s inequality. We now want to rewrite (2.5) in terms of symmetric sums. We would like to do it in such a way that all symmetric sums are normalized, which in this case means that they have the same number of terms. Let x1,x2,...,xq be q variables and let Sq be the group of permutations of {1,2,...,q}. Associated to a partition ℓ = (ℓ1,ℓ2,...,ℓd) ∈ Pd, we define the ℓ-th symmetric sum Σℓ as


τ(d). (2.8)

Σℓ :=

τ(2) ...xℓ

τ(1)xℓ

xℓ

2

1

d

τ∈Sq

Note that, by definition, the symmetric sum Σℓ has q! terms. As an example, if q = 5, d = 3 and ℓ = (2,1,0), we would have

6x2ixj.

Σ(2,1,0) =

1≤i,j≤5 i̸=j

Returning to our setup, the q variables will be {|f(ξ)|2 : ξ ∈ Γ}. A counting argument (consider f ≡ 1 in order to find the multiplicative constant) yields

|πζ(f)|2 = |Wℓ| q!

Σℓ. (2.9)

ζ∈Wℓ

In light of (2.5), (2.7) and (2.9), the desired inequality becomes

2

d ℓ

d ℓ |Wℓ|Σℓ.

|Wℓ|Σℓ ≤ A

ℓ∈Pd

ℓ∈Pd

This can be rewritten as

where the weight ωℓ is defined by

ωℓ Σℓ ≥ 0, (2.10)

ℓ∈Pd

ωℓ := A −

d ℓ

d ℓ |Wℓ|.

We make two remarks. Firstly, from (2.6) and (2.7), we have

ωℓ = 0. (2.11)

ℓ∈Pd

Secondly, ωℓ < 0 if and only if

d! A

. (2.12) We proceed to decompose Pd into two disjoint subsets,

ℓ! := ℓ1! ℓ2! ... ℓd! <

Pd = N ∪ P , (2.13)

where a partition n = (n1,...,nd) belongs to N if ωn < 0, and a partition p = (p1,...,pd) belongs to P if ωp ≥ 0. Inequality (2.10) can be rewritten as

(−ωn)Σn ≤

ωp Σp. (2.14)

n∈N

p∈P

In this way, (2.14) amounts to an inequality between sums of weighted symmetric sums, both of which have non-negative weights. In light of (2.11), the total weight on the left-hand side is the same as on the right-hand side. According to (2.12), the partitions in N have the lowest values of ℓ!.

In the set of integer partitions, there is a notion of partial order that is suitable for our purposes.

Given two partitions ℓ = (ℓ1,ℓ2,...,ℓd) and ℓ′ = (ℓ′1,ℓ′2,...,ℓ′d) we say that ℓ ≤ ℓ′ if the sequence of partial sums of ℓ is always majorized by the sequence of partial sums of ℓ′, that is,

ℓ1 + ... + ℓk ≤ ℓ′1 + ... + ℓ′k for each 1 ≤ k ≤ d. This is known as the dominance order. One can show that, under our standing hypothesis that the coordinates of each ℓ are decreasing,

ℓ ≤ ℓ′ ⇒ ℓ! ≤ (ℓ′)!.

We remark that the converse does not necessarily hold, since two partitions might not be comparable (e.g. take ℓ = (4,1,1) and ℓ′ = (3,3,0) in P6).

The following general inequality between symmetric sums arises naturally as a tool to be used in the present situation. In what follows, if ℓ = (ℓ1,...,ℓd) ∈ Pd, we set ρ(ℓ) := |{1 ≤ i ≤ d : ℓi > 0}|. Note that if ℓ ≤ ℓ′, then ρ(ℓ) ≥ ρ(ℓ′).

- Lemma 4 (Muirhead’s inequality [15]). Let q ∈ N and x1,x2,...,xq be non-negative real numbers. For each ℓ ∈ Pd, let the symmetric sum Σℓ be defined as in (2.8). If ℓ ≤ ℓ′ then


Σℓ ≤ Σℓ′ , (2.15) with equality if and only if at least one the following conditions holds:

- (i) ℓ = ℓ′ ;
- (ii) x1 = x2 = ... = xq ;
- (iii) At least (q − ρ(ℓ′) + 1) of the numbers {xi}qi=1 are zero, in which case both sides of (2.15) are zero;
- (iv) ρ(ℓ) = ρ(ℓ′), with k of the numbers {xi}qi=1 being zero for a certain k ≤ q − ρ(ℓ′), and the remaining (q − k) positive numbers being all equal.


Remarks: In Lemma 4, q can be any natural number (not necessarily a power of a prime). Muirhead’s inequality (also found in [9, pp. 44–45]) is usually stated for positive numbers x1,...,xq, with the equality cases being (i) and (ii). We arrive at the inequality in the case of non-negative xj’s by continuity, but the equality cases (iii) and (iv) are a bit more subtle and, as we have not been able to find a reference in the literature, we provide a brief proof.

Proof of Lemma 4 (cases of equality (iii) and (iv)). Consider a non-negative sequence x1,...,xq. As remarked above, we may assume that some, but not all, of the xj’s are equal to zero. By symmetry, we may further assume that x1,...,xq−k are positive, and that xq−k+1 = ··· = xq = 0.

Observe that if Σℓ′ = 0, then Σℓ = 0 as well, and the former identity holds if and only if each summand in Σℓ′ equals zero. Moreover, the summands of Σℓ′ are all zero if and only if q − k < ρ(ℓ′), i.e., (iii) holds.

Finally, consider the case q − k ≥ ρ(ℓ′), so that Σℓ′ ̸= 0. Of course, Σℓ = Σℓ′ can only hold if Σℓ ̸= 0, so we may assume that q − k ≥ ρ(ℓ) as well. Define

Σℓ :=

τ(2) ...xℓ

xℓ

τ(1)xℓ

1

2

d

τ(d)

τ∈Sq−k

(with xℓτj(j) interpreted as 1 if ρ(ℓ) < j ≤ d), which involves only positive xj’s. By standard combinatorial arguments,

(q − ρ(ℓ))! (q − k − ρ(ℓ))!

Σℓ = (q − ρ(ℓ))...(q − k − ρ(ℓ) + 1) Σℓ, and, since ρ(ℓ) ≥ ρ(ℓ′),

Σℓ =

(q − ρ(ℓ))! (q − k − ρ(ℓ))! ≤

(q − ρ(ℓ′))! (q − k − ρ(ℓ′))!

,

with equality if and only if ρ(ℓ) = ρ(ℓ′). Applying Muirhead’s inequality in the case of positive xj, we arrive at the final case of equality, condition (iv). □

## 2.3. Fractional matching.

- 2.3.1. The strategy. With (2.14) in mind, we seek to find, for each pair (n,p) ∈ N ×P, a non-negative weight τnp such that:


- (i) If n and p are non-comparable (with respect to the partial dominance order), then τnp = 0.
- (ii) For each n ∈ N, setting Pn := {p ∈ P : n ≤ p}, we have

(−ωn) =

p∈Pn

τnp. (2.16)

- (iii) For each p ∈ P, setting Np := {n ∈ N : n ≤ p}, we have


ωp =

τnp. (2.17)

n∈Np

Once we succeed in this task, the sharp inequality (2.14) can then be established using (2.15)–(2.17) as follows:

(−ωn)Σn =

τnp Σn ≤

τnp Σp =

τnp Σp =

ωpΣp. (2.18)

n∈N

n∈N p∈Pn

n∈N p∈Pn

p∈P n∈Np

p∈P

For the case of equality, note that the partition p = (d,0,...,0) ∈ P has ωp > 0 and majorizes all the other partitions in Pd; thus, in particular, it majorizes all the partitions in N. Hence, from (2.17), there exists at least one partition n ∈ N such that τnp > 0. For this particular pair, inequality

τnp Σn ≤ τnp Σp was invoked in (2.18) and we see from Lemma 4 that equality occurs in this case if and only if all the variables (which are {|f(ξ)|2 : ξ ∈ Γ} in our setup) are equal.

- 2.3.2. An example. Let us show how to directly settle the case of the moment curve in d = 3 for

general q = pn, p > 3 prime and n ≥ 1. In this case, one has P3 = {(1,1,1),(2,1,0),(3,0,0)}. We then compute

|W(1,1,1)| =

q(q − 1)(q − 2) 6

; |W(2,1,0)| = q(q − 1) ; |W(3,0,0)| = q. Then

A =

6q3 − 9q2 + 4q q3

= 6 −

9 q

+

4 q2

, and

ω(1,1,1) =

(−9q + 4)(q − 1)(q − 2) q

; ω(2,1,0) =

3(3q2 − 9q + 4)(q − 1) q

; ω(3,0,0) =

5q2 − 9q + 4 q

.

Note that ω(1,1,1) + ω(2,1,0) + ω(3,0,0) = 0 and, since q > 3, we have ω(1,1,1) < 0 ; ω(2,1,0) > 0 ; ω(3,0,0) > 0. Since (1,1,1) ≤ (2,1,0) ≤ (3,0,0), our fractional matching is accomplished by setting

τ(1,1,1)(2,1,0) := ω(2,1,0) and τ(1,1,1)(3,0,0) := ω(3,0,0). This concludes the proof of Theorem 2 in the case d = 3.

- 2.3.3. Strassen’s theorem. It turns out that the possibility of accomplishing the fractional matching construction proposed in §2.3.1 is a well-understood situation in combinatorics, in the context of bipartite graphs. This is characterized by Strassen’s theorem [19], which we now describe. In what follows let G = (V,E,w) be a weighted graph, where V is the set of vertices, E is the set of (undirected)

edges, and each v ∈ V is assigned a weight w(v). For any subset U ⊂ V we set w(U) := v∈U w(v). Recall that a bipartite graph is a graph in which the vertices can be partitioned into two sets {A,B} such that all edges have one endpoint in A and the other endpoint in B.

Lemma 5 (Strassen’s theorem). Let G = (V,E,w) be a weighted bipartite graph with bipartition {A,B} such that w(A) = w(B). Then the following conditions are equivalent:

- (i) For all U ⊂ A we have w(U) ≤ w(N(U)), where N(U) denotes the set of neighbors of U, i.e. the set of all vertices in B that are connected by an edge to some vertex in U.
- (ii) There exists an edge weight function w : E → [0,∞) such that, for all x ∈ V , we have w(x) = e∼x w(e), where the sum is taken over all edges e incident to x.


- 2.3.4. Reduction to finitely many checks. Our situation plainly falls under the scope of Lemma 5, with the vertices being the elements of Pd, and the bipartition of the vertices given by Pd = N ∪ P. The weight of a given n ∈ N is −ωn, and the weight of a given p ∈ P is ωp (hence both sets N and P have the same total weight). We declare that there is an edge connecting n ∈ N and p ∈ P if


and only if n ≤ p. Therefore, by Lemma 5, our strategy boils down to checking a finite number of inequalities, namely: for any U ⊂ N, we must have

ωp. (2.19)

(−ωn) ≤

n∈U

p ∈

Pn

n∈U

- 2.4. Computational part. For each given d and q, the success of our strategy depends on (2.19), and can be verified in finite time. For a fixed dimension d, if one wants to establish the result for all q, we need a tool to prove it for large q, i.e. for q ≥ c(d), and hence the success of our strategy is reduced again to the verification of (2.19) for d < q < c(d). Such a tool is established in Theorem

- 3, which we prove in the following subsection. The computational verification of Theorem 2 is then described in Appendix A.


- 2.5. Asymptotic methods. In this subsection, we prove Theorem 3. The main idea is the following: looking at (2.12), if d!/A ≤ 6, then the set N will contain at most three partitions, namely (1,1,...,1),(2,1,...,1,0) and (2,2,1,...,1,0,0). Observe that


(1,1,...,1) ≤ (2,1,...,1,0) ≤ (2,2,1,...,1,0,0),

and that these three partitions are less than or equal to any other of the remaining partitions. Hence, in this case, each partition in N will be less than or equal to each partition in P, and (2.19) clearly holds.

In light of (2.7), the condition d!/A ≤ 6 is equivalent to

2

d! 6

d ℓ

|Wℓ|. (2.20)

qd ≤

ℓ∈Pd

We shall consider only one summand on the right-hand side of (2.20), namely, the one associated to the partition ℓ = (1,1,...,1) (note that this is the only one of order qd). Hence (2.20) follows from

d! 6

qd ≤ (d!)2 W(1,1,...,1) = d!q(q − 1)...(q − d + 1), where we have used (2.4). In turn, this is equivalent to

1 6 ≤ 1 1 −

1 q

2 q

d − 1 q

1 −

... 1 −

, and taking logarithms, we get

d−1

j q

log 6 ≥ −

log 1 −

. (2.21)

j=1

We may assume that q ≥ 2d. Using that x + x2 ≥ −log(1 − x)

for 0 ≤ x ≤ 1/2, inequality (2.21) follows from

d−1

d−1

2

j q

j q

log 6 ≥

+

j=1

j=1

which is equivalent to the quadratic equation

d(d − 1) 2q

=

+

(d − 1)d(2d − 1) 6q2

,

6(log 6)q2 − 3d(d − 1)q − (d − 1)d(2d − 1) ≥ 0. (2.22) Inequality (2.22) is verified if

3d(d − 1) 1 + 1 + 8 log 63 (2d−1)

d(d−1)

. (2.23)

q ≥

12log 6

Using the fact that √1 + x ≤ 1 + x2 for any x ≥ 0, inequality (2.23) then follows from

3d(d − 1) 2 + 4 log 63 (2d−1)

d(d − 1) 2log 6

(2d − 1) 3

d(d−1)

=

+

q ≥

. This completes the proof of Theorem 3.

12log 6

3. Concluding remarks

- 3.1. On computational complexity. The Hardy–Ramanujan formula [10] provides an asymptotic formula for the number of partitions in Pd:


√

1 4d√3

2d/3, as d → ∞. (3.1)

eπ

|Pd| ∼

The computational work needed to determine the weights ωℓ thus grows as in (3.1). However, a complete computation is not always necessary, as shown in the proof of Theorem 3. In that regime, the size of the set N = {ℓ ∈ Pd : ωℓ < 0} is small, which allowed for a direct verification of (2.19).

In this subsection, we briefly explain why the size of the power set of N (i.e., the number of conditions to be checked in (2.19)) increases rapidly as d increases and q remains close to d. Even though in our setup the smallest possible value of q equals d + 1, in the asymptotic argument below it is harmless to assume, as we shall, that q = d. From (2.7) we then have

2

1 dd ℓ∈P

d ℓ

A =

|Wℓ|. (3.2)

d

We seek an upper bound for A. Split Pd into two disjoint subsets, Pd = Id,k ∪Id,k∁ , where Id,k denotes the set of partitions with a block of at least k consecutive ones (k will be chosen later). By removing

the final k ones in this block, the partitions in Id,k are in bijective correspondence with the partitions in Pd−k. Using dℓ ≤ d! and |Wℓ| ≤ kd!! ≤ dd−k for each ℓ ∈ Id,k, we have

2

(d!)2 dd · dd−k · |Pd−k|. (3.3)

1 dd ℓ∈I

d ℓ

|Wℓ| ≤

d,k

On the other hand, if ℓ ∈ Id,k∁ , note that

. (3.4) In fact, if we remove the final block of ones in ℓ, which in this case is of length at most k−1, we are left with ℓ1 +...+ℓj = a ≥ d−k+1 elements, with ℓ1 ≥ ... ≥ ℓj ≥ 2. Using that (m+1)!(n−1)! ≥ m!n! if m ≥ n ≥ 1, one can check that in this case the minimal value of ℓ1!...ℓj! occurs when they all equal 2 (or one of them equals 3, if a is odd). In all such cases, (3.4) holds. From (3.4) and (2.6),

ℓ! ≥ 2

d−k 2

2

1 dd

- 1 dd

d!

- 2(d−k)/2 ℓ∈P


- 1 dd

d!

- 2(d−k)/2 ℓ∈Id,k∁


d! 2(d−k)/2

d ℓ |Wℓ| ≤

d ℓ |Wℓ| =

d ℓ

. (3.5)

|Wℓ| ≤

ℓ∈Id,k∁

d

Using (3.2), (3.3) and (3.5) we arrive at A d! ≤

1 2(d−k)/2

d! dd · dd−k · |Pd−k| +

. (3.6)

We now choose 3 k = d − 2 logd d. Stirling’s formula together with (3.1) in (3.6) yields

√

√2πd ed · d

d/(3(log d)) 2d (log d)

A d!

- 1

- 2


- 1

- 2


eπ

+

d 2 log d

≲

≲

√3

·

.

d 4 log d

d 4 log d

Recall condition (2.12). Given a ≥ 1, the partition ℓ = (a,1,1,...,1,0,0,...,0) belongs to N whenever

a! ≲ 2

d

4logd.

By Stirling’s formula, this is guaranteed for a ∼ 8(logdd)2 and d large. Then, any partition of the form (ℓ1,ℓ2,...,ℓj,1,1,...1,0,...,0), where ℓi ≥ 1 and ji=1 ℓi = a, belongs to N as well. There are as many such partitions as

√

2(log d)2 d√3

d/(12(logd)2).

eπ

|Pa| ∼

It follows that the size of the power set of N, which corresponds to the number of conditions to be verified in (2.19), grows at least as fast as

√

2(log d)2 d

d/(12(log d)2)

√3 eπ

, as d → ∞.

2

- 3.2. Additional variables. For k ∈ N we might consider a curve Γ ⊂ Fdq+k of the form Γ = {(ξ,ξ2,...,ξd,ϕ(ξ)) : ξ ∈ Fq}, where ϕ : Fq → Fkq is an arbitrary function, and address the sharp inequality


∥(fσ)∨∥L2d(Fdq+k,dx) ≤ C(d,qk) ∥f∥L2(Γ,σ).

3Strictly speaking, we should consider the integer part of this number, but this is again harmless for the asymptotic argument.

For ζ = (ζ1,...,ζd+k) ∈ Fqd+k, in analogy to (2.3), one starts by understanding the structure of the solutions of the system

t1 + t2 + ... + td = ζ1 t21 + t22 + ... + t2d = ζ2 . td1 + td2 + ... + tdd = ζd

d

ϕ(ti) = (ζd+1,...,ζd+k).

i=1

Note that the set {t1,t2,...,td} is completely determined from the sub-vector (ζ1,ζ2,...,ζd), and this in turn uniquely determines the values of ζd+1,...,ζd+k. The analysis of the sharp inequality is then exactly the same as done in Section 2 and we conclude that the optimal constant C(d,qk) coincides with the optimal constant of (1.2).

- 3.3. Related curves. Our strategy allows us to treat the same problem associated to other curves η : Fq → Fdq, provided that in the sum


η(t1) + ··· + η(td) = ζ,

the multiset {t1,...,td} is uniquely determined by ζ. For example, let A be an invertible d×d matrix. With γ(ξ) = (ξ,ξ2,...,ξd), we can consider

η(ξ) := γ(ξ) · A for which the optimal constant is again equal to the optimal constant of (1.2).

The analogous sharp form of (1.2) (e.g. [11, Theorem 1.1]) for a general polynomial is an interesting question when the components of the associated polynomial map Φ : Fdq → Fdq given by

Φ(t1,...,td) := γ(t1) + ... + γ(td)

do not uniquely identify ti up to permutations. For example, associated with the polynomial γ(ξ) = (ξ,ξ3,ξ5), the following system of equations

t1 + t2 + t3 = 1 t31 + t32 + t33 = 1 t51 + t52 + t53 = 1

contains (1,t2,−t2) within the solution set. Moreover, in the continuous setting, the dichotomy between existence of maximizers and concentration of maximizing sequences at (e.g.) t = ±1 has not been resolved [2, Theorem 1.3]. Thus the methods of the present paper cannot be directly adapted.

Acknowledgements

This project was initiated at a SQuaRE at the American Institute of Mathematics. The authors thank AIM for providing a supportive and mathematically rich environment. Oliveira e Silva is partially supported by FCT/Portugal through project UIDB/04459/2020 with DOI identifier 1054499/UIDP/04459/2020. Stovall is partially supported by NSF DMS-2246906, and Tautges is partially supported by NSF DMS-2037851.

Appendix A. Computational part

In this appendix, we describe the algorithm used to verify the validity of (2.19) for dimensions 2 ≤ d ≤ 20 and exponents q < d2 log 6(d−1) + (2d−1)

3 . Computations were performed in Python 3 with SageMath libraries.

For every admissible d (line 8), we use Sage to generate the partition poset with the dominance order (line 10) and compute ℓ! for all ℓ ∈ Pd (lines 11–13). For every admissible q (line 14), we compute the value of ωℓ for all ℓ ∈ Pd (lines 16–24). For each fixed pair (d,q), we iterate over subsets I ⊂ N (recall that N was defined in (2.13)) and verify that

ωℓ′ ≥ 0

ℓ′≥ℓ for some ℓ∈I

(lines 25–32). This is equivalent to (2.19) and, since the check succeeds, Conjecture 1 holds for every dimension d and exponent q in the claimed range. This concludes the proof of Theorem 2.

- 1 from sage.all import *
- 2 def choose(x, l):
- 3 return factorial(x)/product([ factorial(i) for i in l ])
- 4 def get_w(l, d, q):
- 5 c = [ l.count(i) for i in range(d+1) ]
- 6 c[0] = q - len(l)
- 7 return choose(q, c)
- 8 for d in range(2, 20):
- 9 broken = False
- 10 P = posets.IntegerPartitionsDominanceOrder(d)
- 11 chs = {}
- 12 for p in P:
- 13 chs[p] = choose(d, list(p))
- 14 for q in range(d+1, floor(d*(d-1)/(2*log(6)) + (2*d - 1)/3) + 1):
- 15 q = Integer(q)
- 16 ws = omegas = {}
- 17 num = denom = 0
- 18 for p in P:
- 19 ws[p] = get_w(list(p), d, q)


- 20 num += chs[p]**2 * ws[p]
- 21 denom += chs[p] * ws[p]
- 22 C = num / denom
- 23 for p in P:
- 24 omegas[p] = chs[p] * ws[p] * (C - chs[p])
- 25 LHS = [ p for p in P if omegas[p] < 0 ]
- 26 for I in Subsets(LHS):
- 27 if len(I) == 0:
- 28 continue
- 29 if sum([ omegas[p] for p in P.order_filter(I) ]) < 0:
- 30 print("Proposition failed at " + str(p) + ", q = " + str(q))
- 31 broken = True
- 32 break
- 33 if not broken:
- 34 print("Proposition true for d = " + str(d))


References

- [1] C. Biswas and B. Stovall, Existence of extremizers for Fourier restriction to the moment curve, Trans. Amer. Math. Soc. 376 (2023), no. 5, 3473–3492.
- [2] C. Biswas and B. Stovall, Sharp Fourier restriction to monomial curves, Math. Ann. 391 (2025), no. 4, 5391–5425.
- [3] J. Bourgain, C. Demeter and L. Guth, Proof of the main conjecture in Vinogradov’s mean value theorem for degrees higher than three, Ann. of Math. (2) 184 (2016), no. 2, 633–682.
- [4] A. Carbery, B. Stones and J. Wright, Averages in vector spaces over finite fields, Math. Proc. Cambridge Philos. Soc. 144 (2008), no. 1, 13–27.
- [5] S. Drury, Restrictions of Fourier transforms to curves, Ann. Inst. Fourier (Grenoble) 35 (1985), no. 1, 117–123.
- [6] D. Foschi and D. Oliveira e Silva, Some recent progress on sharp Fourier restriction theory, Anal. Math. 43 (2017), no. 2, 241–265.
- [7] C. Gonza´lez-Riquelme and D. Oliveira e Silva, Sharp extension inequalities on finite fields, preprint (2024).
- [8] S. Guo, Z. Li, P.-L. Yung and P. Zorin-Kranich, A short proof of ℓ2 decoupling for the moment curve, Amer. J. Math. 143 (2021), no. 6, 1983–1998.
- [9] G. H. Hardy, J. E. Littlewood and G. P´olya, Inequalities, Reprint of the 1952 edition Cambridge Math. Lib. Cambridge University Press, Cambridge, 1988.
- [10] G. H. Hardy and S. Ramanujan, Asymptotic Formulae in Combinatory Analysis, Proc. London Math. Soc. (2) 17

(1918), 75–115.

- [11] D. Koh and C. Y. Shen, Sharp extension theorems and Falconer distance problems for algebraic curves in two dimensional vector spaces over finite fields, Rev. Mat. Iberoam. 28 (2012), no. 1, 157–178.
- [12] J. Matousek, Lectures on Discrete Geometry, Grad. Texts in Math., 212 Springer-Verlag, New York, 2002.
- [13] J. Matousek, Using the Borsuk–Ulam Theorem. Lectures on topological methods in combinatorics and geometry. Written in cooperation with Anders Bj¨orner and Gu¨nter M. Ziegler. Universitext, Springer-Verlag, Berlin, 2003.
- [14] G. Mockenhaupt and T. Tao, Restriction and Kakeya phenomena for finite fields, Duke Math. J. 121 (2004), no. 1, 35–74.
- [15] R. F. Muirhead, Some Methods Applicable to Identities and Inequalities of Symmetric Algebraic Functions of n Letters, Thesis (D.Sc.)–University of Glasgow (United Kingdom) ProQuest LLC, Ann Arbor, MI, 1904. 34 pp.


- [16] G. Negro, D. Oliveira e Silva and C. Thiele, When does e−|τ| maximize Fourier extension for a conic section? Harmonic analysis and convexity, 391–426. Adv. Anal. Geom., 9 De Gruyter, Berlin, 2023.
- [17] P. Ronda, Finite field sharp extension inequalities for curves and quadratic surfaces, M.Sc. thesis, IST, in preparation (2025).
- [18] K. F. Roth, On a problem of Heilbronn, J. London Math. Soc. 26 (1951), 198–204.
- [19] V. Strassen, The existence of probability measures with given marginals, Ann. Math. Statist. 36 (1965), 423–439.
- [20] B. L. van der Waerden, Modern Algebra, Frederick Ungar, New York, 1953.


Department of Mathematics, Indian Institute of Technology Bombay, Mumbai 400076, India Email address: cbiswas@iitb.ac.in

ICTP - The Abdus Salam International Centre for Theoretical Physics, Strada Costiera, 11, I - 34151, Trieste, Italy

Email address: carneiro@ictp.it

Macalester College, Mathematics, Statistics, and Computer Science, Olin-Rice Science Center, Room 222, Saint Paul, MN 55105-1899, USA

Email address: tflock@macalester.edu

Center for Mathematical Analysis, Geometry and Dynamical Systems & Departamento de Matematica,´ Instituto Superior Tecnico,´ Av. Rovisco Pais, 1049-001 Lisboa, Portugal

Email address: diogo.oliveira.e.silva@tecnico.ulisboa.pt

University of Wisconsin–Madison, Department of Mathematics, 480 Lincoln Drive, Madison, WI 53706, USA

Email address: stovall@math.wisc.edu

University of Wisconsin–Madison, Department of Mathematics, 480 Lincoln Drive, Madison, WI 53706, USA

Email address: tautges2@wisc.edu

