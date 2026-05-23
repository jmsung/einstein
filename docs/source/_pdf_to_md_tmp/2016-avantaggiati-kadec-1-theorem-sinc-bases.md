## KADEC-1/4 THEOREM FOR SINC BASES.

ANTONIO AVANTAGGIATI, PAOLA LORETI, PIERLUIGI VELLUCCI

# arXiv:1603.08762v1[math.FA]29Mar2016

Abstract. In this paper we show two results. In the ﬁrst result we consider λn − n = nAα for n ∈ N; if α > 1/2 and 0 < A < 1

√

, the system {sinc(λn − t)}n∈N is a Riesz basis for PWπ. With the second result, we study the stability of {sinc(λn − t)}n∈Z for λn ∈ C; if |λn − n| L < π1 38α, for all n ∈ Z, then {sinc(λn − t)}n∈Z forms a Riesz basis for PWπ. Here α is the Lamb-Oseen constant.

2√2ζ(2α)

π

Contents

- 1. Introduction 1
- 2. Preliminaries 3

- 2.1. Sampling Theorem and Stability 3
- 2.2. Lambert function W, Lamb-Oseen constant. 5
- 3. Proof of the results 6


- 3.1. Proof of Proposition 1 6


- 3.2. Proof of Theorem 2 7
- 3.3. Proof of Theorem 3. 9
- 4. Tables 11 References 12


1. Introduction Let f be a function which can be expanded as

- (1) f(t) =

n∈Z

cn sinc(t − n)

where

- (2) sinc(α) =


sin(πα)

πα α = 0, 1 α = 0,

is the normalized sinc function. The RHS of (1) is called “cardinal series” or Whittaker cardinal series. A major factor aﬀecting current interest in the cardinal series is its importance for certain applications as, for example, interpolation based on (1) which is usually called ideal bandlimited interpolation (or sinc interpolation), because it provides a perfect reconstruction for all t, if f(t) is bandlimited in [−π,π] and if the sampling frequency is greater that the so-called Nyquist rate. The system used to implement (1) is also known in in engineering applications as ideal DAC (i.e. digital-to-analog converter, see [16]). The presence of the perturbation could lose the correct reconstruction of the function (signal), so it is important to study the conditions for which the system is still able to reconstruct the function (signal) belonging to a given space. Other applications are sampling theory of band-limited signals in communications engineering [9] or sinc-quadrature method for diﬀerential equations [15]. The so-called sinc numerical methods of computation, provide procedures for function approximation over bounded or unbounded regions, encompassing interpolation, approximation of derivatives, approximate deﬁnite and

1

![image 1](<2016-avantaggiati-kadec-1-theorem-sinc-bases_images/imageFile1.png>)

- Figure 1. Left: A function f deﬁned on R has been sampled on a uniformly spaced set. Right: The same function f has been sampled on a non-uniformly spaced set.

![image 2](<2016-avantaggiati-kadec-1-theorem-sinc-bases_images/imageFile2.png>)

- Figure 2. Sampling grids. Left: uniform cartesian sampling. Right: A typical nonuniform sampling set as encountered in various signal and image processing applications.


indeﬁnite integration, and so on [22]. These problems motivated our investigation on sinc systems.

For these reasons, the cardinal series have been widely discussed in the literature; see also [27] and [28]. They are linked to a classical basis, the exponentials {eint}n∈Z in L2(−π,π), through the Fourier transform, indeed formally

π

ei(µ−ξ)tdt = 2π sinc(µ − ξ).

F eitµχ[−π,π] (t) (ξ) =

−π

nt}n∈Z ﬁnd their origin in the celebrated 1934’s work of Paley and Wiener [18] in L2(0,T), where T > 0. They proved that if λn ∈ R,n ∈ Z and

Studies on more general exponential systems {eiλ

|λn − n| ≤ L < π−2 n ∈ Z then the system {eiλ

nt}n∈Z forms a Riesz basis in L2[−π,π]. A well-known theorem by Kadec [12], [29] shows that 1/4 is a stability bound for the exponential basis on L2(−π,π), in the sense that for L < 1/4, {eiλ

nt}n∈Z is still a Riesz basis in L2(−π,π). More than 60 years after Paley and Wiener initiated the study of nonharmonic Fourier series in L2[−π,π], many other approaches to exponential Riesz basis problem have emerged in the literature. For other contributions to exponential Riesz basis problem and Kadec’s theorem see survey papers, as: [20], [25].

For the system of cardinal sines {sinc(t − n)}n∈Z we tried to follow the same approach. For simplicity, we refer to {sinc(t − n)}n∈Z with terms of “sinc system” or sinc basis.

The results of this paper are the following theorems.

First of all, we recall and prove the classical result (see also [1]). Below, we denote with PWπ the Paley-Wiener space. Proposition 1. Let {λn}n∈Z be a sequence of real numbers for which

- (3) |λn − n| L < ∞, n = 0,±1,±2,... If L < 14, the sequence {sinc(λn − t)}n∈Z satisﬁes the Paley-Wiener criterion and so forms a Riesz basis for PWπ. Moreover, constant 1/4 is optimal.

The subsequent results have been achieved in an attempt to reobtain the optimal constant 1/4 without going to the exponential basis, i.e. working directly on cardinal series. Let us consider the following two results.

- Theorem 2. Let λn − n = nA

α

for n = 1,2,3,.... If α > 1/2 and 0 < A < 1

π

√

2√2ζ(2α)

then

the system {sinc(λn − t)}n∈N satisﬁes the Paley-Wiener criterion and so forms a Riesz basis for PWπ.

Numerical evaluation in the case λn − n = nA

α

is given in Section 4; in the Tables are showed

that, when α = 1, for increasing value of A until A 0.443..., the system {sinc(λn − t)}n∈N is a Riesz basis in PWπ. If n = 1,2,..., we have that λn −n ≤ L where L is greater ( 0.443...)

of Kadec’s bound. This is due to the assumption λn − n = nA

α

, that is, to have considered a non-uniform stability bound.

In Section 3.3 we study the stability of {sinc(λn − t)}n∈Z for λn ∈ C, reobtaining a stability bound which depends from Lamb-Oseen constant [17]. This constant was also appeared in previous work [1] although the stability bound was not correct.

In a previous work one of the author studied the extension to complex numbers of Kadec type estimate for exponential bases [26]. The method used there is inspired to work by Duﬃn and Eachus [7]. In [1] we performed a preliminary study by adacting a previous result on sinc. Here we give a complete result by the following theorem.

- Theorem 3. If {λn} is a sequence of complex numbers for which


- (4) |λn − n| L <


1 π

3α 8

, n = 0,±1,±2,... then {sinc(λn−t)}n∈Z satisﬁes the Paley-Wiener criterion and so forms a Riesz basis for PWπ. Observe that the optimality of the bound for the complex case is not studied in our result.

2. Preliminaries

In this section we will introduce some useful notations and results about cardinal series, with reference to applications in sampling. Furthermore, we give a small overview on the Lamb-Oseen constant [17] which is involved in the estimation for the complex case.

- 2.1. Sampling Theorem and Stability. By L2(−∞,+∞) we denote the Hilbert space of real functions that are square integrable in Lebesgue’s sense:


+∞

L2(R) = f :

|f(t)|2dt < +∞ with respect to the inner product and L2-norm that, on R, are

−∞

∞

- 1

- 2π


f(t)g(t)dt ||f|| = f,f Given f ∈ L2(R) we denote by F(f) the Fourier transform of f,

f,g =

−∞

+∞

f(t)e−iξtdt.

F (f)(ξ) =

−∞

Let en be an orthonormal basis of an Hilbert space H. Then Parseval’s identity asserts that for every x ∈ H,

| x,en |2 = x 2. Plancherel identity is expressed, in its common form: ∞

n

∞

- 1

- 2π


F (f)(ξ)F (g)(ξ)dξ.

f(t)g(t)dt =

−∞

−∞

A function f ∈ L2(R) is band-limited if the Fourier transform F (f) has compact support. The Paley-Wiener space PWπ is the subspace of L2(R) deﬁned by

PWπ := f ∈ L2(R) suppF (f) ⊆ [−π,π] .

We will now recall that the Paley-Wiener space has an orthonormal basis consisting of translates of sinc-function.

- Theorem 4. (Shannon’s sampling theorem) [5], [11], [14], [21]. The functions {sinc(·−n)}n∈Z form an orthonormal basis for PWπ. If f ∈ PWπ is continuous, then

(5) f(t) =

n∈Z

f(n) sinc(t − n).

Taking the Fourier transform in equation (5) we obtain

(6) F (f)(ξ) =

n∈Z

F (f),einξ L

2(−π,π) einξ,

where g,h L2(−π,π) = 21π − ππ g(ξ)h(ξ)dξ.

Usually, it is said that bases in Banach spaces form a stable class in the sense that sequences suﬃciently close to bases are themselves bases. The fundamental stability criterion, and historically the ﬁrst, is due to Paley and Wiener [18], [29].

- Theorem 5. Let {xn} be a basis for a Banach space X, and suppose that {yn} is a sequence of elements of X such that

n

i=1

ai(xi − yi) ≤ λ

n

i=1

aixi

for some constant 0 λ < 1, and all choices of the scalars a1,...,an (n = 1,2,3,...). Then {yn} is a basis for X equivalent to {xn}.

We reformulate Theorem 5 to be applied to orthonormal bases.

- Theorem 6. Let {en} be an orthonormal basis for a Hilbert space H, and let {fn} be “close”

to {en} in the sense that

n

i=1

ai(ei − fi) ≤ λ |ci|2

for some constant 0 λ < 1, and all choices of the scalars a1,...,an (n = 1,2,3,...). Then {fn} is a Riesz basis for H.

- Theorem 7 (Kadec 41-Theorem). Let {λn}n∈Z be a sequence in R satisfying


1 4

, n = 0,±1,±2,... then the set {eiλ

|λn − n| <

nt}n∈Z is a Riesz basis for L2[−π,π].

Kadec’s theorem has been extensively generalized. See, for example [2], [3], [13], [19], [24], [26].

![image 3](<2016-avantaggiati-kadec-1-theorem-sinc-bases_images/imageFile3.png>)

Figure 3. Diagram of ξeξ = f(ξ).

- 2.2. Lambert function W, Lamb-Oseen constant. The Lambert function W [6], [8], [23] is deﬁned by the equation


- (7) W(x)eW(x) = x

The function f(ξ) = ξeξ for ξ ∈ R has a strict minimum point in ξ = −1. We draw the picture of ξeξ = f(ξ) in ﬁgure (3). In [1] it is proved the following proposition.

Proposition 8. The function f(ξ) = ξeξ has an increasing inverse in (−1,+∞), and a decreasing inverse in (−∞,−1).

We consider f(ξ) = ξeξ restricted to the interval (−∞,−1] and we denote by W−1 its inverse. W−1 is deﬁned in the interval [−1/e,0). We have two identities arising from the deﬁnition of W−1:

- (8) W−1(ξeξ) = ξ, ⇔ W−1 [f(ξ)] = W−1 ξeξ = ξ ∀ξ ∈ (−∞,−1] and
- (9) W−1(¯x)eW−1(¯x) = x¯ [⇒ f (W−1(¯x)) = x¯]∀x¯ ∈ [−

1 e

,0)

Also we denote by W0 the restriction to the interval [−1/e,0) of the increasing inverse of f(ξ) = ξeξ. The two identities hold true:

- (10) W0(ξeξ) = ξ, ⇔ W0 [f(ξ)] = W0 ξeξ = ξ , ∀ξ ∈ [−1,0) and
- (11) W0(¯x)eW

0(¯x) = x¯ [⇒ f (W0(¯x)) = x¯] ∀x¯ ∈ [−

1 e

,0)

- 2.2.1. Numerical values. Let us assume that x¯ is a solution of our equation.


- (12) ex¯ − 2¯x = 1 In order to use the Lambert function W, we observe that from (12) we get the equivalences

ex¯ − 2¯x = 1 ⇔ ee

x¯−2¯x = e

whence −21ex¯e− −1e < −12e− which veriﬁes the same equation W(x)eW(x) = −12e−

- 1

- 2ex¯ = −12e−


- 1

- 2. Therefore we can identiﬁes −21ex¯ with W −21e−


- 1

- 2 . Since


- 1

- 2 < 0, the equation which deﬁnes the function W of Lambert, has two branches


- 1

- 2 and we will have


- (13) − 12ex¯ = W0 −21e−


- 1

- 2


and

- (14) − 12ex¯ = W−1 −21e−

- 1

- 2 .


We call x¯1 the x¯ solution of (13), and x¯2 the solution of (14). We state easy that x¯1 = 0. In fact from (13) we have

−12ex¯

1

= −12 = W0 −21e− and from ex¯

- 1

- 2


1

= 1, easily follows x¯1 = 0. From (14), and the relation (9) we get ex¯

2

= −2W−1 −21e−

- 1

- 2 , and so x¯2:


ln −2W−1 −12e−

- 1

- 2 = −ln


1

−2W−1 −12e− Now we multiply numerator and denominator by e

- 1

- 2


- 1

- 2


= −ln

 

−21e− W−1 −12e−

- 1

- 2


- 1

- 2


e

- 1

- 2


  = −

- 1

- 2 − ln −12e− W−1 −21e−


- 1

- 2


- 1

- 2


By (9) we have

x¯2 = −

- 1

- 2 − W−1 −12e−


- 1

- 2 .


The value −21 − W−1 −12e− denoted by α. Numerical estimates give

- 1

- 2 is called the parameter of Oseen, or Lamb-Oseen constant,


α = 1.25643...

We have introduced the Lambert function W in order to give an useful expression to the root of equation

- (15) eα = 2α + 1.


In [1] we have proved that the real number α is transcendental, through application of the Lindemann - Weierstrass theorem [4].

3. Proof of the results In the following we give the results of the paper.

- 3.1. Proof of Proposition 1. Proof of Proposition 1. Write


2

cn (sinc(n − ξ) − sinc(λn − ξ))

λ :=

.

n

L2(R)

The Fourier transform of the function t → eitµχ[−π,π](t) is ξ → 2π sinc(µ − ξ). In fact: F eitµχ[−π,π](t) (ξ) =

π

ei(µ−ξ)tdt = 2π sinc(µ − ξ). By Plancherel’s theorem

−π

2

2

cnχ[−π,π](t) eint − eiλ

nt

cn (sinc(n − ξ) − sinc(λn − ξ))

=

n

n

L2(R)

L2(R)

2

### cn eint − eiλ

nt

### =

n

L2(−π,π)

and so, following the proof of Kadec’s theorem (see e.g. [29]), when L < 14 then λ ≤ 1 − cos(πL)−sin(πL) < 1. Since {sinc(n − ξ)} is a Riesz basis of PWπ, the Paley-Wiener criterion shows that also {sinc(λn − ξ)} is a Riesz basis of PWπ.

Constant 1/4 is optimal also for {sinc(λn − ξ)}. A counterexample due to Ingham [10] prove that the set {eiλ

nt} is not a Riesz basis of L2(−π,π) when

- (16) λn =

 



n + 41, n > 0 0, n = 0

n − 14, n < 0

Since PWπ is isometrically equivalent to L2(−π,π) via Fourier transform, the set {sinc(λn − ξ)} is not a Riesz basis.

Corollary 9. Let {x n}n∈Z be a system biorthogonal to {sinc(· − λn)}n∈Z. Let {λn}n∈Z be a sequence of real numbers for which

- (17) |λn − n| L < ∞, n = 0,±1,±2,... If L < 41, and if f ∈ PWπ is continuous, then

- (18) f(t) =

n∈Z

f,x n PW

π

sinc(t − λn).

Proof. Let {λn}n∈Z be a sequence of real numbers for which

- (19) |λn − n| L <

1 4

, n = 0,±1,±2,...

We denote with the sequence {xn}n∈Z the system sinc(t − λn). From Theorem 1, the sequence {xn}n∈Z forms a Riesz basis.

Recall that a sequence {xn}n∈Z in an Hilbert space H is a Riesz basis if and only if any element x ∈ H has a unique expansion x = n∈Z cnxn with {cn}n∈Z ∈ 2. If {xn}n∈Z is a Riesz basis, then in the above expansion the Fourier coeﬃcients cn are given by cn = x,x n , where {x n}n∈Z is a system biorthogonal to {xn}n∈Z, i.e., a system which satisﬁes the condition

xk,x n = δk,n for all k, n ∈ Z.

- 3.2. Proof of Theorem 2. In order to prove Theorem 2, we prove the following Lemma.


- Lemma 10. Deﬁne


I =

n

cn [sinc(λn − t) − sinc(n − t)]

2

L2(R)

.

Then

- (20) I ≤ 2

n

[1 − sinc(λn − n)], n = 0,±1,±2,....

Proof. Write,

- (21) I =

n

cn [sinc(λn − t) − sinc(n − t)]

2

L2(R)

.

First, we develop function sinc(λn − t) respect to basis {sinc(λn − t)}n∈Z. We ﬁnd:

- (22) sinc(λn − t) =

k∈Z

sinc(λn − k)sinc(k − t)

The convergence in L2(R) is insured by

- (23)


sinc2(λn − k) =

sinc2(λn − t)dt = 1

R

k∈Z

Thanks to equation (22) we obtain:

- (24)

n

cn [sinc(λn − t) − sinc(n − t)] =

n

cn

k∈Z

[sinc(λn − k) − sinc(n − k)]sinc(k − t).

This transformation is obvious because sinc(n − k) =

- 0 for n,k ∈ Z and n = k
- 1 for n = k.


We obtain, substituting in (21):

I =

n

cn

k∈Z

[sinc(λn − k) − sinc(n − k)]sinc(k − t)

2

L2(R)

=

k∈Z n

cn [sinc(λn − k) − sinc(n − k)] sinc(k − t)

2

L2(R)

- (25)

Applying the Parseval equality,

I =

k∈Z n

cn [sinc(λn − k) − sinc(n − k)]

2

Using Ho¨lder-Schwarz to the sum of products contained in the absolute value, and the condition on n |cn|2 ≤ 1 we have:

I ≤

k∈Z n

[sinc(λn − k) − sinc(n − k)]2 =

=

n k∈Z\{n}

- (26) sinc2(λn − k) + (sinc(λn − n) − 1)2

From (23),

- (27)

k∈Z\{n}

sinc2(λn − k) = 1 − sinc2(λn − n)

Finally, from (26) and (27), we obtain

- (28) I ≤ 2


[1 − sinc(λn − n)].

n

- Proof of Theorem 2. Let us consider


I ≤ 2

n

[1 − sinc(λn − n)]

for λn − n = nA

:

α

A nα

I ≤ 2

1 − sinc

n

Since, for x ∈ (0,π/2) 1 −

sin2 x cosx(1 + cosx) ≤

sin2 x cosx

sinx x

sinx x

x sinx − 1 ≤

1 cosx − 1 =

, we have:

=

sin2 πAn

A nα ≤ 2

α

I ≤ 2

1 − sinc

### .

cos πAn

α

n

n

α ∈ 0, π2 . Let, for example, πAn

It is veriﬁed if πAn

α ∈ 0, π4 . Hence, I ≤ 2

√

√

sin2 πAn

1 n2α

α

2(πA)2

2(πA)2ζ(2α).

≤ 2

= 2

cos πAn

α

n

n

Then

√

2(πA)2ζ(2α) < 1 if

I ≤ 2

1 π 2√2ζ(2α)

A <

.

Moreover, ζ(2α) < 1 and, under condition on A and for α > 1/2, it is conﬁrmed that πAn

α ∈ 0, π4 .

3.3. Proof of Theorem 3. In this Section we study the system {sinc(λn − t)}n∈Z for λn ∈ C and |λn − n| ≤ L < ∞. First, we state the following Lemma whose proof is left to the reader.

- Lemma 11. Let n, k ∈ N. The Fourier transform of the function t → dtdkk


sinc(t − n) is ξ → (iξ)kχ[−π,π](t)e−inξ.

The following is a stability result for {sinc(λn −t)}n∈Z when λn ∈ C. The result involves the Lamb-Oseen constant, as already announced in [1]. However the stability bound for the case λn ∈ C is π1 38α (and not απ, as written in [1]).

- Proof of Theorem 3. Let us consider,


2

### (29) I =

n

cn [sinc(λn − t) − sinc(n − t)]

.

L2(R)

whenever n |cn|2 1. We use the Taylor series of sinc(λn − t):

+∞

(λn − n)k k!

dk dxk

sinc(n − t) +

sinc(x − t)

x=n

k=1

Then

### (30)

I =

n

+∞

(λn − n)k k!

dk dxk

cn

k=1

=

+∞

1 k! n

k=1

cn (λn − n)k

+∞

1 k! n

≤

k=1

cn (λn − n)k

2

sinc(x − t)

x=n

L2(R)

2

dk dxk

sinc(x − t)

x=n

L2(R)

2

dk dxk

sinc(x − t)

x=n

L2(R)

### The term · is reducible to

n

cn (λn − n)k

dk dxk

sinc(x − t)

x=n

2

=

L2(R)

=

anam

n,m

dk dxk

sinc(x − t)

,

x=n

dk dxk

sinc(x − t)

x=m L2(R)

where an := cn (λn − n)k. Observing that

= −dtdkk

dk dxk

sinc(t − n), k odd

sinc(x − t)

dk

dtk sinc(t − n), k even i.e., dxdk

x=n

### = (−1)kdtdk

sinc(x − t)

sinc(t − n). Then dk dxk

k

k

x=n

dk dxk

sinc(x − t)

sinc(x − t)

,

x=n

x=m L2(R)

dk dtk

dk dtk

(−1)k

sinc(t − n)(−1)k

- (31) sinc(t − m)dt From Plancherel’s equality and Lemma 11, we have

R

(−1)k

dk dtk

sinc(t − n)(−1)k

dk dtk

sinc(t − m)dt =

1 2π

π

−π

ξ2k ei(m−n)ξ dξ. Hence,

- (32)

dk dxk

sinc(x − t)

x=n

,

dk dxk

sinc(x − t)

x=m L2(R)

=

- 1

- 2π


π

−π

ξ2k ei(m−n)ξ dξ.

Taking equation (32) in (30), we obtain:

I ≤

- 1

- 2π


+∞

k=1

1 k! n,m

anam

π

−π

ξ2k ei(m−n)ξ dξ := ω1 + ω2

where ω1, ω2 are the cases, respectively, when n = m and n = m. Thereby,

- (33) ω1 =

1 π

+∞

k=1

1 k! n |an|2

π

0

ξ2k dξ ≤

+∞

k=1

(πL)2k k!(2k + 1)

.

and using integration by parts for ω2, we see that

ω2 =

- 1

- 2π


+∞

k=1

1 k! n,m

n =m

an am i(m − n)

π

−π

ξ2k ei(m−n)ξ dξ

=

- 1

- 2π


+∞

k=1

1 k! n,m

n =m

an am i(m − n)

ξ2k ei(m−n)ξ π−π − 2k

π

−π

ξ2k−1 ei(m−n)ξdξ

=

i π

+∞

k=1

1 (k − 1)! n,m

n =m

an am m − n

π

−π

- (34) ξ2k−1 ei(m−n)ξdξ.


=

R

Putting double series into integral,

i π

ω2 =

+∞

1 (k − 1)!

k=1

π

ane−inξ ame−imξ m − n

ξ2k−1

dξ

−π

n,m n =m

and denoting bn := ane−inξ, ω2 is estimable from above as:

1 π

|ω2| ≤

+∞

1 (k − 1)!

k=1

π

|ξ|2k−1

−π

bnbm m − n

n,m n =m

dξ.

From Hilbert’s inequality for the double series into the integral, we obtain

- (35) |ω2| ≤

+∞

k=1

1 (k − 1)!

π

−π

|ξ|2k−1

n

|bn|2 dξ ≤

+∞

k=1

(πL)2k k!

.

Then,

I ≤ |ω1| + |ω2| ≤

+∞

k=1

(πL)2k k!(2k + 1)

+

+∞

k=1

(πL)2k k!

=

+∞

k=1

(πL)2k k!

1 +

- 1

- 2k + 1


.

We notice that

(πL)2k k!

1 +

- 1

- 2k + 1 ≤


(πL)2k (k + 1)!

8 3

k

for all k ∈ N and, in fact,

2

k + 1 2k + 1 ≤

1 k + 1

8 3

k

is veriﬁed for all k ∈ N. Only for k = 1 the above inequality becomes an equality. Accordingly,

I ≤

+∞

k=1

xk (k + 1)!

=

1 x

(ex − x − 1), where x =

8 3

π2L2.

Set λ = x1 (ex − x − 1) where x = 38 π2L2. In order to get λ < 1, we solve, in a ﬁrst moment, the equation λ = 1, that is

- (36) ex = 2x + 1

We obtain same useful properties on the solutions of equation (36), using the Lambert Function W.

Numerical estimates give

1 π

3α 8

= 0.218492....

4. Tables Let

- (37) I ≤ 2


∞

[π(λn − n)]2l (2l + 1)! In order to numerically valuate I let, for n = 1,2,3,...,

(−1)l+1

[1 − sinc(λn − n)] = 2

n

n

l=1

A nα

- 1

- 2


λn − n =

. Substituting in (37) we obtain

, where α >

I ≤ 2

n

∞

(πA)2l (2l + 1)!

1 n2lα

(−1)l+1

l=1

= 2

∞

(πA)2l (2l + 1)!

(−1)l+1

ζ(2αl)

l=1

where ζ(2lα) is the Riemann zeta function. We have the estimate

I ≤ 2

∞

(πA)2l (2l + 1)!

(−1)l+1

+ 2

l=1

∞

(πA)2l (2l + 1)!

(−1)l+1

l=1

[ζ(2αl) − 1]

= 2(1 − sincA) + 2

∞

(πA)2l (2l + 1)!

(−1)l+1

l=1

[ζ(2αl) − 1]

In the following we evaluate numerically the expression λ := 2 1 −

∞

(πA)2l (2l + 1)!

sinπA πA

(−1)l+1

[ζ(2lα) − 1].

+ 2

l=1

Parameters α and A derive from position λn−n = nA

, for α > 12 and A > 0. From Paley-Wiener λ must be less than 1. For a better comprehension we ﬁx:

α

∞

(πA)2l (2l + 1)!

sinπA πA

(−1)l+1

λ1 = 2 1 −

[ζ(2lα) − 1]

, λ2 = 2

l=1

Below we try with A = 0.25 and varying α.

α A λ1 λ2 λ

0.7 0.25 0.199367 0.431376 0.630743 0.65 0.25 0.199367 0.600929 0.800296 0.63 0.25 0.199367 0.705618 0.904986 0.62 0.25 0.199367 0.771134 0.970502 0.61599 0.25 0.199367 0.800596 0.999963

Notice that for λn − n = 0n.25

(0.25 is just the Kadec’s bound for exponential bases), when we have, for example, α = 0.7 (ﬁrst row of previous table) the parameter λ is still far from 1, which is the maximum value for λ in the Paley-Wiener criterion. For decreasing value of α, when α = 0.61599, λ is very close to 1. If n = 1,2,dots, λn − n ≤ 0.25 for all n ∈ N.

α

We now ﬁx α = 1 while A is variable.

α A λ1 λ2 λ

1 0.25 0.199367 0.132089 0.331456 1 0.35 0.379336 0.257921 0.637257 1 0.4 0.486347 0.336085 0.822432 1 0.42 0.531859 0.370154 0.902013 1 0.44 0.578765 0.405809 0.984574 1 0.44366 0.587491 0.412505 0.999996

At this point, we have λn − n = An. When A = 0.25 (ﬁrst row of previous table) the parameter λ is still far from value 1 of λ in the Paley-Wiener criterion. For increasing value of A, when A 0.443..., λ is very close to 1. If n = 1,2,..., λn − n ≤ L where L seems to be approximately 0.443..., which is greater of Kadec’s bound. We have completed here the study announced in [1], giving a whole proof for stability of sinc bases.

References

- [1] A. Avantaggiati, P. Loreti, P. Vellucci, An explicit bound for stability of Sinc Bases, Proceedings of 12-th International Conference on Informatics in Control, Automation and Robotics, (2015), p. 473-480.
- [2] S.A. Avdonin, On the question of Riesz bases of exponential functions in L2, Vestnik Leningrad. Univ. No. 13 Mat. Meh. Astronom. Vyp. 3, 1974, 5-12.
- [3] B. Bailey, Sampling and recovery of multidimensional bandlimited functions via frames, J. Math. Anal. Appl. 367, 2010, 374388.
- [4] A. Baker, Transcendental number theory. Cambridge University Press, 1990.
- [5] O. Christensen, Functions, spaces, and expansions: mathematical tools in physics and engineering. Springer Science & Business Media, 2010.
- [6] R.M. Corless, G.H. Gonnet, D.E.G. Hare, D.J. Jeﬀrey, D.E. Knuth, On the Lambert W function. Advances in Computational mathematics 5.1 (1996): 329-359.
- [7] R.J. Duﬃn, J.J. Eachus, Some notes on an expansion theorem of Paley and Wiener. Bull. Am. Math. Soc. 48, 850-855, (1942).
- [8] B. Hayes, Computing Science: Why W?, American Scientist (2005): 104-108.


![image 4](<2016-avantaggiati-kadec-1-theorem-sinc-bases_images/imageFile4.png>)

2l

Figure 4. Plot of 2 1 − sinπAπA + 2 ∞l=1(−1)l+1 (πA)

(2l+1)! [ζ(2lα) − 1]. Here A = 0.25, horizontal axis is referred to α and the graphics is obtained in the range α ∈ [0.55,1].

- [9] J.R. Higgins, Five short stories about the cardinal series, Bulletin of the American Mathematical Society 12.1 (1985): 45-89.
- [10] A. E. Ingham, Some trigonometrical inequalities with applications to the theory of series, Math. Z. 41

(1936), 367–379.

- [11] A.J. Jerri, The Shannon sampling theoremIts various extensions and applications: A tutorial review, Proceedings of the IEEE 65.11 (1977): 1565-1596.
- [12] M.I. Kadec, The exact value of the PaleyWiener constant, Sov. Math. Dokl. 5, 1964, 559561.
- [13] S. V. Khrushchev, Perturbation theorems for exponential bases and the Mackenhoupt condition, Dokl. Akad. Nauk SSSR, 247, 1979, 4448.
- [14] V.A. Kotelnikov, On the carrying capacity of the ether and wire in telecommunications, Material for the First All-Union Conference on Questions of Communication, Izd. Red. Upr. Svyazi RKKA, Moscow. Vol.

1. 1933.

- [15] J. Lund, K.L. Bowers, Sinc methods for quadrature and diﬀerential equations, SIAM, 1992.
- [16] D.G. Manolakis, V.K. Ingle, Applied digital signal processing: theory and practice. Cambridge University Press, 2011.
- [17] Oseen, C. W. Uber¨ Wirbelbewegung in einer reibenden Flu¨ssigkeit. Almqvist & Wiksells, 1911.
- [18] R. Paley and N. Wiener, Fourier transforms in the complex domain, Amer. Math. Soc. Colloquium Publications vol. 19. Amer. Math. Soc., New York, 1934.
- [19] B.S. Pavlov, Basicity of an exponential system and Muckenhoupt’s condition, Sov. Math. Dokl. 20, 1979, 655-659.
- [20] A. M. Sedletskii, Nonharmonic Analysis, J. Math. Sc., Vol. 116, No. 5, 2009, 3551-3619.
- [21] C.E. Shannon, A mathematical theory of communication, Bell System Technical Journal, Vol. 27 (1948), pp. 379-423; pp. 623-656.
- [22] F. Stenger, Summary of Sinc numerical methods, Journal of Computational and Applied Mathematics 121.1 (2000): 379-420.
- [23] S. Stewart, A New Elementary Function for Our Curricula? Australian Senior Mathematics Journal 19.2

(2005): 8-26.

- [24] W. Sun, X. Zhou, On the stability of multivariate trigonometric systems, J. Math. Anal. Appl. vol. 235, 1999, 159167.
- [25] D. Ullrich, Divided diﬀerences and systems of nonharmonic Fourier series, Proc. Amer. Math. Soc., vol. 80, 1980, 47-57.
- [26] P. Vellucci, A simple pointview for Kadec-1/4 theorem in the complex case, Ricerche di Matematica, 2014, DOI: 10.1007/s11587-014-0217-5.
- [27] E.T. Whittaker, On the functions which are represented by the expansions of the interpolation theory, Proc. Royal Soc. Edinburgh, 35, (1915) 181-194.
- [28] J.M. Whittaker, Interpolatory function theory, Cambridge Tracts in Mathematics and Mathematical Physics, No. 33, Stechert-Hafner, Inc., New York, 1964.
- [29] R. M. Young, An introduction to nonharmonic Fourier series, Academic Press, 2001.


