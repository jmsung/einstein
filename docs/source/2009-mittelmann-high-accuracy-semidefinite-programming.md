---
type: source
kind: paper
title: High accuracy semidefinite programming bounds for kissing numbers
authors: Hans D. Mittelmann, Frank Vallentin
year: 2009
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/0902.1105v3
source_local: ../raw/2009-mittelmann-high-accuracy-semidefinite-programming.pdf
topic: general-knowledge
cites:
---

arXiv:0902.1105v3[math.OC]26Jun2009

HIGH ACCURACY SEMIDEFINITE PROGRAMMING BOUNDS FOR KISSING NUMBERS

HANS D. MITTELMANN AND FRANK VALLENTIN

Abstract. The kissing number in n-dimensional Euclidean space is the maximal number of non-overlapping unit spheres which simultaneously can touch a central unit sphere. Bachoc and Vallentin developed a method to ﬁnd upper bounds for the kissing number based on semideﬁnite programming. This paper is a report on high accuracy calculations of these upper bounds for n ≤ 24. The bound for n = 16 implies a conjecture of Conway and Sloane: There is no 16-dimensional periodic sphere packing with average theta series

1 + 7680q3 + 4320q4 + 276480q5 + 61440q6 + · · ·

1. Introduction

In geometry, the kissing number in n-dimensional Euclidean space is the maximal number of non-overlapping unit spheres which simultaneously can touch a central unit sphere. The kissing number is only known in dimensions n = 1,2,3,4,8,24, and there were many attempts to ﬁnd good lower and upper bounds. We refer to Casselman [4] for the history of this problem and to Pfender, Ziegler [14], Elkies [7], and Conway, Sloane [6] for more background information on sphere packing problems.

Bachoc and Vallentin [1] develop a method (Section 2 recalls it) to ﬁnd upper bounds for the kissing number based on semideﬁnite programming. Table 1 in Section 3, the main contribution of this paper, gives the values, i.e. the ﬁrst ten signiﬁcant digits, of these upper bounds for all dimensions 3,...,24. In all cases they are the best known upper bounds. Dimension 5 is the ﬁrst dimension in which the kissing number is not known. With our computation we could limit the range of possible values from {40,...,45} to {40,...,44}. In Section 4 we show that the high accuracy computations for the upper bounds in dimension 4 result into a question about a possible approach to prove the uniqueness of the kissing conﬁguration in 4 dimensions.

Although acquiring the data for the table is a purely computational task we think that providing this table is valuable for several reasons: The kissing number is an important constant in geometry and results can depend on good upper bounds for it. For instance in Section 5 we show that there is no periodic point set in dimension

![image 1](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile1.png>)

Date: June 26, 2009. 1991 Mathematics Subject Classiﬁcation. 11F11, 52C17, 90C10. Key words and phrases. kissing number, semideﬁnite programming, average theta series, ex-

tremal modular form.

The second author was partially supported by the Deutsche Forschungsgemeinschaft (DFG) under grant SCHU 1503/4.

1

16 with average theta series 1 + 7680q3 + 4320q4 + 276480q5 + 61440q6 + ···

This proves a conjecture of Conway and Sloane [6, Chapter 7, page 190]. Furthermore, the actual computation of the table was very challenging. Bachoc and Vallentin [1] gave results for dimension 3,...,10. However, they report on numerical diﬃculties which prevented them from extending their results. Now using new, more sophisticated high accuracy software and faster computers and more computation time we could overcome some of the numerical diﬃculties. Section 3 contains details about the computations.

2. Notation

In this section we set up the notation which is needed for our computation. For more information we refer to [1]. For natural numbers d and n ≥ 3 let sd(n) be the optimal value of the minimization problem

d

ak + b11 + F0,S0n(1,1,1) :

min 1 +

k=1

- a1,...,ad ∈ R, a1,...,ad ≥ 0,
- b11,b12,b22 ∈ R, b


11 b12

b12 b22 is positive semideﬁnite, Fk ∈ R(d+1−k)×(d+1−k), Fk is positive semideﬁnite, k = 0,...,d,

- q,q1 ∈ R[u], deg(p + pq1) ≤ d, p,p1 sums of squares,
- r,r1,...,r4 ∈ R[u,v,t], deg(r +


4

piri) ≤ d, r,r1,...,r4 sums of squares,

i=1

d

d

akPkn(u) + 2b12 + b22 + 3

Fk,Skn(u,u,1) + q(u) + p(u)q1(u) = 0,

1 +

k=1

k=0

d

4

Fk,Skn(u,v,t) + r(u,v,t) +

pi(u,v,t)ri(u,v,t) = 0 .

b22 +

i=1

k=0

Here Pkn is the normalized Jacobi polynomial of degree k with Pkn(1) = 1 and parameters ((n − 3)/2,(n − 3)/2). In general, Jacobi polynomials with parameters

(α,β) are orthogonal polynomials for the measure (1−u)α(1+u)βdu on the interval [−1,1]. Before we can deﬁne the matrices Skn we ﬁrst deﬁne the entry (i,j) with i,j ≥ 0 of the (inﬁnite) matrix Ykn containing polynomials in the variables u,v,w by

Ykn i,j(u,v,t) = uivj ·

((1 − u2)(1 − v2))k/2Pkn−1

t − uv (1 − u2)(1 − v2)

![image 2](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile2.png>)

![image 3](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile3.png>)

.

Then we get Skn by symmetrization: Skn = 16 σ σYkn, where σ runs through all permutations of the variables u,v,t which acts on the matrix coeﬃcients in the

![image 4](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile4.png>)

obvious way. The polynomials p, p1,...,p4 are given by p(u) = −(u + 1)(u + 1/2), p1(u,v,t) = p(u), p2(u,v,t) = p(v), p3(u,v,t) = p(t), p4(u,v,t) = 1 + 2uvt − u2 − v2 − t2.

By A,B we denote the inner product between symmetric matrices trace(AB).

In [1] it is shown that this minimization problem is a semideﬁnite program and that every upper bound on sd(n) provides an upper bound for the kissing number in dimension n. Clearly, the numbers sd(n) form a monotonic decreasing sequence in d.

3. Bounds for kissing numbers

![image 5](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile5.png>)

![image 6](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile6.png>)

![image 7](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile7.png>)

best lower best upper bound SDP n bound known previously known bound

![image 8](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile8.png>)

![image 9](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile9.png>)

![image 10](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile10.png>)

![image 11](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile11.png>)

- 3 12 12 s11(3) = 12.42167009 . . . [16] Schu¨tte, v.d. Waerden, 1953 s12(3) = 12.40203212 . . .

![image 12](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile12.png>)

![image 13](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile13.png>)

![image 14](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile14.png>)

![image 15](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile15.png>)

![image 16](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile16.png>)

![image 17](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile17.png>)

![image 18](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile18.png>)

![image 19](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile19.png>)

![image 20](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile20.png>)

![image 21](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile21.png>)

- s13(3) = 12.39266509 . . .

![image 22](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile22.png>)

![image 23](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile23.png>)

![image 24](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile24.png>)

- s14(3) = 12.38180947 . . .


![image 25](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile25.png>)

- 4 24 24 s11(4) = 24.10550859 . . . [11] Musin, 2008 s12(4) = 24.09098111 . . .

![image 26](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile26.png>)

![image 27](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile27.png>)

![image 28](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile28.png>)

![image 29](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile29.png>)

![image 30](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile30.png>)

![image 31](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile31.png>)

![image 32](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile32.png>)

![image 33](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile33.png>)

![image 34](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile34.png>)

![image 35](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile35.png>)

- s13(4) = 24.07519774 . . .

![image 36](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile36.png>)

![image 37](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile37.png>)

![image 38](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile38.png>)

- s14(4) = 24.06628391 . . .


![image 39](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile39.png>)

- 5 40 45 s11(5) = 45.06107293 . . . [1] Bachoc, Vallentin, 2008 s12(5) = 45.02353644 . . .

![image 40](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile40.png>)

![image 41](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile41.png>)

![image 42](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile42.png>)

![image 43](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile43.png>)

![image 44](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile44.png>)

![image 45](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile45.png>)

![image 46](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile46.png>)

![image 47](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile47.png>)

![image 48](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile48.png>)

- s13(5) = 45.00650838 . . .

![image 49](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile49.png>)

![image 50](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile50.png>)

![image 51](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile51.png>)

- s14(5) = 44.99899685 . . .


![image 52](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile52.png>)

![image 53](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile53.png>)

- 6 72 78 s11(6) = 78.58344077 . . . [1] Bachoc, Vallentin, 2008 s12(6) = 78.35518719 . . .

![image 54](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile54.png>)

![image 55](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile55.png>)

![image 56](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile56.png>)

![image 57](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile57.png>)

![image 58](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile58.png>)

![image 59](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile59.png>)

![image 60](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile60.png>)

![image 61](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile61.png>)

![image 62](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile62.png>)

![image 63](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile63.png>)

- s13(6) = 78.29404232 . . .

![image 64](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile64.png>)

![image 65](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile65.png>)

![image 66](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile66.png>)

- s14(6) = 78.24061272 . . .


![image 67](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile67.png>)

- 7 126 135 s11(7) = 134.8824614 . . . [1] Bachoc, Vallentin, 2008 s12(7) = 134.7319671 . . .

![image 68](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile68.png>)

![image 69](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile69.png>)

![image 70](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile70.png>)

![image 71](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile71.png>)

![image 72](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile72.png>)

![image 73](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile73.png>)

![image 74](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile74.png>)

![image 75](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile75.png>)

![image 76](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile76.png>)

![image 77](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile77.png>)

- s13(7) = 134.5730609 . . .

![image 78](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile78.png>)

![image 79](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile79.png>)

![image 80](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile80.png>)

- s14(7) = 134.4488169 . . .


![image 81](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile81.png>)

- 8 240 240 s11(8) = 240.0000000 . . . [12] Odlyzko, Sloane, 1979

![image 82](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile82.png>)

![image 83](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile83.png>)

![image 84](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile84.png>)

![image 85](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile85.png>)

![image 86](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile86.png>)

![image 87](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile87.png>)

![image 88](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile88.png>)

![image 89](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile89.png>)

![image 90](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile90.png>)

[9] Levenshtein, 1979

![image 91](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile91.png>)

![image 92](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile92.png>)

- 9 306 366 s11(9) = 365.3229274 . . . [1] Bachoc, Vallentin, 2008 s12(9) = 364.7282746 . . .

![image 93](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile93.png>)

![image 94](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile94.png>)

![image 95](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile95.png>)

![image 96](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile96.png>)

![image 97](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile97.png>)

![image 98](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile98.png>)

![image 99](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile99.png>)

![image 100](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile100.png>)

![image 101](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile101.png>)

![image 102](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile102.png>)

- s13(9) = 364.3980087 . . .

![image 103](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile103.png>)

![image 104](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile104.png>)

![image 105](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile105.png>)

- s14(9) = 364.0919287 . . .


![image 106](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile106.png>)

- 10 500 567 s11(10) = 558.1442813 . . . [1] Bachoc, Vallentin, 2008 s12(10) = 556.2840736 . . .

![image 107](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile107.png>)

![image 108](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile108.png>)

![image 109](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile109.png>)

![image 110](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile110.png>)

![image 111](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile111.png>)

![image 112](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile112.png>)

![image 113](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile113.png>)

![image 114](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile114.png>)

![image 115](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile115.png>)

- s13(10) = 555.2399024 . . .

![image 116](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile116.png>)

![image 117](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile117.png>)

![image 118](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile118.png>)

- s14(10) = 554.5075418 . . .


![image 119](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile119.png>)

![image 120](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile120.png>)

- 11 582 915 s11(11) = 878.6158044 . . . [12] Odlyzko, Sloane, 1979 s12(11) = 873.3790094 . . .


![image 121](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile121.png>)

![image 122](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile122.png>)

![image 123](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile123.png>)

![image 124](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile124.png>)

![image 125](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile125.png>)

![image 126](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile126.png>)

![image 127](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile127.png>)

![image 128](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile128.png>)

![image 129](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile129.png>)

- s13(11) = 871.9718533 . . .

![image 130](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile130.png>)

![image 131](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile131.png>)

![image 132](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile132.png>)

- s14(11) = 870.8831157 . . .


![image 133](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile133.png>)

![image 134](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile134.png>)

- 12 840 1416 s11(12) = 1364.683810 . . . [12] Odlyzko, Sloane, 1979 s12(12) = 1362.200297 . . .

![image 135](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile135.png>)

![image 136](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile136.png>)

![image 137](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile137.png>)

![image 138](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile138.png>)

![image 139](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile139.png>)

![image 140](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile140.png>)

![image 141](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile141.png>)

![image 142](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile142.png>)

![image 143](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile143.png>)

- s13(12) = 1359.283834 . . .

![image 144](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile144.png>)

![image 145](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile145.png>)

![image 146](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile146.png>)

- s14(12) = 1357.889300 . . .


![image 147](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile147.png>)

![image 148](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile148.png>)

- 13 1130 2233 s11(13) = 2089.116331 . . . [12] Odlyzko, Sloane, 1979 s12(13) = 2080.631518 . . .

![image 149](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile149.png>)

![image 150](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile150.png>)

![image 151](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile151.png>)

![image 152](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile152.png>)

![image 153](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile153.png>)

![image 154](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile154.png>)

![image 155](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile155.png>)

![image 156](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile156.png>)

![image 157](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile157.png>)

- s13(13) = 2073.074796 . . .

![image 158](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile158.png>)

![image 159](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile159.png>)

![image 160](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile160.png>)

- s14(13) = 2069.587585 . . .


![image 161](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile161.png>)

![image 162](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile162.png>)

- 14 1582 3492 s11(14) = 3224.950751 . . . [12] Odlyzko, Sloane, 1979 s12(14) = 3202.448902 . . .

![image 163](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile163.png>)

![image 164](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile164.png>)

![image 165](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile165.png>)

![image 166](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile166.png>)

![image 167](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile167.png>)

![image 168](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile168.png>)

![image 169](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile169.png>)

![image 170](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile170.png>)

![image 171](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile171.png>)

- s13(14) = 3189.127644 . . .

![image 172](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile172.png>)

![image 173](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile173.png>)

![image 174](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile174.png>)

- s14(14) = 3183.133169 . . .


![image 175](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile175.png>)

![image 176](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile176.png>)

- 15 2564 5431 s11(15) = 4949.650431 . . . [12] Odlyzko, Sloane, 1979 s12(15) = 4893.479446 . . .

![image 177](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile177.png>)

![image 178](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile178.png>)

![image 179](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile179.png>)

![image 180](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile180.png>)

![image 181](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile181.png>)

![image 182](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile182.png>)

![image 183](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile183.png>)

![image 184](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile184.png>)

![image 185](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile185.png>)

- s13(15) = 4876.037229 . . .

![image 186](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile186.png>)

![image 187](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile187.png>)

![image 188](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile188.png>)

- s14(15) = 4866.245659 . . .


![image 189](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile189.png>)

![image 190](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile190.png>)

- 16 4320 8312 s11(16) = 7515.952644 . . . [13] Pfender, 2007 s12(16) = 7432.720718 . . .

![image 191](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile191.png>)

![image 192](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile192.png>)

![image 193](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile193.png>)

![image 194](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile194.png>)

![image 195](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile195.png>)

![image 196](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile196.png>)

![image 197](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile197.png>)

![image 198](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile198.png>)

![image 199](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile199.png>)

- s13(16) = 7374.093742 . . .

![image 200](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile200.png>)

![image 201](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile201.png>)

![image 202](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile202.png>)

- s14(16) = 7355.809036 . . .


![image 203](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile203.png>)

![image 204](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile204.png>)

- 17 5346 12210 s11(17) = 11568.41674 . . . [13] Pfender, 2007 s12(17) = 11333.84265 . . .

![image 205](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile205.png>)

![image 206](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile206.png>)

![image 207](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile207.png>)

![image 208](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile208.png>)

![image 209](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile209.png>)

![image 210](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile210.png>)

![image 211](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile211.png>)

![image 212](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile212.png>)

![image 213](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile213.png>)

- s13(17) = 11128.26227 . . .

![image 214](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile214.png>)

![image 215](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile215.png>)

![image 216](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile216.png>)

- s14(17) = 11072.37543 . . .


![image 217](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile217.png>)

![image 218](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile218.png>)

- 18 7398 17877 s11(18) = 17473.48016 . . . [12] Odlyzko, Sloane, 1979 s12(18) = 17034.32488 . . .

![image 219](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile219.png>)

![image 220](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile220.png>)

![image 221](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile221.png>)

![image 222](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile222.png>)

![image 223](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile223.png>)

![image 224](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile224.png>)

![image 225](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile225.png>)

![image 226](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile226.png>)

![image 227](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile227.png>)

- s13(18) = 16686.28908 . . .

![image 228](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile228.png>)

![image 229](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile229.png>)

![image 230](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile230.png>)

- s14(18) = 16572.26478 . . .


![image 231](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile231.png>)

![image 232](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile232.png>)

- 19 10668 25900 s11(19) = 26397.34794 . . . [3] Boyvalenkov, 1994 s12(19) = 25636.98958 . . .

![image 233](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile233.png>)

![image 234](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile234.png>)

![image 235](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile235.png>)

![image 236](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile236.png>)

![image 237](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile237.png>)

![image 238](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile238.png>)

![image 239](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile239.png>)

![image 240](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile240.png>)

![image 241](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile241.png>)

- s13(19) = 25029.87432 . . .

![image 242](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile242.png>)

![image 243](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile243.png>)

![image 244](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile244.png>)

- s14(19) = 24812.30254 . . .


![image 245](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile245.png>)

![image 246](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile246.png>)

- 20 17400 37974 s11(20) = 39045.32761 . . . [12] Odlyzko, Sloane, 1979 s12(20) = 37844.10380 . . .

![image 247](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile247.png>)

![image 248](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile248.png>)

![image 249](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile249.png>)

![image 250](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile250.png>)

![image 251](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile251.png>)

![image 252](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile252.png>)

![image 253](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile253.png>)

![image 254](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile254.png>)

![image 255](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile255.png>)

- s13(20) = 37067.18966 . . .

![image 256](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile256.png>)

![image 257](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile257.png>)

![image 258](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile258.png>)

- s14(20) = 36764.40138 . . .


![image 259](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile259.png>)

![image 260](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile260.png>)

- 21 27720 56851 s11(21) = 58087.03857 . . . [3] Boyvalenkov, 1994 s12(21) = 56079.21685 . . .

![image 261](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile261.png>)

![image 262](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile262.png>)

![image 263](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile263.png>)

![image 264](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile264.png>)

![image 265](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile265.png>)

![image 266](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile266.png>)

![image 267](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile267.png>)

![image 268](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile268.png>)

![image 269](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile269.png>)

- s13(21) = 55170.03449 . . .

![image 270](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile270.png>)

![image 271](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile271.png>)

![image 272](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile272.png>)

- s14(21) = 54584.76757 . . .


![image 273](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile273.png>)

![image 274](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile274.png>)

- 22 49896 86537 s11(22) = 87209.06261 . . . [12] Odlyzko, Sloane, 1979 s12(22) = 84922.09101 . . .

![image 275](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile275.png>)

![image 276](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile276.png>)

![image 277](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile277.png>)

![image 278](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile278.png>)

![image 279](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile279.png>)

![image 280](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile280.png>)

![image 281](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile281.png>)

![image 282](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile282.png>)

![image 283](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile283.png>)

- s13(22) = 84117.92103 . . .

![image 284](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile284.png>)

![image 285](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile285.png>)

![image 286](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile286.png>)

- s14(22) = 82340.08003 . . .


![image 287](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile287.png>)

![image 288](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile288.png>)

- 23 93150 128095 s11(23) = 128360.7969 . . . [3] Boyvalenkov, 1994 s12(23) = 127323.7095 . . .

![image 289](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile289.png>)

![image 290](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile290.png>)

![image 291](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile291.png>)

![image 292](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile292.png>)

![image 293](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile293.png>)

![image 294](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile294.png>)

![image 295](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile295.png>)

![image 296](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile296.png>)

![image 297](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile297.png>)

- s13(23) = 125978.7655 . . .

![image 298](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile298.png>)

![image 299](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile299.png>)

![image 300](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile300.png>)

- s14(23) = 124416.9796 . . .


![image 301](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile301.png>)

![image 302](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile302.png>)

- 24 196560 196560 s11(24) = 196560.0000 . . . [12] Odlyzko, Sloane, 1979


![image 303](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile303.png>)

![image 304](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile304.png>)

![image 305](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile305.png>)

![image 306](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile306.png>)

![image 307](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile307.png>)

![image 308](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile308.png>)

![image 309](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile309.png>)

![image 310](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile310.png>)

![image 311](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile311.png>)

![image 312](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile312.png>)

[9] Levenshtein, 1979 Table 1. New upper bounds for the kissing number (best known values are underlined).

![image 313](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile313.png>)

Finding the solution of the semideﬁnite program deﬁned in Section 2 is a computational challenge. It turns out that the major obstacle is numerical instability and not the problem size. When d is ﬁxed, then the size of the input matrices stays constant with n; when n is ﬁxed, then it grows rather moderately with d.

There is a number of available software packages for solving semideﬁnite programs. Mittelmann compares many existing packages in [10]. For our purpose ﬁrst order, gradient-based methods such as SDPLR are far too inaccurate, and sec-

- ond order, primal-dual interior point methods are more suitable. Here increasingly ill-conditioned linear systems have to be solved even if the underlying problem is well-conditioned. This happens in the ﬁnal phase of the algorithm when one approaches an optimal solution. Our problems are not well-conditioned and even the most robust solver SeDuMi which uses partial quadruple arithmetic in the ﬁnal phase does not produce reliable results for d > 10.


We thus had to fall back on the implementation SDPA-GMP [8] which is much slower but much more accurate than other software packages because it uses the GNU Multiple Precision Arithmetic Library. We worked with 200–300 binary digits and relative stopping criteria of 10−30. The ten signiﬁcant digits listed in the table are thus guaranteed to be correct. One problem was the convergence. Even with the control parameter settings recommended by the authors of SDPA-GMP for “slow but stable” computations, the algorithm failed to converge in several instances. However, we found parameter choices which worked for all cases: We varied the parameter lambdaStar between 100 and 10000 depending on the case while the other parameters could be chosen at or near the values recommended for “slow but stable” performance.

The computations were done on Intel Core 2 platforms with one and two Quad processors. The computation time varied between ﬁve and ten weeks per case for d = 12. An accuracy of 128 bits in SDPA-GMP did yield suﬃcient accuracy but did not yield a reduction in computing time.

After the computations for the cases d = 11 and d = 12 were ﬁnished new 128bit versions (quadruple precision) of SDPA and CSDP became available; partly with our assistance. These new versions do not rely on the GNU Multiple Precision Arithmetic Library. So the computation time for the cases d = 13 and d = 14 were reasonable: from one week to two and a half weeks.

4. Question about the optimality of the D4 root system

Looking at the values sd(4) in Table 1 one is led to the following question: Question 4.1. Is lim

sd(4) = 24?

d→∞

If the answer to this question is yes (which at the moment appears unlikely because we computed s15(4) = 23.06274835 ...), then it would have two noteworthy consequences about optimality properties of the root system D4.

The root system D4 deﬁnes (up to orthogonal transformations) a point conﬁguration on the unit sphere S3 = {x ∈ R4 : x · x = 1} consisting of 24 points; it is the same point conﬁguration as the one coming from the vertices of the regular 24 cell. This point conﬁguration has the property that the spherical distance of every two distinct points is at least arccos1/2. Hence, these points can be the maximal 24 touching points of unit spheres kissing the central unit sphere S3.

If limd→∞ sd(4) = 24, then this would prove that the root system D4 is the unique optimal point conﬁguration of cardinality 24. Here optimality means that

- one cannot distribute 24 points on S3 so that the minimal spherical distance be-


tween two distinct points exceeds arccos1/2. Thus, the root system D4 would be characterized by its kissing property. This is generally believed to be true but so far no proof could be given.

Another consequence would be that there is no universally optimal point conﬁguration of 24 points in S3 as conjectured by Cohn, Conway, Elkies, Kumar [5]. Universally optimal point conﬁgurations minimize every absolutely monotonic potential function. The conjecture would follow if the answer to our question is yes: Every universally optimal point conﬁguration is automatically optimal and Cohn, Conway, Elkies, Kumar [5] show that the root system D4 is not universally optimal.

5. Nonexistence of a sphere packing

Our new upper bound of 7355 for the kissing number in dimension 16 implies that there is no periodic point set in dimension 16 whose average theta series equals

(1) 1 + 7680q3 + 4320q4 + 276480q5 + 61440q6 + ··· .

This settles a conjecture of Conway and Sloane [6, Chapter 7, page 190]. In this section we explain this result. We refer to Conway, Sloane [6], Elkies [7], and to Bowert [2] for more information.

An n-dimensional periodic point set Λ is a ﬁnite union of translates of an ndimensional lattice, i.e. one can write Λ as Λ = (AZn + v1) ∪ ... ∪ (AZn + vN), with v1,...,vN ∈ Rn, and A : Rn → Rn is a linear isomorphism. The average theta series of Λ is

1 N

ΘΛ(z) =

![image 314](<2009-mittelmann-high-accuracy-semidefinite-programming_images/imageFile314.png>)

N

N

i+vj 2, with q = eπiz.

q Av−v

i=1

j=1 v∈Zn

This is a holomorphic function deﬁned on the complex upper half-plane. A holomorphic function f which is deﬁned on the complex upper half-plane, which is meromorphic for z → i∞, and which satisﬁes the transformation laws

f(−1/z) = z8f(z), and f(z + 2) = f(z) for all z ∈ C with ℑz > 0,

is called a modular forms of weight 8 for the Hecke group G(2). The expression (1) deﬁnes the unique modular form of weight 8 for the Hecke group G(2) which starts oﬀ with 1 + 0q1 + 0q2. It is also called an extremal modular form, see Scharlau and Schulze-Pillot [15]

If there would be a 16-dimensional periodic point set whose average theta series coincides with (1) then this periodic point set would deﬁne the sphere centers of a sphere packing with extraordinary high density (see [6, Chapter 7, page 190]). At the same time the existence of such a periodic point set would show that the kissing number in dimension 16 is at least 7680. This is not the case.

Acknowledgements

We thank Etienne de Klerk and Renata Sotirov for initiating our collaboration and we thank Frank Bowert and Rudolf Scharlau for bringing the conjecture of Conway and Sloane to our attention.

References

- [1] C. Bachoc, F. Vallentin, New upper bounds for kissing numbers from semideﬁnite programming, J. Amer. Math. Soc. 21 (2008), 909–924.
- [2] F. Bowert, Gewichtsz¨ahler und Distanzz¨ahler von Codes und Kugelpackungen, Ph.D. thesis, University of Dortmund, 2004.
- [3] P. Boyvalenkov, Small improvements of the upper bounds of the kissing numbers in dimensions 19, 21 and 23, Atti Sem. Mat. Fis. Univ. Modena 42 (1994), 159–163.
- [4] B. Casselman, The diﬃculties of kissing in three dimensions, Notices Amer. Math. Soc. 51

(2004), 884–885.

- [5] H. Cohn, J.H. Conway, N.D. Elkies, A. Kumar, The D4 root system is not universally optimal, Exp. Math. 16 (2007), 313–320.
- [6] J.H. Conway, N.J.A. Sloane, Sphere packings, lattices and groups, third edition, Springer, 1999.
- [7] N.D. Elkies, Lattices, linear codes, and invariants, Part I/II, Notices Amer. Math. Soc. 47

(2000), 1238–1245, 1382–1391.

- [8] K. Fujisawa, M. Fukuda, K. Kobayashi, M. Kojima, K. Nakata, M. Nakata, M. Yamashita, SDPA (SemiDeﬁnite Programming Algorithm) and SDPA-GMP user’s manual — version 7.1.1, Research Report B-448, Department of Mathematical and Computing Sciences, Tokyo Institute of Technology, June 2008.
- [9] V.I. Levenshtein, On bounds for packing in n-dimensional Euclidean space, Soviet Math. Dokl. 20 (1979), 417–421.
- [10] H.D. Mittelmann, An independent benchmarking of SDP and SOCP solvers, Math. Prog. 95 (2003), 407–430.
- [11] O.R. Musin, The kissing number in four dimensions, Ann. of Math. 168 (2008), 1–32.
- [12] A.M. Odlyzko, N.J.A. Sloane, New bounds on the number of unit spheres that can touch a unit sphere in n dimensions, J. Combin. Theory Ser. A 26 (1979), 210–214.
- [13] F. Pfender, Improved Delsarte bounds for spherical codes in small dimensions, J. Combin. Theory Ser. A 114 (2007), 1133–1147.
- [14] F. Pfender, G.M. Ziegler, Kissing numbers, sphere packings and some unexpected proofs, Notices Amer. Math. Soc. 51 (2004), 873–883.
- [15] R. Scharlau, R. Schulze-Pillot, Extremal lattices, p. 139–170 in Algorithmic algebra and number theory (Heidelberg, 1997), Springer, 1999.
- [16] K. Schu¨tte, B.L. van der Waerden, Das Problem der dreizehn Kugeln, Math. Ann. 125


(1953) 325–334. H.D. Mittelmann, School of Mathematical and Statistical Sciences, Arizona State

University, Tempe, AZ 85287-1804, USA E-mail address: mittelmann@asu.edu F. Vallentin, Delft Institute of Applied Mathematics, Technical University of Delft,

P.O. Box 5031, 2600 GA Delft, The Netherlands E-mail address: f.vallentin@tudelft.nl

