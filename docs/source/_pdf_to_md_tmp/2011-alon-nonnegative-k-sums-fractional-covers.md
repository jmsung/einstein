arXiv:1104.1753v2[math.CO]7Aug2011

Nonnegative k-sums, fractional covers, and probability of small deviations

Noga Alon ∗ Hao Huang † Benny Sudakov‡

Abstract More than twenty years ago, Manickam, Miklo´s, and Singhi conjectured that for any integers

n,k satisfying n ≥ 4k, every set of n real numbers with nonnegative sum has at least nk−−11 kelement subsets whose sum is also nonnegative. In this paper we discuss the connection of this

problem with matchings and fractional covers of hypergraphs, and with the question of estimating the probability that the sum of nonnegative independent random variables exceeds its expectation by a given amount. Using these connections together with some probabilistic techniques, we verify the conjecture for n ≥ 33k2. This substantially improves the best previously known exponential lower bound n ≥ eckloglogk. In addition we prove a tight stability result showing that for every k and all suﬃciently large n, every set of n reals with a nonnegative sum that does not contain a member whose sum with any other k − 1 members is nonnegative, contains at least nk−−11 +

n−k−1

k−1 − 1 subsets of cardinality k with nonnegative sum.

# 1 Introduction

Let {x1,··· ,xn} be a set of n real numbers whose sum is nonnegative. It is natural to ask the following question: how many subsets of nonnegative sum must it always have? The answer is quite straightforward, one can set x1 = n − 1 and all the other xi = −1, which gives 2n−1 subsets. This construction is also the smallest possible since for every subset A, either A or [n]\A or both must have a nonnegative sum. Another natural question is, what happens if we further restrict all the subsets to have a ﬁxed size k? The same example yields nk−−11 nonnegative k-sums consisting of n − 1 and (k − 1) −1’s. This construction is similar to the extremal example in the Erd˝os-Ko-Rado theorem [8] which states that for n ≥ 2k, a family of subsets of size k in [n] with the property that every two subsets have a nonempty intersection has size at most nk−−11 . However the relation between k-sum and k-intersecting family is somewhat subtle and there is no obvious way to translate one problem to the other.

Denote by A(n,k) the minimum possible number of nonnegative k-sums over all possible choices of n numbers x1,··· ,xn with ni=1 xi ≥ 0. For which values of n and k, is the construction x1 =

![image 1](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile1.png>)

∗Sackler School of Mathematics and Blavatnik School of Computer Science, Tel Aviv University, Tel Aviv 69978, Israel. Email: nogaa@tau.ac.il. Research supported in part by an ERC Advanced grant and by a USA-Israeli BSF grant.

†Department of Mathematics, UCLA, Los Angeles, CA, 90095. Email: huanghao@math.ucla.edu. ‡Department of Mathematics, UCLA, Los Angeles, CA 90095. Email: bsudakov@math.ucla.edu. Research supported

in part by NSF CAREER award DMS-0812005 and by a USA-Israeli BSF grant.

n − 1,x2 = ··· = xn = −1 best possible? In other words, when can we guarantee that A(n,k) = n−1 k−1 ? This question was ﬁrst raised by Bier and Manickam [4, 5] in their study of the so-called ﬁrst distribution invariant of the Johnson scheme. In 1987, Manickam and Miklo´s [15] proposed the following conjecture, which in the language of the Johnson scheme was also posed by Manickam and Singhi [16] in 1988.

Conjecture 1.1 For all n ≥ 4k, we have A(n,k) = nk−−11 . In the Erd˝os-Ko-Rado theorem, if n < 2k, all the k-subsets form an intersecting family of size

n k > nk−−11 . But for n > 2k, the star structure, which always takes one ﬁxed element and k −1 other arbitrarily chosen elements, will do better than the set of all k-subsets of the ﬁrst 2k − 1 elements. For a similar reason we have the extra condition n ≥ 4k in the Manickam-Miko´s-Singhi conjecture.

n−1 k−1 is not the best construction when n is very small compared to k. For example, take n = 3k + 1 numbers, 3 of which are equal to −(3k − 2) and the other 3k − 2 numbers are 3. It is easy to see that the sum is zero. On the other hand, the nonnegative k-sums are those subsets consisting only of 3’s, which gives 3kk−2 nonnegative k-sums. It is not diﬃcult to verify that when k > 2,

k < (3kk+1)−1−1 . However this kind of construction does not exist for larger n.

3k−2

The Manickam-Miko´s-Singhi conjecture has been open for more than two decades. Only a few partial results of this conjecture are known so far. The most important one among them is that the conjecture holds for all n divisible by k. This claim can be proved directly by considering a random partition of our set of numbers into pairwise disjoint sets, each of size k, but it also follows immediately from Baranyai’s partition theorem [2]. This theorem asserts that if k | n, then the family of all k-subsets of [n] can be partitioned into disjoint subfamilies so that each subfamily is a perfect k-matching. Since the total sum is nonnegative, among the n/k subsets from each subfamily, there must be at least one having a nonnegative sum. Hence there are no less than nk /(n/k) = nk−−11 nonnegative k-sums in total. Besides this case, the conjecture is also known to be true for small k. It is not hard to check it for k = 2, and the case k = 3 was settled by Manickam [14], and by Marino and Chiaselotti [17] independently.

Let f(k) be the minimal number N such that A(n,k) = nk−−11 for all n ≥ N. The ManickamMiklo´s-Singhi conjecture states that f(k) ≤ 4k. The existence of such function f was ﬁrst demonstrated by Manickam and Miklo´s [15] by showing f(k) ≤ (k −1)(kk +k2)+k. Bhattacharya [3] found a new and shorter proof of existence of f later, but he didn’t improve the previous bound. Very recently, Tyomkyn [20] obtained a better upper bound f(k) ≤ k(4elog k)k ∼ ecklog logk, which is still exponential.

In this paper we discuss a connection between the Manickam-Miklo´s-Singhi conjecture and a problem about matchings in dense uniform hypergraph. We call a hypergraph H r-uniform if all the edges have size r. Denote by ν(H) the matching number of H, which is the maximum number of pairwise disjoint edges in H. For our application, we need the fact that if a (k−1)-uniform hypergraph on n − 1 vertices has matching number at most n/k, then its number of edges cannot exceed c nk−−11 for some constant c < 1 independent of n,k. This is closely related to a special case of a long-standing open problem of Erd˝os [7], who in 1965 asked to determine the maximum possible number of edges of an r-uniform hypergraph H on n vertices with matching number ν(H). Erd˝os conjectured that the

optimal case is when H is a clique or the complement of a clique, more precisely, for ν(H) < ⌊n/r⌋ the maximum possible number of edges is given by the following equation:

maxe(H) = max

r[ν(H) + 1] − 1 r

,

n r

−

n − ν(H) r

(1)

For our application to the Manickam-Miklo´s-Singhi conjecture, it suﬃces to prove a weaker statement which bounds the number of edges as a function of the fractional matching number ν∗(H) instead of ν(H). To attack the latter problem we combine duality with a probabilistic technique together with an inequality by Feige [9] which bounds the probability that the sum of an arbitrary number of nonnegative independent random variables exceeds its expectation by a given amount. Using this machinery, we obtain the ﬁrst polynomial upper bound f(k) ≤ 33k2, which substantially improves all the previous exponential estimates.

- Theorem 1.2 Given integers n and k satisfying n ≥ 33k2, for any n real numbers {x1,··· ,xn} whose sum is nonnegative, there are at least nk−−11 nonnegative k-sums.

Recall that earlier we mentioned the similarity between the Manickam-Miklo´s-Singhi conjecture and the Erd˝os-Ko-Rado theorem. When n ≥ 4k, the conjectured extremal example is x1 = n−1,x2 = ··· = xn = −1, where all the nk−−11 nonnegative k-sums use x1. For the Erd˝os-Ko-Rado theorem when n > 2k, the extremal family also consists of all the nk−−11 subsets containing one ﬁxed element. It is a natural question to ask if this kind of structure is forbidden, can we obtain a signiﬁcant improvement on the nk−−11 bound? A classical result of Hilton and Milner [12] asserts that if n > 2k and no element is contained in every k-subset, then the intersecting family has size at most nk−−11 − n−k−k−11 +1, with the extremal example being one of the following two.

- • Fix x ∈ [n] and X ⊂ [n]\{x}, |X| = k. The family F1 consists of X and all the k-subsets containing x and intersecting with X.
- • Take Y ⊂ [n], |Y | = 3. The family F2 consists of all the k-subsets of [n] which intersects Y with at least two elements.


It can be easily checked that both families are intersecting and |F1| = nk−−11 − n−k−k−11 + 1, |F2| = 3 nk−−23 + nk−−33 . When k = 3, |F1| = |F2| and their structures are non-isomorphic. For k ≥ 4, |F1| > |F2|, so only the ﬁrst construction is optimal.

Here we prove a Hilton-Milner type result about the minimum number of nonnegative k-sums. Call a number xi large if its sum with any other k−1 numbers xj is nonnegative. We prove that if no xi is large, then the nk−−11 bound can be greatly improved. We also show that there are two extremal structures, one of which is maximum for every k and the other only for k = 3. This result can be considered as an analogue of the two extremal cases mentioned above in the Hilton-Milner theorem.

- Theorem 1.3 For any ﬁxed integer k and suﬃciently large n, and for any n real numbers x1,··· ,xn


with ni=1 xi ≥ 0, where no xi is large, the number N of diﬀerent nonnegative k-sums is at least n−1 k−1 + n−k−k−11 − 1.

For large n, Theorem 1.3 (whose statement is tight) improves the nk−−11 bound in the nonnegative k-sum problem to nk−−11 + n−k−k−11 −1 when large numbers are forbidden. This bound is asymptotically (2 + o(1)) nk−−11 .

Call a number xi (1 − δ)-moderately large, if there are at least (1 − δ) nk−−11 nonnegative k-sums using xi, for some constant 0 ≤ δ < 1. In particular, when δ = 0 this is the deﬁnition of a large number. If there is no (1 − δ)-moderately large number for some positive δ, we can prove a much

stronger result asserting that at least a constant proportion of the nk k-sums are nonnegative. More precisely, we prove the following statement.

- Theorem 1.4 There exists a positive function g(δ,k), such that for any ﬁxed k and δ and all suﬃ-


ciently large n, the following holds. For any set of n real numbers x1,··· ,xn with nonnegative sum in which no member is (1 − δ)-moderately large, the number N of nonnegative k-sums in the set is at

least g(δ,k) nk .

The rest of this paper is organized as follows. In the next section we present a quick proof of a slightly worse bound for the function f(k) deﬁned above, namely, we show that f(k) ≤ 2k3. The proof uses a simple estimate on the number of edges in a hypergraph with a given matching number. The proof of Theorem 1.2 appears in Section 3, where we improve this estimate using more sophisticated probabilistic tools. In Section 4 we prove the Hilton-Milner type results Theorem 1.3 and 1.4. The last section contains some concluding remarks and open problems.

# 2 Nonnegative k-sums and hypergraph matchings

In this section we discuss the connection of the Manickam-Miklo´s-Singhi conjecture and hypergraph matchings, and verify the conjecture for n ≥ 2k3.

Without loss of generality, we can assume ni=1 xi = 0 and x1 ≥ x2 ≥ ··· ≥ xn with x1 > 0. If the sum of x1 and the k −1 smallest numbers xn−k+2,··· ,xn is nonnegative, there are already nk−−11 nonnegative k-sums by taking x1 and any other k − 1 numbers. Consequently we can further assume that x1 + xn−k+2 + ··· + xn < 0. As all the numbers sum up to zero, we have

x2 + ··· + xn−k+1 > 0 (2)

Let m be the largest integer not exceeding n−k which is divisible by k, then n−2k +1 ≤ m ≤ n−k. Since the numbers are sorted in descending order, we have

m n − k

x2 + ··· + xm+1 ≥

(x2 + ··· + xn−k+1) > 0 (3) As mentioned in the introduction, the Manickam-Miko´s-Singhi conjecture holds when n is divisible by k by Baranyai’s partition theorem, thus there are at least mk−−11 ≥ nk−−21k nonnegative k-sums using only numbers from {x2,··· ,xm+1}. From now on we are focusing on counting the number of nonnegative k-sums involving x1. If this number plus nk−−21k is at least nk−−11 , then the ManickamMiklo´s-Singhi conjecture is true.

![image 2](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile2.png>)

Recall that in the proof of the case k | n, if we regard all the negative k-sums as edges in a k-uniform hypergraph, then the assumption that all numbers add up to zero provides us the fact that

this hypergraph does not have a perfect k-matching. One can prove there are at least nk−−11 edges in the complement of such a hypergraph, which exactly tells the minimum number of nonnegative k-

sums. We utilize the same idea to estimate the number of nonnegative k-sums involving x1. Construct a (k − 1)-uniform hypergraph H on the vertex set {2,··· ,n}. The edge set E(H) consists of all the

(k −1)-tuples {i1,··· ,ik−1} corresponding to the negative k-sum x1 +xi1 +···+xik−1 < 0. Our goal is to show that e(H) = |E(H)| cannot be too large, and therefore there must be lots of nonnegative

k-sums involving x1.

Denote by ν(H) the matching number of our hypergraph H, which is the maximum number of disjoint edges in H. By deﬁnition, every edge corresponds to a (k − 1)-sum which is less than −x1, thus the sum of the (k − 1)ν(H) numbers corresponding to the vertices in the maximal matching is less than −ν(H)x1. On the other hand, all the remaining n − 1 − (k − 1)ν(H) numbers are at most x1. Therefore −x1 = x2 + ··· + xn ≤ −ν(H)x1 + (n − 1 − (k − 1)ν(H))x1. By solving this inequality, we have the following lemma.

- Lemma 2.1 The matching number ν(H) is at most n/k.

If the matching number of a hypergraph is known and n is large with respect to k, we are able to bound the number of its edges using the following lemma. We denote by H the complement of the hypergraph H.

![image 3](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile3.png>)

- Lemma 2.2 If n > k3, any (k − 1)-uniform hypergraph H on n − 1 vertices with matching number at most n/k has at least k+11 nk−−11 edges missing from it.


![image 4](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile4.png>)

Proof. Consider a random permutation σ on the n − 1 vertices v1,··· ,vn−1 of H. Let the random variables Z1 = 1 if (σ(v1),··· ,σ(vk−1)) is an edge in H and 0 otherwise. Repeat the same process for the next k −1 indices and so on. Finally we will have at least m ≥ nk−−k1 random variables Z1,··· ,Zm. Let Z = Z1 + ··· + Zm. Z is always at most n/k since there is no matching of size larger than n/k. On the other hand, EZi is the probability that k − 1 randomly chosen vertices form an edge in H, therefore EZi = e(H)/ nk−−11 . Hence,

![image 5](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile5.png>)

n k

e(H)

≥ EZ = m

≥

![image 6](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile6.png>)

![image 7](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile7.png>)

n−1 k−1

e(H)

n − k k − 1

![image 8](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile8.png>)

![image 9](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile9.png>)

n−1 k−1

(4)

The number of edges missing is equal to e(H) = nk−−11 − e(H). By (4), e(H) ≤ (1 − k1)n−nk nk−−11 , therefore

![image 10](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile10.png>)

![image 11](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile11.png>)

![image 12](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile12.png>)

1 k

n n − k

![image 13](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile13.png>)

e(H) ≥ 1 − 1 −

![image 14](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile14.png>)

![image 15](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile15.png>)

k3 k3 − k

1 k

≥ 1 − 1 −

![image 16](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile16.png>)

![image 17](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile17.png>)

1 k + 1

n − 1 k − 1

=

![image 18](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile18.png>)

n − 1 k − 1

n − 1 k − 1

(5) ✷

Now we can easily prove a polynomial upper bound for the function f(k) considered in the introduction, showing that f(k) ≤ 2k3.

- Theorem 2.3 If n ≥ 2k3, then for any n real numbers {x1,··· ,xn} whose sum is nonnegative, the number of nonnegative k-sums is at least nk−−11 .


Proof. By Lemma 2.2, there are at least k+11 nk−−11 edges missing in H, which also gives a lower bound for the number of nonnegative k-sums involving x1. Together with the previous nk−−21k nonnegative k-sums without using x1, there are at least k+11 nk−−11 + nk−−21k nonnegative k-sums in total. We claim that this number is greater than nk−−11 when n ≥ 2k3. This statement is equivalent to proving

![image 19](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile19.png>)

![image 20](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile20.png>)

n−2k

k−1 / nk−−11 ≥ 1 − 1/(k + 1), which can be completed as follows:

n − 2k k − 1

/

n − 1 k − 1

2k − 1 n − k + 1 ≥ 1 −

2k − 1 n − 2

2k − 1 n − 1

1 −

··· 1 −

= 1 −

![image 21](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile21.png>)

![image 22](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile22.png>)

![image 23](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile23.png>)

(2k − 1)(k − 1) n − k + 1 ≥ 1 −

![image 24](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile24.png>)

(2k − 1)(k − 1) 2k3 − k + 1 ≥ 1 −

![image 25](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile25.png>)

1 k + 1

![image 26](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile26.png>)

(6)

The last inequality is because (2k − 1)(k − 1)(k + 1) = 2k3 − k2 − 2k + 1 ≤ 2k3 − k + 1. ✷

# 3 Fractional covers and small deviations

The method above veriﬁes the Manickam-Miklo´s-Singhi conjecture for n ≥ 2k3 and improves the current best exponential lower bound n ≥ k(4elog k)k by Tyomkyn [20]. However if we look at Lemma 2.2 attentively, there is still some room to improve it. Recall our discussion of Erd˝os’ conjecture in the introduction: if the conjecture is true in general, then in order to minimize the number of edges in a (k − 1)-hypergraph of a given matching number ν(H) = n/k, the hypergraph must be either a clique of size (k − 1)(n/k + 1) − 1 or the complement of a clique of size n − n/k.

e(H) ∼ min

(1 − 1/k)n k − 1

,

n − 1 k − 1

−

n − n/k k − 1

∼ (1 −

1 k

)k−1

![image 27](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile27.png>)

n − 1 k − 1

- 1

![image 28](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile28.png>)

- 2


≤

n − 1 k − 1

(7)

In this case, the number of edges missing from H must be at least 21 nk−−11 , which is far larger than the bound k+11 nk−−11 in Lemma 2.2. If in our proof of Theorem 2.3, the coeﬃcient before nk−−11 can be changed to a constant instead of the original k+11 , the theorem can also be sharpened to n ≥ Ω(k2). Based on this idea, in the rest of this section we are going to prove Lemma 3.3, which asserts that e(H) ≥ c nk−−11 for some constant c independent of n and k, and can be regarded as a strengthening of

![image 29](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile29.png>)

![image 30](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile30.png>)

![image 31](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile31.png>)

- Lemma 2.2. Then we use it to prove our main result of this paper, Theorem 3.5. In order to improve


- Lemma 2.2, instead of using the usual matching number ν(H), it suﬃces to consider its fractional relaxation, which is deﬁned as follows.


ν∗(H) = max

w(e) w : E(H) → [0,1]

e∈E(H)

subject to

w(e) ≤ 1 for every vertex i.

i∈e

(8)

Note that ν∗(H) is always greater or equal than ν(H). On the other hand for our hypergraph, we can prove the same upper bound for the fractional matching number ν∗(H) as in Lemma 2.1. Recall that H is the (k − 1)-uniform hypergraph on the n − 1 vertices {2,··· ,n}, whose edges are those (k − 1)-tuples (i1,··· ,ik−1) corresponding to negative k-sums x1 + xi1 + ··· + xik < 0.

- Lemma 3.1 The fractional matching number ν∗(H) is at most n/k.


Proof. Choose a weight function w : E(H) → [0,1] which optimizes the linear program (8) and gives the fractional matching number ν∗(H), then ν∗(H) = e∈E(H) w(e). Two observations can be easily made: (i) if e ∈ E(H), then i∈e xi < −x1; (ii) xi ≤ x1 for any i = 2,··· ,n since {xi} are in descending order. Therefore we can bound the fractional matching number in a few steps.

n

n

1 −

w(e) xi +

x1 + x2 + ··· + xn = x1 +

i=2

i=2 i∈e

n

xi w(e) +

≤ x1 +

i=2

e∈E(H) i∈e

w(e) xi

i∈e

1 −

w(e) x1

i∈e

w(e) x1

≤ x1 +

w(e)(−x1) + n − 1 −

e∈E(H) i∈e

e∈E(H)

= x1 − ν∗(H)x1 + n − 1 − (k − 1)ν∗(H) x1

= (n − kν∗(H))x1 (9)

- Lemma 3.1 follows from this inequality and our assumption that x1 + ··· + xn = 0 and x1 > 0. ✷ The determination of the fractional matching number is actually a linear programming problem.


Therefore we can consider its dual problem, which gives the fractional covering number τ∗(H).

τ∗(H) = min

i

v(i) v : V (H) → [0,1]

subject to

v(i) ≥ 1 for every edge e.

i∈e

(10)

By duality we have τ∗(H) = ν∗(H) ≤ n/k. Getting a upper bound for e(H) is equivalent to ﬁnding a function v : V (H) → [0,1] satisfying i∈V(H) v(i) ≤ n/k that maximizes the number of (k − 1)-tuples e where i∈e v(i) ≥ 1. Since this number is monotone increasing in every v(i), we can assume that it is maximized by a function v with i∈V (H) v(i) = n/k.

The following lemma was established by Feige [9], and later improved by He, Zhang, and Zhang [11]. It bounds the tail probability of the sum of independent nonnegative random variables with given expectations. It is stronger than Markov’s inequality in the sense that the number of variables

- m does not appear in the bound.


- Lemma 3.2 Given m independent nonnegative random variables X1,··· ,Xm, each of expectation at most 1, then


m

1 13

Xi < m + δ ≥ min δ/(1 + δ),

Pr

(11)

![image 32](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile32.png>)

i=1

Now we can show that the complement of the hypergraph H has at least constant edge density, which implies as a corollary that a constant proportion of the k-sums involving x1 must be nonnegative.

- Lemma 3.3 If n ≥ Ck2 with C ≥ 1, and H is a (k − 1)-uniform hypergraph on n − 1 vertices with


(n − 1)k−1 (k − 1)!

- 1

![image 33](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile33.png>)

- 2C


1 13

fractional covering number τ∗(H) = n/k, then there are at least

(k − 1)-sets which are not edges in H.

−

![image 34](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile34.png>)

![image 35](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile35.png>)

Proof. Choose a weight function v : V (H) → [0,1] which optimizes the linear programming problem (10). Deﬁne a sequence of k − 1 independent and identically distributed random variables X1,··· ,Xk−1, such that for any 1 ≤ j ≤ k − 1,2 ≤ i ≤ n, Xj = v(i) with probability 1/(n − 1). It is easy to compute the expectation of Xi, which is

1 n − 1

EXi =

![image 36](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile36.png>)

n

n k(n − 1)

v(i) =

![image 37](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile37.png>)

i=2

(12)

Now we can estimate the number of (k − 1)-tuples with sum less than 1. The probability of the event i k=1−1 Xi < 1 is basically the same as the probability that a random (k − 1)-tuple has sum less than 1, except that two random variables Xi and Xj might share a weight from the same vertex, which is not allowed for forming an edge. However, we assumed that n is much larger than k, so this error term is indeed negligible for our application. Note that for i1 < ··· < ik−1, the probability that Xj = v(ij) for every 1 ≤ j ≤ k − 1 is equal to 1/(n − 1)k−1.

![image 38](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile38.png>)

e(H) = i1 < ··· < ik−1 : v(i1) + ··· + v(ik−1) < 1

=

≥

≥

≥

(n − 1)k−1 (k − 1)! distinct i

![image 39](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile39.png>)

(n − 1)k−1 (k − 1)!

![image 40](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile40.png>)

Pr

(n − 1)k−1 (k − 1)!

![image 41](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile41.png>)

Pr

(n − 1)k−1 (k − 1)!

![image 42](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile42.png>)

Pr

k−1

i=1

k−1

i=1

k−1

i=1

Pr X1 = v(i1),··· ,Xk−1 = v(ik−1);

1,···,ik−1

Xi < 1 −

Pr Xi = Xj = v(il)

l i =j

k−1 2

Xi < 1 −

![image 43](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile43.png>)

n − 1

- 1

![image 44](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile44.png>)

- 2C


Xi < 1 −

k−1

Xi < 1

i=1

(13)

The last inequality is because n ≥ Ck2 and −1 ≥ −3Ck + 2C for C ≥ 1,k ≥ 1, and the sum of these two inequalities implies that

- 1

![image 45](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile45.png>)

- 2C


(k − 1)(k − 2) 2(n − 1)

≤

.

![image 46](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile46.png>)

Deﬁne Yi = Xi · k(n − 1)/n to normalize the expectations to EYi = 1. Yi’s are nonnegative because each vertex receives a nonnegative weight in the linear program (10). Applying Lemma 3.2

to Y1,··· ,Yk−1 and setting m = k − 1, δ = (n − k)/n, we get Pr X1 + ··· + Xk−1 < 1 = Pr Y1 + ··· + Yk−1 < k(n − 1)/n ≥ min

1 13

n − k 2n − k

(14) When n > Ck2 and k ≥ 2, C ≥ 1, we have

,

![image 47](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile47.png>)

![image 48](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile48.png>)

Ck2 − k 2Ck2 − k

n − k 2n − k

Ck − 1 2Ck − 1

1 13

(15) Combining (13) and (14) we immediately obtain Lemma 3.3. ✷

>

=

≥

![image 49](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile49.png>)

![image 50](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile50.png>)

![image 51](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile51.png>)

![image 52](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile52.png>)

(n − 1)k−1 (k − 1)!

1 13

- 1

![image 53](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile53.png>)

- 2C


Corollary 3.4 If n ≥ Ck2 with C ≥ 1, then there are at least

nonnegative k-sums involving x1.

−

![image 54](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile54.png>)

![image 55](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile55.png>)

Now we are ready to prove our main theorem:

- Theorem 3.5 If n ≥ 33k2, then for any n real numbers x1,··· ,xn with ni=1 xi ≥ 0, the number of nonnegative k-sums is at least nk−−11 .


Proof. By the previous discussion, we know that there are at least nk−−21k nonnegative k-sums using only x2,··· ,xn. By Corollary 3.4, there are at least

(n − 1)k−1 (k − 1)!

(n − 1)k−1 (k − 1)!

- 1

![image 56](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile56.png>)

- 2 · 33


2 33

1 13

−

≥

![image 57](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile57.png>)

![image 58](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile58.png>)

![image 59](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile59.png>)

![image 60](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile60.png>)

nonnegative k-sums involving x1. In order to prove the theorem, we only need to show that for

- n ≥ 33k2, 2


(n − 1)k−1 (k − 1)!

n − 2k k − 1

n − 1 k − 1

+

≥

(16)

![image 61](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile61.png>)

![image 62](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile62.png>)

33

x k − 1

x(x − 1)··· (x − k + 2) (k − 1)!

Deﬁne an inﬁnitely diﬀerentiable function g(x) =

=

. It is not diﬃcult to see g′′(x) > 0 when x > k − 1. Therefore

![image 63](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile63.png>)

n − 1 k − 1

−

n − 2k k − 1

= g(n −1) −g(n −2k) ≤ [(n −1) −(n−2k)]g′(n −1) = (2k −1)g′(n−1) (17)

x(x − 1)··· (x − k + 3) (k − 1)! ≤ (k − 1)

x(x − 2)··· (x − k + 2) (k − 1)!

(x − 1)(x − 2)··· (x − k + 2) (k − 1)!

g′(x) =

+

+ ··· +

![image 64](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile64.png>)

![image 65](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile65.png>)

![image 66](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile66.png>)

x(x − 1)··· (x − k + 3) (k − 1)! ≤ (k − 1)

![image 67](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile67.png>)

xk−2 (k − 1)!

(18)

![image 68](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile68.png>)

Combining (17) and (18),

n − 1 k − 1

−

n − 2k k − 1

(n − 1)k−2 (k − 1)!

≤ (2k − 1)f′(n − 1) ≤ (2k − 1)(k − 1)

≤

![image 69](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile69.png>)

(n − 1)k−1 (k − 1)!

2 33

![image 70](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile70.png>)

![image 71](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile71.png>)

(19)

The last inequality follows from our assumption n ≥ 33k2. ✷

# 4 Hilton-Milner type results

In this section we prove two Hilton-Milner type results about the minimum number of nonnegative k-sums. The ﬁrst theorem asserts that if ni=1 xi ≥ 0 and no xi is large, then there are at least

n−1 k−1 + n−k−k−11 − 1 nonnegative k-sums.

- Proof of Theorem 1.3. We again assume that x1 ≥ ··· ≥ xn and ni=1 xi is zero. Since x1 is


xi < 0. Suppose t is the largest integer so that there are t subsets S1,··· ,St, such that for any 1 ≤ j ≤ t, Sj is disjoint from {1,··· ,j}, has size at most j(k − 1) and

not large, we know that there exists a (k−1)-subset S1 not containing 1, such that x1+ i∈S

1

x1 + ··· + xj +

xi < 0.

i∈Sj

As we explained above t ≥ 1 and since x1 ≥ ··· ≥ xn we may also assume that Sj consists of the last |Sj| indices in {1,··· ,n}. By Corollary 3.4, for suﬃciently large n, there are at least 141 nk−−11 nonnegative k-sums using x1. Note also that after deleting x1 and {xi}i∈S1, the sum of the remaining n − 1 − |S1| ≥ n − k numbers is nonnegative. Therefore, again by Corollary 3.4, there are at least

![image 72](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile72.png>)

n−k−1

1 14

k−1 nonnegative k-sums using x2 but not x1. In the next step, we delete x1,x2 and {xi}i∈S2 and

![image 73](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile73.png>)

bound the number of nonnegative k-sums involving x3 but neither x1 or x2 by 141 n−k2−k1−1 . Repeating this process for 30 steps, we obtain

![image 74](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile74.png>)

n − 1 k − 1

n − k − 1 k − 1

n − 29k − 1 k − 1 >

1 14

+

+ ··· +

N ≥

![image 75](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile75.png>)

n − 29k − 1 k − 1

n − 1 k − 1

30 14

n − 1 k − 1

n − k − 1 k − 1

> 2

>

+

![image 76](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile76.png>)

− 1

where here we used the fact that 3014 > 2 and n is suﬃciently large (as a function of k). If 2 ≤ t < 30, by the maximality of t, we know that the sum of xt+1 with any (k−1) numbers with

![image 77](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile77.png>)

indices not in {1,··· ,t + 1} ∪ St is nonnegative. This gives us n−(t+1)k−1−|St| ≥ n−ktk−1−1 nonnegative k-sums. We can also replace xt+1 by any xi where 1 ≤ i ≤ t and the new k-sum is still nonnegative since xi ≥ xt+1. Therefore,

N ≥ (t + 1)

n − tk − 1 k − 1

≥ (t + 1)

n − 29k − 1 k − 1

> 2

n − 1 k − 1

for suﬃciently large n. Thus the only remaining case is t = 1. Recall that x1 is not large, and hence x1 + (xn−k+2 + ··· + xn) < 0. Suppose I is a (k − 1)-subset

of [2,n] such that x1 + i∈I xi < 0. If 2 ∈ I, then x1 + x2 + i∈I\{2} xi < 0, this contradicts the assumption t = 1 since |I\{2}| = k − 2 ≤ 2(k − 1). Hence we can assume that all the (k − 1)-subsets

I1,··· ,Im corresponding to negative k-sums involving x1 belong to the interval [3,n]. Let N1 be the number of nonnegative k-sums involving x1, and let N2 be the number of nonnegative k-sums using x2 but not x1, then

n − 1 k − 1

N ≥ N1 + N2 =

− m + N2.

In order to prove N ≥ nk−−11 + n−k−k−11 − 1, we only need to establish the following inequality

N2 ≥

n − k − 1 k − 1

+ m − 1. (20)

Observe that the subsets I1,··· ,Im satisfy some additional properties. First of all, if two sets Ii and Ij are disjoint, then by deﬁnition, x1 + l∈I

xl < 0, summing them up gives x1 + x2 + l∈I

xl < 0 and x2 + l∈I

xl ≤ x1 + l∈I

i

j

j

i∪Ij xl < 0 with |Ii ∪ Ij| = 2(k − 1), which again contradicts the assumption t = 1. Therefore we might assume that {Ii}1≤i≤m is an intersecting family. By the Erd˝os-Ko-Rado theorem,

(n − 2) − 1 (k − 1) − 1

n − 3 k − 2

m ≤

=

.

The second observation is that if a (k−1)-subset I ⊂ [3,n] is disjoint from some Ii, then x2+ i∈I xi ≥

xk < 0, for the same reason this contradicts t = 1. Hence N2 is bounded from below by the number of (k − 1)-subsets I ⊂ [3,n] such that I is disjoint from at least one of I1,··· ,Im. Equivalently we need to count the distinct (k − 1)-subsets contained in some Ji = [3,n]\Ii, all of which have sizes n − k − 1. By the real version of the Kruskal-Katona theorem (see Ex.13.31(b) in [13]), if m = n− xk−1 for some positive real number x ≥ n − k − 1, then N2 ≥ k− x1 . On the other hand, it is already known that 1 ≤ m ≤ nk−−23 = n− n−k−31 , thus n − k − 1 ≤ x ≤ n − 3. The only remaining step is to verify the following inequality for x in this range,

0. Otherwise if x2 + i∈I xi < 0 and x1 + k∈I

i

x k − 1

n − k − 1 k − 1

x n − k − 1

≥

+

− 1. (21)

Let f(x) = k− x1 − n− xk−1 , note that when x ≤ n − 4 = (k − 2) + (n − k − 2),

f(x + 1) − f(x) =

=

x + 1 k − 1

x k − 2

−

x + 1 n − k − 1

−

−

x n − k − 2

≥ 0

x k − 1

−

x n − k − 1

The last inequality is because when n is large, x ≥ n−k−1 > 2(k−2). Moreover, xt is an increasing function for 0 < t < x/2, so when x ≤ n − 4, n− xk−2 = x−(n− xk−2) ≤ k− x2 .

Therefore we only need to verify (21) for n − k − 1 ≤ x < n − k, which corresponds to 1 ≤ m ≤ n−k −1. For m = 1, (21) is obvious, so it suﬃces to look at the case m ≥ 2. The number of distinct (k − 1)-subsets of J1 or J2 is minimized when |J1 ∩ J2| = n − k − 2, which, by the inclusion-exclusion principle, gives

N2 ≥ 2

n − k − 1 k − 1

−

n − k − 2 k − 1

=

n − k − 1 k − 1

+

n − k − 2 k − 2

.

So (20) is also true for 2 ≤ m ≤ n−k−k−22 + 1. It is easy to see that for k ≥ 3 and n suﬃciently large, n − k − 1 ≤ n−k−k−22 + 1. For k = 2, we have x = n − 3 and (21) becomes n−13 ≥ n−13 + n n−−33 − 1, which is true and completes the proof. ✷

- Remark 1. In order for all the inequalities to be correct, we only need n > Ck2. By carefully analyzing the above computations, one can check that C = 500 is enough.


- Remark 2. Note that in the proof, the equality (20) holds in two diﬀerent cases. The ﬁrst case is when m = 1, which means x1 + xn−k+2 + ··· + xn < 0 but any other k-sums involving x1 are nonnegative. All the other nonnegative k-sums are formed by x2 together with any (k − 1)-subsets not containing xn−k+2,··· ,xn. This case is realizable by the following construction: x1 = k(k − 1)n, x2 = n−2, x3 = ··· = xn−k+1 = −1, xn−k+2 = ··· = xn = −(kn+1). The second case is in (21) when


x = n−4 and x = n−k−1 holds simultaneously, which gives k = 3. In this case, m = n n−−43 = n−3, and the Kruskal-Katona theorem holds with equality for the (n − 4)-subsets J1,··· ,Jn−3. That is to say, the negative 3-sums using x1 are x1 + xi + xn for 3 ≤ i ≤ n − 1, while the nonnegative 3-sums containing x2 but not x1 are x2 + xi + xj for 3 ≤ i < j ≤ n − 1. This case can also be achieved by setting x1 = x2 = 1, x3 = ··· = xn−1 = 2(n1−3), and xn = −23. For large n, these are the only two possible conﬁgurations achieving equality in Theorem 1.3.

![image 78](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile78.png>)

![image 79](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile79.png>)

Next we prove Theorem 1.4, which states that if i xi ≥ 0 and no xi is moderately large, then at least a constant proportion of the nk k-sums are nonnegative.

- Proof of Theorem 1.4. Suppose t is the largest integer so that there are t subsets S1,··· ,St such that for any 1 ≤ j ≤ t, Sj is disjoint from {1,··· ,j}, has at most j(k − 1) elements, and


x1 + ··· + xj +

xi < 0.

i∈Sj

By the maximality of t, the sum of xt+1 and any k − 1 numbers xi with indices from [n]\({1,··· ,t + 1} ∪ St) is nonnegative, so there are at least n−ktk−1−1 nonnegative k-sums using xt+1. Since xt+1 is not (1 − δ)-moderately large,

n − tk − 1 k − 1

n − 1 k − 1

< (1 − δ)

. For suﬃciently large n, this is asymptotically equivalent to

k−1

tk n

< 1 − δ. Since

1 −

![image 80](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile80.png>)

k−1

tk(k − 1) n

tk n

> 1 −

, we have

1 −

![image 81](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile81.png>)

![image 82](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile82.png>)

n k2

t >

δ

![image 83](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile83.png>)

Recall that by Corollary 3.4, for each i = 1,··· , kn2δ, xi gives at least 141 n−(ik−−1)1k−1 nonnegative k-sums, therefore

![image 84](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile84.png>)

![image 85](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile85.png>)

n − (kn2δ)k − 1 k − 1 ≥

n − 1 k − 1

1 14

![image 86](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile86.png>)

N ≥

+ ··· +

![image 87](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile87.png>)

k n − 1

nδ 14k2

δ k

1 −

![image 88](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile88.png>)

![image 89](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile89.png>)

k − 1 >

δ(1 − δ) 14k

n k

![image 90](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile90.png>)

δ(1 − δ) 14k

Setting g(δ,k) =

![image 91](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile91.png>)

completes the proof. ✷

# 5 Concluding remarks

- • In this paper, we have proved that if n > 33k2, any n real numbers with a nonnegative sum have at

least nk−−11 nonnegative k-sums, thereby verifying the Manickam-Miklo´s-Singhi conjecture in this range. Because of the inequality n−k2k + C nk−−11 ≥ nk−−11 we used, our method will not give a better range than the quadratic one, and we did not try hard to compute the best constant in the quadratic bound. It would be interesting to decide if the Manickam-Miklo´s-Singhi conjecture can be veriﬁed for a linear range n > ck. Perhaps some algebraic methods or structural analysis of the extremal conﬁgurations will help.

- • Feige [9] conjectures that the constant 1/13 in Lemma 3.2 can be improved to 1/e. This is a special case of a more general question suggested by Samuels [18]. He asked to determine, for a ﬁxed m, the inﬁmum of Pr(X1 + ··· + Xk < m), where the inﬁmum is taken over all possible collections of k independent nonnegative random variables X1,··· ,Xk with given expectations µ1,··· ,µk. For k = 1 the answer is given by Markov’s inequality. Samuels [18, 19] solved this question for k ≤ 4, but for all k ≥ 5 his problem is still completely open.
- • Another intriguing objective is to prove the conjecture by Erd˝os which states that the maximum number of edges in an r-uniform hypergraph H on n vertices with matching number ν(H) is exactly

max

r[ν(H) + 1] − 1 r

,

n r

−

n − ν(H) r

.

The ﬁrst number corresponds to a clique and the second case is the complement of a clique. When ν(H) = 1, this conjecture is exactly the Erd˝os-Ko-Rado theorem [8]. Erd˝os also veriﬁed it for n > crν(H) where cr is a constant depending on r. Recall that in our graph H we have ν(H) ≤ n/k and r here is equal to k − 1, so if Erd˝os’ conjecture is true in general, we can give a direct proof of constant edge density in the complement of H. In this way we can avoid using fractional matchings in our proof. But even without the application here, this conjecture is interesting in its own right. The fractional version of Erd˝os’ conjecture is also very interesting. In its asymptotic form it says that if H is an r-uniform n-vertex hypergraph with fractional matching number ν∗(H) = xn, where 0 ≤ x < 1/r, then

e(H) ≤ (1 + o(1))max (rx)r,1 − (1 − x)r

n r

. (22)

- • As pointed out to us by Andrzej Rucin´ski, part of our reasoning in Section 3 implies that the


function A(n,k) deﬁned in the ﬁrst page is precisely nk minus the maximum possible number of edges in a k-uniform hypergraph on n vertices with fractional covering number strictly smaller than

n/k. Indeed, given n reals x1,... ,xn with sum zero and only A(n,k) nonnegative k-sums, we may assume that the absolute value of each xi is smaller than 1/k (otherwise simply multiply all of them by a suﬃciently small positive real.) Next, add a suﬃciently small positive ǫ to each xi, keeping each xi smaller than 1/k and keeping the sum of any negative k-tuple below zero (this is clearly possible.) Note that the sum of these new reals, call them x′i, is strictly positive and the number of positive k-sums is A(n,k). Put ν(i) = 1/k − x′i and observe that i ν(i) < n/k and the k-uniform hypergraph whose edges are all k-sets e for which i∈e ν(i) ≥ 1 has exactly nk − A(n,k) edges.

Therefore, there is a k-uniform hypergraph on n vertices with fractional covering number strictly smaller than n/k and at least nk − A(n,k) edges. Conversely, given a k-uniform hypergraph H on n vertices and a fractional covering of it ν : V (H)  → [0,1] with i ν(i) = n/k − δ < n/k and

i∈e ν(i) ≥ 1 for each e ∈ E(H), one can deﬁne xi = k1 − nδ − ν(i) to get a set of n reals whose sum is zero, in which the number of nonnegative k-sums is at most nk − |E(H)| (as the sum of the numbers xi for every k-set forming an edge of H is at most 1 − kδn − 1 < 0). This implies the desired equality, showing that the problem of determining A(n,k) is equivalent to that of ﬁnding the maximum possible number of edges of a k-uniform hypergraph on n vertices with fractional covering number strictly smaller than n/k. Note that this is equivalent to the problem of settling the fractional version of the conjecture of Erd˝os for the extremal case of fractional matching number < n/k.

![image 92](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile92.png>)

![image 93](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile93.png>)

![image 94](<2011-alon-nonnegative-k-sums-fractional-covers_images/imageFile94.png>)

- • Although the fractional version of Erd˝os’ conjecture is still widely open in general, our techniques can be used to make some progress on this problem. Combining the approach from Section 3 and the above mentioned results of Samuels we veriﬁed, in joint work with Frankl, Ro¨dl and Rucin´ski [1], conjecture (22) for certain ranges of x for 3 and 4-uniform hypergraphs. These results can be used to study a Dirac-type question of Daykin and H¨aggkvist [6] and of H´an, Person and Schacht [10] about perfect matchings in hypergraphs.


For an r-uniform hypergraph H and for 1 ≤ d ≤ r, let δd(H) denote the minimum number of edges containing a subset of d vertices of H, where the minimum is taken over all such subsets. In particular, δ1(H) is the minimum vertex degree of H. For r that divides n, let md(r,n) denote the smallest number, so that any r-uniform hypergraph H on n vertices with δd(H) ≥ md(r,n) contains a perfect matching. Similarly, let m∗d(r,n) denote the smallest number, so that any runiform hypergraph H on n vertices with δd(H) ≥ m∗d(r,n) contains a perfect fractional matching. Together with Frankl, Ro¨dl and Rucin´ski [1] we proved that for all d and r, md(r,n) ∼ m∗d(r,n) and further reduced the problem of determining the asymptotic behavior of these numbers to some special cases of conjecture (22). Using this relation we were able to determine md(r,n) asymptotically for several values of d and r, which have not been known before. Moreover, our approach may lead to a solution of the general case as well, see [1] for the details.

Acknowledgment We would like to thank Andrzej Rucin´ski for helpful discussions and comments, and Nati Linial for inspiring conversations and intriguing questions which led us to the results in Section 4.

# References

- [1] N. Alon, P. Frankl, H. Huang, V. Ro¨dl, A. Rucin´ski and B. Sudakov, preprint.
- [2] Z. Baranyai, On the factorization of the complete uniform hypergraph, Colloq. Math. Soc. J´anos Bolyai 10 (1975), 91–108.
- [3] A. Bhattacharya, On a conjecture of Manickam and Singhi, Discrete Math. 272 (2003), 259–261


- [4] T. Bier, A distribution invariant for the association schemes and strongly regular graphs, Linear algebra and its applications 57 (1984), 230–2521.
- [5] T. Bier and N. Manickam, The ﬁrst distribution invariant of the Johnson scheme, SEAMS Bull. Math. 11 (1987), 61–68.
- [6] D. E. Daykin and R. H¨aggkvist, Degrees giving independent edges in a hypergraph, Bull. Austral. Math. Soc. 23 (1981), 103–109.
- [7] P. Erd˝os, A problem on independent r-tuples, Ann. Univ. Sci. Budapest. Eo¨tv¨os Sect. Math. 8

(1965), 93–95.

- [8] P. Erd˝os, C. Ko and R. Rado, Intersection theorems for systems of ﬁnite sets, Quart. J. Math. Oxford. Series (2) 12 (1961), 312–320.
- [9] U. Feige, On sums of independent random variables with unbounded variance and estimating the average degree in a graph, SIAM J. Comput. 35 (2006), no. 4, 964–984.
- [10] H. H´an, Y. Person and M. Schacht, On perfect matchings in uniform hypergraphs with large minimum vertex degree, SIAM J. Discrete Math. 23 (2009), no. 2, 732–748.
- [11] S. He, J. Zhang and S. Zhang, Bounding probability of small deviation: a fourth moment approach, Math. Oper. Res. 35 (2010), no.1, 208–232.
- [12] A. J. W. Hilton and E. C. Milner, Some intersection theorems for systems of ﬁnite sets, Quart. J. Math. Oxford Ser. (2), 18 (1967), 369–384.
- [13] L. Lov´asz, Combinatorial problems and exercises, North-Holland Publishing Co., Amsterdam, 1979.
- [14] N. Manickam, On the distribution invariants of association schemes, Ph.D. Dissertation, Ohio State University, 1986.
- [15] N. Manickam and D. Miklo´s, On the number of non-negative partial sums of a non-negative sum, Colloq. Math. Soc. Janos Bolyai 52 (1987), 385–392.
- [16] N. Manickam and N. M. Singhi, First distribution invariants and EKR theorems, J. Combinatorial Theory, Series A 48 (1988), 91–103.
- [17] G. Marino and G. Chiaselotti, A method to count the positive 3-subsets in a set of real numbers with non-negative sum, European J. Combin. 23 (2002), 619–629.
- [18] S.M. Samuels, On a Chebyshev-type inequality for sums of independent random variables, Ann. Math. Statist. 37 (1966), 248–259.
- [19] S.M. Samuels, More on a Chebyshev-type inequality for sums of independent random variables, Purdue Stat. Dept. Mimeo. Series no. 155 (1968)
- [20] M. Tyomkyn, An improved bound for the Manickam-Miklo´s-Singhi conjecture, available online at http://arxiv.org/pdf/1011.2803v1.


