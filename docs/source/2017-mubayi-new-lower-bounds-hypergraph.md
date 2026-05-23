---
type: source
kind: paper
title: New lower bounds for hypergraph Ramsey numbers
authors: Dhruv Mubayi, Andrew Suk
year: 2017
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/1702.05509v2
source_local: ../raw/2017-mubayi-new-lower-bounds-hypergraph.pdf
topic: general-knowledge
cites:
---

arXiv:1702.05509v2[math.CO]15Jan2018

New lower bounds for hypergraph Ramsey numbers

Dhruv Mubayi∗ Andrew Suk†

Abstract

The Ramsey number rk(s,n) is the minimum N such that for every red-blue coloring of the k-tuples of {1,...,N}, there are s integers such that every k-tuple among them is red, or n integers such that every k-tuple among them is blue. We prove the following new lower bounds for 4-uniform hypergraph Ramsey numbers:

c log n

r4(5,n) > 2n

cn1/5

and r4(6,n) > 22

,

where c is an absolute positive constant. This substantially improves the previous best bounds of 2n

c log log n

c log n

and 2n

, respectively. Using previously known upper bounds, our result implies that the growth rate of r4(6,n) is double exponential in a power of n.

As a consequence, we obtain similar bounds for the k-uniform Ramsey numbers rk(k + 1,n) and rk(k + 2,n) where the exponent is replaced by an appropriate tower function. This almost solves the question of determining the tower growth rate for all classical oﬀ-diagonal hypergraph Ramsey numbers, a question ﬁrst posed by Erdo˝s and Hajnal in 1972. The only problem that remains is to prove that r4(5,n) is double exponential in a power of n.

# 1 Introduction

A k-uniform hypergraph H with vertex set V is a collection of k-element subsets of V . We write Kn(k) for the complete k-uniform hypergraph on an n-element vertex set. The Ramsey number rk(s,n) is the minimum N such that every red-blue coloring of the edges of KN(k) contains a monochromatic red copy of Ks(k) or a monochromatic blue copy of Kn(k).

Diagonal Ramsey numbers refer to the special case when s = n, i.e. rk(n,n), and have been studied extensively over the past 80 years. Classic results of Erd˝os and Szekeres [12] and Erd˝os [8] imply that 2n/2 < r2(n,n) ≤ 22n for every integer n > 2. While small improvements have been made in both the upper and lower bounds for r2(n,n) (see [18, 4]), the constant factors in the exponents have not changed over the last 70 years.

![image 1](<2017-mubayi-new-lower-bounds-hypergraph_images/imageFile1.png>)

∗Department of Mathematics, Statistics, and Computer Science, University of Illinois, Chicago, IL, 60607 USA. Research partially supported by NSF grant DMS-1300138. Email: mubayi@uic.edu

†Department of Mathematics, University of California at San Diego, La Jolla, CA, 92093 USA. Supported by NSF grant DMS-1800736, NSF CAREER award DMS-1800746, and an Alfred Sloan Fellowship. Email: asuk@ucsd.edu. Mathematics Subject Classiﬁcation (2010) codes: 05D10, 05D40, 05C65

Unfortunately, for 3-uniform hypergraphs, our understanding of r3(n,n) is much less. Results of Erd˝os, Hajnal, and Rado [10] gives the best known lower and upper bounds for r3(n,n),

2c1n2 < r3(n,n) < 22c2n,

where c1 and c2 are positive constants. For k ≥ 4, there is also a diﬀerence of one exponential between the known lower and upper bounds for rk(n,n), that is,

twrk−1(c1n2) ≤ rk(n,n) ≤ twrk(c2n), (1)

where the tower function twrk(x) is deﬁned by twr1(x) = x and twri+1(x) = 2twri(x) (see [12, 11, 9]). A notoriously diﬃcult conjecture of Erd˝os, Hajnal, and Rado states that the upper bound in (1) is

essentially the truth, that is, there are constructions which demonstrates that rk(n,n) > twrk(cn), where c = c(k). The crucial case is when k = 3, since a double exponential lower bound for r3(n,n) would verify the conjecture for all k ≥ 4 by using the well-known stepping-up lemma of Erd˝os and Hajnal (see [13]).

Conjecture 1.1 (Erd˝os). For n ≥ 4, r3(n,n) > 22cn where c is an absolute constant.

Oﬀ-diagonal Ramsey numbers, rk(s,n), refer to the special case when k,s are ﬁxed and n tends to inﬁnity. It is known [1, 14, 2, 3] that r2(3,n) = Θ(n2/log n), and more generally for ﬁxed s > 3, r2(s,n) = nΘ(1). For 3-uniform hypergraphs, a result of Conlon, Fox, and Sudakov [6] shows that

2c1nlogn ≤ r3(s,n) ≤ 2c2ns−2 logn,

where c1 and c2 depend only on s. For k-uniform hypergraphs, where k ≥ 4, it is known that rk(s,n) ≤ twrk−1(nc), where c = c(s) [11]. By applying the Erd˝os-Hajnal stepping up lemma in the oﬀ-diagonal setting, it follows that

rk(s,n) ≥ twrk−1(c′n), (2) for k ≥ 4 and s ≥ 2k−1 − k + 3, where c′ = c′(s). In 1972, Erd˝os and Hajnal [9] conjectured that (2) holds for every ﬁxed k ≥ 4 and s ≥ k + 1. Actually, this was part of a more general conjecture that they posed in that paper (see [16, 17] for details). In [5], Conlon, Fox, and Sudakov veriﬁed the Erd˝os-Hajnal conjecture for all s ≥ ⌈5k/2⌉ − 3. Very recently, the current authors [16] and independently Conlon, Fox, and Sudakov [7] veriﬁed the conjecture for all s ≥ k+3 (using diﬀerent constructions). Since 2k−1−k+3 = ⌈5k/2⌉−3 = k+3 = 7 when k = 4, all three of these approaches succeed in proving a double exponential lower bound for r4(7,n) but fail for r4(6,n) and r4(5,n). Just as for diagonal Ramsey numbers, a double exponential in nc lower bound for r4(5,n) and r4(6,n) would imply rk(k + 1,n) > twrk−1(nc′) and rk(k + 2,n) > twrk−1(nc′) respectively, for all ﬁxed k ≥ 5. This follows from a variant of the stepping-up lemma that we will describe in Section 2. Therefore, the diﬃculty in verifying (2) for the two remaining cases, s = k + 1 and k + 2, is due to our lack of understanding of r4(5,n) and r4(6,n). Consequently, showing double exponential lower bounds for r4(5,n) and r4(6,n) are the only two problems that remain to determine the tower growth rate for all oﬀ-diagonal hypergraph Ramsey numbers.

Until very recently, the only lower bound for both r4(5,n) and r4(6,n) was 2cn, which was implicit in the paper of Erd˝os and Hajnal [9]. Our results in [15, 16] improved both these bounds to

r4(5,n) > 2ncloglogn and r4(6,n) > 2nclogn (3)

and these are the current best known bounds. As mentioned above, the bounds in (3) imply the corresponding improvements to the lower bounds for rk(k + 1,n) and rk(k + 2,n). In this paper we further substantially improve both lower bounds in (3).

Theorem 1.2. For all n ≥ 6,

1/5

r4(5,n) > 2nclogn and r4(6,n) > 22cn

, where c > 0 is an absolute constant.

Using the stepping-up lemma (see Section 2) we obtain the following. Corollary 1.3. For n > k ≥ 5, there is a c = c(k) > 0 such that

rk(k + 1,n) > twrk−2(nclogn) and rk(k + 2,n) > twrk−1(cn1/5).

A standard argument in Ramsey theory together with results in [6] for 3-uniform hypergraph Ramsey numbers yields the upper bound rk(k + 2,n) < twrk−1(c′n3 log n), so we now know the tower growth rate of rk(k + 2,n).

In [16], we established a connection between diagonal and oﬀ-diagonal Ramsey numbers. In particular, we showed that a solution to Conjecture 1.1 implies a solution to the following conjecture.

c

Conjecture 1.4. For n ≥ 5, there is an absolute constant c > 0 such that r4(5,n) > 22n

.

The main idea in our approach is to apply stepping-up starting from a graph to construct a 4uniform hypergraph, rather than the usual method of going from a 3-uniform hypergraph to a 4-uniform hypergraph. Although this approach was implicitly developed in [16], here we use it explicitly.

For more related Ramsey-type results for hypergraphs, we refer the interested reader to [16, 15, 17]. All logarithms are in base 2 unless otherwise stated. For the sake of clarity of presentation, we omit ﬂoor and ceiling signs whenever they are not crucial.

# 2 The stepping-up lemma and proof of Lemma 2.1

The proof of our main result, Theorem 1.2, follows by applying a variant of the classic Erd˝os-Hajnal stepping-up lemma. In this section, we describe the stepping-up procedure and sketch the proof of Lemma 2.1 below which is used to prove Corollary 1.3. The particular case below can be found in [15], though a special case of Lemma 2.1 was communicated to us independently by Conlon, Fox, and Sudakov [7].

- Lemma 2.1. For k ≥ 5 and n ≥ s ≥ k + 1, rk(s,2kn) > 2rk−1(s−1,n)−1.


Proof. Let k ≥ 5, n ≥ s ≥ k + 1, and set A = {0,1,... ,N − 1} where N = rk−1(s − 1,n) − 1. Let φ : k A−1 → {red, blue} be a red/blue coloring of the (k − 1)-tuples of A such that there is

no monochromatic red copy of Ks(−k−11) and no monochromatic blue copy of Kn(k−1). We know φ exists by the deﬁnition of N. Set V = {0,1,... ,2N − 1}. In what follows, we will use φ to deﬁne

a red/blue coloring χ : Vk → {red, blue} of the k-tuples of V such that χ does not contain a monochromatic red copy of Ks(k), and does not contain a monochromatic blue copy of K2(kkn) .

For any v ∈ V , write v = i N=0−1 v(i)2i with v(i) ∈ {0,1} for each i. For u = v, let δ(u,v) ∈ A denote the largest i for which u(i) = v(i). Notice that we have the following stepping-up properties

(see [13])

- Property I: For every triple u < v < w, δ(u,v) = δ(v,w) .
- Property II: For v1 < ··· < vr, δ(v1,vr) = max1≤j≤r−1 δ(vj,vj+1).

We will also use the following two stepping-up properties, which are easy consequences of Properties

- I and II.


- Property III: For every 4-tuple v1 < ··· < v4, if δ(v1,v2) > δ(v2,v3), then δ(v1,v2) = δ(v3,v4). Note that if δ(v1,v2) < δ(v2,v3), it is possible that δ(v1,v2) = δ(v3,v4).
- Property IV: For v1 < ··· < vr, set δj = δ(vj,vj+1) and suppose that δ1,... ,δr−1 forms a monotone sequence. Then for every subset of k-vertices vi1,vi2,... ,vik, where vi1 < ··· < vik, δ(vi1,vi2),δ(vi2,vi3),... ,δ(vik−1,vik) forms a monotone sequence. Moreover, for every subset of k − 1 vertices δj1,δj2,... ,δjk−1, there are k vertices vi1,... ,vik such that δ(vit,vit+1) = δjt.


Given any k-tuple v1 < v2 < ... < vk of V , consider the integers δi = δ(vi,vi+1),1 ≤ i ≤ k − 1. We say that δi is a local minimum if δi−1 > δi < δi+1, a local maximum if δi−1 < δi > δi+1, and a local extremum if it is either a local minimum or a local maximum. Since δi−1 = δi for every i, every nonmonotone sequence δ1,... ,δk−1 has a local extremum.

Using φ : k A−1 → {red, blue}, we deﬁne χ : Vk → {red, blue} as follows. For v1 < ··· < vk and δi = δ(vi,vi+1), we deﬁne χ(v1,... ,vk) = red if

- (a) δ1,... ,δk−1 forms a monotone sequence and φ(δ1,... ,δk−1) = red, or if
- (b) δ1,... ,δk−1 forms a zig-zag sequence such that δ2 is a local maximum. In other words, δ1 < δ2 > δ3 < δ4 > ··· .


Otherwise χ(v1,... ,vk) = blue.

For the sake of contradiction, suppose χ produces a monochromatic red copy of Ks(k) on vertices v1 < ··· < vs, and let δi = δ(vi,vi+1). If δ1,δ2,... ,δs−1 forms a monotone sequence, then by Property IV, φ colors every (k − 1)-tuple in the set {δ1,... ,δs−1} red, which is a contradiction. Let δi denote the ﬁrst local extremum in the sequence δ1,... ,δs−1. It is easy to see that δi is a local maximum since otherwise we would get a contradiction. Suppose i + k − 1 ≤ s. If δi+1 is not a local extremum, then χ(vi−1,vi,vi+1,... ,vi+k−2) = blue which is a contradiction. If δi+1 is a

local extremum, then it must be a local minimum which implies that χ(vi,vi+1,... ,vi+k−1) = blue, contradiction. Therefore we can assume that i + k − 1 > s, which implies i ≥ 3 since s ≥ k + 1.

However, this implies that either χ(vi−2,vi−1,... ,vi+k−3) = blue or χ(vs−k+1,vs−k+2,... ,vs) = blue, contradiction. Hence, χ does not produce a monochromatic red copy of Ks(k) in V .

Let m = 2kn. For the sake of contradiction, suppose χ produces a monochromatic blue copy of Km(k) on vertices v1,... ,vm and let δi = δ(vi,vi+1). By Property IV, there is no x such that δx,δx+1,... ,δx+n−1 forms a monotone sequence. Indeed, otherwise φ would produce a monochromatic blue copy of Kn(k−1) on vertices δx,δx+1,... ,δx+n−1. Therefore, we can set δi1,... ,δik to be the ﬁrst k local minimums in the sequence δ1,... ,δm−1. However, by Property II, χ colors the ﬁrst k vertices in the set {vi1,vi1+1,vi2,vi2+1,... ,vik,vik+1} red which is a contradiction. This completes the proof of Lemma 2.1.

![image 2](<2017-mubayi-new-lower-bounds-hypergraph_images/imageFile2.png>)

![image 3](<2017-mubayi-new-lower-bounds-hypergraph_images/imageFile3.png>)

![image 4](<2017-mubayi-new-lower-bounds-hypergraph_images/imageFile4.png>)

![image 5](<2017-mubayi-new-lower-bounds-hypergraph_images/imageFile5.png>)

# 3 A double exponential lower bound for r4(6, n)

The lower bound for r4(6,n) follows by applying a variant the Erd˝os-Hajnal stepping up lemma. We start with the following simple lemma which is a straightforward application of the probabilistic method.

- Lemma 3.1. There is an absolute constant c > 0 such that the following holds. For every n ≥ 6, there is a red/blue coloring φ of the pairs of {0,1,... ,⌊2cn⌋ − 1} such that


- 1. there are no two disjoint n-sets A,B ⊂ {0,1,... ,⌊2cn⌋ − 1}, such that φ(a,b) = red for every a ∈ A and b ∈ B, or φ(a,b) = blue for every a ∈ A and b ∈ B (i.e., no monochromatic Kn,n),
- 2. there is no n-set A ⊂ {0,1,... ,⌊2cn⌋ − 1} such that every triple ai,aj,ak ∈ A, where ai < aj < ak, avoids the pattern φ(ai,aj) = φ(aj,ak) = blue and φ(ai,ak) = red.


Proof. Set N = ⌊2cn⌋, where c is a suﬃciently small constant that will be determined later. Consider the red/blue coloring φ of the pairs (edges) of {0,1,... ,N − 1}, where each edge has probability 1/2 of being a particular color independent of all other edges. Then the expected number of monochromatic copies of the complete bipartite graph Kn,n is at most

N n

2

2−n2+1 < 1/3,

for c suﬃciently small and n ≥ 6.

We call a triple ai,aj,ak ∈ {0,1,... ,N −1} bad if ai < aj < ak and φ(ai,aj) = φ(aj,ak) = blue and φ(ai,ak) = red. Otherwise, we call the triple (ai,aj,ak) good. Now, let us estimate the expected number of sets A ⊂ {0,1,... ,N − 1} of size n such that every triple in A is good. For a given triple ai,aj,ak ∈ {0,1,... ,N − 1}, where ai < aj < ak, the probability that (ai,aj,ak) is good is 7/8. Let A = {a1,... ,an} be a set of n vertices in {0,1,... ,N − 1}, where a1 < ··· < an. Let S be a partial Steiner (n,3,2)-system with vertex set A, that is, S is a 3-uniform hypergraph such that each 2-element set of vertices is contained in at most one edge in S. Moreover, S satisﬁes

δ1 δ2 δ3

v1: 0 0 0

v2: 1 0 0

v3: 1 1 0

v4: 1 1 1

δ3 δ2 δ1

0 0 0

0 0 1

0 1 1

1 1 1

(a)

δ2 δ1=δ3

0 0

0 1

1 0

1 1

δ2 δ3 δ1

0 0 0

0 0 1

1 0 1

1 1 0

δ2 δ1 δ3

0 0 1

0 1 1

1 1 0

1 1 1

(b)

(c)

δ3 δ1 δ2

0 0 1

0 1 0

0 1 1

1 0 0

δ3 δ1 δ2

0 0 1

0 1 0

0 1 1

1 0 0

(d)

- Figure 1: Examples of v1 < v2 < v3 < v4 and δ1 = δ(v1,v2),δ2 = δ(v2,v3),δ3 = δ(v3,v4), such that χ(v1,v2,v3,v4) = red. For each case, vi is represented in binary form with the left-most entry being the most signiﬁcant bit.


|S| = c′n2. It is known that such a system exists. Then the probability that every triple in A is good is at most the probability that every edge in S is good. Since the edges in S are independent, that is no two edges have more than one vertex in common, the probability that every triple in A

′n2. Therefore, the expected number of sets of size n with every triple being good is at most

is good is at most 8 7 |S| ≤ 8 7 c

![image 6](<2017-mubayi-new-lower-bounds-hypergraph_images/imageFile6.png>)

![image 7](<2017-mubayi-new-lower-bounds-hypergraph_images/imageFile7.png>)

N n

- 7

![image 8](<2017-mubayi-new-lower-bounds-hypergraph_images/imageFile8.png>)

- 8


c′n2

< 1/3,

for an appropriate choice for c. By Markov’s inequality and the union bound, we can conclude that there is a coloring φ with the desired properties.

![image 9](<2017-mubayi-new-lower-bounds-hypergraph_images/imageFile9.png>)

![image 10](<2017-mubayi-new-lower-bounds-hypergraph_images/imageFile10.png>)

![image 11](<2017-mubayi-new-lower-bounds-hypergraph_images/imageFile11.png>)

![image 12](<2017-mubayi-new-lower-bounds-hypergraph_images/imageFile12.png>)

Let c > 0 be the constant from the lemma above, and let A = {0,1,... ,⌊2cn⌋ − 1} and φ :

- A 2 → {red, blue} be a 2-coloring of the pairs of A with the properties described above. Let


- V = {0,1,... ,N − 1}, where N = 2⌊2cn⌋. In what follows, we will use φ to deﬁne a red/blue coloring χ : V4 → {red, blue} of the 4-tuples of V such that χ does not produce a monochromatic


red copy of K6(4) and does not produce a monochromatic blue copy of K32(4)n5. This would imply the desired lower bound for r4(6,n). For v1 < v2 < v3 < v4 and δi = δ(vi,vi+1), we set χ(v1,v2,v3,v4) = red if

- (a) δ1,δ2,δ3 forms a monotone sequence and the triple (δ1,δ2,δ3) is bad, that is, φ(δ1,δ2) = φ(δ2,δ3) = blue and φ(δ1,δ3) = red, or
- (b) δ1 < δ2 > δ3 and δ1 = δ3, or
- (c) δ1 < δ2 > δ3, δ1 = δ3, and the set {δ1,δ2,δ3} is monochromatic with respect to φ, or
- (d) δ1 > δ2 < δ3, δ1 < δ3, and φ(δ3,δ1) = φ(δ3,δ2) and φ(δ1,δ2) = φ(δ3,δ1).


- See Figure 1 for small examples. Otherwise, χ(v1,v2,v3,v4) = blue.


For the sake of contradiction, suppose that the coloring χ produces a red K6(4) on vertices v1 < ··· < v6, and let δi = δ(vi,vi+1), 1 ≤ i ≤ 5. Let us ﬁrst consider the following cases for δ1,... ,δ4, which corresponds to the vertices, v1,... ,v5.

- Case 1. Suppose that δ1,... ,δ4 forms a monotone sequence. If δ1 > ··· > δ4, then we have φ(δ1,δ3) = red since χ(v1,v2,v3,v4) = red. However, this implies that χ(v1,v3,v4,v5) = blue since δ(v1,v3) = δ1 by Property II, contradiction. A similar argument follows if δ1 < ··· < δ4.
- Case 2. Suppose δ1 > δ2 > δ3 < δ4. By Property III, δ4 = δ2,δ1. Since δ1 > δ2 > δ3, this implies that φ(δ1,δ2) = φ(δ2,δ3) = blue and φ(δ1,δ3) = red. Since δ(v2,v4) = δ2 and χ(v1,v2,v4,v5) = red, we have δ4 > δ1. Hence φ(δ4,δ3) = φ(δ4,δ2) = red. However, since δ(v1,v3) = δ1 by Property

II, we have χ(v1,v3,v4,v5) is blue, contradiction.

- Case 3. Suppose δ1 < δ2 < δ3 > δ4. This implies that φ(δ1,δ2) = φ(δ2,δ3) = blue and φ(δ1,δ3) = red. Suppose δ4 = δ2. Since δ(v1,v3) = δ2 and δ2 < δ3 > δ4, this implies the triple (δ1,δ2,δ4) forms a monochromatic blue set with respect to φ, which is a contradiction. A similar argument follows in the case that δ4 = δ1. So we can assume δ4 = δ1,δ2. Since χ(v2,v3,v4,v5) = red, the triple {δ2,δ3,δ4} forms a monochromatic blue set with respect to φ. By Property II we have δ(v2,v4) = δ3 and δ1 < δ(v2,v4) > δ4. This implies that χ(v1,v2,v4,v5) = blue, contradiction
- Case 4. Suppose δ1 < δ2 > δ3 > δ4. This implies that φ(δ2,δ3) = φ(δ3,δ4) = blue and φ(δ2,δ4) = red. Suppose δ1 = δ3. By Property II, we have δ(v2,v4) = δ2. However, χ(v1,v2,v4,v5) = red and δ1 < δ2 > δ4 implies that the triple (δ1,δ2,δ4) must form a monochromatic set with respect to φ, contradiction. A similar argument follows if δ1 = δ4. Therefore, we can assume that δ1 = δ3,δ4. Since χ(v1,v2,v3,v4) = red, the triple (δ1,δ2,δ3) forms a monochromatic blue set with respect to φ. By Property II we have δ(v2,v4) = δ2 and δ1 < δ(v2,v4) > δ4. This implies χ(v1,v2,v4,v5) = blue, contradiction.
- Case 5. Suppose δ1 > δ2 < δ3 < δ4. Note that by Property III, δ1 = δ3,δ4. Since δ1,δ2,δ3 forms a monotone sequence, this implies that φ(δ2,δ3) = φ(δ3,δ4) = blue and φ(δ2,δ4) = red. Moreover, we must have δ1 < δ3 since χ(v1,v2,v3,v4) = red. Hence φ(δ3,δ1) = blue and φ(δ1,δ2) = red. However, since δ(v3,v5) = δ4, we have δ1 > δ2 < δ(v3,v5) and χ(v1,v2,v3,v5) = blue, contradiction.
- Case 6. Suppose δ1 < δ2 > δ3 < δ4. Then we must also have δ4 > δ2 since χ(v2,v3,v4,v5) = red. By Property II, δ(v3,v5) = δ4 and we have δ1 < δ2 < δ(v3,v5). Since χ(v1,v2,v3,v5) = red, we have


- φ(δ1,δ2) = φ(δ2,δ4) = blue and φ(δ1,δ4) = red. Since χ(v1,v2,v3,v4) = red, the triple (δ1,δ2,δ3) forms a monochromatic blue set. However, this implies that χ(v2,v3,v4,v5) = blue, contradiction.


Now if v1,... ,v5 and δ1,... ,δ4 does not fall into one of the 6 cases above, then we must have δ1 > δ2 < δ3 > δ4. However, this implies that v2,... ,v6 and δ2,... ,δ5 does fall into one of the 6 cases above, which implies our contradiction. Therefore, χ does not produce a monochromatic red

copy of K6(4) in our 4-uniform hypergraph.

Next we show that there is no blue Km(4) in coloring χ, where m = 32n5. For the sake of contradiction, suppose we have vertices v1,... ,vm ∈ V such that v1 < ··· < vm, and χ colors every 4-tuple in the set {v1,... ,vm} blue. Let δi = δ(vi,vi+1) for 1 ≤ i ≤ m − 1.

Set δ1∗ = max{δ1,... ,δm}, where δ1∗ = δ(vi1,vi1+1). Set

V1 = {v1,v2,... ,vi1} and V2 = {vi1+1,vi1+2,... ,vm}. Now we establish the following lemma.

- Lemma 3.2. For any W ⊂ {v1,... ,vm}, where W = W1 ∪ W2 is a partition of W described as above, either |W1| < m/2n or |W2| < m/2n. In particular, either |V1| < m/2n or |V2| < m/2n.

Before we prove Lemma 3.2, let us ﬁnish the argument that χ does not color every 4-tuple in the set {v1,... ,vm} blue via the following lemma which will also be used later in the paper.

- Lemma 3.3. If Lemma 3.2 holds, then χ colors a 4-tuple in the set {v1,... ,vm} red.


Proof. We greedily construct a set Dt = {δ1∗,δ2∗,... ,δt∗} ⊂ {δ1,δ2,... ,δm} and a set St ⊂ {v1,... ,vm} such that the following holds.

- 1. We have δ1∗ > ··· > δt∗, where δj∗ = δ(vij,vij+1).
- 2. The indices of the vertices in St are consecutive, that is, St = {vr,vr+1,... ,vs−1,vs} for 1 ≤ r < s ≤ n. Moreover, δt∗ > max{δr,δr+1,... ,δs−1}.
- 3. |St| > m − tm/2n.
- 4. For each δj∗ = δ(vij,vij+1) ∈ Dt, consider the set of vertices S = {vij+1,vij+1+1,vij+2,vij+2+1 ... ,vit,vit+1} ∪ St.


Then either every element in S is greater than vij or every element in S is less than vij+1. In the former case we will label δj∗ white, in the latter case we label it black.

We start with the D0 = ∅ and S0 = {v1,... ,vm}. Having obtained Dt−1 = {δ1∗,... ,δt∗−1} and St−1 = {vr,... ,vs}, where 1 ≤ r < s ≤ n, we construct Dt and St as follows. Let δt∗ = δ(vit,vit+1) be the unique largest element in {δr,δr+1,... ,δs−1}, and set Dt = Dt−1 ∪ δt∗. The uniqueness of δt∗ follows from Properties I and II. We partition St−1 = T1 ∪ T2, where T1 = {vr,vr+1,... ,vit} and T2 = {vit+1,vit+2,... ,vs}. By Lemma 3.2, either |T1| < m/2n or |T2| < m/2n. If |T1| < m/2n, we set St = T2 and label δt∗ white. Likewise, if |T2| < m/2n, we set St = T1 and label δt∗ black. By induction, we have

|St| > |St−1| − m/2n ≥ (m − (t − 1)m/2n) − m/2n = m − tm/2n.

- Since |S0| = m and |St| ≥ 1 for t = 2n, we can construct D2n = {δ1∗,... ,δ2∗n} with the desired properties. By the pigeonhole principle, there are at least n elements in D2n with the same label, say white. The other case will follow by a symmetric argument. We remove all black labeled


elements in D2n, and let {δj∗

,... ,δj∗

} be the resulting set.

does not color every 4-tuple in V = {v1,... ,vm} blue, which completes the proof of Lemma 3.3. Now let us go back and prove Lemma 3.2. First, we make the following observation.

![image 13](<2017-mubayi-new-lower-bounds-hypergraph_images/imageFile13.png>)

![image 14](<2017-mubayi-new-lower-bounds-hypergraph_images/imageFile14.png>)

![image 15](<2017-mubayi-new-lower-bounds-hypergraph_images/imageFile15.png>)

![image 16](<2017-mubayi-new-lower-bounds-hypergraph_images/imageFile16.png>)

- Observation 3.4. Let v1 < ··· < vm ∈ V such that χ colors every 4-tuple in the set {v1,... ,vm} blue. Then for δi = δ(vi,vi+1), δi = δj for 1 ≤ i < j < m.


Proof. For the sake of contradiction, suppose δi = δj for i = j. By Property I, j = i + 1. Without loss of generality, we can assume that for all r such that i < r < j, δr = δi. Set δr = max{δi+1,δi+2,... ,δj−1}, and notice that δ(vi+1,vj) = δr by Property II. Now if δr > δi = δj, then χ(vi,vi+1,vj,vj+1) = red and we have a contradiction. If δr < δi, then this would contradict Property III. Hence, the statement follows.

![image 17](<2017-mubayi-new-lower-bounds-hypergraph_images/imageFile17.png>)

![image 18](<2017-mubayi-new-lower-bounds-hypergraph_images/imageFile18.png>)

![image 19](<2017-mubayi-new-lower-bounds-hypergraph_images/imageFile19.png>)

![image 20](<2017-mubayi-new-lower-bounds-hypergraph_images/imageFile20.png>)

- Proof of Lemma 3.2. It suﬃces to show that the statement holds when W1 = V1 and W2 = V2. For the sake of contradiction, suppose |V1|,|V2| ≥ m/2n = 16n4. Recall that δ1∗ = δ(vi1,vi1+1), V1 = {v1,v2,... ,vi1}, V2 = {vi1+1,vi1+1,... ,vm}, and set A1 = {δ1,... ,δi1−1} and A2 = {δi1+1,... ,δm−1}. For i ∈ {1,2}, let us partition Ai = Ari ∪ Abi where


Ari = {δj ∈ Ai : φ(δ1∗,δj) = red} and Abi = {δj ∈ Ai : φ(δ1∗,δj) = blue}.

By the pigeonhole principle, either |Ab2| ≥ 8n4 or |Ar2| ≥ 8n4. Without loss of generality, we can assume that |Ab2| ≥ 8n4 since a symmetric argument would follow otherwise.

Fix δj1 ∈ Ab1 and δj2 ∈ Ab2, and recall that δj1 = δ(vj1,vj1+1) and δj2 = δ(vj2,vj2+1). By Observation 3.4, δj1 = δj2, and by Property II, we have δ(vj1+1,vj2) = δ1∗. Since χ(vj1,vj1+1,vj2,vj2+1) = blue, this implies that φ(δj1,δj2) = red. By Lemma 3.1 and Observation 3.4, we have |Ab1| < n. Indeed, otherwise we would have a monochromatic red copy of Kn,n in A with respect to φ. Therefore we have |Ar1| ≥ 16n4 − n − 1. Again by the pigeonhole principle, there is a subset B ⊂ Ar1 of size at least (16n4 − n − 1)/n ≥ 8n3 − 1, such that B = {δj,δj+1,... ,δj+8n3−2}, and whose corresponding vertices are U = {vj,vj+1,... ,vj+8n3−1}. For simplicity and without loss of generality, let us rename U = {u1,... ,u8n3} and δi = δ(ui,ui+1) for 1 ≤ i ≤ 8n3 − 1.

Just as before, we greedily construct a set Dt = {δ1∗,... ,δt∗} ⊂ δ1∗ ∪ {δ1,... ,δ8n3−1} and a set St ⊂ {u1,... ,u8n3} such that the following holds.

- 1. We have δ1∗ > ··· > δt∗, where δj∗ = δ(uij,uij+1) for i ≥ 2.
- 2. For each δj∗ = δ(uij,uij+1) ∈ Dt, consider the set of vertices S = {uij+1,uij+1+1,... ,uih,uih+1} ∪ St.

Then either every element in S is greater than uij or every element in S is less than uij+1. In the former case we will label δi∗

j

white, in the latter case we label it black.

- 3. The indices of the vertices in St are consecutive, that is, St = {ur,ur+1,... ,us−1,us} for 1 ≤ r < s ≤ n. Set Bt = {δr,δr+1,... ,δus−1}.


- 4. for each δj∗ ∈ Dt, either φ(δj∗,δ) = red for every δ ∈ {δj∗+1,δj∗+2,... ,δt∗} ∪ Bt, or φ(δj∗,δ) = blue for every δ ∈ {δj∗+1,δj∗+2,... ,δt∗} ∪ Bt.
- 5. We have |St| ≥ 8n3 − (t − 1)2n2.


We start with S1 = U = {u1,... ,u8n3} and D1 = {δ1∗}, where we recall that δ1∗ = δ(vi1,vi1+1). Having obtained Dt−1 = {δ1∗,... ,δt∗−1} and St−1 = {ur,... ,us}, 1 ≤ r < s ≤ n, we construct Dt and St as follows. Let δt∗ = δ(uit,uit+1) be the unique largest element in {δr,δr+1,... ,δs−1}, and set Dt = Dt−1 ∪ δt∗. The uniqueness of δt∗ follows from Properties I and II. Let us partition St = T1 ∪ T2, where T1 = {ur,ur+1,... ,uit} and T2 = {uit+1,uih+1+2,... ,us}. Now we make the following observation.

- Observation 3.5. We have |T1| < 2n2 or |T2| < 2n2.


Proof. For the sake of contradiction, suppose |T1|,|T2| ≥ 2n2 and let B1 = {δr,δr+1,... ,δit−1} and

- B2 = {δi1+1,δit+2,... ,δs−1}. Notice that for every δ ∈ B2 we have φ(δt∗,δ) = red. Indeed, suppose for δ = δ(uℓ,uℓ+1) ∈ B2 we have φ(δt∗,δ) = blue. Recall δ1∗ = δ(vi1,vi1+1), δt∗ = δ(uit,uit+1), where


uit < uit+1 < uℓ < uℓ+1 < vi1 < vi1+1.

Consider the vertices vi1+1,uit,uℓ,uℓ+1. By deﬁnition of χ, we have χ(uit,uℓ,uℓ+1,vi1+1) = red, contradiction. Therefore, by the same argument as above, there are less than n elements δ ∈ B1 such that φ(δt∗,δ) = red. Since |T1| > 2n2, by the pigeonhole principle, there is a set of n + 1 consecutive vertices {uℓ,uℓ+1,... ,uℓ+n} ⊂ T1 and the subset {δℓ,δℓ+1,... ,δℓ+n−1} ⊂ B1 such that φ(δt∗,δ) = blue for every δ ∈ {δℓ,δℓ+1,... ,δℓ+n−1}. Notice that

δℓ < δℓ+1 < ··· < δℓ+n−1.

Indeed, suppose δr > δr+1 for some r ∈ {ℓ,ℓ + 1,... ,ℓ + n − 2}. Then φ(δr,δr+1) = red implies that χ(uit+1,ur,ur+1,ur+2) = red, contradiction. Likewise if φ(δr,δr+1) = blue, then χ(vi1+1,ur,ur+1,ur+2) = red, contradiction. However, by Lemma 3.1, there is a bad triple in {δℓ,δℓ+1,... ,δℓ+n−1} with respect to φ. Since δℓ,δℓ+1,... ,δℓ+n−1 forms a monotone sequence, by Property IV, χ colors some 4-tuple in the set {uℓ,uℓ+1,... ,uℓ+n} red, contradiction. Hence the statement follows.

![image 21](<2017-mubayi-new-lower-bounds-hypergraph_images/imageFile21.png>)

![image 22](<2017-mubayi-new-lower-bounds-hypergraph_images/imageFile22.png>)

![image 23](<2017-mubayi-new-lower-bounds-hypergraph_images/imageFile23.png>)

![image 24](<2017-mubayi-new-lower-bounds-hypergraph_images/imageFile24.png>)

If |T1| < 2n2, we set St = T2. Otherwise by Observation 3.5 we have |T2| < 2n2 and we set St = T1. Hence |St| > |St−1| − 2n2.

- Since |S1| = |U| = 8n3, we have |St| > 0 for t = 2n. Therefore, we can construct D2n = {δ1∗,... ,δ2∗n} with the desired properties. By the pigeonhole principle, at least n elements in D2n have the same label, say white. The other case will follow by a symmetric argument. We remove all black labeled


} be the resulting set, and for simplicity, let δj∗

elements in D2n, and let {δj∗

,... ,δj∗

= δ(vjr,vjr+1).

r

does not color every 4-tuple in V = {v1,... ,vm} blue which is a contradiction.

![image 25](<2017-mubayi-new-lower-bounds-hypergraph_images/imageFile25.png>)

![image 26](<2017-mubayi-new-lower-bounds-hypergraph_images/imageFile26.png>)

![image 27](<2017-mubayi-new-lower-bounds-hypergraph_images/imageFile27.png>)

![image 28](<2017-mubayi-new-lower-bounds-hypergraph_images/imageFile28.png>)

# 4 A new lower bound for r4(5, n)

Again we apply a variant to the Erd˝os-Hajnal stepping up lemma in order to establish a new lower bound for r4(5,n). We will use the following lemma.

- Lemma 4.1. For n ≥ 5, there is an absolute constant c > 0 such that the following holds. For N = ⌊nclogn⌋, there is a red/blue coloring φ on the pairs of {0,1,... ,N − 1} such that


- 1. there is no monochromatic red copy of K⌊logn⌋,
- 2. there are no two disjoint n-sets A,B ⊂ {0,1,... ,N − 1}, such that φ(a,b) = blue for every a ∈ A and b ∈ B (i.e. no blue Kn,n).
- 3. there is no n-set A ⊂ {0,1,... ,N−1} such that every triple ai,aj,ak ∈ A, where ai < aj < ak, avoids the pattern φ(ai,aj) = φ(aj,ak) = blue and φ(ai,ak) = red.


We omit the proof of Lemma 4.1, which follows by the same probabilistic argument used for

- Lemma 3.1. For the reader’s convenience, let us restate the result that we are about to prove. Theorem 4.2. For n ≥ 5, there is an absolute constant c > 0 such that r4(5,n) > 2nclogn.


Proof. Let c > 0 be the constant from Lemma 4.1, and set A = {0,1,... ,⌊nclogn⌋ − 1}. Let φ be the red/blue coloring on the pairs of A with the properties described in Lemma 4.1. Set N = 2⌊nclogn⌋ and let V = {0,1,... ,N − 1}. In what follows, we will use φ to deﬁne a red/blue coloring χ : V4 → {red, blue} of the 4-tuples of V such that χ does not produce a monochromatic red K5(4), and does not produce a monochromatic blue copy of K2(4)n4. This would imply the desired lower bound for r4(5,n).

clog n⌋−1

Just as in the previous section, for any v ∈ V , we write v = ⌊n

i=0 v(i)2i with v(i) ∈ {0,1} for each i. For u = v, set δ(u,v) ∈ A denote the largest i for which u(i) = v(i). Let v1,v2,v3,v4 ∈ V such that v1 < v2 < v3 < v4 and set δi = δ(vi,vi+1). We deﬁne χ(v1,v2,v3,v4) = red if

- (a) δ1,δ2,δ3 is monotone and φ(δ1,δ2) = φ(δ2,δ3) = blue and φ(δ1,δ3) = red, or
- (b) δ1 < δ2 > δ3 and δ1 = δ3, or
- (c) δ1 < δ2 > δ3, δ1 = δ3, and φ(δ1,δ2) = φ(δ2,δ3) = blue and φ(δ1,δ3) = red, or
- (d) δ1 > δ2 < δ3, δ1 < δ3, and φ(δ1,δ3) = φ(δ2,δ3) = red and φ(δ1,δ2) = blue, or
- (e) δ1 > δ2 < δ3, δ1 > δ3, and φ(δ1,δ3) = φ(δ1,δ2) = red and φ(δ2,δ3) = blue.


δ1 δ2 δ3

v1: 0 0 0

v2: 1 0 0

v3: 1 1 0

v4: 1 1 1

δ3 δ2 δ1

0 0 0

0 0 1

0 1 0

1 0 0

(a)

δ2 δ1=δ3

0 0

0 1

1 0

1 1

δ2 δ3 δ1

0 1 0

0 1 1

1 0 0

1 1 0

δ2 δ1 δ3

0 0 0

0 1 0

1 0 0

1 0 1

(b)

(c)

δ3 δ1 δ2

0 0 1

0 1 0

0 1 1

1 0 0

(d)

δ1 δ3 δ2

0 0 1

1 0 0

1 0 1

1 1 0

(e)

- Figure 2: Examples of v1 < v2 < v3 < v4 and δ1 = δ(v1,v2),δ2 = δ(v2,v3),δ3 = δ(v3,v4), such that χ(v1,v2,v3,v4) = red. For each case, vi is represented in binary form with the left-most entry being the most signiﬁcant bit.


- See Figure 2 for small examples. Otherwise, χ(v1,v2,v3,v4) = blue.


For the sake of contradiction, suppose that the coloring χ produces a red K5(4) on vertices v1 < ··· < v5, and let δi = δ(vi,vi+1), 1 ≤ i ≤ 4. The proof now falls into the following cases, similar to the previous section.

- Case 1. Suppose that δ1,... ,δ4 forms a monotone sequence. If δ1 > ··· > δ4, then we have

φ(δ1,δ3) = red since χ(v1,v2,v3,v4) = red. However, this implies that χ(v1,v3,v4,v5) = blue since

- δ(v1,v3) = δ1 by Property II, contradiction. A similar argument follows if δ1 < ··· < δ4.


- Case 2. Suppose δ1 > δ2 > δ3 < δ4. By Property III, δ4 = δ2,δ1. Since δ1 > δ2 > δ3, this implies that φ(δ1,δ2) = φ(δ2,δ3) = blue and φ(δ1,δ3) = red. Now consider the following subcases for δ4.

- Case 2.a. Suppose δ4 > δ1. By Property II, δ(v2,v4) = δ2. Since χ(v1,v2,v4,v5) = red, this implies that φ(δ4,δ1) = φ(δ4,δ2) = red. However, since δ1 = δ(v1,v3), this implies χ(v1,v3,v4,v5) = blue, contradiction.
- Case 2.b. Suppose δ2 < δ4 < δ1. Since χ(v2,v3,v4,v5) = red, we have φ(δ4,δ2) = φ(δ4,δ3) = red. However, this implies that χ(v1,v2,v4,v5) = blue since δ(v2,v4) = δ2, contradiction.
- Case 2.c. Suppose δ3 < δ4 < δ2. Then this would imply χ(v2,v3,v4,v5) = blue, contradiction.


- Case 3. Suppose δ1 < δ2 < δ3 > δ4. This implies that φ(δ1,δ2) = φ(δ2,δ3) = blue and φ(δ1,δ3) = red. Hence we have δ4 = δ1,δ2. Since δ(v2,v4) = δ3, we have χ(v1,v2,v4,v5) = blue, contradiction.
- Case 4. Suppose δ1 < δ2 > δ3 > δ4. This implies that φ(δ2,δ3) = φ(δ3,δ4) = blue and φ(δ2,δ4) = red. Hence we have δ1 = δ3,δ4. Since δ(v2,v4) = δ2, we have χ(v1,v2,v4,v5) = blue, contradiction.
- Case 5. Suppose δ1 > δ2 < δ3 < δ4. Note that by Property III, δ1 = δ3,δ4. Since δ2,δ3,δ4 forms a monotone sequence, this implies that φ(δ2,δ3) = φ(δ3,δ4) = blue and φ(δ2,δ4) = red. Now we consider the following subcases for δ1.


- Case 5.a. Suppose δ2 < δ1 < δ3. Then we have χ(v1,v2,v3,v4) = blue which is a contradiction.


- Case 5.b. Suppose δ3 < δ1 < δ4. Then we have φ(δ1,δ3) = φ(δ1,δ2) = red. Notice that δ(v2,v4) = δ3 by Property II. Therefore χ(v1,v2,v4,v5) = blue, contradiction.
- Case 5.c. Suppose δ1 > δ4. Then we have φ(δ1,δ3) = φ(δ1,δ2) = red. By Property II, δ(v3,v5) = δ4 which implies χ(v1,v2,v3,v5) = blue, contradiction.


- Case 6. Suppose δ1 < δ2 > δ3 < δ4. Then χ(v1,v2,v3,v4) = red implies that φ(δ2,δ1) = φ(δ2,δ3) =

- blue and φ(δ1,δ3) = red. Now if δ2 < δ4, χ(v2,v3,v4,v5) = red implies that φ(δ4,δ2) = φ(δ4,δ3) = red. By Property II, we have δ(v2,v4) = δ2, and therefore δ1 < δ2 < δ4. However, this implies χ(v1,v2,v4,v5) = blue, contradiction. Now if δ4 < δ2, then χ(v2,v3,v4,v5) = blue, which is again a contradiction.

Case 7. Suppose δ1 > δ2 < δ3 > δ4. Then χ(v2,v3,v4,v5) = red implies that φ(δ3,δ2) = φ(δ3,δ4) =

- blue and φ(δ2,δ4) = red. Now if δ1 < δ3, then χ(v1,v2,v3,v4) = blue which is a contradiction. Therefore we can assume that δ1 > δ3. Since χ(v1,v2,v3,v4) = red we have φ(δ1,δ3) = red. By Property II, δ(v1,v3) = δ1 and δ1 > δ3 > δ4. This implies that χ(v1,v3,v4,v5) = blue which is a contradiction.




Next we show that there is no blue Km(4) in coloring χ, where m = 2n4. We will prove this statement via the following claims.

- Claim 4.3. There do not exist vertices w1 < ··· < wn in V such that φ(δ(wi,wj),δ(wj,wk)) = red for every i < j < k.

Proof. Suppose for contradiction that these vertices w1 < ··· < wn exist. Let δi = δ(wi,wi+1) and set δi1 = maxi δi. Let W = {wi : i ≤ i1} and W′ = {wi : i > i1}. By the pigeonhole principle, either |W| ≥ n/2 or |W′| ≥ n/2. Assume without loss of generality that |W| ≥ n/2 and set W1 = W. Observe that by hypothesis and deﬁnition of δi1, for every wi,wj ∈ W1, with i < j, we have

φ(δ(wi,wj),δi1) = φ(δ(wi,wj),δ(wj,wi1+1)) = red. Note that we obtain the same conclusion if |W′| ≥ n/2 and W1 = W′ since

φ(δi1,δ(wi,wj)) = φ(δ(wi1,wi),δ(wi,wj)) = red.

Now deﬁne δi2 = maxi<i1 δi and repeat the argument above to obtain W2 with |W2| ≥ n/4 such that φ(δ(wi,wj),δi2) = red for every wi,wj ∈ W2, with i < j. Continuing in this way, we obtain

- δi1,δi2,... ,δim for m = ⌊log n⌋, such that φ colors every pair in the set {δi1,δi2,... ,δim} red. This contradicts Lemma 4.1, and the statement follows.


![image 29](<2017-mubayi-new-lower-bounds-hypergraph_images/imageFile29.png>)

![image 30](<2017-mubayi-new-lower-bounds-hypergraph_images/imageFile30.png>)

![image 31](<2017-mubayi-new-lower-bounds-hypergraph_images/imageFile31.png>)

![image 32](<2017-mubayi-new-lower-bounds-hypergraph_images/imageFile32.png>)

- Claim 4.4. There do not exist vertices w1 < ··· < wn2 in V such that every 4-tuple among them is blue under χ and for every i < j < k with δ(wi,wj) > δ(wj,wk) we have φ(δ(wi,wj),δ(wj,wk)) = red.


Proof. Suppose for contradiction that these vertices w1 < ··· < wn2 exist. Let δi = δ(wi,wi+1) and set δi1 = maxi δi. Let W = {wi : i ≤ i1} and W′ = {wi : i > i1}. Let us ﬁrst suppose that |W′| ≥ n. Pick wi,wj,wk ∈ W′ with i < j < k. If δ(wi,wj) > δ(wj,wk), then φ(δ(wi,wj),δ(wj,wk)) = red by assumption. If δ(wi,wj) < δ(wj,wk), then consider the 4-tuple wi1,wi,wj,wk. Since

this 4-tuple is blue under χ, and both φ(δ(wi1,wi),δ(wi,wj)) and φ(δ(wi1,wi),δ(wj,wk)) are red, φ(δ(wi,wj),δ(wj,wk)) must also be red. Now we may apply Claim 4.3 to W′ to obtain a contradiction.

We may therefore assume that |W′| < n and hence |W| ≥ n2−n ≥ (n−1)2. We repeat the previous argument to W to obtain δi2 and then δi3,... ,δin, such that

δi1 > δi2 > ··· > δin and i1 > i2 > ··· > in.

Now consider the set S = {wi1+1,wi2+1,... ,win+1,win}, whose corresponding delta set is A = {δi1,δi2,... ,δin}. Then A is an n-set that has the properties of Lemma 4.1 part 3. This implies that there are j < k < l such that φ(δij,δik) = φ(δik,δil) = blue and φ(δij,δil) = red. Consequently, χ(wij,wik,wil,wil+1) = red, a contradiction.

![image 33](<2017-mubayi-new-lower-bounds-hypergraph_images/imageFile33.png>)

![image 34](<2017-mubayi-new-lower-bounds-hypergraph_images/imageFile34.png>)

![image 35](<2017-mubayi-new-lower-bounds-hypergraph_images/imageFile35.png>)

![image 36](<2017-mubayi-new-lower-bounds-hypergraph_images/imageFile36.png>)

By copying the proof above almost verbatim, we have the following.

- Claim 4.5. There do not exist vertices w1 < ··· < wn2 in V such that every 4-tuple among them is blue under χ and for every i < j < k with δ(wi,wj) < δ(wj,wk) we have φ(δ(wi,wj),δ(wj,wk)) = red.


Now we are ready to show that there is no blue Km(4) in coloring χ, where m = 2n4. For the sake of contradiction, suppose we have vertices v1,... ,vm ∈ V such that v1 < ··· < vm, and χ colors every 4-tuple in the set {v1,... ,vm} blue. Let δi = δ(vi,vi+1) for 1 ≤ i ≤ m − 1. Notice that by Observation 3.4 we have δi = δj for 1 ≤ i < j < m.

Let δ1∗ = max{δ1,... ,δm}, where δ1∗ = δ(vi1,vi1+1). Set

V1 = {v1,v2,... ,vi1} and V2 = {vi1+1,vi1+1,... ,vm}. Now we establish the following lemma.

- Lemma 4.6. We have either |V1| < n3 = m/2n or |V2| < n3 = m/2n.


- Proof of Lemma 4.6. For the sake of contradiction, suppose |V1|,|V2| ≥ n3. Recall that δ1∗ =


- δ(vi1,vi1+1), V1 = {v1,v2,... ,vi1}, V2 = {vi1+1,vi1+1,... ,vm}, and set A1 = {δ1,... ,δi1−1} and A2 = {δi1+1,... ,δm−1}. For i ∈ {1,2}, let us partition Ai = Ari ∪ Abi where


Ari = {δj ∈ Ai : φ(δ1∗,δj) = red} and Abi = {δj ∈ Ai : φ(δ1∗,δj) = blue}.

Let us ﬁrst suppose that |Abi| ≥ n for i = 1,2. Fix δj1 ∈ Ab1 and δj2 ∈ Ab2, and recall that

- δj1 = δ(vj1,vj1+1) and δj2 = δ(vj2,vj2+1). By Observation 3.4, δj1 = δj2, and by Property II, we have δ(vj1+1,vj2) = δ1∗. Since χ(vj1,vj1+1,vj2,vj2+1) = blue, this implies that φ(δj1,δj2) = blue. Consequently, we have a monochromatic blue copy of Kn,n in A with respect to φ, which contradicts Lemma 4.1 part 2.


Therefore we have |Ab1| ≤ n or |Ab2| ≤ n. Let us ﬁrst suppose that |Ab1| ≤ n. Since |A1| ≥ n3, by the pigeonhole principle, there is a subset R ⊂ Ar1 such that R = {δj,δj+1,... ,δj+n2−2}, whose corresponding vertices are U = {vj,vj+1,... ,vj+n2−1}. For simplicity and without loss

of generality, let us rename U = {u1,... ,un2} and δi = δ(ui,ui+1) for 1 ≤ i ≤ n2. Now notice that φ(δ(ui,uj),δ(uj,uk)) = red for every i < j < k with δ(ui,uj) > δ(uj,uk). Indeed, since δ(ui,uj),δ(uj,uk) ∈ R we have φ(δ1∗,δ(ui,uj))) = φ(δ1∗,δ(uj,uk))) = red. Since χ(ui,uj,uk,vi1+1) = blue, this implies that we must have φ(δ(ui,uj),δ(uj,uk)) = red by deﬁnition of χ. However, by Claim 4.4 we obtain a contradiction.

In the case that |Ab2| ≤ n, a symmetric argument follows, where we apply Claim 4.5 instead of Claim 4.4 to obtain the contradiction.

![image 37](<2017-mubayi-new-lower-bounds-hypergraph_images/imageFile37.png>)

![image 38](<2017-mubayi-new-lower-bounds-hypergraph_images/imageFile38.png>)

![image 39](<2017-mubayi-new-lower-bounds-hypergraph_images/imageFile39.png>)

![image 40](<2017-mubayi-new-lower-bounds-hypergraph_images/imageFile40.png>)

Now we can ﬁnish the argument that χ does not color every 4-tuple in the set {v1,... ,vm} blue by copying the proof of Lemma 3.3. In particular, we will obtain vertices vj1 < ··· < vjn+1 ∈ {v1,... ,vm} such that δ(vj1,vj2),δ(vj2,vj3),... ,δ(vjn,vjn+1) forms a monotone sequence. By Property IV and Lemma 4.1, χ will color a 4-tuple in the set {vj1,... ,vjn+1} red.

Acknowledgment. We thank a referee for helpful comments.

# References

- [1] M. Ajtai, J. Komlo´s, E. Szemere´di, A note on Ramsey numbers, J. Combin. Theory Ser. A 29

(1980), 354–360.

- [2] T. Bohman, The triangle-free process, Adv. Math. 221 (2009), 1653–1677.
- [3] T. Bohman, P. Keevash, The early evolution of the H-free process, Invent. Math. 181 (2010), 291–336.
- [4] D. Conlon, A new upper bound for diagonal Ramsey numbers, Ann. Math. 170 (2009), 941– 960.
- [5] D. Conlon, J. Fox, and B. Sudakov, An improved bound for the stepping-up lemma, Discrete Applied Mathematics 161 (2013), 1191–1196.
- [6] D. Conlon, J. Fox, and B. Sudakov, Hypergraph Ramsey numbers, J. Amer. Math. Soc. 23

(2010), 247–266.

- [7] D. Conlon, J. Fox, B. Sudakov, personal communication.
- [8] P. Erd˝os, Some remarks on the theory of graphs, Bull. Amer. Math. Soc. 53 (1947), 292–294.
- [9] P. Erd˝os, A. Hajnal, On Ramsey like theorems, problems and results, in Combinatorics (Proc. Conf. Combinatorial Math., Math. Inst., Oxford, 1972), pp. 123–140, Inst. Math. Appl., Southhend-on-Sea, 1972.
- [10] P. Erd˝os, A. Hajnal, R. Rado, Partition relations for cardinal numbers, Acta Math. Acad. Sci. Hungar. 16 (1965), 93–196.
- [11] P. Erd˝os, R. Rado, Combinatorial theorems on classiﬁcations of subsets of a given set, Proc. Lond. Math. Soc. 3 (1952), 417–439.


- [12] P. Erd˝os, G. Szekeres, A combinatorial problem in geometry, Compos. Math. 2 (1935), 463–470.
- [13] R. L. Graham, B. L. Rothschild, J. H. Spencer: Ramsey Theory, 2nd ed., Wiley, New York, 1990.
- [14] J. H. Kim, The Ramsey number R(3,t) has order of magnitude t2/log t, Random Structures Algorithms 7 (1995), 173–207.
- [15] D. Mubayi, A. Suk, Constructions in Ramsey theory, submitted.
- [16] D. Mubayi, A. Suk, Oﬀ-diagonal hypergraph Ramsey numbers, J. Combin. Theory Ser. B 125, (2017), 168–177.
- [17] D. Mubayi, A. Suk, The Erdos-Hajnal hypergraph Ramsey problem, submitted.
- [18] J. Spencer, Ramsey’s theorem - a new lower bound, J. Combin. Theory Ser. A 18, 108–115.


