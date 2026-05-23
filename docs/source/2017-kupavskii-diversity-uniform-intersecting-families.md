---
type: source
kind: paper
title: Diversity of uniform intersecting families
authors: A. Kupavskii
year: 2017
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1709.02829
source_local: ../raw/2017-kupavskii-diversity-uniform-intersecting-families.pdf
topic: general-knowledge
cites:
---

arXiv:1709.02829v2[math.CO]29Jun2018

# Diversity of uniform intersecting families

Andrey Kupavskii∗

Abstract

A family F ⊂ 2[n] is called intersecting, if any two of its sets intersect. Given an intersecting family, its diversity is the number of sets not passing through the most popular element of the ground set. Peter Frankl made the following conjecture: for n > 3k > 0 any intersecting family F ⊂ [nk] has diversity at most nk−−23 . This is tight for the following “two out of three” family: {F ∈ [nk] : |F ∩ [3]| ≥ 2}. In this note we prove this conjecture for n ≥ ck, where c is a constant independent of n and k. In the last section, we discuss the case 2k < n < 3k and show that one natural generalization of Frankl’s conjecture does not hold.

## 1 Introduction

We denote [n] := {1, . . ., n}, 2[n] := {S : S ⊂ [n]} and [nk] := {S : S ⊂ [n], |S| = k}. Any subset of 2[n] we call a family. A family F ⊂ 2[n] is called intersecting, if any two of its

sets intersect. The degree δi of an element i ∈ [n] is the number of sets from F containing

- i. We denote by ∆(F) the largest degree of an element: the maximum of δi over i ∈ [n]. The diversity γ(F) of F is the number of sets, not containing the element of the largest degree: γ(F) := |F| − ∆(F).


The study of intersecting families started from the famous Erd˝os-Ko-Rado theorem [6], and since then a lot of eﬀort was put into understanding the structure of large intersecting families. The EKR theorem states that the largest uniform intersecting family consists of all sets containing a given element, that is, the maximal family of diversity 0. The Hilton-Milner theorem [10] gives the largest size of the family with diversity at least 1. Frankl’s theorem [7], especially in its strengthened version due to Kupavskii and Zakharov

- [18] bounds the size of the families with diversity at least nn−−uk−−11 , where 3 ≤ u ≤ k is a ﬁxed real number. We also refer to [17], where, among other results, a conclusive version of this theorem was obtained.


- Theorem 1 ([18]). Let n > 2k > 0 and F ⊂ [nk] be an intersecting family. Then, if γ(F) ≥ nn−−uk−−11 for some real 3 ≤ u ≤ k, then


n − u − 1 k − 1

n − u − 1 n − k − 1 −

n − 1 k − 1

|F| ≤

. (1) It is easy to see that the theorem above is sharp for each integer u ∈ [3, k]: consider

+

the families Au := {F ∈

[n] k

: F ⊃ [2, u + 1] or 1 ∈ F, F ∩ [2, u + 1] = ∅}, u ∈ [2, k].

![image 1](<2017-kupavskii-diversity-uniform-intersecting-families_images/imageFile1.png>)

∗Moscow Institute of Physics and Technology, University of Birmingham; Email: kupavskii@yandex.ru Research supported by the grant RNF 16-11-10014.

1

The family A3 has diversity nk−−34 and size nk−−11 + nk−−34 − nk−−14 = 3 nk−−23 + nk−−33 . The family A2 has the same size as A3 (and this is why the case u = 2 does not appear in the

Theorem 1), but the diversity of A2 is bigger: it is equal to nk−−23 . The following problem was suggested by Katona and addressed by Lemons and Palmer

- [19]: what is the maximum diversity of an intersecting family F ⊂ [nk] ? They found out that for n > 6k3 we have γ(F) ≤ nk−−23 , with the equality possible only for A2 and some


of its subfamilies. Recently, Frankl [8] (Theorem 2.4) proved that γ(F) ≤ nk−−23 for all n ≥ 6k2, and conjectured that the same holds for n > 3k.

The purpose of this note is to prove the following theorem

- Theorem 2. There exists a constant C, such that for any n > Ck > 0 any intersecting

family F ⊂ [nk] satisﬁes γ(F) ≤ nk−−23 . Moreover, if γ(F) = nk−−23 , then F is a subfamily of an isomorphic copy of A2.

We note that a somewhat similar proof strategy, which ﬁrst uses results on Boolean functions to obtain some rough structure for the problem, and then uses combinatorics to obtain a precise result, was recently used by Keller and Lifshitz [15] in a much more general setting.

2 Proof of Theorem 2

The following theorem, proven by Dinur and Friedgut [4], is the main ingredient in the proof. We say that a family J ⊂ 2[n] is a j-junta, if there exists a subset J ⊂ [n] of size j (the center of the junta), such that the membership of a set in F is determined only by its intersection with J, that is, for some family J ∗ ⊂ 2J (the deﬁning family) we have F = {F : F ∩ J ∈ J ∗}.

- Theorem 3 ([4]). For any integer r ≥ 2,there exist functions j(r), c(r), such that for any


integers 1 < j(r) < k < n/2, if F ⊂ [nk] is an intersecting family with |F| ≥ c(r) nk−−rr , then there exists an intersecting j-junta J with j ≤ j(r) and

n − r k − r

|F \ J | ≤ c(r)

. (2)

We start the proof of the theorem. Choose C suﬃciently large (its choice will become clear later), n > Ck > 0 and an intersecting family F ⊂ [nk] . Then, applying Theorem 3 with r = 5, we get that there exists a j-junta J , j ≤ j(5), such that |F \J | ≤ c(5) nk−−55 <

n−5

k−4 , where the second inequality holds provided C is large enough. The ﬁrst step is to show that, unless J = A2, we have γ(F) < nk−−23 .

Proposition 4. Consider an intersecting j-junta J ⊂ 2[n], with center J ⊂ [n], |J| = j, and deﬁned by an intersecting family J ∗ ⊂ 2J. Then J satisﬁes one of the two following properties:

- • J is contained in a family isomorphic to A2.
- • There exists i ∈ J, such that all sets from J ∗ of size at most 2 contain i.


Proof. Note that the intersecting families of ≤ 2-element sets which cannot be pierced by a single element are isomorphic to [3]2 . Therefore, the junta that does not fall into the second category must have the center of size 3 and be deﬁned by a family containing all 2-element subsets of the center. Then we are only left to observe the fact that A2 is a junta with center J = [3] and deﬁned by the family J ∗ = [3]2 ∪ [3]:

[n] k

: |A ∩ [3]| ≥ 2 .

A2 = A ∈

![image 2](<2017-kupavskii-diversity-uniform-intersecting-families_images/imageFile2.png>)

![image 3](<2017-kupavskii-diversity-uniform-intersecting-families_images/imageFile3.png>)

![image 4](<2017-kupavskii-diversity-uniform-intersecting-families_images/imageFile4.png>)

![image 5](<2017-kupavskii-diversity-uniform-intersecting-families_images/imageFile5.png>)

Assume that J is not isomorphic to A2. Then, as it follows from the proposition above, γ(J ) ≤ 2j nk−−3j . If C = n/k is suﬃciently large, then

2j C

2j+1 C

n − j k − 3 ≤

n − 3 k − 2 ≤

n − 3 k − 2

- 1

![image 6](<2017-kupavskii-diversity-uniform-intersecting-families_images/imageFile6.png>)

- 2


n k − 2

2j

<

.

![image 7](<2017-kupavskii-diversity-uniform-intersecting-families_images/imageFile7.png>)

![image 8](<2017-kupavskii-diversity-uniform-intersecting-families_images/imageFile8.png>)

Moreover, nk−−45 < 21 nk−−23 for any n ≥ 2k. Therefore, in this case we can conclude that

![image 9](<2017-kupavskii-diversity-uniform-intersecting-families_images/imageFile9.png>)

n − 3 k − 2

γ(F) ≤ γ(J ) + |F \ J | <

.

From now on we suppose that J = A2. For i = 1, 2, 3 consider the families Fi := {F ∈ F : F ∩[3] = {i}}. W.l.o.g., assume that F1 has the largest size among Fi. We will use the following obvious bound: γ(F) ≤ |F| − δ1. Consider the following three families on [4, n]:

- G := F ∩ [4, n] : F ∈ F, F ∩ [3] = {2, 3} ,
- H1 := F ∩ [4, n] : F ∈ F1 , H2 := F : F ∈ F, F ⊂ [4, n] .


Clearly, G ⊂ [4k−,n2] , H1 ⊂ [4k−,n1] , H2 ⊂ [4k,n] . Most importantly, γ(F) ≤ |G| + |F2| + |F3| + |H2| ≤ |G| + 2|F1| + |H2| = |G| + 2|H1| + |H2|.

Therefore, to conclude the proof of the theorem, it is suﬃcient to show the following two inequalities:

n − 3 k − 2

|G| + 4|H1| ≤

, (3)

n − 3 k − 2

|G| + 2|H2| ≤

. (4)

Summing these two inequalities with coeﬃcients equal to 1/2, we get that γ(F) ≤ nk−−23 . There are two important properties that we are going to use. The ﬁrst one is that

F\J = F1∪F2∪F3∪H2, and thus, using |H1| = |F1|, we have |H1|, |H2| ≤ |F\J | ≤ nk−−45 . The second one is that the pair of families G, H1 as well as G, H2 are cross-intersecting. We say that two families are cross-intesecting, if any set from one intersects any set from the other.

In what follows we show that (3), (4) hold in a more general form. Similar inequalities appeared in [18], [9] and [17].

Lemma 5. Consider a set [m] and two cross-intersecting families A ⊂ [ma] , B ⊂ [mb] . Assume that m > (C′ + 1) · max{a, b} for some constant C′. Assume also that |B| ≤

m−(b−a+1)

a−1 . Then

m a

|A| + C′|B| ≤

. (5)

Before proving the lemma, let us deduce the inequalities (3), (4) out of (5) and thus conclude the proof of Theorem 2. For (3) we need to substitute A := G, B := H1, a := k − 2, b := k, C′ := C, [m] := [4, n]. Then we conclude that (3) holds even with 4 replaced by C. The deduction of (4) is similar. Moreover, we get that a pair of families may achieve equality in (3) and (4) only if H1 = H2 = ∅ (and therefore Fi = ∅ for i ∈ [3]). Therefore, if γ(F) = nk−−23 , then F ⊂ A2.

To prove Lemma 5, we need to give some deﬁnitions, related to the famous KruskalKatona theorem. A lexicographical order (lex) on the sets from [nk] is an order, in which

- A is less than B iﬀ the minimal element of A \ B is less than the minimal element of
- B \A. For 0 ≤ m ≤ nk let L(m, k) be the collection of m largest sets with respect to lex.


Theorem 6 ([16],[14]). Suppose that A ⊂ [na] , B ⊂ [nb] are cross-intersecting. Then the families L(|A|, a), L(|B|, b) are also cross-intersecting.

Proof of Lemma 5. Using Theorem 6, we may w.l.o.g. assume that A = L(|A|, a), B = L(|B|, b). Due to the restriction on the size of B, any set in it contains [b−a+1]. Consider the families

B0 :={B \ [b − a + 1] : B ∈ B}, A0 :={A : A ∈ A, A ∩ [b − a + 1] = ∅}.

Put Y := [b−a+2, m] (if b < a, put Y := [1, m]). Note that |Y | = min{m−(b−a+1), m}. Clearly, B0 ⊂ a Y−1 and A0 ⊂ Ya . Consider a bipartite graph G with parts Ya , a Y−1 , and edges connecting disjoint sets. Then the intersection of A ∪ B with the parts of the graph is A0 ∪ B0, and it forms an independent set in G0. Thus, we have

|A0|

+ |B0|

≤ 1.

![image 10](<2017-kupavskii-diversity-uniform-intersecting-families_images/imageFile10.png>)

![image 11](<2017-kupavskii-diversity-uniform-intersecting-families_images/imageFile11.png>)

|Y | a

|Y | a−1

We have |Ya| / a |Y−1| = (|Y | − a)/a = min{m − a, m − b − 1}/a ≥ C′. This implies

|Y |

a |B0|

|A0| + C′|B0| ≤ |A0| +

≤

![image 12](<2017-kupavskii-diversity-uniform-intersecting-families_images/imageFile12.png>)

|Y | a−1

|Y | a

.

The lemma follows from the fact that

|A| + C′|B| ≤

m a −

|Y | a

+ |A0| + C′|B0| ≤

m a

.

![image 13](<2017-kupavskii-diversity-uniform-intersecting-families_images/imageFile13.png>)

![image 14](<2017-kupavskii-diversity-uniform-intersecting-families_images/imageFile14.png>)

![image 15](<2017-kupavskii-diversity-uniform-intersecting-families_images/imageFile15.png>)

![image 16](<2017-kupavskii-diversity-uniform-intersecting-families_images/imageFile16.png>)

## 3 What happens when 2k ≤ n ≤ 3k?

Under the same assumption that we make in Theorem 2, it is possible to prove certain Hilton-Milner type stability results for diversity (using more elaborate versions of Lemma 5). However, we think that it is more interesting to resolve the problem for any n > 3k and show that the family with the maximum possible diversity must be isomorphic to a subfamily of A2, or the “two out of three” family. When 2k < n < 3k, then other families have larger diversity. They can be described as “r + 1 out of 2r + 1” families:

Dr := D ∈

[n] k

: |D ∩ [2r + 1]| ≥ r + 1 , r = 1, . . ., k − 1. (6)

The following seems to be a reasonable conjecture at a ﬁrst glance. Conjecture Fix n ≥ 2k > 0 and consider an intersecting family F ⊂ [nk] . If for

some r ∈ Z≥0 we have (k −1) 2+ r+11 +1 ≤ n ≤ (k −1) 2+ 1r +1, then γ(F) ≤ γ(Dr).

![image 17](<2017-kupavskii-diversity-uniform-intersecting-families_images/imageFile17.png>)

![image 18](<2017-kupavskii-diversity-uniform-intersecting-families_images/imageFile18.png>)

Substituting r = 0 in the conjecture, we get that γ(F) ≤ nk−−23 for any n ≥ 3k − 2. Let us explain what stands behind this naive conjecture. Assume that the element with the highest degree in F is 1. Then the conjecture is just stating that, if one restricts the attention to the family F′ := {F ∈ F : 1 ∈/ F}, F ⊂ [2k,n] , then the size of F′ is at most the size of the largest 2-intersecting family on [2, n]. We say that a family is t-intersecting, if any two sets from the family intersect in at least t elements. The exact formulas given in the naive conjecture come from the famous Complete Intersection Theorem by Ahlswede and Khachatrian [1].

The families Dr′ ⊂ [2k,n] , Dr′ := {D ∈ Dr : 1 ∈/ D} are 2-intersecting. And it comes as no surprise. Indeed, the same must be true for any shifted intersecting family F. Let us ﬁrst give the deﬁnition of shifting.

For a given pair of indices 1 ≤ i < j ≤ n and a set A ⊂ [n] deﬁne its (i, j)-shift Si,j(A) as follows. If i ∈ A or j ∈/ A, then Si,j(A) = A. If j ∈ A, i ∈/ A, then Si,j(A) := (A − {j}) ∪ {i}. That is, Si,j(A) is obtained from A by replacing j with i.

The (i, j)-shift Si,j(F) of a family F is as follows:

Si,j(F) := {Si,j(A) : A ∈ F} ∪ {A : A, Si,j(A) ∈ F}. We call a family F shifted, if Si,j(F) = F for all 1 ≤ i < j ≤ n.

For any shifted family δ1(F) = ∆(F) and, if F is intersecting, then F′ must be 2-intersecting. Indeed, if there are two sets F1, F2 ∈ F, such that F1, F2 ⊂ [2, n] and F1 ∩ F2 = {x}, then, by shiftedness, F1′ := F1 \ {x} ∪ {1} also belongs to F, and we have F1′ ∩ F2 = ∅, a contradiction. Consequently, the naive conjecture is true for such F).

Therefore, the conjecture above states that any intersecting family should behave as shifted intersecting families with respect to diversity. Shifting preserves the property of a family to be intersecting, but, unfortunately, it does not allow to control the diversity of a family. This is why the general case cannot be directly reduced to shifted case. In fact, it cannot be reduced to the shifted case at all: the conjecture is false for families that are not shifted!

### 3.1 Intersecting families with the largest diversity are not shifted

Here we present a counterexample to the conjecture above found and communicated to us by Noam Lifshitz. As the counterexample shows, at least in some cases the extremal value of γ(F) is attained on the families that are not shifted, which is unexpected for a problem concerning intersecting families.

We use the notions and results coming from the analysis of Boolean functions. We give all the necessary deﬁnitions, and all the standard results used here may be found in

- [20]. For a real number 0 < p < 1 and a set F ⊂ [n] and F ⊂ 2[n], deﬁne the p-biased


measure µp(F) := p|F|(1 − p)n−|F| and µp(F) := F∈F µp(F). The inﬂuence Iip(F) of coordinate i in F is

Iip(F) := µp {F : |{F, F∆{i}| ∩ F = 1} , and the total inﬂuence is Ip(F) := i Iip(F). In case if F is closed upwards, we have

Iip(F) = p−1µp {F ∈ F : i ∈ F} − (1 − p)−1µp {F ∈ F : i ∈/ F} . (7) Fix a suﬃciently large r and even bigger k ≥ k0(r), n ≥ n0(r), satisfying the condi-

tions on n from the conjecture. Put p := nk. That is, p = 12 − (1 + o(1))1r.

![image 19](<2017-kupavskii-diversity-uniform-intersecting-families_images/imageFile19.png>)

![image 20](<2017-kupavskii-diversity-uniform-intersecting-families_images/imageFile20.png>)

![image 21](<2017-kupavskii-diversity-uniform-intersecting-families_images/imageFile21.png>)

Intersecting family with low inﬂuences. In what follows, we describe the family Tr, which restriction Tr∩J (see below) provides an example showing that the Kahn-KalaiLinial inequality [12] is sharp for indicator functions of intersecting families. The family Tr has larger diversity than Dr. The example is taken from Gil Kalai’s post on MathOverﬂow [13], however, since the explanation of the necessary properties in the post was very brief, we expand the exposition here, hopefully providing all the necessary details.

Consider an intersecting family Tr ⊂ [nk] , which is a (2r + 1)-junta with center J := [2r + 1], and Tr ∩ J is the following intersecting family. Arrange the elements of J on the circle, and for each set S ⊂ 2J form a sequence u := (u1, u2, . . .), where ui is the length of the i-th longest run of consecutive 1’s; similarly, z := (z1, z2, . . .) is the sequence, in which zi is the i-th longest run of consecutive 0’s. Form Tr ∩ J by including all sets, for which its sequence u is lexicographically bigger than z (we denote it u ≻ z). Note that, since |J| is odd, we cannot have equality between the sequences. Therefore, we have

|Tr ∩ J| = 2|J|−1 since if T ⊂ J is in Tr ∩ J, then its complement J \ T is not, and vice versa.

Let us show that Tr ∩ J is an intersecting family. Assume the contrary, and let T1, T2 be two disjoint sets in Tr ∩ J. Let ui, zi, i = 1, 2, be the corresponding one and zero runs sequences. Then, clearly, z1 ≻ u2 and z2 ≻ u1, otherwise, it would be impossible to ﬁt the runs of 1’s of T1 inside the runs of 0’s of T2 (and the same with the roles of T1, T2 interchanged). However, if, say, u1 ≻ u2, then by transitivity z2 ≻ u2, a contradiction.

In what follows, all logarithms have base 2 and all asymptotic notations are with respect to r → ∞.

- Lemma 7. For each i ∈ J, we have Ii1/2(Tr ∩ J) = O logr r .


![image 22](<2017-kupavskii-diversity-uniform-intersecting-families_images/imageFile22.png>)

Proof. The proof requires a somewhat tedious analysis of the typical sets in the family. The family is clearly transitive on J, and thus it is suﬃcient to show that I1/2(Tr ∩ J) =

O(log r). The total inﬂuence I1/2(Tr ∩ J) is the average number of pivotal coordinates in a randomly chosen set from J according to µ1/2, that is, the number of coordinates which change results in the set passing from Tr ∩ J to its complement or vice versa.

Choose a random set T ∈ J according to µ1/2 and denote its zero and one runs sequences z := (z1, z2, . . .) and u := (u1, u2, . . .), respectively. The coordinate is pivotal, if after its change the lexicographical order of z and u is reversed.

Using ﬁrst moment, it is easy to see that with probability 1−o(1/r) the largest run of consecutive 1’s in T has size at most (2 + o(1)) log r, and the same for the runs of zeros. Thus, the sequences not satisfying this property contribute o(1) to the total inﬂuence. In what follows we ignore such sequences.

In what follows, we assume that u ≻ z. The other case is treated analogously. Choose ρ such that zρ = uρ for j ≤ ρ and uρ+1 > zρ+1. The lex order is reversed if at least one of the two happens: either (u1, . . ., uρ+1) is replaced by a lexicographically smaller sequence, or (z1, . . ., zρ+1) is replaced by a lexicographically larger sequence. Denote the number of the former and latter types by s1 and s2, respectively. The number of pivotal coordinates is at most s1 + s2, but we will bound just s1 instead. A pivotal coordinate

- k of the second type is a pivotal coordinate of the ﬁrst type for the set T \ {k}, and, since µ1/2(T) = µ1/2(T \{k}), the average value of s1 is not more than twice smaller than


- s1 + s2, Thus if E[s1] = O(log r), then E[s1 + s2] = O(log r). From the above, we clearly have s1 ≤ ρj=1+1 uρ. Moreover, ui = O(log r) for each i =


1 . . ., ρ+1. Consequently, we can bound E[s1] ≤ E[ ρj=1+1 O(log r)] = O(log r) ∞k=1 Pr[ρ ≥ k]. We use a slight variation of this bound. Since the number of pivotal coordinates is at

most 2r + 1, we can bound

r0 1

E[s1] ≤ O(log r)

Pr[ρ ≥ k] + (2r + 1) Pr[ρ ≥ r0.1]. (8)

k=1

To complete the proof that E[s1] = O(log r) (and thus the proof of the lemma), it is suﬃcient to show the validity of the following lemma

- Lemma 8. For any ρ ≤ r0.1 we have Pr[ρ ≥ k] ≤ e−αlog2k + o(1/r) for some α < 1. In particular, Pr[ρ ≥ rβ] = o(1/r) for any ﬁxed β > 0.


We defer the proof of this lemma to the end of the section, and ﬁnish the proof of Lemma modulo Lemma 8. From it, we have Pr[ρ ≥ r0.1] = o(1/r), and the right hand side of the inequality (8) is at most O(log r) ∞k=1 e−αlog2k + o(1) = O(log r).

![image 23](<2017-kupavskii-diversity-uniform-intersecting-families_images/imageFile23.png>)

![image 24](<2017-kupavskii-diversity-uniform-intersecting-families_images/imageFile24.png>)

![image 25](<2017-kupavskii-diversity-uniform-intersecting-families_images/imageFile25.png>)

![image 26](<2017-kupavskii-diversity-uniform-intersecting-families_images/imageFile26.png>)

Consider the family Tr↑ := {T ⊂ [n] : T ∩ J ∈ Tr ∩ J}. Then we have µ1/2(Tr↑) = 1/2. Similarly, deﬁne the family Dr↑ based on Dr. Again, µ1/2(Dr↑) = 1/2. Deﬁne the p-biased diversity of F as γp(F) := mini∈[n] µp({F ∈ F : i ∈/ F}).

Using the result of Dinur and Safra [5], for suﬃciently large n = n(r) we have

γ(Tr) n k

γp(Tr↑) −

![image 27](<2017-kupavskii-diversity-uniform-intersecting-families_images/imageFile27.png>)

1 r2

≤

, (9)

![image 28](<2017-kupavskii-diversity-uniform-intersecting-families_images/imageFile28.png>)

and the same for Dr and Dr↑. (Note that we use the fact that both families Tr ∩ {T ⊂ J : 1 ∈/ T} and Dr ∩ {T ⊂ J : 1 ∈/ T} are 2r + 1-juntas.) Using the Margulis-Russo lemma, for any upwards closed family F ⊂ 2J and p0 ∈ (0, 1), we have

dµp(F) dp |p0

= Ip

(F).

0

![image 29](<2017-kupavskii-diversity-uniform-intersecting-families_images/imageFile29.png>)

Using large deviation estimates, it is not diﬃcult to see, that for any p0 ∈ [p, 1/2] the contribution of sets from F of size not in [r − r2/3, r + r2/3] to the inﬂuence is negligible (since the measure of such sets is negligible). On the other hand, for any F of size in [r − r2/3, r + r2/3], we have µp

(F) = (1 + o(1))µ1/2(F) for any p0 ∈ [p, 1/2]. Thus, Ip

0

(F) = (1 + o(1))I1/2(F) for any such p0. We conclude that we have µ1/2(F) − µp(F) = (1 + o(1))(1/2 − p)Ip(F).

- 0


At the same time, for a symmetric, closed upward family F ⊂ 2J and for any i ∈ J we have pIip(F) + 1−1pγp(F) = µp(F). Therefore,

![image 30](<2017-kupavskii-diversity-uniform-intersecting-families_images/imageFile30.png>)

p + 2 1 − p |J| |J|

p |J|

![image 31](<2017-kupavskii-diversity-uniform-intersecting-families_images/imageFile31.png>)

Ip(F) = (1−p)µ1/2(F)−(1−p+o(1))

Ip(F).

γp(F) = (1−p) µp(F)−

![image 32](<2017-kupavskii-diversity-uniform-intersecting-families_images/imageFile32.png>)

![image 33](<2017-kupavskii-diversity-uniform-intersecting-families_images/imageFile33.png>)

We know that Ip(Dr ∩ J) = Ω(√r), since Dr ∩ J is the majority function. On the other hand, using Lemma 3.1, we have Ip(Tr ∩J) = O(log r). Using the displayed formula above, we get

![image 34](<2017-kupavskii-diversity-uniform-intersecting-families_images/imageFile34.png>)

- 1 − p

![image 35](<2017-kupavskii-diversity-uniform-intersecting-families_images/imageFile35.png>)

- 2 − Ω


γp(Dr↑) = γp(Dr ∩J) =

1 √r

![image 36](<2017-kupavskii-diversity-uniform-intersecting-families_images/imageFile36.png>)

![image 37](<2017-kupavskii-diversity-uniform-intersecting-families_images/imageFile37.png>)

- 1 − p

![image 38](<2017-kupavskii-diversity-uniform-intersecting-families_images/imageFile38.png>)

- 2 − O


and γp(Tr↑) = γp(Tr ∩ J) =

log r r

![image 39](<2017-kupavskii-diversity-uniform-intersecting-families_images/imageFile39.png>)

.

Combining the formulas above with (9), we conclude that γ(Dr) < γ(Tr).

Proof of Lemma 8. How to express the condition that for a random sequences its vectors of zero and one runs share the ﬁrst k coordinates? Let N(t) be a random variable counting the number of runs of length at least t in the sequence. Choose an integer t0 such that N(t0) ≤ k, but N(t0 − 1) > k. In order to have ρ ≥ k, exactly a half of each N(t),

- t ≥ t0, must be zero runs, and a half must be one runs. In what follows, we analyze the behaviour of N(t).


Take an integer t and ﬁx the value of N(t). For each run of length at least t, reveal the values of the ﬁrst t coordinates that belong to the run (in the clockwise order), as well as the value that precedes the run clockwise. E.g., for t = 3 the sequence may look like xx0111xxx1000xx1000x. . ., where x stands for the coordinates that are not revealed. Let us denote Lj, j ∈ [N(t)], the intervals of unrevealed coordinates between the revealed coordinates. If some Lj has length smaller than r1/10, then reveal its coordinates, otherwise keep it intact. Let us denote S the class of all possible subsequences that can be ﬁxed (revealed) in this way. Each subsequence S ∈ S gives rise to a family C(S) of sequences containing S as a subsequence. Fix any subclass S′ ⊂ S. Then for a randomly chosen cyclic sequence R we have

Pr[ρ ≥ k] ≤

Pr[ρ ≥ k|R ∈ C(S)] Pr[R ∈ C(S)] +

S∈S\S′

Pr[R ∈ C(S)]. (10)

S∈S′

That is, one may think of S′ as a small set of “exceptional” classes. We will show that the latter term on the right hand side is o(1/r), while Pr[ρ ≥ k|R ∈ C(S)] ≤ e−αlog2k for each S ∈ S \ S′. Since s∈S\S′ Pr[R ∈ C(S)] ≤ 1, this will conclude the proof of the lemma.

We note that the expected value of N(t) is r2−t (we choose the starting point, choose arbitrarily the coordinate x before the starting point, and then ﬁx the t coordinates to be equal to 1−x). Moreover, using the Talagrand inequality (e.g., in the form of [2, Theorem

7.7.1]), we can show that when the expectation is, say, bigger than r1/10, then the value of N(t) is well-concentrated around the expectation (it is equal to (1 + o(1))E[N(t)] with probability at least 1 − r−c for any c > 0). We restrict our attention only on the values of t such that the expected value of N(t) does not exceed r1/10, and we include in S′ all sequences for which the value of N(t) exceeds 2r1/10. By the above, there are o(1/r) of those.

Fix some t satisfying the condition E[N(t)] ≤ r1/10 and note that t = Ω(log r). The probability that there is more than one interval Lj of unrevealed coordinates of length ≤ r1/10, given that N(t) ≤ 2r1/10, is o(1/r). Indeed, compare the number of all possible

choices for the starting positions of the runs of length ≥ t (roughly N r(t) ) with the number of choices, in which we ﬁrst ﬁx N(t) − 2 starting positions of such runs, and then choose the remaining two at distance at most 2r1/10 from one of the already chosen ones (at most N(t r)−2 · (4r1/5)2). Include all such subsequences in S′. We are not going to include any more subsequences in S′ and we note that there are o(1/r) sequences that contain subsequences from S′.

Fix one subsequence S ∈ S \ S′. We aim to bound Pr[ρ ≥ k|R ∈ C(S)]. Consider a uniform distribution over all sequences in C(S). Recall that at least [N(t)] − 1 of Lj are unrevealed. We note that the only restriction on the choices of coordinates in Lj is that they cannot contain runs of ones or zeros of length ≥ t, moreover, there is no dependency between the choices of coordinates in diﬀerent Lj. Next, for each j we reveal the ﬁrst coordinate xj of Lj in the clockwise order. We claim that Pr[xj = 1] = (21 +o(1)). Indeed, for each admissible sequence starting from xj we change xj to 1 − xj and obtain an admissible sequence and vice versa, unless the t − 1 elements immediately following xj have the same value, while xj had the opposite value. But this constitutes at most a

![image 40](<2017-kupavskii-diversity-uniform-intersecting-families_images/imageFile40.png>)

- 1/2t-fraction of all possible admissible sequences on Lj, and thus only aﬀects the value of Pr[xj = 1] by o(1).


Since the choices for diﬀerent xj are independent, we have the following. First, the

expected number E[N(t+1)] of “surviving” runs of length t+1 is (12+o(1))N(t). Moreover, it is tightly concentrated around the expectation: using a Chernoﬀ-type bound, we have

![image 41](<2017-kupavskii-diversity-uniform-intersecting-families_images/imageFile41.png>)

Pr[|N(t + 1) − 21N(t)| ≥ 16N(t)] ≤ e−cN(t) for some ﬁxed positive constant c.

![image 42](<2017-kupavskii-diversity-uniform-intersecting-families_images/imageFile42.png>)

![image 43](<2017-kupavskii-diversity-uniform-intersecting-families_images/imageFile43.png>)

Now we are in position to bound Pr[ρ ≥ k|R ∈ C(S)]. First, we ﬁnd t0 as in the ﬁrst paragraph of the proof of the lemma. By the previous paragraph, with probability at least 1 − e−ck for some ﬁxed c > 0 we have 3N(t0) ≥ k and 27N(t0 + 2) ≥ k. In order for ρ ≥ k to hold, a half of runs contributing to N(t0) should be one runs, and the other half should be zero runs. Moreover, the same should be true for N(t) for t ≥ t0 + 1. Thus, we can obtain the following rough bound:

k 27|R ∈ C(S) · P1,

Pr[ρ ≥ k|R ∈ C(S)] ≤ Pr[ρ ≥ N(t0 + 2)|R ∈ C(S)] · P1 ≤ e−ck + Pr ρ ≥

![image 44](<2017-kupavskii-diversity-uniform-intersecting-families_images/imageFile44.png>)

where P1 is the probability that the values xj will be chosen in such a way that the number of zero and one runs of length at least t0 + 1 is the same. It is easy to see that

P1 ≤ (1 + o(1))2−N(t

0)

N(t0)/2

j=0

N(t0)/2 j

2

= Θ N(t0)−1/2 .

(note here that we have to take into account the interval Lj that was ﬁxed and that potentially gave one zero or one run of length t0, but it does not aﬀect the validity of the bound above). Looking at the recursion Pr[ρ ≥ k] ≤ e−ck + Θ(k−1/2) Pr[ρ ≥ k/27],

it is not diﬃcult to conclude that Pr[ρ ≥ k] ≤ e−αlog2k for some positive constant α. Substituting into (10), we get the result.

![image 45](<2017-kupavskii-diversity-uniform-intersecting-families_images/imageFile45.png>)

![image 46](<2017-kupavskii-diversity-uniform-intersecting-families_images/imageFile46.png>)

![image 47](<2017-kupavskii-diversity-uniform-intersecting-families_images/imageFile47.png>)

![image 48](<2017-kupavskii-diversity-uniform-intersecting-families_images/imageFile48.png>)

We remark that the problem treated in Lemma 8 seems to be interesting on its own and that it would be desirable to have a fuller understanding of the behaviour of the probability Pr[ρ ≥ k]. However, we believe that the bound on the probability (modulo o(1/r) and the constant α in the exponent) is essentially sharp.

Remark. While preparing the second version of the manuscript, Hao Huang provided another counterexample to the conjecture in the range 3k ≤ n ≤ (2 + √3)k [11]. We presented our counterexample because we thought that the method used to derive it is interesting in its own right.

![image 49](<2017-kupavskii-diversity-uniform-intersecting-families_images/imageFile49.png>)

Acknowledgements: I thank Peter Frankl for introducing me to the concept of diversity and the problem studied in the paper, as well as for many fruitful discussions and interesting ideas that he shared with me. I thank Noam Lifshitz for proposing a simpliﬁed proof of Lemma 5 and especially for ﬁnding the beautiful counterexample from the last section, as well as pointing out several errors in the earlier version of the text of Section 3.1. I also thank Maksim Zhukovskii for helpful discussions on the proof of Lemma 8.

## References

- [1] R. Ahlswede, L. Khachatrian, The complete intersection theorem for systems of ﬁnite sets, Eur. J. Comb. 18 (1997), N2, 125–136.
- [2] N. Alon, J. Spencer, The probabilistic method, Third Edition, John Wiley & Sons, 2004.
- [3] G.E. Andrews, K. Eriksson, Integer partitions, Cambridge University Press (2004).
- [4] I. Dinur, E. Friedgut, Intersecting families are essentially contained in juntas, Combinatorics, Probability and Computing 18 (2009), 107–122.
- [5] I. Dinur, S. Safra, On the hardness of approximating minimum vertex-cover, Ann. Math. 162 (2005), pp. 439–485.
- [6] P. Erd˝os, C. Ko, R. Rado, Intersection theorems for systems of ﬁnite sets, The Quarterly Journal of Mathematics, 12 (1961) N1, 313–320.
- [7] P. Frankl, Erdos-Ko-Rado theorem with conditions on the maximal degree, Journal of Combinatorial Theory, Series A 46 (1987), N2, 252–263.
- [8] P. Frankl, Antichains of ﬁxed diameter, Moscow Journal of Combinatorics and Number Theory 7 (2017), N3
- [9] P. Frankl, A. Kupavskii, Erd˝s-Ko-Rado theorem for {0 ± 1}-vectors, J. Comb. Th. Ser. A 155 (2018), 157–179, arXiv:1510.03912
- [10] A.J.W. Hilton, E.C. Milner, Some intersection theorems for systems of ﬁnite sets, Quart. J. Math. Oxford 18 (1967), 369–384.
- [11] H. Huang, Two problems on intersecting families, arXiv:1804.11269


- [12] J. Kahn, G. Kalai, N. Linial, The inﬂuence of variables on Boolean functions, Proc. 29th Annual Symposium on Foundations of Computer Science (1988), 68–80.
- [13] G. Kalai, A post on MathOverﬂow, https://mathoverflow.net/questions/105086/kahn-kalai-linial-for-intersecting-upsets
- [14] G. Katona, A theorem of ﬁnite sets, “Theory of Graphs, Proc. Coll. Tihany, 1966”, Akad, Kiado, Budapest, 1968; Classic Papers in Combinatorics (1987), 381–401.
- [15] N. Keller, N. Lifshitz, The junta method for hypergraphs and the Erd˝s-Chv´tal simplex conjecture, arXiv:1707.02643
- [16] J.B. Kruskal, The Number of Simplices in a Complex, Mathematical optimization techniques 251 (1963), 251–278.
- [17] A. Kupavskii, Structure and properties of large intersecting families, arXiv:1710.02440
- [18] A. Kupavskii, D. Zakharov, Regular bipartite graphs and intersecting families, J. Comb. Th. Ser. A 155 (2018), 180–189, arXiv:1611.03129
- [19] N. Lemons, C. Palmer, Unbalance of set systems, Graphs and Combinatorics 24

(2008), N4, 361–365.

- [20] R. O’Donnell, Analysis of boolean functions, Cambridge University Press, New York, NY (2014).


