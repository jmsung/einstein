arXiv:1701.00265v2[math.NT]14Feb2020

FOURIER INTERPOLATION ON THE REAL LINE

DANYLO RADCHENKO AND MARYNA VIAZOVSKA

Abstract. In this paper we construct an explicit interpolation formula for Schwartz functions on the real line. The formula expresses the value of a function at any given point in terms of the values of the function and its Fourier transform on the set {0,±

√3,...}. The functions in the interpolating basis are constructed in a closed form as an integral transform of weakly holomorphic modular forms for the theta subgroup of the modular group.

√2,±

√1,±

![image 1](<2017-radchenko-fourier-interpolation-real-line_images/imageFile1.png>)

![image 2](<2017-radchenko-fourier-interpolation-real-line_images/imageFile2.png>)

![image 3](<2017-radchenko-fourier-interpolation-real-line_images/imageFile3.png>)

1. Introduction Let f : R → R be an integrable function and let f be the Fourier transform of f: f(ξ) =

∞

f(x)e−2πiξxdx.

−∞

The classical Whittaker-Shannon interpolation formula (see [19], [15]) states that if the Fourier transform f is supported in [−w/2, w/2], then

- (1) f(x) =

n∈Z

f(n/w) sinc(wx − n),

where sinc(x) = sin(πx)/(πx) is the cardinal sine function. In other words, the functions sn(x) = sinc(wx − n) form an interpolation basis on the set w1 Z for the space of functions whose Fourier transform is supported in [−w/2, w/2] (the so-called PaleyWiener space PWw). For a nice overview of history of the Whittaker-Shannon formula, its generalizations and other related results, see [7].

![image 4](<2017-radchenko-fourier-interpolation-real-line_images/imageFile4.png>)

Note that it is not possible to apply the Whittaker-Shannon formula directly to functions whose Fourier transform f has unbounded support, say, to f(x) = exp(−πx2). The main goal of this paper is to prove an interpolation formula that can be applied to arbitrary Schwartz functions on the real line.

- Theorem 1. There exists a collection of even Schwartz functions an: R → R with the property that for any even Schwartz function f : R → R and any x ∈ R we have


- (2) f(x) =


∞

∞

an(x)f(√n) +

an(x) f(√n),

![image 5](<2017-radchenko-fourier-interpolation-real-line_images/imageFile5.png>)

![image 6](<2017-radchenko-fourier-interpolation-real-line_images/imageFile6.png>)

n=0

n=0

where the right-hand side converges absolutely. As immediate corollary of Theorem 1, we get the following. Corollary 1. Let f : R → R be an even Schwartz function that satisﬁes

f(√n) = f(√n) = 0, n ∈ Z≥0. Then f vanishes identically.

![image 7](<2017-radchenko-fourier-interpolation-real-line_images/imageFile7.png>)

![image 8](<2017-radchenko-fourier-interpolation-real-line_images/imageFile8.png>)

Denote by s the vector space of all rapidly decaying sequences of real numbers, i.e., sequences (xn)n≥0 such that for all k > 0 we have nkxn → 0, n → ∞. If we denote

1

by Seven the space of even Schwartz functions on R (see Section 6 for a formal deﬁnition), then there is a well-deﬁned map Ψ: Seven → s ⊕ s given by

Ψ(f) = (f(√n))n≥0 ⊕ ( f(√n))n≥0.

![image 9](<2017-radchenko-fourier-interpolation-real-line_images/imageFile9.png>)

![image 10](<2017-radchenko-fourier-interpolation-real-line_images/imageFile10.png>)

Together with Theorem 1 the following result gives a complete description of what values an even Schwartz function and its Fourier transform can take at ±

√n for n ≥ 0.

![image 11](<2017-radchenko-fourier-interpolation-real-line_images/imageFile11.png>)

- Theorem 2. The map Ψ is an isomorphism of the space of even Schwartz functions onto the vector space ker L ⊂ s ⊕ s, where L: s ⊕ s → R is the linear functional


yn2.

xn2 −

L((xn)n≥0, (yn)n≥0) =

n∈Z

n∈Z

In the proof of Theorem 1 we will give an explicit construction of the interpolating basis {an(x)}n≥0. For instance, the Fourier invariant part of an will be given by

1

2zdz,

gn(z) eiπx

an(x) + an(x) =

−1

where gn is a certain weakly holomorphic modular form of weight 3/2, and the integral is over a semicircle in the upper half-plane. The anti-invariant part an(x) − an(x) will be deﬁned by a similar expression. For an explicit example, we deﬁne a0(x) by

1

1 4

2zdz, where θ(z) is the classical theta series

θ3(z) eiπx

a0(x) =

![image 12](<2017-radchenko-fourier-interpolation-real-line_images/imageFile12.png>)

−1

- (3) θ(z) =

n∈Z

eiπn

2z.

The modular transformation property of gn is chosen in such a way that it complements the action of the Fourier transform on Gaussian functions:

ez(ξ) =

1 √

![image 13](<2017-radchenko-fourier-interpolation-real-line_images/imageFile13.png>)

![image 14](<2017-radchenko-fourier-interpolation-real-line_images/imageFile14.png>)

−iz

e−1/z(ξ),

where ez(x) = eiπzx2, and the square root is chosen to be positive when z lies on the imaginary axis (this comment also applies whenever expression (−iz)α occurs throughout the paper; note that z belongs to the upper half-plane). For instance, using the identity

θ −

1 z

![image 15](<2017-radchenko-fourier-interpolation-real-line_images/imageFile15.png>)

= √

![image 16](<2017-radchenko-fourier-interpolation-real-line_images/imageFile16.png>)

−iz θ(z)

and applying the change of variable z  → −1/z in the integral that deﬁnes a0(x) we see that a0 = a0. The general deﬁnition of an needs some preparation and will be given in Section 4. The plots of the ﬁrst three functions are shown in Figure 1.

An analogue of Theorem 1 holds also for odd Schwartz functions, but we postpone its formulation until Section 7. It is possible to combine the two results into a general interpolation theorem, but it is more convenient to work with the two cases separately.

Remark. Another way to interpret equation (2) is to think of it as a “deformation” of the classical Poisson summation formula

- (4)


f(n),

f(n) =

n∈Z

n∈Z

which will be a special case of (2) for x = 0 (more precisely, −an2(0) = an2(0) = 1 for n ≥ 1, a0(0) = a0(0) = 1/2, and all other values are zero). Note also that equation (2) gives a continuous family of measures µx such that µx is a tempered distribution, and

1

1

2 a0

- a1

- a2


0 1 √2 √3 2a0

0 1 √2 √3

![image 17](<2017-radchenko-fourier-interpolation-real-line_images/imageFile17.png>)

![image 18](<2017-radchenko-fourier-interpolation-real-line_images/imageFile18.png>)

![image 19](<2017-radchenko-fourier-interpolation-real-line_images/imageFile19.png>)

![image 20](<2017-radchenko-fourier-interpolation-real-line_images/imageFile20.png>)

- a1

- a2


Figure 1. Plots of an and an for n = 0, 1, 2.

both µx and µx have locally ﬁnite support. Such measures are called crystalline measures, for general discussion and some interesting examples see [11], [8].

Our general approach ﬁts into the framework of Eichler cohomology (see [6]; some relevant results can also be found in [9] and [10]) but for the most part we avoid using its general results and terminology. In our case we prefer to obtain explicit estimates by direct methods, and this also allows us to keep the proofs relatively self-contained.

Let us also remark that functions with properties similar to that of an have recently been used in [17] and [3] to solve the sphere packing problem in dimensions 8 and 24. The functions constructed there, motivated by the Cohn-Elkies optimization problem [2], were also solutions to a very special case of an interpolation problem closely related to (2) that also involved the values of the ﬁrst derivative. Similarly, in the Paley-Wiener space, an analogue of (1) for second-order interpolation (i.e., interpolation of values of the function and the values of its ﬁrst derivative) plays important role in optimization problems of Beurling and Selberg, see [16].

The paper is organized as follows. In Section 2 we recall some known facts about modular forms for the theta group Γθ. In Section 3 we compute an explicit basis of a certain space of weakly holomorphic modular forms of weight 3/2 for the group Γθ. Then, in Section 4 we use these modular forms to construct an interpolation basis for the even Schwartz functions and prove some of its properties. In the next section we prove an estimate on the growth of this sequence functions; this is by far the most technical part of the paper. In Section 6 we prove the main result for even functions, and in Section 7 we deﬁne the interpolation basis and formulate corresponding statements for the odd functions.

Acknowledgements. The authors would like to thank Max Planck Institute for Mathematics, Bonn for hospitality and support while this paper was being written. The ﬁrst named author would like to thank The Absus Salam International Centre for Theoretical Physics, Trieste for ﬁnancial support. The second named author would also like to thank the Berlin Mathematical School for ﬁnancial support and excellent research environment.

The authors are grateful to Andrew Bakan, Andriy Bondarenko, Emanuel Carneiro, Yves Meyer, Don Zagier, and the anonymous referee for many helpful remarks and comments. The second named author is grateful to Andriy Bondarenko for sharing his conjecture about the existence of the interpolation formula.

2. The theta group

In this section we set up notation and collect facts about the theta group and related modular forms. Most of the material from this section can be found, in much greater detail, in [13]. For a motivated general introduction to the theory of modular forms, see [21].

- 2.1. Upper half-plane and the action of SL2(R). Denote by H the complex upper half-plane {z ∈ C : Im(z) > 0}. The group SL2(R) of 2×2 matrices with real coeﬃcients and determinant 1 acts on the upper half-plane on the left by Moebius transformations


γz =

az + b cz + d

, γ =

![image 21](<2017-radchenko-fourier-interpolation-real-line_images/imageFile21.png>)

a b c d ∈ SL2(R).

The kernel of this action coincides with the center {±I} of SL2(R) and thus we can work with the action of PSL2(R) = SL2(R)/{±I} instead.

We will use special notation for the following elements of SL2(Z) (or, by abuse of notation, of PSL2(Z)):

I =

1 0 0 1

, T =

1 1 0 1

, S =

- 0 −1
- 1 0


.

Recall that Γ(2) ⊂ SL2(Z) is deﬁned as Γ(2) = A ∈ SL2(Z) A ≡

1 0 0 1

(mod 2) ,

and the theta group Γθ is the subgroup of SL2(Z) generated by S and T2, or, equivalently, Γθ = A ∈ SL2(Z) A ≡

1 0 0 1

- 0 1
- 1 0


or

(mod 2) .

Note the obvious inclusions SL2(Z) ⊃ Γθ ⊃ Γ(2). The group Γ(2) has three cusps 0, 1, and ∞, while the group Γθ has only two cusps: 1 and ∞. The standard fundamental domain for the theta group is (see Figure 2)

- (5) D = {τ ∈ H : |τ| > 1, Re(τ) ∈ (−1, 1)}.

Finally, we are going to use the “θ-automorphy factor” on the group Γθ, which we deﬁne for all z ∈ H and γ ∈ Γθ by

- (6) jθ(z, γ) =

θ(z) θ(γz)

![image 22](<2017-radchenko-fourier-interpolation-real-line_images/imageFile22.png>)

.

From the deﬁnition it immediately follows that jθ(z, γ1γ2) = jθ(z, γ2)jθ(γ2z, γ1), so jθ is indeed an automorphy factor on Γθ. We have jθ(z, T2) = 1 and jθ(z, S) = (−iz)−1/2, and in general we have jθ(z, ( ac db )) = ζ · (cz + d)−1/2 for some suitable 8-th root of unity ζ (an explicit expression for ζ can be found in [13, Th. 7.1]). Using this automorphy factor we deﬁne the following slash operator in weight k/2 (that acts on holomorphic functions deﬁned on the upper half-plane H)

- (7) f|k/2A (z) = jθ(z, A)kf


az + b cz + d

,

![image 23](<2017-radchenko-fourier-interpolation-real-line_images/imageFile23.png>)

D

−1 1

Figure 2. Fundamental domain for Γθ.

where A = ( ac db ) ∈ Γθ. More generally, for ε ∈ {−, +} deﬁne a slash operator |εk/2 by

- (8) f|εk/2A = χε(A)f|k/2A,

where χε: Γθ → {±1} is the homomorphism deﬁned by χε(S) = ε and χε(T2) = 1. The slash operator deﬁnes a group action, that is, f|AB = (f|A)|B. Another fact that we

will use is that for all ( ac db ) ∈ SL2(R) we have

- (9) Im

aτ + b cτ + d

![image 24](<2017-radchenko-fourier-interpolation-real-line_images/imageFile24.png>)

=

Im(τ) |cτ + d|2

![image 25](<2017-radchenko-fourier-interpolation-real-line_images/imageFile25.png>)

. For any real number a we will denote by qa the analytic function qa = qa(z) = exp(2πiaz).

Any N-periodic holomorphic function on H admits an expansion in powers of q1/N (in general as a Laurent series, but in our case such expansions will have only ﬁnitely many negative powers). We will be using subscripts to indicate the main variable of q, i.e., qτa is the same as qa(τ); by default the variable of qa is z.

- 2.2. Modular forms for the group Γθ. We begin by deﬁning the classical Jacobi theta series (the so-called Thetanullwerte):


- Θ2(z) =

n∈Z+21

![image 26](<2017-radchenko-fourier-interpolation-real-line_images/imageFile26.png>)

q

- 1

![image 27](<2017-radchenko-fourier-interpolation-real-line_images/imageFile27.png>)

- 2n2 = 2


η(2z)2 η(z)

![image 28](<2017-radchenko-fourier-interpolation-real-line_images/imageFile28.png>)

,

- Θ3(z) =

n∈Z

q

- 1

![image 29](<2017-radchenko-fourier-interpolation-real-line_images/imageFile29.png>)

- 2n2 =


η(z)5 η(z/2)2η(2z)2

![image 30](<2017-radchenko-fourier-interpolation-real-line_images/imageFile30.png>)

(= θ(z)),

- Θ4(z) =


n∈Z

(−1)nq

- 1

![image 31](<2017-radchenko-fourier-interpolation-real-line_images/imageFile31.png>)

- 2n2 =


η(z/2)2 η(z)

![image 32](<2017-radchenko-fourier-interpolation-real-line_images/imageFile32.png>)

,

where η(z) = q1/24 n≥1(1 − qn) is the Dedekind eta function. The functions Θ42, Θ43, and Θ44 generate the ring of holomorphic modular forms on Γ(2) and satisfy the Jacobi identity

- (10) Θ43 = Θ42 + Θ44.


The q-expansions of these forms at the cusp i∞ are as follows:

- Θ42(z) = 16q1/2 + 64q3/2 + 96q5/2 + O(q3),
- Θ43(z) = 1 + 8q1/2 + 24q + 32q3/2 + 24q2 + 48q5/2 + O(q3),
- Θ44(z) = 1 − 8q1/2 + 24q − 32q3/2 + 24q2 − 48q5/2 + O(q3).


Under the action of SL2(Z) the theta functions transform as follows. Under the action of S we have

- (11)

and under the action of T we have

- Θ2(z + 1) = eiπ/4Θ2(z),
- Θ3(z + 1) = Θ4(z),
- Θ4(z + 1) = Θ3(z)


- (12)

Together with the q-series for Θ2, Θ3, and Θ4, these transformations allow us to compute the q-series expansion of any expression in theta functions at any of the three cusps of Γ(2).

Using these theta functions we can deﬁne the classical modular lambda invariant

λ(z) =

- Θ42(z)

![image 33](<2017-radchenko-fourier-interpolation-real-line_images/imageFile33.png>)

- Θ43(z)


= 16q1/2 − 128q + 704q3/2 + . . . ,

which is a Hauptmodul for Γ(2). In particular, we have

λ

az + b cz + d

![image 34](<2017-radchenko-fourier-interpolation-real-line_images/imageFile34.png>)

= λ(z),

a b c d ≡

1 0 0 1

(mod 2),

and any meromorphic function with these transformation properties and with appropriate behavior at the cusps can be expressed as a rational function of λ. From (10) – (12) we see that under the action of PSL2(Z) the function λ(z) transforms as follows:

λ −

1 z

![image 35](<2017-radchenko-fourier-interpolation-real-line_images/imageFile35.png>)

= 1 − λ(z),

λ(z + 1) =

λ(z) λ(z) − 1

![image 36](<2017-radchenko-fourier-interpolation-real-line_images/imageFile36.png>)

.

- (13)

Since Θ3, Θ2, and Θ4 do not vanish in H (by the product expression in terms of η(z)), we get the well-known fact that λ(z) omits the values 0 and 1.

Using λ(z), deﬁne a Hauptmodul J for the group Γθ

- (14) J(z) =


- (−iz)−1/2Θ2(−1/z) = Θ4(z),
- (−iz)−1/2Θ3(−1/z) = Θ3(z),
- (−iz)−1/2Θ4(−1/z) = Θ2(z),


1 16

λ(z)(1 − λ(z)) =

![image 37](<2017-radchenko-fourier-interpolation-real-line_images/imageFile37.png>)

Θ42(z)Θ44(z) 16Θ83(z)

![image 38](<2017-radchenko-fourier-interpolation-real-line_images/imageFile38.png>)

= q1/2 − 24q + 300q3/2 + . . . .

Note that J(z) = η(z/2)24η(2z)24η(z)−48, hence it does not have zeros in H. This function satisﬁes the transformation laws

1 z

J −

= J(z), J(z + 2) = J(z),

![image 39](<2017-radchenko-fourier-interpolation-real-line_images/imageFile39.png>)

and it maps the fundamental domain D conformally onto the cut plane C   [1/64, +∞). Finally, note that 1/J vanishes at the cusp 1 since a simple calculation shows that

- (15)

1 J(1 − 1/z)

![image 40](<2017-radchenko-fourier-interpolation-real-line_images/imageFile40.png>)

= −4096q − 98304q2 + O(q3).

- 2.3. Asymptotic notation. We freely use the standard big O notation. In addition, we also use Vinogradov’s “≪” sign


f ≪ε,δ,... g ⇔ f = Oε,δ,...(g). Notationally, we prefer to use “O” for sequences and additive remainders, while for most inequalities with implied constants we use “≪”.

3. Weakly holomorphic modular forms on Γθ of weight 3/2

We begin by constructing a basis for a certain space of weakly holomorphic modular forms of weight 3/2. Namely, let {gn+(z)}n≥0 and {g−

n (z)}n≥1 be two collections of holomorphic functions on the upper half-plane H that satisfy the transformation properties

gnε(z + 2) = gnε(z), (−iz)−3/2gnε(−1/z) = εgnε(z),

- (16)

- as well as the following behavior at the cusps gn+(z) = q−n/2 + O(q1/2), z → i∞, gn−(z) = q−n/2 + O(1), z → i∞, gnε(1 + i/t) → 0, t → ∞.


- (17)

The reason behind these conditions will be made clear in the next section. We make the following ansatz:

gn+(z) = θ3(z)Pn+(J−1(z)), gn−(z) = θ3(z)(1 − 2λ(z))Pn−(J−1(z)),

- (18)

where P±

n ∈ Q[x] are monic polynomials of degree n and P−

n (0) = 0. The polynomials P±

n are uniquely determined by the ﬁrst two conditions in (17), since J−1 has q-expansion starting with q−1/2 + 24 + O(q1/2), and thus the coeﬃcients of P±

n can be found by inverting an upper-triangular matrix. The transformation properties (16) follow from the properties of J(z) and λ(z). The ﬁrst few of these functions are

- g0+ = θ3,
- g1+ = θ3 · (J−1 − 30),
- g2+ = θ3 · (J−2 − 54J−1 + 192),


- g1− = θ3 · (1 − 2λ) · (J−1),
- g2− = θ3 · (1 − 2λ) · (J−2 − 22J−1),
- g3− = θ3 · (1 − 2λ) · (J−3 − 46J−2 + 252J−1).


Note that the polynomials Pn+ are the Faber polynomials associated to the function 1/J, viewed as a function on the unit disk (see [4]). In the next theorem we give closed form expressions for generating functions of {g±

n }.

- Theorem 3. The generating functions for {gn+(z)}n≥0 and {g−


n (z)}n≥1 are given by

∞

- n=0

gn+(z)eiπnτ =

θ(τ)(1 − 2λ(τ))θ3(z)J(z) J(z) − J(τ)

![image 41](<2017-radchenko-fourier-interpolation-real-line_images/imageFile41.png>)

=: K+(τ, z),

∞

- n=1


gn−(z)eiπnτ =

θ(τ)J(τ)θ3(z)(1 − 2λ(z)) J(z) − J(τ)

![image 42](<2017-radchenko-fourier-interpolation-real-line_images/imageFile42.png>)

=: K−(τ, z).

- (19)


Here K±(τ, z) is a meromorphic function with poles at τ ∈ Γθz, and the series on the left-hand side converges for all large enough Im(τ).

Proof. The proof follows the same lines as the proof of Theorem 2 from [5]. We only prove the statement for gn+, since the case of g−

n is almost identical. From the q-expansion of J−1 and the fact that

J(z) J(z) − J(τ)

Jn(τ)J−n(z),

=

![image 43](<2017-radchenko-fourier-interpolation-real-line_images/imageFile43.png>)

n≥0

it is clear that the gn+ deﬁned by (19) are also of the form θ3(z)Pn(J−1(z)) for some monic polynomial Pn of degree n. The only thing that we need to check is that they satisfy

gn+(z) = q−n/2 + O(q1/2), z → i∞, or, equivalently, that Pn = Pn+. By Cauchy’s theorem we know that

gn+(z) =

- 1

![image 44](<2017-radchenko-fourier-interpolation-real-line_images/imageFile44.png>)

- 2


τ0+2

K+(τ, z)qτ−n/2dτ =

τ0

- 1

![image 45](<2017-radchenko-fourier-interpolation-real-line_images/imageFile45.png>)

- 2πi C


K+(τ, z)qτ−(n+1)/2d(qτ1/2),

where τ0 ∈ H has suﬃciently large imaginary part and C is a small enough loop around 0 in the qτ1/2-plane. Using the identity

- (20) qτ1/2

dJ d(qτ1/2)

![image 46](<2017-radchenko-fourier-interpolation-real-line_images/imageFile46.png>)

(τ) =

J′(τ) πi

![image 47](<2017-radchenko-fourier-interpolation-real-line_images/imageFile47.png>)

= θ4(τ)(1 − 2λ(τ))J(τ)

we get that

K+(τ, z) =

qτ1/2 dJ

![image 48](<2017-radchenko-fourier-interpolation-real-line_images/imageFile48.png>)

d(qτ1/2)

(τ) J(z) − J(τ) ·

![image 49](<2017-radchenko-fourier-interpolation-real-line_images/imageFile49.png>)

θ3(z)J(z) θ3(τ)J(τ)

![image 50](<2017-radchenko-fourier-interpolation-real-line_images/imageFile50.png>)

, and thus changing the variable of integration we get

gn+(z) =

- 1

![image 51](<2017-radchenko-fourier-interpolation-real-line_images/imageFile51.png>)

- 2πi C ˜


(qτ1/2(j))−n J(z) − j ·

![image 52](<2017-radchenko-fourier-interpolation-real-line_images/imageFile52.png>)

θ3(z)J(z) θ3(τ)j

![image 53](<2017-radchenko-fourier-interpolation-real-line_images/imageFile53.png>)

dj.

(We write qτ1/2(j) to emphasized dependence on j.)Now recall that θ3(z)Pn+(J−1(z)) = q−n/2 + O(q1/2), so that (θ3(τ)Pn+(j−1) −qτ−n/2(j))/j is holomorphic in some small neighborhood of 0 in the j-plane. Therefore, for some small loop C˜ around zero, we have

gn+(z) =

- 1

![image 54](<2017-radchenko-fourier-interpolation-real-line_images/imageFile54.png>)

- 2πi C ˜


(qτ1/2(j))−n J(z) − j ·

![image 55](<2017-radchenko-fourier-interpolation-real-line_images/imageFile55.png>)

θ3(z)J(z) θ3(τ)j

![image 56](<2017-radchenko-fourier-interpolation-real-line_images/imageFile56.png>)

dj =

θ3(z) 2πi C ˜

![image 57](<2017-radchenko-fourier-interpolation-real-line_images/imageFile57.png>)

Pn+(j−1) j J(z) − j

![image 58](<2017-radchenko-fourier-interpolation-real-line_images/imageFile58.png>)

J(z)dj

= −

θ3(z) 2πi C ˜

![image 59](<2017-radchenko-fourier-interpolation-real-line_images/imageFile59.png>)

Pn+(j−1) j−1 − J−1(z)

![image 60](<2017-radchenko-fourier-interpolation-real-line_images/imageFile60.png>)

dj−1 = θ3(z)Pn+(J−1(z)).

The last sign is changed since the contour for j−1 in the last application of Cauchy’s formula has the opposite orientation.

Remark. From (20) it also follows that Kε(τ, z) has a simple pole at z = τ with

residue iπ1 for all τ ∈ H. We also record here the following identities for Kε: Kε(τ, −1/z) = ε(−iz)3/2Kε(τ, z), Kε(−1/τ, z) = −ε(−iτ)1/2Kε(τ, z).

![image 61](<2017-radchenko-fourier-interpolation-real-line_images/imageFile61.png>)

- (21)


Note that generating functions very similar to (19) have also been used in [20] in the computation of traces of singular moduli.

4. Interpolation basis for even functions Let us deﬁne a function bεm: R → R by the integral

- (22) bεm(x) =

- 1

![image 62](<2017-radchenko-fourier-interpolation-real-line_images/imageFile62.png>)

- 2


1

−1

gmε (z)eiπx

2zdz,

where the path of integration is chosen to lie in the upper half-plane and orthogonal to the real line at the endpoints 1 and −1. Since gmε has exponential decay at ±1, the above integral converges. Note that bεm is deﬁned for m ≥ 0 if ε = +1 and for m ≥ 1 if ε = −1; for convenience let us also deﬁne b−0 (x) = 0.

Recall that Schwartz functions are C∞-smooth functions that, together with all of their derivatives, decay faster than any inverse power of x.

- Proposition 1. The function bεm: R → R is an even Schwartz function that satisﬁes


bεm(x) = εbεm(x) and

bεm(√n) = δn,m, n ≥ 1, m ≥ 0, where δn,m is the Kronecker delta. In addition, we have b+0 (0) = 1.

![image 63](<2017-radchenko-fourier-interpolation-real-line_images/imageFile63.png>)

Proof. Clearly, bεm is an even function, since ez(x) = eiπx2z is even. That it indeed takes real values for x ∈ R can be seen by taking the integral over the semicircle z = eit,

t ∈ (0, π), making a change of variables z  → −z, and noting that gmε (z) = gmε (−z). Let us prove that bεm belongs to the Schwartz class. We will only consider the case “ε = +”, but the same argument will work also in the case “ε = −”. Since gn+(z) = θ3(z)Pn+(J−1(z)), it is enough to prove that for each n ∈ N the integral

![image 64](<2017-radchenko-fourier-interpolation-real-line_images/imageFile64.png>)

![image 65](<2017-radchenko-fourier-interpolation-real-line_images/imageFile65.png>)

![image 66](<2017-radchenko-fourier-interpolation-real-line_images/imageFile66.png>)

βn(x) =

- 1

![image 67](<2017-radchenko-fourier-interpolation-real-line_images/imageFile67.png>)

- 2


1

−1

θ3(z)J−n(z)eiπx

2zdz

is a Schwartz function. On the circle arc from −1 to 1 the function 1/J(z) takes real values between 0 and 64, and moreover

J−1(±1 + i/t) ≤ C exp(−2πt), t → ∞, Re(t) > 0. By taking the k-th derivative of βn(x) with respect to x under the integral we obtain

βn(k)(x) =

- 1

![image 68](<2017-radchenko-fourier-interpolation-real-line_images/imageFile68.png>)

- 2


1

−1

θ3(z)J−n(z)Qk(x, z)eiπx

2zdz,

where Qk(x, z) are polynomials deﬁned by

- (23)


∂k ∂xk

2z. Clearly, there exists a constant Ck such that

2z = Qk(x, z)eiπx

eiπx

![image 69](<2017-radchenko-fourier-interpolation-real-line_images/imageFile69.png>)

|Qk(x, z)| ≤ Ck(1 + |x|2)k(1 + |z|2)k, thus we get

|βn(k)(x)| ≤ π2k+3Ck(1 + |x|2)k

1/2

2sin(πt)dt.

J−n(eiπt)e−πx

0

Here we used a rather crude estimate |θ(eiπt)| < 2 for t ∈ (0, 1/2). When |x| is small, we estimate the above integral by 64n, for all other values of x we estimate the integral by

splitting it into two parts (where we take δ = (√πx)−1):

![image 70](<2017-radchenko-fourier-interpolation-real-line_images/imageFile70.png>)

1/2

δ

1/2

2sin(πt)dt =

2sin(πt)dt +

2sin(πt)dt ≤ Cδe−2/δ + 64ne−2πδx

J−n(eiπt)e−πx

J−n(eiπt)e−πx

J−n(eiπt)e−πx

0

0

δ

√πx(64n + C/(x√π)), from which it follows that βn is a Schwartz function.

2

![image 71](<2017-radchenko-fourier-interpolation-real-line_images/imageFile71.png>)

= e−2

![image 72](<2017-radchenko-fourier-interpolation-real-line_images/imageFile72.png>)

To check that bεm = εbεm we will use the fact that ez = (−iz)−1/2 e−1/z and the transformation property (16):

bεm(x) =

=

=

- 1

![image 73](<2017-radchenko-fourier-interpolation-real-line_images/imageFile73.png>)

- 2


1 2

![image 74](<2017-radchenko-fourier-interpolation-real-line_images/imageFile74.png>)

1 2

![image 75](<2017-radchenko-fourier-interpolation-real-line_images/imageFile75.png>)

1

2(−1/z)dz

gmε (z)(−iz)−1/2eiπx

−1

1

2(−1/z)d(−1/z)

−gmε (z)(−iz)3/2eiπx

−1

−1

2(−1/z)d(−1/z) = εbεm(x).

εgmε (−1/z)eiπx

1

In the above computations we always choose the branch of (−iz)k/2 that takes positive values for z on the imaginary semiaxis. Finally, note that

1

bεm(√n) =

- 1

![image 76](<2017-radchenko-fourier-interpolation-real-line_images/imageFile76.png>)

- 2


gmε (z)eiπnzdz

![image 77](<2017-radchenko-fourier-interpolation-real-line_images/imageFile77.png>)

−1

is simply the coeﬃcient of q−n/2 in the q-expansion of gmε , so that (17) immediately implies bεm(√n) = δn,m and b+0 (0) = 1.

![image 78](<2017-radchenko-fourier-interpolation-real-line_images/imageFile78.png>)

Remark. Note that (17) also implies that b+m(0) = δm,0, and using the explicit formula (19) for the kernel K−, we also get

b−m(0) = −2, m ≥ 1 is a square, 0, otherwise.

Alternatively, this last equation follows from the Poisson summation formula

b−m(n).

b−m(n) =

b−m(n) = −

n∈Z

n∈Z

n∈Z

To establish other properties of the sequences {bεm(x)}m we will need to work with generating functions. Let D be the standard fundamental domain for the group Γθ (as deﬁned in (5)). For a ﬁxed x deﬁne a function Fε(τ, x) on the set

{τ ∈ H : ∀k ∈ Z, |τ − 2k| > 1} ⊃ D + 2Z by

- (24) Fε(τ, x) =

- 1

![image 79](<2017-radchenko-fourier-interpolation-real-line_images/imageFile79.png>)

- 2


1

−1

Kε(τ, z)eiπx

2zdz,

where the contour is the semicircle in the upper half-plane that passes through −1 and 1. Note that for Im(τ) > 1 we have

- (25) Fε(τ, x) =


∞

bεn(x)eiπnτ,

n=0

and the series converges absolutely. Our next task is to show that Fε can be analytically continued to H (and hence (25) also holds for all τ ∈ H).

- Proposition 2. For any ε ∈ {+, −} and x ∈ R the function Fε(τ, x) admits an analytic continuation to H. Moreover, the analytic continuation satisﬁes the functional equations


- (26)

Proof. To prove the theorem, it is enough to show that there exists an analytic continuation to some open set Ω containing the relative closure of D, on which (26) holds. Indeed, we can then choose a smaller Ω in such a way that Ω∩ γ−1(Ω) = ∅ if and only if γ ∈ {T2, T−2, S, I}. Since ∪g∈Γθ

gΩ = H, we can construct a continuation inductively by repeatedly using (26) to pass to the neighboring sets gΩ that have not been covered yet. Since Γθ is generated by S and T2, and the only relation is S2 = 1, this process indeed gives a single-valued analytic continuation (the main reason is that there are no cycles of neighboring domains; this is also clear from Figure 2).

The ﬁrst functional equation in (26) is clearly satisﬁed, since the integral that deﬁnes Fε automatically deﬁnes a 2-periodic function on the open set {τ ∈ H : ∀k ∈ Z, |τ−2k| > 1} that contains the vertical lines Im(τ) = ±1.

Hence, we only need to deal with the second functional equation. We can get an analytic

continuation of Fε to some neighborhood of {z ∈ H : |z| = 1, z = i} by changing the contour of integration in (24). First, we rewrite the integral as

2Fε(τ, x) =

i

−1

Kε(τ, z)eiπx

2zdz +

1

i

Kε(τ, z)eiπx

2zdz

=

i

−1

Kε(τ, z)eiπx

2zdz −

i

−1

Kε(τ, −1/z)eiπx

2(−1/z)z−2dz

=

i

−1

Kε(τ, z)(eiπx

2z + ε(−iz)−1/2 eiπx

2(−1/z))dz,

- (27)


Fε(τ, x) − Fε(τ + 2, x) = 0, Fε(τ, x) + ε(−iτ)−1/2Fε −

1 τ

2

, x = eiπτx

![image 80](<2017-radchenko-fourier-interpolation-real-line_images/imageFile80.png>)

2

+ ε(−iτ)−1/2eiπ(−1/τ)x

.

![image 81](<2017-radchenko-fourier-interpolation-real-line_images/imageFile81.png>)

![image 82](<2017-radchenko-fourier-interpolation-real-line_images/imageFile82.png>)

where we have used the transformation property (21). Note, that if τ belongs to D ∪SD, then the only poles of Kε(τ, z) (as a function of z) inside D ∪ SD are at z = τ and z = −1/τ. Let γ1 be the circle arc from −1 to i, and let γ2 be a simple smooth path from −1 to i that lies inside SD and strictly below γ1. Denote by F the region enclosed between γ1 and γ2. We will now build a continuation of Fε to F and show that it satisﬁes the functional equation. We deﬁne a continuation by the contour integral

![image 83](<2017-radchenko-fourier-interpolation-real-line_images/imageFile83.png>)

![image 84](<2017-radchenko-fourier-interpolation-real-line_images/imageFile84.png>)

![image 85](<2017-radchenko-fourier-interpolation-real-line_images/imageFile85.png>)

- 1

![image 86](<2017-radchenko-fourier-interpolation-real-line_images/imageFile86.png>)

- 2 γ


F˜ε(τ, x) =

2z + ε(−iz)−1/2eiπx

2(−1/z)) dz.

Kε(τ, z)(eiπx

2

Clearly, Fε = F˜ε for τ with big enough imaginary part, so F˜ indeed deﬁnes an analytic continuation to F. For τ ∈ F we compute

εeiπx2(−1/z) √

ε √

1 τ

- 1

![image 87](<2017-radchenko-fourier-interpolation-real-line_images/imageFile87.png>)

- 2 γ


εKε(−1/τ, z) −

F˜ε(τ, x) +

, x = F˜ε(τ, x) −

2z +

(eiπx

√

Fε −

)dz

![image 88](<2017-radchenko-fourier-interpolation-real-line_images/imageFile88.png>)

![image 89](<2017-radchenko-fourier-interpolation-real-line_images/imageFile89.png>)

![image 90](<2017-radchenko-fourier-interpolation-real-line_images/imageFile90.png>)

![image 91](<2017-radchenko-fourier-interpolation-real-line_images/imageFile91.png>)

![image 92](<2017-radchenko-fourier-interpolation-real-line_images/imageFile92.png>)

![image 93](<2017-radchenko-fourier-interpolation-real-line_images/imageFile93.png>)

![image 94](<2017-radchenko-fourier-interpolation-real-line_images/imageFile94.png>)

−iτ

−iτ

−iz

1

- 1

![image 95](<2017-radchenko-fourier-interpolation-real-line_images/imageFile95.png>)

- 2 γ


= F˜ε(τ, x) −

2z + ε(−iz)−1/2eiπx

2(−1/z))dz

Kε(τ, z)(eiπx

1

- 1

![image 96](<2017-radchenko-fourier-interpolation-real-line_images/imageFile96.png>)

- 2 ∂F


2z + ε(−iz)−1/2eiπx

2(−1/z))dz

Kε(τ, z)(eiπx

=

2z + ε(−iz)−1/2eiπx

2(−1/z))

Resz=w Kε(τ, z)(eiπx

= iπ

w∈F

2τ + ε(−iτ)−1/2eiπx

2(−1/τ),

= eiπx

D

i

τ Sτ

- γ1
- γ2


F

−1 1

Figure 3. Fundamental domain for Γθ and the contour of integration.

which is precisely the functional equation that we needed. Similar computation works for the arc from i to 1. The only thing that is left is to check that Fε has no singularity

- at τ = i. For ε = 1 this follows from the second functional equation, while for ε = −1 both 2λ(z) − 1 and eiπzr2 + ε(−iz)−1/2eiπ(−1/z)r2 vanish at z = i, so that they cancel the double pole at i coming from J(i) − J(z), and hence the integral (27) converges at τ = i.


As an immediate corollary, we obtain that formula (25) is valid for all τ ∈ H. This

already implies that for all δ > 0 we have bεn(x) = O((1 + δ)n). In the next section we prove a much stronger estimate.

Note that the only properties of Kε that were used in the proof are the modularity in τ and in z, as well as the fact that the only poles are at z ∈ Γθτ, and that the residue at z = τ is equal to 1/(iπ).

5. Growth estimate The main result of this section is the following.

- Theorem 4. For any ε ∈ {+, −} the numbers bεn(x) satisfy |bεn(x)| = O(n2)


uniformly in x.

To prove this we will use the following general result that goes back to Hecke (see, for example, [1, Lemma 2.2, (ii)]).

- Lemma 1. If a 2-periodic analytic function f : H → C has a Fourier expansion f(τ) = n≥0 aneiπnτ and for some α > 0 it satisﬁes


|f(τ)| ≤ C Im(τ)−α for Im(τ) < c, then for all suﬃciently large n we have

eπ α

α nα.

|an| ≤ C

![image 97](<2017-radchenko-fourier-interpolation-real-line_images/imageFile97.png>)

To prove Theorem 4 we will apply this lemma to the generating function Fε(τ, x). To simplify notation, we will write Fε(τ) instead of Fε(τ, x). The estimate of |Fε(τ)| naturally splits into two parts: combinatorial (estimating Fε(τ) − (Fε|A)(τ) using functional equations) and analytic (estimating Fε(τ) using the deﬁning contour integral).

To deal with the ﬁrst part, we deﬁne functions φA(τ) for A ∈ Γθ:

- (28) φA(τ) := Fε(τ) − (Fε|−1/ε2A)(τ). From the functional equations (26) for Fε we have

φT2(τ) = 0, φS(τ) = eiπx

2τ + ε(−iτ)−1/2eiπx

2(−1/τ) .

- (29)


Moreover, the functions φA satisfy the cocycle relation φAB = φB + φA|B (where we write | for |−1/ε2). In other words, the collection {φA}A∈Γθ

forms what is usually called a Γθ-cocycle (see, for example, [10]).

First, we need the following elementary lemma.

- Lemma 2. For any τ ∈ H with |τ| ≥ 1 and any sequence of non-zero integers {nj}j≥1 deﬁne a sequence of numbers τj ∈ H as follows:

τ0 = τ, τj = 2nj −

1 τj−1

![image 98](<2017-radchenko-fourier-interpolation-real-line_images/imageFile98.png>)

, j ≥ 1.

Then the sequence {Im(τj)}j≥0 is strictly decreasing and Im(τj) ≤ 2j1−1 for all j ≥ 1. Proof. First, observe that |τj| > 1 for all j ≥ 1 (the proof is by induction). The inequality Im(τj) ≥ Im(τj+1) the follows from Im(τj+1) = Im(τj)/|τj|2 < Im(τj).

![image 99](<2017-radchenko-fourier-interpolation-real-line_images/imageFile99.png>)

For a, b ∈ R denote by D(a, b) the half-disk with center (a + b)/2 whose boundary semicircle passes through a and b. Let D be any such half-disk that does not intersect D(−1, 1) and set D′ = SD. Then a simple calculation shows that

diam(D′) ≤

diam(D) 1 + diam(D)

![image 100](<2017-radchenko-fourier-interpolation-real-line_images/imageFile100.png>)

.

Note that τ1 ∈ n =0 D(2n − 1, 2n+ 1), so τ1 lies in some half-disk of diameter 2. Denote this half-disk by D1, and deﬁne Dj+1 = 2nj + SDj. Then τj ∈ Dj and no Dj intersects D(−1, 1). By repeatedly applying the above inequality we get that Dj has diameter at most 2/(2j − 1), thus Im(τj) ≤ 1/(2j − 1).

The following lemma allows us to estimate values of certain cocycles.

- Lemma 3. Let {ψA}A∈Γθ


be a cocycle (with respect to | := |−k/ε2) such that ψT2 = 0, |ψS(τ)| ≤ |τ|α + Im(τ)−β

for some α, β ≥ 0. Let τ′ ∈ D, A ∈ Γθ, and τ = Aτ′ ∈ H and suppose that Im(τ) ≤ 1. Then

|ψA(τ′)| ≤ |τ|α + Im(τ)−α−1 + 2 Im(τ)−β−1. Proof. Let us consider the case when

A = ST2n

ST2n

S . . .T2n

S. By applying the cocycle relation repeatedly, we get that

m

m−1

1

ψA = ψS + ψS|A1 + ψS|A2 + · · · + ψS|Am, where we write Aj = T2n

S . . . T2n

S. Hence

j

1

m

|ψS(τj)| |cjτ′ + dj|k

|ψA(τ′)| ≤

,

![image 101](<2017-radchenko-fourier-interpolation-real-line_images/imageFile101.png>)

j=0

where Aj = ( acj bj

j dj ) and τj are deﬁned by

τ0 = τ′, τj = 2nj − 1/τj−1.

′+bj

Under these deﬁnitions τj = ajτ

cjτ′+dj and τ = −1/τm. Multiplying both sides of the above inequality by Im(τ′)k/2 we get

![image 102](<2017-radchenko-fourier-interpolation-real-line_images/imageFile102.png>)

Im(τ′)k/2|ψA(τ′)| ≤

m

Im(τj)k/2|ψS(τj)|

j=0

Lemma 2 implies that Im(τ)−1 ≥ 2m − 1 and Im(τj) ≥ Im(τ) for j = 0, . . ., m. We also have |τj| ≤ Im(τ)−1 for j = 0, . . ., m − 1, since Im(τ) ≤ Im(τj+1) = Im(τj)/|τj|2 ≤ |τj|−1. Therefore

Im(τ′)k/2|ψA(τ′)| ≤

m

Im(τj)k/2(|τj|α + Im(τj)−β) ≤ Im(τ′)k/2

j=0

m

(|τj|α + Im(τj)−β)

j=0

≤ Im(τ′)k/2(|τ|α + mIm(τ)−α + (m + 1)Im(τ)−β)

≤ Im(τ′)k/2(|τ|α + Im(τ)−α−1 + 2 Im(τ)−β−1), where in the last line we used m + 1 ≤ 4m − 2 ≤ Im(τ)−1.

The proof in the other cases (i.e., when A is of the form T2nkST2nk−1

S . . .T2n

S, ST2nkST2nk−1

1

S . . .T2n

, or T2nkST2nk−1

S . . .T2n

) can be completed using similar estimates.

1

1

Next, we deal with the analytic part of the estimate. For Theorem 1 the case n = 0 of the lemma below will suﬃce, but we need the general form for the proof of Theorem 2.

- Lemma 4. For each n, k ≥ 0 there exists an absolute constant Cn,k > 0 such that the inequality


dn dxn

xk

Fε(τ, x) ≤ Cn,k(1 + Im(τ)−(n+k+1)/2)

![image 103](<2017-radchenko-fourier-interpolation-real-line_images/imageFile103.png>)

holds for all τ ∈ D. Proof. Let τ be any point in D. Since Fε(it) is real for all t > 0, from the Schwarz reﬂection principle we get that

![image 104](<2017-radchenko-fourier-interpolation-real-line_images/imageFile104.png>)

- (30) Fε(−τ) = Fε(τ).


![image 105](<2017-radchenko-fourier-interpolation-real-line_images/imageFile105.png>)

Using this symmetry we reduce the inequality to the case τ ∈ D1, where D1 = {τ ∈ D : Re(τ) ∈ (−1, 0)}. Observe that Im(J(τ)) < 0 for all τ ∈ D1 and Im(J(τ)) ≥ 0 for all τ ∈ D D1. Indeed, since J is a Hauptmodul, the map J : D → C is injective. The identity (30) for J implies that for τ ∈ D the value J(τ) is real if and only if τ lies on the imaginary axis. It is easy to see from (14) that Im(J(τ)) < 0 for τ ∈ D1 and Im(τ) ≫ 1. Hence, this inequality also holds for all τ ∈ D1.

Deﬁne

L = {w ∈ C | Re(w) = J(i) = 1/64, Im(w) > 0}, and let ℓ be the preimage of L under the map J : D → C (see Figure 4). Then ℓ is a smooth path contained in D D1 and goes from i to 1. We set γ to be the path Sℓ ∪ ℓ that goes from −1 to 1. Note that |z| and |z|−1 are bounded on γ and that γ has ﬁnite length (this fact will follow from the computations below).

As in the proof of Proposition 1 let Qn(x, z) be a polynomial deﬁned by (23). We have xk

1

dn dxn

- 1

![image 106](<2017-radchenko-fourier-interpolation-real-line_images/imageFile106.png>)

- 2


2zdz.

Kε(τ, z) xk Qn(x, z) eiπx

Fε(τ, x) =

![image 107](<2017-radchenko-fourier-interpolation-real-line_images/imageFile107.png>)

−1

From (21) we ﬁnd xk

1

dn dxn

- 1

![image 108](<2017-radchenko-fourier-interpolation-real-line_images/imageFile108.png>)

- 2


2z+ε(−iz)−1/2Qn(x, −1/z) eiπx

2(−1/z) dz.

Kε(τ, z) xk Qn(x, z) eiπx

Fε(τ, x) =

![image 109](<2017-radchenko-fourier-interpolation-real-line_images/imageFile109.png>)

i

Without loss of generality, we may assume x ≥ 0. Since |z| is bounded for z ∈ γ, any monomial zαxβ with 0 ≤ β ≤ n is majorized by 1 + xn, and thus for all such z we have |xk Qn(x, z)| ≪n,k,γ 1 + xn+k. Then

dn dxn

2z + ε(−iz)−1/2 Qn(x, −1/z) eiπx

2(−1/z) |dz|

xk

|Kε(τ, z) xk| Qn(x, z) eiπx

Fε(τ, x) ≪

![image 110](<2017-radchenko-fourier-interpolation-real-line_images/imageFile110.png>)

ℓ

- (31) 2Im(−1/z) |dz|. Next, we observe that

(1 + xk+n) e−πx

2Im(z) ≪k+n 1 + Im(z)

−k−n

![image 111](<2017-radchenko-fourier-interpolation-real-line_images/imageFile111.png>)

2 . Note, that 1 ≤ |z| ≪ 1 for z ∈ ℓ. Hence, we get

xk

dn dxn

![image 112](<2017-radchenko-fourier-interpolation-real-line_images/imageFile112.png>)

Fε(τ, x) ≪

ℓ

|Kε(τ, z)| 1 + Im(z)

−k−n

![image 113](<2017-radchenko-fourier-interpolation-real-line_images/imageFile113.png>)

2 + |z|−1/2 Im(−z1)

![image 114](<2017-radchenko-fourier-interpolation-real-line_images/imageFile114.png>)

−k−n 2

![image 115](<2017-radchenko-fourier-interpolation-real-line_images/imageFile115.png>)

|dz|

=

ℓ

|Kε(τ, z)| 1 + Im(z)

−k−n

![image 116](<2017-radchenko-fourier-interpolation-real-line_images/imageFile116.png>)

2 + |z|k+n−1/2 Im(z)

−k−n 2

![image 117](<2017-radchenko-fourier-interpolation-real-line_images/imageFile117.png>)

|dz|

≪

ℓ

|Kε(τ, z)| 1 + Im(z)

−k−n 2

![image 118](<2017-radchenko-fourier-interpolation-real-line_images/imageFile118.png>)

- (32) |dz|.

Without loss of generality, we may also assume that |τ −i| ≥ 1/10, since we can recover the inequality of the Lemma in the region |τ − i| < 1/10 by applying the maximum modulus principle together with the functional equation for Fε.

For τ with Im(τ) ≥ 1/2 and |τ − i| > 1/10 we can estimate |Kε(τ, z)| ≪ |θ(z)|3 with a constant independent of τ. Since |θ3(z)| behaves like Im(z)−2e−π/Im(z) as z approaches 1, by splitting the integral into {z: Im(z) ≥ 1/x} and {z: Im(z) < 1/x} we obtain

|Fε(τ, x)| ≪ (1 + x2)e−cπx, which clearly implies the needed inequality.

Now let Im(τ) < 1/2. To bound |Kε(τ, z)| we use the following estimates

|θ(z)| ≪ |J(z)|−1/8 Im(z)−1/2, |1 − 2λ(z)| ≪ |J(z)|1/2,

which hold for all z ∈ D near the cusp 1 (such z correspond to large values of |J(z)|). The ﬁrst inequality follows from the fact that θ8(z)J(z) is a holomorphic modular form of weight 4 for Γθ (the term Im(z)−1/2 comes from the modular transformation). To prove the second inequality, simply note that (1 − 2λ(z))2 = 1 − 64J(z). Thus, we get

|K+(τ, z)| ≪ Im(τ)−1/2|J(τ)|3/8|J(z)|5/8Im(z)−3/2 |J(z) − J(τ)|

![image 119](<2017-radchenko-fourier-interpolation-real-line_images/imageFile119.png>)

- (33) ,


2Im(z) + |z|−1/2 e−πx

|Kε(τ, z)| (1 + xk+n) e−πx

≪

ℓ

|K−(τ, z)| ≪ Im(τ)−1/2|J(τ)|7/8|J(z)|1/8Im(z)−3/2 |J(z) − J(τ)|

.

![image 120](<2017-radchenko-fourier-interpolation-real-line_images/imageFile120.png>)

D1 D D1

ℓ

i

τ Sℓ

−1 1

Figure 4. Deforming the contour of integration.

From now on, we make all estimates for z ∈ ℓ with Im(z) < 1/2, and we deﬁne t > 0 in such a way that J(z) = 1/64 + it. For such z we can use the following simple geometric estimate (recall that Im(J(τ)) < 0)

- (34) |J(τ) − J(z)| ≫ |J(τ)|2 + |J(z)|2. Let w: C [0, 641 ) → D be the inverse of J on D, so that z = w(1/64 + it). We have

![image 121](<2017-radchenko-fourier-interpolation-real-line_images/imageFile121.png>)

![image 122](<2017-radchenko-fourier-interpolation-real-line_images/imageFile122.png>)

- J′(τ) = iπf(τ)J(τ), where f(τ) = θ4(τ)(1 − 2λ(τ)) is a holomorphic modular form of weight 2. Since f does not vanish at the cusp 1, we have that |f(z)| ≫ Im(z)−2, and thus


- (35) |dz| = |w′(1/64 + it)| |dt| = |dt| |J′(w(641 + it))|


|dt| |J(z)| · Im(z)−2. Note that this last estimate readily implies that ℓ has ﬁnite length.

≪

![image 123](<2017-radchenko-fourier-interpolation-real-line_images/imageFile123.png>)

![image 124](<2017-radchenko-fourier-interpolation-real-line_images/imageFile124.png>)

![image 125](<2017-radchenko-fourier-interpolation-real-line_images/imageFile125.png>)

From inequality (32) it follows that it is enough to ﬁnd a bound for

|Kε(τ, z)| Im(z)−m |dz| for m ≥ 0. From inequalities (33), (34), (35) we deduce

ℓ

∞

|J(τ)|3/8t−3/8Im(z)1/2−m Im(τ)1/2 t2 + |J(τ)|2

|K+(τ, z)| Im(z)−m |dz| ≪

dt.

![image 126](<2017-radchenko-fourier-interpolation-real-line_images/imageFile126.png>)

![image 127](<2017-radchenko-fourier-interpolation-real-line_images/imageFile127.png>)

ℓ

0

We will also need the estimate |J(z)| ≫ eπ/Im(z) for Im(z) small enough. Indeed, this inequality follows from the q-expansion (15) of J(z) at the cusp 1. This implies that Im(z)−m ≪m logm(1 + |J(z)|). Thus, we have

|J(τ)|3/8t−3/8 logm(1 + t)dt |J(τ)|2 + t2

∞

|K+(τ, z)| Im(z)−m |dz| ≪ Im(τ)−1/2

![image 128](<2017-radchenko-fourier-interpolation-real-line_images/imageFile128.png>)

![image 129](<2017-radchenko-fourier-interpolation-real-line_images/imageFile129.png>)

ℓ

0

t−3/8 logm(1 + t|J(τ)|)dt √1 + t2

∞

= Im(τ)−1/2

.

![image 130](<2017-radchenko-fourier-interpolation-real-line_images/imageFile130.png>)

![image 131](<2017-radchenko-fourier-interpolation-real-line_images/imageFile131.png>)

0

By using an obvious inequality log(1 + ab) ≤ log(1 + a) + log(1 + b), we estimate the last integral by

m

Im(τ)−1/2

j=0

m j

logj(1 + |J(τ)|)

t−3/8 logm−j(1 + t)dt √1 + t2 ≪

∞

![image 132](<2017-radchenko-fourier-interpolation-real-line_images/imageFile132.png>)

![image 133](<2017-radchenko-fourier-interpolation-real-line_images/imageFile133.png>)

0

m

cj,mIm(τ)−j−1/2,

j=0

where cj,m = mj 0 ∞(1 + t2)−1/2t−3/8 logm−j(1 + t)dt are ﬁnite constants, and we have used the inequality log(1 + |J(τ)|) ≪ Im(τ)−1 that follows from (15).

The estimates in the case “ε = −” are completely analogous, except that we need to change the exponent 3/8 to 7/8.

We are now ready to prove Theorem 4.

Proof of Theorem 4. Let τ ∈ H be an arbitrary point in the upper half-plane with Im(τ) ≤ 1 that does not lie on the boundary of the fundamental domain D or any

of its translates by elements of Γθ. Let τ = cτaτ′+b

′+d, where τ′ ∈ D and A = ( ac db ) ∈ Γθ. By (28) we have

![image 134](<2017-radchenko-fourier-interpolation-real-line_images/imageFile134.png>)

aτ′ + b cτ′ + d

= Fε(τ′) − φA(τ′).

χε(A)jθ(τ′, A)Fε

![image 135](<2017-radchenko-fourier-interpolation-real-line_images/imageFile135.png>)

Combining the results of Lemma 4 and Lemma 3 (which we apply to ψA = φA with α = 0 and β = 1/2) we obtain

Im(τ′)1/4 Im(τ)1/4 |Fε(τ′)| +

Im(τ′)1/4 Im(τ)1/4 |φA(τ′)|

|Fε(τ)| ≤

![image 136](<2017-radchenko-fourier-interpolation-real-line_images/imageFile136.png>)

![image 137](<2017-radchenko-fourier-interpolation-real-line_images/imageFile137.png>)

Im(τ′)1/4 + Im(τ′)−1/4 Im(τ)1/4

+ Im(τ′)1/4(1 + Im(τ)−5/4 + 2 Im(τ)−7/4). (Here C0 is the constant from Lemma 4.) If c = 0, then Im(τ′) = Im(τ) and thus

≤ C0

![image 138](<2017-radchenko-fourier-interpolation-real-line_images/imageFile138.png>)

|Fε(τ)| ≤ C0(1 + Im(τ)−1/2) + Im(τ)1/4 + Im(τ)−1 + 2 Im(τ)−3/2. If, on the other hand, c = 0, then we have Im(τ) < Im(τ′) and

Im(τ′)2 |cτ′ + d|2

Im(τ)Im(τ′) =

≤ 1, and we get the estimate

![image 139](<2017-radchenko-fourier-interpolation-real-line_images/imageFile139.png>)

|Fε(τ)| ≤ 2C0Im(τ)−1/2 + Im(τ)−1/4 + Im(τ)−3/2 + 2 Im(τ)−2. Therefore, an application of Lemma 1 gives

|bεn(x)| ≪ n2.

The exponent “2” in Theorem 4 is not optimal, but for the proof of Theorem 1 any polynomial bound would suﬃce.

6. Proof of the main results

Now that we know that bεn(x) have polynomial growth in n, the proof of Theorem 1 and Theorem 2 is not hard.

Recall the deﬁnition of Schwartz functions:

S = {f ∈ C∞(R): f α,β < ∞ ∀α, β ≥ 0}, where the seminorms · α,β are deﬁned by

|xαf(β)(x)|.

f α,β = sup

x∈R

Convergence in S is deﬁned in terms of this family of seminorms, i.e., fn → f if and only if fn − f α,β → 0 for all α, β ≥ 0.

- Proof of Theorem 1. Let Seven be the space of even Schwartz functions. Let us deﬁne


b+n (x) + b−

n (x) 2

an(x) :=

. Lemma 1 implies that

![image 140](<2017-radchenko-fourier-interpolation-real-line_images/imageFile140.png>)

b+n (x) − b−

n(x) 2

an(x) =

. Our aim is to show that (2) holds for all f ∈ Seven. Theorem 4 implies that the series

![image 141](<2017-radchenko-fourier-interpolation-real-line_images/imageFile141.png>)

∞

∞

an(x) f(√n)

an(x)f(√n) +

![image 142](<2017-radchenko-fourier-interpolation-real-line_images/imageFile142.png>)

![image 143](<2017-radchenko-fourier-interpolation-real-line_images/imageFile143.png>)

n=0

n=0

converges absolutely. Moreover, it follows from the deﬁnition of bεn and the functional equations (26) that for any τ ∈ H we have

∞

∞

an(x) eτ(√n) +

an(x) eτ(√n),

![image 144](<2017-radchenko-fourier-interpolation-real-line_images/imageFile144.png>)

![image 145](<2017-radchenko-fourier-interpolation-real-line_images/imageFile145.png>)

- (36) eτ(x) =


n=0

n=0

where eτ(x) = eiπτx2. For x ≥ 0 consider the linear functional φx on Seven given by

∞

∞

an(x) f(√n).

an(x)f(√n) −

![image 146](<2017-radchenko-fourier-interpolation-real-line_images/imageFile146.png>)

![image 147](<2017-radchenko-fourier-interpolation-real-line_images/imageFile147.png>)

φx(f) := f(x) −

n=0

n=0

It follows from Theorem 4 that φx is a tempered distribution, i.e., it is continuous with respect to convergence in Seven. From equation (36) we see that φx vanishes on the subspace spanned by {eτ}τ∈H. Our goal is to show that φx vanishes on the whole Seven.

Let C be the space of compactly supported even C∞ functions on R. Recall, that C dense in Seven (see [18, pp. 74-75]). Therefore, it suﬃces to show (2) for f ∈ C. Let f be a function in C. We may assume that

2

f(x) = F(x2) e−πx

where F is a C∞ function with compact support on R. Consider the one-dimensional Fourier transform of F

∞

F(t) e−2πist dt. Note, that F is a Schwartz function. By the Fourier inversion formula we have f(x) = F(x2) e−πx

F(s) :=

−∞

∞

∞

2

2−πx2 ds =

F(s) e2πisx

=

F(s) ei+2s(x) ds. Deﬁne

−∞

−∞

T

hT :=

F(s) ei+2s(x) ds. It is easy to see that for all seminorms · α,β

−T

f − hT α,β → 0 as T → ∞. Therefore, for all x ≥ 0

φx(f − hT) → 0 as T → ∞. On the other hand, we have

T

φx(hT) =

F(s) φx(ei+2s) ds = 0. This ﬁnishes the proof of Theorem 1.

−T

We are also ready to prove Theorem 2.

- Proof of Theorem 2. First, we observe that the image of Ψ is contained in the kernel of L. Indeed, the Poisson summation formula implies


f(n)

f(n) =

n∈Z

n∈Z

for all f ∈ S as well as f ∈ Seven. This identity is equivalent to L ◦ Ψ(f) = 0.

Next, we construct the function Φ : ker L → Seven such that Ψ◦Φ = IkerL. To this end we consider the map

Φ : ker L → Seven, ((xn), (yn))  →

n

xn an(x) + yn an(x).

We need to show that Φ is well-deﬁned. Since S is complete with respect to the family of norms · α,β it is enough to prove that for any ﬁxed α, β ≥ 0 the sequences ( an α,β)n and ( an α,β)n have at most polynomial growth in n. Equivalently, it is enough to prove that the sequences ( bεn α,β)n have polynomial growth.

As before, let Qk(x, z) be the polynomial deﬁned by (23). Let U(τ, x) be the generating function

∞

dβ dxβ

dβ dxβ

U(τ, x) = xα

Fε(τ, x) = xα

bεn(x) eiπnτ.

![image 148](<2017-radchenko-fourier-interpolation-real-line_images/imageFile148.png>)

![image 149](<2017-radchenko-fourier-interpolation-real-line_images/imageFile149.png>)

n=0

Then, following the proof of Proposition 2, we see that the generating function U satisﬁes the functional equation

U(τ) − (U|−1/ε2A)(τ) = φA(τ), where φA is the cocycle deﬁned by φT2(τ) = 0,

2(−1/τ) . Using the estimates

2τ + ε(−iτ)−1/2xαQβ(x, −1/τ)eiπx

φS(τ) = xαQβ(x, τ)eiπx

2τ| ≪ |τ|lIm(τ)−k/2 < Im(τ)−k + |τ|2l and

|xkτleiπx

2(−1/τ)| ≪ |τ|k−lIm(τ)−k/2 < Im(τ)−k + |τ|2k−2l, and in case k < l the replacing |τ|2k−2l by Im(τ)2k−2l, we see that Lemma 3 can be applied to {φA}A∈Γθ

|xkτ−leiπx

(for some choice of α and β in Lemma 3). Lemma 4 implies that for τ ∈ D we have

U(τ, x) ≪ 1 + Im(τ)−(α+β+1)/2. Arguing the same way as in the proof of Theorem 4 we obtain that for some C > 0 and all τ ∈ H with Im(τ) < 1 we have |U(τ, x)| ≪ Im(τ)−C, which implies that bεn α,β ≪ nC. Therefore, the map Φ is well-deﬁned.

and Proposition 1 implies that Ψ◦Φ = IkerL. This ﬁnishes the proof.

Now Theorem 1 implies that Φ◦Ψ = IS

even

7. Interpolation basis for odd functions

The case of odd Schwartz functions is very similar to the even case. The proofs are easy enough to adapt to this case, so we will just give the general outline. The role of the Gaussian eτ(x) = eiπτx2 is played by the Schwartz function

2

oτ(x) = xeiπτx

,

that satisﬁes

oτ(ξ) = −i(−iτ)−3/2o−1/τ(ξ). To construct the interpolation basis for odd Schwartz functions we use the same idea as before: to get an eigenfunction we integrate oτ over τ with some “modular weight”. More precisely, let hεn: H → C be holomorphic functions with the following properties:

hεn(z + 2) = hεn(z),

(−iz)−1/2hεn(−1/z) = εhεn(z), h+n(z) = q−n/2 + O(q1/2), z → i∞, h−n(z) = q−n/2 + O(1), z → i∞,

hεn(1 + i/t) → 0, t → ∞.

Once again, we may assume that they are of the form h+n(z) = θ(z)Q+n (J−1(z)), h−n(z) = θ(z)(1 − 2λ(z))Q−n (J−1(z)),

- (37)

where Q±

n ∈ Q[x] are monic of degree n and Q−

n has no constant term. The ﬁrst few of these functions are

- h+0 = θ,
- h+1 = θ · (J−1 − 26),
- h+2 = θ · (J−2 − 50J−1 + 76),


- h−1 = θ · (1 − 2λ) · (J−1),
- h−2 = θ · (1 − 2λ) · (J−2 − 18J−1),
- h−3 = θ · (1 − 2λ) · (J−3 − 42J−2 + 168J−1).


By the same arguments as in the even case, we establish generating functions for hεn, which turn out to be the same, except for switching the roles of τ and z.

- Theorem 5. The generating functions for {h+n(z)}n≥0 and {h−

n(z)}n≥1 are given by

∞

- n=0

h+n (z)eiπnτ =

θ3(τ)(1 − 2λ(τ))θ(z)J(z) J(z) − J(τ)

![image 150](<2017-radchenko-fourier-interpolation-real-line_images/imageFile150.png>)

= −K−(z, τ),

∞

- n=1


h−n (z)eiπnτ =

θ3(τ)J(τ)θ(z)(1 − 2λ(z)) J(z) − J(τ)

![image 151](<2017-radchenko-fourier-interpolation-real-line_images/imageFile151.png>)

= −K+(z, τ).

(38)

Similarly to the even case, deﬁne dεm: R → R by dεm(x) =

- 1

![image 152](<2017-radchenko-fourier-interpolation-real-line_images/imageFile152.png>)

- 2


1

−1

hεm(z) xeiπx

2zdz.

- Proposition 3. The function dεm: R → R is odd, belongs to the Schwartz class, and satisﬁes


dεm(x) = (−iε) dεm(x) and

dεm(√n) = δn,m√n, n ≥ 1, where δn,m is the Kronecker delta. Moreover,

![image 153](<2017-radchenko-fourier-interpolation-real-line_images/imageFile153.png>)

![image 154](<2017-radchenko-fourier-interpolation-real-line_images/imageFile154.png>)

lim

x→0

d+m(x) x

![image 155](<2017-radchenko-fourier-interpolation-real-line_images/imageFile155.png>)

= δm,0. Furthermore, we have the following estimate on the growth of d± n(x) as a function of n.

- Theorem 6. For any ε ∈ {+, −} the numbers dεn(x) satisfy




dεn(x) = O(n5/2) uniformly in x.

The proof of this estimate is also based on estimating the growth for Im(τ) → 0 of the generating function

dεn(x)eiπnτ. The functional equations for Gε are

Gε(τ, x) =

n≥0

Gε(τ, x) − Gε(τ + 2, x) = 0, Gε(τ, x) + ε(−iτ)−3/2Gε −

- (39)

The diﬀerence in exponents of (−iτ) come from the fact that the weight of Kε(z, τ) in variable τ is now 3/2, but with appropriate changes the proof still goes through. Finally, we get the following interpolation theorem for odd Schwartz functions.

- Theorem 7. For any odd Schwartz function f : R → R and any x ∈ R we have


- (40) f(x) = d+0 (x)


1 τ

2

2

+ ε(−iτ)−3/2xeiπ(−1/τ)x

, x = xeiπτx

.

![image 156](<2017-radchenko-fourier-interpolation-real-line_images/imageFile156.png>)

f(√n) √n

f(√n) √n −

∞

∞

f′(0) + i f ′(0) 2

![image 157](<2017-radchenko-fourier-interpolation-real-line_images/imageFile157.png>)

![image 158](<2017-radchenko-fourier-interpolation-real-line_images/imageFile158.png>)

+

cn(x)

cn(x)

,

![image 159](<2017-radchenko-fourier-interpolation-real-line_images/imageFile159.png>)

![image 160](<2017-radchenko-fourier-interpolation-real-line_images/imageFile160.png>)

![image 161](<2017-radchenko-fourier-interpolation-real-line_images/imageFile161.png>)

![image 162](<2017-radchenko-fourier-interpolation-real-line_images/imageFile162.png>)

![image 163](<2017-radchenko-fourier-interpolation-real-line_images/imageFile163.png>)

n=1

n=1

where cn(x) = (d+n(x) + d−

n(x))/2.

As in the even case, the functional equations for Gε show that (40) holds for oτ(x), so one only needs to show that oτ are dense in the space of odd Schwartz functions, which can be done by an approximation argument, similarly to the proof of Theorem 1.

Let us also note that the even interpolation basis {an(x)}n is deﬁned using the kernel

- K(τ, z) := K+(τ, z) + K−(τ, z), and the odd interpolation basis {cn(x)}n is deﬁned using the kernel K(τ, z) := −K(z, τ). Thus, even though we have dealt with even and odd interpolation problems separately, there is a nice duality between the two.


Remark. As in the even case, using the explicit formula for the kernels, we get d+m ′(0) = δm,0, d−m ′(0) = −r3(m), m ≥ 1,

where r3(m) is the number of representations of m as the sum of squares of 3 integers. Taking x = 0 in (40) we get the following identity

r3(n)i f(√n) √n

r3(n)f(√n) √n

∞

∞

![image 164](<2017-radchenko-fourier-interpolation-real-line_images/imageFile164.png>)

![image 165](<2017-radchenko-fourier-interpolation-real-line_images/imageFile165.png>)

= i f ′(0) +

f′(0) +

,

![image 166](<2017-radchenko-fourier-interpolation-real-line_images/imageFile166.png>)

![image 167](<2017-radchenko-fourier-interpolation-real-line_images/imageFile167.png>)

![image 168](<2017-radchenko-fourier-interpolation-real-line_images/imageFile168.png>)

![image 169](<2017-radchenko-fourier-interpolation-real-line_images/imageFile169.png>)

n=1

n=1

valid for arbitrary odd Schwartz functions. As was pointed out to us by Yves Meyer, this formula was previously found by Guinand [8, p. 265].

8. Open questions and concluding remarks Let us indicate some further directions and observations related to Theorem 1.

Function space. In this paper we have only worked with the space of Schwartz functions, but it is interesting to ask in what generality the interpolation formula (2) holds. The best possible scenario would be a positive answer to the following question.

Question 1. Do the results of Theorems 1 and 7 hold whenever the sum on the right-hand side is well-deﬁned and converges absolutely?

Even to ﬁnd explicit conditions for when the convergence is absolute, one would need

to obtain exact bounds on the growth of bεn(x), which appears to be diﬃcult. Let us outline a simple approximation argument that shows that the interpolation formula is

true whenever both f and f decay suﬃciently fast:

- Proposition 4. Let f be an even integrable function. If f(x) and f(x) are both bounded by (1 + |x|)−13, then the summation formula (2) holds.


Proof sketch. Indeed, for every T > 0 consider the following linear operator RT that takes values in S:

∞

2/T

2

RT(f)(x) = T1/2ei/T · (eiT ∗ f)(x) = T1/2e−πx

f(x − y)e−πTy

dy. The Fourier transform is then given by

−∞

∞

2−π(x−y)2/Tdy. Then a routine calculation shows that

RT(f)(x) = T1/2eiT ∗ (ei/T · f)(x) = T1/2

f(x − y)e−πTy

−∞

2/T)|f(x)| + T−1/2 max

|RT(f)(x) − f(x)| ≪ (1 − e−πx

|f′(y)|, and similarly

y∈[x−1,x+1]

e−πx2T/(1+T2) √1 + T−2 | f(x)| + T−1/2 max

| f′(y)|.

| RT(f)(x) − f(x)| ≪ 1 −

![image 170](<2017-radchenko-fourier-interpolation-real-line_images/imageFile170.png>)

![image 171](<2017-radchenko-fourier-interpolation-real-line_images/imageFile171.png>)

y∈[x−1,x+1]

By summing up these estimates for x = √n over n ≥ 1 and taking the limit as T → ∞ we see that the proof will be complete if we can show that f′(x) and f′(x) decay as (1 + |x|)−l for some l > 6 (since an(x) = O(n2)). We consider only bounding f′(x), since one can obtain the other estimate by interchanging f and f. It was pointed out to the authors by Emanuel Carneiro that this can be done using the following simple observation: if g is a C2-smooth function on [1, ∞) that satisﬁes |g(x)| ≪ x−k and |g′′(x)| ≪ 1 then |g′(x)| ≪ x−k/2. Indeed, then by the Fourier inversion formula we have |f′′(x)| ≪ 1, so we can apply the observation to get |f′(x)| ≪ (1 + |x|)−13/2, and thus we are done.

![image 172](<2017-radchenko-fourier-interpolation-real-line_images/imageFile172.png>)

To prove the above observation: let |g′′(x)| ≤ 1 and |g(x)| ≤ Cx−k. Then Taylor’s theorem with remainder in the Lagrange form implies that for any ∆ ≥ 0 we have

∆2 2

|g(x + ∆) − g(x) − g′(x)∆| ≤

, from which we get, taking ∆ = 2

![image 173](<2017-radchenko-fourier-interpolation-real-line_images/imageFile173.png>)

√

![image 174](<2017-radchenko-fourier-interpolation-real-line_images/imageFile174.png>)

Cx−k, that |g′(x)| ≤

√

2Cx−k ∆

∆ 2

![image 175](<2017-radchenko-fourier-interpolation-real-line_images/imageFile175.png>)

C x−k/2,

+

= 2

![image 176](<2017-radchenko-fourier-interpolation-real-line_images/imageFile176.png>)

![image 177](<2017-radchenko-fourier-interpolation-real-line_images/imageFile177.png>)

- as required.


Note that the number “13” in the above proposition can be improved by using more careful estimates. Relation to the Laplace transform. The basis functions that we have constructed are all of the shape

1

- 1

![image 178](<2017-radchenko-fourier-interpolation-real-line_images/imageFile178.png>)

- 2


2zdz

g(z)eiπx

f(x) =

−1

for some weakly holomorphic modular form g (in the odd case, f is multiplied by x). To get an alternative expression for f we can shift the contour of integration to the rectangular line passing through −1, −1+iT, 1+iT, and 1. A simple computation then shows that

T

1

2tdt + e−πx

2T

2

f(x) = sin(πx2)

g(1 + it)e−πx

g(s + iT)eiπsx

ds.

0

−1

If we take T to inﬁnity, then we see that for all x2 greater than the order of the pole of g

- at i∞ we have


∞

2tdt.

f(x) = sin(πx2)

g(1 + it)e−πx

0

The integral on the right is simply the Laplace transform of g(1+it) evaluated at πx2. This can be used to show that all but ﬁnitely many real zeros of b±

√n. Combined with the q-expansion of g(1 + z) at inﬁnity, this also implies that b±

![image 179](<2017-radchenko-fourier-interpolation-real-line_images/imageFile179.png>)

m(x) are of the form ±

m extends analytically to an entire function. Alternatively, this also follows directly from the deﬁnition (22).

Sine-sinh ratio. The function d+0 (x) is quite special. Recall that it is deﬁned by d+0 (x) =

1

- 1

![image 180](<2017-radchenko-fourier-interpolation-real-line_images/imageFile180.png>)

- 2


2zdz. Changing the contour of integration as before, we get

θ(z) xeiπx

−1

∞

2tdt. Next, integrating the q-expansion of θ termwise and using the identity

d+0 (x) = xsin(πx2)

θ(1 + it)e−πx

0

(−1)n π(x2 + n2)

1 xsinh(πx) we ﬁnd that d+0 (x) is, in fact, an elementary function:

=

![image 181](<2017-radchenko-fourier-interpolation-real-line_images/imageFile181.png>)

![image 182](<2017-radchenko-fourier-interpolation-real-line_images/imageFile182.png>)

n∈Z

sin(πx2) sinh(πx)

d+0 (x) =

.

![image 183](<2017-radchenko-fourier-interpolation-real-line_images/imageFile183.png>)

√n for all n ≥ 0. It follows from Theorems 1 and 7 that any Schwartz function with this property is of the form αd+0 .

Note that d+0 (x) and its Fourier transform d+0 (x) = (−i)d+0 (x) both vanish at x = ±

![image 184](<2017-radchenko-fourier-interpolation-real-line_images/imageFile184.png>)

It appears that this function was ﬁrst considered by Ramanujan in [14], where he studies a number of integrals involving similar expressions, and, in particular, shows the Fourier invariance of d+0 (see [14, eq. 34]). It is also directly related to the so-called Mordell integral [12], which played an important role in Zwegers’s seminal work on mock theta functions [22].

References

- [1] B. C. Berndt, M. I. Knopp, Hecke’s Theory of Modular Forms and Dirichlet Series, World Scientiﬁc

(2008).

- [2] H. Cohn, N. Elkies, New upper bounds on sphere packings I, Ann. of Math. (2) 157, no. 2, pp. 689– 714 (2003).
- [3] H. Cohn, A. Kumar, S. D. Miller, D. Radchenko, and M. S. Viazovska, The sphere packing problem in dimension 24, Ann. of Math. 185 (3), pp. 1017–1033 (2017).
- [4] J. H. Curtiss, Faber polynomials and the Faber series, Amer. Math. Monthly 78, pp. 577–596 (1971).
- [5] W. Duke, P. Jenkins, On the zeros and coeﬃcients of certain weakly holomorphic modular forms, Pure Appl. Math. Q. 4, pp. 1327–1340 (2008).
- [6] M. Eichler, Eine Verallgemeinerung der Abelschen Integrale, Math. Zeit. 67, pp. 267–298 (1957).
- [7] J. R. Higgins, Five short stories about the cardinal series, Bull. Amer. Math. Soc. 12 (1), pp. 45–89

(1985).

- [8] A. P. Guinand, Concordance and the harmonic analysis of sequences, Acta Math. 101, pp. 235–271

(1959).

- [9] M. I. Knopp, Some new results on the Eichler cohomotogy of automorphic forms, Bull. Am. Math. Soc. 80, pp. 607–632 (1974).
- [10] M. I. Knopp, On the growth of entire automorphic integrals, Result. Math. 8, pp. 146–152 (1985).


- [11] Y. F. Meyer, Measures with locally ﬁnite support and spectrum, Proc. Nat. Acad. Sci. 113 (12), pp. 3152–3158 (2016).
- [12] L. J. Mordell, The value of the deﬁnite integral −∞ ∞ e

at2+bt

![image 185](<2017-radchenko-fourier-interpolation-real-line_images/imageFile185.png>)

ect+d dt, Quarterly J. of Math 68, pp. 329–342

(1920).

- [13] D. Mumford, Tata Lectures on Theta: Jacobian theta functions and diﬀerential equations, Progress in mathematics, Birkh¨user (1983).
- [14] S. Ramanujan, Some Deﬁnite Integrals connected with Gauss’s sums, Mess. Math. 44, pp. 75–85

(1915).

- [15] C. E. Shannon, Communications in the presence of noise, Proc. IRE 37, pp. 10–21 (1949).
- [16] J. D. Vaaler, Some extremal functions in Fourier analysis, Bull. Amer. Math. Soc., 12 (2), pp. 183– 216 (1985).
- [17] M. S. Viazovska, The sphere packing problem in dimension 8, Ann. of Math. 185 (3), pp. 991–1015

(2017).

- [18] V. S. Vladimirov, Methods of the theory of generalized functions, Analytical Methods and Special Functions, 6, London (2002).
- [19] E. T. Whittaker, On the functions which are represented by the expansions of the interpolation theory, Proc. Royal Soc. Edinburgh., 35, pp. 181–194 (1915).
- [20] D. Zagier, Traces of singular moduli, in Motives, Polylogarithms and Hodge Theory, Part I. International Press Lecture Series (Eds. F. Bogomolov and L. Katzarkov), pp. 211–244 (2002).
- [21] D. Zagier, Elliptic modular forms and their applications, in The 1-2-3 of Modular Forms (K. Ranestad, ed.), pp. 1–103, Universitext, Springer, Berlin (2008).
- [22] S. Zwegers, Mock Theta Functions, Thesis, Universiteit Utrecht, 2002.


The Abdus Salam International Centre for Theoretical Physics, Str. Costiera 11,

34151 Trieste, Italy E-mail address: danradchenko@gmail.com Ecole´ Polytechnique F´ed´erale de Lausanne, 1015 Lausanne, Switzerland E-mail address: viazovska@gmail.com

