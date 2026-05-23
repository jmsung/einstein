---
type: source
kind: paper
title: Two extremal problems on intersecting families
authors: Hao Huang
year: 2018
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/1804.11269v1
source_local: ../raw/2018-huang-two-extremal-problems-intersecting.pdf
topic: general-knowledge
cites:
---

arXiv:1804.11269v1[math.CO]30Apr2018

Two extremal problems on intersecting families

Hao Huang ∗

Abstract

In this short note, we address two problems in extremal set theory regarding intersecting families. The ﬁrst problem is a question posed by Kupavskii: is it true that given two disjoint cross-intersecting families A,B ⊂ [nk] , they must satisfy min{|A|,|B|} ≤ 12 nk−−11 ? We give an aﬃrmative answer for n ≥ 2k2, and construct families showing that this range is essentially the best one could hope for, up to a constant factor. The second problem is a conjecture of Frankl. It states that for n ≥ 3k, the maximum diversity of an intersecting family F ⊂ [nk] is equal to

![image 1](<2018-huang-two-extremal-problems-intersecting_images/imageFile1.png>)

n−3 k−2 . We are able to ﬁnd a construction beating the conjectured bound for n slightly larger

than 3k, which also disproves a conjecture of Kupavskii.

# 1 Disjoint cross-intersecting families

One of the most famous results in extremal set theory is the Erdo˝s-Ko-Rado Theorem [2]: for n ≥ 2k, an intersecting family F ⊂ [nk] has size at most nk−−11 . The Erdo˝s-Ko-Rado Theorem has many analogues and generalizations. One particularly interesting generalization is by considering two families instead of one. We say two families A and B are cross-intersecting, if for every A ∈ A and B ∈ B, A ∩ B = ∅. Pyber [13] showed that when n is large in k,l, for A ⊂ [nk] , B ⊂ [nl] , we have |A||B| ≤ nk−−11 nl−−11 . Later the same inequality for a precise range n ≥ 2 max{k,l} was established by Matsumoto and Tokushige [12]. The Erdo˝s-Ko-Rado Theorem follows immediately by setting k = l and A = B.

Recently Kupavskii [10] asked the following question: given two cross-intersecting families A and B that are disjoint, is it true that

n − 1 k − 1

- 1

![image 2](<2018-huang-two-extremal-problems-intersecting_images/imageFile2.png>)

- 2


min{|A|,|B|}} ≤

?

This bound, if true, is clearly tight. This is because we can always split the extremal example in Erdo˝s-Ko-Rado Theorem, i.e. a 1-star S, into two subfamilies S1,S2 as evenly as possible. Then A = S1 and B = S2 are cross-intersecting and disjoint, and each has about 21 nk−−11 subsets. In this section, we give a positive answer to this question for n quadratic in k.

![image 3](<2018-huang-two-extremal-problems-intersecting_images/imageFile3.png>)

Theorem 1.1. For n ≥ 2k2, given two disjoint cross-intersecting families A,B ⊂ [nk] , we have

n − 1 k − 1

- 1

![image 4](<2018-huang-two-extremal-problems-intersecting_images/imageFile4.png>)

- 2


min{|A|,|B|} ≤

.

![image 5](<2018-huang-two-extremal-problems-intersecting_images/imageFile5.png>)

∗Department of Math and CS, Emory University, Atlanta, GA 30322, USA. Email: hao.huang@emory.edu. Research supported in part by the Collaboration Grants from the Simons Foundation.

As a warm-up, ﬁrst we show that when n is at least cubic in k, this statement is true. Consider a pair of disjoint crossing-intersecting families A and B of k-sets of [n]. If both A and B are intersecting, then A ∪ B is also intersecting, by the Erdo˝s-Ko-Rado Theorem, for n ≥ 2k, we have

n − 1 k − 1

|A| + |B| ≤

, and thus we have the desired inequality

n − 1 k − 1

- 1

![image 6](<2018-huang-two-extremal-problems-intersecting_images/imageFile6.png>)

- 2


min{|A|,|B|} ≤

.

Now suppose at least one of A and B is not intersecting, without loss of generality we may assume that A is not intersecting, then there exists A1,A2 ∈ A, such that A1 ∩ A2 = ∅. Now the number of sets that intersect with both A1 and A2 provides an upper bound for |B|, which is at most

when n ≥ 2k3.

k2

n − 2 k − 2

k2(k − 1) (n − 1)

=

![image 7](<2018-huang-two-extremal-problems-intersecting_images/imageFile7.png>)

n − 1 k − 1

- 1

![image 8](<2018-huang-two-extremal-problems-intersecting_images/imageFile8.png>)

- 2


<

n − 1 k − 1

Next we will improve the range to n ≥ 2k2. The main tool used in this proof is the technique of shifting, which allows us to limit our attention to sets with certain structure. In this section we will only state and prove some relevant results. For more background on the applications of shifting in extremal set theory, we refer the reader to the survey [3] by Frankl.

Proof of Theorem 1.1. Now assume n ≥ 2k2, suppose there exist disjoint cross-intersecting families A,B ⊂ [nk] such that

n − 1 k − 1

- 1

![image 9](<2018-huang-two-extremal-problems-intersecting_images/imageFile9.png>)

- 2


min{|A|,|B|} >

.

We will prove the following statement: given positive integer k,l, and n ≥ k + l, suppose A ⊂ [nk] , B ⊂ [nl] are cross-intersecting. If |A| > max{k,l} nk−−22 and |B| > max{k,l} nl−−22 , then there exists some element x contained in every subset of A and B. Assuming this claim, if there exists x such that A,B are subfamilies of the 1-star centered at x, then |A ∪ B| ≤ nk−−11 , and Theorem 1.1 follows from the disjointness of A and B. Otherwise, either |A| or |B| has to be strictly smaller than

k − 1 n − 1

n − 2 k − 2

n − 2 k − 2 ≤

n − 2 k − 2

- 1

![image 10](<2018-huang-two-extremal-problems-intersecting_images/imageFile10.png>)

- 2


= k ·

k

![image 11](<2018-huang-two-extremal-problems-intersecting_images/imageFile11.png>)

for n ≥ 2k2, which also proves Theorem 1.1.

To show the claim, we use induction on k,l,n. Given a family F, deﬁne the (i,j)-shifting Sij as follows: let

Sij(F) = {Sij(F) : F ∈ F}, where

F′ i ∈ F, j  ∈ F, F′ = F \ {i} ∪ {j}  ∈ F; F otherwise.

Sij(F) =

.

It is well-known that if we apply Sij on A and B simultaneously, the resulting families are still cross-intersecting. Therefore we can iteratively apply the shifting Sij for j > i until we reach

stable families (Sij(A) = A, Sij(B) = B). We claim that not only A ∈ A and B ∈ B must intersect, their intersection must also contain some element from {1,··· ,k + l}. Suppose not, consider all the pairs (A,B) such that A∩B ∩[k +l] = ∅, pick the one which minimizes |A∩B|. Since A∩B = ∅, there exists i ∈ {k +l+1,··· ,n} such that i ∈ A∩B, and also j ∈ [k +l] such that j  ∈ A ∪ B. Since Sij(A) = A an Sij(B) = B, we must have A′ = A \ {i} ∪ {j} ∈ A. Note that A′ ∩ B ∩ [k + l] is still empty, and |A′ ∩ B| < |A ∩ B|, contradicting the choice of A,B.

Let K = {A ∩ [k + l] : A ∈ A} and L = {B ∩ [k + l] : B ∈ B}. We denote by Ki and Li the family of i-subsets in K and L respectively. Every set A ∈ A must instersect [k + l] with a subset from K, therefore

k

n − k − l k − i

|A| ≤

|Ki|

,

i=1

Similarly,

l

n − k − l l − i

|Li|

|B| ≤

.

i=1

Recall that |A| > max{k,l} nk−−22 , since

k

k + l − 2 i − 2

n − 2 k − 2

n − k − l k − i

=

,

i=1

we know that there exists i ∈ [k], such that |Ki| > max{k,l} k+i−l−22 ≥ i k+i−l−22 . Similarly there exists j such that |Lj| > max{k,l} k+j−l−22 ≥ j k+j−l−22 . Note that Ki and Lj are crossintersecting and k + l ≥ i + j, so by induction, as long as (n,k,l) = (k + l,i,j), there exists x in every set of Ki and Lj. Suppose there exists B ∈ B, such that x  ∈ B, then every set in Ki must intersect B and contains x, there are less than l ni−−22 ≤ max{k,l} ni−−22 such subsets, contracting that Ki is large. Similarly we can show that x is contained in every set of A. When (n,k,l) = (k + l,i,j), we know that A ⊂ [k+k l] and B ⊂ [k+l l] . Since A and B are crossintersecting, A and Bc = {[k + l] \ B : B ∈ B} must be disjoint. Therefore |A| + |B| ≤ k+k l . However, suppose k ≥ l, then by the assumption,

k + l − 2 k − 2

- k + l − 2
- l − 2


k + l k

|A| + |B| ≥ k

+ k

>

.

The last inequality is true for all k ≥ 2,l ≥ 2 except (k,l) = (2,2). In this case it is easy to check the statement is also true. This completes the proof of the previous claim, as well as Theorem 1.1.

![image 12](<2018-huang-two-extremal-problems-intersecting_images/imageFile12.png>)

![image 13](<2018-huang-two-extremal-problems-intersecting_images/imageFile13.png>)

![image 14](<2018-huang-two-extremal-problems-intersecting_images/imageFile14.png>)

![image 15](<2018-huang-two-extremal-problems-intersecting_images/imageFile15.png>)

Naturally one would wonder whether then range n ≥ 2k2 could be further improved. We will show that a quadratic range is necessary here. We consider the following construction, let t ≥ 2 be a ﬁxed integer much smaller than k or n. We choose A so that it consists of all the subsets whose intersection with [t+1] is either {1} or {2,··· ,t+1}. B consists of all the subsets whose intersection with [t + 1] contains 1 and some element of {2,··· ,t + 1}. Then

- |A| =

n − t − 1 k − 1

+

n − t − 1 k − t

,

- |B| =


n − 1 k − 1 −

n − t − 1 k − 1

.

We will choose k/n to be a ﬁxed constant, and let n,k tends to inﬁnity. To estimate the sizes of A and B, the following lemma is useful.

Lemma 1.2. Suppose k = αn for some ﬁxed α ∈ (0,1). Then for ﬁxed t,i, when n → ∞,

n − t k − i

n k → αi(1 − α)t−i.

/

Proof.

n−t k−i n k

k ···(k − i + 1) · (n − k)···(n − k − (t − i) + 1) n ···(n − t + 1)

=

![image 16](<2018-huang-two-extremal-problems-intersecting_images/imageFile16.png>)

![image 17](<2018-huang-two-extremal-problems-intersecting_images/imageFile17.png>)

k − i + 1 n − i + 1 ·

n − k n − i ···

n − k − (t − i) + 1 n − t + 1 → αi(1 − α)t−i.

k n ···

=

![image 18](<2018-huang-two-extremal-problems-intersecting_images/imageFile18.png>)

![image 19](<2018-huang-two-extremal-problems-intersecting_images/imageFile19.png>)

![image 20](<2018-huang-two-extremal-problems-intersecting_images/imageFile20.png>)

![image 21](<2018-huang-two-extremal-problems-intersecting_images/imageFile21.png>)

![image 22](<2018-huang-two-extremal-problems-intersecting_images/imageFile22.png>)

![image 23](<2018-huang-two-extremal-problems-intersecting_images/imageFile23.png>)

![image 24](<2018-huang-two-extremal-problems-intersecting_images/imageFile24.png>)

![image 25](<2018-huang-two-extremal-problems-intersecting_images/imageFile25.png>)

Now we returning to our construction. First observe that |A|+|B| > nk−−11 . Moreover when k/n ∼ α and n,k → ∞, by Lemma 1.2,

|A|

→ (1 − α)t + αt−1(1 − α).

![image 26](<2018-huang-two-extremal-problems-intersecting_images/imageFile26.png>)

n−1 k−1

|B|

→ 1 − (1 − α)t.

![image 27](<2018-huang-two-extremal-problems-intersecting_images/imageFile27.png>)

n−1 k−1

Note that for ﬁxed t, there exists some small positive constant c, such that for α in a small interval [1−(1/2)1/t,1−(1/2)1/t +c], both 1−(1−α)t > 1/2 and (1−α)t +αt−1(1−α) > 1/2. This shows that for α in this interval, if we let k = αn and n,k are suﬃciently large, there exists disjoint cross-intersecting A,B, both of size strictly greater than 12 nk−−11 . Note that 1−(1/2)1/t tends to 0 when t goes to inﬁnity. Therefore it is not possible to prove Theorem 1.1 for n > Ck for any ﬁxed constant C.

![image 28](<2018-huang-two-extremal-problems-intersecting_images/imageFile28.png>)

As pointed out to us by Frankl and Kupavskii [5], the same construction actually shows the quadratic range in Theorem 1.1 is best possible, up to a constant factor. This can be seen by setting t = k − 1 in the construction. Then |A| = nk−−1k + (n − k) and |B| = nk−−11 − nk−−1k . As long as |B| > |A| (which is true until n > Ck2 for some constant C), one can move subsets from B to A and still have a cross-intersecting family, since B itself is intersecting. Recall that the sum of their sizes is strictly greater than nk−−11 , therefore Theorem 1.1 is only correct for n at least qudratic in k. Frankl and Kupavskii have also obtained results similar to Theorem 1.1 using diﬀerent methods.

The proof of Theorem 1.1 relies on the assumption that n is quadratic in k, when we compare k nk−−22 with 12 nk−−11 . One may wonder whether it is possible to show that for smaller n, either |A| or |B| cannot exceed c nk−−11 , for some constant c strictly smaller than 1. The following result conﬁrms this speculations, and actually implies that for n = Ck, min{|A|,|B|} ≤ (21 +δC) nk−−11 , where δC goes to zero as C tends to inﬁnity.

![image 29](<2018-huang-two-extremal-problems-intersecting_images/imageFile29.png>)

![image 30](<2018-huang-two-extremal-problems-intersecting_images/imageFile30.png>)

- Theorem 1.3. For n ≥ 2k, given two cross-intersecting families A,B ⊂ [nk] that are disjoint, we have


n − 2 n − k − 1

n − 1 k − 1 ·

- 1

![image 31](<2018-huang-two-extremal-problems-intersecting_images/imageFile31.png>)

- 2


min{|A|,|B|} ≤

.

![image 32](<2018-huang-two-extremal-problems-intersecting_images/imageFile32.png>)

Proof. The key tool that will be used this proof is the spectrum of Kneser graphs. The Kneser graph KG(n,k) has vertices corresponding to all the k-subsets of [n], and two vertices are adjacent if and only if the two corresponding sets are disjoint. It is known that (see for example

on Page 200 of [6]) its adjacency matrix M has eigenvalues (−1)i+1 n−k−k−i i of multiplicity n i − i− n1 , where i = 0,··· ,k, and − n1 is deﬁned as 0. Moreover, the all-one vector is an

eigenvector of the largest eigenvalue n−kk . We denote by λ1,··· ,λ(

) the eigenvalues in the aforementioned order, i.e. non-increasing in absolute value, and assume that their corresponding eigenvectors are v1,··· ,v(

n k

), which form an orthonormal basis.

n k

We consider the characteristic vectors 1A and 1B of the two disjoint cross-intersecting families. Both of them are in the space {0,1}(n

). We can express them as linear combinations of the eigenvectors:

k

- 1A = α1v1 + ··· + α(

n k

)v(

n k

),

- 1B = β1v1 + ··· + β(n


). Since A and B are disjoint, the inner product of 1A and 1B equals 0. This gives

)v(n

k

k

α1β1 + ··· + α(

) = 0. (1) Moreover, from the cross-intersecting property, we have

)β(

n k

n k

0 = 1A,M · 1B = λ1α1β1 + ··· + λ(

) (2) Let

)β(

)α(

n k

n k

n k

n − k − 1 k − 1 −

n − k − 2 k − 2

- 1

![image 33](<2018-huang-two-extremal-problems-intersecting_images/imageFile33.png>)

- 2


K =

.

We multiply K to the (1) and add the resulting identity to the (2). It is not hard to observe that the coeﬃcient of α1β1 is equal to K + λ1, and the rest of the coeﬃcients have absolute value at most

n − k − 1 k − 1

n − k − 2 k − 2

- 1

![image 34](<2018-huang-two-extremal-problems-intersecting_images/imageFile34.png>)

- 2


+

:= L. Therefore, by the triangle inequality,

(n

|(K + λ1)α1β1| = |

≤ L · (

(n

)

)

k

k

|αi||βi|

(λi + K)αiβi| ≤ L ·

i=2

i=2

(n

(n

)

)

k

k

βi2)1/2 (3)

α2i )1/2 · (

i=2

i=2

![image 35](<2018-huang-two-extremal-problems-intersecting_images/imageFile35.png>)

Recall that 1/ nk is a unit eigenvector for the eigenvalue λ1. Note that |A| = 1A 2 = (n

) i=1 α2i . On the other hand |A| = 1,1A , therefore

k

![image 36](<2018-huang-two-extremal-problems-intersecting_images/imageFile36.png>)

n k

α1 = α21 + ··· + α2(

)

n k

We have a similar inequality for {βi}. Plugging both of them into the previous inequality (3), we have

K + λ1 L

K + λ1 L

α21 ·

β12 ≤ (

![image 37](<2018-huang-two-extremal-problems-intersecting_images/imageFile37.png>)

![image 38](<2018-huang-two-extremal-problems-intersecting_images/imageFile38.png>)

![image 39](<2018-huang-two-extremal-problems-intersecting_images/imageFile39.png>)

n k

α1 − α21)(

![image 40](<2018-huang-two-extremal-problems-intersecting_images/imageFile40.png>)

n k

β1 − β12)

Therefore either

![image 41](<2018-huang-two-extremal-problems-intersecting_images/imageFile41.png>)

n k

K + λ1 L

α1 − α21, or a similar inequality holds for β. Solving this inequality, we get

α21 ≤

![image 42](<2018-huang-two-extremal-problems-intersecting_images/imageFile42.png>)

|A| =

=

=

![image 43](<2018-huang-two-extremal-problems-intersecting_images/imageFile43.png>)

n k

α1 ≤

L K + L + λ1

n k ·

![image 44](<2018-huang-two-extremal-problems-intersecting_images/imageFile44.png>)

n−k−1 k−1 + n−k−k−22 n−k

- 1

![image 45](<2018-huang-two-extremal-problems-intersecting_images/imageFile45.png>)

- 2 ·


n k ·

![image 46](<2018-huang-two-extremal-problems-intersecting_images/imageFile46.png>)

k + n−k−k−11

n − 2 n − k − 1

n − 1 k − 1 ·

- 1

![image 47](<2018-huang-two-extremal-problems-intersecting_images/imageFile47.png>)

- 2


.

![image 48](<2018-huang-two-extremal-problems-intersecting_images/imageFile48.png>)

![image 49](<2018-huang-two-extremal-problems-intersecting_images/imageFile49.png>)

![image 50](<2018-huang-two-extremal-problems-intersecting_images/imageFile50.png>)

![image 51](<2018-huang-two-extremal-problems-intersecting_images/imageFile51.png>)

![image 52](<2018-huang-two-extremal-problems-intersecting_images/imageFile52.png>)

We do not know whether it is possible to further improve this upper bound, say for 2k+1 ≤

n ≤ 2k2. Observe that for example when n = 2k, Theorem 1.3 gives min{|A|,|B|} ≤ 2kk−−11 . This bound is best possible. This can be seen by pairing each k-set with its complement, and

partitioning the 2kk−−11 pairs into A and B as evenly as possible. However, even for n = 2k + 1 this bound does not seem to be sharp. It would be great if for every value of n, the maximum

of min{|A|,|B|} can be determined precisely.

# 2 Diversity of intersecting families

Given an intersecting family F of k-subsets of [n]. Its diversity, denoted by div(F), is deﬁned as the number of sets not passing through the most popular element. For example, the 1-star extremal construction in the Erdo˝s-Ko-Rado Theorem has diversity 0, since every set contains the center of the 1-star. The Hilton-Milner Theorem [7] is equivalent to ﬁnding the maximum size of an intersecting family with diversity at least 1. It is natural to ask the following question: given a family F of k-subset of [n], what is the maximum diversity it can possibly have? Let Fx = {F : x ∈ F ∈ F}, the goal is to maximize div(F) = |F| − maxx∈[n] |Fx|.

This question was ﬁrst suggested by Katona and addressed by Lemons and Palmer [11].

They showed that for n > 6k3, the diversity of F is at most nk−−23 , with the equality attained by the following family:

[n] k

F = F : F ∈

,|F ∩ [3]| ≥ 2 .

Recently, Frankl [4] proved that div(F) ≤ nk−−23 for n ≥ 6k2, and conjectured that the same holds for n > 3k. More recently, Kupavskii [9] veriﬁed Frankl’s conjecture for n > Ck, for some

large constant C. He also consider the intersecting families

Dr = {D : D ∈

[n] k

,|D ∩ [2r + 1]| ≥ r + 1}.

Here the “two out of three” family F is just D1. By computing the diversities of Dr for r = 1,··· ,k −1, it is not hard to show that Dr has the largest diversity among all D1,···Dk−1, for (k − 1)(2 + r1) + 1 ≤ n ≤ (k − 1)(2 + r−11) + 1. This observation prompts the following stronger conjecture in [9]:

![image 53](<2018-huang-two-extremal-problems-intersecting_images/imageFile53.png>)

![image 54](<2018-huang-two-extremal-problems-intersecting_images/imageFile54.png>)

Conjecture 2.1. Fix n ≥ 2k, and consider an intersecting family F ⊂ [nk] . If for some r ∈ Z≥0, we have (k − 1)(2 + r1) + 1 ≤ n ≤ (k − 1)(2 + r−11) + 1, then div(F) ≤ div(Dr).

![image 55](<2018-huang-two-extremal-problems-intersecting_images/imageFile55.png>)

![image 56](<2018-huang-two-extremal-problems-intersecting_images/imageFile56.png>)

Note that the r = 1 case corresponds to Frankl’s conjecture. Below we will present a construction showing that 3k is not the right threshold for Frankl’s conjecture, thus disproving both conjectures.

Let t be a positive integer, and H be an intersecting family of subsets of [t], which is not necessarily uniform. Let

[n] k

F = {F : F ∈

,F ∩ [t] ∈ H},

then F is also intersecting. Denote by Ni the number of i-sets in H, and Ni(x) the number of i-sets in H not containing the element x. It is not hard to see that for x ∈ [t],

t

n − t k − i

|F \ Fx| =

Ni(x)

,

i=1

and for x ∈ [n] \ [t],

t

n − t − 1 k − i

|F \ Fx| =

.

Ni

i=1

- Theorem 2.2. For k suﬃciently large and 3k < n < (2 + √3)k, there exists a family F such that


![image 57](<2018-huang-two-extremal-problems-intersecting_images/imageFile57.png>)

n − 3 k − 2

div(F) >

.

Proof. Let t = 6, and

G = {{1,2,3},{2,3,4},{3,4,5},{4,5,1},{5,1,2},{1,3,6},{2,4,6},{2,5,6},{3,5,6},{1,4,6}}. This family of 10 sets of size 3 is intersecting, every pair of elements appears exactly twice, and every element exactly 5 times. Deﬁne

H = {F : F ⊂ [t], there exists G ∈ G such that G ⊂ F}.

Now we can compute Ni and Ni(x) for H. We have N3 = 10, N4 = 15, N5 = 6, N6 = 1. And for each x ∈ [6], N3(x) = 5, N4(x) = 5, N5(x) = 1, N6(x) = 0. Therefore, when we assume k = αn for ﬁxed constant α, as n,k tends to inﬁnity, by Lemma 1.2, for x ∈ [6],

6 i=1 Ni(x) nk−−it

6

|F \ Fx| n k

Ni(x) · αi(1 − α)t−i.

→

=

![image 58](<2018-huang-two-extremal-problems-intersecting_images/imageFile58.png>)

![image 59](<2018-huang-two-extremal-problems-intersecting_images/imageFile59.png>)

n k

i=1

= 5α3(1 − α)3 + 5α4(1 − α)2 + α5(1 − α)

= 5α3 − 10α4 + 6α5 − α6 := f1(α). For x  ∈ [6],

6 i=1 Ni n−k−t−i1

6

|F \ Fx| n k

Niαi(1 − α)t+1−i

→

=

![image 60](<2018-huang-two-extremal-problems-intersecting_images/imageFile60.png>)

![image 61](<2018-huang-two-extremal-problems-intersecting_images/imageFile61.png>)

n k

i=1

= 10α3 − 25α4 + 21α5 − 6α6 := f2(α).

From Lemma 1.2, we also have that nk−−23 → nk · α2(1 − α). Solving f1(α) > α2(1 − α), we have α ∈ (2 −

√3,1). Solving f2(α) > α2(1 − α), we have α ∈ (9−

√57 12 ,1). Combining these two

![image 62](<2018-huang-two-extremal-problems-intersecting_images/imageFile62.png>)

![image 63](<2018-huang-two-extremal-problems-intersecting_images/imageFile63.png>)

![image 64](<2018-huang-two-extremal-problems-intersecting_images/imageFile64.png>)

√3,1), k = αn and n goes to inﬁnity, for every x,

![image 65](<2018-huang-two-extremal-problems-intersecting_images/imageFile65.png>)

ranges, we know that when α ∈ (2 −

n − 2 k − 3

|F \ Fx| >

,

thus the diversity of F is strictly greater than nk−−32 .

![image 66](<2018-huang-two-extremal-problems-intersecting_images/imageFile66.png>)

![image 67](<2018-huang-two-extremal-problems-intersecting_images/imageFile67.png>)

![image 68](<2018-huang-two-extremal-problems-intersecting_images/imageFile68.png>)

![image 69](<2018-huang-two-extremal-problems-intersecting_images/imageFile69.png>)

One can check that that the family H used in this construction is a maximum intersecting family of subsets of [6]. Moreover it also has the largest diversity. We believe that this property is the main reason that causes the resulting uniform family F to have large diversity. For Dr, the family playing the role of H consists of subsets of [2k + 1] of size at least k + 1. In order to completely settle the problem of determining the maximum diversity of a uniform intersecting family for every n, perhaps one should ﬁrst prove the non-uniform version of the diversity problem: given an integer n, what is the family F ⊂ 2[n] that has the maximum diversity? Motivated by the above discussions, the following conjecture seems natural. Let n = 2k + 1, and Qk = {A : A ⊂ [2k + 1],|A| ≥ k + 1}.

- Conjecture 2.3. For n = 2k + 1, suppose F ⊂ 2[n] is intersecting. Then

div(F) ≤ div(Qk) =

2k

i=k+1

2k i

.

When n = 2k, the situation could be slightly more complicated. Ideally the extremal family F should contain all the subsets of size at least k + 1, together with half of the k-sets. Note that in this case, F is intersecting if and only if Fk, its subfamily consisting of all the k-sets, is intersecting. So to maximize div(F), we need to look for Fk ⊂ [2kk] having the largest diversity. By the Erdo˝s-Ko-Rado theorem, |Fk| ≤ 2kk−−11 . And therefore

div(Fk) ≤ |Fk| − |Fk| ·

k 2k ≤

![image 70](<2018-huang-two-extremal-problems-intersecting_images/imageFile70.png>)

- 1

![image 71](<2018-huang-two-extremal-problems-intersecting_images/imageFile71.png>)

- 2


2k − 1 k − 1

. However this bound can only be attained when a regular k-uniform intersecting family of

subset of [2k] of size 2kk−−11 exists. Brace and Daykin [1] showed that this happens if and only if k is not a power of 2. When k is a power of 2, Ihringer and Kupavskii [8] showed that the

maximum size of such a regular family is 2kk−−11 −3. It is plausible that for even n = 2k, div(F) is always maximized by Fk ∪ ≥ [kn+1] , where Fk is a k-uniform family of size 2kk−−11 as regular as possible. This prompts the following conjecture for the even case.

- Conjecture 2.4. For n = 2k, suppose F ⊂ 2[n] is an intersecting family. If k is not a power of 2, then


2k − 1 k − 1

2k − 1 k + 1

2k − 1 2k − 1

- 1

![image 72](<2018-huang-two-extremal-problems-intersecting_images/imageFile72.png>)

- 2


div(F) ≤

+ ··· +

+

; and if k is a power of 2, then

2k − 1 k − 1 − 1 +

2k − 1 k + 1

2k − 1 2k − 1

- 1

![image 73](<2018-huang-two-extremal-problems-intersecting_images/imageFile73.png>)

- 2


div(F) ≤

+ ··· +

. The validity of Conjecture 2.3 and 2.4 has been checked using a computer for n ≤ 6.

Acknowledgment. The author would like to thank Peter Frankl and Andrey Kupavskii for their helpful comments and observation regarding the sharpness of Theorem 1.3, and bringing up the reference [8]; and Jie Han for his signiﬁcant contribution at the early stage of research.

# References

- [1] A. Brace and D. E. Daykin, Sperner-type theorems for ﬁnite sets. In: Combinatorics, D. R. Woodall and D. J. A. Welsh, eds, 18–37, Inst. Maths. Applics., Southend-on-Sea, 1972.
- [2] P. Erdo˝s, C. Ko and R. Rado, Intersection theorems for systems of ﬁnite sets, Quart. J. Math. Oxford Ser. (2) , 12 (1961), 313–318.
- [3] P. Frankl, The shifting techniques in extremal set theory, in: Surveys in Combinatorics, Lond. Math. Soc. Lect. Note Ser. 123 (1987), 81–110.
- [4] P. Frankl, Antichains of ﬁxed diameter, Moscow Journal of Combinatorics and Number Theory 7 (2017), N3.
- [5] P. Frankl and A. Kupavskii, private communication.
- [6] C. Godsil and G. Royle, Algebraic Graph Theory, New York: Springer-Verlag, 2001, vol. 207, Graduate Texts in Mathematics.
- [7] A. J. W. Hilton and E. C. Milner, Some intersection theorems for systems of ﬁnite sets, Quart. J. Math. Oxford Ser. 18 (2) (1967), 369–384.
- [8] F. Ihringer, A. Kupavskii, Regular intersecting families, preprint availble at https://arxiv.org/abs/1709.10462.
- [9] A. Kupavskii, Diversity of uniform intersecting families, to appear in European Journal of Combinatorics.
- [10] A. Kupavskii, Structure and properties of large intersecting families, preprint available at https://arxiv.org/abs/1710.02440.
- [11] N. Lemons, C. Palmer, Unbalance of set systems, Graphs and Combinatorics 24 (2008), N4, 361-365.
- [12] M. Matsumoto, N. Tokushige, The exact bound in the Erdo˝s-Ko-Rado Theorem for crossintersecting families, J. Combin. Theory Ser. A 52 (1989), 90–97.
- [13] L. Pyber, A new generalization of the Erdo˝s-Ko-Rado theorem, J. Combin. Theory Ser. A 43 (1986), 85–90.


