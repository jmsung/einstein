---
type: source
kind: paper
title: Exponential polynomials and identification of polygonal regions from Fourier samples
authors: Mihail N. Kolountzakis, Emmanuil Spyridakis
year: 2024
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2409.01432v2
source_local: ../raw/2024-kolountzakis-exponential-polynomials-identification-pol.pdf
topic: general-knowledge
cites:
---

## EXPONENTIAL POLYNOMIALS AND IDENTIFICATION OF POLYGONAL REGIONS FROM FOURIER SAMPLES

MIHAIL N. KOLOUNTZAKIS AND EMMANUIL SPYRIDAKIS

# arXiv:2409.01432v2[math.CA]14Oct2025

Abstract. Consider the set E(D,N) of all bivariate exponential polynomials

n

pj(ξ,η)e2πi(x

jξ+yjη),

f(ξ,η) =

j=1

where the polynomials pj ∈ C[ξ,η] have degree < D, n ≤ N and where xj, yj ∈ T = R/Z. We find a set A ⊆ Z2 that depends on N and D only and is of size O(D2N logN) such that the values of f on A determine f. Notice that the size of A is only larger by a logarithmic quantity than the number of parameters needed to write down f. We emphasize that, unlike most existing work on this problem, this is a nonadaptive sampling method: the sampling points are fixed a priori and depend on the maximum degree D and maximum number of terms N only.

We use this in order to prove some uniqueness results about polygonal regions given a small set of samples of the Fourier Transform of their indicator function. If the number of different slopes of the edges of the polygonal region is ≤ k then the region is determined from a predetermined set of Fourier samples that depends only on k and the maximum number of vertices N and is of size O(k2N logN). In the particular case where all edges are known to be parallel to the axes the polygonal region is determined from a set of O(N logN) Fourier samples that depends on N only.

Our methods are non-constructive.

Contents

- 1. Introduction 2

- 2. Indentifying exponential polynomials 4

- 3. Application to identification of polygons 11 3.1. Unknown slopes 14 References 16


Date: October 15, 2025. 2020 Mathematics Subject Classification. 41A05, 41A27, 42A15, 42A16. Key words and phrases. Interpolation, sparse exponential sums, non-harmonic exponential

sums, exponential polynomials, polygon reconstruction, Fourier coefficients, inverse problem.

1

1. Introduction

We deal with the general problem of identifying an object (a region in Eudlidean space, a measure or a function of a certain type) from samples of its Fourier Trasform or samples of the function itself. If the object comes from a parametric family where each object is defined by N real or complex parameters then it is a reasonable expectation that the number of samples used to identify the object should not be much larger than N.

Suppose for instance, to mention an almost obvious but important case, that our parametric family consists of all one-variable algebraic polynomials of degree < N and complex coefficients

f(x) = fn−1xn−1 + ··· + f1x + f0, with fj ∈ C,n ≤ N.

Then, if f is such a polynomial, the set of samples of f on the set {0,1,...,N − 1}, which consists of N points, is enough to determine f: any two such polynomials agreeing on that set must be the same polynomial as the difference of these polynomials can have at most N − 1 roots unless it is identically 0.

Another famous case is the determination of exponential sums (trigonometric polynomials) with at most N frequencies

n

fje2πiλ

### jξ, (fj ∈ C, n ≤ N)

f(ξ) =

j=1

from samples. Let us restrict the frequencies λj to lie in the torus T = R/Z, which we can identify with [0,1) (it is after all natural to assume that all frequencies are in a bounded region), and seek to determine f(ξ) from its samples on a set A ⊆ Z. The famous Prony method from the 18th century [dP95,DKP23,VMB02] says that we can identify f from its values on the set A = {0,1,...,2N}. See also Lemma 2.1 below, with D = 1, for a slightly different viewpoint.

The case of exponential polynomials with n ≤ N terms and polynomial coefficients of degree degpj < D and frequencies λj ∈ T is also dealt with in [VMB02]:

n

pj(ξ)e2πiλ

jξ

f(ξ) =

j=1

can be identified from its samples on the set A = {0,1,...,2ND} as shown also in our Lemma 2.1.

I1 I2 In

...

0

1

Figure 1. A set E ⊆ T consisting of n arcs.

An example of a more geometric flavor [Cou10,DKP23] is the case of a set E ⊆ T which is a union of at most N arcs (intervals) as shown in Fig. 1. Such a set can be identified by sampling its Fourier Transform E on the set A = {0,1,...,N}.

The situation becomes more complicated in higher dimension. Multivariate exponential sums

n

fje2πiλ

### j·t, (n ≤ N, fj ∈ C,λj ∈ Td,t ∈ Zd)

f(t) =

j=1

were shown recently [DKP23] (see also [Sau18]) to be identifiable by O(N logN) samples, only slightly more than the number O(N) of degrees of freedom.

In this paper we study the identification, from a predetermined set of samples, of bivariate exponential polynomials

n

pj(ξ,η)e−2πi(x

j·ξ+yj·η),

f(ξ,η) =

j=1

with n ≤ N, pj being a polynomial of degree < D and (xj, yj) ∈ T2, when we know only the maximum degree D and the maximum number of terms N. We apply our results to the identification of certain polygonal regions from samples of the Fourier Transform of their indicator functions. Our work is inspired from the paper [WP16]. Our method assumes, in contrast to [WP16], that we know the possible slopes of the edges of the polygons.

Our results are as follows. In §2 (see Theorem 2.1) we show that any bivariate exponential polynomial with at most N terms and polynomial coefficients of degree < D can be identified from its samples on a predetermined set of size O(D2N logN). This sampling set depends on N and D only. In §3 we use this result in order to show, for instance, that polygonal regions with edges parallel to the two axes and at most N vertices can be identified by sampling the Fourier Transform of their indicator function at a predetermined set of size O(N logN), where, again, the sampling set depends only on N (see Corollary 3.3).

- Remark 1.1. Note than in [WP16] it is precisely the polygons whose vertices project non-uniquely onto a line that create the most problems, which happens a lot with polygons whose edges are parallel to the two axes. This coincidence of projections is reflected in the logN factor in the size of our sampling set: a small and uniform price to pay for all polygons.


We emphasize that the sampling problems we are studying are of the non-adaptive

type. In other words, given the class of functions that we want to identify, the sampling sets are specified a priori and are not allowed to change depending on what values we have already seen from f (this would be adaptive sampling, as is the approach in [WP16]).

Note on algorihmic inversion. We should also clarify that we do not provide algorithms for recovering the object (function, polygon) from its samples or Fourier samples. We only deal with the concept of inversion in principle. Whenever we claim that a function f from a certain class C can be identified from its values on a sampling set A all we mean is that the mapping

f → (f(a))a∈A

is injective on C (different functions from C give different data). We do not deal at all with the algorithmic reconstruction of f. There have been many papers (e.g. [WP16,CL18]), especially for the case of exponential sums, where a more constructive approach has been taken but our goal is to have the minimal a priori sample set for a given class of functions. Allowing one (which we do not do) to alter the sampling points as the method progresses can lead to reconstruction with fewer samples.

Notation: We write [n] = {1,2,...,n} and [n]0 = {0,1,...,n}.

2. Indentifying exponential polynomials

A multivariate polynomial is of degree d if d is the highest power that any of its variables is raised to. Thus, a two-variable polynomial p(ξ,η) is of degree ≤ d if and only if it can be written in the form

d

pk(ξ)ηk,

p(ξ,η) =

k=0

where the univariate polynomials pk(ξ) are of degree ≤ d. All the polynomials have complex coefficients.

- Remark 2.1 (Determination of an exponential polynomial by its values on the integers). An exponential polynomial


n

pj(ξ,η)e2πi(x

### jξ+yjη), (xj, yj) ∈ T2,

f(ξ,η) =

j=1

whose values are known for all ξ,η ∈ Z is completely determined. The reason is that it can be viewed as the Fourier Transform (defined on Z2) of the distribution (automatically tempered) on T2, the dual group of Z2 [Rud62],

n

- 1

- 2πi


- 1

- 2πi


- (1) S =


pj

∂1,

### ∂2 δ(x

j,yj).

j=1

Here δ(x

j,yj) denotes a unit point mass at (xj, yj) ∈ T2 and ∂j denotes differentiation with respect to the j-th variable, j = 1,2. By Fourier inversion (the Fourier Transform is a linear isomorphism from the space of tempered distributions onto itself) knowing f on Z2 (the dual group of T2) we automatically know the tempered distribution S

on T2. And it is easy to see that S determines uniquely both the points (xj, yj) and the corresponding polynomials pj.

The analogous statement is true for exponential polynomials with any number of variables.

In this section we identify an exponential polynomial, obeying some assumptions, by its values on a sampling set in Z or Z2. We shall not always attempt to give the smallest possible sampling set. For the sake of simplicity in expressions we may opt to prescribe a slightly larger sampling set. In the end what matters to us is the size of the sampling set as N (the maximum number of terms in the exponential polynomial) tends to infinity.

Let us start with univariate exponential polynomials.

- Lemma 2.1. Let f(ξ) = nj=1 pj(ξ)e2πixjξ, xj ∈ T, be a univariate exponential polynomial with n ≤ N terms. Assume also that the degree of each polynomial coefficient pj is < D.

Then the function f is determined by its values on the set A = [2ND]0.

Proof. It is well known [EvdPSW15, Ch. 1, “Generalized power sums”] that the sequence f(n), n ∈ Z, satisfies a homogeneous linear recurrence relation of order

n

j=1

(1 + degpj) ≤ ND.

This implies that if f = 0 on [ND]0 then f(n) = 0 for all n ∈ Z.

If two exponential polynomials f1 and f2 have at most N frequencies each and polynomial coefficients of degree < D then the exponential polynomial f1 − f2 has at most 2N frequencies and polynomial coefficients of degree < D. If f1, f2 agree on [2ND]0 it follows from the discussion in the previous paragraph that f1(n)− f2(n) = 0 for all n ∈ Z, so that f1, f2 are the same exponential polynomial.

□ Moving to the bivariate case let us first settle the case of simple algebraic poly-

nomials.

- Lemma 2.2. Let p(ξ,η) be a polynomial of degree < D. Then p is determined by its values on the sampling set A = [D]0 × [D]0.


Proof. Take two polynomials p1(ξ,η),p2(ξ,η) in R2 of degree < D, that are identical on A. We will show that they are equal in R2, and are therefore the same polynomial. Indeed, for every (ξ,η) ∈ A we have :

(p1 − p2)(ξ,η) =

(p1k − p2k)(ξ)ηk = 0,

0≤k<D

where we have written pkj(ξ) for the coefficient of ηk in pj. Fix ξ ∈ [D − 1]0 and let η vary in [D − 1]0. For every such ξ, we get a D × D linear system as below:













- (p10 − p20)(ξ)
- (p11 − p21)(ξ) ···


- 1 0 0 ··· 0
- 1 1 12 ··· 1D−1


0 0 ··· 0

=

··· ··· ··· ··· ···













1 D − 1 (D − 1)2 ··· (D − 1)D−1

(p1D−1 − p2D−1)(ξ)

with the D × D matrix on the left being an invertible Vandermonde matrix and so we get that for k ∈ [D − 1]0 and every ξ ∈ [D − 1]0:

(p1k − p2k)(ξ) = 0

Since for each k ∈ [D − 1]0 the polynomial (p1k − p2k)(ξ) has degree < D, we conclude that for every k ∈ [D − 1]0 :

p1k(ξ) = p2k(ξ) for every ξ ∈ R and hence our two polynomials p1,p2 are equal on R2. We have shown that the sampling set [D−1]0 ×[D−1]0 is enough for identification, hence so is its superset [D]0 × [D]0.

### □

Next we introduce frequencies in one variable only.

- Lemma 2.3. Let f(ξ,η) = nj=1 pj(ξ,η)e2πiξxj, xj ∈ T, with the polynomials pj having degree < D and such that n ≤ N.


Then f is determined by its values on the sampling set A = [2ND]0 × [D]0, a set of size O(D2N).

Proof. Fix η = η0 ∈ [D]0. Then f(ξ,η0) is a univariate exponential polynomial with coefficients of degree < D, so, by Lemma 2.1, sampling on [2ND]0 × η0 determines all polynomials pj(·,η0) and all xj for which pj(·,η0) is not the zero polynomial. But it may happen, for a fixed η0, that some of the xj will not be revealed by invoking Lemma 2.1 since pj(·,η0) may be identically zero in the first variable for that particular value η0 of η.

Since each pj(·,·) is assumed not to be identically 0 as a bivariate polynomial it follows from Lemma 2.2 that some of the values of pj(·,·) on [D]0×[D]0 are non-zero. Hence, by the process described in the previous paragraph repeated for all η0 ∈ [D]0 all the xj will be revealed. This implies that for each j we know all the values of pj(·,·) on [D]0 × [D]0, so, by Lemma 2.2 again, all the pj are determined.

### □

The next Lemma is the crucial technical result concerning bivariate exponential polynomials.

x · y = 4D2N

Figure 2. The sampling set for Lemma 2.4

- Lemma 2.4. Let f(ξ,η) = nj=1 pj(ξ,η)e−2πi(xj·ξ+yj·η), (xj, yj) ∈ T2, with the polynomials pj having degree < D and such that n ≤ N.


We can determine f by the following data (see Fig. 2):

- (a) Its values at the sampling set

(2) AN =

1≤r≤N

2

N r

D

0

× [2rD]0

- (b) How many many points of the frequency set V = {(xj, yj)}j≤n of f, project to each x ∈ T. In other words, we know the set X = xj of distinct xj and for each x ∈ X we know the size of the set (x, yj) ∈ V .


The sampling set in (2) is of size O(D2N logN).

Proof. Write X = {xj} for the set of distinct x that appear as first coordinates for the points of V. We partition X according to how many points of V project to each point (see Fig. 3):

X = X1 ∪ ··· ∪ Xr, (for some r ≤ N) where

Xt = x ∈ X : {y : (x, y) ∈ V} = t .

In the proof that follows assumption (b) is only used in order to known to which Xt a given x ∈ X belongs.

A crucial observation (proof by contradiction) here is that for 1 ≤ t ≤ r we have:

N t

- (3) |Xt ∪ Xt+1 ∪ ··· ∪ Xr| ≤


y

(xj, yj)

x

X! X2 X3 X4

Figure 3. The partition of the set X (projections of the points to the x-axis), to the sets X1,X2,···.

We write f as :



p(x,y)(ξ,η)e2πiηy

e2πiξx.

### f(ξ,η) =





x∈X

y : (x,y)∈V

For any fixed η this is an exponential polynomial in ξ with |X| ≤ N terms and polynomial coefficients of degree < D, so, using Lemma 2.1, sampling at [2|X|D]0 × η determines the polynomials of ξ

- (4) qx,η(ξ) =


p(x,y)(ξ,η)e2πiηy,

y : (x,y)∈V

for every ξ ∈ R. Write now

p(x,y)(ξ,η)e2πi(xξ+yη)

### ft(ξ,η) =

x∈Xt y: (x,y)∈V

for the part of f extending over x ∈ Xt only, so that f = f1 + f2 + ··· + fr. We shall first determine f1, then f2, etc.

Notice that for any fixed ξ the quantity qx,η(ξ) is an exponential polynomial in η. If x ∈ Xt then, from (3), this exponential polynomial has |Xt| ≤ ⌊N/t⌋ terms and all its polynomial coefficients have degree < D.

For x ∈ X1, from Lemma 2.3 with the roles of ξ and η reversed, qx,η(ξ) is determined by sampling it on [D]0 × [2D]0. By the discussion before (4) these values of qx,η(ξ) can be determined from the samples of f at [2ND]0 × [2D]0 ⊆ AN. Thus sampling f at AN suffices to determine the bivariate exponential polynomial f1(ξ,η).

To determine f2 we apply roughly the same procedure to the polynomial f − f1. Since we now know f1 we can assume that we have sampled f − f1 on AN. But f − f1 now has |X2 + X3 + ··· + Xr| ≤ ⌊N/2⌋ terms, so to determine the polynomials of ξ

qx,η(ξ), (x ∈ X2 ∪ X3 ∪ ··· ∪ Xr)

we only need to sample f at [2⌊N/2⌋D]0× η . Viewing, again, qx,η(ξ) as an exponential polynomial in η for every fixed ξ, Lemma 2.3 tells us that, for x ∈ X2, it is enough to sample qx,η(ξ) at [D]0 × [4D]0 (since qx,η(ξ) has 2 terms. By the discussion before (4) these values of qx,η(ξ) can be determined from the samples of f at [2⌊N/2⌋D]0×[4D]0 ⊆ AN.

Thus we have also determined f2. We next work on f − f1− f2 to determine f3 from the samples of f at [2⌊N/3⌋D]0 × [6D]0 ⊆ AN and so on.

The fact that |AN| = O(D2N logN) is easily seen as all pairs (m,n) ∈ AN satisfy m · n ≤ 4D2N.

### □

In the next Lemma we point out that data (b) from Lemma 2.4 represent only a finite number of options. These correspond to the finite number of ways a given number of points in T2, whose set of projections onto the x-axis is known, can be distributed over these projections if all we care about is how many points project to each point of the x-axis.

- Lemma 2.5. There are at most finitely many exponential polynomials f of the form


K

pj(ξ,η)e−2πi(x

### j·ξ+yj·η), (xj, yj) ∈ T2,

f(ξ,η) =

j=1

where K ≤ N, pj polynomials of degree < D, with given values on the set AN in (2) and with given the projections of its frequencies onto the x-axis

X = {xj}1≤j≤K. (We do not assume to know how many frequencies project to each x ∈ X)

Proof. Knowing the values of f at AN is exactly the data (a) of Lemma 2.4. What is missing in order to fully know also data (b) of that Lemma is to know how many frequencies project to each x ∈ X. There are only finitely many possibilities for this information. For each of them there is at most one exponential polynomial fitting the data by Lemma 2.4, so, in total, we have finitely many exponential polynomials matching the given values at AN and the given set of projections X.

### □

But a whole continuum of different exponential polynomials with the same data and the same x-projections of their frequencies arise from just two different exponential polynomials with the same data. The conflict between Lemma 2.6 that follows and the preceding Lemma 2.5 will be exploited in the non-constructive, proof by contradiction of our main Theorem 2.1.

- Lemma 2.6. Suppose that


K1

j·ξ+y1j·η), (x1j, y1j) ∈ T2, and

1

p1j(ξ,η)e−2πi(x

f1(ξ,η) =

j=1

K2

j·ξ+y2j·η), (x2j, y2j) ∈ T2,

2

p2j(ξ,η)e−2πi(x

f2(ξ,η) =

j=1

are two different exponential polynomials with K1,K2 ≤ N, p1j,p2j polynomials of degree < D, and with the same values at A2N as in (2).

Then there are infinitely many different exponential polynomials of the form

K

pj(ξ,η)e−2πi(x

j·ξ+yj·η), (xn, yj) ∈ T2,

f(ξ,η) =

j=1

with K ≤ 2N, deg(pj) < D, with xj

⊆ x1j

∪ x2j

1≤j≤K

1≤j≤K1

1≤j≤K2

and having the same values at A2N Proof. Write for λ ∈ C

fλ = λf1 + (1 − λ)f2 Then fλ has the same values at A2N (for every λ) and all these exponential polynomials are different since there is at least one point (ξ,η) where f1 and f2 differ. Finally observe that fλ has at most 2N frequencies all of them at locations projecting down inside the set {x1j} ∪ {x2j}.

□ We arrive to our main result.

## Theorem 2.1. Let

n

pj(ξ,η)e−2πi(x

j·ξ+yj·η), (xj, yj) ∈ T2,

f(ξ,η) =

j=1

with n ≤ N, pj being a polynomial of degree < D.

Then f is determined by knowing its values on the sampling set

- (5) A2N =

1≤r≤2N

2

2N r

D

0

× [2rD]0

with size O(D2N logN).

Proof. Suppose not, so that we can find two exponential polynomials

f1(ξ,η) =

K1

j=1

p1j(ξ,η)e−2πi(x

1 j·ξ+y1j·η)

and

f2(ξ,η) =

K2

j=1

p2j(ξ,η)e−2πi(x

2 j·ξ+y2j·η)

with K1,K2 ≤ N, with the same values on A2N. From Lemma 2.6 then there are infinitely many exponential polynomials with up to 2N frequencies and polynomial coefficients of degree < D that have the same values at A2N. But this contradicts Lemma 2.5 ( used with 2N in place of N).

□

3. Application to identification of polygons

A polygonal region in the plane is described by an ordered sequence of n vertices v0,v1,...,vn−1 ∈ R2. This sequence of vertices, connected by line segments, the edges, which do not intersect except at the vertices, defines a polygonal curve, whose interior is the polygonal region. We also assume that successive edges are not parallel to each other: this forbids redundant vertices in the interior of an edge.

Define the edges wj = vj+1 − vj, where j ∈ [n − 1]0 and addition and subtraction of the indices is done mod n (see Fig. 4) and the corresponding unit vectors uj = wj/ wj . Write sr, r = 1,2,...,k, for all the different directions (slopes) of the edges wj, written once each (no two sr are parallel to each other). The sj are vectors of unit length, so uj = ϵjsϕ(j)), where ϵj = ±1 and ϕ : [n − 1]0 → [k] is the function which tells us which direction vector sr corresponds to edge wj.

Let P be a polygonal region in the plane and P its indicator function. The BrionBarvinok formula [Rob24] is a valuable formula for the Fourier Transform of P. In our notation it becomes, for t = (ξ,η) ∈ R2,

- (6) P(t) =


1 4π2

n−1

det(uj−1,uj) (uj−1 · t) (uj · t)

e−2πiv

### j·t.

j=0

v0

vn−1

vj−1

wj−1

vj

wj = wj uj vj+1

Figure 4. A polygonal region in the plane.

This formula is valid whenever all the denominators uj · t are not zero. To cancel all denominators we multiply (6) by the product

(s1 · t) (s2 · t) ··· (sk · t). Since uj−1 and uj correspond to different direction vectors we obtain

- (7) (s1 · t) (s2 · t) ··· (sk · t) P(t) =


n−1

1 4π2

(sr · t) e−2πiv

j·t.

det(uj−1,uj) ϵj−1ϵj

=

j=0

r=1,...,k r ϕ(j−1),ϕ(j)

The expression on the right hand side of (7) is an exponential polynomial, which we denote by fP(t), in t = (ξ,η) with n terms and polynomial coefficients of degree < k−1. If we happen to know the direction vectors s1,...,sk then knowing the values of P on a sampling set A ⊆ Z2 implies that we know the samples of fP(t) on A.

If the sampling set A is enough to identify fP(t) then we have determined P(t) except when t is on the finite set of straight lines

t ∈ R2 : sr · t = 0 for some r ∈ [k] .

By the continuity of P(t) this function is then determined everywhere and so is P by Fourier inversion.

Combining this with Theorem 2.1 we obtain the following. (Again, the restriction of knowing an apriori bounded region where P lies is natural.)

- Theorem 3.1. Suppose P ⊆ [0,1)2 is a polygonal region with n ≤ N vertices and whose edges are of a finite set of known slopes s1,...,sk.


Then P can be determined by sampling its Fourier Transform P on the following set of points in Z2

N

2N r

- (8) A = A(k,N) =


2

(k − 1)

× [2r(k − 1)]0

0

r=1

which is of size O(k2N logN).

Figure 5. A polygonal region in the plane with sides parallel to the axes.

- Corollary 3.1. Suppose P ⊆ [0,1)2 is a polygonal region all of whose edges are parallel to the x or the y axis (see Fig. 5).


Then P can be determined by sampling its Fourier Transform on the set A in (8) with k = 2.

- Remark 3.1. It is perhaps interesting to see that when identifying a polygon in the plane all of whose edges are parallel to the axes it is enough to know the vertices: the interconnections of the vertices via axis-parallel edges (and when these vertices are guaranteed to be non-degenerate) arise uniquely.


To see this observe first that any vertical line (parallel to the y-axis) must always contain an even number of polygon vertices and they are always connected as follows. Since every polygon vertex has both a vertical and a horizontal edge it follows that all vertical edges of the vertices belonging to a vertical line must connect them among themselves and the only way for this is if the lowest vertex connects to the second lowest, the third lowest to the fourth and so on. This determines all vertical edges of the polygon. Similarly all horizontal edges are determined.

This is not strictly used in our (non-constructive) proof as what we do is to determine the Fourier Transform of the indicator function of the polygon, which contains all the information we need.

The following Theorem, a generalization of Theorem 3.1, has essentially the same proof as Theorem 3.1, which we indicate below.

- Theorem 3.2. Suppose f : [0,1)2 → C takes finitely many values and each level set of f


L(v) = t ∈ [0,1)2 : f(t) = v

- f = v4
- f = v5


f = v3 f = v2

f = v1

Figure 6. The level sets of a function are polygonal regions with few slopes.

is a polygonal region whose edges are of a finite set of known slopes s1,...,sk (see Fig. 6). Suppose also that the total number of vertices appearing in any L(v) (written once each) is n ≤ N.

Then f can be determined by the samples of f on the set A(k,N) in (8) which is of size O(k2N logN). Proof. The function f can be written as the finite sum

f(x) =

v L(v)(x),

v∈V

where V ⊆ C is the finite set of values taken by f. It follows that f(t) =

v L(v)(t).

v∈V

Using again the Brion-Barvinok formula for each L(v) we obtain an identity analogous to (6), valid, again, whenever all sj ·t are non-zero. As in the proof of Theorem 3.1, multiplying by (s1 · t)···(sk · t) we obtain an exponential polynomial analogous to (7) which has at most N vertices and the polynomial coefficients all have degree < k − 1. The remaining of the proof is exactly the same.

### □

3.1. Unknown slopes. When we try to extend Theorems 3.1 and 3.2 to the case of knowning the maximum number of different slopes but not knowing the slopes themselves, we encounter the unpleasant fact that when one subtracts two functions like those in Theorem 3.2 one obtains again such a function but with much larger parameters. If the numbers f1, f2 are as in Theorem 3.2, with at most N vertices total in the polygonal regions involved then it can be that the number of vertices in the corresponding representation of f1 − f2 is quadratic in N, as shown

in Fig. 7. If we try to apply Theorem 3.2 to f1 − f2 we end up with a superquadratic number of samples.

f2 = w2

f2 = w1

f2 = w3 f2 = wN

- f1 = v1
- f1 = v2 f1 = v3


f1 − f2 = v3 − w3

f1 = vN

Figure 7. The two functions f1, f2 have N different levels each, with number of vertices O(N), but f1 − f2 may have N2 different values with a quadratic total number of vertices.

The solution to this is to change the representation. Instead of parametrizing f by the number of values it takes we parametrize it by the number of building blocks, indicator functions of a polygonal region, that are needed to construct f.

- Theorem 3.3. Suppose f : [0,1)2 → C is of the form


n

- (9) f(x, y) =


(x, y),

fj P

j

j=1

where fj ∈ C and the Pj are polygonal regions, not necessarily disjoint, with a total number of vertices at most N. Suppose also that the different slopes appearing in some Pj are among the known slopes s1,...,sk.

Then f can be determined by the samples of f on the set A(k,N) in (8) which is of size O(k2N logN). Proof. Exactly the same as the proof of Theorem 3.2.

### □

- Corollary 3.2. Suppose f is as in Theorem 3.3 with parameters k (maximum number of different slopes) and N (maximum total number of vertices appearing in any of the polygons Pj), but we do not assume that we know the slopes.


Then f can be determined by the samples of f on the set A(2k,2N) in (8) which is of size O(k2N logN).

Proof. Suppose f1, f2 are both of the form (9) with parameters k and N. Then f1 − f2 is also of the same form but with parameters 2k and 2N, at most. If f1, f2 have the same Fourier samples on A(2k,2N) then, by Theorem 3.3, since f1 − f2 has Fourier samples identically 0 on A(2k,2N), it follows that f1 ≡ f2.

### □

Refering to Fig. 7 notice that f1 − f2 has parameters 2k and 2N if we assume that f1, f2 have parameters k and N. We do not demand that the Pj in (9) are disjoint and this makes for a more flexible and algebraically pliable representation.

- Corollary 3.3. Suppose P ⊆ [0,1)2 is a polygonal region with n ≤ N vertices and whose edges have at most k different (unknown) slopes.


Then P can be determined by sampling its Fourier Transform P on A(2k,2N) which is of size O(k2N logN). Proof. The function P is of the form covered by Corollary 3.2, so it is determined by its Fourier samples on A(2k,2N).

### □

Remark 3.2. It is less than satisfying that the maximum number k of different slopes appears quadratically in the size of the sample. Of course in the general case of exponential polynomials with coefficients of degree < k the number of parameters involved in each polynomial coefficient is also quadratic so one cannot expect a general improvement. But in the case of polygonal regions the polynomial coefficients that appear on the right side of (7) are a product of ≤ k linear forms in R2 and that involves only 2k parameters, so one may hope to find a way to exploit this. As it stands, using the general recovery of exponential polynomials as a means to recover polygons the general case with N different slopes gives a sample size larger than N3 which is much larger than the number of parameters.

References

[CL18] A. Cuyt and W.-S. Lee. Multivariate exponential analysis from the minimal number of samples. Advances in Computational Mathematics, 44(4):987–1002, 2018. [Cou10] D. Courtney. Unions of arcs from fourier partial sums. The New York Journal of Mathematics [electronic only], 16:235–243, 2010. [DKP23] B. Diederichs, M. N. Kolountzakis, and E. Papageorgiou. How many fourier coefficients are needed? Monatshefte für Mathematik, 200(1):23–42, 2023.

[dP95] G. R. de Prony. Essai experimental et analytique: sur les lois de la dilatabilite des fluides elastique et sur celles de la force expansive de la vapeur de l’eau et de la vapeur de l’alkool, a differentes temperatures. Journal Polytechnique ou Bulletin du Travail fait a l’Ecole Centrale des Travaux Publics, 1795.

[EvdPSW15] G. Everest, A. van der Poorten, I. Shparlinski, and Th. Ward. Recurrence Sequences. American Mathematical Soc., 2015. [Rob24] S. Robins. Fourier Analysis on Polytopes and the Geometry of Numbers: Part I: A

Friendly Introduction, volume 107. American Mathematical Society, 2024. [Rud62] W. Rudin. Fourier analysis on groups. Wiley-Interscience, 1962. [Sau18] T. Sauer. Prony’s method in several variables: symbolic solutions by universal inter-

polation. Journal of Symbolic Computation, 84:95–112, 2018. [VMB02] M. Vetterli, P. Marziliano, and T. Blu. Sampling signals with finite rate of innovation. IEEE transactions on Signal Processing, 50(6):1417–1428, 2002.

[WP16] M. Wischerhoff and G. Plonka. Reconstruction of polygonal shapes from sparse Fourier samples. Journal of Computational and Applied Mathematics, 297:117–131, 2016.

Department of Mathematics and Applied Mathematics, University of Crete,, Voutes Campus, 70013 Heraklion, Greece,, and, Institute of Computer Science, Foundation of Research and Technology Hellas, N. Plastira 100, Vassilika Vouton, 700 13, Heraklion, Greece

#### Email address: kolount@gmail.com

Department of Mathematics and Applied Mathematics, University of Crete,, Voutes Campus, 70013 Heraklion, Greece.

#### Email address: manos.ch.spyridakis@gmail.com

