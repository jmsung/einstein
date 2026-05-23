arXiv:1801.00270v1[math.NA]31Dec2017

A HERMITE WENO RECONSTRUCTION FOR FOURTH ORDER TEMPORAL ACCURATE SCHEMES BASED ON THE GRP SOLVER FOR HYPERBOLIC CONSERVATION LAWS

ZHIFANG DU AND JIEQUAN LI

Abstract. This paper develops a new ﬁfth order accurate Hermite WENO (HWENO) reconstruction method for hyperbolic conservation schemes in the framework of the two-stage fourth order accurate temporal discretization in [J. Li and Z. Du, A two-stage fourth order time-accurate discretization Lax–Wendroﬀ type ﬂow solvers, I. Hyperbolic conservation laws, SIAM, J. Sci. Comput., 38 (2016), pp. A3046–A3069]. Instead of computing the ﬁrst moment of the solution additionally in the conventional HWENO or DG approach, we can directly take the interface values, which are already available in the numerical ﬂux construction using the generalized Riemann problem (GRP) solver, to approximate the ﬁrst moment. The resulting scheme is fourth order temporal accurate by only invoking the HWENO reconstruction twice so that it becomes more compact. Numerical experiments show that such compactness makes signiﬁcant impact on the resolution of nonlinear waves.

Key Words. Hyperbolic conservation laws, Two-stage fourth-order accurate scheme, Hermite WENO reconstruction, GRP solver.

1. Introduction

In the development of high order accurate schemes for hyperbolic conservation laws, two families of approaches play important roles: one belongs to the method of line that achieves the temporal accuracy using the Runge-Kutta strategy [7, 27, 13, 8, 25]; the other is the LaxWendroﬀ type approach that adopts the Cauchy-Kowaleveski expansions to design temporalspatial coupled schemes [10, 1, 3, 15, 20, 31, 18]. Either family of approaches have their own advantages and disadvantages. The former has the simplicity in their practical implementation thanks to exact or approximate Riemann solvers, but the multi-stage temporal iteration inevitably causes the enlargement of the size of stencils; the latter can avoid the multi-stage temporal iteration but have to repeatedly make the diﬀerentiation of governing equations in order to construct high order accurate numerical ﬂuxes. A recent two-stage fourth order accurate temporal discretization based on the Lax-Wendroﬀ type solvers [11, 17] makes a compromise between these two families of methods: It just takes a two-stage iteration for the fourth order accuracy by using second order accurate temporal-spatial coupled Lax-Wendroﬀ ﬂow solvers so half of reconstruction steps can be saved in comparison with the same accurate method and complicated successive diﬀerentiations of governing equations can be avoided, which could be further extended using the multi-derivative Runge-Kutta methods [17, 5, 33]. Moreover, we notice that the solution values on cell interfaces already available in the procedure of numerical ﬂux construction, called interface values in the present paper, can be used for the reconstruction procedure, thanks to the Lax-Wendroﬀ ﬂow solvers, which motivates

![image 1](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile1.png>)

This research is supported by NSFC with No 11371063.

1

us for such a study.

We develop a new ﬁfth order accurate Hermite WENO (HWENO) reconstruction in the framework of two-stage fourth order accurate temporal discretization [11]. The HWENO interpolation adopts two values: the average value of the solution and the corresponding averaged gradient value (the ﬁrst moment), as usual. The novelty is that the gradient values are directly approximated using the interface values when the Lax-Wendroﬀ type ﬂow solvers are used [1, 3, 18, 32], which is diﬀerent from the standard HWENO method in [21, 22, 14]. Technically, we can further adjust nonlinear weights during the HWENO reconstruction, just like the WENO-Z method [4] modifying the classical WENO-JS [8]. In doing so, the resulting scheme is much more compact and has several distinct features.

- (i) The scheme just uses half of the reconstruction steps, compared with the standard RK-WENO methods.
- (ii) The interface values are already available in the computation of numerical ﬂuxes and no extra eﬀorts are made on the gradient approximation.
- (iii) The interface values are approximated by using the GRP solver and thus they are strong solution values without taking account of possible discontinuities in trouble cells.
- (iv) A single HWENO reconstruction is more compact than the standard WENO reconstruction [8], as shown in other HWENO schemes [21, 22, 14].


This paper is organized as follows. In Section 2, we quickly review the two-stage method based on the Lax-Wendroﬀ ﬂow solvers and the HWENO reconstruction methods. In Section 3, we show the gradient approximation over each computational cell by using interface values of solutions. In Section 4, several numerical examples are displayed for the performance of such a HWENO reconstruction, by comparing with the WENO reconstruction with the same numerical ﬂux. A discussion is made in Section 5.

2. The two-stage fourth oder method and the Hermite WENO reconstruction

This section serves to present a quick review of the two-stage fourth order method based on the Lax-Wendroﬀ type ﬂow solvers in [11] and the HWENO reconstruction procedure, originally in [21]. Instead of independently computing the ﬁrst moment (the gradient of solution) in [21], we will construct it together with the solution average using the generalized Riemann problem (GRP) solver, which will be described in Setion 3.

- 2.1. Review of the two-stage fourth-order scheme. The two-stage fourth-order ﬁnite volume schemes based on the GRP solver was developed in [11]. Certainly, we can also use Men’shov’s modiﬁed GRP solver [15, 16] and the ADER solver [31, 32]. Both the acoustic and nonlinear versions of the GRP solver are provided in [3].


In this subsection, we quickly review this method by taking one-dimensional hyperbolic conservation laws,

- (2.1)

∂u ∂t

![image 2](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile2.png>)

+

∂f(u) ∂x

![image 3](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile3.png>)

= 0, x ∈ R, t > 0,

u(x, 0) = u0(x), x ∈ R, where u is a vector of conservative variables and f(u) is the associated ﬂux function vector. Given the computational mesh Ij = (xj−1

![image 4](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile4.png>)

2

, xj+1

![image 5](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile5.png>)

2

) with the size h = xj+1

![image 6](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile6.png>)

2

− xj−1

![image 7](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile7.png>)

2

for every j, we write (2.1) in form of the balance law,

- (2.2)

du¯j(t) dt

![image 8](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile8.png>)

= Lj(u) := −

1 h

![image 9](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile9.png>)

[f(u(xj+1

![image 10](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile10.png>)

2

, t)) − f(u(xj−1

![image 11](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile11.png>)

2

, t))], u¯j(t) =

1 h I

![image 12](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile12.png>)

j

u(x, t)dx,

where u(xj+1

![image 13](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile13.png>)

2

, t) is described in terms of GRP solver [3]. Then the two-stage approach for

- (2.1) is summarized as follows.


- Step 1. With the cell averages u¯nj and interface values uˆnj+1

![image 14](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile14.png>)

2

, reconstruct the data at tn as a piece-wise polynomial function u(x, tn) = un(x) by the HWENO interpolation that will be described below, and compute the corresponding GRP value (unj+1

![image 15](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile15.png>)

2

, (∂u/∂t)nj+1

![image 16](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile16.png>)

2

).

- Step 2. Compute the intermediate cell averages u¯n+ tn+

- 1

![image 17](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile17.png>)

- 2(x) and the interface values uˆn+ j+12 at


- 1

![image 18](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile18.png>)

- 2


![image 19](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile19.png>)

- 1

![image 20](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile20.png>)

- 2 = tn + k2 using the formulae,


![image 21](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile21.png>)

(2.3)

u¯n+

- 1

![image 22](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile22.png>)

- 2


j = u¯nj −

k 2h

![image 23](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile23.png>)

[fj∗+1

![image 24](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile24.png>)

2

− fj∗−1

![image 25](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile25.png>)

2

],

fj∗+1

![image 26](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile26.png>)

2

= f(unj+1

![image 27](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile27.png>)

2

) +

k 4

![image 28](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile28.png>)

∂f ∂u

![image 29](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile29.png>)

(unj+1

![image 30](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile30.png>)

2

)

∂u ∂t

![image 31](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile31.png>)

n

j+21

![image 32](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile32.png>)

,

uˆn+ j+21 = unj+1

- 1

![image 33](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile33.png>)

- 2


![image 34](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile34.png>)

![image 35](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile35.png>)

2

+

k 2

![image 36](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile36.png>)

∂u ∂t

![image 37](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile37.png>)

n

j+21

![image 38](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile38.png>)

.

where k is the time step size and

∂f ∂u

![image 39](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile39.png>)

is the Jacobian of f(u). At this intermediate stage, the HWENO interpolation is carried out once again with the values (u¯n+

- 1

![image 40](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile40.png>)

- 2


j , uˆn+

- 1

![image 41](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile41.png>)

- 2


j+21 ), to construct a piecewise polynomial un+ (un+

![image 42](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile42.png>)

- 1

![image 43](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile43.png>)

- 2(x) and ﬁnd the GRP value


- 1

![image 44](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile44.png>)

- 2


j+12 , (∂u/∂t)n+

![image 45](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile45.png>)

- 1

![image 46](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile46.png>)

- 2


j+12 ), as done in Step 1.

![image 47](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile47.png>)

- Step 3. Advance the solution to the next time level tn+1 = tn + k by


- (2.4)


k h

u¯nj+1 = u¯nj −

![image 48](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile48.png>)

fj4+th1

= f(unj+1

![image 49](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile49.png>)

![image 50](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile50.png>)

2

2

uˆnj++11

= unj+1

![image 51](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile51.png>)

![image 52](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile52.png>)

2

2

[fj4+th1

− fj4−th1

![image 53](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile53.png>)

![image 54](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile54.png>)

2

2

k

∂f ∂t

) +

![image 55](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile55.png>)

![image 56](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile56.png>)

- 2

1

![image 57](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile57.png>)

- 3


n+21 j+21

∂u ∂t

![image 58](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile58.png>)

+ k

,

![image 59](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile59.png>)

![image 60](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile60.png>)

],

- 2

![image 61](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile61.png>)

- 3


n

+

j+21

![image 62](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile62.png>)

∂f ∂t

![image 63](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile63.png>)

n+21 j+21

![image 64](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile64.png>)

![image 65](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile65.png>)

,

where the notations are

∂f ∂t

![image 66](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile66.png>)

∂f ∂u

n

(unj+1

=

)

![image 67](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile67.png>)

j+21

![image 68](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile68.png>)

2

![image 69](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile69.png>)

∂u ∂t

![image 70](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile70.png>)

n

,

j+21

![image 71](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile71.png>)

∂f ∂t

![image 72](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile72.png>)

n+21 j+12

∂f ∂u

- 1

![image 73](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile73.png>)

- 2


(un+ j+21 )

![image 74](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile74.png>)

=

![image 75](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile75.png>)

![image 76](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile76.png>)

![image 77](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile77.png>)

∂u ∂t

![image 78](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile78.png>)

n+12 j+12

![image 79](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile79.png>)

.

![image 80](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile80.png>)

The same procedure can be applied for two-dimensional cases. The details can be referred to [11].

Remark 2.1. For this two-stage fourth order temporal accuracy method, the HWENO reconstruction is invoked only twice instead of four times from tn to tn+1 = tn +k. In addition to save the computational cost, the size of stencils is automatically decreased.

- 2.2. A Hermite WENO Interpolation. In the approximation to a given function, there are two types of typical polynomial interpolations: the Lagrangian interpolation and the Hermite interpolation [24]. The former only uses the grid point values of the function, while the latter uses both the function value and its derivative value at the same grid point. It turns out that the latter uses half of grid points to derive the the polynomial approximations of the same degree to the given function compared to the former interpolation. So it is signiﬁcant to develop a HWENO reconstruction technology for high order accurate schemes of hyperbolic conservation laws, as done in [21], so that the resulting scheme becomes more compact even though the same ﬂux function approximation is adopted.


Let’s summarize the HWENO reconstruction in [21] for hyperbolic conservation laws in the ﬁnite volume framework although almost the same approach can be applied in the discontinuous Galerkin (DG) framework too [14]. Given the average u¯j and the derivative ∆uj of the function over the cell Ij,

- (2.5) u¯j =

1 h I

![image 81](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile81.png>)

j

u(x, t)dx, ∆uj =

1 h I

![image 82](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile82.png>)

j

∂u ∂x

![image 83](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile83.png>)

(x, t)dx,

we want to construct a polynomial p(x) such that uj+1

![image 84](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile84.png>)

2,− := p(xj+1

![image 85](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile85.png>)

2

) approximates the left limiting value of u(·, t) at x = xj+1

![image 86](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile86.png>)

2

. We choose three stencils

- (2.6) S(−1) = Ij−1 ∪ Ij, S(0) = Ij−1 ∪ Ij ∪ Ij+1, S(1) = Ij ∪ Ij+1.

On stencil S(0), u¯j−1, u¯j and u¯j+1 are used to construct a polynomial p(0) for the interpolation. Hence at xj+1

![image 87](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile87.png>)

2

, we have

- (2.7) u(0)j+1

![image 88](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile88.png>)

2,− := p(0)(xj+1

![image 89](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile89.png>)

2

) = −

1 6

![image 90](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile90.png>)

u¯j−1 +

- 5

![image 91](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile91.png>)

- 6


u¯j +

1 3

![image 92](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile92.png>)

u¯j+1.

Similarly, p(−1) and p(1) are constructed by using u¯j, u¯j−1, ∆uj−1 on S(−1) and by using u¯j, u¯j+1, ∆uj+1 on S(1), respectively,

- (2.8)


13 6

- 2h

![image 93](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile93.png>)

- 3


7 6

uj(−+1)1

2,− := p(−1)(xj+1

u¯j−1 +

u¯j −

∆uj−1,

) = −

![image 94](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile94.png>)

![image 95](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile95.png>)

![image 96](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile96.png>)

2

![image 97](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile97.png>)

- 5

![image 98](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile98.png>)

- 6


h 3

1 6

u(1)j+1

2,− := p(1)(xj+1

u¯j +

u¯j+1 −

∆uj+1.

) =

![image 99](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile99.png>)

![image 100](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile100.png>)

![image 101](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile101.png>)

2

![image 102](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile102.png>)

If the solution is smooth on the large stencil I−1 ∪ I0 ∪ I1, we have

- (2.9) u˜j+1

![image 103](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile103.png>)

2,− =

1 120

![image 104](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile104.png>)

(−23u¯j−1 + 76u¯j + 67u¯j+1 − 9h∆uj−1 − 21h∆uj+1). Thus the linear weights of the three stencils are

- (2.10) γ(−1) =

9 80

![image 105](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile105.png>)

, γ(0) =

29 80

![image 106](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile106.png>)

, γ(1) =

21 40

![image 107](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile107.png>)

, which ensure

u˜j+1

![image 108](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile108.png>)

2,− =

1

r=−1

γ(r)u(jr+)1

![image 109](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile109.png>)

2,−. The smoothness indicators are deﬁned by

- (2.11) β(r) =

2

l=1 Ij

h2l−1

dl dxl

![image 110](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile110.png>)

p(r)(x)

2

dx, r = −1, 0, 1,

in the same way as in the WENO reconstructions where p(r)(x) is the interpolation polynomial on stencil S(r). Their explicit expressions are

- (2.12)

β(−1) = (−2u¯j−1 + 2u¯j − h∆uj−1)2 +

13 3

![image 111](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile111.png>)

(−u¯j−1 + u¯j − h∆uj−1)2,

- β(0) =

1 4

![image 112](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile112.png>)

(−u¯j−1 + u¯j+1)2 +

13 12

![image 113](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile113.png>)

(−u¯j−1 + 2u¯j − u¯j+1)2,

- β(1) = (2u¯j+1 − 2u¯j − h∆uj+1)2 +


13 3

![image 114](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile114.png>)

(u¯j+1 − u¯j − h∆uj+1)2. Then we compute the nonlinear weights in the same way as the WENO-Z method does

- (2.13) ωrz =

αrz l αl

![image 115](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile115.png>)

, αrz = γ(r)(1 +

τz β(r) + ε

![image 116](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile116.png>)

), r = −1, 0, 1,

where ε is a small parameter in order to avoid a zero denominator and τz = |β(1) − β(−1)|. Finally we have

- (2.14) uj+1

![image 117](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile117.png>)

2,− =

1

r=−1

ωrzu(jr+)1

![image 118](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile118.png>)

2,−. The right interface value uj−1

![image 119](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile119.png>)

2,+ can be reconstructed in a similar way by mirroring the above procedure with respect to xj =

- 1

![image 120](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile120.png>)

- 2


(xj−1

![image 121](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile121.png>)

2

+ xj+1

![image 122](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile122.png>)

2

).

Since the GRP solver has to use the spatial derivative (∂u/∂x)j+1

![image 123](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile123.png>)

2,±, we approximate them using the interpolation,

- (2.15)


1 12h

∂u ∂x j+21,±

(u¯j−1 − 15u¯j + 15u¯j+1 − u¯j+2) .

:=

![image 124](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile124.png>)

![image 125](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile125.png>)

![image 126](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile126.png>)

The practical simulations later on indicate that the WENO-type stencil selection procedure in (2.15) can be avoided and the similar observation can be found in [23, 9].

In [21], the approaches for deriving ∆uj were proposed both for the DG method and the ﬁnite volume method. In the current study, we use the GRP solver to obtain it, without

extra manipulation of governing equations in Section 3.

3. Construction of gradients based on the GRP solver

It is already presented in the original GRP scheme [2, 3] using interface values for the gradient reconstruction. Now we want to apply the idea for the HWENO reconstruction procedure.

- 3.1. One-dimensional case. First we discuss the one-dimensional case. Over the computational cell Ij, we regard ∆uj as the average of the corresponding spatial derivative,


1 h I

1 h

∂u ∂x

- (3.1) ∆uj =


u(xj+1

(x, t)dx =

, t) , where the second equality is the Newton-Leibniz formula. Assume that the GRP values (unj+1

, t) − u(xj−1

![image 127](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile127.png>)

![image 128](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile128.png>)

![image 129](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile129.png>)

![image 130](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile130.png>)

![image 131](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile131.png>)

2

2

j

- 1

![image 132](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile132.png>)

- 2


1 2

j+21 , (∂u/∂t)n+

) and (un+

, (∂u/∂t)nj+1

![image 133](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile133.png>)

. Then we obtain the interface values for any time t ∈ (tn, tn+1). In particular, we have

j+12 ) are available around each grid point x = xj+1

![image 134](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile134.png>)

2

![image 135](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile135.png>)

![image 136](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile136.png>)

![image 137](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile137.png>)

![image 138](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile138.png>)

2

2

- (3.2) uˆn+ j+21 = unj+1

- 1

![image 139](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile139.png>)

- 2


![image 140](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile140.png>)

![image 141](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile141.png>)

2

+

k 2

![image 142](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile142.png>)

∂u ∂t

![image 143](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile143.png>)

n

j+21

![image 144](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile144.png>)

, uˆnj++11

![image 145](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile145.png>)

2

= unj+1

![image 146](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile146.png>)

2

+ k

∂u ∂t

![image 147](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile147.png>)

n+12 j+12

![image 148](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile148.png>)

![image 149](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile149.png>)

. It turns out that

- (3.3) ∆un+

- 1

![image 150](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile150.png>)

- 2


j =

1 h

![image 151](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile151.png>)

u ˆn+ j+21 − uˆn+

- 1

![image 152](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile152.png>)

- 2


![image 153](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile153.png>)

- 1

![image 154](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile154.png>)

- 2


j−21

![image 155](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile155.png>)

, ∆unj+1 =

1 h

![image 156](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile156.png>)

u ˆnj++11

![image 157](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile157.png>)

2

− uˆnj−+11

![image 158](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile158.png>)

2

. These values, together with the solution averages u¯n+

- 1

![image 159](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile159.png>)

- 2


j and u¯nj+1, are used in the HWENO reconstruction at the intermediate stage tn+

- 1

![image 160](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile160.png>)

- 2 and the ﬁnal time stage tn+1, respectively.


Now we analyze that such a construction has the desired accuracy. This is not obvious because the interface values uˆn+

- 1

![image 161](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile161.png>)

- 2


j+12 and uˆnj++11

![image 162](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile162.png>)

![image 163](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile163.png>)

2

bear truncation errors of lower orders compared with those of the cell averages. That is, uˆn+

- 1

![image 164](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile164.png>)

- 2


j+21 is ﬁrst order accurate since it is evaluated by the forward Euler evolution in (2.3) and uˆnj++11

![image 165](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile165.png>)

![image 166](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile166.png>)

2

is second order accurate with the mid-point rule in (2.4). One might wonder whether the reconstruction can still achieve the desired order of accuracy.

Recall that the fourth-order accurate numerical ﬂux is deﬁned as

- (3.4)


k2 2

n+21 j+21

∂u ∂t

1 3

∂f ∂u

∂f ∂u

∂u ∂t

- 2

![image 167](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile167.png>)

- 3


n

- 1

![image 168](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile168.png>)

- 2


(un+ j+21 )

![image 169](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile169.png>)

(unj+1

kfj4+th1

= kf(unj+1

) +

)

+

![image 170](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile170.png>)

![image 171](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile171.png>)

![image 172](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile172.png>)

![image 173](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile173.png>)

![image 174](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile174.png>)

![image 175](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile175.png>)

j+21

![image 176](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile176.png>)

![image 177](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile177.png>)

![image 178](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile178.png>)

![image 179](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile179.png>)

2

2

2

![image 180](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile180.png>)

![image 181](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile181.png>)

k2 2 −

n+21 j+21

1 3

∂f ∂u

∂f ∂u

- 2

![image 182](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile182.png>)

- 3


2 ∂u ∂x

2 ∂u ∂x

n

- 1

![image 183](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile183.png>)

- 2


(un+ j+21 )

![image 184](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile184.png>)

(unj+1

= kf(unj+1

−

) +

)

![image 185](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile185.png>)

![image 186](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile186.png>)

![image 187](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile187.png>)

![image 188](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile188.png>)

![image 189](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile189.png>)

![image 190](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile190.png>)

j+21

![image 191](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile191.png>)

![image 192](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile192.png>)

![image 193](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile193.png>)

2

2

![image 194](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile194.png>)

![image 195](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile195.png>)

tn+1

, t))dt + O(k5),

=

f(u(xj+1

![image 196](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile196.png>)

2

tn

- 1

![image 197](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile197.png>)

- 2


- 1

![image 198](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile198.png>)

- 2


) and (un+ j+21 , (∂u/∂x)n+

, (∂u/∂x)nj+1

where (unj+1

j+12 ) are the GRP values. This shows that the tolerance for the errors of unj+1

![image 199](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile199.png>)

![image 200](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile200.png>)

![image 201](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile201.png>)

![image 202](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile202.png>)

2

2

- 1

![image 203](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile203.png>)

- 2


is O(k4). And the tolerance for the errors of un+ j+21 ,

![image 204](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile204.png>)

![image 205](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile205.png>)

2

- 1

![image 206](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile206.png>)

- 2


and (∂u/∂x)n+

j+12 is O(k3). The Taylor expansion for uˆn+

(∂u/∂x)nj+1

![image 207](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile207.png>)

![image 208](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile208.png>)

2

- 1

![image 209](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile209.png>)

- 2


j+12 gives

![image 210](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile210.png>)

- (3.5) uˆn+ j+21 = unj+1

- 1

![image 211](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile211.png>)

- 2


![image 212](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile212.png>)

![image 213](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile213.png>)

2

+

k 2

![image 214](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile214.png>)

∂u ∂t

![image 215](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile215.png>)

n

j+21

![image 216](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile216.png>)

= u(xj+1

![image 217](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile217.png>)

2

, tn+

- 1

![image 218](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile218.png>)

- 2) −


k2 8

![image 219](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile219.png>)

∂2u ∂t2

![image 220](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile220.png>)

n

j+21

![image 221](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile221.png>)

+ O(k3).

By the deﬁnition of ∆un+

- 1

![image 222](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile222.png>)

- 2


j in (3.3), we have

- (3.6)

h∆un+

- 1

![image 223](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile223.png>)

- 2


j = uˆn+

- 1

![image 224](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile224.png>)

- 2


j+12 − uˆn+

![image 225](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile225.png>)

- 1

![image 226](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile226.png>)

- 2


j−12

![image 227](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile227.png>)

= u(xj+1

![image 228](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile228.png>)

2

, tn+

- 1

![image 229](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile229.png>)

- 2) − u(xj−1


![image 230](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile230.png>)

2

, tn+

- 1

![image 231](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile231.png>)

- 2) −


k2 8

![image 232](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile232.png>)

∂2u ∂t2

![image 233](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile233.png>)

n

j+12

![image 234](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile234.png>)

−

∂2u ∂t2

![image 235](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile235.png>)

n

j−21

![image 236](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile236.png>)

+ O(k4)

=

Ij

∂u ∂x

![image 237](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile237.png>)

(x, tn+

- 1

![image 238](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile238.png>)

- 2)dx −


k2h 8

![image 239](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile239.png>)

∂3u ∂t2∂x

![image 240](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile240.png>)

n

j−21

![image 241](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile241.png>)

+ O(k4).

Since h and k are proportional thanks to the CFL condition, h∆un+

- 1

![image 242](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile242.png>)

- 2


j bears the truncation error O(k3). Therefore un+

- 1

![image 243](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile243.png>)

- 2


j+21,± is approximated with error O(k3) in (2.9). Finally, since the Riemann solution un+

![image 244](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile244.png>)

1 2

![image 245](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile245.png>)

j+12 is calculated from the data un+

![image 246](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile246.png>)

- 1

![image 247](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile247.png>)

- 2


j+12,±, we conclude that it has the error O(k3).

![image 248](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile248.png>)

At the time step tn+1, it is obvious that the cell average u¯nj+1 has the error O(k5), as shown in [11]. As for the cell boundary values uˆnj++11

![image 249](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile249.png>)

2

, they are second order accurate thanks to the mid-point rule,

- (3.7) uˆnj++11

![image 250](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile250.png>)

2

= unj+1

![image 251](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile251.png>)

2

+ k

∂u ∂t

![image 252](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile252.png>)

n+12

![image 253](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile253.png>)

j+21

![image 254](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile254.png>)

= u(xj+1

![image 255](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile255.png>)

2

, tn+1) −

k3 24

![image 256](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile256.png>)

∂3u ∂t3

![image 257](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile257.png>)

n

j+21

![image 258](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile258.png>)

+ O(k4),

which further gives

- (3.8) h∆unj+1 =


n

k3h 24

∂4u ∂t3∂x

∂u ∂x

(x, tn+1)dx −

+ O(k5).

![image 259](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile259.png>)

![image 260](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile260.png>)

![image 261](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile261.png>)

j−21

Ij

![image 262](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile262.png>)

With the same arguement, we can show that h∆unj+1 bears an error O(k4). Therefore the Riemann solution unj++11

bears O(k4).

![image 263](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile263.png>)

2

1 2

With (2.15), we can show that (∂u/∂x)n+

2,± bear errors of orders O(k3) and O(k4), respectively, which meet the above requirement.

j+12,± and (∂u/∂x)nj+1

![image 264](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile264.png>)

![image 265](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile265.png>)

![image 266](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile266.png>)

3.2. Two-dimensional cases. In this subsection, we supress the dependence of u on the variable t to simplify the presentation. The gradient construction for two-dimensional cases can be treated similarly. Let ΩJ be a computational cell, with the boundary LJℓ, ℓ =

1, · · · , K. Then we use the Gauss theorem to have

- (3.9) ∇uJ :=

1 |ΩJ| ΩJ

![image 267](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile267.png>)

∇u(x, y)dxdy =

1 |ΩJ|

![image 268](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile268.png>)

K

ℓ=1 LJℓ

unJ

ℓ

dL,

where nJ

ℓ

is the unit outer normal of ΩJ on LJ

ℓ

. Therefore, once we know the interface values on LJ

ℓ

, we can approximate the gradient ∇uJ as

- (3.10) ∇uJ ≈

1 |ΩJ|

![image 269](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile269.png>)

K

ℓ=1

M

m

ωJ

ℓm

uˆJ

ℓm

nJ

ℓm|LJ

ℓ| =:

∆xuJ ∆yuJ

,

where uˆJ

ℓm

is the interface value at the Gauss point xJ

ℓm

on the interface LJ

ℓ

and ωJ

ℓm

is the corresponding Gauss weight.

Speciﬁed to the uniformly rectangular meshes ΩJ = Ωij = [xi−1

![image 270](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile270.png>)

2

, xi+1

![image 271](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile271.png>)

2

] × [yj−1

![image 272](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile272.png>)

2

, yj+1

![image 273](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile273.png>)

2

] for which hx = xi+1

![image 274](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile274.png>)

2

− xi−1

![image 275](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile275.png>)

2

and hy = yi+1

![image 276](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile276.png>)

2

− yi−1

![image 277](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile277.png>)

2

, there are two Gaussian quadrature points on each boundary of Ωij to achieve the ﬁfth order accuracy in space. For example we have (xi+1

![image 278](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile278.png>)

2

, yj

1

) and (xi+1

![image 279](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile279.png>)

2

, yj

2

) on x = xi+1

![image 280](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile280.png>)

2

for y ∈ [yj−1

![image 281](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile281.png>)

2

, yj+1

![image 282](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile282.png>)

2

], with yj

1

= 1+

√3

![image 283](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile283.png>)

![image 284](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile284.png>)

2 yj−1

![image 285](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile285.png>)

2

+ 1−

√3

![image 286](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile286.png>)

![image 287](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile287.png>)

2 yj+1

![image 288](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile288.png>)

2

and yj

2

= 1−

√3

![image 289](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile289.png>)

![image 290](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile290.png>)

2 yj−1

![image 291](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile291.png>)

2

+ 1+

√3

![image 292](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile292.png>)

![image 293](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile293.png>)

2 yj+1

![image 294](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile294.png>)

2

. The corresponding weights are taken as ω1 = ω2 = 21. As for the outer normals, we have

![image 295](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile295.png>)

- (3.11) ni±1

![image 296](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile296.png>)

2,jm = ±1

0

, ni

m,j±21

![image 297](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile297.png>)

=

0 ±1

, m = 1, 2.

It turns out that, by combining (3.10) and (3.11), the gradient ∇uij is approximated as

- (3.12)

∆xuij =

1 hx

![image 298](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile298.png>)

1 2

![image 299](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile299.png>)

(uˆi+1

![image 300](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile300.png>)

2,j1 + uˆi+1

![image 301](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile301.png>)

2,j2) −

- 1

![image 302](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile302.png>)

- 2


(uˆi−1

![image 303](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile303.png>)

2,j1 + uˆi−1

![image 304](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile304.png>)

2,j2) , ∆yuij =

1 hy

![image 305](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile305.png>)

- 1

![image 306](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile306.png>)

- 2


(uˆi

1,j+21 + uˆi

![image 307](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile307.png>)

2,j+21) −

![image 308](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile308.png>)

- 1

![image 309](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile309.png>)

- 2


(uˆi

1,j−21

![image 310](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile310.png>)

+ uˆi

2,j−21

![image 311](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile311.png>)

) ,

which are the componentwise expressions of (3.10) over the rectangular grids.

Now we need the limiting values of the solution u and its derivatives at each Gaussian quadrature point on the cell boundaries, i.e., ui

m,(j+21,±), (∂∂yu)i

![image 312](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile312.png>)

![image 313](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile313.png>)

m,(j+21,±), (∂∂xu)i

![image 314](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile314.png>)

![image 315](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile315.png>)

m,(j+21,±), u(i+1

![image 316](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile316.png>)

![image 317](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile317.png>)

2,±),jm, (∂∂xu)(i+1

![image 318](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile318.png>)

![image 319](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile319.png>)

2,±),jm and (∂∂yu)(i+1

![image 320](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile320.png>)

![image 321](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile321.png>)

2,±),jm for m = 1, 2. We adopt the dimension-by-dimension strategy conventionally used over rectangular grids [28] to interpolate them.

With (u¯ij, ∆xuij), we implement the HWENO reconstruction on u in the x-direction to obtain the line average of u over y ∈ [yj−1

![image 322](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile322.png>)

2

, yj+1

![image 323](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile323.png>)

2

] at xi

1

and xi

2

, i.e.,

- (3.13) u(xi


1 hy

![image 324](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile324.png>)

, ·)j :=

![image 325](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile325.png>)

m

yj+1 2

![image 326](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile326.png>)

u(xi

m

yj−1 2

![image 327](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile327.png>)

, y)dy, m = 1, 2.

Diﬀerent from the procedure for one-dimensional case in Subsection 2.2, we interpolate at the Gaussian quadrature points xi

and xi

instead of the boundaries. Thus the formulae

1

2

- (2.7) to (2.10) are modiﬁed correspondingly. Furthermore, we have
- (3.14) ∆u(xi


1 hy

(uˆi

m,j+21 − uˆi

, ·)j =

) m = 1, 2.

m,j−21

![image 328](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile328.png>)

m

![image 329](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile329.png>)

![image 330](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile330.png>)

![image 331](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile331.png>)

, ·))j) deﬁned in (3.13) and (3.14) to obtain u(xi

, ·)j, (∆yu(xi

, ·) with (u(xi

Finally, we implement the HWENO reconstruction for u(xi

m

m

m

2,±) and ∂∂yu(xi

, yj+1

, yj+1

2,±), which are just ui

![image 332](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile332.png>)

m

m

![image 333](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile333.png>)

![image 334](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile334.png>)

m,(j+21,±) and (∂∂yu)i

m,(j+21,±). As for the tangential derivatives (∂∂xu)i

![image 335](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile335.png>)

![image 336](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile336.png>)

![image 337](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile337.png>)

m,(j+21,±), implement the HWENO reconstruction on u with (u¯ij, ∆yuij) in the y-direction to obtain the line average of u over x ∈ [xi−1

![image 338](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile338.png>)

![image 339](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile339.png>)

] at yj+1

, xi+1

![image 340](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile340.png>)

![image 341](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile341.png>)

2

2

2,±, i.e.,

![image 342](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile342.png>)

i+21

1 hx

![image 343](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile343.png>)

![image 344](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile344.png>)

u(·, yj+1

2,±)dx. With u(·, yj+1

2,±)

:=

u(x, yj+1

![image 345](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile345.png>)

![image 346](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile346.png>)

![image 347](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile347.png>)

i

i−12

![image 348](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile348.png>)

![image 349](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile349.png>)

2,±) at xi

2,±)

already obtained above, we interpolate the derivatives of u(·, yj+1

![image 350](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile350.png>)

![image 351](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile351.png>)

i

as

1

- (3.15) ∂u


(xi

, yj+1

2,±)

![image 352](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile352.png>)

1

∂x

![image 353](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile353.png>)

√

√

1 108hx

![image 354](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile354.png>)

![image 355](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile355.png>)

![image 356](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile356.png>)

![image 357](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile357.png>)

3)u(·, yj+1

3)u(·, yj+1

2,±)

− (72 + 26

2,±)

(9 + 2

=

![image 358](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile358.png>)

i−2

i−1

![image 359](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile359.png>)

![image 360](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile360.png>)

+ (72 − 26√3)u(·, yj+1

− (9 − 2√3)u(·, yj+1

+48√3 u(·, yj+1

![image 361](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile361.png>)

![image 362](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile362.png>)

![image 363](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile363.png>)

![image 364](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile364.png>)

![image 365](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile365.png>)

![image 366](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile366.png>)

2,±)

2,±)

2,±)

,

i+1

i+2

![image 367](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile367.png>)

![image 368](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile368.png>)

![image 369](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile369.png>)

i

which is just (∂∂xu)i

1,(j+21,±), the tangential derivative of u at the Gaussian quadrature point (xi

![image 370](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile370.png>)

![image 371](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile371.png>)

2,±). We can obtain (∂∂xu)i

2,±). Similar interpolations are made for u(i+1

, yj+1

2,(j+21,±) by simply mirroring (3.15) with respect to (xi, yj+1

![image 372](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile372.png>)

1

![image 373](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile373.png>)

![image 374](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile374.png>)

![image 375](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile375.png>)

2,±),jm, (∂∂xu)(i+1

2,±),jm and (∂∂yu)(i+1

2,±),jm for m = 1, 2. The details are omitted.

![image 376](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile376.png>)

![image 377](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile377.png>)

![image 378](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile378.png>)

![image 379](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile379.png>)

![image 380](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile380.png>)

For system cases, the characteristic decomposition in [28] is adopted in the current study. All the reconstruction procedures described above are applied for the characteristic variables. The details are omitted here.

4. Numerical Examples

In this section, we provide several examples for one- and two-dimensional compressible Euler equations to verify the expected performance of this approach. The Euler equations can be found in any CFD books and we do not write out them here. Each example will be computed with the HWENO interpolation and the WENO interpolation in the same framework of two-stage fourth-order time discretization based the GRP solver [11]. Both the HWENO and the WENO reconstruction use the nonlinear weights in formulae (2.13). The resulting schemes are denoted as GRP4-HWENO5 and GRP4-WENO5, respectively. We emphasize again that the only diﬀerence is the data reconstruction. The CFL number

0.6 is used for all the computations except in the ﬁrst example.

- Example 1. Smooth initial value problem. We check the numerical results for a one-dimensional smooth initial value problem of the Euler equations with the initial data

(4.1) ρ(x, 0) = 1 + 0.2sin(πx), v(x, 0) = 1, p(x, 0) = 1,

to verify the numerical accuracy of the present approach where ρ is the density, v is the velocity, p is the pressure and u = [ρ, v, p]⊤. The periodic boundary conditions are used. The exact solution at time t is just a shift of the initial condition, i.e.

(4.2) u(x, t) = u(x − t, 0).

Here we set the CFL number to be 0.1 to show the numerical order of the spatial reconstructions. The errors shown in Table 1 are those of the cell averages of the density ρ at time t = 10.

Both reconstruction approaches achieve the designed numerical order while the errors of the scheme GRP4-HWENO5 is smaller than those of GRP4-WNEO5. And we can see that the the CPU time cost by both schemes are almost the same which veriﬁes our claim that no additional eﬀorts are made to obtain the ﬁrst moment of the solution.

Table 1. The L1, L∞ errors of the density and numerical orders for the smooth initial value problem in Example 1. The results are shown at time t = 10.

![image 381](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile381.png>)

![image 382](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile382.png>)

m GRP4-WENO5 GRP4-HWENO5 CPU time (s) L1 error Order L∞ error Order CPU time (s) L1 error Order L∞ error Order

![image 383](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile383.png>)

![image 384](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile384.png>)

![image 385](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile385.png>)

![image 386](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile386.png>)

![image 387](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile387.png>)

![image 388](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile388.png>)

![image 389](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile389.png>)

![image 390](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile390.png>)

![image 391](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile391.png>)

![image 392](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile392.png>)

![image 393](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile393.png>)

![image 394](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile394.png>)

![image 395](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile395.png>)

![image 396](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile396.png>)

![image 397](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile397.png>)

![image 398](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile398.png>)

![image 399](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile399.png>)

![image 400](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile400.png>)

![image 401](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile401.png>)

![image 402](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile402.png>)

40 0.31 6.25e-6 4.98 9.83e-6 4.99 0.41 1.50e-6 4.99 2.36e-6 5.02 80 1.25 1.96e-7 4.99 3.08e-7 5.00 1.46 4.69e-8 5.00 7.37e-8 5.00

![image 403](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile403.png>)

![image 404](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile404.png>)

![image 405](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile405.png>)

![image 406](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile406.png>)

![image 407](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile407.png>)

![image 408](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile408.png>)

![image 409](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile409.png>)

![image 410](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile410.png>)

![image 411](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile411.png>)

![image 412](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile412.png>)

![image 413](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile413.png>)

![image 414](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile414.png>)

![image 415](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile415.png>)

![image 416](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile416.png>)

![image 417](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile417.png>)

![image 418](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile418.png>)

![image 419](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile419.png>)

![image 420](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile420.png>)

![image 421](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile421.png>)

![image 422](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile422.png>)

![image 423](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile423.png>)

![image 424](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile424.png>)

![image 425](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile425.png>)

![image 426](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile426.png>)

160 5.14 6.13e-9 5.00 9.64e-9 5.00 4.95 1.47e-9 5.00 2.30e-9 5.00 320 19.77 1.92e-10 5.00 3.01e-10 5.00 19.61 4.59e-11 5.00 7.21e-11 5.00 640 122.38 5.99e-12 5.00 9.47e-12 4.99 117.23 1.43e-12 5.00 2.36e-12 4.93

![image 427](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile427.png>)

![image 428](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile428.png>)

![image 429](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile429.png>)

![image 430](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile430.png>)

![image 431](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile431.png>)

![image 432](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile432.png>)

![image 433](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile433.png>)

![image 434](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile434.png>)

![image 435](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile435.png>)

![image 436](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile436.png>)

![image 437](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile437.png>)

![image 438](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile438.png>)

![image 439](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile439.png>)

![image 440](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile440.png>)

![image 441](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile441.png>)

![image 442](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile442.png>)

![image 443](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile443.png>)

![image 444](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile444.png>)

![image 445](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile445.png>)

![image 446](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile446.png>)

![image 447](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile447.png>)

![image 448](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile448.png>)

![image 449](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile449.png>)

![image 450](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile450.png>)

![image 451](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile451.png>)

![image 452](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile452.png>)

![image 453](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile453.png>)

![image 454](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile454.png>)

![image 455](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile455.png>)

![image 456](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile456.png>)

![image 457](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile457.png>)

![image 458](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile458.png>)

![image 459](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile459.png>)

![image 460](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile460.png>)

![image 461](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile461.png>)

![image 462](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile462.png>)

- Example 2. The Titarev-Toro problem. This example was proposed in [30] as an extension of the Shu-Osher problem [26]. The initial data is taken as

- (4.3) (ρ, v, p)(x, 0) = 


 

(1.515695, 0.523346, 1.805), for x < −4.5, (1 + 0.1 sin(20πx), 0, 1), for x ≥ −4.5.

The output time is t = 5 and the numerical solutions computed with 1000 cells are shown in Figure 4.1. The reference solution is computed with 10000 cells. The scheme GRP4HWENO5 can catch the peaks and the troughs in the solution better.

- Example 3. Large pressure ratio problem. The large pressure ratio problem is a Riemann problem ﬁrst presented in [29]. In this problem, initially the pressure and density ratio between the two neighboring states are very high. The initial data is (ρ, v, p) = (10000, 0, 10000) for 0 ≤ x < 0.3 and (ρ, v, p) = (1, 0, 1) for 0.3 ≤ x ≤ 1.0. The boundary


1.7

1.7

1.65

1.6

1.6

| |
|---|
| |


1.5

1.55

| |
|---|
| |


1.4

1.5

Density

Density

1.45

1.3

1.4

1.2

1.35

1.1

1.3

- 0.9
- 1


|reference<br><br>GRP4-WENO5 GRP4-HWENO5<br><br>| |
|---|
|
|---|


|reference<br><br>GRP4-WENO5 GRP4-HWENO5<br><br>| |
|---|
|
|---|


1.25

1.2

-5 -4 -3 -2 -1 0 1 2 3 4 5

-2 -1.5 -1 -0.5 0 0.5 1 1.5 2

x

x

Figure 4.1. The comparison of the density proﬁle (left) and its local enlargement (right) for the Titarev-Toro problem in Example 2. The schemes used are GRP4-WENO5 (squares) and GRP4-HWENO5 (circles) with 1000 cells. The solid lines are the reference solution.

condition is dealt with in the same with that in the standard Riemann problem. The output time is t = 0.12.

An extremely strong rarefaction wave forms and it signiﬁcantly aﬀects the shock location in the numerical solution. Two factors determine the ability of a numerical scheme to properly capture the position of the shock. The ﬁrst one is whether the thermodynamical eﬀect is included in the numerical ﬂuxes properly [12]. The second one is the numerical dissipation of the schemes. Figure 4.2 shows the density proﬁle of the numerical solutions simulated by GRP4-WENO5 and GRP4-HWENO5 with 300 cells. We can see that GRP4-HWENO5 behaves better due to smaller stencils and less numerical dissipations of the resulting scheme.

- Example 4. The double Mach reﬂection problem. This is a standard test problem to display the performance of high resolution schemes. The computational domain for this problem is [0, 4] × [0, 1], and [0, 3] × [0, 1] is shown. The reﬂective wall lies at the bottom of the computaional domain starting from x = 61. Initially a right-moving Mach 10 shock is positioned at x = 61, y = 0 and makes a π3 angle with the x-axis. The results are shown in Figure 4.3 from which we can see that the numerical result by GRP4-HWENO5 can resolve more structures along the slip line than that by GRP4-WENO5.

![image 463](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile463.png>)

![image 464](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile464.png>)

![image 465](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile465.png>)

- Example 5. Two-dimensional Riemann problems. We provide an example of twodimensional Riemann problem taken from [6] involving the interactions of vortex sheets with rarefaction waves. The computation is implemented over the domain [0, 1] × [0, 1].


- 10 0
- 10 1
- 10 2
- 10 3
- 10 4


|exact<br><br>GRP4-WENO5 GRP4-HWENO5<br><br>| |
|---|
|
|---|


Density

|exact<br><br>GRP4-WENO5 GRP4-HWENO5<br><br>| |
|---|
|
|---|


- 0.83 0.84 0.85 0.86 0.87

Density

- 1

- 1.5
- 2

2.5

3

- 3.5
- 4

4.5

5

- 5.5




0 0.2 0.4 0.6 0.8 1

x

x

- Figure 4.2. The comparison of the density proﬁle (left) and its local enlargement (right) for the large pressure ration problem in Example 3. The schemes GRP4-WENO5 (squares) and GRP4-HWENO5 (circles) are performed with 300 cells. The solid lines refer to the exact solution.

0.5 1 1.5 2 2.5

y

0.1

0.2

0.3

0.4

0.5

0.6

0.7

0.8

0.9

0.5 1 1.5 2 2.5

y

0.1

0.2

0.3

0.4

0.5

0.6

0.7

0.8

0.9

- Figure 4.3. The density contours of the double Mach reﬂection problem in Example 4 by GRP4-WENO5 (upper) and the GRP4-HWENO5 (lower) with 960 × 240 cells.


 

- (4.4) (ρ, u, v, p)(x, y, 0) =




(1, 0.1, 0.1, 1), 0.5 < x < 1, 0.5 < y < 1, (0.5197, −0.6259, 0.1, 0.4), 0 < x < 0.5, 0.5 < y < 1, (0.8, 0.1, 0.1, 0.4), 0 < x < 0.5, 0 < y < 0.5, (0.5197, 0.1, −0.6259, 0.4), 0.5 < x < 1, 0 < y < 0.5.

The output time is 0.3.

The contours of the density and their local enlargements are shown in Figures 4.4. We can see that the scheme with the HWENO reconstruction can resolve more small structures along the vortex sheet.

0.9

0.55

0.8

0.7

0.5

0.6

0.45

0.5

0.4

0.4

0.3

0.35

0.2

0.1

0.3

0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9

0.3 0.35 0.4 0.45 0.5 0.55 0.6

0.9

0.55

0.8

0.7

0.5

0.6

0.45

0.5

0.4

0.4

0.3

0.35

0.2

0.1

0.3

0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9

0.3 0.35 0.4 0.45 0.5 0.55 0.6

Figure 4.4. The density contours of the 2-D Riemann problem in Example 5 computed with the schemes GRP4-WENO5 (upper) and GRP4-HWENO5 (lower), respectively. 700 × 700 cells are used.

5. Discussion

In this paper we developed a new HWENO reconstruction method just over structural (rectangular) meshes. This can be extended over unstructured meshes, but we think that the technicality may be nontrivial, which remains for future study.

A subtlety also lies in the reconstruction of spatial derivatives close to interfaces at the intermediate stage. If we would use the formulae below to interpolate the ﬁrst-order derivatives

as,

1 8h

∂u ∂x j−21,+

(−13u¯j−1 + 16u¯j − 3u¯j+1 − 3h∆uj−1 + h∆uj+1),

:=

![image 466](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile466.png>)

![image 467](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile467.png>)

- (5.1)


![image 468](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile468.png>)

∂u ∂x j+21,−

1 8h

(3u¯j−1 − 16u¯j + 13u¯j+1 + h∆uj−1 − 3h∆uj+1) ,

:=

![image 469](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile469.png>)

![image 470](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile470.png>)

![image 471](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile471.png>)

∂u ∂x j+21,±

would be O(k2) so that

the same analysis performed in Subsection 3.1 shows that the errors of

![image 472](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile472.png>)

![image 473](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile473.png>)

tn+1

1 k

fj4+th1

, t))dt + O(k3). This makes the resulting scheme third-order accurate.

f(u(xj+1

=

![image 474](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile474.png>)

![image 475](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile475.png>)

![image 476](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile476.png>)

2

2

tn

There is a remedy here. We could use the third order GRP solver in [19] , which is relatively complicated and we want to use an alternative method. Instead of the formulae in (5.1) to interpolate

n+12 j+21,±

∂u ∂x

![image 477](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile477.png>)

, we adopt

![image 478](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile478.png>)

![image 479](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile479.png>)

1 12h

∂u ∂x j+21,±

(u¯j−1 − 15u¯j + 15u¯j+1 − u¯j+2)

:=

(2.15)

![image 480](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile480.png>)

![image 481](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile481.png>)

![image 482](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile482.png>)

in practice. Although the stencil becomes larger, the numerical results in Section 4 show that such a choice has a good practical eﬀect.

References

- [1] M. Ben-Artzi and J. Falcovitz. A second-order Godunov-type scheme for compressible ﬂuid dynamics. J. Comput. Phys., 55:1–32, 1984.
- [2] M. Ben-Artzi and J. Falcovitz. Generalized Riemann Problems in Computational Fluid Dynamics. Cambridge University Press, Cambridge, 2003.
- [3] M. Ben-Artzi, J. Li, and G. Warnecke. A direct Eulerian GRP scheme for compressible ﬂuid ﬂows. J. Comput. Phys., 218:19–43, 2006.
- [4] R. Borges, M. Carmona, B. Costa, and W. Don. An improved weighted essentially non-oscillatory scheme for hyperbolic conservation laws. Journal of Computational Physics, 227:3191–3211, 2008.
- [5] A. Christlieb, S. Gottlieb, Z. Grant, and D. Seal. Explicit strong stability preserving multistage twoderivative time-stepping schemes. J. Sci. Comput., 68:914–942, 2016.
- [6] E. Han, J. Li, and H. Tang. Accuracy of the adaptive GRP scheme and the simulation of 2-D Riemann problem for compressible Euler equations. Commun. Comput. Phys., 10(3):577–606, 2011.
- [7] A. Harten, B. Engquist, S. Osher, and S. Chakravarthy. Uniformly high-order accurate essentially nonoscillatory schemes, III. J. Comput. Phys., 71(2):231–303, 1987.
- [8] G. Jiang and C.-W. Shu. Eﬃcient implementation of weighted ENO schemes. J. Comput. Phys., 126:202– 228, 1996.
- [9] Yan Jiang, Chi-Wang Shu, and Mengping Zhang. An alternative formulation of ﬁnite diﬀerence weighted ENO schemes with Lax-Wendroﬀ time discretization for hyperbolic conservation laws. SIAM Journal on Scientiﬁc Computing, 35(6):A1137–A1160, 2013.
- [10] P. Lax and B. Wendroﬀ. Systems of conservation laws. Comm. Pure Appl. Math., XIII:217–237, 1960.
- [11] J. Li and Z. Du. A two-stage fourth order temporal discretization for on the Lax-Wendroﬀ type ﬂow solvers, I. Hyperbolic conservation laes. SIAM, J. Sci. Comput., 38:A3046–A3069, 2016.


- [12] J. Li and Y. Wang. Thermodynamical eﬀects and high resolution methods for compressible ﬂuid ﬂows. J. Comput. Phys., 343:340–354, 2017.
- [13] X. D. Liu, S. Osher, and T. Chan. Weighted essentially non-oscillatory schemes. J. Comput. Phys., 115(1):200–212, 1994.
- [14] H. Luo, J. Baum, and Lo¨hner. A Hermite WENO-based limiter for DG methods on unstructured grids. J. Comput. Phys., 225(1):686–713, 2007.
- [15] I. S. Men’shov. Increasing the order of approximation of godunov’s scheme using the solution of the generalized riemann problem. U.S.S.R. Coumput. Math. Math. Phys., 30(5):54–65, 1990.
- [16] I. S. Men’shov. Generalized problem of break-up of a single discontinuity. J. Applied Mathematics and Mechanics, 55(1):86–95, 1991.
- [17] L. Pan, K. Xu, Q. Li, and J. Li. An eﬃcient and accurate two-stage fourth-order gas-kinetic scheme for the Euler and NavierStokes equations. J. Comput. Phys., 326:197–221, 2016.
- [18] K. Prendergast and K. Xu. Numerical hydrodynamics from gas-kinetic theory. J. Comput. Phys., 109:53– 66, 1993.
- [19] J. Qian, J. Li, and S. Wang. The generalized Riemann problems for compressible ﬂuid ﬂows: Towards high order. J. Comput. Phys., 259:358–389, 2014.
- [20] J. Qiu, M. Dumbser, and C.-W. Shu. The discontinuous galerkin method with lax-wendroﬀ type time discretizations. Computer Methods in Applied Mechanics and Engineering, 194:4528–4543, 2005.
- [21] J. Qiu and C.-W. Shu. Hermite WENO schemes and their application as limiters for Runge-Kutta discontinuous Galerkin method: one-dimensional case. J. Comput. Phys., 193:115–135, 2004.
- [22] J. Qiu and C.-W. Shu. Hermite WENO schemes and their application as limiters for Runge-Kutta discontinuous Galerkin method II: Two dimensional case. Comput. & Fluids, 34:642–663, 2005.
- [23] Jianxian Qiu and Chi-Wang Shu. Finite diﬀerence WENO schemes with Lax-Wendroﬀ-type time discretizations. SIAM Journal on Scientiﬁc Computing, 24(6):2185–2198, 2003.
- [24] A. Quarteroni, R. Sacco, and F. Saleri. Numerical Mathematics. Springer, 2007.
- [25] C.-W. Shu. High order WENO and DG methods for time-dependent convection-dominated PDEs: A brief survey of several recent developments. J. Comput. Phys., 316:598–613, 2016.
- [26] C.-W. Shu and S. Osher. Eﬃcient implementation of essentially nonoscillatory shock-capturing schemes, II. J. Comput. Phys., 83:32–78, 1989.
- [27] C.-W. Shu and Stanley Osher. Eﬃcient implementation of essentially non-oscillatory shock-capturing schemes. J. Comput. Phys., 77:439–471, 1988.
- [28] Chi-Wang Shu. High order ENO and WENO schemes. In T. J. Barth and H. Deconinck, editors, HighOrder Methods for Computational Physics, pages 439–582. Springer-Verlag, Berlin, 1999.
- [29] H. Tang and T. Liu. A note on the conservative schemes for the Euler equations. J. Comput. Phys., 218(1):451–459, 2006.
- [30] V. Titarev and E. Toro. Finite volume WENO schemes for three-dimensional conservation laws. J. Comput. Phys., 201:238–260, 2014.
- [31] E. F. Toro. Primitive, Conservative and Adaptive Schemes for Hyperbolic Conservation Laws, pages 323–385. Springer Netherlands, Dordrecht, 1998.
- [32] E. F. Toro and V. Titarev. Derivative Riemann solvers for systems of conservation laws and ADER methods. J. Comput. Phys., 212:150–165, 2006.
- [33] M. Okten¨ Turaci and Turgut Ozis.¨ Derivation of three-derivative runge-kutta methods. Numerical Algorithms, 74:247–265, 2017.


Zhifang Du: School of Mathematical Sciences, Beijing Normal University, 100875, P. R. China; Email: du@mail.bnu.edu.cn

Jiequan Li: Laboratory of Computational Physics, Institute of Applied Physics and Computational Mathematics, Beijing, P. R. China; Email: li jiequan@iapcm.ac.cn

![image 483](<2017-du-hermite-weno-reconstruction-fourth_images/imageFile483.png>)

