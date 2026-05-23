arXiv:1409.3606v1[math.CO]11Sep2014

Cross-Intersecting Erdo˝s-Ko-Rado Sets in Finite Classical Polar Spaces

Ferdinand Ihringer

Abstract. A cross-intersecting Erd˝s-Ko-Rado set of generators of a ﬁnite classical polar space is a pair (Y, Z) of sets of generators such that all y ∈ Y and z ∈ Z intersect in at least a point. We provide upper bounds on |Y | · |Z| and classify the cross-intersecting Erd˝s-Ko-Rado sets of maximum size with respect to |Y | · |Z| for all polar spaces except Hermitian polar spaces in odd projective dimension.

1. Introduction

Erdo˝s-Ko-Rado sets (EKR sets) were introduced by Erdo˝s, Ko, and Rado [6] as a set Y of k-element subsets of {1,...,n} such that the elements of Y pairwise intersect non-trivially. In particular, Erdo˝s, Ko, and Rado partially classiﬁed all such Y of maximum size.

Theorem 1.1 (Theorem of Erdo˝s, Ko, and Rado). Let be n ≥ 2k. Let Y be an EKR set of k-element subsets of {1,...,n}. Then

n − 1 k − 1

|Y | ≤

with equality for n > 2k if and only if Y is set of all k-elemental sets containing a ﬁxed element.

Stronger versions of this theorem were later proven by several authors including the famous work by Wilson [19], Ahlswede and Khachatrian [1].

This theorem for EKR sets was generalized to many structures, including subspaces of projective spaces [12, 7, 3] and generators (maximal totally isotropic, respectively, singular subspaces) of polar spaces [16, 3, 4]. In polar spaces the problem is partially open, since the maximum size of EKR sets of generators of H(2d−1,q2), d > 3 odd, is still unknown. To the knowledge of the author the best known upper bound is given in [13].

There exists the following modiﬁcation of the original problem which generated a lot of interest: a cross-intersecting EKR set is a pair (Y,Z) of sets of subsets with k elements of {1,...,n} such that all y ∈ Y and z ∈ Z intersect non-trivially. If one wants to generalize the theorem of Erdo˝s, Ko, and Rado to this structure, then the following question arises: how do we measure the size of (Y,Z)? There are at least two natural choices. Either one goes for an upper bound for |Y | + |Z| or one tries to ﬁnd the upper bound for |Y |·|Z|. In the set case the ﬁrst project was pursued in [9], while the second one was completed in [15]. Results for vectors spaces are due to Tokushige [17]. Again this problem can be generalized to polar spaces, where

![image 1](<2014-ihringer-cross-intersecting-erd-s-ko-rado-sets_images/imageFile1.png>)

1991 Mathematics Subject Classiﬁcation. 51E20; 05B25. Key words and phrases. Erd˝s-Ko-Rado Theorem; Polar Space; Association Scheme; Cross-

intersecting Family.

1

an cross-intersecting EKR set of generators is a pair (Y,Z) of sets of generators such that all y ∈ Y and z ∈ Z intersect in at least a point. In this setting this paper is only concerned with an upper bound for |Y | · |Z| and a classiﬁcation of all cross-intersecting EKR sets reaching this bound.

One additional motivation for this problem is the following: as mentioned before the problem of EKR sets of maximum size in H(2d − 1,q2) is still open for d > 3 odd. Let P be a point of H(2d − 1,q2) and let X be an EKR set of H(2d − 1,q2). Furthermore, let Y be the set of generators of X on P and Z the set of generators of X not on P. Now in the quotient geometry of P isomorphic to H(2d − 3,q2) the projection of the generators of Y and Z onto the quotient geometry is a crossintersecting EKR set. So both problems are related.

One last thing to point out is that this work does not provide tight upper bounds for cross-intersecting EKR sets in H(2d − 1,q2) for all d > 1. The problem is very similar to the open problem of the maximum size of EKR sets in H(9,q2). Therefore, it could be reasonable to ﬁrst solve the problem of the maximum size of cross-intersecting EKR sets in H(7,q2) and then generalize the technique to EKR sets in H(9,q2).

2. Projective Spaces & Polar Spaces

We refer to [10] for details on projective spaces. A projective space PG(n−1,q) of projective dimension n − 1 (respectively vector space dimension n) over the ﬁeld with q elements has exactly

k

qn−i+1 − 1 qi − 1

n k q

:=

![image 3](<2014-ihringer-cross-intersecting-erd-s-ko-rado-sets_images/imageFile3.png>)

i=1

subspaces of (vector space) dimension k. We denote the number of points in PG(n− 1,q) by

[n]q :=

n 1 q

.

So we have

n k q

k

[n − i + 1]q [i]q

.

=

![image 4](<2014-ihringer-cross-intersecting-erd-s-ko-rado-sets_images/imageFile4.png>)

i=1

We shall write nk instead of nk q whenever the choice for q is clear. We will often use the following analog of the recursive deﬁnition of binomial coeﬃcients.

(2.1)

n + 1 k + 1

=

n k + 1

+ q(n−k)

n k

Remark 2.2. All the used eigenvalue formulas are more convenient if we use vector space dimensions and not projective dimensions. Consequently, the word dimension will always refer to the vector space dimension of a subspace.

A polar space is a incidence geometry with subspaces of dimension from 0 to d deﬁned by a non-degenerate sesquilinear form or a non-degenerate quadratic form. The ﬁnite classical polar spaces are Q+(2d − 1,q), Q(2d,q), Q−(2d + 1,q), W(2d − 1,q), where q is a prime power, H(2d − 1,q), and H(2d,q), where q is the square of a prime power. We refer to [11] for details. Denote totally isotropic, respectively, singular subspaces of (vector space) dimension d as generators. Each subspace of (vector space) dimension d − 1 of a polar space is incident with exactly qe + 1 generators, where e = 0 for Q+(2d − 1,q), e = 1/2 for H(2d − 1,q), e = 1 for

Q(2d,q) and W(2d − 1,q), e = 3/2 for H(2d,q), and e = 2 for Q−(2d + 1,q). It is well known that a polar space possesses exactly

d−1

(qi+e + 1)

i=0

generators and (qd+e−1 + 1)[d] points (i.e. 1-dimensional totally isotropic, respectively, singular subspaces).

3. The Association Scheme of a Polar Space

We need some basic properties of an association scheme of generators on a dual polar space of rank d and type e. A complete introduction to association schemes can be found in [2, Ch. 2].

Definition 3.1. Let X be a ﬁnite set. A d-class association scheme is a pair (X,R), where R = {R0,...,Rd} is a set of symmetric binary relations on X with the following properties:

- (1) {R0,...,Rd} is a partition of X × X.
- (2) R0 is the identity relation.
- (3) There are numbers pkij such that for x,y ∈ X with xRky there are exactly pkij elements z with xRiz and zRjy.


The number ni := p0ii is called the i-valency of Ri. The total number of elements of X is

d

n := |X| =

ni.

i=0

The relations Ri are described by their adjacency matrices Ai ∈ Cn,n deﬁned by

(Ai)xy =

1 if xRiy 0 otherwise.

There exist (e.g. in [2, p. 45]) idempotent Hermitian matrices Ej ∈ Cn,n (hence they are positive semideﬁnite) with the properties

d

Ej = I, E0 = n−1J,

j=0

d

d

1 n

QijAi,

PijEi, Ej =

Aj =

![image 6](<2014-ihringer-cross-intersecting-erd-s-ko-rado-sets_images/imageFile6.png>)

i=0

i=0

where P = (Pij) ∈ Cd+1,d+1 and Q = (Qij) ∈ Cd+1,d+1 are the so-called eigenmatrices of the association scheme.

The generators of a polar space deﬁne an association scheme if we say that two generators a and b are in relation Ri if and only if codim(a ∩ b) = i. Hence a cross-intersecting EKR set (Y,Z) is a set of vertices such that there are no edges between Y and Z in the (distance-regular) graph associated with Ad. This scheme is cometric, so there exists a natural ordering of its Ej’s and its eigenspaces Wj [2, Sec. 2.7, Sec. 9.4]. The matrix P can be found in the literature (for example in [18, Theorem 4.3.6]). In particular, the eigenvalues of Ad are

(−1)rq(d−r

)+(r

(3.2) )+e(d−r)

2

2

for r ∈ {0,1,...,d}. Here W0 = j , where j is the all-one vector. Furthermore, notice that all eigenspaces Wi of an association scheme are pairwise orthogonal (see [2, Ch. 2]).

4. An Algebraic Bound

We shall apply a technique that was, to the knowledge of the author, ﬁrst used by Willem H. Haemers in [8]. The author learned about this technique from a paper by Tokushige [17], where he uses a variant of the result based on the work of Ellis, Friedgut, and Pipel [5] to prove a result on EKR sets of permutations. Let G be a graph with n vertices {1,...,n}. A matrix A = (axy) ∈ Cn×n is called extended weight adjacency matrix of G if A is symmetric, and

- (1) axy ≤ 0 if x and y are non-adjacent,
- (2) axx = 0,
- (3) the all-ones vector j is an eigenvector of A.
- (4) A is not the all-zero matrix.


Let λ1,...,λn be the (possibly pairwise equal) eigenvalues of A. Denote the eigenvalue of j by k. Denote the smallest eigenvalue by λ−, and the corresponding eigenspace by V−. Denote the largest eigenvalue with eigenvectors not in j by λ+. Denote the corresponding eigenspace by V+ if k = λmax, and by j ⊥ V+ if k = λmax. Denote max{−λ−,λ+} by λb. We say that λb is the second largest absolute eigenvalue of A.

A characteristic vector χY of a subset Y ⊆ {1,...,n} is deﬁned by

χi =

1 if i ∈ Y 0 if i ∈/ Y

.

Ellis, Friedgut, and Pipel used the following result, a generalization of the Hoﬀman bound for cocliques in graphs:

Lemma 4.1. Let A be an extended weight adjacency matrix of a regular graph G with n vertices. Let k be the eigenvalue of the all-one vector j, and let λb the second largest absolute eigenvalue of A. Let Y and Z be sets of vertices such that there are no edges between Y and Z. Then

λb k + λb

![image 8](<2014-ihringer-cross-intersecting-erd-s-ko-rado-sets_images/imageFile8.png>)

|Y | · |Z| ≤

n.

![image 9](<2014-ihringer-cross-intersecting-erd-s-ko-rado-sets_images/imageFile9.png>)

Remark 4.2. Very often the Hoﬀman bound is only formulated for so-called weight adjacency matrices or pseudo adjacency matrices where aij is zero if i and j are non-adjacent and aij > 0 if i and j are adjacent. It is regularly mentioned in the literature and easy to see that all the proofs for variants of the Hoﬀman bound (at least the ones used in this paper) also work for extended adjacency matrices without changing much of the proof. The Hoﬀman bound for an extended weight matrix A is optimal only if A is also a weight matrix. Our more general deﬁnition will turn out to be more convenient in Section 6 where we shall not bother to calculate the exact minimum of the Hoﬀman bound.

Tokushige reformulates Lemma 4.1 in a more detailed way in [17], Lemma 2. Unfortunately, his reformulation misses to point out some details necessary for the special case handled in this paper. Hence, we have to restate his wording of the following lemma.

Lemma 4.3. Suppose that equality holds in Lemma 4.1. Then one of the following cases occurs:

- (a) We have λ+ = λb > −λ−, χY = αj + v+, and χZ = αj − v+ for some vector v+ ∈ V+.
- (b) We have λ+ < λb = −λ−, χY = αj + v−, and χZ = αj + v− for some vector v− ∈ V−. In this case Y = Z, and Y is an EKR set.
- (c) We have λ+ = λb = −λ−, χY = αj + v− + v+, and χZ = αj + v− − v+ for some vectors v− ∈ V− and v+ ∈ V+.


Furthermore, |Y | = |Z| = αn.

Proof. The proof of Lemma 2 in [17] still works for the ﬁrst three claims if one reads it carefully. For the claim |Y | = |Z| consider the following: j is orthogonal to to v− and v+. Hence,

|Y | = χTY j = αn = χTZj = |Z|.

5. Cross-intersecting EKR Sets of Maximum Size

In this section we shall calculate tight upper bounds for all polar spaces except H(2d − 1,q2), and classify all examples in case of equality. For all polar spaces except H(2d − 1,q2) we can imitate the approach of Pepe, Storme, and Vanhove [16]. Recall from Section 3 that we have a natural ordering of the eigenspaces W0(= j ),W1,...,Wd of the association scheme which we deﬁned on generators of a polar space of rank d.

Theorem 5.1. Let (Y,Z) be a cross-intersecting EKR set of generators of a polar space P. Let n be the number of generators of P. Then we have the following:

- • If P = Q+(2d − 1,q), then |Y | · |Z| is at most n/2, and if this bound is reached, then χY ,χZ ∈ W0 ⊥ Wd.

![image 11](<2014-ihringer-cross-intersecting-erd-s-ko-rado-sets_images/imageFile11.png>)

- • If P ∈ {Q(2d,q),W(2d − 1,q)}, then |Y | · |Z| is at most the number of generators on a ﬁxed point, and if this bound is reached, then χY ,χZ ∈ W0 ⊥ W1 ⊥ Wd.

![image 12](<2014-ihringer-cross-intersecting-erd-s-ko-rado-sets_images/imageFile12.png>)

- • If P ∈ {H(2d,q),Q−(2d + 1,q)}, then |Y | · |Z| is at most the number of generators on a ﬁxed point, and if this bound is reached, then χY ,χZ ∈ W0 ⊥ W1.


![image 13](<2014-ihringer-cross-intersecting-erd-s-ko-rado-sets_images/imageFile13.png>)

Proof. To apply Lemma 4.1, we have to calculate the second largest absolute eigenvalue of the disjointness graph (with associated adjacency matrix Ad). The eigenvalues of Ad were given in (3.2) as

(−1)rq(d−r

)+(r

)+e(d−r).

2

2

For r = 0 this is the eigenvalue which belongs to the all-one vector j, so with k deﬁned as in Lemma 4.1 we have

k = q(d

)+de.

2

For e = 0 note that the absolute eigenvalues for r = 0 and r = d are equal. Therefore, the eigenspace belonging to k has dimension at least 2 which make k also the second largest absolute eigenvalue. Hence, we have the following for the diﬀerent polar spaces. For e = 0 (i.e. P = Q+(2d−1,q)) the second largest absolute eigenvalue occurs if and only if r = d, for e = 1 (i.e. P ∈ {Q(2d,q),W(2d−1,q)}) the second largest absolute eigenvalue occurs if and only if r ∈ {1,d}, for e ∈ {3/2,2} (i.e. P ∈ {H(2d,q),Q−(2d+ 1,q)}) the second largest absolute eigenvalue occurs if and only if r = 1. Applying Lemma 4.1 and Lemma 4.3 yields the assertion.

Using Lemma 4.3 and the classiﬁcation of EKR sets of generators given in [16] we get the following result.

Corollary 5.2. Let (Y,Z) be an cross-intersecting EKR set of a ﬁnite classical polar space P not isomorphic to Q(2d,q) with d even, W(2d − 1,q) with d even, Q+(2d−1,q) with d even, or H(2d,q2), where |Y |·|Z| reaches the bound in Theorem 5.1. Then Y = Z, and Y is an EKR set.

Proof. For the stated cases, the eigenspaces given in Theorem 5.1 (not equal to j ) belong to negative eigenvalues. By Lemma 4.3, then all cross-intersecting EKR which reach the bound given in Theorem 5.1 are EKR sets.

Similar to [16] we shall continue to classify the more complicated cases.

5.1. The Hyperbolic Quadric, d even. The generators of Q+(2d−1,q) can be partitioned into two sets X1 and X2 of generators (commonly known as latins and greeks) with |X1| = |X2| = n/2. For x1 ∈ X1 and x2 ∈ X2 the codimension of the intersection of x∩y is odd. For x1,x2 ∈ X1 the codimension of the intersection of x ∩ y is even. This implies for d even that (X1,X2) is a cross-intersecting EKR set of maximum size according to Theorem 5.1. There exist x1,x2 ∈ X1 with dim(x1 ∩ x2) = 0 if d is even, so (X1,X1) is not a cross-intersecting EKR set.

Theorem 5.3. Let (Y,Z) be an cross-intersecting EKR set of maximum size of Q+(2d − 1,q) with d even. Then Y = Xi and Z = Xj for {i,j} = {1,2}.

Proof. By Theorem 5.1, we have χY ,χZ ∈ W0 ⊥ Wd. As in Theorem 16 of [16] W0 is spanned by χX

− χX

. Hence χY ,χZ ∈ {χX

, and Wd is spanned by χX

+ χX

2

1

2

1

} as χY ,χZ,χX

= j. Hence without loss of generality Y = X1. Since (X1,X1) is not a cross-intersecting EKR set, we have Z = X2.

+ χX

are 0-1-vectors with χX

,χX

,χX

2

1

2

1

2

1

5.2. The Parabolic Quadric and the Symplectic Polar Space, d even. If a cross-intersecting EKR set (Y,Z) of Q(2d,q) satisﬁes χY ,χZ ∈ W0 ⊥ W1, then Y = Z, and Y is an EKR set as before. So only the case χY ,χZ ∈ W0 ⊥ W1 ⊥ Wd remains. In the following denote W1 by V− and Wd by V+. Furthermore, as in Lemma 4.3 we write

χY = αj + v− + v+

|Y | n

=

j + v− + v+

![image 15](<2014-ihringer-cross-intersecting-erd-s-ko-rado-sets_images/imageFile15.png>)

λb k + λb

j + v− + v+ and

=

![image 16](<2014-ihringer-cross-intersecting-erd-s-ko-rado-sets_images/imageFile16.png>)

χZ = αj + v− + v+

|Z| n

=

j + v− + v+

![image 17](<2014-ihringer-cross-intersecting-erd-s-ko-rado-sets_images/imageFile17.png>)

λb k + λb

j + v− − v+ with v− ∈ V− and v+ ∈ V+. We need the following well-known lemma.

=

![image 18](<2014-ihringer-cross-intersecting-erd-s-ko-rado-sets_images/imageFile18.png>)

Lemma 5.4. Let χ ∈ j ⊥ V for some eigenspace V of an (extended weight) adjacency matrix of a k-regular graph with n vertices associated with eigenvalue λ. Then the characteristic vector ei of the i-th vertex satisﬁes

χTj n

(k − λ) + λeTi χ.

eTi Aχ =

![image 19](<2014-ihringer-cross-intersecting-erd-s-ko-rado-sets_images/imageFile19.png>)

Proof. As χ ∈ j ⊥ V , we can write χ = αj + v for some v ∈ V and α = χ

T j n . Then

![image 20](<2014-ihringer-cross-intersecting-erd-s-ko-rado-sets_images/imageFile20.png>)

eTi Aχ = eTi A(αj + v)

= eTi (αkj + λv)

= eTi (α(k − λ)j + λχ)

χTj n

(k − λ) + λeTi χ.

=

![image 21](<2014-ihringer-cross-intersecting-erd-s-ko-rado-sets_images/imageFile21.png>)

Corollary 5.5. Let χ,ψ ∈ j ⊥ V− ⊥ V+ for some eigenspaces V−, respectively, V+ of a (extended weight) adjacency matrix of the graph with eigenvalue λ−, respectively, λ+. If χ = αj + v− + v+ and ψ = αj + v− − v+ for some α ∈ R, v− ∈ V−, and v+ ∈ V +, then

(χ + ψ)Tj 2n

(λ− + λ+) 2

eTi χ

eTi Aχ =

(k − λ−) +

![image 23](<2014-ihringer-cross-intersecting-erd-s-ko-rado-sets_images/imageFile23.png>)

![image 24](<2014-ihringer-cross-intersecting-erd-s-ko-rado-sets_images/imageFile24.png>)

(χ + ψ)Tj 2n

(λ− − λ+) 2

eTi Aψ =

eTi ψ

(k − λ−) +

![image 25](<2014-ihringer-cross-intersecting-erd-s-ko-rado-sets_images/imageFile25.png>)

![image 26](<2014-ihringer-cross-intersecting-erd-s-ko-rado-sets_images/imageFile26.png>)

Proof. We have χ + ψ ∈ j ⊥ V− and χ − ψ ∈ V+. By Lemma 5.4 and jTv− = 0 = jTv+,

(χ + ψ)Tj n

(k − λ−) + λ−eTi (χ + ψ) eTi A(χ − ψ) = λ+eTi (χ − ψ).

eTi A(χ + ψ) =

![image 27](<2014-ihringer-cross-intersecting-erd-s-ko-rado-sets_images/imageFile27.png>)

Now the equations 2eTi Aχ = eTi A(χ+ψ)+eTi A(χ−ψ) and 2eTi Aψ = eTi A(χ+ψ)− eTi A(χ − ψ) yield the assertion.

Lemma 5.6. For the adjacency matrix Ad−s, 0 < s < d, the eigenspace W1 is associated with eigenvalue

λ−,s := −

d − 1 s

q(d−s

) +

2

d − 1 s − 1

q(d−s+1

),

2

the eigenspace Wd is associated with eigenvalue λ+,s := (−1)d−s

d s

q(d−s

), and

2

d − 1 s

d − 1 s − 1

d s

qd−s q(d−s+1

q(d−s+1

).

) =

ks :=

+

2

2

Proof. See [18, Theorem 4.3.6], where the eigenvalue of Wj for Ai is given by

(−1)j+u

0,j−i≤u≤d−i,j

d − j d − i − u

j u

).

q(u+i−j)(u+i−j+2e−1)/2+(

j−u 2

For j = 1, respectively, j = d, and i = d − s, this formula yields the assertion. The last equality is an application of (2.1).

Proposition 5.7. Let (Y,Z) be a cross-intersecting EKR set of Q(2d,q) or W(2d − 1,q), d even, of maximum size such that Y ∩ Z = Y . Let G ∈ Y .

- (a) If d − s is even, then G meets 0 elements of Z in dimension s.
- (b) If d − s is odd, then G meets 0 elements of Y in dimension s.
- (c) If d − s is even, then G meets

d s

q(

d−s 2

)

- elements of Y in dimension s.

(d) If d − s is odd, then G meets

d s

q(

d−s 2

)

- elements of Z in dimension s.




In particular, Y ∩ Z = ∅.

Proof. We can calculate these numbers with Lemma 5.6 and Corollary 5.5 by choosing χ{G} as ei. For Ad−s the parameters are given by

d − 1 s

d − 1 s − 1

d−s+1 2

)

qd−s q(

ks − λ−,s =

+

d − 1 s

d − 1 s − 1

q(d−s+1

q(d−s

) −

)

+

2

2

) d − 1 s

) d − 1 s − 1

d−s+1 2

= q(

qd−s + 1 + q(

d−s 2

qd−s − 1

) d − 1 s

) d − 1 s

Def.= q(d−s

qd−s + 1 + qd−s · q(d−s

(qs − 1)

2

2

) d − 1 s

= q(

d−s 2

qd + 1 ,

for d − s even

d − 1 s − 1

λ−,s + λ+,s (2.1)= 2

q(d−s+1

),

2

d − 1 s

λ−,s − λ+,s (2.1)= −2

),

q(

d−s 2

for d − s odd

d − 1 s

λ−,s + λ+,s (2.1)= −2

d − 1 s − 1

λ−,s − λ+,s (2.1)= 2

q(

q(d−s

),

2

d−s+1 2

).

By assumption (Y,Z) is of maximum size, so by Lemma 4.3 (recall λ+ = λ+,0, and λ− = λ−,0)

Hence,

nλ+ k + λ+

χTZj = |Z| = |Y | = χTY j =

.

![image 29](<2014-ihringer-cross-intersecting-erd-s-ko-rado-sets_images/imageFile29.png>)

(χY + χZ)Tj 2n

=

![image 30](<2014-ihringer-cross-intersecting-erd-s-ko-rado-sets_images/imageFile30.png>)

λ+ k + λ+

=

![image 31](<2014-ihringer-cross-intersecting-erd-s-ko-rado-sets_images/imageFile31.png>)

Hence by Corollary 5.5,

q(d

) q(d+1

2

=

![image 32](<2014-ihringer-cross-intersecting-erd-s-ko-rado-sets_images/imageFile32.png>)

) + q(d

)

2

2

1 qd + 1

.

![image 33](<2014-ihringer-cross-intersecting-erd-s-ko-rado-sets_images/imageFile33.png>)

ks − λ−,s qd + 1

(λ− + λ+) 2

eTi χ

eTi Aχ =

+

![image 34](<2014-ihringer-cross-intersecting-erd-s-ko-rado-sets_images/imageFile34.png>)

![image 35](<2014-ihringer-cross-intersecting-erd-s-ko-rado-sets_images/imageFile35.png>)

) d − 1 s

(λ− + λ+) 2

= q(d−s

eTi χ.

+

2

![image 36](<2014-ihringer-cross-intersecting-erd-s-ko-rado-sets_images/imageFile36.png>)

If d − s is even and eTi χ = 1, then by (2.1)

) d − 1 s

eTi Aχ = q(

d−s 2

d−s+1 2

+ q(

) d − 1 s − 1

) d s

= q(

d−s 2

.

If d − s is odd and eTi χ = 1, then

) d − 1 s

) d − 1 s

− q(d−s

eTi Aχ = q(d−s

= 0. All the remaining cases are either similar or trivial.

2

2

Now we have a strong combinatorial information about cross-intersecting EKR sets (Y,Z) of maximum size which are not EKR sets. By adding some geometrical arguments this leads to a complete classiﬁcation of cross-intersecting EKR sets in these parabolic and symplectic polar spaces as we shall see in the following.

Lemma 5.8. Let (Y,Z) be a cross-intersecting EKR set of Q(2d,q) or W(2d − 1,q), d even, of maximum size. Let G,H ∈ Y disjoint (see Proposition 5.7 (c)). Let π1,...,π[d] ⊆ G be the [d] subspaces of dimension d−1 of G. Then the following holds:

- (a) Exactly [d] elements z1,...,z[d] of Z meet G in dimension d − 1.
- (b) We have {zi | i ∈ {1,...,[d]}} = { πi,πi⊥ ∩ H | i ∈ {1,...,[d]}}. Proof. By Proposition 5.7 (d) and Y = Z, exactly [d] elements of Z meet Y


in dimension d − 1. This shows (a). By Proposition 5.7 (b), dim(zi ∩ zj) < d − 1 for i = j. Hence, each hyperplane πi lies in exactly one element zj, and zj satisﬁes zj ⊆ πi⊥. Since (Y,Z) is a cross-intersecting EKR set, all zj meet H in at least a point. Since πi ⊆ G and G ∩ H = ∅, we see that πi⊥ ∩ H is a point. Hence,

{zi | i ∈ {1,...,[d]}} = { πi,πi⊥ ∩ H | i ∈ {1,...,[d]}}.

We write (5.9) ZG,H = {{zi | i ∈ {1,...,[d]}}

= { πi,πi⊥ ∩ H | i ∈ {1,...,[d]}} ⊆ Z for G,H ∈ Y whenever Lemma (5.8) in applicable.

5.2.1. The Parabolic Quadric Q(2d,q). Let h be a subspace of PG(2d,q). We write Y ⊆ h if all elements of Y are subspaces of h, Y ∩ h for all elements of Y in h, and Y \ h for all elements of Y not in h.

Lemma 5.10. Let G and H be disjoint generators of Q(2d,q). Then h := G,H ∩ Q(2d,q) is isomorphic to Q+(2d − 1,q).

Proof. The generators G and H are disjoint, hence h ∩ Q(2d,q) is not degenerate. The hyperplane h obviously contains generators, hence h ∩ Q(2d,q) does not have type Q−(2(d−1)+1,q). Therefore, the intersection h∩Q(2d,q) is isomorphic to Q+(2d − 1,q).

Lemma 5.11. Let (Y,Z) be a cross-intersecting EKR set of Q(2d,q), d even, of maximum size such that Y ∩ Z = Y . Let G ∈ Y . Let Y˜ be the set of the q(d

) generators of Y disjoint to G (see Proposition 5.7).

2

- (a) There exists a hyperplane h of type Q+(2d − 1,q) such that G,Y˜ ⊆ h.
- (b) If G˜ ∈ Y \ h, then G˜ meets all elements of Y˜ non-trivially.
- (c) If G˜ ∈ Y and dim(G˜∩H) = d−2 for any H ∈ Y˜, then G˜ and the q(d


) generators

2

disjoint to G˜ are in h. Proof. By Proposition 5.7, a generator G ∈ Y is disjoint to q(d

) generators

2

- of Y . Let H ∈ Y˜. By Lemma 5.10, h := G,H has type Q+(2d − 1,q). We shall show Y˜ ⊆ h.


Suppose to the contrary that there exists a generator H˜ ∈ Y˜ not in h. We deﬁne ZG in (5.9) by

ZG = ZG,H

= {zi | i ∈ {1,...,[d]}} ⊆ Z. Set

P := {H˜ ∩ zi | i ∈ {1,...,[d]}}.

The generators of ZG intersect G in a hyperplane of G, hence P is a set of points. For i = j we have G ⊆ zi∩G,zj∩G ⊥, so (zi∩zj)\G is empty. Hence, |P| = |ZG| = [d]. Furthermore, ZG ⊆ h, so P ⊆ H˜ ∩ h. Hence,

[d] = |P| ≤ |H˜ ∩ h| = [d − 1]. This is a contradiction. Thus, Y˜ ⊆ h. This proves (a).

Assume that there exists a generator G˜ ∈ Y \ h with dim(H ∩ G˜) = 0. Then, by (a), H is only disjoint to generators of Y in G,H ˜ . Hence, G,H ˜ = G,H . This contradicts G˜ ∈ Y \ h. This proves (b).

Suppose that there exists a generator G˜ ∈ Y \ h with dim(H ∩ G˜) = d − 2. By (b) and Proposition 5.7, dim(G ∩ G˜) ≥ 2. Hence,

G˜ = H ∩ G,G˜ ∩ G˜ ⊆ h,

which contradicts G˜ h. This shows G˜ ∈ Y˜. By (a), all elements disjoint to G˜ are in G,G˜ = h.

We need the following bound. Lemma 5.12. Let q ≥ 2. Let d ≥ 1. Then

d−1

2qd qd + 1

(qi + 1) ≤

![image 39](<2014-ihringer-cross-intersecting-erd-s-ko-rado-sets_images/imageFile39.png>)

i=1

) + 1 + q(d−2

) − q(d−1

q(d

)+2(d−2).

2

2

2

Proof. We will prove the assertion by induction over d. It can be easily checked that the assertion is true for d ≤ 4. If the assertion is true for d ≥ 4, then

d

2qd qd + 1

d−2 2

d−1 2

)+2(d−2)

) + 1 + q(

) − q(

q(

d 2

(qi + 1) ≤ (qd + 1)

![image 40](<2014-ihringer-cross-intersecting-erd-s-ko-rado-sets_images/imageFile40.png>)

i=1

2qd+1 qd+1 + 1

(∗)

d−1 2

d+1 2

)+2(d−1). The diﬀerence between the right hand side of (*) and the left hand side of (*) equals

) + 1 + q(

) − q(

q(

d 2

≤

![image 41](<2014-ihringer-cross-intersecting-erd-s-ko-rado-sets_images/imageFile41.png>)

q−32d−1 qd + 1

![image 42](<2014-ihringer-cross-intersecting-erd-s-ko-rado-sets_images/imageFile42.png>)

(2q

![image 43](<2014-ihringer-cross-intersecting-erd-s-ko-rado-sets_images/imageFile43.png>)

d2

d2

d2

2 +2d+3 − 2q

2 +2d+2 − 3q

2 +2d+1

![image 44](<2014-ihringer-cross-intersecting-erd-s-ko-rado-sets_images/imageFile44.png>)

![image 45](<2014-ihringer-cross-intersecting-erd-s-ko-rado-sets_images/imageFile45.png>)

![image 46](<2014-ihringer-cross-intersecting-erd-s-ko-rado-sets_images/imageFile46.png>)

d2

d2

7d

5d

5d

2 +d+2 − q

2 +d − 2q

2 +2 + 2q

2 +2 − 2q

2 +1)

+ 2q

![image 47](<2014-ihringer-cross-intersecting-erd-s-ko-rado-sets_images/imageFile47.png>)

![image 48](<2014-ihringer-cross-intersecting-erd-s-ko-rado-sets_images/imageFile48.png>)

![image 49](<2014-ihringer-cross-intersecting-erd-s-ko-rado-sets_images/imageFile49.png>)

![image 50](<2014-ihringer-cross-intersecting-erd-s-ko-rado-sets_images/imageFile50.png>)

![image 51](<2014-ihringer-cross-intersecting-erd-s-ko-rado-sets_images/imageFile51.png>)

which is a positive expression for q ≥ 2 and d ≥ 4.

Proposition 5.13. Let (Y,Z) be a cross-intersecting EKR set of Q(2d,q) of maximum size such that Y ∩ Z = Y . Then there exists a hyperplane h such that Y,Z ⊆ h.

Proof. In the view of Lemma 5.11, we ﬁnd a hyperplane h that contains G, the q(

) generators of Y disjoint to G, and, by Proposition 5.7 and Lemma 5.11 (d), the d2 q(

d 2

d−2 2

) generators which meet G in dimension d − 2.

Suppose that there exists an element G ∈ Y that is not in h. Then G and the q(d

) elements of Y disjoint to G lie in a second hyperplane h′ = h by Lemma 5.11. Lemma 5.11 makes it clear that the at least q(d

2

) + 1 generators of Y in h are diﬀerent to the at least q(d

2

) + d2 q(d−2

) + 1 generators of Y in h′. Hence,

2

2

) + 1 +

|Y | ≥ 2 q(

d 2

d 2

d−2 2

).

q(

According to Theorem 5.1,

This contradicts Lemma 5.12.

d−1

(qi + 1).

|Y | =

i=1

Theorem 5.14. Let (Y,Z) be a cross-intersecting EKR set of Q(2d,q), or W(2d − 1,q), q even, of maximum size such that Y ∩ Z = Y . Then either Y = Z and Y is an EKR set, or d even and Y ∪ Z are the generators of a subgeometry isomorphic to Q+(2d − 1,q).

Proof. First consider Q(2d,q). By Proposition 5.13, Y,Z ⊆ h for some hyperplane h isomorphic to Q+(2d − 1,q) if not Y = Z. Hence, (Y,Z) is a crossintersecting set of Q+(2d − 1,q) of maximum size. These sets were classiﬁed in Theorem 5.3.

The part of the assertion for W(2d − 1,q), q even, follows, since then Q(2d,q) and W(2d − 1,q) are isomorphic for q even.

5.2.2. The Symplectic Polar Space W(2d − 1,q), d even, q odd. Similar to [16] we use the following property of W(2d − 1,q), d even ([16, Theorem 34]):

- Theorem 5.15. Let ℓ1,ℓ2,ℓ3 be three pairwise disjoint lines of W(3,q), q odd.

Then the number of lines meeting ℓ1,ℓ2,ℓ3 is 0 or 2.

- Theorem 5.16. Let (Y,Z) be a cross-intersecting EKR set of maximum size of


W(2d − 1,q), d even, q odd. Then Y = Z.

Proof. Suppose to the contrary that Y ∩ Z = Y . By Proposition 5.7, we can ﬁnd two disjoint generators G and H in Y . Again by Proposition 5.7, there are exactly q[d][d − 1]/(q + 1) generators Y ′ ⊆ Y which meet G in a subspace of dimension d − 2. The generator G has [d][d − 1]/(q + 1) subspaces of dimension

- d − 2. Hence, we ﬁnd a subspace ℓ ⊆ G of dimension d − 2 such that ℓ is contained


in q elements of Y ′. Since q is odd, there are at least three elements y1,y2,y3 of Y through ℓ.

Consider the quotient geometry W3 of ℓ isomorphic to W(3,q) and the projection of the elements of Y and Z onto W3 from ℓ. Since elements of Y do not meet each other in dimension d−1 by Proposition 5.7, y1,y2,y3 are three disjoint lines in W3 after projection. Lemma 5.8 says that the [d] generators Z′ ⊆ Z which meet H in dimension d − 1 also meet G in [d] pairwise diﬀerent points. Hence there are at least 3 generators in Z′ which are projected onto three diﬀerent lines on W3. These three lines have to meet the projections of y1, y2, and y3, since (Y,Z) is an crossintersecting EKR set. By Theorem 5.15 this is not possible. Contradiction.

6. The Hermitian Polar Space H(2d − 1,q2)

It is well-known (see for example [14]) that the linear programming bound given in [13] can be reformulated as a weighted Hoﬀman bound. Hence, Lemma 4.1 is applicable if d > 1. The original bound on EKR sets on H(2d − 1,q2) is as follows.

Theorem 6.1 ([13]). Let Y be a EKR set of H(2d − 1,q2) with d > 1 odd. Then

nqd−1 − f1(qd−1 − 1)(1 − c) q2d−1 + qd−1 + f1(qd−1 − 1)c

|Y | ≤

![image 53](<2014-ihringer-cross-intersecting-erd-s-ko-rado-sets_images/imageFile53.png>)

2−2d+2,

≈ qd

where n = di=0−1(q2i+1 + 1), f1 = q2[d]q2

2−q−1+q−2d+3

q2d−3+1

q+1 and c = q

q2d−1 .

![image 54](<2014-ihringer-cross-intersecting-erd-s-ko-rado-sets_images/imageFile54.png>)

![image 55](<2014-ihringer-cross-intersecting-erd-s-ko-rado-sets_images/imageFile55.png>)

The result by Luz [14] which shows that the linear programming bound is a special case of the weighted Hoﬀman bound1 also holds for cross-intersecting EKR sets, but we feel that we should show this directly, since the transition from the linear programming technique used in [13] to the weighted Hoﬀman bound is not obvious. We shall prove a cross-intersecting result similar to [13] in the following.

Theorem 6.2. Let (Y,Z) be a cross-intersecting EKR set of H(2d−1,q2) with d > 1. Then

nλb λb − k

2−2d+2,

![image 57](<2014-ihringer-cross-intersecting-erd-s-ko-rado-sets_images/imageFile57.png>)

≈ qd

|Y | · |Z| ≤

![image 58](<2014-ihringer-cross-intersecting-erd-s-ko-rado-sets_images/imageFile58.png>)

2

2

where n = di=0−1(q2i+1+1), λb = −q(d−1)

−α 1 − f11−nc , k = qd

+αf1 c + 1−nc , f1 = q2[d]q2

![image 59](<2014-ihringer-cross-intersecting-erd-s-ko-rado-sets_images/imageFile59.png>)

![image 60](<2014-ihringer-cross-intersecting-erd-s-ko-rado-sets_images/imageFile60.png>)

2−q−1+q−2d+3

q2d−3+1

q+1 , c = q

q2d−1 , and

![image 61](<2014-ihringer-cross-intersecting-erd-s-ko-rado-sets_images/imageFile61.png>)

![image 62](<2014-ihringer-cross-intersecting-erd-s-ko-rado-sets_images/imageFile62.png>)

α =

2

qd(d−1) + q(d−1)

if d odd,

nqd2−d−nq(d−1)2

n+(2c−2)f1 if d even.

![image 63](<2014-ihringer-cross-intersecting-erd-s-ko-rado-sets_images/imageFile63.png>)

Proof. Let d > 1. Let Ad be the disjointness matrix as deﬁned in Section 3. Consider the matrix A deﬁned as

1 − c n

αf1c n

A = Ad − αE1 +

J + αf1

I.

![image 64](<2014-ihringer-cross-intersecting-erd-s-ko-rado-sets_images/imageFile64.png>)

![image 65](<2014-ihringer-cross-intersecting-erd-s-ko-rado-sets_images/imageFile65.png>)

Claim 1. Our ﬁrst claim is that A is a extended weight adjacency matrix. By Section 3, it is clear that the entry (x,y) of E1 equals Qi,1/n if x and y meet in codimension i. It was shown in [13, Equations (6)–(11)] that the following holds (note that the equation in [13] do not depend on d odd):

- (a) Q0,1 = f1,
- (b) Qd−1,1 = f1c,


(c) Qs,1 ≥ f1c if s < d, (d) Qd,1 < 0.

Hence, the entry (x,y) of the matrix A is 0 if x = y, it is less or equal to zero if 1 ≤ codim(x ∩ y) ≤ d − 1, and it is larger than 1 if x and y are disjoint. This shows that A is an extended weight adjacency matrix of the disjointness graph of generators.

Claim 2. Our second claim is that one of the second absolute largest eigenvalues of A is

1 − c n

2

−q(d−1)

− α 1 − f1

,

![image 66](<2014-ihringer-cross-intersecting-erd-s-ko-rado-sets_images/imageFile66.png>)

and that

1 − c n

2

k = qd

+ αf1 c +

. By (3.2), the eigenvalues of A are

![image 67](<2014-ihringer-cross-intersecting-erd-s-ko-rado-sets_images/imageFile67.png>)

1 − c n

2

qd

+ αf1 c +

for j ,

![image 68](<2014-ihringer-cross-intersecting-erd-s-ko-rado-sets_images/imageFile68.png>)

1 − c n

2

− q(d−1)

− α 1 − f1

for W1,

![image 69](<2014-ihringer-cross-intersecting-erd-s-ko-rado-sets_images/imageFile69.png>)

1 − c n

2+r(r−1) + αf1

(−1)rq(d−r)

for Wr with 1 < r < d, (−1)dqd(d−1) + αf1

![image 70](<2014-ihringer-cross-intersecting-erd-s-ko-rado-sets_images/imageFile70.png>)

1 − c n

for Wd.

![image 71](<2014-ihringer-cross-intersecting-erd-s-ko-rado-sets_images/imageFile71.png>)

![image 72](<2014-ihringer-cross-intersecting-erd-s-ko-rado-sets_images/imageFile72.png>)

1This seems to be part of the mathematical folklore for a long time, but the author is not aware of any source older than [14].

2

− α 1 − f11−nc = (−1)d(qd(d−1) − αf11−nc) is the second largest absolute eigenvalue. This proves our claim.

An simple calculation shows that −q(d−1)

![image 74](<2014-ihringer-cross-intersecting-erd-s-ko-rado-sets_images/imageFile74.png>)

![image 75](<2014-ihringer-cross-intersecting-erd-s-ko-rado-sets_images/imageFile75.png>)

Now we can apply Lemma 4.1 with these values. Note that k has approximately size qd

2+d−2, the second largest absolute eigenvalue λb has approximately size qd(d−1), and n has approximately size qd

2

. Therefore, nλb λb − k has approximately size qd

![image 76](<2014-ihringer-cross-intersecting-erd-s-ko-rado-sets_images/imageFile76.png>)

2−2d+2. Note that the normal adjacency matrix of the graph only yields qd

2−d as an upper bound, so this improves the bound signiﬁcantly.

For the sake of completeness we want to mention the cross-intersecting EKR sets for d = 2 is We will do this after providing a general geometrical results on (maximal) cross-intersecting EKR sets, where we call an (cross-intersecting) EKR set (Y,Z) maximal if there exists no generator x such that (Y ∪{x},Z) or (Y,Z∪{x}) is an cross-intersecting EKR set.

Lemma 6.3. Let (Y,Z) be a maximal cross-intersecting EKR set in a ﬁnite classical polar space of rank d. If two distinct elements y1,y2 ∈ Y meet in a subspace of dimension d − 1, then all elements of Z meet this subspace in at least a point.

Proof. Assume that there exists a generator z which meets y1 and y2 in points P,Q not in y1 ∩y2. Then P,Q,y1 ∩y2 is a totally isotropic subspace of dimension d + 1. Contradiction.

Lemma 4.1 yields

(q + 1)(q3 + 1) q2 + 1 as an upper bound for H(3,q2). This bound is not sharp as the following trivial results shows.

![image 77](<2014-ihringer-cross-intersecting-erd-s-ko-rado-sets_images/imageFile77.png>)

Theorem 6.4. Let (Y,Z) be a maximal cross-intersecting EKR set of H(3,q2) with |Y | ≥ |Z|. Then one of the following cases occurs:

- (a) The set Y is the set of all lines of H(3,q2), and Z = ∅. Here |Y | · |Z| = 0.
- (b) The set Y is the set of all lines meeting a ﬁxed line ℓ in at least a point, and Z = {ℓ}. Here |Y | · |Z| = (q2 + 1)q + 1.
- (c) The set Y is the set of all lines on a ﬁxed point P, and Y = Z. Here |Y |·|Z| = (q + 1)2.
- (d) The set Y is the set of lines meeting two disjoint lines ℓ1,ℓ2, and Z = {ℓ1,ℓ2}. Here |Y | · |Z| = 2(q2 + 1).
- (e) The set Y is the set of lines meeting three disjoint lines ℓ1,ℓ2,ℓ3, and Z is the set of all q + 1 lines meeting the lines of Y . Here |Y | · |Z| = (q + 1)2.


Proof. Assume that (a) does not occur. By Lemma 6.3, as soon as two elements of Y meet in a point P, then all elements

- of Z contain P. Hence, (b) occurs or at least 2 elements of Z meet in P. Hence, all elements of Y contain P by Lemma 6.3. This is case (c).


So assume that Y and vice-versa Z only consist of disjoint lines. If there are two lines ℓ1,ℓ2 ⊆ Z, then there are q2 + 1 (disjoint) lines L meeting ℓ1 and ℓ2 in a point (hence |Y | ≤ q2 + 1). If more than q + 1 of these lines meet ℓ1 (hence |Y | > q +1), then Z contains at most two lines, since in H(3,q2) exactly q +1 lines meet 3 pairwise disjoint lines in a point. This yields (d). If |Z| ≥ 3, then |Y | ≤ q+1 by the previous argument. We may assume |Y | ≥ 3. Then it is well-known that there are exactly q + 1 lines meeting the q + 1 lines of Y . Hence, we can add these lines and then Z is maximal. This yields (e).

The author tried to prove that the maximum cross-intersecting EKR set of H(5,q2) is the unique EKR of maximum size given in [16], but aborted this attempt after he got lost in too many case distinctions. This EKR set of all generators meeting a ﬁxed generator in at least a line is the largest cross-intersecting EKR set known to the author and has size q5 + q3 + q + 1. The largest example known to the author for H(7,q2) is the following.

Example 6.5. Let G be a generator of H(7,q2). Let Y be the set of all generators that meet G in at least a 2-space. Let Z be the set of all generators that meet G in at least a 3-space. Then (Y,Z) is a cross-intersecting EKR set.

Proof. A generator of H(7,q2) is a 4-space. A plane and a line of a 4-space meet pairwise in at least a point. Hence, (Y,Z) is a cross-intersecting EKR set.

In this example Y has

1 + q + q3 + q4 + q5 + q6 + q7 + 2q8 + q10 + q12 elements, Z has

1 + q + q3 + q5 + q7 elements, so in total the cross-intersecting EKR set has size

![image 79](<2014-ihringer-cross-intersecting-erd-s-ko-rado-sets_images/imageFile79.png>)

|Y | · |Z| ≈ q19/2.

The bound given in Theorem 6.2 for this case is approximately q10. For H(2d−1,q2), d > 4, the largest example known to the author is the EKR set of all generators on a ﬁxed point. The author assumes that the largest known examples are also the largest examples.

7. Summary

We summarize our results in the following table. We only list the cases, where cross-intersecting EKR sets of maximum size are not necessarily EKR sets. The table includes the size of the largest known example if it is not known if the best known bound does not seem to be tight.

![image 80](<2014-ihringer-cross-intersecting-erd-s-ko-rado-sets_images/imageFile80.png>)

![image 81](<2014-ihringer-cross-intersecting-erd-s-ko-rado-sets_images/imageFile81.png>)

Polar Space Maximum Size |Y | · |Z| Largest (known) Examples

Reference

![image 82](<2014-ihringer-cross-intersecting-erd-s-ko-rado-sets_images/imageFile82.png>)

Q+(2d − 1, q), d odd

n/2 Y latins, Z greeks Th. 5.3

Q(2d, q), d odd (q + 1) · . . . · (qd−1 + 1) Y latins and Z greeks of a Q+(2d + 1, q), or Y = Z EKR set

Th. 5.14

(q + 1) · . . . · (qd−1 + 1) see Q(2d, q) Th. 5.14

W(2d−1, q), d odd, q even

H(3, q2) q3 + q + 1 Th. 6.4 Th. 6.4 H(5, q2) q5 largest EKR set, size ≈

Th. 6.2

q5

H(7, q2) q10 Example 6.5, size ≈ q19/2

Th. 6.2

H(2d−1, q2), d > 1 q(d−1)2+1 all generators on a point, size ≈ q(d−1)2

Th. 6.2

References

- [1] Rudolf Ahlswede and Levon H. Khachatrian. The complete intersection theorem for systems of ﬁnite sets. European J. Combin., 18(2):125–136, 1997.
- [2] A.E. Brouwer, A.M. Cohen, and A. Neumaier. Distance-regular graphs. Ergebnisse der Mathematik und ihrer Grenzgebiete. Springer, 1989.
- [3] M. De Boeck. The largest Erd˝s-Ko-Rado sets of planes in ﬁnite projective and ﬁnite classical polar spaces. Des. Codes Cryptogr., Accepted(Special issue “Finite Geometries, in honor of F. De Clerck”), 2013.


- [4] M. De Boeck. The second largest Erd˝s-Ko-Rado sets of generators of the hyperbolic quadrics Q+(4n + 1, q). Adv. Geom., Submitted, 2014.
- [5] David Ellis, Ehud Friedgut, and Haran Pilpel. Intersecting families of permutations. J. Amer. Math. Soc., 24(3):649–682, 2011.
- [6] P. Erd˝s, Chao Ko, and R. Rado. Intersection theorems for systems of ﬁnite sets. Quart. J. Math. Oxford Ser. (2), 12:313–320, 1961.
- [7] P. Frankl and R. M. Wilson. The Erd˝s-Ko-Rado theorem for vector spaces. J. Combin. Theory Ser. A, 43(2):228–236, 1986.
- [8] Willem H. Haemers. Disconnected vertex sets and equidistant code pairs. Electron. J. Combin., 4(1):Research Paper 7, 10 pp. (electronic), 1997.
- [9] A. J. W. Hilton. An intersection theorem for a collection of families of subsets of a ﬁnite set. J. London Math. Soc. (2), 15(3):369–376, 1977.
- [10] J.W.P. Hirschfeld. Projective Geometries Over Finite Fields. Oxford Mathematical Monographs. Clarendon Press, 1998.
- [11] J.W.P. Hirschfeld and J.A. Thas. General Galois geometries. Oxford mathematical monographs. Clarendon Press, 1991.
- [12] W. N. Hsieh. Intersection theorems for systems of ﬁnite vector spaces. Discrete Math., 12:1–16, 1975.
- [13] Ferdinand Ihringer and Klaus Metsch. On the maximum size of Erd˝s-Ko-Rado sets in H(2d+ 1, q2). Des. Codes Cryptogr., 2012.
- [14] Carlos J. Luz. A characterization of Delsarte’s linear programming bound as a ratio bound. Linear Algebra Appl., 423(1):99–108, 2007.
- [15] Makoto Matsumoto and Norihide Tokushige. The exact bound in the Erd˝s-Ko-Rado theorem for cross-intersecting families. J. Combin. Theory Ser. A, 52(1):90–97, 1989.
- [16] Valentina Pepe, Leo Storme, and Fr´ed´eric Vanhove. Theorems of Erd˝s-Ko-Rado type in polar spaces. J. Combin. Theory Ser. A, 118(4):1291–1312, 2011.
- [17] Norihide Tokushige. The eigenvalue method for cross t-intersecting families. J. Algebraic Combin., 38(3):653–662, 2013.
- [18] Fr´ed´eric Vanhove. Incidence geometry from an algebraic graph theory point of view. PhD thesis, University Of Ghent, 2011.
- [19] Richard M. Wilson. The exact bound in the Erd˝s-Ko-Rado theorem. Combinatorica, 4(23):247–257, 1984.


Mathematisches Institut, Justus Liebig University Giessen, Arndtstraße 2, 35392 Giessen, Germany.

E-mail address: Ferdinand.Ihringer@math.uni-giessen.de

