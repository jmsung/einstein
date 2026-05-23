arXiv:1509.06674v1[math.CA]22Sep2015

A SHARP TRILINEAR INEQUALITY RELATED TO FOURIER RESTRICTION ON THE CIRCLE

EMANUEL CARNEIRO, DAMIANO FOSCHI, DIOGO OLIVEIRA E SILVA AND CHRISTOPH THIELE

Abstract. In this paper we prove a sharp trilinear inequality which is motivated by a program to obtain the sharp form of the L2 − L6 Tomas-Stein adjoint restriction inequality on the circle. Our method uses intricate estimates for integrals of sixfold products of Bessel functions developed in a companion paper [24]. We also establish that constants are local extremizers of the Tomas-Stein adjoint restriction inequality as well as of another inequality appearing in the program.

1. Introduction

Let (S1,σ) denote the unit circle in the plane equipped with its arc length measure. We are interested in the sharp version of the endpoint Tomas-Stein adjoint restriction inequality [32, 31] on the circle:

fσ L6(R2) ≤ Copt f L2(S1), (1.1) where the Fourier transform of the measure fσ is given by

f(ω)e−ix·ω dσω, (x ∈ R2), and Copt denotes the optimal constant,

fσ(x) =

S1

Φ(f); Φ(f) := fσ L6(R2) f −L21(S1).

Copt := sup

0 =f∈L2(S1)

The existence of global extremizers of Φ was recently established by Shao [30]. Our ﬁrst result establishes that the constant function 1 is a local extremizer of Φ.

- Theorem 1. There exists δ > 0 such that, whenever f − 1 L2(S1) < δ, we have Φ(f) ≤ Φ(1).


It is known that the constant function 1 is a critical point of Φ. Indeed, by rotational symmetry, f = 1 satisﬁes the generalized Euler-Lagrange equation f = λ(| fσ|4 fσ)∨ |S1 that characterizes critical points, see

- [9, Proposition 2.1] for details. We give the proof of Theorem 1 in Section 4. Our second and main result concerns a trilinear form related to Fourier restriction. To motivate this


trilinear form, we start by using Plancherel’s identity and writing fσ 6L6(R2) = (2π)2 fσ ∗ fσ ∗ fσ 2L2(R2)

= (2π)2(fσ) ∗ (fσ) ∗ (fσ) ∗ (f⋆σ) ∗ (f⋆σ) ∗ (f⋆σ)(0)

= (2π)2

f(ω1)f(ω2)f(ω3)f⋆(ω4)f⋆(ω5)f⋆(ω6)dΣ ω, (1.2)

(S1)6

![image 1](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile1.png>)

Date: September 23, 2015. 2010 Mathematics Subject Classiﬁcation. 42B10. Key words and phrases. Circle, Fourier restriction, sharp inequalities, extremizers, convolution of surface measures, Bessel

functions.

![image 2](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile2.png>)

where f⋆(ω) = f(−ω) and dΣ ω = δ(ω1 + ω2 + ω3 + ω4 + ω5 + ω6)dσω

.

dσω

dσω

dσω

dσω

dσω

6

5

4

3

2

1

Here δ stands for the two dimensional Dirac measure. Note that the measure dΣ ω is supported on the four dimensional manifold Γ ⊂ (S1)6 determined by

ω1 + ω2 + ω3 + ω4 + ω5 + ω6 = 0. (1.3) We deﬁne the trilinear form:

T(h1,h2,h3) :=

h1(ω1)h2(ω2)h3(ω3) |ω4 + ω5 + ω6|2 − 1 dΣ ω. (1.4)

(S1)6

The main result of this paper is the following monotonicity estimate, obtained in Section 5 via a spectral decomposition and a careful analysis of integrals involving Bessel functions. By antipodally symmetric function we mean a function h on S1 with h(ω) = h(−ω).

- Theorem 2. Let h ∈ L1(S1) be a nonnegative and antipodally symmetric function. Let c = 21π S


h(ω)dσω be the mean value of h. Then

![image 3](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile3.png>)

1

T(h,h,h) ≤ T(c,c,c), with equality if and only if h is constant.

This bound for the trilinear form T is the penultimate step in a six-step program that we propose to obtain the sharp form of the Tomas-Stein adjoint restriction inequality (1.1) and characterize its global extremizers. A similar program was used in [15] to obtain the sharp endpoint L2 − L4 Tomas-Stein adjoint restriction inequality on the sphere S2, and subsequently in [7] to obtain the sharp non-endpoint L2 − L4 estimate on the sphere Sd for 3 ≤ d ≤ 6. In this paper we complete all the steps of this program in the case of S1, except for Step 4 which remains unresolved and that we pose as a conjecture.

We brieﬂy describe each of these steps, which result in a proof of the conditional Theorem 5 below.

- 1.0.1. Step 1. Reduction to nonnegative functions. Since |fσ ∗ fσ ∗ fσ| ≤ |f|σ ∗ |f|σ ∗ |f|σ holds pointwise, it follows that

fσ ∗ fσ ∗ fσ L

2(R2) ≤ |f|σ ∗ |f|σ ∗ |f|σ L

2(R2). (1.5) Here equality holds if and only if there is a measurable complex-valued function h on the closed ball B(3) ⊂ R2 of radius 3 centered at the origin such that

![image 4](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile4.png>)

f(ω1)f(ω2)f(ω3) = h(ω1 + ω2 + ω3) f(ω1)f(ω2)f(ω3)

for σ3−a.e. (ω1,ω2,ω3) ∈ (S1)3. This can be seen as in the proof of [7, Lemma 8]. Compare also with [10, 15].

- 1.0.2. Step 2. Reduction to antipodally symmetric functions. Deﬁne the nonnegative, antipodally symmetric rearrangement f♯ of a function f ∈ L2(S1) by


![image 5](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile5.png>)

f♯ := |f|2 + |f⋆|2 2

.

![image 6](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile6.png>)

If f is in L2(S1), then so is its antipodal rearrangement, with f♯ L2(S1) = f L2(S1). A simple application of the arithmetic/geometric mean inequality as in [15, Corollary 3.3] shows that

f(ω1)f(ω2)f(ω3)f⋆(ω4)f⋆(ω5)f⋆(ω6)dΣ ω ≤

(S1)6

f♯(ω1)f♯(ω2)f♯(ω3)f♯(ω4)f♯(ω5)f♯(ω6)dΣ ω. (1.6)

(S1)6

Here equality holds if and only if f = f⋆ = f♯ (σ−a.e. in S1). This follows as in the proof of [7, Lemma 9]. From inequalities (1.5) and (1.6) it follows that

Copt = sup

0 =f∈L2(S1), f≥0, f=f⋆

Φ(f).

We may hence assume that our candidate f ∈ L2(S1) to being an extremizer of (1.1) is also a nonnegative, antipodally symmetric function.

- 1.0.3. Step 3. Geometric considerations. Suppose that we naively try to follow the method used in [14] and apply the Cauchy-Schwarz inequality directly to the last integral in (1.2) (or in (1.6)). We would obtain

fσ 6L6(R2) ≤ (2π)2

(S1)6

|f(ω1)|2|f(ω2)|2|f(ω3)|2 dΣ ω

= (2π)2

(S1)3

|f(ω1)|2|f(ω2)|2|f(ω3)|2σ ∗ σ ∗ σ(ω1 + ω2 + ω3)dσω

1

dσω

2

dσω

3

.

If the 3-fold convolution product σ ∗ σ ∗ σ were a constant function inside its support, then the last integral would reduce to a constant multiple of f 6L2(S1), and we would immediately obtain the estimate (1.1). Unfortunately, the quantity σ∗σ∗σ(x) diverges logarithmically as x approaches the unit circle; the singularity of σ ∗ σ ∗ σ will be described in Section 2. This singularity can be neutralized if in the integral (1.6) we insert an appropriate weight which vanishes when the sum of three unit vectors is again a unit vector. This is made possible thanks to the geometrical identity illustrated in the next lemma.

Lemma 3. If (ω1,ω2,ω3,ω4,ω5,ω6) ∈ Γ, then

(

6 3

)

|ωi + ωj + ωk|2 − 1 = 16, (1.7)

where the sum above runs over all the 63 = 20 diﬀerent choices of unordered distinct indices i,j,k ∈ {1,2,3,4,5,6}.

For the proof, one squares (1.3) and expands (1.7) to arrive at the desired conclusion. Using this identity, we can write

fσ 6L6(R2) = (2π)2

1 16

![image 7](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile7.png>)

(

6 3

) (S

1)6

f(ω1)f(ω2)f(ω3)f(ω4)f(ω5)f(ω6) |ωi + ωj + ωk|2 − 1 dΣ ω

= (2π)2

5 4 (S1)6

![image 8](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile8.png>)

f(ω1)f(ω2)f(ω3)f(ω4)f(ω5)f(ω6) |ω4 + ω5 + ω6|2 − 1 dΣ ω , since by symmetry all 20 integrals in the ﬁrst line of the last display have the same numerical value.

- 1.0.4. Step 4. Reduction to a trilinear problem. At this point in the program [15], a similar weight as


|ω4 + ω5 + ω6|2 − 1 has been introduced, albeit nonnegative. The program there continues with an application of the Cauchy-Schwarz inequality. Since our weight is partially negative, we cannot simply apply the Cauchy-Schwarz inequality. Nevertheless, we pose this inequality as a conjecture:

Conjecture 4. Let f ∈ L2(S1) be nonnegative and antipodally symmetric. Then:

f(ω1)f(ω2)f(ω3)f(ω4)f(ω5)f(ω6) |ω4 + ω5 + ω6|2 − 1 dΣ ω

(S1)6

≤

f(ω1)2f(ω2)2f(ω3)2 |ω4 + ω5 + ω6|2 − 1 dΣ ω. (1.8)

(S1)6

Numerical simulations suggest that this inequality holds. One reason to believe so is that the negative portion of the weight is small, and via antipodal symmetry the values of the functions on this negative portion have a strong correlation with the values of the functions on the positive part. However, the antipodal symmetry does not preserve the support of dΣ ω, which makes it diﬃcult to exploit this correlation.

If on the right-hand side of (1.8) we replace ω4 + ω5 + ω6 by ω1 + ω2 + ω3 and integrate out ω4, ω5 and ω6, we obtain an additional weight given by the 3-fold convolution product σ ∗ σ ∗ σ(|ω1 + ω2 + ω3|). As we have already observed, this convolution has a logarithmic singularity at |ω1 +ω2 +ω3| = 1, which disappears when multiplied by the weight |ω1 + ω2 + ω3|2 − 1, in analogy to the program of [15].

- 1.0.5. Step 5. Spectral analysis of a cubic form. The right-hand side of (1.8) invokes the trilinear form T of our main Theorem 2. Thus, using (1.8) and Theorem 2 yields for nonnegative, antipodally symmetric functions f:

fσ 6L6(R2) ≤ (2π)2

5 4

![image 9](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile9.png>)

T(f2,f2,f2) ≤ (2π)2

5 4

![image 10](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile10.png>)

f 6L2(S1) 1 6L2(S1)

![image 11](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile11.png>)

T(1,1,1) =

σ 6L6(R2) 1 6L2(S1)

![image 12](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile12.png>)

f 6L2(S1). (1.9) This proves the ﬁrst part of Theorem 5 below.

- 1.0.6. Step 6. Characterizing the complex-valued extremizers. If f ∈ L2(S1) is a complex-valued extremizer


of (1.9), by Theorem 2 we must have |f|♯ = γ 1, where γ > 0 is a constant. By the discussion in Step 2 above we must have |f| = γ 1. By the discussion in Step 1 above there is a measurable function h : B(3) → C such that

![image 13](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile13.png>)

f(ω1)f(ω2)f(ω3) = γ3 h(ω1 + ω2 + ω3)

for σ3−a.e. (ω1,ω2,ω3) ∈ (S1)3. We now invoke [7, Theorem 4] (which is originally inspired in the work of Charalambides [8]) to conclude that there exist c ∈ C \ {0} and ν ∈ C2 such that

f(ω) = c eν·ω

for σ−a.e. ω ∈ S1. Since |f| is constant, we must have ℜ(ν) = 0 and |c| = γ. This completes the proof of the following theorem.

- Theorem 5. Assume the validity of Conjecture 4. Then Copt = (2π)−1/2 σ L6(R2).


Moreover, all complex-valued extremizers of (1.1) are given by

f(ω) = c eiξ·ω, where c ∈ C \ {0} and ξ ∈ R2.

The endpoint problem for the sphere S2 discussed in [15] is simpler than the above in Steps 4 and 5. In Step 4, one faces the convolution of the surface measure of the sphere with itself, which has a singularity

at the origin, and one can choose a nonnegative weight vanishing at the origin, so that the corresponding Step 4 follows from a plain application of the Cauchy-Schwarz inequality. In Step 5, the analogue spectral analysis is over a bilinear rather than trilinear form. One uses the Funk-Hecke formula and properties of the Gegenbauer polynomials to show that a certain bilinear term has a sign. This is considerably simpler than the proof of Theorem 2.

As evidence towards Conjecture 4 we prove the following local result in Section 6. Deﬁne

f(ω1)f(ω2)f(ω3) − f(ω4)f(ω5)f(ω6) 2 |ω4 + ω5 + ω6|2 − 1 dΣ ω. (1.10)

Ψ(f) :=

(S1)6

Observe that Ψ(1) is identically zero and that Conjecture 4 is equivalent to the fact that Ψ(f) ≥ 0 for f ∈ L2(S1) nonnegative and antipodally symmetric.

- Theorem 6. There exists δ > 0 such that, whenever f is real-valued and f − 1 L2(S1) < δ, we have Ψ(f) ≥ 0.


Note that this result holds for all real-valued functions, without assumption of nonnegativity nor antipodal symmetry.

The study of sharp Fourier restriction inequalities for the sphere Sd is quite recent, with the aforementioned works [7, 10, 15, 30] and the additional [11]. The literature on sharp Fourier restriction inequalities related to the paraboloid and cone is extensive and we highlight the works [1, 4, 6, 14, 19, 21, 26]. Other interesting works on sharp Strichartz-type estimates and on the existence of extremizers for other Fourier restriction estimates include [2, 3, 5, 12, 13, 16, 18, 20, 23, 25, 27, 28, 29].

2. Convolutions of unit circle measures We start by recalling a particular case of [7, Lemma 5].

Lemma 7. The convolution σ ∗ σ is supported on the disk of radius 2 centered at the origin, and for |x| ≤ 2 we have:

4 |x| 4 − |x|2

.

σ ∗ σ(x) =

![image 14](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile14.png>)

![image 15](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile15.png>)

- Lemma 7 can be combined together with an additional convolution to yield

σ ∗ (σ ∗ σ)(x) =

Sx

4dσω |x − ω| 4 − |x − ω|2

![image 16](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile16.png>)

![image 17](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile17.png>)

,

where Sx = {ω ∈ S1 : |x − ω| ≤ 2}. The last integrand can be written as a function which depends only on the radius r := |x| and on the cosine u := |xx| · ω. We have that dσω = (1 − u2)−1/2du and, by applying this change of variables in the integration, we obtain the following formula.

![image 18](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile18.png>)

- Lemma 8. The convolution σ ∗ σ ∗ σ is supported on the disk of radius 3 centered at the origin, and for |x| ≤ 3 we have:


1

du √1 − u2 (1−r)

4 r

, (2.1)

σ ∗ σ ∗ σ(x) =

![image 19](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile19.png>)

![image 20](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile20.png>)

![image 21](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile21.png>)

![image 22](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile22.png>)

2

2r + 1 − u (3+r2)(1r −r) + 1 + u

![image 23](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile23.png>)

A(r)

![image 24](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile24.png>)

![image 25](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile25.png>)

where r = |x| and A(r) := −1 + max{0,(3 + r)(r − 1)/(2r)}.

The integral (2.1) diverges for r = 1. Suppose ε := |r − 1| > 0. The contribution coming from integration over the intervals (A(r),A(r) + ε) and (1 − ε2,1) remains bounded as ε → 0, while the contribution coming from the integration over [A(r) + ε,1 − ε2] grows like |log ε|. We obtain, as |x| → 1,

for some absolute constants c,C > 0.

σ ∗ σ ∗ σ(x) log |x| − 1

c ≤

≤ C,

![image 26](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile26.png>)

3. Bessel functions

The main technical part of this paper uses the Bessel functions Jn and estimates for integrals of sixfold products of Bessel functions that are proved in the companion paper [24]. Here we introduce the basic deﬁnitions and present the estimates from [24] in a convenient form for our purposes. We identify R2 ≃ C, and write a vector x ∈ R2 as a point in the complex plane x = |x|eiarg(x). For every n ∈ Z, deﬁne

en(x) := xn = |x|neinarg(x). Bessel functions can be deﬁned via the Fourier transform of the circular harmonics.

Deﬁnition 9. Let n ∈ Z and x ∈ R2. Then the Bessel function of order n, denoted Jn, is deﬁned by

enσ(x) = 2π(−i)nJn(|x|)|x|−nen(x). (3.1) Bessel functions come into play via the following calculation. We have

(2π)2

f1(ω1)f2(ω2)f3(ω3)f4(ω4)f5(ω5)f6(ω6)dΣ ω =

(S1)6

f1σ f2σ f3σ f4σ f5σ f6σ dx. (3.2)

R2

(ω) = ωn

Assume that the six functions fj, 1 ≤ j ≤ 6, are spherical harmonics on S1, that is fj(ω) = en

. Restricted to circles about the origin, the integrand on the right-hand side of (3.2) is a spherical harmonic of index n := n1 + n2 + n3 + n4 + n5 + n6. So unless n = 0, the last display vanishes. If n = 0, then the integrand is constant on circles about the origin, and integrating in polar coordinates yields for the last display

j

j

∞

= (2π)7

(r)r dr =: (2π)7In

1,n2,n3,n4,n5,n6. For more general functions on S1 we write

(r)Jn

(r)Jn

(r)Jn

(r)Jn

(r)Jn

Jn

6

5

4

3

2

1

0

fj(ω) =

fj(n)en(ω) (3.3)

n∈Z

and obtain for (3.2): (2π)7

1,n2,n3,n4,n5,n6. (3.4)

f1(n1) f2(n2) f3(n3) f4(n4) f5(n5) f6(n6)In

n1+n2+n3+n4+n5+n6=0

1,n2,n3,n4,n5,n6. Note that the parity Jn = J−n for even n and Jn = −J−n for odd n allows us to restrict attention to these integrals for nonnegative indices. In particular, the following sequences (deﬁned for n ∈ Z) will come into play:

Thus we will be interested in a good understanding of the quantities In

∞

Jn2(r)J04(r)r dr, (3.5)

αn :=

0

∞

Jn2(r)J12(r)J02(r)r dr, (3.6) as well as the linear combination

αn :=

0

∞

Jn2(r)J02(r) 3J12(r) − J02(r) r dr. (3.7)

βn :=

0

Table 1 shows some of these values, accurate to 5 × 10−7. Computing the values of αn and αn with Mathematica required some care which is described in the companion paper [24, Section 8]. The values of βn were obtained by subtracting the values on the ﬁrst column from three times the values on the second column.

![image 27](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile27.png>)

![image 28](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile28.png>)

![image 29](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile29.png>)

![image 30](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile30.png>)

n αn αn βn

![image 31](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile31.png>)

- 0 0.3368280 0.0673656 -0.1347312

![image 32](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile32.png>)

![image 33](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile33.png>)

![image 34](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile34.png>)

- 1 0.0673656 0.0423752 0.0597600

![image 35](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile35.png>)

![image 36](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile36.png>)

![image 37](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile37.png>)

- 2 0.0369428 0.0138533 0.0046171

![image 38](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile38.png>)

![image 39](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile39.png>)

![image 40](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile40.png>)

- 3 0.0249883 0.0088143 0.0014546

![image 41](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile41.png>)

![image 42](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile42.png>)

![image 43](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile43.png>)

- 4 0.0188523 0.0064847 0.0006018

![image 44](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile44.png>)

![image 45](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile45.png>)

![image 46](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile46.png>)

- 5 0.0151231 0.0051433 0.0003068

![image 47](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile47.png>)

![image 48](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile48.png>)

![image 49](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile49.png>)

- 6 0.0126216 0.0042662 0.0001770

![image 50](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile50.png>)

![image 51](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile51.png>)

![image 52](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile52.png>)

- 7 0.0108283 0.0036466 0.0001115

![image 53](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile53.png>)

![image 54](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile54.png>)

![image 55](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile55.png>)

- 8 0.0094804 0.0031850 0.0000746

![image 56](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile56.png>)

![image 57](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile57.png>)

![image 58](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile58.png>)

- 9 0.0084305 0.0028276 0.0000523

![image 59](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile59.png>)

![image 60](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile60.png>)

![image 61](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile61.png>)

- 10 0.0075896 0.0025426 0.0000382 Table 1


![image 62](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile62.png>)

![image 63](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile63.png>)

![image 64](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile64.png>)

![image 65](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile65.png>)

The companion paper [24] gives precise estimates for these sequences summarized in the following theorem. Theorem 10. (cf. [24, Theorem 1]) For n ≥ 7 we have

1 500n4

3 32π2(n − 1)n(n + 1) ≤

- 3

![image 66](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile66.png>)

- 4π2n


;

+

αn −

![image 67](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile67.png>)

![image 68](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile68.png>)

1 4π2n −

1 500n4

3 32π2(n − 1)n(n + 1) ≤

αn −

.

![image 69](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile69.png>)

![image 70](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile70.png>)

![image 71](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile71.png>)

We deduce the following estimate for the sequence βn. Deﬁne c0 =

3 8π2

. (3.8) Corollary 11. For n ≥ 2 even and ε1 = 0.03, we have

![image 72](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile72.png>)

c0 n3

c0 n3

< ε1

βn −

.

![image 73](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile73.png>)

![image 74](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile74.png>)

Proof. For n ≤ 10 this follows by direct checking with the values given in Table 1, the tightest case being n = 2. For n ≥ 12 one takes a linear combination of the estimates of the previous theorem to obtain

1 125n4

c0 (n − 1)n(n + 1) ≤

. The triangle inequality then yields

βn −

![image 75](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile75.png>)

![image 76](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile76.png>)

c0 n3 ≤

c0 n3(n2 − 1)

c0 n3

1 125n4 ≤

1 1500c0

c0 n3

1 143

βn −

. This proves the corollary.

< 0.025

+

+

![image 77](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile77.png>)

![image 78](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile78.png>)

![image 79](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile79.png>)

![image 80](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile80.png>)

![image 81](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile81.png>)

![image 82](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile82.png>)

![image 83](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile83.png>)

Note that the linear combination in the corollary is such that the terms of order n−1 in the asymptotics of αn and αn cancel.

We will also need estimates for γn,m :=

∞

Jn(r)Jm(r)Jn+m(r)J03(r)r dr, (3.9)

0

∞

Jn(r)Jm(r)Jn+m(r)J12(r)J0(r)r dr, (3.10) and

γn,m :=

0

∞

Jn(r)Jm(r)Jn+m(r) 3J12(r) − J02(r) J0(r)r dr. (3.11) The values on the ﬁrst two columns of Table 2 were again computed with Mathematica and have precision 5 × 10−8.

δn,m :=

0

![image 84](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile84.png>)

![image 85](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile85.png>)

![image 86](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile86.png>)

![image 87](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile87.png>)

![image 88](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile88.png>)

n m γn,m γn,m δn,m

![image 89](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile89.png>)

![image 90](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile90.png>)

![image 91](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile91.png>)

![image 92](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile92.png>)

![image 93](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile93.png>)

2 2 0.00090754 0.00061039 0.00092363 4 2 0.00019186 0.00012012 0.00016850 6 2 0.00006958 0.00004264 0.00005834 4 4 0.00002195 0.00001272 0.00001621 6 4 0.00000498 0.00000281 0.00000345 8 4 0.00000160 0.00000089 0.00000107

![image 94](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile94.png>)

![image 95](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile95.png>)

![image 96](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile96.png>)

![image 97](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile97.png>)

![image 98](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile98.png>)

![image 99](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile99.png>)

![image 100](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile100.png>)

![image 101](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile101.png>)

![image 102](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile102.png>)

![image 103](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile103.png>)

![image 104](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile104.png>)

![image 105](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile105.png>)

![image 106](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile106.png>)

![image 107](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile107.png>)

![image 108](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile108.png>)

![image 109](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile109.png>)

![image 110](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile110.png>)

![image 111](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile111.png>)

![image 112](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile112.png>)

![image 113](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile113.png>)

![image 114](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile114.png>)

![image 115](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile115.png>)

![image 116](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile116.png>)

![image 117](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile117.png>)

10 4 0.00000064 0.00000035 0.00000041 Table 2

![image 118](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile118.png>)

The companion paper [24] proves the following result.

Theorem 12. (cf. [24, Theorem 1]) For n ≥ 6 even we have

- (i)

γn,2 −

15 64π2n(n + 1)(n + 2) ≤

![image 119](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile119.png>)

1 500n4

![image 120](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile120.png>)

;

γn,2 −

9 64π2n(n + 1)(n + 2) ≤

![image 121](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile121.png>)

1 500n4

![image 122](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile122.png>)

.

- (ii)

γn,4 −

1557 1024π2n(n + 1)(n + 2)(n + 3)(n + 4) ≤

![image 123](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile123.png>)

3 2000n4

![image 124](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile124.png>)

;

γn,4 −

855 1024π2n(n + 1)(n + 2)(n + 3)(n + 4) ≤

![image 125](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile125.png>)

3 2000n4

![image 126](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile126.png>)

.

For n and m even with n ≥ m ≥ 6 we have

- (iii)


3 2000n4

|γn,m| , | γn,m| ≤

.

![image 127](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile127.png>)

Again we obtain a simple corollary for δn,m, where we recall the constant c0 from (3.8).

Corollary 13. (i) For n ≥ 2 even and ε2 = 0.11 we have |δn,2| ≤ (1 + ε2)

c0 2n3/2(n + 2)3/2

.

![image 128](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile128.png>)

- (ii) For n ≥ 4 even and γ3 = 1.3 we have

δn,4 −

21c0 8n(n + 1)(n + 2)(n + 3)(n + 4) ≤ γ3

![image 129](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile129.png>)

c0 8n4

![image 130](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile130.png>)

.

- (iii) For n and m even with n ≥ m ≥ 6 and again γ3 = 1.3 we have


c0 8n4

|δn,m| ≤ γ3

.

![image 131](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile131.png>)

Proof. We begin with inequality (i). For n = 2,4,6 this is veriﬁed directly with Table 2. Again the tightest case is n = 2. For n ≥ 8, from Theorem 12 we have

3/2 1 1000 n3/2(n + 2)3/2

c0 2n3/2(n + 2)3/2

1 125n4 ≤

10 8

c0 2n(n + 1)(n + 2)

+

+

,

|δn,2| ≤

![image 132](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile132.png>)

![image 133](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile133.png>)

![image 134](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile134.png>)

![image 135](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile135.png>)

![image 136](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile136.png>)

which is less than the desired quantity. Inequalities (ii) and (iii) follow from Theorem 12 via the estimate 3 500 ≤ 1.3

3 64π2

. This completes the proof of the corollary.

![image 137](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile137.png>)

![image 138](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile138.png>)

4. Proof of Theorem 1: Constants are local extremizers of the extension inequality In this section we follow the outline of [10, Section 16] to prove Theorem 1. Note that

- (i) Φ(f) = Φ(λf) for all λ > 0;
- (ii) Φ(f) ≤ Φ(|f|) ≤ Φ(|f|♯);
- (iii)  |f|♯ − 1 L2(S1) ≤  |f| − 1 L2(S1) ≤ f − 1 L2(S1).


We may therefore restrict attention to functions of the form f = 1 + εg,

where 0 ≤ ε ≤ δ, g ⊥ 1, g L2(S1) = 1, with g real-valued and antipodally symmetric. A straightforward calculation gives the Taylor expansion

Φ(f)6 = Φ(1)6 +(2πε)2 1 −2 6 15gσ∗gσ∗σ ∗σ ∗σ ∗σ(0)−3σ∗σ ∗σ ∗σ ∗σ ∗σ(0) 1 −2 2 g 22 +O(ε3), (4.1) where O(ε3) denotes a quantity whose absolute value is majorized by Cε3, uniformly for g satisfying

g L2(S1) ≤ 1. Note that we do not have a term in ε since gσ ∗ σ ∗ σ ∗ σ ∗ σ ∗ σ(0) = 0 due to the discussion after (3.2) and the fact that g ⊥ 1, i.e. g(0) = 0. From (4.1) it suﬃces to show that 5 sup

gσ ∗ gσ ∗ σ ∗ σ ∗ σ ∗ σ(0) < σ ∗ σ ∗ σ ∗ σ ∗ σ ∗ σ(0) 1 −2 2 g 22.

g 2=1

Using (3.4) together with the fact that g is real with mean zero and antipodally symmetric, and therefore can only have even nonzero Fourier coeﬃcients, this reduces to1

| g(n)|2αn <

5

n∈(2Z)×

| g(n)|2α0, (4.2)

n∈(2Z)×

![image 139](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile139.png>)

1Throughout this paper, we let (2Z)× := 2Z \ {0} and Z× := Z \ {0}. Similarly for (2N)×, where N := {0, 1, 2, . . .}.

where we have used the fact that g 2L2(S1) = 2π n∈(2Z)× | g(n)|2. Estimate (4.2) will follow from 5αn < α0 for all n ∈ (2Z)×. This in turn follows from Theorem 10 and Table 1.2 In particular, for n ≥ 10 we conclude from Theorem 10 that

- 3

![image 140](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile140.png>)

- 4π2n


1 50

3 32π2(n − 1)n(n + 1)

1 500n4 ≤

αn ≤

. This completes the proof of Theorem 1.

+

+

![image 141](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile141.png>)

![image 142](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile142.png>)

![image 143](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile143.png>)

Remark: By using Theorem 10, we appeal to the companion paper [24]. However, this particular consequence (4.2) is a very simple case of the analysis in [24], and for self containment we sketch a proof of the bound 5αn < α0 for all n ∈ (2Z)×. One ﬁrst reduces the estimate to an estimate for integrals over bounded domains, that is to

100

100

Jn2(r)J04(r)r dr <

J06(r)r dr, (4.3) by establishing bounds for the tails, that is

7

0

0

∞

∞

100

Jn2(r)J04(r)r dr, 200

J06(r)r dr <

J06(r)r dr . To see these tail bounds, one estimates the left-hand sides using the well known bounds

25

100

100

0

J0(r) −

2 πr

![image 144](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile144.png>)

1/2

π 4 ≤ r−3/2

cos r −

![image 145](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile145.png>)

and

|Jn(r)| ≤ r−1/3 , for all n ≥ 0. A sharper form of the latter inequality can be found in [22], while the former is reviewed in [24]. The right-hand sides are then evaluated numerically. Here, we assume to have a suﬃciently accurate evaluation of Bessel functions at hand such as, for example, provided by the Mathematica package. Moreover, Riemann sums with step size 1000−1 will give suﬃcient accuracy. To see the estimate (4.3) for the integrals over bounded domains, in case n ≤ 200 one simply evaluates likewise numerically. To see the estimate for n > 200, one estimates the left-hand side using |J0| ≤ 1 and the well-known estimate

rn 2nn!

Jn(r) ≤

![image 146](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile146.png>)

for all n ≥ 0 and r > 0, reviewed in [24]. This completes the outline of the proof that 5αn < α0 for n ∈ (2Z)×.

- As a ﬁnal remark, note that a more reﬁned analysis would allow to reduce the numerical component of the proof.


5. Proof of Theorem 2: The sharp trilinear inequality

We shall prove Theorem 2 for h being a nonnegative and antipodally symmetric trigonometric polynomial. The result for a general h ∈ L1(S1) nonnegative and antipodally symmetric follows by a standard approximation argument, for example by convolving with the F´ejer kernel, since the map h  → T(h,h,h) is continuous on L1(S1). To pass the case of equality to the limit in the approximation argument, we observe from the proof below that each nonzero even Fourier coeﬃcient of h has a strictly negative contribution.

Let h be a nonnegative and antipodally symmetric trigonometric polynomial. Write h = c + g,

![image 147](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile147.png>)

2However, it can be shown using integration by parts that 5α1 = α0.

![image 148](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile148.png>)

with g ⊥ 1 and c = 21π S

h(ω)dσω. By the assumptions on h, we have that h(−n) = h(n) for every n ∈ Z, and that h(n) = 0 only if n ∈ 2Z. The analogous statements hold for g, and moreover g(0) = 0. By linearity and symmetry, one can immediately check that

![image 149](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile149.png>)

1

T(h,h,h) = T(c,c,c) + 3T(c,c,g) + 3T(c,g,g) + T(g,g,g). The strategy to prove Theorem 2 will be to analyze each of these summands separately. It turns out that the linear term is zero, the bilinear term is nonpositive, and the trilinear term can be controlled in absolute value by the bilinear term. Once we establish these facts, which are the subject of the remainder of this section, the result follows.

- 5.1. Linear term. Let Rθω denote the rotation of ω by the angle θ counterclockwise around the origin. Denote Rθg(ω) = g(Rθω). Then it is immediate from the deﬁnition that T(Rθf1,Rθf2,Rθf3) = T(f1,f2,f3) for any functions f1,f2,f3 in L2(S1). For the linear term of our expansion this means that

T(c,c,f) = T(c,c,Rθf).

Hence f  → T(c,c,f) is a rotation invariant linear functional on L2(S1), and therefore it is a multiple of the averaging operator. Since g has mean zero, we obtain T(c,c,g) = 0.

- 5.2. Bilinear term. We expand |ω4 + ω5 + ω6|2 − 1 = 2 (1 + ω4 · ω5 + ω5 · ω6 + ω6 · ω4). (5.1)


Thus the integral (1.4) deﬁning T(c,g,g) splits into a sum of four terms, the last three of which are identical by symmetry considerations. We ﬁrst consider

g(ω2)g(ω3)dΣ ω. It follows by calculations as the ones leading to (3.4) that

I :=

(S1)6

I = gσ ∗ gσ ∗ σ ∗ σ ∗ σ ∗ σ(0)

= (2π)−2

g(n) g(m)

n∈(2Z)× m∈(2Z)×

enσ emσ σ σ σ σ dx

R2

= (2π)−2

| g(n)|2

n∈(2Z)×

R2

| g(n)|2 αn,

= (2π)5

n∈(2Z)×

enσ e−nσ σ σ σ σ dx

(5.2)

where the sequence {αn} was deﬁned in (3.5). We now focus on the second integral, II :=

g(ω2)g(ω3)(ω4 · ω5)dΣ ω. Observe that, using the algebra of complex numbers, we can write

(S1)6

- 1

![image 150](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile150.png>)

- 2


ω4 · ω5 = cos(arg(ω4) − arg(ω5)) = ℜ(ω4ω5) =

![image 151](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile151.png>)

- 1

![image 152](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile152.png>)

- 2


ω4ω5 + ω4ω5 =

![image 153](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile153.png>)

![image 154](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile154.png>)

e1(ω4)e−1(ω5) + e−1(ω4)e1(ω5) .

By symmetry we obtain

g(ω2)g(ω3)e1(ω4)e−1(ω5)dΣ ω. By a similar calculation as for the ﬁrst integral we obtain

II =

(S1)6

II = (2π)−2

gσ gσ e1σ e−1σ σ σ dx

R2

= (2π)−2

g(n) g(m)

n∈(2Z)× m∈(2Z)×

= −(2π)5

| g(n)|2 αn,

n∈(2Z)×

enσ emσ e1σ e−1σ σ σ dx

R2

(5.3)

where the sequence { αn} was deﬁned in (3.6). Finally we obtain T(c,g,g) = 2c(I + 3II) = −2c(2π)5

n∈(2Z)×

| g(n)|2 βn,

with {βn} as deﬁned in (3.7). Since the numbers βn are positive by Corollary 11, this establishes that the bilinear term T(c,g,g) is nonpositive.

- 5.3. Trilinear term. Identity (5.1) allows us to again express T(g,g,g) as a sum of four integrals, the last three of which are identical by symmetry considerations. We start by computing the ﬁrst one similarly to the previous calculations:

I =

(S1)6

g(ω1)g(ω2)g(ω3)dΣ ω = (2π)−2

R2

gσ gσ gσ σ σ σ dx

= (2π)−2

n∈(2Z)× m∈(2Z)× k∈(2Z)×

g(n) g(m) g(k)

R2

enσ emσ ekσ σ σ σ dx

= (2π)5

n∈(2Z)× m∈(2Z)×

g(n) g(m) g(n + m)γn,m,

![image 155](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile155.png>)

with {γn,m} as deﬁned in (3.9). For the second integral we obtain similarly II =

(S1)6

g(ω1)g(ω2)g(ω3)(ω4 · ω5)dΣ ω

= −(2π)5

n∈(2Z)× m∈(2Z)×

g(n) g(m) g(n + m) γn,m,

![image 156](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile156.png>)

with { γn,m} as deﬁned in (3.10). Summarizing, we obtain T(g,g,g) = 2(I + 3II) = −2(2π)5

n∈(2Z)× m∈(2Z)×

g(n) g(m) g(n + m)δn,m,

![image 157](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile157.png>)

with {δn,m} as deﬁned in (3.11).

- 5.4. Bilinear controls trilinear. We want to show that the trilinear term we just computed is controlled in absolute value by the bilinear term −3T(c,g,g). Since h ≥ 0, the constant c is given by (recall that we are using the normalization (3.3) for the Fourier series)


h 1 2π

= h(0) = h ∞.

c =

![image 158](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile158.png>)

Observe that g(n) = h(n) for n = 0. Our task can thus be reformulated as the following statement:

![image 159](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile159.png>)

| h(n)|2βn.

h(n) h(m) h(n + m)δn,m ≤ 3 h ∞

n,m,n+m∈(2Z)×

n∈(2Z)×

Letting k = −m−n, we further simplify the problem by using the symmetries of the planar lattice (2Z)× 3∩ {n + m + k = 0}. We have two possibilities: (i) two numbers positive and one negative or (ii) two numbers negative and one positive. Since h(n) = h(−n) for every n ∈ Z, the two cases are actually the same, and so we work with case (i) only. In this case, we consider the instances where k is negative. By the triangle inequality, it suﬃces to show that

![image 160](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile160.png>)

![image 161](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile161.png>)

h(n) h(m) h(n + m)δn,m ≤ h ∞

n,m∈(2N)×

| h(n)|2βn. (5.4)

n∈(2N)×

Recall that c0 = 3/8π2 and deﬁne ηn,4 =

1 n(n + 1)(n + 2)(n + 3)(n + 4) and

21c0 8

![image 162](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile162.png>)

![image 163](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile163.png>)

δn,4 = δn,4 − ηn,4. For n ∈ {6,8,...} and m ∈ {6,...,n}, deﬁne

δn,m = δn,m.

We break the left-hand side of (5.4) into 6 sums. The ﬁrst two are the terms for which min(n,m) = 2, sorted into those for which n ≤ m and those for which n > m. The next two are the terms for which min(n,m) = 4, in which we have isolated the main contribution ηn,4. The last two sums are the terms with min(n,m) ≥ 4 with the residual contribution δn,m.

(LHS) ≤

![image 164](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile164.png>)

h(n) h(2) h(n + 2)δn,2 +

n∈2N: 2≤n

![image 165](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile165.png>)

h(n) h(2) h(n + 2)δn,2

n∈2N: 2<n

+

![image 166](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile166.png>)

h(n) h(4) h(n + 4)ηn,4 +

n∈2N: 4≤n

![image 167](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile167.png>)

h(n) h(4) h(n + 4)ηn,4

n∈2N: 4<n

+

![image 168](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile168.png>)

h(n) h(m) h(n + m) δn,m +

n,m∈2N: 4≤m≤n

![image 169](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile169.png>)

h(n) h(m) h(n + m) δn,m

n,m∈2N: 4≤m<n

= S1 + S2 + S3 + S4 + S5 + S6.

- 5.4.1. Analysis of S1. We treat these terms in a special way so as to not have to estimate h(2) by h ∞ as in S5 and S6. Using Corollary 13 and the Cauchy-Schwarz inequality, we proceed as follows:


c0 2

S1 ≤ | h(2)|(1 + ε2)

![image 170](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile170.png>)

| h(n)| n3/2

| h(n + 2)| (n + 2)3/2

![image 171](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile171.png>)

![image 172](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile172.png>)

n∈(2N)×

1/2 

  

 

 

1/2

| h(n)|2 n3

| h(n)|2 n3

c0 2

 

≤ | h(2)|(1 + ε2)

.

![image 173](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile173.png>)

![image 174](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile174.png>)

![image 175](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile175.png>)

n∈2N: 4≤n

n∈(2N)×

| h(n)|2

n3 = S. We seek to maximize

Let | h(2)| = x and n∈(2N)×

![image 176](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile176.png>)

1/2

x2 8

x  → x2 S −

.

![image 177](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile177.png>)

This maximum occurs when x2 = 4S. We also note that S ≤

c2 8

ζ(3), (5.5)

![image 178](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile178.png>)

where ζ(s) = ∞n=1 n1s is the Riemann zeta-function. At the point of maximum we then have that

![image 179](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile179.png>)

1/2

![image 180](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile180.png>)

x2 8

ζ(3) 2

= 2S2 1/2 ≤

c S1/2 < (0.55)c S1/2. Hence

x2 S −

![image 181](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile181.png>)

![image 182](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile182.png>)

S1 < (1 + ε2)c0 (0.275)c S. Using Corollary 11 we then arrive at

S1 <

(1 + ε2)(0.275) (1 − ε1)

![image 183](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile183.png>)

| h(n)|2 βn. (5.6)

c

n∈(2N)×

- 5.4.2. Analysis of S2. We follow the same outline as above, and now we obtain a slight improvement due to the restricted summation indices. In fact,


| h(n + 2)| (n + 2)3/2

c0 2 n∈2N:

| h(n)| n3/2

S2 ≤ | h(2)|(1 + ε2)

![image 184](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile184.png>)

![image 185](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile185.png>)

![image 186](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile186.png>)

2<n

| h(n)|2 n3

c0 2 n∈2N:

≤ | h(2)|(1 + ε2)

.

![image 187](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile187.png>)

![image 188](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile188.png>)

4≤n

Again we let | h(2)| = x and n∈(2N)×

| h(n)|2

n3 = S. We now seek to maximize x  → x S −

![image 189](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile189.png>)

x2 8

.

![image 190](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile190.png>)

![image 191](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile191.png>)

The maximum occurs when x = 8S/3. Using (5.5), at the point of maximum we have that

![image 192](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile192.png>)

![image 193](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile193.png>)

x2 8

2 ζ(3) 3√3

2S 3 ≤

8S 3

=

c S < (0.422)c S. Using Corollary 11, this leads to

x S −

![image 194](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile194.png>)

![image 195](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile195.png>)

![image 196](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile196.png>)

![image 197](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile197.png>)

![image 198](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile198.png>)

S2 <

(1 + ε2)(0.211) (1 − ε1)

![image 199](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile199.png>)

| h(n)|2 βn. (5.7)

c

n∈(2N)×

- 5.4.3. Analysis of S3. First notice that

S3 ≤ | h(4)|

21c0 8 n∈2N:

![image 200](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile200.png>)

4≤n

| h(n)| n3/2

![image 201](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile201.png>)

| h(n + 4)| (n + 4)3/2

![image 202](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile202.png>)

n3/2(n + 4)3/2 n(n + 1)(n + 2)(n + 3)(n + 4)

![image 203](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile203.png>)

.

Note that the function

x  →

x3/2(x + 4)3/2 x(x + 1)(x + 2)(x + 3)(x + 4) is decreasing on [4,∞). Therefore

![image 204](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile204.png>)

S3 ≤ | h(4)|

21c0 8

![image 205](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile205.png>)

4√2 5 × 6 × 7 n∈2N:

![image 206](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile206.png>)

![image 207](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile207.png>)

4≤n

| h(n)| n3/2

![image 208](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile208.png>)

| h(n + 4)| (n + 4)3/2

![image 209](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile209.png>)

.

Using the Cauchy-Schwarz inequality, we then obtain that

S3 ≤ | h(4)|

√2c0 20

![image 210](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile210.png>)

![image 211](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile211.png>)

  

n∈2N: 4≤n

| h(n)|2 n3

![image 212](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile212.png>)

  

1/2 

 

n∈2N: 6≤n

| h(n)|2 n3

![image 213](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile213.png>)

  

1/2

.

Now let | h(4)| = x and n∈2N:

4≤n

| h(n)|2

![image 214](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile214.png>)

n3 = T. We want to maximize

x  → x2 T −

x2 64

![image 215](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile215.png>)

1/2

.

This maximum occurs when x2 = 32T. Note also that T ≤

c2 8

![image 216](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile216.png>)

(ζ(3) − 1). (5.8) At the point of maximum, we then have that

x2 T −

x2 64

![image 217](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile217.png>)

1/2

= 4T ≤

4 ζ(3) − 1 √8

![image 218](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile218.png>)

![image 219](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile219.png>)

![image 220](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile220.png>)

c T1/2. Hence

S3 ≤ c0

![image 221](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile221.png>)

ζ(3) − 1 10

![image 222](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile222.png>)

c T < c0 (0.045)c T, and from Corollary 11 we arrive at

S3 <

(0.045) (1 − ε1)

![image 223](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile223.png>)

c

n∈2N: 4≤n

| h(n)|2 βn. (5.9)

- 5.4.4. Analysis of S4. We follow the same outline as in the analysis of S3 to get


√2c0 20 n∈2N:

| h(n)|2 n3

![image 224](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile224.png>)

.

S4 ≤ | h(4)|

![image 225](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile225.png>)

![image 226](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile226.png>)

6≤n

Again we let | h(4)| = x and n∈2N:

4≤n

| h(n)|2

n3 = T. We now seek to maximize

![image 227](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile227.png>)

x2 64

x  → x T −

![image 228](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile228.png>)

.

![image 229](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile229.png>)

The maximum occurs when x = 64T/3. Using (5.8), at the point of maximum we have that

![image 230](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile230.png>)

![image 231](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile231.png>)

x2 64

ζ(3) − 1 √8

64T 3

2T 3 ≤

- 2

![image 232](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile232.png>)

- 3


8 √3

c T. Hence

=

x T −

![image 233](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile233.png>)

![image 234](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile234.png>)

![image 235](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile235.png>)

![image 236](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile236.png>)

![image 237](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile237.png>)

![image 238](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile238.png>)

![image 239](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile239.png>)

√2 20

![image 240](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile240.png>)

![image 241](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile241.png>)

ζ(3) − 1 √8

- 2

![image 242](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile242.png>)

- 3


8 √3

c T < c0 (0.035)c T, and from Corollary 11 we arrive at

S4 ≤ c0

![image 243](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile243.png>)

![image 244](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile244.png>)

![image 245](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile245.png>)

![image 246](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile246.png>)

![image 247](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile247.png>)

(0.035) (1 − ε1)

S4 <

c

![image 248](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile248.png>)

| h(n)|2 βn. (5.10)

n∈2N: 4≤n

- 5.4.5. Analysis of S5. From Corollary 11 and Corollary 13, for every positive even integers m and n satisfying 4 ≤ m ≤ n, we have that

| δn,m| βn1/2βm1/2

![image 249](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile249.png>)

≤ γ3

c0 8n4

![image 250](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile250.png>)

n3/2 m3/2 (1 − ε1)c0 ≤

![image 251](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile251.png>)

γ3 8(1 − ε1)n

![image 252](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile252.png>)

. (5.11) Using (5.11), it follows that

S5 ≤ h ∞

n,m∈2N: 4≤m≤n

| h(n)|βn1/2 | h(m)|βm1/2 | δn,m| βn1/2βm1/2

![image 253](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile253.png>)

≤

γ3 8(1 − ε1)

![image 254](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile254.png>)

h ∞

n∈2N: 4≤n

| h(n)|βn1/2

  

m∈2N: 4≤m≤n

| h(m)|βm1/2 n

![image 255](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile255.png>)

  

≤

γ3 16(1 − ε1)

![image 256](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile256.png>)

h ∞

n∈2N: 4≤n

| h(n)|βn1/2

  

m∈2N: 4≤m≤n

| h(m)|βm1/2 (n/2) − 1

![image 257](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile257.png>)

  .

This last term can be estimated using the Cauchy-Schwarz inequality yielding

S5 ≤

γ3 16(1 − ε1)

![image 258](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile258.png>)

h ∞

  

n∈2N: 4≤n

| h(n)|2βn

  

1/2 

 

n∈2N: 4≤n

  

m∈2N: 4≤m≤n

| h(m)|βm1/2 (n/2) − 1

![image 259](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile259.png>)

  

2

 

1/2

. (5.12)

We now recall a sharp version of Hardy’s inequality for sequences.

Lemma 14. (Hardy’s inequality, cf. [17, p. 239]) Given any sequence {an} of nonnegative real numbers, we have ∞

n=1

a1 + a2 + ... + an n

![image 260](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile260.png>)

2

≤ 4

∞

n=1

a2n.

Using Hardy’s inequality in (5.12), with aj−1 = | h(2j)|β21j/2, for 2 ≤ j ≤ n2, yields S5 ≤

![image 261](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile261.png>)

γ3 8(1 − ε1)

![image 262](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile262.png>)

h ∞

n∈2N: 4≤n

| h(n)|2βn. (5.13)

- 5.4.6. Analysis of S6. For S6 we have (at least) the same bound (5.13) as for S5. This is suﬃcient for our purposes.


- 5.4.7. Conclusion. Putting together the estimates (5.6), (5.7), (5.9), (5.10) and (5.13) (twice), and recalling c = h ∞, we conclude that


0.08 + (1 + ε2)(0.486) + γ

3

![image 263](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile263.png>)

| h(n)|2βn.

4 (1 − ε1)

S1 + S2 + S3 + S4 + S5 + S6 <

h ∞

![image 264](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile264.png>)

n∈2N: 2≤n

The values of ε1 = 0.03, ε2 = 0.11 and γ3 = 1.3 provided by Corollaries 11 and 13 guarantee that 0.08 + (1 + ε2)(0.486) + γ (1 − ε1)

- 3

![image 265](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile265.png>)

- 4


< 0.974 < 1.

![image 266](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile266.png>)

This establishes (5.4) and concludes the proof of Theorem 2.

6. Proof of Theorem 6: A local estimate of Cauchy-Schwarz type

It is suﬃcient to show that there exists a universal ε0 > 0 such that for all g ∈ L2(S1), with g ⊥ 1 and g L2(S1) = 1, we have Ψ(1 + εg) ≥ 0 for 0 ≤ ε < ε0. In order to simplify notation, let us write gi := g(ωi).

Note that

Ψ(1 + εg) = ε2

(g1 + g2 + g3 − g4 − g5 − g6)2 |ω4 + ω5 + ω6|2 − 1 dΣ ω + O(ε3),

(S1)6

where the constant implicit in the big O notation is uniform for g satisfying g L2(S1) ≤ 1. Let us investigate the second order term

S :=

(g1 + g2 + g3 − g4 − g5 − g6)2 |ω4 + ω5 + ω6|2 − 1 dΣ ω

(S1)6

= 6

g12 |ω4 + ω5 + ω6|2 − 1 dΣ ω + 12

(S1)6

g1g2 |ω4 + ω5 + ω6|2 − 1 dΣ ω

(S1)6

− 18

g1g4 |ω4 + ω5 + ω6|2 − 1 dΣ ω

(S1)6

= 12

g12 dΣ ω − 12

(S1)6

g1g2 dΣ ω + 36

(S1)6

g12 (ω4 · ω5)dΣ ω

(S1)6

(6.1)

+ 36

g1g2 (ω4 · ω5)dΣ ω − 72

(S1)6

g1g4 (ω4 · ω5)dΣ ω

(S1)6

=: 12A − 12B + 36C + 36D − 72E.

- By (5.2) we have (note that we are not assuming here that g is even)

B = (2π)5

n∈Z×

| g(n)|2 (−1)n αn, (6.2)

- and similarly to (5.2) we obtain

A = g2σ ∗ σ ∗ σ ∗ σ ∗ σ ∗ σ(0) = (2π)5α0 g2(0) = (2π)5

n∈Z×

| g(n)|2 α0. (6.3)

By (5.3) it follows that

D = −(2π)5

n∈Z×

| g(n)|2 (−1)n αn, (6.4)

- and similarly to (5.3) we obtain




C = (2π)−2

g2σ σ e1σ e−1σ σ σ dx = −(2π)5 α0 g2(0) = −(2π)5

R2

| g(n)|2 α0. (6.5)

n∈Z×

Finally, expanding the identity

g1g4 |ω1 + ω2 + ω3 + ω6|2 dΣ ω, and using the symmetries to simplify, we arrive at

g1g4 |ω4 + ω5|2 dΣ ω =

(S1)6

(S1)6

B 2 −

3D 2

E = −

. (6.6) Combining (6.1), (6.2), (6.3), (6.4), (6.5) and (6.6) we obtain

![image 267](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile267.png>)

![image 268](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile268.png>)

S = 12(A + 2B + 3C + 12D) = 12 (2π)5

| g(n)|2 cn,

n∈Z×

where

cn = α0 + 2(−1)nαn − 3 α0 − 12(−1)n αn. We must verify that cn > η > 0 for all n ∈ Z×, with η universal. Since cn = c−n, we can restrict our attention to n > 0. The cases n = 1,2,...,6 can be veriﬁed by direct computation using the values on Table 1. For n ≥ 7, we use Theorem 10 to get

- 3

![image 269](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile269.png>)

- 4π2n


21 32π2(n − 1)n(n + 1)

7 500n4

6 αn − αn ≤

< 0.012 and hence

+

+

![image 270](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile270.png>)

![image 271](<2015-carneiro-sharp-trilinear-inequality-related_images/imageFile271.png>)

cn ≥ α0 − 3 α0 − 2 6 αn − αn > 0.134 − 0.024 > 0. This completes the proof of Theorem 6.

We note that Theorem 2 and Theorem 6 provide an alternative proof of Theorem 1.

Acknowledgements

The software Mathematica was used to compute the entries of Tables 1 and 2. We are grateful to Jon Bennett, Michael Christ, Ren´e Quilodr´an, Stefan Steinerberger and Po-Lam Yung for valuable discussions during the preparation of this work. Finally, we would like to thank HIM (Bonn), IMPA (Rio de Janeiro) and Universit`a di Ferrara for supporting research visits.

References

- [1] J. Bennett, N. Bez, A. Carbery and D. Hundertmark, Heat-ﬂow monotonicity of Strichartz norms, Anal. PDE 2 (2009), no. 2, 147–158.
- [2] J. Bennett, N. Bez, C. Jeavons and N. Pattakos, On sharp bilinear Strichartz estimates of Ozawa-Tsutsumi type, preprint at http://arxiv.org/abs/1404.2466. To appear in the Journal of the Mathematical Society of Japan.
- [3] N. Bez and C. Jeavons, A Sharp Sobolev–Strichartz estimate for the wave equation, Electron. Res. Announc. Math. Sci. 22 (2015), 46–54.
- [4] N. Bez and K. Rogers, A sharp Strichartz estimate for the wave equation with data in the energy space, J. Eur. Math. Soc. (JEMS) 15 (2013), no. 3, 805–823.
- [5] A. Bulut, Maximizers for the Strichartz inequalities for the wave equation, Diﬀerential Integral Equations 23 (2010), no. 11-12, 1035–1072.
- [6] E. Carneiro, A sharp inequality for the Strichartz norm, Int. Math. Res. Not. IMRN (2009), no. 16, 3127–3145.
- [7] E. Carneiro and D. Oliveira e Silva, Some sharp restriction inequalities on the sphere, Int. Math. Res. Not. IMRN (2015), no. 17, 8233–8267.
- [8] M. Charalambides, On restricting Cauchy-Pexider functional equations to submanifolds, Aequationes Math. 86 (2013), no. 3, 231–253.


- [9] M. Christ and R. Quilodra´n, Gaussians rarely extremize adjoint Fourier restriction inequalities for paraboloids, Proc. Amer. Math. Soc. 142 (2014), no. 3, 887–896.
- [10] M. Christ and S. Shao, Existence of extremals for a Fourier restriction inequality, Anal. PDE. 5 (2012), no. 2, 261–312.
- [11] M. Christ and S. Shao, On the extremizers of an adjoint Fourier restriction inequality, Adv. Math. 230 (2012), no. 3, 957–977.
- [12] L. Fanelli, L. Vega and N. Visciglia, On the existence of maximizers for a family of restriction theorems, Bull. Lond. Math. Soc. 43 (2011), no. 4, 811–817.
- [13] L. Fanelli, L. Vega and N. Visciglia, Existence of maximizers for Sobolev-Strichartz inequalities, Adv. Math. 229 (2012), no. 3, 1912–1923.
- [14] D. Foschi, Maximizers for the Strichartz inequality, J. Eur. Math. Soc. (JEMS) 9 (2007), no. 4, 739–774.
- [15] D. Foschi, Global maximizers for the sphere adjoint Fourier restriction inequality, J. Funct. Anal. 268 (2015), 690–702.
- [16] D. Foschi and S. Klainerman, Bilinear space-time estimates for homogeneous wave equations, Ann. Sci. Ecole´ Norm. Sup.

(4) 33 (2000), no. 2, 211–274.

- [17] G. H. Hardy, J. E. Littlewood and G. P´olya, Inequalities, Reprint of the 1952 edition, Cambridge University Press, Cambridge, 1988.
- [18] D. Hundertmark and S. Shao, Analyticity of extremizers to the Airy-Strichartz inequality, Bull. Lond. Math. Soc. 44

(2012), no. 2, 336–352.

- [19] D. Hundertmark and V. Zharnitsky, On sharp Strichartz inequalities in low dimensions, Int. Math. Res. Not. IMRN (2006), Art. ID 34080, 1–18.
- [20] C. Jeavons, A sharp bilinear estimate for the Klein-Gordon equation in arbitrary space-time dimensions, Diﬀerential Integral Equations 27 (2014), no. 1-2, 137–156.
- [21] M. Kunze, On the existence of a maximizer for the Strichartz inequality, Comm. Math. Phys. 243 (2003), no. 1, 137–162.
- [22] L. J. Landau, Bessel functions: monotonicity and bounds, J. London Math. Soc. (2) 61 (2000), 197–215.
- [23] D. Oliveira e Silva, Extremals for Fourier restriction inequalities: convex arcs, J. Anal. Math. 124 (2014), 337–385.
- [24] D. Oliveira e Silva and C. Thiele, Estimates for certain integrals of products of six Bessel functions, preprint at http://arxiv.org/abs/1509.06309.
- [25] T. Ozawa and K. Rogers, Sharp Morawetz estimates, J. Anal. Math. 121 (2013), 163–175.
- [26] R. Quilodra´n, On extremizing sequences for the adjoint restriction inequality on the cone, J. Lond. Math. Soc. (2) 87

(2013), no. 1, 223–246.

- [27] J. Ramos, A reﬁnement of the Strichartz inequality for the wave equation with applications, Adv. Math. 230 (2012), no. 2, 649–698.
- [28] S. Shao, Maximizers for the Strichartz and the Sobolev-Strichartz inequalities for the Schro¨dinger equation, Electron. J. Diﬀerential Equations (2009), No. 3, 13 pp.
- [29] S. Shao, The linear proﬁle decomposition for the Airy equation and the existence of maximizers for the Airy-Strichartz inequality, Anal. PDE 2 (2009), no. 1, 83–117.
- [30] S. Shao, On existence of extremizers for the Tomas-Stein inequality for S1, preprint at http://arxiv.org/abs/1507.04302.
- [31] E. M. Stein, Harmonic Analysis: Real-Variable Methods, Orthogonality, and Oscillatory Integrals, Princeton Univ. Press, Princeton, NJ, 1993.
- [32] P. Tomas, A restriction theorem for the Fourier transform, Bull. Amer. Math. Soc. 81 (1975), no. 2, 477–478.


IMPA - Instituto Nacional de Matematica´ Pura e Aplicada, Estrada Dona Castorina 110, Rio de Janeiro, RJ 22460-320, Brazil

E-mail address: carneiro@impa.br

Dipartimento di Matematica e Informatica, Universita` di Ferrara, via Macchiavelli 35, 44121 Ferrara, Italy E-mail address: damiano.foschi@unife.it

Hausdorff Center for Mathematics, Universitat¨ Bonn, Endenicher Allee 60, 53115 Bonn, Germany E-mail address: dosilva@math.uni-bonn.de E-mail address: thiele@math.uni-bonn.de

