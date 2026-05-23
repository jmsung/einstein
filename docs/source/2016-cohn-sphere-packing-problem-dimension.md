---
type: source
kind: paper
title: The sphere packing problem in dimension 24
authors: Henry Cohn, Abhinav Kumar, Stephen D. Miller, Danylo Radchenko, Maryna Viazovska
year: 2016
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/1603.06518v3
source_local: ../raw/2016-cohn-sphere-packing-problem-dimension.pdf
topic: general-knowledge
cites:
---

# arXiv:1603.06518v3[math.NT]28Aug2017

Annals of Mathematics 185 (2017), 1017–1033 https://doi.org/10.4007/annals.2017.185.3.8

## The sphere packing problem in dimension 24

By Henry Cohn, Abhinav Kumar, Stephen D. Miller, Danylo Radchenko, and Maryna Viazovska

### Abstract

Building on Viazovska’s recent solution of the sphere packing problem in eight dimensions, we prove that the Leech lattice is the densest packing of congruent spheres in twenty-four dimensions and that it is the unique optimal periodic packing. In particular, we ﬁnd an optimal auxiliary function for the linear programming bounds, which is an analogue of Viazovska’s function for the eight-dimensional case.

### 1. Introduction

The sphere packing problem asks how to arrange congruent balls as densely as possible without overlap between their interiors. The density is the fraction of space covered by the balls, and the problem is to ﬁnd the maximal possible density. This problem plays an important role in geometry, number theory, and information theory. See [5] for background and references on sphere packing and its applications.

Although many interesting constructions are known, provable optimality is very rare. Aside from the trivial case of one dimension, the optimal density was previously known only in two [11], three [7], [8], and eight [12] dimensions, with the latter result being a recent breakthrough due to Viazovska; see [1], [9] for expositions. Building on her work, we solve the sphere packing problem in twenty-four dimensions:

Theorem 1.1. The Leech lattice achieves the optimal sphere packing density in R24, and it is the only periodic packing in R24 with that density, up to scaling and isometries.

Miller’s research was supported by National Science Foundation grants DMS-1500562 and CNS-1526333.

c 2017 by the authors. This paper may be reproduced, in its entirety, for noncommercial purposes.

1017

In particular, the optimal sphere packing density in R24 is that of the Leech lattice, namely

π12 12!

= 0.0019295743... . For an appealing construction of the Leech lattice, see Section 2.8 of [6].

It is unknown in general whether optimal packings have any special structure, but our theorem shows that they do in R24. The optimality and uniqueness of the Leech lattice were previously known only among lattice packings [3], which is a far more restrictive setting. Recall that a lattice is a discrete subgroup of Rn of rank n, and a lattice packing uses spheres centered at the points of a lattice, while a periodic packing is the union of ﬁnitely many translates of a lattice. Lattices are far more algebraically constrained, and it is widely believed that they do not achieve the optimal density in most dimensions. (For example, see [5, p. 140] for an example in R10 of a periodic packing that is denser than any known lattice.) By contrast, periodic packings at least come arbitrarily close to the optimal sphere packing density.

The proof of Theorem 1.1 will be based on the linear programming bounds for sphere packing, as given by the following theorem.

Theorem 1.2 (Cohn and Elkies [2]). Let f : Rn → Rn be a Schwartz function and r a positive real number such that f(0) = f(0) = 1, f(x) ≤ 0 for |x| ≥ r, and f(y) ≥ 0 for all y. Then the sphere packing density in Rn is at most

Å

ãn

πn/2 (n/2)!

r 2

.

Here (n/2)! means Γ(n/2 + 1) when n is odd, and the Fourier transform is normalized by

f(x)e−2πi x,y dx,

f(y) =

Rn

where  ·,·  denotes the usual inner product on Rn. Without loss of generality, we can radially symmetrize f, in which case f is radial as well. We will often tacitly identify radial functions on R24 with functions on [0,∞) and vice versa, by using f(r) with r ∈ [0,∞) to denote the common value f(x) with |x| = r. All Fourier transforms will be in R24 unless otherwise speciﬁed. In other words, if f is a function of one variable deﬁned on [0,∞), then f(r) means

Ä

ä

e−2πi x,y dx, where y ∈ R24 satisﬁes |y| = r.

|x|

f

R24

Optimizing the bound from Theorem 1.1 requires choosing the right auxiliary function f. It was not previously known how to do so except in one dimension [2] or eight [12], but Cohn and Elkies conjectured the existence of

an auxiliary function proving the optimality of the Leech lattice [2]. We prove this conjecture by developing an analogue for the Leech lattice of Viazovska’s construction for the E8 root lattice.

In the case of the Leech lattice, proving optimality amounts to achieving r = 2, which requires that f and f have roots on the spheres of radius

√

2k about the origin for k = 2,3,... . See [2] for further explanation and discussion of this condition. Furthermore, the argument in Section 8 of [2] shows that if f has no other roots at distance 2 or more, then the Leech lattice is the unique optimal periodic packing in R24. Thus, the proof of Theorem 1.1 reduces to constructing such a function.

The existence of an optimal auxiliary function in R24 has long been anticipated, and Cohn and Miller made further conjectures in [4] about special values of the function, which we also prove. Our approach is based on a new connection with quasimodular forms discovered by Viazovska [12], and our proof techniques are analogous to hers. In Sections 2 and 3 we will build two radial Fourier eigenfunctions in R24, one with eigenvalue 1 constructed using a weakly holomorphic quasimodular form of weight −8 and depth 2 for SL2(Z), and one with eigenvalue −1 constructed using a weakly holomorphic modular form of weight −10 for the congruence subgroup Γ(2). We will then take a linear combination of these eigenfunctions in Section 4 to construct the optimal auxiliary function. Throughout the paper, we will make free use of the standard deﬁnitions and notation for modular forms from [12], [13].

### 2. The +1 eigenfunction

We begin by constructing a radial eigenfunction of the Fourier transform in R24 with eigenvalue 1 in terms of the quasimodular form

Ä

ä

Ä

ä

25E44 − 49E62E4

+ 48E6E42E2 +

E22 ∆2

−49E43 + 25E62

ϕ =

- (2.1)


ä

Ä

= −3657830400q − 314573414400q2 − 13716864000000q3 + O

q4

,

where q = e2πiz and the variable z lies in the upper half plane. As mentioned in the introduction, we follow the notation of [12]. In particular, Ek denotes the Eisenstein series

∞

2 ζ(1 − k)

dk−1e2πinz,

Ek(z) = 1 +

n=1 d | n

which is a modular form of weight k for SL2(Z) when k is even and greater than 2 (and a quasimodular form when k = 2). Furthermore, we normalize ∆ by

Ä

ä

E43 − E62 1728

= q − 24q2 + 252q3 + O

q4

. Recall that ∆ vanishes nowhere in the upper half plane.

∆ =

#### This function ϕ is a weakly holomorphic quasimodular form of weight −8 and depth 2 for the full modular group. Speciﬁcally, because

Å

ã

1 z

6i πz

z−2E2

−

= E2(z) −

,

we have the quasimodularity relation

- (2.2) z8ϕ

Å

−

1 z

ã

= ϕ(z) +

ϕ1(z) z

+

ϕ2(z) z2

,

where

ϕ1 = −

6i π

48

E6E42 ∆2 −

12i π

E2

Ä

−49E43 + 25E62 ∆2 ä

=

i π

725760q−1 + 113218560 + 19691320320q + O

Ä

q2

ä

and

ϕ2 = −

36

Ä

−49E43 + 25E62 π2∆2 ä

=

1 π2

864q−2 + 2218752q−1 + 223140096 + 23368117248q + O

Ä

q2

ä

.

It follows from setting z = it in (2.2) that

- (2.3) ϕ(i/t) = O

Ä

t−10e4πt as t → ∞, while the q-series (2.1) for ϕ shows thatä

- (2.4) ϕ(i/t) = O

Ä

e−2π/t as t → 0. We deﬁne ä

- (2.5) a(r) = −4sin


Å

ã

Ä

ä2 i∞

1 z

z10eπir2z dz

πr2/2

−

ϕ

0

for r > 2, which converges absolutely by these bounds.

Lemma 2.1. The function r  → a(r) analytically continues to a holomorphic function on a neighborhood of R. Its restriction to R is a Schwartz function and a radial eigenfunction of the Fourier transform in R24 with eigenvalue 1.

Proof. We follow the approach of [12], adapted to use modular forms of diﬀerent weight. Substituting

Ä

ä2

#### = eπir2 − 2 + e−πir2

πr2/2

−4sin

yields

Å

ã

Å

ã

i∞−1

i∞

1 z + 1

1 z

(z + 1)10eπir2z dz − 2

z10eπir2z dz

−

−

a(r) =

ϕ

ϕ

−1

0

Å

ã

i∞+1

1 z − 1

(z − 1)10eπir2z dz

−

+

ϕ

1

Å

ã

i

1 z + 1

(z + 1)10eπir2z dz

−

=

ϕ

−1

Å

ã

i∞

1 z + 1

(z + 1)10eπir2z dz

−

+

ϕ

i

Å

Å

ã

ã

i∞

i

1 z

1 z

z10eπir2z dz − 2

z10eπir2z dz

−

−

− 2

ϕ

ϕ

0

i

Å

ã

i

1 z − 1

(z − 1)10eπir2z dz

−

ϕ

+

1

Å

ã

i∞

1 z − 1

(z − 1)10eπir2z dz,

−

ϕ

+

i

where we have shifted contours as in the proof of Proposition 2 in [12]. Now the quasimodularity relation (2.2) and periodicity modulo 1 show that

Å

ã

Å

ã

Å

ã

1 z + 1

1 z

1 z − 1

(z + 1)10 − 2ϕ

z10 + ϕ

(z − 1)10

−

−

−

ϕ

= ϕ(z + 1)(z + 1)2 − 2ϕ(z)z2 + ϕ(z − 1)(z − 1)2

- + ϕ1(z + 1)(z + 1) − 2ϕ1(z)z + ϕ1(z − 1)(z − 1)
- + ϕ2(z + 1) − 2ϕ2(z) + ϕ2(z − 1)


= 2ϕ(z). Thus,

ã

Å

i

1 z + 1

(z + 1)10eπir2z dz

−

a(r) =

ϕ

−1

Å

ã

i

1 z − 1

(z − 1)10eπir2z dz

- (2.6)


−

+

ϕ

1

Å

ã

i∞

i

1 z

z10eπir2z dz + 2

ϕ(z)eπir2z dz,

− 2

−

ϕ

0

i

which gives the analytic continuation of a to a neighborhood of R by (2.3) and (2.4). Essentially the same estimates as in Proposition 1 of [12] show that it is a Schwartz function. Speciﬁcally, the exponential decay of ϕ(z) as the imaginary part of z tends to inﬁnity suﬃces to bound all the terms in (2.6), which shows that a and all its derivatives decay exponentially.

Taking the 24-dimensional radial Fourier transform commutes with the integrals in (2.6) and amounts to replacing eπir2z with z−12eπir2(−1/z). Therefore

Å

ã

i

1 z + 1

(z + 1)10z−12eπir2(−1/z) dz

−

a(r) =

ϕ

−1

Å

ã

i

1 z − 1

(z − 1)10z−12eπir2(−1/z) dz

−

+

ϕ

1

ã

Å

i∞

i

1 z

ϕ(z)z−12eπir2(−1/z) dz. Now setting w = −1/z shows that

z−2eπir2(−1/z) dz + 2

− 2

−

ϕ

i

0

Å

ã Å

ã10

i

1 w − 1

1 w

w10eπir2w dw

−1 −

−

a(r) =

ϕ

+ 1

1

Å

ã Å

ã10

i

1 w + 1

1 w − 1

w10eπir2w dw

1 −

−

+

ϕ

−1

Å

ã

i∞

i

1 w

ϕ(w)eπir2w dw − 2

w10eπir2w dw.

−

+ 2

ϕ

i

0

Thus, (2.6) and the fact that ϕ is periodic modulo 1 show that a = a, as desired.

For r > 2, we have

- (2.7) a(r) = 4isin

Ä

πr2/2

ä2 ∞

0

ϕ(i/t)t10e−πr2t dt by (2.5). By the quasimodularity relation (2.2),

- (2.8) t10ϕ(i/t) = t2ϕ(it) − itϕ1(it) − ϕ2(it). Thanks to the q-expansions with q = e−2πt, we have
- (2.9) t10ϕ(i/t) = p(t) + O

Ä

t2e−2πt as t → ∞, where ä p(t) = −

864 π2

e4πt +

725760 π

te2πt −

2218752 π2

e2πt +

113218560 π

t −

223140096 π2

. Let

p(r) =

∞

0

p(t)e−πr2t dt

= −

864 π3(r2 − 4)

+

725760 π3(r2 − 2)2 −

2218752 π3(r2 − 2)

+

113218560 π3r4 −

223140096 π3r2

. Then

- (2.10) a(r) = 4isin


ä2 Å

Ä

Ä

∞

πr2/2

ϕ(i/t)t10 − p(t)

p(r) +

0

ã

ä

e−πr2t dt

#### for r > 2. The integral

Ä

ä

∞

e−πr2t dt

ϕ(i/t)t10 − p(t)

0

is analytic on a neighborhood of [0,∞), and hence (2.10) holds for all r. Note in particular that a maps R to iR by (2.10) (or by (2.5) via analytic continuation).

√ Equation (2.10) implies that a(r) vanishes to second order whenever r =

2k with k > 2, because p has no poles at these points. Furthermore, this formula implies that

and

113218560i π

, a

a(0) =

√

725760i π

,

2 =

= −4437504√2i π

Ä√

ä

a

, a(2) = 0,

2

a (2) = −3456i π

.

The Taylor series expansion is

Ä

ä

113218560i π −

223140096i π

r2 + O

r4

a(r) =

around r = 0.

If we rescale a so that its value at 0 is 1, then the value at √2 becomes 1/156 and the derivative there becomes −107√2/2730, and the derivative at 2 becomes −1/32760. The Taylor series becomes

Ä

ä

3587 1820

r2 + O

r4

1 −

.

However, the higher order terms in this Taylor series do not appear to be rational, because they involve contributions from the integral in (2.10).

We arrived at the deﬁnition (2.1) of ϕ via the Ansatz that ∆2ϕ should be a holomorphic quasimodular form of weight 16 and depth 2 for SL2(Z). The space of such forms is ﬁve-dimensional, spanned by E44, E62E4, E6E42E2, E43E22, and E62E22. Within this space, one can solve for ϕ in several ways. We initially found it by matching the numerical conjectures from [4], but in retrospect one can instead impose constraints on its behavior at 0 and i∞, namely, (2.3) and (2.4). This information is enough to determine ϕ and hence the eigenfunction a, up to a constant factor.

### 3. The −1 eigenfunction

Next we construct a radial eigenfunction of the Fourier transform in R24 with eigenvalue −1. We will use the notation

- Θ00(z) = n∈Z

eπin2z,

- Θ01(z) = n∈Z


(−1)neπin2z, and

eπi(n+1/2)2z

Θ10(z) =

n∈Z

for theta functions from [12]. These functions satisfy the transformation laws

- Θ400|2S = −Θ400, Θ401|2S = −Θ410, Θ410|2S = −Θ401,
- Θ400|2T = Θ401, Θ401|2T = Θ400, Θ410|2T = −Θ410,


Ç

å

Ç

å

- 0 −1
- 1 0


1 1 0 1

where S =

, T =

, and

Å

ã

Ä

ä

az + b cz + d

(z) = (cz + d)−kg

g|kM

Ç

å

a b c d

∈ SL2(R). Let

for a function g on the upper half plane and a matrix M =

7Θ2001Θ810 + 7Θ2401Θ410 + 2Θ2801 ∆2

ψI =

- (3.1)

which is a weakly holomorphic modular form of weight −10 for Γ(2), and let

ψS = ψI|−10S = −

7Θ2010Θ801 + 7Θ2410Θ401 + 2Θ2810 ∆2

= −7340032q1/2 − 918552576q3/2 + O

Ä

q5/2

- (3.2) ä


= 2q−2 − 464q−1 + 172128 − 3670016q1/2 + 47238464q − 459276288q3/2 + O

ä

Ä

q2

,

and

7Θ2000Θ810 − 7Θ2400Θ410 + 2Θ2800 ∆2

ψT = ψI|−10T =

= 2q−2 − 464q−1 + 172128 + 3670016q1/2

Ä

ä

+ 47238464q + 459276288q3/2 + O

q2

. Note that ψS+ψT = ψI, which follows from the Jacobi identity Θ401 + Θ410 = Θ400.

Using these q-expansions, we ﬁnd that

- (3.3) ψI(it) = O

Ä

e4πt as t → ∞, and ä

- (3.4) ψI(it) = O


as t → 0. Let ä b(r) = −4sin

Ä

t10e−π/t

Ä

ä2 i∞

ψI(z)eπir2z dz for r > 2, where the integral converges by the above bounds.

πr2/2

0

Lemma 3.1. The function r  → b(r) analytically continues to a holomorphic function on a neighborhood of R. Its restriction to R is a Schwartz function and a radial eigenfunction of the Fourier transform in R24 with eigenvalue −1.

Proof. As in the proof of Proposition 6 from [12], we substitute

Ä

ä2

= e−πir2 − 2 + eπir2 and shift contours to show that for r > 2,

πr2/2

−4sin

i∞

i∞−1

ψI(z + 1)eπir2z dz − 2

ψI(z)eπir2z dz

b(r) =

−1

0

i∞+1

ψI(z − 1)eπir2z dz

+

1

i

i

i

ψT(z)eπir2z dz +

ψT(z)eπir2z dz − 2

ψI(z)eπir2z dz

=

−1

1

0

Ä

ä

i∞

eπir2z dz.

ψT(z) − ψI(z)

+ 2

i

Here, we have used ψI(z + 1) = ψI(z − 1) = ψT(z), and we have shifted the endpoints from i∞ ± 1 to i∞ (which is justiﬁed because the inequality r > 2 ensures that the integrand decays exponentially). Finally, applying ψT − ψI = −ψS yields

i

i

i

ψT(z)eπir2z dz +

ψT(z)eπir2z dz − 2

ψI(z)eπir2z dz

b(r) =

−1

1

0

i∞

ψS(z)eπir2z dz,

− 2

i

which yields the analytic continuation to r ≤ 2, and essentially the same estimates prove that it is a Schwartz function.

To show that the 24-dimensional radial Fourier transform b satisﬁes b = −b, we follow the approach of Proposition 5 from [12]. As in the proof of Lemma 2.1,

i

i

ψT(z)z−12eπir2(−1/z) dz +

ψT(z)z−12eπir2(−1/z) dz

b(r) =

−1

1

i∞

i

ψS(z)z−12eπir2(−1/z) dz, and the change of variables w = −1/z yields

ψI(z)z−12eπir2(−1/z) dz − 2

− 2

0

i

Å

ã

Å

ã

i

i

1 w

1 w

w10eπir2w dw +

w10eπir2w dw

−

−

b(r) =

ψT

ψT

−1

1

Å

Å

ã

ã

i∞

i

1 w

1 w

w10eπir2w dw. Finally, b = −b follows from the equations

w10eπir2w dw + 2

−

−

ψS

ψI

+ 2

0

i

ψI|−10S = ψS, ψS|−10S = ψI, and ψT|−10S = −ψT,

where the ﬁrst two equations amount to the deﬁnition of ψS and the third follows from ψS + ψT = ψI.

For r > 2, we have

Ä

ä2 ∞

ψI(it)e−πr2t dt. From the q-expansion, we have

πr2/2

- (3.5) b(r) = −4isin


0

e−πt as t → ∞, and ä

Ä

ψI(it) = 2e4πt − 464e2πt + 172128 + O

Ä

ä

∞

2 π(r2 − 4) −

464 π(r2 − 2)

172128 πr2

e−πr2t dt =

2e4πt − 464e2πt + 172128

. Thus, for all r ≥ 0,

+

- 0


Ç

ä2

Ä

2 π(r2 − 4) −

464 π(r2 − 2)

172128 πr2

πr2/2

b(r) = −4isin

+

å

Ä

ä

∞

e−πr2t dt

ψI(it) − 2e4πt + 464e2πt − 172128

, by analytic continuation.

+

0

√

This formula implies that b(r) vanishes to second order whenever r =

2k with k > 2. Furthermore, it implies that

Ä√

ä

= b(2) = 0, b

b(0) = b

2

ä

Ä√

√

2, and

2

= 928iπ

b (2) = −8πi.

The Taylor series expansion is b(r) = −172128πir2 + O

r4 around r = 0, and b maps R to iR. ä

Ä

To obtain the deﬁnition (3.1) of ψI, we began with the Ansatz that ∆2ψI should be a holomorphic modular form of weight 14 for Γ(2). The space of such forms is eight-dimensional, spanned by Θ401iΘ2810−4i with i = 0,1,...,7, and the subspace of forms satisfying the linear constraint ψS + ψT = ψI is three-dimensional. As in the case of ϕ in Section 2, one can solve for ψI in several ways. In particular, within the subspace satisfying ψS + ψT = ψI, the asymptotic behavior speciﬁed by (3.3) and (3.4) determines ψI up to a constant factor.

### 4. Proof of Theorem 1.1

We can now construct the optimal auxiliary function for use in Theorem 1.2. Let

i 262080π

πi 113218560

a(r) −

f(r) = −

b(r).

Then f(0) = f(0) = 1, and the quadratic Taylor coeﬃcients of f and f are −14347/5460 and −205/156, respectively, as conjectured in [4]. The functions f and f have roots at all of the vector lengths in the Leech lattice, i.e.,

√

2k for k = 2,3,... . These roots are double roots except for the root of f at 2, where f (2) = −1/16380 (in accordance with Lemma 5.1 in [4]). Furthermore, f has the value 1/156 and derivative −146√2/4095 at √2, while f has the value 1/156 and derivative −5√2/117 there.

We must still check that f satisﬁes the hypotheses of Theorem 1.2. We will do so using the approach of [12], with one extra complication at the end.

For r > 2, equations (2.7) and (3.5) imply that f(r) = sin

Ä

ä2 ∞

A(t)e−πr2t dt, where

πr2/2

0

π 28304640

1 65520π

t10ϕ(i/t) −

A(t) =

ψI(it)

π 28304640

1 65520π

t10ψS(i/t). To show that f(r) ≤ 0 for r ≥ 2 with equality only at r of the form

t10ϕ(i/t) +

=

√

2k with k = 2,3,..., it suﬃces to show that A(t) ≤ 0. Speciﬁcally, A cannot be identically zero since then f would vanish as well; given that A is continuous, nonpositive everywhere, and negative somewhere, it follows that

∞

A(t)e−πr2t dt < 0 for all r for which it converges (i.e., r > 2).

0

Because

Å

ã

π 28304640

432 π2

t10

A(t) =

, showing that A(t) ≤ 0 amounts to showing that

ϕ(i/t) +

ψS(i/t)

- (4.1) ϕ(it) +

432 π2

ψS(it) ≤ 0. The formula

ψS = −

7Θ2010Θ801 + 7Θ2410Θ401 + 2Θ2810 ∆2

immediately implies that ψS(it) ≤ 0, and so to prove (4.1) it suﬃces to prove that ϕ(it) ≤ 0. We prove this inequality in Lemma A.1 by bounding the truncation error in the q-series and examining the leading terms (splitting into the cases t ≥ 1 and t ≤ 1). It follows that f(r) ≤ 0 for r ≥ 2, as desired.

For r > 2, the analogous formula for f is

- (4.2) f(r) = sin

Ä

πr2/2

ä2 ∞

0

B(t)e−πr2t dt, where

B(t) =

π 28304640

t10ϕ(i/t) +

1 65520π

ψI(it)

=

π 28304640

t10ϕ(i/t) −

1 65520π

t10ψS(i/t).

- (4.3)

To show that f(r) ≥ 0 for r > 2, it suﬃces to show that B(t) ≥ 0 for all t ≥ 0, i.e.,

- (4.4) ϕ(it) −


432 π2

ψS(it) ≥ 0, for the same reason as we saw above with A(t). This inequality is Lemma A.2.

The formula (4.2) in fact holds for r > √2, not just r > 2. To see why, we must examine the asymptotics of B(t). There is no problem with the integral in (4.2) as t → 0, because B(t) vanishes in this limit by (2.4) and (3.4). However, the exponential growth of B(t) as t → ∞ causes divergence when r is too small for e−πr2t to counteract this growth. To estimate the growth rate, note that by

- (2.9) and (3.1), the e4πt terms cancel in the asymptotic expansion of B(t) as


ä

Ä

te2πt

t → ∞, which means that B(t) = O

. Thus, the formula (4.2) for f(r) converges when r > √2, and it must equal f(r) by analytic continuation. Note that it cannot hold for the whole interval (0,∞), because that would force f to vanish at √2, which does not happen.

Thus, (4.2) and the inequality B(t) ≥ 0 in fact prove that f ≥ 0 for all r ≥

√2. When 0 < r < √2, this inequality no longer implies that f(r) ≥ 0,

which is a complication that does not occur in [12]. Instead, we must analyze B(t) more carefully. As t → ∞, equations (2.9) and (3.1) show that

1 39

10 117π

te2πt −

e2πt + O(t).

B(t) =

We will ameliorate this behavior by subtracting these terms over the interval [1,∞). They contribute

Å

ã

(10 − 3π)(2 − r2) + 3 117π2(r2 − 2)2

∞

1 39

10 117π

e−π(r2−2),

e−πr2t dt =

te2πt −

e2πt

1

which is nonnegative for 0 < r < √2, and the remaining terms

ã

Å

∞

1

10 117π

1 39

e−πr2t dt

B(t)e−πr2t dt +

te2πt +

e2πt

B(t) −

0

1

converge for all r > 0. The integrand B(t) in the ﬁrst integral is nonnegative, and thus to prove that f(r) ≥ 0 for 0 < r < √2 it suﬃces to prove that

10 117π

1 39

e2πt for t ≥ 1, which is Lemma A.3.

te2πt −

- (4.5) B(t) ≥


Combining the results of this section shows that f satisﬁes the hypotheses of Theorem 1.2, and thus that the Leech lattice is an optimal sphere packing in R24. Furthermore, f has no roots r > 2 other than r =

√

2k with k = 2,3,..., and as in Section 8 of [2] this condition implies that the Leech lattice is the unique densest periodic packing in R24. This completes the proof of Theorem 1.1.

### Appendix A. Inequalities for quasimodular forms

The proof in Section 4 requires checking certain inequalities for quasimodular forms on the imaginary axis. Fortunately, these inequalities are not too delicate, because equality is never attained. The behavior at inﬁnity is easily analyzed, which reduces the proof to verifying the inequalities on a compact interval, and that can be done by a ﬁnite calculation.

Thus, these inequalities are clearly provable if true. The proof of the analogous inequalities in [12] used interval arithmetic, but in this appendix we take a diﬀerent approach, based on applying Sturm’s theorem to truncated q-series. We have documented the calculations carefully, to facilitate checking the proof. Computer code for verifying our calculations is contained in the ancillary ﬁle appendix.txt. The code can be obtained at https://doi.org/10. 4007/annals.2017.185.3.8, as well as at the arXiv.org e-print archive, where this paper is available as arXiv 1603.06518. Our code is for the free computer algebra system PARI/GP (see [10]), but the calculations are simple enough that they are not diﬃcult to check in any computer algebra system.

To prove each inequality, we approximate the modular form using q-series and prove error bounds for truncating the series, which we then incorporate by adding them to an appropriate term of the truncated series. The result is nearly a polynomial in q, with the possible exceptions being factors of t (where z = it), and we bound those factors so as to reduce to the case of a polynomial in q. Furthermore, we bound any factors of π so that the coeﬃcients become rational. Finally, we use Sturm’s theorem with exact rational arithmetic to verify that the truncated series never changes sign.

To prove the error bounds, we need to control the growth of the coeﬃcients. We ﬁrst multiply by ∆2 to clear the denominators that appear in (2.1),

- (3.1), and (3.2). The advantage of doing so is that the coeﬃcients of the numerator grow only polynomially. To estimate the growth rate, we bound the coeﬃcient of qn in E2 by 24(n+1)2 in absolute value, in E4 by 240(n+1)4, and in E6 by 504(n+1)6. It is also not diﬃcult to show that the coeﬃcient of qn/2 in Θ400, Θ401 or Θ410 is at most 24(n + 1)2 in absolute value.1 Multiplying series


Äis straightforward: if |an| ≤ (n+1) and |bn| ≤ (n+1)m, then the coeﬃcients of n anqn

ä

äÄ

are bounded by (n+1) +m+1. When we add two q-series with coeﬃcients bounded by diﬀerent powers of n+1, we typically produce an upper bound by rounding up the lower power for simplicity. Using these techniques leads to explicit polynomial bounds for the coeﬃcients of ϕ∆2, ψI∆2, and ψS∆2 by using their deﬁnitions in terms of Eisenstein series and theta functions. These bounds are ineﬃcient, but they suﬃce for our purposes.

n bnqn

When t ≥ 1, q = e−2πt is small enough that these coeﬃcient bounds yield a reasonable error term. When t ≤ 1, we replace it with 1/t (via z  → −1/z) and compute the corresponding q-expansion.

Lemma A.1. For t > 0,

ϕ(it) < 0. Proof. First, we prove this inequality for t ≥ 1, in which case q = e−2πt <

- 1/535. The bounds described above show that the coeﬃcient of qn in ϕ∆2 is at most 513200655360(n + 1)20 in absolute value, and exact computation shows that ∞


513200655360(n + 1)20 535n−6 < 10−50.

n=50

Thus, the sum of the absolute values of the terms in ϕ∆2 for n ≥ 50 amounts to at most 10−50q6. Let σ be the sum of the terms with n < 50. We use Sturm’s theorem to check that σ + 10−50q6 never changes sign on (0,1/535)

1Both Θ400 and Θ410 have nonnegative coeﬃcients, and their sum is the theta series of the D4 root lattice in the variable q1/2, from which one can bound their coeﬃcients. Furthermore, Θ401 = Θ400 − Θ410.

as a polynomial in q, and we observe that it is negative in the limit as q → 0. This proves that ϕ(it) < 0 for t ≥ 1.

Using (2.8), the bound for t ≤ 1 is equivalent to showing that −t2ϕ(it) + itϕ1(it) + ϕ2(it) > 0

for t ≥ 1. Again we multiply by ∆2 to control the coeﬃcients. This case is more complicated, because there are factors of t and π. We replace factors of π with rational bounds, namely 1010π /1010 or 1010π /1010 based on the sign of the term and whether it is a positive power of π (so that we obtain a lower bound), and we similarly use the bounds 1 ≤ t ≤ 1/

Ä

ä

23q1/2

; the latter bound follows from q = e−2πt and te−πt ≤ e−π ≤ 1/23. To estimate the error bound from truncation, we use q1/2 < 1/23; the result is that the error from omitting the qn terms with n ≥ 50 is at most 10−50q6. These observations reduce the problem to showing that a polynomial in q1/2 with rational coeﬃcients is positive over the interval (0,e−π). Using Sturm’s theorem, we check that it holds over the larger interval (0,1/23).

Note that we could have avoided fractional powers of q in this proof if we had used a diﬀerent upper bound for t, but fractional powers will be needed to handle ψS and ψI in any case. We will use the bounds such as 1 ≤ t ≤ 1/

Ä

ä

23q1/2

from the preceding proof systematically in the remaining proofs. Lemma A.2. For t > 0,

432 π2

ϕ(it) −

ψS(it) > 0.

Proof. We use exactly the same technique as in the proof of Lemma A.1. For t≥1, removing the q50 and higher terms in the q-series for

Ä

ä

∆2 introduces an error of at most 10−50q6, and Sturm’s theorem shows that the resulting polynomial has no sign changes. Note that ψS involves powers of q1/2, and so we must view the truncated series as a polynomial in q1/2 rather than q.

ϕ−432ψS/π2

For t ≤ 1, we apply relations (2.2) and (3.2) to reduce the problem to showing that

432 π2

−t2ϕ(it) + itϕ1(it) + ϕ2(it) −

ψI(it) < 0

for t ≥ 1. When we multiply by ∆2 and remove the q50 and higher terms, the error bound is at most 10−50q6, and Sturm’s theorem completes the proof. As in the previous proof, this case involves handling factors of t and π, but they present no diﬃculties.

Of course these proofs are by no means optimized. Instead, they were chosen to be straightforward and easy to describe.

The ﬁnal inequality we must verify is (4.5): Lemma A.3. For all t ≥ 1,

1 39

10 117π

e2πt. Proof. As usual, we multiply

te2πt −

B(t) >

Å

ã

1 39

10 117π

te2πt −

e2πt

B(t) −

by ∆2 and compute its q-series. Our usual truncation bounds show that removing the q50 and higher terms introduces an error bound of at most 10−50q6, and Sturm’s theorem again completes the proof.

### References

- [1] H. Cohn, A conceptual breakthrough in sphere packing, Notices Amer. Math. Soc. 64 (2017), 102–115. arXiv 1611.01685. https://doi.org/10.1090/noti1474.
- [2] H. Cohn and N. Elkies, New upper bounds on sphere packings. I, Ann. of Math. 157 (2003), 689–714. MR 1973059. Zbl 1041.52011. arXiv math/0110009. https://doi.org/10.4007/annals.2003.157.689.
- [3] H. Cohn and A. Kumar, Optimality and uniqueness of the Leech lattice among lattices, Ann. of Math. 170 (2009), 1003–1050. MR 2600869. Zbl 1213.11144. arXiv math.MG/0403263. https://doi.org/10.4007/annals.2009.170.1003.
- [4] H. Cohn and S. D. Miller, Some properties of optimal functions for sphere packing in dimensions 8 and 24, preprint, 2016. arXiv 1603.04759.
- [5] J. H. Conway and N. J. A. Sloane, Sphere Packings, Lattices and Groups, third ed., Grundl. Math. Wissen. 290, Springer-Verlag, New York, 1999. MR 1662447. Zbl 0915.52003. https://doi.org/10.1007/978-1-4757-6568-7.
- [6] W. Ebeling, Lattices and Codes, A course partially based on lectures by Friedrich Hirzebruch, third ed., Adv. Lect. Math., Springer-Verlag, New York,

2013. MR 2977354. Zbl 1257.11066. https://doi.org/10.1007/978-3-658-00360-9.

- [7] T. C. Hales, A proof of the Kepler conjecture, Ann. of Math. 162 (2005), 1065–1185. MR 2179728. Zbl 1096.52010. https://doi.org/10.4007/annals.2005. 162.1065.
- [8] T. Hales, M. Adams, G. Bauer, D. T. Dang, J. Harrison, T. L. Hoang, C. Kaliszyk, V. Magron, S. McLaughlin, T. T. Nguyen, T. Q. Nguyen, T. Nipkow, S. Obua, J. Pleso, J. Rute, A. Solovyev, A. H. T. Ta, T. N. Tran, D. T. Trieu, J. Urban, K. K. Vu, and R. Zumkeller, A formal proof of the Kepler conjecture, to appear in Forum of Mathematics, Pi. arXiv 1501. 02155.
- [9] D. de Laat and F. Vallentin, A breakthrough in sphere packing: the search for magic functions, Nieuw Arch. Wiskd. 17 (2016), 184–192. arXiv 1607.02111.
- [10] The PARI Group, PARI/GP version 2.9.1, 2016, Univ. Bordeaux. Available at http://pari.math.u-bordeaux.fr/.


- [11] A. Thue, Om nogle geometrisk-taltheoretiske Theoremer, Forhandlingerne ved de Skandinaviske Naturforskeres 14 (1892), 352–353. Zbl 24.0259.01.
- [12] M. S. Viazovska, The sphere packing problem in dimension 8, Ann. of Math. 185 (2017), 991–1015. arXiv 1603.04246. https://doi.org/10.4007/annals.2017. 185.3.7.
- [13] D. Zagier, Elliptic modular forms and their applications, in The 1-2-3 of Modular Forms, Universitext, Springer-Verlag, New York, 2008, pp. 1–103. MR 2409678. Zbl 1259.11042. https://doi.org/10.1007/978-3-540-74119-0 1.


#### (Received: May 23, 2016)

Microsoft Research New England, Cambridge, MA E-mail : cohn@microsoft.com

Stony Brook University, Stony Brook, NY E-mail : thenav@gmail.com

Rutgers University, Piscataway, NJ E-mail : miller@math.rutgers.edu

Max Planck Institute for Mathematics, Bonn, Germany Current address : The Abdus Salam International Centre for Theoretical Physics, Trieste, Italy E-mail : danradchenko@gmail.com

Berlin Mathematical School and Humboldt University of Berlin, Berlin, Germany Current address : Ecole´ Polytechnique Fed´ erale´ de Lausanne, Lausanne, Switzerland E-mail : viazovska@gmail.com

