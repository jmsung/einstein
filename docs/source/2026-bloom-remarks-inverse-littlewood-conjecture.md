---
type: source
kind: paper
title: Remarks on the inverse Littlewood conjecture
authors: Thomas F. Bloom, Ben Green
year: 2026
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2602.16482v2
source_local: ../raw/2026-bloom-remarks-inverse-littlewood-conjecture.pdf
topic: general-knowledge
cites:
---

# arXiv:2602.16482v2[math.NT]18Apr2026

## REMARKS ON THE INVERSE LITTLEWOOD CONJECTURE

THOMAS F. BLOOM AND BEN GREEN

Abstract. The Littlewood conjecture, proven by Konyagin and McGeheePigno-Smith in the 1980s, states that if A ⊂ Z is a finite set of integers with |A| = N then ∥ 1A∥1 ⩾ c log N for some absolute constant c > 0. We explore what structure A must have if ∥ 1A∥1 ⩽ K log N for some constant K. Under such an assumption we prove, for instance, that A contains a subset A′ ⊆ A with |A′| ⩾ N0.99 such that |A′ +A′| ≪ KO(1)|A′|. As a consequence, for any k ⩾ 3, if N is sufficiently large depending on k and K, then A must contain an arithmetic progression of length k. A byproduct of our analysis is a (slightly) improved bound for the constant c.

1. Introduction

For a finite set A ⊂ Z the Fourier transform 1A : R/Z → C is defined by 1A(θ) = n∈A e(−nθ), where e(x) := e2πix. Define

1

∥ 1A∥1 =

| 1A(θ)|dθ.

0

A famous conjecture of Littlewood stated that1 ∥ 1A∥1 ≫ log N for any set A of N integers, which is achieved for example by an arithmetic progression of length N. This was proved in 1981 independently by Konyagin [11] and McGehee, Pigno, and Smith [12]. A discussion of the problem and its history may be found in [3, Chapter 10].

This lower bound is universal, yet rarely achieved – in fact generically we expect ∥ 1A∥1 to be closer to the trivial upper bound N1/2, which is an immediate consequence of the Cauchy-Schwarz inequality and Parseval’s identity. This is achieved when A is lacunary, for example, or a random positive density subset of an interval (with high probability). In fact, the only examples we know that achieve O(log N) are arithmetic progressions and simple variations, for example the union of O(1) arithmetic progressions and some small unstructured set.

It is therefore natural, especially from the viewpoint of modern additive combinatorics, to ask the following inverse question. Question 1.1. Let K > 0 be some large constant. What can we say about the structure of sets A ⊂ Z with |A| = N and ∥ 1A∥1 ⩽ K log N?

This question was asked by the second author [6] and one possible precise conjecture in this direction was formulated by Petridis [13, Question 5.1] (see Section 6 for further details). While we are some way from a full resolution of this question, in this paper we offer the following weak partial progress.

1We use the Vinogradov notation f ≫ g, equivalent to g = O(f), to denote the existence of some absolute constant c > 0 such that |f(x)| ⩾ c |g(x)| for all sufficiently large x.

1

Recall that the additive energy E(B) of a finite set B ⊂ Z is defined by

E(B) = #{(b1,b2,b3,b4) ∈ B4 : b1 + b2 = b3 + b4}. (1.1) We have

1

| 1B(θ)|4dθ, (1.2)

E(B) =

0

as can be checked using the orthogonality relation for characters. We also write ω[B] := E(B)/|B|3 for the normalised additive energy of B, which satisfies 0 < ω[B] ⩽ 1.

Theorem 1.2. Let N be a sufficiently large positive integer. Let δ ∈ (0, 12] and K > 0. If A is a set of N integers such that ∥ 1A∥1 ⩽ K log N then there is a subset A′ ⊆ A of size |A′| ≫ N1−δ such that ω[A′] ≫ (δ/K)2.

The set A′ produced in Theorem 1.2 is in fact an initial segment of A . The following two corollaries are almost immediate consequences of this and

standard results in additive combinatorics.

- Corollary 1.3. Let N be a sufficiently large positive integer. Let K > 0 and

suppose that A ⊂ Z is a finite set of size N such that ∥ 1A∥1 ⩽ K log N. Then there exists an arithmetic progression P of length ⩾ Nc

K

such that |A ∩ P| ⩾ cK |P|, where cK > 0 depends only on K.

Proof. Apply Theorem 1.2 with δ = 12. Applying the Balog-Szemer´edi-Gowers theorem (see, for example, [16, Theorem 2.31]) to the resulting set A′, we obtain a set

A′′ ⊆ A, |A′′| ≫ K−O(1)N1/2, with |A′′ + A′′| ⩽ KO(1)|A′′|. By the Freiman-Ruzsa theorem (see, for example [16, Theorem 5.33]), there are arithmetic progressions P1,...,Pr with r = OK(1) such that A′′ ⊆ P1 + ··· + Pr and

|P1 + ··· + Pr| = |P1|···|Pr| ≪K |A′′|. By averaging there exists some i, 1 ⩽ i ⩽ r, and x such that

|(Pi + x) ∩ A′′| ≫K |Pi| ≫K |A′′|1/r . Since N is large, the length of Pi is bounded below by Nc

K

for some cK > 0. □

- Corollary 1.4. Let K > 0 and let k ⩾ 3 be an integer. Let N be sufficiently large


in terms of k,K and let A ⊂ Z be a finite set of size N such that ∥ 1A∥1 ⩽ K log N. Then A contains an arithmetic progression of length k.

Proof. This follows immediately from Corollary 1.3 and Szemer´edi’s theorem. □

Remark. The key feature of Theorem 1.2 is that the lower bound on E(A′) is a constant times |A′|3. If one is prepared to tolerate logarithmic losses then a one line application of H¨lder’s inequality on the Fourier side shows that we in fact have E(A) ⩾ N3/(K log N)2. However, this would certainly be too weak to deduce Corollary 1.4 given our current knowledge of bounds in Szemer´edi’s theorem when k ⩾ 4.

- 1.1. Previous structural results. We now summarise what was previously known concerning this inverse question for sets with small ∥ 1A∥1.

- • As noted above, it is a trivial consequence of H¨lder’s inequality that A itself must have reasonably large additive energy: E(A) ⩾ N3/(K log N)2.
- • Pichorides [14, Lemma 3] noted that an argument of Zygmund [18, Chapter XII, 7.6] implies that the largest dissociated2 subset of A has size OK((log N)3). This was independently rediscovered by Bedert [1].
- • Petridis [13] showed that A cannot have genuine 3-dimensional structure, in a certain precise sense.
- • Picking up on the theme of Petridis, Hanson [8] showed that A cannot have genuine 2-dimensional structure, again in a sense he was able to make precise.
- • If we replace the upper bound ⩽ K log N with ⩽ K, and replace Z with a finite abelian group G, then a much more satisfactory answer is known: the second author and Sanders [7] have shown that if A ⊆ G has ∥ 1A∥1 ⩽ K then 1A can be written as a simple linear combination of OK(1) indicator functions of cosets of subgroups of G. This condition is (qualitatively) necessary and sufficient.


Part of the motivation for inverse results of this nature originated in work of Bourgain [2], which highlighted a connection between Littlewood’s conjecture and the task of improving the lower bounds for the sum-free subset problem in additive combinatorics. Bedert [1] has made significant progress on this problem recently, making use of that connection.

- 1.2. Bounds for the Littlewood conjecture. The lower bound ∥ 1A∥1 ≫ log N is the best possible up to an absolute constant, since this is achieved when A is an arithmetic progression of length N. In this case, one may compute (see, for example, [18, II.12.1]) that


4 π2

∥ 1A∥1 =

log N + O(1).

One may ask (and Hardy and Littlewood did ask [9, p 167]) whether this leading constant is the best possible or even whether ∥ 1A∥1 ⩾ ∥ 1P∥1 where P is an arithmetic progression of length N. This statement, or the slightly weaker statement that ∥ 1A∥1 ⩾ (π42 − o(1))log N, is usually called the Strong Littlewood Conjecture.

Less ambitiously, one can seek to prove the best possible value of c in an inequality

∥ 1A∥1 ⩾ (c − o(1))log N. The argument of McGehee, Pigno, and Smith [12] achieved c = 1/30. The numerics were optimised by Stegeman [15] and Yabuta [17], the latter proving a value of c ≈ 0.1295. We give a slight improvement on this constant.

Theorem 1.5. If A ⊂ Z is a finite set of size N then

∥ 1A∥1 ⩾ (c − o(1))log N where c = 0.170934···.

2A set X ⊂ Z is dissociated if all 2|X| subset sums are distinct.

For comparison note that 4/π2 ≈ 0.405 so we are still about a factor of 2.4 away from the conjectured optimal value. The value of c is found as the maximum of a complicated two-variable expression and presumably has no nicer form.

The proofs of Theorems 1.2 and 1.5 both hinge on a detailed analysis of the test functions used by McGehee, Pigno, and Smith. This is the main business of the paper.

In the final section of the paper we make some additional comments and record some further questions and conjectures.

Notation. For any function f ∈ ℓ1(Z) we define the Fourier transform f : [0,1] → C by

f(n)e(−nθ),

f(θ) =

n

where e(x) = e2πix. The convolution is defined in the usual way, so that if f,g ∈ ℓ1(Z) then

f ∗ g(x) =

f(y)g(x − y).

y

Note that if A = supp(f) and B = supp(g) then supp(f ∗ g) ⊆ A + B. We note here the useful property that f ∗ g = f · g. It is convenient to use inner product notation, so that if f,g : Z → C we write

⟨f,g⟩ =

f(n)g(n),

n∈Z

and ⟨ f, g⟩ = 0 1 f(θ) g(θ)dθ. By Parseval’s identity

⟨f,g⟩ = ⟨ f, g⟩.

Acknowledgements. TB is supported by a Royal Society University Research Fellowship. BG is supported by a Simons Investigator award. We thank Benjamin Bedert for many insightful and productive discussions concerning the inverse Littlewood problem, and the referee for observing that a minor modification to the argument gives a larger value of c than we had originally claimed.

2. McGehee-Pigno-Smith test functions The overall strategy to prove Theorem 1.2 is to mimic proofs of the Littlewood

conjecture, aiming to prove a lower bound of the shape ∥ 1A∥1 > K log N. Since this lower bound is false by assumption, some stage in our purported proof must fail, which will reveal structural information about A.

All proofs of the Littlewood conjecture follow a similar strategy, obtaining a

lower bound for ∥ 1A∥1 via construction of a suitable test function. In particular, our goal will be to try to construct a test function R : Z → C such that

- (1) ∥ R∥∞ ⩽ 1 and
- (2) ⟨1A,R⟩ > K log N.


By Parseval’s identity and the triangle inequality these facts combined imply ∥ 1A∥1 >

K log N. This contradicts our hypothesis, so the construction of such a test function must fail. The new observation is that, examining the details of the construction of the test function, this yields some additive information about A.

We will use the test functions of McGehee, Pigno, and Smith [12]. These are not the only ones capable of proving the Littlewood conjecture but, of the ones

we are aware of, they perform the best from the quantitative point of view. For a discussion of other possible test functions we refer to the survey paper of Fournier [4].

The following lemma details the construction of these test functions.

- Lemma 2.1. Let b > 0 and set c = 1 − e−b. If f : Z → R is a finitely supported


function then there exists a function Rf : Z → C (which depends on b) with the following properties:

- (1) Rf is supported on Z⩽0;
- (2) ∥Rf∥2 ⩽ 21/2b∥f∥2;
- (3) ∥ Rf + 1∥∞ ⩽ 1; and
- (4) if ∥ f∥∞ ⩽ 1 then, for any g : Z → C with ∥ g∥∞ ⩽ 1, the function h := g + cf + g ∗ Rf


satisfies ∥ h∥∞ ⩽ 1. Proof. Since | f| is a 1-periodic symmetric function we can write | f(θ)| =

cne(nθ)

n∈Z

for some cn ∈ R with cn = c−n, and define hf : Z → C by

 

c0 if n = 0 2cn if n < 0, and 0 otherwise,

hf(n) =



so that hf is supported on Z⩽0. Furthermore, since hf(θ) = c0 + 2

cne(nθ),

n<0

for any θ ∈ R/Z we have ℜ hf(θ) = c0 +

cn(e(nθ) + e(−nθ)) = | f(θ)| ⩾ 0.

n<0

By Parseval’s theorem, ∥hf∥22 = c20 + 2

c2n ⩽ 2

c2n = 2∥f∥22.

n

n̸=0

We may now define

(−b)j j!

h(fj)(n),

Rf(n) =

j⩾1

where h(fj) = hf ∗ ··· ∗ hf denotes the j-fold convolution. Equivalently, we may define Rf via its Fourier transform by

(−b)j j!

hf(θ)j = e−b h

f(θ) − 1.

Rf(θ) =

j⩾1

Since supp(g1 ∗ g2) ⊆ supp(g1) + supp(g2) for any pair of functions g1,g2 : Z → C, it is clear that Rf is supported on Z⩽0, which is item (1).

The inequality |e−z − 1| ⩽ |z|, valid whenever ℜz ⩾ 0, implies

| Rf(θ)| ⩽ b| hf(θ)| pointwise, and hence in particular

∥Rf∥2 ⩽ b∥hf∥2 ⩽ 21/2b∥f∥2 , which is item (2). We also have

f(θ) = e−b| f(θ)| ⩽ 1 pointwise, which is (3).

| Rf(θ) + 1| = e−bℜ h

Finally, suppose ∥ f∥∞,∥ g∥∞ ⩽ 1 and consider

h = cf + g + g ∗ Rf, where c = 1 − e−b. Taking the Fourier transform, we have the pointwise inequality

| h| ⩽ | g||1 + Rf| + c| f| ⩽ e−b| f| + (1 − e−b)| f| ⩽ 1, which is (4). In the final step here we used the inequality e−bx + (1 − e−b)x ⩽ 1, which is valid for all x with 0 ⩽ x ⩽ 1. □

The form of item (4) lends itself to an iterative argument, the details of which are as follows.

- Lemma 2.2. Let b > 0 and c = 1 − e−b. Let J ∈ N and suppose that g1,...,gJ : Z → R are finitely supported functions such that ∥ gi∥∞ ⩽ 1 for all i = 1,...,J. Then there exists a test function R : Z → C such that ∥ R∥∞ ⩽ 1 and


J

J

R = c

Dj, (2.1)

gj +

j=1

j=1

where the function Dj has the shape Dj = c

gi ∗ Fij, (2.2)

1⩽i<j

where

∥Fij∥2 ⩽ 21/2b∥gj∥2 , (2.3)

and Fij is supported on Z⩽0. Proof. We iteratively define functions Ri : Z → C by R1 := cg1 and

Ri+1 := Ri + cgi+1 + Di+1 for i ⩾ 1, where

Di+1 := Ri ∗ Rgi+1

. (Here Rgi+1

is the test function given by Lemma 2.1 with f = gi+1.) We then set R = RJ. The fact that R has the form (2.1) is a trivial induction.

By the final property of Lemma 2.1 and a trivial induction, we have ∥ Ri∥∞ ⩽ 1 for all i. A downwards induction on i using the identity

Ri = c gi + Ri−1( Rgi

+ 1) yields, for any i < j,

Rj = c

gk

i<k⩽j

( Rgℓ

k<ℓ⩽j

+ 1) + Ri

( Rgℓ

+ 1),

i<ℓ⩽j

where the product over k < ℓ ⩽ j is interpreted as 1 when k = j. In particular, taking i = 1 we have

Rj = c

( Rgℓ

gi

+ 1).

1⩽i⩽j

i<ℓ⩽j

From the definition of Dj it then follows that Dj = Rj−1 Rgj

gi Rgj

( Rgℓ

= c

+ 1).

1⩽i<j

i<ℓ<j

Defining

Fij := Rgj

( Rgℓ

+ 1),

i<ℓ<j

we see that (2.2) holds.

The bound (2.3) now follows using Lemma 2.1 (2) and (3) and Parseval’s identity ∥ Fij∥2 = ∥Fij∥2. To see that Fij is supported on Z⩽0, observe that Fij is a sum of convolutions of functions Rgℓ

, and each such function is supported on Z⩽0 by Lemma 2.1 (1). □

3. A lower bound for ∥ 1A∥1

We will now apply the McGehee-Pigno-Smith test function from the previous section to prove the following technical proposition. It will be the key input in the proof of our two main results, Theorems 1.2 and 1.5. An initial segment of A is a non-empty subset of the shape A ∩ (−∞,x] for some x ∈ R.

Proposition 3.1. Let b > 0 be a real parameter, and let J ∈ N. Let A ⊂ Z be a finite set and suppose that A1,...,AJ are initial segments of A with A1 ⊆ ··· ⊆ AJ. Let λ > 1 be a parameter, and suppose that |Aj+1| ⩾ λ|Aj| for j = 1,...,J − 1. Then

J

b √

(ω[Ai] + |Ai|−1)1/2 , where ω[·] denotes the normalised additive energy. Proof. For j = 1,...,J, let µj = |A1

∥ 1A∥1 ⩾ (1 − e−b) J −

λ − 1

i=1

. Then ∥µj∥1 = 1 and ∥ µj∥∞ ⩽ 1. Let R be the associated McGehee-Pigno-Smith test function given by Lemma 2.2, with parameter b, so that ∥ R∥∞ ⩽ 1 and

j|1A

j

J

J

R = c

µj +

Dj,

j=1

j=1

where c = 1 − e−b. Since ⟨µj,1A⟩ = 1 for all j, we deduce that ∥ 1A∥1 ⩾ |⟨R,1A⟩| ⩾ cJ −

⟨Dj,1A⟩ . (3.1)

j

It therefore suffices to prove an upper bound on j⟨Dj,1A⟩ of sufficient quality. By (2.2) we have Dj = c i<j µi ∗ Fij, and so

J

⟨Dj,1A⟩ = c

⟨1A,µi ∗ Fij⟩. (3.2)

1⩽i<j⩽J

j=1

### Since Fij is supported on Z⩽0, from the nesting property of the Ai we have ⟨1A,µi ∗ Fij⟩ = ⟨1A

i ∗ µ◦i ,Fij⟩, where g◦(x) := g(−x). Moreover by (2.3) we have

,µi ∗ Fij⟩ = ⟨1A

i

∥Fij∥2 ⩽ 21/2b∥µj∥2 = 21/2b|Aj|−1/2 . By the Cauchy-Schwarz inequality, we thus have, recalling that Fij is supported on Z⩽0,

i ∗ µ◦i ,Fij⟩ ⩽ 21/2b|Aj|−1/2 (1A

i ∗ µ◦i )1Z

⟨1A,µi ∗ Fij⟩ = ⟨1A

⩽0 2. (3.3) However one may compute that

⩽0∥2 = |Ai|−1

i ∗ µ◦i )1Z

∥(1A

E(Ai) + |Ai|2 2

1/2

.

Combining this with (3.2) and (3.3) yields

J

(E(Ai) + |Ai|2)1/2 |Ai||Aj|1/2

⟨Dj,1A⟩ ⩽ cb

.

1⩽i<j⩽J

j=1

Substituting into (3.1) gives

J

(E(Ai) + |Ai|2)1/2 |Ai| i<j⩽J

|Aj|−1/2 .

∥ 1A∥1 ⩾ (1 − e−b) J − b

i=1

By the assumption in the proposition we have |Aj|−1/2 ⩽ λ(i−j)/2|Ai|−1/2 for j ⩾ i. Summing the geometric series yields

|Aj|−1/2 ⩽ |Ai|−1/2

√

,

λ − 1

j>i

and the stated conclusion follows using the definition ω[Ai] = E(Ai)/|Ai|3. □ 4. Improved constants for Littlewood’s conjecture

In the next two sections we deduce our two main theorems from Proposition 3.1, starting here with Theorem 1.5, the improved constant for Littlewood’s conjecture.

One may deduce Littlewood’s conjecture (with some constant) from Proposition 3.1 by taking Ai to be roughly the ≈ λi smallest elements of A for all i and using the trivial bound ω[Ai] ⩽ 1, choosing b > 0 and 1/λ suitably small absolute constants yields ∥ 1A∥1 ≫ J, where λJ ≍ N and hence J ≫λ log N as required.

To extract a decent constant from this is a delicate optimisation in both b and λ, and this was the task considered by [15, 17]. To get the slightly better constant in Theorem 1.5, we will use a slightly less trivial bound for the ω[Ai], obtained using a rearrangement inequality.

Lemma 4.1. Suppose that A,B are finite sets of integers with cardinalities n,m respectively, where m ⩽ n. Then

m 3

m 3n

E(A,B) = #{(a1,b1,a2,b2) ∈ A×B×A×B : a1+b1 = a2+b2} ⩽ nm2 1−

.

+

In particular, ω[A] ⩽ 32 + on→∞(1).

Proof. This follows from a well-known rearrangement inequality (see Gabriel [5, Theorem 3] or [10, Theorem 376]3). A quick proof is as follows. Let the elements of A be a1 < a2 < ··· < an, and the elements of B be b1 < ··· < bm. Writing r(x) for the number of pairs (a,b) ∈ A × B with a + b = x, we have

r(ai + bj) ⩽ 1 + min(n − i,j − 1) + min(m − j,i − 1). (4.1) Indeed, the constant 1 counts the representation ai +bj itself. The min(n−i,j −1) term is an upper bound for representations ai + bj = ai′ + bj′ with i < i′ ⩽ n, which must have also have 1 ⩽ j′ < j; for each i′ (or j′) there is at most one such representation. The min(m − j,i − 1) term is an upper bound for representations ai + bj = ai′ + bj′ with 1 ⩽ i′ < i (and hence j < j′ ⩽ m). Now sum (4.1) over 1 ⩽ i ⩽ n and 1 ⩽ j ⩽ m. The left-hand side becomes E(A,B), and (after a computation) the right-hand side becomes nm2 1 − 3mn + m3 . □

We now give the deduction of Theorem 1.5 from Proposition 3.1.

Proof of Theorem 1.5. Let b > 0 and λ ⩾ 2 be some constants to be chosen later, and fix some A ⊂ Z of size N, for some large N (where the notion of ‘large’ may depend on λ and b). We now construct nested initial segments A1 ⊆ ··· ⊆ AJ of A, for a certain parameter J.

Let A1 be the set consisting of the smallest ⌊log N⌋ elements of A. In general, if A1,...,Aj have been constructed, let Aj+1 be the set of the smallest ⌈λ|Aj|⌉ elements of A and continue. Otherwise, we set J = j and halt. Furthermore we have |Aj+1| ⩾ λ|Aj| for j = 1,...,J − 1. Additionally, |Aj+1| ⩽ λ|Aj| + 1 for j = 1,...,J − 1, and hence by induction

|Aj| ⩽ λr |Aj−r| + λ−1 + λ−2 + ··· + λ−r for any r ⩾ 1. Taking r = j − 1 (and since λ ⩾ 2) we have

|Aj| ⩽ λj−1(1 + log N). By definition, the parameter J was minimal such that

N < λ|AJ|. It follows that

N < λJ(1 + log N) and so

log N log λ

J ⩾ (1 − o(1))

. (4.2) Here, and below, o(1) means a quantity tending to 0 as N → ∞.

Applying Lemma 4.1 to A1,...,AJ and substituting in to Proposition 3.1, and recalling our bound (4.2) on J, we deduce that

∥ 1A∥1 ⩾ (1 − o(1))f(b,λ)log N where

1 − e−b log λ

b √

1 − (2/3)1/2

.

f(b,λ) =

λ − 1

3It is important to note, when reading this reference, the convention established on the previous page: ‘We may agree that, when there is no indication to the contrary, sums involving several suffixes are extended over values of the suffixes whose sum vanishes’.

It remains to choose b > 0 and λ ∈ [2,∞) to maximise f(b,λ). Computational investigations tell us that the maximum value is

f(b,λ) = 0.170934··· achieved at

b = 0.932199··· and λ = 9.112038··· . □

5. A structural inverse result

Now we turn to the deduction of Theorem 1.2. In deducing Theorem 1.2 we are not concerned with constants, and so we record the following simpler consequence of Proposition 3.1.

- Corollary 5.1. Let η ∈ (0,1/4]. Let A ⊂ Z be a finite set. Suppose we have a nested sequence A1 ⊆ A2 ⊆ ··· ⊆ AJ of initial segments of A such that


|Ai−1| ⩽ (1 − η)|Ai|. There exists a constant c > 0 such that

J

∥ 1A∥1 ≫ J − cη−1

ω[Ai]1/2.

i=1

Proof. Noting that ω[A] ⩾ |A|−1 for any nonempty set A of integers, this follows immediately from Proposition 3.1 with b = 1 and 1/λ = 1 − η, so that √λ1−1 ≪ η−1. □

We may now prove Theorem 1.2.

Proof of Theorem 1.2. We may assume that K ⩾ 1001 (say) since the Littlewood conjecture is true. If δ/K ⩽ N−1/2 then the result is trivial by taking A′ = A, since any set of size N has at least N2 additive quadruples. If δ ⩽ C(log N)−1 for some absolute constant C > 0 then the result is again true with A′ = A by applying H¨lder’s inequality on the Fourier side, noting that E(A)1/4 is the L4-norm of 1A.

In what follows we suppose that δ/K > N−1/2 and that δ ⩾ C(log N)−1 (where

C > 0 is some absolute constant to be chosen later). Set η := cδ/K, where c ∈ (0, 14] is an absolute constant to be specified later. In particular, η−1 ≪ N1/2.

We construct nested initial segments A1 ⊆ A2 ⊆ ··· ⊆ AJ of A in the following fashion. Let A1 be the smallest ⌊N1−δ⌋ elements of A. In general, if A1,...,Aj have been constructed, then let Aj+1 be the set of the smallest ⌈(1 − η)−1 |Aj|⌉ elements of A if A has this many elements, or else halt with j = J. By construction it is clear that |Aj| ⩽ (1 − η)|Aj+1| for all j ∈ {1,...,J − 1}. Furthermore, |Aj+1| ⩽ (1 − η)−1 |Aj| + 1 for j ∈ {1,...,J − 1}, and hence by the same induction leading to (4.2) we have

|Aj| ⩽ (1 − η)1−j(N1−δ + η−1) ≪ (1 − η)1−jN1−δ. (5.1) The parameter J was the minimal j ⩾ 1 such that

N < (1 − η)−1 |AJ|,

and hence by (5.1) we have Nδ ≪ (1 − η)−J ⩽ e2ηJ. Since δ ⩾ C(log N)−1 (and N is sufficiently large), provided C > 0 is chosen sufficiently large, it follows that J ≫ η−1δ log N.

By Corollary 5.1 we see that either

J

ω[Ai]1/2 ≫ ηJ (5.2)

i=1

or ∥ 1A∥1 ≫ η−1δ log N. If the constant c is chosen appropriately then, since η = cδ/K, the latter option is contrary to our assumption. Thus (5.2) holds and so there exists some i such that

ω[Ai] ≫ η2 ≫ (δ/K)2.

The conclusion now follows taking A′ = Ai (noting that since A1 ⊆ A′ we always have |A′| ⩾ ⌊N1−δ⌋). □

6. Speculations about stronger structure

The structure found by Theorem 1.2 is, although non-trivial, still quite weak compared to the kind of structure one expects to find. For instance, we do not know of a counterexample to the following conjecture.

- Conjecture 6.1. Let A ⊂ Z be a finite set of size N. If ∥ 1A∥1 ⩽ K log N then for some m,r ≪K 1 the following holds. There are finite arithmetic progressions P1,...,Pm ⊂ Z, each of length at most N, and finite sets X1,...,Xr ⊂ Z such that

j Xj = oK(N), together with ϵ1,...,ϵm,η1,...,ηr ∈ {−1,1} such that 1A =

1⩽i⩽m

ϵi1P

i

+

1⩽j⩽r

ηj1X

j

.

A very similar (but slightly stronger) conjecture was put forward in print by Petridis [13, Question 5.1]. Analogous results are known to be true in finite field settings due to work of Sanders and the second author [7].

A consequence of Conjecture 6.1, still much stronger than anything we can prove, would be that there exists an arithmetic progression P of length at most N such that |A ∩ P| ≫K N.

A third possible inverse statement concerns the ‘dimension’ of A, defined as the size of the largest dissociated subset of A. As noted in the introduction, Pichorides [14] has proved that if ∥ 1A∥1 ⩽ K log N then

dimA ≪K (log N)3.

In the other direction, there are examples where ∥ 1A∥1 ≪ log N and yet dim(A) ≫ (log N)2 – simply take the union of an arithmetic progression P of size ≈ N and a dissociated set of size ≈ X = ⌊(log N)2⌋, and use the triangle inequality together with the observation that

∥ 1X∥1 ⩽ |X|1/2 ≪ log N. We conjecture that this is the best possible.

- Conjecture 6.2. Let K > 0 and N be sufficiently large depending only on K. Let A ⊂ Z be a finite set of size N. If ∥ 1A∥1 ⩽ K log N then dimA ≪K (log N)2. Furthermore, A contains a subset of size ≫K N and dimension ≪K log N.


### References

- [1] Benjamin Bedert. Large sum-free subsets of sets of integers via l1 estimates for trigonometric series. arXiv:2502.08624, 2025.
- [2] Jean Bourgain. Estimates related to sumfree subsets of sets of integers. Israel J. Math., 97:71–92, 1997.
- [3] D. Choimet and H. Queffe´lec. Twelve landmarks of twentieth-century analysis. Cambridge University Press, New York, 2015. Illustrated by Michae¨l Monerau, Translated from the 2009 French original by Danie`le Gibbons and Greg Gibbons, With a foreword by Gilles Godefroy.
- [4] John J. F. Fournier. Some remarks on the recent proofs of the Littlewood conjecture. In Second Edmonton conference on approximation theory (Edmonton, Alta., 1982), volume 3 of CMS Conf. Proc., pages 157–170. Amer. Math. Soc., Providence, RI, 1983.
- [5] R. M. Gabriel. The Rearrangement of Positive Fourier Coefficients. Proc. London Math. Soc.

(2), 33(1):32–51, 1931.

- [6] Ben Green. Approximate algebraic structure. In Proceedings of the International Congress of Mathematicians—Seoul 2014. Vol. 1, pages 341–367. Kyung Moon Sa, Seoul, 2014.
- [7] Ben Green and Tom Sanders. A quantitative version of the idempotent theorem in harmonic analysis. Ann. of Math. (2), 168(3):1025–1054, 2008.
- [8] Brandon Hanson. Littlewood’s problem for sets with multidimensional structure. Int. Math. Res. Not. IMRN, (21):16736–16750, 2021.
- [9] G. H. Hardy and J. E. Littlewood. A new proof of a theorem on rearrangements. J. London Math. Soc., 23:163–168, 1948.
- [10] G. H. Hardy, J. E. Littlewood, and G. Po´lya. Inequalities. Cambridge, at the University Press,, 1952. 2d ed.
- [11] Sergei V. Konyagin. On the Littlewood problem. Izv. Akad. Nauk SSSR Ser. Mat., 45(2):243– 265, 463, 1981.
- [12] O. Carruth McGehee, Louis Pigno, and Brent Smith. Hardy’s inequality and the L1 norm of exponential sums. Ann. of Math. (2), 113(3):613–618, 1981.
- [13] Giorgis Petridis. The L1-norm of exponential sums in Zd. Math. Proc. Cambridge Philos. Soc., 154(3):381–392, 2013.
- [14] Stylianos K. Pichorides. On the L1 norm of exponential sums. Ann. Inst. Fourier (Grenoble), 30(2):v, 79–89, 1980.
- [15] Jan D. Stegeman. On the constant in the Littlewood problem. Math. Ann., 261(1):51–54, 1982.
- [16] Terence Tao and Van H. Vu. Additive combinatorics, volume 105 of Cambridge Studies in Advanced Mathematics. Cambridge University Press, Cambridge, 2006.
- [17] Kˆozˆo Yabuta. A remark on the Littlewood conjecture. Bull. Fac. Sci. Ibaraki Univ. Ser. A,

(14):19–21, 1982.

- [18] Antoni Sz. Zygmund. Trigonometric series. Vol. I, II. Cambridge Mathematical Library. Cambridge University Press, Cambridge, third edition, 2002. With a foreword by Robert A. Fefferman.


Department of Mathematics, University of Manchester, Manchester, M13 9PL, UK Email address: thomas.bloom@manchester.ac.uk

Mathematical Institute, Andrew Wiles Building, Radcliffe Observatory Quarter, Woodstock Rd, Oxford OX2 6QW, UK

Email address: ben.green@maths.ox.ac.uk

