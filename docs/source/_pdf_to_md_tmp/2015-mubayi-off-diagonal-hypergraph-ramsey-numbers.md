arXiv:1505.05767v2[math.CO]29May2015

Oﬀ-diagonal hypergraph Ramsey numbers

Dhruv Mubayi∗ Andrew Suk†

Abstract

The Ramsey number rk(s,n) is the minimum N such that every red-blue coloring of the k-subsets of {1,...,N} contains a red set of size s or a blue set of size n, where a set is red (blue) if all of its k-subsets are red (blue). A k-uniform tight path of size s, denoted by Ps, is a set of s vertices v1 < ··· < vs in Z, and all s−k+1 edges of the form {vj,vj+1,...,vj+k−1}. Let rk(Ps,n) be the minimum N such that every red-blue coloring of the k-subsets of {1,...,N} results in a red Ps or a blue set of size n. The problem of estimating both rk(s,n) and rk(Ps,n) for k = 2 goes back to the seminal work of Erdo˝s and Szekeres from 1935, while the case k ≥ 3 was ﬁrst investigated by Erdo˝s and Rado in 1952.

In this paper, we deduce a quantitative relationship between multicolor variants of rk(Ps,n) and rk(n,n). This yields several consequences including the following:

- • We determine the correct tower growth rate for both rk(s,n) and rk(Ps,n) for s ≥ k + 3. The question of determining the tower growth rate of rk(s,n) for all s ≥ k + 1 was posed by Erdo˝s and Hajnal in 1972.
- • We show that determining the tower growth rate of rk(Pk+1,n) is equivalent to determining the tower growth rate of rk(n,n), which is a notorious conjecture of Erdo˝s, Hajnal and Rado from 1965 that remains open.


Some related oﬀ-diagonal hypergraph Ramsey problems are also explored.

# 1 Introduction

A k-uniform hypergraph H with vertex set V is a collection of k-element subsets of V . We write Kn(k) for the complete k-uniform hypergraph on an n-element vertex set. The Ramsey number rk(s,n) is the minimum N such that every red-blue coloring of the edges of KN(k) contains a monochromatic red copy of Ks(k) or a monochromatic blue copy of Kn(k). Due to its wide range of applications in logic, number theory, analysis, geometry, and computer science, estimating Ramsey numbers has become one of the most central problems in combinatorics.

![image 1](<2015-mubayi-off-diagonal-hypergraph-ramsey-numbers_images/imageFile1.png>)

∗Department of Mathematics, Statistics, and Computer Science, University of Illinois, Chicago, IL, 60607 USA. Research partially supported by NSF grant DMS-1300138. Email: mubayi@uic.edu

†Department of Mathematics, Statistics, and Computer Science, University of Illinois, Chicago, IL, 60607 USA. Supported by NSF grant DMS-1500153. Email: suk@uic.edu.

## 1.1 Diagonal Ramsey numbers.

The diagonal Ramsey number, rk(n,n) where k is ﬁxed and n tends to inﬁnity, has been studied extensively over the past 80 years. Classic results of Erd˝os and Szekeres [16] and Erd˝os [12] imply that 2n/2 < r2(n,n) ≤ 22n for every integer n > 2. These bounds have been improved by various authors (see [5, 25, 17]). However, the constant factors in the exponents have not changed over the last 70 years. For 3-uniform hypergraphs, a result of Erd˝os, Hajnal, and Rado [14] gives the best known lower and upper bounds for r3(n,n) which are of the form1 2Ω(n2) < r3(n,n) ≤ 22O(n). For k ≥ 4, there is also a diﬀerence of one exponential between the known lower and upper bounds for rk(n,n), that is,

twrk−1(Ω(n2)) ≤ rk(n,n) ≤ twrk(O(n)),

where the tower function twrk(x) is deﬁned by twr1(x) = x and twri+1 = 2twri(x) (see [16, 15, 13]). A notoriously diﬃcult conjecture of Erd˝os, Hajnal, and Rado states the following (Erd˝os oﬀered $500 for a proof).

- Conjecture 1.1. (Erdo˝s-Hajnal-Rado [14]) For k ≥ 3 ﬁxed, rk(n,n) ≥ twrk(Ω(n)).


The study of r3(n,n) may be particularly important for our understanding of hypergraph Ramsey numbers. Any improvement on the lower bound for r3(n,n) can be used with a result of Erd˝os and Hajnal [13], known as the stepping-up lemma, to obtain improved lower bounds for rk(n,n), for all k ≥ 4. In particular, proving that r3(n,n) grows at least double exponential in Ω(n), would imply that rk(n,n) does indeed grow as a tower of height k in Ω(n), settling Conjecture 1.1. In the other direction, any improvement on the upper bound for r3(n,n) can be used with a result of Erd˝os and Rado [15], to obtain improved upper bounds for rk(n,n), for all k ≥ 4. It is widely believed that Conjecture 1.1 is true, based on the fact that such bounds are known for four colors. More precisely, the q-color Ramsey number,

)

rk(n,... ,n

![image 2](<2015-mubayi-off-diagonal-hypergraph-ramsey-numbers_images/imageFile2.png>)

![image 3](<2015-mubayi-off-diagonal-hypergraph-ramsey-numbers_images/imageFile3.png>)

q times

is the minimum N such that every q-coloring of the edges of the complete N-vertex k-uniform hypergraph KN(k), contains a monochromatic copy of Kn(k). A result of Erd˝os and Hajnal [13] shows that r3(n,n,n,n) > 22Ω(n), and this implies that

rk(n,n,n,n) = twrk(Θ(n)), for all ﬁxed k ≥ 4. For three colors, Conlon, Fox, and Sudakov [7] showed that for ﬁxed k ≥ 3, rk(n,n,n) ≥ twrk(Ω(log2 n)).

![image 4](<2015-mubayi-off-diagonal-hypergraph-ramsey-numbers_images/imageFile4.png>)

1We write f(n) = O(g(n)) if |f(n)| ≤ c|g(n)| for some ﬁxed constant c and for all n ≥ 1; f(n) = Ω(g(n)) if g(n) = O(f(n)); and f(n) = Θ(g(n)) if both f(n) = O(g(n)) and f(n) = Ω(g(n)) hold. We write f(n) = o(g(n)) if for every positive ǫ > 0 there exists a constant n0 such that f(n) ≤ ǫ|g(n)| for all n ≥ n0.

## 1.2 Oﬀ-diagonal Ramsey numbers.

The oﬀ-diagonal Ramsey number, rk(s,n) with k,s ﬁxed and n tending to inﬁnity, has also been extensively studied. It is known [2, 19, 3, 4] that r2(3,n) = Θ(n2/log n) and, for ﬁxed s > 3,

c1

n log n

![image 5](<2015-mubayi-off-diagonal-hypergraph-ramsey-numbers_images/imageFile5.png>)

s+1 2

ns−1 logs−2 n

![image 6](<2015-mubayi-off-diagonal-hypergraph-ramsey-numbers_images/imageFile6.png>)

≤ r2(s,n) ≤ c2

,

![image 7](<2015-mubayi-off-diagonal-hypergraph-ramsey-numbers_images/imageFile7.png>)

where c1 and c2 are absolute constants. For 3-uniform hypergraphs, a result of Conlon, Fox, and Sudakov [7] shows that for ﬁxed s ≥ 4

2Ω(nlogn) ≤ r3(s,n) ≤ 2ns−2 logn. For ﬁxed s > k ≥ 4, it is known that

rk(s,n) ≤ twrk−1(O(ns−2 log n)). By applying the Erd˝os-Hajnal stepping up lemma in the oﬀ-diagonal setting, it follows that rk(s,n) ≥ twrk−1(Ω(n)), for k ≥ 4 and for all s ≥ 2k−1 − k + 3. In 1972, Erd˝os and Hajnal conjectured the following.

- Conjecture 1.2. (Erdo˝s-Hajnal [13]) For s ≥ k + 1 ≥ 5 ﬁxed, rk(s,n) ≥ twrk−1(Ω(n)).


In [6], Conlon, Fox, and Sudakov modiﬁed the Erd˝os-Hajnal stepping-up lemma to show that Conjecture 1.2 holds for all s ≥ ⌈5k/2⌉ − 3. Using a result of Duﬀus et al. [9] (see also Moshkovitz and Shapira [22] and Milans et al. [21]), one can show that rk(s,n) ≥ twrk−2(Ω(n)) for all s ≥ k+1. In this paper, we prove the following result that nearly settles Conjecture 1.2 by determining the correct tower growth rate for s ≥ k + 3, and obtaining new bounds for the two remaining cases.

- Theorem 1.3. There is a positive constant c > 0 such that the following holds. For k ≥ 4 and n > 3k, we have


- 1. rk(k + 3,n) ≥ twrk−1(cn),
- 2. rk(k + 2,n) ≥ twrk−1(clog2 n),
- 3. rk(k + 1,n) ≥ twrk−2(cn2).


There are two novel ingredients to our constructions. First, we relate these problems to estimates for Ramsey numbers of tight-paths versus cliques, which we ﬁnd of independent interest. Second, we use (k −1)-uniform diagonal Ramsey numbers for more than two colors to obtain constructions for k-uniform oﬀ-diagonal Ramsey numbers for two colors. This diﬀers from the usual paradigm in this area, exempliﬁed by the stepping up lemma, where the number of colors stays the same or goes up as the uniformity increases (see, e.g. [1, 6, 7, 9, 13, 14, 20, 23]). This topic has also been extensively studied in the context of partition relations for ordinals. It is quite possible that our constructions can also be applied to the inﬁnite setting, though we have not explored this here.

After this paper was written, we learned that a bound similar to Theorem 1.3 part (1) was also recently proved by Conlon, Fox, and Sudakov (unpublished), using the more traditional stepping-up argument of Erd˝os and Hajnal.

## 1.3 Tight-path versus clique.

Consider an ordered N-vertex k-uniform hypergraph H, that is, a hypergraph whose vertex set is [N] = {1,2,... ,N}. A tight path of size s in H, denoted by Ps(k), comprises a set of s vertices v1,... ,vs ∈ [N], v1 < ··· < vs, such that (vj,vj+1,... ,vj+k−1) ∈ E(H) for j = 1,2,... ,s − k + 1. The length of Ps(k) is the number of edges, s − k + 1.

Here, we obtain lower and upper bounds for Ramsey numbers for tight-paths versus cliques. To be more precise, we need the following deﬁnition. Given q k-uniform hypergraphs F1,... ,Fq, the Ramsey number r(F1,... ,Fq) is the minimum N such that every q-coloring of the edges of the complete N-vertex k-uniform hypergraph KN(k), whose vertex set is [N] = {1,... ,N}, contains an i-colored copy of Fi for some i. In order to avoid the excessive use of superscripts, we use the simpler notation

rk(Ps,Pn) = r(Ps(k),Pn(k)) and rk(Ps,n) = r(Ps(k),Kn(k)). Two famous theorems of Erd˝os and Szekeres in [16], known as the monotone subsequence theorem and the cups-caps theorem, imply that r2(Ps,Pn) = (n−1)(s−1)+1 and r3(Ps,Pn) = n+s−s−24 +1. Fox, Pach, Sudakov, and Suk [10] later extended their results to k-uniform hypergraphs, and gave a geometric application related to the Happy Ending Theorem.2 See also [9, 22, 21] for related results.

The proof of the Erd˝os-Szekeres monotone subsequence theorem [16] (see also Dilworth’s Theorem [8]) actually implies that r2(Ps,n) = (n − 1)(s − 1) + 1. For k ≥ 3, estimating rk(Ps,n) appears to be more diﬃcult. Clearly we have

rk(Ps,n) ≤ rk(s,n) ≤ twrk−1(O(ns−2 log n)). (1)

Our main result is a new connection between rk(Ps,n) and rk(n,n). Again, we will use the simpler notation

) and rk(Ps1,... ,Pst,n) = r(Ps(1k),... ,Ps(tk),Kn(k)).

rk(n;q) = rk(n,... ,n

![image 8](<2015-mubayi-off-diagonal-hypergraph-ramsey-numbers_images/imageFile8.png>)

![image 9](<2015-mubayi-off-diagonal-hypergraph-ramsey-numbers_images/imageFile9.png>)

q times

- Theorem 1.4. (Main Result) Let k ≥ 2 and s1,... ,st ≥ k+1. Then for q = (s1−k+1)··· (st− k + 1), we have


rk−1(⌊n/q⌋;q) ≤ rk(Ps1,... ,Pst,n) ≤ rk−1(n;q).

Theorem 1.4 has several immediate consequences with t = 1. First, we can considerably improve the upper bound for rk(Ps,n) in (1).

Corollary 1.5. For ﬁxed k ≥ 3 and s ≥ k + 1, we have rk(Ps,n) ≤ twrk−1(O(sn log s)).

![image 10](<2015-mubayi-off-diagonal-hypergraph-ramsey-numbers_images/imageFile10.png>)

2The main result in [16], known as the Happy Ending Theorem, states that for any positive integer n, any suﬃciently large set of points in the plane in general position has a subset of n members that form the vertices of a convex polygon.

Indeed, using the standard Erd˝os-Szekeres recurrence [16], we have r2(n;q) < qnq = twr2(O(qn log q)), and the upper bound argument of Erd˝os-Rado [15] then yields rk−1(n;q) < twrk−1(O(qn log q)). Applying Theorem 1.4 with t = 1,s1 = s, and q = s − k + 1 < s, now implies Corollary 1.5.

Combining the lower bounds in Theorem 1.4 with the known lower bounds for rk−1(n,n,n,n) in [13], rk−1(n,n,n) in [7], and rk−1(n,n) in [13], we establish the following inequalities. There is an absolute constant c > 0 such that for all k ≥ 4 and n > 3k

n 4

n 4

n 4 ≥ twrk−1(cn),

n 4

rk(Pk+3,n) ≥ rk−1

,

,

,

![image 11](<2015-mubayi-off-diagonal-hypergraph-ramsey-numbers_images/imageFile11.png>)

![image 12](<2015-mubayi-off-diagonal-hypergraph-ramsey-numbers_images/imageFile12.png>)

![image 13](<2015-mubayi-off-diagonal-hypergraph-ramsey-numbers_images/imageFile13.png>)

![image 14](<2015-mubayi-off-diagonal-hypergraph-ramsey-numbers_images/imageFile14.png>)

rk(Pk+2,n) ≥ rk−1

n 3

n 3 ≥ twrk−1(clog2 n),

n 3

,

,

![image 15](<2015-mubayi-off-diagonal-hypergraph-ramsey-numbers_images/imageFile15.png>)

![image 16](<2015-mubayi-off-diagonal-hypergraph-ramsey-numbers_images/imageFile16.png>)

![image 17](<2015-mubayi-off-diagonal-hypergraph-ramsey-numbers_images/imageFile17.png>)

n 2

n 2 ≥ twrk−2(cn2).

rk(Pk+1,n) ≥ rk−1

,

![image 18](<2015-mubayi-off-diagonal-hypergraph-ramsey-numbers_images/imageFile18.png>)

![image 19](<2015-mubayi-off-diagonal-hypergraph-ramsey-numbers_images/imageFile19.png>)

Summarizing, we have just proved parts 1–3 of the following theorem, which is a strengthening of Theorem 1.3 as rk(s,n) ≥ rk(Ps,n).

Theorem 1.6. There is a positive constant c > 0 such that r3(P4,n) > 2cn, and for k ≥ 4 and n > 3k,

- 1. rk(Pk+3,n) ≥ twrk−1(cn),
- 2. rk(Pk+2,n) ≥ twrk−1(clog2 n),
- 3. rk(Pk+1,n) ≥ twrk−2(cn2).


We conjecture the following strengthening of the Erd˝os-Hajnal conjecture. Conjecture 1.7. For k ≥ 4 ﬁxed, rk(Pk+1,n) ≥ twrk−1(Ω(n)).

For t = 1, q = 2, and s1 = k+1 in Theorem 1.4, we have rk−1(n/2,n/2) ≤ rk(Pk+1,n) ≤ rk−1(n,n). Hence, we obtain the following corollary which relates rk(Pk+1,n) to the diagonal Ramsey number rk(n,n).

Corollary 1.8. Conjecture 1.1 holds if and only if Conjecture 1.7 holds.

- Corollary 1.8 shows that our lack of understanding of the Ramsey number rk(Pk+1,n) is due to our lack of understanding of the diagonal Ramsey number rk−1(n,n). However, if we add one additional color, then Theorem 1.4 with t = 2 implies that rk(Pk+1,Pk+1,n) does indeed grow as a tower of height k − 1 in Ω(n).
- Corollary 1.9. There is a positive constant c > 0 such that for k ≥ 4 and n > 3k,


n 4

n 4

n 4 ≥ twrk−1(cn).

n 4

rk(k + 1,k + 1,n) ≥ rk(Pk+1,Pk+1,n) ≥ rk−1

,

,

,

![image 20](<2015-mubayi-off-diagonal-hypergraph-ramsey-numbers_images/imageFile20.png>)

![image 21](<2015-mubayi-off-diagonal-hypergraph-ramsey-numbers_images/imageFile21.png>)

![image 22](<2015-mubayi-off-diagonal-hypergraph-ramsey-numbers_images/imageFile22.png>)

![image 23](<2015-mubayi-off-diagonal-hypergraph-ramsey-numbers_images/imageFile23.png>)

Note that by the results of Erd˝os and Rado [15], for every k ≥ 4, there is an ck > 0 such that rk(k + 1,k + 1,n) ≤ twrk−1(nck).

In the next Section, we prove Theorem 1.4 and the inequality r3(P4,n) > 2Ω(n) from Theorem 1.6. In Sections 3 and 4, we study several related Ramsey problems. We sometimes omit ﬂoor and ceiling signs whenever they are not crucial for the sake of clarity of presentation.

# 2 Ramsey numbers for tight paths versus cliques

In this section, we prove Theorem 1.4.

Proof of Theorem 1.4. Let us ﬁrst prove the upper bound. Set qi = si−k+1 so that q = q1 ··· qt, and N = rk−1(n;q). Let χ : [Nk] → {1,2,... ,t + 1} be a (t + 1)-coloring of the edges of KN(k). We will show that χ must produce a monochromatic copy of Ps(ik) in color i, for some i, or a monochromatic copy of Kn(k) in color t + 1.

Deﬁne φ : k [N−1] → Zt, where for v1,... ,vk−1 ∈ [N], v1 < ··· < vk−1, we have φ(v1,... ,vk−1) = (a1,... ,at), where ai is the length of the longest monochromatic tight-path in color i ending with v1,... ,vk−1. If ai ≥ qi for some i, then we would be done since this implies we have a monochromatic copy of Ps(ik) in color i. Therefore, we can assume ai ∈ {0,1,... ,qi − 1} for all i, and hence φ uses at most q colors.

Since N = rk−1(n;q), there is a subset S ⊂ [N] of n vertices such that φ colors every (k−1)-tuple in

- S the same color, say with color (b1,... ,bt). Then notice that for every k-tuple (v1,... ,vk) ∈ Sk , we have χ(v1,... ,vk) = t + 1. Indeed, suppose there are k vertices v1,... ,vk ∈ S such that χ(v1,... ,vk) = i, where i ≤ t. Since the longest monochromatic tight-path in color i ending with vertices v1,... ,vk−1 is bi, this implies that the longest monochromatic tight-path in color i ending with vertices v2,... ,vk is at least bi + 1, a contradiction. Therefore, S induces a monochromatic copy of Kn(k) in color t + 1. This concludes the proof of the upper bound


We now prove the lower bound. Set N = rk−1(⌊n/q⌋;q)−1 and qi = si −k+1, so that q = q1 ··· qt. Let KN(k−1) be the complete N-vertex (k − 1)-uniform hypergraph with vertex set [N]. Next, let

N k − 1 → [q1] × ··· × [qt]

φ :

be a q-coloring on the edges of KN(k−1), that does not produce a monochromatic copy of K⌊(n/qk−1)⌋ . Such a coloring φ exists since N = rk−1(⌊n/q⌋;q) − 1. We now deﬁne a (t + 1)-coloring

[N] k → [t + 1]

χ :

on the k-tuples of [N] as follows. For v1,... ,vk ∈ [N], where v1 < ··· < vk, let χ(v1,... ,vk) = i if and only if for φ(v1,... ,vk−1) = (a1,... ,at) and φ(v2,... ,vk) = (b1,... ,bt), i is the minimum index such that ai < bi. If no such i exists, then χ(v1,... ,vk) = t + 1. We will show that χ does not produce a monochromatic i-colored copy of Ps(ik), for i ≤ t, nor a monochromatic (t+1)-colored copy of Kn(k).

First, suppose that the coloring χ produces a monochromatic Ps(ik) in color i. That is, there are si vertices v1,v2,... ,vsi ∈ [N], v1 < ··· < vsi, such that χ(vj,vj+1,... ,vj+k−1) = i for

- j = 1,... ,si − k + 1. Let φ(vj,vj+1,... ,vj+k−2) = (aj,1,... ,aj,t), for j = 1,... ,si − k + 2. Then we have


a1,i < a2,i < ··· < asi−k+2,i,

which is a contradiction since qi < si − k + 2. Hence, χ does not produce a monochromatic Ps(ik) in color i for i ≤ t.

Next, we show that χ does not produce a monochromatic copy of Kn(k) in color t + 1. Again, for sake of contradiction, suppose there is a set S ⊂ [N] where S = {v1,... ,vn}, v1 < ··· < vn, such that χ colors every k-tuple of S with color t + 1. We obtain a contradiction from the following claim.

Claim 2.1. Let S = {v1,... ,vn}, χ, and φ be as above, and 1 ≤ ℓ ≤ q. If φ uses at most ℓ distinct colors on k− S1 , and if χ colors every k-tuple of S with color t + 1, then there is a subset T ⊂ S of size ⌊n/ℓ⌋ and a color a = (a1,... ,at) such that φ(T′) = a for every T′ ∈ k T−1 .

The contradiction follows from the fact that ⌊n/ℓ⌋ ≥ ⌊n/q⌋, and φ does not produce a monochromatic copy of K⌊(n/qk−1)⌋ .

Proof of Claim. We proceed by induction on ℓ. The base case ℓ = 1 is trivial. For the inductive step, assume that the statement holds for ℓ′ < ℓ. Let C be the set of ℓ distinct colors deﬁned by φ on k− S1 , and let (a∗1,... ,a∗t) ∈ C be the smallest element in C with respect to the lexicographic ordering. We set S1 = {v1,... ,vn−⌊n/ℓ⌋} and S2 = {vn−⌊n/ℓ⌋+1,... ,vn}. The proof now falls into two cases.

- Case 1. Suppose there is a (k − 1)-tuple (u1,... ,uk−1) ∈ k S−11 such that φ(u1,... ,uk−1) =

(a∗1,... ,a∗t). Then we have φ(T′) = (a∗1,... ,a∗t) for all T′ ∈ k S−21 . Indeed let T′ = (w1,... ,wk−1) ∈

S2

k−1 . Since χ(u1,... ,uk−1,w1) = t+1, we have φ(u2,... ,uk−1,w1) = (a∗1,... ,a∗t). Likewise, since we have χ(u2,... ,uk−1,w1,w2) = t+1, we have φ(u3,... ,uk−1,w1,w2) = (a∗1,... ,a∗t). By repeating this argument k − 3 more times, φ(w1,... ,wk−1) = (a∗1,... ,a∗t).

- Case 2. If we are not in Case 1, then φ(T′) ∈ C \ {(a∗1,... ,a∗t)} for every T′ ∈ k S−11 . Hence φ uses at most ℓ−1 distinct colors on k S−11 . By the induction hypothesis, there is a subset T ⊂ S1 of size


(n − ⌊n/ℓ⌋)/(ℓ − 1) ≥ ⌊n/ℓ⌋ and a color a = (a1,... ,at) such that φ(T′) = a for every T′ ∈ k T−1 . This concludes the proof of the claim and the theorem.

![image 24](<2015-mubayi-off-diagonal-hypergraph-ramsey-numbers_images/imageFile24.png>)

![image 25](<2015-mubayi-off-diagonal-hypergraph-ramsey-numbers_images/imageFile25.png>)

![image 26](<2015-mubayi-off-diagonal-hypergraph-ramsey-numbers_images/imageFile26.png>)

![image 27](<2015-mubayi-off-diagonal-hypergraph-ramsey-numbers_images/imageFile27.png>)

Lower bound construction for r3(P4,n) in Theorem 1.6. Set N = 2cn where c will be determined later. Consider the coloring φ : [N2] → {1,2}, where each edge has probability 1/2 of being a particular color independent of all other edges. Using φ, we deﬁne the coloring χ : [N3] → {red,blue}, where the triple (v1,v2,v3), v1 < v2 < v3, is red if φ(v1,v2) < φ(v2,v3), and is blue otherwise. It is easy to see that χ does not produce a monochromatic red copy of P4(3).

Next we estimate the expected number of monochromatic blue copies of Kn(k) in χ. For a given triple {v1,v2,v3} ∈ [N3] , the probability that χ(v1,v2,v3) = blue is 3/4. Let T = {v1,... ,vn} be a set of t vertices in [N], where v1 < ··· < vn. Let S be a partial Steiner (n,3,2)-system with vertex set T, that is, S is a 3-uniform hypergraph such that each 2-element set of vertices is contained in at most one edge in S. Moreover, S satisﬁes |S| = c′n2. It is known that such a system exists. Then the probability that every triple in T is blue is at most the probability that every triple in

- S is blue. Since the edges in S are independent, that is no two edges have more than one vertex in common, the probability that T is a monochromatic blue clique is at most 34 |S| ≤ 4 3 c

![image 28](<2015-mubayi-off-diagonal-hypergraph-ramsey-numbers_images/imageFile28.png>)

![image 29](<2015-mubayi-off-diagonal-hypergraph-ramsey-numbers_images/imageFile29.png>)

′n2. Therefore the expected number of monochromatic blue copies of Kn(k) produced by χ is at most

N n

- 3

![image 30](<2015-mubayi-off-diagonal-hypergraph-ramsey-numbers_images/imageFile30.png>)

- 4


c′n2

< 1,

for an appropriate choice for c. Hence, there is a coloring χ with no monochromatic red copy of P4(3), and no monochromatic blue copy of Kn(k). Therefore

r3(P4,n) > 2Ω(n).

3 A Ramsey-type result for nonincreasing sets

Notice that the proof of Theorem 1.4 does not require the full strength of Ramsey’s theorem. For example when t = 1, rather than ﬁnding n vertices with the property that every (k − 1)-tuple has the same color, it is enough to ﬁnd a set T of n vertices such that for any subset of k vertices v1,... ,vk ∈ T, where v1 < ··· < vk, we have φ(v1,... ,vk−1) ≥ φ(v2,... ,vk).

Motivated by the observation above, we study the following variant of rk(n;q). Let χ : [Nk] → {1,... ,q} be a q-coloring on the k-tuples of [N] with colors {1,2,... ,q}. For T ⊂ [N], we say that

- T is nonincreasing, if for any set of k + 1 vertices v1,... ,vk+1 ∈ T, where v1 < ··· < vk+1, we have χ(v1,... ,vk) ≥ χ(v2,... ,vk+1). Let fk(n;q) be the minimum integer N, such that for any q-coloring on the k-tuples of [N], with colors {1,2,... ,q}, contains a nonincreasing set T of size


n. Clearly we have fk(n;q) ≤ rk(n;q), and recall that the best known upper bound for r2(n,n) is 4n−o(n). Our next result makes the following improvement in this fundamental case.

- Theorem 3.1. We have f2(n;2) ≤ 2 + √2 n ≈ (3.414)n.


![image 31](<2015-mubayi-off-diagonal-hypergraph-ramsey-numbers_images/imageFile31.png>)

Proof. We proceed by induction on n. The base case n = 1 is trivial. Suppose now the statement holds for n′ < n. Set N = 2 + √2 n , and let χ : [N2] → {1,2}. We will show that there is a nonincreasing subset of size n. Suppose there is a vertex v ∈ [N] and a subset Sv ⊂ {1,... ,v − 1} such that |Sv| ≥ 2 + √2 n−1 , and for every u ∈ Sv we have χ(u,v) = 1. By the induction hypothesis, Sv contains a nonincreasing set of size n−1, and together with v we have a nonincreasing set of size n and we are done. Therefore we can assume no such vertex v ∈ [N] exist.

![image 32](<2015-mubayi-off-diagonal-hypergraph-ramsey-numbers_images/imageFile32.png>)

![image 33](<2015-mubayi-off-diagonal-hypergraph-ramsey-numbers_images/imageFile33.png>)

Set L = 2 + √2 n−1 , and let E2 ⊂ [N2] denote the set of pairs in [N] with color 2, and whose left endpoint lies in {1,... ,N − L}. For each v ∈ [N], let d2(v) denote the number of edges in E2 whose right endpoint is v. By the assumption above, the back degree of each v ∈ [N] in color 1 is at most L − 1, which implies d2(v) ≥ v − 1 − (L − 1) = v − L. Thus we have

![image 34](<2015-mubayi-off-diagonal-hypergraph-ramsey-numbers_images/imageFile34.png>)

|E2| ≥

N

d2(v)

v=L+1

≥ 1 + 2 + ··· + (N − 2L + 2) + (L − 1)(N − 2L + 2)

≥ N(N−22L+2).

![image 35](<2015-mubayi-off-diagonal-hypergraph-ramsey-numbers_images/imageFile35.png>)

By the pigeonhole principle, there is a vertex u ∈ {1,... ,N − L} and a set T ⊂ {u + 1,... ,N}, such that

|T| ≥ N(2(NN−−2LL+2))

![image 36](<2015-mubayi-off-diagonal-hypergraph-ramsey-numbers_images/imageFile36.png>)

= N2((NN−−2LL)) + NN−L

![image 37](<2015-mubayi-off-diagonal-hypergraph-ramsey-numbers_images/imageFile37.png>)

![image 38](<2015-mubayi-off-diagonal-hypergraph-ramsey-numbers_images/imageFile38.png>)

√2 1+√2

√2 1+√2

![image 39](<2015-mubayi-off-diagonal-hypergraph-ramsey-numbers_images/imageFile39.png>)

![image 40](<2015-mubayi-off-diagonal-hypergraph-ramsey-numbers_images/imageFile40.png>)

N 2 + 2+

≥

![image 41](<2015-mubayi-off-diagonal-hypergraph-ramsey-numbers_images/imageFile41.png>)

![image 42](<2015-mubayi-off-diagonal-hypergraph-ramsey-numbers_images/imageFile42.png>)

![image 43](<2015-mubayi-off-diagonal-hypergraph-ramsey-numbers_images/imageFile43.png>)

![image 44](<2015-mubayi-off-diagonal-hypergraph-ramsey-numbers_images/imageFile44.png>)

![image 45](<2015-mubayi-off-diagonal-hypergraph-ramsey-numbers_images/imageFile45.png>)

≥ (2 + √2)n−1 + 2+

√2 1+√2 ,

![image 46](<2015-mubayi-off-diagonal-hypergraph-ramsey-numbers_images/imageFile46.png>)

![image 47](<2015-mubayi-off-diagonal-hypergraph-ramsey-numbers_images/imageFile47.png>)

![image 48](<2015-mubayi-off-diagonal-hypergraph-ramsey-numbers_images/imageFile48.png>)

![image 49](<2015-mubayi-off-diagonal-hypergraph-ramsey-numbers_images/imageFile49.png>)

and for all v ∈ T we have χ(u,v) = 2. Hence, |T| ≥ 2 + √2 n−1 . By the induction hypothesis, we can ﬁnd a nonincreasing set in T of size n − 1, and together with u we have a nonincreasing set of size n.

![image 50](<2015-mubayi-off-diagonal-hypergraph-ramsey-numbers_images/imageFile50.png>)

![image 51](<2015-mubayi-off-diagonal-hypergraph-ramsey-numbers_images/imageFile51.png>)

![image 52](<2015-mubayi-off-diagonal-hypergraph-ramsey-numbers_images/imageFile52.png>)

![image 53](<2015-mubayi-off-diagonal-hypergraph-ramsey-numbers_images/imageFile53.png>)

![image 54](<2015-mubayi-off-diagonal-hypergraph-ramsey-numbers_images/imageFile54.png>)

n

Corollary 3.2. We have r3(P4,n) ≤ 2− 2√2

≈ (3.414)n.

![image 55](<2015-mubayi-off-diagonal-hypergraph-ramsey-numbers_images/imageFile55.png>)

![image 56](<2015-mubayi-off-diagonal-hypergraph-ramsey-numbers_images/imageFile56.png>)

# 4 A related oﬀ-diagonal problem

Let K4(3) \ e denote the 3-uniform hypergraph on four vertices, obtained by removing one edge from K4(3). A simple argument of Erd˝os and Hajnal [13] implies r(K4(3) \ e,Kn(3)) < (n!)2. Here, we generalize their argument to establish an upper bound for Ramsey numbers for k-half-graphs versus cliques. A k-half-graph, denote by B(k), is a k-uniform hypergraph on 2k −2 vertices, whose vertex set is of the form S ∪ T, where |S| = |T| = k − 1, and whose edges are all k-subsets that contain S, and one k-subset that contains T. So B(3) = K4(3) \ e. The goal of this section is to obtain upper and lower bounds for r(B(k),Kn(k)). We start with the upper bound.

- Theorem 4.1. For k ≥ 4, we have r(B(k),Kn(k)) ≤ (n!)k−1.


First, let us recall an old lemma due to Spencer. Lemma 4.2 ([24]). Let H = (V,E) be a k-uniform hypergraph on N vertices. If |E(H)| > N/k, then there exists a subset S ⊂ V (H) such that S is an independent set and

1 k

|S| ≥ 1 −

![image 57](<2015-mubayi-off-diagonal-hypergraph-ramsey-numbers_images/imageFile57.png>)

N

N k|E(H)|

![image 58](<2015-mubayi-off-diagonal-hypergraph-ramsey-numbers_images/imageFile58.png>)

1 k−1

![image 59](<2015-mubayi-off-diagonal-hypergraph-ramsey-numbers_images/imageFile59.png>)

.

Proof of Theorem 4.1. We proceed by induction on n. The base case n = k is trivial. Let n > k and assume the statement holds for n′ < n. Let k ≥ 4 and let χ be a red/blue coloring on the

edges of KN(k), where N = (n!)k−1. Let ER denote the set of red edges in KN(k).

- Case 1: Suppose |ER| <

(1−k1)k−1Nk knk−1 . Then by Lemma 4.2, KN(k) contains a blue clique of size n.

![image 60](<2015-mubayi-off-diagonal-hypergraph-ramsey-numbers_images/imageFile60.png>)

![image 61](<2015-mubayi-off-diagonal-hypergraph-ramsey-numbers_images/imageFile61.png>)

- Case 2: Suppose |ER| ≥


(1−k1)k−1Nk

![image 62](<2015-mubayi-off-diagonal-hypergraph-ramsey-numbers_images/imageFile62.png>)

knk−1 . Then by averaging, there is a (k − 1)-element subset S ⊂ V such that N(S) = {v ∈ V : S ∪ {v} ∈ ER} satisﬁes

![image 63](<2015-mubayi-off-diagonal-hypergraph-ramsey-numbers_images/imageFile63.png>)

1 − k1 k−1 Nk nk−1 k− n1 ≥ ((n − 1)!)k−1 .

![image 64](<2015-mubayi-off-diagonal-hypergraph-ramsey-numbers_images/imageFile64.png>)

|N(S)| ≥

![image 65](<2015-mubayi-off-diagonal-hypergraph-ramsey-numbers_images/imageFile65.png>)

The last inequality follows from the fact that k ≥ 4. Fix a vertex u ∈ S. If {u} ∪ T ∈ ER for some

- T ⊂ N(S) such that |T| = k − 1, then S ∪ T forms a red B(k) and we are done. Therefore we can assume otherwise. By the induction hypothesis, N(S) contains a red copy of B(k), or a blue copy


of Kn(k−)1. We are done in the former case, and the latter case, we can form a blue Kn(k) by adding the vertex u.

We now give constructions which show that r(B(k),Kn(k)) is at least exponential in n. Theorem 4.3. For ﬁxed k ≥ 3, we have r(B(k),Kn(k)) > 2Ω(n). Proof. Surprisingly, we require diﬀerent arguments for k even and k odd.

The case when k is odd. Assume k is odd, and set N = 2cn where c = c(k) will be determined later. Then let T be a random tournament on the vertex set [N], that is, for i,j ∈ [N], independently,

either (i,j) ∈ E or (j,i) ∈ E, where each of the two choices is equally likely. Then let χ : [Nk] → {red,blue} be a red/blue coloring on the k-subsets of [N], where χ(v1,... ,vk) = red if v1,... ,vk induces a regular tournament, that is, the indegree of every vertex is (k − 1)/2 (and hence the outdegree of every vertex is (k − 1)/2). Otherwise we color it blue. We note that since k is odd, a regular tournament on k vertices is possible by the fact that Kk has an Eulerian circuit, and then by directing the edges according to the circuit we obtain a regular tournament.

Notice that the coloring χ does not contain a red B(k). Indeed, let S,T ⊂ [N] such that |S| = |T| = k − 1, S ∩ T = ∅, and every k-tuple of the form S ∪ {v} is red, for all v ∈ T. Then for any

u ∈ S, all edges in the set u × T must have the same direction, either all emanating out of u or all directed towards u. Therefore it is impossible for u ∪ T to have color red, for any choice u ∈ S.

Next we estimate the expected number of monochromatic blue copies of Kn(k) in χ. For a given k-tuple v1,... ,vk ∈ [N], the probability that χ(v1,... ,vk) = blue is clearly at most 1 − 1/2(k2). Let T = {v1,... ,vn} be a set of t vertices in [n], where v1 < ··· < vn. Let S be a partial Steiner (n,k,2)-system with vertex set T, that is, S is a k-uniform hypergraph such that each 2-element set of vertices is contained in at most one edge in S. Moreover, S satisﬁes |S| = ckn2. It is known that such a system exists. Then the probability that every k-tuple in T has color blue is at most the probability that every k-tuple in S is blue. Since the edges in S are independent, that is no two edges have more than one vertex in common, the probability that T is a monochromatic blue clique is at most 1 − 1/2(k2) |S| ≤ 1 − 1/2(k2) ckn

2

. Therefore the expected number of monochromatic blue copies of Kn(k) in χ is at most

N n

2

1 − 1/2(k2) ckn

< 1,

for an appropriate choice for c = c(k). Hence, there is a coloring χ with no red B(k) and no blue Kn(k). Therefore

r(B(k),Kn(k)) > 2cn.

The case when k is even. Assume k is even and set N = 2ct where c = c(k) will be determined later. Consider the coloring φ : [N2] → {1,... ,k − 1}, where each edge has probability 1/(k − 1) of being a particular color independent of all other edges (pairs). Using φ, we deﬁne the coloring χ : [Nk] → {red,blue}, where the k-tuple (v1,... ,vk) is red if φ is a proper edge-coloring on all pairs among {v1,... ,vk}, that is, each of the k −1 colors appears as a perfect matching. Otherwise we color it blue.

Notice that the coloring χ does not contain a red B(k). Indeed let S,T ⊂ [N] such that |S| = |T| =

- k − 1 and S ∩ T = ∅. If every k-tuple of the form S ∪ {v} is red, for all v ∈ T, then all k − 1 colors from φ appear among the edges (pairs) in the set S ×{v}. Hence for any vertex u ∈ S, χ could not have colored u ∪ T red since it is impossible to have any of the k − 1 colors to appear as a perfect matching in u ∪ T.


For a given k-tuple v1,... ,vk ∈ [N], the probability that χ(v1,... ,vk) = blue is at most 1−(1/(k− 1))(k2). By the same argument as above, the expected number of monochromatic blue copies of Kn(k) with respect to χ is less than 1 for an appropriate choice of c = c(k). Hence, there is a coloring χ with no red B(k) and no blue Kn(k). Therefore

r(B(k),Kn(k)) > 2cn and the proof is complete.

![image 66](<2015-mubayi-off-diagonal-hypergraph-ramsey-numbers_images/imageFile66.png>)

![image 67](<2015-mubayi-off-diagonal-hypergraph-ramsey-numbers_images/imageFile67.png>)

![image 68](<2015-mubayi-off-diagonal-hypergraph-ramsey-numbers_images/imageFile68.png>)

![image 69](<2015-mubayi-off-diagonal-hypergraph-ramsey-numbers_images/imageFile69.png>)

# 5 Acknowledgments

We thank David Conlon and Jacob Fox for comments that helped improve the presentation of this paper.

# References

- [1] M. Axenovich, A. Gy´arf´as, H. Liu, D. Mubayi, Multicolor Ramsey numbers for triple systems, Discrete Math. 322 (2014), 69–77.
- [2] M. Ajtai, J. Komlo´s, and E. Szemere´di, A note on Ramsey numbers, J. Combin. Theory Ser. A 29 (1980), 354–360.
- [3] T. Bohman, The triangle-free process, Adv. Math. 221 (2009), 1653–1677.
- [4] T. Bohman and P. Keevash, The early evolution of the H-free process, Invent. Math. 181

(2010), 291–336.

- [5] D. Conlon, A new upper bound for diagonal Ramsey numbers, Ann. of Math. 170 (2009), 941–960.
- [6] D. Conlon, J. Fox, and B. Sudakov, An improved bound for the stepping-up lemma, Discrete Applied Mathematics 161 (2013), 1191–1196.
- [7] D. Conlon, J. Fox, and B. Sudakov, Hypergraph Ramsey numbers, J. Amer. Math. Soc. 23

(2010), 247–266.

- [8] R. P. Dilworth, A decomposition theorem for partially ordered sets, Ann. of Math. 51 (1950), 161–166.
- [9] D. Duﬀus, H. Lefmann, V. Ro¨dl, Shift graphs and lower bounds on Ramsey numbers rk(l;r), Discrete Mathematics 137 (1995), 177–187.
- [10] J. Fox, J. Pach, B. Sudakov, A. Suk, Erd˝os-Szekeres-type theorems for monotone paths and convex bodies, Proceedings of the London Mathematical Society 105 (2012), 953–982.
- [11] M. Elia´sˇ and J. Matousˇek, Higher-order Erd˝os-Szekeres theorems, Advances in Mathematics 244 (2013), 1–15.
- [12] P. Erd˝os, Some remarks on the theory of graphs, Bull. Amer. Math. Soc. 53 (1947), 292–294.
- [13] P. Erd˝os and A. Hajnal, On Ramsey like theorems, Problems and results, Combinatorics (Proc. Conf. Combinatorial Math., Math. Inst., Oxford, 1972), pp. 123–140, Inst. Math. Appl., Southhend-on-Sea, 1972.
- [14] P. Erd˝os, A. Hajnal, and R. Rado, Partition relations for cardinal numbers, Acta Math. Acad. Sci. Hungar. 16 (1965), 93–196.
- [15] P. Erd˝os and R. Rado, Combinatorial theorems on classiﬁcations of subsets of a given set, Proc. London Math. Soc. 3 (1952), 417–439.


- [16] P. Erd˝os and G. Szekeres, A combinatorial problem in geometry, Compos. Math. 2 (1935), 463–470.
- [17] R. L. Graham, V. Ro¨dl, Numbers in ramsey theory, Surveys in Combinatorics, London Math. Soc. Lecture Note Series no. 123, Cambridge Univ. Press, London (1987), 111–153.
- [18] R. L. Graham, B. L. Rothschild, J. H. Spencer: Ramsey Theory, 2nd ed., Wiley, New York, 1990.
- [19] J. H. Kim, The Ramsey number R(3,t) has order of magnitude t2/log t, Random Structures Algorithms 7 (1995), 173–207.
- [20] A. Kruse, A note on the partition calculus of P. Erd˝os and R. Rado, J. London Math. Soc. 40 1965 137–148.
- [21] K.G. Milans, D. Stolee, and D. West, Ordered Ramsey theory and track representations of graphs, to appear in J. Combinatorics.
- [22] G. Moshkovitz and A. Shapira, Ramsey-theory, integer partitions and a new proof of the Erd˝os-Szekeres theorem, Advances in Mathematics 262 (2014), 1107–1129.
- [23] D. Mubayi, Coloring triple systems with local conditions, to appear in Journal of Graph Theory.
- [24] J. Spencer, Tura´n’s theorem for k-graphs, Disc. Math. 2 (1972), 183–186.
- [25] A. Thomason, An upper bound for some ramsey numbers, J. Graph Theory 12 (1988), 509– 517.


