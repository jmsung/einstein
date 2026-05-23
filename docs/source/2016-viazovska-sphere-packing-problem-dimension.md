---
type: source
kind: paper
title: The sphere packing problem in dimension 8
authors: Maryna Viazovska
year: 2016
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/1603.04246v2
source_local: ../raw/2016-viazovska-sphere-packing-problem-dimension.pdf
topic: general-knowledge
cites:
---

arXiv:1603.04246v2[math.NT]4Apr2017

# The sphere packing problem in dimension 8

### Maryna S. Viazovska April 5, 2017

In this paper we prove that no packing of unit balls in Euclidean space R8 has density greater than that of the E8-lattice packing.

Keywords: Sphere packing, Modular forms, Fourier analysis AMS subject classiﬁcation: 52C17, 11F03, 11F30

## 1 Introduction

The sphere packing constant measures which portion of d-dimensional Euclidean space can be covered by non-overlapping unit balls. More precisely, let Rd be the Euclidean vector space equipped with distance · and Lebesgue measure Vol(·). For x ∈ Rd and r ∈ R>0 we denote by Bd(x,r) the open ball in Rd with center x and radius r. Let X ⊂ Rd be a discrete set of points such that x−y ≥ 2 for any distinct x,y ∈ X. Then the union

P =

Bd(x,1)

x∈X

is a sphere packing. If X is a lattice in Rd then we say that P is a lattice sphere packing. The ﬁnite density of a packing P is deﬁned as

Vol(P ∩ Bd(0,r)) Vol(Bd(0,r))

∆P(r) :=

, r > 0.

We deﬁne the density of a packing P as the limit superior ∆P := limsup

∆P(r).

r→∞

The number be want to know is the supremum over all possible packing densities ∆d := sup

∆P,

P⊂Rd sphere packing

called the sphere packing constant.

For which dimensions do we know the exact value of ∆d? Trivially, in dimension 1 we have ∆1 = 1. It has long been known that a best packing in dimension 2 is the familiar hexagonal lattice packing, in which each disk is touching six others. The ﬁrst proof of this result was given by A. Thue at the beginning ot twentieth century [18]. However, his proof was considered by some experts incomplete. A rigorous proof was given by L. Fejes T´th in 1940s [10]. The density of the hexagonal lattice packing

is √π12, therefore ∆2 = √π12 ≈ 0.90690. The packing problem in dimension 3 turned out to be more diﬃcult. Johannes Kepler conjectured in his essay “On the six-cornered

snowﬂake” (1611) that no arrangement of equally sized spheres ﬁlling space has density greater than √π18. This density is attained by the face-centered cubic packing and also by uncountably many non-lattice packings. The Kepler conjecture was famously proven by T. Hales in 1998 [11] and therefore we know that ∆3 = √π18 ≈ 0.74048. In 2015 Hales and his 21 coauthors published a complete formal proof of the Kepler conjecture that can be veriﬁed by automated proof checking software. Before now, the exact values of the sphere packing constants in all dimensions greater than 3 have been unknown. A list of conjectural best packings in dimensions less than 10 can be found in [6]. Upper bounds for the sphere packing constants ∆d as d ≤ 36 are given in [4]. Surprisingly enough, these upper bounds and known lower bounds on ∆d are extremely close in dimensions d = 8 and d = 24.

The main result of this paper is the proof that

π4 384 ≈ 0.25367.

∆8 =

This is the density of the E8-lattice sphere packing. Recall that the E8-lattice Λ8 ⊂ R8 is given by

8

Λ8 = {(xi) ∈ Z8 ∪ (Z + 12)8|

xi ≡ 0 (mod 2)}.

i=1

Λ8 is the unique up to isometry positive-deﬁnite, even, unimodular lattice of rank 8. The name derives from the fact that it is the root lattice of the E8 root system. The minimal distance between two points in Λ8 is √2. The E8-lattice sphere packing is the packing of unit balls with centers at √12Λ8. Our main result is

Theorem 1. No packing of unit balls in Euclidean space R8 has density greater than that of the E8-lattice packing.

Furthermore, our proof of Theorem 1 combined with arguments given in [4, Section 8] implies that the E8-lattice sphere packing is the unique periodic packing of maximal density.

The paper is organized as follows. In Section 2 we explain the idea of the proof of

- Theorem 1 and describe the methods we use. In Section 3 we give a brief overview of the theory of modular forms. In Section 4 we construct supplementary radial functions a, b : R8 → iR, which are eigenfunctions of the Fourier transform and have double zeroes at


almost all points of Λ8. This construction is crucial for our proof of Theorem 1. Finally, in Section 5 we complete the proof.

## 2 Linear programming bounds

Our proof of Theorem 1 is based on linear programming bounds. This technique was successfully applied to obtain upper bounds in a wide range of discrete optimization problems such as error-correcting codes [7], equal weight quadrature formulas [8], and spherical codes [13, 16]. In exceptional cases linear programming bounds are optimal [5]. However, in general linear programming bounds are not sharp and it is an open question how big the errors of such bounds can be. It is known [2] that the linear programming bounds for the minimal number of points in an equal weight quadrature formula on the sphere Sd are asymptotically optimal up to a constant depending on d. Linear programming bounds can also be applied to the sphere packing problem. Kabatiansky and Levenshtein [13] deduced upper bounds for sphere packing from their results on spherical codes.

In 2003 Cohn and Elkies [4] developed linear programming bounds that apply directly to sphere packings. Using their new method they improved the previously known upper bounds for the sphere packing constant in dimensions from 4 to 36. The most striking results obtained by this technique are upper bounds for dimensions 8 and 24. For example, their upper bound for ∆8 was only 1.000001 times greater than the lower bound, which is given by the density of the E8 sphere packing. This bound can be improved even further by more extensive computer computations.

We explain the Cohn–Elkies linear programming bounds in more detail. To this end we recall a few deﬁnitions from Fourier analysis. The Fourier transform of an L1 function f : Rd → C is deﬁned as

F(f)(y) = f(y) :=

Rd

f(x)e−2πix·y dx, y ∈ Rd

where x · y = 12 x 2 + 21 y 2 − 21 x − y 2 is the standard scalar product in Rd. A C∞ function f : Rd → C is called a Schwartz function if it tends to zero as x → ∞

faster then any inverse power of x , and the same holds for all partial derivatives of f. The set of all Schwartz functions is called the Schwartz space. The Fourier transform is an automorphism of this space. We will also need the following wider class of functions. We say that a function f : Rd → C is admissible if there is a constant δ > 0 such that |f(x)| and | f(x)| are bounded above by a constant times (1 + |x|)−d−δ. The following theorem is the key result of [4]:

- Theorem 2. (Cohn, Elkies [4]) Suppose that f : Rd → R is an admissible function, is not identically zero, and satisﬁes:


f(x) ≤ 0 for x ≥ 1 (1)

and

f(x) ≥ 0 for all x ∈ Rd. (2) Then the density of d-dimensional sphere packings is bounded above by

f(0) f(0)

·

πd2 2d Γ(d2 + 1)

f(0) f(0)

- 1

- 2


· VolBd(0,

=

).

Without loss of generality we can assume that a function f in Theorem 2 is radial, i. e. its value at each point depends only on the distance between the point and the origin [4, p. 695]. For a radial function f0 : Rd → R we will denote by f0(r) the common value of f0 on vectors of length r. Henceforth we assume d = 8. The Poisson summation formula implies

f( ) = 24

f( ).

√2Λ8

∈√12Λ8

∈

Hence, if a function f satisﬁes conditions (1) and (2) then

f(0) f(0)

≥ 24.

We say that an admissible function f : R8 → R is optimal if it satisﬁes (1), (2) and f(0)/ f(0) = 24.

The main step in our proof of Theorem 1 is the explicit construction of an optimal function. It will be convenient for us to scale this function by √2.

- Theorem 3. There exists a radial Schwartz function g : R8 → R which satisﬁes:


√

g(x) ≤ 0 for x ≥

2, (3) g(x) ≥ 0 for all x ∈ R8, (4) g(0) = g(0) = 1. (5)

Moreover, the values g(x) and g(x) do not vanish for all vectors x with x 2 ∈/ 2Z>0.

Theorem 2 applied to the optimal function f(x) = g(√2x) immediately implies Theorem 1. Additionally, the function g satisﬁes the conclusions of [4, Conjecture 8.1]. This implies the uniqueness of the densest periodic sphere packing in R8.

Let us brieﬂy explain our strategy for the proof of Theorem 3. First, we observe that conditions (3)–(5) imply additional properties of the function g. Suppose that there exists a Schwartz function g such that the conditions (3)–(5) hold. The Poisson summation formula states

g( ) =

g( ). (6)

∈Λ8

∈Λ8

√2 for all ∈ Λ8\{0}, conditions (3) and (5) imply

Since ≥

g( ) ≤ g(0) = 1. (7)

∈Λ8

On the other hand, conditions (4) and (5) imply

g( ) ≥ g(0) = 1. (8)

∈Λ8

Therefore, we deduce that g( ) = g( ) = 0 for all ∈ Λ8\{0}. Moreover, the ﬁrst derivatives drd g(r) and drd g(r) also vanish at all Λ8-lattice points of length bigger than √2. We will say that g and g have double zeroes at these points. This property gives us a hint on constructing the function g explicitly.

In Section 5 a function g satisfying (3)–(5) is given in a closed form. Namely, it is deﬁned as an integral transform (Laplace transform) of a modular form of a certain kind. The next section is a brief introduction to the theory of modular forms.

## 3 Modular forms

Let H be the upper half-plane {z ∈ C | Im(z) > 0}. The modular group Γ(1) := PSL2(Z) acts on H by linear fractional transformations

az + b cz + d

a b c d z :=

.

Let N be a positive integer. The level N principal congruence subgroup of Γ(1) is

Γ(N) := ac db ∈ Γ(1) ac db ≡ (10 01) mod N .

A subgroup Γ ⊂ Γ(1) is called a congruence subgroup if Γ(N) ⊂ Γ for some N ∈ N. An important example of a congruence subgroup is

Γ0(N) := ac db ∈ Γ(1) c ≡ 0 mod N .

Let z ∈ H, k ∈ Z, and ac db ∈ SL2(Z). The automorphy factor of weight k is deﬁned as

jk(z, ac db ) := (cz + d)−k. The automorphy factor satisﬁes the chain rule

jk(z,γ1γ2) = jk(z,γ2)jk(γ2z,γ1). Let F be a function on H and γ ∈ PSL2(Z). Then the slash operator acts on F by

(F|kγ)(z) := jk(z,γ)F(γz). The chain rule implies

F|kγ1γ2 = (F|kγ1)|kγ2.

A (holomorphic) modular form of integer weight k and congruence subgroup Γ is a holomorphic function f : H → C such that:

- 1. f|kγ = f for all γ ∈ Γ and
- 2. for each α ∈ Γ(1) the function f|kα has Fourier expansion


∞

n nα

n

)e2πi

nα z

f|kα(z) =

cf(α,

n=0

for some nα ∈ N and Fourier coeﬃcients cf(α,m) ∈ C.

Let Mk(Γ) be the space of modular forms of weight k for the congruence subgroup Γ. A key fact in the theory of modular forms is that the spaces Mk(Γ) are ﬁnite dimensional.

We consider several examples of modular forms. For an even integer k ≥ 4 we deﬁne the weight k Eisenstein series as

- 1

- 2ζ(k) (c,d)∈Z2\(0,0)


(cz + d)−k. (9)

Ek(z) :=

Since the sum converges absolutely, it is easy to see that Ek ∈ Mk(Γ(1)). The Eisenstein series possesses the Fourier expansion

2 ζ(1 − k)

Ek(z) = 1 +

∞

σk−1(n)e2πinz, (10)

n=1

where σk−1(n) = d|n dk−1. In particular, we have

∞

σ3(n)e2πinz,

E4(z) =1 + 240

n=1

∞

σ5(n)e2πinz.

E6(z) =1 − 504

n=1

The inﬁnite sum (9) does not converge absolutely for k = 2. On the other hand, the expression (10) converges to a holomorphic function on the upper half-plane and therefore we set

∞

σ1(n)e2πinz. (11)

E2(z) := 1 − 24

n=1

This function is not modular, but it satisﬁes

z−2 E2 −1 z

6i π

= E2(z) −

1 z

. (12)

The proof of this identity can be found in [20, Section 2.3]. The weight two Eisenstein series E2 is an example of a quasimodular form [20, Section 5.1].

Another example of modular forms we consider are theta functions [20, Section 3.1]. We deﬁne three theta functions (so-called “Thetanullwerte”) as

- θ00(z) = n∈Z

eπin2z,

- θ01(z) = n∈Z


(−1)n eπin2z,

eπi(n+21)2z.

θ10(z) =

n∈Z

The group Γ(1) is generated by the elements T = (10 11) and S = − 01 10 . These elements act on the fourth powers of the theta functions in the following way

z−2 θ004 −1

= − θ004 (z), (13) z−2 θ014 −1

z

= − θ104 (z), (14) z−2 θ104 −1

z

= − θ014 (z), (15) and

z

θ004 (z + 1) =θ014 (z), (16) θ014 (z + 1) =θ004 (z), (17) θ104 (z + 1) = − θ104 (z). (18)

Moreover, these three theta functions satisfy the Jacobi identity

θ014 + θ104 = θ004 . (19) The theta functions θ004 ,θ014 , and θ104 belong to M2(Γ(2)).

A weakly-holomorphic modular form of integer weight k and congruence subgroup Γ is a holomorphic function f : H → C such that:

- 1. f|kγ = f for all γ ∈ Γ,
- 2. for each α ∈ Γ(1) the function f|kα has Fourier expansion


∞

n nα

n

nα z

)e2πi

f|kα(z) =

cf(α,

n=n0

for some n0 ∈ Z and nα ∈ N.

For an m-periodic holomorphic function f and n ∈ m1 Z we will denote the n-th Fourier coeﬃcient of f by cf(n) so that

##### cf(n)e2πinz.

f(z) =

n∈m1 Z

We denote the space of weakly-holomorphic modular forms of weight k and group Γ by Mk!(Γ). The spaces Mk!(Γ) are inﬁnite dimensional. Probably the most famous weaklyholomorphic modular form is the elliptic j-invariant

1728E43 E43 − E62

.

j :=

This function belongs to M0!(Γ(1)) and has the Fourier expansion j(z) = q−1 + 744 + 196884q + 21493760q2 + 864299970q3 + 20245856256q4 + O(q5)

where q = e2πiz. Using a simple computer algebra system such as PARI GP or Mathematica one can compute the ﬁrst hundred terms of this Fourier expansion within a few seconds. An important question is to ﬁnd an asymptotic formula for cj(n), the n-th Fourier coeﬃcient of j. Using the Hardy-Ramanujan circle method [17, p. 460 – 461] or the non-holomorphic Poincar´e series [15] one can show that

∞

2π √n

Ak(n) k

cj(n) =

I1

k=1

4π√n k

n ∈ Z>0 (20)

where

e−2kπi(nh+h ), hh ≡ −1(mod k),

Ak(n) =

h mod k (h,k)=1

and Iα(x) denotes the modiﬁed Bessel function of the ﬁrst kind deﬁned as in [1, Section 9.6]. A similar convergent asymptotic expansion holds for the Fourier coeﬃcients of any weakly holomorphic modular form [12, p.660 – 662], [3, Propositions 1.10 and 1.12]. Such a convergent expansion implies eﬀective estimates for the Fourier coeﬃcients.

For a comprehensive introduction to the theory of modular forms we refer the reader to [20] and [9].

## 4 Fourier eigenfunctions with double zeroes at lattice points

In this section we construct two radial Schwartz functions a,b : R8 → iR such that

- F(a) = a (21)
- F(b) = −b (22)


which double zeroes at all Λ8-vectors of length greater than √2. Recall that each vector of Λ8 has length √2n for some n ∈ N≥0. We deﬁne a and b so that their values are purely imaginary because this simpliﬁes some of our computations. We will show in Section 5 that an appropriate linear combination of functions a and b satisﬁes conditions (3)–(5).

First, we will deﬁne the function a. To this end we consider the following weakly holomorphic modular forms:

ϕ−2 := −1728E4 E6 E43 − E62

, (23)

1728E42 E43 − E62

ϕ−4 :=

. (24)

The modular form E43 − E62 does not vanish in the upper half-plain, hence ϕ−2 and ϕ−4 have no poles in H. Analogously to (20), the Fourier coeﬃcients of ϕ−2 and ϕ−4 satisfy

4π√n k

∞

Ak(n) k

cϕκ(n) = 2π nκ−21

n ∈ Z>0, κ = −2,−4. (25)

I1−κ

k=1

We deﬁne

φ−4 :=ϕ−4, (26) φ−2 :=ϕ−4 E2 + ϕ−2, (27)

φ0 :=ϕ−4 E22 + 2ϕ−2 E2 + j − 1728. (28)

The function φ0(z) is not modular; however the identity (12) implies the following transformation rule:

φ0 −1 z

12i π

1 z

36 π2

1 z2

= φ0(z) −

φ−2(z) −

φ−4(z). (29) Moreover, we have

φ−2 = − 3D(ϕ−4) + 3ϕ−2, (30) φ0 =12D2(ϕ−4) − 36D(ϕ−2) + 24j − 17856, (31)

where Df(z) = 21πi dzd f(z). These identities combined with (20) and (25) give the asymptotic formula for the Fourier coeﬃcients cφ−4(n), cφ−2(n), and cφ0(n). The ﬁrst several terms of the corresponding Fourier expansions are

φ−4(z) =q−1 + 504 + 73764q + 2695040q2 + 54755730q3 + O(q4), (32) φ−2(z) =720 + 203040q + 9417600q2 + 223473600q3 + 3566782080q4 + O(q5), (33)

φ0(z) =518400q + 31104000q2 + 870912000q3 + 15697152000q4 + O(q5), (34) where q = e2πiz. For x ∈ R8 we deﬁne

i

a(x) :=

- −1

φ0 −1 z + 1

(z + 1)2 eπi x 2z dz +

i

1

φ0 −1 z − 1

(z − 1)2 eπi x 2z dz (35)

- −2


0

i

φ0 −1 z

z2 eπi x 2z dz + 2

i

i∞

φ0(z)eπi x 2z dz.

We observe that the contour integrals in (35) converge absolutely and uniformly for x ∈ R8. Indeed, φ0(z) = O(e−2πiz) as Im(z) → ∞. Therefore, a(x) is well deﬁned. Now we prove that a satisﬁes condition (21).

- Proposition 1. The function a deﬁned by (35) belongs to the Schwartz space and satisﬁes


a(x) = a(x).

Proof. First, we prove that a is a Schwartz function. From (20), (25), and (31) we deduce that the Fourier coeﬃcients of φ0 satisfy

√n n ∈ Z>0. Thus, there exists a positive constant C such that

|cφ0(n)| ≤ 2e4π

- 1

- 2


|φ0(z)| ≤ C e−2πImz for Imz >

.

We estimate the ﬁrst summand in the right-hand side of (35). For r ∈ R≥0 we have

−1/(i+1)

i

φ0 −1 z + 1

(z + 1)2 eπir2z dz =

φ0(z)z−4 eπir2(−1/z−1) dz ≤

−1

i∞

∞

∞

√

e−2πt e−πr2/t dt ≤ C1

e−2πt e−πr2/t dt = C2 r K1(2

C1

2π r)

0

1/2

where C1 and C2 are some positive constants and Kα(x) is the modiﬁed Bessel function of the second kind deﬁned as in [1, Section 9.6]. This estimate also holds for the second and third summand in (35). For the last summand we have

i∞

φ0(z)eπir2z dz ≤ C

i

∞

eπ(r2+2) r2 + 2

e−2πt e−πr2t dt = C3

.

1

Therefore, we arrive at

√

|a(r)| ≤ 4C2 r K1(2

e−π(r2+2) r2 + 2

2πr) + 2C3

.

It is easy to see that the left hand side of this inequality decays faster then any inverse power of r. Analogous estimates can be obtained for all derivatives drdkka(r).

Now we show that a is an eigenfunction of the Fourier transform. We recall that the Fourier transform of a Gaussian function is

F(eπi x 2z)(y) = z−4 eπi y 2 (−z1). (36)

Next, we exchange the contour integration with respect to z variable and Fourier transform with respect to x variable in (35). This can be done, since the corresponding double integral converges absolutely. In this way we obtain

a(y) =

i

- −1

φ0 −1 z + 1

(z + 1)2 z−4 eπi y 2 (−z1) dz +

i

1

φ0 −1 z − 1

(z − 1)2 z−4 eπi y 2 (−z1) dz

- −2


0

i

φ0 −1 z

z2 z−4 eπi y 2 (−z1) dz + 2

i

i∞

φ0(z)z−4 eπi y 2 (−z1) dz.

Now we make a change of variables w = −z1. We obtain

a(y) =

1

+

i

1 w − 1

φ0 1 −

i

(−1 w

+ 1)2 w2 eπi y 2 w dw

- −1

φ0 1 −

1 w + 1

(−1 w − 1)2 w2 eπi y 2 w dw

- −2


i

φ0(w)eπi y 2 w dw + 2

i∞

i

Since φ0 is 1-periodic we have

0

φ0 −1 w

w2 eπi y 2 w dw.

i

φ0 −1 z − 1

(z − 1)2 eπi y 2 z dz +

a(y) =

1

i∞

i

φ0 −1 z

φ0(z)eπi y 2 z dz − 2

+2

0

i

=a(y). This ﬁnishes the proof of the proposition.

i

φ0 −1 z + 1

−1

(z + 1)2 eπi y 2 z dz

z2 eπi y 2 z dz

| |
|---|


√2.Next, we check that a has double zeroes at all Λ8-lattice points of length greater then

- Proposition 2. For r > √2 we can express a(r) in the following form


a(r) = −4sin(πr2/2)2

i∞

φ0 −1 z

0

z2 eπir2 z dz. (37)

Proof. We denote the right hand side of (37) by d(r). It is easy to see that d(r) is welldeﬁned. Indeed, from the transformation formula (29) and the expansions (34)–(32) we obtain

φ0 −1 it

=O(e−2π/t) as t → 0

φ0 −1 it

=O(t−2 e2πt) as t → ∞

Hence, the integral (37) converges absolutely for r > √2. We can write

i∞−1

φ0 −1 z + 1

d(r) =

−1

i∞+1

φ0 −1 z − 1

+

1

(z + 1)2 eπir2 z dz − 2

0

i∞

φ0 −1 z

(z − 1)2 eπir2 z dz.

z2 eπir2 z dz

From (29) we deduce that if r > √2 then φ0 −z1 z2 eπir2 z → 0 as Im(z) → ∞. Therefore, we can deform the paths of integration and rewrite

d(r) =

−1

−2

0

+

1

i

φ0 −1 z + 1

(z + 1)2 eπir2 z dz +

i

i∞

i

φ0 −1 z

φ0 −1 z

z2 eπir2 z dz − 2

i

i

φ0 −1 z − 1

(z − 1)2 eπir2 z dz +

i

i∞

φ0 −1 z + 1

(z + 1)2 eπir2 z dz

z2 eπir2 z dz

i∞

φ0 −1 z − 1

(z − 1)2 eπir2 z dz.

Now from (29) we ﬁnd

φ0 −1 z + 1

(z + 1)2 − 2φ0 −1 z

z2 + φ0 −1 z − 1

(z − 1)2 = φ0(z + 1)(z + 1)2 − 2φ0(z)z2 + φ0(z − 1)(z − 1)2

12i π

−

φ−2(z + 1)(z + 1) − 2φ−2(z)z + φ−2(z − 1)(z − 1) −

36 π2

φ−4(z + 1) − 2φ−4(z) + φ−4(z − 1) = 2φ0(z).

Thus, we obtain

i

φ0 −1 z + 1

d(r) =

−1

i

φ0 −1 z − 1

+

1

(z + 1)2 eπir2 z dz − 2

0

(z − 1)2 eπir2 z dz + 2

i

i

φ0 −1 z

z2 eπir2 z dz

i∞

φ0(z)eπir2 z dz = a(r).

This ﬁnishes the proof.

| |
|---|


Finally, we ﬁnd another convenient integral representation for a and compute values of a(r) at r = 0 and r = √2.

#### Proposition 3. For r ≥ 0 we have

a(r) =4i sin(πr2/2)2

+

∞

0

t2 φ0

i t −

8640 π3 r4

36 π3 (r2 − 2) −

+

36 π2

8640 π

18144 π2

e2πt +

t −

The integral converges absolutely for all r ∈ R≥0. Proof. Suppose that r > √2. Then by Proposition 2

18144 π3 r2

e−πr2t dt .

a(r) = 4i sin(πr2/2)2

∞

φ0(i/t)t2 e−πr2t dt.

0

(38)

From (34)–(29) we obtain

φ0(i/t)t2 =

For r > √2 we have

36 π2

8640 π

e2πt −

18144 π2

+ O(t2 e−2πt) as t → ∞. (39)

t +

∞

36 π2

8640 π

18144 π2

36 π3 (r2 − 2) −

8640 π3 r4

18144 π3 r2

e−πr2t dt =

e2πt +

t +

+

. (40)

0

Therefore, the identity (38) holds for r > √2.

On the other hand, from the deﬁnition (35) we see that a(r) is analytic in some neighborhood of [0,∞). The asymptotic expansion (39) implies that the right hand side of (38) is also analytic in some neighborhood of [0,∞). Hence, the identity (38) holds on the whole interval [0,∞). This ﬁnishes the proof of the proposition.

| |
|---|


From the identity (38) we see that the values a(r) are in iR for all r ∈ R≥0. In particular, we have

#### Proposition 4. We have

a(0) = −i8640 π

√

a(

√

2) = 0 a (

i72√2 π

2) =

. (41)

Proof. These identities follow immediately from the previous proposition. Now we construct function b. To this end we consider the modular form h := 128

| |
|---|


θ004 + θ014 θ108

. (42)

It is easy to see that h ∈ M−! 2(Γ0(2)). Indeed, ﬁrst we check that h|−2γ = h for all γ ∈ Γ0(2). Since the group Γ0(2) is generated by elements (12 01) and (10 11) it suﬃces to check that h is invariant under their action. This follows immediately from (13)–(18) and (42). Next we analyze the poles of h. It is known [14, Chapter I Lemma 4.1] that θ10 has no zeros in the upper-half plane and hence h has poles only at the cusps. At the cusp i∞ this modular form has the Fourier expansion

h(z) = q−1 + 16 − 132q + 640q2 − 2550q3 + O(q4).

Let I = (10 01), T = (10 11), and S = 01 −01 be elements of Γ(1). We deﬁne the following three functions

More explicitly, we have

ψI :=h − h|−2ST, (43) ψT :=ψI|−2T, (44) ψS :=ψI|−2S. (45)

θ004 + θ014 θ108

θ014 − θ104 θ008

ψI =128

+ 128

θ004 + θ104 θ018

θ004 + θ014 θ108

+ 128

ψT =128

θ004 + θ104 θ018 − 128

ψS = − 128

The Fourier expansions of these functions are

, (46)

, (47)

θ104 − θ014 θ008

. (48)

ψI(z) =q−1 + 144 − 5120q1/2 + 70524q − 626688q3/2 + 4265600q2 + O(q5/2), (49) ψT(z) =q−1 + 144 + 5120q1/2 + 70524q + 626688q3/2 + 4265600q2 + O(q5/2), (50) ψS(z) = − 10240q1/2 − 1253376q3/2 − 48328704q5/2 − 1059078144q7/2 + O(q9/2). (51)

For x ∈ R8 deﬁne

b(x) :=

i

- −1

ψT(z)eπi x 2z dz +

i

1

ψT(z)eπi x 2z dz (52)

- −2


0

i

ψI(z)eπi x 2z dz − 2

i∞

ψS(z)eπi x 2z dz.

i

Now we prove that b satisﬁes condition (22).

- Proposition 5. The function b deﬁned by (52) belongs to the Schwartz space and satisﬁes


b(x) = −b(x).

Proof. Here, we repeat the arguments used in the proof of Proposition 1. First we show that b is a Schwartz function. We have

i

ψT(z)eπir2z dz =

i+1

ψI(z)eπir2(z−1) dz =

−1

−1/(i+1)

ψI −1 z

i∞

0

eπir2(−1/z−1) z−2 dz =

−1/(i+1)

ψS(z)z−4 eπir2(−1/z−1) dz.

i∞

There exists a positive constant C such that

- 1

- 2


|ψS(z)| ≤ C e−πImz for Imz >

.

Thus, as in the proof of Proposition 1 we estimate the ﬁrst summand in the left-hand side of (52)

i

ψT(z)eπir2z dz ≤ C1 r K1(2πr).

−1

We combine this inequality with analogous estimates for the other three summands and obtain

e−π(r2+1) r2 + 1

|b(r)| ≤ C2 r K1(2πr) + C3

.

Here C1, C2, and C3 are some positive constants. Similar estimates hold for all derivatives ddkkrb(r).

Now we prove that b is an eigenfunction of the Fourier transform. We use identity (36) and interchange contour integration in z and Fourier transform in x. Thus we obtain

i

F(b)(x) =

- −1

ψT(z)z−4 eπi x 2(−z1) dz +

i

1

ψT(z)z−4 eπi x 2(−z1) dz

- −2


i

ψI(z)z−4 eπi x 2(−z1) dz − 2

0

i∞

ψS(z)z−4 eπi x 2(−z1) dz.

i

We make the change of variables w = −z1 and arrive at

i

i

ψT −1 w

ψT −1 w

w2 eπi x 2w dw +

F(b)(x) =

−1

1

i

0

ψI −1 w

w2 eπi x 2w dw − 2

−2

i∞

i

Now we observe that the deﬁnitions (43)–(45) imply

w2 eπi x 2w dw

ψS −1 w

w2 eπi x 2w dw.

ψT|−2S = − ψT, ψI|−2S =ψS, ψS|−2S =ψI.

Therefore, we arrive at

F(b)(x) =

1

+2

Now from (52) we see that

i

i

−ψT(z)eπi x 2z dz +

−1

i∞

ψS(z)eπi x 2z dz + 2

i

−ψT(z)eπi x 2z dz

i

ψI(z)eπi x 2w dw.

0

F(b)(x) = −b(x).

| |
|---|


Now we regard the radial function b as a function on R≥0. We check that b has double roots at Λ8-points.

- Proposition 6. For r > √2 function b(r) can be expressed as


b(r) = −4sin(πr2/2)2

i∞

ψI(z)eπir2 z dz. (53)

0

Proof. We denote the right hand side of (53) by c(r). First, we check that c(r) is well-deﬁned. We have

ψI(it) = O(t2 e−π/t) as t → 0, ψI(it) = O(e2πt) as t → ∞.

Therefore, the integral (53) converges for r > √2. Then we rewrite it in the following way:

i∞−1

i∞

i∞+1

ψI(z + 1)eπir2 z dz − 2

ψI(z)eπir2 z dz +

ψI(z − 1)eπir2 z dz.

c(r) =

−1

0

1

From the Fourier expansion (49) we know that ψI(z) = e−2πiz + O(1) as Im(z) → ∞. By assumption r2 > 2, hence we can deform the path of integration and write

We have

i∞−1

ψI(z + 1)eπir2 z dz =

−1

−1

i∞+1

ψI(z − 1)eπir2 z dz =

−1

1

i

ψT(z)eπir2 z dz +

i

i

ψT(z)eπir2 z dz +

i

i∞

ψT(z)eπir2 z dz, (54)

i∞

ψT(z)eπir2 z dz. (55)

c(r) =

−1

i

i

ψT(z)eπir2 z dz +

ψT(z)eπir2 z dz − 2

1

0

i∞

(ψT(z) − ψI(z))eπir2 z dz.

+ 2

i

i

ψI(z)eπir2 z dz (56)

Next, we check that the functions ψI,ψT, and ψS satisfy the following identity:

ψT + ψS = ψI. (57) Indeed, from deﬁnitions (43)-(45) we get

ψT + ψS =(h − h|−2ST)|−2T + (h − h|−2ST)|−2S =h|−2T − h|−2ST2 + h|−2S − h|−2STS.

Note that ST2S belongs to Γ0(2). Thus, since h ∈ M−! 2Γ0(2) we get ψT + ψS = h|−2T − h|−2STS. Now we observe that T and STS(ST)−1 are also in Γ0(2). Therefore, ψT + ψS = h|−2T − h|−2STS = h − h|−2ST = ψI.

Combining (56) and (57) we ﬁnd

c(r) =

i

ψT(z)eπir2 z dz +

i

−1

1

i∞

ψS(z)eπir2 z dz

− 2

i

=b(r).

ψT(z)eπir2 z dz − 2

0

i

ψI(z)eπir2 z dz

| |
|---|


At the end of this section we ﬁnd another integral representation of b(r) for r ∈ R≥0 and compute special values of b.

#### Proposition 7. For r ≥ 0 we have

  144

 . (58)

∞

1 π (r2 − 2)

ψI(it) − 144 − e2πt e−πr2t dt

b(r) = 4i sin(πr2/2)2

+

+

π r2

0

The integral converges absolutely for all r ∈ R≥0. Proof. The proof is analogous to the proof of Proposition 3. First, suppose that r > √2. Then by Proposition 6

b(r) = 4i sin(πr2/2)2

∞

ψI(it)e−πr2t dt.

0

From (49) we obtain

ψI(it) = e2πt + 144 + O(e−πt) as t → ∞. (59) For r > √2 we have

∞

1 π (r2 − 2)

144 π r2

e2πt + 144 e−πr2t dt =

+

. (60)

0

Therefore, the identity (38) holds for r > √2.

On the other hand, from the deﬁnition (52) we see that b(r) is analytic in some neighborhood of [0,∞). The asymptotic expansion (59) implies that the right hand side of (58) is also analytic in some neighborhood of [0,∞). Hence, the identity (58) holds on the whole interval [0,∞). This ﬁnishes the proof of the proposition.

| |
|---|


We see from (58) that b(r) ∈ iR far all r ∈ R≥0. Another immediate corollary of this proposition is

#### Proposition 8. We have

b(0) = 0 b(

√

√

2) = 0 b (

√

2) = 2

2π i. (61)

## 5 Proof of Theorem 3

Finally, we are ready to prove Theorem 3. Theorem 4. The function

π i 8640

i 240π

g(x) :=

a(x) +

b(x)

satisﬁes conditions (3)–(5). Moreover, the values g(x) and g(x) do not vanish for all vectors x with x 2 ∈/ 2Z>0. Proof. First, we prove that (3) holds. By Propositions 2 and 6 we know that for r > √2

π 2160

sin(πr2/2)2

g(r) =

∞

A(t)e−πr2t dt (62)

0

where

36 π2

A(t) = −t2φ0(i/t) −

ψI(it).

Our goal is to show that A(t) < 0 for t ∈ (0,∞). The function A(t) is plotted in Figure 1.

- Figure 1: Plot of the functions A(t), A(2)0 (t) = −368640π2 t2 e−π/t, and A(1)∞ (t) = −π722 e2πt + 8640


π t − 23328π2 .

| | |
|---|---|
| |A t<br><br>A0 2 t<br><br>A 1 t<br><br>1<br>2 1 32<br><br><br>|


t

8000

16000

We observe that we can compute the values of A(t) for t ∈ (0,∞) with any given precision. Indeed, from identities (29) and (45) we obtain the following two presentations for A(t)

36 π2

A(t) = − t2φ0(i/t) +

t2 ψS(i/t), A(t) = − t2φ0(it) +

36 π2

12 π

tφ−2(it) −

φ−4(it) −

36 π2

ψI(it).

For an integer n ≥ 0 let A(0n) and A∞(n) be the functions such that

A(t) =A(0n)(t) + O(t2 e−πn/t) as t → 0, (63) A(t) =A(∞n)(t) + O(t2 e−πnt) as t → ∞. (64)

For each n ≥ 0 we can compute these functions from the Fourier expansions (34)–(32),

(49), and (51). For example, from (32)–(34) and (49) we compute

- A(6)∞ (t) =−


72 π2

+t(

23328 π2

184320 π2

5194368 π2

22560768 π2

250583040 π2

e−πt−

e−2πt+

e−3πt−

e−4πt+

e2πt−

+

8640 π +

2436480 π e−2πt+

113011200 π e−4πt)−t2(518400 e−2πt+31104000 e−4πt).

869916672 π2

e−5πt

##### From (32)–(34) and (51) we compute

- A(6)0 (t) = t2(−368640π2 e−π/t−518400e−2π/t−45121536π2 e−3π/t−31104000e−4π/t−1739833344π2 e−5π/t).


Moreover, from the convergent asymptotic expansion for the Fourier coeﬃcients of a weakly holomorphic modular form [3, Proposition 1.12] we ﬁnd that the n-th Fourier coeﬃcient cψI(n) of ψI satisﬁes

√n n ∈ 12Z>0. (65) Similar inequalities hold for the Fourier coeﬃcients of ψS, φ0, φ−2, and φ−4:

|cψI(n)| ≤ e4π

√n n ∈ 12Z>0, (66) |cφ0(n)| ≤ 2e4π

|cψS(n)| ≤ 2e4π

- √n n ∈ Z>0, (67)

|cφ−2(n)| ≤ e4π

- √n n ∈ Z>0, (68)


√n n ∈ Z>0. (69)

|cφ−4(n)| ≤ e4π

Therefore, we can estimate the error terms in the asymptotic expansions (63) and (64) of A(t)

36 π2

A(t) − A(0m)(t) ≤(t2 +

12 π

A(t) − A(∞m)(t) ≤(t2 +

For an integer m ≥ 0 we set

∞

36 π2

R0(m) :=(t2 +

)

n=m

12 π

36 π2

R∞(m) :=(t2 +

t +

∞

√2π√n e−πn/t,

2e2

)

n=m

∞

√2π√n e−πnt.

36 π2

2e2

t +

)

n=m

√2π√n e−πn/t,

2e2

∞

√2π√n e−πnt.

2e2

)

n=m

Using interval arithmetic we check that R0(6)(t) ≤ A(6)0 (t) for t ∈ (0,1], R∞(6)(t) ≤ A(6)∞ (t) for t ∈ [1,∞),

A(6)0 (t) < 0 for t ∈ (0,1], A(6)∞ (t) < 0 for t ∈ [1,∞).

Thus, we see that A(t) < 0 for t ∈ (0,∞). Then identity (62) implies (3). Next, we prove (4). By Propositions 3 and 7 we know that for r > 0

π 2160

sin(πr2/2)2

g(r) =

∞

B(t)e−πr2t dt (70)

0

where

36 π2

B(t) = −t2φ0(i/t) +

ψI(it). This function can also be written as

36 π2

B(t) = − t2φ0(i/t) −

t2 ψS(i/t), B(t) = − t2φ0(it) +

12 π

36 π2

36 π2

tφ−2(it) −

ψI(it). Our aim is to prove that B(t) > 0 for t ∈ (0,∞). A plot of B(t) is given in Figure 2.

φ−4(it) +

- Figure 2: Plot of the functions B(t), B0(2)(t) = 368640π2 t2 e−π/t, and B∞(1)(t) = 8640π t−23328π2 .


| |B t<br><br>B0 2 t<br><br>B 1 t<br><br>|
|---|---|
| |1<br>2 1 32 2<br><br><br>|


4000

2000

t

For n ≥ 0 let B0(n) and B∞(n) be the functions such that

B(t) =B0(n)(t) + O(t2 e−πn/t) as t → 0, B(t) =B∞(n)(t) + O(t2 e−πnt) as t → ∞.

We ﬁnd

- B∞(6)(t) = − 12960π2 − 184320π2 e−πt − 116640π2 e−2πt − 22560768π2 e−3πt + 56540160π2 e−4πt − 869916672π2 e−5πt


+ t(8640π + 2436480π e−2πt + 113011200π e−4πt) − t2(518400e−2πt +31104000e−4πt) and

- B0(6)(t) = t2(368640π2 e−π/t−518400e−2π/t+45121536π2 e−3π/t−31104000e−4π/t+1739833344π2 e−5π/t). The estimates (65)–(69) imply that


B(t) − B0(6)(t) ≤ R0(6)(t) for t ∈ (0,1] and

B(t) − B∞(6)(t) ≤ R∞(6)(t) for t ∈ [1,∞).

Using interval arithmetic we verify that R0(6)(t) ≤ B0(6)(t) for t ∈ (0,1], R∞(6)(t) ≤ B∞(6)(t) for t ∈ [1,∞),

B0(6)(t) > 0 for t ∈ (0,1], B∞(6)(t) > 0 for t ∈ [1,∞).

Now identity (70) implies (4).

Finally, the property (5) readily follows from Proposition 4 and Proposition 8. This ﬁnishes the proof of Theorems 4 and 3.

| |
|---|


## Acknowledgments

I thank Andriy Bondarenko for sharing his ideas, for fruitful discussions, and for his support. Also I am grateful to Danilo Radchenko for his valuable ideas and his help with numerical computations. I am most grateful to J. Kramer, J. M. Sullivan, G. M. Ziegler , and anonymous referees for their valuable comments and suggestions on the manuscript.

## References

- [1] M. Abramowitz, I. Stegun, Handbook of Mathematical Functions with Formulas, Graphs, and Mathematical Tables, Applied Mathematics Series 55 (10th ed.), New York, USA: United States Department of Commerce, National Bureau of Standards; Dover Publications, 1964.
- [2] A. Bondarenko, D. Radchenko, M. Viazovska, On optimal asymptotic bounds for spherical designs, Annals of Math. 178 (2)(2013), pp. 443–452.


- [3] J. Bruinier, Borcherds products on O(2,l) and Chern classes of Heegner divisors, Springer Lecture Notes in Mathematics 1780 (2002).
- [4] H. Cohn, N. Elkies, New upper bounds on sphere packings I, Annals of Math. 157 (2003) pp. 689–714.
- [5] H. Cohn, A. Kumar, Universally optimal distribution of points on spheres, J. Amer. Math. Soc. 20 (1) (2007), pp. 99–148.
- [6] J. H. Conway and N. J. A. Sloane, What Are All the Best Sphere Packings in Low Dimensions?, Discrete Comput. Geom. (L´szl´ Fejes T´th Festschrift), 13

(1995), pp. 383–403.

- [7] P. Delsarte, Bounds for unrestricted codes, by linear programming, Philips Res. Rep. 27 (1972), pp. 272–289.
- [8] P. Delsarte, J. M. Goethals, and J. J. Seidel, Spherical codes and designs, Geom. Dedicata, 6 (1977), pp. 363–388.
- [9] F. Diamond, J. Shurman, A First Course in Modular Forms, Springer New York, 2005.
- [10] L. Fejes Toth´ , Uber¨ die dichteste Kugellagerung, Math. Z. 48 (1943), pp. 676– 684.
- [11] T. Hales, A proof of the Kepler conjecture, Annals of Math. 162 (3) (2005), pp. 1065–1185.
- [12] D. Hejhal, The Selberg trace formula for PSL(2,R), Vol. 2, Springer Lecture Notes in Mathematics 1001 (1983).
- [13] G. A. Kabatiansky and V. I. Levenshtein, Bounds for packings on a sphere and in space, Problems of Information Transmission 14 (1978), pp. 1–17.
- [14] D. Mumford, Tata Lectures on Theta I, Birkh¨user, 1983.
- [15] H. Petersson, Ueber die Entwicklungskoeﬃzienten der automorphen Formen, Acta Mathematica, Bd. 58 (1932), pp. 169–215.
- [16] F. Pfender, G. M. Ziegler, Kissing numbers, sphere packings, and some unexpected proofs, Notices of the AMS 51 (8) (2004) pp. 873–883.
- [17] H. Rademacher and H. S. Zuckerman, On the Fourier coeﬃcients of certain modular forms of positive dimension, Annals of Math. (2) 39 (1938), pp. 433–462.
- [18] A. Thue, Uber¨ die dichteste Zusammenstellung von kongruenten Kreisen in einer Ebene, Norske Vid. Selsk. Skr. No.1 (1910), pp. 1–9.
- [19] V. A. Yudin, Lower bounds for spherical designs, Izv. Ross. Akad. Nauk Ser. Mat. 61 (1997), pp. 211–233. English transl., Izv. Math. 6 (1997), pp. 673–683.


##### [20] D. Zagier, Elliptic Modular Forms and Their Applications, In: The 1-2-3 of Modular Forms, (K. Ranestad, ed.) Norway, Springer Universitext, 2008.

Berlin Mathematical School Str. des 17. Juni 136 10623 Berlin and Humboldt University of Berlin Rudower Chaussee 25 12489 Berlin Email address: viazovska@gmail.com

