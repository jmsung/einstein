arXiv:1402.3521v3[math.FA]25Feb2015

# FINITE TWO-DISTANCE TIGHT FRAMES

ALEXANDER BARGa, ALEXEY GLAZYRINb, KASSO A. OKOUDJOUc, AND WEI-HSUAN YUd

ABSTRACT. A ﬁnite collection of unit vectors S ⊂ Rn is called a spherical two-distance set if there are two numbers a and b such that the inner products of distinct vectors from S are either a or b. We prove that if a = −b, then a two-distance set that forms a tight frame for Rn is a spherical embedding of a strongly regular graph. We also describe all two-distance tight frames obtained from a given graph. Together with an earlier work by S. Waldron on the equiangular case (Linear Alg. Appl., vol. 41, pp. 2228-2242, 2009) this completely characterizes two-distance tight frames. As an intermediate result, we obtain a classiﬁcation of all two-distance 2-designs.

1. INTRODUCTION

A ﬁnite collection of unit vectors S ⊂ Rn is called a spherical two-distance set if there are two numbers a and b such that the inner products of distinct vectors from S are either a or b. If in addition a = −b, then S deﬁnes a set of equiangular lines through the origin in Rn. Equiangular lines form a classical subject in discrete geometry following foundational papers of Van Lint, Seidel, and Lemmens [17, 16]. Equiangular line sets are closely related to strongly regular graphs and two-graphs [10, 11] which form the main source of their constructions. Another group of results is concerned with bounding the maximum size g(n) of spherical two-distance sets in n dimensions. We refer to [3, 4] for the latest results on upper bounds on g(n) as well as an overview of the relevant literature.

A ﬁnite collection of vectors S = {x1,...,xN} ⊂ Rn is called a ﬁnite frame for the Euclidean space Rn if there are constants 0 < A ≤ B < ∞ such that for all x ∈ Rn

N

x,xi 2 ≤ B||x||2. (1.1)

A||x||2 ≤

i=1

If A = B, then S is called an A-tight frame, in which case A =

1 n i

xi 2. (1.2)

![image 1](<2014-barg-finite-two-distance-tight-frames_images/imageFile1.png>)

It is trivially seen that a ﬁnite collection of vectors S = {xi : i = 1,...N} ⊂ Rn is an A-tight frame if and only if for any x ∈ Rn,

![image 2](<2014-barg-finite-two-distance-tight-frames_images/imageFile2.png>)

Date: February 26, 2015. 2000 Mathematics Subject Classiﬁcation. Primary 42C15; Secondary 15B48. Key words and phrases. Spherical two-distance sets, ﬁnite tight frames, strongly regular graphs, spherical 2-designs, spherical designs of

harmonic index 2.

- a Department of ECE and Institute for Systems Research, University of Maryland, College Park, MD 20742, and IITP, Russian Academy of

Sciences, Moscow, Russia. Email: abarg@umd.edu. Research supported in part by NSF grants CCF1217894, DMS1101697, and NSA 98230-12-

- 1-0260;


- b Department of Mathematics, The University of Texas, Brownsville, TX 78520, Email: Alexey.Glazyrin@utb.edu. Research supported in part

by NSF grants DMS1101688, DMS1400876.

- c Department of Mathematics, University of Maryland, College Park, MD 20742, Email: kasso@math.umd.edu. Research supported in part by

- a RASA from the Graduate School of UMCP, and by a grant from the Simons Foundation (#319197 to Kasso Okoudjou).


- d Department of Mathematics, University of Maryland and Inst. for Systems Research, College Park, MD 20742, Email:


mathyu@math.umd.edu. Research supported in part by NSF grants CCF1217894, DMS1101697.

1

N

x,xi xi. (1.3)

Ax =

i=1

If in addition xi = 1 for all i ∈ I, then S is a ﬁnite unit-norm tight frame or FUNTF. If at the same time S is a spherical two-distance set, we call it a two-distance tight frame. In particular, if the two inner products in S satisfy the condition a = −b, then it is an equiangular tight frame or ETF. All frames in this paper will be assumed unit-norm.

The Gram matrix G of S is deﬁned by Gij = xi,xj ,1 ≤ i,j ≤ N, where N = |S|. If S is a FUNTF for Rn, then it is straightforward to show [12] that G has one nonzero eigenvalue λ = N/n of multiplicity n and eigenvalue 0 of multiplicity N − n.

Frames have been used in signal processing and have a large number of applications in sampling theory, wavelet theory, data transmission, and ﬁlter banks [8, 14]. The study of ETFs was initiated by Strohmer and Heath [23] and Holmes and Paulsen [13]. In particular, [13] shows that equiangular tight frames give error correcting codes that are robust against two erasures. Bodmann et al. [6] show that ETFs are useful for signal reconstruction when all the phase information is lost. Sustik et al. [22] derived necessary conditions on the existence of ETFs as well as bounds on their maximum cardinality.

Benedetto and Fickus [5] introduced a useful parameter of the frame, called the frame potential. For our purposes it sufﬁces to deﬁne it as FP(S) = Ni,j=1 xi,xj 2. For a two-distance frame we obtain

N

xi,xj 2 = N + 2νaa2 + (N(N − 1) − 2νa)b2, (1.4)

i,j=1

where νa = |{(i,j) : i < j : xi,xj = a}|.

- Theorem 1.1. [5, Theorem.6.2] Let N > n. If S = {xi : 1 ≤ i ≤ N} is any set of unit-norm vectors, then


N2 n

(1.5) with equality if and only if S is a tight frame.

FP(S) ≥

![image 3](<2014-barg-finite-two-distance-tight-frames_images/imageFile3.png>)

A ﬁnite collection of unit vectors S = {xi : i = 1,...,N} in Rn is called a spherical 2-design [10] if

N

N

N2 n

. (1.6)

xi,xj 2 =

xi = 0,

![image 4](<2014-barg-finite-two-distance-tight-frames_images/imageFile4.png>)

i,j=1

i=1

In other words, a spherical 2-design is a FUNTF with the center of mass at the origin.

- Remark 1.1. In [2] spherical sets that satisfy only the tight frame condition (the second condition in (1.6)) are called spherical designs of harmonic index 2. In the sequel we will refer to such spherical designs as shifted 2-designs.


To state our main result we need several deﬁnitions. A regular graph of degree k on v vertices is called strongly regular if every two adjacent vertices have λ common neighbors and every two non-adjacent vertices have µ common neighbors. Below we use the notation SRG(v,k,λ,µ) to denote such a graph. Note that the complement of a strongly regular graph SRG(v,k,λ,µ), is also strongly regular, namely SRG(v,v − k − 1,v − 2k + µ − 2,v − 2k + λ). The theory of strongly regular graphs is presented, for instance, in [11, 9]. Below we use a classical construction of spherical embeddings of strongly regular graphs introduced by Delsarte, Goethals, and Seidel [10, Example 9.1]; see also [19, 1]. Roughly speaking, a spherical embedding of Γ = SRG(v,k,λ,µ) is obtained by associating a basis of Rv with the vertices of Γ and projecting these vectors on an eigenspace of the adjacency matrix of Γ. A more detailed description is given in Sect. 3 after we develop all the necessary pieces of notation.

In this paper we characterize two-distance FUNTFs by linking them to spherical 2-designs and strongly regular graphs. Our main result is as follows:

- Theorem 1.2. Let S = {xi : i ∈ I} be a non-equiangular two-distance FUNTF in Rn. Then S forms a spherical two-distance 2-design or a shifted 2-design. In either case S can be obtained as a spherical embedding of a strongly regular graph. Under spherical embedding, every strongly regular graph gives rise to three different two-distance


- 2-designs and therefore, to six different two-distance tight frames, two of which are regular simplices.


The proof is given in Sections 2, 3. As an intermediate result (see Theorem 3.4), we fully characterize spherical 2-designs that form spherical two-distance sets.

Strongly regular graphs form examples of classical objects in algebraic combinatorics called association schemes [9]. Although we do not use the language of schemes in this paper, we note that our results contribute to the study of the general problem of characterizing spherical designs that can be obtained from association schemes.

Note that the connection between equiangular line sets and strongly regular graphs is well known (Seidel et al. [21, 10]; see also [11]). It has been recently addressed in the context of frame theory, particularly in the study of ETFs [23, 13]. A recent paper by Waldron [24] proves that an ETF in Rn with N ≥ n vectors exists if and only if there exists an SRG(N − 1,k,(3k − N)/2,k/2), where k is a certain function of n and N. Furthermore, [24] also contains many examples of ETFs in Rn,n ≤ 50. Together with Theorem 1.2 this result completes the description of two-distance tight frames, equiangular or not.

2. BASIC PROPERTIES

We begin with an easy example of 2-distance FUNTFs which is given by the following construction. We will need the following theorem.

Theorem 2.1 (Larman, Rogers, and Seidel, [15]). Let S be a spherical two-distance set in Rn. If |S| > 2n + 1 then the inner products a,b are related by the equation b = (ka − 1)/(k − 1) where k ∈ {2,...,⌊(1 + √2n)/2⌋} is an integer.

![image 5](<2014-barg-finite-two-distance-tight-frames_images/imageFile5.png>)

The original proof of [15] had 2n + 3 in place of 2n + 1, while the above improvement is due to Neumaier [19]. Given the value of a, we denote by bk(a) the corresponding value of b.

- Proposition 2.2. Let e1,...,en+1 be the standard basis in Rn+1. The projection of the set S = {ei + ej,1 ≤ i < j ≤ n + 1} (2.1)


on the hyperplane x1 + ··· + xn+1 = 2 forms a two-distance tight frame for Rn. Proof. Note that the inner products of distinct vectors in S are either 1 or 0. Let

ν1,1 = |{(i,j) : i < j, e1 + e2,ei + ej = 1}|

Observe that (i,j) is contained in this set if and only if i = 1 or i = 2, and we obtain ν1,1 = 2(n − 1). By symmetry, the value ν1,1 does not depend on the choice of the ﬁxed vector e1 + e2, so the total number of unordered pairs of vectors in S with inner product 1 equals

- 1

![image 6](<2014-barg-finite-two-distance-tight-frames_images/imageFile6.png>)

- 2


n + 1 2

- 1

![image 7](<2014-barg-finite-two-distance-tight-frames_images/imageFile7.png>)

- 2


ν1,1 =

(n − 1)n(n + 1). The pairs of distinct vectors not counted in ν1 are orthogonal, and their number is ν0 =

ν1 =

1 8

n(n + 1)/2 2 − ν1 =

(n − 2)(n − 1)n(n + 1).

![image 8](<2014-barg-finite-two-distance-tight-frames_images/imageFile8.png>)

Now let us project the vectors of S on the plane x1 + ··· + xn+1 = 2 and scale the result to place them on the unit sphere around the point z0 = n+12 (1,1,...,1). Since each vector zi,j = ei + ej already belongs to the plane, the resulting vector will be zi,j′ = c(zi,j − z0) where c = √ 1

![image 9](<2014-barg-finite-two-distance-tight-frames_images/imageFile9.png>)

2−n+14 . By a series of computations we see that zi,j′ ,zk,l′ = c2( zi,j,zk,l − n+14 ).

![image 10](<2014-barg-finite-two-distance-tight-frames_images/imageFile10.png>)

![image 11](<2014-barg-finite-two-distance-tight-frames_images/imageFile11.png>)

![image 12](<2014-barg-finite-two-distance-tight-frames_images/imageFile12.png>)

![image 13](<2014-barg-finite-two-distance-tight-frames_images/imageFile13.png>)

And since zi,j,zk,l ∈ {0,1} we arrive that the fact that zi,j′ ,zk,l′ ∈ {a,b} with a = (n − 3)/(2(n − 1)) and

- b = −2/(n − 1). This information sufﬁces to compute the frame potential, and we obtain


N2 n

FP(S) = N + 2ν1a2 + 2ν0b2 =

![image 14](<2014-barg-finite-two-distance-tight-frames_images/imageFile14.png>)

The frame potential meets the lower bound (1.5) with equality, which implies that S forms a FUNTF for Rn.

We next give a characterization result for two-distance FUNTFs.

Deﬁnition 2.3. Let S ⊂ Rn be a spherical two-distance set with inner products a and b, b < a, let xi ∈ S, and let

Na,i = |{j : xj ∈ S, xi,xj = a}|. S is called regular if Na,i does not depend on i. For regular sets we denote this quantity simply by Na.

- Theorem 2.4. Let S ⊂ Rn,|S| = N be a two-distance FUNTF with inner products a and b such that a2 − b2 = 0. Then S is regular and


(N/n) − 1 − (N − 1)b2 a2 − b2

(2.2) −n(a + b) − nab(N − 1) = N − n or (N − n)(a + b) − nab(N − 1) = N − n. (2.3)

Na =

![image 15](<2014-barg-finite-two-distance-tight-frames_images/imageFile15.png>)

Proof. G is similar to a diagonal matrix of order N with n nonzero entries λ = N/n on the diagonal. Therefore, G2 − λG = 0, so G2 = λG and (G2)ii = λ for all i since Gii = 1. We also have (G2)ii = Nj=1 G2ij, so the norm of every row and of every column is the same and equals √

![image 16](<2014-barg-finite-two-distance-tight-frames_images/imageFile16.png>)

λ. Now let Na be the number of entries a in any ﬁxed column. Then

N n

1 + a2Na + b2(N − 1 − Na) =

. This implies (2.2).

![image 17](<2014-barg-finite-two-distance-tight-frames_images/imageFile17.png>)

Thus, 1 = (11 ...1) is an eigenvector of the Gram matrix G with eigenvalue 0 or N/n. Suppose it is the former, then G·1 = 0, so the sum of entries in every row is 0. This implies that 1+aNa+(N −1−Na)b = 0. By substituting Na given by (2.2) into this last equation, and after some simpliﬁcations we obtain the ﬁrst of the two options for b in (2.3).

Now suppose that G · 1 = Nn 1, so the sum of entries of G in any given row equals N/n. Repeating the calculation performed for the ﬁrst case, we obtain the second of the two possibilities for b.

![image 18](<2014-barg-finite-two-distance-tight-frames_images/imageFile18.png>)

- Remark 2.1. Another way to express the alternative in (2.3) is as follows. The sum of squared entries of every row of G equals N/n and the sum of the entries is either 0 or N/n. These two equations translate into the two conditions for a and b.


In the next section we characterize FUNTF for each of the two cases in (2.3).

- Remark 2.2. If a = −b, then the statement of Theorem 2.4 does not hold. Indeed, consider the set S = {x1,...,x28} of 28 vectors in R7 constructed as in (2.1). By Theorem 2.1 the inner products between distinct vectors in S are ±1/3, so they form a set of equiangular lines. For any given vector x ∈ S we have |{y ∈ S : x,y = 1/3}| = 12 and


|{y ∈ S : x,y = −1/3}| = 15. Now consider the set S′ = {−x1,x2,...,x28} which is also a FUNTF with inner products ±1/3, but the ﬁrst column of G contains 12 entries equal to −1/3, which is different from all the other columns.

3. TWO-DISTANCE FUNTFS AND STRONGLY REGULAR GRAPHS

Connections between equiangular line sets and ETFs on the one side and strongly regular graphs on the other are well known and have been used in the literature to characterize the sets of parameters of ETFs [11, Ch. 11], [24]. In this section we extend this connection by relating two-distance (non equiangular) FUNTFs, 2 designs, and strongly regular graphs.

We begin with a necessary condition for the existence of two-distance FUNTFs. Let S be such a frame. The Gram matrix of any two-distance set with inner products a,b can be written as

G = I + aΦ1 + bΦ2, (3.1)

where Φ1 and Φ2 are the corresponding indicator matrices. We also denote by Γ1 and Γ2 the graphs with adjacency matrices Φ1 and Φ2, respectively.

- Proposition 3.1. If S is a 2-distance FUNTF in Rn with inner products a,b, then S is either an n-dimensional spherical 2-design, or is similar to an (n − 1)-dimensional spherical 2-design contained in a subsphere of radius


![image 19](<2014-barg-finite-two-distance-tight-frames_images/imageFile19.png>)

- 1 − 1/n. In the former (resp., latter) case a and b satisfy the ﬁrst (resp., second) equality in (2.3).


Proof. Let S = {xi : 1 ≤ i ≤ N} and let s = Ni=1 xi. Then for each i, 1 ≤ i ≤ N the value t := xi,s does not depend on i and is equal to t = Naa + (N − Na)b + 1, where Na is given in (2.2).

Applying (1.3) for x = s, we obtain

N

N n

txi = ts.

s =

![image 20](<2014-barg-finite-two-distance-tight-frames_images/imageFile20.png>)

i=1

2

Hence either s = 0 and S is a spherical 2-design, or t = Nn and then s,s = Nt = N

n . Suppose that s = 0 (equivalently t = N/n). For each i, 1 ≤ i ≤ N, denote yi = x

![image 21](<2014-barg-finite-two-distance-tight-frames_images/imageFile21.png>)

![image 22](<2014-barg-finite-two-distance-tight-frames_images/imageFile22.png>)

√i−s/N

. We will show that the

![image 23](<2014-barg-finite-two-distance-tight-frames_images/imageFile23.png>)

![image 24](<2014-barg-finite-two-distance-tight-frames_images/imageFile24.png>)

1−1/n

set S′ = {yi : i = 1,...,N}, which is similar to the set S, forms a spherical 2-design in Rn−1. This will imply that S lies on a sphere of radius 1 − 1/n in Rn.

![image 25](<2014-barg-finite-two-distance-tight-frames_images/imageFile25.png>)

First we check that yi,s = 0 for all i. Indeed,

xi,s − s,s /N 1 − 1/n

yi,s =

=

![image 26](<2014-barg-finite-two-distance-tight-frames_images/imageFile26.png>)

![image 27](<2014-barg-finite-two-distance-tight-frames_images/imageFile27.png>)

2/n N

N/n − N

![image 28](<2014-barg-finite-two-distance-tight-frames_images/imageFile28.png>)

= 0. (3.2)

![image 29](<2014-barg-finite-two-distance-tight-frames_images/imageFile29.png>)

![image 30](<2014-barg-finite-two-distance-tight-frames_images/imageFile30.png>)

1 − 1/n

This establishes that S′ is an (n − 1)-dimensional set. Moreover, S′ lies on the unit sphere. Indeed, using that yi,s = 0, we obtain

xi 2 − s/N 2 1 − 1/n

yi 2 =

=

![image 31](<2014-barg-finite-two-distance-tight-frames_images/imageFile31.png>)

2/n N2

1 − N

![image 32](<2014-barg-finite-two-distance-tight-frames_images/imageFile32.png>)

= 1.

![image 33](<2014-barg-finite-two-distance-tight-frames_images/imageFile33.png>)

1 − 1/n

Clearly S′ is a two-distance set. It remains to show that S′ forms a 2-design (1.6). The center-of-masses condition is clearly satisﬁed. To check the tight frame condition let us compute the frame potential of S′ and use Theorem 1.1. We

have

N2 n

![image 34](<2014-barg-finite-two-distance-tight-frames_images/imageFile34.png>)

N

N

| xi,xj |2 =

=

i,j=1

i,j=1

![image 35](<2014-barg-finite-two-distance-tight-frames_images/imageFile35.png>)

1 n

1 −

yi +

![image 36](<2014-barg-finite-two-distance-tight-frames_images/imageFile36.png>)

![image 37](<2014-barg-finite-two-distance-tight-frames_images/imageFile37.png>)

1 n

s N

s N

, 1 −

yi +

![image 38](<2014-barg-finite-two-distance-tight-frames_images/imageFile38.png>)

![image 39](<2014-barg-finite-two-distance-tight-frames_images/imageFile39.png>)

![image 40](<2014-barg-finite-two-distance-tight-frames_images/imageFile40.png>)

2

N

=

i,j=1

1 n

1 −

![image 41](<2014-barg-finite-two-distance-tight-frames_images/imageFile41.png>)

s 2 N2

yi,yj +

![image 42](<2014-barg-finite-two-distance-tight-frames_images/imageFile42.png>)

2

N

N2 n2

1 n

2 n

2

FP(S′) +

= 1 −

yi,yj +

![image 43](<2014-barg-finite-two-distance-tight-frames_images/imageFile43.png>)

![image 44](<2014-barg-finite-two-distance-tight-frames_images/imageFile44.png>)

![image 45](<2014-barg-finite-two-distance-tight-frames_images/imageFile45.png>)

i,j=1

N2 n2

1 n

2

FP(S′) +

= 1 −

![image 46](<2014-barg-finite-two-distance-tight-frames_images/imageFile46.png>)

![image 47](<2014-barg-finite-two-distance-tight-frames_images/imageFile47.png>)

2

where the last step uses the condition i yi = 0. Thus, FP(S′) = N

n−1 and therefore, S′ is an (n − 1)-dimensional 2-design.

![image 48](<2014-barg-finite-two-distance-tight-frames_images/imageFile48.png>)

Finally, note that t is an eigenvalue of G, namely, G · 1 = t1. Recalling that the two cases in (2.3) correspond to t = 0 and t = N/n, we obtain the ﬁnal claim of the proposition.

Observe that a related result was proved in [20]. Namely, Theorem 4.7 in that paper states (in our terms) that a spherical set S ⊂ Rn is a 2-design if and only if G · 1 = 0 and G2 =

x∈S x 2

n G.

![image 49](<2014-barg-finite-two-distance-tight-frames_images/imageFile49.png>)

Due to the Delsarte-Goethals-Seidel theorem ([10, Theorem 7.4]), any spherical two-distance 2-design is associated with a strongly regular graph and therefore, due to Proposition 3.1, any two-distance tight frame, too, is associated with a strongly regular graph. To keep our exposition self-contained we give a short direct proof of this fact.

- Proposition 3.2. If S is a two-distance tight frame with inner products a and b, a2 −b2 = 0, then its associated graph Γ1 (and Γ2 as the complement of Γ1) is a strongly regular graph. Proof. It follows from (1.3) and (1.2) that for any two vectors xk, xl of S,


N

N n

xk,xi xi,xl . (3.3)

xk,xl =

![image 50](<2014-barg-finite-two-distance-tight-frames_images/imageFile50.png>)

i=1

Fix indices k and l and assume xk,xl = a. Let Iα,β = {i ∈ {1,...,N} : xk,xi = α and xi,xl = β},

where α,β ∈ {a,b}, and let Ca := |Ia,a|. Note that by the symmetry of the Gram matrix G, we have that |Ia,b| = |Ib,a|. Let us ﬁnd the cardinality of Ia,b, i.e., the set of indices i with the entry a in row k and entry b in row l. Consider the subset of indices i in row k of G with xk,xi = a except i = l (in this position row l contains 1). There are Na − 1 such indices, where Na is the number of a’s in the row (see the remark before Theorem 2.4). We then need to subtract the number of those i for which xi,xl = a. But those are precisely the indices in the set Ia,a. Consequently,

|Ia,b| = |Ib,a| = Na − Ca − 1. (3.4)

We next observe that the union of the (disjoint) sets Iα,β α,β ∈ {a,b} gives all the indices in row k of G except the diagonal entry. Therefore, we obtain

N − 1 = |Ia,a| + 2|Ia,b| + |Ib,b|. (3.5)

Recall that we have Nb + Na = N − 1. Taking this together with (3.4) and (3.5) and performing simpliﬁcations, we obtain

|Ib,b| = Nb − Na + Ca + 1.

We can then rewrite (3.3) as

N n

a = 2(Na − Ca − 1)ab + Caa2 + (Nb − Na + Ca + 1)b2

![image 51](<2014-barg-finite-two-distance-tight-frames_images/imageFile51.png>)

= 2(Na − 1)ab + (Nb − Na + 1)b2 + Ca(a − b)2.

Since a = b, there is a unique Ca that satisﬁes this equality. In other words, any pair of connected vertices of the associated graph Γ1 has the same number Ca of common neighbors. Similarly, any two non-connected vertices of Γ1 have the same number Cb of common neighbors. Therefore, Γ1 is a strongly regular graph.

We now set out to describe all two-distance tight frames. Propositions 3.1 and 3.2 imply that we just need to ﬁnd all spherical two-distance embeddings of strongly regular graphs and check the 2-design conditions for them.

Spherical embeddings of SRGs. Let Γ1 be an SRG(v,k,λ,µ) which is not a complete or empty graph and let Φ1 be its adjacency matrix. As already mentioned, the set of vertices of Γ1 can be embedded in the sphere by projecting the vectors of the standard basis of the space Rv on the eigenspaces of Φ1.

The spectral structure of the matrix Φ1 is as follows. It has three mutually orthogonal eigenspaces that correspond to three eigenvalues: the all-one vector 1 with eigenvalue k, an eigenspace E1 of dimension n1 with eigenvalue r1, and an eigenspace E2 of dimension n2 with eigenvalue r2 [9, p.117]. Note that for Tura´n graphs and their complements it is possible that r1 = k. The values of n1,r1,n2,r2 can be found explicitly via the parameters (v,k,λ,µ). Since these values are useful in constructing examples, we quote the expressions for them from [11, pp.219-220]:

- 1

![image 52](<2014-barg-finite-two-distance-tight-frames_images/imageFile52.png>)

- 2


![image 53](<2014-barg-finite-two-distance-tight-frames_images/imageFile53.png>)

(λ − µ ± (λ − µ)2 + 4(k − µ))

r1,2 =

- 1

![image 54](<2014-barg-finite-two-distance-tight-frames_images/imageFile54.png>)

- 2


2k + (v − 1)(λ − µ) (λ − µ)2 + 4(k − µ)

n1,2 =

v − 1 ∓

.

![image 55](<2014-barg-finite-two-distance-tight-frames_images/imageFile55.png>)

![image 56](<2014-barg-finite-two-distance-tight-frames_images/imageFile56.png>)

Geometrically the Delsarte-Goethals-Seidel construction amounts to projecting orthogonally the standard basis vectors of Rv on an eigenspace, for instance E1, and normalizing the projections (they all have the same length) to obtain unit lengths. Denote the obtained spherical set by S1 = S1(Γ1) and denote its two inner products by a1 and b1, so that Γ1 is the graph of inner products a1,b1; cf. (3.1). It is easy to show [10] that this spherical set supports an n1-dimensional 2-design.

Similarly we can obtain an n2-dimensional 2-design S2 = S2(Γ1) with inner products a2 and b2 by projecting RN on E2 and normalizing the projections. Finally, let S0 denote the trivial one-dimensional embedding and note that a0 = b0 = 1.

Let Γ2 be the complement graph of Γ1 and let Φ2 be its adjacency matrix. We have Φ2 = J − I − Φ1.

The vector 1 is an eigenvector of each of these matrices, and any vector z such that z,1 = zi = 0 is an eigenvector of J and I. Hence if such vector z is an eigenvector of Φ1, it is also an eigenvector of Φ2. Thus, the matrices Φ1 and Φ2 share the same spectral structure. In particular, Φ2 also has three eigenvalues and three eigenspaces that coincide with the eigenspaces of Φ1: a vector of all ones 1 with eigenvalue v − 1 − k, an eigenspace E1 of dimension n1 with eigenvalue s1, an eigenspace E2 of dimension n2 with eigenvalue s2.

- Proposition 3.3. Let Γ1(N,k,λ,µ) be a strongly regular graph that is not complete or empty. For any two-distance spherical embedding S = {x1,...,xN} of Γ1, there are three nonnegative real numbers α,β,γ, α2 + β2 + γ2 = 1 such that for all i = 1,...,N


xi = αxi(0) + βxi(1) + γxi(2) (3.6)

for some xi(j),j = 0,1,2. The sets Sj(Γ1) = {xi(j) : 1 ≤ i ≤ N},j = 0,1,2 form the Delsarte-Goethals-Seidel spherical embeddings of Γ1 and are contained in mutually orthogonal unit spheres of dimensions 1, n1, and n2, respectively.

Proof. Let S be a two-distance spherical embedding of Γ1 with distances a and b. Write the Gram matrix G of S as in (3.1). The embedding S exists if and only if G is positive semideﬁnite. Since the matrices Φ1 and Φ2 share the spectral structure, we can ﬁnd all eigenvalues of G and check their non-negativity. This results in the following inequalities:

1 + ak + b(N − 1 − k) ≥ 0

(3.7)

- 1 + ar1 + bs1 ≥ 0
- 1 + ar2 + bs2 ≥ 0,


(some of these inequalities may trivialize to 1 ≥ 0). The set of all feasible pairs (a,b) is the intersection of at most three half-planes in the plane. Note that this set must belong to the square [−1,1]2, so it is bounded. Moreover, G 0 if and only if the inequalities (3.7) hold true, so this region is either a triangle or a single point. Since there are always at least two different embeddings, namely S0 and the (N − 1)-dimensional regular simplex, this set must be a triangle whose vertices are the intersections of any two of the three lines deﬁning the inequalities.

Next we note that these intersection points precisely represent S0, S1, and S2 so they are (a0,b0), (a1,b1), and (a2,b2). Indeed, project the basis orthogonallyon one of the spaces 1,E1,E2 and denote the (normalized) resulting set by X. The eigenvectors of this projection, corresponding to the two other spaces have zero eigenvalues. Subsequently, the eigenvalues of these vectors for the Gram matrix G = XtX are also zero, which turns two of the inequalities in (3.7) into equalities.

Any other pair (a,b) can be represented as (a,b) = α2(a0,b0) + β2(a1,b1)+ γ2(a2,b2), where α2 + β2 + γ2 = 1 and α,β,γ are non-negative. Now note that the set {xi : 1 ≤ i ≤ N} such that xi = αxi(0) + βxi(1) + γxi(2), where the set of all vectors xi(0) forms S0, the set of all xi(1) forms S1, and the set of all xi(2) forms S2 in mutually orthogonal unit spheres, gives a two-distance spherical embedding of Γ1 with inner products a and b. Moreover, any such embedding is completely determined by its Gram matrix, and therefore, this gives a description of all spherical two-distance embeddings of Γ1. This completes the proof.

Proposition 3.3 entails the following description of two-distance 2-designs.

- Theorem 3.4. Any spherical two-distance 2-design S = {x1,...,xN} with graph Γ1 for one of the distances is either S1(Γ1) or S2(Γ1), or a regular (N − 1)-dimensional simplex.


Proof. We begin with the representation of the vectors xi given by (3.6). Note that since Ni=1 xi = 0, the coefﬁcient α must be 0. If one of β or γ is 0, then S is either S1 or S2. The remaining case is when they are both positive. In this case the set S is (n1 + n2)-dimensional, so it must satisfy the tight-frame condition (1.1)-(1.2) for any x ∈ Rn1+n2:

N

N n1 + n2||x||2 =

x,xi 2. (3.8)

![image 57](<2014-barg-finite-two-distance-tight-frames_images/imageFile57.png>)

i=1

Now we express x as the sum of x(1) and x(2), where x(1) belongs to the space Rn1 that contains all the vectors xi(1), and x(2) belongs to the space Rn2 containing all xi(2). Since S1 and S2 form 2-designs, they must satisfy the tight-frame condition, namely

N

N nj ||x(j)||2 =

x(j),xi(j) 2, j = 1,2. Using (3.6) and (3.8), we obtain:

![image 58](<2014-barg-finite-two-distance-tight-frames_images/imageFile58.png>)

i=1

N n1 + n2

(||x(1)||2 + ||x(2)||2) =

![image 59](<2014-barg-finite-two-distance-tight-frames_images/imageFile59.png>)

= β2

N

(β x(1),xi(1) + γ x(2),xi(2) )2

i=1

N

N n1||x(1)||2 + γ2

N n2||x(2)||2 + 2βγ

![image 60](<2014-barg-finite-two-distance-tight-frames_images/imageFile60.png>)

![image 61](<2014-barg-finite-two-distance-tight-frames_images/imageFile61.png>)

i=1

x(1),xi(1) x(2),xi(2) .

n1+n2 and γ2 = n

This equality must hold for any x(1) and x(2), so β2 = n

n1+n2 . To show that with these values of β and γ the set S forms a 2-design we just need to explain why

2

1

![image 62](<2014-barg-finite-two-distance-tight-frames_images/imageFile62.png>)

![image 63](<2014-barg-finite-two-distance-tight-frames_images/imageFile63.png>)

N

x(1),xi(1) x(2),xi(2) is always 0. Refer to the deﬁnition of S1 and S2 and let their ambient spaces be E1 and E2. Then the vector with components

i=1

x(1),xi(1) is just Φ1x(1) times a normalizing coefﬁcient, and the vector with components x(2),xi(2) is Φ1x(2) with its normalizing coefﬁcient. The ﬁrst vector belongs to E1 and the second vector belongs to E2 so they must be orthogonal.

A regular (N −1)-dimensional simplex is obviously a 2-design and can be considered as a two-distance embedding of Γ1 with equal distances. Since S1 and S2 are not (N − 1)-dimensional, the third 2-design that we constructed must be a regular simplex (recall that n1 + n2 = N − 1). This observation ﬁnishes the proof of the theorem.

- Remark 3.1. The regular simplex can be constructed similarly to S1 and S2: it is obtained by ﬁnding orthogonal projections of (the basis vectors of) RN on E1 ∪ E2 and normalizing to get unit lengths. Another simplex is given by the orthonormal basis itself which represents a trivial projection.


Proof. Proof of Theorem 1.2. We now recap the arguments that lead to the classiﬁcation of all non-equiangular twodistance tight frames in Theorem 1.2. Let S be such a frame and assume that a and b are the two distinct inner products of the vectors in S. Then, a2 − b2 = 0. First, by Proposition 3.1, S is either a n dimensional spherical

- 2−design or similar to (n − 1) dimensional spherical 2−design. On account of Prop. 3.2 the graphs deﬁned by the Gram matrix of a non-equiangular two-distance FUNTF are strongly regular, so we need to describe all spherical two-distance embeddings of SRGs and check if they satisfy the design condition. We show in Theorem 3.4 that all such embeddings are of the Delsarte-Goethals-Seidel type, and yield spherical two-distance 2-designs. Since each such design gives rise to two FUNTFs, this completes the classiﬁcation.


The results established above enable us to construct large classes of two-distance tight frames. For brevity we write FUNTF(n,N,Na,a,b) to refer to a two-distance tight frame in n dimensions, with N points, inner products b < a, and with Na entries a in each row of G. We give a few examples of 2-distance frames derived from the table of strongly regular graphs in [9, pp.143ff]. Many more examples can be easily obtained using the described recipe.

SRG(N, k, λ, µ) 2-design FUNTF(n,N, Na, a, b) shifted 2-design FUNTF(n,N, Na, a, b) (10, 6, 3, 4) (4, 10, 6, 1/6, −2/3), (5, 10, 3, 1/3, −1/3) (5, 10, 6, 1/3, −1/3), (6, 10, 3, 4/9, −1/9)

![image 64](<2014-barg-finite-two-distance-tight-frames_images/imageFile64.png>)

![image 65](<2014-barg-finite-two-distance-tight-frames_images/imageFile65.png>)

![image 66](<2014-barg-finite-two-distance-tight-frames_images/imageFile66.png>)

![image 67](<2014-barg-finite-two-distance-tight-frames_images/imageFile67.png>)

![image 68](<2014-barg-finite-two-distance-tight-frames_images/imageFile68.png>)

![image 69](<2014-barg-finite-two-distance-tight-frames_images/imageFile69.png>)

![image 70](<2014-barg-finite-two-distance-tight-frames_images/imageFile70.png>)

- (15, 8, 4, 4) (5, 15, 8, 1/4, −1/2), (9, 15, 8, 1/6, −1/4) (6, 15, 8, 3/8, −1/4), (10, 15, 6, 1/4, −1/8)

![image 71](<2014-barg-finite-two-distance-tight-frames_images/imageFile71.png>)

![image 72](<2014-barg-finite-two-distance-tight-frames_images/imageFile72.png>)

![image 73](<2014-barg-finite-two-distance-tight-frames_images/imageFile73.png>)

- (16, 10, 6, 6) (5, 16, 10, 1/5, −3/5), (10, 16, 5, 1/5, −1/5) (6, 16, 10, 1/3, −1/3), (11, 16, 5, 3/11, −1/11)


![image 74](<2014-barg-finite-two-distance-tight-frames_images/imageFile74.png>)

![image 75](<2014-barg-finite-two-distance-tight-frames_images/imageFile75.png>)

![image 76](<2014-barg-finite-two-distance-tight-frames_images/imageFile76.png>)

REFERENCES

- [1] E. Bannai and Et. Bannai, A note on the spherical embeddings of strongly regular graphs, European J. Comb., 26 (2005), 1177–1179.
- [2] E. Bannai, T. Okuda, and M. Tagami, Spherical designs of harmonic index t, J. Approximation Theory, in press; Preprint available arXiv:1306:5101.
- [3] A. Barg and W.-H. Yu, New bounds for spherical two-distance sets, Experimental Mathematics, 22, no. 2, (2013), 187–194.
- [4] A. Barg and W.-H. Yu, New bounds on equiangular lines, in: Discrete Geometry and Algebraic Combinatorics, A. Barg abd O. Musin, eds., (Contemporary Mathematics, vol. 625), Amer. Math. Soc., Providence, RI, 2014, pp. 111–121.
- [5] J. J. Benedetto and M. Fickus, Finite normalized tight frames, Advances in Computational Math, Vol 18, nos. 2-4, (2003), 357–385.
- [6] B. Bodmann, P. Casazza, and R. Balan, Frames for linear reconstruction without phase, Proc. 42nd IEEE Annual Conference on Information Sciences and Systems (CISS 2008), Princeton, NJ, March 19-21, 2008, pp. 721–726.
- [7] A. E. Brouwer and W. H. Haemers, Spectra of graphs, Springer, New York e.a., (2012).
- [8] P. G. Casazza and G. Kutyniok (Editors), “Finite Frame Theory,” Birkha¨user, Boston (2012).
- [9] A. E. Brouwer and W. H. Haemers, Spectra of graphs, Springer, New York e.a., 2012.
- [10] P. Delsarte, J. M. Goethals, and J. J. Seidel, Spherical codes and designs, Geometriae Dedicata 6 (1977), 363–388.


- [11] C. Godsil and G. Royle, Algebraic Graph Theory, Springer, New York 2001.
- [12] D. Han, K. Kornelson, D. Larson, and E. Weber, Frames for Undergraduates, American Mathematical Society, Providence, RI, 2007.
- [13] R. B. Holmes and V.I. Paulsen, Optimal frames for erasures, Linear Alg. and Application, 377 (2004), 31-51.
- [14] J. Kovacˇevic´ and A. Chebira, Life Beyond Bases: The Advent of Frames (Part I-II), Signal Processing Magazine, IEEE, Volume 24 (2007), 86–104 and 115–125.
- [15] D. G. Larman, C. A. Rogers, and J. J. Seidel, On two-distance sets in Euclidean space, Bull. London Math. Soc. 9 (1977), 261–267.
- [16] P. W. H. Lemmens and J. J. Seidel, Equiangular lines, Journal of Algebra 24 (1973), 494–512.
- [17] J. H. van Lint and J.J. Seidel, Equiangular point sets in elliptic geometry Proc. Nedert. Akad. Wetensh. Series 69 (1966), 335-348.
- [18] O. R. Musin, Spherical two-distance sets, J. Combin. Theory Ser. A 116, no. 4 (2009), 988–995.
- [19] A. Neumaier, Distance matrices, dimension, and conference graphs, Indag. Math., 43, no. 4 (1981), 385–391.
- [20] H. Nozaki and M. Shinohara, A geometrical characterization of strongly regular graphs, Linear Alg. Appl. 437 (2012), 2587–2600.
- [21] J. J. Seidel, A survey of two-graphs, Colloquio Internazionale sulle Teorie Combinatorie (Rome, 1973), Tomo I, pp. 481–511. Atti dei Convegni Lincei, No. 17, Accad. Naz. Lincei, Rome, 1976.
- [22] M. A. Sustik, J. A. Tropp, I. S. Dhillon and R.W. Heath, Jr., On the existence of equiangular tight frames, Linear Alg. and Applications 426, no. 2-3 (2007), 619-635.
- [23] T. Strohmer and R. W. Heath, Grassmannian frames with applications to coding and communication, Appl. Comp. Harmonic Anal. 14, no. 3

(2003), 619-635.

- [24] S. Waldron, On the construction of equiangular frames from graph, Linear Alg. and its Applications 431, no. 11 (2009), 2228-2242.


