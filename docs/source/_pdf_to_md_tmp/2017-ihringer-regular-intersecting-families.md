arXiv:1709.10462v3[math.CO]1Jul2019

Regular Intersecting Families

Ferdinand Ihringer∗, Andrey Kupavskii† July 2, 2019

Abstract

We call a family of sets intersecting, if any two sets in the family intersect. In this paper we investigate intersecting families F of k-element subsets of [n] := {1,...,n}, such that every element of [n] lies in the same (or approximately the same) number of members of F. In particular, we show that we can guarantee |F| = o( nk−−11 ) if and only if k = o(n).

# 1 Introduction

Let us denote [n] := {1,... ,n} and 2[n] := {X : X ⊂ [n]}. A family F ⊂ 2[n] of subsets of [n] is called intersecting, if any two of its sets intersect. A family is called k-uniform, if it consists of sets of size k. For shorthand, we denote such a family by F ⊂ [nk] .

The investigation of intersecting families started from the following famous result due to Erd˝os, Ko and Rado.

- Theorem 1 ([10]). Let n ≥ 2k and consider an intersecting family F ⊂ [nk] . Then

|F| ≤

n − 1 k − 1

.

For n > 2k equality occurs if and only if F consists of all k-sets that contain a ﬁxed element of [n].

An intersecting family with all its sets containing a ﬁxed element of [n] is called trivial. The EKR theorem was sharpened by Hilton and Milner [18], who determined the size of the largest non-trivial intersecting k-uniform family. Later, a very strong result in this direction was obtained by Frankl [11]. Below we give a stronger and a more convenient version of that theorem, proven in [22]. The degree δ(x) of x ∈ [n] is deﬁned as the number of members of F that contain x. The maximal degree of F is denoted by ∆(F). The diversity γ(F) of F is the number of sets from F not containing an element of the maximal degree: γ(F) := |F| − ∆(F).

- Theorem 2 ([22]). Let n > 2k > 0 and F ⊂ [nk] be an intersecting family. Then, if γ(F) ≥ n−u−1 n−k−1 for some real 3 ≤ u ≤ k, then


n − 1 k − 1

n − u − 1 n − k − 1 −

n − u − 1 k − 1

|F| ≤

+

. (1)

![image 1](<2017-ihringer-regular-intersecting-families_images/imageFile1.png>)

∗Department of Mathematics: Analysis, Logic and Discrete Mathematics, Ghent University, Belgium. The author is supported by a postdoctoral fellowship of the Research Foundation - Flanders (FWO). Supported by ERC advanced grant 320924 while the author was a postdoctoral fellow at the Einstein Institute of Mathematics, Hebrew University of Jerusalem, Israel. Ferdinand.Ihringer@gmail.com.

†Moscow Institute of Physics and Technology, University of Oxford; Email: kupavskii@yandex.ru. Research supported by the grant RNF 16-11-10014.

Other stability results for k-uniform intersecting families were obtained by several researchers (cf. [1, 7, 9, 19, 21, 26, 27]). Dinur and Friedgut [7] introduced the methods of analysis of Boolean functions to the study of intersecting families. Roughly speaking, they showed that any intersecting family is essentially contained in juntas with small centers. We say that a family J ⊂ 2[n] is a j-junta, if there exist a subset J ⊂ [n] of size j, such that the membership of a set in F is determined only by its intersection with J, that is, for some family J ∗ ⊂ 2J we have

- F = {F : F ∩ J ∈ J ∗}. Here is one of their two main results.


- Theorem 3 ([7]). For any integer r ≥ 2, there exist functions j(r),c(r), such that for any


integers 1 < j(r) < k < n/2, if F ⊂ [nk] is an intersecting family with |F| ≥ c(r) nk−−rr , then there exists an intersecting j-junta J with j ≤ j(r) and

n − r k − r

|F \ J | ≤ c(r)

. (2)

The methods of Dinur and Friedgut were developed and extended to other extremal questions on set systems by other researchers, notably Ellis, Keller, and Lifshitz [9, 20].

In this paper we study intersecting families with respect to another natural measure of nontriviality: the distribution of degrees. The question we address in this paper is as follows: how large an intersecting family may be, provided that all elements of the ground set have the same degree? We call such families regular. In what follows, we always denote the degree of an element in such a family by δ.

Theorem 1 implies that for n > 2k the largest k-uniform intersecting family has one element

of degree nk−−11 while all the other elements of [n] have degree nk−−22 . Hence, the spread between the largest and the smallest degree is very large.

Using Theorem 2 with u = 3, we get that any family of size strictly bigger than nk−−11 + n−4 k−3 − nk−−14 = 3 nk−−23 + nk−−33 has diversity strictly smaller than nk−−34 . Therefore, the maximal

degree of any such family is ∆(F) = |F| − γ(F) > 3 nk−−23 . At the same time, the sum of the degrees of all elements except for a most popular one is (k−1)∆(F)+kγ(F), and so the minimal

degree of F is at most nk−−11∆(F) + n−k1γ(F) < nk−−11∆(F) + n−k1 nk−−34 < nk−−11∆(F) + nk−−23 . It is easy to see that the diﬀerence between the maximal and the minimal degrees is at least

![image 2](<2017-ihringer-regular-intersecting-families_images/imageFile2.png>)

![image 3](<2017-ihringer-regular-intersecting-families_images/imageFile3.png>)

![image 4](<2017-ihringer-regular-intersecting-families_images/imageFile4.png>)

![image 5](<2017-ihringer-regular-intersecting-families_images/imageFile5.png>)

![image 6](<2017-ihringer-regular-intersecting-families_images/imageFile6.png>)

∆(F) − nk−−11∆(F) − nk−−23 = nn−−k1∆(F) − nk−−23 > 23 nk−−23 − nk−−23 > 0. Therefore, we may conclude the following.

![image 7](<2017-ihringer-regular-intersecting-families_images/imageFile7.png>)

![image 8](<2017-ihringer-regular-intersecting-families_images/imageFile8.png>)

![image 9](<2017-ihringer-regular-intersecting-families_images/imageFile9.png>)

Proposition 4. If n ≥ 2k > 0, then any regular k-uniform intersecting family has size at most 3 nk−−23 + nk−−33 .

We write Sn for the symmetric group on [n]. A symmetric family F on [n] is a family such that the automorphism group Aut(F) := {σ ∈ Sn : σ(F) = F} of F is a transitive subgroup of Sn, that is, for all i,j ∈ [n] there exists a permutation σ ∈ Aut(F) such that σ(i) = j. Clearly, any symmetric family must be regular, and the converse is not true in general.

Cameron, Frankl and Kantor [5] studied maximal intersecting families F ⊂ 2[n] (that is, families of size 2n−1), that are additionally symmetric or regular. They proved the following result that relates the size of the ground set and the size of the smallest set in the family.

- Theorem 5 ([5, Theorem 3]). Consider an intersecting family F ⊂ 2[n] of size 2n−1 and an arbitrary set F ∈ F.


- 1. If F is symmetric, then n ≤ |F|2.


- 2. If F is regular, then n ≤ π24|F|.


![image 10](<2017-ihringer-regular-intersecting-families_images/imageFile10.png>)

Ellis, Kalai and Narayanan investigated k-uniform symmetric intersecting families [8]. They obtained the following analogue of the theorem above.

- Theorem 6 ([8, Lemma 4.5]). Let k2 − k + 1 be prime. A k-uniform symmetric intersecting family F on [n] satisﬁes n ≤ k2 − k + 1. Further, equality holds if and only if F is a pointtransitive projective plane of order k − 1.

This result was already shown by Lov´asz without the characterization of equality, but not published (it is mentioned in [24, 25]), and Fu¨redi [14, 16] for regular families. We give a second proof for this result that was obtained independently.

- Theorem 7 ([14, Corollary 3]). A k-uniform regular intersecting family F on [n] satisﬁes n ≤ k2 − k + 1. Further, equality holds if and only if F is a projective plane of order k − 1.

Ellis, Kalai and Narayanan obtained the following bound on the size of a k-uniform symmetric intersecting family.

- Theorem 8 ([8, Theorem 1.3]). There exists a constant c > 0 (independent of n and k) such that for k ≤ n/2 and any symmetric intersecting family F we have

|F| ≤ exp −

c(n − 2k)log n k(log n − log k)

![image 11](<2017-ihringer-regular-intersecting-families_images/imageFile11.png>)

n k

.

Their proof uses tools from the analysis of Boolean functions, notably, the sharp threshold result due to Friedgut and Kalai [13]. They managed to show that this bound is tight up to the constant c in the exponent, if k/n is bounded away from zero.

Using Theorem 3, we are able to obtain the following upper bound on the size of regular intersecting families.

- Theorem 9. For any r ∈ N there exists a constant C = C(r), such that for n > Ck any regular family F ⊂ [nk] satisﬁes

|F| ≤ C

n − r k − r

.

Moreover, it is possible to strengthen the theorem above to the following setting. We say that the family is α-irregular for α ≥ 1, if the ratio between the maximal degree and the minimal degree is at most α.

- Theorem 10. For any r ∈ N and α ∈ R≥1 there exists a constant C = C(r,α), such that for n > Ck any α-irregular family F ⊂ [nk] satisﬁes

|F| ≤ C

n − r k − r

.

The next result uses algebraic methods, and may be applied for all values of n and k. However, it works only for regular families and is weaker than Theorem 9 in the range when Theorem 9 may be applied.

- Theorem 11. A regular k-uniform intersecting family on [n] satisﬁes


n k

|F| ≤

.

![image 12](<2017-ihringer-regular-intersecting-families_images/imageFile12.png>)

1 + (n−k)(k(nk−−k1)(−1)(k−n2)−k−2)

![image 13](<2017-ihringer-regular-intersecting-families_images/imageFile13.png>)

We only know sporadic examples for which the bound is tight. We also remark that it is not diﬃcult to see that the bound in Theorem 11 is always stronger than the bound from Proposition 4.

If n = ck for some constant c, then all the upper bounds we give have order Θ( nk−−11 ). This is in sharp contrast with the situation for symmetric intersecting families, for which in [8] the upper bounds have order o( nk−−11 ) for n − 2k = Θ(k/log k). However, this is not a shortcoming of our methods: for any c we give a series of examples of a regular intersecting families in [nk] , such that n > ck and that have size Θ( nk−−11 ). Therefore, the following is true.

Proposition 12. If k = o(n), then any regular intersecting family in [nk] has size o( nk−−11 ). At the same time, for any c > 0 there are regular intersecting families in [nk] with n > ck and which have size Θc( nk−−11 ).

We note that a similar construction was used in [15, Theorem 3] by Fu¨redi and [12, Theorem

- 2.4] by Frankl and Fu¨redi. However, their studies were concerned with intersecting families with bounded maximum degree and they did not require the families to be regular. In particular, the lower bounds they prove resemble Theorem 9, but are only meaningful for n ≫ k2, which is by Theorem 7 not interesting as long as regular intersecting families are considered.


The structure of the paper is as follows. In Section 2 we review some notions from the theory of association schemes, needed in the proofs of Theorems 7 and 11. In Section 3 we prove the upper bounds on the size of regular intersecting families and some of its generalizations, in particular, to the case of degrees of subsets. In the ﬁrst part of Section 4 we provide some general constructions of regular intersecting families, which in particular imply the corresponding part of Proposition 12. In the second part of Section 4 we study in detail the case n = 2k, and give some results in the case n = 2k + 1. Finally, in Section 5 we conclude and give future directions for research.

# 2 The Johnson Scheme

In the proof of Theorems 7 and 11 we use the theory of association schemes. To make this paper more self-contained, this section summarizes the necessary notions and results. We refer to Delsarte’s PhD thesis [6] as a standard reference on the combinatorial applications of association schemes.

Deﬁnition 13. Let X be a ﬁnite set. A k-class association scheme is a pair (X,R), where R = {R0,... ,Rk} is a set of symmetric binary relations on X with the following properties:

- (a) {R0,... Rk} is a partition of X × X.
- (b) R0 is the identity relation.
- (c) There are constants pℓij such that for x,y ∈ X with (x,y) ∈ Rℓ there are exactly pℓij elements z with (x,z) ∈ Ri and (z,y) ∈ Rj.


We denote p0ii by ri, the valency of Ri. We denote |X| by v = ki=0 ri. The relations Ri can be described by their adjacency matrices Ai ∈ Cv×v deﬁned by

(Ai)xy =

1 if xRiy, 0 otherwise.

Let J denote the all-ones matrix and let j denote the all-ones vector. It is easily veriﬁed that the matrices Ai are Hermitian and commute pairwise, hence we can diagonalize them simultaneously, i.e. there is a set of common eigenvectors. From this we obtain pairwise orthogonal, idempotent Hermitian matrices Ej ∈ Cv×v with the properties (possibly after reordering)

k

Ej = I, E0 = v−1J,

j=0

Ai =

k

k

PjiEj, Ej = v−1

i=0

j=0

QijAi (3)

for some constants Pij and Qij. From this it is clear that the matrices A0,A1,... ,Ak have k +1 common eigenspaces V0 = j ,V1,... ,Vk, where the eigenspaces Vj has dimension fj := rk(Ej) = tr(Ej) and Pji is the eigenvalue of Ai in the eigenspace Vj. Note that Ej is an orthogonal projection from Cv×v onto Vj. There are several connections between the parameters of an association scheme, for example ri = P0i. For us the following is important.

Lemma 14 ([6, Eq. (4.34)]). We have riQij = fjPji. Let F be a subset of X. Let χ be the characteristic vector of F, i.e.

χx =

1 if x ∈ F, 0 otherwise.

Deﬁne the inner distribution a of F, |F| > 0, by

1 |F|

χTAiχ.

ai =

![image 14](<2017-ihringer-regular-intersecting-families_images/imageFile14.png>)

The essential property of association schemes, which we use, is summarized in the following result which is often referred to as Delsarte’s linear programming bound (LP bound). Theorem 15 ([3, Lemma 2.5.1 (iv) and Prop. 2.5.2]). We have (aQ)j = |F|v χTEjχ ≥ 0 with equality if and only if χ ∈ Vj⊥.

![image 15](<2017-ihringer-regular-intersecting-families_images/imageFile15.png>)

The vector aQ is often referred to as the MacWilliams transform of a. A very particular, well-known case in Delsarte’s LP bound is when χ ∈ j + Vj for some j ∈ {1,... ,k}:

- Lemma 16. Let χ be the characteristic vector of F. If χ ∈ j + Vj, then the following holds:


- (a) If F ∈ F, then F meets exactly |F|(P0i − Pji)/v + Pji elements of F in relation Ri.
- (b) If F ∈/ F, then F meets exactly |F|(P0i − Pji)/v elements of F in relation Ri.


Proof. Let ψ be the characteristic vector of {F}. Write χ = |F|v j + χ′ with χ′ ∈ Vj. Then the number of elements in F that are in relation Ri to F is

![image 16](<2017-ihringer-regular-intersecting-families_images/imageFile16.png>)

k

PjiEj |F| v

j + χ′

ψTAiχ = ψT

![image 17](<2017-ihringer-regular-intersecting-families_images/imageFile17.png>)

i=0

= ψT P0i|F| v

|F| v

j) = |F|(P0i − Pji)/v + PjiψTχ.

j + Pji(χ −

![image 18](<2017-ihringer-regular-intersecting-families_images/imageFile18.png>)

![image 19](<2017-ihringer-regular-intersecting-families_images/imageFile19.png>)

![image 20](<2017-ihringer-regular-intersecting-families_images/imageFile20.png>)

![image 21](<2017-ihringer-regular-intersecting-families_images/imageFile21.png>)

![image 22](<2017-ihringer-regular-intersecting-families_images/imageFile22.png>)

![image 23](<2017-ihringer-regular-intersecting-families_images/imageFile23.png>)

The Johnson scheme has X = [nk] . Two k-sets are in relation Ri if their intersection is of size k − i. We recall the eigenvalues of the Johnson scheme. As this association scheme is cometric, its eigenspaces have a canonical ordering which we use in the following.

- Lemma 17 ([6, p. 48] and [17, Theorem 6.5.2]). The eigenvalue of Ai of the eigenspace Vj is

Pji =

i

h=0

(−1)h

j h

k − j i − h

n − k − j i − h

=

k

h=i

(−1)h−i+j

- h
- i


n − 2h k − h

n − h − j h − j

.

In particular, Pjk = (−1)j n−k−k−j j . We will use Theorem 15 for j = 1 and j = 2, so we need Qi1 and Qi2 explicitly.

- Lemma 18. We have

- (a) c1Qi1 = kn − in − k2, and
- (b) c2Qi2 = (k − i)(k − i − 1)(n − k − i)(n − k − i − 1) − 2i2(k − i)(n − k − i) + i2(i − 1)2, where c1 = k(n − k)/f1 and c2 = k(k − 1)(n − k)(n − k − 1)/f2. Proof. Evaluate Lemma 14 for the stated cases using Lemma 17.


![image 24](<2017-ihringer-regular-intersecting-families_images/imageFile24.png>)

![image 25](<2017-ihringer-regular-intersecting-families_images/imageFile25.png>)

![image 26](<2017-ihringer-regular-intersecting-families_images/imageFile26.png>)

![image 27](<2017-ihringer-regular-intersecting-families_images/imageFile27.png>)

The eigenspaces of the Johnson scheme have various nice combinatorial descriptions. Let GS denote the family of all k-sets that contain a ﬁxed s-set S. Clearly, |GS| = nk−−ss . Let λs = nk−−ss / nk . Let ψS denote the characteristic vector of GS.

- Lemma 19 ([17, Theorem 6.3.3]). Fix s ∈ {1,... ,k}. The set ∪sr=1{ψR −λrj : R ∈ [nr] } spans V1 + V2 + ... + Vs.

We say that a family F is s-subset-regular if every s-set lies in the same number of elements δs of F. For any r with 1 ≤ r ≤ s, double counting pairs (R,S) ∈ [nr] × [ns] with R ⊂ S shows that every r-set lies in exactly δs ns−−rr / ks−−rr elements of F. The following is well-known, but we include a short proof for completeness.

- Lemma 20. Fix s ≥ 1. Let F be a family of k-uniform sets and let χ be the characteristic vector of F. Then (a) implies (b) and (c):


- (a) F is s-subset-regular.
- (b) The vector χ is orthogonal to the eigenspaces V1,... ,Vs.
- (c) The inner distribution a of F satisﬁes


k

Qi1ai.

0 =

i=0

Proof. The eigenspaces V0, V1, .. ., Vk are pairwise orthogonal, so we can write χ = E0χ+(E1+ E2 + ... + Ek)χ = |F|v j + χ′, where χ′ ∈ V1 + V2 + ... + Vk. Hence, for any R ∈ [nr] , where 1 ≤ r ≤ s,

![image 28](<2017-ihringer-regular-intersecting-families_images/imageFile28.png>)

T

χTψR = |F| v

(λrj) + χ′T (ψR − λrj)

j

![image 29](<2017-ihringer-regular-intersecting-families_images/imageFile29.png>)

= |F|λr + χ′T (ψR − λrj) .

Since, by simple double counting, the degree of R in F is λr|F|, we have χ′T (ψR − λrj) = 0. Hence, χ is orthogonal to all vectors in V1 + V2 + ... + Vs. Hence, (a) implies (b).

By Theorem 15, χ ∈ V1⊥ is equivalent to (c).

![image 30](<2017-ihringer-regular-intersecting-families_images/imageFile30.png>)

![image 31](<2017-ihringer-regular-intersecting-families_images/imageFile31.png>)

![image 32](<2017-ihringer-regular-intersecting-families_images/imageFile32.png>)

![image 33](<2017-ihringer-regular-intersecting-families_images/imageFile33.png>)

# 3 Upper Bounds

## 3.1 Proof of Theorems 9 and 10

Clearly, Theorem 9 is implied by Theorem 10, so we only need to prove Theorem 10. In terms of Theorem 3, we put C = max{2αj(r),2c(r)}. Fix n,k, such that n ≥ Ck and an

α-irregular family F ⊂ [nk] . Then Theorem 3 states that there exists an intersecting j-junta J = {A ∈ [nk] : A ∩ J ∈ J ∗} for some J with |J| = j ≤ j(r) and J ∗ ⊂ 2J, such that |F \ J | ≤ c(r) nk−−rr .

We may assume that |F| > C nk−−rr ≥ 2c(r) nk−−rr , otherwise we have nothing to prove. Therefore, we have |F ∩ J |/|F| > 1/2.

Given the approximation by the junta J , let us bound the degrees of elements in F. On the one hand, clearly, any set from F ∩ J intersects J, therefore, the maximal degree of an element in J is at least |F ∩ J |/j. On the other hand, the average degree of an element in [n] is nk|F| ≤ |F|/C. Hence, the ratio between the maximal and the minimal degree in F is at least

![image 34](<2017-ihringer-regular-intersecting-families_images/imageFile34.png>)

|F ∩ J |/j |F|/C

C 2j ≥ α.

>

![image 35](<2017-ihringer-regular-intersecting-families_images/imageFile35.png>)

![image 36](<2017-ihringer-regular-intersecting-families_images/imageFile36.png>)

We conclude that, if |F| > C nk−−rr , then F is not α-irregular. Theorem 10 is proved.

## 3.2 Proof of Theorem 11

Theorem 11 is implied by the following result for s-subset-regular k-uniform intersecting families. It is a variation of Hoﬀman’s bound.

Theorem 21. Fix odd s ≥ 1. An s-subset-regular k-uniform intersecting family F on [n] satisﬁes

v 1 − P0k/P(s+2)k

|F| ≤

![image 37](<2017-ihringer-regular-intersecting-families_images/imageFile37.png>)

n k

.

=

![image 38](<2017-ihringer-regular-intersecting-families_images/imageFile38.png>)

(n−kk) (n−k−k−s−s−22)

1 +

![image 39](<2017-ihringer-regular-intersecting-families_images/imageFile39.png>)

For n > 2k we have equality only if the characteristic vector χ of F lies in the span of j and the eigenspace Vs+2.

Proof of Theorem 21. Let χ be the characteristic vector of F. First notice that

k

|F| = χTχ = |F|2 v

χTEjχ. (4)

+

![image 40](<2017-ihringer-regular-intersecting-families_images/imageFile40.png>)

j=1

Let A = Ak − si=1 PikEi. Obviously, A has the eigenvalues Pjk for j = 0 and j > s, and the eigenvalue 0 for the eigenspace Vi, where 1 ≤ i ≤ s. From the deﬁnition of F, χTAkχ = 0. By Lemma 20, χTEiχ = 0 for 1 ≤ 1 ≤ s. Hence, χTAχ = 0. Notice that, using Lemma 17 and Equation (3), P(s+2)k is the smallest eigenvalue of A, so we obtain

0 = χTAχ =

≥

(=4)

k

P0k v

PjkχTEjχ

χTJχ +

![image 41](<2017-ihringer-regular-intersecting-families_images/imageFile41.png>)

j=s+1

k

P0k v

χTJχ + P(s+2)k

χTEjχ

![image 42](<2017-ihringer-regular-intersecting-families_images/imageFile42.png>)

j=1

|F|2 v

P0k v · |F|2 + P(s+2)k |F| −

![image 43](<2017-ihringer-regular-intersecting-families_images/imageFile43.png>)

![image 44](<2017-ihringer-regular-intersecting-families_images/imageFile44.png>)

.

Rearranging yields

v 1 − P0k/P(s+2)k

|F| ≤

,

![image 45](<2017-ihringer-regular-intersecting-families_images/imageFile45.png>)

which, together with Lemma 17, shows the ﬁrst half of the assertion. For the second half of the assertion notice that we have equality in this bound only if χTEs+2χ = kj=1 χTEjχ.

![image 46](<2017-ihringer-regular-intersecting-families_images/imageFile46.png>)

![image 47](<2017-ihringer-regular-intersecting-families_images/imageFile47.png>)

![image 48](<2017-ihringer-regular-intersecting-families_images/imageFile48.png>)

![image 49](<2017-ihringer-regular-intersecting-families_images/imageFile49.png>)

Evaluating Lemma 16 for the case of equality in Theorem 21 and s = 1, we obtain that a k-set F ∈/ F meets exactly

3k(k − 1)(k − 2) n2 − 3kn − n + 3k2

![image 50](<2017-ihringer-regular-intersecting-families_images/imageFile50.png>)

elements of F in k − 1 elements. As this has to be an integer, Theorem 21 cannot be tight for many combinations of n and k. In particular, the bound is never tight for 3k(k − 1)(k − 2) < n2 − 3kn − n + 3k2. For odd s ≥ 1 ﬁxed, the same argument yields that the bound is not tight for n at least ∼

√s + 2k

s+2

![image 51](<2017-ihringer-regular-intersecting-families_images/imageFile51.png>)

s+1.

![image 52](<2017-ihringer-regular-intersecting-families_images/imageFile52.png>)

Ray-Chaudhuri and Wilson showed in [28, Theorem 1] that a 2t-design contains at least nt blocks. Together with Theorem 21 this implies that s-subset-regular intersecting families do not exist when s is large compared to k (vaguely k < 23(s + 1)). Remark 22. The bound of

![image 53](<2017-ihringer-regular-intersecting-families_images/imageFile53.png>)

v 1 − P0k/P(s+2)k

![image 54](<2017-ihringer-regular-intersecting-families_images/imageFile54.png>)

and its consequences hold for various other association schemes, where the eigenspaces can be characterized in a similar way. One example for such an association scheme would be the qanalog of the Johnson scheme, the q-Johnson (Grassmann) scheme.

## 3.3 Proof of Theorem 7

For small n Delsarte’s linear programming (LP) bound corresponds to Theorem 21, but for n close to k2 − k + 1 Delsarte’s LP bound is much better. In particular, Delsarte’s LP bound implies Theorem 7. In the following we prove this formally.

Proof of Theorem 7. The inner distribution a of an intersecting family F has the form a = (1,a1,... ,ak−1,0). In terms of Lemma 18, denote αi := c2Qi2 and βi := c1Qi1. By Lemma 20, we know that i k=0−1 βiai = 0. By Theorem 15, we know that i k=0−1 αiai ≥ 0. Hence,

k−1 i=0 (αi − (k − 1)(n − k − 1)βi)ai ≥ 0. Using Lemma 18, we have that

γi := αi − (k − 1)(n − k − 1)βi = −i(n − 2)(kn − in − k2 + i).

If n > k2 − k + 1, then γi < 0 for all i ∈ {1,... ,k − 1}. Hence, i k=0−1 γiai ≥ 0 implies a = (1,0,... ,0), which is a contradiction. Thus, we can assume n = k2 − k + 1. Then γi = 0 for i ∈ {0,k − 1} and γi < 0 for i ∈ {1,... ,k − 2}. Hence, i k=0−1 γiai ≥ 0 implies a = (1,0,... ,0,ak−1,0). Now i k=0−1 βiai = 0 together with Lemma 20 implies (k − 1)k = ak−1. Therefore, |F| = k2 − k + 1, each element in [k2 − k + 1] has degree k, and each set in F meets all other sets in F in exactly one point. This is a well-known deﬁnition of a projective plane of order k − 1.

![image 55](<2017-ihringer-regular-intersecting-families_images/imageFile55.png>)

![image 56](<2017-ihringer-regular-intersecting-families_images/imageFile56.png>)

![image 57](<2017-ihringer-regular-intersecting-families_images/imageFile57.png>)

![image 58](<2017-ihringer-regular-intersecting-families_images/imageFile58.png>)

A similar method also gives us the following lower bound on the size of a regular k-uniform intersecting family F. Lemma 23. If a regular k-uniform intersecting F exists, then

k(n − k) k2 − n with equality only if i k=1−2 ai = 0.

|F| ≥ 1 +

![image 59](<2017-ihringer-regular-intersecting-families_images/imageFile59.png>)

Proof. Let a be the inner distribution of F. By Lemma 19, kn−k2 + i k=1−1(kn−in−k2)ai = 0. It is easy to see that under this constraint |F| = i k=0−1 ai is minimized if a = (1,0,... ,0,ak−1,0).

![image 60](<2017-ihringer-regular-intersecting-families_images/imageFile60.png>)

![image 61](<2017-ihringer-regular-intersecting-families_images/imageFile61.png>)

![image 62](<2017-ihringer-regular-intersecting-families_images/imageFile62.png>)

![image 63](<2017-ihringer-regular-intersecting-families_images/imageFile63.png>)

# 4 Lower Bounds

We have already shown that there are no regular families for n > k2 − k + 1 and that for n = k2 − k + 1 a projective plane of order k − 1 is the only possible example. We note that the existence of projective planes is only known for k − 1 being a prime power. In the ﬁrst part of this section we give some general constructions of how to build bigger regular intersecting families out of smaller ones, and derive some general lower bounds. In the second part of this section we discuss the case n = 2k and n = 2k + 1, as well as some results for small values of k.

We note that Ellis, Kalai, and Lifshitz in [9, Section 4] construct symmetric (and thus regular) k-uniform intersecting families on [n] for all k and n satisfying k ≥ 1.1527√n. They rely on the relation between intersecting families and diﬀerence covers for Zn. We could not improve their results for the case of regular intersecting families, so a very interesting question that remains is whether regular intersecting families exist for all suﬃciently large n,k satisfying k ≥ (1 + o(1))√n.

![image 64](<2017-ihringer-regular-intersecting-families_images/imageFile64.png>)

![image 65](<2017-ihringer-regular-intersecting-families_images/imageFile65.png>)

## 4.1 General Constructions and Proposition 12

For any regular family F ⊂ [nk] we put α(F) := k/n. We call this parameter the ratio of F. Due to the simple equality |F|k = nδ, α(F) = δ/|F| and α(F) tells us, what proportion of all

sets from F contains a given element.

Let us start with giving some general ways of constructing a regular intersecting family. Assume that we have a regular intersecting family F ⊂ Xk on the set X, a regular intersecting family F2 ⊂ k Y

on the set Y , and a regular (but not necessarily intersecting) family G ⊂ m Z on the set Z. Assume additionally that the sets X,Y,Z are pairwise disjoint and that the ratios of F and G are the same: α(F) = α(G).

2

Fix a parameter l, 1 ≤ l < min{|F1 \ F2| : F1,F2 ∈ F,F1 = F2}. Then the following families are intersecting and regular:

Fl := F′ ∈

X k + l

: F′ ⊃ F for some F ∈ F , Fl ⊂

X k + l

F + G := F ∪ G : F ∈ F,G ∈ G , F + G ⊂

F × F2 := F × F2 : F ∈ F,F2 ∈ F2 , F × F2 ⊂

; (5)

X ∪ Z k + m

; (6)

X × Y kk2

. (7)

It is easy to see that each of the families above is intersecting. Let us show that all these families are regular. It is obvious in the case of F × F2.

This is the most diﬃcult to show in the case of family Fl. First, note that, due to the choice of l, for any F′ ∈ Fl there is a unique set F ∈ F, such that F′ ⊃ F. Thus, we may partition Fl into families Fl(F) := {F′ ∈ k X+l : F′ ⊃ F}, where F ∈ F. The elements in Fl(F) have two possible degrees. Each element x ∈ F has degree |Fl(F)| = |X|−l k , while any element x ∈ X\F has degree |X|−l−k1−1 . It is clear that, since F is regular, each x ∈ X has degree of the ﬁrst type in α(F)|F| families Fl(F) and the degree of the second type in all the others. Since the degree of each element in Fl is the sum of its degrees in Fl(F), we conclude that F′ is regular. We note that |Fl| = |X|−l k |F|.

The family F + G is regular, since each element from X is contained in α(F)-fraction of all sets in F + G, and each element from Y is contained in α(G)-fraction of all sets in F + G. However, α(F) = α(G) by assumption. We note that |F+G| = |F||G| and that α(F+G) = α(F).

We use Construction (6) to show the lower bound from Proposition 12. Fix c > 0 from the proposition. Recall that we need to construct a regular intersecting family with ratio at most 1/c and size Θ( nk−−11 ). In particular, nk and nk−−11 are of the same order of magnitude. Find a prime power q, such that (q2 + q + 1)/(q + 1) > c. Put F to be the projective plane of order q on the set X. Note that F is regular, intersecting, and α(F) = (q + 1)/(q2 + q + 1). Take

- G = l(q Z+1) , where Z is a set of size l(q2+q+1) disjoint with X. Here we think of q that is ﬁxed and l that tends to inﬁnity. Then α(G) = α(F). Thus, the family F + G is regular, intersecting, and satisﬁes α(F + G) < 1/c. Moreover, F + G ⊂ (l+1)( |X∪qZ+1)| and


|F + G|

![image 66](<2017-ihringer-regular-intersecting-families_images/imageFile66.png>)

|X∪Z| (l+1)(q+1)

(q2 + q + 1) l(ql2(q++1)q+1)

=

>

![image 67](<2017-ihringer-regular-intersecting-families_images/imageFile67.png>)

(l+1)(q2+q+1) (l+1)(q+1)

(q2 + q + 1) l(ql(2q++1)q+1) l(q2+q+1) l(q+1)

### = Θq(1).

![image 68](<2017-ihringer-regular-intersecting-families_images/imageFile68.png>)

q2+q+1

(l+1)(q2+q+1)

![image 69](<2017-ihringer-regular-intersecting-families_images/imageFile69.png>)

q2

q+1

lq2

l(q+1)

## 4.2 Case n = 2k

In the case n = 2k no intersecting family of k-sets can have size bigger than 2kk−1 . Brace and Daykin [2] (in somewhat diﬀerent terms) showed that for k not a power of 2, this bound is tight.

- Theorem 24 ([2, Example 1]). If k is not a power of 2, then a largest k-uniform regular intersecting family on [2k] has size 2kk−1 .

Brace and Daykin also noted that it is easy to see that if k is a power of 2 that then a regular

family of size 2kk−1 would have a non-integer degree, that is there the bound of 2kk−1 is not tight. We complete their result by showing the following.

- Theorem 25. If k ≥ 4 is a power of 2, then the largest k-uniform regular intersecting family on [2k] has size 2kk−1 − 3.


Note that there is no regular intersecting family for k = 2, n = 4, and substituting k = 2 in the bound above gives 0. We also remark that from the proof we give below it is fairly easy to reconstruct the proof of Theorem 24.

Proof. First we show the upper bound. Let F be the largest regular intersecting family for n = 2k, k = 2t. Consider the family F(2k) := {F ∈ F : 2k ∈ F}. Simple counting shows that |F(2k)| = 21|F|. Assume that the degree of an element i in F(2k) is d(i). If all d(i), i = 1,... ,2k −1, are the same, then 12|F| = |F(2k)| = d(1)2kk−−11, and thus 2(2k −1) must divide

![image 70](<2017-ihringer-regular-intersecting-families_images/imageFile70.png>)

![image 71](<2017-ihringer-regular-intersecting-families_images/imageFile71.png>)

![image 72](<2017-ihringer-regular-intersecting-families_images/imageFile72.png>)

- |F| and |F| ≤ 2kk−1 −(2k −1). (Here we use an easy-to-check fact that (2k −1) divides 2kk−1 , but 2 does not.)

Otherwise, consider the family

F¯(2k) :=

[2k − 1]

k \ [2k] \ F : F ∈ F(2k) . (8) Clearly, F \ F(2k) ⊂ F¯(2k). Moreover, the degree of the element i ∈ [2k − 1] in F¯(2k) is d¯(i) = 2kk−−12 − |F(2k)| + d(i). Therefore, the degree of i ∈ [2k − 1] in F′ := F(2k) ∪ F¯(2k) is

2k − 2 k − 1 − |F(2k)| + 2d(i). (9)

We have |F| = 2kk−1 − (2l + 1) for some l ≥ 0. Thus F \ F(2k) = F¯(2k) \ G, where

- |G| = 2l + 1. Since not all d(i), i = 1,... ,2k − 1, are equal to each other, by the displayed formula above two degrees in F′ diﬀer by at least 2. Thus, one has to delete at least two sets


from F′ to get a regular family, which implies that l ≥ 1 and proves |F| ≤ 2kk−1 − 3. This shows the upper bound in Theorem 25.

Now let us show the lower bound. The following lemma is the key step. (We postpone the proof of the lemma until the end of the proof of the theorem.)

Lemma 26. There exists a family Q ⊂ [2kk−−11] of size 12( 2kk−−11 − 3) with the degrees d′(i) of i ∈ [2k −1] satisfying d′(1)−1 = d′(2)−1 = ... = d′(3k/2)−1 = d′(3k/2+1) = ... = d′(2k −1)

![image 73](<2017-ihringer-regular-intersecting-families_images/imageFile73.png>)

and such that the sets A1 := [k + 1,2k − 1], A2 := [1,k/2] ∪ [3k/2 + 1,2k − 1], and A3 := [k/2 + 1,k] ∪ [3k/2 + 1,2k − 1] are not in Q.

Double counting the sum of d′(i) in such Q, we get that the degree of, say, 2k − 1 equals

2k − 1 k − 1 − 3 −

k − 1 2(2k − 1)

k − 1 2

2k − 1 k − 1 −

2k − 2 k − 2 −

- 1

![image 74](<2017-ihringer-regular-intersecting-families_images/imageFile74.png>)

- 2


3k 2

3 2

3 2

- 1

![image 75](<2017-ihringer-regular-intersecting-families_images/imageFile75.png>)

- 2k − 1


=

=

, (10)

![image 76](<2017-ihringer-regular-intersecting-families_images/imageFile76.png>)

![image 77](<2017-ihringer-regular-intersecting-families_images/imageFile77.png>)

![image 78](<2017-ihringer-regular-intersecting-families_images/imageFile78.png>)

![image 79](<2017-ihringer-regular-intersecting-families_images/imageFile79.png>)

![image 80](<2017-ihringer-regular-intersecting-families_images/imageFile80.png>)

which, in particular, is an integer number (recall that 2kk−−11 is odd, and so is 2kk−−22 =

2k−1 k−1 ). This shows that there are no divisibility obstructions to the existence of Q.

k−1 2k−1

![image 81](<2017-ihringer-regular-intersecting-families_images/imageFile81.png>)

We put F(2k) := {{2k} ∪ Q : Q ∈ Q}. Next, we consider the family F¯(2k) deﬁned as in

(8). The family F′ := F(2k) ∪ F¯(2k) has size 2kk−1 and the degrees of the ﬁrst 3k/2 elements are bigger by two than the degrees of the last k/2 elements as we will see in the following. The

degree of 2k in F′ is |F(2k)| = 21( 2kk−1 − 3), which is the same as the degree of, say, 2k − 1, equal by (9) and (10) to

![image 82](<2017-ihringer-regular-intersecting-families_images/imageFile82.png>)

2k − 2 k − 1 −

2k − 1 k − 1 − 3 +

2k − 1 k − 1 − 3 .

2k − 2 k − 2 − 3 =

- 1

![image 83](<2017-ihringer-regular-intersecting-families_images/imageFile83.png>)

- 2


- 1

![image 84](<2017-ihringer-regular-intersecting-families_images/imageFile84.png>)

- 2


Moreover, F′ contains [2k − 1] \ Ai for i = 1,2,3. The family {[2k − 1] \ Ai : i = 1,2,3} has degree 2 on the ﬁrst 3k/2 elements and 0 on the remaining ones. Thus, deleting these sets from

F′, we get a regular family F of size 2kk−1 − 3. It remains to show that F′ is intersecting. Clearly, F(2k) is intersecting as all elements

contain 2k and F¯(2k) is intersecting as all its elements are in [2kk−1] . By the deﬁnition of F¯(2k) in (8), if F ∈ F(2k), then [2k] \ F ∈/ F¯(2k). Hence, each element of F(2k) intersects all

elements of F¯(2k). Proof of Lemma 26. Due to (10), we only need to show that there exists Q of desired size and without Ai, in which any two degrees diﬀer by at most 1.

![image 85](<2017-ihringer-regular-intersecting-families_images/imageFile85.png>)

![image 86](<2017-ihringer-regular-intersecting-families_images/imageFile86.png>)

![image 87](<2017-ihringer-regular-intersecting-families_images/imageFile87.png>)

![image 88](<2017-ihringer-regular-intersecting-families_images/imageFile88.png>)

We start with a construction of some auxiliary family Q′ which satisﬁes |Q′| = |Q|. The ﬁrst part of Q′ is the family Q(2k−1) of all sets containing the element 2k−1 except for the sets Ai. This accounts for 2kk−−22 −3 sets, and we have to choose 12( 2kk−−11 −3)− 2kk−−22 +3 = 2k1−2 2kk−−22 +23 sets more. The remaining sets we choose out of [2kk−−12] in such a way that the degrees of the elements in [2k − 2] diﬀer by at most one and are non-decreasing as i ∈ [2k − 2] increases. This could be done as follows (the same idea was used in the proof of Theorem 1 in [2]).

![image 89](<2017-ihringer-regular-intersecting-families_images/imageFile89.png>)

![image 90](<2017-ihringer-regular-intersecting-families_images/imageFile90.png>)

![image 91](<2017-ihringer-regular-intersecting-families_images/imageFile91.png>)

We start with any family Q′′ in [2kk−−12] of needed size. Then, if there are g,h ∈ [2k − 1], such that the degree of g is bigger than the degree of h by at least 2, then we take a set A, such that g ∈ A, h ∈/ A, and A′ := {h} ∪ A \ {g} is not in the family, and replace A with A′. We call such an operation a (g,h)-replacement. Repeating this procedure will eventually lead to a family Q(2k − 1), in which any two degrees diﬀer by at most 1. We may also w.l.o.g. assume that elements are ordered from the ones with the smaller degree to the ones with the larger degree.

![image 92](<2017-ihringer-regular-intersecting-families_images/imageFile92.png>)

The resulting family is Q′ := Q(2k − 1) ∪ Q(2k − 1). Due to the fact that Ai ∈/ Q(2k − 1), the degrees of the ﬁrst 3k/2 elements are bigger by 2 than the degrees of 3k/2 + 1,... ,2k − 2. However, the degree of any i ∈ [3k/2] in Q′ is at most

![image 93](<2017-ihringer-regular-intersecting-families_images/imageFile93.png>)

k − 32 2k − 2

2k − 3 k − 3 − 1 +

2k − 2 k − 2

2k − 2 k − 2

- 1

![image 94](<2017-ihringer-regular-intersecting-families_images/imageFile94.png>)

- 2


- 1

![image 95](<2017-ihringer-regular-intersecting-families_images/imageFile95.png>)

- 2k − 2


3 2 ≤

- 1

![image 96](<2017-ihringer-regular-intersecting-families_images/imageFile96.png>)

- 2


![image 97](<2017-ihringer-regular-intersecting-families_images/imageFile97.png>)

.

+

+

![image 98](<2017-ihringer-regular-intersecting-families_images/imageFile98.png>)

![image 99](<2017-ihringer-regular-intersecting-families_images/imageFile99.png>)

where the ﬁrst term in the left hand side is the degree of 1 in Q(2k − 1) and the second term is the upper integer part of the average degree in Q(2k − 1). The right hand side is at most the right hand side of (10) plus 1 (which should be the degree of i ∈ [3k/2] in Q), since the diﬀerence is 4k1−4 2kk−−22 − 45 ≥ 0 for any k ≥ 4. Similarly, the degree of each element in [3k/2 + 1,2k − 2] in Q′ is at most what it should be in Q.

![image 100](<2017-ihringer-regular-intersecting-families_images/imageFile100.png>)

![image 101](<2017-ihringer-regular-intersecting-families_images/imageFile101.png>)

![image 102](<2017-ihringer-regular-intersecting-families_images/imageFile102.png>)

This implies that we can obtain the family Q with degrees that diﬀer by at most 1 doing (2k − 1,h)-replacements (and thus transferring the excess of the degree of 2k − 1 to other elements). In particular, since 2k−1 ∈ Ai, it implies that such Q will not contain Ai, i = 1,2,3. The lemma is proven.

![image 103](<2017-ihringer-regular-intersecting-families_images/imageFile103.png>)

![image 104](<2017-ihringer-regular-intersecting-families_images/imageFile104.png>)

![image 105](<2017-ihringer-regular-intersecting-families_images/imageFile105.png>)

![image 106](<2017-ihringer-regular-intersecting-families_images/imageFile106.png>)

## 4.3 The cases n = 2k + 1 and k = 4

Consider the case n = 2k + 1. The bound in Theorem 21 in this case is 2kk−−21 2kk+1 . For k = 3 this is 7 and Theorem 7 states that this is only obtained if F is the Fano plane. It is easy to

![image 107](<2017-ihringer-regular-intersecting-families_images/imageFile107.png>)

see that the bound is always an integer and that the degree in case of equality is the integer

2k−1 · 2kk+1 2kk+1 = 2kk−−21 k 2−k1 . We found examples that reach this bound for k ∈ {3,4}. For k = 3 there is one example, the Fano plane. By computer, we classiﬁed all examples for k = 4

k−2

![image 108](<2017-ihringer-regular-intersecting-families_images/imageFile108.png>)

![image 109](<2017-ihringer-regular-intersecting-families_images/imageFile109.png>)

![image 110](<2017-ihringer-regular-intersecting-families_images/imageFile110.png>)

where there are exactly two regular examples of size 36 up to isomorphism. The following table summarizes our knowledge for small k and n = 2k + 1.

k 3 4 5 6 Theorem 21 7 36 154 624 Largest 7 36 ≥ 110 ≥ 442 δ 3 16 ≥ 50 ≥ 204

![image 111](<2017-ihringer-regular-intersecting-families_images/imageFile111.png>)

![image 112](<2017-ihringer-regular-intersecting-families_images/imageFile112.png>)

![image 113](<2017-ihringer-regular-intersecting-families_images/imageFile113.png>)

As we know the complete situation for k = 3, here is a table of computer results for k = 4. The general bound refers to either Theorem 21 (including improvements due to the fact that the size of the regular intersecting family and its degree are integers), or to Theorem 7.

n 8 9 10 11 12 13 General Bound 34 36 35 33 33 13 Largest 32 36 20 11 ≥ 12 13 δ 16 16 8 4 ≥ 4 4

![image 114](<2017-ihringer-regular-intersecting-families_images/imageFile114.png>)

![image 115](<2017-ihringer-regular-intersecting-families_images/imageFile115.png>)

![image 116](<2017-ihringer-regular-intersecting-families_images/imageFile116.png>)

# 5 Conclusion

All known ﬁnite projective planes have a prime power as order. It is a famous and long-standing open problem to decide whether there exist projective planes which do not have prime power order. In light of this it is clear that determining the existence of regular k-uniform intersecting families is hard for n = k2 − k + 1.

There are several other problems for which it seems to be more feasible to obtain new results. We list some of them below.

The Bruck-Ryser-Chowla theorem [4] implies that if there is a projective plane of order k−1 and k − 1 is congruent 1 or 2 modulo 4, then k − 1 is the sum of two squares. This implies that Theorem 5 is not tight for the orders 6,14,21,22,.... The case of order 10 was ruled out separately by computer [23].

- Question 1. For those k for which the non-existence of a projective plane of order k − 1 is known, what is the largest n for which a regular k-uniform intersecting family exists?
- Question 2. Are there examples for which the bound in Theorem 21 with n ≥ 2k +1 and s = 1 is tight except for (n,k) = (7,3) and (n,k) = (9,4)?1


Theorem 3 is based on the analysis of Boolean functions in the Hamming graph, that means an investigation on how 0-1-vectors can lie in certain eigenspaces of the adjacency matrix of the Hamming graph. It would be very interesting to do this investigation directly in the Johnson scheme with more direct algebraic techniques to obtain a non-asymptotic version of Theorem 9.

![image 117](<2017-ihringer-regular-intersecting-families_images/imageFile117.png>)

1In an earlier version of this document we mistakenly did not specify s = 1. For general s Adam S. Wagner noticed that there exists a 3-regular intersecting family which reaches the bound in Theorem 21, see [29].

# Acknowledgements

The research of the ﬁrst author is supported by ERC advanced grant 320924 and he is supported by a postdoctoral fellowship of the Research Foundation - Flanders (FWO). The research of the second author is supported the grant RNF 16-11-10014.

# References

- [1] B. Bollob´s, B.P. Narayanan and A.M. Raigorodskii. On the stability of the Erd˝os–Ko– Rado theorem. J. Comb. Th. Ser. A 137 (2016), 64–78.
- [2] A. Brace and D. E. Daykin. Sperner-type theorems for ﬁnite sets. In: Combinatorics, D. R. Woodall and D. J. A. Welsh, eds, 18–37, Inst. Maths. Applics., Southend-on-Sea, 1972.
- [3] A. E. Brouwer, A. M. Cohen, and A. Neumaier. Distance-regular graphs, volume 18 of Ergebnisse der Mathematik und ihrer Grenzgebiete (3) [Results in Mathematics and Related Areas (3)]. Springer-Verlag, Berlin, 1989.
- [4] R. H. Bruck, and H. J. Ryser. The nonexistence of certain ﬁnite projective planes. Canad. J. Math., 1:88–93, 1949.
- [5] P. J. Cameron, P. Frankl, and W. M. Kantor. Intersecting families of ﬁnite sets and ﬁxedpoint-free 2-elements. Europ. J. Combin., 10:149–160, 1989.
- [6] P. Delsarte. An algebraic approach to the association schemes of coding theory. Philips Res. Rep. Suppl., (10):vi+97, 1973.
- [7] I. Dinur, E. Friedgut. Intersecting families are essentially contained in juntas. Combin. Probab. Comput. 18 (2009), 107–122.
- [8] D. Ellis, G. Kalai, and B. Narayanan. On symmetric intersecting families. arXiv:1302.3636v3 [math.CO].
- [9] D. Ellis, N. Keller, N. Lifshitz. Stability versions of Erd˝os-Ko-Rado type theorems, via isoperimetry. J. Eur. Math. Soc., to appear.
- [10] P. Erd˝os, C. Ko, and R. Rado. Intersection theorems for systems of ﬁnite sets. Quart. J. Math. Oxford Ser. (2), 12:313–320, 1961.
- [11] P. Frankl. Erdos-Ko-Rado theorem with conditions on the maximal degree. J. Combin. Theory Ser. A 46 (1987), N2, 252–263.
- [12] P. Frankl, Z. Fu¨redi. Finite projective spaces and intersecting hypergraphs. Combinatorica 6(4) (1986), 335–354.
- [13] E. Friedgut and G. Kalai. Every monotone graph property has a sharp threshold. Proc. Amer. Math. Soc. 124 (1996), 2993–3002.
- [14] Z. Fu¨redi. Maximum degree and fractional matchings in uniform hypergraphs. Combinatorica 1 (1981), 155–162.
- [15] Z. Fu¨redi. Erd˝os-Ko-Rado Type Theorems with upper bounds on the maximum degree. In: Algebraic Methods in graph theory, (Szeged, Hungary, 1978), L. Lov´as et al. eds. Proc. Colloq. Math. Soc. J. Bolyai 25, North-Holland, Amsterdam 1981, 177–207.


- [16] Z. Fu¨redi. Covering pairs by q2+q+1 sets. J. Combin. Theory, Ser. A 54 (1990), 248–271.
- [17] C. Godsil and K. Meagher. Erdo˝s-Ko-Rado Theorems: Algebraic Approaches. Number 149 in Cambridge Studies in Advanced Mathematics. Cambridge Univ. Press, December 2016.
- [18] A.J.W. Hilton, E.C. Milner. Some intersection theorems for systems of ﬁnite sets. Quart. J. Math. Oxford 18 (1967), 369–384.
- [19] P. Keevash, D. Mubayi. Set systems without a simplex or a cluster. Combinatorica, 30(2)

(2010), 175–200.

- [20] N. Keller, N. Lifshitz. The Junta Method for Hypergraphs and Chv´atal’s Conjecture. Electron. Notes Discrete Math., 61 (2017), 711–717.
- [21] S. Kiselev, A. Kupavskii. Sharp bounds for the chromatic number of random Kneser graphs and hypergraphs arXiv:1810.01161
- [22] A. Kupavskii, D. Zakharov. Regular bipartite graphs and intersecting families. J. Comb. Theory Ser. A 155 (2018), 180–189.
- [23] C. W. H. Lam, L. Thiel, and S. Swiercz. The nonexistence of ﬁnite projective planes of order 10. Canad. J. Math., 41(6):1117–1123, 1989.
- [24] L. Lov´asz. On minmax theorems of combinatorics (in Hungarian). Matematikai Lapok, 26

(1975), 209–264.

- [25] L. Lov´asz. Doctoral thesis (in Hungarian), Szeged 1977.
- [26] M. Pyaderkin. On the stability of some Erdos-Ko-Rado type results Discrete Math., 340(4)

(2017), 822–831.

- [27] A. M. Raigorodskii. On the stability of the independence number of a random subgraph. Dokl. Math. 96(3) (2017), 628–630.
- [28] D. K. Ray-Chaudhuri, R. M. Wilson. On t-designs. Osaka Journal of Mathematics, 12(3)

(1975), 737–744.

- [29] A. Z. Wagner. Refuting conjectures in extremal combinatorics via linear programming. arXiv:1903.05495.


