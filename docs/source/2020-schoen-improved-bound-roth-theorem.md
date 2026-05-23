---
type: source
kind: paper
title: Improved bound in Roth's theorem on arithmetic progressions
authors: Tomasz Schoen
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2005.01145v1
source_local: ../raw/2020-schoen-improved-bound-roth-theorem.pdf
topic: general-knowledge
cites:
---

arXiv:2005.01145v1[math.NT]3May2020

Improved bound in Roth’s theorem on arithmetic progressions

By Tomasz Schoen∗

Abstract

We prove that if A ⊆ {1,...,N} does not contain any non-trivial three-term arithmetic progression, then

(log log N)3+o(1) log N

N .

|A| ≪

![image 1](<2020-schoen-improved-bound-roth-theorem_images/imageFile1.png>)

- 1 Introduction In this paper we prove the following bound in Roth’s theorem on arithmetic progressions.


- Theorem 1 If A ⊆ {1,... ,N} does not contain any non-trivial arithmetic progression of length three then


(log log N)3(log log log N)5 log N

N .

|A| ≪

![image 2](<2020-schoen-improved-bound-roth-theorem_images/imageFile2.png>)

The ﬁrst non-trivial upper bound concerning the size of progression-free sets was given by Roth [18] who showed the above inequality with N/log log N. Then it was subsequently reﬁned by Heath-Brown [14] and Szemere´di [26] with a denominator of (log N)c for a positive constant c, by Bourgain [6, 7] and Sanders [21] by proving that bound with c = 1/2−o(1), c = 2/3−o(1) and c = 3/4 − o(1). Sanders [22] showed a result close to the logarithmic barrier

(log log N)6 log N

|A| ≪

N

![image 3](<2020-schoen-improved-bound-roth-theorem_images/imageFile3.png>)

and Bloom [4] further proved that

(log log N)4 log N

N ,

|A| ≪

![image 4](<2020-schoen-improved-bound-roth-theorem_images/imageFile4.png>)

for set A ⊆ {1,... ,N} avoiding three-term arithmetic progressions. Recently a slightly weaker bound was obtained by a diﬀerent argument by Bloom and Sisask [5]. Other results related to Roth’s theorem can be found in [12], [15], [16], [24] and [25].

![image 5](<2020-schoen-improved-bound-roth-theorem_images/imageFile5.png>)

∗The author is partially supported by National Science Centre, Poland grant 2019/35/B/ST1/00264

1

Let us also comment on the recent progress for the analogous problem in a high-dimensional case. Croot, Lev and Pach [9] proved, by a polynomial method, an upper estimate (4 −c)n with some constant c > 0, for the size of progression-free sets in (Z/4Z)n. Later Ellenberg and Gijswijt [11] obtained the bound (3 − c)n with a positive constant c for subsets of Fn3. The latter result signiﬁcantly improves the previous best bound of Bateman and Katz [1], however this the paper [1] contains many deep results and valuable ideas that could potentially be also used in the integer case.

Each of the mentioned papers contains signiﬁcant novel ideas and methods, any of them are used in our proof of Theorem 1. We employ the density increment argument obtained via the Fourier analytical method invented by Roth [18]. We make use of the Bohr set machinery introduced by Bourgain [6]. We focus on the structure of the large spectrum, explored ﬁrst by Bourgain [7] and thenceforth used in all further works. We also take advantage of deep insight into the structure of the large spectrum done by Bateman and Katz in [1] and [2].

Finally, let us mention that as far as the lower bound on the maximal size of progressionfree subsets of {1,... ,N} is concerned, the ﬁrst non-trivial lower estimate N1−c(log logN)−1 was established by Salem and Spencer [19]. Then Behrend [3] improved it to exp(−c√log N)N. Elkin [10] reﬁned slightly Behrend’s bound by a factor of (log N)1/2 and his argument was simpliﬁed in [13].

![image 6](<2020-schoen-improved-bound-roth-theorem_images/imageFile6.png>)

# 2 Notation, Bohr sets and standard results

All sets considered in the paper are ﬁnite subsets of Z or Z/NZ. We write 1A(x) for the indicator function of set A. Given functions f,g : Z/NZ → C, the convolution of f and g is deﬁned by

(f ∗ g)(x) =

f(t)g(x − t).

t∈Z/NZ

The Fourier coeﬃcients of a function f : Z/NZ → C are deﬁned by f(r) =

f(x)e−2πixr/N,

x∈Z/NZ

where r ∈ Z/NZ, and the above applies to the indicator function of A ⊆ Z/NZ as well. Parseval’s formula states in particular that

N−1

| 1A(r)|2 = |A|N .

r=0

We also recall the fact that

(1A ∗ 1B)(r) = 1A(r) 1B(r). For a real number θ 0, the θ−spectrum of a set A is the set

∆θ(A) = r ∈ Z/NZ : | 1A(r)| θ|A| . For a speciﬁed set A we often write ∆θ instead of ∆θ(A).

For m ∈ N by E2m(A) we denote the number of 2m–tuples (a1,... ,am,b1,... ,bm) ∈ A2m such that

a1 + ··· + am = b1 + ··· + bm. For m = 2, we simply write E(A) for E4(A) and we call it the additive energy of set A. We deﬁne the span of a ﬁnite set X by

Span (X) =

εxx : εx ∈ {−1,0,1} for all x ∈ X .

x∈X

The dimension dim(A) of set A is the minimal size of set X such that A ⊆ Span(X). The following theorem proven in [20] (see also [23] and [30]) provides an upper bound on the dimension of a set in terms of its additive doubling K = |A + A|/|A|.

- Theorem 2 [20] Suppose that |A + A| = K|A|. Then dim(A) ≪ K log |A|.


We are going to use a sophisticated concept of Bohr sets-a fundamental tool introduced to modern additive combinatorics by Bourgain [6].

Let G = Z/NZ be a cyclic group and let us denote the group of its characters by G ⋍ Z/NZ. We deﬁne the Bohr set with a generating set Γ ⊆ G and a radius γ ∈ (0, 21] to be the set

![image 7](<2020-schoen-improved-bound-roth-theorem_images/imageFile7.png>)

B(Γ,γ) = x ∈ Z/NZ : tx/N γ for all t ∈ Γ .

Here  ·  denotes the distance to the integers, i.e. x = miny∈Z |x − y| for x ∈ R. Given η > 0 and a Bohr set B = B(Γ,γ), by Bη we mean the Bohr set B(Γ,ηγ). The two lemmas below are pretty standard, hence we refer the reader to [31] for a complete account. The size of Γ is called the rank of B and we denote it by rk(B).

- Lemma 3 For every γ ∈ (0, 12] we have γ|Γ|N |B(Γ,γ)| 8|Γ|+1|B(Γ,γ/2)|.

![image 8](<2020-schoen-improved-bound-roth-theorem_images/imageFile8.png>)

Bohr sets do not always behave like convex bodies. The size of Bohr sets can vary signiﬁcantly even for small changes of the radius which was the motivation behind the following deﬁnition.

We call a Bohr set B(Γ,γ) regular if for every η, with |η| 1/(100|Γ|) we have

(1 − 100|Γ||η|)|B| |B1+η| (1 + 100|Γ||η|)|B|. Bourgain [6] showed that regular Bohr sets are ubiquitous.

- Lemma 4 For every Bohr set B(Γ,γ), there exists γ′ such that 12γ γ′ γ and B(Γ,γ′) is regular.


![image 9](<2020-schoen-improved-bound-roth-theorem_images/imageFile9.png>)

The last lemma of this section presents a standard L2 density increment technique introduced by Heath-Brown [14] and Szemere´di [26], see also [17]. A proof of the lemma below can be found in either of the following papers [21], [22] and [4].

- Lemma 5 Let A ⊆ Z/NZ be a set with density δ. Let Γ ⊆ Z/NZ and ν 0 be such that


| 1A(r)|2 ν|A|2 .

r∈Γ\{0}

Then there is a regular Bohr set B with rk(B) = dim(Γ) and radius Ω((dim(Γ))−1) such that

|(A + t) ∩ B| (1 + Ω(ν))δ|B| for some t.

Throughout the paper we assume that set A does not contain any non-trivial arithmetic progression of length three and that N is a large number.

# 3 Sketch of the argument

We apply a widely used density increment argument introduced by Roth [18], however we use it in a rather non-standard way. In the ﬁrst step, we increase the density by a large factor of the form (log(1/δ))1−o(1) on some low-rank Bohr set. Then we apply the iterative method of Bloom to our new set with larger density to obtain the desired bound.

The general strategy can be roughly described as follows. Let A ⊆ [N] be a set with density δ without arithmetic progressions of length three then it is known that 1A must have large Fourier coeﬃcients. To obtain a density increment we would have to ﬁnd a small set Λ such that Span(Λ) has large intersection with the spectrum ∆δ. The size of Λ is equal to the rank of a Bohr set, on which we will increase density, and density increment (given by the L2 method) equals

(1 + Ω(δ2|Span(Λ) ∩ ∆δ|))δ.

If we want to obtain the density increment by factor Ω(L) for some function L → ∞, we have to locate Λ of size O(δ−1+c),c > 0 such that

|Span (Λ) ∩ ∆δ| ≫ Lδ−2 . (1)

The main problem is that by of Bateman-Katz structural result (see Theorem 10) there are sets with spectrum such that the described set Λ does not exist. Hence one needs to combine the above method with some new ideas.

In order to obtain the density increment we will consider three separate cases with respect to the size of Fourier coeﬃcients of 1A that in a sense dominate in ∆δ1+µ for a some small constant µ > 0. If the contribution of middle size or small Fourier coeﬃcients is large we follow the method introduced by Bateman and Katz [1]. We consider essentially two subcases according to the additive behavior of the large spectrum ∆. Following [1], we call the cases smoothing and nonsmoothing, respectively. If the higher energy E8(∆) is much bigger than one can deduce from the H¨older inequality applied to E(∆) (smoothing case), then based on the Bateman-Katz argument we can indeed ﬁnd a small set Λ satisfying (1). The nonsmoothing case is more delicate. In that case we use a seminal result of Bateman and Katz [1, 2] that describes the structure of the spectrum in the nonsmoothing case and it turns out that again we can also ﬁnd a small set

Λ satisfying (1), apart from one situation where roughly ∆ ≈ X + H ,|∆| ∼ δ−3+O(µ) ,|X| ∼ δ−2+O(µ) ,|H| ∼ δ−1+O(µ) and H is a highly structured set. This case is considered separately in Lemma 13 which is an important part of our argument. We show that either the density can be increased on a Bohr set generated by H (such a Bohr set has a very low rank) or X contains additive substructure which again leads to a density increment on a low-rank Bohr set. The above argument does not apply when ∆δ1+µ is dominated by large Fourier coeﬃcients. Then assuming that there are very few smaller Fourier coeﬃcients in ∆δ1+µ, using a diﬀerent technique based on Fourier approximation method, we prove that A does indeed have density increment on a low-rank Bohr set.

# 4 Middle size Fourier coeﬃcients

Assume that A ⊆ {1,... ,N′} does not contain any non-trivial arithmetic progressions of length three. Let N be any prime number satisfying 2N′ < N 4N′. We embed A in Z/NZ in a natural way and observe that A also does not contain any non-trivial arithmetic progression of length 3 in Z/NZ. Let us recall a standard argument that shows that 1A must have large Fourier coeﬃcients. The number of three-term arithmetic progressions in A (including trivial ones) is expressed by the sum N1 r N=0−1 1A(r)2 1A(−2r), whence we have

![image 10](<2020-schoen-improved-bound-roth-theorem_images/imageFile10.png>)

N−1

1 N

1A(r)2 1A(−2r) = |A|.

![image 11](<2020-schoen-improved-bound-roth-theorem_images/imageFile11.png>)

r=0

Clearly, we can assume that |A| > √2N, so by the H¨older inequality

![image 12](<2020-schoen-improved-bound-roth-theorem_images/imageFile12.png>)

- 1

![image 13](<2020-schoen-improved-bound-roth-theorem_images/imageFile13.png>)

- 2|A|3 .


| 1A(r)|3 |A|3 − N|A|

r =0

Since

it follows that

| 1A(r)|3

r ∈∆δ/4(A)

N−1

1 4

1 4|A|3

| 1A(r)|2 =

δ|A|

![image 14](<2020-schoen-improved-bound-roth-theorem_images/imageFile14.png>)

![image 15](<2020-schoen-improved-bound-roth-theorem_images/imageFile15.png>)

r=0

| 1A(r)|3

r∈∆δ/4\{0}

1 4|A|3 ,

![image 16](<2020-schoen-improved-bound-roth-theorem_images/imageFile16.png>)

hence there are non-trivial Fourier coeﬃcients with | 1A(r)| ≫ δ|A|.

However to obtain a large density increment we have to control Fourier coeﬃcients below typical treshold δ|A|. We will consider three separate cases:

1 10

δµ/5|A|3 , (2)

| 1A(r)|3

![image 17](<2020-schoen-improved-bound-roth-theorem_images/imageFile17.png>)

r: δ1−µ|A| | 1A(r)| δ1/10|A|

| 1A(r)|3

r: δ1+µ|A| | 1A(r)| δ1−µ|A|

1 10

δµ/5|A|3 , (3)

![image 18](<2020-schoen-improved-bound-roth-theorem_images/imageFile18.png>)

and the last one if (2) and (3) do not hold, where µ is a small positive constant. Throughout the paper we assume that δµ/20 < log−1(1/δ) since we know that δ → 0 as N → ∞.

By dyadic argument, we obtain

| 1A(r)|3

r: θ|A| | 1A(r)| 2θ|A|

1 10

δµ/5|A|3 log−1(1/δ) (4)

![image 19](<2020-schoen-improved-bound-roth-theorem_images/imageFile19.png>)

for some δ1−µ θ δ1/10, so

|∆θ| ≫ θ−3δµ/5 log−1(1/δ) θ−3δµ/4 . (5)

In this section we consider the ﬁrst case (2). We will apply the Bateman-Katz-Bloom lemma, see Lemma 5.3 in [1] and Theorem 4.1 in [4] (a slightly weaker version of Lemma 6 can be easily deduced from Lemma 8).

- Lemma 6 Let A ⊆ Z/NZ be a set with density δ, and let ∆ be a subset of ∆θ. Then there exists

- a set ∆′ ⊆ ∆ such that |∆′| ≫ θ|∆| and dim(∆′) ≪ θ−1 log(1/δ).


- Lemma 7 Let A ⊆ Z/NZ be a set with density δ, and suppose that (5) holds for some δ1−µ θ δ1/10. Then there is a regular Bohr set B with rk(B) ≪ δ−1+µ/3 and radius Ω(δ1−µ/3) such that for some t


|(A + t) ∩ B| ≫ δ1−µ/4|B|.

Proo f. By Lemma 6 there exists a set ∆1 ⊆ ∆θ such that |∆1| = Θ(θ|∆θ|) and dim(∆1) ≪ θ−1 log(1/δ).

By iterative application of Lemma 6, we see that there are disjoint sets ∆1,... ,∆k ⊆ ∆θ, for k = Θ(δ−µ/2) such that |∆i| = Θ(θ|∆θ|) and

dim(∆i) ≪ θ−1 log(1/δ)

for every 1 i k. Put Γ = ki=1 ∆i ⊆ ∆θ then by (5) we have

|Γ| ≫ δ−µ/2θ−2δµ/4 ≫ δ−µ/4θ−2 and

dim(Γ) ≪ δ−µ/2θ−1 log(1/δ) ≪ δ−1+µ/2 log(1/δ) ≪ δ−1+µ/3 . Therefore, by Lemma 5 a shift of the set A has density at least

(1 + Ω(θ2|Γ|))δ ≫ δ−1+µ/3 on a regular Bohr set with rank O(δ−1+µ/3) and radius Ω(δ1−µ/3). ✷

# 5 Additively smoothing spectrum

In sections 5 and 6 we obtain a density increment provided that (3) holds. Hence for some δ1+µ θ δ1−µ we have

| 1A(r)|3 ≫ |A|3 log−1(1/δ).

r: θ|A| | 1A(r)| 2θ|A|

Thus

|∆θ| δµ/5θ−3 log−1(1/δ) δ2µθ−2δ−1 , (6) so the size of ∆θ is close to the maximal possible value.

A well-known theorem of Shkredov [28, 29] states that for every ∆ ⊆ ∆θ and m ∈ N we have

E2m(∆) θ2mδ|∆|2m.

Observe that by the Parseval formula |∆θ| θ−2δ−1, so if we additionally assume that |∆θ| ≫ θ−2δ−1, then the H¨older inequality implies that for m 3

E2m(∆θ) E(∆θ)m−1|∆θ|m−2 ≫m θ2mδ|∆θ|2m ,

which essentially meets Shkredov’s bound. This observation motivates the next deﬁnition introduced by Bateman and Katz. We say that a spectrum ∆θ is σ-additively smoothing (or simply additively smoothing if σ is indicated) if

E8(∆θ) δ−σθ8δ|∆θ|8.

Otherwise, we say that the spectrum ∆θ is σ-additively nonsmoothing. In this section, we will obtain a density increment for additively smoothing spectrum.

The following lemma, proven in [23] (see Corollary 7.5) is an abelian group version of Bateman-Katz Lemma 5.3. The proof of this result requires some modiﬁcations, but similarly as in Bloom’s Theorem 4.1 in [4] it relies on a probabilistic argument of Bateman and Katz.

- Lemma 8 Let ∆ ⊆ Z/NZ be a set such that E2s(∆) = κ|∆|2s 10ss2s|∆|s, where 2 s = ⌊log |∆|⌋. Then there exists a set Λ ⊆ ∆ such that |Λ| ≪ κ−1/2s log3/2 |∆| and

|Span (Λ) ∩ ∆| ≫ κ1/2s|∆|log−3/2 |∆|.

- Lemma 9 Let A ⊆ Z/NZ, |A| = δN and suppose that for some δ1+µ θ δ1−µ we have


E8(∆θ) δ−20µθ8δ|∆θ|8. Then there is a regular Bohr set B with rank rk(B) ≪ δ−1+µ/2 and radius Ω(δ1−µ/2) such that for some t

|(A + t) ∩ B| ≫ δ1−µ/2|B|.

Proo f. Put s = ⌊log |∆θ|⌋. Using the H¨older inequality and (5) we have E2s(∆θ) E8(∆θ)s−31

|∆θ|−s−4

3 δO(1)δ13(1−20µ)sθ83s|∆θ|7

3s δ−13(18µ+o(1))sθ2s|∆θ|2s δ−4µsθ2s|∆θ|2s ,

![image 20](<2020-schoen-improved-bound-roth-theorem_images/imageFile20.png>)

![image 21](<2020-schoen-improved-bound-roth-theorem_images/imageFile21.png>)

![image 22](<2020-schoen-improved-bound-roth-theorem_images/imageFile22.png>)

![image 23](<2020-schoen-improved-bound-roth-theorem_images/imageFile23.png>)

![image 24](<2020-schoen-improved-bound-roth-theorem_images/imageFile24.png>)

![image 25](<2020-schoen-improved-bound-roth-theorem_images/imageFile25.png>)

provided that N is large enough. Notice that (6) implies that E2s(∆θ) ≫ 10ss2s|∆θ|s, so we can apply Lemma 8. Thus, there exists a set Λ such that

|Λ| ≪ δ2µθ−1 log3/2(1/δ) ≪ δ−1+µ/2 and

|Span(Λ) ∩ ∆θ| ≫ δ−2µθ log−3/2(1/δ)|∆θ| ≫ δ−2µθ−2 log−5/2(1/δ) ≫ δ−µ/2θ−2 . Now it is enough to use Lemma 5 with Γ = Span(Λ) to get the required result. ✷

# 6 Additively nonsmoothing spectrum

In this section, we will obtain a density increment in a more diﬃcult case, when the spectrum ∆θ is an additively nonsmoothing set. Recall that for some δ1+µ θ δ1−µ we have

|∆θ| δ2µθ−2δ−1 .

Bateman and Katz [1, 2] proved the following fundamental result characterizing the structure of additively nonsmoothing sets.

Theorem 10 Let τ > 0 be a ﬁxed number. There exists a function f = fτ : (0,1) → (0,∞) with f(x) → 0 as x → 0 such that the following holds. Let ∆ be a symmetric set of an abelian group and let σ > 0. Assume that E(∆′) ≫ |∆|2+τ for every ∆′ ⊆ ∆ with |∆′| ≫ |∆| and that E8(∆) |∆|4+3τ+σ. Then there exists α, 0 α 1−2τ , such that for i = 1,... ,⌈|∆|α−f(σ)⌉ there are sets Hi,Xi and ∆i ⊆ ∆ such that

![image 26](<2020-schoen-improved-bound-roth-theorem_images/imageFile26.png>)

|Hi| ≪ |∆|τ+α+f(σ), (7) |Xi| ≪ |∆|1−τ−2α+f(σ), (8)

|Hi + Hi| ≪ |Hi|1+f(σ), (9) and

|(Xi + Hi) ∩ ∆i| ≫ |∆|1−α−f(σ). (10) Furthermore, the sets ∆i are pairwise disjoint.

We will apply Theorem 10 to the set ∆θ. By Shkredov’s theorem for every ∆ ⊆ ∆θ with |∆| ≫ |∆θ| we have

E(∆) θ4δ|∆|4 ≫ δ10µ/3θ2/3δ−2/3|∆|7/3 δ4µ|∆|7/3 ≫ |∆θ|7/3−2µ .

On the other hand, by Lemma 9 we can assume that

E8(∆θ) δ−20µθ8δ|∆θ|8 |∆θ|5+10µ . Therefore we can apply Theorem 10 with

τ = 1/3 − 2µ and σ = 16µ,

hence our spectrum ∆θ has structure described in Theorem 10.

Throughout the paper assume that f(σ) σ and that µ and f = f(16µ) are small constants. Each of the four inequalities given in Theorem 10 is crucial in our approach. Note that from

(7), (8) and (10) we can deduce lower bounds for the size of Hi and Xi. In order to apply the last one, we will need the following simple, elementary lemma.

- Lemma 11 Let c,ε > 0 be such that |(X + H) ∩ ∆| c|X||H|1−ε. Then there is a set X′ ⊆ X such that |X′| 4 c|X||H|−ε and for every Y ⊆ X′ we have |(Y + H) ∩ ∆| c82|Y ||H|1−2ε. Proo f. Put S = (X + H) ∩ ∆ and notice that


![image 27](<2020-schoen-improved-bound-roth-theorem_images/imageFile27.png>)

![image 28](<2020-schoen-improved-bound-roth-theorem_images/imageFile28.png>)

(1X ∗ 1H)(t) = |X||H|.

t∈X+H

Let us denote by P the set of elements t with (1X ∗ 1H)(t) 2c|H|ε. Clearly, |P| 2 c|X||H|1−ε and therefore

![image 29](<2020-schoen-improved-bound-roth-theorem_images/imageFile29.png>)

![image 30](<2020-schoen-improved-bound-roth-theorem_images/imageFile30.png>)

(1X ∗ 1H)(t) =

t∈S\P

|(x + H) ∩ (S \ P)| |S| − |P|

x∈X

c 2|X||H|1−ε .

![image 31](<2020-schoen-improved-bound-roth-theorem_images/imageFile31.png>)

- Let X′ be the set of all x ∈ X satisfying the inequality |(x + H) ∩ (S \ P)| 4 c|H|1−ε. Observe that


![image 32](<2020-schoen-improved-bound-roth-theorem_images/imageFile32.png>)

c 4|H|1−ε|X \ X′|

c 4|X||H|1−ε ,

|(x + H) ∩ (S \ P)|

![image 33](<2020-schoen-improved-bound-roth-theorem_images/imageFile33.png>)

![image 34](<2020-schoen-improved-bound-roth-theorem_images/imageFile34.png>)

x∈X\X′

hence

|X′||H|

|(x + H) ∩ (S \ P)|

x∈X′

c 4|X||H|1−ε .

![image 35](<2020-schoen-improved-bound-roth-theorem_images/imageFile35.png>)

Thus, |X′| 4 c|X||H|−ε and if Y ⊆ X′, then

![image 36](<2020-schoen-improved-bound-roth-theorem_images/imageFile36.png>)

|(Y + H) ∩ ∆|

c 4|Y ||H|1−ε

![image 37](<2020-schoen-improved-bound-roth-theorem_images/imageFile37.png>)

,

![image 38](<2020-schoen-improved-bound-roth-theorem_images/imageFile38.png>)

2 c|H|ε

![image 39](<2020-schoen-improved-bound-roth-theorem_images/imageFile39.png>)

which yields to the required inequality. ✷

The next lemma provides a density increment in a simpler case-in Bateman-Katz theorem we have α 20f.

- Lemma 12 Let A ⊆ Z/NZ,|A| = δN, and assume that for every ∆′ ⊆ ∆ with |∆′| ≫ |∆| we


have E(∆′) ≫ |∆|7/3−2µ and E8(∆) |∆|5+10µ. Then either there is a regular Bohr set B with rk(B) ≪ δ−1+f and radius Ω(δ1−f) such that

|(A + t) ∩ B| ≫ δ1−f|B|

for some t; or there are sets H and X such that |H| ≪ |∆θ|1/3+21f,|H + H| ≪ |H|1+f, |X| ≪ |∆θ|2/3+2f, and

|(X + H) ∩ ∆θ| ≫ |∆θ|1−21f.

Proo f. By Theorem 10 applied with τ = 1/3 − 2µ there exist 0 α 1/3 + µ and sets Hi,Xi for 1 i ⌈|∆θ|α−f⌉ such that

- |∆θ|1/3−2µ+α−2f ≪ |Hi| ≪ |∆θ|1/3−2µ+α+f ,

and

- |∆θ|2/3+2µ−2α−2f ≪ |Xi| ≪ |∆θ|2/3+2µ−2α+f ,


that fulﬁll inequalities (7)–(10). First, we assume that 1/3 − 20f α 1/3 + µ and put k = ⌈|∆θ|α−25f⌉. Then by (10), (9) and Theorem 2 we have

k

(Xi + Hi) ∩ ∆θ ≫ |∆θ|α−25f|∆θ|1−α−f |∆θ|1−f θ−2δ−f ,

i=1

and

k

k

|Xi|dim(Hi) |∆θ|α−25f|Xi||Hi|f log |Hi|

(Xi + Hi) ≪

dim

i=1

i=1

≪ |∆θ|2/3+2µ−α−22f |∆θ|1/3−f ≪ δ−1+f . Next let us assume that 20f α 1/3 − 20f. Observe that by (10) for every i we have

|(Xi + Hi) ∩ ∆i| ≫ |∆θ|1−α−f ≫ |Xi||Hi||∆θ|−3f ≫ |Xi||Hi|1−5f . (11) By Lemma 11 applied with Xi,Hi and ε = 5f there is Xi′ ⊆ Xi such that

|Xi′| ≫ |Xi||Hi|−5f ≫ |∆θ|2/3+2µ−2α−5f |∆θ|1/3−α+15f . Let Yi ⊆ Xi′ be any subset of size ⌈|∆θ|1/3−α+15f⌉. By Lemma 11, we have

|(Yi + Hi) ∩ ∆i| ≫ |∆θ|2/3−2µ+3f |∆θ|2/3+f θ−2δ−f . Again Theorem 2 and (9) imply that

dim(Yi + Hi) dim(Yi)dim(Hi) ≪ |∆θ|1/3−α+15f|Hi|f log |Hi| |∆θ|1/3−α+17f |∆θ|1/3−f δ−1+f .

In both above considered cases we found a subset of ∆θ of size Ω(θ−2δ−f) and dimension O(δ−1+f) hence by Lemma 5 there is a regular Bohr set B with rk(B) ≪ δ−1+f and radius Ω(δ1−f) such that

|(A + t) ∩ B| (1 + Ω(θ2θ−2δ−f))δ|B| ≫ δ1−f|B| for some t.

Finally, if α 20f then for every i we have |Hi| ≪ |∆θ|1/3−µ/3+α+f |∆θ|1/3+21f,|Hi + Hi| ≪ |Hi|1+f,|Xi| ≪ |∆θ|2/3+2µ/3−2α+f |∆θ|2/3+2f and

|(Xi + Hi) ∩ ∆θ| ≫ |∆θ|1−f , which completes the proof. ✷

Finally, we arrived at a more diﬃcult case, where ∆ ≈ X + H, |X| ∼ δ−2+O(µ),|H| ∼ δ−1+O(µ) and the set H is highly structured.

- Lemma 13 Let A ⊆ Z/NZ,|A| = δN, and assume that there are sets H and X such that |H| ≪ |∆θ|1/3+21f,|H + H| ≪ |H|1+f, |X| ≪ |∆θ|2/3+2f, and


|(X + H) ∩ ∆θ| ≫ |∆θ|1−21f. Then there is a regular Bohr set B with rk(B) δ−1+f and radius Ω(δ1−f) such that

|(A + t) ∩ B| ≫ δ1−f|B| for some t.

Proo f. Since dim(H) ≪ δ−2f then there is a set Λ such that |Λ| ≪ δ−2f and H ⊆ Span(Λ). Let B = B(Λ,γ) be a regular Bohr set with radius 1/(6|Λ|) γ 1/(3|Λ|) (the existence of such γ is guaranteed by Lemma 4). Then clearly B ⊆ B(H,1/3). Furthermore, for h ∈ H and

- b ∈ B we have hb/N


λb/N 1/3,

λ∈Λ

so

- 1

![image 40](<2020-schoen-improved-bound-roth-theorem_images/imageFile40.png>)

- 2|B|.


ℜe−2πihb/N

| 1B(h)|

b∈B

Put At = (A + t) ∩ B and let us assume that for each t we have |At| ≪ δ1−f|B|, (12)

as otherwise we would obtain the required density increment on a Bohr set with the rank O(δ−2f) and radius Ω(δ2f). For every x ∈ Z/NZ we have

1 N h

1B(h) 1A(x − h)e2πit(x−h)/N ,

1At(x) =

![image 41](<2020-schoen-improved-bound-roth-theorem_images/imageFile41.png>)

hence by the Parseval formula

t

1 N h | 1B(h) 1A(x + h)|2

| 1At(x)|2 =

![image 42](<2020-schoen-improved-bound-roth-theorem_images/imageFile42.png>)

1 N h∈H | 1B(h) 1A(x + h)|2 . (13)

![image 43](<2020-schoen-improved-bound-roth-theorem_images/imageFile43.png>)

- Let Y ⊆ X be a set given by Lemma 11 when applied to X,H and ε = 5f. Bounding similarly as in (11) we have


|Y | ≫ |X||H|−5f ≫ |∆θ|2/3−O(f) . Therefore, summing (13) over Y we get

| 1At(x)|2

t x∈Y

1 N h∈H x∈Y | 1B(h) 1A(x + h)|2 ≫

1

N |(Y + H) ∩ ∆θ||B|2δ2−2µ|A|2 ≫ δ3|∆θ|1−O(f)|B|2|A| ≫ δO(f)|B|2|A|.

![image 44](<2020-schoen-improved-bound-roth-theorem_images/imageFile44.png>)

![image 45](<2020-schoen-improved-bound-roth-theorem_images/imageFile45.png>)

Using averaging argument and (12) we see that there is a t such that

| 1At(x)|2 ≫ δ1+O(f)|B|2 ≫ δ−1+O(f)|At|2 . (14)

x∈Y

We can ignore all small terms in (14) that satisfy

δ−1/2+O(f) |X|1/2

|At| = δ1/2+O(f)|At|,

| 1At(x)| c

![image 46](<2020-schoen-improved-bound-roth-theorem_images/imageFile46.png>)

where c > 0 is a suﬃciently small constant, so by dyadic argument there is η ≫ δ1/2+O(f) such that

| 1At(x)|2 ≫ δ−1+O(f) log−1(1/δ)|At|2 ≫ δ−1+O(f)|At|2 .

x∈Y : η|At| | 1At(x)| 2η|At|

Put

S = x ∈ Y : η|At| | 1At(x)| 2η|At| then by the above inequality it follows that

|S| ≫ η−2δ−1+O(f) .

By Lemma 6 there is a set Z ⊆ S ⊆ Y such that |Z| η|S| ≫ η−1δ−1+O(f) and dim(Z) ≪ η−1 log(N/|At|). From (14) one can deduce that |At| ≫ δ2|B| hence by Lemma 3 it follows that

|At| ≫ δ2|B| δ2γδ−2fN (δ/8)2δ−2f N , so

dim(Z) ≪ η−1δ−3f ≪ δ−1/2−O(f) .

Put η1 = η and let Z1 ⊆ Y be any set of size Θ(η1−1δ−1+O(f)) such that dim(Z) ≪ η1−1δ−3f ≪ δ−1/2−O(f). Then we apply the above argument to the set Y \Z1 to ﬁnd Z2 ⊆ Y \Z1 and η2 ≫ δ1/2+O(f) with the same properties (observe that the whole argument can be applied

for any set Y ′ ⊆ Y giving essentially the same conclusion, as long as |Y ′| ≫ |Y |). Applying this procedure k times we obtain disjoint sets Z1,... ,Zk ⊆ Y such that |Zi| = Θ(ηi−1δ−1+O(f)) and dim(Zi) ≪ ηi−1δ−2f ≪ δ1−O(f)|Zi| for some ηi ≫ δ1/2+O(f), where k is the smallest integer such that

|Z1| + ··· + |Zk| δ−3/2 . Since for each i we have |Zi| δ−3/2 it follows that

|Z1| + ··· + |Zk| 2δ−3/2 . Put U = ki=1 Zi ⊆ X then |U| δ−3/2 and

k

k

|Zi| ≪ δ−1/2−O(f) .

dim(Zi) ≪ δ1−O(f)

dim(U + H) dim(H)

i=1

i=1

Again, by Lemma 11 we have |U + H| ≫ |U||H|1−10f ≫ δ−5/2+O(f) .

Lemma 5 implies that there exists a Bohr set B′ with rk(B′) ≪ δ−1/2−O(f) and radius Ω(δ1/2+O(f)) such that

|(A + t) ∩ B′| ≫ (1 + Ω(δ2+2µδ−5/2+O(f)))δ|B′| ≫ δ1/2+O(f)|B′| ≫ δ1−f|B′| (15) for some t which is a contradiction. ✷

# 7 Large Fourier coeﬃcients

In this section we obtain the density increment if (2) and (3) do not hold, so there is a kind of spectral gap in terms of L3-norm. We will use the well-known Chang’s Spectral Lemma [8], which states that for every θ we have

dim(∆θ) ≪ θ−2 log(1/δ). For any function f : ZN → R deﬁne

T(f) =

f(x)f(y)f(2z).

x+y=2z

We also make use of the following lower bound on the number of 3-term arithmetic progressions in a set S ⊆ Z/NZ with density γ proven by Bloom [4]

T(1A) γO(γ−1 log4(1/γ))N2.

- Lemma 14 Let A ⊆ Z/NZ, be a set with density δ such that (2) and (3) do not hold. Then there is a regular Bohr set B with rk(B) δ−2/5 and radius Ω(δ4) such that


for some t.

log(1/δ) log log5(1/δ)

|(A + t) ∩ B| ≫ µ

δ|B|

![image 47](<2020-schoen-improved-bound-roth-theorem_images/imageFile47.png>)

Proo f. By Chang’s lemma

dim(∆δ1/10) ≪ δ−1/5 log(1/δ) δ−2/5

hence there is a set Λ such that |Λ| ≪ δ−2/5 and ∆δ1/10 ⊆ Span (Λ). Let B = B(Λ,γ) be a regular Bohr set with radius γ ≫ δ3. Let β = |B1|1B then for every r ∈ ∆δ1/10 we have

![image 48](<2020-schoen-improved-bound-roth-theorem_images/imageFile48.png>)

β(r) − 1

1 |B| b∈B

|e−2πiλb/N − 1|

![image 49](<2020-schoen-improved-bound-roth-theorem_images/imageFile49.png>)

2π |B| b∈B λ∈Λ

![image 50](<2020-schoen-improved-bound-roth-theorem_images/imageFile50.png>)

rb/N 2πδ2 , (16)

and similarly | β(2r) − 1| ≪ δ2. Let f : ZN → [0,1] be a function deﬁned by f(t) = β ∗ 1A(t). We may assume that f(t) = |B1||(A + t) ∩ B| Lδ, where L = cµ

![image 51](<2020-schoen-improved-bound-roth-theorem_images/imageFile51.png>)

log(1/δ) log log5(1/δ) and c > 0 is a small constant. Put

![image 52](<2020-schoen-improved-bound-roth-theorem_images/imageFile52.png>)

S = t : f(t) δ/2

then by t f(t) = |A| it follows that |S| N/L hence by Bloom’s Theorem we have

1 8

δ3T(S) ≫ δ3 exp(−O(Llog5 L))N2 ≫ δ3+µ/10N2 . (17)

T(f)

![image 53](<2020-schoen-improved-bound-roth-theorem_images/imageFile53.png>)

Our next step is to compare T(f) and T(1A). By (16), (2), (3), Parseval’s formula and H¨older’s inequality we have

N−1

N−1

1 N

1A(r)2 1A(−2r) −

f(r)2 f(−2r) 1

T(1A) − T(f) =

![image 54](<2020-schoen-improved-bound-roth-theorem_images/imageFile54.png>)

r=0

r=0

2 N r ∈∆

| 1A(r)2 1A(−2r)(1 − β(r)2 β(−2r))| +

| 1A(r)|3

![image 55](<2020-schoen-improved-bound-roth-theorem_images/imageFile55.png>)

![image 56](<2020-schoen-improved-bound-roth-theorem_images/imageFile56.png>)

N r∈∆

δ1/10

δ1/10

2 N r ∈∆

2 N

1 N r∈∆

| 1A(r)|3 +

| 1A(r)|3 +

| 1A(r)|3

≪ δ2

![image 57](<2020-schoen-improved-bound-roth-theorem_images/imageFile57.png>)

![image 58](<2020-schoen-improved-bound-roth-theorem_images/imageFile58.png>)

![image 59](<2020-schoen-improved-bound-roth-theorem_images/imageFile59.png>)

r∈∆δ1+µ\∆δ1/10

δ1+µ

δ1/10

≪ δ2|A|2 + δ1+µ/5|A|2 + 2δ1+µ|A|2 ≪ δ3+µ/5N2 . Thus, by (17)

T(1A) ≫ δ3+µ/10N2 , which is a contradiction. ✷

- 8 Proof of Theorem 1 Summarizing all considered cases, we can state the following result.


Theorem 15 There exists an absolute constant c > 0 such that the following holds. Let A ⊆ Z/NZ be a set without any non-trivial arithmetic progressions of length three and let |A| = δN. Then there is a regular Bohr set B with rk(B) ≪ δ−1+c and radius Ω(δ4) such that for some t

log(1/δ) log log5(1/δ)

|(A + t) ∩ B| ≫

δ|B|.

![image 60](<2020-schoen-improved-bound-roth-theorem_images/imageFile60.png>)

Proo f. Let us ﬁrst make a suitable choice of parameters . Let µ > 0 be a constant the such that for every σ µ, (15) holds with f = f(16σ). Since we assumed that f(µ) µ, we see that in all considered cases in Lemma 7, Lemma 9, Lemma 12, Lemma 13 and Lemma 14 we obtain density increment at least by factor of Ω(µlog(1/δ)log log−5(1/δ)) on a Bohr set with rk(B) ≪ δ−1+µ/3 and radius Ω(δ4). Thus, it is enough to take c = µ/3. ✷

After the ﬁrst step of our iterative procedure we obtain a larger density increment on a low-rank Bohr set and then we apply less eﬀective method of Bloom (Theorem 7.1 [4]).

Lemma 16 [4] There exists an absolute constant c1 > 0 such that the following holds. Let B ⊆ Z/NZ be a regular Bohr set of rank d. Let A1 ⊆ B and A2 ⊆ Bε, each with relative densities αi. Let α = min(c1,α1,α2) and assume that d exp(c1(log2(1/α)). Suppose that Bε is also regular and c1α/(4d) ε c1α/d. Then either

- (i) there is a regular Bohr set B′ of rank rk(B′) d + O(α−1 log(1/α)) and size |B′| exp − O(log2(1/α)(d + α−1 log(1/α))) |B|

such that

|(A1 + t) ∩ B′| ≫ (1 + c1)α1|B′| for some t ∈ Z/NZ;

- (ii) or there are Ω(α21α2|B||Bε|) three-term arithmetic progressions x + y = 2z with x,y ∈ A1,z ∈ A2;


Now we are in position to ﬁnish the proof of our main result. We will not give detailed proof of the iteration procedure as it is very standard and the reader can ﬁnd details on it in the literature (see [4], [21]). In the ﬁrst step we apply Theorem 15 to obtain a regular Bohr set B0 with rk(B0) ≪ δ−1+c, radius Ω(δ4) and a progression-free set A0 ⊆ A + t for some t such that

|A0 ∩ B0| ≫ α|B0|, where

log(1/δ) log log5(1/δ)

δ .

α ≫

![image 61](<2020-schoen-improved-bound-roth-theorem_images/imageFile61.png>)

By Lemma 3 we have

|B0| exp − O(δ−1+c log(1/δ)) N .

Next we iteratively apply Lemma 16 and let Bi be Bohr sets obtained in the iterative procedure. Observe that after k ≪ log(1/α) steps we will be in the case (ii) of Lemma 16 and that rk(Bi) ≪ α−1 log2(1/α) for every i k. Thus, there are

Ω(α3|Bk||Bεk|) three-term arithmetic progressions in A, where ε c1α/(4rk(Bk)) ≫ α2 log2(1/α). Hence by Lemma 16 we have

|Bk| exp − O(α−1 log4(1/α)) N exp − O(δ−1 log3(1/δ))log log5(1/δ) N , and by Lemma 3

|Bεk| exp − O(α−1 log3(1/α)) exp − O(α−1 log4(1/α)) N

exp − O(δ−1 log3(1/δ)log log5(1/δ)) N . Therefore A contains

α3 exp − O(δ−1 log3(1/δ)log log5(1/δ)) N2

arithmetic progressions of length three. Since there are only |A| trivial progressions it follows that

|A| α3 exp − O(δ−1 log3(1/δ)log log5(1/δ)) N2 , which completes the proof of Theorem 1.

# 9 Concluding remarks

In Lemma 7, Lemma 9, Lemma 12 and Lemma 13 we obtained a density increment by factor of δ−c on a low-rank Bohr set, where c is a positive constant. Such density increment even in the ﬁrst step of an iterative method would lead to the upper bound O((log N)−1−c) in Theorem 1. However, in Lemma 14 we only were able to prove an increment by factor (log(1/δ))1−o(1). Any reﬁnement of Lemma 14 will directly imply an improvement of Theorem 1.

# References

- [1] M. Bateman, N. Katz, New bounds on cap sets, Journal of AMS 2 (2012), 585–613.
- [2] M. Bateman, N. Katz, Structure in additively nonsmoothing sets, arXiv:1104.2862v1 [math.CO] 14 Apr 2011.
- [3] F. A. Behrend, On sets of integers which contain no three terms in arithmetical progression, Proc. Nat. Acad. Sci. U. S. A. 32, (1946). 331–332.


- [4] T. Bloom, A quantitative improvement for Roth’s theorem on arithmetic progressions, J. Lond. Math. Soc. 93 (2016), 643–663.
- [5] T. Bloom, O. Sisask, Logarithmic bounds for Roth’s theorem via almost-periodicity, Discrete Analysis 4 (2019), 20 pp.
- [6] J. Bourgain, On triples in arithmetic progression, Geom. Funct. Anal. 9 (1999), 968–984.
- [7] J. Bourgain, Roth’s Theorem on Progressions Revisited, J. Anal. Math. 104 (2008), 155– 206.
- [8] M.–C. Chang, A polynomial bound in Freiman’s theorem, Duke Math. J. 3 (2002), 399– 419.
- [9] E. Croot, V. Lev, P. Pach, Progression-free sets in Zn4 are exponentially small, Ann. of Math. 185 (2017), 331–337.
- [10] M. Elkin, An Improved Construction of Progression-Free Sets, Israel J. Math. 184 (2011), 93–128.
- [11] J. Ellenberg, D. Gijswijt, On large subsets of Fnq with no three-term arithmetic progression Ann. of Math. 185 (2017), 339–343.
- [12] B. Green, Roths theorem in the primes, Ann. of Math. 161 (2005), 1609–1636.
- [13] B. Green and J. Wolf, A note on Elkin’s improvement of Behrend’s construction, in Additive Number Theory (Springer, New York, 2010), 141–144.
- [14] D. R. Heath-Brown, Integer sets containing no arithmetic progressions, J. Lond. Math. Soc. 35 (1987), 385–394.
- [15] H. Helfgott and A. de Roton, Improving Roths theorem in the primes, Int. Math. Res. Not. IMRN 4 (2011), 767–783.
- [16] E. Naslund, On improving Roth’s theorem in the primes, Mathematika 61 (2015), 49–62.
- [17] J. Pintz, W. L. Steiger, E. Szemer´edi, On sets of natural numbers whose diﬀerence set contains no squares, J. London Math. Soc. 37 (1988), 219-231.
- [18] K. F. Roth, On certain sets of integers, J. London Math. Soc. 28 (1953), 104–109.
- [19] R. Salem, D. C. Spencer, On sets of integers which contain no three terms in arithmetical progression, Proc. Nat. Acad. Sci. Wash., 28 (1942), 561 – 563.
- [20] T. Sanders, On a theorem of Shkredov, Online J. Anal. Comb. No. 5 (2010), Art. 5, 4 pp.
- [21] T. Sanders, On certain other sets of integers, J. Anal. Math. 116 (2012), 53–82.
- [22] T. Sanders, On Roth’s Theorem on Progressions, Ann. of Math. 174 (2011), 619–636.


- [23] T. Schoen, I. D. Shkredov, Additive dimension and a theorem of Sanders, J. Aust. Math. Soc. 100 (2016), 124–144.
- [24] T. Schoen, I. D. Shkredov, Roth’s theorem in many variables, Israel J. Math. 199 (2014), 287–308.
- [25] T. Schoen, O. Sisask, Roth’s theorem for four variables and additive structures in sums of sparse sets, Forum Math. Sigma 4 (2016), e5, 28 pp.
- [26] E. Szemer´edi, Integer sets containing no arithmetic progressions, Acta Math. Hungar. 56

(1990), 155–158.

- [27] E. Szemer´edi, Integer sets containing no k elements in arithmetic progression, Acta Arith. 27 (1975), 199–245.
- [28] I. D. Shkredov, On sets of large trigonometric sums, (Russian) Izv. Ross. Akad. Nauk Ser. Mat. 72 (2008), no. 1, 161–182; translation in Izv. Math. 72 (2008), 149–168.
- [29] I. D. Shkredov, On sumsets of dissociated sets, Online J. Anal. Comb. No. 4 (2009), 26 pp.
- [30] I. D. Shkredov, S. Yekhanin, Sets with large additive energy and symmetric sets, Journal of Combinatorial Theory, Series A 118 (2011), 1086–1093.
- [31] T. Tao, V. Vu, Additive combinatorics, Cambridge University Press 2006.


Faculty of Mathematics and Computer Science, Adam Mickiewicz University, Umultowska 87, 61-614 Poznan´, Poland schoen@amu.edu.pl

