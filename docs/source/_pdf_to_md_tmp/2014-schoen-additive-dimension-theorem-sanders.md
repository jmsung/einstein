arXiv:1404.2044v1[math.CO]8Apr2014

Additive dimension and a theorem of Sanders

By Tomasz Schoen∗ and Ilya D. Shkredov†

Abstract

We prove some new bounds for the size of the maximal dissociated subset of structured (having small sumset, large energy and so on) subsets A of an abelian group.

- 1 Introduction Let G be an abelian group. A ﬁnite set Λ ⊆ G is called dissociated if any equality of the form


ελλ = 0

λ∈Λ

for ελ ∈ {−1,0,1} implies ελ = 0 for all λ. In many problems of additive combinatorics (see e.g. [1, 2, 3, 4, 7, 17, 19, 20]) it is important to control the maximal (by cardinality) dissociated subset of A, which we call the (additive) dimension of the set A. The ﬁrst general theorem on dimension of so–called large spectrum of a set was obtained in [7]. For further results see [4, 5, 16, 17, 26]. Let us recall two theorems proved in [17] and [26], respectively, which we will apply later.

- Theorem 1 Let A,B ⊆ G be ﬁnite sets and suppose that |A + B| K|A|. Then dim(B) ≪ K log |A|.
- Theorem 2 Let A,B ⊆ G be ﬁnite sets and suppose that E(A,B) |A||B|2/K. Then there exist a set B1 ⊆ B such that dim(B1) ≪ K log |A| and


E(A,B1) 2−5E(A,B). (1)

In particular, |B1| 2−3K−1/2|B|. If B = A then E(B1) 2−10E(A) and, consequently, |B1| 2−4K−1/3|A|.

![image 1](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile1.png>)

∗The author is supported by NCN 2012/07/B/ST1/03556. †This work was supported by grant RFFI NN 11-01-00759, Russian Government project 11.G34.31.0053,

Federal Program ”Scientiﬁc and scientiﬁc–pedagogical staﬀ of innovative Russia” 2009–2013, grant mol a ved 12–01–33080 and grant Leading Scientiﬁc Schools N 2519.2012.1.

![image 2](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile2.png>)

![image 3](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile3.png>)

1

The aim of this paper is to obtain some further estimates on dimensions of sets. First of all, we give a simple combinatorial proof of Theorem 1 and reﬁne the result in the case of small doubling constant K, see Theorem 13. Furthermore, we generalize Theorem 2 for the case of another sorts of energies and improve it by ﬁnding subset having even smaller additive dimension (see Theorems 20, 23). In section 6 we present an application of our results. In the last section we reformulate some results from the papers [1], [2] in terms of the additive dimensions and prove them for general abelian groups.

The Polynomial Freiman–Ruzsa Conjecture (PFRC) roughly states (see for details [9]) that every set A with |A + A| K|A| contains highly structured subset of size |A|/KO(1).

If PFRC holds then for every set A with |A + A| K|A| there is a subset B ⊆ A, |B| ≫ K−C|A| with dim(A) ≪ Ko(1) log |A|, as K → ∞. Our results provide bounds of the form dim(A) ≪ Kc log |A|, where c > 0 are some constants, which are much weaker than one could expect from PFRC. However, our theorems are still applicable because in our results size of the set B is large and explicit, which is crucial, for example, in problems concerning sets without solutions to a linear equation, see e.g. [1, 17].

I.D.S. is grateful of S.V. Konyagin for very fruitful discussions.

# 2 Notation

Let G be an abelian group. If G is ﬁnite then denote by N the cardinality of G. It is well– known [12] that the dual group G is isomorphic to G in the case. Let f be a function from G to C. We denote the Fourier transform of f by f,

f(ξ) =

f(x)e(−ξ · x), (2)

x∈G

where e(x) = e2πix. We rely on the following basic identities

and

If

then

1 N

|f(x)|2 =

![image 4](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile4.png>)

x∈G

2

f(x)g(y − x)

=

y∈G x∈G

f(ξ) 2 . (3)

ξ∈ G

1 N

![image 5](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile5.png>)

ξ∈ G

f(ξ) 2 g(ξ) 2 . (4)

1 N

f(x) =

![image 6](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile6.png>)

f(ξ)e(ξ · x). (5)

ξ∈ G

(f ∗ g)(x) :=

f(y)g(x − y) and (f ◦ g)(x) :=

y∈G

f(y)g(y + x)

y∈G

![image 7](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile7.png>)

f ∗ g = f g and f ◦ g = fc g = f g , (6)

![image 8](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile8.png>)

where for a function f : G → C we put fc(x) := f(−x). Clearly, (f ∗ g)(x) = (g ∗ f)(x) and (f ◦g)(x) = (g◦f)(−x), x ∈ G. The k–fold convolution, k ∈ N we denote by ∗k, so ∗k := ∗(∗k−1).

The characteristic function of a set S ⊆ G we denote by S(x). Write E(A,B) for the additive energy of sets A,B ⊆ G (see e.g. [27]), that is

E(A,B) = |{a1 + b1 = a2 + b2 : a1,a2 ∈ A, b1,b2 ∈ B}|. If A = B we simply write E(A) instead of E(A,A). Clearly,

E(A,B) =

x

(A ∗ B)(x)2 =

x

(A ◦ B)(x)2 =

x

(A ◦ A)(x)(B ◦ B)(x), (7)

and by (4),

1

N ξ | A(ξ)|2| B(ξ)|2 . (8) Let

E(A,B) =

![image 9](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile9.png>)

Tk(A) := |{a1 + ··· + ak = a′1 + ··· + a′k : a1,... ,ak,a′1,... ,a′k ∈ A}|. Clearly, Tk(A) = N1 ξ | A(ξ)|2k. For A1,... ,A2k ⊆ G let

![image 10](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile10.png>)

Tk(A1,... ,A2k) := |{a1 + ··· + ak = ak+1 + ··· + a2k : ai ∈ Ai, i ∈ [2k]}|. Put also

σk(A) := (A ∗k A)(0) = |{a1 + ··· + ak = 0 : a1,... ,ak ∈ A}|. Notice that for a symmetric set A that is A = −A one has σ2(A) = |A| and σ2k(A) = Tk(A).

For a sequence s = (s1,... ,sk−1) put ABs = B ∩ (A − s1)··· ∩ (A − sk−1). If B = A then write As for AAs . Let

(A ◦ A)(x)k =

|As|2 (9)

Ek(A) =

x∈G

s1,...,sk−1∈G

and

(A ◦ A)(x)(B ◦ B)(x)k−1 =

|BsA|2 (10)

Ek(A,B) =

x∈G

s1,...,sk−1∈G

be the higher energies of A and B. The second formulas in (9), (10) can be considered as the deﬁnitions of Ek(A), Ek(A,B) for non integer k, k 1.

For a positive integer n, we set [n] = {1,... ,n}. All logarithms used in the paper are to base 2. Signs ≪ and ≫ are the usual Vinogradov symbols. If p is a prime number then write Fp for Z/pZ and F∗p for (Z/pZ) \ {0}.

# 3 Preliminaries

In this section we recall some results, which we will need in the paper.

First of all, it was proved by Rudin [12] that all norms of Fourier transform of a function with support on a dissociated set are equivalent.

- Lemma 3 Let Λ ⊆ ZN be a dissociated set and let an be any complex numbers. Then for each

- p 2 we have 1


![image 11](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile11.png>)

N

N−1

x=0

|

n∈Λ

ane−2πinx/N|p (Cp)p/2

n∈Λ

|an|2

p/2

,

for some absolute constant C.

A consequence of the above lemma is the following result due of Sanders [16]. (Similar results were obtained by Bourgain [5] and by the second author [23].)

- Lemma 4 Let G be a ﬁnite abelian group, Q ⊆ G be a set and l be a positive integer. There is a partition Q = Qstr ∪ Qdiss such that dim(Qstr) < l and Qdiss is a union of dissociated sets of sizes l. Moreover for all p 2 the following holds

1 N ξ | Qdiss(ξ)|p

![image 12](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile12.png>)

1/p

≪ p/l · |Q|. (11)

![image 13](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile13.png>)

We will also make use of a known Chang’s Covering Lemma [7] and Plu¨nnecke–Ruzsa inequality, see [14], [15] or [27].

- Lemma 5 Let L,K be real numbers, and A,B ⊆ G be two sets. If |A + A| K|A| and |A + B| L|B| then there are sets S1,... ,Sl each of size at most 2K such that A ⊆ B − B + (S1 − S1) + ··· + (Sl − Sl) and l log(2KL).
- Lemma 6 Let j < k be positive integers. Let also A,B be ﬁnite set of an abelian group such that |A + jB| K|A|. Then there is a nonempty set X ⊆ A such that

|X + kB| Kk/j|X|. (12) In particular, if |A + A| K|A| then

|mA − nA| Kn+m|A| (13)

for all n,m ∈ N. Furthermore, for ﬁxed j 1 and arbitrary 0 < δ < 1 there exists X ⊆ A such that |X| (1 − δ)|A| and

|X + kB| (K/δ)k|X|. (14) We will also make use of some results concerning higher additive energies (see [22] and [25]).

- Lemma 7 Let A be a subset of an abelian group. Then for every k,l ∈ N


E(As,At) = Ek+l(A),

s,t: s =k−1, t =l−1

where x denote the number of components of vector x.

- Theorem 8 Let A be a ﬁnite subset of an abelian group. Suppose that E(A) = |A|3/K, and

E3+ε = M|A|4+ε/K2+ε, where ε ∈ (0,1]. Put P := {x : (A ◦ A)(x) |A|/2K}. Then |P| ≫ K|A|/M2/(1+ε) and E(P) ≫ M−β|P|3, where β = (3 + 4ε)/(ε(1 + ε)).

- Theorem 9 Let A ⊆ G be a ﬁnite set, and l 2 be a positive integer. Then |A|8

![image 14](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile14.png>)

8E3(A)

l

Tl(A)|A − A|2l+1 , (15)

Another relations between Es and Ts can be found in [22], [24].

- Theorem 10 Let A ⊆ G be a ﬁnite set. Suppose that Es(A) = |A|s+1/Ks−1, s ∈ (1,3/2] and T4(A) := M|A|7/K3, then

E4(A) ≫s−1

|A|5 MK

![image 15](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile15.png>)

.

By an arithmetic progression of dimension d and size L we mean a set of the form

Q = {a0 + a1x1 + ··· + adxd : 0 xj < lj}, (16)

where L := l1 ... ld. Q is said to be proper if all of the sums in (16) are distinct. By a proper coset progression of dimension d we will mean a subset of G of the form Q + H, where H ⊆ G is a subgroup, Q is a proper progression of dimension d and the sum is direct in the sense that q + h = q′ + h′ if and only if h = h′ and q = q′. By the size of a proper coset progression we mean simply its cardinality.

Finally, let us recall the main result proved in [18].

- Theorem 11 Suppose that G is an abelian group and A,S ⊆ G are ﬁnite non–empty sets such that |A + S| K min{|A|,|S|}. Then (A − A) + (S − S) contains a proper symmetric d(K)– dimensional coset progression P of size exp(−h(K))|A + S|. Moreover, we may take d(K) = O(log6 K), and h(K) = O(log6 K log log K).


- 4 Additive dimension of sets with small doubling At the beginning we derive a consequence of Theorem 11. Lemma 12 Let A be a subset of an abelian group such that |A + A| K|A|. Then


O(K log8 K)

3ek K

|A|,

|kA|

![image 16](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile16.png>)

for every k K.

Proo f. By Theorem 11 there exists a proper generalized arithmetic progression P of dimension d ≪ log7 K and size at least |A|/KO(log7 K) such that P ⊆ 2A − 2A. Thus, applying Plu¨nnecke– Ruzsa inequality (13), we have

|A + P| |3A − 2A| K5|A| KO(log7 K)|P|. By Lemma 5, we obtain

A ⊆ P − P + (S1 − S1) + ··· + (Sl − Sl) with l ≪ (log 2K)8. Therefore,

2l

2K + k − 1 k

|kP − kP| 2K + k − 1 k

|kA| |kP − kP + (kS1 − kS1) + ··· + (kSl − kSl)|

2l

O(K log8 K)

3ek K

3ek 2K − 1

4lK

(2k)d|P|

(2k)d|P|

|A|, provided that k K. ✷ Our ﬁrst result reﬁnes Sanders’ Theorem 1, provided that K is not too large.

![image 17](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile17.png>)

![image 18](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile18.png>)

- Theorem 13 Let A ⊆ G be a ﬁnite set and suppose that |A + A| K|A|. Then, we have dim(A) ≪ K log |A|


and

dim(A) ≪ log |A| + K(log K)8 log log |A|. (17)

Proo f. Let Λ ⊆ A be a dissociated set such that |Λ| = dim(A). Then by Lemma 3 (or simple counting arguments) and Lemma 6 we have for some absolute constant C > 0

|Λ|k

(Ck)k |kΛ| |kA| Kk|A|. Taking k ∼ log |A| we obtain the ﬁrst assertion.

![image 19](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile19.png>)

Similarly, by Lemma 12 we have

|Λ|k (Ck)k

![image 20](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile20.png>)

3ek K

![image 21](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile21.png>)

O(K log8 K)

|A|,

for k K. Thus, putting

k ∼ log |A| + K(log K)8 log log |A| , we get

|Λ| ≪ log |A| + K(log K)8 log log |A| as required. ✷

In the above proof the hardest case is when the size of kA attains its maximal value Kk|A|. However, we show that if it is the case then one can ﬁnd a huge subset of A with very small additive dimension.

- Theorem 14 Let A ⊆ G be a set and K 1, ε > 0 be real numbers. Suppose that |A + A| K|A| and |kA| Kk−ε|A| for some k 3. Then there exists a set A′ ⊆ A of size at least |A|/2 such that dim(A′) ≪ 2kKε log |kA|.

Proo f. From Lemma 6 it follows that there exists a set X, |X| |A|/2 such that |X + kA| (2K)k|A|. Therefore

|X + kA| 2kKε|kA|. (18) By Sanders’ Theorem 1, we have dim(X) ≪ 2kKε log |kA|. This completes the proof. ✷ Recall the main result of [21] (see Lemma 3).

- Theorem 15 Let A be a ﬁnite set of an abelian group such that |A+A| K|A|. Then for every k ∈ N there exist sets X ⊆ A and Y ⊆ A + A such that |X| (2K)−2k+1|A|, |Y | |A| and E(X,Y ) K−2/k|X|2|Y |. Combining Theorem 15 with Theorem 2, we obtain the following consequence.


Corollary 16 Let A be a ﬁnite set of an abelian group such that |A+A| K|A|. Then for every k ∈ N there exists set X ⊆ A such that |X| ≫ (2K)−2k+1|A|/K1/2 and dim(X) ≪ K2/k log |A|.

Using a well-known Croot-Sisask Lemma Sanders proved the following result (Proposition 3.1 in [18]).

Theorem 17 Let A be a ﬁnite subset of an abelian group with |A + A| K|A|. Then for every k ∈ N there exists a set X ⊆ A − t for some t, of size at least e−O(k2 log2 2K)|A + A| such that kX ⊆ 2A − 2A.

Applying Theorem 17 we show that every set with small sumset contains relatively large subset with very small additive dimension. Corollary 18 Let A be a ﬁnite subset of an abelian group with |A+A| K|A|. Then for every k ∈ N there exists a set X ⊆ A of size at least e−O(k2 log2 2K)|A + A| such that

dim(X) ≪ K4/k log |A|.

Proo f. Observe that we can assume that k log |A|, because otherwise our theorem is trivial. Let X be the set given by Theorem 17. By Plu¨nnecke-Ruzsa inequality we have

|klX| |2lA − 2lA| K4l|A|.

Now, we argue as in Theorem 13. Let Λ ⊆ X be a dissociated set with |Λ| = dim(X). By Rudin’s inequality, we have for some absolute constant C1 > 0

|Λ|kl

(C1kl)kl |klΛ| |klX| K4l|A|. Putting l = [logk|A|] we see that

![image 22](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile22.png>)

![image 23](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile23.png>)

dim(X) ≪ K4/k log |A|, which completes the proof. ✷

# 5 Additive dimension of sets with large additive energy

The aim of this section is to reﬁne Theorem 2, in the sense, that under the same assumption E(A) = |A|3/K, we ﬁnd a possibly large subset of A having additive dimension O(K1−γ log |A|), where γ > 0 is an absolute constant.

Our ﬁrst result reﬁnes Theorem 2.

- Theorem 19 Let A,B be subsets of ﬁnite abelian group, and let ε > 0. Suppose that E(A,B) = |A||B|2/K, then there exist a set B∗ ⊆ B such that


2

|B∗| |B|

dim(B∗) ≪ε K(log K)2+ε log |A| ·

, (19) and

![image 24](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile24.png>)

E(A,B∗) 2−2E(A,B). (20)

Proo f. We establish Theorem 19 using the following algorithm.

At zero step we put B0 := B, ε0(x) = 0 and β0 = 1. At step j 1 we apply Lemma 4 to the set Bj−1 with parameters p = 2 + log |A| and

lj = η−1K(log K)βj2−1j1+ε log |A|,

where η−1 = 24 j 1 1/j1+ε. Lemma 4 gives us a new set Bj ⊆ Bj−1, where Bj = Bstr, in other words Bj−1 \Bj is a disjoint union of all dissociated subsets each of size lj. After that put εj(x) = Bj−1(x)−Bj(x), βj = |Bj|/|B| and iterate the procedure. The described algorithm will satisfy the following property

E(A,Bj) 2−2E(A,B). (21)

Obviously, at the ﬁrst step inequality (21) is satisﬁed. If at some step j we get βj 2 1βj−1 then our algorithm terminates with the output B∗ = Bj. In view of inequality (21) it is clear the total number of steps k does not exceed log K. Further, if our iteration procedure terminates with the output B∗, then E(A,B∗) 2−2E(A,B) and

![image 25](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile25.png>)

dim(B∗) = dim(Bj) lj = η−1K(log K)βj2−1j1+ε log |A|

2η−1K(log K)2+εβj2 log |A| ≪ε K(log K)2+ε log |A| ·

2

|B∗| |B|

.

![image 26](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile26.png>)

Thus, the constructed set B∗ satisﬁes (19), (20).

It remains to check (21), and clearly, it is suﬃcient to do it for the ﬁnal step k. We have N · E(A,B) =

| A(ξ)|2| B(ξ)|2 =

| A(ξ)|2| Bk(ξ)|2 +

ξ

ξ

k

k

k

![image 27](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile27.png>)

| A(ξ)|2| εj(ξ)|2

| A(ξ)|2 Bj(ξ) εj(ξ) +

| A(ξ)|2 Bj(ξ) εj(ξ) +

![image 28](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile28.png>)

+

j=1 ξ

j=1 ξ

j=1 ξ

= σ0 + σ1 + σ2 . (22)

k

σ2

- j=1 ξ

| εj(ξ)|2p

1/p

·

ξ

| A(ξ)|

2p p−1

![image 29](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile29.png>)

1−1/p

- k


k

p lj ≪ η(log K)−1K−1|A||B|2N

j−1−ε

|A|1+1/p|Bj−1|2N

![image 30](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile30.png>)

j=1

j=1

2−4k−1K−1|A||B|2N .

Next, we estimate σ1 in a similar way. Let us consider only the ﬁrst term in σ1, the second one can be bounded in the same manner. By the Cauchy–Schwarz inequality, we get

N−1

k

j=1 ξ

![image 31](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile31.png>)

| A(ξ)|2 Bj(ξ) εj(ξ)

k

E1/2(A,Bj)E1/2(A,εj)

j=1

k

- j=1

E(A,Bj)

1/2

·

k

j=1

E(A,εj)

1/2

- k1/2E1/2(A,B)σ21/2 2−2E(A,B).


So, by (22), we obtain E(A,Bk) 2−2K−1|A||B|2. This completes the proof. ✷

- Theorem 20 Let A be a ﬁnite subset of an abelian group. Suppose that E(A) = |A|3/K, then there exists a set B ⊆ A such that |B| ≫ |A|/K25/8 and dim(B) ≪ K7/8 log |A|.


Proo f. Let E4(A) = M|A|5/K3 and P := {x : (A ◦ A)(x) |A|/2K}. By Theorem 8, |P| ≫ K|A|/M and E(P) ≫ |P|3/M7/2. By Theorem 2 there exists P′ ⊆ P of size ≫ |P|/M7/6 such that dim(P′) ≪ M7/2 log |P|. We have

|A|2 M13/6

(P′ ◦ A)(x) |A| 2K |P′| ≫

|P| M7/6 ≫

|A| K

.

![image 32](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile32.png>)

![image 33](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile33.png>)

![image 34](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile34.png>)

![image 35](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile35.png>)

x∈A

Therefore, (P′ ◦ A)(x) ≫ |A|/M13/6 for some x. Putting B = A ∩ (P′ + x) we see that

|B| ≫ |A|/M13/6 (23) and

dim(B) ≪ M7/2 log(K|A|) ≪ M7/2 log |A|. (24) On the other hand, by Lemma 7

κ4|A|5 =

M|A|5 K3

E(A,As)

= E4(A) =

E(A,As) 2

![image 36](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile36.png>)

|As| 2 1κ4|A|

s =2

![image 37](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile37.png>)

E(A,As) |As|2

E(A,As) |As|2

· |As|2 max

· E3(A)

2 max

![image 38](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile38.png>)

![image 39](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile39.png>)

|As| 2 1κ4|A|

|As| 2 1κ4|A|

![image 40](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile40.png>)

![image 41](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile41.png>)

and similarly

κ3|A|4 = E3(A) =

E(A,At) |At|2

· E(A).

E(A,At) 2 max

![image 42](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile42.png>)

|At| 2 1κ3|A|

![image 43](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile43.png>)

t =1

so there exist |As| 2 1κ4|A| and |At| 12κ3|A| such that E(A,As) ≫ κ4κ−3 1|A||As|2 and E(A,At) ≫ κ3K|A||At|2. But κ4κ−3 1κ3K = M/K2, so either κ4κ−3 1 M1/2/K or κ3K M1/2/K. Hence by Theorem 2 there is a set B ⊆ A such that

![image 44](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile44.png>)

![image 45](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile45.png>)

|B| |A|

≫ min{κ4(κ4κ−3 1)1/2,κ3(κ3K)1/2} min{M3/2K−7/2,M3/2K−5/2} = M3/2K−7/2 , (25) and

![image 46](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile46.png>)

K M1/2

dim(B) ≪

log |A|. (26) Combining (24), (26) and (23), (25), we obtain the required result. ✷

![image 47](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile47.png>)

Clearly, using Theorem 19 instead of Theorem 2 in the proof one can estimate the dimension of the set B in terms of the size of B.

To prove the next result we need a generalization of Theorem 2 for the energies Tk(A). Proposition 21 Let A ⊆ G be a ﬁnite set, k 2 be a positive integer and suppose that

- Tk(A) = c|A|2k−1. Then there is a set A∗ ⊆ A such that Tk(A,... ,A,A∗,A∗) 2−5Tk(A) (27)


and

Tk−1(A)|A|2 Tk(A)

log(c−1|A|) c−1/(k−1) log(c−1|A|). (28)

dim(A∗) ≪

![image 48](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile48.png>)

In particular |A∗| ≫ c1/(2k−1)|A|. Proo f. For any l k let Tl(A) = cl|A|2l−1, hence ck = c. By Fourier transform, we have

1 N ξ | A(ξ)|2k.

Tk(A) =

![image 49](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile49.png>)

We apply Lemma 4 to the set A with parameters p = 2+log(c−1|A|) and l = η−1c−1ck−1 log(c−1|A|), where η > 0 is an appropriate constant to be speciﬁed later. Write ε(x) = A(x) − A∗(x), where A∗ = Astr, in other words A \ A∗ is a disjoint union of all dissociated subsets each of size l. We have

| A(ξ)|2k−2| A(ξ)|2 =

| A(ξ)|2k−2| A∗(ξ)|2 +

N · Tk(A) =

ξ

ξ

![image 50](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile50.png>)

| A(ξ)|2k−2 A∗(ξ) ε(ξ) +

| A(ξ)|2k−2 A∗(ξ) ε(ξ) +

![image 51](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile51.png>)

+

ξ

ξ

= σ0 + σ1 + σ2 .

ξ

| A(ξ)|2k−2| ε(ξ)|2

1/p

1−1/p

(2k−2)p p−1

| ε(ξ)|2p

·

| A(ξ)|

σ2

![image 52](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile52.png>)

ξ

ξ

1/p

p l |A|2 · Tk−1(A) |A|2k−2

≪

N (29) 2−1ck|A|2k−1N . (30)

![image 53](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile53.png>)

![image 54](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile54.png>)

Tk−1(A)

To obtain the last inequality, we have used a simple bound Tk−1(A) c|A|2k−3. Hence either σ0 or σ1 is at least 2−2ck|A|2k−1N. In the ﬁrst case we are done. In the second case an application of the Cauchy–Schwarz inequality yields

2−6N2T2k(A) N · Tk(A,... ,A,A∗,A∗) · σ2 . Combining the inequality above with (29), we get

Tk(A,... ,A,A∗,A∗) 2−5Tk(A).

Using the last estimate and the H¨older inequality, we see that |A∗| ≫ c1/(2k−1)|A|. Furthermore, we have dim(A∗) l = η−1c−1ck−1 log(c−1|A|), which proves the ﬁrst inequality in (27). Applying the H¨older inequality again, we see that ck−1 c

k−2

k−1, which gives the second inequality in

![image 55](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile55.png>)

- (27). This completes the proof of Proposition 21. ✷

Remark 22 One can also obtain an asymmetric version of the result above as well as a variant of Theorem 19 for the energies Tk.

Let us also remark that the bound on the size of A∗ in Proposition 21 is sharp up to

a constant factor (see example at the end of section 2 from [26]). Indeed, let G = Fn2, and A = H ∪ Λ, where H is a subspace, |H| ∼ c1/(2k−1)|A|, Λ is a dissociated set (basis) and c is an

appropriate parameter. Then Tk(A) Tk(H) = |H|2k−1 ≫ c|A|2k−1, any set A∗ ⊆ A satisfying

- (28) has large intersection with H, hence it cannot have size much greater then c1/(2k−1)|A|.


If one replace the condition of Theorem 20 on E(A) by a similar one on E3/2(A), then the the following result can be proved.

- Theorem 23 Let A be a ﬁnite subset of an abelian group and suppose that E3/2(A) = |A|5/2/K1/2. Then there exists a set B ⊆ A such that


|B| ≫ |A|/K2 (31) and

dim(B) ≪ K3/4 log |A|. (32)

Proo f. Write T4(A) = M|A|7/K3, M 1, then by Theorem 10, we have

|A|5 MK

E4(A) := κ4|A|5 ≫

,

![image 56](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile56.png>)

Furthermore,

hence by Lemma 7

E(As,At)

|As| 4 1κ4|A|

![image 57](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile57.png>)

|As|2|At|

|As| 4 1κ4|A|

![image 58](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile58.png>)

1 4

E4(A)

![image 59](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile59.png>)

- 1

![image 60](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile60.png>)

- 2


E4(A)

E(As,At) |As|3/2|At|3/2

·

E(As,At) max

![image 61](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile61.png>)

|As|, |At| 4 1κ4|A|

![image 62](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile62.png>)

|As|, |At| 4 1κ4|A|

![image 63](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile63.png>)

|As|3/2|At|3/2 .

s,t

Therefore, there are |As|,|At| ≫ 14κ4|A| such that

![image 64](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile64.png>)

E4(A) E3/2(A)2

E(As,At) ≫ |As|3/2|At|3/2 ·

![image 65](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile65.png>)

|As|3/2|At|3/2 M

![image 66](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile66.png>)

and by the Cauchy–Schwarz inequality we see that either E(As) ≫ |As|3/M, or E(At) ≫ |At|3/M. Applying Theorem 2 in the symmetric case we ﬁnd B ⊆ A such that

|A| M4/3K

κ4|A| M1/3 ≫

|B| ≫

, (33)

![image 67](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile67.png>)

![image 68](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile68.png>)

and

dim(B) ≪ M log |A|. (34)

On the other hand, using Proposition 21, we get a set B′ ⊆ A such that |B′| ≫ M1/7K−3/7|A| and

dim(B′) ≪ KM−1/3 log |A|. Combining the last inequalities with (33), (34), we obtain the required result. ✷

Again, using Theorem 19 instead of Theorem 2 in the proof one can estimate the dimension of the set B in terms of the size of B.

The last result of this section shows that small E3(A) energy implies that a large subset of A has small dimension.

- Theorem 24 Let A be a ﬁnite subset of an abelian group. Suppose that |A − A| K|A| and E3(A) = M|A|4/K2. Then there exists A∗ ⊆ A such that |A∗| ≫ |A|/M1/2 and


dim(A∗) ≪ M(log |A| + log K log M). Proo f. By Theorem 9 for every l 2 we have Tl(A) |A|2l−1/(K(8M)l). Applying Proposition

- 21 with l ∼ log K we obtain the result. ✷


# 6 An application

Konyagin posed the following interesting problem. Is it true that there is a constant c > 0 such that if A ⊆ Fp and |A|

√p then there exists x such that 0 < (A ∗ A)(x) ≪ |A|1−c. First nontrivial results toward this conjecture were obtained in [11]. It was proved that there exists

![image 69](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile69.png>)

- x such that 0 < (A ∗ A)(x) ≪ e−O((log log|A|)2)|A|, provided that |A| eclog1/5 p. Our next result improves the above estimate as well as the condition on size of A.


√logp. Then there exists x such that

![image 70](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile70.png>)

- Theorem 25 Suppose that A ⊆ Fp and |A| ec


0 < (A ∗ A)(x) ≪ e−O(log1/4 |A|)|A| for some absolute constant c > 0.

Proo f. Let us write |A|/K = minx∈A+A(A∗A)(x), then clearly |A+A| K|A|. Let X ⊆ A be a set given by Corollary 18 for k = [log K]. Then |X| ≫ e−O(log4 K)|A| and dim(X) ≪ log |A|. Suppose that Λ satisﬁes |Λ| = dim(X) and X ⊆ Span(Λ). By Dirichlet approximation theorem there exists r ∈ F∗p such that

rt/p p−1/|Λ|. for every t ∈ Λ and therefore

1 K|A|

rx/p |Λ|p−1/|Λ| ≪ (log |A|)p−O(1/log|A|) <

![image 71](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile71.png>)

for every x ∈ X. We can assume that there is a set X′ ⊆ X ⊆ A of size at least |X|/2 such that for each x ∈ X′ we have {rx/p} < 1/(K|A|).

Notice that for every r ∈ F∗p there is a large gap in the set r · (A + A) i.e. there exists s ∈ A + A such that

{rs + 1,... ,rs + l} ∩ r · (A + A) = ∅,

where l = p−||AA++AA| | ≫ Kp|A|. Since (A ∗ A)(s) |A|/K it follows that there are at least |A|/K elements a ∈ A such that

![image 72](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile72.png>)

![image 73](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile73.png>)

{ra + 1,... ,ra + l} ∩ (r · A) = ∅. Denote the set of such a’s by Y ⊆ A. Thus,

K|A| |A + A| = |r · A + r · A| |X′ + Y | = |X′||Y | e−O(log4 2K)|A|2, so that K ≫ eO(log1/4 |A|), and the assertion follows. ✷

Bukh proved [6] that if A ⊆ G and λi ∈ Z \ {0} then |λ1 · A + ··· + λk · A| KO( i log(1+|λi|))|A|,

where K = |A ± A|/|A|. We also prove here an estimate for sums of dilates. It is not directly related with the additive dimension of sets but it is another consequence of Theorem 11.

- Theorem 26 Let A ⊆ G is a ﬁnite set and λi ∈ Z \ {0}. Suppose that |A + A| K|A| then |λ1 · A + ··· + λk · A| eO((log8 K)(k+log( i |λi|))|A|.


Proo f. From Sanders’ Theorem 11 it follows that there is a O(log7 K)−dimensional arithmetic progression P of size |P| ≫ |A|/KO(log7 K) contained in 2A − 2A. By the well-known Ruzsa covering lemma there is a set S with |S| ≪ KO(log7 K) such that

A ⊆ S + P − P. Therefore,

|λ1 · A + ··· + λk · A| KO(klog7 K)|λ1 · (P − P) + ··· + λk · (P − P)| KO(klog7 K)|(

λi)(P − P) + (

λi)(P − P)|

λi>0

λi<0

KO(klog7 K)(|λ1| + ··· + |λk|)log7 K|P − P| eO((log8 K)(k+log( i |λi|))|A|,

which completes the proof. ✷

# 7 A result of Bateman and Katz

In this section we reformulate some results from [1, 2] in terms of additive dimension. Although in [1, 2] the authors have deal with the case G = Fnp, where p is a prime number, it is easy to see that their arguments work in more general groups. We will follow their argument with some modiﬁcations.

Let A ⊆ G and s be a positive integer. A 2s–tuple (x1,... ,x2s) ∈ A2s is called the additive 2s–tuple if x1 + ··· + xs = xs+1 + ··· + x2s. We say that an additive 2s–tuple (x1,... ,x2s) is trivial if at least two variables are equal. Otherwise we say that 2s–tuples is nontrivial. Let

T∗s(A) denotes the number of nontrivial 2s–tuples. We will often use the following inequality

- Tl(A)s−1 Ts(A)l−1|A|s−l, which holds for every s l 2.


- Lemma 27 Let A ⊆ G and s 4. Suppose that Ts(A) ≫ 10ss2s|A|s. Then T∗s(A) 2 1Ts(A).


![image 74](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile74.png>)

Proo f. We proceed similarly like in the proof of Theorem 5.1 in [13]. Let (A˜∗sA)(x) denotes the number of representations x = x1 +··· +xs in distinct xi ∈ A. Observe that x(A˜∗sA)(x)2 equals T∗s(A) plus the number of additive tuples (x1,... ,x2s) such that for some i s and j > s we have xi = xj. Hence,

x

(A˜∗sA)(x)2 − T∗

s(A) s2|A|

x

(A˜∗s−1A)(x)2 s2|A|Ts−1(A). (35)

Notice that (A∗sA)(x)−(A˜∗sA)(x) is the number of representations x = x1+···+xs, for which

- xi = xj for some i < j. Thus, we have (A ∗s A)(x) − (A˜∗sA)(x) s2q(x), (36)


where q(x) is the number of solutions of x = 2x1 + ··· + xs−1. By Fourier inversion

x

s−3 s−1

2

q(x)2 = | A(2α)|2| A(α)|2s−4 dα |A|2Ts−2(A) |A|2+

s−1Ts(A)

![image 75](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile75.png>)

![image 76](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile76.png>)

2

2

= |A|2+

s−1Ts(A)−

s−1Ts(A)

![image 77](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile77.png>)

![image 78](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile78.png>)

1 100

s−4Ts(A). (37)

![image 79](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile79.png>)

Therefore, by the triangle inequality and inequalities (36), (37), we get

(A˜∗sA)(x)2 Ts(A)1/2 Ts(A)1/2 − 2s2(

q(x)2)1/2

x

x

1 5

Ts(A)1/2 Ts(A). (38) Finally, using the assumption that Ts(A) ≫ 10ss2s|A|s, and bounds (35), (38), we obtain T∗ s(A)

Ts(A)1/2 Ts(A)1/2 −

![image 80](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile80.png>)

- 4

![image 81](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile81.png>)

- 5


- 4

![image 82](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile82.png>)

- 5


- 4

![image 83](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile83.png>)

- 5


- 1

![image 84](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile84.png>)

- 2


s−2 s−1

s

Ts(A) − s2|A|Ts−1(A)

Ts(A) − s2|A|

Ts(A)

s−1Ts(A)

![image 85](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile85.png>)

![image 86](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile86.png>)

and the assertion follows. ✷

We will also use the following simple lemmas.

- Lemma 28 Let A ⊆ G be a ﬁnite set and let s > 0 be an even integer. Suppose that A contains a family of nontrivial s–tuples, involving at least rs elements of A. Then dim(A) |A| − r.

Proo f. Let S denotes the given family of s–tuples and let M ⊆ A be the set of all elements of A involved in some s–tuple of S. To proof the lemma it is suﬃcient to show that there are s–tuples S1,... ,Sr ∈ S and elements aj ∈ Sj, j ∈ [r] such that each aj does not belong to Si, i = j. Indeed, it is easy to see that A ⊆ Span(A \ {a1,... ,ar}).

We use induction on r 0. The result is trivial for r = 0. Now assume that r 1. In view of the assumption |M| rs there is an element a ∈ M belonging at most k := s|S|/|M| |S|/r tuples from S. Let S1,... ,Sk be all these tuples and put S′ = S \{S1,... ,Sk}. One can suppose that the minimum of such k is attained on the element a ∈ M. Notice that S′ involves at least rs − s elements of A. Indeed, otherwise |S1 ∪ ··· ∪ Sk| s + 1 and each element of S1 ∪ ··· ∪ Sk belongs to at least k sets from S, so that it belongs to all sets S1,... ,Sk. But this implies that |S1∪···∪Sk| ks/k = s, which gives a contradiction. By induction assumption there are tuples S1′,... ,Sr′ ∈ S′ and elements a′j ∈ Sj′, j r − 1 such that each a′j does not belong to Si′, i = j. Hence the sets S1,S1′,... ,Sr′ ∈ S and the elements a1,a′1,... ,a′r−1 posses the required property. ✷

- Lemma 29 Let M ⊆ G be a ﬁnite set and suppose that M = X ∪ D, where D is a dissociated set. Then there is an absolute constant C > 0 such that Ts(M) Csss|D|s + 22s|X|2s−1.


Proo f. By Rudin’s inequality we have

Ts(M) = | M(α)|2s dα 22s | D(α)|2s dα + 22s | X(α)|2s dα Csss|D|s + 22s|X|2s−1. ✷

Proposition 30 Let A ⊆ G be a ﬁnite set such that Tk(A) 10ks2k|A|k, where 2 k < s = ⌊log |A|⌋. Furthermore, let σ 1 and d be such that

s−k

|A|1−

2s(k−1) log3/2 |A| Tk(A)

≪ d |A|1/2 σ1/2

![image 87](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile87.png>)

. (39)

![image 88](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile88.png>)

![image 89](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile89.png>)

s−1 2s(k−1)

![image 90](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile90.png>)

Then there is a set A′ ⊆ A such that dim(A′) d and |A′| σdim(A′). (40)

Proo f. Suppose that for all sets A′ ⊆ A such that dimA′ = m d we have |A′| < mσ. We choose d elements from A uniformly and random. We show that

P dim({x1,... ,xd}) d − l = O(l)−l . (41) Indeed, suppose that we have chosen x1,... ,xm for some m d. Put

A′ := Span(W) ∩ A,

where W is a maximal dissociated subset of {x1,... ,xm}. Clearly, |W| m and hence dim(A′) m. By our assumption d |A|

1/2

σ1/2 and therefore the probability that xm+1 belongs to A′ is at most |A′|/|A| mσ/|A| dσ/|A| 1/d. Observe that if dim({x1,... ,xd}) d − l then there are at least l elements xi+1 such that xi+1 ∈ Span(Wi) ∩ A, where Wi is a maximal dissociated subset of {x1,... ,xi}. Thus, the required probability is bounded from above by

![image 91](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile91.png>)

∞

d

j 1 dj

ed j

d j

1 dj

= O(l)−l

![image 92](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile92.png>)

![image 93](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile93.png>)

![image 94](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile94.png>)

j=l

j=l

and (41) is proved.

Next, suppose that the tuple (x1,... ,xd) ∈ Ad has dimension d − l. Let M be the set that consists of all elements of {x1,... ,xd}, which are involved in some nontrivial 2s−tuple. Then by Lemma 28, |M| 2sl. Since M contains |M|−l element dissociated subset it follows by Lemma

- 29 that T∗s(M) Ts(M) Csss(2sl)s + 22sl2s−1. Therefore, the expected number of nontrivial 2s−tuples in (x1,... ,xd) is bounded from above by


d

C1s

(s2sls + l2s−1)O(l)−l C2ss3s , (42)

l=0

where C1,C2 > 0 are absolute constants.

On the other hand the expected number of nontrivial 2s−tuples in (x1,... ,xd) equals T∗s(A)(d/|A|)2s and by Lemma 27 we have

s−1 k−1

2s 1 2

2s Tk(A)

2s

d |A|

d |A|

d |A|

![image 95](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile95.png>)

T∗

s(A)

Ts(A)

.

![image 96](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile96.png>)

![image 97](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile97.png>)

![image 98](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile98.png>)

![image 99](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile99.png>)

![image 100](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile100.png>)

s−k k−1

2|A|

![image 101](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile101.png>)

Comparing the last estimate with (42) (recalling that s = ⌊log |A|⌋), we obtain a contradiction. This completes the proof. ✷

Finally let us formulate the Bateman–Katz thorem for general abelian group G.

Corollary 31 Let A ⊆ G be a ﬁnite set and let k be a ﬁxed integer, 2 k < ⌊log |A|⌋. Suppose that Tk(A) = c|A|2k−1 10k|A|k log2k |A|. Then there is a set A′ ⊆ A such that

1 k−1

|A| log3 |A|

c

![image 102](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile102.png>)

1 k−1

|A′| ≫

· log(c

|A|), (43)

![image 103](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile103.png>)

![image 104](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile104.png>)

and

- 1

![image 105](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile105.png>)

- 2(k−1) · log3/2 |A|. (44)


dim(A′) ≪k c−

Proo f. As in Proposition 30 put s = ⌊log |A|⌋. In view of k < s, we have Ts(A) ≫ 10ss2s|A|s and Ts(A) c

s−1 k−1

|A|2s−1. We apply Proposition 30 with d ∼ |A|T−1/2s

![image 106](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile106.png>)

s (A)log3/2 |A| ≪ c−1/2(k−1) log3/2 |A| and σ ∼ |A|d−2 .

Then the conditions (39) are satisﬁed. Thus, there exists a set A′ ⊆ A of dimension at most d such that

1 k−1

|A| log3 |A|

c

![image 107](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile107.png>)

1 k−1

|A′| σdim(A′) ≫ σ log σ ≫

· log(c

|A|). This completes the proof. ✷

![image 108](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile108.png>)

![image 109](<2014-schoen-additive-dimension-theorem-sanders_images/imageFile109.png>)

# 8 Further remarks

We ﬁnish the paper with some remarks on other possible variants of additive dimension, which we considered here. For any A ⊆ G put

d(A) = min{|S| : S ⊆ A, A ⊆ SpanS}, d∗(A) = min{|S| : A ⊆ SpanS}, where for S = {s1,... ,sl} we deﬁne

l

εjsj : εj ∈ {0,−1,1} .

Span (S) :=

j=1

Example 32 Let x = y be integers and let A1 = {x,y,x + y,2x + y}, A2 = {y,x + y,2x + y}. Clearly, A2 A1 and dim(A1) = 3, d(A) = d∗(A1) = 2, dim(A2) = d(A2) = 3, d∗(A2) = 2, Thus every kind of dimension can diﬀer from another one. Note also that d(A2) > d(A1), but A2 A1.

Observe that

d∗(A) d(A) d ˜(A) dim(A). On the other hand

dim(A) ≪ d∗(A)log d∗(A) d(A)log d(A) (see [10]). Indeed, let Λ ⊆ A be a maximal dissociated subset of A, |Λ| = dim(A) and let |S| = d∗(A). There are 2|Λ| diﬀerent subset sums of Λ and any element of A and hence any element of Λ belongs to SpanS, so that

2|Λ| (2|Λ| + 1)|S| and the result follows.

Each of the dimensions has useful properties: dim(A), d∗(A) are monotone (but d(A) is not as Example 32 shows), furthermore all dimensions are subadditive

dim(C1 ∪ ··· ∪ Cn)

n

dim(Cj)

j=1

and the same holds for d∗(A), d(A) and the dimension d(A) is ”subadditive” in the following sense

n

d(C1 + ··· + Cn)

d(Cj)

j=1

for any disjoint sets Cj. There are another dimensions, e.g. d˜(A) = min{|Λ| : Λ ⊆ A, Λ is maximal (by inclusion) dissociated subset of A}, Clearly, d(A) d ˜(A) dim(A) and d˜ is monotone because of 3 = d˜(A2) > d˜(A1) = 2.

# References

- [1] M. Bateman, N. Katz, New bounds on cap sets, Journal of AMS 25:2 (2012), 585–613.
- [2] M. Bateman, N. Katz, Structure in additively nonsmoothing sets, arXiv:1104.2862v1 [math.CO] 14 Apr 2011.
- [3] J. Bourgain, On triples in arithmetic progression, Geom. Funct. Anal. 9 (1999), 968–984.
- [4] J. Bourgain, Roth’s Theorem on Progressions Revisited, J. Anal. Math., 104 (2008), 155–206.


- [5] J. Bourgain, On Aritmetic Progressions in Sums of Sets of Integers, A Tribute of Paul Erd¨os, 105–109, Cambridge University Press, Cambridge, 1990.
- [6] B. Bukh, Sums of dilates, Combin. Probab. Comput., 17:5 (2008), 627–639.
- [7] M.–C. Chang, A polynomial bound in Freiman’s theorem, Duke Math. J. 113:3 (2002), 399–419.
- [8] B. Green, T. Tao, Freimans theorem in ﬁnite ﬁelds via extremal set theory, Combinatorics, Probability and Computing 18 (2009), 335–355.
- [9] B. Green, T. Tao, An equavalence between inverse sumset theorems and inverse conjectures for the U3–norms, Mathematical Proceedings of the Cambridge Philosophical Society 149:1 (2010).
- [10] V.F. Lev, R. Yuster, On the size of dissociated bases, The Electronic Journal of Combinatorics 18 (1) (2011), #P117.
- [11] T.  Luczak, T. Schoen, On a problem of Konyagin, vol. 134 (2008), 101–109.
- [12] W. Rudin, Fourier analysis on groups, Wiley 1990 (reprint of the 1962 original).
- [13] I.Z. Ruzsa, Solving linear equations in sets of integers. I, Acta Arith., 65 (1993), 259–282.
- [14] I.Z. Ruzsa, Sumsets and structure, book.
- [15] I.Z. Ruzsa, Cardinality questions about sumsets, Additive combinatorics, ser. CRM Proc. Lecture Notes. Providence, RI: Amer. Math. Soc 43 (2007), 195–205.
- [16] T. Sanders, On a theorem of Shkredov, Online J. Anal. Comb. No. 5 (2010), Art. 5, 4 pp.
- [17] T. Sanders, Structure in sets with logarithmic doubling, Canad. Math. Bull., to appear..
- [18] T. Sanders, On the Bogolubov–Ruzsa Lemma, Anal. PDE 5 (2012), 627–655.
- [19] T. Sanders, On certain other sets of integers, J. Anal. Math. 116 (2012), 53-82.
- [20] T. Sanders, On Roth’s Theorem on Progressions, Ann. of Math. (2) 174 (2011), 619-636.
- [21] T. Schoen, Near optimal bounds in Freiman’s theorem, Duke Math. J. 158 (2011), 1–12.
- [22] T. Schoen I. D. Shkredov, Higher moments of convolutions, J. of Number Theory, 133

(2013), 1693–1737.

- [23] I. D. Shkredov, On Sets with Small Doubling, Mat. Zametki, 84:6 (2008), 927–947.
- [24] I. D. Shkredov, Some new results on higher energies, Transactions of MMS, 74:1 (2013), 35–73.
- [25] I. D. Shkredov, I. V. V’ugin, On additive shifts of multiplicative subgroups, Mat. Sbornik, 203:6 (2012), 81–100.


- [26] I. D. Shkredov, S. Yekhanin, Sets with large additive energy and symmetric sets, Journal of Combinatorial Theory, Series A 118 (2011) 1086–1093.
- [27] T. Tao, V. Vu, Additive combinatorics, Cambridge University Press 2006.


Faculty of Mathematics and Computer Science, Adam Mickiewicz University, Umultowska 87, 61-614 Poznan´, Poland schoen@amu.edu.pl

Division of Algebra and Number Theory, Steklov Mathematical Institute, ul. Gubkina, 8, Moscow, Russia, 119991 and Delone Laboratory of Discrete and Computational Geometry, Yaroslavl State University, Sovetskaya str. 14, Yaroslavl, Russia, 150000 and IITP RAS, Bolshoy Karetny per. 19, Moscow, Russia, 127994 ilya.shkredov@gmail.com

