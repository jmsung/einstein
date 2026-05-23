---
type: source
kind: paper
title: Large feedback arc sets, high minimum degree subgraphs, and long cycles in Eulerian digraphs
authors: Hao Huang, Jie Ma, Asaf Shapira, Benny Sudakov, Raphael Yuster
year: 2012
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/1202.2602v1
source_local: ../raw/2012-huang-large-feedback-arc-sets.pdf
topic: general-knowledge
cites:
---

arXiv:1202.2602v1[math.CO]13Feb2012

Large feedback arc sets, high minimum degree subgraphs, and long cycles in Eulerian digraphs

Hao Huang∗ Jie Ma† Asaf Shapira ‡ Benny Sudakov§ Raphael Yuster ¶

Abstract

A minimum feedback arc set of a directed graph G is a smallest set of arcs whose removal makes G acyclic. Its cardinality is denoted by β(G). We show that an Eulerian digraph with n vertices and m arcs has β(G) ≥ m2/2n2 + m/2n, and this bound is optimal for inﬁnitely many m,n. Using this result we prove that an Eulerian digraph contains a cycle of length at most 6n2/m, and has an Eulerian subgraph with minimum degree at least m2/24n3. Both estimates are tight up to a constant factor. Finally, motivated by a conjecture of Bollob´as and Scott, we also show how to ﬁnd long cycles in Eulerian digraphs.

Keywords: Eulerian digraph, feedback arc set, girth, long cycles AMS Subject classiﬁcation: 05C20, 05C70

# 1 Introduction

One of the central themes in graph theory is to study the extremal graphs which satisfy certain properties. Extremity can be taken with respect to diﬀerent parameters as order, size, or girth. There are many classical results in this area. For example, any undirected graph G with n vertices and m edges has a subgraph with minimum degree at least m/n, and thus G also contains a cycle of length at least m/n + 1. It is natural to ask whether such results can be extended to digraphs. However, it turns out that these statements are often trivially false even for very dense general digraphs. For instance, a transitive tournament does not contain any cycle, and its subgraphs always have zero minimum in-degree and out-degree. Therefore in order to obtain meaningful results as in the undirected case, it is necessary to restrict to a smaller family of digraphs. A natural candidate one may consider is the family of Eulerian digraphs, in which the in-degree

![image 1](<2012-huang-large-feedback-arc-sets_images/imageFile1.png>)

∗Department of Mathematics, UCLA, Los Angeles, CA 90095. Email: huanghao@math.ucla.edu. Research

supported by a UC Dissertation Year Fellowship. †Department of Mathematics, UCLA, Los Angeles, CA 90095. Email: jiema@math.ucla.edu. ‡School of Mathematics, Tel-Aviv University, Tel-Aviv, Israel 69978, and Schools of Mathematics and Computer

Science, Georgia Institute of Technology, Atlanta, GA 30332. Email: asafico@math.gatech.edu. Supported in part by NSF Grant DMS-0901355 and ISF Grant 224/11.

§Department of Mathematics, UCLA, Los Angeles, CA 90095. Email: bsudakov@math.ucla.edu. Research supported in part by NSF grant DMS-1101185, NSF CAREER award DMS-0812005, and by a USA-Israeli BSF grant.

¶Department of Mathematics, University of Haifa, Haifa 31905, Israel. Email: raphy@math.haifa.ac.il.

equals the out-degree at each vertex. In this paper, we investigate several natural parameters of Eulerian digraphs, and study the connections between them. In particular, the parameters we consider are minimum feedback arc set, shortest cycle , longest cycle, and largest minimum degree subgraph. Throughout this paper, we always assume the Eulerian digraph is simple, i.e. it has no multiple arcs or loops, but arcs in diﬀerent directions like (u,v) and (v,u) are allowed. For other standard graph-theoretic terminology involved, the reader is referred to [2].

A feedback arc set of a digraph is a set of arcs whose removal makes the digraph acyclic. Given a digraph G, denote by β(G) the minimum size of a feedback arc set. Computing β(G) and ﬁnding a corresponding minimum feedback arc set is a fundamental problem in combinatorial optimization. It has applications in many other ﬁelds such as testing of electronic circuits and eﬃcient deadlock resolution (see, e.g., [8, 10]). However, computing β(G) turns out to be diﬃcult, and it is NP-hard even for tournaments [1, 5]. One basic question in this area is to bound β(G) as a function of other parameters of G, and there are several papers (see, e.g., [6, 7, 11]) studying upper bounds for β(G) of this form. However, much less is known for the lower bound of β(G), perhaps because a general digraph could be very dense and still have a small minimum feedback arc set. For example, a transitive tournament has β(G) = 0. Nevertheless, it is easy to see that any Eulerian digraph G with n vertices and m arcs has β(G) ≥ m/n, since the arcs can be decomposed into a disjoint union of cycles, each of length at most n, and any feedback arc set contains at least one arc from each cycle. In this paper we actually prove the following much stronger lower bound for β(G).

Theorem 1.1. Every Eulerian digraph G with n vertices and m arcs has β(G) ≥ m2/2n2 +m/2n.

Moreover, Theorem 1.1 is tight for an inﬁnite family of Eulerian digraphs, as can be seen from the following proposition. Proposition 1.2. For every pair of integers m and n such that m is divisible by n, there exists an Eulerian digraph G with n vertices and m arcs, and with β(G) = m2/2n2 + m/2n.

The study of the existence of cycles plays a very important role in graph theory, and there are numerous results for undirected graphs in the classical literature. However, there are signiﬁcantly fewer results for digraphs. The main reason for this is probably because digraphs often behave more similar to hypergraphs, and questions concerning cycles in digraphs are often much more diﬃcult than the corresponding questions in graphs. One of the most famous problems in this area is the celebrated Caccetta-H¨aggkvist conjecture [4]: every directed n-vertex digraph with minimum outdegree at least r contains a cycle with length at most ⌈n/r⌉, which is not completely solved even when restricted to Eulerian digraphs (for more discussion, we direct the interested reader to the surveys [9, 12]). In this paper, we study the existence of short cycles in Eulerian digraphs with a given order and size. The girth g(G) of a digraph G is deﬁned as the length of the shortest cycle in G. Combining Theorem 1.1 and a result of Fox, Keevash and Sudakov [7] which connects β(G) and g(G) for a general digraph G, we are able to obtain the following corollary.

Corollary 1.3. Every Eulerian digraph G with n vertices and m arcs has g(G) ≤ 6n2/m.

We also point out that the upper bound in Corollary 1.3 is tight up to a constant, since the construction of Proposition 1.2 also provides an example of Eulerian digraphs with girth at least n2/m.

A repeated application of Corollary 1.3 gives an Eulerian subgraph of the original digraph G, whose arc set is a disjoint union of Ω(m2/n2) cycles. Using this fact we can ﬁnd an Eulerian subgraph of G with large minimum degree.

Theorem 1.4. Every Eulerian digraph G with n vertices and m arcs has an Eulerian subgraph with minimum degree at least m2/24n3. This bound is tight up to a constant for inﬁnitely many m,n.

In 1996, Bollob´s and Scott ([3], Conjecture 6) asked whether every Eulerian digraph G with nonnegative arc-weighting w contains a cycle of weight at least cw(G)/(n − 1), where w(G) is the total weight and c is some absolute constant. For the unweighted case, i.e. w = 1, this conjecture becomes: “Is it true that every Eulerian digraph with n vertices and m arcs contains a cycle of length at least cm/n?” Even this special case is still wide open after 15 years. An obvious consequence of Theorem 1.4 is that every Eulerian digraph contains a cycle of length at least 1 + m2/24n3. When the digraph is dense, i.e. m = cn2, our theorem provides a cycle of length linear in n, which partially veriﬁes the Bollob´s-Scott conjecture in this range. However observe that when m is small, in particular when m = o(n3/2), Theorem 1.4 becomes meaningless. Nevertheless, we can always ﬁnd a long cycle of length at least ⌊ m/n⌋ + 1, as shown by the following proposition1.

![image 2](<2012-huang-large-feedback-arc-sets_images/imageFile2.png>)

Proposition 1.5. Every Eulerian digraph G with n vertices and m arcs has a cycle of length at least 1 + ⌊ m/n⌋. Together with Theorem 1.4, this implies that G has a cycle of length at least

![image 3](<2012-huang-large-feedback-arc-sets_images/imageFile3.png>)

- 1 + max{m2/24n3,⌊ m/n⌋}.

![image 4](<2012-huang-large-feedback-arc-sets_images/imageFile4.png>)

The rest of this paper is organized as follows. In Section 2, we obtain our bounds for feedback arc sets by proving Theorem 1.1 and Proposition 1.2. Section 3 contains the proof of our results for the existences of short cycles, long cycles, and subgraph with large minimum degree. The ﬁnal section contains some concluding remarks and open problems.

- 2 Feedback arc sets


This section contains the proofs of Theorem 1.1 and Proposition 1.2. Consider some linear order of the vertex set of an Eulerian digraph G = (V,E) with n vertices and m arcs. Let vi is the i’th vertex in this order. We say that vi is before vj if i < j. An arc (vi,vj) is a forward arc if i < j, and is a backward arc if i > j. Observe that any cycle contains at least one backward arc. Hence, the set of backward arcs forms a feedback arc set. We prove Theorem 1.1 by showing that any linear order of V has at least as many backward arcs as the amount stated in the theorem. We ﬁrst require the following simple lemma. Here a cut is deﬁned as a partition of the vertices of a digraph into two disjoint subsets.

![image 5](<2012-huang-large-feedback-arc-sets_images/imageFile5.png>)

1This proposition was also obtained independently by Jacques Verstraete.

- Lemma 2.1. In any cut (A,V \ A) of an Eulerian digraph, the number of arcs from A to V \ A equals the number of arcs from V \ A to A.


Proof. The sum of the out-degrees of the vertices of A equals the sum of the in-degrees of the vertices of A. Each arc with both endpoints in A contributes one unit to each of these sums. Hence, the number of arcs with only one endpoint in A splits equally between arcs that go from A to V \ A and arcs that go from V \ A to A.

![image 6](<2012-huang-large-feedback-arc-sets_images/imageFile6.png>)

![image 7](<2012-huang-large-feedback-arc-sets_images/imageFile7.png>)

![image 8](<2012-huang-large-feedback-arc-sets_images/imageFile8.png>)

![image 9](<2012-huang-large-feedback-arc-sets_images/imageFile9.png>)

Proof of Theorem 1.1. Fix an Eulerian digraph G with |V | = n and |E| = m. We claim that it suﬃces to only consider Eulerian digraphs which are 2-cycle-free, i.e. between any pair of vertices {i,j}, there do not exist arcs in two diﬀerent directions. Suppose there are k diﬀerent 2-cycles in G. By removing all of them, we delete exactly 2k arcs. Note that the resulting 2-cycle-free digraph G′ is still Eulerian and contains m − 2k arcs. Therefore if Theorem 1.1 is true for all 2-cycle-free Eulerian digraphs, then

(m − 2k)2 2n2

m − 2k 2n

β(G′) ≥

.

+

![image 10](<2012-huang-large-feedback-arc-sets_images/imageFile10.png>)

![image 11](<2012-huang-large-feedback-arc-sets_images/imageFile11.png>)

Obviously in any linear order of V (G), exactly half of the 2k arcs deleted must be backward arcs. Therefore,

(m − 2k)2 2n2

m − 2k 2n

β(G) ≥ β(G′) + k ≥

+

+ k =

![image 12](<2012-huang-large-feedback-arc-sets_images/imageFile12.png>)

![image 13](<2012-huang-large-feedback-arc-sets_images/imageFile13.png>)

2k n2 n2

m2 2n2

m2 2n2

m 2n −

k n

+ k −

≥

+

=

+

![image 14](<2012-huang-large-feedback-arc-sets_images/imageFile14.png>)

![image 15](<2012-huang-large-feedback-arc-sets_images/imageFile15.png>)

![image 16](<2012-huang-large-feedback-arc-sets_images/imageFile16.png>)

![image 17](<2012-huang-large-feedback-arc-sets_images/imageFile17.png>)

![image 18](<2012-huang-large-feedback-arc-sets_images/imageFile18.png>)

m2 2n2

+

![image 19](<2012-huang-large-feedback-arc-sets_images/imageFile19.png>)

m 2n

.

![image 20](<2012-huang-large-feedback-arc-sets_images/imageFile20.png>)

2k(m − k) n2

m 2n −

k n

+ k −

![image 21](<2012-huang-large-feedback-arc-sets_images/imageFile21.png>)

![image 22](<2012-huang-large-feedback-arc-sets_images/imageFile22.png>)

![image 23](<2012-huang-large-feedback-arc-sets_images/imageFile23.png>)

The last inequality follows from the fact that m − k ≤ n2 , since m − k counts the number of pairs of vertices with an arc between them.

From now on, we always assume that G is a 2-cycle-free Eulerian digraph. In order to prove a lower bound on β(G), we ﬁx a linear order v1,... ,vn. It will be important for the analysis to consider the length of an arc (vi,vj) which is |i−j|. Observe that the length of any arc is an integer in {1,... ,n − 1}. Moreover, we call an arc short if its length is at most n/2. Otherwise, it is long.

Partition the arc set E into two parts, S and L, where S contains the short arcs and L contains the long arcs. For a vertex vi, let si denote the number of short arcs connecting vi with some vj where j > i. It is important to note that at this point we claim nothing regarding the directions of these arcs. Since G is 2-cycle-free, si ≤ n − i. As each short arc (vi,vj) contributes exactly one to either si or sj, we have that:

n

si = |S| .

i=1

We now estimate the sum of the lengths of the short arcs. Consider some vertex vi. Since G is 2-cycle-free, the si short arcs connecting vi to vertices appearing after vi must have distinct lengths. Hence, the sum of their lengths is at least 1 + 2 + ··· + si = si2+1 . Thus, denoting by w(S) the sum of the lengths of the short arcs, we have that

n

w(S) ≥

i=1

si + 1 2

. (1)

Next we calculate the sum of the lengths of the long arcs, that is denoted by w(L). There is at most one long arc of length n− 1. There are at most two arcs of length n −2, and, more generally, there are at most n − i arcs of length i. Thus, if we denote by ti the number of long arcs of length

- i for i ≥ ⌊n/2⌋ + 1 and set ti = 0 for i ≤ ⌊n/2⌋, we have that ti ≤ n − i, and


n

i · ti . (2)

w(L) =

i=1

Obviously,

n

n

si = |L| + |S| = m .

ti +

i=1

i=1

Let Ai = {v1,... ,vi} and consider the cuts Ci = (Ai,V \ Ai) for i = 1,... ,n. Let ci denote the number of arcs crossing Ci (and notice that cn = 0). Since an arc of length x crosses precisely x of these cuts, we have that

n

ci = w(S) + w(L) . (3)

i=1

Consider a pair of cuts Ci,Ci+⌊n/2⌋ for i = 1,... ,⌊n/2⌋. If an arc crosses both Ci and Ci+⌊n/2⌋ then its length is at least ⌊n/2⌋ + 1. Hence, a short arc cannot cross both of these cuts. Let yi denote the number of long arcs that cross both of these cuts. By Lemma 2.1, ci/2 backward arcs cross Ci and ci+⌊n/2⌋/2 backward arcs cross Ci+⌊n/2⌋, and we have counted at most yi such arcs twice. It follows that the number of backward arcs is at least

- 1

![image 24](<2012-huang-large-feedback-arc-sets_images/imageFile24.png>)

- 2


(ci + ci+⌊n/2⌋) − yi . Averaging over all ⌊n/2⌋ such pairs of cuts, it follows that the number of backward arcs is at least

⌊n/2⌋

1 ⌊n/2⌋

- 1

![image 25](<2012-huang-large-feedback-arc-sets_images/imageFile25.png>)

- 2


(ci + ci+⌊n/2⌋) − yi . (4)

![image 26](<2012-huang-large-feedback-arc-sets_images/imageFile26.png>)

i=1

As each long arc of length j crosses precisely j − ⌊n/2⌋ pairs of cuts Ci and Ci+⌊n/2⌋, we have that ⌊n/2⌋ i=1 yi = j≥⌊n/2⌋ tj(j −⌊n/2⌋) = w(L) −|L| · ⌊n/2⌋. This, together with (3) and (4) gives that

- 1

![image 27](<2012-huang-large-feedback-arc-sets_images/imageFile27.png>)

- 2


1 ⌊n/2⌋

(w(S) + w(L)) − (w(L) − |L| · ⌊n/2⌋)

β(G) ≥

![image 28](<2012-huang-large-feedback-arc-sets_images/imageFile28.png>)

w(S) − w(L) 2⌊n/2⌋

≥

+ |L| . (5) Note that when n = 2k is even, the above inequality becomes

![image 29](<2012-huang-large-feedback-arc-sets_images/imageFile29.png>)

w(S) − w(L) n

β(G) ≥

+ |L| .

![image 30](<2012-huang-large-feedback-arc-sets_images/imageFile30.png>)

Next we show that when n = 2k+1 is odd, the same inequality still holds. To see this, ﬁrst assume that w(S) ≥ w(L). Then applying inequality (5), we have that for n = 2k + 1,

w(S) − w(L) n

w(S) − w(L) 2k

+ |L| ≥

β(G) ≥

+ L .

![image 31](<2012-huang-large-feedback-arc-sets_images/imageFile31.png>)

![image 32](<2012-huang-large-feedback-arc-sets_images/imageFile32.png>)

Next suppose that w(S) < w(L). Instead of considering the cuts Ci and Ci+k, we look at the pair Ci and Ci+k+1 for i = 1,··· ,k. Moreover, denote by zi the number of long arcs that cross both of these cuts. By a similar argument as before, the number of backward arcs is at least 12(ci + ci+k+1) − zi for 1 ≤ i ≤ k, and ci/2 for i = k + 1. This provides k + 1 lower bounds for β(G), and we will average over all of them. Since each long arc of length j crosses precisely j − (k + 1) pairs of cuts Ci and Ci+k+1, we again have that ki=1 zi = j≥k+1 tj(j − (k + 1)) = w(L) − (k + 1)|L|, and we have that

![image 33](<2012-huang-large-feedback-arc-sets_images/imageFile33.png>)

k

- 1

![image 34](<2012-huang-large-feedback-arc-sets_images/imageFile34.png>)

- 2


ck+1 2 ≥

1 k + 1

(ci + ci+k+1) − zi +

β(G) ≥

![image 35](<2012-huang-large-feedback-arc-sets_images/imageFile35.png>)

![image 36](<2012-huang-large-feedback-arc-sets_images/imageFile36.png>)

i=1

- 1

![image 37](<2012-huang-large-feedback-arc-sets_images/imageFile37.png>)

- 2


1 k + 1

(w(S) + w(L)) − (w(L) − (k + 1)|L|)

![image 38](<2012-huang-large-feedback-arc-sets_images/imageFile38.png>)

w(S) − w(L) 2k + 2

w(S) − w(L) n

≥

+ |L| , where we use the fact that w(L) > w(S).

+ |L| ≥

![image 39](<2012-huang-large-feedback-arc-sets_images/imageFile39.png>)

![image 40](<2012-huang-large-feedback-arc-sets_images/imageFile40.png>)

Using our lower bound estimate (1) for w(S) and the expression (2) for w(L), we obtain that β(G) ≥

w(S) − w(L) n

+ |L|

![image 41](<2012-huang-large-feedback-arc-sets_images/imageFile41.png>)

n

n

n

si + 1 2 −

1 n

i · ti +

≥

ti (6)

![image 42](<2012-huang-large-feedback-arc-sets_images/imageFile42.png>)

i=1

i=1

i=1

n

si + 1 2

1 n

+ (n − i)ti .

=

![image 43](<2012-huang-large-feedback-arc-sets_images/imageFile43.png>)

i=1

Deﬁne

n

si + 1 2

+ (n − i)ti . In order to ﬁnd a lower bound of β(G), we need to solve the following integer optimization problem.

F(s1,··· ,sn;t1,··· ,tn) :=

i=1

F(m,n) := min F(s1,··· ,sn;t1,··· ,tn) subject to si ≤ n − i, ti ≤ n − i,

n

si +

i=1

n

ti = m .

i=1

The following Lemma 2.2 provides a precise solution to this optimization problem, which gives that F(m,n) = tm − (t2 − t)n/2, where t = ⌈m/n⌉. Hence if we assume that m = tn − k with

- 0 ≤ k ≤ n − 1, then


t2 − t 2

t2 − t 2

t(tn − k) n −

1 n

tm n −

β(G) ≥

F(m,n) =

=

![image 44](<2012-huang-large-feedback-arc-sets_images/imageFile44.png>)

![image 45](<2012-huang-large-feedback-arc-sets_images/imageFile45.png>)

![image 46](<2012-huang-large-feedback-arc-sets_images/imageFile46.png>)

![image 47](<2012-huang-large-feedback-arc-sets_images/imageFile47.png>)

![image 48](<2012-huang-large-feedback-arc-sets_images/imageFile48.png>)

k2 2n2 −

t2 + t 2 −

t2 + t 2 −

tk n ≥

tk n

k 2n

+

=

![image 49](<2012-huang-large-feedback-arc-sets_images/imageFile49.png>)

![image 50](<2012-huang-large-feedback-arc-sets_images/imageFile50.png>)

![image 51](<2012-huang-large-feedback-arc-sets_images/imageFile51.png>)

![image 52](<2012-huang-large-feedback-arc-sets_images/imageFile52.png>)

![image 53](<2012-huang-large-feedback-arc-sets_images/imageFile53.png>)

![image 54](<2012-huang-large-feedback-arc-sets_images/imageFile54.png>)

m2 2n2

(tn − k)2 2n2

tn − k 2n

m 2n

=

.

+

+

=

![image 55](<2012-huang-large-feedback-arc-sets_images/imageFile55.png>)

![image 56](<2012-huang-large-feedback-arc-sets_images/imageFile56.png>)

![image 57](<2012-huang-large-feedback-arc-sets_images/imageFile57.png>)

![image 58](<2012-huang-large-feedback-arc-sets_images/imageFile58.png>)

The last inequality is because 0 ≤ k ≤ n − 1, so 0 ≤ k/n < 1 and k2/2n2 ≤ k/2n. Note that equality is possible only when m is a multiple of n.

![image 59](<2012-huang-large-feedback-arc-sets_images/imageFile59.png>)

![image 60](<2012-huang-large-feedback-arc-sets_images/imageFile60.png>)

![image 61](<2012-huang-large-feedback-arc-sets_images/imageFile61.png>)

![image 62](<2012-huang-large-feedback-arc-sets_images/imageFile62.png>)

- Lemma 2.2. F(m,n) = tm − (t2 − t)n/2, where t = ⌈m/n⌉. Proof. The proof of this lemma consists of several claims. We assume that si + ti = ai, then


- 0 ≤ ai ≤ 2(n − i) and si ≤ n − i, so

si + 1 2

+ (n − i)ti =

- 1

![image 63](<2012-huang-large-feedback-arc-sets_images/imageFile63.png>)

- 2


s2i − (n − i − 1/2)si + (n − i)ai .

Since si is an integer, this function of si is minimized when si = n − i if ai ≥ n − i, and when si = ai if ai < n − i. Therefore, subject to i ai = m and ai ≤ 2(n − i), we want to minimize

F =

ai<n−i

ai + 1 2

+

ai≥n−i

n − i + 1 2

+ (n − i)(ai − (n − i))

=

ai<n−i

ai + 1 2

+

ai≥n−i

(n − i)ai −

n − i 2

. (7)

For convenience, deﬁne A = {i : ai < n − i}, and B = {i : ai ≥ n − i}.

- Claim 1. For any i ∈ A, if we increase ai by 1 then F increases by ai + 1, and if we decrease ai by 1 then F decreases by ai. For any j ∈ B, if we increase (decrease) aj by 1 then F increases (decreases) by n − j.

Proof. Note that when ai = n − i or n − i − 1, ai2+1 = (n − i)ai − n2−i , therefore if we increase ai by 1 for any i ∈ A, the contribution of ai to F always increases by ai2+2 − ai2+1 = ai + 1. When we decrease ai by 1, F decreases by ai2+1 − a2i = ai. It is also easy to see that for any j ∈ B, if we increase or decrease aj by 1, the contribution of aj to F always increases or decreases by n − j.

![image 64](<2012-huang-large-feedback-arc-sets_images/imageFile64.png>)

![image 65](<2012-huang-large-feedback-arc-sets_images/imageFile65.png>)

![image 66](<2012-huang-large-feedback-arc-sets_images/imageFile66.png>)

![image 67](<2012-huang-large-feedback-arc-sets_images/imageFile67.png>)

Next we show that for any extremal conﬁguration (a1,··· ,an) which minimizes F, any integer of A is smaller than any integer of B.

- Claim 2. F is minimized when A = {1,··· ,l − 1} and B = {l,··· ,n} for some integer l.

Proof. We prove by contradiction. Suppose this statement is false, then F is minimized by some {ai}ni=1 such that there exists i < j, i ∈ B and j ∈ A. Now we decrease ai by 1 and increase aj by 1, which can be done since aj < 2(n − j). Then by Claim 1, F decreases by (n − i) − (aj + 1) ≥ n − (j − 1) − (aj + 1) = (n − j) − aj > 0 since j ∈ A, which contradicts the minimality of F.

![image 68](<2012-huang-large-feedback-arc-sets_images/imageFile68.png>)

![image 69](<2012-huang-large-feedback-arc-sets_images/imageFile69.png>)

![image 70](<2012-huang-large-feedback-arc-sets_images/imageFile70.png>)

![image 71](<2012-huang-large-feedback-arc-sets_images/imageFile71.png>)

Since ni=1 ai = m, which is ﬁxed. The next claim shows that in order to minimize F, we need to take the variables whose index is in B to be as large as possible, with at most one exception.

- Claim 3. F is minimized when A = {1,··· ,l−1}, and B = {l,··· ,n} for some integer l. Moreover,




- ai = 2(n − i) for all i ≥ l + 1.


Proof. First note that for i ∈ B, its contribution to F is (n−i)ai − n−2 i . The second term is ﬁxed, and ai has coeﬃcient n − i which decreases in i. Therefore when F is minimized, if i is the largest index in B such that ai < 2(n − i), then all j < i in B must satisfy aj = n − j; otherwise we might decrease aj and increase ai to make F smaller. Therefore, if i > l, we have ai−1 = n − i + 1. Note that if we increase ai by 1 and decrease ai−1 by 1, by Claim 1 the target function F decreases by ai−1 − (n − i) = 1. Therefore the only possibility is that i = l, which proves Claim 3.

![image 72](<2012-huang-large-feedback-arc-sets_images/imageFile72.png>)

![image 73](<2012-huang-large-feedback-arc-sets_images/imageFile73.png>)

![image 74](<2012-huang-large-feedback-arc-sets_images/imageFile74.png>)

![image 75](<2012-huang-large-feedback-arc-sets_images/imageFile75.png>)

- Claim 4. There is an extremal conﬁguration for which ai = n − l or ai = n − l + 1 for i ≤ l − 1, al is between n − l and 2(n − l), and ai = 2(n − i) for i ≥ l + 1.


Proof. From Claim 3, we know that in an extremal conﬁguration, ai < n − i for 1 ≤ i ≤ l − 1, n − l ≤ al ≤ 2(n − l), and ai = 2(n − i) for i ≥ l + 1. Among all extremal conﬁgurations, we take one with the largest l, and for all such conﬁgurations, we take one for which al is the smallest. For such a conﬁguration, if we increase aj by 1 for some j ∈ A and decrease al by 1, then by Claim

- 1, F increases by (aj + 1) − (n − l), which must be nonnegative. Suppose aj + 1 = n − l. If j is changed to be in B, it contradicts Claim 3 no matter whether l remains in B or is changed to be in A; if j remains in A, it contradicts the maximality of l if l is changed to be in A or contradicts the minimality of al if l remains in B. Therefore aj ≥ n − l for every 1 ≤ j ≤ l − 1. We next consider two cases: either al is equal to 2(n − l), or strictly less than 2(n − l).


- Case 1. al = 2(n − l). From the discussions above, we already know that aj ≥ n − l for every 1 ≤ j ≤ l−1. In particular al−1 = n−l since it is strictly less than n−(l−1). If for some j ≤ l−1,

![image 76](<2012-huang-large-feedback-arc-sets_images/imageFile76.png>)

- aj ≥ n − l + 2, then we can decrease aj by 1 and increase al−1 by 1 since aj is strictly greater than


- 0 and al−1 is strictly less than 2(n − l + 1). By Claim 1, F decreases by aj − (n − l + 1) ≥ 1, which contradicts the minimality of F. Hence we have that n − l ≤ aj ≤ n − l + 1 for every j ≤ l − 1.


- Case 2. al < 2(n − l). If we decrease aj by 1 and increase al by 1, F decreases by aj − (n − l) by Claim 1, therefore aj ≤ n − l by the minimality of F, hence aj = n − l for all 1 ≤ j ≤ l − 1.


![image 77](<2012-huang-large-feedback-arc-sets_images/imageFile77.png>)

In both cases, the extremal conﬁguration consists of n−l or n−l+1 for the ﬁrst l−1 variables, al is between n − l and 2(n − l), and ai = 2(n − i) for i ≥ l + 1.

![image 78](<2012-huang-large-feedback-arc-sets_images/imageFile78.png>)

![image 79](<2012-huang-large-feedback-arc-sets_images/imageFile79.png>)

![image 80](<2012-huang-large-feedback-arc-sets_images/imageFile80.png>)

![image 81](<2012-huang-large-feedback-arc-sets_images/imageFile81.png>)

By Claim 4, we can bound the number of arcs m from both sides,

n

l−1

ai ≥ (l − 1)(n − l) + (n − l) +

ai +

m =

i=1

i=l

n

2(n − i) = (n − l)(n − 1) .

i=l+1

m =

l−1

ai +

i=1

n

ai < (l − 1)(n − l + 1) +

i=l

n

2(n − i) = (n − l + 1)(n − 1) .

i=l

Solving these two inequalities, we get n −

- m

![image 82](<2012-huang-large-feedback-arc-sets_images/imageFile82.png>)

- n − 1


- m

![image 83](<2012-huang-large-feedback-arc-sets_images/imageFile83.png>)

- n − 1 ≤ l < n + 1 −


.

Let m = tn − k, where t = ⌈m/n⌉ and 0 ≤ k ≤ n − 1. It is not diﬃcult to check that if t ≥ k, l = n − t and if t < k, l = n − t + 1.

Now let x be the number of variables a1,...,al−1 which are equal to n−l+1. Since ai = 2(n−i) for i ≥ l + 1, we have that

x + al = m − (l − 1)(n − l) −

ai = m − (n − 2)(n − l) . (8)

i≥l+1

When t ≥ k, then l = n − t and

x + al = m − (n − 2)t = 2t − k < 2t = 2(n − l),

hence al < 2(n − l). By the analysis of the second case in Claim 4, aj = n − l = t for all j ≤ l − 1, therefore x = 0 and al = 2t − k. Since l = n − t, then using the summation formula

n k=1 k2 = k(k + 1)(2k + 1)/6, we have from (7) that (with details of the calculation omitted)

- F =


t + 1 2

(n − t − 1) + t(2t − k) −

t 2

+

i≥l+1

2(n − i)2 −

n − i 2

= tm − (t2 − t)n/2 .

Now we assume t < k, then l = n − t + 1. Then using (8) again,

x + al = m − (n − 2)(t − 1) = n − k + 2(t − 1) > 2(t − 1) = 2(n − l) .

The only possibility without contradicting the second case in Claim 4 is that al = 2(n − l) and x = n − k. Thus, there are n − k of a1,...,al−1 which are equal to n − l + 1 = t and the rest k − t are equal to t − 1. Again by (7),

n − i 2

t + 1 2

t 2

2(n − i)2 −

= tm − (t2 − t)n/2 .

(n − k) +

(k − t) +

F =

i≥l

As we have covered both cases, we have completed the proof of Lemma 2.2.

![image 84](<2012-huang-large-feedback-arc-sets_images/imageFile84.png>)

![image 85](<2012-huang-large-feedback-arc-sets_images/imageFile85.png>)

![image 86](<2012-huang-large-feedback-arc-sets_images/imageFile86.png>)

![image 87](<2012-huang-large-feedback-arc-sets_images/imageFile87.png>)

Proof of Proposition 1.2. Now we construct an inﬁnite family of Eulerian digraphs which achieve the bound in Theorem 1.1. For any positive integers n,m such that t := m/n is an integer, we deﬁne the Cayley digraph G(n,m) to have vertex set {1,2,...,n} and arc set {(i,i + j) : 1 ≤

- i ≤ n,1 ≤ j ≤ t}, where all additions are modulo n. From the deﬁnition, it is easy to verify that G(n,m) is an Eulerian digraph. Consider an order of the vertex set such that vertex i is the i’th vertex in this order, we observe that for n − t + 1 ≤ i ≤ n, vertex i has backward arcs (i,j), where


- 1 + n − i ≤ j ≤ t and there is no backward arc from vertex i for i ≤ n − t. Therefore,


t

n

m2 2n2

t + 1 2

m 2n

t − (n − i) =

β(G(n,m)) ≤

j =

=

+

.

![image 88](<2012-huang-large-feedback-arc-sets_images/imageFile88.png>)

![image 89](<2012-huang-large-feedback-arc-sets_images/imageFile89.png>)

j=1

i=n−t+1

![image 90](<2012-huang-large-feedback-arc-sets_images/imageFile90.png>)

![image 91](<2012-huang-large-feedback-arc-sets_images/imageFile91.png>)

![image 92](<2012-huang-large-feedback-arc-sets_images/imageFile92.png>)

![image 93](<2012-huang-large-feedback-arc-sets_images/imageFile93.png>)

# 3 Short cycles, long cycles, and Eulerian subgraphs with high minimum degree

In this section, we prove the existence of short cycles, long cycles, and subgraphs with large minimum degree in Eulerian digraphs. An important component in our proofs is the following result by Fox, Keevash and Sudakov [7] on general digraphs. We point out that the original Theorem 1.2 in [7] was proved with a constant 25, which can be improved to 18 using the exact same proof if we further assume r ≥ 11.

Theorem 3.1. If a digraph G with n vertices and m arcs has β(G) > 18n2/r2, with r ≥ 11, then

- G contains a cycle of length at most r, i.e. g(G) ≤ r.


Applying this theorem and Theorem 1.1, we can now prove Corollary 1.3, which says that every Eulerian digraph G with n vertices and m arcs contains a cycle of length at most 6n2/m.

Proof of Corollary 1.3. Given an Eulerian digraph G with n vertices and m arcs, if G contains a 2-cycle, then g(G) ≤ 2 ≤ 6n2/m. So we may assume that G is 2-cycle-free and thus m ≤ n2 . By Theorem 1.1,

m2 2n2

18n2 (6n2/m)2

m2 2n2

m 2n

β(G) ≥

>

+

=

.

![image 94](<2012-huang-large-feedback-arc-sets_images/imageFile94.png>)

![image 95](<2012-huang-large-feedback-arc-sets_images/imageFile95.png>)

![image 96](<2012-huang-large-feedback-arc-sets_images/imageFile96.png>)

![image 97](<2012-huang-large-feedback-arc-sets_images/imageFile97.png>)

Since r = 6n2/m > 6n2/ n2 > 11, we can use Theorem 3.1 to conclude that

6n2 m

g(G) ≤ r =

.

![image 98](<2012-huang-large-feedback-arc-sets_images/imageFile98.png>)

To see that this bound is tight up to a constant factor, we consider the construction of the Cayley digraphs in Proposition 1.2. It is not hard to see that if k = m/n, the shortest directed cycle in G(n,m) has length at least ⌈n/k⌉ ≥ n2/m.

![image 99](<2012-huang-large-feedback-arc-sets_images/imageFile99.png>)

![image 100](<2012-huang-large-feedback-arc-sets_images/imageFile100.png>)

![image 101](<2012-huang-large-feedback-arc-sets_images/imageFile101.png>)

![image 102](<2012-huang-large-feedback-arc-sets_images/imageFile102.png>)

Next we show that every Eulerian digraph with n vertices and m arcs has an Eulerian subgraph with minimum degree Ω(m2/n3).

Proof of Theorem 1.4. We start with an Eulerian digraph G with n vertices and m arcs. Note that Corollary 1.3 implies that every Eulerian digraph with n vertices and at least m/2 arcs contains a cycle of length at most 12n2/m. In every step, we pick one such cycle and delete all of its arcs from G. Obviously the resulting digraph is still Eulerian, and this process will continue until there are less than m/2 arcs left in the digraph. Therefore through this process we obtain a collection C of t arc-disjoint cycles C1,··· ,Ct, where t ≥ (m − m/2)/(12n2/m) ≥ m2/24n2. Denote by H the union of all these cycles, obviously H is an Eulerian subgraph of G.

If H has minimum degree at least ⌈t/n⌉ ≥ m2/24n3, then we are already done. Otherwise, we repeatedly delete from H any vertex v with degree d(v) ≤ ⌈t/n⌉−1, together with all the d(v) cycles in C passing through v. This process stops after a ﬁnite number of steps. In the end we delete at most n(⌈t/n⌉ − 1) ≤ t − 1 cycles in C, so the resulting digraph H′ is nonempty. Moreover, every vertex in H′ has degree at least ⌈t/n⌉ ≥ m2/24n3. Since H′ is the disjoint union of the remaining cycles, it is also an Eulerian subgraph of G, and we conclude the proof of Theorem 1.4.

![image 103](<2012-huang-large-feedback-arc-sets_images/imageFile103.png>)

![image 104](<2012-huang-large-feedback-arc-sets_images/imageFile104.png>)

![image 105](<2012-huang-large-feedback-arc-sets_images/imageFile105.png>)

![image 106](<2012-huang-large-feedback-arc-sets_images/imageFile106.png>)

Remark. The proof of Theorem 1.4 also shows that G contains an Eulerian subgraph with minimum degree Ω(m2/n3) and at least Ω(m) arcs.

To see that the bound in Theorem 1.4 is tight up to a constant, for any integers s,t > 0, we construct an Eulerian digraph H := H(s,t) such that

- • V (H) = (U1 ∪ ··· ∪ Us) ∪ (V1 ∪ ... ∪ Vt), |Ui| = |Vj| = s for 1 ≤ i ≤ s,1 ≤ j ≤ t,
- • for any 1 ≤ i ≤ t − 1 and vertices u ∈ Vi, v ∈ Vi+1, the arc (u,v) ∈ E(H),
- • for any 1 ≤ i ≤ s and every vertex u ∈ Ui, there is an arc from u to the i’th vertex in V1, and another arc from the i’th vertex in Vt to u.


U1

U2

V1 V2

Vt

U3

Figure 1: The Eulerian digraph H(s,t) with s = 3

It can be veriﬁed that H(s,t) is an Eulerian digraph with (s + t)s vertices and s2(t + 1) arcs. Moreover, every cycle in H(s,t) must pass through a vertex in U1∪···∪Us, whose degree is exactly 1. Therefore any Eulerian subgraph of H(s,t) has minimum degree at most 1. Next we deﬁne the δ-blowup H(s,t,δ): for any integer δ > 0, we replace every vertex i ∈ V (H(s,t)) with an independent set |Wi| = δ, and each arc (i,j) ∈ E(H(s,t)) by a complete bipartite digraph with arcs directed from Wi to Wj. The blowup digraph H(s,t,δ) is still Eulerian, and has n = s(s + t)δ vertices and m = s2(t + 1)δ2 arcs. Taking t = 2s, we have that for H(s,2s,δ),

m2 n3

=

![image 107](<2012-huang-large-feedback-arc-sets_images/imageFile107.png>)

(s2(2s + 1)δ2)2 (s(s + 2s)δ)3

=

![image 108](<2012-huang-large-feedback-arc-sets_images/imageFile108.png>)

1 27

![image 109](<2012-huang-large-feedback-arc-sets_images/imageFile109.png>)

1 s

2 +

![image 110](<2012-huang-large-feedback-arc-sets_images/imageFile110.png>)

2

4 27

δ ≥

δ .

![image 111](<2012-huang-large-feedback-arc-sets_images/imageFile111.png>)

Note that similarly with the previous discussion on H(s,t), every cycle in the blowup H(s,2s,δ) contains at least one vertex with degree δ. Therefore, the minimum degree of any Eulerian subgraph of H(s,2s,δ) is at most δ ≤ 274

m2 n3 . This implies that the bound in Theorem 1.4 is tight up to a

![image 112](<2012-huang-large-feedback-arc-sets_images/imageFile112.png>)

![image 113](<2012-huang-large-feedback-arc-sets_images/imageFile113.png>)

constant factor for inﬁnitely many m,n. Before proving Proposition 1.5, let us recall the following easy fact.

![image 114](<2012-huang-large-feedback-arc-sets_images/imageFile114.png>)

![image 115](<2012-huang-large-feedback-arc-sets_images/imageFile115.png>)

![image 116](<2012-huang-large-feedback-arc-sets_images/imageFile116.png>)

![image 117](<2012-huang-large-feedback-arc-sets_images/imageFile117.png>)

Proposition 3.2. If a digraph G has minimum outdegree δ+(G), then G contains a directed cycle of length at least δ+(G) + 1.

Proof. Let P = v1 → v2 → ··· → vt be the longest directed path in G. Then all the out neighbors of vt must lie on this path, otherwise P will become longer. If i < t is minimal with (vt,vi) ∈ E(G), then vi → ··· → vt → vi gives a cycle of length at least d+(vt) + 1 ≥ δ+(G) + 1.

![image 118](<2012-huang-large-feedback-arc-sets_images/imageFile118.png>)

![image 119](<2012-huang-large-feedback-arc-sets_images/imageFile119.png>)

![image 120](<2012-huang-large-feedback-arc-sets_images/imageFile120.png>)

![image 121](<2012-huang-large-feedback-arc-sets_images/imageFile121.png>)

This proposition, together with Theorem 1.4, shows that an Eulerian digraph G with n vertices and m arcs contains a cycle of length at least 1+m2/24n3. But as we discussed in the introduction, this bound becomes meaningless when the number of arcs m is small. However, we may use a diﬀerent approach to obtain a cycle of length at least ⌊ m/n⌋ + 1.

![image 122](<2012-huang-large-feedback-arc-sets_images/imageFile122.png>)

Proof of Proposition 1.5. To prove that any Eulerian digraph G with n vertices and m arcs has a cycle of length at least ⌊ m/n⌋ + 1, we use induction on the number of vertices n. Note that the base case when n = 2 is obvious, since the only Eulerian digraph is the 2-cycle with ⌊ m/n⌋ + 1 = 2. Suppose the statement is true for n − 1. Consider an Eulerian digraph G with n vertices and m arcs. If its minimum degree δ+(G) ≥ ⌊ m/n⌋, by Proposition 3.2 G already contains a cycle of length at least 1+⌊ m/n⌋. Therefore we can assume that there exists a vertex v with ⌊ m/n⌋ > d+(v) := t. As G is Eulerian, there exist t arc-disjoint cycles C1,C2,...,Ct passing through v. If one of these cycles has length at least ⌊ m/n⌋ + 1 then again we are done. Otherwise, |Ci| ≤ ⌊ m/n⌋ for all 1 ≤ i ≤ t. Now we delete from G the vertex v together with the arcs of the cycles C1,··· ,Ct. The resulting Eulerian digraph has n − 1 vertices and m′ arcs, where m′ = m − ti=1 |Ci| ≥ m − t⌊ m/n⌋ ≥ m(1 − n1). By the inductive hypothesis, the new digraph (therefore G) has a cycle of length at least 1 + m′/(n − 1) ≥ 1 + m(1 − n1)/(n − 1) ≥ 1 + ⌊ m/n⌋.

![image 123](<2012-huang-large-feedback-arc-sets_images/imageFile123.png>)

![image 124](<2012-huang-large-feedback-arc-sets_images/imageFile124.png>)

![image 125](<2012-huang-large-feedback-arc-sets_images/imageFile125.png>)

![image 126](<2012-huang-large-feedback-arc-sets_images/imageFile126.png>)

![image 127](<2012-huang-large-feedback-arc-sets_images/imageFile127.png>)

![image 128](<2012-huang-large-feedback-arc-sets_images/imageFile128.png>)

![image 129](<2012-huang-large-feedback-arc-sets_images/imageFile129.png>)

![image 130](<2012-huang-large-feedback-arc-sets_images/imageFile130.png>)

![image 131](<2012-huang-large-feedback-arc-sets_images/imageFile131.png>)

![image 132](<2012-huang-large-feedback-arc-sets_images/imageFile132.png>)

![image 133](<2012-huang-large-feedback-arc-sets_images/imageFile133.png>)

![image 134](<2012-huang-large-feedback-arc-sets_images/imageFile134.png>)

![image 135](<2012-huang-large-feedback-arc-sets_images/imageFile135.png>)

![image 136](<2012-huang-large-feedback-arc-sets_images/imageFile136.png>)

![image 137](<2012-huang-large-feedback-arc-sets_images/imageFile137.png>)

![image 138](<2012-huang-large-feedback-arc-sets_images/imageFile138.png>)

![image 139](<2012-huang-large-feedback-arc-sets_images/imageFile139.png>)

# 4 Concluding remarks

We end with some remarks on the Bollob´s-Scott conjecture whose unweighted version states that an Eulerian digraph with n vertices and m arcs has a cycle of length Ω(m/n). The “canonical” proof for showing that an undirected graph with this many vertices and edges has a cycle of length m/n proceeds by ﬁrst passing to a subgraph G′ with minimum degree at least m/n and then applying

- Proposition 3.2 to G′. We can then interpret the second statement of Theorem 1.4 as stating that when applied to Eulerian digraphs, this approach can only produce cycles of length O(m2/n3).


There is, however, another way to show that an undirected graph has a cycle of length m/n using DFS. Recall that the DFS (Depth First Search) is a graph algorithm that visits all the vertices of a (directed or undirected) graph G as follows. It maintains three sets of vertices, letting S be the set of vertices which we have completed exploring them, T be the set of unvisited vertices, and U = V (G) \ (S ∪T), where the vertices of U are kept in a stack (a last in, ﬁrst out data structure). The DFS starts with S = U = ∅ and T = V (G).

While there is a vertex in V (G) \ S, if U is non-empty, let v be the last vertex that was added to U. If v has a neighbor u ∈ T, the algorithm inserts u to U and repeats this step. If v does

not have a neighbor in T then v is popped out from U and is inserted to S. If U is empty, the algorithm chooses an arbitrary vertex from T and pushes it to U. Observe crucially that all the vertices in U form a directed path, and that there are no edges from S to T.

Consider any DFS tree T rooted at some vertex v. Recall that any edge of G is either an edge of T or a backward edge, that is, an edge connecting a vertex v to one of its ancestors in T. Hence, if G has no cycle of length at least t, then any vertex of T sends at most t−1 edges to his ancestors in T. This means that m ≤ nt or that t ≥ m/n. Note that this argument shows that any DFS tree of an undirected graph has depth at least m/n. It is thus natural to try and adapt this idea to the case of Eulerian digraphs. Unfortunately, as the following proposition shows, this approach fails in Eulerian digraphs.

- Proposition 4.1. There is an Eulerian digraph G with average degree at least √n/20 such that some DFS tree of G has depth 4.


![image 140](<2012-huang-large-feedback-arc-sets_images/imageFile140.png>)

Proof. We ﬁrst deﬁne a graph G′ as follows. Let t be a positive integer and let G′ be a graph consisting of 2t vertex sets V1,... ,V2t, each of size t. We also have a special vertex r, so G′ has 2t2 + 1 vertices. We now deﬁne the arcs of G′ using the following iterative process. We have t iterations, where in iteration 1 ≤ j ≤ t we add the following arcs; we have t arcs pointing from r to the t vertices of Vj, then a matching between the t vertices of Vj to the vertices of Vj+1, and in general a matching between Vk to Vk+1 for every j ≤ k ≤ 2t − j. We ﬁnally have t arcs from V2t−j+1 to r. We note that we can indeed add a new (disjoint from previous ones) matching between any pair of sets (Vk,Vk+1) in each of the t iterations by relying on the fact that the edges of the complete bipartite graph Kt,t can be split into t perfect matchings. Observe that in iteration

- j we add t(2t − 2j + 3) arcs to G′. Hence G′ has


t

t(2t − 2j + 3) ≥ t3

j=1

arcs. Moreover it is easy to see from construction that G′ is Eulerian. To get the graph G we modify G′ as follows; for every vertex v ∈ 2i=1t Vi we add two new vertices vin,vout and add a 4-cycle (r,vin,v,vout,r). We get that G has 6t2 + 1 vertices and more than t3 arcs, so setting n = 6t2 + 1 we see that G has average degree at least √n/20.

![image 141](<2012-huang-large-feedback-arc-sets_images/imageFile141.png>)

Now consider a DFS tree of G which proceeds as follows; we start at r, and then for every v ∈ V2t go to vin then to v and then to vout. Next, for every v ∈ V2t−1 we go to vin then to v and then to vout. We continue this way until we cover all the vertices of G. The DFS tree we thus get has r as its root, and 2t2 paths of length 3 (of type r,vin,v,vout) attached to it.

![image 142](<2012-huang-large-feedback-arc-sets_images/imageFile142.png>)

![image 143](<2012-huang-large-feedback-arc-sets_images/imageFile143.png>)

![image 144](<2012-huang-large-feedback-arc-sets_images/imageFile144.png>)

![image 145](<2012-huang-large-feedback-arc-sets_images/imageFile145.png>)

Observe that the above proposition does not rule out the possibility that some DFS tree has depth Ω(m/n). We note that proving such a claim will imply that an Eulerian digraph has a path of length Ω(m/n). It appears that even this special case of the Bollob´s-Scott conjecture is still open, so it might be interesting to further investigate this problem. In fact, we suspect that if G is a connected Eulerian digraph then for any vertex v ∈ G there is a path of length Ω(m/n) starting

at v. This statement for undirected graphs follows from the DFS argument at the beginning of this section.

Acknowledgment: We would like to thank Jacques Verstraete for helpful initial discussions.

# References

- [1] N. Alon, Ranking tournaments, SIAM J. Discrete Math., 20 (2006), no. 1, 137–142.
- [2] B. Bollob´s, Modern graph theory, Graduate Texts in Mathematics, vol. 184, Springer, New York, 1998.
- [3] B. Bollob´s and A. Scott, A proof of a conjecture of Bondy concerning paths in weighted digraphs, J. Combin. Theory Ser. B, 66 (1996), no. 2, 283–292.
- [4] L. Caccetta and R. H¨aggkvist, On minimal digraphs with given girth, in Proc. 9th Southeastern Conference on Combinatorics, Graph Theory, and Computing (Boca Raton 1978), Congress. Numer. XXI 181–187.
- [5] P. Charbit, S. Thomasse´ and A. Yeo, The minimum feedback arc set problem is NP-hard for tournaments, Combin. Probab. Comput., 16 (2007), 1–4.
- [6] M. Chudnovsky, P. Seymour and B. Sullivan, Cycles in dense digraphs, Combinatorica, 28

(2008) 1–18.

- [7] J. Fox, P. Keevash and B. Sudakov, Directed graphs without short cycles, Combin. Probab. Comput., 19 (2010), 285–301.
- [8] C. Leiserson and J. Saxe, Retiming synchronous circuitry, Algorithmica 6 (1991), 5–35.
- [9] M. Nathanson, The Caccetta-H¨aggkvist conjecture and additive number theory, AIM Preprint 2006-10: www.aimath.org/preprints.html.
- [10] A. Shaw, The logical design of operating systems, Prentice-Hall, Englewood Cliﬀs, NJ, 1974.
- [11] B. Sullivan, Extremal problems in digraphs, PhD thesis, Princeton University, 2008.
- [12] B. Sullivan, A summary of results and problems related to the Caccetta-H¨aggkvist conjecture, available online at http://arxiv.org/abs/math/0605646v1.


