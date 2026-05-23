arXiv:1106.1601v1[math.NT]8Jun2011

# Roth’s theorem in many variables

Tomasz Schoen∗ and Ilya D. Shkredov†

Abstract

We prove, in particular, that if A ⊆ {1,... ,N} has no nontrivial solution to the equation

- x1 + x2 + x3 + x4 + x5 = 5y then |A| ≪ Ne−c(logN)1/6−ε, c > 0. In view of the well-known Behrend construction this estimate is close to best possible.


## 1 Introduction

The celebrated theorem of Roth [14] asserts that every subset of {1, . . ., N} that does not contain any three term arithmetic progression has size O(N/ log log N). There are numerous reﬁnements of Roth’s result [2, 3, 8, 26]. Currently the best known upper bound O(N/(log N)1−o(1)) is due to Sanders [22]. The comprehensive history of the subject can be found in [27].

It turns out that the Roth’s method gives a similar upper bound for the size of sets having no nontrivial solutions to a invariant linear equation

a1x1 + · · · + akxk = 0, (1)

i.e. a1 + · · · + ak = 0, k 3 (three term arithmetic progressions corresponds to the equation x+y = 2z). On the other hand, the well-known construction of Behrend [1, 7, 9, 12, 13, 17, 18] provides large sets having no solution to certain kind of invariant equations. He showed that there are subsets of {1, . . ., N} of size Ne(−C

√logN) without solution to the invariant equation

![image 1](<2011-schoen-roth-theorem-many-variables_images/imageFile1.png>)

b,k

a1x1 + · · · + akxk = by, (2) where a1 + · · · + ak = b, ai > 0.

The aim of this paper is to establish a new upper bound for subsets of {1, . . ., N} having no solution to an invariant equation in at least 6 variables.

Theorem 1.1 Let N and k 6 be positive integers. Let A ⊆ {1, . . ., N} be a set having no solution to the equation (1), where all x1, . . ., xk, y are distinct integers. Then

|A| ≪ exp − c

log N log log N

![image 2](<2011-schoen-roth-theorem-many-variables_images/imageFile2.png>)

1/6

N , (3)

![image 3](<2011-schoen-roth-theorem-many-variables_images/imageFile3.png>)

∗The author is partly supported by MNSW grant N N201 543538. †The author is supported by grant RFFI NN 06-01-00383, 11-01-00759 and grant Leading Scientiﬁc Schools

No. 8684.2010.1

where c = c(a1, . . ., ak).

Observe, that Theorem 1.1 together with Behrend’s example give a reasonable estimates for all equations of the type (2). Let us also formulate an immediate corollary to Theorem 1.1 for the equation

x1 + x2 + x3 + x4 + x5 = 5y (4) which is very close to the most intriguing case x + y = 2z.

Corollary 1.2 Suppose that A ⊆ {1, . . ., N} has no solution to the equation (4) with distinct integers. Then there exists a constant c > 0 such that

|A| ≪ exp − c

log N log log N

![image 4](<2011-schoen-roth-theorem-many-variables_images/imageFile4.png>)

1/6

N .

Our argument heavily relies on a recent work on Polynomial Freiman-Ruzsa Conjecture, by Sanders [21] (see also [23]). A fundamental tool in our approach is a version of BogolyubovRuzsa Lemma proved in [21]. We also use the density increment method introduced by Roth, however in a diﬀerent way. The density increment is not deduced from the existence of a large Fourier coeﬃcient of a set A, |A| = αN, having no solution to an equation (1) (which is always the case). We will be rather interested in ﬁnding a translation of a large Bohr set in a1 · A + a2 · A + a3 · A + a4 · A, from which one can easily deduce a large density increment of A by a constant factor on some large Bohr set. By Sanders’ theorem dimension of the Bohr set increases by O(log4(1/α)) in each iteration step, which makes the argument very eﬀective.

The paper is organized as follows. We start with proving analogues of Theorem 1.1 and Corollary 1.2 for ﬁnite ﬁelds in section 3. The argument is especially simple and transparent in this case. Theorem 1.1 is proved in next three sections. In section 4 we recall some basic properties of Bohr sets in abelian groups. In section 5 we prove a local version of Sanders result. The next section contains the proof of Theorem 1.1. We conclude the paper with a discussion concerning consequences of Polynomial Freiman–Ruzsa Conjecture for sets having no solutions to an invariant linear equation with distinct integers.

## 2 Notation

Let G = (G, +) be a ﬁnite Abelian group with additive group operation +, and let N = |G|. By G we denote the Pontryagin dual of G, i.e. the space of homomorphisms γ from G to S1. It is well known that G is an additive group which is isomorphic to G. The Fourier coeﬃcients of f : G → C are deﬁned by

f(γ) =

f(x)γ(x).

![image 5](<2011-schoen-roth-theorem-many-variables_images/imageFile5.png>)

x∈G

By the convolution of two function f, g : G → C we mean (f ∗ g)(x) =

f(x)g(y − x).

x∈G

It is easy to see that f ∗ g(γ) = f(γ) g(γ). If X is a nonempty set, then by µX we denote the uniform probability measure on X and let

Specǫ(µX) := {γ ∈ G : | X(γ)| ǫ|X|}.

Let Zp = Z/pZ, and F∗p = Zp \ {0}. If A is a set, then we write A(x) for its characteristic function i.e. A(x) = 1 if x ∈ A and A(x) = 0 otherwise. All logarithms are to base 2. The signs ≪ and ≫ are usual Vinogradov’s symbols.

## 3 Finite ﬁelds model

In this section we present proofs of Corollary 1.2 and Theorem 1.1 in ﬁnite ﬁelds setting. Here we assume that a1, . . ., ak ∈ F∗p. The case of Fnp, in view of its linear space structure over Fp, is considerable simpler than the case of Z. Even the simplest version of Roth’s argument yields an estimate Op(pn/nk−2) for size of sets free of solution to (1) (see [11, 10], [19],[20]).

Our main tool is the following ﬁnite ﬁelds version of Sanders’ theorem [21]. Lemma 3.1 Suppose that A, S ⊆ Fnp are ﬁnite non–empty sets such that |A + S| ≤

K min{|A|, |S|}. Then A−A+S−S contains a subspace V of codimension at most Op(log4 K).

The proof of the next theorem illustrates the main idea of our approach. Theorem 3.2 Suppose that A ⊆ Fnp, p = 5, and A has no nontrivial solution to (4) with

- xi = y for some i. Then |A| pn · exp(−cp(log pn)1/5)


for some positive constant cp. Proof. Suppose that A ⊆ Fnp has density α and contains no solution to (4). We split A into two disjoint sets A1, A2 of equal size. Clearly, there exists z ∈ Fnp such that

|A1 ∩ (z − A2)| ≫ α2pn . Let us put B = A1 ∩ (z − A2).

By Lemma 3.1, there exists a subspace V of codimension at most Op(log4(1/α)) such that V ⊆ 2B − 2B, so that

2z + V ⊆ 2A1 + 2A2 .

Therefore, in view of A1 ∩A2 = ∅, we have 5y −x  ∈ 2z +V for all x, y ∈ A, hence A intersects at most half of cosets of V, which implies

|A ∩ (v + V )| ≥ 2α|V |,

for some v. Thus, (A−v)∩V is free of solutions to (4) and has density at least 2α on V. After t iterations we obtain a subspace of codimension at most Op(t · log4(1/α)) such that

|(A − vt) ∩ Vt| ≥ 2tα|Vt| ,

for some vt. Since the density is always at most one we can iterate this procedure at most log(1/α) + 1 times. Hence

(log(1/α) + 1) · log4(1/α) ≫p n,

so that

α exp(−cpn1/5) for some positive constant cp.

To prove the main result of the section we will need the following consequence of Lemma 3.1. We sketch its proof here; the interested reader will ﬁnd all details in Section 5.

Lemma 3.3 Let A1, . . ., Ak ⊆ Fnp be sets of density at least α. Then A1−A1+· · ·+Ak−Ak contains a subspace V of codimension at most Op(k−3 log4(1/α)). Proof. We have

|A1| ≤ |A1 + A2| ≤ · · · ≤ |A1 + · · · + Ak| ≤ α−1|A1|, so that there exists 2 ≤ i ≤ k such that

|A1 + · · · + Ai| ≤ α−1/(k−1)|A1 + · · · + Ai−1|.

Thus, setting A = A1 + · · · + Ai−1, S = T = Ai, we have |A + S| α−1/(k−1)|A|, |S + T| α−1|S|. Then applying Lemma 3.1 and Theorem 5.2 (see Section 5) we infer that there is a subspace V of codimension Op(log3(α−1/(k−1)) · log(1/α)) = Op(k−3 log4(1/α)) such that

v + V ⊆ A1 − A1 + · · · + Ai − Ai ⊆ A1 − A1 + · · · + Ak − Ak , and the assertion follows.

Theorem 3.4 Suppose that A ⊆ Fnp has no solution with distinct elements to an invariant equation

a1x1 + · · · + akxk = 0, (5) where a1, . . ., ak ∈ F∗p and k 6. Then

|A| kpn · exp(−cp(k3 log pn)1/5) . for a positive constant cp.

Proof. Suppose A ⊆ Fnp has no solution with distinct elements to (5) and |A| = αpn. Let A1, . . ., A2l, l = ⌊(k − 2)/2⌋ be arbitrary disjoint subsets of A of size ⌊|A|/(5k)⌋ and put A′ = A \ Ai. Clearly, there are z1, . . ., zl such that

|(a2i−1 · A2i−1) ∩ (zi − a2i · A2i)| ≫ (k/α)2pn

and let Bi, 1 i l, be the sets on the left hand side in the above inequalities, respectively. By Lemma 3.3, applied for B1, . . ., Bl and K = O((k/α)2) there is a subspace V of codimension d = Op(k−3 log4(k/α)) such that

V ⊆ B1 − B1 + · · · + Bl − Bl , so that

v + V ⊆ a1 · A1 + · · · + ak−2 · Ak−2

for some v. Since A does not contain any solution to (5) with distinct elements it follows that ak−1x + aky ∈/ v + V,

for all x, y ∈ A′, x = y. Hence, if for some w the coset w + V contains at least 2 elements of A′, then −a−k 1(ak−1w − v) + V is disjoint from A′. The number of cosets of V sharing exactly

- 1 element with A is trivially at most pd. Thus, there exists w′ such that |A′ ∩ (w′ + V )|

(4/5)αpn−pd

![image 6](<2011-schoen-roth-theorem-many-variables_images/imageFile6.png>)

pd/2 |V |, which is at least (3/2)α|V |, provided that pn−d ≫ α−1. (6)

After t iterates of this argument we obtain a subspace Vt of codimension Op(tk−3 log4(k/α)) such that

|(A − vt) ∩ Vt| (3/2)tα|Vt|. Since (3/2)tα 1 it follows that t 2 log(1/α). Thus, (6) must be violated after at most

- 2 log(1/α) steps, in particular pn−2 log(1/α)d ≪ α−1, so that k−3 log(1/α) log4(k/α) ≫p n/2 .


Hence α k exp(−cp(k3 log pn)1/5) .

## 4 Basic properties of Bohr sets

Bohr sets were introduced to additive number theory by Ruzsa [15]. Bourgain [2] was the ﬁrst, who used Fourier analysis on Bohr sets to improve estimate in Roth’s theorem. Sanders [21] further developed the theory of Bohr sets proving many important theorems, see for example

- Lemma 5.4 below. Let Γ be a subset of G, |Γ| = d, and ε = (ε1, . . ., εd) ∈ (0, 1]d. Deﬁnition 4.1 Deﬁne the Bohr set B = B(Γ, ε) setting


B(Γ, ε) = {n ∈ G : γj(n) < εj for all γj ∈ Γ} , where x = | arg x|/2π.

The number d is called dimension of B and is denoted by dimB. If M = B + n, n ∈ G, is a translation of a Bohr set B, we put dimM = dimB. The intersection B ∧ B′ of two Bohr sets B = B(Γ, ε) and B′ = B(Γ′, ε′) is the Bohr set with the generating set Γ ∪ Γ′ and new vector ε˜ = min(εj, ε′

j). We write B′ B for two Bohr sets B = B(Γ, ε), B′ = B(Γ′, ε′) if Γ ⊆ Γ′ and ε′

j εj, j ∈ [dimB]. Thus B′ ≤ B implies that B′ ⊆ B and always B∧B′ ≤ B, B′. Furthermore, if B = B(Γ, ε) and ρ > 0 then by Bρ we mean B(Γ, ρε).

Deﬁnition 4.2 A Bohr set B = B(Γ, ε) is called regular, if for every η, d|η| 1/100 we have

(1 − 100d|η|)|B1| < |B1+η| < (1 + 100d|η|)|B1| . (7)

We formulate a sequence of basic properties of Bohr (see [2]), which will be used later.

- Lemma 4.3 Let B(Γ, ε) be a Bohr set. Then there exists ε1 such that 2ε < ε1 < ε and

![image 7](<2011-schoen-roth-theorem-many-variables_images/imageFile7.png>)

B(Γ, ε1) is regular.

- Lemma 4.4 Let B(Γ, ε) be a Bohr set. Then

|B(Γ, ε)| ≥

N 2

![image 8](<2011-schoen-roth-theorem-many-variables_images/imageFile8.png>)

d

j=1

εj .

- Lemma 4.5 Let B(Γ, ε) be a Bohr set. Then |B(Γ, ε)| 8|Γ|+1|B(Γ, ε/2)| .
- Lemma 4.6 Suppose that B(1), . . ., B(k) is a sequence of Bohr sets. Then


k

B(i)) ≥

µG(

i=1

k

µG(B1(i/)2) .

i=1

The next lemma is due to Bourgain [2]. It shows the fundamental property of regular Bohr sets. We recall his argument for the sake of completeness.

Lemma 4.7 Let B = B(Γ, ε) be a regular Bohr set. Then for every Bohr set B′ = B(Γ, ε′) such that ε′ κε/(100d) we have:

- 1) the number of n′s such that (B ∗ B′)(n) > 0 does not exceed |B|(1 + κ),
- 2) the number of n′s such that (B ∗ B′)(n) = |B′| is greater than |B|(1 − κ) and (µB ∗ µB′)(n) − µB(n) 1 < 2κ. (8)


Proof. If (B ∗ B′)(n) > 0, then there exists m such that for any γj ∈ Γ, we have γj · m <

κ 100d

εj, γj · (n − m) < εj , so that

![image 9](<2011-schoen-roth-theorem-many-variables_images/imageFile9.png>)

κ 100d

γj · n < 1 +

εj ,

![image 10](<2011-schoen-roth-theorem-many-variables_images/imageFile10.png>)

for all γj ∈ Γ. Therefore n ∈ B+ := B Γ, 1 + 100κd ε and by Lemma 4.3, we have |B+| (1 + κ)|B|.

![image 11](<2011-schoen-roth-theorem-many-variables_images/imageFile11.png>)

On the other hand, if

κ 100d

n ∈ B− := B Γ, 1 −

ε , then (B ∗ B′)(n) = |B′|. Using Lemma 4.3, we obtain |B−| ≥ (1 − κ)|B|. To prove (8) observe that

![image 12](<2011-schoen-roth-theorem-many-variables_images/imageFile12.png>)

|B+| − |B−| |B|

(µB ∗ µB′)(n) − µB(n) 1 = (µB ∗ µB′)(n) − µB(n) l1(B+\B−)

< 2κ as required.

![image 13](<2011-schoen-roth-theorem-many-variables_images/imageFile13.png>)

Corollary 4.8 With the assumptions of Lemma 4.7 we have |B| |B + B′| |B+| (1 + κ)|B|.

Notice that for every γ ∈ Z∗p and a Bohr set B(Γ, ε) we have γ · B(Γ, ε) = B(γ−1 · Γ, ε). Thus, if B(Γ, ε) is a regular, then γ · B(Γ, ε) is regular as well.

## 5 A variant of Sanders’ theorem

Very recently Sanders [21] proved the following remarkable result.

Theorem 5.1 Suppose that G is an abelian group and A, S ⊆ G are ﬁnite non–empty sets such that |A + S| K min{|A|, |S|}. Then (A − A) + (S − S) contains a proper symmetric d(K)–dimensional coset progression M of size exp(−h(K))|A + S|. Moreover, we may take d(K) = O(log6 K), and h(K) = O(log6 K log log K).

The aim of this section is to show the following modiﬁcation of Sanders’ theorem which is crucial for our argument.

Theorem 5.2 Let ε, δ ∈ (0, 1] be real numbers. Let A, A′ be subsets of a regular Bohr sets B and let S, S′ be subsets of a regular Bohr sets Bε, where ε 1/(100d) and d = dimB. Suppose that µB(A), µB(A′), µB

(S′) α. Then the set (A − A′) + (S − S′) contains a translation of a regular Bohr set z + B˜ such that dimB˜ = d + O(log4(1/α)) and

(S), µB

ε

ε

|B˜| exp(−O(d log d + d log(1/ε) + log4(1/α) log d + log5(1/α) + d log(1/α)))|B| . (9)

Observe that the statement above with O(d4 + log4(1/α)) instead of d + O(log4(1/α)) is a direct consequence of Theorem 5.1 (see the beginning of the proof of Theorem 5.2).

Next we will formulate two results, which will be used in the course of the proof of Theorem 5.2. The ﬁrst lemma, proved by Sanders [21], is a version of Croot–Sisask theorem [6].

Lemma 5.3 Suppose that G is a group, A, S, T ⊆ G are ﬁnite non–empty sets such that |AS| K|A| and |TS| L|S|. Let ǫ ∈ (0, 1] and let h be a positive integer. Then there is t ∈ T and a set X ⊆ T − t, with

|X| exp(−O(ǫ−2h2 log K log L))|T| such that

|µA−1 ∗ AS ∗ µS−1(x) − 1| ǫ for all x ∈ Xh .

The next lemma is a special case of Lemma 5.3 from [21]. This is a local version of Chang’s spectral lemma [5], which is another important result recently proved in additive combinatorics.

Lemma 5.4 Let ǫ, ν, ρ be positive real number. Suppose that B is a regular Bohr set and let

X ⊆ B. Then there is a set Λ of size O(ǫ−2 log(2µ−B1/2(X))) such that for any γ ∈ Specǫ(µX) we have

|1 − γ(x)| = O(|Λ|(ν + ρdim2(B))) for all x ∈ Bρ ∧ Bν′ , where B′ = B(Λ, 1/2).

Proof of Theorem 5.2 Applying Lemma 5.3 with A, S and T = Bδ, δ = ε/100d and K = L = O(1/α), we ﬁnd a set X ⊆ Bδ − t such that

|X| exp(−O(ǫ−2h2 log2 K))|Bδ| , (10)

and

|µ−A ∗ (A + S) ∗ µ−S(x) − 1| ǫ/3 for all x ∈ hX . (11) We may assume that Bδ is regular.

Let ǫ be a small positive constant to be specify later. Put h = ⌈log(K/ǫ)⌉ and l = O(ǫ−4h2 log2 K). Applying Lemma 5.4 for X + t ⊆ Bδ with parameters ν = O(ǫ/(lK1/2)), ρ = O(ǫ/(ld2K1/2)), we obtain

|1 − γ(x)| ǫ/(3K1/2) for all x ∈ Bδρ ∧ Bν′ and γ ∈ Specǫ(µX) . (12) We have dim(Bδρ ∧ B′

ν) = d + O(log4(1/α)).

By the same argument, applied for sets A′, S′ there are sets X′, Λ′ of cardinality l and a Bohr set Bν∗ that satisfy inequalities (10) and (12), respectively. Finally, we set

B′′ = Bδρ ∧ Bν′ ∧ Bν∗.

Clearly, d′′ = dimB′′ = d + O(log4(1/α)) and by Lemma 4.4, Lemma 4.5, Lemma 4.6 and ǫ = Ω(1) we have

|B˜| exp(−O(d logd + d log(1/ε) + log4(1/α) log d + log5(1/α) + d log(1/α)))|B|. (13) In view of the inequality

γ

| (A + S)(γ) µA(γ) µS(γ)|

(|A + S||A|)1/2 |S|

![image 14](<2011-schoen-roth-theorem-many-variables_images/imageFile14.png>)

K1/2,

which follows from Cauchy-Schwarz inequality and Parseval’s formula, we may proceed in the same way as in the proof of Lemma 9.2 in [21] and conclude that for any probability measure µ supported on B′′ we have

(A + S) ∗ µ ∞ 1 − ǫ and (A′ + S′) ∗ µ ∞ 1 − ǫ. (14) Let η = 1/4d′′. We show that (A − A′) + (S − S′) contains a translation of B˜ := B′′

η. Indeed, note that

B1′′/2 ⊆ B1′′/2+η ⊆ · · · ⊆ B1′′/2+2d′′η = B′′ . so that by pigeonhole principle, there is some i ≤ 2d′′ such that |B′′ 1/2+iη|

√2|B′′

![image 15](<2011-schoen-roth-theorem-many-variables_images/imageFile15.png>)

1/2+(i−1)η|. We apply (14) for

B1′′/2+iη + B1′′/2+(i−1)η |B′′

.

µ =

![image 16](<2011-schoen-roth-theorem-many-variables_images/imageFile16.png>)

1/2+iη| + |B′′

1/2+(i−1)η|

Thus, there is x such that

|(x + A + S) ∩ B1′′/2+iη| + |(x + A + S) ∩ B1′′/2+(i−1)η| (1 − ǫ) |B1′′/2+iη| + |B1′′/2+(i−1)η| . Taking ǫ suﬃciently small (see [21] for details), we get

|(x + A + S) ∩ B1′′/2+iη|

- 3

![image 17](<2011-schoen-roth-theorem-many-variables_images/imageFile17.png>)

- 4|B1′′/2+(i−1)η| , |(x + A + S) ∩ B1′′/2+(i−1)η|


- 3

![image 18](<2011-schoen-roth-theorem-many-variables_images/imageFile18.png>)

- 4|B1′′/2+(i−1)η| .


Analogously, for some y, we obtain

- 3

![image 19](<2011-schoen-roth-theorem-many-variables_images/imageFile19.png>)

- 4|B1′′/2+(i−1)η| , |(y + A′ + S′) ∩ B1′′/2+(i−1)η|


- 3

![image 20](<2011-schoen-roth-theorem-many-variables_images/imageFile20.png>)

- 4|B1′′/2+(i−1)η| .


|(y + A′ + S′) ∩ B1′′/2+iη| Hence for each b ∈ B˜, we have (A + S) ∗ (−A′ − S′)(b + y − x) = (x + A + S) ∗ (−y − A′ − S′)(b)

((x + A + S) ∩ B1′′/2+iη) ∗ ((−y − A − S) ∩ B1′′/2+(i−1)η)(b) |(x + A + S) ∩ B1′′/2+iη| + |(y + A + S) ∩ B1′′/2+(i−1)η|

− |((x + A + S) ∩ B1′′/2+iη) ∩ ((−y − A − S) ∩ B1′′/2+iη)| 3 2|B1′′/2+(i−1)η| − |B1′′/2+iη| > 0 .

![image 21](<2011-schoen-roth-theorem-many-variables_images/imageFile21.png>)

Therefore, (A − A′) + (S − S′) contains a translation of B˜. Finally, by Lemma 4.3, there is 1/2 σ 1 such that B˜σ is regular. By (13) and Lemma 4.5 B˜σ also satisﬁes (9). This completes the proof.

## 6 Proof of the main result

Let A ⊆ {1, . . ., N} be a set having no solution to (1). As usually, we embed A in Zp with p between ( |ai|)N and 2( |ai|)N, so A has no solution to (1) in Zp. All sets considered below are subsets of Zp. We start with the following simple observation.

Lemma 6.1 Let B be a regular Bohr set of dimension d, B′ ≤ Bρ be a Bohr set and ρ α/(1600d). Suppose that µB(A), µB(A′) α. Then there exists x ∈ B such that

(µB′ ∗ A)(x), (µB′ ∗ A′)(−x) α/4 (15) or

µB′ ∗ A ∞ 1.5α or µB′ ∗ A′ ∞ 1.5α (16) Proof. By regularity of B we have

1 |B| x∈B

(µB′ ∗ A)(x)

(µB ∗ µB′)(x)A(x) α/8 +

α

µB(x)A(x) α/8 +

![image 22](<2011-schoen-roth-theorem-many-variables_images/imageFile22.png>)

x∈B

x∈B

and

1 |B| x∈B

(µB′ ∗ A′)(x). Hence

α α/8 +

![image 23](<2011-schoen-roth-theorem-many-variables_images/imageFile23.png>)

((µB′ ∗ A)(x) + (µB′ ∗ A′)(−x)) (7α/4)|B|

x∈B

and the result follows. Theorem 1.1 is a consequence of the next lemma. Lemma 6.2 Suppose that B is a regular Bohr set of dimension d and A ⊆ B, µB(A) = α

has no solution with distinct elements to (1). Assume that |B| exp(O(d logd + log5(1/α) + d log(1/α) + log d log4(1/α) + d logk)). (17)

Then there exists a regular Bohr set B′, such that

µB′ ∗ A ∞ (1 + 1/(16k))α , (18) dimB′ = d + O(log4(1/α)), and

|B′| exp(−O(d log d + log5(1/α) + d log(1/α) + log d log4(1/α)))|B| . (19)

Proof. We start with mimicking the argument used by Sanders in [22]. Suppose that ε = cα/(100Mdk2), where c > 0 is a small constant and M = |ai|, is such that Bε is a regular Bohr set and put Bi = ( j =i aj) · Bε. By Lemma 4.7, we have

k · (A ∗ µB) −

k

A ∗ µB ∗ µBi ∞ 2kcα . (20)

i=1

Thus, for η = 1/(16k), either we have µBi ∗ A ∞ (1 + η)α for some 1 i k, or there is w ∈ B such that µBi(A+w) = µB′(ai·(A+w)) (1−kη)α for every i, where B′ = ( aj)·Bε. In the ﬁrst case we are done, so assume that the last inequalities hold. Since (1) is an invariant equation we may translate our set and assume that µB′(ai · A) (1 − kη)α for all 1 i k.

ε are regular Bohr sets. By regularity of B′ and

ε and B′′

ε/2 ⊆ B′′′ ⊆ B′′

Let B′

ε/2 ⊆ B′′ ⊆ B′

- Lemma 6.1 either (16) holds, and we are done, or there exists x ∈ B′ with µB′′+x(a1 · A) α/8 and µB′′−x(a2 · A) α/8. We show that there are disjoint sets A1, A2 of A such that α/32 µB′′+x(a1 · A1) α/16 and α/32 µB′′−x(a2 · A2) α/16. Indeed, let Q1 = {q ∈ A : a1 · q ∈ B′′ + x}, Q2 = {q ∈ A : a2 · q ∈ B′′ − x}. Note that |Q1|, |Q2| ≥ α|B′′|/8. If |Q1 ∩ Q2| > α|B′′|/16 then split Q1 ∩ Q2 into two parts A1, A2 whose sizes diﬀer by at most one. Otherwise, we put A1 = Q1 \ Q2 and A2 = Q2 \ Q1.


Put A′ = A \ (A1 ∪ A2) then µB′(ai · A′) 3α/4 for i ≥ 3. Again applying Lemma 6.1 for B′′′ and the arguments above, we ﬁnd y ∈ B′ and disjoint sets A3, A4 ⊆ A′ such that µB′′′+y(a3 · A3) α/16 and µB′′′−y(a4 · A4) α/16.

Assume that k is even. Let l = (k − 6)/2 ≥ 0. Using the arguments as before, we infer that then there are disjoint sets A5, . . ., Ak−2 and elements y1, . . ., yl such that

a5 · A5 − y1 ⊆ B′′, −a6 · A6 − y1 ⊆ B′′, . . ., ak−3 · Ak−3 − yl ⊆ B′′, −ak−2 · Ak−2 − yl ⊆ B′′ and

α 16k

µB′′+y1(a5 · A5), µB′′−y1(a6 · A6) , . . . , µB′′+yl(ak−3 · Ak−3), µB′′−yl(ak−2 · Ak−2) ≥

.

![image 24](<2011-schoen-roth-theorem-many-variables_images/imageFile24.png>)

Finally, by Theorem 5.2 applied to sets

a1 · A1 − x ⊆ B′′, −a2 · A2 − x ⊆ B′′, a3 · A3 − y ⊆ B′′′, −a4 · A4 − y ⊆ B′′′, there exists a Bohr set B˜ ≤ B′ and z such that

k−2

B˜ + z ⊆ a1 · A1 + a2 · A2 + a3 · A3 + a4 · A4 +

aj · Aj , (21)

j=5

d˜= dimB˜ = d + O(log4(1/α)) and |B˜| exp(−O(d logd + log5(1/α) + d log(1/α) + log d log4(1/α)))|B| . (22)

The sum over j in (21) can be empty. In the case we put the sum to be equal to zero. Notice that z ∈ 4B′′ + (k − 6)B′′′ ⊆ kB′′. Since A1, . . ., Ak−2 are disjoint it follows that

ak−1xk−1 + akxk ∈/ B˜ − z (23) for all distinct xk−1, xk ∈ A \ ∪jk=1−2Aj.

By Lemma 4.3 we ﬁnd 1/(400kd˜) δ 1/(200kd˜) such that B˜δ is regular. Obviously B˜δ satisﬁes (22). Write

∗ (ai · A))(x) k/|B˜δ|} .

Ei := {x ∈ B′ : (µB˜

δ

Observe that if −z ∈ Ek−1+Ek, then one can ﬁnd a solution to (1) with distinct x1, . . ., xk ∈ A. Therefore Ek−1 ⊆ B′ \ (−Ek − z), so that

|Ek−1| |B′ \ (−Ek − z)| = |B′| − |B′ ∩ (Ek + z)| |B′| − |Ek| + 100εMdk|B′| . Finally

|Ek−1| + |Ek| (3/2)|B′|, so that |Ei| (3/4)|B′| for some i. Thus

∗ (ai · A) ∞|Ei| + (k/|B˜δ|)|B1+′ δ| . By (17)

∗ (ai · A) 1 µB˜

|A| = µB˜

δ

δ

|B˜δ| exp(O(−(d log d + log5(1/α) + d log(1/α) + log d log4(1/α))))|B| 10 · 8d+1k/α , and since Lemma 4.5 implies |B′

1+δ| 2|B′|, so that µB˜

∗ (ai · A) ∞|Ei||B˜δ| 0.9|B˜δ||A|. Hence

δ

µB∗ ∗ A ∞ 1.1α, where B∗ = a−i 1 · B˜δ, and the assertion follows.

Now suppose that k is odd. Only the ﬁrst part of the proof needs to be slightly modiﬁed. Certainly, we may assume that a5 = 1. By regularity of B we have

k · (A ∗ µB) − A ∗ µB ∗ µB′′ −

A ∗ µB ∗ µBi ∞ 2kcα , (24)

i =5

where Bi and B′′ are deﬁned as before. Put l = (k−7)/2 ≥ 0. By Lemma 6.1 there are disjoint sets A1, . . ., Ak and elements x, y, y1, . . ., yl such that (21)–(23) hold. However, A5 ⊆ B′′, so that z ∈ kB′′. One can ﬁnish the proof in exactly the same way as before.

Proof of Theorem 1.1 Let A ⊆ B0 = Zp, |A| αp. We apply iteratively Lemma 6.2. After t steps we obtain a regular Bohr set Bt and xt ∈ Zp such that |A ∩ (Bt + xt)| (1 + 1/(16k))tα|Bt|, dimBt ≪ tlog4(1/α), and

|Bt| exp(−O(tlog4(1/α) log log(1/α) + log5(1/α)))|Bt−1|.

Since the density is always less than 1 we may apply Lemma 6.2 at most O(log(1/α)) times. Therefore, after t = O(log(1/α)) iterates assumption of Lemma 6.2 are violated, so that

exp(−O(log6(1/α) loglog(1/α)))p |Bt| exp(O(log5(1/α))), which yields

α ≪ exp(−c(log p/ log log p)1/6), and the assertion follows.

## 7 Polynomial Freiman–Ruzsa Conjecture and linear equation

Freiman-Ruzsa Polynomial Conjecture can be formulated in the following way.

Conjecture 7.1 Let A ⊆ ZN, |A| = αN, then there exists a Bohr set B(Γ, ε) ⊆ 2A − 2A such that |Γ| = d ≪ log(1/α) and ε ≫ 1/ log(1/α).

We have

- 1

![image 25](<2011-schoen-roth-theorem-many-variables_images/imageFile25.png>)

- 2


εdN,

|B(Γ, ε)|

so that it would give a nontrivial result provided that α ≫ N−c/log logN. However, it was proved in [24] and [25] that in Chang’s lemma (see section 5) one can take much larger ε. This give a (little) support for the following version of the above conjecture for sparse sets.

Conjecture 7.2 Let A, A′ ⊆ ZN, |A|, |A′| N1−c, then there exists a δc log N−dimensional Bohr set B ⊆ A − A + A′ − A′ such that |B| ≫ N1−c′ and δc → 0, c′ → 0 with c → 0. Furthermore, each b ∈ B has ≫ |A|2|A′|2/N representations in the form a − b + a′ − b′, a, b ∈ A, a′, b′ ∈ A′.

We shall give here an application of Conjecture 7.2. First we recall some deﬁnitions from [16]. Let

a1x1 + · · · + akxk = 0 (25)

be an invariant linear equation. We say that the solution x1, . . ., xk of (25) is trivial if there is a partition {1, . . ., k} = T1 ∪ · · · ∪ Tl into nonempty and disjoint sets Tj such that xu = xv if and only if u, v ∈ Tj for some j and

ai = 0,

i∈Tj

for every 1 j l. The genus of (25) is the largest g such that there is a partition {1, . . ., k} = T1 ∪ · · · ∪ Tg into nonempty and disjoint sets Tj such that

ai = 0,

i∈Tj

for every 1 j g. Let r(N) be the maximum size of a set A ⊆ {1, . . ., N} having no nontrivial solution to (25) with xi ∈ A and let R(N) be the analogous maximum over sets

that the equation (25) has no solution with distinct xi ∈ A. It is not hard to prove that r(N) ≪ N1/g. Much less is known about the behavior of R(N). Bukh [4] showed that we always have R(N) ≪ N1/2−ε for the symmetric equations

a1x1 + · · · + alxl = a1y1 + · · · + alyl. Our result is the following.

Theorem 7.3 Assuming Conjecture 7.2 we have R(N) ≪ N1−c, for every invariant equation (25) with a1 = −a2, a3 = −a4, where c = c(a1, . . ., ak).

Proof. Suppose that A has no solution to an equation (25) with a1 = −a2, a3 = −a4, where c = c(a1, . . ., ak) and assume that |A| ≫ N1−c, c > 0. We embed A in ZM with M = SN, where S = |ai|, so that any solution to (25) in ZM is a genuine solution in Z. Let A = A1∪A2 be a partition of A into roughly equal parts. If Conjecture 7.2 holds, then there is a Bohr set

B ⊆ a1 · A1 − a1 · A1 + a3 · A1 − a3 · A1

of dimension at most δc log N and size at least ≫ N1−c′. Put B′ = B1/S. We show that for every t ∈ ZM we have

|(t + B′) ∩ A2| k − 4. Indeed, if there are distinct x5, . . ., xk ∈ (t + B′) ∩ A2, then

k

k

aixi ∈

ait + B = B.

i=5

i=5

However, each element in B has at least |A|4/M representations in the form a1x−a1y +a3z − a3w, x, y, z, w ∈ A1. This would give a solution to (25) with distinct integers. Hence,

|B′||A2| =

t

|(t + B′) ∩ A2| kM

so

|A| 2kSN/|B′|.

Now, by Lemma 4.5 it follows that |B′| ≫ S−4d|B| ≫ N1−c′−2δclogS. This leads to a contradiction, provided c is small enough.

Acknowledgement We wish to thank Tom Sanders for stimulating discussions.

## References

- [1] F. A. Behrend, On sets of integers which contain no three terms in arithmetic progression, Proc. Nat. Acad. Sci. 23 (1946), 331–332.
- [2] J. Bourgain, On triples in arithmetic progression, Geom. Funct. Anal. 9 (1999), 968– 984.


- [3] J. Bourgain, Roth’s Theorem on Progressions Revisited, J. Anal. Math. 104 (2008), 155–192.
- [4] B. Bukh, Non-trivial solutions to a linear equation in integers, Acta Arth. 131 (2008), 51–55.
- [5] M. C. Chang, A polynomial bound in Freiman’s theorem, Duke Math. J. 113 (2002), 399–419.
- [6] E. Croot, O. Sisask, A probabilistic technique for ﬁnding almost–periods of convolutions, Geom. Funct. Anal. 20 (2010), 1367-1396.
- [7] M. Elkin, An Improved Construction of Progression-Free Sets, Israel J. Math, to appear.
- [8] D. R. Heath–Brown, Integer sets containing no arithmetic progressions, J. London Math. Soc. 35 (1987), 385–394.
- [9] P. Koester, An extension of Behrend’s theorem, J. Anal. Comb. 8 (2008)
- [10] Y. R. Liu, C. V. Spencer, A generalization of Meshulam’s theorem on subsets of ﬁnite abelian groups with no 3–term arithmetic progression, Des. Codes Cryptogr., 52 (2009), 83–91.
- [11] R. Meshulam, On subsets of ﬁnite abelian groups with no 3–term arithmetic progressions, J. Combin. Theory Ser. A, 71(1995), 168–172.
- [12] L. Moser, On non–averaging sets of integers, Canad. Math. J., 5 (1953), 245–252.
- [13] R. A. Rankin, Sets of Integers Containing not more than a Given Number of Terms in Arithmetic Progression, Proc. Roy. Soc. Edinburgh 65 (1961), 332–344.
- [14] K. F. Roth, On certain sets of integers, J. London Math. Soc. 28 (1953), 104–109.
- [15] I. Z. Ruzsa, Generalized arithemtic progresions and sumsets, Acta Math. Hung. 65

(1994), 379–388.

- [16] I. Z. Ruzsa, Solving linear equations in sets of integers. I, Acta Arith. 65 (1993), 259– 282.
- [17] R. Salem, D. C. Spencer, On sets of integers which contain no three terms in arithmetical progression, Proc. Nat. Acad. Sci. Wash., 28 (1942), 561 – 563.
- [18] R. Salem, D. C. Spencer, On sets which do not contain a given number of terms in arithmetical progression, Nieuw Arch. Wisk., 23 (1950), 561 – 563.
- [19] T. Sanders, Roth’s theorem in Zn4, Anal. PDE 2 (2009), 211-234.
- [20] T. Sanders, Structure in sets with logarithmic doubling, Canad. Math. Bull., to appear.
- [21] T. Sanders, On the Bogolubov–Ruzsa Lemma, preprint.
- [22] T. Sanders, On Roth’s Theorem on Progressions, Ann. of Math., to appear.
- [23] T. Schoen, Near optimal bounds in Freiman’s theorem, Duke Math. J. 158 (2011), 1–12.


- [24] I. D. Shkredov, On Sets of Large Exponential Sums, Izvestiya of Russian Academy of Sciences, 72 (2008), 161–182.
- [25] I. D. Shkredov, Some Examples of Sets of Large Exponential Sums, Mat. Sbornik, 198 (2007), 105–140.
- [26] E. Szemer´edi, On sets of integers containing no arithmetic progressions, Acta Math. Hungar., 56 (1990), 155–158.
- [27] T. Tao, V. Vu, Additive combinatorics, Cambridge University Press 2006.


Faculty of Mathematics and Computer Science, Adam Mickiewicz University, Umultowska 87, 61-614 Pozna´n, Poland schoen@amu.edu.pl

Division of Algebra and Number Theory, Steklov Mathematical Institute, ul. Gubkina, 8, Moscow, Russia, 119991 ilya.shkredov@gmail.com

