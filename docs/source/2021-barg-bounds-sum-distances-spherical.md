---
type: source
kind: paper
title: Bounds for the sum of distances of spherical sets of small size
authors: Alexander Barg, Peter Boyvalenkov, Maya Stoyanova
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2105.03511v2
source_local: ../raw/2021-barg-bounds-sum-distances-spherical.pdf
topic: general-knowledge
cites:
---

arXiv:2105.03511v2[math.MG]21Dec2022

BOUNDS FOR THE SUM OF DISTANCES OF SPHERICAL SETS OF SMALL SIZE

ALEXANDER BARG1, PETER BOYVALENKOV2, MAYA STOYANOVA3

ABSTRACT. We derive upper and lower bounds on the sum of distances of a spherical code of size N in n dimensions when N “ Θpnαq, 0 ă α ď 2. The bounds are derived by specializing recent general, universal bounds on energy of spherical sets. We discuss asymptotic behavior of our bounds along with several examples of codes whose sum of distances closely follows the upper bound.

1. INTRODUCTION: SUM OF DISTANCES AND RELATED PROBLEMS

- 1.1. Problem statement and overview of results. Let CN “ tz1,...,zNu be a set of N points (code) on


řN

the unit sphere Sn´1 in Rn. Denote by τnpCNq “

i,j“1 }zi ´ zj} the sum of pairwise distances between the points in CN and let τpn,Nq “ supC

τnpCNq be the largest attainable sum of distances over all sets of cardinality N. The problem of estimating τpn,Nq was introduced by Fejes To´th [29] and it has been studied in a large number of follow-up papers, [32, 10]. The main body of results in the literature are concerned with the asymptotic regime of ﬁxed n and N Ñ 8. In particular, it is known that

N

1 n´1

1

cN1´

ď WpSn´1qN2 ´ τpn,Nq ď CN1´

n´1, (1) where WpSn´1q “

![image 1](<2021-barg-bounds-sum-distances-spherical_images/imageFile1.png>)

![image 2](<2021-barg-bounds-sum-distances-spherical_images/imageFile2.png>)

ť

}x ´ y}dσnpxqdσnpyq is the average distance on the sphere, σn is the normalized (surface area) measure on the sphere. and c,C are some positive constants that depend only on n. The upper bound in (1) is due to Alexander [1] for n “ 3 and Stolarsky [48] for higher dimensions, and the lower bound was proved by Beck [6]. Kuijlaars and Saff [37] extended these results to bounds on the s-Riesz energy of spherical sets for all s ą 0, and Brauchart et al. [17] computed next terms of the asymptotics; see also Ch. 6 in a comprehensive monograph by Borodachov et al. [11] for a recent overview.

In this paper we adopt a different view, allowing both the dimension n and the cardinality N to increase in a certain related way. The main emphasis of this work is on obtaining explicit lower and upper bounds on the sum of distances of a spherical set CN for N „ δnα, for certain δ and 0 ă α ď 2. Upper bounds apply uniformly for all spherical sets, while to derive lower bounds we need to assume that the minimum pairwise distance is bounded from below (otherwise the sum of distances can be made arbitrarily small). If the minimum distance is large, then the neighbors of a point are naturally placed on or near the orthogonal subsphere (the “equator”), and the distance to them is about ?2. This suggests that the main term in the asymptotic expression for the sum of distances is ?2N2, and it is easy to obtain a bound of the form τpn,Nq ď

![image 3](<2021-barg-bounds-sum-distances-spherical_images/imageFile3.png>)

![image 4](<2021-barg-bounds-sum-distances-spherical_images/imageFile4.png>)

?2N2p1 ` op1qq, as shown below in Sec. 1.2.

![image 5](<2021-barg-bounds-sum-distances-spherical_images/imageFile5.png>)

Our main results are related to reﬁnements of this claim. Using linear programming, we derive lower and upper bounds for the sum of distances of codes of small size. For a number of code families, the sum of distances behaves as ?2N2, and the bound is asymptotically tight. We compute lower-order terms in a number of examples, including codes obtained from equiangular line sets, spherical embeddings of strongly regular graphs (two-distance tight frames), and spherical embeddings of some classes of small-size binary

![image 6](<2021-barg-bounds-sum-distances-spherical_images/imageFile6.png>)

![image 7](<2021-barg-bounds-sum-distances-spherical_images/imageFile7.png>)

- 1 Department of ECE and ISR, University of Maryland, College Park, MD 20742, USA. Supported in part by NSF grants CCF

1814487, CCF 2110113 (NSF-BSF) and CCF 2104489. Email: abarg@umd.edu.

- 2 Institute of Mathematics and Informatics, Bulgarian Academy of Sciences, 8 G Bonchev Str., 1113 Soﬁa, Bulgaria. Supported in

part by Bulgarian NSF project KP-06-Russia/33-2020. Email: peter@math.bas.bg.

- 3 Faculty of Mathematics and Informatics, Soﬁa University, 5 James Bourchier Blvd., 1164 Soﬁa, Bulgaria. Supported in part by


Bulgarian NSF project KP-06-N32/2-2019. Email: stoyanova@fmi.uni-soﬁa.bg.

1

codes. Numerical calculations, some of which we include, conﬁrm that the sum of distances of these codes follows closely the upper bound.

- 1.2. Sum of distances and Stolarsky’s invariance. The sum of distances in a spherical code enjoys several links with other problems in geometry of spherical sets. One of them is related to the theory of uniform


distributions on the sphere. A sequence of spherical sets pCNqN is called asymptotically uniformlydistributed if for every closed set A Ă Sn´1

|CN X A|

N “ σnpAq. To quantify the proximity of a sequence of sets CN to the uniform distribution on Sn´1, deﬁne the quadratic discrepancy1 of CN :

lim

![image 8](<2021-barg-bounds-sum-distances-spherical_images/imageFile8.png>)

NÑ8

ÿN

pCNq :“ ż 1

ż

1 N

2

DL

Cpx,tqpzjq ´ σnpCpx,tqqˇ

dσnpxqdt, (2)

2

![image 9](<2021-barg-bounds-sum-distances-spherical_images/imageFile9.png>)

ˇ

Sn´1

´1

j“1

where Cpx,tq “ ty P Sn´1 : px ¨ yq ě tu is a spherical cap of radius arccost centered at x. A classic result states that a sequence of sets CN is asymptotically uniformly distributed if and only if limNÑ8 DL

pCNq “ 0; see, e.g., [11, Theorem 6.1.5]. A fundamental relation between τnpCNq and DL

2

pCNq states that the sum of these two quantities is a constant that depends only on N and n. Namely,

2

1 N2

pCNq “ WpSn´1q ´

cnDL

τnpCNq, (3) where cn “ pn ´ 1q

2

![image 10](<2021-barg-bounds-sum-distances-spherical_images/imageFile10.png>)

?πΓppn ´ 1q{2q{Γpn{2q is a universal constant that depends only on the dimension of the sphere. This relation was proved by Stolarsky [48] and is now known as Stolarsky’s invariance principle. The average distance on the sphere is given by

![image 11](<2021-barg-bounds-sum-distances-spherical_images/imageFile11.png>)

şπ 0 2 sinpθ{2qsinn´1 θdθ{

şπ

0 sinn´1 θdθ, which evaluates to WpSn´1q “

?

2n´1Γpn{2q2 ?πΓpn ´ 1{2q

1

4?2n ` Opn´2q. Since DL

![image 12](<2021-barg-bounds-sum-distances-spherical_images/imageFile12.png>)

2 ´

“

![image 13](<2021-barg-bounds-sum-distances-spherical_images/imageFile13.png>)

![image 14](<2021-barg-bounds-sum-distances-spherical_images/imageFile14.png>)

![image 15](<2021-barg-bounds-sum-distances-spherical_images/imageFile15.png>)

![image 16](<2021-barg-bounds-sum-distances-spherical_images/imageFile16.png>)

pCNq ě 0, the following bound is immediate: for any code CN Ă Sn´1 τnpCNq ď N2

2

´?

1 4?2n ` Opn´2q¯

![image 17](<2021-barg-bounds-sum-distances-spherical_images/imageFile17.png>)

2 ´

. (4)

![image 18](<2021-barg-bounds-sum-distances-spherical_images/imageFile18.png>)

![image 19](<2021-barg-bounds-sum-distances-spherical_images/imageFile19.png>)

This inequality in effect states a well-known fact that the average of a radial negative-deﬁnite kernel, over a subset of the sphere is at most the average over the entire sphere. It also forms a very particular case of a recent general result in [14, Theorem 3.1].

Remarks

- 1. On account of (3), the problem of maximizing the sum of distances is equivalent to minimizing the quadratic discrepancy, i.e., the sum of distances serves as a proxy for uniformity: a set of N points on the sphere is “more uniform” if the sum of pairwise distances is large for its size.
- 2. Sequences pCNq with average distance ?2p1 ` op1qq are asymptotically uniformly distributed. As we have already pointed out, many sequences of codessatisfy this condition; moreover,as shown below, spherical codes obtained from the binary Kerdock and dual BCH codes match the second term in (4), implying a faster rate of convergence to the limit.

![image 20](<2021-barg-bounds-sum-distances-spherical_images/imageFile20.png>)

- 3. Extensions and generalizations of Stolarsky’s invariance were proposed in recent works [18, 9, 8, 46, 47, 4]. In particular, [4] studied quadratic discrepancy of binary codes, deriving explicit expressions as well as some bounds. Below in Sec. 4, we point out that this problem is closely related to the sum-of-distances problem in the spherical case, and translate our results on bounds to the binary case. This link also motivates


![image 21](<2021-barg-bounds-sum-distances-spherical_images/imageFile21.png>)

1More precisely, the discrepancy is deﬁned as pDL2pCNqq1{2, and it is called the spherical cap discrepancy, as there are also other types of discrepancy on the sphere.

studying the asymptotic regime of n Ñ 8 for spherical codes because this is the only possible asymptotics in the binary space.

- 1.3. Details of our approach. Viewing the distance }x ´ y} as a two-point potential on the sphere, we can relate the problem of estimating τpn,Nq to the search for spherical conﬁgurations with the minimum potential energy. References [37], [17], [11], and many others adopt this point of view, considering the energy minimization for general classes of potential functionson the sphere. A line of works on energyminimization, initiated by Yudin [52, 36] and developed by Cohn and Kumar [24], uses the linear programming bounds on codes to derive results about optimality as well as lower bounds on the energy of spherical codes. Extending the approach of earlier works by Yudin and Levenshtein [39, 41], the authors of [24] proved optimality of several known spherical codes for all absolutely monotone potentials2 and called such codes universally optimal. In particular, denoting t “ tpx,yq “ x ¨ y, we immediately observe that the potential Lptq “


![image 22](<2021-barg-bounds-sum-distances-spherical_images/imageFile22.png>)

´}x ´ y} “ ´a

2p1 ´ tq ﬁts in this scheme since 2 ` Lptq is absolutely monotone, and thus all the known universally optimal codes are maximizers of the sum of distances.

While the results of [24] apply to speciﬁc spherical codes, a suite of universal bounds on the potential energy was derived in recent papers of Boyvalenkov, Dragnev, Hardin, Saff, and Stoyanova [13, 14, 15, 16]. While the bounds can be written in a general form relying on the Levenshtein formalism, explicit expressions are difﬁcult to come by. We derive an explicit form of the ﬁrst few bounds in the Levenshtein hierarchy and evaluate them for the families of spherical codes mentioned above, limiting ourselves to the potential Lptq. Our approach can be summarized as follows. Given an absolutely monotone potential h, deﬁne the minimum h-energy over all spherical sets of size N by

EhpCNq, where EhpCNq “

Ehpn,Nq :“ inf CN

řN i,j“1 hpzi ¨ zjq. This quantity is bounded from below as follows:

k´ÿ1`ε

Ehpn,Nq ě N2

ρihpαiq, (5)

i“0

where the positive integer k, the value ε P t0,1u, and the real parameters pρi,αiq, i “ 0,1,...,k ´ 1 ` ε, are functions of N and n as explained in [14] and in Section 5 below. The bound (5) was called a universal lower bound (ULB) in [14]. For given k and ε we obtain a degree-m bound, m “ 2k ´ 1 ` ε, where the term “degree” refers to the degree of the polynomial used in the corresponding linear programming problem. The bound of degree m applies to the values of code cardinality in the segment D˚pn,mq ď N ă D˚pn,m`1q, where D˚pn,mq :“

`n`k´2`ε

`n`k´2

˘

˘

`

comes from the Delsarte, Goethals and Seidel’s bound [26] for the mimimum possible cardinality of spherical τ-designs on Sn´1. The ﬁrst few segments are as follows:

n´1

n´1

r2,nq, rn ` 1,2nq, r2n,npn ` 3q{2q, rnpn ` 3q{2,npn ` 1qq, rnpn ` 1q,npn2 ` 6n ` 5q{6q.

The results of [14] also imply the optimal choice of the polynomial, so the bounds we obtain cannot be improved by choosing a different polynomial of degree ď m. The bound (5) will be expressed below in terms of n and N for m “ 1, 2, and 3.

Similarly, it is possible to bound the h-energy from above under the condition that the maximum inner product s between distinct vectors in CN is ﬁxed, or, allowing n and N to grow, satisﬁes the condition limsupnÑ8 s ă 1. Note that if n increases then so does N, and the relation between them affects the asymptotic expressions. Consider the quantity

Ehpn,N,sq :“ suptEhpCNq : x ¨ y ď s,x,y P CN,x ‰ yu,

![image 23](<2021-barg-bounds-sum-distances-spherical_images/imageFile23.png>)

2A potential hptq : r´1, 1s Ñ R is called absolutely monotone if for every n ě 0 the derivative hpnqptq exists and is nonnegative for all t.

i.e., the supremum of h-energy of spherical codes of ﬁxed dimension, cardinality, and minimum separation. Universal upper bounds (UUBs) for Ehpn,N,sq were derived in [16]. To this end, the linear programming functional f0|C| ´ fp1q is minimized on the set of polynomials

degÿpfq

!

)

fiPipnqptq : fptq ě hptq,t P r´1,ss;fi ď 0,i ě 1

fptq “

,

i“0

where Pipnqptq are the Gegenbauer polynomials (normalized by Pipnqp1q “ 1). In [16], the authors use a speciﬁc choice of the polynomials fptq for ﬁxed n, N, and s as explained in Section 5. This leads to the

bound

k´ÿ1`ε

Ehpn,N,sq ď ˆ

N N1 ´ 1˙Nfp1q ` N2

ρihpαiq, (6)

![image 24](<2021-barg-bounds-sum-distances-spherical_images/imageFile24.png>)

i“0

where this time the parameters pρi,αiq are functions of the dimension n and the minimum separation s, and N1 “ Lmpn,sq, m “ 2k ´ 1 ` ε, is the corresponding Levenshtein bound (see Sec. 5 for additional details). The bound (6) will be expressed below in terms of n, N, and s for m “ 1, 2, and 3.

While in this paper our focus is on codes of small size, a recent general result in [15] (Theorem 7 and Corollary 1) implies the following asymptotic bound for the sum of distances:

τnpCNq ď

?

N3{2 4?2 p1 ` op1qq,

![image 25](<2021-barg-bounds-sum-distances-spherical_images/imageFile25.png>)

2N2 ´

![image 26](<2021-barg-bounds-sum-distances-spherical_images/imageFile26.png>)

![image 27](<2021-barg-bounds-sum-distances-spherical_images/imageFile27.png>)

which is applicable, in particular, for all N such that D˚pn,2lq ď N ă D˚pn,2l ` 1q,l ě 1.

2. BOUNDS

General boundson energyof spherical codes obtained earlier in [14] and [16] apply to the sum of distances, although obtaining explicit expressions is not immediate. In this section we list the lower and upper bounds on the sum of distances obtained from the general results in the cited works, deferring the proof to Sec. 5. We limit ourselves to the ﬁrst three bounds in the sequence of lower and upper bounds, noting that even in this case, the resulting expressions are unusually cumbersome.

- 2.1. Upper bounds. The following bounds on the maximum sum of distances of a spherical code in n dimensions hold true:


$

- τ1pn,Nq :“ N

a

![image 28](<2021-barg-bounds-sum-distances-spherical_images/imageFile28.png>)

2NpN ´ 1q (7)

- τ2pn,Nq :“

N

´

2NpN ´ n ´ 1q ` pN ´ 2q

a

![image 29](<2021-barg-bounds-sum-distances-spherical_images/imageFile29.png>)

2nNpn ´ 1qpN ´ 2q¯ Nn ` N ´ 4n

![image 30](<2021-barg-bounds-sum-distances-spherical_images/imageFile30.png>)

(8)

- τ3pn,Nq :“ Nd


’&

τpn,Nq ď

![image 31](<2021-barg-bounds-sum-distances-spherical_images/imageFile31.png>)

2NpnA1 ` 2pN ´ n ´ 1q2B1q n2pn ´ 1q2 ` 4npN ´ n ´ 1qpN ´ 2nq

(9)

’%

![image 32](<2021-barg-bounds-sum-distances-spherical_images/imageFile32.png>)

where the ﬁrst bound applies for 2 ď N ď n ` 1, the second for n ` 1 ď N ď 2n, the third for 2n ď N ď npn ` 3q{2, and where

A1 “ Nn3 ` p2N ´ 1qn2 ´ pN ´ 1qp7N ´ 2qn ` pN ´ 1q2p2N ` 3q, (10) B1 “ a

![image 33](<2021-barg-bounds-sum-distances-spherical_images/imageFile33.png>)

npn ´ 1qNpN ´ n ´ 1q. (11)

Bound (7) is attained by the simplex code, bound (8) is attained by the biorthogonal code, and bound (9) is attained by all codes that meet the 3rd Levenshtein bound3 [41, p.620]. Due to (3), these codes have the smallest quadratic discrepancy among all codes of their size. In the asymptotics of n Ñ 8 bounds (7) and (8) yield

- τ1pn,Nq “

?

![image 34](<2021-barg-bounds-sum-distances-spherical_images/imageFile34.png>)

2N2 ´

N ?2 ` Op1q if N „ δn,0 ă δ ď 1, (12)

![image 35](<2021-barg-bounds-sum-distances-spherical_images/imageFile35.png>)

![image 36](<2021-barg-bounds-sum-distances-spherical_images/imageFile36.png>)

- τ2pn,Nq “


?

1 ´ 3δ{2 ?2 ¯

´

![image 37](<2021-barg-bounds-sum-distances-spherical_images/imageFile37.png>)

2N2 ´ 2

1 ´ δ ´

N ` Op1q if N „ δn,1 ď δ ď 2. (13) Note that the bound (13) is slightly tighter than (12) because of a larger second term, which is greater than ?12 for all δ ą 1. The bound (13) is also uniformly better than (4) for all N “ δn,δ P r1,2s.

![image 38](<2021-barg-bounds-sum-distances-spherical_images/imageFile38.png>)

![image 39](<2021-barg-bounds-sum-distances-spherical_images/imageFile39.png>)

![image 40](<2021-barg-bounds-sum-distances-spherical_images/imageFile40.png>)

![image 41](<2021-barg-bounds-sum-distances-spherical_images/imageFile41.png>)

The bound (9) is valid for N ď npn ` 3q{2. Writing N „ δnα, we note that its asymptotic behavior depends on α. For instance, for N “ δn2 we obtain

?2δ 8

?

![image 42](<2021-barg-bounds-sum-distances-spherical_images/imageFile42.png>)

N3{2 ` OpNq. (14)

![image 43](<2021-barg-bounds-sum-distances-spherical_images/imageFile43.png>)

2N2 ´

τ3pn,Nq “

![image 44](<2021-barg-bounds-sum-distances-spherical_images/imageFile44.png>)

Here the order of the second term of the asymptotics coincides with the bound obtained from the average distance (4) while the constant factor is better for all δ ą 1.

- 2.2. Lower bounds. Let CN be a spherical code in n dimensions, and assume that the minimum distance between distinct points zi,zj P CN is bounded from below, i.e., that zi ¨zj ď s for some s P r´1,1q. Denote


τnpCNq the smallest possible sum of distances for such codes. We have

by τnpN,sq “ infC

N

τnpN,sq ěτpiqpn,N,sq,i “ 1,2,3, (15) where the bound

![image 45](<2021-barg-bounds-sum-distances-spherical_images/imageFile45.png>)

τp1qpn,N,sq “ NpN ´ 1qa

2p1 ´ sq, (16) is applicable in (15) for N P r2,n ` 1s and s P r´1{pN ´ 1q,´1{ns, the bound

´

2p1 ´ sq¯ np1 ´ s2q

![image 46](<2021-barg-bounds-sum-distances-spherical_images/imageFile46.png>)

a

2Np1 ´ ns2q ´ 2np1 ´ s2q ` pn ´ 1q

N

τp2qpn,N,sq “

, (17)

![image 47](<2021-barg-bounds-sum-distances-spherical_images/imageFile47.png>)

is applicable for n ` 1 ď N ď 2n and s P ”

ı

N´2n

npN´2q,0

, and the bound

![image 48](<2021-barg-bounds-sum-distances-spherical_images/imageFile48.png>)

¯ ´ 2Np1 ` 2s ` ns2qC4?A6

”

´p1 ´ sqp1 ` nsqA4 ` B4

ı

![image 49](<2021-barg-bounds-sum-distances-spherical_images/imageFile49.png>)

a

![image 50](<2021-barg-bounds-sum-distances-spherical_images/imageFile50.png>)

p1 ´ sqB5

N

A5

τp3qpn,N,sq “

np1 ´ sqp1 ` 2s ` ns2q2C4?2B5

, (18) is applicable for 2n ď N ď npn ` 3q{2 and

![image 51](<2021-barg-bounds-sum-distances-spherical_images/imageFile51.png>)

![image 52](<2021-barg-bounds-sum-distances-spherical_images/imageFile52.png>)

?n ` 3 ´ 1 n ` 2

s P «a

ﬀ, (19)

![image 53](<2021-barg-bounds-sum-distances-spherical_images/imageFile53.png>)

![image 54](<2021-barg-bounds-sum-distances-spherical_images/imageFile54.png>)

n2pn ´ 1q2 ` 4npN ´ n ´ 1qpN ´ 2nq ´ npn ´ 1q 2npN ´ n ´ 1q

,

![image 55](<2021-barg-bounds-sum-distances-spherical_images/imageFile55.png>)

![image 56](<2021-barg-bounds-sum-distances-spherical_images/imageFile56.png>)

![image 57](<2021-barg-bounds-sum-distances-spherical_images/imageFile57.png>)

3All the known codes attaining Levenshtein bounds are listed in [40, Table 9.1]. There are two inﬁnite series of codes as well as three sporadic examples that meet the 3rd bound. Some of these codes, originating from strongly regular graphs, were discovered in [23] which established a condition for them to meet the 3rd Levenshtein bound; see [40] for the details of this connection.

where the notation in (18) is as follows:

- A2 “ p1 ` nsq5p1 ´ sq ` pn ´ 1q2ppn ` 1qs ` 2q,
- B2 “ pn ´ 1qap1 ´ sqp1 ` nsqppn ` 1qs ` 2q


![image 58](<2021-barg-bounds-sum-distances-spherical_images/imageFile58.png>)

- A4 “ npn ` 2qpn ` 3qs4 ` 2p3n2 ` 13n ` 8qs3 ` 2pn2 ` 12n ` 23qs2 ` 2p2n2 ` 5n ` 17qs ` 9n ` 3,
- B4 “ 2pn ´ 1qppn ` 1qs ` 2qppn ´ 2qs2 ´ 2ns ´ 1q,
- C4 “ 2npn ` 2qs3 ´ pn2 ´ 5n ´ 2qs2 ´ 6ns ´ n ´ 5,


- A5 “ Np1 ´ ns2q ´ np1 ´ sqppn ` 1qs ` 2q,
- B5 “


pn ` 1qs ` 2 1 ` ns

,

![image 59](<2021-barg-bounds-sum-distances-spherical_images/imageFile59.png>)

p1 ´ sqpA2 ` 2p1 ` nsq2B2q 1 ` ns

A6 “

.

![image 60](<2021-barg-bounds-sum-distances-spherical_images/imageFile60.png>)

(20) Remarks.

1. Note that expression (16) yields a trivial bound on the sum of distances, assuming that every pair of code points is at distance

![image 61](<2021-barg-bounds-sum-distances-spherical_images/imageFile61.png>)

a

2p1 ´ sq. It is included for completeness because it follows by optimizing the linear polynomial in the linear programming problem.

- 2. The bounds (16)–(18) are proved for s in the speciﬁed intervals above but are valid at least for slightly larger s (by continuity). For example, the bound (16) is valid for all s. The lower limits for s are determined from the inequality N1 ě N and the upper limits are the same as for the Levenshtein bound Lmpn,sq (see in Sec. 5 for more details).
- 3. Using Mathematica, we can compute asymptotic behavior of τp3qpn,N,sq for n Ñ 8. Since it depends on s, we do not include general expressions, leaving this for the examples.


3. EXAMPLES OF CODES OF SMALL SIZE

In this section we consider several families of spherical codes that attain the asymptotic extremum of the sum of distances. We focus on sets with a small number of distinct distances because the sum of distances is easier to compute, and because their cardinalities ﬁt the range of the parameters used to derive the bounds in the previous section. We consider three types of objects, families of equiangular lines, strongly regular graphs, and binary codes. General introductions to their properties are found in [31, Ch.11], [19], and [43], respectively.

- 3.1. Equiangular lines. A family of M equiangular lines in Rn with common inner product s deﬁnes a spherical code CN with N “ 2M vectors, each of which has inner product s with M ´ 1 other vectors and ´s with their opposites. The sum of distances in CN equals


ÿN

?2 ` 2sq ` 2q

?2 ´ 2s `

![image 62](<2021-barg-bounds-sum-distances-spherical_images/imageFile62.png>)

![image 63](<2021-barg-bounds-sum-distances-spherical_images/imageFile63.png>)

}zi ´ zj} “ NppM ´ 1qp

τnpCNq “

i,j“1

?1 ´ s `

?1 ` sq ` OpNq. (21)

N2 ?2p

![image 64](<2021-barg-bounds-sum-distances-spherical_images/imageFile64.png>)

![image 65](<2021-barg-bounds-sum-distances-spherical_images/imageFile65.png>)

“

![image 66](<2021-barg-bounds-sum-distances-spherical_images/imageFile66.png>)

![image 67](<2021-barg-bounds-sum-distances-spherical_images/imageFile67.png>)

?1 ` s “ 2 ´ s

For small s we can write ?1 ´ s `

2

4 ` Ops4q, so for M “ Θpn2q the sum of distances will be close to the value

![image 68](<2021-barg-bounds-sum-distances-spherical_images/imageFile68.png>)

![image 69](<2021-barg-bounds-sum-distances-spherical_images/imageFile69.png>)

![image 70](<2021-barg-bounds-sum-distances-spherical_images/imageFile70.png>)

?2N2 given by the bound (14). Example 1 below illustrates this claim. EXAMPLES.

![image 71](<2021-barg-bounds-sum-distances-spherical_images/imageFile71.png>)

1. Constructions with M “ Θpn2q. There are several constructions of large-size sets of equiangular lines, starting with De Caen’s family [25]; see also [33]. In all these constructions s Ñ 0, and thus the sum

?2N2p1 ` op1qq, showing that such families yield asymptotically optimal spherical codes. For instance, De Caen’s family yields codes CN with the parameters

![image 72](<2021-barg-bounds-sum-distances-spherical_images/imageFile72.png>)

of distances equals τnpCNq “

4 9pn ` 1q2, s “

- 1

![image 73](<2021-barg-bounds-sum-distances-spherical_images/imageFile73.png>)

- 2r ` 1


n “ 3 ¨ 22r´1 ´ 1, N “

, r ě 1, and we ﬁnd from (21) that

![image 74](<2021-barg-bounds-sum-distances-spherical_images/imageFile74.png>)

?

1 4?2

N3{2 ` OpN5{4q.

![image 75](<2021-barg-bounds-sum-distances-spherical_images/imageFile75.png>)

2N2 ´

τnpCNq “

![image 76](<2021-barg-bounds-sum-distances-spherical_images/imageFile76.png>)

![image 77](<2021-barg-bounds-sum-distances-spherical_images/imageFile77.png>)

![image 78](<2021-barg-bounds-sum-distances-spherical_images/imageFile78.png>)

At the same time, on account (14) and (18) any sequence of codes CN with N „ 94n2 and s „ b

3

2n satisﬁes ?

![image 79](<2021-barg-bounds-sum-distances-spherical_images/imageFile79.png>)

![image 80](<2021-barg-bounds-sum-distances-spherical_images/imageFile80.png>)

?

1 5?2

1 6?2

N7{4 ´ OpN3{2q ď τnpCNq ď

N3{2 ` OpNq

![image 81](<2021-barg-bounds-sum-distances-spherical_images/imageFile81.png>)

![image 82](<2021-barg-bounds-sum-distances-spherical_images/imageFile82.png>)

2N2 ´

2N2 ´

![image 83](<2021-barg-bounds-sum-distances-spherical_images/imageFile83.png>)

![image 84](<2021-barg-bounds-sum-distances-spherical_images/imageFile84.png>)

![image 85](<2021-barg-bounds-sum-distances-spherical_images/imageFile85.png>)

![image 86](<2021-barg-bounds-sum-distances-spherical_images/imageFile86.png>)

(computations for the lower bound performed with Mathematica). We give examples of the bounds on the sum of distances of de Caen’s codes and of its true value for the ﬁrst few values of r.

![image 87](<2021-barg-bounds-sum-distances-spherical_images/imageFile87.png>)

r n N Upper bound τ3pn, Nq τnpCNq Lower bound τp3qpn, N, sq

![image 88](<2021-barg-bounds-sum-distances-spherical_images/imageFile88.png>)

![image 89](<2021-barg-bounds-sum-distances-spherical_images/imageFile89.png>)

![image 90](<2021-barg-bounds-sum-distances-spherical_images/imageFile90.png>)

![image 91](<2021-barg-bounds-sum-distances-spherical_images/imageFile91.png>)

![image 92](<2021-barg-bounds-sum-distances-spherical_images/imageFile92.png>)

![image 93](<2021-barg-bounds-sum-distances-spherical_images/imageFile93.png>)

![image 94](<2021-barg-bounds-sum-distances-spherical_images/imageFile94.png>)

![image 95](<2021-barg-bounds-sum-distances-spherical_images/imageFile95.png>)

- 3 95 4096 2.369344 ¨ 107 2.368643 ¨ 107 2.341901 ¨ 107

![image 96](<2021-barg-bounds-sum-distances-spherical_images/imageFile96.png>)

![image 97](<2021-barg-bounds-sum-distances-spherical_images/imageFile97.png>)

![image 98](<2021-barg-bounds-sum-distances-spherical_images/imageFile98.png>)

![image 99](<2021-barg-bounds-sum-distances-spherical_images/imageFile99.png>)

![image 100](<2021-barg-bounds-sum-distances-spherical_images/imageFile100.png>)

![image 101](<2021-barg-bounds-sum-distances-spherical_images/imageFile101.png>)

![image 102](<2021-barg-bounds-sum-distances-spherical_images/imageFile102.png>)

![image 103](<2021-barg-bounds-sum-distances-spherical_images/imageFile103.png>)

- 4 383 65536 6.0719880 ¨ 109 6.071317 ¨ 109 6.036098 ¨ 109

![image 104](<2021-barg-bounds-sum-distances-spherical_images/imageFile104.png>)

![image 105](<2021-barg-bounds-sum-distances-spherical_images/imageFile105.png>)

![image 106](<2021-barg-bounds-sum-distances-spherical_images/imageFile106.png>)

![image 107](<2021-barg-bounds-sum-distances-spherical_images/imageFile107.png>)

![image 108](<2021-barg-bounds-sum-distances-spherical_images/imageFile108.png>)

![image 109](<2021-barg-bounds-sum-distances-spherical_images/imageFile109.png>)

![image 110](<2021-barg-bounds-sum-distances-spherical_images/imageFile110.png>)

![image 111](<2021-barg-bounds-sum-distances-spherical_images/imageFile111.png>)

- 5 1535 1048576 1.5548171 ¨ 1012 1.554765 ¨ 1012 1.550113 ¨ 1012

![image 112](<2021-barg-bounds-sum-distances-spherical_images/imageFile112.png>)

![image 113](<2021-barg-bounds-sum-distances-spherical_images/imageFile113.png>)

![image 114](<2021-barg-bounds-sum-distances-spherical_images/imageFile114.png>)

![image 115](<2021-barg-bounds-sum-distances-spherical_images/imageFile115.png>)

![image 116](<2021-barg-bounds-sum-distances-spherical_images/imageFile116.png>)

![image 117](<2021-barg-bounds-sum-distances-spherical_images/imageFile117.png>)

![image 118](<2021-barg-bounds-sum-distances-spherical_images/imageFile118.png>)

![image 119](<2021-barg-bounds-sum-distances-spherical_images/imageFile119.png>)

- 6 6143 16777216 3.9805762.1014 3.980539 ¨ 1014 3.974463 ¨ 1014

![image 120](<2021-barg-bounds-sum-distances-spherical_images/imageFile120.png>)

![image 121](<2021-barg-bounds-sum-distances-spherical_images/imageFile121.png>)

![image 122](<2021-barg-bounds-sum-distances-spherical_images/imageFile122.png>)

![image 123](<2021-barg-bounds-sum-distances-spherical_images/imageFile123.png>)

![image 124](<2021-barg-bounds-sum-distances-spherical_images/imageFile124.png>)

![image 125](<2021-barg-bounds-sum-distances-spherical_images/imageFile125.png>)

![image 126](<2021-barg-bounds-sum-distances-spherical_images/imageFile126.png>)

![image 127](<2021-barg-bounds-sum-distances-spherical_images/imageFile127.png>)

- 7 24575 268435456 1.0190430 ¨ 1017 1.019041 ¨ 1017 1.018254 ¨ 1017


![image 128](<2021-barg-bounds-sum-distances-spherical_images/imageFile128.png>)

![image 129](<2021-barg-bounds-sum-distances-spherical_images/imageFile129.png>)

![image 130](<2021-barg-bounds-sum-distances-spherical_images/imageFile130.png>)

![image 131](<2021-barg-bounds-sum-distances-spherical_images/imageFile131.png>)

![image 132](<2021-barg-bounds-sum-distances-spherical_images/imageFile132.png>)

![image 133](<2021-barg-bounds-sum-distances-spherical_images/imageFile133.png>)

![image 134](<2021-barg-bounds-sum-distances-spherical_images/imageFile134.png>)

![image 135](<2021-barg-bounds-sum-distances-spherical_images/imageFile135.png>)

2. Below by Mspnq we denote the maximum number of equiangular lines in n dimensions with inner product s. It is known [38] that M1{3pnq “ 2pn ´ 1q. Taking N “ 4pn ´ 1q for a given n, we obtain a spherical code CN with sum of distances equal to

- ?2

![image 136](<2021-barg-bounds-sum-distances-spherical_images/imageFile136.png>)

![image 137](<2021-barg-bounds-sum-distances-spherical_images/imageFile137.png>)

- ?3 p1 ` op1qq.


1 `

![image 138](<2021-barg-bounds-sum-distances-spherical_images/imageFile138.png>)

![image 139](<2021-barg-bounds-sum-distances-spherical_images/imageFile139.png>)

4{3 ` a

τnpCNq “ NppM ´ 1qpa

8{3q ` 2q “ N2

![image 140](<2021-barg-bounds-sum-distances-spherical_images/imageFile140.png>)

The constant factor in this expression is approximately 1.39. A more detailed calculation shows that lim

?

?

τnpCNq τ3pn,Nq

2 ´ 1qq´1 « 0.9856.

![image 141](<2021-barg-bounds-sum-distances-spherical_images/imageFile141.png>)

![image 142](<2021-barg-bounds-sum-distances-spherical_images/imageFile142.png>)

6p

“ p

![image 143](<2021-barg-bounds-sum-distances-spherical_images/imageFile143.png>)

nÑ8

3. Further, by [44], M1{5pnq “ t3pn´1q{2u for all sufﬁciently large n. This set of lines yields a spherical code with sum of distances τnpCNq “ N2pp

?2`

?5qp1`op1qq « 1.407N2, which is again very close to (14). It is not difﬁcult to check that

?3q{

![image 144](<2021-barg-bounds-sum-distances-spherical_images/imageFile144.png>)

![image 145](<2021-barg-bounds-sum-distances-spherical_images/imageFile145.png>)

![image 146](<2021-barg-bounds-sum-distances-spherical_images/imageFile146.png>)

?

?

“ ´?

τnpCNq τ3pn,Nq

¯{

![image 147](<2021-barg-bounds-sum-distances-spherical_images/imageFile147.png>)

![image 148](<2021-barg-bounds-sum-distances-spherical_images/imageFile148.png>)

![image 149](<2021-barg-bounds-sum-distances-spherical_images/imageFile149.png>)

2 `

10 « 0.9949.

lim

3

![image 150](<2021-barg-bounds-sum-distances-spherical_images/imageFile150.png>)

nÑ8

4. A recent paper by Jiang and Polyanskii [34] shows that M1{p1`2?2qpnq “ 3n{2 ` Op1q, yielding a spherical code of size N “ 3n ` Op1q. For this code, the constant factor in (21) equals

![image 151](<2021-barg-bounds-sum-distances-spherical_images/imageFile151.png>)

![image 152](<2021-barg-bounds-sum-distances-spherical_images/imageFile152.png>)

![image 153](<2021-barg-bounds-sum-distances-spherical_images/imageFile153.png>)

d1 ´

1 1 ` 2?2 ` d1 `

1

1 ?2´

1 ` 2?2¯ « 1.40189. In the limit of n Ñ 8, the sum of distances satisﬁes τnpCNq{τ3pn,Nq Ñ 0.991.

![image 154](<2021-barg-bounds-sum-distances-spherical_images/imageFile154.png>)

![image 155](<2021-barg-bounds-sum-distances-spherical_images/imageFile155.png>)

![image 156](<2021-barg-bounds-sum-distances-spherical_images/imageFile156.png>)

![image 157](<2021-barg-bounds-sum-distances-spherical_images/imageFile157.png>)

![image 158](<2021-barg-bounds-sum-distances-spherical_images/imageFile158.png>)

![image 159](<2021-barg-bounds-sum-distances-spherical_images/imageFile159.png>)

More examples can be generated relying on constructions of equiangular line sets of size Opn3{2q based on Taylor graphs and projective planes [38]. Recent additions to the literature include new upper bounds and exact asymptotics of the size of equiangular line sets with ﬁxed inner product s [2, 30, 35].

- 3.2. Strongly regular graphs and tight frames. Here we consider the sum-of-distances function for spherical codes obtained from strongly regular graphs (SRG). A k-regular graph on v vertices is strongly regular if every pair of adjacent vertices has a common neighbors and every pair of nonadjacent vertices has c common neighbors. Below we use the notation SRGpv,k,a,cq when we need to mention the parameters explicitly.


The spectral structure of SRGs is well known; see for instance [21, p. 118], [23], or [28, Sec. 9.4] (the last two references highlight the relation between spherical codes and SRGs and more generally, association schemes). The adjacency matrix of an SRG has three eigenspaces that correspond to the eigenvalues k,r1,r2. Let ∆ “ pa ´ cq2 ` 4pk ´ cq, then the eigenvalues other than k have the form

?

?

- 1

![image 160](<2021-barg-bounds-sum-distances-spherical_images/imageFile160.png>)

- 2pa ´ c `


- 1

![image 161](<2021-barg-bounds-sum-distances-spherical_images/imageFile161.png>)

- 2pa ´ c ´


![image 162](<2021-barg-bounds-sum-distances-spherical_images/imageFile162.png>)

![image 163](<2021-barg-bounds-sum-distances-spherical_images/imageFile163.png>)

r1 “

∆q, and the dimensions of the corresponding eigenspaces are

∆q, r2 “

pv ´ 1qpc ´ aq ´ 2k ?∆ ¯

- 1

![image 164](<2021-barg-bounds-sum-distances-spherical_images/imageFile164.png>)

- 2´


n1,2 “

v ´ 1 ˘

, (22) where we write n1,2 to refer to both eigenspaces at the same time.

![image 165](<2021-barg-bounds-sum-distances-spherical_images/imageFile165.png>)

![image 166](<2021-barg-bounds-sum-distances-spherical_images/imageFile166.png>)

Spherical embeddings of SRGs were introduced by Delsarte, Goethals, and Seidel [26], Example 9.1. To obtain a spherical code from an SRG, assign vectors of the standard basis of Rv to the vertices, and then project the basis on an eigenspace of the graph. In particular, using the eigenspace Wr

that corresponds to r1, we obtain a spherical code in Rn1

1

with N “ v points and inner products s1 “

1 ` r1 v ´ 1 ´ k

r1 k

, s2 “ ´

. (23) A similar procedure for r2 yields a spherical code in Rn2

![image 167](<2021-barg-bounds-sum-distances-spherical_images/imageFile167.png>)

![image 168](<2021-barg-bounds-sum-distances-spherical_images/imageFile168.png>)

with v points and inner products s1 “ ´

1 ` r2 v ´ 1 ´ k

r2 k

, s2 “

, (24) where in both cases s1 ě 0 ą s2. We again reference [28, Sec. 9.4] for the details and [3] for a short proof.

![image 169](<2021-barg-bounds-sum-distances-spherical_images/imageFile169.png>)

![image 170](<2021-barg-bounds-sum-distances-spherical_images/imageFile170.png>)

The distribution of distances in the obtained spherical codes does not depend on the point zi P CN. If the code is obtained by projecting on Wr

, then the number of neighbors of a point with inner product r1{k is k, and if it is obtained by projecting on Wr

1

, then the number of neighbors of a point with inner product r2{k is k. Thus, in both cases, the number of neighbors with the remaining value of the inner product is N ´ k ´ 1.

2

Combining (22), (23), and (24), we obtain

- Proposition 3.1. Projecting an SRGpv,k,a,cq on the eigenspace Wθ,θ “ r1,r2 results in a spherical code


in Rn1,2

of size N “ v whose sum of distances equals τn

2pN ´ 1 ´ kqpN ` θ ´ kq¯

´a

![image 171](<2021-barg-bounds-sum-distances-spherical_images/imageFile171.png>)

![image 172](<2021-barg-bounds-sum-distances-spherical_images/imageFile172.png>)

2kpk ´ θq ` a

pCNq “ N

, (25) where θ “ r1 or r2 as appropriate.

1,2

Remark: Families of spherical codes considered below attain sums of distances that can be written in the form τnpCNq “

?2N2p1 ` op1qq. A sufﬁcient condition for this is that the eigenvalues are small compared to N, as can be seen upon rewriting (25) in the form

![image 173](<2021-barg-bounds-sum-distances-spherical_images/imageFile173.png>)

![image 174](<2021-barg-bounds-sum-distances-spherical_images/imageFile174.png>)

![image 175](<2021-barg-bounds-sum-distances-spherical_images/imageFile175.png>)

c

kpk ´ θq N2 ` cpN ´ k ´ 1qpN ´ k ` θq N2 ¯

?

´

![image 176](<2021-barg-bounds-sum-distances-spherical_images/imageFile176.png>)

2N2

ipCNq “

τn

.

![image 177](<2021-barg-bounds-sum-distances-spherical_images/imageFile177.png>)

![image 178](<2021-barg-bounds-sum-distances-spherical_images/imageFile178.png>)

- As long as θ{N “ opNq, as is the case in the examples below, the main term of the asymptotic expression will be ?2N2.


![image 179](<2021-barg-bounds-sum-distances-spherical_images/imageFile179.png>)

or Rn2

Spherical codes obtained from SRGs have an additional property of forming tight frames for Rn1

. Recall that a spherical code CN “ tz1,...,zNu forms a tight frame for Rd if

řN i“1px ¨ ziq2 “ A}x}2 for any

x P Rn, where A is a constant. A necessary and sufﬁcient condition for the tight frame property to hold is the equality [7]

ÿN

N2 n

pzi ¨ zjq2 “

. (26)

![image 180](<2021-barg-bounds-sum-distances-spherical_images/imageFile180.png>)

i,j“1

In the frame theory literature the sum on the left-hand side of (26) is called the frame potential [50].

It turns out that all two-distance tight frames are obtained as spherical embeddings of SRGs [5, 49]. EXAMPLES.

The families of graphs considered below are taken from the online database [20].

1. Graph of points on a quadric in PGp2m,qq. The parameters of the SRG are

qpq2m´2 ´ 1q q ´ 1

q2pq2m´4 ´ 1q q ´ 1 ` q ´ 1, c “

q2m´2 ´ 1 q ´ 1

q2m ´ 1 q ´ 1

, k “

, a “

v “

,

![image 181](<2021-barg-bounds-sum-distances-spherical_images/imageFile181.png>)

![image 182](<2021-barg-bounds-sum-distances-spherical_images/imageFile182.png>)

![image 183](<2021-barg-bounds-sum-distances-spherical_images/imageFile183.png>)

![image 184](<2021-barg-bounds-sum-distances-spherical_images/imageFile184.png>)

and the eigenvalues are r1,2 “ ˘qm´1 ´ 1. Spherical embeddings of this graph give tight frames in dimensions (22)

?

- 1

![image 185](<2021-barg-bounds-sum-distances-spherical_images/imageFile185.png>)

- 2pN ´ 1 ˘ qmq «


- 1

![image 186](<2021-barg-bounds-sum-distances-spherical_images/imageFile186.png>)

- 2pN ˘


![image 187](<2021-barg-bounds-sum-distances-spherical_images/imageFile187.png>)

n1,2 “

Nq, which is easily seen since

?∆ “ 2qm´1. The size of the code CN “ CNpr1q is N “ v and the sum of distances is computed from (25) and equals

![image 188](<2021-barg-bounds-sum-distances-spherical_images/imageFile188.png>)

2pqm ` 1q”qm´1 ´ 1 q ´ 1 a

ı

3m´2 2

![image 189](<2021-barg-bounds-sum-distances-spherical_images/imageFile189.png>)

![image 190](<2021-barg-bounds-sum-distances-spherical_images/imageFile190.png>)

a

qpqm´1 ` 1q ` q

1pCNq “ N

. Taking m Ñ 8, we compute

τn

![image 191](<2021-barg-bounds-sum-distances-spherical_images/imageFile191.png>)

![image 192](<2021-barg-bounds-sum-distances-spherical_images/imageFile192.png>)

?

5 4?2

![image 193](<2021-barg-bounds-sum-distances-spherical_images/imageFile193.png>)

2N2 ´

1pCNq “

N ` Op1q. (27)

τn

![image 194](<2021-barg-bounds-sum-distances-spherical_images/imageFile194.png>)

![image 195](<2021-barg-bounds-sum-distances-spherical_images/imageFile195.png>)

Since in this case N « 2n1 ´ 2?2n1, the appropriate bound to look at is τ2pn,Nq with δ “ 2. The second term of the sum of distances in (27) is approximately ´0.884N while the second term in (13) is ´2p

![image 196](<2021-barg-bounds-sum-distances-spherical_images/imageFile196.png>)

?2 ´ 1qN « ´0.828N. Likewise, the projection on the eigenspace Wr

![image 197](<2021-barg-bounds-sum-distances-spherical_images/imageFile197.png>)

gives a spherical code CN “ CNpr2q whose sum of distances equals

2

2pqm ´ 1q”qm´1 ` 1 q ´ 1 a

ı

3m´2 2

![image 198](<2021-barg-bounds-sum-distances-spherical_images/imageFile198.png>)

![image 199](<2021-barg-bounds-sum-distances-spherical_images/imageFile199.png>)

a

qpqm´1 ´ 1q ` q

2pCNq “ N

τn

.

![image 200](<2021-barg-bounds-sum-distances-spherical_images/imageFile200.png>)

![image 201](<2021-barg-bounds-sum-distances-spherical_images/imageFile201.png>)

For large m this behaves as ?2N2 ´ 4?52N `Op1q, exhibiting similar behavior as the code in dimension n1.

![image 202](<2021-barg-bounds-sum-distances-spherical_images/imageFile202.png>)

![image 203](<2021-barg-bounds-sum-distances-spherical_images/imageFile203.png>)

![image 204](<2021-barg-bounds-sum-distances-spherical_images/imageFile204.png>)

2. Graph of points on a hyperbolic quadric in PGp2m ´ 1,qq. The parameters of the SRG are

q2m´1 ´ 1 q ´ 1 ` qm´1, k “

qpq2m´3 ´ 1q q ´ 1 ` qm´1, a “ k ´ q2m´3 ´ 1, c “ k{q, (28)

v “

![image 205](<2021-barg-bounds-sum-distances-spherical_images/imageFile205.png>)

![image 206](<2021-barg-bounds-sum-distances-spherical_images/imageFile206.png>)

and the eigenvalues are r1 “ qm´1 ´ 1 and r2 “ ´qm´2 ´ 1. Using (28), we obtain that the dimensions of the spherical embeddings of this graph are

q2pq2m´2 ´ 1q q2 ´ 1

qpqm´2 ` 1qpqm ´ 1q q2 ´ 1

, n2 “

n1 “

![image 207](<2021-barg-bounds-sum-distances-spherical_images/imageFile207.png>)

![image 208](<2021-barg-bounds-sum-distances-spherical_images/imageFile208.png>)

and thus, n1 « N{pq ` 1q,n2 « Nq{pq ` 1q. The sum of distances in CNpr1q is found to be

2qpqm´1 ` 1q”qm´1 ´ 1 q ´ 1 a

ı

3m

![image 209](<2021-barg-bounds-sum-distances-spherical_images/imageFile209.png>)

![image 210](<2021-barg-bounds-sum-distances-spherical_images/imageFile210.png>)

a

2 ´2

qm´2 ` 1 ` q

1pCNq “ N

τn

.

![image 211](<2021-barg-bounds-sum-distances-spherical_images/imageFile211.png>)

![image 212](<2021-barg-bounds-sum-distances-spherical_images/imageFile212.png>)

?2N2 ´ 4q?`42N ´ Op1q. At the same time, from the bound (9) we obtain an upper estimate of the form ?2N2 ´ OpNq, giving the second term of the same order, although with a smaller constant factor.

![image 213](<2021-barg-bounds-sum-distances-spherical_images/imageFile213.png>)

1pCNq “

For large m we obtain τn

![image 214](<2021-barg-bounds-sum-distances-spherical_images/imageFile214.png>)

![image 215](<2021-barg-bounds-sum-distances-spherical_images/imageFile215.png>)

![image 216](<2021-barg-bounds-sum-distances-spherical_images/imageFile216.png>)

, we ﬁnd that

Turning to the code CN obtained by projecting on the eigenspace Wr

2

2pqm ´ 1q”qm´2 ` 1 q ´ 1 a

ı

3m

![image 217](<2021-barg-bounds-sum-distances-spherical_images/imageFile217.png>)

![image 218](<2021-barg-bounds-sum-distances-spherical_images/imageFile218.png>)

a

2 ´2

qpqm´1 ´ 1q ` q

2pCNq “ N

τn

,

![image 219](<2021-barg-bounds-sum-distances-spherical_images/imageFile219.png>)

![image 220](<2021-barg-bounds-sum-distances-spherical_images/imageFile220.png>)

?2N2´ 44qq?´12N ´Op1q, with similar conclusions in regards to asymptotics of the upper bound.

![image 221](<2021-barg-bounds-sum-distances-spherical_images/imageFile221.png>)

2pCNq “

yielding τn

![image 222](<2021-barg-bounds-sum-distances-spherical_images/imageFile222.png>)

![image 223](<2021-barg-bounds-sum-distances-spherical_images/imageFile223.png>)

Remark: It is known [7] that N2{n is the smallest value of the frame potential in over all pn,Nq spherical codes. Thus, two-distance tight frames form spherical codes in Rn that have asymptotically maximum sum of distances while also minimizing the frame potential.

- 3.3. Spherical embeddings of binary codes. Inﬁnite sequences of asymptotically optimal spherical codes can be obtained by spherical embeddings of binary codes. Let CN Ă Xn “ t0,1un be a binary code of


length n and cardinality N, and denote by Aw “ N1 #ta,b P C : dHpa,bq “ wu the average number of neighbors of a code vector at Hamming distance w. The pn ` 1q-tuple pA0 “ 1,A1,...,Anq is called the distance distribution of the code CN. For a vector z P Xn denote by z˜ the n-dimensional real vector given by z˜i “ p´1qz

![image 224](<2021-barg-bounds-sum-distances-spherical_images/imageFile224.png>)

?n,i “ 1,...,n, and let C˜N Ă Sn´1 be the spherical embedding of the code CN. Since }x˜ ´ y˜} “ 2

![image 225](<2021-barg-bounds-sum-distances-spherical_images/imageFile225.png>)

{

i

dHpx,yq{n, the sum of distances in C˜N can be written as ÿN

![image 226](<2021-barg-bounds-sum-distances-spherical_images/imageFile226.png>)

a

ÿn

Aw?w. (29)

2N ?n

![image 227](<2021-barg-bounds-sum-distances-spherical_images/imageFile227.png>)

}z˜i ´ z˜j} “

![image 228](<2021-barg-bounds-sum-distances-spherical_images/imageFile228.png>)

![image 229](<2021-barg-bounds-sum-distances-spherical_images/imageFile229.png>)

w“0

i,j“1

Using this correspondence, we give several examples of asymptotically optimal families of spherical codes.

- 3.3.1. Sidelnikov codes. In [45, Thm. 7], Sidelnikov constructed a class of binary linear codes Cr,r ě 1 with


4r´1

the parameters n “ 2

2r`1 , N “ 24r. The distance distribution of the codes has two nonzero components (in addition to A0 “ 1):

![image 230](<2021-barg-bounds-sum-distances-spherical_images/imageFile230.png>)

- w1 “

24r´1 ´ 22r´1 2r ` 1

![image 231](<2021-barg-bounds-sum-distances-spherical_images/imageFile231.png>)

, Aw

1 “ 24r ´ n ´ 1,

- w2 “


24r´1 ` 23r´1 2r ` 1

2 “ n. Let us compute the sum of distances of the spherically embedded Sidelnikov codes. Using (29), we obtain

, Aw

![image 232](<2021-barg-bounds-sum-distances-spherical_images/imageFile232.png>)

?

?w2qq “

?w1 ` Aw

1 8

7 16

13 128

2N ?npAw

´

¯ ` OpN1{2q.

N5{4 ´

N3{4

![image 233](<2021-barg-bounds-sum-distances-spherical_images/imageFile233.png>)

N2 ´

N ´

![image 234](<2021-barg-bounds-sum-distances-spherical_images/imageFile234.png>)

![image 235](<2021-barg-bounds-sum-distances-spherical_images/imageFile235.png>)

2

![image 236](<2021-barg-bounds-sum-distances-spherical_images/imageFile236.png>)

![image 237](<2021-barg-bounds-sum-distances-spherical_images/imageFile237.png>)

![image 238](<2021-barg-bounds-sum-distances-spherical_images/imageFile238.png>)

![image 239](<2021-barg-bounds-sum-distances-spherical_images/imageFile239.png>)

2

1

![image 240](<2021-barg-bounds-sum-distances-spherical_images/imageFile240.png>)

- At the same time, the bounds (14) and (9) imply that for any sequence of codes CN with N as above and s “ 1 ´ 2w1{n


?

?

1 8

- 1

![image 241](<2021-barg-bounds-sum-distances-spherical_images/imageFile241.png>)

- 2?2


7 16

5 128

´

¯ ` OpN1{2q,

N5{4 ´

N3{4

N7{4 ´ OpN11{8q ď τnpCNq ď

![image 242](<2021-barg-bounds-sum-distances-spherical_images/imageFile242.png>)

![image 243](<2021-barg-bounds-sum-distances-spherical_images/imageFile243.png>)

N2 ´

2N2 ´

N ´

2

![image 244](<2021-barg-bounds-sum-distances-spherical_images/imageFile244.png>)

![image 245](<2021-barg-bounds-sum-distances-spherical_images/imageFile245.png>)

![image 246](<2021-barg-bounds-sum-distances-spherical_images/imageFile246.png>)

![image 247](<2021-barg-bounds-sum-distances-spherical_images/imageFile247.png>)

and so as r Ñ 8 the true value agrees with the upper bound in the ﬁrst three terms. The ﬁrst few values of the sum of distances together with the bounds of Sec. 2 are shown in the table below.

![image 248](<2021-barg-bounds-sum-distances-spherical_images/imageFile248.png>)

r n N Upper bound τ3pn, Nq τnpCNq Lower bound τp3qpn, N, sq

![image 249](<2021-barg-bounds-sum-distances-spherical_images/imageFile249.png>)

![image 250](<2021-barg-bounds-sum-distances-spherical_images/imageFile250.png>)

![image 251](<2021-barg-bounds-sum-distances-spherical_images/imageFile251.png>)

![image 252](<2021-barg-bounds-sum-distances-spherical_images/imageFile252.png>)

![image 253](<2021-barg-bounds-sum-distances-spherical_images/imageFile253.png>)

![image 254](<2021-barg-bounds-sum-distances-spherical_images/imageFile254.png>)

![image 255](<2021-barg-bounds-sum-distances-spherical_images/imageFile255.png>)

![image 256](<2021-barg-bounds-sum-distances-spherical_images/imageFile256.png>)

![image 257](<2021-barg-bounds-sum-distances-spherical_images/imageFile257.png>)

- 1 5 16 345.4941208 345.4941208 345.4941208

![image 258](<2021-barg-bounds-sum-distances-spherical_images/imageFile258.png>)

![image 259](<2021-barg-bounds-sum-distances-spherical_images/imageFile259.png>)

![image 260](<2021-barg-bounds-sum-distances-spherical_images/imageFile260.png>)

![image 261](<2021-barg-bounds-sum-distances-spherical_images/imageFile261.png>)

![image 262](<2021-barg-bounds-sum-distances-spherical_images/imageFile262.png>)

![image 263](<2021-barg-bounds-sum-distances-spherical_images/imageFile263.png>)

![image 264](<2021-barg-bounds-sum-distances-spherical_images/imageFile264.png>)

![image 265](<2021-barg-bounds-sum-distances-spherical_images/imageFile265.png>)

- 2 51 256 92338.0198 92334.5230 91959.9016

![image 266](<2021-barg-bounds-sum-distances-spherical_images/imageFile266.png>)

![image 267](<2021-barg-bounds-sum-distances-spherical_images/imageFile267.png>)

![image 268](<2021-barg-bounds-sum-distances-spherical_images/imageFile268.png>)

![image 269](<2021-barg-bounds-sum-distances-spherical_images/imageFile269.png>)

![image 270](<2021-barg-bounds-sum-distances-spherical_images/imageFile270.png>)

![image 271](<2021-barg-bounds-sum-distances-spherical_images/imageFile271.png>)

![image 272](<2021-barg-bounds-sum-distances-spherical_images/imageFile272.png>)

![image 273](<2021-barg-bounds-sum-distances-spherical_images/imageFile273.png>)

- 3 455 4096 2.371820900 ¨ 107 2.371817158 ¨ 107 2.369984979 ¨ 107

![image 274](<2021-barg-bounds-sum-distances-spherical_images/imageFile274.png>)

![image 275](<2021-barg-bounds-sum-distances-spherical_images/imageFile275.png>)

![image 276](<2021-barg-bounds-sum-distances-spherical_images/imageFile276.png>)

![image 277](<2021-barg-bounds-sum-distances-spherical_images/imageFile277.png>)

![image 278](<2021-barg-bounds-sum-distances-spherical_images/imageFile278.png>)

![image 279](<2021-barg-bounds-sum-distances-spherical_images/imageFile279.png>)

![image 280](<2021-barg-bounds-sum-distances-spherical_images/imageFile280.png>)

![image 281](<2021-barg-bounds-sum-distances-spherical_images/imageFile281.png>)

- 4 3855 65536 6.0737748 ¨ 109 6.0737745 ¨ 109 6.073097678 ¨ 109

![image 282](<2021-barg-bounds-sum-distances-spherical_images/imageFile282.png>)

![image 283](<2021-barg-bounds-sum-distances-spherical_images/imageFile283.png>)

![image 284](<2021-barg-bounds-sum-distances-spherical_images/imageFile284.png>)

![image 285](<2021-barg-bounds-sum-distances-spherical_images/imageFile285.png>)

![image 286](<2021-barg-bounds-sum-distances-spherical_images/imageFile286.png>)

![image 287](<2021-barg-bounds-sum-distances-spherical_images/imageFile287.png>)

![image 288](<2021-barg-bounds-sum-distances-spherical_images/imageFile288.png>)

![image 289](<2021-barg-bounds-sum-distances-spherical_images/imageFile289.png>)

- 5 31775 1048576 1.554937673 ¨ 1012 1.554937671 ¨ 1012 1.554914842 ¨ 1012


![image 290](<2021-barg-bounds-sum-distances-spherical_images/imageFile290.png>)

![image 291](<2021-barg-bounds-sum-distances-spherical_images/imageFile291.png>)

![image 292](<2021-barg-bounds-sum-distances-spherical_images/imageFile292.png>)

![image 293](<2021-barg-bounds-sum-distances-spherical_images/imageFile293.png>)

![image 294](<2021-barg-bounds-sum-distances-spherical_images/imageFile294.png>)

![image 295](<2021-barg-bounds-sum-distances-spherical_images/imageFile295.png>)

![image 296](<2021-barg-bounds-sum-distances-spherical_images/imageFile296.png>)

The relative difference between the upper bound and the true value for r “ 5 is about 10´9, and the upper and lower bounds on the sum of distances are also rather close.

We next discuss some families of spherical codes obtained from binary codes of cardinality N « n2 that share the following common property: they have a small number of nonzero distances concentrated around n{2. Since the factor ?w «

an

![image 297](<2021-barg-bounds-sum-distances-spherical_images/imageFile297.png>)

![image 298](<2021-barg-bounds-sum-distances-spherical_images/imageFile298.png>)

2 for large n can be taken outside the sum in (29), and since the nonzero coefﬁcients Aw add to N ´ 1, all such families satisfy

![image 299](<2021-barg-bounds-sum-distances-spherical_images/imageFile299.png>)

?

![image 300](<2021-barg-bounds-sum-distances-spherical_images/imageFile300.png>)

2N2p1 ` op1qq, differing only in the lower terms of the asymptotics.

τnpCNq „

- 3.3.2. Kerdock codes. [43, §15.5]. Binary Kerdock codes form a family of nonlinear codes of length n “ 22m,m ě 2 and cardinality N “ n2. The distribution of Hamming distances does not depend on the code point and the nonzero entries pAiq are as follows:

A0 “ An “ 1,Apn˘?nq{2 “ npn{2 ´ 1q,An{2 “ 2pn ´ 1q. From (29), the sum of distances of the spherical Kerdock code equals

![image 301](<2021-barg-bounds-sum-distances-spherical_images/imageFile301.png>)

τnpC˜Nq “

?

![image 302](<2021-barg-bounds-sum-distances-spherical_images/imageFile302.png>)

2N2 ´

1 4?2

![image 303](<2021-barg-bounds-sum-distances-spherical_images/imageFile303.png>)

![image 304](<2021-barg-bounds-sum-distances-spherical_images/imageFile304.png>)

N3{2 ` OpNq,

which agrees with the bound (4), (14). Note that for general completely monotone potentials, the ﬁrst-term optimality of the Kerdock codes was previously observed in [13].

- 3.3.3. Dual BCH codes. [43, §15.4]. Let CN be a linear binary BCH code of length n “ 2r ´ 1, r ě 3 with minimum distance 5. Suppose that r is odd. Then the dual code pCNqK has cardinality N “ 22r and distance distribution A0 “ 1 and


?n ` 1 2?2 ¯

![image 305](<2021-barg-bounds-sum-distances-spherical_images/imageFile305.png>)

´n ` 1 4 ¯

npn ` 3q 2

?

“ n

“

, An`1

An`1

. For r even the dual BCH code of length 2r ´ 1 has distance distribution A0 “ 1 and

![image 306](<2021-barg-bounds-sum-distances-spherical_images/imageFile306.png>)

![image 307](<2021-barg-bounds-sum-distances-spherical_images/imageFile307.png>)

![image 308](<2021-barg-bounds-sum-distances-spherical_images/imageFile308.png>)

![image 309](<2021-barg-bounds-sum-distances-spherical_images/imageFile309.png>)

n`1 2

2 ˘

![image 310](<2021-barg-bounds-sum-distances-spherical_images/imageFile310.png>)

![image 311](<2021-barg-bounds-sum-distances-spherical_images/imageFile311.png>)

2

![image 312](<2021-barg-bounds-sum-distances-spherical_images/imageFile312.png>)

![image 313](<2021-barg-bounds-sum-distances-spherical_images/imageFile313.png>)

![image 314](<2021-barg-bounds-sum-distances-spherical_images/imageFile314.png>)

´c

?n ` 1 ˘ 1q

n?n ` 1

n?n ` 1p

n ` 1 4 ˘ 1

- 1

![image 315](<2021-barg-bounds-sum-distances-spherical_images/imageFile315.png>)

- 2


1 3

¯

?

![image 316](<2021-barg-bounds-sum-distances-spherical_images/imageFile316.png>)

![image 317](<2021-barg-bounds-sum-distances-spherical_images/imageFile317.png>)

![image 318](<2021-barg-bounds-sum-distances-spherical_images/imageFile318.png>)

?n`1 “

“

An`1

, An`1

![image 319](<2021-barg-bounds-sum-distances-spherical_images/imageFile319.png>)

![image 320](<2021-barg-bounds-sum-distances-spherical_images/imageFile320.png>)

![image 321](<2021-barg-bounds-sum-distances-spherical_images/imageFile321.png>)

![image 322](<2021-barg-bounds-sum-distances-spherical_images/imageFile322.png>)

n`1 2

2 ¯

2 ¯

![image 323](<2021-barg-bounds-sum-distances-spherical_images/imageFile323.png>)

![image 324](<2021-barg-bounds-sum-distances-spherical_images/imageFile324.png>)

![image 325](<2021-barg-bounds-sum-distances-spherical_images/imageFile325.png>)

´n ` 1 4 ` 1

¯

“ n

. Using (29), we ﬁnd that the sum of distances in both cases comes out to be τnppC˜NqKq “

An`1

![image 326](<2021-barg-bounds-sum-distances-spherical_images/imageFile326.png>)

![image 327](<2021-barg-bounds-sum-distances-spherical_images/imageFile327.png>)

2

?

1 4?2

N3{2 ´ OpNq.

![image 328](<2021-barg-bounds-sum-distances-spherical_images/imageFile328.png>)

2N2 ´

![image 329](<2021-barg-bounds-sum-distances-spherical_images/imageFile329.png>)

![image 330](<2021-barg-bounds-sum-distances-spherical_images/imageFile330.png>)

Note that τnppC˜NqKq follows closely the upper bound (4).

Many more similar examples can be given using the known results on binary codes with few weights [43, Ch.15], [22, 27, 42, 51] (this list is far from being complete). At the same time, obviously there are sequences of binary codes pCNq that yield spherical codes whose sum of distances differs signiﬁcantly from ?2N2. For instance, consider the code CN formed of

![image 331](<2021-barg-bounds-sum-distances-spherical_images/imageFile331.png>)

`n 2

˘

vectors of Hamming weight 2, then the pairwise distances are 2 and 4, and a calculation shows that τNpC˜Nq “ p2Nq7{4p1 ` op1qq.

4. SUM OF DISTANCES AND BOUNDS FOR QUADRATIC DISCREPANCY OF BINARY CODES

An analog of Stolarsky’s identity (3) for the Hamming space Xn “ t0,1un was recently derived in [4]. For a binary code CN P Xn deﬁne the quadratic discrepancy as follows:

ÿn

vptq 2n ¯2

´|Bpx,tq X CN| N ´

ÿ

DL

b pCNq “

,

2

![image 332](<2021-barg-bounds-sum-distances-spherical_images/imageFile332.png>)

![image 333](<2021-barg-bounds-sum-distances-spherical_images/imageFile333.png>)

t“0

xPX

řt

`n i

˘

where Bpx,tq “ ty P Xn : dHpx,yq ď tu is the Hamming ball centered at x and vptq “

is its volume. Note that we again abuse the terminology since strictly speaking, DL

i“0

b pCNq is a square of the discrepancy; see also footnote 1 above. We use the subscript b to differentiate this quantity from it spherical counterpart deﬁned in (2). To state the Hamming space version of Stolarsky’s identity, let us deﬁne a function λ : Z Ñ Z. By deﬁnition, λp0q “ 0 and for w “ 2i,1 ď i ď tn{2u

2

λpw ´ 1q “ λpwq “ 2n´wiˆ

i ˙. (30) An analog of relation (2) in the binary case has the following form:

w

ÿN

n 2n`1ˆ

2n n ˙ ´

1 N2

DL

λpdHpzi,zjqq.

b pCNq “

2

![image 334](<2021-barg-bounds-sum-distances-spherical_images/imageFile334.png>)

![image 335](<2021-barg-bounds-sum-distances-spherical_images/imageFile335.png>)

i,j“1

The average value of λp¨q over the code can be written in the form

ÿn

ÿN

1 N2

1 N

λpdHpzi,zjqq “

Awλpwq, (31)

![image 336](<2021-barg-bounds-sum-distances-spherical_images/imageFile336.png>)

![image 337](<2021-barg-bounds-sum-distances-spherical_images/imageFile337.png>)

w“1

i,j“1

where pAw,w “ 1,...,nq is the distribution of distances in CN deﬁned above. Thus, the value of discrepancy of the code is determined once we know the average “energy” for the potential λ, denoted xλyCN

. Some estimates of this quantity were proved in [4].

In this section we note that the bounds on the sum of distances derived above in Sec. 2 imply bounds on xλyCN

via the spherical embedding, and thus also imply bounds on DL

b . Our results are based on the following simple observation.

2

- Proposition 4.1. Let n be even and let CN Ă Xn be a binary code and let C˜N Ă Sn´1 be its spherical embedding. We have


2n´1 N2 c

![image 338](<2021-barg-bounds-sum-distances-spherical_images/imageFile338.png>)

n π

τnpC˜Nq (32) Proof. Assume that n is even. From (31) and (30) we obtain

xλyCN ď

![image 339](<2021-barg-bounds-sum-distances-spherical_images/imageFile339.png>)

![image 340](<2021-barg-bounds-sum-distances-spherical_images/imageFile340.png>)

nÿ{2

ÿN

1 N

λpdHpzi,zjqq “ ÿ

![image 341](<2021-barg-bounds-sum-distances-spherical_images/imageFile341.png>)

a

pA2i´1 ` A2iq2n

i{π

Awλpwq ď

![image 342](<2021-barg-bounds-sum-distances-spherical_images/imageFile342.png>)

w“1

i“1

i,j“1

nÿ{2

ÿn

?

2n´1{2 ?π

2n ?π

Aw?w

![image 343](<2021-barg-bounds-sum-distances-spherical_images/imageFile343.png>)

![image 344](<2021-barg-bounds-sum-distances-spherical_images/imageFile344.png>)

“

2i ď

pA2i´1 ` A2iq

![image 345](<2021-barg-bounds-sum-distances-spherical_images/imageFile345.png>)

![image 346](<2021-barg-bounds-sum-distances-spherical_images/imageFile346.png>)

![image 347](<2021-barg-bounds-sum-distances-spherical_images/imageFile347.png>)

![image 348](<2021-barg-bounds-sum-distances-spherical_images/imageFile348.png>)

w“1

i“1

`2i

![image 349](<2021-barg-bounds-sum-distances-spherical_images/imageFile349.png>)

a

i{π 22i, valid for all i. Substituting the value of the sum from (29), we obtain the claim.

˘

ď

where for the ﬁrst inequality we used the estimate i

i

With minor differences, this result is also valid for odd n. Earlier results [4, Thm.5.2] give several estimates for average value of λ; for instance, for n “ 2l ´ 1, l

even

- 1

![image 350](<2021-barg-bounds-sum-distances-spherical_images/imageFile350.png>)

- 2N q.


xλyCN ď λplqp1 ´

Using this inequality and estimating the binomial coefﬁcient, we obtain xλyCN ď 2n´l

l 2ˆ

l l{2˙ ď 2n´1{2

![image 351](<2021-barg-bounds-sum-distances-spherical_images/imageFile351.png>)

a

l{π, (33)

![image 352](<2021-barg-bounds-sum-distances-spherical_images/imageFile352.png>)

valid for all odd n. While in [4] inequality (30) is proved by linear programming in the Hamming space, similar estimates are also obtained from (32) and the upper bounds (7)-(9) (for N in the range of their applicability), and they largely coincide with earlier results. For instance, using (32) and a bound of the form

(14) with N “ δn2, we obtain xλyCN ď 2n´21

an πp1 ´ OpN´1{2qq, which is only slightly inferior to (33).

![image 353](<2021-barg-bounds-sum-distances-spherical_images/imageFile353.png>)

![image 354](<2021-barg-bounds-sum-distances-spherical_images/imageFile354.png>)

![image 355](<2021-barg-bounds-sum-distances-spherical_images/imageFile355.png>)

In summary, spherical embeddings of binary codes give an alternative way of proving lower bounds for their quadratic discrepancy.

5. PROOFS OF THE BOUNDS

In this section, we prove the bounds on the sum of distances stated in Sec. 2, using the energy function Ehpn,Nq with hptq “ Lptq “ ´

![image 356](<2021-barg-bounds-sum-distances-spherical_images/imageFile356.png>)

a

2p1 ´ tq (the negative distance). Accordingly, the upper and lower bounds of Sec. 2 exchange their roles. All the derivatives Lpiqptq, i ě 1, are deﬁned and positive in r´1,1q and limtÑ1´ Lpiqptq “ `8; Lptq ` 2 is nonnegative and increasing in r´1,1s, and thus Lptq is absolutely monotone up to an additive constant. Thus, Lptq ﬁts the frameworks for ULB and UUB from [14] and [16], respectively (the possible ULB application was mentioned already in the introduction of [14]).

- 5.1. Derivation of the necessary parameters. Here we explain the choice of the parameters in the Levenshtein framework used to derive the bounds.


The parameters k, ε, m “ 2k ´ 1 ` ε, and pρi,αiq, i “ 0,1,...,k ´ 1 ` ε, originate in the paper of Levenshtein [40] (see also [41, Section 5]), where the author used them to establish optimality of his bound on the size of codes (see Theorem 5.39 in [41]).

For each positive integer m “ 2k ´1`ε, where ε P t0,1u accounts for the parity of m, Levenshtein used the degree m polynomial

k´ź2`ε

fmpn,sqptq “ pt ´ α0q2´εpt ´ αk´1`εq

pt ´ αiq2

i“1

to obtain his universal upper bound Lmpn,sq on the maximal cardinality of a code on Sn´1 with separation

- s. The numbers α0 ă α1 ă ¨¨¨ ă αk´1`ε belong to r´1,1q and αk´1`ε “ s and α0 “ ´1 if and only if ε “ 1. The polynomial fm can be written in the form


fmpn,sqptq “ pt ` 1qε pPkptqPk´1psq ´ PkpsqPk´1ptqq2 {pt ´ sq, (34) where Piptq “ Pp

n´1

2 , n´2 3`εq

![image 357](<2021-barg-bounds-sum-distances-spherical_images/imageFile357.png>)

![image 358](<2021-barg-bounds-sum-distances-spherical_images/imageFile358.png>)

i ptq is the Jacobi polynomial normalized to satisfy Pip1q “ 1. For small m the zeros αi of fm can be easily found.

The quadrature formula

k´ÿ1`ε

fp1q Lmpn,sq

f0 “

`

ρifpαiq, (35) which is exact for all real polynomials fptq “

![image 359](<2021-barg-bounds-sum-distances-spherical_images/imageFile359.png>)

i“0

i“0 fiPipnqptq of degree d ď m, reveals a strong relation between the Levenshtein bounds and the energy bounds, as explained in the next paragraph (for more details, see [14, Section 2.2] and [16, Section 3.1]). We also use (35) to calculate the weights ρi; see, for example, [12], where the formulas for ρi for odd m were derived from a Vandermonde-type system. We also note that Lmpn,sq “ fmpn,sqp1q{f0, where f0 is the constant coefﬁcient of fmpn,sq.

řd

Formula (35) is instrumental in the representation (5) of the ULB for the energy EhpCNq and the proof of its optimality in [14]. For ULB, we need polynomials that are positive deﬁnite (i.e., their Gegenbauer expansions have nonnegative coefﬁcients) and such that f ď h in r´1,1s. First, m “ 2k ´ 1 ` ε is

determined by the rule N P rD˚pn,mq,D˚pn,m ` 1q. Hermite interpolation with fpαiq “ hpαiq, where the nodes αi, i “ 0,1,...,k ´ 1 ` ε arise as the roots of Lmpn,sq “ N considered as an equation in s, provides an LP polynomial satisfying both requirements [14, Theorem 3.1]. Then the quantity f0N ´ fp1q, which gives rise to the ULB, is computed from (35) (applied with Lmpn,sq “ N) to give the right-hand side of (5). Note that eventually everything is determined by n and N. We will see how it works in practice in Section 5.2.

We next explain the derivation of the universal upper bound (UUB) from [16] (see Section 3.2 in that paper) which is based on choice of polynomials

fptq “ ´λfmpn,sqptq ` gTptq for given n, N, and s. As mentioned in the Introduction, the polynomial fptq has to satisfy f ě h for

- t P r´1,ss and to have fi ď 0 for i ě 1 in its Gegenbauer expansion. To fulﬁl these conditions, fmpn,sqptq is taken to be the degree-m Levenshtein polynomial (34), gTptq interpolates the potential function at the multiset T, which consists of the roots of fmpn,sqptq (counted with their multiplicities; this means that the degree of gT is m ´ 1) and λ “ maxtgi{ℓi : 1 ď i ď m´ 1u is a positive constant. More speciﬁcally, where


mÿ´1

ÿm

giPipnqptq

ℓiPipnqptq, gTptq “

fmpn,sqptq “

i“0

i“0

are the Gegenbauer expansions of fmpn,sqptq and gTptq, respectively (note that ℓi ą 0 for every i ď m [41, Theorem 5.42]). The parameter N1 “ Lmpn,sq ě N, computed for given n ans s (the latter determining m uniquely), is used to ﬁnd the parameters ρi and αi exactly as in the ULB part (but with N1 instead of N; for this to work we assume that N1 “ Lmpn,sq P rD˚pn,mq,D˚pn,m ` 1qq). Note that the equality N1 “ N holds if and only if there exists a universally optimal code of size N in n dimensions (in this case, ULB and UUB coincide4). In our computations of UUBs below we ﬁrst ﬁnd the Hermite interpolant gTptq, then the parameter λ (which already gives fptq), and ﬁnally compute the bound (6).

- 5.2. Lower bounds.


- Proposition 5.1. For 2 ď N ď n ` 1 we have


- ELpn,Nq ě ´τ1pn,Nq. (36)

For n ` 1 ď N ď 2n, we have

- ELpn,Nq ě ´τ2pn,Nq. (37)

For 2n ď N ď npn ` 3q{2, we have

- ELpn,Nq ě ´τ3pn,Nq. (38)


where τ1, τ2, and τ3 are deﬁned in (7)-(9).

These estimates constitute the ﬁrst three bounds in (5), beginning with expressing the parameters pρi,αiq as functions of the dimension n and cardinality N P rD˚pn,mq,D˚pn,m ` 1qq, m “ 1,2,3. In all three proofs below we ﬁrst ﬁnd the roots αi of the Levenshtein polynomial (34) setting Lmpn,sq “ N for m “ 1,2,3, respectively. This is equivalent to solving in s the equation Lmpn,sq “ N. Then we give the weights ρi, computed by setting suitable polynomials (we used fptq “ 1,t,t2,t3; for example fptq “ 1 gives the identity

řk´1`ε i“1 ρi “ 1 ´ 1{N) in the quadrature formula (35).

Proof of (36). For the degree 1 bound (36) we have α0 “ ´1{pN ´1q and ρ0 “ ´1{Nα0 “ pN ´1q{N. Therefore

![image 360](<2021-barg-bounds-sum-distances-spherical_images/imageFile360.png>)

a

ELpn,Nq ě N2ρ0Lpα0q “ NpN ´ 1qLpα0q “ ´N

2NpN ´ 1q.

l

![image 361](<2021-barg-bounds-sum-distances-spherical_images/imageFile361.png>)

4Having said that, we may view the difference between the ULB and UUB as a measure of how far the codes are from being universally optimal.

Proof of (37). For degree 2 (with k “ 1 and ε “ 1) we have α0 “ ´1, α1 “ ´n2pnN´´N2q, ρ0 “ NnN`´Nn´´14n and ρ1 “ npN´2q

![image 362](<2021-barg-bounds-sum-distances-spherical_images/imageFile362.png>)

![image 363](<2021-barg-bounds-sum-distances-spherical_images/imageFile363.png>)

![image 364](<2021-barg-bounds-sum-distances-spherical_images/imageFile364.png>)

NpNn`N´4nq. Since Lp´1q “ ´2 and Lpα1q “ ´b

2

2Npn´1q

npN´2q , we obtain that the expression N2pρ0Lpα0q ` ρ1Lpα1qq from (5) is equal to ´τ2pn,Nq as given in (8). l

![image 365](<2021-barg-bounds-sum-distances-spherical_images/imageFile365.png>)

![image 366](<2021-barg-bounds-sum-distances-spherical_images/imageFile366.png>)

Proof of (38). For the degree-3 lower bound we take k “ 2 and ε “ 0. By (5) we have

ELpn,Nq ě N2pρ0Lpα0q ` ρ1Lpα1qq, (39) where N P rD˚pn,3q,D˚pn,4qs “ r2n,npn ` 3q{2s, and

?D 2npN ´ n ´ 1q

![image 367](<2021-barg-bounds-sum-distances-spherical_images/imageFile367.png>)

´npn ´ 1q ˘

, D “ n2pn ´ 1q2 ` 4npN ´ n ´ 1qpN ´ 2nq,

α0,1 “

![image 368](<2021-barg-bounds-sum-distances-spherical_images/imageFile368.png>)

are the roots of the quadratic equation npN ´n´1qs2`npn´1qs`2n´N “ 0 obtained from the equality L3pn,sq “ N. Further, the weights ρ0 and ρ1 satisfy the formulas

1 ´ α21 α0pα21 ´ α20q

1 ´ α20 α1pα20 ´ α21q (note that the numerators resemble the potential Lptq computed for α0,α1; this will make our expressions symmetric). In the sequel, we use the following symmetric expressions for α0 and α1

ρ0N “

, ρ1N “

![image 369](<2021-barg-bounds-sum-distances-spherical_images/imageFile369.png>)

![image 370](<2021-barg-bounds-sum-distances-spherical_images/imageFile370.png>)

?D npN ´ n ´ 1q2

![image 371](<2021-barg-bounds-sum-distances-spherical_images/imageFile371.png>)

n ´ 1 N ´ n ´ 1

N ´ 2n npN ´ n ´ 1q

pn ´ 1q

, α20 ´ α21 “

α0 ` α1 “ ´

, α0α1 “ ´

,

![image 372](<2021-barg-bounds-sum-distances-spherical_images/imageFile372.png>)

![image 373](<2021-barg-bounds-sum-distances-spherical_images/imageFile373.png>)

![image 374](<2021-barg-bounds-sum-distances-spherical_images/imageFile374.png>)

pn ´ 1qpN ´ 2nq npN ´ n ´ 1q

pn ´ 1qN npN ´ n ´ 1q

, p1 ` α0qp1 ` α1q “

p1 ´ α0qp1 ´ α1q “

.

![image 375](<2021-barg-bounds-sum-distances-spherical_images/imageFile375.png>)

![image 376](<2021-barg-bounds-sum-distances-spherical_images/imageFile376.png>)

Our task is to express the bound (39) via n and N. Using the above equalities, we obtain ELpn,Nq ě Npρ0NLpα0q ` ρ1NLpα1qq

¸

“ ´N ˜p1 ´ α21q

![image 377](<2021-barg-bounds-sum-distances-spherical_images/imageFile377.png>)

![image 378](<2021-barg-bounds-sum-distances-spherical_images/imageFile378.png>)

a

a

p1 ´ α20q

2p1 ´ α0q α0pα21 ´ α20q

2p1 ´ α1q α1pα20 ´ α21q

`

![image 379](<2021-barg-bounds-sum-distances-spherical_images/imageFile379.png>)

![image 380](<2021-barg-bounds-sum-distances-spherical_images/imageFile380.png>)

n2NpN ´ n ´ 1q3 pn ´ 1qpN ´ 2nq

?D ´

2p1 ´ α1q¯

![image 381](<2021-barg-bounds-sum-distances-spherical_images/imageFile381.png>)

![image 382](<2021-barg-bounds-sum-distances-spherical_images/imageFile382.png>)

α1p1 ´ α21qa

2p1 ´ α0q ´ α0p1 ´ α20qa

“ ´

.

![image 383](<2021-barg-bounds-sum-distances-spherical_images/imageFile383.png>)

![image 384](<2021-barg-bounds-sum-distances-spherical_images/imageFile384.png>)

![image 385](<2021-barg-bounds-sum-distances-spherical_images/imageFile385.png>)

![image 386](<2021-barg-bounds-sum-distances-spherical_images/imageFile386.png>)

a

a

Consider the expression S “ α1p1 ´ α21q

2p1 ´ α0q ´ α0p1 ´ α20q

2p1 ´ α1q. We compute S2

pn ´ 1qpA ´ Bq N npN ´ n ´ 1q

2 “

, and thus

![image 387](<2021-barg-bounds-sum-distances-spherical_images/imageFile387.png>)

![image 388](<2021-barg-bounds-sum-distances-spherical_images/imageFile388.png>)

![image 389](<2021-barg-bounds-sum-distances-spherical_images/imageFile389.png>)

S “ d

2pA ´ Bqpn ´ 1qN npN ´ n ´ 1q

, where we have denoted

![image 390](<2021-barg-bounds-sum-distances-spherical_images/imageFile390.png>)

pn ´ 1qpN ´ 2nq2rNn3 ` p2N ´ 1qn2 ´ pN ´ 1qp7N ´ 2qn ` pN ´ 1q2p2N ` 3qs n2pN ´ n ´ 1q5 and

A “

![image 391](<2021-barg-bounds-sum-distances-spherical_images/imageFile391.png>)

![image 392](<2021-barg-bounds-sum-distances-spherical_images/imageFile392.png>)

2pn ´ 1qpN ´ 2nq2apn ´ 1qN pnpN ´ n ´ 1qq5{2

B “ ´

.

![image 393](<2021-barg-bounds-sum-distances-spherical_images/imageFile393.png>)

Therefore

![image 394](<2021-barg-bounds-sum-distances-spherical_images/imageFile394.png>)

c

nNpN ´ n ´ 1q2 pN ´ 2nq

2pA ´ BqnNpN ´ n ´ 1q n ´ 1

?D

ELpn,Nq ě ´

.

![image 395](<2021-barg-bounds-sum-distances-spherical_images/imageFile395.png>)

![image 396](<2021-barg-bounds-sum-distances-spherical_images/imageFile396.png>)

![image 397](<2021-barg-bounds-sum-distances-spherical_images/imageFile397.png>)

Performing simpliﬁcations under the square root, we obtain 2pA ´ BqnNpN ´ n ´ 1q n ´ 1 “ 2nNpN ´ n ´ 1q˜ pN ´ 2nq2A1 n2pN ´ n ´ 1q5

¸

![image 398](<2021-barg-bounds-sum-distances-spherical_images/imageFile398.png>)

2pN ´ 2nq2a

Npn ´ 1q n5{2pN ´ n ´ 1q5{2

`

![image 399](<2021-barg-bounds-sum-distances-spherical_images/imageFile399.png>)

![image 400](<2021-barg-bounds-sum-distances-spherical_images/imageFile400.png>)

![image 401](<2021-barg-bounds-sum-distances-spherical_images/imageFile401.png>)

2NpN ´ 2nq2 n4pN ´ n ´ 1q4 ´

Npn ´ 1qn5pN ´ n ´ 1q5¯

![image 402](<2021-barg-bounds-sum-distances-spherical_images/imageFile402.png>)

a

n3A1 ` 2

“

![image 403](<2021-barg-bounds-sum-distances-spherical_images/imageFile403.png>)

2NpN ´ 2nq2 n2pN ´ n ´ 1q4 `

nA1 ` 2pN ´ n ´ 1q2B1

˘

“

![image 404](<2021-barg-bounds-sum-distances-spherical_images/imageFile404.png>)

with A1 and B1 as in (10) and (11), respectively. Upon substituting this back into the bound for ELpn,Nq, we obtain

![image 405](<2021-barg-bounds-sum-distances-spherical_images/imageFile405.png>)

a

2NpnA1 ` 2pN ´ n ´ 1q2B1q ?D

N

ELpn,Nq ě ´

, establishing the bound (38) with τ3pn,Nq as in (9). l

![image 406](<2021-barg-bounds-sum-distances-spherical_images/imageFile406.png>)

![image 407](<2021-barg-bounds-sum-distances-spherical_images/imageFile407.png>)

- 5.3. Upper bounds. In this section we prove bounds (16)-(18), deriving an explicit form of the ﬁrst three universal upper bounds for CNpn,sq codes from [16] for Lptq as functions of n, N and s. In addition to the parameters pρi,αiq as explained above (but now related to N1 “ Lmpn,sq instead of N), we need to ﬁnd the polynomial gTptq, then the real parameter λ and ﬁnally the polynomial fptq as explained in the last paragraph of Section 5.1. Recall again that because of the sign change, the inequalities (16)-(18) are inverted.


- Proposition 5.2. For N P r2,n ` 1s and s P r´1{pN ´ 1q,´1{ns, we have


- ELpn,N,sq ď ´τp1qpn,N,sq. (40)

For N P rn ` 1,2ns and s P rpN ´ 2nq{npN ´ 2q,0s, we have

- ELpn,N,sq ď ´τp2qpn,N,sq. (41)

For N P r2n,npn ` 3q{2s and s P „?

![image 408](<2021-barg-bounds-sum-distances-spherical_images/imageFile408.png>)

n2pn´1q2`4npN´n´1qpN´2nq´npn´1q

![image 409](<2021-barg-bounds-sum-distances-spherical_images/imageFile409.png>)

2npN´n´1q ,

?n`3´1

![image 410](<2021-barg-bounds-sum-distances-spherical_images/imageFile410.png>)

![image 411](<2021-barg-bounds-sum-distances-spherical_images/imageFile411.png>)

n`2 , we have

- ELpn,N,sq ď ´τp3qpn,N,sq (42)


where the quantities τp1q,τp2q,τp3q are deﬁned in (16)-(18) above.

- Remark 5.1. We set upper limits for s in all three cases as suggested implicitly by the framework in [16]. The bounds are valid beyond these limits but most likely they can be improved by polynomials of higher degrees.

Proof of (40). For ﬁxed n, N P r2,n ` 1s and s P r´1{pN ´ 1q,´1{ns, we consider the degree 1 UUB ELpn,N,sq ď N ˆ

N L1pn,sq

![image 412](<2021-barg-bounds-sum-distances-spherical_images/imageFile412.png>)

´ 1˙fp1q ` N2ρ0Lpsq, where the parameters are as follows: L1pn,sq “ ps ´ 1q{s “: N1 is the ﬁrst Levenshtein bound,

fptq “ ´λf1pn,sqptq ` gTptq “ ´λpt ´ sq ` gTptq is our linear programming polynomial, and α0 “ s, ρ0 “ ´1{N1s “ 1{p1´sq are Levenshtein’s parameters corresponding to s (i.e., to N1). The polynomial gTptq is constant and is found from gTpsq “ Lpsq. Then λ “ 0 and fptq “ Lpsq give the bound

ELpn,N,sq ď ˆ

N N1 ´ 1˙NLpsq ` N2ρ0Lpsq “ NpN ´ 1qLpsq.

![image 413](<2021-barg-bounds-sum-distances-spherical_images/imageFile413.png>)

- Remark 5.2. As already observed, this bound is straightforward upon estimating all terms in the energy sum ELpCNq by the constant Lpsq.


Proof of (41). For ﬁxed n, N P rn ` 1,2ns and s P rpN ´ 2nq{npN ´ 2q,0s, we consider the degree 2 UUB following the derivation in [16]

ELpn,N,sq ď N ˆ

´ 1˙fp1q ` N2pρ0Lpα0q ` ρ1Lpα1qq, (43)

N L2pn,sq

![image 414](<2021-barg-bounds-sum-distances-spherical_images/imageFile414.png>)

where the parameters are deﬁned as follows: N1 :“ L2pn,sq “ 2np1´sq{p1´nsq is the second Levenshtein bound,

fptq “ ´λf2pn,sqptq ` gTptq “ ´λpt ` 1qpt ´ sq ` gTptq is our linear programming polynomial (to be described below), and

npN1 ´ 2q2 N1pN1n ` N1 ´ 4nq

N1 ´ n ´ 1 N1n ` N1 ´ 4n

, ρ1 “

α0 “ ´1, α1 “ s, ρ0 “

![image 415](<2021-barg-bounds-sum-distances-spherical_images/imageFile415.png>)

![image 416](<2021-barg-bounds-sum-distances-spherical_images/imageFile416.png>)

are the Levenshtein parameters corresponding to s (compare with the parameters in the proof of (37)). The polynomial gTptq with T “ t´1,su, i.e. gTp´1q “ Lp´1q, gTpsq “ Lpsq, becomes

![image 417](<2021-barg-bounds-sum-distances-spherical_images/imageFile417.png>)

![image 418](<2021-barg-bounds-sum-distances-spherical_images/imageFile418.png>)

a

a

2p1 ´ sqqt ´ 2s´

2p1 ´ sq 1 ` s

p2 ´

Lpsq ´ Lp´1q 1 ` s

Lpsq ` sLp´1q 1 ` s “

gTptq “

t `

.

![image 419](<2021-barg-bounds-sum-distances-spherical_images/imageFile419.png>)

![image 420](<2021-barg-bounds-sum-distances-spherical_images/imageFile420.png>)

![image 421](<2021-barg-bounds-sum-distances-spherical_images/imageFile421.png>)

The coefﬁcient λ is chosen to make f1 “ 0 in the Gegenbauer expansion fptq “ f2P2pnqptq`f1P1pnqptq`f0 (this choice is unique). This gives λ “ 2´

?

![image 422](<2021-barg-bounds-sum-distances-spherical_images/imageFile422.png>)

2p1´sq

1´s2 and fptq “ ´

![image 423](<2021-barg-bounds-sum-distances-spherical_images/imageFile423.png>)

![image 424](<2021-barg-bounds-sum-distances-spherical_images/imageFile424.png>)

![image 425](<2021-barg-bounds-sum-distances-spherical_images/imageFile425.png>)

a

a

2p1 ´ sqqt2 ´ 2s2 `

p2 ´

2p1 ´ sq 1 ´ s2

, whence fp1q “ ´2.

![image 426](<2021-barg-bounds-sum-distances-spherical_images/imageFile426.png>)

Therefore, (43) gives

N N1 ´ 1˙p´2q ` N2 ˜pN1 ´ n ´ 1qp´2q

¸,

![image 427](<2021-barg-bounds-sum-distances-spherical_images/imageFile427.png>)

a

npN1 ´ 2q2p´

ELpn,N,sq ď N ˆ

2p1 ´ sqq N1pN1n ` N1 ´ 4nq

N1n ` N1 ´ 4n `

![image 428](<2021-barg-bounds-sum-distances-spherical_images/imageFile428.png>)

![image 429](<2021-barg-bounds-sum-distances-spherical_images/imageFile429.png>)

![image 430](<2021-barg-bounds-sum-distances-spherical_images/imageFile430.png>)

implying (41). Proof of (42). For ﬁxed n, N, and s as in the condition (19), we derive the degree 3 UUB

ELpn,N,sq ď N ˆ

´ 1˙fp1q ` N2pρ0Lpα0q ` ρ1Lpα1qq, (44) where the parameters are deﬁned as follows:

N L3pn,sq

![image 431](<2021-barg-bounds-sum-distances-spherical_images/imageFile431.png>)

np1 ´ sqppn ` 1qs ` 2q 1 ´ ns2 is the third Levenshtein bound,

N1 :“ L3pn,sq “

![image 432](<2021-barg-bounds-sum-distances-spherical_images/imageFile432.png>)

fptq “ ´λf3pn,sqptq ` gTptq “ ´λpt ´ α0q2pt ´ sq ` gTptq is the linear programming polynomial to be found, and

?D1 2npN1 ´ n ´ 1q

?D1 2npN1 ´ n ´ 1q

![image 433](<2021-barg-bounds-sum-distances-spherical_images/imageFile433.png>)

![image 434](<2021-barg-bounds-sum-distances-spherical_images/imageFile434.png>)

1 ` s 1 ` ns

´npn ´ 1q `

´npn ´ 1q ´

“ ´

, α1 “

“ s,

α0 “

![image 435](<2021-barg-bounds-sum-distances-spherical_images/imageFile435.png>)

![image 436](<2021-barg-bounds-sum-distances-spherical_images/imageFile436.png>)

![image 437](<2021-barg-bounds-sum-distances-spherical_images/imageFile437.png>)

n2pn ´ 1q2p1 ` 2s ` ns2q2 p1 ´ ns2q2

D1 “ n2pn ´ 1q2 ` 4npN1 ´ n ´ 1qpN1 ´ 2nq “

,

![image 438](<2021-barg-bounds-sum-distances-spherical_images/imageFile438.png>)

1 ´ α21 N1α0pα21 ´ α20q

p1 ` nsq3 nppn ` 1qs ` 2qp1 ` 2s ` ns2q

ρ0 “

“

,

![image 439](<2021-barg-bounds-sum-distances-spherical_images/imageFile439.png>)

![image 440](<2021-barg-bounds-sum-distances-spherical_images/imageFile440.png>)

1 ´ α20 N1α1pα20 ´ α21q

n ´ 1 np1 ´ sqp1 ` 2s ` ns2q

ρ1 “

“

,

![image 441](<2021-barg-bounds-sum-distances-spherical_images/imageFile441.png>)

![image 442](<2021-barg-bounds-sum-distances-spherical_images/imageFile442.png>)

are the Levenshtein’s parameters corresponding to s (note that they are also shown to depend on n and s only).

The ULB part ρ0Lpα0q ` ρ1Lpα1q in (44) can be found as in the proof of (38) but with N1 instead of N. Explicitly, this means that

1 N1

ρ0Lpα0q ` ρ1Lpα1q “ ´

![image 443](<2021-barg-bounds-sum-distances-spherical_images/imageFile443.png>)

![image 444](<2021-barg-bounds-sum-distances-spherical_images/imageFile444.png>)

d

2N1pnA1 ` 2pN1 ´ n ´ 1q2B1q D1

,

![image 445](<2021-barg-bounds-sum-distances-spherical_images/imageFile445.png>)

- where A1 and B1 are as in (10) and (11), respectively, but with N1 instead of N, and D1 as above (so D1 has the same form as D, but with N1 instead of N). We obtain

ELpn,N,sq ď

N N1

![image 446](<2021-barg-bounds-sum-distances-spherical_images/imageFile446.png>)

˜pN ´ N1qfp1q ´ Nd

![image 447](<2021-barg-bounds-sum-distances-spherical_images/imageFile447.png>)

2N1pnA1 ` 2pN1 ´ n ´ 1q2B1q D1

![image 448](<2021-barg-bounds-sum-distances-spherical_images/imageFile448.png>)

¸ , (45)

In order to rewrite (45) in terms of n and s, we ﬁrst write the ULB part in terms of n and s by using the above expressions, i.e.

- A1 “

pn ´ 1q2rp1 ` nsq5p1 ´ sq ` pn ´ 1q2ppn ` 1qs ` 2qs p1 ´ ns2q3

![image 449](<2021-barg-bounds-sum-distances-spherical_images/imageFile449.png>)

,

- B1 “


npn ´ 1qap1 ´ sqp1 ` nsqppn ` 1qs ` 2q 1 ´ ns2

![image 450](<2021-barg-bounds-sum-distances-spherical_images/imageFile450.png>)

![image 451](<2021-barg-bounds-sum-distances-spherical_images/imageFile451.png>)

,

N1 ´ n ´ 1 “

pn ´ 1qp1 ` nsq 1 ´ ns2

![image 452](<2021-barg-bounds-sum-distances-spherical_images/imageFile452.png>)

, and D1 “ D1pn,sq as found above. We ﬁnd

ELpn,N,sq ď

N N1

![image 453](<2021-barg-bounds-sum-distances-spherical_images/imageFile453.png>)

˜pN ´ N1qfp1q ´

p1 ´ ns2qN

a

![image 454](<2021-barg-bounds-sum-distances-spherical_images/imageFile454.png>)

2N1pnA1 ` 2pN1 ´ n ´ 1q2B1q npn ´ 1qp1 ` 2s ` ns2q

![image 455](<2021-barg-bounds-sum-distances-spherical_images/imageFile455.png>)

¸

“

N N1

![image 456](<2021-barg-bounds-sum-distances-spherical_images/imageFile456.png>)

˜pN ´ N1qfp1q ´

N

a

![image 457](<2021-barg-bounds-sum-distances-spherical_images/imageFile457.png>)

2N1pnA2 ` 2p1 ` nsq2B2q np1 ` 2s ` ns2q

![image 458](<2021-barg-bounds-sum-distances-spherical_images/imageFile458.png>)

¸

“

N N1

![image 459](<2021-barg-bounds-sum-distances-spherical_images/imageFile459.png>)

˜pN ´ N1qfp1q ´

N

a

![image 460](<2021-barg-bounds-sum-distances-spherical_images/imageFile460.png>)

2p1 ´ sqppn ` 1qs ` 2qpA2 ` 2p1 ` nsq2B2q p1 ` 2s ` ns2qp1 ´ ns2q

![image 461](<2021-barg-bounds-sum-distances-spherical_images/imageFile461.png>)

¸ , (46)

- where A2 and B2 are as given in (20).


Second, we ﬁnd fptq in order to compute fp1q. The polynomial gTptq “ at2 ` bt ` c interpolates Lptq in T “ tα0,α0,α1u, i.e. gpα0q “ Lpα0q, g1pα0q “ L1pα0q, and gpα1q “ Lpα1q. Resolving this to ﬁnd a, b, and c, we obtain the Gegenbauer expansion of fptq as follows

λpn ´ 1q n ` 2

pn ´ 1qpa ` λp2α0 ` α1qq n

P2pnqptq ` ˆb ´

P3pnqptq `

fptq “ ´

![image 462](<2021-barg-bounds-sum-distances-spherical_images/imageFile462.png>)

![image 463](<2021-barg-bounds-sum-distances-spherical_images/imageFile463.png>)

λppα20 ` 2α0α1qpn ` 2q ` 3q n ` 2 ˙P1pnqptq `

λpα20α1n ` 2α0 ` α1q ` a ` cn n

P0pnqptq, where

![image 464](<2021-barg-bounds-sum-distances-spherical_images/imageFile464.png>)

![image 465](<2021-barg-bounds-sum-distances-spherical_images/imageFile465.png>)

- a “

Lpα1q ´ Lpα0q ´ L1pα0qpα1 ´ α0q pα1 ´ α0q2

![image 466](<2021-barg-bounds-sum-distances-spherical_images/imageFile466.png>)

,

- b “

L1pα0qpα21 ´ α20q ´ 2α0pLpα1q ´ Lpα0qq pα1 ´ α0q2

![image 467](<2021-barg-bounds-sum-distances-spherical_images/imageFile467.png>)

,

- c “


α20pLpα1q ´ Lpα0qq ´ α0α1pα1 ´ α0qL1pα0q ` pα1 ´ α0q2Lpα0q pα1 ´ α0q2

.

![image 468](<2021-barg-bounds-sum-distances-spherical_images/imageFile468.png>)

According to the rule in Theorem 3.2 from [16], the coefﬁcient λ has to be chosen as maxtg1{ℓ1,g2{ℓ2u, which is equivalent to the choice between tf1 “ 0,f2 ă 0u and tf1 ă 0,f2 “ 0u, respectively. We will prove below that f2 ă 0, i.e., that the ﬁrst of these conditions is realized for all n and s under consideration.

The equality f1 “ 0 gives λ “

bpn ` 2q pα20 ` 2α0α1qpn ` 2q ` 3 “

![image 469](<2021-barg-bounds-sum-distances-spherical_images/imageFile469.png>)

pn ` 2qpL1pα0qpα21 ´ α20q ´ 2α0pLpα1q ´ Lpα0qqq pα1 ´ α0q2ppα20 ` 2α0α1qpn ` 2q ` 3q

. Then

![image 470](<2021-barg-bounds-sum-distances-spherical_images/imageFile470.png>)

A3pLpα1q ´ Lpα0qq ` B3Lpα0q ´ C3L1pα0q B3

fp1q “ ´λp1 ´ α0q2p1 ´ α1q ` a ` b ` c “

, where

![image 471](<2021-barg-bounds-sum-distances-spherical_images/imageFile471.png>)

- A3 “ p1 ´ α0q2ppn ` 2qp1 ` α0q2 ´ n ` 1q “

pn ´ 1qppn ` 1qs ` 2q2ppn ´ 2qs2 ´ 2ns ´ 1q p1 ` nsq4

![image 472](<2021-barg-bounds-sum-distances-spherical_images/imageFile472.png>)

,

- B3 “ pα1 ´ α0q2ppα20 ` 2α0α1qpn ` 2q ` 3q

“ ´

p1 ` 2s ` ns2q2p2npn ` 2qs3 ´ pn2 ´ 5n ´ 2qs2 ´ 6ns ´ n ´ 5q p1 ` nsq4

![image 473](<2021-barg-bounds-sum-distances-spherical_images/imageFile473.png>)

,

- C3 “ p1 ´ α0qp1 ´ α1qpα1 ´ α0qppn ` 2qpα0 ` α1 ` α0α1q ` 3q


pn ´ 1qp1 ´ sqppn ` 1qs ` 2qp1 ` 2s ` ns2qppn ` 2qs2 ` 2s ´ 1q p1 ` nsq3

“

.

![image 474](<2021-barg-bounds-sum-distances-spherical_images/imageFile474.png>)

Therefore

ppn ` 1qs ` 2q”p1 ´ sqp1 ` nsqA4 ` B4

ı

![image 475](<2021-barg-bounds-sum-distances-spherical_images/imageFile475.png>)

ap1 ´ sqB5

p1 ` 2s ` ns2q2C4?2B5

fp1q “

, where A4, B4, B5 and C4 are as given in Equation (20) in Section 2.

![image 476](<2021-barg-bounds-sum-distances-spherical_images/imageFile476.png>)

![image 477](<2021-barg-bounds-sum-distances-spherical_images/imageFile477.png>)

Substituting these parameters into (46) and performing simpliﬁcations, we eventually obtain (18):

¸ ,

˜pN ´ N1qfp1q ´

![image 478](<2021-barg-bounds-sum-distances-spherical_images/imageFile478.png>)

a

2p1 ´ sqppn ` 1qs ` 2qpA2 ` 2p1 ` nsq2B2q p1 ` 2s ` ns2qp1 ´ ns2q

N

N N1

ELpn,N,sq ď

![image 479](<2021-barg-bounds-sum-distances-spherical_images/imageFile479.png>)

![image 480](<2021-barg-bounds-sum-distances-spherical_images/imageFile480.png>)

˜

¸,

![image 481](<2021-barg-bounds-sum-distances-spherical_images/imageFile481.png>)

a

Np1 ´ ns2q np1 ´ sqppn ` 1qs ` 2q

2p1 ´ sqppn ` 1qs ` 2qpA2 ` 2p1 ` nsq2B2q p1 ` 2s ` ns2qp1 ´ ns2q

A5fp1q 1 ´ ns2 ´

N

“

![image 482](<2021-barg-bounds-sum-distances-spherical_images/imageFile482.png>)

![image 483](<2021-barg-bounds-sum-distances-spherical_images/imageFile483.png>)

![image 484](<2021-barg-bounds-sum-distances-spherical_images/imageFile484.png>)

![image 485](<2021-barg-bounds-sum-distances-spherical_images/imageFile485.png>)

![image 486](<2021-barg-bounds-sum-distances-spherical_images/imageFile486.png>)

a

a

N2

2p1 ´ sqppn ` 1qs ` 2qpA2 ` 2p1 ` nsq2B2q np1 ´ sqppn ` 1qs ` 2qp1 ` 2s ` ns2q

p1 ´ sqB5q np1 ´ sqp1 ` 2s ` ns2q2C4?2B5 ´

NA5pp1 ´ sqp1 ` nsqA4 ` B4

“

,

![image 487](<2021-barg-bounds-sum-distances-spherical_images/imageFile487.png>)

![image 488](<2021-barg-bounds-sum-distances-spherical_images/imageFile488.png>)

![image 489](<2021-barg-bounds-sum-distances-spherical_images/imageFile489.png>)

![image 490](<2021-barg-bounds-sum-distances-spherical_images/imageFile490.png>)

![image 491](<2021-barg-bounds-sum-distances-spherical_images/imageFile491.png>)

a

ap1 ´ sqB5q np1 ´ sqp1 ` 2s ` ns2q2C4?2B5 ´

N2

2p1 ´ sqpA2 ` 2p1 ` nsq2B2q np1 ´ sqp1 ` 2s ` ns2q

NA5pp1 ´ sqp1 ` nsqA4 ` B4

?B5

“

,

![image 492](<2021-barg-bounds-sum-distances-spherical_images/imageFile492.png>)

![image 493](<2021-barg-bounds-sum-distances-spherical_images/imageFile493.png>)

![image 494](<2021-barg-bounds-sum-distances-spherical_images/imageFile494.png>)

![image 495](<2021-barg-bounds-sum-distances-spherical_images/imageFile495.png>)

p1 ´ sqB5q ´ 2Np1 ` 2s ` ns2qC4?A6s np1 ´ sqp1 ` 2s ` ns2q2C4?2B5

![image 496](<2021-barg-bounds-sum-distances-spherical_images/imageFile496.png>)

a

![image 497](<2021-barg-bounds-sum-distances-spherical_images/imageFile497.png>)

NrA5pp1 ´ sqp1 ` nsqA4 ` B4

“

,

![image 498](<2021-barg-bounds-sum-distances-spherical_images/imageFile498.png>)

![image 499](<2021-barg-bounds-sum-distances-spherical_images/imageFile499.png>)

where Ai, Bi, and Ci are as given in (20). The condition f2 ă 0 is equivalent to λp2α0 ` sq ` a ă 0. This gives the inequality 6B6

![image 500](<2021-barg-bounds-sum-distances-spherical_images/imageFile500.png>)

ap1 ´ sqp1 ` nsqppn ` 1qs ` 2q ´ C6 C4 ă 0,

![image 501](<2021-barg-bounds-sum-distances-spherical_images/imageFile501.png>)

where

B6 “ pn ´ 2qpn ` 1qs2 ´ 4s ´ n ´ 1, C6 “ n3pn ` 2qs6 ` 3n2pn ` 2qs5 ´ 3npn2 ´ n ´ 2qs4 ` 2p3n3 ´ 6n2 ´ 8n ´ 4qs3 `

3p3n2 ´ 16n ´ 14qs2 ´ 3p2n2 ` 5n ` 18qs ´ 11n ´ 13.

?n ` 3q{pn ` 2q (just use that s ă 1{

We have C4 ă 0 since 2npn ` 2qs3 ă n ` 5 follows for n ě 3 and 0 ă s ă p´1 `

![image 502](<2021-barg-bounds-sum-distances-spherical_images/imageFile502.png>)

?n ` 2). It remains to see that 6B6

![image 503](<2021-barg-bounds-sum-distances-spherical_images/imageFile503.png>)

a

![image 504](<2021-barg-bounds-sum-distances-spherical_images/imageFile504.png>)

p1 ´ sqp1 ` nsqppn ` 1qs ` 2q ą C6. Since B6 ă 0 for 0 ă s ă p´1`

?n ` 3q{pn `2q, we need to prove that C62 ą 36B62p1 ´ sqp1 `nsqppn `1qs ` 2q. This inequality is reduced to an 8-degree polynomial (in s) inequality shown to hold true by a computer algebra system.

![image 505](<2021-barg-bounds-sum-distances-spherical_images/imageFile505.png>)

Acknowledgements. We thank the referees for spending time and effort on our manuscript and for providing an extensive set of remarks which improved the exposition.

REFERENCES

- [1] J. R. Alexander, On the sum of distances between n points on the sphere, Acta Math. Hungar. 23 (1972), no. 3-4, 443–448.
- [2] I. Balla, F. Dra¨xler, P. Keevash, and B. Sudakov, Equiangular lines and spherical codes in Euclidean space, Invent. Math. 211

(2018), no. 1, 179–212.

- [3] E. Bannai and Et. Bannai, A note on the spherical embeddings of strongly regular graphs, European J. Comb. 26 (2005), 1177– 1179.
- [4] A. Barg, Stolarsky’s invariance principle for ﬁnite metric spaces, Mathematika 67 (2021), no. 1, 158–186.
- [5] A. Barg, A. Glazyrin, K. A. Okoudjou, and W.-H. Yu, Finite two-distance tight frames, Linear Algebra Appl. 475 (2015), 163–175.
- [6] J. Beck, Sums of distances between points on a sphere—an application of the theory of irregularities of distribution to discrete geometry, Mathematika 31 (1984), no. 1, 33–41.
- [7] J.J. Benedetto and M. Fickus, Finite normalized tight frames, Adv. Comput. Math. 18 (2003), no. 2–4, 357–385.
- [8] D. Bilyk, F. Dai, and R. Matzke, The Stolarsky principle and energy optimization on the sphere, Constr. Approx. 48 (2018), 31–60.
- [9] D. Bilyk and M.T. Lacey, One-bit sensing, discrepancy and Stolarsky’s principle, Sbornik: Mathematics 208 (2017), no. 6, 744– 763, Translation from the Russian, Mat. Sbornik, vol. 208, no. 6, pp.4–25.
- [10] D. Bilyk and R. W. Matzke, On the Fejes T´oth problem about the sum of angles between lines, Proc. Amer. Math. Soc. 147 (2019), no. 1, 51–59.
- [11] S. V. Borodachov, D. P. Hardin, and E. B. Saff, Discrete energy on rectiﬁable sets, Springer, 2019.
- [12] P. Boyvalenkov, D. Danev, and I. Landjev, On maximal spherical codes II, J. Combin. Des. 7 (1999), 316–326.
- [13] P. G. Boyvalenkov, P. D. Dragnev, D. P. Hardin, E. B. Saff, and M. M. Stoyanova, Universal upper and lower bounds on energy of spherical designs, Dolomites Res. Notes Approx. 8 (2015), 51–65.
- [14] , Universal lower bounds for potential energy of spherical codes, Constr. Approx. 44 (2016), no. 3, 385–415.

![image 506](<2021-barg-bounds-sum-distances-spherical_images/imageFile506.png>)

- [15] , Energy bounds for codes in polynomial metric spaces, Anal. Math. Phys. 9 (2019), no. 2, 781–808.

![image 507](<2021-barg-bounds-sum-distances-spherical_images/imageFile507.png>)

- [16] , Upper bounds for energies of spherical codes of given cardinality and separation, Des. Codes Cryptogr. 88 (2020), no. 9, 1811–1826.

![image 508](<2021-barg-bounds-sum-distances-spherical_images/imageFile508.png>)

- [17] J. S. Brauchart, D. P. Hardin, and E. B. Saff, The next-order term for optimal Riesz and logarithmic energy asymptotics on the sphere, Recent advances in orthogonal polynomials, special functions, and their applications, Contemp. Math., vol. 578, Amer. Math. Soc., Providence, RI, 2012, pp. 31–61.
- [18] J.S. Brauchart and J. Dick, A simple proof of Stolarsky’s invariance principle, Proc. Amer. Math. Soc. 141 (2013), 2085–2096.
- [19] A. E. Brouwer and H. Van Maldeghem, Strongly regular graphs, Encyclopedia of Mathematics and its Applications, vol. 182, Cambridge University Press, Cambridge, 2022.
- [20] A.E. Brouwer, SRG family parameters, https://www.win.tue.nl/ aeb/graphs/srghub.html.
- [21] A.E. Brouwer and W.H. Haemers, Spectra of graphs, Springer, New York, 2012.
- [22] R. Calderbank and W. M. Kantor, The geometry of two-weight codes, Bull. London Math. Soc. 18 (1986), no. 2, 97–122.
- [23] P.J. Cameron, J.M. Goethals, and J.J. Seidel, Strongly regular graphs having strongly regular subconstituents, J. Algebra 55 (1978), 257–280.
- [24] H. Cohn and A. Kumar, Universally optimal distribution of points on spheres, J. Amer. Math. Soc. 20 (2007), no. 1, 99–148.
- [25] D. de Caen, Large equiangular sets of lines in Euclidean space, Electron. J. Combin. 7 (2000), Research Paper 55, 3.
- [26] P. Delsarte, J. M. Goethals, and J. J. Seidel, Spherical codes and designs, Geometriae Dedicata 6 (1977), 363–388.
- [27] C. Ding, A construction of binary linear codes from Boolean functions, Discrete Math. 339 (2016), no. 9, 2288–2303.
- [28] T. Ericson and V. Zinoviev, Codes on Euclidean spheres, Elsevier Science, Amsterdam e.a., 2001.
- [29] L. Fejes To´th, On the sum of distances determined by a pointset, Acta Math. Acad. Sci. Hungar. 7 (1956), 397–401.
- [30] A. Glazyrin and W.-H. Yu, Upper bounds for s-distance sets and equiangular lines, Adv. Math. 330 (2018), 810–833.


- [31] C. Godsil and G. Royle, Algebraic graph theory, Graduate Texts in Mathematics, vol. 207, Springer-Verlag, New York, 2001.
- [32] X. Hou and J. Shao, Spherical distribution of 5 points with maximal distance sum, Discrete Comput. Geom. 46 (2011), no. 1, 156–174.
- [33] J. Jedwab and A. Wiebe, Large sets of complex and real equiangular lines, J. Combin. Theory Ser. A 134 (2015), 98–102.
- [34] Z. Jiang and A. Polyanskii, Forbidden subgraphs for graphs of bounded spectral radius, with applications to equiangular lines, Israel J. Math. 236 (2020), no. 1, 393–421.
- [35] Z. Jiang, J. Tidor, Y. Yao, S. Zhang, and Y. Zhao, Equiangular lines with a ﬁxed angle, Ann. of Math. (2) 194 (2021), no. 3, 729–743.
- [36] A. V. Kolushov and V. A. Yudin, Extremal dispositions of points on the sphere, Anal. Math. 23 (1997), no. 1, 25–34.
- [37] A. B. J. Kuijlaars and E. B. Saff, Asymptotics for minimal discrete energy on the sphere, Trans. Amer. Math. Soc. 350 (1998), no. 2, 523–538.
- [38] P. W. H. Lemmens and J. J. Seidel, Equiangular lines, J. Algebra 24 (1973), 494–512.
- [39] V. I. Levenshtein, Bounds for packings of metric spaces and some of their applications, Problemy Kibernet. 40 (1983), 43–110 (In Russian).
- [40] , Designs as maximum codes in polynomial metric spaces, Acta Applicandae Math. 25 (1992), 1–82.

![image 509](<2021-barg-bounds-sum-distances-spherical_images/imageFile509.png>)

- [41] , Universal bounds for codes and designs, Handbook of Coding Theory (V. Pless and W. C. Huffman, eds.), vol. 1, Elsevier Science, Amsterdam, 1998, pp. 499–648.

![image 510](<2021-barg-bounds-sum-distances-spherical_images/imageFile510.png>)

- [42] K. Li, C. Li, T. Helleseth, and L. Qu, Binary linear codes with few weights from two-to-one functions, IEEE Trans. Inform. Theory 67 (2021), no. 7, 4263–4275.
- [43] F. J. MacWilliams and N. J. A. Sloane, The theory of error-correcting codes, North-Holland, Amsterdam, 1991.
- [44] A. Neumaier, Graph representations, two-distance sets, and equiangular lines, Linear Algebra Appl. 114/115 (1989), 141–156.
- [45] V.M. Sidel’nikov, The mutual correlation of sequences, Soviet Math. Dokl. 12 (1971), 197–201.
- [46] M. M. Skriganov, Point distributions in two-point homogeneous spaces, Mathematika 65 (2019), no. 3, 557–587.
- [47] , Stolarsky’s invariance principle for projective spaces, J. Complexity 56 (2020), 101428.

![image 511](<2021-barg-bounds-sum-distances-spherical_images/imageFile511.png>)

- [48] K. B. Stolarsky, Sums of distances between points on a sphere, II, Proc. AMS 41 (1973), 575–582.
- [49] S. Waldron, On the construction of equiangular frames from graphs, Linear Algebra Appl. 431 (2009), no. 11, 2228–2242.
- [50] S. F. D. Waldron, An introduction to ﬁnite tight frames, Applied and Numerical Harmonic Analysis, Birkha¨user/Springer, New York, 2018.
- [51] X. Wang, D. Zheng, L. Hu, and X. Zeng, The weight distributions of two classes of binary cyclic codes, Finite Fields Appl. 34

(2015), 192–207.

- [52] V. A. Yudin, The minimum of potential energy of a system of point charges, Discrete Math. Appl. 3 (1993), no. 1, 75–81, Translation from the Russian, Diskretnaya Matematika, vol.4, no. 2, 1992, pp. 115–121.


