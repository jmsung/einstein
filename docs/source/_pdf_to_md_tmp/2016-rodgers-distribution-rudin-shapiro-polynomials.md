arXiv:1606.01637v3[math.CA]13Sep2017

ON THE DISTRIBUTION OF RUDIN-SHAPIRO POLYNOMIALS AND LACUNARY WALKS ON SU(2)

BRAD RODGERS

ABSTRACT. We characterize the limiting distribution of Rudin-Shapiro polynomials, showing that, normalized, their values become uniformly distributed in the disc. This resolves conjectures of Saffari and Montgomery. Our proof proceeds by relating the polynomials’ distribution to that of a product of weakly dependent random matrices, which we analyze using the representation theory of SU(2). Our approach leads us to a non-commutative analogue of the classical central limit theorem of Salem and Zygmund, which may be of independent interest.

1. INTRODUCTION The Rudin-Shapiro polynomials are deﬁned inductively as follows:

P0(z) = Q0(z) = 1, and

Pk+1(z) = Pk(z) + z2kQk(z), (1) Qk+1(z) = Pk(z) − z2kQk(z). (2)

Thus deﬁned, Pk and Qk are of degree 2k − 1 and have all coefﬁcients equal to 1 or −1. These polynomials were discovered independently by Golay [13], Shapiro [24], and Rudin [22] and in addition to having many interesting algebraic and combinatorial properties in their own right [5, 6], they play an important role in for instance signal processing [18], the study of ﬁnite automata [1], and especially as a source of counterexamples in classical analysis [19, 15].

Perhaps most importantly they furnish an example of polynomials P of arbitrarily high degree N with all coefﬁcients 1 or −1 such that |P(z)| ≪

√N for all |z| = 1. Indeed, for |z| = 1, it may be shown inductively that

![image 1](<2016-rodgers-distribution-rudin-shapiro-polynomials_images/imageFile1.png>)

|Pk(z)|2 + |Qk(z)|2 = 2k+1.

It remains an open problem whether there exist polynomials P of arbitrarily high degree N with all coefﬁcients 1 or −1 such that

√N ≪ |P(z)| ≪

√N for all |z| = 1. (See [21] for recent numerical evidence that such polynomials exist.1) As a consequence of results proved in this paper we will see that Rudin-Shapiro polynomials do not satisfy a lower bound of this sort – this has always been quite evident numerically, though there does not seem to be a proof of this fact already

![image 2](<2016-rodgers-distribution-rudin-shapiro-polynomials_images/imageFile2.png>)

![image 3](<2016-rodgers-distribution-rudin-shapiro-polynomials_images/imageFile3.png>)

![image 4](<2016-rodgers-distribution-rudin-shapiro-polynomials_images/imageFile4.png>)

1If the coefﬁcients are instead only restricted to be complex unimodular, such polynomials do indeed exist and in fact one can ensure |P(z)| ∼

√

![image 5](<2016-rodgers-distribution-rudin-shapiro-polynomials_images/imageFile5.png>)

N uniformly; see [14, 4, 7].

1

in the literature2 – and it is natural moreover to ask how far they deviate from such a lower bound. Investigations related to this question date at least back to Saffari in 1980, who let ω be a random variable distributed uniformly on the unit circle |ω| = 1 and asked about the radial distribution of Pk(ω). Saffari conjectured that for any n ≥ 0,

1 n + 1

Pk(ω) √

2n

∼

E

(3) as k → ∞ or equivalently that

![image 6](<2016-rodgers-distribution-rudin-shapiro-polynomials_images/imageFile6.png>)

![image 7](<2016-rodgers-distribution-rudin-shapiro-polynomials_images/imageFile7.png>)

![image 8](<2016-rodgers-distribution-rudin-shapiro-polynomials_images/imageFile8.png>)

2k+1

Pk(ω) √

2

∈ [α,β] ∼ β − α (4)

P

![image 9](<2016-rodgers-distribution-rudin-shapiro-polynomials_images/imageFile9.png>)

![image 10](<2016-rodgers-distribution-rudin-shapiro-polynomials_images/imageFile10.png>)

2k+1

as k → ∞, for 0 ≤ α < β ≤ 1. Saffari evidently did not publish this conjecture himself, and it ﬁrst appeared in print in work of Doche and Habsieger [8], who veriﬁed (3) for n ≤ 26. Erd´elyi [10] has considered closely related questions involving the Mahler measure of Rudin-Shapiro polynomials, and obtains absolute upper bounds for moments.

In this note we resolve Saffari’s conjecture in general:

- Theorem 1.1 (Saffari’s Conjecture). For ω a random variable uniformly distributed on the unit circle, (3) and (4) are true.

In fact with more work we will be able to resolve a more recent conjecture of Montgomery [19, 20] which generalizes Saffari’s: we show that Pk(ω)/

√

![image 11](<2016-rodgers-distribution-rudin-shapiro-polynomials_images/imageFile11.png>)

2k+1 tends towards uniform distribution in the unit disc D = {z ∈ C : |z| ≤ 1}, as k → ∞:

- Theorem 1.2 (Montgomery’s Conjecture). For any rectangle E ⊆ D,


1 π|E|,

Pk(ω) √

∈ E ∼

P

![image 12](<2016-rodgers-distribution-rudin-shapiro-polynomials_images/imageFile12.png>)

![image 13](<2016-rodgers-distribution-rudin-shapiro-polynomials_images/imageFile13.png>)

![image 14](<2016-rodgers-distribution-rudin-shapiro-polynomials_images/imageFile14.png>)

2k+1

as k → ∞.

Our proofs of both results proceed by characterizing the distribution of a product of weakly dependent random matrices. Note that from the inductive deﬁnition (1) and (2), we have

1 z2k−1 1 −z2k−1 ···

1 z2k 1 −z2k

1 z 1 −z

1 0

Pk(z) Qk(z)

=

We will work with a normalized version of the matrices above. Deﬁne g(z) :=

iz−1 iz iz−1 −iz

1 √2

,

![image 15](<2016-rodgers-distribution-rudin-shapiro-polynomials_images/imageFile15.png>)

![image 16](<2016-rodgers-distribution-rudin-shapiro-polynomials_images/imageFile16.png>)

.

![image 17](<2016-rodgers-distribution-rudin-shapiro-polynomials_images/imageFile17.png>)

2The polynomials Pk satisfy the recursion Pk+2(z) = (1 − z2k+1)Pk+1(z) + 2z2k+1Pk(z) (see [6]), and so it follows inductively that Pk(−1) = 0 for odd k. In this way, H. Montgomery has pointed out, one may observe for odd k that Pk(z) does not satisfy lower bound of this sort, but it is not clear that a similarly simple proof exists for even k.

which is an element of SU(2) for |z| = 1. We have

√

![image 18](<2016-rodgers-distribution-rudin-shapiro-polynomials_images/imageFile18.png>)

Pk(z2)/

2k+1 Qk(z2)/

(ik+1z2k+1−1)

= g(z2k)··· g(z)

√

![image 19](<2016-rodgers-distribution-rudin-shapiro-polynomials_images/imageFile19.png>)

2k+1

1 0

. (5)

We note Pk(ω) has the same distribution as Pk(ω2), so Saffari’s conjecture will directly follow from

- Theorem 1.3 (Equidistribution in SU(2)). As k → ∞, the distribution of g(ω2k)··· g(ω) tends to Haar measure on SU(2).


√

Indeed, this shows that the distribution of |Pk(ω)/

2

1 0

1 0

,g

,

![image 20](<2016-rodgers-distribution-rudin-shapiro-polynomials_images/imageFile20.png>)

2k+1|2 tends to that of

for g ∈ SU(2) chosen according to Haar measure. We leave it to the reader to verify that this implies (4) (using for instance an Euler angle parameterization of g, see e.g. [12, Prop. 7.4.1]).

Returning our attention to the representation (5), we shall also show

Lemma 1.4. The random variables ω2k+1−1 and g(ω2k)··· g(ω) become independent as k → ∞.

As a consequence we immediately obtain Montgomery’s conjecture and more generally

- Theorem 1.5 (Equidistribution in U(2)). Let


1 √2

1 ω 1 −ω

.

G(ω) :=

![image 21](<2016-rodgers-distribution-rudin-shapiro-polynomials_images/imageFile21.png>)

![image 22](<2016-rodgers-distribution-rudin-shapiro-polynomials_images/imageFile22.png>)

As k → ∞, the distribution of G(ω2k)··· G(ω) tends to Haar measure on U(2).

√

![image 23](<2016-rodgers-distribution-rudin-shapiro-polynomials_images/imageFile23.png>)

2k+1 tends to that of

Montgomery’s conjecture is thus veriﬁed by noting the distribution of Pk(ω)/

1 0

1 0

,G

,

where G ∈ U(2) is chosen according to Haar measure. This may again be analyzed using Euler angles. Alternatively, perhaps more simply, Montgomery’s conjecture follows from the Lemma and Theorem 1.1 by noting that the distribution of Pk(ω)/

√

√

![image 24](<2016-rodgers-distribution-rudin-shapiro-polynomials_images/imageFile24.png>)

![image 25](<2016-rodgers-distribution-rudin-shapiro-polynomials_images/imageFile25.png>)

2k+1| where ζ is an independent random variable uniformly distributed on the unit circle.3

2k+1 tends to that of ζ ·|Pk(ω)/

The moral of Theorems 1.3 and 1.5 should be clear; it is that the sequence of

random variables ω,ω2,...,ω2k resemble i.i.d. variables ω0,ω1,...,ωk and therefore the matrix product in Theorem 1.3 for instance has a distribution close to that of

![image 26](<2016-rodgers-distribution-rudin-shapiro-polynomials_images/imageFile26.png>)

3This may be compared to the results proved in [11] for the class of ﬂat polynomials.

g(ω0)··· g(ωk). But this latter matrix product is just a random walk on the compact group SU(2), which is known to equidistribute unless certain obvious obstacles (support on a proper closed subgroup or support on a coset of a proper closed subgroup [17]) arise, which in this case they do not. These theorems may thus be thought of as a non-commutative version of the well-known central limit theorem of Salem and Zygmund for lacunary trigonometric series [23].

There is a sense in which this analogy to statistical independence may be misleading and this is discussed in the ﬁnal section of this paper. In any case it is not by a comparison to a product of i.i.d. variables that we prove Theorem 1.3 and Lemma 1.4. Instead we return to earlier principles and make use of the representation theory of SU(2).

We note that very recently and independently, D. Zeilberger [9] has sketched a different possible approach to Saffari’s conjecture from the one we take. Zeilberger’s sketch is contingent on the algorithmic proof of certain identities which have been found empirically and also a claim called the small change hypothesis which is used to bound error terms. This hypothesis does not necessarily follow algorithmically at the present moment, but it might after an explicit identiﬁcation of certain terms that arise in his sketch. [9] also computes the asymptotics of moments E[Pk(ω)]n[Pk(ω)]m for small n and m, with an output consistent with Montgomery’s conjecture.

![image 27](<2016-rodgers-distribution-rudin-shapiro-polynomials_images/imageFile27.png>)

2. EQUIDISTRIBUTION IN SU(2): A PROOF OF THEOREM 1.3

This section is devoted to a proof of Theorem 1.3 regarding equidistribution in SU(2). Our proof of Lemma 1.4 and thus Theorem 1.5, which generalizes the result to U(2), uses similar methods but adds an additional layer of complexity and will come in the next section.

Our approach will be to demonstrate for every nontrivial irreducible representation π of SU(2) that4

Eπ(g(ω2k)··· g(ω)) = Eπ(g(ω2k))··· π(g(ω)) → 0. (6)

By a well-known criterion, this is necessary and sufﬁcient to prove the theorem. Indeed, in general we have

- Theorem 2.1. For H a compact Lie group and h1,h2,h3,... a sequence of H-valued random elements, the distributions of hk tend to Haar measure if and only if for every nontrivial irreducible representation π of H,


Eπ(hk) → 0. (7)

Theorem 2.1 is a corollary of Theorem 4.2.5 of [3]. Theorem 4.2.5 there is a slightly more general result characterizing arbitrary limiting distributions; the case

![image 28](<2016-rodgers-distribution-rudin-shapiro-polynomials_images/imageFile28.png>)

4By (6) we mean that the expectation of all matrix coefﬁcients of the representations tend to 0; that is for any nontrivial irreducible representation (π, Cn), we have E u, π(g(ω2k))· · · π(g(ω))v → 0 for all vectors u, v ∈ Cn.

that the limiting distribution of the random elements is Haar measure follows from Example 2 of section 4.2 in the same source.

This approach of demonstrating (6) we note, is very much just a variant of the moment method in this context, and fortunately the representation theory of SU(2) is elegant and well-understood (see, e.g. [12], [25], or [2]). We recall the necessary facts here.

Any matrix of SU(2) has the form

α β −β α

g =

,

![image 29](<2016-rodgers-distribution-rudin-shapiro-polynomials_images/imageFile29.png>)

![image 30](<2016-rodgers-distribution-rudin-shapiro-polynomials_images/imageFile30.png>)

with |α|2 + |β|2 = 1. Nontrivial irreducible representations of the matrix g are parameterized by semi-integers ℓ = 1/2,1,3/2,2,... and consist of the matrices with entries

![image 31](<2016-rodgers-distribution-rudin-shapiro-polynomials_images/imageFile31.png>)

dz 2πiz

- (ℓ − m)!(ℓ + m)!

![image 32](<2016-rodgers-distribution-rudin-shapiro-polynomials_images/imageFile32.png>)

- (ℓ − n)!(ℓ + n)! Γ


(αz + γ)ℓ−n(βz + δ)ℓ+nzm−ℓ

tℓm,n(g) =

![image 33](<2016-rodgers-distribution-rudin-shapiro-polynomials_images/imageFile33.png>)

where m,n ∈ {−ℓ,−ℓ + 1,...,ℓ}, and the contour Γ is the unit circle. (Here the range of m and n is such that ℓ − n and ℓ + n are integers.) Note that

tℓm,n(g(ω)) = τm,nℓ ω2n (8) with

![image 34](<2016-rodgers-distribution-rudin-shapiro-polynomials_images/imageFile34.png>)

i2ℓ 2ℓ Γ

dz 2πiz

- (ℓ − m)!(ℓ + m)!

![image 35](<2016-rodgers-distribution-rudin-shapiro-polynomials_images/imageFile35.png>)

- (ℓ − n)!(ℓ + n)!


(z + 1)ℓ−n(z − 1)ℓ+nzm−ℓ

τm,nℓ :=

.

![image 36](<2016-rodgers-distribution-rudin-shapiro-polynomials_images/imageFile36.png>)

![image 37](<2016-rodgers-distribution-rudin-shapiro-polynomials_images/imageFile37.png>)

Note that τℓ is itself a unitary matrix, corresponding to the representation of the matrix g(1).

If ℓ = 1/2,3/2,5/2,... then it is transparent that Etℓ(g(ω2k))··· tℓ(g(ω)) = 0,

for all n ≥ 0, since every entry of the matrix product of which we are taking the expectation will be a Laurent polynomial in ω with only odd powers appearing.

On the other hand, for ℓ = 1,2,... nothing so simple is true. Each entry of tℓ(g(ω2k))··· tℓ(g(ω)) will be a Laurent polynomial in ω with exclusively even powers however, so at least we have

Etℓ(g(ω2k))··· tℓ(g(ω)) = Etℓ(g(ω2k−1))··· tℓ(g(ω1/2)). We use the notation:

ω−ℓ



Tℓ(ω) := τℓ

 

ω−ℓ+1

...

ωℓ



 

so that Tℓ(ω) = tℓ(g(ω1/2)).

In this notation, we must show ETℓ(ω2k)··· Tℓ(ω) → 0 to prove the theorem; in turn to show this we need only show that all constant coefﬁcients in Tℓ(ω2k)··· Tℓ(ω) go to 0. To this end we note the following two facts:

- (i) The matrix entries of Tℓ(ω2k)··· Tℓ(ω) will be Laurent polynomials in ω lying in the span of {ω(2k+1−1)ℓ,...,ω−(2k+1−1)ℓ}.
- (ii) To ﬁnd a coefﬁcient of ων2k+1 for ν ∈ Z (and in particular the constant coefﬁcient) of a matrix entry of


Tℓ(ω2k)··· Tℓ(ω) = Tℓ(ω2k) × Tℓ(ω2k−1)··· Tℓ(ω)

we need only keep track of the coefﬁcients of ωµ2k for µ ∈ Z in the entries of Tℓ(ω2k−1)··· Tℓ(ω).

We let P be the space of Laurent polynomials in ω (with complex coefﬁcients) and deﬁne an operator Sℓ on the product space P2ℓ+1 as follows: for

A = A−ℓ(ω), ··· ,Aℓ(ω) T ∈ P2ℓ+1, if

Tℓ(ω)A = j∈Z β−ℓ(j)ωj, ··· , j∈Z βℓ(j)ωj T where the coefﬁcients βh(j)are deﬁned by this relation, we deﬁne

SℓA := j∈Z β−ℓ(2j)ωj, ··· , j∈Z βℓ(2j)ωj T . We note, in view of fact (ii) above, that for arbitrary v ∈ C2ℓ+1

ETℓ(ω2k)··· Tℓ(ω)v = E(Sℓ)k+1v. (9)

Moreover, deﬁne the space of Laurent polynomials Pℓ := spanC{ω−(ℓ−1),...,ωℓ−1}. Note that Sℓ is a linear operator mapping the ﬁnite dimensional complex vector

space (Pℓ)2ℓ+1 into itself. We let Sℓ be the operator Sℓ restricted to (Pℓ)2ℓ+1, and rewrite the vector in (9) as

E(Sℓ)k+1v. (10) If we show that for all ℓ the spectral radius of Sℓ is less than 1, then (Sℓ)k+1 → 0 as k → ∞, and (10) likewise will tend to 0 for all vectors v which implies the theorem. We let ρ(·) denote the spectral radius of an operator; the remainder of this section is devoted to a proof that ρ(Sℓ) < 1.

We make the following observation:

- Proposition 2.2. In the above notation, ρ(Sℓ) ≤ 1. Moreover, if ρ(Sℓ) = 1, then there must exist non-zero A ∈ (Pℓ)2ℓ+1 such that


Tℓ(ω)A(ω) = cA(ω2).

Proof. From the deﬁnition if Sℓ has an eigenvalue c, there must exist non-zero A ∈ (Pℓ)2ℓ+1 and B ∈ P2ℓ+1 with

Tℓ(ω)A(ω) = cA(ω2) + ωB(ω2),

by separating the polynomial vector on the left hand side into odd and even powers. But because Tℓ(ω) is unitary and A(ω2) and ωB(ω2) have complementary powers, this implies that

E A(ω) 2ℓ2 = |c|2 · E A(ω2) 2ℓ2 + E B(ω2) 2ℓ2

= |c|2 · E A(ω) 2ℓ2 + E B(ω) 2ℓ2. (11)

This obviously implies |c| ≤ 1, so ρ(Sℓ) ≤ 1. Moreover, if ρ(Sℓ) = 1, then |c| = 1, and (11) implies that B = 0.

We now suppose that it is the case that ρ(Sℓ) = 1, aiming at a proof by contradiction. By the proposition, we will obtain a contradiction if we show that for |c| = 1, the only A ∈ (Pℓ)2ℓ+1 satisfying Tℓ(ω)A(ω) = cA(ω2) is A = 0. Labeling the coefﬁcients of A, we are looking to ﬁnd numbers αh(j) such that

ω−ℓ





   = c

  

  

  

ℓ−1 j=−(ℓ−1) α−ℓ(j)ωj

ℓ−1 j=−(ℓ−1) α−ℓ(j)ω2j

ω−(ℓ−1)

τℓ

...

.

.

 

 

ℓ−1 j=−(ℓ−1) αℓ(j)ωj

ℓ−1 j=−(ℓ−1) αℓ(j)ω2j

ωℓ

By equating the coefﬁcient of ων in each coordinate of the two column vectors above we obtain a homogeneous system of linear equations in the αh(j). We give a proof that the only solution of this system of equations is αh(j) = 0 for all h,j.

Let L(ν) be the linear equation in the coefﬁcients αh(j) that results from examining the coefﬁcient of ων in the system above. Meaningful information is got from L(ν) for −2ℓ + 1 ≤ ν ≤ 2ℓ − 1; in this range L(ν) becomes









α−ℓ(ν + ℓ) α−ℓ+1(ν + ℓ − 1)

α−ℓ(ν/2) α−ℓ+1(ν/2)

τℓ

= c

 

 

 

 

. αℓ(ν − ℓ)

. αℓ(ν/2)

with the convention that αh(j) = 0 if j is not an integer or |j| > ℓ − 1.

The information we need about the matrix τℓ in solving this system is not very special. The properties we need are contained in

- Proposition 2.3. For ℓ = 1,2,... the (2ℓ + 1) × (2ℓ + 1) matrix τℓ satisﬁes the following properties


- a) τℓ is invertible.
- b) |τ00ℓ | < 1.
- c) The matrix τℓ is such that if any one of the linear equations below hold,






β−ℓ

.

β−1 0 0

τℓ

=

 

.

0

 





- γ0 0
- γ1 0
- γ2


.

 

 

γℓ

or τℓ









β−ℓ

0

- γ0 0
- γ1 0


.

β−1 0 0

=

 

.

0

.

 

 

 

0





0





- γ0 0
- γ1 0
- γ2


.

0 0 β1

or τℓ

=

.

 

 

βℓ

.

 

 

γℓ

then βi = 0 and γi = 0 for all i.





0





0

- γ0 0
- γ1 0


.

0 0 β1

or τℓ

=

,

.

 

 

βℓ

.

 

 

0

Proof. Of these properties, a) is true simply because τℓ is unitary and b) is straightforward to verify. For c), we will show that the ﬁrst of these linear equations implies βi,γi = 0 for all i, with the others being handled similarly. We make the linear change of variables

(−1)ℓ 2ℓ

1 (2ℓ − i)!(2i)!

1 (ℓ − n)!(ℓ + n)!

β−n, γi′ :=

β−′ n :=

γi,

![image 38](<2016-rodgers-distribution-rudin-shapiro-polynomials_images/imageFile38.png>)

![image 39](<2016-rodgers-distribution-rudin-shapiro-polynomials_images/imageFile39.png>)

![image 40](<2016-rodgers-distribution-rudin-shapiro-polynomials_images/imageFile40.png>)

![image 41](<2016-rodgers-distribution-rudin-shapiro-polynomials_images/imageFile41.png>)

![image 42](<2016-rodgers-distribution-rudin-shapiro-polynomials_images/imageFile42.png>)

and note from the deﬁnition of τℓ that the ﬁrst linear equation is equivalent to the polynomial identity

β−′ ℓ(z + 1)2ℓ + β−′ ℓ+1(z + 1)2ℓ−1(z − 1) + β−′ 1(z + 1)ℓ+1(z − 1)ℓ−1

= γ0′ z2ℓ + γ1′ z2ℓ−2 + ··· + γℓ′.

We let P(z) := γ0′ zℓ +γ1′ zℓ−1 +···+γℓ′. Then (z +1)ℓ+1|P(z2). But P((−z)2) = P(z2), so (z − 1)ℓ+1|P(z2) also. Since (z + 1)ℓ+1 and (z − 1)ℓ+1 are coprime, this implies by multiplying the two factors together that (z2−1)ℓ+1|P(z2) and therefore that (z − 1)ℓ+1|P(z). Yet deg P(z) ≤ ℓ, so we must have P = 0. Because P = 0, we have γi = 0 for all i and βi = 0 for all i as well.

Using this proposition, we examine the linear equations L(−2ℓ + 1), L(−2ℓ + 3),..., L(2ℓ−1). By writing out the resulting equations and utilizing the invertibility of τℓ, one sees that the (2ℓ + 1) × (2ℓ − 1) matrix

α−ℓ(−ℓ + 1) α−ℓ(−ℓ + 2) ··· α−ℓ(ℓ − 1) α−ℓ+1(−ℓ + 1)





... .

α :=

 

 

. . αℓ(−ℓ + 1) ··· ··· αℓ(ℓ − 1)

with 4ℓ−1 skew-diagonals in total, has entirely 0 entries along its alternating skewdiagonals (that is, from top left, its 1st, 3rd,..., (4ℓ − 1)th skew-diagonals).

We now consider L(−2ℓ+2), which using the information we have just obtained reduces to the equation





0 α−ℓ+1(−ℓ + 1) 0 α−ℓ+3(−ℓ + 1)





α−ℓ(−ℓ + 2) α−ℓ+1(−ℓ + 1) 0 . 0

τℓ

= c

 

 

 

 

. 0

By part c) of Proposition 2.3, both vectors in the above equation must be 0, so that the second skew-diagonal of α also consists of 0 entries, as does the ﬁrst (leftmost) column.

In turn, updating α to reﬂect the fact that its ﬁrst column is 0, the linear equation L(−2ℓ + 4) becomes









α−ℓ(−ℓ + 4)

α−ℓ(−ℓ + 2) 0

- α−ℓ+1(−ℓ + 3)
- α−ℓ+2(−ℓ + 2) 0


α−ℓ+2(−ℓ + 2) 0 . αℓ(−ℓ + 2)

τℓ

= c

 

 

 

 

. 0

Again by part c) of the proposition this implies both vectors above are 0, so that the fourth skew-diagonal and second column of α consists of 0 entries.

Continuing on in this fashion, after L(−2ℓ+2) and L(−2ℓ+4), we may consider L(−2ℓ + 6),...,L(−2), with L(−2ℓ + 2j) becoming one of the two equations:

α−ℓ(−ℓ + 2j) . α−ℓ+j(−ℓ + j) 0 . 0













0 α−ℓ+1(−ℓ + j) 0 α−ℓ+3(−ℓ + j)

α−ℓ(−ℓ + j) 0

α−ℓ+2(−ℓ + j) 0 . αℓ(−ℓ + j)

τℓ

= c

or c

.

 

 

 

 

 

 

. 0

In either case, part c) of the proposition implies that the vectors above are 0. Taken all together we see that the ﬁrst ℓ−1 columns of α consist of 0 entries, and likewise the 2nd, 4th, ..., (2ℓ − 2)th skew-diagonals consist of 0 entries as well.

This same argument may be run in the reverse direction by considering L(2ℓ−2)), L(2ℓ − 4)),...,L(2), with the result that the last ℓ − 1 columns of α consist of 0 entries, as do the (4ℓ − 2)th, (4ℓ − 4)th,..., (2ℓ + 2)th skew-diagonals.

We have therefore shown that all skew-diagonals but the middle 2ℓth (out of 4ℓ− 1) consist of 0 entries. Likewise all columns, except for perhaps the middle ℓth (out of 2ℓ − 1) consist of 0 entries. By combining the two pieces of information, one

sees that that all entries of the matrix α except perhaps α0(0) are equal to 0. But then L(0) reduces to the statement that τ00ℓ α0(0) = cα0(0), which by part b) of

- Proposition 2.3 is impossible for |c| = 1 unless α0(0) = 0 as well.

Hence all eigenvalues of the operator Sℓ must be smaller in modulus than 1 as claimed, and Theorem 1.3 follows.

3. INDEPENDENCE OF DETERMINANT AND NORMALIZED ENTRIES: A PROOF OF LEMMA 1.4

In this section we prove Lemma 1.4. By virtue of the Peter-Weyl theorem, to prove that ω2k+1−1 and g(ω2k)··· g(ω) become independent as k → ∞, it will be sufﬁcient to show that

E(ω2k+1−1)λπ(g(ω2k)··· g(ω)) = Eωλ2kπ(g(ω2k))··· ωλπ(g(ω)) → 0 (12)

as k → ∞, for any ﬁxed λ ∈ Z and irreducible representation π of SU(2). Our proof will mimic the proof the Theorem 1.3 in the last section. We break the proof into two cases.

- Case 1: λ is even. In this case, as before, for π = tℓ with ℓ = 1/2,3/2,..., it is clear that (12) is true since each matrix entry of which we are taking the expectation will be a Laurent polynomial in ω with only odd powers. So it will sufﬁce in this case to consider π = tℓ with ℓ = 1,2,....
- Case 2: λ is odd. In this case, for π = tℓ with ℓ = 1,2,... it is clear that (12) is true, for the same reason as in case 1. Hence it will sufﬁce to consider π = tℓ with ℓ = 1/2,3/2,....


We analyze case 2 ﬁrst. For ℓ = 1/2,3/2,... let Tℓ(ω) = tℓ(g(ω1/2)) and observe that the problem reduces to showing that

Eω(λ/2)2kTℓ(ω2k)··· ωλ/2Tℓ(ω) → 0. (13) Note that

ωλ/2Tℓ(ω) = τℓ



 

ωλ/2−ℓ

ωλ/2−ℓ+1

...

ωλ/2+ℓ



 

so although λ/2 and ℓ are half-integers, all powers of ω appearing above are integers. We will need a result similar to Proposition 2.3 for half-integer5 ℓ.

- Proposition 3.1. For ℓ = 1/2,3/2,... the (2ℓ+1)×(2ℓ+1) matrix τℓ satisﬁes the following properties


- a) τℓ is invertible.
- b) |τ−ℓ ℓ,−ℓ| < 1 and |τℓ,ℓℓ | < 1.


![image 43](<2016-rodgers-distribution-rudin-shapiro-polynomials_images/imageFile43.png>)

5Note that this implies 2ℓ + 1 is now an even integer.

- c) The matrix t˜ℓ is such that if any one of the linear equations below hold,






β−ℓ





γ0 0 γ1 0

.

β−1/2 0

τℓ

=

or τℓ





β−ℓ



.

β−1/2 0

=

0

- γ0 0
- γ1




 

 

 

 

.

.

 

 

 

 

.

.

0

γℓ−1/2

0

0









0

0









- γ0 0
- γ1 0


0

- γ0 0
- γ1


.

.

0 β1/2

0 β1/2

or τℓ

or τℓ

=

=

,

 

 

 

 

.

.

 

 

 

 

.

.

0

γℓ−1/2

βℓ

βℓ

then βi = 0 and γi = 0 for all i.

Proof. a) and b) are of course straightforward, while c) follows by mimicking the argument in Proposition 2.3.

In demonstrating (13), we consider four possibilities:

- 1) If 0 ∈/ [λ/2 − ℓ,λ/2 + ℓ], then the left hand side of (13) is 0 for all k.
- 2) If 0 = λ/2 − ℓ, then all entries of ωλ/2Tℓ(ω) are polynomials in ω (i.e. no negative powers appear) and by inspection of matrix entries,

Eω(λ/2)2kTℓ(ω2k)··· ωλ/2Tℓ(ω) = (tℓ−ℓ,−ℓ)k

  

tℓ−ℓ,−ℓ 0 ···

. .

... tℓℓ,−ℓ 0 ···

   → 0,

by part b) of the proposition.

- 3) If 0 = λ/2 + ℓ, then all entries of ωλ/2Tℓ(ω) are polynomials in ω−1 (i.e. no positive powers appear) and in this case,

Eω(λ/2)2kTℓ(ω2k)··· ωλ/2Tℓ(ω) = (tℓℓ,ℓ)k

  

··· 0 tℓ−ℓ,ℓ

... . . ··· 0 tℓℓ,ℓ

   → 0,

again by part b) of the proposition.

- 4) Finally, if 0 ∈ (λ/2 − ℓ,λ/2 + ℓ), then we proceed along lines similar to the last section. We note much as before


- (i) The matrix entries of ω(λ/2)2kTℓ(ω2k)··· ωλ/2Tℓ(ω) will be Laurent polynomials in ω lying in the span of {ω(2k+1−1)(λ/2+ℓ),...,ω(2k+1−1)(λ/2−ℓ)}.


- (ii) The coefﬁcients of ων2k+1 for ν ∈ Z (and in particular constant coefﬁcients) of ω(λ/2)2kTℓ(ω2k)··· ωλ/2Tℓ(ω) are determined entirely by the coefﬁcients of ων2k for ν ∈ Z of ω(λ/2)2k−1Tℓ(ω2k−1)··· ωλ/2Tℓ(ω).


We continue to let P be the space of Laurent polynomials in ω and deﬁne the operator Sℓ,λ on P2ℓ+1 as follows: if for A ∈ P2ℓ+1,

ωλ/2Tℓ(ω)A = j∈Z β−ℓ(j)ωj, ··· , j∈Z βℓ(j)ωj T , deﬁne

Sℓ,λA := j∈Z β−ℓ(2j)ωj, ··· , j∈Z βℓ(2j)ωj T . Then just as before, for any v ∈ C2ℓ+1, we have

Eω(λ/2)2kTℓ(ω2k)··· ωλ/2Tℓ(ω) = E(Sℓ,λ)k+1v.

We deﬁne Pℓ,λ := spanC{ωλ/2−ℓ+1,...,ωλ/2+ℓ−1}, and note that Sℓ,λ maps (Pℓ,λ)2ℓ+1 into itself, and moreover in this fourth case C2ℓ+1 ⊂ (Pℓ,λ)2ℓ+1. Thus letting Sℓ,λ be the operator Sℓ,λ restricted to the ﬁnite dimensional complex vector space (Pℓ,λ)2ℓ+1, if as before we demonstrate ρ(Sℓ,λ) < 1, we will be done.

The same argument we used in the previous section shows that we will have such a bound on the spectral radius provided there is no nonzero (2ℓ+1)×(2ℓ−1) array of numbers αh(j) such that

ω−ℓ





j α−ℓ(j)ωj

j α−ℓ(j)ω2j

  

   = c

  

  

ω−(ℓ−1)

ωλ/2τℓ

...

. j αℓ(j)ωj

. j αℓ(j)ω2j

 

 

ωℓ

for a constant |c| = 1, where in each sum j runs from λ/2 − ℓ + 1 to λ/2 + ℓ − 1.

Let L(ν) be the linear equation obtained from examining the coefﬁcient of ων. The argument will be the same as the previous section except now there will be no need to examine an extraneous middle column. We ﬁrst consider ω taken to an odd power, that is the equations L(λ−2ℓ+1),L(λ−2ℓ+3),...,L(λ+2ℓ−1), to see that the array (αh(j)) has entries all 0 across alternating skew diagonals. We then turn to even powers, considering in succession L(λ −2ℓ +2),L(λ − 2ℓ + 4),...,L(λ − 1), showing that the ﬁrst (2ℓ + 1)/2 columns consist of 0 entries by using Proposition 3.1. Finally consider L(λ+2ℓ−2),...,L(λ+1) to see the same for the last (2ℓ+1)/2 columns. This veriﬁes that indeed all entries of any such array (αh(j)) must be 0. Hence ρ(Sℓ,λ) < 1 and (13) is true, which completes the analysis of case 2.

What remains is case 1. This is much the same argument and we leave the details to the reader. Again we must break the proof up into cases depending upon whether 0 lies outside, on the boundary of, or inside the interval [λ/2 − ℓ,λ/2 + ℓ]. If 0 lies outside, matters are again trivial. In the case that 0 lies on the boundary, we need the additional computation that for ℓ = 1,2,..., we have |τ−ℓ ℓ,−ℓ| < 1 and |τℓ,ℓℓ | < 1, but use the same argument. Analysis of the case that 0 lies inside the interval does not substantially differ from that in section 1, and in particular all necessary facts about the matrix τℓ have already been proved there.

4. A REMARK ON EQUIDISTRIBUTION

The proofs we have given of the equidstribution results Theorems 1.3 and 1.5 have depended upon the special form of the matrices g(ω) and G(ω). It is natural to ask whether this need be so. Indeed, by the analogy with random walks made in the introduction, one may be led to believe more generally that for a compact group H and a function f : R/Z → H such that f is supported on neither a proper closed subgroup (’non-degeneracy’) nor a coset of a proper closed subgroup (’aperiodicity’), the product

f(2kt)f(2k−1t)··· f(t), (14) will equidistribute on H as k → ∞, where t ∈ R/Z is a random variable with uniform distribution. (More generally one may think to replace multiplication by 2 by another ergodic or mixing action on a probability space.)

Theorems 1.3 and 1.5 furnish examples of such a phenomenon, but it does not hold in general. Indeed for H = Z/2Z, let

- 0 if t ∈ [0, 18) ∪ [21, 58) ∪ [34,1)

![image 44](<2016-rodgers-distribution-rudin-shapiro-polynomials_images/imageFile44.png>)

![image 45](<2016-rodgers-distribution-rudin-shapiro-polynomials_images/imageFile45.png>)

![image 46](<2016-rodgers-distribution-rudin-shapiro-polynomials_images/imageFile46.png>)

![image 47](<2016-rodgers-distribution-rudin-shapiro-polynomials_images/imageFile47.png>)

- 1 if t ∈ [18, 12) ∪ [85, 34)


f(t) =

![image 48](<2016-rodgers-distribution-rudin-shapiro-polynomials_images/imageFile48.png>)

![image 49](<2016-rodgers-distribution-rudin-shapiro-polynomials_images/imageFile49.png>)

![image 50](<2016-rodgers-distribution-rudin-shapiro-polynomials_images/imageFile50.png>)

![image 51](<2016-rodgers-distribution-rudin-shapiro-polynomials_images/imageFile51.png>)

and extend f periodically. Then for k ≥ 1, one may see that

P(f(2kt)··· f(t) = 0) = 5/8, which certainly does not tend to 1/2.

It would be interesting nonetheless to understand better what general conditions on f ensure that products like (14) equidistribute. Such products bear a resemblance to those arising in certain noncommutative ergodic theorems [16], but involve a different sort of averaging at a different scale and therefore seem to require different techniques.

5. ACKNOWLEDGEMENTS

I thank Hugh Montgomery for a number of helpful discussions regarding this problem along with making his notes on Rudin-Shapiro polynomials available to me and also Anders Karlsson, Jeff Lagarias, Alon Nishry, and Doron Zeilberger for helpful feedback.

REFERENCES

- [1] J.-P. Allouche and J. Shallit. Automatic Sequences: Theory, Applications, Generalizations. Cambridge University Press (2003).
- [2] G. E. Andrews, R. Askey, and R. Roy. Special functions. Encyclopedia of Mathematics and its Applications, 71. Cambridge University Press (1999).
- [3] D. Applebaum. Probability on compact Lie groups. Probability Theory and Stochastic Modelling,

70. Springer (2014).

- [4] J. Beck. “Flat polynomials on the unit circle - note on a problem of Littlewood.” Bull. London Math. Soc. 23 (1991): 269-277.
- [5] J. Brillhart. “On the Rudin-Shapiro polynomials.” Duke Math. J. 40.2 (1973): 335-353.


- [6] J. Brillhart, J.S. Lomont, and P. Morton. “Cyclotomic properties of the Rudin-Shapiro polynomials.” J. Reine Angew. Math. 288 (1976): 37-65.
- [7] E. Bombieri and J. Bourgain. “On Kahane’s ultraﬂat polynomials.” J. Eur. Math. Soc. 11 (2009): 627-703.
- [8] C. Doche and L. Habsieger, “Moments of the Rudin-Shapiro polynomials.” J. Fourier Anal. Appl. 10 (2004).
- [9] S.B. Ekhad and D. Zeilberger, “Integrals Involving Rudin-Shapiro Polynomials and Sketch of a Proof of Saffari’s Conjecture.” Number Theory: In Honor of Krishna Alladis 60-th Birthday, G. Andrews and F. Gravan, eds., Springer, to appear. Available at http://arxiv.org/abs/1605.06679 and http://www.math.rutgers.edu/~zeilberg/mamarim/mamarimhtml/hss.html .
- [10] T. Erd´elyi, “The Mahler Measure of the Rudin-Shapiro Polynomials.” Constructive Approximation. 43 (2016) 357-369.
- [11] T. Erd´elyi, “The phase problem of ultraﬂat unimodular polynomials: the resolution of the conjecture of Saffari.” Math. Ann. 321.4 (2001): 905-924.
- [12] J. Faraut, Analysis on Lie Groups: An Introduction. Cambridge Studies in Advanced Mathematics, 110. Cambridge University Press (2008).
- [13] M. Golay, “Multislit spectrometry.” J. Opt. Soc. Amer. 39 (1949): 437-444.
- [14] J.-P. Kahane, “Sur les polynˆomes `a coefﬁcients unimodulaires.” Bull. London Math. Soc. 12

(1980): 321342.

- [15] J.-P. Kahane and R. Salem, Ensembles parfaits et s´eries trigonom´etriques. Hermann, Revised Edition (1994).
- [16] A. Karlsson and F. Ledrappier, “Noncommutative ergodic theorems.” Geometry, rigidity, and group actions. Chicago Lectures in Math., Univ. Chicago Press (2011): 396 - 418.
- [17] Y. Kawada and K. Itˆo, “On the probability distribution on a compact group.” I. Proc. Phys.-Math. Soc. Japan. 22 (1940) 977-998.
- [18] A. la Cour-Harbo, “On the Rudin-Shapiro transform.” Appl. Comput. Harmon. Anal. 24.3 (2008): 310328.
- [19] H. L. Montgomery, “Littlewood polynomials. Number Theory: In Honor of Krishna Alladis 60-th Birthday, G. Andrews and F. Gravan, eds., Springer, to appear.
- [20] H. Montgomery, in “Problem Session.” Mathematisches Forschungsinstitut Oberwolfach, Report No. 51/2013 (2013): 3029-3030.
- [21] A. M. Odlyzko, “Search for ultraﬂat polynomials with plus and minus one coefﬁcients.” Preprint. Available at http://www.dtc.umn.edu/~odlyzko/doc/ultraflat.pdf .
- [22] W. Rudin, “Some theorems on Fourier coefﬁcients,” Proc. Amer. Math. Soc. 10 (1959) 855-859.
- [23] R. Salem, and A. Zygmund, “On lacunary trigonometric series.” Proc. Nat. Acad. Sci. USA. 33

(1947) 333-338.

- [24] H. S. Shapiro, Extremal problems for polynomials. M. S. Thesis, MIT (1951).
- [25] N. Vilenkin, Special Functions and the Theory of Group Representations. Translations of Mathematical Monographs. American Mathematical Society (1968).


DEPARTMENT OF MATHEMATICS, UNIVERSITY OF MICHIGAN, 530 CHURCH ST., ANN ARBOR, MI 48109

E-mail address: rbrad@umich.edu

