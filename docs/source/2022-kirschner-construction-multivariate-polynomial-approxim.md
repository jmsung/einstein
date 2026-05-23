---
type: source
kind: paper
title: Construction of multivariate polynomial approximation kernels via semidefinite programming
authors: Felix Kirschner, Etienne de Klerk
year: 2022
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2203.05892v3
source_local: ../raw/2022-kirschner-construction-multivariate-polynomial-approxim.pdf
topic: general-knowledge
cites:
---

# arXiv:2203.05892v3[math.OC]17Jul2023

## CONSTRUCTION OF MULTIVARIATE POLYNOMIAL APPROXIMATION KERNELS VIA SEMIDEFINITE PROGRAMMING

#### Felix Kirschner ∗ Etienne de Klerk †

July 18, 2023

Abstract

In this paper we construct a hierarchy of multivariate polynomial approximation kernels for uniformly continuous functions on the hypercube via semidefinite programming. We give details on the implementation of the semidefinite programs defining the kernels. Finally, we show how symmetry reduction may be performed to increase numerical tractability.

Keywords Polynomial kernel method · semidefinite programming

### 1 Introduction

A classical problem in approximation theory is uniform approximation of a given function by linear combinations of orthogonal polynomials. In the following we will denote by K the n-dimensional hypercube, i.e. K := [−1,1]n. Orthogonality of polynomials may be defined in the following way. Let µ be a positive finite Borel measure supported on the compact set K = [−1,1]n ⊂ Rn. We say two functions f,g ∈ C(K) are orthogonal (w.r.t. µ), if

f(x)g(x)dµ(x) = 0.

⟨f,g⟩µ :=

K

Let {pα}α∈Nn be a system of orthogonal polynomials with respect to a measure µ. Consider a kernel Kr(x,y) : Rn × Rn → R given by

Kr(x,y) :=

gαpα(x)pα(y), (1)

α∈Nnr

for given constants gα for α ∈ Nnr , where Nnr = {α ∈ Nn : α1 + ··· + αn ≤ r}. Then the convolution operator, defined as

f(y)Kr(x,y)dµ(y), (2) maps any µ-integrable function f to a polynomial of degree at most r. More precisely,

K(r)(f)(x) :=

K

K(r)(f)(x) =

bαpα(x), where bα = ⟨pα,f⟩µ gα. (3)

α∈Nnr

The coefficients gα of the kernel Kr determine the approximation. Our goal is to approximate a given continuous f defined on K, by a sequence of polynomials of increasing degree, such that the sequence converges to f, uniformly on K. We further introduce a quantity

1/2

∥x − y∥2Kr(x,y)dµ(x)dµ(y)

σr :=

,

K×K

∗Tilburg University, f.c.kirschner@tilburguniversity.edu †Tilburg University, e.deklerk@tilburguniversity.edu

This work is supported by the European Union’s Framework Programme for Research and Innovation Horizon 2020 under the Marie Skłodowska-Curie grant agreement N. 813211 (POEMA).

called the resolution of the kernel Kr(x,y) in [28]. Our aim in this paper is to construct kernels Kr with minimal resolution such that K(r)(f) converges to f uniformly on K = [−1,1]n and to bound the rate of convergence in terms of σr. The resolution may be interpreted as a measure of how much mass of the kernel is concentrated away from the line where x = y. If all gα = 1 in expression (3) then K(r) is the identity operator on the space of polynomials of degree at most r, and the associated resolution is zero.. This kernel will have all of its mass concentrated at x = y. To ensure uniform convergence we want a kernel that has as much mass as possible at the line x = y for every r ∈ N, while fulfilling some other properties.

#### Outline and contributions

The aim of this paper is to present a computational procedure, based on semidefinite programming (SDP) (cf. [23, 26]), to construct non-negative polynomial kernels on K = [−1,1]n suitable for approximation. We show that these kernels generalize a kernel which is called the Jackson kernel in [28], but this is different from the original kernels introduced by Jackson in [15]; we give more details on this in section 2.2. As the orthogonal basis we will use products of univariate Chebyshev polynomials, as reviewed in section 1.3, and the fixed measure µ will be the corresponding product of measures so that the Chebyshev polynomials are orthogonal. The resulting kernel polynomial method is reviewed in section 2 for the univariate case (n = 1), and extended to the multivariate case in section 2.4. In section 3 we discuss how to form the SDP problems that yield the optimal kernels, in the sense that their resolution is minimal. In section 4 we show how to exploit algebraic symmetry by using techniques from [21, 25] to reduce the size of these SDP problems. We show in section 5 that our constructions are superior to simply multiplying optimal univariate kernels in a well-defined sense. Finally, in section 6 we give further details of our numerical computations and show they are useful in practice to approximate non-differentiable functions and related applications in physics.

#### 1.1 Prior and related work

Setting all coefficients of the kernel Kr equal to gα = (⟨pα,pα⟩µ)−1, the resulting approximation in the setting described above is simply the Chebyshev expansion truncated at degree r. In the univariate case, the resulting kernel is known as the Dirichlet kernel [9]. In the multivariate case it is known as the Christoffel-Darboux kernel (named after [5, 6]). This approximation works well for analytic functions, as reviewed in [24]. Lasserre [18] draws an interesting connection between the celebrated moment-SOS hierarchy [16] and the Christoffel-Darboux kernel. For non-differentiable functions, the truncated Chebyshev expansion, i.e., the Christoffel-Darboux kernel, may lead to unwanted oscillations at points where the function is not differentiable, as reviewed in [28]. These oscillations are often referred to as the Gibbs phenomenon, see [13] for a survey. In [20] the authors develop a method for approximating possibly discontinuous functions using the Christoffel-Darboux kernel, where the Gibbs phenomenon does not occur. Other approaches to get rid of unwanted oscillations is to make use of non-negative kernels as has been done in [28]. For this reason, positive approximation kernels are popular in physics for the approximation of non-smooth functions in various settings. The reader is again referred to the excellent survey [28] for more details. The aim of our work is to generalize these kernels to several variables in a natural way, thus providing computational alternatives to using products of univariate kernels.

We continue to fix some notation, and the review properties of univariate Chebyshev polynomials for later use. Our exposition closely follows the survey [28].

#### 1.2 Notation

For 1 < n ∈ N we define [n] := {1,2,...,n}. The canonical unit vectors in Rn are denoted by ei, i.e., ei is the zero vector with a 1 at the i-th component. The polynomial ring is denoted by R[x], where x = (x1,...,xn). A polynomial

p ∈ R[x] is said to be a sum-of-squares if it can be written as a sum of squared polynomials, i.e., p(x) = ki=1 qi(x)2 for k ∈ N and qi ∈ R[x] for all i ∈ [k]. The set of polynomials of degree less than or equal to r will be denoted by the set R[x]r. For a set K ⊆ Rn we denote by C(K) the set of continuous functions on K. Sn is the set of n × n symmetric matrices, and Sn⪰ is the set of symmetric positive semidefinite (psd) matrices. A symmetric matrix S is called positive semidefinite if xTSx ≥ 0 for all x ∈ Rn. We may write S ⪰ 0 to indicate S is psd. For α,β ∈ Nn the Kronecker-δα,β is defined as

1, if αi = βi ∀i ∈ [n] 0, otherwise.

δα,β =

For two matrices A,B of appropriate size we define the trace inner product ⟨A,B⟩ := Tr(ATB). We also set

n + r r

s(n,r) =

.

- 1.3 Chebyshev polynomials Let K = [−1,1] and fix the measure µ on K defined by dµ(x) = (π√1 − x2)−1dx, x ∈ K. The Chebyshev polynomials of the first kind form a system of orthogonal polynomials. We will refer to the k-th Chebyshev polynomial of first kind as Tk(x). We have for k ∈ Z

Tk(x) = cos(k arccos(x)). (4) Define for f,g : [−1,1] → R

⟨f,g⟩µ =

1

−1

f(x)g(x) π√1 − x2

dx

to obtain the following orthogonality relations for the Chebyshev polynomials of the first kind

⟨Tk,Tm⟩µ =

1 + δk,0 2

δk,m. (5)

Chebyshev polynomials exhibit nice stability and convergence properties in practice which is why they are the first choice in many applications. It is straightforward to generalize the Chebyshev polynomials to the multivariate case. Let K = [−1,1]n and define

dµ(x) :=

n

i=1

1 π 1 − x2i

dx.

Then, for α ∈ Nn the corresponding multivariate Chebyshev polynomial of the first kind is defined as

Tα(x) =

n

i=1

Tα

i

(xi).

The orthogonality relations extend in the following way

⟨Tα,Tβ⟩µ =

K

Tα(x)Tβ(x)dµ(x) =

n

i=1

1

−1

Tα

i

(xi)Tβ

i

(xi) π 1 − x2i

dxi

=

n

i=1

1 + δα

i,0

2

δα

i,βi = cαδα,β,

with cα = 2 1 H(α), where H(α) is the Hamming weight of α, i.e. the number of non-zero entries.

- 1.4 Main result


Using the Chebyshev polynomials we are ready to state our main result. We will be interested in kernels Kr(x,y) satisfying the following properties for K = [−1,1]n:

- P1. Kr(x,y) = α∈Nn

r

gαTα(x)Tα(y), for gα ∈ R for α ∈ Nnr

- P2. Kr(x,y) ≥ 0 for all (x,y) ∈ K × K and all r;
- P3. K Kr(x,y)dµ(y) = 1 for all x ∈ K for all r;
- P4. limr→∞ σr = 0.


In the statement of proposition 1, recall that the modulus of continuity of f ∈ C(K) is defined as

|f(x) − f(y)|.

ωf(δ) := max

x,y∈K ∥x−y∥≤δ

Proposition 1. Let K = [−1,1]n and f : K → R be continuous on K with modulus of continuity ωf. Under the above conditions P1-P4 on Kr(x,y) one has K(r)(f) → f as r → ∞, uniformly on K. Moreover,

π √2

∥K(r)(f) − f∥∞,K≤ 2 1 +

ωf(σr). (6)

Our main result is the construction of kernels whose resolutions satisfy σr = O(1/r) using semidefinite programming techniques (see proposition 2). This proves that our kernels yield the best possible rate of convergence for continuous f that are not differentiable, due to Bernstein’s theorem (see [2]). The proof of proposition 1 will be postponed to later, until we have given all necessary definitions and auxiliary results. Let us mention at this point that proposition 1 is a known result in approximation theory. Indeed, the argument is essentially as given in the PhD thesis of Jackson [14]. We simply give a proof in our specific setting for completeness, since we could not find a statement of proposition 1 in a suitable form in the literature.

### 2 The kernel polynomial method

We begin by considering kernels to approximate univariate functions. Let Kr be a kernel of the following form

r

gkTk(x)Tk(y). (7)

Kr(x,y) = g0 + 2

k=1

Kernels of this kind clearly satisfy property P1. If we set g0 = 1, the resulting kernel also satisfies P3. In the following, we will explore how to find kernels that of this form that additionally satisfy P2 and are therefore suitable for approximation. For this we will first introduce trigonometric polynomials.

- 2.1 Trigonometric polynomials A trigonometric polynomial p(t) of degree r is defined as


r

p(t) = p0 +

(pk cos(kt) + p−k sin(kt)),

k=1

for pk ∈ R for k = −r,−r + 1,...,r − 1,r. The following lemma is proved in [12].

- Lemma 1. If p(t) is a non-negative trigonometric polynomial of degree r, then there exists a positive semidefinite matrix Q ∈ S⪰r+1 such that p(t) = vTQv where


vT = [1,cos(t),...,cos(mt),sin(mt)] if r = 2m for some m ∈ N and

t 2

t 2

t 2

t 2

t 2

vT = cos

,sin

,cos t +

,...,cos mt +

,sin mt +

if r = 2m + 1 for some m ∈ N. Remark 1. Let us mention that there are stronger results of the kind of lemma 1. For example Corollary 2 in [11]. We state this weaker result for the ease of exposition.

Note that every trigonometric polynomial of the form

gives rise to a kernel of the form

r

p(t) = g0 + 2

k=1

Kr(x,y) = g0 + 2

To see this, consider the following substitution

gk cos(kt) (8)

r

gkTk(x)Tk(y).

k=1

- 1

- 2


[p(arccos(x) + arccos(y)) + p(arccos(x) − arccos(y))]

r

- 1

- 2


[cos(k(arccos(x) + arccos(y))) + cos(k(arccos(x) − arccos(y)))]

= g0 + 2

gk

k=1

r

r

gkTk(x)Tk(y). (9)

= g0 + 2

gk cos(k arccos(x))cos(k arccos(y)) = g0 + 2

k=1

k=1

If p(t) is non-negative on [−π,π], then Kr(x,y) is non-negative on [−1,1]2.

- Theorem 1. (Fej´er (1915)) Every non-negative trigonometric polynomial of degree r of the form


p(t) = λ0 + λ1 cost + µ1 sint + ··· + λr cosrt + µr sinrt can be written as

2

r

cνeiνt

p(t) =

ν=0

for cν ∈ C. In other words, there is a one-to-one correspondence between trigonometric polynomials of the form

t  → λ0 + λ1 cos(t) + µ1 sin(t) + ··· + λr cos(rt) + µr sin(rt) that are non-negative for every t and functions of the form

2

r

cνeiνt

t  →

##### .

ν=0

This correspondence may be leveraged to obtain kernels with minimum resolution, which is done in the next section.

#### 2.2 Constructing optimal kernels

In this subsection we will revisit the approach described in [28], showing the kernel they obtain has minimum resolution among all non-negative kernels on [−1,1]2. To avoid ambiguity, note the following. The authors in [28] refer to their kernel as the Jackson kernel, even though in the literature there is another object which is referred to in that name. Therefore, we will refer to the kernel from [28] as the minimum resolution kernel, reserving the term ”Jackson kernel” for the object Jackson used in [15] to prove his theorems. We are interested in non-negative trigonometric polynomials with cosine terms only, as these are the ones giving rise to kernels of the form that we want as we have seen in (8), (9). It is easy to see that if all sine-terms are zero, then the cν terms are real. Thus, this gives us a way to characterize kernels of the form (7) that are non-negative. Consider a function of the form

2

r

aνeiνφ

p(φ) =

##### ,

ν=0

for aν ∈ R. Rewriting this expression we find

r

aνaµ cos([µ − ν]φ)

p(φ) =

ν,µ=0

r−k

r

r

a2ν +

=

aνaν+k cos(kφ)

ν=0

ν=0

k=1

r

gk cos(kφ), for

= g0 +

k=1

r−k

aνaν+k. (10)

gk =

ν=0

Therefore, every set of real numbers a0,a1,...,ar satisfying rk=0 a2k = 1 gives rise to a kernel of the form (7) satisfying P1, P2, P3 when the gk are set as in (10). A first idea to construct a kernel would be to set all ak = √r1+1, to ensure that g0 = 1. This leads to the so called Fej´er kernel, whose coefficients we denote by

k r + 1

gkF = 1 −

.

However, this kernel is not optimal in the sense that is does not have minimum resolution. We next take a look at kernels satisfying P1-P3, with minimal resolution σr. Note that for the resolution of the kernel we have

σr2 =

(x − y)2Kr(x,y)dµ(x)dµ(y) = g0 − g1.

K

We will formulate an optimization problem to minimize resolution with respect to ak.

min g0 − g1 ⇔ min

r

s.t. g0 = 1 s.t.

k=0

r−1

r

a2k −

akak+1

k=0

k=0

a2k = 1

(11)

Solving this problem results in the minimum resolution kernel mentioned earlier which is called the Jackson kernel in [28], whose coefficients are given by

(r − k + 2)cos r πk+2 + sin r πk+2 cot r+2 π r + 2

gk,rKPM =

. (12)

Thus, we see that σr2 = g0KPM,r − g1KPM,r = 1 − cos r+2 π = O(1/r2).

#### 2.3 Uniform convergence in terms of σr in the multivariate case

In this subsection we prove we may also bound the rate of convergence in terms of σr in the multivariate case. We first prove the result for uniformly continuous periodic functions on [−π,π]n and then extend the results for the case of uniformly continuous functions on [−1,1]n. Recall that the modulus of continuity for a uniformly continuous function f is defined as

|f(x) − f(y)|.

ωf(δ) := max

x,y∈K ∥x−y∥≤δ

Further, note the following properties of the modulus of continuity

- 1. For λ,δ > 0 : ωf(λδ) ≤ (1 + λ)ωf(δ) (Lemma 1.3 in [22])
- 2. For continuous f and δ > 0 one has |f(x − y) − f(x)|≤ 1 + δ12 ||y||2 ωf(δ) (by proof of Proposition 5.1.5 in [1])


Let f be uniformly continuous and periodic on B := [−π,π]n and let the kernel

n

Kr(x) = 1 +

2H(α)gα

cos(αixi) (13)

α∈Nnr \{0}

i=1

be non-negative of degree r. Define

1 (2π)n B

f(x − y)Kr(y)dy.

K(r)(f)(x) =

Further, note that

1

|K(r)(f)(x) − f(x)| ≤

(2π)n B|f(x − y) − f(x)|Kr(y)dy ∗

1 (2π)n B

1 δ2∥y∥2 ωf(δ)Kr(y)dy

≤

1 +

1 (2π)n B∥y∥2Kr(y)dy,

ωf(δ) δ2

= ωf(δ) +

where ∗ follows from the second property of the modulus of continuity. Note that since −π ≤ yi ≤ π we find

n

n

π2 2

||y||2 =

yi2 ≤

(1 − cos(yi)).

i=1

i=1

(14)

Thus,

 

n

π2 2

∥y∥2Kr(y)dy ≤

B

i=1

π2 2

= (2π)n

where we used the fact that

  (15)

n

cos(αiyi)dy

(2π)n −

2H(α)gα

cos(yi)

B

α∈Nnr

i=1

n

) , (16)

(1 − ge

i

i=1

- 1

- 2


(cos((k − 1)x) + cos((k + 1)x)).

cos(x)cos(kx) =

) = π/√2σr we find by (14) and the first property of the modulus of continuity:

) = σr2. Choosing δ = π22 ni=1(1 − ge

Straight-forward calculation shows that ni=1(1 − ge

i

i

√

√

|K(r)(f)(x) − f(x)|≤ 2ωf(π/

2σr) ≤ 2(1 + π/

2)ωf(σr).

If f is a continuous function on [−1,1]n define g(θ) = f(cos(θ)) = f(cos(θ1),...,cos(θn)) for θ ∈ [0,π]n. Further, define for θi ∈ [−π,0] g(θ) = g(θ1,...,−θi,...,θn). Similarly, we may define g(θ) for all θ ∈ [−π,π]n. We see g(θ) is even and periodic on [−π,π]n. Since it is even, the convolution with a kernel of the form (13) will have only cosine terms. The argument is as follows:

(2π)nB(r)(g)(θ) =

g(θ − φ)Kr(φ)dφ

K

g(φ)Kr(θ − φ)dφ

=

B

 1 +

 dφ.

n

2H(α)gα

cos(αi(θi − φi))

=

g(φ)

B

α∈Nnr \{0}

i=1

=

g(φ)dφ+

B

n

2H(α)gα

g(φ)

(cos(αiθi)cos(αiφi) + sin(αiθi)sin(αiφi))dφ.

B

α∈Nnr \{0}

i=1

The integrand in the last integral will be the function g times the sum of products of sine and cosine functions. The domain B = [−π,π]n is symmetric and g is even by construction. Hence, every integral containing a sine function will evaluate to zero, since the sine function is odd. We may now assume the approximation will take the following form

n

qr(θ) = K(r)(g)(θ) = a0 +

2H(α)aα

cos(αiθi) . (17)

α∈Nnr

i=1

Substituting θi = arccos(xi) results in a polynomial

pr(x) = a0 +

aαTα(x).

α∈ Nnr

This polynomial will serve as an approximation for f, and we will bound the absolute error in terms of σr. For this we will need the following Lemma.

- Lemma 2. For f,g as defined above we have ωg(δ) ≤ ωf(δ).


Proof. The proof is straight-forward and omitted for the sake of brevity.

We have gathered everything required to prove proposition 1.

Proof of proposition 1. First, note that

|f(x) − pr(x)| ≤ sup

|g(θ) − qr(θ)| ≤ 2(1 + π/

sup

x∈[−1,1]n

θ∈[−π,π]n

√

2)ωg(σr) ≤ 2(1 + π/

√

2)ωf(σr),

where the last inequality follows by lemma 2. Above we have obtained a polynomial pr of degree less than r which approximates f ∈ C(K). We did so by using the convolution with a kernel of the form (13). Using the substitution given in (9) we may transform the kernel into a positive kernel of the form

Kr(x,y) = 1 +

2H(α)gαTα(x)Tα(y).

α∈Nnr

It is left to show that both approaches are equivalent, i.e., lead to the same approximation of the function f. For this note the following. The polynomial we obtain via the approximation process defined as per (2) is

K(r)(f)(x) =

f(y)dµ(y) +

f(y)Tα(y)dµ(y) Tα(x)

2H(α)gα

K

K

α∈Nnr

2H(α)gαcαTα(x),

= c0 +

α∈Nnr

where

f(y)Tα(y)dµ(y).

cα = ⟨f,Tα⟩µ =

K

We need to check whether we get the same coefficients from both approaches. Recall the approximation from before

where

pr(x) = a0 +

α∈Nnr

1 (2π)n B

aα =

We would like to show that aα = cα, i.e.,

2H(α)gαaαTα(x),

n

g(φ)

cos(αiφi)dφ.

i=1

For this note that

n

f(y)

K

i=1

cos(αi arccos(yi)) 1 − yi2

- 1

- 2n B


dy =

1 2n B

aα =

g(φ)

n

cos(αiφi)dφ =

i=1

[0,π]n

n

g(φ)

cos(αiφi)dφ.

i=1

f(cosφ)

n

cos(αiφi)dφ. (18)

i=1

Next we can make use of the following substitution

Finally, using (18) we find

1 1 − x2i

φi = arccos(xi) ⇒ dφi = −

dxi.

n

n

cos(αi arccos(xi)) 1 − x2i

f(x)

dx = cα.

aα =

cos(αiφi)dφ =

f(cos(φ))

[0,π]n

K

i=1

i=1

This proves we indeed have that both approaches are equivalent, i.e., they lead to the same approximation. This completes the proof of proposition 1.

#### 2.4 Positivstellensatz for the multivariate case

In this subsection we present a Positivstellensatz for multivariate trigonometric polynomials. This result allows for the construction of semidefinite programs whose solutions provide optimal kernels with respect to σr. To this end, recall the identities: if pk(ϕ) = cos(kϕ), then, for x,y ∈ [−1,1],

pk(arccos(x)) = Tk(x) (pk(arccos(x) + arccos(y)) + pk(arccos(x) − arccos(y))) = Tk(x)Tk(y).

- 1

- 2


As a consequence, if we start with a non-negative multivariate trigonometric polynomial of the form

2H(α)gα

(ϕ1,...,ϕn)  → 1 +

α∈Nnr \{0}

cos(αiϕi),

i∈[n]

then replacing each pα

(ϕi) := cos(αiϕi) by (pα

i

- 1

- 2


(arccos(xi) − arccos(yi))) as in (9) (this operation preserves non-negativity), one obtains the non-negative kernel

(arccos(xi) + arccos(yi)) + pα

i

i

K(x,y) = 1 +

(yi) x,y ∈ K.

2H(α)gα

Tα

(xi)Tα

i

i

α∈Nnr \{0}

i∈[n]

In contrast to the polynomial case, each multivariate, positive, trigonometric polynomial is a sum of squares of trigonometric polynomials. (The degrees appearing in the sums-of-squares may be arbitrarily large, though.)

- Theorem 2 (e.g. Theorem 3.5 in [10]). If p is a positive trigonometric polynomial, then there exists an r ∈ N and a hermitian p.s.d. matrix M of order n+r r such that

p(ϕ) = exp(ıαTϕ) ∗α∈N

n r

M exp(ıαTϕ) α∈N

n r

.

Again, the value r in the theorem may be arbitrarily large, but for fixed r, one may consider the kernel given by solving the SDP:

σr2 = min

gα : α∈Nnr

n

i=1

(1 − ge

i

) (19) subject to

1 +

α∈Nnr \{0}

2H(α)gα

i∈[n]

cos(αiϕi) = exp(ıαTϕ) ∗α∈N

n r

M exp(ıαTϕ) α∈N

n r

M ⪰ 0.

- 3 Reformulation of the SDP


In this section we present how to find solutions to problem (19). But first we show that the optimal solution to the problem maybe assumed w.l.o.g. to be real.

- 3.1 Existence of a real solution Let M = P + ıQ, for P ∈ Ss(n,r) and Q being skew-symmetric of the same size. Then,


exp(ıαTϕ) ∗α∈N

(P + ıQ) exp(ıαTϕ) α∈N

cos (α − β)Tϕ Pα,β

=

n r

n r

α,β∈Nnr

sin (α − β)Tϕ Qα,β,

−

α,β∈Nnr

![image 1](<2022-kirschner-construction-multivariate-polynomial-approxim_images/imageFile1.png>)

![image 2](<2022-kirschner-construction-multivariate-polynomial-approxim_images/imageFile2.png>)

(a) r = 30 (b) r = 50

Figure 1: Plots of K(r)(δ(0,0)), i.e. convolution of kernel with minimum resolution σr with the Dirac-δ at (x,y) = (0,0) for different values of r

because of the identities

cos αTϕ cos βTϕ + sin αTϕ sin βTϕ = cos (α − β)Tϕ and

cos αTϕ sin βTϕ − sin αTϕ cos βTϕ = sin (α − β)Tϕ .

We continue to show we may without loss of generality assume there exists an optimal solution which is real symmetric, i.e., Q = 0. Let P + ıQ be an optimal solution to (19) and define

G(ϕ1,...,ϕn) =

γ∈Nnr

=

2H(γ)gγ

cos(γiϕi)

i∈[n]

cos (α − β)Tϕ Pα,β −

sin (α − β)Tϕ Qα,β

α,β∈Nnr

α,β∈Nnr

Now, since the cosine is even we find G(ϕ1,...,ϕn) = G(−ϕ1,...,−ϕn). So

- 1

- 2


(G(ϕ1,...,ϕn) + G(−ϕ1,...,−ϕn))

G(ϕ1,...,ϕn) =

- 1

- 2 α,β∈N


cos (α − β)Tϕ Pα,β −

sin (α − β)Tϕ Qα,β

=

α,β∈Nnr

n r

cos (β − α)Tϕ Pα,β −

sin (β − α)Tϕ Qα,β

+

α,β∈Nnr

α,β∈Nnr

cos (α − β)Tϕ Pα,β.

=

α,β∈Nnr

Therefore, we may subsequently assume that in (19) the matrix M is real symmetric.

#### 3.2 Equating coefficients via trigonometric identities

The standard idea of SOS-optimization is equating coefficients. For convenience, we restate the optimization problem. Recall that it is enough to consider real symmetric matrices.

σr2 = min

gα : α∈Nnr

n

) (20)

(1 − ge

i

i=1

subject to

2H(γ)gγ

cos[(α − β)Tϕ]Mα,β (21)

1 +

cosγiϕi =

α,β∈Nnr

γ∈Nnr \{0}

i∈[n]

M ⪰ 0,

However, the form in which the two representations of the sought polynomial are given does not allow for an immediate construction of the corresponding constraint matrices. The question is, what α,β of the right-hand-side end up contributing to a γ of the left-hand-side, and in what way. Let for I ⊆ [n] the function ωI : Rn → Rn be defined as follows

##### ωI(x)i = −xi, if i ∈ I xi, otherwise.

In other words, ωI flips the sign of xi for all i ∈ I. Recall the trigonometric identity

n

n

2H(x)

ωI(x)i , (22)

cos(xi) =

cos

i=1

i=1

I⊆[n]

which may be proved by induction on n by using the well-known identity

cos(x + y) = cos(x)cos(y) − sin(x)sin(y). The identity (22) will allow us to compare coefficients of trigonometric polynomials in (20). On the right-hand side in (21) we will find all γ ∈ Zn for which there exist α,β ∈ Nnr , such that γ = α − β. The identity (22) now tells us that we have to make sure that for a given γ ∈ Nnr the following holds

Mα,β for all I ⊂ [n],

##### Mα,β =

α,β∈Nn

α,β∈Nn

r

r

α−β=γ

α−β=ωI(γ)

since then we can factor out the same sum for each ωI(γ) and apply identity (22). Noting that α − β = −(β − α) we can construct symmetric constraint matrices. For each γ ∈ Nnr let C(γ,I) ∈ {0,1}s(n,r)×s(n,r)

1, if α − β = ωI(γ) ∨ ωIc(γ) 0, otherwise.

Cα,β(γ,I) =

These matrices will always be symmetric since if α − β = ωI(γ) then β − α = ωIc(γ). We define I as a set of subsets of [n] such that no complement Ic of a set I ∈ I lies in I and ∪I∈I{I,Ic} = {I : I ⊆ [n]}. With this we can formulate the first set of constraints, i.e.,

⟨M,C(γ,∅)⟩ = ⟨M,C(γ,I)⟩ ∀I ∈ I,∀γ ∈ Nnr . Then gγ = 21⟨M,C(γ,I)⟩ for any I ∈ I. Additionally, we need the following. Let

n

Γ(n,r) = γ ∈ Zn : ∃α,β ∈ Nnr ,α − β = γ ∧

|γi|> r , which leads us to the next set of constraints

i=1

##### ⟨M,C(γ,I)⟩ = 0 ∀I ∈ I,∀γ ∈ Γ(n,r).

This way we ensure that there will not appear any unwanted terms in the resulting polynomial. Any γ ∈ Γ(n,r) will not find the necessary pairs to use identity (22). Therefore, we force all such terms to be zero. We can formulate the SDP now as

n

- 1

- 2⟨M,C(e


i,∅)⟩ (23) subject to

σr2 = min

1 −

i=1

⟨M,C(α,∅) − C(α,I)⟩ = 0 ∀I ∈ I,∀α ∈ Nnr \ {0} ⟨M,C(γ,I)⟩ = 0 ∀I ∈ I,∀γ ∈ Γ(n,r) Tr(M) = 1

M ⪰ 0. Note that Tr(M) = 1 ensures gα = 1 for α = (0,...,0).

### 4 Symmetry reduction

In this section we will present an approach that exploits existing symmetries in semidefinite programs in order to improve numerical tractability. There has been done research on the exploitation of symmetries in semidefinite programming [25]. There are also results available focusing on symmetry exploitation for semidefinite relaxations of polynomial optimization problems. We refer the reader to [12], [21]. The name readily implies that we will use some symmetry to reduce the size of the SDP. The goal is to set up an equivalent SDP, where we can impose a block diagonal structure on the matrix variable. This is helpful because we then only have to enforce the positive semidefiniteness for the individual blocks instead of the whole matrix.

#### 4.1 Symmetry adapted basis

Let Sn be the symmetric group acting on the variables xi for i ∈ [n] by permuting the elements, i.e.,

σ(xi) = xσ(i) for i ∈ [n],σ ∈ Sn.

The action of Sn may be defined on functions as well in the following way. Let f : Rn → R, then

σ(f) = f(σ(x)),

where, if an element σ ∈ Sn is applied to an n-tuple, we define for x ∈ Rn

σ(x) = (σ(x1),σ(x2)...,σ(xn)) = (xσ(1),xσ(2),...,xσ(n)),

i.e., elementwise application. We will call a function f invariant under Sn if σ(f) = f(x) for all σ ∈ Sn. Note that our kernel is defined over the set [−π,π]n, which is invariant under the action of Sn. We can also assume without loss of generality that the optimal kernel Kr will be invariant under the action of Sn, meaning that for all coefficients we will have

gα = gσ(α) for all σ ∈ Sn,α ∈ Nnr ,

To see that the optimal kernel will be invariant under Sn, note that all constraints in problem (20) are invariant under Sn. Thus, any optimal solution to (20) can be ”symmetrized” using the Reynolds-operator, which is defined as

1 |Sn| σ∈S

##### RS

(f,g) :=

σ(f)σ(g).

n

n

Let Kr = α∈Nn

g˜α i∈[n] cosαiϕi be a feasible solution to (20), then

r

 

 

1 |Sn| σ∈S

##### RS

cos(αiϕi)

g˜ασ

(Kr,1) =

n

n α∈Nnr

i∈[n]

is also feasible and will lead to the same objective value. Therefore, we may assume the optimal kernel is invariant under Sn, as well.

We will continue to summarize how to use the symmetry reduction technique described in [21, Section 2.4, 4.1], without dwelling on details unnecessary for our discussion. Therefore, we will not focus on the technicalities of the construction of the symmetry adapted basis, but rather show how it may be used. The idea is as follows. Let T[φ]r = T[φ1,...,φn]r be the set of trigonometric polynomials of degree less that r. We will define T[φ]S

rn to be the set of trigonometric polynomials of degree at most r which are invariant under the action of Sn. A basis for T[φ]r is given by {exp(ıαTϕ)}α∈Nn

. To exploit the symmetry we will construct a new basis B, which we call the symmetry adapted basis. The set B may be seen as a collection of k(n,r) ∈ N sub-bases Bi = {bi

r

j ∈ T[φ]r : for j ∈ [ki]}, for some ki ∈ N in the sense that B = {Bi : i ∈ [k(n,r)]}. In general there are no closed form expressions for k(n,r) and ki available as functions of n and r, but to give some impression of these numbers we provide table 1. We call B a basis because

n

span RS

,b∗i

), i ∈ [k(n,r)], l,m ∈ [ki] = T[φ]S

(bi

r .

n

l

m

The basis B has the property that its elements are pairwise orthogonal in the sense that for bi

m ∈ Bj with i ̸= j the symmetrized product is zero, i.e.,

l ∈ Bi,bj

##### RS

,b∗j

) = 0.

(bi

n

l

m

Before, we were interested in suitable kernels that could be written as

Kr = exp(ıαTϕ) ∗α∈N

M exp(ıαTϕ) α∈N

,

n r

n r

where M ∈ Ss⪰(0n,r). Knowing that the optimal Kr is invariant under Sn, we can write

k(n,r)

i]M(i)[bi,j]j∈[k

Kr =

[bi,j]j∈[k

i]

i=1

for M(i) ⪰ 0 for all i ∈ [k(n,r)]. The pairwise orthogonality of B means that we can consider a block diagonal matrix





M(1) 0 0 ... 0 0 M(2) 0 ... 0 0 0

...

... .

 

 

...

... 0

. .

0 0 ... 0 M(k(n,r))

with M(i) ∈ Sk

⪰0 in our SDP. The computational advantage is that we only have to ensure the positive semidefiniteness of the individual blocks, instead of the much larger matrix M.

i

Example 1. Consider the following example for a symmetry adapted basis with n = 2,r = 2. In this case k(n,r) = k(2,2) = 2 and k1 = 4,k2 = 2. For a corresponding SDP we would have to consider two psd blocks of sizes 4 and 2 instead of one psd matrix of size 6 × 6. For B1,B2 we find

- B1 = {exp(ı(0φ1 + 0φ2)) = 1, exp(ı(φ1 + φ2)), exp(ıφ1) + exp(ıφ2), exp(ı2φ1) + exp(ı2φ2)}
- B2 = {exp(ıφ1) − exp(ıφ2), exp(ı2φ1) − exp(ı2φ2)}.


#### 4.2 Construction of the symmetry adapted SDP

For α ∈ Nnr we define the corresponding orbit as Oα = {σ(α) : σ ∈ Sn}. For each orbit we choose a representative α which is sorted, i.e., α1 ≤ α2 ≤ ... ≤ αn and index the orbit by that α. We define S(Nnr ) = {α ∈ Nnr : α1 ≤ α2 ≤ ... ≤ αn} to be the set of representatives for the set of orbits. The set Nnr can be written as the union of orbits, i.e.,

Nnr =

Oα.

α∈S(Nnr )

The invariance of Kr means that gα = gβ for every β ∈ Oα. We are now equipped to reformulate (20) as an equivalent optimization problem which is easier to solve. We first note that for the invariant kernel we have

 

 .

n

n

2H(α)gα

2H(α)gα

cos(αiφi) =

cos(βiφi)

α∈Nnr

α∈S(Nnr )

i=1

i=1

β∈Oα

For every Bi ∈ B we define a matrix M(i) of size ki ×ki with ki = |Bi|. Then the program may be written as follows.

σr2 = min n(1 − ge

) (24) subject to

n

 

  =

k(n,r)

ki

n

)Mj,ℓ(i)

##### RS

,b∗i

2H(α)gα

cos(βiϕi)

(bi

n

j

ℓ

α∈S(Nnr )

i=1

i=1

β∈Oα

j,ℓ=1

M(i) ⪰ 0, i ∈ [k]. Let us take a closer look at the terms RS

j ∈ Bi are given in the following form

). Assume that the elements bi

,b∗i

(bi

n

l

m

kij

T

b(im)

exp ı α(m)

bi

=

#### ϕ .

j

j

m=1

Then,

1 |Sn| σ∈S

##### ,b∗i

##### RS

##### )σ(b∗i

##### (bi

) =

##### σ(bi

)

n

j

j

ℓ

ℓ

n

kij

kiℓ

∗

T

T

1 |Sn| σ∈S

b(im)

b(ip)

exp ı α(m)

σ(ϕ) + ı β(p)

=

σ(ϕ)

j

ℓ

m=1

p=1

n

kij

kiℓ

1 |Sn| σ∈S

b(im)

b(ip)

##### cos[σ(α(m) − β(p))Tϕ].

=

j

ℓ

m=1

p=1

n

Recalling the trigonometric identity (22) from before, we can now construct the constraint matrices. Let γ ∈ S(Nnr ). For each i ∈ [k(n,r)],I ∈ I for I as in the previous subsection we define

c(γ,I,i,j,ℓ)), if ωI(γ) or ωIc(γ) occurs in RS

##### ,b∗i

) 0, otherwise,

##### (bi

n

Ci(γ,I)

j

=

ℓ

j,ℓ

where

1 |Sn|

b(im)

b(ip)

##### .

c(γ,I,i,j,ℓ)) =

j

ℓ

m,p∈[ki] α(m)−β(p)=±ωI(γ)

As before, we must ensure that for all I ∈ I we have that the corresponding coefficients in our resulting polynomial are equal. Therefore, we arrive at the set of constraints

k(n,r)

⟨M(i),Ci(γ,∅) − Ci(γ,I)⟩ = 0, for every γ ∈ S(Nnr ),I ∈ I,I ̸= ∅.

i=1

We will now define the set SΓ(n,r) = Γ(n,r)/Sn, which is the ”symmetry adapted” version of Γ(n,r) of the previous subsection, where we factored out all permutations σ ∈ Sn of a reference element γ except the identity. This leads to the constraint set

k(n,r)

⟨M(i),Ci(γ,I)⟩ = 0, for every γ ∈ SΓ(n,r),I ∈ I. The resulting SDP reads as follows.

i=1

subject to

 1 −

σr2 = min n

  (25)

k(n,r)

- 1

- 2


⟨M(i),Ci(en,∅)⟩

i=1

k(n,r)

⟨M(i),Ci(γ,∅) − Ci(γ,I)⟩ = 0, for every γ ∈ S(Nnr )/{(0,...,0)},I ∈ I,I ̸= ∅

i=1

k(n,r)

⟨M(i),Ci(γ,I)⟩ = 0, for every γ ∈ SΓ(n,r),I ∈ I

i=1

k(n,r)

⟨M(i),Ci((0,...,0),∅)⟩ = 1 M(i) ⪰ 0 for all i ∈ [k(n,r)].

i=1

The efficiency of using this symmetry reduction increases when n grows, since the underlying group is Sn. Fixing n and increasing the degree r the size of the underlying program still grows fast. It is also possible to use software for the symmetry reduction, such as the Julia package SDPSymmetryReduction.jl3 which is based on the paper [4] by Brosch and de Klerk. This software takes as input a semidefinite program and numerically performs a symmetry

3see https://github.com/DanielBrosch/SDPSymmetryReduction.jl

|n|r| |k(n,r)<br><br>|k1,...,kk(n,r)|s(n,r)|
|---|---|---|---|---|---|


|2<br><br>|1| |2<br><br>|2 , 1 ,|3|
|---|---|---|---|---|---|
|2<br><br>|1| |2<br><br>|2, 1|3|
|2|2| |2<br><br>|4, 2|6|
|2<br><br>|3| |2<br><br>|6, 4|10|
|2<br><br>|4| |2|9, 6<br><br>|15|
|2<br><br>|5| |2<br><br>|12, 9<br><br>|21|
|2<br><br>|6| |2|16, 12<br><br>|28|
|2<br><br>|7| |2<br><br>|20, 16<br><br>|36|
|2<br><br>|8| |2|25, 20|45|
|2|9| |2<br><br>|30, 25|55|
|2|10| |2<br><br>|36, 30<br><br>|66|


|3|1| |2|2, 1|4|
|---|---|---|---|---|---|
|3<br><br>|2| |2<br><br>|4, 3|10|
|3<br><br>|3| |3|7, 6, 1<br><br>|20|
|3|4| |3|11, 11, 2|35|
|3|5| |3<br><br>|16, 18, 4|56|
|3<br><br>|6| |3<br><br>|23, 27, 7|84|
|3<br><br>|7| |3<br><br>|31, 39, 11<br><br>|120|
|3|8| |3|41, 54, 16<br><br>|165|
|3|9| |3|53, 72, 23|220|
|3|10| |3<br><br>|67, 94, 31|286|


|4|1| |2|2, 1<br><br>|5|
|---|---|---|---|---|---|
|4|2| |3<br><br>|4, 3, 1<br><br>|15|
|4|3| |4<br><br>|7, 7, 2, 1|35|
|4<br><br>|4| |4<br><br>|12, 13, 5, 3<br><br>|70|
|4<br><br>|5| |4<br><br>|18, 23, 9, 7<br><br>|126|
|4|6| |5<br><br>|27, 37, 16, 13, 1|210|
|4<br><br>|7| |5<br><br>|38, 57, 25, 23, 2|330|
|4<br><br>|8| |5<br><br>|53, 83, 39, 37, 4|495|
|4|9| |5|71, 118, 56, 57, 7<br><br>|715|
|4|10| |5|94, 162, 80, 83, 12<br><br>|1001|


|5|1| |2|2 , 1 ,|6|
|---|---|---|---|---|---|
|5|2| |3<br><br>|4, 3, 1|21|
|5|3| |4<br><br>|7, 7, 3, 1|56|
|5<br><br>|4| |5<br><br>|12, 14, 7, 3, 1<br><br>|126|
|5<br><br>|5| |5|19, 25, 14, 8, 3|252|
|5|6| |6<br><br>|29, 42, 26, 16, 7, 1|462|
|5<br><br>|7| |6<br><br>|42 , 67, 44, 30, 14, 3<br><br>|792|
|5|8| |6|60, 102, 71, 51, 26, 7<br><br>|1287|
|5|9| |6|83, 150, 109, 83, 44, 14|2002|
|5<br><br>|10| |7|113, 214, 162, 128, 71, 25, 1<br><br>|3003|


Table 1: Comparison for size of SDP (25) and (23) for different values of n and r.

reduction without any need to specify the underlying group. The advantage that comes with this is that there is no need for the construction of a specific symmetry adapted basis. But even for small n, if r becomes too large the resulting optimization problem becomes numerically unstable. It is still worthwhile to compare the two approaches. The block sizes which are returned by the software are the same as the ones we obtained by our approach presented in this section. This suggests that the symmetry is fully exhausted by the symmetric group Sn.

To give some insights into the efficiency of the symmetry reduction, we present in table 1 a comparison of the sizes and numbers of the blocks of the symmetry reduced program vs. the size of the SDP matrix in the case without symmetry reduction, i.e. program (23).

#### Further structure exploitation

We would like to point out that besides symmetry reduction another useful tool for solving large (semidefinite) optimization problems can be sparsity exploitation. In the context of polynomial optimization this topic has been studied before and results are available (cf. [17, 27]). Since our symmetry reduction works well for large n but not necessarily for large r it would be interesting to study sparsity patterns in our context. Our problem after symmetry reduction as given in (25) is not sparse. However, one could enforce certain sparsity patterns on the data matrices while ensuring the problem stays feasible. This could lead to a more tractable optimization problem, whose solution may be less accurate but could still lead to decent approximation results. All theoretical guarantees on the speed of convergence will be lost in this case, though.

### 5 Comparison to products of univariate minimum resolution kernels

In the following we will have a look at what kernels we get when we take the shortcut and multiply univariate kernels instead of solving the corresponding SDP. The clear advantage is that some optimal univariate kernels are available in closed form. Generating kernels as products means solving the corresponding SDP is unnecessary. Recall that in the univariate case kernels of the form

r

KrKPM(x,y) = 1 + 2

g(KPMk,r) Tk(x)Tk(y), (26)

k=1

for gk,rKPM as in (12), have minimum resolution σr. The product of n univariate degree r kernels of the form (26) results in an n-variate kernel of degree nr that is feasible for the optimization problem (25). A natural question is to ask how these kernels compare to the ones obtained by solving the SDP. Consider the product of n degree r kernels

where

n

i=1

r

##### 2H(α)g˜αKPMTα(x)Tα(y),

gk,rKPMTk(xi)Tk(yi) =

1 + 2

α∈Nn

k=1

nr

αi≤r,i∈[n]

n

g˜αKPM =

gαKPM

i,r

i=1

We know the resolution is

n

σr2 =

(1 − ge

) = n(1 − ge

).

i

1

i=1

Thus, we can generate a feasible n-variate kernel with a degree nr multiplying n univariate degree r kernels with minimum resolution and the corresponding resolution is

nπ2 2(r + 2)2

σnr,2 KPM = n 1 − g1KPM,r ≈

.

We would expect these to have a worse resolution than the kernels we obtain via solving the SDP where σr2 is minimized. The reason for this is that the product kernels would be feasible to the same SDP with the additional set of constraints

gα = 0 for all α ∈ Nnnr with αi > r for some i ∈ [n]. In particular, we have the following result. Proposition 2. Fix n ∈ N. For r ≥ n we have

n3π2 2(r + n)2

nπ r + n ∼

σr2 ≤ n 1 − cos

if r ≫ 0.

Proof. Clearly, σr2 ≤ σr2−1 for any r ≥ 1. Let now k ∈ N be such that kn ≤ r ≤ (k + 1)n. Then we find

n3π2 2(r + n)2

π k + 2 ≤ n 1 − cos

π

σr2 ≤ σnk2 ≤ σnk,2 KPM = n 1 − cos

r n + 1 ∼

, for r ≫ 0.

| |
|---|


| | |n = 2<br><br>| |n = 3| |n = 4| |
|---|---|---|---|---|---|---|---|
|r| |σr2|σr,2KPM<br><br>|σr2<br><br>|σr,2KPM|σr2<br><br>|σr,2KPM|


|1| |1.5<br><br>|-<br><br>|2.5|-|3.5<br><br>|-|
|---|---|---|---|---|---|---|---|
|2| |1|1|2<br><br>|-<br><br>|2.9310|-|
|3| |0.7378|-<br><br>|1.5|1.5<br><br>|2.4561<br><br>|-|
|4| |0.5487|0.5858<br><br>|1.1823<br><br>|-|1.9948<br><br>|2|
|5| |0.4260|-|0.9451<br><br>|-|1.6354<br><br>|-|
|6| |0.3395<br><br>|0.3820|0.7764|0.8787<br><br>|1.3605|-|
|7| |0.2774<br><br>|-|0.6474<br><br>|-|1.1518|-|
|8| |0.2299<br><br>|0.2679|0.5461<br><br>|-|0.9901|1.1716|
|9| |0.1939|-<br><br>|0.4692<br><br>|0.5729<br><br>|0.8584|-|
|10| |0.1655|0.1981<br><br>|0.4062<br><br>|-|0.7524|-|
|11| |0.1431<br><br>|-|0.3556<br><br>|-|0.6648<br><br>|-|
|12| |0.1248<br><br>|0.1522|0.3136|0.4019<br><br>|0.5917<br><br>|0.7639|
|13| |0.1099|-<br><br>|0.2787<br><br>|-<br><br>|0.5299|-|
|14| |0.0975<br><br>|0.1206<br><br>|0.2493|-<br><br>|-|-|
|15| |0.0871<br><br>|-<br><br>|0.2243|0.2971|-|-|
|16| |0.0782<br><br>|0.0979<br><br>|0.2028|-|-<br><br>|0.5359|
|17| |0.0706<br><br>|-|0.1843<br><br>|-|-<br><br>|-|
|18| |0.0641<br><br>|0.0810|0.1682|0.2284|-<br><br>|-|
|19| |0.0585<br><br>|-|0.1541|-<br><br>|-|-|
|20| |0.0535|0.0681|0.1417<br><br>|-<br><br>|-|0.3961|
|21| |0.0492<br><br>|-<br><br>|0.1307|0.1809|-<br><br>|-|
|22| |0.0453<br><br>|0.0581|0.1209<br><br>|-|-<br><br>|-|
|23| |0.0419<br><br>|-|-|-<br><br>|-|-|
|24| |0.0389<br><br>|0.0501|-|0.1468<br><br>|-|0.3045|
|25| |0.0362<br><br>|-|-<br><br>|-|-<br><br>|-|
|30| |0.0261|0.0341<br><br>|-<br><br>|0.1022|-<br><br>|-|
|35| |0.0197|-<br><br>|-<br><br>|-<br><br>|-|-|
|40| |0.0154|0.0204<br><br>|-<br><br>|-|-<br><br>|0.1363|
|45| |0.0123<br><br>|-<br><br>|-|0.0511<br><br>|-|-|
|50| |0.0101|0.01352<br><br>|-|-<br><br>|-|-|


Table 2: Computational results for σr2 and σr,2KPM for different values of n and r obtained by solving (25).

Looking at table 2 we find that the values σr,KPM are larger than σr.

Therefore, our generalization of the minimum resolution kernels to the multivariate case leads to better approximations than simply multiplying univariate kernels together. Also, for large n, i.e., the case for which our symmetry reduction is efficient, multiplying identical univariate kernels together is not always a feasible approach as the degree is always a multiple of n. In fig. 2 and fig. 3 we compare the errors of the approximation via the products of Jackson kernels with the approximation via minimum resolution for two different functions.

### 6 Numerical computations

In this section we discuss the numerical computations that were conducted. All code was written in the Julia programming language and is available on GitHub4. At the same website we also list the coefficients of the kernel for various values of n and r. We present some values of σr2 for different values of n and r in table 2. We also compare them to the resolution of the product of identical univariate minimum resolution kernels with the same degree. The results show our method is superior to simple multiplication of identical univariate minimum resolution kernels. In fig. 6 we plotted some of the values of σr for different values of n.

For n = 2 we were able to compute the coefficients for up to r = 50 in a reasonable amount of time (375.5 seconds for σ502 on an Apple M1 Pro with 32GB of RAM). After the symmetry reduction, the corresponding program contains two semidefinite matrix variables of order 676 and 650 and has 1277 constraints. We used the CSDP solver version

4see https://github.com/FelixKirschner/Approximation-Kernels

3

| | | | |
|---|---|---|---|
| | | | |
| | | | |
| | | | |


Error min. res. kernel Error product kernel

Uniformapproximationerror

2.25

1.5

0.75

0

10 20 30 40 50

Approximation degree r

- Figure 2: Comparison of uniform approximation errors of several approximations of the function q(x) := x2 sin(2πx1). We plotted the errors for the kernel with minimal resolution σr and for the product of two univariate degree r/2 kernels, i.e. Kr/KPM2 as in (26).

| | | | |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |


10 20 30 40 50

0

2.5

5

7.5

10

12.5

Approximation degree r

Uniformapproximationerror

Error min. res. kernel Error product kernel

- Figure 3: Comparison of uniform approximation errors of several approximations of the peaks function p(x) :=


##### 3(1 − x1)2 exp(−x21 − (x2 + 1)2) − 10(x1/5 − x31 − x52)exp(−x21 − x22) − (1/3)exp(−(x1 + 1)2 − x22). We plotted the errors for the kernel with minimal resolution σr and for the product of two univariate degree r/2 kernels, i.e. Kr/KPM2 as in (26).

6.2.05 (see [3]) to compute these values. Without the symmetry reduction the program would have one matrix variable of order 522 = 1326. We computed the values of σr for up to r = 22 for n = 3 and r = 13 for n = 4. In the latter case, i.e. n = 4,r = 13, without the symmetry reduction the program contains one matrix of size 2380. Using the symmetry reduction we can reduce the size to five matrices of the orders 194,370,192,218 and 38. For values of n > 2 the limiting factor was time.

#### 6.1 Decoupling the degrees

Taking a look at problem (19) it is clear the value of r on the right-hand-side could be increased to obtain a kernel with potentially smaller resolution. Consider the following problem for fixed r and r′ such that r′ ≥ r.

n

σr,r2 ′ = min

) (27)

(1 − ge

i

gα : α∈Nnr

i=1

subject to

cos(αiϕi) = exp(ıαTϕ) ∗α∈N

2H(α)gα

M exp(ıαTϕ) α∈N

1 +

n r′

n r′

α∈Nnr \{0}

i∈[n]

##### M ⪰ 0.

5available at https://github.com/coin-or/Csdp

- r = 3

- r = 4

- r = 5

- r = 6

- r = 7

- r = 8

- r = 9

- r = 10


0.7

0.6

0.5

0.4

0.3

0.2

0.1

0

0 2 4 6 8 10 12 14 16 18 20

r′

- Figure 4: Plot σr,r2 ′ vs r′ for r = 3,...,10 and r′ = r,r + 1,...,20 and n = 2

0 2 4 6 8 10 12 14 16 18 20 r′

- 0

- 0.5
- 1


- 1.5
- 2


- r = 2

- r = 3

- r = 4

- r = 5

- r = 6

- r = 7

- r = 8

- r = 9

- r = 10


- Figure 5: Plot σr,r2 ′ vs r′ for r = 2,...,10 and r′ = r,r + 1,...,20 and n = 3


For n = 2 (resp. n = 3) we show how the resolution evolves for r = 3,...,10 (resp. r = 2,...,10) and r′ = r,r + 1,...,20 in Figure 4 (resp. fig. 5). We note that the optimal values in the case n = 2 seem to stabilize for

r′ ≥ r + ⌊r−21⌋, whereas such a stabilization pattern may not be observed for n ≥ 3. We leave further investigation in this direction for future research.

### 7 Concluding remarks

We have shown how to construct polynomial approximation kernels with minimal resolution on the hypercube. A major open question is if one may find closed form solutions of the semidefinite programs that yield these kernels.

These type of results are also of independent interest in the study of SDP hierarchies for polynomial optimization on the hypercube, as shown recently by Laurent and Slot [19]. In particular, our kernels may be useful to study hierarchies of the Lasserre-type [16] on the hypercube (see also [7, 8]).

The advantage of our approach over the multiplication of univariate minimum resolution kernels is that it is more efficient (fewer coefficients needed for the same quality approximation), while the clear disadvantage is that we have no closed form solution for the coefficients. Having said that, the tables of coefficients only have to computed once using SDP, and we provide a partial list online6. Moreover, our approach should become more viable in practice as

6Available at https://github.com/FelixKirschner/Approximation-Kernels/tree/master/SigmaKernels

- 0

0.2

0.4

0.6

- 0.8
- 1


1.2

1.4

1.6

- 1.8
- 2


0 2 4 6 8 10 12 14 16 18 20 22 24 26 r

Figure 6: Plot σr2 vs r for n = 1,2,3,4 (⊗,□,△,⋄ resp.)

SDP solvers continue to improve, allowing to compute the coefficients of the kernels in higher dimensions and for larger values of r.

### Acknowledgments

The authors would like to thank Yuan Xu and Simon Foucart for helpful comments on the paper. Also, we want to thank Monique Laurent and Lucas Slot for fruitful discussions on different angles on the subject. Finally, the first author would like to thank Daniel Brosch for helpful discussions about symmetry reduction.

### References

- [1] F. ALTOMARE AND M. CAMPITI, Korovkin-type Approximation Theory and its Applications, De Gruyter, 2011.
- [2] S. BERNSTEIN, Sur l’ordre de la meilleure approximation des fonctions continues par des polynˆomes de degr´e donn´e, M´emoire couronn´e, Brussels, (1912).
- [3] B. BORCHERS, CSDP, A C library for semidefinite programming, Optimization Methods and Software, 11

(1999), pp. 613–623.

- [4] D. BROSCH AND E. DE KLERK, Jordan symmetry reduction for conic optimization over the doubly nonnegative cone: theory and software, Optimization Methods and Software, (2022).
- [5] E. CHRISTOFFEL, Uber¨ die Gaußische Quadratur und eine Verallgemeinerung derselben., 1858 (1858), pp. 61– 82, https://doi.org/doi:10.1515/crll.1858.55.61, https://doi.org/10.1515/crll.1858.55. 61.
- [6] G. DARBOUX, M´emoire sur l’approximation des fonctions de tr`es-grands nombres, et sur une classe etendue´ de d´eveloppements en s´erie., Journal de Math´ematiques Pures et Appliqu´ees, (1878), pp. 5–56, http://eudml. org/doc/235405.
- [7] E. DE KLERK, R. HESS, AND M. LAURENT, Improved convergence rates for Lasserre-type hierarchies of upper bounds for box-constrained polynomial optimization, SIAM Journal on Optimization, 27 (2017), pp. 347–367.
- [8] E. DE KLERK AND M. LAURENT, Error bounds for some semidefinite programming approaches to polynomial minimization on the hypercube, SIAM Journal on Optimization, 20 (2010), pp. 3104–3120.
- [9] G. L. DIRICHLET, Sur la convergence des s´eries trigonom´etriques qui servent a` repr´esenter une fonction arbitraire entre des limites donn´ees., 1829 (1829), pp. 157–169, https://doi.org/doi:10.1515/crll.1829. 4.157, https://doi.org/10.1515/crll.1829.4.157.
- [10] B. DUMITRESCU, Positive Trigonometric Polynomials and Signal Processing Applications, Signals and Communication Technology, Springer, Dordrecht, 2007.


- [11] S. FOUCART AND V. POWERS, Basc: constrained approximation by semidefinite programming, IMA Journal of Numerical Analysis, 37 (2016), pp. 1066–1085.
- [12] K. GATERMANN AND P. A. PARRILO, Symmetry groups, semidefinite programs, and sums of squares, Journal of Pure and Applied Algebra, 192 (2004), pp. 95–128.
- [13] D. GOTTLIEB AND C.-W. SHU, On the Gibbs phenomenon and its resolution, SIAM Review, 39 (1997), pp. 644–668, http://www.jstor.org/stable/2132695 (accessed 2022-08-23).
- [14] D. JACKSON, Uber¨ die Genauigkeit der Ann¨aherung stetiger Funktionen durch ganze rationale Funktionen gegebenen Grades und trigonometrische Summen gegebener Ordnung, Universit¨at G¨ottingen, June 1911.
- [15] D. JACKSON, On approximation by trigonometric sums and polynomials, Transactions of the American Mathematical Society, 13 (1912), pp. 491–515, https://www.jstor.org/stable/1988583.
- [16] J. B. LASSERRE, Global optimization with polynomials and the problem of moments, SIAM Journal on Optimization, 11 (2001), pp. 796–817.
- [17] J. B. LASSERRE, Convergent SDP-relaxations in polynomial optimization with sparsity, SIAM Journal on Optimization, 17 (2006), pp. 822–843, https://doi.org/10.1137/05064504X, https://doi.org/10.1137/ 05064504X, https://arxiv.org/abs/https://doi.org/10.1137/05064504X.
- [18] J. B. LASSERRE, The moment-SOS hierarchy and the Christoffel-Darboux kernel, Optimization Letters, 15

(2021), pp. 1835–1845, https://doi.org/10.1007/s11590-021-01713-4, https://doi.org/10.1007/ s11590-021-01713-4.

- [19] M. LAURENT AND L. SLOT, An effective version of Schm¨udgen’s Positivstellensatz for the hypercube, 2021, https://arxiv.org/abs/2109.09528. arXiv pre-print 2109.09528.
- [20] S. MARX, E. PAUWELS, T. WEISSER, D. HENRION, AND J. B. LASSERRE, Semi-algebraic approximation using Christoffel-Darboux kernel, Constructive Approximation, 54 (2021), pp. 391–429, https://doi.org/ 10.1007/s00365-021-09535-4, https://hal.archives-ouvertes.fr/hal-02085835.
- [21] C. RIENER, T. THEOBALD, L. J. ANDREN´ , AND J. B. LASSERRE, Exploiting symmetries in SDP-relaxations for polynomial optimization, Mathematics of Operations Research, 38 (2013), pp. 122–141.
- [22] T. RIVLIN, An introduction to the approximation of functions, Blaisdell Pub. Co, 1969.
- [23] M. J. TODD, Semidefinite optimization, Acta Numerica, 10 (2001), pp. 515–560.
- [24] L. N. TREFETHEN, Multivariate polynomial approximation in the hypercube, Proceedings of the American mathematical society, 145 (2017), pp. 4837–4844.
- [25] F. VALLENTIN, Symmetry in semidefinite programs, Linear Algebra and its Applications, 430 (2009), pp. 360– 369.
- [26] L. VANDENBERGHE AND S. BOYD, Semidefinite programming, SIAM Review, 38 (1996), pp. 49–95.
- [27] J. WANG, V. MAGRON, AND J.-B. LASSERRE, TSSOS: A moment-SOS hierarchy that exploits term sparsity, SIAM Journal on Optimization, 31 (2021), pp. 30–58, https://doi.org/10.1137/19M1307871, https: //doi.org/10.1137/19M1307871, https://arxiv.org/abs/https://doi.org/10.1137/19M1307871.
- [28] A. WEISSE, G. WELLEIN, A. ALVERMANN, AND H. FEHSKE, The kernel polynomial method, Rev. Mod. Phys., 78 (2006), pp. 275–306, https://doi.org/10.1103/RevModPhys.78.275.


