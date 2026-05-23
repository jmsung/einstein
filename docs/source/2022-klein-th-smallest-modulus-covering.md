---
type: source
kind: paper
title: On the $j$-th smallest modulus of a covering system with distinct moduli
authors: Jonah Klein, Dimitris Koukoulopoulos, Simon Lemieux
year: 2022
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2212.01299v2
source_local: ../raw/2022-klein-th-smallest-modulus-covering.pdf
topic: general-knowledge
cites:
---

arXiv:2212.01299v2[math.NT]23Aug2023

ON THE j-TH SMALLEST MODULUS OF A COVERING SYSTEM WITH DISTINCT MODULI

JONAH KLEIN, DIMITRIS KOUKOULOPOULOS, AND SIMON LEMIEUX

ABSTRACT. Covering systems were introduced by Erdo˝s in 1950. In the same article where he introduced them, he asked if the minimum modulus of a covering system with distinct moduli is bounded. In 2015, Hough answered afﬁrmatively this long standing question. In 2022, Balister, Bolloba´s, Morris, Sahasrabudhe and Tiba gave a simpler and more versatile proof of Hough’s result. Building upon their work, we show that there exists some absolute constant c > 0 such that the j-th smallest modulus of a minimal covering system with distinct moduli is exp(cj2/ log(j + 1)).

1. INTRODUCTION

A covering system is a ﬁnite set of arithmetic progressions whose union is Z. We say a covering system is minimal if there exists no proper subset of its arithmetic progressions that also covers Z.

Covering systems were ﬁrst introduced by Paul Erd˝os in a seminar 1950 article [7], where he used them to give an answer to a question of Romanoff on integers of the form 2k + p with p a prime and k an integer. More precisely, Erd˝os proved that there exists an arithmetic progression that contains no integers of the above form.

Throughout his life, Erd˝os posed many questions on the properties of covering systems. One of the most famous ones comes from his 1950 article: consider all covering systems with distinct moduli. Is there a uniform bound on the smallest modulus of all these systems? This problem remained open for 65 years, until it was recently solved by Hough [9]. In fact, Hough proved that every such system has minimum modulus at most 1016. In 2022, Balister, Bolloba´s, Morris, Sahasrabudhe and Tiba [4] reduced this bound to 616,000. Their method, which they named the distortion method, is rather versatile – see [2] for an expository note on it and [1] for another application of it to the so-called Erdos–Selfridge˝ problem. Using the distortion method, Cummings, Filaseta and Trifonov [6] improved Hough’s bound to 118 under the additional assumption that all moduli are square-free. In the present paper, we use this method to demonstrate the following generalization of Hough’s theorem.

- Theorem 1. There exists an absolute constant c > 0 such that the j-th smallest modulus in a minimal covering system with distinct moduli is exp(cj2/ log(j + 1)).


Except for the distortion method, the other key input to the proof of Theorem 1 is the following result of Crittenden and Vanden Eynden [5], originally conjectured by Erd˝os [8]: if a set of n arithmetic progressions does not cover Z, then it does not cover the interval {1, 2, . . ., 2n}. Interestingly, a shorter proof of this theorem was recently discovered by Balister, Bolloba´s, Morris, Sahasrabudhe and Tiba [1].

Remark. Cummings, Filaseta and Trifonov [6] have obtained a weaker version of Theorem 1 independently: they show that the j-th smallest modulus in a minimal covering system with distinct

![image 1](<2022-klein-th-smallest-modulus-covering_images/imageFile1.png>)

Date: August 25, 2023.

1

moduli is Cj for some unspeciﬁed constant Cj. Their proof is rather different, showing the existence of Cj in an inductive fashion, as a corollary of Hough’s theorem.

We conclude this introductory section with the following result that complements Theorem 1.

- Theorem 2. For each j 5, there exists a minimal covering system with the following j distinct moduli placed in increasing order:


2 < 22 < 23 < · · · < 2j−4 < 3 · 2j−5 < 2j−3 < 3 · 2j−4 < 3 · 2j−3. Proof. Fix j 5, and let

Cj = {1 (mod2), 2 (mod4), . . ., 2j−4 (mod2j−3), A0, A1, A2},

where Ak is the intersection of the congruence classes k (mod3) and 0 (mod2j−5+k). We claim that Cj is a covering system.

Indeed, for each integer n, either 2j−3|n or 2j−3 ∤ n. In the former case, let k ∈ {0, 1, 2} be such that n ≡ k (mod3). In particular, we have n ∈ Ak, and thus n is covered by Cj. Let us now consider the case when 2j−3 ∤ n. Then, there must exist some i ∈ {1, 2 . . ., j − 3} such that 2i−1|n and 2i ∤ n. Hence, n ≡ 2i−1 (mod2i), so that n is covered again by Cj.

We have thus proven that Cj is a covering system. Clearly, its list of moduli is the one prescribed in the statement of the theorem. Lastly, Cj is a minimal covering system: the arithmetic progressions 2i−1 (mod2i) with i = 1, . . ., j − 3 are disjoint and cover exactly the integers not divisible by 2j−3. On the other hand, the arithmetic progressions A0, A1, A2 are disjoint and are all needed to cover the integers in 0 (mod2j−3). This completes the proof of the theorem.

2. OUTLINE OF THE PROOF OF THEOREM 1 Let

C = {r1 (modq1), r2 (modq2), . . ., rk (modqk)}

be a minimal covering system with q1 < q2 < · · · < qk, and let ℓ ∈ {1, 2, . . ., k}. In particular, the ﬁrst ℓ − 1 congruence classes do not cover Z. Now, consider the system

- (2.1) Cℓ = rj − h(modqj) : ℓ j k, 0 h < 2ℓ−1 , so that C1 = C. Claim 2.1. The set Cℓ is a covering system for ℓ = 1, 2, . . ., k.


Proof. Recall that Crittenden and Vanden Eynden [5] proved that if ℓ progressions cover an interval I ⊂ Z of length 2ℓ, then they cover Z. Hence, for any ﬁxed n ∈ Z, we must have

ℓ−1

n + {0, . . ., 2ℓ−1 − 1}  ⊂

i=1

qiZ + ri ;

otherwise the progressions on the right-hand side would cover Z, which would contradict the minimality of the covering system C. Therefore, there is some h ∈ {0, . . ., 2ℓ−1 − 1} such that n + h ∈/ qiZ + ri for each i ∈ {0, 1, . . ., ℓ − 1}. Since C is a covering system, there must exist some j ℓ such that n + h is covered by qjZ + rj. We conclude that n ∈ qjZ + rj − h, and so n is covered by a progression in Cℓ.

The above claim motivates the following deﬁnition:

Deﬁnition 2.2. Let A = {a1 (modd1), a2 (modd2), . . ., an (moddn)} be a set of congruences. We deﬁne the multiplicity of A to be the number

#{1 j n : dj = d}. Remark. The moduli of a system of congruences A are distinct if and only if m(A) = 1.

m(A) := max

d∈N

With this deﬁnition in mind, we have that m(Cℓ) = 2ℓ−1 for the system of congruences deﬁned in (2.1). Hence, Theorem 1 is an immediate corollary of the following result.

- Theorem 3. Let A be a covering system of multiplicity s. Then there exists an absolute constant c > 0 such that its smallest modulus is exp(c log2(s + 1)/ log log(s + 2)).


We will prove Theorem 3 in the following section by a suitable modiﬁcation of the distortion method. Notation. Given n ∈ N, we write P+(n) for its largest prime factor with the convention that P+(1) = 1. In addition, we write ω(n) for the number of distinct prime factors of n.

We adopt the usual asymptotic notation of Vinogradov: given two functions f, g : X → R and a set Y ⊆ X, we write “f(x) ≪ g(x) for all x ∈ Y ” if there is a constant c = c(f, g, Y ) > 0 such that |f(x)| cg(x) for all x ∈ Y . The constant is absolute unless otherwise noted by the presence of a subscript. If h : X → R is a third function, we use Landau’s notation “f = g + O(h) on Y ” to mean that |f − g| ≪ h on Y . Typically the set Y is clear from the context and so not stated explicitly. Finally, if f ≪ g and g ≪ f, we write f ≍ g.

3. COVERING SYSTEMS OF BOUNDED MULTIPLICITY

- 3.1. The distortion method. In this section we slightly modify some of the deﬁnitions in [4] (see also [2]) to allow for covering systems of multiplicity > 1.


We start with a ﬁnite set of congruences A = {a1 (modd1), . . ., an (moddn)} with 1 < d1 d2 · · · dn. The goal is to show that if d1 is large enough in terms of the multiplicity of A, then A is not a covering system.

Let Q = [d1, . . ., dn], and let p1 < p2 < · · · < pJ be the distinct primes dividing Q. We may then write

J

pν

i , where νi is the pi-adic valuation of Q. For j ∈ {1, 2, . . ., J}, deﬁne Qj :=

Q =

i

i=1

j

pν

a(modQ) : a ≡ ai (moddi) .

i and Bj :=

i

1 i n P+(di)=pj

i=1

The most crucial deﬁnition is that of certain probability measures P0, P1, . . ., PJ on Z/QZ, which we construct exactly as in [4] in terms of some free parameters δ1, . . ., δJ ∈ [0, 1/2].

First of all, we set up some notation. Let πj : Z/QZ → Z/QjZ be the natural projection for all j ∈ {0, 1, . . ., J}, where Q0 = 1. In addition, let

Fj(x) := {x′ ∈ Z/QZ : πj(x′) = πj(x)},

so that |Fj(x)| = Q/Qj. The measure Pj will be Qj-measurable by construction, meaning that it will have the property that

Pj(x) = Pj(x′) whenever πj(x) = πj(x′).

We are now ready to deﬁne the measures Pj. We begin by letting P0 be the uniform measure on Z/QZ. Next, consider j ∈ {1, . . ., J} and suppose we have already constructed Pj−1 to be Qj−1-measurable. Let

|Fj−1(x) ∩ Bj| |Fj−1(x)|

αj(x) :=

![image 2](<2022-klein-th-smallest-modulus-covering_images/imageFile2.png>)

for all x ∈ Z/QZ,

and note that αj is a Qj−1-measurable function, meaning that αj(x′) = αj(x) if πj−1(x′) = πj−1(x). We then deﬁne Pj on the congruence class x ∈ Z/QZ as follows:

- • If αj(x) < δj, we let

Pj(x) := Pj−1(x) ·

1x/∈B

j

![image 3](<2022-klein-th-smallest-modulus-covering_images/imageFile3.png>)

1 − αj(x)

.

- • If αj(x) δj, we let


 

αj(x) − δj αj(x)(1 − δj)

if x ∈ Bj,

![image 4](<2022-klein-th-smallest-modulus-covering_images/imageFile4.png>)

Pj(x) := Pj−1(x) ·

1 1 − δj

if x ∈/ Bj.



![image 5](<2022-klein-th-smallest-modulus-covering_images/imageFile5.png>)

We may easily check that Pj(Fj−1(x)) =

- (3.1) Pj(x′) = Pj−1(x) · |Fj−1(x)| = Pj−1(Fj−1(x))


x′∈Fj−1(x)

for all x ∈ Z/QZ. Since Pj−1 is a probability measure on Z/QZ, so is Pj. In addition, Pj is Qj-measurable by construction. We have thus completed the inductive step.

Having deﬁned the measures Pj, we introduce the notation Ej[f] :=

f(x)Pj(x) for all functions f : Z/QZ → C.

x∈Z/QZ

We then deﬁne

Mj(1) := Ej−1[αj] and Mj(2) := Ej−1[αj2] for j = 1, . . ., J − 1.

Given the above notation and deﬁnitions, the key result of the distortion method is the following.

- Lemma 3.1 (Theorem 3.1 in [4]). Assume the above notation. If


Mj(2) 4δj(1 − δj)

J

min Mj(1),

![image 6](<2022-klein-th-smallest-modulus-covering_images/imageFile6.png>)

j=1

< 1,

then A does not cover the integers. Remark. As a matter of fact, Theorem 3.1 in [4] also contains a second part about the density of the uncovered set R, but we do not need it here.

- 3.2. Bounding the ﬁrst and second moment. We now proceed with bounding Mj(1) and Mj(2). Doing so is the context of Theorem 3.2 in [4], but this result is only valid for systems of congruences of multiplicity 1. We thus need to generalize it. This is rather straightforward, and we describe how to do it below.


- Lemma 3.2. Assume the above notation. For x ∈ Z/QZ and j ∈ {1, 2, . . ., J}, we have

αj(x)

νj

r=1 g|Qj−1 1 i n di=gprj

1x⊆a

i+gZ

![image 7](<2022-klein-th-smallest-modulus-covering_images/imageFile7.png>)

prj

.

Proof. Note that |Fj−1(x)| = Q/Qj−1 and that we may write x = c + QZ for some c ∈ Z. Hence, αj(x) =

|Fj−1(x) ∩ Bj| Q/Qj−1

![image 8](<2022-klein-th-smallest-modulus-covering_images/imageFile8.png>)

Qj−1 Q 1 i n

![image 9](<2022-klein-th-smallest-modulus-covering_images/imageFile9.png>)

P+(di)=pj

a (mod Q) a≡c (mod Qj−1) a≡ai (mod di)

1,

by the union bound. For each i with P+(di) = pj we may write uniquely di = gprj with g|Qj−1 and 1 r νj. We thus ﬁnd that

αj(x)

Qj−1 Qj

![image 10](<2022-klein-th-smallest-modulus-covering_images/imageFile10.png>)

νj

r=1 g|Qj−1 1 i n di=gprj

a (mod Q) a≡c (mod Qj−1) a≡ai (mod di)

1.

For the congruences a ≡ ai (moddi) and a ≡ c (modQj−1) to be compatible, we must have c ≡ ai (moddi) or, equivalently, that x is a subset of ai + gZ. Under this assumption, a lies in some congruence class mod Qj−1prj, so there are Q/(Qj−1prj) choices for a(modQ). This completes the proof of the lemma.

- Lemma 3.3. Assume the above notation, let s = m(A), and let j ∈ {1, 2, . . ., J}.


- (a) If δi = 0 for i ∈ {1, . . ., j − 1}, then

Mj(1) s

d d1 P+(d)=pj

1 d

![image 11](<2022-klein-th-smallest-modulus-covering_images/imageFile11.png>)

.

- (b) We have


s2(log p)6 p2

Mj(2) ≪

.

![image 12](<2022-klein-th-smallest-modulus-covering_images/imageFile12.png>)

Proof. We treat both parts simultaneously for now. Let k ∈ {1, 2} and let us write p = pj for simplicity. By Lemma 3.2, we have

Ej−1[αjk]

Pj−1 kℓ=1(ai

+ gℓZ) pr1+···+rk .

ℓ

![image 13](<2022-klein-th-smallest-modulus-covering_images/imageFile13.png>)

1 r1,...,rk νj g1,...,gk|Qj−1 1 i1,...,ik n diℓ=gℓprℓ ∀ℓ

Since di d1 for all i, we must have gℓpr

d1 for all ℓ. Given r1, . . ., rk and g1, . . ., gk, there are at most sk choices for i1, . . ., ik with di

ℓ

= gℓprℓ

(because we have assumed that A has multiplicity s). For each such choice of i1, . . ., ik, the Chinese Remainder Theorem implies that

ℓ

the set kℓ=1(ai

+ gℓZ) is either empty, or an arithmetic progression with modulus [g1, . . ., gk]. Hence, Lemma 3.4 in [4] implies that

ℓ

k

(1 − δi)−1 [g1, . . ., gk]

+ gℓZ) pi|[g1,...,gk]

(ai

Pj−1

(3.2) ,

![image 14](<2022-klein-th-smallest-modulus-covering_images/imageFile14.png>)

ℓ

ℓ=1

for each of the sk possible values of i1, . . ., ik. We thus conclude that

pi|[g1,...,gk](1 − δi)−1 [g1, . . ., gk]pr1+···+rk .

Ej−1[αjk] sk

![image 15](<2022-klein-th-smallest-modulus-covering_images/imageFile15.png>)

1 r1,...,rk νj g1,...,gk|Qj−1 gℓprℓ d1 ∀ℓ

When k = 1 and δi = 0 for all i < j, this readily proves part (a) of the lemma.

Now, let us consider the case when k = 2 and prove part (b). Here, there are no conditions on the parameters δi except for knowing that δi ∈ [0, 1/2] for all i. In particular, p

i|[g1,g2](1−δi)−1 2ω([g

1,g2]). Therefore,

2ω([g

1,g2])

Ej−1[αj2] s2

![image 16](<2022-klein-th-smallest-modulus-covering_images/imageFile16.png>)

[g1, g2]pr1+r2

1 r1,r2 νj g1,g2|Qj−1

2ω([g

1,g2])

s2 (p − 1)2

.

![image 17](<2022-klein-th-smallest-modulus-covering_images/imageFile17.png>)

![image 18](<2022-klein-th-smallest-modulus-covering_images/imageFile18.png>)

[g1, g2]

g1,g2|Qj−1

The function N ∋ m → #{(g1, g2) ∈ N2 : [g1, g2] = m} is multiplicative and takes the value 2ν + 1 on each ν-th prime power. Hence,

2ω([g

1,g2])

![image 19](<2022-klein-th-smallest-modulus-covering_images/imageFile19.png>)

[g1, g2]

g1,g2|Qj−1

=

i<j

6 pi

+ O

1 +

![image 20](<2022-klein-th-smallest-modulus-covering_images/imageFile20.png>)

1 p2i

![image 21](<2022-klein-th-smallest-modulus-covering_images/imageFile21.png>)

exp

i<j

6 pi

+ O

![image 22](<2022-klein-th-smallest-modulus-covering_images/imageFile22.png>)

1 p2i

![image 23](<2022-klein-th-smallest-modulus-covering_images/imageFile23.png>)

≪ (log p)6

by the inequality 1+t et and Mertens’ estimate [10, Theorem 3.4(b)]. This completes the proof of part (b) of the lemma too.

- 3.3. Proof of Theorem 3. It remains to prove Theorem 3. We will need the following simple consequence of Theorem 16.3 in [10]:


- Lemma 3.4. Let x y 2 be such that y (log x)3, and let u = log x/ log y. Then we have that


1 d

![image 24](<2022-klein-th-smallest-modulus-covering_images/imageFile24.png>)

d>yu P+(d) y

log y uu

≪

.

![image 25](<2022-klein-th-smallest-modulus-covering_images/imageFile25.png>)

Now, let us complete the proof of Theorem 3. In the notation of Section 3, we must show that if d1 > exp(c log2(s + 1)/ log log(s + 2)), then A that does not cover Z. In view of Lemma 3.1, it sufﬁces to show that

Mj(2) 4δj(1 − δj)

min Mj(1),

η :=

< 1.

![image 26](<2022-klein-th-smallest-modulus-covering_images/imageFile26.png>)

1 j J

Let y = Cs3, where C is a constant that will be chosen to be large enough, and let k = max{j ∈ [1, J] ∩ Z : pj y}. We set δi = 0 for i k and δi = 1/2 for i > k, so that

η

Mj(1) +

Mj(2) =: η1 + η2.

1 j k

k<j J

Then, Lemma 3.3(b) and Chebyshev’s estimate [10, Theorem 2.4] imply that η2 ≪

s2(log p)6 p2

s2(log y)5 y

≍

.

![image 27](<2022-klein-th-smallest-modulus-covering_images/imageFile27.png>)

![image 28](<2022-klein-th-smallest-modulus-covering_images/imageFile28.png>)

p>y

If C is large enough, then η2 < 1/2. From now on, we ﬁx such a choice of C. It remains to bound η1. Applying Lemma 3.3(a) and our assumption that

d1 > x := exp{c log2(s + 1)/ log log(s + 2)}, we ﬁnd that

1 d

η1 s

.

![image 29](<2022-klein-th-smallest-modulus-covering_images/imageFile29.png>)

d>x P+(d) y

If c is large enough compared to C (which we have already ﬁxed), then Lemma 3.4, applied with u =

c log2(s + 1) log(Cs3) log log(s + 2)

- log x

![image 30](<2022-klein-th-smallest-modulus-covering_images/imageFile30.png>)

- log y


c log s log log s

=

∼

when s → ∞,

![image 31](<2022-klein-th-smallest-modulus-covering_images/imageFile31.png>)

![image 32](<2022-klein-th-smallest-modulus-covering_images/imageFile32.png>)

implies that the sum over d is < 1/(2s). Hence, η1 < 1/2, and thus η η1 + η2 < 1, as needed. This shows that if d1 > x, then A does not cover Z, thus completing the proof of Theorem 3.

Acknowledgment. The authors would like to thank Michael Filaseta for a helpful conversation about paper [6]. They would also like to thank the referee of the paper for their comments and suggestions.

Funding. This project started during a 2020 summer internship of JK and SL, who were both funded by Undergraduate Summer Research Awards of the Natural Sciences and Engineering Research Council of Canada.

JK is supported by a fellowship of the Fonds de recherche du Que´bec - Nature et technologies. DK is supported by the Courtois Chair II in fundamental research, by the Natural Sciences and

Engineering Research Council of Canada (RGPIN-2018-05699) and by the Fonds de recherche du Que´bec - Nature et technologies (2022-PR-300951).

SL is supported by a fellowship funded by the Courtois Chair II in fundamental research. REFERENCES

- [1] P. Balister, B. Bolloba´s, R. Morris, J. Sahasrabudhe and M. Tiba, Covering intervals with arithmetic progressions. Acta Math. Hungar., 161 (2020), no. 1, 197–200.
- [2] , Erdos˝ covering systems. Acta Math. Hungar., 161 (2020), no. 2, 540–549.

![image 33](<2022-klein-th-smallest-modulus-covering_images/imageFile33.png>)

- [3] , The Erdos-Selfridge˝ problem with square-free moduli. Algebra Number Theory 15 (2021), no. 3, 609– 626.

![image 34](<2022-klein-th-smallest-modulus-covering_images/imageFile34.png>)

- [4] , On the Erdos˝ covering problem : The density of the uncovered set. Invent. Math. 228 (2022), no. 1, 377–414.

![image 35](<2022-klein-th-smallest-modulus-covering_images/imageFile35.png>)

- [5] R. B. Crittenden and C. L. Vanden Eynden, Any n arithmetic progressions covering the ﬁrst 2n integers cover all integers. Proc. Amer. Math. Soc. (1970), 475–481.
- [6] M. Cummings, M. Filaseta and O. Trifonov, An upper bound for the minimum modulus in a covering system with squarefree moduli. Preprint (2022), 25 pages, arXiv:2211.08548.
- [7] P. Erdo˝s, On integers of the form 2k + p and some related problems. Summa Brasil. Math. 2 (1950), 113–123.
- [8] , Remarks on number theory. IV. Extremal problems in number theory. I. (Hungarian) Mat. Lapok 13

![image 36](<2022-klein-th-smallest-modulus-covering_images/imageFile36.png>)

(1962), 228–255.

- [9] R. Hough, Solution of the minimum modulus problem for covering systems. Ann. of Math. (2) 181 (2015), no. 1, 361–382.


- [10] D. Koukoulopoulos, The distribution of prime numbers. Graduate Studies in Mathematics, 203. American Mathematical Society, Providence, RI, 2019.


DEPARTEMENT´ DE MATHEMATIQUES´ ET DE STATISTIQUE, UNIVERSITE´ DE MONTREAL´ , CP 6128 SUCC.

CENTRE-VILLE, MONTREAL´ , QC H3C 3J7, CANADA Email address: jonah.klein@umontreal.ca DEPARTEMENT´ DE MATHEMATIQUES´ ET DE STATISTIQUE, UNIVERSITE´ DE MONTREAL´ , CP 6128 SUCC.

CENTRE-VILLE, MONTREAL´ , QC H3C 3J7, CANADA Email address: dimitris.koukoulopoulos@umontreal.ca DEPARTEMENT´ DE MATHEMATIQUES´ ET DE STATISTIQUE, UNIVERSITE´ DE MONTREAL´ , CP 6128 SUCC.

CENTRE-VILLE, MONTREAL´ , QC H3C 3J7, CANADA Email address: simon.lemieux.6@umontreal.ca

