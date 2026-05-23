arXiv:1711.07926v1[math.NA]21Nov2017

High Order Finite Difference Schemes for the Heat Equation Whose Convergence Rates are Higher Than Their Truncation Errors1,2

A. Ditkowski

Abstract Typically when a semi-discrete approximation to a partial differential equation (PDE) is constructed a discretization of the spatial operator with a truncation error τ is derived. This discrete operator should be semi-bounded for the scheme to be stable. Under these conditions the Lax–Ricchtmyer equivalence theorem assures that the scheme convergesand that the error will be, at most, of the order of τ . In most cases the error is in indeed of the order of τ .

We demonstrate that for the Heat equation stable schemes can be constructed, whose truncation errors are τ, however, the actual errors are much smaller. This gives more degrees of freedom in the design of schemes which can make

- them more efﬁcient (more accurate or compact) than standard schemes. In some cases the accuracy of the schemes can be further enhanced using post-processing procedures.


## 1 Introduction

Consider the differential problem:

∂u ∂t

∂ ∂x

u , x ∈ Ω ⊂ Rd ,t ≥ 0

= P

![image 1](<2017-ditkowski-high-order-finite-difference_images/imageFile1.png>)

![image 2](<2017-ditkowski-high-order-finite-difference_images/imageFile2.png>)

(1) u(t = 0) = f(x) .

where u = (u1,...,um)T and P(∂/∂x) is a linear differential operator with appropriate boundary conditions. It is assumed that this problem is well posed, i.e. ∃K(t) < ∞ such that ||u(t)|| ≤ K(t)||f||, where typically K(t) = Keαt.

Let Q be the discretization of P(∂/∂x) where we assume:

- Assumption 1: The discrete operator Q is based on grid points {xj}, j = 1,...,N.
- Assumption 2: Q is semi–bounded in some equivalent scalar product (·,·)H = (·,H·), i.e (w,Qw)H ≤ α(w,w)H = α w 2H . (2)
- Assumption 3: The local truncation error vector of Q is Te which is deﬁned, at each entry j by (Te)j = (Pw(xj)) − (Qw)j , (3)


where w(x) is a smooth function and w is the projection of w(x) onto the grid. It is assumed that Te −−−→ N→∞ 0. Consider the semi–discrete approximation:

![image 3](<2017-ditkowski-high-order-finite-difference_images/imageFile3.png>)

A. Ditkowski School of Mathematical Sciences, Tel Aviv University, Tel Aviv 69978, Israel e-mail: adid@post.tau.ac.il

- 1. The ﬁnal publication is available at link.springer.com via http://dx.doi.org/10.1007/978-3-319-19800-2 13

![image 4](<2017-ditkowski-high-order-finite-difference_images/imageFile4.png>)

- 2. In later works these schemes are called Error Inhibiting Schemes (EIS).


1

∂v ∂t

= Qv , t ≥ 0 (4)

![image 5](<2017-ditkowski-high-order-finite-difference_images/imageFile5.png>)

v(t = 0) = f . Proposition: Under Assumptions 1–3 The semi–discrete approximation converges. Proof: Let u is the projection of u(x,t) onto the grid. Then, from assumption 3,

∂u ∂t

= Pu = Qu+Te . (5) Let E = u−v then by subtracting (4) from (5) one obtains the equation for E, namely

![image 6](<2017-ditkowski-high-order-finite-difference_images/imageFile6.png>)

∂E ∂t

= QE+Te . (6)

![image 7](<2017-ditkowski-high-order-finite-difference_images/imageFile7.png>)

Next, by taking the H scalar product with E, using assumption 2 and the Schwartz inequality the following estimate can be derived

∂E ∂t H

E,

![image 8](<2017-ditkowski-high-order-finite-difference_images/imageFile8.png>)

=

∂ ∂t

∂ ∂t ||E H = (E,QE)H +(E,Te)H ≤ α(E,E)H + E H Te H .

- 1

![image 9](<2017-ditkowski-high-order-finite-difference_images/imageFile9.png>)

- 2


(E,E)H = E H

![image 10](<2017-ditkowski-high-order-finite-difference_images/imageFile10.png>)

![image 11](<2017-ditkowski-high-order-finite-difference_images/imageFile11.png>)

Thus

∂ ∂t

E H ≤ α E H + Te H . (7) Therefore:

![image 12](<2017-ditkowski-high-order-finite-difference_images/imageFile12.png>)

eαt −1

Te H −−−→N→∞ 0 . (8)

E H (t) ≤ E H (t = 0)eαt +

max

![image 13](<2017-ditkowski-high-order-finite-difference_images/imageFile13.png>)

α

0≤τ≤t

Here we assumed that E H (t = 0) is either 0, or at least of the order of machine accuracy. Equation (8) establishes the fact that if the scheme is stable and consistent, the numerical solution v converges to the projection of the exact

solution onto the grid, u. Furthermore, it assures that the error will be at most in the truncation error Te H. This is one part of the landmark Lax–Richtmyer equivalence theorem for semi–discrete approximation. See e.g. [6].

Due to this and similar results the common way for constructing ﬁnite difference schemes is to derive a semi– bounded Q with proper truncation error. Typically the error E H is indeed of the order of Te H.

It should be noted, however, that (6) is the exact equation for the error dynamics, while (8) is an estimate. In this paper we present ﬁnite difference schemes in which the errors are smaller than their truncation errors. It is well known that boundary conditions can be of one order lower accuracy without destroying the convergence rate expected from the approximation at inner points, see e.g. [4], [5], [1] and [10]. In [5] and [10] it was shown that for parabolic, incompletely parabolic and 2nd-order hyperbolic equations the boundary conditions can be of two order less. Here, however, we consider low order truncation errors in most or all of the grid points.

This paper is constructed as follows; in Section 2 we present a preliminary example and illustrate the mechanism which reduces the error. In Section 3 we present a two–point block scheme which has a ﬁrst order truncation error but has a second or third order error. In Section 4 two three–point block schemes are presented. Discussion and remarks are presented in Section 5.

## 2 Preliminary Example

Consider the heat equation

∂2u ∂x2

∂u ∂t

+F(x,t) , x ∈ [0,2π) ,t ≥ 0

=

![image 14](<2017-ditkowski-high-order-finite-difference_images/imageFile14.png>)

![image 15](<2017-ditkowski-high-order-finite-difference_images/imageFile15.png>)

u(t = 0) = f(x) (9)

with periodic boundary conditions. Let the scheme be:

∂vj ∂t

= D+D−vj + (−1)jcvj + Fj(t) ; xj = jh, h = 2π/N , N is even

![image 16](<2017-ditkowski-high-order-finite-difference_images/imageFile16.png>)

vj(t = 0) = fj (10) where Fj(t) is the projection of F(x,t) onto the spatial grid. The truncation error is

h2 12

(uj)xxxx +O(h2)−(−1)jcvj = O(1) . (11)

(Te)j =

![image 17](<2017-ditkowski-high-order-finite-difference_images/imageFile17.png>)

Formally, this scheme is not consistent. The scheme (10) was run with the initial condition f(x) = cos(x), F = 0 and N = 32,64,...,1024 with forward–Euler time propagator. The plots of log10 E vs. log10N, at tﬁnal = 2π, for c = 0,0.5,1 are presented in Figure 1a. It can be seen that this is a second order scheme.

# a b

10−2

10−1

|c=0 , slope: −2.0069<br><br>c=0.5, slope: −2.0051<br><br>c=1.0, slope: −2.0091<br>|
|---|


10−2

10−3

10−3

10−4

||E||h

||E||h

10−4

10−5

10−5

10−6

|c=0 , slope: −2.00410 c=1/6 , slope: −2.00503<br><br>c=−1/6 , slope: −2.12895 c=−1/4 , slope: −3.01426<br><br>|
|---|


10−6

10−7

10−7

102 103

101 102 103

number of grid points

number of grid points

- Fig. 1 Convergence plots, log10 E vs. log10N, for different values of c. a: Scheme (10). b: Scheme (16).


In order to understand this phenomenon let us consider one high frequency mode of the error3. Denote (Tc)j = (−1)j cvj. This term can also be written as:

(Tc)j = (−1)j chα = chαeiNxj/2 (12) For the scheme (10) α = 0. The equation for the error term caused by Tc is

∂Ec ∂t

= D+D−Ec +Tc (13)

![image 18](<2017-ditkowski-high-order-finite-difference_images/imageFile18.png>)

Since (Ec)j = EˆceiNxj/2√2π, Eˆ c ∈ C, then the equation for Eˆc is

![image 19](<2017-ditkowski-high-order-finite-difference_images/imageFile19.png>)

![image 20](<2017-ditkowski-high-order-finite-difference_images/imageFile20.png>)

- 3 This scheme was presented for demonstrating the phenomenon that the error, due to high frequency modes, is lower than the truncation error. As this is not a practical scheme, full analysis of the error is not presented, only a demonstration of the dynamics of high frequency error modes is presented. Full analysis is given for the scheme presented in the next section


∂Eˆc ∂t

= −

![image 21](<2017-ditkowski-high-order-finite-difference_images/imageFile21.png>)

N 2

![image 22](<2017-ditkowski-high-order-finite-difference_images/imageFile22.png>)

2

Ec +c′hα (14)

Therefore,

2

2 N

Ec (t) = E ˆ c (t) = E ˆc (0)e−(N2 )2t +

1−e−(N2 )2t c′hα (15)

![image 23](<2017-ditkowski-high-order-finite-difference_images/imageFile23.png>)

![image 24](<2017-ditkowski-high-order-finite-difference_images/imageFile24.png>)

![image 25](<2017-ditkowski-high-order-finite-difference_images/imageFile25.png>)

≤ E ˆc (0)e−(N2 )2t +O hα+2

![image 26](<2017-ditkowski-high-order-finite-difference_images/imageFile26.png>)

Note that the actual error, Ec (t), is two orders lower that the truncation error, Tc . In the next sections we present practical schemes which utilize this idea.

- 3 Two–point Block, 3rd Order Scheme


Let the grid be: xj = jh, h = 2π/(N +1) and xj+1/2 = xj +h/2, j = 0,...N. Altogether there are 2(N +1) points with spacing of h/2. For simplicity, we assume that N is even.

Consider the approximation:

d2 dx2

1 (h/2)2

uj ≈

uj−1/2 −2uj +uj+1/2 + c −uj−1/2+3uj −3uj+1/2+uj+1

![image 27](<2017-ditkowski-high-order-finite-difference_images/imageFile27.png>)

![image 28](<2017-ditkowski-high-order-finite-difference_images/imageFile28.png>)

(16) d2 dx2

1 (h/2)2

uj+1/2 ≈

uj −2uj+1/2+uj+1 + c uj−1/2 −3uj +3uj+1/2−uj+1

![image 29](<2017-ditkowski-high-order-finite-difference_images/imageFile29.png>)

![image 30](<2017-ditkowski-high-order-finite-difference_images/imageFile30.png>)

The truncation errors are:

1 12

(Te)j=

![image 31](<2017-ditkowski-high-order-finite-difference_images/imageFile31.png>)

h 2

![image 32](<2017-ditkowski-high-order-finite-difference_images/imageFile32.png>)

2

(uj)xxxx +c

h 2

![image 33](<2017-ditkowski-high-order-finite-difference_images/imageFile33.png>)

- 1

![image 34](<2017-ditkowski-high-order-finite-difference_images/imageFile34.png>)

- 2


(uj)xxx +

h 2

![image 35](<2017-ditkowski-high-order-finite-difference_images/imageFile35.png>)

2

(uj)xxxx +O(h3) = O(h)

1 12

=

(Te)j+1

![image 36](<2017-ditkowski-high-order-finite-difference_images/imageFile36.png>)

![image 37](<2017-ditkowski-high-order-finite-difference_images/imageFile37.png>)

2

h 2

![image 38](<2017-ditkowski-high-order-finite-difference_images/imageFile38.png>)

2

+c −

uj+1

![image 39](<2017-ditkowski-high-order-finite-difference_images/imageFile39.png>)

2 xxxx

h 2

![image 40](<2017-ditkowski-high-order-finite-difference_images/imageFile40.png>)

- 1

![image 41](<2017-ditkowski-high-order-finite-difference_images/imageFile41.png>)

- 2


+

uj+1

![image 42](<2017-ditkowski-high-order-finite-difference_images/imageFile42.png>)

2 xxx

h 2

![image 43](<2017-ditkowski-high-order-finite-difference_images/imageFile43.png>)

2

uj+1

![image 44](<2017-ditkowski-high-order-finite-difference_images/imageFile44.png>)

2 xxxx

+O(h3) = O(h)

(17)

The motivation leading to this scheme is that the highly oscillating O(h) error terms will be dissipated, as in the previous example, while the O(h2) terms will be canceled, for the proper value of c.

3.1 Analysis

Let ω ∈ {−N/2,...,N/2} and

 

ω−(N +1) ω > 0 ω+(N +1) ω ≤ 0

ν =

(18)



Then

eiωxj = eiνxj and eiωxj+1/2 = −eiνxj+1/2 . (19) We look for eigenvectors in the form of:









. eiωxj eiωxj+1/2

. eiνxj eiνxj+1/2

αk √2π

βk √2π

ψk(ω) =

+

(20)

 

 

 

 

![image 45](<2017-ditkowski-high-order-finite-difference_images/imageFile45.png>)

![image 46](<2017-ditkowski-high-order-finite-difference_images/imageFile46.png>)

![image 47](<2017-ditkowski-high-order-finite-difference_images/imageFile47.png>)

![image 48](<2017-ditkowski-high-order-finite-difference_images/imageFile48.png>)

.

.

where, for normalization, it is require that |αk|2 +|βk|2 = 1, k = 1,2. The expressions for αk, βk and the eigenvalues (symbols) Qˆk are:

![image 49](<2017-ditkowski-high-order-finite-difference_images/imageFile49.png>)

c2cos(4(h/2)ω)+4(2c−1)∆cos((h/2)ω)+4(c(7c−8)+2)cos(2(h/2)ω)+(35c−32)c+8 2c2(2sin((h/2)ω)+sin(2(h/2)ω))2

α1 = 1+

![image 50](<2017-ditkowski-high-order-finite-difference_images/imageFile50.png>)

−1

(21)

i((8c−4)cos((h/2)ω)+∆) 2c(2sin((h/2)ω)+sin(2(h/2)ω))α1−1

β1 = −

![image 51](<2017-ditkowski-high-order-finite-difference_images/imageFile51.png>)

(22)

![image 52](<2017-ditkowski-high-order-finite-difference_images/imageFile52.png>)

2c2(2sin((h/2)ω)+sin(2(h/2)ω))2 c2cos(4(h/2)ω)+4(1−2c)∆cos((h/2)ω)+4(c(7c−8)+2)cos(2(h/2)ω)+(35c−32)c+8

β2 = 1+

![image 53](<2017-ditkowski-high-order-finite-difference_images/imageFile53.png>)

−1

(23)

where

2ic(2sin((h/2)ω)+sin(2(h/2)ω)) ((4−8c)cos((h/2)ω)+∆)β2−1

α2 = −

![image 54](<2017-ditkowski-high-order-finite-difference_images/imageFile54.png>)

(24)

![image 55](<2017-ditkowski-high-order-finite-difference_images/imageFile55.png>)

∆ = 2c2cos(4(h/2)ω)+38c2+8(c−1)(3c−1)cos(2(h/2)ω)−32c+8 (25) and the

Qˆ1,2(ω) = −4+2c(cos(2(h/2)ω)+3)±∆

. (26)

![image 56](<2017-ditkowski-high-order-finite-difference_images/imageFile56.png>)

2(h/2)2

It can be shown that the eigenvalues are real and non positive for |c| < 1/2. It should be noted that by construction ψk(ω) ⊥ ψk(ν), ω = ν. However, for all ω ψ1(ω) and ψ2(ω) are not orthogonal. Nevertheless it can be shown that they are ’almost’ perpendicular in the sense that

cos(θ(ω)) =

ψ1(ω),ψ2(ω) ψ1(ω) ψ2(ω)

![image 57](<2017-ditkowski-high-order-finite-difference_images/imageFile57.png>)

> 0.9

Therefore the scheme is stable.

For ωh ≪ 1 the eigenvalues and eigenvectors are:

2

(1+4c)ω4 12−24c

h 2

Qˆ1(ω) = −ω2+

+O(h4) (27)

![image 58](<2017-ditkowski-high-order-finite-difference_images/imageFile58.png>)

![image 59](<2017-ditkowski-high-order-finite-difference_images/imageFile59.png>)

6

3

c2 32(1−2c)2

ωh 2

ωh 2

ic 4−8c

+O(h5) (28) and

+O h7 , β1 = −

α1 = 1−

![image 60](<2017-ditkowski-high-order-finite-difference_images/imageFile60.png>)

![image 61](<2017-ditkowski-high-order-finite-difference_images/imageFile61.png>)

![image 62](<2017-ditkowski-high-order-finite-difference_images/imageFile62.png>)

![image 63](<2017-ditkowski-high-order-finite-difference_images/imageFile63.png>)

4−8c (h/2)2

+(1−4c)ω2+O(h2) (29)

Qˆ2(ω) = −

![image 64](<2017-ditkowski-high-order-finite-difference_images/imageFile64.png>)

ωh 2

ic 2c−1

+O(h3) , β2 = 1+O(h2) (30) If the initial condition is

α2 =

![image 65](<2017-ditkowski-high-order-finite-difference_images/imageFile65.png>)

![image 66](<2017-ditkowski-high-order-finite-difference_images/imageFile66.png>)

ωxj+ 1

(0) = ei

vj(0) = eiωxj ,vj+1

2 ; ω2h ≪ 1 (31)

![image 67](<2017-ditkowski-high-order-finite-difference_images/imageFile67.png>)

![image 68](<2017-ditkowski-high-order-finite-difference_images/imageFile68.png>)

2

- then


(1+4c)ω2t 12−24c

(v)j (t) = e−ω2t 1−

![image 69](<2017-ditkowski-high-order-finite-difference_images/imageFile69.png>)

ωh 2

![image 70](<2017-ditkowski-high-order-finite-difference_images/imageFile70.png>)

2

ic 4−8c

+O(h4) eiωxj + −

![image 71](<2017-ditkowski-high-order-finite-difference_images/imageFile71.png>)

ωh 2

![image 72](<2017-ditkowski-high-order-finite-difference_images/imageFile72.png>)

3

+O(h5) eiνxj (32)

. Therefore the scheme is, in general, 2nd order and it is 3rd order if c = −1/4. Note that by naive analysis of the truncation error terms, (17), one would expect to get 3rd order with c = −1/6.

The same expression hold for xj+1

![image 73](<2017-ditkowski-high-order-finite-difference_images/imageFile73.png>)

2

We used the approximation (16) for solving the heat equation (9), where F(x,t) and the initial condition were chosen such that the exact solution is u(x,t) = exp(cos(x −t)). The scheme was run with N = 32,64,...,1024. 4th order Runge–Kutta scheme was used for time integration. The plots of log10 E vs. log10N for c = 0,1/6,−1/6,−1/4 are presented in Figure 1b. As can be seen, the results are as predicted by the analysis.

## 4 Three–point Block

In this section we brieﬂy present two schemes which are based on three–point block. Here we use the grid, xj = jh, h = 2π/(N+1) with the internal block nodes xj+1/3 = xj +h/3 and xj+2/3 = xj +2h/3, j = 0,...N. Altogether there are 3(N +1) points with spacing of h/3.

three–point block, 3rd order scheme Consider the approximation:

d2 dx2

1 4(h/3)2

uj =

![image 74](<2017-ditkowski-high-order-finite-difference_images/imageFile74.png>)

![image 75](<2017-ditkowski-high-order-finite-difference_images/imageFile75.png>)

d2 dx2

1 4(h/3)2

uj+1/3 =

![image 76](<2017-ditkowski-high-order-finite-difference_images/imageFile76.png>)

![image 77](<2017-ditkowski-high-order-finite-difference_images/imageFile77.png>)

d2 dx2

1 4(h/3)2

uj+2/3 =

![image 78](<2017-ditkowski-high-order-finite-difference_images/imageFile78.png>)

![image 79](<2017-ditkowski-high-order-finite-difference_images/imageFile79.png>)

4uj−1/3−8uj +4uj+1/3 + c −uj−1/3 +3uj −3uj+1/3+uj+2/3 + O(h)

4uj −8uj+1/3+4uj+2/3 + O(h2) (33)

4uj+1/3−8uj+2/3+4uj+1 + c uj −3uj+1/3+3uj+2/3−uj+1 + O(h)

This scheme was run under the same conditions as the example in Section 3. As in the previous example the truncation error is of O(h), however this is a 2nd order scheme and 3rd order for c = 1.340. The convergence results are presented in Figure 2a.

# a b

10−1

10−2

|c=0 , slope: −3.99411 c=1.0 , slope: −4.02288<br><br>c=−1.0 , slope: −4.02185 c=−0.385, slope: −5.04424<br><br>|
|---|


10−2

10−4

10−3

10−6

10−4

||E||h

||E||h

10−5

10−8

10−6

10−10

|c=0 , slope: −2.00029 c=1.0 , slope: −2.00272<br><br>c=−1.0 , slope: −2.11597 c=−1.340, slope: −2.99559<br><br>|
|---|


10−7

10−8

10−12

101 102 103

101 102 103

number of grid points

number of grid points

- Fig. 2 Convergence plots, log10 E vs. log10N, for different values of c. a: Scheme (33). b: Scheme (34).


three–point block, 5th order scheme

d2 dx2

1 12(h/3)2 −uj−2/3 +16uj−1/3−30uj +16uj+1/3−uj+2/3 + c uj−2/3 −5uj−1/3+10uj −10uj+1/3+5uj+2/3−uj + O(h3)

uj =

![image 80](<2017-ditkowski-high-order-finite-difference_images/imageFile80.png>)

![image 81](<2017-ditkowski-high-order-finite-difference_images/imageFile81.png>)

d2 dx2

1

12(h/3)2 −uj−1/3 +16uj −30uj+1/3+16uj+2/3−uj + O(h4) (34) d2 dx2

uj+1/3 =

![image 82](<2017-ditkowski-high-order-finite-difference_images/imageFile82.png>)

![image 83](<2017-ditkowski-high-order-finite-difference_images/imageFile83.png>)

1 12(h/3)2 −uj +16uj+1/3−30uj+2/3+16uj+1−uj+4/3 + c −uj−1/3+5uj −10uj+1/3+10uj+2/3−5uj+1+uj+4/3 + O(h3)

uj+2/3 =

![image 84](<2017-ditkowski-high-order-finite-difference_images/imageFile84.png>)

![image 85](<2017-ditkowski-high-order-finite-difference_images/imageFile85.png>)

This scheme was run under the same conditions as the previous examples, with the exception that now a 6th order Runge–Kutta scheme was used for time integration. Here the truncation error is of O(h3), however this is a 4th order scheme and 5th order for c = −0.385. The convergence results are presented in Figure 2b.

It should be noted that by taking c = 1 the coefﬁcients of uj−2/3 and uj+4/3 are 0. Therefore the scheme is more ’compact’ than standard explicit 4th order scheme in the sense that the scheme depends only on one term, on each side, out of the three–point block uj,uj+1/3,uj+2/3. Potentially, this thinner stencil helps in the derivation of boundary schemes for initial–boundary value problems.

- 5 Summary


In this paper we presented a few block–ﬁnite–difference schemes in which the actual errors are much smaller than their truncation errors. This reduction of error was achieved by constructing the truncation errors to be oscillatory and using the dissipative property of the scheme.

A comparison between standard and block ﬁnite difference schemes in terms of the number of points out of the cell and operation count is presented in Table 1. As can be seen, in terms of accuracy and computational cost the 3rd and 5th order schemes are between the standards 2nd and 4th order and 4th and 6th order schemes respectively.

Scheme Points out the block Number of operations Scheme Points out the block Number of operations

![image 86](<2017-ditkowski-high-order-finite-difference_images/imageFile86.png>)

(at each side) + × (at each side) + × standard 2nd order 1 2 3 2–point block 3rd order 1 3 4 standard 4th order 2 4 5 3–point block 3rd order 1 223 323 standard 6th order 3 6 7 3–point block 5th order 2 423 523

![image 87](<2017-ditkowski-high-order-finite-difference_images/imageFile87.png>)

![image 88](<2017-ditkowski-high-order-finite-difference_images/imageFile88.png>)

![image 89](<2017-ditkowski-high-order-finite-difference_images/imageFile89.png>)

![image 90](<2017-ditkowski-high-order-finite-difference_images/imageFile90.png>)

![image 91](<2017-ditkowski-high-order-finite-difference_images/imageFile91.png>)

![image 92](<2017-ditkowski-high-order-finite-difference_images/imageFile92.png>)

![image 93](<2017-ditkowski-high-order-finite-difference_images/imageFile93.png>)

![image 94](<2017-ditkowski-high-order-finite-difference_images/imageFile94.png>)

![image 95](<2017-ditkowski-high-order-finite-difference_images/imageFile95.png>)

3–point block 4th order 1 4 5 compact

![image 96](<2017-ditkowski-high-order-finite-difference_images/imageFile96.png>)

Table 1 Comparison between standard ﬁnite difference schemes and the ones presented on Sections 3,4.

If c = −1/4 in the two–point block, 3rd order scheme (16), the leading term in the error is highly oscillatory, see (32). It was suggested by Jennifer K. Ryan [8] that this term can be ﬁltered by post–processing. In this technique the high frequency error terms are ﬁltered using convolution with a proper kernel. This method was successfully applied

- to the discontinuous Galerkin method. As this ﬁltering is done only once, after the ﬁnal time step, the cost is minimal, see e.g. [9], [2], [3]. Here we used a global spectral ﬁlter and the local ﬁlter suggested in [3]. As can be seen in ﬁgure 3, the ﬁltered scheme is 4th order accurate. The difference between both kernels is that the global ﬁlter is more computationally expensive, O(N logN) for proper values of N, but is accurate for small values of N while the local ﬁlter requires only O(N) operation but is accurate only for large values of N. The investigation of which is the optimal ﬁlter for these schemes is a topic for future research.


100

spectral filter, slope: −3.99978 * local filter , slope: −4.04835 no filter , slope: −3.01298

10−2

10−4

||E||h

10−6

10−8

10−10

10−12

101 102 103 104

number of grid points

- Fig. 3 Convergence plots, log10 E vs. log10N, for scheme (16), c−1/4. with no post–processing, with spectral ﬁlter and with the ﬁlter suggested in [3].


It should be noted that that ﬁnite difference representations of discontinuous Galerkin schemes for the heat equation have a similar form to the schemes presented above. They may also present similar enhancing of accuracy. See [11]. This manuscript was the inspiration to the current work. As was also pointed out in [11] the increasing of accuracy may be related to a phenomenon called Supra–Convergence [7].

Further research of the properties and implementations of these schemes as well as the existence of these kinds of schemes for hyperbolic problems are topics for future research.

Acknowledgments The author would like to thank Jennifer K. Ryan, Chi–Wang Shu and Sigal Gottlieb for the fruitful discussions and their help. The author would also like to thank the anonymous reviewers for their useful remarks.

References

- 1. Saul Abarbanel, Adi Ditkowski, and Bertil Gustafsson, On error bounds of ﬁnite difference approximations to partial differential equationstemporal behavior and rate of convergence, Journal of Scientiﬁc Computing 15 (2000), no. 1, 79–116.
- 2. Bernardo Cockburn, Mitchell Luskin, Chi-Wang Shu, and Endre Suli, Post-processing of galerkin methods for hyperbolic problems, Springer, 2000.
- 3. , Enhanced accuracy by post-processing for ﬁnite element methods for hyperbolic equations, Mathematics of Computation 72

![image 97](<2017-ditkowski-high-order-finite-difference_images/imageFile97.png>)

(2003), no. 242, 577–606.

- 4. Bertil Gustafsson, The convergence rate for difference approximations to mixed initial boundary value problems, Mathematics of Computation 29 (1975), no. 130, 396–406.
- 5. , The convergence rate for difference approximations to general mixed initial-boundary value problems, SIAM Journal on Numerical Analysis 18 (1981), no. 2, 179–190.

![image 98](<2017-ditkowski-high-order-finite-difference_images/imageFile98.png>)

- 6. Bertil Gustafsson, Heinz-Otto Kreiss, and Joseph Oliger, Time-dependent problems and difference methods, John Wiley & Sons, 1995.
- 7. H-O Kreiss, Thomas A Manteuffel, B Swartz, B Wendroff, and AB White, Supra-convergent schemes on irregular grids, Mathematics of Computation 47 (1986), no. 176, 537–554.
- 8. Jennifer Ryan, Privet communucation.
- 9. Jennifer Ryan, Chi-Wang Shu, and Harold Atkins, Extension of a post processing technique for the discontinuous galerkin method for hyperbolic equations with application to an aeroacoustic problem, SIAM Journal on Scientiﬁc Computing 26 (2005), no. 3, 821–843.
- 10. Magnus Sva¨rd and Jan Nordstro¨m, On the order of accuracy for difference approximations of initial-boundary value problems, Journal of Computational Physics 218 (2006), no. 1, 333–352.
- 11. Mengping Zhang and Chi-Wang Shu, An analysis of three different formulations of the discontinuous galerkin method for diffusion equations, Mathematical Models and Methods in Applied Sciences 13 (2003), no. 03, 395–413.


