---
type: source
kind: paper
title: A non-uniform extension of Baranyai's Theorem
authors: Jinye He, Hao Huang, Jie Ma
year: 2022
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2207.00277v1
source_local: ../raw/2022-he-non-uniform-extension-baranyai-theorem.pdf
topic: general-knowledge
cites:
---

arXiv:2207.00277v1[math.CO]1Jul2022

A non-uniform extension of Baranyai’s Theorem

Jinye He ∗ Hao Huang † Jie Ma ‡

Abstract

A celebrated theorem of Baranyai states that when k divides n, the family Knk of all k-subsets of an n-element set can be partitioned into perfect matchings. In other words, Knk is 1-factorable. In this paper, we determine all n,k, such that the family Kn≤k consisting of subsets of [n] of size up to k is 1-factorable, and thus extend Baranyai’s Theorem to the non-uniform setting. In particular, our result implies that for ﬁxed k and suﬃciently large n, Kn≤k is 1-factorable if and only if n ≡ 0 or −1 (mod k).

# 1 Introduction

A hypergraph is a system of subsets of ﬁnite sets. Formally, a hypergraph H = (V,E) consists of a vertex set V , and an edge set E which is a family of non-empty subsets of V . A k-uniform hypergraph is a hypergraph such that all its edges are of size k. A ℓ-factor of a hypergraph H is a spanning sub-hypergraph H′ in which every vertex is contained in ℓ edges. We say that H has a ℓ-factorization if its edge set can be partitioned into ℓ-factors. A hypergraph H is said to be ℓ-factorable if it admits a ℓ-factorization. There have been extensive research on 1-factorization of graphs (see [1, 10, 11, 16, 17, 19, 21, 23, 24, 25, 26] and the resolution of the 1-factorization conjecture [13]).

We denote the complete k-uniform hypergraph on n vertices by Knk. Clearly, a necessary condition for Knk to be 1-factorable is k | n. It turns out that this is also suﬃcient for k = 2 (folklore) and k = 3 (proved by Peltesohn [22] in 1936). The suﬃciency for general k was eventually established by Baranyai [7] in 1975 as follows.

- Theorem 1.1 (Baranyai [7]). For any positive integers k,n such that k divides n, the complete k-uniform hypergraph Knk can be decomposed into nk n k = nk−−11 1-factors.


![image 1](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile1.png>)

![image 2](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile2.png>)

∗School of Mathematical Sciences, University of Science and Technology of China, Hefei, Anhui 230026, China. Email: zykxxxx@mail.ustc.edu.cn.

†Department of Mathematics, National University of Singapore. Research supported in part by a start-up grant at NUS and an MOE Academic Research Fund (AcRF) Tier 1 grant. Email: huanghao@nus.edu.sg.

‡School of Mathematical Sciences, University of Science and Technology of China, Hefei, Anhui 230026, China. Research supported in part by the National Key R and D Program of China 2020YFA0713100, National Natural Science Foundation of China grant 12125106, Innovation Program for Quantum Science and Technology 2021ZD0302904, and Anhui Initiative in Quantum Information Technologies grant AHY150200. Email: jiema@ustc.edu.cn.

His proof was based on an ingenious use of the Max-Flow Min-Cut Theorem. Generalizations and extensions of Baranyai’s Theorem can be found in [3, 4, 5, 6, 8, 9, 18].

In this paper, we mainly consider the non-uniform hypergraph Kn≤k, whose vertex set is [n] =

{1,··· ,n} and edge set consists of all the non-empty subsets of [n] of size up to k, denoted by [n] ≤k . We show that when k is ﬁxed and n is suﬃciently large, a necessary and suﬃcient condition

for such hypergraph to be 1-factorable is that n is congruent to 0 or −1 modulo k. Our result is actually much more precise.

- Theorem 1.2. For positive integers n,k such that k < n/2, Kn≤k is 1-factorable if and only if one of the two following conditions is met:

- (i) n ≡ 0 (mod k) and n ≥ k(k − 2),
- (ii) n ≡ −1 (mod k) and n ≥ k(⌈k2⌉ − 1) − 1. The k ≥ n/2 case can be reduced to the previous range by the following equivalence.


![image 3](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile3.png>)

- Theorem 1.3. For positive integers n,k such that n/2 ≤ k ≤ n − 1, Kn≤k is 1-factorable if and only if Kn≤n−k−1 is 1-factorable.


Theorems 1.2 and 1.3 together provide a complete characterization of all n,k such that Kn≤k has a 1-factorization.

The rest of this paper is organized as follows: in the next section, using the Max-Flow Min-Cut Theorem, we show that the 1-factorization problem is equivalent to ﬁnding non-negative integer solutions to a system of linear equations given by the partitions of [n] into parts of size up to k. Section 3 determines when this equivalent problem is feasible. Section 4 discusses an extension of

- Theorem 1.2 to other families of subsets obtained from taking the union of multiple levels of the hypercube. The last section contains some concluding remarks and open problems.


# 2 A reduction using network ﬂow

In this section, we reduce the 1-factorization problem of Kn≤k to ﬁnding non-negative integer solutions to a system of linear equations (as we should see soon, both problems in fact are equivalent). Throughout this section, let n,k be two ﬁxed positive integers with n ≥ k, and let L be a set consisting of k and some positive integers in {1,2,··· ,k −1}. We denote by [Ln] the family of subsets of [n] whose size is an element of L. We will prove a more general reduction for the 1-factorization of [Ln] which holds for any L (the case when L = [k] corresponds to our main results).

For given n,k and L, an (n,L)-type, or simply a type is a vector λ = (λ1,λ2,··· ,λk) in Zk≥0 such that j∈L j · λj = n and λj = 0 for every j ∈ [k]\L. If L = [k], then we also call it an (n,k)-type. Let | λ| = kj=1 λk. We say that A = {A1,A2,··· ,At} is a λ-partition of [n], if Ai’s are pairwise disjoint subsets of [n] such that ∪ti=1Ai = [n], and for every 1 ≤ j ≤ k, there are λj subsets Ai’s of size j.

For given n,k, we now deﬁne a matrix AL, which we will soon show to be closely related to the 1-factorization of [Ln] . Let AL be the matrix with k columns composed by all admissible

(n,L)-types λ as follows:

  

  

λ λ′

AL =

.

When L is clear from the context, we will simply write it for A. Below we give an example of AL. Example 2.1. For n = 7, k = 3 and L = [3], the matrix A is deﬁned as follows. For example, the third row corresponds to λ = (2,1,1) which is a (7,3)-type because 7 = (2,1,1) · (1,2,3)T .





- 1 0 2

- 0 2 1

2 1 1

- 4 0 1

1 3 0 3 2 0

- 5 1 0 7 0 0






AL =

 

 

For given n,k and L, suppose the hypergraph [Ln] can be decomposed into 1-factors A1,··· ,Am.1

Denote the number of Aj’s that are λ-partitions of [n] by x λ. Then the total number of i-subsets of [n] appeared in {A1,··· ,Am} is equal to the i-th coordinate of (AL)T x, where  x = (x λ) is a column vector indexed by all the (n,L)-types λ. Observe that [Ln] contains exactly ni subsets of size i for each i ∈ L. Thus by setting bL = (b1,··· ,bk)T with bi = ni for i ∈ L and bi = 0 for

- i ∈ [k]\L, we immediately have (AL)T x = bL. (1)


Therefore the system (1) having a non-negative integer solution (meaning that all x λ are nonnegative integers) is a necessary condition for [Ln] to be 1-factorable.

Our next theorem shows that this is indeed suﬃcient. We remark that for Baranyai’s Theorem (corresponding to n,k and L = {k} with k | n), a non-negative integer solution to the corresponding system exists trivially because the only type involved is (0,··· ,0,n/k) and nk | nk .

![image 4](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile4.png>)

- Theorem 2.2. Given positive integers n,k and a set L of positive integers with n ≥ k and k ∈ L ⊆


[k], the hypergraph [Ln] is 1-factorable if and only if the system of linear equations (1) associated with it has a non-negative integer solution.

We will imitate Baranyai’s ideas and construct a ﬂow network to prove Theorem 2.2. Here we give a brief review of the deﬁnition of ﬂow network and the statement of the Max-Flow Min-Cut Theorem of Ford and Fulkerson (1956), to facilitate our later discussion. A network is a ﬁnite digraph D = (V,E) together with two distinguished vertices called the source s and the sink t, and a capacity function κ : E(D) → R≥0 which associates a non-negative real number κ(a) to each arc a ∈ E(D). The source s must be the tail of every arc containing s, and the sink t must be the head of every arc containing t. We further assume that D does not contain any arc of the form

![image 5](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile5.png>)

1It is easy to see that we must have m = j∈L nj−−11 .

a = (v,v) for a vertex v ∈ V . A ﬂow on D is a function f : E(D) → R≥0 which assigns to each arc a ∈ E(D) a non-negative real number f(a) such that

- 1. (Capacity Constraint) 0 ≤ f(a) ≤ κ(a) for all arcs a ∈ E(D);
- 2. (Conservation of Flow) for each vertex v ∈ V \ {s,t}, we have


f(a) =

f(a).

a∈E(D): v is the head of a

a∈E(D): v is the tail of a

The value of the ﬂow f, denoted by |f|, is the sum of f(a) over all arcs a leaving s. A cut (S,T) is a partition of V (D) = S ∪ T such that s ∈ S and t ∈ T. The capacity of a cut (S,T), denoted by c(S,T), is the sum of the capacities of the arcs which has tail in S and head in T, that is

c(S,T) =

κ(xy).

xy∈E(D): x∈S, y∈T

- Theorem 2.3 (The Max-Flow Min-Cut Theorem). Given a ﬂow network D = (V,E), the maximum value of a ﬂow on D is equal to the minimum capacity over all cuts in D.

We will also utilize the Integral Flow Theorem by Dantzig and Fulkerson [14].

- Theorem 2.4 (The Integral Flow Theorem). If D = (V,E) is a network in which every arc has integral capacity, then there exists a maximum ﬂow f on D such that for each a ∈ E(D), f(a) is an integer.


Now we are ready to prove Theorem 2.2. In the coming proofs, for any integers a,b, the binomial coeﬃcient ab is interpreted as zero whenever a < 0, b < 0 or a < b. In particular, we have 0b = 1 if b = 0 and 0b = 0 otherwise. In this way, ab = ab−−11 + a−b1 holds for any integers a,b.

Proof of Theorem 2.2: Throughout this proof, n,k and L are ﬁxed. From our previous discussions, it suﬃces to show that if the system (1) has a non-negative integer solution  x = (x λ) where λ is over all (n,L)-types, then [Ln] is 1-factorable.

For a given (n,L)-type λ, we slightly extend the deﬁnition of a λ-partition of [n] to partitions of [ℓ] for any 0 ≤ ℓ ≤ n. A partition A = {A1,A2,... ,At} of [ℓ] with t = | λ| is called a λ-partition of [ℓ], if for every j ∈ L, we assign the label, which we call potential value, j to exactly λj subsets Ai. We point out here that repetitions are allowed only for empty sets. Let

M =

j∈L

n − 1 j − 1

.

We will prove the following statement by induction on ℓ: for any 0 ≤ ℓ ≤ n, there exists a collection of A1,A2,... ,AM of partitions of [ℓ] such that all of the following hold:

- (1) each set S appeared in each partition is associated with a potential value j ∈ L with j ≥ |S|,
- (2) for each (n,L)-type λ, there are exactly x λ partitions Ai that are λ-partitions, and


- (3) for each S ⊆ [ℓ] and each j ∈ L with j ≥ |S|, S occurs j n−|−Sℓ| times with potential value j as subsets in the partitions A1,··· ,AM.


Observe that when ℓ = n, the third property ensures that every set S in [Ln] appears exactly once (only with potential value j = |S|), which would provide a 1-factorization of [Ln] . It would be helpful to view this inductive proof as an evolution where each set (say with potential value j) in the partitions grows from an empty set to a set of size j gradually.

Now we start the proof. For the base case when ℓ = 0, the existence of {A1,··· ,AM} is given by the non-negative integer solution  x of the system (1). This is because for each (n,L)-type λ we could construct x λ partitions formed by taking | λ| empty sets, and assigning a potential value

- j ∈ L to λj of them. Note that the total number of partitions is indeed


λ

(1,2,··· ,k) · (AL)T x n

=

x λ =

![image 6](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile6.png>)

(1,2,··· ,k) · bL n

= M.

![image 7](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile7.png>)

Now for the inductive step, assume that the statement holds for some 0 ≤ ℓ ≤ n − 1. We construct the following network.

.

- S(j)
- S(k)


- A1
- A2


.

. s t Ai

.

.

AM

Let s be the source and t be the sink. Each partition Ai deﬁnes a vertex and we add an arc from the source s to each Ai. For each subset S ⊆ [ℓ], in the network we create vertices S(j) for all j ∈ L with j ≥ |S|, where S(j) stands for the set S with potential value j. We add an arc from each S(j) to the sink t. If S occurs as a subset with potential value j in the partition Ai, then we add to the network an arc from Ai to S(j). Next we deﬁne the capacity function κ as follows:

n − ℓ − 1 j − 1 − |S|

κ(s,Ai) = 1, κ(Ai,S(j)) = +∞, and κ(S(j),t) =

. Then we deﬁne a ﬂow f on this network as follows:

j − |S| n − ℓ

, and f(S(j),t) =

f(s,Ai) = 1, f(Ai,S(j)) =

![image 8](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile8.png>)

n − ℓ − 1 j − 1 − |S|

.

Let us check that f is indeed a ﬂow. It is easy to check that 0 ≤ f(a) ≤ κ(a) for every arc a in this network. To see that f satisﬁes the conservation of ﬂow, we consider the vertices Ai and S(j) separately:

- 1. For each λ-partition Ai of [ℓ] with λ = (λ1,λ2,... ,λk), the total value of ﬂow leaving Ai is

S∈Ai

j − |S| n − ℓ

![image 9](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile9.png>)

=

n j∈L j · λj −

S∈Ai

|S| n − ℓ

![image 10](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile10.png>)

=

n − ℓ n − ℓ

![image 11](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile11.png>)

= 1 = f(s,Ai);

- 2. For each S(j), by the inductive hypothesis, it appears in the partitions {A1,··· ,AM} for exactly j n−|−Sℓ| times. So we have the total value of ﬂow entering S(j) is

n − ℓ j − |S|

·

j − |S| n − ℓ

![image 12](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile12.png>)

=

n − ℓ − 1 j − 1 − |S|

= f(S(j),t).

Since f(a) = κ(a) for all the edges a leaving the source s, the so-deﬁned f must be a maximum ﬂow. By Theorem 2.4, there is an integral ﬂow f∗ of the same maximum value. Therefore for each Ai, we have f∗(s,Ai) = 1, and consequently, there is a unique arc Ai → S(j) with f∗(Ai,S(j)) = 1. As for each vertex S(j), we have f∗(S(j),t) = j n−−1ℓ−|−S1| , and by the conservation of ﬂow, there are exactly

n−ℓ−1

j−1−|S| arcs a directed to S(j) with f∗(a) = 1. Let us pay some attention to vertices S(j) with j = |S| that as f∗(S(j),t) = j n−−1ℓ−|−S1| = 0, each arc a directed to S(j) must have f∗(a) = 0, hence it is impossible for any of the vertices Ai to have the unique arc Ai → S(j) with f∗(Ai,S(j)) = 1.

Finally, we use f∗ to construct a desired collection A1′,A2′,... ,AM′ of partitions of [ℓ + 1]. As mentioned above, every Ai has a unique S(j) such that f∗(Ai,S(j))) = 1, where j > |S| by the above discussion. Let S′ = S ∪ {ℓ + 1}, and update Ai by replacing S with S′ and assigning to S′ the same potential value j. Note that we have j ≥ |S′|. By deﬁnition, the new partition Ai′ is still a λ-partition of [ℓ + 1]. So the ﬁrst and second properties for the new partitions A1′,··· ,AM′ are satisﬁed. Since there are j n−−1ℓ−|−S1| many arcs directed to S(j), the new set S′ = S ∪ {ℓ + 1} with potential value j (i.e. S′(j)) is contained in exactly j n−−1ℓ−|−S1| = nj−−|(ℓS+1)′| new partitions Ai’. For those S ⊂ [ℓ + 1] not containing the element ℓ, by induction they occur

n − ℓ j − |S|

−

n − ℓ − 1 j − 1 − |S|

=

n − (ℓ + 1) j − |S|

times with potential value j in the new partitions A1′,··· ,AM′ . This proves the third property for the new partitions A1′,··· ,AM′ . Hence the statement holds for ℓ+1 and the proof is completed.

![image 13](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile13.png>)

![image 14](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile14.png>)

![image 15](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile15.png>)

![image 16](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile16.png>)

- 3 Finding non-negative integer solutions


After establishing Theorem 2.2, to prove Theorem 1.2, it remains to determine for which n,k, the system (for L = [k]) of linear equations (1) has a non-negative integer solution. For convenience, in this section the system (1) without speciﬁed L (or A and b without subscripts) always means the case L = [k]. In the next two subsections we discuss the necessary and suﬃcient conditions respectively, and we prove Theorems 1.2 and 1.3 in the last subsection.

## 3.1 Necessary condition

The following lemma shows that it is necessary for n to come from certain congruence classes modulo k.

- Lemma 3.1. For any n,k satisfying 2 ≤ k < n2, if n  ≡ 0,−1 (mod k), then the system (1) does not have a non-negative real solution.

![image 17](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile17.png>)

It turns out that unlike Baranyai’s Theorem, the congruence condition in Lemma 3.1 alone is not enough to guarantee a 1-factorization. For example, one could show that K18≤6 is not 1-factorable even though 18 ≡ 0 (mod 6). More generally, if n is not very large compared to k, even if it is from those congruence classes, it is still possible that the system (1) does not have a non-negative integer solution. In these cases, there are not even non-negative real solutions.

- Lemma 3.2. For every positive integer k ≥ 2,

- (i) Suppose n = j · k + k, where j is a non-negative integer. If 2 ≤ j ≤ k − 4, then the system (1) has no non-negative solution.
- (ii) Suppose n = j ·k +k −1, where j is a non-negative integer. If 2 ≤ j ≤ ⌈k2⌉−3, then the system


![image 18](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile18.png>)

(1) has no non-negative solution.

The proofs of Lemma 3.1 and 3.2 use Farkas’ Lemma. In order to show that AT x = b has no non-negative real solution, we will construct a hyperplane separating the convex cone formed by the column vectors of the matrix AT and the vector b. Here we say a vector  x ≥ 0 if each of its coordinates is non-negative.

- Lemma 3.3 (Farkas [15]). Let P ∈ Rm×n and b ∈ Rn. Then exactly one of the following two assertions is true:


- 1. There exists a vector  x ∈ Rm such that PT x = b and  x ≥ 0.
- 2. There exists a vector  y ∈ Rn such that P y ≥ 0 and bT y < 0. Below we give proofs to both Lemmas 3.1 and 3.2.


- Proof of Lemma 3.1: Let n = j ·k +r, 0 < r < k −1. We ﬁrst consider the case when j ≥ 3. Let


j 2

j 2

 yT = (

,··· ,

![image 19](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile19.png>)

![image 20](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile20.png>)

![image 21](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile21.png>)

![image 22](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile22.png>)

r−1

j − 1 2

j − 1 2

,−1).

,··· ,

,j,

![image 23](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile23.png>)

![image 24](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile24.png>)

![image 25](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile25.png>)

![image 26](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile26.png>)

k−r−1

By Lemma 3.3 we just need to prove A y ≥ 0 and bT y < 0.

Take an arbitrary row vector of A. By deﬁnition we know that it is of the form λ = (λ1,··· ,λk) such that ki=1 i · λi = n and all λi’s are non-negative integers. Since n = jk + r, we have λk ≤ j. Suppose λk = j, then i k=1−1 i · λi = n − kj = r > 0 and thus for some index 1 ≤ s ≤ r, λs must be strictly positive. Either we have at least two such λs to be positive, or λr = 1. In either case,

r i=1 λiyi ≥ j. This already gives

k

λiyi ≥

i=1

r

λiyi + λkyk ≥ j − j = 0.

i=1

Now we may assume that λk ≤ j−1. Similar as before, if at least two of λ1,··· λr−1, or λr itself is

strictly positive, then ki=1 λiyi is non-negative. Otherwise suppose λr = 0 and λ1+···+λr−1 ≤ 1, then

i · λi = n − kλk ≥ jk + r − (j − 1)k = k + r.

i =r,1≤i≤k−1

Since

i · λi ≤ (k − 1)

λi.

i =r,1≤i≤k−1

i =r,1≤i≤k−1

We immediately have i =r,1≤i≤k−1 λi ≥ 2. Therefore we also have

·   i =r,1≤i≤k−1

λi

k

j − 1 2

λiyi ≥

 − λk ≥ (j − 1) − (j − 1) = 0.

![image 27](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile27.png>)

i=1

Next we prove  yT b < 0. Recall that bi = ni . So it suﬃces to verify that for 1 ≤ r ≤ k − 2 and n = jk + r with j ≥ 3,

Note that

n k − i + 1

r−1

j 2

![image 28](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile28.png>)

i=1

n i

+ j

n r

k−1

j − 1 2

+

![image 29](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile29.png>)

i=r+1

n i

<

n k

. (2)

j − 1 2

=

![image 30](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile30.png>)

n k − i

j − 1 2

+

![image 31](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile31.png>)

n k − i

r + 1 + j(i − 1) k − (i − 1)

+

![image 32](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile32.png>)

n k − i

.

By substituting one of the k n−i by the above identity for i + 1 and repeat this process, we obtain

n k

k−1

=

i=1

j − 1 2

![image 33](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile33.png>)

i n k − i

+

j − 1 2

![image 34](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile34.png>)

k−1 n 1

k−1

+

i=1

j − 1 2

![image 35](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile35.png>)

i−1 r + 1 + j(i − 1) k − (i − 1)

![image 36](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile36.png>)

n k − i

. (3)

We compare the coeﬃcients of k n−i in this expression with the left hand side of (2). Note that 1 ≤ r ≤ k − 2, we discuss the following cases according to the value of j.

- 1. For j ≥ 6, using that for i ≥ k − r ≥ 2, (j−21)i ≥ (j−21)2 > j,

![image 37](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile37.png>)

![image 38](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile38.png>)

n k

>

k−1

i=1

j − 1 2

![image 39](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile39.png>)

i n k − i

>

k−r−1

i=1

j − 1 2

![image 40](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile40.png>)

n k − i

+

k−1

i=k−r

- j

n

- k − i


.

- 2. For j = 5, note that (j−21)3 − j > 0, we could establish the same inequality when r ≤ k − 3. It suﬃces to check the case r = k − 2 and compare the coeﬃcients of k− n2 . Here we also involve the last sum on the right hand side of (3). Note that in (3) the coeﬃcients of k− n2 add up to be 22 + 2 · k−2+1+5(2k−(2−1)−1) > 5 = j. It completes the proof of the j = 5 case.


![image 41](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile41.png>)

![image 42](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile42.png>)

- 3. For j = 4, since (j−21)4 −j > 0, like in Case 2, it suﬃces to check the cases r = k −2 and r = k−3. For r = k−3, the coeﬃcient of k− n3 from (3) is (j−21)3+(j−21)2· (k−3)+1+k−(3−j1)(3−1), which is greater than j. For r = k−2, the coeﬃcient of k− n3 from (3) is (j−21)3+(j−21)2·(k−2)+1+k−(3−j1)(3−1), greater than j. The coeﬃcient of k− n2 from (3) is (j−21)2 + (j−21) · (k−2)+1+k−(2−j1)(2−1), combined with the surplus term (k−k2)+1 · k− n1 ≥ (k−k2)+1 · k− n2 , which is not hard to check that 9 4 + 23 · kk+3−1 + k−k1 is greater than j = 4 for all k.

![image 43](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile43.png>)

![image 44](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile44.png>)

![image 45](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile45.png>)

![image 46](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile46.png>)

![image 47](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile47.png>)

![image 48](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile48.png>)

![image 49](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile49.png>)

![image 50](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile50.png>)

![image 51](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile51.png>)

![image 52](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile52.png>)

![image 53](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile53.png>)

![image 54](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile54.png>)

![image 55](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile55.png>)

![image 56](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile56.png>)

![image 57](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile57.png>)

![image 58](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile58.png>)

- 4. When j = 3, we compare the identity (3) with inequality (2), note that what we need to prove is


k−1

k−1

r + 1 + 3(i − 1) k − (i − 1)

n 1

n k − i

n k − i

n r

- 1

![image 59](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile59.png>)

- 2


+

> 2

. (4)

+

![image 60](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile60.png>)

i=1

i=k−r+1

Note that k n−i / k− ni−1 = (n−k +i+1)/(k −i) > 2, therefore the right hand side is at most 2 nr + r− n1 , while the left hand side is at least

r + 1 k

![image 61](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile61.png>)

n k − 1

r + 4 k − 1

+

![image 62](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile62.png>)

n k − 2

r + 7 k − 2

+

![image 63](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile63.png>)

n k − 3

.

Note that n

n − k + 2 r + 1

(n − k + 2)··· (n − r) (r + 1)··· (k − 1)

k r + 1

k−1 n r

≥

≥

.

=

![image 64](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile64.png>)

![image 65](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile65.png>)

![image 66](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile66.png>)

![image 67](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile67.png>)

For r = k − 2, kr+4−1 k− n2 = kk−+21 k− n2 > k− n2 , and for r ≤ k − 3,

![image 68](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile68.png>)

![image 69](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile69.png>)

n k−2 n r

=

![image 70](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile70.png>)

(n − k + 3)··· (n − r) (r + 1)··· (k − 2)

≥

![image 71](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile71.png>)

n − k + 3 r + 1

≥

![image 72](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile72.png>)

k − 1 r + 4

.

![image 73](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile73.png>)

Finally, when r = k − 2, kr+7−2 k− n3 = kk+5−2 k− n3 > k− n3 , and for r ≤ k − 3,

![image 74](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile74.png>)

![image 75](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile75.png>)

n k−3 n r−1

=

![image 76](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile76.png>)

(n − k + 4)··· (n − r + 1) r ··· (k − 3)

≥

![image 77](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile77.png>)

n − k + 4 r

≥

![image 78](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile78.png>)

k − 2 r + 7

.

![image 79](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile79.png>)

These three inequalities immediately imply inequality (4).

For j = 2, we will use a diﬀerent hyperplane when applying Farkas’ Lemma. Now we have n = 2k + r, 1 ≤ r ≤ k − 2. We deﬁne  y as follows. We always take y1 = ··· = yr−1 = 1, yr = 2, and yk = −1. For r  ≡ k (mod 2), we take yr+1 = ··· = y⌊(r+k)/2⌋ = 1, and for r ≡ k (mod 2), we take we take yr+1 = ··· = y⌊(r+k)/2⌋−1 = 1, y⌊(r+k)/2⌋ = 1/2. The remaining yi’s are set to be 0.

First we prove ki=1 λiyi ≥ 0. This is obviously true if λk = 0. Suppose λk = 2, then k−1 i=1 iλi = r. In this case we either have i r=1−1 λi ≥ 2 or λr = 1, both implying ki=1 λiyi ≥ 0. The remaining case is λk = 1 and we have i k=1−1 iλi = k + r. If there exists i ≤ r with λi ≥ 1 then we are already done. Now suppose λ1 = ··· = λr = 0, we have i k=−r1+1 iλi = k + r. Either (in the case when k and r have the same parity) we have λ(k+r)/2 = 2, or there exists some i < (k + r)/2 such that λi = 1. By our choice of  y, it is not hard to see that once again ki=1 λiyi ≥ 0.

Finally let us prove that  yT b < 0. For r ≡ k (mod 2), 1 ≤ r ≤ k − 2 and n = 2k + r, we need to show 

  +

(k+r)/2−1

n i

n (k + r)/2

- 1

![image 80](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile80.png>)

- 2


n r

n k

+

<

(5)



i=1

For i ≤ (k + r)/2 we have

n i − 1

/

n i

i n − i + 1

≤

=

![image 81](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile81.png>)

(k + r)/2 (3k + r)/2 + 1

≤

![image 82](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile82.png>)

k − 1 2k

.

![image 83](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile83.png>)

Also nr ≤ (k+r n)/2−1 , thus the left hand side of (5) is at most

2

k − 1 2k

k − 1 2k

k − 1 2k

n (k + r)/2 <

n (k + r)/2

n (k + r)/2

- 1

![image 84](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile84.png>)

- 2


+ ···

+

+

+

![image 85](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile85.png>)

![image 86](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile86.png>)

![image 87](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile87.png>)

4k2 − k − 1 2k2 + 2k

2k − 1 2k

k − 1 k + 1

n (k + r)/2

n (k + r)/2

n (k + r)/2

n k

≤

+

=

.

![image 88](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile88.png>)

![image 89](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile89.png>)

![image 90](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile90.png>)

The last inequality follows from

n k

/

n (k + r)/2

(n − k + 1)··· (n − (k + r)/2) (k+2r + 1)··· k

=

![image 91](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile91.png>)

![image 92](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile92.png>)

3k + (k − 2) k + (k − 2) + 2

3k + r k + r + 2

≥

=

=

![image 93](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile93.png>)

![image 94](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile94.png>)

n − (k + r)/2 (k + r)/2 + 1

≥

![image 95](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile95.png>)

2k − 1 k

.

![image 96](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile96.png>)

For the case r  ≡ k (mod 2), in this case we have r ≤ k − 3, we need to show

For i ≤ (k + r + 1)/2,

n r

(k+r−1)/2

+

i=1

n i

<

n k

n i − 1

/

n i

i n − i + 1

≤

=

![image 97](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile97.png>)

k + r + 1 3k + r + 1

≤

![image 98](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile98.png>)

k + (k − 3) + 1 3k + (k − 3) + 1

=

![image 99](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile99.png>)

k − 1 2k − 1

.

![image 100](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile100.png>)

Also nr ≤ (k+r n−1)/2 ≤ 2kk−−11 (k+r n+1)/2 . So the left hand side of (6) is at most

![image 101](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile101.png>)

k − 1 2k − 1

+

![image 102](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile102.png>)

k − 1 2k − 1

![image 103](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile103.png>)

2

+ ···

n (k + r + 1)/2

+

n r

k − 1 k

<

![image 104](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile104.png>)

n (k + r + 1)/2

k − 1 2k − 1

+

![image 105](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile105.png>)

n (k + r + 1)/2

<

n k

.

The last inequality follows from

n k

/

n (k + r + 1)/2

(n − k + 1)··· (n − (k + r + 1)/2) (k + r + 3)/2··· k

≥

=

![image 106](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile106.png>)

3k + (k − 3) − 1 k + (k − 3) + 3

3k + r − 1 k + r + 3

≥

=

=

![image 107](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile107.png>)

![image 108](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile108.png>)

n − (k + r + 1)/2 (k + r + 3)/2

![image 109](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile109.png>)

2k − 2 k

k − 1 k

k − 1 2k − 1

>

+

.

![image 110](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile110.png>)

![image 111](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile111.png>)

![image 112](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile112.png>)

(6)

- Proof of Lemma 3.2: (i) We ﬁrst consider the case n = jk + k, 1 ≤ j ≤ k − 4. Let


 yT = (j + 1,... ,j + 1

,−1,0).

,j/2,... ,j/2

![image 113](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile113.png>)

![image 114](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile114.png>)

![image 115](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile115.png>)

![image 116](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile116.png>)

j+1

k−j−3

![image 117](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile117.png>)

![image 118](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile118.png>)

![image 119](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile119.png>)

![image 120](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile120.png>)

Then once again from Farkas’ Lemma, we just need to verify A y ≥ 0 and bT y < 0. For each row vector λ = (λ1,··· ,λk) of A, we know ki=1 iλi = n. Since n = jk + k =

(j + 1)(k − 1) + j + 1 and 1 ≤ j ≤ k − 4, we know that λk + λk−1 ≤ j + 1 and λk + λk−1 ≤ j if k−2 i=j+2 λi > 0. We discuss these two cases separately:

- 1. When i k=−j2+2 λi = 0. If we also have ji=1+1 λi = 0, then λ = (0,... ,0,j + 1) and trivially λy  ≥ 0. Now suppose ji=1+1 λi ≥ 1, this case is also trivial since λk + λk−1 ≤ j + 1.
- 2. When i k=−j2+2 λi > 0. If i k=−j2+2 λi ≥ 2, observe that λk + λk−1 ≤ j and we also have


λy  ≥ 2 · (j/2) − j ≥ 0. Thus we just need to consider the case i k=−j2+2 λi = 1. If ji=1+1 λi = 0 then (k−1)λk−1+kλk ∈ {(jk+2,(j+1)k−(j+2)}, which implies that λk−1 ∈ {j+2,··· ,k−2}, contradicting λk + λk−1 ≤ j. Therefore ji=1+1 λi ≥ 1, and this implies λ y ≥ (j + 1) − j > 0.

To apply Farkas’ Lemma, we will also need to show that bT y < 0. We know bi = ni in the system (1). First of all, similar as before,

n k − i + 1

j 2

=

![image 121](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile121.png>)

n k − i

j 2

+

![image 122](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile122.png>)

n k − i

1 + (j + 1)(i − 1) k − (i − 1)

+

![image 123](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile123.png>)

n k − i

.

Thus by repeatedly applying this identity, we have

n k − 1

k−1

=

i=2

j 2

![image 124](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile124.png>)

i−1 n k − i

What we need to prove is

+

j 2

![image 125](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile125.png>)

k−2 n 1

k−1

+

i=2

j 2

![image 126](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile126.png>)

i−21 + (j + 1)(i − 1) k − (i − 1)

![image 127](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile127.png>)

n k − i

. (7)

n k − 1

k−1

j 2

>

![image 128](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile128.png>)

i=2

n k − i

k−1

j + 2 2

+

![image 129](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile129.png>)

i=k−j−1

n k − i

. (8)

Notice that j + 1 ≤ k − 3 since 2 ≤ j ≤ k − 4, we divide our discussion into several cases based on the value of j.

- 1. For j ≥ 5, we have 2 j


![image 130](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile130.png>)

2

− j − 1 > 0 and thus

n k − 1

k−1

=

i=2

k−1

>

i=2

j 2

![image 131](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile131.png>)

i−1 n k − i

j 2

![image 132](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile132.png>)

i−1 n k − i

+

j 2

![image 133](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile133.png>)

k−2 n 1

k−1

j 2

>

![image 134](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile134.png>)

i=2

n k − i

k−1

i−21 + (j + 1)(i − 1) k − (i − 1)

j 2

+

![image 135](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile135.png>)

![image 136](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile136.png>)

i=2

k−1

n k − i

j + 2 2

+

.

![image 137](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile137.png>)

i=k−j−1

n k − i

- 2. For j = 4, we have 2 j

![image 138](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile138.png>)

3

−j−1 > 0. It is easy to verify the inequality (8) for j+1 ≤ k−4. So it remains to check the case when j+1 = k−3 (i.e. k = j+4 = 8 and n = jk+k = 40). We have y T = (5,5,5,5,5,2,−1,0) and bT = 408 ,... , 401 when k = j +4 = 8 and n = jk +k = 40. We have bTy  < 0 by calculation.

- 3. For j = 3, note that 2 j

![image 139](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile139.png>)

4

− j − 1 > 0, it is easy to check that the inequality (8) when j +1 ≤ k −5. So we just need to check the case that j +1 = k −3 and j +1 = k −4. We have y T = (4,4,4,4,1.5,−1,0) and bT = 287 ,... , 281 when k = j + 4 = 7 and n = jk + k = 28. We have bTy  < 0 by calculation. Similarly, we have  yT = (4,4,4,4,1.5,1.5, −1,0) and bT = 328 ,... , 321 when k = j + 5 = 8 and n = jk + k = 32. Both cases have bTy  < 0 by calculation.

- 4. For j = 2, we compare the identity (7) with the inequality (8), after canceling some terms, what we need to prove is


n 1

k−1

1 + 3(i − 1) k − (i − 1)

+

![image 140](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile140.png>)

i=2

n k − i

> 2

n 3

+

n 2

+

n 1

. (9)

Note that 1+3(k−(ii−−1)1) is increasing in i. Furthermore setting i = k − 3, we have 1+3(k−(ii−−1)1) = 1+3(k−3−1)

![image 141](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile141.png>)

![image 142](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile142.png>)

k−(k−3−1) = 3k−411. If 3k−411 ≥ 2, i.e. k ≥ 7, we have proved the inequality (9). Since j ≤ k − 4, we also have k ≥ 6. Thus we just need to check the case that j = 2 and k = 6. We have  yT = (3,3,3,1,−1,0) and bT = 186 ,... , 181 . It is easy to check that bT y < 0 by calculation.

![image 143](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile143.png>)

![image 144](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile144.png>)

![image 145](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile145.png>)

(ii) Next we consider the case n = j · k + k − 1, 1 ≤ j ≤ ⌈k2⌉ − 3. Let y T = (j + 1,... ,j + 1

![image 146](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile146.png>)

,−1,j,−1).

,j/2,... ,j/2

![image 147](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile147.png>)

![image 148](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile148.png>)

![image 149](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile149.png>)

![image 150](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile150.png>)

2j+1

k−2j−4

Then we just need to prove A y ≥ 0 and bT y < 0. We start by checking A y ≥ 0. For each row vector λ = (λ1,··· ,λk) of A, by deﬁnition we have ki=1 iλi = n. Since n =

- j · k + k − 1 = (j + 1) · (k − 2) + 2j + 1 and 1 ≤ j ≤ ⌈k2⌉ − 3, we have λk + λk−2 ≤ j + 1 and λk + λk−2 ≤ j if ( i k=2−3j+2 λi) + λk−1 > 0. Then we consider the following two cases:


![image 151](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile151.png>)

- 1. When i k=2−3j+2 λi = 0. If 2i=1j+1 λi = 0, note that the equation (k−2)λk−2 +kλk = jk+k−1 has no non-negative integer solution. Therefore the only possibility is λ = (0,... ,0

![image 152](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile152.png>)

![image 153](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile153.png>)

k−2

,1,j),

which gives λ y ≥ 0 trivially. The case i 2=1j+1 λi ≥ 1 is also trivial since λk + λk−2 ≤ j + 1.

- 2. Now suppose i k=2−3j+2 λi > 0. If i k=2−3j+2 λi ≥ 2, then λk + λk−2 ≤ j, and thus λ y ≥ 0. So we just need to consider the case i k=2−3j+2 λi = 1. To prove λy  ≥ 0, we just need to show


( 2i=1j+1 λi) + λk−1 ≥ 1. This is true since the inequality n − (k − 3) ≤ (k − 2)λk−2 + kλk ≤ n − (2j + 2) has no non-negative integers solution for 1 ≤ j ≤ ⌈k/2⌉ − 3.

Next we will prove that bT y < 0. Recall that bi = ni in the system (1). It is easy to check that

n k − i + 1

j 2

=

![image 154](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile154.png>)

n k − i

j 2

+

![image 155](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile155.png>)

n k − i

(j + 1)(i − 1) k − (i − 1)

+

![image 156](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile156.png>)

n k − i

.

Thus we have

n k − 2

k−1

=

i=3

j 2

![image 157](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile157.png>)

i−2 n k − i

+

j 2

![image 158](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile158.png>)

k−3 n 1

k−1

+

i=3

j 2

![image 159](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile159.png>)

i−3(j + 1)(i − 1) k − (i − 1)

![image 160](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile160.png>)

n k − i

. (10)

Observe that nk = j k− n1 when n = jk + (k − 1), so what we need to prove is

n k − 2

k−1

j 2

>

![image 161](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile161.png>)

i=3

n k − i

k−1

j + 2 2

+

![image 162](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile162.png>)

i=k−2j−1

n k − i

. (11)

Note that 2j + 1 ≤ k − 4 since 2 ≤ j ≤ ⌈k2⌉ − 3, we discuss the following cases according to the value of j.

![image 163](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile163.png>)

- 1. For j ≥ 5, we have 2 j

![image 164](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile164.png>)

2

− j − 1 > 0, therefore

n k − 2

=

k−1

i=3

j 2

![image 165](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile165.png>)

i−2 n k − i

+

j 2

![image 166](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile166.png>)

k−3 n 1

+

k−1

i=3

j 2

![image 167](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile167.png>)

i−3(j + 1)(i − 1) k − (i − 1)

![image 168](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile168.png>)

n k − i

>

k−1

i=3

j 2

![image 169](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile169.png>)

i−2 n k − i

>

k−1

i=3

j 2

![image 170](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile170.png>)

n k − i

+

k−1

i=k−2j−1

j + 2 2

![image 171](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile171.png>)

n k − i

.

- 2. For j = 4, we have 2 j

![image 172](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile172.png>)

3

−j −1 > 0, it is easy to check that the inequality (11) similarly with Case 1 when 2j +1 ≤ k−5. So we just need to check the case that 2j +1 = k−4, which gives k = 2j + 5 = 13 and n = jk + k − 1 = 64. We have  yT = (5,5,5,5,5,5,5,5,5,2,−1, 4,−1) and bT = 6413 ,... , 641 . By calculation bTy  < 0.

- 3. For j = 3, we have 2 j

![image 173](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile173.png>)

4

−j −1 > 0. it is easy to check that the inequality (11) similarly with case 1 when 2j +1 ≤ k−6. So we just need to check the case that 2j +1 = k−4 and 2j +1 = k − 5. We have  yT = (4,4,4,4,4,4,4, 1.5,−1, 3, −1) and bT = 4311 ,... , 431 when k = 2j+5 = 11 and n = jk+k−1 = 43. Similarly, we have y T = (4,4,4,4,4,4,4,1.5,1.5,−1, 3,−1) and bT = 4712 ,... , 471 when k = 2j + 6 = 12 and n = jk + k − 1 = 47. In both cases, calculations give bT y < 0.

- 4. For j = 2, we compare the identity (10) with the inequality (11) and note that it suﬃces to prove


5

k−1

3(i − 1) k − (i − 1)

n k − i

n i

n 1

> 2

. (12)

+

![image 174](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile174.png>)

i=1

i=3

Note that k3(−i(−i−1)1) is monotone increasing in i. So we could focus our attention on the coeﬃcient of the term n5 . Note that when i = k − 5, k3(−i(−i−1)1) = 3k−618. If 3k−618 ≥ 2, i.e. k ≥ 10, the inequality (12) is obviously true. Since j ≤ ⌈k2⌉ − 3, we also have k ≥ 9. Thus it remains to check the case that j = 2 and k = 9. We have  yT = (3,3,3,3,3,1,−1,2, −1) and bT = 269 ,... , 261 . It is easy to verify bT y < 0 by calculation.

![image 175](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile175.png>)

![image 176](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile176.png>)

![image 177](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile177.png>)

![image 178](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile178.png>)

![image 179](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile179.png>)

![image 180](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile180.png>)

![image 181](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile181.png>)

![image 182](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile182.png>)

![image 183](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile183.png>)

## 3.2 Suﬃcient condition

In the previous subsection, we have found necessary conditions for the system (1) to have a nonnegative integer solution. The following two lemmas below show that these necessary conditions are indeed suﬃcient.

- Lemma 3.4. Suppose n > 2k and n = j · k + k, where j is a non-negative integer such that


- j ≥ k − 3, then the system (1) has a non-negative integer solution.


Proof. Suppose n = jk + k and j ≥ k − 3. So n is at least k2 − 2k and divisible by k. Below we construct an explicit non-negative integer solution to the system (1). First we consider the case when n ≥ k2 − k. For each i ∈ {1,··· ,k − 1}, we consider λi = (λ1,λ2,··· ,λk) ∈ Zk≥0 such that

n k

k gcd(k,i)

, λk =

λi =

![image 184](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile184.png>)

![image 185](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile185.png>)

i gcd(k,i)

−

, and λs = 0 for s  ∈ {i,k}.

![image 186](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile186.png>)

It is easy to check that kℓ=1 ℓλℓ = n. Also note that λk = n/k − i/gcd(k,i) ≥ n/k − i ≥ n/k − (k − 1) ≥ 0.

So λi is an (n,k)-type and thus appears as a row of the matrix A. We will assign ni /(k/gcd(k,i)) to x λ

, but ﬁrst we explain why ni /(k/gcd(k,i)) is an integer. For every prime p, if the p-adic valuation of n is x and that of i is y, then the p-adic valuation of n/gcd(n,i) equals max{x−y,0}. On the other hand, Kummer’s Theorem [20] says that for any prime p, the p-adic valuation of ni is equal to the number of carries when n − i is added to i in base p. This quantity is obviously at least max{x − y,0}. Consequently n/gcd(n,i) always divides ni . Since n is a multiple of k, it is easy to see that k/gcd(k,i) divides n/gcd(n,i). This completes the proof of our claim.

i

for the aforementioned λi for i ∈ {1,··· ,k − 1}, the ﬁrst k − 1 equations of the system (1) have already been taken care of. We just use the type λk = (λ1,··· ,λk) with λk = n/k and λs = 0 for s = k to cover whatever is left for bk = nk . Recall that k− ni−1 / k n−i ≤ k/(n − k + 1) for i ≥ 0, and n ≥ k2 − k, therefore the accumulated value γn,k of the last equation of the system (1) equals

Once we have chosen the value of x λ

i

k−1

n/k − i/gcd(k,i) k/gcd(k,i)

·

![image 187](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile187.png>)

i=1

n i

k−1

=

i=1

≤

n 2k

![image 188](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile188.png>)

i k

n k2/gcd(k,i)

−

![image 189](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile189.png>)

![image 190](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile190.png>)

·

1 k

−

![image 191](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile191.png>)

k n − k + 1

+

![image 192](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile192.png>)

n i

k−1

≤

i=1

k n − k + 1

![image 193](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile193.png>)

1 k

n 2k

−

![image 194](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile194.png>)

![image 195](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile195.png>)

2

+ ···

·

n i

n k

n − 2 2(n − 2k + 1)

<

![image 196](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile196.png>)

n k

k2 − k − 2 2(k2 − 3k + 1)

≤

![image 197](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile197.png>)

n k

≤

n k

= bk

if k ≥ 4. For k = 2 the left hand side is (n/2 − 1)n/2, which is always less than n2 . For k = 3, the left hand side is (n − 3)n/9 + (n − 6) n2 /9, which is also less than n3 . It shows the number x λ

= ( nk − γn,k)/(n/k) of the type λk needed is non-negative (it should be mentioned that the divisibility of n/k to nk −γn,k is automatic by the setting). This proves the case when n ≥ k2 −k.

k

For the remaining case n = k2 − 2k, we deﬁne the same λi and repeat the same assignment x λ

as the n ≥ k2 − k case for i ∈ {1,··· ,k − 3}. We then let x λ = k− n2 for the (n,k)-type λ with λk−2 = 1 and λk−1 = k − 2. As k− n2 / k− n1 = 1/(k − 2), these together take care of the ﬁrst

- i


- k −1 equations of the system (1). Finally, using the type λk and by the same estimation as the the n ≥ k2 − k case, we can cover the level k precisely. This also gives a non-negative integer solution to the system (1).


![image 198](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile198.png>)

![image 199](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile199.png>)

![image 200](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile200.png>)

![image 201](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile201.png>)

- Lemma 3.5. Suppose n > 2k and n = j ·k+k−1, where j is a non-negative such that j ≥ ⌈k2⌉−2, then the system (1) has a non-negative integer solution.


![image 202](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile202.png>)

Proof. Suppose n = jk + (k − 1) for j ≥ ⌈k/2⌉ − 2. As n > 2k, in fact we have n ≥ 3k − 1. First we consider the case when k is even. Then we have n ≥ k2/2 − k − 1 and k divides n + 1. Now instead of ﬁnding solutions to AT x = b, we consider the n+1 case and the new system (A′)Ty  = b′. Here A′ is the matrix deﬁned for the (n+1,L) case with L = {2,4,··· ,k}, and b′ is a vector in Rk such that bi = n+1i for even i, and 0 for odd i. This system of linear equations has a non-negative integer solution by taking the type λi = (λ1,λ2,··· ,λk) with

n + 1 k

k gcd(k,i)

, λk =

λi =

![image 203](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile203.png>)

![image 204](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile204.png>)

i gcd(k,i)

−

, and λs = 0 for s  ∈ {i,k}.

![image 205](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile205.png>)

and assigning n+1i /(k/gcd(k,i)) to y λ

, for i = 2,4,··· ,k − 2 and then using the type λk = (λ′1,λ′2,··· ,λ′k) such that λ′k = (n + 1)/k and λ′s = 0 for each s = k to cover whatever is left for bk. Similar as before, all deﬁned y λ are integers. Furthermore, since we only do it for even i, k is also even and n + 1 ≥ k(k − 2)/2, we always have

i

n + 1 k

−

![image 206](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile206.png>)

i gcd(k,i)

≥

![image 207](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile207.png>)

n + 1 k

i 2

−

![image 208](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile208.png>)

![image 209](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile209.png>)

≥

n + 1 k

−

![image 210](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile210.png>)

k − 2 2

≥ 0. (13)

![image 211](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile211.png>)

It only remains to show that the type λk appears for a non-negative number of times. This can be estimated as follows (in a similar way as in the proof of Lemma 3.4)

(n + 1)/k − i/gcd(k,i) k/gcd(k,i)

·

![image 212](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile212.png>)

i∈{2,4,···,k−2}

=

i∈{2,4,···,k−2}

n + 1 2k

2 k

−

![image 213](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile213.png>)

![image 214](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile214.png>)

·

n + 1 i

n − 3 2k

≤

·

![image 215](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile215.png>)

k n − k + 2

![image 216](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile216.png>)

2

+

k n − k + 2

![image 217](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile217.png>)

n + 1 i

3

+ ··· ·

n − 3 k

·

<

![image 218](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile218.png>)

k n − k + 2

![image 219](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile219.png>)

2

·

n + 1 k

k(n − 3) (n − k + 2)2

·

=

![image 220](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile220.png>)

n + 1 k

n + 1 k

≤

n + 1 k

= bk,

where we have k n−+1i−1 / nk+1−i ≤ k/(n − k + 2) ≤ 1/2 for i ≥ 0 and k(n − 3) ≤ (n − k + 2)2 under the fact that n ≥ 3k − 1. So this indeed gives a non-negative integer solution to (A′)T y = b′. Therefore by Theorem 2.2, if we let F consist of all the subsets of [n + 1] of even size up to k, i.e., F = {2 [,n4,+1]···,k} , then this family can be decomposed into 1-factors. We delete the element n + 1 from the unique subset containing it in each 1-factor. It is not hard to see that this immediately gives a 1-factorization of Kn≤k, and thus the system (1) has a non-negative integer solution (under the conditions of Lemma 3.5) when k is even.

For the remaining proof, we assume that k is odd. In this case, we have n = jk + k − 1 with

- j ≥ ⌈k/2⌉ − 2 = (k − 3)/2. So we may assume that n = (k2 − k − 2)/2 + tk for some integer t ≥ 0.

It is not hard to see that the above proof for the even k case still works for the odd k case (i.e., applied to {1,3, [···n+1],k−2,k} ) whenever the corresponding form for (13) holds. However, for odd k and i ∈ {1,3,··· ,k −2}, we cannot ensure gcd(k,i) ≥ 2, which was used in (13) for the even k case. As to infer that n+1k − gcd(ik,i) ≥ n+1k − i ≥ 0 holds for all i ∈ {1,3,··· ,k − 2}, this approach requires an additional condition n + 1 ≥ k(k − 2) or equivalently t ≥ (k − 3)/2. Therefore, from now on we may further assume that

![image 221](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile221.png>)

![image 222](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile222.png>)

![image 223](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile223.png>)

0 ≤ t ≤ (k − 5)/2. Since n = k(k + 2t − 1)/2 − 1 and (k + 2t − 1)/2 ≤ k − 3, if we view (k + 2t − 1)/2 as a new parameter k′, then n = j′ · k′ − 1 with j′ = k ≥ k′ + 3. By the previous proofs, no matter if k′ is odd or even, we can always conclude that ≤(k+2 [nt]−1)/2 = ≤ [nk]′ is 1-factorable. So it suﬃces to show that the family consisting of subsets of [n] of size between (k + 2t + 1)/2 and k, denoted by

[n]

{(k+2t+1)/2,···,k−1,k} , is 1-factorable.2

The rest of the proof will be divided into two cases: when t = (k − 5)/2 and when 0 ≤ t ≤ (k−7)/2. First we consider the case when t = (k−5)/2. In this case, we have n = (k2−k−2)/2+tk =

- k2 − 3k − 1, and (k + 2t + 1)/2 = k − 2. So it suﬃces to show {k−2 [,kn−] 1,k} is 1-factorable. We will use the following three (n,{k − 2,k − 1,k})-types (all unspeciﬁed coordinates λi are 0 by default):


A : λk−2 = (k + 1)/2, and λk = (k − 5)/2. B : λk−2 = (k − 1)/2, λk−1 = 2, and λk = (k − 7)/2. C : λk−1 = 1, and λk = k − 4. Note that nk / k− n1 = (n − k + 1)/k = k − 4 and type C has the same ratio for level k − 1 and

- k. So if we assume that type A is used a times and type B is used b times, then we need to ﬁnd a non-negative integer solution to the following system of equations:


k − 1 2

k + 1 2

a +

b =

![image 224](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile224.png>)

![image 225](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile225.png>)

n k − 2

=

k2 − 3k − 1 k − 2

,

![image 226](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile226.png>)

2Theorem 2.2 states that for any set L of distinct positive integers, the family [Ln] is 1-factorable if and only if the corresponding system (1) for L has a non-negative integer solution. We are aware that we are looking for non-negative integer solutions for the (corresponding) system (1), however for convenience of presentation, we should mention and identify both settings.

k − 5 2

k − 7 2

b 2b = k − 4. Solving it gives that

a +

![image 227](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile227.png>)

![image 228](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile228.png>)

(k − 3)/2 (k2 − 3k − 1)/3

a =

![image 229](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile229.png>)

k2 − 3k − 1 k − 2

(k − 5)/2 k2 − 3k − 1

and b =

![image 230](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile230.png>)

k2 − 3k − 1 k − 2

.

Note that k2−33k−1 divides gcd(3k2−3,kk−−2)1 , and gcd(3k2−3,kk−−2)1 = gcd(kk22−−33kk−−11,k−2) divides k2−k−3k2−1 ; also k is odd, so we can see that a is a non-negative integer. For b, note that when k  ≡ 2 (mod 3),

![image 231](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile231.png>)

![image 232](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile232.png>)

![image 233](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile233.png>)

![image 234](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile234.png>)

k2 − 3k − 1 = gcd(3k2−3,kk−−2)1 divides k2−k−3k2−1 , while when k ≡ 2 (mod 3) (k is odd, so in fact k ≡ 5 (mod 6)), (k2 − 3k − 1)/3 divides k2−k−3k2−1 and (k − 5)/6 is an integer. Therefore b is also an non-negative integer. Finally by considering the level k − 1, we can use the type C for c times, where

![image 235](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile235.png>)

k − 5 k2 − 3k − 1

n k − 1

n k − 2

n k − 1

− 2b =

≥ 0.

−

c =

![image 236](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile236.png>)

The above analysis gives a non-negative integer solution to the corresponding system (1) for L = {k − 2,k − 1,k} and thus the proof for the case t = (k − 5)/2 is complete.

Now we consider the last case when 0 ≤ t ≤ (k − 7)/2. For this case, we have k ≥ 7 and we

want to show that [Ln] is 1-factorable for L = {(k + 2t + 1)/2,··· ,k − 1,k}. To show that, we will use the following (n,L)-types labelled by

R,S0,S1,S2,··· ,Sk−5 2 −t,T1,T2,··· ,Tk−5 2 −t.

![image 237](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile237.png>)

![image 238](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile238.png>)

Each of them is a vector λ = (λ1,··· ,λk) deﬁned as follows (here all the unspeciﬁed coordinates λi are equal to 0): for each 1 ≤ i ≤ (k − 5)/2 − t,

- R : λk−1 = 1, and λk = (k − 3)/2 + t,
- S0 : λk−2 = (k + 1)/2, and λk = t,


Si : λk−2−i = 1, λk−2 = (k − 1)/2 − i, λk−1 = i, and λk = t, and Ti : λk−2−i = 2, λk−2 = (k − 3)/2 − i, λk−1 = 0, and λk = t + i.

It is not hard to verify that each such λ satisﬁes ℓ∈L ℓλℓ = n so all of them are indeed (n,L)-types. The assumption t ≤ (k − 7)/2 guarantees that some types other than R and S0 are used. Let us assume that we use type R for x times, type Si for ai times for each i ∈ {0,1,··· ,(k − 5)/2 − t}, and type Ti for bi times for each i ∈ {1,··· ,(k − 5)/2 − t}. Note that only the type R corresponds to 1-factors of size (k − 1)/2 + t, while the other types correspond to 1-factors of size (k + 1)/2 + t. If we let y = a0 + a1 ··· + a(k−5)/2−t + b1 + ··· + b(k−5)/2−t, then we have

and

k − 1 2

+ t x +

![image 239](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile239.png>)

k + 1 2

+ t y =

![image 240](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile240.png>)

n (k + 1)/2 + t

+ ··· +

n k

, (14)

x + y =

n − 1 (k − 1)/2 + t

+ ··· +

n − 1 k − 1

. (15)

The ﬁrst equation is derived from double counting the total number of subsets in {(k+2t+1) [/n2],···,k−1,k} , while the second equation follows by double counting the number of 1-factors in the 1-factorization of {(k+2t+1) [/n2],···,k−1,k} . Solving (14) and (15) (see Appendix A for a detailed proof), we can obtain the precise values of x and y and show that both x and y are non-negative integers, where

(k−5)/2−t

(k−5)/2−t

k − 2 + 2t + i((k − 1)/2 + t) n

a0 +

(ai + bi) = y =

![image 241](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile241.png>)

i=1

i=0

n k − 2 − i

. (16)

After ﬁxing the number of times x for type R and the total number of times y for all other

types, our next step is to use the types S1,··· ,S(k−5)/2−t,T1,··· ,T(k−5)/2−t to fully occupy the levels from (k + 2t + 1)/2 to k − 3. This give rise to the following equations:

ai + 2bi =

n k − 2 − i

for each i ∈ {1,··· ,(k − 5)/2 − t}. (17)

Also note that nk / k− n1 = (k−3)/2+t and the type R maintains this ratio. Hence, we also need to guarantee that the contributions of other types except R to level k −1 and k are at an 1 : (k−23 +t) ratio. This leads to the following equality

![image 242](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile242.png>)

(k−5)/2−t

ibi −

ty +

i=1

(k−5)/2−t

k − 3 2

+ t ·

iai = 0. (18)

![image 243](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile243.png>)

i=1

It turns out that to ﬁnd a non-negative integer solution to the corresponding system (1) for L = {(k + 2t + 1)/2,··· ,k − 1,k}, it will suﬃce to ﬁnd a non-negative integer solution a0,a1,··· ,a(k−5)/2−t, b1,··· ,b(k−5)/2−t to the system of (k − 1)/2 − t equations formed by (16), (17) and (18). To solve the latter system, we could simply take

bi =

n k − 2 − i

/2 and ai =

n k − 2 − i

− 2bi for each i = 2,··· ,(k − 5)/2 − t,

and leave the other three variables a0,a1,b1 to be uniquely determined by the three equations (16), (17) for i = 1 and (18). A proof for showing the above assertions will be fully provided in Appendix

- A. We have now completed the proof of Lemma 3.5.


![image 244](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile244.png>)

![image 245](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile245.png>)

![image 246](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile246.png>)

![image 247](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile247.png>)

- 3.3 Proofs of Theorems 1.2 and 1.3 With all the preparations above, ﬁnally we are ready to address our main theorems.

- Proof of Theorem 1.2: For k < n/2, suppose n,k satisfy one of the two conditions. By Lemmas


- 3.4 and 3.5, the system (1) has a non-negative integer solution. Theorem 2.2 immediately tells us that for such n,k, Kn≤k is 1-factorable.


Now suppose Kn≤k is 1-factorable. Again using Theorem 2.2, it is neccesary that the system (1) has a non-negative integer solution. By Lemma 3.1, n must be congruent to 0 or −1 mod k. Now apply Lemma 3.2, we know that one of the two conditions in the statement of Theorem 1.2 must be met and this completes our proof.

![image 248](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile248.png>)

![image 249](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile249.png>)

![image 250](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile250.png>)

![image 251](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile251.png>)

As of now, we have completely characterized all the n,k in the range k < n/2 such that Kn≤k is 1-factorable. The range k ≥ n/2 could be tackled in a similar fashion by applying Farkas’ Lemma and Theorem 2.2. However, the statement of Theorem 1.3 already suggests that there is a very simple reduction to the k < n/2 range, as demonstrated below.

- Proof of Theorem 1.3: We ﬁrst show that for k ≥ n/2, if Kn≤n−k−1 is 1-factorable, then Kn≤k is also 1-factorable. Note that in this range, we always have n − k ≤ k. Take an arbitrary 1factorization M1,··· ,Mt of Kn≤n−k−1. For every subset S of [n] of size between n − k and k, we just pair S with its complement. This gives 12 ki=n−k ni 1-factors, which together with M1,··· ,Mt form a 1-factorization of Kn≤k.

![image 252](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile252.png>)

Next we prove the opposite direction. Suppose k ≥ n/2 and Kn≤k can be decomposed into 1-factors M1,··· ,Ms. For every k-set S, it must appear in some Mi. Suppose Mi consists of the subset S, together with ℓ other subsets T1,··· ,Tℓ. Then |T1 ∪ ··· ∪ Tℓ| = n − |S| = n − k ≤ k. So T1 ∪··· ∪Tℓ must also appear in some Mj (possibly j = i if ℓ = 1). We move those T1,··· ,Tℓ from Mi to Mj, and also move T1 ∪···∪Tℓ from Mj to Mi, to obtain a new 1-factorization of Kn≤k. Now S is paired with S. We repeat this process for every k-set S, and apply the same operation for sets of size between n/2 and k − 1 as well. At the end of this process, we end up with a 1-factorization of Kn≤k such that for each n−k ≤ i ≤ k, every i-set is paired with its complement. Removing these 1-factors gives an 1-factorization of Kn≤n−k−1.

![image 253](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile253.png>)

![image 254](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile254.png>)

![image 255](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile255.png>)

![image 256](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile256.png>)

![image 257](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile257.png>)

- 4 Extensions to other unions of levels of hypercube


Given a set L of distinct positive integers, recall that we denote by [Ln] the family of subsets of [n] whose size is an element of L. Can we ﬁnd a necessary and suﬃcient condition for [Ln] to be 1factorable, when n is suﬃciently large? Our Theorem 1.2 answers this question for L = {1,··· ,k}, showing that the condition needed is simply n ≡ 0,−1 (mod k). Does there exist such a neat suﬃcient and necessary condition for general L? In this section we establish a number of results in this direction. For the proofs below, we always let k be the maximum element of L.

- Theorem 4.1. When n is suﬃciently large and divisible by k, [Ln] is always 1-factorable. Proof. Suppose L = {ℓ1,··· ,ℓt} with ℓ1 < ··· < ℓt = k, n = jk and j is suﬃcient large. We present


a non-negative integer solution to the system (1) with bi = ni for i ∈ L and 0 otherwise, along the same line of the proof of Lemma 3.4, and the conclusion follows from Theorem 2.2.

For each 1 ≤ i ≤ t − 1, we take λ ∈ Zk≥0 such that

n k

k gcd(k,ℓi)

, λk =

λℓi =

![image 258](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile258.png>)

![image 259](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile259.png>)

ℓi gcd(k,ℓi)

−

, λs = 0 for s  ∈ {ℓi,k}.

![image 260](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile260.png>)

Similarly as before, it is not hard to see that λ is a (n,L)-type for suﬃciently large n divisible by k. Now we just let x λ = ℓ n

/(k/gcd(k,ℓi)) to take care of bℓi for each i = 1,··· ,t − 1. Finally we use the type λ = (0,··· ,0,n/k) to take care of the remainder for bk. The number of such types is non-negative follows similarly as before.

i

![image 261](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile261.png>)

![image 262](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile262.png>)

![image 263](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile263.png>)

![image 264](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile264.png>)

Our next result generalizes Lemma 3.1.

- Theorem 4.2. For suﬃciently large n, if [Ln] is 1-factorable, then n ≡ 0 or −1 (mod k).

Proof. Suppose n = jk + r for 1 ≤ r ≤ k − 2. We use Farkas’ Lemma and take  y ∈ Rk such that yk = −1, yr = j and ys = j/2 for s  ∈ {k,r}. First we explain why AL y ≥ 0. Take a row λ of AL, by our deﬁnition of AL, we have ki=1 iλi = n and λi = 0 for those i  ∈ L. Note that n = jk + r < (j + 1)k, we have λk ≤ j and i k=1−1 iλi = r or i k=1−1 iλi ≥ r + k. These imply either λr = 1 or i k=1−1 λi ≥ 2. In either case we have

k

i=1

λiyi =

k−1

i=1

λkyk + λkyk ≥ j − j = 0.

Next we show that y  · bL < 0. Equivalently, we need to prove

i∈L\{k}

j 2

![image 265](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile265.png>)

n i

+ 1r∈L ·

j 2

![image 266](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile266.png>)

·

n r

<

n k

.

We instead prove a stronger inequality

k−1

i=1

j 2

![image 267](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile267.png>)

n i

+

j 2

![image 268](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile268.png>)

·

n r

<

n k

. (19)

Note that for i ≥ 1,

n k − i

/

n k − i + 1

=

k − i + 1 n − k + i

![image 269](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile269.png>)

=

k − i + 1 (j − 1)k + i + r

![image 270](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile270.png>)

≤

k (j − 1)k + r + 1

![image 271](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile271.png>)

≤

1 j − 1

![image 272](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile272.png>)

.

Also we have nr ≤ k− n2 . Therefore the left hand side of (19) is at most

1 j − 1

![image 273](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile273.png>)

+

1 j − 1

![image 274](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile274.png>)

2

+ ··· ·

j 2

![image 275](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile275.png>)

·

n k

+

j 2

![image 276](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile276.png>)

·

1 (j − 1)2

![image 277](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile277.png>)

·

n k

<

j 2(j − 2)

![image 278](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile278.png>)

+

j 2(j − 1)2

![image 279](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile279.png>)

n k

<

n k

for j ≥ 5. Since we assume that n is suﬃciently large, this completes the proof. When n ≡ −1 (mod k), we can further prove the following.

![image 280](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile280.png>)

![image 281](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile281.png>)

![image 282](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile282.png>)

![image 283](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile283.png>)

- Theorem 4.3. Suppose n is suﬃcient large and n = jk +k −1 for some positive integer k. If [Ln] is 1-factorable, then L must contain the element k − 1.


Proof. We prove the contra-positive: suppose k −1  ∈ L = {ℓ1,··· ,ℓt} with ℓ1 < ··· < ℓt = k, then [n] L is not 1-factorable. Once again we would like to use Farkas’ Lemma to show that ATL x = bL

has no non-negative solution. Take the vector y  ∈ Rk such that

j 2

yℓi =

![image 284](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile284.png>)

for i = 1,··· ,t − 1, yk = −1.

The rest of the coordinates of  y are set to be zero. First we show that ALy  ≥ 0. Take a row λ = (λ1,··· ,λk), recall that λi = 0 for i  ∈ L. So ti=1 ℓiλℓi = n = jk + (k − 1). Therefore λk ≤ j and ti=1−1 λℓi ≥ 1. If ti=1−1 λℓi ≥ 2, then

k

j 2

λiyi ≥

·

![image 285](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile285.png>)

i=1

t−1

λℓi − λk ≥ j − j = 0.

i=1

If ti=1−1 λℓi = 1, then n is congruent to ℓi modulo k, for some 1 ≤ i ≤ t − 1, this is not possible since k − 1  ∈ L and thus all such ℓi are at most k − 2, but we have n ≡ k − 1 (mod k).

Next we prove bL ·  y < 0. Since k − 1  ∈ L, it suﬃces to prove

Note that for every i ≥ 1,

k−2

j 2

![image 286](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile286.png>)

i=1

n i

<

n k

. (20)

n k − i

/

n k − i + 1

k − i + 1 n − k + i

=

=

![image 287](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile287.png>)

k − i + 1 jk + i − 1

1 j

≤

.

![image 288](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile288.png>)

![image 289](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile289.png>)

Therefore the left hand side of inequality (20) is at most

j 2

![image 290](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile290.png>)

1 j3

1 j2

+ ···

+

![image 291](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile291.png>)

![image 292](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile292.png>)

n k

1 2(j − 1)

<

![image 293](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile293.png>)

n k

≤

n k

,

as long as j ≥ 2. We make the following conjecture based on the above results.

![image 294](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile294.png>)

![image 295](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile295.png>)

![image 296](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile296.png>)

![image 297](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile297.png>)

Conjecture 4.4. Given a set of distinct positive integers L whose largest element is k. Depending on the choice of L, exactly one of the following statements must be true:

- (i) For suﬃciently large n, [Ln] is 1-factorable if and only if n ≡ 0 (mod k),
- (ii) For suﬃciently large n, [Ln] is 1-factorable if and only if n ≡ 0,−1 (mod k). When k −1 ∈ L, it seems that both scenarios are possible. For example, L = {k −1,k} satisﬁes


(ii), since for n = jk − 1, we could use the type λ = (0,··· ,0,1,j − 1) exactly k− n1 times, and Theorem 4.1 takes care of the n = jk case. On the other hand, if we take k = 4 and L = {2,3,4},

then for n = 4j − 1, applying Farkas’ Lemma with the vector  y = (−1/2,j − 1,−1)T shows that [n] L is not 1-factorable, and thus L = {2,3,4} corresponds to case (i) in Conjecture 4.4. It would

be great if some criteria on those L satisfying k − 1 ∈ L could be found to tell whether [Ln] is 1-factorable for suﬃciently large n ≡ −1 (mod k).

# 5 Concluding Remarks

In this paper, we determine all the pairs of positive integers (n,k) such that ≤ [nk] is 1-factorable. We include a few open questions and possible future projects below.

- • Our method might be extendable to the scenario when repetition of subsets are allowed in the hypergraph. In [2], Bahmanian show that the existence of a symmetric Latin cube is equivalent to the existence of a partition into parallel classes of some non-uniform set system.

In particular, he determined all n such that [n1] ∪ 3 [n2] ∪ 2 [n3] is 1-factorable. Here every pair appears three times and every triple shows up twice. Would it be possible to determine

for which n and sequence {mi}i=1,···,n of non-negative integers, ∪ni=1mi [ni] is 1-factorable?

- • A famous conjecture of Chv´atal [12] says that any for any given hereditary family F (i.e. A ∈ F and B ⊂ A implies B ∈ F), the maximum size of its intersecting subfamily is attained by taking all sets containing the most popular element. If we construct a graph GF such that V (GF) = F, and two vertices S,T ∈ F are adjacent if and only if S ∩ T = ∅, then Chv´atal’s conjecture is equivalent to showing α(GF) = maxx |Fx|, here we denote by Fx the family of subsets containing x. Observe that when F is regular, i.e. every element in the ground set occurs for an equal number of times, F is 1-factorable if and only if χ(GF) = maxx |Fx|, which is a stronger bound and immediately implies α(GF) = maxx |Fx|. Inspired by Theorem 1.2, one may wonder whether there is a nice characterization of all the regular hereditary families F that are 1-factorable.


![image 298](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile298.png>)

# References

- [1] N. Alon and S. Friedland, The maximum number of perfect matchings in graphs with a given degree sequence, Electron. J. Combin. 15 (2008), N13.
- [2] A. Bahmanian, Symmetric layer-rainbow colorations of cubes, available at arXiv:2205.02210 [math.CO].
- [3] A. Bahmanian, Connected Baranyai’s theorem, Combinatorica 34 (2014), 129–138.
- [4] A. Bahmanian, Factorizations of complete multipartite hypergraphs, Discrete Math. 340

(2017), 46–50.

- [5] A. Bahmanian, A. Johnsen and S. Napirata, Embedding connected factorizations, J. Combin. Theory, Ser. B 155 (2022), 358–373.
- [6] A. Bahmanian and M. Newman, Extending factorizations of complete uniform hypergraphs, Combinatorica 38 (2018), 1309–1335.
- [7] Zs. Baranyai, On the factorization of the complete uniform hypergraph, Colloq. Math. Soc. Janos Bolyai 10 (1975), 91–108.
- [8] Zs. Baranyai and A. E. Brouwer, Extension of colourings of the edges of a complete (uniform Hyper)graph, CWI Technical Report ZW 91/77, 1977.
- [9] P. J. Cameron, Parallelisms of complete designs, Cambridge University Press, Cambridge-New York-Melbourne, 1976. London Mathematical Society Lecture Note Series, No. 23.


- [10] A.G. Chetwynd and A.J.W. Hilton, Regular graphs of high degree are 1-factorizable, Proc. London Math. Soc. 50 (1985), 193–206.
- [11] A.G. Chetwynd and A.J.W. Hilton, 1-factorizing regular graphs of high degree — an improved bound, Discrete Math. 75 (1989), 103–112.
- [12] V. Chv´atal, Intersecting families of edges in hypergraphs having the hereditary property, Hypergraph Seminar (Proc. First Working Sem., Ohio State Univ., Columbus, Ohio, 1972; dedicated to Arnold Ross), 61–66. Lecture Notes in Math., Vol. 411, Springer, Berlin, 1974.
- [13] B. Csaba, D. Ku¨hn, A. Lo, D. Osthus, A. Treglown, Proof of the 1-factorization and Hamilton decomposition conjectures, Mem. Amer. Math. Soc. 244, (2016), no. 1154, v+164 pp.
- [14] G. Dantzig and D. Fulkerson, On the max-ﬂow min-cut theorem of networks, in: H.W. Kuhn, A.W. Tucker (Eds.), Linear Inequalities and Related Systems, in: Annals of Mathematics Study, vol. 38, Princeton University Press, Princeton, NJ, 1956, 215–221.
- [15] J. Farkas, Theorie der Einfachen Ungleichungen, Journal fu¨r die Reine und Angewandte Mathematik 124 (1902), 1–27.
- [16] A. Ferber and V. Jain, 1-factorizations of pseudorandom graphs, 2018 IEEE 59th Annual Symposium on Foundations of Computer Science (FOCS), 2018, pp. 698-708, doi: 10.1109/FOCS.2018.00072
- [17] A. Ferber, V. Jain, and B. Sudakov, Number of 1-factorizations of regular high-degree graphs, Combinatorica 40 (2020), 315–344.
- [18] R. H¨aggkvist and T. Hellgren, Extensions of edge-colourings in hypergraphs, I, in: Combinatorics, Paul Erdo˝s is eighty, Vol. 1, Bolyai Soc. Math. Stud., 215–238. Ja´nos Bolyai Math. Soc., Budapest, 1993.
- [19] I. Holyer, The NP-completeness of edge-colouring, SIAM Journ. Comp. 10 (1981), 718–720.
- [20] E. Kummer, Uber¨ die Erg¨anzungss¨tze zu den allgemeinen Reciprocit¨atsgesetzen, Journal fu¨r die reine und angewandte Mathematik 1852(44), 93–146. (Erschienen im Druck 1852) https://doi.org/10.1515/crll.1852.44.93
- [21] E. Mendelsohn and A. Rosa One-factorizations of the complete graph - a survey, J. Graph Theory 9 (1985), 43–65.
- [22] R. Peltesohn, Das Turnierproblem fu¨r Spiele zu je dreien, Inaugural dissertation, Berlin 1936.
- [23] L. Perkovic and B. Reed, Edge coloring regular graphs of high degree, Discrete Math. 165/166

(1997), 567–578.

- [24] M.J. Plantholt and S.K. Tipnis, All regular multigraphs of even order and high degree are 1-factorable, Electron. J. Combin. 8 (2001), R41.


- [25] M. Stiebitz, D. Scheide, B. Toft and L.M. Favrholdt, Graph edge coloring: Vizing’s Theorem and Goldberg’s Conjecture, Wiley 2012
- [26] W. D. Wallis, One-factorization of complete graphs, Contemporary Design Theory: A Collection of Surveys (1992) 593–631.


# Appendix A Finding a non-negative integer solution in the proof of Lemma 3.5

We consider the case when k is odd, n = (k2 − k − 2)/2 + tk and 0 ≤ t ≤ (k − 7)/2. In particular k ≥ 7. Our aim here is to provide detailed arguments to the proof described for this case of Lemma 3.5, as to ﬁnd a non-negative integer solution to the corresponding system (1) for L = {(k + 2t + 1)/2,··· ,k − 1,k}.

First let us determine x and y as non-negative integers. From (14) and (15),

k

k − 1 2

n i

−

+ t ·

y =

![image 299](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile299.png>)

i=(k+1)/2+t

= 

k−2

n − i((k − 1)/2 + t) n

·



![image 300](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile300.png>)

i=(k+1)/2+t

k−2

n − i((k − 1)/2 + t) n

·

=

![image 301](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile301.png>)

i=(k+1)/2+t

n − 1 i − 1

n i

n i

(k−5)/2−t

k − 2 + 2t + i((k − 1)/2 + t) n

=

![image 302](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile302.png>)

i=0

  +

(k − 3)/2 + t n

![image 303](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile303.png>)

n k − 1

1 n

−

![image 304](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile304.png>)

n k

n k − 2 − i

. (21)

From the ﬁrst equality, we know that y is an integer, and the last form clearly indicates that y is non-negative. From (14) and (15), using n = k(k+12 +t)−(k +1) and k+12 +t ≤ k +1, we also have

![image 305](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile305.png>)

![image 306](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile306.png>)

x =

k

i=(k+1)/2+t

k + 1 2

+ t ·

![image 307](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile307.png>)

n − 1 i − 1

−

n i

k

i((k + 1)/2 + t) − n n

·

=

![image 308](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile308.png>)

i=(k+1)/2+t

n i

=

k

1 n

![image 309](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile309.png>)

i=(k+1)/2+t

k + 1 2

(k + 1) − (k − i)(

+ t) ·

![image 310](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile310.png>)

n i

≥

k−1

1 n

![image 311](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile311.png>)

i=(k+1)/2+t

(k + 1) ·

n i + 1

k + 1 2

+ t) ·

− (k − i)(

![image 312](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile312.png>)

k−1

n − i − (k − i)(i + 1) i + 1

k + 1 n

·

≥

![image 313](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile313.png>)

![image 314](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile314.png>)

i=(k+1)/2+t

n i

≥ 0,

n i

where the ﬁrst equality shows x is an integer and the last inequality follows from the fact that n − i − (k − i)(i + 1) = n − (k − i)i − k ≥ k2−2k−2 − k42 − k ≥ 0 holds for k ≥ 7.

![image 315](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile315.png>)

![image 316](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile316.png>)

Recall the system of (k − 1)/2 − t equations formed by (16), (17) and (18), and that to ﬁnd

a non-negative integer solution a0,a1,··· ,a(k−5)/2−t, b1,··· ,b(k−5)/2−t to this system, we take for each i ∈ {2,3,··· ,(k − 5)/2 − t},

bi =

n k − 2 − i

/2 and ai =

n k − 2 − i

− 2bi ∈ {0,1}. (22)

It remains to ﬁnd non-negative integers a0,a1,b1 for the system. Consider A = i (=1k−5)/2−t iai and

- B = i (=1k−5)/2−t ibi. Rewriting (18), we obtain


B =

k − 3 2

+ t A − ty. (23)

![image 317](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile317.png>)

Now we multiply i to (17), and sum over all deﬁned i, we have

(k−5)/2−t

A + 2B =

i

i=1

n k − 2 − i

. (24)

Plugging in the expression (23) on B to (24), we can solve A as follows:

(k−5)/2−t

n k − 2 − i

(k − 2 + 2t)A = 2ty +

i

i=1

(k−5)/2−t

(k − 2 + 2t)(2t + i(t + k+12 ))) n

n k − 2 − i

![image 318](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile318.png>)

·

=

![image 319](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile319.png>)

i=0

(k−5)/2−t

n k−2−i

k + 1 2

= (k − 2 + 2t)

2t + i(t +

)

![image 320](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile320.png>)

![image 321](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile321.png>)

n

i=0

(k−5)/2−t

n k−2−i

k + 1 2

= (k − 2 + 2t)

n − (k − 2 − i)(

+ t)

![image 322](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile322.png>)

![image 323](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile323.png>)

n

i=0

(k−5)/2−t

n − 1 k − 3 − i

n k − 2 − i

k + 1 2

− (

= (k − 2 + 2t)

+ t)

![image 324](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile324.png>)

i=0

.

(25)

This shows that A is an non-negative integer (where the third last form shows the non-negativity). Using (23), B is also an integer.

We now show a1,b1,a0 are non-negative integers in order. First we determine a1 from A.

If k−25 − t = 1, then clearly a1 = A is a non-negative integer. Assume k−25 − t ≥ 2, which implies that k ≥ 9. By (22), we have ai ∈ {0,1} for 2 ≤ i ≤ (k − 5)/2 − t. Using (25) that

![image 325](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile325.png>)

![image 326](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile326.png>)

A = i (=0k−5)/2−t 2t+i(t+(nk+1)/2) k− n2−i , we then get

![image 327](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile327.png>)

(k−5)/2−t

(k−5)/2−t

a1 = A −

iai =

i=2

i=2

(k−5)/2−t

k + 1 2

≥

)

2t + i(t +

![image 328](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile328.png>)

i=2

k + 1 2

)

2t + i(t +

![image 329](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile329.png>)

n k−2−i

![image 330](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile330.png>)

n

(k−5)/2−t

n k−2−i

− i ≥

![image 331](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile331.png>)

n

i=2

(k−5)/2−t

−

iai

i=2

k + 1 2

− 1 i ≥ 0,

![image 332](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile332.png>)

as desired. Since B is an integer, it is easy to see that b1 = B − i (=2k−5)/2−t ibi is also an integer. We also have a1 + 2b1 = k− n2−1 from (17), which gives

- 1

![image 333](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile333.png>)

- 2


b1 =

n k − 3

- 1

![image 334](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile334.png>)

- 2


− a1 ≥

n k − 3

− A .

Using (25), k− n2 / k− n3 = n−k−k+32 , and k−3 n−i−1 / k− n3−i ≤ n−k−k+43 for i ≥ 0, we have

![image 335](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile335.png>)

![image 336](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile336.png>)

n k − 3

(k−5)/2−t

2t + k+12 + t i n

k+1

2 + 3t n

2t(n − k + 3) n(k − 2)

n k − 3

n k − 2 − i

![image 337](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile337.png>)

![image 338](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile338.png>)

−

−

− A = 1 −

![image 339](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile339.png>)

![image 340](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile340.png>)

![image 341](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile341.png>)

i=2

(k−5)/2−t

2t + k+12 + t i n

k − 3 − 2t k − 2

n k − 3

n k − 2 − i

![image 342](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile342.png>)

−

=

![image 343](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile343.png>)

![image 344](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile344.png>)

i=2

(k−5)/2−t

(k2 − 4k − 5)/4 n

k − 3 − 2t k − 2

n k − 3

n k − 2 − i

−

≥

![image 345](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile345.png>)

![image 346](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile346.png>)

i=2

2

k2 − 4k − 5 4n

k − 3 n − k + 4

k − 3 n − k + 4

k − 3 − 2t k − 2

n k − 3 ≥

n k − 3

+ ···

−

≥

+

![image 347](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile347.png>)

![image 348](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile348.png>)

![image 349](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile349.png>)

![image 350](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile350.png>)

k2 − 4k − 5 4n

k − 3 n − 2k + 7

k − 3 − 2t k − 2

n k − 3 ≥

n k − 3

·

−

![image 351](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile351.png>)

![image 352](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile352.png>)

![image 353](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile353.png>)

k2 − 8k + 15 k2 − 5k + 12

4 k − 2

n k − 3

n k − 3

1 k − 2

3 k − 2

−

·

≥

≥ 0,

![image 354](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile354.png>)

![image 355](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile355.png>)

![image 356](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile356.png>)

![image 357](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile357.png>)

where the third last inequality uses that t ≤ (k − 7)/2 and n ≥ (k2 − k − 2)/2. From the analysis above, we have shown that b1 is a non-negative integer.

Recall that y = a0+ i (=1k−5)/2−t(ai+bi). It is easy to check that i (=1k−5)/2−t ai ≤ i (=1k−5)/2−t iai = A and bi ≤ 12 k− n2−i for 2 ≤ i ≤ (k − 5)/2 − t. In addition, we have b1 = 21 k− n3 − a1 and

![image 358](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile358.png>)

![image 359](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile359.png>)

a1 ≥ A − i (=2k−5)/2−t i. Thus we have

(k−5)/2−t

(k−5)/2−t

a0 = y −

ai −

bi

i=1

i=1

(k−5)/2−t

n k − 2 − i

1 2

≥ y − A −

![image 360](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile360.png>)

i=2

−

= y −

- 1

![image 361](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile361.png>)

- 2


A −

(k−5)/2−t

- 1

![image 362](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile362.png>)

- 2


i=1

n k − 2 − i

Recall from (21) that

  n

− 

i

 

(k−5)/2−t

- 1

![image 363](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile363.png>)

- 2


A −



k − 3

i=2

((k − 1)/2 − t) ((k − 7)/2 − t) 4

−

.

![image 364](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile364.png>)

(k−5)/2−t

k − 2 + 2t + i(t + (k − 1)/2) n

y =

![image 365](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile365.png>)

i=0

n k − 2 − i

(26)

and from (25) that A = i (=0k−5)/2−t 2t+i(t+(nk+1)/2) k− n2−i . Using ((k − 1)/2 − t)((k − 7)/2 − t) ≤ (k − 1)(k − 7)/4 ≤ n/2 and k−2 n−i−1 / k− n2−i ≤ n−k−k+32 for i ≥ 0, we can derive that (note that 2k − 4 − n < 0)

![image 366](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile366.png>)

![image 367](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile367.png>)

a0 ≥ 

(k−5)/2−t

2k − 4 + 2t + i k−23 + t − n 2n

n k − 2 − i

![image 368](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile368.png>)



![image 369](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile369.png>)

i=1

≥ 

  +

(k−5)/2−t

2k − 4 − n 2n

k − 2 n

n k − 2 − i

n k − 2



![image 370](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile370.png>)

![image 371](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile371.png>)

i=1

2

n − 2k + 4 2n

k − 2 n − k + 3

k − 2 n − k + 3

≥ −

···

+

![image 372](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile372.png>)

![image 373](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile373.png>)

![image 374](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile374.png>)

  +

k − 2 + t n

![image 375](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile375.png>)

n 8

−

![image 376](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile376.png>)

n k − 2

n 8

−

![image 377](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile377.png>)

n k − 2

k − 2 n

+

![image 378](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile378.png>)

n k − 2

n 8

−

![image 379](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile379.png>)

k − 2 n

=

![image 380](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile380.png>)

k − 2 2n

≥

![image 381](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile381.png>)

n k − 2

n k − 2

k − 2 n − 2k + 5

n − 2k + 4 2n

n k − 2

−

![image 382](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile382.png>)

![image 383](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile383.png>)

n − 1 k − 3

- 1

![image 384](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile384.png>)

- 2


n 8

n 8

≥

≥ 0.

−

−

![image 385](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile385.png>)

![image 386](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile386.png>)

n 8

−

![image 387](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile387.png>)

This completes the proof for ﬁnding a non-negative integer solution

S = {a0,a1,··· ,a(k−5)/2−t,b1,··· ,b(k−5)/2−t} to the system formed by (16), (17) and (18).

Lastly, we show that the above non-negative integer solution S together with the non-negative integer x solved from (14) and (15), along with the corresponding (n,L)-types, give a non-negative integer solution to the corresponding system (1) for L = {(k + 2t + 1)/2,··· ,k − 1,k}. By (17), the contribution of these types to level k − 2 − i satisﬁes

ai + 2bi =

n k − 2 − i

for each i ∈ {1,··· ,(k − 5)/2 − t}. (27)

Thus, it is enough to check that the contribution of these types to each level j ∈ {k − 2,k − 1,k} equals nj . We observe that as S satisﬁes (14), (15) and (18), it in fact suﬃces to verify that the contribution of these types to level k − 2 equals k− n2 , that is, we need to show the following

(k−5)/2−t

k + 1 2

a0 +

![image 388](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile388.png>)

i=1

(k−5)/2−t

k − 1 2

− i ai +

![image 389](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile389.png>)

i=1

k − 3 2

− i bi =

![image 390](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile390.png>)

n k − 2

. (28)

We claim that the above equation (28) is a linear combination of (18), (26), and (27) for all i ∈ {1,··· ,(k − 5)/2 − t}, with coeﬃcients

1 k − 2 + 2t

,

![image 391](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile391.png>)

n k − 2 + 2t

, and −

![image 392](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile392.png>)

k − 2 + 2t + i((k − 1)/2 + t) k − 2 + 2t

k − 5 2

for all i ∈ {1,··· ,

− t},

![image 393](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile393.png>)

![image 394](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile394.png>)

respectively. It is easy to see that the right side hand of the above linear combination equals k− n2 . For the left side hand of this linear combination, a careful calculation, using t+n = k+12 (k −2+2t) and y = a0 + i (=1k−5)/2−t(ai + bi), shows that it equals

![image 395](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile395.png>)

(k−5)/2−t

k − 1 2

(t + n)y k − 2 + 2t

1 k − 2 + 2t

i − 2 k − 2 + 2t + i

+

+ t bi

![image 396](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile396.png>)

![image 397](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile397.png>)

![image 398](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile398.png>)

i=1

(k−5)/2−t

k − 3 2

k − 1 2

1 k − 2 + 2t

+ t i + k − 2 + 2t + i

−

+ t ai

![image 399](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile399.png>)

![image 400](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile400.png>)

![image 401](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile401.png>)

i=1

(ai + bi)

 a0 +

(k−5)/2−t

(k−5)/2−t

(k−5)/2−t

k + 1 2

(i + 2)bi −

 −

(i + 1)ai

=

![image 402](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile402.png>)

i=1

i=1

i=1

(k−5)/2−t

(k−5)/2−t

k − 1 2

k − 3 2

k + 1 2

− i ai +

− i bi,

=

a0 +

![image 403](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile403.png>)

![image 404](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile404.png>)

![image 405](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile405.png>)

i=1

i=1

which is the left side hand of (28). This proves our claim, completing the proof of this appendix.

![image 406](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile406.png>)

![image 407](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile407.png>)

![image 408](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile408.png>)

![image 409](<2022-he-non-uniform-extension-baranyai-theorem_images/imageFile409.png>)

