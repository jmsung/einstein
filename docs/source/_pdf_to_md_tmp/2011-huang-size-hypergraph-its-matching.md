arXiv:1107.5544v2[math.CO]15Sep2011

The size of a hypergraph and its matching number

Hao Huang∗ Po-Shen Loh† Benny Sudakov‡

Abstract More than forty years ago, Erdo˝s conjectured that for any t ≤ nk, every k-uniform hypergraph

![image 1](<2011-huang-size-hypergraph-its-matching_images/imageFile1.png>)

on n vertices without t disjoint edges has at most max ktk−1 , nk − n−kt+1 edges. Although this appears to be a basic instance of the hypergraph Tur´an problem (with a t-edge matching as

the excluded hypergraph), progress on this question has remained elusive. In this paper, we verify this conjecture for all t < 3nk2 . This improves upon the best previously known range t = O k n3 , which dates back to the 1970’s.

![image 2](<2011-huang-size-hypergraph-its-matching_images/imageFile2.png>)

![image 3](<2011-huang-size-hypergraph-its-matching_images/imageFile3.png>)

# 1 Introduction

A k-uniform hypergraph is a pair H = (V,E), where V = V (H) is a ﬁnite set of vertices, and E = E(H) ⊆ Vk is a family of k-element subsets of V called edges. A matching in H is a set of disjoint edges in E(H). We denote by ν(H) the size of the largest matching, i.e., the maximum number of disjoint edges in H. The problem of ﬁnding the maximum matching in a hypergraph has many applications in various diﬀerent areas of mathematics, computer science, and even computational chemistry. Yet although the graph matching problem is fairly well-understood, and solvable in polynomial time, most of the problems related to hypergraph matching tend to be very diﬃcult and remain unsolved. Indeed, the hypergraph matching problem is known to be NP-hard even for 3-uniform hypergraphs, without any good approximation algorithm.

One of the most basic open questions in this area was raised in 1965 by Erd˝os [5], who asked to determine the maximum possible number of edges that can appear in any k-uniform hypergraph with matching number ν(H) < t ≤ nk (equivalently, without any t pairwise disjoint edges). He conjectured that this problem has only two extremal constructions. The ﬁrst one is a clique consisting of all the k-subsets on kt − 1 vertices, which obviously has matching number t − 1. The second example is a kuniform hypergraph on n vertices containing all the edges intersecting a ﬁxed set of t−1 vertices, which also forces the matching number to be at most t − 1. Neither construction is uniformly better than the other across the entire parameter space, so the conjectured bound is the maximum of these two possibilities. Note that in the second case, the complement of this hypergraph is a clique on n−t+1 vertices together with t−1 isolated vertices, and thus the original hypergraph has nk − n−kt+1 edges.

![image 4](<2011-huang-size-hypergraph-its-matching_images/imageFile4.png>)

![image 5](<2011-huang-size-hypergraph-its-matching_images/imageFile5.png>)

∗Department of Mathematics, UCLA, Los Angeles, CA 90095. Email: huanghao@math.ucla.edu. Research supported by a UC Dissertation Year Fellowship.

†Department of Mathematical Sciences, Carnegie Mellon University, Pittsburgh, PA 15213. Email: ploh@cmu.edu. Research supported by an NSA Young Investigators Grant.

‡Department of Mathematics, UCLA, Los Angeles, CA 90095. Email: bsudakov@math.ucla.edu. Research supported in part by NSF grant DMS-1101185, NSF CAREER award DMS-0812005, and by a USA-Israeli BSF grant.

Conjecture 1.1 Every k-uniform hypergraph H on n vertices with matching number ν(H) < t ≤ nk satisﬁes

![image 6](<2011-huang-size-hypergraph-its-matching_images/imageFile6.png>)

kt − 1 k

n − t + 1 k

n k

e(H) ≤ max

−

,

. (1)

In addition to being important in its own right, this Erd˝os conjecture has several interesting applications, which we discuss in the concluding remarks. Yet although it is more than forty years old, only partial results have been discovered so far. In the case t = 2, the condition simpliﬁes to the requirement that every pair of edges intersects, so Conjecture 1.1 is thus equivalent to a classical theorem of Erd˝os, Ko, and Rado [7]: that any intersecting family of k-subsets on n ≥ 2k elements has size at most nk−−11 . The graph case (k = 2) was separately veriﬁed in [6] by Erd˝os and Gallai. For general ﬁxed t and k, Erd˝os [5] proved his conjecture for suﬃciently large n. Frankl [8] showed that Conjecture 1.1 was asymptotically true for all n by proving the weaker bound e(H) ≤ (t − 1) nk−−11 .

A short calculation shows that when t ≤ k+1n , we always have nk − n−kt+1 > ktk−1 , so the potential extremal example in this case has all edges intersecting a ﬁxed set of t − 1 vertices. One natural question is then to determine the range of t (with respect to n and k ≥ 3) for which the maximum is indeed equal to nk − n−kt+1 , i.e., where the second case is optimal. Recently, Frankl, Ro¨dl, and Rucin´ski [9] studied 3-uniform hypergraphs (k = 3), and proved that for t ≤ n/4, the maximum was indeed n3 − n−3t+1 , establishing the conjecture in that range. For general k ≥ 4, Bollob´s, Daykin, and Erd˝os [4] explicitly computed the bounds achieved by the proof in [5], showing that the conjecture holds for t < 2nk3. Frankl and Fure¨di [8] established the result in a diﬀerent range t < 100 nk 1/2, which improves the original bound when k is large relative to n. In this paper, we extend the range in which the Erd˝os conjecture holds to all t < 3nk2.

![image 7](<2011-huang-size-hypergraph-its-matching_images/imageFile7.png>)

![image 8](<2011-huang-size-hypergraph-its-matching_images/imageFile8.png>)

![image 9](<2011-huang-size-hypergraph-its-matching_images/imageFile9.png>)

![image 10](<2011-huang-size-hypergraph-its-matching_images/imageFile10.png>)

Theorem 1.2 For any integers n,k,t satisfying t < 3nk2, every k-uniform hypergraph on n vertices without t disjoint edges contains at most nk − n−kt+1 edges.

![image 11](<2011-huang-size-hypergraph-its-matching_images/imageFile11.png>)

To describe the idea of our proof, we ﬁrst outline Erd˝os’s original approach for the case t < 2nk3. Let v be a vertex of maximum degree. By induction on t we ﬁnd t − 1 disjoint edges F1,... ,Ft−1, none of which contain v. If deg(v) exceeds k(t − 1) nk−−22 , which is the maximum possible number of edges containing v which also meet a vertex in ti=1−1 Fi, then we can ﬁnd t disjoint edges. Otherwise, the number of edges meeting any of Fi is at most | ti=1−1 Fi| · k(t − 1) nk−−22 = k(t − 1) · k(t − 1) nk−−22 , which turns out to be less than the total number of edges when n ≥ 2k3t. Any other edge will serve

![image 12](<2011-huang-size-hypergraph-its-matching_images/imageFile12.png>)

- as the t-th edge in the matching. To improve Erd˝os’s bound, we show that in the ﬁrst part of the argument, we are already done if


the t-th largest degree exceeds 2t nk−−22 . This puts a tighter constraint on the sum of the degrees of the k(t − 1) vertices in ti=1−1 Fi, allowing the second stage to proceed under the relaxed assumption n ≥ 3k2t. The fact that t vertices of degree at least 2t nk−−22 are enough to ﬁnd t disjoint edges leads naturally to the following multicolored version of the Erd˝os conjecture, which was also considered independently by Aharoni and Howard in [1].

Conjecture 1.3 Let F1,... ,Ft be families of subsets in [nk] . If |Fi| > max nk − n−kt+1 , ktk−1 for all 1 ≤ i ≤ t, then there is a “rainbow” matching of size t: one that contains exactly one edge from each family.

The k = 2 case of this conjecture was established by Meshulam (see [1]). To obtain Theorem 1.2, we prove an asymptotic version of Conjecture 1.3, by showing that a rainbow matching exists whenever |Fi| > (t − 1) nk−−11 for every 1 ≤ i ≤ t.

The rest of this paper is organized as follows. In the next section, we describe the so-called shifting method, which is a well known technique in extremal set theory, and use it to prove some preliminary results. In Section 3 we ﬁrst prove the multicolored Erd˝os conjecture asymptotically, and then use it to prove Theorem 1.2. There, we also use the same argument to show that Conjecture 1.3 holds for all t < 3nk2. The last section contains some concluding remarks and open problems.

![image 13](<2011-huang-size-hypergraph-its-matching_images/imageFile13.png>)

# 2 Shifting

In extremal set theory, one of the most important and widely-used tools is the technique of shifting, which allows us to limit our attention to sets with certain structure. In this section we will only state and prove the relevant results for Section 3. For more background on the applications of shifting in extremal set theory, we refer the reader to the survey [8] by Frankl.

Given a family F of equal-size subsets of [n], for integers 1 ≤ j < i ≤ n, we deﬁne the (i,j)-shift map Sij as follows: for any set F ∈ F,

Sij(F) =   

F \ {i} ∪ {j}, iﬀ i ∈ F, j  ∈ F and F \ {i} ∪ {j}  ∈ F ; F , otherwise.

Also, we denote the family after shifting as

Sij(F) = {Sij(F) : F ∈ F} .

- Lemma 2.1 The shift map Sij satisﬁes the following properties.


- (i) |Sij(F)| = |F|.
- (ii) If F is k-uniform, then so is Sij(F).
- (iii) If the families F1, ..., Ft have the property that no subsets F1 ∈ F1, ..., Ft ∈ Ft are pairwise disjoint, then the shifted families Sij(F1), ..., Sij(Ft) still preserve this property.


Proof. Claims (i) and (ii) are obvious. For (iii), assume that the statement is false, i.e., we have Fi ∈ Fi such that Sij(F1), . .. , Sij(Ft) are pairwise disjoint, while F1, .. ., Ft are not. Without loss of generality, F1 ∩ F2 = ∅. Next, observe that whenever Sij(Fk) = Fk, we also have j ∈ Sij(Fk), so the pairwise disjointness of the Sij(Fk) implies that the only possible case (re-indexing if necessary) is for Sij(F1) = F1 \ {i} ∪ {j}, and Sij(Fk) = Fk for every k ≥ 2. Note also that since F1 and F2 intersect while Sij(F1) and Sij(F2) do not, we must have i ∈ F2 and j  ∈ F2.

Therefore the only reason that Sij(F2) = F2 is because F2′ = F2 \ {i} ∪ {j} is already in F2. The pair of disjoint sets Sij(F1) and Sij(F2) = F2 have the same union as the pair of disjoint sets F1 and F2′. Using the pairwise disjointness of the Sij(Fk), we conclude that the sets F1, F2′, F3, ... , Ft are pairwise disjoint as well, contradicting our initial assumption. ✷

In practice, we often combine the shifting technique with induction on the number of elements in the underlying set. Indeed, let us apply the shifts {Sni}1≤i≤n−1 successively, and with slight abuse of notation, let us again call the resulting families F1, . .. , Ft. Create from each Fi two sub-families based on containment of the ﬁnal element n:

Fi(n) = {F \ {n} : F ∈ Fi,n ∈ F} , Fi(¯n) = {F : F ∈ Fi,n  ∈ F} .

It turns out that the rainbow matching number does not increase by this decomposition.

- Lemma 2.2 Let F1, ..., Ft be the shifted families, where each Fi is ki-uniform and ti=1 ki ≤ n. Suppose that no subsets F1 ∈ F1, ..., Ft ∈ Ft are pairwise disjoint. Then, for any 0 ≤ s ≤ t, the families F1(n),... ,Fs(n),Fs+1(¯n),... ,Ft(¯n) still have the same property.

Proof. Assume for the sake of contradiction that there exist pairwise disjoint sets F1 ∈ F1(n), .. ., Fs ∈ Fs(n), Fs+1 ∈ Fs+1(¯n), .. ., Ft ∈ Ft(¯n). By deﬁnition of Fi(n) and Fi(¯n), we know that Fi ∪ {n} ∈ Fi for 1 ≤ i ≤ s, and Fi ∈ Fi for s + 1 ≤ i ≤ t. The size of ti=1 Fi is equal to

t

i=1

|Fi| =

s

i=1

(ki − 1) +

t

i=s+1

ki =

t

i=1

ki − s ≤ n − s ,

so there exist distinct elements x1,... ,xs  ∈ ti=1 Fi. Since Fi ∪ {n} is invariant under the shift Snxi, the set Fi ∪ {xi} = (Fi ∪ {n}) \ {n} ∪ {xi} must also be in the family Fi. Taking Fi′ = Fi ∪ {xi} for 1 ≤ i ≤ s, together with Fi for s +1 ≤ i ≤ t, it is clear that we have found pairwise disjoint sets from Fi, contradiction. ✷

- 3 Main result


In this section, we discuss the Erd˝os conjecture and its multicolored generalizations, and prove the original conjecture for the range t < 3nk2. The colored interpretation arises from considering the collection of families Fi as a single uniform hypergraph (possibly with repeated edges) on the vertex set [n], where each set in Fi introduces a hyperedge colored in the i-th color. The following lemma is a multicolored generalization of Theorem 10.3 in [8], and provides a suﬃcient condition for a multicolored hypergraph to contain a rainbow matching of size t.

![image 14](<2011-huang-size-hypergraph-its-matching_images/imageFile14.png>)

Lemma 3.1 Let F1, ..., Ft be families of subsets of [n] such that for each i, Fi only contains sets of size ki, |Fi| > (t − 1) k n−1

i−1 , and n ≥ ti=1 ki. Then there exist t pairwise disjoint sets F1 ∈ F1,

..., Ft ∈ Ft.

Proof. We proceed by induction on t and n. The case t = 1 is trivial. For general t, we can also handle all minimal cases of the form n = ti=1 ki. Indeed, consider a uniformly random permutation π of [n], and deﬁne a series of indicator random variables {Xi} as follows: X1 = 1 iﬀ {π(1),... ,π(k1)} is

a set in F1 and X1 = 0 otherwise, and in general, Xj = 1 iﬀ {π(k1+···+kj−1+1),... ,π(k1+···+kj)} is a set in Fj. We assume that there are no t disjoint sets from diﬀerent families, so we deterministically have:

X1 + ··· + Xt ≤ t − 1. (2)

On the other hand, it is easy to see that the expectation of Xi is the probability that a random ki-set is in Fi, so

|Fi| n ki

EXi =

.

![image 15](<2011-huang-size-hypergraph-its-matching_images/imageFile15.png>)

Yet we know that for every i, we have |Fi| > (t − 1) k n−1

i−1 , so

(t − 1) k n−1

ki n

i−1

= (t − 1)

.

EXi >

![image 16](<2011-huang-size-hypergraph-its-matching_images/imageFile16.png>)

![image 17](<2011-huang-size-hypergraph-its-matching_images/imageFile17.png>)

n ki

Summing these inequalities over 1 ≤ i ≤ t, we obtain that ti=1 EXi > t − 1, a contradiction to (2).

Now we consider a generic instance with n > ti=1 ki, and inductively assume that all instances with smaller n are known. By Lemma 2.1, after applying all shifts {Sni}1≤i≤n−1, we obtain families in which any rainbow t-matching can be pulled back to a rainbow t-matching in {Fi}. For convenience we still call the shifted families {Fi}. Our next step is to partition each Fi into Fi(n) ∪ Fi(¯n), but in order to avoid empty sets, we ﬁrst dispose of the case when there is some ki = 1 with {n} ∈ Fi. After re-indexing, we may assume that this is F1. Since |Fi| > (t − 1) k n−1

i−1 and there are at most

n−1 ki−1 sets containing n, every other Fi has more than (t − 2) k n−1

i−1 sets which in fact lie in [n − 1]. By induction on the t − 1 sizes k2,... ,kt, we ﬁnd t − 1 such disjoint sets from F2, .. ., Ft which, together with {n} ∈ F1, establish the claim.

Returning to the general case, since |Fi| = |Fi(n)| + |Fi(¯n)| and our size condition is

|Fi| > (t − 1)

n − 1 ki − 1

= (t − 1)

n − 2 ki − 2

+ (t − 1)

n − 2 ki − 1

,

i−2 or |Fi(¯n)| > (t − 1) k n−2

we conclude that for each i, either |Fi(n)| > (t − 1) k n−2

i−1 . Without loss of generality, we may assume that |Fi(n)| > (t − 1) k n−2

i−2 for 1 ≤ i ≤ s, and |Fi(¯n)| > (t − 1) k n−2

i−1 for s + 1 ≤ i ≤ t. Note that Fi is (ki − 1)-uniform for 1 ≤ i ≤ s and ki-uniform for s + 1 ≤ i ≤ t, and the base set now has n − 1 elements. Induction on n and Lemma 2.2 then produce t disjoint sets from diﬀerent families. ✷

As mentioned in the introduction, the conjectured extremal hypergraph when t ≤ k+1n is the hypergraph consisting of all edges intersecting a ﬁxed set of size t−1. If we inspect the vertex degree sequence of this hypergraph, we observe that although there are t−1 vertices with high degree nk−−11 , the remaining vertices only have degree nk−−11 − k n−−1t . For small t, this is asymptotically about (t − 1) nk−−22 , which is much smaller than nk−−11 = nk−−11 nk−−22 . The following corollary of Lemma 3.1 shows that this sort of phenomenon generally occurs when hypergraphs satisfy the conditions in the Erd˝os conjecture.

![image 18](<2011-huang-size-hypergraph-its-matching_images/imageFile18.png>)

![image 19](<2011-huang-size-hypergraph-its-matching_images/imageFile19.png>)

Corollary 3.2 If a k-uniform hypergraph H on n vertices has t distinct vertices v1, ..., vt with degrees d(vi) > 2(t − 1) nk−−22 , and kt ≤ n, then H contains t disjoint edges.

Proof. Let Hi be a (k − 1)-uniform hypergraph containing all the subsets of V (H) \ {v1,... ,vt} of size k − 1 which together with vi form an edge of H. For any ﬁxed 1 ≤ i ≤ t and j = i, there are at most nk−−22 edges of H containing both vertices vi and vj. Therefore for every hypergraph Hi,

e(Hi) ≥ d(vi) − (t − 1)

n − 2 k − 2

> (t − 1)

n − 2 k − 2

≥ (t − 1)

n − t − 1 k − 2

.

Since every hypergraph Hi is (k − 1)-uniform and has n − t vertices, we can use Lemma 3.1 with Fi = E(Hi), ki = k − 1 and n replaced by n − t, to ﬁnd t disjoint edges e1 ∈ E(H1), ... , et ∈ E(Ht). Taking the edges ei ∪ {vi} ∈ E(H), we obtain t disjoint edges in the original hypergraph H. ✷

Now we are ready to prove our main result, Theorem 1.2, which states that for t < 3nk2, every k-uniform hypergraph on n vertices without t disjoint edges contains at most nk − n−kt+1 edges.

![image 20](<2011-huang-size-hypergraph-its-matching_images/imageFile20.png>)

Proof of Theorem 1.2. We proceed by induction on t. The base case t = 1 is trivial, so we consider the general case, assuming that the t − 1 case is known. Suppose e(H) > nk − n−kt+1 , and let us seek t disjoint edges in H. We ﬁrst consider the situation when there is a vertex v of degree d(v) > k(t − 1) nk−−22 . Let Hv be the sub-hypergraph induced by the vertex set V (H) \ {v}. Since there are at most nk−−11 edges containing v,

e(Hv) ≥ e(H) −

n − 1 k − 1

>

=

n k

−

n − 1 k

n − t + 1 k

n − 1 k − 1

−

(n − 1) − (t − 1) + 1 k

−

.

By induction, there are t − 1 disjoint edges e1, .. ., et−1 in Hv, spanning (t − 1)k distinct vertices u1, ... , u(t−1)k. Note that the number of edges containing v and any vertex uj is at most nk−−22 . Therefore since we assumed that d(v) > k(t − 1) nk−−22 , there must be another edge et which contains v but avoids u1, .. ., u(t−1)k. We then have t disjoint edges e1,... ,et in H.

Now suppose that the maximum vertex degree in H is at most k(t − 1) nk−−22 . After re-indexing the vertices, we may assume that k(t − 1) nk−−22 ≥ d(v1) ≥ ··· ≥ d(vn). If the t-th largest degree satisﬁes d(vt) > 2(t − 1) nk−−22 , then Corollary 3.2 immediately produces t disjoint edges in H, so we may also assume for the remainder that d(vt) ≤ 2(t − 1) nk−−22 .

By induction (with room to spare), we also know that there are t−1 disjoint edges in H, spanning

(t − 1)k vertices. Among these vertices, the t − 1 largest degrees are at most k(t − 1) nk−−22 by our maximum degree assumption, while the remaining (t−1)(k−1) vertices cannot have degrees exceeding

d(vt) ≤ 2(t − 1) nk−−22 . Therefore the sum of degrees of these (t − 1)k vertices is at most

(t − 1) · k(t − 1)

n − 2 k − 2

+ (t − 1)(k − 1) · 2(t − 1)

n − 2 k − 2

= (t − 1)2(3k − 2)

n − 2 k − 2

.

However, we know that the total number of edges exceeds

n − t + 1 k

n k

−

e(H) >

t − 1 n − k + 1

t − 1 n

··· 1 −

= 1 − 1 −

![image 21](<2011-huang-size-hypergraph-its-matching_images/imageFile21.png>)

![image 22](<2011-huang-size-hypergraph-its-matching_images/imageFile22.png>)

k n k

t − 1 n

≥ 1 − 1 −

![image 23](<2011-huang-size-hypergraph-its-matching_images/imageFile23.png>)

t − 1 n

≥ k ·

−

![image 24](<2011-huang-size-hypergraph-its-matching_images/imageFile24.png>)

k 2

≥

(n − 1)(t − 1) k − 1

−

![image 25](<2011-huang-size-hypergraph-its-matching_images/imageFile25.png>)

t − 1 n

![image 26](<2011-huang-size-hypergraph-its-matching_images/imageFile26.png>)

2 n(n − 1) k(k − 1)

![image 27](<2011-huang-size-hypergraph-its-matching_images/imageFile27.png>)

(t − 1)2 2

![image 28](<2011-huang-size-hypergraph-its-matching_images/imageFile28.png>)

n − 2 k − 2

,

n k

n − 2 k − 2

where we used that (1 − x)k ≤ 1 − kx + k2 x2 when 0 ≤ kx ≤ 1. Since n > 3k2t, we also have n − 1 > 3k(k − 1)(t − 1). Therefore,

- 1

![image 29](<2011-huang-size-hypergraph-its-matching_images/imageFile29.png>)

- 2


e(H) > (t − 1)2 3k −

n − 2 k − 2

,

and so there is another edge in H disjoint from the previous t − 1 edges, again producing t disjoint edges in H. ✷

Based on the same idea and technique, we can also obtain a multicolored version of the Erd˝os conjecture, which is an analogue of a theorem of Kleitman [10] for matching number greater than one. Note that Theorem 1.2 is the F1 = ··· = Ft case of the following result.

Theorem 3.3 Let F1, ..., Ft be k-uniform families of subsets of [n], where t < 3nk2, and every |Fi| > nk − n−kt+1 . Then there exist pairwise disjoint sets F1 ∈ F1, ..., Ft ∈ Ft.

![image 30](<2011-huang-size-hypergraph-its-matching_images/imageFile30.png>)

Proof. For any vertex v ∈ Fi, let Hvj be the sub-hypergraph of Fj induced by the vertex set [n]\{v}. Then as in the previous proof,

e(Hvj) ≥ |Fi| −

n − 1 k − 1

>

n − 1 k

−

(n − 1) − (t − 1) + 1 k

.

By induction on t, for every i there exist t − 1 disjoint edges {ej}j =i such that ej ∈ Hvj. So as before, if some Fi has a vertex with degree d(v) > k(t − 1) nk−−22 , then there is an edge in Fi which contains v and is disjoint from {ej}j =i. Hence we may assume the maximum degree in each hypergraph Fi is

- at most k(t − 1) nk−−22 . On the other hand, by induction on t we also know that for every i there exist t−1 disjoint edges


from the families {Fj}j =i, spanning (t − 1)k vertices. If some Fi has t-th largest degree at most 2(t − 1) nk−−22 , then the sum of degrees of these (t − 1)k vertices in Fi is again at most

(t − 1)2(3k − 2)

n − 2 k − 2

≤

n k

−

n − t + 1 k

< e(Fi),

which guarantees the existence of an edge in Fi disjoint from the previous t − 1 edges from {Fj}j =i. So, we may assume that each Fi contains at least t vertices with degree above 2(t − 1) nk−−22 .

Now select distinct vertices vi, such that for each 1 ≤ i ≤ t, the degree of vi in Fi exceeds

2(t − 1) nk−−22 . Consider all the subsets of [n] \ {v1,... ,vt} which together with vi form an edge of Fi. Denote this (k − 1)-uniform hypergraph by Ti. The same calculation as in Corollary 3.2 gives

e(Ti) > (t − 1)

n − t − 1 k − 2

.

Applying Lemma 3.1 to {Ti}, we again ﬁnd t disjoint edges from diﬀerent families, as desired. ✷

# 4 Concluding Remarks

- • In this paper, we proved that for t < 3nk2, every k-uniform hypergraph on n vertices with matching

![image 31](<2011-huang-size-hypergraph-its-matching_images/imageFile31.png>)

number less than t has at most nk − n−kt+1 edges. This veriﬁes the conjecture of Erd˝os in this range of t, and improves upon the previously best known range by a factor of k. As we discussed

in the introduction, if the Erd˝os conjecture is true in general, then for t < k+1n , the maximum number of edges cannot exceed nk − n−kt+1 . It would be very interesting to tighten the range to t < O nk .

![image 32](<2011-huang-size-hypergraph-its-matching_images/imageFile32.png>)

![image 33](<2011-huang-size-hypergraph-its-matching_images/imageFile33.png>)

- • A fractional matching in a k-uniform hypergraph H = (V,E) is a function w : E → [0,1] such that

for each v ∈ V we have e∋v w(e) ≤ 1. The size of w is the sum e∈E w(e), and the size of the largest fractional matching in H is denoted by ν∗(H). The fractional version of the Erd˝os conjecture states that among k-uniform hypergraphs H on n vertices with fractional matching number ν∗(H) < xn, the maximum number of edges is asymptotically (1 + o(1))max (kx)k,1 − (1 − x)k nk .

It appears that these conjectures are closely related to several other interesting problems. For example, it was shown in [3] that the integral version can be used to determine the minimum degree condition which ensures the existence of perfect matchings in uniform hypergraphs. Furthermore, it turns out that the fractional version is closely related to an old probability conjecture of Samuels [12] and in computer science, it has applications to ﬁnding optimal data allocations in distributed storage systems (see [3] for more details). In [2], the fractional Erd˝os conjecture was used to attack an old problem of Manickam-Miklo´s-Singhi, which states that for n ≥ 4k, every set of n real numbers with nonnegative sum has at least nk−−11 k-element subsets whose sums are also nonnegative.

- • Pyber [11] proved the following product-type generalization of the Erd˝os-Ko-Rado theorem. Let F1 and F2 be families of k1- and k2-element subsets of [n]. If every pair of sets F1 ∈ F1 and F2 ∈ F2


intersects, then |F1||F2| ≤ k n−1

n−1 k2−1 for suﬃciently large n. The special case when k1 = k2 and F1 = F2 corresponds to the Erd˝os-Ko-Rado theorem. Our Theorem 3.3 is a minimum-type result of similar ﬂavor. Hence, it would be interesting to study the following multicolor analogue of Pyber’s result.

1−1

Question 4.1 What is the maximum of ti=1 |Fi| among families F1,... ,Ft of subsets of [n], where each Fi is ki-uniform, and there are no t pairwise disjoint subsets F1 ∈ F1, ..., Ft ∈ Ft?

Acknowledgments The authors would like to thank the anonymous referee for carefully reading the paper and the many helpful comments.

# References

- [1] R. Aharoni and D. Howard, Size conditions for the existence of rainbow matchings, in preparation.
- [2] N. Alon, H. Huang and B. Sudakov, Nonnegative k-sums, fractional covers, and probability of small deviations, submitted.
- [3] N. Alon, P. Frankl, H. Huang, V. Ro¨dl, A. Rucin´ski and B. Sudakov, Large matchings in uniform hypergraphs and the conjectures of Erd˝os and Samuels, submitted.
- [4] B. Bollob´as, D. E. Daykin and P. Erd˝os, Sets of independent edges of a hypergraph, Quart. J. Math. Oxford Ser. (2), 27 (1976), no. 105, 25–32.
- [5] P. Erd˝os, A problem on independent r-tuples, Ann. Univ. Sci. Budapest. Eo¨tv¨os Sect. Math. 8

(1965), 93–95.

- [6] P. Erd˝os and T. Gallai, On the maximal paths and circuits of graphs, Acta Math. Acad. Sci. Hung., 10 (1959), 337–357.
- [7] P. Erd˝os, C. Ko and R. Rado, Intersection theorems for systems of ﬁnite sets, Quart. J. Math. Oxford Ser. (2) , 12 (1961), 313–318.
- [8] P. Frankl, The shifting techniques in extremal set theory, in: Surveys in Combinatorics, Lond. Math. Soc. Lect. Note Ser. 123 (1987), 81–110.
- [9] P. Frankl, V. Ro¨dl, and A. Rucin´ski, On the maximum number of edges in a triple system not containing a disjoint family of a given size, submitted.
- [10] D. Kleitman, On a conjecture of Milner on k-graphs with non-disjoint edges, J. Combinatorial Theory, 5 (1968), 153–156.
- [11] L. Pyber, A new generalization of the Erd˝os-Ko-Rado theorem, J. Combin. Theory Ser. A, 43

(1986), no. 1, 85–90.

- [12] S. M. Samuels, On a Chebyshev-type inequality for sums of independent random variables, Ann. Math. Statist. 37 (1966), 248–259.


