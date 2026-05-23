---
type: source
kind: paper
title: On convex equations
authors: Tomasz Schoen
year: 2023
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2310.09584v1
source_local: ../raw/2023-schoen-convex-equations.pdf
topic: general-knowledge
cites:
---

arXiv:2310.09584v1[math.CO]14Oct2023

On convex equations

Tomasz Schoen Faculty of Mathematics and Computer Science, Adam Mickiewicz University, Uniwersytetu Pozna´nskiego 4, 61-614 Pozna´n, Poland schoen@amu.edu.pl

Abstract

We prove that every subset of {1,...,N} which does not contain any solutions to the equation x + y + z = 3w has at most

exp − c(log N)1/5+o(1) N

elements, for some c > 0. This theorem improves upon previous estimates. Additionally, our method has the potential to yield an optimal estimate for this problem that matches the known Behrend’s lower estimate. Our approach relies on a new result on almost-periodicity of convolutions.

1. Introduction

The problem of estimating the maximum size of a subset of {1,... ,N} that does not contain solutions to an invariant linear equation

a1x1 + ··· + akxk = 0,

where a1,... ,ak ∈ Z,k ≥ 3 and a1 + ··· + ak = 0, appears to be one of the most intriguing in additive combinatorics. In the general case not much is known, and even for the ’simplest’ equation [13]

2x1 + 2x2 = y1 + 3y2

we are only able to prove only an upper bound of the form N1−o(1) and the lower bound cN1/2. More precise estimates are known only in the case of certain symmetric equations i.e.

a1x1 + ··· + akxk = a1y1 + ··· + akyk,

![image 1](<2023-schoen-convex-equations_images/imageFile1.png>)

Keywords and phrases: sumsets, arithmetic progressions. 2010 Mathematics Subject Classiﬁcation: primary 11B30 , secondary 11B25.

1

and equations of the form

a1x1 + ··· + akxk = by, (1)

where a1,... ,ak,b are positive integers and a1 + ··· + ak = b, which we call convex. We focus here on the later type of equations. An important issue is the fact that we have a general lower bound of a similar shape that applies to all convex equations. Behrend [1] showed (see also [7] and [9] for slight improvements) that for any convex equation (1) there is a solution free subset of {1,... ,N} of size

exp − C(log N)1/2) N,

where C > 0 and it depends only on the coeﬃcients of the given equation. The most interesting convex equation is, of course, x + y = 2z, as each of its nontrivial solutions (diﬀerent form x = y = z) forms a nontrivial three term arithmetic progression. The ﬁrst signiﬁcant upper estimate was established by Roth [12] ( Roth’s theorem, along with all the results quoted below, provides the same bounds for any invariant equation with an equal or greater number of variables).

- Theorem 1 (Roth) Suppose that A ⊆ {1,... ,N} does not contain any nontrivial three term arithmetic progression. Then

|A| ≪

N log log N

![image 2](<2023-schoen-convex-equations_images/imageFile2.png>)

.

Despite considerable eﬀort and a high level of interest in the problem, we were only able to improve Roth’s theorem by replacing his upper bound with N/(log N)1+c, for some small constant c > 0. Very recently, Kelley and Meka [10] (see also [4]) proved a breakthrough result, much improving previous bounds, which is quite close to Behrend’s lower bound.

- Theorem 2 (Kelley-Meka) Suppose that A ⊆ {1,... ,N} does not contain any nontrivial three term arithmetic progression. Then

|A| ≪ exp − c(log N)1/11 N.

- A short time later, Bloom and Sisask [3], by utilizing almost-periodic more eﬃciently in KelleyMeka proof, were able to increase the exponent from 1/11 to 1/9.


However, several years earlier, even better upper bounds were already known for invariant equations equations with more than three variables. Shkredov and the author [17] established such result for invariant equations with at least six variables.

- Theorem 3 ([16]) Suppose that A ⊆ {1,... ,N} does not contain any nontrivial solutions to the equation x1 + ··· + x5 = 5y. Then


|A| ≤ exp − c(log N)1/7 N.

The above result was extended in [17] to invariant equations with at least four variables with the same upper bound. Furthermore, in a recent work by Ko’sciuszko [11], it was showed, among other results, that if a subset of {1,... ,N} does not contain any nontrivial solutions to the equation x1 + ··· + xk = ky, with k ≥ 2 · 3m+1 + 2, then its size is at most

exp − c(log N)1/(6+γm) N

where γm = 21−m.

In this paper, we further improve upon the aforementioned results for invariant equations with at least four variables by narrowing the upper bound closer to Behrend’s lower bound.

- Theorem 4 Suppose that A ⊆ {1,... ,N} does not contain any nontrivial solutions to the equation x + y + z = 3w. Then


|A| ≤ exp − c(log N)1/5 exp(−C log log(1/N)) N.

![image 3](<2023-schoen-convex-equations_images/imageFile3.png>)

We ground our argument in a new result related to the almost-periodicity of convolutions, which is elaborated upon in Section 3 (see Theorem 9).

2. Elementary properties of Bohr sets and notation

Throughout the paper we will use Bohr sets, which are a fundamental tool introduced to additive combinatorics by Bourgain [5]. Bohr sets have a rich arithmetic structure and can serve

- as a substitute for subspaces, which is especially useful when applying the density increment strategy.


Let G be an abelian group and let us denote the dual group of its characters by G. We deﬁne the Bohr set with a generating set Γ ⊆ G and a radius ρ ≥ 0 to be the set

B = B(Γ,ρ) = x ∈ G : |1 − γ(x)| ≤ ρ for all γ ∈ Γ .

The size of Γ is called the rank of B. Given δ > 0 and a Bohr set B = B(Γ,γ), by Bδ we mean the Bohr set B(Γ,δγ). The next lemma is pretty standard, hence we refer the reader to [18] for a complete account.

- Lemma 5 Let B ⊆ G be a Bohr set of rank d and radius ρ ∈ [0,2]. Then we have |B| ≥ (ρ/2π)dN,

|B2| ≤ 6d|B| and for every δ ∈ [0,1]

|Bδ| ≥ (δ/2)3d|B|.

Bohr sets do not always behave like convex bodies. The size of Bohr sets can vary signiﬁcantly even for small changes of the radius which was the motivation behind the following deﬁnition. We call a Bohr set B of rank d and radius ρ regular if for every δ, with |δ| ≤ 1/100d we have

(1 − 100d|δ|)|B| ≤ |B1+δ| ≤ (1 + 100d|δ|)|B|. Bourgain [5] showed that regular Bohr sets are ubiquitous.

- Lemma 6 For every Bohr set B there exists δ ∈ [1/2,1] such that Bδ is regular.


The advantage of regularity is that the size of sumset B +Bδ ⊆ B1+δ is only slightly bigger than the size of B, provided that δ ≤ 1/100d.

Throughout the paper, we will use a fairly standard notation in additive combinatorics.

If T and A are two sets, we refer by µT(A) := |A|T∩T| | the relative density of A in T, and put µT := 1T/|T|, where 1T is the indicator function of T.

![image 4](<2023-schoen-convex-equations_images/imageFile4.png>)

For two functions f,g : G → C we write f ∗ g(x) =

f(y)g(x − y)

y

for the convolution of f and g. Notice that 1A ∗ µT(x) = |A∩(|Tx−| T)|. For p ≥ 1 deﬁne f p :=

![image 5](<2023-schoen-convex-equations_images/imageFile5.png>)

|f(x)|p 1/p,

x∈G

and

f ∞ := sup x∈G

|f(x)|.

For convenience, we employ the symbols C and c to represent positive constants that are adequately large and small, respectively. It should be noted that these constants’ values may diﬀer in various instances. We also use standard Vinogradov’s ≪ notation. By log we always mean log2 . Moreover, when we refer to the group G it is understood to be a ﬁnite abelian group; however, in applications, we always have G = Z/NZ for a prime N. As usually if A ⊆ {1,... ,M} then we consider A as a subset of Z/NZ with 3M ≤ N ≤ 6M.

3. A sketch of the argument

Like in all previous works concerning sets free of solutions to a convex equation, we also employ the density increment strategy. The general line of the proof is the same as in [17], but the details are very diﬀerent. The proof method in [17] relies on the L∞-almost periodicity of three-fold convolution (see Theorem 7 below), which extends Sanders’ observation [14] that the Croot-Sisak [6] Lp-almost periodicity lemma (for two-fold convolution) works exceptionally eﬃciently for the convolution 1A ∗ 1A−A. This allowed us in [17] to achieve a density increment

- at each step by a factor of 5/4 on the Bohr set of rank increased by log4(2/α), where α is the initial density of our solution-free set.


Here we proceed diﬀerently, applying our key ingredient, a version of L∞-almost periodicity Theorem 9, we will be able to obtain alternative result. This approach leads us to a result, which, in its simplest form, can be summarized as follows: either we attain a substantial increase in density within a Bohr set, whose the rank increases by log4+o(1)(2/α), or we achieve a modest density increment within a Bohr set, whose the rank increases by log1+o(1)(2/α).

Another crucial element in proving the main theorem’s bound lies in the precise control of the radii of successive Bohr sets. Remarkably, Theorem 9 works highly eﬀective in this regard as well.

4. An almost-periods lemma

Here we will establish the key lemma for our approach, which is particularly useful when applying the density increment argument on a sequence of Bohr sets. The main idea is that if, after applying the following Theorem 7 proved in [17], the shifts of set A do not achieve a signiﬁcant density increment on Bohr set B, then we will be able to obtain the conclusion of Theorem 7 for a much larger Bohr set. To accomplish this, we will use a probabilistic argument, approximating the convolution 1M∗µB by a much larger set R, and then applying again Theorem

- 7 to it, obtaining much more eﬃcient estimates. The concept of applying the fact that 1M ∗µB is small resembles a part the argument in [15] (speciﬁcally, refer to Lemma 14 in [15]). Nevertheless, this idea was employed in [15] in a completely distinct manner, making use of Fourier analysis techniques.


Theorem 7 ([17]) Let ε ∈ (0,1). Let A,M,L be subsets of a ﬁnite abelian group G and let

- B ⊆ G be a regular Bohr set of rank d and radius ρ. Suppose |A + S| ≤ K|A| for some subset S ⊆ B with µB(S) ≥ σ > 0, and assume η := |M|/|L| ≤ 1. Then there is a regular Bohr set T


- of rank d + d′ and radius at least cρεη1/2/d2d′, where d′ ≪ ε−2 log2(2/εη)log(2/η)log(2K) + log(1/σ)


such that

1A ∗ 1M ∗ 1L ∗ µT − 1A ∗ 1M ∗ 1L ∞ ≤ ε|A||M|. (2)

In the course of the proof of the main result of this section we will use classical Bernstein’s inequality [2].

Lemma 8 (Bernstein) Let X1,... ,XN be independent random variables and suppose that |Xk− E(Xk)| ≤ m for every 1 ≤ k ≤ N. Then, for all positive t

N

N

- 1

![image 6](<2023-schoen-convex-equations_images/imageFile6.png>)

- 2t2


.

P |

Xk −

E(Xk)| ≥ t ≤ 2exp −

![image 7](<2023-schoen-convex-equations_images/imageFile7.png>)

N k=1 Var(Xk) + 13tm

![image 8](<2023-schoen-convex-equations_images/imageFile8.png>)

k=1

k=1

Theorem 9 Let ε ∈ (0,1). Let sets A,M,L,S,B ⊆ G satisfy the assumptions of Theorem 7.

- Let T ⊆ B be a regular Bohr set such that 1A ∗ 1M ∗ 1L ∗ µT − 1A ∗ 1M ∗ 1L ∞ ≤ ε|A||M|. (3)


Let ε1 ∈ (0,1) and suppose that for some positive γ ≤ 1 we have 1M ∗ µT(x) ≤ γ for every x, and |M| ≥ 2. Then there is a regular Bohr set B1 ⊆ B of rank d + d1 and radius at least ρε1(η/2γ)1/2/d2d1, where

d1 ≪ ε−1 2 log2(4γ/ε1η)log(4γ/η)log(2K) + log(1/σ) such that

![image 9](<2023-schoen-convex-equations_images/imageFile9.png>)

1A ∗1M ∗1L ∗µB1 −1A ∗1M ∗1L ∞ ≤ (2ε+ε1)|A||M|+18|A| γ|M|log |A + M + L + T|. (4)

Proo f. First, we show that there exists a set R ⊆ G such that

γ−1|M| − 6 γ−1|M| ≤ |R| ≤ γ−1|M| + 6 γ−1|M| (5) and

![image 10](<2023-schoen-convex-equations_images/imageFile10.png>)

![image 11](<2023-schoen-convex-equations_images/imageFile11.png>)

![image 12](<2023-schoen-convex-equations_images/imageFile12.png>)

1A ∗ 1M ∗ 1L ∗ µT − γ1A ∗ 1R ∗ 1L ∞ ≤ 6|A| γ|M|log |A + M + L + T|. (6) Let R be a random subset of G chosen by picking each x ∈ G independently with probability

P(x ∈ R) = γ−11M ∗ µT(x).

Note that the expected size of R is γ−1|M| and its variance does not exceed γ−1|M|, so by Bernstein’s inequality

P |R| − γ−1|M| ≤ 6 γ−1|M| ≥ 3/4. (7) Next, for a ﬁxed x ∈ W := A + M + L + T the random variable

![image 13](<2023-schoen-convex-equations_images/imageFile13.png>)

1A ∗ 1R ∗ 1L(x) =

y

1A ∗ 1L(x − y)1R(y)

has an expected value

E(1A ∗ 1R ∗ 1L(x)) = γ−11A ∗ 1M ∗ 1L ∗ µT(x) and its variance can be bouned from above by

Var(1A ∗ 1R ∗ 1L(x)) ≤

y

(1A ∗ 1L(x − y))2γ−11M ∗ µT(y) ≤ γ−1|M||A|2.

Thus, again by Bernstein’s inequality for any x ∈ W

1 4|W|

P 1A ∗ 1R ∗ 1L(x) − γ−11A ∗ 1M ∗ 1L ∗ µT(x) ≤ 6|A| γ−1|M|log |W| ≥ 1 −

![image 14](<2023-schoen-convex-equations_images/imageFile14.png>)

,

![image 15](<2023-schoen-convex-equations_images/imageFile15.png>)

so

P 1A ∗ 1R ∗ 1L − γ−11A ∗ 1M ∗ 1L ∗ µT ∞ ≤ 6|A| γ−1|M|log |W| ≥ 3/4. (8) Due to (7) and (8) there exists a set satisfying (5) and (6).

![image 16](<2023-schoen-convex-equations_images/imageFile16.png>)

By Theorem 7 applied with R in place of M and ε1 in place of ε there is a regular Bohr set B1 ⊆ B of rank d1 and radius at least ρε1η11/2/d2d1, where

γ−1|M| − 6 γ−1|M| |L|

![image 17](<2023-schoen-convex-equations_images/imageFile17.png>)

≥ η/2γ,

η1 = |R|/|L| ≥

![image 18](<2023-schoen-convex-equations_images/imageFile18.png>)

and

d1 ≪ ε−1 2 log2(2/εη1)log(2/η1)log(2K) + log(1/σ) such that

1A ∗ 1R ∗ 1L ∗ µB1 − 1A ∗ 1R ∗ 1L ∞ ≤ ε1|A||R| ≤ ε1γ−1|A||M| + 6 γ−1|M|.

![image 19](<2023-schoen-convex-equations_images/imageFile19.png>)

In view of (3), (6) and the triangle inequality we infer that

![image 20](<2023-schoen-convex-equations_images/imageFile20.png>)

1A ∗ 1M ∗ 1L − γ1A ∗ 1R ∗ 1L ∞ ≤ ε|A||M| + 6|A| γ|M|log |W|, which leads to

1A ∗ 1M ∗ 1L ∗ µB1 − γ1A ∗ 1R ∗ 1L ∗ µB1 ∞ ≤ 1A ∗ 1M ∗ 1L − γ1A ∗ 1R ∗ 1L ∞ µB1 1

= 1A ∗ 1M ∗ 1L − γ1A ∗ 1R ∗ 1L ∞ ≤ ε|A||M| + 6|A| γ|M|log |W|.

![image 21](<2023-schoen-convex-equations_images/imageFile21.png>)

By the triangle inequality we have 1A ∗ 1M ∗ 1L ∗ µB1 − 1A ∗ 1M ∗ 1L ∞ ≤ 1A ∗ 1M ∗ 1L − γ1A ∗ 1R ∗ 1L ∞

+ 1A ∗ 1M ∗ 1L ∗ µB1 − γ1A ∗ 1R ∗ 1L ∞ ≤ ε|A||M| + 6|A| γ|M|log |W|

![image 22](<2023-schoen-convex-equations_images/imageFile22.png>)

+ 1A ∗ 1M ∗ 1L ∗ µB1 − γ1A ∗ 1R ∗ 1L ∗ µB1 ∞

+ γ1A ∗ 1R ∗ 1L − γ1A ∗ 1R ∗ 1L ∗ µB1 ∞ ≤ (2ε + ε1)|A||M| + 18|A| γ|M|log |W|,

![image 23](<2023-schoen-convex-equations_images/imageFile23.png>)

which completes the proof.

4. Iterative lemmas

In this section, our goal is to establish a result (Proposition 13) that will be iteratively applied in the proof of the main theorem. Similar to the approach in [17], we divide our analysis into two cases, depending on the size of the sumset A + A′. We will begin with the case where A + A′ is large.

- Lemma 10 Let B ⊆ Z/NZ be a regular Bohr set of rank d and radius ρ such that |B| ≥ (Cd/α)5, and let A ⊆ B has relative density c0 ≥ µB(A) ≥ α for some small constant c0 > 0.


- Let B′ = Bδ, where δ = 1/Cd, be a regular Bohr set such that B1+3δ ≤ 1.01|B| and assume that A′ = A∩B satisﬁes µB′(A′) ≥ α and |A+A′| ≥ |A|/2α. Let 2 ≤ h ≤ log(1/α) be a real number. If A does not contain any nontrivial solutions to x +y + z = 3w, then there is a positive integer


- k ≤ ⌈log log(1/α8)/log h⌉ and a Bohr set T ⊆ B of rank at most d + d′ and radius at least cρα1/2hk−1/d4d′ log(1/α)1/logh,


where

d′ ≪ log log(1/α) + h−(k−1) log(1/α) 3 log(1/α) 1+2/logh such that 1A ∗ µT ∞ ≥ 107 α1−1/hk. Proo f. We apply Theorem 7 and Theorem 9 with A := −3 · A′, S := 3 · Bν′ , where ν ≤ 1/Cd, M := A and B1+3δ \ (A + A′) in place of L, and

![image 24](<2023-schoen-convex-equations_images/imageFile24.png>)

1 160

(log(1/α8))−1/logh.

ε =

![image 25](<2023-schoen-convex-equations_images/imageFile25.png>)

Observe that by regularity of B′ we have

2 α|3 · A′|.

|3 · A′ + S| ≤ |B1+′ ν| ≤

![image 26](<2023-schoen-convex-equations_images/imageFile26.png>)

By Theorem 7 there is a Bohr set B1 ⊆ S of rank at most d+d1 and radius at least cρεα1/2/d4d1, where d1 ≪ ε−2 log4(1/α) ≪ log(1/α) 4+2/logh such that

1−3·A′ ∗ 1A ∗ 1L ∗ µB1 − 1−3·A′ ∗ 1A ∗ 1L ∞ ≤ ε|A′||A|.

If 1A ∗ µB1 ∞ ≥ 107 α1−1/h the proof is concluded; otherwise, we will apply Theorem 9 with ε1 = ε and γ = 107 α1−1/h. Then there is a Bohr set B2 ⊆ S of rank d + d2 and radius at least

![image 27](<2023-schoen-convex-equations_images/imageFile27.png>)

![image 28](<2023-schoen-convex-equations_images/imageFile28.png>)

cρεα1/2h/d4d2, where

d2 ≪ ε−2 log2(14/5εα1/h)log(14/5α1/h)log(2/α) ≪ Cε−2 log2(3/εα1/h)log(3/α1/h)log(2/α) ≪ log log(1/α) + h−1 log(1/α) 3 log(1/α) 1+2/logh

such that 1−3·A′ ∗ 1A ∗ 1L ∗ µB2 − 1−3·A′ ∗ 1A ∗ 1L ∞ ≤ 3ε|A′||A|

![image 29](<2023-schoen-convex-equations_images/imageFile29.png>)

10 7

+18|A′|

α1−1/h|A|log |A + L − 3 · A′ + B1|

![image 30](<2023-schoen-convex-equations_images/imageFile30.png>)

![image 31](<2023-schoen-convex-equations_images/imageFile31.png>)

≤ 3ε|A′||A| + 18|A′| |A|log(36d|B|), the last inequality results from the assumption that α ≤ c0, and Lemma 5

|A + L − 3 · A′ + B1| ≤ |B3+3δ+3ν| ≤ |B4| ≤ 36d|B|.

We will apply the above procedure iteratively, and suppose that after k steps we obtain a Bohr set Bk ⊆ S of rank d + dk and radius

cρεα1/2hk−1/d4dk, where

dk ≪ log log(1/α) + h−(k−1) log(1/α) 3 log(1/α) 1+2/logh such that

1−3·A′ ∗ 1A ∗ 1L ∗ µBk − 1−3·A′ ∗ 1A ∗ 1L ∞ ≤ (2k − 1)ε|A′||A|

![image 32](<2023-schoen-convex-equations_images/imageFile32.png>)

+(2k−1 − 1)18|A′| |A|log |A + L − 3 · A′ + Bk−1| ≤ (2k − 1)ε|A′||A| + (2k−1 − 1)18|A′| |A|log(36d|B|),

![image 33](<2023-schoen-convex-equations_images/imageFile33.png>)

due to the inequality |A + L − 3 · A′ + Bk−1| ≤ |B4|. If 1A ∗ µBk ∞ ≥ 107 α1−1/hk the proof is concluded; otherwise, we will apply Theorem 9 with ε1 = ε and γ = 107 α1−1/hk. Thus, there is a Bohr set Bk+1 ⊆ S of rank d + dk+1 and radius

![image 34](<2023-schoen-convex-equations_images/imageFile34.png>)

![image 35](<2023-schoen-convex-equations_images/imageFile35.png>)

cρεα1/2h−k/d4dk+1, where

dk+1 ≪ C log log(1/α) + h−k log(1/α) 3 log(1/α) 1+2/logh such that

![image 36](<2023-schoen-convex-equations_images/imageFile36.png>)

1−3·A′ ∗1A∗1L∗µBk+1 −1−3·A′ ∗1A∗1L ∞ ≤ (2k+1−1)ε|A′||A|+(2k−1)18|A′| |A|log(36d|B|).

If for every k < l := ⌈log log(1/α8)/log h⌉ we have 1A ∗ µBk ∞ < 107 α1−1/hk then again by Theorem 9 there is a Bohr set Bl ⊆ S of rank d + dl and radius

![image 37](<2023-schoen-convex-equations_images/imageFile37.png>)

cρεα1/2hl−1/d4dl, where

dl ≪ log log(1/α) + h−(l−1) log(1/α) 3 log(2/α) log(2/α) 1+2/logh such that

![image 38](<2023-schoen-convex-equations_images/imageFile38.png>)

1−3·A′ ∗ 1A ∗ 1L ∗ µBl − 1−3·A′ ∗ 1A ∗ 1L ∞ ≤ (2l − 1)ε|A′||A| + (2l−1 − 1)18|A′| |A|log(36d|B|) ≤

1

![image 39](<2023-schoen-convex-equations_images/imageFile39.png>)

80|A′||A| + (2l − 1)18|A′| |A|log(36d|B|) ≤

![image 40](<2023-schoen-convex-equations_images/imageFile40.png>)

1 80|A′||A| + 20log(1/α)|A′| |A|log(36d|B|).

![image 41](<2023-schoen-convex-equations_images/imageFile41.png>)

![image 42](<2023-schoen-convex-equations_images/imageFile42.png>)

Next, we show that the last term of the right hand side of the above inequality does not exceed 1 80|A′||A|. Note that the inequalities

![image 43](<2023-schoen-convex-equations_images/imageFile43.png>)

1

1 1602

400(log(1/α))25d ≤ 2000α−2d ≤

1602 |A| and

α|B| ≤

![image 44](<2023-schoen-convex-equations_images/imageFile44.png>)

![image 45](<2023-schoen-convex-equations_images/imageFile45.png>)

1

400(log(1/α))2 log |B| ≤

1602 |A| hold provided that |B| ≥ (Cd/α)5 and C is large enough, hence

![image 46](<2023-schoen-convex-equations_images/imageFile46.png>)

1

80|A′||A| and therefore we have

20log(1/α)|A′||A|1/2 log1/2(64d+1|B|) ≤

![image 47](<2023-schoen-convex-equations_images/imageFile47.png>)

1 40|A′||A|.

1−3·A′ ∗ 1A ∗ 1L ∗ µBl − 1−3·A′ ∗ 1A ∗ 1L ∞ ≤

![image 48](<2023-schoen-convex-equations_images/imageFile48.png>)

The last step is treated diﬀerently as we now utilize the fact that A is a solution free set. Since there are only trivial solutions in A to x + y + z = 3w it follows that

1−3·A′ ∗ 1A ∗ 1L(0) = 1−3·A′ ∗ 1A ∗ 1B1+3δ(0) − 1−3·A′ ∗ 1A ∗ 1A+A′(0) = |A′||A| − |A′|. Thus

1 40|A′||A| ≥

- 19

![image 49](<2023-schoen-convex-equations_images/imageFile49.png>)

- 20|A′||A|,


1−3·A′ ∗ 1A ∗ 1L ∗ µBl(0) ≥ |A′||A| − |A′| −

![image 50](<2023-schoen-convex-equations_images/imageFile50.png>)

- as A is large enough, hence


0.501

- 19

![image 51](<2023-schoen-convex-equations_images/imageFile51.png>)

- 20|A′||A| ≤ |A′||L| 1A ∗ µBk ∞ ≤


α |A′||A| 1A ∗ µBl ∞, so

![image 52](<2023-schoen-convex-equations_images/imageFile52.png>)

9 5

1A ∗ µBl ∞ ≥

α. To complete the proof it is enough to observe that

![image 53](<2023-schoen-convex-equations_images/imageFile53.png>)

1

α−1/hl ≤ α−

8log(1/α) = 21/8 < 1.1 hence

![image 54](<2023-schoen-convex-equations_images/imageFile54.png>)

10 7

9 5

α1−1/hl and the assertion follows.

α ≥

1A ∗ µBl ∞ ≥

![image 55](<2023-schoen-convex-equations_images/imageFile55.png>)

![image 56](<2023-schoen-convex-equations_images/imageFile56.png>)

The density increment in the case |A + A′| ≤ |A|/2α will be proved by a similar reasoning, so we present the argument in a somewhat condensed form. Here, we do not even need the assumption that A does not contain any nontrivial solutions to the equation x + y + z = 3w.

- Lemma 11 Let B ⊆ Z/NZ be a regular Bohr set of rank d and radius ρ such that |B| ≥


(Cd/α)5, and let A ⊆ B has relative density c0 ≥ µB(A′) ≥ α, for some small constant c0 > 0, and suppose that |A + A′| ≤ |A|/2α. Let 2 ≤ h ≤ log(1/α) be a real number. Then there is a positive integer k ≤ ⌈log log(1/α8)/log h⌉ and a Bohr set T ⊆ B of rank at most d + d′ and radius at least

cρα1/2hk−1/d4d′ log(1/α)1/logh, where

d′ ≪ log log(1/α) + h−(k−1) log(1/α) 3 log(2/α) 1+2/logh such that 1A ∗ µBk ∞ ≥ 107 α1−1/hk. Proo f. Set S = Bν, where ν := 1/Cd, then by regularity of B we have

![image 57](<2023-schoen-convex-equations_images/imageFile57.png>)

2 α|A′|.

|A′ + S| ≤ |B1+ν| ≤

![image 58](<2023-schoen-convex-equations_images/imageFile58.png>)

We apply Theorem 7 and Theorem 9 with A := A′, the set S, M := A, L := −A − A′, and

1 40

(log(1/α8))−1/logh

ε =

![image 59](<2023-schoen-convex-equations_images/imageFile59.png>)

to get a Bohr set B1 ⊆ S of rank at most d + d1 and radius at lest cρεα1/2/d3d1, where d1 ≪ ε−2 log4(1/α) ≪ log(1/α) 4+2/logh such that

1A′ ∗ 1A ∗ 1L ∗ µB1 − 1A′ ∗ 1A ∗ 1L ∞ ≤ ε|A′||A|.

If 1A ∗ µB1 ∞ ≥ 107 α1−1/h the proof is concluded; otherwise, we will apply Theorem 9 with ε1 = ε and γ = 107 α1−1/h to get a Bohr set B2 of rank d + d2, where and radius at least

![image 60](<2023-schoen-convex-equations_images/imageFile60.png>)

![image 61](<2023-schoen-convex-equations_images/imageFile61.png>)

cρεα1/2h/d3d2, where

d2 ≪ log log(1/α) + h−1 log(1/α) 3 log(2/α) 1+2/logh such that

![image 62](<2023-schoen-convex-equations_images/imageFile62.png>)

1A′ ∗ 1A ∗ 1L ∗ µB2 − 1A′ ∗ 1A ∗ 1L ∞ ≤ 3ε|A′||A| + 18|A′| |A|log(36d|B|). After k iterations we obtain a Bohr set Bk of rank d + dk and radius

cρεα1/2hk−1/d3dk, where

dk ≪ log log(1/α) + h−(k−1) log(1/α) 3 log(2/α) 1+2/logh, such that

![image 63](<2023-schoen-convex-equations_images/imageFile63.png>)

1A′ ∗ 1A ∗ 1L ∗ µBk − 1A′ ∗ 1A ∗ 1L ∞ ≤ (2k − 1)ε|A′||A| + (2k−1 − 1)18|A′| |A|log(36d|B|). We will repeat this argument unless we achieve required density increment, but no more than

- l := ⌈log log(1/α8)/log h⌉ times. If we do not obtain required density increment for any k < l, then there is a there is a Bohr set Bl of rank d + dl and radius


cρεα1/2hl−1/d3dl, where

dl ≪ log log(1/α) + h−(l−1) log(1/α) 3 log(1/α) 1+2/logh such that

1

10|A′||A|. Clearly, 1A′ ∗ 1A ∗ 1L(0) = |A||A′|, so

1A′ ∗ 1A ∗ 1L ∗ µBl − 1A′ ∗ 1A ∗ 1L ∞ ≤

![image 64](<2023-schoen-convex-equations_images/imageFile64.png>)

- 9

![image 65](<2023-schoen-convex-equations_images/imageFile65.png>)

- 10|A||A′|,


1

20|A′||A| ≥ hence

1A′ ∗ 1A ∗ 1L ∗ µBl(0) ≥ |A||A′| −

![image 66](<2023-schoen-convex-equations_images/imageFile66.png>)

9 5

10 7

α1−1/hl. This concludes the proof.

1A ∗ µBl ∞ ≥

α ≥

![image 67](<2023-schoen-convex-equations_images/imageFile67.png>)

![image 68](<2023-schoen-convex-equations_images/imageFile68.png>)

The next lemma is quite standard; however, we cannot utilize its analogous version proven in [17] (Lemma 6.4). This is because in [17], it is proven for much smaller δ ≤ α/Cd, which is insuﬃcient for our approach and would not allow us to increase the exponent to 1/5 in the main result. It turned out, however, that only a minor modiﬁcation of the proof allows us to show the same thesis for a signiﬁcantly larger δ ≤ 1/Cd.

- Lemma 12 Let B be a regular Bohr set of rank d, let A ⊆ B has relative density µB(A) = α.


- Let C > 0 be a constant such that |B| ≥ (1 − 201 )|B1+δ|, δ = 1/Cd and let B′,B′′ ⊆ Bδ. Then either:


![image 69](<2023-schoen-convex-equations_images/imageFile69.png>)

- 1. there is an x such that 1A ∗ µB′(x) ≥ 108 α and 1A ∗ µB′′(x) ≥ 108 α; or

![image 70](<2023-schoen-convex-equations_images/imageFile70.png>)

![image 71](<2023-schoen-convex-equations_images/imageFile71.png>)

- 2. 1A ∗ µB′ ∞ ≥ 1.1α, or 1A ∗ µB′′ ∞ ≥ 1.1α.


Proo f. Since A + B′,A + B′′ ⊆ B1+δ it follows that

hence

x∈B1+δ

Thus, for some x we have

1A ∗ µB′′(x) = |A|,

1A ∗ µB′(x) =

x∈B1+δ

x∈B1+δ

1A ∗ µB′(x) + 1A ∗ µB′′(x) = 2|A|.

1 10

1A ∗ µB′(x) + 1A ∗ µB′′(x) ≥ 2|A|/|B1+δ| = 2α|B|/|B1+δ| ≥ 2 −

![image 72](<2023-schoen-convex-equations_images/imageFile72.png>)

α.

If 1A ∗ µB′ ∞, 1A ∗ µB′′ ∞ < 1.1α then

1 10

1A ∗ µB′(x),1A ∗ µB′′(x) ≥ 2 −

![image 73](<2023-schoen-convex-equations_images/imageFile73.png>)

8 10

α,

α − 1.1α =

![image 74](<2023-schoen-convex-equations_images/imageFile74.png>)

and the proof is completed. Now, we are in position to prove the main result of this section.

- Proposition 13 Let B ⊆ Z/NZ be a regular Bohr set of rank d and radius ρ, and let A ⊆ B


has relative density c0 ≥ µB(A) ≥ α. Assume that |B| ≥ (Cd/α)5d. Let 2 ≤ h ≤ log(2/α) be a real number. If A does not contain any nontrivial solutions to x + y + z = 3w then there exist a positive integer k ≤ ⌈log log(1/α9)/log h⌉ and a Bohr set T ⊆ B of rank at most d + d′ and radius at least

cρα1/2hk−1/d5d′ log(1/α) 1/logh, where

d′ ≪ log log(1/α) + h−(k−1) log(1/α) 3 log(1/α) 1+2/logh such that 1A ∗ µT ∞ ≥ α1−1/hk.

Proo f. We chose constants c′,c′′ ∈ [1/2,1] such that the Bohr sets B′ = Bδ′ and B′′ = Bδ′′′, where δ′ = c′/100d and δ′′ = c′′/100d, are regular and |B1+3δ| ≤ 1.01|B|. If the second conclusion of Lemma 12 holds then we have

1A ∗ µB′ ∞ ≥ 1.1α or 1A ∗ µB′′ ∞ ≥ 1.1α.

Clearly, the Bohr sets B′ and B′′ have rank d and radius at least cρ/d2. In this case we can take k = ⌈log log(1/α8)/log h⌉ to get the required inequalities. Indeed, for such choice of k we have

α1−1/hk ≤ 21/9α < 1.1α. If the ﬁrst conclusion of Lemma 12 holds then for some x ∈ B we have a1 := 1A ∗ µB′(x) ≥

8 10

8 10

α and α2 := 1A ∗ µB′′(x) ≥

α,

![image 75](<2023-schoen-convex-equations_images/imageFile75.png>)

![image 76](<2023-schoen-convex-equations_images/imageFile76.png>)

and by the above, we can assume that α1,α1 ≤ 1.1α. In order to apply Lemma 10 and Lemma 11, it is necessary to ensure that both α1 and α2 do not exceed c0. If this is not the case, we ﬁnd a subset A1 ⊆ A such that

7 10

7 10

α and c0 ≥ 1A1 ∗ µB′′(x) ≥

α.

c0 ≥ 1A1 ∗ µB′(x) ≥

![image 77](<2023-schoen-convex-equations_images/imageFile77.png>)

![image 78](<2023-schoen-convex-equations_images/imageFile78.png>)

Since we have |B′| ≥ 2 by assumption, the Cauchy-Davenport theorem yields

⌊100/c′′⌋ 2 |B′′| ≥ 25|B′′|. (9)

|B′| ≥ |⌊100d/c′′⌋B′′| ≥ ⌊100d/c′′⌋|B′′| − ⌊100d/c′′⌋ + 1 ≥

![image 79](<2023-schoen-convex-equations_images/imageFile79.png>)

- Let U′ ⊆ (A − x) ∩ (B′ \ B′′) and U′′ ⊆ (A − x) ∩ B′′ be arbitrary subsets such that |U′′| = max 0,(α2 − c0)|B′′| and |U′| = max 0,(α1 − c0) |B′| − |U′′|. We show that A1 can be taken


- as A \ (U′ ∪ U′′). Indeed, we have


8 10

α and due to (9)

c0 ≥ 1A1 ∗ µB′′(x) = α2 − max 0,(α2 − c0) ≥

![image 80](<2023-schoen-convex-equations_images/imageFile80.png>)

1 25

α2 − max 0,(α2 − c0) ≥

c0 ≥ 1A1 ∗ µB′(x) = α1 − max 0,(α1 − c0) −

![image 81](<2023-schoen-convex-equations_images/imageFile81.png>)

8 10

1 25

7 10

α −

1.1α ≥

α.

![image 82](<2023-schoen-convex-equations_images/imageFile82.png>)

![image 83](<2023-schoen-convex-equations_images/imageFile83.png>)

![image 84](<2023-schoen-convex-equations_images/imageFile84.png>)

We put A′ := (A1 − x) ∩ B′,A′′ := (A1 − x) ∩ B′′ and observe that A′ is solution free to the equation x + y + z = 3w.

If |A′ + A′′| ≥ |A′|/2λ, where λ := 107 α then by Lemma 10 applied with

![image 85](<2023-schoen-convex-equations_images/imageFile85.png>)

2 ≤ h ≤ log(1/λ) ≤ log(2/α) there is a Bohr set T of rank d + d′ and radius at least

c(ρ/C′d)λ1/2hk−1/d4d′ log(1/λ) 1/logh ≫ ρα1/2hk−1/d5d′ log(1/α) 1/logh,

with

d′ ≪ log log(1/λ) + h−(k−1) log(1/λ) 3 log(1/λ) 1+2/logh

≪ log log(1/α) + h−(k−1) log(1/α) 3 log(1/α) 1+2/logh for some k ≤ ⌈log log(1/λ8)/log h⌉ ≤ ⌈log log(1/α9)/log h⌉ such that

10 7

λ1−1/hk ≥ α1−1/hk.

1A ∗ µT ∞ ≥ 1A′ ∗ µT ∞ ≥

![image 86](<2023-schoen-convex-equations_images/imageFile86.png>)

If |A′ + A′′| ≤ |A′|/2λ, then by Lemma 11 there is a Bohr set T of rank d + d′ and radius

- at least c(ρ/C′C′′d2)α1/2hk−1/d3d′ log(1/α) 1/logh ≫ ρα1/2hk−1/d5d′ log(1/α) 1/logh,


with

d′ ≤ C log log(1/α) + h−(k−1) log(1/α) 3 log(2/α) 1+2/logh for some k ≤ ⌈log log(1/λ8)/log h⌉ ≤ ⌈log log(1/α9)/log h⌉ such that

10 7

λ1−1/hk ≥ α1−1/hk.

1A ∗ µT ∞ ≥ 1A′ ∗ µT ∞ ≥

![image 87](<2023-schoen-convex-equations_images/imageFile87.png>)

Remark Notice that the density increment obtained in Proposition 13 is always at least α−1/hl ≥ 21/9h. (10)

Let us also refer to a similar lemma from [3]. Despite implying weaker result than Proposition 13, we will also apply it in the case of α > c0.

- Proposition 14 Let B ⊆ Z/NZ be a regular Bohr set of rank d and radius ρ, and let A ⊆ B has


relative density µB(A) ≥ α. Assume that |B| ≥ (Cd/α)3d. If A does not contain any nontrivial solutions to x + y + z = 3w then there exist a Bohr set T ⊆ B of rank at most d + d′ and radius

- at least ρα3/2/d5d′, where d′ ≪ log4(2/α) such that 1A ∗ µT ∞ ≥ 45α.


![image 88](<2023-schoen-convex-equations_images/imageFile88.png>)

2. Proof of Theorem 4

Now, we iteratively apply the Proposition 13 and Proposition 14 to prove Theorem 4. We start with A0 = A,B0 = Z/NZ, so d0 = 1,ρ0 = 2 and α0 = α. We will apply the following iteration scheme as long as it is possible.

If |Bi| ≥ (Cdi/αi)5di and αi ≤ c0, then we apply Proposition 13 with hi := exp( log log(1/αi)) (11)

![image 89](<2023-schoen-convex-equations_images/imageFile89.png>)

to get a Bohr set Bi+1 ⊆ Bi of rank di+1, radius ρi+1 and a positive integer

ki ≤ ⌈log log(2/αi)/log hi⌉ such that

di+1 ≤ di + C log log(1/αi) + h−i (ki−1) log(1/αi) 3 log(2/αi) 1+2/loghi, (12)

(ki−1) i

ρr+1 ≥ cρiα1/2h

i /d5i di+1(log 1/αi)1/loghi, (13) and a set Ai+1 = (Ai − xi) ∩ Bi+1 of relative density on Bi+1

ki i

αi+1 ≥ α1−1/h

i . (14)

Let us here recall that our equation is translation invariant, so (Ai − x) ∩ Bi+1 for any x is still free of solutions to our equation.

If |Bi| ≥ (Cdi/αi)5di but αi > c0, then we apply Proposition 14 to get a Bohr set Bi+1 ⊆ Bi

- of rank di+1 and radius ρi+1 such that di+1 ≤ di + C log4(2/αi), (15)


ρr+1 ≥ cρiα3i/2/d5i di+1, (16) and a set Ai+1 = (Ai − xi) ∩ Bi+1 of relative density on Bi+1

5 4

αi+1 ≥

αi. (17)

![image 90](<2023-schoen-convex-equations_images/imageFile90.png>)

Note that because αi > c0, we can apply Proposition 14 only a constant number of times. Since the density is naturally bounded from above by 1 and the growth of αi, by (10) and

(11), in each step is at least by the factor

1 9 exp(

√

![image 91](<2023-schoen-convex-equations_images/imageFile91.png>)

![image 92](<2023-schoen-convex-equations_images/imageFile92.png>)

2

loglog(1/α)), so after

![image 93](<2023-schoen-convex-equations_images/imageFile93.png>)

s ≪ log(1/α)exp( log log(1/α))

iterations we will be not able to continue this process. This implies that the condition |Bs| ≥ (Cd/αs)5ds must be violated. Let t be the number of steps where we applied Proposition 13, clearly s − t = O(1). Thus, by Lemma 5 we have

ρdssN < (Cds/αs)5ds, so

N < (Cds/ρsαs)5ds (18) Observe that by (14)

α ti=0−1(1−1/hkii) ≤ c0,

hence

t−1

(1 − 1/hkii) ≫ log−1(1/α). Together with the inequality 1 − 1/x < e−x this yields

i=0

t

1/hkii ≪ log log(1/α). (19)

i=0

Since

![image 94](<2023-schoen-convex-equations_images/imageFile94.png>)

1/hi ≥ exp(− log log(1/α)) for every i, it follows from (19) that

t

t

1/hiki−1, so

1/hkii ≥ exp(−2 log log(1/α))

![image 95](<2023-schoen-convex-equations_images/imageFile95.png>)

i=0

i=0

t

1/hkii−1 ≪ exp(2 log log(1/α)). (20) Therefore, by (12), (15) and (20) we infer that

![image 96](<2023-schoen-convex-equations_images/imageFile96.png>)

i=0

t

log log(1/αi) + hi−(ki−1) log(1/αi) 3(log4(1/αi))4+2/loghi + (s − t)log4(2/α)

ds ≪

i=0

t

≪ t log log(1/α) 3 +

h−i 3(ki−1)(log4(1/αi))4+2/loghi + (s − t)log4(2/α) ≪ log4(2/α)exp(C log log(1/α)).

i=0

![image 97](<2023-schoen-convex-equations_images/imageFile97.png>)

In view of (13), (16) and (20) we have

ρs ≥ csα ti=0 1/2hiki−1+23(s−t)/( d6i )(log 1/αi)s/loghi ≥ csαC exp(2

![image 98](<2023-schoen-convex-equations_images/imageFile98.png>)

√

![image 99](<2023-schoen-convex-equations_images/imageFile99.png>)

log log(1/α))/(log(1/α))C log(1/α) ≥ cαC′ exp(2

√

![image 100](<2023-schoen-convex-equations_images/imageFile100.png>)

log log(1/α)). Inserting the above estimates to (18) we get

N ≤ exp(C log5(1/α)exp(C log log(1/α)), and the assertion follows.

![image 101](<2023-schoen-convex-equations_images/imageFile101.png>)

3. Concluding remarks

It is conjectured in [8] that if µG(A) = α then 2A−2A contains a Bohr set of rank C log(1/α) and radius αC. Theorem 7 is closely related to Bogolyubov-type results, as seen in [14]. The

currently best estimate of rank of the Bohr set in Bogolyubov’s lemma is due to Sanders [14] and is bounded from above by C log4(2/α). However, any improvement in Theorem 7 leads to a better estimate in Bogolyubov’s lemma. This provides some support for the conjecture that in Theorem 7, we can replace roughly C log4(2/α) with C log(2/α). Assuming this conjecture is true and using our method we would obtain the upper bound

|A| ≪ exp − c(log N)1/2−o(1) N

for any set A ⊆ {1,... ,N} without nontrivial solutions to x + y + z = 3w, which essentially matches Behrend’s lower bound.

Since Theorem 7 is also a crucial component of the proof of the Kelley-Meka theorem, a natural question arises whether the argument presented in this work, based on Theorem 9, can be applied in the proof of the Kelley-Meka theorem. However, Theorem 7 is not employed directly on the set A in the proof of the Kelley-Meka theorem. Instead, it is applied to sets of the form X = (A + s1) ∩ ··· ∩ (A + sp), which have signiﬁcantly lower density. The application of Theorem 9 would only lead to a relatively minor increase of the density of the set X, which seems to be of marginal relevance.

# References

- [1] F. A. Behrend, On sets of integers which contain no three terms in arithmetical progression, Proc. Nat. Acad. Sci. U. S. A. 32, (1946). 331–332.
- [2] S. Bernstein, Die Wahrscheinlichkeitsrechnung, (Russian). Moskau-Leningrad: Staatsverlag (Lehrbu¨cher fu¨r Hochschulen), 1927.
- [3] T. Bloom, O. Sisask, An improvement to the Kelley-Meka bounds on three-term arithmetic progressions, arXiv:2309.02353.
- [4] T. Bloom, O. Sisask, The Kelley–Meka bounds for sets free of three-term arithmetic progressions, arXiv:2302.07211.
- [5] J. Bourgain, On triples in arithmetic progression, Geom. Funct. Anal. 9 (1999) 968–984.
- [6] E. Croot, O. Sisask, A probabilistic technique for ﬁnding almost-periods of convolutions, Geom. Funct. Anal. 20 (2010), 1367–1396.
- [7] M. Elkin, An Improved Construction of Progression-Free Sets, Israel J. Math. 184 (2011), 93–128.
- [8] B. Green and T. Tao, Freiman’s theorem in ﬁnite ﬁelds via extremal set theory, Combin. Probab. Comput. 18 (2009), 335–355.
- [9] B. Green and J. Wolf, A note on Elkin’s improvement of Behrend’s construction, in Additive Number Theory (Springer, New York, 2010), 141–144.
- [10] A. Kelley, R. Meka, Strong bounds for 3-progressions, arXiv:2302.05537.


- [11] T. Ko´sciuszko, Counting solutions to invariant equations in dense sets, arXiv:2306.08567.
- [12] K. F. Roth, On certain sets of integers, J. London Math. Soc. 28 (1953), 104–109.
- [13] I. Ruzsa, Solving a linear equation in a set of integers. I. Acta Arith. 65 (1993), 259–282.
- [14] T. Sanders, On the Bogolubov–Ruzsa Lemma, Anal. PDE 5 (2012), 627–655.
- [15] T. Schoen, Improved bound in Roth’s theorem on arithmetic progressions, Adv. Math. 386

(2021), Paper No. 107801, 20 pp.

- [16] T. Schoen, I. D. Shkredov, Roth’s theorem in many variables, Israel J. Math. 199 (2014), 287–308.
- [17] T. Schoen, O. Sisask, Roth’s theorem for four variables and additive structures in sums of sparse sets, Forum Math. Sigma 4 (2016), e5, 28 pp.
- [18] T. Tao, V. Vu, Additive combinatorics, Cambridge University Press 2005.


