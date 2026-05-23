arXiv:1710.07664v2[math.CO]17Jul2018

# On the Tur´an number of some ordered even cycles

Ervin Gy˝ori ∗1 D´aniel Kora´ndi †2 Abhishek Methuku ∗3 Istva´n Tomon †2 Casey Tompkins ∗1 Ma´t´e Vizer ‡1

1Alfr´ed R´enyi Institute of Mathematics, Hungarian Academy of Sciences.

gyori.ervin@renyi.mta.hu, {ctompkins496,vizermate}@gmail.com 2Ecole´ Polytechnique F´ed´erale de Lausanne. {daniel.korandi,istvan.tomon}@epfl.ch 3Central European University, Budapest. abhishekmethuku@gmail.com

November 4, 2021

Abstract

A classical result of Bondy and Simonovits in extremal graph theory states that if a graph on n vertices contains no cycle of length 2k then it has at most O(n1+1/k) edges. However, matching lower bounds are only known for k = 2,3,5.

In this paper we study ordered variants of this problem and prove some tight estimates for a certain class of ordered cycles that we call bordered cycles. In particular, we show that the maximum number of edges in an ordered graph avoiding bordered cycles of length at most 2k is Θ(n1+1/k).

Strengthening the result of Bondy and Simonovits in the case of 6-cycles, we also show that it is enough to forbid these bordered orderings of the 6-cycle to guarantee an upper bound of O(n4/3) on the number of edges.

Keywords: Geometric graph, Tura´n number, Ordered hexagon, Bordered cycle AMS Subj. Class. (2010): 05D99, 51E99

![image 1](<2017-gyri-tur-number-some-ordered_images/imageFile1.png>)

∗Research supported by NKFIH grant K116769. †Research supported by SNSF grants 200020-162884 and 200021-175977. ‡Research supported by NKFIH grant SNN 116095.

## 1 Introduction

Tura´n-type problems are generally formulated in the following way: one ﬁxes some graph properties and tries to determine the maximum or minimum number of edges an n-vertex graph with the prescribed properties can have. These kinds of extremal problems have a rich history in combinatorics, going back to 1907, when Mantel [14] determined the maximum number of edges possible in a triangle-free graph. The systematic study of these problems began with Tura´n [20], who generalized Mantel’s result to arbitrary complete graphs.

For simple graphs G and H, we say that G is H-free if G does not contain H as a subgraph. Given a graph G, its vertex set and edge set are denoted by V (G) and E(G), respectively.

- Deﬁnition 1. Given a graph H and a positive integer n, the Tura´n number of H is ex(n, H) := max{|E(G)| : |V (G)|= n and G is H-free}.


Erd˝os, Stone and Simonovits [4, 6] showed that the behavior of the Tura´n number of a general graph H is determined by its chromatic number, χ(H), when χ(H) ≥ 3 . They proved that if H is a simple graph, then

1 χ(H) − 1

ex(n, H) = 1 −

![image 2](<2017-gyri-tur-number-some-ordered_images/imageFile2.png>)

n2 2

+ o(n2),

![image 3](<2017-gyri-tur-number-some-ordered_images/imageFile3.png>)

which is an asymptotically correct result except when H is bipartite.

In the bipartite case, one of the most natural problems is to estimate the Tura´n number of even cycles. A classical result of Bondy and Simonovits [1] from 1974 is the following.

1

- Theorem 1 (Bondy–Simonovits). For any k ≥ 2, we have ex(n, C2k) = O(n1+


k).1

![image 4](<2017-gyri-tur-number-some-ordered_images/imageFile4.png>)

A major open question in extremal graph theory is whether this upper bound gives the correct order of magnitude. This was veriﬁed for k = 2, 3 and 5. For example, the best known bounds for hexagons are due to F¨uredi, Naor and Verstra¨ete [8], who proved that

0.5338 n4/3 ≤ ex(n, C6) ≤ 0.6272 n4/3. (1)

The corresponding girth problem was studied by Erd˝os and Simonovits [5], who conjectured that the same lower bound holds even if we also forbid cycles of shorter lengths.

- Conjecture 1 (Erdo˝s–Simonovits). For any k ≥ 2, we have


1

ex(n, {C3, . . ., C2k}) = Θ(n1+

k).

![image 5](<2017-gyri-tur-number-some-ordered_images/imageFile5.png>)

Once again, this conjecture is only known to hold for k = 2, 3, 5. For a survey on the extremal number of bipartite graphs, we refer the reader to [9].

![image 6](<2017-gyri-tur-number-some-ordered_images/imageFile6.png>)

1In this paper we use the standard asymptotic notations O,o,Θ understood as n → ∞. The parameter

- k is always assumed to be a constant.


### 1.1 Ordered graphs and forbidden submatrices

An ordered graph is a simple graph G = (V, E) with a linear ordering on its vertex set. We say that the ordered graph H is an ordered subgraph of G if there is an embedding of H in G that respects the ordering of the vertices. The Tura´n problem for a set of ordered graphs H asks the following. What is the maximum number ex<(n, H) of edges that an ordered graph on n vertices can have without containing any H ∈ H as an ordered subgraph? When H contains a single ordered graph H, we simply write ex<(n, H).

The systematic study of this problem was initiated by Pach and Tardos [16]. They noted that the following analog of the Erd˝os–Stone–Simonovits result holds (see also [3]):

1 χ<(H) − 1

ex<(n, H) = 1 −

![image 7](<2017-gyri-tur-number-some-ordered_images/imageFile7.png>)

n2 2

+ o(n2),

![image 8](<2017-gyri-tur-number-some-ordered_images/imageFile8.png>)

where χ<(H), the interval chromatic number of H, is the minimum number of intervals the (linearly ordered) vertex set of H can be partitioned into, so that no two vertices belonging to the same interval are adjacent in H. This formula determines the asymptotics of the ordered Tura´n number, except when χ<(H) = 2.

The case χ<(H) = 2 turns out to be closely related to a well-studied problem of forbidden patterns in 0-1 matrices. To formulate it, let AH be the bipartite adjacency matrix of H, where rows and columns correspond to the two intervals of H (in the appropriate ordering), and 1-entries correspond to edges in H. Then we are interested in the maximum number of 1-entries in an n × m matrix that does not contain the pattern AH in the sense that AH is not a submatrix, nor can it be obtained from a submatrix by changing some 1-entries to 0-entries.

The problem of ﬁnding the extremal number of matrix patterns was introduced by F¨uredi and Hajnal [7] about 25 years ago, and several results have been obtained since then (see e.g. [12, 15, 16, 18] and the references therein), although most of them concern matrices of acyclic graphs. One notable exception is a result of Pach and Tardos [16] that establishes ex<(n, H) = Θ(n4/3) for an inﬁnite set of ordered cycles H that they call “positive” cycles. The deﬁnition of positive cycles is motivated by an incidence geometry problem, where they correspond to a class of forbidden conﬁgurations.

In this paper we estimate ex<(n, H) for various ﬁnite sets H of ordered cycles that all come from the class of bordered cycles that we deﬁne as follows. In an ordered graph with interval chromatic number 2 and intervals U and V (U preceding V ), we call the edge connecting the ﬁrst vertex of U and the last vertex of V an outer border, and the edge connecting the last vertex of U and the ﬁrst vertex of V an inner border. Then a bordered cycle is an ordered cycle with interval chromatic number 2 that contains both an inner and an outer border. For example, out of the six ordered bipartite 6-cycles, three are bordered (see Figure 1).

Let us emphasize that there is no containment relationship between our bordered cycles and the positive cycles of Pach and Tardos. For example, using the notation of Figure 1, the positive 6-cycles are C61, C63, C6I and C6O, whereas the bordered 6-cycles are C61, C62 and C63.

C61

C6I

C62

C6U

C63

C6O

C6B

Figure 1: Bordered (C6B = {C61, C62, C63}), outbordered (C6O), unbordered (C6U) and inbordered (C6I) 6-cycles. Orderings shown in the same row can be obtained from each other by reversing the order of vertices in the second interval.

### 1.2 Our results

Let C2Bk be the set of bordered 2k-cycles. Our main result determines the asymptotics of the maximum number of edges in an ordered graph with no bordered cycle of length up to 2k. This can be thought of as an analog of Conjecture 1 for bordered cycles.

- Theorem 2. For every ﬁxed integer k > 1,

ex<(n, {C4B, C6B, . . ., C2Bk}) = Θ(n1+1/k). We do not know whether the bordered version of Theorem 1 is true in general, i.e.,

if forbidding C2Bk alone suﬃces to get the same asymptotic upper bound for the extremal number. However, we can prove this for k = 3.

- Theorem 3. For bordered 6-cycles,

ex<(n, C6B) = Θ(n4/3). Actually, Theorem 3 is an immediate consequence of Theorem 2 and the fact that when

- l − 1 divides k − 1, then any C2Bk-free ordered graph contains a large C2Bl-free subgraph. This is established by the following theorem.


- Theorem 4. Let k, l ≥ 2 be integers such that k − 1 is divisible by l − 1. Then any C2Bk-free ordered graph G contains a C2Bl-free subgraph with at least kl−−11 fraction of the edges of G.


![image 9](<2017-gyri-tur-number-some-ordered_images/imageFile9.png>)

Note that for l = 2, Theorem 4 is a generalization of a theorem of K¨uhn and Osthus [13] which states that any bipartite C2k-free graph G contains a C4-free subgraph with at least

1/(k − 1) fraction of the edges of G. Indeed, if we order the vertices of G so that all of the vertices in one of its color classes appear before the vertices of the other color class, then any C4 in G is bordered. Then Theorem 4 gives a C4-free subgraph of G that has at least 1/(k − 1) fraction of the edges of G.

This paper is organized as follows. In Section 2 we prove the lower bound of Theorem 2 by constructing a dense ordered graph without short ordered cycles. The matching upper bound is shown in Section 3. In Section 4 we give a short proof of Theorem 4. We conclude the paper with some remarks and open problems in Section 5.

## 2 Lower bound construction

Our construction is based on generalized Sidon sets deﬁned as follows.

- Deﬁnition 2. Let k ≥ 2 be an integer. A set of integers S is called a Bk-set if all k-sums of elements in S are diﬀerent, i.e., if for every integer C, there is at most one solution to


x1 + x2 + · · · + xk = C

in S, up to permuting the elements xi (the xi need not be distinct). We denote the maximum size of a Bk-set S ⊆ {1, 2, . . ., n} by Fk(n).

Note that this deﬁnition implies that if x1 + x2 + · · · + xl = x′1 + x′2 + · · · + x′l for some l ≤ k and xi, x′i ∈ S, then {x1, x2, . . ., xl} = {x′1, x′2, . . ., x′l} as multisets.

Bose and Chowla [2] proved that Fk(n) ≥ n1/k + o(n1/k).

For a ﬁxed n ≥ 1, let S ⊂ {1, 2, ..., n} be a Bk-set of size |S| = Fk(n). Our construction will be an ordered graph G on 4n vertices that we deﬁne through its bipartite adjacency matrix AG ∈ {0, 1}2n×2n as follows. For 1 ≤ i, j ≤ 2n we put

AG(i, j) =

1 if i − j + n ∈ S and 1 ≤ i ≤ n 0 otherwise.

We will prove that G contains no 2l-cycle with a border edge for any l ≤ k. Note that the edges of a 2l-cycle correspond to 1-entries in S at coordinates (i1, j1), . . ., (i2l, j2l), where

- 1. i2s−1 = i2s and j2s−1 = j2s for s = 1, 2, . . ., l, and
- 2. j2s = j2s+1 and i2s = i2s+1 for s = 1, 2, . . ., l (taking indices modulo 2l).


This readily implies ls=1 i2s = ls=1 i2s−1 and ls=1 j2s = ls=1 j2s−1, and in particular

l

(i2s − j2s + n) =

s=1

l

(i2s−1 − j2s−1 + n). (2)

s=1

By the deﬁnition of AG, we know that is − js + n ∈ S for every 1 ≤ s ≤ 2l, so both sides of (2) are l-sums in S. But S was a Bk-set with l ≤ k, so by the observation above, the two sums must have the same terms (possibly in a diﬀerent order).

However, an outer (resp. inner) border of this cycle uniquely minimizes (resp. maximizes) is−js over all s = 1, 2, . . ., 2l so if our cycle has a border edge, then there is a unique number among the terms, a contradiction.

Therefore, G does not contain any cycle of length at most 2k with a border edge, and it is easy to see that it contains nFk(n) ≥ n1+1/k + o(n1+1/k) edges. This proves the lower bound of Theorem 2.

## 3 Upper bound

Let G = (V, E) be an ordered graph on the vertex set V = {x1 < x2 < · · · < xn} that avoids all cycles in C4B, . . ., C2Bk. We want to show that the number of edges m in G is O(n1+1/k). Let us call a path P = v0v1 . . .vk k-zigzag, if vk < vk−2 < · · · < v0 < v1 < v3 < · · · < vk−1 for k even, and vk−1 < vk−3 < · · · < v0 < v1 < v3 < · · · < vk for k odd.

- Claim 1. The graph G contains at most one k-zigzag path between any pair of vertices.

Proof. Suppose to the contrary that v0 . . .vk and v0′ . . .vk′ are two diﬀerent k-zigzag paths such that v0 = v0′ and vk = vk′ . Let s ∈ {0, . . ., k} be the largest index such that vi = vi′ for every i ∈ {0, . . ., s}, and let t be the smallest index larger than s such that vt = vt′. Then vsvs+1 . . .vtvt′−1vt′−2 . . . vs′ are the consecutive vertices of a cycle of length 2(t − s), where 2 ≤ t − s ≤ k. Also, this cycle has two border edges, namely vs min{vs+1, vs′+1} and max{vt−1, vt′−1}vt. But then G contains a cycle in C2(Bt−s), a contradiction.

![image 10](<2017-gyri-tur-number-some-ordered_images/imageFile10.png>)

![image 11](<2017-gyri-tur-number-some-ordered_images/imageFile11.png>)

![image 12](<2017-gyri-tur-number-some-ordered_images/imageFile12.png>)

![image 13](<2017-gyri-tur-number-some-ordered_images/imageFile13.png>)

This tells us that the number of k-zigzag paths in G is at most n2. Now let us bound the number of k-zigzag paths from below.

- Claim 2. The graph G contains at least


mk kk(3n)k−1 k-zigzag paths.

![image 14](<2017-gyri-tur-number-some-ordered_images/imageFile14.png>)

Proof. We will deﬁne a sequence of graphs Gk, . . ., G1 ⊆ G recursively as follows. We set Gk = G, and we will obtain Gi−1 from Gi by deleting the edges between each vertex and its u = ⌊m/2kn⌋ largest and u smallest neighbors.

More precisely, we deﬁne the left and right neighborhood of a vertex xs ∈ V in Gi as Li(xs) = {xj : j < s, xjxs ∈ Gi} and Ri(xs) = {xj : j > s, xsxj ∈ Gi},

respectively. Also, let L+i (xs) be the u smallest elements of Li(xs), and let Ri+(xs) be the u largest elements of Ri(xs). (If |Li(xs)|< u, then we deﬁne L+i (xs) = Li(xs), and we do the same for Ri+(xs).) We then set

Gi−1 = Gi \

n

{xjxs : xj ∈ L+i (xs)} ∪

s=1

n

{xsxj : xj ∈ Ri+(xs)} .

s=1

Let us collect some properties of the graphs Gi.

- 1. We delete at most 2nu ≤ m/k edges from Gi to obtain Gi−1, so we have |E(Gi)|≥ mi/k for every i, and in particular, |E(G1)|≥ m/k.
- 2. For every x ∈ V and every i, we have L+2i(x) < L+2i+2(x) and R2+i+1(x) < R2+i−1(x), where we write A < B for some sets A, B ⊂ V if maxA < minB.
- 3. For every x ∈ V , if L2i−1(x) is non-empty, then |L+2i(x)|= u. Similarly, if R2i(x) is non-empty, then |R2+i+1(x)|= u.

Now we show that for every edge f = v0v1 ∈ G1, there are at least uk−1 k-zigzag paths starting with f. Observe that every sequence of vertices v0, v1, . . ., vk satisfying vi ∈ L+i (vi−1) for i even, and vi ∈ Ri+(vi−1) for i odd is a k-zigzag path by property 2. Also, the number of such paths is exactly uk−1 by property 3. Hence, using u ≥ m/3kn, we have at least |E(G1)|uk−1 > mk/kk(3n)k−1 diﬀerent k-zigzag paths in G.

![image 15](<2017-gyri-tur-number-some-ordered_images/imageFile15.png>)

![image 16](<2017-gyri-tur-number-some-ordered_images/imageFile16.png>)

![image 17](<2017-gyri-tur-number-some-ordered_images/imageFile17.png>)

![image 18](<2017-gyri-tur-number-some-ordered_images/imageFile18.png>)

Now comparing our lower and upper bound for the number of k-zigzag paths in G, we arrive at the inequality

n2 ≥

mk kk(3n)k−1

![image 19](<2017-gyri-tur-number-some-ordered_images/imageFile19.png>)

, which yields m < 3kn1+1/k.

![image 20](<2017-gyri-tur-number-some-ordered_images/imageFile20.png>)

![image 21](<2017-gyri-tur-number-some-ordered_images/imageFile21.png>)

![image 22](<2017-gyri-tur-number-some-ordered_images/imageFile22.png>)

![image 23](<2017-gyri-tur-number-some-ordered_images/imageFile23.png>)

- 4 Deleting small cycles


Our proof of Theorem 4 is inspired by the proof of Gr´sz, Methuku and Tompkins in [11] on deleting 4-cycles, which is a simple proof of a theorem of K¨uhn and Osthus [13]. We make use of the following result of Gallai [10] and Roy [17].

- Theorem 5 (Gallai–Roy). If a directed graph G contains no directed path of length h then χ(G) ≤ h.


Proof of Theorem 4. Let G = (V, E) be an ordered graph which is C2Bk-free, where the elements of V are x1 < · · · < xn. Deﬁne the directed graph H on E as a vertex set such that for f, f′ ∈ E,

−→ ff′ is a directed edge of H if there exists a bordered 2l-cycle with outer border f

−→ ff′ ∈ E(H), where f = ab, f′ = a′b′,

and inner border f′. Note that H is acyclic, because if

a < b and a′ < b′, then a < a′ < b′ < b.

We show that the longest directed path in H has length less than h = kl−−11. Suppose to the contrary that there is a directed path f1 . . .fh+1 in H. Then for every i = 1, . . ., h, there is a bordered cycle Ci with outer border fi and inner border fi+1. Then it is easy to see that

![image 24](<2017-gyri-tur-number-some-ordered_images/imageFile24.png>)

- h
- i=1 Ci \ {f2, . . ., fh} is a bordered cycle of length 2lh − 2h + 2 = 2k, with outer border


f1, and inner border fh+1, contradicting the choice of G. Hence we can apply Theorem 5 to get a proper h-coloring of H. Here the largest color

class E0 ⊆ E is an independent set of size at least kl−−11 |E|, so there is no cycle in C2Bl that has all its edges in E0. The edges of E0 will then form an ordered subgraph of G that satisﬁes our conditions.

![image 25](<2017-gyri-tur-number-some-ordered_images/imageFile25.png>)

![image 26](<2017-gyri-tur-number-some-ordered_images/imageFile26.png>)

![image 27](<2017-gyri-tur-number-some-ordered_images/imageFile27.png>)

![image 28](<2017-gyri-tur-number-some-ordered_images/imageFile28.png>)

![image 29](<2017-gyri-tur-number-some-ordered_images/imageFile29.png>)

## 5 Concluding remarks

Note that Theorem 3 is stronger than the k = 3 case of Theorem 1 because it only forbids three out of the six orderings of the hexagon. In fact, it is enough to forbid two orderings of the hexagon to achieve the same asymptotic bound.

- Theorem 6. Let C1 = {C62, C61}, C2 = {C62, C63}, C3 = {C6U, C6I}, and C4 = {C6U, C6O}. For any i ∈ {1, 2, 3, 4}, we have ex<(n, Ci) = Θ(n4/3).


Sketch of the proof. It is enough to show that every Ci-free ordered graph G on 2n vertices has O(n4/3) edges between the ﬁrst n and the last n vertices. Indeed, an inductive argument applied to the two halves of G then yields a O(n4/3) upper bound on the total number of edges, as well. We ﬁrst show this for C1, so let G be an ordered graph on the vertex set A ∪ B with |A|= |B|= n and A < B that has no edges induced by A or B, and avoids C61 and C62.

Note that G cannot contain two bordered 4-cycles such that the inner border of one is the outer border of the other, because they would create a copy of C62. So by the argument of Theorem 4, we can assume that G does not contain any bordered 4-cycle. The rest of the proof follows that of Theorem 2; we only need that, analogously to Claim 1, if for some x ∈ A, y ∈ B, we have two 3-zigzag paths P1 and P2 from x to y, then P1 ∪ P2 is either C61 or C62, or it induces a bordered 4-cycle. So we once again get that the number of 3-zigzag paths in G is at most n2, and can ﬁnish the argument as before.

To obtain an upper bound on ex<(n, Ci) for i ∈ {2, 3, 4}, note that we can obtain each Ci from C1 by reversing the order of the vertices in one (or both) of the color intervals. This means, for example, that the graph G above is C1-free if and only if the graph G′, obtained from G by reversing the order of vertices in B, is C3-free. In particular, such a G′ has O(n4/3) edges, and a similar reduction works for all other i.

![image 30](<2017-gyri-tur-number-some-ordered_images/imageFile30.png>)

![image 31](<2017-gyri-tur-number-some-ordered_images/imageFile31.png>)

![image 32](<2017-gyri-tur-number-some-ordered_images/imageFile32.png>)

![image 33](<2017-gyri-tur-number-some-ordered_images/imageFile33.png>)

As we mentioned before, Pach and Tardos [16] showed that ex<(n, C) = Θ(n4/3) for a certain set of cycles that they call “positive”. They also asked if it would be enough to forbid the positive 6-cycles (i.e., C61, C63, C6O, C6I) to get the same upper bound. More generally, we propose the following conjecture.

- Conjecture 2. Let C be an ordered 6-cycle of interval chromatic number 2. Then ex<(n, C) = Θ(n4/3).


Finally, let us remark that while we are unable to prove that ex<(n, C2Bk) = O(n1+1/k), there is certainly no absolute constant ε > 0 such that ex<(n, C2Bk) ≥ n1+ε for every k:

- Theorem 7. There exists a sequence of positive real numbers (λk)k=2,3,... such that ex<(n, C2Bk) =


O(n1+λ

) and liminfk→∞ λk = 0.

k

Proof. We will show that we can choose λ(m−1)!+1 = 1/m. Let k = (m − 1)! +1 and let G be a C2Bk-free ordered graph with n vertices. Then for any 2 ≤ l ≤ m, l − 1 divides k − 1. Therefore, applying Theorem 4 repeatedly, we obtain a subgraph G′ of G such that G′ is {C4B, C6B, . . ., C2Bm}-free, and G′ has at least (m − 1)! /(k − 1)m−1 proportion of the edges of G. But then, by Theorem 2, |E(G′)|= O(n1+1/m), and thus |E(G)|= O(n1+1/m), as well.

![image 34](<2017-gyri-tur-number-some-ordered_images/imageFile34.png>)

![image 35](<2017-gyri-tur-number-some-ordered_images/imageFile35.png>)

![image 36](<2017-gyri-tur-number-some-ordered_images/imageFile36.png>)

![image 37](<2017-gyri-tur-number-some-ordered_images/imageFile37.png>)

After our paper was submitted, we learned that Timmons [19] also studied the Tura´n number of ordered cycles, and observed that ex<(n, C2k) = O(n1+1/k) for the family C2k of all ordered 2k-cycles with interval chromatic number 2. On the other hand, he found the construction we presented in Section 2, and asked whether a matching upper bound holds, i.e., if the upper bound O(n1+1/k) holds when only the ordered 2k-cycles with an inner or an outer border are forbidden. Our Theorem 3 (or Theorem 6) answers this question positively for k = 3 (for an even smaller subfamily), and Theorem 2 answers a variant for every k where shorter cycles are also forbidden. We kept the construction in this paper for completeness.

Acknowledgments. We thank Ga´bor Tardos for fruitful discussions, and Craig Timmons for bringing [19] to our attention. We also thank the referees for their valuable comments.

## References

- [1] J. Bondy, M. Simonovits. Cycles of even length in graphs. J. Combin. Theory Ser. B, 16(2), 97–105, 1974.
- [2] R. C. Bose, S. Chowla. Theorems in the additive theory of numbers. Comment. Math. Helv., 37(1), 141–147, 1962.
- [3] P. Brass, Gy. Ka´rolyi, P. Valtr. A Tura´n-type extremal theory of convex geometric graphs. Discrete and Computational Geometry, Springer Berlin Heidelberg, 275–300, 2003.
- [4] P. Erd˝os, M. Simonovits. A limit theorem in graph theory. Studia Sci. Math. Hung. 1, 51–57, 1965.
- [5] P. Erd˝os, M. Simonovits. Compactness results in extremal graph theory. Combinatorica 2, 275–288, 1982.


- [6] P. Erd˝os, A. H. Stone. On the structure of linear graphs. Bull. Amer. Math. Soc. 52, 1087–1091, 1946.
- [7] Z. F¨uredi, P. Hajnal. Davenport-Schinzel theory of matrices. Discrete Math., 103(3), 233–251, 1992.
- [8] Z. F¨uredi, A. Naor, J. Verstra¨ete. On the Tura´n number for the hexagon. Adv. Math. 203(2), 476–496, 2006.
- [9] Z. F¨uredi, M. Simonovits. The history of degenerate (bipartite) extremal graph problems. Erd˝s Centennial, Springer Berlin Heidelberg, 169–264, 2013.
- [10] T. Gallai. On directed paths and circuits. In: P. Erd˝s, G. Katona: Theory of Graphs, pp. 115–118 Tihany, New York: Academic Press, 1968.
- [11] D. Gr´sz, A. Methuku, C. Tompkins. On subgraphs of C2k-free graphs and a problem of K¨uhn and Osthus. arXiv preprint arXiv:1708.05454, 2017.
- [12] D. Kor´andi, G. Tardos, I. Tomon, C. Weidert. On the Tura´n number of ordered forests. arXiv preprint arXiv:1711.07723, 2017.
- [13] D. K¨uhn, D. Osthus. Four-cycles in graphs without a given even cycle. J. Graph Theory 48(2), 147–156, 2005.
- [14] W. Mantel. Problem 28. Wiskundige Opgaven 10, 60–61, 1907.
- [15] A. Marcus, G. Tardos. Excluded permutation matrices and the Stanley-Wilf conjecture. J. Combin. Theory Ser. A 107(1), 153–160, 2004.
- [16] J. Pach, G. Tardos. Forbidden paths and cycles in ordered graphs and matrices. Israel J. Math., 155(1), 359–380, 2006.
- [17] B. Roy. Nombre chromatique et plus longs chemins d’un graph. Rev. AFIRO 1, 127–132, 1967.
- [18] G. Tardos. On 0-1 matrices and small excluded submatrices. J. Combin. Theory Ser. A 111(2), 266–288, 2005.
- [19] C. Timmons. An ordered Tura´n problem for bipartite graphs. Electron. J. Combin. 19(4), #P43, 2012.
- [20] P. Tura´n. An extremal problem in graph theory. Mat. Fiz. Lapok 48, 436–452, 1941. [Hungarian]


