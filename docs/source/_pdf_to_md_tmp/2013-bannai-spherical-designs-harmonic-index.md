arXiv:1308.5101v1[math.MG]23Aug2013

SPHERICAL DESIGNS OF HARMONIC INDEX t

EIICHI BANNAI, TAKAYUKI OKUDA, AND MAKOTO TAGAMI

Abstract. Spherical t-design is a ﬁnite subset on sphere such that, for any polynomial of degree at most t, the average value of the integral on sphere can be replaced by the average value at the ﬁnite subset. It is well-known that an equivalent condition of spherical design is given in terms of harmonic polynomials. In this paper, we deﬁne a spherical design of harmonic index t from the viewpoint of this equivalent condition, and we give its construction and a Fisher type lower bound on the cardinality. Also we investigate whether there is a spherical design of harmonic index attaining the bound.

1. Introduction

Let t be a natural number, Sn−1 the (n − 1)-dimensional unit sphere centered at the origin. A ﬁnite nonempty subset X on Sn−1 is called a spherical t-design if, for any polynomial f(x) = f(x1,...,xn) of degree at most t, the following equality holds:

1 |X| x∈X

1 |Sn−1| Sn−1

f(x)dσ(x) =

f(x),

![image 1](<2013-bannai-spherical-designs-harmonic-index_images/imageFile1.png>)

![image 2](<2013-bannai-spherical-designs-harmonic-index_images/imageFile2.png>)

where σ is an O(Rn)-invariant measure on Sn−1 and |Sn−1| denotes the surface volume of the sphere Sn−1. The concept of spherical design was deﬁned by DelsarteGoethals-Seidel (refer to [8, 7, 2, 3]). A spherical t-design means to be a good conﬁguration of points on sphere so that the average value of the integral of any polynomial of degree at most t on sphere can be replaced by the average value at the ﬁnite set on sphere.

2

2

∂x21 + ··· + ∂

Let △ = ∂

∂x2n be the Laplacian. A polynomial f(x) is harmonic if

![image 3](<2013-bannai-spherical-designs-harmonic-index_images/imageFile3.png>)

![image 4](<2013-bannai-spherical-designs-harmonic-index_images/imageFile4.png>)

△f(x) = 0. Then put Harmt(Rn) = {f(x) | f(x) is a harmonic and homogeneous polynomial of degree t on Rn}.

The dimension of Harmt(Rn) is n+tt−1 − n+t−t−23 (refer to [1, page 478 ]). Some equivalent conditions of spherical design are known. In particular, the following

condition is quite often used([7, 2, 3]):

For any f(x) ∈ Harmj(Rd) and 1 ≤ j ≤ t, x∈X f(x) = 0. From this condition, we introduce the following notion which is the main subject in this paper:

Deﬁnition 1.1 (Spherical design of harmonic index t). A ﬁnite nonempty subset X on Sn−1 is called a spherical design of harmonic index t (or simply, harmonic index t-design) if, for any f(x) ∈ Harmt(Rn), x∈X f(x) = 0.

We are interested in what ﬁgure appears as spherical designs of harmonic index, and whether we can give a natural lower bound for harmonic index designs similar to the case of usual spherical design.

1

When t is odd, any antipodal two points X = {x,−x} forms a harmonic index

t-design because x∈X f(x) = f(x) + f(−x) = f(x) − f(x) = 0 for any f(x) in Harmt(Rn). So, from now on, we consider only the case when t is even.

When t is even, for any f(x) ∈ Harmt(Rn), f(−x) = f(x). So we remark that one can take harmonic index t-designs just on hemisphere. For any n,t ∈ N, from Seymour-Zaslavsky’s theorem[16], if we make the number of vertices big enough, there always exists a harmonic index t-design on Sn−1. We denote the minimum cardinality of harmonic index t-design on Sn−1 by A(n,t). From the above, we see that, when t is odd, A(n,t) = 2.

First we consider the case when n = 2 and t = 2e. Let x,y be two unit vectors in R2 with angular θ = jπ/2e for odd j. Then X = {x,y} is a harmonic index

- 2e-design on S1. So we see that A(2,t) = 2.

Next we consider the case when t = 2 and n ≥ 2. Let X = {e1,...,en} be an orthonormal basis of Rn (that is, an antipodal half part of regular cross-polytope). Then it is easy to see that X is a harmonic index 2-design on Sn−1. Therefore A(n,2) ≤ n. In fact, we will show A(n,2) = n later. 1

Let Ctλ(x) be the Gegenbauer poynomial of degree t, that is, when λ = 0, (1 − 2xr + r2)−λ =

∞

t=0

Ctλ(x)rt,

and when λ = 0, it is the Chebychev polynomial of ﬁrst kind, that is, Ct0(x) = Tt(x) = cos(tarccos(x)). {Ctλ(x)} is a set of orthogonal polynomials on an interval [−1,1] with a weight function (1 − x2)λ−1/2 and so they have all roots on [−1,1] (refer to [1, 10]). For simplicity, we normalize Ctλ(x) as Qn,t(x) = Qt(x) = An,tC

n−2 2

![image 5](<2013-bannai-spherical-designs-harmonic-index_images/imageFile5.png>)

t (x), where a normalization factor An,t is given so as to be Qt(1) = n+tt−1 − n+t−t−23 . For x,y ∈ Rn, x,y denotes the standard inner product. Then (for covenience, using the same symbol Qn,t), Qn,t(x,y) = Qn,t( x,y ) becomes the reproducing kernel on the Hilbert space Harmt(Sn−1) which consists of all functions of Harmt(Rn) restricted on Sn−1 (refer to [11]). Also for a ﬁnite subset X on sphere, we set I(X) = { x,y | x, = y ∈ X}.

The following is the main theorem I in this paper, which gives a simple construction of harmonic index designs by using usual spherical designs in lower dimension by 1.

- Theorem 1. Let X be a spherical t-design on Sn−2, r a root of Qn,t(s). Set X′ ⊂ Sn−1 to be :


X′ = r, 1 − r2x ∈ Sn−1 | x ∈ X . Then X′ is a harmonic index t-design.

![image 6](<2013-bannai-spherical-designs-harmonic-index_images/imageFile6.png>)

The proof will be given in Section 2. By Bondarenko–Radchenko–Viazovska’s result in [5, 6], for a ﬁxed n, there exists a spherical t-design on Sn−1 of size O(tn−1). Hence Theorem 1 gives A(n,t) ≤ O(tn−2) as a function of t (see Corollary 2.1 in Section 2 for more details).

![image 7](<2013-bannai-spherical-designs-harmonic-index_images/imageFile7.png>)

1We note that this is also proved as follows. If X is a harmonic index 2-design in Sn−1, then X ∪(−X) is a spherical 3-design (possibly with multiplicities). The classiﬁcation of tight spherical

- 3-desigs(possibly with multiplicities) implies the claim.


Since the regular (2e + 1)-gon is a spherical (2e)-design on S1, by Theorem 1, taking the radius suitably and putting it on S2, we obtain a harmonic index (2e)design on S2. To construct a harmonic index 4-design by Theorem 1, we must take a regular 5-gon. By computer calculation, we will show that there does not exist a harmonic index 4-design of 4 vertices on S2 and so A(3,4) = 5. Moreover we will show that the conﬁguration of points giving A(3,4) = 5 is essentially unique, that is, they are given by the conﬁguration obtained from a regular 5-gon using Theorem 1 (for these proofs, refer to Section 3). Similarly, from a regular 7-gon, we have A(3,6) ≤ 7. Also up to the present, we have not detected a harmonic index 6-design with at most 6 vertices. From these facts, at ﬁrst, we conjectured that a minimum size harmonic index (2e + 1)-design on S2 is always given by a regular (2e + 1)-gon and it is unique. But in fact, we realized from the following examples that, even if t is big, there exists a harmonic index t-design with rather small number of vertices. For examples, take 6 vertices of an antipodal half part from 12 vertices of a regular icosahedron, then they form a harmonic index 8-design and moreover it is also a harmonic index 14-design. This fact follows from the harmonic Molien series of the icosahedral group. This number of vertices, 6 is far smaller than the number of vertices for hamonic index 14-design, 15, which is obtained from the regular 15-gon on S1 by Theorem 1. A similar phenomenon can be seen in the following example, too. For example, in the case when n = 8, the root system of type E8, 240 points (and its antipodal half part, 120 points) is a harmonic index 10-design. While, the Fisher type inequality for usual spherical 10-designs on S6 ⊂ R7 gives a lower bound 115 + 104 = 672, and it is far bigger than 120. Also in the case when n = 4, 120 points of the 600-cell (and its antipodal half part, 60 pointsjis a harmonic index 58-design. While, the Fisher type inequality for usual spherical 58-designs on S2 ⊂ R3 gives a lower bound 3129 + 3028 = 900, and it is far bigger than 60.

For spherical designs, there is the lower bound which is called the Fisher type inequality (refer to [8]). The following is the main theorem II in this paper, which gives a Fisher type inequality for harmonic index designs.

- Theorem 2. Let X be a harmonic index t-design on Sn−1. Put


Qn,t(x). Then the following inequality holds:

cn,t = − min

−1≤x≤1

n + t − 1 t −

n + t − 3 t − 2

1 cn,t

. Moreover, equality holds in (1) if and only if for any a ∈ I(X), cn,t = −Qn,t(a).

- (1) |X| ≥ 1 +


![image 8](<2013-bannai-spherical-designs-harmonic-index_images/imageFile8.png>)

We note that, since Qn,t(x) is an orthogonal polynomial on [−1,1], cn,t is always positive. The proof of Theorem 2 will be given in Section 2. Denote the lower bound of (1) by bn,tF

1 cn,t

n + t − 1 t −

n + t − 3 t − 2

bn,t := 1 +

.

![image 9](<2013-bannai-spherical-designs-harmonic-index_images/imageFile9.png>)

We are interested in the case when bn,t is an integer. In this case, if there exists a harmonic index t-design X on Sn−1 whose cardinality is exaclty bn,t, then we say that X is a tight harmonic index t-design. For example, in the case when t = 2, bn,2 = n, and, as we stated above, an antipodal half part of a regular cross-polytope

is a harmonic index 2-design with the cardinality |X| = n, and therefore it is a tight harmonic index 2-design. In particular, we have A(n,2) = n.

A tight harmonic index design forms equiangular lines (refer to Corollary 4.1 and for equiangular lines, refer to Brouwer-Haemers[4, page 161]). Also ﬁx n and make t big limitlessly, then bn,t converges some value, and, in general, the convergence value becomes bigger than the absolute bound n(n + 1)/2 on equiangular lines on Rn. Therefore we see that there hardly exists a tight harmonic index design for general n,t. On non-existence of tight harmonic index design, refer to Section 4.

The contents of this paper is as follows. In Section 2, we will give the proof of the main theorems I and II. In Section 3, we will state some calculation results on harmonic index designs, in particular, we will state on a unique conﬁguration of points giving A(3,4) = 5. In Section 4, we will give a necessary condition for parameters such that a tight harmonic index design exists, and we will show that tight harmonic index designs hardly exist. Also in Appendix I, we give a table on bn,t of Theorem 2 for 3 ≤ n ≤ 10 and 4 ≤ t ≤ 20. In Appendix II, we will give a Groebner basis used to show the uniqueness of points conﬁguration giving A(3,4) = 5.

2. Proof of Main Theorems I,II Proof of Theorem 1 We use the construction of an orthogonal basis in Harmt(Sn−1)

which is given in Andrews-Askey-Roy [1, page 461]. But here, for convenience, we use Qn,t(x) instead of Ctλ(x) in [1]. Let dn,t := dimHarmt(Sn−1), and for 0 ≤ j ≤ t, {Sj,l(ξn−1) : 1 ≤ l ≤ dn−1,j} be an orthogonal basis of Harmj(Sn−2) where ξn−1 ∈ Sn−2. Then if we take a variable ξ ∈ Sn−1 as ξ = x/|x| = s,√1 − s2ξn−1

![image 10](<2013-bannai-spherical-designs-harmonic-index_images/imageFile10.png>)

j

Sj,l(ξn−1)(1 − s2)

2Q2j+n,t−j(s) : 0 ≤ j ≤ t,1 ≤ l ≤ dj,n−1

![image 11](<2013-bannai-spherical-designs-harmonic-index_images/imageFile11.png>)

becomes an orthogonal basis of Harmt(Sn−1). It is clear that the sum over X for functions in the above basis of Harmt(Sn−1) except for j = 0 is 0 since X is a spherical t-design on Sn−2. Also in the case when j = 0, the function of the above basis is Qn,t(s). Therefore, if we take a root of Qn,t(s) as r, then all functions of the above basis satisﬁes that the sum over X′ is 0, and the theorem follows. ✷

Lemma 2.1. X ⊂ Sn−1 is a harmonic index t-design if and only if

Qn,t( x,y ) = 0.

x,y∈X

Proof. Let {fi(x) | 1 ≤ i ≤ dn,t} is an orthonormal basis of a Hilbert space Harmt(Sn−1). Then since Qn,t(x,y) is the reproducing kernel of Harmt(Sn−1), we have the following addition formula:

Hence,

Qn,t(x,y) = Qn,t( x,y ) =

dn,t

fi(x)fi(y).

i=1

Qn,t( x,y ) =

x,y∈X

x,y∈X

dn,t

dn,t

dn,t

fi(x)

fi(x)fi(y) =

fi(x)fi(y) =

i=1 x∈X

i=1 x,y∈X

i=1

2

.

From this equation, this lemma follows.

By combining Theorem 1 with results in [5, 6] (see Remark 1 below for more details), we obtain the following corollary:

Corollary 2.1. There exists a constant Cn−2 depending only on n such that for each N > Cn−2tn−2, there exists a spherical design of harmonic index t on Sn−1 of size N.

Remark 1. Let us ﬁx n and t. In [5], Bondarenko–Radchenko–Viazovska proved that for each N ≥ Cn−1tn−1, there exists a sequence x1,...,xN ∈ Sn−1 such that

N

1 |Sn−1| Sn−1

1 N

f(xi) =

- (2) f(x)dσ(x)

for any polynomial f(x) of degree at most t, where Cn−1 is a constant depending only on n. It should be remarked that a sequence x1,...,xN ∈ Sn−1 with the property (2) is called a “spherical t-design” in their paper. However, in our definition of spherical designs, a sequence x1,...,xN is required to be distinct each other. In [6], Bondarenko–Radchenko–Viazovska improved their result as follows: there exist positive constants Cn′ −1 and λn−1 depending only on n such that for each N > Cn′ −1tn−1, we can ﬁnd a “spherical t-design” x1,...,xN ∈ Sn−1 in their sense with

|xi − xj| > λn−1N−1/(n−1) for any distinct i,j. Especially, x1,...,xN ∈ Sn−1 gives a spherical t-design of size N even in our sense.

Proof of Theorem 2 Let F(s) := cn,t + Qn,t(s). Then from the deﬁnition of cn,t,

F(s) is a non-negative function on [−1,1]. We evaluate x,y∈X F( x,y ) in two ways.

Since X is a harmonic index t-design, by Lemma 2.1, x,y∈X Qn,t( x,y ) = 0. Therefore,

- (3) x,y∈X

F( x,y ) =

x,y∈X

(cn,t + Qn,t( x,y )) = cn,t|X|2.

Next, since F(s) is non-negative on [−1,1] and Qn,t(1) = dimHarmt(Rn) = n+tt−1 −

n+t−3

t−2 ,

- (4)


![image 12](<2013-bannai-spherical-designs-harmonic-index_images/imageFile12.png>)

![image 13](<2013-bannai-spherical-designs-harmonic-index_images/imageFile13.png>)

i=1

n + t − 1 t −

n + t − 3 t − 2

F( x,y ) ≥

F( x,x ) = |X|F(1) = |X| cn,t +

x,y∈X

x∈X

By (3) and (4), we have the following inequality:

n + t − 1 t −

n + t − 3 t − 2 Therefore,

cn,t|X|2 ≥ |X| cn,t +

n + t − 1 t −

n + t − 3 t − 2

1 cn,t

.

|X| ≥ 1 +

![image 14](<2013-bannai-spherical-designs-harmonic-index_images/imageFile14.png>)

Moreover, equality in this inequality holds if and only if equality holds in (4), that is, for any x, = y ∈ X, cn,t + Qn,t( x,y ) = 0. Therefore the ﬁnal assertion of the theorem follows. ✷

.

3. Some calculation results First we apply Theorem 2 to the case when n = 2. Since Q2,t(x) = 2 cos(tarccos(x)), c2,t = − min

2 cos(tarccos(x)) = 2. Therefore, we have

−1≤x≤1

t + 1 t −

- t − 1
- t − 2


1 c2,t

= 2,

b2,t = 1 +

![image 15](<2013-bannai-spherical-designs-harmonic-index_images/imageFile15.png>)

and so A(2,t) ≥ 2. Let x,y be two unit vectors with angular θ = jπ/2e where j is odd. Then X = {x,y} is a harmonic index (2e)-design on S1 and we have

- A(2,t) = 2. Conversely let X = {x,y} ⊂ S1 be a harmonic index t-design with two vertices. From the ﬁnal assertion of Theorem 2, cost x,y = −1 must hold. Hence we see that X must be obtained by the above construction.


n + 2 2

(nx2 − 1),

Next we consider the case when t = 2. Then since Qn,2(x) =

![image 16](<2013-bannai-spherical-designs-harmonic-index_images/imageFile16.png>)

n + 2 2

. This value is given at x = 0. Therefore, we have bn,2 = 1 +

c2,t = − min

Qn,2(x) =

![image 17](<2013-bannai-spherical-designs-harmonic-index_images/imageFile17.png>)

−1≤x≤1

1 cn,2

n + 1 2 −

n − 1 0

= n,

![image 18](<2013-bannai-spherical-designs-harmonic-index_images/imageFile18.png>)

and An,2 ≥ n. Let X = {ei | 1 ≤ i ≤ n} be an orthonomal basis of Rn. Then X is a harmonic index 2-design on Sn−1 and so we have A(n,2) = n. Conversely let X be a harmonic index 2-design on Sn−1 with n vertices. Then From the ﬁnal assertion of Theorem 2, we see that, for any x = y ∈ X, x,y = 0. So X must be an orthonormal basis of Rn.

The ﬁrst non-trivial case is the case when n = 3 and t = 4.

- Theorem 3. A(3,4) = 5. Moreover a harmonic index 4-design with 5 vertices on


S2 is congruent to the following X0± or any one of the conﬁgurations obtained by replacing some points in X0± to its antipodal points:

X0± =

√

√

![image 19](<2013-bannai-spherical-designs-harmonic-index_images/imageFile19.png>)

![image 20](<2013-bannai-spherical-designs-harmonic-index_images/imageFile20.png>)

1 35

1 35

![image 21](<2013-bannai-spherical-designs-harmonic-index_images/imageFile21.png>)

![image 22](<2013-bannai-spherical-designs-harmonic-index_images/imageFile22.png>)

30,0 , 1 35

525 ± 70

30,

700 ∓ 70

![image 23](<2013-bannai-spherical-designs-harmonic-index_images/imageFile23.png>)

![image 24](<2013-bannai-spherical-designs-harmonic-index_images/imageFile24.png>)

10 + 2√5 140

√5 − 1 140

![image 25](<2013-bannai-spherical-designs-harmonic-index_images/imageFile25.png>)

√

√

√

![image 26](<2013-bannai-spherical-designs-harmonic-index_images/imageFile26.png>)

![image 27](<2013-bannai-spherical-designs-harmonic-index_images/imageFile27.png>)

![image 28](<2013-bannai-spherical-designs-harmonic-index_images/imageFile28.png>)

![image 29](<2013-bannai-spherical-designs-harmonic-index_images/imageFile29.png>)

![image 30](<2013-bannai-spherical-designs-harmonic-index_images/imageFile30.png>)

![image 31](<2013-bannai-spherical-designs-harmonic-index_images/imageFile31.png>)

![image 32](<2013-bannai-spherical-designs-harmonic-index_images/imageFile32.png>)

![image 33](<2013-bannai-spherical-designs-harmonic-index_images/imageFile33.png>)

525 ± 70

30,

700 ∓ 70

30,

700 ∓ 70

30 ,

![image 34](<2013-bannai-spherical-designs-harmonic-index_images/imageFile34.png>)

![image 35](<2013-bannai-spherical-designs-harmonic-index_images/imageFile35.png>)

![image 36](<2013-bannai-spherical-designs-harmonic-index_images/imageFile36.png>)

10 − 2√5 140

√5 + 1 140

![image 37](<2013-bannai-spherical-designs-harmonic-index_images/imageFile37.png>)

√

√

√

![image 38](<2013-bannai-spherical-designs-harmonic-index_images/imageFile38.png>)

![image 39](<2013-bannai-spherical-designs-harmonic-index_images/imageFile39.png>)

![image 40](<2013-bannai-spherical-designs-harmonic-index_images/imageFile40.png>)

![image 41](<2013-bannai-spherical-designs-harmonic-index_images/imageFile41.png>)

![image 42](<2013-bannai-spherical-designs-harmonic-index_images/imageFile42.png>)

1 35

![image 43](<2013-bannai-spherical-designs-harmonic-index_images/imageFile43.png>)

![image 44](<2013-bannai-spherical-designs-harmonic-index_images/imageFile44.png>)

![image 45](<2013-bannai-spherical-designs-harmonic-index_images/imageFile45.png>)

30 ,

525 ± 70

30,−

700 ∓ 70

30,

700 ∓ 70

![image 46](<2013-bannai-spherical-designs-harmonic-index_images/imageFile46.png>)

![image 47](<2013-bannai-spherical-designs-harmonic-index_images/imageFile47.png>)

![image 48](<2013-bannai-spherical-designs-harmonic-index_images/imageFile48.png>)

10 − 2√5 140

√5 + 1 140

![image 49](<2013-bannai-spherical-designs-harmonic-index_images/imageFile49.png>)

√

√

√

![image 50](<2013-bannai-spherical-designs-harmonic-index_images/imageFile50.png>)

![image 51](<2013-bannai-spherical-designs-harmonic-index_images/imageFile51.png>)

![image 52](<2013-bannai-spherical-designs-harmonic-index_images/imageFile52.png>)

![image 53](<2013-bannai-spherical-designs-harmonic-index_images/imageFile53.png>)

![image 54](<2013-bannai-spherical-designs-harmonic-index_images/imageFile54.png>)

1 35

![image 55](<2013-bannai-spherical-designs-harmonic-index_images/imageFile55.png>)

![image 56](<2013-bannai-spherical-designs-harmonic-index_images/imageFile56.png>)

![image 57](<2013-bannai-spherical-designs-harmonic-index_images/imageFile57.png>)

525 ± 70

30,−

700 ∓ 70

30,−

700 ∓ 70

30 ,

![image 58](<2013-bannai-spherical-designs-harmonic-index_images/imageFile58.png>)

![image 59](<2013-bannai-spherical-designs-harmonic-index_images/imageFile59.png>)

![image 60](<2013-bannai-spherical-designs-harmonic-index_images/imageFile60.png>)

√5 − 1 140

10 + 2√5 140

![image 61](<2013-bannai-spherical-designs-harmonic-index_images/imageFile61.png>)

√

√

√

![image 62](<2013-bannai-spherical-designs-harmonic-index_images/imageFile62.png>)

![image 63](<2013-bannai-spherical-designs-harmonic-index_images/imageFile63.png>)

![image 64](<2013-bannai-spherical-designs-harmonic-index_images/imageFile64.png>)

![image 65](<2013-bannai-spherical-designs-harmonic-index_images/imageFile65.png>)

![image 66](<2013-bannai-spherical-designs-harmonic-index_images/imageFile66.png>)

1 35

![image 67](<2013-bannai-spherical-designs-harmonic-index_images/imageFile67.png>)

![image 68](<2013-bannai-spherical-designs-harmonic-index_images/imageFile68.png>)

![image 69](<2013-bannai-spherical-designs-harmonic-index_images/imageFile69.png>)

30 ,

525 ± 70

30,

700 ∓ 70

30,−

700 ∓ 70

![image 70](<2013-bannai-spherical-designs-harmonic-index_images/imageFile70.png>)

![image 71](<2013-bannai-spherical-designs-harmonic-index_images/imageFile71.png>)

![image 72](<2013-bannai-spherical-designs-harmonic-index_images/imageFile72.png>)

Here double-sign is corresponding.

Proof. First we apply Theorem 2. Since

Q3,4(x) =

9 8

9 8

(35x4 − 30x2 + 3) =

![image 73](<2013-bannai-spherical-designs-harmonic-index_images/imageFile73.png>)

![image 74](<2013-bannai-spherical-designs-harmonic-index_images/imageFile74.png>)

3 7

35 x2 −

![image 75](<2013-bannai-spherical-designs-harmonic-index_images/imageFile75.png>)

2

24 7

−

![image 76](<2013-bannai-spherical-designs-harmonic-index_images/imageFile76.png>)

,

c3,4 = 27/7. So b3,4 = 10/3 = 3.333 ... and we have A(3,4) ≥ 4. Next in order to give an upper bound of A(3,4), we apply Theorem 1. A regular 5-gon is a spherical

- 4-design on S1 (cf. [2, 12]). Hence by Theorem 1, adjusting the radius of a regular
- 5-gon suitably and putting it on S2, we obtain a harmonic index 4-design with 5 vertices on S2. These two conﬁgurations obtained in this way by using two positive roots of Q3,4(s) are X0+ and X0− in the assertion of the theorem. Thus we have


- A(3,4) ≤ 5. A problem is whether there exists a harmonic index 4-design with 4 vertices on S2. We can solve this problem by the direct calculation as follows.


Take the following basis of Harm4(R3).

H = {x3y − xy3,x3z − 3xy2z,3x2yz − y3z,x4 − 6x2y2 + y4,4xz3 − 3x3z − xy2z, 4yz3 − 3x2yz − 3y3z,6xyz2 − x3y − xy3,6x2z2 − x4 − 6y2z2 + y4, 8z4 − 24x2z2 − 24y2z2 + 3x4 + 6x2y2 + 3y4}.

Let X be a four point subset on S2. Since the property as harmonic index design is invariant under orthogonal transformations, by Lemma 2.1, without loss of generality, we may put the points of X as follows:

X = {x1 = (1,0,0),x2 = (s21,s22,0),x3 = (s31,s32,s33),x4 = (s41,s42,s43)}. Here s21,s22,...,s43 are variables and satisfy xi,xi = 1 for i = 1,...,4. Let

EQ1 = { xi,xi − 1 | i = 1,...,4}, EQ2 =

f(x) | f ∈ H .

x∈X

By Deﬁniton 1.1, X is a harmonic index 4-design if and only if, for any f ∈ H,

x∈X f(x) = 0. Thus, the common zeros of EQ := EQ1 ∪ EQ2 give exactly harmonic index 4-designs. We calculated the ideal which is generated by EQ in a multivariate polynomial ring R[s21,s22,...,s43] by Groebner bases function in a computational algebra system, Magma, and we found that the ideal equals to the whole of the ring. It means that there is no common zero of EQ and therefore, that there does not exist a harmonic index 4-design with 4 vertices on S2.

Next we show the uniqueness of conﬁgurations giving A(3,4) = 5. Suppose t is even. Here we note that, for a harmonic index t-design, even if we replace some points of them to its antipodal points, it also becomes a hamonic index t-design.

In order to prove the uniqueness, ﬁrst we count the number of the conﬁgurations given in the assertion of the theorem. As a promise to count them, we put X = {x1,x2,...,x5}, and two points in its ﬁve points are put as x1 = (1,0,0),x2 = (a,b,0), and we count the number of values a,b and the coordinates of x3,x4,x5 such that X is congruent to any one of the conﬁgurations given in the assertion

√

![image 77](<2013-bannai-spherical-designs-harmonic-index_images/imageFile77.png>)

1 35

![image 78](<2013-bannai-spherical-designs-harmonic-index_images/imageFile78.png>)

of the theorem. The positive roots of Q3,4(s) are r1 =

30 and r2 =

525 + 70

![image 79](<2013-bannai-spherical-designs-harmonic-index_images/imageFile79.png>)

√

![image 80](<2013-bannai-spherical-designs-harmonic-index_images/imageFile80.png>)

1 35

![image 81](<2013-bannai-spherical-designs-harmonic-index_images/imageFile81.png>)

30. X0± in the theorem are exactly ones obtained by Theorem 1 with r1 and r2, respectively, and they are cited as the small 5-gon and the big 5gon on S2, respectively. First, on X0± and the conﬁgurations obtained by replacing some points in X0± to its antipodal points (which are said to be the derived ones

525 − 70

![image 82](<2013-bannai-spherical-designs-harmonic-index_images/imageFile82.png>)

by this operation), we can conﬁrm by numerical calculation that exactly 8 values appear among I(X)’s for the conﬁgurations X’s which are given in the assertion of the theorem. The 8 values of inner products are given by the following pairs of two points: two vertices neighboring on the small 5-gon, two vertices on the diagonals of the small 5-gon, a vertex of the small 5-gon and the antipodal points of the neighbor vetices on the 5-gon, a vertex of the small 5-gon and the antipodal points of the diagonal vertices on the 5-gon, and 4 kinds of the corresponding ones for the big 5-gon. The number of them is 8 in all. In particular, inner products appearing in these pairs of two points are all diﬀerent. This fact means that, once we determine a distance between a pair of two points, it is determined which conﬁguration the whole ﬁve points are on , the small 5-gon and the derived one, or the big 5-gon and the derived one.

First ﬁx x1 = (1,0,0). For each of the above 8 distances, there are two choices to put x2 by the distance from x1 to a clockwise direction or a counterclockwise direction on the equator. Hence there are 16 choices as a position of x2 overall. From the above fact, by the distance x1x2, it is determined which conﬁguration the whole ﬁve points are on, the small 5-gon and the derived one, or the big 5-gon and the derived one. Hence after determining the distance x1x2, there are 6 positions to put x3 among the remaining vertices of 5-gons and the derived one, and the positions all have diﬀerent combinations of distances from x1 and x2. For each combination of distances, we need to choose which x3 is on, the north hemisphere or the south hemisphere, so we have two choices. Finally, we have 12 choices as positions of x3. Similarly, after determining the coordinates of x1,x2 and x3, we see that there are 4 combinations of distances x1x4,x2x4,x3x4. Since a coordinate of a point in R3 is determined by distances from linearly independent three points,

- a coordinate of x4 is determined by a combination of distances. Similarly, after determining the coordinates of x1,...,x4, there are 2 positions to put x5. After all, we see that there are 16 × 12 × 4 × 2 = 1536 combinations for coordinates of


x2,...,x5 overall.

Next, we carry out a Groebner basis calculation for the case of ﬁve points in a similar way to the case of four points. Let H be the same as the above and X = {x1 = (1,0,0),x2 = (s1,s2,s3),x3 = (s4,s5,s6),x4 = (s7,s8,s9),x5 = (s10,s11,s12)}, where s3 = 0. Also let

EQ′1 = { xi,xi − 1 | i = 1,...,5}, EQ′2 =

f(x) | f ∈ H .

x∈X

Similar to the case of four points, the common zeros of EQ′ := EQ′1 ∪ EQ′2 give exactly harmonic index 4-designs. For the ideal generated by EQ′ in a multivariate

polynomial ring R[s1,s2,s4 ...,s12], we calculate a Groebner basis of a lexicographical order using Magma. the calculation result is given in Appendix 2.

First we factorize P16 as follows: P16 =

1 866761

(931s812−1302s612+627s412−126s212+9)(931s812−1428s612+732s412−144s212+9). Put

![image 83](<2013-bannai-spherical-designs-harmonic-index_images/imageFile83.png>)

- f1 = 931s812 − 1302s612 + 627s412 − 126s212 + 9,
- f2 = 931s812 − 1428s612 + 732s412 − 144s212 + 9.


We checked by Sturm’s theorem that f1 and f2 have the eight real zeros. First for eight zeros of f1 in s12, we investigate possible values for s1,...,s11. Since P15 is divided by f1, we do not need to consider P15 for zeros of f1. For each value of s12, the value of s11 is determined by a polynomial P14 in s11, and there are at most

- 4 possible values. Similarly, for each possibility of s12 and s11, s10 has at most 2 possibilities by P13. We are to determine the number of possibilities for s1,...,s11 in this way. P12 is divided by f1. s9 has at most 4 possibilities by P11. s8 has at most a possibility by P10, s7 has at most a possibility by P6, s6 has at most 2 possibilities by P5, s5 has at most a possibility by P4, s4 has at most a possibility by P3, s2 has at most 2 possibilities by P2. s1 has at most a possibility by P1. Finally, from the zeros of f1, the total number of possibilities for s1,...,s11 is 8 × 42 × 23. Similarly we count the number of possibilities in the case of 8 zeros of f2. Since P15 is not divided by f2, for each zero of f2, s11 has at most 2 possibilities by P15. s10 has at most 2 possibilities by P13, s9 has at most 2 possibilities by P12. Since P8, P9, P10 and P11 are in the ideal generated by P12, P13, P14, P15 and P16, s8 has at most 2 possibilities by P7. s7 has at most a possibility by P6, s6 has at most 2 possibilities by P5, s5 has at most a possibility by P4, s4 has at most a possibility by P3, s2 has at most 2 possibilities by P2. s1 has at most a possibility by P1. Finally, for the zeros of f2, the total number of possibilities is 8×26. In conclusion, the number of the common zeros of EQ′ is at most 23 × 42 × +8 × 26 = 29 × 3, which is equal to the number of examples given in the assertion of the theorem. This completes the proof of the theorem.


From the Groebner basis calculation, which is used in the proof of Theorem 3, and the existence of an antipodal half of vertices of icosahedron, we see 5 ≤ A(3,8) ≤ 6. Other exact values of A(n,t) are all open.

4. On existence of tight harmonic index design

In this section, we investigate the conditions for the existence of tight harmonic index designs. First we show the following:

- Corollary 4.1. Suppose that bn,t is a natural number and X is a harmonic index t-design on Sn−1 with |X| = bn,t. Then there exists some α ∈ [−1,1] such that I(X) = {±α}.


Proof. By the ﬁnal assertion of Theorem 2, for any α ∈ I(X), Qn,t(α) must attain the minimum of Qn,t(x) on [−1,1]. But it is known that local minima of Gegenbauer polynomials change monotonously from the origin (cf. Szego¨ [17, 168 page]). Hence the minimum point α is unique. Therefore the assertion of the corollary is concluded.

Let Jα(z) is the Bessel function of the ﬁst kind for parameter α. Refer to [1, 17] on Bessel funtion. jα,k denotes the k-th positive root of Jα(z).

− n−2 3

z 2

![image 84](<2013-bannai-spherical-designs-harmonic-index_images/imageFile84.png>)

(z). Then ﬁx n and make t tend to inﬁnity, then

Jn−3

- Proposition 4.1. Let Fn(z) =


![image 85](<2013-bannai-spherical-designs-harmonic-index_images/imageFile85.png>)

![image 86](<2013-bannai-spherical-designs-harmonic-index_images/imageFile86.png>)

2

- 1

![image 87](<2013-bannai-spherical-designs-harmonic-index_images/imageFile87.png>)

Fn jn−1

![image 88](<2013-bannai-spherical-designs-harmonic-index_images/imageFile88.png>)

- 2 ,1


bn,t → 1 −

.

n − 3 2

and Pn,t(s) = Bn,tQn,t(s). Here the normalization factor

Proof. Let α =

![image 89](<2013-bannai-spherical-designs-harmonic-index_images/imageFile89.png>)

Bn,t is taken so as to be Pn,t(1) = t+tα . Then under the notation in Szego¨[17], Pn,t(s) = Pt(α,α). Also denote by c′n,t the minimum of Pn,t(s) on [−1,1] times -1. Then

n + t − 1 t −

n + t − 1 t −

1 cn,t

Bn,t Bn,tcn,t

1 c′n,t

n + t − 3 t − 2

n + t − 3 t − 2

=

=

![image 90](<2013-bannai-spherical-designs-harmonic-index_images/imageFile90.png>)

![image 91](<2013-bannai-spherical-designs-harmonic-index_images/imageFile91.png>)

![image 92](<2013-bannai-spherical-designs-harmonic-index_images/imageFile92.png>)

tα c′n,t

t + α t ∼ tα, lim

Since Pn,t(1) =

bn,t = lim

1 −

. By [17, page 63], d ds

![image 93](<2013-bannai-spherical-designs-harmonic-index_images/imageFile93.png>)

t→∞

t→∞

- 1

![image 94](<2013-bannai-spherical-designs-harmonic-index_images/imageFile94.png>)

- 2


Pn,t(s) =

(t + n − 2)Pn+2,t−1(s).

![image 95](<2013-bannai-spherical-designs-harmonic-index_images/imageFile95.png>)

Since local minima of Pn,t(s) change monotonously from the origin, the minimum is attained at the maximum root of Pn+2,t−1(s). Let −1 < x(n,tt) < x(n,t)2 < ··· < x(n,t)1 < 1 be the roots of Pn,t(s), and set x(n,it) = cosθn,i(t) 0 < θn,i(t) < π . So the minimum of Pn,t(s) is c′n,t = Pn,t xn(t+2−1),1 = Pn,t cosθn(t+2−1),1 . The following convergence is well-known ([17, 192 page]):

t + α t

Pn,t(1) c′n,t

=

.

![image 96](<2013-bannai-spherical-designs-harmonic-index_images/imageFile96.png>)

- (5) lim

t→∞

t−αPn,t cos

z t

![image 97](<2013-bannai-spherical-designs-harmonic-index_images/imageFile97.png>)

=

z 2

![image 98](<2013-bannai-spherical-designs-harmonic-index_images/imageFile98.png>)

−α

Jα(z). This convergence is uniform in every bounded region of the complex z-plane. Also by [17, 192 page], limt→∞ tθn,i(t) = jα,i. Finally,

- (6) lim


tα c′n,t

bn,t = lim

1 −

![image 99](<2013-bannai-spherical-designs-harmonic-index_images/imageFile99.png>)

t→∞

t→∞

= 1 − lim

t→∞

tα c′n,t

tα Pn,t cosθn(t+2−1),1

.

= 1 − lim

![image 100](<2013-bannai-spherical-designs-harmonic-index_images/imageFile100.png>)

![image 101](<2013-bannai-spherical-designs-harmonic-index_images/imageFile101.png>)

t→∞

Put zm = mθn(m+2−,1)1 . Then lim

m m − 1

m m − 1

(m−1)θn(m+2−,1)1 = 1·jα+1,1 = jα+1,1. Since the convergence is uniform,

(m−1)θn(m+2−,1)1 = lim

zm = lim

lim

![image 102](<2013-bannai-spherical-designs-harmonic-index_images/imageFile102.png>)

![image 103](<2013-bannai-spherical-designs-harmonic-index_images/imageFile103.png>)

m→∞

m→∞

m→∞

m→∞

tθn(t+2−1),1 t

zm t

t−αPn,t cosθn(t+2−1),1 = lim

t−αPn,t cos

t−αPn,t cos

= lim

lim

lim

![image 104](<2013-bannai-spherical-designs-harmonic-index_images/imageFile104.png>)

![image 105](<2013-bannai-spherical-designs-harmonic-index_images/imageFile105.png>)

m→∞

t→∞

t→∞

t→∞

−α

zm 2

= lim

(7) Jα(zm) = Fn(jα+1,1). By (6) and (7), the proof of the proposition is completed.

![image 106](<2013-bannai-spherical-designs-harmonic-index_images/imageFile106.png>)

m→∞

The set of lines passing through the origin in Rn is called equiangular lines if any distinct two lines in the set make the same angle. If X ⊂ Rn satisﬁes I(X) = {±α}, the set of lines combining the origin and the points of X forms equiangular lines. Since x and −x give the same line, we obtain equiangular lines with at least |X|/2 lines from this construction. If a tight harmonic index t-design X exists, then I(X) = {±α} by Corollary 4.1, and since X = −X does not hold by the tightness, we obtain equiangular lines with at least |X|/2 + 1 lines. It is well-known that the cardinality of equiangular lines in Rn is bounded above by n(n + 1)/2 ([14]). For small n’s, calculating the covergence value of Proposition 4.1, we have b3 = 3.482871935 (6), b4 = 5.079602836 (10), b5 = 8.559751097 (15),

- b6 = 16.42679115 (21), b7 = 35.11842602 (28), b8 = 81.85047703 (36), b9 =


204.5294426 (45), b10 = 541.6547218 (55) where the parentheses denotes the value n(n+1)/2 for each n. Hence we see that, for n = 8,9,10, a tight harmonic index tdesign does not exist for large enough t. Also we note that bn,t is not monotonously increasing in the case when n = 4.

From now on, we consider the case when t = 4.

- Proposition 4.2.


(n + 1)(n + 2) 6

.

bn,4 =

![image 107](<2013-bannai-spherical-designs-harmonic-index_images/imageFile107.png>)

In particular, bn,4 is an integer if and only if n is not divided by 3. Furthermore, in that case, for X ⊂ Sn−1 with |X| = bn,4, the following are equivalent:

- (i) X is a hamonic index 4-design,
- (ii) I(X) ⊂ ± n+43 .


![image 108](<2013-bannai-spherical-designs-harmonic-index_images/imageFile108.png>)

![image 109](<2013-bannai-spherical-designs-harmonic-index_images/imageFile109.png>)

Proof.

n(n + 6) 24

n(n + 6) 24 {(n+2)(n+4)x4−6(n+2)x2+3} =

Qn,4(x) =

![image 110](<2013-bannai-spherical-designs-harmonic-index_images/imageFile110.png>)

![image 111](<2013-bannai-spherical-designs-harmonic-index_images/imageFile111.png>)

3 n + 4

(n + 2)(n + 4) s2 −

![image 112](<2013-bannai-spherical-designs-harmonic-index_images/imageFile112.png>)

n(n + 1)(n + 6) 4(n + 4)

at x2 =

Hence on [−1,1], Qn,4(x) attains the minimum cn,4 = −

![image 113](<2013-bannai-spherical-designs-harmonic-index_images/imageFile113.png>)

- 3

![image 114](<2013-bannai-spherical-designs-harmonic-index_images/imageFile114.png>)

n + 4

. Therefore, we have bn,4 =

(n + 1)(n + 2) 6

![image 115](<2013-bannai-spherical-designs-harmonic-index_images/imageFile115.png>)

. It is clear that bn,4 is an integer if and only if n is not a multiple of 3. Also the latter of the assertion in the proposition follows from the ﬁnal assertion of Theorem 2.

Lemma 4.1 (Musin[15]). Let N be a natural number and 0 < α < 1. Then the following are equivalent:

- (i) there exists X ⊂ Sn−1 with |X| = N and I(X) ⊂ {±α},
- (ii) there exists Y ⊂ Sn−2 with |Y | = N − 1 and I(Y ) ⊂


α 1 + α

![image 116](<2013-bannai-spherical-designs-harmonic-index_images/imageFile116.png>)

, −α 1 − α

![image 117](<2013-bannai-spherical-designs-harmonic-index_images/imageFile117.png>)

. More-

over if 1/2 < α < 1, then we may suppose I(Y ) ⊂

α 1 + α

![image 118](<2013-bannai-spherical-designs-harmonic-index_images/imageFile118.png>)

. By Lemma 4.1, we have the following corollary:

Corollary 4.2. For t = 4 and n = 4,5, there does not exist a tight harmonic index

- 4-design.


Proof. We show the case when t = 4 and n = 4. The case when n = 5 is shown similarly. Suppose that X is s a tight 4-design on S3. Then X satisﬁes |X| = 5 and I(X) ⊂ ± 3/8 . By Lemma 4.1, in this case, there exists Y ⊂ S2 such that |Y | = 4 and

![image 119](<2013-bannai-spherical-designs-harmonic-index_images/imageFile119.png>)

2√6 − 3 5

![image 120](<2013-bannai-spherical-designs-harmonic-index_images/imageFile120.png>)

 

 

3 8

![image 121](<2013-bannai-spherical-designs-harmonic-index_images/imageFile121.png>)

![image 122](<2013-bannai-spherical-designs-harmonic-index_images/imageFile122.png>)

.

I(Y ) ⊂

=

![image 123](<2013-bannai-spherical-designs-harmonic-index_images/imageFile123.png>)

![image 124](<2013-bannai-spherical-designs-harmonic-index_images/imageFile124.png>)

![image 125](<2013-bannai-spherical-designs-harmonic-index_images/imageFile125.png>)

1 + 38





![image 126](<2013-bannai-spherical-designs-harmonic-index_images/imageFile126.png>)

But Y is a regular simplex on S2 with I(Y ) = {−1/3}. This is a contradiction.

In order to show the non-existence of tight harmonic index 4-designs on Sn−1 for some more n, we use the method of Einhorn-Schoenberg [9]. The ﬁnite subset X on Euclidean space is called a 2-distance set if the number of distances appearing on

2

6(n + 1) n + 4

−

![image 127](<2013-bannai-spherical-designs-harmonic-index_images/imageFile127.png>)

.

X is exactly 2. Let X = {x1,...,xm} be a 2-distance set with distances {1,(<)b}. Construct a graph G = (X,E) for X as follows. The vertex set is X, and the edge is joined when and only when the distance is b. Let B be the adjacency matrix of G indexed by X = {x1,...,xm}. Put C := (b2 − 1)B + J − I. Let L be a (m − 1) × (m − 1) matrix with the (i − 1,j − 1)-entry Li−1,j−1 := C1i + C1j − Cij where Cij denotes the (i,j)-entry of C and i,j move from 2 to m. Then if X can be isometrically embedded in Rn, then the rank of L must be at most n.

Let X be a tight harmonic index 4-design on S6. Then by Proposition 4.2, |X| = 12,I(X) ⊂ {± 3/11}. In particular, there must be a 2-distance set of 9 points with b2 =

![image 128](<2013-bannai-spherical-designs-harmonic-index_images/imageFile128.png>)

7 + √33 4

![image 129](<2013-bannai-spherical-designs-harmonic-index_images/imageFile129.png>)

on R7. By using Magma and the database of graphs with 9 points (including inconnected ones), we checked by the above method whether there exists a graph of 9 points which can be isometrically embedded in R7 as a 2distance set with b2 =

![image 130](<2013-bannai-spherical-designs-harmonic-index_images/imageFile130.png>)

7 + √33 4

![image 131](<2013-bannai-spherical-designs-harmonic-index_images/imageFile131.png>)

, and from this calculation, we found 60 possibilities of graphs among them. Next considering all extensions of the 60 possibilities to graphs of 10 points, we checked by the above method whether there exists an extended graph which can be isometrically embedded in R7 with b2 =

![image 132](<2013-bannai-spherical-designs-harmonic-index_images/imageFile132.png>)

7 + √33 4

![image 133](<2013-bannai-spherical-designs-harmonic-index_images/imageFile133.png>)

![image 134](<2013-bannai-spherical-designs-harmonic-index_images/imageFile134.png>)

among them, and we found that such an extended graph of 10 points does not exist. This means that there does not exist a 2-distance set of 10 points in R7

7 + √33 4

![image 135](<2013-bannai-spherical-designs-harmonic-index_images/imageFile135.png>)

with b2 =

and in particular, there does not exist a tight harmonic index 4-design on S6.

![image 136](<2013-bannai-spherical-designs-harmonic-index_images/imageFile136.png>)

Similarly let X be a tight harmonic index 4-design on S7, then |X| = 15,I(X) ⊂ {±1/2}. Particularly, there is a 2-distance set of 10 points with b2 = 3 in R8. Running through all graphs of 10 points, we investigated whether there is a graph whose L is of rank at most 8, and we found that there is not such a graph. This means that there is not a 2-distance set of 10 points with b2 = 3 in R8. Therefore we see that there is not a tight harmonic index 4-design on S7.

Next we consider the case when n = 10. In this case, let X be a tight harmonic index 4-design in R10, then |X| = 22, I(X) = ± 143 . By Lemma 4.1, there is some X′ ⊂ S8 with |X′| = 21, I(X′) = α =

![image 137](<2013-bannai-spherical-designs-harmonic-index_images/imageFile137.png>)

![image 138](<2013-bannai-spherical-designs-harmonic-index_images/imageFile138.png>)

√3 √14 + √3

√3 √14 −

![image 139](<2013-bannai-spherical-designs-harmonic-index_images/imageFile139.png>)

![image 140](<2013-bannai-spherical-designs-harmonic-index_images/imageFile140.png>)

,β = −

√3

. Fix a

![image 141](<2013-bannai-spherical-designs-harmonic-index_images/imageFile141.png>)

![image 142](<2013-bannai-spherical-designs-harmonic-index_images/imageFile142.png>)

![image 143](<2013-bannai-spherical-designs-harmonic-index_images/imageFile143.png>)

![image 144](<2013-bannai-spherical-designs-harmonic-index_images/imageFile144.png>)

![image 145](<2013-bannai-spherical-designs-harmonic-index_images/imageFile145.png>)

![image 146](<2013-bannai-spherical-designs-harmonic-index_images/imageFile146.png>)

point of X′ and set Xα and Xβ to be subsets of X′ with inner products α and β from the point, respectively. Each of them lies on the circle with the same latitude. By Pigeonhole principle, |Xα| ≥ 10 or |Xβ| ≥ 10. In particular, considering like as Xα,Xβ ⊂ S7 and adjusting the norm, we can think Xα and Xβ 2-distance sets with inner products

β − α2 1 − α2

α − β2 1 − β2

α 1 + α

β 1 + β

on S7. Similar to the

,

,

,

![image 147](<2013-bannai-spherical-designs-harmonic-index_images/imageFile147.png>)

![image 148](<2013-bannai-spherical-designs-harmonic-index_images/imageFile148.png>)

![image 149](<2013-bannai-spherical-designs-harmonic-index_images/imageFile149.png>)

![image 150](<2013-bannai-spherical-designs-harmonic-index_images/imageFile150.png>)

above, by Einhorn-S choenberg’s method, we checked for all graphs of 10 points whether there is a 2-distance set with the above inner product in R8, and we found that there is not such a graph. Therefore, ﬁnally, we see that there is not a tight harmonic index 4-design in R10.

Finally we use the following theorem to investigate the existence of tight harmonic index 4-designs.

- Theorem 4 (Larman-Rogers-Seidel[13]). Let X ⊂ Rn be a 2-distance set with distances α,(<)β. If |X| > 2n + 3, then there is a natural number k at least 2 such that α2/β2 = (k − 1)/k.

From this theorem, we have the following:

- Theorem 5. Let X be a tight harmonic index 4-design on Sn−1. Then n = 2 or there is an odd p ≥ 5 such that n = 3p2 − 4.


Proof. Suppose n ≤ 10. By Proposition 4.2, when bn,4 is an integer, n = 2,4,5,7,8,10.

But as we mentioned above, in these cases, there is not a tight harmonic index 4design. Therefore we suppose n ≥ 11, and then bn,4 ≥ 2n + 4. By Proposition 4.2, if X is a tight harmonic index 4-design on Sn−1, then X is a 2-distance set with I(X) = {± 3/(n + 4)}. Therefore, by Theorem 4, there is a natural number k such that

![image 151](<2013-bannai-spherical-designs-harmonic-index_images/imageFile151.png>)

![image 152](<2013-bannai-spherical-designs-harmonic-index_images/imageFile152.png>)

2 − 2 n+43 2 + 2 n+43

![image 153](<2013-bannai-spherical-designs-harmonic-index_images/imageFile153.png>)

=

![image 154](<2013-bannai-spherical-designs-harmonic-index_images/imageFile154.png>)

![image 155](<2013-bannai-spherical-designs-harmonic-index_images/imageFile155.png>)

![image 156](<2013-bannai-spherical-designs-harmonic-index_images/imageFile156.png>)

k − 1 k

.

![image 157](<2013-bannai-spherical-designs-harmonic-index_images/imageFile157.png>)

Deforming this equation, we have

(2k − 1)

![image 158](<2013-bannai-spherical-designs-harmonic-index_images/imageFile158.png>)

3 n + 4

= 1.

![image 159](<2013-bannai-spherical-designs-harmonic-index_images/imageFile159.png>)

Hence if we put p = 2k − 1, then n = 3p2 − 4. When p = 3, that is, n = 23, a tight harmonic index 4-design X in R23 satisﬁes

|X| = 100 and I(X) = ±13 . So we obtain equiangular lines of at least 51 lines in R23. But, since the maximum number of equiangular lines with inner product 1/3

![image 160](<2013-bannai-spherical-designs-harmonic-index_images/imageFile160.png>)

is 44 ([14]), there is not a tight harmonic index 4-design in R23.

Remark 2. Wei-Hsuan Yu (University of Maryland) informed us in a private communication (July, 2013) that there are no tight harmonic 4-designs for p = 5,7,9 in Theorem 5. He showed that in these 3 cases the maximum sizes of equiangular lines with inner product 1/p are respectively 416, 1506, 3952, by using the semi-deﬁnite programming, which are strictly smaller than (n + 1)(n + 2)/6 = 876,3480,9640 (respectively), and this is a contradiction. Similar results are also expected for larger p, but it seems diﬃcult to deal with the semideﬁnite programming for larger dimensions.

Acknowledgement. We are grateful to A. Munemasa for his help to the Groebner basis calculation in this paper. Also we would like to thank A. Barg, O. Musin and W-H. Yu for the fruitful discussion. E. Bannai is supported in part by NSFC grant No. 11271257. T. Okuda is supported by Grant-in-Aid for JSPS Fellow No.25-6095.

5. Appendix I

In the table below, n denotes the dimension, t the harmonic index, the inner value is the corresponding bn,t.

![image 161](<2013-bannai-spherical-designs-harmonic-index_images/imageFile161.png>)

![image 162](<2013-bannai-spherical-designs-harmonic-index_images/imageFile162.png>)

![image 163](<2013-bannai-spherical-designs-harmonic-index_images/imageFile163.png>)

![image 164](<2013-bannai-spherical-designs-harmonic-index_images/imageFile164.png>)

![image 165](<2013-bannai-spherical-designs-harmonic-index_images/imageFile165.png>)

![image 166](<2013-bannai-spherical-designs-harmonic-index_images/imageFile166.png>)

![image 167](<2013-bannai-spherical-designs-harmonic-index_images/imageFile167.png>)

![image 168](<2013-bannai-spherical-designs-harmonic-index_images/imageFile168.png>)

n = 3 n = 4 n = 5 n = 6 n = 7 n = 8 n = 9 n = 10 t = 4 3.33.. 5 7 9.33.. 12 15 18.33.. 22 t = 6 3.41.. 5.29.. 7.69.. 10.69.. 14.33.. 18.67.. 23.76.. 29.68.. t = 8 3.44.. 5.41.. 8.01.. 11.35.. 15.55.. 20.72.. 27.004.. 34.52..

![image 169](<2013-bannai-spherical-designs-harmonic-index_images/imageFile169.png>)

![image 170](<2013-bannai-spherical-designs-harmonic-index_images/imageFile170.png>)

![image 171](<2013-bannai-spherical-designs-harmonic-index_images/imageFile171.png>)

![image 172](<2013-bannai-spherical-designs-harmonic-index_images/imageFile172.png>)

![image 173](<2013-bannai-spherical-designs-harmonic-index_images/imageFile173.png>)

![image 174](<2013-bannai-spherical-designs-harmonic-index_images/imageFile174.png>)

![image 175](<2013-bannai-spherical-designs-harmonic-index_images/imageFile175.png>)

![image 176](<2013-bannai-spherical-designs-harmonic-index_images/imageFile176.png>)

![image 177](<2013-bannai-spherical-designs-harmonic-index_images/imageFile177.png>)

![image 178](<2013-bannai-spherical-designs-harmonic-index_images/imageFile178.png>)

![image 179](<2013-bannai-spherical-designs-harmonic-index_images/imageFile179.png>)

![image 180](<2013-bannai-spherical-designs-harmonic-index_images/imageFile180.png>)

![image 181](<2013-bannai-spherical-designs-harmonic-index_images/imageFile181.png>)

![image 182](<2013-bannai-spherical-designs-harmonic-index_images/imageFile182.png>)

![image 183](<2013-bannai-spherical-designs-harmonic-index_images/imageFile183.png>)

![image 184](<2013-bannai-spherical-designs-harmonic-index_images/imageFile184.png>)

![image 185](<2013-bannai-spherical-designs-harmonic-index_images/imageFile185.png>)

![image 186](<2013-bannai-spherical-designs-harmonic-index_images/imageFile186.png>)

![image 187](<2013-bannai-spherical-designs-harmonic-index_images/imageFile187.png>)

![image 188](<2013-bannai-spherical-designs-harmonic-index_images/imageFile188.png>)

![image 189](<2013-bannai-spherical-designs-harmonic-index_images/imageFile189.png>)

![image 190](<2013-bannai-spherical-designs-harmonic-index_images/imageFile190.png>)

![image 191](<2013-bannai-spherical-designs-harmonic-index_images/imageFile191.png>)

![image 192](<2013-bannai-spherical-designs-harmonic-index_images/imageFile192.png>)

![image 193](<2013-bannai-spherical-designs-harmonic-index_images/imageFile193.png>)

![image 194](<2013-bannai-spherical-designs-harmonic-index_images/imageFile194.png>)

![image 195](<2013-bannai-spherical-designs-harmonic-index_images/imageFile195.png>)

![image 196](<2013-bannai-spherical-designs-harmonic-index_images/imageFile196.png>)

![image 197](<2013-bannai-spherical-designs-harmonic-index_images/imageFile197.png>)

![image 198](<2013-bannai-spherical-designs-harmonic-index_images/imageFile198.png>)

![image 199](<2013-bannai-spherical-designs-harmonic-index_images/imageFile199.png>)

![image 200](<2013-bannai-spherical-designs-harmonic-index_images/imageFile200.png>)

![image 201](<2013-bannai-spherical-designs-harmonic-index_images/imageFile201.png>)

![image 202](<2013-bannai-spherical-designs-harmonic-index_images/imageFile202.png>)

![image 203](<2013-bannai-spherical-designs-harmonic-index_images/imageFile203.png>)

![image 204](<2013-bannai-spherical-designs-harmonic-index_images/imageFile204.png>)

t = 10 3.45.. 5.47.. 8.18.. 11.73.. 16.26.. 21.97.. 29.04.. 37.69.. t = 12 3.46.. 5.51.. 8.28.. 11.95.. 16.71.. 22.77.. 30.39.. 39.84.. t = 14 3.46.. 5.53.. 8.35.. 12.10.. 17.22.. 23.32.. 31.33.. 41.37.. t = 16 3.47.. 5.54.. 8.39.. 12.21.. 17.37.. 23.71.. 32.01.. 42.48.. t = 18 3.47.. 5.56.. 8.42.. 12.28.. 17.37.. 24.004.. 32.51.. 43.32.. t = 20 3.47.. 5.56.. 8.45.. 12.34.. 17.49.. 24.22.. 32.89.. 43.97..

![image 205](<2013-bannai-spherical-designs-harmonic-index_images/imageFile205.png>)

![image 206](<2013-bannai-spherical-designs-harmonic-index_images/imageFile206.png>)

![image 207](<2013-bannai-spherical-designs-harmonic-index_images/imageFile207.png>)

![image 208](<2013-bannai-spherical-designs-harmonic-index_images/imageFile208.png>)

![image 209](<2013-bannai-spherical-designs-harmonic-index_images/imageFile209.png>)

![image 210](<2013-bannai-spherical-designs-harmonic-index_images/imageFile210.png>)

![image 211](<2013-bannai-spherical-designs-harmonic-index_images/imageFile211.png>)

![image 212](<2013-bannai-spherical-designs-harmonic-index_images/imageFile212.png>)

![image 213](<2013-bannai-spherical-designs-harmonic-index_images/imageFile213.png>)

![image 214](<2013-bannai-spherical-designs-harmonic-index_images/imageFile214.png>)

![image 215](<2013-bannai-spherical-designs-harmonic-index_images/imageFile215.png>)

![image 216](<2013-bannai-spherical-designs-harmonic-index_images/imageFile216.png>)

![image 217](<2013-bannai-spherical-designs-harmonic-index_images/imageFile217.png>)

![image 218](<2013-bannai-spherical-designs-harmonic-index_images/imageFile218.png>)

![image 219](<2013-bannai-spherical-designs-harmonic-index_images/imageFile219.png>)

![image 220](<2013-bannai-spherical-designs-harmonic-index_images/imageFile220.png>)

![image 221](<2013-bannai-spherical-designs-harmonic-index_images/imageFile221.png>)

![image 222](<2013-bannai-spherical-designs-harmonic-index_images/imageFile222.png>)

![image 223](<2013-bannai-spherical-designs-harmonic-index_images/imageFile223.png>)

![image 224](<2013-bannai-spherical-designs-harmonic-index_images/imageFile224.png>)

![image 225](<2013-bannai-spherical-designs-harmonic-index_images/imageFile225.png>)

![image 226](<2013-bannai-spherical-designs-harmonic-index_images/imageFile226.png>)

![image 227](<2013-bannai-spherical-designs-harmonic-index_images/imageFile227.png>)

![image 228](<2013-bannai-spherical-designs-harmonic-index_images/imageFile228.png>)

![image 229](<2013-bannai-spherical-designs-harmonic-index_images/imageFile229.png>)

![image 230](<2013-bannai-spherical-designs-harmonic-index_images/imageFile230.png>)

![image 231](<2013-bannai-spherical-designs-harmonic-index_images/imageFile231.png>)

![image 232](<2013-bannai-spherical-designs-harmonic-index_images/imageFile232.png>)

![image 233](<2013-bannai-spherical-designs-harmonic-index_images/imageFile233.png>)

![image 234](<2013-bannai-spherical-designs-harmonic-index_images/imageFile234.png>)

![image 235](<2013-bannai-spherical-designs-harmonic-index_images/imageFile235.png>)

![image 236](<2013-bannai-spherical-designs-harmonic-index_images/imageFile236.png>)

![image 237](<2013-bannai-spherical-designs-harmonic-index_images/imageFile237.png>)

![image 238](<2013-bannai-spherical-designs-harmonic-index_images/imageFile238.png>)

![image 239](<2013-bannai-spherical-designs-harmonic-index_images/imageFile239.png>)

![image 240](<2013-bannai-spherical-designs-harmonic-index_images/imageFile240.png>)

![image 241](<2013-bannai-spherical-designs-harmonic-index_images/imageFile241.png>)

![image 242](<2013-bannai-spherical-designs-harmonic-index_images/imageFile242.png>)

![image 243](<2013-bannai-spherical-designs-harmonic-index_images/imageFile243.png>)

![image 244](<2013-bannai-spherical-designs-harmonic-index_images/imageFile244.png>)

![image 245](<2013-bannai-spherical-designs-harmonic-index_images/imageFile245.png>)

![image 246](<2013-bannai-spherical-designs-harmonic-index_images/imageFile246.png>)

![image 247](<2013-bannai-spherical-designs-harmonic-index_images/imageFile247.png>)

![image 248](<2013-bannai-spherical-designs-harmonic-index_images/imageFile248.png>)

![image 249](<2013-bannai-spherical-designs-harmonic-index_images/imageFile249.png>)

6. Appendix II

- P1 = s1 −

2065889 90

![image 250](<2013-bannai-spherical-designs-harmonic-index_images/imageFile250.png>)

s2s10s311s612 +

133819 5

![image 251](<2013-bannai-spherical-designs-harmonic-index_images/imageFile251.png>)

s2s10s311s412 −

53179 6

![image 252](<2013-bannai-spherical-designs-harmonic-index_images/imageFile252.png>)

s2s10s311s212 +

8691 10

![image 253](<2013-bannai-spherical-designs-harmonic-index_images/imageFile253.png>)

s2s10s311 −

42787813648741 1534950

![image 254](<2013-bannai-spherical-designs-harmonic-index_images/imageFile254.png>)

s2s10s11s1412 +

115559013011239 1534950

![image 255](<2013-bannai-spherical-designs-harmonic-index_images/imageFile255.png>)

s2s10s11s1212 −

7079980409537 85275

![image 256](<2013-bannai-spherical-designs-harmonic-index_images/imageFile256.png>)

s2s10s11s1012 + 12340902711704 255825

![image 257](<2013-bannai-spherical-designs-harmonic-index_images/imageFile257.png>)

s2s10s11s812 −

451353797911 28425

![image 258](<2013-bannai-spherical-designs-harmonic-index_images/imageFile258.png>)

s2s10s11s612 +

502755386489 170550

![image 259](<2013-bannai-spherical-designs-harmonic-index_images/imageFile259.png>)

s2s10s11s412 −

16159950307 56850

![image 260](<2013-bannai-spherical-designs-harmonic-index_images/imageFile260.png>)

s2s10s11s212 +

620366243 56850

![image 261](<2013-bannai-spherical-designs-harmonic-index_images/imageFile261.png>)

s2s10s11

- P2 = s22 +

123226544609 153495

![image 262](<2013-bannai-spherical-designs-harmonic-index_images/imageFile262.png>)

s1412 −

12142761148 5685

![image 263](<2013-bannai-spherical-designs-harmonic-index_images/imageFile263.png>)

s1212 +

13149854522 5685

![image 264](<2013-bannai-spherical-designs-harmonic-index_images/imageFile264.png>)

s1012 −

22430288734 17055

![image 265](<2013-bannai-spherical-designs-harmonic-index_images/imageFile265.png>)

s812 +

7204390444 17055

![image 266](<2013-bannai-spherical-designs-harmonic-index_images/imageFile266.png>)

s612 −

434722732 5685

![image 267](<2013-bannai-spherical-designs-harmonic-index_images/imageFile267.png>)

s412 +

13667541 1895

![image 268](<2013-bannai-spherical-designs-harmonic-index_images/imageFile268.png>)

s212 −

518644 1895

![image 269](<2013-bannai-spherical-designs-harmonic-index_images/imageFile269.png>)

,

- P3 = s4 −


1169 15

723 10

14 5

931 90

s6s8s9s10s11s612 +

s6s8s9s10s11s412 −

s6s8s9s10s11s212 +

s6s8s9s10s11 −

![image 270](<2013-bannai-spherical-designs-harmonic-index_images/imageFile270.png>)

![image 271](<2013-bannai-spherical-designs-harmonic-index_images/imageFile271.png>)

![image 272](<2013-bannai-spherical-designs-harmonic-index_images/imageFile272.png>)

![image 273](<2013-bannai-spherical-designs-harmonic-index_images/imageFile273.png>)

2032163 30

393431 18

43413 20

6570067 108

s6s29s10s211s12 −

s6s29s10s211s712 +

s6s29s10s211s512 −

s6s29s10s211s312 +

![image 274](<2013-bannai-spherical-designs-harmonic-index_images/imageFile274.png>)

![image 275](<2013-bannai-spherical-designs-harmonic-index_images/imageFile275.png>)

![image 276](<2013-bannai-spherical-designs-harmonic-index_images/imageFile276.png>)

![image 277](<2013-bannai-spherical-designs-harmonic-index_images/imageFile277.png>)

3875621 180

1182097 180

36059 60

5384771 270

s6s29s10s712 +

s6s29s10s512 −

s6s29s10s312 +

s6s29s10s12

![image 278](<2013-bannai-spherical-designs-harmonic-index_images/imageFile278.png>)

![image 279](<2013-bannai-spherical-designs-harmonic-index_images/imageFile279.png>)

![image 280](<2013-bannai-spherical-designs-harmonic-index_images/imageFile280.png>)

![image 281](<2013-bannai-spherical-designs-harmonic-index_images/imageFile281.png>)

356573 90

117439 36

27467 60

1849 60

s6s10s211s712 −

s6s10s211s512 +

s6s10s211s312 +

s6s10s211s12 −

+

![image 282](<2013-bannai-spherical-designs-harmonic-index_images/imageFile282.png>)

![image 283](<2013-bannai-spherical-designs-harmonic-index_images/imageFile283.png>)

![image 284](<2013-bannai-spherical-designs-harmonic-index_images/imageFile284.png>)

![image 285](<2013-bannai-spherical-designs-harmonic-index_images/imageFile285.png>)

33389002989181 341100

165129256285693 1534950

669664592777551 18419400

s6s10s1512 +

s6s10s1312 −

s6s10s1112

![image 286](<2013-bannai-spherical-designs-harmonic-index_images/imageFile286.png>)

![image 287](<2013-bannai-spherical-designs-harmonic-index_images/imageFile287.png>)

![image 288](<2013-bannai-spherical-designs-harmonic-index_images/imageFile288.png>)

10457057636549 511650

1291518147979 341100

21245809013441 341100

s6s10s512 −

s6s10s912 −

s6s10s712 +

+

![image 289](<2013-bannai-spherical-designs-harmonic-index_images/imageFile289.png>)

![image 290](<2013-bannai-spherical-designs-harmonic-index_images/imageFile290.png>)

![image 291](<2013-bannai-spherical-designs-harmonic-index_images/imageFile291.png>)

248918696267 682200

1591261873 113700

s6s10s312 +

s6s10s12,

![image 292](<2013-bannai-spherical-designs-harmonic-index_images/imageFile292.png>)

![image 293](<2013-bannai-spherical-designs-harmonic-index_images/imageFile293.png>)

- P4 = s5 −

21413 90

![image 294](<2013-bannai-spherical-designs-harmonic-index_images/imageFile294.png>)

s6s8s9s612 +

12698 45

![image 295](<2013-bannai-spherical-designs-harmonic-index_images/imageFile295.png>)

s6s8s9s412 −

547 6

![image 296](<2013-bannai-spherical-designs-harmonic-index_images/imageFile296.png>)

s6s8s9s212 +

157 15

![image 297](<2013-bannai-spherical-designs-harmonic-index_images/imageFile297.png>)

s6s8s9 +

234370871 2700

![image 298](<2013-bannai-spherical-designs-harmonic-index_images/imageFile298.png>)

s6s29s311s712 −

10332679 108

![image 299](<2013-bannai-spherical-designs-harmonic-index_images/imageFile299.png>)

s6s29s311s512 +

8818663 300

![image 300](<2013-bannai-spherical-designs-harmonic-index_images/imageFile300.png>)

s6s29s311s312 −

612916 225

![image 301](<2013-bannai-spherical-designs-harmonic-index_images/imageFile301.png>)

s6s29s311s12 −

119641879 2700

![image 302](<2013-bannai-spherical-designs-harmonic-index_images/imageFile302.png>)

s6s29s11s712

+

13122571 270

![image 303](<2013-bannai-spherical-designs-harmonic-index_images/imageFile303.png>)

s6s29s11s512 −

2260261 150

![image 304](<2013-bannai-spherical-designs-harmonic-index_images/imageFile304.png>)

s6s29s11s312 +

1280941 900

![image 305](<2013-bannai-spherical-designs-harmonic-index_images/imageFile305.png>)

s6s29s11s12 −

33137083 900

![image 306](<2013-bannai-spherical-designs-harmonic-index_images/imageFile306.png>)

s6s311s712

+

3377731 90

![image 307](<2013-bannai-spherical-designs-harmonic-index_images/imageFile307.png>)

s6s311s512 −

1659631 150

![image 308](<2013-bannai-spherical-designs-harmonic-index_images/imageFile308.png>)

s6s311s312 +

292957 300

![image 309](<2013-bannai-spherical-designs-harmonic-index_images/imageFile309.png>)

s6s311s12 +

73245280332707 92097000

![image 310](<2013-bannai-spherical-designs-harmonic-index_images/imageFile310.png>)

s6s11s1512 −

450846965863 189500

![image 311](<2013-bannai-spherical-designs-harmonic-index_images/imageFile311.png>)

s6s11s1312 +

10986176538638 3837375

![image 312](<2013-bannai-spherical-designs-harmonic-index_images/imageFile312.png>)

s6s11s1112 −

2315729753414 1279125

![image 313](<2013-bannai-spherical-designs-harmonic-index_images/imageFile313.png>)

s6s11s912

+

1139869081667 1705500

![image 314](<2013-bannai-spherical-designs-harmonic-index_images/imageFile314.png>)

s6s11s712 −

21377631109 142125

![image 315](<2013-bannai-spherical-designs-harmonic-index_images/imageFile315.png>)

s6s11s512 +

66029795539 3411000

![image 316](<2013-bannai-spherical-designs-harmonic-index_images/imageFile316.png>)

s6s11s312 −

605545711 568500

![image 317](<2013-bannai-spherical-designs-harmonic-index_images/imageFile317.png>)

s6s11s12,

- P5 = s26 + s29 +

31477292476 51165

![image 318](<2013-bannai-spherical-designs-harmonic-index_images/imageFile318.png>)

s1412 −

28546636678 17055

![image 319](<2013-bannai-spherical-designs-harmonic-index_images/imageFile319.png>)

s1212 +

31772393212 17055

![image 320](<2013-bannai-spherical-designs-harmonic-index_images/imageFile320.png>)

s1012 −

18667559008 17055

![image 321](<2013-bannai-spherical-designs-harmonic-index_images/imageFile321.png>)

s812

+

2075243891 5685

![image 322](<2013-bannai-spherical-designs-harmonic-index_images/imageFile322.png>)

s612 −

130374328 1895

![image 323](<2013-bannai-spherical-designs-harmonic-index_images/imageFile323.png>)

s412 +

12793807 1895

![image 324](<2013-bannai-spherical-designs-harmonic-index_images/imageFile324.png>)

s212 −

502928 1895

![image 325](<2013-bannai-spherical-designs-harmonic-index_images/imageFile325.png>)

,

- P6 = s7 +

80066 225

![image 326](<2013-bannai-spherical-designs-harmonic-index_images/imageFile326.png>)

s8s10s11s612 −

11473 25

![image 327](<2013-bannai-spherical-designs-harmonic-index_images/imageFile327.png>)

s8s10s11s412 +

514 3

![image 328](<2013-bannai-spherical-designs-harmonic-index_images/imageFile328.png>)

s8s10s11s212 −

326 25

![image 329](<2013-bannai-spherical-designs-harmonic-index_images/imageFile329.png>)

s8s10s11

+

149163889 1350

![image 330](<2013-bannai-spherical-designs-harmonic-index_images/imageFile330.png>)

s39s10s211s712 −

166091023 1350

![image 331](<2013-bannai-spherical-designs-harmonic-index_images/imageFile331.png>)

s39s10s211s512 +

1981177 50

![image 332](<2013-bannai-spherical-designs-harmonic-index_images/imageFile332.png>)

s39s10s211s312 −

882044 225

![image 333](<2013-bannai-spherical-designs-harmonic-index_images/imageFile333.png>)

s39s10s211s12

+

31101917 1350

![image 334](<2013-bannai-spherical-designs-harmonic-index_images/imageFile334.png>)

s39s10s712 −

5639221 225

![image 335](<2013-bannai-spherical-designs-harmonic-index_images/imageFile335.png>)

s39s10s512 +

1748518 225

![image 336](<2013-bannai-spherical-designs-harmonic-index_images/imageFile336.png>)

s39s10s312 −

110357 150

![image 337](<2013-bannai-spherical-designs-harmonic-index_images/imageFile337.png>)

s39s10s12 −

10474681 270

![image 338](<2013-bannai-spherical-designs-harmonic-index_images/imageFile338.png>)

s9s10s211s712 +

9832354 225

![image 339](<2013-bannai-spherical-designs-harmonic-index_images/imageFile339.png>)

s9s10s211s512 −

128839 9

![image 340](<2013-bannai-spherical-designs-harmonic-index_images/imageFile340.png>)

s9s10s211s312 +

215869 150

![image 341](<2013-bannai-spherical-designs-harmonic-index_images/imageFile341.png>)

s9s10s211s12

+

350356120184819 15349500

![image 342](<2013-bannai-spherical-designs-harmonic-index_images/imageFile342.png>)

s9s10s1512 −

17538932686289 284250

![image 343](<2013-bannai-spherical-designs-harmonic-index_images/imageFile343.png>)

s9s10s1312 +

261228066120826 3837375

![image 344](<2013-bannai-spherical-designs-harmonic-index_images/imageFile344.png>)

s9s10s1112 −

50587288180003 1279125

![image 345](<2013-bannai-spherical-designs-harmonic-index_images/imageFile345.png>)

s9s10s912 +

33283484702111 2558250

![image 346](<2013-bannai-spherical-designs-harmonic-index_images/imageFile346.png>)

s9s10s712 −

343022968073 142125

![image 347](<2013-bannai-spherical-designs-harmonic-index_images/imageFile347.png>)

s9s10s512

+

132249006263 568500

![image 348](<2013-bannai-spherical-designs-harmonic-index_images/imageFile348.png>)

s9s10s312 −

845412947 94750

![image 349](<2013-bannai-spherical-designs-harmonic-index_images/imageFile349.png>)

s9s10s12,

@

- P7 = s28 −


15771 25

3884 15

12103 25

s8s9s11s712 +

s8s9s11s512 −

s8s9s11s312 +

![image 350](<2013-bannai-spherical-designs-harmonic-index_images/imageFile350.png>)

![image 351](<2013-bannai-spherical-designs-harmonic-index_images/imageFile351.png>)

![image 352](<2013-bannai-spherical-designs-harmonic-index_images/imageFile352.png>)

47836 75

5999 150

4958 75

111398 45

s29s211s412 −

s29s211s212 +

s29s211 −

s29s612 +

+

![image 353](<2013-bannai-spherical-designs-harmonic-index_images/imageFile353.png>)

![image 354](<2013-bannai-spherical-designs-harmonic-index_images/imageFile354.png>)

![image 355](<2013-bannai-spherical-designs-harmonic-index_images/imageFile355.png>)

![image 356](<2013-bannai-spherical-designs-harmonic-index_images/imageFile356.png>)

154501 150

1771 6

1147 50

222257 225

25127 1050

s211s612 −

s211s412 +

s211s212 −

s29 +

+

![image 357](<2013-bannai-spherical-designs-harmonic-index_images/imageFile357.png>)

![image 358](<2013-bannai-spherical-designs-harmonic-index_images/imageFile358.png>)

![image 359](<2013-bannai-spherical-designs-harmonic-index_images/imageFile359.png>)

![image 360](<2013-bannai-spherical-designs-harmonic-index_images/imageFile360.png>)

![image 361](<2013-bannai-spherical-designs-harmonic-index_images/imageFile361.png>)

1807447305433 1279125

2072199005099 2558250

9949282989527 7674750

s1212 −

s1012 +

s812 −

+

![image 362](<2013-bannai-spherical-designs-harmonic-index_images/imageFile362.png>)

![image 363](<2013-bannai-spherical-designs-harmonic-index_images/imageFile363.png>)

![image 364](<2013-bannai-spherical-designs-harmonic-index_images/imageFile364.png>)

287748973489 5969250

6099957393 1326500

343461673 1989750

s412 −

s212 +

+

,

![image 365](<2013-bannai-spherical-designs-harmonic-index_images/imageFile365.png>)

![image 366](<2013-bannai-spherical-designs-harmonic-index_images/imageFile366.png>)

![image 367](<2013-bannai-spherical-designs-harmonic-index_images/imageFile367.png>)

782 25

123823 50

s29s211s612

s8s9s11s12 −

![image 368](<2013-bannai-spherical-designs-harmonic-index_images/imageFile368.png>)

![image 369](<2013-bannai-spherical-designs-harmonic-index_images/imageFile369.png>)

610697 3150

19913 150

s29s412 −

s29s212

![image 370](<2013-bannai-spherical-designs-harmonic-index_images/imageFile370.png>)

![image 371](<2013-bannai-spherical-designs-harmonic-index_images/imageFile371.png>)

7439110878101 15349500

s211 −

s1412

![image 372](<2013-bannai-spherical-designs-harmonic-index_images/imageFile372.png>)

784671190763 2984625

s612

![image 373](<2013-bannai-spherical-designs-harmonic-index_images/imageFile373.png>)

- P8 = s8s29 −

931 30

![image 374](<2013-bannai-spherical-designs-harmonic-index_images/imageFile374.png>)

s8s612 +

581 15

![image 375](<2013-bannai-spherical-designs-harmonic-index_images/imageFile375.png>)

s8s412 −

27 2

![image 376](<2013-bannai-spherical-designs-harmonic-index_images/imageFile376.png>)

s8s212 +

- 4

![image 377](<2013-bannai-spherical-designs-harmonic-index_images/imageFile377.png>)

- 5


s8 +

20417761 300

![image 378](<2013-bannai-spherical-designs-harmonic-index_images/imageFile378.png>)

s39s311s712 −

13248179 180

![image 379](<2013-bannai-spherical-designs-harmonic-index_images/imageFile379.png>)

s39s311s512

+

6730367 300

![image 380](<2013-bannai-spherical-designs-harmonic-index_images/imageFile380.png>)

s39s311s312 −

310181 150

![image 381](<2013-bannai-spherical-designs-harmonic-index_images/imageFile381.png>)

s39s311s12 −

87766301 2700

![image 382](<2013-bannai-spherical-designs-harmonic-index_images/imageFile382.png>)

s39s11s712 +

529613 15

![image 383](<2013-bannai-spherical-designs-harmonic-index_images/imageFile383.png>)

s39s11s512 −

4892887 450

![image 384](<2013-bannai-spherical-designs-harmonic-index_images/imageFile384.png>)

s39s11s312

+

305753 300

![image 385](<2013-bannai-spherical-designs-harmonic-index_images/imageFile385.png>)

s39s11s12 −

10569643 900

![image 386](<2013-bannai-spherical-designs-harmonic-index_images/imageFile386.png>)

s9s311s712 +

1102409 90

![image 387](<2013-bannai-spherical-designs-harmonic-index_images/imageFile387.png>)

s9s311s512 −

89701 25

![image 388](<2013-bannai-spherical-designs-harmonic-index_images/imageFile388.png>)

s9s311s312 +

97157 300

![image 389](<2013-bannai-spherical-designs-harmonic-index_images/imageFile389.png>)

s9s311s12

+

190976459657431 30699000

![image 390](<2013-bannai-spherical-designs-harmonic-index_images/imageFile390.png>)

s9s11s1512 −

42777492988657 2558250

![image 391](<2013-bannai-spherical-designs-harmonic-index_images/imageFile391.png>)

s9s11s1312 +

15659663136481 852750

![image 392](<2013-bannai-spherical-designs-harmonic-index_images/imageFile392.png>)

s9s11s1112 −

27213265067107 2558250

![image 393](<2013-bannai-spherical-designs-harmonic-index_images/imageFile393.png>)

s9s11s912 +

5977648644193 1705500

![image 394](<2013-bannai-spherical-designs-harmonic-index_images/imageFile394.png>)

s9s11s712 −

280742045533 426375

![image 395](<2013-bannai-spherical-designs-harmonic-index_images/imageFile395.png>)

s9s11s512

+

74541803387 1137000

![image 396](<2013-bannai-spherical-designs-harmonic-index_images/imageFile396.png>)

s9s11s312 −

381858611 142125

![image 397](<2013-bannai-spherical-designs-harmonic-index_images/imageFile397.png>)

s9s11s12,

- P9 = s8s211 −

266 9

![image 398](<2013-bannai-spherical-designs-harmonic-index_images/imageFile398.png>)

s8s612 + 39s8s412 −

43 3

![image 399](<2013-bannai-spherical-designs-harmonic-index_images/imageFile399.png>)

s8s212 + s8 +

16326947 135

![image 400](<2013-bannai-spherical-designs-harmonic-index_images/imageFile400.png>)

s39s311s712 −

2353435 18

![image 401](<2013-bannai-spherical-designs-harmonic-index_images/imageFile401.png>)

s39s311s512

+

3603841 90

![image 402](<2013-bannai-spherical-designs-harmonic-index_images/imageFile402.png>)

s39s311s312 −

111427 30

![image 403](<2013-bannai-spherical-designs-harmonic-index_images/imageFile403.png>)

s39s311s12 −

4447387 90

![image 404](<2013-bannai-spherical-designs-harmonic-index_images/imageFile404.png>)

s39s11s712 +

2887003 54

![image 405](<2013-bannai-spherical-designs-harmonic-index_images/imageFile405.png>)

s39s11s512 −

1473799 90

![image 406](<2013-bannai-spherical-designs-harmonic-index_images/imageFile406.png>)

s39s11s312 +

68422 45

![image 407](<2013-bannai-spherical-designs-harmonic-index_images/imageFile407.png>)

s39s11s12 −

4821649 270

![image 408](<2013-bannai-spherical-designs-harmonic-index_images/imageFile408.png>)

s9s311s712 +

337631 18

![image 409](<2013-bannai-spherical-designs-harmonic-index_images/imageFile409.png>)

s9s311s512 −

497281 90

![image 410](<2013-bannai-spherical-designs-harmonic-index_images/imageFile410.png>)

s9s311s312 +

2507 5

![image 411](<2013-bannai-spherical-designs-harmonic-index_images/imageFile411.png>)

s9s311s12 +

10917806127109 767475

![image 412](<2013-bannai-spherical-designs-harmonic-index_images/imageFile412.png>)

s9s11s1512 −

176502793283831 4604850

![image 413](<2013-bannai-spherical-designs-harmonic-index_images/imageFile413.png>)

s9s11s1312

+

32394402183899 767475

![image 414](<2013-bannai-spherical-designs-harmonic-index_images/imageFile414.png>)

s9s11s1112 −

37638196267127 1534950

![image 415](<2013-bannai-spherical-designs-harmonic-index_images/imageFile415.png>)

s9s11s912 +

1380774469283 170550

![image 416](<2013-bannai-spherical-designs-harmonic-index_images/imageFile416.png>)

s9s11s712 −

777290373751 511650

![image 417](<2013-bannai-spherical-designs-harmonic-index_images/imageFile417.png>)

s9s11s512 +

12800538154 85275

![image 418](<2013-bannai-spherical-designs-harmonic-index_images/imageFile418.png>)

s9s11s312 −

1029239317 170550

![image 419](<2013-bannai-spherical-designs-harmonic-index_images/imageFile419.png>)

s9s11s12,

- P10 = s8s812 −

204 133

![image 420](<2013-bannai-spherical-designs-harmonic-index_images/imageFile420.png>)

s8s612 +

732 931

![image 421](<2013-bannai-spherical-designs-harmonic-index_images/imageFile421.png>)

s8s412 −

144 931

![image 422](<2013-bannai-spherical-designs-harmonic-index_images/imageFile422.png>)

s8s212 +

9 931

![image 423](<2013-bannai-spherical-designs-harmonic-index_images/imageFile423.png>)

s8 −

1961 10

![image 424](<2013-bannai-spherical-designs-harmonic-index_images/imageFile424.png>)

s39s311s712 +

55473 266

![image 425](<2013-bannai-spherical-designs-harmonic-index_images/imageFile425.png>)

s39s311s512 −

591987 9310

![image 426](<2013-bannai-spherical-designs-harmonic-index_images/imageFile426.png>)

s39s311s312 +

27351 4655

![image 427](<2013-bannai-spherical-designs-harmonic-index_images/imageFile427.png>)

s39s311s12 +

2467 30

![image 428](<2013-bannai-spherical-designs-harmonic-index_images/imageFile428.png>)

s39s11s712 −

11731 133

![image 429](<2013-bannai-spherical-designs-harmonic-index_images/imageFile429.png>)

s39s11s512 +

125099 4655

![image 430](<2013-bannai-spherical-designs-harmonic-index_images/imageFile430.png>)

s39s11s312 −

22983 9310

![image 431](<2013-bannai-spherical-designs-harmonic-index_images/imageFile431.png>)

s39s11s12 +

451 10

![image 432](<2013-bannai-spherical-designs-harmonic-index_images/imageFile432.png>)

s9s311s712 −

5968 133

![image 433](<2013-bannai-spherical-designs-harmonic-index_images/imageFile433.png>)

s9s311s512 +

60906 4655

![image 434](<2013-bannai-spherical-designs-harmonic-index_images/imageFile434.png>)

s9s311s312 −

1551 1330

![image 435](<2013-bannai-spherical-designs-harmonic-index_images/imageFile435.png>)

s9s311s12 −

14205863 900

![image 436](<2013-bannai-spherical-designs-harmonic-index_images/imageFile436.png>)

s9s11s1512 +

9613783 225

![image 437](<2013-bannai-spherical-designs-harmonic-index_images/imageFile437.png>)

s9s11s1312 −

67333066 1425

![image 438](<2013-bannai-spherical-designs-harmonic-index_images/imageFile438.png>)

s9s11s1112 +

641577172 23275

![image 439](<2013-bannai-spherical-designs-harmonic-index_images/imageFile439.png>)

s9s11s912 −

60864437 6650

![image 440](<2013-bannai-spherical-designs-harmonic-index_images/imageFile440.png>)

s9s11s712 +

40366983 23275

![image 441](<2013-bannai-spherical-designs-harmonic-index_images/imageFile441.png>)

s9s11s512 −

16224543 93100

![image 442](<2013-bannai-spherical-designs-harmonic-index_images/imageFile442.png>)

s9s11s312 +

167133 23275

![image 443](<2013-bannai-spherical-designs-harmonic-index_images/imageFile443.png>)

s9s11s12,

- P11 = s49 −

931 3

![image 444](<2013-bannai-spherical-designs-harmonic-index_images/imageFile444.png>)

s29s612 +

1036 3

![image 445](<2013-bannai-spherical-designs-harmonic-index_images/imageFile445.png>)

s29s412 − 111s29s212 + 10s29 −

1922475898 17055

![image 446](<2013-bannai-spherical-designs-harmonic-index_images/imageFile446.png>)

s1412 +

31186458317 102330

![image 447](<2013-bannai-spherical-designs-harmonic-index_images/imageFile447.png>)

s1212 −

5734068788 17055

![image 448](<2013-bannai-spherical-designs-harmonic-index_images/imageFile448.png>)

s1012 +

3329333917 17055

![image 449](<2013-bannai-spherical-designs-harmonic-index_images/imageFile449.png>)

s812 −

364230059 5685

![image 450](<2013-bannai-spherical-designs-harmonic-index_images/imageFile450.png>)

s612 +

67069961 5685

![image 451](<2013-bannai-spherical-designs-harmonic-index_images/imageFile451.png>)

s412 −

2116188 1895

![image 452](<2013-bannai-spherical-designs-harmonic-index_images/imageFile452.png>)

s212 +

156859 3790

![image 453](<2013-bannai-spherical-designs-harmonic-index_images/imageFile453.png>)

,

- P12 = s29s812 −


186 133

![image 454](<2013-bannai-spherical-designs-harmonic-index_images/imageFile454.png>)

33227 665

s812 −

+

![image 455](<2013-bannai-spherical-designs-harmonic-index_images/imageFile455.png>)

33 49

s29s612 +

s29s412 −

![image 456](<2013-bannai-spherical-designs-harmonic-index_images/imageFile456.png>)

73329 4655

12756 4655

s612 +

![image 457](<2013-bannai-spherical-designs-harmonic-index_images/imageFile457.png>)

![image 458](<2013-bannai-spherical-designs-harmonic-index_images/imageFile458.png>)

18 133

9 931

s29s212 +

s29 −

![image 459](<2013-bannai-spherical-designs-harmonic-index_images/imageFile459.png>)

![image 460](<2013-bannai-spherical-designs-harmonic-index_images/imageFile460.png>)

117 490

36 4655

s412 −

s212 +

![image 461](<2013-bannai-spherical-designs-harmonic-index_images/imageFile461.png>)

![image 462](<2013-bannai-spherical-designs-harmonic-index_images/imageFile462.png>)

931 30

1232 15

8414 95

s1412 +

s1212 −

s1012

![image 463](<2013-bannai-spherical-designs-harmonic-index_images/imageFile463.png>)

![image 464](<2013-bannai-spherical-designs-harmonic-index_images/imageFile464.png>)

![image 465](<2013-bannai-spherical-designs-harmonic-index_images/imageFile465.png>)

,

P13 = s210 + s211 + s212 − 1,

- P14 = s411 +

266 3

![image 466](<2013-bannai-spherical-designs-harmonic-index_images/imageFile466.png>)

s211s612 −

334 3

![image 467](<2013-bannai-spherical-designs-harmonic-index_images/imageFile467.png>)

s211s412 + 44s211s212 − 6s211 +

5261982208 30699

![image 468](<2013-bannai-spherical-designs-harmonic-index_images/imageFile468.png>)

s1412 −

4743342590 10233

![image 469](<2013-bannai-spherical-designs-harmonic-index_images/imageFile469.png>)

s1212

+

5243879872 10233

![image 470](<2013-bannai-spherical-designs-harmonic-index_images/imageFile470.png>)

s1012 −

1019857462 3411

![image 471](<2013-bannai-spherical-designs-harmonic-index_images/imageFile471.png>)

s812 +

337961738 3411

![image 472](<2013-bannai-spherical-designs-harmonic-index_images/imageFile472.png>)

s612 −

21126893 1137

![image 473](<2013-bannai-spherical-designs-harmonic-index_images/imageFile473.png>)

s412 +

2064566 1137

![image 474](<2013-bannai-spherical-designs-harmonic-index_images/imageFile474.png>)

s212 −

26734 379

![image 475](<2013-bannai-spherical-designs-harmonic-index_images/imageFile475.png>)

,

- P15 = s211s812 −

186 133

![image 476](<2013-bannai-spherical-designs-harmonic-index_images/imageFile476.png>)

s211s612 +

33 49

![image 477](<2013-bannai-spherical-designs-harmonic-index_images/imageFile477.png>)

s211s412 −

18 133

![image 478](<2013-bannai-spherical-designs-harmonic-index_images/imageFile478.png>)

s211s212 +

9 931

![image 479](<2013-bannai-spherical-designs-harmonic-index_images/imageFile479.png>)

s211 −

266 9

![image 480](<2013-bannai-spherical-designs-harmonic-index_images/imageFile480.png>)

s1412 +

241 3

![image 481](<2013-bannai-spherical-designs-harmonic-index_images/imageFile481.png>)

s1212 −

35423 399

![image 482](<2013-bannai-spherical-designs-harmonic-index_images/imageFile482.png>)

s1012 +

47770 931

![image 483](<2013-bannai-spherical-designs-harmonic-index_images/imageFile483.png>)

s812 −

15469 931

![image 484](<2013-bannai-spherical-designs-harmonic-index_images/imageFile484.png>)

s612 +

2784 931

![image 485](<2013-bannai-spherical-designs-harmonic-index_images/imageFile485.png>)

s412 −

255 931

![image 486](<2013-bannai-spherical-designs-harmonic-index_images/imageFile486.png>)

s212 +

9 931

![image 487](<2013-bannai-spherical-designs-harmonic-index_images/imageFile487.png>)

,

- P16 = s1612 −


63765 17689

299970 123823

843138 866761

207090 866761

30375 866761

2430 866761

390 133

s1412 +

s1212 −

s1012 +

s812 −

s612 +

s412 −

s212

![image 488](<2013-bannai-spherical-designs-harmonic-index_images/imageFile488.png>)

![image 489](<2013-bannai-spherical-designs-harmonic-index_images/imageFile489.png>)

![image 490](<2013-bannai-spherical-designs-harmonic-index_images/imageFile490.png>)

![image 491](<2013-bannai-spherical-designs-harmonic-index_images/imageFile491.png>)

![image 492](<2013-bannai-spherical-designs-harmonic-index_images/imageFile492.png>)

![image 493](<2013-bannai-spherical-designs-harmonic-index_images/imageFile493.png>)

![image 494](<2013-bannai-spherical-designs-harmonic-index_images/imageFile494.png>)

81 866761

+

![image 495](<2013-bannai-spherical-designs-harmonic-index_images/imageFile495.png>)

References

- [1] G. Andrews, R. Askey and R. Roy, Special function, Encyclopedia of Mathematics and Its Applications, Cambridge University Press.1999.
- [2] Ei. Bannai and Et. Bannai, Algebraic Combinatorics on Spheres, (in Japanese) Springer Tokyo 1999.
- [3] Ei. Bannai and Et . Bannai, A survey on spherical designs and algebraic combinatorics on spheres, European J. Combin. 30 (2009), 1392–1425.
- [4] A. Brouwer and W. Haemers, Spectra of graphs, Universitext, Springer, New York, 2012.
- [5] A. Bondarenko, D. Radchenko and M. Viazovska, Optimal asymptotic bounds for spherical designs, Ann. of Math. 178 (2013), 1–10.
- [6] A. Bondarenko, D. Radchenko and M. Viazovska, Well separated spherical designs, preprint, 25 pp, arXiv:1303.5991.
- [7] P. Delsarte, An algebraic approach to the association schemes of coding theory, Philips Res. Rep. Suppl. 10 (1973).
- [8] P. Delsarte, J.M. Goethals, and J.J. Seidel, Spherical codes and designs, Geom. Dedicata 6

(1977), 363–388.

- [9] S.J. Einhorn, I.J. Schoenberg, On Euclidean sets having only two distances between points.

I. II, Nederl. Akad. Wetensch. Proc. Ser. A Indag. Math. 28 (1966) 479–488., 489–504.

- [10] A. Erdelyi et al., Higher Transcendental Function, Vol II, (Bateman Manuscript Project), MacGraw-Hill, 1953.
- [11] P. de la Harpe and C. Pache, Cubature formulas, geometrical designs, reproducing kernels, and Markov operators, Inﬁnite groups: geometric, combinatorial and dynamical aspects, Progr. Math., 248, Birkhauser, Basel, 2005, pp.,219–267.
- [12] Y. Hong, On spherical t-designs in Rn, European J. Combin. 3 (1982) 255–258.
- [13] D. G. Larman, C. A. Rogers, and J. J. Seidel, On two-distance sets in Euclidean space, Bull. London Math. Soc. 9 (1977), 26–267.
- [14] P. W. H. Lemmens and J. J. Seidel, Equiangular lines, J. Alg 24(1973) 494–512.
- [15] O. Musin, Spherical two-distance sets, J.Combin. Theory Ser. A 116(2009), no. 4, 988-995.
- [16] P. Seymour and T. Zaslavsky, Averaging sets: a generalization of mean values and spherical designs, Adv. in Math. 52 (1984), no. 3, 213–240.
- [17] G. Szego¨, Orthogonal Polynomials, 4th edition, Amer. Math. Soc., Colloquim Publications, volume 23 (2003).


Department of Mathematics, Shanghai Jiao Tong University, 800 Dongchuan RD.

Minhang District, Shanghai, China E-mail address: bannai@sjtu.edu.cn, bannai@math.kyushu-u.ac.jp Graduate School of Information Sciences, Tohoku University, Aramaki aza Aoba

6-3-09, Aoba-ku Sendai-city Miyagi-pref. 980-8579, Japan E-mail address: okuda@ims.is.tohoku.ac.jp Graduate School of Computer Science and Systems Engineering, Kyushu Institute

of Technology, 680-4 Kawazu, Iizuka-shi, Fukuoka, 820-8502, Japan E-mail address: tagami@ces.kyutech.ac.jp

