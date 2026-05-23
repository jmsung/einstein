arXiv:1801.00990v3[math.NA]12Jun2018

A two-stage fourth order time-accurate discretization for Lax–Wendroﬀ type ﬂow solvers II. High order numerical boundary conditions

Zhifang Dua, Jiequan Lib,c,∗

aSchool of Mathematical Sciences, Beijing Normal University, 100875, Beijing, P. R. China bLaboratory of Computational Physics, Institute of Applied Physics and Computational Mathematics, Beijing, P. R. China cCenter for Applied Physics and Technology, Peking University, Beijing, P. R. China

![image 1](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile1.png>)

Abstract

This paper serves to treat boundary conditions numerically with high order accuracy in order to suit the two-stage fourth-order ﬁnite volume schemes for hyperbolic problems developed in [J. Li and Z. Du, A two-stage fourth order time-accurate discretization Lax–Wendroﬀ type ﬂow solvers, I. Hyperbolic conservation laws, SIAM, J. Sci. Comput., 38 (2016), pp. A3046–A3069]. As such, it is signiﬁcant when capturing small scale structures near physical boundaries. Diﬀerent from previous contributions in literature, the current approach constructs a fourth order accurate approximation to boundary conditions by only using the Jacobian matrix of the ﬂux function (characteristic information) instead of its successive diﬀerentiation of governing equations leading to tensors of high ranks in the inverse Lax-Wendroﬀ method. Technically, data in several ghost cells are constructed with interpolation so that the interior scheme can be implemented over boundary cells, and theoretical boundary condition has to be modiﬁed properly at intermediate stages so as to make the two-stage scheme over boundary cells fully consistent with that over interior cells. This is nonintuitive and highlights the fact that theoretical boundary conditions are only prescribed for continuous partial diﬀerential equations (PDEs), while they must be approximated in a consistent way (even though they could be exactly valued) when the PDEs are discretized. Several numerical examples are provided to illustrate the performance of the current approach when dealing with general boundary conditions.

Keywords: Hyperbolic conservation laws, a two-stage fourth-order accurate scheme, Lax-Wendorﬀ type ﬂow solvers, fourth order numerical boundary conditions

![image 2](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile2.png>)

∗Corresponding author

Email addresses: du@mail.bnu.edu.cn (Zhifang Du), li_jiequan@iapcm.ac.cn (Jiequan Li)

Preprint submitted to Elsevier June 13, 2018

2010 MSC: 65M08, 76M12, 35L60, 35L65, 76N15

![image 3](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile3.png>)

- 1. Introduction


This study aims to develop high order accurate numerical approximations to theoretical boundary conditions suitable for the two-stage fourth-order accurate ﬁnite volume scheme based on the Lax–Wendroﬀ type ﬂow solvers in [14]. This scheme diﬀers from Runge–Kutta type schemes in the sense that second-order Lax–Wendroﬀ type ﬂow solvers [14, 17] are used to achieve fourth-order temporal accuracy through a two-stage temporal iteration. The numerical evidence shows that it is less computational consuming, less dissipative near discontinuities and more eﬀective to resolve physical and multi-dimensional eﬀects. Yet, the numerical boundary conditions have not been constructed correspondingly and in particular, the theoretical boundary data have to be modiﬁed at intermediate stages, analogous to other multi-stage methods [5, 18], through our detail analysis.

There are a large number of contributions to numerical boundary conditions for hyperbolic problems in literature and most of them are only ﬁrst- or second-order accurate. For example, second-order accurate ﬁnite diﬀerence approximations are constructed for the wave equation with Dirichlet or Neumann boundary conditions in [11, 12] from which our basic idea comes. As is wellknown, a second order wave equation is equivalent to a system of ﬁrst order hyperbolic equations. Therefore the similar idea applies to approximate (theoretical) boundary conditions of hyperbolic conservation laws in [19]. We brieﬂy illustrate their idea in the ﬁnite diﬀerence framework by considering the initial boundary value problem (IBVP) for a scalar conservation law



∂f(u) ∂x

∂u ∂t

+

= 0, x ∈ (0,1), t > 0,

![image 4](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile4.png>)

![image 5](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile5.png>)



u(x,0) = u0(x), x ∈ (0,1),

u(0,t) = g(t), t > 0.



(1)

Assume that f′(u) > 0 for all u ∈ R so that x = 0 is an inﬂow boundary and x = 1 is an outﬂow boundary. We equally distribute M + 1 points {xj = (j + 1/2)h : j = 0,1,...,M} in the computational domain (0,1), as shown in Figure 1. We use uj to denote the value of u at x = xj and suppress the index for the time levels. Obviously at the inﬂow boundary, the solution value at the

x = 1

x = 0

x

xM−1 xM xM+1

x−1 x0 x1

Figure 1: The computational domain (0, 1). Set x0 = h/2 and xM = 1 − h/2. Then x−1 = −h/2 and xM+1 = 1 + h/2 are ghost points.

ghost point x−1 is required in order to perform a second-order ﬁnite diﬀerence at x0. For this purpose, a polynomial is constructed in the region around the inﬂow boundary by using point-wise values u−1, u0 and u1,

L(x) = g−1(x)u−1 + g0(x)u0 + g1(x)u1, (2)

from which we want to ﬁnd the value u−1. The Lagrangian interpolation tells that

(x − x0)(x − x1) 2h2

,

g−1(x) =

![image 6](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile6.png>)

(3)

- g0(x) =

(x − x−1)(x − x1) −h2

![image 7](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile7.png>)

,

- g1(x) =


(x − x−1)(x − x0) 2h2

.

![image 8](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile8.png>)

Then u−1 can be obtained by solving the linear equation u(0,t) = L(0) where u(0,t) = g(t). At the outﬂow boundary x = 1, we simply use the extrapolation

uM+1 = 2uM − uM−1 (4)

to obtain the value uM+1 since the signal goes out of the computational domain at this end. Other works can be found e.g. in [4, 8, 7] on ﬁrst- and second-order accurate approaches for hyperbolic conservation laws in the ﬁnite volume framework and in [13] on the body ﬁtted boundary treatment for the discontinuous Galerkin (DG) methods.

In the present paper, we propose a fourth-order accurate boundary condition treatment in order to suit the two-stage fourth-order ﬁnite volume scheme developed in [14]. This boundary condition treatment can be regarded as a fourthorder extension of the methods developed in [11, 12, 19]. With the methodology described above, a polynomial is constructed near the boundary to interpolate the data in ghost cells with the information from both the interior cells and the boundary condition u(0,t) = g(t). In order to reduce the number of the interior cells used, ﬁrst-order spatial derivatives of the conservative variables are utilized in addition to their values at the boundary, for which we adopt the inverse Lax-Wendroﬀ (ILW) approach in [9, 20, 21, 15]. Recall that the original ILW method makes successive diﬀerentiation of the governing equations in order to calculate high order derivatives of the solution. A novelty of the current approach is that just ﬁrst order derivatives are used in the approximation and governing equations themselves are used only once in the process of the substitution of spatial derivatives by temporal derivatives. There is no need to make the complicated successive diﬀerentiation procedure.

Another novelty is about the treatment of theoretical boundary data when approximated as numerical boundary conditions. In analogy with other multistage methods [5, 18], the theoretical boundary data needs modifying properly at the intermediate stage for the two-stage approach in [14] so that fourth order accuracy is achieved. Otherwise, the direct input of the boundary data would lose accuracy by our detailed analysis. This seems quite counter-intuitive. However, this highlights the fact that theoretical boundary conditions are prescribed for continuous partial diﬀerential equations (PDEs). As the PDEs are discretized for numerical purposes, the boundary data should be properly approximated, instead that their exact values are directly input. In other words, the approximation of theoretical boundary data should be consistent with the discretization of the associated governing equations.

This paper is organized as follows. After the introduction section, we will have a brief review over the two-stage fourth-order scheme for hyperbolic conservation laws in Section 2. In Section 3, the basic idea and formulation are

explained using the one-dimensional scalar equation. The system case is shown in Section 4, with the speciﬁcation to the compressible Euler equations. Several numerical examples are shown in Section 5 to display the performance of the current numerical boundary condition treatment.

- 2. A review over the two-stage fourth-order scheme


In [14], we proposed a two-stage fourth order accurate temporal discretization based on Lax–Wendroﬀ type ﬂow solvers, particularly for hyperbolic conservation laws,

∂f(u) ∂x

∂u ∂t

+

= 0, x ∈ R,t > 0,

![image 9](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile9.png>)

![image 10](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile10.png>)

(5)

u(x,0) = u0(x), x ∈ R,

where u is a conservative variable and f(u) is the associated ﬂux function vector. Given a computational mesh Ij = (xj−1

, we write (5) in the semi-discrete form

,xj+1

) with the size h = xj+1

− xj−1

![image 11](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile11.png>)

![image 12](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile12.png>)

![image 13](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile13.png>)

![image 14](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile14.png>)

2

2

2

2

du¯j(t) dt

1 h

= Lj(u) := −

![image 15](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile15.png>)

![image 16](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile16.png>)

,t)) − f(u(xj−1

,t)) , (6)

f(u(xj+1

![image 17](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile17.png>)

![image 18](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile18.png>)

2

2

where u¯j(t) is the average of the solution u(x,t) over the control volume Ij,

1 h I

u¯j(t) =

![image 19](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile19.png>)

u(x,t)dt, (7)

j

,t) is the solution of (6) in a certain sense. Thanks to the Lax– Wendroﬀ ﬂow solvers, which is specialized as the GRP solver [3] in the current study, Lj(u) is well-deﬁned. We denote by tn = nk, n = 1,2,···, and by k the time increment. Then the two-stage approach for (5) is summarized as follows.

and u(xj+1

![image 20](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile20.png>)

2

- Step 1. With cell averages u¯nj and interface values uˆnj+1


at the time level t = tn, reconstruct the initial data as a piece-wise polynomial u(x,tn) = un(x) using the HWENO interpolation [6]. Then we compute instantaneous Riemann solutions unj+1

![image 21](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile21.png>)

2

and time derivatives (∂u/∂t)nj+1

using the GRP solver [3].

![image 22](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile22.png>)

![image 23](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile23.png>)

2

2

- Step 2. Compute intermediate cell averages u¯n+

- 1

![image 24](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile24.png>)

- 2


j and interface values uˆn+

- 1

![image 25](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile25.png>)

- 2


j+ 21 at tn+21 = tn + k2 using the following formulae,

![image 26](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile26.png>)

![image 27](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile27.png>)

![image 28](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile28.png>)

u¯n+

- 1

![image 29](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile29.png>)

- 2


j = u¯nj −

k 2h

![image 30](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile30.png>)

fj(1)+1

![image 31](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile31.png>)

2

− fj(1)−1

![image 32](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile32.png>)

2

,

fj(1)+1

![image 33](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile33.png>)

2

= f(unj+1

![image 34](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile34.png>)

2

) +

k 4

![image 35](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile35.png>)

∂f ∂u

![image 36](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile36.png>)

(unj+1

![image 37](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile37.png>)

2

)

∂u ∂t

![image 38](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile38.png>)

n

j+ 21

![image 39](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile39.png>)

,

uˆn+ j+21 = unj +

- 1

![image 40](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile40.png>)

- 2


![image 41](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile41.png>)

k 2

![image 42](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile42.png>)

∂u ∂t

![image 43](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile43.png>)

n

j+ 21

![image 44](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile44.png>)

,

(8)

where k is the time increment constrained by the CFL condition, and ∂f/∂u is the Jacobian matrix of f(u). With cell averages u¯n+

- 1

![image 45](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile45.png>)

- 2


j and interface values uˆn+

- 1

![image 46](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile46.png>)

- 2


j+21 , we use the HWENO interpolation again to construct a piece-wise polynomial un+12(x) and continue to ﬁnd Riemann solutions un+

![image 47](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile47.png>)

![image 48](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile48.png>)

- 1

![image 49](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile49.png>)

- 2


j+21 and time derivatives (∂u/∂t)n+

![image 50](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile50.png>)

- 1

![image 51](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile51.png>)

- 2


j+21 at the intermediate stage tn+

![image 52](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile52.png>)

- 1

![image 53](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile53.png>)

- 2 = tn + k2, as done in Step 1.


![image 54](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile54.png>)

- Step 3. Advance the solution to the next time level tn+1 = tn + k by


k h

u¯nj+1 = u¯nj −

![image 55](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile55.png>)

fj4+th1

= f(unj+1

![image 56](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile56.png>)

![image 57](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile57.png>)

2

2

uˆnj++11

= unj + k

![image 58](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile58.png>)

2

fj4+th1

− fj4−th1

![image 59](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile59.png>)

![image 60](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile60.png>)

2

2

,

k 2

) +

![image 61](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile61.png>)

∂u ∂t

![image 62](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile62.png>)

∂f ∂u

1 3

(unj+1

![image 63](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile63.png>)

![image 64](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile64.png>)

![image 65](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile65.png>)

2

n+ 12

![image 66](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile66.png>)

.

j+ 21

![image 67](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile67.png>)

∂u ∂t

- 2

![image 68](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile68.png>)

- 3


)nj+1

)(

+

![image 69](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile69.png>)

![image 70](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile70.png>)

2

∂u ∂t

∂f ∂u

- 1

![image 71](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile71.png>)

- 2


- 1

![image 72](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile72.png>)

- 2


(un+ j+21 )(

)n+ j+21 ,

![image 73](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile73.png>)

![image 74](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile74.png>)

![image 75](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile75.png>)

![image 76](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile76.png>)

(9)

- Remark 2.1. The HWENO reconstruction, based on the GRP solver, was developed in [6], to which is referred for details. In the smooth case, given cell averages u¯j and x-diﬀerences ∆uj of the solution,


1 hj I

1 h

1 h I

,t) − uˆ(xj−1

u¯j =

u ˆ(xj+1

,t) ,

ux(x,t)dx =

u(x,t)dx, ∆uj =

![image 77](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile77.png>)

![image 78](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile78.png>)

![image 79](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile79.png>)

![image 80](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile80.png>)

![image 81](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile81.png>)

2

2

j

j

(10) cell boundary values are reconstructed as

1 120

uj−1

2,− =

![image 82](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile82.png>)

![image 83](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile83.png>)

1 120

uj−1

2,+ =

![image 84](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile84.png>)

![image 85](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile85.png>)

(∂u/∂x)j−1

![image 86](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile86.png>)

(−23u¯j−2 + 76u¯j−1 + 67u¯j − 9h∆uj−2 − 21h∆uj),

(67u¯j−1 + 76u¯j − 23u¯j+1 + 21h∆uj−1 + 9h∆uj+1),

2,± =

1 12h

(u¯j−2 − 15u¯j−1 + 15u¯j − u¯j+1).

![image 87](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile87.png>)

(11)

In the presence of discontinuities, a WENO-type stencil selection is performed. Details can be found in [6].

- Remark 2.2. Riemann solutions unj+1

![image 88](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile88.png>)

2

, and time derivatives (∂u/∂t)nj+1

![image 89](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile89.png>)

2

in Step 1 are deﬁned as

unj+1

![image 90](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile90.png>)

2

= lim

t→tn+0

u(xj+1

![image 91](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile91.png>)

2

,t),

∂u ∂t

![image 92](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile92.png>)

n

j+ 21

![image 93](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile93.png>)

= lim

t→tn+0

∂u ∂t

![image 94](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile94.png>)

(xj+1

![image 95](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile95.png>)

2

,t) = lim

t→tn+0

−

∂f ∂u

![image 96](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile96.png>)

(u(xj+1

![image 97](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile97.png>)

2

,t))

∂u ∂x

![image 98](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile98.png>)

(xj+1

![image 99](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile99.png>)

2

,t).

(12) The last equality explains the Lax-Wendroﬀ methodology for which the governing equation (5) is employed. In practice, due to the singularity of the initial data un(x) at (xj+1

![image 100](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile100.png>)

2

,tn), the GRP solver is applied to resolve the singularity so that both values un+

- 1

![image 101](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile101.png>)

- 2


j+21 and (∂u/∂t)n+

![image 102](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile102.png>)

- 1

![image 103](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile103.png>)

- 2


j+21 are deﬁned.

![image 104](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile104.png>)

In [14], we did not touch the indispensable numerical boundary conditions. In the coming sections, we will present numerical boundary conditions suitable for the implementation of this two-stage scheme.

- 3. Numerical boundary condition treatment for one-dimensional scalar conservation laws


Let’s consider (5) in the computational domain (0,1) and assume that f(u) to be scalar f(u) = f(u) with f′(u) > 0 for all u ∈ R. Then x = 0 is an inﬂow boundary and x = 1 is an outﬂow boundary. Thus a boundary condition is required at x = 0. Denote by u(0,t) = g(t) the boundary condition for t > 0. The resulting initial boundary value problem (IBVP) can be formulated as in (1). The mesh {Ij = (xj−1

= jh,j = 0,1,...,M} is used in our computation. Notice that in order to place the left boundary at x = 0, our mesh is a little diﬀerent from Ij = ((j − 21)h,(j + 21)h) which is conventionally used in the ﬁnite volume context.

,xj+1

) : xj−1

![image 105](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile105.png>)

![image 106](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile106.png>)

![image 107](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile107.png>)

2

2

2

![image 108](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile108.png>)

![image 109](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile109.png>)

In computations, we need numerical boundary conditions at the inﬂow bound-

ary x = 0 corresponding to the boundary condition u(0,t) = g(t),t > 0. In this section, we will make the numerical treatment for inﬂow boundary conditions and present the modiﬁcation at intermediate stages. The WENO-type extrapolation is introduced to deal with outﬂow boundary conditions in the last part of this section, which is the same as that in [21].

- 3.1. Inﬂow boundary condition treatment As far as the IBVP (1) is concerned with, several values outside of the com-


putational domain are needed. For the present case, u¯−1, u¯−2, ∆u−1 and ∆u−2, deﬁned over I−1 = (−h,0) and I−2 = (−2h,−h) respectively, are needed in the reconstruction procedure (11) for the values indexed by j = 0 and j = 1. We call I−1 and I−2 ghost cells. In this subsection, we suppress all superscripts for the time levels.

First of all, assume the solution to be smooth near the boundary x = 0. To obtain the values mentioned above, a cubic polynomial,

p(x) = α3x3 + α2x2 + α1x + α0, (13)

is constructed over I−2 ∪ I−1 ∪ I0 ∪ I1 = (−2h,2h) to interpolate the solution u(x,tn) such that

1 h I

p(x)dx = u¯i, i = −2,−1,0,1. (14)

![image 110](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile110.png>)

i

Substitute the constraints (14) into (13) to determine the coeﬃcients α0, α1, α2 and α3 as

u¯1 − 3¯u0 + 3¯u−1 − u¯−2 6h3

u¯1 − u¯0 − u¯−1 + u¯−2 4h2

α3 =

, α2 =

,

![image 111](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile111.png>)

![image 112](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile112.png>)

−u¯1 + 15¯u0 − 15¯u−1 + u¯−2 12h

−u¯1 + 7¯u0 + 7¯u−1 − u¯−2 12

α1 =

, α0 =

,

![image 113](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile113.png>)

![image 114](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile114.png>)

(15)

in which u¯−1 and u¯−2 are yet to be determined and they are obtained by eval-

uating p(0) and p′(0) at the boundary x = 0,

1 12

(−u¯1 + 7¯u0 + 7¯u−1 − u¯−2) = g(t) + O(h4), p′(0) =

p(0) =

![image 115](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile115.png>)

1 12h

(−u¯1 + 15¯u0 − 15¯u−1 + u¯−2) = −f′(g(t))−1 g′(t) + O(h3).

![image 116](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile116.png>)

(16)

The ﬁrst equation results directly from the boundary condition u(0,t) = g(t) and the interpolation accuracy p(0) = u(0,t)+O(h4); the second one is obtained by using the inverse Lax-Wendroﬀ approach [20] that expresses the spatial variation through the temporal variation. The second equation in (16) is well-deﬁned by recalling that f′(u) > 0 is assumed for all u ∈ R at the beginning of this section. Solving (16) in terms of u¯−1 and u¯−2 yields (by ignoring high order terms)

- u¯−1 =

1 4

![image 117](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile117.png>)

(−6g + 6 h f′(g)−1 g′ + 11¯u0 − u¯1),

- u¯−2 =


1 4

(−90g + 42 h f′(g)−1 g′ + 105¯u0 − 11¯u1).

![image 118](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile118.png>)

(17)

Substituting (17) into (15), in turn, gives us the explicit expressions of αi, i = 0,...,3, and then the expression of p(x). Therefore we have (by ignoring high order terms)

- ∆u−1 =

p(0) − p(−h) h

![image 119](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile119.png>)

=

1 8h

![image 120](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile120.png>)

(66g − 34 h f′(g)−1 g′ − 73¯u0 + 7¯u1),

- ∆u−2 =


p(−h) − p(−2h) h

![image 121](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile121.png>)

1 8h

(294g − 118 h f′(g)−1 g′ − 331¯u0 + 37¯u1).

=

![image 122](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile122.png>)

(18)

The errors of the above approximations are of order O(h3) due to the accuracy of p(x). Thus (17) and (18) together provide the values in the ghost cells I−1 and I−2.

As there are discontinuities close to the inﬂow boundary, a WENO-type stencil selecting procedure can be applied. Assume that there is a discontinuity in either I0 or I1, we shorten the stencil cell by cell. Denote the stencils by

S(2) = {I−2,I−1,I0,I1}, S(1) = {I−2,I−1,I0}, S(0) = {I−2,I−1}. (19)

Denote by p(r)(x) the interpolation polynomial on S(r), r = 0,1,2, just as the polynomial p(x) constructed before. Then deﬁne

1 h I

1 h I

u¯(−r1) =

p(r)(x)dx, u¯−(r2) =

p(r)(x)dx,

![image 123](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile123.png>)

![image 124](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile124.png>)

(20)

−1

−2

1 h

1 h

∆u(−r1) =

(p(r)(0) − p(r)(−h)), ∆u−(r2) =

(p(r)(−h) − p(r)(−2h)).

![image 125](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile125.png>)

![image 126](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile126.png>)

The expressions of u¯(−r1), u¯(−r2), ∆u−(r1) and ∆u−(r2) for r = 0,1,2 will be listed in Appendix A.1.

The smoothness indicators are deﬁned in the same way as for the classical WENO interpolation,

r+1

h2l−1

β(r) =

l=1 I−1

dlp(r) dxl

![image 127](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile127.png>)

2

dx, r = 0,1,2, (21)

where p(r) is the interpolation polynomial of degree r + 1 on stencil S(r). Expressions of β(r) are put in Appendix A.2. With the Taylor expansion, we can express them at the boundary as

2

2

∂2u ∂x2

∂3u ∂x3

∂2u ∂x2

∂u ∂x

∂u ∂x

4 3

1 3

∂u ∂x

+ O(h5),

+ h4

β(2) = h2(

− h3

)

+

)

(

![image 128](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile128.png>)

![image 129](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile129.png>)

![image 130](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile130.png>)

![image 131](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile131.png>)

![image 132](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile132.png>)

![image 133](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile133.png>)

![image 134](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile134.png>)

![image 135](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile135.png>)

2

2

∂2u ∂x2

∂3u ∂x3

∂2u ∂x2

∂u ∂x

4 3

1 4

∂u ∂x

∂u ∂x

(22)

+ O(h5),

+ h4

− h3

β(1) = h2(

)

−

)

(

![image 136](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile136.png>)

![image 137](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile137.png>)

![image 138](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile138.png>)

![image 139](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile139.png>)

![image 140](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile140.png>)

![image 141](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile141.png>)

![image 142](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile142.png>)

![image 143](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile143.png>)

2

∂u ∂x

β(0) = h2(

)

,

![image 144](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile144.png>)

where ∂u/∂x, ∂2u/∂x2 and ∂3u/∂x3 are evaluated at x = 0. The linear weights of each stencil are

d(0) = h2, d(1) = h, d(2) = 1 − d(0) − d(1). (23) Then, we calculate the weights of the stencils by

Finally, we obtain

α(r) 2 l=0 α(l)

d(r) (ε + β(r))2

, ω(r) =

α(r) =

. (24)

![image 145](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile145.png>)

![image 146](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile146.png>)

2

u¯−1 =

r=0

∆u−1 =

2

ω(r)u¯−(r1), u¯−2 =

r=0

2

ω(r)∆u−(r1), ∆u−2 =

r=0

ω(r)u¯−(r2),

2

ω(r)∆u−(r2).

r=0

(25)

3.2. Inﬂow boundary condition treatment at intermediate stages

As pointed out by many researchers e.g., in [5, 18], the direct use of exact boundary conditions at intermediate stages in the process of multi-stage time discretizations will cause defects of the numerical accuracy. The same argument applies in the current study. We need to treat the boundary condition properly at the intermediate stage.

Our strategy is made as follows. We ﬁrst specify to the advancing formula

(9) for the two-stage fourth-order scheme in the leftmost control volume I0 as

k h

u¯n0+1 = u¯n0 −

![image 147](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile147.png>)

1 h

= u¯n0 −

![image 148](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile148.png>)

+

+

f41th

− f−4th1

![image 149](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile149.png>)

![image 150](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile150.png>)

2

2

k f(un1

) − f(un−1

)

![image 151](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile151.png>)

![image 152](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile152.png>)

2

2

k2 6

![image 153](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile153.png>)

k2 3

![image 154](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile154.png>)

∂u ∂t

f′(un1

)(

![image 155](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile155.png>)

![image 156](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile156.png>)

2

1 2

f′(un+

![image 157](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile157.png>)

- 1

![image 158](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile158.png>)

- 2


)(

)n1

− f′(un−1

![image 159](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile159.png>)

![image 160](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile160.png>)

2

2

∂u ∂t

)n−1

)(

![image 161](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile161.png>)

![image 162](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile162.png>)

2

∂u ∂t

- 1

![image 163](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile163.png>)

- 2


)n+

![image 164](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile164.png>)

- 1

![image 165](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile165.png>)

- 2


∂u ∂t

- 1

![image 166](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile166.png>)

- 2


− f′(un+ −21 )(

![image 167](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile167.png>)

![image 168](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile168.png>)

- 1

![image 169](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile169.png>)

- 2


)n+ −21 .

![image 170](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile170.png>)

(26)

Using the governing equation (5) to replace the temporal derivatives by the corresponding spatial ones, we obtain

1 h

u¯n0+1 = u¯n0 −

![image 171](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile171.png>)

−

k2 3

−

![image 172](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile172.png>)

k f(un1

) − f(un−1

)

![image 173](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile173.png>)

![image 174](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile174.png>)

2

2

k2 6

![image 175](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile175.png>)

(f′(un1

))2(

![image 176](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile176.png>)

2

- 1

![image 177](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile177.png>)

- 2


(f′(un+

- 1

![image 178](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile178.png>)

- 2


))2(

∂u ∂x

)n1

![image 179](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile179.png>)

∂u ∂x

)n−1

− (f′(un−1

))2(

![image 180](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile180.png>)

![image 181](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile181.png>)

![image 182](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile182.png>)

![image 183](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile183.png>)

2

2

2

∂u ∂x

1 2

)n+

![image 184](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile184.png>)

![image 185](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile185.png>)

- 1

![image 186](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile186.png>)

- 2


∂u ∂x

- 1

![image 187](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile187.png>)

- 2


− (f′(un+ −21 ))2(

![image 188](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile188.png>)

![image 189](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile189.png>)

- 1

![image 190](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile190.png>)

- 2


)n+ −21 .

![image 191](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile191.png>)

(27)

- 1

![image 192](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile192.png>)

- 2


- 1

![image 193](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile193.png>)

- 2


The diﬃculty results from the presence of (∂u/∂x)n+

and (∂u/∂x)n+

−21 evaluated at the intermediate stage t = tn+

- 1

![image 194](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile194.png>)

- 2


![image 195](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile195.png>)

- 1

![image 196](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile196.png>)

- 2. In fact, the interpolation are stated in


(11) and speciﬁed to this boundary control volume as,

∂u ∂x

![image 197](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile197.png>)

∂u ∂x

![image 198](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile198.png>)

n+ 12

1 12h

![image 199](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile199.png>)

- 1

![image 200](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile200.png>)

- 2


- 1

![image 201](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile201.png>)

- 2


- 1

![image 202](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile202.png>)

- 2


- 1

![image 203](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile203.png>)

- 2


(¯un+

−2 − 15¯un+

−1 + 15¯un+

0 − u¯n+

1 ),

=

![image 204](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile204.png>)

− 21

![image 205](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile205.png>)

n+ 12

1 12h

![image 206](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile206.png>)

- 1

![image 207](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile207.png>)

- 2


- 1

![image 208](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile208.png>)

- 2


- 1

![image 209](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile209.png>)

- 2


- 1

![image 210](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile210.png>)

- 2


−1 − 15¯un+

0 + 15¯un+

1 − u¯n+

(¯un+

2 ),

=

![image 211](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile211.png>)

- 1

![image 212](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile212.png>)

- 2


(28)

1 2

1 2

where u¯n+

−1 and u¯n+

![image 213](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile213.png>)

![image 214](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile214.png>)

−2 are determined in (17). Substituting (17) into (28) gives their direct reconstructions

∂u ∂x

![image 215](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile215.png>)

∂u ∂x

![image 216](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile216.png>)

n+ 21

![image 217](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile217.png>)

= −(f′(g(tn+12)))−1g′(tn+21 ),

![image 218](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile218.png>)

![image 219](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile219.png>)

− 21

![image 220](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile220.png>)

n+ 21

1 48h

![image 221](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile221.png>)

- 1

![image 222](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile222.png>)

- 2


- 1

![image 223](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile223.png>)

- 2


- 1

![image 224](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile224.png>)

- 2


0 + 59¯un+

1 − 4¯un+

−49¯un+

=

![image 225](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile225.png>)

2

- 1

![image 226](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile226.png>)

- 2


−6g(tn+12) + 6h(f′(g(tn+12)))−1g′(tn+21 ) .

![image 227](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile227.png>)

![image 228](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile228.png>)

![image 229](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile229.png>)

(29)

The errors in the above formulae come from two sources: the interpolation error and the truncation error carried by u¯n+

- 1

![image 230](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile230.png>)

- 2


- 1

![image 231](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile231.png>)

- 2


- 1

![image 232](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile232.png>)

- 2


0 , u¯n+

1 and u¯n+

2 within second-order accuracy. The latter one can be analyzed carefully as follows.

Recall the deﬁnition of the numerical ﬂux fj(1)+1

in (8),

![image 233](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile233.png>)

2

k 2

fj(1)+1

![image 234](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile234.png>)

![image 235](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile235.png>)

2

k2 8

∂f ∂t

k 2

f(unj+1

)nj+1

(

) +

=

![image 236](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile236.png>)

![image 237](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile237.png>)

![image 238](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile238.png>)

![image 239](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile239.png>)

![image 240](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile240.png>)

2

2

tn+21

![image 241](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile241.png>)

k3 48

=

,t))dt −

f(u(xj+1

![image 242](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile242.png>)

![image 243](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile243.png>)

2

tn

∂2f ∂t2

,tn) + O(k4).

(xj+1

![image 244](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile244.png>)

![image 245](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile245.png>)

2

(30)

- 1

![image 246](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile246.png>)

- 2


Then we ﬁnd that the intermediate value u¯n+

j in (29) bears the truncation error of order O(k3), compared to the exact solution, as

k 2h

- 1

![image 247](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile247.png>)

- 2


u¯n+

fj(1)+1

− fj(1)−1

j = u¯nj −

![image 248](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile248.png>)

![image 249](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile249.png>)

![image 250](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile250.png>)

2

2

tn+21

![image 251](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile251.png>)

k3 48

∂2f ∂t2

1 h

= u¯nj −

f(u(xj+1

,t))dt −

![image 252](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile252.png>)

![image 253](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile253.png>)

![image 254](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile254.png>)

![image 255](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile255.png>)

2

tn

tn+12

![image 256](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile256.png>)

k3 48

∂2f ∂t2

,t))dt +

−

f(u(xj−1

![image 257](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile257.png>)

![image 258](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile258.png>)

![image 259](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile259.png>)

2

tn

∂2f ∂t2

k3 48h

∂2f ∂t2

![image 260](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile260.png>)

= u(·,tn+21)j +

,tn) −

(xj+1

![image 261](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile261.png>)

![image 262](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile262.png>)

![image 263](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile263.png>)

![image 264](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile264.png>)

![image 265](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile265.png>)

2

,tn)

(xj+1

![image 266](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile266.png>)

2

,tn) + O(k5)

(xj−1

![image 267](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile267.png>)

2

,tn) + O(k4),

(xj−1

![image 268](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile268.png>)

2

where the diﬀerence in the bracket provides an O(h) term and

(31)

1 h I

![image 269](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile269.png>)

u(·,tn+12 )j =

![image 270](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile270.png>)

![image 271](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile271.png>)

- 1

![image 272](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile272.png>)

- 2)dx, j = 0,1,2.


u(x,tn+

j

For j = 0,1,2, we replace the diﬀerence quotients in (31) by the corresponding

diﬀerential quotients at x = 0 to further get

- 1

![image 273](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile273.png>)

- 2


![image 274](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile274.png>)

u¯n+

j = u(·,tn+21)j +

![image 275](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile275.png>)

![image 276](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile276.png>)

= u(·,tn+21)j −

![image 277](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile277.png>)

![image 278](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile278.png>)

= u(·,tn+21)j −

![image 279](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile279.png>)

![image 280](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile280.png>)

= u(·,tn+21)j −

![image 281](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile281.png>)

k3 48

∂3f ∂t2∂x

(0,tn) + O(k4)

![image 282](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile282.png>)

![image 283](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile283.png>)

k3 48

∂3u ∂t3

(0,tn) + O(k4)

![image 284](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile284.png>)

![image 285](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile285.png>)

k3 48

g′′′(tn) + O(k4)

![image 286](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile286.png>)

k3 48

- 1

![image 287](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile287.png>)

- 2) + O(k4),


g′′′(tn+

![image 288](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile288.png>)

(32)

where the second equality is derived by replacing the spatial derivative by the corresponding temporal derivative through the governing equation in (1). Substituting (32) into (29) gives us

∂u ∂x

![image 289](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile289.png>)

∂u ∂x

![image 290](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile290.png>)

n+ 21

∂u ∂x

![image 291](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile291.png>)

- 1

![image 292](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile292.png>)

- 2),


= −(f′(g(tn+12 )))−1g′(tn+21) =

,tn+

(x−1

![image 293](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile293.png>)

![image 294](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile294.png>)

![image 295](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile295.png>)

![image 296](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile296.png>)

2

− 21

![image 297](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile297.png>)

n+ 21

1 48h

![image 298](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile298.png>)

![image 299](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile299.png>)

![image 300](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile300.png>)

![image 301](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile301.png>)

− 49u(·,tn+12)0 + 59u(·,tn+12)1 − 4u(·,tn+12 )2 −6g(tn+12 ) + 6h(f′(g(tn+12)))−1g′(tn+21) −

=

![image 302](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile302.png>)

![image 303](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile303.png>)

![image 304](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile304.png>)

![image 305](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile305.png>)

1 2

![image 306](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile306.png>)

![image 307](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile307.png>)

![image 308](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile308.png>)

![image 309](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile309.png>)

6k3 48

- 1

![image 310](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile310.png>)

- 2) ,


g′′′(tn+

![image 311](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile311.png>)

6k3 48

1 48h

∂u ∂x

- 1

![image 312](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile312.png>)

- 2) + O(h3) −


- 1

![image 313](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile313.png>)

- 2).


,tn+

g′′′(tn+

=

(x1

![image 314](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile314.png>)

![image 315](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile315.png>)

![image 316](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile316.png>)

![image 317](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile317.png>)

2

(33)

The error O(h3) in the second equation in (33) comes from the interpolation approximation while

6k3 48

1 48h

- 1

![image 318](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile318.png>)

- 2 ) is induced from (32). It is easy to see


g′′′(tn+ that substituting (33) into (27) leads to

![image 319](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile319.png>)

![image 320](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile320.png>)

1 h I

u¯n0+1 =

![image 321](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile321.png>)

0

u(x,tn+1)dx + O(k3),

which means that the numerical scheme is only third-order accurate if the exact value of the boundary data is input directly in I0.

In order to restore the fourth-order accuracy of the two-stage fourth-order

scheme, we need to eliminate the O(k2) error in (33). For this purpose, we use

∂u ∂x

![image 322](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile322.png>)

∂u ∂x

![image 323](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile323.png>)

n+ 21

![image 324](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile324.png>)

= −(f′(g(tn+12 )))−1(g′)n+21,

![image 325](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile325.png>)

![image 326](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile326.png>)

− 21

![image 327](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile327.png>)

n+ 21

1 48h

![image 328](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile328.png>)

- 1

![image 329](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile329.png>)

- 2


- 1

![image 330](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile330.png>)

- 2


- 1

![image 331](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile331.png>)

- 2


0 + 59¯un+

1 − 4¯un+

−49¯un+

=

![image 332](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile332.png>)

2

- 1

![image 333](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile333.png>)

- 2


−6gn+21 + 6h(f′(g(tn+21)))−1(g′)n+12 ,

![image 334](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile334.png>)

![image 335](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile335.png>)

![image 336](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile336.png>)

(34)

- 1

![image 337](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile337.png>)

- 2


to reconstruct (∂u/∂x)n+

±12 instead of (29). Here the exact boundary values g(tn+12) and g′(tn+21 ) used in (29) are replaced by

![image 338](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile338.png>)

![image 339](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile339.png>)

![image 340](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile340.png>)

gn+12 = g(tn+21 ) + e(0)k3,

![image 341](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile341.png>)

![image 342](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile342.png>)

- 1

![image 343](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile343.png>)

- 2


(g′)n+

= g′(tn+21) + e(1)k2.

![image 344](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile344.png>)

(35)

- 1

![image 345](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile345.png>)

- 2


The terms e(0)k3 and e(1)k2 are introduced into gn+21 and (g′)n+

to cancel the truncation errors carried by u¯n+

![image 346](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile346.png>)

- 1

![image 347](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile347.png>)

- 2


1 2

1 2

0 , u¯n+

1 and u¯n+

![image 348](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile348.png>)

![image 349](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile349.png>)

2 and they are to be determined in the following. By combining (32), (34) and (35), we have

∂u ∂x

![image 350](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile350.png>)

n+ 21

![image 351](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile351.png>)

− 21

![image 352](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile352.png>)

1 2

= −(f′(g(tn+12)))−1(g′)n+

![image 353](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile353.png>)

![image 354](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile354.png>)

- 1

![image 355](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile355.png>)

- 2)))−1g′(tn+


- 1

![image 356](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile356.png>)

- 2) − (f′(g(tn+


- 1

![image 357](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile357.png>)

- 2)))−1e(1)k2


= −(f′(g(tn+

(36)

and

∂u ∂x

![image 358](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile358.png>)

n+ 12

![image 359](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile359.png>)

- 1

![image 360](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile360.png>)

- 2


∂u ∂x

- 1

![image 361](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile361.png>)

- 2)))−1e(1)k2,


- 1

![image 362](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile362.png>)

- 2 ) − (f′(g(tn+


,tn+

=

(x−1

![image 363](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile363.png>)

![image 364](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile364.png>)

2

1 48h

=

![image 365](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile365.png>)

- 1

![image 366](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile366.png>)

- 2


- 1

![image 367](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile367.png>)

- 2


- 1

![image 368](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile368.png>)

- 2


−49¯un+

0 + 59¯un+

1 − 4¯un+

2 −6gn+

- 1

![image 369](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile369.png>)

- 2


- 1

![image 370](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile370.png>)

- 2)))−1(g′)n+


- 1

![image 371](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile371.png>)

- 2 + 6h(f′(g(tn+


1 48h

=

![image 372](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile372.png>)

![image 373](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile373.png>)

![image 374](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile374.png>)

![image 375](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile375.png>)

−49u(·,tn+12)0 + 59u(·,tn+12)1 − 4u(·,tn+12 )2 −6g(tn+12) + 6h(f′(g(tn+12)))−1g′(tn+21 ) −

![image 376](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile376.png>)

![image 377](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile377.png>)

![image 378](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile378.png>)

![image 379](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile379.png>)

![image 380](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile380.png>)

![image 381](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile381.png>)

6 48

- 1

![image 382](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile382.png>)

- 2)))−1e(1)hk2 .


- 1

![image 383](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile383.png>)

- 2 ) − 6e(0)k3 + 6(f′(g(tn+


k3g′′′(tn+

![image 384](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile384.png>)

# (37)

This can be evaluated as

∂u ∂x

![image 385](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile385.png>)

n+ 12

![image 386](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile386.png>)

- 1

![image 387](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile387.png>)

- 2


∂u ∂x

- 1

![image 388](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile388.png>)

- 2) + O(h3)


,tn+

(x1

=

![image 389](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile389.png>)

![image 390](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile390.png>)

2

k3 48h

h k

6 48

- 1

![image 391](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile391.png>)

- 2 )))−1e(1)


- 1

![image 392](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile392.png>)

- 2) − 6e(0) + 6(f′(g(tn+


g′′′(tn+

+

−

![image 393](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile393.png>)

![image 394](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile394.png>)

![image 395](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile395.png>)

.

(38) In order to eliminate the O(k2) terms in both (36) and (38), we require

f′(g(tn+12))−1e(1) = 0,

![image 396](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile396.png>)

6 48

h k

- 1

![image 397](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile397.png>)

- 2)))−1e(1)


- 1

![image 398](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile398.png>)

- 2) − 6e(0) + 6(f′(g(tn+


g′′′(tn+

−

= 0.

![image 399](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile399.png>)

![image 400](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile400.png>)

(39)

Solving the above system of linear equations with respect to e(0) and e(1) provides

- e(0) = −

1 48

![image 401](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile401.png>)

g′′′(tn+

- 1

![image 402](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile402.png>)

- 2 ),


- e(1) = 0.


(40)

Therefore at the intermediate stage tn+12 , the boundary values used in numerical computations are modiﬁed as

![image 403](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile403.png>)

k3 48

- 1

![image 404](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile404.png>)

- 2 ),


gn+21 = g(tn+12 ) + e(0)k3 = g(tn+21) −

g′′′(tn+ (g′)n+

![image 405](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile405.png>)

![image 406](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile406.png>)

![image 407](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile407.png>)

![image 408](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile408.png>)

- 1

![image 409](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile409.png>)

- 2


- 1

![image 410](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile410.png>)

- 2 ).


= g′(tn+

(41)

Remark 3.1. The ﬁnal intermediate boundary values (41) are consistent with those given in [18] where the author indicates that the boundary values used at the intermediate stage should have the same truncation errors as those in the interior cells when multi-stage methods are used for initial and boundary value hyperbolic problems.

- 3.3. Outﬂow boundary condition treatment


For the initial and boundary problem (1), we set xM+1

= 1 as an outﬂow boundary, at which no boundary condition is required theoretically. However, we have to interpolate it to obtain the required values u¯M+1, u¯M+2, ∆uM+1

![image 411](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile411.png>)

2

and ∆uM+2 in ghost cells in order to implement the scheme. Since the signal propagates out of the computational domain through the boundary x = 1, the extrapolation can be used to construct the data in the ghost cells IM+1 and I,M+2. Here the extrapolation developed in [20] is brieﬂy summarized.

In order to achieve the fourth-order accuracy, a cubic polynomial is constructed by using u¯M−3, u¯M−2, u¯M−1 and u¯M, which is

u¯M − 3¯uM−1 + 3¯uM−2 − u¯M−3 6h3

(x − 1)3

q(x) =

![image 412](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile412.png>)

5¯uM − 13¯uM−1 + 11¯uM−2 − 3¯uM−3 4h2

(x − 1)2

+

![image 413](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile413.png>)

35¯uM − 69¯uM−1 + 45¯uM−2 − 11¯uM−3 12h

(x − 1)

+

![image 414](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile414.png>)

25¯uM − 23¯uM−1 + 13¯uM−2 − 3¯uM−3 12

.

+

![image 415](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile415.png>)

This gives the values

(42)

- u¯M+1 = 4¯uM − 6¯uM−1 + 4¯uM−2 − u¯M−3,
- u¯M+2 = 10¯uM − 20¯uM−1 + 15¯uM−2 − 4¯uM−3,


- ∆uM+1 =

26¯uM − 57¯uM−1 + 42¯uM−2 − 11¯uM−3 6

![image 416](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile416.png>)

,

- ∆uM+2 =


47¯uM − 114¯uM−1 + 93¯uM−2 − 26¯uM−3 6

.

![image 417](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile417.png>)

(43)

If there is a discontinuity in either IM−3, IM−2, IM−1 or IM, a WENO-type stencil selection can be applied. Details can be found in [21].

- 4. Numerical boundary condition treatment for hyperbolic systems


This section turns to investigate numerical treatment for boundary conditions of hyperbolic systems. We focus on hyperbolic conservation laws. As far

- as source terms are included, the corresponding extensions are automatically made. Systems of hyperbolic conservation laws in one dimension read


∂f(u) ∂x

∂u ∂t

+

= 0, (44)

![image 418](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile418.png>)

![image 419](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile419.png>)

where u has m components u = (u1,...,um)⊤, x ∈ (0,1) and t > 0, f(u) is the associated ﬂux vector function. In this section, all bold letters represent vectors. In contrast with the scalar case in Section 3, the case of systems is more complicated since inﬂow and outﬂow signals are coupled. The basic idea of numerical treatments originates from [19, 20]. Inﬂow signals and outﬂow signals are separated to be treated using the characteristic decomposition so that the technique of inﬂow and outﬂow boundary condition treatments in Section 3 can be applied, respectively. Denote by q(k) :=

∂kq ∂xk

the k-th order spatial derivative of a certain quantity q at the boundary, k = 0,1, and denote by

![image 420](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile420.png>)

∂f(u) ∂u

the Jacobian matrix of f(u). Assume that there are m real eigenvalues of

![image 421](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile421.png>)

∂f ∂u

(u(0))

![image 422](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile422.png>)

λ1 ≤ ··· ≤ λr ≤ 0 < λr+1 ≤ ··· ≤ λm, (45)

and a complete set of corresponding left eigenvectors Li(u(0)),

Li(u(0))⊤

∂f ∂u

(u(0)) = λiLi(u(0))⊤. (46)

![image 423](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile423.png>)

Thus there are m−r out-going signals from the boundary x = 0 and the number of boundary conditions should equal to the number of out-going characteristics, symbolically denoted as

Bi(u(0,t)) = ψi(t), i = r + 1,...,m. (47)

We refer to [10] for details. The similar boundary conditions can be imposed when the right boundary is considered.

In the following part of this section, we ﬁrst propose the general procedure for one-dimensional conservation systems and then specify to several examples, including the solid-wall boundary condition for the one-dimensional Euler equations, the subsonic inﬂow and the subsonic outﬂow boundary conditions involved in computations of the nuzzle ﬂow problem. In the last subsection, we extend our boundary condition treatment to the two-dimensional case by implementing it for the solid-wall boundary condition.

- 4.1. General framework for hyperbolic systems At ﬁrst, introduce characteristic variables


( ¯wi)j = Li · u¯j, i = 1,...,r, (48)

where u¯j is the cell average of u over the cell Ij. Theoretically, Li(u(0)) should be used here. However in practice, we can use Li(u¯0) in the expression (48) if Li(u(0)) is not available. Since w1,...,wr are out-going signals, the extrapolation technique in Subsection 3.3 is applied to obtain wi(0) and wi(1) for i = 1,...,r. For example, as the solution is smooth close to the boundary x = 0, similar to (42), an interpolation polynomial with respect to wi near x = 0 can be constructed which leads to

- wi(0) =

1 12

![image 424](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile424.png>)

− 25( ¯wi)0 + 23( ¯wi)1 − 13( ¯wi)2 + 3( ¯wi)3 ,

- wi(1) =


1 12h

![image 425](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile425.png>)

− 35( ¯wi)0 + 69( ¯wi)1 − 45( ¯wi)2 + 11( ¯wi)3 .

Then we solve the system

(49)



L1 · u(0) = w1(0),

. Lr · u(0) = wr(0), Br+1(u(0)) = ψ˜r+1,



(50)

. Bm(u(0)) = ψ˜m,



to obtain u(0) := u(0,t). Here wi(0) is obtained by (49). For i ∈ {r + 1,...,m}, ψ˜i is the modiﬁed boundary data deﬁned by ψ˜i = ψi(tn+12) −

k3 48

- 1

![image 426](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile426.png>)

- 2 ) at the intermediate stage t = tn+12 and ψ˜i = ψi(tn) at t = tn.


ψi′′′(tn+

![image 427](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile427.png>)

![image 428](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile428.png>)

![image 429](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile429.png>)

In order to derive u(1) := ∂u/∂x(0,t), we carry out the following manipulation. We take temporal derivatives on both sides of the boundary conditions in

(47) to yield

∇uBi(u(0))⊤

∂u ∂t

(0,t) = ψi′(t), i = r + 1,...,m. (51)

![image 430](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile430.png>)

Then the governing equations (44) are adopted to convert temporal derivatives to spatial ones as

∂f ∂u

∂u ∂x

(u(0))

∇uBi(u(0))⊤ −

(0,t) = ψi′(t), i = r + 1,...,m. (52) Furthermore, we have

![image 431](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile431.png>)

![image 432](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile432.png>)

Li · u(1) = wi(1), i = 1,...,r, (53) by taking spatial derivatives on both sides of the ﬁrst r equations in (50). Thus we derive the following linear system 

L1 · u(1) = w1(1),

. Lr · u(1) = wr(1), ∇uBr+1(u(0))⊤



(54)

∂f ∂u

(u(0)) u(1) = −ψr′+1,

![image 433](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile433.png>)

. ∇uBm(u(0))⊤

∂f ∂u

(u(0)) u(1) = −ψm′ ,



![image 434](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile434.png>)

with u(1) as the unknown and wi(1) deﬁned in (49).

After u(0) = [u(0)1 ,...,u(0)m ]⊤ and u(1) = [u(1)1 ,...,u(1)m ]⊤ are obtained by solving linear systems (50) and (54), for each pair u(0)i and u(1)i , i = 1,...,m, we construct polynomials p(ir) on stencils Si(r), r = 0,1,2, under the conditions p(ir)(0) = u(0)i and [p(ir)]′(0) = u(1)i , as in Subsection 3.1. Then (u¯i)−1, ( ¯ui)−2, (∆ui)−1 and (∆ui)−2 are deﬁned as in (25). Finally, we obtain





(u¯1)−1 . (u¯m)−1

u¯−1 =

 

 



(∆u1)−1 . (∆um)−1

∆u−1 =

 

for practical computations.



, u¯−2 =

 



, ∆u−2 =

 



(u¯1)−2 . (u¯m)−2

,

 





(∆u1)−2 . (∆um)−2

 

 

(55)

- 4.2. Solid-wall boundary condition for the one-dimensional Euler equations In this subsection, we will practically apply (50) and (54) for the solid-wall


boundary condition of the one-dimensional compressible Euler equations,

u = (ρ,ρv,ρE)⊤, f(u) = (ρv,ρv2 + p,v(ρE + p))⊤, (56)

1 2

v2 + e is the total energy with the internal energy e = e(p,ρ), which is given in terms of the equation of state (EOS). In this paper, we just consider the case of polytropic gases with e =

where ρ,v,p are the density, velocity and pressure, E =

![image 435](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile435.png>)

p (γ − 1)ρ

, γ > 1. Then the Jacobian matrix of the ﬂux function in terms of the conservative variables u takes

![image 436](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile436.png>)



∂f ∂u

=

![image 437](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile437.png>)

 

0 1 0 γ − 3 2

v2 (3 − γ)v γ − 1 γ − 2 2

![image 438](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile438.png>)

1 γ − 1

3 − 2γ 2

1 γ − 1

v3 −

vc2

v2 +

c2 γv

![image 439](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile439.png>)

![image 440](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile440.png>)

![image 441](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile441.png>)

![image 442](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile442.png>)



. (57)

 

![image 443](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile443.png>)

It has three eigenvalues λ1 = v − c, λ2 = v and λ3 = v + c, where c = γp/ρ is the sound speed. The corresponding left eigenvectors are

1 2c2

L1 =

![image 444](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile444.png>)

1 c2

L2 = −

![image 445](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile445.png>)

- 1

![image 446](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile446.png>)

- 2c2


L3 =

⊤

γ − 1 2

v2 + vc,−(γ − 1)v − c,γ − 1

,

![image 447](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile447.png>)

⊤

γ − 1 2

v2 − c2,−(γ − 1)v,γ − 1

,

![image 448](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile448.png>)

⊤

γ − 1 2

v2 − vc,−(γ − 1)v + c,γ − 1

.

![image 449](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile449.png>)

(58)

Assume that x = 0 is a solid wall, on which the ﬂow velocity is zero, v(0,t) = 0 which leads to

u2(0,t) = ρ(0,t)v(0,t) = 0. (59) So the system (50), when speciﬁed to the current case, is

 

L1 · u(0) = w1(0), L2 · u(0) = w2(0), w2(0) = 0.



(60)

The modiﬁcation term in (50) is zero for the present case since ψ takes a constant value at the boundary and therefore ψ′′′ is always zero.

Taking temporal derivatives on both sides of u(0)2 = 0 and converting temporal derivatives into spatial ones, we obtain

∂f ∂u

(u(0)) u(1)

0 = [0, 1, 0]

![image 450](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile450.png>)

γ − 3 2

(v(0))2, (3 − γ)v(0), γ − 1] u(1)

= [

![image 451](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile451.png>)

= [0, 0, γ − 1] u(1).

(61)

The last equality results from the boundary condition v(0) = 0. So (54) becomes, for this speciﬁc case,

 

L1 · u(1) = w1(1), L2 · u(1) = w2(1), [0, 0, γ − 1] u(1) = 0.

(62)



The numerical example with the solid-wall boundary condition is presented in Example 5 when dealing with the Woodward–Colella problem.

- 4.3. Inﬂow and outﬂow boundary conditions for the nozzle ﬂow The nozzle ﬂow is ubiquitous in gas dynamics. See [1] and references therein.


The nozzle ﬂow is an IBVP for the Euler equations with the geometry eﬀect resulting from the shape of the duct. The governing equations takes the form













Aρ Aρv AρE

Aρv A(ρv2 + p) Av(ρE + p)

0 A′p 0

∂ ∂x

∂ ∂t

+

=

, (63)

![image 452](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile452.png>)

![image 453](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile453.png>)

 

 

 

 

 

 

where A = A(x) is the sectional area of the duct. In Example 6 of the next section, the duct occupies the computational domain x ∈ (0,1). The ﬂuid ﬂows into the duct at x = 0 and ﬂows out of the duct at x = 1. Therefore three kinds of boundary conditions are involved in the computations and they are the subsonic inﬂow boundary condition, the subsonic outﬂow boundary condition

and the supersonic boundary condition. As for the supersonic out-going ﬂow

- at x = 1, we can simply extrapolate u by using the WENO-type extrapolation component-wise.


(I) Subsonic inﬂow boundary condition. As |v| < c at x = 0, the inﬂow is subsonic. That is, v − c < 0, v + c > v > 0 at x = 0. Then two boundary conditions are required at this end. In our computation, the inﬂow pressure and the inﬂow density are given as

(γ − 1) u3(0,t) −

u2(0,t)2 u1(0,t)

- 1

![image 454](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile454.png>)

- 2


= A(0)pin(t), u1(0,t) = A(0)ρin(t).

![image 455](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile455.png>)

(64)

These two equations and L1 · u(0) = w1(0) together meet the form of (50) specifically 

L1 · u(0) = w1(0),

2



u(0)2

- 1

![image 456](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile456.png>)

- 2


(65)

(γ − 1) u(0)3 −

= A(0)˜pin,

![image 457](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile457.png>)

u(0)1

u(0)1 = A(0)˜ρin,



where the notations are

- 1

![image 458](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile458.png>)

- 2 ) −


ρ˜in = ρin(tn+

k3 48

- 1

![image 459](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile459.png>)

- 2) −


- 1

![image 460](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile460.png>)

- 2), p˜in = pin(tn+


ρ′′′in(tn+

![image 461](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile461.png>)

- 1

![image 462](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile462.png>)

- 2 and


at the intermediate stage t = tn+

k3 48

- 1

![image 463](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile463.png>)

- 2),


p′′′in(tn+

![image 464](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile464.png>)

ρ˜in = ρin(tn), p˜in = pin(tn),

at t = tn.

In order to get u(1), we take temporal derivatives on both sides of (64) and obtain

1 2

1 γ − 1

(v(0))3 −

(c(0))2v(0), −(v(0))2 +

![image 465](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile465.png>)

![image 466](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile466.png>)

A(0)p′in γ − 1

− A′(0)p(0)v(0),

= −

![image 467](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile467.png>)

1 γ − 1

(c(0))2, v(0) u(1)

![image 468](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile468.png>)

(66)

[0, 1, 0] u(1) = −A(0)ρ′in.

The combination of them and L1 · u(1) = w1(1) possesses the structure of (54).

(II) Subsonic outﬂow boundary condition. At the exit of the nozzle x = 1, the out-going ﬂow is subsonic if v − c < 0 and v + c > v > 0. This means that only the characteristics associated with v−c are impinging onto the exit x = 1 from the exterior of the computational domain. Therefore just one boundary condition is prescribed theoretically at this end. In the conventional treatment, the outﬂow pressure at the exit is given, denoted by pex. So the boundary condition is

(γ − 1) u3(1,t) −

u2(1,t)2 u1(1,t)

- 1

![image 469](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile469.png>)

- 2


![image 470](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile470.png>)

= A(1)pex(t). (67)

The above equation together with L2 · u(0) = w2(0) and L3 · u(0) = w3(0) satisfy the form of (50) as

u(0)2 2 u(0)1



- 1

![image 471](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile471.png>)

- 2


(γ − 1) u(0)3 −

= A(1)˜pex,

![image 472](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile472.png>)



(68)

L2 · u(0) = w2(0), L3 · u(0) = w3(0),



k3 48

- 1

![image 473](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile473.png>)

- 2) at the intermediate stage t = tn+21 and


where p˜ex = pex(tn+12) −

p′′′ex(tn+ p˜ex = pex(tn) at t = tn.

![image 474](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile474.png>)

![image 475](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile475.png>)

![image 476](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile476.png>)

Once again, for the linear system of u(1), take temporal derivatives on both sides of (67) and convert temporal derivatives to spatial ones to get

1 2

(v(0))3 −

![image 477](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile477.png>)

1 γ − 1

(c(0))2v(0), −(v(0))2 +

![image 478](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile478.png>)

= −

1 γ − 1

(c(0))2, v(0) u(1)

![image 479](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile479.png>)

A(1)p′ex γ − 1

− A′(1)p(0)v(0).

![image 480](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile480.png>)

(69)

Then, we combine it with L2 ·u(1) = w2(1) and L3 · u(1) = w3(1) meet the form of

(54).

- 4.4. Solid-wall boundary condition for the two-dimensional Euler equations In this subsection, we show how this boundary condition treatment deals


with the solid-wall boundary condition of the two-dimensional Euler equations

∂f(u) ∂x

∂g(u) ∂y

∂u ∂t

= 0 (70) with

+

+

![image 481](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile481.png>)

![image 482](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile482.png>)

![image 483](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile483.png>)













ρvx ρ(vx)2 + p ρvxvy vx(ρE + p)

ρvy ρvxvy ρ(vy)2 + p vy(ρE + p)

ρ ρvx ρvy ρE

u =

f(u) =

g(u) =

,

 

 

 

 

 

 

(71) where ρ,(vx,vy),p are the density, velocity and pressure, E =

1 2

((vx)2+(vy)2)+ e is the total energy with the internal energy e =

![image 484](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile484.png>)

p ρ

1 γ − 1

for polytropic gases. Consider the computational domain Ω = {(x,y) : x > 0,y ∈ (ymin,ymax)} with a solid wall Γ = {(x,y) : x = 0,y ∈ (ymin,ymax)}. Here f is the ﬂux normal to Γ and its Jacobian matrix is

![image 485](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile485.png>)

![image 486](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile486.png>)





0 1 0 0 (γ − 1)H − (vx)2 − c2 (3 − γ)vx −(γ − 1)vy γ − 1 −vxvy vy vx 0 vy[(γ − 2)H − c2] H − (γ − 1)(vx)2 −(γ − 1)vxvy γvx

∂f ∂u

=

,

![image 487](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile487.png>)

 

 

(72) where c = γp/ρ is the sound speed and H = E +

(vx)2 + (vy)2 2

c2 γ − 1

p ρ

![image 488](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile488.png>)

=

+

![image 489](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile489.png>)

![image 490](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile490.png>)

![image 491](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile491.png>)

is the enthalpy. The Jacobian matrix ∂f/∂u has four eigenvalues λ1 = vx − c,

- λ2 = λ3 = vx and λ4 = vx + c and four associated left eigenvectors


γ − 1 2

1 2c2

((vx)2 + (vy)2) + vxc, −(γ − 1)vx − c, −(γ − 1)vy, γ − 1

Lx1 =

![image 492](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile492.png>)

![image 493](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile493.png>)

⊤

1 c2

γ − 1 2

((vx)2 + (vy)2) − c2, −(γ − 1)vx, −(γ − 1)vy, γ − 1

Lx2 = −

,

![image 494](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile494.png>)

![image 495](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile495.png>)

⊤

Lx3 = − vy, 0, 1, 0

,

⊤

,

- 1

![image 496](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile496.png>)

- 2c2


Lx4 =

⊤

γ − 1 2

((vx)2 + (vy)2) − vxc, −(γ − 1)vx + c, −(γ − 1)vy, γ − 1

. (73)

![image 497](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile497.png>)

Along the boundary Γ, we have the solid-wall boundary condition vx(0,y,t) =

0, which gives us u(0)2 = 0. Combining this with Lxi ·u(0) = wi(0), i = 1,2,3, will specify the system (50) of u(0) for the current case as



- Ly1 · u(0) = w1(0),
- Ly2 · u(0) = w2(0),
- Ly3 · u(0) = w3(0), u(0)2 = 0.




(74)



By taking temporal derivatives on both sides of u(0)2 = 0 and converting temporal derivatives to spatial ones, one obtains

∂f ∂u

(u(0))

[0, 1, 0, 0] −

![image 498](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile498.png>)

∂u ∂x

∂g ∂u

(u(0))

(0,y,t) −

![image 499](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile499.png>)

![image 500](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile500.png>)

∂u ∂y

(0,y,t) = 0, (75)

![image 501](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile501.png>)

and therefore

[0, 1, 0, 0]

∂f ∂u

(u(0)) u(1) = −[0, 0, 1, 0]

![image 502](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile502.png>)

∂g ∂u

(u(0))

![image 503](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile503.png>)

∂u ∂y

(0,y,t), (76)

![image 504](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile504.png>)

where the Jacobian matrix of g is





0 0 1 0 −vxvy vy vx 0

∂g ∂u

=

.

![image 505](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile505.png>)

(γ − 1)H − (vy)2 − c2 −(γ − 1)vx (3 − γ)vy γ − 1 vy[(γ − 2)H − c2] −(γ − 1)vxvy H − (γ − 1)(vy)2 γvy

 

 

(77) Then the right hand side of (76) is calculated as

∂g ∂u

∂u ∂y

(u(0))

−[0, 1, 0, 0]

(0,y,t)

![image 506](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile506.png>)

![image 507](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile507.png>)

∂u ∂y

= [(vx)(0)(vy)(0), −(vy)(0), −(vx)(0), 0]

(x,0,t)

![image 508](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile508.png>)

∂u1 ∂y

∂u2 ∂y

(0,y,t) − (vy)(0)

(0,y,t) − (vx)(0)

= (vx)(0)(vy)(0)

![image 509](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile509.png>)

![image 510](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile510.png>)

= 0.

∂u3 ∂y

(0,y,t)

![image 511](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile511.png>)

The last identity comes from the fact that (vx)(0) = 0 and

∂u2 ∂y

(0,y,t) = 0.

![image 512](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile512.png>)

Hence we combine (76) with Lyi · u(1) = wi(1), i = 1,2,3 to obtain 

- Ly1 · u(1) = w1(1),
- Ly2 · u(1) = w2(1),
- Ly3 · u(1) = w3(1), γ − 1




((vy)(0))2, 0, −(γ − 1)(vy)(0), γ − 1 u(1) = 0,

![image 513](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile513.png>)



2

which is the speciﬁc form of (54) in the present case.

(78)

The two-dimensional numerical examples with the solid-wall boundary condition are presented in Examples 7 and 8 in the next section when dealing with the double Mach reﬂection problem and the forward facing step problem.

- 5. Numerical examples


All examples displayed in this section are computed using the two-stage fourth-order scheme on Cartesian grids with the GRP solver [3] as the representative of the Lax–Wendroﬀ type ﬂow solvers. The ﬁfth order Hermite-type WENO reconstruction is used for the spatial reconstruction. We denote this scheme by GRP4-HWENO5.

- Example 1. Linear scalar equations with smooth solutions. We use a linear equation as the ﬁrst example to verify the accuracy order of the current boundary condition treatment. Consider the scalar IBVP (1) with the ﬂux f(u) = u. The initial and boundary conditions are u0(x) = sin(2πx) and g(t) = sin(−2πt), respectively. The setting of the initial data and the boundary condition allows the solution to be periodic. The inﬂow and outﬂow boundary condition treatments are applied at x = 0 and x = 1, respectively.


The CFL number is set to be 0.4. The computation stops at t = 5. The numerical errors and orders are shown in Table 1, which conﬁrms that the computation attains the expected order of accuracy.

Table 1: The numerical errors and orders of the linear scalar equation in Example 1.

![image 514](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile514.png>)

![image 515](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile515.png>)

![image 516](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile516.png>)

![image 517](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile517.png>)

![image 518](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile518.png>)

![image 519](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile519.png>)

![image 520](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile520.png>)

m L1 error order L∞ error order

![image 521](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile521.png>)

![image 522](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile522.png>)

![image 523](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile523.png>)

![image 524](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile524.png>)

![image 525](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile525.png>)

![image 526](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile526.png>)

![image 527](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile527.png>)

40 4.97e-07 4.32 1.75e-06 4.95 80 2.85e-08 4.13 8.64e-08 4.34

![image 528](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile528.png>)

![image 529](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile529.png>)

![image 530](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile530.png>)

![image 531](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile531.png>)

![image 532](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile532.png>)

![image 533](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile533.png>)

![image 534](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile534.png>)

![image 535](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile535.png>)

![image 536](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile536.png>)

![image 537](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile537.png>)

![image 538](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile538.png>)

![image 539](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile539.png>)

160 1.76e-09 4.02 5.66e-09 3.93 320 1.10e-10 4.00 3.60e-10 3.98 640 6.86e-12 4.00 2.27e-11 3.99

![image 540](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile540.png>)

![image 541](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile541.png>)

![image 542](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile542.png>)

![image 543](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile543.png>)

![image 544](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile544.png>)

![image 545](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile545.png>)

![image 546](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile546.png>)

![image 547](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile547.png>)

![image 548](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile548.png>)

![image 549](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile549.png>)

![image 550](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile550.png>)

![image 551](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile551.png>)

![image 552](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile552.png>)

- Example 2. Nonlinear scalar equations. This example purposes to see the accuracy order for nonlinear equations. Consider the scalar IBVP (1) with the ﬂux f(u) = u2/2 and the initial value u0(x) = 0.5 + 0.25 sin(2πx). The boundary condition g(t) is given to be consistent with the initial value problem in which the initial data is periodically extend to x ∈ R. At x = 0, there are no explicit expressions available for g(t) and its derivatives because of the nonlinearity. However, the point-wise values of g could be obtained through the characteristic method and g′′′(t) used in (41) can be approximated by

g′′′(t) =

- 1

![image 553](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile553.png>)

- 2τ3


− 5g(t) + 18g(t + τ) − 24g(t + 2τ)

+14g(t + 3τ) − 3g(t + 4τ) ,

(79)

where τ is proportional to the time step k. For example, we set τ =

k 10

![image 554](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile554.png>)

in our computations.

The CFL number is set to be 0.4. The computation stops at t = 1/3π. For this example, x = 0 is always an inﬂow boundary while x = 1 is always an outﬂow boundary. Therefore the inﬂow and outﬂow boundary condition treatments are applied at x = 0 and x = 1, respectively. The numerical errors and accuracy orders in Table 2 shows that the computation reaches the expected order of accuracy.

- Example 3. Scalar advection equations with discontinuous solutions. In this example, we verify the capability of our boundary condition treatment


Table 2: The numerical errors and orders of the Burgers equation in Example 2.

![image 555](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile555.png>)

![image 556](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile556.png>)

![image 557](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile557.png>)

![image 558](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile558.png>)

![image 559](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile559.png>)

![image 560](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile560.png>)

![image 561](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile561.png>)

m L1 error order L∞ error order

![image 562](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile562.png>)

![image 563](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile563.png>)

![image 564](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile564.png>)

![image 565](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile565.png>)

![image 566](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile566.png>)

![image 567](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile567.png>)

![image 568](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile568.png>)

40 6.00e-06 5.15 4.27e-05 4.07 80 1.49e-07 5.33 9.84e-07 5.44

![image 569](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile569.png>)

![image 570](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile570.png>)

![image 571](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile571.png>)

![image 572](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile572.png>)

![image 573](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile573.png>)

![image 574](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile574.png>)

![image 575](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile575.png>)

![image 576](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile576.png>)

![image 577](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile577.png>)

![image 578](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile578.png>)

![image 579](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile579.png>)

![image 580](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile580.png>)

160 7.63e-09 4.29 4.25e-08 4.53 320 4.77e-10 4.00 2.51e-09 4.09 640 2.95e-11 4.01 1.61e-10 3.96

![image 581](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile581.png>)

![image 582](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile582.png>)

![image 583](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile583.png>)

![image 584](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile584.png>)

![image 585](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile585.png>)

![image 586](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile586.png>)

![image 587](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile587.png>)

![image 588](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile588.png>)

![image 589](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile589.png>)

![image 590](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile590.png>)

![image 591](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile591.png>)

![image 592](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile592.png>)

![image 593](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile593.png>)

to deal with the discontinuous boundary condition. The same example with similar initial and boundary conditions was used in [20] for the same purpose. Consider the IBVP (1) with the ﬂux to be linear, f(u) = u. The initial data is u0(x) = sin(4πx) and the boundary data is taken as

 

sin(−4πt), t < 0.25, 0, 0.25 < t < 0.5, 3, t > 0.5.

g(t) =

(80)



The inﬂow and outﬂow boundary condition treatments are applied at x = 0 and x = 1, respectively. We compare the result in the domain (0,1) with the exact one in Figure 2. The numerical solution matches the exact solution represented by the solid line perfectly.

- Example 4. Linear systems, Consider the linearized Euler equations




∂ ∂t

![image 594](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile594.png>)

 





ρˆ vˆ pˆ

+

 

 

v¯ ρ¯ 0 0 v¯ 1/ρ¯ 0 γp¯ v¯





∂ ∂x

![image 595](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile595.png>)

 

 



ρˆ vˆ pˆ

= 0, x ∈ (0,2), t > 0 (81)

 

with the background state (¯ρ,v,¯ p¯) and the perturbation (ˆρ,v,ˆ pˆ), where γ = 1.4 is the speciﬁc heat ratio. The eigenvalues of A¯ are λ1 = v¯ − c¯, λ2 = v¯ and

- λ3 = v¯ + c¯ with c¯2 = γp/¯ ρ¯. In this example, we set ρ¯ = 1.4, v¯ = 1 and p¯ = 4, which makes λ1 < 0 < λ2 < λ3. Therefore subsonic inﬂow and subsonic outﬂow boundary conditions are prescribed at x = 0 and x = 2, respectively.


|exact solution<br><br>GRP4-HWENO5 with the present boundary treatment|
|---|


u

- 0

- 0.5
- 1

1.5

2

- 2.5
- 3




- -1
- -0.5


0 0.5 1 1.5 2 2.5 3 3.5 4

x

- Figure 2: The discontinuous solution in Example 3 with 80 computational cells (circles). The exact solution is shown as a solid curve.


This example is designed to allow the solution to be a combination of three sine waves carried by the three characteristics, i.e.







- α1 sin(k1π(x − (¯v − c¯)t))
- α2 sin(k2π(x − vt¯ ))
- α3 sin(k3π(x − (¯v + c¯)t))


ρˆ(x,t) vˆ(x,t) pˆ(x,t)

= R1,R2,R3

 

 

 

where ki and αi, i = 1,2,3 are parameters, and



, (82)

 

R1 = 1, −

c¯ ρ¯

, c¯2

![image 596](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile596.png>)

⊤

, R2 = 1, 0, 0

⊤

, R3 = 1,

c¯ ρ¯

, c¯2

![image 597](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile597.png>)

⊤

. (83)

For example, we set k1 = 1, k2 = 3, k3 = 2, α1 = 0.1, α2 = −0.1 and α3 = 0.08. Following the instruction of the ﬂuid dynamics [16], the inﬂow density ρin(t) = ρˆ(0,t) and pressure pin(t) = pˆ(0,t) are given at x = 0 and the outﬂow pressure pex(t) = pˆ(2,t) is given at x = 2. The initial condition is deﬁned by setting t = 0.

In the computation, subsonic inﬂow and subsonic outﬂow boundary condition treatments are applied at x = 0 and x = 2, respectively. The CFL condition is 0.4 and the output time is t = 10. Table 3 shows the numerical errors and orders.

Table 3: The numerical errors and orders of the linear system in Example 4.

![image 598](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile598.png>)

![image 599](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile599.png>)

![image 600](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile600.png>)

![image 601](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile601.png>)

![image 602](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile602.png>)

![image 603](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile603.png>)

![image 604](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile604.png>)

m L1 error order L∞ error order

![image 605](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile605.png>)

![image 606](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile606.png>)

![image 607](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile607.png>)

![image 608](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile608.png>)

![image 609](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile609.png>)

![image 610](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile610.png>)

![image 611](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile611.png>)

40 1.87e-2 -0.12 2.11e-2 0.06 80 8.18e-4 4.52 1.01e-3 4.39

![image 612](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile612.png>)

![image 613](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile613.png>)

![image 614](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile614.png>)

![image 615](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile615.png>)

![image 616](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile616.png>)

![image 617](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile617.png>)

![image 618](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile618.png>)

![image 619](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile619.png>)

![image 620](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile620.png>)

![image 621](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile621.png>)

![image 622](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile622.png>)

![image 623](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile623.png>)

160 4.08e-5 4.33 4.54e-5 4.47 320 2.79e-6 3.87 3.04e-6 3.90 640 1.78e-7 3.97 1.89e-7 4.00

![image 624](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile624.png>)

![image 625](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile625.png>)

![image 626](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile626.png>)

![image 627](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile627.png>)

![image 628](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile628.png>)

![image 629](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile629.png>)

![image 630](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile630.png>)

![image 631](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile631.png>)

![image 632](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile632.png>)

![image 633](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile633.png>)

![image 634](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile634.png>)

![image 635](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile635.png>)

![image 636](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile636.png>)

- Example 5. The Woodward–Colella problem. This classical example assumes that initially the gas is at rest and ideal with γ = 1.4 in the computation domain [0,1], the density is everywhere unit and the pressure is p = 1000 for 0 ≤ x < 0.1 and p = 100 for 0.9 < x ≤ 1.0, while it is only p = 0.01 for 0.1 < x < 0.9. The solid-wall boundary condition is prescribed at both ends. Two numerical methods are used to deal with the boundary condition. The ﬁrst one is the traditional numerical treatment with which we symmetrically extend the solution values into ghost cells. The second one uses the present boundary condition treatment in the solid-wall case, with which the procedure in Subsections 4.1 and 4.2 are applied. The CFL number is 0.6.

The numerical solutions using the present boundary condition treatments are displayed in Figure 3 at output time t = 0.038, in comparison with those using symmetric extension of interior information to ghost cells. The similar results veriﬁes the eﬀectiveness of the current approach for the one-dimensional solid-wall boundary condition.

- Example 6. The nozzle ﬂow. The problem of the nozzle ﬂow is quasi onedimensional. A converging-diverging duct occupies the spatial interval x ∈ (0,1) and has a continuous cross-sectional area function A(x) given by


 

Ain exp[− log(Ain)sin2(2πx)], 0 ≤ x ≤ 0.25,

A(x) =

(84)

2π(1 − x) 3

Aex exp[− log(Aex)sin2(

)], 0.25 ≤ x ≤ 1,



![image 637](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile637.png>)

with Ain = 4.864317646 and Aex = 4.234567901. The cross-sectional area

## 400 cells

## 800 cells

- 0
- 1
- 2
- 3
- 4
- 5
- 6
- 7


- 0
- 1
- 2
- 3
- 4
- 5
- 6
- 7


|reference<br><br>GRP4-HWENO5 with the present boundary treatment GRP4-HWENO5 with the traditional boundary treatment<br><br>| |
|---|
|
|---|


|reference<br><br>GRP4-HWENO5 with the present boundary treatment GRP4-HWENO5 with the traditional boundary treatment<br><br>| |
|---|
|
|---|


| | |
|---|---|
| | |
| | |
| | |


| | |
|---|---|
| | |
| | |
| | |
| | |


| | |
|---|---|
| | |
| | |
| | |
| | |


| | | |
|---|---|---|
| | | |


Density

Density

| | |
|---|---|
| | |
| | |


0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1

0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1

x

x

- Figure 3: The Woodward–Colella problem computed with the present boundary condition treatment (squares) and the conventional reﬂection boundary condition treatment (dots) with 400 cells (200 are shown, left) and 800 cells (400 are shown, right). The numerical scheme used is the GRP4-HWENO5 scheme. The solid lines are the reference solution computed with 4000 cells.


reaches its minimal value at x = 0.25, which is called the throat of the duct. The governing PDEs of the nozzle ﬂow are the Euler equations with the geometric source term (63). The ﬂuid ﬂows from the left to the right. We set x = 0 as the entrance of the duct and x = 1 as the exit. The ﬂow in the duct should ﬁnally reaches a steady state as the physics indicates.

There are two types of steady states: a continuous steady state and a discontinuous steady state containing a stationary shock. The initial conditions for both cases take

 

(ρ0, 0, p0), x < 0.25, (ρ0(pex/p0)1/γ, 0, pex), x > 0.25,

(85)

(ρ(x,0), v(x,0), p(x,0)) =



where γ = 1.4, ρ0 and p0 are parameters, determining if the steady state is continuous or not. In the previous numerical studies of the nozzle ﬂow [1, 2], the inﬂow density, velocity and pressure are assigned as the inﬂow boundary condition to the ghost cells out of the entrance, and the outﬂow pressure is assigned as the outﬂow boundary condition to the ghost cell out of the exit. In the present study, the approximation strategy of boundary conditions in

Subsections 4.1 and 4.3 is applied.

For the ﬁrst case, we set ρ0 = p0 = 1 and pex = 0.0272237 in (85). See [1]. This makes the steady solution a continuous isentropic one deﬁned by

γ − 1 2

[M(x)]2

ρ(x) = ρ0 1 +

![image 638](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile638.png>)

γ − 1 2

[M(x)]2

p(x) = p0 1 +

![image 639](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile639.png>)

− γ−1 1

![image 640](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile640.png>)

,

− γ−γ 1

![image 641](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile641.png>)

,

(86)

![image 642](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile642.png>)

v(x) = M(x) γ p(x)/ρ(x),

where M(x) is determined by the sectional area A(x) through the relation

1 [M(x)]2

[A(x)]2 =

![image 643](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile643.png>)

1 γ + 1

![image 644](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile644.png>)

γ − 1 2

[M(x)]2

1 +

![image 645](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile645.png>)

γ+1 γ−1

![image 646](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile646.png>)

. (87)

In this case, the ﬂow is subsonic upstream to the throat and supersonic downstream to the throat. Thus the inﬂow boundary condition at the entrance x = 0 is prescribed as in (64) with,

γ − 1 2

[M(0)]2

pin := p0 1 +

![image 647](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile647.png>)

γ − 1 2

[M(0)]2

ρin := ρ0 1 +

![image 648](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile648.png>)

− γ−γ 1

![image 649](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile649.png>)

,

− γ−1 1

![image 650](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile650.png>)

.

(88)

At the exit x = 1, the ﬂow is supersonic and no boundary condition is required. The numerical result is displayed in Figure 4 with the current method, using 22 computational cells. The output time is t = 5 and the CFL number is 0.6. The solution converges to the expected steady one and attains a better agreement with the steady solution compared with those given in [1, 2].

The other steady solution contains a stationary shock separating two pieces of isentropic solutions deﬁned as in (86) with separate pairs of (ρ0,p0). In this case we set ρ0 = p0 = 1 and pex = 0.4 in (85) to get the initial data. The shock stands downstream to the throat, and the ﬂow jumps from supersonic to subsonic after passing the shock. The exit x = 1 is subsonic for such a case. Now we set the inﬂow boundary condition to be (64) and (88) with ρ0 = p0 = 1 at the entrance x = 0 and the outﬂow boundary condition to be (67) with pex = 0.4 at the exit x = 1. Figure 5 shows the numerical results with 22 computational

- 0.8
- 1


|exact solution<br><br>GRP4-HWENO5 with the present boundary treatment|
|---|


|exact solution<br><br>GRP4-HWENO5 with the present boundary treatment|
|---|


Machnumber

0.6

Pressure

0.4

0.2

| | |
|---|---|
| | |


0

- 0

- 0.5
- 1

1.5

2

- 2.5
- 3




0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1

0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1

x

x

- Figure 4: The isentropic ﬂow throughout all the duct computed with the two-stage fourthorder scheme. The density and the Mach number at t = 5 are shown (squares). 22 cells are used. The solid line is the exact solution given by (86).

cells. The output time is t = 5 and the CFL number is 0.6. Once again, the solution converges to the expected steady one and matches it better compared with those given in [1, 2].

x

0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1

Pressure

0

0.2

0.4

0.6

- 0.8
- 1


|exact solution<br><br>GRP4-HWENO5 with the present boundary treatment|
|---|


x

0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1

Machnumber

- 0

- 0.5
- 1

1.5

2

- 2.5
- 3




|exact solution<br><br>GRP4-HWENO5 with the present boundary treatment|
|---|


- Figure 5: The ﬂow with a steady shock computed with the two-stage fourth-order scheme. The density and the Mach number at t = 5 are shown (squares). 22 cells are used. The solid line is the exact solution given by (86).


As the accuracy test is performed for such a case, we need to modify the cross section a little bit, such as

A(x) = Ain exp[− log(Ain)sin2(πx)], for 0 ≤ x ≤ 1, (89)

instead of (84), in order to guarantee the ﬂow is smooth. This is because A′′(x) in (84) is discontinuous, which leads to the solution formula in (86) has the discontinuity in its ﬁrst order derivative at the throat of the duct which can be

seen in Figure 4. The initial data in this case is

 

(ρ0, 0, p0), x < 0.5, (ρ0(pex/p0)1/γ, 0, pex), x > 0.5,

(ρ(x,0), v(x,0), p(x,0)) =



by setting ρ0 = p0 = 1 and pex = 0.021910717. The numerical errors and accuracy orders of the momentum Aρv are shown in Table 4, which veriﬁes the numerical accuracy of the present boundary condition treatment.

Table 4: Numerical errors and accuracy orders for the case with the cross section (89)

![image 651](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile651.png>)

![image 652](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile652.png>)

![image 653](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile653.png>)

![image 654](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile654.png>)

![image 655](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile655.png>)

![image 656](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile656.png>)

![image 657](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile657.png>)

m L1 error order L∞ error order

![image 658](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile658.png>)

![image 659](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile659.png>)

![image 660](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile660.png>)

![image 661](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile661.png>)

![image 662](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile662.png>)

![image 663](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile663.png>)

![image 664](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile664.png>)

40 2.13e-04 2.04 2.59e-03 1.94 80 1.40e-06 7.25 1.22e-05 7.73

![image 665](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile665.png>)

![image 666](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile666.png>)

![image 667](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile667.png>)

![image 668](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile668.png>)

![image 669](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile669.png>)

![image 670](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile670.png>)

![image 671](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile671.png>)

![image 672](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile672.png>)

![image 673](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile673.png>)

![image 674](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile674.png>)

![image 675](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile675.png>)

![image 676](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile676.png>)

160 2.87e-08 5.61 3.34e-07 5.19 320 2.10e-09 3.77 2.12e-08 3.98 640 1.30e-10 4.02 1.34e-09 3.98

![image 677](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile677.png>)

![image 678](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile678.png>)

![image 679](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile679.png>)

![image 680](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile680.png>)

![image 681](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile681.png>)

![image 682](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile682.png>)

![image 683](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile683.png>)

![image 684](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile684.png>)

![image 685](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile685.png>)

![image 686](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile686.png>)

![image 687](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile687.png>)

![image 688](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile688.png>)

![image 689](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile689.png>)

- Example 7. The double Mach reﬂection problem. This is a standard two-dimensional test problem for high resolution schemes. The computational domain for this problem is [0,4] × [0,1], and [0,3] × [0,1] is shown. A reﬂective wall lies at the bottom of the computational domain starting from x = 16. Initially a right-moving Mach 10 shock is positioned at x = 61,y = 0 and makes


![image 690](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile690.png>)

![image 691](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile691.png>)

a π3 angle with the x-axis. More details about this problem can be seen in [22].

![image 692](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile692.png>)

Our computations use both the traditional and the present new numerical boundary condition treatments to deal with the reﬂective boundary condition along the wall {(x,0) : x ∈ [1/6,4]}. For the traditional boundary condition treatment, we use the symmetrical extension for the ghost cells outside the boundary. For the present new boundary condition treatment, we apply the procedure in Subsections 4.1 and 4.4.

The computations are carried out by the GRP4-HWENO5 scheme with 960× 240 grids, using both numerical boundary condition treatments. The numerical results are displayed in Figure 6 with 30 contours of the density at time 0.2. The

CFL number is 0.6. The two numerical results are similar which indicates that the present approach works well for the two-dimensional solid-wall boundary condition.

0.9

0.8

0.7

0.6

0.5

0.4

0.3

0.2

0.1

0.5 1 1.5 2 2.5

0.9

0.8

0.7

0.6

0.5

0.4

0.3

0.2

0.1

0.5 1 1.5 2 2.5

- Figure 6: The numerical results of the double mach reﬂection problem in Example 7 given by the scheme GRP4-HWENO5 combined with the traditional reﬂection boundary condition treatment (upper) and the current boundary condition treatment (lower). The contours of density are shown. 960 × 240 cells are used.


- Example 8. The forward facing step problem. This is also a standard test problem for the two-dimensional computations proposed in [22]. The wind tunnel is 1 length unit wide and 3 length units long. The step is 0.2 length units high and is located 0.6 length units from the left-hand end of the tunnel. The problem is initialized by a unit right-going Mach 3 ﬂow with (ρ0,u0,v0,p0) = (1.4,3,0,1) in the tunnel. Reﬂective boundary conditions are applied along the walls of the tunnel.


As in Example 7, both the traditional and the present new boundary condition treatments are applied to the reﬂective walls of the tunnel. The numerical

results are shown in Figure 7, with 960 × 320 cells. The computations stop at the time t = 4 and the CFL number is 0.6. The two numerical results are similar which once again veriﬁes the eﬀectiveness of the present approach.

0.9

0.8

0.7

0.6

0.5

0.4

0.3

0.2

0.1

0

0.5 1 1.5 2 2.5 3

0.9

0.8

0.7

0.6

0.5

0.4

0.3

0.2

0.1

0

0.5 1 1.5 2 2.5 3

- Figure 7: The numerical results of the forward facing step problem in Example 8 given by the scheme GRP4-HWENO5 using the traditional boundary condition treatment (upper) and the present one (lower). The contours of density are shown. 960 × 320 cells are used.


- 6. Discussions


In this paper we provide a method to approximate boundary conditions with fourth-order accuracy in order to suit the two-stage fourth order accurate schemes for hyperbolic conservation laws that we proposed earlier [14]. The application is speciﬁed to the compressible Euler equations with several commonly-used boundary conditions. We are certainly aware that there are many issues waiting for investigation, such as moving boundary problems, solid wall boundary conditions with curved geometry, small cut-cell problems, and

moving boundary problems, which will be studied in a future paper.

Here we would like to emphasize that the inverse Lax-Wendroﬀ approach is fundamental in the sense that the governing equations are eﬀectively adopted to treat the boundary conditions [9, 20, 21, 15]. In the paper the inverse LaxWendroﬀ approach is used with the least complexity by taking advantage of the two-stage method [14]. No successive diﬀerentiation of governing equations is made. Nevertheless, the boundary conditions have to be carefully treated at intermediate stages, analogous to any other multi-stage numerical methods.

Of course, just as the fact that the two-stage fourth order method in [14] can be extended to higher order accurate multi-stage method in [17], the current numerical boundary condition treatment can be extended to much higher order accuracy in a straightforward way. The application to hyperbolic systems beyond the compressible ﬂuid ﬂows can be treated similarly. We do not want to repeat the technicality from the scientiﬁc viewpoint.

Appendix A. The interpolation results in subsection 3.1

This appendix is dedicated to list the interpolation results in Section 3.1. Recall that we assume x = 0 and x = 1 are the inﬂow and outﬂow boundaries for the IBVP (1) of the one-dimensional scalar conservation laws, respectively. The stencils are denoted in (19).

- Appendix A.1. Cell averages and cell diﬀerences The reconstructed average of u in I−1 and I−2 on those stencils are:

u¯(2)−1 =

1 4

![image 693](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile693.png>)

(−6g + 6 h f′(g)−1 g′ + 11¯u0 − u¯1),

- u¯(1)−1 = h f′(g)−1 g′ + u¯0,

- u¯(0)−1 = g +

1 2

![image 694](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile694.png>)

h f′(g)−1 g′,

u¯(2)−2 =

1 4

![image 695](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile695.png>)

(−90g + 42 h f′(g)−1 g′ + 105¯u0 − 11¯u1),

- u¯(1)−2 = −6gh + 5 f′(g)−1 g′ + 7¯u0,




u¯(0)−2 = g +

3 2

![image 696](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile696.png>)

h f′(g)−1 g′.

(A.1)

The reconstructed x-diﬀerence of u in I−1 and I−2 on those stencils are:

∆u(2)−1 =

1 8h

![image 697](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile697.png>)

(66g − 34 h f′(g)−1 g′ − 73¯u0 + 7¯u1),

- ∆u(1)−1 =

1 2h

![image 698](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile698.png>)

(6g − 5 h f′(g)−1 g′ − 6¯u0),

- ∆u(0)−1 = −f′(g)−1 g′,

∆u(2)−2 =

1 8h

![image 699](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile699.png>)

(294g − 118 h f′(g)−1 g′ − 331¯u0 + 37¯u1),

- ∆u(1)−2 =




- 1

![image 700](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile700.png>)

- 2h


(18g − 11 h f′(g)−1 g′ − 18¯u0),

∆u(0)−2 = −f′(g)−1 g′.

(A.2)

- Appendix A.2. Smoothness indicators The smoothness indicators on these stencils are listed as follows,


1 80

β(2) =

![image 701](<2018-du-two-stage-fourth-order-time-accurate_images/imageFile701.png>)

66516g2 + 9444(hf′(g)−1g′)2 − 56348f′(g)−1g′hu¯0

+85929¯u20 + 6644f′(g)−1g′hu¯1 − 20694¯u0u¯1 + 1281¯u21

+12g(4142f′(g)−1g′h − 12597¯u0 + 1511¯u1) ,

β(1) = 48g2 + 54ghf′(g)−1g′ + 16(hf′(g)−1g′)2

(A.3)

−96gu¯0 + 48¯u20 − 54hf′(g)−1g′u¯0, β(0) = (hf′(g)−1g′)2.

Acknowledgements

This work is supported by NSFC (no. 11771054) and Foundation of LCP. Both authors appreciate an anonymous reviewer for his suggestions on the accuracy test of the nozzle problem and on curved geometry or small cut-cell problems. The latter suggestion would be adopted in the future due to very technical details and the clarity of the paper. We also thank the other two reviewers for their suggestions that substantially polish this paper.

References

- [1] M. Ben-Artzi and J. Falcovitz, Generalized Riemann Problems in Computational Fluid Dynamics, Cambridge University Press, Cambridge, 2003.
- [2] M. Ben-Artzi and J. Li, Hyperbolic balance laws: Riemann invariants and the generalized Riemann problem, Numer. Math., 106 (2007), pp. 369– 425.
- [3] M. Ben-Artzi, J. Li, and G. Warnecke, A direct Eulerian GRP scheme for compressible ﬂuid ﬂows, J. Comput. Phys., 218 (2006), pp. 19–43.
- [4] M. Berger, C. Helzel, and R. LeVeque, h-Box methods for the approximation of hyperbolic conservation laws on irregular grids, SIAM J. Numer. Anal., 41 (2003), pp. 893–918.
- [5] M. Carpenter, D. Gottlieb, S. Abarbanel, and W.-S. Don, The theoretical accuracy of Runge-Kutta time discretizations for the initial boundary value problem: a study of the boundary error, SIAM J. Sci. Comput., 16 (1995), pp. 1241–1252.
- [6] Z. Du and J. Li, A Hermite WENO reconstruction for fourth order temporal accurate schemes based on the GRP solver for hyperbolic conservation laws, J. Comput. Phys., 355 (2018), pp. 385–396.


- [7] H. Forrer and R. Jeltsch, A higher-order boundary treatment for Cartesian-grid methods, J. Comput. Phys., 140 (1998), pp. 259–277.
- [8] C. Helzel, M. Berger, and R. LeVeque, A high-resolution rotated grid method for conservation laws with embedded geometries, SIAM J. Sci. Comput., 26 (2005), pp. 785–809.
- [9] L. Huang, C.-W. Shu, and M. Zhang, Numerical boundary conditions for the fast sweeping high order WENO methods for solving the Eikonal equation, J. Comput. Math., 26 (2008), pp. 336–346.
- [10] H.-O. Kreiss and J. Lorenz, Initial-Boundary Value Problems and the Navier-Stokes Equations, Academic Press, San Diego, 1989.
- [11] H.-O. Kreiss and N. Petersson, A second order accurate embedded boundary method for the wave equation with Dirichlet data, SIAM J. Sci. Comput., 27 (2006), pp. 1141–1167.
- [12] H.-O. Kreiss, N. Petersson, and J. Ystrom¨ , Diﬀerence approximations of the Neumann problem for the second order wave equation, SIAM J. Numer. Anal., 42 (2004), pp. 1292–1323.
- [13] L. Krivodonova and M. Berger, High-order accurate implementation of solid wall boundary conditions in curved geometries, J. Comput. Phys., 211 (2006), pp. 492–512.
- [14] J. Li and Z. Du, A two-stage fourth order time-accurate discretization for Lax-Wendroﬀ type ﬂow solvers, I. Hyperbolic conservation laws, SIAM J. Sci. Comput., 38 (2016), pp. A3046–A3069.
- [15] T. Li, C.-W. Shu, and M. Zhang, Stability analysis of the inverse LaxWendroﬀ boundary treatment for high order upwind-biased ﬁnite diﬀerence schemes, J. Comput. Appl. Math., 299 (2016), pp. 140–158.
- [16] H. Liepmann and A. Roshko, Elements of Gasdynamics, Wiley, New York, 1957.


- [17] L. Pan, K. Xu, Q. Li, and J. Li, An eﬃcient and accurate two-stage fourth-order gas-kinetic scheme for the Euler and Navier-Stokes equations, J. Comput. Phys., 326 (2016), pp. 197–221.
- [18] D. Pathria, The correct formulation of intermediate boundary conditions for Runge-Kutta time integration of initial boundary value problems, SIAM J. Sci. Comput., 18 (1997), pp. 1255–1266.
- [19] B. Sjogreen¨ and N. Petersson, A Cartesian embedded boundary method for hyperbolic conservation laws, Commun. Comput. Phys., 2

(2007), pp. 1199–1219.

- [20] S. Tan and C.-W. Shu, Inverse Lax-Wendroﬀ procedure for numerical boundary conditions of conservation laws, J. Comput. Phys., 229 (2010), pp. 8144–8166.
- [21] S. Tan, C. Wang, C.-W. Shu, and J. Ning, Eﬃcient implementation of high order inverse Lax-Wendroﬀ boundary treatment for conservation laws, J. Comput. Phys., 231 (2012), pp. 2510–2527.
- [22] P. Woodward and P. Colella, The numerical simulation of twodimensional ﬂuid ﬂow with strong shocks, J. Comput. Phys., 54 (1984), pp. 115–173.


