---
type: source
kind: paper
title: "Multidimensional Padé approximation of binomial functions: Equalities"
authors: Michael A. Bennett, Greg Martin, Kevin O'Bryant
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2108.00549v2
source_local: ../raw/2021-bennett-multidimensional-pad-approximation-binomial.pdf
topic: general-knowledge
cites:
---

arXiv:2108.00549v2[math.NT]6Sep2021

MULTIDIMENSIONAL PADE´ APPROXIMATION OF BINOMIAL FUNCTIONS: EQUALITIES

Michael A. Bennett1 Department of Mathematics, University of British Columbia, Room 121, 1984 Mathematics Road, Vancouver, BC, Canada bennett@math.ubc.ca

Greg Martin2 Department of Mathematics, University of British Columbia, Room 121, 1984 Mathematics Road, Vancouver, BC, Canada gerg@math.ubc.ca Kevin O’Bryant3 Department of Mathematics, City University of New York, The College of Staten Island and The Graduate Center 2800 Victory Boulevard, Staten Island, NY USA kevin.obryant@csi.cuny.edu

Received: 1/9/21, Revised: 8/3/21, Accepted: 8/12/21, Published: 8/23/21

This article appears in the Ron Graham Memorial Volume of Integers: Electronic Journal of Combinatorial Number Theory. (Integers 21A (2021), Paper No. A4, 29 pages).

Abstract Let ω0,...,ωM be complex numbers. If H0,...,HM are polynomials of degree at most ρ0,...,ρM, and G(z) = Mm=0 Hm(z)(1−z)ω

has a zero at z = 0 of maximal order (for the given ωm,ρm), we say that H0,...,HM are a multidimensional Pade´ approximation of binomial functions, and call G the Pad´e remainder. We collect here with proof all of the known expressions for G and Hm, including a new one: the Taylor series of G. We also give a new criterion for systems of Pad´e approximations of binomial functions to be perfect (a speciﬁc sort of independence used in applications).

m

![image 1](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile1.png>)

- 1supported in part by a Natural Sciences and Engineering Research Council of Canada Discov-

ery Grant

- 2supported in part by a Natural Sciences and Engineering Research Council of Canada Discov-


ery Grant

3Support for this project was provided by a PSC-CUNY Award, jointly funded by The Professional Staﬀ Congress and The City University of New York.

- 1. Introduction


Fix complex functions f0,f1,...,fM (all analytic in a neighborhood of 0) and nonnegative integers ρ0,...,ρM. The set of functions

X :=

M

Hm(z)fm(z) : Hm ∈ C[z],deg(Hm) ≤ ρm

m=0

forms a ﬁnite dimensional vector space, and the subsets of functions Xs := {G ∈ X : ordz=0(G) ≥ s}

with a zero at z = 0 of order at least s are subspaces. Trivially X0 ⊇ X1 ⊇ X2 ⊇ ···. Let σ be the least integer with Xσ having dimension 0, if such σ exists. Then Xσ−1 has positive dimension, and the functions in Xσ−1 are of particular interest, and are called the Pade´ remainders of f0,...,fM.

The M = 1 case is the standard tool in numerical analysis known as Pad´e approximation [2], which generalizes Taylor Series. In particular, if f0(z) = −1 identically, and ρ1 = 0, then

X = {−H0(z) + H1 · f1(z) : H0 ∈ C[z],deg(H0) ≤ ρ0,H1 ∈ C} .

Taking H0(z)/H1 to be the ρ0-th Taylor polynomial of f1(z), we ﬁnd that the Pad´e remainders are the constant multiples of the Taylor polynomial remainder. Letting ρ1 ≥ 0 leads to rational functions H0(z)/H1(z) that approximate f1(z) at least as well as Taylor polynomials. If f1 has poles near 0, then this rational approximation is typically much sharper than the Taylor’s polynomial approximation.

When M > 1, we include the adjective “multidimensional”. This setting has not been exploited as systematically as the M = 1 case. For a few particular choices of f0,...,fM, there is enough structure that we can work out explicit formulae for the Pad´e remainders and for the system of Pad´e approximants, i.e., generating polynomials H0,...,HM. In this paper, we take the binomials fm(z) := (1 − z)ω

m

for complex numbers ω0,...,ωM, no pair of which has an integer diﬀerence. The resulting system of equations was studied by Riemann [10], Thue [13], Siegel [11], Mahler [7], Baker [1], Chudnovsky [4], Bennett [3], and many others, and the use of these Pad´e approximations for Diophantine analysis is known as the method of Thue-Siegel.

We present in this article our exposition of these classic results on multidimensional Pad´e approximation of binomial functions. We combine, and in some cases simplify, the work of Mahler and Jager [6,7]. While there are some original results here, e.g., Theorem 4((iv)) and some cases of Theorem 6, we see the main value of this work as collating the work of many people over many years with common notation, complete proofs, and specialization to the choice fm(z). The results presented

in this work are equalities, and so as a check against oﬀ-by-one errors, one can implement the various forms given and directly check the equations for randomly chosen parameters. We have done so in Mathematica; a notebook containing these calculations is on the arXiv.

The current work focuses on various expressions for the Pad´e remainders and approximants. In subsequent works, we will provide new bounds, both archimedian and non-archimedian, on the size of the approximant polynomials H0,...,HM and on the Pad´e remainder, and will exploit those bounds to give new irrationality measures for some numbers of the form (a/b)s/n.

- 2. Statement of Results


Let M be a nonnegative integer. Consider  ω := ω0,ω1,...,ωM , a vector of M +1 distinct complex numbers, no pair of which has a diﬀerence that is an integer, and ρ  := ρ0,...,ρM , a vector of M + 1 nonnegative integers (typically not distinct). We index the vectors  ω ∈ CM+1,ρ  ∈ NM+1 with 0,1,...,M; for example, the 0-th coordinate of ρ  is ρ0 and the M-th coordinate is ρM. We will only consider M,  ω, ρ  satisfying these constraints. Two fundamental parameters are

σ = σ(ρ ) :=

M

M

(ρm + 1), and ρ ! :=

ρm!.

m=0

m=0

Some notation used in Theorem 1 is both standard and uncommon; we give deﬁnitions in the next section. When we add a scalar to a vector, we mean that the scalar is added to each coordinate, such as ρ  + 1 = ρ0 + 1,ρ2 + 1,...,ρM + 1 . When we delete the m-th coordinate, reducing the length of the vector by 1, we use a “⋆m” exponent, such as

 ω⋆m = ω0,...,ωm−1,ωm+1,...,ωM . The standard basis vectors are denoted  e0, e1,..., eM. Theorem 1. Let ρ  and  ω be ﬁxed vectors as above.

- (i) (Existence) There are polynomials Hm in z of degree at most ρm, with at least one Hm not identically 0, and with


M

Hm(z)(1 − z)ω

G(z) :=

m

m=0

having a zero of order at least σ − 1 at z = 0.

- (ii) (Uniqueness) For such G(z), the function G(z) necessarily has a zero of order

exactly σ − 1 at z = 0, and furthermore the polynomials Hm(z) are uniquely determined given the additional constraint that

lim

z→0

G(z) zσ−1

![image 2](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile2.png>)

=

1 (σ − 1)!

![image 3](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile3.png>)

.

Each Hm(z) has degree exactly ρm. There is no α ∈ C with H0(α) = ··· = HM(α) = 0.

- (iii) (Domain) G(z) is analytic on C \ [1,∞).


Theorem 1 allows us to make the following deﬁnition of Pad´e approximants and remainders.

Deﬁnition 2. Let ρ  and  ω be ﬁxed vectors as above. The M +1 Pade´ approximants Polym z  ωρ  (with 0 ≤ m ≤ M) are the polynomials with degrees ρm, and with Pade´ remainder

Rem z  ωρ  :=

M

Polym z  ωρ  (1 − z)ω

m

m=0

both having a zero of order σ − 1 at z = 0, and satisfying

Rem z  ωρ  zσ−1

=

lim

![image 4](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile4.png>)

z→0

1 (σ − 1)!

.

![image 5](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile5.png>)

In Proposition 3, we draw attention to some obvious symmetries, immediate from Theorem 1, whose proofs we do not spell out. Proposition 3 (Permutation and Shift Symmetry). If π is any permutation of 0,1,...,M, then

ρ0,ρ1,...,ρM = Rem z ω ρπ(0),ωπ(1),...,ωπ(M)

Rem z  ωρ  = Rem z ω

0,ω1,...,ωM

π(0),ρπ(1),...,ρπ(M)

and Polym z  ωρ  = Polym z ω

ρ0,ρ1,...,ρM = Polyπ−1(m) z ω ρπ(0),ωπ(1),...,ωπ(M)

0,ω1,...,ωM

π(0),ρπ(1),...,ρπ(M) . For any α, we have

(1 − z)α Rem z  ωρ  = Rem z α+ρ  ω and Polym z  ωρ  = Polym z α+ρ  ω .

The purpose of the current work is to collect together various explicit formulae for the Pad´e remainder Rem z  ωρ  and the Pad´e approximants Polym z  ωρ  , in a common notation, and with complete proofs. Formulae for the Pad´e remainder are given in Theorem 4, and formulae for the Pad´e approximants are given in Theorem 5.

- Theorem 4 (Forms for the Pad´e Remainder). The following ﬁve expressions give Rem z  ωρ  .


- (i) The Pade´ remainder Rem z  ωρ  is given by the iterated integral

(1 − z)ω

0

![image 6](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile6.png>)

ρ !

z

0

t1

0

t2

0

···

tM−1

0

G(z,t1,t2,...,tM)dtM ···dt3 dt2 dt1, where

G(t0,t1,...,tM) = tρ

M

M

M

h=1

th−1 − th 1 − th

![image 7](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile7.png>)

ρh−1 M

h=1

(1 − th)ω

h−ωh−1−1 .

- (ii) The Pade´ remainder Rem z  ωρ  is given by the M-dimensional integral

zσ−1

(1 − z)ω

0

![image 8](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile8.png>)

ρ ! [0,1]M

UM−1

M

h=1

U1+ρ

h

h

![image 9](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile9.png>)

(1 − zUh)1−ωh+ωh−1

1 − uh 1 − zUh

![image 10](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile10.png>)

ρh−1

d u,

where Um = mh=1 uh.

- (iii) The Pade´ remainder Rem z  ωρ  is the contour integral (−1)σ−1

![image 11](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile11.png>)

2πi γ

(1 − z)ξ

M

k=0

1 (ξ − ωk)ρ

![image 12](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile12.png>)

k+1 dξ,

![image 13](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile13.png>)

where γ is any simple positively oriented contour enclosing all σ of the complex numbers ωm + r (0 ≤ m ≤ M,0 ≤ r ≤ ρm).

- (iv) The Maclaurin series for Rem z  ωρ  is ∞

n=0

(−1)n

M

m=0

1 ρm!

![image 14](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile14.png>)

ρm

r=0

ρm r

(−1)r(ωm + r)n M

![image 15](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile15.png>)

![image 16](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile16.png>)

k=0 k =m

(ωk − ωm − r)ρk+1

![image 17](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile17.png>)

zn n!

![image 18](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile18.png>)

,

which converges for |z| < 1.

- (v) Finally, Rem z  ωρ  is the special value of Meijer’s G-function given by


GMM+1+1,, 0M+1 1 − z

 ω + ρ  + 1  ω

.

In addition to the formulae for Rem z  ωρ  given in Theorem 4, we note that

Rem z  ωρ  =

M

Polym z  ωρ  (1 − z)ω

,

m

m=0

and so any formula for Polym z  ωρ  generates a formula for Rem z  ωρ  . Theorem 5 gives a number of useful representations of Polym z  ωρ  .

- Theorem 5 (Forms for the Pad´e Approximants). The following ﬁve expressions give Polym z  ωρ  .


- (i) Let γm be a simple positively oriented contour enclosing all ρm + 1 of the complex numbers ωm + r (0 ≤ r ≤ ρm) and none of ωk + r (0 ≤ k ≤ M,k = m,0 ≤ r ≤ ρk). Then Polym z  ωρ  is given by

(−1)σ−1 2πi γ

![image 19](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile19.png>)

m

(1 − z)ξ−ω

m

M

k=0

1 (ξ − ωk)ρ

![image 20](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile20.png>)

k+1 dξ.

![image 21](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile21.png>)

- (ii) The Pade´ approximant Polym z  ωρ  is equal to 1

![image 22](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile22.png>)

ρm!

ρm

r=0

(z − 1)r

ρm r

M

k=0 k =m

1 (ωk − ωm − r)ρk+1.

![image 23](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile23.png>)

![image 24](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile24.png>)

- (iii) For M ≥ 1, the Pade´ approximant Polym z  ωρ  is the M-fold iterated integral Qm

![image 25](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile25.png>)

ρ ! (G)

T−ω

m−1 m

M

k=0 k =m

tω

k

k (1 + tk)ρ

k

1 − (−1)M

1 − z Tm

![image 26](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile26.png>)

ρm

d t,

where (G) ···d t integrates each of t0,...,tM (except tm) counterclockwise on the unit circle from −π radians to π radians (i.e., the principal value),

Qm :=

M

k=0 k =m

1 2i sin(π(ωk − ωm))

![image 27](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile27.png>)

, and Tm :=

M

k=0 k =m

tk.

- (iv) The Pade´ approximant is a scaled generalized hypergeometric function: 1

![image 28](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile28.png>)

ρm!

M

k=0 k =m

1 (ωk − ωm)ρk+1

![image 29](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile29.png>)

![image 30](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile30.png>)

M+1FM

ωm −  ω − ρ  (1 + ωm −  ω)⋆m

; 1 − z .

- (v) Set W := W(m,k) = ωk − ωm, and deﬁne Cm,k,r by


Cm,k,r :=

ρk r

,

if m = k, by

k+1 r ρk

Cm,k,r := (−1)ρ

−1 Γ(r + 1) Γ(r + 1 − W)

Γ(r − ρk − W) Γ(r − ρk + 1)

![image 31](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile31.png>)

![image 32](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile32.png>)

if m = k and ρk < r, and by Cm,k,r := (−1)r

π sin(πW) if m = k and ρk ≥ r. Then, we have

Γ(ρk − r + 1) Γ(ρk − r + 1 + W)

Γ(r + 1) Γ(r + 1 − W)

ρk r

![image 33](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile33.png>)

![image 34](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile34.png>)

![image 35](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile35.png>)

1 ρ !

Polym z  ωρ  =

![image 36](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile36.png>)

ρm

M

(z − 1)r

Cm,k,r.

r=0

k=0

Theorem 6 precisely states that notion that the approximants for nearby ρ  are independent. This property is referred to as “perfect approximation”, and relies mostly on deg(Polym z  ωρ  ) = ρm and ordz=0(Rem z  ωρ  ) = σ − 1. Recall that our M + 1 dimensional vectors have coordinates indexed from 0 through M.

- Theorem 6 (Approximants are Perfect). Fix ρ  ∈ NM+1 and  ǫ0, ǫ1,..., ǫM ∈ ZM+1 with each ρ  + ǫk having nonnegative coordinates, and denote the j-th coordinate of  ǫi as  ǫi,j. Let S be maximum of Mi=0 ǫi,β(i) taken over all permutations β of


0,1,...,M, and let T be the minimum of Mj=0 ǫi,j taken over 0 ≤ i ≤ M. Suppose the following two conditions are satisﬁed:

- (i) There is a unique permutation α of 0,1,...,M with S = Mi=0 ǫi,α(i);
- (ii) T + M = S.


Then the (M + 1) × (M + 1) matrix whose (k,m) coordinate is the polynomial Polym z ρ +  ω ǫ

has determinant

k

Czσ(ρ )+T−1, where C does not depend on z.

The most startling aspect of Theorem 6 is that  ω plays no role in the hypotheses nor in the conclusion.

We note that (in Theorem 6) with  ǫk =  ek one has T = 1,S = M + 1, and the conditions in Theorem 6 are satisﬁed. This recovers a result stated and used by Mahler, Chudnovsky and Bennett [3,4,7]. If one takes Ik ⊆ {0,1,...,k − 1} and  ǫk =  ek + i∈I

 ei, one recovers a result of Jager [6]. Our result covers many more examples than we found in the literature, but it is not exhaustive.

k

- 3. More Notation


We denote the rising and falling factorials as

![image 37](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile37.png>)

xr := x · (x + 1)r−1 = x · (x + 1) · (x + 2)···(x + r − 1), xr := x · (x − 1)r−1 = x · (x − 1) · (x − 2)···(x − r + 1),

![image 38](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile38.png>)

![image 39](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile39.png>)

![image 40](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile40.png>)

![image 41](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile41.png>)

for positive integers r, and deﬁne x0 = x0 = 1. We use the following trivial identities without comment (provided x − r + 1  ∈ {0,−1,−2,...}):

![image 42](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile42.png>)

Γ(x + 1) Γ(x − r + 1)

xr =

, xr = (x − r + 1)r = (−1)r(−x)r,

![image 43](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile43.png>)

![image 44](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile44.png>)

![image 45](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile45.png>)

![image 46](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile46.png>)

![image 47](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile47.png>)

and typically choose to eliminate ratios of Γ functions in preference for the more computationally friendly rising and falling factorials. All of our functions will be analytic in a complex neighborhood of z = 0. We use deg(f(z)) to be the degree of f, which is ∞ if f is not a polynomial. We use ordz=0(f(z)) to denote the order of the zero of f at z = 0, and we use O(zk) to denote a function that has a zero at z = 0 of order at least k.

We shall brieﬂy encounter the generalized hypergeometric function (deﬁned for |z| < 1, q < p, and appropriate integers ai,bi)

pFq

∞

- a1, a2, ..., ap
- b1, b2, ..., bq


; z =

n=0

an1an2 ···anp bn1bn2 ···bnq

![image 48](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile48.png>)

![image 49](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile49.png>)

![image 50](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile50.png>)

zn n!

,

![image 51](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile51.png>)

![image 52](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile52.png>)

![image 53](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile53.png>)

![image 54](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile54.png>)

![image 55](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile55.png>)

and also the Meijer G-function [8]

Gm,p, qn z

- a1, a2, ..., ap
- b1, b2, ..., bq


(deﬁned for natural numbers m,n,p,q, provided m ≤ q and n ≤ p, although we only encounter it in this work with n = 0,m = p = q = M + 1), deﬁned by

m k=1 Γ(s + bk) nk=1 Γ(1 − ak − s)

- 1

![image 56](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile56.png>)

- 2πi C


z−s ds,

p k=n+1 Γ(s + ak) qk=m+1 Γ(1 − bk − s)

![image 57](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile57.png>)

where C is an inﬁnite contour that separates the poles of Γ(1 − ak − s) from those of Γ(bk + s); the particular contour required for convergence varies depending on m,n,p,q,z.

- 4. Claims and Proofs


It is at least plausible that there are polynomials H0,...,HM with degrees ρ0,...,ρM and

M

zσ−1 (σ − 1)!

Hm(z)(1 − z)ω

+ O(zσ), (1)

G(z) :=

=

m

![image 58](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile58.png>)

m=0

where O(zσ) refers to z → 0. After all, the polynomials have a total of σ coeﬃcients, and we may choose them so that G(z) has a zero at z = 0 of order σ − 1, and the ﬁrst nonzero coeﬃcient in the power series expansion of G(z) is according to our choosing. Establishing this rigorously is the point to our ﬁrst claims.

In all the Claims in this section, we assume that M is a nonnegative integer, and that 0 ≤ m ≤ M. We assume that ρ  = ρ0,...,ρM is vector of M + 1 nonnegative integers, and that  ω = ω0,...,ωM is a vector of M +1 distinct complex numbers, no two of which have a diﬀerence that is an integer. Both ρ  and  ω (and vectors derived from them) are indexed 0 through M.

- 4.1. Existence and Uniqueness The following claim is used implicitly frequently throughout this work.


- Claim 7. For any polynomials Hm(z) (not all zero), the sum

G(z) :=

M

m=0

Hm(z)(1 − z)ω

m

is not identically 0. Proof. Since no two ωi have diﬀerence that is an integer, there is a unique k with

ωk + deg(Hk) = max{ωi + deg(Hi) : Hi = 0}. Then

lim

z→−∞

G(z) Hk(z)(1 − z)ωk

![image 59](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile59.png>)

= 1 +

M

m=0 m =k

lim

z→−∞

Hm(z)(1 − z)ω

m

![image 60](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile60.png>)

Hk(z)(1 − z)ωk

= 1.

Consequently, G cannot be identically 0.

![image 61](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile61.png>)

![image 62](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile62.png>)

![image 63](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile63.png>)

![image 64](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile64.png>)

- Claim 8. There are polynomials H0(z),...,HM(z) of degrees at most ρ0,...,ρM, respectively, not all identically 0, such that


ordz=0

M

Hm(z)(1 − z)ω

m

m=0

≥ σ − 1.

Proof. Consider polynomials H0(z),...,HM(z) of degrees ρ0,...,ρM with unknown coeﬃcients, a total of σ unknowns. Recall Newton’s Binomial Theorem: for |z| < 1 and any complex ω, we have

∞

ωi i!

![image 65](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile65.png>)

(−1)i

(1 − z)ω =

zi.

![image 66](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile66.png>)

i=0

Considering the coeﬃcient of zj, for 0 ≤ j ≤ σ − 2, on both sides of the desired equality

M

ωmi i!

![image 67](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile67.png>)

zi = O(zσ−1)

(−1)i

Hm(z)

![image 68](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile68.png>)

m=0

i≥0

yields a homogeneous linear equation in the unknowns, a total of σ − 1 equations. By linear algebra, there is a choice of the σ unknowns, not all zero, which satisﬁes all of the equations. In other words, there are polynomials H0(z),...,HM(z) (not all zero) with degrees at most ρ0,...,ρM, such that

M

Hm(z)(1 − z)ω

m

m=0

has a zero of order at least σ − 1 at z = 0.

![image 69](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile69.png>)

![image 70](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile70.png>)

![image 71](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile71.png>)

![image 72](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile72.png>)

- Claim 8 establishes Theorem 1(i). The next claim is slightly stronger than the M = 0 case of Theorem 1, in that

explicit formulae are given, and is used as a base case for subsequent induction arguments.

- Claim 9. The M = 0 Pade´ approximant and remainder are given by the formulae

Poly0 z ω

0

ρ0 =

zρ

0

![image 73](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile73.png>)

ρ0!

, and Rem z ω

0

ρ0 =

zρ

0

![image 74](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile74.png>)

ρ0!

(1 − z)ω

0

.

Proof. We need to show that the only nonzero polynomials H0 with ordz=0(H0(z)(1− z)ω

0

) ≥ σ−1 and degree at most ρ0 are H0(z) = Czρ

0

. First, observe that σ = ρ0+1. As ordz=0((1−z)ω

0

) = 0, we know that ordz=0(H0(z)(1−z)ω

0

) = ordz=0(H0). That is, H0 must be a nonzero polynomial with ordz=0(H0) ≥ ρ0 and deg(H0) ≤ ρ0. The only candidates are Poly0 z ω

0

ρ0 = Czρ

0

and Rem z ω

0

ρ0 = Czρ

0

(1 − z)ω

0

. Now, observe that

C = lim

z→0

Czρ

0

(1 − z)ω

0

![image 75](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile75.png>)

zρ0

=

1 (σ − 1)!

![image 76](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile76.png>)

=

1 ρ0!

![image 77](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile77.png>)

.

Thus, Theorem 1(ii) is proved in the M = 0 case, and the values of Polym z  ωρ  and Rem z  ωρ  are as claimed here.

![image 78](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile78.png>)

![image 79](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile79.png>)

![image 80](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile80.png>)

![image 81](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile81.png>)

- Claim 10. If deg(Hm(z)) ≤ ρm, and some Hm = 0, then


ordz=0

M

Hm(z)(1 − z)ω

m

m=0

≤ σ − 1.

Proof. Suppose M = 0. With H0 a nonzero polynomial with degree at most ρ0, we have

ordz=0 (H0(z)(1 − z)ω

) = ordz=0 (H0(z)) ≤ deg(H0) ≤ ρ0 = σ − 1. So, the claim holds for M = 0.

0

Assume the claim is false, and let M be the smallest positive integer for which this claim does not hold, and let ρ0 correspond to the ﬁrst counterexample: that is,

for any  ω,ρ  that has a smaller M, or the same M but smaller ρ0, the claim holds. Let

M

Hm(z)(1 − z)ω

G(z) :=

m

m=0

be a counterexample, i.e., ordz=0(G) ≥ σ. As multiplying by (1 − z)−ω

does not change ordz=0(G(z)), we may assume that ω0 = 0.

0

If ρ0 = 0, so that H0(z) is a constant, we have

M

d dz

dzHm(z)(1 − z)ω

d

G(z) = dzd H0(z) +

m

![image 82](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile82.png>)

![image 83](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile83.png>)

![image 84](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile84.png>)

m=1

M

(Hm′ (z)(1 − z) − Hm(z)ωm)(1 − z)ω

m−1.

=

m=1

Note that deg(Hm′ (z)(1 − z) − Hm(z)ωm) ≤ deg(Hm) ≤ ρm, for 1 ≤ m ≤ M. Thus

d

dzG(z) has a smaller M and the same ρm. By assumption on G(z), ordz=0(dzd G(z)) ≥ σ − 1, but by our assumption of the minimality of G(z), we know that ordz=0 dz d G(z) ≤ σ − 2. This contradiction shows that ρ0 = 0. But even in the case that ρ0 > 0,

![image 85](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile85.png>)

![image 86](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile86.png>)

![image 87](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile87.png>)

d dz

G(z) = H0′(z) +

![image 88](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile88.png>)

M

= H0′(z) +

M

dzHm(z)(1 − z)ω

d

m

![image 89](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile89.png>)

m=1

(Hm′ (z)(1 − z) − Hm(z)ωm)(1 − z)ω

m−1.

m=0

As above, our assumption on the minimality of ρ0, as deg(H0′) = deg(H0) − 1, implies a contradiction.

![image 90](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile90.png>)

![image 91](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile91.png>)

![image 92](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile92.png>)

![image 93](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile93.png>)

The proof of the next claim establishes the rest of Theorem 1(ii), and justiﬁes Deﬁnition 2.

- Claim 11. Suppose that Hm (with 0 ≤ m ≤ M) are polynomials with degree at


most ρm, and that G(z) := Mm=0 Hm(z)(1−z)ω

has a zero of order at least σ −1 at z = 0. Then G(z) has an order of exactly σ − 1 at z = 0. Suppose further that

m

G(z) zσ−1

=

lim

![image 94](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile94.png>)

z→0

1 (σ − 1)!

.

![image 95](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile95.png>)

Then G and Hm are uniquely determined by these constraints. The polynomial Hm(z) has degree exactly ρm, and there is no α ∈ C with H0(α) = ··· = Hm(α) = 0.

Proof. By Claims 8 and 10, we can take ordz=0(G(z)) to be at least σ − 1, and can never have it be larger than σ − 1, so there are polynomials Hm with

G(z) =

M

Hm(z)(1 − z)ω

m

m=0

= Czσ−1 + O(zσ).

By multiplying through by a constant, we can take

1 (σ − 1)!

C =

.

![image 96](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile96.png>)

If both G1(z) and G2(z) have this form, then their diﬀerence would have a zero of order greater than σ−1, and by Claim 10 this is not possible unless G1(z)−G2(z) is identically 0. By Claim 7, however, this is only possible if all of the polynomials are identically 0. That is, only if G1(z) = G2(z). Thus, G is uniquely deﬁned and the deﬁnition of Rem z  ωρ  is justiﬁed.

If

M

M

Bm(z)(1 − z)ω

Hm(z)(1 − z)ω

Rem z  ωρ  =

=

m

m

m=0

m=0

for polynomials Hm,Bm of degree at most ρm, then

M

(Hm(z) − Bm(z))(1 − z)ω

.

0 =

m

m=0

But by Claim 7, this implies that Hm(z) = Bm(z). Thus, Hm is uniquely deﬁned and the deﬁnition of Polym z  ωρ  is justiﬁed.

Suppose that Polym z  ωρ  has degree strictly less than ρm, which in particular means that ρm ≥ 1. Let  em be the M + 1-dimensional unit vector in the m-th coordinate direction. Then Rem z ρ −  ω e

is a constant multiple of Rem z  ωρ  , which has a zero of order σ(ρ ) − 1 > σ(ρ  −  em) − 1, contradicting Claim 10.

m

Finally, if Hm(α) = 0 for 0 ≤ m ≤ M, then Hm(z)/(z −α) are polynomials with degree ρm −1, and G(z)/(z −α) has a zero of order σ(ρ )−1 at z = 0, contradicting the uniqueness of G.

![image 97](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile97.png>)

![image 98](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile98.png>)

![image 99](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile99.png>)

![image 100](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile100.png>)

- 4.2. Respectful Diﬀerential Operators


- Claim 12 (Diﬀerentiation To Reduce ρ). Deﬁne the operators


dω := (1 − z)ω+1

d dz

![image 101](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile101.png>)

(1 − z)−ω.

If ρi > 0, then dω

i

reduces ρi by 1 and increases ωi by 1, i.e., if ρi > 0, then dω

Rem z  ωρ  = Rem z  ω+ e

ρ − ei .

i

i

eliminates the i-th coordinates of  ω and ρ , i.e., if ρi = 0, then dω

If ρi = 0, then dω

i

⋆i ρ ⋆i . Consequently, for any ρ0,

Rem z  ωρ  = Rem z  ω

0

ρ0+1

0+ρ0+1 d dz

0 Rem z  ωρ  = Rem z ω

1,...,ωM

(1 − z)ω

(1 − z)−ω

ρ1,...,ρM . Proof. As dω is linear and

![image 102](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile102.png>)

Rem z  ωρ  = Polyi z  ωρ  (1 − z)ω

+

i

M

Polym z  ωρ  (1 − z)ω

,

m

m=0 m =i

we can assess the impact of dω

i

on the two pieces separately. First,

Polyi z  ωρ  (1 − z)ω

dω

i

i

i+1 d dz

(1 − z)−ω

= (1 − z)ω

i

![image 103](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile103.png>)

d dz

Polyi z  ωρ  (1 − z)ω

=

![image 104](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile104.png>)

· Polyi z  ωρ  (1 − z)ω

i

i+1.

This is 0 if ρi = 0, and if ρi > 0 it has the form Pi(z)(1−z)ω

i+1 with Pi a polynomial of degree ρi − 1. The other piece is more involved (for the sake of the margins, we let H(z) := Polym z  ωρ  in the following displayed equations):

M

Polym z  ωρ  (1 − z)ω

dω

m

i

m=0 m =i

i+1 d dz

= (1 − z)ω

![image 105](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile105.png>)

(1 − z)−ω

i

M

m=0 m =i

= (1 − z)ω

i+1

M

d dz

H(z)(1 − z)ω

![image 106](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile106.png>)

m=0 m =i

H(z)(1 − z)ω

m

m−ωi

= (1 − z)ω

i+1

M

(1 − z)ω

m−ωi d

dzH(z) − H(z)(ωm − ωi)(1 − z)ω

m−ωi−1

![image 107](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile107.png>)

m=0 m =i

M

= (1 − z)ω

i+1

m=0 m =i

(1 − z)dzd H(z) − (ωm − ωi)H(z) (1 − z)ω

m−ωi−1

![image 108](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile108.png>)

M

=

m=0 m =i

(1 − z)dzd Polym z  ωρ  − (ωm − ωi)Polym z  ωρ  (1 − z)ω

.

m

![image 109](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile109.png>)

This has the form

M

Pm(z)(1 − z)ω

m

m=0 m =i

Rem z  ωρ  has the correct form to be Rem z  ω+ e

with Pm a polynomial of degree at most ρm. To wit, dω

i

⋆i

ρ − ei if ρi > 0, and the correct form to be Rem z  ω

ρ ⋆i if ρi = 0. By our earlier uniqueness result, it remains only to check that dω

i

Rem z  ωρ  has a zero (at z = 0) of order one less than Rem z  ωρ  and the correct scaling. These are both clear, as (1 − z)ω

i

have no zero at z = 0, and the dzd reduces the order of the zero by one and the scaling coeﬃcient is multiplied by σ − 1.

i+1 and (1 − z)−ω

i

![image 110](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile110.png>)

The last sentence of Claim 12 is now immediate, as the product of operators telescopes

0+ρ0 ···dω

0+1dω

dω

0

0+ρ0+1 d dz

= (1 − z)ω

![image 111](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile111.png>)

ρ0+1

(1 − z)−ω

.

0

![image 112](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile112.png>)

![image 113](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile113.png>)

![image 114](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile114.png>)

![image 115](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile115.png>)

The previous claim establishes Rem z  ωρ  as the solution of a diﬀerential equation (henceforth DE), which we make explicit next. Then, we solve the DE to express Rem z  ωρ  as an M-fold iterated integral.

- Claim 13. Let D0,...,DM be the operators


i+ρi+1 d dz

Di := (1 − z)ω

![image 116](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile116.png>)

ρi+1

(1 − z)−ω

i

With this notation, G(z) = Rem z  ωρ  is the unique analytic solution to the diﬀerential equation

zρ

M

(1 − z)ω

DM−1 ···D1D0G(z) =

M

![image 117](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile117.png>)

ρM!

with initial conditions G(σ−1)(0) = 1, G(m)(0) = 0, (0 ≤ m ≤ σ − 2).

Proof. That Rem z  ωρ  satisﬁes the DE is a consequence of Claim 12, and the initial conditions are part of the deﬁnition of Rem z  ωρ  .

As for uniqueness, suppose that G(z) = ∞i=0 gizi. Observe that the initial conditions force

1 (σ − 1)!

, gi = 0, (0 ≤ i ≤ σ − 2). The DE then forces the value of gi for i ≥ σ.

gσ−1 =

![image 118](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile118.png>)

![image 119](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile119.png>)

![image 120](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile120.png>)

![image 121](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile121.png>)

![image 122](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile122.png>)

It would be interesting to use the proof of the above claim to work out the full power series of Rem z  ωρ  .

- 4.3. Iterated Integrals


- Claim 14 is Theorem 4(i), and Claim 15 is Theorem 4(ii).


- Claim 14 (Mahler). We can represent Rem z  ωρ  as an M-fold integral as


ρ ! · Rem z  ωρ  = (1 − z)ω

0

z

t1

0

0

where

G(t0,t1,...,tM) = tρ

M

M

t2

···

0

tM−1

G(z,t1,t2,...,tM)dtM ···dt3 dt2 dt1,

0

M

h=1

th−1 − th 1 − th

![image 123](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile123.png>)

ρh−1 M

(1 − th)ω

h−ωh−1−1 .

h=1

Mahler’s Proof [7]. “This [Claim 13] can easily be brought to the following form.”

![image 124](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile124.png>)

![image 125](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile125.png>)

![image 126](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile126.png>)

![image 127](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile127.png>)

This result allows one to produce to an eﬃcient bound for Rem z  ωρ  , and is thereby a lynchpin in applications. Other authors cite Mahler, or cite authors who cite Mahler. We did not ﬁnd it easy, and hence indicate in some detail how to arrive at Mahler’s conclusion.

Proof. We begin with the diﬀerential equation given in Claim 12:

ρ0+1

0+ρ0+1 d dz

Rem z  ωρ  = Rem z ω

1,...,ωM

(1 − z)ω

(1 − z)−ω

ρ1,...,ρM . Hence,

0

![image 128](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile128.png>)

ρ0+1

d dz

0+ρ0+1) Rem z ω

1,...,ωM ρ1,...,ρM

(1 − z)−ω

0 Rem z  ωρ  = (1 − z)−(ω

![image 129](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile129.png>)

= Rem z ω

1,...,ωM −ω0−ρ0−1

ρ1,...,ρM , where the second equality follows from Proposition 3.

We observe that

z

(z − t)k k!

f(z), k = 0;

d dz

f(t)dt =

(z−t)k−1

z 0

![image 130](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile130.png>)

![image 131](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile131.png>)

(k−1)! f(t)dt, k > 0. It then follows by repetition that

0

![image 132](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile132.png>)

d dz

![image 133](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile133.png>)

ρ0+1 z

(z − t)ρ

0

f(t)dt = f(z).

![image 134](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile134.png>)

ρ0!

0

ρ0

0 Rem z  ωρ  and 0 z (z−t)

ρ0! Rem t ω

1,...,ωM −ω0−ρ0−1

Thus (1 − z)−ω

ρ1,...,ρM dt have the same (ρ0 + 1)-th derivative. Therefore, they diﬀer by a polynomial with degree at most ρ0.

![image 135](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile135.png>)

From the deﬁnition of Rem z  ωρ  , we have

ordz=0 Rem z  ωρ  = ρ0 + 1 + ordz=0 Rem t ω

1,...,ωM −ω0−ρ0−1

ρ1,...,ρM ,

which dictates that the degree-at-most-ρ0 polynomial is identically 0. We can thus undo the diﬀerential operators as

z

(z − t)ρ

0

Rem t ω

1,...,ωM −ω0−ρ0−1

(1 − z)−ω

Rem z  ωρ  =

ρ1,...,ρM dt, whence

0

![image 136](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile136.png>)

ρ0!

0

(1 − z)ω

0

Rem z  ωρ  =

![image 137](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile137.png>)

ρ0!

z

(z − t)ρ

0

0

Rem t ω

1,...,ωM −ω0−ρ0−1

ρ1,...,ρM dt. (2)

We wish to apply equation (2) inductively to express Rem z  ωρ  as an iterated integral. So that the notation will ﬁt on the page, we deﬁne for 1 ≤ i ≤ M

S0 := 0, Si := ωi−1 + ρi−1 + 1,

G0(z) := Rem z  ωρ  , Gi(z) := Rem z ω

i,ωi+1,...,ωM −Si

ρi,...,ρM . Note that GM(z) = z

ρM

ρM! (1 − z)ω

M−SM by Claim 9, while equation (2) gives

![image 138](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile138.png>)

(1 − z)ω

i−Si ρi!

Gi(z) =

![image 139](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile139.png>)

z

(z − t)ρ

Gi+1(t)dt

i

0

for 0 ≤ i < M. Now, iterating equation (2) gives

Rem t0  ωρ  = G0(t0)

(1 − t0)ω

0

=

![image 140](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile140.png>)

ρ0!

(1 − t0)ω

0

=

![image 141](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile141.png>)

ρ0!ρ1!

t0

(t0 − t1)ρ

G1(t1)dt1

0

0

t0

· (1 − t1)ω

1−S1

(t0 − t1)ρ

0

0

t1

(t1 − t2)ρ

G2(t2)dt2 dt1

1

0

. =

(1 − t0)ω

0

![image 142](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile142.png>)

ρ0!···ρM!

t0

0

t1

···

0

tM−1

G(t0,t1,...,tM)dtM ···dt2 dt1,

0

where

M−1

(th − th+1)ρ

G(t0,t1,...,tM) =

h

h=0

M

th−1 − th 1 − th

= tρ

M

![image 143](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile143.png>)

M

h=1

M−1

h−Sh tρ

M (1 − tM)ω

M−SM

(1 − th)ω

M

h=1

ρh−1 M

(1 − th)ω

h−ωh−1−1 ,

h=1

as claimed.

![image 144](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile144.png>)

![image 145](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile145.png>)

![image 146](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile146.png>)

![image 147](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile147.png>)

- Claim 15. The Pade´ remainder Rem z  ωρ  is given by the M-dimensional integral

zσ−1

(1 − z)ω

0

![image 148](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile148.png>)

ρ ! [0,1]M

UM−1

M

h=1

U1+ρ

h

h

1 − uh 1 − zUh

![image 149](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile149.png>)

ρh−1

(1 − zUh)ω

h−ωh−1−1 d u,

where Um = mh=1 uh. Proof. This follows from the previous claim upon the substitutions

th = z

- h
- i=1


ui = z Uh, dtMdtM−1 ···dt2dt1 = zM

M−1

h=1

Uhd u,

and the obvious algebraic manipulations.

![image 150](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile150.png>)

![image 151](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile151.png>)

![image 152](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile152.png>)

![image 153](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile153.png>)

4.4. Contour Integrals and Derived Expressions

- Claim 16 is Theorem 4(iii). Claim 17 is Theorem 5(i). Claim 18 is Theorem 5(ii). Claim 19 is Theorem 5(v). Claim 20 is Theorem 5(iii).


- Claim 16. Let γ be a simple positively oriented contour enclosing all σ of the complex numbers ωm + r (0 ≤ m ≤ M,0 ≤ r ≤ ρm). Then


M

(−1)σ−1 2πi γ

(1 − z)ξ

Rem z  ωρ  =

![image 154](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile154.png>)

k=0

1 (ξ − ωk)ρ

k+1 dξ.

![image 155](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile155.png>)

![image 156](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile156.png>)

Proof. Set

M

(−1)σ−1 2πi γ

1 (ξ − ωk)ρ

(1 − z)ξ

I z  ωρ  :=

k+1 dξ, and, as in Claim 13,

![image 157](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile157.png>)

![image 158](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile158.png>)

![image 159](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile159.png>)

k=0

i+ρi+1 d dz

Di := (1 − z)ω

![image 160](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile160.png>)

ρi+1

(1 − z)−ω

.

i

We will show that

D0I z  ωρ  = I z  ω ω∗∗00 .

Substituting yields

0+ρ0+1 d dz

D0I z  ωρ  = (1 − z)ω

![image 161](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile161.png>)

ρ0+1

(1 − z)−ω

I z  ωρ 

0

0+ρ0+1 d dz

= (1 − z)ω

![image 162](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile162.png>)

ρ0+1 (−1)σ−1 2πi γ

(1 − z)ξ−ω

0

![image 163](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile163.png>)

M

1 (ξ − ωk)ρ

k+1 dξ.

![image 164](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile164.png>)

![image 165](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile165.png>)

k=0

As

ρ0+1

d dz

0−ρ0−1, diﬀerentiating under the integral eliminates the k = 0 factor in the product, giving

0+1(1 − z)ξ−ω

= (−1)ρ

0+1(ξ − ω0)ρ

(1 − z)ξ−ω

0

![image 166](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile166.png>)

![image 167](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile167.png>)

M

(−1)σ−ρ

0−2

(1 − z)ξ

D0I z  ωρ  =

![image 168](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile168.png>)

2πi γ

k=1

1 (ξ − ωk)ρ

∗0

k+1 dξ = I z  ω

ρ ∗0 .

![image 169](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile169.png>)

![image 170](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile170.png>)

We iterate, using D1,...,DM−1 successively to remove all but the ﬁnal coordinates of  ω,ρ , arriving at

(1 − z)ξ (ξ − ωM)ρ

(−1)ρ

M

DM−1 ···D1D0I z  ωρ  = I z ω

M+1 dξ. By partial fractions [5, equation (5.41) in Section 5.3]

ρM =

M

![image 171](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile171.png>)

![image 172](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile172.png>)

2πi γ

![image 173](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile173.png>)

ρM

(−1)ρ

1 ρM!

M

M+1 =

![image 174](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile174.png>)

![image 175](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile175.png>)

(ξ − ωM)ρ

![image 176](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile176.png>)

r=0

(−1)r ξ − ωM − r

![image 177](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile177.png>)

ρM r

,

and with Cauchy’s Integral Formula we conclude (−1)ρ

ρM

(−1)r ξ − ωM − r

(1 − z)ξ (ξ − ωM)ρ

(1 − z)ξ ρM!

ρM r

- 1

![image 178](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile178.png>)

- 2πi γ


M

dξ

M+1 dξ =

![image 179](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile179.png>)

![image 180](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile180.png>)

![image 181](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile181.png>)

![image 182](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile182.png>)

2πi γ

![image 183](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile183.png>)

r=0

ρM

(1 − z)ξ ξ − ωM − r

- 1

![image 184](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile184.png>)

- 2πi γ


1 ρM!

ρM r

(−1)r

=

dξ

![image 185](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile185.png>)

![image 186](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile186.png>)

r=0

ρM

1 ρM!

ρM r

(−1)r(1 − z)ω

M+r

=

![image 187](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile187.png>)

r=0

ρM

(1 − z)ω

ρM r

M

(z − 1)r

=

![image 188](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile188.png>)

ρM!

r=0

(1 − z)ω

M

zρ

.

=

M

![image 189](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile189.png>)

ρM!

Thus, I z  ωρ  satisﬁes the DE in Claim 13. We now show that it also satisﬁes the initial conditions given there, and so by Claim 13 we will have I z  ωρ  = Rem z  ωρ  .

r

As for the initial conditions, it remains to show that d

dzr I z  ωρ  z=0 = 0 for 0 ≤ r ≤ σ − 2, and for r = σ − 1 we get 1. We start with

![image 190](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile190.png>)

M

(−1)σ−1 2πi γ

dr dzr

(−1)rξr(1 − z)ξ−r

I z  ωρ  =

![image 191](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile191.png>)

![image 192](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile192.png>)

![image 193](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile193.png>)

k=0

1 (ξ − ωk)ρ

k+1 dξ

![image 194](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile194.png>)

![image 195](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile195.png>)

and evaluating this at z = 0 gives (−1)σ−r−1

ξr

![image 196](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile196.png>)

k+1 dξ. (3)

![image 197](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile197.png>)

![image 198](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile198.png>)

M k=0 (ξ − ωk)ρ

2πi γ

![image 199](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile199.png>)

We may take γ to be a circle with large radius N, where N > ωk +r for 0 ≤ k ≤ M and 0 ≤ r ≤ ρk + 1. We now appeal to an argument that has little to do with our particular integrand, and so we generalize. Let P(ξ) = (ξ − pj) be a monic polynomial of degree r, and let Q(ξ) = (ξ−qj) be a monic polynomial of degree σ with all of its roots inside |ξ| = N. Then, using the substitution ξ  → N2/u, which reverses the orientation of the contour,

- 1

![image 200](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile200.png>)

- 2πi |ξ|=N


- P(ξ)

![image 201](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile201.png>)

- Q(ξ)


N2 u2

- P(N2/u)

![image 202](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile202.png>)

- Q(N2/u)


- 1

![image 203](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile203.png>)

- 2πi |u|=N


du

dξ =

![image 204](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile204.png>)

(N2/u − pj) (N2/u − qj)

N2 2πi |u|=N

du u2

=

![image 205](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile205.png>)

![image 206](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile206.png>)

![image 207](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile207.png>)

N2 2πi |u|=N

(N2 − upj) (N2 − uqj)

uσ−r−2 du.

=

![image 208](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile208.png>)

![image 209](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile209.png>)

As all the roots of the denominator (N2 − uqj) are outside the contour, this integral is 0 provided that σ − r − 2 ≥ 0, that is, provided r ≤ σ − 2. If r = σ − 1, then

- 1

![image 210](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile210.png>)

- 2πi |ξ|=N


- P(ξ)

![image 211](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile211.png>)

- Q(ξ)


(N2 − upj) (N2 − uqj)

N2 2πi |u|=N

uσ−r−2 du

dξ =

![image 212](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile212.png>)

![image 213](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile213.png>)

(N2 − 0 · pj) (N2 − 0 · qj)

(N2)r (N2)σ

= N2 ·

= N2 ·

= 1.

![image 214](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile214.png>)

![image 215](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile215.png>)

![image 216](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile216.png>)

![image 217](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile217.png>)

![image 218](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile218.png>)

![image 219](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile219.png>)

- Claim 17. Let γm be a simple positively oriented contour enclosing all ρm + 1 of the complex numbers ωm + r (0 ≤ r ≤ ρm) and none of ωk + r (0 ≤ k ≤ M,k = m,0 ≤ r ≤ ρm). Then


(−1)σ−1 2πi γ

Polym z  ωρ  =

![image 220](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile220.png>)

m

(1 − z)ξ−ω

m

M

1 (ξ − ωk)ρ

k+1 dξ.

![image 221](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile221.png>)

![image 222](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile222.png>)

k=0

Proof. As no pair of the ωi has a diﬀerence that is an integer, the σ numbers ωm+r, where 0 ≤ m ≤ M,0 ≤ r ≤ ρm, are distinct. Set

M

Φr,m(ξ) := (ξ − ωm − r)

k=0

1 (ξ − ωk)ρ

k+1 ,

![image 223](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile223.png>)

![image 224](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile224.png>)

where we understand the removable singularity to be removed. Observe that each Φr,m has σ − 1 simple poles. We will evaluate Rem z  ωρ  using Cauchy’s Integral Formula. Let γr,m be a simple closed contour enclosing ωm + r, but none of the roots of Φr,m. From Claim 16, we ﬁnd that

M

(−1)σ−1 2πi γ

1 (ξ − ωk)ρ

(1 − z)ξ

Rem z  ωρ  =

k+1 dξ

![image 225](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile225.png>)

![image 226](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile226.png>)

![image 227](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile227.png>)

k=0

ρm

M

(1 − z)ξΦr,m(ξ) ξ − ωm − r

1 2πi γ

= (−1)σ−1

dξ

![image 228](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile228.png>)

![image 229](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile229.png>)

r=0

m=0

r,m

ρm

M

= (−1)σ−1

(1 − z)ω

m+rΦr,m(ωm + r)

r=0

m=0

ρm

M

(−1)σ−1

(1 − z)r Φr,m(ωm + r) (1 − z)ω

.

=

m

r=0

m=0

We now notice that

Polym z  ωρ  = (−1)σ−1

ρm

(1 − z)rΦr,m(ωm + r), (4)

r=0

as this is a polynomial of the required degree. Also,

(−1)σ−1 2πi γ

![image 230](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile230.png>)

m

M

1 (ξ − ωk)ρ

(1 − z)ξ−ω

k+1 dξ

m

![image 231](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile231.png>)

![image 232](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile232.png>)

k=0

ρm

(1 − z)ξ−ω

- 1

![image 233](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile233.png>)

- 2πi γ


Φr,m(ξ) ξ − ωm − r

m

= (−1)σ−1

dξ

![image 234](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile234.png>)

r=0

m,r

ρm

= (−1)σ−1

(1 − z)(ω

m+r)−ωmΦr,m(ωm + r)

r=0

ρm

= (−1)σ−1

(1 − z)rΦr,m(ωm + r)

r=0

= Polym z  ωρ  .

![image 235](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile235.png>)

![image 236](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile236.png>)

![image 237](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile237.png>)

![image 238](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile238.png>)

- Claim 18. Polym z  ωρ  =

1 ρm!

![image 239](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile239.png>)

ρm

r=0

(z − 1)r

ρm r

M

k=0 k =m

1 (ωk − ωm − r)ρk+1.

![image 240](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile240.png>)

![image 241](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile241.png>)

Proof. We continue with the notation of the proof of Claim 17. In particular, we simplify the expression (4). Observe that

Φr,m(ξ) =

  

M

k=0 k =m

1 (ξ − ωk)ρ

![image 242](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile242.png>)

k+1

![image 243](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile243.png>)

   ·

  

ρm

r′=0 r′ =r

1 ξ − ωm − r′

![image 244](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile244.png>)

  

so that

Φr,m(ωm + r) =

  

M

k=0 k =m

1 (ωm − ωk + r)ρ

![image 245](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile245.png>)

k+1

![image 246](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile246.png>)

   ·

  

ρm

r′=0 r′ =r

1 r − r′

![image 247](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile247.png>)

  .

Now,

ρm

r′=0 r′ =r

(r − r′) = (r)(r − 1)···(2)(1)(−1)(−2)···(r − ρm) = (−1)r−ρ

m

r!(ρm − r)!,

so that

1

![image 248](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile248.png>)

ρm

r′=0 r′ =r

(r − r′)

=

(−1)r−ρ

m

![image 249](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile249.png>)

ρm!

ρm r

.

Also,

M

k=0 k =m

(ωm − ωk + r)ρ

k+1 =

![image 250](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile250.png>)

M

k=0 k =m

(−1)ρ

k+1(ωk − ωm − r)ρ

![image 251](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile251.png>)

k+1

= (−1)σ−ρ

m−1

M

k=0 k =m

(ωk − ωm − r)ρ

![image 252](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile252.png>)

k+1.

We now have Polym z  ωρ  as claimed.

![image 253](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile253.png>)

![image 254](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile254.png>)

![image 255](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile255.png>)

![image 256](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile256.png>)

- Claim 19. Set W := W(m,k) = ωk − ωm, and deﬁne Cm,k,r by


Cm,k,r :=

ρk r

,

if m = k, by

k+1 r ρk

Cm,k,r := (−1)ρ

−1 Γ(r + 1) Γ(r + 1 − W)

Γ(r − ρk − W) Γ(r − ρk + 1)

![image 257](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile257.png>)

![image 258](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile258.png>)

if m = k and ρk < r, and by Cm,k,r := (−1)r

Γ(r + 1) Γ(r + 1 − W)

ρk r

π sin(πW) if m = k and ρk ≥ r. Then, we have

Γ(ρk − r + 1) Γ(ρk − r + 1 + W)

![image 259](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile259.png>)

![image 260](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile260.png>)

![image 261](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile261.png>)

1 ρ !

Polym z  ωρ  =

![image 262](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile262.png>)

ρm

M

(z − 1)r

Cm,k,r.

r=0

k=0

Proof. We begin from Claim 18, writing W in place of ωk − ωm:

1 ρm!

Polym z  ωρ  =

![image 263](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile263.png>)

1 ρ !

=

![image 264](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile264.png>)

ρm

(z − 1)r

r=0

ρm r

ρm

(z − 1)r

r=0

ρm r

M

1 (W − r)ρk+1

![image 265](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile265.png>)

![image 266](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile266.png>)

k=0 k =m

M

ρk! (W − r)ρk+1.

![image 267](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile267.png>)

![image 268](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile268.png>)

k=0 k =m

If k = m and ρk < r, then

−1 Γ(r + 1)

−1 r! (r − ρk)!

r ρk

r ρk

=

ρk! =

![image 269](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile269.png>)

![image 270](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile270.png>)

Γ(r − ρk + 1) and

k+1 Γ(r − W + 1) Γ(r − W − ρk)

![image 271](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile271.png>)

(W − r)ρ

k+1 = (−1)ρ

k+1 = (−1)ρ

k+1(r − W)ρ

. Combining these,

![image 272](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile272.png>)

![image 273](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile273.png>)

ρk! (W − r)ρk+1 = (−1)ρ

k+1 r ρk

![image 274](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile274.png>)

![image 275](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile275.png>)

k+1 r ρk

= (−1)ρ

= Cm,k,r. If k = m and ρk ≥ r, then

−1 Γ(r + 1) Γ(r − ρk + 1)

Γ(r − W − ρk) Γ(r − W + 1)

![image 276](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile276.png>)

![image 277](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile277.png>)

−1 Γ(r + 1) Γ(r + 1 − W)

Γ(r − ρk − W) Γ(r − ρk + 1)

![image 278](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile278.png>)

![image 279](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile279.png>)

ρk r

ρk r

Γ(r + 1)Γ(ρk − r + 1) and

r!(ρk − r)! =

ρk! =

![image 280](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile280.png>)

![image 281](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile281.png>)

(W − r)ρ

k+1 = (W − r)r · Wρ

k+1−r

![image 282](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile282.png>)

= (−1)r(r − W)r · (W + ρk − r)ρ

k−r+1

![image 283](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile283.png>)

![image 284](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile284.png>)

Γ(ρk − r + W + 1) Γ(ρk − r + W − (ρk − r + 1) + 1)

Γ(r − W + 1) Γ(r − W − r + 1)

= (−1)r

·

![image 285](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile285.png>)

![image 286](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile286.png>)

Γ(r + 1 − W)Γ(ρk − r + 1 + W) Γ(1 − W)Γ(W)

= (−1)r

.

![image 287](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile287.png>)

By Euler’s reﬂection formula for the Gamma fucntion, Γ(1−W)Γ(W) = π/ sin(πW). Combining these,

ρk! (W − r)ρk+1 = (−1)r

Γ(r + 1) Γ(r + 1 − W)

Γ(ρk − r + 1) Γ(ρk − r + 1 + W)

π sin(πW)

![image 288](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile288.png>)

![image 289](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile289.png>)

![image 290](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile290.png>)

![image 291](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile291.png>)

![image 292](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile292.png>)

= Cm,k,r. This concludes the proof.

ρk r

![image 293](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile293.png>)

![image 294](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile294.png>)

![image 295](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile295.png>)

![image 296](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile296.png>)

- Claim 20. For M ≥ 1, we can represent Polym z  ωρ  as an M-fold iterated (principal value) contour integral as


Qm ρ ! (G)

T−ω

m−1 m

Polym z  ωρ  =

![image 297](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile297.png>)

M

tω

k (1 + tk)ρ

k

k

k=0 k =m

where

M

1 2i sin(π(ωk − ωm))

Qm :=

![image 298](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile298.png>)

k=0 k =m

M

Tm :=

tk

k=0 k =m

1 − z Tm

1 − (−1)M

![image 299](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile299.png>)

ρm

d t,

:=

·

···

|tM|=1 d t := dtM ···dtm+1 dtm−1 ···t1.

|tm−1|=1 |tm+1|=1

|t0|=1

(G)

Proof. By induction and integration-by-parts, we notice that

P.V.

tx−1(1 + t)ρ dt =

|t|=1

π

2i sin(πx)ρ! xρ+1

ei(x−1)t(1 + eit)ρ ieitdt =

, (5)

![image 300](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile300.png>)

![image 301](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile301.png>)

−π

provided that ρ is a nonnegative integer and x ∈ C \ {0,−1,−2,...}. In this claim and its proof, all integrals are understood to be principal values.

Beginning with Claim 18, we may write Polym z  ωρ  as Polym z  ωρ 

ρm

M

1 (ωk − ωm − r)ρk+1

ρm r

1 ρm!

(z − 1)r

=

![image 302](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile302.png>)

![image 303](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile303.png>)

![image 304](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile304.png>)

r=0

k=0 k =m

ρm

M

1 ρ !

2i sin(π(ωk − ωm − r))ρk! (ωk − ωm − r)ρk+1 .

ρm r

1 2i sin(π(ωk − ωm − r))

(z − 1)r

=

![image 305](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile305.png>)

![image 306](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile306.png>)

![image 307](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile307.png>)

![image 308](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile308.png>)

r=0

k=0 k =m

We now use equation (5) to continue Polym z  ωρ 

ρm

M

1 ρ !

ρm r

(−1)rQm

(z − 1)r

=

![image 309](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile309.png>)

r=0

k=0 k =m

ρm

M

ρm r

Qm ρ !

(−1)rM(z − 1)r

=

![image 310](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile310.png>)

r=0

k=0 k =m

|tk|=1

tω

k−ωm−r−1

k (1 + tk)ρ

k

dtk

|tk|=1

tω

k−ωm−r−1

k (1 + tk)ρ

k

dtk

Compressing the product of integrals using the (G) notation, we continue with Polym z  ωρ 

ρm

M

ρm r

Qm ρ ! (G)

tω

k−ωm−r−1

k (1 + tk)ρ

(−1)rM(z − 1)r

d t

=

k

![image 311](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile311.png>)

r=0

k=0 k =m

ρm

M

Qm ρ ! (G)

ρm r

tω

k (1 + tk)ρ

Tm−r T−ω

m−1 m

(−1)rM(z − 1)r

=

d t

k

k

![image 312](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile312.png>)

r=0

k=0 k =m

ρm

M

r

z − 1 Tm

ρm r

Qm ρ ! (G)

tω

(−1)M

k (1 + tk)ρ

T−ω

m−1 m

d t

=

k

k

![image 313](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile313.png>)

![image 314](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile314.png>)

r=0

k=0 k =m

Qm ρ ! (G)

T−ω

m−1 m

=

![image 315](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile315.png>)

M

tω

k (1 + tk)ρ

k

k

k=0 k =m

1 − z Tm

1 − (−1)M

![image 316](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile316.png>)

ρm

d t,

- as asserted in the Claim.


![image 317](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile317.png>)

![image 318](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile318.png>)

![image 319](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile319.png>)

![image 320](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile320.png>)

- 4.5. Hypergeometric Functions


- Claim 21 below is Theorem 4(v), and Claim 23 is Theorem 5(iv). The Meijer G-function [8] is deﬁned for natural numbers m,n,p,q, provided m ≤


q and n ≤ p, although we only encounter it here with n = 0,m = p = q = M + 1. It is denoted

- a1, a2, ..., ap
- b1, b2, ..., bq


Gm,p, qn z and deﬁned as

m k=1 Γ(s + bk) nk=1 Γ(1 − ak − s)

- 1

![image 321](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile321.png>)

- 2πi C


z−s ds,

p k=n+1 Γ(s + ak) qk=m+1 Γ(1 − bk − s)

![image 322](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile322.png>)

where C is a particular inﬁnite contour that separates the poles of Γ(1−ak−s) from those of Γ(bk +s); the particular contour required for convergence varies depending on m,n,p,q,z.

Claim 21. Rem z  ωρ  , when |z| < 1 and |1 − z| < 1, is a special value of Meijer’s G-function

 ω + ρ  + 1  ω

Rem z  ωρ  = GMM+1+1,, 0M+1 1 − z

.

Sketch of Proof. With m = p = q = M + 1,n = 0, we see that

q

n

Γ(1 − ak − s) =

Γ(1 − bk − s) = 1.

k=1

k=m+1

Further, with ak+1 = ωk + ρk + 1,bk+1 = ωk,

M

M

m k=1 Γ(s + bk)

Γ(s + ωk) Γ(s + ωk + ρk + 1)

1 (s + ωk)ρk+1 . We now have

=

=

p k=n+1 Γ(s + ak)

![image 323](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile323.png>)

![image 324](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile324.png>)

![image 325](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile325.png>)

![image 326](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile326.png>)

k=0

k=0

GMM+1+1,, 0M+1 1 − z

 ω + ρ  + 1  ω

M

- 1

![image 327](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile327.png>)

- 2πi C


1 (s + ωk)ρk+1 ds

(1 − z)−s

=

![image 328](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile328.png>)

![image 329](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile329.png>)

k=0

M

k+1 (ξ − ωk)ρ

(−1)ρ

1 2πi C

(1 − z)ξ

k+1 (−dξ)

=

![image 330](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile330.png>)

![image 331](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile331.png>)

![image 332](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile332.png>)

k=0

M

(−1)σ−1 2πi C

1 (ξ − ωk)ρ

(1 − z)ξ

=

k+1 dξ

![image 333](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile333.png>)

![image 334](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile334.png>)

![image 335](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile335.png>)

k=0

= Rem z  ωρ  .

Admittedly, we have played fast-and-loose with the contour, and therefore the conditions |z| < 1 and |1 − z| < 1 are not explained.

![image 336](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile336.png>)

![image 337](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile337.png>)

![image 338](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile338.png>)

![image 339](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile339.png>)

Theorem 22 (Slater’s Theorem [12]). Provided that aj −bh is not a positive integer (with j ≤ n,h ≤ m), and bj − bk is not an integer (with 1 ≤ j < k ≤ q), and 0 < |z| < 1,

- a1, a2, ..., ap
- b1, b2, ..., bq


Gm,p, qn z

=

m

Γ(bk − bh) nk=1 Γ(1 + bh − ak)

m

k=1 k =h

Fq−1

q k=m+1 Γ(1 + bh − bk) pk=n+1 Γ(ak − bh) p

![image 340](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile340.png>)

h=1

 a b

; (−1)m+n−pz zb

,

h

where a h = 1 + bh − a1,...,1 + bh − ap and bh = 1 + bh − b1,...,1 + bh − bq (with the 1 + bh − bh term omitted).

- Claim 23. The Pade´ approximant Polym z  ωρ  is associated with a generalized hypergeometric function by

Polym z  ωρ  =

1 ρm!

![image 341](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile341.png>)

M

k=0 k =m

1 (ωk − ωm)ρk+1

![image 342](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile342.png>)

![image 343](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile343.png>)

M+1FM

ωm −  ω − ρ  (1 + ωm −  ω)⋆m

; 1 − z .

Proof. Using Claim 21 and Theorem 22, we may write Rem z  ωρ  as

M

m=0

M

k=0 k =m

Γ(ωk − ωm)

![image 344](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile344.png>)

M k=0 Γ(ωk + ρk + 1 − ωm) M+1

FM

1 + ωm −  ω − ρ  − 1 (1 + ωm −  ω)⋆m

; 1 − z (1 − z)ω

m

,

which we manipulate into the form

M

m=0

1 ρm!

![image 345](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile345.png>)

M

k=0 k =m

1 (ωk − ωm)ρk+1

![image 346](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile346.png>)

![image 347](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile347.png>)

M+1FM

ωm −  ω − ρ  (1 + ωm −  ω)⋆m

; 1 − z (1 − z)ω

m

.

One coordinate of ωm −  ω − ρ  is −ρm, a nonpositive integer. Consequently,

1 ρm!

![image 348](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile348.png>)

M

k=0 k =m

1 (ωk − ωm)ρk+1

![image 349](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile349.png>)

![image 350](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile350.png>)

M+1FM

ωm −  ω − ρ  (1 + ωm −  ω)⋆m

; 1 − z

is a polynomial with degree at most ρm. Therefore, it must be Polym z  ωρ  . 4.6. Power Series

![image 351](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile351.png>)

![image 352](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile352.png>)

![image 353](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile353.png>)

![image 354](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile354.png>)

- Claim 24 is Theorem 4(iv).


- Claim 24. Let gn be the coeﬃcients in the power series expansion of Rem z  ωρ 


∞

zn n!

- at z = 0, i.e., Rem z  ωρ  =


. Then for n ≥ 0 we have

gn

![image 355](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile355.png>)

n=0

ρm

M

1 ρm!

gn = (−1)n

![image 356](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile356.png>)

m=0

r=0

ρm r

(−1)r(ωm + r)n M

![image 357](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile357.png>)

.

![image 358](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile358.png>)

![image 359](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile359.png>)

(ωk − ωm − r)ρk+1

k=0 k =m

In particular, gn = 0 for 0 ≤ n ≤ σ − 2 and gσ−1 = 1.

Proof. We begin with the contour integral representation of Rem z  ωρ  given in Claim 16, replace (1 − z)ξ with its power series, and then integrate term by term,

obtaining

M

(−1)σ−1 2πi γ

1 (ξ − ωk)ρ

(1 − z)ξ

Rem z  ωρ  =

k+1 dξ

![image 360](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile360.png>)

![image 361](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile361.png>)

![image 362](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile362.png>)

k=0

∞

M

(−1)σ−1 2πi γ

zn n!

1 (ξ − ωk)ρ

(−1)nξn

=

k+1 dξ

![image 363](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile363.png>)

![image 364](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile364.png>)

![image 365](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile365.png>)

![image 366](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile366.png>)

![image 367](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile367.png>)

n=0

k=0

∞

(−1)σ−1ξn

zn n!

- 1

![image 368](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile368.png>)

- 2πi γ


![image 369](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile369.png>)

(−1)n

.

=

k+1 dξ

![image 370](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile370.png>)

![image 371](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile371.png>)

M k=0(ξ − ωk)ρ

n=0

![image 372](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile372.png>)

Continuing as in the proof of Claims 17 and 18, we see that

gn = (−1)n

M

= (−1)n

m=0

M

= (−1)n

m=0

M

= (−1)n

m=0

M

= (−1)n

m=0

(−1)σ−1ξn

- 1

![image 373](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile373.png>)

- 2πi γ


![image 374](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile374.png>)

k+1 dξ (6)

![image 375](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile375.png>)

M k=0(ξ − ωk)ρ

![image 376](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile376.png>)

ρm

(−1)σ−1(ωm + r)nΦr,m(ωm + r)

![image 377](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile377.png>)

r=0

ρm

M

(−1)r−ρ

1 (ωm + r − ωk)ρk+1

ρm r

m

(−1)σ−1(ωm + r)n

![image 378](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile378.png>)

![image 379](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile379.png>)

![image 380](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile380.png>)

![image 381](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile381.png>)

ρm!

r=0

k=0 k =m

ρm

M

(−1)r−ρ

(−1)ρ

k+1

ρm r

m

(−1)σ−1(ωm + r)n

![image 382](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile382.png>)

![image 383](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile383.png>)

![image 384](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile384.png>)

![image 385](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile385.png>)

ρm!

(ωk − ωm − r)ρk+1

r=0

k=0 k =m

ρm

(−1)r(ωm + r)n M

ρm r

1 ρm!

![image 386](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile386.png>)

.

![image 387](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile387.png>)

![image 388](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile388.png>)

![image 389](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile389.png>)

(ωk − ωm − r)ρk+1

k=0 k =m

r=0

That gn = 0 for 0 ≤ n ≤ σ−2 and gσ−1 = 1 follow from the deﬁnition of Rem z  ωρ  . Alternatively, the expression on line (6) is shown directly to have these values in the proof of Claim 16, beginning with equation (3).

![image 390](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile390.png>)

![image 391](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile391.png>)

![image 392](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile392.png>)

![image 393](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile393.png>)

- 4.7. Perfection


We remind our reader that our vectors are indexed from 0, so that the j-th coordinate of ρ0,...,ρM is ρj. The coordinates of the (M + 1) × (M + 1) matrix H in the next claim is indexed in the same manner.

Claim 25 is Theorem 6.

- Claim 25. Fix ρ  ∈ NM+1 and  ǫ0, ǫ1,..., ǫM ∈ ZM+1 with each ρ  +  ǫk having nonnegative coordinates, and denote the j-th coordinate of  ǫi as  ǫi,j. Let S be maximum of Mi=0 ǫi,β(i) taken over all permutations β of 0,1,...,M, and let T


be the minimum of Mj=0 ǫi,j taken over 0 ≤ i ≤ M. Suppose the following two conditions are satisﬁed:

- 1. There is a unique permutation α of 0,1,...,M with S = Mi=0 ǫi,α(i);
- 2. T + M = S.


Then the (M + 1) × (M + 1) matrix H, whose (k,m) coordinate is the polynomial Polym z ρ +  ω ǫ

, has determinant

k

Czσ(ρ )+T−1, where C is nonzero and does not depend on z. Proof. The determinant of H, by the familiar permutation expansion, is

(−1)sgn(β)

det(H) =

β∈Σ[0,M]

M

Polyβ(k) z ρ +  ω ǫ

k

k=0

,

which is clearly a polynomial. Notice that

deg

M

Polyβ(k) z ρ +  ω ǫ

k

k=0

M

deg Polyβ(k) z ρ +  ω ǫ

=

k

k=0

M

=

(ρβ(k) + ǫk,β(k)) ≤ σ(ρ ) − (M + 1) + S,

k=0

with equality achieved for (and only for) β = α. Consequently,

deg(det(H)) = σ(ρ ) − M − 1 + S = σ(ρ ) + T − 1, and in particular det(H) is not identically 0.

M T. By deﬁnition H v is a column of M + 1 functions of z: in row k it is Rem z ρ +  ω ǫ

,...,(1 − z)ω

,(1 − z)ω

Let  v be the column vector (1 − z)ω

1

0

, which has a

k

zero of order σ(ρ  + ǫk) − 1 = σ(ρ ) + Mj=0 ǫk,j − 1 ≥ σ(ρ ) + T − 1. Now multiply H v by the adjoint of H, which is also a matrix of polynomials. We have

det(H) v = adj(H)H v

Rem z ρ +  ω ǫ





- 0

Rem z ρ +  ω ǫ

- 1


= adj(H)

 

 

. Rem z ρ +  ω e

M

∞

= adj(H) zσ(ρ )+T−1

 vnzn

n=0

∞

= zσ(ρ )+T−1

(adj(H) vn)zn

n=0

for some column vectors  v0 = 0, v1,.... That  v0 = 0 follows from the deﬁnition of T. Each coordinate of det(H) v has the form det(H)(1−z)ω, and so has a zero at z = 0 of order at most deg(det(H)) = σ(ρ )−M −1+S. By the above displayed equations, each coordinate of det(H) v has a zero at z = 0 of order at least σ(ρ ) + T − 1 with equality for some coordinate. But T + M = S, by hypothesis, so that det(H) is a polynomial whose degree coincides with the order of its zero at z = 0. Therefore

det(H) = Czσ(ρ )+T−1 = Czσ(ρ )+S−M−1, as claimed. The constant C is nonzero as det(H) is not identically 0.

![image 394](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile394.png>)

![image 395](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile395.png>)

![image 396](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile396.png>)

![image 397](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile397.png>)

5. Opportunities for Further Work

- 1. Is there a nice iterated integral representation of Polym z  ωρ  without contours, similar to the representation in Theorem 4(i) for Rem z  ωρ  ?
- 2. For ﬁxed  ω, which degree vectors ρ (0),ρ (1),...,ρ (M) lead to a perfect system? There seems to be some geometry involved. That is, a modest amount of computation suggests that for each M there is B such that if any coordinate

of any  ǫk −  ǫj is not between −B and B, then the resulting system is not perfect for any ρ (the determinant of H doesn’t have the form Czn).

- 3. What is the value of C in Theorem 6?
- 4. What is the nice power series expression for Polym z  ωρ  ? For M = 1, this is an important part of the best explicit irrationality measure for 21/3.


References

- [1] A. Baker, Rational approximations to √3 2 and other algebraic numbers, Quart. J. Math. Oxford Ser. (2) 15 (1964), 375–383, DOI 10.1093/qmath/15.1.375. MR171750

![image 398](<2021-bennett-multidimensional-pad-approximation-binomial_images/imageFile398.png>)

- [2] George A. Baker Jr. and Peter Graves-Morris, Pade´ approximants, 2nd ed., Encyclopedia of Mathematics and its Applications, vol. 59, Cambridge University Press, Cambridge, 1996. MR1383091 (97h:41001)
- [3] Michael A. Bennett, Rational approximation to algebraic numbers of small height: the Diophantine equation |axn − byn| = 1, J. Reine Angew. Math. 535 (2001), 1–49, DOI 10.1515/crll.2001.044. MR1837094 (2002d:11079)
- [4] G. V. Chudnovsky, On the method of Thue-Siegel, Ann. of Math. (2) 117 (1983), no. 2, 325–382, DOI 10.2307/2007080. MR690849 (85g:11058)
- [5] Ronald L. Graham, Donald E. Knuth, and Oren Patashnik, Concrete mathematics, 2nd ed., Addison-Wesley Publishing Company, Reading, MA, 1994. A foundation for computer science. MR1397498


- [6] H. Jager, A multidimensional generalization of the Pade´ table. I, II, III, IV, V, VI, Nederl. Akad. Wetensch. Proc. Ser. A 67=Indag. Math. 26 (1964), 193–249. MR0163099 (29 #402), MR0165287 (29 #2576)
- [7] Kurt Mahler, Ein Beweis des Thue-Siegelschen Satzes u¨ber die Approximation algebraischer Zahlen fu¨r binomische Gleichungen, Math. Ann. 105 (1931), no. 1, 267–276, DOI 10.1007/BF01455819 (German). English translation by Karl Levy at https://arxiv.org/abs/1507.01447. MR1512715
- [8] NIST Digital Library of Mathematical Functions, http://dlmf.nist.gov/. Accessed April 25, Release 1.0.8 of 2014. Online companion to [9].
- [9] F. W. J. Olver, D. W. Lozier, R. F. Boisvert, and C. W. Clark (eds.), NIST Handbook of Mathematical Functions, Cambridge University Press, New York, NY, 2010. Print companion to [8].
- [10] B. Riemann, Oeuvres Mathimatiques, Albert Blanchard, Paris, 1968.
- [11] C. L. Siegel, Approximation algebraische zahlen, Mat. Zeit. 10 (1921), 127–213.
- [12] Lucy Joan Slater, Generalized hypergeometric functions, Cambridge University Press, Cambridge, 1966. MR0201688
- [13] A. Thue, Bemerkung u¨ber gewisse N¨ahrungsbru¨che algebraischer Zahlen, Skrifter udigvne af Videnskabsselskabet i Christiania (1908).


