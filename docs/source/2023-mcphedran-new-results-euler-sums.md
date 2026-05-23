---
type: source
kind: paper
title: New Results for Euler Sums
authors: Ross C. McPhedran, David H. Bailey
year: 2023
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2311.06294v4
source_local: ../raw/2023-mcphedran-new-results-euler-sums.pdf
topic: general-knowledge
cites:
---

# arXiv:2311.06294v4[math.NT]28Jul2025

## New results for Euler sums

Ross C. McPhedran, School of Physics, University of Sydney, and David H. Bailey, Lawrence Berkeley National Laboratory

July 30, 2025

Abstract

We present a large number of analytic evaluations of Euler sums, namely sums such as

∞

H(k)m kn0(k + 1)n1(k + 2)n2

M(m, n0, n1, n2, . . . , nt) =

,

· · · (k + t)nt

k=1

for nonnegative integers m and (ni), with m ≥ 1 and n0 +n1 +· · ·+nt ≥ 2, where H(k) = kj=1 1/j is the harmonic function. These results were obtained either by algebraic manipulations, or else by

very high-precision numerical evaluations combined with an integer relation algorithm to obtain the analytic formulas. We show how many of these results can be derived from a few basic facts, and that these techniques are applicable to Euler sums of even more general forms than the above cases. We then show that these results permit the calculation of constants for Euler sums resembling the Stieltjes γ constants arising in the theory of the Riemann zeta function, and we also present some preliminary results on the asymptotic behavior of these constants.1

### 1 Introduction

The investigations reported here had their origins in work [1] on the Keiper-Li criterion for the Riemann hypothesis [2, 3]. The Keiper-Li criterion involves positive valued coefficients an arising in expansions of the Riemann zeta function. The new representation of the an reported in [1] involved a combination of two sets of coefficients Cn,p and Σξp, again positive valued. This representation enabled the accurate calculation of the first 4000 coefficients an. The coefficients Cn,p obeyed a recurrence relation, and had representations involving the classical Euler sums. A deeper understanding of the asymptotic behaviour of the Cn,p as the two integer parameters n and p tended to infinity was sought, and naturally involved results from the extensive literature on Euler sums [4]-[11].

In this paper we address Euler sums of the form

∞

M(m,n0,n1,n2,...,nt) =

k=1

H(k)m kn0(k + 1)n1(k + 2)n2

, (1)

···(k + t)nt

for nonnegative integers m and (ni), with m ≥ 1 and n0+n1+···+nt ≥ 2, where H(k) = Hk = kj=1 1/j is the harmonic function (we use both notations interchangeably below). However, the techniques pre-

sented below are applicable to Euler sums of even more general forms. We focus on Euler sums having a common order r, where r = m + n0 + n1 + ··· + nt. We combine results from the literature with many new results, in an effort to say as much as possible about systems of order r ranging from 3 to 12. The complexity of these analyses increases rapidly with r.

1The authors dedicate this paper to the memory of Jonathan and Peter Borwein, two giants of mathematical research who recently passed away. Jonathan in particular investigated Euler sums in some earlier studies that we reference.

Among the most striking results of this paper are the linkages between Euler sums and Stieltjes constants. The latter can be defined by:

lim

n→∞

n

(log k)p k −

(log n)p+1 p + 1

k=1

= γp. (2)

The Stieltjes constants γp have a sign which varies in a complicated way as p increases and their modulus increases. We define their equivalent for Euler sums as

lim

n→∞

n

Hkp−1 k −

k=1

1 p

Hnp = γpH. (3)

Here the harmonic Stieltjes constants γpH are all positive, and again increase rapidly as p increases. The harmonic Stieltjes constants are shown to be given by a sum over a set of primitive sums which form a basis for the Euler sums of order p.

### 2 Previous results on Euler Sums

We now present selected results from the literature on Euler sums, including relatively recent results due to the late Jonathan Borwein and collaborators [8, 9], which were obtained using the techniques of experimental mathematics to complement analysis. Two of the sets of sums they consider are:

∞

sh(m,n) =

k=1

∞

σh(m,n) =

k=1

Hkm (k + 1)n

(4)

Hk(m) (k + 1)n

, (5)

where Hk(m) = kj=1 1/jm. We define slight modifications of these:

∞

Ih(m,n) =

k=1

∞

Hkm kn

, Jh(m,n) =

k=1

Hk(m) kn

. (6)

Then [8]:

∞

Jh(m,n) =

k=1

Hk(m) kn

= σh(m,n) + ζ(m + n), (7)

where ζ(p) = k≥1 1/kp is the Riemann zeta function. For m = 1, this is

Ih(1,n) − sh(1,n) = ζ(n + 1). (8) For the special case m = 2 under particular investigation in [8, 9],

Ih(2,n) − sh(2,n) = 2Ih(1,n + 1) − ζ(n + 2) = 2sh(1,n + 1) + ζ(n + 2). (9) For both these cases, the right-hand side tends down to unity as n → ∞.

The sums Ih(n,p) can be represented in terms of the sh(m,n) as follows:

∞

n

Hkn kp

n m

sh(m,p + n − m). (10)

Ih(n,p) =

= ζ(n + p) +

m=1

We can define the order of this expression to be n + p, i.e., the sum of the powers of Hk and k on the left-hand side. The sum of the arguments of sh on the right-hand side is also n + p. The dual expression to equation (10) is

∞

sh(n,p) =

k=1

n

Hkn (k + 1)p

= (−1)nζ(n + p) +

m=1

n m

(−1)m−nIh(m,p + n − m). (11)

Euler provided the solution for σh(1,m) = sh(1,m) and thus for Jh(1,m) = Ih(1,m) for all m ≥ 2:

m−2

- 1

- 2


m 2

ζ(m + 1) −

ζ(m − k)ζ(k + 1). (12)

σh(1,m) =

k=1

Another useful relationship is the reflection formula, valid for m,n ≥ 2:

σh(m,n) + σh(n,m) = ζ(m)ζ(n) − ζ(m + n), (13) or, written with different notation,

Jh(m,n) + Jh(n,m) = ζ(m)ζ(n) + ζ(m + n), (14) so that 2Jh(m,m) = ζ(m)2 + ζ(2m) for m ≥ 2.

Euler [9] was able to derive the following expansions in terms of zeta functions, for the particular case where the sum of parameters s + t is odd, and t > 1. The first is for s odd, t even:

σh(s,t) =

For s even, t odd:

- 1

- 2


s + t s − 1 ζ(s + t) + ζ(s)ζ(t)

(s+t−1)/2

2j − 2 s − 1

2j − 2 t − 1

ζ(2j − 1)ζ(s + t − 2j + 1). (15)

−

+

j=2

- 1

- 2


s + t s

σh(s,t) = −

(s+t−1)/2

+

j=2

A valuable result derived in [9] is:

+ 1 ζ(s + t)

2j − 2 s − 1

+

2j − 2 t − 1

ζ(2j − 1)ζ(s + t − 2j + 1). (16)

sh(2,2n − 1) =

n−2

1 6

- 1

- 2


(2n2 − 7n − 3)ζ(2n + 1) + ζ(2)ζ(2n − 1) −

(2k − 1)ζ(2n − 1 − 2k)ζ(2k + 2)

k=1

n−2

n−2−k

1 3

ζ(2j + 1)ζ(k + 1 − j)ζ(2n − 1 − 2k − 2j). (17)

ζ(2k + 1)

+

j=1

k=1

Table 5 of [8] gives a list of sums sh for which the authors were unable to find representations in terms of zeta functions or zeta functions complemented by powers of logarithms of integers and polylogarithms of argument 1/2, using various search algorithms. These results highlight the difficulty of finding closed form representations of all the Euler-type sums arising in treatments of the sums Cn,p for p large.

The literature on Euler sums [5]-[11] concentrates on the sums sh(m,n), σh(m,n), Ih(m,n) and Jh(m,n). Below we will analyze the mixed sums M(m,n,p,q), which include the existing results for sh(m,n) (setting n = q = 0) and Ih(m,n) (setting p = q = 0) as special cases. The results we present in

Appendix 2 include literature results up to order 7, extend them to orders 8–11 and also include selected results for order 12, as well as adding many extra results of all orders (inter alia for p,q ̸= 0).

Note that the extension to orders larger than 7 is not straightforward. Order 8 was painstakingly investigated by Bailey, Borwein and Girgensohn [8], and only the single analytic result for Ih(1,7) was found. By refining and extending the numerical methods used, and regarding Ih(2,6) as a known quantity, we have been able to obtain all the other sums for order eight in closed form, as reported in Appendix 2. Similar methods have been applied for orders 9, 10, 11 and 12, with the addition of the sums Ih(2,6), Ih(2,8), Ih(3,8), Ih(2,10), Ih(4,8) to the set of assumed constants. In Apppendix 1, the numerical values of these five assumed constants are given to 400 figures accuracy.

Some evaluations of I(m,n) are now presented [5, 8, 9, 4, 11], arranged according to the order m+n (in the remainder of this section we will drop the h subscript on Ih). For order 3, there is only one:

∞

H(k) k2

Ih(1,2) =

= 2ζ(3). (18)

k=1

- For order 4, there are two:

Ih(1,3) =

∞

k=1

H(k) k3

=

1 4

(5ζ(4)), Ih(2,2) =

∞

k=1

H(k)2 k2

=

1 4

(17ζ(4)). (19)

- For order 5, there are three:

Ih(1,4) =

∞

k=1

H(k) k4

= 3ζ(5) − ζ(2)ζ(3), Ih(2,3) =

∞

k=1

H(k)2 k3

=

- 1

- 2


(7ζ(5) − 2ζ(2)ζ(3)),

Ih(3,2) =

∞

k=1

H(k)3 k2

= 10ζ(5) + ζ(2)ζ(3). (20)

- For order 6, there are four: ∞

k=1

H(k) k5

=

1 4

7ζ(6) − 2ζ(3)2 ,

∞

k=1

H(k)2 k4

=

1 24

97ζ(6) − 48ζ(3)2 ,

∞

k=1

H(k)3 k3

=

1 16

93ζ(6) − 40ζ(3)2 ,

∞

k=1

H(k)4 k2

=

1 24

979ζ(6) + 72ζ(3)2 . (21)

- For order 7, there are five:


- Ih(1,6) =

∞

k=1

H(k) k6

= −ζ(4)ζ(3) − ζ(2)ζ(5) + 4ζ(7),

- Ih(2,5) =

∞

k=1

H(k)2 k5

= −

5 2

ζ(4)ζ(3) − ζ(2)ζ(5) + 6ζ(7),

- Ih(3,4) =

∞

k=1

H(k)3 k4

=

693 48

ζ(7) + 2ζ(5)ζ(2) −

51 4

ζ(4)ζ(3),

- Ih(4,3) =

∞

k=1

H(k)4 k3

=

185 8

ζ(7) + 5ζ(5)ζ(2) −

43 2

ζ(4)ζ(3),

- Ih(5,2) =


∞

H(k)5 k2

2051 16

=

ζ(7) +

57 2

ζ(5)ζ(2) + 33ζ(4)ζ(3). (22)

For order eight, there is a paucity of results in the literature. A careful study of this case was given by Bailey, Borwein and Girgensohn [8]. It employed an Euler-Maclaurin scheme for the high-precision evaluation of these sums, an enhanced version of which we describe in Section 5 below. The only analytic formula we can give in complete form is one studied by Euler:

∞

H(k) k7

Ih(1,7) =

k=1

9 2

ζ(8) − ζ(6)ζ(2) − ζ(5)ζ(3) −

=

- 1

- 2


ζ(4)2, (23)

which can be simplified using the analytic expressions for ζ(2n) to

1 4

(9ζ(8) − 4ζ(3)ζ(5)). (24) We have been able to establish solutions for four additional I constants if we express them in terms

Ih(1,7) =

of the set of constants ζ(8), ζ(3)ζ(5) and ζ(2)ζ(3)2, together with I(2,6):

- Ih(3,5) =

1 96

595ζ(8) + 120ζ(2)ζ(3)2 − 576ζ(3)ζ(5) − 264I(2,6) (25)

- Ih(4,4) =

1 144 −14833ζ(8) − 4032ζ(2)ζ(3)2 + 16704ζ(3)ζ(5) + 3744I(2,6) (26)

- Ih(5,3) =

1 288

67811ζ(8) + 19080ζ(2)ζ(3)2 − 78768ζ(3)ζ(5) − 16920I(2,6) (27)

- Ih(6,2) =


1 8

5843ζ(8) − 328ζ(2)ζ(3)2 + 3896ζ(3)ζ(5) + 456I(2,6) (28)

An earlier study [8] gives the expansions for all sh(m,n) with m + n = 9, apart from those coming from (12) and (17). The basis of function values needed is ζ(9), ζ(2)ζ(7), ζ(3)ζ(6), ζ(4)ζ(5) and ζ(3)3, the last coming from the double sum in (17). These may be used with (10) to produce the following evaluations of I(m,n) for order m + n = 9:

- Ih(1,8) = 5ζ(9) − ζ(3)ζ(6) − ζ(4)ζ(5) − ζ(2)ζ(7) (29)
- Ih(2,7) =

1 6

55ζ(9) − 21ζ(3)ζ(6) − 15ζ(4)ζ(5) − 6ζ(2)ζ(7) + 2ζ(3)3 (30)

- Ih(3,6) =

1 24

521ζ(9) − 291ζ(3)ζ(6) − 306ζ(4)ζ(5) + 72ζ(2)ζ(7) + 48ζ(3)3 (31)

- Ih(4,5) =

1 12

436ζ(9) − 279ζ(3)ζ(6) − 258ζ(4)ζ(5) + 84ζ(2)ζ(7) + 40ζ(3)3 (32)

- Ih(5,4) =

1 72

9442ζ(9) − 14685ζ(3)ζ(6) + 4752ζ(4)ζ(5) + 2385ζ(2)ζ(7) − 360ζ(3)3 (33)

- Ih(6,3) =

1 24

7474ζ(9) − 13122ζ(3)ζ(6) + 6048ζ(4)ζ(5) + 1953ζ(2)ζ(7) − 544ζ(3)3 (34)

- Ih(7,2) =


1 72

276341ζ(9) + 88665ζ(3)ζ(6) + 143163ζ(4)ζ(5) + 59166ζ(2)ζ(7) + 4032ζ(3)3 (35)

The approximate numerical value of Ih(7,2) is 9043.54574728044; its integral estimate is 8976.6033415307.

We next present the first results we know of for order m + n = 10. We originally obtained these results using the method described in Section 5. The eight basic sums I are obtained with two sums Ih(2,6) and Ih(2,8) assumed known:

1 4

11ζ(10) − 4ζ(3)ζ(7) − 2ζ(5)2 (36)

Ih(1,9) =

1 160 −1661ζ(10) + 1280ζ(3)ζ(7) + 80ζ(3)2ζ(4) − 560ζ(2)ζ(3)ζ(5) + 720ζ(5)2

Ih(3,7) =

+520I(2,8)) (37)

- Ih(4,6) =

1 640 −68823ζ(10) + 60000ζ(3)ζ(7) + 1000ζ(3)2ζ(4) − 21680ζ(2)ζ(3)ζ(5)

+23560ζ(5)2 + 12120I(2,8) + 1280ζ(2)I(2,6) (38)

- Ih(5,5) =

1 256

64433ζ(10) − 57760ζ(3)ζ(7) + 360ζ(3)2ζ(4) + 20560ζ(2)ζ(3)ζ(5) −22648ζ(5)2 − 10920I(2,8) − 1280ζ(2)I(2,6) (39)

- Ih(6,4) =

1 128 −271367ζ(10) + 176560ζ(3)ζ(7) − 84648ζ(3)2ζ(4) − 400ζ(2)ζ(3)ζ(5)

+121688ζ(5)2 + 34376I(2,8) + 15040ζ(2)I(2,6) (40)

- Ih(7,3) =

1 2560

16614991ζ(10) − 10315520ζ(3)ζ(7) + 5879160ζ(3)2ζ(4) − 705040ζ(2)ζ(3)ζ(5) −7710760ζ(5)2 − 2021880I(2,8) − 1008000ζ(2)I(2,6) (41)

- Ih(8,2) =


1 480

18741581ζ(10) + 6689520ζ(3)ζ(7) − 524640ζ(3)2ζ(4) + 1452480ζ(2)ζ(3)ζ(5)

+4247040ζ(5)2 + 485280I(2,8) + 299520ζ(2)I(2,6) (42)

We now present results for order m + n = 11, which again are new in this study, and which again were originally found by us using the methods described below in Section 5. These formulas involve the two sums I(2,6) and I(3,8).

- Ih(1,10) = 6ζ(11) − ζ(2)ζ(9) − ζ(3)ζ(8) − ζ(4)ζ(7) − ζ(5)ζ(6) (43)
- Ih(2,9) =


- 1

- 2


26ζ(11) − 2ζ(2)ζ(9) − 9ζ(3)ζ(8) − 5ζ(4)ζ(7) − 7ζ(5)ζ(6) + 2ζ(3)2ζ(5) (44)

- Ih(4,7) =

1 48

(−2877ζ(11) − 272ζ(2)ζ(9) + 1190ζ(3)ζ(8) + 1212ζ(4)ζ(7) + 1018ζ(5)ζ(6)

+80ζ(2)ζ(3)3 − 576ζ(3)2ζ(5) + 176I(3,8) (45)

- Ih(5,6) =

1 576

(−781671ζ(11) − 88016ζ(2)ζ(9) + 296660ζ(3)ζ(8) + 411984ζ(4)ζ(7) +220080ζ(5)ζ(6) + 21120ζ(2)ζ(3)3 − 141120ζ(3)2ζ(5) + 8640ζ(3)I(2,6)

+27840I(3,8)) (46)

- Ih(6,5) =

1 192

(734643ζ(11)83472ζ(2)ζ(9) − 271244ζ(3)ζ(8) − 395088ζ(4)ζ(7) −205424ζ(5)ζ(6) − 19360ζ(2)ζ(3)3 + 130176ζ(3)2ζ(5) − 9120ζ(3)I(2,6) −25600I(3,8)) (47)

- Ih(7,4) =

1 1152

(16370805ζ(11)1684144ζ(2)ζ(9) + 5889744ζ(3)ζ(8) − 10724760ζ(4)ζ(7) −10480104ζ(5)ζ(6) + 844032ζ(2)ζ(3)3 − 2330496ζ(3)2ζ(5) − 1431360ζ(3)I(2,6) −630336I(3,8)) (48)

- Ih(8,3) =

1 72

(2824380ζ(11)277304ζ(2)ζ(9) + 1926401ζ(3)ζ(8) − 1998972ζ(4)ζ(7) −2270310ζ(5)ζ(6) + 243648ζ(2)ζ(3)3 − 803808ζ(3)2ζ(5) − 341280ζ(3)I(2,6) −113760I(3,8)) (49)

- Ih(9,2) =


1 64

(7739347ζ(11) + 2048432ζ(2)ζ(9) + 5357920ζ(3)ζ(8)

+8811792ζ(4)ζ(7) + 10526056ζ(5)ζ(6) − 294208ζ(2)ζ(3)3 + 2064192ζ(3)2ζ(5)

+540096ζ(3)I(2,6) + 199936I(3,8)) (50)

Finally, we present results for order m + n = 12, which as before are new to this study, having been originally obtained by us using the methods described in Section 5. These results involve the two sums Ih(2,10) and Ih(4,8):

∞

1 4

H(k) k11

(13ζ(12) − 4ζ(3)ζ(9) − 4ζ(5)ζ(7)) (51)

=

k=1

∞

H(k)3 k9

1 22112

(355355ζ(12) − 221120ζ(3)ζ(9) − 265344ζ(5)ζ(7)

=

k=1

−33168ζ(3)2ζ(6) + 5528ζ(3)4 + 49752ζ(2)ζ(5)2 + 99504ζ(2)ζ(3)ζ(7) −82920I(2,10)) (52)

∞

H(k)5 k7

1 265344

(3612841ζ(12) − 884480ζ(3)ζ(9) − 597024ζ(5)ζ(7)

=

k=1

+364848ζ(3)2ζ(6) + 221120ζ(3)4 + 364848ζ(2)ζ(5)2 + 729696ζ(2)ζ(3)ζ(7) −3250464ζ(3)ζ(4)ζ(5) − 1028208I(2,10) + 663360I(4,8)) (53)

∞

H(k)6 k6

1 530688

(−4262917573ζ(12) + 2820739392ζ(3)ζ(9) + 2446737024ζ(5)ζ(7)

=

k=1

+112663404ζ(3)2ζ(6) − 41128320ζ(3)4 − 402626352ζ(2)ζ(5)2 −741769152ζ(2)ζ(3)ζ(7) − 205077744ζ(3)ζ(4)ζ(5) + 52538112ζ(4)I(2,6)

+84213552ζ(2)I(2,8) + 519676224I(2,10) − 22554240I(4,8)) (54)

∞

H(k)7 k5

1 1061376

(−29991036967ζ(12) + 19798731008ζ(3)ζ(9) + 17219233536ζ(5)ζ(7)

=

k=1

+722473668ζ(3)2ζ(6) − 292232192ζ(3)4 − 2832315024ζ(2)ζ(5)2 −5220245184ζ(2)ζ(3)ζ(7) − 1329671952ζ(3)ζ(4)ζ(5) + 381697344ζ(4)I(2,6)

+589494864ζ(2)I(2,8) + 3662808576I(2,10) − 167166720I(4,8)) (55)

∞

H(k)8 k4

1 199008

(−6469168763ζ(12) − 4417645920ζ(3)ζ(9) + 2316436536ζ(5)ζ(7)

=

k=1

−7185432600ζ(3)2ζ(6) + 210815808ζ(3)4 + 2292190728ζ(2)ζ(5)2

+3705761136ζ(2)ζ(3)ζ(7) + 4396086720ζ(3)ζ(4)ζ(5) + 2171077776ζ(4)I(2,6)

+241230864ζ(2)I(2,8) − 842782296I(2,10) + 116552352I(4,8)) (56)

∞

H(k)9 k3

1 176896

(4340755723ζ(12) − 37498812096ζ(3)ζ(9) − 8003239392ζ(5)ζ(7)

=

k=1

−29417337684ζ(3)2ζ(6) + 1136645248ζ(3)4 + 12010630320ζ(2)ζ(5)2

+20062394496ζ(2)ζ(3)ζ(7) + 18880585488ζ(3)ζ(4)ζ(5) + 8292663360ζ(4)I(2,6)

+375428592ζ(2)I(2,8) − 7045878240I(2,10) + 635233536I(4,8)) (57)

∞

H(k)10 k2

1 176896

=

(702828643635ζ(12) + 39514453568ζ(3)ζ(9) + 93510608736ζ(5)ζ(7)

k=1

−23538514220ζ(3)2ζ(6) + 2706951040ζ(3)4 + 35094519056ζ(2)ζ(5)2

+62104868800ζ(2)ζ(3)ζ(7) + 96955381936ζ(3)ζ(4)ζ(5) + 16400028160ζ(4)I(2,6)

+954077520ζ(2)I(2,8) − 12973442080I(2,10) + 1115329280I(4,8)) (58)

|m 1|Ih(m,2) 2.4041138063|Formula (60) 1.5772156649|ratio 0.656048|
|---|---|---|---|
|2|4.5998737432|3.4876092536|0.758196|
|3|12.346581901|10.655143277|0.863003|
|4|45.833941465|42.731580639|0.932313|
|5|220.80305576|213.72197848|0.967930|
|6|1302.2827194|1282.3688561|0.984708|
|7|9043.5457472|8976.6033415|0.992597|
|8|72074.045293|71812.839054|0.996375|
|9|647472.79308|646315.55860|0.998212|


Table 1: The sums Ih(m,2) are compared with their integral approximation (60), together with ratios.

#### 2.1 Asymptotics of the sum Ih(m,2)

The summands of the Euler sums Ih(m,n) are always positive, and increase as m increases, while decreasing as n increases. The values of sums depending on the I(m,n) discussed in this paper tend to be dominated by the lowest sum I(m,2) for large values of m, and so it is valuable to have asymptotic approximations for it. The value of the sum can be well estimated by an integral, given that the maximum of the truncated summand (log k+γ)m/k2 occurs for k = exp(m/2), large enough for the discrete sum to be well approximated by the corresponding integral. For a general positive integer q, the result follows from the recursion

∞

(log k + γ)q+1 dk k2

= γq+1 + (q + 1)Nq, N1 = 1 + γ, (59) where γ = 0.5772156649... is Euler’s constant. This recurrence can be solved exactly, giving

Nq+1 =

1

∞

(log k + γ)m k2

dk = m![eγ]m . (60) Here we have introduced the notation for the truncated exponential:

1

m

[eγ]m = 1 +

q=1

γq q!

. (61)

Note that for large m, Nm/m! → exp(γ).

Although the integral in equation (60) is exactly evaluated, its use in approximating the sums I(m,2) for m large depends on two approximations: the sum is well approximated by an integral, and the twoterm asymptotic series of the harmonic number function gives a sufficiently accurate representation for the integrand. These approximations are tested in Table 1, which shows that the integral approximation gains relative accuracy rapidly as m increases, until at m = 9 it is accurate to two parts in 1000.

### 3 Mixed Euler sums

In the previous sections, we have focused on the I sums, whose denominators are powers of k, and on the sh sums, which have powers of k +1. But one is immediately led to consider more general denominators, which have not been previously studied in the literature in any detail. To that end we now consider “mixed Euler sums,” namely sums such as

∞

M(m,n0,n1,n2,...,nt) =

k=1

H(k)m kn0(k + 1)n1(k + 2)n2

, (62)

···(k + t)nt

for nonnegative integers m and (ni), with m ≥ 1 and n0+n1+···+nt ≥ 2, where H(k) = Hk = kj=1 1/j is the harmonic function as before, and where r = m + n0 + n1 + ··· + nt is the order. It is clear that the sh and I sums are merely special cases: sh(m,n) = M(m,0,n) and I(m,n) = M(m,n), so hereafter we will use the M notation. We first demonstrate, by means of examples, why Euler sums with more complicated denominators can be reduced to the basic M(m,n) cases.

Theorem 1. If the order of a mixed Euler sum of the form (62) is 12 or less, then it is expressible as a rational linear sum of terms chosen from the following list, depending on the order as shown (constants for a given order include all those of smaller orders, plus the listed “additional constants”):

Constants for order 3: 1, ζ(2), ζ(3) Additional constant for order 4: ζ(4)

- Additional constants for order 5: ζ(5), ζ(2)ζ(3)
- Additional constants for order 6: ζ(6), ζ(3)2
- Additional constants for order 7: ζ(7), ζ(2)ζ(5), ζ(3)ζ(4)
- Additional constants for order 8: ζ(8), ζ(2)ζ(3)2, ζ(3)ζ(5), M(2,6)
- Additional constants for order 9: ζ(9), ζ(2)ζ(7), ζ(3)ζ(6), ζ(4)ζ(5), ζ(3)3
- Additional constants for order 10: ζ(10), ζ(3)ζ(7), ζ(3)2ζ(4), ζ(2)ζ(3)ζ(5), ζ(5)2, ζ(2)M(2,6), M(2,8)
- Additional constants for order 11: ζ(11), ζ(2)ζ(9), ζ(3)ζ(8), ζ(4)ζ(7), ζ(5)ζ(6), ζ(2)ζ(3)3, ζ(5)ζ(3)2, ζ(3)M(2,6), M(3,8)
- Additional constants for order 12: ζ(12), ζ(3)ζ(9), ζ(5)ζ(7), ζ(2)ζ(5)2, ζ(2)ζ(3)ζ(7), ζ(3)ζ(4)ζ(5), ζ(3)2ζ(6), ζ(3)4, ζ(4)M(2,6), ζ(2)M(2,8), M(2,10), M(4,8)


Note: We conjecture that the representation of a order-12 or less mixed Euler sum as a rational linear combination of the constants in the list in Theorem 1 above is unique, since integer relation computations on this set rule out any relations with reasonable-sized coefficients (see next paragraph for details), but we have no proof of this. We also conjecture that a result similar to Theorem 1 applies for all higher orders: most likely it only remains to identify the appropriate “atoms,” akin to the list in Theorem 1.

We should also clarify that Theorem 1 relies in part on some results in the previous section that were obtained using the computational techniques described below in Section 5.

Note that the above list includes the constants M(2,6), M(2,8), M(3,8), M(2,10) and M(4,8). These constants appear to be linearly independent from the rest of the set, as indicated by the fact that a multipair PSLQ computer run (see Section 5) with the full set of order 8 constants shown above finds no integer relation with Euclidean norm less than 5.88·1022; the full set of order 10 constants above produces no integer relation with Euclidean norm less than 1.28·1013; and the full set of order 12 constants produces no integer relation with Euclidean norm less than 2.13 · 106. Nevertheless, the question of whether M(2,6), M(2,8), M(3,8), M(2,10) and M(4,8), singly or collectively, can be expressed analytically in terms of zetas or other well-known mathematical constants remains open. As an aid to further research, we include 400-digit values of these constants in Appendix 1 (Section 7).

Sketch of proof: We first observe (see Section 2 above) that each of the basic Euler sums M(m,n) = I(m,n) with order m+n ≤ 12 is reducible to a rational linear sum of the above-listed “atomic” constants. We now argue that any general mixed Euler sum (62) of order 12 or less can be reduced to a rational linear combination of the basic Euler sums M(m,n) of the same order or less, and thus to a rational linear combination of the constants in Theorem 1, by the application (possibly repeated) of these two algebraic techniques:

- 1. Changing sums with expressions involving (k +1), (k +2) or (k +w) for any integer w > 0 to sums involving only k, by means of a process akin to “completing the square” of elementary algebra.
- 2. Applying a partial fraction decomposition: Recall that any rational function can be written uniquely as the sum of terms based on the factorization of the denominator polynomial, as in the example


1 (k + 1)(k + 2)2

=

1 k + 1 −

1 k + 2 −

1 (k + 2)2

. (63)

This can be produced in Wolfram Mathematica by the command: Apart[1/((k+1)*(k+2)^2)]. To illustrate these techniques, note that one can write M(2,0,2) = ∞k=1 H(k)2/(k + 1)2 as

∞

H(k)2 (k + 1)2

- M(2,0,2) =


k=1

(1 + 1/2)2 32

(1 + 1/2 + 1/3)2 42

(1 + 1/2 + 1/3 + 1/4)2 52

1 22

+ ···

+

+

+

=

(1 + 1/2)2 22 −

(1 + 1/2 + 1/3)2 32 −

2/2 22 −

1/4 22

2/3(1 + 1/2) 32 −

1/9 32

=

+

(1 + 1/2 + 1/3 + 1/4)2 42 −

2/4(1 + 1/2 + 1/3) 42 −

1/16 42

+ ···

+

(1 + 1/2)2 22

(1 + 1/2 + 1/3)2 32

1 23

(1 + 1/2) 33 ··· −

1 24

1 34

+ ··· − 2

+ ···

=

+

+

+

∞

∞

H(k)2 k2 − 1 − 2

H(k) (k + 1)3 − (ζ(4) − 1)

=

k=1

k=1

= M(2,2) − 2M(1,0,3) − ζ(4). (64)

Note, crucially, that this manipulation rewrites the mixed Euler sum M(2,0,2) (of order 4) to an expression involving M(2,2) (of order 4), the mixed sum M(1,0,3) = ∞k=1 H(k)/(k + 1)3, (also of order 4), and the constant ζ(4) (again of order 4). A similar manipulation can now be performed on M(1,0,3):

∞

H(k) (k + 1)3

1 23

(1 + 1/2) 33

(1 + 1/2 + 1/3) 43

+ ···

M(1,0,3) =

=

+

+

k=1

(1 + 1/2) 23 −

1/2 23

(1 + 1/2 + 1/3) 33 −

1/3 33

+ ···

=

+

∞

H(k) k3 − 1 − (ζ(4) − 1)

=

k=1

= M(1,3) − ζ(4) = 5/4ζ(4) − ζ(4) = 1/4ζ(4), (65)

so that M(2,0,2) = M(2,2) − 2M(1,0,3) − ζ(4) = 17/4ζ(4) − 1/2ζ(4) − ζ(4) = 11/4ζ(4), which is of order 4. Note that none of these algebraic manipulations increased the order.

A second example of this technique is M(2,1,1) = k≥1 H(k)2/(k(k + 1)). Note that by employing a manipulation similar to that used above in (64) and (65), combined with the partial fraction decomposition

1 k −

1 k(k + 1)

=

1 k + 1

, (66)

this can be written

∞

- M(2,1,1) =


k=1

=

=

−

+

= 1 + 2

∞

H(k)2 k(k + 1)

H(k)2 k + 1

H(k)2 k −

=

k=1

(1 + 1/2)2 2

(1 + 1/2 + 1/3)2 3

(1 + 1/2)2 3

(1 + 1/2 + 1/3)2 4

1 1

- 1

- 2


+ ··· −

+ ···

+

+

+

+

(1 + 1/2)2 2

(1 + 1/2 + 1/3)2 3

1 1

+ ···

+

+

(1 + 1/2)2 2 −

(1 + 1/2 + 1/3)2 3 −

2/2 2 −

- 1/4

- 2


2/3(1 + 1/2) 3 −

1/9 3

+

(1 + 1/2 + 1/3 + 1/4)2 4 −

2/4(1 + 1/2 + 1/3) 4 −

1/16 4

+ ···

∞

H(k) (k + 1)2

+ (ζ(3) − 1) = 2M(1,2) + ζ(3) = 3ζ(3). (67)

k=1

Note again that none of these operations increased the order; in fact, in this case the order of the final result, namely 3, is less than the order of the original problem, namely 4.

Consider now a more complicated sum such as M(2,2,2) = k≥1 H(k)2/(k2(k + 1)2. Sums like this can be readily reduced by means of a partial fraction decomposition, which in this case is:

1 k2(k + 1)2

= −2

1 k −

1 k + 1

1 k2

1 (k + 1)2

+

+

, (68)

so that

∞

H(k)2 k2(k + 1)2

M(2,2,2) =

k=1

∞

∞

∞

H(k)2 (k + 1)2

H(k)2 k2

1 k −

1 k + 1

H(k)2

= −2

+

+

k=1

k=1

k=1

= −6ζ(3) + 17/4ζ(4) + 11/4ζ(4)

= 7ζ(4) − 6ζ(3), (69) where we have employed results from (64), (65) and (67) above.

One example involving (k+2) is M(2,0,0,2) = k≥1 H(k)2/(k+2)2. This can be reduced as follows (omitting details of some intermediate evaluations using the above techniques):

M(2,0,0,2) =

=

=

+

+

∞

H(k)2 (k + 2)2

k=1

(1 + 1/2)2 42

(1 + 1/2 + 1/3)2 52

(1 + 1/2 + 1/3 + 1/4)2 62

12 32

+ ···

+

+

+

(1 + 1/2 + 1/3)2 32 −

(1/2 + 1/3)2 32

2(1/2 + 1/3) 32 −

(1/2 + 1/3 + 1/4)2 42 −

(1/3 + 1/4)2 42

2(1 + 1/2)(1/3 + 1/4) 42 −

(1/4 + 1/5)2 52

1/2 + 1/3 + 1/4 + 1/5)2 52 −

2(1 + 1/2 + 1/3)(1/4 + 1/5) 52 −

+ ···

∞

∞

∞

∞

H(k)2 k2 − 2

H(k) (k + 1)(k + 2)2 − 2

H(k) (k + 2)3 −

1 (k + 1)2(k + 2)2

=

k=1

k=1

k=1

k=3

∞

∞

1 (k + 1)(k + 2)3 −

1 (k + 2)4

− 2

k=1

k=1

25 16

17 4

1 4

= −

ζ(4) − 2(3 − ζ(2) − ζ(3)) − 2 −3 + ζ(2) + ζ(3) +

+

ζ(4)

13 4

23 8 − ζ(2) − ζ(3) − −

17 16

− −

+ 2ζ(2) − 2

+ ζ(4)

11 4

= −3 + 2ζ(3) +

ζ(4) (70) The same techniques work for denominators involving (k + w) for any integer w > 2. For example,

after rather laborious effort one can deduce that

∞

H(k)2 (k + 4)2

1 3456

(−1045 + 288ζ(2) + 648ζ(3)). (71)

M(2,0,0,0,0,2) =

=

k=1

We should note, however, that the algebraic manipulations required in these evaluations grow very sharply in complexity with increasing powers of H(k) in the numerator and increasing terms in the denominator. Thus we have found, quite frankly, that in most cases these analytic formulas are more easily obtained by the computational methods we describe below in Section 5.

### 4 Euler sum analogues to the Stieltjes constants

##### As an application of these techniques, we address a finite Euler sum result from Choi and Srivastava[4]:

n−1

Hk k

=

k=1

- 1

- 2


Hn2−1 +

- 1

- 2


Hn(2)−1. (72)

(Note that in this section it is more convenient to use the subscript notation for the harmonic function: Hk = H(k).) We note also the following result from [7]:

n

n

Hk(2) k

= Hn(2)Hn −

k=1

k=1

Hk k2

+ Hn(3). (73)

This is easily generalised to an arbitrary harmonic number of order p:

n

n

Hk(p) k

= Hn(p)Hn −

k=1

k=1

Hk kp

+ Hn(p+1). (74)

We continue with the sums over a finite range, commencing with a result given in [6]:

n

n

Hk2 k

1 3

1 3

Hk k2

Hn3 −

Hn(3) +

. (75)

=

k=1

k=1

The method used to derive (75) employs Abel’s summation formula and may easily be generalised to higher values of p. When this was done, a pattern emerged for all the sums:

n

Hkp−1 k

=

k=1

- p−1
- q=2


1 p

Hnp + Dp,1Hn(p) +

Dp,q

n

Hkq−1 kp−q+1. (76)

k=1

| |p|Dp,q| |
|---|---|---|---|
| |2|1/2| |
| |3<br><br>|-1/3, 1| |
| |4<br><br>|1/4, -1, 3/2| |
| |5<br><br>|-1/5, 1, -2, 2| |
| |6<br><br>|1/6, -1, 5/2, -10/3, 5/2| |
| |7<br><br>|-1/7, 1, -3, 5, -5, 3| |
| |8|1/8, -1, 7/2, -7, 35/4, -7, 7/2| |
| |9<br><br>|-1/9, 1, -4, 28/3, -14, 14, -28/3, 4| |
| |10|1/10, -1, 9/2, -12, 21, -126/5, 21, -12, 9/2| |
| |11|-1/11, 1, -5, 15, -30, 42, -42, 30, -15, 5| |
| |12<br><br>|1/12, -1, 11/2, -55/3, 165/4, -66, 77, -66, 165/4, -55/3, 11/2| |
| |13<br><br>|-1/13, 1, -6, 22, -55, 99, -132, 132, -99, 55, -22, 6| |
| |14<br><br>|1/14, -1, 13/2, -26, 143/2, -143, 429/2, -1716/7, 429/2, -143, 143/2, -26, 13/2| |
| |15<br><br>|-1/15, 1, -7, 91/3, -91, 1001/5, -1001/3, 429, -429, 1001/3, -1001/5, 91, -91/3, 7| |
| |16<br><br>|1/16, -1, 15/2, -35, 455/4, -273, 1001/2, -715, 6435/8, -715, 1001/2, -273, 455/4, -35, 15/2| |
| |17<br><br>|-1/17, 1, -8, 40, -140, 364, -728, 1144, -1430, 1430, -1144, 728, -364, 140, -40, 8| |
| |18<br><br>|1/18, -1, 17/2, -136/3, 170, -476, 3094/3, -1768, 2431, -1768, 3094/3, -476, 170, -136/3, 17/2| |
| |19|1/19, 1, -9, 51, -204, 612, -1428, 2652, -3978, 4862, -4862, 3978, -2652, 1428, -612, 204, -51, 9| |
| |20<br><br>|1/20, -1, 19/2, -57, 969/4, -3876/5, 1938, -3876, 12597/2, -8398, 9237, -8398, 12597/2, -3876, 1938, -3876/5, 969/4, -57, 19/2| |


Table 2: The quantities Dp,q in equation (76) and (78) for various values of p.

Employing this pattern, it is easy to evaluate the coefficients Dp,q by choosing the same number of values of n as the number of unknowns, and solving linear equations for the p−1 unknowns. The values obtained can easily be checked for other values of n. Note that the coefficients in the linear equations are exactly known, and the values for the Dp,q are also exact. Some values are given in Table 4.

The lists of coefficients in Table 4 have some evident properties. The sum of the Dp,q over q when combined with 1/p from the first term on the right-hand side in equation (76) is required to be unity, so that the results for n = 1 on both sides of equation (76) match. For p even, Dp,1 = 1/p and later coefficients show an even symmetry. For p odd, later coefficients show an odd symmetry. For p odd, the second coefficient in Table 4 is 1, while for p even it is -1. There are p − 1 coefficients D, with the first two being 1/p,±1. The rest of the D’s fall into (p − 3)/2 pairs which combine subtractively for p odd, or (p − 4)/2 additive pairs and a central element for p even.

We take the limit as n → ∞ in equation (76) to define a set of harmonic sum Stieltjes constants γpH, where:

n

Hkp−1 k −

1 p

Hnp = γpH, (77)

lim

n→∞

k=1

and

γpH = Dp,1ζ(p) +

= Dp,1ζ(p) +

- p−1
- q=2


∞

Hkq−1 kp−q+1

Dp,q

k=1

- p−1
- q=2


Dp,qMq−1,p−q+1. (78)

##### The most slowly convergent by direct summation of the terms in (78) occurs for q = p − 1, where the summand goes to zero as log(k)p−2/k2.

|p 3|γpH 2.0034281719|Formula (89) 1.5772156649|Ratio 0.787258|
|---|---|---|---|
|4|5.8174873811|5.2314138804|0.899256|
|5|22.315371582|21.310286555|0.954959|
|6|109.08138223|106.82895159|0.979350|
|7|647.55020378|641.16593544|0.990140|
|8|4510.0214667|4488.2909965|0.995181|
|9|35992.013221|35906.413366|0.997621|
|10|323539.34424|323157.77574|0.998820|
|11|3233473.9305|3231577.7930|0.999413|


Table 3: The values γpH are compared with their integral approximations (89), together with ratios.

By applying formula (78), together with the computational techniques described below in Section 5, we were able to obtain these results:

- γ2H =

- 1

- 2


(ζ(2)) (79)

- γ3H =

1 3

(5ζ(3)) (80)

- γ4H =

1 8

(43ζ(4)) (81)

- γ5H =

1 5

(79ζ(5) + 15ζ(2)ζ(3)) (82)

- γ6H =

1 24

2187ζ(6) + 272ζ(3)2 (83)

- γ7H =

1 56

(18311ζ(7) + 4060ζ(2)ζ(5) + 8358ζ(3)ζ(4)) (84)

- γ8H =

1 576

1926401ζ(8) + 48384ζ(2)ζ(3)2 + 440064ζ(3)ζ(5) (85)

- γ9H =

1 36

501978ζ(9) + 266355ζ(3)ζ(6) + 241794ζ(4)ζ(5) + 105273ζ(2)ζ(7) + 12104ζ(3)3 (86)

- γ10H =

1 80

17061619ζ(10) + 3161210ζ(3)ζ(7) + 705180ζ(3)2ζ(4) + 928080ζ(2)ζ(3)ζ(5)

+1770112ζ(5)2 + 37320ζ(2)M(2,6) (87)

- γ11H =


1 264

(230253219ζ(11) + 49094276ζ(2)ζ(9) + 165822855ζ(3)ζ(8) + 130449891ζ(4)ζ(7)

+156493260ζ(5)ζ(6) + 805200ζ(2)ζ(3)3 + 19281504ζ(3)2ζ(5) + 1849320ζ(3)M(2,6)

+1232880M(3,8)) (88) Using the integral estimate Nn → [exp(γ)]nn! and replacing n by p−2, we multiply this by (p−1)/2,

the final Dp,q in each line of Table 2. This gives the estimate for γpH:

(p − 1)! 2

γpH ≈ [exp(γ)]p−2

. (89)

The approximation (89) is compared with the γpH for p ranging from 3 to 11 in Table 4. The trend is clearly for the relative accuracy to improve as p increases.

We turn now to equivalent expressions for the case when the denominator in the basic sum is k + 1

rather than k. From [4],

n−1

Hk k + 1

- 1

- 2


- 1

- 2


Hn(2). (90) The equivalent of equation (75) is

Hn2 −

=

k=1

n−1

n

Hk2 k + 1

1 3

1 3

Hk (k + 1)2

Hn3 −

Hn(3) −

. (91)

=

k=1

k=1

Once again, this may be extended to higher powers of Hk in the numerator, giving results of the following form:

- p−1
- q=2


n−1

n

Hkp−1 k + 1

Hkq−1 (k + 1)p−q+1. (92)

1 p

Hnp + Ep,1Hn(p) +

Ep,q

=

k=1

k=1

The sums on the right-hand side are the quantities sh studied inter alia in [8, 9], and connected with the I by (11). The coefficients Ep,q are given for p up to 21 in Table 4. Note that all the Ep,q are negative, unlike the alternating sign behaviour of the Dp,q.

We can define an alternate set of Stieltjes-like constants from equation (92):

lim

n→∞

n−1

Hkp−1 k + 1 −

k=1

1 p

Hnp = γph, (93)

where

- p−1
- q=2


γph = Ep,1ζ(p) +

Ep,qsh(q − 1,p − q + 1). (94)

The γph would then all be negative, and by virtue of (9) with a modulus well approximated asymptotically by (89).

### 5 Computational techniques

We initially obtained many of the formulas presented above and in Appendix 2 (Section 8) by a computational procedure that utilizes advanced techniques to produce a very high-precision numerical value of the sum, then employs an integer relation algorithm to identify the numerical value as a rational linear sum of constants from the list in Theorem 1. We present here a brief summary of these techniques, which are based in part on schemes described in [8, 15].

In this way, we have found formulas for the much more numerous set of mixed Euler cases

∞

M(m,n,p,q) =

k=1

Hkm kn(k + 1)p(k + 2)q

(95)

for orders r = m + n + p + q = 3 through 11, and also a selection of results of order 12. As noted above, this class includes the cases sh(m,n) and I(m,n) as subsets. We present the full collection of these formulas in Appendix 2 (Section 8).

#### 5.1 Computing Euler sums to high precision

One key tool for these computations is the Euler-Maclaurin summation formula [12, pg. 285], which approximates a summation as an integral with high-order corrections (here f(t) is assumed to have (2s + 2)-th order derivatives on [a,b]):

b

f(j) =

j=a

b

f(t)dt +

a

- 1

- 2


(f(a) + f(b)) +

s

B2j D2j−1f(b) − D2j−1f(a) (2j)!

j=1

+ Rs(a,b), (96)

| |p|Ep,q| |
|---|---|---|---|
| |2|-1/2| |
| |3|-1/3, -1| |
| |4<br><br>|-1/4, -1, -3/2| |
| |5|-1/5, -1, -2, -2| |
| |6|-1/6, -1, -5/2, -10/3, -5/2| |
| |7|-1/7, -1, -3, -5, -5, -3| |
| |8|-1/8, -1, -7/2, -7, -35/4, -7, -7/2| |
| |9<br><br>|-1/9, -1, -4, -28/3, -14, -14, -28/3, -4| |
| |10<br><br>|-1/10, -1, -9/2, -12, -21, -126/5, -21, -12, -9/2| |
| |11<br><br>|-1/11, -1, -5, -15, -30, -42, -42, -30, -15, -5| |
| |12|-1/12,-1, -(11/2), -(55/3), -(165/4), -66, -77, -66, -(165/4), -(55/3), -(11/2)| |
| |13|-1/13,-1, -6, -22, -55, -99, -132, -132, -99, -55, -22, -6| |
| |14|-1/14,-1, -(13/2), -26, -(143/2), -143, -(429/2), -(1716/7), -(429/2), -143, -(143/2), -26, -(13/2)| |
| |15<br><br>|-1/15,-1, -7, -(91/3), -91, -(1001/5), -(1001/3), -429, -429, -(1001/3), -(1001/5), -91, -(91/3), -7| |
| |16<br><br>|-1/16,-1, -(15/2), -35, -(455/4), -273, -(1001/2), -715, -(6435/8), -715, -(1001/2), -273, -(455/4), -35, -(15/2)| |
| |17<br><br>|-1/17,-1, -8, -40, -140, -364, -728, -1144, -1430, -1430, -1144, -728, -364, -140, -40, -8| |
| |18<br><br>|-1/18,-1, -(17/2), -(136/3), -170, -476, -(3094/3), -1768, -2431, -(24310/9), -2431, -1768, -(3094/3), -476, -170, -(136/3), -(17/2)| |
| |19|-1/19, -1, -9, -51, -204, -612, -1428, -2652, -3978, -4862, -4862, -3978, -2652, -1428, -612, -204, -51, -9| |
| |20|-1/20, -1, -(19/2), -57, -(969/4), -(3876/5), -1938, -3876, -(12597/2), -8398, -(46189/5), -8398, -(12597/2), -3876, -1938, -(3876/5), -(969/4), -57, -(19/2)| |
| |21<br><br>|-1/21,-1, -10, -(190/3), -285, -969, -2584, -(38760/7), -9690, -(41990/3), -16796, -16796, -(41990/3), -9690, -(38760/7), -2584, -969, -285, -(190/3), -10| |


##### Table 4: The coefficients Ep,q in equation (76) for various values of p.

where Bk is the k-th Bernoulli number [10], Dkf(a) is the k-th derivative of f(t) evaluated at t = a, and

Rs(a,b) = −1 (2s + 2)!

b

B2s+2(t − [t])D2s+2f(t)dt, (97)

a

where [·] denotes greatest integer and Bk(·) is the k-th Bernoulli polynomial [10] (note Bk = Bk(0)). Applying the Euler-Maclaurin summation formula to the harmonic function H(t) = tj=1 1/j yields

- 1

- 2t


H(t) = γ + log(t) +

s

+

j=1

B2j 2jt2j

+ Rs(t), (98)

where γ = 0.5772156649... is Euler’s constant and |Rs(t)| ≤ |B2s+2|/((2s + 2)t2s+2); see [8] for full details. In the computations for the present study, we set s = 21, so that H(t) is approximated by

- 1

- 2t −


1 120t4 −

1 252t6

1 240t8 −

1 132t10

691 32760t12 −

1 12t14

1 12t2

Hˆ(t) = γ + log(t) +

+

+

+

3392780147 3480t28 −

3617 8160t16 −

43867 14364t18

174611 6600t20 −

77683 276t22

236364091 65520t24 −

657931 12t26

+

+

+

+

26315271553053477373 69090840t36 −

7709321041217 16320t32 −

151628697551 12t34

1723168255201 85932t30

+

+

261082718496449122051 541200t40 −

1520097643918070802691 75852t42

154210205991661 12t38

+

, (99)

which approximates H(t) to within roughly t−44 for large t. The expression (99) can be obtained using Wolfram Mathematica with the command Series[HarmonicNumber[t],{t,Infinity,42}].

Given M(m,n,p,q), denote Gˆ(t) = Hˆ(t)m/(tn(t+1)p(t+2)q). Using the Euler-Maclaurin summation formula (96) once again, one can write

k

M(m,n,p,q) =

j=1

k

≈

j=1

H(j)m jn(j + 1)p(j + 2)q

+

H(j)m jn(j + 1)p(j + 2)q

+

∞

H(j)m jn(j + 1)p(j + 2)q ≈

j=k+1

k

j=1

∞

Gˆ(t)dt +

k+1

- 1

- 2


Gˆ(k + 1) −

H(j)m jn(j + 1)p(j + 2)q

∞

Gˆ(j)

+

j=k+1

s

B2jD2j−1Gˆ(k + 1) (2j)!

, (100)

j=1

where s = 21, which is accurate to within roughly k−44. Initially we set k = 108 = 100,000,000, so the approximation in the second line of (100) is correct to within roughly 10−354, which was sufficient for our early investigations. For larger cases, and for all runs listed in Appendix 2, we set k = 109 = 1,000,000,000, so this approximation is correct to within roughly 10−396.

We evaluated the first term of (100) (the explicit summation) using an arbitrary precision package [13]. Using k = 108 and a working precision of 360 digits (producing roughly 350 good digits) required 5–9 minutes CPU time per case on a 2024 Apple Mac Studio system with an M4 processor; using k = 109 and a working precision of 420 digits (producing roughly 400 good digits) required 50–90 minutes per case. For our 400-digit computations, we evaluated the second term (the integral) using the exp-sinh quadrature algorithm [13, 14], with the arbitrary precision software set to 400 digits; this required only 3– 4 seconds per case (we first tried to evaluate these integrals using Wolfram Mathematica version 14.2, but this failed for larger m). The third term is straightforward. The fourth term, which involves the symbolic expansion and numerical evaluation to 400-digit accuracy of high-order derivatives of the approximation function Gˆ(t) = Hˆ(t)m/(tn(t + 1)p(t + 2)q), where Hˆ(t) is given by the expression (99), was computed using Wolfram Mathematica; this required up to 400 seconds CPU time per case for larger m.

#### 5.2 Using an integer relation algorithm to find formulas

Once a 400-digit value for a given mixed Euler constant was obtained, we employed the multipair PSLQ algorithm to search for integer relations with known constants [15, 16, 17]. Given an v-long vector

x = (x0,x1,··· ,xv−1) of high-precision floating-point reals, the multipair PSLQ algorithm searches for integers (a0,a1,··· ,av−1) such that a0x0 + a1x1 + ··· + av−1xv−1 = 0 to within available precision, or else establishes that there is no such integer relation within a given bound. The algorithm operates by generating an iterative sequence of v × v integer matrices B, so that the entries of the vector y = B · x become progressively smaller, until one entry of y is numerically zero, at which iteration the algorithm halts, with the relation given by the row of B corresponding to the zero entry of y. In the application here, we set x0 to the 400-digit value of M(m,n,p,q). For the other entries of the input x vector, we specified 400-digit values of constants listed in Theorem 1, depending on the order r.

Integer relation detection by any algorithm requires very high precision (at least v · maxi log10 |ai| digits) to produce numerically reliable results, since otherwise the real relation, if any, will be lost in a sea of numerical artifacts. An effective check of numerical reliability with the multipair PSLQ algorithm is to note the dynamic range of the entries of the y vector at the iteration of detection. In the computer runs for results presented above and in Appendix 8, this dynamic range always exceeded 1063, and in most cases exceeded 10300. In other words, each of these relations holds to at least 63 digits (and in most cases to more than 300 digits) beyond the level required to discover the relation. However, these results should not be regarded as formally proven by these computations.

Figure 1 illustrates the process of finding a relation using the multipair PSLQ algorithm and assessing the numerical reliability of the result. This shows the base-10 logarithm of the minimum absolute value of the y vector (vertical axis), plotted against the iteration number (horizontal axis), in the multipair PSLQ computer run that the present authors employed to discover the order-10 formula

∞

1 4

H(k) k3(k + 1)6

84ζ(2) − 108ζ(3) − 5ζ(4) − 48ζ(5) + 24ζ(2)ζ(3) − 9ζ(6) + 6ζ(3)2

=

M(1,3,6,0) =

k=1

−12ζ(7) + 4ζ(2)ζ(5) + 4ζ(3)ζ(4)). (101)

Note that as the algorithm proceeds, the minimum absolute value of the y vector slowly decreases, from approximately 10−3 to approximately 10−65, but at iteration 311 abruptly drops to approximately 10−405, a drop of 340 orders of magnitude. Note that since we are using 400-digit precision, 10−405 is effectively zero, so the algorithm terminates here with the relation (4,−84,108,5,48,−24,9,−6,12,−4,−4). In other words, formula (101) holds to roughly 340 digits beyond the precision level required to discover it. This dynamic range at the iteration of detection can thus be considered a “confidence level” of the result’s numerical reliability.

#### 5.3 Computational results

The process described above succeeded in finding relations for each of the cases of form (95) with orders between 3 and 11, a total of 960 cases, plus an additional 54 selected cases of order 12. See Appendix 2 (Section 8) for a complete listing of these formulas. As noted below, in order to minimize the possibility of transcription errors, the LaTeX code for each section of results was generated automatically by a computer program from the output computer files, and this LaTeX code is included here without any alteration.

The techniques described in this section are applicable to more general classes of Euler sums, including Euler sums of orders higher than 12 and Euler sums with more complicated polynomial denominators. However, the computational cost increases with the precision required and the number of selected righthand-side constants. The principal challenges here are the first and fourth term of (100), namely (a) the cost of explicitly computing and summing to high precision a large number of terms of the mixed Euler sum series, and (b) the symbolic expansion and numerical evaluation of high-order derivatives of the function Gˆ(t). Perhaps further investigation into the underlying theory of Euler sums will yield computational schemes that are more efficient for large problems.

0

−50

−100

−150

||logminyii10

−200

−250

−300

−350

−400

50 100 150 200 250 300

Iteration

Figure 1: Plot of log10 mini |yi| in the multipair PSLQ computer run for M(1,3,6,0), showing the detection of the relation at iteration 311.

### 6 Conclusions

We have presented techniques, both algebraic and computational, for finding analytic evaluations of a significantly larger class of Euler sums than studied previously. We believe that most of these formulas are new to the literature. Along this line, we have found that Wolfram Mathematica (version 14.2) can evaluate many of the basic cases, but a large majority are not evaluated by this software.

These methods appear to be applicable to even more general Euler sums. For example, by applying the methods described above, we have obtained these intriguing computational results, among others:

∞

H(k) k(2k + 1)

= 2log(2)2 (102)

k=1

∞

H(k) k2(2k + 1)

= 2ζ(3) − 4log(2)2 (103)

k=1

∞

H(k) (2k + 1)2

1 4

(7ζ(3) − 6log(2)ζ(2)) (104)

=

k=1

∞

H(k) k2(2k + 1)2

= 9ζ(3) − 6log(2)ζ(2) − 8log(2)2 (105)

k=1

∞

1 16

H(k) (2k + 1)4

(62ζ(5) − 21ζ(2)ζ(3) − 30log(2)ζ(4)) (106)

=

k=1

Note the appearance of log(2) in these formulas. Each of these formulas holds to nearly 400-digit accuracy (approximately 350 digits beyond the level required to discover them), but at present we do not yet know

how they can be rigorously proven.

The new results presented in this study also highlight the benefits of attempting to solve for all Euler sums of a given order. The results given for sums of mixed type may be of use in indicating the zeta function values likely to arise in attempts to numerically solve for recalcitrant sums like those for order eight and higher. It is hoped that the asymptotic form inferred for the constants γpH can be deduced rigorously, as it may well prove useful in other applications of high-order Euler sums.

### References

- [1] McPhedran, R.C., Scott, T.C., and Maignan, A. 2023. The Keiper-Li criterion for the Riemann hypothesis and generalized Lambert functions, ACM Comm. in Computer Algebra, 57, 85–110.
- [2] Keiper, J.B. 1992. Power Series Expansions of Riemann’s ξ Function Math. Comp. 58 765–773.
- [3] Li, X.J. 1997. The positivity of a sequence of numbers and the Riemann hypothesis J. Number Th. 65 325–333.
- [4] Choi, J. and Srivastava, H.M. 2011. Some summation formulas involving harmonic numbers and generalised harmonic numbers, Math and Comp. Mod., 54, 220-2234.
- [5] Wenchang Chu. 1997. Hypergeometric series and the Riemann zeta function, Acta Arithmetica, 82, 103–118
- [6] Mathematics Stack Exchange: Is there a closed form for nk=1 Hk2−1/k?
- [7] Mathematics Stack Exchange: Sum of powers of Harmonic Numbers.
- [8] Bailey, D.H., Borwein, J.M. and Girgensohn, R. 1994. Experimental evaluation of Euler sums, Experimental Mathematics, 3, 17-30.
- [9] Borwein, D., Borwein, J.M. and Girgenshon, R. 1995. Explicit evaluation of Euler sums, Proc. Edinb. Math. Soc., 38, 277-294.
- [10] NIST, Handbook of Mathematical Functions. 2020. Cambridge University Press. Chap. 2; Chap. 6; Chap. 24; Chap. 25, https://dlmf.nist.gov.
- [11] Zheng, D-Y 2007 Further summation formulae related to generalized harmonic numbers, J. Math. Anal. Appl., 335, 692-706.
- [12] Kendall E. Atkinson. 1990. An Introduction to Numerical Analysis, 2nd ed., John Wiley and Sons, New York.
- [13] Bailey, D.H., “MPFUN2020: A new thread-safe arbitrary precision package,” 2024, https://www. davidhbailey.com/dhbpapers/mpfun2020.pdf.
- [14] Bailey, D.H., Li, X.S. and Jeyabalan, K. 2005. A comparison of three high-precision quadrature schemes, Experimental Mathematics, 14, 317–329.
- [15] Bailey, D.H., “The two-level multipair PSLQ algorithm,” 2025, https://www.davidhbailey.com/ dhbpapers/pslqm2-alg.pdf.
- [16] Bailey, D.H. and Broadhurst, D.J. 2000. Parallel integer relation detection: Techniques and applications, Math. of Computation, 70, 1719–1736.
- [17] Ferguson, H.R.P., Bailey, D.H. and Arno, S. 1999. Analysis of PSLQ, an integer relation finding algorithm, Math. of Computation, 68, 351–369.


### 7 Appendix 1: 400-digit values of three key constants

We present here 400-digit approximations of M(2,6), M(2,8), M(3,8), M(2,10), M(4,8): 1.041413395855265060833934370636480151499859280096830090748511645153773087302971 78483751544719684852509976852158376374740737268847953695380222383595172532123654 63963612795034976112760332996361625685218808108323018034356756036322549570832977 08604139265652530043836463078378465035583569011375448218307043216126923803712749 23988797094981204968396475470138806138535478550733612009250215922048841374239723 645442685850 1.009386471889869832518544227219279156409372942639652641202049549364385367847079 49180863769095027121905627225975982985135460410529740749826141104503536876835470 18469301862442802589875242849768895787689895958104331283788277223328457927340866 40158920385626435450329285165922784555461987108701748322359094830741802548831985 88668354450902612335818964472409228594433865464246509588184931824643738162119198 662316661058 1.014305290895216264339827024366251554326370696089068947073583456867667637693523 94671117513355550815252027023563642862142136424802329417381850641867359561102369 07708608852232885420834448581394420559852401108798464519014241848466439384418357 64122407964525143823389069592803884034573487533288088530610292952331243167418134 67198428033583320677784291408584463648948157254030603048103031772735772545074505 256977622009 1.002258993186511461546882204200782204716716526446955625961726703382258341612187 43078937691748374313286427718378216976785972900132909275418926271525587620211343 23828486038109593077991669275749305259201098402321866062725818826804223344328667 24311160745124744110382924162704634065128094036087399151400598689180216783658166 11238941907596547797317455957463173904843228565114429853394147887119147441919740 167418480233 1.021889991239632409955119439812528407213142628943801388819377166083386890422403 37811800890914656945480609918216413770587578233999208809687116705691954898386671 55265235208787528310809835281206739252549491701207237871226480178257316430518840 84028017686753324378706573579491021902617968550914371718501262794713100873318573 13123823952255996488552702615920587505801228078818063210192756692513776767867839 561290224768

### 8 Appendix 2: Formulas for orders 3 through 12

We present here the full set of results for M(m,n,p,q) for orders 3 through 11, a total of 960 cases, plus 54 additional selected cases of order 12. The algorithms employed by our computer programs to generate these formulas are described above in Section 5. Each of these formulas holds to at least 380digit precision, which is at least 63 digits (and in most cases more than 300 digits) beyond the level required to discover the relation. However, these formulas should not be regarded as formally proven solely by these computations.

To minimize the possibility of transcription errors, in each section below the formulas were produced by a computer program that parses the computer run output files, extracts the formulas, sorts them lexiographically and then generates LaTeX code (including all spacing, line breaks and page breaks). We have included this LaTeX code here without any alteration.

∞

H(k) k2

= 2ζ(3) (107)

k=1

∞

H(k) k(k + 1)

= ζ(2) (108)

k=1

∞

H(k) (k + 1)2

= ζ(3) (109)

k=1

∞

H(k) k(k + 2)

- 1

- 2


=

(1 + ζ(2)) (110)

k=1

∞

H(k) (k + 1)(k + 2)

= 1 (111)

k=1

∞

H(k) (k + 2)2

= 2 − ζ(2) − ζ(3) (112)

k=1

∞

1 4

H(k) k3

=

(5ζ(4)) (113)

k=1

∞

H(k) k2(k + 1)

= −ζ(2) + 2ζ(3) (114)

k=1

∞

H(k) k(k + 1)2

= ζ(2) − ζ(3) (115)

k=1

∞

H(k) (k + 1)3

1 4

=

(ζ(4)) (116)

k=1

∞

H(k) k2(k + 2)

1 4

(−1 − ζ(2) + 4ζ(3)) (117)

=

k=1

∞

- 1

- 2


H(k) k(k + 1)(k + 2)

(1 − ζ(2)) (118)

=

k=1

∞

H(k) (k + 1)2(k + 2)

= −1 + ζ(3) (119)

k=1

∞

H(k) k(k + 2)2

1 4

(5 − ζ(2) − 2ζ(3)) (120)

=

k=1

∞

H(k) (k + 1)(k + 2)2

= 3 − ζ(2) − ζ(3) (121)

k=1

∞

H(k) (k + 2)3

1 4

(−12 + 4ζ(2) + 4ζ(3) + ζ(4)) (122)

=

k=1

∞

H(k)2 k2

1 4

=

(17ζ(4)) (123)

k=1

∞

H(k)2 k(k + 1)

= 3ζ(3) (124)

k=1

∞

H(k)2 (k + 1)2

1 4

=

(11ζ(4)) (125)

k=1

∞

H(k)2 k(k + 2)

- 1

- 2


=

(1 + ζ(2) + 3ζ(3)) (126)

k=1

∞

H(k)2 (k + 1)(k + 2)

= 1 + ζ(2) (127)

k=1

∞

H(k)2 (k + 2)2

1 4

(−12 + 8ζ(3) + 11ζ(4)) (128)

=

k=1

∞

H(k) k4

= 3ζ(5) − ζ(2)ζ(3) (129)

k=1

∞

H(k) k3(k + 1)

1 4

(4ζ(2) − 8ζ(3) + 5ζ(4)) (130)

=

k=1

∞

H(k) k2(k + 1)2

= 2ζ(2) − 3ζ(3) (131)

k=1

∞

1 4

H(k) k(k + 1)3

(4ζ(2) − 4ζ(3) − ζ(4)) (132)

=

k=1

∞

H(k) (k + 1)4

= 2ζ(5) − ζ(2)ζ(3) (133)

k=1

∞

H(k) k3(k + 2)

1 8

(1 + ζ(2) − 4ζ(3) + 5ζ(4)) (134)

=

k=1

∞

1 4

H(k) k2(k + 1)(k + 2)

(1 − 3ζ(2) + 4ζ(3)) (135)

=

k=1

∞

H(k) k(k + 1)2(k + 2)

- 1

- 2


(1 + ζ(2) − 2ζ(3)) (136)

=

k=1

∞

H(k) (k + 1)3(k + 2)

1 4

(4 − 4ζ(3) + ζ(4)) (137)

=

k=1

∞

H(k) k2(k + 2)2

1 4

(3 − 3ζ(3)) (138)

=

k=1

∞

1 4

H(k) k(k + 1)(k + 2)2

(7 − 3ζ(2) − 2ζ(3)) (139)

=

k=1

∞

H(k) (k + 1)2(k + 2)2

= 4 − ζ(2) − 2ζ(3) (140)

k=1

∞

H(k) k(k + 2)3

1 8

(17 − 5ζ(2) − 6ζ(3) − ζ(4)) (141)

=

k=1

∞

1 4

H(k) (k + 1)(k + 2)3

(24 − 8ζ(2) − 8ζ(3) − ζ(4)) (142)

=

k=1

∞

H(k) (k + 2)4

= −4 + ζ(2) + ζ(3) + ζ(4) + 2ζ(5) − ζ(2)ζ(3) (143)

k=1

∞

H(k)2 k3

1 2

(7ζ(5) − 2ζ(2)ζ(3)) (144)

=

k=1

∞

H(k)2 k2(k + 1)

1 4

(12ζ(3) − 17ζ(4)) (145)

=

k=1

∞

H(k)2 k(k + 1)2

1 4

(12ζ(3) − 11ζ(4)) (146)

=

k=1

∞

H(k)2 (k + 1)3

- 1

- 2


(−3ζ(5) + 2ζ(2)ζ(3)) (147)

=

k=1

∞

H(k)2 k2(k + 2)

1 8

(−2 − 2ζ(2) − 6ζ(3) + 17ζ(4)) (148)

=

k=1

∞

H(k)2 k(k + 1)(k + 2)

- 1

- 2


(1 + ζ(2) − 3ζ(3)) (149)

=

k=1

∞

H(k)2 (k + 1)2(k + 2)

1 4

(−4 − 4ζ(2) + 11ζ(4)) (150)

=

k=1

∞

H(k)2 k(k + 2)2

1 8

(14 + 2ζ(2) − 2ζ(3) − 11ζ(4)) (151)

=

k=1

∞

H(k)2 (k + 1)(k + 2)2

1 4

(16 + 4ζ(2) − 8ζ(3) − 11ζ(4)) (152)

=

k=1

∞

H(k)2 (k + 2)3

- 1

- 2


(12 − 2ζ(2) − 6ζ(3) − ζ(4) + 3ζ(5) − 2ζ(2)ζ(3)) (153)

=

k=1

∞

H(k)3 k2

= 10ζ(5) + ζ(2)ζ(3) (154)

k=1

∞

H(k)3 k(k + 1)

= 10ζ(4) (155)

k=1

∞

H(k)3 (k + 1)2

- 1

- 2


(15ζ(5) + 2ζ(2)ζ(3)) (156)

=

k=1

∞

H(k)3 k(k + 2)

- 1

- 2


=

(1 + 2ζ(2) + 4ζ(3) + 10ζ(4)) (157)

k=1

∞

H(k)3 (k + 1)(k + 2)

= 1 + 2ζ(2) + 4ζ(3) (158)

k=1

∞

H(k)3 (k + 2)2

1 4

(16 + 12ζ(2) + 4ζ(3) − 33ζ(4) − 30ζ(5) − 4ζ(2)ζ(3)) (159)

=

k=1

- Formulas for order r = m + n + p + q = 6: ∞


1 4

H(k) k5

7ζ(6) − 2ζ(3)2 (160)

=

k=1

∞

H(k) k4(k + 1)

1 4

(4ζ(2) − 8ζ(3) + 5ζ(4) − 12ζ(5) + 4ζ(2)ζ(3)) (161)

=

k=1

∞

1 4

H(k) k3(k + 1)2

(12ζ(2) − 20ζ(3) + 5ζ(4)) (162)

=

k=1

∞

1 4

H(k) k2(k + 1)3

(−12ζ(2) + 16ζ(3) + ζ(4)) (163)

=

k=1

∞

1 4

H(k) k(k + 1)4

(4ζ(2) − 4ζ(3) − ζ(4) − 8ζ(5) + 4ζ(2)ζ(3)) (164)

=

k=1

∞

1 4

H(k) (k + 1)5

3ζ(6) − 2ζ(3)2 (165)

=

k=1

∞

1 16

H(k) k4(k + 2)

(1 + ζ(2) − 4ζ(3) + 5ζ(4) − 24ζ(5) + 8ζ(2)ζ(3)) (166)

=

k=1

∞

H(k) k3(k + 1)(k + 2)

1 8

(−1 + 7ζ(2) − 12ζ(3) + 5ζ(4)) (167)

=

k=1

∞

H(k) k2(k + 1)2(k + 2)

1 4

(−1 − 5ζ(2) + 8ζ(3)) (168)

=

k=1

∞

H(k) k(k + 1)3(k + 2)

1 4

(−2 + 2ζ(2) − ζ(4)) (169)

=

k=1

∞

1 4

H(k) (k + 1)4(k + 2)

(4 − 4ζ(3) + ζ(4) − 8ζ(5) + 4ζ(2)ζ(3)) (170)

=

k=1

∞

H(k) k3(k + 2)2

1 16

(7 + ζ(2) − 10ζ(3) + 5ζ(4)) (171)

=

k=1

∞

H(k) k2(k + 1)(k + 2)2

1 4

(4 − 3ζ(2) + ζ(3)) (172)

=

k=1

∞

1 4

H(k) k(k + 1)2(k + 2)2

(9 − ζ(2) − 6ζ(3)) (173)

=

k=1

∞

H(k) (k + 1)3(k + 2)2

1 4

(20 − 4ζ(2) − 12ζ(3) + ζ(4)) (174)

=

k=1

∞

H(k) k2(k + 2)3

1 16

(−23 + 5ζ(2) + 12ζ(3) + ζ(4)) (175)

=

k=1

∞

1 8

H(k) k(k + 1)(k + 2)3

(−31 + 11ζ(2) + 10ζ(3) + ζ(4)) (176)

=

k=1

∞

1 4

H(k) (k + 1)2(k + 2)3

(−40 + 12ζ(2) + 16ζ(3) + ζ(4)) (177)

=

k=1

∞

1 16

H(k) k(k + 2)4

(49 − 13ζ(2) − 14ζ(3) − 9ζ(4) − 16ζ(5) + 8ζ(2)ζ(3)) (178)

=

k=1

∞

1 4

H(k) (k + 1)(k + 2)4

(40 − 12ζ(2) − 12ζ(3) − 5ζ(4) − 8ζ(5) + 4ζ(2)ζ(3)) (179)

=

k=1

∞

1 4 −20 + 4ζ(2) + 4ζ(3) + 4ζ(4) + 4ζ(5) + 3ζ(6) − 2ζ(3)2 (180)

H(k) (k + 2)5

=

k=1

∞

H(k)2 k4

1 24

97ζ(6) − 48ζ(3)2 (181)

=

k=1

∞

H(k)2 k3(k + 1)

1 4

(12ζ(3) − 17ζ(4) + 14ζ(5) − 4ζ(2)ζ(3)) (182)

=

k=1

∞

H(k)2 k2(k + 1)2

= 6ζ(3) − 7ζ(4) (183)

k=1

∞

H(k)2 k(k + 1)3

1 4

(12ζ(3) − 11ζ(4) + 6ζ(5) − 4ζ(2)ζ(3)) (184)

=

k=1

∞

H(k)2 (k + 1)4

1 24

37ζ(6) − 24ζ(3)2 (185)

=

k=1

∞

H(k)2 k3(k + 2)

1 16

(2 + 2ζ(2) + 6ζ(3) − 17ζ(4) + 28ζ(5) − 8ζ(2)ζ(3)) (186)

=

k=1

∞

H(k)2 k2(k + 1)(k + 2)

1 8

(2 + 2ζ(2) − 18ζ(3) + 17ζ(4)) (187)

=

k=1

∞

H(k)2 k(k + 1)2(k + 2)

1 4

(2 + 2ζ(2) + 6ζ(3) − 11ζ(4)) (188)

=

k=1

∞

H(k)2 (k + 1)3(k + 2)

1 4

(4 + 4ζ(2) − 11ζ(4) − 6ζ(5) + 4ζ(2)ζ(3)) (189)

=

k=1

∞

H(k)2 k2(k + 2)2

1 4

(4 + ζ(2) + ζ(3) − 7ζ(4)) (190)

=

k=1

∞

H(k)2 k(k + 1)(k + 2)2

1 8

(18 + 6ζ(2) − 14ζ(3) − 11ζ(4)) (191)

=

k=1

∞

H(k)2 (k + 1)2(k + 2)2

- 1

- 2


(−10 − 4ζ(2) + 4ζ(3) + 11ζ(4)) (192)

=

k=1

∞

H(k)2 k(k + 2)3

1 16

(62 − 6ζ(2) − 26ζ(3) − 15ζ(4) + 12ζ(5) − 8ζ(2)ζ(3)) (193)

=

k=1

∞

H(k)2 (k + 1)(k + 2)3

1 4

(40 − 20ζ(3) − 13ζ(4) + 6ζ(5) − 4ζ(2)ζ(3)) (194)

=

k=1

∞

H(k)2 (k + 2)4

1 24

(240 − 48ζ(2) − 96ζ(3) − 36ζ(4) − 96ζ(5) + 48ζ(2)ζ(3) − 37ζ(6)

=

k=1

+24ζ(3)2 (195) ∞

H(k)3 k3

1 16

93ζ(6) − 40ζ(3)2 (196)

=

k=1

∞

H(k)3 k2(k + 1)

= 10ζ(4) − 10ζ(5) − ζ(2)ζ(3) (197)

k=1

∞

H(k)3 k(k + 1)2

- 1

- 2


(20ζ(4) − 15ζ(5) − 2ζ(2)ζ(3)) (198)

=

k=1

∞

H(k)3 (k + 1)3

1

16 −33ζ(6) + 32ζ(3)2 (199) ∞

=

k=1

H(k)3 k2(k + 2)

1 4

(1 + 2ζ(2) + 4ζ(3) + 10ζ(4) − 20ζ(5) − 2ζ(2)ζ(3)) (200)

=

k=1

∞

H(k)3 k(k + 1)(k + 2)

- 1

- 2


(1 + 2ζ(2) + 4ζ(3) − 10ζ(4)) (201)

=

k=1

∞

H(k)3 (k + 1)2(k + 2)

- 1

- 2


(2 + 4ζ(2) + 8ζ(3) − 15ζ(5) − 2ζ(2)ζ(3)) (202)

=

k=1

∞

H(k)3 k(k + 2)2

1 8

(18 + 16ζ(2) + 12ζ(3) − 13ζ(4) − 30ζ(5) − 4ζ(2)ζ(3)) (203)

=

k=1

∞

H(k)3 (k + 1)(k + 2)2

1 4

(20 + 20ζ(2) + 20ζ(3) − 33ζ(4) − 30ζ(5) − 4ζ(2)ζ(3)) (204)

=

k=1

∞

H(k)3 (k + 2)3

1 16

(160 + 48ζ(2) − 48ζ(3) − 144ζ(4) + 72ζ(5) − 48ζ(2)ζ(3) + 33ζ(6)

=

k=1

−32ζ(3)2 (205) ∞

H(k)4 k2

1 24

979ζ(6) + 72ζ(3)2 (206)

=

k=1

∞

H(k)4 k(k + 1)

= 30ζ(5) + 6ζ(2)ζ(3) (207)

k=1

∞

H(k)4 (k + 1)2

1 24

859ζ(6) + 72ζ(3)2 (208)

=

k=1

∞

H(k)4 k(k + 2)

1 4

=

(2 + 6ζ(2) + 22ζ(3) + 37ζ(4) + 60ζ(5) + 12ζ(2)ζ(3)) (209)

k=1

∞

H(k)4 (k + 1)(k + 2)

- 1

- 2


=

(2 + 6ζ(2) + 22ζ(3) + 37ζ(4)) (210)

k=1

∞

H(k)4 (k + 2)2

1 24

(−120 − 192ζ(2) − 432ζ(3) − 48ζ(4) + 720ζ(5) + 96ζ(2)ζ(3)

=

k=1

+859ζ(6) + 72ζ(3)2 (211)

- Formulas for order r = m + n + p + q = 7: ∞


H(k) k6

= 4ζ(7) − ζ(2)ζ(5) − ζ(3)ζ(4) (212)

k=1

∞

H(k) k5(k + 1)

1 4

(4ζ(2) − 8ζ(3) + 5ζ(4) − 12ζ(5) + 4ζ(2)ζ(3) + 7ζ(6)

=

k=1

−2ζ(3)2 (213) ∞

- 1

- 2


H(k) k4(k + 1)2

(−8ζ(2) + 14ζ(3) − 5ζ(4) + 6ζ(5) − 2ζ(2)ζ(3)) (214)

=

k=1

∞

H(k) k3(k + 1)3

= 6ζ(2) − 9ζ(3) + ζ(4) (215)

k=1

∞

H(k) k2(k + 1)4

- 1

- 2


(8ζ(2) − 10ζ(3) − ζ(4) − 4ζ(5) + 2ζ(2)ζ(3)) (216)

=

k=1

∞

H(k) k(k + 1)5

1 4

(4ζ(2) − 4ζ(3) − ζ(4) − 8ζ(5) + 4ζ(2)ζ(3) − 3ζ(6)

=

k=1

+2ζ(3)2 (217) ∞

H(k) (k + 1)6

= 3ζ(7) − ζ(2)ζ(5) − ζ(3)ζ(4) (218)

k=1

∞

H(k) k5(k + 2)

1 32

(1 + ζ(2) − 4ζ(3) + 5ζ(4) − 24ζ(5) + 8ζ(2)ζ(3) + 28ζ(6)

=

k=1

−8ζ(3)2 (219) ∞

H(k) k4(k + 1)(k + 2)

1 16

(1 − 15ζ(2) + 28ζ(3) − 15ζ(4) + 24ζ(5) − 8ζ(2)ζ(3)) (220)

=

k=1

∞

H(k) k3(k + 1)2(k + 2)

1 8

(1 + 17ζ(2) − 28ζ(3) + 5ζ(4)) (221)

=

k=1

∞

H(k) k2(k + 1)3(k + 2)

1 4

(1 − 7ζ(2) + 8ζ(3) + ζ(4)) (222)

=

k=1

∞

1 2

H(k) k(k + 1)4(k + 2)

(1 + ζ(2) − 2ζ(3) − 4ζ(5) + 2ζ(2)ζ(3)) (223)

=

k=1

∞

1 4

H(k) (k + 1)5(k + 2)

4 − 4ζ(3) + ζ(4) − 8ζ(5) + 4ζ(2)ζ(3) + 3ζ(6) − 2ζ(3)2 (224)

=

k=1

∞

H(k) k4(k + 2)2

1 16

(−4 − ζ(2) + 7ζ(3) − 5ζ(4) + 12ζ(5) − 4ζ(2)ζ(3)) (225)

=

k=1

∞

H(k) k3(k + 1)(k + 2)2

1 16

(9 − 13ζ(2) + 14ζ(3) − 5ζ(4)) (226)

=

k=1

∞

1 4

H(k) k2(k + 1)2(k + 2)2

(−5 − 2ζ(2) + 7ζ(3)) (227)

=

k=1

∞

1 4

H(k) k(k + 1)3(k + 2)2

(11 − 3ζ(2) − 6ζ(3) + ζ(4)) (228)

=

k=1

∞

1 2

H(k) (k + 1)4(k + 2)2

(12 − 2ζ(2) − 8ζ(3) + ζ(4) − 4ζ(5) + 2ζ(2)ζ(3)) (229)

=

k=1

∞

1 16

H(k) k3(k + 2)3

(15 − 2ζ(2) − 11ζ(3) + 2ζ(4)) (230)

=

k=1

∞

1 16

H(k) k2(k + 1)(k + 2)3

(39 − 17ζ(2) − 8ζ(3) − ζ(4)) (231)

=

k=1

∞

H(k) k(k + 1)2(k + 2)3

1 8

(49 − 13ζ(2) − 22ζ(3) − ζ(4)) (232)

=

k=1

∞

H(k) (k + 1)3(k + 2)3

= 15 − 4ζ(2) − 7ζ(3) (233)

k=1

∞

H(k) k2(k + 2)4

1 16

(36 − 9ζ(2) − 13ζ(3) − 5ζ(4) − 8ζ(5) + 4ζ(2)ζ(3)) (234)

=

k=1

∞

H(k) k(k + 1)(k + 2)4

1 16

(111 − 35ζ(2) − 34ζ(3) − 11ζ(4) − 16ζ(5) + 8ζ(2)ζ(3)) (235)

=

k=1

∞

H(k) (k + 1)2(k + 2)4

1 2

(−40 + 12ζ(2) + 14ζ(3) + 3ζ(4) + 4ζ(5) − 2ζ(2)ζ(3)) (236)

=

k=1

∞

H(k) k(k + 2)5

1 32

(129 − 29ζ(2) − 30ζ(3) − 25ζ(4) − 32ζ(5) + 8ζ(2)ζ(3) − 12ζ(6)

=

k=1

+8ζ(3)2 (237) ∞

H(k) (k + 1)(k + 2)5

1 4

(60 − 16ζ(2) − 16ζ(3) − 9ζ(4) − 12ζ(5) + 4ζ(2)ζ(3) − 3ζ(6)

=

k=1

+2ζ(3)2 (238) ∞

H(k) (k + 2)6

= 6 − ζ(2) − ζ(3) − ζ(4) − ζ(5) − ζ(6) − 3ζ(7) + ζ(2)ζ(5) + ζ(3)ζ(4) (239)

k=1

∞

H(k)2 k5

- 1

- 2


(12ζ(7) − 2ζ(2)ζ(5) − 5ζ(3)ζ(4)) (240)

=

k=1

∞

H(k)2 k4(k + 1)

1 24

(−72ζ(3) + 102ζ(4) − 84ζ(5) + 24ζ(2)ζ(3) + 97ζ(6)

=

k=1

−48ζ(3)2 (241)

∞

H(k)2 k3(k + 1)2

1 4

(36ζ(3) − 45ζ(4) + 14ζ(5) − 4ζ(2)ζ(3)) (242)

=

k=1

∞

H(k)2 k2(k + 1)3

1 4

(−36ζ(3) + 39ζ(4) − 6ζ(5) + 4ζ(2)ζ(3)) (243)

=

k=1

∞

H(k)2 k(k + 1)4

1 24

(72ζ(3) − 66ζ(4) + 36ζ(5) − 24ζ(2)ζ(3) − 37ζ(6)

=

k=1

+24ζ(3)2 (244) ∞

H(k)2 (k + 1)5

- 1

- 2


(2ζ(7) − 2ζ(2)ζ(5) + ζ(3)ζ(4)) (245)

=

k=1

∞

H(k)2 k4(k + 2)

1 96

(6 + 6ζ(2) + 18ζ(3) − 51ζ(4) + 84ζ(5) − 24ζ(2)ζ(3) − 194ζ(6)

=

k=1

+96ζ(3)2 (246) ∞

H(k)2 k3(k + 1)(k + 2)

1 16

(−2 − 2ζ(2) + 42ζ(3) − 51ζ(4) + 28ζ(5) − 8ζ(2)ζ(3)) (247)

=

k=1

∞

H(k)2 k2(k + 1)2(k + 2)

1 8

(−2 − 2ζ(2) − 30ζ(3) + 39ζ(4)) (248)

=

k=1

∞

H(k)2 k(k + 1)3(k + 2)

- 1

- 2


(−1 − ζ(2) + 3ζ(3) + 3ζ(5) − 2ζ(2)ζ(3)) (249)

=

k=1

∞

H(k)2 (k + 1)4(k + 2)

1 24

(−24 − 24ζ(2) + 66ζ(4) + 36ζ(5) − 24ζ(2)ζ(3) + 37ζ(6)

=

k=1

−24ζ(3)2 (250) ∞

H(k)2 k3(k + 2)2

1 32

(18 + 6ζ(2) + 10ζ(3) − 45ζ(4) + 28ζ(5) − 8ζ(2)ζ(3)) (251)

=

k=1

∞

H(k)2 k2(k + 1)(k + 2)2

1 8

(10 + 4ζ(2) − 16ζ(3) + 3ζ(4)) (252)

=

k=1

∞

H(k)2 k(k + 1)2(k + 2)2

1 8

(22 + 10ζ(2) − 2ζ(3) − 33ζ(4)) (253)

=

k=1

∞

H(k)2 (k + 1)3(k + 2)2

1 4

(24 + 12ζ(2) − 8ζ(3) − 33ζ(4) − 6ζ(5) + 4ζ(2)ζ(3)) (254)

=

k=1

∞

H(k)2 k2(k + 2)3

1 32

(−78 + 2ζ(2) + 22ζ(3) + 43ζ(4) − 12ζ(5) + 8ζ(2)ζ(3)) (255)

=

k=1

∞

H(k)2 k(k + 1)(k + 2)3

1 16

(98 + 6ζ(2) − 54ζ(3) − 37ζ(4) + 12ζ(5) − 8ζ(2)ζ(3)) (256)

=

k=1

∞

H(k)2 (k + 1)2(k + 2)3

1 4

(60 + 8ζ(2) − 28ζ(3) − 35ζ(4) + 6ζ(5) − 4ζ(2)ζ(3)) (257)

=

k=1

∞

H(k)2 k(k + 2)4

1 96

(666 − 114ζ(2) − 270ζ(3) − 117ζ(4) − 156ζ(5) + 72ζ(2)ζ(3)

=

k=1

−74ζ(6) + 48ζ(3)2 (258) ∞

H(k)2 (k + 1)(k + 2)4

1 24

(480 − 48ζ(2) − 216ζ(3) − 114ζ(4) − 60ζ(5) + 24ζ(2)ζ(3)

=

k=1

−37ζ(6) + 24ζ(3)2 (259) ∞

H(k)2 (k + 2)5

- 1

- 2


(30 − 6ζ(2) − 10ζ(3) − 5ζ(4) − 10ζ(5) + 4ζ(2)ζ(3) − 3ζ(6)

=

k=1

+2ζ(3)2 + 2ζ(7) − 2ζ(2)ζ(5) + ζ(3)ζ(4) (260) ∞

H(k)3 k4

1 16

(231ζ(7) + 32ζ(2)ζ(5) − 204ζ(3)ζ(4)) (261)

=

k=1

∞

H(k)3 k3(k + 1)

1 16

160ζ(4) − 160ζ(5) − 16ζ(2)ζ(3) + 93ζ(6) − 40ζ(3)2 (262)

=

k=1

∞

H(k)3 k2(k + 1)2

- 1

- 2


(−40ζ(4) + 35ζ(5) + 4ζ(2)ζ(3)) (263)

=

k=1

∞

H(k)3 k(k + 1)3

1 16

160ζ(4) − 120ζ(5) − 16ζ(2)ζ(3) + 33ζ(6) − 32ζ(3)2 (264)

=

k=1

∞

H(k)3 (k + 1)4

1 16

(119ζ(7) + 32ζ(2)ζ(5) − 132ζ(3)ζ(4)) (265)

=

k=1

∞

H(k)3 k3(k + 2)

1 32

(4 + 8ζ(2) + 16ζ(3) + 40ζ(4) − 80ζ(5) − 8ζ(2)ζ(3) + 93ζ(6)

=

k=1

−40ζ(3)2 (266) ∞

H(k)3 k2(k + 1)(k + 2)

1 4

(1 + 2ζ(2) + 4ζ(3) − 30ζ(4) + 20ζ(5) + 2ζ(2)ζ(3)) (267)

=

k=1

∞

H(k)3 k(k + 1)2(k + 2)

- 1

- 2


(1 + 2ζ(2) + 4ζ(3) + 10ζ(4) − 15ζ(5) − 2ζ(2)ζ(3)) (268)

=

k=1

∞

H(k)3 (k + 1)3(k + 2)

1 16

(16 + 32ζ(2) + 64ζ(3) − 120ζ(5) − 16ζ(2)ζ(3) − 33ζ(6)

=

k=1

+32ζ(3)2 (269) ∞

H(k)3 k2(k + 2)2

1 16

(−20 − 20ζ(2) − 20ζ(3) − 7ζ(4) + 70ζ(5) + 8ζ(2)ζ(3)) (270)

=

k=1

∞

H(k)3 k(k + 1)(k + 2)2

1 8

(−22 − 24ζ(2) − 28ζ(3) + 53ζ(4) + 30ζ(5) + 4ζ(2)ζ(3)) (271)

=

k=1

∞

H(k)3 (k + 1)2(k + 2)2

1 4

(24 + 28ζ(2) + 36ζ(3) − 33ζ(4) − 60ζ(5) − 8ζ(2)ζ(3)) (272)

=

k=1

∞

H(k)3 k(k + 2)3

1 32

(196 + 80ζ(2) − 24ζ(3) − 170ζ(4) + 12ζ(5) − 56ζ(2)ζ(3)

=

k=1

+33ζ(6) − 32ζ(3)2 (273) ∞

H(k)3 (k + 1)(k + 2)3

1 16

(240 + 128ζ(2) + 32ζ(3) − 276ζ(4) − 48ζ(5) − 64ζ(2)ζ(3)

=

k=1

+33ζ(6) − 32ζ(3)2 (274) ∞

H(k)3 (k + 2)4

1 16

320 + 32ζ(2) − 128ζ(3) − 172ζ(4) − 24ζ(5) − 74ζ(6) + 48ζ(3)2

=

k=1

−119ζ(7) − 32ζ(2)ζ(5) + 132ζ(3)ζ(4)) (275)

∞

H(k)4 k3

1 8

(185ζ(7) + 40ζ(2)ζ(5) − 172ζ(3)ζ(4)) (276)

=

k=1

∞

H(k)4 k2(k + 1)

1 24

720ζ(5) + 144ζ(2)ζ(3) − 979ζ(6) − 72ζ(3)2 (277)

=

k=1

∞

H(k)4 k(k + 1)2

1 24

720ζ(5) + 144ζ(2)ζ(3) − 859ζ(6) − 72ζ(3)2 (278)

=

k=1

∞

H(k)4 (k + 1)3

1 8

(109ζ(7) + 40ζ(2)ζ(5) − 148ζ(3)ζ(4)) (279)

=

k=1

∞

H(k)4 k2(k + 2)

1 48

(−12 − 36ζ(2) − 132ζ(3) − 222ζ(4) − 360ζ(5) − 72ζ(2)ζ(3)

=

k=1

+979ζ(6) + 72ζ(3)2 (280) ∞

H(k)4 k(k + 1)(k + 2)

1 4

(−2 − 6ζ(2) − 22ζ(3) − 37ζ(4) + 60ζ(5) + 12ζ(2)ζ(3)) (281)

=

k=1

∞

H(k)4 (k + 1)2(k + 2)

1 24

24 + 72ζ(2) + 264ζ(3) + 444ζ(4) − 859ζ(6) − 72ζ(3)2 (282)

=

k=1

∞

H(k)4 k(k + 2)2

1 48

(132 + 228ζ(2) + 564ζ(3) + 270ζ(4) − 360ζ(5) − 24ζ(2)ζ(3)

=

k=1

−859ζ(6) − 72ζ(3)2 (283) ∞

H(k)4 (k + 1)(k + 2)2

1 24

(144 + 264ζ(2) + 696ζ(3) + 492ζ(4) − 720ζ(5) − 96ζ(2)ζ(3)

=

k=1

−859ζ(6) − 72ζ(3)2 (284)

∞

H(k)4 (k + 2)3

1 8

(−120 − 112ζ(2) − 160ζ(3) + 124ζ(4) + 168ζ(5) + 80ζ(2)ζ(3)

=

k=1

−66ζ(6) + 64ζ(3)2 − 109ζ(7) − 40ζ(2)ζ(5) + 148ζ(3)ζ(4) (285) ∞

H(k)5 k2

1 16

=

(2051ζ(7) + 456ζ(2)ζ(5) + 528ζ(3)ζ(4)) (286)

k=1

∞

H(k)5 k(k + 1)

- 1

- 2


357ζ(6) + 45ζ(3)2 (287)

=

k=1

∞

H(k)5 (k + 1)2

1 16

=

(1855ζ(7) + 456ζ(2)ζ(5) + 528ζ(3)ζ(4)) (288)

k=1

∞

H(k)5 k(k + 2)

1 8

=

(4 + 16ζ(2) + 84ζ(3) + 251ζ(4) + 284ζ(5) + 60ζ(2)ζ(3) + 714ζ(6)

k=1

+90ζ(3)2 (289) ∞

H(k)5 (k + 1)(k + 2)

1 4

=

(4 + 16ζ(2) + 84ζ(3) + 251ζ(4) + 284ζ(5) + 60ζ(2)ζ(3)) (290)

k=1

∞

H(k)5 (k + 2)2

1 48

(−288 − 720ζ(2) − 2784ζ(3) − 4704ζ(4) + 192ζ(5) − 240ζ(2)ζ(3)

=

k=1

+8590ζ(6) + 720ζ(3)2 + 5565ζ(7) + 1368ζ(2)ζ(5) + 1584ζ(3)ζ(4) (291)

##### Formulas for order r = m + n + p + q = 8:

∞

1 4

H(k) k7

(9ζ(8) − 4ζ(3)ζ(5)) (292)

=

k=1

∞

H(k) k6(k + 1)

1 4

4ζ(2) − 8ζ(3) + 5ζ(4) − 12ζ(5) + 4ζ(2)ζ(3) + 7ζ(6) − 2ζ(3)2

=

k=1

−16ζ(7) + 4ζ(2)ζ(5) + 4ζ(3)ζ(4)) (293)

∞

1 4

H(k) k5(k + 1)2

(20ζ(2) − 36ζ(3) + 15ζ(4) − 24ζ(5) + 8ζ(2)ζ(3) + 7ζ(6)

=

k=1

−2ζ(3)2 (294) ∞

- 1

- 2


H(k) k4(k + 1)3

(20ζ(2) − 32ζ(3) + 7ζ(4) − 6ζ(5) + 2ζ(2)ζ(3)) (295)

=

k=1

∞

1 2

H(k) k3(k + 1)4

(20ζ(2) − 28ζ(3) + ζ(4) − 4ζ(5) + 2ζ(2)ζ(3)) (296)

=

k=1

∞

H(k) k2(k + 1)5

1 4

(20ζ(2) − 24ζ(3) − 3ζ(4) − 16ζ(5) + 8ζ(2)ζ(3) − 3ζ(6)

=

k=1

+2ζ(3)2 (297) ∞

H(k) k(k + 1)6

1 4

4ζ(2) − 4ζ(3) − ζ(4) − 8ζ(5) + 4ζ(2)ζ(3) − 3ζ(6) + 2ζ(3)2

=

k=1

−12ζ(7) + 4ζ(2)ζ(5) + 4ζ(3)ζ(4)) (298)

∞

1 4

H(k) (k + 1)7

(5ζ(8) − 4ζ(3)ζ(5)) (299)

=

k=1

∞

H(k) k6(k + 2)

1 64

(−1 − ζ(2) + 4ζ(3) − 5ζ(4) + 24ζ(5) − 8ζ(2)ζ(3) − 28ζ(6)

=

k=1

+8ζ(3)2 + 128ζ(7) − 32ζ(2)ζ(5) − 32ζ(3)ζ(4) (300) ∞

H(k) k5(k + 1)(k + 2)

1 32

(−1 + 31ζ(2) − 60ζ(3) + 35ζ(4) − 72ζ(5) + 24ζ(2)ζ(3) + 28ζ(6)

=

k=1

−8ζ(3)2 (301) ∞

H(k) k4(k + 1)2(k + 2)

1 16

(−1 − 49ζ(2) + 84ζ(3) − 25ζ(4) + 24ζ(5) − 8ζ(2)ζ(3)) (302)

=

k=1

∞

1 8

H(k) k3(k + 1)3(k + 2)

(−1 + 31ζ(2) − 44ζ(3) + 3ζ(4)) (303)

=

k=1

∞

1 4

H(k) k2(k + 1)4(k + 2)

(−1 − 9ζ(2) + 12ζ(3) + ζ(4) + 8ζ(5) − 4ζ(2)ζ(3)) (304)

=

k=1

∞

H(k) k(k + 1)5(k + 2)

1 4

2 − 2ζ(2) + ζ(4) + 3ζ(6) − 2ζ(3)2 (305)

=

k=1

∞

H(k) (k + 1)6(k + 2)

1 4

4 − 4ζ(3) + ζ(4) − 8ζ(5) + 4ζ(2)ζ(3) + 3ζ(6) − 2ζ(3)2

=

k=1

−12ζ(7) + 4ζ(2)ζ(5) + 4ζ(3)ζ(4)) (306)

∞

1 64

H(k) k5(k + 2)2

(9 + 3ζ(2) − 18ζ(3) + 15ζ(4) − 48ζ(5) + 16ζ(2)ζ(3) + 28ζ(6)

=

k=1

−8ζ(3)2 (307) ∞

1 16

H(k) k4(k + 1)(k + 2)2

(5 − 14ζ(2) + 21ζ(3) − 10ζ(4) + 12ζ(5) − 4ζ(2)ζ(3)) (308)

=

k=1

∞

H(k) k3(k + 1)2(k + 2)2

1 16

(11 + 21ζ(2) − 42ζ(3) + 5ζ(4)) (309)

=

k=1

∞

H(k) k2(k + 1)3(k + 2)2

1 4

(6 − 5ζ(2) + ζ(3) + ζ(4)) (310)

=

k=1

∞

H(k) k(k + 1)4(k + 2)2

1 4

(13 − ζ(2) − 10ζ(3) + ζ(4) − 8ζ(5) + 4ζ(2)ζ(3)) (311)

=

k=1

∞

H(k) (k + 1)5(k + 2)2

1 4

(28 − 4ζ(2) − 20ζ(3) + 3ζ(4) − 16ζ(5) + 8ζ(2)ζ(3) + 3ζ(6)

=

k=1

−2ζ(3)2 (312) ∞

H(k) k4(k + 2)3

1 32

(19 − ζ(2) − 18ζ(3) + 7ζ(4) − 12ζ(5) + 4ζ(2)ζ(3)) (313)

=

k=1

∞

H(k) k3(k + 1)(k + 2)3

1 16

(−24 + 15ζ(2) − 3ζ(3) + 3ζ(4)) (314)

=

k=1

∞

H(k) k2(k + 1)2(k + 2)3

1 16

(−59 + 9ζ(2) + 36ζ(3) + ζ(4)) (315)

=

k=1

∞

H(k) k(k + 1)3(k + 2)3

1 8

(−71 + 19ζ(2) + 34ζ(3) − ζ(4)) (316)

=

k=1

∞

- 1

- 2


H(k) (k + 1)4(k + 2)3

(42 − 10ζ(2) − 22ζ(3) + ζ(4) − 4ζ(5) + 2ζ(2)ζ(3)) (317)

=

k=1

∞

H(k) k3(k + 2)4

1 32

(51 − 11ζ(2) − 24ζ(3) − 3ζ(4) − 8ζ(5) + 4ζ(2)ζ(3)) (318)

=

k=1

∞

H(k) k2(k + 1)(k + 2)4

1 16

(75 − 26ζ(2) − 21ζ(3) − 6ζ(4) − 8ζ(5) + 4ζ(2)ζ(3)) (319)

=

k=1

1 16

H(k) k(k + 1)2(k + 2)4

(209 − 61ζ(2) − 78ζ(3) − 13ζ(4) − 16ζ(5) + 8ζ(2)ζ(3)) (320)

=

k=1

∞

- 1

- 2


H(k) (k + 1)3(k + 2)4

(70 − 20ζ(2) − 28ζ(3) − 3ζ(4) − 4ζ(5) + 2ζ(2)ζ(3)) (321)

=

k=1

∞

1 64

H(k) k2(k + 2)5

(−201 + 47ζ(2) + 56ζ(3) + 35ζ(4) + 48ζ(5) − 16ζ(2)ζ(3) + 12ζ(6)

=

k=1

−8ζ(3)2 (322) ∞

1 32

H(k) k(k + 1)(k + 2)5

(351 − 99ζ(2) − 98ζ(3) − 47ζ(4) − 64ζ(5) + 24ζ(2)ζ(3) − 12ζ(6)

=

k=1

+8ζ(3)2 (323) ∞

1 4

H(k) (k + 1)2(k + 2)5

(140 − 40ζ(2) − 44ζ(3) − 15ζ(4) − 20ζ(5) + 8ζ(2)ζ(3) − 3ζ(6)

=

k=1

+2ζ(3)2 (324) ∞

H(k) k(k + 2)6

1 64

(321 − 61ζ(2) − 62ζ(3) − 57ζ(4) − 64ζ(5) + 8ζ(2)ζ(3) − 44ζ(6)

=

k=1

+8ζ(3)2 − 96ζ(7) + 32ζ(2)ζ(5) + 32ζ(3)ζ(4) (325) ∞

H(k) (k + 1)(k + 2)6

1 4

(84 − 20ζ(2) − 20ζ(3) − 13ζ(4) − 16ζ(5) + 4ζ(2)ζ(3) − 7ζ(6)

=

k=1

+2ζ(3)2 − 12ζ(7) + 4ζ(2)ζ(5) + 4ζ(3)ζ(4) (326) ∞

H(k) (k + 2)7

1 4

(28 − 4ζ(2) − 4ζ(3) − 4ζ(4) − 4ζ(5) − 4ζ(6) − 4ζ(7) − 5ζ(8)

=

k=1

+4ζ(3)ζ(5)) (327)

∞

H(k)2 k6

= M(2,6) (328)

k=1

∞

H(k)2 k5(k + 1)

1 24

72ζ(3) − 102ζ(4) + 84ζ(5) − 24ζ(2)ζ(3) − 97ζ(6) + 48ζ(3)2

=

k=1

+144ζ(7) − 24ζ(2)ζ(5) − 60ζ(3)ζ(4)) (329)

∞

H(k)2 k4(k + 1)2

1 24

(−288ζ(3) + 372ζ(4) − 168ζ(5) + 48ζ(2)ζ(3) + 97ζ(6)

=

k=1

−48ζ(3)2 (330) ∞

H(k)2 k3(k + 1)3

= 18ζ(3) − 21ζ(4) + 5ζ(5) − 2ζ(2)ζ(3) (331)

k=1

∞

H(k)2 k2(k + 1)4

1 24

(−288ζ(3) + 300ζ(4) − 72ζ(5) + 48ζ(2)ζ(3) + 37ζ(6)

=

k=1

−24ζ(3)2 (332) ∞

H(k)2 k(k + 1)5

1 24

72ζ(3) − 66ζ(4) + 36ζ(5) − 24ζ(2)ζ(3) − 37ζ(6) + 24ζ(3)2

=

k=1

+24ζ(7) − 24ζ(2)ζ(5) + 12ζ(3)ζ(4)) (333)

∞

H(k)2 (k + 1)6

- 1

- 2


(7ζ(8) − 4ζ(3)ζ(5) − 2M(2,6)) (334)

=

k=1

∞

H(k)2 k5(k + 2)

1 192

(6 + 6ζ(2) + 18ζ(3) − 51ζ(4) + 84ζ(5) − 24ζ(2)ζ(3) − 194ζ(6)

=

k=1

+96ζ(3)2 + 576ζ(7) − 96ζ(2)ζ(5) − 240ζ(3)ζ(4) (335) ∞

H(k)2 k4(k + 1)(k + 2)

1 96

(6 + 6ζ(2) − 270ζ(3) + 357ζ(4) − 252ζ(5) + 72ζ(2)ζ(3)

=

k=1

+194ζ(6) − 96ζ(3)2 (336) ∞

H(k)2 k3(k + 1)2(k + 2)

1 16

(2 + 2ζ(2) + 102ζ(3) − 129ζ(4) + 28ζ(5)

=

k=1

−8ζ(2)ζ(3)) (337)

∞

H(k)2 k2(k + 1)3(k + 2)

1 8

(2 + 2ζ(2) − 42ζ(3) + 39ζ(4) − 12ζ(5) + 8ζ(2)ζ(3)) (338)

=

k=1

∞

H(k)2 k(k + 1)4(k + 2)

1 24

12 + 12ζ(2) + 36ζ(3) − 66ζ(4) − 37ζ(6) + 24ζ(3)2 (339)

=

k=1

∞

H(k)2 (k + 1)5(k + 2)

1 24

(24 + 24ζ(2) − 66ζ(4) − 36ζ(5) + 24ζ(2)ζ(3) − 37ζ(6)

=

k=1

+24ζ(3)2 − 24ζ(7) + 24ζ(2)ζ(5) − 12ζ(3)ζ(4) (340) ∞

H(k)2 k4(k + 2)2

1 96

(−30 − 12ζ(2) − 24ζ(3) + 93ζ(4) − 84ζ(5) + 24ζ(2)ζ(3)

=

k=1

+97ζ(6) − 48ζ(3)2 (341) ∞

H(k)2 k3(k + 1)(k + 2)2

1 32

(−22 − 10ζ(2) + 74ζ(3) − 57ζ(4) + 28ζ(5)

=

k=1

−8ζ(2)ζ(3)) (342)

∞

H(k)2 k2(k + 1)2(k + 2)2

1 4

(−6 − 3ζ(2) − 7ζ(3) + 18ζ(4)) (343)

=

k=1

H(k)2 k(k + 1)3(k + 2)2

1 8

(26 + 14ζ(2) − 14ζ(3) − 33ζ(4) − 12ζ(5)

=

k=1

+8ζ(2)ζ(3)) (344)

∞

H(k)2 (k + 1)4(k + 2)2

1 24

(−168 − 96ζ(2) + 48ζ(3) + 264ζ(4) + 72ζ(5) − 48ζ(2)ζ(3)

=

k=1

+37ζ(6) − 24ζ(3)2 (345) ∞

H(k)2 k3(k + 2)3

1 16

(24 + ζ(2) − 3ζ(3) − 22ζ(4) + 10ζ(5) − 4ζ(2)ζ(3)) (346)

=

k=1

∞

H(k)2 k2(k + 1)(k + 2)3

1 32

(118 + 14ζ(2) − 86ζ(3) − 31ζ(4) + 12ζ(5)

=

k=1

−8ζ(2)ζ(3)) (347)

∞

H(k)2 k(k + 1)2(k + 2)3

1 16

(142 + 26ζ(2) − 58ζ(3) − 103ζ(4) + 12ζ(5)

=

k=1

−8ζ(2)ζ(3)) (348)

∞

H(k)2 (k + 1)3(k + 2)3

= 21 + 5ζ(2) − 9ζ(3) − 17ζ(4) (349)

k=1

∞

H(k)2 k2(k + 2)4

1 96

(450 − 60ζ(2) − 168ζ(3) − 123ζ(4) − 60ζ(5) + 24ζ(2)ζ(3)

=

k=1

−37ζ(6) + 24ζ(3)2 (350) ∞

H(k)2 k(k + 1)(k + 2)4

1 96

(1254 − 78ζ(2) − 594ζ(3) − 339ζ(4) − 84ζ(5) + 24ζ(2)ζ(3)

=

k=1

−74ζ(6) + 48ζ(3)2 (351) ∞

H(k)2 (k + 1)2(k + 2)4

1

24 −840 + 384ζ(3) + 324ζ(4) + 24ζ(5) + 37ζ(6) − 24ζ(3)2 (352) ∞

=

k=1

H(k)2 k(k + 2)5

1 192

(2106 − 402ζ(2) − 750ζ(3) − 357ζ(4) − 636ζ(5) + 264ζ(2)ζ(3)

=

k=1

−218ζ(6) + 144ζ(3)2 + 96ζ(7) − 96ζ(2)ζ(5) + 48ζ(3)ζ(4) (353) ∞

H(k)2 (k + 1)(k + 2)5

1 24

(840 − 120ζ(2) − 336ζ(3) − 174ζ(4) − 180ζ(5) + 72ζ(2)ζ(3)

=

k=1

−73ζ(6) + 48ζ(3)2 + 24ζ(7) − 24ζ(2)ζ(5) + 12ζ(3)ζ(4) (354) ∞

H(k)2 (k + 2)6

- 1

- 2


(42 − 8ζ(2) − 12ζ(3) − 7ζ(4) − 12ζ(5) + 4ζ(2)ζ(3) − 5ζ(6)

=

k=1

+2ζ(3)2 − 12ζ(7) + 4ζ(2)ζ(5) + 4ζ(3)ζ(4) + 7ζ(8) − 4ζ(3)ζ(5) −2M(2,6)) (355)

∞

H(k)3 k5

1 96

595ζ(8) + 120ζ(2)ζ(3)2 − 576ζ(3)ζ(5) − 264M(2,6) (356)

=

k=1

∞

H(k)3 k4(k + 1)

1 16 −160ζ(4) + 160ζ(5) + 16ζ(2)ζ(3) − 93ζ(6) + 40ζ(3)2 + 231ζ(7)

=

k=1

+32ζ(2)ζ(5) − 204ζ(3)ζ(4)) (357)

∞

H(k)3 k3(k + 1)2

1 16

480ζ(4) − 440ζ(5) − 48ζ(2)ζ(3) + 93ζ(6) − 40ζ(3)2 (358)

=

k=1

∞

H(k)3 k2(k + 1)3

1

16 −480ζ(4) + 400ζ(5) + 48ζ(2)ζ(3) − 33ζ(6) + 32ζ(3)2 (359) ∞

=

k=1

H(k)3 k(k + 1)4

1 16

160ζ(4) − 120ζ(5) − 16ζ(2)ζ(3) + 33ζ(6) − 32ζ(3)2 − 119ζ(7)

=

k=1

−32ζ(2)ζ(5) + 132ζ(3)ζ(4)) (360)

∞

H(k)3 (k + 1)5

1 96

43ζ(8) + 120ζ(2)ζ(3)2 − 288ζ(3)ζ(5) + 24M(2,6) (361)

=

k=1

∞

H(k)3 k4(k + 2)

1 64

(−4 − 8ζ(2) − 16ζ(3) − 40ζ(4) + 80ζ(5) + 8ζ(2)ζ(3) − 93ζ(6)

=

k=1

+40ζ(3)2 + 462ζ(7) + 64ζ(2)ζ(5) − 408ζ(3)ζ(4) (362) ∞

H(k)3 k3(k + 1)(k + 2)

1 32

(−4 − 8ζ(2) − 16ζ(3) + 280ζ(4) − 240ζ(5) − 24ζ(2)ζ(3)

=

k=1

+93ζ(6) − 40ζ(3)2 (363) ∞

H(k)3 k2(k + 1)2(k + 2)

1 4

(1 + 2ζ(2) + 4ζ(3) + 50ζ(4) − 50ζ(5) − 6ζ(2)ζ(3)) (364)

=

k=1

∞

H(k)3 k(k + 1)3(k + 2)

1 16

8 + 16ζ(2) + 32ζ(3) − 80ζ(4) − 33ζ(6) + 32ζ(3)2 (365)

=

k=1

∞

H(k)3 (k + 1)4(k + 2)

1 16

(−16 − 32ζ(2) − 64ζ(3) + 120ζ(5) + 16ζ(2)ζ(3) + 33ζ(6)

=

k=1

−32ζ(3)2 + 119ζ(7) + 32ζ(2)ζ(5) − 132ζ(3)ζ(4) (366) ∞

H(k)3 k3(k + 2)2

1 64

(44 + 48ζ(2) + 56ζ(3) + 54ζ(4) − 220ζ(5) − 24ζ(2)ζ(3)

=

k=1

+93ζ(6) − 40ζ(3)2 (367) ∞

H(k)3 k2(k + 1)(k + 2)2

1 16

(24 + 28ζ(2) + 36ζ(3) − 113ζ(4) + 10ζ(5)) (368)

=

k=1

∞

H(k)3 k(k + 1)2(k + 2)2

1 8

(26 + 32ζ(2) + 44ζ(3) − 13ζ(4) − 90ζ(5)

=

k=1

−12ζ(2)ζ(3)) (369)

∞

H(k)3 (k + 1)3(k + 2)2

1 16

(112 + 144ζ(2) + 208ζ(3) − 132ζ(4) − 360ζ(5) − 48ζ(2)ζ(3)

=

k=1

−33ζ(6) + 32ζ(3)2 (370) ∞

H(k)3 k2(k + 2)3

1 64

(236 + 120ζ(2) + 16ζ(3) − 156ζ(4) − 128ζ(5) − 72ζ(2)ζ(3)

=

k=1

+33ζ(6) − 32ζ(3)2 (371) ∞

H(k)3 k(k + 1)(k + 2)3

1 32

(−284 − 176ζ(2) − 88ζ(3) + 382ζ(4) + 108ζ(5) + 72ζ(2)ζ(3)

=

k=1

−33ζ(6) + 32ζ(3)2 (372) ∞

H(k)3 (k + 1)2(k + 2)3

1 16

(−336 − 240ζ(2) − 176ζ(3) + 408ζ(4) + 288ζ(5) + 96ζ(2)ζ(3)

=

k=1

−33ζ(6) + 32ζ(3)2 (373) ∞

H(k)3 k(k + 2)4

1 64

(836 + 144ζ(2) − 280ζ(3) − 514ζ(4) − 36ζ(5) − 56ζ(2)ζ(3)

=

k=1

−115ζ(6) + 64ζ(3)2 − 238ζ(7) − 64ζ(2)ζ(5) + 264ζ(3)ζ(4) (374) ∞

H(k)3 (k + 1)(k + 2)4

1 16

(560 + 160ζ(2) − 96ζ(3) − 448ζ(4) − 72ζ(5) − 64ζ(2)ζ(3)

=

k=1

−41ζ(6) + 16ζ(3)2 − 119ζ(7) − 32ζ(2)ζ(5) + 132ζ(3)ζ(4) (375) ∞

H(k)3 (k + 2)5

1 96

(−3360 + 1344ζ(3) + 1296ζ(4) + 816ζ(5) − 288ζ(2)ζ(3) + 660ζ(6)

=

k=1

−432ζ(3)2 − 288ζ(7) + 288ζ(2)ζ(5) − 144ζ(3)ζ(4) − 43ζ(8) −120ζ(2)ζ(3)2 + 288ζ(3)ζ(5) − 24M(2,6) (376)

∞

H(k)4 k4

1

144 −14833ζ(8) − 4032ζ(2)ζ(3)2 + 16704ζ(3)ζ(5) + 3744M(2,6) (377) ∞

=

k=1

H(k)4 k3(k + 1)

1 24

720ζ(5) + 144ζ(2)ζ(3) − 979ζ(6) − 72ζ(3)2 + 555ζ(7)

=

k=1

+120ζ(2)ζ(5) − 516ζ(3)ζ(4)) (378)

∞

H(k)4 k2(k + 1)2

1 12

720ζ(5) + 144ζ(2)ζ(3) − 919ζ(6) − 72ζ(3)2 (379)

=

k=1

1 24

720ζ(5) + 144ζ(2)ζ(3) − 859ζ(6) − 72ζ(3)2 + 327ζ(7)

=

k(k + 1)3

k=1

+120ζ(2)ζ(5) − 444ζ(3)ζ(4)) (380)

∞

H(k)4 (k + 1)4

1 144

12415ζ(8) + 3312ζ(2)ζ(3)2 − 13824ζ(3)ζ(5) − 3024M(2,6) (381)

=

k=1

∞

H(k)4 k3(k + 2)

1 96

=

(12 + 36ζ(2) + 132ζ(3) + 222ζ(4) + 360ζ(5) + 72ζ(2)ζ(3)

k=1

−979ζ(6) − 72ζ(3)2 + 1110ζ(7) + 240ζ(2)ζ(5) − 1032ζ(3)ζ(4) (382) ∞

H(k)4 k2(k + 1)(k + 2)

1 48

(12 + 36ζ(2) + 132ζ(3) + 222ζ(4) − 1080ζ(5) − 216ζ(2)ζ(3)

=

k=1

+979ζ(6) + 72ζ(3)2 (383) ∞

H(k)4 k(k + 1)2(k + 2)

1 24

=

(12 + 36ζ(2) + 132ζ(3) + 222ζ(4) + 360ζ(5) + 72ζ(2)ζ(3)

k=1

−859ζ(6) − 72ζ(3)2 (384) ∞

H(k)4 (k + 1)3(k + 2)

1 24

24 + 72ζ(2) + 264ζ(3) + 444ζ(4) − 859ζ(6) − 72ζ(3)2

=

k=1

−327ζ(7) − 120ζ(2)ζ(5) + 444ζ(3)ζ(4)) (385)

∞

H(k)4 k2(k + 2)2

1 48

(72 + 132ζ(2) + 348ζ(3) + 246ζ(4) + 24ζ(2)ζ(3) − 919ζ(6)

=

k=1

−72ζ(3)2 (386) ∞

H(k)4 k(k + 1)(k + 2)2

1 48

(−156 − 300ζ(2) − 828ζ(3) − 714ζ(4) + 1080ζ(5) + 168ζ(2)ζ(3)

=

k=1

+859ζ(6) + 72ζ(3)2 (387) ∞

H(k)4 (k + 1)2(k + 2)2

1 12

(84 + 168ζ(2) + 480ζ(3) + 468ζ(4) − 360ζ(5) − 48ζ(2)ζ(3)

=

k=1

−859ζ(6) − 72ζ(3)2 (388) ∞

H(k)4 k(k + 2)3

1 96

(852 + 900ζ(2) + 1524ζ(3) − 474ζ(4) − 1368ζ(5) − 504ζ(2)ζ(3)

=

k=1

−463ζ(6) − 456ζ(3)2 + 654ζ(7) + 240ζ(2)ζ(5) − 888ζ(3)ζ(4) (389) ∞

H(k)4 (k + 1)(k + 2)3

1 24

(504 + 600ζ(2) + 1176ζ(3) + 120ζ(4) − 1224ζ(5) − 336ζ(2)ζ(3)

=

k=1

−661ζ(6) − 264ζ(3)2 + 327ζ(7) + 120ζ(2)ζ(5) − 444ζ(3)ζ(4) (390)

1 144

(−5040 − 2880ζ(2) − 2304ζ(3) + 5040ζ(4) + 2880ζ(5) + 1728ζ(2)ζ(3)

=

(k + 2)4

k=1

+144ζ(6) + 288ζ(3)2 + 4284ζ(7) + 1152ζ(2)ζ(5) − 4752ζ(3)ζ(4) − 12415ζ(8) −3312ζ(2)ζ(3)2 + 13824ζ(3)ζ(5) + 3024M(2,6) (391)

∞

H(k)5 k3

1 288

67811ζ(8) + 19080ζ(2)ζ(3)2 − 78768ζ(3)ζ(5) − 16920M(2,6) (392)

=

k=1

∞

H(k)5 k2(k + 1)

1 16 −2856ζ(6) − 360ζ(3)2 + 2051ζ(7) + 456ζ(2)ζ(5)

=

k=1

+528ζ(3)ζ(4)) (393)

∞

H(k)5 k(k + 1)2

1 16

2856ζ(6) + 360ζ(3)2 − 1855ζ(7) − 456ζ(2)ζ(5)

=

k=1

−528ζ(3)ζ(4)) (394)

∞

H(k)5 (k + 1)3

1 288

65621ζ(8) + 17640ζ(2)ζ(3)2 − 72432ζ(3)ζ(5) − 15480M(2,6) (395)

=

k=1

∞

H(k)5 k2(k + 2)

1 32

(−8 − 32ζ(2) − 168ζ(3) − 502ζ(4) − 568ζ(5) − 120ζ(2)ζ(3)

=

k=1

−1428ζ(6) − 180ζ(3)2 + 2051ζ(7) + 456ζ(2)ζ(5) + 528ζ(3)ζ(4) (396) ∞

H(k)5 k(k + 1)(k + 2)

1 8

(4 + 16ζ(2) + 84ζ(3) + 251ζ(4) + 284ζ(5) + 60ζ(2)ζ(3) − 714ζ(6)

=

k=1

−90ζ(3)2 (397) ∞

H(k)5 (k + 1)2(k + 2)

1 16

=

(16 + 64ζ(2) + 336ζ(3) + 1004ζ(4) + 1136ζ(5) + 240ζ(2)ζ(3)

k=1

−1855ζ(7) − 456ζ(2)ζ(5) − 528ζ(3)ζ(4)) (398)

∞

H(k)5 k(k + 2)2

1 96

=

(312 + 816ζ(2) + 3288ζ(3) + 6210ζ(4) + 1512ζ(5) + 600ζ(2)ζ(3)

k=1

−4306ζ(6) − 180ζ(3)2 − 5565ζ(7) − 1368ζ(2)ζ(5) − 1584ζ(3)ζ(4) (399) ∞

H(k)5 (k + 1)(k + 2)2

1 48

=

(336 + 912ζ(2) + 3792ζ(3) + 7716ζ(4) + 3216ζ(5) + 960ζ(2)ζ(3)

k=1

−8590ζ(6) − 720ζ(3)2 − 5565ζ(7) − 1368ζ(2)ζ(5) − 1584ζ(3)ζ(4) (400) ∞

H(k)5 (k + 2)3

1 288

(−6048 − 10080ζ(2) − 30240ζ(3) − 30096ζ(4) + 18432ζ(5)

=

k=1

+4320ζ(2)ζ(3) + 45600ζ(6) + 10080ζ(3)2 − 19620ζ(7) − 7200ζ(2)ζ(5)

+26640ζ(3)ζ(4) + 65621ζ(8) + 17640ζ(2)ζ(3)2 − 72432ζ(3)ζ(5) −15480M(2,6)) (401)

1 8

5843ζ(8) − 328ζ(2)ζ(3)2 + 3896ζ(3)ζ(5) + 456M(2,6) (402)

=

k2

k=1

∞

H(k)6 k(k + 1)

= 644ζ(7) + 145ζ(2)ζ(5) + 297ζ(3)ζ(4) (403)

k=1

∞

H(k)6 (k + 1)2

1 24

17027ζ(8) − 924ζ(2)ζ(3)2 + 11328ζ(3)ζ(5) + 1308M(2,6) (404)

=

k=1

∞

H(k)6 k(k + 2)

1 8

=

(4 + 20ζ(2) + 136ζ(3) + 571ζ(4) + 1142ζ(5) + 244ζ(2)ζ(3) + 2097ζ(6)

k=1

+268ζ(3)2 + 2576ζ(7) + 580ζ(2)ζ(5) + 1188ζ(3)ζ(4) (405) ∞

H(k)6 (k + 1)(k + 2)

1 4

=

(4 + 20ζ(2) + 136ζ(3) + 571ζ(4) + 1142ζ(5) + 244ζ(2)ζ(3)

k=1

+2097ζ(6) + 268ζ(3)2 (406) ∞

H(k)6 (k + 2)2

1 24

(−168 − 576ζ(2) − 3120ζ(3) − 9288ζ(4) − 10104ζ(5) − 2448ζ(2)ζ(3)

=

k=1

+303ζ(6) − 528ζ(3)2 + 16695ζ(7) + 4104ζ(2)ζ(5) + 4752ζ(3)ζ(4) + 17027ζ(8) −924ζ(2)ζ(3)2 + 11328ζ(3)ζ(5) + 1308M(2,6) (407)

##### Formulas for order r = m + n + p + q = 9:

∞

H(k) k8

= 5ζ(9) − ζ(3)ζ(6) − ζ(4)ζ(5) − ζ(2)ζ(7) (408)

k=1

∞

H(k) k7(k + 1)

1 4

4ζ(2) − 8ζ(3) + 5ζ(4) − 12ζ(5) + 4ζ(2)ζ(3) + 7ζ(6) − 2ζ(3)2

=

k=1

−16ζ(7) + 4ζ(2)ζ(5) + 4ζ(3)ζ(4) + 9ζ(8) − 4ζ(3)ζ(5)) (409)

∞

1 2

H(k) k6(k + 1)2

(−12ζ(2) + 22ζ(3) − 10ζ(4) + 18ζ(5) − 6ζ(2)ζ(3) − 7ζ(6)

=

k=1

+2ζ(3)2 + 8ζ(7) − 2ζ(2)ζ(5) − 2ζ(3)ζ(4) (410) ∞

1 4

H(k) k5(k + 1)3

(60ζ(2) − 100ζ(3) + 29ζ(4) − 36ζ(5) + 12ζ(2)ζ(3) + 7ζ(6)

=

k=1

−2ζ(3)2 (411) ∞

H(k) k4(k + 1)4

= 20ζ(2) − 30ζ(3) + 4ζ(4) − 5ζ(5) + 2ζ(2)ζ(3) (412)

k=1

∞

H(k) k3(k + 1)5

1 4

(60ζ(2) − 80ζ(3) − ζ(4) − 24ζ(5) + 12ζ(2)ζ(3) − 3ζ(6)

=

k=1

+2ζ(3)2 (413) ∞

H(k) k2(k + 1)6

1 2

(−12ζ(2) + 14ζ(3) + 2ζ(4) + 12ζ(5) − 6ζ(2)ζ(3) + 3ζ(6)

=

k=1

−2ζ(3)2 + 6ζ(7) − 2ζ(2)ζ(5) − 2ζ(3)ζ(4) (414) ∞

H(k) k(k + 1)7

1 4

4ζ(2) − 4ζ(3) − ζ(4) − 8ζ(5) + 4ζ(2)ζ(3) − 3ζ(6) + 2ζ(3)2

=

k=1

−12ζ(7) + 4ζ(2)ζ(5) + 4ζ(3)ζ(4) − 5ζ(8) + 4ζ(3)ζ(5)) (415)

∞

H(k) (k + 1)8

= 4ζ(9) − ζ(3)ζ(6) − ζ(4)ζ(5) − ζ(2)ζ(7) (416)

k=1

∞

H(k) k7(k + 2)

1 128

(1 + ζ(2) − 4ζ(3) + 5ζ(4) − 24ζ(5) + 8ζ(2)ζ(3) + 28ζ(6)

=

k=1

−8ζ(3)2 − 128ζ(7) + 32ζ(2)ζ(5) + 32ζ(3)ζ(4) + 144ζ(8) −64ζ(3)ζ(5)) (417)

∞

1 64

H(k) k6(k + 1)(k + 2)

(1 − 63ζ(2) + 124ζ(3) − 75ζ(4) + 168ζ(5) − 56ζ(2)ζ(3)

=

k=1

−84ζ(6) + 24ζ(3)2 + 128ζ(7) − 32ζ(2)ζ(5) − 32ζ(3)ζ(4) (418) ∞

H(k) k5(k + 1)2(k + 2)

1 32

(1 + 129ζ(2) − 228ζ(3) + 85ζ(4) − 120ζ(5) + 40ζ(2)ζ(3)

=

k=1

+28ζ(6) − 8ζ(3)2 (419)

∞

H(k) k4(k + 1)3(k + 2)

1 16

(1 − 111ζ(2) + 172ζ(3) − 31ζ(4) + 24ζ(5) − 8ζ(2)ζ(3)) (420)

=

k=1

∞

H(k) k3(k + 1)4(k + 2)

1 8

(1 + 49ζ(2) − 68ζ(3) + ζ(4) − 16ζ(5) + 8ζ(2)ζ(3)) (421)

=

k=1

∞

1 4

H(k) k2(k + 1)5(k + 2)

(1 − 11ζ(2) + 12ζ(3) + 2ζ(4) + 8ζ(5) − 4ζ(2)ζ(3) + 3ζ(6)

=

k=1

−2ζ(3)2 (422) ∞

1 2

H(k) k(k + 1)6(k + 2)

(1 + ζ(2) − 2ζ(3) − 4ζ(5) + 2ζ(2)ζ(3) − 6ζ(7) + 2ζ(2)ζ(5)

=

k=1

+2ζ(3)ζ(4)) (423)

∞

H(k) (k + 1)7(k + 2)

1 4

4 − 4ζ(3) + ζ(4) − 8ζ(5) + 4ζ(2)ζ(3) + 3ζ(6) − 2ζ(3)2

=

k=1

−12ζ(7) + 4ζ(2)ζ(5) + 4ζ(3)ζ(4) + 5ζ(8) − 4ζ(3)ζ(5)) (424)

∞

H(k) k6(k + 2)2

1 64

(5 + 2ζ(2) − 11ζ(3) + 10ζ(4) − 36ζ(5) + 12ζ(2)ζ(3) + 28ζ(6)

=

k=1

−8ζ(3)2 − 64ζ(7) + 16ζ(2)ζ(5) + 16ζ(3)ζ(4) (425) ∞

H(k) k5(k + 1)(k + 2)2

1 64

(11 − 59ζ(2) + 102ζ(3) − 55ζ(4) + 96ζ(5) − 32ζ(2)ζ(3)

=

k=1

−28ζ(6) + 8ζ(3)2 (426) ∞

H(k) k4(k + 1)2(k + 2)2

1 16

(−6 − 35ζ(2) + 63ζ(3) − 15ζ(4) + 12ζ(5)

=

k=1

−4ζ(2)ζ(3)) (427)

∞

H(k) k3(k + 1)3(k + 2)2

1 16

(13 − 41ζ(2) + 46ζ(3) − ζ(4)) (428)

=

k=1

∞

H(k) k2(k + 1)4(k + 2)2

1 4

(−7 − 4ζ(2) + 11ζ(3) + 8ζ(5) − 4ζ(2)ζ(3)) (429)

=

k=1

∞

H(k) k(k + 1)5(k + 2)2

1 4

(15 − 3ζ(2) − 10ζ(3) + 2ζ(4) − 8ζ(5) + 4ζ(2)ζ(3) + 3ζ(6)

=

k=1

−2ζ(3)2 (430) ∞

- 1

- 2


H(k) (k + 1)6(k + 2)2

(16 − 2ζ(2) − 12ζ(3) + 2ζ(4) − 12ζ(5) + 6ζ(2)ζ(3) + 3ζ(6)

=

k=1

−2ζ(3)2 − 6ζ(7) + 2ζ(2)ζ(5) + 2ζ(3)ζ(4) (431)

∞

1 128

H(k) k5(k + 2)3

(47 + ζ(2) − 54ζ(3) + 29ζ(4) − 72ζ(5) + 24ζ(2)ζ(3) + 28ζ(6)

=

k=1

−8ζ(3)2 (432) ∞

1 32

H(k) k4(k + 1)(k + 2)3

(29 − 29ζ(2) + 24ζ(3) − 13ζ(4) + 12ζ(5) − 4ζ(2)ζ(3)) (433)

=

k=1

∞

1 16

H(k) k3(k + 1)2(k + 2)3

(35 + 6ζ(2) − 39ζ(3) + 2ζ(4)) (434)

=

k=1

∞

1 16

H(k) k2(k + 1)3(k + 2)3

(83 − 29ζ(2) − 32ζ(3) + 3ζ(4)) (435)

=

k=1

∞

1 8

H(k) k(k + 1)4(k + 2)3

(97 − 21ζ(2) − 54ζ(3) + 3ζ(4) − 16ζ(5) + 8ζ(2)ζ(3)) (436)

=

k=1

∞

1 4

H(k) (k + 1)5(k + 2)3

(112 − 24ζ(2) − 64ζ(3) + 5ζ(4) − 24ζ(5) + 12ζ(2)ζ(3)

=

k=1

+3ζ(6) − 2ζ(3)2 (437) ∞

H(k) k4(k + 2)4

1 32

(−35 + 6ζ(2) + 21ζ(3) − 2ζ(4) + 10ζ(5) − 4ζ(2)ζ(3)) (438)

=

k=1

∞

H(k) k3(k + 1)(k + 2)4

1 32

(−99 + 41ζ(2) + 18ζ(3) + 9ζ(4) + 8ζ(5) − 4ζ(2)ζ(3)) (439)

=

k=1

∞

H(k) k2(k + 1)2(k + 2)4

1 16

(−134 + 35ζ(2) + 57ζ(3) + 7ζ(4) + 8ζ(5)

=

k=1

−4ζ(2)ζ(3)) (440)

∞

H(k) k(k + 1)3(k + 2)4

1 16

(−351 + 99ζ(2) + 146ζ(3) + 11ζ(4) + 16ζ(5)

=

k=1

−8ζ(2)ζ(3)) (441)

∞

H(k) (k + 1)4(k + 2)4

= −56 + 15ζ(2) + 25ζ(3) + ζ(4) + 4ζ(5) − 2ζ(2)ζ(3) (442)

k=1

∞

1 128

H(k) k3(k + 2)5

(303 − 69ζ(2) − 104ζ(3) − 41ζ(4) − 64ζ(5) + 24ζ(2)ζ(3)

=

k=1

−12ζ(6) + 8ζ(3)2 (443) ∞

1 64

H(k) k2(k + 1)(k + 2)5

(501 − 151ζ(2) − 140ζ(3) − 59ζ(4) − 80ζ(5) + 32ζ(2)ζ(3)

=

k=1

−12ζ(6) + 8ζ(3)2 (444)

∞

1 32

H(k) k(k + 1)2(k + 2)5

(769 − 221ζ(2) − 254ζ(3) − 73ζ(4) − 96ζ(5) + 40ζ(2)ζ(3)

=

k=1

−12ζ(6) + 8ζ(3)2 (445) ∞

1 4

H(k) (k + 1)3(k + 2)5

(280 − 80ζ(2) − 100ζ(3) − 21ζ(4) − 28ζ(5) + 12ζ(2)ζ(3)

=

k=1

−3ζ(6) + 2ζ(3)2 (446) ∞

1 64

H(k) k2(k + 2)6

(261 − 54ζ(2) − 59ζ(3) − 46ζ(4) − 56ζ(5) + 12ζ(2)ζ(3) − 28ζ(6)

=

k=1

+8ζ(3)2 − 48ζ(7) + 16ζ(2)ζ(5) + 16ζ(3)ζ(4) (447) ∞

1 64

H(k) k(k + 1)(k + 2)6

(−1023 + 259ζ(2) + 258ζ(3) + 151ζ(4) + 192ζ(5) − 56ζ(2)ζ(3)

=

k=1

+68ζ(6) − 24ζ(3)2 + 96ζ(7) − 32ζ(2)ζ(5) − 32ζ(3)ζ(4) (448) ∞

- 1

- 2


H(k) (k + 1)2(k + 2)6

(112 − 30ζ(2) − 32ζ(3) − 14ζ(4) − 18ζ(5) + 6ζ(2)ζ(3) − 5ζ(6)

=

k=1

+2ζ(3)2 − 6ζ(7) + 2ζ(2)ζ(5) + 2ζ(3)ζ(4) (449) ∞

H(k) k(k + 2)7

1 128

(769 − 125ζ(2) − 126ζ(3) − 121ζ(4) − 128ζ(5) + 8ζ(2)ζ(3) − 108ζ(6)

=

k=1

+8ζ(3)2 − 160ζ(7) + 32ζ(2)ζ(5) + 32ζ(3)ζ(4) − 80ζ(8)

+64ζ(3)ζ(5)) (450)

∞

H(k) (k + 1)(k + 2)7

1 4

(112 − 24ζ(2) − 24ζ(3) − 17ζ(4) − 20ζ(5) + 4ζ(2)ζ(3) − 11ζ(6)

=

k=1

+2ζ(3)2 − 16ζ(7) + 4ζ(2)ζ(5) + 4ζ(3)ζ(4) − 5ζ(8) + 4ζ(3)ζ(5) (451) ∞

H(k) (k + 2)8

= −8 + ζ(2) + ζ(3) + ζ(4) + ζ(5) + ζ(6) + ζ(7) + ζ(8) + 4ζ(9) − ζ(3)ζ(6)

k=1

− ζ(4)ζ(5) − ζ(2)ζ(7) (452)

∞

H(k)2 k7

1 6

(55ζ(9) − 21ζ(3)ζ(6) − 15ζ(4)ζ(5) − 6ζ(2)ζ(7)

=

k=1

+2ζ(3)3 (453) ∞

H(k)2 k6(k + 1)

1 24

72ζ(3) − 102ζ(4) + 84ζ(5) − 24ζ(2)ζ(3) − 97ζ(6) + 48ζ(3)2

=

k=1

+144ζ(7) − 24ζ(2)ζ(5) − 60ζ(3)ζ(4) − 24M(2,6)) (454)

∞

H(k)2 k5(k + 1)2

1 12

(180ζ(3) − 237ζ(4) + 126ζ(5) − 36ζ(2)ζ(3) − 97ζ(6)

=

k=1

+48ζ(3)2 + 72ζ(7) − 12ζ(2)ζ(5) − 30ζ(3)ζ(4) (455)

1 24

(720ζ(3) − 876ζ(4) + 288ζ(5) − 96ζ(2)ζ(3) − 97ζ(6)

=

k4(k + 1)3

k=1

+48ζ(3)2 (456) ∞

H(k)2 k3(k + 1)4

1 24

(720ζ(3) − 804ζ(4) + 192ζ(5) − 96ζ(2)ζ(3) − 37ζ(6)

=

k=1

+24ζ(3)2 (457) ∞

H(k)2 k2(k + 1)5

1 12

(180ζ(3) − 183ζ(4) + 54ζ(5) − 36ζ(2)ζ(3) − 37ζ(6)

=

k=1

+24ζ(3)2 + 12ζ(7) − 12ζ(2)ζ(5) + 6ζ(3)ζ(4) (458) ∞

H(k)2 k(k + 1)6

1 24

72ζ(3) − 66ζ(4) + 36ζ(5) − 24ζ(2)ζ(3) − 37ζ(6) + 24ζ(3)2

=

k=1

+24ζ(7) − 24ζ(2)ζ(5) + 12ζ(3)ζ(4) + 84ζ(8) − 48ζ(3)ζ(5) − 24M(2,6)) (459)

∞

H(k)2 (k + 1)7

1 6

(ζ(9) − 9ζ(3)ζ(6) − 3ζ(4)ζ(5) + 6ζ(2)ζ(7)

=

k=1

+2ζ(3)3 (460) ∞

H(k)2 k6(k + 2)

1 384

(6 + 6ζ(2) + 18ζ(3) − 51ζ(4) + 84ζ(5) − 24ζ(2)ζ(3) − 194ζ(6)

=

k=1

+96ζ(3)2 + 576ζ(7) − 96ζ(2)ζ(5) − 240ζ(3)ζ(4) − 192M(2,6) (461) ∞

H(k)2 k5(k + 1)(k + 2)

1 64

(−2 − 2ζ(2) + 186ζ(3) − 255ζ(4) + 196ζ(5) − 56ζ(2)ζ(3)

=

k=1

−194ζ(6) + 96ζ(3)2 + 192ζ(7) − 32ζ(2)ζ(5) − 80ζ(3)ζ(4) (462) ∞

H(k)2 k4(k + 1)2(k + 2)

1 96

(6 + 6ζ(2) + 882ζ(3) − 1131ζ(4) + 420ζ(5) − 120ζ(2)ζ(3)

=

k=1

−194ζ(6) + 96ζ(3)2 (463) ∞

H(k)2 k3(k + 1)3(k + 2)

1 16

(−2 − 2ζ(2) + 186ζ(3) − 207ζ(4) + 52ζ(5)

=

k=1

−24ζ(2)ζ(3)) (464)

∞

H(k)2 k2(k + 1)4(k + 2)

1 24

(−6 − 6ζ(2) − 162ζ(3) + 183ζ(4) − 36ζ(5) + 24ζ(2)ζ(3)

=

k=1

+37ζ(6) − 24ζ(3)2 (465) ∞

H(k)2 k(k + 1)5(k + 2)

- 1

- 2


(−1 − ζ(2) + 3ζ(3) + 3ζ(5) − 2ζ(2)ζ(3) + 2ζ(7)

=

k=1

−2ζ(2)ζ(5) + ζ(3)ζ(4)) (466)

1 24

(24 + 24ζ(2) − 66ζ(4) − 36ζ(5) + 24ζ(2)ζ(3) − 37ζ(6)

=

(k + 1)6(k + 2)

k=1

+24ζ(3)2 − 24ζ(7) + 24ζ(2)ζ(5) − 12ζ(3)ζ(4) + 84ζ(8) − 48ζ(3)ζ(5) −24M(2,6)) (467)

∞

H(k)2 k5(k + 2)2

1 384

(66 + 30ζ(2) + 66ζ(3) − 237ζ(4) + 252ζ(5) − 72ζ(2)ζ(3)

=

k=1

−388ζ(6) + 192ζ(3)2 + 576ζ(7) − 96ζ(2)ζ(5) − 240ζ(3)ζ(4) (468) ∞

H(k)2 k4(k + 1)(k + 2)2

1 96

(36 + 18ζ(2) − 246ζ(3) + 264ζ(4) − 168ζ(5) + 48ζ(2)ζ(3)

=

k=1

+97ζ(6) − 48ζ(3)2 (469) ∞

H(k)2 k3(k + 1)2(k + 2)2

1 32

(26 + 14ζ(2) + 130ζ(3) − 201ζ(4) + 28ζ(5)

=

k=1

−8ζ(2)ζ(3)) (470)

∞

H(k)2 k2(k + 1)3(k + 2)2

1 8

(14 + 8ζ(2) − 28ζ(3) + 3ζ(4) − 12ζ(5)

=

k=1

+8ζ(2)ζ(3)) (471)

∞

H(k)2 k(k + 1)4(k + 2)2

1 24

(90 + 54ζ(2) − 6ζ(3) − 165ζ(4) − 36ζ(5) + 24ζ(2)ζ(3)

=

k=1

−37ζ(6) + 24ζ(3)2 (472) ∞

H(k)2 (k + 1)5(k + 2)2

1 12

(96 + 60ζ(2) − 24ζ(3) − 165ζ(4) − 54ζ(5) + 36ζ(2)ζ(3)

=

k=1

−37ζ(6) + 24ζ(3)2 − 12ζ(7) + 12ζ(2)ζ(5) − 6ζ(3)ζ(4) (473) ∞

H(k)2 k4(k + 2)3

1 192

(−174 − 18ζ(2) − 6ζ(3) + 225ζ(4) − 144ζ(5) + 48ζ(2)ζ(3)

=

k=1

+97ζ(6) − 48ζ(3)2 (474) ∞

H(k)2 k3(k + 1)(k + 2)3

1 32

(−70 − 12ζ(2) + 80ζ(3) − 13ζ(4) + 8ζ(5)) (475)

=

k=1

∞

H(k)2 k2(k + 1)2(k + 2)3

1 32

(−166 − 38ζ(2) + 30ζ(3) + 175ζ(4) − 12ζ(5)

=

k=1

+8ζ(2)ζ(3)) (476)

∞

H(k)2 k(k + 1)3(k + 2)3

1 16

(194 + 54ζ(2) − 86ζ(3) − 169ζ(4) − 12ζ(5)

=

k=1

+8ζ(2)ζ(3)) (477)

∞

H(k)2 (k + 1)4(k + 2)3

1 24

(−672 − 216ζ(2) + 264ζ(3) + 672ζ(4) + 72ζ(5) − 48ζ(2)ζ(3)

=

k=1

+37ζ(6) − 24ζ(3)2 (478) ∞

H(k)2 k3(k + 2)4

1 192

594 − 54ζ(2) − 186ζ(3) − 255ζ(4) − 37ζ(6) + 24ζ(3)2 (479)

=

k=1

∞

H(k)2 k2(k + 1)(k + 2)4

1 96

(804 − 18ζ(2) − 426ζ(3) − 216ζ(4) − 24ζ(5) − 37ζ(6)

=

k=1

+24ζ(3)2 (480) ∞

H(k)2 k(k + 1)2(k + 2)4

1 96

(2106 + 78ζ(2) − 942ζ(3) − 957ζ(4) − 12ζ(5) − 24ζ(2)ζ(3)

=

k=1

−74ζ(6) + 48ζ(3)2 (481) ∞

H(k)2 (k + 1)3(k + 2)4

1 24

(1344 + 120ζ(2) − 600ζ(3) − 732ζ(4) − 24ζ(5) − 37ζ(6)

=

k=1

+24ζ(3)2 (482) ∞

H(k)2 k2(k + 2)5

1 384

(−3006 + 522ζ(2) + 1086ζ(3) + 603ζ(4) + 756ζ(5) − 312ζ(2)ζ(3)

=

k=1

+292ζ(6) − 192ζ(3)2 − 96ζ(7) + 96ζ(2)ζ(5) − 48ζ(3)ζ(4) (483) ∞

H(k)2 k(k + 1)(k + 2)5

1 64

(1538 − 186ζ(2) − 646ζ(3) − 345ζ(4) − 268ζ(5) + 104ζ(2)ζ(3)

=

k=1

−122ζ(6) + 80ζ(3)2 + 32ζ(7) − 32ζ(2)ζ(5) + 16ζ(3)ζ(4) (484) ∞

H(k)2 (k + 1)2(k + 2)5

1 12

(840 − 60ζ(2) − 360ζ(3) − 249ζ(4) − 102ζ(5) + 36ζ(2)ζ(3)

=

k=1

−55ζ(6) + 36ζ(3)2 + 12ζ(7) − 12ζ(2)ζ(5) + 6ζ(3)ζ(4) (485) ∞

H(k)2 k(k + 2)6

1 384

(6138 − 1170ζ(2) − 1902ζ(3) − 1029ζ(4) − 1788ζ(5) + 648ζ(2)ζ(3)

=

k=1

−698ζ(6) + 336ζ(3)2 − 1056ζ(7) + 288ζ(2)ζ(5) + 432ζ(3)ζ(4) + 672ζ(8) −384ζ(3)ζ(5) − 192M(2,6)) (486)

∞

H(k)2 (k + 1)(k + 2)6

1 24

(1344 − 216ζ(2) − 480ζ(3) − 258ζ(4) − 324ζ(5) + 120ζ(2)ζ(3)

=

k=1

−133ζ(6) + 72ζ(3)2 − 120ζ(7) + 24ζ(2)ζ(5) + 60ζ(3)ζ(4) + 84ζ(8) −48ζ(3)ζ(5) − 24M(2,6)) (487)

∞

H(k)2 (k + 2)7

1 6

(168 − 30ζ(2) − 42ζ(3) − 27ζ(4) − 42ζ(5) + 12ζ(2)ζ(3) − 21ζ(6)

=

k=1

+6ζ(3)2 − 42ζ(7) + 12ζ(2)ζ(5) + 12ζ(3)ζ(4) − 15ζ(8) + 12ζ(3)ζ(5) −ζ(9) + 9ζ(3)ζ(6) + 3ζ(4)ζ(5) − 6ζ(2)ζ(7) − 2ζ(3)3 (488)

∞

H(k)3 k6

1 24

(521ζ(9) − 291ζ(3)ζ(6) − 306ζ(4)ζ(5) + 72ζ(2)ζ(7)

=

k=1

+48ζ(3)3 (489) ∞

H(k)3 k5(k + 1)

1 96

960ζ(4) − 960ζ(5) − 96ζ(2)ζ(3) + 558ζ(6) − 240ζ(3)2

=

k=1

−1386ζ(7) − 192ζ(2)ζ(5) + 1224ζ(3)ζ(4) − 595ζ(8) − 120ζ(2)ζ(3)2

+576ζ(3)ζ(5) + 264M(2,6)) (490)

∞

H(k)3 k4(k + 1)2

1 16

640ζ(4) − 600ζ(5) − 64ζ(2)ζ(3) + 186ζ(6) − 80ζ(3)2

=

k=1

−231ζ(7) − 32ζ(2)ζ(5) + 204ζ(3)ζ(4)) (491)

∞

H(k)3 k3(k + 1)3

1 8

480ζ(4) − 420ζ(5) − 48ζ(2)ζ(3) + 63ζ(6) − 36ζ(3)2 (492)

=

k=1

∞

H(k)3 k2(k + 1)4

1 16

640ζ(4) − 520ζ(5) − 64ζ(2)ζ(3) + 66ζ(6) − 64ζ(3)2

=

k=1

−119ζ(7) − 32ζ(2)ζ(5) + 132ζ(3)ζ(4)) (493)

∞

H(k)3 k(k + 1)5

1 96

960ζ(4) − 720ζ(5) − 96ζ(2)ζ(3) + 198ζ(6) − 192ζ(3)2

=

k=1

−714ζ(7) − 192ζ(2)ζ(5) + 792ζ(3)ζ(4) + 43ζ(8) + 120ζ(2)ζ(3)2 −288ζ(3)ζ(5) + 24M(2,6)) (494)

∞

H(k)3 (k + 1)6

1 24

(197ζ(9) − 111ζ(3)ζ(6) − 198ζ(4)ζ(5) + 72ζ(2)ζ(7)

=

k=1

+24ζ(3)3 (495) ∞

H(k)3 k5(k + 2)

1 384

(12 + 24ζ(2) + 48ζ(3) + 120ζ(4) − 240ζ(5) − 24ζ(2)ζ(3)

=

k=1

+279ζ(6) − 120ζ(3)2 − 1386ζ(7) − 192ζ(2)ζ(5) + 1224ζ(3)ζ(4) − 1190ζ(8) −240ζ(2)ζ(3)2 + 1152ζ(3)ζ(5) + 528M(2,6) (496)

∞

H(k)3 k4(k + 1)(k + 2)

1 64

(4 + 8ζ(2) + 16ζ(3) − 600ζ(4) + 560ζ(5) + 56ζ(2)ζ(3)

=

k=1

−279ζ(6) + 120ζ(3)2 + 462ζ(7) + 64ζ(2)ζ(5) − 408ζ(3)ζ(4) (497) ∞

H(k)3 k3(k + 1)2(k + 2)

1 32

(4 + 8ζ(2) + 16ζ(3) + 680ζ(4) − 640ζ(5) − 72ζ(2)ζ(3)

=

k=1

+93ζ(6) − 40ζ(3)2 (498)

1 16

(4 + 8ζ(2) + 16ζ(3) − 280ζ(4) + 200ζ(5) + 24ζ(2)ζ(3)

=

k2(k + 1)3(k + 2)

k=1

−33ζ(6) + 32ζ(3)2 (499) ∞

H(k)3 k(k + 1)4(k + 2)

1 16

(8 + 16ζ(2) + 32ζ(3) + 80ζ(4) − 120ζ(5) − 16ζ(2)ζ(3)

=

k=1

−119ζ(7) − 32ζ(2)ζ(5) + 132ζ(3)ζ(4)) (500)

∞

H(k)3 (k + 1)5(k + 2)

1 96

(96 + 192ζ(2) + 384ζ(3) − 720ζ(5) − 96ζ(2)ζ(3) − 198ζ(6)

=

k=1

+192ζ(3)2 − 714ζ(7) − 192ζ(2)ζ(5) + 792ζ(3)ζ(4) − 43ζ(8) −120ζ(2)ζ(3)2 + 288ζ(3)ζ(5) − 24M(2,6) (501)

∞

H(k)3 k4(k + 2)2

1 64

(−24 − 28ζ(2) − 36ζ(3) − 47ζ(4) + 150ζ(5) + 16ζ(2)ζ(3)

=

k=1

−93ζ(6) + 40ζ(3)2 + 231ζ(7) + 32ζ(2)ζ(5) − 204ζ(3)ζ(4) (502) ∞

H(k)3 k3(k + 1)(k + 2)2

1 64

(−52 − 64ζ(2) − 88ζ(3) + 506ζ(4) − 260ζ(5) − 24ζ(2)ζ(3)

=

k=1

+93ζ(6) − 40ζ(3)2 (503) ∞

H(k)3 k2(k + 1)2(k + 2)2

1 16

(28 + 36ζ(2) + 52ζ(3) + 87ζ(4) − 190ζ(5)

=

k=1

−24ζ(2)ζ(3)) (504)

∞

H(k)3 k(k + 1)3(k + 2)2

1 16

(60 + 80ζ(2) + 120ζ(3) − 106ζ(4) − 180ζ(5) − 24ζ(2)ζ(3)

=

k=1

−33ζ(6) + 32ζ(3)2 (505) ∞

H(k)3 (k + 1)4(k + 2)2

1 16

(−128 − 176ζ(2) − 272ζ(3) + 132ζ(4) + 480ζ(5) + 64ζ(2)ζ(3)

=

k=1

+66ζ(6) − 64ζ(3)2 + 119ζ(7) + 32ζ(2)ζ(5) − 132ζ(3)ζ(4) (506) ∞

H(k)3 k3(k + 2)3

1 64

(140 + 84ζ(2) + 36ζ(3) − 51ζ(4) − 174ζ(5) − 48ζ(2)ζ(3)

=

k=1

+63ζ(6) − 36ζ(3)2 (507) ∞

H(k)3 k2(k + 1)(k + 2)3

1 64

(332 + 232ζ(2) + 160ζ(3) − 608ζ(4) − 88ζ(5) − 72ζ(2)ζ(3)

=

k=1

+33ζ(6) − 32ζ(3)2 (508) ∞

H(k)3 k(k + 1)2(k + 2)3

1 32

(388 + 304ζ(2) + 264ζ(3) − 434ζ(4) − 468ζ(5)

=

k=1

−120ζ(2)ζ(3) + 33ζ(6) − 32ζ(3)2 (509)

1 4

(112 + 96ζ(2) + 96ζ(3) − 135ζ(4) − 162ζ(5)

=

(k + 1)3(k + 2)3

k=1

−36ζ(2)ζ(3)) (510)

∞

H(k)3 k2(k + 2)4

1 64

(−536 − 132ζ(2) + 132ζ(3) + 335ζ(4) + 82ζ(5) + 64ζ(2)ζ(3)

=

k=1

+41ζ(6) − 16ζ(3)2 + 119ζ(7) + 32ζ(2)ζ(5) − 132ζ(3)ζ(4) (511) ∞

H(k)3 k(k + 1)(k + 2)4

1 64

(−1404 − 496ζ(2) + 104ζ(3) + 1278ζ(4) + 252ζ(5) + 200ζ(2)ζ(3)

=

k=1

+49ζ(6) + 238ζ(7) + 64ζ(2)ζ(5) − 264ζ(3)ζ(4)) (512)

∞

H(k)3 (k + 1)2(k + 2)4

1 16

(896 + 400ζ(2) + 80ζ(3) − 856ζ(4) − 360ζ(5) − 160ζ(2)ζ(3)

=

k=1

−8ζ(6) − 16ζ(3)2 − 119ζ(7) − 32ζ(2)ζ(5) + 132ζ(3)ζ(4) (513) ∞

H(k)3 k(k + 2)5

1 384

(9228 + 432ζ(2) − 3528ζ(3) − 4134ζ(4) − 1740ζ(5) + 408ζ(2)ζ(3)

=

k=1

−1665ζ(6) + 1056ζ(3)2 − 138ζ(7) − 768ζ(2)ζ(5) + 1080ζ(3)ζ(4) + 86ζ(8)

+240ζ(2)ζ(3)2 − 576ζ(3)ζ(5) + 48M(2,6) (514) ∞

H(k)3 (k + 1)(k + 2)5

1 96

(6720 + 960ζ(2) − 1920ζ(3) − 3984ζ(4) − 1248ζ(5) − 96ζ(2)ζ(3)

=

k=1

−906ζ(6) + 528ζ(3)2 − 426ζ(7) − 480ζ(2)ζ(5) + 936ζ(3)ζ(4) + 43ζ(8)

+120ζ(2)ζ(3)2 − 288ζ(3)ζ(5) + 24M(2,6) (515) ∞

H(k)3 (k + 2)6

1 24

(1344 − 72ζ(2) − 504ζ(3) − 414ζ(4) − 396ζ(5) + 144ζ(2)ζ(3)

=

k=1

−243ζ(6) + 144ζ(3)2 − 144ζ(7) + 108ζ(3)ζ(4) + 252ζ(8) − 144ζ(3)ζ(5) −72M(2,6) − 197ζ(9) + 111ζ(3)ζ(6) + 198ζ(4)ζ(5) − 72ζ(2)ζ(7) −24ζ(3)3 (516)

∞

H(k)4 k5

1 12

(436ζ(9) − 279ζ(3)ζ(6) − 258ζ(4)ζ(5) + 84ζ(2)ζ(7)

=

k=1

+40ζ(3)3 (517) ∞

H(k)4 k4(k + 1)

1 144 −4320ζ(5) − 864ζ(2)ζ(3) + 5874ζ(6) + 432ζ(3)2 − 3330ζ(7) −720ζ(2)ζ(5) + 3096ζ(3)ζ(4) − 14833ζ(8) − 4032ζ(2)ζ(3)2

=

k=1

+16704ζ(3)ζ(5) + 3744M(2,6)) (518)

1 8

720ζ(5) + 144ζ(2)ζ(3) − 939ζ(6) − 72ζ(3)2 + 185ζ(7)

=

k3(k + 1)2

k=1

+40ζ(2)ζ(5) − 172ζ(3)ζ(4)) (519)

∞

H(k)4 k2(k + 1)3

1 8 −720ζ(5) − 144ζ(2)ζ(3) + 899ζ(6) + 72ζ(3)2 − 109ζ(7)

=

k=1

−40ζ(2)ζ(5) + 148ζ(3)ζ(4)) (520)

∞

H(k)4 k(k + 1)4

1 144

4320ζ(5) + 864ζ(2)ζ(3) − 5154ζ(6) − 432ζ(3)2 + 1962ζ(7)

=

k=1

+720ζ(2)ζ(5) − 2664ζ(3)ζ(4) + 12415ζ(8) + 3312ζ(2)ζ(3)2 −13824ζ(3)ζ(5) − 3024M(2,6)) (521)

∞

H(k)4 (k + 1)5

1 12

(−174ζ(9) + 99ζ(3)ζ(6) + 222ζ(4)ζ(5) − 84ζ(2)ζ(7)

=

k=1

−32ζ(3)3 (522) ∞

H(k)4 k4(k + 2)

1 576

=

(36 + 108ζ(2) + 396ζ(3) + 666ζ(4) + 1080ζ(5) + 216ζ(2)ζ(3)

k=1

−2937ζ(6) − 216ζ(3)2 + 3330ζ(7) + 720ζ(2)ζ(5) − 3096ζ(3)ζ(4) + 29666ζ(8)

+8064ζ(2)ζ(3)2 − 33408ζ(3)ζ(5) − 7488M(2,6) (523) ∞

H(k)4 k3(k + 1)(k + 2)

1 32

(−4 − 12ζ(2) − 44ζ(3) − 74ζ(4) + 840ζ(5) + 168ζ(2)ζ(3)

=

k=1

−979ζ(6) − 72ζ(3)2 + 370ζ(7) + 80ζ(2)ζ(5) − 344ζ(3)ζ(4) (524) ∞

H(k)4 k2(k + 1)2(k + 2)

1 16

(−4 − 12ζ(2) − 44ζ(3) − 74ζ(4) − 600ζ(5) − 120ζ(2)ζ(3)

=

k=1

+899ζ(6) + 72ζ(3)2 (525) ∞

H(k)4 k(k + 1)3(k + 2)

1 8

(4 + 12ζ(2) + 44ζ(3) + 74ζ(4) − 120ζ(5) − 24ζ(2)ζ(3)

=

k=1

−109ζ(7) − 40ζ(2)ζ(5) + 148ζ(3)ζ(4)) (526)

∞

H(k)4 (k + 1)4(k + 2)

1 144

144 + 432ζ(2) + 1584ζ(3) + 2664ζ(4) − 5154ζ(6) − 432ζ(3)2

=

k=1

−1962ζ(7) − 720ζ(2)ζ(5) + 2664ζ(3)ζ(4) + 12415ζ(8) + 3312ζ(2)ζ(3)2 −13824ζ(3)ζ(5) − 3024M(2,6)) (527)

∞

H(k)4 k3(k + 2)2

1 64

=

(52 + 100ζ(2) + 276ζ(3) + 238ζ(4) + 120ζ(5) + 40ζ(2)ζ(3)

k=1

−939ζ(6) − 72ζ(3)2 + 370ζ(7) + 80ζ(2)ζ(5) − 344ζ(3)ζ(4) (528)

1 4

(7 + 14ζ(2) + 40ζ(3) + 39ζ(4) − 90ζ(5) − 16ζ(2)ζ(3)

=

k2(k + 1)(k + 2)2

k=1

+5ζ(6)) (529)

∞

H(k)4 k(k + 1)2(k + 2)2

1 16

(60 + 124ζ(2) + 364ζ(3) + 386ζ(4) − 120ζ(5) − 8ζ(2)ζ(3)

=

k=1

−859ζ(6) − 72ζ(3)2 (530) ∞

H(k)4 (k + 1)3(k + 2)2

1 8

(64 + 136ζ(2) + 408ζ(3) + 460ζ(4) − 240ζ(5) − 32ζ(2)ζ(3)

=

k=1

−859ζ(6) − 72ζ(3)2 − 109ζ(7) − 40ζ(2)ζ(5) + 148ζ(3)ζ(4) (531) ∞

H(k)4 k2(k + 2)3

1 64

(−332 − 388ζ(2) − 740ζ(3) − 6ζ(4) + 456ζ(5) + 152ζ(2)ζ(3)

=

k=1

+767ζ(6) + 200ζ(3)2 − 218ζ(7) − 80ζ(2)ζ(5) + 296ζ(3)ζ(4) (532) ∞

H(k)4 k(k + 1)(k + 2)3

1 32

(−388 − 500ζ(2) − 1060ζ(3) − 318ζ(4) + 1176ζ(5) + 280ζ(2)ζ(3)

=

k=1

+727ζ(6) + 200ζ(3)2 − 218ζ(7) − 80ζ(2)ζ(5) + 296ζ(3)ζ(4) (533) ∞

H(k)4 (k + 1)2(k + 2)3

1 8

(224 + 312ζ(2) + 712ζ(3) + 352ζ(4) − 648ζ(5) − 144ζ(2)ζ(3)

=

k=1

−793ζ(6) − 136ζ(3)2 + 109ζ(7) + 40ζ(2)ζ(5) − 148ζ(3)ζ(4) (534) ∞

H(k)4 k(k + 2)4

1 576

(12636 + 8460ζ(2) + 9180ζ(3) − 11502ζ(4) − 9864ζ(5)

=

k=1

−4968ζ(2)ζ(3) − 1677ζ(6) − 1944ζ(3)2 − 6606ζ(7) − 1584ζ(2)ζ(5)

+6840ζ(3)ζ(4) + 24830ζ(8) + 6624ζ(2)ζ(3)2 − 27648ζ(3)ζ(5) −6048M(2,6)) (535)

∞

H(k)4 (k + 1)(k + 2)4

1 144

(8064 + 6480ζ(2) + 9360ζ(3) − 4320ζ(4) − 10224ζ(5)

=

k=1

−3744ζ(2)ζ(3) − 4110ζ(6) − 1872ζ(3)2 − 2322ζ(7) − 432ζ(2)ζ(5)

+2088ζ(3)ζ(4) + 12415ζ(8) + 3312ζ(2)ζ(3)2 − 13824ζ(3)ζ(5) −3024M(2,6)) (536)

∞

H(k)4 (k + 2)5

1 24

(−1680 − 600ζ(2) − 120ζ(3) + 1380ζ(4) + 672ζ(5) + 240ζ(2)ζ(3)

=

k=1

+318ζ(6) − 144ζ(3)2 + 570ζ(7) + 336ζ(2)ζ(5) − 864ζ(3)ζ(4) − 43ζ(8) −120ζ(2)ζ(3)2 + 288ζ(3)ζ(5) − 24M(2,6) − 348ζ(9) + 198ζ(3)ζ(6)

+444ζ(4)ζ(5) − 168ζ(2)ζ(7) − 64ζ(3)3 (537)

∞

H(k)5 k4

1 72

(9442ζ(9) − 14685ζ(3)ζ(6) + 4752ζ(4)ζ(5) + 2385ζ(2)ζ(7)

=

k=1

−360ζ(3)3 (538) ∞

H(k)5 k3(k + 1)

1 288

51408ζ(6) + 6480ζ(3)2 − 36918ζ(7) − 8208ζ(2)ζ(5)

=

k=1

−9504ζ(3)ζ(4) − 67811ζ(8) − 19080ζ(2)ζ(3)2 + 78768ζ(3)ζ(5)

+16920M(2,6)) (539)

∞

H(k)5 k2(k + 1)2

1 8

2856ζ(6) + 360ζ(3)2 − 1953ζ(7) − 456ζ(2)ζ(5)

=

k=1

−528ζ(3)ζ(4)) (540)

∞

H(k)5 k(k + 1)3

1 288

51408ζ(6) + 6480ζ(3)2 − 33390ζ(7) − 8208ζ(2)ζ(5)

=

k=1

−9504ζ(3)ζ(4) − 65621ζ(8) − 17640ζ(2)ζ(3)2 + 72432ζ(3)ζ(5)

+15480M(2,6)) (541)

∞

H(k)5 (k + 1)4

1 72

(7120ζ(9) − 12885ζ(3)ζ(6) + 4752ζ(4)ζ(5) + 2385ζ(2)ζ(7)

=

k=1

−360ζ(3)3 (542) ∞

H(k)5 k3(k + 2)

1 576

=

(72 + 288ζ(2) + 1512ζ(3) + 4518ζ(4) + 5112ζ(5) + 1080ζ(2)ζ(3)

k=1

+12852ζ(6) + 1620ζ(3)2 − 18459ζ(7) − 4104ζ(2)ζ(5) − 4752ζ(3)ζ(4) −67811ζ(8) − 19080ζ(2)ζ(3)2 + 78768ζ(3)ζ(5) + 16920M(2,6) (543)

∞

H(k)5 k2(k + 1)(k + 2)

1 32

=

(8 + 32ζ(2) + 168ζ(3) + 502ζ(4) + 568ζ(5) + 120ζ(2)ζ(3)

k=1

−4284ζ(6) − 540ζ(3)2 + 2051ζ(7) + 456ζ(2)ζ(5) + 528ζ(3)ζ(4) (544) ∞

H(k)5 k(k + 1)2(k + 2)

1 16

=

(8 + 32ζ(2) + 168ζ(3) + 502ζ(4) + 568ζ(5) + 120ζ(2)ζ(3)

k=1

+1428ζ(6) + 180ζ(3)2 − 1855ζ(7) − 456ζ(2)ζ(5) − 528ζ(3)ζ(4) (545) ∞

H(k)5 (k + 1)3(k + 2)

1 288

=

(288 + 1152ζ(2) + 6048ζ(3) + 18072ζ(4) + 20448ζ(5)

k=1

+4320ζ(2)ζ(3) − 33390ζ(7) − 8208ζ(2)ζ(5) − 9504ζ(3)ζ(4) + 65621ζ(8)

+17640ζ(2)ζ(3)2 − 72432ζ(3)ζ(5) − 15480M(2,6) (546) ∞

H(k)5 k2(k + 2)2

1 96

(−168 − 456ζ(2) − 1896ζ(3) − 3858ζ(4) − 1608ζ(5) − 480ζ(2)ζ(3)

=

k=1

+11ζ(6) − 180ζ(3)2 + 5859ζ(7) + 1368ζ(2)ζ(5) + 1584ζ(3)ζ(4) (547)

∞

H(k)5 k(k + 1)(k + 2)2

1 96

(−360 − 1008ζ(2) − 4296ζ(3) − 9222ζ(4) − 4920ζ(5)

=

k=1

−1320ζ(2)ζ(3) + 12874ζ(6) + 1260ζ(3)2 + 5565ζ(7) + 1368ζ(2)ζ(5)

+1584ζ(3)ζ(4)) (548)

∞

H(k)5 (k + 1)2(k + 2)2

1 24

(−192 − 552ζ(2) − 2400ζ(3) − 5364ζ(4) − 3312ζ(5)

=

k=1

−840ζ(2)ζ(3) + 4295ζ(6) + 360ζ(3)2 + 5565ζ(7) + 1368ζ(2)ζ(5)

+1584ζ(3)ζ(4)) (549)

∞

H(k)5 k(k + 2)3

1 576

(6984 + 12528ζ(2) + 40104ζ(3) + 48726ζ(4) − 13896ζ(5)

=

k=1

−2520ζ(2)ζ(3) − 58518ζ(6) − 10620ζ(3)2 + 2925ζ(7) + 3096ζ(2)ζ(5) −31392ζ(3)ζ(4) − 65621ζ(8) − 17640ζ(2)ζ(3)2 + 72432ζ(3)ζ(5)

+15480M(2,6)) (550)

∞

H(k)5 (k + 1)(k + 2)3

1 288

(8064 + 15552ζ(2) + 52992ζ(3) + 76392ζ(4) + 864ζ(5)

=

k=1

+1440ζ(2)ζ(3) − 97140ζ(6) − 14400ζ(3)2 − 13770ζ(7) − 1008ζ(2)ζ(5) −36144ζ(3)ζ(4) − 65621ζ(8) − 17640ζ(2)ζ(3)2 + 72432ζ(3)ζ(5)

+15480M(2,6)) (551)

∞

H(k)5 (k + 2)4

1 144

(8064 + 9360ζ(2) + 22320ζ(3) + 11520ζ(4) − 17136ζ(5)

=

k=1

−5760ζ(2)ζ(3) − 22050ζ(6) − 6480ζ(3)2 − 900ζ(7) + 720ζ(2)ζ(5) −1440ζ(3)ζ(4) + 62075ζ(8) + 16560ζ(2)ζ(3)2 − 69120ζ(3)ζ(5) − 15120M(2,6) −14240ζ(9) + 25770ζ(3)ζ(6) − 9504ζ(4)ζ(5) − 4770ζ(2)ζ(7)

+720ζ(3)3 (552) ∞

H(k)6 k3

1 24

(7474ζ(9) − 13122ζ(3)ζ(6) + 6048ζ(4)ζ(5) + 1953ζ(2)ζ(7)

=

k=1

−544ζ(3)3 (553) ∞

H(k)6 k2(k + 1)

1 8

(−5152ζ(7) − 1160ζ(2)ζ(5) − 2376ζ(3)ζ(4) + 5843ζ(8)

=

k=1

−328ζ(2)ζ(3)2 + 3896ζ(3)ζ(5) + 456M(2,6) (554) ∞

H(k)6 k(k + 1)2

1 24

(15456ζ(7) + 3480ζ(2)ζ(5) + 7128ζ(3)ζ(4) − 17027ζ(8)

=

k=1

+924ζ(2)ζ(3)2 − 11328ζ(3)ζ(5) − 1308M(2,6) (555)

1 24

(−6146ζ(9) + 12582ζ(3)ζ(6) − 5832ζ(4)ζ(5) − 1953ζ(2)ζ(7)

=

(k + 1)3

k=1

+536ζ(3)3 (556) ∞

H(k)6 k2(k + 2)

1 16

=

(4 + 20ζ(2) + 136ζ(3) + 571ζ(4) + 1142ζ(5) + 244ζ(2)ζ(3)

k=1

+2097ζ(6) + 268ζ(3)2 + 2576ζ(7) + 580ζ(2)ζ(5) + 1188ζ(3)ζ(4) − 5843ζ(8)

+328ζ(2)ζ(3)2 − 3896ζ(3)ζ(5) − 456M(2,6) (557) ∞

H(k)6 k(k + 1)(k + 2)

1 8

(−4 − 20ζ(2) − 136ζ(3) − 571ζ(4) − 1142ζ(5) − 244ζ(2)ζ(3)

=

k=1

−2097ζ(6) − 268ζ(3)2 + 2576ζ(7) + 580ζ(2)ζ(5) + 1188ζ(3)ζ(4) (558) ∞

H(k)6 (k + 1)2(k + 2)

1 24

(−24 − 120ζ(2) − 816ζ(3) − 3426ζ(4) − 6852ζ(5) − 1464ζ(2)ζ(3)

=

k=1

−12582ζ(6) − 1608ζ(3)2 + 17027ζ(8) − 924ζ(2)ζ(3)2 + 11328ζ(3)ζ(5)

+1308M(2,6)) (559)

∞

H(k)6 k(k + 2)2

1 48

=

(180 + 636ζ(2) + 3528ζ(3) + 11001ζ(4) + 13530ζ(5) + 3180ζ(2)ζ(3)

k=1

+5988ζ(6) + 1332ζ(3)2 − 8967ζ(7) − 2364ζ(2)ζ(5) − 1188ζ(3)ζ(4) − 17027ζ(8)

+924ζ(2)ζ(3)2 − 11328ζ(3)ζ(5) − 1308M(2,6) (560) ∞

H(k)6 (k + 1)(k + 2)2

1 24

=

(192 + 696ζ(2) + 3936ζ(3) + 12714ζ(4) + 16956ζ(5)

k=1

+3912ζ(2)ζ(3) + 12279ζ(6) + 2136ζ(3)2 − 16695ζ(7) − 4104ζ(2)ζ(5) −4752ζ(3)ζ(4) − 17027ζ(8) + 924ζ(2)ζ(3)2 − 11328ζ(3)ζ(5) − 1308M(2,6)

(561)

∞

H(k)6 (k + 2)3

1 48

=

(1344 + 3312ζ(2) + 14832ζ(3) + 33120ζ(4) + 20592ζ(5) + 5184ζ(2)ζ(3)

k=1

−24396ζ(6) − 3024ζ(3)2 − 23580ζ(7) − 4608ζ(2)ζ(5) − 22824ζ(3)ζ(4) −65621ζ(8) − 17640ζ(2)ζ(3)2 + 72432ζ(3)ζ(5) + 15480M(2,6) + 12292ζ(9) −25164ζ(3)ζ(6) + 11664ζ(4)ζ(5) + 3906ζ(2)ζ(7) − 1072ζ(3)3 (562)

∞

H(k)7 k2

1 72

=

(276341ζ(9) + 88665ζ(3)ζ(6) + 143163ζ(4)ζ(5) + 59166ζ(2)ζ(7)

k=1

+4032ζ(3)3 (563) ∞

H(k)7 k(k + 1)

1 18

119774ζ(8) + 3024ζ(2)ζ(3)2 + 27405ζ(3)ζ(5) (564)

=

k=1

1 72

=

(269402ζ(9) + 88665ζ(3)ζ(6) + 141273ζ(4)ζ(5) + 59166ζ(2)ζ(7)

(k + 1)2

k=1

+4032ζ(3)3 (565) ∞

H(k)7 k(k + 2)

1 288

=

(144 + 864ζ(2) + 7200ζ(3) + 38664ζ(4) + 108504ζ(5) + 23184ζ(2)ζ(3)

k=1

+352887ζ(6) + 45864ζ(3)2 + 319554ζ(7) + 73080ζ(2)ζ(5) + 148932ζ(3)ζ(4)

+958192ζ(8) + 24192ζ(2)ζ(3)2 + 219240ζ(3)ζ(5) (566) ∞

H(k)7 (k + 1)(k + 2)

1 48

=

(48 + 288ζ(2) + 2400ζ(3) + 12888ζ(4) + 36168ζ(5) + 7728ζ(2)ζ(3)

k=1

+117629ζ(6) + 15288ζ(3)2 + 106518ζ(7) + 24360ζ(2)ζ(5) + 49644ζ(3)ζ(4) (567) ∞

H(k)7 (k + 2)2

1 144

(−1152 − 5040ζ(2) − 34992ζ(3) − 146340ζ(4) − 287712ζ(5)

=

k=1

−64512ζ(2)ζ(3) − 525384ζ(6) − 76608ζ(3)2 + 31041ζ(7) + 13104ζ(2)ζ(5) −49140ζ(3)ζ(4) + 715134ζ(8) − 38808ζ(2)ζ(3)2 + 475776ζ(3)ζ(5) + 54936M(2,6)

+538804ζ(9) + 177330ζ(3)ζ(6) + 282546ζ(4)ζ(5) + 118332ζ(2)ζ(7)

+8064ζ(3)3 (568)

##### Formulas for order r = m + n + p + q = 10:

∞

1 4

H(k) k9

11ζ(10) − 4ζ(3)ζ(7) − 2ζ(5)2 (569)

=

k=1

∞

H(k) k8(k + 1)

1 4

4ζ(2) − 8ζ(3) + 5ζ(4) − 12ζ(5) + 4ζ(2)ζ(3) + 7ζ(6) − 2ζ(3)2

=

k=1

−16ζ(7) + 4ζ(2)ζ(5) + 4ζ(3)ζ(4) + 9ζ(8) − 4ζ(3)ζ(5) − 20ζ(9)

+4ζ(3)ζ(6) + 4ζ(4)ζ(5) + 4ζ(2)ζ(7)) (570)

∞

1 4

H(k) k7(k + 1)2

(28ζ(2) − 52ζ(3) + 25ζ(4) − 48ζ(5) + 16ζ(2)ζ(3) + 21ζ(6)

=

k=1

−6ζ(3)2 − 32ζ(7) + 8ζ(2)ζ(5) + 8ζ(3)ζ(4) + 9ζ(8) − 4ζ(3)ζ(5) (571) ∞

1 4

H(k) k6(k + 1)3

(−84ζ(2) + 144ζ(3) − 49ζ(4) + 72ζ(5) − 24ζ(2)ζ(3) − 21ζ(6)

=

k=1

+6ζ(3)2 + 16ζ(7) − 4ζ(2)ζ(5) − 4ζ(3)ζ(4) (572) ∞

H(k) k5(k + 1)4

1 4

(140ζ(2) − 220ζ(3) + 45ζ(4) − 56ζ(5) + 20ζ(2)ζ(3) + 7ζ(6)

=

k=1

−2ζ(3)2 (573) ∞

H(k) k4(k + 1)5

1 4

(−140ζ(2) + 200ζ(3) − 15ζ(4) + 44ζ(5) − 20ζ(2)ζ(3) + 3ζ(6)

=

k=1

−2ζ(3)2 (574) ∞

1 4

H(k) k3(k + 1)6

(84ζ(2) − 108ζ(3) − 5ζ(4) − 48ζ(5) + 24ζ(2)ζ(3) − 9ζ(6)

=

k=1

+6ζ(3)2 − 12ζ(7) + 4ζ(2)ζ(5) + 4ζ(3)ζ(4) (575) ∞

1 4

H(k) k2(k + 1)7

(28ζ(2) − 32ζ(3) − 5ζ(4) − 32ζ(5) + 16ζ(2)ζ(3) − 9ζ(6)

=

k=1

+6ζ(3)2 − 24ζ(7) + 8ζ(2)ζ(5) + 8ζ(3)ζ(4) − 5ζ(8) + 4ζ(3)ζ(5) (576) ∞

H(k) k(k + 1)8

1 4

4ζ(2) − 4ζ(3) − ζ(4) − 8ζ(5) + 4ζ(2)ζ(3) − 3ζ(6) + 2ζ(3)2

=

k=1

−12ζ(7) + 4ζ(2)ζ(5) + 4ζ(3)ζ(4) − 5ζ(8) + 4ζ(3)ζ(5) − 16ζ(9)

+4ζ(3)ζ(6) + 4ζ(4)ζ(5) + 4ζ(2)ζ(7)) (577)

∞

H(k) (k + 1)9

1 4

7ζ(10) − 4ζ(3)ζ(7) − 2ζ(5)2 (578)

=

k=1

∞

1 256

H(k) k8(k + 2)

(−1 − ζ(2) + 4ζ(3) − 5ζ(4) + 24ζ(5) − 8ζ(2)ζ(3) − 28ζ(6)

=

k=1

+8ζ(3)2 + 128ζ(7) − 32ζ(2)ζ(5) − 32ζ(3)ζ(4) − 144ζ(8) + 64ζ(3)ζ(5)

+640ζ(9) − 128ζ(3)ζ(6) − 128ζ(4)ζ(5) − 128ζ(2)ζ(7)) (579)

H(k) k7(k + 1)(k + 2)

1 128

(1 − 127ζ(2) + 252ζ(3) − 155ζ(4) + 360ζ(5) − 120ζ(2)ζ(3)

=

k=1

−196ζ(6) + 56ζ(3)2 + 384ζ(7) − 96ζ(2)ζ(5) − 96ζ(3)ζ(4) − 144ζ(8)

+64ζ(3)ζ(5)) (580)

∞

1 64

H(k) k6(k + 1)2(k + 2)

(1 + 321ζ(2) − 580ζ(3) + 245ζ(4) − 408ζ(5) + 136ζ(2)ζ(3)

=

k=1

+140ζ(6) − 40ζ(3)2 − 128ζ(7) + 32ζ(2)ζ(5) + 32ζ(3)ζ(4) (581) ∞

1 32

H(k) k5(k + 1)3(k + 2)

(−1 + 351ζ(2) − 572ζ(3) + 147ζ(4) − 168ζ(5) + 56ζ(2)ζ(3)

=

k=1

+28ζ(6) − 8ζ(3)2 (582) ∞

H(k) k4(k + 1)4(k + 2)

1 16

(1 + 209ζ(2) − 308ζ(3) + 33ζ(4) − 56ζ(5) + 24ζ(2)ζ(3)) (583)

=

k=1

∞

H(k) k3(k + 1)5(k + 2)

1 8

(−1 + 71ζ(2) − 92ζ(3) − 3ζ(4) − 32ζ(5) + 16ζ(2)ζ(3) − 6ζ(6)

=

k=1

+4ζ(3)2 (584) ∞

H(k) k2(k + 1)6(k + 2)

1 4

(−1 − 13ζ(2) + 16ζ(3) + 2ζ(4) + 16ζ(5) − 8ζ(2)ζ(3) + 3ζ(6)

=

k=1

−2ζ(3)2 + 12ζ(7) − 4ζ(2)ζ(5) − 4ζ(3)ζ(4) (585) ∞

H(k) k(k + 1)7(k + 2)

1 4 −2 + 2ζ(2) − ζ(4) − 3ζ(6) + 2ζ(3)2 − 5ζ(8)

=

k=1

+4ζ(3)ζ(5)) (586)

∞

H(k) (k + 1)8(k + 2)

1 4

4 − 4ζ(3) + ζ(4) − 8ζ(5) + 4ζ(2)ζ(3) + 3ζ(6) − 2ζ(3)2

=

k=1

−12ζ(7) + 4ζ(2)ζ(5) + 4ζ(3)ζ(4) + 5ζ(8) − 4ζ(3)ζ(5) − 16ζ(9)

+4ζ(3)ζ(6) + 4ζ(4)ζ(5) + 4ζ(2)ζ(7)) (587)

∞

1 256

H(k) k7(k + 2)2

(11 + 5ζ(2) − 26ζ(3) + 25ζ(4) − 96ζ(5) + 32ζ(2)ζ(3) + 84ζ(6)

=

k=1

−24ζ(3)2 − 256ζ(7) + 64ζ(2)ζ(5) + 64ζ(3)ζ(4) + 144ζ(8) −64ζ(3)ζ(5)) (588)

∞

H(k) k6(k + 1)(k + 2)2

1 64

(6 − 61ζ(2) + 113ζ(3) − 65ζ(4) + 132ζ(5) − 44ζ(2)ζ(3)

=

k=1

−56ζ(6) + 16ζ(3)2 + 64ζ(7) − 16ζ(2)ζ(5) − 16ζ(3)ζ(4) (589)

1 64

H(k) k5(k + 1)2(k + 2)2

(13 + 199ζ(2) − 354ζ(3) + 115ζ(4) − 144ζ(5) + 48ζ(2)ζ(3)

=

k=1

+28ζ(6) − 8ζ(3)2 (590) ∞

1 16

H(k) k4(k + 1)3(k + 2)2

(7 − 76ζ(2) + 109ζ(3) − 16ζ(4) + 12ζ(5)

=

k=1

−4ζ(2)ζ(3)) (591)

∞

1 16

H(k) k3(k + 1)4(k + 2)2

(15 + 57ζ(2) − 90ζ(3) + ζ(4) − 32ζ(5)

=

k=1

+16ζ(2)ζ(3)) (592)

∞

1 4

H(k) k2(k + 1)5(k + 2)2

8 − 7ζ(2) + ζ(3) + 2ζ(4) + 3ζ(6) − 2ζ(3)2 (593)

=

k=1

∞

H(k) k(k + 1)6(k + 2)2

1 4

(17 − ζ(2) − 14ζ(3) + 2ζ(4) − 16ζ(5) + 8ζ(2)ζ(3) + 3ζ(6)

=

k=1

−2ζ(3)2 − 12ζ(7) + 4ζ(2)ζ(5) + 4ζ(3)ζ(4) (594) ∞

H(k) (k + 1)7(k + 2)2

1 4

(36 − 4ζ(2) − 28ζ(3) + 5ζ(4) − 32ζ(5) + 16ζ(2)ζ(3) + 9ζ(6)

=

k=1

−6ζ(3)2 − 24ζ(7) + 8ζ(2)ζ(5) + 8ζ(3)ζ(4) + 5ζ(8) − 4ζ(3)ζ(5) (595) ∞

H(k) k6(k + 2)3

1 256

(57 + 5ζ(2) − 76ζ(3) + 49ζ(4) − 144ζ(5) + 48ζ(2)ζ(3) + 84ζ(6)

=

k=1

−24ζ(3)2 − 128ζ(7) + 32ζ(2)ζ(5) + 32ζ(3)ζ(4) (596) ∞

H(k) k5(k + 1)(k + 2)3

1 128

(69 − 117ζ(2) + 150ζ(3) − 81ζ(4) + 120ζ(5) − 40ζ(2)ζ(3)

=

k=1

−28ζ(6) + 8ζ(3)2 (597) ∞

H(k) k4(k + 1)2(k + 2)3

1 32

(41 + 41ζ(2) − 102ζ(3) + 17ζ(4) − 12ζ(5)

=

k=1

+4ζ(2)ζ(3)) (598)

∞

1 16

H(k) k3(k + 1)3(k + 2)3

(−48 + 35ζ(2) − 7ζ(3) − ζ(4)) (599)

=

k=1

∞

H(k) k2(k + 1)4(k + 2)3

1 16

(111 − 13ζ(2) − 76ζ(3) + 3ζ(4) − 32ζ(5)

=

k=1

+16ζ(2)ζ(3)) (600)

∞

H(k) k(k + 1)5(k + 2)3

1 8

(−127 + 27ζ(2) + 74ζ(3) − 7ζ(4) + 32ζ(5) − 16ζ(2)ζ(3)

=

k=1

−6ζ(6) + 4ζ(3)2 (601)

1 4

H(k) (k + 1)6(k + 2)3

(−144 + 28ζ(2) + 88ζ(3) − 9ζ(4) + 48ζ(5) − 24ζ(2)ζ(3)

=

k=1

−9ζ(6) + 6ζ(3)2 + 12ζ(7) − 4ζ(2)ζ(5) − 4ζ(3)ζ(4) (602) ∞

1 256

H(k) k5(k + 2)4

(187 − 23ζ(2) − 138ζ(3) + 37ζ(4) − 112ζ(5) + 40ζ(2)ζ(3)

=

k=1

+28ζ(6) − 8ζ(3)2 (603) ∞

1 32

H(k) k4(k + 1)(k + 2)4

(64 − 35ζ(2) + 3ζ(3) − 11ζ(4) + 2ζ(5)) (604)

=

k=1

∞

1 32

H(k) k3(k + 1)2(k + 2)4

(169 − 29ζ(2) − 96ζ(3) − 5ζ(4) − 8ζ(5)

=

k=1

+4ζ(2)ζ(3)) (605)

∞

1 16

H(k) k2(k + 1)3(k + 2)4

(217 − 64ζ(2) − 89ζ(3) − 4ζ(4) − 8ζ(5)

=

k=1

+4ζ(2)ζ(3)) (606)

∞

H(k) k(k + 1)4(k + 2)4

1 16

(545 − 141ζ(2) − 254ζ(3) − 5ζ(4) − 48ζ(5)

=

k=1

+24ζ(2)ζ(3)) (607)

∞

1 4

H(k) (k + 1)5(k + 2)4

(336 − 84ζ(2) − 164ζ(3) + ζ(4) − 40ζ(5) + 20ζ(2)ζ(3)

=

k=1

+3ζ(6) − 2ζ(3)2 (608) ∞

H(k) k4(k + 2)5

1 256

(443 − 93ζ(2) − 188ζ(3) − 33ζ(4) − 104ζ(5) + 40ζ(2)ζ(3)

=

k=1

−12ζ(6) + 8ζ(3)2 (609) ∞

H(k) k3(k + 1)(k + 2)5

1 128

(−699 + 233ζ(2) + 176ζ(3) + 77ζ(4) + 96ζ(5) − 40ζ(2)ζ(3)

=

k=1

+12ζ(6) − 8ζ(3)2 (610) ∞

1 64

H(k) k2(k + 1)2(k + 2)5

(1037 − 291ζ(2) − 368ζ(3) − 87ζ(4) − 112ζ(5) + 48ζ(2)ζ(3)

=

k=1

−12ζ(6) + 8ζ(3)2 (611) ∞

1 32

H(k) k(k + 1)3(k + 2)5

(1471 − 419ζ(2) − 546ζ(3) − 95ζ(4) − 128ζ(5) + 56ζ(2)ζ(3)

=

k=1

−12ζ(6) + 8ζ(3)2 (612)

1 4

H(k) (k + 1)4(k + 2)5

(−504 + 140ζ(2) + 200ζ(3) + 25ζ(4) + 44ζ(5) − 20ζ(2)ζ(3)

=

k=1

+3ζ(6) − 2ζ(3)2 (613) ∞

1 256

H(k) k3(k + 2)6

(825 − 177ζ(2) − 222ζ(3) − 133ζ(4) − 176ζ(5) + 48ζ(2)ζ(3)

=

k=1

−68ζ(6) + 24ζ(3)2 − 96ζ(7) + 32ζ(2)ζ(5) + 32ζ(3)ζ(4) (614) ∞

1 64

H(k) k2(k + 1)(k + 2)6

(762 − 205ζ(2) − 199ζ(3) − 105ζ(4) − 136ζ(5) + 44ζ(2)ζ(3)

=

k=1

−40ζ(6) + 16ζ(3)2 − 48ζ(7) + 16ζ(2)ζ(5) + 16ζ(3)ζ(4) (615) ∞

1 64

H(k) k(k + 1)2(k + 2)6

(2561 − 701ζ(2) − 766ζ(3) − 297ζ(4) − 384ζ(5) + 136ζ(2)ζ(3)

=

k=1

−92ζ(6) + 40ζ(3)2 − 96ζ(7) + 32ζ(2)ζ(5) + 32ζ(3)ζ(4) (616) ∞

1 4

H(k) (k + 1)3(k + 2)6

(504 − 140ζ(2) − 164ζ(3) − 49ζ(4) − 64ζ(5) + 24ζ(2)ζ(3)

=

k=1

−13ζ(6) + 6ζ(3)2 − 12ζ(7) + 4ζ(2)ζ(5) + 4ζ(3)ζ(4) (617) ∞

H(k) k2(k + 2)7

1 256

(1291 − 233ζ(2) − 244ζ(3) − 213ζ(4) − 240ζ(5) + 32ζ(2)ζ(3)

=

k=1

−164ζ(6) + 24ζ(3)2 − 256ζ(7) + 64ζ(2)ζ(5) + 64ζ(3)ζ(4) − 80ζ(8)

+64ζ(3)ζ(5)) (618)

∞

H(k) k(k + 1)(k + 2)7

1 128

(−2815 + 643ζ(2) + 642ζ(3) + 423ζ(4) + 512ζ(5) − 120ζ(2)ζ(3)

=

k=1

+244ζ(6) − 56ζ(3)2 + 352ζ(7) − 96ζ(2)ζ(5) − 96ζ(3)ζ(4) + 80ζ(8) −64ζ(3)ζ(5)) (619)

∞

H(k) (k + 1)2(k + 2)7

1 4

(336 − 84ζ(2) − 88ζ(3) − 45ζ(4) − 56ζ(5) + 16ζ(2)ζ(3)

=

k=1

−21ζ(6) + 6ζ(3)2 − 28ζ(7) + 8ζ(2)ζ(5) + 8ζ(3)ζ(4) − 5ζ(8)

+4ζ(3)ζ(5)) (620)

∞

1 256

H(k) k(k + 2)8

(1793 − 253ζ(2) − 254ζ(3) − 249ζ(4) − 256ζ(5) + 8ζ(2)ζ(3)

=

k=1

−236ζ(6) + 8ζ(3)2 − 288ζ(7) + 32ζ(2)ζ(5) + 32ζ(3)ζ(4) − 208ζ(8)

+64ζ(3)ζ(5) − 512ζ(9) + 128ζ(3)ζ(6) + 128ζ(4)ζ(5) + 128ζ(2)ζ(7)) (621)

∞

1 4

H(k) (k + 1)(k + 2)8

(144 − 28ζ(2) − 28ζ(3) − 21ζ(4) − 24ζ(5) + 4ζ(2)ζ(3) − 15ζ(6)

=

k=1

+2ζ(3)2 − 20ζ(7) + 4ζ(2)ζ(5) + 4ζ(3)ζ(4) − 9ζ(8) + 4ζ(3)ζ(5) −16ζ(9) + 4ζ(3)ζ(6) + 4ζ(4)ζ(5) + 4ζ(2)ζ(7)) (622)

1 4

H(k) (k + 2)9

(−36 + 4ζ(2) + 4ζ(3) + 4ζ(4) + 4ζ(5) + 4ζ(6) + 4ζ(7) + 4ζ(8)

=

k=1

+4ζ(9) + 7ζ(10) − 4ζ(3)ζ(7) − 2ζ(5)2 (623) ∞

H(k)2 k8

= M(2,8) (624)

k=1

∞

H(k)2 k7(k + 1)

1 24

72ζ(3) − 102ζ(4) + 84ζ(5) − 24ζ(2)ζ(3) − 97ζ(6) + 48ζ(3)2

=

k=1

+144ζ(7) − 24ζ(2)ζ(5) − 60ζ(3)ζ(4) − 24M(2,6) + 220ζ(9) − 84ζ(3)ζ(6) −60ζ(4)ζ(5) − 24ζ(2)ζ(7) + 8ζ(3)3 (625)

∞

H(k)2 k6(k + 1)2

1 8

(144ζ(3) − 192ζ(4) + 112ζ(5) − 32ζ(2)ζ(3) − 97ζ(6)

=

k=1

+48ζ(3)2 + 96ζ(7) − 16ζ(2)ζ(5) − 40ζ(3)ζ(4) − 8M(2,6) (626) ∞

H(k)2 k5(k + 1)3

1 8

(360ζ(3) − 450ζ(4) + 180ζ(5) − 56ζ(2)ζ(3) − 97ζ(6)

=

k=1

+48ζ(3)2 + 48ζ(7) − 8ζ(2)ζ(5) − 20ζ(3)ζ(4) (627) ∞

H(k)2 k4(k + 1)4

1 12

(−720ζ(3) + 840ζ(4) − 240ζ(5) + 96ζ(2)ζ(3) + 67ζ(6)

=

k=1

−36ζ(3)2 (628) ∞

H(k)2 k3(k + 1)5

1 8

(360ζ(3) − 390ζ(4) + 100ζ(5) − 56ζ(2)ζ(3) − 37ζ(6)

=

k=1

+24ζ(3)2 + 8ζ(7) − 8ζ(2)ζ(5) + 4ζ(3)ζ(4) (629) ∞

H(k)2 k2(k + 1)6

1 8

(−144ζ(3) + 144ζ(4) − 48ζ(5) + 32ζ(2)ζ(3) + 37ζ(6)

=

k=1

−24ζ(3)2 − 16ζ(7) + 16ζ(2)ζ(5) − 8ζ(3)ζ(4) − 28ζ(8) + 16ζ(3)ζ(5)

+8M(2,6)) (630)

∞

H(k)2 k(k + 1)7

1 24

72ζ(3) − 66ζ(4) + 36ζ(5) − 24ζ(2)ζ(3) − 37ζ(6) + 24ζ(3)2

=

k=1

+24ζ(7) − 24ζ(2)ζ(5) + 12ζ(3)ζ(4) + 84ζ(8) − 48ζ(3)ζ(5) − 24M(2,6) −4ζ(9) + 36ζ(3)ζ(6) + 12ζ(4)ζ(5) − 24ζ(2)ζ(7) − 8ζ(3)3 (631)

∞

H(k)2 (k + 1)8

- 1

- 2


9ζ(10) − 4ζ(3)ζ(7) − 2ζ(5)2 − 2M(2,8) (632)

=

k=1

∞

H(k)2 k7(k + 2)

1 768

(6 + 6ζ(2) + 18ζ(3) − 51ζ(4) + 84ζ(5) − 24ζ(2)ζ(3) − 194ζ(6)

=

k=1

+96ζ(3)2 + 576ζ(7) − 96ζ(2)ζ(5) − 240ζ(3)ζ(4) − 192M(2,6) + 3520ζ(9) −1344ζ(3)ζ(6) − 960ζ(4)ζ(5) − 384ζ(2)ζ(7) + 128ζ(3)3 (633)

1 384

(6 + 6ζ(2) − 1134ζ(3) + 1581ζ(4) − 1260ζ(5) + 360ζ(2)ζ(3)

=

k6(k + 1)(k + 2)

k=1

+1358ζ(6) − 672ζ(3)2 − 1728ζ(7) + 288ζ(2)ζ(5) + 720ζ(3)ζ(4)

+192M(2,6)) (634)

∞

H(k)2 k5(k + 1)2(k + 2)

1 192

(6 + 6ζ(2) + 2322ζ(3) − 3027ζ(4) + 1428ζ(5)

=

k=1

−408ζ(2)ζ(3) − 970ζ(6) + 480ζ(3)2 + 576ζ(7) − 96ζ(2)ζ(5) −240ζ(3)ζ(4)) (635)

∞

H(k)2 k4(k + 1)3(k + 2)

1 96

(6 + 6ζ(2) − 1998ζ(3) + 2373ζ(4) − 732ζ(5) + 264ζ(2)ζ(3)

=

k=1

+194ζ(6) − 96ζ(3)2 (636) ∞

H(k)2 k3(k + 1)4(k + 2)

1 48

(6 + 6ζ(2) + 882ζ(3) − 987ζ(4) + 228ζ(5) − 120ζ(2)ζ(3)

=

k=1

−74ζ(6) + 48ζ(3)2 (637) ∞

H(k)2 k2(k + 1)5(k + 2)

1 24

(6 + 6ζ(2) − 198ζ(3) + 183ζ(4) − 72ζ(5) + 48ζ(2)ζ(3)

=

k=1

+37ζ(6) − 24ζ(3)2 − 24ζ(7) + 24ζ(2)ζ(5) − 12ζ(3)ζ(4) (638) ∞

H(k)2 k(k + 1)6(k + 2)

1 24

12 + 12ζ(2) + 36ζ(3) − 66ζ(4) − 37ζ(6) + 24ζ(3)2 + 84ζ(8)

=

k=1

−48ζ(3)ζ(5) − 24M(2,6)) (639)

∞

H(k)2 (k + 1)7(k + 2)

1 24

(24 + 24ζ(2) − 66ζ(4) − 36ζ(5) + 24ζ(2)ζ(3) − 37ζ(6)

=

k=1

+24ζ(3)2 − 24ζ(7) + 24ζ(2)ζ(5) − 12ζ(3)ζ(4) + 84ζ(8) − 48ζ(3)ζ(5) −24M(2,6) + 4ζ(9) − 36ζ(3)ζ(6) − 12ζ(4)ζ(5) + 24ζ(2)ζ(7) + 8ζ(3)3 (640)

∞

H(k)2 k6(k + 2)2

1 128

(12 + 6ζ(2) + 14ζ(3) − 48ζ(4) + 56ζ(5) − 16ζ(2)ζ(3)

=

k=1

−97ζ(6) + 48ζ(3)2 + 192ζ(7) − 32ζ(2)ζ(5) − 80ζ(3)ζ(4) − 32M(2,6) (641) ∞

H(k)2 k5(k + 1)(k + 2)2

1 384

(78 + 42ζ(2) − 1050ζ(3) + 1293ζ(4) − 924ζ(5)

=

k=1

+264ζ(2)ζ(3) + 776ζ(6) − 384ζ(3)2 − 576ζ(7) + 96ζ(2)ζ(5)

+240ζ(3)ζ(4)) (642)

∞

H(k)2 k4(k + 1)2(k + 2)2

1 96

(42 + 24ζ(2) + 636ζ(3) − 867ζ(4) + 252ζ(5)

=

k=1

−72ζ(2)ζ(3) − 97ζ(6) + 48ζ(3)2 (643)

1 32

(30 + 18ζ(2) − 242ζ(3) + 213ζ(4) − 76ζ(5)

=

k3(k + 1)3(k + 2)2

k=1

+40ζ(2)ζ(3)) (644)

∞

H(k)2 k2(k + 1)4(k + 2)2

1 24

(−48 − 30ζ(2) − 78ζ(3) + 174ζ(4) + 37ζ(6)

=

k=1

−24ζ(3)2 (645) ∞

H(k)2 k(k + 1)5(k + 2)2

1 24

(−102 − 66ζ(2) + 42ζ(3) + 165ζ(4) + 72ζ(5) − 48ζ(2)ζ(3)

=

k=1

+37ζ(6) − 24ζ(3)2 + 24ζ(7) − 24ζ(2)ζ(5) + 12ζ(3)ζ(4) (646) ∞

H(k)2 (k + 1)6(k + 2)2

1 8

(−72 − 48ζ(2) + 16ζ(3) + 132ζ(4) + 48ζ(5) − 32ζ(2)ζ(3)

=

k=1

+37ζ(6) − 24ζ(3)2 + 16ζ(7) − 16ζ(2)ζ(5) + 8ζ(3)ζ(4) − 28ζ(8)

+16ζ(3)ζ(5) + 8M(2,6)) (647)

∞

H(k)2 k5(k + 2)3

1 256

(138 + 22ζ(2) + 26ζ(3) − 229ζ(4) + 180ζ(5) − 56ζ(2)ζ(3)

=

k=1

−194ζ(6) + 96ζ(3)2 + 192ζ(7) − 32ζ(2)ζ(5) − 80ζ(3)ζ(4) (648) ∞

H(k)2 k4(k + 1)(k + 2)3

1 192

(246 + 54ζ(2) − 486ζ(3) + 303ζ(4) − 192ζ(5) + 48ζ(2)ζ(3)

=

k=1

+97ζ(6) − 48ζ(3)2 (649) ∞

H(k)2 k3(k + 1)2(k + 2)3

1 16

(48 + 13ζ(2) + 25ζ(3) − 94ζ(4) + 10ζ(5)

=

k=1

−4ζ(2)ζ(3)) (650)

∞

H(k)2 k2(k + 1)3(k + 2)3

1 32

(222 + 70ζ(2) − 142ζ(3) − 163ζ(4) − 36ζ(5)

=

k=1

+24ζ(2)ζ(3)) (651)

∞

H(k)2 k(k + 1)4(k + 2)3

1 48

(762 + 270ζ(2) − 270ζ(3) − 837ζ(4) − 108ζ(5) + 72ζ(2)ζ(3)

=

k=1

−74ζ(6) + 48ζ(3)2 (652) ∞

H(k)2 (k + 1)5(k + 2)3

1 8

(288 + 112ζ(2) − 104ζ(3) − 334ζ(4) − 60ζ(5) + 40ζ(2)ζ(3)

=

k=1

−37ζ(6) + 24ζ(3)2 − 8ζ(7) + 8ζ(2)ζ(5) − 4ζ(3)ζ(4) (653) ∞

H(k)2 k4(k + 2)4

1 192

(−384 + 18ζ(2) + 90ζ(3) + 240ζ(4) − 72ζ(5) + 24ζ(2)ζ(3)

=

k=1

+67ζ(6) − 36ζ(3)2 (654)

1 192

(−1014 − 18ζ(2) + 666ζ(3) + 177ζ(4) + 48ζ(5) + 37ζ(6)

=

k3(k + 1)(k + 2)4

k=1

−24ζ(3)2 (655) ∞

H(k)2 k2(k + 1)2(k + 2)4

1 96

(−1302 − 96ζ(2) + 516ζ(3) + 741ζ(4) − 12ζ(5)

=

k=1

+24ζ(2)ζ(3) + 37ζ(6) − 24ζ(3)2 (656) ∞

H(k)2 k(k + 1)3(k + 2)4

1 96

(−3270 − 402ζ(2) + 1458ζ(3) + 1971ζ(4) + 84ζ(5)

=

k=1

−24ζ(2)ζ(3) + 74ζ(6) − 48ζ(3)2 (657) ∞

H(k)2 (k + 1)4(k + 2)4

1 12

(1008 + 168ζ(2) − 432ζ(3) − 702ζ(4) − 48ζ(5) + 24ζ(2)ζ(3)

=

k=1

−37ζ(6) + 24ζ(3)2 (658) ∞

H(k)2 k3(k + 2)5

1 256

(1398 − 210ζ(2) − 486ζ(3) − 371ζ(4) − 252ζ(5) + 104ζ(2)ζ(3)

=

k=1

−122ζ(6) + 80ζ(3)2 + 32ζ(7) − 32ζ(2)ζ(5) + 16ζ(3)ζ(4) (659) ∞

H(k)2 k2(k + 1)(k + 2)5

1 384

(6222 − 594ζ(2) − 2790ζ(3) − 1467ζ(4) − 852ζ(5)

=

k=1

+312ζ(2)ζ(3) − 440ζ(6) + 288ζ(3)2 + 96ζ(7) − 96ζ(2)ζ(5)

+48ζ(3)ζ(4)) (660)

∞

H(k)2 k(k + 1)2(k + 2)5

1 192

(8826 − 402ζ(2) − 3822ζ(3) − 2949ζ(4) − 828ζ(5)

=

k=1

+264ζ(2)ζ(3) − 514ζ(6) + 336ζ(3)2 + 96ζ(7) − 96ζ(2)ζ(5)

+48ζ(3)ζ(4)) (661)

∞

H(k)2 (k + 1)3(k + 2)5

1 8

(1008 − 440ζ(3) − 410ζ(4) − 76ζ(5) + 24ζ(2)ζ(3) − 49ζ(6)

=

k=1

+32ζ(3)2 + 8ζ(7) − 8ζ(2)ζ(5) + 4ζ(3)ζ(4) (662) ∞

H(k)2 k2(k + 2)6

1 128

(−1524 + 282ζ(2) + 498ζ(3) + 272ζ(4) + 424ζ(5) − 160ζ(2)ζ(3)

=

k=1

+165ζ(6) − 88ζ(3)2 + 160ζ(7) − 32ζ(2)ζ(5) − 80ζ(3)ζ(4) − 112ζ(8)

+64ζ(3)ζ(5) + 32M(2,6)) (663)

∞

H(k)2 k(k + 1)(k + 2)6

1 384

(15366 − 2286ζ(2) − 5778ζ(3) − 3099ζ(4) − 3396ζ(5)

=

k=1

+1272ζ(2)ζ(3) − 1430ζ(6) + 816ζ(3)2 − 864ζ(7) + 96ζ(2)ζ(5)

+528ζ(3)ζ(4) + 672ζ(8) − 384ζ(3)ζ(5) − 192M(2,6)) (664)

∞

H(k)2 (k + 1)2(k + 2)6

1 8

(−1008 + 112ζ(2) + 400ζ(3) + 252ζ(4) + 176ζ(5) − 64ζ(2)ζ(3)

=

k=1

+81ζ(6) − 48ζ(3)2 + 32ζ(7) − 24ζ(3)ζ(4) − 28ζ(8) + 16ζ(3)ζ(5)

+8M(2,6)) (665)

∞

H(k)2 k(k + 2)7

1 768

(16890 − 3090ζ(2) − 4590ζ(3) − 2757ζ(4) − 4476ζ(5) + 1416ζ(2)ζ(3)

=

k=1

−2042ζ(6) + 720ζ(3)2 − 3744ζ(7) + 1056ζ(2)ζ(5) + 1200ζ(3)ζ(4) − 288ζ(8)

+384ζ(3)ζ(5) − 192M(2,6) − 64ζ(9) + 576ζ(3)ζ(6) + 192ζ(4)ζ(5) −384ζ(2)ζ(7) − 128ζ(3)3 (666)

∞

H(k)2 (k + 1)(k + 2)7

1 24

(2016 − 336ζ(2) − 648ζ(3) − 366ζ(4) − 492ζ(5) + 168ζ(2)ζ(3)

=

k=1

−217ζ(6) + 96ζ(3)2 − 288ζ(7) + 72ζ(2)ζ(5) + 108ζ(3)ζ(4) + 24ζ(8) − 24M(2,6) −4ζ(9) + 36ζ(3)ζ(6) + 12ζ(4)ζ(5) − 24ζ(2)ζ(7) − 8ζ(3)3 (667)

∞

H(k)2 (k + 2)8

- 1

- 2


(72 − 12ζ(2) − 16ζ(3) − 11ζ(4) − 16ζ(5) + 4ζ(2)ζ(3) − 9ζ(6)

=

k=1

+2ζ(3)2 − 16ζ(7) + 4ζ(2)ζ(5) + 4ζ(3)ζ(4) − 7ζ(8) + 4ζ(3)ζ(5) −16ζ(9) + 4ζ(3)ζ(6) + 4ζ(4)ζ(5) + 4ζ(2)ζ(7) + 9ζ(10) − 4ζ(3)ζ(7) −2ζ(5)2 − 2M(2,8) (668)

∞

H(k)3 k7

1 160 −1661ζ(10) + 1280ζ(3)ζ(7) + 80ζ(3)2ζ(4) − 560ζ(2)ζ(3)ζ(5)

=

k=1

+720ζ(5)2 + 520M(2,8) (669) ∞

H(k)3 k6(k + 1)

1 96

960ζ(4) − 960ζ(5) − 96ζ(2)ζ(3) + 558ζ(6) − 240ζ(3)2

=

k=1

−1386ζ(7) − 192ζ(2)ζ(5) + 1224ζ(3)ζ(4) − 595ζ(8) − 120ζ(2)ζ(3)2

+576ζ(3)ζ(5) + 264M(2,6) − 2084ζ(9) + 1164ζ(3)ζ(6) + 1224ζ(4)ζ(5) −288ζ(2)ζ(7) − 192ζ(3)3 (670)

∞

H(k)3 k5(k + 1)2

1 96

4800ζ(4) − 4560ζ(5) − 480ζ(2)ζ(3) + 1674ζ(6) − 720ζ(3)2

=

k=1

−2772ζ(7) − 384ζ(2)ζ(5) + 2448ζ(3)ζ(4) − 595ζ(8) − 120ζ(2)ζ(3)2

+576ζ(3)ζ(5) + 264M(2,6)) (671)

∞

H(k)3 k4(k + 1)3

1 16 −1600ζ(4) + 1440ζ(5) + 160ζ(2)ζ(3) − 312ζ(6) + 152ζ(3)2

=

k=1

+231ζ(7) + 32ζ(2)ζ(5) − 204ζ(3)ζ(4)) (672)

∞

H(k)3 k3(k + 1)4

1 16

1600ζ(4) − 1360ζ(5) − 160ζ(2)ζ(3) + 192ζ(6) − 136ζ(3)2

=

k=1

−119ζ(7) − 32ζ(2)ζ(5) + 132ζ(3)ζ(4)) (673)

∞

H(k)3 k2(k + 1)5

1 96 −4800ζ(4) + 3840ζ(5) + 480ζ(2)ζ(3) − 594ζ(6) + 576ζ(3)2

=

k=1

+1428ζ(7) + 384ζ(2)ζ(5) − 1584ζ(3)ζ(4) − 43ζ(8) − 120ζ(2)ζ(3)2

+288ζ(3)ζ(5) − 24M(2,6)) (674)

∞

H(k)3 k(k + 1)6

1 96

960ζ(4) − 720ζ(5) − 96ζ(2)ζ(3) + 198ζ(6) − 192ζ(3)2

=

k=1

−714ζ(7) − 192ζ(2)ζ(5) + 792ζ(3)ζ(4) + 43ζ(8) + 120ζ(2)ζ(3)2 −288ζ(3)ζ(5) + 24M(2,6) − 788ζ(9) + 444ζ(3)ζ(6) + 792ζ(4)ζ(5) −288ζ(2)ζ(7) − 96ζ(3)3 (675)

∞

H(k)3 (k + 1)7

1 160

501ζ(10) − 800ζ(3)ζ(7) − 80ζ(3)2ζ(4) + 560ζ(2)ζ(3)ζ(5)

=

k=1

−480ζ(5)2 − 40M(2,8) (676) ∞

H(k)3 k6(k + 2)

1 768

(12 + 24ζ(2) + 48ζ(3) + 120ζ(4) − 240ζ(5) − 24ζ(2)ζ(3)

=

k=1

+279ζ(6) − 120ζ(3)2 − 1386ζ(7) − 192ζ(2)ζ(5) + 1224ζ(3)ζ(4) − 1190ζ(8) −240ζ(2)ζ(3)2 + 1152ζ(3)ζ(5) + 528M(2,6) − 8336ζ(9) + 4656ζ(3)ζ(6)

+4896ζ(4)ζ(5) − 1152ζ(2)ζ(7) − 768ζ(3)3 (677) ∞

H(k)3 k5(k + 1)(k + 2)

1 384

(12 + 24ζ(2) + 48ζ(3) − 3720ζ(4) + 3600ζ(5) + 360ζ(2)ζ(3)

=

k=1

−1953ζ(6) + 840ζ(3)2 + 4158ζ(7) + 576ζ(2)ζ(5) − 3672ζ(3)ζ(4) + 1190ζ(8)

+240ζ(2)ζ(3)2 − 1152ζ(3)ζ(5) − 528M(2,6) (678) ∞

H(k)3 k4(k + 1)2(k + 2)

1 64

(4 + 8ζ(2) + 16ζ(3) + 1960ζ(4) − 1840ζ(5) − 200ζ(2)ζ(3)

=

k=1

+465ζ(6) − 200ζ(3)2 − 462ζ(7) − 64ζ(2)ζ(5) + 408ζ(3)ζ(4) (679) ∞

H(k)3 k3(k + 1)3(k + 2)

1 32

(4 + 8ζ(2) + 16ζ(3) − 1240ζ(4) + 1040ζ(5) + 120ζ(2)ζ(3)

=

k=1

−159ζ(6) + 104ζ(3)2 (680) ∞

H(k)3 k2(k + 1)4(k + 2)

1 16

(−4 − 8ζ(2) − 16ζ(3) − 360ζ(4) + 320ζ(5) + 40ζ(2)ζ(3)

=

k=1

−33ζ(6) + 32ζ(3)2 + 119ζ(7) + 32ζ(2)ζ(5) − 132ζ(3)ζ(4) (681)

48 + 96ζ(2) + 192ζ(3) − 480ζ(4) − 198ζ(6) + 192ζ(3)2

=

k(k + 1)5(k + 2)

96

k=1

−43ζ(8) − 120ζ(2)ζ(3)2 + 288ζ(3)ζ(5) − 24M(2,6) (682) ∞

H(k)3 (k + 1)6(k + 2)

1 96

(−96 − 192ζ(2) − 384ζ(3) + 720ζ(5) + 96ζ(2)ζ(3) + 198ζ(6)

=

k=1

−192ζ(3)2 + 714ζ(7) + 192ζ(2)ζ(5) − 792ζ(3)ζ(4) + 43ζ(8)

+120ζ(2)ζ(3)2 − 288ζ(3)ζ(5) + 24M(2,6) + 788ζ(9) − 444ζ(3)ζ(6) −792ζ(4)ζ(5) + 288ζ(2)ζ(7) + 96ζ(3)3 (683)

∞

H(k)3 k5(k + 2)2

1 768

(156 + 192ζ(2) + 264ζ(3) + 402ζ(4) − 1140ζ(5) − 120ζ(2)ζ(3)

=

k=1

+837ζ(6) − 360ζ(3)2 − 2772ζ(7) − 384ζ(2)ζ(5) + 2448ζ(3)ζ(4) − 1190ζ(8) −240ζ(2)ζ(3)2 + 1152ζ(3)ζ(5) + 528M(2,6) (684)

∞

H(k)3 k4(k + 1)(k + 2)2

1 64

(28 + 36ζ(2) + 52ζ(3) − 553ζ(4) + 410ζ(5) + 40ζ(2)ζ(3)

=

k=1

−186ζ(6) + 80ζ(3)2 + 231ζ(7) + 32ζ(2)ζ(5) − 204ζ(3)ζ(4) (685) ∞

H(k)3 k3(k + 1)2(k + 2)2

1 64

(60 + 80ζ(2) + 120ζ(3) + 854ζ(4) − 1020ζ(5)

=

k=1

−120ζ(2)ζ(3) + 93ζ(6) − 40ζ(3)2 (686) ∞

H(k)3 k2(k + 1)3(k + 2)2

1 16

(32 + 44ζ(2) + 68ζ(3) − 193ζ(4) + 10ζ(5) − 33ζ(6)

=

k=1

+32ζ(3)2 (687) ∞

H(k)3 k(k + 1)4(k + 2)2

1 16

(68 + 96ζ(2) + 152ζ(3) − 26ζ(4) − 300ζ(5) − 40ζ(2)ζ(3)

=

k=1

−33ζ(6) + 32ζ(3)2 − 119ζ(7) − 32ζ(2)ζ(5) + 132ζ(3)ζ(4) (688) ∞

H(k)3 (k + 1)5(k + 2)2

1 96

(864 + 1248ζ(2) + 2016ζ(3) − 792ζ(4) − 3600ζ(5)

=

k=1

−480ζ(2)ζ(3) − 594ζ(6) + 576ζ(3)2 − 1428ζ(7) − 384ζ(2)ζ(5)

+1584ζ(3)ζ(4) − 43ζ(8) − 120ζ(2)ζ(3)2 + 288ζ(3)ζ(5) − 24M(2,6) (689) ∞

H(k)3 k4(k + 2)3

1 128

(−164 − 112ζ(2) − 72ζ(3) + 4ζ(4) + 324ζ(5) + 64ζ(2)ζ(3)

=

k=1

−156ζ(6) + 76ζ(3)2 + 231ζ(7) + 32ζ(2)ζ(5) − 204ζ(3)ζ(4) (690) ∞

H(k)3 k3(k + 1)(k + 2)3

1 64

(−192 − 148ζ(2) − 124ζ(3) + 557ζ(4) − 86ζ(5) + 24ζ(2)ζ(3)

=

k=1

+30ζ(6) − 4ζ(3)2 (691)

(444 + 376ζ(2) + 368ζ(3) − 260ζ(4) − 848ζ(5)

=

k2(k + 1)2(k + 2)3

64

k=1

−168ζ(2)ζ(3) + 33ζ(6) − 32ζ(3)2 (692) ∞

H(k)3 k(k + 1)3(k + 2)3

1 32

(−508 − 464ζ(2) − 504ζ(3) + 646ζ(4) + 828ζ(5)

=

k=1

+168ζ(2)ζ(3) + 33ζ(6) − 32ζ(3)2 (693) ∞

H(k)3 (k + 1)4(k + 2)3

1 16

(576 + 560ζ(2) + 656ζ(3) − 672ζ(4) − 1128ζ(5)

=

k=1

−208ζ(2)ζ(3) − 66ζ(6) + 64ζ(3)2 − 119ζ(7) − 32ζ(2)ζ(5)

+132ζ(3)ζ(4)) (694)

∞

H(k)3 k3(k + 2)4

1 128

(676 + 216ζ(2) − 96ζ(3) − 386ζ(4) − 256ζ(5) − 112ζ(2)ζ(3)

=

k=1

+22ζ(6) − 20ζ(3)2 − 119ζ(7) − 32ζ(2)ζ(5) + 132ζ(3)ζ(4) (695) ∞

H(k)3 k2(k + 1)(k + 2)4

1 64

(868 + 364ζ(2) + 28ζ(3) − 943ζ(4) − 170ζ(5)

=

k=1

−136ζ(2)ζ(3) − 8ζ(6) − 16ζ(3)2 − 119ζ(7) − 32ζ(2)ζ(5)

+132ζ(3)ζ(4)) (696)

∞

H(k)3 k(k + 1)2(k + 2)4

1 64

(2180 + 1104ζ(2) + 424ζ(3) − 2146ζ(4) − 1188ζ(5)

=

k=1

−440ζ(2)ζ(3) + 17ζ(6) − 64ζ(3)2 − 238ζ(7) − 64ζ(2)ζ(5)

+264ζ(3)ζ(4)) (697)

∞

H(k)3 (k + 1)3(k + 2)4

1 16

(1344 + 784ζ(2) + 464ζ(3) − 1396ζ(4) − 1008ζ(5)

=

k=1

−304ζ(2)ζ(3) − 8ζ(6) − 16ζ(3)2 − 119ζ(7) − 32ζ(2)ζ(5)

+132ζ(3)ζ(4)) (698)

∞

H(k)3 k2(k + 2)5

1 768

(12444 + 1224ζ(2) − 4320ζ(3) − 6144ζ(4) − 2232ζ(5)

=

k=1

+24ζ(2)ζ(3) − 1911ζ(6) + 1152ζ(3)2 − 852ζ(7) − 960ζ(2)ζ(5)

+1872ζ(3)ζ(4) + 86ζ(8) + 240ζ(2)ζ(3)2 − 576ζ(3)ζ(5) + 48M(2,6) (699) ∞

H(k)3 k(k + 1)(k + 2)5

1 384

(−17652 − 3408ζ(2) + 4152ζ(3) + 11802ζ(4) + 3252ζ(5)

=

k=1

+792ζ(2)ζ(3) + 1959ζ(6) − 1056ζ(3)2 + 1566ζ(7) + 1152ζ(2)ζ(5) −2664ζ(3)ζ(4) − 86ζ(8) − 240ζ(2)ζ(3)2 + 576ζ(3)ζ(5) − 48M(2,6) (700)

1 96

(12096 + 3360ζ(2) − 1440ζ(3) − 9120ζ(4) − 3408ζ(5)

=

(k + 1)2(k + 2)5

k=1

−1056ζ(2)ζ(3) − 954ζ(6) + 432ζ(3)2 − 1140ζ(7) − 672ζ(2)ζ(5)

+1728ζ(3)ζ(4) + 43ζ(8) + 120ζ(2)ζ(3)2 − 288ζ(3)ζ(5) + 24M(2,6) (701) ∞

H(k)3 k(k + 2)6

1 768

(30732 − 720ζ(2) − 11592ζ(3) − 10758ζ(4) − 8076ζ(5)

=

k=1

+2712ζ(2)ζ(3) − 5553ζ(6) + 3360ζ(3)2 − 2442ζ(7) − 768ζ(2)ζ(5)

+2808ζ(3)ζ(4) + 4118ζ(8) + 240ζ(2)ζ(3)2 − 2880ζ(3)ζ(5) − 1104M(2,6) −3152ζ(9) + 1776ζ(3)ζ(6) + 3168ζ(4)ζ(5) − 1152ζ(2)ζ(7) − 384ζ(3)3 (702)

∞

H(k)3 (k + 1)(k + 2)6

1 96

(12096 + 672ζ(2) − 3936ζ(3) − 5640ζ(4) − 2832ζ(5)

=

k=1

+480ζ(2)ζ(3) − 1878ζ(6) + 1104ζ(3)2 − 1002ζ(7) − 480ζ(2)ζ(5)

+1368ζ(3)ζ(4) + 1051ζ(8) + 120ζ(2)ζ(3)2 − 864ζ(3)ζ(5) − 264M(2,6) −788ζ(9) + 444ζ(3)ζ(6) + 792ζ(4)ζ(5) − 288ζ(2)ζ(7) − 96ζ(3)3 (703)

∞

H(k)3 (k + 2)7

1 160

(13440 − 1120ζ(2) − 4640ζ(3) − 3520ζ(4) − 4080ζ(5) + 1440ζ(2)ζ(3)

=

k=1

−2300ζ(6) + 1200ζ(3)2 − 2560ζ(7) + 480ζ(2)ζ(5) + 1200ζ(3)ζ(4) + 1080ζ(8) −480ζ(3)ζ(5) − 480M(2,6) − 80ζ(9) + 720ζ(3)ζ(6) + 240ζ(4)ζ(5) −480ζ(2)ζ(7) − 160ζ(3)3 + 501ζ(10) − 800ζ(3)ζ(7) − 80ζ(3)2ζ(4) +560ζ(2)ζ(3)ζ(5) − 480ζ(5)2 − 40M(2,8) (704)

∞

H(k)4 k6

1 640 −68823ζ(10) + 60000ζ(3)ζ(7) + 1000ζ(3)2ζ(4) −21680ζ(2)ζ(3)ζ(5) + 23560ζ(5)2 + 12120M(2,8) + 1280ζ(2)M(2,6) (705)

=

k=1

∞

H(k)4 k5(k + 1)

1 144

4320ζ(5) + 864ζ(2)ζ(3) − 5874ζ(6) − 432ζ(3)2 + 3330ζ(7)

=

k=1

+720ζ(2)ζ(5) − 3096ζ(3)ζ(4) + 14833ζ(8) + 4032ζ(2)ζ(3)2 −16704ζ(3)ζ(5) − 3744M(2,6) + 5232ζ(9) − 3348ζ(3)ζ(6) − 3096ζ(4)ζ(5)

+1008ζ(2)ζ(7) + 480ζ(3)3 (706) ∞

H(k)4 k4(k + 1)2

1 144 −17280ζ(5) − 3456ζ(2)ζ(3) + 22776ζ(6) + 1728ζ(3)2 −6660ζ(7) − 1440ζ(2)ζ(5) + 6192ζ(3)ζ(4) − 14833ζ(8) − 4032ζ(2)ζ(3)2

=

k=1

+16704ζ(3)ζ(5) + 3744M(2,6)) (707)

1 4

720ζ(5) + 144ζ(2)ζ(3) − 919ζ(6) − 72ζ(3)2 + 147ζ(7)

=

k3(k + 1)3

k=1

+40ζ(2)ζ(5) − 160ζ(3)ζ(4)) (708)

∞

H(k)4 k2(k + 1)4

1 144 −17280ζ(5) − 3456ζ(2)ζ(3) + 21336ζ(6) + 1728ζ(3)2 −3924ζ(7) − 1440ζ(2)ζ(5) + 5328ζ(3)ζ(4) − 12415ζ(8) − 3312ζ(2)ζ(3)2

=

k=1

+13824ζ(3)ζ(5) + 3024M(2,6)) (709)

∞

H(k)4 k(k + 1)5

1 144

4320ζ(5) + 864ζ(2)ζ(3) − 5154ζ(6) − 432ζ(3)2 + 1962ζ(7)

=

k=1

+720ζ(2)ζ(5) − 2664ζ(3)ζ(4) + 12415ζ(8) + 3312ζ(2)ζ(3)2 −13824ζ(3)ζ(5) − 3024M(2,6) + 2088ζ(9) − 1188ζ(3)ζ(6) − 2664ζ(4)ζ(5)

+1008ζ(2)ζ(7) + 384ζ(3)3 (710) ∞

H(k)4 (k + 1)6

1 640 −48647ζ(10) + 42080ζ(3)ζ(7) − 280ζ(3)2ζ(4) −12720ζ(2)ζ(3)ζ(5) + 13320ζ(5)2 + 7640M(2,8) + 1280ζ(2)M(2,6) (711)

=

k=1

∞

H(k)4 k5(k + 2)

1 1152

=

(36 + 108ζ(2) + 396ζ(3) + 666ζ(4) + 1080ζ(5) + 216ζ(2)ζ(3)

k=1

−2937ζ(6) − 216ζ(3)2 + 3330ζ(7) + 720ζ(2)ζ(5) − 3096ζ(3)ζ(4) + 29666ζ(8)

+8064ζ(2)ζ(3)2 − 33408ζ(3)ζ(5) − 7488M(2,6) + 20928ζ(9) − 13392ζ(3)ζ(6) −12384ζ(4)ζ(5) + 4032ζ(2)ζ(7) + 1920ζ(3)3 (712)

∞

H(k)4 k4(k + 1)(k + 2)

1 576

(36 + 108ζ(2) + 396ζ(3) + 666ζ(4) − 16200ζ(5) − 3240ζ(2)ζ(3)

=

k=1

+20559ζ(6) + 1512ζ(3)2 − 9990ζ(7) − 2160ζ(2)ζ(5) + 9288ζ(3)ζ(4) − 29666ζ(8) −8064ζ(2)ζ(3)2 + 33408ζ(3)ζ(5) + 7488M(2,6) (713)

∞

H(k)4 k3(k + 1)2(k + 2)

1 32

=

(4 + 12ζ(2) + 44ζ(3) + 74ζ(4) + 2040ζ(5) + 408ζ(2)ζ(3)

k=1

−2777ζ(6) − 216ζ(3)2 + 370ζ(7) + 80ζ(2)ζ(5) − 344ζ(3)ζ(4) (714) ∞

H(k)4 k2(k + 1)3(k + 2)

1 16

(4 + 12ζ(2) + 44ζ(3) + 74ζ(4) − 840ζ(5) − 168ζ(2)ζ(3)

=

k=1

+899ζ(6) + 72ζ(3)2 − 218ζ(7) − 80ζ(2)ζ(5) + 296ζ(3)ζ(4) (715) ∞

H(k)4 k(k + 1)4(k + 2)

1 144

=

(72 + 216ζ(2) + 792ζ(3) + 1332ζ(4) + 2160ζ(5) + 432ζ(2)ζ(3)

k=1

−5154ζ(6) − 432ζ(3)2 + 12415ζ(8) + 3312ζ(2)ζ(3)2 − 13824ζ(3)ζ(5) −3024M(2,6)) (716)

1 144

144 + 432ζ(2) + 1584ζ(3) + 2664ζ(4) − 5154ζ(6) − 432ζ(3)2

=

(k + 1)5(k + 2)

k=1

−1962ζ(7) − 720ζ(2)ζ(5) + 2664ζ(3)ζ(4) + 12415ζ(8) + 3312ζ(2)ζ(3)2 −13824ζ(3)ζ(5) − 3024M(2,6) − 2088ζ(9) + 1188ζ(3)ζ(6) + 2664ζ(4)ζ(5) −1008ζ(2)ζ(7) − 384ζ(3)3 (717)

∞

H(k)4 k4(k + 2)2

1 576

(−252 − 504ζ(2) − 1440ζ(3) − 1404ζ(4) − 1080ζ(5)

=

k=1

−288ζ(2)ζ(3) + 5694ζ(6) + 432ζ(3)2 − 3330ζ(7) − 720ζ(2)ζ(5)

+3096ζ(3)ζ(4) − 14833ζ(8) − 4032ζ(2)ζ(3)2 + 16704ζ(3)ζ(5)

+3744M(2,6)) (718)

∞

H(k)4 k3(k + 1)(k + 2)2

1 64

(−60 − 124ζ(2) − 364ζ(3) − 386ζ(4) + 1560ζ(5)

=

k=1

+296ζ(2)ζ(3) − 1019ζ(6) − 72ζ(3)2 + 370ζ(7) + 80ζ(2)ζ(5) −344ζ(3)ζ(4)) (719)

∞

H(k)4 k2(k + 1)2(k + 2)2

1 16

(−32 − 68ζ(2) − 204ζ(3) − 230ζ(4) − 240ζ(5)

=

k=1

−56ζ(2)ζ(3) + 879ζ(6) + 72ζ(3)2 (720) ∞

H(k)4 k(k + 1)3(k + 2)2

1 16

(−68 − 148ζ(2) − 452ζ(3) − 534ζ(4) + 360ζ(5) + 56ζ(2)ζ(3)

=

k=1

+859ζ(6) + 72ζ(3)2 + 218ζ(7) + 80ζ(2)ζ(5) − 296ζ(3)ζ(4) (721) ∞

H(k)4 (k + 1)4(k + 2)2

1 144

(−1296 − 2880ζ(2) − 8928ζ(3) − 10944ζ(4) + 4320ζ(5)

=

k=1

+576ζ(2)ζ(3) + 20616ζ(6) + 1728ζ(3)2 + 3924ζ(7) + 1440ζ(2)ζ(5) −5328ζ(3)ζ(4) − 12415ζ(8) − 3312ζ(2)ζ(3)2 + 13824ζ(3)ζ(5)

+3024M(2,6)) (722)

∞

H(k)4 k3(k + 2)3

1 64

(192 + 244ζ(2) + 508ζ(3) + 122ζ(4) − 168ζ(5) − 56ζ(2)ζ(3)

=

k=1

−853ζ(6) − 136ζ(3)2 + 294ζ(7) + 80ζ(2)ζ(5) − 320ζ(3)ζ(4) (723) ∞

H(k)4 k2(k + 1)(k + 2)3

1 64

(444 + 612ζ(2) + 1380ζ(3) + 630ζ(4) − 1896ζ(5)

=

k=1

−408ζ(2)ζ(3) − 687ζ(6) − 200ζ(3)2 + 218ζ(7) + 80ζ(2)ζ(5) −296ζ(3)ζ(4)) (724)

1 32

(508 + 748ζ(2) + 1788ζ(3) + 1090ζ(4) − 1416ζ(5)

=

k(k + 1)2(k + 2)3

k=1

- −296ζ(2)ζ(3) − 2445ζ(6) − 344ζ(3)2 + 218ζ(7) + 80ζ(2)ζ(5)
- −296ζ(3)ζ(4)) (725)


∞

H(k)4 (k + 1)3(k + 2)3

- 1

- 2


(72 + 112ζ(2) + 280ζ(3) + 203ζ(4) − 222ζ(5) − 44ζ(2)ζ(3)

=

k=1

−413ζ(6) − 52ζ(3)2 (726) ∞

H(k)4 k2(k + 2)4

1 576

(7812 + 5976ζ(2) + 7920ζ(3) − 5724ζ(4) − 6984ζ(5)

=

k=1

−3168ζ(2)ζ(3) − 4290ζ(6) − 1872ζ(3)2 − 2322ζ(7) − 432ζ(2)ζ(5)

+2088ζ(3)ζ(4) + 12415ζ(8) + 3312ζ(2)ζ(3)2 − 13824ζ(3)ζ(5) −3024M(2,6)) (727)

∞

H(k)4 k(k + 1)(k + 2)4

1 576

(19620 + 17460ζ(2) + 28260ζ(3) − 5778ζ(4) − 31032ζ(5)

=

k=1

−10008ζ(2)ζ(3) − 14763ζ(6) − 5544ζ(3)2 − 2682ζ(7) − 144ζ(2)ζ(5)

+1512ζ(3)ζ(4) + 24830ζ(8) + 6624ζ(2)ζ(3)2 − 27648ζ(3)ζ(5) −6048M(2,6)) (728)

∞

H(k)4 (k + 1)2(k + 2)4

1 144

(12096 + 12096ζ(2) + 22176ζ(3) + 2016ζ(4) − 21888ζ(5)

=

k=1

−6336ζ(2)ζ(3) − 18384ζ(6) − 4320ζ(3)2 − 360ζ(7) + 288ζ(2)ζ(5) −576ζ(3)ζ(4) + 12415ζ(8) + 3312ζ(2)ζ(3)2 − 13824ζ(3)ζ(5) − 3024M(2,6)

(729)

∞

H(k)4 k(k + 2)5

1 1152

(52956 + 22860ζ(2) + 12060ζ(3) − 44622ζ(4) − 25992ζ(5)

=

k=1

−10728ζ(2)ζ(3) − 9309ζ(6) + 1512ζ(3)2 − 20286ζ(7) − 9648ζ(2)ζ(5)

+27576ζ(3)ζ(4) + 25862ζ(8) + 9504ζ(2)ζ(3)2 − 34560ζ(3)ζ(5) − 5472M(2,6)

+8352ζ(9) − 4752ζ(3)ζ(6) − 10656ζ(4)ζ(5) + 4032ζ(2)ζ(7)

+1536ζ(3)3 (730) ∞

H(k)4 (k + 1)(k + 2)5

1 144

(18144 + 10080ζ(2) + 10080ζ(3) − 12600ζ(4) − 14256ζ(5)

=

k=1

−5184ζ(2)ζ(3) − 6018ζ(6) − 1008ζ(3)2 − 5742ζ(7) − 2448ζ(2)ζ(5)

+7272ζ(3)ζ(4) + 12673ζ(8) + 4032ζ(2)ζ(3)2 − 15552ζ(3)ζ(5) − 2880M(2,6)

+2088ζ(9) − 1188ζ(3)ζ(6) − 2664ζ(4)ζ(5) + 1008ζ(2)ζ(7) + 384ζ(3)3 (731)

1 1920

(241920 + 53760ζ(2) − 26880ζ(3) − 161280ζ(4) − 88320ζ(5)

=

(k + 2)6

k=1

−7680ζ(2)ζ(3) − 56640ζ(6) + 30720ζ(3)2 − 57120ζ(7) − 30720ζ(2)ζ(5)

+82560ζ(3)ζ(4) + 43760ζ(8) + 9600ζ(2)ζ(3)2 − 46080ζ(3)ζ(5) − 9600M(2,6) −63040ζ(9) + 35520ζ(3)ζ(6) + 63360ζ(4)ζ(5) − 23040ζ(2)ζ(7) − 7680ζ(3)3

+145941ζ(10) − 126240ζ(3)ζ(7) + 840ζ(3)2ζ(4) + 38160ζ(2)ζ(3)ζ(5) −39960ζ(5)2 − 22920M(2,8) − 3840ζ(2)M(2,6) (732)

∞

H(k)5 k5

1 256

64433ζ(10) − 57760ζ(3)ζ(7) + 360ζ(3)2ζ(4)

=

k=1

+20560ζ(2)ζ(3)ζ(5) − 22648ζ(5)2 − 10920M(2,8) − 1280ζ(2)M(2,6) (733) ∞

H(k)5 k4(k + 1)

1 288

51408ζ(6) + 6480ζ(3)2 − 36918ζ(7) − 8208ζ(2)ζ(5)

=

k=1

−9504ζ(3)ζ(4) − 67811ζ(8) − 19080ζ(2)ζ(3)2 + 78768ζ(3)ζ(5) + 16920M(2,6) −37768ζ(9) + 58740ζ(3)ζ(6) − 19008ζ(4)ζ(5) − 9540ζ(2)ζ(7)

+1440ζ(3)3 (734) ∞

H(k)5 k3(k + 1)2

1 288

154224ζ(6) + 19440ζ(3)2 − 107226ζ(7) − 24624ζ(2)ζ(5)

=

k=1

−28512ζ(3)ζ(4) − 67811ζ(8) − 19080ζ(2)ζ(3)2 + 78768ζ(3)ζ(5)

+16920M(2,6)) (735)

∞

H(k)5 k2(k + 1)3

1 288

154224ζ(6) + 19440ζ(3)2 − 103698ζ(7) − 24624ζ(2)ζ(5)

=

k=1

−28512ζ(3)ζ(4) − 65621ζ(8) − 17640ζ(2)ζ(3)2 + 72432ζ(3)ζ(5)

+15480M(2,6)) (736)

∞

H(k)5 k(k + 1)4

1 288

51408ζ(6) + 6480ζ(3)2 − 33390ζ(7) − 8208ζ(2)ζ(5)

=

k=1

−9504ζ(3)ζ(4) − 65621ζ(8) − 17640ζ(2)ζ(3)2 + 72432ζ(3)ζ(5) + 15480M(2,6) −28480ζ(9) + 51540ζ(3)ζ(6) − 19008ζ(4)ζ(5) − 9540ζ(2)ζ(7)

+1440ζ(3)3 (737) ∞

H(k)5 (k + 1)5

1 256

49901ζ(10) − 43040ζ(3)ζ(7) − 1080ζ(3)2ζ(4)

=

k=1

+13840ζ(2)ζ(3)ζ(5) − 13592ζ(5)2 − 7560M(2,8) − 1280ζ(2)M(2,6) (738) ∞

H(k)5 k4(k + 2)

1 1152

(−72 − 288ζ(2) − 1512ζ(3) − 4518ζ(4) − 5112ζ(5) − 1080ζ(2)ζ(3)

=

k=1

−12852ζ(6) − 1620ζ(3)2 + 18459ζ(7) + 4104ζ(2)ζ(5) + 4752ζ(3)ζ(4)

+67811ζ(8) + 19080ζ(2)ζ(3)2 − 78768ζ(3)ζ(5) − 16920M(2,6) + 75536ζ(9) −117480ζ(3)ζ(6) + 38016ζ(4)ζ(5) + 19080ζ(2)ζ(7) − 2880ζ(3)3 (739)

(−72 − 288ζ(2) − 1512ζ(3) − 4518ζ(4) − 5112ζ(5)

=

k3(k + 1)(k + 2)

576

k=1

−1080ζ(2)ζ(3) + 89964ζ(6) + 11340ζ(3)2 − 55377ζ(7) − 12312ζ(2)ζ(5) −14256ζ(3)ζ(4) − 67811ζ(8) − 19080ζ(2)ζ(3)2 + 78768ζ(3)ζ(5)

+16920M(2,6)) (740)

∞

H(k)5 k2(k + 1)2(k + 2)

1 32

(−8 − 32ζ(2) − 168ζ(3) − 502ζ(4) − 568ζ(5) − 120ζ(2)ζ(3)

=

k=1

−7140ζ(6) − 900ζ(3)2 + 5761ζ(7) + 1368ζ(2)ζ(5) + 1584ζ(3)ζ(4) (741) ∞

H(k)5 k(k + 1)3(k + 2)

1 288

(−144 − 576ζ(2) − 3024ζ(3) − 9036ζ(4) − 10224ζ(5)

=

k=1

−2160ζ(2)ζ(3) + 25704ζ(6) + 3240ζ(3)2 − 65621ζ(8) − 17640ζ(2)ζ(3)2

+72432ζ(3)ζ(5) + 15480M(2,6)) (742)

∞

H(k)5 (k + 1)4(k + 2)

1 288

=

(288 + 1152ζ(2) + 6048ζ(3) + 18072ζ(4) + 20448ζ(5)

k=1

+4320ζ(2)ζ(3) − 33390ζ(7) − 8208ζ(2)ζ(5) − 9504ζ(3)ζ(4) + 65621ζ(8)

+17640ζ(2)ζ(3)2 − 72432ζ(3)ζ(5) − 15480M(2,6) − 28480ζ(9) + 51540ζ(3)ζ(6) −19008ζ(4)ζ(5) − 9540ζ(2)ζ(7) + 1440ζ(3)3 (743)

∞

H(k)5 k3(k + 2)2

1 1152

=

(1080 + 3024ζ(2) + 12888ζ(3) + 27666ζ(4) + 14760ζ(5)

k=1

+3960ζ(2)ζ(3) + 12786ζ(6) + 2700ζ(3)2 − 53613ζ(7) − 12312ζ(2)ζ(5) −14256ζ(3)ζ(4) − 67811ζ(8) − 19080ζ(2)ζ(3)2 + 78768ζ(3)ζ(5)

+16920M(2,6)) (744)

∞

H(k)5 k2(k + 1)(k + 2)2

1 96

=

(192 + 552ζ(2) + 2400ζ(3) + 5364ζ(4) + 3312ζ(5)

k=1

+840ζ(2)ζ(3) − 12863ζ(6) − 1440ζ(3)2 + 294ζ(7) (745) ∞

H(k)5 k(k + 1)2(k + 2)2

1 96

=

(408 + 1200ζ(2) + 5304ζ(3) + 12234ζ(4) + 8328ζ(5)

k=1

+2040ζ(2)ζ(3) − 4306ζ(6) − 180ζ(3)2 − 16695ζ(7) − 4104ζ(2)ζ(5) −4752ζ(3)ζ(4)) (746)

∞

H(k)5 (k + 1)3(k + 2)2

1 288

(2592 + 7776ζ(2) + 34848ζ(3) + 82440ζ(4) + 60192ζ(5)

=

k=1

+14400ζ(2)ζ(3) − 51540ζ(6) − 4320ζ(3)2 − 100170ζ(7) − 24624ζ(2)ζ(5) −28512ζ(3)ζ(4) + 65621ζ(8) + 17640ζ(2)ζ(3)2 − 72432ζ(3)ζ(5) −15480M(2,6)) (747)

(7992 + 15264ζ(2) + 51480ζ(3) + 71874ζ(4) − 4248ζ(5)

=

k2(k + 2)3

1152

k=1

+360ζ(2)ζ(3) − 58584ζ(6) − 9540ζ(3)2 − 32229ζ(7) − 5112ζ(2)ζ(5) −40896ζ(3)ζ(4) − 65621ζ(8) − 17640ζ(2)ζ(3)2 + 72432ζ(3)ζ(5)

+15480M(2,6)) (748)

∞

H(k)5 k(k + 1)(k + 2)3

1 576

(−9144 − 18576ζ(2) − 65880ζ(3) − 104058ζ(4) − 15624ζ(5)

=

k=1

−5400ζ(2)ζ(3) + 135762ζ(6) + 18180ζ(3)2 + 30465ζ(7) + 5112ζ(2)ζ(5)

+40896ζ(3)ζ(4) + 65621ζ(8) + 17640ζ(2)ζ(3)2 − 72432ζ(3)ζ(5) −15480M(2,6)) (749)

∞

H(k)5 (k + 1)2(k + 2)3

1 288

=

(10368 + 22176ζ(2) + 81792ζ(3) + 140760ζ(4) + 40608ζ(5)

k=1

+11520ζ(2)ζ(3) − 148680ζ(6) − 18720ζ(3)2 − 80550ζ(7) − 17424ζ(2)ζ(5) −55152ζ(3)ζ(4) − 65621ζ(8) − 17640ζ(2)ζ(3)2 + 72432ζ(3)ζ(5)

+15480M(2,6)) (750)

∞

H(k)5 k(k + 2)4

1 1152

(39240 + 49968ζ(2) + 129384ζ(3) + 94806ζ(4) − 82440ζ(5)

=

k=1

−25560ζ(2)ζ(3) − 146718ζ(6) − 36540ζ(3)2 − 675ζ(7) + 5976ζ(2)ζ(5) −37152ζ(3)ζ(4) + 182679ζ(8) + 48600ζ(2)ζ(3)2 − 204048ζ(3)ζ(5) − 45000M(2,6) −56960ζ(9) + 103080ζ(3)ζ(6) − 38016ζ(4)ζ(5) − 19080ζ(2)ζ(7)

+2880ζ(3)3 (751) ∞

H(k)5 (k + 1)(k + 2)4

1 288

(24192 + 34272ζ(2) + 97632ζ(3) + 99432ζ(4) − 33408ζ(5)

=

k=1

−10080ζ(2)ζ(3) − 141240ζ(6) − 27360ζ(3)2 − 15570ζ(7) + 432ζ(2)ζ(5) −39024ζ(3)ζ(4) + 58529ζ(8) + 15480ζ(2)ζ(3)2 − 65808ζ(3)ζ(5) − 14760M(2,6) −28480ζ(9) + 51540ζ(3)ζ(6) − 19008ζ(4)ζ(5) − 9540ζ(2)ζ(7)

+1440ζ(3)3 (752) ∞

H(k)5 (k + 2)5

1 2304

(290304 + 241920ζ(2) + 460800ζ(3) + 48960ζ(4) − 414720ζ(5)

=

k=1

−149760ζ(2)ζ(3) − 384960ζ(6) − 97920ζ(3)2 − 162720ζ(7) − 57600ζ(2)ζ(5)

+178560ζ(3)ζ(4) + 1003520ζ(8) + 293760ζ(2)ζ(3)2 − 1175040ζ(3)ζ(5) −236160M(2,6) + 167040ζ(9) − 95040ζ(3)ζ(6) − 213120ζ(4)ζ(5) + 80640ζ(2)ζ(7)

+30720ζ(3)3 − 449109ζ(10) + 387360ζ(3)ζ(7) + 9720ζ(3)2ζ(4) −124560ζ(2)ζ(3)ζ(5) + 122328ζ(5)2 + 68040M(2,8) + 11520ζ(2)M(2,6)

(753)

∞

H(k)6 k4

1 128 −271367ζ(10) + 176560ζ(3)ζ(7) − 84648ζ(3)2ζ(4) −400ζ(2)ζ(3)ζ(5) + 121688ζ(5)2 + 34376M(2,8) + 15040ζ(2)M(2,6) (754)

=

k=1

∞

H(k)6 k3(k + 1)

1 24

(15456ζ(7) + 3480ζ(2)ζ(5) + 7128ζ(3)ζ(4) − 17529ζ(8)

=

k=1

+984ζ(2)ζ(3)2 − 11688ζ(3)ζ(5) − 1368M(2,6) + 7474ζ(9) − 13122ζ(3)ζ(6)

+6048ζ(4)ζ(5) + 1953ζ(2)ζ(7) − 544ζ(3)3 (755) ∞

H(k)6 k2(k + 1)2

1 6

(−7728ζ(7) − 1740ζ(2)ζ(5) − 3564ζ(3)ζ(4) + 8639ζ(8)

=

k=1

−477ζ(2)ζ(3)2 + 5754ζ(3)ζ(5) + 669M(2,6) (756) ∞

H(k)6 k(k + 1)3

1 24

(15456ζ(7) + 3480ζ(2)ζ(5) + 7128ζ(3)ζ(4) − 17027ζ(8)

=

k=1

+924ζ(2)ζ(3)2 − 11328ζ(3)ζ(5) − 1308M(2,6) + 6146ζ(9) − 12582ζ(3)ζ(6)

+5832ζ(4)ζ(5) + 1953ζ(2)ζ(7) − 536ζ(3)3 (757) ∞

H(k)6 (k + 1)4

1 128 −259945ζ(10) + 163568ζ(3)ζ(7) − 81848ζ(3)2ζ(4)

=

k=1

+5200ζ(2)ζ(3)ζ(5) + 113288ζ(5)2 + 31576M(2,8) + 15040ζ(2)M(2,6) (758) ∞

H(k)6 k3(k + 2)

1 96

=

(12 + 60ζ(2) + 408ζ(3) + 1713ζ(4) + 3426ζ(5) + 732ζ(2)ζ(3)

k=1

+6291ζ(6) + 804ζ(3)2 + 7728ζ(7) + 1740ζ(2)ζ(5) + 3564ζ(3)ζ(4) − 17529ζ(8)

+984ζ(2)ζ(3)2 − 11688ζ(3)ζ(5) − 1368M(2,6) + 14948ζ(9) − 26244ζ(3)ζ(6)

+12096ζ(4)ζ(5) + 3906ζ(2)ζ(7) − 1088ζ(3)3 (759) ∞

H(k)6 k2(k + 1)(k + 2)

1 16

=

(4 + 20ζ(2) + 136ζ(3) + 571ζ(4) + 1142ζ(5) + 244ζ(2)ζ(3)

k=1

+2097ζ(6) + 268ζ(3)2 − 7728ζ(7) − 1740ζ(2)ζ(5) − 3564ζ(3)ζ(4) + 5843ζ(8) −328ζ(2)ζ(3)2 + 3896ζ(3)ζ(5) + 456M(2,6) (760)

∞

H(k)6 k(k + 1)2(k + 2)

1 24

=

(12 + 60ζ(2) + 408ζ(3) + 1713ζ(4) + 3426ζ(5) + 732ζ(2)ζ(3)

k=1

+6291ζ(6) + 804ζ(3)2 + 7728ζ(7) + 1740ζ(2)ζ(5) + 3564ζ(3)ζ(4) − 17027ζ(8)

+924ζ(2)ζ(3)2 − 11328ζ(3)ζ(5) − 1308M(2,6) (761) ∞

H(k)6 (k + 1)3(k + 2)

1 24

=

(24 + 120ζ(2) + 816ζ(3) + 3426ζ(4) + 6852ζ(5) + 1464ζ(2)ζ(3)

k=1

+12582ζ(6) + 1608ζ(3)2 − 17027ζ(8) + 924ζ(2)ζ(3)2 − 11328ζ(3)ζ(5) −1308M(2,6) − 6146ζ(9) + 12582ζ(3)ζ(6) − 5832ζ(4)ζ(5) − 1953ζ(2)ζ(7)

+536ζ(3)3 (762)

H(k)6 k2(k + 2)2

k=1

∞

H(k)6 k(k + 1)(k + 2)2

k=1

∞

H(k)6 (k + 1)2(k + 2)2

k=1

∞

H(k)6 k(k + 2)3

k=1

∞

H(k)6 (k + 1)(k + 2)3

k=1

∞

H(k)6 (k + 2)4

k=1

1 96

=

(192 + 696ζ(2) + 3936ζ(3) + 12714ζ(4) + 16956ζ(5)

+3912ζ(2)ζ(3) + 12279ζ(6) + 2136ζ(3)2 − 1239ζ(7) − 624ζ(2)ζ(5)

+2376ζ(3)ζ(4) − 34556ζ(8) + 1908ζ(2)ζ(3)2 − 23016ζ(3)ζ(5) −2676M(2,6)) (763)

1 48

=

(204 + 756ζ(2) + 4344ζ(3) + 14427ζ(4) + 20382ζ(5)

+4644ζ(2)ζ(3) + 18570ζ(6) + 2940ζ(3)2 − 24423ζ(7) − 5844ζ(2)ζ(5) −8316ζ(3)ζ(4) − 17027ζ(8) + 924ζ(2)ζ(3)2 − 11328ζ(3)ζ(5) − 1308M(2,6)

(764)

1 24

=

(216 + 816ζ(2) + 4752ζ(3) + 16140ζ(4) + 23808ζ(5)

+5376ζ(2)ζ(3) + 24861ζ(6) + 3744ζ(3)2 − 16695ζ(7) − 4104ζ(2)ζ(5) −4752ζ(3)ζ(4) − 34054ζ(8) + 1848ζ(2)ζ(3)2 − 22656ζ(3)ζ(5) −2616M(2,6)) (765)

1 96

(1524 + 3948ζ(2) + 18360ζ(3) + 44121ζ(4) + 34122ζ(5)

=

+8364ζ(2)ζ(3) − 18408ζ(6) − 1692ζ(3)2 − 32547ζ(7) − 6972ζ(2)ζ(5) −24012ζ(3)ζ(4) − 82648ζ(8) − 16716ζ(2)ζ(3)2 + 61104ζ(3)ζ(5) + 14172M(2,6)

+12292ζ(9) − 25164ζ(3)ζ(6) + 11664ζ(4)ζ(5) + 3906ζ(2)ζ(7) −1072ζ(3)3 (766)

1 48

=

(1728 + 4704ζ(2) + 22704ζ(3) + 58548ζ(4) + 54504ζ(5)

+13008ζ(2)ζ(3) + 162ζ(6) + 1248ζ(3)2 − 56970ζ(7) − 12816ζ(2)ζ(5) −32328ζ(3)ζ(4) − 99675ζ(8) − 15792ζ(2)ζ(3)2 + 49776ζ(3)ζ(5) + 12864M(2,6)

+12292ζ(9) − 25164ζ(3)ζ(6) + 11664ζ(4)ζ(5) + 3906ζ(2)ζ(7) −1072ζ(3)3 (767)

1 384

(−32256 − 59136ζ(2) − 224256ζ(3) − 386496ζ(4) − 122880ζ(5)

=

−26880ζ(2)ζ(3) + 378528ζ(6) + 66432ζ(3)2 + 167280ζ(7) + 23424ζ(2)ζ(5)

+225792ζ(3)ζ(4) + 28368ζ(8) + 8640ζ(2)ζ(3)2 − 26496ζ(3)ζ(5) − 2880M(2,6)

+227840ζ(9) − 412320ζ(3)ζ(6) + 152064ζ(4)ζ(5) + 76320ζ(2)ζ(7) − 11520ζ(3)3 −779835ζ(10) + 490704ζ(3)ζ(7) − 245544ζ(3)2ζ(4) + 15600ζ(2)ζ(3)ζ(5)

+339864ζ(5)2 + 94728M(2,8) + 45120ζ(2)M(2,6) (768)

∞

H(k)7 k3

1 2560

16614991ζ(10) − 10315520ζ(3)ζ(7) + 5879160ζ(3)2ζ(4)

=

k=1

−705040ζ(2)ζ(3)ζ(5) − 7710760ζ(5)2 − 2021880M(2,8) − 1008000ζ(2)M(2,6)

(769)

∞

H(k)7 k2(k + 1)

1 72

479096ζ(8) + 12096ζ(2)ζ(3)2 + 109620ζ(3)ζ(5) − 276341ζ(9)

=

k=1

−88665ζ(3)ζ(6) − 143163ζ(4)ζ(5) − 59166ζ(2)ζ(7) − 4032ζ(3)3 (770) ∞

H(k)7 k(k + 1)2

1 72

479096ζ(8) + 12096ζ(2)ζ(3)2 + 109620ζ(3)ζ(5) − 269402ζ(9)

=

k=1

−88665ζ(3)ζ(6) − 141273ζ(4)ζ(5) − 59166ζ(2)ζ(7) − 4032ζ(3)3 (771) ∞

H(k)7 (k + 1)3

1 2560

16597239ζ(10) − 9974400ζ(3)ζ(7) + 5800760ζ(3)2ζ(4)

=

k=1

−834960ζ(2)ζ(3)ζ(5) − 7473640ζ(5)2 − 1956920M(2,8) − 1008000ζ(2)M(2,6)

(772)

∞

H(k)7 k2(k + 2)

1 576

(−144 − 864ζ(2) − 7200ζ(3) − 38664ζ(4) − 108504ζ(5)

=

k=1

−23184ζ(2)ζ(3) − 352887ζ(6) − 45864ζ(3)2 − 319554ζ(7) − 73080ζ(2)ζ(5) −148932ζ(3)ζ(4) − 958192ζ(8) − 24192ζ(2)ζ(3)2 − 219240ζ(3)ζ(5)

+1105364ζ(9) + 354660ζ(3)ζ(6) + 572652ζ(4)ζ(5) + 236664ζ(2)ζ(7)

+16128ζ(3)3 (773) ∞

H(k)7 k(k + 1)(k + 2)

1 288

(−144 − 864ζ(2) − 7200ζ(3) − 38664ζ(4) − 108504ζ(5)

=

k=1

−23184ζ(2)ζ(3) − 352887ζ(6) − 45864ζ(3)2 − 319554ζ(7) − 73080ζ(2)ζ(5) −148932ζ(3)ζ(4) + 958192ζ(8) + 24192ζ(2)ζ(3)2 + 219240ζ(3)ζ(5) (774)

∞

H(k)7 (k + 1)2(k + 2)

1 144

=

(144 + 864ζ(2) + 7200ζ(3) + 38664ζ(4) + 108504ζ(5)

k=1

+23184ζ(2)ζ(3) + 352887ζ(6) + 45864ζ(3)2 + 319554ζ(7) + 73080ζ(2)ζ(5)

+148932ζ(3)ζ(4) − 538804ζ(9) − 177330ζ(3)ζ(6) − 282546ζ(4)ζ(5) −118332ζ(2)ζ(7) − 8064ζ(3)3 (775)

∞

H(k)7 k(k + 2)2

1 576

=

(2448 + 10944ζ(2) + 77184ζ(3) + 331344ζ(4) + 683928ζ(5)

k=1

+152208ζ(2)ζ(3) + 1403655ζ(6) + 199080ζ(3)2 + 257472ζ(7) + 46872ζ(2)ζ(5)

+247212ζ(3)ζ(4) − 472076ζ(8) + 101808ζ(2)ζ(3)2 − 732312ζ(3)ζ(5) −109872M(2,6) − 1077608ζ(9) − 354660ζ(3)ζ(6) − 565092ζ(4)ζ(5) − 236664ζ(2)ζ(7) −16128ζ(3)3 (776)

∞

H(k)7 (k + 1)(k + 2)2

1 144

=

(1296 + 5904ζ(2) + 42192ζ(3) + 185004ζ(4) + 396216ζ(5)

k=1

+87696ζ(2)ζ(3) + 878271ζ(6) + 122472ζ(3)2 + 288513ζ(7) + 59976ζ(2)ζ(5)

+198072ζ(3)ζ(4) − 715134ζ(8) + 38808ζ(2)ζ(3)2 − 475776ζ(3)ζ(5) − 54936M(2,6) −538804ζ(9) − 177330ζ(3)ζ(6) − 282546ζ(4)ζ(5) − 118332ζ(2)ζ(7) −8064ζ(3)3 (777)

∞

H(k)7 (k + 2)3

1 7680

(−276480 − 913920ζ(2) − 5429760ζ(3) − 18389760ζ(4) − 26899200ζ(5)

=

k=1

−6182400ζ(2)ζ(3) − 28153920ζ(6) − 4381440ζ(3)2 + 16691520ζ(7)

+3951360ζ(2)ζ(5) + 7674240ζ(3)ζ(4) + 74888240ζ(8) + 7808640ζ(2)ζ(3)2 −15187200ζ(3)ζ(5) − 5738880M(2,6) − 13767040ζ(9) + 28183680ζ(3)ζ(6) −13063680ζ(4)ζ(5) − 4374720ζ(2)ζ(7) + 1200640ζ(3)3 + 49791717ζ(10) −29923200ζ(3)ζ(7) + 17402280ζ(3)2ζ(4) − 2504880ζ(2)ζ(3)ζ(5) −22420920ζ(5)2 − 5870760M(2,8) − 3024000ζ(2)M(2,6) (778)

∞

H(k)8 k2

1 480

18741581ζ(10) + 6689520ζ(3)ζ(7) − 524640ζ(3)2ζ(4)

=

k=1

+1452480ζ(2)ζ(3)ζ(5) + 4247040ζ(5)2 + 485280M(2,8) + 299520ζ(2)M(2,6)

(779)

∞

H(k)8 k(k + 1)

1 6

=

(166700ζ(9) + 88665ζ(3)ζ(6) + 80400ζ(4)ζ(5) + 35091ζ(2)ζ(7)

k=1

+4032ζ(3)3 (780) ∞

H(k)8 (k + 1)2

1 240

9295879ζ(10) + 3314520ζ(3)ζ(7) − 258540ζ(3)2ζ(4)

=

k=1

+733800ζ(2)ζ(3)ζ(5) + 2098980ζ(5)2 + 238860M(2,8) + 149760ζ(2)M(2,6)

(781)

∞

H(k)8 k(k + 2)

1 144

=

(72 + 504ζ(2) + 4968ζ(3) + 32400ζ(4) + 116280ζ(5) + 24768ζ(2)ζ(3)

k=1

+530346ζ(6) + 69264ζ(3)2 + 849654ζ(7) + 193104ζ(2)ζ(5) + 404280ζ(3)ζ(4)

+1906367ζ(8) + 48384ζ(2)ζ(3)2 + 436896ζ(3)ζ(5) + 2000400ζ(9)

+1063980ζ(3)ζ(6) + 964800ζ(4)ζ(5) + 421092ζ(2)ζ(7) + 48384ζ(3)3 (782) ∞

H(k)8 (k + 1)(k + 2)

1 72

=

(72 + 504ζ(2) + 4968ζ(3) + 32400ζ(4) + 116280ζ(5) + 24768ζ(2)ζ(3)

k=1

+530346ζ(6) + 69264ζ(3)2 + 849654ζ(7) + 193104ζ(2)ζ(5) + 404280ζ(3)ζ(4)

+1906367ζ(8) + 48384ζ(2)ζ(3)2 + 436896ζ(3)ζ(5) (783)

∞

H(k)8 (k + 2)2

1 720

=

(6480 + 34560ζ(2) + 292320ζ(3) + 1564560ζ(4) + 4348800ζ(5)

k=1

+950400ζ(2)ζ(3) + 14106480ζ(6) + 1926720ζ(3)2 + 12318480ζ(7) + 2712960ζ(2)ζ(5)

+6755040ζ(3)ζ(4) + 4760990ζ(8) + 1260000ζ(2)ζ(3)2 − 5146560ζ(3)ζ(5) −1098720M(2,6) − 21552160ζ(9) − 7093200ζ(3)ζ(6) − 11301840ζ(4)ζ(5) −4733280ζ(2)ζ(7) − 322560ζ(3)3 − 27887637ζ(10) − 9943560ζ(3)ζ(7)

+775620ζ(3)2ζ(4) − 2201400ζ(2)ζ(3)ζ(5) − 6296940ζ(5)2 − 716580M(2,8) −449280ζ(2)M(2,6)) (784)

##### Formulas for order r = m + n + p + q = 11:

∞

H(k) k10

= 6ζ(11) − ζ(2)ζ(9) − ζ(3)ζ(8) − ζ(4)ζ(7) − ζ(5)ζ(6) (785)

k=1

∞

H(k) k9(k + 1)

1 4

4ζ(2) − 8ζ(3) + 5ζ(4) − 12ζ(5) + 4ζ(2)ζ(3) + 7ζ(6) − 2ζ(3)2

=

k=1

−16ζ(7) + 4ζ(2)ζ(5) + 4ζ(3)ζ(4) + 9ζ(8) − 4ζ(3)ζ(5) − 20ζ(9)

+4ζ(3)ζ(6) + 4ζ(4)ζ(5) + 4ζ(2)ζ(7) + 11ζ(10) − 4ζ(3)ζ(7) −2ζ(5)2 (786)

∞

1 2

H(k) k8(k + 1)2

(16ζ(2) − 30ζ(3) + 15ζ(4) − 30ζ(5) + 10ζ(2)ζ(3) + 14ζ(6)

=

k=1

−4ζ(3)2 − 24ζ(7) + 6ζ(2)ζ(5) + 6ζ(3)ζ(4) + 9ζ(8) − 4ζ(3)ζ(5) −10ζ(9) + 2ζ(3)ζ(6) + 2ζ(4)ζ(5) + 2ζ(2)ζ(7)) (787)

∞

1 4

H(k) k7(k + 1)3

(112ζ(2) − 196ζ(3) + 74ζ(4) − 120ζ(5) + 40ζ(2)ζ(3) + 42ζ(6)

=

k=1

−12ζ(3)2 − 48ζ(7) + 12ζ(2)ζ(5) + 12ζ(3)ζ(4) + 9ζ(8) − 4ζ(3)ζ(5) (788) ∞

H(k) k6(k + 1)4

1 2

(112ζ(2) − 182ζ(3) + 47ζ(4) − 64ζ(5) + 22ζ(2)ζ(3) + 14ζ(6)

=

k=1

−4ζ(3)2 − 8ζ(7) + 2ζ(2)ζ(5) + 2ζ(3)ζ(4) (789) ∞

H(k) k5(k + 1)5

= 70ζ(2) − 105ζ(3) + 15ζ(4) − 25ζ(5) + 10ζ(2)ζ(3) + ζ(6) (790)

k=1

∞

- 1

- 2


H(k) k4(k + 1)6

(112ζ(2) − 154ζ(3) + 5ζ(4) − 46ζ(5) + 22ζ(2)ζ(3) − 6ζ(6)

=

k=1

+4ζ(3)2 − 6ζ(7) + 2ζ(2)ζ(5) + 2ζ(3)ζ(4) (791) ∞

H(k) k3(k + 1)7

1 4

(112ζ(2) − 140ζ(3) − 10ζ(4) − 80ζ(5) + 40ζ(2)ζ(3) − 18ζ(6)

=

k=1

+12ζ(3)2 − 36ζ(7) + 12ζ(2)ζ(5) + 12ζ(3)ζ(4) − 5ζ(8) + 4ζ(3)ζ(5) (792) ∞

H(k) k2(k + 1)8

- 1

- 2


(16ζ(2) − 18ζ(3) − 3ζ(4) − 20ζ(5) + 10ζ(2)ζ(3) − 6ζ(6)

=

k=1

+4ζ(3)2 − 18ζ(7) + 6ζ(2)ζ(5) + 6ζ(3)ζ(4) − 5ζ(8) + 4ζ(3)ζ(5) − 8ζ(9)

+2ζ(3)ζ(6) + 2ζ(4)ζ(5) + 2ζ(2)ζ(7)) (793)

∞

H(k) k(k + 1)9

1 4

4ζ(2) − 4ζ(3) − ζ(4) − 8ζ(5) + 4ζ(2)ζ(3) − 3ζ(6) + 2ζ(3)2

=

k=1

−12ζ(7) + 4ζ(2)ζ(5) + 4ζ(3)ζ(4) − 5ζ(8) + 4ζ(3)ζ(5) − 16ζ(9)

+4ζ(3)ζ(6) + 4ζ(4)ζ(5) + 4ζ(2)ζ(7) − 7ζ(10) + 4ζ(3)ζ(7)

+2ζ(5)2 (794)

= 5ζ(11) − ζ(2)ζ(9) − ζ(3)ζ(8) − ζ(4)ζ(7) − ζ(5)ζ(6) (795)

(k + 1)10

k=1

∞

H(k) k9(k + 2)

1 512

(1 + ζ(2) − 4ζ(3) + 5ζ(4) − 24ζ(5) + 8ζ(2)ζ(3) + 28ζ(6)

=

k=1

−8ζ(3)2 − 128ζ(7) + 32ζ(2)ζ(5) + 32ζ(3)ζ(4) + 144ζ(8) − 64ζ(3)ζ(5) −640ζ(9) + 128ζ(3)ζ(6) + 128ζ(4)ζ(5) + 128ζ(2)ζ(7) + 704ζ(10) −256ζ(3)ζ(7) − 128ζ(5)2 (796)

∞

H(k) k8(k + 1)(k + 2)

1 256

(1 − 255ζ(2) + 508ζ(3) − 315ζ(4) + 744ζ(5) − 248ζ(2)ζ(3)

=

k=1

−420ζ(6) + 120ζ(3)2 + 896ζ(7) − 224ζ(2)ζ(5) − 224ζ(3)ζ(4) − 432ζ(8)

+192ζ(3)ζ(5) + 640ζ(9) − 128ζ(3)ζ(6) − 128ζ(4)ζ(5) −128ζ(2)ζ(7)) (797)

∞

1 128

H(k) k7(k + 1)2(k + 2)

(1 + 769ζ(2) − 1412ζ(3) + 645ζ(4) − 1176ζ(5) + 392ζ(2)ζ(3)

=

k=1

+476ζ(6) − 136ζ(3)2 − 640ζ(7) + 160ζ(2)ζ(5) + 160ζ(3)ζ(4) + 144ζ(8) −64ζ(3)ζ(5)) (798)

∞

1 64

H(k) k6(k + 1)3(k + 2)

(1 − 1023ζ(2) + 1724ζ(3) − 539ζ(4) + 744ζ(5) − 248ζ(2)ζ(3)

=

k=1

−196ζ(6) + 56ζ(3)2 + 128ζ(7) − 32ζ(2)ζ(5) − 32ζ(3)ζ(4) (799) ∞

H(k) k5(k + 1)4(k + 2)

1 32

(1 + 769ζ(2) − 1188ζ(3) + 213ζ(4) − 280ζ(5) + 104ζ(2)ζ(3)

=

k=1

+28ζ(6) − 8ζ(3)2 (800) ∞

H(k) k4(k + 1)5(k + 2)

1 16

(1 − 351ζ(2) + 492ζ(3) − 27ζ(4) + 120ζ(5) − 56ζ(2)ζ(3)

=

k=1

+12ζ(6) − 8ζ(3)2 (801) ∞

H(k) k3(k + 1)6(k + 2)

1 8

(1 + 97ζ(2) − 124ζ(3) − 7ζ(4) − 64ζ(5) + 32ζ(2)ζ(3)

=

k=1

−12ζ(6) + 8ζ(3)2 − 24ζ(7) + 8ζ(2)ζ(5) + 8ζ(3)ζ(4) (802) ∞

1 4

H(k) k2(k + 1)7(k + 2)

(1 − 15ζ(2) + 16ζ(3) + 3ζ(4) + 16ζ(5) − 8ζ(2)ζ(3) + 6ζ(6)

=

k=1

−4ζ(3)2 + 12ζ(7) − 4ζ(2)ζ(5) − 4ζ(3)ζ(4) + 5ζ(8) − 4ζ(3)ζ(5) (803) ∞

- 1

- 2


H(k) k(k + 1)8(k + 2)

(1 + ζ(2) − 2ζ(3) − 4ζ(5) + 2ζ(2)ζ(3) − 6ζ(7) + 2ζ(2)ζ(5)

=

k=1

+2ζ(3)ζ(4) − 8ζ(9) + 2ζ(3)ζ(6) + 2ζ(4)ζ(5) + 2ζ(2)ζ(7)) (804)

1 4

4 − 4ζ(3) + ζ(4) − 8ζ(5) + 4ζ(2)ζ(3) + 3ζ(6) − 2ζ(3)2

=

(k + 1)9(k + 2)

k=1

−12ζ(7) + 4ζ(2)ζ(5) + 4ζ(3)ζ(4) + 5ζ(8) − 4ζ(3)ζ(5) − 16ζ(9)

+4ζ(3)ζ(6) + 4ζ(4)ζ(5) + 4ζ(2)ζ(7) + 7ζ(10) − 4ζ(3)ζ(7) −2ζ(5)2 (805)

∞

1 256

H(k) k8(k + 2)2

(−6 − 3ζ(2) + 15ζ(3) − 15ζ(4) + 60ζ(5) − 20ζ(2)ζ(3) − 56ζ(6)

=

k=1

+16ζ(3)2 + 192ζ(7) − 48ζ(2)ζ(5) − 48ζ(3)ζ(4) − 144ζ(8) + 64ζ(3)ζ(5)

+320ζ(9) − 64ζ(3)ζ(6) − 64ζ(4)ζ(5) − 64ζ(2)ζ(7)) (806)

∞

1 256

H(k) k7(k + 1)(k + 2)2

(13 − 249ζ(2) + 478ζ(3) − 285ζ(4) + 624ζ(5) − 208ζ(2)ζ(3)

=

k=1

−308ζ(6) + 88ζ(3)2 + 512ζ(7) − 128ζ(2)ζ(5) − 128ζ(3)ζ(4) − 144ζ(8)

+64ζ(3)ζ(5)) (807)

∞

H(k) k6(k + 1)2(k + 2)2

1 64

(−7 − 260ζ(2) + 467ζ(3) − 180ζ(4) + 276ζ(5) − 92ζ(2)ζ(3)

=

k=1

−84ζ(6) + 24ζ(3)2 + 64ζ(7) − 16ζ(2)ζ(5) − 16ζ(3)ζ(4) (808) ∞

H(k) k5(k + 1)3(k + 2)2

1 64

(−15 + 503ζ(2) − 790ζ(3) + 179ζ(4) − 192ζ(5) + 64ζ(2)ζ(3)

=

k=1

+28ζ(6) − 8ζ(3)2 (809) ∞

H(k) k4(k + 1)4(k + 2)2

1 16

(−8 − 133ζ(2) + 199ζ(3) − 17ζ(4) + 44ζ(5)

=

k=1

−20ζ(2)ζ(3)) (810)

∞

H(k) k3(k + 1)5(k + 2)2

1 16

(−17 + 85ζ(2) − 94ζ(3) − 7ζ(4) − 32ζ(5) + 16ζ(2)ζ(3)

=

k=1

−12ζ(6) + 8ζ(3)2 (811) ∞

H(k) k2(k + 1)6(k + 2)2

1 4

(−9 − 6ζ(2) + 15ζ(3) + 16ζ(5) − 8ζ(2)ζ(3) + 12ζ(7)

=

k=1

−4ζ(2)ζ(5) − 4ζ(3)ζ(4)) (812)

∞

H(k) k(k + 1)7(k + 2)2

1 4

(−19 + 3ζ(2) + 14ζ(3) − 3ζ(4) + 16ζ(5) − 8ζ(2)ζ(3) − 6ζ(6)

=

k=1

+4ζ(3)2 + 12ζ(7) − 4ζ(2)ζ(5) − 4ζ(3)ζ(4) − 5ζ(8) + 4ζ(3)ζ(5) (813) ∞

H(k) (k + 1)8(k + 2)2

1 2

(20 − 2ζ(2) − 16ζ(3) + 3ζ(4) − 20ζ(5) + 10ζ(2)ζ(3) + 6ζ(6)

=

k=1

−4ζ(3)2 − 18ζ(7) + 6ζ(2)ζ(5) + 6ζ(3)ζ(4) + 5ζ(8) − 4ζ(3)ζ(5) − 8ζ(9)

+2ζ(3)ζ(6) + 2ζ(4)ζ(5) + 2ζ(2)ζ(7)) (814)

(34 + 5ζ(2) − 51ζ(3) + 37ζ(4) − 120ζ(5) + 40ζ(2)ζ(3) + 84ζ(6)

=

k7(k + 2)3

256

k=1

−24ζ(3)2 − 192ζ(7) + 48ζ(2)ζ(5) + 48ζ(3)ζ(4) + 72ζ(8) −32ζ(3)ζ(5)) (815)

∞

1 256

H(k) k6(k + 1)(k + 2)3

(81 − 239ζ(2) + 376ζ(3) − 211ζ(4) + 384ζ(5) − 128ζ(2)ζ(3)

=

k=1

−140ζ(6) + 40ζ(3)2 + 128ζ(7) − 32ζ(2)ζ(5) − 32ζ(3)ζ(4) (816) ∞

1 128

H(k) k5(k + 1)2(k + 2)3

(95 + 281ζ(2) − 558ζ(3) + 149ζ(4) − 168ζ(5)

=

k=1

+56ζ(2)ζ(3) + 28ζ(6) − 8ζ(3)2 (817) ∞

H(k) k4(k + 1)3(k + 2)3

1 32

(55 − 111ζ(2) + 116ζ(3) − 15ζ(4) + 12ζ(5)

=

k=1

−4ζ(2)ζ(3)) (818)

∞

H(k) k3(k + 1)4(k + 2)3

1 16

(63 + 22ζ(2) − 83ζ(3) + 2ζ(4) − 32ζ(5)

=

k=1

+16ζ(2)ζ(3)) (819)

∞

H(k) k2(k + 1)5(k + 2)3

1 16

(143 − 41ζ(2) − 72ζ(3) + 11ζ(4) − 32ζ(5) + 16ζ(2)ζ(3)

=

k=1

+12ζ(6) − 8ζ(3)2 (820) ∞

H(k) k(k + 1)6(k + 2)3

1 8

(161 − 29ζ(2) − 102ζ(3) + 11ζ(4) − 64ζ(5) + 32ζ(2)ζ(3)

=

k=1

+12ζ(6) − 8ζ(3)2 − 24ζ(7) + 8ζ(2)ζ(5) + 8ζ(3)ζ(4) (821) ∞

H(k) (k + 1)7(k + 2)3

1 4

(180 − 32ζ(2) − 116ζ(3) + 14ζ(4) − 80ζ(5) + 40ζ(2)ζ(3)

=

k=1

+18ζ(6) − 12ζ(3)2 − 36ζ(7) + 12ζ(2)ζ(5) + 12ζ(3)ζ(4) + 5ζ(8) −4ζ(3)ζ(5)) (822)

∞

1 256

H(k) k6(k + 2)4

(122 − 9ζ(2) − 107ζ(3) + 43ζ(4) − 128ζ(5) + 44ζ(2)ζ(3)

=

k=1

+56ζ(6) − 16ζ(3)2 − 64ζ(7) + 16ζ(2)ζ(5) + 16ζ(3)ζ(4) (823) ∞

1 256

H(k) k5(k + 1)(k + 2)4

(325 − 257ζ(2) + 162ζ(3) − 125ζ(4) + 128ζ(5) − 40ζ(2)ζ(3)

=

k=1

−28ζ(6) + 8ζ(3)2 (824)

(−105 − 6ζ(2) + 99ζ(3) − 6ζ(4) + 10ζ(5)

=

k4(k + 1)2(k + 2)4

32

k=1

−4ζ(2)ζ(3)) (825)

∞

1 32

H(k) k3(k + 1)3(k + 2)4

(265 − 99ζ(2) − 82ζ(3) − 3ζ(4) − 8ζ(5)

=

k=1

+4ζ(2)ζ(3)) (826)

∞

1 16

H(k) k2(k + 1)4(k + 2)4

(−328 + 77ζ(2) + 165ζ(3) + ζ(4) + 40ζ(5)

=

k=1

−20ζ(2)ζ(3)) (827)

∞

1 16

H(k) k(k + 1)5(k + 2)4

(799 − 195ζ(2) − 402ζ(3) + 9ζ(4) − 112ζ(5) + 56ζ(2)ζ(3)

=

k=1

+12ζ(6) − 8ζ(3)2 (828) ∞

H(k) (k + 1)6(k + 2)4

- 1

- 2


(−240 + 56ζ(2) + 126ζ(3) − 5ζ(4) + 44ζ(5) − 22ζ(2)ζ(3)

=

k=1

−6ζ(6) + 4ζ(3)2 + 6ζ(7) − 2ζ(2)ζ(5) − 2ζ(3)ζ(4) (829) ∞

H(k) k5(k + 2)5

1 256

(315 − 58ζ(2) − 163ζ(3) + 2ζ(4) − 108ζ(5) + 40ζ(2)ζ(3)

=

k=1

+8ζ(6)) (830)

∞

H(k) k4(k + 1)(k + 2)5

1 256

(955 − 373ζ(2) − 164ζ(3) − 121ζ(4) − 88ζ(5) + 40ζ(2)ζ(3)

=

k=1

−12ζ(6) + 8ζ(3)2 (831) ∞

H(k) k3(k + 1)2(k + 2)5

1 128

(1375 − 349ζ(2) − 560ζ(3) − 97ζ(4) − 128ζ(5)

=

k=1

+56ζ(2)ζ(3) − 12ζ(6) + 8ζ(3)2 (832) ∞

H(k) k2(k + 1)3(k + 2)5

1 64

(1905 − 547ζ(2) − 724ζ(3) − 103ζ(4) − 144ζ(5)

=

k=1

+64ζ(2)ζ(3) − 12ζ(6) + 8ζ(3)2 (833) ∞

1 32

H(k) k(k + 1)4(k + 2)5

(2561 − 701ζ(2) − 1054ζ(3) − 105ζ(4) − 224ζ(5) + 104ζ(2)ζ(3)

=

k=1

−12ζ(6) + 8ζ(3)2 (834) ∞

H(k) (k + 1)5(k + 2)5

= 210 − 56ζ(2) − 91ζ(3) − 6ζ(4) − 21ζ(5) + 10ζ(2)ζ(3) (835)

k=1

(634 − 135ζ(2) − 205ζ(3) − 83ζ(4) − 140ζ(5) + 44ζ(2)ζ(3)

=

k4(k + 2)6

256

k=1

−40ζ(6) + 16ζ(3)2 − 48ζ(7) + 16ζ(2)ζ(5) + 16ζ(3)ζ(4) (836) ∞

1 256

H(k) k3(k + 1)(k + 2)6

(2223 − 643ζ(2) − 574ζ(3) − 287ζ(4) − 368ζ(5) + 128ζ(2)ζ(3)

=

k=1

−92ζ(6) + 40ζ(3)2 − 96ζ(7) + 32ζ(2)ζ(5) + 32ζ(3)ζ(4) (837) ∞

1 64

H(k) k2(k + 1)2(k + 2)6

(1799 − 496ζ(2) − 567ζ(3) − 192ζ(4) − 248ζ(5)

=

k=1

+92ζ(2)ζ(3) − 52ζ(6) + 24ζ(3)2 − 48ζ(7) + 16ζ(2)ζ(5)

+16ζ(3)ζ(4)) (838)

∞

1 64

H(k) k(k + 1)3(k + 2)6

(−5503 + 1539ζ(2) + 1858ζ(3) + 487ζ(4) + 640ζ(5)

=

k=1

−248ζ(2)ζ(3) + 116ζ(6) − 56ζ(3)2 + 96ζ(7) − 32ζ(2)ζ(5) −32ζ(3)ζ(4)) (839)

∞

H(k) (k + 1)4(k + 2)6

1 2

(504 − 140ζ(2) − 182ζ(3) − 37ζ(4) − 54ζ(5) + 22ζ(2)ζ(3)

=

k=1

−8ζ(6) + 4ζ(3)2 − 6ζ(7) + 2ζ(2)ζ(5) + 2ζ(3)ζ(4) (840) ∞

H(k) k3(k + 2)7

1 256

(1058 − 205ζ(2) − 233ζ(3) − 173ζ(4) − 208ζ(5) + 40ζ(2)ζ(3)

=

k=1

−116ζ(6) + 24ζ(3)2 − 176ζ(7) + 48ζ(2)ζ(5) + 48ζ(3)ζ(4) − 40ζ(8)

+32ζ(3)ζ(5)) (841)

∞

H(k) k2(k + 1)(k + 2)7

1 256

(4339 − 1053ζ(2) − 1040ζ(3) − 633ζ(4) − 784ζ(5)

=

k=1

+208ζ(2)ζ(3) − 324ζ(6) + 88ζ(3)2 − 448ζ(7) + 128ζ(2)ζ(5) + 128ζ(3)ζ(4) −80ζ(8) + 64ζ(3)ζ(5)) (842)

∞

H(k) k(k + 1)2(k + 2)7

1 128

(7937 − 2045ζ(2) − 2174ζ(3) − 1017ζ(4) − 1280ζ(5)

=

k=1

+392ζ(2)ζ(3) − 428ζ(6) + 136ζ(3)2 − 544ζ(7) + 160ζ(2)ζ(5) + 160ζ(3)ζ(4) −80ζ(8) + 64ζ(3)ζ(5)) (843)

∞

1 4

H(k) (k + 1)3(k + 2)7

(840 − 224ζ(2) − 252ζ(3) − 94ζ(4) − 120ζ(5) + 40ζ(2)ζ(3)

=

k=1

−34ζ(6) + 12ζ(3)2 − 40ζ(7) + 12ζ(2)ζ(5) + 12ζ(3)ζ(4) − 5ζ(8)

+4ζ(3)ζ(5)) (844)

(1542 − 243ζ(2) − 249ζ(3) − 231ζ(4) − 248ζ(5) + 20ζ(2)ζ(3)

=

k2(k + 2)8

256

k=1

−200ζ(6) + 16ζ(3)2 − 272ζ(7) + 48ζ(2)ζ(5) + 48ζ(3)ζ(4) − 144ζ(8)

+64ζ(3)ζ(5) − 256ζ(9) + 64ζ(3)ζ(6) + 64ζ(4)ζ(5) + 64ζ(2)ζ(7)) (845)

∞

1 256

H(k) k(k + 1)(k + 2)8

(−7423 + 1539ζ(2) + 1538ζ(3) + 1095ζ(4) + 1280ζ(5) − 248ζ(2)ζ(3)

=

k=1

+724ζ(6) − 120ζ(3)2 + 992ζ(7) − 224ζ(2)ζ(5) − 224ζ(3)ζ(4) + 368ζ(8) −192ζ(3)ζ(5) + 512ζ(9) − 128ζ(3)ζ(6) − 128ζ(4)ζ(5) −128ζ(2)ζ(7)) (846)

∞

1 2

H(k) (k + 1)2(k + 2)8

(−240 + 56ζ(2) + 58ζ(3) + 33ζ(4) + 40ζ(5) − 10ζ(2)ζ(3)

=

k=1

+18ζ(6) − 4ζ(3)2 + 24ζ(7) − 6ζ(2)ζ(5) − 6ζ(3)ζ(4) + 7ζ(8) −4ζ(3)ζ(5) + 8ζ(9) − 2ζ(3)ζ(6) − 2ζ(4)ζ(5) − 2ζ(2)ζ(7)) (847)

∞

1 512

H(k) k(k + 2)9

(4097 − 509ζ(2) − 510ζ(3) − 505ζ(4) − 512ζ(5) + 8ζ(2)ζ(3)

=

k=1

−492ζ(6) + 8ζ(3)2 − 544ζ(7) + 32ζ(2)ζ(5) + 32ζ(3)ζ(4) − 464ζ(8) +64ζ(3)ζ(5) − 768ζ(9) + 128ζ(3)ζ(6) + 128ζ(4)ζ(5) + 128ζ(2)ζ(7) −448ζ(10) + 256ζ(3)ζ(7) + 128ζ(5)2 (848)

∞

H(k) (k + 1)(k + 2)9

1 4

(180 − 32ζ(2) − 32ζ(3) − 25ζ(4) − 28ζ(5) + 4ζ(2)ζ(3) − 19ζ(6)

=

k=1

+2ζ(3)2 − 24ζ(7) + 4ζ(2)ζ(5) + 4ζ(3)ζ(4) − 13ζ(8) + 4ζ(3)ζ(5) −20ζ(9) + 4ζ(3)ζ(6) + 4ζ(4)ζ(5) + 4ζ(2)ζ(7) − 7ζ(10) + 4ζ(3)ζ(7)

+2ζ(5)2 (849) ∞

H(k) (k + 2)10

= 10 − ζ(2) − ζ(3) − ζ(4) − ζ(5) − ζ(6) − ζ(7) − ζ(8) − ζ(9) − ζ(10) − 5ζ(11)

k=1

+ ζ(2)ζ(9) + ζ(3)ζ(8) + ζ(4)ζ(7) + ζ(5)ζ(6) (850)

∞

H(k)2 k9

- 1

- 2


(26ζ(11) − 2ζ(2)ζ(9) − 9ζ(3)ζ(8) − 5ζ(4)ζ(7) − 7ζ(5)ζ(6)

=

k=1

+2ζ(3)2ζ(5) (851) ∞

H(k)2 k8(k + 1)

1 24 −72ζ(3) + 102ζ(4) − 84ζ(5) + 24ζ(2)ζ(3) + 97ζ(6) − 48ζ(3)2 −144ζ(7) + 24ζ(2)ζ(5) + 60ζ(3)ζ(4) + 24M(2,6) − 220ζ(9) + 84ζ(3)ζ(6)

=

k=1

+60ζ(4)ζ(5) + 24ζ(2)ζ(7) − 8ζ(3)3 + 24M(2,8) (852)

1 12

(252ζ(3) − 339ζ(4) + 210ζ(5) − 60ζ(2)ζ(3) − 194ζ(6)

=

k7(k + 1)2

k=1

+96ζ(3)2 + 216ζ(7) − 36ζ(2)ζ(5) − 90ζ(3)ζ(4) − 24M(2,6) + 110ζ(9) −42ζ(3)ζ(6) − 30ζ(4)ζ(5) − 12ζ(2)ζ(7) + 4ζ(3)3 (853)

∞

H(k)2 k6(k + 1)3

1 4

(−252ζ(3) + 321ζ(4) − 146ζ(5) + 44ζ(2)ζ(3) + 97ζ(6)

=

k=1

−48ζ(3)2 − 72ζ(7) + 12ζ(2)ζ(5) + 30ζ(3)ζ(4) + 4M(2,6) (854) ∞

H(k)2 k5(k + 1)4

1 24

(2520ζ(3) − 3030ζ(4) + 1020ζ(5) − 360ζ(2)ζ(3) − 425ζ(6)

=

k=1

+216ζ(3)2 + 144ζ(7) − 24ζ(2)ζ(5) − 60ζ(3)ζ(4) (855) ∞

H(k)2 k4(k + 1)5

1 24

(2520ζ(3) − 2850ζ(4) + 780ζ(5) − 360ζ(2)ζ(3) − 245ζ(6)

=

k=1

+144ζ(3)2 + 24ζ(7) − 24ζ(2)ζ(5) + 12ζ(3)ζ(4) (856) ∞

H(k)2 k3(k + 1)6

1 4

(252ζ(3) − 267ζ(4) + 74ζ(5) − 44ζ(2)ζ(3) − 37ζ(6)

=

k=1

+24ζ(3)2 + 12ζ(7) − 12ζ(2)ζ(5) + 6ζ(3)ζ(4) + 14ζ(8) − 8ζ(3)ζ(5) −4M(2,6)) (857)

∞

H(k)2 k2(k + 1)7

1 12

(−252ζ(3) + 249ζ(4) − 90ζ(5) + 60ζ(2)ζ(3) + 74ζ(6)

=

k=1

−48ζ(3)2 − 36ζ(7) + 36ζ(2)ζ(5) − 18ζ(3)ζ(4) − 84ζ(8) + 48ζ(3)ζ(5)

+24M(2,6) + 2ζ(9) − 18ζ(3)ζ(6) − 6ζ(4)ζ(5) + 12ζ(2)ζ(7) + 4ζ(3)3 (858) ∞

H(k)2 k(k + 1)8

1 24

72ζ(3) − 66ζ(4) + 36ζ(5) − 24ζ(2)ζ(3) − 37ζ(6) + 24ζ(3)2

=

k=1

+24ζ(7) − 24ζ(2)ζ(5) + 12ζ(3)ζ(4) + 84ζ(8) − 48ζ(3)ζ(5) − 24M(2,6) −4ζ(9) + 36ζ(3)ζ(6) + 12ζ(4)ζ(5) − 24ζ(2)ζ(7) − 8ζ(3)3 + 108ζ(10) −48ζ(3)ζ(7) − 24ζ(5)2 − 24M(2,8) (859)

∞

H(k)2 (k + 1)9

1 2

(4ζ(11) + 2ζ(2)ζ(9) − 5ζ(3)ζ(8) − ζ(4)ζ(7) − 3ζ(5)ζ(6)

=

k=1

+2ζ(3)2ζ(5) (860) ∞

H(k)2 k8(k + 2)

1 1536

(−6 − 6ζ(2) − 18ζ(3) + 51ζ(4) − 84ζ(5) + 24ζ(2)ζ(3) + 194ζ(6)

=

k=1

−96ζ(3)2 − 576ζ(7) + 96ζ(2)ζ(5) + 240ζ(3)ζ(4) + 192M(2,6) − 3520ζ(9)

+1344ζ(3)ζ(6) + 960ζ(4)ζ(5) + 384ζ(2)ζ(7) − 128ζ(3)3 + 768M(2,8) (861)

∞

H(k)2 k7(k + 1)(k + 2)

1 768

(6 + 6ζ(2) − 2286ζ(3) + 3213ζ(4) − 2604ζ(5) + 744ζ(2)ζ(3)

=

k=1

+2910ζ(6) − 1440ζ(3)2 − 4032ζ(7) + 672ζ(2)ζ(5) + 1680ζ(3)ζ(4) + 576M(2,6) −3520ζ(9) + 1344ζ(3)ζ(6) + 960ζ(4)ζ(5) + 384ζ(2)ζ(7) − 128ζ(3)3 (862)

∞

H(k)2 k6(k + 1)2(k + 2)

1 384

(6 + 6ζ(2) + 5778ζ(3) − 7635ζ(4) + 4116ζ(5)

=

k=1

−1176ζ(2)ζ(3) − 3298ζ(6) + 1632ζ(3)2 + 2880ζ(7) − 480ζ(2)ζ(5) −1200ζ(3)ζ(4) − 192M(2,6)) (863)

∞

H(k)2 k5(k + 1)3(k + 2)

1 192

(−6 − 6ζ(2) + 6318ζ(3) − 7773ζ(4) + 2892ζ(5)

=

k=1

−936ζ(2)ζ(3) − 1358ζ(6) + 672ζ(3)2 + 576ζ(7) − 96ζ(2)ζ(5) −240ζ(3)ζ(4)) (864)

∞

H(k)2 k4(k + 1)4(k + 2)

1 32

(2 + 2ζ(2) + 1254ζ(3) − 1449ζ(4) + 396ζ(5) − 168ζ(2)ζ(3)

=

k=1

−114ζ(6) + 64ζ(3)2 (865) ∞

H(k)2 k3(k + 1)5(k + 2)

1 48

(6 + 6ζ(2) − 1278ζ(3) + 1353ζ(4) − 372ζ(5) + 216ζ(2)ζ(3)

=

k=1

+148ζ(6) − 96ζ(3)2 − 48ζ(7) + 48ζ(2)ζ(5) − 24ζ(3)ζ(4) (866) ∞

H(k)2 k2(k + 1)6(k + 2)

1 24

(6 + 6ζ(2) + 234ζ(3) − 249ζ(4) + 72ζ(5) − 48ζ(2)ζ(3)

=

k=1

−74ζ(6) + 48ζ(3)2 + 24ζ(7) − 24ζ(2)ζ(5) + 12ζ(3)ζ(4) + 84ζ(8) −48ζ(3)ζ(5) − 24M(2,6)) (867)

∞

H(k)2 k(k + 1)7(k + 2)

1 6

(3 + 3ζ(2) − 9ζ(3) − 9ζ(5) + 6ζ(2)ζ(3) − 6ζ(7)

=

k=1

+6ζ(2)ζ(5) − 3ζ(3)ζ(4) + ζ(9) − 9ζ(3)ζ(6) − 3ζ(4)ζ(5)

+6ζ(2)ζ(7) + 2ζ(3)3 (868) ∞

H(k)2 (k + 1)8(k + 2)

1 24

(24 + 24ζ(2) − 66ζ(4) − 36ζ(5) + 24ζ(2)ζ(3) − 37ζ(6)

=

k=1

+24ζ(3)2 − 24ζ(7) + 24ζ(2)ζ(5) − 12ζ(3)ζ(4) + 84ζ(8) − 48ζ(3)ζ(5) −24M(2,6) + 4ζ(9) − 36ζ(3)ζ(6) − 12ζ(4)ζ(5) + 24ζ(2)ζ(7) + 8ζ(3)3

+108ζ(10) − 48ζ(3)ζ(7) − 24ζ(5)2 − 24M(2,8) (869) ∞

H(k)2 k7(k + 2)2

1 1536

(78 + 42ζ(2) + 102ζ(3) − 339ζ(4) + 420ζ(5) − 120ζ(2)ζ(3)

=

k=1

−776ζ(6) + 384ζ(3)2 + 1728ζ(7) − 288ζ(2)ζ(5) − 720ζ(3)ζ(4) − 384M(2,6)

+3520ζ(9) − 1344ζ(3)ζ(6) − 960ζ(4)ζ(5) − 384ζ(2)ζ(7) + 128ζ(3)3 (870)

(42 + 24ζ(2) − 1092ζ(3) + 1437ζ(4) − 1092ζ(5)

=

k6(k + 1)(k + 2)2

384

k=1

+312ζ(2)ζ(3) + 1067ζ(6) − 528ζ(3)2 − 1152ζ(7) + 192ζ(2)ζ(5)

+480ζ(3)ζ(4) + 96M(2,6)) (871)

∞

H(k)2 k5(k + 1)2(k + 2)2

1 128

(30 + 18ζ(2) + 1198ζ(3) − 1587ζ(4) + 644ζ(5)

=

k=1

−184ζ(2)ζ(3) − 388ζ(6) + 192ζ(3)2 + 192ζ(7) − 32ζ(2)ζ(5) −80ζ(3)ζ(4)) (872)

∞

H(k)2 k4(k + 1)3(k + 2)2

1 96

(48 + 30ζ(2) − 1362ζ(3) + 1506ζ(4) − 480ζ(5)

=

k=1

+192ζ(2)ζ(3) + 97ζ(6) − 48ζ(3)2 (873) ∞

H(k)2 k3(k + 1)4(k + 2)2

1 96

(102 + 66ζ(2) + 1038ζ(3) − 1335ζ(4) + 228ζ(5)

=

k=1

−120ζ(2)ζ(3) − 148ζ(6) + 96ζ(3)2 (874) ∞

H(k)2 k2(k + 1)5(k + 2)2

1 8

(18 + 12ζ(2) − 40ζ(3) + 3ζ(4) − 24ζ(5) + 16ζ(2)ζ(3)

=

k=1

−8ζ(7) + 8ζ(2)ζ(5) − 4ζ(3)ζ(4)) (875)

∞

H(k)2 k(k + 1)6(k + 2)2

1 24

(114 + 78ζ(2) − 6ζ(3) − 231ζ(4) − 72ζ(5) + 48ζ(2)ζ(3)

=

k=1

−74ζ(6) + 48ζ(3)2 − 24ζ(7) + 24ζ(2)ζ(5) − 12ζ(3)ζ(4) + 84ζ(8) −48ζ(3)ζ(5) − 24M(2,6)) (876)

∞

H(k)2 (k + 1)7(k + 2)2

1 12

(120 + 84ζ(2) − 24ζ(3) − 231ζ(4) − 90ζ(5) + 60ζ(2)ζ(3)

=

k=1

−74ζ(6) + 48ζ(3)2 − 36ζ(7) + 36ζ(2)ζ(5) − 18ζ(3)ζ(4) + 84ζ(8) −48ζ(3)ζ(5) − 24M(2,6) + 2ζ(9) − 18ζ(3)ζ(6) − 6ζ(4)ζ(5) + 12ζ(2)ζ(7)

+4ζ(3)3 (877) ∞

H(k)2 k6(k + 2)3

1 512

(−162 − 34ζ(2) − 54ζ(3) + 325ζ(4) − 292ζ(5) + 88ζ(2)ζ(3)

=

k=1

+388ζ(6) − 192ζ(3)2 − 576ζ(7) + 96ζ(2)ζ(5) + 240ζ(3)ζ(4) + 64M(2,6)

(878)

∞

H(k)2 k5(k + 1)(k + 2)3

1 768

(−570 − 150ζ(2) + 2022ζ(3) − 1899ζ(4) + 1308ζ(5)

=

k=1

−360ζ(2)ζ(3) − 970ζ(6) + 480ζ(3)2 + 576ζ(7) − 96ζ(2)ζ(5) −240ζ(3)ζ(4)) (879)

1 192

(330 + 102ζ(2) + 786ζ(3) − 1431ζ(4) + 312ζ(5)

=

k4(k + 1)2(k + 2)3

k=1

−96ζ(2)ζ(3) − 97ζ(6) + 48ζ(3)2 (880) ∞

H(k)2 k3(k + 1)3(k + 2)3

1 32

(126 + 44ζ(2) − 192ζ(3) + 25ζ(4) − 56ζ(5)

=

k=1

+32ζ(2)ζ(3)) (881)

∞

H(k)2 k2(k + 1)4(k + 2)3

1 96

(−858 − 330ζ(2) + 114ζ(3) + 1185ζ(4) + 108ζ(5)

=

k=1

−72ζ(2)ζ(3) + 148ζ(6) − 96ζ(3)2 (882) ∞

H(k)2 k(k + 1)5(k + 2)3

1 48

(966 + 402ζ(2) − 354ζ(3) − 1167ζ(4) − 252ζ(5)

=

k=1

+168ζ(2)ζ(3) − 148ζ(6) + 96ζ(3)2 − 48ζ(7) + 48ζ(2)ζ(5) −24ζ(3)ζ(4)) (883)

∞

H(k)2 (k + 1)6(k + 2)3

1 4

(180 + 80ζ(2) − 60ζ(3) − 233ζ(4) − 54ζ(5) + 36ζ(2)ζ(3)

=

k=1

−37ζ(6) + 24ζ(3)2 − 12ζ(7) + 12ζ(2)ζ(5) − 6ζ(3)ζ(4) + 14ζ(8) −8ζ(3)ζ(5) − 4M(2,6)) (884)

∞

H(k)2 k5(k + 2)4

1 1536

(1950 − 6ζ(2) − 282ζ(3) − 1647ζ(4) + 828ζ(5) − 264ζ(2)ζ(3)

=

k=1

−850ζ(6) + 432ζ(3)2 + 576ζ(7) − 96ζ(2)ζ(5) − 240ζ(3)ζ(4) (885) ∞

H(k)2 k4(k + 1)(k + 2)4

1 64

(210 + 12ζ(2) − 192ζ(3) + 21ζ(4) − 40ζ(5) + 8ζ(2)ζ(3)

=

k=1

+10ζ(6) − 4ζ(3)2 (886) ∞

H(k)2 k3(k + 1)2(k + 2)4

1 192

(1590 + 174ζ(2) − 366ζ(3) − 1305ζ(4) + 72ζ(5)

=

k=1

−48ζ(2)ζ(3) − 37ζ(6) + 24ζ(3)2 (887) ∞

H(k)2 k2(k + 1)3(k + 2)4

1 96

(1968 + 306ζ(2) − 942ζ(3) − 1230ζ(4) − 96ζ(5)

=

k=1

+48ζ(2)ζ(3) − 37ζ(6) + 24ζ(3)2 (888) ∞

H(k)2 k(k + 1)4(k + 2)4

1 32

(1598 + 314ζ(2) − 666ζ(3) − 1215ζ(4) − 100ζ(5)

=

k=1

+56ζ(2)ζ(3) − 74ζ(6) + 48ζ(3)2 (889)

(2880 + 672ζ(2) − 1176ζ(3) − 2406ζ(4) − 276ζ(5)

=

(k + 1)5(k + 2)4

24

k=1

+168ζ(2)ζ(3) − 185ζ(6) + 120ζ(3)2 − 24ζ(7) + 24ζ(2)ζ(5) −12ζ(3)ζ(4)) (890)

∞

H(k)2 k4(k + 2)5

1 1536

(−5730 + 702ζ(2) + 1818ζ(3) + 2073ζ(4) + 468ζ(5)

=

k=1

−216ζ(2)ζ(3) + 634ζ(6) − 384ζ(3)2 − 96ζ(7) + 96ζ(2)ζ(5) −48ζ(3)ζ(4)) (891)

∞

H(k)2 k3(k + 1)(k + 2)5

1 768

(8250 − 558ζ(2) − 4122ζ(3) − 1821ζ(4) − 948ζ(5)

=

k=1

+312ζ(2)ζ(3) − 514ζ(6) + 336ζ(3)2 + 96ζ(7) − 96ζ(2)ζ(5)

+48ζ(3)ζ(4)) (892)

∞

H(k)2 k2(k + 1)2(k + 2)5

1 128

(−3810 + 70ζ(2) + 1618ζ(3) + 1477ζ(4) + 268ζ(5)

=

k=1

−72ζ(2)ζ(3) + 196ζ(6) − 128ζ(3)2 − 32ζ(7) + 32ζ(2)ζ(5) −16ζ(3)ζ(4)) (893)

∞

H(k)2 k(k + 1)3(k + 2)5

1 192

(−15366 − 402ζ(2) + 6738ζ(3) + 6891ζ(4) + 996ζ(5)

=

k=1

−312ζ(2)ζ(3) + 662ζ(6) − 432ζ(3)2 − 96ζ(7) + 96ζ(2)ζ(5) −48ζ(3)ζ(4)) (894)

∞

H(k)2 (k + 1)4(k + 2)5

1 24

(−5040 − 336ζ(2) + 2184ζ(3) + 2634ζ(4) + 324ζ(5)

=

k=1

−120ζ(2)ζ(3) + 221ζ(6) − 144ζ(3)2 − 24ζ(7) + 24ζ(2)ζ(5) −12ζ(3)ζ(4)) (895)

∞

H(k)2 k3(k + 2)6

1 512

(4446 − 774ζ(2) − 1482ζ(3) − 915ζ(4) − 1100ζ(5)

=

k=1

+424ζ(2)ζ(3) − 452ζ(6) + 256ζ(3)2 − 288ζ(7) + 32ζ(2)ζ(5) + 176ζ(3)ζ(4)

+224ζ(8) − 128ζ(3)ζ(5) − 64M(2,6)) (896)

∞

H(k)2 k2(k + 1)(k + 2)6

1 384

(10794 − 1440ζ(2) − 4284ζ(3) − 2283ζ(4) − 2124ζ(5)

=

k=1

+792ζ(2)ζ(3) − 935ζ(6) + 552ζ(3)2 − 384ζ(7) + 288ζ(3)ζ(4) + 336ζ(8) −192ζ(3)ζ(5) − 96M(2,6)) (897)

∞

H(k)2 k(k + 1)2(k + 2)6

1 384

(33018 − 3090ζ(2) − 13422ζ(3) − 8997ζ(4) − 5052ζ(5)

=

k=1

+1800ζ(2)ζ(3) − 2458ζ(6) + 1488ζ(3)2 − 672ζ(7) − 96ζ(2)ζ(5)

+624ζ(3)ζ(4) + 672ζ(8) − 384ζ(3)ζ(5) − 192M(2,6)) (898)

∞

H(k)2 (k + 1)3(k + 2)6

1 4

(1008 − 56ζ(2) − 420ζ(3) − 331ζ(4) − 126ζ(5) + 44ζ(2)ζ(3)

=

k=1

−65ζ(6) + 40ζ(3)2 − 12ζ(7) − 4ζ(2)ζ(5) + 14ζ(3)ζ(4) + 14ζ(8) −8ζ(3)ζ(5) − 4M(2,6)) (899)

∞

H(k)2 k2(k + 2)7

1 1536

(26034 − 4782ζ(2) − 7578ζ(3) − 4389ζ(4) − 7020ζ(5)

=

k=1

+2376ζ(2)ζ(3) − 3032ζ(6) + 1248ζ(3)2 − 4704ζ(7) + 1248ζ(2)ζ(5)

+1680ζ(3)ζ(4) + 384ζ(8) − 384M(2,6) − 64ζ(9) + 576ζ(3)ζ(6) + 192ζ(4)ζ(5) −384ζ(2)ζ(7) − 128ζ(3)3 (900)

∞

H(k)2 k(k + 1)(k + 2)7

1 768

(47622 − 7662ζ(2) − 16146ζ(3) − 8955ζ(4) − 11268ζ(5)

=

k=1

+3960ζ(2)ζ(3) − 4902ζ(6) + 2352ζ(3)2 − 5472ζ(7) + 1248ζ(2)ζ(5)

+2256ζ(3)ζ(4) + 1056ζ(8) − 384ζ(3)ζ(5) − 576M(2,6) − 64ζ(9) + 576ζ(3)ζ(6)

+192ζ(4)ζ(5) − 384ζ(2)ζ(7) − 128ζ(3)3 (901) ∞

H(k)2 (k + 1)2(k + 2)7

1 12

(2520 − 336ζ(2) − 924ζ(3) − 561ζ(4) − 510ζ(5)

=

k=1

+180ζ(2)ζ(3) − 230ζ(6) + 120ζ(3)2 − 192ζ(7) + 36ζ(2)ζ(5) + 90ζ(3)ζ(4)

+54ζ(8) − 24ζ(3)ζ(5) − 24M(2,6) − 2ζ(9) + 18ζ(3)ζ(6) + 6ζ(4)ζ(5) −12ζ(2)ζ(7) − 4ζ(3)3 (902)

∞

H(k)2 k(k + 2)8

1 1536

(44538 − 7698ζ(2) − 10734ζ(3) − 6981ζ(4) − 10620ζ(5)

=

k=1

+2952ζ(2)ζ(3) − 5498ζ(6) + 1488ζ(3)2 − 9888ζ(7) + 2592ζ(2)ζ(5)

+2736ζ(3)ζ(4) − 2976ζ(8) + 1920ζ(3)ζ(5) − 192M(2,6) − 6208ζ(9)

+2112ζ(3)ζ(6) + 1728ζ(4)ζ(5) + 1152ζ(2)ζ(7) − 128ζ(3)3 + 3456ζ(10) −1536ζ(3)ζ(7) − 768ζ(5)2 − 768M(2,8) (903)

∞

H(k)2 (k + 1)(k + 2)8

1 24

(2880 − 480ζ(2) − 840ζ(3) − 498ζ(4) − 684ζ(5) + 216ζ(2)ζ(3)

=

k=1

−325ζ(6) + 120ζ(3)2 − 480ζ(7) + 120ζ(2)ζ(5) + 156ζ(3)ζ(4) − 60ζ(8)

+48ζ(3)ζ(5) − 24M(2,6) − 196ζ(9) + 84ζ(3)ζ(6) + 60ζ(4)ζ(5) + 24ζ(2)ζ(7) −8ζ(3)3 + 108ζ(10) − 48ζ(3)ζ(7) − 24ζ(5)2 − 24M(2,8) (904)

1 2

(−90 + 14ζ(2) + 18ζ(3) + 13ζ(4) + 18ζ(5) − 4ζ(2)ζ(3) + 11ζ(6)

=

(k + 2)9

k=1

−2ζ(3)2 + 18ζ(7) − 4ζ(2)ζ(5) − 4ζ(3)ζ(4) + 9ζ(8) − 4ζ(3)ζ(5)

+18ζ(9) − 4ζ(3)ζ(6) − 4ζ(4)ζ(5) − 4ζ(2)ζ(7) + 7ζ(10) − 4ζ(3)ζ(7) −2ζ(5)2 + 4ζ(11) + 2ζ(2)ζ(9) − 5ζ(3)ζ(8) − ζ(4)ζ(7) − 3ζ(5)ζ(6)

+2ζ(3)2ζ(5) (905) ∞

H(k)3 k8

= M(3,8) (906)

k=1

∞

H(k)3 k7(k + 1)

1 480

4800ζ(4) − 4800ζ(5) − 480ζ(2)ζ(3) + 2790ζ(6) − 1200ζ(3)2

=

k=1

−6930ζ(7) − 960ζ(2)ζ(5) + 6120ζ(3)ζ(4) − 2975ζ(8) − 600ζ(2)ζ(3)2

+2880ζ(3)ζ(5) + 1320M(2,6) − 10420ζ(9) + 5820ζ(3)ζ(6) + 6120ζ(4)ζ(5) −1440ζ(2)ζ(7) − 960ζ(3)3 − 4983ζ(10) + 3840ζ(3)ζ(7) + 240ζ(3)2ζ(4) −1680ζ(2)ζ(3)ζ(5) + 2160ζ(5)2 + 1560M(2,8) (907)

∞

H(k)3 k6(k + 1)2

1 48

2880ζ(4) − 2760ζ(5) − 288ζ(2)ζ(3) + 1116ζ(6) − 480ζ(3)2

=

k=1

−2079ζ(7) − 288ζ(2)ζ(5) + 1836ζ(3)ζ(4) − 595ζ(8) − 120ζ(2)ζ(3)2

+576ζ(3)ζ(5) + 264M(2,6) − 1042ζ(9) + 582ζ(3)ζ(6) + 612ζ(4)ζ(5) −144ζ(2)ζ(7) − 96ζ(3)3 (908)

∞

H(k)3 k5(k + 1)3

1 96

(14400ζ(4) − 13200ζ(5) − 1440ζ(2)ζ(3) + 3546ζ(6)

=

k=1

−1632ζ(3)2 − 4158ζ(7) − 576ζ(2)ζ(5) + 3672ζ(3)ζ(4) − 595ζ(8) −120ζ(2)ζ(3)2 + 576ζ(3)ζ(5) + 264M(2,6) (909)

∞

H(k)3 k4(k + 1)4

1 8

1600ζ(4) − 1400ζ(5) − 160ζ(2)ζ(3) + 252ζ(6) − 144ζ(3)2

=

k=1

−175ζ(7) − 32ζ(2)ζ(5) + 168ζ(3)ζ(4)) (910)

∞

H(k)3 k3(k + 1)5

1 96

14400ζ(4) − 12000ζ(5) − 1440ζ(2)ζ(3) + 1746ζ(6) − 1392ζ(3)2

=

k=1

−2142ζ(7) − 576ζ(2)ζ(5) + 2376ζ(3)ζ(4) + 43ζ(8) + 120ζ(2)ζ(3)2 −288ζ(3)ζ(5) + 24M(2,6)) (911)

∞

H(k)3 k2(k + 1)6

1 48 −2880ζ(4) + 2280ζ(5) + 288ζ(2)ζ(3) − 396ζ(6) + 384ζ(3)2

=

k=1

+1071ζ(7) + 288ζ(2)ζ(5) − 1188ζ(3)ζ(4) − 43ζ(8) − 120ζ(2)ζ(3)2 +288ζ(3)ζ(5) − 24M(2,6) + 394ζ(9) − 222ζ(3)ζ(6) − 396ζ(4)ζ(5) +144ζ(2)ζ(7) + 48ζ(3)3 (912)

4800ζ(4) − 3600ζ(5) − 480ζ(2)ζ(3) + 990ζ(6) − 960ζ(3)2

=

k(k + 1)7

480

k=1

−3570ζ(7) − 960ζ(2)ζ(5) + 3960ζ(3)ζ(4) + 215ζ(8) + 600ζ(2)ζ(3)2 −1440ζ(3)ζ(5) + 120M(2,6) − 3940ζ(9) + 2220ζ(3)ζ(6) + 3960ζ(4)ζ(5) −1440ζ(2)ζ(7) − 480ζ(3)3 + 1503ζ(10) − 2400ζ(3)ζ(7) − 240ζ(3)2ζ(4)

+1680ζ(2)ζ(3)ζ(5) − 1440ζ(5)2 − 120M(2,8) (913) ∞

H(k)3 (k + 1)8

- 1

- 2


(44ζ(11) − 21ζ(3)ζ(8) − 9ζ(4)ζ(7) − 15ζ(5)ζ(6)

=

k=1

+6ζ(3)2ζ(5) − 2M(3,8) (914) ∞

H(k)3 k7(k + 2)

1 7680

(60 + 120ζ(2) + 240ζ(3) + 600ζ(4) − 1200ζ(5) − 120ζ(2)ζ(3)

=

k=1

+1395ζ(6) − 600ζ(3)2 − 6930ζ(7) − 960ζ(2)ζ(5) + 6120ζ(3)ζ(4) − 5950ζ(8) −1200ζ(2)ζ(3)2 + 5760ζ(3)ζ(5) + 2640M(2,6) − 41680ζ(9) + 23280ζ(3)ζ(6)

+24480ζ(4)ζ(5) − 5760ζ(2)ζ(7) − 3840ζ(3)3 − 39864ζ(10) + 30720ζ(3)ζ(7)

+1920ζ(3)2ζ(4) − 13440ζ(2)ζ(3)ζ(5) + 17280ζ(5)2 + 12480M(2,8) (915) ∞

H(k)3 k6(k + 1)(k + 2)

1 768

(12 + 24ζ(2) + 48ζ(3) − 7560ζ(4) + 7440ζ(5) + 744ζ(2)ζ(3)

=

k=1

−4185ζ(6) + 1800ζ(3)2 + 9702ζ(7) + 1344ζ(2)ζ(5) − 8568ζ(3)ζ(4) + 3570ζ(8)

+720ζ(2)ζ(3)2 − 3456ζ(3)ζ(5) − 1584M(2,6) + 8336ζ(9) − 4656ζ(3)ζ(6) −4896ζ(4)ζ(5) + 1152ζ(2)ζ(7) + 768ζ(3)3 (916)

∞

H(k)3 k5(k + 1)2(k + 2)

1 384

(12 + 24ζ(2) + 48ζ(3) + 15480ζ(4) − 14640ζ(5)

=

k=1

−1560ζ(2)ζ(3) + 4743ζ(6) − 2040ζ(3)2 − 6930ζ(7) − 960ζ(2)ζ(5)

+6120ζ(3)ζ(4) − 1190ζ(8) − 240ζ(2)ζ(3)2 + 1152ζ(3)ζ(5) + 528M(2,6)

(917)

∞

H(k)3 k4(k + 1)3(k + 2)

1 64

(4 + 8ζ(2) + 16ζ(3) − 4440ζ(4) + 3920ζ(5) + 440ζ(2)ζ(3)

=

k=1

−783ζ(6) + 408ζ(3)2 + 462ζ(7) + 64ζ(2)ζ(5) − 408ζ(3)ζ(4) (918) ∞

H(k)3 k3(k + 1)4(k + 2)

1 32

(4 + 8ζ(2) + 16ζ(3) + 1960ζ(4) − 1680ζ(5) − 200ζ(2)ζ(3)

=

k=1

+225ζ(6) − 168ζ(3)2 − 238ζ(7) − 64ζ(2)ζ(5) + 264ζ(3)ζ(4) (919) ∞

H(k)3 k2(k + 1)5(k + 2)

1 96

(24 + 48ζ(2) + 96ζ(3) − 2640ζ(4) + 1920ζ(5)

=

k=1

+240ζ(2)ζ(3) − 396ζ(6) + 384ζ(3)2 + 714ζ(7) + 192ζ(2)ζ(5) − 792ζ(3)ζ(4) −43ζ(8) − 120ζ(2)ζ(3)2 + 288ζ(3)ζ(5) − 24M(2,6) (920)

(24 + 48ζ(2) + 96ζ(3) + 240ζ(4) − 360ζ(5) − 48ζ(2)ζ(3)

=

k(k + 1)6(k + 2)

48

k=1

−357ζ(7) − 96ζ(2)ζ(5) + 396ζ(3)ζ(4) − 394ζ(9) + 222ζ(3)ζ(6)

+396ζ(4)ζ(5) − 144ζ(2)ζ(7) − 48ζ(3)3 (921) ∞

H(k)3 (k + 1)7(k + 2)

1 480

(480 + 960ζ(2) + 1920ζ(3) − 3600ζ(5) − 480ζ(2)ζ(3) − 990ζ(6)

=

k=1

+960ζ(3)2 − 3570ζ(7) − 960ζ(2)ζ(5) + 3960ζ(3)ζ(4) − 215ζ(8) −600ζ(2)ζ(3)2 + 1440ζ(3)ζ(5) − 120M(2,6) − 3940ζ(9) + 2220ζ(3)ζ(6)

+3960ζ(4)ζ(5) − 1440ζ(2)ζ(7) − 480ζ(3)3 − 1503ζ(10) + 2400ζ(3)ζ(7)

+240ζ(3)2ζ(4) − 1680ζ(2)ζ(3)ζ(5) + 1440ζ(5)2 + 120M(2,8) (922) ∞

H(k)3 k6(k + 2)2

1 768

(−84 − 108ζ(2) − 156ζ(3) − 261ζ(4) + 690ζ(5) + 72ζ(2)ζ(3)

=

k=1

−558ζ(6) + 240ζ(3)2 + 2079ζ(7) + 288ζ(2)ζ(5) − 1836ζ(3)ζ(4) + 1190ζ(8)

+240ζ(2)ζ(3)2 − 1152ζ(3)ζ(5) − 528M(2,6) + 4168ζ(9) − 2328ζ(3)ζ(6) −2448ζ(4)ζ(5) + 576ζ(2)ζ(7) + 384ζ(3)3 (923)

∞

H(k)3 k5(k + 1)(k + 2)2

1 768

(−180 − 240ζ(2) − 360ζ(3) + 7038ζ(4) − 6060ζ(5)

=

k=1

−600ζ(2)ζ(3) + 3069ζ(6) − 1320ζ(3)2 − 5544ζ(7) − 768ζ(2)ζ(5)

+4896ζ(3)ζ(4) − 1190ζ(8) − 240ζ(2)ζ(3)2 + 1152ζ(3)ζ(5) + 528M(2,6)

(924)

∞

H(k)3 k4(k + 1)2(k + 2)2

1 64

(−32 − 44ζ(2) − 68ζ(3) − 1407ζ(4) + 1430ζ(5)

=

k=1

+160ζ(2)ζ(3) − 279ζ(6) + 120ζ(3)2 + 231ζ(7) + 32ζ(2)ζ(5) −204ζ(3)ζ(4)) (925)

∞

H(k)3 k3(k + 1)3(k + 2)2

1 64

(68 + 96ζ(2) + 152ζ(3) − 1626ζ(4) + 1060ζ(5)

=

k=1

+120ζ(2)ζ(3) − 225ζ(6) + 168ζ(3)2 (926) ∞

H(k)3 k2(k + 1)4(k + 2)2

1 16

(36 + 52ζ(2) + 84ζ(3) + 167ζ(4) − 310ζ(5)

=

k=1

−40ζ(2)ζ(3) − 119ζ(7) − 32ζ(2)ζ(5) + 132ζ(3)ζ(4)) (927)

∞

H(k)3 k(k + 1)5(k + 2)2

1 96

(456 + 672ζ(2) + 1104ζ(3) − 636ζ(4) − 1800ζ(5)

=

k=1

−240ζ(2)ζ(3) − 396ζ(6) + 384ζ(3)2 − 714ζ(7) − 192ζ(2)ζ(5) + 792ζ(3)ζ(4) −43ζ(8) − 120ζ(2)ζ(3)2 + 288ζ(3)ζ(5) − 24M(2,6) (928)

(480 + 720ζ(2) + 1200ζ(3) − 396ζ(4) − 2160ζ(5)

=

(k + 1)6(k + 2)2

48

k=1

−288ζ(2)ζ(3) − 396ζ(6) + 384ζ(3)2 − 1071ζ(7) − 288ζ(2)ζ(5)

+1188ζ(3)ζ(4) − 43ζ(8) − 120ζ(2)ζ(3)2 + 288ζ(3)ζ(5) − 24M(2,6) − 394ζ(9)

+222ζ(3)ζ(6) + 396ζ(4)ζ(5) − 144ζ(2)ζ(7) − 48ζ(3)3 (929) ∞

H(k)3 k5(k + 2)3

1 1536

(1140 + 864ζ(2) + 696ζ(3) + 378ζ(4) − 3084ζ(5) − 504ζ(2)ζ(3)

=

k=1

+1773ζ(6) − 816ζ(3)2 − 4158ζ(7) − 576ζ(2)ζ(5) + 3672ζ(3)ζ(4) − 1190ζ(8) −240ζ(2)ζ(3)2 + 1152ζ(3)ζ(5) + 528M(2,6) (930)

∞

H(k)3 k4(k + 1)(k + 2)3

1 128

(220 + 184ζ(2) + 176ζ(3) − 1110ζ(4) + 496ζ(5)

=

k=1

+16ζ(2)ζ(3) − 216ζ(6) + 84ζ(3)2 + 231ζ(7) + 32ζ(2)ζ(5) −204ζ(3)ζ(4)) (931)

∞

H(k)3 k3(k + 1)2(k + 2)3

1 64

(252 + 228ζ(2) + 244ζ(3) + 297ζ(4) − 934ζ(5)

=

k=1

−144ζ(2)ζ(3) + 63ζ(6) − 36ζ(3)2 (932) ∞

H(k)3 k2(k + 1)3(k + 2)3

1 64

(572 + 552ζ(2) + 640ζ(3) − 1032ζ(4) − 808ζ(5)

=

k=1

−168ζ(2)ζ(3) − 99ζ(6) + 96ζ(3)2 (933) ∞

H(k)3 k(k + 1)4(k + 2)3

1 32

(644 + 656ζ(2) + 808ζ(3) − 698ζ(4) − 1428ζ(5)

=

k=1

−248ζ(2)ζ(3) − 99ζ(6) + 96ζ(3)2 − 238ζ(7) − 64ζ(2)ζ(5)

+264ζ(3)ζ(4)) (934)

∞

H(k)3 (k + 1)5(k + 2)3

1 96

(4320 + 4608ζ(2) + 5952ζ(3) − 4824ζ(4) − 10368ζ(5)

=

k=1

−1728ζ(2)ζ(3) − 990ζ(6) + 960ζ(3)2 − 2142ζ(7) − 576ζ(2)ζ(5)

+2376ζ(3)ζ(4) − 43ζ(8) − 120ζ(2)ζ(3)2 + 288ζ(3)ζ(5) − 24M(2,6) (935) ∞

H(k)3 k4(k + 2)4

1 128

(420 + 164ζ(2) − 12ζ(3) − 195ζ(4) − 290ζ(5) − 88ζ(2)ζ(3)

=

k=1

+89ζ(6) − 48ζ(3)2 − 175ζ(7) − 32ζ(2)ζ(5) + 168ζ(3)ζ(4) (936) ∞

H(k)3 k3(k + 1)(k + 2)4

1 128

(−1060 − 512ζ(2) − 152ζ(3) + 1500ζ(4) + 84ζ(5)

=

k=1

+160ζ(2)ζ(3) + 38ζ(6) + 12ζ(3)2 + 119ζ(7) + 32ζ(2)ζ(5) −132ζ(3)ζ(4)) (937)

(1312 + 740ζ(2) + 396ζ(3) − 1203ζ(4) − 1018ζ(5)

=

k2(k + 1)2(k + 2)4

64

k=1

−304ζ(2)ζ(3) + 25ζ(6) − 48ζ(3)2 − 119ζ(7) − 32ζ(2)ζ(5)

+132ζ(3)ζ(4)) (938)

∞

H(k)3 k(k + 1)3(k + 2)4

1 64

(3196 + 2032ζ(2) + 1432ζ(3) − 3438ζ(4) − 2844ζ(5)

=

k=1

−776ζ(2)ζ(3) − 49ζ(6) − 238ζ(7) − 64ζ(2)ζ(5) + 264ζ(3)ζ(4)) (939)

∞

H(k)3 (k + 1)4(k + 2)4

1 8

(960 + 672ζ(2) + 560ζ(3) − 1034ζ(4) − 1068ζ(5)

=

k=1

−256ζ(2)ζ(3) − 37ζ(6) + 24ζ(3)2 − 119ζ(7) − 32ζ(2)ζ(5)

+132ζ(3)ζ(4)) (940)

∞

H(k)3 k3(k + 2)5

1 1536

(16500 + 2520ζ(2) − 4896ζ(3) − 8460ζ(4) − 3768ζ(5)

=

k=1

−648ζ(2)ζ(3) − 1779ζ(6) + 1032ζ(3)2 − 1566ζ(7) − 1152ζ(2)ζ(5)

+2664ζ(3)ζ(4) + 86ζ(8) + 240ζ(2)ζ(3)2 − 576ζ(3)ζ(5) + 48M(2,6) (941) ∞

H(k)3 k2(k + 1)(k + 2)5

1 768

(22860 + 5592ζ(2) − 3984ζ(3) − 17460ζ(4) − 4272ζ(5)

=

k=1

−1608ζ(2)ζ(3) − 2007ζ(6) + 960ζ(3)2 − 2280ζ(7) − 1344ζ(2)ζ(5)

+3456ζ(3)ζ(4) + 86ζ(8) + 240ζ(2)ζ(3)2 − 576ζ(3)ζ(5) + 48M(2,6) (942) ∞

H(k)3 k(k + 1)2(k + 2)5

1 384

(30732 + 10032ζ(2) − 1608ζ(3) − 24678ζ(4) − 10380ζ(5)

=

k=1

−3432ζ(2)ζ(3) − 1857ζ(6) + 672ζ(3)2 − 2994ζ(7) − 1536ζ(2)ζ(5)

+4248ζ(3)ζ(4) + 86ζ(8) + 240ζ(2)ζ(3)2 − 576ζ(3)ζ(5) + 48M(2,6) (943) ∞

H(k)3 (k + 1)3(k + 2)5

1 96

(20160 + 8064ζ(2) + 1344ζ(3) − 17496ζ(4) − 9456ζ(5)

=

k=1

−2880ζ(2)ζ(3) − 1002ζ(6) + 336ζ(3)2 − 1854ζ(7) − 864ζ(2)ζ(5)

+2520ζ(3)ζ(4) + 43ζ(8) + 120ζ(2)ζ(3)2 − 288ζ(3)ζ(5) + 24M(2,6) (944) ∞

H(k)3 k2(k + 2)6

1 768

(21588 + 252ζ(2) − 7956ζ(3) − 8451ζ(4) − 5154ζ(5)

=

k=1

+1368ζ(2)ζ(3) − 3732ζ(6) + 2256ζ(3)2 − 1647ζ(7) − 864ζ(2)ζ(5)

+2340ζ(3)ζ(4) + 2102ζ(8) + 240ζ(2)ζ(3)2 − 1728ζ(3)ζ(5) − 528M(2,6) −1576ζ(9) + 888ζ(3)ζ(6) + 1584ζ(4)ζ(5) − 576ζ(2)ζ(7) − 192ζ(3)3 (945)

∞

H(k)3 k(k + 1)(k + 2)6

1 768

(−66036 − 6096ζ(2) + 19896ζ(3) + 34362ζ(4) + 14580ζ(5)

=

k=1

−1128ζ(2)ζ(3) + 9471ζ(6) − 5472ζ(3)2 + 5574ζ(7) + 3072ζ(2)ζ(5) −8136ζ(3)ζ(4) − 4290ζ(8) − 720ζ(2)ζ(3)2 + 4032ζ(3)ζ(5) + 1008M(2,6)

+3152ζ(9) − 1776ζ(3)ζ(6) − 3168ζ(4)ζ(5) + 1152ζ(2)ζ(7) + 384ζ(3)3 (946) ∞

H(k)3 (k + 1)2(k + 2)6

1 48

(−12096 − 2016ζ(2) + 2688ζ(3) + 7380ζ(4) + 3120ζ(5)

=

k=1

+288ζ(2)ζ(3) + 1416ζ(6) − 768ζ(3)2 + 1071ζ(7) + 576ζ(2)ζ(5) −1548ζ(3)ζ(4) − 547ζ(8) − 120ζ(2)ζ(3)2 + 576ζ(3)ζ(5) + 120M(2,6) + 394ζ(9) −222ζ(3)ζ(6) − 396ζ(4)ζ(5) + 144ζ(2)ζ(7) + 48ζ(3)3 (947)

∞

H(k)3 k(k + 2)7

1 7680

(476220 − 30480ζ(2) − 169320ζ(3) − 138270ζ(4) − 138300ζ(5)

=

k=1

+48120ζ(2)ζ(3) − 82965ζ(6) + 45600ζ(3)2 − 73650ζ(7) + 7680ζ(2)ζ(5)

+42840ζ(3)ζ(4) + 46510ζ(8) + 1200ζ(2)ζ(3)2 − 25920ζ(3)ζ(5) − 17040M(2,6) −17680ζ(9) + 26160ζ(3)ζ(6) + 21600ζ(4)ζ(5) − 17280ζ(2)ζ(7) − 5760ζ(3)3

+12024ζ(10) − 19200ζ(3)ζ(7) − 1920ζ(3)2ζ(4) + 13440ζ(2)ζ(3)ζ(5) −11520ζ(5)2 − 960M(2,8) (948)

∞

H(k)3 (k + 1)(k + 2)7

1 480

(100800 − 33600ζ(3) − 38760ζ(4) − 26400ζ(5) + 6720ζ(2)ζ(3)

=

k=1

−16290ζ(6) + 9120ζ(3)2 − 12690ζ(7) − 960ζ(2)ζ(5) + 10440ζ(3)ζ(4) + 8495ζ(8)

+600ζ(2)ζ(3)2 − 5760ζ(3)ζ(5) − 2760M(2,6) − 4180ζ(9) + 4380ζ(3)ζ(6)

+4680ζ(4)ζ(5) − 2880ζ(2)ζ(7) − 960ζ(3)3 + 1503ζ(10) − 2400ζ(3)ζ(7) −240ζ(3)2ζ(4) + 1680ζ(2)ζ(3)ζ(5) − 1440ζ(5)2 − 120M(2,8) (949)

∞

H(k)3 (k + 2)8

1 8

(960 − 96ζ(2) − 304ζ(3) − 222ζ(4) − 284ζ(5) + 96ζ(2)ζ(3)

=

k=1

−157ζ(6) + 72ζ(3)2 − 216ζ(7) + 48ζ(2)ζ(5) + 84ζ(3)ζ(4) + 16ζ(8) − 24M(2,6) −100ζ(9) + 60ζ(3)ζ(6) + 36ζ(4)ζ(5) − 8ζ(3)3 + 108ζ(10) − 48ζ(3)ζ(7) −24ζ(5)2 − 24M(2,8) + 176ζ(11) − 84ζ(3)ζ(8) − 36ζ(4)ζ(7) − 60ζ(5)ζ(6)

+24ζ(3)2ζ(5) − 8M(3,8) (950) ∞

H(k)4 k7

1 48

(−2877ζ(11) − 272ζ(2)ζ(9) + 1190ζ(3)ζ(8) + 1212ζ(4)ζ(7)

=

k=1

+1018ζ(5)ζ(6) + 80ζ(2)ζ(3)3 − 576ζ(3)2ζ(5) + 176M(3,8) (951)

1 5760

172800ζ(5) + 34560ζ(2)ζ(3) − 234960ζ(6) − 17280ζ(3)2

=

k6(k + 1)

k=1

+133200ζ(7) + 28800ζ(2)ζ(5) − 123840ζ(3)ζ(4) + 593320ζ(8)

+161280ζ(2)ζ(3)2 − 668160ζ(3)ζ(5) − 149760M(2,6) + 209280ζ(9) −133920ζ(3)ζ(6) − 123840ζ(4)ζ(5) + 40320ζ(2)ζ(7) + 19200ζ(3)3

+619407ζ(10) − 540000ζ(3)ζ(7) − 9000ζ(3)2ζ(4) + 195120ζ(2)ζ(3)ζ(5) −212040ζ(5)2 − 109080M(2,8) − 11520ζ(2)M(2,6) (952)

∞

H(k)4 k5(k + 1)2

1 72

10800ζ(5) + 2160ζ(2)ζ(3) − 14325ζ(6) − 1080ζ(3)2 + 4995ζ(7)

=

k=1

+1080ζ(2)ζ(5) − 4644ζ(3)ζ(4) + 14833ζ(8) + 4032ζ(2)ζ(3)2 −16704ζ(3)ζ(5) − 3744M(2,6) + 2616ζ(9) − 1674ζ(3)ζ(6) − 1548ζ(4)ζ(5)

+504ζ(2)ζ(7) + 240ζ(3)3 (953) ∞

H(k)4 k4(k + 1)3

1 144

43200ζ(5) + 8640ζ(2)ζ(3) − 55860ζ(6) − 4320ζ(3)2

=

k=1

+11952ζ(7) + 2880ζ(2)ζ(5) − 11952ζ(3)ζ(4) + 14833ζ(8) + 4032ζ(2)ζ(3)2 −16704ζ(3)ζ(5) − 3744M(2,6)) (954)

∞

H(k)4 k3(k + 1)4

1 144

43200ζ(5) + 8640ζ(2)ζ(3) − 54420ζ(6) − 4320ζ(3)2

=

k=1

+9216ζ(7) + 2880ζ(2)ζ(5) − 11088ζ(3)ζ(4) + 12415ζ(8) + 3312ζ(2)ζ(3)2 −13824ζ(3)ζ(5) − 3024M(2,6)) (955)

∞

H(k)4 k2(k + 1)5

1 72

10800ζ(5) + 2160ζ(2)ζ(3) − 13245ζ(6) − 1080ζ(3)2 + 2943ζ(7)

=

k=1

+1080ζ(2)ζ(5) − 3996ζ(3)ζ(4) + 12415ζ(8) + 3312ζ(2)ζ(3)2 −13824ζ(3)ζ(5) − 3024M(2,6) + 1044ζ(9) − 594ζ(3)ζ(6) − 1332ζ(4)ζ(5)

+504ζ(2)ζ(7) + 192ζ(3)3 (956) ∞

H(k)4 k(k + 1)6

1 5760

172800ζ(5) + 34560ζ(2)ζ(3) − 206160ζ(6) − 17280ζ(3)2

=

k=1

+78480ζ(7) + 28800ζ(2)ζ(5) − 106560ζ(3)ζ(4) + 496600ζ(8) + 132480ζ(2)ζ(3)2 −552960ζ(3)ζ(5) − 120960M(2,6) + 83520ζ(9) − 47520ζ(3)ζ(6) − 106560ζ(4)ζ(5)

+40320ζ(2)ζ(7) + 15360ζ(3)3 + 437823ζ(10) − 378720ζ(3)ζ(7)

+2520ζ(3)2ζ(4) + 114480ζ(2)ζ(3)ζ(5) − 119880ζ(5)2 − 68760M(2,8) −11520ζ(2)M(2,6)) (957)

1 48

(237ζ(11) + 368ζ(2)ζ(9) − 86ζ(3)ζ(8) − 684ζ(4)ζ(7)

=

(k + 1)7

k=1

−202ζ(5)ζ(6) − 80ζ(2)ζ(3)3 + 288ζ(3)2ζ(5) + 16M(3,8) (958) ∞

H(k)4 k6(k + 2)

1 11520

=

(180 + 540ζ(2) + 1980ζ(3) + 3330ζ(4) + 5400ζ(5) + 1080ζ(2)ζ(3)

k=1

−14685ζ(6) − 1080ζ(3)2 + 16650ζ(7) + 3600ζ(2)ζ(5) − 15480ζ(3)ζ(4)

+148330ζ(8) + 40320ζ(2)ζ(3)2 − 167040ζ(3)ζ(5) − 37440M(2,6) + 104640ζ(9) −66960ζ(3)ζ(6) − 61920ζ(4)ζ(5) + 20160ζ(2)ζ(7) + 9600ζ(3)3 + 619407ζ(10) −540000ζ(3)ζ(7) − 9000ζ(3)2ζ(4) + 195120ζ(2)ζ(3)ζ(5) − 212040ζ(5)2 −109080M(2,8) − 11520ζ(2)M(2,6)) (959)

∞

H(k)4 k5(k + 1)(k + 2)

1 384

(12 + 36ζ(2) + 132ζ(3) + 222ζ(4) − 11160ζ(5) − 2232ζ(2)ζ(3)

=

k=1

+14685ζ(6) + 1080ζ(3)2 − 7770ζ(7) − 1680ζ(2)ζ(5) + 7224ζ(3)ζ(4) − 29666ζ(8) −8064ζ(2)ζ(3)2 + 33408ζ(3)ζ(5) + 7488M(2,6) − 6976ζ(9) + 4464ζ(3)ζ(6)

+4128ζ(4)ζ(5) − 1344ζ(2)ζ(7) − 640ζ(3)3 (960) ∞

H(k)4 k4(k + 1)2(k + 2)

1 576

(−36 − 108ζ(2) − 396ζ(3) − 666ζ(4) − 52920ζ(5)

=

k=1

−10584ζ(2)ζ(3) + 70545ζ(6) + 5400ζ(3)2 − 16650ζ(7) − 3600ζ(2)ζ(5)

+15480ζ(3)ζ(4) − 29666ζ(8) − 8064ζ(2)ζ(3)2 + 33408ζ(3)ζ(5)

+7488M(2,6)) (961)

∞

H(k)4 k3(k + 1)3(k + 2)

1 32

(−4 − 12ζ(2) − 44ζ(3) − 74ζ(4) + 3720ζ(5) + 744ζ(2)ζ(3)

=

k=1

−4575ζ(6) − 360ζ(3)2 + 806ζ(7) + 240ζ(2)ζ(5) − 936ζ(3)ζ(4) (962) ∞

H(k)4 k2(k + 1)4(k + 2)

1 144

=

(36 + 108ζ(2) + 396ζ(3) + 666ζ(4) + 9720ζ(5)

k=1

+1944ζ(2)ζ(3) − 13245ζ(6) − 1080ζ(3)2 + 1962ζ(7) + 720ζ(2)ζ(5) −2664ζ(3)ζ(4) + 12415ζ(8) + 3312ζ(2)ζ(3)2 − 13824ζ(3)ζ(5) −3024M(2,6)) (963)

∞

H(k)4 k(k + 1)5(k + 2)

1 24

(12 + 36ζ(2) + 132ζ(3) + 222ζ(4) − 360ζ(5) − 72ζ(2)ζ(3)

=

k=1

−327ζ(7) − 120ζ(2)ζ(5) + 444ζ(3)ζ(4) − 348ζ(9) + 198ζ(3)ζ(6)

+444ζ(4)ζ(5) − 168ζ(2)ζ(7) − 64ζ(3)3 (964)

1 5760

(5760 + 17280ζ(2) + 63360ζ(3) + 106560ζ(4) − 206160ζ(6)

=

(k + 1)6(k + 2)

k=1

−17280ζ(3)2 − 78480ζ(7) − 28800ζ(2)ζ(5) + 106560ζ(3)ζ(4) + 496600ζ(8)

+132480ζ(2)ζ(3)2 − 552960ζ(3)ζ(5) − 120960M(2,6) − 83520ζ(9) + 47520ζ(3)ζ(6)

+106560ζ(4)ζ(5) − 40320ζ(2)ζ(7) − 15360ζ(3)3 + 437823ζ(10) −378720ζ(3)ζ(7) + 2520ζ(3)2ζ(4) + 114480ζ(2)ζ(3)ζ(5) − 119880ζ(5)2 −68760M(2,8) − 11520ζ(2)M(2,6)) (965)

∞

H(k)4 k5(k + 2)2

1 2304

=

(540 + 1116ζ(2) + 3276ζ(3) + 3474ζ(4) + 3240ζ(5)

k=1

+792ζ(2)ζ(3) − 14325ζ(6) − 1080ζ(3)2 + 9990ζ(7) + 2160ζ(2)ζ(5) −9288ζ(3)ζ(4) + 59332ζ(8) + 16128ζ(2)ζ(3)2 − 66816ζ(3)ζ(5) − 14976M(2,6)

+20928ζ(9) − 13392ζ(3)ζ(6) − 12384ζ(4)ζ(5) + 4032ζ(2)ζ(7)

+1920ζ(3)3 (966) ∞

H(k)4 k4(k + 1)(k + 2)2

1 576

(288 + 612ζ(2) + 1836ζ(3) + 2070ζ(4) − 15120ζ(5)

=

k=1

−2952ζ(2)ζ(3) + 14865ζ(6) + 1080ζ(3)2 − 6660ζ(7) − 1440ζ(2)ζ(5)

+6192ζ(3)ζ(4) − 14833ζ(8) − 4032ζ(2)ζ(3)2 + 16704ζ(3)ζ(5)

+3744M(2,6)) (967)

∞

H(k)4 k3(k + 1)2(k + 2)2

1 64

=

(68 + 148ζ(2) + 452ζ(3) + 534ζ(4) + 2520ζ(5)

k=1

+520ζ(2)ζ(3) − 4535ζ(6) − 360ζ(3)2 + 370ζ(7) + 80ζ(2)ζ(5) −344ζ(3)ζ(4)) (968)

∞

H(k)4 k2(k + 1)3(k + 2)2

1 8

(18 + 40ζ(2) + 124ζ(3) + 152ζ(4) − 300ζ(5)

=

k=1

−56ζ(2)ζ(3) + 10ζ(6) − 109ζ(7) − 40ζ(2)ζ(5) + 148ζ(3)ζ(4)) (969)

∞

H(k)4 k(k + 1)4(k + 2)2

1 144

(684 + 1548ζ(2) + 4860ζ(3) + 6138ζ(4) − 1080ζ(5)

=

k=1

−72ζ(2)ζ(3) − 12885ζ(6) − 1080ζ(3)2 − 1962ζ(7) − 720ζ(2)ζ(5)

+2664ζ(3)ζ(4) + 12415ζ(8) + 3312ζ(2)ζ(3)2 − 13824ζ(3)ζ(5) −3024M(2,6)) (970)

∞

H(k)4 (k + 1)5(k + 2)2

1 72

(720 + 1656ζ(2) + 5256ζ(3) + 6804ζ(4) − 2160ζ(5)

=

k=1

−288ζ(2)ζ(3) − 12885ζ(6) − 1080ζ(3)2 − 2943ζ(7) − 1080ζ(2)ζ(5)

+3996ζ(3)ζ(4) + 12415ζ(8) + 3312ζ(2)ζ(3)2 − 13824ζ(3)ζ(5) − 3024M(2,6) −1044ζ(9) + 594ζ(3)ζ(6) + 1332ζ(4)ζ(5) − 504ζ(2)ζ(7) − 192ζ(3)3 (971)

1 1152

(−1980 − 2700ζ(2) − 6012ζ(3) − 2502ζ(4) + 432ζ(5)

=

k4(k + 2)3

k=1

+216ζ(2)ζ(3) + 13371ζ(6) + 1656ζ(3)2 − 5976ζ(7) − 1440ζ(2)ζ(5)

+5976ζ(3)ζ(4) − 14833ζ(8) − 4032ζ(2)ζ(3)2 + 16704ζ(3)ζ(5)

+3744M(2,6)) (972)

∞

H(k)4 k3(k + 1)(k + 2)3

1 32

(−126 − 184ζ(2) − 436ζ(3) − 254ζ(4) + 864ζ(5)

=

k=1

+176ζ(2)ζ(3) − 83ζ(6) + 32ζ(3)2 + 38ζ(7) − 12ζ(3)ζ(4) (973) ∞

H(k)4 k2(k + 1)2(k + 2)3

1 64

(572 + 884ζ(2) + 2196ζ(3) + 1550ζ(4) − 936ζ(5)

=

k=1

−184ζ(2)ζ(3) − 4203ζ(6) − 488ζ(3)2 + 218ζ(7) + 80ζ(2)ζ(5) −296ζ(3)ζ(4)) (974)

∞

H(k)4 k(k + 1)3(k + 2)3

1 32

(−644 − 1044ζ(2) − 2692ζ(3) − 2158ζ(4) + 2136ζ(5)

=

k=1

+408ζ(2)ζ(3) + 4163ζ(6) + 488ζ(3)2 + 218ζ(7) + 80ζ(2)ζ(5) −296ζ(3)ζ(4)) (975)

∞

H(k)4 (k + 1)4(k + 2)3

1 144

(6480 + 10944ζ(2) + 29088ζ(3) + 25560ζ(4) − 20304ζ(5)

=

k=1

−3744ζ(2)ζ(3) − 50352ζ(6) − 5472ζ(3)2 − 3924ζ(7) − 1440ζ(2)ζ(5)

+5328ζ(3)ζ(4) + 12415ζ(8) + 3312ζ(2)ζ(3)2 − 13824ζ(3)ζ(5) −3024M(2,6)) (976)

∞

H(k)4 k3(k + 2)4

1 1152

(9540 + 8172ζ(2) + 12492ζ(3) − 4626ζ(4) − 8496ζ(5)

=

k=1

−3672ζ(2)ζ(3) − 11967ζ(6) − 3096ζ(3)2 + 324ζ(7) + 288ζ(2)ζ(5) −792ζ(3)ζ(4) + 12415ζ(8) + 3312ζ(2)ζ(3)2 − 13824ζ(3)ζ(5) − 3024M(2,6)

(977)

∞

H(k)4 k2(k + 1)(k + 2)4

1 576

(11808 + 11484ζ(2) + 20340ζ(3) − 54ζ(4) − 24048ζ(5)

=

k=1

−6840ζ(2)ζ(3) − 10473ζ(6) − 3672ζ(3)2 − 360ζ(7) + 288ζ(2)ζ(5) −576ζ(3)ζ(4) + 12415ζ(8) + 3312ζ(2)ζ(3)2 − 13824ζ(3)ζ(5) − 3024M(2,6)

(978)

∞

H(k)4 k(k + 1)2(k + 2)4

1 576

(28764 + 30924ζ(2) + 60444ζ(3) + 13842ζ(4) − 56520ζ(5)

=

k=1

−15336ζ(2)ζ(3) − 58773ζ(6) − 11736ζ(3)2 + 1242ζ(7) + 1296ζ(2)ζ(5) −3816ζ(3)ζ(4) + 24830ζ(8) + 6624ζ(2)ζ(3)2 − 27648ζ(3)ζ(5) −6048M(2,6)) (979)

∞

H(k)4 (k + 1)3(k + 2)4

1 144

(17280 + 20160ζ(2) + 42336ζ(3) + 16632ζ(4) − 37872ζ(5)

=

k=1

−9504ζ(2)ζ(3) − 48120ζ(6) − 8064ζ(3)2 − 360ζ(7) + 288ζ(2)ζ(5) −576ζ(3)ζ(4) + 12415ζ(8) + 3312ζ(2)ζ(3)2 − 13824ζ(3)ζ(5) − 3024M(2,6)

(980)

∞

H(k)4 k2(k + 2)5

1 2304

(68580 + 34812ζ(2) + 27900ζ(3) − 56070ζ(4) − 39960ζ(5)

=

k=1

−17064ζ(2)ζ(3) − 17889ζ(6) − 2232ζ(3)2 − 24930ζ(7) − 10512ζ(2)ζ(5)

+31752ζ(3)ζ(4) + 50692ζ(8) + 16128ζ(2)ζ(3)2 − 62208ζ(3)ζ(5) − 11520M(2,6)

+8352ζ(9) − 4752ζ(3)ζ(6) − 10656ζ(4)ζ(5) + 4032ζ(2)ζ(7)

+1536ζ(3)3 (981) ∞

H(k)4 k(k + 1)(k + 2)5

1 384

(30732 + 19260ζ(2) + 22860ζ(3) − 18726ζ(4) − 29352ζ(5)

=

k=1

−10248ζ(2)ζ(3) − 12945ζ(6) − 3192ζ(3)2 − 8550ζ(7) − 3312ζ(2)ζ(5)

+10200ζ(3)ζ(4) + 25174ζ(8) + 7584ζ(2)ζ(3)2 − 29952ζ(3)ζ(5) − 5856M(2,6)

+2784ζ(9) − 1584ζ(3)ζ(6) − 3552ζ(4)ζ(5) + 1344ζ(2)ζ(7) + 512ζ(3)3 (982) ∞

H(k)4 (k + 1)2(k + 2)5

1 72

(15120 + 11088ζ(2) + 16128ζ(3) − 5292ζ(4) − 18072ζ(5)

=

k=1

−5760ζ(2)ζ(3) − 12201ζ(6) − 2664ζ(3)2 − 3051ζ(7) − 1080ζ(2)ζ(5)

+3348ζ(3)ζ(4) + 12544ζ(8) + 3672ζ(2)ζ(3)2 − 14688ζ(3)ζ(5) − 2952M(2,6)

+1044ζ(9) − 594ζ(3)ζ(6) − 1332ζ(4)ζ(5) + 504ζ(2)ζ(7) + 192ζ(3)3 (983) ∞

H(k)4 k(k + 2)6

1 11520

(990540 + 275580ζ(2) − 20340ζ(3) − 706950ζ(4) − 394920ζ(5)

=

k=1

−76680ζ(2)ζ(3) − 216465ζ(6) + 99720ζ(3)2 − 272790ζ(7) − 140400ζ(2)ζ(5)

+385560ζ(3)ζ(4) + 260590ζ(8) + 76320ζ(2)ζ(3)2 − 311040ζ(3)ζ(5) − 56160M(2,6) −147360ζ(9) + 82800ζ(3)ζ(6) + 136800ζ(4)ζ(5) − 48960ζ(2)ζ(7) − 15360ζ(3)3

+437823ζ(10) − 378720ζ(3)ζ(7) + 2520ζ(3)2ζ(4) + 114480ζ(2)ζ(3)ζ(5) −119880ζ(5)2 − 68760M(2,8) − 11520ζ(2)M(2,6) (984)

∞

H(k)4 (k + 1)(k + 2)6

1 5760

(1451520 + 564480ζ(2) + 322560ζ(3) − 987840ζ(4) − 835200ζ(5)

=

k=1

−230400ζ(2)ζ(3) − 410640ζ(6) + 51840ζ(3)2 − 401040ζ(7) − 190080ζ(2)ζ(5)

+538560ζ(3)ζ(4) + 638200ζ(8) + 190080ζ(2)ζ(3)2 − 760320ζ(3)ζ(5) −144000M(2,6) − 105600ζ(9) + 59040ζ(3)ζ(6) + 83520ζ(4)ζ(5) − 28800ζ(2)ζ(7) −7680ζ(3)3 + 437823ζ(10) − 378720ζ(3)ζ(7) + 2520ζ(3)2ζ(4)

+114480ζ(2)ζ(3)ζ(5) − 119880ζ(5)2 − 68760M(2,8) − 11520ζ(2)M(2,6)

(985)

H(k)4 (k + 2)7

1 240

(−50400 − 6720ζ(2) + 10080ζ(3) + 27720ζ(4) + 18000ζ(5)

=

k=1

−1440ζ(2)ζ(3) + 12180ζ(6) − 6720ζ(3)2 + 11700ζ(7) + 3360ζ(2)ζ(5) −12960ζ(3)ζ(4) − 9310ζ(8) − 1200ζ(2)ζ(3)2 + 7680ζ(3)ζ(5) + 2640M(2,6)

+8120ζ(9) − 6600ζ(3)ζ(6) − 8640ζ(4)ζ(5) + 4320ζ(2)ζ(7) + 1440ζ(3)3 −3006ζ(10) + 4800ζ(3)ζ(7) + 480ζ(3)2ζ(4) − 3360ζ(2)ζ(3)ζ(5)

+2880ζ(5)2 + 240M(2,8) − 1185ζ(11) − 1840ζ(2)ζ(9) + 430ζ(3)ζ(8)

+3420ζ(4)ζ(7) + 1010ζ(5)ζ(6) + 400ζ(2)ζ(3)3 − 1440ζ(3)2ζ(5) −80M(3,8)) (986)

∞

H(k)5 k6

1 576

(−781671ζ(11) − 88016ζ(2)ζ(9) + 296660ζ(3)ζ(8) + 411984ζ(4)ζ(7)

=

k=1

+220080ζ(5)ζ(6) + 21120ζ(2)ζ(3)3 − 141120ζ(3)2ζ(5) + 8640ζ(3)M(2,6)

+27840M(3,8)) (987)

∞

H(k)5 k5(k + 1)

1 2304

411264ζ(6) + 51840ζ(3)2 − 295344ζ(7) − 65664ζ(2)ζ(5)

=

k=1

−76032ζ(3)ζ(4) − 542488ζ(8) − 152640ζ(2)ζ(3)2 + 630144ζ(3)ζ(5) + 135360M(2,6) −302144ζ(9) + 469920ζ(3)ζ(6) − 152064ζ(4)ζ(5) − 76320ζ(2)ζ(7) + 11520ζ(3)3 −579897ζ(10) + 519840ζ(3)ζ(7) − 3240ζ(3)2ζ(4) − 185040ζ(2)ζ(3)ζ(5)

+203832ζ(5)2 + 98280M(2,8) + 11520ζ(2)M(2,6) (988) ∞

H(k)5 k4(k + 1)2

1 144

102816ζ(6) + 12960ζ(3)2 − 72072ζ(7) − 16416ζ(2)ζ(5)

=

k=1

−19008ζ(3)ζ(4) − 67811ζ(8) − 19080ζ(2)ζ(3)2 + 78768ζ(3)ζ(5) + 16920M(2,6) −18884ζ(9) + 29370ζ(3)ζ(6) − 9504ζ(4)ζ(5) − 4770ζ(2)ζ(7)

+720ζ(3)3 (989) ∞

H(k)5 k3(k + 1)3

1 72

77112ζ(6) + 9720ζ(3)2 − 52731ζ(7) − 12312ζ(2)ζ(5)

=

k=1

−14256ζ(3)ζ(4) − 33358ζ(8) − 9180ζ(2)ζ(3)2 + 37800ζ(3)ζ(5)

+8100M(2,6)) (990)

∞

H(k)5 k2(k + 1)4

1 144 −102816ζ(6) − 12960ζ(3)2 + 68544ζ(7) + 16416ζ(2)ζ(5)

=

k=1

+19008ζ(3)ζ(4) + 65621ζ(8) + 17640ζ(2)ζ(3)2 − 72432ζ(3)ζ(5) − 15480M(2,6)

+14240ζ(9) − 25770ζ(3)ζ(6) + 9504ζ(4)ζ(5) + 4770ζ(2)ζ(7) −720ζ(3)3 (991)

∞

H(k)5 k(k + 1)5

1 2304

411264ζ(6) + 51840ζ(3)2 − 267120ζ(7) − 65664ζ(2)ζ(5)

=

k=1

−76032ζ(3)ζ(4) − 524968ζ(8) − 141120ζ(2)ζ(3)2 + 579456ζ(3)ζ(5) + 123840M(2,6) −227840ζ(9) + 412320ζ(3)ζ(6) − 152064ζ(4)ζ(5) − 76320ζ(2)ζ(7) + 11520ζ(3)3 −449109ζ(10) + 387360ζ(3)ζ(7) + 9720ζ(3)2ζ(4) − 124560ζ(2)ζ(3)ζ(5)

+122328ζ(5)2 + 68040M(2,8) + 11520ζ(2)M(2,6) (992) ∞

H(k)5 (k + 1)6

1 576

(−667227ζ(11) − 68816ζ(2)ζ(9) + 248300ζ(3)ζ(8)

=

k=1

+350784ζ(4)ζ(7) + 176280ζ(5)ζ(6) + 16320ζ(2)ζ(3)3 − 112320ζ(3)2ζ(5)

+8640ζ(3)M(2,6) + 23040M(3,8)) (993)

∞

H(k)5 k5(k + 2)

1 4608

=

(144 + 576ζ(2) + 3024ζ(3) + 9036ζ(4) + 10224ζ(5) + 2160ζ(2)ζ(3)

k=1

+25704ζ(6) + 3240ζ(3)2 − 36918ζ(7) − 8208ζ(2)ζ(5) − 9504ζ(3)ζ(4) −135622ζ(8) − 38160ζ(2)ζ(3)2 + 157536ζ(3)ζ(5) + 33840M(2,6) − 151072ζ(9)

+234960ζ(3)ζ(6) − 76032ζ(4)ζ(5) − 38160ζ(2)ζ(7) + 5760ζ(3)3 − 579897ζ(10)

+519840ζ(3)ζ(7) − 3240ζ(3)2ζ(4) − 185040ζ(2)ζ(3)ζ(5) + 203832ζ(5)2

+98280M(2,8) + 11520ζ(2)M(2,6)) (994)

∞

H(k)5 k4(k + 1)(k + 2)

1 1152

=

(72 + 288ζ(2) + 1512ζ(3) + 4518ζ(4) + 5112ζ(5)

k=1

+1080ζ(2)ζ(3) − 192780ζ(6) − 24300ζ(3)2 + 129213ζ(7) + 28728ζ(2)ζ(5)

+33264ζ(3)ζ(4) + 203433ζ(8) + 57240ζ(2)ζ(3)2 − 236304ζ(3)ζ(5) − 50760M(2,6)

+75536ζ(9) − 117480ζ(3)ζ(6) + 38016ζ(4)ζ(5) + 19080ζ(2)ζ(7) −2880ζ(3)3 (995)

∞

H(k)5 k3(k + 1)2(k + 2)

1 576

=

(72 + 288ζ(2) + 1512ζ(3) + 4518ζ(4) + 5112ζ(5)

k=1

+1080ζ(2)ζ(3) + 218484ζ(6) + 27540ζ(3)2 − 159075ζ(7) − 36936ζ(2)ζ(5) −42768ζ(3)ζ(4) − 67811ζ(8) − 19080ζ(2)ζ(3)2 + 78768ζ(3)ζ(5)

+16920M(2,6)) (996)

∞

H(k)5 k2(k + 1)3(k + 2)

1 288

=

(72 + 288ζ(2) + 1512ζ(3) + 4518ζ(4) + 5112ζ(5)

k=1

+1080ζ(2)ζ(3) − 89964ζ(6) − 11340ζ(3)2 + 51849ζ(7) + 12312ζ(2)ζ(5)

+14256ζ(3)ζ(4) + 65621ζ(8) + 17640ζ(2)ζ(3)2 − 72432ζ(3)ζ(5) −15480M(2,6)) (997)

1 144

=

(72 + 288ζ(2) + 1512ζ(3) + 4518ζ(4) + 5112ζ(5)

k(k + 1)4(k + 2)

k=1

+1080ζ(2)ζ(3) + 12852ζ(6) + 1620ζ(3)2 − 16695ζ(7) − 4104ζ(2)ζ(5) −4752ζ(3)ζ(4) − 14240ζ(9) + 25770ζ(3)ζ(6) − 9504ζ(4)ζ(5) − 4770ζ(2)ζ(7)

+720ζ(3)3 (998) ∞

H(k)5 (k + 1)5(k + 2)

1 2304

=

(2304 + 9216ζ(2) + 48384ζ(3) + 144576ζ(4) + 163584ζ(5)

k=1

+34560ζ(2)ζ(3) − 267120ζ(7) − 65664ζ(2)ζ(5) − 76032ζ(3)ζ(4) + 524968ζ(8)

+141120ζ(2)ζ(3)2 − 579456ζ(3)ζ(5) − 123840M(2,6) − 227840ζ(9)

+412320ζ(3)ζ(6) − 152064ζ(4)ζ(5) − 76320ζ(2)ζ(7) + 11520ζ(3)3

+449109ζ(10) − 387360ζ(3)ζ(7) − 9720ζ(3)2ζ(4) + 124560ζ(2)ζ(3)ζ(5) −122328ζ(5)2 − 68040M(2,8) − 11520ζ(2)M(2,6) (999)

∞

H(k)5 k4(k + 2)2

1 1152

=

(576 + 1656ζ(2) + 7200ζ(3) + 16092ζ(4) + 9936ζ(5)

k=1

+2520ζ(2)ζ(3) + 12819ζ(6) + 2160ζ(3)2 − 36036ζ(7) − 8208ζ(2)ζ(5) −9504ζ(3)ζ(4) − 67811ζ(8) − 19080ζ(2)ζ(3)2 + 78768ζ(3)ζ(5) + 16920M(2,6) −37768ζ(9) + 58740ζ(3)ζ(6) − 19008ζ(4)ζ(5) − 9540ζ(2)ζ(7)

+1440ζ(3)3 (1000) ∞

H(k)5 k3(k + 1)(k + 2)2

1 1152

(−1224 − 3600ζ(2) − 15912ζ(3) − 36702ζ(4) − 24984ζ(5)

=

k=1

−6120ζ(2)ζ(3) + 167142ζ(6) + 19980ζ(3)2 − 57141ζ(7) − 12312ζ(2)ζ(5) −14256ζ(3)ζ(4) − 67811ζ(8) − 19080ζ(2)ζ(3)2 + 78768ζ(3)ζ(5)

+16920M(2,6)) (1001)

∞

H(k)5 k2(k + 1)2(k + 2)2

1 96

(−216 − 648ζ(2) − 2904ζ(3) − 6870ζ(4) − 5016ζ(5)

=

k=1

−1200ζ(2)ζ(3) − 8557ζ(6) − 1260ζ(3)2 + 16989ζ(7) + 4104ζ(2)ζ(5)

+4752ζ(3)ζ(4)) (1002)

∞

H(k)5 k(k + 1)3(k + 2)2

1 288

(−1368 − 4176ζ(2) − 18936ζ(3) − 45738ζ(4) − 35208ζ(5)

=

k=1

−8280ζ(2)ζ(3) + 38622ζ(6) + 3780ζ(3)2 + 50085ζ(7) + 12312ζ(2)ζ(5)

+14256ζ(3)ζ(4) − 65621ζ(8) − 17640ζ(2)ζ(3)2 + 72432ζ(3)ζ(5)

+15480M(2,6)) (1003)

(1440 + 4464ζ(2) + 20448ζ(3) + 50256ζ(4) + 40320ζ(5)

(k + 1)4(k + 2)2

144

k=1

+9360ζ(2)ζ(3) − 25770ζ(6) − 2160ζ(3)2 − 66780ζ(7) − 16416ζ(2)ζ(5) −19008ζ(3)ζ(4) + 65621ζ(8) + 17640ζ(2)ζ(3)2 − 72432ζ(3)ζ(5) − 15480M(2,6) −14240ζ(9) + 25770ζ(3)ζ(6) − 9504ζ(4)ζ(5) − 4770ζ(2)ζ(7)

+720ζ(3)3 (1004) ∞

H(k)5 k3(k + 2)3

1 1152

=

(4536 + 9144ζ(2) + 32184ζ(3) + 49770ζ(4) + 5256ζ(5)

k=1

+2160ζ(2)ζ(3) − 22899ζ(6) − 3420ζ(3)2 − 42921ζ(7) − 8712ζ(2)ζ(5) −27576ζ(3)ζ(4) − 66716ζ(8) − 18360ζ(2)ζ(3)2 + 75600ζ(3)ζ(5)

+16200M(2,6)) (1005)

∞

H(k)5 k2(k + 1)(k + 2)3

1 1152

(10296 + 21888ζ(2) + 80280ζ(3) + 136242ζ(4) + 35496ζ(5)

=

k=1

+10440ζ(2)ζ(3) − 212940ζ(6) − 26820ζ(3)2 − 28701ζ(7) − 5112ζ(2)ζ(5) −40896ζ(3)ζ(4) − 65621ζ(8) − 17640ζ(2)ζ(3)2 + 72432ζ(3)ζ(5)

+15480M(2,6)) (1006)

∞

H(k)5 k(k + 1)2(k + 2)3

1 576

=

(11592 + 25776ζ(2) + 97704ζ(3) + 177462ζ(4) + 65592ζ(5)

k=1

+17640ζ(2)ζ(3) − 161598ζ(6) − 19260ζ(3)2 − 130635ζ(7) − 29736ζ(2)ζ(5) −69408ζ(3)ζ(4) − 65621ζ(8) − 17640ζ(2)ζ(3)2 + 72432ζ(3)ζ(5)

+15480M(2,6)) (1007)

∞

H(k)5 (k + 1)3(k + 2)3

1 24

=

(1080 + 2496ζ(2) + 9720ζ(3) + 18600ζ(4) + 8400ζ(5)

k=1

+2160ζ(2)ζ(3) − 16685ζ(6) − 1920ζ(3)2 − 15060ζ(7) − 3504ζ(2)ζ(5) −6972ζ(3)ζ(4)) (1008)

∞

H(k)5 k2(k + 2)4

1 1152

(−23616 − 32616ζ(2) − 90432ζ(3) − 83340ζ(4) + 43344ζ(5)

=

k=1

+12600ζ(2)ζ(3) + 102651ζ(6) + 23040ζ(3)2 + 16452ζ(7) − 432ζ(2)ζ(5)

+39024ζ(3)ζ(4) − 58529ζ(8) − 15480ζ(2)ζ(3)2 + 65808ζ(3)ζ(5) + 14760M(2,6)

+28480ζ(9) − 51540ζ(3)ζ(6) + 19008ζ(4)ζ(5) + 9540ζ(2)ζ(7) −1440ζ(3)3 (1009)

∞

H(k)5 k(k + 1)(k + 2)4

1 1152

(57528 + 87120ζ(2) + 261144ζ(3) + 302922ζ(4) − 51192ζ(5)

=

k=1

−14760ζ(2)ζ(3) − 418242ζ(6) − 72900ζ(3)2 − 61605ζ(7) − 4248ζ(2)ζ(5) −118944ζ(3)ζ(4) + 51437ζ(8) + 13320ζ(2)ζ(3)2 − 59184ζ(3)ζ(5) − 14040M(2,6) −56960ζ(9) + 103080ζ(3)ζ(6) − 38016ζ(4)ζ(5) − 19080ζ(2)ζ(7)

+2880ζ(3)3 (1010)

(8640 + 14112ζ(2) + 44856ζ(3) + 60048ζ(4) + 1800ζ(5)

(k + 1)2(k + 2)4

72

k=1

+360ζ(2)ζ(3) − 72480ζ(6) − 11520ζ(3)2 − 24030ζ(7) − 4248ζ(2)ζ(5) −23544ζ(3)ζ(4) − 1773ζ(8) − 540ζ(2)ζ(3)2 + 1656ζ(3)ζ(5) + 180M(2,6) −7120ζ(9) + 12885ζ(3)ζ(6) − 4752ζ(4)ζ(5) − 2385ζ(2)ζ(7) + 360ζ(3)3 (1011)

∞

H(k)5 k(k + 2)5

1 4608

(368784 + 341856ζ(2) + 719568ζ(3) + 238572ζ(4) − 579600ζ(5)

=

k=1

−200880ζ(2)ζ(3) − 678396ζ(6) − 171000ζ(3)2 − 164070ζ(7) − 45648ζ(2)ζ(5)

+104256ζ(3)ζ(4) + 1368878ζ(8) + 390960ζ(2)ζ(3)2 − 1583136ζ(3)ζ(5) −326160M(2,6) + 53120ζ(9) + 111120ζ(3)ζ(6) − 289152ζ(4)ζ(5) + 42480ζ(2)ζ(7)

+36480ζ(3)3 − 449109ζ(10) + 387360ζ(3)ζ(7) + 9720ζ(3)2ζ(4) −124560ζ(2)ζ(3)ζ(5) + 122328ζ(5)2 + 68040M(2,8) + 11520ζ(2)M(2,6)

(1012)

∞

H(k)5 (k + 1)(k + 2)5

1 2304

(483840 + 516096ζ(2) + 1241856ζ(3) + 844416ζ(4) − 681984ζ(5)

=

k=1

−230400ζ(2)ζ(3) − 1514880ζ(6) − 316800ζ(3)2 − 287280ζ(7) − 54144ζ(2)ζ(5) −133632ζ(3)ζ(4) + 1471752ζ(8) + 417600ζ(2)ζ(3)2 − 1701504ζ(3)ζ(5) −354240M(2,6) − 60800ζ(9) + 317280ζ(3)ζ(6) − 365184ζ(4)ζ(5) + 4320ζ(2)ζ(7)

+42240ζ(3)3 − 449109ζ(10) + 387360ζ(3)ζ(7) + 9720ζ(3)2ζ(4) −124560ζ(2)ζ(3)ζ(5) + 122328ζ(5)2 + 68040M(2,8) + 11520ζ(2)M(2,6)

(1013)

∞

H(k)5 (k + 2)6

1 1152

(−290304 − 177408ζ(2) − 266112ζ(3) + 87552ζ(4) + 298368ζ(5)

=

k=1

+97920ζ(2)ζ(3) + 236112ζ(6) + 28800ζ(3)2 + 161280ζ(7) + 69120ζ(2)ζ(5) −201600ζ(3)ζ(4) − 547240ζ(8) − 161280ζ(2)ζ(3)2 + 645120ζ(3)ζ(5)

+126720M(2,6) + 11040ζ(9) − 5760ζ(3)ζ(6) + 11520ζ(4)ζ(5) − 5760ζ(2)ζ(7) −3840ζ(3)3 − 437823ζ(10) + 378720ζ(3)ζ(7) − 2520ζ(3)2ζ(4) −114480ζ(2)ζ(3)ζ(5) + 119880ζ(5)2 + 68760M(2,8) + 11520ζ(2)M(2,6) − 1334454ζ(11) −137632ζ(2)ζ(9) + 496600ζ(3)ζ(8) + 701568ζ(4)ζ(7) + 352560ζ(5)ζ(6)

+32640ζ(2)ζ(3)3 − 224640ζ(3)2ζ(5) + 17280ζ(3)M(2,6) + 46080M(3,8)

(1014)

∞

H(k)6 k5

1 192

(734643ζ(11) + 83472ζ(2)ζ(9) − 271244ζ(3)ζ(8) − 395088ζ(4)ζ(7)

=

k=1

−205424ζ(5)ζ(6) − 19360ζ(2)ζ(3)3 + 130176ζ(3)2ζ(5) − 9120ζ(3)M(2,6) −25600M(3,8)) (1015)

(−247296ζ(7) − 55680ζ(2)ζ(5) − 114048ζ(3)ζ(4) + 280464ζ(8)

=

k4(k + 1)

384

k=1

−15744ζ(2)ζ(3)2 + 187008ζ(3)ζ(5) + 21888M(2,6) − 119584ζ(9) + 209952ζ(3)ζ(6) −96768ζ(4)ζ(5) − 31248ζ(2)ζ(7) + 8704ζ(3)3 − 814101ζ(10) + 529680ζ(3)ζ(7) −253944ζ(3)2ζ(4) − 1200ζ(2)ζ(3)ζ(5) + 365064ζ(5)2 + 103128M(2,8)

+45120ζ(2)M(2,6)) (1016)

∞

H(k)6 k3(k + 1)2

1 24

(46368ζ(7) + 10440ζ(2)ζ(5) + 21384ζ(3)ζ(4) − 52085ζ(8)

=

k=1

+2892ζ(2)ζ(3)2 − 34704ζ(3)ζ(5) − 4044M(2,6) + 7474ζ(9) − 13122ζ(3)ζ(6)

+6048ζ(4)ζ(5) + 1953ζ(2)ζ(7) − 544ζ(3)3 (1017) ∞

H(k)6 k2(k + 1)3

1 24

(46368ζ(7) + 10440ζ(2)ζ(5) + 21384ζ(3)ζ(4) − 51583ζ(8)

=

k=1

+2832ζ(2)ζ(3)2 − 34344ζ(3)ζ(5) − 3984M(2,6) + 6146ζ(9) − 12582ζ(3)ζ(6)

+5832ζ(4)ζ(5) + 1953ζ(2)ζ(7) − 536ζ(3)3 (1018) ∞

H(k)6 k(k + 1)4

1 384

(247296ζ(7) + 55680ζ(2)ζ(5) + 114048ζ(3)ζ(4) − 272432ζ(8)

=

k=1

+14784ζ(2)ζ(3)2 − 181248ζ(3)ζ(5) − 20928M(2,6) + 98336ζ(9) − 201312ζ(3)ζ(6)

+93312ζ(4)ζ(5) + 31248ζ(2)ζ(7) − 8576ζ(3)3 + 779835ζ(10) − 490704ζ(3)ζ(7)

+245544ζ(3)2ζ(4) − 15600ζ(2)ζ(3)ζ(5) − 339864ζ(5)2 − 94728M(2,8) −45120ζ(2)M(2,6)) (1019)

∞

H(k)6 (k + 1)5

1 192

(686799ζ(11) + 74512ζ(2)ζ(9) − 262484ζ(3)ζ(8)

=

k=1

−362208ζ(4)ζ(7) − 182584ζ(5)ζ(6) − 18080ζ(2)ζ(3)3 + 120384ζ(3)2ζ(5) −8160ζ(3)M(2,6) − 23360M(3,8)) (1020)

∞

H(k)6 k4(k + 2)

1 768

=

(48 + 240ζ(2) + 1632ζ(3) + 6852ζ(4) + 13704ζ(5) + 2928ζ(2)ζ(3)

k=1

+25164ζ(6) + 3216ζ(3)2 + 30912ζ(7) + 6960ζ(2)ζ(5) + 14256ζ(3)ζ(4) −70116ζ(8) + 3936ζ(2)ζ(3)2 − 46752ζ(3)ζ(5) − 5472M(2,6) + 59792ζ(9) −104976ζ(3)ζ(6) + 48384ζ(4)ζ(5) + 15624ζ(2)ζ(7) − 4352ζ(3)3 + 814101ζ(10) −529680ζ(3)ζ(7) + 253944ζ(3)2ζ(4) + 1200ζ(2)ζ(3)ζ(5) − 365064ζ(5)2 −103128M(2,8) − 45120ζ(2)M(2,6)) (1021)

∞

H(k)6 k3(k + 1)(k + 2)

1 96

=

(12 + 60ζ(2) + 408ζ(3) + 1713ζ(4) + 3426ζ(5) + 732ζ(2)ζ(3)

k=1

+6291ζ(6) + 804ζ(3)2 − 54096ζ(7) − 12180ζ(2)ζ(5) − 24948ζ(3)ζ(4)

+52587ζ(8) − 2952ζ(2)ζ(3)2 + 35064ζ(3)ζ(5) + 4104M(2,6) − 14948ζ(9)

+26244ζ(3)ζ(6) − 12096ζ(4)ζ(5) − 3906ζ(2)ζ(7) + 1088ζ(3)3 (1022)

1 48

=

(12 + 60ζ(2) + 408ζ(3) + 1713ζ(4) + 3426ζ(5)

k2(k + 1)2(k + 2)

k=1

+732ζ(2)ζ(3) + 6291ζ(6) + 804ζ(3)2 + 38640ζ(7) + 8700ζ(2)ζ(5)

+17820ζ(3)ζ(4) − 51583ζ(8) + 2832ζ(2)ζ(3)2 − 34344ζ(3)ζ(5) −3984M(2,6)) (1023)

∞

H(k)6 k(k + 1)3(k + 2)

1 24

=

(12 + 60ζ(2) + 408ζ(3) + 1713ζ(4) + 3426ζ(5) + 732ζ(2)ζ(3)

k=1

+6291ζ(6) + 804ζ(3)2 − 7728ζ(7) − 1740ζ(2)ζ(5) − 3564ζ(3)ζ(4) − 6146ζ(9)

+12582ζ(3)ζ(6) − 5832ζ(4)ζ(5) − 1953ζ(2)ζ(7) + 536ζ(3)3 (1024) ∞

H(k)6 (k + 1)4(k + 2)

1 384

=

(384 + 1920ζ(2) + 13056ζ(3) + 54816ζ(4) + 109632ζ(5)

k=1

+23424ζ(2)ζ(3) + 201312ζ(6) + 25728ζ(3)2 − 272432ζ(8) + 14784ζ(2)ζ(3)2 −181248ζ(3)ζ(5) − 20928M(2,6) − 98336ζ(9) + 201312ζ(3)ζ(6) − 93312ζ(4)ζ(5) −31248ζ(2)ζ(7) + 8576ζ(3)3 + 779835ζ(10) − 490704ζ(3)ζ(7)

+245544ζ(3)2ζ(4) − 15600ζ(2)ζ(3)ζ(5) − 339864ζ(5)2 − 94728M(2,8) −45120ζ(2)M(2,6)) (1025)

∞

H(k)6 k3(k + 2)2

1 192

=

(204 + 756ζ(2) + 4344ζ(3) + 14427ζ(4) + 20382ζ(5)

k=1

+4644ζ(2)ζ(3) + 18570ζ(6) + 2940ζ(3)2 + 6489ζ(7) + 1116ζ(2)ζ(5)

+5940ζ(3)ζ(4) − 52085ζ(8) + 2892ζ(2)ζ(3)2 − 34704ζ(3)ζ(5) − 4044M(2,6)

+14948ζ(9) − 26244ζ(3)ζ(6) + 12096ζ(4)ζ(5) + 3906ζ(2)ζ(7) −1088ζ(3)3 (1026)

∞

H(k)6 k2(k + 1)(k + 2)2

1 96

=

(216 + 816ζ(2) + 4752ζ(3) + 16140ζ(4) + 23808ζ(5)

k=1

+5376ζ(2)ζ(3) + 24861ζ(6) + 3744ζ(3)2 − 47607ζ(7) − 11064ζ(2)ζ(5) −19008ζ(3)ζ(4) + 502ζ(8) − 60ζ(2)ζ(3)2 + 360ζ(3)ζ(5) + 60M(2,6) (1027)

∞

H(k)6 k(k + 1)2(k + 2)2

1 16

=

(76 + 292ζ(2) + 1720ζ(3) + 5951ζ(4) + 9078ζ(5)

k=1

+2036ζ(2)ζ(3) + 10384ζ(6) + 1516ζ(3)2 − 2989ζ(7) − 788ζ(2)ζ(5) −396ζ(3)ζ(4) − 17027ζ(8) + 924ζ(2)ζ(3)2 − 11328ζ(3)ζ(5) − 1308M(2,6)

(1028)

∞

H(k)6 (k + 1)3(k + 2)2

1 24

=

(240 + 936ζ(2) + 5568ζ(3) + 19566ζ(4) + 30660ζ(5)

k=1

+6840ζ(2)ζ(3) + 37443ζ(6) + 5352ζ(3)2 − 16695ζ(7) − 4104ζ(2)ζ(5) −4752ζ(3)ζ(4) − 51081ζ(8) + 2772ζ(2)ζ(3)2 − 33984ζ(3)ζ(5) − 3924M(2,6) −6146ζ(9) + 12582ζ(3)ζ(6) − 5832ζ(4)ζ(5) − 1953ζ(2)ζ(7) + 536ζ(3)3

(1029)

=

(1716 + 4644ζ(2) + 22296ζ(3) + 56835ζ(4) + 51078ζ(5)

k2(k + 2)3

192

k=1

+12276ζ(2)ζ(3) − 6129ζ(6) + 444ζ(3)2 − 33786ζ(7) − 7596ζ(2)ζ(5) −21636ζ(3)ζ(4) − 117204ζ(8) − 14808ζ(2)ζ(3)2 + 38088ζ(3)ζ(5) + 11496M(2,6)

+12292ζ(9) − 25164ζ(3)ζ(6) + 11664ζ(4)ζ(5) + 3906ζ(2)ζ(7) −1072ζ(3)3 (1030)

∞

H(k)6 k(k + 1)(k + 2)3

1 96

(−1932 − 5460ζ(2) − 27048ζ(3) − 72975ζ(4) − 74886ζ(5)

=

k=1

−17652ζ(2)ζ(3) − 18732ζ(6) − 4188ζ(3)2 + 81393ζ(7) + 18660ζ(2)ζ(5)

+40644ζ(3)ζ(4) + 116702ζ(8) + 14868ζ(2)ζ(3)2 − 38448ζ(3)ζ(5) − 11556M(2,6) −12292ζ(9) + 25164ζ(3)ζ(6) − 11664ζ(4)ζ(5) − 3906ζ(2)ζ(7)

+1072ζ(3)3 (1031) ∞

H(k)6 (k + 1)2(k + 2)3

1 48

=

(2160 + 6336ζ(2) + 32208ζ(3) + 90828ζ(4) + 102120ζ(5)

k=1

+23760ζ(2)ζ(3) + 49884ζ(6) + 8736ζ(3)2 − 90360ζ(7) − 21024ζ(2)ζ(5) −41832ζ(3)ζ(4) − 167783ζ(8) − 12096ζ(2)ζ(3)2 + 4464ζ(3)ζ(5) + 7632M(2,6)

+12292ζ(9) − 25164ζ(3)ζ(6) + 11664ζ(4)ζ(5) + 3906ζ(2)ζ(7) −1072ζ(3)3 (1032)

∞

H(k)6 k(k + 2)4

1 768

=

(38352 + 74928ζ(2) + 297696ζ(3) + 562980ζ(4) + 259368ζ(5)

k=1

+60336ζ(2)ζ(3) − 452160ζ(6) − 73200ζ(3)2 − 297468ζ(7) − 51312ζ(2)ζ(5) −321840ζ(3)ζ(4) − 358960ζ(8) − 75504ζ(2)ζ(3)2 + 270912ζ(3)ζ(5) + 59568M(2,6) −178672ζ(9) + 311664ζ(3)ζ(6) − 105408ζ(4)ζ(5) − 60696ζ(2)ζ(7) + 7232ζ(3)3

+779835ζ(10) − 490704ζ(3)ζ(7) + 245544ζ(3)2ζ(4) − 15600ζ(2)ζ(3)ζ(5) −339864ζ(5)2 − 94728M(2,8) − 45120ζ(2)M(2,6) (1033)

∞

H(k)6 (k + 1)(k + 2)4

1 384

=

(46080 + 96768ζ(2) + 405888ζ(3) + 854880ζ(4) + 558912ζ(5)

k=1

+130944ζ(2)ζ(3) − 377232ζ(6) − 56448ζ(3)2 − 623040ζ(7) − 125952ζ(2)ζ(5) −484416ζ(3)ζ(4) − 825768ζ(8) − 134976ζ(2)ζ(3)2 + 424704ζ(3)ζ(5)

+105792M(2,6) − 129504ζ(9) + 211008ζ(3)ζ(6) − 58752ζ(4)ζ(5) − 45072ζ(2)ζ(7)

+2944ζ(3)3 + 779835ζ(10) − 490704ζ(3)ζ(7) + 245544ζ(3)2ζ(4) −15600ζ(2)ζ(3)ζ(5) − 339864ζ(5)2 − 94728M(2,8) − 45120ζ(2)M(2,6)

(1034)

1 384

(−80640 − 112896ζ(2) − 368256ζ(3) − 494496ζ(4) − 35136ζ(5)

=

(k + 2)5

k=1

+5760ζ(2)ζ(3) + 565536ζ(6) + 111360ζ(3)2 + 197280ζ(7) + 31104ζ(2)ζ(5)

+202752ζ(3)ζ(4) − 471672ζ(8) − 133440ζ(2)ζ(3)2 + 549504ζ(3)ζ(5)

+116160M(2,6) + 144320ζ(9) − 364800ζ(3)ζ(6) + 258624ζ(4)ζ(5) + 36000ζ(2)ζ(7) −26880ζ(3)3 + 449109ζ(10) − 387360ζ(3)ζ(7) − 9720ζ(3)2ζ(4)

+124560ζ(2)ζ(3)ζ(5) − 122328ζ(5)2 − 68040M(2,8) − 11520ζ(2)M(2,6) + 1373598ζ(11)

+149024ζ(2)ζ(9) − 524968ζ(3)ζ(8) − 724416ζ(4)ζ(7) − 365168ζ(5)ζ(6) −36160ζ(2)ζ(3)3 + 240768ζ(3)2ζ(5) − 16320ζ(3)M(2,6) − 46720M(3,8) (1035)

∞

H(k)7 k4

1 1152

=

(16370805ζ(11) + 1684144ζ(2)ζ(9) + 5889744ζ(3)ζ(8)

k=1

−10724760ζ(4)ζ(7) − 10480104ζ(5)ζ(6) + 844032ζ(2)ζ(3)3 −2330496ζ(3)2ζ(5) − 1431360ζ(3)M(2,6) − 630336M(3,8) (1036)

∞

H(k)7 k3(k + 1)

1 23040

153310720ζ(8) + 3870720ζ(2)ζ(3)2 + 35078400ζ(3)ζ(5)

=

k=1

−88429120ζ(9) − 28372800ζ(3)ζ(6) − 45812160ζ(4)ζ(5) − 18933120ζ(2)ζ(7) −1290240ζ(3)3 − 149534919ζ(10) + 92839680ζ(3)ζ(7) − 52912440ζ(3)2ζ(4)

+6345360ζ(2)ζ(3)ζ(5) + 69396840ζ(5)2 + 18196920M(2,8) + 9072000ζ(2)M(2,6)

(1037)

∞

H(k)7 k2(k + 1)2

1 72 −958192ζ(8) − 24192ζ(2)ζ(3)2 − 219240ζ(3)ζ(5) + 545743ζ(9)

=

k=1

+177330ζ(3)ζ(6) + 284436ζ(4)ζ(5) + 118332ζ(2)ζ(7) + 8064ζ(3)3 (1038) ∞

H(k)7 k(k + 1)3

1 23040

153310720ζ(8) + 3870720ζ(2)ζ(3)2 + 35078400ζ(3)ζ(5)

=

k=1

−86208640ζ(9) − 28372800ζ(3)ζ(6) − 45207360ζ(4)ζ(5) − 18933120ζ(2)ζ(7) −1290240ζ(3)3 − 149375151ζ(10) + 89769600ζ(3)ζ(7) − 52206840ζ(3)2ζ(4)

+7514640ζ(2)ζ(3)ζ(5) + 67262760ζ(5)2 + 17612280M(2,8) + 9072000ζ(2)M(2,6)

(1039)

∞

H(k)7 (k + 1)4

1 1152

(16196565ζ(11) + 1630384ζ(2)ζ(9) + 5721072ζ(3)ζ(8)

=

k=1

−10468728ζ(4)ζ(7) − 10317144ζ(5)ζ(6) + 837312ζ(2)ζ(3)3 −2330496ζ(3)2ζ(5) − 1411200ζ(3)M(2,6) − 616896M(3,8) (1040)

∞

H(k)7 k3(k + 2)

1 46080

=

(5760 + 34560ζ(2) + 288000ζ(3) + 1546560ζ(4) + 4340160ζ(5)

k=1

+927360ζ(2)ζ(3) + 14115480ζ(6) + 1834560ζ(3)2 + 12782160ζ(7) + 2923200ζ(2)ζ(5)

+5957280ζ(3)ζ(4) + 38327680ζ(8) + 967680ζ(2)ζ(3)2 + 8769600ζ(3)ζ(5) −44214560ζ(9) − 14186400ζ(3)ζ(6) − 22906080ζ(4)ζ(5) − 9466560ζ(2)ζ(7) −645120ζ(3)3 − 149534919ζ(10) + 92839680ζ(3)ζ(7) − 52912440ζ(3)2ζ(4)

+6345360ζ(2)ζ(3)ζ(5) + 69396840ζ(5)2 + 18196920M(2,8) + 9072000ζ(2)M(2,6) 119 (1041)

∞

H(k)7 k2(k + 1)(k + 2)

k=1

∞

H(k)7 k(k + 1)2(k + 2)

k=1

∞

H(k)7 (k + 1)3(k + 2)

k=1

∞

H(k)7 k2(k + 2)2

k=1

∞

H(k)7 k(k + 1)(k + 2)2

k=1

∞

H(k)7 (k + 1)2(k + 2)2

k=1

1 576

=

(144 + 864ζ(2) + 7200ζ(3) + 38664ζ(4) + 108504ζ(5)

+23184ζ(2)ζ(3) + 352887ζ(6) + 45864ζ(3)2 + 319554ζ(7) + 73080ζ(2)ζ(5)

+148932ζ(3)ζ(4) − 2874576ζ(8) − 72576ζ(2)ζ(3)2 − 657720ζ(3)ζ(5) +1105364ζ(9) + 354660ζ(3)ζ(6) + 572652ζ(4)ζ(5) + 236664ζ(2)ζ(7) +16128ζ(3)3 (1042)

1 288

=

(144 + 864ζ(2) + 7200ζ(3) + 38664ζ(4) + 108504ζ(5)

+23184ζ(2)ζ(3) + 352887ζ(6) + 45864ζ(3)2 + 319554ζ(7) + 73080ζ(2)ζ(5)

+148932ζ(3)ζ(4) + 958192ζ(8) + 24192ζ(2)ζ(3)2 + 219240ζ(3)ζ(5) −1077608ζ(9) − 354660ζ(3)ζ(6) − 565092ζ(4)ζ(5) − 236664ζ(2)ζ(7) −16128ζ(3)3 (1043)

1 23040

=

(23040 + 138240ζ(2) + 1152000ζ(3) + 6186240ζ(4) + 17360640ζ(5)

+3709440ζ(2)ζ(3) + 56461920ζ(6) + 7338240ζ(3)2 + 51128640ζ(7)

+11692800ζ(2)ζ(5) + 23829120ζ(3)ζ(4) − 86208640ζ(9) − 28372800ζ(3)ζ(6) −45207360ζ(4)ζ(5) − 18933120ζ(2)ζ(7) − 1290240ζ(3)3 + 149375151ζ(10) −89769600ζ(3)ζ(7) + 52206840ζ(3)2ζ(4) − 7514640ζ(2)ζ(3)ζ(5) −67262760ζ(5)2 − 17612280M(2,8) − 9072000ζ(2)M(2,6) (1044)

1 576

=

(1296 + 5904ζ(2) + 42192ζ(3) + 185004ζ(4) + 396216ζ(5)

+87696ζ(2)ζ(3) + 878271ζ(6) + 122472ζ(3)2 + 288513ζ(7) + 59976ζ(2)ζ(5)

+198072ζ(3)ζ(4) + 243058ζ(8) + 63000ζ(2)ζ(3)2 − 256536ζ(3)ζ(5) − 54936M(2,6) −1091486ζ(9) − 354660ζ(3)ζ(6) − 568872ζ(4)ζ(5) − 236664ζ(2)ζ(7) −16128ζ(3)3 (1045)

1 576

=

(2736 + 12672ζ(2) + 91584ζ(3) + 408672ζ(4) + 900936ζ(5)

+198576ζ(2)ζ(3) + 2109429ζ(6) + 290808ζ(3)2 + 896580ζ(7) + 193032ζ(2)ζ(5)

+545076ζ(3)ζ(4) − 2388460ζ(8) + 53424ζ(2)ζ(3)2 − 1170792ζ(3)ζ(5) −109872M(2,6) − 1077608ζ(9) − 354660ζ(3)ζ(6) − 565092ζ(4)ζ(5) − 236664ζ(2)ζ(7) −16128ζ(3)3 (1046)

1 144

=

(1440 + 6768ζ(2) + 49392ζ(3) + 223668ζ(4) + 504720ζ(5)

+110880ζ(2)ζ(3) + 1231158ζ(6) + 168336ζ(3)2 + 608067ζ(7) + 133056ζ(2)ζ(5)

+347004ζ(3)ζ(4) − 715134ζ(8) + 38808ζ(2)ζ(3)2 − 475776ζ(3)ζ(5) − 54936M(2,6) −1077608ζ(9) − 354660ζ(3)ζ(6) − 565092ζ(4)ζ(5) − 236664ζ(2)ζ(7) −16128ζ(3)3 (1047)

(927360 + 3179520ζ(2) + 19376640ζ(3) + 68423040ζ(4) + 108054720ζ(5)

k(k + 2)3

46080

k=1

+24635520ζ(2)ζ(3) + 140607960ζ(6) + 21107520ζ(3)2 − 39775680ζ(7) −9979200ζ(2)ζ(5) − 13134240ζ(3)ζ(4) − 243547760ζ(8) − 19353600ζ(2)ζ(3)2

+16269120ζ(3)ζ(5) + 12821760M(2,6) − 1803200ζ(9) − 98737440ζ(3)ζ(6)

+16587360ζ(4)ζ(5) + 3657600ζ(2)ζ(7) − 4247040ζ(3)3 − 149375151ζ(10)

+89769600ζ(3)ζ(7) − 52206840ζ(3)2ζ(4) + 7514640ζ(2)ζ(3)ζ(5)

+67262760ζ(5)2 + 17612280M(2,8) + 9072000ζ(2)M(2,6) (1048) ∞

H(k)7 (k + 1)(k + 2)3

1 23040

=

(1036800 + 3686400ζ(2) + 23040000ζ(3) + 84769920ζ(4)

k=1

+144092160ζ(5) + 32578560ζ(2)ζ(3) + 224985120ζ(6) + 32739840ζ(3)2 − 3912480ζ(7)

−2257920ζ(2)ζ(5) + 8668800ζ(3)ζ(4) − 339086160ζ(8) − 17216640ζ(2)ζ(3)2 −30562560ζ(3)ζ(5) + 8426880M(2,6) − 44907520ζ(9) − 112923840ζ(3)ζ(6) −6016320ζ(4)ζ(5) − 5808960ζ(2)ζ(7) − 4892160ζ(3)3 − 149375151ζ(10)

+89769600ζ(3)ζ(7) − 52206840ζ(3)2ζ(4) + 7514640ζ(2)ζ(3)ζ(5)

+67262760ζ(5)2 + 17612280M(2,8) + 9072000ζ(2)M(2,6) (1049) ∞

H(k)7 (k + 2)4

1 1152

=

(138240 + 354816ζ(2) + 1838592ζ(3) + 5175072ζ(4) + 5821632ζ(5)

k=1

+1338624ζ(2)ζ(3) + 2929008ζ(6) + 443520ζ(3)2 − 4509648ζ(7) − 959616ζ(2)ζ(5) −3108672ζ(3)ζ(4) − 13269200ζ(8) − 1725696ζ(2)ζ(3)2 + 4491648ζ(3)ζ(5)

+1314432M(2,6) − 327264ζ(9) + 101808ζ(3)ζ(6) + 362880ζ(4)ζ(5) − 145152ζ(2)ζ(7) −59136ζ(3)3 + 16376535ζ(10) − 10304784ζ(3)ζ(7) + 5156424ζ(3)2ζ(4) −327600ζ(2)ζ(3)ζ(5) − 7137144ζ(5)2 − 1989288M(2,8) − 947520ζ(2)M(2,6)

+16196565ζ(11) + 1630384ζ(2)ζ(9) + 5721072ζ(3)ζ(8) − 10468728ζ(4)ζ(7) −10317144ζ(5)ζ(6) + 837312ζ(2)ζ(3)3 − 2330496ζ(3)2ζ(5) − 1411200ζ(3)M(2,6) −616896M(3,8)) (1050)

∞

H(k)8 k3

1 72

=

(2824380ζ(11) + 277304ζ(2)ζ(9) + 1926401ζ(3)ζ(8)

k=1

−1998972ζ(4)ζ(7) − 2270310ζ(5)ζ(6) + 243648ζ(2)ζ(3)3 − 803808ζ(3)2ζ(5) −341280ζ(3)M(2,6) − 113760M(3,8)) (1051)

∞

H(k)8 k2(k + 1)

1 480

=

(13336000ζ(9) + 7093200ζ(3)ζ(6) + 6432000ζ(4)ζ(5)

k=1

+2807280ζ(2)ζ(7) + 322560ζ(3)3 − 18741581ζ(10) − 6689520ζ(3)ζ(7)

+524640ζ(3)2ζ(4) − 1452480ζ(2)ζ(3)ζ(5) − 4247040ζ(5)2 − 485280M(2,8) −299520ζ(2)M(2,6)) (1052)

(6668000ζ(9) + 3546600ζ(3)ζ(6) + 3216000ζ(4)ζ(5)

k(k + 1)2

240

k=1

+1403640ζ(2)ζ(7) + 161280ζ(3)3 − 9295879ζ(10) − 3314520ζ(3)ζ(7)

+258540ζ(3)2ζ(4) − 733800ζ(2)ζ(3)ζ(5) − 2098980ζ(5)2 − 238860M(2,8) −149760ζ(2)M(2,6)) (1053)

∞

H(k)8 (k + 1)3

1 72

=

(2839707ζ(11) + 274424ζ(2)ζ(9) + 1906367ζ(3)ζ(8)

k=1

−1976076ζ(4)ζ(7) − 2252940ζ(5)ζ(6) + 242208ζ(2)ζ(3)3 − 798912ζ(3)2ζ(5) −339120ζ(3)M(2,6) − 113040M(3,8)) (1054)

∞

H(k)8 k2(k + 2)

1 2880

=

(720 + 5040ζ(2) + 49680ζ(3) + 324000ζ(4) + 1162800ζ(5)

k=1

+247680ζ(2)ζ(3) + 5303460ζ(6) + 692640ζ(3)2 + 8496540ζ(7) + 1931040ζ(2)ζ(5)

+4042800ζ(3)ζ(4) + 19063670ζ(8) + 483840ζ(2)ζ(3)2 + 4368960ζ(3)ζ(5)

+20004000ζ(9) + 10639800ζ(3)ζ(6) + 9648000ζ(4)ζ(5) + 4210920ζ(2)ζ(7)

+483840ζ(3)3 − 56224743ζ(10) − 20068560ζ(3)ζ(7) + 1573920ζ(3)2ζ(4) −4357440ζ(2)ζ(3)ζ(5) − 12741120ζ(5)2 − 1455840M(2,8) − 898560ζ(2)M(2,6)

(1055)

∞

H(k)8 k(k + 1)(k + 2)

1 144

(−72 − 504ζ(2) − 4968ζ(3) − 32400ζ(4) − 116280ζ(5)

=

k=1

−24768ζ(2)ζ(3) − 530346ζ(6) − 69264ζ(3)2 − 849654ζ(7) − 193104ζ(2)ζ(5) −404280ζ(3)ζ(4) − 1906367ζ(8) − 48384ζ(2)ζ(3)2 − 436896ζ(3)ζ(5)

+2000400ζ(9) + 1063980ζ(3)ζ(6) + 964800ζ(4)ζ(5) + 421092ζ(2)ζ(7)

+48384ζ(3)3 (1056) ∞

H(k)8 (k + 1)2(k + 2)

1 720

=

(720 + 5040ζ(2) + 49680ζ(3) + 324000ζ(4) + 1162800ζ(5)

k=1

+247680ζ(2)ζ(3) + 5303460ζ(6) + 692640ζ(3)2 + 8496540ζ(7) + 1931040ζ(2)ζ(5)

+4042800ζ(3)ζ(4) + 19063670ζ(8) + 483840ζ(2)ζ(3)2 + 4368960ζ(3)ζ(5) −27887637ζ(10) − 9943560ζ(3)ζ(7) + 775620ζ(3)2ζ(4) − 2201400ζ(2)ζ(3)ζ(5) −6296940ζ(5)2 − 716580M(2,8) − 449280ζ(2)M(2,6) (1057)

∞

H(k)8 k(k + 2)2

1 1440

(6840 + 37080ζ(2) + 317160ζ(3) + 1726560ζ(4) + 4930200ζ(5)

=

k=1

+1074240ζ(2)ζ(3) + 16758210ζ(6) + 2273040ζ(3)2 + 16566750ζ(7)

+3678480ζ(2)ζ(5) + 8776440ζ(3)ζ(4) + 14292825ζ(8) + 1501920ζ(2)ζ(3)2 −2962080ζ(3)ζ(5) − 1098720M(2,6) − 11550160ζ(9) − 1773300ζ(3)ζ(6) −6477840ζ(4)ζ(5) − 2627820ζ(2)ζ(7) − 80640ζ(3)3 − 27887637ζ(10) −9943560ζ(3)ζ(7) + 775620ζ(3)2ζ(4) − 2201400ζ(2)ζ(3)ζ(5) − 6296940ζ(5)2 −716580M(2,8) − 449280ζ(2)M(2,6)) (1058)

(7200 + 39600ζ(2) + 342000ζ(3) + 1888560ζ(4) + 5511600ζ(5)

(k + 1)(k + 2)2

720

k=1

+1198080ζ(2)ζ(3) + 19409940ζ(6) + 2619360ζ(3)2 + 20815020ζ(7)

+4644000ζ(2)ζ(5) + 10797840ζ(3)ζ(4) + 23824660ζ(8) + 1743840ζ(2)ζ(3)2 −777600ζ(3)ζ(5) − 1098720M(2,6) − 21552160ζ(9) − 7093200ζ(3)ζ(6) −11301840ζ(4)ζ(5) − 4733280ζ(2)ζ(7) − 322560ζ(3)3 − 27887637ζ(10) −9943560ζ(3)ζ(7) + 775620ζ(3)2ζ(4) − 2201400ζ(2)ζ(3)ζ(5) − 6296940ζ(5)2 −716580M(2,8) − 449280ζ(2)M(2,6)) (1059)

∞

H(k)8 (k + 2)3

1 2880

=

(129600 + 541440ζ(2) + 4008960ζ(3) + 18103680ζ(4) + 40584960ζ(5)

k=1

+9020160ζ(2)ζ(3) + 98753280ζ(6) + 13881600ζ(3)2 + 48610080ζ(7)

+10391040ζ(2)ζ(5) + 28817280ζ(3)ζ(4) − 74914520ζ(8) − 1733760ζ(2)ζ(3)2 −18086400ζ(3)ζ(5) − 120960M(2,6) − 65558080ζ(9) − 70648320ζ(3)ζ(6) −25611840ζ(4)ζ(5) − 12371040ζ(2)ζ(7) − 3091200ζ(3)3 − 149375151ζ(10)

+89769600ζ(3)ζ(7) − 52206840ζ(3)2ζ(4) + 7514640ζ(2)ζ(3)ζ(5)

+67262760ζ(5)2 + 17612280M(2,8) + 9072000ζ(2)M(2,6) − 113588280ζ(11) −10976960ζ(2)ζ(9) − 76254680ζ(3)ζ(8) + 79043040ζ(4)ζ(7) + 90117600ζ(5)ζ(6) −9688320ζ(2)ζ(3)3 + 31956480ζ(3)2ζ(5) + 13564800ζ(3)M(2,6) + 4521600M(3,8)

(1060)

∞

H(k)9 k2

1 64

(7739347ζ(11) + 2048432ζ(2)ζ(9) + 5357920ζ(3)ζ(8)

=

k=1

+8811792ζ(4)ζ(7) + 10526056ζ(5)ζ(6) − 294208ζ(2)ζ(3)3 + 2064192ζ(3)2ζ(5)

+540096ζ(3)M(2,6) + 199936M(3,8)) (1061)

∞

H(k)9 k(k + 1)

1 40

17039209ζ(10) + 3158190ζ(3)ζ(7) + 704820ζ(3)2ζ(4)

=

k=1

+928080ζ(2)ζ(3)ζ(5) + 1767000ζ(5)2 + 37320ζ(2)M(2,6) (1062) ∞

H(k)9 (k + 1)2

1 64

=

(7676163ζ(11) + 2050992ζ(2)ζ(9) + 5357920ζ(3)ζ(8)

k=1

+8776416ζ(4)ζ(7) + 10489496ζ(5)ζ(6) − 292928ζ(2)ζ(3)3 + 2058432ζ(3)2ζ(5)

+538176ζ(3)M(2,6) + 199296M(3,8)) (1063)

∞

H(k)9 k(k + 2)

1 160

=

(80 + 640ζ(2) + 7280ζ(3) + 55780ζ(4) + 243200ζ(5) + 51600ζ(2)ζ(3)

k=1

+1416700ζ(6) + 185160ζ(3)2 + 3186110ζ(7) + 721920ζ(2)ζ(5) + 1525680ζ(3)ζ(4)

+12880535ζ(8) + 365400ζ(2)ζ(3)2 + 2739360ζ(3)ζ(5) − 37320M(2,6) + 9964440ζ(9)

+5312700ζ(3)ζ(6) + 4812120ζ(4)ζ(5) + 2105460ζ(2)ζ(7) + 241760ζ(3)3

+34078418ζ(10) + 6316380ζ(3)ζ(7) + 1409640ζ(3)2ζ(4) + 1856160ζ(2)ζ(3)ζ(5)

+3534000ζ(5)2 + 74640ζ(2)M(2,6) (1064)

(16 + 128ζ(2) + 1456ζ(3) + 11156ζ(4) + 48640ζ(5) + 10320ζ(2)ζ(3)

(k + 1)(k + 2)

16

k=1

+283340ζ(6) + 37032ζ(3)2 + 637222ζ(7) + 144384ζ(2)ζ(5) + 305136ζ(3)ζ(4)

+2576107ζ(8) + 73080ζ(2)ζ(3)2 + 547872ζ(3)ζ(5) − 7464M(2,6) + 1992888ζ(9)

+1062540ζ(3)ζ(6) + 962424ζ(4)ζ(5) + 421092ζ(2)ζ(7) + 48352ζ(3)3 (1065) ∞

H(k)9 (k + 2)2

1 320

(−3200 − 20160ζ(2) − 200960ζ(3) − 1307040ζ(4) − 4662400ζ(5)

=

k=1

−1005120ζ(2)ζ(3) − 21224080ζ(6) − 2841600ζ(3)2 − 33558720ζ(7) −7513920ζ(2)ζ(5) − 16977600ζ(3)ζ(4) − 83974040ζ(8) − 3958080ζ(2)ζ(3)2 −9227520ζ(3)ζ(5) + 1763520M(2,6) + 3246560ζ(9) − 7064400ζ(3)ζ(6) +3355200ζ(4)ζ(5) + 1044720ζ(2)ζ(7) − 321920ζ(3)3 + 111550548ζ(10) +39774240ζ(3)ζ(7) − 3102480ζ(3)2ζ(4) + 8805600ζ(2)ζ(3)ζ(5)

+25187760ζ(5)2 + 2866320M(2,8) + 1797120ζ(2)M(2,6) + 38380815ζ(11)

+10254960ζ(2)ζ(9) + 26789600ζ(3)ζ(8) + 43882080ζ(4)ζ(7) + 52447480ζ(5)ζ(6) −1464640ζ(2)ζ(3)3 + 10292160ζ(3)2ζ(5) + 2690880ζ(3)M(2,6) + 996480M(3,8)

(1066)

##### Formulas for order r = m + n = 12:

∞

1 4

H(k) k11

(13ζ(12) − 4ζ(3)ζ(9) − 4ζ(5)ζ(7)) (1067)

=

k=1

∞

1 4 −4ζ(2) + 8ζ(3) − 5ζ(4) + 12ζ(5) − 4ζ(2)ζ(3) − 7ζ(6) + 2ζ(3)2

H(k) k10(k + 1)

=

k=1

+16ζ(7) − 4ζ(2)ζ(5) − 4ζ(3)ζ(4) − 9ζ(8) + 4ζ(3)ζ(5) + 20ζ(9) −4ζ(3)ζ(6) − 4ζ(4)ζ(5) − 4ζ(2)ζ(7) − 11ζ(10) + 4ζ(3)ζ(7) + 2ζ(5)2

+24ζ(11) − 4ζ(2)ζ(9) − 4ζ(3)ζ(8) − 4ζ(4)ζ(7) − 4ζ(5)ζ(6)) (1068)

∞

H(k) k9(k + 1)2

1 4

(36ζ(2) − 68ζ(3) + 35ζ(4) − 72ζ(5) + 24ζ(2)ζ(3) + 35ζ(6)

=

k=1

−10ζ(3)2 − 64ζ(7) + 16ζ(2)ζ(5) + 16ζ(3)ζ(4) + 27ζ(8) − 12ζ(3)ζ(5) −40ζ(9) + 8ζ(3)ζ(6) + 8ζ(4)ζ(5) + 8ζ(2)ζ(7) + 11ζ(10) − 4ζ(3)ζ(7) −2ζ(5)2 (1069)

∞

1 4

H(k) k8(k + 1)3

(144ζ(2) − 256ζ(3) + 104ζ(4) − 180ζ(5) + 60ζ(2)ζ(3) + 70ζ(6)

=

k=1

−20ζ(3)2 − 96ζ(7) + 24ζ(2)ζ(5) + 24ζ(3)ζ(4) + 27ζ(8) − 12ζ(3)ζ(5) −20ζ(9) + 4ζ(3)ζ(6) + 4ζ(4)ζ(5) + 4ζ(2)ζ(7)) (1070)

∞

H(k) k7(k + 1)4

1 4

(336ζ(2) − 560ζ(3) + 168ζ(4) − 248ζ(5) + 84ζ(2)ζ(3) + 70ζ(6)

=

k=1

−20ζ(3)2 − 64ζ(7) + 16ζ(2)ζ(5) + 16ζ(3)ζ(4) + 9ζ(8) − 4ζ(3)ζ(5) (1071) ∞

H(k) k6(k + 1)5

1 2

(252ζ(2) − 392ζ(3) + 77ζ(4) − 114ζ(5) + 42ζ(2)ζ(3) + 16ζ(6)

=

k=1

−4ζ(3)2 − 8ζ(7) + 2ζ(2)ζ(5) + 2ζ(3)ζ(4) (1072) ∞

H(k) k5(k + 1)6

- 1

- 2


(252ζ(2) − 364ζ(3) + 35ζ(4) − 96ζ(5) + 42ζ(2)ζ(3) − 4ζ(6)

=

k=1

+4ζ(3)2 − 6ζ(7) + 2ζ(2)ζ(5) + 2ζ(3)ζ(4) (1073) ∞

1 4 −336ζ(2) + 448ζ(3) + 172ζ(5) − 84ζ(2)ζ(3) + 30ζ(6) − 20ζ(3)2

H(k) k4(k + 1)7

=

k=1

+48ζ(7) − 16ζ(2)ζ(5) − 16ζ(3)ζ(4) + 5ζ(8) − 4ζ(3)ζ(5)) (1074)

∞

H(k) k3(k + 1)8

1 4

(144ζ(2) − 176ζ(3) − 16ζ(4) − 120ζ(5) + 60ζ(2)ζ(3) − 30ζ(6)

=

k=1

+20ζ(3)2 − 72ζ(7) + 24ζ(2)ζ(5) + 24ζ(3)ζ(4) − 15ζ(8) + 12ζ(3)ζ(5) −16ζ(9) + 4ζ(3)ζ(6) + 4ζ(4)ζ(5) + 4ζ(2)ζ(7)) (1075)

1 4

H(k) k2(k + 1)9

(−36ζ(2) + 40ζ(3) + 7ζ(4) + 48ζ(5) − 24ζ(2)ζ(3) + 15ζ(6)

=

k=1

−10ζ(3)2 + 48ζ(7) − 16ζ(2)ζ(5) − 16ζ(3)ζ(4) + 15ζ(8) − 12ζ(3)ζ(5)

+32ζ(9) − 8ζ(3)ζ(6) − 8ζ(4)ζ(5) − 8ζ(2)ζ(7) + 7ζ(10) − 4ζ(3)ζ(7) −2ζ(5)2 (1076)

∞

1 4

H(k) k(k + 1)10

4ζ(2) − 4ζ(3) − ζ(4) − 8ζ(5) + 4ζ(2)ζ(3) − 3ζ(6) + 2ζ(3)2

=

k=1

−12ζ(7) + 4ζ(2)ζ(5) + 4ζ(3)ζ(4) − 5ζ(8) + 4ζ(3)ζ(5) − 16ζ(9)

+4ζ(3)ζ(6) + 4ζ(4)ζ(5) + 4ζ(2)ζ(7) − 7ζ(10) + 4ζ(3)ζ(7) + 2ζ(5)2 −20ζ(11) + 4ζ(2)ζ(9) + 4ζ(3)ζ(8) + 4ζ(4)ζ(7) + 4ζ(5)ζ(6)) (1077)

∞

H(k) (k + 1)11

1 4

(9ζ(12) − 4ζ(3)ζ(9) − 4ζ(5)ζ(7)) (1078)

=

k=1

∞

H(k)2 k10

= M(2,10) (1079)

k=1

∞

H(k)2 k9(k + 1)

1 24

72ζ(3) − 102ζ(4) + 84ζ(5) − 24ζ(2)ζ(3) − 97ζ(6) + 48ζ(3)2

=

k=1

+144ζ(7) − 24ζ(2)ζ(5) − 60ζ(3)ζ(4) − 24M(2,6) + 220ζ(9) − 84ζ(3)ζ(6) −60ζ(4)ζ(5) − 24ζ(2)ζ(7) + 8ζ(3)3 − 24M(2,8) + 312ζ(11) − 24ζ(2)ζ(9) −108ζ(3)ζ(8) − 60ζ(4)ζ(7) − 84ζ(5)ζ(6) + 24ζ(3)2ζ(5) (1080)

∞

H(k)2 k8(k + 1)2

1 24

(576ζ(3) − 780ζ(4) + 504ζ(5) − 144ζ(2)ζ(3) − 485ζ(6)

=

k=1

+240ζ(3)2 + 576ζ(7) − 96ζ(2)ζ(5) − 240ζ(3)ζ(4) − 72M(2,6) + 440ζ(9) −168ζ(3)ζ(6) − 120ζ(4)ζ(5) − 48ζ(2)ζ(7) + 16ζ(3)3 − 24M(2,8) (1081)

∞

H(k)2 k7(k + 1)3

1 12

(1008ζ(3) − 1302ζ(4) + 648ζ(5) − 192ζ(2)ζ(3) − 485ζ(6)

=

k=1

+240ζ(3)2 + 432ζ(7) − 72ζ(2)ζ(5) − 180ζ(3)ζ(4) − 36M(2,6) + 110ζ(9) −42ζ(3)ζ(6) − 30ζ(4)ζ(5) − 12ζ(2)ζ(7) + 4ζ(3)3 (1082)

∞

H(k)2 k6(k + 1)4

1 24

(4032ζ(3) − 4956ζ(4) + 1896ζ(5) − 624ζ(2)ζ(3) − 1007ζ(6)

=

k=1

+504ζ(3)2 + 576ζ(7) − 96ζ(2)ζ(5) − 240ζ(3)ζ(4) − 24M(2,6) (1083) ∞

H(k)2 k5(k + 1)5

1 12

(2520ζ(3) − 2940ζ(4) + 900ζ(5) − 360ζ(2)ζ(3) − 335ζ(6)

=

k=1

+180ζ(3)2 + 84ζ(7) − 24ζ(2)ζ(5) − 24ζ(3)ζ(4) (1084)

(4032ζ(3) − 4452ζ(4) + 1224ζ(5) − 624ζ(2)ζ(3) − 467ζ(6)

=

k4(k + 1)6

24

k=1

+288ζ(3)2 + 96ζ(7) − 96ζ(2)ζ(5) + 48ζ(3)ζ(4) + 84ζ(8) − 48ζ(3)ζ(5) −24M(2,6)) (1085)

∞

H(k)2 k3(k + 1)7

1 12

(1008ζ(3) − 1050ζ(4) + 312ζ(5) − 192ζ(2)ζ(3) − 185ζ(6)

=

k=1

+120ζ(3)2 + 72ζ(7) − 72ζ(2)ζ(5) + 36ζ(3)ζ(4) + 126ζ(8) − 72ζ(3)ζ(5) −36M(2,6) − 2ζ(9) + 18ζ(3)ζ(6) + 6ζ(4)ζ(5) − 12ζ(2)ζ(7) − 4ζ(3)3 (1086)

∞

H(k)2 k2(k + 1)8

1 24

(576ζ(3) − 564ζ(4) + 216ζ(5) − 144ζ(2)ζ(3) − 185ζ(6)

=

k=1

+120ζ(3)2 + 96ζ(7) − 96ζ(2)ζ(5) + 48ζ(3)ζ(4) + 252ζ(8) − 144ζ(3)ζ(5) −72M(2,6) − 8ζ(9) + 72ζ(3)ζ(6) + 24ζ(4)ζ(5) − 48ζ(2)ζ(7) − 16ζ(3)3

+108ζ(10) − 48ζ(3)ζ(7) − 24ζ(5)2 − 24M(2,8) (1087) ∞

H(k)2 k(k + 1)9

1 24

72ζ(3) − 66ζ(4) + 36ζ(5) − 24ζ(2)ζ(3) − 37ζ(6) + 24ζ(3)2

=

k=1

+24ζ(7) − 24ζ(2)ζ(5) + 12ζ(3)ζ(4) + 84ζ(8) − 48ζ(3)ζ(5) − 24M(2,6) −4ζ(9) + 36ζ(3)ζ(6) + 12ζ(4)ζ(5) − 24ζ(2)ζ(7) − 8ζ(3)3 + 108ζ(10) −48ζ(3)ζ(7) − 24ζ(5)2 − 24M(2,8) − 48ζ(11) − 24ζ(2)ζ(9) + 60ζ(3)ζ(8)

+12ζ(4)ζ(7) + 36ζ(5)ζ(6) − 24ζ(3)2ζ(5) (1088) ∞

H(k)2 (k + 1)10

- 1

- 2


(−11ζ(12) + 4ζ(3)ζ(9) + 4ζ(5)ζ(7) + 2M(2,10)) (1089)

=

k=1

∞

H(k)3 k9

1 22112

(−355355ζ(12) + 221120ζ(3)ζ(9) + 265344ζ(5)ζ(7)

=

k=1

+33168ζ(3)2ζ(6) − 5528ζ(3)4 − 49752ζ(2)ζ(5)2 − 99504ζ(2)ζ(3)ζ(7)

+82920M(2,10)) (1090)

∞

H(k)3 k8(k + 1)

1 480 −4800ζ(4) + 4800ζ(5) + 480ζ(2)ζ(3) − 2790ζ(6) + 1200ζ(3)2

=

k=1

+6930ζ(7) + 960ζ(2)ζ(5) − 6120ζ(3)ζ(4) + 2975ζ(8) + 600ζ(2)ζ(3)2 −2880ζ(3)ζ(5) − 1320M(2,6) + 10420ζ(9) − 5820ζ(3)ζ(6) − 6120ζ(4)ζ(5)

+1440ζ(2)ζ(7) + 960ζ(3)3 + 4983ζ(10) − 3840ζ(3)ζ(7) − 240ζ(3)2ζ(4)

+1680ζ(2)ζ(3)ζ(5) − 2160ζ(5)2 − 1560M(2,8) + 480M(3,8) (1091) ∞

H(k)3 k7(k + 1)2

1 480

(33600ζ(4) − 32400ζ(5) − 3360ζ(2)ζ(3) + 13950ζ(6)

=

k=1

−6000ζ(3)2 − 27720ζ(7) − 3840ζ(2)ζ(5) + 24480ζ(3)ζ(4) − 8925ζ(8) −1800ζ(2)ζ(3)2 + 8640ζ(3)ζ(5) + 3960M(2,6) − 20840ζ(9) + 11640ζ(3)ζ(6)

+12240ζ(4)ζ(5) − 2880ζ(2)ζ(7) − 1920ζ(3)3 − 4983ζ(10) + 3840ζ(3)ζ(7)

+240ζ(3)2ζ(4) − 1680ζ(2)ζ(3)ζ(5) + 2160ζ(5)2 + 1560M(2,8) (1092)

20160ζ(4) − 18720ζ(5) − 2016ζ(2)ζ(3) + 5778ζ(6) − 2592ζ(3)2

=

k6(k + 1)3

96

k=1

−8316ζ(7) − 1152ζ(2)ζ(5) + 7344ζ(3)ζ(4) − 1785ζ(8) − 360ζ(2)ζ(3)2

+1728ζ(3)ζ(5) + 792M(2,6) − 2084ζ(9) + 1164ζ(3)ζ(6) + 1224ζ(4)ζ(5) −288ζ(2)ζ(7) − 192ζ(3)3 (1093)

∞

H(k)3 k5(k + 1)4

1 96

(33600ζ(4) − 30000ζ(5) − 3360ζ(2)ζ(3) + 6570ζ(6)

=

k=1

−3360ζ(3)2 − 6258ζ(7) − 960ζ(2)ζ(5) + 5688ζ(3)ζ(4) − 595ζ(8) −120ζ(2)ζ(3)2 + 576ζ(3)ζ(5) + 264M(2,6) (1094)

∞

H(k)3 k4(k + 1)5

1 96

33600ζ(4) − 28800ζ(5) − 3360ζ(2)ζ(3) + 4770ζ(6) − 3120ζ(3)2

=

k=1

−4242ζ(7) − 960ζ(2)ζ(5) + 4392ζ(3)ζ(4) + 43ζ(8) + 120ζ(2)ζ(3)2 −288ζ(3)ζ(5) + 24M(2,6)) (1095)

∞

H(k)3 k3(k + 1)6

1 96

20160ζ(4) − 16560ζ(5) − 2016ζ(2)ζ(3) + 2538ζ(6) − 2160ζ(3)2

=

k=1

−4284ζ(7) − 1152ζ(2)ζ(5) + 4752ζ(3)ζ(4) + 129ζ(8) + 360ζ(2)ζ(3)2 −864ζ(3)ζ(5) + 72M(2,6) − 788ζ(9) + 444ζ(3)ζ(6) + 792ζ(4)ζ(5) −288ζ(2)ζ(7) − 96ζ(3)3 (1096)

∞

H(k)3 k2(k + 1)7

1 480

(33600ζ(4) − 26400ζ(5) − 3360ζ(2)ζ(3) + 4950ζ(6)

=

k=1

−4800ζ(3)2 − 14280ζ(7) − 3840ζ(2)ζ(5) + 15840ζ(3)ζ(4) + 645ζ(8)

+1800ζ(2)ζ(3)2 − 4320ζ(3)ζ(5) + 360M(2,6) − 7880ζ(9) + 4440ζ(3)ζ(6)

+7920ζ(4)ζ(5) − 2880ζ(2)ζ(7) − 960ζ(3)3 + 1503ζ(10) − 2400ζ(3)ζ(7) −240ζ(3)2ζ(4) + 1680ζ(2)ζ(3)ζ(5) − 1440ζ(5)2 − 120M(2,8) (1097)

∞

H(k)3 k(k + 1)8

1 480

4800ζ(4) − 3600ζ(5) − 480ζ(2)ζ(3) + 990ζ(6) − 960ζ(3)2

=

k=1

−3570ζ(7) − 960ζ(2)ζ(5) + 3960ζ(3)ζ(4) + 215ζ(8) + 600ζ(2)ζ(3)2 −1440ζ(3)ζ(5) + 120M(2,6) − 3940ζ(9) + 2220ζ(3)ζ(6) + 3960ζ(4)ζ(5) −1440ζ(2)ζ(7) − 480ζ(3)3 + 1503ζ(10) − 2400ζ(3)ζ(7) − 240ζ(3)2ζ(4)

+1680ζ(2)ζ(3)ζ(5) − 1440ζ(5)2 − 120M(2,8) + 10560ζ(11) − 5040ζ(3)ζ(8) −2160ζ(4)ζ(7) − 3600ζ(5)ζ(6) + 1440ζ(3)2ζ(5) − 480M(3,8) (1098)

∞

H(k)3 (k + 1)9

1 22112

(161875ζ(12) − 154784ζ(3)ζ(9) − 199008ζ(5)ζ(7)

=

k=1

−33168ζ(3)2ζ(6) + 5528ζ(3)4 + 49752ζ(2)ζ(5)2 + 99504ζ(2)ζ(3)ζ(7) −16584M(2,10)) (1099)

= M(4,8) (1100)

k8

k=1

∞

H(k)4 k7(k + 1)

1 5760

172800ζ(5) + 34560ζ(2)ζ(3) − 234960ζ(6) − 17280ζ(3)2

=

k=1

+133200ζ(7) + 28800ζ(2)ζ(5) − 123840ζ(3)ζ(4) + 593320ζ(8)

+161280ζ(2)ζ(3)2 − 668160ζ(3)ζ(5) − 149760M(2,6) + 209280ζ(9) −133920ζ(3)ζ(6) − 123840ζ(4)ζ(5) + 40320ζ(2)ζ(7) + 19200ζ(3)3

+619407ζ(10) − 540000ζ(3)ζ(7) − 9000ζ(3)2ζ(4) + 195120ζ(2)ζ(3)ζ(5) −212040ζ(5)2 − 109080M(2,8) − 11520ζ(2)M(2,6) − 345240ζ(11) − 32640ζ(2)ζ(9)

+142800ζ(3)ζ(8) + 145440ζ(4)ζ(7) + 122160ζ(5)ζ(6) + 9600ζ(2)ζ(3)3 −69120ζ(3)2ζ(5) + 21120M(3,8) (1101)

∞

H(k)4 k6(k + 1)2

1 1920 −345600ζ(5) − 69120ζ(2)ζ(3) + 460320ζ(6) + 34560ζ(3)2 −177600ζ(7) − 38400ζ(2)ζ(5) + 165120ζ(3)ζ(4) − 593320ζ(8) −161280ζ(2)ζ(3)2 + 668160ζ(3)ζ(5) + 149760M(2,6) − 139520ζ(9) + 89280ζ(3)ζ(6)

=

k=1

+82560ζ(4)ζ(5) − 26880ζ(2)ζ(7) − 12800ζ(3)3 − 206469ζ(10) + 180000ζ(3)ζ(7)

+3000ζ(3)2ζ(4) − 65040ζ(2)ζ(3)ζ(5) + 70680ζ(5)2 + 36360M(2,8)

+3840ζ(2)M(2,6)) (1102)

∞

H(k)4 k5(k + 1)3

1 48

21600ζ(5) + 4320ζ(2)ζ(3) − 28170ζ(6) − 2160ζ(3)2

=

k=1

+7314ζ(7) + 1680ζ(2)ζ(5) − 7080ζ(3)ζ(4) + 14833ζ(8) + 4032ζ(2)ζ(3)2 −16704ζ(3)ζ(5) − 3744M(2,6) + 1744ζ(9) − 1116ζ(3)ζ(6) − 1032ζ(4)ζ(5)

+336ζ(2)ζ(7) + 160ζ(3)3 (1103) ∞

H(k)4 k4(k + 1)4

1 18

10800ζ(5) + 2160ζ(2)ζ(3) − 13785ζ(6) − 1080ζ(3)2 + 2646ζ(7)

=

k=1

+720ζ(2)ζ(5) − 2880ζ(3)ζ(4) + 3406ζ(8) + 918ζ(2)ζ(3)2 − 3816ζ(3)ζ(5) −846M(2,6)) (1104)

∞

H(k)4 k3(k + 1)5

1 48

21600ζ(5) + 4320ζ(2)ζ(3) − 26970ζ(6) − 2160ζ(3)2 + 5034ζ(7)

=

k=1

+1680ζ(2)ζ(5) − 6360ζ(3)ζ(4) + 12415ζ(8) + 3312ζ(2)ζ(3)2 −13824ζ(3)ζ(5) − 3024M(2,6) + 696ζ(9) − 396ζ(3)ζ(6) − 888ζ(4)ζ(5)

+336ζ(2)ζ(7) + 128ζ(3)3 (1105)

345600ζ(5) + 69120ζ(2)ζ(3) − 421920ζ(6) − 34560ζ(3)2

=

k2(k + 1)6

1920

k=1

+104640ζ(7) + 38400ζ(2)ζ(5) − 142080ζ(3)ζ(4) + 496600ζ(8)

+132480ζ(2)ζ(3)2 − 552960ζ(3)ζ(5) − 120960M(2,6) + 55680ζ(9) − 31680ζ(3)ζ(6) −71040ζ(4)ζ(5) + 26880ζ(2)ζ(7) + 10240ζ(3)3 + 145941ζ(10) − 126240ζ(3)ζ(7)

+840ζ(3)2ζ(4) + 38160ζ(2)ζ(3)ζ(5) − 39960ζ(5)2 − 22920M(2,8) −3840ζ(2)M(2,6)) (1106)

∞

H(k)4 k(k + 1)7

1 5760

172800ζ(5) + 34560ζ(2)ζ(3) − 206160ζ(6) − 17280ζ(3)2

=

k=1

+78480ζ(7) + 28800ζ(2)ζ(5) − 106560ζ(3)ζ(4) + 496600ζ(8) + 132480ζ(2)ζ(3)2 −552960ζ(3)ζ(5) − 120960M(2,6) + 83520ζ(9) − 47520ζ(3)ζ(6) − 106560ζ(4)ζ(5)

+40320ζ(2)ζ(7) + 15360ζ(3)3 + 437823ζ(10) − 378720ζ(3)ζ(7)

+2520ζ(3)2ζ(4) + 114480ζ(2)ζ(3)ζ(5) − 119880ζ(5)2 − 68760M(2,8)

−11520ζ(2)M(2,6) + 28440ζ(11) + 44160ζ(2)ζ(9) − 10320ζ(3)ζ(8) −82080ζ(4)ζ(7) − 24240ζ(5)ζ(6) − 9600ζ(2)ζ(3)3 + 34560ζ(3)2ζ(5) +1920M(3,8)) (1107)

∞

H(k)4 (k + 1)8

1 5528

(289019ζ(12) − 199008ζ(3)ζ(9) − 243232ζ(5)ζ(7)

=

k=1

−33168ζ(3)2ζ(6) + 5528ζ(3)4 + 49752ζ(2)ζ(5)2 + 99504ζ(2)ζ(3)ζ(7) −49752M(2,10) + 5528M(4,8)) (1108)

∞

H(k)5 k7

1 265344

(3612841ζ(12) − 884480ζ(3)ζ(9) − 597024ζ(5)ζ(7)

=

k=1

+364848ζ(3)2ζ(6) + 221120ζ(3)4 + 364848ζ(2)ζ(5)2 + 729696ζ(2)ζ(3)ζ(7) −3250464ζ(3)ζ(4)ζ(5) − 1028208M(2,10) + 663360M(4,8)) (1109)

∞

H(k)5 k6(k + 1)

1 2304 −411264ζ(6) − 51840ζ(3)2 + 295344ζ(7) + 65664ζ(2)ζ(5)

=

k=1

+76032ζ(3)ζ(4) + 542488ζ(8) + 152640ζ(2)ζ(3)2 − 630144ζ(3)ζ(5) − 135360M(2,6)

+302144ζ(9) − 469920ζ(3)ζ(6) + 152064ζ(4)ζ(5) + 76320ζ(2)ζ(7) − 11520ζ(3)3

+579897ζ(10) − 519840ζ(3)ζ(7) + 3240ζ(3)2ζ(4) + 185040ζ(2)ζ(3)ζ(5) −203832ζ(5)2 − 98280M(2,8) − 11520ζ(2)M(2,6) − 3126684ζ(11) − 352064ζ(2)ζ(9)

+1186640ζ(3)ζ(8) + 1647936ζ(4)ζ(7) + 880320ζ(5)ζ(6) + 84480ζ(2)ζ(3)3 −564480ζ(3)2ζ(5) + 34560ζ(3)M(2,6) + 111360M(3,8) (1110)

2056320ζ(6) + 259200ζ(3)2 − 1448496ζ(7) − 328320ζ(2)ζ(5)

=

k5(k + 1)2

2304

k=1

−380160ζ(3)ζ(4) − 1627464ζ(8) − 457920ζ(2)ζ(3)2 + 1890432ζ(3)ζ(5)

+406080M(2,6) − 604288ζ(9) + 939840ζ(3)ζ(6) − 304128ζ(4)ζ(5) − 152640ζ(2)ζ(7)

+23040ζ(3)3 − 579897ζ(10) + 519840ζ(3)ζ(7) − 3240ζ(3)2ζ(4) −185040ζ(2)ζ(3)ζ(5) + 203832ζ(5)2 + 98280M(2,8) + 11520ζ(2)M(2,6) (1111)

∞

H(k)5 k4(k + 1)3

1 144

257040ζ(6) + 32400ζ(3)2 − 177534ζ(7) − 41040ζ(2)ζ(5)

=

k=1

−47520ζ(3)ζ(4) − 134527ζ(8) − 37440ζ(2)ζ(3)2 + 154368ζ(3)ζ(5) + 33120M(2,6) −18884ζ(9) + 29370ζ(3)ζ(6) − 9504ζ(4)ζ(5) − 4770ζ(2)ζ(7)

+720ζ(3)3 (1112) ∞

H(k)5 k3(k + 1)4

1 144

257040ζ(6) + 32400ζ(3)2 − 174006ζ(7) − 41040ζ(2)ζ(5)

=

k=1

−47520ζ(3)ζ(4) − 132337ζ(8) − 36000ζ(2)ζ(3)2 + 148032ζ(3)ζ(5) + 31680M(2,6) −14240ζ(9) + 25770ζ(3)ζ(6) − 9504ζ(4)ζ(5) − 4770ζ(2)ζ(7)

+720ζ(3)3 (1113) ∞

H(k)5 k2(k + 1)5

1 2304

2056320ζ(6) + 259200ζ(3)2 − 1363824ζ(7) − 328320ζ(2)ζ(5)

=

k=1

−380160ζ(3)ζ(4) − 1574904ζ(8) − 423360ζ(2)ζ(3)2 + 1738368ζ(3)ζ(5)

+371520M(2,6) − 455680ζ(9) + 824640ζ(3)ζ(6) − 304128ζ(4)ζ(5) − 152640ζ(2)ζ(7)

+23040ζ(3)3 − 449109ζ(10) + 387360ζ(3)ζ(7) + 9720ζ(3)2ζ(4) −124560ζ(2)ζ(3)ζ(5) + 122328ζ(5)2 + 68040M(2,8) + 11520ζ(2)M(2,6) (1114)

∞

H(k)5 k(k + 1)6

1 2304

411264ζ(6) + 51840ζ(3)2 − 267120ζ(7) − 65664ζ(2)ζ(5)

=

k=1

−76032ζ(3)ζ(4) − 524968ζ(8) − 141120ζ(2)ζ(3)2 + 579456ζ(3)ζ(5) + 123840M(2,6) −227840ζ(9) + 412320ζ(3)ζ(6) − 152064ζ(4)ζ(5) − 76320ζ(2)ζ(7) + 11520ζ(3)3 −449109ζ(10) + 387360ζ(3)ζ(7) + 9720ζ(3)2ζ(4) − 124560ζ(2)ζ(3)ζ(5)

+122328ζ(5)2 + 68040M(2,8) + 11520ζ(2)M(2,6) + 2668908ζ(11) + 275264ζ(2)ζ(9) −993200ζ(3)ζ(8) − 1403136ζ(4)ζ(7) − 705120ζ(5)ζ(6) − 65280ζ(2)ζ(3)3

+449280ζ(3)2ζ(5) − 34560ζ(3)M(2,6) − 92160M(3,8) (1115) ∞

H(k)6 k5(k + 1)

1 384

(247296ζ(7) + 55680ζ(2)ζ(5) + 114048ζ(3)ζ(4) − 280464ζ(8)

=

k=1

+15744ζ(2)ζ(3)2 − 187008ζ(3)ζ(5) − 21888M(2,6) + 119584ζ(9) − 209952ζ(3)ζ(6)

+96768ζ(4)ζ(5) + 31248ζ(2)ζ(7) − 8704ζ(3)3 + 814101ζ(10) − 529680ζ(3)ζ(7)

+253944ζ(3)2ζ(4) + 1200ζ(2)ζ(3)ζ(5) − 365064ζ(5)2 − 103128M(2,8)

−45120ζ(2)M(2,6) − 1469286ζ(11) − 166944ζ(2)ζ(9) + 542488ζ(3)ζ(8) +790176ζ(4)ζ(7) + 410848ζ(5)ζ(6) + 38720ζ(2)ζ(3)3 − 260352ζ(3)2ζ(5) +18240ζ(3)M(2,6) + 51200M(3,8)) (1116)

(989184ζ(7) + 222720ζ(2)ζ(5) + 456192ζ(3)ζ(4) − 1113824ζ(8)

=

k4(k + 1)2

384

k=1

+62016ζ(2)ζ(3)2 − 742272ζ(3)ζ(5) − 86592M(2,6) + 239168ζ(9) − 419904ζ(3)ζ(6)

+193536ζ(4)ζ(5) + 62496ζ(2)ζ(7) − 17408ζ(3)3 + 814101ζ(10) −529680ζ(3)ζ(7) + 253944ζ(3)2ζ(4) + 1200ζ(2)ζ(3)ζ(5) − 365064ζ(5)2 −103128M(2,8) − 45120ζ(2)M(2,6)) (1117)

∞

H(k)6 k3(k + 1)3

1 4

(15456ζ(7) + 3480ζ(2)ζ(5) + 7128ζ(3)ζ(4) − 17278ζ(8)

=

k=1

+954ζ(2)ζ(3)2 − 11508ζ(3)ζ(5) − 1338M(2,6) + 2270ζ(9) − 4284ζ(3)ζ(6)

+1980ζ(4)ζ(5) + 651ζ(2)ζ(7) − 180ζ(3)3 (1118) ∞

H(k)6 k2(k + 1)4

1 384

(989184ζ(7) + 222720ζ(2)ζ(5) + 456192ζ(3)ζ(4) − 1097760ζ(8)

=

k=1

+60096ζ(2)ζ(3)2 − 730752ζ(3)ζ(5) − 84672M(2,6) + 196672ζ(9) − 402624ζ(3)ζ(6)

+186624ζ(4)ζ(5) + 62496ζ(2)ζ(7) − 17152ζ(3)3 + 779835ζ(10) −490704ζ(3)ζ(7) + 245544ζ(3)2ζ(4) − 15600ζ(2)ζ(3)ζ(5) − 339864ζ(5)2 −94728M(2,8) − 45120ζ(2)M(2,6)) (1119)

∞

H(k)6 k(k + 1)5

1 384

(247296ζ(7) + 55680ζ(2)ζ(5) + 114048ζ(3)ζ(4) − 272432ζ(8)

=

k=1

+14784ζ(2)ζ(3)2 − 181248ζ(3)ζ(5) − 20928M(2,6) + 98336ζ(9) − 201312ζ(3)ζ(6)

+93312ζ(4)ζ(5) + 31248ζ(2)ζ(7) − 8576ζ(3)3 + 779835ζ(10) − 490704ζ(3)ζ(7)

+245544ζ(3)2ζ(4) − 15600ζ(2)ζ(3)ζ(5) − 339864ζ(5)2 − 94728M(2,8)

−45120ζ(2)M(2,6) − 1373598ζ(11) − 149024ζ(2)ζ(9) + 524968ζ(3)ζ(8) +724416ζ(4)ζ(7) + 365168ζ(5)ζ(6) + 36160ζ(2)ζ(3)3 − 240768ζ(3)2ζ(5) +16320ζ(3)M(2,6) + 46720M(3,8)) (1120)

