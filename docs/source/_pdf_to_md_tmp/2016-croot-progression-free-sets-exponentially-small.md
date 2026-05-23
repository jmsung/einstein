arXiv:1605.01506v2[math.NT]21May2016

PROGRESSION-FREE SETS IN Zn4 ARE EXPONENTIALLY SMALL

ERNIE CROOT, VSEVOLOD F. LEV, AND PETER´ PAL´ PACH†

Abstract. We show that for integer n ≥ 1, any subset A ⊆ Zn4 free of three-term arithmetic progressions has size |A| ≤ 4γn, with an absolute constant γ ≈ 0.926.

1. Background and Motivation

In his inﬂuential papers [R52, R53], Roth has shown that if a set A ⊆ {1, 2, . . ., N} does not contain three elements in an arithmetic progression, then |A| = o(N) and indeed, |A| = O(N/ log log N) as N grows. Since then, estimating the largest possible size of such a set has become one of the central problems in additive combinatorics. Roth’s original results were improved by Heath-Brown [H87], Szemer´edi [S90], Bourgain [B99], Sanders [S12, S11], and Bloom [B], the current record due to Bloom being |A| = O(N(log log N)4/ log N).

It is easily seen that Roth’s problem is essentially equivalent to estimating the largest possible size of a subset of the cyclic group ZN, free of three-term arithmetic progressions. This makes it natural to investigate other ﬁnite abelian groups.

We say that a subset A of an (additively written) abelian group G is progression-free if there do not exist pairwise distinct a, b, c ∈ A with a+ b = 2c, and we denote by r3(G) the largest size of a progression-free subset A ⊆ G. For abelian groups G of odd order, Brown and Buhler [BB82] and independently Frankl, Graham, and Ro¨dl [FGR87] proved that r3(G) = o(|G|) as |G| grows. Meshulam [M95], following the general lines of Roth’s argument, has shown that if G is an abelian group of odd order, then r3(G) ≤ 2|G|/ rk(G) (where we use the standard notation rk(G) for the rank of G); in particular, r3(Znm) ≤ 2mn/n. Despite many eﬀorts, no further progress was made for over 15 years, till Bateman and Katz in their ground-breaking paper [BK12] proved that r3(Zn3) = O(3n/n1+ε) with an absolute constant ε > 0.

Abelian groups of even order were ﬁrst considered in [L04] where, as a further elaboration on the Roth-Meshulam proof, it is shown that r3(G) < 2|G|/ rk(2G) for any ﬁnite abelian group G; here 2G = {2g: g ∈ G}. For the homocyclic groups of exponent 4 this

![image 1](<2016-croot-progression-free-sets-exponentially-small_images/imageFile1.png>)

† Supported by the Hungarian Scientiﬁc Research Funds (Grant Nr. OTKA PD115978 and OTKA K108947) and the J´anos Bolyai Research Scholarship of the Hungarian Academy of Sciences.

1

result was improved by Sanders [S11] who proved that r3(Zn4) = O(4n/n(log n)ε) with an absolute constant ε > 0. The goal of this paper is to further improve Sanders’s result, as follows.

Let H denote the binary entropy function; that is,

H(x) = −xlog2 x − (1 − x) log2(1 − x), x ∈ (0, 1), where log2 x is the base-2 logarithm of x. Theorem 1. If n ≥ 1 and A ⊆ Zn4 is progression-free, then letting

- 1

![image 2](<2016-croot-progression-free-sets-exponentially-small_images/imageFile2.png>)

- 2


γ := max

H(0.5 − ε) + H(2ε) : 0 < ε < 0.25 ≈ 0.926 we have

|A| ≤ 4γn.

The proof of Theorem 1 is presented in the next section. We note that the exponential reduction in Theorem 1 is ﬁrst of a kind for problems of

this sort.

Starting from Roth, the standard way to obtain quantitative estimates for r3(G) involves a combination of the Fourier analysis and the density increment technique; the only exception is [L12] where for the groups G ∼= Znq with a prime power q, the abovementioned Meshulam’s result is recovered using a completely elementary argument. In contrast, in the present paper we use the polynomial method, without resorting to the familiar Fourier analysis – density increment strategy.

For a ﬁnite abelian group G ∼= Zm

with positive integer m1 | · · · | mk, denote by rk4(G) the number of indices i ∈ [1, k] with 4 | mi. Since, writing n := rk4(G), the group G is a union of 4−n|G| cosets of a subgroup isomorphic to Zn4, as a direct consequence of Theorem 1 we get the following corollary.

⊕ · · · ⊕ Zm

1

k

Corollary 1. If G is a ﬁnite abelian group then, writing n := rk4(G), we have r3(G) ≤ 4−(1−γ)n|G|, where γ ≈ 0.926 is the constant of Theorem 1.

2. Proof of Theorem 1 The proof of Theorem 1 is based on the following lemma.

Lemma 1. Suppose that n ≥ 1 and d ≥ 0 are integers, P is a multilinear polynomial in n variables of total degree at most d over a ﬁeld F, and A ⊆ Fn is a set with |A| > 2 0≤i≤d/2 ni . If P(a − b) = 0 for all a, b ∈ A with a = b, then also P(0) = 0.

Proof. Let m := 0≤i≤d/2 ni , and let K = {K1, . . ., Km} be the collection of all sets K ⊆ [n] with |K| ≤ d/2. Writing for brevity

xI :=

xi, x = (x1, . . ., xn) ∈ Fn, I ⊆ [n],

i∈I

there exist coeﬃcients CI,J ∈ F (I, J ⊆ [n]) depending only on the polynomial P, such that for all x, y ∈ Fn we have

CI,J xIyJ

P(x − y) =

I,J⊆[n] I∩J=∅ |I|+|J|≤d

CI,J xI yJ.

CI,J yJ +

xI

=

I∈K

J∈K I⊆[n]\J d/2<|I|≤d−|J|

J⊆[n]\I |J|≤d−|I|

The right-hand side can be interpreted as the scalar product of the vectors u(x), v(y) ∈ F2m deﬁned by

ui(x) = xK

xI

, um+i(x) =

CI,K

i

i

I⊆[n]\Ki d/2<|I|≤d−|Ki|

and

vi(y) =

J⊆[n]\Ki |J|≤d−|Ki|

i,J yJ, vm+i(y) = yK

CK

i

for all 1 ≤ i ≤ m. Consequently, if we had P(a− b) = 0 for all a, b ∈ A with a = b, while P(0) = 0, this would imply that the vectors u(a) and v(b) are orthogonal if and only if a = b. As a result, the vectors u(a) would be linearly independent (an equality of the sort a∈A λau(a) = 0 with the coeﬃcients λa ∈ F after a scalar multiplication by v(b) yields λb = 0, for any b ∈ A). Finally, the linear independence of {u(a): a ∈ A} ⊆ F2m implies |A| ≤ 2m, contrary to the assumptions of the lemma.

Remark. It is easy to extend the lemma relaxing the multilinearity assumption to the assumption that P has bounded degree in each individual variable. Speciﬁcally, denoting by fδ(n, d) the number of monomials xi

1 . . .xi

n with 0 ≤ i1, . . ., in ≤ δ and i1+· · ·+in ≤ d, if P has all individual degrees not exceeding δ, and the total degree not exceeding d, then |A| > 2fδ(n, ⌊d/2⌋) along with P(a−b) = 0 (a, b ∈ A, a = b) imply P(0) = 0. Moreover, taking δ = d, or δ = |F| − 1 for F ﬁnite, one can drop the individual degree assumption altogether.

1

n

We will use the estimate

0≤i≤z

n i

< 2nH(z/n) (1)

valid for all integer n ≥ 1 and real 0 < z ≤ n/2.

Recall, that for integer n ≥ d ≥ 0, the sum di=0 ni is the dimension of the vector space of all multilinear polynomials in n variables of total degree at most d over the two-element ﬁeld F2. In particular, the dimension of the vector space of all multilinear polynomials in n variables over F2 is equal to the dimension of the vector space of all F2valued functions on Fn2, and it follows that any non-zero multilinear polynomial represents a non-zero function. These basic facts are used in the proof of Proposition 1 below.

For integer n ≥ 1, denote by Fn the subgroup of the group Zn4 generated by its involutions; thus, Fn is both the image and the kernel of the doubling endomorphism of Zn4 deﬁned by g  → 2g (g ∈ Zn4), and we have Fn ∼= Zn2.

Proposition 1. Suppose that n ≥ 1 and A ⊆ Zn4 is progression-free. Then for every 0 < ε < 0.25, the number of Fn-cosets containing at least 2nH(0.5−ε)+1 elements of A is less than 2nH(2ε).

Proof. Let R be the set of all those Fn-cosets containing at least 2nH(0.5−ε)+1 elements of A, and for each coset R ∈ R let AR := A ∩ R; thus, ∪R∈RAR ⊆ A (where the union is disjoint), and

|AR| ≥ 2nH(0.5−ε)+1, R ∈ R. (2) For a subset S ⊆ Zn4, write

2 · S := {s′ + s′′: (s′, s′′) ∈ S × S, s′ = s′′} and 2 ∗ S := {2s: s ∈ S}. The assumption that A is progression-free implies that the sets

B := ∪R∈R(2 · AR) ⊆ Fn and C := ∪R∈R(2 ∗ R) ⊆ Fn

are disjoint: this follows by observing that if 2r ∈ 2 · AR with some r ∈ R, then for each a ∈ r + Fn we have 2a = 2r ∈ 2 · AR ⊆ 2 · A. Furthermore, the sets 2 ∗ R are in fact pairwise distinct singletons (for 2r1 = 2r2 is equivalent to r1 − r2 ∈ Fn and thus to r1 + Fn = r2 + Fn), whence |C| = |R|.

Let d = n − ⌈2εn⌉ so that, in view of (2) and (1),

2

0≤i≤d/2

n i

< 2nH(0.5−ε)+1 ≤ |AR|, R ∈ R. (3)

Denoting by C the complement of C in Fn, and assuming that |R| ≥ 2nH(2ε) (contrary to what we want to prove), from (1) we get

![image 3](<2016-croot-progression-free-sets-exponentially-small_images/imageFile3.png>)

⌈2εn⌉−1

d

n i

n i

= 2n −

> 2n − 2nH(2ε) ≥ 2n − |R| = 2n − |C| = |C|.

![image 4](<2016-croot-progression-free-sets-exponentially-small_images/imageFile4.png>)

i=0

i=0

Consequently, identifying Fn with the additive group of the vector space Fn2, and accordingly considering B and C as subsets of Fn2, we conclude that the dimension of the vector space of all multilinear n-variate polynomials over the ﬁeld F2 exceeds the dimension of the vector space of all F2-valued functions on C. Thus, the evaluation map, associating with every polynomial the corresponding function, is degenerate. As a result, there exists a non-zero multilinear polynomial P ∈ F2[x1, . . ., xn] of total degree deg P ≤ d such that P vanishes on C. In particular, P vanishes on B ⊆ C, and therefore on each set 2·AR, for all R ∈ R. Fixing arbitrarily an element r ∈ R, the polynomial P(2r + x) thus vanishes whenever x ∈ 2 · (AR − r). Hence, also P(2r) = 0 by Lemma 1 (which is applicable in view of (3)); that is, P also vanishes on each singleton set 2∗AR, for all R ∈ R. It follows that P vanishes on C. However, P was chosen to vanish on C. Therefore, P vanishes on all of Fn2, and it follows that P is the zero polynomial. This is a contradiction showing that |R| < 2nH(2ε), and thus completing the proof.

![image 5](<2016-croot-progression-free-sets-exponentially-small_images/imageFile5.png>)

![image 6](<2016-croot-progression-free-sets-exponentially-small_images/imageFile6.png>)

![image 7](<2016-croot-progression-free-sets-exponentially-small_images/imageFile7.png>)

![image 8](<2016-croot-progression-free-sets-exponentially-small_images/imageFile8.png>)

Proof of Theorem 1. For x ≥ 0, let N(x) denote the number of Fn-cosets containing at least x elements of A; thus N(x) = 0 for x > 2n, and we can write

2n+1

|A| =

N(x) dx. (4) Trivially, we have N(x) ≤ 2n for all x ≥ 0, so that

0

2nH(1/4)+1

N(x) dx ≤ 2(H(1/4)+1)n+1 < 2 · 4γn. (5) On the other hand, the substitution x = 2nH(0.5−ε)+1 gives

0

2n+1

1/4

0.5 + ε 0.5 − ε

2nH(0.5−ε)+1N(2nH(0.5−ε)+1) log

dε, (6) and applying Proposition 1, the integral in the right-hand side can be estimated as

N(x) dx = n

![image 9](<2016-croot-progression-free-sets-exponentially-small_images/imageFile9.png>)

2nH(1/4)+1

0

1/4

1/4

0.5 + ε 0.5 − ε

2n(H(0.5−ε)+H(2ε)) log

2n(H(0.5−ε)+H(2ε)) dε < n · 2γn. (7)

2n

dε < 3n

![image 10](<2016-croot-progression-free-sets-exponentially-small_images/imageFile10.png>)

0

0

From (4)–(7) we get |A| < (n + 2) · 4γn, and to conclude the proof we use the tensor power trick: for integer k ≥ 1, the set A×· · ·×A ⊆ Zkn4 is progression-free and therefore |A|k < (kn + 2) · 4γkn

by what we have just shown. This readily implies the result.

References

[BK12] M. Bateman and N.H. Katz, New bounds on cap sets, J. Amer. Math. Soc. 25 (2012), no. 2, 585–613. [B] T.F. Bloom, A quantitative improvement for Roth’s theorem on arithmetic progressions,

submitted. [B99] J. Bourgain, On triples in arithmetic progression, Geom. Funct. Anal. 9 (1999), 968–984. [BB82] T.C. Brown and J.C. Buhler, A density version of a geometric Ramsey theorem, J. Combin.

Theory, Ser. A 32 (1982), 20–34. [FGR87] P. Frankl, G Graham, and V. Rodl¨ , On subsets of abelian groups with no 3-term arithmetic progression, J. Combin. Theory, Ser. A 45 (1987), 157–161. [H87] D.R. Heath-Brown, Integer sets containing no arithmetic progressions, J. London Math. Soc. 35 (1987), 385–394. [L04] V.F. Lev, Progression-free sets in ﬁnite abelian groups, J. Number Theory 104 (2004), no. 1, 162–169. [L12] , Character-free approach to progression-free sets, Finite Fields Appl. 18 (2012), no. 2, 378–383. [M95] R. Meshulam, On subsets of ﬁnite abelian groups with no 3-term arithmetic progressions, J. Combin. Theory Ser. A 71 (1995), no. 1, 168–172.

![image 11](<2016-croot-progression-free-sets-exponentially-small_images/imageFile11.png>)

- [R52] K. Roth, Sur quelques ensembles d’entiers, C. R. Acad. Sci. Paris 234 (1952), 388–390.
- [R53] , On certain sets of integers, J. London Math. Soc. 28 (1953), 104–109.


![image 12](<2016-croot-progression-free-sets-exponentially-small_images/imageFile12.png>)

[S09] T. Sanders, Roth’s theorem in Z4n, Anal. PDE 2 (2009), no. 2, 211–234. [S12] , On certain other sets of integers, J. Anal. Math. 116 (2012), 53–82. [S11] , On Roth’s theorem on progressions, Ann. of Math. (2) 174 (2011), no. 1, 619–636. [S90] E. Szemer´edi, Integer sets containing no arithmetic progressions, Acta Math. Hungar. 56

![image 13](<2016-croot-progression-free-sets-exponentially-small_images/imageFile13.png>)

![image 14](<2016-croot-progression-free-sets-exponentially-small_images/imageFile14.png>)

(1990), 155–158. E-mail address: ecroot@math.gatech.edu School of Mathematics, Georgia Institute of Technology, Atlanta, Georgia 30332,

USA E-mail address: seva@math.haifa.ac.il Department of Mathematics, The University of Haifa at Oranim, Tivon 36006, Israel E-mail address: ppp@cs.bme.hu Department of Computer Science and Information Theory, Budapest University of

Technology and Economics, 1117 Budapest, Magyar tudosok´ kor¨ utja´ 2, Hungary

