arXiv:1604.08657v2[math.CO]27Aug2016

On the Erd˝os-Szekeres convex polygon problem

Andrew Suk∗

Abstract

Let ES(n) be the smallest integer such that any set of ES(n) points in the plane in general position contains n points in convex position. In their seminal 1935 paper, Erdo˝s and Szekeres showed that ES(n) ≤ 2nn−−24 + 1 = 4n−o(n). In 1960, they showed that ES(n) ≥ 2n−2 + 1 and conjectured this to be optimal. In this paper, we nearly settle the Erdo˝s-Szekeres conjecture by showing that ES(n) = 2n+o(n).

# 1 Introduction

In their classic 1935 paper, Erd˝os and Szekeres [7] proved that, for every integer n ≥ 3, there is a minimal integer ES(n), such that any set of ES(n) points in the plane in general position1 contains n points in convex position, that is, they are the vertices of a convex n-gon.

Erd˝os and Szekeres gave two proofs of the existence of ES(n). Their ﬁrst proof used a quantitative version of Ramsey’s Theorem, which gave a very poor upper bound for ES(n). The second proof was more geometric and showed that ES(n) ≤ 2nn−−24 + 1 (see Theorem 2.2 in the next section). On the other hand, they showed that ES(n) ≥ 2n−2 + 1 and conjectured this to be sharp [8].

Small improvements have been made on the upper bound 2nn−−24 +1 ≈ √4nn by various researchers [3, 13, 22, 23, 17, 18], but no improvement in the order of magnitude has ever been made. The most recent upper bound, due to Norin and Yuditsky [18] and Mojarrad and Vlachos [17], says that

![image 1](<2016-suk-erdos-szekeres-convex-polygon-problem_images/imageFile1.png>)

![image 2](<2016-suk-erdos-szekeres-convex-polygon-problem_images/imageFile2.png>)

lim sup

n→∞

In the present paper, we prove the following.

ES(n)

7 16

≤

.

![image 3](<2016-suk-erdos-szekeres-convex-polygon-problem_images/imageFile3.png>)

![image 4](<2016-suk-erdos-szekeres-convex-polygon-problem_images/imageFile4.png>)

2n−4 n−2

- Theorem 1.1. For all n ≥ n0, where n0 is a large absolute constant, ES(n) ≤ 2n+6n2/3 logn.


The study of ES(n) and its variants2 has generated a lot of research over the past several decades. For a more thorough history on the subject, we refer the interested reader to [15, 2, 22]. All logarithms are to base 2.

![image 5](<2016-suk-erdos-szekeres-convex-polygon-problem_images/imageFile5.png>)

∗University of Illinois, Chicago, IL. Supported by NSF grant DMS-1500153. Email: suk@uic.edu.

- 1No three of the points are on a line. 2Higher dimensions [11, 12, 21], for families of convex bodies in the plane [9, 5], etc.


Figure 1: A 4-cup and a 5-cap.

# 2 Notation and tools

In this section, we recall several results that will be used in the proof of Theorem 1.1. We start with the following simple lemma.

Lemma 2.1 (See Theorem 1.2.3 in [14]). Let X be a ﬁnite point set in the plane in general position such that every four members in X are in convex position. Then X is in convex position.

The next theorem is a well-known result from [7], which is often referred to as the Erd˝os-Szekeres cups-caps theorem. Let X be a k-element point set in the plane in general position. We say that X forms a k-cup (k-cap) if X is in convex position and its convex hull is bounded above (below) by a single edge. In other words, X is a cup (cap) if and only if for every point p ∈ X, there is a line L passing through it such that all of the other points in X lie on or above (below) L. See Figure 1.

- Theorem 2.2 ([7]). Let f(k,ℓ) be the smallest integer N such that any N-element planar point set in the plane in general position contains a k-cup or an ℓ-cap. Then


f(k,ℓ) =

k + ℓ − 4 k − 2

+ 1.

The next theorem is a combinatorial reformulation of Theorem 2.2 observed by Hubard et al. [10] (see also [9, 16]). A transitive 2-coloring of the triples of {1,2,... ,N} is a 2-coloring, say with colors red and blue, such that, for i1 < i2 < i3 < i4, if triples (i1,i2,i3) and (i2,i3,i4) are red (blue), then (i1,i2,i4) and (i1,i3,i4) are also red (blue).

- Theorem 2.3 ([7]). Let g(k,ℓ) denote the minimum integer N such that, for every transitive 2coloring on the triples of {1,2,... ,N}, there exists a red clique of size k or a blue clique of size ℓ. Then

g(k,ℓ) = f(k,ℓ) =

k + ℓ − 4 k − 2

+ 1.

The next theorem is due to Po´r and Valtr [20], and is often referred to as the positive-fraction

Erd˝os-Szekeres theorem (see also [1, 19]). Given a k-cap (k-cup) X = {x1,... ,xk}, where the points appear in order from left to right, we deﬁne the support of X to be the collection of open

regions C = {T1,... ,Tk}, where Ti is the region outside of conv(X) bounded by the segment xixi+1 and by the lines xi−1xi, xi+1xi+2 (where xk+1 = x1, xk+2 = x2, etc.). See Figure 2.

![image 6](<2016-suk-erdos-szekeres-convex-polygon-problem_images/imageFile6.png>)

- Theorem 2.4 (Proof of Theorem 4 in [20]). Let k ≥ 3 and let P be a ﬁnite point set in the plane in general position such that |P| ≥ 232k. Then there is a k-element subset X ⊂ P such that X is


T3

T4

x

x

4

T2

3

x2 B3 x5

T1

x

1

T5

x

6

T6

Figure 2: Regions T1,... ,T6 in the support of X = {x1,... ,x6}, and segment B3.

either a k-cup or a k-cap, and the regions T1,... ,Tk−1 from the support of X satisfy |Ti∩P| ≥ 2|32P|k . In particular, every (k −1)-tuple obtained by selecting one point from each Ti ∩P, i = 1,... ,k − 1, is in convex position.

![image 7](<2016-suk-erdos-szekeres-convex-polygon-problem_images/imageFile7.png>)

Note that Theorem 2.4 does not say anything about the points inside region Tk. Let us also remark that in the proof of Theorem 2.4 in [20], the authors ﬁnd a 2k-element set X ⊂ P, such that k of the regions in the support of X each contain at least 2|32Pk| points from P, and therefore these regions may not be consecutive. However, by appropriately selecting a k-element subset X′ ⊂ X, we obtain Theorem 2.4.

![image 8](<2016-suk-erdos-szekeres-convex-polygon-problem_images/imageFile8.png>)

# 3 Proof of Theorem 1.1

Let P be an N-element planar point set in the plane in general position, where N = ⌊2n+6n2/3 logn⌋ and n ≥ n0, where n0 is a suﬃciently large absolute constant. Set k = ⌈n2/3⌉. We apply Theorem 2.4 to P with parameter k + 3, and obtain a subset X = {x1,... ,xk+3} ⊂ P such that X is a cup or a cap, and the points in X appear in order from left to right. Moreover since k = ⌈n2/3⌉ is large, regions T1,... ,Tk+2 in the support of X satisfy

N 240k

|Ti ∩ P| ≥

.

![image 9](<2016-suk-erdos-szekeres-convex-polygon-problem_images/imageFile9.png>)

Set Pi = Ti ∩ P for i = 1,... ,k + 2. We will assume that X is a cap, since a symmetric argument would apply. We say that the two regions Ti and Tj are adjacent if i and j are consecutive indices.

Consider the subset Pi ⊂ P and the region Ti, for some ﬁxed i ∈ {2,... ,k + 1}. Let Bi be the segment xi−1xi+2. See Figure 2. The point set Pi naturally comes with a partial order ≺, where p ≺ q if p = q and q ∈ conv(Bi ∪ p). Set α = 3n−1/3 log n. By Dilworth’s Theorem [4], Pi contains

![image 10](<2016-suk-erdos-szekeres-convex-polygon-problem_images/imageFile10.png>)

either a chain of size at least |Pi|1−α or an antichain of size at least |Pi|α with respect to ≺. The proof now falls into two cases.

- Case 1. Suppose there are t = ⌈n12/3⌉ parts Pi in the collection F = {P2,P3,... ,Pk+1}, such that no two of them are in adjacent regions, and each such part contains a subset Qi of size at least |Pi|α such that Qi is an antichain with respect to ≺. Let Qj1,Qj2,... ,Qjt be the selected subsets.

![image 11](<2016-suk-erdos-szekeres-convex-polygon-problem_images/imageFile11.png>)

For each Qjr, r ∈ {1,... ,t}, the line spanned by any two points in Qjr does not intersect the segment Bjr, and therefore, does not intersect region Tjw for w = r (by the non-adjacency property). Since n is suﬃciently large, we have 40k < n2/3 log n, and therefore

|Qjr| ≥ |Pi|α ≥

N 240k

![image 12](<2016-suk-erdos-szekeres-convex-polygon-problem_images/imageFile12.png>)

α

≥ 23n2/3 logn+15n1/3 log2 n ≥

n + ⌈2n2/3⌉ − 4 n − 2

+ 1 = f(n,⌈2n2/3⌉).

Theorem 2.2 implies that Qjr contains either an n-cup or a ⌈2n2/3⌉-cap. If we are in the former case for any r ∈ {1,... ,t}, then we are done. Therefore we can assume Qjr contains a subset Sjr that is a ⌈2n2/3⌉-cap, for all r ∈ {1,... ,t}.

We claim that S = Sj1 ∪ ··· ∪ Sjt is a cap, and therefore S is in convex position. Let p ∈ Sjr. Since |Sjr| ≥ 2, there is a point q ∈ Sjr such that the line L supported by the segment pq has the property that all of the other points in Sjr lie below L. Since L does not intersect Bjr, all of the points in S \ {p,q} must lie below L. Hence, S is a cap and

![image 13](<2016-suk-erdos-szekeres-convex-polygon-problem_images/imageFile13.png>)

|S| = |Sj1 ∪ ··· ∪ Sjt| ≥

n1/3 2

![image 14](<2016-suk-erdos-szekeres-convex-polygon-problem_images/imageFile14.png>)

(2n2/3) = n.

- Case 2. Suppose we are not in Case 1. Then there are ⌈n1/3⌉ consecutive indices j,j +1,j +2,... , such that each such part Pj+r contains a subset Qj+r such that Qj+r is a chain of length at least |Pj+r|1−α with respect to ≺. For simplicity, we can relabel these sets Q1,Q2,Q3,....


Consider the subset Qi inside the region Ti, and order the elements in Qi = {p1,p2,p3,...} with respect to ≺. We say that Y ⊂ Qi is a right-cap if xi ∪ Y is in convex position, and we say that Y is a left-cap if xi+1 ∪ Y is in convex position. Notice that left-caps and right-caps correspond to the standard notion of cups and caps after applying an appropriate rotation to the plane so that the segment xixi+1 is vertical. Since Qi is a chain with respect to ≺, every triple in Qi is either a left-cap or a right-cap, but not both. Moreover, for i1 < i2 < i3 < i4, if (pi1,pi2,pi3) and (pi2,pi3,pi4) are right-caps (left-caps), then (pi1,pi2,pi4) and (pi1,pi3,pi4) are both right-caps (left-caps). By Theorem 2.3, if |Qi| ≥ f(k,ℓ), then Qi contains either a k-left-cap or an ℓ-right-cap. We make the following observation.

![image 15](<2016-suk-erdos-szekeres-convex-polygon-problem_images/imageFile15.png>)

Observation 3.1. Consider the (adjacent) sets Qi−1 and Qi. If Qi−1 contains a k-left-cap Yi−1, and Qi contains an ℓ-right-cap Yi, then Yi−1 ∪ Yi forms k + ℓ points in convex position.

Proof. By Lemma 2.1, it suﬃces to show every four points in Yi−1 ∪ Yi are in convex position. If all four points lie in Yi, then they are in convex position. Likewise if they all lie in Yi−1, they are in convex position. Suppose we take two points p1,p2 ∈ Yi−1 and two points p3,p4 ∈ Yi. Since Qi−1 and Qi are both chains with respect to ≺, the line spanned by p1,p2 does not intersect the region Ti, and the line spanned by p3,p4 does not intersect the region Ti−1. Hence p1,p2,p3,p4 are in convex position. Now suppose we have p1,p2,p3 ∈ Yi−1 and p4 ∈ Yi. Since the three lines L1,L2,L3 spanned by p1,p2,p3 all intersect the segment Bi−1, both xi and p4 lie in the same region in the arrangement of L1 ∪ L2 ∪ L3. Therefore p1,p2,p3,p4 are in convex position. The same argument follows in the case that p1 ∈ Yi−1 and p2,p3,p4 ∈ Yi. See Figure 3.

![image 16](<2016-suk-erdos-szekeres-convex-polygon-problem_images/imageFile16.png>)

![image 17](<2016-suk-erdos-szekeres-convex-polygon-problem_images/imageFile17.png>)

![image 18](<2016-suk-erdos-szekeres-convex-polygon-problem_images/imageFile18.png>)

![image 19](<2016-suk-erdos-szekeres-convex-polygon-problem_images/imageFile19.png>)

## xi

xi−1 xi+1

Figure 3: A 3-left-cap in Qi−1 and a 4-right-cap in Qi, which forms 7 points in convex position.

We have for i ∈ {1,... ,⌈n1/3⌉},

|Qi| ≥ |Pi|(1−α) ≥

N 240k

![image 20](<2016-suk-erdos-szekeres-convex-polygon-problem_images/imageFile20.png>)

1−α

≥ 2n+2n2/3 logn−15n1/3 log2 n. (1)

Set K = ⌈n2/3⌉. Since n is suﬃciently large, we have

|Q1| ≥

n + K − 4 K − 2

+ 1 = f(K,n),

which implies that Q1 either contains an n-right-cap, or a K-left-cap. In the former case we are done, so we can assume that Q1 contains a K-left-cap. Likewise, |Q2| ≥ n2+KK−−24 +1 = f(2K,n−K), which implies Q2 contains either an (n − K)-right-cap, or a (2K)-left-cap. In the former case we are done since Observation 3.1 implies that the K-left-cap in Q1 and the (n − K)-right-cap in Q2 form n points in convex position. Therefore we can assume Q2 contains a (2K)-left-cap.

In general, if we know that Qi−1 contains an (iK − K)-left-cap, then we can conclude that Qi contains an (iK)-left-cap. Indeed, for all i ≤ ⌈n1/3⌉ we have

n + K − 4 iK − 2

≤ 2n+⌈n2/3⌉−4. (2) Since n is suﬃciently large, (1) and (2) imply that

|Qi| ≥ 2n+2n2/3 logn−15n1/3 log2 n ≥

n + K − 4 iK − 2

+ 1 = f(iK,n − iK + K).

Therefore, Qi contains either an (n − iK + K)-right-cap or an (iK)-left-cap. In the former case we are done by Observation 3.1 (recall that we assumed Qi−1 contains an (iK − K)-left-cap), and therefore we can assume Qi contains an (iK)-left-cap. Hence for i = ⌈n1/3⌉, we can conclude that Q⌈n1/3⌉ contains an n-left-cap. This completes the proof of Theorem 1.1.

![image 21](<2016-suk-erdos-szekeres-convex-polygon-problem_images/imageFile21.png>)

![image 22](<2016-suk-erdos-szekeres-convex-polygon-problem_images/imageFile22.png>)

![image 23](<2016-suk-erdos-szekeres-convex-polygon-problem_images/imageFile23.png>)

![image 24](<2016-suk-erdos-szekeres-convex-polygon-problem_images/imageFile24.png>)

# 4 Concluding remarks

Following the initial publication of this work on arXiv, we have learned that Ga´bor Tardos has improved the lower order term in the exponent, showing that ES(n) = 2n+O(

√nlogn).

![image 25](<2016-suk-erdos-szekeres-convex-polygon-problem_images/imageFile25.png>)

Acknowledgments. I would like to thank Ja´nos Pach, Ga´bor Tardos, and Ge´za T´oth for numerous helpful comments.

# References

- [1] I. B´ara´ny and P. Valtr, A positive fraction Erd˝os-Szekeres theorem, Discrete Comput. Geom. 19 (1998), 335–342.
- [2] P. Brass, W. Moser, and J. Pach, Convex polygons and the Erd˝os Szekeres problem, Chapter 8.2 in Research problems in discrete geometry, Springer, (2005).
- [3] F. R. K. Chung and R. L. Graham, Forced convex n-gons in the plane, Discrete Comput. Geom. 19 (1998), 367–371.
- [4] R. Dilworth, A decomposition theorem for partially ordered sets, Ann. of Math. 51 (1950), 161–166.
- [5] M. Dobbins, A. Holmsen, and A. Hubard, The Erd˝os-Szekeres problem for non-crossing convex sets, Mathematika 60 (2014), 463–484.
- [6] P. Erd˝os, Some of my favorite problems and results, The Mathematics of Paul Erdo˝s, Vol. I (R. L. Graham and J. Nesetril, eds.), Springer-Verlag, Berlin, 1997, 47–67.
- [7] P. Erd˝os and G. Szekeres, A combinatorial problem in geometry, Compos. Math. 2 (1935), 463–470.
- [8] P. Erd˝os and G. Szekeres, On some extremum problems in elementary geometry, Ann. Univ. Sci. Budapest. Eo¨tv¨os Sect. Math. 3-4 (1960/1961), 53–62.
- [9] J. Fox, J. Pach, B. Sudakov, and A. Suk, Erd˝os-Szekeres-type theorems for monotone paths and convex bodies, Proc. Lond. Math. Soc. 105 (2012), 953–982.
- [10] A. Hubard, L. Montejano, E. Mora, and A. Suk, Order types of convex bodies, Order 28

(2011), 121–130.

- [11] G. Ka´rolyi, Ramsey-remainder for convex sets and the Erd˝os-Szekeres theorem, Discrete Appl. Math. 109 (2001), 163–175.
- [12] G. Ka´rolyi and P. Valtr, Point conﬁgurations in d-space without large subsets in convex position, Discrete Comput. Geom. 30 (2003) 277–286.
- [13] D. Kleitman and L. Pachter, Finding convex sets among points in the plane, Discrete Comput. Geom. 19 (1998), 405–410.
- [14] J. Matousˇek, Lectures on Discrete Geometry, Springer-Verlag New York, Inc., 2002.


- [15] W. Morris and V. Soltan, The Erd˝os-Szekeres problem on points in convex position - a survey, Bull. Amer. Math. Soc. 37 (2000), 437–458.
- [16] G. Moshkovitz and A. Shapira, Ramsey Theory, integer partitions and a new proof of the Erd˝os-Szekeres Theorem, Adv. Math. 262 (2014), 1107–1129.
- [17] H. Mojarrad and G. Vlachos, On the Erd˝os-Szekeres conjecture, Discrete Comput. Geom. 56

(2016), 165–180.

- [18] S. Norin and Y. Yuditsky, Erd˝os-Szekeres without induction, http://arxiv.org/abs/1509.03332,

(2015).

- [19] J. Pach and J. Solymosi, Canonical theorems for convex sets, Discrete Comput. Geom. 19

(1998), 427–435.

- [20] A. Po´r and P. Valtr, The partitioned version of the Erd˝os-Szekeres theorem, Discrete Comput. Geom. 28 (2002), 625–637.
- [21] A. Suk, A note on order-type homogeneous point sets, Mathematika 60 (2014), 37–42.
- [22] G. To´th and P. Valtr, The Erd˝os-Szekeres theorem: Upper bounds and related results, Combinatorial and Computational Geometry (J.E. Goodman et al., eds.), Publ. M.S.R.I. 52 (2006) 557–568.
- [23] G. To´th and P. Valtr, Note on the Erd˝os-Szekeres theorem, Discrete Comput. Geom. 19 (1998), 457–459.


