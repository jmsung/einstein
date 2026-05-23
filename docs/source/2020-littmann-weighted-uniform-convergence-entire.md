---
type: source
kind: paper
title: Weighted uniform convergence of entire Grünwald operators on the real line
authors: Friedrich Littmann, Mark Spanier
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2011.09910v1
source_local: ../raw/2020-littmann-weighted-uniform-convergence-entire.pdf
topic: author-sweep
cites:
---

arXiv:2011.09910v1[math.CA]19Nov2020

WEIGHTED UNIFORM CONVERGENCE OF ENTIRE GRUNWALD¨ OPERATORS ON THE REAL LINE

FRIEDRICH LITTMANN AND MARK SPANIER

Abstract. We consider weighted uniform convergence of entire analogues of the Gru¨nwald operator on the real line. The main result deals with convergence of entire interpolations of exponential type τ > 0 at zeros of Bessel functions in spaces with homogeneous weights. We discuss extensions to Gru¨nwald operators from de Branges spaces.

1. Introduction and Results

An entire function F, not identically zero, has exponential type if τ(F) deﬁned by

|z|−1 log |F(z)| (1)

τ(F) = limsup

|z|→∞

is ﬁnite. The nonnegative number τ(F) is called the exponential type of F.

Let w be a measurable, nonnegative function on R; we call w a weight. We denote by Bp(τ,w) the space of entire functions F of exponential type τ ≥ 0 with Fw ∈ Lp(R). For functions f : R → C and a weight w, we seek discrete sets T ⊆ R and Gτf ∈ B∞(τ,w) with Gτf(t) = f(t) for t ∈ T and

lim

(Gτf − f)w ∞ = 0. (2)

τ→∞

By way of motivation we review known results from polynomial interpolation. Feje´r discovered the following property of interpolation at the zeros of the Chebyshev polynomials: denoting by xn,k the kth zero of the nth Chebyshev polynomial, there exists a polynomial H2n−1 of degree 2n − 1 with H2n−1(xn,k) = f(xn,k) and H2′n−1(xn,k) = 0 such that for continuous

- f the statement f − H2n−1 L∞[−1,1] → 0 as n → ∞ holds. There has been a large amount of research into analogous statements for


weighted polynomial spaces where the interpolation points are chosen to be zeros of certain associated orthogonal polynomials, cf. Horva´th [7], Lubinsky [8], Szabados [9, 10], Szabo´ [12], and the references therein. For earlier work we refer to the book by Szabados and Ve´rtesi [11]. There are diﬀerent generalizations of Feje´r’s result; the so called Feje´r-Hermite interpolation has derivative zero at the interpolation nodes, while the Gru¨nwald operator assigns a derivative value at each node that depends on the function and

![image 1](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile1.png>)

2010 Mathematics Subject Classiﬁcation. Primary 41A05; Secondary 41A17, 30E05. Key words and phrases. Gru¨nwald operator, Hermite-Feje´r interpolation, weighted uni-

form approximation, de Branges space, exponential type.

1

the location of the nodes. Concretely, the polynomial Gru¨nwald operator is given by

n

f(yn,k)ℓ2n,k(z)

z  →

k=1

where (yn,k) is a given set of nodes and ℓn,k is the kth Lagrange interpolating polynomial of degree ≤ n for (yn,k). As we indicate below, the corresponding operator for functions of exponential type is in some sense the most natural generalization of Feje´r’s result to weighted spaces on the real line. It was pointed out in Gervais, Rahman, and Schmeisser [4] that the series

sin2(τz) (τz − k)2

f(τ−1k)

(3)

Fτf(z) =

![image 2](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile2.png>)

k∈Z

has convergence properties entirely analogous to the Feje´r result but no other entire Gru¨nwald operators seem to have been investigated.

Let ν > −1. Our ﬁrst results deals with homogeneous weights wν(x) = |x|2ν+1.

Let Jν be the Bessel function of order ν of the ﬁrst kind. We deﬁne entire functions Aν and Bν by

- Aν(z) = Γ(ν + 1)(z/2)−νJν(z),
- Bν(z) = Γ(ν + 1)(z/2)−νJν+1(z),


(4)

and for τ > 0 we deﬁne the formal series Gν,τf,Hν,τf by

- Gν,τf(z) = t∈Tν

f(τ−1t)

A2ν(τz) A′ν(t)2(τz − t)2

![image 3](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile3.png>)

- Hν,τf(z) = t∈Tν+1


(5)

Bν2(τz) Bν′ (t)2(τz − t)2

f(τ−1t)

![image 4](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile4.png>)

where Tν = {±ξ : Jν(ξ) = 0,ξ > 0}.

Let f be continuous on R\{0} and assume that fwν has a limit at the origin. We say that fwν has a uniformly continuous extension to R if, after deﬁning the value of fwν at the origin to be this limit, the resulting function is uniformly continuous on R.

Theorem 1. Let ν > −1 with ν = −12 and τ > 0. If f ∈ C(R\{0}) with fwν ∈ L∞(R), then Gν,τf and Hν,τf deﬁne entire functions of exponential type 2τ. If in addition fwν has a uniformly continuous extension to R with

![image 5](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile5.png>)

then (a) for ν > −12

![image 6](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile6.png>)

lim

f(x)wν(x) = 0,

x→0

lim

τ→∞

(Gν,τf − f)wν ∞ = 0,

and (b) for −1 < ν < −21 lim

![image 7](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile7.png>)

(Hν,τf − f)wν ∞ = 0.

τ→∞

The usual approach to polynomial analogues of (2) consists in requiring a condition of the form fv ∈ L∞(R) with a diﬀerent weight v which is usually more restrictive than the target weight (but not always, see Szabo´ [12, Corollary 2]), prove (2) for a dense set, and extend to the smaller space. In this paper we follow a diﬀerent approach that is modeled after Feje´r’s original proof. We construct approximations Lν,τ to 1/wν and use the identity

(Gν,τf − f)wν = (Gν,τf − fLν,τwν)wν + fwν(Lν,τwν − 1). (6)

A good candidate for Lν,τ is the extremal minorant of 1/wν among functions of exponential type 2τ with respect to L1(wν) norm (cf. [2]). We show in Lemmas 3 and 6 that Lν,τ = Gν,τwν−1 for ν > −21 and Lν,τ = Hν,τwν−1 for −1 < ν < −21 which allows estimation of the ﬁrst summand on the right. The diﬀerence Lν,τ − 1/wν has a representation in terms of Laplace transforms that gives L∞ bounds to control the second summand.

![image 8](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile8.png>)

![image 9](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile9.png>)

Remarks.

- (a) Uniform convergence fails for f = 1/wν if ν = 12, i.e., the condition f(x)wν(x) → 0 as x → 0 is necessary. (The case ν = −21 is the unweighted case where (3) is used.)

![image 10](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile10.png>)

![image 11](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile11.png>)

- (b) To obtain uniform convergence of (Gν,τf − f)wν for −1 < ν < −12 requires considerably more restrictive conditions on f, and the same


![image 12](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile12.png>)

remark holds for uniform convergence of (Hν,τf − f)wν for ν > −12. This can be traced back to the fact that the series Gν,τ(1/wν) and Hν,τ(1/wν) do not minorize 1/wν for these choices of ν.

![image 13](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile13.png>)

A second candidate for Lν,τ comes from the observation that the space of entire functions F of exponential type τ with F L2(wν) < ∞ is a reproducing kernel Hilbert space. Denoting by Kν,τ(w,z) the reproducing kernel, it follows from de Branges [3, Theorem 22] that

A2ν(τz) A′ν(t)2(τz − t)2

Kν,τ(τ−1t,τ−1t)

, (7)

Kν,τ(¯z,z) =

![image 14](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile14.png>)

t∈Tν

leading to a version of Theorem 1 with less general assumptions.

An identity analogous to (7) holds for every weight w with the property that evaluation functionals are bounded on B2(τ,w). In particular, reproducing kernels enable us to deal with weights of the form w(x) = |W(x)|−2 where W is a Hermite-Biehler entire function of exponential type. Since the corresponding statements require some notation from the theory of de Branges spaces, we give it as Theorem 2 in Section 5.

2. Notation and Bessel function estimates

Throughout this article cν,Cν denote unspeciﬁed positive constants depending only on ν. (Their value may change between lines.) We use the notation f(x,τ) ≃ν g(x,τ) to mean that f(x,τ) ≤ cνg(x,τ) and g(x,τ) ≤ Cνf(x,τ) for all x and τ.

For λ ≥ 0 and complex z we denote by gλ the Gaussian gλ(z) = e−πλz2.

Bessel functions satisfy Jν2(x) + Jν2+1(x) ≃ν x−1 for |x| ≥ 1. Hence for real x

1 if |x| ≤ 1, |x|−2ν−1 if |x| ≥ 1.

A2ν(x) + Bν2(x) ≃ν

A direct calculation gives A′ν(z) = −Γ(ν + 1)(z/2)−νJν+1(z) A′′ν(z) =

2νΓ(ν + 1) z2+ν

(2ν + 4ν2 − z2)Jν(z) − z(1 + 2ν)Jν−1(z)

![image 15](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile15.png>)

and this gives |A′ν(t)| ≃ν |t|−ν−21 and |A′′ν(t)| ≃ν |t|−ν−23 for t ∈ Tν. Analogous statements hold for Bν and its derivatives, and they lead to the same bounds for Bν′ (u) and Bν′′(u) when u ∈ Tν+1. These estimates are used repeatedly in the calculations below.

![image 16](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile16.png>)

![image 17](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile17.png>)

3. The case ν > −12

![image 18](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile18.png>)

- 3.1. Extremal minorants. We review the construction of extremal minorants from [2]. In view of (12) below, we start by constructing entire minorants of exponential type τ of the Gaussian gλ with nodes at the zeros of Aν. It was observed in [2] that this can be achieved by ﬁrst constructing a minorant of type zero of the exponential e−λz at zeros of Aν(√z) (see (10) below) and then substituting z  → z2. In [2] the integration in λ is performed on the Fourier transform side to get maximum generality, but since we require L∞ estimates, we integrate the minorants directly. (The error estimates in Lemma 2 are not contained in [2].)


![image 19](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile19.png>)

Since the derivative of a minorant of 1/wν must interpolate the derivative

of 1/wν at any interpolation point, we consider A2ν in the following. We have

2

∞

z2 ην,j2

A2ν(z) =

1 −

![image 20](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile20.png>)

j=1

where 0 < ην,1 < ην,2 < ... are the positive zeros of Jν. It is known that

ην,j−2 < ∞. Since A2ν is even, the function Fν deﬁned by A2ν(z) = Fν(z2) is entire, nonnegative on R, and has only positive (double) zeros zj = ην,j2 .

We have Fν(0) = 1 and

∞

zj−1 < ∞.

j=1

It follows from the theory of Polya-Laguerre entire functions (e.g., [6, Ch. III Corollary 5.4 and Ch. V Corollary 3.1]) that gν deﬁned for real t by

i∞

etz Fν(z)

- 1

![image 21](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile21.png>)

- 2πi


gν(t) =

dz (8)

![image 22](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile22.png>)

−i∞

is nonnegative, equal to zero on [0,∞), and satisﬁes for ℜz < z1 the inversion formula

0

1 Fν(z)

e−ztgν(t)dt. The inversion formula can be put in the form

=

![image 23](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile23.png>)

−∞

λ

e−ztgν(t − λ)dt (9)

e−λz = Fν(z)

−∞

in ℜz < z1, and since gν ≥ 0 on R it follows that the entire function Aλ,ν deﬁned by

λ

e−wzgν(w − λ)dw (10)

Aλ,ν(z) = e−λz − Fν(z)

0

satisﬁes Aλ,ν(x) ≤ e−λx for all real x. Evidently Aλ,ν(x) = e−λx at the zeros of F. Hence, z  → Aπλ,ν(z2) is a minorant of gλ on R that interpolates gλ at the points of Tν. To simplify notation in the following we set

1 4

- 3

![image 24](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile24.png>)

- 4


ην,2 1, ξ2 =

ην,2 1.

ξ1 =

![image 25](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile25.png>)

- Lemma 1. Let λ > 0 and ν > −12. There exists cν > 0 with the following property.


![image 26](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile26.png>)

- (a) For all complex z

e−λz − Aλ,ν(z) ≤ cν|Fν(z)|

e−λξ1 − e−λℜz ℜz − ξ1

![image 27](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile27.png>)

.

- (b) In the half plane ℜz ≤ 21ην,2 1 |Aλ,ν(z)| ≤ cν|Fν(z)|e−λξ2.


![image 28](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile28.png>)

Moreover, the function z  → Aλ,ν(z2) has exponential type 2.

Proof. Combining the properties of gν above with [6, Ch. V Theorem 2.1] implies that for every ξ ∈ (0,ην,2 1) there exists cξ > 0 with

gν(t) = 0 for t > 0, 0 ≤ gν(t) ≤ cξ exp(ξt) for t < 0.

(11)

Applying (11) with ξ = ξ1 in (10) gives for every complex z

λ

e−wℜz+ξ1(w−λ)dw and (a) follows.

Aλ,ν(z) − e−λz ≤ cξ1|Fν(z)|

0

Let now ℜz < ξ2. We replace the term e−λz in (10) by (9), combine the integrals, apply (11) with ξ = ξ2, and obtain

0

e(w−λ)(ξ2−ℜz)dw.

|Aλ,ν(z)| ≤ cξ2|Fν(z)|

−∞

After evaluation of the integration we further restrict to ℜz ≤ 21ην,2 1 which leads to (b). Moreover, since e−λz is bounded in ℜz ≥ 12ην,2 1, combining (a) with (b) shows that |Aλ,ν|/(1 + |Fν|) is bounded in C by a constant (which may depend on λ and ν). After substituting z  → z2 the ﬁnal statement of the lemma follows since Aν has exponential type 1.

![image 29](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile29.png>)

![image 30](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile30.png>)

For functions that are subordinated to the Gaussian gλ(z) = e−πλz2, minorants can now be obtained by integrating an appropriate measure in λ. We use this to construct an approximation to 1/wν. The measure is obtained by noting that for ν > −12 and (real) x = 0

![image 31](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile31.png>)

∞

|x|−2ν−1 = πν+21Γ ν + 12 −1

gλ(x)λν−12dλ. (12)

![image 32](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile32.png>)

![image 33](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile33.png>)

![image 34](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile34.png>)

0

It follows from Lemma 1 that in the range ℜ(z2) ≤ 21ην,2 1 the integral (in λ) of Aπλ,ν(z2) with respect to the measure from (12) is convergent, while in the range ℜ(z2) ≥ 21ην,2 1 the same is true for the integral of Aπλ,ν(z2)−gλ(z). Since gλ is also integrable in the latter region with respect to this measure, the function z  → Lν(z) deﬁned by

![image 35](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile35.png>)

![image 36](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile36.png>)

∞

Lν(z) = πν+12Γ(ν + 21)

Aπλ,ν(z2)λν−12dλ

![image 37](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile37.png>)

![image 38](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile38.png>)

![image 39](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile39.png>)

0

is entire and a minorant of |x|−2ν−1 that interpolates this function at the zeros of Aν. Furthermore, investigating the bounds obtained from Lemma 1(a) in ℜz ≥ 14ην,2 1 and Lemma 1(b) in ℜz ≤ 41ην,2 1 shows that Lν has exponential type 2. To obtain a minorant of type 2τ, we deﬁne

![image 40](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile40.png>)

![image 41](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile41.png>)

Lν,τ(z) = τ2ν+1Lν(τz).

- Lemma 2. Let ν > −12 and τ > 0. There exists cν > 0 so that for real x


![image 42](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile42.png>)

0 ≤ |x|−2ν−1 − Lν,τ(x) ≤ cνA2ν(τx)|x|−2ν−1 − 12τ−1ην,1 −2ν−1 1 4ην,2 1 − τ2x2

![image 43](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile43.png>)

.

![image 44](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile44.png>)

![image 45](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile45.png>)

For (real) |x| ≤ √12τ−1ην,1 we also have 0 ≤ Lν,τ(x) ≤ cνA2ν(τx) η2ν,τ1 −2ν−1 .

![image 46](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile46.png>)

![image 47](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile47.png>)

![image 48](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile48.png>)

Proof. These estimates follow by setting z = x2 in Lemma 1, integrate with respect to λ against the measure from (12) to get the bounds for τ = 1, multiply by τ2ν+1 and substitute x  → τx.

- Lemma 3. Let ν > −21 and τ > 0. The identity


![image 49](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile49.png>)

A2ν(τz) A′ν(t)2(τz − t)2 holds for all complex z.

|τ−1t|−2ν−1

Lν,τ(z) =

![image 50](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile50.png>)

t∈Tν

Proof. It follows from Lemma 1(a) that x  → Aπλ,ν(x2) is in L1(wν). The entire function Eν = Aν − iBν is Hermite-Biehler, that is, the inequality |E(z)| > |E(¯z)| holds for all ℜz > 0 (cf. de Branges [3, Section 50]). It follows that z  → Aπλ,ν(z2) satisﬁes the assumptions of Gonc¸alves [5, Theorem 1], see in particular the discussion of homogeneous spaces in [5, Section 4.1]. In place of Eν we use iEν (which is also Hermite-Biehler) and obtain an interpolation series at the zeros of Aν.

The minorant property implies that gλ(z)−Aπλ,ν(z2) must have derivative equal to zero at z = t ∈ Tν. Hence we obtain

A′′ν(t) A′ν(t)

A2ν(z) A′ν(t)2(z − t)2

Aπλ,ν(z2) =

(z − t)

1 −

gλ(t)

![image 51](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile51.png>)

![image 52](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile52.png>)

t∈Tν

(13)

A2ν(z) A′ν(t)2(z − t)

+ g′λ(t)

.

![image 53](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile53.png>)

Combining estimates from Section 2 with the classical fact that the zeros of Jν grow at the same rate as the positive integers allows application of Fubini to interchange summation in t and integration in λ. It follows that

Lν has a representation obtained from (13) by replacing gλ(t) and g′λ(t) with wν(t)−1 and ∂/∂t[wν(t)−1], respectively. The diﬀerential equation of the Bessel function gives

(2ν + 1)A′ν(z) + zA′′ν(z) = −zAν(z),

which implies that A′′ν(t)/A′ν(t) = −(2ν + 1)/t for t ∈ Tν. It follows that the series for Lν simpliﬁes to the right hand side of the claimed identity for τ = 1, and scaling in τ gives the general result.

- 3.2. Gru¨nwald operator. We give the proof of Theorem 1(a). Let τ > 0


and ν > −21. Since fwν ∈ L∞(R), it follows that the series deﬁning Gν,τf converges uniformly on compact subsets of C and thus deﬁnes an entire

![image 54](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile54.png>)

function. Since the diﬀerence of consecutive zeros of Aν is ≃ν 1 we see that |Gν,τf(z)| ≤ cντ2|A2ν(τz)| and hence Gν,τf has exponential type 2τ. (For |ℑz| ≤ 1 we use a contour integral of (u−z)−1Gν,τf(u) over a rectangle with vertical sides through zeros of Aν that are at least distance 1 away from z.)

Let ε > 0. By assumption there exists δ > 0 so that for |x − y| < δ and |u| < δ

|f(y)wν(y) − f(x)wν(x)| < ε |f(u)wν(u)| < ε.

(14)

The identity (6) takes the form Gν,τ(x) − f(x) wν(x) (15)

wν(τ−1t)−1A2ν(τx) A′ν(t)2(τx − t)2

f(τ−1t)wν(τ−1t) − f(x)wν(x)

= wν(x)

![image 55](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile55.png>)

t∈Tν

+ f(x)wν(x)(Lν,τ(x)wν(x) − 1).

We consider the sum ﬁrst and partition Tν into t with |τ−1t − x| < δ and with |τ−1t − x| ≥ δ. We observe for all τ > 0

f(τ−1t)wν(τ−1t) − f(x)wν(x) |τ−1t|−2ν−1A2ν(τx) A′ν(t)2(τx − t)2

wν(x)

![image 56](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile56.png>)

|τ−1t−x|<δ

≤ εwν(x)Lν,τ(x) ≤ ε. (16)

For the second sum we use that fwν is uniformly bounded on R (by M, say), and we obtain

f(τ−1t)wν(τ−1t) − f(x)wν(x) |τ−1t|−2ν−1A2ν(τx) A′ν(t)2(τx − t)2

wν(x)

![image 57](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile57.png>)

|τ−1t−x|≥δ

(17)

|τ−1t|−2ν−1 A′ν(t)2(τx − t)2

≤ 2Mwν(x)A2ν(τx)

![image 58](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile58.png>)

|τ−1t−x|≥δ

Combining the estimates of Section 2 with wν(x) ≤ wν(1/τ) for |x| ≤ 1/τ gives wν(x)A2ν(τx) ≤ cνwν(1/τ) for all x and τ. Denote by t+ the zero of

- Aν greater (smaller) than t if t is positive (negative). Since 1 ≤ cν|t − t+| for all zeros of Aν, the ﬁnal expression in (17) is


|τ−1t − τ−1t+| (x − τ−1t)2 ≤

1 τ t∈T

cνM τδ

≤ cνM

(18)

![image 59](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile59.png>)

![image 60](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile60.png>)

![image 61](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile61.png>)

ν

|τ−1t−x|≥δ

where the last inequality above follows by recognizing the series as a Riemann sum for the integral of u  → (x − u)−2 on R\[x − δ,x + δ].

It remains to analyze wνf(Lν,τwν − 1). It follows from Lemma 2 that

wν(x)−1 − wν(η2ν,τ1 )−1

![image 62](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile62.png>)

|Lν,τ(x)wν(x) − 1| ≤ cνA2ν(τx)wν(x)

![image 63](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile63.png>)

ην,2 1

4 − τ2x2 which implies that Lν,τ(x)wν(x) − 1 converges to zero uniformly for |x| ≥ δ

![image 64](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile64.png>)

- as τ → ∞. For |x| ≤ δ we use 0 ≤ Lν,τwν ≤ 1. Combining this with (14),


(16), and (18) leads to limsup

(Gν,τf − f)wν ∞ < 2ε, and hence the claim of Theorem 1(a).

τ→∞

4. The case −1 < ν < −12

![image 65](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile65.png>)

- 4.1. Extremal minorants. For the construction of the minorant of 1/wν with −1 < ν < −21 only a few modiﬁcations need to be made. We have


![image 66](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile66.png>)

∞

z2 ην2+1,j

1 −

Bν(z) = z

![image 67](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile67.png>)

j=1

where 0 < ην+1,1 < ην+1,2 < ... are all positive zeros of Jν+1. We deﬁne Fν by Bν2(z) = Fν(z2), and we observe that Fν is entire, nonnegative on (0,∞), negative on (−∞,0) with a simple zero at the origin, double zeros

- at zj = ην2+1,j, and no other zeros in C. We set


−1+i∞

etz Fν(z)

- 1

![image 68](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile68.png>)

- 2πi


dz

gν(t) =

![image 69](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile69.png>)

−1−i∞

and we note that gν is nonpositive on R, equal to zero on [0,∞) and satisﬁes

(9) for ℜz < 0. Deﬁning Aλ,ν by (10), the sign of gν gives

Aλ,ν(x2) ≥ gλ(x) for real x. (Since Fν has a zero at the origin for −1 < ν < −12, the function

![image 70](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile70.png>)

- gν is bounded on t < 0, but does not converge to zero as t → −∞.) An integration by parts shows that the two-sided Laplace transform of gν′ (t) equals the reciprocal of Fν(z)/z in ℜz < ην2+1,1 (hence in particular gν′ ≥ 0), and it follows that g′ satisﬁes (11) for ξ < ην2+1,1. We set


1 4

ην2+1,1 in the following two lemmas.

ξ =

![image 71](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile71.png>)

- Lemma 4. Let −1 < ν < −21 and λ > 0. Then Aλ,ν is an entire function of exponential type 2 that satisﬁes the following growth estimates.


![image 72](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile72.png>)

- (a) For all complex z

Aλ,ν(z) − e−λz ≤

|Fν(z)| |z|

![image 73](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile73.png>)

|gν(−λ)| +

λ

0

e−wℜz+(w−λ)ξgν′ (w)dw

- (b) For ℜz ≤ 0


e−λξ |z − ξ|

|Fν(z)| |z|

|gν(−λ)| +

|Aλ,ν(z)| ≤ −

![image 74](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile74.png>)

![image 75](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile75.png>)

Proof. An integration by parts shows

λ

Fν(z) z

Fν(z) z

e−wzgν′ (w − λ)dw which gives (a). Combining with (9) gives for ℜz < ξ

Aλ,ν(z) − e−λz = −

gν(−λ) −

![image 76](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile76.png>)

![image 77](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile77.png>)

0

0

Fν(z) z −gν(−λ) +

e−ztgν′ (w − λ)dw (19)

Aλ,ν(z) =

![image 78](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile78.png>)

−∞

leading to (b). As in the proof of Lemma 1 it follows that z  → Aλ,ν(z2) is entire and has exponential type 2.

We require sharper estimates on the real line.

- Lemma 5. For −1 < ν < −12, λ > 0, and x > 0

![image 79](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile79.png>)

0 ≤ Aλ,ν(x) − e−λx ≤ cν

Fν(x) x

![image 80](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile80.png>)

1 − e−λξ ξ −

![image 81](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile81.png>)

e−λx − e−λξ ξ − x Proof. We have for x > 0

![image 82](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile82.png>)

Aλ,ν(x) − e−λx =

Fν(x) x

![image 83](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile83.png>)

0

−λ

(1 − e−x(u+λ))gν′ (u)du. An application of (11) for g′ gives the upper inequality.

The identity |x|−2ν−1 = πν+12

![image 84](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile84.png>)

−Γ ν + 12 −1

![image 85](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile85.png>)

∞

0

(1 − gλ(x))λν−12dλ, (20)

![image 86](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile86.png>)

valid for −1 < ν < −21 and (real) x = 0, suggests the deﬁnition Lν(z) = πν+12

![image 87](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile87.png>)

![image 88](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile88.png>)

−Γ ν + 21 −1

![image 89](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile89.png>)

∞

0

(1 − Aπλ,ν(z2))λν−12dλ, and as before, Lν,τ(z) = τ2ν+1Lν(τz).

![image 90](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile90.png>)

- Lemma 6. Let −1 < ν < −12. The integral deﬁning Lν converges uniformly on compact subsets of C and is an entire function of exponential type 2. We have for real x


![image 91](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile91.png>)

0 ≤ |x|−2ν−1 − Lν,τ(x) ≤

|x|−2ν−1 − |21τ−1ην+1,1|−2ν−1 1 4ην2+1,1 − τ2x2

|12τ−1ην+1,1|−2ν−1 1 4ην2+1,1 −

Bν2(τx) (τx)2

![image 92](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile92.png>)

![image 93](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile93.png>)

.

![image 94](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile94.png>)

![image 95](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile95.png>)

![image 96](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile96.png>)

![image 97](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile97.png>)

![image 98](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile98.png>)

Proof. Writing gν(−λ) as an integral of its derivative on [−λ,0] and observing the growth estimates for gν′ shows that gν(−λ)λν−21 is integrable on [0,∞). Similarly, the integral in Lemma 4(a) is integrable with respect to λν−21dλ, which gives the ﬁrst part of the lemma. This also gives the necessary estimates in ℜz ≥ −1 to show the claimed exponential growth in this half plane.

![image 99](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile99.png>)

![image 100](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile100.png>)

Let ℜz ≤ −1. Equation (19) combined with the inversion formula for gν,τ′ gives

0

Fν(z) z

e−zt gν′ (w) − gν′ (w − λ) dw .

gν(−λ) +

1 − Aλ,ν(z) =

![image 101](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile101.png>)

−∞

Since gν′ (w −λ)−gν′ (w) = O(1−eλw), the integral can be integrated in λ with respect to the measure λν−21dλ, and the growth estimates in ℜz ≤ −1 follow as above. We leave the details to the reader. The minorant property follows from Aλ,ν(x2) ≥ Gλ(x) and Γ(ν + 12) < 0.

![image 102](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile102.png>)

![image 103](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile103.png>)

The last inequality of the lemma follows by integrating the inequality of Lemma 5 in λ, substituting x2 for x, observing (20), and scaling by τ.

- Lemma 7. Let −1 < ν < −12 and τ > 0. The identity


![image 104](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile104.png>)

Bν2(τz) Bν′ (t)2(τz − t)2 holds for all complex z.

|τ−1t|−2ν−1

Lν,τ(z) =

![image 105](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile105.png>)

t∈Tν+1

Proof. Denote by Γt the square in C with center at the origin and sides through ±t. Since −1 < ν < −21, it follows that 1/Bν(t) → 0 if |t| → ∞ through the points t with Jν(t) = 0. Moreover, for ﬁxed t we have 1/|Bν(t + iy)| ≤ 1/|Bν(t)|, and we have 1/|Bν(x + iy)| → 0 uniformly in x as |y| → ∞. Integrating (w − z)−1Bν−2(w) in w over Γt with t ∈ Tν+1, applying the residue theorem, and letting |t| → ∞ shows that the regular part in the representation of 1/Bν2 obtained from the Mittag-Leﬄer theorem is equal to zero.

![image 106](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile106.png>)

We combine this with the fact from [5] that the function z  → Aλ,ν(z2) has an analogous representation to (13) with Tν replaced by Tν+1 ∪{0} (this set contains the zeros of Bν) and Aν replaced by Bν. It follows that

Bν′′(t) Bν′ (t)

Bν2(z) Bν′ (t)2(z − t)2

- 1 − Aπλ,ν(z2) = t∈Tν+1


(z − t)

1 −

(1 − gλ(t))

![image 107](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile107.png>)

![image 108](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile108.png>)

Bν2(z) Bν′ (t)2(z − t)

− g′λ(t)

. (21)

![image 109](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile109.png>)

The remaining steps utilize the diﬀerential equation

ν2 − (ν + 1)2 z2

2ν + 1 z

Bν′′(z) +

Bν′ (z) + 1 +

Bν(z) = 0 and proceed analogously to the proof of Lemma 3.

![image 110](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile110.png>)

![image 111](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile111.png>)

4.2. Gru¨nwald operator. The proof of Theorem 1(b) proceeds completely analogously to the arguments in Section 3.2 by replacing Tν with Tν+1, the function Aν by Bν, observing nonnegativity of Lν,τ from Lemma 7, and estimating fwν(Lν,τwν − 1) using Lemma 6. We omit the details.

5. De Branges spaces For 1 ≤ p ≤ ∞ we denote by Hp(C+) the space of analytic functions F in

the upper half plane C+ for which supy>0 F(.+iy) p is ﬁnite. We require a few facts from the theory of de Branges spaces. For a more complete picture we refer to de Branges [3] for p = 2 and Baranov [1] for arbitrary p.

An entire function E satisfying |E(z)| > |E(¯z)| (22)

for ℑz > 0 will be called a Hermite-Biehler function. Throughout this article we assume that E has no real zeros. We set

Hp(E) = {F entire : F/E,F∗/E ∈ Hp(C+)},

![image 112](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile112.png>)

where F∗ is the entire function F∗(z) = F(¯z), and the norm is given by F  → F/E p. We write E = A − iB with real entire A = 2−1(E + E∗) and

- B = 2−1i(E − E∗), and we denote by TA the set of zeros of A. These are necessarily real by (22). We denote by KE the function


A(w¯)B(z) − A(z)B(w¯) π(z − w¯)

KE(w,z) =

, (23) and we observe that z  → KE(w,z) is an entire function in Hp(E) for all

![image 113](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile113.png>)

- w ∈ C and p ∈ [0,∞]. The Cauchy integral formula for the upper half plane and the alternative representation KE(w,z) = [2πi(z − w¯)]−1(E( ¯w)E∗(z) − E(z)E∗( ¯w)) may be used to check that KE(w,z) is the reproducing kernel for H2(E). A function ϕE with the property E(x)eiϕE(x) ∈ R for all real
- x is called a phase of E. As a consequence of (22) it may be chosen to be analytic on an open set containing the real line.


If B2(τ,w) has bounded evaluation functionals, then by [3, Theorem 23] it is isometrically equal to a space H2(E).

Let f be continuous and f|E|−2 ∈ L∞(R). We deﬁne the formal series GEf by

A2(z) A′(t)2(z − t)2

.

GEf(z) =

f(t)

![image 114](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile114.png>)

t∈TA

In the following {Eτ : τ > 0} is a collection of Hermite-Biehler functions Eτ of exponential type τ. We set Gτf = GEτf, Tτ = TAτ, and ϕτ = ϕEτ if the choice of Eτ is clear from the context. We consider f with the following properties.

- (a) For every ε > 0 there exists δ > 0 and τ0 > 0 such that for all x,t ∈ R and all τ ≥ τ0

|x − t| < δ =⇒

f(x) |Eτ(x)|2

![image 115](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile115.png>)

−

f(t) |Eτ(t)|2

![image 116](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile116.png>)

< ε (24)

- (b) There exists M > 0 so that for all x ∈ R and positive τ f(x)


≤ M (25)

![image 117](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile117.png>)

|Eτ(x)|2

If |Eτ|−2 converges to w uniformly in x as τ → ∞, then these conditions may be reformulated in terms of uniform continuity and uniform boundedness of fw.

Theorem 2. Let Eτ, τ > 0, be a Hermite-Biehler entire function of exponential type τ without real zeros, and such that there exists C > 0 so that

|ϕ′τ(x) − τ| ≤ C for all x and τ.

- (a) If f : R → C satisﬁes (24) and (25), then Gτ converges uniformly on compact sets, Gτ ∈ H∞(Eτ2) and

lim

τ→∞

(Gτf − f)Eτ−2 ∞ = 0.

- (b) If in addition there exists constants c > 0,d > 0 with c ≤ |Eτ(x)|2w(x) ≤ d


for all real x and τ ≥ τ0, then lim

(Gτf − f)w ∞ = 0.

τ→∞

Proof. Let ε > 0,δ > 0,τ0 > 0 as in (24). We apply [3, Theorem 22] with iE in place of E to z  → Kτ(x,z) with x ∈ R to obtain

|Kτ(x,t)|2 Kτ(t,t)

Kτ(x,x) = Kτ(x,.)/E 22 =

.

![image 118](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile118.png>)

t∈Tτ

Equation (23) leads to

A2τ(x) A′τ(t)2(x − t)2

Kτ(t,t)

Kτ(x,x) =

. (26)

![image 119](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile119.png>)

t∈Tτ

It follows that

Kτ(t,t)A2τ(x) A′τ(t)2(x − t)2

f(x) − Gτ(x) Kτ(x,x)

f(x) Kτ(x,x) −

1 Kτ(x,x) t∈T

f(t) Kτ(t,t)

=

.

![image 120](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile120.png>)

![image 121](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile121.png>)

![image 122](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile122.png>)

![image 123](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile123.png>)

![image 124](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile124.png>)

τ

We recall the identity πKτ(x,x) = ϕ′τ(x)|Eτ(x)|2 from [3, Problem 48]. In the range |x − t| ≥ δ we use πKτ(t,t)A′τ(t)−2 = (πϕ′τ(t))−1 ≤ cτ−1. In the range |x − t| < δ we add and subtract f(t)(ϕ′τ(x)|Eτ(t)|2)−1 and use |ϕ′τ(x)−1 − ϕ′τ(t)−1| ≤ cτ−2 with c independent of t and x. Since the values in Tτ are the points where Eτ is purely imaginary we have π = ϕτ(t)−ϕτ(s) for consecutive s,t ∈ Tτ, and the mean value theorem gives τ−1 ≤ c(s − t). With these estimates (a) can be proved analogous to (16), (17) and (18), and we leave the details to the reader. Statement (b) is an immediate consequence.

Let τ ≥ τ0 ≥ 0, and assume that W is a Hermite-Biehler entire function of exponential type τ0. Deﬁne Eτ(z) = e(τ−τ0)zW(z) and real entire Aτ,α,Bτ,α

by eiαEτ = Aτ,α − iBτ,α. Deﬁne formal series Gτ,αf by

A2τ,α(z) A′τ,α(t)2(z − t)2

,

f(t)

Gτ,αf(z) =

![image 125](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile125.png>)

t∈Tτ,α

where Tτ,α is the set of (real) zeros of Aτ,α. A direct consequence of Theorem

- 2 is the following statement.


Corollary 1. Let f|W|−2 ∈ L∞(R) be uniformly continuous. Then Gτ,αf deﬁnes an entire function of exponential type 2τ, and

(Gτ,αf − f)|W|−2 ∞ = 0. This corollary includes for example the Poisson measure dx/(1 + x2).

lim

τ→∞

We ﬁnally describe some open questions. It would be of interest to have a characterization of those entire functions that may be used in place of Aτ and give uniform convergence of the corresponding Gru¨nwald operator, but even for simple measures this seems out of reach. We consider the concrete example w(x) = x2 + 1. First, for the Hermite-Biehler entire function

Eτ(z) =

2 sinh(2τ)

![image 126](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile126.png>)

- 1

![image 127](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile127.png>)

- 2 sin(τ(z + i))


![image 128](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile128.png>)

z + i

we observe that tanh(τ) ≤ (x2 + 1)|Eτ(x)|2 ≤ coth(τ). Since Kτ(x,x) =

1 π

1

τ (x2 + 1)|Eτ(x)|2

x2 + 1 |Eτ(x)|2, we obtain

−

![image 129](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile129.png>)

![image 130](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile130.png>)

![image 131](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile131.png>)

sinh(2τ) cosh(2τ) − cos(2τx) −

1 x2 + 1

ϕ′(x) = τ

,

![image 132](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile132.png>)

![image 133](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile133.png>)

![image 134](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile134.png>)

zcosh(τ)sin(τz) + sinh(τ)cos(τz) z2 + 1

2 sinh(2τ)

.

Aτ(z) =

![image 135](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile135.png>)

![image 136](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile136.png>)

(27)

Hence for f with fw ∈ L∞(R) and uniformly continuous on R the interpo-

lation series GEτf satisﬁes (GEτf −f)w ∞ → 0. This is true in particular for f = 1/w.

On the other hand, it can be shown that starting with an even PolyaLaguerre function A of exponential type 1 with A(0) = 1, A′(t) ≤ C/t and |s − t| ≥ D > 0 for all zeros s,t of A the dilation Aτ(z) = A(τz) has the property that GAτ(1/w)(0) → ∞ as τ → ∞. In particular, using the dilation E1(τz) in place of (27) fails to give a uniformly converging interpolation.

In contrast, Aτ(z) = cos(τz) has the property that (GAτf −f)w ∞ → 0 as τ → ∞ for f with fw ∈ L∞(R) that is uniformly continuous on R; the series

cos2(τz) τ2(z − t)2

1 t2 + 1

GAτw−1(z) =

![image 137](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile137.png>)

![image 138](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile138.png>)

cos(τt)=0

has a closed form that may be used to show w(x)GAτ w−1(x) = 1+τ−1pτ(x) with |pτ(x)| ≤ 2 for real x, which allows an argument analogous to the proofs of Theorems 1 and 2.

References

- 1. A. D. Baranov, On estimates for the Lp-norms of derivatives in spaces of entire functions, J. Math. Sci. 129 (2005), no. 4, 3927 – 3943. MR 2037529
- 2. E. Carneiro and F. Littmann, Extremal functions in de Branges and Euclidean spaces, II, Amer. J. Math. 139 (2017), no. 2, 525–566. MR 3636639
- 3. L. de Branges, Hilbert spaces of entire functions, Prentice-Hall, Inc., Englewood Cliﬀs, N.J., 1968. MR 0229011
- 4. R. Gervais, Q. I. Rahman, and G. Schmeisser, Simultaneous interpolation and approximation by entire functions of exponential type, Numerische Methoden der Approximationstheorie, Band 4 (Meeting, Math. Forschungsinst., Oberwolfach, 1977), Internat. Schriftenreihe Numer. Math., vol. 42, Birkh¨auser, Basel-Boston, Mass., 1978, pp. 145–

153. MR 527101

- 5. F. Gonc¸alves, Interpolation formulas with derivatives in de Branges spaces, Trans. Amer. Math. Soc. 369 (2017), no. 2, 805–832. MR 3572255
- 6. I. I. Hirschman and D. V. Widder, The convolution transform, Princeton University Press, Princeton, N. J., 1955. MR 0073746
- 7. A.´ P. Horva´th, Weighted Hermite-Fej´er interpolation on the real line: L∞ case, Acta Math. Hungar. 115 (2007), no. 1-2, 101–131. MR 2316624
- 8. D. S. Lubinsky, Hermite and Hermite-Fej´er interpolation and associated product integration rules on the real line: the L∞ theory, J. Approx. Theory 70 (1992), no. 3, 284–334. MR 1178375
- 9. J. Szabados, Weighted Lagrange and Hermite-Fej´er interpolation on the real line, J. Inequal. Appl. 1 (1997), no. 2, 99–123. MR 1731425
- 10. , On some problems of weighted polynomial approximation and interpolation, New developments in approximation theory (Dortmund, 1998), Internat. Ser. Numer. Math., vol. 132, Birkh¨auser, Basel, 1999, pp. 315–328. MR 1724926

![image 139](<2020-littmann-weighted-uniform-convergence-entire_images/imageFile139.png>)

- 11. J. Szabados and P. Ve´rtesi, Interpolation of functions, World Scientiﬁc Publishing Co., Inc., Teaneck, NJ, 1990. MR 1089431
- 12. V. E. S. Szab´o, Weighted interpolation: the L∞ theory. I, Acta Math. Hungar. 83


(1999), no. 1-2, 131–159. MR 1682908 North Dakota State University, Department of Mathematics, Fargo, ND

58108-6050 Email address: Friedrich Littmann@ndsu.edu Dakota State University, The Beacom College of Computer and Cyber

Science, Madison, SD 57042 Email address: Mark.Spanier@dsu.edu

