arXiv:1909.09909v3[math.MG]11Mar2022

Log–optimal (d + 2)-conﬁgurations in d–dimensions

Peter D. Dragnev and Oleg R. Musin

Abstract

We enumerate and classify all stationary logarithmic conﬁgurations of d + 2 points on the unit sphere in d–dimensions. In particular, we show that the logarithmic energy attains its local minima at conﬁgurations that consist of two orthogonal to each other regular simplexes of cardinality m and n. The global minimum occurs when m = n if d is even and m = n + 1 otherwise. This characterizes a new class of conﬁgurations that minimize the logarithmic energy on Sd−1 for all d. The other two classes known in the literature, the regular simplex (d+1 points on Sd−1) and the cross polytope (2d points on Sd−1), are both universally optimal conﬁgurations.

Keywords: Thomson’s problem, Riesz potential, logarithmic energy, optimal conﬁgurations Mathematics Subject Classiﬁcation: Primary 74G05, 74G65; Secondary 31B15, 31C15

# 1 Introduction and main result

Let X = {x1,... ,xN} be a set of distinct points (unit vectors) on the unit sphere Sd−1 in Rd. Conﬁgurations that minimize the logarithmic energy

Elog(X) :=

log

1≤i =j≤N

1 |xi − xj|

N(N − 1)ln 2 2

= −(1/2)

log(1 − xi · xj) −

, (1)

![image 1](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile1.png>)

![image 2](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile2.png>)

1≤i =j≤N

are called log-optimal. More generally, a conﬁguration is called h-optimal for a potential interaction

- h : [−1,1) → R, if it minimizes the h-energy


Eh(X) :=

h(xi · xj). (2)

1≤i =j≤N

The Newton potential (h(t) = (1 − t)−d/2+1), and more generally the Riesz potential (h(t) = (1 − t)−s/2) , as well as the Gaussian potential (h(t) = eαt, α > 0) have been well studied in the literature (see [14]). The logarithmic potential −log(1−t) is the limiting case of the Riesz potential as s → 0. All of these potentials are absolutely monotone potentials, i.e. h(k)(t) ≥ 0, for all k = 1,2,... . The regular simplex (N = d + 1) and the cross polytope (N = 2d) are the only known classes of conﬁgurations that minimize the logarithmic energy for all d; actually, they are universally optimal conﬁgurations, namely they minimize the energy for all absolutely monotone potentials h (see [3, Table 1]). Another (inﬁnite) class of universally optimal conﬁgurations is the so-called isotropic spaces, for which d = q(q2 + q + 1) and N = (q + 1)(q3 + 1), where q is a power of a prime number.

All other known optimal conﬁgurations in the literature, even when the interacting potential h is ﬁxed, have particular values of the dimension d and the cardinality N.

While the original problem of ﬁnding log-optimal conﬁgurations on the sphere, sometimes referred to as Whyte’s problem (see [19]), was posed in 1952, few advances have been made throughout the years. That the regular simplex is a log-optimal conﬁguration follows from the classical arithmetic-geometric mean inequality. Kolushev and Yudin [7], using analytic methods derived in 1997 that the cross-polytope (the 2d intersection points of the coordinate axes and the unit sphere) minimizes the logarithmic energy. In 1996 Andreev [1] proved that the regular icosahedron is a log-optimal conﬁguration. Subsequently, in 2007 Cohn and Kumar [3] showed all these to be universally optimal conﬁgurations (ones that minimize all absolutely monotone potentials). The ﬁrst non-universally optimal case of d + 2 points on Sd−1 for d = 3 was resolved in 2002 (see [4]) and the cases d = 4 and d = 5 were derived in 2016 (see [5]).

Note that all partial results have been focused on ﬁnding the global minima. The goal of this article somewhat more general, namely to classify all local minima for the logarithmic energy for the class of N = d + 2 points on Sd−1, d ≥ 2, and in particular, determine the log-optimal energy conﬁguration for this class. The following is our main theorem.

- Theorem 1.1. Up to orthogonal transform, every local minimum of the logarithmic energy Elog(X) of d + 2 points on Sd−1 consists of two regular simplexes of cardinality m ≥ n > 1, m + n = d + 2, such that these simplexes are orthogonal to each other. The global minimum occurs when m = n if d is even and m = n + 1 otherwise.


The theorem is derived following a careful analysis of non-degenerate stationary conﬁgurations. While inspired by [5], our approach in this article is new and allows us to establish much stronger necessary conditions for stationarity (see Theorems 2.1 and 2.4). As pointed in Remark 2.2, that the number of orthogonal simplexes in Theorem 2.1 is two, a byproduct of Theorem 3.3. For degenerate stationary conﬁgurations, Theorem 2.3 shows that the h-energy may be decreased whenever h is strictly convex potential function, including in the logarithmic case.

Note that for d even the log-optimal conﬁguration in Theorem 1.1 is a two-distance set (see [11] and references therein) that is the two-design introduced by Mimura [10]. We also draw the reader’s attention to a remarkable connection with the classiﬁcation of best packing conﬁgurations of d + k, 1 ≤ k ≤ d points on Sd−1 found by W. Kuperberg in [8]. In particular, his classiﬁcation implies that any best packing conﬁgurations of d+2 points will split into two orthogonal simplexes, not necessarily regular, but with minimal distance at least √2. It is easy to see that the local minima above minimize the logarithmic energy among such best packing conﬁgurations. Kuperbergtype theorems for two–distance sets are considered in [11]. We ﬁnally point out the connection with Steven Smale’s 7th problem [17] asking for generating in polynomial time nearly log-optimal conﬁgurations on S2 for large N.

![image 4](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile4.png>)

In the next section we classify the stationary conﬁgurations and deal with the cases that don’t lead to local minima. In Section 3 we introduce some auxiliary results utilized in Section 4 to prove the results about stationary conﬁgurations that are saddle points. The proof of the main theorem is presented in Section 5. In Section 6 we derive the Morse index for all stationary conﬁguration of ﬁve points on S2 and list some related open problems and future plans of research.

# 2 Stationary Conﬁgurations of d + 2 points on Sd−1

In this section we completely classify the stationary conﬁgurations of d +2 points on Sd−1. We call a conﬁguration X non-degenerate if span(X) = Rd and degenerate otherwise.

- Theorem 2.1. Let N = d + 2 and X = {x1,... ,xN} be a non-degenerate stationary logarithmic conﬁguration on Sd−1. Suppose there is no point x ∈ X that is equidistant to all other points in

- X. Then X can be split into two sets such that these sets are vertices of two regular orthogonal simplexes with the centers of mass in the center of Sd−1. Remark 2.2. This theorem strengthens signiﬁcantly the characterization theorem [5, Theorem


- 1.5], which asserts that a stationary conﬁguration is either degenerate; has a vertex equidistant to all others; or that every vertex has a mirror related partner, i.e. another vertex, such that the perpendicular bisector hyperplane of the segment formed by the two vertices contains all other points of the conﬁguration. The mirror relation as an equivalence relation splits the points in a non-degenerate stationary conﬁguration that has no vertex equidistant to all other vertices into equivalence classes that form regular simplexes. Theorem 2.1 states that these simplexes are only two. This along, together with [5, Lemma 3.2] implies the global minimum part of Theorem 1.1.

In the process of classifying all local minima for the energy, we need to eliminate the other cases. We ﬁrst consider degenerate stationary conﬁgurations. While there are such conﬁgurations that are global minimizers of energy among all conﬁgurations conﬁned to their spanning subspace (say a regular pentagon on the Equator of S2), the next theorem (a generalization of [5, Theorem

- 1.6]) shows that for any strictly convex potential function h, the h-energy (see (2)) of a degenerate conﬁguration with cardinality N ≥ d + 2 can be strictly decreased by a small perturbation, and hence may not be a local minimum.


- Theorem 2.3. Let X be a degenerate conﬁguration, N ≥ d + 2, and h : [−1,1] → R be a strictly convex potential function. Then there exists a continuous perturbation that decreases the h-energy Eh(X).

Next, we focus on conﬁgurations that are not degenerate, but have a vertex, say the North Pole xN, that is equidistant to all other vertices xj. We shall denote such conﬁgurations with {1,N −1}. Then the vertices {x1,... ,xN−1} are lying on a hyperplane in the Southern hyper-hemisphere at height −1/(N − 1). By projecting these vertices to the Equatorial hyperplane and normalizing to become unit vectors, we reduce the conﬁguration to d+1 points on Sd−2 that form a non-degenerate stationary (w.r.t logarithmic energy) conﬁguration. This conﬁguration may have a vertex that is equidistant to all others, we shall denote such a case as {1,1,N −2}. As for 4 points on S1 the only stationary conﬁguration is the two orthogonal simplexes split (diagonals of a square), this process will stop with two orthogonal simplexes case. The following theorem sheds light on this case.

- Theorem 2.4. A non-degenerate stationary log-energy conﬁguration of type {1,1,... ,k,l}, where 1 + 1 + ··· + k + l = d + 2 is a saddle point. Moreover, there is a continuous perturbation that decreases the logarithmic energy of the {1,k,l} part of the conﬁguration to either {k + 1,l} or {k,l + 1}. Subsequently, with a sequence of such perturbations, one can reach a local minimum as described in Theorem 1.1.


# 3 Auxiliary results

Utilizing Lagrange multipliers to the constrained minimization of (1) we show that for any stationary conﬁguration X the following vector equations (also referred to in the literature as force equations) hold true

xi − xj ri,j

= λixi i = 1,... ,N,

![image 7](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile7.png>)

j =i

where rij := 1 − xi · xj. Taking inner product of both sides with xi one obtains λi = N − 1,

- i = 1,... ,N. Therefore,


xi − xj ri,j

= (N − 1)xi, i = 1,... ,N. (3)

![image 8](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile8.png>)

j =i

Summing (3) implies that the centroid of a stationary conﬁguration X lies at the origin and that for all i = 1,... ,N we have

rij = N. (4)

j

Let

B = (bij), bij :=

1 rij

, bii := N − 1 −

bij,

![image 9](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile9.png>)

j =i

N − 1 N

.

A = (aij) , where aij := c − bij, c :=

![image 10](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile10.png>)

- Lemma 3.1. Let X = {x1,... ,xN} be a stationary logarithmic conﬁguration on Sd−1 that is non-degenerate (span(X) = Rd). Then

rank(A) ≤ N − d − 1,

N

j=1

aij = 0, i = 1,... ,N.

Proof. Let X := [x1,... ,xN]T. The force equations (3) imply that

N

j=1

bijxj = 0,

N

j=1

bij = N − 1.

In other words, BX = 0 and B1 = (N − 1)1, where 1 denotes the N-dimensional column-vector of ones. As X is non-degenerate, we have rank X = d. Therefore, the column-vectors of X are linearly independent. As 1 is eigenvector of B with an eigenvalue of N − 1 it is linearly independent to the columns of X (eigenvectors with eigenvalue 0). The lemma follows from the rank-nullity theorem applied to A[X,1] = 0.

![image 11](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile11.png>)

![image 12](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile12.png>)

![image 13](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile13.png>)

![image 14](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile14.png>)

The following lemma elaborates on the case when N = d + 2.

- Lemma 3.2. Let N = d + 2 and X = {x1,... ,xN} be a non-degenerate stationary logarithmic conﬁguration on Sd−1. Without loss of generality we may assume that a1i ≥ 0 for i = 1,... k and


- a1i < 0 for i = k + 1,... N. Let


√aii, i = k + 1,... N.

ai = √aii, i = 1,... k; ai = −

![image 15](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile15.png>)

![image 16](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile16.png>)

Then

aij = ai aj, a1 + ... + aN = 0, c − aiaj ≥

- 1

![image 18](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile18.png>)

- 2


, for all i = j,

1 c − aiaj

= N, i = 1,... ,N. (5)

![image 19](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile19.png>)

j =i

Proof. We ﬁrst observe that if N = d + 2, then rank(A) = 1. Indeed, rank(A) = 0 yields that all mutual distances are equal, which is impossible.

Since A is a symmetric matrix of rank 1, aij = ai aj for all i,j. Lemma 3.1 implies that for all

- i we have


aij = ai(a1 + ... + aN) = 0.

j

Since all ai cannot be 0, we have a1 + ... + aN = 0. By deﬁnitions we have aij = c − 1/rij, i.e.

1 c − aiaj

1 c − aij

=

, i = j.

rij =

![image 20](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile20.png>)

![image 21](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile21.png>)

Since rij ≤ 2, we have

- 1

![image 22](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile22.png>)

- 2


c − aiaj ≥

. It is easy to see that (4) implies (5).

![image 23](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile23.png>)

![image 24](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile24.png>)

![image 25](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile25.png>)

![image 26](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile26.png>)

Note that if ai = 0 then the i-th row and i-th column in the matrix A are zero. Therefore, xi is equidistant to all other points xj and

N N − 1

, j = 1,...,i − 1,i + 1,... ,N.

rij =

![image 27](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile27.png>)

Thus, if a conﬁguration has no point that is equidistant to all others, then ai = 0 for all i = 1,... ,N. The following theorem is the main in this section.

Theorem 3.3. Let a1,... ,aN be real numbers that satisfy the following assumptions a1 ≥ ... ≥ ak > 0 > ak+1 ≥ ... ≥ aN, a1 + ... ,+aN = 0,

1 c − aiaj

N − 1 N

= N, i = 1,... ,N, c − aiaj > 0, for all i = j, where c :=

.

![image 28](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile28.png>)

![image 29](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile29.png>)

j =i

Then

a1 = ... = ak, ak+1 = ... = aN. First we prove two technical Lemmas.

- Lemma 3.4. Suppose a1,... ,aN are as in Theorem 3.3. Then for all i = 1,... ,N we have


c − a2j c − aiaj

= N − 2. (6)

Ti :=

![image 30](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile30.png>)

j =i

Proof. Let

1 c − aiaj

.

Qi :=

![image 32](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile32.png>)

j =i

Then by the assumption Qi = N for all i. Let

aj c − aiaj

.

Ri :=

![image 33](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile33.png>)

j =i

Since ai = 0, we obtain from N − 1 =

c − aiaj c − aiaj

= cQi − aiRi = N − 1 − aiRi,

![image 34](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile34.png>)

j =i

that Ri = 0. Along with ai = −(a1 + ... + ai−1 + ai+1 + ...aN) we derive the following equality

a2j − ajai c − aiaj

aj c − aiaj −

ai = (c − a2i)

.

aj = ai

![image 35](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile35.png>)

![image 36](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile36.png>)

j =i

j =i

j =i

As ai = 0 this yields

and subsequently

N − 2 =

a2j − ajai c − aiaj

Si :=

= 1, (7)

![image 37](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile37.png>)

j =i

c − aiaj c − aiaj − Si =

![image 38](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile38.png>)

j =i

c − a2j c − aiaj

= Ti

![image 39](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile39.png>)

j =i

![image 40](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile40.png>)

![image 41](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile41.png>)

![image 42](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile42.png>)

![image 43](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile43.png>)

- Lemma 3.5. Suppose a1,... ,aN are as in Theorem 3.3. Then |ai| < √c, i = 1,...,N.


![image 44](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile44.png>)

Proof. Let i > 1. By (7) we have

Then

Therefore,

a2j − aiaj c − aiaj

=

1 =

![image 45](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile45.png>)

j =i

a21 − aia1 c − aia1

![image 46](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile46.png>)

a2j − aiaj c − aiaj

+

.

![image 47](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile47.png>)

2≤j =i

a2j − aiaj c − aiaj

=

![image 48](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile48.png>)

2≤j =i

c − a21 c − aia1

, i = 2,... ,N.

![image 49](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile49.png>)

N

a2j − aiaj c − aiaj

=

![image 50](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile50.png>)

i=2 2≤j =i

N

N

(ai − aj)2 c − aiaj

= (c − a21)

![image 51](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile51.png>)

i>j=2

i=2

1 c − aia1

= (c − a21)Q1.

![image 52](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile52.png>)

Since Q1 = N and by the assumption c − aiaj > 0, we have

c − a21 =

N

(ai − aj)2 c − aiaj

1 N

![image 54](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile54.png>)

![image 55](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile55.png>)

i>j=2

> 0. (8)

We may assume that |a1| ≥ |ai| for all i. Thus, (8) implies that c − a2i > 0. Proof of Theorem 3.3: Let

N

c − a2j c − taj

F(t) :=

.

![image 56](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile56.png>)

j=1

Then Lemma 3.4 implies that for all i = 1,... ,N

![image 57](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile57.png>)

![image 58](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile58.png>)

![image 59](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile59.png>)

![image 60](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile60.png>)

F(ai) = N − 1. (9) Since

c − a2j a2j (c − taj)3

F′′(t) = 2

,

![image 61](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile61.png>)

j

√c,√c). Hence F(t) is a convex function in this interval. Therefore, the equation F(t) = N − 1 has at most two solutions. By assumptions we have ai > 0

by Lemma 3.5 we have F′′(t) > 0 for t ∈ (−

![image 62](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile62.png>)

![image 63](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile63.png>)

- for i = 1,... ,k and ai < 0, for i = k + 1,... ,N. Thus, (9) yields that all positive ai are equal and all negative ai are equal too.


- 4 Stationary Conﬁgurations - Proofs We are now in a position to prove the classiﬁcation result Theorem 2.1.


Proof of Theorem 2.1: As there is no point that is equidistant from all others we have ai = 0 for all i = 1,... ,N Theorem 3.3 yields

a := a1 = ... = ak > 0 > ak+1 = ... = aN =: b, where ka + (N − k)b = 0. As

a(x1 + ··· + xk) + b(xk+1 + ··· + xN) = 0 and x1 + ··· + xN = 0, we obtain that x1 + ··· + xk = 0 = xk+1 + ··· + xN. Moreover, using (7) we easily obtain that

- a2 = (N − k)/(kN), b2 = k/((N − k)N), and ab = −1/N. This yields that xi · xj = −1/(k − 1) for 1 ≤ i < j ≤ k, xi·xj = −1/(N −k−1) for k+1 ≤ i < j ≤ N, and xi·xj = 0 for 1 ≤ i ≤ k < j ≤ N. This proves the theorem.


We next derive that degenerate stationary conﬁgurations may not be local minima of the henergy for convex potential interaction h.

We shall ﬁrst introduce the following lemma.

- Lemma 4.1. Let h : [−1,1] → R be a strictly convex function and let a,b ∈ R be such that |a| + |b| ≤ 1, b = 0. Then the function


F(t) := h(a + bt) + h(a − bt) is strictly decreasing for t ∈ [−1,0] and strictly increasing for t ∈ [0,1]. Proof. Since F(t) is even, we consider only t ∈ [0,1]. Let 0 ≤ t1 < t2 ≤ 1. Deﬁne

t2 − t1 2t2

t1 + t2 2t2

, β :=

.

α :=

![image 65](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile65.png>)

![image 66](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile66.png>)

Clearly, α,β > 0 and α + β = 1. Observe that

a + bt1 = α(a + bt2) + β(a − bt2), a − bt1 = β(a + bt2) + α(a − bt2). Using the strict convexity of h and that a + bt2 = a − bt2 (b = 0) we obtain

h(a + bt1) < αh(a + bt2) + βh(a − bt2), h(a − bt1) < βh(a + bt2) + αh(a − bt2) (10) Adding the two inequalities in (10) we derive the lemma.

![image 67](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile67.png>)

![image 68](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile68.png>)

![image 69](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile69.png>)

![image 70](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile70.png>)

- Proof of Theorem 2.3: As X is degenerate, we may assume without loss of generality that the Equatorial hyperplane contains X, or X ⊂ {xd = 0}. Since N ≥ d + 2, X is not a regular simplex and therefore there are at least two adjacent edges of distinct length, say |x3 − x1| = |x3 − x2|, or equivalently x1 · x3 = x2 · x3. Without loss of generality assume

x1 = (r, 1 − r2,0,... ,0),x2 = (r,− 1 − r2,0,... ,0),xj = (cj1,cj2,cj3,... ,0), j = 3,... ,N, where at least c32 = 0. Form the conﬁguration X with the ﬁrst two points perturbed

![image 71](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile71.png>)

![image 72](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile72.png>)

x˜1 = (r, 1 − r2 cos θ,0,... , 1 − r2 sin θ),x˜2 = (r,− 1 − r2 cos θ,0,... ,− 1 − r2 sin θ). Observe that

![image 73](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile73.png>)

![image 74](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile74.png>)

![image 75](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile75.png>)

![image 76](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile76.png>)

x˜1 · xj = cj1r + cj2 1 − r2 cosθ, x˜2 · xj = cj1r − cj2 1 − r2 cos θ.

![image 77](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile77.png>)

![image 78](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile78.png>)

We now apply Lemma 4.1 with a = cj,1r, b = cj2√1 − r2, and t = cos θ to conclude that for all j such that cj2 = 0 (this is not empty as c32 = 0)

![image 79](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile79.png>)

h(˜x1 · xj) + h(˜x2 · xj) < h(x1 · xj) + h(x2 · xj).

Obviously if cj2 = 0 we have equality in the above inequality. This implies that Eh( X) < Eh(X) for all 0 < θ < π.

- Proof of Theorem 2.4 : Theorem 2.1 shows that non-degenerate stationary conﬁguration X must


either split into two orthogonal regular simplexes X = Xm ∪ Xn with m + n = d + 2, or have a vertex that is equidistant to all other vertices. The ﬁrst case will be dealt with in Section 5.

Suppose that the second case holds. As in the discussion before the formulation of the theorem, suppose xN · xi = −1/(N − 1) for all i = 1,... ,N − 1. For all i = 1,... ,N − 1 denote xi = (yi,−1/(N − 1)) and let zi := (N − 1)yi/ N(N − 2). Then {zi}iN=1−1 ⊂ Sd−2 satisfy similar force equations as (3).

![image 81](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile81.png>)

As {xi} is non-degenerate, so is {zi}. Thus, we have reduced the problem’s dimension. The process will stop and at the last step we shall obtain two orthogonal simplexes.

So, without loss of generality we may assume the process has stopped after one step, namely we

have a conﬁguration of the type {1,k,m}, where one of the points p := (0k−1,0m−1,1) is equidistant to all others, and these other points form two regular orthogonal simplexes

![image 82](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile82.png>)

![image 83](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile83.png>)

- Y := {( 1 − 1/(k + m)2 yi,0m−1,−1/(k + m))}, Z := {(0k−1, 1 − 1/(k + m)2 zj,−1/(k + m))}


with k and m points respectively (here 1 + k + m = d + 2). We perturb the conﬁguration X := {p,Y,Z} to Xt := {p, Yt, Zt}, where

k i=1

![image 84](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile84.png>)

Yt = 1 − (mt + 1/(k + m))2 yi,0m−1,−1/(k + m) − mt

and

m j=1

![image 85](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile85.png>)

Zt = 0k−1, 1 − (kt − 1/(k + m))2 zj,−1/(k + m) + kt

. The logarithmic energy of the perturbed conﬁguration as a function of t is given by

k(k − 1) 2

k k − 1

k(k + 1) 2

1 1 + k+1m + mt

1 1 − k+1m − mt ·

+

Elog(Xt) =

log

log

![image 86](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile86.png>)

![image 87](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile87.png>)

![image 88](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile88.png>)

![image 89](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile89.png>)

![image 90](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile90.png>)

![image 91](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile91.png>)

![image 92](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile92.png>)

1 1 + k+1m − kt

1 1 − k+1m + kt ·

m(m − 1) 2

m m − 1

m(m + 1) 2

log

log

+

+

![image 93](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile93.png>)

![image 94](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile94.png>)

![image 95](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile95.png>)

![image 96](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile96.png>)

![image 97](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile97.png>)

![image 98](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile98.png>)

![image 99](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile99.png>)

1 1 − (k+1m + mt)(k+1m − kt)

+ kmlog

=: f(t)

![image 100](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile100.png>)

![image 101](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile101.png>)

![image 102](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile102.png>)

(11)

The derivative can be computed as

  

  . (12)

km(m + k)t(mt + k+1m)(kt − k+1m) 1 − (k+1m + mt)(k+1m − kt)

m 1 − k+ 1m + mt

k 1 − k+ 1m − kt

![image 103](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile103.png>)

![image 104](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile104.png>)

f′(t) =

2 +

![image 105](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile105.png>)

![image 106](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile106.png>)

![image 107](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile107.png>)

2

![image 108](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile108.png>)

![image 109](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile109.png>)

![image 110](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile110.png>)

![image 111](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile111.png>)

Observe that the denominator of the ﬁrst fraction and the expression in the brackets are positive as Xt ⊂ Sd−1. Therefore,

1 k + m

1 k + m

sign f′(t) = sign t mt +

kt −

.

![image 112](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile112.png>)

![image 113](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile113.png>)

Thus, we observe that for t ∈ [−1/m(k +m),0] the logarithmic energy is strictly increasing and for t ∈ [0,1/k(k + m)] it is strictly decreasing, thus being maximal when t = 0. This shows that {1,k,m} is not a local minimum and we can make a continuous perturbation that decreases the

energy from t = 0 to t = −1/m(k + m), which corresponds to a {k,m + 1} conﬁguration of two orthogonal simplexes, or to t = 1/k(k + m), which corresponds to a {k + 1,m} conﬁguration.

Of course, should we consider one of the simplexes, say Y , ﬁxed and vary the other one within the hyperplne in which it is embedded (which is equivalent to let zj vary), then the maximum is attained when Z is regular. Therefore, this is a case of a saddle point for the logarithmic energy.

# 5 Local Minima - Proof of the Main Result The proof of Theorem 1.1 utilizes the following two lemmas.

- Lemma 5.1. Let A = (aij) be an m × m matrix, m ≥ 3, such that (a) aii = 0, i = 1,... ,m; and (b) mj=1 aij = 0. Then the following inequality holds


1 m − 2

(aij + aji)2 ≥

![image 115](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile115.png>)

1≤i<j≤m

Proof. For all i,j = 1,... ,m deﬁne

m

x2j, where xj :=

j=1

m

aij. (13)

i=1

1 m2 − 2m

m − 1 m2 − 2m

βij :=

xi +

xj, i = j, and βii = 0.

![image 116](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile116.png>)

![image 117](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile117.png>)

Since mj=1 xj = 0, we have mj=1 βij = 0 and mi=1 βij = xj, i.e.

m

m

aij and

βij =

j=1

j=1

m

m

aij.

βij =

i=1

i=1

Let aij := aij − βij. Then

i

aij =

j

aij = 0.

Consider tij := aij + aji = wij + βij + βji, where wij = aij + aji. Then tij = wij + mx−i2 + mx−j2,

![image 118](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile118.png>)

![image 119](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile119.png>)

- i = j, where i wij = j wij = 0 (observe that tii = 0). Then


t2ij =

i<j

i<j

which implies (13).

xi m − 2

+

wij +

![image 120](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile120.png>)

xj m − 2

![image 121](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile121.png>)

m

2

1 m − 2

wij2 +

x2i ,

=

![image 122](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile122.png>)

i<j

i=1

![image 123](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile123.png>)

![image 124](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile124.png>)

![image 125](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile125.png>)

![image 126](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile126.png>)

Lemma 5.2. Given an m × n matrix F = (fij) and an n × m matrix G = (gij) such that n j=1 fij = 0 for all i = 1,... ,m and mj=1 gij = 0 for all i = 1,... ,n. Then we have

m

n

(fij + gji)2 ≥

j=1

i=1

n

1 m

![image 127](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile127.png>)

j=1

1 n

yj2 +

![image 128](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile128.png>)

m

zi2, where yj :=

i=1

m

fij,zi :=

i=1

n

gji. (14)

j=1

Proof. Let

yj m

fij := fij −

![image 130](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile130.png>)

zi n

and gij := gij −

.

![image 131](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile131.png>)

Since j yj = i zi = 0, we have i,j( fij + gji) = 0. Let tij := fij + gji. Observe that

n

m

tij = 0.

tij =

j=1

i=1

From

yj m

zi n

fij + gji =

+ tij. one derives that

+

![image 132](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile132.png>)

![image 133](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile133.png>)

m

m

n

n

(fij + gji)2 =

i=1

i=1

j=1

j=1

yj m

zi n

+

+ tij

![image 134](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile134.png>)

![image 135](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile135.png>)

m

n

1 m

2

t2ij +

=

![image 136](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile136.png>)

i=1

j=1

n

1 n

yj2 +

![image 137](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile137.png>)

j=1

m

zi2,

i=1

which completes the proof. Proof of Theorem 1.1 : Denote the two regular orthogonal simplexes, whose centers of mass are both in the origin with

![image 138](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile138.png>)

![image 139](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile139.png>)

![image 140](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile140.png>)

![image 141](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile141.png>)

Xm = {x1,x2,... ,xm}, Xn = {xm+1,xm+2,... ,xm+n}.

Let ǫ > 0 be a positive number and let us perturb the points of the simplexes to yi ∈ Sd−1, yi := xi + hi, where hi < ǫ, i = 1,... d + 2. Denote the new conﬁguration Y = Ym ∪ Yn. Since

xi = yi = 1, we have 2xi · hi = − hi 2. We also have 1 − yi · yj = (1 − xi · xj)(1 − zi,j), where



m − 1

![image 142](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile142.png>)

- m

(xi · hj + xj · hi + hi · hj), 1 ≤ i = j ≤ m

xi · hj + xj · hi + hi · hj, i ≤ m < j or j ≤ m < i

- n − 1




(15)

zi,j :=



(xi · hj + xj · hi + hi · hj), m < i = j ≤ m + n.

![image 143](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile143.png>)

n

Clearly |zi,j| < 2ǫ + O(ǫ2). The deﬁnition of the logarithmic energy (1) implies that

zi,j2 2

+ O(ǫ3). (16)

2[Elog(Y ) − Elog(X)] = −

log(1 − zi,j) =

zi,j +

![image 144](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile144.png>)

1≤i =j≤m+n

1≤i =j≤m+n

Excluding O(ǫ3) terms from (16) the remainder is

- 1

![image 145](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile145.png>)

- 2 1≤i =j≤m+n


D :=

zi,j +

1≤i =j≤m+n

xi · hj + xj · hi 1 − x·xj

![image 146](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile146.png>)

2

.

To compute D, without loss of generality we may assume that xi = (pi,0), hi = (ai,bi), i = 1,... ,m and xm+j = (0,qj), hm+j = (cj,dj), j = 1,... ,n, where pi,ai,cj ∈ Rm−1 and qj,bi,dj ∈ Rn−1. Application of 2xi · hi = − hi 2 yields

m

m

m

m

1 m

2(m − 1) m

2

2

−

hi

hi +

xi

.

hi

zi,j =

![image 148](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile148.png>)

![image 149](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile149.png>)

i=1

i=1

i=1

i=1

1≤i =j≤m

As the origin is the center of mass of Xm we have

zi,j =

1≤i =j≤m

m

hi

i=1

1 m

2

−

![image 150](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile150.png>)

m

ai

i=1

2

Similarly,

and

zi,j =

m+1≤i =j≤m+n

m+n

hj

j=m+1

m+n

m

zi,j =

j=m+1

i=1

 

1 n

2

−

![image 151](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile151.png>)

m

hi ·

i=1

n

cj

j=1

m+n

i=m+1

This simpliﬁes to

 

m+n

m

m

1 m

1 n

2

2

2

−

hi

D =

−

bi

+

ai

![image 152](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile152.png>)

![image 153](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile153.png>)

i=1

i=1

i=1

2

m − 1 m

n − 1 n

(pi · aj + pj · ai)2 +

+

![image 154](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile154.png>)

![image 155](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile155.png>)

1≤i<j≤m

m

n

(pi · cj + qj · bi)2.

+

i=1

j=1

+

m

bi

i=1

2

.

2

+

n

dj

j=1

 ,

2

hj ,

 

n

n

2

2

dj

+

cj

j=1

j=1

2

(qi · dj + qj · di)2 (17)

1≤i<j≤n

Thus, in this case we shall reduce the theorem to proving the inequalities

D1 :=

m − 1 m

![image 156](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile156.png>)

2

1 m

(pi · aj + pj · ai)2 −

![image 157](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile157.png>)

1≤i<j≤m

m

ai

i=1

2

≥ 0 (18)

and

D2 :=

n − 1 n

![image 158](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile158.png>)

2

1 n

(qi · dj + qj · di)2 −

![image 159](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile159.png>)

1≤i<j≤n

n

j=1

m

D3 :=

i=1

n

1 m

(pi · cj + qj · bi)2 −

![image 160](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile160.png>)

j=1

m

1 n

bi 2 −

![image 161](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile161.png>)

i=1

dj

n

cj

j=1

2

≥ 0 (19)

2

≥ 0. (20)

If we denote hi := hi − (xi · hi) xi, i = 1,... ,m + n, then xi · hi = 0. Since 2xi · hi = − hi 2, we respectively have ai = ai + O(ǫ2)pi, bi = bi, for i = 1,... ,m, and cj = cj and dj = dj + O(ǫ2)qj

- for j = 1,... ,n. Therefore, by adding additional O(ǫ3) terms to (16), it suﬃces to prove (18) and


(19) under the additional assumption that pi · ai = 0 and qj · dj = 0.

To prove the inequalities we embed the ﬁrst simplex Xm = {p1,... ,pm} in the hyperplane of Rm that is orthogonal to (1,1,... ,1). Similarly, we embed the second simplex Xn = {q1,... ,qn} in Rn. Thus, we embed Xm ∪Xn ⊂ Rm×Rn. Denote wm = (m1 , m1 ,... , m1 ) ∈ Rm and let pi := ei −wm, i = 1,... ,m. Then pi = mm−1 pi. Similarly, if qj := ej − wn, then qj = n−n1 qj. For the perturbation vectors ai = (ai1,ai2,... ,aim), bi = (bi1,bi2,... ,bin), cj = (cj1,cj2,... ,cjm), dj = (bj1,bj2,... ,bjn), we will have that mj=1 aij = 0, nj=1 bij = 0, i = 1,... ,m, and mj=1 cij = 0, nj=1 dij = 0, i = 1,... ,n. The conditions pi · ai = 0 and qj · dj = 0 imply that aii = 0 for all i = 1,... ,m and djj = 0 for all j = 1,... ,n.

![image 163](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile163.png>)

![image 164](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile164.png>)

![image 165](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile165.png>)

![image 166](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile166.png>)

![image 167](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile167.png>)

![image 168](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile168.png>)

![image 169](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile169.png>)

Using that pi · aj = aji we can re-write (18) as

2

m

m

1 m − 1

(aij + aji)2 ≥

aij

,

![image 170](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile170.png>)

i=1

j=1

1≤i<j≤m

which follows from the stronger inequality (13) in Lemma 5.1. Observe that equality holds in (18) and (19) if and only aij+aji = 0 and dij+dji = 0 respectively, which is equivalent to pi·aj+pj·ai = 0, qj · di + qi · dj = 0, ai = 0, and dj = 0.

In a similar manner we shall utilize Lemma 5.2 to derive the inequality (20). We have that

![image 171](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile171.png>)

![image 172](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile172.png>)

m m − 1

n n − 1

cji +

bij

pi · cj + qj · bi =

![image 173](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile173.png>)

![image 174](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile174.png>)

![image 175](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile175.png>)

![image 176](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile176.png>)

with the substitution fij = n−n1bij and gji = mm−1cji we re-write (20) as

![image 177](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile177.png>)

![image 178](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile178.png>)

m

n

n

1

- m
- n − 1 n


(fij + gij)2 ≥

![image 179](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile179.png>)

![image 180](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile180.png>)

j=1

i=1

j=1

yj2 +

m

1 n

m − 1 m

zi2,

![image 181](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile181.png>)

![image 182](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile182.png>)

i=1

which clearly follows from (14). Moreover, equality occurs if and only if pi ·cj +qj ·bi = 0, ci = 0, and bj = 0.

To summarize, the quadratic term in ǫ will be strictly positive, and hence Elog(Y )−Elog(X) > 0, for any perturbation vectors {ai,bi,ci,di} (pi · ai = 0, qj · dj = 0), except when

pi · aj + pj · ai = 0, qj · di + qi · dj = 0, pi · cj + qj · bi = 0, and m

n

n

m

dj = 0.

ci = 0,

bi = 0,

ai = 0,

j=1

j=1

i=1

i=1

Utilizing (15) and these conditions, one simpliﬁes (16) to

(n − 1)2 2n2 1≤i =j≤n

(m − 1)2 2m2 1≤i =j≤m

(ai · aj)2 +

(di · dj)2

2[Elog(Y ) − Elog(X)] =

![image 183](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile183.png>)

![image 184](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile184.png>)

m

n

(bi · cj)2 + O(ǫ5).

+

i=1

j=1

Clearly, the quartic term will be positive, unless all inner products vanish, in which case we easily derive that ai = cj = 0 and bi = dj = 0 for all i = 1,... ,m and j = 1,... ,n. This completes the proof.

# 6 Concluding remarks and open problems

- 6.1 Morse theory of (d + 2)-conﬁgurations in d–dimensions Let Conf(d,N) denote the conﬁguration space of N–tuples of points in Sd−1 up to isometry. Then


Conf(d,N) = (Sd−1 × ... × Sd−1)/SO(d) and the dimension of this space is

d(d − 1) 2

. In particular,

dimConf(d,N) = (d − 1)N −

![image 186](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile186.png>)

(d + 2)(d − 1) 2

dimConf(d,d + 2) =

, dimConf(3,5) = 7.

![image 187](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile187.png>)

The Morse index of a critical point x of a smooth function f on a manifold M is equal, by deﬁnition, to the negative index of inertia of the Hessian of f at x.

By the above results we have a classiﬁcation of all critical (stationary) points of Elog on Conf(d,d + 2). In particular, if d = 3 then we have only three types of critical points: C0 of type (0,5), C1 of type (1,2,2) and C2 of type (2,3).

- Theorem 6.1. The Morse index of Elog on Conf(3,5) at Ci, i = 0,1,2, is 2 − i. Proof. Denote by µ(x) the Morse index of Elog on Conf(3,5) at x. Since Elog has at C2 a minimum,


µ(C2) = 0. Let x,y ∈ S2 with spherical coordinates (φ,θ) and (φ′,θ′). Then [x − y|2 = 2 − 2(sin θ sin θ′ cos(φ − φ′) + cos θ cos θ′). (21)

Consider X = {x1,...,x5} ⊂ S2 with spherical coordinates {(φ1,θ1),...,(φ5,θ5)} as a point in Conf(3,5). Without loss of generality we can assume that φ1 = θ1 = φ2 = 0. Then

v = v(X) := (θ2,φ3,θ3,φ4,θ4,φ5,θ5)

is a vector of seven variables that uniquely deﬁned a point in the conﬁguration space Conf(3,5). It is not hard to show that

v(C0) = (2π/5,0,4π/5,π,4π/5,π, 2π/5), v(C1) = (w,π/2,w,π,w,3π/2, w), w := arccos(−1/4).

Using (21) we can represent Elog(X) as a function f(v). Then the Hessian H(v) of f(v) and its eigenvalues at v(C0) and v(C1) can be found by direct calculations. These calculations show that

µ(C0) = 2, µ(C1) = 1.

![image 188](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile188.png>)

![image 189](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile189.png>)

![image 190](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile190.png>)

![image 191](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile191.png>)

It is an interesting problem: Find the Morse indexes of all critical points of Elog on Conf(d,d + 2) for all d.

## 6.2 Extensions of the main theorems for other potentials

It is of interest to determine other potentials for which we are able to characterize the optimal d + 2-point conﬁgurations on Sd−1.

(a) Riesz potentials: It is an interesting open problem to ﬁnd all critical conﬁgurations of the energy Eh on Conf(3,5) for Riesz potential interaction h(t) = (1 − t)−s/2 (see [2, Section 2.5] for details). Even in this simple case of ﬁve points on S2, rigorous results are limited. Here we have two competing conﬁgurations: the triangular bi-pyramid (TBP) consisting of one point at the north pole, one at the south pole, and three arranged in an equilateral triangle around the equator; and the regular four-pyramid (FP) with square base and varying height on the parameter s.

For s = 0 it is shown in [4] that TBP is the unique up to rotations minimizer of Elog. Utilizing computer aided proofs the optimality of TBP is established for s = −1 in [6] and for s = 1,2 in [15], which was recently extended [16] to show that there is a constant s∗ ≈ 15.048081 (conjectured in [9]), such that the TBP is the global minimizer for s ≤ s∗, and for s∗ ≤ s < 15 + 51225 the FP is the global minimizer.

![image 193](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile193.png>)

The determination of d + 2 points on Sd−1 with minimal Riesz energy is an interesting open problem, even for d = 4 and particular values of s, say the Newton potential interaction case s = 2. We expect similar transition value s∗(d) so that for 0 ≤ s ≤ s∗(d) the optimal conﬁguration will be the conﬁguration consisting of two orthogonal simplexes of minimal cardinality diﬀerence.

(b) Bi-quadratic potential energy: In [18] it was shown that the TBP is the unique up to rotations optimal spherical conﬁguration of ﬁve points on S2 for the bi-quadratic potential

h(xi · xj) = a(xi · xj)2 + b(xi · xj) + c, a > 0, b > 2a. We expect that our results will extend to bi-quadratic potentials and d + 2 points on Sd−1 and

intend to return to this problem in the near future. (c) Optimal 1–designs of cardinality d + 2 in d–dimensions: Since log-optimal stationary conﬁgurations X have their centroid at the origin, It is of interest to minimize various energies among the class of conﬁgurations that are 1-designs, i.e. x1+...+xN = 0, also called balanced conﬁgurations. Minimizing energy over balanced conﬁgurations is an interesting problem that has physical meaning, we intend to return to it in the near future as well.

(d) SDP bounds for optimal conﬁgurations: Recently, in [12] have been obtained new SDP bounds for distance distribution and distance

graphs of spherical codes. It is an interesting problem to extend these bounds for optimal conﬁgurations.

## 6.3 Optimal (d + k)-conﬁgurations in d–dimensions

Now we consider X ⊂ Sd−1 with d+2 ≤ |X| ≤ 2d. Rankin’s theorem states that if X is a subset of Sd−1 with |X| ≥ d+2, then the minimum distance between points in X is at most √2. For the case |X| = 2d Rankin proved that X is a regular cross–polytope. Wlodzimierz Kuperberg [8] extended Rankin’s theorem.

![image 194](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile194.png>)

Kuperberg’s theorem: Let X be a (d + k)–point subset of Sd−1 with 2 ≤ k ≤ d such that the minimum distance between points is at least √2. Then Rd splits into the orthogonal product

![image 195](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile195.png>)

k i=1 Li of nondegenerate linear subspaces Li such that for Si := X ∩ Li we have |Si| = di + 1 and

rank(Si) = di (i = 1,2,...,k), where di := dimLi. The following theorem is equivalent to [13, Theorem 4.2].

- Theorem 6.2. Let h : [−1,1) → R be a convex monotone increasing function. Let X be a subset of Sd−1 of cardinality d + k with 2 ≤ k ≤ d such that the minimum distance between distinct points in X is at least √2. Then the set of all local minima of Eh (see (2) in Sect. 1) consists of k orthogonal to each other regular di–simplexes Si such that all di ≥ 1 and d1 + ... + dk = d.


![image 197](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile197.png>)

Actually, this theorem easily follows from the optimality of simplices ([13, Theorem 4.1]) and Kuperberg’s theorem.

Let h(t) := −log(1 − t). If k = 2, then Theorem 1.1 yields Theorem 6.2. Moreover, we don’t need the assumption that for all x,y ∈ X with x = y we have |x − y| ≥

√2. For the case k = d it is proven by [7] that Log–optimal X is a regular cross–polytope.

![image 198](<2019-dragnev-log-optimal-configurations-d-dimensions_images/imageFile198.png>)

It is an interesting open problem to extend Theorem 1.1 for 2 < k ≤ d. Our conjecture is that for all k such that 2 ≤ k ≤ d we have the same result as in Theorem 6.2.

Acknowledgment. This paper is based upon work supported by the National Science Foundation under Grant No. DMS-1439786 while the authors were in residence at the Institute for Computational and Experimental Research in Mathematics in Providence, RI, during the Spring 2018 semester. The research of the ﬁrst author was supported, in part, by a Simons Foundation grant no. 282207, and in part, by the U. S. National Science Foundation under grant DMS-1936543.

# References

- [1] N. N. Andreev, An extremal property of the icosahedron, East J. Approx. 2 (1996), 459–462.
- [2] S.Borodachov, D. Hardin, E. Saﬀ, Discrete Energy on Rectiﬁable Sets, Springer Monographs in Mathematics, Springer (2019), DOI: 10.1007/978-0-387-84808-2
- [3] H.Cohn, A. Kumar, Universally optimal distribution of points on spheres, J. of AMS 20 (2007), 99–148.
- [4] P. D. Dragnev, D. A. Legg, and D. W. Townsend, Discrete logarithmic energy on the sphere, Paciﬁc J. Math. 207 (2002), 345–357.
- [5] P. D. Dragnev, Log-optimal conﬁgurations on the sphere, Contemporary Mathematics, AMS 661, (2016), 41–55.
- [6] X. Hou, J. Shao, Spherical Distribution of 5 Points with Maximal Distance Sum, Discr. Comp. Geom. 46 (2011), 156–174.
- [7] A. V. Kolushov and V. A. Yudin, Extremal dispositions of points on the sphere, Anal. Math. 23 (1997), 25–34.
- [8] W. Kuperberg, Optimal Arrangements in Packing Congruent Balls in a Spherical Container, Discr. Comput. Geometry 37 (2007), 205–212.


- [9] T. W. Melnik, O. Knop, and W. R. Smith, Extremal arrangements of points and unit charges on a sphere: equilibrium conﬁgurations revised, Can. J. Chem., 55 (1977), 1745–1761.
- [10] Y.Mimura. A construction of spherical 2-designs, Graphs Combin. 6, (1990), 369–372.
- [11] O. R. Musin, Graphs and spherical two-distance sets, Euro. J. Combin., 80 (2019), 311–325.
- [12] O. R. Musin, An extension the semideﬁnite programming bound for spherical codes, preprint, arXiv:1903.05767, 2019
- [13] O. R. Musin, Majorization and minimal energy on spheres, SIAM Journal on Discrete Mathematics, 35:3 (2021), 1578–1591.
- [14] E. B. Saﬀ and A. B. J. Kuijlaars, Distributing many points on a sphere, Math. Intelligencer 19 (1997), 5–11.
- [15] R. Schwartz, The ﬁve-electron case of Thomson’s problem, Exp. Math. 22 (2013), 157–186.
- [16] R. Schwartz, Five Point Energy Minimization: A Synopsis, Constr. Approx., 51 (2020), 537– 564.
- [17] S. Smale, Mathematical problems for the next century, in Arnold, V. I.; Atiyah, M.; Lax, P.; Mazur, B. Mathematics: frontiers and perspectives, AMS (1999), 271–294. ISBN 0821820702.
- [18] A. Tumanov, Minimal biquadratic energy of ﬁve particles on a 2-sphere, Indiana Univ. Math. J. 62 (2013), 1717–1731.
- [19] L. L. Whyte, Unique arrangements of points on a sphere, Amer. Math. Monthly 59 (1952), 606–611.


P. D. Dragnev, Purdue University Fort Wayne, Department of Mathematical Sciences, Fort

Wayne, IN 46805, USA E-mail address: dragnevp@pfw.edu O. R. Musin, University of Texas Rio Grande Valley, School of Mathematical and Statistical

Sciences, One West University Boulevard, Brownsville, TX 78520, USA &

E-mail address: oleg.musin@utrgv.edu

