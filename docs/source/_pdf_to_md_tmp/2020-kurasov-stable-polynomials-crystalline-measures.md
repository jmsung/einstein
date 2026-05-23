# arXiv:2004.05678v1[math.FA]12Apr2020

## STABLE POLYNOMIALS AND CRYSTALLINE MEASURES

PAVEL KURASOV AND PETER SARNAK

Abstract. Explicit examples of positive crystalline measures and Fourier quasicrystals are constructed using pairs of stable of polynomials, answering several open questions in the area.

1. Introduction

Our investigation of the additive structure of the spectrum of metric graphs [14] provides exotic crystalline measures, in fact ones that give answers to a number of open problems. In this note we explicate the simplest examples and place the construction into the natural general setting of stable polynomials in several variables.

We recall the deﬁnitions. Deﬁnition. A crystalline measure µ on R is a tempered distribution of the form

- (1) µ = λ∈Λ

aλδλ, for which µˆ =

s∈S

bsδs,

where δξ is a delta mass at ξ, and Λ and S are discrete subsets of R [25]. If both |µ| and |µˆ| are tempered as well, then following [22, Section 1.1] we call µ a Fourier quasicrystal.

The basic example of a crystalline measure, in fact a Fourier quasicrystal, comes from the Poisson summation formula:

- (2) µ = m∈Z


δm ⇒ µˆ =

δ2πs,

s∈Z

and its extension to ﬁnite combinations of these called “generalized Dirac combs” [25]. Various examples of crystallline measures that are not Dirac combs were constructed by Guinand [9]. Note however that his example 4 page 264 coming from the explicit formula in the theory of primes does not give a Fourier quasicrystal, even assuming the Riemann hypothesis. Towards a classiﬁcation theory of crystalline measures µ there are a series of results that ensure that µ is a generalized Dirac comb ([4,20,22,24]), one of the ﬁrst being

Theorem (Meyer [24]). If aλ take values in a ﬁnite set and |µˆ| is translation bounded, that is sup

|µˆ|(x + [0,1]) < ∞, then µ is a generalized Dirac comb.

x∈R

Examples of varying complexity of Fourier quasicrystals which are not generalized Dirac combs, have been given ([11,21,25,27]), showing that any such classiﬁcation is probably very diﬃcult [5].

Date: April 14, 2020.

1

A basic question which has been open for some time is whether there are positive (that is with aλ ≥ 0) crystalline measures which are not generalized Dirac combs? The constructions in Sections 2 and 3 yield such µ’s which enjoy some other properties which resolve related open problems. In Section 2 we review the deﬁnition of stable polynomials and use them to construct positive Fourier quasicrystals. In Section 3 we examine the simplest non-trivial example and use Liardet’s proof of Lang’s conjecture in dimension two [16, 23] to analyze the additive structure of Λ, see Theorem 3. This example is rich enough for the purposes of this note. We end the section by recording the general additive structure theorem from [14] which applies to the supports Λ of the Fourier quasicrystal measures µ that are constructed from stable polynomials.

2. Summation formula

Stable polynomials. If P(z) = P(z1,...,zn) is a multivariable polynomial with complex coeﬃcients, we say that P is D = {z : |z| < 1} stable if P(z) = 0 for z = (z1,z2,...,zn) with zj ∈ D for all j. To deﬁne a stable pair, consider the involution operation on P obtained by zj → 1/zj for j = 1,2,...,n, the result being denoted by Pι.

Deﬁnition. Two multivariate polynomials P,Q are said to form stable pair if

- (1) both polynomials P and Q are D-stable;
- (2) there exist an integer-valued vector = ( 1, 2,..., n) ∈ Nn and a constant η such that P and Q satisfy the functional equation
- (3) Q(z) = η z

- 1

1 z

2

- 2 ...z


n

n Pι(z);

(3) the normalization condition P( 0) = Q( 0) = 1

is fulﬁlled. If such and η exists they are unique. Such stable pairs arise in many contexts and there are powerful techniques for proving stability [2,30]. We point to two basic examples.

- 1) Spectral pairs These come up as secular polynomials in quantum graphs [1,3]. Let P1,P2,...,Pk be monomials in z1,...,zn of the form


- (4) Pj(z) = z1aj,1z2aj,2 ...za

j,n

n , j = 1,2,...,k,

aj,ν ∈ N. Let ν = kj=1 aj,ν, which we assume being positive for every ν = 1,...,n. If S is a k × k unitary matrix, set

- (5) RS(z) = det










P1(z) 0 ... 0 0 P2(z) ... 0

Ik×k −

S

.

 

 

 

 

... . 0 0 ... Pk(z)

. .

Then it is easy to see that

P = RS, Q = RS−1,

is a stable pair with = ( 1,..., k) and η = (det(−S))−1. Our studies in [14] were inspired by the trace formula for metric graphs [10,12,13].

- 2) Lee-Yang pairs ([28, Theorem 5.12]) Let −1 ≤ Aij ≤ 1,Aij = Aji and


- (6) P(z) = S

 

i∈S j∈S

Aij

 zS,

where we use multi-index notation for zS = j∈S zj, the sum is over all subsets S of {1,2,...,n} and S is the complement of S. Then P is a self dual stable pair

- (7) (z1z2 ...zn) Pι(z) = P(z).

For generalizations of these see [2,19,30]. For the rest of this section we show how to attach to a stable pair and real numbers b1,b2,...,bn > 1 a crystalline measure.

Notations. Assume that P,Q is a stable pair of multivariable polynomials:

- (8) P(z) = 1 + m∈MP

aP(m)zm, Q(z) = 1 +

m∈MQ

aQ(m)zm,

where MP,Q are ﬁnite subsets of

- (9) Zn+ := {k = (k1,k2,...,kn),kj ∈ Z,kj ≥ 0,k = (0,0,...,0)}. Taking the logarithm we get the following expansion
- (10)

log P(z) =

∞

ν=1

(−1)ν ν m∈M

P

aP(m)zm

ν

=

∞

ν=1

(−1)ν ν m

1,m2,...,mν∈MP

aP(m1)aP(m2)...aP(mν)zm

1

zm

2

...zm

ν

=

∞

ν=1

(−1)ν ν k∈Z

n

+ m1+m2+···+mν=k

aP(m1)aP(m2)...aP(mν)zk,

hence

- (11) log P(z) = k∈Zn+

cP(k)zk,

where for k ∈ Zn+

- (12) cP(k) =

n j=1 kj

ν=1 m1+m2+···+mν=k

(−1)νaP(m1)aP(m2)...aP(mν) ν

.

Similar formulas hold for log Q(z). Dirichlet series. Let b1,b2,...,bn be real numbers larger than 1 and let ξj = lnbj > 0, j = 1,2,...,n. Let us denote by Γ+ and L+ the corresponding multiplicative and additive semigroups

- (13)


Γ+ = {bm

- 1

1 bm

2

- 2 ...bm


n : mj ∈ N ∪ {0}} \ {1};

n

L+ = log Γ+ = {m1ξ1 + m2ξ2 + ··· + mnξn : mj ∈ N ∪ {0}} \ {0}.

The elements of these semigroups will be denoted by b and ξ respectively

b ∈ Γ+, ξ ∈ L+.

Let us introduce the following two entire functions of order 1

- (14)

- F(s) := P(b−1 s,b−2 s,...,b−ns) ≡ P(e−ξ

1s,e−ξ

2s....,e−ξ

ns), s ∈ C.

- G(s) := Q(b−1 s,b−2 s,...,b−ns) ≡ Q(e−ξ


1s,e−ξ

2s....,e−ξ

ns), The functions are related via the functional equation

F(−s) = P(bs1,bs2,...,bsn) = Pι(b−1 s,...,b−ns)

= η−1 b

1

1 ...b

n

n

s

G(s)

- (15) ⇒ F(−s) = η−1 b 1 s G(s),

where = ( 1, 2,..., n). The stability conditions on P and Q ensure that all zeroes of F(s) and G(s) are on the imaginary axis (s) = 0. Moreover (15) implies that the zeroes for F an G are obtained from each other via reﬂection. F and G are ﬁnite Dirichlet series, that is

- (16) F(s) = 1 + m∈MP

aP(m)(bm)−s, G(s) = 1 +

m∈MQ

aQ(m)(bm)−s.

Logarithmic derivatives. For (s) large enough the series for log F(s) converges absolutely:

- (17) log F(s) = k∈Zn+

cP(k)e−(k

1ξ1+k2ξ2+···+knξn)s =

k∈Zn+

cP(k)e−(ξ·k)s.

Hence for (s) large

- (18)

F (s) F(s)

= −

k∈Zn+

(ξ · k)cP(k)e−(ξ·k)s.

A similar analysis can be applied to the entire function G(s) leading to

- (19)

G (s) G(s)

= −

k∈Zn+

(ξ · k)cQ(k)e−(ξ·k)s.

Formula (15) establishes the following relation between the logarithmic derivatives of F and G

log F(−s) = −log η + s(ξ · ) + log G(s)

- (20) ⇒ −


F (−s) F(−s)

G (s) G(s)

= (ξ · ) +

.

Note that this relation is independent of the parameter η appeared ﬁrst in (3).

## Logarithmic derivative as a distribution. Let Ψ ∈ C0∞(R>0) and

∞

dx x

### (21) Ψ(˜ s) =

Ψ(x)xs

.

0

Ψ(˜ s) is entire and is rapidly decreasing when |t| → ∞ for s = σ + it, σ ﬁxed. Consider the integral

- 1

- 2πi (s)=R


### (22) I :=

F (s) F(s)

Ψ(˜ s)ds,

which is converging for large real R. We next calculate I in two diﬀerent ways using the functional equation connecting F and G. Expansion (18) gives us

 −

 Ψ(˜ s)ds

- 1

- 2πi (s)=R


(ξ · k)cP(k)e−(ξ·k)s

I =

k∈Zn+

### (23)

- 1

- 2πi (s)=R


Ψ(˜ s)e−(ξ·k)sds.

= −

(ξ · k)cP(k)

k∈Zn+

To get the second representation we shift the contour for the integral deﬁning I to (s) = −R picking up the residues, which are Ψ(˜ ρ), since the function Ψ˜ is integrated with the logarithmic derivative. Summing over all zeroes of F (which are lying on the imaginary axis) we obtain

Ψ(˜ ρ),

### (24) ρ:F(ρ)=0

hence

F (s) F(s)

- 1

- 2πi (s)=−R


Ψ(˜ ρ) +

Ψ(˜ s)ds

I =

ρ:F(ρ)=0

F (−s) F(−s)

- 1

- 2πi (s)=R


Ψ(˜ ρ) +

Ψ(˜ −s)ds

=

ρ:F(ρ)=0

Formula (20) together with expansion (19) then imply

- 1

- 2πi (s)=R


Ψ(˜ ρ) − (ξ · )

Ψ(˜ −s)ds

I =

ρ:F(ρ)=0

### (25)

- 1

- 2πi (s)=R


Ψ(˜ −s)e−(ξ·k)sds

(ξ · k)cQ(k)

+

k∈Zn+

Comparing two formulas for I (expressions (23) and (25)) we may calculate the sum over the zeroes of F

- 1

- 2πi (s)=R


Ψ(˜ s)ds

Ψ(˜ ρ) = (ξ · )

ρ:F(ρ)=0

- 1

- 2πi (s)=R


Ψ(˜ s)e−(ξ·k)sds

−

(ξ · k)cP(k)

### (26)

k∈Zn+

- 1

- 2πi (s)=R


Ψ(˜ −s)e−(ξ·k)sds

−

(ξ · k)cQ(k)

k∈Zn+

Summation formula. We make change of variables:

x = et; (0,+∞) → (−∞,+∞),

so that

Ψ(et) = h(t) for a certain h ∈ C0∞(R). We have in particular: Ψ(˜ iγ) =

∞

∞

x = et dx = etdt

dx x

h(t)eiγtdt = hˆ(γ),

Ψ(x)xiγ

=

=

−∞

0

where hˆ is the Fourier transform of h and Ψ(˜ s)e−(ξ·k)sds =

∞

dx x

- 1

- 2πi (s)=R


- 1

- 2πi (s)=R


e−(ξ·k)sds

Ψ(x)xs

0

∞

+∞

1 2π

h(t)e(R+is)tdt e−(ξ·k)Re−i(ξ·k)sds

=

−∞

−∞

= h(ξ · k). Then formula (26) becomes the following summation formula

- (27) γ:F(iγ)=0

hˆ(γ) = (ξ· )h(0)−

k∈Zn+

(ξ·k)cP(k)h(ξ·k)−

k∈Zn+

(ξ·k)cQ(k)h(−ξ·k)

which is valid for any hˆ ∈ C0∞(R), and extends to all of S(R) as shown in the proof of Theorem 1 below. To be precise, introducing the discrete support set

ΛP := {γ : F(iγ) = 0} obtained from the zero set of F (all lying on the imaginary axis) we deﬁne the discrete measure associated with the left hand side of (27)

- (28) µP := γ:F(iγ)=0

δγ ≡

λ∈ΛP

m(λ)δλ,

where m(λ) is the multiplicity of the corresponding zero. Then the spectrum SP of µ is a subset of

L+ ∪ −L+ ∪ {0}. (with L+ introduced in (13)) and the Fourier transform of µ can be written as

- (29) µˆ = (ξ · ) − k∈Zn+


(ξ · k)cP(k)δξ·k −

(ξ · k)cQ(k)δ−ξ·k.

k∈Zn+

- Theorem 1. Given any pair P,Q of stable polynomials satisfying assumptions (1) and (2) the measure µ is a positive crystalline measure, in fact a Fourier quasicrystal and is an almost periodic measure.


Proof. The support of µ is given by the zeroes iγj of the entire function F in (14) and hence the support Λ of µ is discrete. The support S of µˆ is a subset of L+ ∪ −L+ ∪ {0} which is also discrete. Since m(λ) ≥ 1 and µ is positive, applying the summation formula to φ(y) = φ0(x − y) with φ0 ≥ 0,φ0 ≥ 1 on [−1,1] and φˆ0 having compact support in (− 0, 0) where (− 0, 0) ∩ (L+ ∪ −L+) is empty, yields

m(λ) (ξ · )φˆ0(0), uniformly in x. That is µ = |µ|

λ:x−1≤λ≤x+1

is translation bounded and in particular µ and hence µˆ are both tempered. This shows that µ is a crystalline measure. To show that it is a Fourier quasicrystal we need to show in addition that |µˆ| is tempered (since µ = |µ|). To this end we ﬁrst bound the coeﬃcients cP(k) in (11). The series in (11) converges absolutely and uniformly for z in compact subsets of Dn = D × D × ··· × D, and yields log P(z) = ln|P(z)| + iarg P(z) where the arg is gotten by continuous variation along the path {sz},0 ≤ s ≤ 1. Since P(sz), as a function of s is a polynomial in s of degree deg P, it follows that

- (30) |arg P(z)| ≤ π(deg P).

Let K = sup

z∈Dn

|P(z)|, then

- (31) ln|P(z)| ≤ lnK, for z ∈ Dn. Introducing the notation

eiθ = (eiθ

1

,eiθ

2

,...,eiθ

n

) we have from (11) that for 0 ≤ r < 1

- (32) Tn

log P(reiθ)e−ik·θdθ = r[k|cP(k). In particular for k = 0

- (33) Tn

ln|P(reiθ)|dθ = 0, since the constant term is absent in (11). According to (31)

ln|P(reiθ)| − lnK ≤ 0 and hence

- (34)

Tn

ln|P(reiθ)| dθ =

Tn

ln|P(reiθ)| − lnK + lnK dθ

≤ −

Tn

ln|P(reiθ)| − lnK dθ + lnK

= 2lnK by (33). From (32) and the r independent bounds (30) and (34) we deduce

- (35) |cP(k)| ≤ C < ∞. From (29), it follows that the measure |µˆ| satisﬁes
- (36) |µˆ|([−A,A]) ≤ ξ · + 2


(ξ · k)|cP(k)|

k∈Zn+,ξ·k≤A

≤ ξ · + 2max{ξj}C

(k1 + k2 + ··· + kn)

k∈Zn+, k1+k2+···+kn≤A/ min{ξj}

n+1

A min{ξj}

≤ ξ · + 2max{ξj}C

+ 1

.

Hence |µˆ|([−A,A]) grows at most polynomially (∼ An+1) and therefore determines a tempered distribution.

To complete the proof we invoke Theorem 11 of [8] which asserts that our translation bounded µ which has countable spectrum is an almost periodic measure in the sense of [25, Deﬁnition 5].

## Remarks.

• Starting with the function G instead of F we get a similar summation formula

- (37)

γ:F(iγ)=0

hˆ(−γ) = (ξ · )h(0)−

k∈Zn+

(ξ ·k)cQ(k)h(ξ ·k)−

k∈Zn+

(ξ ·k)cP(k)h(−ξ ·k).

Summing the two formulas we get

- (38)

γ:F(iγ)=0

h ˆ(γ)+hˆ(−γ) = 2(ξ· )h(0)−

k∈Zn+

(ξ·k) cP(k)+cQ(k) h(ξ·k)+h(−ξ·k) .

• In the self dual case P(z) = Q(z) the summation formula takes the simplest form

- (39) γ:F(iγ)=0

hˆ(γ) = (ξ · )h(0) −

k∈Zn+

(ξ · k)cP(k) h(ξ · k) + h(−ξ · k) .

• The simplest stable polynomial is

P(z1) = 1 − z1. For it

Q(z1) = z1 − 1; F(s) = 1 − 1/bs1; γn =

2π ξ1

n, n ∈ Z;

log F(s) = log(1 −

1 bs1

) = −

∞

n=1

1 n

1 (bn1)s

;

F F

(s) =

∞

n=1

1 (bn1)s

ξ1; Substitution into the summation formula (27) gives

- (40) n∈Z

hˆ

2π ξ1

n = ξ1 h(0) +

∞

n=1

h(nξ1) + h(−nξ1) ≡ ξ1

n∈Z

h(nξ1),

which is nothing else than the classical Poisson summation formula (properly scaled) (see (2) below).

3. The first non-trivial example

Our goal in this section is to present an explicit example of a positive crystalline measure. Consider the following polynomial

- (41) P(z1,z2) = 1 −


1 3

1 3

z22 − z1z22, in fact describing the non-linear part of the spectrum of the lasso graph [14]. With 1 = 1, 2 = 2 and η = −1 we get Q(z1,z2) = (−1) z1z22 −

z1 +

1 3

1 3

z22 +

z1 − 1 ≡ P(z1,z2).

The polynomial is D-stable since the equation P(z1,z2) = 0 can be writen as z1 − 3

= z22

1 − 3z1

1−3

and the M¨bius transformation z1  → z

1−3z1 maps the unit disk to its complement. The Dirichlet series is equal to

F(s) = 1 −

1 3

1 bs1

+

1 3

1 bs1b22s

1 b22s −

.

with

∞

k

1 k

1 3

1 bs1 −

1 3

1 b22s

1 bs1b22s

log F(s) = −

+

k=1

1 bn

### =

c(n1,2n2)

,

1 b2n

1s

2s 2

(n1,n2)∈Z2+

(−1)k

(k1 + k2 + k3 − 1)! k1! k2! k3!

2

- (42) c(n1,2n2) = − k1,k2,k3∈N∪{0}


3k1+k2 .

- k1+k3=n1
- k2+k3=n2


To determine the zero set of F(s) let us ﬁrst describe the zero set of P on the unit torus T = (z1,z2) ∈ C2 : |z1| = |z2| = 1 . Introducing notations z1 = eix,z2 = eiy the same torus can be seen as the square [0,2π] × [0,2π] with the opposite sides identiﬁed. Then the zero set is described by the Laurent polynomial

x 2

L(x,y) = 3sin(

x 2 − y)

+ y) + sin(

and is plotted in Figure 1.

- 0

- 1

- 2

- 3

- 4

- 5

- 6


Y

0 1 2 3 4 5 6 X

### Figure 1. Zero set for L(x,y).

Note that the normal to the curve always lies in the ﬁrst quadrant, in fact

∂y ∂x

∂L(x,y)

- ∂x

∂L(x,y)

- ∂y


= −

- 1

- 2
- 3cos(x/2 + y) + cos(x/2 − y) 3cos(x/2 + 1) − cos(x/2 − y)


= − = −

- 1

- 2


8 (3cos(x/2 + y) − cos(x/2 − y))2 < 0,

where we used that L(x,y) = 0. Knowing the zero set of L(x,y) the zeroes of the Dirichlet series F(s) (all lying on the imaginary axis) are obtained in the following way:

0 = F(iγj) = P(biγ1 j,biγ2 j) = P(eiγ

jξ1,eiγ

jξ2) = L(γjξ1,γjξ2)

- (43) ⇔ 3sin (

ξ1 2

+ ξ2)γj + sin (

ξ1 2 − ξ2)γj = 0,

where we used that ξj = lnbj > 0. In other words, zeroes of F are situated at the intersection points between the line (γξ1,γξ2) and the zero curve for L. Both the normal to the zero curve and the guide vector for the line belong to the ﬁrst quadrant, hence the intersection is never tangential. This implies in particular that all zeroes are simple. γ0 = 0 is always a solution since L(0,0) = 0. All other zeroes γj indicate the distance between the intersection points and the origin measured along the line. It is clear that L(−x,−y) = −L(x,y) (which also follows from (15) and the fact that F = G in the current example) implying that the zeroes are symmetric with respect to the origin. The summation formula (27) takes the form

- (44)


hˆ(γj) = (ξ1 + 2ξ2)h(0) −

γj

c(n1,2n2)(n1ξ1 + 2n2b2) h(n1ξ1 + 2n2ξ2)

n=(n1,n2)∈Z2+

+h(−(n1ξ1 + 2n2ξ2)) , where

- • γj are solutions to the secular equation (43);
- • c(n1,2n2) are given by (43);
- • h ∈ C0∞(R) - an arbitrary test function.


The diﬀerence between formula (44) and the general formula (27) is due to the fact that the stable polynomials depend just on z22. Both series on the left and right hand sides are inﬁnite but they have diﬀerent properties depending on whether ξ1 and ξ2 are rationally dependent or not. This is related to the number of intersection points on the torus. Also the number of zeroes iγj is always inﬁnite, the number of intersection points on the torus may be ﬁnite. Indeed, if ξ

ξ2 ∈ Q, then the line is periodic on the torus, implying that there are ﬁnitely many intersection points (on the torus). The points γj form a periodic sequence implying that obtained summation formula is just a ﬁnite sum of Poisson summation formulas with the same period and µ is a generalized Dirac comb.

1

Next we assume that ξ1 and ξ2 are rationally independent

- (45)

- ξ1

- ξ2


∈/ Q.

By Kronecker’s theorem the line covers the torus densely and therefore the intersection points (γjξ1,γjξ2) cover densely the zero curve of L as well. We are interested in the rational dependence of γj,j ∈ Z. In particular we shall need the following

Lemma 1. If ξ1 and ξ2 are rationally independent, then the secular equation (43) L(γξ1,γξ2) = 0

has inﬁnitely many rationally independent solutions, i.e.

- (46) dimQ LQ{γj}j∈Z = ∞,

where LQ denotes the linear span with rational coeﬃcients and dimQ the dimension of the vector space with respect to the ﬁeld Q.

Proof. Assume that the dimension is ﬁnite. This means that there exists a certain M ∈ N such that every γj for arbitrary j can be written as a rational combination of γ1,...,γM:

- (47) γj = aj1γ1 + aj2γ2 + ··· + ajMγM, ajm ∈ Q. It follows that

eiγ

jξα = eiγ

1ξα aj1 eiγ

2ξα aj2 × ··· × eiγ

Mξα ajM , α = 1,2, or equivalently

- (48) biγ

j

α = bik

1

α

aj1 bik

2

α

aj2 × ··· × bik

M

α

ajM . Consider the multiplicative subgroup of (C∗)2 generated by

(bik

m

1 ,bik

m

2 ), m = 1,2,...,M

with the multiplication carried out coordinate wise. Then points (bik1 j,bik2 j) belong to the division group Γ of Γ, that is

Γ = z ∈ (C∗)2 : zm ∈ Γ for some m ≥ 1 .

In accordance with S. Lang’s conjecture [16] intersection between any algebraic subvariety and the division group for a ﬁnitely generated subgroup is along a ﬁnitely many subtori. The following theorem is proven in [23]

Theorem (Liardet [23]). Assume that:

- • Γ is a ﬁnitely generated subgroup of the multiplicative group of the complex torus (C∗)2;
- • Γ is the division group of Γ;

- • V ⊂ (C∗)2 is an algebraic subvariety given by the zero set of Laurent polynomials.


Then the intersection of V and Γ belongs to the union of a ﬁnitely many translates of certain subtori T1,...,Tν contained in V :

- (49) V ∩ Γ = V ∩ T1 ∪ T2 ∪ ··· ∪ Tν .


Now no line belongs to the zero set of L, so L contains no one dimensional subtori and hence the intersection of the zero set (the curves plotted in Figure 1) and the union of Tj in (49) is also ﬁnite. This contradicts the fact that the number of intersection points is inﬁnite if ξ1 and ξ2 are rationally independent, which completes the proof.

Our main result can be formulated as

- Theorem 2. For ξ1/ξ2 ∈/ Q, the Fourier quasicrystal measure µ corresponding to P in (41), satisﬁes:


- i) aλ = 1 for λ ∈ Λ, that is µ is a positive “idempotent”.
- ii) dimQ Λ = ∞, dimQ S = 2, in particular µ is not a generalized Dirac comb.
- iii) Λ meets any arithmetic progression in R in a ﬁnite number of points.
- iv) Λ is a Delone set (that is the minimal distance between elements of Λ is bounded below by a positive constant and Λ is relative dense in R) while S is not a Delone set.
- v) |µˆ| is not translation bounded.


Proof. That µ is a Fourier quasicrystal follows from Theorem 1. Note however that the argument with c(n1,2n2) being Fourier coeﬃcients for log P on the torus is especially transparent, since P is real on T2 and log P has just logarithmic singularities on the smooth curve L(x,y) = 0 and therefore is absolutely integrable.

- i) All zeroes of the secular equation (43) have multiplicity one and form a discrete set, hence by construction aλ = 1 and µ is a positive idempotent discrete measure.
- ii) Since ξ1/ξ2 ∈/ Q Lemma 1 implies that dimQ ΛP = ∞, hence the support of µ is not contained in a ﬁnite union of translates of any lattice and µ is not a generalized Dirac comb. The spectrum SP – the support of µˆ – belongs to

L+ ∪ −L+ ∪ {0} and its dimension is equal to 2.

- iii) Assume that there exists a full arithmetic progression, say γ∗n which intersects support of µ at an inﬁnite number of points. Consider the corresponding group

generated by (bγ

∗

1 ,bγ

∗

2 ). Its intersection with the algebraic subvariety P(z1,z2) = 0 (where P is given by (41)) is along a ﬁnitely many subtori (Liardet’s Theorem) as before. The zero set contains no one-dimensional subtori, hence the number of intersection points on the torus is ﬁnite. The number of intersection points between the arithmetic progression and the zero set can be inﬁnite only if certain points occur several times, but this is impossible since ξ1/ξ2 ∈/ Q. It follows that the intersection between any arithmetic progression and Λ is always ﬁnite. The same result could be proven using Lech’s theorem (Lemma on page 417 in [18]).

- iv) The zero set of L(x,y) is given by two non-intersecting curves on [0,2π]2 implying that there is a minimal distance ρ between the diﬀerent components of the


curve. Taking into account that the intersection between the line (ξ1γ,ξ2γ) and the zero curve of L(x,y) is non-tangential we conclude that there is a minimal distance between the consecutive solutions γj of the secular equation (43). The function L(γξ1,γξ2) is given by a sum of two sinus functions with amplitudes 3 and 1 implying that every interval [n 2π

### 2 +ξ2 ,(n+1) 2π

2 +ξ2 ] contains a solution to the secular equation. It follows that the support of µ is relatively dense and uniformly discrete, i.e. is a Delone set. The spectrum SP is not a Delone set, since otherwise the measure µ would be a generalized Dirac comb [20].

ξ1

ξ1

- v) Similarly |µˆ| is not translation bounded since otherwise this would contradict Meyer’s Theorem stating that every crystalline measure with aλ from a ﬁnite set (aλ = 1 in our case) and |µˆ| translation bounded is a generalized Dirac comb (see Introduction and [24]).


## Remarks to Theorem 2:

- • Properties (ii) and (iii) show that the measures µ in the theorem are far from being generalized Dirac combs.
- • In Theorem 5.16 of [26] a positive measure µ of the type in (1) is constructed for which Λ is discrete but for which S need not be (called there a Poisson measure). In fact these Λ’s can be realized as the intersection of the graph of a periodic continuous function on the two torus with an irrational line, and as such are of a similar shape to our µ’s.


The measures µ in Theorem 2 provide examples answering the following questions concerning crystalline measures:

- (A) The last question in [25]): a positive crystalline measure which is not a generalized Dirac comb;
- (B) Part 3 of question 11.2 in [22]: a positive Fourier quasicrystal for which every arithmetic progression meets the support in a ﬁnite set;
- (C) The question on page 3158 of [25] and part 2 of question 11.2 in [22]) a Fourier quasicrystal for which the support (that is Λ) is a Delone set, but the spectrum (that is S) is not;
- (D) Problem 4.4 in [15]: a discrete set (that is Λ) which is a Bohr almost periodic Delone set, but is not an ideal crystal.


In our forthcoming paper [14] we use higher dimensional quantitative theorems from Diophantine analysis [6,7,17,29] to show that general crystalline µ constructed in Section 2 using a stable pair P,Q with parameters b1,...,bn, satisﬁes:

Theorem 3. For such a µ we have that

- i) Λ = L1 L2  ··· Lν N, with L1,...,Lν full arithmetic progressions and N if not empty is inﬁnite dimensional over Q (the union means counted with multiplicities).
- ii) aλ take values in a ﬁnite set of positive integers; µ is a positive Fourier quasicrystal.
- iii) dimQ S = dimQ {ξ1,...,ξn}.
- iv) There is c = c(P) < ∞ such that any arithmetic progression in R+ meets N in at most c(P) points.


## Remarks to Theorem 3:

• Theorem 3 allows us to make µ’s for which dimQ S is as large as we please, however in as much as any positive crystalline measure is (measure) almost periodic it follows from Lemma 5 of [25] that S ∩ (0,∞) or S ∩ (−∞,0) cannot be linearly independent over Q.

4. Acknowledgement

The authors would like to thank Boris Shapiro for initiating our collaboration, Yves Meyer for attracting our attention to crystalline measures and pointing us to his paper [26], Alexei Poltoratskii for pointing out importance of positive crystalline measures, and Nir Lev and Alexander Olevskii for their comments.

References

- [1] F. Barra and P. Gaspard, On the level spacing distribution in quantum graphs, J. Statist. Phys. 101 (2000), no. 1-2, 283–319, DOI 10.1023/A:1026495012522. Dedicated to Gre´goire Nicolis on the occasion of his sixtieth birthday (Brussels, 1999). MR1807548
- [2] Julius Borcea and Petter Br¨ande´n, The Lee-Yang and P´olya-Schur programs. I. Linear operators preserving stability, Invent. Math. 177 (2009), no. 3, 541–569, DOI 10.1007/s00222009-0189-3. MR2534100
- [3] Yves Colin de Verdie`re, Semi-classical measures on quantum graphs and the Gaußmap of the determinant manifold, Ann. Henri Poincare´ 16 (2015), no. 2, 347–364, DOI 10.1007/s00023014-0326-4. MR3302601
- [4] Antonio C´ordoba, La formule sommatoire de Poisson, C. R. Acad. Sci. Paris Se´r. I Math. 306 (1988), no. 8, 373–376 (French, with English summary). MR934622
- [5] Freeman Dyson, Birds and frogs, Notices Amer. Math. Soc. 56 (2009), no. 2, 212–223. MR2483565
- [6] Jan-Hendrik Evertse, Points on subvarieties of tori, A panorama of number theory or the view from Baker’s garden (Zu¨rich, 1999), Cambridge Univ. Press, Cambridge, 2002, pp. 214–230, DOI 10.1017/CBO9780511542961.015. MR1975454
- [7] J.-H. Evertse, H. P. Schlickewei, and W. M. Schmidt, Linear equations in variables which lie in a multiplicative group, Ann. of Math. (2) 155 (2002), no. 3, 807–836, DOI 10.2307/3062133. MR1923966
- [8] S. Yu. Favorov, Large Fourier quasicrystals and Wiener’s theorem, J. Fourier Anal. Appl. 25

(2019), no. 2, 377–392, DOI 10.1007/s00041-017-9576-0. MR3917950

- [9] A. P. Guinand, Concordance and the harmonic analysis of sequences, Acta Math. 101 (1959), 235–271, DOI 10.1007/BF02559556. MR107784
- [10] Boris Gutkin and Uzy Smilansky, Can one hear the shape of a graph?, J. Phys. A 34 (2001), no. 31, 6061–6068, DOI 10.1088/0305-4470/34/31/301. MR1862642
- [11] Mihail N. Kolountzakis, Fourier pairs of discrete support with little structure, J. Fourier Anal. Appl. 22 (2016), no. 1, 1–5, DOI 10.1007/s00041-015-9416-z. MR3448912
- [12] Pavel Kurasov, Schro¨dinger operators on graphs and geometry. I. Essentially bounded potentials, J. Funct. Anal. 254 (2008), no. 4, 934–953, DOI 10.1016/j.jfa.2007.11.007. MR2381199
- [13] , Graph Laplacians and topology, Ark. Mat. 46 (2008), no. 1, 95–111, DOI 10.1007/s11512-007-0059-4. MR2379686

- [14] Pavel Kurasov and Peter Sarnak, The additive structure of the spectrum of a quantum graph, in preparation (2020).
- [15] Jeﬀrey C. Lagarias, Mathematical quasicrystals and the problem of diﬀraction, Directions in mathematical quasicrystals, CRM Monogr. Ser., vol. 13, Amer. Math. Soc., Providence, RI, 2000, pp. 61–93. MR1798989
- [16] Serge Lang, Report on diophantine approximations, Bull. Soc. Math. France 93 (1965), 177–

192. MR193064

- [17] Michel Laurent, Equations´ diophantiennes exponentielles, Invent. Math. 78 (1984), no. 2, 299–327, DOI 10.1007/BF01388597 (French). MR767195
- [18] Christer Lech, A note on recurring series, Ark. Mat. 2 (1953), 417–421, DOI 10.1007/BF02590997. MR56634
- [19] T. D. Lee and C. N. Yang, Statistical theory of equations of state and phase transitions. II. Lattice gas and Ising model, Phys. Rev. (2) 87 (1952), 410–419. MR53029
- [20] Nir Lev and Alexander Olevskii, Quasicrystals and Poisson’s summation formula, Invent. Math. 200 (2015), no. 2, 585–606, DOI 10.1007/s00222-014-0542-z. MR3338010
- [21] , Quasicrystals with discrete support and spectrum, Rev. Mat. Iberoam. 32 (2016), no. 4, 1341–1352, DOI 10.4171/RMI/920. MR3593527


- [22] , Fourier quasicrystals and discreteness of the diﬀraction spectrum, Adv. Math. 315

(2017), 1–26, DOI 10.1016/j.aim.2017.05.015. MR3667579

- [23] Pierre Liardet, Sur une conjecture de Serge Lang, Journ´ees Arithme´tiques de Bordeaux (Conf., Univ. Bordeaux, Bordeaux, 1974), Soc. Math. France, Paris, 1975, pp. 187–210. Ast´erisque, Nos. 24-25 (French). MR0376688
- [24] Yves Meyer, Nombres de Pisot, nombres de Salem et analyse harmonique, Lecture Notes in Mathematics, Vol. 117, Springer-Verlag, Berlin-New York, 1970 (French). Cours Peccot donn´e au Coll`ege de France en avril-mai 1969. MR0568288
- [25] Yves F. Meyer, Measures with locally ﬁnite support and spectrum, Proc. Natl. Acad. Sci. USA 113 (2016), no. 12, 3152–3158, DOI 10.1073/pnas.1600685113. MR3482845
- [26] , Global and local estimates on trigonometric sums, Trans. R. Norw. Soc. Sci. Lett. 2

(2018), 1–25.

- [27] Danylo Radchenko and Maryna Viazovska, Fourier interpolation on the real line, Publ. Math. Inst. Hautes Etudes´ Sci. 129 (2019), 51–81, DOI 10.1007/s10240-018-0101-z. MR3949027
- [28] David Ruelle, Thermodynamic formalism, Encyclopedia of Mathematics and its Applications, vol. 5, Addison-Wesley Publishing Co., Reading, Mass., 1978. The mathematical structures of classical equilibrium statistical mechanics; With a foreword by Giovanni Gallavotti and Gian-Carlo Rota. MR511655
- [29] Wolfgang M. Schmidt, The zero multiplicity of linear recurrence sequences, Acta Math. 182

(1999), no. 2, 243–282, DOI 10.1007/BF02392575. MR1710183

- [30] David G. Wagner, Multivariate stable polynomials: theory and applications, Bull. Amer. Math. Soc. (N.S.) 48 (2011), no. 1, 53–84, DOI 10.1090/S0273-0979-2010-01321-5. MR2738906


