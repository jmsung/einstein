---
type: source
kind: paper
title: A survey of hypergraph Ramsey problems
authors: Dhruv Mubayi, Andrew Suk
year: 2017
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/1707.04229v3
source_local: ../raw/2017-mubayi-survey-hypergraph-ramsey-problems.pdf
topic: general-knowledge
cites:
---

arXiv:1707.04229v3[math.CO]6May2018

A survey of hypergraph Ramsey problems

Dhruv Mubayi∗ Andrew Suk†

Abstract

The classical hypergraph Ramsey number rk(s,n) is the minimum N such that for every redblue coloring of the k-tuples of {1,...,N}, there are s integers such that every k-tuple among them is red, or n integers such that every k-tuple among them is blue. We survey a variety of problems and results in hypergraph Ramsey theory that have grown out of understanding the quantitative aspects of rk(s,n). Our focus is on recent developments and open problems.

# 1 Introduction

A k-uniform hypergraph H (k-graph for short) with vertex set V is a collection of k-element subsets of V . We write Kn(k) for the complete k-graph on an n-element vertex set. The Ramsey number rk(s,n) is the minimum N such that every red-blue coloring of the edges of KN(k) contains a monochromatic red copy of Ks(k) or a monochromatic blue copy of Kn(k). The existence of rk(s,n) follows from the celebrated theorem of Frank Ramsey from 1930 [87]. However, the asymptotic behavior of rk(s,n) is still not well understood.

In this survey we focus on open problems and results related to generalizations and extensions of rk(s,n) in the hypergraph case, i.e., when k ≥ 3 (we refer the reader to [26] for a survey of Graph Ramsey theory). Our emphasis is on recent results and although we believe we have touched on most important developments in this area, this survey is not an exhaustive compendium of all work in hypergraph Ramsey theory.

# 2 General notation

The full statement of Ramsey’s theorem extends to multiple colors and to general hypergraphs as follows. Given an integer q ≥ 2 and k-uniform hyergraphs H1,... ,Hq, there is a minimum rk(H1,... ,Hq) = N, such that every q-coloring of the edges of KN(k) contains a copy of Hi in the ith color. In the special case that H = H1 = ··· = Hq, we simply write

![image 1](<2017-mubayi-survey-hypergraph-ramsey-problems_images/imageFile1.png>)

∗Department of Mathematics, Statistics, and Computer Science, University of Illinois, Chicago, IL, 60607 USA. Research partially supported by NSF grant DMS-1300138. Email: mubayi@uic.edu

†Department of Mathematics, University of California at San Diego, La Jolla, CA, 92093 USA. Supported by NSF grant DMS-1800736, an NSF CAREER award, and an Alfred Sloan Fellowship. Email: asuk@ucsd.edu.

).

rk(H;q) = rk(H,... ,H

![image 2](<2017-mubayi-survey-hypergraph-ramsey-problems_images/imageFile2.png>)

![image 3](<2017-mubayi-survey-hypergraph-ramsey-problems_images/imageFile3.png>)

q times

If Hi = Kn(ki), we use the simpler notation rk(n1,... ,nq) and rk(n;q) = rk(n,... ,n

).

![image 4](<2017-mubayi-survey-hypergraph-ramsey-problems_images/imageFile4.png>)

![image 5](<2017-mubayi-survey-hypergraph-ramsey-problems_images/imageFile5.png>)

q times

# 3 Diagonal Ramsey numbers

Diagonal Ramsey numbers refer to the special case when s = n, i.e. rk(n,n), and have been studied extensively over the past 80 years. Classic results of Erd˝os and Szekeres [48] and Erd˝os [38] imply that 2n/2 < r2(n,n) ≤ 22n for every integer n > 2. While small improvements have been made in both the upper and lower bounds for r2(n,n) (see [90, 14]), the constant factors in the exponents have not changed over the last 70 years.

Unfortunately for 3-graphs, our understanding of r3(n,n) is much less than in the graph case. A result of Erd˝os, Hajnal, and Rado [45] gives the best known lower and upper bounds for r3(n,n),

2c1n2 < r3(n,n) < 22c2n, where c1 and c2 are absolute constants. Another proof of the lower bound above was given by Conlon, Fox, and Sudakov in [21], which will be discussed in more detail in Section 4. For k ≥ 4, there is also a diﬀerence of one exponential between the known lower and upper bounds for rk(n,n), that is,

twrk−1(c1n2) ≤ rk(n,n) ≤ twrk(c2n), (1)

where the tower function twrk(x) is deﬁned by twr1(x) = x and twri+1(x) = 2twri(x) (see [48, 46, 44]). A notoriously diﬃcult conjecture of Erd˝os, Hajnal, and Rado states that the upper bound in (1) is essentially the truth, that is, there are constructions which demonstrate that rk(n,n) > twrk(cn), where c = c(k). The crucial case is when k = 3, since a double exponential lower bound for r3(n,n) would verify the conjecture for all k ≥ 4 by using the well-known steppingup lemma of Erd˝os and Hajnal (see [53]).

- Conjecture 3.1 (Erd˝os). For n ≥ 4 we have r3(n,n) > 22cn, where c is an absolute constant.


It is worth mentioning that Erd˝os oﬀered a $500 reward for a proof of this conjecture (see [11]), and his conjecture is supported by the fact that a double exponential lower bound is known if one allows four colors. More precisely, Erd˝os and Hajnal (see [53]) showed that r3(n;4) > 22cn, and for three colors, the best known lower bound for r3(n;3) is due to Conlon, Fox, and Sudakov [21] who showed that r3(n;3) > 2nclogn. There is some evidence that perhaps Conjecture 3.1 is false, and we refer the interested reader to [20, 18] for two results in this direction.

# 4 Oﬀ-Diagonal Ramsey numbers

Oﬀ-diagonal Ramsey numbers, rk(s,n), refer to the special case when k,s are ﬁxed and n tends to inﬁnity. It is known [2, 57, 5, 7] that r2(3,n) = Θ(n2/log n), and more generally for ﬁxed

s > 3, r2(s,n) = nΘ(1). For 3-graphs, Conlon, Fox and Sudakov [21] proved that there are absolute constants c,c′ > 0 such that for all 4 ≤ s ≤ n,

2csnlog(ns+1) < r3(s,n) < 2(c′n/s)s−2 log(n/s). For s = n, this gives another proof that r3(n,n) > 2cn2. For k-graphs, where s > k ≥ 4, it is known that rk(s,n) ≤ twrk−1(nc), where c = c(s) [46]. Erd˝os and Hajnal proved that

![image 6](<2017-mubayi-survey-hypergraph-ramsey-problems_images/imageFile6.png>)

rk(s,n) > twrk−1(c′n), (2)

for k ≥ 4 and s ≥ 2k−1 − k + 3, where c′ = c′(s). They conjectured that a similar bound should hold for smaller s as follows.

- Conjecture 4.1 (Erd˝os-Hajnal [44]). Fix 4 ≤ k < s. There are constants c and c′ such that twrk−1(cn) < rk(s,n) < twrk−1(c′n).


Actually, this was part of a more general conjecture that they posed in that paper which will be discussed in Section 4. Erd˝os and Hajnal (see [53]) showed that r4(7,n) > 22cn, and the authors [81] and Conlon, Fox, and Sudakov [23] independently veriﬁed the conjecture for k ≥ 4 and s ≥ k +3 (using diﬀerent constructions). However, showing that r4(5,n) and r4(6,n) grows double exponentially in a power of n seemed to be much more diﬃcult.

Just as for diagonal Ramsey numbers, a double exponential in nc lower bound for r4(5,n) and r4(6,n) would imply rk(k + 1,n) > twrk−1(nc′) and rk(k + 2,n) > twrk−1(nc′) respectively, for all ﬁxed k ≥ 5, by a variant of the Erd˝os-Hajnal stepping up lemma. In [79], the authors established the following lower bounds for r4(5,n) and r4(6,n), which represents the current best bounds: for all n ≥ 6,

1/5

r4(5,n) > 2nclogn and r4(6,n) > 22cn

,

where c > 0 is an absolute constant. More generally, for n > k ≥ 5, there is a c = c(k) > 0 such that

rk(k + 1,n) > twrk−2(nclogn) and rk(k + 2,n) > twrk−1(cn1/5). A standard argument in Ramsey theory together with results in [21] for 3-graphs yields

rk(k + 2,n) < twrk−1(c′n3 log n),

so we now know the tower growth rate of rk(k + 2,n). It remains an open problem to prove that r4(5,n) is double exponential in a power of n.

c

- Conjecture 4.2. For n ≥ 5, there is an absolute constant c > 0 such that r4(5,n) > 22n


.

In [81], the authors established a connection between diagonal and oﬀ-diagonal Ramsey numbers, by showing that a solution to Conjecture 3.1 implies a solution to Conjecture 4.2 (see Section 10 for more details).

# 5 The Erd˝os-Hajnal Problem

As mentioned in previous sections, it is a major open problem to determine if r3(n,n) and r4(5,n) grow double exponentially in a power of n. In order to shed more light on these questions, Erd˝os and Hajnal [44] in 1972 considered the following more general parameter.

- Deﬁnition 5.1. For integers 2 ≤ k < s < n and 2 ≤ t ≤ k s , let rk(s,t;n) be the minimum N such


that every red/blue coloring of the edges of KN(k) results in a monochromatic blue copy of Kn(k) or has a set of s vertices which contains at least t red edges.

The function rk(s,t;n) encompasses several fundamental problems which have been studied for a while. Clearly rk(s,n) = rk(s, k s ;n) so rk(s,t;n) includes classical Ramsey numbers. In addition to oﬀ-diagonal and diagonal Ramsey numbers already mentioned, the function rk(k+1,k+1;k+1) has been studied in the context of the Erd˝os-Szekeres theorem and Ramsey numbers of ordered tight-paths by several researchers [35, 37, 52, 71, 70], the more general function rk(k + 1,k + 1;n) is related to high dimensional tournaments [66], and even the very special case r3(4,3;n) has tight connections to quasirandom hypergraph constructions [4, 58, 64, 65].

The main conjecture of Erd˝os and Hajnal [44] for rk(s,t;n) is that, as t grows from 1 to k s , there is a well-deﬁned value t1 = h(1k)(s) at which rk(s,t1 − 1;n) is polynomial in n while rk(s,t1;n) is exponential in a power of n, another well-deﬁned value t2 = h(2k)(s) at which it changes from exponential to double exponential in a power of n and so on, and ﬁnally a well-deﬁned value tk−2 = h(kk−)2(s) < k s at which it changes from twrk−2 to twrk−1 in a power of n. They were not able to oﬀer a conjecture as to what h(ik)(s) is in general, except when i = 1 and when s = k + 1.

- • When i = 1, they conjectured that t1 = h(1k)(s) is one more than the number of edges in the k-graph obtained by taking a complete k-partite k-graph on s vertices with almost equal part sizes, and repeating this construction recursively within each part. Erd˝os oﬀered $500 for a proof of this (see [11]).
- • When s = k +1, they conjectured that h(ik)(k +1) = i+2, that is, rk(k +1,2;n) is polynomial in n, rk(k + 1,3;n) is exponential in a power of n, rk(k + 1,4;n) is double exponential in a power of n, and etc. such that at the end, both rk(k + 1,k;n) and rk(k + 1,k + 1;n) are twrk−1 in a power of n. They proved this for i = 1 via the following: Theorem 5.2 (Erdos-Hajnal [44]). For k ≥ 3, there are positive c = c(k) and c′ = c′(k) such that


rk(k + 1,2;n) < cnk−1 and rk(k + 1,3;n) > 2c′n.

Results of Ro¨dl-Sinajov´aˇ [88] on partial Steiner systems, and of Kostochka-Mubayi-Verstrae¨te [62] on independent sets in hypergraphs, determine the order of magnitude of the function rk(k+1,2;n) as follows. For each k ≥ 3 there exist positive c = ck and c′ = c′(k) such that

c′nk−1/log n < rk(k + 1,2;n) < cnk−1/log n.

For the t = 3 case, the authors in [82] showed that for k ≥ 3, there are positive c = c(k) and c′ = c′(k) such that

2cnk−2 ≤ rk(k + 1,3;n) ≤ 2c′nk−2 logn. (3) For general t, the methods of Erd˝os and Rado [46] show that there exists c = c(k,t) > 0 such that rk(k + 1,t;n) ≤ twrt−1(nc), (4)

for 3 ≤ t ≤ k. Erd˝os and Hajnal conjectured that this upper bound is the correct tower growth rate for rk(k + 1,t;n).

- Conjecture 5.3 (Erdos-Hajnal [44]). For k ≥ 3 and 2 ≤ t ≤ k, there exists c = c(k,t) > 0 such that


rk(k + 1,t;n) ≥ twrt−1(cn).

Note that when t = k + 1, the results from the previous section states that rk(k + 1,k + 1;n) = rk(k + 1,n) ≤ twrk−1(nc′) where c′ = c′(k,t).

Hence for 3-graphs, r3(4,t;n) is fairly well understood. We know that r3(4,2;n) is polynomial in n, and both r3(4,3;n) and r3(4,4;n) are exponential in n1+o(1). See [21] for more results on h(3)1 (s) for s > 4. Unfortunately for 4-graphs, we do not have a good understanding of r4(5,t;n) when 4 ≤ t ≤ 5. The best known upper and lower bounds for r4(5,4;n) are obtained by (3) and (4), which give 2cn2 < r4(5,4;n) < 22n

c

. Notice that Conjecture 5.3 states that r4(5,4;n) grows double exponential in a power of n, but we don’t even know if r4(5,5;n) = r4(5,n) is double exponential in a power of n. Likewise, for 5-graphs, not much is known about r5(6,4;n) and r5(6,5;n). Combining (3) and (4) gives

nc

c

and 2c′n3 < r5(6,5;n) < 222

2c′n3 < r5(6,4;n) < 22n

. (5) Problem 5.4. Determine the tower growth rate of r4(5,4;n), r5(6,4;n), and r5(6,5;n).

However for k-graphs, when k ≥ 6, the authors in [82] settled Conjecture 5.3 in almost all cases in a strong form, by determining the correct tower growth rate, and in half of the cases also determining the correct power of n within the tower.

Theorem 5.5 (Mubayi-Suk [82]). For k ≥ 6 and 4 ≤ t ≤ k − 2, there are positive c = c(k,t) and c′ = c′(k,t) such that

twrt−1(c′nk−t+1 log n) ≥ rk(k + 1,t; n) ≥

twrt−1(cnk−t+1) if k − t is even twrt−1(cn(k−t+1)/2) if k − t is odd.

When k ≥ 6 and t ∈ {k − 1,k}, Conjecture 5.3 remains open. We note that the upper bound in Theorem 5.5 also holds when k − 1 ≤ t ≤ k. The best known upper and lower bounds for rk(k + 1,k − 1;n) and rk(k + 1,k;n), also due to the authors [82], are

twrk−3(cn3) ≤ rk(k + 1,k − 1; n) ≤ twrk−2(c′ n2),

and

twrk−3(cn3) ≤ rk(k + 1,k; n) ≤ twrk−1(c′ n).

In fact, by using the stepping-up lemma established in [82], any improvement in the lower bound for r5(6,4;n) and r5(6,5;n) in (5) would imply a better lower bound for rk(k + 1,k − 1; n) and rk(k + 1,k; n) respectively.

# 6 The Erd˝os-Rogers Problem

An s-independent set in a k-graph H is a vertex subset that contains no copy of Ks(k). So if s = k, then it is just an independent set. Let αs(H) denote the size of the largest s-independent set in H.

- Deﬁnition 6.1. For k ≤ s < t < N, the Erd˝os-Rogers function fs,tk (N) is the minimum of αs(H) taken over all Kt(k)-free k-graphs H of order N.


To prove the lower bound fs,tk (N) ≥ n, one must show that every Kt(k)-free k-graph on N vertices contains an s-independent set with n vertices. On the other hand, to prove the upper bound

fs,t(k)(N) < n, one must construct a Kt(k)-free k-graph H of order N with αs(H) < n. The problem of determining fs,tk (n) extends that of ﬁnding Ramsey numbers. Formally,

rk(s,n) = min{N : fk,sk (N) ≥ n}.

For k = 2, the above function was ﬁrst considered by Erd˝os and Rogers [47] only for t = s+1, which is perhaps the most interesting case. So in this case we wish to construct a Ks+1-free graph on N vertices such that the s-independence number is as small as possible. Since then the function has been studied by several researchers culminating in the work of Wolfowitz [93] and Dudek, Retter and Ro¨dl [34] who proved the upper bound that follows (the lower bound is due to Dudek and the ﬁrst author [33]): for every s ≥ 3 there are positive constants c1 and c2 = c2(s) such that

1/2

N log N log log N

< fs,s2 +1(N) < c2(log N)4s2N1/2. (6)

c1

![image 7](<2017-mubayi-survey-hypergraph-ramsey-problems_images/imageFile7.png>)

The problem of estimating the Erd˝os-Rogers function for k > 2 appears to be much harder. Let us denote

g(k,N) = fkk+1,k+2(N).

In other words, g(k,N) is the minimum n such that every Kk(k+2) -free k-graph on N vertices has the property that every n-set of vertices has a copy of Kk(k+1) . With this notation, the bounds in (6) for s = 3 imply that g(2,N) = N1/2+o(1).

Dudek and the ﬁrst author [33] proved that (log N)1/4+o(1) < g(3,N) < O(log N), and more generally, that there are positive c1 = c1(k) and c2 = c2(k) with

c1(log(k−2) N)1/4 < g(k,N) < c2(log N)1/(k−2), (7)

where log(i) is the log function iterated i times. The exponent 1/4 in (7) was improved to 1/3 by Conlon, Fox and Sudakov [25]. Both sets of authors asked whether the upper bound could be improved (presumably to an iterated log function). This was achieved by the current authors [80] who proved that for k ≥ 14,

g(k,N) = O(log(k−13) N). It remains an open problem to determine the correct number of iterations (which may well be k−2). We pose this as a conjecture.

- Conjecture 6.2. For all k ≥ 3, there are c1,c2 > 0 such that c1 log(k−2) N < g(k,N) < c2 log(k−2) N.


# 7 The Erd˝os-Gy´arf´as-Shelah Problem

A (p,q)-coloring of KN(k) is an edge-coloring of KN(k) that gives every copy of Kp(k) at least q colors. Let fk(N,p,q) be the minimum number of colors in a (p,q)-coloring of KNk .

The problem of determining fk(N,p,q) for ﬁxed k,p,q has a long history, beginning with its introduction by Erd˝os and Shelah [39, 41], and subsequent investigation (for graphs) by Erd˝os and Gy´arf´as [43]. Since

fk(N,p,2) = t ⇐⇒ rk(p;t) ≥ N + 1 and rk(p;t − 1) ≤ N,

most of the eﬀort on determining fk(N,p,q) has been for q > 2. As mentioned above, Erd˝os and Gy´arf´as [43] initiated a systematic study of this parameter for graphs and posed many open problems. One main question was to determine the minimum q such that f2(N,p,q) = No(1) and f2(N,p,q+1) > Ncp for some cp > 0. For p = 3 this value is clearly q = 2 as f2(N,3,2) = O(log N) due to the easy bound r2(3;t) > 2t, while f2(N,3,3) = χ′(KN) ≥ N −1. Erd˝os and Gy´arf´as proved

- that f2(N,p,p) > Ncp and asked whether f2(N,p,p−1) = No(1). The ﬁrst open case was f2(N,4,3), which was shown to be No(1) by the ﬁrst author [73] and later Ω(log N) (see [51, 60]). The same upper bound was shown for f(N,5,4) in [36]. Conlon, Fox, Lee and Sudakov [17] recently extended this construction considerably by proving that f2(N,p,p − 1) = No(1) for all ﬁxed p ≥ 4. Their result is sharp in the sense that f2(N,p,p) = Ω(N1/(p−2)). The exponent 1/(p − 2) was shown to be sharp for p = 4 by the ﬁrst author [74] and recently also for p = 5 by Cameron and Heath [10] via explicit constructions.


The ﬁrst nontrivial hypergraph case is f3(N,4,3) and this function has tight connections to Shelah’s breakthrough proof [89] of primitive recursive bounds for the Hales-Jewett numbers. Answering a question of Graham, Rothschild and Spencer [53], Conlon, Fox, Lee and Sudakov showed that

f3(N,4,3) = No(1).

They also posed a variety of basic questions about fk(N,p,q) and related parameters including the following generalization of the Erd˝os-Gy´rf´as problem for hypergraphs. Using a variant of the pigeonhole argument for hypergraph Ramsey numbers due to Erd˝os and Rado, [16] proved that

fk N,p,

p − i k − i

+ 1 = Ω(log(i−1) Ncp,k,i)

where log(0)(x) = x and, as usual, log(i+1) x = log log(i) x for i ≥ 0.

- Problem 7.1 (Conlon-Fox-Lee-Sudakov [16]). For p > k ≥ 3 and 0 < i < k prove that fk(N,p, k p−−ii )

is substantially smaller than fk(N,p, k p−−ii + 1), in particular, prove that fk(N,p, k p−−ii ) is much smaller than log(i−1) N.

One natural way to interpret this problem is that it asks whether

fk N,p,

p − i k − i

= (log(i−1) N)o(1)?

The case k = 2 is precisely the Erd˝os-Gy´rf´as problem and the case k = 3,p = 4,i = 1 is to prove that f3(N,4,3) = No(1) which was established in [16]. The next open case is k = 3,p = 5,i = 2, which asks whether f3(N,5,3) = (log N)o(1). This was solved with a better bound by the ﬁrst author [75], who showed that

f3(N,5,3) = eO(

√log logN) = (log N)O(1/

![image 8](<2017-mubayi-survey-hypergraph-ramsey-problems_images/imageFile8.png>)

√log logN).

![image 9](<2017-mubayi-survey-hypergraph-ramsey-problems_images/imageFile9.png>)

No other nontrivial cases of Problem 7.1 have been solved. We refer the reader to [16] for related problems and results.

8 More oﬀ-diagonal problems

In this section we consider k-graph Ramsey numbers of the form rk(H,n) := rk(H,Kn(k)) where H is a (ﬁxed) k-graph and n grows.

- 8.1 K4(3) minus an edge and a generalization


Let K4(3) \ e denote the 3-graph on four vertices, obtained by removing one edge from K4(3). A simple argument of Erd˝os and Hajnal [44] implies r(K4(3) \ e,Kn(3)) < (n!)2. This was generalized in [80] as follows. A k-half-graph, denote by B = B(k), is a k-graph on 2k −2 vertices, whose vertex set is of the form S ∪ T, where |S| = |T| = k − 1, and whose edges are all k-subsets that contain S, and one k-subset that contains T. So B(3) = K4(3) \ e. Write rk(B,n) = r(B(k),Kn(k)). It was shown in [80] that for each k ≥ 4 there exists c = ck such that

2cn < rk(B,n) < (n!)k−1.

A problem that goes back to the 1972 paper of Erd˝os and Hajnal (for k = 3) is to improve the lower bound above. Indeed, r3(B,n) = r3(4,3;n) and this is therefore a very special case of the Erd˝os-Hajnal problem discussed earlier.

- Problem 8.1. Show that for each k ≥ 3 there exists c = ck such that rk(B,n) > 2cnlogn.


## 8.2 Independent neighborhoods

Deﬁnition 8.2. A k-uniform triangle T(k) is a set of k + 1 edges b1,... ,bk,a with bi ∩ bj = R for all i < j where |R| = k − 1 and a = ∪i(bi − R). In other words, k of the edges share a common (k − 1)-set of vertices, and the last edge contains the remaining point in all these previous edges.

When k = 2, then T(2) = K3, so in this sense T(k) is a generalization of a graph triangle. We may view a T(k)-free k-graph as one in which all neighborhoods are independent sets, where the

neighborhood of an R ∈ Vk(−H1) is {x : R ∪ {x} ∈ H}. As usual, write rk(T,n) for r(T(k),Kn(k)). Bohman, Frieze and Mubayi [6] proved that for ﬁxed k ≥ 2, there are positive constants c1 and c2 with

nk (log n)k/(k−1)

< rk(T,n) < c2nk.

c1

![image 10](<2017-mubayi-survey-hypergraph-ramsey-problems_images/imageFile10.png>)

They conjectured that the upper bound could be improved to o(nk) and believed that the log factor in the lower bound could also be improved. Results of Kostochka-Mubayi-Verstrae¨te [62] proved this and then Bohman-Mubayi-Picollelli [9] achieved a matching lower bound by analyzing the hypergraph independent neighborhood process. This may be viewed as a hypergraph generalization of the results of Ajtai-Koml´os-Szemere´di [2] for graphs.

- Theorem 8.3 (Kostochka-Mubayi-Verstrae¨te [62], Bohman-Mubayi-Picollelli [9]). For ﬁxed k ≥ 3 there are positive constants c1 and c2 with


nk log n

nk log n

< rk(T,n) < c2

.

c1

![image 11](<2017-mubayi-survey-hypergraph-ramsey-problems_images/imageFile11.png>)

![image 12](<2017-mubayi-survey-hypergraph-ramsey-problems_images/imageFile12.png>)

- 8.2.1 Unordered tight-paths versus cliques


An (unordered) 3-uniform tight-path TPs(3) = TPs is the 3-graph with vertex set {v1,... ,vs} and edge set {{vi,vi+1,vi+2} : i ∈ {1,... ,s − 2}}. Note that the vertex set {v1,... ,vs} is not ordered. Results of Phelps and Ro¨dl [84] imply that there are c1 and c2 such that

c1n2/log n < r3(TP4,n) < c2n2/log n.

It is easy to prove that for all s ≥ 5, there is c = cs such that r3(TPs,n) < cn2. A matching lower bound for s ≥ 6 was provided by Cooper and Mubayi [30] with the following construction. Let H be a 3-graph where V (H) = [n] × [n], and E(H) = {{ab,ac,db} ∈ [n] × [n] : c > b,d > a}. It is easy to see that H is TP6-free and α(H) < 2n. Thus, For s ≥ 6 there exists c = cs such that r3(TPs,n) > cn2. The construction above has many copies of TP5 so this leaves open the case s = 5. Using the trivial lower bound r3(TP4,n) we thus have c1n2/log n < r3(TP5,n) < c2n2.

Problem 8.4 ([30]). Determine the order of magnitude of r3(TP5,n).

The corresponding problems for k-graphs when k > 3 are wide open.

## 8.3 Cycles versus cliques

For ﬁxed s ≥ 3 the graph Ramsey number r(Cs,n) = r(Cs,Kn) has been extensively studied. The case s = 3 is one of the oldest questions in Ramsey theory and it is known that r(C3,Kn) = Θ(n2/log n) (see [2, 57] and [8, 50] for recent improvements). The next case r(C4,Kn) seems substantially more diﬃcult. An old open problem of Erd˝os [42] asks whether there is a positive ǫ for which r(C4,Kn) = O(n2−ǫ). The current best upper bound r(C4,Kn) = O(n2/log2 n) is an unpublished result of Szemere´di which was reproved in [86] and the current best lower bound is Ω(n3/2/log n) from [7]. For longer cycles, the best known bounds can be found in [7, 91], and the order of magnitude of r(Cs,Kn) is not known for any ﬁxed s ≥ 4.

There are several natural ways to deﬁne a cycle in hypergraphs. The two that have been investigated the most are tight cycles and loose cycles.

- 8.3.1 Loose cycles versus cliques


For s ≥ 3, the loose cycle LCs(k) is the k-graph with vertex set Z(k−1)s and edge set {e1,e2,... ,es} where ei = {i(k − 1) − k + 2,... ,i(k − 1) + 1}. In other words, consecutive edges intersect in exactly one vertex and nonconsecutive edges are pairwise disjoint. As usual, write rk(LCs,n) for r(LCs(k),Kn(k)). Since loose cycles are k-partite, it is easy to see that rk(LCs,n) has polynomial growth rate for ﬁxed k,s so the question here is to determine the correct power of n.

- Theorem 8.5 (Kostochka-Mubayi-Verstrae¨te [61]). There exists c1,c2 > 0 such that for all n ≥ 1,


c1n3/2

(log n)3/4 ≤ r3(LC3,n) ≤ c2n3/2. For k ≥ 3, we also have rk(LC3,n) = n3/2+o(1).

![image 13](<2017-mubayi-survey-hypergraph-ramsey-problems_images/imageFile13.png>)

Analogous to the basic result r(3,n) = O(n2/log n) due to Ajtai, Komlo´s and Szemere´di [2], the authors conjectured something similar for hypergraphs.

- Conjecture 8.6 ([61]). For all ﬁxed k ≥ 3, we have rk(LC3,n) = o(n3/2).


Deﬁne the 3-graph F = {abc,abd,cde}. Cooper and Mubayi [29] proved the following weaker version of Conjecture 8.6 in the case k = 3:

r3({LC3,F,K4(3) − e},n) = O

n3/2 (log n)1/2

![image 14](<2017-mubayi-survey-hypergraph-ramsey-problems_images/imageFile14.png>)

. (8)

Notice that the three forbidden 3-graphs in (8) are all types of triangles, comprising three edges that cyclically share a vertex. Conjecture 8.6 asks that we forbid only one of these three triangles, the loose triangle.

For longer cycles, the following general lower bounds were proved in [61] which improve the bounds given by the standard probabilistic deletion method:

rk(LCs,n) > n1+1/(3s−1)+o(1). Furthermore, there exists c = ck such that

rk(LC5,n) > c

n log n

![image 15](<2017-mubayi-survey-hypergraph-ramsey-problems_images/imageFile15.png>)

5/4

.

- Conjecture 8.7 ([61]). For each k ≥ 3, there exists c = ck such that rk(LC5,n) < cn5/4.


Me´roueh [69] recently proved that r3(LC5,n) < cn4/3 and more generally that

1

r3(LCs,n) < csn1+

⌊(s+1)/2⌋.

![image 16](<2017-mubayi-survey-hypergraph-ramsey-problems_images/imageFile16.png>)

He also proved that for odd s ≥ 5 and k ≥ 4, rk(LCs,n) < ck,sn1+1/⌊s/2⌋ which slightly improved the exponent 1 +1/(⌊s/2⌋ −1) proved by Collier-Cartaino, Graber and Jiang [13] for all k ≥ 3 and s ≥ 4.

8.3.2 Tight cycles versus cliques

For k ≥ 2 and s > 3, the tight cycle TCs(k) is the k-graph with vertex set Zs (integers modulo s) and edge set

{{i,i + 1,... ,i + k − 1} : i ∈ Zs}.

We can view the vertex set of TCs(k) as s points on a circle and the edge set as the s subintervals each containing k consecutive vertices.

When s ≡ 0 (mod 3) the tight cycle TCs(3) is 3-partite, and in this case it is trivial to observe that r3(TCs,n) := r(TCs(3),Kn(3)) grows polynomially in n. The growth rate of this polynomial is not known for any s > 3. When s  ≡ 0 (mod 3) the Ramsey number is exponential in n.

- Theorem 8.8 (Mubayi-R¨dl [78, 77]). Fix s ≥ 5 and s  ≡ 0 (mod 3). There are positive constants c1 and c2 such that


2c1n < r3(TCs,n) < 2c2n2 logn.

If s  ≡ 0 (mod 3) and s ≥ 16 or s ∈ {8,11,14}, there is a positive constant cs such that r3(TCs,n) < 2csnlogn.

Note that when s = 4, the cycle TC4(3) is K4(3) and in this case the lower bound was proved much earlier by Erd˝os and Hajnal [44], and in fact has been improved to 2c1nlogn more recently by Conlon, Fox and Sudakov [21].

- Problem 8.9. Prove similar bounds for s ∈ {4,5,7,10,13} and determine whether the log factor in the exponent is necessary.


The problem of determining rk(TCs,n) := rk(TCs(k),Kt(k)) for ﬁxed s > k > 3 seems harder as k grows. It was shown in [78] that we have a lower bound

rk(TCs,n) > 2ck,snk−2

The best upper bound that is known (for ﬁxed s > k and all n) is the trivial one rk(s,n). Consequently, we have

2ck,snk−2 < rk(TCs,n) < rk(s,n) < twrk−1(nds,k).

Closing the gap above seems to be a very interesting open problem. For the case s = k + 1, one has a substantially better lower bound as

rk(TCk+1,n) = rk(k + 1,n) > twrk−2(bnlogn) where b = bk.

- Problem 8.10. For ﬁxed s > k+1 > 4 (in particular for s = k+2), determine whether rk(TCs,n) is at least a tower function in a power of n where the tower height grows with k.


# 9 Bounded degree hypergraphs

Given a bounded degree graph G, the Ramsey number r2(G,G) has been studied extensively. A famous result due to Chv´atal, Ro¨dl, Szemere´di, and Trotter [12] says that if G is a graph on n vertices with maximum degree ∆, then r2(G,G) ≤ c∆n where c∆ depends only on ∆. This was later extended to 3-graphs by Cooly, Fountoulakis, Ku¨hn, Osthus [27], Nagle, Olsen, Ro¨dl, Schacht [83], and Ishigami [63] independently, where the degree of a vertex v in a hypergraph H is the number of edges which contain v. Using diﬀerent methods, Cooly, Fountoulakis, Ku¨hn, Osthus [28] and Conlon, Fox, Sudakov [24] extended this to general k-graphs.

- Theorem 9.1 (Cooly et al. [28], Conlon-Fox-Sudakov [24]). For all ∆,k ≥ 1, there is a c(∆,k) such that for any k-graph H on n vertices with maximum degree ∆, we have


rk(H,H) ≤ c(∆,k)n.

In the special case that H = LCn(3) or TCn(3), the asymptotics for both r3(LCn,LCn) and r3(TCn,TCn) were determined in [55] and [56] respectively.

- Theorem 9.2 (Haxell et al. [55]). r3(LCn,LCn) = 52n(1 + o(1)).


![image 17](<2017-mubayi-survey-hypergraph-ramsey-problems_images/imageFile17.png>)

- Theorem 9.3 (Haxell et al. [56]). For n divisible by 3, we have r3(TCn,TCn) = 43n(1 + o(1)). Otherwise, if n is not divisible by 3, we have r3(TCn,TCn) = 2n(1 + o(1)).


![image 18](<2017-mubayi-survey-hypergraph-ramsey-problems_images/imageFile18.png>)

For q-colors, Gy´arf´as and Raeisi [54] proved that q + 5 ≤ r3(LC3;q) ≤ 3q + 1.

It seems to be an interesting open problem to determine which bound above is closer to the truth. The lower bound appears more likely to be the answer. There has been some work on determining

r3(P;q) where P = {123,345,567} is the 3-uniform loose path of length three. In particular, the lower bound r3(P;q) ≥ q + 6 for all q ≥ 3 is sharp for all q ≤ 9 (see [54, 85]). The general upper bound which comes from the Tura´n number of P is again 3q + 1. This upper bound was improved by Luczak and Polcyn [67] ﬁrst to (2+o(1))q and more recently to λq +O(√q) where the constant λ = 1.97466.. is the solution to a particular cubic equation.

![image 19](<2017-mubayi-survey-hypergraph-ramsey-problems_images/imageFile19.png>)

# 10 Ordered Hypergraph Ramsey Problems

In this section, we discuss several Ramsey-type results for ordered hypergraphs. An ordered Nvertex k-graph H is a hypergraph whose vertex set is [N] = {1,... ,N}. Given two ordered k-graphs G and H with vertex set [n] and [N] respectively, we say that H contains G if there is a function φ : [n] → [N] such that φ(i) < φ(j) for all 1 ≤ i < j ≤ n, and (v1,... ,vk) ∈ E(G) implies that (φ(v1),... ,φ(vk)) ∈ E(H). Given q ordered k-graphs H1,... ,Hq, the ordered Ramsey number rk(H1,... ,Hn) is the minimum integer N, such that every q-coloring of the edges of the complete k-graph with vertex set [N], contains a copy of Hi in the ith color.

![image 20](<2017-mubayi-survey-hypergraph-ramsey-problems_images/imageFile20.png>)

## 10.1 Tight-paths and cliques in hypergraphs

An ordered tight path Ps(k) is an ordered k-graph with vertex set [s], whose edges are of the form (i,i + 1,... ,i + k − 1), for 1 ≤ i ≤ s − k + 1. The length of an ordered tight path Ps(k) is the number of edges it contains, that is, s − k + 1. In order to avoid the excessive use of superscripts, we write Ps = Ps(k) when the uniformity is already implied. Two famous theorems of Erd˝os and Szekeres in [48], known as the monotone subsequence theorem and the cups-caps theorem, imply

- that r2(Ps,Pn) = (n− 1)(s − 1) +1 and r3(Ps,Pn) = n+s−s−24 +1. In [52], Fox, Pach, Sudakov, and Suk extended their results to k-graphs and determined the correct tower growth rate for rk(Ps,Ps). Their results gave a geometric application related to the Happy Ending Theorem.1 A few years later, Moshkovitz and Shapira [71] sharpened the bounds for rk(Ps,Ps) by determining an exact formula for r3(Ps,... ,Ps) = r3(Ps;q) with q colors.


![image 21](<2017-mubayi-survey-hypergraph-ramsey-problems_images/imageFile21.png>)

![image 22](<2017-mubayi-survey-hypergraph-ramsey-problems_images/imageFile22.png>)

![image 23](<2017-mubayi-survey-hypergraph-ramsey-problems_images/imageFile23.png>)

![image 24](<2017-mubayi-survey-hypergraph-ramsey-problems_images/imageFile24.png>)

![image 25](<2017-mubayi-survey-hypergraph-ramsey-problems_images/imageFile25.png>)

![image 26](<2017-mubayi-survey-hypergraph-ramsey-problems_images/imageFile26.png>)

- Theorem 10.1 (Moshkovitz-Shapira [71]). Let Pq−1(s) denote the number of s × ··· × s (q − 1)dimensional partitions with entries {0,1,... ,s}. Then


r3(Ps;q) = Pq−1(s) + 1.

![image 27](<2017-mubayi-survey-hypergraph-ramsey-problems_images/imageFile27.png>)

Soon after, Milans-Stolee-West [70] obtained an exact formula for rk(Ps1,... ,Psq) for all k,q ≥ 2, and si ≥ k (see [31, 35] for some related results).

![image 28](<2017-mubayi-survey-hypergraph-ramsey-problems_images/imageFile28.png>)

- Theorem 10.2 (Milans-Stolee-West [70]). Let k,q ≥ 2, and si > k for all i ∈ [q]. Let J1 be the poset comprising disjoint chains C1,... ,Cq, with |Ci| = si − k for i ∈ [q] and for i ≥ 1, let Ji+1 be the poset whose elements are the ideals (down sets) of Ji with order deﬁned by containment. Then


rk(Ps1,... ,Psq) = |Jk| + 1.

![image 29](<2017-mubayi-survey-hypergraph-ramsey-problems_images/imageFile29.png>)

![image 30](<2017-mubayi-survey-hypergraph-ramsey-problems_images/imageFile30.png>)

1The main result in [48], known as the Happy Ending Theorem, states that for any positive integer n, any suﬃciently large set of points in the plane in general position has a subset of n members that form the vertices of a convex polygon.

Just as before, we will use the simpler notation rk(Ps,n) = rk(Ps(k),Kn(k)), and note that there is only one ordered complete hypergraph Kn(k) up to isomorphism. Interestingly, the proof of the Erd˝os-Szekeres monotone subsequence theorem [48] (see also Dilworth’s Theorem [32]) actually implies that r2(Ps,n) = (n − 1)(s − 1) + 1. For k ≥ 3, estimating rk(Ps,n) appears to be more diﬃcult. Clearly we have

![image 31](<2017-mubayi-survey-hypergraph-ramsey-problems_images/imageFile31.png>)

![image 32](<2017-mubayi-survey-hypergraph-ramsey-problems_images/imageFile32.png>)

![image 33](<2017-mubayi-survey-hypergraph-ramsey-problems_images/imageFile33.png>)

![image 34](<2017-mubayi-survey-hypergraph-ramsey-problems_images/imageFile34.png>)

rk(Ps,n) ≤ rk(s,n) ≤ twrk−1(O(ns−2 log n)). (9)

![image 35](<2017-mubayi-survey-hypergraph-ramsey-problems_images/imageFile35.png>)

In [81], the authors established the following connection between the ordered Ramsey number rk(Ps,n) and the classical multi-color Ramsey number rk(n;q)

![image 36](<2017-mubayi-survey-hypergraph-ramsey-problems_images/imageFile36.png>)

Theorem 10.3 (Mubayi-Suk [81]). Let k ≥ 2 and s ≥ k + 1. Then for q = s − k + 1, we have rk−1(⌊n/q⌋;q) ≤ rk(Ps,n) ≤ rk−1(n;q).

![image 37](<2017-mubayi-survey-hypergraph-ramsey-problems_images/imageFile37.png>)

The upper bound in Theorem 10.3 follows from the following argument. Let q = s − k + 1, N = rk−1(n;q), and suppose χ is a red/blue coloring on the k-tuples of [N]. We can assume χ does not produce a red tight-path of length q, since otherwise we would have a red Ps and be done. We deﬁne the coloring φ : k [N−1] → {0,1,... ,q − 1} on the (k − 1)-tuples of [N], where φ(i1,... ,ik−1) = j if the longest red tight-path ending in vertices (i1,... ,ik−1) has length j. Since N = rk−1(n;q), by Ramsey’s theorem, we have a monochromatic clique of size n in color j for some

- j ∈ {0,1,... ,q − 1}. However, this clique would correspond to a blue clique with respect to χ. For


the lower bound, set N = rk−1(⌊n/q⌋;q) − 1, and let χ be a q coloring on the (k − 1)-tuples of [N] with colors {1,2,... ,q}, such that χ does not produce a monochromatic clique of size ⌊n/q⌋.

Then let φ : [Nk] → {red,blue} such that for i1 < ··· < ik, φ(i1,... ,ik) is red if and only if χ(i1,... ,ik−1) < χ(i2,... ,ik). It is easy to see that φ does not produce a red tight-path Ps. With a slightly more complicated argument, one can show by contradiction that φ also does not produce a monochromatic blue clique of size n.

The arguments above can be easily extended to obtain the following result for multiple colors [81]. Let k ≥ 2 and s1,... ,st ≥ k + 1. Then for q = (s1 − k + 1)··· (st − k + 1), we have

rk−1(⌊n/q⌋;q) ≤ rk(Ps1,... ,Pst,n) ≤ rk−1(n;q).

![image 38](<2017-mubayi-survey-hypergraph-ramsey-problems_images/imageFile38.png>)

Together with known bounds for rk−1(n;q), Theorem 10.3 has several consequences. First, we can considerably improve the upper bound for rk(Ps,n) in (9) to rk(Ps,n) ≤ twrk−1(O(sn log s)). In the other direction, the authors in [81] showed that r3(P4,n) > 2cn, and Theorem 10.3 implies that for k ≥ 4 and n > 3k,

![image 39](<2017-mubayi-survey-hypergraph-ramsey-problems_images/imageFile39.png>)

![image 40](<2017-mubayi-survey-hypergraph-ramsey-problems_images/imageFile40.png>)

![image 41](<2017-mubayi-survey-hypergraph-ramsey-problems_images/imageFile41.png>)

- 1. rk(Pk+3,n) ≥ twrk−1(cn),

![image 42](<2017-mubayi-survey-hypergraph-ramsey-problems_images/imageFile42.png>)

- 2. rk(Pk+2,n) ≥ twrk−1(clog2 n),

![image 43](<2017-mubayi-survey-hypergraph-ramsey-problems_images/imageFile43.png>)

- 3. rk(Pk+1,n) ≥ twrk−2(cn2).


![image 44](<2017-mubayi-survey-hypergraph-ramsey-problems_images/imageFile44.png>)

We conjecture the following strengthening of the Erd˝os-Hajnal conjecture.

Conjecture 10.4. For k ≥ 4 ﬁxed, rk(Pk+1,n) ≥ twrk−1(Ω(n)).

![image 45](<2017-mubayi-survey-hypergraph-ramsey-problems_images/imageFile45.png>)

For s = k + 1 in Theorem 10.3, we have rk−1(⌊n/2⌋,⌊n/2⌋) ≤ rk(Pk+1,n) ≤ rk−1(n,n). Hence, we obtain the following corollary which relates r4(P5,n) to the diagonal Ramsey number r3(n,n).

![image 46](<2017-mubayi-survey-hypergraph-ramsey-problems_images/imageFile46.png>)

![image 47](<2017-mubayi-survey-hypergraph-ramsey-problems_images/imageFile47.png>)

Corollary 10.5 ([81]). Conjecture 3.1 holds if and only if there is a constant c > 0 such that r4(P5,n) ≥ 22cn.

![image 48](<2017-mubayi-survey-hypergraph-ramsey-problems_images/imageFile48.png>)

For the case when the size of Ps tends to inﬁnity and the size of Kn is ﬁxed, the ﬁrst author in [76] showed that r3(Ps,4) < s21, and more generally for each k ≥ 3, there exists c > 0 such that for s large,

![image 49](<2017-mubayi-survey-hypergraph-ramsey-problems_images/imageFile49.png>)

twrk−2(sc) < rk(Ps,k + 1) < twrk−2(s62).

![image 50](<2017-mubayi-survey-hypergraph-ramsey-problems_images/imageFile50.png>)

Unfortunately much less is known about rk(Ps,k + 2). The main open problem here is to prove

![image 51](<2017-mubayi-survey-hypergraph-ramsey-problems_images/imageFile51.png>)

- that r3(Ps,5) has polynomial growth rate, and more generally, that r3(Ps,n) has polynomial growth rate for all ﬁxed n > 4. The corresponding results for higher uniformity follow easily from the case


![image 52](<2017-mubayi-survey-hypergraph-ramsey-problems_images/imageFile52.png>)

![image 53](<2017-mubayi-survey-hypergraph-ramsey-problems_images/imageFile53.png>)

- k = 3.


We next consider a version of the Erd˝os-Hajnal hypergraph Ramsey problem with respect to tightpaths.

- Deﬁnition 10.6. For integers 2 ≤ k < s < n and 2 ≤ t ≤ k s , let rk(s,t;Pn) be the minimum N such that every red/blue coloring of the k-sets of [N] results in a monochromatic blue copy of Pn or has a set of s vertices which induces at least t red edges.


![image 54](<2017-mubayi-survey-hypergraph-ramsey-problems_images/imageFile54.png>)

Of course, rk(s, k s ;Pn) = rk(s,Pn). We will focus our attention on the smallest case s = k + 1. The following conjecture which parallels the Erd˝os-Hajnal conjecture for cliques was posed in [76].

![image 55](<2017-mubayi-survey-hypergraph-ramsey-problems_images/imageFile55.png>)

![image 56](<2017-mubayi-survey-hypergraph-ramsey-problems_images/imageFile56.png>)

Conjecture 10.7 ([76]). For 3 ≤ t ≤ k, there are positive c = c(k,t) and c′ = c′(k,t) such that twrt−2(nc) < rk(k + 1,t;Pn) < twrt−2(nc′).

![image 57](<2017-mubayi-survey-hypergraph-ramsey-problems_images/imageFile57.png>)

This conjecture seems more diﬃcult than the original problem of Erd˝os and Hajnal. The current best lower bound is only an exponential function; unfortunately the constructions used for Theorem 5.5 fail. Standard arguments yield an upper bound of the form twrt−1(nc) for Conjecture 10.7. This upper bound was improved in [76] to twrt−2(nc). Some further minor progress towards Conjecture 10.7 was made in [76] for the cases t = 3 and (k,t) = (4,4).

## 10.2 Ordered ℓ-power paths in graphs

- As mentioned above, The proof of Dilworth’s theorem shows that r2(Ps,n) = r(Ps,Pn) = (s − 1)(n − 1) + 1. On the other hand, we know that the classical Ramsey number r2(n,n) grows exponentially in Θ(n). One can consider the case of ordered graphs that are denser than paths but sparser than cliques.


![image 58](<2017-mubayi-survey-hypergraph-ramsey-problems_images/imageFile58.png>)

![image 59](<2017-mubayi-survey-hypergraph-ramsey-problems_images/imageFile59.png>)

- Deﬁnition 10.8. Given ℓ ≥ 1, the ℓth power Psℓ of a path Ps has ordered vertex set v1 < ··· < vs and edge set {vivj : |i − j| ≤ ℓ}. In particular, Ps1 = Ps. The ordered Ramsey number r(Psℓ,Pnℓ)

is the minimum N such that every red/blue coloring of [N2] results in a red copy of Psℓ or a blue copy of Pnℓ.

In [76] it was shown that the problem of determining r(Pnℓ,Pnℓ) is closely related to the hypergraph ordered Ramsey function r3(s,Pn). Conlon-Fox-Lee-Sudakov [15] asked whether r(Pnℓ,Pnℓ) is polynomial in n for every ﬁxed ℓ ≥ 1. Actually, the problem in [15] is about the Ramsey number of ordered graphs with bandwidth at most ℓ but Pnℓ contains all such graphs so an upper bound for Pnℓ provides an upper bound for the bandwidth problem. This question was answered by Balko-Cibulka-Kra´l-Kyncˇl [3]. Later a better bound was proved in [76] for ℓ = 2.

![image 60](<2017-mubayi-survey-hypergraph-ramsey-problems_images/imageFile60.png>)

![image 61](<2017-mubayi-survey-hypergraph-ramsey-problems_images/imageFile61.png>)

![image 62](<2017-mubayi-survey-hypergraph-ramsey-problems_images/imageFile62.png>)

- Theorem 10.9 (Balko-Cibulka-Kra´l-Kyncˇl [3] (ℓ ≥ 3), Mubayi [76] (ℓ = 2)). There is an absolute constant c > 0 and for every ℓ > 0 there exists c = cℓ such that

![image 63](<2017-mubayi-survey-hypergraph-ramsey-problems_images/imageFile63.png>)

r(Pnℓ,Pnℓ) <

cn19.487 for ℓ = 2 cℓ n128ℓ for ℓ ≥ 3.

(10)

The main open problem here is to improve the exponents above. To our knowledge, there are no nontrivial lower bounds published for this problem.

- Problem 10.10 (Balko-Cibulka-Kra´l-Kyncˇl [3]). Determine the growth rate of r(Pnℓ,Pnℓ) for every ﬁxed ℓ ≥ 2.


![image 64](<2017-mubayi-survey-hypergraph-ramsey-problems_images/imageFile64.png>)

11 A bipartite hypergraph Ramsey problem of Erd˝os

We end with an old problem of Erd˝os that was perhaps posed to gain a better understanding of the growth rate of the diagonal Ramsey numbers.

Deﬁnition 11.1. Let Sa,b = (U,V,E) be the 3-graph with vertex set U ∪ V , where |U| = a and |V | = b, such that E(Sa,b) = {(x,y,z) : x ∈ U and y,z ∈ V }. Write Sn := Sn,n.

An old result due to Erd˝os (see [40]) says that r3(Sn,Sn) = 2O(n2), which is tight up to a constant factor in the exponent by the standard probabilistic method. We were not able to ﬁnd a published proof of this result and we therefore present a proof below (of a stronger result).

- Theorem 11.2. For every c > 0 and suﬃciently large n, r3(Sn,Sn) < r3(S2cn,n,S2cn,n) < 23n2.




Proof. We begin with the simple observation that r3(S1,n,S1,n) < 1 + r2(n,n) < 4n. Indeed, if r = 1 + r2(n,n) and [3r] is 2-colored by χ then we have an induced 2-coloring χ′ of [r−21] where χ′(ij) = χ(ijr). Because r − 1 = r2(n,n) we have a monochromatic n-set under χ′ and this yields a monochromatic S1,n under χ with U = {r}.

Now we use a simple supersaturation trick to prove the result. Suppose that N = 2c′n2 and χ is a 2-coloring of [N3] . For every r-set of [N], where r = 4n, there is a monochromatic copy of S1,n in χ. Hence the number of monochromatic copies of S1,n in χ is at least

N

(N)n+1 (r)n+1

r N−n−1 r−n−1

=

.

![image 65](<2017-mubayi-survey-hypergraph-ramsey-problems_images/imageFile65.png>)

![image 66](<2017-mubayi-survey-hypergraph-ramsey-problems_images/imageFile66.png>)

- At least half of these monochromatic copies of S1,n have the same color, say blue. Now, to each of these blue copies of S1,n with parts |U| = 1 and |V | = n, we associate the n-set V . A short calculation and the fact that n is large shows that


(N)n+1 (r)n+1

>

![image 67](<2017-mubayi-survey-hypergraph-ramsey-problems_images/imageFile67.png>)

2cNe n

![image 68](<2017-mubayi-survey-hypergraph-ramsey-problems_images/imageFile68.png>)

n

> 2cn

N n

.

Consequently, by the pigeonhole principle, there are at least 2cn blue copies of S1,n associated to the same n-set V . These blue copies together form a blue copy of Sn as desired.

![image 69](<2017-mubayi-survey-hypergraph-ramsey-problems_images/imageFile69.png>)

![image 70](<2017-mubayi-survey-hypergraph-ramsey-problems_images/imageFile70.png>)

![image 71](<2017-mubayi-survey-hypergraph-ramsey-problems_images/imageFile71.png>)

![image 72](<2017-mubayi-survey-hypergraph-ramsey-problems_images/imageFile72.png>)

Erd˝os stated that an important and diﬃcult problem is to decide if his result can be strengthened to imply all triples that meet both U and V .

- Deﬁnition 11.3. Let Bn = (U,V,E) be the 3-graph with vertex set U ∪ V , where |U| = |V | = n, such that E(Bn) = {(x,y,z) : x,y ∈ U,z ∈ V or x,y ∈ V,z ∈ U}.


Clearly we have

′n

2cn2 < r3(Bn,Bn) ≤ r3(n,n) ≤ 22c

where the lower bound follows from the probabilistic method.

- Problem 11.4 (Erd˝os [40]). Improve the upper or lower bounds for r3(Bn,Bn).


# References

- [1] M. Axenovich, A. Gy´arf´as, H. Liu, D. Mubayi, Multicolor Ramsey numbers for triple systems Discrete Math. 322 (2014), 69–77.
- [2] M. Ajtai, J. Komlo´s, E. Szemere´di, A note on Ramsey numbers, J. Combin. Theory Ser. A 29

(1980), 354–360.

- [3] M. Balko, J. Cibulka, K. Kra´l, J. Kyncˇl, Ramsey numbers of ordered graphs, submitted. arXiv:1310.7208. Extended abstract in: Proceedings of The Eight European Conference on Combinatorics, Graph Theory and Applications (EuroComb 2015), Electronic Notes in Discrete Mathematics 49 (2015), 419-424.
- [4] V. Bhat and V. Ro¨dl, Note on upper density of quasi-random hypergraphs, Electron. J. Combin. 20 (2013), no. 2, Paper 59, 8 pp.
- [5] T. Bohman, The triangle-free process, Adv. Math. 221 (2009), 1653–1677.
- [6] T. Bohman, A. Frieze, D. Mubayi, Coloring H-free hypergraphs, Random Structures and Algorithms, 36 (2010) 11–25.


- [7] T. Bohman, P. Keevash, The early evolution of the H-free process, Invent. Math. 181 (2010), 291–336.
- [8] T. Bohman and P. Keevash, Dynamic concentration of the triangle-free process, submitted, http://arxiv.org/abs/1302.5963arXiv.1302.5963.
- [9] T. Bohman, D. mubayi, M. Picollelli, The independent neighborhoods process, Israel J. Math. 214 (2016), 333–357.
- [10] A. Cameron, E. Heath, A (5,5)-coloring of the complete graph with few colors, https://arxiv.org/abs/1702.06227.
- [11] F. R. K. Chung, Open problems of Paul Erd˝os in graph theory J. Graph Theory 25 (1997), 3–36.
- [12] V. Chv´atal, V. Ro¨dl, E. Szemere´di and W. T. Trotter Jr, The Ramsey number of a graph with bounded maximum degree, J. Combin. Theory Ser. B 34 (1983), 239–243.
- [13] C. Collier-Cartaino, N. Graber, T. Jiang, Linear Tura´n numbers of r-uniform linear cycles and related Ramsey numbers, arXiv:1404.5015v2 (2014).
- [14] D. Conlon, A new upper bound for diagonal Ramsey numbers, Ann. Math. 170 (2009), 941– 960.
- [15] D. Conlon, J. Fox, C. Lee, B. Sudakov, Ordered Ramsey numbers, J. Combin. Theory Ser. B. 122 (2017), 353–383.
- [16] D. Conlon, J. Fox, C. Lee, B. Sudakov, On the grid Ramsey problem and related questions, Int. Math. Res. Not., 2015 (2015), 8052–8084.
- [17] D. Conlon, J. Fox, C. Lee and B. Sudakov, The Erd˝os-Gy´rf´as problem on generalized Ramsey numbers, Proc. London Math. Soc. 110 (2015), 1–18.
- [18] D. Conlon, J. Fox, V. Ro¨dl, Hedgehogs are not colour blind, J. Combin. 8 (2017), 475–485.
- [19] D. Conlon, J. Fox, and B. Sudakov, An improved bound for the stepping-up lemma, Discrete Appl. Math. 161 (2013), 1191–1196.
- [20] D. Conlon, J. Fox, and B. Sudakov, Large almost monochromatic subsets in hypergraphs, Israel Journal of Mathematics 181 (2011), 423–432.
- [21] D. Conlon, J. Fox, and B. Sudakov, Hypergraph Ramsey numbers, J. Amer. Math. Soc. 23

(2010), 247–266.

- [22] D. Conlon, J. Fox and B. Sudakov, On two problems in graph Ramsey theory, Combinatorica 32 (2012), 513–535.
- [23] D. Conlon, J. Fox, B. Sudakov, personal communication.
- [24] D. Conlon, J. Fox, B. Sudakov, Ramsey numbers of sparse hypergraphs, Random Structures and Algorithms 35 (2009), 1–14.


- [25] D. Conlon, J. Fox, and B. Sudakov, Short proofs of some extremal results, Combin. Probab. Comput. 23 (2014), 8–28.
- [26] D. Conlon, J. Fox, B. Sudakov, Recent developments in graph Ramsey theory, Surveys in Combinatorics (2015), 49–118.
- [27] O. Cooley, N. Fountoulakis, D. Ku¨hn, D. Osthus, 3-uniform hypergraphs of bounded degree have linear Ramsey numbers, J. Combin. Theory Ser. B. 98 (2008), 484–505.
- [28] O. Cooley, N. Fountoulakis, D. Ku¨hn, D. Osthus ,Embeddings and Ramsey numbers of sparse k-uniform hypergraphs, Combinatorica 29 (2009), 263–297.
- [29] J. Cooper, D. Mubayi, List Coloring Triangle-Free Hypergraphs, Random Structures and Algorithms 47 (2015), 487–519.
- [30] J. Cooper, D. Mubayi, Sparse hypergraphs with low independence number, Combinatorica 37

(2017), 31–40

- [31] C. Cox, D. Stolee, Ordered Ramsey numbers of loose paths and matchings, Discrete Math. 339 (2016), no. 2, 499-505.
- [32] R. P. Dilworth, A decomposition theorem for partially ordered sets, Ann. of Math. 51 (1950), 161–166.
- [33] A. Dudek, D. Mubayi, On generalized Ramsey numbers for 3-uniform hypergraphs, J. Graph Theory 76 (2014), 217–223.
- [34] A. Dudek, T. Retter, V. Ro¨dl, On generalized Ramsey numbers of Erd˝os and Rogers, J. Combin. Theory Ser. B 109 (2014), 213–227.
- [35] D. Duﬀus, H. Lefmann, and V. Ro¨dl, Shift graphs and lower bounds on Ramsey numbers rk(l;r), Discrete Math. 137 (1995), 177–187.
- [36] D. Eichhorn and D. Mubayi, Edge-coloring cliques with many colors on subcliques, Combinatorica 20 (2000), 441–444.
- [37] M. Elia´sˇ and J. Matousˇek, Higher-order Erd˝os-Szekeres theorems, Adv. Math. 244 (2013), 1–15.
- [38] P. Erd˝os, Some remarks on the theory of graphs, Bull. Amer. Math. Soc. 53 (1947), 292–294.
- [39] P. Erd˝os, Problems and results on ﬁnite and inﬁnite graphs, in Recent advances in graph theory (Proc. Second Czechoslovak Sympos., Prague, 1974), 183–192, Academia, Prague, 1975.
- [40] P. Erd˝os, Problems and results on graphs and hypergraphs: similarities and diﬀerences, in Mathematics of Ramsey theory, Algorithms Combin., Vol. 5 (J. Nesˇetrˇil and V. Ro¨dl) 12–28. Berlin: Springer-Verlag, 1990.
- [41] P. Erd˝os, Solved and unsolved problems in combinatorics and combinatorial number theory, in Proceedings of the twelfth southeastern conference on combinatorics, graph theory and comput-ing, Vol. I (Baton Rouge, La., 1981), Congr. Numer. 32 (1981), 49–62.


- [42] P. Erd˝os, Extremal problems in number theory, combinatorics and geometry, Proceedings of the International Congress of Mathematicians, Vol. 1, 2 (Warsaw, 1983), 51–70, PWN, Warsaw, 1984.
- [43] P. Erd˝os and A. Gy´arf´as, A variant of the classical Ramsey problem, Combinatorica 17 (1997), 459–467.
- [44] P. Erd˝os, A. Hajnal, On Ramsey like theorems, problems and results, in Combinatorics (Proc. Conf. Combinatorial Math., Math. Inst., Oxford, 1972), pp. 123–140, Inst. Math. Appl., Southhend-on-Sea, 1972.
- [45] P. Erd˝os, A. Hajnal, R. Rado, Partition relations for cardinal numbers, Acta Math. Acad. Sci. Hungar. 16 (1965), 93–196.
- [46] P. Erd˝os, R. Rado, Combinatorial theorems on classiﬁcations of subsets of a given set, Proc. Lond. Math. Soc. 3 (1952), 417–439.
- [47] P. Erd˝os, C.A. Rogers, The construction of certain graphs, Canad. J. Math. 14 (1962), 702– 707.
- [48] P. Erd˝os, G. Szekeres, A combinatorial problem in geometry, Compos. Math. 2 (1935), 463–470.
- [49] P. Erd˝os, G. Szekeres, On some extremum problems in elementary geometry, Ann. Univ. Sci. Budapest. Eo¨tv¨os Sect. Math., 3–4 (1960-61), 53–62.
- [50] G. Fiz Pontiveros, S. Griﬃths and R. Morris, The triangle-free process and R(3,k), submitted, http://arxiv.org/abs/1302.6279 arXiv.1302.6279.
- [51] J. Fox and B. Sudakov, Ramsey-type problem for an almost monochromatic K4, SIAM J. Discrete Math. 23 (2008), 155–162.
- [52] J. Fox, J. Pach, B. Sudakov, and A. Suk, Erd˝os-Szekeres-type theorems for monotone paths and convex bodies, Proc. Lond. Math. Soc. 105 (2012), 953–982.
- [53] R. L. Graham, B. L. Rothschild and J. H. Spencer, Ramsey theory, second ed., Wiley Interscience Series in Discrete Mathematics and Optimization, John Wiley & Sons Inc., New York, 1990.
- [54] A. Gy´arf´as, G. Raeisi, The Ramsey number of loose triangles and quadrangles in hypergraphs, Electron. J. Combin. 19 (2) (2012) #R30.
- [55] P. Haxell, T. Luczak, Y. Peng, V. Ro¨dl, A. Rucin´ski, M. Simonovits, J. Skokan, The Ramsey number for hypergraph cycles I, J. Combin. Theory Ser. A 113 (2006) 67–83.
- [56] P. Haxell, T. Luczak, Y. Peng, V. Ro¨dl, A. Rucin´ski, J. Skokan, The Ramsey number for hypergraph cycles II, Combin., Probab. Comput. 18 (2009) 165–203
- [57] J. H. Kim, The Ramsey number R(3,t) has order of magnitude t2/log t, Random Structures Algorithms 7 (1995), 173–207.
- [58] Y. Kohayakawa, B. Nagle, V. Ro¨dl, and M. Schacht, Weak hypergraph regularity and linear hypergraphs, J. Combin. Theory Ser. B 100 (2010), 151–160.


- [59] G. Ka´rolyi, P. Valtr, Point conﬁgurations in d-space without large subsets in convex position, Disc. Comp. Geom. 30 (2003), 277–286.
- [60] A. Kostochka and D. Mubayi, When is an almost monochromatic K4 guaranteed?, Combin. Probab. Comput. 17 (2008), 823–830.
- [61] A. Kostochka, D. Mubayi, J. Verstrae¨te, Hypergraph Ramsey Numbers: Triangles versus Cliques, J. Combin Theory, Series A 120 (2013), 1491–1507.
- [62] A. Kostochka, D. Mubayi, J. Verstrae¨te, On independent sets in hypergraphs, Random Structures Algorithms 44 (2014), 224–239.
- [63] Y. Ishigami, Linear Ramsey numbers for bounded-degree hypergraphs, Electronic Notes in Discrete Mathematics 29 (2007), 47–51.
- [64] J. Lenz and D. Mubayi, The poset of hypergraph quasirandomness, Random Structures Algorithms 46 (2015), 762–800.
- [65] J. Lenz and D. Mubayi, Eigenvalues and linear quasirandom hypergraphs, Forum Math. Sigma 3 (2015), e2, 26 pp.
- [66] N. Linial and A. Morgenstern, On high-dimensional acyclic tournaments, Discrete Comput. Geom. 50 (2013), 1085-1100.
- [67] T. Luczak, J. Polcyn, The multipartite Ramsey number for the 3-path of length three, https://arxiv.org/abs/1706.08937
- [68] J. Matousˇek, Lectures in Discrete Geometry, Springer, 2002.
- [69] A. Me´roueh, The Ramsey number of loose cycles versus cliques, https://arxiv.org/abs/1504.03668.
- [70] K.G. Milans, D. Stolee, and D. West, Ordered Ramsey theory and track representations of graphs, to appear in J. Combinatorics.
- [71] G. Moshkovitz and A. Shapira, Ramsey-theory, integer partitions and a new proof of the Erd˝os-Szekeres theorem, Adv. Math. 262 (2014), 1107–1129.
- [72] T. Motzkin, Cooperative classes of ﬁnite sets in one and more dimensions, Journal of Combinatorial Theory 3 (1967), 244–251.
- [73] D. Mubayi, Edge-coloring cliques with three colors on all 4-cliques, Combinatorica 18 (1998), 293–296.
- [74] D. Mubayi, An explicit construction for a Ramsey problem, Combinatorica, 24 (2004), 313–324
- [75] D. Mubayi, Coloring triple systems with local conditions, J. Graph Theory 81 (2016), 307–311.
- [76] D. Mubayi, Variants of the Erd˝os-Szekeres and Erd˝os-Hajnal Ramsey problems, European J. Combin. 62 (2017), 197–205.
- [77] D. Mubayi, Improved bounds for the Ramsey number of tight cycles versus cliques Combin. Probab. Comput. 25 (2016), 791–796.


- [78] D. Mubayi and V. Ro¨dl, Hypergraph Ramsey numbers: tight cycles versus cliques, Bull. Lond. Math. Soc. 48 (2016), 127–134.
- [79] D. Mubayi, A. Suk, New lower bounds for hypergraph Ramsey numbers, submitted.
- [80] D. Mubayi, A. Suk, Constructions in Ramsey theory, submitted.
- [81] D. Mubayi, A. Suk, Oﬀ-diagonal hypergraph Ramsey numbers, submitted.
- [82] D. Mubayi, A. Suk, The Erdos-Hajnal hypergraph Ramsey problem, submitted.
- [83] B. Nagle, S. Olsen, V. Ro¨dl, M. Schacht, On the Ramsey number of sparse 3-graphs, Graphs Combin. 24 (2008), 205–228.
- [84] K. T. Phelps, V. Ro¨dl, Steiner triple systems with minimum independence number, Ars Combin. 21 (1986), 167–172.
- [85] J. Polcyn, A. Rucin´ski, Reﬁned Turan numbers and Ramsey numbers for the loose 3-uniform path of length three, Discrete Math. 340 (2017), 107–118
- [86] Y. Caro, Y. Li, C. Rousseau and Y. Zhang, Asymptotic bounds for some bipartite graph: complete graph Ramsey numbers, Discrete Math. 220 (2000), 51–56.
- [87] F. Ramsey, On a Problem of Formal Logic, Proc. London Math. Soc. 30 (1930), 264–286.
- [88] V. Ro¨dl and E. Sinajov´a,ˇ Note on independent sets in steiner systems, Random Structures Algorithms 5 (1994), 183–190.
- [89] S. Shelah, Primitive recursive bounds for van der Waerden numbers, J. Amer. Math. Soc. 1

(1989), 683–697.

- [90] J. Spencer, Ramsey’s theorem - a new lower bound, J. Combin. Theory Ser. A 18, 108–115.
- [91] B. Sudakov, A new lower bound for a Ramsey-type problem, Combinatorica 25 (2005), 487– 498.
- [92] A. Suk, On the Erd˝os-Szekeres convex polygon problem, to appear in Journal of the American Mathematical Society.
- [93] G. Wolfowitz, K4-free graphs without large induced triangle-free subgraphs, Combinatorica 33 (2013), 623–631.


