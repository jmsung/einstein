---
type: source
kind: paper
title: Rationality of the inner products of spherical $s$-distance $t$-designs for $t \geq 2s-2$, $s \geq 3$
authors: Peter Boyvalenkov, Hiroshi Nozaki, Navid Safaei
year: 2022
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2204.00261v1
source_local: ../raw/2022-boyvalenkov-rationality-inner-products-spherical.pdf
topic: general-knowledge
cites:
---

arXiv:2204.00261v1[math.CO]1Apr2022

RATIONALITY OF THE INNER PRODUCTS OF SPHERICAL s-DISTANCE t-DESIGNS FOR t ≥ 2s − 2, s ≥ 3

PETER BOYVALENKOV†, HIROSHI NOZAKI‡, AND NAVID SAFAEI∗

Abstract. We prove that the inner products of spherical s-distance t-designs with t ≥ 2s − 2 (Delsarte codes) and s ≥ 3 are rational with the only exception being the icosahedron. In other formulations, we prove that all sharp conﬁgurations have rational inner products and all spherical codes which attain the Levenshtein bound, have rational inner products, except for the icosahedron.

Keywords. Spherical codes and designs, s-distance sets MSC Codes. 05B30

1. Introduction

Let Sn−1 be the unit sphere in Rn. A ﬁnite set C ⊂ Sn−1 is called a spherical code. A special class of spherical codes, called spherical designs, was introduced by Delsarte, Goethals and Seidel in 1977 in a seminal paper [13].

Deﬁnition 1.1. A spherical code C ⊂ Sn−1 is called a spherical t-design if the quadrature formula

1 µ(Sn−1) Sn−1

1 |C| x∈C

f(x)

f(x)dµ(x) =

![image 1](<2022-boyvalenkov-rationality-inner-products-spherical_images/imageFile1.png>)

![image 2](<2022-boyvalenkov-rationality-inner-products-spherical_images/imageFile2.png>)

is exact for all polynomials f(x) = f(x1,x2,... ,xn) of degree at most t.

For a spherical code C we consider the set A(C) := { x,y : x,y ∈ C,x = y} and denote by s := |A(C)| the number of distinct inner products of C.

Designs with large t and small s are clearly interesting. Delsarte–Goethals–Seidel [13] proved that t ≤ 2s, and t ≤ 2s − 1 if the set A(C) ∪ {1} is symmetric with respect to 0 and discuss the cases of equality. On the other hand, it is shown in [13] (see Theorem 2.2 below) that t ≥ 2s−2 implies that C carries an s-c1ass association scheme.

Delsarte–Goethals–Seidel [13] also proved the bound

n + m − 1 − ε n − 1

n + m − 2 n − 1

- (1) |C| ≥


+

for any spherical t-design C ⊂ Sn−1, where t = 2m − ε, ε ∈ {0,1}. A design is said to be tight if it attains (1). Tight spherical designs were considered by Bannai–Damerell [2, 3] where it was

![image 3](<2022-boyvalenkov-rationality-inner-products-spherical_images/imageFile3.png>)

Date: April 4, 2022. † The research of the ﬁrst author was supported, in part, by Bulgarian NSF under project KP-06-N32/2-2019. ‡ The second author is supported by JSPS KAKENHI Grant Numbers 18K03396, 19K03445 and 20K03527.

1

proved that tight 2m-designs do not exist for m ≥ 3 and tight (2m − 1)-designs do not exist for m ≥ 5 except for the tight 11-design deﬁned by the Leech lattice in 24 dimensions. Further nonexistence results for tight 4-, 5-, and 7-designs were proved in [5, 19].

Levenshtein [15] proved (in the more general setting of polynomial metric spaces) that the codes with t ≥ 2s − 1 or even t ≥ 2s − 2 if the code is diametrical are maximal, that is they attain what is now known as Levenshtein bound (see [16]). Such codes were called Delsarte codes in polynomial metric spaces [15].

Cohn–Kumar [11] considered spherical codes with t = 2s − 1 or t = 2s − 2 which were called sharp conﬁgurations and appeared to be universally optimal since they have the minimum possible energy for a large class of potential functions1. Boyvalenkov–Dragnev–Hardin–Saﬀ– Stoyanova [8] obtained an energy counterpart of the Levenshtein bound which is attained by all sharp conﬁgurations.

In this paper we prove that the inner products of spherical s-distance t-designs with t ≥ 2s−2 and s ≥ 3 are rational with the only exception being the icosahedron. In other words, we prove that all sharp conﬁgurations have rational inner products and, still in other words, all spherical codes which attain the Levenshtein bound, have rational inner products, except for the icosahedron.

The rationality problem was considered from the very beginning (see Theorem 7.7 in [13]). Bannai–Damerell [2, 3] proved and applied the rationality of the inner products of tight spherical designs in order to prove the nonexistence results, mentioned above. The case (t,s) = (3,2) was considered in [10]. Note that there are spherical 2-distance 2-designs with irrational inner products, which are called conference graphs. Rationality of inner products of antipodal sdistance sets of large cardinalities was proved in [20].

The list of all known spherical s-distance t-designs with t ≥ 2s − 2 and t ≥ 3 is unchanged since 1987 when Levenshtein [14] noticed that an inﬁnite series of spherical 2-distance 3-designs can be added to the examples from Delsarte–Goethals–Seidel [13]. In particular, remarkable optimal codes are good kissing number conﬁgurations [21].

The paper is organized as follows. In section 2 we use algebraic tools for proving the main result in the case s ≥ 6 and derive an important corollary for the small cases. Section 3 is devoted to detailed investigation of the cases s = 3, 4 and 5. In section 4 we present certain consequences and a diﬀerent proof for the case t = 2s − 1 which works for s ≥ 2.

2. The case s ≥ 6

In this section we consider the cases (s,t) = (s,2s−1) and (s,2s−2) for s ≥ 6. The spherical sets have the structures of Q-polynomial association schemes [13]. We will prove the rationality of inner products that appear in the spherical set by using an automorphism of the Bose– Mesner algebra of the association scheme given from the Galois group of its splitting ﬁeld [17] and Suzuki’s result on multiple Q-polynomial structures [23]. First, we give several deﬁnitions and known related results.

![image 4](<2022-boyvalenkov-rationality-inner-products-spherical_images/imageFile4.png>)

1More precisely, for all absolutely monotone potentials.

Let X be a ﬁnite set, and R = {Ri}di=0 be disjoint binary relations on X, where R0 = {(x,x) | x ∈ X}. The pair (X,R) is a (symmetric) association scheme of class d if the following conditions hold:

- (1) X × X = R0 ∪ R1 ∪ ··· ∪ Rd.
- (2) For each i ∈ {0,1,... ,d}, if (x,y) ∈ Ri, then (y,x) ∈ Ri.
- (3) For any i,j,k ∈ {0,1,... ,d}, there exists an integer pkij such that for each (x,y) ∈ Rk it follows pkij = |{z : (x,z) ∈ Ri,(z,y) ∈ Rj}|.


Let Ai be the symmetric matrix whose rows and columns are indexed by X with (x,y) entries

(Ai)xy =

1 if (x,y) ∈ Ri, 0 otherwise.

The linear space spanned by {Ai}di=0 over C is called the Bose–Mesner algebra of an association scheme, and it has two structures of commutative algebra with usual matrix multiplication and

entrywise multiplication. There exist the primitive idempotents {Ei}di=0 of the algebra with the usual multiplication. Namely, it satisﬁes that EiEj = δijEi with Kronecker’s delta δij. The matrix Ei is a positive semideﬁnite matrix with equal diagonal entries, and it is an orthogonal projection matrix onto a same eigenspace of {Ai}di=0. An association scheme is Q-polynomial with respect to the ordering E0,E1,... ,Ed (or with respect to E1) if for each i ∈ {0,1,... ,d}, there exists a polynomial vi(x) of degree i such that Ei = vi(E1) where we use the entrywise multiplication. See [4] for more details on association schemes.

Suzuki [23] proved the following theorem on the multiple structures of Q-polynomial association schemes.

- Theorem 2.1. Let X = (X,{Ri}di=0) be a Q-polynomial association scheme with respect to the ordering E0,E1,... ,Ed such that the rank of E1 is greater than 2. If X is Q-polynomial with respect to another ordering, then the new ordering is one of the following.


- (I) E0,E2,E4,E6,... ,E5,E3,E1.
- (II) E0,Ed,E1,Ed−1,E2,Ed−2,E3,Ed−3,...
- (III) E0,Ed,E2,Ed−2,E4,Ed−4,... Ed−5,E5,Ed−3,E3,Ed−1,E1.
- (IV) E0,Ed−1,E2,Ed−3,E4,Ed−5,... ,E5,Ed−4,E3,Ed−2,E1,Ed.
- (V) d = 5 and E0,E5,E3,E2,E4,E1.


Moreover X has at most two Q-polynomial structures.

The splitting ﬁeld F of an association scheme is the smallest extension of the rationals Q containing the eigenvalues of all Ai [17, 18]. Indeed, the splitting ﬁeld coincides with the smallest extension of Q containing the entries of all Ei. We consider the algebra

A′ = SpanF{Ai}di=0 = SpanF{Ei}di=0. Then a ﬁeld automorphism σ in Gal(F/Q) induces the algebra automorphism of A′ (for the both multiplications) by entrywise action (mij)σ := (mσij). The ﬁeld automorphism σ faithfully acts on the primitive idempotents {Ei}di=0 and Aσi = Ai [17]. If there exists an irrational entry in Ei, then there exists σ ∈ Gal(F/Q) such that Eiσ = Ei. For such σ, a Q-polynomial ordering E0,E1,... ,Ed becomes the other Q-polynomial ordering E0σ = E0,E1σ,... ,Edσ [17].

Delsarte, Goethals, and Seidel [13] showed that an s-distance set with high strength as spherical design has a connection to association scheme as follows.

- Theorem 2.2 (Delsarte–Goethals–Seidel [13]). Let C be a spherical s-distance t-design. For inner products ai ∈ A(C) with 1 = a0 > a1 > ··· > as, we deﬁne the relations Ri = {(x,y) ∈ C × C | x,y = ai}. If t ≥ 2s − 2 holds, then (C,{Ri}si=0) is an association scheme.

For the association scheme obtained from Theorem 2.2, the primitive idempotents are written by characteristic matrices Hk. We introduce the relationship between spherical design and characteristic matrices. A polynomial with real coeﬃcients in n variables ξ1,... ,ξn is harmonic if it is in the kernel of the Laplacian ni=1 ∂2/∂ξi2. Let Harm(n,k) = Harm(k) be the linear space of the homogeneous harmonic polynomials of degree k in n variables. The dimension of Harm(n,k) is

hn,k = hk =

n + k − 1 k −

n + k − 3 k − 2

.

Let {Wk,i}hi=1k be an orthonormal basis of Harm(k) with respect to the inner product

Sn−1

f(x)g(x)dµ(x).

For a ﬁnite set C ⊂ Sd−1 and an orthonormal basis {Wk,i}hi=1k , the k-th characteristic matrix Hk is deﬁned to be the |C| × hk matrix Hk = (Wk,i(x))x∈C,i∈{1,...,hk}.

- Theorem 2.3 ([13]). Let C be a ﬁnite subset of Sn−1 and Hk be a characteristic matrix of C (we

may take any basis of Harm(k)). Then C is a spherical t-design if and only if Hk⊤Hl = |C|∆k,l for 0 ≤ k + l ≤ t, where ∆k,l is the identity matrix if k = l, the zero matrix otherwise.

The following is an expression of the primitive idempotents of the association scheme obtained from Theorem 2.2.

- Theorem 2.4 ([12, 13]). Let C be an s-distance t-design with t ≥ 2s−2, which has the structure of an association scheme. Then the primitive idempotent Ei can be expressed by


1 |C|

HiHi⊤

Ei =

![image 5](<2022-boyvalenkov-rationality-inner-products-spherical_images/imageFile5.png>)

for i ∈ {0,1,... ,s − 1}, and Es = I − i s=0−1 Ei, where I is the identity matrix.

- Remark 2.5. For t ≥ 2s − 2, Hi⊤Hi is the identity matrix of degree hi for i ∈ {0,1,... ,s − 1} by Theorem 2.3. This implies that the rank of Ei is hi and the matrix Ei can be expressed by |C|Ei = (hiQi( x,y ))x,y∈C for i ∈ {0,1,... ,s − 1}, where Qi is the Gegenbauer polynomial of degree i normalized by Qi(1) = 1. From this fact, E1 is identiﬁed with the Gram matrix of C, and the association scheme obtained from C is a Q-polynomial association scheme with respect to E1.


Now we prove the rationality of the inner products.

- Theorem 2.6. Let s be an integer greater than 5, and n an integer greater than 2. Let C be a spherical s-distance t-design in Sn−1. If t ≥ 2s − 2 holds, then the inner product between any two points in C is rational.


Proof. With our assumption, C has the structure of a Q-polynomial association scheme of class s by Theorem 2.2 and Remark 2.5. Let {Ei}si=0 be the primitive idempotents of the Bose–Mesner algebra of the association scheme, where E1 is identiﬁed with the Gram matrix of C. By Remark

- 2.5, the rank of Ek is equal to hn,k for each k ∈ {0,... ,s − 1}. In particular, the rank of E1 is diﬀerent from Ek except for k = s.

Assume there exists an irrational inner product in A(C), namely there exists an irrational entry a in E1. Let F be the splitting ﬁeld of the association scheme. Then there exists a ﬁeld automorphism σ in Gal(F/Q) which does not ﬁx a. The automorphism σ faithfully acts on the

primitive idempotents {Ei}si=0, and does not ﬁx E1. Since the rank of Ekσ is the same as Ek, we must have E1σ = Es and Ekσ = Ek for each k ∈ {2,... ,s − 1}. This implies that the association scheme has the other Q-polynomial structure with ordering E0,Es,E2,E3,... ,Es−1,E1. By

- Theorem 2.1, the possible cases are (II) with s = 2, or (III) with s = 3,4,5. Therefore, for

- s ≥ 6, the inner products are all rationals.


3. The cases s = 3,4,5 The small cases s = 3, 4, 5 are dealt by careful investigation of the distance distributions

of the corresponding codes. Let A(C) = {a1,a2,... ,as} be the nontrivial inner products in C satisfying

−1 ≤ as < as−1 < ··· < a1 < 1.

For ﬁxed x ∈ C and a ∈ A(C), let Aa(x) := |{y ∈ C : x,y = a}|. Then the system of nonnegative integers

(Aa1(x),Aa2(x),... ,Aas(x)) is called the distance distribution of C with respect to x.

Let C ⊂ Sn−1 be a spherical s-distance t-design for n ≥ 3, s ≥ 3, and t ≥ 2s − 2. Then the numbers Aai(x) do not depend on x (so we omit x in the sequel) and satisfy the equations

(2)

s

i=1

ajiAai = fj|C| − 1, j = 0,1,... ,s,

where fj = 0 for odd j, f0 = 1, f2i = (2i−1)!!/n(n+2)··· (n+2i−2) for 1 ≤ i ≤ [t/2] [13]. We will use below the design properties (i.e., the equations from (2)) to analyze the possibilities for the distance distributions and the inner products.

3.1. The cases s = 4,5.

- Theorem 3.1. Let s = 4 or 5, and n be an integer greater than 2. Let C be a spherical sdistance t-design in Sn−1, where t ≥ 2s − 2. Then the inner product between any two points in C is rational.




Proof. It follows from the end of the proof of Theorem 2.6 (see also Remark 2.5) that Qk(a) is rational for each inner product a and k = 2,... ,s − 1. Using this for k = 2, we conclude that all inner products are of the form ±

√

![image 6](<2022-boyvalenkov-rationality-inner-products-spherical_images/imageFile6.png>)

b for some rational b. Using the same fact for k = 3, we see that ±

√b(ub +v) is rational (with u and v rational), which means that either √b is rational or ub + v = 0. In the ﬁrst case we are done, and in the second case the explicit form of the Gegenbauer third degree polynomial implies that b = 3/(n + 2).

![image 7](<2022-boyvalenkov-rationality-inner-products-spherical_images/imageFile7.png>)

![image 8](<2022-boyvalenkov-rationality-inner-products-spherical_images/imageFile8.png>)

![image 9](<2022-boyvalenkov-rationality-inner-products-spherical_images/imageFile9.png>)

Therefore, we may have only ± 3/(n + 2) as possible irrational inner products. Clearly, both should appear with, moreover, A−√

3/(n+2) = A√

3/(n+2), following trivially from (2) for j = 1. We consider separately the cases s = 4 and s = 5, where C has s − 2 = 2 or 3 further rational inner products.

![image 10](<2022-boyvalenkov-rationality-inner-products-spherical_images/imageFile10.png>)

![image 11](<2022-boyvalenkov-rationality-inner-products-spherical_images/imageFile11.png>)

Case 1. s = 4. We denote the two rational inner products by a and b, where a < b, and the corresponding entries from the distance distribution by X and Y . The design properties (2) for odd i (note that t ≥ 2s − 2 ≥ 6) imply that

Xa + Y b = Xa3 + Y b3 = Xa5 + Y b5 = −1. If a2 = b2 and ab = 0, the ﬁrst two equations give

1 − a2 b(b2 − a2)

1 − b2 a(a2 − b2)

. Then,

, Y = −

X = −

![image 12](<2022-boyvalenkov-rationality-inner-products-spherical_images/imageFile12.png>)

![image 13](<2022-boyvalenkov-rationality-inner-products-spherical_images/imageFile13.png>)

a4(1 − b2) b2 − a2 −

b4(1 − a2) b2 − a2

−1 = Xa5 + Y b5 =

= a2b2 − a2 − b2, whence (1 − a2)(1 − b2) = 0. This implies a = −1 and then Y = 0, which is a contradiction.

![image 14](<2022-boyvalenkov-rationality-inner-products-spherical_images/imageFile14.png>)

![image 15](<2022-boyvalenkov-rationality-inner-products-spherical_images/imageFile15.png>)

If a2 = b2, it follows that a = −b. Then −1 = aX + bY = a(X − Y ) and −1 = a3X + b3Y = a3(X − Y ), implying a = −1, a contradiction with a = −b.

If ab = 0, let for example b = 0. Then Xa = Xa3 = −1 gives a = −1 and X = 1, i.e. the inner products are −1, 0 and ± 3/(n + 2); note that the assumption a = 0 would already contradict to a < b. Using (2) for i = 2 and 4, we have

![image 16](<2022-boyvalenkov-rationality-inner-products-spherical_images/imageFile16.png>)

3 n + 2 · A√

3/(n+2) = |C|

2 ·

n − 2 and

![image 17](<2022-boyvalenkov-rationality-inner-products-spherical_images/imageFile17.png>)

![image 18](<2022-boyvalenkov-rationality-inner-products-spherical_images/imageFile18.png>)

![image 19](<2022-boyvalenkov-rationality-inner-products-spherical_images/imageFile19.png>)

9 (n + 2)2 · A√

3|C|

n(n + 2) − 2, respectively, yielding the equality

2 ·

3/(n+2) =

![image 20](<2022-boyvalenkov-rationality-inner-products-spherical_images/imageFile20.png>)

![image 21](<2022-boyvalenkov-rationality-inner-products-spherical_images/imageFile21.png>)

![image 22](<2022-boyvalenkov-rationality-inner-products-spherical_images/imageFile22.png>)

3 n + 2 ·

|C| n − 2 =

3|C|

n(n + 2) − 2, which is only possible for n = 1, a contradiction.

![image 23](<2022-boyvalenkov-rationality-inner-products-spherical_images/imageFile23.png>)

![image 24](<2022-boyvalenkov-rationality-inner-products-spherical_images/imageFile24.png>)

![image 25](<2022-boyvalenkov-rationality-inner-products-spherical_images/imageFile25.png>)

Case 2. s = 5. Denote by a < b < c the three rational inner products and by X, Y , and Z the corresponding entries from the distance distribution. Since t ≥ 2s − 2 ≥ 8, we have

Xa + Y b + Zc = Xa3 + Y b3 + Zc3 = Xa5 + Y b5 + Zb5 = Xa7 + Y b7 + Zc7 = −1

from (2) for i = 1,3,5,7, respectively. Assuming that there are no equal among a2, b2, and c2 and abc = 0, we obtain

(1 − a2)(1 − b2) c(c2 − b2)(c2 − a2) by the ﬁrst three equations. Therefore,

(1 − a2)(1 − c2) b(b2 − a2)(b2 − c2)

(1 − b2)(1 − c2) a(a2 − b2)(a2 − c2)

, Y = −

, Z = −

X = −

![image 26](<2022-boyvalenkov-rationality-inner-products-spherical_images/imageFile26.png>)

![image 27](<2022-boyvalenkov-rationality-inner-products-spherical_images/imageFile27.png>)

![image 28](<2022-boyvalenkov-rationality-inner-products-spherical_images/imageFile28.png>)

−1 = Xa7 + Y b7 + Zc7 = −a2 − b2 − c2 + a2b2 + a2c2 + b2c2 − a2b2c2, that is (1 − a2)(1 − b2)(1 − c2) = 0. If a = −1, then Y = Z = 0, a contradiction.

Assume now (without loss of generality) that b2 = c2 that is, b = −c. This gives the equations Xa + (Y − Z)b = Xa3 + (Y − Z)b3 = Xa5 + (Y − Z)b5 = Xa7 + (Y − Z)b7 = −1,

which implies, in the same way as in the case s = 4, that a = −1, X = 1, and Y − Z = 0 (note that still abc = 0). The equations for even i from (2) give

3/(n+2) + 2Y b2 = |C|

3 n + 2 · A√

n − 2, 2 ·

2 ·

![image 29](<2022-boyvalenkov-rationality-inner-products-spherical_images/imageFile29.png>)

![image 30](<2022-boyvalenkov-rationality-inner-products-spherical_images/imageFile30.png>)

![image 31](<2022-boyvalenkov-rationality-inner-products-spherical_images/imageFile31.png>)

9 (n + 2)2 · A√

3|C|

3/(n+2) + 2Y b4 =

n(n + 2) − 2, 2 ·

![image 32](<2022-boyvalenkov-rationality-inner-products-spherical_images/imageFile32.png>)

![image 33](<2022-boyvalenkov-rationality-inner-products-spherical_images/imageFile33.png>)

![image 34](<2022-boyvalenkov-rationality-inner-products-spherical_images/imageFile34.png>)

27 (n + 2)3 · A√

15|C|

3/(n+2) + 2Y b6 =

n(n + 2)(n + 4) − 2. 2 ·

![image 35](<2022-boyvalenkov-rationality-inner-products-spherical_images/imageFile35.png>)

![image 36](<2022-boyvalenkov-rationality-inner-products-spherical_images/imageFile36.png>)

![image 37](<2022-boyvalenkov-rationality-inner-products-spherical_images/imageFile37.png>)

81 (n + 2)4 · A√

105|C|

3/(n+2) + 2Y b8 =

n(n + 2)(n + 4)(n + 6) − 2, respectively. Expressing b2 from the ﬁrst three equations yields

![image 38](<2022-boyvalenkov-rationality-inner-products-spherical_images/imageFile38.png>)

![image 39](<2022-boyvalenkov-rationality-inner-products-spherical_images/imageFile39.png>)

![image 40](<2022-boyvalenkov-rationality-inner-products-spherical_images/imageFile40.png>)

n(n + 2)(n + 4) − 3|C| n(n + 2)(n + 4) and, similarly, the last three equations give

b2 =

![image 41](<2022-boyvalenkov-rationality-inner-products-spherical_images/imageFile41.png>)

n(n + 2)(n + 4)(n + 6) − 30|C| (n + 6)(n(n + 2)(n + 4) − 3|C|)

b2 =

.

![image 42](<2022-boyvalenkov-rationality-inner-products-spherical_images/imageFile42.png>)

This implies 3|C| = 2n(n+1)(n+2)(n+4)/(n+6), whence in turn b2 = 4n−+6n, possible for n = 2 and 3 only. Now it follows that |C| = 12 and n = 2, which gives s ≥ 6.

![image 43](<2022-boyvalenkov-rationality-inner-products-spherical_images/imageFile43.png>)

Finally, if c = 0 (again without loss of generality), then

Xa + Y b = Xa3 + Y b3 = Xa5 + Y b5 = Xa7 + Y b7 = −1 which is dealt in the same way as in the case s = 4 with a2 = b2.

3.2. The case s = 3. We will use the following fact which can be referred to as Besicovitch’s theorem [6]. If n1,n2,... ,nk are mutually distinct squarefree positive integers and b1,b2,... ,bk are rationals, then the equality

- (3) b1√n1 + b2√n2 + ··· + bk√nk = 0


![image 44](<2022-boyvalenkov-rationality-inner-products-spherical_images/imageFile44.png>)

![image 45](<2022-boyvalenkov-rationality-inner-products-spherical_images/imageFile45.png>)

![image 46](<2022-boyvalenkov-rationality-inner-products-spherical_images/imageFile46.png>)

is possible only when b1 = b2 = ··· = bk = 0. Allowing equal ni’s, it follows that (3) implies, possibly after some rearrangements, that ni = nj and bi + bj = 0 for some 1 ≤ i < j ≤ k.

- Theorem 3.2. If C ⊂ Sn−1, n ≥ 3, is a spherical 3-distance 4-design, then its inner products are rational or n = 3 and C is isometric to the icosahedron.


Proof. We recall that tight 5-designs could possibly exist only in dimensions n = m2 − 2 for some odd positive integer m ≥ 3 or n = 3 (the icosahedron) and their inner products are −1 and ±1/m if n = m2 − 2 or −1 and ±1/√5 if n = 3. We will prove below that C is a 5-design, thus we may assume afterwards in the proof that C is not tight. In particular, we will have |C| > n2 + n by the Delsarte–Goethals–Seidel bound (1).

![image 47](<2022-boyvalenkov-rationality-inner-products-spherical_images/imageFile47.png>)

As in the beginning of the proof of Theorem 3.1 we conclude that all irrational inner products of C are of the form ±

√b for some rational b. We could not use now the third Gegenbauer polynomial and proceed by a direct argument. Let the inner products of C be a1, a2, and a3. Combining the Besicovitch’s theorem (or proceeding directly) and the 1-degree design property

![image 48](<2022-boyvalenkov-rationality-inner-products-spherical_images/imageFile48.png>)

a1Aa1 + a2Aa2 + a3Aa3 = −1

we conclude that that, without loss of generality, a1 = −a2 = √b and Aa1 = Aa2. Therefore a3Aa3 = −1. The 3-degree design property gives a23 = 1, i.e. a3 = −1 and A−1 = 1 (i.e., C is antipodal, therefore a 5-design). Further, we compute Aa1 = Aa2 = (|C| − 2)/2 and

![image 49](<2022-boyvalenkov-rationality-inner-products-spherical_images/imageFile49.png>)

3|C| − 2n(n + 2) n(n + 2)(|C| − 2)

b = |C| − 2n n(|C| − 2)

, b2 =

![image 50](<2022-boyvalenkov-rationality-inner-products-spherical_images/imageFile50.png>)

![image 51](<2022-boyvalenkov-rationality-inner-products-spherical_images/imageFile51.png>)

by the 2- and 4-degree design conditions, respectively. Hence

2

|C| − 2n n(|C| − 2)

3|C| − 2n(n + 2) n(n + 2)(|C| − 2)

=

,

![image 52](<2022-boyvalenkov-rationality-inner-products-spherical_images/imageFile52.png>)

![image 53](<2022-boyvalenkov-rationality-inner-products-spherical_images/imageFile53.png>)

yielding (n − 1)(|C| − n2 − n) = 0, i.e. |C| = n2 + n and C is a tight spherical 5-design, which is a contradiction.

- Remark 3.3. The splitting ﬁeld of a Q-polynomial association scheme is an extension of rationals of degree at most 2 [17, Theorem 2.2]. We may use this instead of the argument via Theorem 2.6 and the Besicovitch theorem.


4. Consequences and reformulations The next theorem is implicit in [15] and a short proof can be found in [9].

- Theorem 4.1. If C ⊂ Sn−1 is a spherical s-distance (2s − 1)-design, which is not tight, then its inner products are exactly the roots of the Levenshtein polynomial


- (4) Ps(u)Ps−1(r) − Ps(r)Ps−1(u) = 0,


2 ,n−2 3)

n−1

where Pi(u) = P(

![image 54](<2022-boyvalenkov-rationality-inner-products-spherical_images/imageFile54.png>)

![image 55](<2022-boyvalenkov-rationality-inner-products-spherical_images/imageFile55.png>)

i (u) is a Jacobi polynomial normalized for Pi(1) = 1 and r is determined as the maximal root of the equation

|C| = L2s−1(n,u), L2s−1(n,u) is the Levenshtein bound.

√

![image 56](<2022-boyvalenkov-rationality-inner-products-spherical_images/imageFile56.png>)

b and the Besicovitch’s theorem implies that either all inner products are rational or there are two products which sum up to 0. The last gives a contradiction the following lemma from [7].

Combining Theorem 4.1 with the fact that the inner products are ±

Lemma 4.2 ([7]). Let t = 2s − 1 ≥ 3 in the non-tight design case. If a0,a1,... ,as−1 are the roots of (4), then ai + aj = 0 for every i,j ∈ {0,1,... ,s − 1}.

This gives an alternative proof of the main result in the case t = 2s − 1 ≥ 3. We present some diﬀerent formulations. Our rationality result implies the following charac-

terization of the spherical codes which attain the Levenshtein bounds.

Corollary 4.3. All codes that attain Levenshtein bounds Lt(n,u) for t ≥ 3, apart from the icosahedron, have rational inner products.

- Remark 4.4. We may have an alternative proof here as well. Indeed, there exist no codes attaining the even bounds L2s(n,u) for s ≥ 2 apart from the tight 4-designs [7], while for odd


- t = 2s − 1 the claim follows from the above discussion.


Cohn–Kumar [11] called sharp conﬁgurations all spherical s-distance (2s −1)-designs. Therefore we may reformulate Corollary 4.3 as follows.

Corollary 4.5. All sharp conﬁgurations apart from the icosahedron have rational inner products. Remark 4.6. After we ﬁnished the ﬁrst version of this manuscript, Bannai [1] suggested to write a simple proof of the rationality for t = 2s − 1 using only the parameters of the corresponding Q-polynomial association schemes. His idea is the use of the equality ms = ms−1b∗s−1/c∗s [4, Ch. II. Proposition 3.7 (vi)]. Under our assumption, we can obtain ms−1 = hs−1, b∗s−1 = n − n(s − 1)/(n + 2(s − 1) − 2) [22, Theorem 3.1], and c∗s ≤ n, where n is the dimension of the sphere Sn−1. If the set X ⊂ Sn−1 has an irrational inner product, then ms = n holds, which implies

- b∗s−1

![image 57](<2022-boyvalenkov-rationality-inner-products-spherical_images/imageFile57.png>)

- c∗s ≥ hs−1 1 −


s − 1 n + 2(s − 1) − 2

.

n = ms = ms−1

![image 58](<2022-boyvalenkov-rationality-inner-products-spherical_images/imageFile58.png>)

However, this inequality is not satisﬁed for s = 3, n > 3, or s = 4,5, n ≥ 3. This method might be not applicable for t = 2s − 2 since b∗s−1 depends on a∗s−1 which is not determined.

Acknowledgments. The authors thank Eiichi Bannai for providing the method to prove the rationality of inner products for t = 2s − 1 as explained in Remark 4.6.

References

- [1] E. Bannai, private communication, Feb. 2022.
- [2] E. Bannai, R.M. Damerell, Tight spherical designs I, J. Math. Soc. Japan 31 (1979) 199-207. DOI:10.2969/jmsj/03110199
- [3] E. Bannai, R.M. Damerell, Tight spherical designs II, J. London Math. Soc. 21 (1980) 13-30. https://doi.org/10.1112/jlms/s2-21.1.13
- [4] E. Bannai, T. Ito, Algebraic Combinatorics I, Benjamin-Cummings, Menlo Park, CA, 1984.
- [5] E. Bannai, A. Munemasa, B. Venkov, The nonexistence of certain tight spherical designs, Algebra i Analiz 16 (2004) 1-23. https://doi.org/10.1090/S1061-0022-05-00868-X
- [6] A.S. Besicovitch, On the linear independence of fractional powers of integers, J. London Math. Soc. 15 (1940) 3-6. https://doi.org/10.1112/jlms/s1-15.1.3
- [7] P. Boyvalenkov, D. Danev, I. Landgev, On maximal spherical codes II, J. Combin. Designs 7 (1999) 316-326. https://doi.org/10.1002/(SICI)1520-6610(1999)7:5<316::AID-JCD2>3.0.CO;2-Z
- [8] P. Boyvalenkov, P. Dragnev, D. Hardin, E. Saﬀ, M. Stoyanova, Universal lower bounds for potential energy of spherical codes, Constr. Approx. 44 (2016) 385-415. https://doi.org/10.1007/s00365-016-9327-5
- [9] P. Boyvalenkov, N. Safaei, On 3-distance spherical 5-designs, Serdica Math. J. 46 (2020) 165-174 (arXiv:2007.01895).
- [10] P. Boyvalenkov, M. Stoyanova, Spherical 2-distance sets which are spherical 3-designs, Ann. Soﬁa Univ. 95

(2004) 53-58.

- [11] H. Cohn, A. Kumar, Universally optimal distribution of points on spheres, J. Amer. Math. Soc. 20 (2007) 99-148. https://doi.org/10.1090/S0894-0347-06-00546-7


- [12] P. Delsarte, An algebraic approach to the association schemes of coding theory, Philips Res. Repts. Suppl. 10 (1973).
- [13] P. Delsarte, J.-M. Goethals, J.J. Seidel, Spherical codes and designs, Geom. Dedicata 6 (1977) 363-388. https://doi.org/10.1016/B978-0-12-189420-7.50013-X
- [14] V.I. Levenshtein, Packing of polynomial metric spaces, in Proc. of Third Intern. Workshop on Inform Theory, Sochi, 1987, 271-274.
- [15] V.I. Levenshtein, Designs as maximum codes in polynomial metric spaces, Acta Appl. Math. 25 (1992) 1-82. https://doi.org/10.1007/BF00053379
- [16] V.I. Levenshtein, Universal bounds for codes and designs, in: V.S. Pless, W.C. Huﬀman (Eds.), Handbook of Coding Theory, Elsevier, Amsterdam, 1998, Ch. 6, 499-648.
- [17] W.J. Martin, J.S. Williford, There are ﬁnitely many Q-polynomial association schemes with given ﬁrst multiplicity at least three, Europ. J. Combin. 30 (2009) 698-704. https://doi.org/10.1016/j.ejc.2008.07.009
- [18] A. Munemasa, Splitting ﬁelds of association schemes, J. Combin. Theory, Ser. A, 57 (1991) 157-161. https://doi.org/10.1016/0097-3165(91)90014-8
- [19] G. Nebe, B. Venkov, On tight spherical designs, St. Petersburg Mathematical Journal 24 (2013) 485-491. https://doi.org/10.1090/S1061-0022-2013-01249-0
- [20] H. Nozaki, A generalization of Larman–Rogers–Seidel’s theorem, Discr. Math. 311 (2011) 792-799. https://doi.org/10.1016/j.disc.2011.01.026
- [21] A.M. Odlyzko, N.J.A. Sloane, New bounds on the number of unit spheres that can touch a unit sphere in n dimensions, J. Combin. Theory, Ser. A, 26 (1979) 210-214. https://doi.org/10.1016/0097-3165(79)90074-8
- [22] S. Suda, On spherical designs obtained from Q-polynomial association schemes, J. Comb. Des. 19(3) (2011) 167-177. https://doi.org/10.1002/jcd.20278
- [23] H. Suzuki, Association schemes with multiple Q-polynomial structures, J. Algebr. Comb. 7 (1998) 181-196. https://doi.org/10.1023/A:1008612505738


Institute of Mathematics and Informatics, Bulgarian Academy of Sciences, 8 G Bonchev Str.,

1113 Sofia, Bulgaria Email address: peter@math.bas.bg Aichi University of Education, Department of Mathematics Education 1 Hirosawa, Igaya-cho,

Kariya-city, Aichi, 448-8542, Japan Email address: hnozaki@auecc.aichi-edu.ac.jp Research Institute of Policy Making, Sharif University of Technology, Tehran, Iran Email address: navid safaei@gsme.sharif.edu

![image 59](<2022-boyvalenkov-rationality-inner-products-spherical_images/imageFile59.png>)

