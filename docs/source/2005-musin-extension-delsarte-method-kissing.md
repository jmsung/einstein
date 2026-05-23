---
type: source
kind: paper
title: An extension of Delsarte's method. The kissing problem in three and four dimensions
authors: Oleg R. Musin
year: 2005
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/math/0512649v1
source_local: ../raw/2005-musin-extension-delsarte-method-kissing.pdf
topic: general-knowledge
cites:
---

# arXiv:math/0512649v1[math.MG]30Dec2005

## AN EXTENSION OF DELSARTE’S METHOD. THE KISSING PROBLEM IN THREE AND FOUR DIMENSIONS

Oleg R. Musin ∗

### 1 Introduction

The kissing number k(n) is the highest number of equal nonoverlapping spheres in Rn that can touch another sphere of the same size. In three dimensions the kissing number problem is asking how many white billiard balls can kiss (touch) a black ball.

The most symmetrical conﬁguration, 12 billiard balls around another, is if the 12 balls are placed at positions corresponding to the vertices of a regular icosahedron concentric with the central ball. However, these 12 outer balls do not kiss each other and may all moved freely. So perhaps if you moved all of

- them to one side a 13th ball would possibly ﬁt in? This problem was the subject of a famous discussion between Isaac Newton


and David Gregory in 1694. (May 4, 1694; see interesting article [33] for details of this discussion.) It is commonly said that Newton believed the answer was 12 balls, while Gregory thought that 13 might be possible. However, Bill Casselman [9] found some puzzling features in this story.

This problem is often called the thirteen spheres problem. R. Hoppe [19] thought he had solved the problem in 1874. But, Thomas Hales [18] in 1994 published analysis of Hoppe’s mistake (see also [32]). Finally this problem was solved by Sch¨utte and van der Waerden in 1953 [31]. A subsequent two-pages sketch of an elegant proof was given by Leech [23] in 1956. No much doubts that Leech’s proof is correct, but there are gaps in his exposition, many involved sophisticated spherical trigonometry. (Leech’s proof was presented in the ﬁrst edition of the well known book by Aigner & Ziegler [1], the authors removed this chapter from the second edition because a complete proof to include so much spherical trigonometry.) The thirteen spheres problem continues to be of interest, new proofs have been published in the last few years by Wu-Yi Hsiang [21], K´aroly B¨or¨czky [7], and Kurt Anstreicher [2].

![image 1](<2005-musin-extension-delsarte-method-kissing_images/imageFile1.png>)

∗Institute for Math. Study of Complex Systems, Moscow State University, Moscow, Russia omusin@mail.ru

Note that k(4) 24. Indeed, the unit sphere in R4 centered at (0,0,0,0) has 24 unit spheres around it, centered at the points (±

√2,0,0), with any choice of signs and any ordering of the coordinates. The convex hull of these 24 points yields a famous 4-dimensional regular polytope - the “24-cell”. Its facets are 24 regular octahedra.

√2,±

![image 2](<2005-musin-extension-delsarte-method-kissing_images/imageFile2.png>)

![image 3](<2005-musin-extension-delsarte-method-kissing_images/imageFile3.png>)

Coxeter proposed upper bounds on k(n) in 1963 [11]; for n = 4,5,6,7, and 8 these bounds were 26, 48, 85, 146, and 244, respectively. Coxeter’s bounds are based on the conjecture that equal size spherical caps on a sphere Sk can be packed no denser than k + 1 spherical caps on Sk that simultaneously touch one another. B¨or¨czky proved this conjecture in 1978 [6].

The main progress in the kissing number problem in high dimensions was in the end of 1970’s. Vladimir Levenshtein [24], and independently Andrew Odlyzko and Neil Sloane [27], [10, Chap.13] using Delsarte’s method in 1979 proved that k(8) = 240, and k(24) = 196560. This proof is surprisingly short, clean, and technically easier than all proofs in three dimensions.

However, n = 8,24 are the only dimensions in which this method gives a precise result. For other dimensions (for instance, n = 3,4) the upper bounds exceed the lower. In [27] the Delsarte method was applied in dimensions up to 24 (see [10, Table 1.5]). For comparison with the values of Coxeter’s bounds on k(n) for n = 4,5,6,7, and 8 this method gives 25, 46, 82, 140, and 240, respectively. (For n = 3 Coxeter’s and Delsarte’s methods only gave k(3) 13 [11, 27].) Kabatiansky and Levenshtein have found an asymptotic upper bound 20.401n(1+o(1)) for k(n) in 1978 [22]. The lower bound 20.2075n(1+o(1)) was found in [34].

Improvements in the upper bounds on kissing numbers (for n < 24) were rather weak during next years ([10, Preface to Third Edition] gives a brief review and references). Arestov and Babenko [3] proved that the bound k(4) 25 cannot be improved using Delsarte’s method. Hsiang [20] claims a proof of k(4) = 24. His work has not received yet a positive peer review.

If M unit spheres kiss the unit sphere in Rn, then the set of kissing points is an arrangement on the central sphere such that the (Euclidean) distance between any two points is at least 1. So the kissing number problem can be stated in other way: How many points can be placed on the surface of Sn−1 so that the angular separation between any two points is at least 60◦?

This leads to an important generalization: a ﬁnite subset X of Sn−1 is called a spherical z-code if for every pair (x,y) of X the scalar product x·y ≤ z. Spherical codes have many applications. The main application outside mathematics is in the design of signals for data transmission and storage. There are interesting applications to the numerical evaluation of n-dimensional integrals [10, Chap.3].

The Delsarte method (also known in coding theory as Delsarte’s linear programming method, Delsarte’s scheme, polynomial method) is described in [10, 22]. Let f(t) be a real polynomial such that f(t) ≤ 0 for t ∈ [−1,z], the coeﬃcients ck’s in the expansion of f(t) in terms of Gegenbauer polynomials

- G(kn) are nonnegative, and c0 = 1. Then the maximal number of points in a spherical z-code in Sn−1 is bounded by f(1). Suitable coeﬃcients ck’s can be


found by the linear programming method [10, Chapters 9,13].

We found an extension of the Delsarte method in 2003 [25](see details in [26]), that allowed to prove the bound k(4) < 25, i.e. k(4) = 24. This extension yields also a proof k(3) < 13.

The ﬁrst version of these proofs was relatively short, but used a numerical solution of some nonconvex optimization problems. Later on [26] these calculations have been reduced to calculations of roots of polynomials in one variable. (This is not a big problem now, all computer algebra systems such as Maple, Mathematica, and Matlab can ﬁnd roots. Also these calculations can be independently veriﬁed. If you have approximate values all roots of a polynomial,

- then you can check the existence of these roots by simple computations.) We present in this paper a new proof of the Newton-Gregory problem, an


extension of Delsarte’s method, and a proof that k(4) = 24.

### 2 The thirteen spheres problem: a new proof

Let us recall the deﬁnition of Legendre polynomials Pk(t) by recurrence formula:

3 2

P0 = 1, P1 = t, P2 =

![image 4](<2005-musin-extension-delsarte-method-kissing_images/imageFile4.png>)

- 1

![image 5](<2005-musin-extension-delsarte-method-kissing_images/imageFile5.png>)

- 2


2k − 1 k

k − 1 k

t2 −

,..., Pk =

tPk−1 −

Pk−2;

![image 6](<2005-musin-extension-delsarte-method-kissing_images/imageFile6.png>)

![image 7](<2005-musin-extension-delsarte-method-kissing_images/imageFile7.png>)

- 1

![image 8](<2005-musin-extension-delsarte-method-kissing_images/imageFile8.png>)

- 2k k!


or equivalently Pk(t) =

dk dtk

(t2 − 1)k (Rodrigues’ formula).

![image 9](<2005-musin-extension-delsarte-method-kissing_images/imageFile9.png>)

- Lemma 1. Let X = {x1,x2,...,xn} be any ﬁnite subset of the unit sphere S2 in R3. By φi,j = dist(xi,xj) we denote the spherical (angular) distance between

xi and xj. Then

n

i=1

n

j=1

Pk(cos(φi,j)) 0.

Let f(t) =

2431 80

![image 10](<2005-musin-extension-delsarte-method-kissing_images/imageFile10.png>)

t9 −

1287 20

![image 11](<2005-musin-extension-delsarte-method-kissing_images/imageFile11.png>)

t7 +

18333 400

![image 12](<2005-musin-extension-delsarte-method-kissing_images/imageFile12.png>)

t5 +

343 40

![image 13](<2005-musin-extension-delsarte-method-kissing_images/imageFile13.png>)

t4 −

83 10

![image 14](<2005-musin-extension-delsarte-method-kissing_images/imageFile14.png>)

t3 −

213 100

![image 15](<2005-musin-extension-delsarte-method-kissing_images/imageFile15.png>)

t2 +

t 10 −

![image 16](<2005-musin-extension-delsarte-method-kissing_images/imageFile16.png>)

1 200

![image 17](<2005-musin-extension-delsarte-method-kissing_images/imageFile17.png>)

.

- Lemma 2. Suppose X = {x1,x2,...,xn} ⊂ S2. Then

S(X) =

n

i=1

n

j=1

f(cos(φi,j)) n2.

- Lemma 3. Suppose X = {x1,x2,...,xn} is a subset of S2 such that the angular separation φi,j between any two distinct points xi,xj is at least 60◦. Then


n

S(X) =

i=1

n

f(cos(φi,j)) < 13n.

j=1

- Theorem 1. k(3) = 12.


Proof. Suppose X is a kissing arrangement on S2 with n = k(3). Then X is satisfying the assumptions in Lemmas 2, 3. Therefore, n2 S(X) < 13n. From this follows n < 13, i.e. n 12. From other side we have k(3) 12, then n = k(3) = 12.

![image 18](<2005-musin-extension-delsarte-method-kissing_images/imageFile18.png>)

![image 19](<2005-musin-extension-delsarte-method-kissing_images/imageFile19.png>)

![image 20](<2005-musin-extension-delsarte-method-kissing_images/imageFile20.png>)

![image 21](<2005-musin-extension-delsarte-method-kissing_images/imageFile21.png>)

We need the only one fact from spherical trigonometry, namely the law of cosines:

cosφ = cosθ1 cosθ2 + sinθ1 sinθ2 cosϕ,

- where for spherical triangle ABC the angular lengths of its sides are θ1,θ2,φ and the angle between AB,AC is ϕ (Fig. 1). If ϕ = 90◦, then cosφ = cosθ1 cosθ2 (spherical Pythagorean theorem).

![image 22](<2005-musin-extension-delsarte-method-kissing_images/imageFile22.png>)

![image 23](<2005-musin-extension-delsarte-method-kissing_images/imageFile23.png>)

![image 24](<2005-musin-extension-delsarte-method-kissing_images/imageFile24.png>)

![image 25](<2005-musin-extension-delsarte-method-kissing_images/imageFile25.png>)

![image 26](<2005-musin-extension-delsarte-method-kissing_images/imageFile26.png>)

![image 27](<2005-musin-extension-delsarte-method-kissing_images/imageFile27.png>)

![image 28](<2005-musin-extension-delsarte-method-kissing_images/imageFile28.png>)

![image 29](<2005-musin-extension-delsarte-method-kissing_images/imageFile29.png>)

![image 30](<2005-musin-extension-delsarte-method-kissing_images/imageFile30.png>)

![image 31](<2005-musin-extension-delsarte-method-kissing_images/imageFile31.png>)

![image 32](<2005-musin-extension-delsarte-method-kissing_images/imageFile32.png>)

![image 33](<2005-musin-extension-delsarte-method-kissing_images/imageFile33.png>)

![image 34](<2005-musin-extension-delsarte-method-kissing_images/imageFile34.png>)

![image 35](<2005-musin-extension-delsarte-method-kissing_images/imageFile35.png>)

![image 36](<2005-musin-extension-delsarte-method-kissing_images/imageFile36.png>)

![image 37](<2005-musin-extension-delsarte-method-kissing_images/imageFile37.png>)

![image 38](<2005-musin-extension-delsarte-method-kissing_images/imageFile38.png>)

![image 39](<2005-musin-extension-delsarte-method-kissing_images/imageFile39.png>)

![image 40](<2005-musin-extension-delsarte-method-kissing_images/imageFile40.png>)

![image 41](<2005-musin-extension-delsarte-method-kissing_images/imageFile41.png>)

![image 42](<2005-musin-extension-delsarte-method-kissing_images/imageFile42.png>)

![image 43](<2005-musin-extension-delsarte-method-kissing_images/imageFile43.png>)

![image 44](<2005-musin-extension-delsarte-method-kissing_images/imageFile44.png>)

![image 45](<2005-musin-extension-delsarte-method-kissing_images/imageFile45.png>)

![image 46](<2005-musin-extension-delsarte-method-kissing_images/imageFile46.png>)

![image 47](<2005-musin-extension-delsarte-method-kissing_images/imageFile47.png>)

![image 48](<2005-musin-extension-delsarte-method-kissing_images/imageFile48.png>)

![image 49](<2005-musin-extension-delsarte-method-kissing_images/imageFile49.png>)

![image 50](<2005-musin-extension-delsarte-method-kissing_images/imageFile50.png>)

![image 51](<2005-musin-extension-delsarte-method-kissing_images/imageFile51.png>)

![image 52](<2005-musin-extension-delsarte-method-kissing_images/imageFile52.png>)

![image 53](<2005-musin-extension-delsarte-method-kissing_images/imageFile53.png>)

![image 54](<2005-musin-extension-delsarte-method-kissing_images/imageFile54.png>)

![image 55](<2005-musin-extension-delsarte-method-kissing_images/imageFile55.png>)

![image 56](<2005-musin-extension-delsarte-method-kissing_images/imageFile56.png>)

![image 57](<2005-musin-extension-delsarte-method-kissing_images/imageFile57.png>)

![image 58](<2005-musin-extension-delsarte-method-kissing_images/imageFile58.png>)

![image 59](<2005-musin-extension-delsarte-method-kissing_images/imageFile59.png>)

![image 60](<2005-musin-extension-delsarte-method-kissing_images/imageFile60.png>)

![image 61](<2005-musin-extension-delsarte-method-kissing_images/imageFile61.png>)

![image 62](<2005-musin-extension-delsarte-method-kissing_images/imageFile62.png>)

![image 63](<2005-musin-extension-delsarte-method-kissing_images/imageFile63.png>)

![image 64](<2005-musin-extension-delsarte-method-kissing_images/imageFile64.png>)

![image 65](<2005-musin-extension-delsarte-method-kissing_images/imageFile65.png>)

![image 66](<2005-musin-extension-delsarte-method-kissing_images/imageFile66.png>)

![image 67](<2005-musin-extension-delsarte-method-kissing_images/imageFile67.png>)

![image 68](<2005-musin-extension-delsarte-method-kissing_images/imageFile68.png>)

![image 69](<2005-musin-extension-delsarte-method-kissing_images/imageFile69.png>)

![image 70](<2005-musin-extension-delsarte-method-kissing_images/imageFile70.png>)

![image 71](<2005-musin-extension-delsarte-method-kissing_images/imageFile71.png>)

![image 72](<2005-musin-extension-delsarte-method-kissing_images/imageFile72.png>)

![image 73](<2005-musin-extension-delsarte-method-kissing_images/imageFile73.png>)

![image 74](<2005-musin-extension-delsarte-method-kissing_images/imageFile74.png>)

![image 75](<2005-musin-extension-delsarte-method-kissing_images/imageFile75.png>)

![image 76](<2005-musin-extension-delsarte-method-kissing_images/imageFile76.png>)

![image 77](<2005-musin-extension-delsarte-method-kissing_images/imageFile77.png>)

![image 78](<2005-musin-extension-delsarte-method-kissing_images/imageFile78.png>)

![image 79](<2005-musin-extension-delsarte-method-kissing_images/imageFile79.png>)

![image 80](<2005-musin-extension-delsarte-method-kissing_images/imageFile80.png>)

![image 81](<2005-musin-extension-delsarte-method-kissing_images/imageFile81.png>)

![image 82](<2005-musin-extension-delsarte-method-kissing_images/imageFile82.png>)

![image 83](<2005-musin-extension-delsarte-method-kissing_images/imageFile83.png>)

![image 84](<2005-musin-extension-delsarte-method-kissing_images/imageFile84.png>)

![image 85](<2005-musin-extension-delsarte-method-kissing_images/imageFile85.png>)

![image 86](<2005-musin-extension-delsarte-method-kissing_images/imageFile86.png>)

![image 87](<2005-musin-extension-delsarte-method-kissing_images/imageFile87.png>)

![image 88](<2005-musin-extension-delsarte-method-kissing_images/imageFile88.png>)

![image 89](<2005-musin-extension-delsarte-method-kissing_images/imageFile89.png>)

![image 90](<2005-musin-extension-delsarte-method-kissing_images/imageFile90.png>)

![image 91](<2005-musin-extension-delsarte-method-kissing_images/imageFile91.png>)

![image 92](<2005-musin-extension-delsarte-method-kissing_images/imageFile92.png>)

![image 93](<2005-musin-extension-delsarte-method-kissing_images/imageFile93.png>)

![image 94](<2005-musin-extension-delsarte-method-kissing_images/imageFile94.png>)

![image 95](<2005-musin-extension-delsarte-method-kissing_images/imageFile95.png>)

![image 96](<2005-musin-extension-delsarte-method-kissing_images/imageFile96.png>)

![image 97](<2005-musin-extension-delsarte-method-kissing_images/imageFile97.png>)

![image 98](<2005-musin-extension-delsarte-method-kissing_images/imageFile98.png>)

![image 99](<2005-musin-extension-delsarte-method-kissing_images/imageFile99.png>)

![image 100](<2005-musin-extension-delsarte-method-kissing_images/imageFile100.png>)

![image 101](<2005-musin-extension-delsarte-method-kissing_images/imageFile101.png>)

![image 102](<2005-musin-extension-delsarte-method-kissing_images/imageFile102.png>)

![image 103](<2005-musin-extension-delsarte-method-kissing_images/imageFile103.png>)

![image 104](<2005-musin-extension-delsarte-method-kissing_images/imageFile104.png>)

![image 105](<2005-musin-extension-delsarte-method-kissing_images/imageFile105.png>)

![image 106](<2005-musin-extension-delsarte-method-kissing_images/imageFile106.png>)

![image 107](<2005-musin-extension-delsarte-method-kissing_images/imageFile107.png>)

![image 108](<2005-musin-extension-delsarte-method-kissing_images/imageFile108.png>)

![image 109](<2005-musin-extension-delsarte-method-kissing_images/imageFile109.png>)

![image 110](<2005-musin-extension-delsarte-method-kissing_images/imageFile110.png>)

![image 111](<2005-musin-extension-delsarte-method-kissing_images/imageFile111.png>)

![image 112](<2005-musin-extension-delsarte-method-kissing_images/imageFile112.png>)

![image 113](<2005-musin-extension-delsarte-method-kissing_images/imageFile113.png>)

![image 114](<2005-musin-extension-delsarte-method-kissing_images/imageFile114.png>)

![image 115](<2005-musin-extension-delsarte-method-kissing_images/imageFile115.png>)

![image 116](<2005-musin-extension-delsarte-method-kissing_images/imageFile116.png>)

![image 117](<2005-musin-extension-delsarte-method-kissing_images/imageFile117.png>)

![image 118](<2005-musin-extension-delsarte-method-kissing_images/imageFile118.png>)

![image 119](<2005-musin-extension-delsarte-method-kissing_images/imageFile119.png>)

![image 120](<2005-musin-extension-delsarte-method-kissing_images/imageFile120.png>)

![image 121](<2005-musin-extension-delsarte-method-kissing_images/imageFile121.png>)

![image 122](<2005-musin-extension-delsarte-method-kissing_images/imageFile122.png>)

![image 123](<2005-musin-extension-delsarte-method-kissing_images/imageFile123.png>)

![image 124](<2005-musin-extension-delsarte-method-kissing_images/imageFile124.png>)

![image 125](<2005-musin-extension-delsarte-method-kissing_images/imageFile125.png>)

![image 126](<2005-musin-extension-delsarte-method-kissing_images/imageFile126.png>)

![image 127](<2005-musin-extension-delsarte-method-kissing_images/imageFile127.png>)

![image 128](<2005-musin-extension-delsarte-method-kissing_images/imageFile128.png>)

![image 129](<2005-musin-extension-delsarte-method-kissing_images/imageFile129.png>)

![image 130](<2005-musin-extension-delsarte-method-kissing_images/imageFile130.png>)

![image 131](<2005-musin-extension-delsarte-method-kissing_images/imageFile131.png>)

![image 132](<2005-musin-extension-delsarte-method-kissing_images/imageFile132.png>)

![image 133](<2005-musin-extension-delsarte-method-kissing_images/imageFile133.png>)

![image 134](<2005-musin-extension-delsarte-method-kissing_images/imageFile134.png>)

![image 135](<2005-musin-extension-delsarte-method-kissing_images/imageFile135.png>)

![image 136](<2005-musin-extension-delsarte-method-kissing_images/imageFile136.png>)

![image 137](<2005-musin-extension-delsarte-method-kissing_images/imageFile137.png>)

![image 138](<2005-musin-extension-delsarte-method-kissing_images/imageFile138.png>)

![image 139](<2005-musin-extension-delsarte-method-kissing_images/imageFile139.png>)

![image 140](<2005-musin-extension-delsarte-method-kissing_images/imageFile140.png>)

![image 141](<2005-musin-extension-delsarte-method-kissing_images/imageFile141.png>)

![image 142](<2005-musin-extension-delsarte-method-kissing_images/imageFile142.png>)

![image 143](<2005-musin-extension-delsarte-method-kissing_images/imageFile143.png>)

![image 144](<2005-musin-extension-delsarte-method-kissing_images/imageFile144.png>)

![image 145](<2005-musin-extension-delsarte-method-kissing_images/imageFile145.png>)

![image 146](<2005-musin-extension-delsarte-method-kissing_images/imageFile146.png>)

![image 147](<2005-musin-extension-delsarte-method-kissing_images/imageFile147.png>)

![image 148](<2005-musin-extension-delsarte-method-kissing_images/imageFile148.png>)

![image 149](<2005-musin-extension-delsarte-method-kissing_images/imageFile149.png>)

![image 150](<2005-musin-extension-delsarte-method-kissing_images/imageFile150.png>)

![image 151](<2005-musin-extension-delsarte-method-kissing_images/imageFile151.png>)

![image 152](<2005-musin-extension-delsarte-method-kissing_images/imageFile152.png>)

![image 153](<2005-musin-extension-delsarte-method-kissing_images/imageFile153.png>)

![image 154](<2005-musin-extension-delsarte-method-kissing_images/imageFile154.png>)

![image 155](<2005-musin-extension-delsarte-method-kissing_images/imageFile155.png>)

![image 156](<2005-musin-extension-delsarte-method-kissing_images/imageFile156.png>)

![image 157](<2005-musin-extension-delsarte-method-kissing_images/imageFile157.png>)

![image 158](<2005-musin-extension-delsarte-method-kissing_images/imageFile158.png>)

![image 159](<2005-musin-extension-delsarte-method-kissing_images/imageFile159.png>)

![image 160](<2005-musin-extension-delsarte-method-kissing_images/imageFile160.png>)

![image 161](<2005-musin-extension-delsarte-method-kissing_images/imageFile161.png>)

![image 162](<2005-musin-extension-delsarte-method-kissing_images/imageFile162.png>)

![image 163](<2005-musin-extension-delsarte-method-kissing_images/imageFile163.png>)

![image 164](<2005-musin-extension-delsarte-method-kissing_images/imageFile164.png>)

![image 165](<2005-musin-extension-delsarte-method-kissing_images/imageFile165.png>)

![image 166](<2005-musin-extension-delsarte-method-kissing_images/imageFile166.png>)

![image 167](<2005-musin-extension-delsarte-method-kissing_images/imageFile167.png>)

![image 168](<2005-musin-extension-delsarte-method-kissing_images/imageFile168.png>)

![image 169](<2005-musin-extension-delsarte-method-kissing_images/imageFile169.png>)

![image 170](<2005-musin-extension-delsarte-method-kissing_images/imageFile170.png>)

![image 171](<2005-musin-extension-delsarte-method-kissing_images/imageFile171.png>)

![image 172](<2005-musin-extension-delsarte-method-kissing_images/imageFile172.png>)

![image 173](<2005-musin-extension-delsarte-method-kissing_images/imageFile173.png>)

![image 174](<2005-musin-extension-delsarte-method-kissing_images/imageFile174.png>)

![image 175](<2005-musin-extension-delsarte-method-kissing_images/imageFile175.png>)

![image 176](<2005-musin-extension-delsarte-method-kissing_images/imageFile176.png>)

![image 177](<2005-musin-extension-delsarte-method-kissing_images/imageFile177.png>)

![image 178](<2005-musin-extension-delsarte-method-kissing_images/imageFile178.png>)

![image 179](<2005-musin-extension-delsarte-method-kissing_images/imageFile179.png>)

![image 180](<2005-musin-extension-delsarte-method-kissing_images/imageFile180.png>)

![image 181](<2005-musin-extension-delsarte-method-kissing_images/imageFile181.png>)

![image 182](<2005-musin-extension-delsarte-method-kissing_images/imageFile182.png>)

![image 183](<2005-musin-extension-delsarte-method-kissing_images/imageFile183.png>)

![image 184](<2005-musin-extension-delsarte-method-kissing_images/imageFile184.png>)

![image 185](<2005-musin-extension-delsarte-method-kissing_images/imageFile185.png>)

![image 186](<2005-musin-extension-delsarte-method-kissing_images/imageFile186.png>)

![image 187](<2005-musin-extension-delsarte-method-kissing_images/imageFile187.png>)

![image 188](<2005-musin-extension-delsarte-method-kissing_images/imageFile188.png>)

![image 189](<2005-musin-extension-delsarte-method-kissing_images/imageFile189.png>)

![image 190](<2005-musin-extension-delsarte-method-kissing_images/imageFile190.png>)

![image 191](<2005-musin-extension-delsarte-method-kissing_images/imageFile191.png>)

![image 192](<2005-musin-extension-delsarte-method-kissing_images/imageFile192.png>)

![image 193](<2005-musin-extension-delsarte-method-kissing_images/imageFile193.png>)

![image 194](<2005-musin-extension-delsarte-method-kissing_images/imageFile194.png>)

![image 195](<2005-musin-extension-delsarte-method-kissing_images/imageFile195.png>)

![image 196](<2005-musin-extension-delsarte-method-kissing_images/imageFile196.png>)

![image 197](<2005-musin-extension-delsarte-method-kissing_images/imageFile197.png>)

![image 198](<2005-musin-extension-delsarte-method-kissing_images/imageFile198.png>)

![image 199](<2005-musin-extension-delsarte-method-kissing_images/imageFile199.png>)

![image 200](<2005-musin-extension-delsarte-method-kissing_images/imageFile200.png>)

![image 201](<2005-musin-extension-delsarte-method-kissing_images/imageFile201.png>)

![image 202](<2005-musin-extension-delsarte-method-kissing_images/imageFile202.png>)

![image 203](<2005-musin-extension-delsarte-method-kissing_images/imageFile203.png>)

![image 204](<2005-musin-extension-delsarte-method-kissing_images/imageFile204.png>)

![image 205](<2005-musin-extension-delsarte-method-kissing_images/imageFile205.png>)

![image 206](<2005-musin-extension-delsarte-method-kissing_images/imageFile206.png>)

![image 207](<2005-musin-extension-delsarte-method-kissing_images/imageFile207.png>)

![image 208](<2005-musin-extension-delsarte-method-kissing_images/imageFile208.png>)

![image 209](<2005-musin-extension-delsarte-method-kissing_images/imageFile209.png>)

![image 210](<2005-musin-extension-delsarte-method-kissing_images/imageFile210.png>)

![image 211](<2005-musin-extension-delsarte-method-kissing_images/imageFile211.png>)

![image 212](<2005-musin-extension-delsarte-method-kissing_images/imageFile212.png>)

![image 213](<2005-musin-extension-delsarte-method-kissing_images/imageFile213.png>)

![image 214](<2005-musin-extension-delsarte-method-kissing_images/imageFile214.png>)

![image 215](<2005-musin-extension-delsarte-method-kissing_images/imageFile215.png>)

![image 216](<2005-musin-extension-delsarte-method-kissing_images/imageFile216.png>)

![image 217](<2005-musin-extension-delsarte-method-kissing_images/imageFile217.png>)

![image 218](<2005-musin-extension-delsarte-method-kissing_images/imageFile218.png>)

![image 219](<2005-musin-extension-delsarte-method-kissing_images/imageFile219.png>)

![image 220](<2005-musin-extension-delsarte-method-kissing_images/imageFile220.png>)

![image 221](<2005-musin-extension-delsarte-method-kissing_images/imageFile221.png>)

![image 222](<2005-musin-extension-delsarte-method-kissing_images/imageFile222.png>)

![image 223](<2005-musin-extension-delsarte-method-kissing_images/imageFile223.png>)

![image 224](<2005-musin-extension-delsarte-method-kissing_images/imageFile224.png>)

![image 225](<2005-musin-extension-delsarte-method-kissing_images/imageFile225.png>)

![image 226](<2005-musin-extension-delsarte-method-kissing_images/imageFile226.png>)

![image 227](<2005-musin-extension-delsarte-method-kissing_images/imageFile227.png>)

![image 228](<2005-musin-extension-delsarte-method-kissing_images/imageFile228.png>)

![image 229](<2005-musin-extension-delsarte-method-kissing_images/imageFile229.png>)

![image 230](<2005-musin-extension-delsarte-method-kissing_images/imageFile230.png>)

![image 231](<2005-musin-extension-delsarte-method-kissing_images/imageFile231.png>)

![image 232](<2005-musin-extension-delsarte-method-kissing_images/imageFile232.png>)

![image 233](<2005-musin-extension-delsarte-method-kissing_images/imageFile233.png>)

![image 234](<2005-musin-extension-delsarte-method-kissing_images/imageFile234.png>)

![image 235](<2005-musin-extension-delsarte-method-kissing_images/imageFile235.png>)

![image 236](<2005-musin-extension-delsarte-method-kissing_images/imageFile236.png>)

![image 237](<2005-musin-extension-delsarte-method-kissing_images/imageFile237.png>)

![image 238](<2005-musin-extension-delsarte-method-kissing_images/imageFile238.png>)

![image 239](<2005-musin-extension-delsarte-method-kissing_images/imageFile239.png>)

![image 240](<2005-musin-extension-delsarte-method-kissing_images/imageFile240.png>)

![image 241](<2005-musin-extension-delsarte-method-kissing_images/imageFile241.png>)

![image 242](<2005-musin-extension-delsarte-method-kissing_images/imageFile242.png>)

![image 243](<2005-musin-extension-delsarte-method-kissing_images/imageFile243.png>)

![image 244](<2005-musin-extension-delsarte-method-kissing_images/imageFile244.png>)

![image 245](<2005-musin-extension-delsarte-method-kissing_images/imageFile245.png>)

![image 246](<2005-musin-extension-delsarte-method-kissing_images/imageFile246.png>)

![image 247](<2005-musin-extension-delsarte-method-kissing_images/imageFile247.png>)

![image 248](<2005-musin-extension-delsarte-method-kissing_images/imageFile248.png>)

![image 249](<2005-musin-extension-delsarte-method-kissing_images/imageFile249.png>)

![image 250](<2005-musin-extension-delsarte-method-kissing_images/imageFile250.png>)

![image 251](<2005-musin-extension-delsarte-method-kissing_images/imageFile251.png>)

![image 252](<2005-musin-extension-delsarte-method-kissing_images/imageFile252.png>)

![image 253](<2005-musin-extension-delsarte-method-kissing_images/imageFile253.png>)

![image 254](<2005-musin-extension-delsarte-method-kissing_images/imageFile254.png>)

![image 255](<2005-musin-extension-delsarte-method-kissing_images/imageFile255.png>)

![image 256](<2005-musin-extension-delsarte-method-kissing_images/imageFile256.png>)

![image 257](<2005-musin-extension-delsarte-method-kissing_images/imageFile257.png>)

![image 258](<2005-musin-extension-delsarte-method-kissing_images/imageFile258.png>)

![image 259](<2005-musin-extension-delsarte-method-kissing_images/imageFile259.png>)

![image 260](<2005-musin-extension-delsarte-method-kissing_images/imageFile260.png>)

![image 261](<2005-musin-extension-delsarte-method-kissing_images/imageFile261.png>)

![image 262](<2005-musin-extension-delsarte-method-kissing_images/imageFile262.png>)

![image 263](<2005-musin-extension-delsarte-method-kissing_images/imageFile263.png>)

![image 264](<2005-musin-extension-delsarte-method-kissing_images/imageFile264.png>)

![image 265](<2005-musin-extension-delsarte-method-kissing_images/imageFile265.png>)

![image 266](<2005-musin-extension-delsarte-method-kissing_images/imageFile266.png>)

![image 267](<2005-musin-extension-delsarte-method-kissing_images/imageFile267.png>)

![image 268](<2005-musin-extension-delsarte-method-kissing_images/imageFile268.png>)

![image 269](<2005-musin-extension-delsarte-method-kissing_images/imageFile269.png>)

![image 270](<2005-musin-extension-delsarte-method-kissing_images/imageFile270.png>)

![image 271](<2005-musin-extension-delsarte-method-kissing_images/imageFile271.png>)

![image 272](<2005-musin-extension-delsarte-method-kissing_images/imageFile272.png>)

![image 273](<2005-musin-extension-delsarte-method-kissing_images/imageFile273.png>)

![image 274](<2005-musin-extension-delsarte-method-kissing_images/imageFile274.png>)

![image 275](<2005-musin-extension-delsarte-method-kissing_images/imageFile275.png>)

![image 276](<2005-musin-extension-delsarte-method-kissing_images/imageFile276.png>)

![image 277](<2005-musin-extension-delsarte-method-kissing_images/imageFile277.png>)

![image 278](<2005-musin-extension-delsarte-method-kissing_images/imageFile278.png>)

![image 279](<2005-musin-extension-delsarte-method-kissing_images/imageFile279.png>)

![image 280](<2005-musin-extension-delsarte-method-kissing_images/imageFile280.png>)

![image 281](<2005-musin-extension-delsarte-method-kissing_images/imageFile281.png>)

![image 282](<2005-musin-extension-delsarte-method-kissing_images/imageFile282.png>)

![image 283](<2005-musin-extension-delsarte-method-kissing_images/imageFile283.png>)

![image 284](<2005-musin-extension-delsarte-method-kissing_images/imageFile284.png>)

![image 285](<2005-musin-extension-delsarte-method-kissing_images/imageFile285.png>)

![image 286](<2005-musin-extension-delsarte-method-kissing_images/imageFile286.png>)

![image 287](<2005-musin-extension-delsarte-method-kissing_images/imageFile287.png>)

![image 288](<2005-musin-extension-delsarte-method-kissing_images/imageFile288.png>)

![image 289](<2005-musin-extension-delsarte-method-kissing_images/imageFile289.png>)

![image 290](<2005-musin-extension-delsarte-method-kissing_images/imageFile290.png>)

![image 291](<2005-musin-extension-delsarte-method-kissing_images/imageFile291.png>)

![image 292](<2005-musin-extension-delsarte-method-kissing_images/imageFile292.png>)

![image 293](<2005-musin-extension-delsarte-method-kissing_images/imageFile293.png>)

![image 294](<2005-musin-extension-delsarte-method-kissing_images/imageFile294.png>)

![image 295](<2005-musin-extension-delsarte-method-kissing_images/imageFile295.png>)

![image 296](<2005-musin-extension-delsarte-method-kissing_images/imageFile296.png>)

![image 297](<2005-musin-extension-delsarte-method-kissing_images/imageFile297.png>)

![image 298](<2005-musin-extension-delsarte-method-kissing_images/imageFile298.png>)

![image 299](<2005-musin-extension-delsarte-method-kissing_images/imageFile299.png>)

![image 300](<2005-musin-extension-delsarte-method-kissing_images/imageFile300.png>)

![image 301](<2005-musin-extension-delsarte-method-kissing_images/imageFile301.png>)

![image 302](<2005-musin-extension-delsarte-method-kissing_images/imageFile302.png>)

![image 303](<2005-musin-extension-delsarte-method-kissing_images/imageFile303.png>)

![image 304](<2005-musin-extension-delsarte-method-kissing_images/imageFile304.png>)

![image 305](<2005-musin-extension-delsarte-method-kissing_images/imageFile305.png>)

![image 306](<2005-musin-extension-delsarte-method-kissing_images/imageFile306.png>)

![image 307](<2005-musin-extension-delsarte-method-kissing_images/imageFile307.png>)

![image 308](<2005-musin-extension-delsarte-method-kissing_images/imageFile308.png>)

![image 309](<2005-musin-extension-delsarte-method-kissing_images/imageFile309.png>)

![image 310](<2005-musin-extension-delsarte-method-kissing_images/imageFile310.png>)

![image 311](<2005-musin-extension-delsarte-method-kissing_images/imageFile311.png>)

![image 312](<2005-musin-extension-delsarte-method-kissing_images/imageFile312.png>)

![image 313](<2005-musin-extension-delsarte-method-kissing_images/imageFile313.png>)

![image 314](<2005-musin-extension-delsarte-method-kissing_images/imageFile314.png>)

![image 315](<2005-musin-extension-delsarte-method-kissing_images/imageFile315.png>)

![image 316](<2005-musin-extension-delsarte-method-kissing_images/imageFile316.png>)

![image 317](<2005-musin-extension-delsarte-method-kissing_images/imageFile317.png>)

![image 318](<2005-musin-extension-delsarte-method-kissing_images/imageFile318.png>)

![image 319](<2005-musin-extension-delsarte-method-kissing_images/imageFile319.png>)

![image 320](<2005-musin-extension-delsarte-method-kissing_images/imageFile320.png>)

![image 321](<2005-musin-extension-delsarte-method-kissing_images/imageFile321.png>)

![image 322](<2005-musin-extension-delsarte-method-kissing_images/imageFile322.png>)

![image 323](<2005-musin-extension-delsarte-method-kissing_images/imageFile323.png>)

![image 324](<2005-musin-extension-delsarte-method-kissing_images/imageFile324.png>)

![image 325](<2005-musin-extension-delsarte-method-kissing_images/imageFile325.png>)

![image 326](<2005-musin-extension-delsarte-method-kissing_images/imageFile326.png>)

![image 327](<2005-musin-extension-delsarte-method-kissing_images/imageFile327.png>)

![image 328](<2005-musin-extension-delsarte-method-kissing_images/imageFile328.png>)

![image 329](<2005-musin-extension-delsarte-method-kissing_images/imageFile329.png>)

![image 330](<2005-musin-extension-delsarte-method-kissing_images/imageFile330.png>)

![image 331](<2005-musin-extension-delsarte-method-kissing_images/imageFile331.png>)

![image 332](<2005-musin-extension-delsarte-method-kissing_images/imageFile332.png>)

![image 333](<2005-musin-extension-delsarte-method-kissing_images/imageFile333.png>)

![image 334](<2005-musin-extension-delsarte-method-kissing_images/imageFile334.png>)

![image 335](<2005-musin-extension-delsarte-method-kissing_images/imageFile335.png>)

![image 336](<2005-musin-extension-delsarte-method-kissing_images/imageFile336.png>)

![image 337](<2005-musin-extension-delsarte-method-kissing_images/imageFile337.png>)

![image 338](<2005-musin-extension-delsarte-method-kissing_images/imageFile338.png>)

![image 339](<2005-musin-extension-delsarte-method-kissing_images/imageFile339.png>)

![image 340](<2005-musin-extension-delsarte-method-kissing_images/imageFile340.png>)

![image 341](<2005-musin-extension-delsarte-method-kissing_images/imageFile341.png>)

![image 342](<2005-musin-extension-delsarte-method-kissing_images/imageFile342.png>)

![image 343](<2005-musin-extension-delsarte-method-kissing_images/imageFile343.png>)

![image 344](<2005-musin-extension-delsarte-method-kissing_images/imageFile344.png>)

![image 345](<2005-musin-extension-delsarte-method-kissing_images/imageFile345.png>)

![image 346](<2005-musin-extension-delsarte-method-kissing_images/imageFile346.png>)

![image 347](<2005-musin-extension-delsarte-method-kissing_images/imageFile347.png>)

![image 348](<2005-musin-extension-delsarte-method-kissing_images/imageFile348.png>)

![image 349](<2005-musin-extension-delsarte-method-kissing_images/imageFile349.png>)

![image 350](<2005-musin-extension-delsarte-method-kissing_images/imageFile350.png>)

![image 351](<2005-musin-extension-delsarte-method-kissing_images/imageFile351.png>)

![image 352](<2005-musin-extension-delsarte-method-kissing_images/imageFile352.png>)

![image 353](<2005-musin-extension-delsarte-method-kissing_images/imageFile353.png>)

![image 354](<2005-musin-extension-delsarte-method-kissing_images/imageFile354.png>)

![image 355](<2005-musin-extension-delsarte-method-kissing_images/imageFile355.png>)

![image 356](<2005-musin-extension-delsarte-method-kissing_images/imageFile356.png>)

![image 357](<2005-musin-extension-delsarte-method-kissing_images/imageFile357.png>)

![image 358](<2005-musin-extension-delsarte-method-kissing_images/imageFile358.png>)

![image 359](<2005-musin-extension-delsarte-method-kissing_images/imageFile359.png>)

![image 360](<2005-musin-extension-delsarte-method-kissing_images/imageFile360.png>)

![image 361](<2005-musin-extension-delsarte-method-kissing_images/imageFile361.png>)

![image 362](<2005-musin-extension-delsarte-method-kissing_images/imageFile362.png>)

![image 363](<2005-musin-extension-delsarte-method-kissing_images/imageFile363.png>)

![image 364](<2005-musin-extension-delsarte-method-kissing_images/imageFile364.png>)

![image 365](<2005-musin-extension-delsarte-method-kissing_images/imageFile365.png>)

![image 366](<2005-musin-extension-delsarte-method-kissing_images/imageFile366.png>)

![image 367](<2005-musin-extension-delsarte-method-kissing_images/imageFile367.png>)

![image 368](<2005-musin-extension-delsarte-method-kissing_images/imageFile368.png>)

![image 369](<2005-musin-extension-delsarte-method-kissing_images/imageFile369.png>)

![image 370](<2005-musin-extension-delsarte-method-kissing_images/imageFile370.png>)

![image 371](<2005-musin-extension-delsarte-method-kissing_images/imageFile371.png>)

![image 372](<2005-musin-extension-delsarte-method-kissing_images/imageFile372.png>)

![image 373](<2005-musin-extension-delsarte-method-kissing_images/imageFile373.png>)

![image 374](<2005-musin-extension-delsarte-method-kissing_images/imageFile374.png>)

![image 375](<2005-musin-extension-delsarte-method-kissing_images/imageFile375.png>)

![image 376](<2005-musin-extension-delsarte-method-kissing_images/imageFile376.png>)

![image 377](<2005-musin-extension-delsarte-method-kissing_images/imageFile377.png>)

![image 378](<2005-musin-extension-delsarte-method-kissing_images/imageFile378.png>)

![image 379](<2005-musin-extension-delsarte-method-kissing_images/imageFile379.png>)

![image 380](<2005-musin-extension-delsarte-method-kissing_images/imageFile380.png>)

![image 381](<2005-musin-extension-delsarte-method-kissing_images/imageFile381.png>)

![image 382](<2005-musin-extension-delsarte-method-kissing_images/imageFile382.png>)

![image 383](<2005-musin-extension-delsarte-method-kissing_images/imageFile383.png>)

![image 384](<2005-musin-extension-delsarte-method-kissing_images/imageFile384.png>)

![image 385](<2005-musin-extension-delsarte-method-kissing_images/imageFile385.png>)

![image 386](<2005-musin-extension-delsarte-method-kissing_images/imageFile386.png>)

![image 387](<2005-musin-extension-delsarte-method-kissing_images/imageFile387.png>)

![image 388](<2005-musin-extension-delsarte-method-kissing_images/imageFile388.png>)

![image 389](<2005-musin-extension-delsarte-method-kissing_images/imageFile389.png>)

![image 390](<2005-musin-extension-delsarte-method-kissing_images/imageFile390.png>)

![image 391](<2005-musin-extension-delsarte-method-kissing_images/imageFile391.png>)

![image 392](<2005-musin-extension-delsarte-method-kissing_images/imageFile392.png>)

![image 393](<2005-musin-extension-delsarte-method-kissing_images/imageFile393.png>)

![image 394](<2005-musin-extension-delsarte-method-kissing_images/imageFile394.png>)

![image 395](<2005-musin-extension-delsarte-method-kissing_images/imageFile395.png>)

![image 396](<2005-musin-extension-delsarte-method-kissing_images/imageFile396.png>)

![image 397](<2005-musin-extension-delsarte-method-kissing_images/imageFile397.png>)

![image 398](<2005-musin-extension-delsarte-method-kissing_images/imageFile398.png>)

![image 399](<2005-musin-extension-delsarte-method-kissing_images/imageFile399.png>)

![image 400](<2005-musin-extension-delsarte-method-kissing_images/imageFile400.png>)

![image 401](<2005-musin-extension-delsarte-method-kissing_images/imageFile401.png>)

![image 402](<2005-musin-extension-delsarte-method-kissing_images/imageFile402.png>)

![image 403](<2005-musin-extension-delsarte-method-kissing_images/imageFile403.png>)

![image 404](<2005-musin-extension-delsarte-method-kissing_images/imageFile404.png>)

![image 405](<2005-musin-extension-delsarte-method-kissing_images/imageFile405.png>)

![image 406](<2005-musin-extension-delsarte-method-kissing_images/imageFile406.png>)

![image 407](<2005-musin-extension-delsarte-method-kissing_images/imageFile407.png>)

![image 408](<2005-musin-extension-delsarte-method-kissing_images/imageFile408.png>)

![image 409](<2005-musin-extension-delsarte-method-kissing_images/imageFile409.png>)

![image 410](<2005-musin-extension-delsarte-method-kissing_images/imageFile410.png>)

![image 411](<2005-musin-extension-delsarte-method-kissing_images/imageFile411.png>)

![image 412](<2005-musin-extension-delsarte-method-kissing_images/imageFile412.png>)

![image 413](<2005-musin-extension-delsarte-method-kissing_images/imageFile413.png>)

![image 414](<2005-musin-extension-delsarte-method-kissing_images/imageFile414.png>)

![image 415](<2005-musin-extension-delsarte-method-kissing_images/imageFile415.png>)

![image 416](<2005-musin-extension-delsarte-method-kissing_images/imageFile416.png>)

![image 417](<2005-musin-extension-delsarte-method-kissing_images/imageFile417.png>)

![image 418](<2005-musin-extension-delsarte-method-kissing_images/imageFile418.png>)

![image 419](<2005-musin-extension-delsarte-method-kissing_images/imageFile419.png>)

![image 420](<2005-musin-extension-delsarte-method-kissing_images/imageFile420.png>)

![image 421](<2005-musin-extension-delsarte-method-kissing_images/imageFile421.png>)

![image 422](<2005-musin-extension-delsarte-method-kissing_images/imageFile422.png>)

![image 423](<2005-musin-extension-delsarte-method-kissing_images/imageFile423.png>)

![image 424](<2005-musin-extension-delsarte-method-kissing_images/imageFile424.png>)

![image 425](<2005-musin-extension-delsarte-method-kissing_images/imageFile425.png>)

![image 426](<2005-musin-extension-delsarte-method-kissing_images/imageFile426.png>)

![image 427](<2005-musin-extension-delsarte-method-kissing_images/imageFile427.png>)

![image 428](<2005-musin-extension-delsarte-method-kissing_images/imageFile428.png>)

![image 429](<2005-musin-extension-delsarte-method-kissing_images/imageFile429.png>)

![image 430](<2005-musin-extension-delsarte-method-kissing_images/imageFile430.png>)

![image 431](<2005-musin-extension-delsarte-method-kissing_images/imageFile431.png>)

![image 432](<2005-musin-extension-delsarte-method-kissing_images/imageFile432.png>)

![image 433](<2005-musin-extension-delsarte-method-kissing_images/imageFile433.png>)

![image 434](<2005-musin-extension-delsarte-method-kissing_images/imageFile434.png>)

![image 435](<2005-musin-extension-delsarte-method-kissing_images/imageFile435.png>)

![image 436](<2005-musin-extension-delsarte-method-kissing_images/imageFile436.png>)

![image 437](<2005-musin-extension-delsarte-method-kissing_images/imageFile437.png>)

![image 438](<2005-musin-extension-delsarte-method-kissing_images/imageFile438.png>)

![image 439](<2005-musin-extension-delsarte-method-kissing_images/imageFile439.png>)

![image 440](<2005-musin-extension-delsarte-method-kissing_images/imageFile440.png>)

![image 441](<2005-musin-extension-delsarte-method-kissing_images/imageFile441.png>)

![image 442](<2005-musin-extension-delsarte-method-kissing_images/imageFile442.png>)

![image 443](<2005-musin-extension-delsarte-method-kissing_images/imageFile443.png>)

![image 444](<2005-musin-extension-delsarte-method-kissing_images/imageFile444.png>)

![image 445](<2005-musin-extension-delsarte-method-kissing_images/imageFile445.png>)

![image 446](<2005-musin-extension-delsarte-method-kissing_images/imageFile446.png>)

![image 447](<2005-musin-extension-delsarte-method-kissing_images/imageFile447.png>)

![image 448](<2005-musin-extension-delsarte-method-kissing_images/imageFile448.png>)

![image 449](<2005-musin-extension-delsarte-method-kissing_images/imageFile449.png>)

![image 450](<2005-musin-extension-delsarte-method-kissing_images/imageFile450.png>)

![image 451](<2005-musin-extension-delsarte-method-kissing_images/imageFile451.png>)

![image 452](<2005-musin-extension-delsarte-method-kissing_images/imageFile452.png>)

![image 453](<2005-musin-extension-delsarte-method-kissing_images/imageFile453.png>)

![image 454](<2005-musin-extension-delsarte-method-kissing_images/imageFile454.png>)

![image 455](<2005-musin-extension-delsarte-method-kissing_images/imageFile455.png>)

![image 456](<2005-musin-extension-delsarte-method-kissing_images/imageFile456.png>)

![image 457](<2005-musin-extension-delsarte-method-kissing_images/imageFile457.png>)

![image 458](<2005-musin-extension-delsarte-method-kissing_images/imageFile458.png>)

![image 459](<2005-musin-extension-delsarte-method-kissing_images/imageFile459.png>)

![image 460](<2005-musin-extension-delsarte-method-kissing_images/imageFile460.png>)

![image 461](<2005-musin-extension-delsarte-method-kissing_images/imageFile461.png>)

![image 462](<2005-musin-extension-delsarte-method-kissing_images/imageFile462.png>)

![image 463](<2005-musin-extension-delsarte-method-kissing_images/imageFile463.png>)

![image 464](<2005-musin-extension-delsarte-method-kissing_images/imageFile464.png>)

![image 465](<2005-musin-extension-delsarte-method-kissing_images/imageFile465.png>)

![image 466](<2005-musin-extension-delsarte-method-kissing_images/imageFile466.png>)

![image 467](<2005-musin-extension-delsarte-method-kissing_images/imageFile467.png>)

![image 468](<2005-musin-extension-delsarte-method-kissing_images/imageFile468.png>)

![image 469](<2005-musin-extension-delsarte-method-kissing_images/imageFile469.png>)

![image 470](<2005-musin-extension-delsarte-method-kissing_images/imageFile470.png>)

![image 471](<2005-musin-extension-delsarte-method-kissing_images/imageFile471.png>)

![image 472](<2005-musin-extension-delsarte-method-kissing_images/imageFile472.png>)

![image 473](<2005-musin-extension-delsarte-method-kissing_images/imageFile473.png>)

![image 474](<2005-musin-extension-delsarte-method-kissing_images/imageFile474.png>)

![image 475](<2005-musin-extension-delsarte-method-kissing_images/imageFile475.png>)

![image 476](<2005-musin-extension-delsarte-method-kissing_images/imageFile476.png>)

![image 477](<2005-musin-extension-delsarte-method-kissing_images/imageFile477.png>)

![image 478](<2005-musin-extension-delsarte-method-kissing_images/imageFile478.png>)

![image 479](<2005-musin-extension-delsarte-method-kissing_images/imageFile479.png>)

![image 480](<2005-musin-extension-delsarte-method-kissing_images/imageFile480.png>)

![image 481](<2005-musin-extension-delsarte-method-kissing_images/imageFile481.png>)

![image 482](<2005-musin-extension-delsarte-method-kissing_images/imageFile482.png>)

![image 483](<2005-musin-extension-delsarte-method-kissing_images/imageFile483.png>)

![image 484](<2005-musin-extension-delsarte-method-kissing_images/imageFile484.png>)

![image 485](<2005-musin-extension-delsarte-method-kissing_images/imageFile485.png>)

![image 486](<2005-musin-extension-delsarte-method-kissing_images/imageFile486.png>)

![image 487](<2005-musin-extension-delsarte-method-kissing_images/imageFile487.png>)

![image 488](<2005-musin-extension-delsarte-method-kissing_images/imageFile488.png>)

![image 489](<2005-musin-extension-delsarte-method-kissing_images/imageFile489.png>)

![image 490](<2005-musin-extension-delsarte-method-kissing_images/imageFile490.png>)

![image 491](<2005-musin-extension-delsarte-method-kissing_images/imageFile491.png>)

![image 492](<2005-musin-extension-delsarte-method-kissing_images/imageFile492.png>)

![image 493](<2005-musin-extension-delsarte-method-kissing_images/imageFile493.png>)

![image 494](<2005-musin-extension-delsarte-method-kissing_images/imageFile494.png>)

![image 495](<2005-musin-extension-delsarte-method-kissing_images/imageFile495.png>)

![image 496](<2005-musin-extension-delsarte-method-kissing_images/imageFile496.png>)

![image 497](<2005-musin-extension-delsarte-method-kissing_images/imageFile497.png>)

![image 498](<2005-musin-extension-delsarte-method-kissing_images/imageFile498.png>)

![image 499](<2005-musin-extension-delsarte-method-kissing_images/imageFile499.png>)

![image 500](<2005-musin-extension-delsarte-method-kissing_images/imageFile500.png>)

![image 501](<2005-musin-extension-delsarte-method-kissing_images/imageFile501.png>)

![image 502](<2005-musin-extension-delsarte-method-kissing_images/imageFile502.png>)

![image 503](<2005-musin-extension-delsarte-method-kissing_images/imageFile503.png>)

![image 504](<2005-musin-extension-delsarte-method-kissing_images/imageFile504.png>)

![image 505](<2005-musin-extension-delsarte-method-kissing_images/imageFile505.png>)

![image 506](<2005-musin-extension-delsarte-method-kissing_images/imageFile506.png>)

![image 507](<2005-musin-extension-delsarte-method-kissing_images/imageFile507.png>)

![image 508](<2005-musin-extension-delsarte-method-kissing_images/imageFile508.png>)

![image 509](<2005-musin-extension-delsarte-method-kissing_images/imageFile509.png>)

![image 510](<2005-musin-extension-delsarte-method-kissing_images/imageFile510.png>)

![image 511](<2005-musin-extension-delsarte-method-kissing_images/imageFile511.png>)

![image 512](<2005-musin-extension-delsarte-method-kissing_images/imageFile512.png>)

![image 513](<2005-musin-extension-delsarte-method-kissing_images/imageFile513.png>)

![image 514](<2005-musin-extension-delsarte-method-kissing_images/imageFile514.png>)

![image 515](<2005-musin-extension-delsarte-method-kissing_images/imageFile515.png>)

![image 516](<2005-musin-extension-delsarte-method-kissing_images/imageFile516.png>)

![image 517](<2005-musin-extension-delsarte-method-kissing_images/imageFile517.png>)

![image 518](<2005-musin-extension-delsarte-method-kissing_images/imageFile518.png>)

![image 519](<2005-musin-extension-delsarte-method-kissing_images/imageFile519.png>)

![image 520](<2005-musin-extension-delsarte-method-kissing_images/imageFile520.png>)

![image 521](<2005-musin-extension-delsarte-method-kissing_images/imageFile521.png>)

![image 522](<2005-musin-extension-delsarte-method-kissing_images/imageFile522.png>)

![image 523](<2005-musin-extension-delsarte-method-kissing_images/imageFile523.png>)

![image 524](<2005-musin-extension-delsarte-method-kissing_images/imageFile524.png>)

![image 525](<2005-musin-extension-delsarte-method-kissing_images/imageFile525.png>)

![image 526](<2005-musin-extension-delsarte-method-kissing_images/imageFile526.png>)

![image 527](<2005-musin-extension-delsarte-method-kissing_images/imageFile527.png>)

![image 528](<2005-musin-extension-delsarte-method-kissing_images/imageFile528.png>)

![image 529](<2005-musin-extension-delsarte-method-kissing_images/imageFile529.png>)

![image 530](<2005-musin-extension-delsarte-method-kissing_images/imageFile530.png>)

![image 531](<2005-musin-extension-delsarte-method-kissing_images/imageFile531.png>)

![image 532](<2005-musin-extension-delsarte-method-kissing_images/imageFile532.png>)

![image 533](<2005-musin-extension-delsarte-method-kissing_images/imageFile533.png>)

![image 534](<2005-musin-extension-delsarte-method-kissing_images/imageFile534.png>)

![image 535](<2005-musin-extension-delsarte-method-kissing_images/imageFile535.png>)

![image 536](<2005-musin-extension-delsarte-method-kissing_images/imageFile536.png>)

![image 537](<2005-musin-extension-delsarte-method-kissing_images/imageFile537.png>)

![image 538](<2005-musin-extension-delsarte-method-kissing_images/imageFile538.png>)

![image 539](<2005-musin-extension-delsarte-method-kissing_images/imageFile539.png>)

![image 540](<2005-musin-extension-delsarte-method-kissing_images/imageFile540.png>)

![image 541](<2005-musin-extension-delsarte-method-kissing_images/imageFile541.png>)

![image 542](<2005-musin-extension-delsarte-method-kissing_images/imageFile542.png>)

![image 543](<2005-musin-extension-delsarte-method-kissing_images/imageFile543.png>)

![image 544](<2005-musin-extension-delsarte-method-kissing_images/imageFile544.png>)

![image 545](<2005-musin-extension-delsarte-method-kissing_images/imageFile545.png>)

![image 546](<2005-musin-extension-delsarte-method-kissing_images/imageFile546.png>)

![image 547](<2005-musin-extension-delsarte-method-kissing_images/imageFile547.png>)

![image 548](<2005-musin-extension-delsarte-method-kissing_images/imageFile548.png>)

![image 549](<2005-musin-extension-delsarte-method-kissing_images/imageFile549.png>)

![image 550](<2005-musin-extension-delsarte-method-kissing_images/imageFile550.png>)

![image 551](<2005-musin-extension-delsarte-method-kissing_images/imageFile551.png>)

![image 552](<2005-musin-extension-delsarte-method-kissing_images/imageFile552.png>)

![image 553](<2005-musin-extension-delsarte-method-kissing_images/imageFile553.png>)

![image 554](<2005-musin-extension-delsarte-method-kissing_images/imageFile554.png>)

![image 555](<2005-musin-extension-delsarte-method-kissing_images/imageFile555.png>)

![image 556](<2005-musin-extension-delsarte-method-kissing_images/imageFile556.png>)

![image 557](<2005-musin-extension-delsarte-method-kissing_images/imageFile557.png>)

![image 558](<2005-musin-extension-delsarte-method-kissing_images/imageFile558.png>)

![image 559](<2005-musin-extension-delsarte-method-kissing_images/imageFile559.png>)

![image 560](<2005-musin-extension-delsarte-method-kissing_images/imageFile560.png>)

![image 561](<2005-musin-extension-delsarte-method-kissing_images/imageFile561.png>)

![image 562](<2005-musin-extension-delsarte-method-kissing_images/imageFile562.png>)

![image 563](<2005-musin-extension-delsarte-method-kissing_images/imageFile563.png>)

![image 564](<2005-musin-extension-delsarte-method-kissing_images/imageFile564.png>)

![image 565](<2005-musin-extension-delsarte-method-kissing_images/imageFile565.png>)

![image 566](<2005-musin-extension-delsarte-method-kissing_images/imageFile566.png>)

![image 567](<2005-musin-extension-delsarte-method-kissing_images/imageFile567.png>)

![image 568](<2005-musin-extension-delsarte-method-kissing_images/imageFile568.png>)

![image 569](<2005-musin-extension-delsarte-method-kissing_images/imageFile569.png>)

![image 570](<2005-musin-extension-delsarte-method-kissing_images/imageFile570.png>)

![image 571](<2005-musin-extension-delsarte-method-kissing_images/imageFile571.png>)

![image 572](<2005-musin-extension-delsarte-method-kissing_images/imageFile572.png>)

![image 573](<2005-musin-extension-delsarte-method-kissing_images/imageFile573.png>)

![image 574](<2005-musin-extension-delsarte-method-kissing_images/imageFile574.png>)

![image 575](<2005-musin-extension-delsarte-method-kissing_images/imageFile575.png>)

![image 576](<2005-musin-extension-delsarte-method-kissing_images/imageFile576.png>)

![image 577](<2005-musin-extension-delsarte-method-kissing_images/imageFile577.png>)

![image 578](<2005-musin-extension-delsarte-method-kissing_images/imageFile578.png>)

![image 579](<2005-musin-extension-delsarte-method-kissing_images/imageFile579.png>)

![image 580](<2005-musin-extension-delsarte-method-kissing_images/imageFile580.png>)

![image 581](<2005-musin-extension-delsarte-method-kissing_images/imageFile581.png>)

![image 582](<2005-musin-extension-delsarte-method-kissing_images/imageFile582.png>)

![image 583](<2005-musin-extension-delsarte-method-kissing_images/imageFile583.png>)

![image 584](<2005-musin-extension-delsarte-method-kissing_images/imageFile584.png>)

![image 585](<2005-musin-extension-delsarte-method-kissing_images/imageFile585.png>)

![image 586](<2005-musin-extension-delsarte-method-kissing_images/imageFile586.png>)

![image 587](<2005-musin-extension-delsarte-method-kissing_images/imageFile587.png>)

![image 588](<2005-musin-extension-delsarte-method-kissing_images/imageFile588.png>)

![image 589](<2005-musin-extension-delsarte-method-kissing_images/imageFile589.png>)

![image 590](<2005-musin-extension-delsarte-method-kissing_images/imageFile590.png>)

![image 591](<2005-musin-extension-delsarte-method-kissing_images/imageFile591.png>)

![image 592](<2005-musin-extension-delsarte-method-kissing_images/imageFile592.png>)

![image 593](<2005-musin-extension-delsarte-method-kissing_images/imageFile593.png>)

![image 594](<2005-musin-extension-delsarte-method-kissing_images/imageFile594.png>)

![image 595](<2005-musin-extension-delsarte-method-kissing_images/imageFile595.png>)

![image 596](<2005-musin-extension-delsarte-method-kissing_images/imageFile596.png>)

![image 597](<2005-musin-extension-delsarte-method-kissing_images/imageFile597.png>)

![image 598](<2005-musin-extension-delsarte-method-kissing_images/imageFile598.png>)

![image 599](<2005-musin-extension-delsarte-method-kissing_images/imageFile599.png>)

![image 600](<2005-musin-extension-delsarte-method-kissing_images/imageFile600.png>)

![image 601](<2005-musin-extension-delsarte-method-kissing_images/imageFile601.png>)

![image 602](<2005-musin-extension-delsarte-method-kissing_images/imageFile602.png>)

![image 603](<2005-musin-extension-delsarte-method-kissing_images/imageFile603.png>)

![image 604](<2005-musin-extension-delsarte-method-kissing_images/imageFile604.png>)

![image 605](<2005-musin-extension-delsarte-method-kissing_images/imageFile605.png>)

![image 606](<2005-musin-extension-delsarte-method-kissing_images/imageFile606.png>)

![image 607](<2005-musin-extension-delsarte-method-kissing_images/imageFile607.png>)

![image 608](<2005-musin-extension-delsarte-method-kissing_images/imageFile608.png>)

![image 609](<2005-musin-extension-delsarte-method-kissing_images/imageFile609.png>)

![image 610](<2005-musin-extension-delsarte-method-kissing_images/imageFile610.png>)

![image 611](<2005-musin-extension-delsarte-method-kissing_images/imageFile611.png>)

![image 612](<2005-musin-extension-delsarte-method-kissing_images/imageFile612.png>)

![image 613](<2005-musin-extension-delsarte-method-kissing_images/imageFile613.png>)

![image 614](<2005-musin-extension-delsarte-method-kissing_images/imageFile614.png>)

![image 615](<2005-musin-extension-delsarte-method-kissing_images/imageFile615.png>)

![image 616](<2005-musin-extension-delsarte-method-kissing_images/imageFile616.png>)

![image 617](<2005-musin-extension-delsarte-method-kissing_images/imageFile617.png>)

![image 618](<2005-musin-extension-delsarte-method-kissing_images/imageFile618.png>)

![image 619](<2005-musin-extension-delsarte-method-kissing_images/imageFile619.png>)

![image 620](<2005-musin-extension-delsarte-method-kissing_images/imageFile620.png>)

![image 621](<2005-musin-extension-delsarte-method-kissing_images/imageFile621.png>)

![image 622](<2005-musin-extension-delsarte-method-kissing_images/imageFile622.png>)

![image 623](<2005-musin-extension-delsarte-method-kissing_images/imageFile623.png>)

![image 624](<2005-musin-extension-delsarte-method-kissing_images/imageFile624.png>)

![image 625](<2005-musin-extension-delsarte-method-kissing_images/imageFile625.png>)

![image 626](<2005-musin-extension-delsarte-method-kissing_images/imageFile626.png>)

![image 627](<2005-musin-extension-delsarte-method-kissing_images/imageFile627.png>)

![image 628](<2005-musin-extension-delsarte-method-kissing_images/imageFile628.png>)

![image 629](<2005-musin-extension-delsarte-method-kissing_images/imageFile629.png>)

![image 630](<2005-musin-extension-delsarte-method-kissing_images/imageFile630.png>)

![image 631](<2005-musin-extension-delsarte-method-kissing_images/imageFile631.png>)

![image 632](<2005-musin-extension-delsarte-method-kissing_images/imageFile632.png>)

![image 633](<2005-musin-extension-delsarte-method-kissing_images/imageFile633.png>)

![image 634](<2005-musin-extension-delsarte-method-kissing_images/imageFile634.png>)

![image 635](<2005-musin-extension-delsarte-method-kissing_images/imageFile635.png>)

![image 636](<2005-musin-extension-delsarte-method-kissing_images/imageFile636.png>)

![image 637](<2005-musin-extension-delsarte-method-kissing_images/imageFile637.png>)

![image 638](<2005-musin-extension-delsarte-method-kissing_images/imageFile638.png>)

![image 639](<2005-musin-extension-delsarte-method-kissing_images/imageFile639.png>)

![image 640](<2005-musin-extension-delsarte-method-kissing_images/imageFile640.png>)

![image 641](<2005-musin-extension-delsarte-method-kissing_images/imageFile641.png>)

![image 642](<2005-musin-extension-delsarte-method-kissing_images/imageFile642.png>)

![image 643](<2005-musin-extension-delsarte-method-kissing_images/imageFile643.png>)

![image 644](<2005-musin-extension-delsarte-method-kissing_images/imageFile644.png>)

![image 645](<2005-musin-extension-delsarte-method-kissing_images/imageFile645.png>)

![image 646](<2005-musin-extension-delsarte-method-kissing_images/imageFile646.png>)

![image 647](<2005-musin-extension-delsarte-method-kissing_images/imageFile647.png>)

![image 648](<2005-musin-extension-delsarte-method-kissing_images/imageFile648.png>)

![image 649](<2005-musin-extension-delsarte-method-kissing_images/imageFile649.png>)

![image 650](<2005-musin-extension-delsarte-method-kissing_images/imageFile650.png>)

![image 651](<2005-musin-extension-delsarte-method-kissing_images/imageFile651.png>)

![image 652](<2005-musin-extension-delsarte-method-kissing_images/imageFile652.png>)

![image 653](<2005-musin-extension-delsarte-method-kissing_images/imageFile653.png>)

![image 654](<2005-musin-extension-delsarte-method-kissing_images/imageFile654.png>)

![image 655](<2005-musin-extension-delsarte-method-kissing_images/imageFile655.png>)

![image 656](<2005-musin-extension-delsarte-method-kissing_images/imageFile656.png>)

![image 657](<2005-musin-extension-delsarte-method-kissing_images/imageFile657.png>)

![image 658](<2005-musin-extension-delsarte-method-kissing_images/imageFile658.png>)

![image 659](<2005-musin-extension-delsarte-method-kissing_images/imageFile659.png>)

![image 660](<2005-musin-extension-delsarte-method-kissing_images/imageFile660.png>)

![image 661](<2005-musin-extension-delsarte-method-kissing_images/imageFile661.png>)

![image 662](<2005-musin-extension-delsarte-method-kissing_images/imageFile662.png>)

![image 663](<2005-musin-extension-delsarte-method-kissing_images/imageFile663.png>)

![image 664](<2005-musin-extension-delsarte-method-kissing_images/imageFile664.png>)

![image 665](<2005-musin-extension-delsarte-method-kissing_images/imageFile665.png>)

![image 666](<2005-musin-extension-delsarte-method-kissing_images/imageFile666.png>)

![image 667](<2005-musin-extension-delsarte-method-kissing_images/imageFile667.png>)

![image 668](<2005-musin-extension-delsarte-method-kissing_images/imageFile668.png>)

![image 669](<2005-musin-extension-delsarte-method-kissing_images/imageFile669.png>)

![image 670](<2005-musin-extension-delsarte-method-kissing_images/imageFile670.png>)

![image 671](<2005-musin-extension-delsarte-method-kissing_images/imageFile671.png>)

![image 672](<2005-musin-extension-delsarte-method-kissing_images/imageFile672.png>)

![image 673](<2005-musin-extension-delsarte-method-kissing_images/imageFile673.png>)

![image 674](<2005-musin-extension-delsarte-method-kissing_images/imageFile674.png>)

![image 675](<2005-musin-extension-delsarte-method-kissing_images/imageFile675.png>)

![image 676](<2005-musin-extension-delsarte-method-kissing_images/imageFile676.png>)

![image 677](<2005-musin-extension-delsarte-method-kissing_images/imageFile677.png>)

![image 678](<2005-musin-extension-delsarte-method-kissing_images/imageFile678.png>)

![image 679](<2005-musin-extension-delsarte-method-kissing_images/imageFile679.png>)

![image 680](<2005-musin-extension-delsarte-method-kissing_images/imageFile680.png>)

![image 681](<2005-musin-extension-delsarte-method-kissing_images/imageFile681.png>)

![image 682](<2005-musin-extension-delsarte-method-kissing_images/imageFile682.png>)

![image 683](<2005-musin-extension-delsarte-method-kissing_images/imageFile683.png>)

![image 684](<2005-musin-extension-delsarte-method-kissing_images/imageFile684.png>)

![image 685](<2005-musin-extension-delsarte-method-kissing_images/imageFile685.png>)

![image 686](<2005-musin-extension-delsarte-method-kissing_images/imageFile686.png>)

![image 687](<2005-musin-extension-delsarte-method-kissing_images/imageFile687.png>)

![image 688](<2005-musin-extension-delsarte-method-kissing_images/imageFile688.png>)

![image 689](<2005-musin-extension-delsarte-method-kissing_images/imageFile689.png>)

![image 690](<2005-musin-extension-delsarte-method-kissing_images/imageFile690.png>)

![image 691](<2005-musin-extension-delsarte-method-kissing_images/imageFile691.png>)

![image 692](<2005-musin-extension-delsarte-method-kissing_images/imageFile692.png>)

![image 693](<2005-musin-extension-delsarte-method-kissing_images/imageFile693.png>)

![image 694](<2005-musin-extension-delsarte-method-kissing_images/imageFile694.png>)

![image 695](<2005-musin-extension-delsarte-method-kissing_images/imageFile695.png>)

![image 696](<2005-musin-extension-delsarte-method-kissing_images/imageFile696.png>)

![image 697](<2005-musin-extension-delsarte-method-kissing_images/imageFile697.png>)

![image 698](<2005-musin-extension-delsarte-method-kissing_images/imageFile698.png>)

![image 699](<2005-musin-extension-delsarte-method-kissing_images/imageFile699.png>)

![image 700](<2005-musin-extension-delsarte-method-kissing_images/imageFile700.png>)

![image 701](<2005-musin-extension-delsarte-method-kissing_images/imageFile701.png>)

![image 702](<2005-musin-extension-delsarte-method-kissing_images/imageFile702.png>)

![image 703](<2005-musin-extension-delsarte-method-kissing_images/imageFile703.png>)

![image 704](<2005-musin-extension-delsarte-method-kissing_images/imageFile704.png>)

![image 705](<2005-musin-extension-delsarte-method-kissing_images/imageFile705.png>)

![image 706](<2005-musin-extension-delsarte-method-kissing_images/imageFile706.png>)

![image 707](<2005-musin-extension-delsarte-method-kissing_images/imageFile707.png>)

![image 708](<2005-musin-extension-delsarte-method-kissing_images/imageFile708.png>)

![image 709](<2005-musin-extension-delsarte-method-kissing_images/imageFile709.png>)

![image 710](<2005-musin-extension-delsarte-method-kissing_images/imageFile710.png>)

![image 711](<2005-musin-extension-delsarte-method-kissing_images/imageFile711.png>)

![image 712](<2005-musin-extension-delsarte-method-kissing_images/imageFile712.png>)

![image 713](<2005-musin-extension-delsarte-method-kissing_images/imageFile713.png>)

![image 714](<2005-musin-extension-delsarte-method-kissing_images/imageFile714.png>)

![image 715](<2005-musin-extension-delsarte-method-kissing_images/imageFile715.png>)

![image 716](<2005-musin-extension-delsarte-method-kissing_images/imageFile716.png>)

![image 717](<2005-musin-extension-delsarte-method-kissing_images/imageFile717.png>)

![image 718](<2005-musin-extension-delsarte-method-kissing_images/imageFile718.png>)

![image 719](<2005-musin-extension-delsarte-method-kissing_images/imageFile719.png>)

![image 720](<2005-musin-extension-delsarte-method-kissing_images/imageFile720.png>)

![image 721](<2005-musin-extension-delsarte-method-kissing_images/imageFile721.png>)

![image 722](<2005-musin-extension-delsarte-method-kissing_images/imageFile722.png>)

![image 723](<2005-musin-extension-delsarte-method-kissing_images/imageFile723.png>)

![image 724](<2005-musin-extension-delsarte-method-kissing_images/imageFile724.png>)

![image 725](<2005-musin-extension-delsarte-method-kissing_images/imageFile725.png>)

![image 726](<2005-musin-extension-delsarte-method-kissing_images/imageFile726.png>)

![image 727](<2005-musin-extension-delsarte-method-kissing_images/imageFile727.png>)

![image 728](<2005-musin-extension-delsarte-method-kissing_images/imageFile728.png>)

![image 729](<2005-musin-extension-delsarte-method-kissing_images/imageFile729.png>)

![image 730](<2005-musin-extension-delsarte-method-kissing_images/imageFile730.png>)

![image 731](<2005-musin-extension-delsarte-method-kissing_images/imageFile731.png>)

![image 732](<2005-musin-extension-delsarte-method-kissing_images/imageFile732.png>)

![image 733](<2005-musin-extension-delsarte-method-kissing_images/imageFile733.png>)

![image 734](<2005-musin-extension-delsarte-method-kissing_images/imageFile734.png>)

![image 735](<2005-musin-extension-delsarte-method-kissing_images/imageFile735.png>)

![image 736](<2005-musin-extension-delsarte-method-kissing_images/imageFile736.png>)

![image 737](<2005-musin-extension-delsarte-method-kissing_images/imageFile737.png>)

![image 738](<2005-musin-extension-delsarte-method-kissing_images/imageFile738.png>)

![image 739](<2005-musin-extension-delsarte-method-kissing_images/imageFile739.png>)

![image 740](<2005-musin-extension-delsarte-method-kissing_images/imageFile740.png>)

![image 741](<2005-musin-extension-delsarte-method-kissing_images/imageFile741.png>)

![image 742](<2005-musin-extension-delsarte-method-kissing_images/imageFile742.png>)

![image 743](<2005-musin-extension-delsarte-method-kissing_images/imageFile743.png>)

![image 744](<2005-musin-extension-delsarte-method-kissing_images/imageFile744.png>)

![image 745](<2005-musin-extension-delsarte-method-kissing_images/imageFile745.png>)

![image 746](<2005-musin-extension-delsarte-method-kissing_images/imageFile746.png>)

![image 747](<2005-musin-extension-delsarte-method-kissing_images/imageFile747.png>)

![image 748](<2005-musin-extension-delsarte-method-kissing_images/imageFile748.png>)

![image 749](<2005-musin-extension-delsarte-method-kissing_images/imageFile749.png>)

![image 750](<2005-musin-extension-delsarte-method-kissing_images/imageFile750.png>)

![image 751](<2005-musin-extension-delsarte-method-kissing_images/imageFile751.png>)

![image 752](<2005-musin-extension-delsarte-method-kissing_images/imageFile752.png>)

![image 753](<2005-musin-extension-delsarte-method-kissing_images/imageFile753.png>)

![image 754](<2005-musin-extension-delsarte-method-kissing_images/imageFile754.png>)

![image 755](<2005-musin-extension-delsarte-method-kissing_images/imageFile755.png>)

![image 756](<2005-musin-extension-delsarte-method-kissing_images/imageFile756.png>)

![image 757](<2005-musin-extension-delsarte-method-kissing_images/imageFile757.png>)

![image 758](<2005-musin-extension-delsarte-method-kissing_images/imageFile758.png>)

![image 759](<2005-musin-extension-delsarte-method-kissing_images/imageFile759.png>)

![image 760](<2005-musin-extension-delsarte-method-kissing_images/imageFile760.png>)

![image 761](<2005-musin-extension-delsarte-method-kissing_images/imageFile761.png>)

![image 762](<2005-musin-extension-delsarte-method-kissing_images/imageFile762.png>)

![image 763](<2005-musin-extension-delsarte-method-kissing_images/imageFile763.png>)

![image 764](<2005-musin-extension-delsarte-method-kissing_images/imageFile764.png>)

![image 765](<2005-musin-extension-delsarte-method-kissing_images/imageFile765.png>)

![image 766](<2005-musin-extension-delsarte-method-kissing_images/imageFile766.png>)

![image 767](<2005-musin-extension-delsarte-method-kissing_images/imageFile767.png>)

![image 768](<2005-musin-extension-delsarte-method-kissing_images/imageFile768.png>)

![image 769](<2005-musin-extension-delsarte-method-kissing_images/imageFile769.png>)

![image 770](<2005-musin-extension-delsarte-method-kissing_images/imageFile770.png>)

![image 771](<2005-musin-extension-delsarte-method-kissing_images/imageFile771.png>)

![image 772](<2005-musin-extension-delsarte-method-kissing_images/imageFile772.png>)

![image 773](<2005-musin-extension-delsarte-method-kissing_images/imageFile773.png>)

![image 774](<2005-musin-extension-delsarte-method-kissing_images/imageFile774.png>)

![image 775](<2005-musin-extension-delsarte-method-kissing_images/imageFile775.png>)

![image 776](<2005-musin-extension-delsarte-method-kissing_images/imageFile776.png>)

![image 777](<2005-musin-extension-delsarte-method-kissing_images/imageFile777.png>)

![image 778](<2005-musin-extension-delsarte-method-kissing_images/imageFile778.png>)

![image 779](<2005-musin-extension-delsarte-method-kissing_images/imageFile779.png>)

![image 780](<2005-musin-extension-delsarte-method-kissing_images/imageFile780.png>)

![image 781](<2005-musin-extension-delsarte-method-kissing_images/imageFile781.png>)

![image 782](<2005-musin-extension-delsarte-method-kissing_images/imageFile782.png>)

![image 783](<2005-musin-extension-delsarte-method-kissing_images/imageFile783.png>)

![image 784](<2005-musin-extension-delsarte-method-kissing_images/imageFile784.png>)

![image 785](<2005-musin-extension-delsarte-method-kissing_images/imageFile785.png>)

![image 786](<2005-musin-extension-delsarte-method-kissing_images/imageFile786.png>)

![image 787](<2005-musin-extension-delsarte-method-kissing_images/imageFile787.png>)

![image 788](<2005-musin-extension-delsarte-method-kissing_images/imageFile788.png>)

![image 789](<2005-musin-extension-delsarte-method-kissing_images/imageFile789.png>)

![image 790](<2005-musin-extension-delsarte-method-kissing_images/imageFile790.png>)

![image 791](<2005-musin-extension-delsarte-method-kissing_images/imageFile791.png>)

![image 792](<2005-musin-extension-delsarte-method-kissing_images/imageFile792.png>)

![image 793](<2005-musin-extension-delsarte-method-kissing_images/imageFile793.png>)

![image 794](<2005-musin-extension-delsarte-method-kissing_images/imageFile794.png>)

![image 795](<2005-musin-extension-delsarte-method-kissing_images/imageFile795.png>)

![image 796](<2005-musin-extension-delsarte-method-kissing_images/imageFile796.png>)

![image 797](<2005-musin-extension-delsarte-method-kissing_images/imageFile797.png>)

![image 798](<2005-musin-extension-delsarte-method-kissing_images/imageFile798.png>)

![image 799](<2005-musin-extension-delsarte-method-kissing_images/imageFile799.png>)

![image 800](<2005-musin-extension-delsarte-method-kissing_images/imageFile800.png>)

![image 801](<2005-musin-extension-delsarte-method-kissing_images/imageFile801.png>)

![image 802](<2005-musin-extension-delsarte-method-kissing_images/imageFile802.png>)

![image 803](<2005-musin-extension-delsarte-method-kissing_images/imageFile803.png>)

![image 804](<2005-musin-extension-delsarte-method-kissing_images/imageFile804.png>)

![image 805](<2005-musin-extension-delsarte-method-kissing_images/imageFile805.png>)

![image 806](<2005-musin-extension-delsarte-method-kissing_images/imageFile806.png>)

![image 807](<2005-musin-extension-delsarte-method-kissing_images/imageFile807.png>)

![image 808](<2005-musin-extension-delsarte-method-kissing_images/imageFile808.png>)

![image 809](<2005-musin-extension-delsarte-method-kissing_images/imageFile809.png>)

![image 810](<2005-musin-extension-delsarte-method-kissing_images/imageFile810.png>)

![image 811](<2005-musin-extension-delsarte-method-kissing_images/imageFile811.png>)

![image 812](<2005-musin-extension-delsarte-method-kissing_images/imageFile812.png>)

![image 813](<2005-musin-extension-delsarte-method-kissing_images/imageFile813.png>)

![image 814](<2005-musin-extension-delsarte-method-kissing_images/imageFile814.png>)

![image 815](<2005-musin-extension-delsarte-method-kissing_images/imageFile815.png>)

![image 816](<2005-musin-extension-delsarte-method-kissing_images/imageFile816.png>)

![image 817](<2005-musin-extension-delsarte-method-kissing_images/imageFile817.png>)

![image 818](<2005-musin-extension-delsarte-method-kissing_images/imageFile818.png>)

![image 819](<2005-musin-extension-delsarte-method-kissing_images/imageFile819.png>)

![image 820](<2005-musin-extension-delsarte-method-kissing_images/imageFile820.png>)

![image 821](<2005-musin-extension-delsarte-method-kissing_images/imageFile821.png>)

![image 822](<2005-musin-extension-delsarte-method-kissing_images/imageFile822.png>)

![image 823](<2005-musin-extension-delsarte-method-kissing_images/imageFile823.png>)

![image 824](<2005-musin-extension-delsarte-method-kissing_images/imageFile824.png>)

![image 825](<2005-musin-extension-delsarte-method-kissing_images/imageFile825.png>)

![image 826](<2005-musin-extension-delsarte-method-kissing_images/imageFile826.png>)

![image 827](<2005-musin-extension-delsarte-method-kissing_images/imageFile827.png>)

![image 828](<2005-musin-extension-delsarte-method-kissing_images/imageFile828.png>)

![image 829](<2005-musin-extension-delsarte-method-kissing_images/imageFile829.png>)

![image 830](<2005-musin-extension-delsarte-method-kissing_images/imageFile830.png>)

![image 831](<2005-musin-extension-delsarte-method-kissing_images/imageFile831.png>)

![image 832](<2005-musin-extension-delsarte-method-kissing_images/imageFile832.png>)

![image 833](<2005-musin-extension-delsarte-method-kissing_images/imageFile833.png>)

![image 834](<2005-musin-extension-delsarte-method-kissing_images/imageFile834.png>)

![image 835](<2005-musin-extension-delsarte-method-kissing_images/imageFile835.png>)

![image 836](<2005-musin-extension-delsarte-method-kissing_images/imageFile836.png>)

![image 837](<2005-musin-extension-delsarte-method-kissing_images/imageFile837.png>)

![image 838](<2005-musin-extension-delsarte-method-kissing_images/imageFile838.png>)

![image 839](<2005-musin-extension-delsarte-method-kissing_images/imageFile839.png>)

![image 840](<2005-musin-extension-delsarte-method-kissing_images/imageFile840.png>)

![image 841](<2005-musin-extension-delsarte-method-kissing_images/imageFile841.png>)

![image 842](<2005-musin-extension-delsarte-method-kissing_images/imageFile842.png>)

![image 843](<2005-musin-extension-delsarte-method-kissing_images/imageFile843.png>)

![image 844](<2005-musin-extension-delsarte-method-kissing_images/imageFile844.png>)

![image 845](<2005-musin-extension-delsarte-method-kissing_images/imageFile845.png>)

![image 846](<2005-musin-extension-delsarte-method-kissing_images/imageFile846.png>)

![image 847](<2005-musin-extension-delsarte-method-kissing_images/imageFile847.png>)

![image 848](<2005-musin-extension-delsarte-method-kissing_images/imageFile848.png>)

![image 849](<2005-musin-extension-delsarte-method-kissing_images/imageFile849.png>)

![image 850](<2005-musin-extension-delsarte-method-kissing_images/imageFile850.png>)

![image 851](<2005-musin-extension-delsarte-method-kissing_images/imageFile851.png>)

![image 852](<2005-musin-extension-delsarte-method-kissing_images/imageFile852.png>)

![image 853](<2005-musin-extension-delsarte-method-kissing_images/imageFile853.png>)

![image 854](<2005-musin-extension-delsarte-method-kissing_images/imageFile854.png>)

![image 855](<2005-musin-extension-delsarte-method-kissing_images/imageFile855.png>)

![image 856](<2005-musin-extension-delsarte-method-kissing_images/imageFile856.png>)

![image 857](<2005-musin-extension-delsarte-method-kissing_images/imageFile857.png>)

![image 858](<2005-musin-extension-delsarte-method-kissing_images/imageFile858.png>)

![image 859](<2005-musin-extension-delsarte-method-kissing_images/imageFile859.png>)

![image 860](<2005-musin-extension-delsarte-method-kissing_images/imageFile860.png>)

![image 861](<2005-musin-extension-delsarte-method-kissing_images/imageFile861.png>)

![image 862](<2005-musin-extension-delsarte-method-kissing_images/imageFile862.png>)

![image 863](<2005-musin-extension-delsarte-method-kissing_images/imageFile863.png>)

![image 864](<2005-musin-extension-delsarte-method-kissing_images/imageFile864.png>)

![image 865](<2005-musin-extension-delsarte-method-kissing_images/imageFile865.png>)

![image 866](<2005-musin-extension-delsarte-method-kissing_images/imageFile866.png>)

![image 867](<2005-musin-extension-delsarte-method-kissing_images/imageFile867.png>)

![image 868](<2005-musin-extension-delsarte-method-kissing_images/imageFile868.png>)

![image 869](<2005-musin-extension-delsarte-method-kissing_images/imageFile869.png>)

![image 870](<2005-musin-extension-delsarte-method-kissing_images/imageFile870.png>)

![image 871](<2005-musin-extension-delsarte-method-kissing_images/imageFile871.png>)

![image 872](<2005-musin-extension-delsarte-method-kissing_images/imageFile872.png>)

![image 873](<2005-musin-extension-delsarte-method-kissing_images/imageFile873.png>)

![image 874](<2005-musin-extension-delsarte-method-kissing_images/imageFile874.png>)

![image 875](<2005-musin-extension-delsarte-method-kissing_images/imageFile875.png>)

![image 876](<2005-musin-extension-delsarte-method-kissing_images/imageFile876.png>)

![image 877](<2005-musin-extension-delsarte-method-kissing_images/imageFile877.png>)

![image 878](<2005-musin-extension-delsarte-method-kissing_images/imageFile878.png>)

![image 879](<2005-musin-extension-delsarte-method-kissing_images/imageFile879.png>)

![image 880](<2005-musin-extension-delsarte-method-kissing_images/imageFile880.png>)

![image 881](<2005-musin-extension-delsarte-method-kissing_images/imageFile881.png>)

![image 882](<2005-musin-extension-delsarte-method-kissing_images/imageFile882.png>)

![image 883](<2005-musin-extension-delsarte-method-kissing_images/imageFile883.png>)

![image 884](<2005-musin-extension-delsarte-method-kissing_images/imageFile884.png>)

![image 885](<2005-musin-extension-delsarte-method-kissing_images/imageFile885.png>)

![image 886](<2005-musin-extension-delsarte-method-kissing_images/imageFile886.png>)

![image 887](<2005-musin-extension-delsarte-method-kissing_images/imageFile887.png>)

![image 888](<2005-musin-extension-delsarte-method-kissing_images/imageFile888.png>)

![image 889](<2005-musin-extension-delsarte-method-kissing_images/imageFile889.png>)

![image 890](<2005-musin-extension-delsarte-method-kissing_images/imageFile890.png>)

![image 891](<2005-musin-extension-delsarte-method-kissing_images/imageFile891.png>)

![image 892](<2005-musin-extension-delsarte-method-kissing_images/imageFile892.png>)

![image 893](<2005-musin-extension-delsarte-method-kissing_images/imageFile893.png>)

![image 894](<2005-musin-extension-delsarte-method-kissing_images/imageFile894.png>)

![image 895](<2005-musin-extension-delsarte-method-kissing_images/imageFile895.png>)

![image 896](<2005-musin-extension-delsarte-method-kissing_images/imageFile896.png>)

![image 897](<2005-musin-extension-delsarte-method-kissing_images/imageFile897.png>)

![image 898](<2005-musin-extension-delsarte-method-kissing_images/imageFile898.png>)

![image 899](<2005-musin-extension-delsarte-method-kissing_images/imageFile899.png>)

![image 900](<2005-musin-extension-delsarte-method-kissing_images/imageFile900.png>)

![image 901](<2005-musin-extension-delsarte-method-kissing_images/imageFile901.png>)

![image 902](<2005-musin-extension-delsarte-method-kissing_images/imageFile902.png>)

−1 −0.5 0 0.5 0.8

0

Fig. 2. The graph of the function f(t)

✁

✁

✁

✁

✁

✁

✁

✁

❆

❆

❆

❆

❆

❆

❆

❆ ϕ

![image 903](<2005-musin-extension-delsarte-method-kissing_images/imageFile903.png>)

![image 904](<2005-musin-extension-delsarte-method-kissing_images/imageFile904.png>)

![image 905](<2005-musin-extension-delsarte-method-kissing_images/imageFile905.png>)

![image 906](<2005-musin-extension-delsarte-method-kissing_images/imageFile906.png>)

![image 907](<2005-musin-extension-delsarte-method-kissing_images/imageFile907.png>)

![image 908](<2005-musin-extension-delsarte-method-kissing_images/imageFile908.png>)

![image 909](<2005-musin-extension-delsarte-method-kissing_images/imageFile909.png>)

![image 910](<2005-musin-extension-delsarte-method-kissing_images/imageFile910.png>)

![image 911](<2005-musin-extension-delsarte-method-kissing_images/imageFile911.png>)

![image 912](<2005-musin-extension-delsarte-method-kissing_images/imageFile912.png>)

![image 913](<2005-musin-extension-delsarte-method-kissing_images/imageFile913.png>)

![image 914](<2005-musin-extension-delsarte-method-kissing_images/imageFile914.png>)

![image 915](<2005-musin-extension-delsarte-method-kissing_images/imageFile915.png>)

![image 916](<2005-musin-extension-delsarte-method-kissing_images/imageFile916.png>)

![image 917](<2005-musin-extension-delsarte-method-kissing_images/imageFile917.png>)

![image 918](<2005-musin-extension-delsarte-method-kissing_images/imageFile918.png>)

![image 919](<2005-musin-extension-delsarte-method-kissing_images/imageFile919.png>)

![image 920](<2005-musin-extension-delsarte-method-kissing_images/imageFile920.png>)

![image 921](<2005-musin-extension-delsarte-method-kissing_images/imageFile921.png>)

![image 922](<2005-musin-extension-delsarte-method-kissing_images/imageFile922.png>)

![image 923](<2005-musin-extension-delsarte-method-kissing_images/imageFile923.png>)

![image 924](<2005-musin-extension-delsarte-method-kissing_images/imageFile924.png>)

![image 925](<2005-musin-extension-delsarte-method-kissing_images/imageFile925.png>)

![image 926](<2005-musin-extension-delsarte-method-kissing_images/imageFile926.png>)

![image 927](<2005-musin-extension-delsarte-method-kissing_images/imageFile927.png>)

![image 928](<2005-musin-extension-delsarte-method-kissing_images/imageFile928.png>)

![image 929](<2005-musin-extension-delsarte-method-kissing_images/imageFile929.png>)

![image 930](<2005-musin-extension-delsarte-method-kissing_images/imageFile930.png>)

![image 931](<2005-musin-extension-delsarte-method-kissing_images/imageFile931.png>)

![image 932](<2005-musin-extension-delsarte-method-kissing_images/imageFile932.png>)

![image 933](<2005-musin-extension-delsarte-method-kissing_images/imageFile933.png>)

![image 934](<2005-musin-extension-delsarte-method-kissing_images/imageFile934.png>)

![image 935](<2005-musin-extension-delsarte-method-kissing_images/imageFile935.png>)

![image 936](<2005-musin-extension-delsarte-method-kissing_images/imageFile936.png>)

![image 937](<2005-musin-extension-delsarte-method-kissing_images/imageFile937.png>)

![image 938](<2005-musin-extension-delsarte-method-kissing_images/imageFile938.png>)

![image 939](<2005-musin-extension-delsarte-method-kissing_images/imageFile939.png>)

![image 940](<2005-musin-extension-delsarte-method-kissing_images/imageFile940.png>)

![image 941](<2005-musin-extension-delsarte-method-kissing_images/imageFile941.png>)

![image 942](<2005-musin-extension-delsarte-method-kissing_images/imageFile942.png>)

![image 943](<2005-musin-extension-delsarte-method-kissing_images/imageFile943.png>)

![image 944](<2005-musin-extension-delsarte-method-kissing_images/imageFile944.png>)

![image 945](<2005-musin-extension-delsarte-method-kissing_images/imageFile945.png>)

![image 946](<2005-musin-extension-delsarte-method-kissing_images/imageFile946.png>)

![image 947](<2005-musin-extension-delsarte-method-kissing_images/imageFile947.png>)

![image 948](<2005-musin-extension-delsarte-method-kissing_images/imageFile948.png>)

![image 949](<2005-musin-extension-delsarte-method-kissing_images/imageFile949.png>)

![image 950](<2005-musin-extension-delsarte-method-kissing_images/imageFile950.png>)

![image 951](<2005-musin-extension-delsarte-method-kissing_images/imageFile951.png>)

![image 952](<2005-musin-extension-delsarte-method-kissing_images/imageFile952.png>)

![image 953](<2005-musin-extension-delsarte-method-kissing_images/imageFile953.png>)

![image 954](<2005-musin-extension-delsarte-method-kissing_images/imageFile954.png>)

A

- B C


θ1 θ2

φ

Fig. 1

Proof of Lemma 1. This lemma easily follows from Schoenberg’s theorem [29] for Gegenbauer

polynomials. Note that Pk = G(3)k . For completeness we give a proof of Lemma 1 here. In this proof we are using original Schoenberg’s proof that based on the

addition theorem for Gegenbauer polynomials.1

The addition theorem for Legendre polynomials was discovered by Laplace and Legendre in 1782-1785:

Pk(cos θ1 cosθ2 + sinθ1 sinθ2 cosϕ) =

k

cm,k Pkm(cos θ1)Pkm(cosθ2) cosmϕ

m=0

k

(k − m)! (k + m)!

Pkm(cosθ1)Pkm(cosθ2) cosmϕ,

= Pk(cosθ1)Pk(cosθ2) + 2

![image 955](<2005-musin-extension-delsarte-method-kissing_images/imageFile955.png>)

m=1

![image 956](<2005-musin-extension-delsarte-method-kissing_images/imageFile956.png>)

1Pfender and Ziegler[28] give a proof as a simple consequence of the addition theorem for spherical harmonics. This theorem is not so elementary. The addition theorem for Legendre polynomials can be proven by elementary algebraic calculations.

where

dm dtm

m 2

Pkm(t) = (1 − t2)

Pk(t). (See details in [8, 16].)

![image 957](<2005-musin-extension-delsarte-method-kissing_images/imageFile957.png>)

![image 958](<2005-musin-extension-delsarte-method-kissing_images/imageFile958.png>)

Proof. Let X = {x1,...,xn} ⊂ S2 and xi has spherical (polar) coordinates (θi,ϕi). Then from the law of cosines we have:

cosφi,j = cosθi cosθj + sinθi sinθj cosϕi,j, ϕi,j = ϕi − ϕj, which yields

Pk(cosφi,j) =

i,j

k

cm,kPkm(cosθi)Pkm(cosθj)cosmϕi,j

m=0

i,j

=

m

cm,k

um,ium,j cosmϕi,j, um,i = Pkm(cosθi).

i,j

Let us prove that for any real u1,...,un

uiuj cosmϕi,j 0.

i,j

Pick n vectors y1,...,yn in R2 with coordinates yi = (cosmϕi,sinmϕi). If y = u1y1 + ... + unyn, then

< y,y > = ||y||2 =

uiuj cosmϕi,j 0.

i,j

This inequality and the inequalities cm,k > 0 complete our proof.

![image 959](<2005-musin-extension-delsarte-method-kissing_images/imageFile959.png>)

![image 960](<2005-musin-extension-delsarte-method-kissing_images/imageFile960.png>)

![image 961](<2005-musin-extension-delsarte-method-kissing_images/imageFile961.png>)

![image 962](<2005-musin-extension-delsarte-method-kissing_images/imageFile962.png>)

Proof of Lemma 2. Proof. The expansion of f in terms of Pk is

9

f =

ckPk = P0 + 1.6P1 + 3.48P2 + 1.65P3 + 1.96P4 + 0.1P5 + 0.32P9.

k=0

We have c0 = 1, ck 0, k = 1,2,...,9. Using Lemma 1 we get

9

S(X) =

ck

k=0

n

n

Pk(cos(φi,j))

i=1

j=1

n

n

c0P0 = n2.

i=1

j=1

![image 963](<2005-musin-extension-delsarte-method-kissing_images/imageFile963.png>)

![image 964](<2005-musin-extension-delsarte-method-kissing_images/imageFile964.png>)

![image 965](<2005-musin-extension-delsarte-method-kissing_images/imageFile965.png>)

![image 966](<2005-musin-extension-delsarte-method-kissing_images/imageFile966.png>)

Proof of Lemma 3. Proof. 1. The polynomial f(t) satisﬁes the following properties (see Fig.2):

- (i) f(t) is a monotone decreasing function on the interval [−1,−t0];
- (ii) f(t) < 0 for t ∈ (−t0,1/2]; where f(−t0) = 0, t0 ≈ 0.5907.


These properties hold because f(t) has the only one root −t0 on [−1,1/2], and there are no zeros of the derivative f′(t) (8th degree polynomial) on [−1,−t0].

Let Si(X) :=

n

f(cos(φi,j)), then S(X) =

j=1

n

Si(X). From this follows

i=1

if Si(X) < 13 for i = 1,2,...,n, then S(X) < 13n.

We obviously have φi,i = 0, so f(cosφi,i) = f(1). Note that our assumption on X (φi,j 60◦, i = j) yields cosφi,j 1/2. Therefore, cosφi,j lies in the interval [-1,1/2]. Since (ii), if cosφi,j ∈ [−t0,1/2], then f(cosφi,j) 0. Let J(i) := {j : cosφi,j ∈ [−1,−t0)}. We obtain

Si(X) Ti(X) := f(1) +

f(cosφi,j). (1)

j∈J(i)

Let θ0 = arccost0,θ0 ≈ 53.794◦. Then j ∈ J(i) iﬀ φi,j > 180◦ − θ0, i.e. θj < θ0, where θj = 180◦ − φi,j. In other words all xi,j, j ∈ J(i) lie inside the circle of center e0 and radius θ0, where e0 = −xi is the antipodal point to xi.

2. Let us consider on S2 points e0,y1,...,ym such that φi,j = dist(yi,yj) 60◦ for all i = j, dist(e0,yi) θ0 for 1 i m. (2)

Denote by µ the highest value of m such that the constraints in (2) deﬁne a non-empty set of points y1,...,ym.

Suppose 0 m µ and Y = {y1,...,ym} satisﬁes (2). Let

- H(Y ) = H(y1,...,ym) := f(1)+f(− cosθ1)+...+f(− cosθm), θi = dist(e0,yi)


hm := max

H(Y ), hmax := max{h0,h1,...,hµ}.

Y

It is clear that Ti(X) hm, where m = |J(i)|. From (1) it follows that Si(X) hm. Thus, if we prove that hmax < 13, then we prove Lemma 3.

3. Now we prove that µ 4. Suppose Y = {y1,...,ym} ⊂ S2 satisﬁes (2). If e0 is the North pole and yi has polar coordinates (θi,ϕi), then from the law of cosines we have:

cosφi,j = cosθi cosθj + sinθi sinθj cos(ϕi − ϕj). From (2) we have cosφi,j 1/2, then

cos(ϕi − ϕj)

1/2 − cosθi cosθj sinθi sinθj

. (3)

![image 967](<2005-musin-extension-delsarte-method-kissing_images/imageFile967.png>)

1/2 − cosαcosβ sinαsinβ

2 cosβ − cosα 2 sin2 α sinβ

, then Q′(α) =

Let Q(α) =

.

![image 968](<2005-musin-extension-delsarte-method-kissing_images/imageFile968.png>)

![image 969](<2005-musin-extension-delsarte-method-kissing_images/imageFile969.png>)

From this follows, if 0 < α,β θ0, then cosβ > 1/2 (because θ0 < 60◦); so then Q′(α) > 0, and Q(α) Q(θ0). Therefore,

1/2 − cosθi cosθj sinθi sinθj

![image 970](<2005-musin-extension-delsarte-method-kissing_images/imageFile970.png>)

1/2 − cos2 θ0 sin2 θ0

=

![image 971](<2005-musin-extension-delsarte-method-kissing_images/imageFile971.png>)

Combining this inequality and (3), we get

1/2 − t20 1 − t20

.

![image 972](<2005-musin-extension-delsarte-method-kissing_images/imageFile972.png>)

1/2 − t20 1 − t20

cos(ϕi − ϕj)

.

![image 973](<2005-musin-extension-delsarte-method-kissing_images/imageFile973.png>)

Note that arccos((1/2 − t20)/(1 − t20)) ≈ 76.582◦ > 72◦. Then m 4 because no more than four points can lie in an unit circle with the minimum angular separation between any two points greater than 72◦.

4. Now we have to prove that hmax = max{h0,h1,h2,h3,h4} < 13. We obviously have h0 = f(1) = 10.11 < 13.

From (i) follows that f(− cosθ) is a monotone decreasing function in θ on [0,θ0]. Then for m = 1 : H(y1) = f(1) + f(− cosθ1) attains its maximum at θ1 = 0,

h1 = f(1) + f(−1) = 12.88 < 13

5. Let us consider for m = 2,3,4 an optimal arrangement {e0,y1,...,ym} in S2 that gives maximum of H(Y ) = hm. Note that for optimal arrangement points yk cannot be shifted towards e0 because in this case H(Y ) increases.

- For m = 2 this yields: e0 ∈ y1y2, and dist(y1,y2) = 60◦. If e0 ∈/ y1y2, then

whole arc y1y2 can be shifted to e0. Also if dist(y1,y2) > 60◦, then y1 (and y2) can be shifted to e0.

- For m = 3 we prove that ∆3 = y1y2y3 is a spherical regular triangle with


edge length 60◦. As above, e0 ∈ ∆3, otherwise whole triangle can be shifted

- to e0. Suppose dist(y1,yi) > 60◦, i = 2,3, then dist(y1,e0) can be decreased. From this follows that for any yi at least one of the distances {dist(yi,yj)} is equal to 60◦. Therefore, at least two sides of ∆3 (say y1y2 and y1y3) have length 60◦. Also dist(y2,y3) = 60◦, conversely y3 (or y2, if e0 ∈ y1y3) can be rotated about y1 by a small angle towards e0 (Fig.3).


When m = 4 ﬁrst we prove that ∆4 = y1y2y3y4 is a convex quadrangle. Conversely, we may assume that y4 ∈ y1y2y3.

The great circle that is orthogonal to the arc e0y4 divides S2 into two hemispheres: H1 and H2. Suppose e0 ∈ H1, then at least one yi (say y3) belongs H2 (Fig.4). So the angle ∠e0y4y3 greater than 90◦, then (again from the law of cosines) dist(y3,e0) > dist(y3,y4). Thus,

θ3 = dist(y3,e0) > dist(y3,y4) 60◦ > θ0 − a contradiction.

Arguing as for m = 3 it is easy to prove that ∆4 is a spherical equilateral quadrangle (rhomb) with edge length 60◦.

![image 974](<2005-musin-extension-delsarte-method-kissing_images/imageFile974.png>)

![image 975](<2005-musin-extension-delsarte-method-kissing_images/imageFile975.png>)

![image 976](<2005-musin-extension-delsarte-method-kissing_images/imageFile976.png>)

![image 977](<2005-musin-extension-delsarte-method-kissing_images/imageFile977.png>)

![image 978](<2005-musin-extension-delsarte-method-kissing_images/imageFile978.png>)

y3

- y3
- y4


♣♣♣♣♣♣♣♣♣♣♣ ☎

❏❏

✡✡

☎

e0 ❛❛❛❛❛❛❛❛❛

H2 H1

❏

✡

❅

☎

y3 y2 60◦ 60◦

e0

❏

✡

❅

☎

60◦ 60◦

θ3

yc e0

❏

✡

❅

☎

☞

❏

✡

❅

y1 ❵❵❵❵❵ y2

✏✏✏

θ1 θ2

y1

y1

❏

✡

y2

![image 979](<2005-musin-extension-delsarte-method-kissing_images/imageFile979.png>)

Fig. 5

Fig. 4

Fig. 3

![image 980](<2005-musin-extension-delsarte-method-kissing_images/imageFile980.png>)

6. Now we introduce the function F1(ψ),2 where ψ ∈ [60◦,2θ0]: F1(ψ) := max

{ F1(θ,ψ)}, F1(θ,ψ) = f(− cosθ) + f(− cos(ψ − θ)).

ψ/2 θ θ0

So if dist(yi,yj) = ψ, then

f(− cosθi) + f(− cosθj) F1(ψ). (4) Therefore,

H(y1,y2) h2 = f(1) + F1(60◦) ≈ 12.8749 < 13.

7. When m = 4, ∆4 is a spherical rhomb. Let d1 = dist(y1,y3), and

d2 = dist(y2,y4), then cos(d1/2)cos(d2/2) = 1/2 (Pythagorean theorem, the diagonals of ∆4 are orthogonal). So if ρ(s) := 2 arccos[1/(2 cos(s/2))], then d1 = ρ(d2), d2 = ρ(d1), ρ(90◦) = 90◦.

Suppose d1 d2. Since θi θ0, d2 2θ0, then ρ(2θ0) d1 90◦ d2 2θ0.

Now we consider two cases:

1) ρ(2θ0) d1 < 77◦, and 2) 77◦ d1 90◦.

- 1) F1(ψ) is a monotone decreasing function in ψ. Then (4) implies f(− cosθ1) + f(− cosθ3) F1(ρ(2θ0)), f(− cosθ2) + f(− cosθ4) < F1(ρ(77◦)), so then

H(Y ) < f(1) + F1(ρ(2θ0)) + F1(ρ(77◦)) ≈ 12.9171 < 13.

- 2) In this case we have H(Y ) f(1) + F1(77◦) + F1(90◦) ≈ 12.9182 < 13.


Thus, h4 < 13.

8. Our last step is to show that h3 < 13.3

![image 981](<2005-musin-extension-delsarte-method-kissing_images/imageFile981.png>)

- 2For given ψ, the value F1(ψ) can be ﬁnd as the maximum of the 9th degree polynomial Ω(s) = F1(θ, ψ), s = cos (θ − ψ/2), on the interval [cos(θ0 − ψ/2), 1].
- 3More detailed analysis shows h3 ≈ 12.8721, h4 ≈ 12.4849.


Since ∆3 is a regular triangle, H(Y ) = f(1) + f(− cosθ1) + f(− cosθ2) + f(− cosθ3) is a symmetric function in θi, so we can consider only the case θ1 θ2 θ3 θ0. In this case R0 θ3 θ0, where R0 = arccos 2/3 ≈ 35.2644◦. (Note that the circumradius of ∆3 equals R0.)

![image 982](<2005-musin-extension-delsarte-method-kissing_images/imageFile982.png>)

Let yc is the center of ∆3. Denote by u the angle ∠e0y3yc. Then (see Fig.5)

- cosθ1 = cos60◦ cosθ3 + sin60◦ sinθ3 cos(R0 − u),
- cosθ2 = cos60◦ cosθ3 + sin60◦ sinθ3 cos(R0 + u),


where ∠y1y3yc = ∠y2y3yc = R0, 0 u u0 = arccos(cotθ3/√3) − R0 (if u = u0, then θ2 = θ3).

![image 983](<2005-musin-extension-delsarte-method-kissing_images/imageFile983.png>)

For ﬁxed θ3 = ψ, H(y1,y2) becomes the polynomial of degree 9 in s = cosu. Denote by F2(ψ) the maximum of this polynomial on the interval [cosu0,1].

Let

{ψ1,...,ψ6} = {R0, 38◦, 41◦, 44◦, 48◦, θ0}.

It’s clear that F2(ψ) is a monotone increasing function in ψ on [R0,θ0]. From other side, f(− cosψ) is a monotone decreasing function in ψ. Therefore for θ3 ∈ [ψi,ψi+1] we have

H(Y ) = H(y1,y2) + f(− cosθ3) < wi := F2(ψi+1) + f(− cosψi). Since,

{w1,...,w5} ≈ {12.9425,12.9648,12.9508,12.9606,12.9519}, we get h3 < max{wi} < 13.

Thus, hm < 13 for all m as required.

![image 984](<2005-musin-extension-delsarte-method-kissing_images/imageFile984.png>)

![image 985](<2005-musin-extension-delsarte-method-kissing_images/imageFile985.png>)

![image 986](<2005-musin-extension-delsarte-method-kissing_images/imageFile986.png>)

![image 987](<2005-musin-extension-delsarte-method-kissing_images/imageFile987.png>)

### 3 Delsarte’s method

Let X = {x1,x2,...,xM} be any ﬁnite subset of the unit sphere Sn−1 ⊂ Rn, Sn−1 = {x : x ∈ Rn, x·x = ||x||2 = 1}. From here on we will speak of x ∈ Sn−1 alternatively of points in Sn−1 or of vectors in Rn.

By φij we denote the spherical (angular) distance between xi, xj. It is clear that for any real numbers u1,u2,...,uM the relation

|| uixi||2 =

cosφijuiuj ≥ 0

i,j

holds, or equivalently the Gram matrix T(X) is positive semideﬁnite, where T(X) = (tij), tij = cosφij = xi · xj.

Schoenberg [29] extended this property to Gegenbauer (ultraspherical) poly-

nomials G(kn) of tij. He proved that if gij = Gk(n)(tij), then the matrix (gij) is positive semideﬁnite. Schoenberg proved also that the converse holds: if f(t) is

a real polynomial and for any ﬁnite X ⊂ Sn−1 the matrix (f(tij)) is positive semideﬁnite, then f is a sum of Gk(n) with nonnegative coeﬃcients.

Let us recall the deﬁnition of Gegenbauer polynomials. Suppose Ck(n)(t) be the polynomials deﬁned by the expansion

(1 − 2rt + r2)1−n/2 =

∞

rkCk(n)(t).

k=0

Then the polynomials G(kn)(t) = Ck(n)(t)/Ck(n)(1) are called Gegenbauer or ultraspherical polynomials. (So the normalization of Gk(n) is determined by the condition G(kn)(1) = 1.)

Also the Gegenbauer polynomials Gk(n) can be deﬁned by recurrence formula:

(2k + n − 4)tGk(n−)1 − (k − 1)Gk(n−)2 k + n − 3

G(0n) = 1, G(1n) = t, ..., Gk(n) =

![image 988](<2005-musin-extension-delsarte-method-kissing_images/imageFile988.png>)

They are orthogonal on the interval [−1,1] with respect to the weight function ρ(t) = (1−t2)(n−3)/2 (see details in [8, 10, 16, 29]). In the case n = 3, Gk(n) are Legendre polynomials Pk, and G(4)k are Chebyshev polynomials of the second kind (but with a diﬀerent normalization than usual, Uk(1) = 1),

sin((k + 1)φ) (k + 1)sinφ

G(4)k (t) = Uk(t) =

, t = cosφ, k = 0,1,2,...

![image 989](<2005-musin-extension-delsarte-method-kissing_images/imageFile989.png>)

For instance, U0 = 1, U1 = t, U2 = (4t2 − 1)/3, U3 = 2t3 − t, U4 = (16t4 − 12t2 + 1)/5, ..., U9 = (256t9 − 512t7 + 336t5 − 80t3 + 5t)/5.

Let us now prove the bound of Delsarte’s method. If a matrix (gij) is positive semideﬁnite, then for any real ui the inequality gijuiuj 0 holds, and then for ui = 1, we have

gij ≥ 0. Therefore, for gij = Gk(n)(tij), we obtain

i,j

M

M

Gk(n)(tij) 0 (3.1)

i=1

j=1

Suppose

f(t) = c0G(0n)(t) + ... + cdGd(n)(t), where c0 0,..., cd 0. (3.2) Let S(X) =

f(tij). Using (3.1), we get

i j

d

M

S(X) =

i=1

k=0

M

ckGk(n)(tij)

j=1

M

M

c0G0(n)(tij) = c0M2. (3.3)

i=1

j=1

Let X = {x0,...,xM} ⊂ Sn−1 be a spherical z-code, i.e. for all i = j, tij = cosφij = xi · xj z, i.e. tij ∈ [−1,z] (but tii = 1). Suppose f(t) 0 for

t ∈ [−1,z], then S(X) = Mf(1)+ 2f(t12) + ... + 2f(tM−1M) Mf(1). If we combine this with (3.2), then for c0 > 0 we get

M

f(1) c0

![image 990](<2005-musin-extension-delsarte-method-kissing_images/imageFile990.png>)

(3.4)

The inequality (3.4) play a crucial role in the Delsarte method (see details in [3, 4, 5, 10, 14, 15, 22, 24, 27]). If z = 1/2 and c0 = 1, then (3.4) implies k(n)

f(1). In [24, 27] Levenshtein, Odlyzko and Sloane have found the polynomials f(t) such that f(1) = 240, when n = 8; and f(1) = 196 560, when n = 24. Then k(8) 240, k(24) 196 560. When n = 8,24, there exist sphere packings (E8 and Leech lattices) with these kissing numbers. Thus k(8) = 240 and k(24) = 196 560. When n = 4, a polynomial f of degree 9 with f(1) = 25.5585... was found in [27]. This implies 24 k(4) 25.

### 4 An extension of Delsarte’s method.

Let us now generalize the Delsarte bound M f(1)/c0. Deﬁnition. Let f(t) be any function on the interval [−1,1]. Consider on Sn−1 points y0,y1,...,ym such that

yi · yj z for all i = j, f(y0 · yi) > 0 for 1 i m. (4.1) Denote by µ = µ(n,z,f) the highest value of m such that the constraints in

(4.1) deﬁne a non-empty set of points (y0,...,ym). Suppose 0 m µ. Let

H(Y ) = H(y0;y1,...,ym) := f(1) + f(y0 · y1) + ... + f(y0 · ym), hm := max

{H(Y )}, hmax := max {h0,h1,...,hµ}.

Y

Remark. hmax depends on n, z, and f. Throughout this paper it is clear what f, n, and z are; so we denote by hmax the value hmax(n,z,f).

- Theorem 2. Suppose X ⊂ Sn−1 is a spherical z-code, |X| = M, and f(t) = c0G(0n)(t) + ... + cdGd(n)(t), where c0 > 0, c1 0,..., cd 0. Then


1 c0

hmax c0

max{h0,h1,...,hµ}. Proof. Since f satisﬁes (3.2), then (3.3) yields

=

M

![image 991](<2005-musin-extension-delsarte-method-kissing_images/imageFile991.png>)

![image 992](<2005-musin-extension-delsarte-method-kissing_images/imageFile992.png>)

S(X) c0M2. Let J(i) := {j : f(xi · xj) > 0, j = i}, and X(i) = {xj : j ∈ J(i)}. Then

M

f(xi · xj) = H(xi;X(i)) hmax,

f(xi · xj) f(1) +

Si(X) =

j=1

j∈J(i)

so then

M

Si(X) Mhmax.

S(X) =

i=1

We have c0M2 S(X) Mhmax, i.e. c0M hmax as required. Note that h0 = f(1). If f(t) 0 for all t ∈ [−1,z], then for a z-code X we

![image 993](<2005-musin-extension-delsarte-method-kissing_images/imageFile993.png>)

![image 994](<2005-musin-extension-delsarte-method-kissing_images/imageFile994.png>)

![image 995](<2005-musin-extension-delsarte-method-kissing_images/imageFile995.png>)

![image 996](<2005-musin-extension-delsarte-method-kissing_images/imageFile996.png>)

have µ = 0, i.e. hmax = h0 = f(1). Therefore, this theorem yields the Delsarte bound M f(1)/c0.

The problem of evaluating of hmax in general case looks even more complicated than the upper bound problem for spherical z-codes. It is not clear how to ﬁnd µ? Here we consider this problem only for a very restrictive class of functions f(t): f(t) 0 for t ∈ [−t0,z], t0 > z 0.

Let us denote by A(k,ω) the maximal number of points in a spherical s-code Ω ⊂ Sk−1 of minimal angle ω, cosω = s. (Note that A(n,60◦) is the kissing number k(n).)

- Theorem 3. Suppose Y = {y1,...,ym} is a spherical z-code in Sn−1, and points yi lie inside the sphere of center e0 and radius θ0, where t0 = cosθ0 z. Then


z − t20 1 − t20

m A n − 1,arccos

.

![image 997](<2005-musin-extension-delsarte-method-kissing_images/imageFile997.png>)

Proof. We have φi,j = dist(yi,yj) δ = arccosz for i = j; θi = arccos(e0 · yi) θ0 for 1 i m; and θ0 δ.

Let Π be the projection of Y onto equator Sn−2 from pole e0. Denote by γi,j the distances between points of Π in Sn−2. Then from the law of cosines and the inequality cosφi,j z, we get

cosφi,j − cosθi cosθj sinθi sinθj

cosγi,j =

![image 998](<2005-musin-extension-delsarte-method-kissing_images/imageFile998.png>)

z − cosθi cosθj sinθi sinθj

![image 999](<2005-musin-extension-delsarte-method-kissing_images/imageFile999.png>)

z − cosαcosβ sinαsinβ

cosβ − z cosα sin2 αsinβ

, then Q′(α) =

Let Q(α) =

.

![image 1000](<2005-musin-extension-delsarte-method-kissing_images/imageFile1000.png>)

![image 1001](<2005-musin-extension-delsarte-method-kissing_images/imageFile1001.png>)

From this follows, if 0 < α,β θ0, then cosβ z (because θ0 δ); so then Q′(α) 0, and Q(α) Q(θ0). Therefore,

cosγi,j

z − cosθi cosθj sinθi sinθj

![image 1002](<2005-musin-extension-delsarte-method-kissing_images/imageFile1002.png>)

that complete our proof.

z − cos2 θ0 sin2 θ0

=

![image 1003](<2005-musin-extension-delsarte-method-kissing_images/imageFile1003.png>)

z − t20 1 − t20

![image 1004](<2005-musin-extension-delsarte-method-kissing_images/imageFile1004.png>)

![image 1005](<2005-musin-extension-delsarte-method-kissing_images/imageFile1005.png>)

![image 1006](<2005-musin-extension-delsarte-method-kissing_images/imageFile1006.png>)

![image 1007](<2005-musin-extension-delsarte-method-kissing_images/imageFile1007.png>)

![image 1008](<2005-musin-extension-delsarte-method-kissing_images/imageFile1008.png>)

- Corollary 1. Suppose f(t) 0 for t ∈ [−t0,z], t0 z 0, then


z − t20 1 − t20

µ(n,z,f) A n − 1,arccos

.

![image 1009](<2005-musin-extension-delsarte-method-kissing_images/imageFile1009.png>)

Proof. The assumption on f yields f(y0 · yi) > 0 only if θi = dist(e0,yi) < θ0 = arccost0,

where e0 = −y0 is the antipodal point to y0. Therefore, this set of points {e0,y1,...,ym} satisﬁes the assumptions in Theorem 3.

![image 1010](<2005-musin-extension-delsarte-method-kissing_images/imageFile1010.png>)

![image 1011](<2005-musin-extension-delsarte-method-kissing_images/imageFile1011.png>)

![image 1012](<2005-musin-extension-delsarte-method-kissing_images/imageFile1012.png>)

![image 1013](<2005-musin-extension-delsarte-method-kissing_images/imageFile1013.png>)

The next claim will be applied to prove that k(4) = 24.

- Corollary 2. Suppose f(t) 0 for t ∈ [−t0,1/2], t0 0.6058, then µ = µ(4,1/2,f) 6.


Proof. Note that for t0 0.6058, arccos[(1/2 − t20)/(1 − t20)] > 77.87◦. So Corollary 1 implies µ(4,1/2,f) A(3,77.87◦).

Denote by ϕk(M) the largest angular separation that can be attained in a spherical code on Sk−1 containing M points. In three dimensions the best codes and the values ϕ3(M) presently known for M 12 and M = 24 (see [12, 17, 30]). For instance, Sch¨utte and van der Waerden [30] proved that ϕ3(5) = ϕ3(6) = 90◦ and ϕ3(7) ≈ 77.86954◦ (cosϕ3(7) = cot40◦ cot80◦).

Since 77.87◦ > ϕ3(7), then A(3,77.87◦) < 7, i.e. µ 6.

![image 1014](<2005-musin-extension-delsarte-method-kissing_images/imageFile1014.png>)

![image 1015](<2005-musin-extension-delsarte-method-kissing_images/imageFile1015.png>)

![image 1016](<2005-musin-extension-delsarte-method-kissing_images/imageFile1016.png>)

![image 1017](<2005-musin-extension-delsarte-method-kissing_images/imageFile1017.png>)

Corollary 1 shows that if t0 is close enough to 1, then µ is small enough. Then one gets relatively small - dimensional optimization problems for computation of numbers hm for small n. If additionally f(t) is a monotone decreasing function on [−1,−t0], then these problems can be reduced to low-dimensional optimization problems of a type that can be treated numerically.

### 5 Optimal sets for monotonic functions

In this section we consider f(t) that satisﬁes the monotonicity assumption: f(t) is a monotone decreasing function on the interval [−1,−t0], f(t) 0 for t ∈ [−t0,z], t0 > z 0 (∗)

.

Consider on Sn−1 points y0,y1,...,ym that satisfy (4.1). Denote by θk for k > 0 the distance between yk and e0, where e0 = −y0 is the antipodal point to y0. Then y0 · yk = − cosθk, and H(Y ) is represented in the form:

H(Y ) = f(1) + f(− cosθ1) + ... + f(− cosθm). (5.1)

A subset C of Sn−1 is called (spherical) convex if it contains, with every two nonantipodal points, the small arc of the great circle containing them. If, in addition, C does not contain antipodal points, then C is called strongly convex. The closure of a convex set is convex and is the intersection of closed hemispheres (see details in [13]). If a subset Z of Sn−1 lies in a hemisphere, then the convex hull of Z is well deﬁned, and is the intersection of all convex sets containing Z.

Suppose f(t) satisﬁes (∗), then Qm = {y1,...,ym} lies in the hemisphere of center e0. Denote by ∆m the convex hull of Qm in Sn−1, ∆m = conv Qm.

Now we consider an optimal arrangement of Qm for H. Let δ = arccosz, φi,j = dist(yi,yj), N˜(Qm) = number of φi,j = δ (yi · yj = z). Deﬁnition We say that Qm is optimal if H(Y ) = hm. If optimal Qm is not unique up to isometry, then we call Qm as optimal if it has maximal N˜(Qm).

The function f(t) is monotone decreasing on [−1,−t0]. By (5.1) it follows that the function H(Y ) increases whenever θk decreases. This means that for an optimal Qm no yk ∈ Qm can be shifted towards e0.

That yields

e0 ∈ ∆m (5.2) because in the converse case whole Qm can be shifted to e0.

From this follows that for m = 1, e0 = y1. Thus h1 = f(1) + f(−1). It was proved in Section 2 that for m = 2 : dist(y1,y2) = δ, thus h2 = f(1) + max

{(f(− cosθ) + f(− cos(δ − θ))}, θ0 = arccost0.

δ/2 θ θ0

It was also proved that ∆3 is a spherical regular triangle with edge length δ. Using similar arguments it’s not hard to prove that for n > 3, ∆4 is a spherical regular tetrahedra with edge length δ. 4

Let ∆m, m n, is a spherical regular simplex with edge length δ, and

Ωm = {y : y ∈ ∆m, y · yk t0, 1 k m}. Note that Ωm is a convex set in Sn−1. Let

Hm(y) = f(1) + f(−y · y1) + ... + f(−y · ym). Then hm is the maximum of Hm(y) on Ωm.

Hm(y), Ωm ⊂ ∆m ⊂ Sn−1, 2 m min(n,µ). (5.3) When n > m any yk ∈ Qm is a vertex of ∆m. In other words, no yk that lies

hm = max y∈Λm

inside ∆m. In fact, that has been proved in Section 2 (see 5, Fig. 4).

In the ﬁrst version of the paper [26] has been claimed that for optimal Qm with m > n, for any yk ∈ Qm there are at least n − 1 distinct points in Qm at the distance of δ from yk.

However, Eiichi Bannai and Makoto Tagami found some gaps in our exposition. Most of them are related to “degenerated” conﬁgurations. In this paper we need only the case n = 4, m = 5. For this case they veriﬁed each step of our proof, considered all “degenerated” conﬁgurations, and ﬁnally gave clean and detailed proof. I wish to thank Eiichi Bannai and Makoto Tagami for this work. Now this claim in general case can be considered only as conjecture.

![image 1018](<2005-musin-extension-delsarte-method-kissing_images/imageFile1018.png>)

4For m n, ∆m is a spherical regular simplex with edge length δ. In this paper we need just cases m = 3, 4.

### 6 An algorithm for computation suitable polynomials f(t)

In this section is presented an algorithm for computation “optimal” 5 polynomials f such that f(t) is a monotone decreasing function on the interval [−1,−t0], and f(t) 0 for t ∈ [−t0,z], t0 > z 0. This algorithm based on our knowledge about optimal arrangement of points yi for given m. Coeﬃcients ck can be found via discretization and linear programming; such method had been employed already by Odlyzko and Sloane [27] for the same purpose.

d

ckGk(n)(t).

Let us have a polynomial f represented in the form f(t) = 1+

k=1

We have the following constraints for f: (C1) ck 0, 1 k d; (C2) f(a) > f(b) for −1 a < b −t0; (C3) f(t) 0 for −t0 t z.

When m n, hm = maxHm(y), y ∈ Λm. We do not know y where Hm attains its maximum, so for evaluation of hm let us use yc − the center of ∆m. All vertices yk of ∆m are at the distance of Rm from yc, where cosRm = (1 + (m − 1)z)/m.

![image 1019](<2005-musin-extension-delsarte-method-kissing_images/imageFile1019.png>)

When m = 2n − 2, ∆m presumably is a regular (n − 1)-dimensional crosspolytope. (It is not proven yet.) In this case cosRm = √z.

![image 1020](<2005-musin-extension-delsarte-method-kissing_images/imageFile1020.png>)

Let In = {1,...,n} {2n − 2}, m ∈ In, bm = − cosRm, whence

Hm(yc) = f(1) + mf(bm). If F0 is such that Hm(y) E = F0 + f(1), then (C4) f(bm) F0/m, m ∈ In. A polynomial f that satisﬁes (C1-C4) and gives the minimal E (note that E = F0 + 1 + c1 + ... + cd = F0 + f(1) will become a lower estimate of hmax) can be found by the following

Algorithm.

Input: n, z, t0, d, N. Output: c1,...,cd, F0, E.

First replace (C2) and (C3) by a ﬁnite set of inequalities at the points aj = −1 + ǫj, 0 j N, ǫ = (1 + z)/N :

Second use linear programming to ﬁnd F0,c1,...,cd so as to minimize E − 1 = F0 +

d

ck subject to the constraints

k=1

ck 0, 1 k d;

d

ckGk(n)(aj)

k=1

d

ckGk(n)(aj+1), aj ∈ [−1,−t0];

k=1

d

d

ckG(kn)(aj) 0, aj ∈ [−t0,z]; 1+

1+

k=1

k=1

ckGk(n)(bm) F0/m, m ∈ In.

Let us note again that E = max

Hm(yc) hmax here, and that E = hmax only if hmax = Hm

m∈In

(yc) for some m0 ∈ In.

0

![image 1021](<2005-musin-extension-delsarte-method-kissing_images/imageFile1021.png>)

5Open problem: is it true that for given t0, d this algorithm deﬁnes f with minimal hmax?

### 7 On calculations of hm for m n

Here we explain how to solve the optimization problem (5.3). Let ∆m ⊂ Sm−1 is a spherical regular simplex with edge length δ = arccosz; yi, i = 1,...,m, are the vertices of ∆m; ti = y · yi = cosθi t0 = cosθ0; t0 > z; f(t) is a monotone decreasing function on the interval [−1,−t0]; hm is the maximum of Hm(y) subject to the constraints ti t0; Hm(y) = f(1)+f(−y ·y1)+...+f(−y ·ym). The ﬁrst method.

Hm(y) is a symmetric function in the variables θ1,...,θm. Then we can consider this problem only on the domain Λ = {y : θm ... θ2 θ1}. Note that Λ is a spherical simplex. Let us consider a barycentric triangulation of this simplex such that the diameter of any simplex σi of this triangulation is not exceed ǫ.

It is easy to prove that for any yk, y ·yk attains its maximum on σi at some vertex of σi. Denote this vertex by yk,i. Let I = {i : y1,i · y1 t0}. So for i ∈ I we have

{f(−y · yk)}, then

f(−yk,i · yk) = max y∈σi

m

hm max

f(−yk,i · yk) .

i∈I

k=1

That yields a very simple method for calculation of hm. For f from Section 9 this method gives h3 ≈ 24.8345, h4 ≈ 24.818. The second method.

- For m n the values hm can be calculated another way. We are using here that f(t) = f0+f1t+...+fdtd is a polynomial. The ﬁrst method is technically easier then the second one. However, the second method doesn’t assume that f is a


monotone decreasing function on [−1,−t0], and it can be applied to functions without monotonicity assumption.

Let us consider Hm(y) as the symmetric polynomial Fm(t1,...,tm) in the variables ti = y · yi : Fm(t1,...,tm) = f(1) + f(−t1) + ... + f(−tm). Denote by sk = sk(t1,...,tm) the power sum tk1 + ... + tkm. Then

Fm(t1,...,tm) = Ψm(s1,...,sd) = f(1) + mf0 − f1 s1 + ... + (−1)dfd sd. From the fact that ∆m is a spherical regular simplex follows s2 = σ(s1) :=

z (m − 1)z + 1

s21 + 1 − z. (7.1)

![image 1022](<2005-musin-extension-delsarte-method-kissing_images/imageFile1022.png>)

Any symmetric polynomial in m variables can be expressed as a polynomial of s1,...,sm. Therefore, in the case k > m the power sum sk is Rk(s1,...,sm). Combining this with (7.1), we get

Ψm(s1,σ(s1),s3,...,sd) = Φm(s1,s3,...,sm). Therefore, we have

hm = max Φm(s1,s3,...,sm), (s1,s3,...,sm) ∈ Dm ⊂ Rm−1,

where Dm is the domain in Rm−1 deﬁned by the constraints ti t0 and (7.1).

Let us show now how to determine Dm for m > 2. The equation (7.1) deﬁnes the ellipsoid E : s2 = σ(s1) in space {t1,...,tm}. Then s1 = t1+...+tm attains its maximum on E at the point with t1 = t2 = ... = tm, and s1 achieves its minimum on E {ti t0} at the point with t2 = ... = tm = t0. From this follows w1 s1 w2, where

![image 1023](<2005-musin-extension-delsarte-method-kissing_images/imageFile1023.png>)

(p − t20)(p − z2) + z t0 p

1 + (m − 2)z m − 1

w1 =

+ (m − 1)t0, p =

,

![image 1024](<2005-musin-extension-delsarte-method-kissing_images/imageFile1024.png>)

![image 1025](<2005-musin-extension-delsarte-method-kissing_images/imageFile1025.png>)

![image 1026](<2005-musin-extension-delsarte-method-kissing_images/imageFile1026.png>)

w2 = m(m − 1)z + m.

The equation s1 = ω gives the hyperplane, and the equation s2 = σ(ω) gives the (m − 1)-sphere in space: {(t1,...,tm)}. Denote by S(ω) the (m − 2)sphere that is the intersection of these hyperplane and sphere. Let lk(ω) be the minimum of sk on S(ω) {ti t0}, and vk(ω) is its maximum. Now we have

Φm(s1,s3,...,sm), where w1 s1 w2, lk(s1) sk ≤ vk(s1), k = 3,...,m.

...max

max

hm = max

sm

s3

s1

For the polynomial f from Section 9 (and Section 2) we can give more details about calculations of hm for m = 3,4.

Let us consider the case m = 3 with d = 9. In this case Fω(s3) = Φ3(ω,s3) is a polynomial of degree 3 in the variable s3.

- Lemma 4. Let f be a 9th degree polynomial f(t) = f0 + f1t + ... + f9t9 such that f9 > 0, f6 = f8 = 0, and f7 > −15f9/7. If Fω′ (s) ≤ 0 at s = l3(ω), then the function Fω(s) achieves its maximum on the interval [l3(ω),v3(ω)] at s = l3(ω). Proof. The expansion of s9 in terms of si1sj2sk3, i + 2j + 3k = 9, is


- 2

![image 1027](<2005-musin-extension-delsarte-method-kissing_images/imageFile1027.png>)

- 3


3 8

3 8

- 7

![image 1028](<2005-musin-extension-delsarte-method-kissing_images/imageFile1028.png>)

- 8


5 24

1 9

s61) + R(s1,s2). The coeﬃcient of s23s1 in s7 equals 7/9. Thus

s33 + s23(

s31 + s2s1) + s3(

s32 −

s22s21 −

s2s41 +

s9 =

![image 1029](<2005-musin-extension-delsarte-method-kissing_images/imageFile1029.png>)

![image 1030](<2005-musin-extension-delsarte-method-kissing_images/imageFile1030.png>)

![image 1031](<2005-musin-extension-delsarte-method-kissing_images/imageFile1031.png>)

![image 1032](<2005-musin-extension-delsarte-method-kissing_images/imageFile1032.png>)

Fω(s) = −s3 f9/9 − s2 (f9 ω σ(ω) + 2f9 ω3/3 − 7f7 ω/9) + sR1(ω) + R0(ω).

Fω(s) is a cubic polynomial with negative coeﬃcient of s3. Then Fω(s) is a concave function for s > r, where r : Fω′′(r) = 0. Therefore, if r < l3(ω), then Fω(s) is a concave function on the interval [l3(ω),v3(ω)]. r < l3(ω) iﬀ

B(ω) := 3l3(ω) + 6ω3 + 9ω σ(ω) > −7ωf7/f9. This inequality holds for t0 < −z ≤ 0. Indeed,

ω w1 1 + 2z, σ (ω) ≥ 1, l3(ω) > 0; so then

B(ω) > 15ω > −7ωf7/f9.

The inequality Fω′ (l3(ω)) 0 implies that Fω(s) is a decreasing function on the interval [l3(ω),v3(ω)].

![image 1033](<2005-musin-extension-delsarte-method-kissing_images/imageFile1033.png>)

![image 1034](<2005-musin-extension-delsarte-method-kissing_images/imageFile1034.png>)

![image 1035](<2005-musin-extension-delsarte-method-kissing_images/imageFile1035.png>)

![image 1036](<2005-musin-extension-delsarte-method-kissing_images/imageFile1036.png>)

The polynomial f from Section 9 satisﬁes the assumptions in this lemma. Then Φ3(ω,s) attains its maximum at the point s = l3(ω), i.e. at the point with

- t1 = t2 t3, or with t1 t2 ≥ t3 = t0. If t1 = t2 t3, then p(ω) = Φ3(ω,l3(ω)) is a polynomial in ω. This polynomial is a decreasing function in the variable ω on the interval t3 t0. Therefore, p(ω) achieves its maximum on this interval at the point with t3 = t0. The calculations show that for f from Section 9


- h3 = maxp(ω) ≈ 24.8345, when θ3 = θ0, θ1 = θ2 ≈ 30.0715◦.

Corollary 3. Let f be the polynomial from Section 9, then h3 ≈ 24.8345.

Consider the function Fω(s3,s4) = Φ4(ω,s3,s4) on S(ω). Let qi ∈ S(ω) and q1 : t1 = t2 > t3 = t4, q2 : t1 = t2 = t3 > t4, and q3 : t1 > t2 = t3 = t4.

Lemma 5. Let f be a 9th degree polynomial f(t) = fiti. If f9 > 0 and f6 = f8 = 0, then the function Fω(s3,s4) achieves its maximum on S(ω) with ω > 1 at one of the points (s3(qi),s4(qi)), i = 1,2,3.

Proof. The expansion of s9 in terms of si1sj2sk3sl4 is s9 =

9 16

![image 1037](<2005-musin-extension-delsarte-method-kissing_images/imageFile1037.png>)

s24s1 +

1 9

![image 1038](<2005-musin-extension-delsarte-method-kissing_images/imageFile1038.png>)

s33 −

1 3

![image 1039](<2005-musin-extension-delsarte-method-kissing_images/imageFile1039.png>)

s23s31 +

- 3

![image 1040](<2005-musin-extension-delsarte-method-kissing_images/imageFile1040.png>)

- 4


s4s3s1 +

3 8

![image 1041](<2005-musin-extension-delsarte-method-kissing_images/imageFile1041.png>)

s4s2s31 −

3 8

![image 1042](<2005-musin-extension-delsarte-method-kissing_images/imageFile1042.png>)

s3s22s21 −

1 24

![image 1043](<2005-musin-extension-delsarte-method-kissing_images/imageFile1043.png>)

s3s61 +R(s1,s2).

The coeﬃcient of s23s1 in s7 equals 0. We have f6 = f8 = 0, then Fω(s3,s4) = −f9 s9 + ... = −f9(s33/9 − s23 ω3/3) + ... Therefore,

F33 =

∂2Fω(s3,s4) ∂2s3

![image 1044](<2005-musin-extension-delsarte-method-kissing_images/imageFile1044.png>)

= −f9(

- 2

![image 1045](<2005-musin-extension-delsarte-method-kissing_images/imageFile1045.png>)

- 3


s3 −

- 2

![image 1046](<2005-musin-extension-delsarte-method-kissing_images/imageFile1046.png>)

- 3


ω3) =

- 2f9

![image 1047](<2005-musin-extension-delsarte-method-kissing_images/imageFile1047.png>)

- 3


(ω3 − s3).

If Fω(s3,s4) has its maximum on S(ω) at the point x, and x is not a critical point of s3 on S(ω), then F33 ≤ 0. From other side, for all ti ∈ [0,1] and s1 = ω > 1 we have s3 ω < ω3, so then F33 > 0. The function s3 on S(ω) (up to permutation of labels) has critical points at qi, i = 1,2,3.

![image 1048](<2005-musin-extension-delsarte-method-kissing_images/imageFile1048.png>)

![image 1049](<2005-musin-extension-delsarte-method-kissing_images/imageFile1049.png>)

![image 1050](<2005-musin-extension-delsarte-method-kissing_images/imageFile1050.png>)

![image 1051](<2005-musin-extension-delsarte-method-kissing_images/imageFile1051.png>)

Corollary 4. Let f be the polynomial from Section 9, then h4 ≈ 24.818. Proof. By direct calculations it can be shown that Fω(s3(q1),s4(q1)) > Fω(s3(qi),s4(qi)) for i = 2,3. Then Lemma 5 implies

- h4 = maxp(ω), where p(ω) = Fω(s3(q1),s4(q1)) = Φ4(ω,s3(q1),s4(q1)). The polynomial p(ω) attains its maximum h4 ≈ 24.818 at the point with


θ1 = θ2 ≈ 30.2310◦, θ3 = θ4 ≈ 51.6765◦.

![image 1052](<2005-musin-extension-delsarte-method-kissing_images/imageFile1052.png>)

![image 1053](<2005-musin-extension-delsarte-method-kissing_images/imageFile1053.png>)

![image 1054](<2005-musin-extension-delsarte-method-kissing_images/imageFile1054.png>)

![image 1055](<2005-musin-extension-delsarte-method-kissing_images/imageFile1055.png>)

### 8 On calculations of h5 in four dimensions

Let us consider the case n = 4, m = 5. For simplicity here we consider only the case z = 1/2. Then δ = 60◦ and θ0 = arccost0 < 60◦.

Denote by Γ5 the graph of the edges of ∆5 with length 60◦ , where Q5 is an optimal set. The degree of any vertex of Γ5 is not less than 3 (see Section 5). This implies that at least one vertex of Γ5 has degree 4. Indeed, if all vertices of Γ5 are of degree 3, then the sum of the degrees equals 15, i.e. is not an even number. There exists only one type of Γ5 with these conditions (Fig. 6).

y1

✓

❉ ❉

![image 1056](<2005-musin-extension-delsarte-method-kissing_images/imageFile1056.png>)

y3

✓

✏✏✏✏✏✏

✁

✓

❉

y4

✁

✓

❉ ❉

✑

✁

✓

♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣❉♣ ♣

✑

✁

✓

✑

❉ ❉

✑

✁

✓

✑

α y5

✁

✓

✑

❉

❳❳❳❳❳❳❳❳

✁

❉

✁

y2

Fig. 6

For ﬁxed dist(y2,y4) = α, Q5 is uniquely deﬁned up to isometry. Therefore, we have the 1-parametric family ∆5(α) on S3. If dist(y3,y5) = β, then

2 cosα cosβ + cosα + cosβ = 0 (8.1) The equation (8.1) deﬁnes the function β = λ(α). Then α = λ(β), λ(90◦) = 90◦.

For all i we have dist(yi,e0) θ0, then dist(yi,yj) dist(yi,e0) + dist(yj,e0) 2θ0. Suppose α β, then (8.1) and the inequality β 2θ0 yield

α0 α 90◦ β 2θ0, α0 := max{60◦,λ(2θ0)}. Let

H5(y,α) = f(1) + f(−y · y1(α)) + ... + f(−y · y5(α)). Then

{H5(y,α)}, y ∈ S3, y ·yk(α) t0, 1 k 5, α0 α 90◦ (8.2)

h5 = max

y,α

We have four-dimensional optimization problem (8.2). Our ﬁrst approach for this problem was to apply numerical methods [25]. For the polynomial f from Section 9 this optimization problem was solved numerically by using the Nelder-Mead simplex method: H5(y,α) achieves its maximum h5 ≈ 24.6856 at α = 60◦ and y with θ1 ≈ 42.1569◦, θ2 = θ4 ≈ 32.3025◦, θ3 = θ5 = θ0. (The similar approach for the case n = 4, m = 6 gives the 3-parametric family ∆6(α,β,γ), and for f from Section 9: h6 ≈ 22.5205.)

Note that (8.2) is a nonconvex constrained optimization problem. In this case, the Nelder-Mead simplex method and other local improvements methods cannot guarantee ﬁnding a global optimum. It’s possible (using estimations of derivatives) to organize computational process in such way that it gives a global optimum. However, such kind solutions are very hard to verify and some mathematicians do not accept such kind proofs. Fortunately, an estimation of

- h5 can be reduced to discrete optimization problems.


Let dist(y1,y) = ψ, and Φi,j(y,ψ) = f(−y · yi) + f(−y · yj). It’s clear that for ﬁxed ψ, Φi,j(y,ψ) attains its maximum at some point that lies in the great 2-sphere that contains y1,yi,yj. Now we introduce the function F(ψ,γ).6 Suppose y1yiyj is a spherical triangle in S2 with dist(y1,yi) = dist(y1,yj) = 60◦, dist(yi,yj) = γ, denote by F(ψ,γ) the maximum of Φi,j(y,ψ) on S2 subject to the constraints y · yk t0, k = i,j. Then Φi,j(y,ψ) F(ψ,γ), so then Φ2,4(y,ψ) F(ψ,α), Φ3,5(y,ψ) F(ψ,β). Thus

h5 f(1) + f(− cosψ) + F(ψ,α) + F(ψ,λ(α)). (8.3)

Let α0 < α1 < ... < αk < αk+1 = 90◦. It’s easy to see that F(ψ,γ) is a monotone decreasing function in γ. That implies for α ∈ [αi,αi+1] : F(ψ,α) F(ψ,αi), F(ψ,λ(α)) F(ψ,λ(αi+1)). Therefore, from (8.3) follows

h5 f(1) + f(− cosψ) + max

{F(ψ,αi) + F(ψ,λ(αi+1))}. (8.4)

0 i k

Note that (8.4) to reduce the dimension of the optimization problem (8.1) from 4 to 2. It is not too hard to solve this problem in general case. However, the polynomial f from Section 9 satisﬁes an additional assumptions that allowed to ﬁnd a weak bound on h5 even more easier.

Let us brieﬂy explain how to check the following assumptions for f:

- 1) Φi,j(y,ψ) achieves its maximum at one of the ends of the arc ω(ψ,γ), where ω(ψ,γ) := {y : y ∈ S2, dist(y1,y) = ψ, y · yℓ t0, ℓ = i,j};
- 2) F(ψ,γ) is a monotone increasing function in ψ. For given γ (γ = dist(yi,yj)) and ψ the function Φi,j(y,ψ) becomes a poly-


nomial p(s) of degree d on [s0,1], where s = cosu, u = ∠yiy1yc, and yc is the center of y1yiyj (see Section 2, 8). Then 1) holds iﬀ p′(s) has no roots on (s0,1), either if s : p′(s) = 0, then p′′(s) > 0.

Using 1) it’s easy to check 2). For the polynomial f(t) from Section 9 if γ > 62.41◦, then p(s) achieves its maximum at s = s0 (i.e. dist(yj,y) = θ0), so it’s clear that 2) holds. From other side if γ < 69.34◦, then the arc ω(ψ,γ) lies inside the triangle y1yiyj, therefore F(ψ,γ) increases whenever ψ increases.

Note that 1) gives us the explicit expression for F(ψ,γ) = max(p(s0),p(1)). For ﬁxed γ and ψ ψℓ from 2) follows F(ψ,γ) F(ψℓ,γ).

Denote by ψL(i), ψU(i) the lower and upper bounds on ψ that deﬁned by the constraints α ∈ [αi,αi+1], y · yq t0, q = 1,...,5. Let ψL(i) = ψi,0 < ψi,1 < ... < ψi,ℓ < ψi,ℓ+1 = ψU(i). Recall that f(− cosψ) is a monotone decreasing function in ψ. Then 2) and (8.4) yield

{Ri,j}, (8.5) where

h5 f(1) + max

max

0 i k

0 j ℓ

Ri,j = f(− cosψi,j) + F(ψi,j+1,αi)} + F(ψi,j+1,λ(αi+1)).

It’s very easy to apply this method. Here we need just to calculate the matrix (Ri,j) and the maximal value of its entries gives the bound on h5. For

![image 1057](<2005-musin-extension-delsarte-method-kissing_images/imageFile1057.png>)

6F(ψ, 60◦) = F2(ψ) − f(1) (see Section 2, 8, Fig. 5).

f from Section 9 and t0 ≈ 0.60794, θ0 = arccost0 ≈ 52.5588◦, f(−t0) = 0, this method gives the bound h5 < 24.8434.7

Now we show how to ﬁnd an upper bound on h6. Let {e0,y1,...,y6} ∈ S3, H(y1,...,y6) = f(1) + f(− cosθ1) + ... + f(− cosθ6), where θi = dist(e0,yi). Suppose θ1 θ2 ... θ6. Now we prove that θ6 45◦. That can be proven as Corollary 2 (Section 4). Conversely, all θi < 45◦. In this case t0∗ = cosθ6 > 1/√2, and ω = arccos[(1/2 − t20∗)/(1 − t20∗)] > 90◦. But if

![image 1058](<2005-musin-extension-delsarte-method-kissing_images/imageFile1058.png>)

- u > 90◦, then A(3,ω) 4 (see [30, 17]) - a contradiction. (In fact we proved that θ5 45◦ also.)


Let us consider two cases: (i) θ0 θ6 > 50◦ (ii) 50◦ θ6 45◦.

- (i) H(y1,...,y6) = H(y1,...,y5) + f(− cosθ6). We have H(y1,...,y5) h5 < 24.8434, f(− cosθ6) < f(− cos50◦) ≈ 0.0906,

then H(y1,...,y6) < 24.934.

- (ii) In this case all θi 50◦. Therefore, we can apply (8.5) for θ0 = 50◦. This method gives h5(50◦) < 23.9181, then H(y1,...,y5) h5(50◦) < 23.9181, so then


H(y1,...,y6) < 23.9181 + f(− cos45◦) ≈ 23.9181 + 0.4533 = 24.3714 Thus

h6 < max{24.934,24.3714} = 24.934

### 9 k(4) = 24

- For n = 4, z = cos60◦ = 1/2 we apply this extension of Delsarte’s method with f(t) = 53.76t9−107.52t7+70.56t5+16.384t4−9.832t3−4.128t2−0.434t−0.016


The expansion of f in terms of Uk = G(4)k is f = U0 + 2U1 + 6.12U2 + 3.484U3 + 5.12U4 + 1.05U9 The polynomial f has two roots on [−1,1]: t1 = −t0, t0 ≈ 0.60794, t2 = 1/2,

f(t) 0 for t ∈ [−t0,1/2], and f is a monotone decreasing function on the interval [−1,−t0]. The last property holds because there are no zeros of the derivative f′(t) on [−1,−t0]. Therefore, f satisﬁes (∗) for z = 1/2.

Remark. The polynomial f was found by using the algorithm in Section 6. This algorithm for n = 4, z = 1/2, d = 9, N = 2000, t0 = 0.6058 gives E ≈ 24.7895. For the polynomial f the coeﬃcients ck were changed to “better looking” ones with E ≈ 24.8644.

![image 1059](<2005-musin-extension-delsarte-method-kissing_images/imageFile1059.png>)

7R achieves its maximum at α = 60◦, ψ ≈ 30.9344◦. Note that this bound exceeds the tight bound on h5 ≈ 24.6856 given by numerical methods.

![image 1060](<2005-musin-extension-delsarte-method-kissing_images/imageFile1060.png>)

![image 1061](<2005-musin-extension-delsarte-method-kissing_images/imageFile1061.png>)

![image 1062](<2005-musin-extension-delsarte-method-kissing_images/imageFile1062.png>)

![image 1063](<2005-musin-extension-delsarte-method-kissing_images/imageFile1063.png>)

![image 1064](<2005-musin-extension-delsarte-method-kissing_images/imageFile1064.png>)

![image 1065](<2005-musin-extension-delsarte-method-kissing_images/imageFile1065.png>)

![image 1066](<2005-musin-extension-delsarte-method-kissing_images/imageFile1066.png>)

![image 1067](<2005-musin-extension-delsarte-method-kissing_images/imageFile1067.png>)

![image 1068](<2005-musin-extension-delsarte-method-kissing_images/imageFile1068.png>)

![image 1069](<2005-musin-extension-delsarte-method-kissing_images/imageFile1069.png>)

![image 1070](<2005-musin-extension-delsarte-method-kissing_images/imageFile1070.png>)

![image 1071](<2005-musin-extension-delsarte-method-kissing_images/imageFile1071.png>)

![image 1072](<2005-musin-extension-delsarte-method-kissing_images/imageFile1072.png>)

- 0
- 1
- 2
- 3
- 4
- 5
- 6


![image 1073](<2005-musin-extension-delsarte-method-kissing_images/imageFile1073.png>)

![image 1074](<2005-musin-extension-delsarte-method-kissing_images/imageFile1074.png>)

![image 1075](<2005-musin-extension-delsarte-method-kissing_images/imageFile1075.png>)

![image 1076](<2005-musin-extension-delsarte-method-kissing_images/imageFile1076.png>)

![image 1077](<2005-musin-extension-delsarte-method-kissing_images/imageFile1077.png>)

![image 1078](<2005-musin-extension-delsarte-method-kissing_images/imageFile1078.png>)

![image 1079](<2005-musin-extension-delsarte-method-kissing_images/imageFile1079.png>)

![image 1080](<2005-musin-extension-delsarte-method-kissing_images/imageFile1080.png>)

![image 1081](<2005-musin-extension-delsarte-method-kissing_images/imageFile1081.png>)

![image 1082](<2005-musin-extension-delsarte-method-kissing_images/imageFile1082.png>)

![image 1083](<2005-musin-extension-delsarte-method-kissing_images/imageFile1083.png>)

![image 1084](<2005-musin-extension-delsarte-method-kissing_images/imageFile1084.png>)

![image 1085](<2005-musin-extension-delsarte-method-kissing_images/imageFile1085.png>)

![image 1086](<2005-musin-extension-delsarte-method-kissing_images/imageFile1086.png>)

![image 1087](<2005-musin-extension-delsarte-method-kissing_images/imageFile1087.png>)

![image 1088](<2005-musin-extension-delsarte-method-kissing_images/imageFile1088.png>)

![image 1089](<2005-musin-extension-delsarte-method-kissing_images/imageFile1089.png>)

![image 1090](<2005-musin-extension-delsarte-method-kissing_images/imageFile1090.png>)

![image 1091](<2005-musin-extension-delsarte-method-kissing_images/imageFile1091.png>)

![image 1092](<2005-musin-extension-delsarte-method-kissing_images/imageFile1092.png>)

![image 1093](<2005-musin-extension-delsarte-method-kissing_images/imageFile1093.png>)

![image 1094](<2005-musin-extension-delsarte-method-kissing_images/imageFile1094.png>)

![image 1095](<2005-musin-extension-delsarte-method-kissing_images/imageFile1095.png>)

![image 1096](<2005-musin-extension-delsarte-method-kissing_images/imageFile1096.png>)

![image 1097](<2005-musin-extension-delsarte-method-kissing_images/imageFile1097.png>)

![image 1098](<2005-musin-extension-delsarte-method-kissing_images/imageFile1098.png>)

![image 1099](<2005-musin-extension-delsarte-method-kissing_images/imageFile1099.png>)

![image 1100](<2005-musin-extension-delsarte-method-kissing_images/imageFile1100.png>)

![image 1101](<2005-musin-extension-delsarte-method-kissing_images/imageFile1101.png>)

![image 1102](<2005-musin-extension-delsarte-method-kissing_images/imageFile1102.png>)

![image 1103](<2005-musin-extension-delsarte-method-kissing_images/imageFile1103.png>)

![image 1104](<2005-musin-extension-delsarte-method-kissing_images/imageFile1104.png>)

![image 1105](<2005-musin-extension-delsarte-method-kissing_images/imageFile1105.png>)

![image 1106](<2005-musin-extension-delsarte-method-kissing_images/imageFile1106.png>)

![image 1107](<2005-musin-extension-delsarte-method-kissing_images/imageFile1107.png>)

![image 1108](<2005-musin-extension-delsarte-method-kissing_images/imageFile1108.png>)

![image 1109](<2005-musin-extension-delsarte-method-kissing_images/imageFile1109.png>)

![image 1110](<2005-musin-extension-delsarte-method-kissing_images/imageFile1110.png>)

![image 1111](<2005-musin-extension-delsarte-method-kissing_images/imageFile1111.png>)

![image 1112](<2005-musin-extension-delsarte-method-kissing_images/imageFile1112.png>)

![image 1113](<2005-musin-extension-delsarte-method-kissing_images/imageFile1113.png>)

![image 1114](<2005-musin-extension-delsarte-method-kissing_images/imageFile1114.png>)

![image 1115](<2005-musin-extension-delsarte-method-kissing_images/imageFile1115.png>)

![image 1116](<2005-musin-extension-delsarte-method-kissing_images/imageFile1116.png>)

![image 1117](<2005-musin-extension-delsarte-method-kissing_images/imageFile1117.png>)

![image 1118](<2005-musin-extension-delsarte-method-kissing_images/imageFile1118.png>)

![image 1119](<2005-musin-extension-delsarte-method-kissing_images/imageFile1119.png>)

![image 1120](<2005-musin-extension-delsarte-method-kissing_images/imageFile1120.png>)

![image 1121](<2005-musin-extension-delsarte-method-kissing_images/imageFile1121.png>)

![image 1122](<2005-musin-extension-delsarte-method-kissing_images/imageFile1122.png>)

![image 1123](<2005-musin-extension-delsarte-method-kissing_images/imageFile1123.png>)

![image 1124](<2005-musin-extension-delsarte-method-kissing_images/imageFile1124.png>)

![image 1125](<2005-musin-extension-delsarte-method-kissing_images/imageFile1125.png>)

![image 1126](<2005-musin-extension-delsarte-method-kissing_images/imageFile1126.png>)

![image 1127](<2005-musin-extension-delsarte-method-kissing_images/imageFile1127.png>)

![image 1128](<2005-musin-extension-delsarte-method-kissing_images/imageFile1128.png>)

![image 1129](<2005-musin-extension-delsarte-method-kissing_images/imageFile1129.png>)

![image 1130](<2005-musin-extension-delsarte-method-kissing_images/imageFile1130.png>)

![image 1131](<2005-musin-extension-delsarte-method-kissing_images/imageFile1131.png>)

![image 1132](<2005-musin-extension-delsarte-method-kissing_images/imageFile1132.png>)

![image 1133](<2005-musin-extension-delsarte-method-kissing_images/imageFile1133.png>)

![image 1134](<2005-musin-extension-delsarte-method-kissing_images/imageFile1134.png>)

![image 1135](<2005-musin-extension-delsarte-method-kissing_images/imageFile1135.png>)

![image 1136](<2005-musin-extension-delsarte-method-kissing_images/imageFile1136.png>)

![image 1137](<2005-musin-extension-delsarte-method-kissing_images/imageFile1137.png>)

![image 1138](<2005-musin-extension-delsarte-method-kissing_images/imageFile1138.png>)

![image 1139](<2005-musin-extension-delsarte-method-kissing_images/imageFile1139.png>)

![image 1140](<2005-musin-extension-delsarte-method-kissing_images/imageFile1140.png>)

![image 1141](<2005-musin-extension-delsarte-method-kissing_images/imageFile1141.png>)

![image 1142](<2005-musin-extension-delsarte-method-kissing_images/imageFile1142.png>)

![image 1143](<2005-musin-extension-delsarte-method-kissing_images/imageFile1143.png>)

![image 1144](<2005-musin-extension-delsarte-method-kissing_images/imageFile1144.png>)

![image 1145](<2005-musin-extension-delsarte-method-kissing_images/imageFile1145.png>)

![image 1146](<2005-musin-extension-delsarte-method-kissing_images/imageFile1146.png>)

![image 1147](<2005-musin-extension-delsarte-method-kissing_images/imageFile1147.png>)

![image 1148](<2005-musin-extension-delsarte-method-kissing_images/imageFile1148.png>)

![image 1149](<2005-musin-extension-delsarte-method-kissing_images/imageFile1149.png>)

![image 1150](<2005-musin-extension-delsarte-method-kissing_images/imageFile1150.png>)

![image 1151](<2005-musin-extension-delsarte-method-kissing_images/imageFile1151.png>)

![image 1152](<2005-musin-extension-delsarte-method-kissing_images/imageFile1152.png>)

![image 1153](<2005-musin-extension-delsarte-method-kissing_images/imageFile1153.png>)

![image 1154](<2005-musin-extension-delsarte-method-kissing_images/imageFile1154.png>)

![image 1155](<2005-musin-extension-delsarte-method-kissing_images/imageFile1155.png>)

![image 1156](<2005-musin-extension-delsarte-method-kissing_images/imageFile1156.png>)

![image 1157](<2005-musin-extension-delsarte-method-kissing_images/imageFile1157.png>)

![image 1158](<2005-musin-extension-delsarte-method-kissing_images/imageFile1158.png>)

![image 1159](<2005-musin-extension-delsarte-method-kissing_images/imageFile1159.png>)

![image 1160](<2005-musin-extension-delsarte-method-kissing_images/imageFile1160.png>)

![image 1161](<2005-musin-extension-delsarte-method-kissing_images/imageFile1161.png>)

![image 1162](<2005-musin-extension-delsarte-method-kissing_images/imageFile1162.png>)

![image 1163](<2005-musin-extension-delsarte-method-kissing_images/imageFile1163.png>)

![image 1164](<2005-musin-extension-delsarte-method-kissing_images/imageFile1164.png>)

![image 1165](<2005-musin-extension-delsarte-method-kissing_images/imageFile1165.png>)

![image 1166](<2005-musin-extension-delsarte-method-kissing_images/imageFile1166.png>)

![image 1167](<2005-musin-extension-delsarte-method-kissing_images/imageFile1167.png>)

![image 1168](<2005-musin-extension-delsarte-method-kissing_images/imageFile1168.png>)

![image 1169](<2005-musin-extension-delsarte-method-kissing_images/imageFile1169.png>)

![image 1170](<2005-musin-extension-delsarte-method-kissing_images/imageFile1170.png>)

![image 1171](<2005-musin-extension-delsarte-method-kissing_images/imageFile1171.png>)

![image 1172](<2005-musin-extension-delsarte-method-kissing_images/imageFile1172.png>)

![image 1173](<2005-musin-extension-delsarte-method-kissing_images/imageFile1173.png>)

![image 1174](<2005-musin-extension-delsarte-method-kissing_images/imageFile1174.png>)

![image 1175](<2005-musin-extension-delsarte-method-kissing_images/imageFile1175.png>)

![image 1176](<2005-musin-extension-delsarte-method-kissing_images/imageFile1176.png>)

![image 1177](<2005-musin-extension-delsarte-method-kissing_images/imageFile1177.png>)

![image 1178](<2005-musin-extension-delsarte-method-kissing_images/imageFile1178.png>)

![image 1179](<2005-musin-extension-delsarte-method-kissing_images/imageFile1179.png>)

![image 1180](<2005-musin-extension-delsarte-method-kissing_images/imageFile1180.png>)

![image 1181](<2005-musin-extension-delsarte-method-kissing_images/imageFile1181.png>)

![image 1182](<2005-musin-extension-delsarte-method-kissing_images/imageFile1182.png>)

![image 1183](<2005-musin-extension-delsarte-method-kissing_images/imageFile1183.png>)

![image 1184](<2005-musin-extension-delsarte-method-kissing_images/imageFile1184.png>)

![image 1185](<2005-musin-extension-delsarte-method-kissing_images/imageFile1185.png>)

![image 1186](<2005-musin-extension-delsarte-method-kissing_images/imageFile1186.png>)

![image 1187](<2005-musin-extension-delsarte-method-kissing_images/imageFile1187.png>)

![image 1188](<2005-musin-extension-delsarte-method-kissing_images/imageFile1188.png>)

![image 1189](<2005-musin-extension-delsarte-method-kissing_images/imageFile1189.png>)

![image 1190](<2005-musin-extension-delsarte-method-kissing_images/imageFile1190.png>)

![image 1191](<2005-musin-extension-delsarte-method-kissing_images/imageFile1191.png>)

![image 1192](<2005-musin-extension-delsarte-method-kissing_images/imageFile1192.png>)

![image 1193](<2005-musin-extension-delsarte-method-kissing_images/imageFile1193.png>)

![image 1194](<2005-musin-extension-delsarte-method-kissing_images/imageFile1194.png>)

![image 1195](<2005-musin-extension-delsarte-method-kissing_images/imageFile1195.png>)

![image 1196](<2005-musin-extension-delsarte-method-kissing_images/imageFile1196.png>)

![image 1197](<2005-musin-extension-delsarte-method-kissing_images/imageFile1197.png>)

![image 1198](<2005-musin-extension-delsarte-method-kissing_images/imageFile1198.png>)

![image 1199](<2005-musin-extension-delsarte-method-kissing_images/imageFile1199.png>)

![image 1200](<2005-musin-extension-delsarte-method-kissing_images/imageFile1200.png>)

![image 1201](<2005-musin-extension-delsarte-method-kissing_images/imageFile1201.png>)

![image 1202](<2005-musin-extension-delsarte-method-kissing_images/imageFile1202.png>)

![image 1203](<2005-musin-extension-delsarte-method-kissing_images/imageFile1203.png>)

![image 1204](<2005-musin-extension-delsarte-method-kissing_images/imageFile1204.png>)

![image 1205](<2005-musin-extension-delsarte-method-kissing_images/imageFile1205.png>)

![image 1206](<2005-musin-extension-delsarte-method-kissing_images/imageFile1206.png>)

![image 1207](<2005-musin-extension-delsarte-method-kissing_images/imageFile1207.png>)

![image 1208](<2005-musin-extension-delsarte-method-kissing_images/imageFile1208.png>)

![image 1209](<2005-musin-extension-delsarte-method-kissing_images/imageFile1209.png>)

![image 1210](<2005-musin-extension-delsarte-method-kissing_images/imageFile1210.png>)

![image 1211](<2005-musin-extension-delsarte-method-kissing_images/imageFile1211.png>)

![image 1212](<2005-musin-extension-delsarte-method-kissing_images/imageFile1212.png>)

![image 1213](<2005-musin-extension-delsarte-method-kissing_images/imageFile1213.png>)

![image 1214](<2005-musin-extension-delsarte-method-kissing_images/imageFile1214.png>)

![image 1215](<2005-musin-extension-delsarte-method-kissing_images/imageFile1215.png>)

![image 1216](<2005-musin-extension-delsarte-method-kissing_images/imageFile1216.png>)

![image 1217](<2005-musin-extension-delsarte-method-kissing_images/imageFile1217.png>)

![image 1218](<2005-musin-extension-delsarte-method-kissing_images/imageFile1218.png>)

![image 1219](<2005-musin-extension-delsarte-method-kissing_images/imageFile1219.png>)

![image 1220](<2005-musin-extension-delsarte-method-kissing_images/imageFile1220.png>)

![image 1221](<2005-musin-extension-delsarte-method-kissing_images/imageFile1221.png>)

![image 1222](<2005-musin-extension-delsarte-method-kissing_images/imageFile1222.png>)

![image 1223](<2005-musin-extension-delsarte-method-kissing_images/imageFile1223.png>)

![image 1224](<2005-musin-extension-delsarte-method-kissing_images/imageFile1224.png>)

![image 1225](<2005-musin-extension-delsarte-method-kissing_images/imageFile1225.png>)

![image 1226](<2005-musin-extension-delsarte-method-kissing_images/imageFile1226.png>)

![image 1227](<2005-musin-extension-delsarte-method-kissing_images/imageFile1227.png>)

![image 1228](<2005-musin-extension-delsarte-method-kissing_images/imageFile1228.png>)

![image 1229](<2005-musin-extension-delsarte-method-kissing_images/imageFile1229.png>)

![image 1230](<2005-musin-extension-delsarte-method-kissing_images/imageFile1230.png>)

![image 1231](<2005-musin-extension-delsarte-method-kissing_images/imageFile1231.png>)

![image 1232](<2005-musin-extension-delsarte-method-kissing_images/imageFile1232.png>)

![image 1233](<2005-musin-extension-delsarte-method-kissing_images/imageFile1233.png>)

![image 1234](<2005-musin-extension-delsarte-method-kissing_images/imageFile1234.png>)

![image 1235](<2005-musin-extension-delsarte-method-kissing_images/imageFile1235.png>)

![image 1236](<2005-musin-extension-delsarte-method-kissing_images/imageFile1236.png>)

![image 1237](<2005-musin-extension-delsarte-method-kissing_images/imageFile1237.png>)

![image 1238](<2005-musin-extension-delsarte-method-kissing_images/imageFile1238.png>)

![image 1239](<2005-musin-extension-delsarte-method-kissing_images/imageFile1239.png>)

![image 1240](<2005-musin-extension-delsarte-method-kissing_images/imageFile1240.png>)

![image 1241](<2005-musin-extension-delsarte-method-kissing_images/imageFile1241.png>)

![image 1242](<2005-musin-extension-delsarte-method-kissing_images/imageFile1242.png>)

![image 1243](<2005-musin-extension-delsarte-method-kissing_images/imageFile1243.png>)

![image 1244](<2005-musin-extension-delsarte-method-kissing_images/imageFile1244.png>)

![image 1245](<2005-musin-extension-delsarte-method-kissing_images/imageFile1245.png>)

![image 1246](<2005-musin-extension-delsarte-method-kissing_images/imageFile1246.png>)

![image 1247](<2005-musin-extension-delsarte-method-kissing_images/imageFile1247.png>)

![image 1248](<2005-musin-extension-delsarte-method-kissing_images/imageFile1248.png>)

![image 1249](<2005-musin-extension-delsarte-method-kissing_images/imageFile1249.png>)

![image 1250](<2005-musin-extension-delsarte-method-kissing_images/imageFile1250.png>)

![image 1251](<2005-musin-extension-delsarte-method-kissing_images/imageFile1251.png>)

![image 1252](<2005-musin-extension-delsarte-method-kissing_images/imageFile1252.png>)

![image 1253](<2005-musin-extension-delsarte-method-kissing_images/imageFile1253.png>)

![image 1254](<2005-musin-extension-delsarte-method-kissing_images/imageFile1254.png>)

![image 1255](<2005-musin-extension-delsarte-method-kissing_images/imageFile1255.png>)

![image 1256](<2005-musin-extension-delsarte-method-kissing_images/imageFile1256.png>)

![image 1257](<2005-musin-extension-delsarte-method-kissing_images/imageFile1257.png>)

![image 1258](<2005-musin-extension-delsarte-method-kissing_images/imageFile1258.png>)

![image 1259](<2005-musin-extension-delsarte-method-kissing_images/imageFile1259.png>)

![image 1260](<2005-musin-extension-delsarte-method-kissing_images/imageFile1260.png>)

![image 1261](<2005-musin-extension-delsarte-method-kissing_images/imageFile1261.png>)

![image 1262](<2005-musin-extension-delsarte-method-kissing_images/imageFile1262.png>)

![image 1263](<2005-musin-extension-delsarte-method-kissing_images/imageFile1263.png>)

![image 1264](<2005-musin-extension-delsarte-method-kissing_images/imageFile1264.png>)

![image 1265](<2005-musin-extension-delsarte-method-kissing_images/imageFile1265.png>)

![image 1266](<2005-musin-extension-delsarte-method-kissing_images/imageFile1266.png>)

![image 1267](<2005-musin-extension-delsarte-method-kissing_images/imageFile1267.png>)

![image 1268](<2005-musin-extension-delsarte-method-kissing_images/imageFile1268.png>)

![image 1269](<2005-musin-extension-delsarte-method-kissing_images/imageFile1269.png>)

![image 1270](<2005-musin-extension-delsarte-method-kissing_images/imageFile1270.png>)

![image 1271](<2005-musin-extension-delsarte-method-kissing_images/imageFile1271.png>)

![image 1272](<2005-musin-extension-delsarte-method-kissing_images/imageFile1272.png>)

![image 1273](<2005-musin-extension-delsarte-method-kissing_images/imageFile1273.png>)

![image 1274](<2005-musin-extension-delsarte-method-kissing_images/imageFile1274.png>)

![image 1275](<2005-musin-extension-delsarte-method-kissing_images/imageFile1275.png>)

![image 1276](<2005-musin-extension-delsarte-method-kissing_images/imageFile1276.png>)

![image 1277](<2005-musin-extension-delsarte-method-kissing_images/imageFile1277.png>)

![image 1278](<2005-musin-extension-delsarte-method-kissing_images/imageFile1278.png>)

![image 1279](<2005-musin-extension-delsarte-method-kissing_images/imageFile1279.png>)

![image 1280](<2005-musin-extension-delsarte-method-kissing_images/imageFile1280.png>)

![image 1281](<2005-musin-extension-delsarte-method-kissing_images/imageFile1281.png>)

![image 1282](<2005-musin-extension-delsarte-method-kissing_images/imageFile1282.png>)

![image 1283](<2005-musin-extension-delsarte-method-kissing_images/imageFile1283.png>)

![image 1284](<2005-musin-extension-delsarte-method-kissing_images/imageFile1284.png>)

![image 1285](<2005-musin-extension-delsarte-method-kissing_images/imageFile1285.png>)

![image 1286](<2005-musin-extension-delsarte-method-kissing_images/imageFile1286.png>)

![image 1287](<2005-musin-extension-delsarte-method-kissing_images/imageFile1287.png>)

![image 1288](<2005-musin-extension-delsarte-method-kissing_images/imageFile1288.png>)

![image 1289](<2005-musin-extension-delsarte-method-kissing_images/imageFile1289.png>)

![image 1290](<2005-musin-extension-delsarte-method-kissing_images/imageFile1290.png>)

![image 1291](<2005-musin-extension-delsarte-method-kissing_images/imageFile1291.png>)

![image 1292](<2005-musin-extension-delsarte-method-kissing_images/imageFile1292.png>)

![image 1293](<2005-musin-extension-delsarte-method-kissing_images/imageFile1293.png>)

![image 1294](<2005-musin-extension-delsarte-method-kissing_images/imageFile1294.png>)

![image 1295](<2005-musin-extension-delsarte-method-kissing_images/imageFile1295.png>)

![image 1296](<2005-musin-extension-delsarte-method-kissing_images/imageFile1296.png>)

![image 1297](<2005-musin-extension-delsarte-method-kissing_images/imageFile1297.png>)

![image 1298](<2005-musin-extension-delsarte-method-kissing_images/imageFile1298.png>)

![image 1299](<2005-musin-extension-delsarte-method-kissing_images/imageFile1299.png>)

![image 1300](<2005-musin-extension-delsarte-method-kissing_images/imageFile1300.png>)

![image 1301](<2005-musin-extension-delsarte-method-kissing_images/imageFile1301.png>)

![image 1302](<2005-musin-extension-delsarte-method-kissing_images/imageFile1302.png>)

![image 1303](<2005-musin-extension-delsarte-method-kissing_images/imageFile1303.png>)

![image 1304](<2005-musin-extension-delsarte-method-kissing_images/imageFile1304.png>)

![image 1305](<2005-musin-extension-delsarte-method-kissing_images/imageFile1305.png>)

![image 1306](<2005-musin-extension-delsarte-method-kissing_images/imageFile1306.png>)

![image 1307](<2005-musin-extension-delsarte-method-kissing_images/imageFile1307.png>)

![image 1308](<2005-musin-extension-delsarte-method-kissing_images/imageFile1308.png>)

![image 1309](<2005-musin-extension-delsarte-method-kissing_images/imageFile1309.png>)

![image 1310](<2005-musin-extension-delsarte-method-kissing_images/imageFile1310.png>)

![image 1311](<2005-musin-extension-delsarte-method-kissing_images/imageFile1311.png>)

![image 1312](<2005-musin-extension-delsarte-method-kissing_images/imageFile1312.png>)

![image 1313](<2005-musin-extension-delsarte-method-kissing_images/imageFile1313.png>)

![image 1314](<2005-musin-extension-delsarte-method-kissing_images/imageFile1314.png>)

![image 1315](<2005-musin-extension-delsarte-method-kissing_images/imageFile1315.png>)

![image 1316](<2005-musin-extension-delsarte-method-kissing_images/imageFile1316.png>)

![image 1317](<2005-musin-extension-delsarte-method-kissing_images/imageFile1317.png>)

![image 1318](<2005-musin-extension-delsarte-method-kissing_images/imageFile1318.png>)

![image 1319](<2005-musin-extension-delsarte-method-kissing_images/imageFile1319.png>)

![image 1320](<2005-musin-extension-delsarte-method-kissing_images/imageFile1320.png>)

![image 1321](<2005-musin-extension-delsarte-method-kissing_images/imageFile1321.png>)

![image 1322](<2005-musin-extension-delsarte-method-kissing_images/imageFile1322.png>)

![image 1323](<2005-musin-extension-delsarte-method-kissing_images/imageFile1323.png>)

![image 1324](<2005-musin-extension-delsarte-method-kissing_images/imageFile1324.png>)

![image 1325](<2005-musin-extension-delsarte-method-kissing_images/imageFile1325.png>)

![image 1326](<2005-musin-extension-delsarte-method-kissing_images/imageFile1326.png>)

![image 1327](<2005-musin-extension-delsarte-method-kissing_images/imageFile1327.png>)

![image 1328](<2005-musin-extension-delsarte-method-kissing_images/imageFile1328.png>)

![image 1329](<2005-musin-extension-delsarte-method-kissing_images/imageFile1329.png>)

![image 1330](<2005-musin-extension-delsarte-method-kissing_images/imageFile1330.png>)

![image 1331](<2005-musin-extension-delsarte-method-kissing_images/imageFile1331.png>)

![image 1332](<2005-musin-extension-delsarte-method-kissing_images/imageFile1332.png>)

![image 1333](<2005-musin-extension-delsarte-method-kissing_images/imageFile1333.png>)

![image 1334](<2005-musin-extension-delsarte-method-kissing_images/imageFile1334.png>)

![image 1335](<2005-musin-extension-delsarte-method-kissing_images/imageFile1335.png>)

![image 1336](<2005-musin-extension-delsarte-method-kissing_images/imageFile1336.png>)

![image 1337](<2005-musin-extension-delsarte-method-kissing_images/imageFile1337.png>)

![image 1338](<2005-musin-extension-delsarte-method-kissing_images/imageFile1338.png>)

![image 1339](<2005-musin-extension-delsarte-method-kissing_images/imageFile1339.png>)

![image 1340](<2005-musin-extension-delsarte-method-kissing_images/imageFile1340.png>)

![image 1341](<2005-musin-extension-delsarte-method-kissing_images/imageFile1341.png>)

![image 1342](<2005-musin-extension-delsarte-method-kissing_images/imageFile1342.png>)

![image 1343](<2005-musin-extension-delsarte-method-kissing_images/imageFile1343.png>)

![image 1344](<2005-musin-extension-delsarte-method-kissing_images/imageFile1344.png>)

![image 1345](<2005-musin-extension-delsarte-method-kissing_images/imageFile1345.png>)

![image 1346](<2005-musin-extension-delsarte-method-kissing_images/imageFile1346.png>)

![image 1347](<2005-musin-extension-delsarte-method-kissing_images/imageFile1347.png>)

![image 1348](<2005-musin-extension-delsarte-method-kissing_images/imageFile1348.png>)

![image 1349](<2005-musin-extension-delsarte-method-kissing_images/imageFile1349.png>)

![image 1350](<2005-musin-extension-delsarte-method-kissing_images/imageFile1350.png>)

![image 1351](<2005-musin-extension-delsarte-method-kissing_images/imageFile1351.png>)

![image 1352](<2005-musin-extension-delsarte-method-kissing_images/imageFile1352.png>)

![image 1353](<2005-musin-extension-delsarte-method-kissing_images/imageFile1353.png>)

![image 1354](<2005-musin-extension-delsarte-method-kissing_images/imageFile1354.png>)

![image 1355](<2005-musin-extension-delsarte-method-kissing_images/imageFile1355.png>)

![image 1356](<2005-musin-extension-delsarte-method-kissing_images/imageFile1356.png>)

![image 1357](<2005-musin-extension-delsarte-method-kissing_images/imageFile1357.png>)

![image 1358](<2005-musin-extension-delsarte-method-kissing_images/imageFile1358.png>)

![image 1359](<2005-musin-extension-delsarte-method-kissing_images/imageFile1359.png>)

![image 1360](<2005-musin-extension-delsarte-method-kissing_images/imageFile1360.png>)

![image 1361](<2005-musin-extension-delsarte-method-kissing_images/imageFile1361.png>)

![image 1362](<2005-musin-extension-delsarte-method-kissing_images/imageFile1362.png>)

![image 1363](<2005-musin-extension-delsarte-method-kissing_images/imageFile1363.png>)

![image 1364](<2005-musin-extension-delsarte-method-kissing_images/imageFile1364.png>)

![image 1365](<2005-musin-extension-delsarte-method-kissing_images/imageFile1365.png>)

![image 1366](<2005-musin-extension-delsarte-method-kissing_images/imageFile1366.png>)

![image 1367](<2005-musin-extension-delsarte-method-kissing_images/imageFile1367.png>)

![image 1368](<2005-musin-extension-delsarte-method-kissing_images/imageFile1368.png>)

![image 1369](<2005-musin-extension-delsarte-method-kissing_images/imageFile1369.png>)

![image 1370](<2005-musin-extension-delsarte-method-kissing_images/imageFile1370.png>)

![image 1371](<2005-musin-extension-delsarte-method-kissing_images/imageFile1371.png>)

![image 1372](<2005-musin-extension-delsarte-method-kissing_images/imageFile1372.png>)

![image 1373](<2005-musin-extension-delsarte-method-kissing_images/imageFile1373.png>)

![image 1374](<2005-musin-extension-delsarte-method-kissing_images/imageFile1374.png>)

![image 1375](<2005-musin-extension-delsarte-method-kissing_images/imageFile1375.png>)

![image 1376](<2005-musin-extension-delsarte-method-kissing_images/imageFile1376.png>)

![image 1377](<2005-musin-extension-delsarte-method-kissing_images/imageFile1377.png>)

![image 1378](<2005-musin-extension-delsarte-method-kissing_images/imageFile1378.png>)

![image 1379](<2005-musin-extension-delsarte-method-kissing_images/imageFile1379.png>)

![image 1380](<2005-musin-extension-delsarte-method-kissing_images/imageFile1380.png>)

![image 1381](<2005-musin-extension-delsarte-method-kissing_images/imageFile1381.png>)

![image 1382](<2005-musin-extension-delsarte-method-kissing_images/imageFile1382.png>)

![image 1383](<2005-musin-extension-delsarte-method-kissing_images/imageFile1383.png>)

![image 1384](<2005-musin-extension-delsarte-method-kissing_images/imageFile1384.png>)

![image 1385](<2005-musin-extension-delsarte-method-kissing_images/imageFile1385.png>)

![image 1386](<2005-musin-extension-delsarte-method-kissing_images/imageFile1386.png>)

![image 1387](<2005-musin-extension-delsarte-method-kissing_images/imageFile1387.png>)

![image 1388](<2005-musin-extension-delsarte-method-kissing_images/imageFile1388.png>)

![image 1389](<2005-musin-extension-delsarte-method-kissing_images/imageFile1389.png>)

![image 1390](<2005-musin-extension-delsarte-method-kissing_images/imageFile1390.png>)

![image 1391](<2005-musin-extension-delsarte-method-kissing_images/imageFile1391.png>)

![image 1392](<2005-musin-extension-delsarte-method-kissing_images/imageFile1392.png>)

![image 1393](<2005-musin-extension-delsarte-method-kissing_images/imageFile1393.png>)

![image 1394](<2005-musin-extension-delsarte-method-kissing_images/imageFile1394.png>)

![image 1395](<2005-musin-extension-delsarte-method-kissing_images/imageFile1395.png>)

![image 1396](<2005-musin-extension-delsarte-method-kissing_images/imageFile1396.png>)

![image 1397](<2005-musin-extension-delsarte-method-kissing_images/imageFile1397.png>)

![image 1398](<2005-musin-extension-delsarte-method-kissing_images/imageFile1398.png>)

![image 1399](<2005-musin-extension-delsarte-method-kissing_images/imageFile1399.png>)

![image 1400](<2005-musin-extension-delsarte-method-kissing_images/imageFile1400.png>)

![image 1401](<2005-musin-extension-delsarte-method-kissing_images/imageFile1401.png>)

![image 1402](<2005-musin-extension-delsarte-method-kissing_images/imageFile1402.png>)

![image 1403](<2005-musin-extension-delsarte-method-kissing_images/imageFile1403.png>)

![image 1404](<2005-musin-extension-delsarte-method-kissing_images/imageFile1404.png>)

![image 1405](<2005-musin-extension-delsarte-method-kissing_images/imageFile1405.png>)

![image 1406](<2005-musin-extension-delsarte-method-kissing_images/imageFile1406.png>)

![image 1407](<2005-musin-extension-delsarte-method-kissing_images/imageFile1407.png>)

![image 1408](<2005-musin-extension-delsarte-method-kissing_images/imageFile1408.png>)

![image 1409](<2005-musin-extension-delsarte-method-kissing_images/imageFile1409.png>)

![image 1410](<2005-musin-extension-delsarte-method-kissing_images/imageFile1410.png>)

![image 1411](<2005-musin-extension-delsarte-method-kissing_images/imageFile1411.png>)

![image 1412](<2005-musin-extension-delsarte-method-kissing_images/imageFile1412.png>)

![image 1413](<2005-musin-extension-delsarte-method-kissing_images/imageFile1413.png>)

![image 1414](<2005-musin-extension-delsarte-method-kissing_images/imageFile1414.png>)

![image 1415](<2005-musin-extension-delsarte-method-kissing_images/imageFile1415.png>)

![image 1416](<2005-musin-extension-delsarte-method-kissing_images/imageFile1416.png>)

![image 1417](<2005-musin-extension-delsarte-method-kissing_images/imageFile1417.png>)

![image 1418](<2005-musin-extension-delsarte-method-kissing_images/imageFile1418.png>)

![image 1419](<2005-musin-extension-delsarte-method-kissing_images/imageFile1419.png>)

![image 1420](<2005-musin-extension-delsarte-method-kissing_images/imageFile1420.png>)

![image 1421](<2005-musin-extension-delsarte-method-kissing_images/imageFile1421.png>)

![image 1422](<2005-musin-extension-delsarte-method-kissing_images/imageFile1422.png>)

![image 1423](<2005-musin-extension-delsarte-method-kissing_images/imageFile1423.png>)

![image 1424](<2005-musin-extension-delsarte-method-kissing_images/imageFile1424.png>)

![image 1425](<2005-musin-extension-delsarte-method-kissing_images/imageFile1425.png>)

![image 1426](<2005-musin-extension-delsarte-method-kissing_images/imageFile1426.png>)

![image 1427](<2005-musin-extension-delsarte-method-kissing_images/imageFile1427.png>)

![image 1428](<2005-musin-extension-delsarte-method-kissing_images/imageFile1428.png>)

![image 1429](<2005-musin-extension-delsarte-method-kissing_images/imageFile1429.png>)

![image 1430](<2005-musin-extension-delsarte-method-kissing_images/imageFile1430.png>)

![image 1431](<2005-musin-extension-delsarte-method-kissing_images/imageFile1431.png>)

![image 1432](<2005-musin-extension-delsarte-method-kissing_images/imageFile1432.png>)

![image 1433](<2005-musin-extension-delsarte-method-kissing_images/imageFile1433.png>)

![image 1434](<2005-musin-extension-delsarte-method-kissing_images/imageFile1434.png>)

![image 1435](<2005-musin-extension-delsarte-method-kissing_images/imageFile1435.png>)

![image 1436](<2005-musin-extension-delsarte-method-kissing_images/imageFile1436.png>)

![image 1437](<2005-musin-extension-delsarte-method-kissing_images/imageFile1437.png>)

![image 1438](<2005-musin-extension-delsarte-method-kissing_images/imageFile1438.png>)

![image 1439](<2005-musin-extension-delsarte-method-kissing_images/imageFile1439.png>)

![image 1440](<2005-musin-extension-delsarte-method-kissing_images/imageFile1440.png>)

![image 1441](<2005-musin-extension-delsarte-method-kissing_images/imageFile1441.png>)

![image 1442](<2005-musin-extension-delsarte-method-kissing_images/imageFile1442.png>)

![image 1443](<2005-musin-extension-delsarte-method-kissing_images/imageFile1443.png>)

![image 1444](<2005-musin-extension-delsarte-method-kissing_images/imageFile1444.png>)

![image 1445](<2005-musin-extension-delsarte-method-kissing_images/imageFile1445.png>)

![image 1446](<2005-musin-extension-delsarte-method-kissing_images/imageFile1446.png>)

![image 1447](<2005-musin-extension-delsarte-method-kissing_images/imageFile1447.png>)

![image 1448](<2005-musin-extension-delsarte-method-kissing_images/imageFile1448.png>)

![image 1449](<2005-musin-extension-delsarte-method-kissing_images/imageFile1449.png>)

![image 1450](<2005-musin-extension-delsarte-method-kissing_images/imageFile1450.png>)

![image 1451](<2005-musin-extension-delsarte-method-kissing_images/imageFile1451.png>)

![image 1452](<2005-musin-extension-delsarte-method-kissing_images/imageFile1452.png>)

![image 1453](<2005-musin-extension-delsarte-method-kissing_images/imageFile1453.png>)

![image 1454](<2005-musin-extension-delsarte-method-kissing_images/imageFile1454.png>)

![image 1455](<2005-musin-extension-delsarte-method-kissing_images/imageFile1455.png>)

![image 1456](<2005-musin-extension-delsarte-method-kissing_images/imageFile1456.png>)

![image 1457](<2005-musin-extension-delsarte-method-kissing_images/imageFile1457.png>)

![image 1458](<2005-musin-extension-delsarte-method-kissing_images/imageFile1458.png>)

![image 1459](<2005-musin-extension-delsarte-method-kissing_images/imageFile1459.png>)

![image 1460](<2005-musin-extension-delsarte-method-kissing_images/imageFile1460.png>)

![image 1461](<2005-musin-extension-delsarte-method-kissing_images/imageFile1461.png>)

![image 1462](<2005-musin-extension-delsarte-method-kissing_images/imageFile1462.png>)

![image 1463](<2005-musin-extension-delsarte-method-kissing_images/imageFile1463.png>)

![image 1464](<2005-musin-extension-delsarte-method-kissing_images/imageFile1464.png>)

![image 1465](<2005-musin-extension-delsarte-method-kissing_images/imageFile1465.png>)

![image 1466](<2005-musin-extension-delsarte-method-kissing_images/imageFile1466.png>)

![image 1467](<2005-musin-extension-delsarte-method-kissing_images/imageFile1467.png>)

![image 1468](<2005-musin-extension-delsarte-method-kissing_images/imageFile1468.png>)

![image 1469](<2005-musin-extension-delsarte-method-kissing_images/imageFile1469.png>)

![image 1470](<2005-musin-extension-delsarte-method-kissing_images/imageFile1470.png>)

![image 1471](<2005-musin-extension-delsarte-method-kissing_images/imageFile1471.png>)

![image 1472](<2005-musin-extension-delsarte-method-kissing_images/imageFile1472.png>)

![image 1473](<2005-musin-extension-delsarte-method-kissing_images/imageFile1473.png>)

![image 1474](<2005-musin-extension-delsarte-method-kissing_images/imageFile1474.png>)

![image 1475](<2005-musin-extension-delsarte-method-kissing_images/imageFile1475.png>)

![image 1476](<2005-musin-extension-delsarte-method-kissing_images/imageFile1476.png>)

![image 1477](<2005-musin-extension-delsarte-method-kissing_images/imageFile1477.png>)

![image 1478](<2005-musin-extension-delsarte-method-kissing_images/imageFile1478.png>)

![image 1479](<2005-musin-extension-delsarte-method-kissing_images/imageFile1479.png>)

![image 1480](<2005-musin-extension-delsarte-method-kissing_images/imageFile1480.png>)

![image 1481](<2005-musin-extension-delsarte-method-kissing_images/imageFile1481.png>)

![image 1482](<2005-musin-extension-delsarte-method-kissing_images/imageFile1482.png>)

![image 1483](<2005-musin-extension-delsarte-method-kissing_images/imageFile1483.png>)

![image 1484](<2005-musin-extension-delsarte-method-kissing_images/imageFile1484.png>)

![image 1485](<2005-musin-extension-delsarte-method-kissing_images/imageFile1485.png>)

![image 1486](<2005-musin-extension-delsarte-method-kissing_images/imageFile1486.png>)

![image 1487](<2005-musin-extension-delsarte-method-kissing_images/imageFile1487.png>)

![image 1488](<2005-musin-extension-delsarte-method-kissing_images/imageFile1488.png>)

![image 1489](<2005-musin-extension-delsarte-method-kissing_images/imageFile1489.png>)

![image 1490](<2005-musin-extension-delsarte-method-kissing_images/imageFile1490.png>)

![image 1491](<2005-musin-extension-delsarte-method-kissing_images/imageFile1491.png>)

![image 1492](<2005-musin-extension-delsarte-method-kissing_images/imageFile1492.png>)

![image 1493](<2005-musin-extension-delsarte-method-kissing_images/imageFile1493.png>)

![image 1494](<2005-musin-extension-delsarte-method-kissing_images/imageFile1494.png>)

![image 1495](<2005-musin-extension-delsarte-method-kissing_images/imageFile1495.png>)

![image 1496](<2005-musin-extension-delsarte-method-kissing_images/imageFile1496.png>)

![image 1497](<2005-musin-extension-delsarte-method-kissing_images/imageFile1497.png>)

![image 1498](<2005-musin-extension-delsarte-method-kissing_images/imageFile1498.png>)

![image 1499](<2005-musin-extension-delsarte-method-kissing_images/imageFile1499.png>)

![image 1500](<2005-musin-extension-delsarte-method-kissing_images/imageFile1500.png>)

![image 1501](<2005-musin-extension-delsarte-method-kissing_images/imageFile1501.png>)

![image 1502](<2005-musin-extension-delsarte-method-kissing_images/imageFile1502.png>)

![image 1503](<2005-musin-extension-delsarte-method-kissing_images/imageFile1503.png>)

![image 1504](<2005-musin-extension-delsarte-method-kissing_images/imageFile1504.png>)

![image 1505](<2005-musin-extension-delsarte-method-kissing_images/imageFile1505.png>)

![image 1506](<2005-musin-extension-delsarte-method-kissing_images/imageFile1506.png>)

![image 1507](<2005-musin-extension-delsarte-method-kissing_images/imageFile1507.png>)

![image 1508](<2005-musin-extension-delsarte-method-kissing_images/imageFile1508.png>)

![image 1509](<2005-musin-extension-delsarte-method-kissing_images/imageFile1509.png>)

![image 1510](<2005-musin-extension-delsarte-method-kissing_images/imageFile1510.png>)

![image 1511](<2005-musin-extension-delsarte-method-kissing_images/imageFile1511.png>)

![image 1512](<2005-musin-extension-delsarte-method-kissing_images/imageFile1512.png>)

![image 1513](<2005-musin-extension-delsarte-method-kissing_images/imageFile1513.png>)

![image 1514](<2005-musin-extension-delsarte-method-kissing_images/imageFile1514.png>)

![image 1515](<2005-musin-extension-delsarte-method-kissing_images/imageFile1515.png>)

![image 1516](<2005-musin-extension-delsarte-method-kissing_images/imageFile1516.png>)

![image 1517](<2005-musin-extension-delsarte-method-kissing_images/imageFile1517.png>)

![image 1518](<2005-musin-extension-delsarte-method-kissing_images/imageFile1518.png>)

![image 1519](<2005-musin-extension-delsarte-method-kissing_images/imageFile1519.png>)

![image 1520](<2005-musin-extension-delsarte-method-kissing_images/imageFile1520.png>)

![image 1521](<2005-musin-extension-delsarte-method-kissing_images/imageFile1521.png>)

![image 1522](<2005-musin-extension-delsarte-method-kissing_images/imageFile1522.png>)

![image 1523](<2005-musin-extension-delsarte-method-kissing_images/imageFile1523.png>)

![image 1524](<2005-musin-extension-delsarte-method-kissing_images/imageFile1524.png>)

![image 1525](<2005-musin-extension-delsarte-method-kissing_images/imageFile1525.png>)

![image 1526](<2005-musin-extension-delsarte-method-kissing_images/imageFile1526.png>)

![image 1527](<2005-musin-extension-delsarte-method-kissing_images/imageFile1527.png>)

![image 1528](<2005-musin-extension-delsarte-method-kissing_images/imageFile1528.png>)

![image 1529](<2005-musin-extension-delsarte-method-kissing_images/imageFile1529.png>)

![image 1530](<2005-musin-extension-delsarte-method-kissing_images/imageFile1530.png>)

![image 1531](<2005-musin-extension-delsarte-method-kissing_images/imageFile1531.png>)

![image 1532](<2005-musin-extension-delsarte-method-kissing_images/imageFile1532.png>)

![image 1533](<2005-musin-extension-delsarte-method-kissing_images/imageFile1533.png>)

![image 1534](<2005-musin-extension-delsarte-method-kissing_images/imageFile1534.png>)

![image 1535](<2005-musin-extension-delsarte-method-kissing_images/imageFile1535.png>)

![image 1536](<2005-musin-extension-delsarte-method-kissing_images/imageFile1536.png>)

![image 1537](<2005-musin-extension-delsarte-method-kissing_images/imageFile1537.png>)

![image 1538](<2005-musin-extension-delsarte-method-kissing_images/imageFile1538.png>)

![image 1539](<2005-musin-extension-delsarte-method-kissing_images/imageFile1539.png>)

![image 1540](<2005-musin-extension-delsarte-method-kissing_images/imageFile1540.png>)

![image 1541](<2005-musin-extension-delsarte-method-kissing_images/imageFile1541.png>)

![image 1542](<2005-musin-extension-delsarte-method-kissing_images/imageFile1542.png>)

![image 1543](<2005-musin-extension-delsarte-method-kissing_images/imageFile1543.png>)

![image 1544](<2005-musin-extension-delsarte-method-kissing_images/imageFile1544.png>)

![image 1545](<2005-musin-extension-delsarte-method-kissing_images/imageFile1545.png>)

![image 1546](<2005-musin-extension-delsarte-method-kissing_images/imageFile1546.png>)

![image 1547](<2005-musin-extension-delsarte-method-kissing_images/imageFile1547.png>)

![image 1548](<2005-musin-extension-delsarte-method-kissing_images/imageFile1548.png>)

![image 1549](<2005-musin-extension-delsarte-method-kissing_images/imageFile1549.png>)

![image 1550](<2005-musin-extension-delsarte-method-kissing_images/imageFile1550.png>)

![image 1551](<2005-musin-extension-delsarte-method-kissing_images/imageFile1551.png>)

![image 1552](<2005-musin-extension-delsarte-method-kissing_images/imageFile1552.png>)

![image 1553](<2005-musin-extension-delsarte-method-kissing_images/imageFile1553.png>)

![image 1554](<2005-musin-extension-delsarte-method-kissing_images/imageFile1554.png>)

![image 1555](<2005-musin-extension-delsarte-method-kissing_images/imageFile1555.png>)

![image 1556](<2005-musin-extension-delsarte-method-kissing_images/imageFile1556.png>)

![image 1557](<2005-musin-extension-delsarte-method-kissing_images/imageFile1557.png>)

![image 1558](<2005-musin-extension-delsarte-method-kissing_images/imageFile1558.png>)

![image 1559](<2005-musin-extension-delsarte-method-kissing_images/imageFile1559.png>)

![image 1560](<2005-musin-extension-delsarte-method-kissing_images/imageFile1560.png>)

![image 1561](<2005-musin-extension-delsarte-method-kissing_images/imageFile1561.png>)

![image 1562](<2005-musin-extension-delsarte-method-kissing_images/imageFile1562.png>)

![image 1563](<2005-musin-extension-delsarte-method-kissing_images/imageFile1563.png>)

![image 1564](<2005-musin-extension-delsarte-method-kissing_images/imageFile1564.png>)

![image 1565](<2005-musin-extension-delsarte-method-kissing_images/imageFile1565.png>)

![image 1566](<2005-musin-extension-delsarte-method-kissing_images/imageFile1566.png>)

![image 1567](<2005-musin-extension-delsarte-method-kissing_images/imageFile1567.png>)

![image 1568](<2005-musin-extension-delsarte-method-kissing_images/imageFile1568.png>)

![image 1569](<2005-musin-extension-delsarte-method-kissing_images/imageFile1569.png>)

![image 1570](<2005-musin-extension-delsarte-method-kissing_images/imageFile1570.png>)

![image 1571](<2005-musin-extension-delsarte-method-kissing_images/imageFile1571.png>)

![image 1572](<2005-musin-extension-delsarte-method-kissing_images/imageFile1572.png>)

![image 1573](<2005-musin-extension-delsarte-method-kissing_images/imageFile1573.png>)

![image 1574](<2005-musin-extension-delsarte-method-kissing_images/imageFile1574.png>)

![image 1575](<2005-musin-extension-delsarte-method-kissing_images/imageFile1575.png>)

![image 1576](<2005-musin-extension-delsarte-method-kissing_images/imageFile1576.png>)

![image 1577](<2005-musin-extension-delsarte-method-kissing_images/imageFile1577.png>)

![image 1578](<2005-musin-extension-delsarte-method-kissing_images/imageFile1578.png>)

![image 1579](<2005-musin-extension-delsarte-method-kissing_images/imageFile1579.png>)

![image 1580](<2005-musin-extension-delsarte-method-kissing_images/imageFile1580.png>)

![image 1581](<2005-musin-extension-delsarte-method-kissing_images/imageFile1581.png>)

![image 1582](<2005-musin-extension-delsarte-method-kissing_images/imageFile1582.png>)

![image 1583](<2005-musin-extension-delsarte-method-kissing_images/imageFile1583.png>)

![image 1584](<2005-musin-extension-delsarte-method-kissing_images/imageFile1584.png>)

![image 1585](<2005-musin-extension-delsarte-method-kissing_images/imageFile1585.png>)

![image 1586](<2005-musin-extension-delsarte-method-kissing_images/imageFile1586.png>)

![image 1587](<2005-musin-extension-delsarte-method-kissing_images/imageFile1587.png>)

![image 1588](<2005-musin-extension-delsarte-method-kissing_images/imageFile1588.png>)

![image 1589](<2005-musin-extension-delsarte-method-kissing_images/imageFile1589.png>)

![image 1590](<2005-musin-extension-delsarte-method-kissing_images/imageFile1590.png>)

![image 1591](<2005-musin-extension-delsarte-method-kissing_images/imageFile1591.png>)

![image 1592](<2005-musin-extension-delsarte-method-kissing_images/imageFile1592.png>)

![image 1593](<2005-musin-extension-delsarte-method-kissing_images/imageFile1593.png>)

![image 1594](<2005-musin-extension-delsarte-method-kissing_images/imageFile1594.png>)

![image 1595](<2005-musin-extension-delsarte-method-kissing_images/imageFile1595.png>)

![image 1596](<2005-musin-extension-delsarte-method-kissing_images/imageFile1596.png>)

![image 1597](<2005-musin-extension-delsarte-method-kissing_images/imageFile1597.png>)

![image 1598](<2005-musin-extension-delsarte-method-kissing_images/imageFile1598.png>)

![image 1599](<2005-musin-extension-delsarte-method-kissing_images/imageFile1599.png>)

![image 1600](<2005-musin-extension-delsarte-method-kissing_images/imageFile1600.png>)

![image 1601](<2005-musin-extension-delsarte-method-kissing_images/imageFile1601.png>)

![image 1602](<2005-musin-extension-delsarte-method-kissing_images/imageFile1602.png>)

![image 1603](<2005-musin-extension-delsarte-method-kissing_images/imageFile1603.png>)

![image 1604](<2005-musin-extension-delsarte-method-kissing_images/imageFile1604.png>)

![image 1605](<2005-musin-extension-delsarte-method-kissing_images/imageFile1605.png>)

![image 1606](<2005-musin-extension-delsarte-method-kissing_images/imageFile1606.png>)

![image 1607](<2005-musin-extension-delsarte-method-kissing_images/imageFile1607.png>)

![image 1608](<2005-musin-extension-delsarte-method-kissing_images/imageFile1608.png>)

![image 1609](<2005-musin-extension-delsarte-method-kissing_images/imageFile1609.png>)

![image 1610](<2005-musin-extension-delsarte-method-kissing_images/imageFile1610.png>)

![image 1611](<2005-musin-extension-delsarte-method-kissing_images/imageFile1611.png>)

![image 1612](<2005-musin-extension-delsarte-method-kissing_images/imageFile1612.png>)

![image 1613](<2005-musin-extension-delsarte-method-kissing_images/imageFile1613.png>)

![image 1614](<2005-musin-extension-delsarte-method-kissing_images/imageFile1614.png>)

![image 1615](<2005-musin-extension-delsarte-method-kissing_images/imageFile1615.png>)

![image 1616](<2005-musin-extension-delsarte-method-kissing_images/imageFile1616.png>)

![image 1617](<2005-musin-extension-delsarte-method-kissing_images/imageFile1617.png>)

![image 1618](<2005-musin-extension-delsarte-method-kissing_images/imageFile1618.png>)

![image 1619](<2005-musin-extension-delsarte-method-kissing_images/imageFile1619.png>)

![image 1620](<2005-musin-extension-delsarte-method-kissing_images/imageFile1620.png>)

![image 1621](<2005-musin-extension-delsarte-method-kissing_images/imageFile1621.png>)

![image 1622](<2005-musin-extension-delsarte-method-kissing_images/imageFile1622.png>)

![image 1623](<2005-musin-extension-delsarte-method-kissing_images/imageFile1623.png>)

![image 1624](<2005-musin-extension-delsarte-method-kissing_images/imageFile1624.png>)

![image 1625](<2005-musin-extension-delsarte-method-kissing_images/imageFile1625.png>)

![image 1626](<2005-musin-extension-delsarte-method-kissing_images/imageFile1626.png>)

![image 1627](<2005-musin-extension-delsarte-method-kissing_images/imageFile1627.png>)

![image 1628](<2005-musin-extension-delsarte-method-kissing_images/imageFile1628.png>)

![image 1629](<2005-musin-extension-delsarte-method-kissing_images/imageFile1629.png>)

![image 1630](<2005-musin-extension-delsarte-method-kissing_images/imageFile1630.png>)

![image 1631](<2005-musin-extension-delsarte-method-kissing_images/imageFile1631.png>)

![image 1632](<2005-musin-extension-delsarte-method-kissing_images/imageFile1632.png>)

![image 1633](<2005-musin-extension-delsarte-method-kissing_images/imageFile1633.png>)

![image 1634](<2005-musin-extension-delsarte-method-kissing_images/imageFile1634.png>)

![image 1635](<2005-musin-extension-delsarte-method-kissing_images/imageFile1635.png>)

![image 1636](<2005-musin-extension-delsarte-method-kissing_images/imageFile1636.png>)

![image 1637](<2005-musin-extension-delsarte-method-kissing_images/imageFile1637.png>)

![image 1638](<2005-musin-extension-delsarte-method-kissing_images/imageFile1638.png>)

![image 1639](<2005-musin-extension-delsarte-method-kissing_images/imageFile1639.png>)

![image 1640](<2005-musin-extension-delsarte-method-kissing_images/imageFile1640.png>)

![image 1641](<2005-musin-extension-delsarte-method-kissing_images/imageFile1641.png>)

![image 1642](<2005-musin-extension-delsarte-method-kissing_images/imageFile1642.png>)

![image 1643](<2005-musin-extension-delsarte-method-kissing_images/imageFile1643.png>)

![image 1644](<2005-musin-extension-delsarte-method-kissing_images/imageFile1644.png>)

![image 1645](<2005-musin-extension-delsarte-method-kissing_images/imageFile1645.png>)

![image 1646](<2005-musin-extension-delsarte-method-kissing_images/imageFile1646.png>)

![image 1647](<2005-musin-extension-delsarte-method-kissing_images/imageFile1647.png>)

![image 1648](<2005-musin-extension-delsarte-method-kissing_images/imageFile1648.png>)

![image 1649](<2005-musin-extension-delsarte-method-kissing_images/imageFile1649.png>)

![image 1650](<2005-musin-extension-delsarte-method-kissing_images/imageFile1650.png>)

![image 1651](<2005-musin-extension-delsarte-method-kissing_images/imageFile1651.png>)

![image 1652](<2005-musin-extension-delsarte-method-kissing_images/imageFile1652.png>)

![image 1653](<2005-musin-extension-delsarte-method-kissing_images/imageFile1653.png>)

![image 1654](<2005-musin-extension-delsarte-method-kissing_images/imageFile1654.png>)

![image 1655](<2005-musin-extension-delsarte-method-kissing_images/imageFile1655.png>)

![image 1656](<2005-musin-extension-delsarte-method-kissing_images/imageFile1656.png>)

![image 1657](<2005-musin-extension-delsarte-method-kissing_images/imageFile1657.png>)

![image 1658](<2005-musin-extension-delsarte-method-kissing_images/imageFile1658.png>)

![image 1659](<2005-musin-extension-delsarte-method-kissing_images/imageFile1659.png>)

![image 1660](<2005-musin-extension-delsarte-method-kissing_images/imageFile1660.png>)

![image 1661](<2005-musin-extension-delsarte-method-kissing_images/imageFile1661.png>)

![image 1662](<2005-musin-extension-delsarte-method-kissing_images/imageFile1662.png>)

![image 1663](<2005-musin-extension-delsarte-method-kissing_images/imageFile1663.png>)

![image 1664](<2005-musin-extension-delsarte-method-kissing_images/imageFile1664.png>)

![image 1665](<2005-musin-extension-delsarte-method-kissing_images/imageFile1665.png>)

![image 1666](<2005-musin-extension-delsarte-method-kissing_images/imageFile1666.png>)

![image 1667](<2005-musin-extension-delsarte-method-kissing_images/imageFile1667.png>)

![image 1668](<2005-musin-extension-delsarte-method-kissing_images/imageFile1668.png>)

![image 1669](<2005-musin-extension-delsarte-method-kissing_images/imageFile1669.png>)

![image 1670](<2005-musin-extension-delsarte-method-kissing_images/imageFile1670.png>)

![image 1671](<2005-musin-extension-delsarte-method-kissing_images/imageFile1671.png>)

![image 1672](<2005-musin-extension-delsarte-method-kissing_images/imageFile1672.png>)

![image 1673](<2005-musin-extension-delsarte-method-kissing_images/imageFile1673.png>)

![image 1674](<2005-musin-extension-delsarte-method-kissing_images/imageFile1674.png>)

![image 1675](<2005-musin-extension-delsarte-method-kissing_images/imageFile1675.png>)

![image 1676](<2005-musin-extension-delsarte-method-kissing_images/imageFile1676.png>)

![image 1677](<2005-musin-extension-delsarte-method-kissing_images/imageFile1677.png>)

![image 1678](<2005-musin-extension-delsarte-method-kissing_images/imageFile1678.png>)

![image 1679](<2005-musin-extension-delsarte-method-kissing_images/imageFile1679.png>)

![image 1680](<2005-musin-extension-delsarte-method-kissing_images/imageFile1680.png>)

![image 1681](<2005-musin-extension-delsarte-method-kissing_images/imageFile1681.png>)

![image 1682](<2005-musin-extension-delsarte-method-kissing_images/imageFile1682.png>)

![image 1683](<2005-musin-extension-delsarte-method-kissing_images/imageFile1683.png>)

![image 1684](<2005-musin-extension-delsarte-method-kissing_images/imageFile1684.png>)

![image 1685](<2005-musin-extension-delsarte-method-kissing_images/imageFile1685.png>)

![image 1686](<2005-musin-extension-delsarte-method-kissing_images/imageFile1686.png>)

![image 1687](<2005-musin-extension-delsarte-method-kissing_images/imageFile1687.png>)

![image 1688](<2005-musin-extension-delsarte-method-kissing_images/imageFile1688.png>)

![image 1689](<2005-musin-extension-delsarte-method-kissing_images/imageFile1689.png>)

![image 1690](<2005-musin-extension-delsarte-method-kissing_images/imageFile1690.png>)

![image 1691](<2005-musin-extension-delsarte-method-kissing_images/imageFile1691.png>)

![image 1692](<2005-musin-extension-delsarte-method-kissing_images/imageFile1692.png>)

![image 1693](<2005-musin-extension-delsarte-method-kissing_images/imageFile1693.png>)

![image 1694](<2005-musin-extension-delsarte-method-kissing_images/imageFile1694.png>)

![image 1695](<2005-musin-extension-delsarte-method-kissing_images/imageFile1695.png>)

![image 1696](<2005-musin-extension-delsarte-method-kissing_images/imageFile1696.png>)

![image 1697](<2005-musin-extension-delsarte-method-kissing_images/imageFile1697.png>)

![image 1698](<2005-musin-extension-delsarte-method-kissing_images/imageFile1698.png>)

![image 1699](<2005-musin-extension-delsarte-method-kissing_images/imageFile1699.png>)

![image 1700](<2005-musin-extension-delsarte-method-kissing_images/imageFile1700.png>)

![image 1701](<2005-musin-extension-delsarte-method-kissing_images/imageFile1701.png>)

![image 1702](<2005-musin-extension-delsarte-method-kissing_images/imageFile1702.png>)

![image 1703](<2005-musin-extension-delsarte-method-kissing_images/imageFile1703.png>)

![image 1704](<2005-musin-extension-delsarte-method-kissing_images/imageFile1704.png>)

![image 1705](<2005-musin-extension-delsarte-method-kissing_images/imageFile1705.png>)

![image 1706](<2005-musin-extension-delsarte-method-kissing_images/imageFile1706.png>)

![image 1707](<2005-musin-extension-delsarte-method-kissing_images/imageFile1707.png>)

![image 1708](<2005-musin-extension-delsarte-method-kissing_images/imageFile1708.png>)

![image 1709](<2005-musin-extension-delsarte-method-kissing_images/imageFile1709.png>)

![image 1710](<2005-musin-extension-delsarte-method-kissing_images/imageFile1710.png>)

![image 1711](<2005-musin-extension-delsarte-method-kissing_images/imageFile1711.png>)

![image 1712](<2005-musin-extension-delsarte-method-kissing_images/imageFile1712.png>)

![image 1713](<2005-musin-extension-delsarte-method-kissing_images/imageFile1713.png>)

![image 1714](<2005-musin-extension-delsarte-method-kissing_images/imageFile1714.png>)

![image 1715](<2005-musin-extension-delsarte-method-kissing_images/imageFile1715.png>)

![image 1716](<2005-musin-extension-delsarte-method-kissing_images/imageFile1716.png>)

![image 1717](<2005-musin-extension-delsarte-method-kissing_images/imageFile1717.png>)

![image 1718](<2005-musin-extension-delsarte-method-kissing_images/imageFile1718.png>)

![image 1719](<2005-musin-extension-delsarte-method-kissing_images/imageFile1719.png>)

![image 1720](<2005-musin-extension-delsarte-method-kissing_images/imageFile1720.png>)

![image 1721](<2005-musin-extension-delsarte-method-kissing_images/imageFile1721.png>)

![image 1722](<2005-musin-extension-delsarte-method-kissing_images/imageFile1722.png>)

![image 1723](<2005-musin-extension-delsarte-method-kissing_images/imageFile1723.png>)

![image 1724](<2005-musin-extension-delsarte-method-kissing_images/imageFile1724.png>)

![image 1725](<2005-musin-extension-delsarte-method-kissing_images/imageFile1725.png>)

![image 1726](<2005-musin-extension-delsarte-method-kissing_images/imageFile1726.png>)

![image 1727](<2005-musin-extension-delsarte-method-kissing_images/imageFile1727.png>)

![image 1728](<2005-musin-extension-delsarte-method-kissing_images/imageFile1728.png>)

![image 1729](<2005-musin-extension-delsarte-method-kissing_images/imageFile1729.png>)

![image 1730](<2005-musin-extension-delsarte-method-kissing_images/imageFile1730.png>)

![image 1731](<2005-musin-extension-delsarte-method-kissing_images/imageFile1731.png>)

![image 1732](<2005-musin-extension-delsarte-method-kissing_images/imageFile1732.png>)

![image 1733](<2005-musin-extension-delsarte-method-kissing_images/imageFile1733.png>)

![image 1734](<2005-musin-extension-delsarte-method-kissing_images/imageFile1734.png>)

![image 1735](<2005-musin-extension-delsarte-method-kissing_images/imageFile1735.png>)

![image 1736](<2005-musin-extension-delsarte-method-kissing_images/imageFile1736.png>)

![image 1737](<2005-musin-extension-delsarte-method-kissing_images/imageFile1737.png>)

![image 1738](<2005-musin-extension-delsarte-method-kissing_images/imageFile1738.png>)

![image 1739](<2005-musin-extension-delsarte-method-kissing_images/imageFile1739.png>)

![image 1740](<2005-musin-extension-delsarte-method-kissing_images/imageFile1740.png>)

![image 1741](<2005-musin-extension-delsarte-method-kissing_images/imageFile1741.png>)

![image 1742](<2005-musin-extension-delsarte-method-kissing_images/imageFile1742.png>)

![image 1743](<2005-musin-extension-delsarte-method-kissing_images/imageFile1743.png>)

![image 1744](<2005-musin-extension-delsarte-method-kissing_images/imageFile1744.png>)

![image 1745](<2005-musin-extension-delsarte-method-kissing_images/imageFile1745.png>)

![image 1746](<2005-musin-extension-delsarte-method-kissing_images/imageFile1746.png>)

![image 1747](<2005-musin-extension-delsarte-method-kissing_images/imageFile1747.png>)

![image 1748](<2005-musin-extension-delsarte-method-kissing_images/imageFile1748.png>)

![image 1749](<2005-musin-extension-delsarte-method-kissing_images/imageFile1749.png>)

![image 1750](<2005-musin-extension-delsarte-method-kissing_images/imageFile1750.png>)

![image 1751](<2005-musin-extension-delsarte-method-kissing_images/imageFile1751.png>)

![image 1752](<2005-musin-extension-delsarte-method-kissing_images/imageFile1752.png>)

![image 1753](<2005-musin-extension-delsarte-method-kissing_images/imageFile1753.png>)

![image 1754](<2005-musin-extension-delsarte-method-kissing_images/imageFile1754.png>)

![image 1755](<2005-musin-extension-delsarte-method-kissing_images/imageFile1755.png>)

![image 1756](<2005-musin-extension-delsarte-method-kissing_images/imageFile1756.png>)

![image 1757](<2005-musin-extension-delsarte-method-kissing_images/imageFile1757.png>)

![image 1758](<2005-musin-extension-delsarte-method-kissing_images/imageFile1758.png>)

![image 1759](<2005-musin-extension-delsarte-method-kissing_images/imageFile1759.png>)

![image 1760](<2005-musin-extension-delsarte-method-kissing_images/imageFile1760.png>)

![image 1761](<2005-musin-extension-delsarte-method-kissing_images/imageFile1761.png>)

![image 1762](<2005-musin-extension-delsarte-method-kissing_images/imageFile1762.png>)

![image 1763](<2005-musin-extension-delsarte-method-kissing_images/imageFile1763.png>)

![image 1764](<2005-musin-extension-delsarte-method-kissing_images/imageFile1764.png>)

![image 1765](<2005-musin-extension-delsarte-method-kissing_images/imageFile1765.png>)

![image 1766](<2005-musin-extension-delsarte-method-kissing_images/imageFile1766.png>)

![image 1767](<2005-musin-extension-delsarte-method-kissing_images/imageFile1767.png>)

![image 1768](<2005-musin-extension-delsarte-method-kissing_images/imageFile1768.png>)

![image 1769](<2005-musin-extension-delsarte-method-kissing_images/imageFile1769.png>)

![image 1770](<2005-musin-extension-delsarte-method-kissing_images/imageFile1770.png>)

![image 1771](<2005-musin-extension-delsarte-method-kissing_images/imageFile1771.png>)

![image 1772](<2005-musin-extension-delsarte-method-kissing_images/imageFile1772.png>)

![image 1773](<2005-musin-extension-delsarte-method-kissing_images/imageFile1773.png>)

![image 1774](<2005-musin-extension-delsarte-method-kissing_images/imageFile1774.png>)

![image 1775](<2005-musin-extension-delsarte-method-kissing_images/imageFile1775.png>)

![image 1776](<2005-musin-extension-delsarte-method-kissing_images/imageFile1776.png>)

![image 1777](<2005-musin-extension-delsarte-method-kissing_images/imageFile1777.png>)

![image 1778](<2005-musin-extension-delsarte-method-kissing_images/imageFile1778.png>)

![image 1779](<2005-musin-extension-delsarte-method-kissing_images/imageFile1779.png>)

![image 1780](<2005-musin-extension-delsarte-method-kissing_images/imageFile1780.png>)

![image 1781](<2005-musin-extension-delsarte-method-kissing_images/imageFile1781.png>)

![image 1782](<2005-musin-extension-delsarte-method-kissing_images/imageFile1782.png>)

![image 1783](<2005-musin-extension-delsarte-method-kissing_images/imageFile1783.png>)

![image 1784](<2005-musin-extension-delsarte-method-kissing_images/imageFile1784.png>)

![image 1785](<2005-musin-extension-delsarte-method-kissing_images/imageFile1785.png>)

![image 1786](<2005-musin-extension-delsarte-method-kissing_images/imageFile1786.png>)

![image 1787](<2005-musin-extension-delsarte-method-kissing_images/imageFile1787.png>)

![image 1788](<2005-musin-extension-delsarte-method-kissing_images/imageFile1788.png>)

![image 1789](<2005-musin-extension-delsarte-method-kissing_images/imageFile1789.png>)

![image 1790](<2005-musin-extension-delsarte-method-kissing_images/imageFile1790.png>)

![image 1791](<2005-musin-extension-delsarte-method-kissing_images/imageFile1791.png>)

![image 1792](<2005-musin-extension-delsarte-method-kissing_images/imageFile1792.png>)

![image 1793](<2005-musin-extension-delsarte-method-kissing_images/imageFile1793.png>)

![image 1794](<2005-musin-extension-delsarte-method-kissing_images/imageFile1794.png>)

![image 1795](<2005-musin-extension-delsarte-method-kissing_images/imageFile1795.png>)

![image 1796](<2005-musin-extension-delsarte-method-kissing_images/imageFile1796.png>)

![image 1797](<2005-musin-extension-delsarte-method-kissing_images/imageFile1797.png>)

![image 1798](<2005-musin-extension-delsarte-method-kissing_images/imageFile1798.png>)

![image 1799](<2005-musin-extension-delsarte-method-kissing_images/imageFile1799.png>)

![image 1800](<2005-musin-extension-delsarte-method-kissing_images/imageFile1800.png>)

![image 1801](<2005-musin-extension-delsarte-method-kissing_images/imageFile1801.png>)

![image 1802](<2005-musin-extension-delsarte-method-kissing_images/imageFile1802.png>)

![image 1803](<2005-musin-extension-delsarte-method-kissing_images/imageFile1803.png>)

![image 1804](<2005-musin-extension-delsarte-method-kissing_images/imageFile1804.png>)

![image 1805](<2005-musin-extension-delsarte-method-kissing_images/imageFile1805.png>)

![image 1806](<2005-musin-extension-delsarte-method-kissing_images/imageFile1806.png>)

![image 1807](<2005-musin-extension-delsarte-method-kissing_images/imageFile1807.png>)

![image 1808](<2005-musin-extension-delsarte-method-kissing_images/imageFile1808.png>)

![image 1809](<2005-musin-extension-delsarte-method-kissing_images/imageFile1809.png>)

![image 1810](<2005-musin-extension-delsarte-method-kissing_images/imageFile1810.png>)

![image 1811](<2005-musin-extension-delsarte-method-kissing_images/imageFile1811.png>)

![image 1812](<2005-musin-extension-delsarte-method-kissing_images/imageFile1812.png>)

![image 1813](<2005-musin-extension-delsarte-method-kissing_images/imageFile1813.png>)

![image 1814](<2005-musin-extension-delsarte-method-kissing_images/imageFile1814.png>)

![image 1815](<2005-musin-extension-delsarte-method-kissing_images/imageFile1815.png>)

![image 1816](<2005-musin-extension-delsarte-method-kissing_images/imageFile1816.png>)

![image 1817](<2005-musin-extension-delsarte-method-kissing_images/imageFile1817.png>)

![image 1818](<2005-musin-extension-delsarte-method-kissing_images/imageFile1818.png>)

![image 1819](<2005-musin-extension-delsarte-method-kissing_images/imageFile1819.png>)

![image 1820](<2005-musin-extension-delsarte-method-kissing_images/imageFile1820.png>)

![image 1821](<2005-musin-extension-delsarte-method-kissing_images/imageFile1821.png>)

![image 1822](<2005-musin-extension-delsarte-method-kissing_images/imageFile1822.png>)

![image 1823](<2005-musin-extension-delsarte-method-kissing_images/imageFile1823.png>)

![image 1824](<2005-musin-extension-delsarte-method-kissing_images/imageFile1824.png>)

![image 1825](<2005-musin-extension-delsarte-method-kissing_images/imageFile1825.png>)

![image 1826](<2005-musin-extension-delsarte-method-kissing_images/imageFile1826.png>)

![image 1827](<2005-musin-extension-delsarte-method-kissing_images/imageFile1827.png>)

![image 1828](<2005-musin-extension-delsarte-method-kissing_images/imageFile1828.png>)

![image 1829](<2005-musin-extension-delsarte-method-kissing_images/imageFile1829.png>)

![image 1830](<2005-musin-extension-delsarte-method-kissing_images/imageFile1830.png>)

![image 1831](<2005-musin-extension-delsarte-method-kissing_images/imageFile1831.png>)

![image 1832](<2005-musin-extension-delsarte-method-kissing_images/imageFile1832.png>)

![image 1833](<2005-musin-extension-delsarte-method-kissing_images/imageFile1833.png>)

![image 1834](<2005-musin-extension-delsarte-method-kissing_images/imageFile1834.png>)

![image 1835](<2005-musin-extension-delsarte-method-kissing_images/imageFile1835.png>)

![image 1836](<2005-musin-extension-delsarte-method-kissing_images/imageFile1836.png>)

![image 1837](<2005-musin-extension-delsarte-method-kissing_images/imageFile1837.png>)

![image 1838](<2005-musin-extension-delsarte-method-kissing_images/imageFile1838.png>)

![image 1839](<2005-musin-extension-delsarte-method-kissing_images/imageFile1839.png>)

![image 1840](<2005-musin-extension-delsarte-method-kissing_images/imageFile1840.png>)

![image 1841](<2005-musin-extension-delsarte-method-kissing_images/imageFile1841.png>)

![image 1842](<2005-musin-extension-delsarte-method-kissing_images/imageFile1842.png>)

![image 1843](<2005-musin-extension-delsarte-method-kissing_images/imageFile1843.png>)

![image 1844](<2005-musin-extension-delsarte-method-kissing_images/imageFile1844.png>)

![image 1845](<2005-musin-extension-delsarte-method-kissing_images/imageFile1845.png>)

![image 1846](<2005-musin-extension-delsarte-method-kissing_images/imageFile1846.png>)

![image 1847](<2005-musin-extension-delsarte-method-kissing_images/imageFile1847.png>)

![image 1848](<2005-musin-extension-delsarte-method-kissing_images/imageFile1848.png>)

![image 1849](<2005-musin-extension-delsarte-method-kissing_images/imageFile1849.png>)

![image 1850](<2005-musin-extension-delsarte-method-kissing_images/imageFile1850.png>)

![image 1851](<2005-musin-extension-delsarte-method-kissing_images/imageFile1851.png>)

![image 1852](<2005-musin-extension-delsarte-method-kissing_images/imageFile1852.png>)

![image 1853](<2005-musin-extension-delsarte-method-kissing_images/imageFile1853.png>)

![image 1854](<2005-musin-extension-delsarte-method-kissing_images/imageFile1854.png>)

![image 1855](<2005-musin-extension-delsarte-method-kissing_images/imageFile1855.png>)

![image 1856](<2005-musin-extension-delsarte-method-kissing_images/imageFile1856.png>)

![image 1857](<2005-musin-extension-delsarte-method-kissing_images/imageFile1857.png>)

![image 1858](<2005-musin-extension-delsarte-method-kissing_images/imageFile1858.png>)

![image 1859](<2005-musin-extension-delsarte-method-kissing_images/imageFile1859.png>)

![image 1860](<2005-musin-extension-delsarte-method-kissing_images/imageFile1860.png>)

![image 1861](<2005-musin-extension-delsarte-method-kissing_images/imageFile1861.png>)

![image 1862](<2005-musin-extension-delsarte-method-kissing_images/imageFile1862.png>)

![image 1863](<2005-musin-extension-delsarte-method-kissing_images/imageFile1863.png>)

![image 1864](<2005-musin-extension-delsarte-method-kissing_images/imageFile1864.png>)

![image 1865](<2005-musin-extension-delsarte-method-kissing_images/imageFile1865.png>)

![image 1866](<2005-musin-extension-delsarte-method-kissing_images/imageFile1866.png>)

![image 1867](<2005-musin-extension-delsarte-method-kissing_images/imageFile1867.png>)

![image 1868](<2005-musin-extension-delsarte-method-kissing_images/imageFile1868.png>)

![image 1869](<2005-musin-extension-delsarte-method-kissing_images/imageFile1869.png>)

![image 1870](<2005-musin-extension-delsarte-method-kissing_images/imageFile1870.png>)

![image 1871](<2005-musin-extension-delsarte-method-kissing_images/imageFile1871.png>)

![image 1872](<2005-musin-extension-delsarte-method-kissing_images/imageFile1872.png>)

![image 1873](<2005-musin-extension-delsarte-method-kissing_images/imageFile1873.png>)

![image 1874](<2005-musin-extension-delsarte-method-kissing_images/imageFile1874.png>)

![image 1875](<2005-musin-extension-delsarte-method-kissing_images/imageFile1875.png>)

![image 1876](<2005-musin-extension-delsarte-method-kissing_images/imageFile1876.png>)

![image 1877](<2005-musin-extension-delsarte-method-kissing_images/imageFile1877.png>)

![image 1878](<2005-musin-extension-delsarte-method-kissing_images/imageFile1878.png>)

![image 1879](<2005-musin-extension-delsarte-method-kissing_images/imageFile1879.png>)

![image 1880](<2005-musin-extension-delsarte-method-kissing_images/imageFile1880.png>)

![image 1881](<2005-musin-extension-delsarte-method-kissing_images/imageFile1881.png>)

![image 1882](<2005-musin-extension-delsarte-method-kissing_images/imageFile1882.png>)

![image 1883](<2005-musin-extension-delsarte-method-kissing_images/imageFile1883.png>)

![image 1884](<2005-musin-extension-delsarte-method-kissing_images/imageFile1884.png>)

![image 1885](<2005-musin-extension-delsarte-method-kissing_images/imageFile1885.png>)

![image 1886](<2005-musin-extension-delsarte-method-kissing_images/imageFile1886.png>)

![image 1887](<2005-musin-extension-delsarte-method-kissing_images/imageFile1887.png>)

![image 1888](<2005-musin-extension-delsarte-method-kissing_images/imageFile1888.png>)

![image 1889](<2005-musin-extension-delsarte-method-kissing_images/imageFile1889.png>)

![image 1890](<2005-musin-extension-delsarte-method-kissing_images/imageFile1890.png>)

![image 1891](<2005-musin-extension-delsarte-method-kissing_images/imageFile1891.png>)

![image 1892](<2005-musin-extension-delsarte-method-kissing_images/imageFile1892.png>)

![image 1893](<2005-musin-extension-delsarte-method-kissing_images/imageFile1893.png>)

![image 1894](<2005-musin-extension-delsarte-method-kissing_images/imageFile1894.png>)

![image 1895](<2005-musin-extension-delsarte-method-kissing_images/imageFile1895.png>)

![image 1896](<2005-musin-extension-delsarte-method-kissing_images/imageFile1896.png>)

![image 1897](<2005-musin-extension-delsarte-method-kissing_images/imageFile1897.png>)

![image 1898](<2005-musin-extension-delsarte-method-kissing_images/imageFile1898.png>)

![image 1899](<2005-musin-extension-delsarte-method-kissing_images/imageFile1899.png>)

![image 1900](<2005-musin-extension-delsarte-method-kissing_images/imageFile1900.png>)

![image 1901](<2005-musin-extension-delsarte-method-kissing_images/imageFile1901.png>)

![image 1902](<2005-musin-extension-delsarte-method-kissing_images/imageFile1902.png>)

![image 1903](<2005-musin-extension-delsarte-method-kissing_images/imageFile1903.png>)

![image 1904](<2005-musin-extension-delsarte-method-kissing_images/imageFile1904.png>)

![image 1905](<2005-musin-extension-delsarte-method-kissing_images/imageFile1905.png>)

![image 1906](<2005-musin-extension-delsarte-method-kissing_images/imageFile1906.png>)

![image 1907](<2005-musin-extension-delsarte-method-kissing_images/imageFile1907.png>)

![image 1908](<2005-musin-extension-delsarte-method-kissing_images/imageFile1908.png>)

![image 1909](<2005-musin-extension-delsarte-method-kissing_images/imageFile1909.png>)

![image 1910](<2005-musin-extension-delsarte-method-kissing_images/imageFile1910.png>)

![image 1911](<2005-musin-extension-delsarte-method-kissing_images/imageFile1911.png>)

![image 1912](<2005-musin-extension-delsarte-method-kissing_images/imageFile1912.png>)

![image 1913](<2005-musin-extension-delsarte-method-kissing_images/imageFile1913.png>)

![image 1914](<2005-musin-extension-delsarte-method-kissing_images/imageFile1914.png>)

![image 1915](<2005-musin-extension-delsarte-method-kissing_images/imageFile1915.png>)

![image 1916](<2005-musin-extension-delsarte-method-kissing_images/imageFile1916.png>)

![image 1917](<2005-musin-extension-delsarte-method-kissing_images/imageFile1917.png>)

![image 1918](<2005-musin-extension-delsarte-method-kissing_images/imageFile1918.png>)

![image 1919](<2005-musin-extension-delsarte-method-kissing_images/imageFile1919.png>)

![image 1920](<2005-musin-extension-delsarte-method-kissing_images/imageFile1920.png>)

![image 1921](<2005-musin-extension-delsarte-method-kissing_images/imageFile1921.png>)

![image 1922](<2005-musin-extension-delsarte-method-kissing_images/imageFile1922.png>)

![image 1923](<2005-musin-extension-delsarte-method-kissing_images/imageFile1923.png>)

![image 1924](<2005-musin-extension-delsarte-method-kissing_images/imageFile1924.png>)

![image 1925](<2005-musin-extension-delsarte-method-kissing_images/imageFile1925.png>)

![image 1926](<2005-musin-extension-delsarte-method-kissing_images/imageFile1926.png>)

![image 1927](<2005-musin-extension-delsarte-method-kissing_images/imageFile1927.png>)

![image 1928](<2005-musin-extension-delsarte-method-kissing_images/imageFile1928.png>)

![image 1929](<2005-musin-extension-delsarte-method-kissing_images/imageFile1929.png>)

![image 1930](<2005-musin-extension-delsarte-method-kissing_images/imageFile1930.png>)

![image 1931](<2005-musin-extension-delsarte-method-kissing_images/imageFile1931.png>)

![image 1932](<2005-musin-extension-delsarte-method-kissing_images/imageFile1932.png>)

![image 1933](<2005-musin-extension-delsarte-method-kissing_images/imageFile1933.png>)

![image 1934](<2005-musin-extension-delsarte-method-kissing_images/imageFile1934.png>)

![image 1935](<2005-musin-extension-delsarte-method-kissing_images/imageFile1935.png>)

![image 1936](<2005-musin-extension-delsarte-method-kissing_images/imageFile1936.png>)

![image 1937](<2005-musin-extension-delsarte-method-kissing_images/imageFile1937.png>)

![image 1938](<2005-musin-extension-delsarte-method-kissing_images/imageFile1938.png>)

![image 1939](<2005-musin-extension-delsarte-method-kissing_images/imageFile1939.png>)

![image 1940](<2005-musin-extension-delsarte-method-kissing_images/imageFile1940.png>)

![image 1941](<2005-musin-extension-delsarte-method-kissing_images/imageFile1941.png>)

![image 1942](<2005-musin-extension-delsarte-method-kissing_images/imageFile1942.png>)

![image 1943](<2005-musin-extension-delsarte-method-kissing_images/imageFile1943.png>)

![image 1944](<2005-musin-extension-delsarte-method-kissing_images/imageFile1944.png>)

![image 1945](<2005-musin-extension-delsarte-method-kissing_images/imageFile1945.png>)

![image 1946](<2005-musin-extension-delsarte-method-kissing_images/imageFile1946.png>)

![image 1947](<2005-musin-extension-delsarte-method-kissing_images/imageFile1947.png>)

![image 1948](<2005-musin-extension-delsarte-method-kissing_images/imageFile1948.png>)

![image 1949](<2005-musin-extension-delsarte-method-kissing_images/imageFile1949.png>)

![image 1950](<2005-musin-extension-delsarte-method-kissing_images/imageFile1950.png>)

![image 1951](<2005-musin-extension-delsarte-method-kissing_images/imageFile1951.png>)

![image 1952](<2005-musin-extension-delsarte-method-kissing_images/imageFile1952.png>)

![image 1953](<2005-musin-extension-delsarte-method-kissing_images/imageFile1953.png>)

![image 1954](<2005-musin-extension-delsarte-method-kissing_images/imageFile1954.png>)

![image 1955](<2005-musin-extension-delsarte-method-kissing_images/imageFile1955.png>)

![image 1956](<2005-musin-extension-delsarte-method-kissing_images/imageFile1956.png>)

![image 1957](<2005-musin-extension-delsarte-method-kissing_images/imageFile1957.png>)

![image 1958](<2005-musin-extension-delsarte-method-kissing_images/imageFile1958.png>)

![image 1959](<2005-musin-extension-delsarte-method-kissing_images/imageFile1959.png>)

![image 1960](<2005-musin-extension-delsarte-method-kissing_images/imageFile1960.png>)

![image 1961](<2005-musin-extension-delsarte-method-kissing_images/imageFile1961.png>)

![image 1962](<2005-musin-extension-delsarte-method-kissing_images/imageFile1962.png>)

![image 1963](<2005-musin-extension-delsarte-method-kissing_images/imageFile1963.png>)

![image 1964](<2005-musin-extension-delsarte-method-kissing_images/imageFile1964.png>)

![image 1965](<2005-musin-extension-delsarte-method-kissing_images/imageFile1965.png>)

![image 1966](<2005-musin-extension-delsarte-method-kissing_images/imageFile1966.png>)

![image 1967](<2005-musin-extension-delsarte-method-kissing_images/imageFile1967.png>)

![image 1968](<2005-musin-extension-delsarte-method-kissing_images/imageFile1968.png>)

![image 1969](<2005-musin-extension-delsarte-method-kissing_images/imageFile1969.png>)

![image 1970](<2005-musin-extension-delsarte-method-kissing_images/imageFile1970.png>)

![image 1971](<2005-musin-extension-delsarte-method-kissing_images/imageFile1971.png>)

![image 1972](<2005-musin-extension-delsarte-method-kissing_images/imageFile1972.png>)

![image 1973](<2005-musin-extension-delsarte-method-kissing_images/imageFile1973.png>)

![image 1974](<2005-musin-extension-delsarte-method-kissing_images/imageFile1974.png>)

![image 1975](<2005-musin-extension-delsarte-method-kissing_images/imageFile1975.png>)

![image 1976](<2005-musin-extension-delsarte-method-kissing_images/imageFile1976.png>)

![image 1977](<2005-musin-extension-delsarte-method-kissing_images/imageFile1977.png>)

![image 1978](<2005-musin-extension-delsarte-method-kissing_images/imageFile1978.png>)

![image 1979](<2005-musin-extension-delsarte-method-kissing_images/imageFile1979.png>)

![image 1980](<2005-musin-extension-delsarte-method-kissing_images/imageFile1980.png>)

![image 1981](<2005-musin-extension-delsarte-method-kissing_images/imageFile1981.png>)

![image 1982](<2005-musin-extension-delsarte-method-kissing_images/imageFile1982.png>)

![image 1983](<2005-musin-extension-delsarte-method-kissing_images/imageFile1983.png>)

![image 1984](<2005-musin-extension-delsarte-method-kissing_images/imageFile1984.png>)

![image 1985](<2005-musin-extension-delsarte-method-kissing_images/imageFile1985.png>)

![image 1986](<2005-musin-extension-delsarte-method-kissing_images/imageFile1986.png>)

![image 1987](<2005-musin-extension-delsarte-method-kissing_images/imageFile1987.png>)

![image 1988](<2005-musin-extension-delsarte-method-kissing_images/imageFile1988.png>)

![image 1989](<2005-musin-extension-delsarte-method-kissing_images/imageFile1989.png>)

![image 1990](<2005-musin-extension-delsarte-method-kissing_images/imageFile1990.png>)

![image 1991](<2005-musin-extension-delsarte-method-kissing_images/imageFile1991.png>)

![image 1992](<2005-musin-extension-delsarte-method-kissing_images/imageFile1992.png>)

![image 1993](<2005-musin-extension-delsarte-method-kissing_images/imageFile1993.png>)

![image 1994](<2005-musin-extension-delsarte-method-kissing_images/imageFile1994.png>)

![image 1995](<2005-musin-extension-delsarte-method-kissing_images/imageFile1995.png>)

![image 1996](<2005-musin-extension-delsarte-method-kissing_images/imageFile1996.png>)

![image 1997](<2005-musin-extension-delsarte-method-kissing_images/imageFile1997.png>)

![image 1998](<2005-musin-extension-delsarte-method-kissing_images/imageFile1998.png>)

![image 1999](<2005-musin-extension-delsarte-method-kissing_images/imageFile1999.png>)

![image 2000](<2005-musin-extension-delsarte-method-kissing_images/imageFile2000.png>)

![image 2001](<2005-musin-extension-delsarte-method-kissing_images/imageFile2001.png>)

![image 2002](<2005-musin-extension-delsarte-method-kissing_images/imageFile2002.png>)

![image 2003](<2005-musin-extension-delsarte-method-kissing_images/imageFile2003.png>)

![image 2004](<2005-musin-extension-delsarte-method-kissing_images/imageFile2004.png>)

![image 2005](<2005-musin-extension-delsarte-method-kissing_images/imageFile2005.png>)

![image 2006](<2005-musin-extension-delsarte-method-kissing_images/imageFile2006.png>)

![image 2007](<2005-musin-extension-delsarte-method-kissing_images/imageFile2007.png>)

![image 2008](<2005-musin-extension-delsarte-method-kissing_images/imageFile2008.png>)

![image 2009](<2005-musin-extension-delsarte-method-kissing_images/imageFile2009.png>)

![image 2010](<2005-musin-extension-delsarte-method-kissing_images/imageFile2010.png>)

![image 2011](<2005-musin-extension-delsarte-method-kissing_images/imageFile2011.png>)

![image 2012](<2005-musin-extension-delsarte-method-kissing_images/imageFile2012.png>)

![image 2013](<2005-musin-extension-delsarte-method-kissing_images/imageFile2013.png>)

![image 2014](<2005-musin-extension-delsarte-method-kissing_images/imageFile2014.png>)

![image 2015](<2005-musin-extension-delsarte-method-kissing_images/imageFile2015.png>)

![image 2016](<2005-musin-extension-delsarte-method-kissing_images/imageFile2016.png>)

![image 2017](<2005-musin-extension-delsarte-method-kissing_images/imageFile2017.png>)

![image 2018](<2005-musin-extension-delsarte-method-kissing_images/imageFile2018.png>)

![image 2019](<2005-musin-extension-delsarte-method-kissing_images/imageFile2019.png>)

![image 2020](<2005-musin-extension-delsarte-method-kissing_images/imageFile2020.png>)

![image 2021](<2005-musin-extension-delsarte-method-kissing_images/imageFile2021.png>)

![image 2022](<2005-musin-extension-delsarte-method-kissing_images/imageFile2022.png>)

![image 2023](<2005-musin-extension-delsarte-method-kissing_images/imageFile2023.png>)

![image 2024](<2005-musin-extension-delsarte-method-kissing_images/imageFile2024.png>)

![image 2025](<2005-musin-extension-delsarte-method-kissing_images/imageFile2025.png>)

![image 2026](<2005-musin-extension-delsarte-method-kissing_images/imageFile2026.png>)

![image 2027](<2005-musin-extension-delsarte-method-kissing_images/imageFile2027.png>)

![image 2028](<2005-musin-extension-delsarte-method-kissing_images/imageFile2028.png>)

![image 2029](<2005-musin-extension-delsarte-method-kissing_images/imageFile2029.png>)

![image 2030](<2005-musin-extension-delsarte-method-kissing_images/imageFile2030.png>)

![image 2031](<2005-musin-extension-delsarte-method-kissing_images/imageFile2031.png>)

![image 2032](<2005-musin-extension-delsarte-method-kissing_images/imageFile2032.png>)

![image 2033](<2005-musin-extension-delsarte-method-kissing_images/imageFile2033.png>)

![image 2034](<2005-musin-extension-delsarte-method-kissing_images/imageFile2034.png>)

![image 2035](<2005-musin-extension-delsarte-method-kissing_images/imageFile2035.png>)

![image 2036](<2005-musin-extension-delsarte-method-kissing_images/imageFile2036.png>)

![image 2037](<2005-musin-extension-delsarte-method-kissing_images/imageFile2037.png>)

![image 2038](<2005-musin-extension-delsarte-method-kissing_images/imageFile2038.png>)

![image 2039](<2005-musin-extension-delsarte-method-kissing_images/imageFile2039.png>)

![image 2040](<2005-musin-extension-delsarte-method-kissing_images/imageFile2040.png>)

![image 2041](<2005-musin-extension-delsarte-method-kissing_images/imageFile2041.png>)

![image 2042](<2005-musin-extension-delsarte-method-kissing_images/imageFile2042.png>)

![image 2043](<2005-musin-extension-delsarte-method-kissing_images/imageFile2043.png>)

![image 2044](<2005-musin-extension-delsarte-method-kissing_images/imageFile2044.png>)

![image 2045](<2005-musin-extension-delsarte-method-kissing_images/imageFile2045.png>)

![image 2046](<2005-musin-extension-delsarte-method-kissing_images/imageFile2046.png>)

![image 2047](<2005-musin-extension-delsarte-method-kissing_images/imageFile2047.png>)

![image 2048](<2005-musin-extension-delsarte-method-kissing_images/imageFile2048.png>)

![image 2049](<2005-musin-extension-delsarte-method-kissing_images/imageFile2049.png>)

![image 2050](<2005-musin-extension-delsarte-method-kissing_images/imageFile2050.png>)

![image 2051](<2005-musin-extension-delsarte-method-kissing_images/imageFile2051.png>)

![image 2052](<2005-musin-extension-delsarte-method-kissing_images/imageFile2052.png>)

![image 2053](<2005-musin-extension-delsarte-method-kissing_images/imageFile2053.png>)

![image 2054](<2005-musin-extension-delsarte-method-kissing_images/imageFile2054.png>)

![image 2055](<2005-musin-extension-delsarte-method-kissing_images/imageFile2055.png>)

![image 2056](<2005-musin-extension-delsarte-method-kissing_images/imageFile2056.png>)

![image 2057](<2005-musin-extension-delsarte-method-kissing_images/imageFile2057.png>)

![image 2058](<2005-musin-extension-delsarte-method-kissing_images/imageFile2058.png>)

![image 2059](<2005-musin-extension-delsarte-method-kissing_images/imageFile2059.png>)

![image 2060](<2005-musin-extension-delsarte-method-kissing_images/imageFile2060.png>)

![image 2061](<2005-musin-extension-delsarte-method-kissing_images/imageFile2061.png>)

![image 2062](<2005-musin-extension-delsarte-method-kissing_images/imageFile2062.png>)

![image 2063](<2005-musin-extension-delsarte-method-kissing_images/imageFile2063.png>)

![image 2064](<2005-musin-extension-delsarte-method-kissing_images/imageFile2064.png>)

![image 2065](<2005-musin-extension-delsarte-method-kissing_images/imageFile2065.png>)

![image 2066](<2005-musin-extension-delsarte-method-kissing_images/imageFile2066.png>)

![image 2067](<2005-musin-extension-delsarte-method-kissing_images/imageFile2067.png>)

![image 2068](<2005-musin-extension-delsarte-method-kissing_images/imageFile2068.png>)

![image 2069](<2005-musin-extension-delsarte-method-kissing_images/imageFile2069.png>)

![image 2070](<2005-musin-extension-delsarte-method-kissing_images/imageFile2070.png>)

![image 2071](<2005-musin-extension-delsarte-method-kissing_images/imageFile2071.png>)

![image 2072](<2005-musin-extension-delsarte-method-kissing_images/imageFile2072.png>)

![image 2073](<2005-musin-extension-delsarte-method-kissing_images/imageFile2073.png>)

![image 2074](<2005-musin-extension-delsarte-method-kissing_images/imageFile2074.png>)

![image 2075](<2005-musin-extension-delsarte-method-kissing_images/imageFile2075.png>)

![image 2076](<2005-musin-extension-delsarte-method-kissing_images/imageFile2076.png>)

![image 2077](<2005-musin-extension-delsarte-method-kissing_images/imageFile2077.png>)

![image 2078](<2005-musin-extension-delsarte-method-kissing_images/imageFile2078.png>)

![image 2079](<2005-musin-extension-delsarte-method-kissing_images/imageFile2079.png>)

![image 2080](<2005-musin-extension-delsarte-method-kissing_images/imageFile2080.png>)

![image 2081](<2005-musin-extension-delsarte-method-kissing_images/imageFile2081.png>)

![image 2082](<2005-musin-extension-delsarte-method-kissing_images/imageFile2082.png>)

![image 2083](<2005-musin-extension-delsarte-method-kissing_images/imageFile2083.png>)

![image 2084](<2005-musin-extension-delsarte-method-kissing_images/imageFile2084.png>)

![image 2085](<2005-musin-extension-delsarte-method-kissing_images/imageFile2085.png>)

![image 2086](<2005-musin-extension-delsarte-method-kissing_images/imageFile2086.png>)

![image 2087](<2005-musin-extension-delsarte-method-kissing_images/imageFile2087.png>)

![image 2088](<2005-musin-extension-delsarte-method-kissing_images/imageFile2088.png>)

![image 2089](<2005-musin-extension-delsarte-method-kissing_images/imageFile2089.png>)

![image 2090](<2005-musin-extension-delsarte-method-kissing_images/imageFile2090.png>)

![image 2091](<2005-musin-extension-delsarte-method-kissing_images/imageFile2091.png>)

![image 2092](<2005-musin-extension-delsarte-method-kissing_images/imageFile2092.png>)

![image 2093](<2005-musin-extension-delsarte-method-kissing_images/imageFile2093.png>)

![image 2094](<2005-musin-extension-delsarte-method-kissing_images/imageFile2094.png>)

![image 2095](<2005-musin-extension-delsarte-method-kissing_images/imageFile2095.png>)

![image 2096](<2005-musin-extension-delsarte-method-kissing_images/imageFile2096.png>)

![image 2097](<2005-musin-extension-delsarte-method-kissing_images/imageFile2097.png>)

![image 2098](<2005-musin-extension-delsarte-method-kissing_images/imageFile2098.png>)

![image 2099](<2005-musin-extension-delsarte-method-kissing_images/imageFile2099.png>)

![image 2100](<2005-musin-extension-delsarte-method-kissing_images/imageFile2100.png>)

![image 2101](<2005-musin-extension-delsarte-method-kissing_images/imageFile2101.png>)

![image 2102](<2005-musin-extension-delsarte-method-kissing_images/imageFile2102.png>)

![image 2103](<2005-musin-extension-delsarte-method-kissing_images/imageFile2103.png>)

![image 2104](<2005-musin-extension-delsarte-method-kissing_images/imageFile2104.png>)

![image 2105](<2005-musin-extension-delsarte-method-kissing_images/imageFile2105.png>)

![image 2106](<2005-musin-extension-delsarte-method-kissing_images/imageFile2106.png>)

![image 2107](<2005-musin-extension-delsarte-method-kissing_images/imageFile2107.png>)

![image 2108](<2005-musin-extension-delsarte-method-kissing_images/imageFile2108.png>)

![image 2109](<2005-musin-extension-delsarte-method-kissing_images/imageFile2109.png>)

![image 2110](<2005-musin-extension-delsarte-method-kissing_images/imageFile2110.png>)

![image 2111](<2005-musin-extension-delsarte-method-kissing_images/imageFile2111.png>)

![image 2112](<2005-musin-extension-delsarte-method-kissing_images/imageFile2112.png>)

![image 2113](<2005-musin-extension-delsarte-method-kissing_images/imageFile2113.png>)

![image 2114](<2005-musin-extension-delsarte-method-kissing_images/imageFile2114.png>)

![image 2115](<2005-musin-extension-delsarte-method-kissing_images/imageFile2115.png>)

![image 2116](<2005-musin-extension-delsarte-method-kissing_images/imageFile2116.png>)

![image 2117](<2005-musin-extension-delsarte-method-kissing_images/imageFile2117.png>)

![image 2118](<2005-musin-extension-delsarte-method-kissing_images/imageFile2118.png>)

![image 2119](<2005-musin-extension-delsarte-method-kissing_images/imageFile2119.png>)

![image 2120](<2005-musin-extension-delsarte-method-kissing_images/imageFile2120.png>)

![image 2121](<2005-musin-extension-delsarte-method-kissing_images/imageFile2121.png>)

![image 2122](<2005-musin-extension-delsarte-method-kissing_images/imageFile2122.png>)

![image 2123](<2005-musin-extension-delsarte-method-kissing_images/imageFile2123.png>)

![image 2124](<2005-musin-extension-delsarte-method-kissing_images/imageFile2124.png>)

![image 2125](<2005-musin-extension-delsarte-method-kissing_images/imageFile2125.png>)

![image 2126](<2005-musin-extension-delsarte-method-kissing_images/imageFile2126.png>)

![image 2127](<2005-musin-extension-delsarte-method-kissing_images/imageFile2127.png>)

![image 2128](<2005-musin-extension-delsarte-method-kissing_images/imageFile2128.png>)

![image 2129](<2005-musin-extension-delsarte-method-kissing_images/imageFile2129.png>)

![image 2130](<2005-musin-extension-delsarte-method-kissing_images/imageFile2130.png>)

![image 2131](<2005-musin-extension-delsarte-method-kissing_images/imageFile2131.png>)

![image 2132](<2005-musin-extension-delsarte-method-kissing_images/imageFile2132.png>)

![image 2133](<2005-musin-extension-delsarte-method-kissing_images/imageFile2133.png>)

![image 2134](<2005-musin-extension-delsarte-method-kissing_images/imageFile2134.png>)

![image 2135](<2005-musin-extension-delsarte-method-kissing_images/imageFile2135.png>)

![image 2136](<2005-musin-extension-delsarte-method-kissing_images/imageFile2136.png>)

![image 2137](<2005-musin-extension-delsarte-method-kissing_images/imageFile2137.png>)

![image 2138](<2005-musin-extension-delsarte-method-kissing_images/imageFile2138.png>)

![image 2139](<2005-musin-extension-delsarte-method-kissing_images/imageFile2139.png>)

![image 2140](<2005-musin-extension-delsarte-method-kissing_images/imageFile2140.png>)

![image 2141](<2005-musin-extension-delsarte-method-kissing_images/imageFile2141.png>)

![image 2142](<2005-musin-extension-delsarte-method-kissing_images/imageFile2142.png>)

![image 2143](<2005-musin-extension-delsarte-method-kissing_images/imageFile2143.png>)

![image 2144](<2005-musin-extension-delsarte-method-kissing_images/imageFile2144.png>)

![image 2145](<2005-musin-extension-delsarte-method-kissing_images/imageFile2145.png>)

![image 2146](<2005-musin-extension-delsarte-method-kissing_images/imageFile2146.png>)

![image 2147](<2005-musin-extension-delsarte-method-kissing_images/imageFile2147.png>)

![image 2148](<2005-musin-extension-delsarte-method-kissing_images/imageFile2148.png>)

![image 2149](<2005-musin-extension-delsarte-method-kissing_images/imageFile2149.png>)

![image 2150](<2005-musin-extension-delsarte-method-kissing_images/imageFile2150.png>)

![image 2151](<2005-musin-extension-delsarte-method-kissing_images/imageFile2151.png>)

![image 2152](<2005-musin-extension-delsarte-method-kissing_images/imageFile2152.png>)

![image 2153](<2005-musin-extension-delsarte-method-kissing_images/imageFile2153.png>)

![image 2154](<2005-musin-extension-delsarte-method-kissing_images/imageFile2154.png>)

![image 2155](<2005-musin-extension-delsarte-method-kissing_images/imageFile2155.png>)

![image 2156](<2005-musin-extension-delsarte-method-kissing_images/imageFile2156.png>)

![image 2157](<2005-musin-extension-delsarte-method-kissing_images/imageFile2157.png>)

![image 2158](<2005-musin-extension-delsarte-method-kissing_images/imageFile2158.png>)

![image 2159](<2005-musin-extension-delsarte-method-kissing_images/imageFile2159.png>)

![image 2160](<2005-musin-extension-delsarte-method-kissing_images/imageFile2160.png>)

![image 2161](<2005-musin-extension-delsarte-method-kissing_images/imageFile2161.png>)

![image 2162](<2005-musin-extension-delsarte-method-kissing_images/imageFile2162.png>)

![image 2163](<2005-musin-extension-delsarte-method-kissing_images/imageFile2163.png>)

![image 2164](<2005-musin-extension-delsarte-method-kissing_images/imageFile2164.png>)

![image 2165](<2005-musin-extension-delsarte-method-kissing_images/imageFile2165.png>)

![image 2166](<2005-musin-extension-delsarte-method-kissing_images/imageFile2166.png>)

![image 2167](<2005-musin-extension-delsarte-method-kissing_images/imageFile2167.png>)

![image 2168](<2005-musin-extension-delsarte-method-kissing_images/imageFile2168.png>)

![image 2169](<2005-musin-extension-delsarte-method-kissing_images/imageFile2169.png>)

![image 2170](<2005-musin-extension-delsarte-method-kissing_images/imageFile2170.png>)

![image 2171](<2005-musin-extension-delsarte-method-kissing_images/imageFile2171.png>)

![image 2172](<2005-musin-extension-delsarte-method-kissing_images/imageFile2172.png>)

![image 2173](<2005-musin-extension-delsarte-method-kissing_images/imageFile2173.png>)

![image 2174](<2005-musin-extension-delsarte-method-kissing_images/imageFile2174.png>)

![image 2175](<2005-musin-extension-delsarte-method-kissing_images/imageFile2175.png>)

![image 2176](<2005-musin-extension-delsarte-method-kissing_images/imageFile2176.png>)

![image 2177](<2005-musin-extension-delsarte-method-kissing_images/imageFile2177.png>)

![image 2178](<2005-musin-extension-delsarte-method-kissing_images/imageFile2178.png>)

![image 2179](<2005-musin-extension-delsarte-method-kissing_images/imageFile2179.png>)

![image 2180](<2005-musin-extension-delsarte-method-kissing_images/imageFile2180.png>)

![image 2181](<2005-musin-extension-delsarte-method-kissing_images/imageFile2181.png>)

![image 2182](<2005-musin-extension-delsarte-method-kissing_images/imageFile2182.png>)

![image 2183](<2005-musin-extension-delsarte-method-kissing_images/imageFile2183.png>)

![image 2184](<2005-musin-extension-delsarte-method-kissing_images/imageFile2184.png>)

![image 2185](<2005-musin-extension-delsarte-method-kissing_images/imageFile2185.png>)

![image 2186](<2005-musin-extension-delsarte-method-kissing_images/imageFile2186.png>)

![image 2187](<2005-musin-extension-delsarte-method-kissing_images/imageFile2187.png>)

![image 2188](<2005-musin-extension-delsarte-method-kissing_images/imageFile2188.png>)

![image 2189](<2005-musin-extension-delsarte-method-kissing_images/imageFile2189.png>)

![image 2190](<2005-musin-extension-delsarte-method-kissing_images/imageFile2190.png>)

![image 2191](<2005-musin-extension-delsarte-method-kissing_images/imageFile2191.png>)

![image 2192](<2005-musin-extension-delsarte-method-kissing_images/imageFile2192.png>)

![image 2193](<2005-musin-extension-delsarte-method-kissing_images/imageFile2193.png>)

![image 2194](<2005-musin-extension-delsarte-method-kissing_images/imageFile2194.png>)

![image 2195](<2005-musin-extension-delsarte-method-kissing_images/imageFile2195.png>)

![image 2196](<2005-musin-extension-delsarte-method-kissing_images/imageFile2196.png>)

![image 2197](<2005-musin-extension-delsarte-method-kissing_images/imageFile2197.png>)

![image 2198](<2005-musin-extension-delsarte-method-kissing_images/imageFile2198.png>)

![image 2199](<2005-musin-extension-delsarte-method-kissing_images/imageFile2199.png>)

![image 2200](<2005-musin-extension-delsarte-method-kissing_images/imageFile2200.png>)

![image 2201](<2005-musin-extension-delsarte-method-kissing_images/imageFile2201.png>)

![image 2202](<2005-musin-extension-delsarte-method-kissing_images/imageFile2202.png>)

![image 2203](<2005-musin-extension-delsarte-method-kissing_images/imageFile2203.png>)

![image 2204](<2005-musin-extension-delsarte-method-kissing_images/imageFile2204.png>)

![image 2205](<2005-musin-extension-delsarte-method-kissing_images/imageFile2205.png>)

![image 2206](<2005-musin-extension-delsarte-method-kissing_images/imageFile2206.png>)

![image 2207](<2005-musin-extension-delsarte-method-kissing_images/imageFile2207.png>)

![image 2208](<2005-musin-extension-delsarte-method-kissing_images/imageFile2208.png>)

![image 2209](<2005-musin-extension-delsarte-method-kissing_images/imageFile2209.png>)

![image 2210](<2005-musin-extension-delsarte-method-kissing_images/imageFile2210.png>)

![image 2211](<2005-musin-extension-delsarte-method-kissing_images/imageFile2211.png>)

![image 2212](<2005-musin-extension-delsarte-method-kissing_images/imageFile2212.png>)

![image 2213](<2005-musin-extension-delsarte-method-kissing_images/imageFile2213.png>)

![image 2214](<2005-musin-extension-delsarte-method-kissing_images/imageFile2214.png>)

![image 2215](<2005-musin-extension-delsarte-method-kissing_images/imageFile2215.png>)

![image 2216](<2005-musin-extension-delsarte-method-kissing_images/imageFile2216.png>)

![image 2217](<2005-musin-extension-delsarte-method-kissing_images/imageFile2217.png>)

![image 2218](<2005-musin-extension-delsarte-method-kissing_images/imageFile2218.png>)

![image 2219](<2005-musin-extension-delsarte-method-kissing_images/imageFile2219.png>)

![image 2220](<2005-musin-extension-delsarte-method-kissing_images/imageFile2220.png>)

![image 2221](<2005-musin-extension-delsarte-method-kissing_images/imageFile2221.png>)

![image 2222](<2005-musin-extension-delsarte-method-kissing_images/imageFile2222.png>)

![image 2223](<2005-musin-extension-delsarte-method-kissing_images/imageFile2223.png>)

![image 2224](<2005-musin-extension-delsarte-method-kissing_images/imageFile2224.png>)

![image 2225](<2005-musin-extension-delsarte-method-kissing_images/imageFile2225.png>)

![image 2226](<2005-musin-extension-delsarte-method-kissing_images/imageFile2226.png>)

![image 2227](<2005-musin-extension-delsarte-method-kissing_images/imageFile2227.png>)

![image 2228](<2005-musin-extension-delsarte-method-kissing_images/imageFile2228.png>)

![image 2229](<2005-musin-extension-delsarte-method-kissing_images/imageFile2229.png>)

![image 2230](<2005-musin-extension-delsarte-method-kissing_images/imageFile2230.png>)

![image 2231](<2005-musin-extension-delsarte-method-kissing_images/imageFile2231.png>)

![image 2232](<2005-musin-extension-delsarte-method-kissing_images/imageFile2232.png>)

![image 2233](<2005-musin-extension-delsarte-method-kissing_images/imageFile2233.png>)

![image 2234](<2005-musin-extension-delsarte-method-kissing_images/imageFile2234.png>)

−1

![image 2235](<2005-musin-extension-delsarte-method-kissing_images/imageFile2235.png>)

![image 2236](<2005-musin-extension-delsarte-method-kissing_images/imageFile2236.png>)

![image 2237](<2005-musin-extension-delsarte-method-kissing_images/imageFile2237.png>)

![image 2238](<2005-musin-extension-delsarte-method-kissing_images/imageFile2238.png>)

![image 2239](<2005-musin-extension-delsarte-method-kissing_images/imageFile2239.png>)

![image 2240](<2005-musin-extension-delsarte-method-kissing_images/imageFile2240.png>)

![image 2241](<2005-musin-extension-delsarte-method-kissing_images/imageFile2241.png>)

![image 2242](<2005-musin-extension-delsarte-method-kissing_images/imageFile2242.png>)

![image 2243](<2005-musin-extension-delsarte-method-kissing_images/imageFile2243.png>)

![image 2244](<2005-musin-extension-delsarte-method-kissing_images/imageFile2244.png>)

![image 2245](<2005-musin-extension-delsarte-method-kissing_images/imageFile2245.png>)

![image 2246](<2005-musin-extension-delsarte-method-kissing_images/imageFile2246.png>)

![image 2247](<2005-musin-extension-delsarte-method-kissing_images/imageFile2247.png>)

![image 2248](<2005-musin-extension-delsarte-method-kissing_images/imageFile2248.png>)

![image 2249](<2005-musin-extension-delsarte-method-kissing_images/imageFile2249.png>)

![image 2250](<2005-musin-extension-delsarte-method-kissing_images/imageFile2250.png>)

![image 2251](<2005-musin-extension-delsarte-method-kissing_images/imageFile2251.png>)

![image 2252](<2005-musin-extension-delsarte-method-kissing_images/imageFile2252.png>)

−1 −0.8 −0.6 −0.4 −0.2 0 0.2 0.4 0.6 0.8

Fig. 7. The graph of the function f(t)

We have t0 > 0.6058. Then Corollary 2 gives µ 6. Consider all m 6. h0 = f(1) = 18.774, h1 = f(1) + f(−1) = 24.48. h2 = f(1) + max

{(f(− cosθ) + f(− cos(60◦ − θ))} ≈ 24.8644, where θ0 = arccost0 ≈ 52.5588◦.

30◦ θ θ0

Note that h2 can be calculated by the same method as in Section 2. Here h2 = f(1) + 2f(− cos30◦) also.

In Sections 7, 8 have been shown that

h3 ≈ 24.8345, h4 ≈ 24.818, h5 < 24.8434, h6 < 24.934. Theorem 4. k(4) = 24 Proof. Let X be a spherical 1/2-code in S3 with M = k(4) points. The polynomial f is such that hmax < 25, then combining this and Theorem 2, we get k(4) hmax < 25. Recall that k(4) 24. Consequently, k(4) = 24.

![image 2253](<2005-musin-extension-delsarte-method-kissing_images/imageFile2253.png>)

![image 2254](<2005-musin-extension-delsarte-method-kissing_images/imageFile2254.png>)

![image 2255](<2005-musin-extension-delsarte-method-kissing_images/imageFile2255.png>)

![image 2256](<2005-musin-extension-delsarte-method-kissing_images/imageFile2256.png>)

### 10 Concluding remarks

The algorithm in Section 6 can be applied to other dimensions and spherical z-codes. If t0 = 1, then the algorithm gives the Delsarte method. E is an estimation of hmax in this algorithm.

Direct application of the method developed in this paper, presumably could lead to some improvements in the upper bounds on kissing numbers in dimensions 9, 10, 16, 17, 18 given in [10, Table 1.5]. (“Presumably” because the equality hmax = E is not proven yet.)

In 9 and 10 dimensions Table 1.5 gives: 306 k(9) 380, 500 k(10) 595. The algorithm gives:

- n = 9 : deg f = 11, E = h1 = 366.7822, t0 = 0.54;
- n = 10 : deg f = 11, E = h1 = 570.5240, t0 = 0.586. For these dimensions there is a good chance to prove that k(9) 366, k(10) 570.


From the equality k(3) = 12 follows ϕ3(13) < 60◦. The method gives ϕ3(13) < 59.4◦ (deg f = 11). The lower bound on ϕ3(13) is 57.1367◦ [17]. Therefore, we have 57.1367◦ ϕ3(13) < 59.4◦.

The method gives ϕ4(25) < 59.81◦, ϕ4(24) < 60.5◦. (This is theorem that can be proven by the same method as Theorem 4.) That improve the bounds:

ϕ4(25) < 60.79◦, ϕ4(24) < 61.65◦ [24] (cf. [5]); ϕ4(24) < 61.47◦ [5];

ϕ4(25) < 60.5◦, ϕ4(24) < 61.41◦ [4]. Now in these cases we have

57.4988◦ < ϕ4(25) < 59.81◦, 60◦ ϕ4(24) < 60.5◦.

For all cases that were considered (z 0.6) this method gives better bounds than Fejes T´th’s bounds for ϕ3(M) [17] and Coxeter’s bounds for all ϕn(M) [11]. However, for n = 5,6,7 direct use of this generalization of the Delsarte method does not give better upper bounds on k(n) than the Delsarte method. It is an interesting problem to ﬁnd better methods.

Acknowledgment. I wish to thank Eiichi Bannai, Ivan Dynnikov, Dmitry Leshchiner, Sergei Ovchinnikov, Makoto Tagami and G¨unter Ziegler for helpful discussions and useful comments on this paper.

### References

- [1] M. Aigner and G.M. Ziegler, Proofs from THE BOOK, Springer, 1998 (ﬁrst ed.) and 2002 (second ed.)
- [2] K. Anstreicher, The thirteen spheres: A new proof, Discrete and Computational Geometry, 31(2004), 613-625.
- [3] V.V. Arestov and A.G. Babenko, On Delsarte scheme of estimating the contact numbers, Trudy Mat. Inst. im. V.A.Steklova 219, 1997, 44-73; English translation, Proc. of the Steklov Inst. of Math. 219, 1997, 36-65.
- [4] V.V. Arestov and A.G. Babenko, On kissing number in four dimensions, in Proc. Conf. memory of Paul Erdo¨s, Budapest, Hingary, July 4-11, 1999, A.Sali, M.Simonovits and V.T.S´os (eds), J. Bolyai Math. Soc., Budapest, 1999, 10-14.


- [5] P.G. Boyvalenkov, D.P. Danev and S.P. Bumova, Upper bounds on the minimum distance of spherical codes, IEEE Trans. Inform. Theory, 42(5), 1996, 1576-1581.
- [6] K. B¨or¨czky, Packing of spheres in spaces of constant curvature, Acta Math. Acad. Sci. Hung. 32 (1978), 243-261.
- [7] K. B¨or¨czky, The Newton-Gregory problem revisited, Proc. Discrete Geometry, Marcel Dekker, 2003, 103-110.
- [8] B.C. Carlson, Special functions of applied mathematics, Academic Press, 1977.
- [9] B. Casselman, The diﬃculties of kissing in three dimensions, Notices Amer. Math. Soc., 51(2004), 884-885.
- [10] J.H. Conway and N.J.A. Sloane, Sphere Packings, Lattices, and Groups, New York, Springer-Verlag, 1999 (Third Edition).
- [11] H.S.M. Coxeter, An upper bound for the number of equal nonoverlapping spheres that can touch another of the same size, Proc. of Symp. in Pure Math. AMS, 7 (1963), 53-71 = Chap. 9 of H.S.M. Coxeter, Twelve Geometric Essays, Southern Illinois Press, Carbondale Il, 1968.
- [12] L. Danzer, Finite point-sets on S2 with minimum distance as large as possible, Discr. Math., 60 (1986), 3-66.
- [13] L. Danzer, B. Gr¨unbaum, and V. Klee. Helly’s theorem and its relatives. Proc. Sympos. Pure Math., vol. 7, AMS, Providence, RI, 1963, pp. 101-180.
- [14] Ph. Delsarte, Bounds for unrestricted codes by linear programming, Philips Res. Rep., 27, 1972, 272-289.
- [15] Ph. Delsarte, J.M. Goethals and J.J. Seidel, Spherical codes and designs, Geom. Dedic., 6, 1977, 363-388.
- [16] A. Erd´elyi, editor, Higher Transcendental Function, McGraw-Hill, NY, 3 vols, 1953, Vol. II, Chap. XI.
- [17] L. Fejes T´th, Lagerungen in der Ebene, auf der Kugel und in Raum, Springer-Verlag, 1953; Russian translation, Moscow, 1958.
- [18] T. Hales, The status of the Kepler conjecture, Mathematical Intelligencer 16(1994), 47-58.
- [19] R. Hoppe, Bemerkung der Redaction, Archiv Math. Physik (Grunet) 56

(1874), 307-312.

- [20] W.-Y. Hsiang, The geometry of spheres, in Diﬀerential Geometry (Shanghai,1991), Word Scientiﬁc, River Edge, NJ, 1993, pp. 92-107.


- [21] W.-Y. Hsiang, Least Action Principle of Crystal Formation of Dense Packing Type and Kepler’s Conjecture, World Scientiﬁc, 2001.
- [22] G.A. Kabatiansky and V.I. Levenshtein, Bounds for packings on a sphere and in space, Problemy Peredachi informacii 14(1), 1978, 3-25; English translation, Problems of Information Transmission, 14(1), 1978, 1-17.
- [23] J. Leech, The problem of the thirteen spheres, Math. Gazette 41 (1956), 22-23.
- [24] V.I. Levenshtein, On bounds for packing in n-dimensional Euclidean space, Sov. Math. Dokl. 20(2), 1979, 417-421.
- [25] O.R. Musin, The problem of the twenty-ﬁve spheres, Russian Math. Surveys, 58(2003), 794-795.
- [26] O.R. Musin, The kissing number in four dimensions, preprint, September 2003, math. MG/0309430.
- [27] A.M. Odlyzko and N.J.A. Sloane, New bounds on the number of unit spheres that can touch a unit sphere in n dimensions, J. of Combinatorial Theory A26(1979), 210-214.
- [28] F. Pfender and G.M. Ziegler, Kissing numbers, sphere packings, and some unexpected proofs, Notices Amer. Math. Soc., 51(2004), 873-883.
- [29] I.J. Schoenberg, Positive deﬁnite functions on spheres, Duke Math. J., 9

(1942), 96-107.

- [30] K. Sch¨utte and B.L. van der Waerden, Auf welcher Kugel haben 5,6,7,8 oder 9 Punkte mit Mindestabstand 1 Platz? Math. Ann. 123 (1951), 96124.
- [31] K. Sch¨utte and B.L. van der Waerden, Das Problem der dreizehn Kugeln, Math. Ann. 125 (1953), 325-334.
- [32] G.G. Szpiro, Kepler’s conjecture, Wiley, 2002.
- [33] G.G. Szpiro, Newton and the kissing problem, http://plus.maths.org/issue23/features/kissing/
- [34] A.D. Wyner, Capabilities of bounded discrepancy decoding, Bell Sys. Tech. J. 44 (1965), 1061-1122.


