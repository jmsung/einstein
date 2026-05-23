arXiv:1602.05803v1[math.NA]18Feb2016

An Eﬃcient and Accurate Two-Stage Fourth-order Gas-kinetic Scheme for the Navier-Stokes Equations

Liang Pana, Kun Xua,b,∗, Qibing Lic, Jiequan Lid

aDepartment of Mathematics, Hong Kong University of Science and Technology, Clear Water Bay, Kowloon, Hong Kong bDepartment of Mechanical and Aerospace Engineering, Hong Kong University of Science and Technology, Clear Water Bay, Kowloon, Hong Kong cSchool of Aerospace, Tsinghua University, Beijing 100084, China dInstitute of Applied Physics and Computational Mathematics, Beijing, 100088, China

![image 1](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile1.png>)

Abstract

For computational ﬂuid dynamics (CFD), the generalized Riemann problem (GRP) solver and the gas-kinetic kinetic scheme (GKS) provide a time-accurate ﬂux function starting from a discontinuous piecewise linear ﬂow distributions around each cell interface. With the use of time derivative of the ﬂux function, a two-stage Lax-Wendroﬀ-type (L-W for short) time stepping method has been recently proposed in the design of a fourth-order time accurate method [18]. In this paper, based on the same time-stepping method and the second-order GKS ﬂux function [34], a fourth-order gas-kinetic scheme is constructed for the Euler and Navier-Stokes equations. In comparison with the formal one-stage time-stepping third-order gas-kinetic solver [21], the current fourth-order method not only reduces the complexity of the ﬂux function, but also improves the accuracy of the scheme, even though the third- and fourth-order schemes have similar computation cost. Most importantly, the robustness of the fourth-order GKS is as good as the second-order one. Perfect numerical solutions can be obtained from the high Reynolds number boundary layer solutions to the hypersonic viscous heat conducting ﬂow computations. Many numerical tests, including many diﬃcult ones for the Navier-Stokes solvers, have been used to validate the current fourth-order method. Following the two-stage time-stepping framework, the one-stage third-order GKS can be easily extended to a ﬁfth-order method with the usage of both ﬁrst-order and second-order time derivatives of the ﬂux function. The use of time-accurate ﬂux function may have great impact on the development of higher-order CFD methods.

Keywords: two-stage Lax-Wendroﬀ-type time stepping method, fourth-order gas-kinetic scheme, Navier-Stokes equations.

![image 2](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile2.png>)

![image 3](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile3.png>)

∗Corresponding author

Email addresses: panliangjlu@sina.com (Liang Pan), makxu@ust.hk (Kun Xu), lbq@tsinghua.edu.cn (Qibing Li), li_jiequan@iapcm.ac.cn (Jiequan Li)

Preprint submitted to Elsevier October 7, 2018

- 1. Introduction


To develop third and higher-order numerical methods has attracted great attention in recent decades. In comparison with second-order schemes, which were mostly developed in the 70s and 80s, the higher-order methods can provide more accurate solutions, but they are less robust and more complicated. There are many review papers and monographs about the current status of higher-orders schemes, which include the discontinuous Galerkin (DG) [6], essential non-oscillatory (ENO) [12], weighted essential non-oscillatory (WENO) [23],PNPM [8], multi-moment constrained method [13], and many others. Most of those methods use the Runge-Kutta time-stepping approach to achieve higher order temporal accuracy [10]. Based on the time-independent ﬂux function of the Riemann solver [31], in order to achieve a fourth-order time accuracy, four-stage Runge-Kutta time stepping method has to be used. Moreover, the CFL number for those methods strongly depend on the order of the scheme, such as the DG method.

Recently, based on the time-dependent ﬂux function of the generalized Riemann problem (GRP) [1, 2, 3], a two-stage fourth order time-accurate discretization was developed for Lax-Wendroﬀ type (L-W for short) ﬂow solvers, particularly applied for the hyperbolic conservation laws [18]. The reason for the success of a two-stage L-W type time stepping method in achieving a fourth-order time accuracy is solely due to the use of both ﬂux function and its time derivative. In terms of the gas evolution model, the gas-kinetic scheme (GKS) provides a time accurate ﬂux function as well, even though it depends on time through a much more complicated relaxation process from the kinetic to the hydrodynamic scale physics than the time-dependent ﬂux function of GRP. This paper is about to construct a fourth-order time accurate gas-kinetic scheme (GKS) with the two-stage temporal discretization for the Euler and Navier-Stokes (NS) equations.

For the NS solutions, second-order and third-order gas-kinetic schemes have been constructed in the past years [34, 21, 16, 29]. The ﬂux evaluation in the scheme is based on the time evolution of ﬂow variables from an initial piece-wise discontinuous polynomials around each cell interface, where high-order spatial and temporal evolutions of a gas distribution function are coupled nonlinearly. In comparison with other high-order schemes, the GKS integrates the ﬂux function over a time step analytically without employing the multi-stage Runge-Kutta time stepping techniques. However, with the one-stage gas evolution model, the formulation of GKS can become very complicated for the further improvement of the order of the scheme, such as the fourth-order scheme [22], especially for multidimensional computations. The two-stage L-W time stepping method in [18] provides a reliable framework to develop a fourth-order GKS with a second-order ﬂux function. In this paper, we are going to present such a fourth-order GKS for the Euler and Navier-Stokes solutions. The current scheme can use a time step with CFL number on the order of 0.5. Most importantly, the current fourth-order GKS is as robust as the second-order method, which works perfectly from the subsonic to the hypersonic viscous heat conducting ﬂows. Numerical tests show that the current scheme not only has the expected order of accuracy for the smooth ﬂow, but also has favorable shock capturing property for the discontinuous solutions. As a further extension, the third-order ﬂux function [28, 21, 24] can be also used to construct

two-stage ﬁfth-order temporal accurate methods with the inclusion of both ﬁrst-order and second-order time derivatives of the ﬂux function. The detailed formulation is presented in the Appendix of this paper. Theoretically, this process for constructing even higher-order schemes can go forward continuously.

This paper is organized as follows. In Section 2, the general formulation for the twostage temporal discretization is introduced. In Section 3, a fourth-order gas-kinetic scheme is presented based on the two-stage time discretization. Section 4 includes numerical examples to validate the current algorithm. The last section is drawing the conclusion. The extension for the construction of two-stage ﬁfth-order schemes is given in Appendix.

- 2. Fourth-order temporal discretization


A two-stage fourth-order time-accurate discretization was developed for Lax-Wendroﬀ ﬂow solvers, particularly applied for hyperbolic equations with the generalized Riemann problem (GRP) solver [18]. Consider the following time-dependent equation,

with the initial condition at tn, i.e.,

∂w ∂t

= L(w), (1)

![image 4](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile4.png>)

w(t = tn) = wn, (2)

where L is an operator for spatial derivative of ﬂux. The time derivatives are obtained using the Cauchy-Kovalevskaya method,

∂wn ∂t

∂ ∂tL(wn) =

∂

∂wL(wn)L(wn). Introducing an intermediate state at t∗ = tn + ∆t/2,

= L(wn),

![image 5](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile5.png>)

![image 6](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile6.png>)

![image 7](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile7.png>)

w∗ = wn +

- 1

![image 8](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile8.png>)

- 2


1 8

∆tL(wn) +

![image 9](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile9.png>)

∂ ∂tL(wn), (3)

∆t2

![image 10](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile10.png>)

the corresponding time derivatives are obtained as well for the intermediate stage state,

∂ ∂tL(w∗) =

∂

∂w∗ ∂t

∂wL(w∗) · L(w∗). Then, the state w can be updated with the following formula,

= L(w∗),

![image 11](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile11.png>)

![image 12](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile12.png>)

![image 13](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile13.png>)

wn+1 = wn + ∆tL(wn) +

1 6

∆t2

![image 14](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile14.png>)

∂ ∂tL(wn) + 2

∂ ∂tL(w∗) . (4)

![image 15](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile15.png>)

![image 16](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile16.png>)

It can be proved that the above time stepping method with Eq.(3) and Eq.(4) provides a fourth-order time accurate solution for w(t) at t = tn + ∆t. The details of the analysis can be found in [18]. Thus, based on a time accurate solution ∂L/∂t, a fourth-order temporal

accuracy can be achieved from the two-stage discretization of Eq.(1) through Eq.(3) and Eq.(4).

We apply this approach for conservation laws

f(w) ∂x

∂w ∂t

+

= 0, (5)

![image 17](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile17.png>)

![image 18](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile18.png>)

where w is a conservative variable and f(w) is the corresponding ﬂux, which includes all terms related to the viscous heat conducting ﬂow. The semi-discrete form of a ﬁnite volume scheme for equations Eq.(5) can be written as

∂wi ∂t

1 ∆xi

= Li(w) = −

![image 19](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile19.png>)

![image 20](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile20.png>)

(fi+1/2 − fi−1/2), (6)

where wi are the cell averaged conservative variables of the cell Ii = [xi−1/2, xi+1/2], fi+1/2 are the ﬂuxes at the cell interface x = xi+1/2, and ∆xi = xi+1/2 − xi−1/2. A similar ﬁnite volume formulation can be obtained in two- and three-dimensional cases. Then (6) falls into the framework of the two-stage L-W time stepping.

- 3. A fourth-order gas-kinetic scheme


The similarity between the generalized Riemann problem (GRP) solver and the gaskinetic scheme has been studied in [19]. In both schemes, the spatial and temporal accuracy are coupled through a generalized Lax-Wendroﬀ-type procedure for the discontinuous cases, and a single stage time integration is used for the ﬂux transport across a cell interface for the second-order schemes. In this section, a fourth-order gas-kinetic scheme from a secondorder ﬂux function will be constructed through a two-stage time discretization framework of Eq.(3) and Eq.(4) for the Euler and Navier-Stokes solutions.

- 3.1. Second-order gas-kinetic ﬂux solver The two-dimensional BGK equation can be written as [4],


ft + u · ∇f =

g − f τ

, (7)

![image 21](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile21.png>)

where f is the gas distribution function, g is the corresponding equilibrium state, and τ is the collision time. The collision term satisﬁes the compatibility condition

g − f τ

ψdΞ = 0, (8)

![image 22](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile22.png>)

- 1

![image 23](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile23.png>)

- 2


(u2 + v2 + ξ2)), dΞ = dudvdξ1...dξK, K is the number of internal freedom, i.e. K = (4 − 2γ)/(γ − 1) for two-dimensional ﬂows, and γ is the speciﬁc heat ratio. The conservative variables are denoted as W = (ρ, ρU, ρV, ρE). In the smooth region,

where ψ = (1, u, v,

the gas distribution function can be expanded as f = g − τDug + τDu(τDu)g − τDu[τDu(τDu)g] + ...,

where Du = ∂/∂t + u · ∇. By truncating on diﬀerent orders of τ, the corresponding macroscopic equations can be derived. For the Euler equations, the zeroth order truncation is taken, i.e. f = g. For the Navier-Stokes equations, the ﬁrst order truncation is used,

f = g − τ(ugx + vgy + gt). (9)

Based on the higher order truncations, the Burnett and super-Burnett equations can be obtained [5, 37, 35].

In order to update the ﬂow variables, the ﬂux is based on the integral solution of gas distribution function from the BGK equation at a cell interface,

1 τ

f(xi+1/2, t, u, v, ξ) =

![image 24](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile24.png>)

t

′)/τdt′ + e−t/τf0(−ut, y − vt, u, v, ξ), (10)

g(x′, y′, t′, u, v, ξ)e−(t−t

0

where xi+1/2 = 0 is the location of the cell interface, x = x′ + u(t − t′) and y = y′ + v(t − t′) are the trajectory of particles, f0 is the initial gas distribution function, and g is the corresponding equilibrium state. According to Eq.(10), the time dependent gas distribution function f(xi+1/2, t, u, ξ) at the cell interface xi+1/2 can be expressed as [34, 36]

f(xi+1/2, t, u, v, ξ) =(1 − e−t/τ)g0 + ((t + τ)e−t/τ − τ)(a1u + a2v)g0

![image 25](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile25.png>)

![image 26](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile26.png>)

+(t − τ + τe−t/τ)Ag¯ 0

+e−t/τgr[1 − (τ + t)(a1ru + a2rv) − τAr)]H(u)

+e−t/τgl[1 − (τ + t)(a1lu + a2lv) − τAl)](1 − H(u)). (11)

Based on the spatial reconstruction of macroscopic ﬂow variables, which will be given in the next subsection, the conservative variables Wl and Wr on the left and right hand sides of a cell interface, and the corresponding equilibrium states gl and gr, can be determined. Their spatial derivatives in both normal and tangential directions, such as (a1l, a1r, a2l, a2r), are related to the normal and tangential derivatives of the initial macroscopic ﬂow variables. The time derivatives (Al, Ar) can be obtained from the requirement on the ﬁrst-order ChapmanEnskog expansion, such as

gl(a1lu + a2lv + Al)ψdΞ = 0,

and

gr(a1ru + a2rv + Ar)ψdΞ = 0. Through the compatibility condition Eq.(8), the conservative variables W0 and the equi-

librium state g0 at the cell interface can be determined as follows,

ψg0dΞ = W0 =

ψgldΞ +

u>0

ψgrdΞ. (12)

u<0

Then, with the spatial derivatives of macroscopic ﬂow variables across and along a cell interface and the compatibility condition, the coeﬃcients related to the spatial derivatives in the equilibrium state in Eq.(11), such as (a¯1, a¯2), and its time derivative A¯, can be fully obtained by,

![image 27](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile27.png>)

∂W ∂x

a1 =

, a2 =

![image 28](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile28.png>)

![image 29](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile29.png>)

![image 30](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile30.png>)

![image 31](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile31.png>)

∂W ∂y

![image 32](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile32.png>)

, a1u + a2v + A = 0, (13)

![image 33](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile33.png>)

![image 34](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile34.png>)

![image 35](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile35.png>)

where ... are the moments of the equilibrium gas distribution function g0, and deﬁned by

... = g0(...)ψdΞ.

More details of the gas-kinetic scheme can be found in [36].

- 3.2. Spatial reconstruction


The above time evolution solution is based on the high-order initial reconstruction for macroscopic ﬂow variables, and the ﬁfth-order WENO reconstruction is adopted in this study [14].

For one dimensional computation, Wl, Wr and W0 corresponding to the equilibrium states gl, gr and g0 in Eq.(11) can be constructed at the cell interface xi+1/2. The spatial derivatives ∂W/∂x are also given based on the reconstruction. Especially, for the determination of the equilibrium state g0 across the cell interface with a ﬁfth-order of accuracy, the conservative variables around the cell interface can be expanded as

1 6

1 24

- 1

![image 36](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile36.png>)

- 2


S4(x − x∗)4. With the following conditions,

S2(x − x∗)2 +

S3(x − x∗)3 +

![image 37](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile37.png>)

W(x) = W0 + S1(x − x∗) +

![image 38](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile38.png>)

![image 39](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile39.png>)

![image 40](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile40.png>)

W(x) = Wi+k, k = −1, ..., 2,

Ii+k

the derivatives are given by

5 4

1 12

![image 41](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile41.png>)

(Wi+1 − Wi) /∆x. For two dimensional computation, the ﬁfth-order Gauss quadrature is used to achieve the

(Wi+2 − Wi−1) +

Wx = S1 = −

![image 42](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile42.png>)

![image 43](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile43.png>)

accuracy in space

1 ∆y

![image 44](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile44.png>)

yj+1/2

F(W(xi+1/2, y, t))dy =

yj−1/2

k

ωℓF(W(xi+1/2, yℓ, t)), (14)

ℓ=1

where yl ∈ [yj−1/2, yj+1/2], ℓ = 1, ..., 3 are the Gauss quadrature points, and ωℓ are corresponding weights. Based on the tangential reconstruction, the tangential derivatives at each Gauss quadrature points can be obtained.

- 3.3. Two-stage gas-kinetic scheme


In this section, a two-stage fourth-order gas-kinetic scheme will be presented based on the time-dependent gas distribution function (11) at each cell interface.

For the gas-kinetic scheme, the gas evolution is a relaxation process from kinetic to hydrodynamic scale through the exponential function, and the corresponding ﬂux is a complicated function of time. In order to obtain the time derivatives of the ﬂux function at tn and t∗ = tn + ∆t/2 with the correct physics, the ﬂux function should be approximated as a linear function of time within a time interval. Let’s ﬁrst introduce the following notation,

Fi+1/2(Wn, δ) =

tn+δ

Fi+1/2(Wn, t)dt =

tn

tn+δ

tn

uf(xi+1/2, t, u, v, ξ)dudξdt.

In the time interval [tn, tn + ∆t], the ﬂux is expanded as the following linear form

Fi+1/2(Wn, t) = Fin+1/2 + ∂tFjn+1/2(t − tn). (15) The coeﬃcients Fjn+1/2 and ∂tFjn+1/2 can be determined as follows,

- 1

![image 45](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile45.png>)

- 2


Fi+1/2(Wn, tn)∆t +

∂tFi+1/2(Wn, tn)∆t2 = Fi+1/2(Wn, ∆t), Fi+1/2(Wn, tn)∆t +

- 1

![image 46](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile46.png>)

- 2


1 8

∂tFi+1/2(Wn, tn)∆t2 = Fi+1/2(Wn, ∆t/2). By solving the linear system, we have

![image 47](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile47.png>)

Fi+1/2(Wn, tn) = (4Fi+1/2(Wn, ∆t/2) − Fi+1/2(Wn, ∆t))/∆t, ∂tFi+1/2(Wn, tn) = 4(Fi+1/2(Wn, ∆t) − 2Fi+1/2(Wn, ∆t/2))/∆t2. (16)

Similarly, Fi+1/2(W∗, t∗), ∂tFi+1/2(W∗, t∗) for the intermediate state can be constructed. For the two-dimensional computation, the corresponding ﬂuxes in the y-direction can be obtained as well.

With these notations, the two-stage algorithm for both Euler and Navier-Stokes equations is given as follows

- (i) With the initial reconstruction, update Wij∗ at t∗ = tn + ∆t/2 by

Wij∗ = Wijn −

1 ∆x

![image 48](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile48.png>)

Fi+1/2,j(Wn, ∆t/2) − Fi−1/2,j(Wn, ∆t/2) −

1 ∆y

![image 49](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile49.png>)

Gi,j+1/2(Wn, ∆t/2) − Gi,j−1/2(Wn, ∆t/2) ,

and compute the ﬂuxes and their derivatives by Eq.(16) for future use, Fi+1/2,j(Wn, tn), Gi,j+1/2,(Wn, tn), ∂tFi+1/2,j(Wn, tn), ∂tGi,j+1/2(Wn, tn).

- (ii) Reconstruct intermediate value Wij∗, and compute ∂tFi+1/2,j(W∗, t∗), ∂tGi,j+1/2(W∗, t∗),

where the derivatives are determined by Eq.(16) in the time interval [t∗, t∗ + ∆t].

- (iii) Update Wijn+1 by


Wijn+1 = Wijn −

∆t ∆x

[Fin+1/2,j − Fin−1/2,j] −

![image 50](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile50.png>)

∆t ∆y

[Gi,jn +1/2 − Gi,jn −1/2],

![image 51](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile51.png>)

where Fin+1/2,j and Gi,jn +1/2 are the numerical ﬂuxes and expressed as

∆t 6

∂tFi+1/2,j(Wn, tn) + 2∂tFi+1/2,j(W∗, t∗) ,

Fin+1/2,j = Fi+1/2,j(Wn, tn) +

![image 52](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile52.png>)

∆t 6

Gi,jn +1/2 = Gi,j+1/2,(Wn, tn) +

∂tGi,j+1/2(Wn, tn) + 2∂tGi,j+1/2(W∗, t∗) . For each ﬂux, the Gaussian quadratures Eq.(14) are used.

![image 53](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile53.png>)

- 4. Numerical tests


In this section, numerical tests for both inviscid and viscous ﬂows will be presented to validate our numerical scheme. For the inviscid ﬂow, the collision time τ takes

pl − pr pl + pr |∆t,

τ = ǫ∆t + C|

![image 54](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile54.png>)

where ε = 0.05 and C = 1. For the viscous ﬂow, we have

τ =

µ p

pl − pr pl + pr |∆t,

+ C|

![image 55](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile55.png>)

![image 56](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile56.png>)

where pl and pr denote the pressure on the left and right sides of the cell interface, µ is the viscous coeﬃcient, and p is the pressure at the cell interface. In smooth ﬂow regions, it will reduce to τ = µ/p. The ratio of speciﬁc heats takes γ = 1.4. The reason for including

artiﬁcial dissipation through the additional term in the particle collision time is to enlarge the kinetic scale physics in the discontinuous region for the construction of a numerical shock structure through the particle free transport and inadequate particle collision.

For the smooth ﬂow, the WENO reconstruction can be used directly on the conservative ﬂow variables. For the ﬂow with strong discontinuity, the characteristic variables can be used in the reconstruction. Based on Ai+1/2,j = (∂F/∂W)W=W∗, where W are the conservative variables, F(W) are the corresponding ﬂuxes, and W∗ = (Wi,j + Wi+1,j)/2, the cell averaged and point conservative values can be projected into the characteristic ﬁeld by ω = RW, where R is the matrix corresponding to right eigenvectors of A. The reconstruction scheme is applied on the characteristic variables ω. With the reconstructed polynomials for characteristic variables, the conservative ﬂow variables can be recovered by the inverse projection.

- 4.1. Accuracy tests


The ﬁrst case is the advection of density perturbation, and the initial condition is set as follows

ρ(x) = 1 + 0.2 sin(πx), U(x) = 1, p(x) = 1, x ∈ [0, 2]. The periodic boundary condition is adopted, and the analytic solution is

ρ(x, t) = 1 + 0.2 sin(π(x − t)), U(x, t) = 1, p(x, t) = 1.

In the computation, a uniform mesh with N points is used. As analyzed in the section before, with the ﬁfth-order spatial reconstruction, the leading truncation error for the fourth-order GKS is O(∆x5 + ∆t4). In these tests, a ﬁxed CFL number CFL = 0.4 is used for diﬀerent meshes. The L1 and L2 errors and orders at t = 2 are presented in Table.1. The ﬁfth order accuracy can be kept until the mesh N = 640. As a comparison, with the original second-order GKS, the leading error is on the order of O(∆x5 + ∆t2). With the identical spatial reconstruction and CFL number CFL = 0.4, only a second-order accuracy can be achieved. To show the order of accuracy, a small CFL number CFL = 0.1 is used. The L1 and L2 errors and orders at t = 2 are presented in Table.2. The ﬁfth order accuracy can be kept at the beginning. With the mesh reﬁnement, the temporal error becomes the dominant one and the accuracy reduces to a second order method.

The next test is the isotropic vortex propagation problem. The mean ﬂow is (ρ, U, V, p) = (1, 1, 1, 1), and an isotropic vortex is added to the mean ﬂow, i.e., with perturbation in u, v and temperature T = p/ρ, and no perturbation in entropy S = p/ργ. The perturbation is given by

ǫ 2π

(δU, δV ) =

![image 57](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile57.png>)

(γ − 1)ǫ2 8γπ2

(1−r2)

e1−r

2 (−y, x), δT = −

e

![image 58](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile58.png>)

![image 59](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile59.png>)

2

, δS = 0,

where r2 = x2 + y2 and the vortex strength ǫ = 5. The computational domain is [−5, 5] × [−5, 5], the periodic boundary conditions are imposed on the boundaries in both x and

![image 60](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile60.png>)

mesh L1 error convergence order L2 error convergence order 20 4.4759E-004 3.7653E-004 40 1.3764E-005 5.0231 1.1504E-005 5.0324 80 4.2791E-007 5.0075 3.4744E-007 5.0493

![image 61](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile61.png>)

![image 62](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile62.png>)

![image 63](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile63.png>)

![image 64](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile64.png>)

![image 65](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile65.png>)

![image 66](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile66.png>)

![image 67](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile67.png>)

![image 68](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile68.png>)

![image 69](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile69.png>)

![image 70](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile70.png>)

![image 71](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile71.png>)

160 1.3354E-008 5.0018 1.0644E-008 5.0286 320 4.1722E-010 5.0003 3.2940E-010 5.0140 640 1.3039E-011 4.9998 1.0250E-011 5.0060

![image 72](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile72.png>)

![image 73](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile73.png>)

![image 74](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile74.png>)

![image 75](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile75.png>)

![image 76](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile76.png>)

![image 77](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile77.png>)

1280 4.5156E-013 4.8517 3.5536E-013 4.8502

![image 78](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile78.png>)

- Table 1: Accuracy test for the advection of density perturbation by the fourth-order GKS. mesh L1 error convergence order L2 error convergence order

![image 79](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile79.png>)

![image 80](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile80.png>)

![image 81](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile81.png>)

![image 82](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile82.png>)

20 4.5797E-004 3.7856E-004 40 1.3994E-005 5.0322 1.1735E-005 5.0116 80 1.0709E-006 3.7078 8.5971E-007 3.7708

![image 83](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile83.png>)

![image 84](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile84.png>)

![image 85](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile85.png>)

![image 86](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile86.png>)

![image 87](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile87.png>)

![image 88](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile88.png>)

160 2.5659E-007 2.0613 2.0167E-007 2.0918 320 6.4243E-008 1.9978 5.0455E-008 1.9989

![image 89](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile89.png>)

![image 90](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile90.png>)

![image 91](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile91.png>)

![image 92](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile92.png>)

![image 93](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile93.png>)

- Table 2: Accuracy test for the advection of density perturbation by the second-order GKS. mesh L1 error convergence order L∞ error convergence order

![image 94](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile94.png>)

![image 95](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile95.png>)

![image 96](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile96.png>)

![image 97](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile97.png>)

20×20 1.98E-3 3.79E-2 40×40 1.69E-4 3.55 8.08E-3 2.23 80×80 8.92E-6 4.24 4.10E-4 4.30

![image 98](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile98.png>)

![image 99](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile99.png>)

![image 100](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile100.png>)

![image 101](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile101.png>)

![image 102](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile102.png>)

![image 103](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile103.png>)

160×160 2.31E-7 5.27 5.29E-6 6.28 320×320 7.40E-9 4.96 2.09E-7 4.66 640×640 2.76E-10 4.74 7.09E-9 4.88

![image 104](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile104.png>)

![image 105](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile105.png>)

![image 106](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile106.png>)

![image 107](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile107.png>)

![image 108](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile108.png>)

![image 109](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile109.png>)

![image 110](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile110.png>)

- Table 3: Accuracy of the fourth-order GKS for the isentropic vortex propagation at time t = 10


y directions. The exact solution is the perturbation which propagates with the velocity (1, 1). The L1 and L∞ errors and orders at t = 10 with N × N uniform mesh cells are presented in Table 3, which shows that the expected accuracy can be also achieved for the two dimensional computation.

- 4.2. One dimensional Riemann problems For one-dimensional case, two Riemann problems are considered. The ﬁrst one is the


Sod problem. The computational domain is [0, 1] with 100 uniform mesh points and with non-reﬂected boundary condition on both ends. The initial condition is given by

(ρ, U, p) =

(1, 0, 1), 0 < x < 0.5, (0.125, 0, 0.1), 0.5 < x < 1.

- 0

- 1

- 2

- 3

- 4

- 5

- 6

- 7


- 0.8

- 1


exact solution 200 cells 400 cells

exact solution 100 cells

density

density

0.6

0.4

0.2

0.2 0.4 0.6 0.8

20 40 60 80 100

x

x

14

| | | | |
|---|---|---|---|
| | | | |


exact solution 100 cells

exact solution 200 cells 400 cells

0.8

12

10

0.6

8

velocity

velocity

0.4

6

4

0.2

2

0

0

0.2 0.4 0.6 0.8

20 40 60 80 100

x

x

- 0.8

- 1


400

exact solution 200 cells 400 cells

exact solution 100 cells

300

pressure

pressure

0.6

200

0.4

100

0.2

0.2 0.4 0.6 0.8

20 40 60 80 100

x

x

Figure 1: Sod problem (left): the density, velocity and pressure distributions at t=0.2 with 100 cells, and blast wave problem (right): the density, velocity and pressure distributions at t = 3.8 with 200 and 400 cells.

- 0

- 1

- 2

- 3

- 4

- 5


- 2.5

- 3

- 3.5

- 4


- 4.5

- 5


| | |
|---|---|
| | |


| | |
|---|---|


| | |
|---|---|


| | |
|---|---|
| | |


| | |
|---|---|


| | |
|---|---|
| | |


| | |
|---|---|


| | |
|---|---|
| | |


| | |
|---|---|
| | |


| | |
|---|---|


| | |
|---|---|


| | |
|---|---|
| | |


| |
|---|
| |


| |
|---|
| |


density

density

| | |
|---|---|
| | |


| | |
|---|---|
| | |


| | |
|---|---|
| | |


exact solution 400 cells

###### exact solution 400 cells

-4 -2 0 2 4

0 0.5 1 1.5 2 2.5

x

x

Figure 2: Shu-Osher shock acoustic-wave interaction. Density distributios at t = 1.8 with 400 cells.

The second one is the Woodward-Colella blast wave problem [33]. The computational domain is [0, 100] with 200 and 400 uniform mesh points. The reﬂected boundary conditions are imposed on both ends. The initial conditions are given as follows,

(ρ, U, p) =   

(1, 0, 1000), 0 ≤ x < 10, (1, 0, 0.01), 10 ≤ x < 90, (1, 0, 100), 90 ≤ x ≤ 100.

The density, velocity, and pressure distributions for the fourth-order GKS and the exact solutions are presented in Fig.1 for the Sod problem at t = 0.2 and for the blast wave problem at t = 3.8. The numerical results agree well with the exact solutions. The scheme can resolve the wave proﬁles well, particularly for the local extreme values.

In the one-dimensional case, another standard test case is the Shu-Osher shock acoustic interaction [30]. The computational domain is [−5, 5] and the ﬂow ﬁeld is initialized as

(ρ, U, p) =

(3.857134, 2.629369, 10.33333), x ≤ −4, (1 + 0.2 sin(5x), 0, 1), −4 < x.

The computed density proﬁle with 400 mesh points at t = 1.8 is shown in Fig.2.

The stability for the current scheme is tested by the Sod problem. The velocity proﬁles with diﬀerent CFL numbers from 0.2 to 0.7, are shown in Fig.3. The scheme is basically stable under the conventional CFL condition. The waves proﬁles can be well resolved at a CFL number around 0.5. In the following numerical tests, without spacial statement, the CFL number takes a ﬁxed value of 0.4.

- 4.3. Two-dimensional Riemann problems


In the following, two examples of two-dimensional Riemann problems are considered, which involve the interactions of shocks, the interaction of shocks with vortex sheets, and

- 0.8

- 1


0.9

velocity

0.6

velocity

###### CFL=0.7 CFL=0.6 CFL=0.5 CFL=0.4 CFL=0.2

0.8

0.4

0.2

0.7

0

0.2 0.4 0.6 0.8

0.5 0.6 0.7 0.8

x

x

Figure 3: The stability test for the Sod problem.

the interaction of vortices [17, 20, 11]. The computational domain is [0, 1] × [0, 1], and the non-reﬂecting boundary conditions are used in all boundaries. The initial conditions for the ﬁrst problem are

 

(1.5, 0, 0, 1.5), x > 0.5, y > 0.5, (0.5323, 1.206, 0, 0.3), x < 0.5, y > 0.5, (0.138, 1.206, 1.206, 0.029), x < 0.5, y < 0.5, (0.5323, 0, 1.206, 0.3), x > 0.5, y < 0.5.

(ρ, U, V, p) =



Four initial shock waves interact with each other and result in a more complicated pattern. The density distribution and the local enlargement are given at t = 0.4 in Fig.4 with 400×400 and 800 × 800 mesh points. From the analysis in [17], the initial shock wave S23− bifurcates at the trip point into a reﬂected shock wave, a Mach stem, and a slip line. The reﬂected shock wave interacts with the shock wave S12− to produce a new shock. The small scale ﬂow structures are well captured by the current scheme. The initial conditions for the second case are

 

(1, 0.1, 0.1, 1), x > 0.5, y > 0.5, (0.5197, −0.6259, 0.1, 0.4), x < 0.5, y > 0.5, (0.8, 0.1, 0.1, 0.4), x < 0.5, y < 0.5, (0.5197, 0.1, −0.6259, 0.4), x > 0.5, y < 0.5.

(ρ, U, V, p) =



This case is to simulate the interaction of the rarefaction waves and the vortex-sheets. The density distribution at t = 0.4 and the local enlargement are given in Fig.5 with 600 × 600 and 1000 × 1000 mesh points. The roll-up is well captured by the current scheme.

On the computational cost, the above two-dimensional Riemann problems are tested again. As a reference, the CPU times for diﬀerent schemes are obtained with 100×100 cells and 10 time steps with Intel Core i7-4770 CPU @ 3.40GHz. Based on the same WENO reconstruction, the CPU times for the second-order GKS [34], the single stage third-order

0.5

0.8

0.4

0.6

y

y

0.3

0.4

0.2

0.2

0.2 0.4 0.6 0.8

0.2 0.3 0.4 0.5

x

x

0.5

0.8

0.4

0.6

y

### x y

0.3

0.4

0.2

0.2

0.2 0.4 0.6 0.8

0.2 0.3 0.4 0.5

x

- Figure 4: The density distribution for the ﬁrst two-dimensional Riemann problem at t = 0.3 with 400× 400 (top) and 800 × 800 (bottom) mesh points.


GKS [21, 24], and the current two-stage fourth-order GKS are given in Table 4, where both conservative and characteristic reconstructions are used.

![image 111](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile111.png>)

![image 112](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile112.png>)

variable 2nd-order GKS 3rd-order GKS 4th-order GKS conservative 0.704893s 1.24681s 1.95370s

![image 113](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile113.png>)

![image 114](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile114.png>)

![image 115](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile115.png>)

characteristic 0.842873s 1.38178s 2.20566s

![image 116](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile116.png>)

Table 4: The test of the computational cost for diﬀerent schemes.

For the fourth-order GKS, the computational cost is about 3 times of that of second-

0.6

0.8

0.5

0.6

y

y

0.4

0.4

0.3

0.2

0.2

0.2 0.4 0.6 0.8 1

0.2 0.3 0.4 0.5 0.6

x

x

0.6

0.8

0.5

0.6

y

### x y

0.4

0.4

0.3

0.2

0.2

0.2 0.4 0.6 0.8 1

0.2 0.3 0.4 0.5 0.6

x

- Figure 5: The density distribution for the second two-dimensional Riemann problem at t = 0.25 with 600 × 600 (top) and 1000 × 1000 (bottom) mesh points.


order scheme. Since the fourth-order GKS has three Gauss points for ﬂux evaluation and two stages, the three times computational time diﬀerence means that the reconstruction makes great contribution to the computational cost as well, because in terms of reconstruction cost the fourth-order scheme only takes about two times of computational cost of second-order scheme. However, in order to get the same accuracy as that of the fourth-order scheme, the second-order method needs reﬁne the mesh, at least once. In the two-dimensional calculation, the computational cost for one mesh reﬁnement will be increased by 8 times. Therefore, the fourth-order scheme is more eﬃcient than the second order method. Since higher-order scheme does have advantages in comparison with lower order method, it is

worth to construct the two-stage ﬁfth-order GKS from the third-order GKS ﬂux function, see Appendix. Besides the computational cost, another important property of the fourthorder GKS is its accuracy and robustness. As tested in the above cases and all cases in the following, it clearly indicates that the fourth-order scheme is very accurate and is as robust

- as the second-order one. The accuracy of the scheme is closely related to the higher-order gas evolution model, multi-dimensionality for the inclusion of both normal and tangential derivatives around a cell interface, and the uniﬁed treatment of the inviscid and viscous terms. A fundamental reason for the robustness of the scheme is its ﬁrst-order relaxation model, where the system is fully hyperbolic with local source term.


- 4.4. Shock vortex interaction

The interaction between a stationary shock and a vortex for the inviscid ﬂow [14] is presented. The computational domain is taken to be [0, 2] × [0, 1]. A stationary Mach 1.1 shock is positioned at x = 0.5 and normal to the x-axis. The left upstream state is (ρ, U, V, p) = (Ma2, √γ, 0, 1), where Ma is the Mach number. A small vortex is obtained through a perturbation on the mean ﬂow with the velocity (U, V ), temperature T = p/ρ, and entropy S = ln(p/ργ). The perturbation is expressed as

![image 117](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile117.png>)

(δU, δV ) = κηeµ(1−η

2)(sinθ, −cos θ), δT = −

(γ − 1)κ2 4µγ

![image 118](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile118.png>)

e2µ(1−η

2), δS = 0,

where η = r/rc, r = (x − xc)2 + (y − yc)2, and (xc, yc) = (0.25, 0.5) is the center of the vortex. Here κ indicates the strength of the vortex, µ controls the decay rate of the vortex, and rc is the critical radius for which the vortex has the maximum strength. In the computation, κ = 0.3, µ = 0.204, and rc = 0.05. The reﬂected boundary conditions are used on the top and bottom boundaries. The pressure distributions with mesh size ∆x = ∆y = 1/200 at t = 0, 0.3, 0.6 and 0.8 are shown in Fig.6. By t = 0.8, one branch of the shock bifurcations has reached the top boundary and been reﬂected. The reﬂection is well captured. The detailed density distributions along the center horizontal line with mesh size ∆x = ∆y = 1/50, 1/100 and 1/200 at t = 0.8 are shown in Fig.7. The accuracy of the scheme is well demonstrated.

![image 119](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile119.png>)

- 4.5. Double Mach reﬂection problem This problem was extensively studied by Woodward and Colella [33] for the inviscid


ﬂow. The computational domain is [0, 4] × [0, 1], and a solid wall lies at the bottom of the computational domain starting from x = 1/6. Initially a right-moving Mach 10 shock is positioned at (x, y) = (1/6, 0), and makes a 60◦ angle with the x-axis. The initial pre-shock and post-shock conditions are

√

![image 120](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile120.png>)

(ρ, U, V, p) = (8, 4.125

3, −4.125, 116.5), (ρ, U, V, p) = (1.4, 0, 0, 1).

0.8

0.8

0.6

0.6

y

y

0.4

0.4

0.2

0.2

0.3 0.6 0.9 1.2

0.3 0.6 0.9 1.2

x

x

0.8

0.8

0.6

0.6

y

y

0.4

0.4

0.2

0.2

0.3 0.6 0.9 1.2

0.3 0.6 0.9 1.2

x

x

- Figure 6: Shock vortex interaction: the pressure distribution at t = 0,0.3,0.6 and 0.8 with mesh size ∆x = ∆y = 1/200.

x

density

0 0.5 1 1.5 2

1.2

1.25

1.3

1.35

1.4

1.45

∆x=∆y=1/50 ∆x=∆y=1/100 ∆x=∆y=1/200

- Figure 7: Shock vortex interaction: the density distribution at t = 0.8 along the horizontal symmetric line y = 0.5 with mesh size ∆x = ∆y = 1/50,1/100 and 1/200.


The reﬂective boundary condition is used at the wall, while for the rest of bottom boundary, the exact post-shock condition is imposed. At the top boundary, the ﬂow values are set to describe the exact motion of the Mach 10 shock. The density distributions with 720 × 240 and 1440 × 480 uniform mesh points at t = 0.2 are shown in Fig.8 and Fig.9, respectively. The current scheme resolves the ﬂow structure under the triple Mach stem clearly. The

- 0.8

- 1


0.6

y

0.4

0.2

0 0.5 1 1.5 2 2.5 3

x

- 0.8

- 1


0.6

y

0.4

0.2

0 0.5 1 1.5 2 2.5 3

x

- Figure 8: Double Mach reﬂection: density contours with the 720 × 240 (top) and 1440 × 480 (bottom) mesh points.

x

y

2.2 2.4 2.6 2.8

0

0.2

0.4

0.6

x

y

2.2 2.4 2.6 2.8

0

0.2

0.4

0.6

- Figure 9: Double Mach reﬂection: enlarged density distributions around the triple point with the 720× 240 (left) and 1440 × 480 (right) mesh points.


amplitude of the oscillation of the slip line from the triple point is not as large as that from many other higher-order schemes, because the GKS is intrinsically solving the NS equations and the physical dissipation will stabilize the shear instability.

- 4.6. Hypersonic ﬂow past a cylinder In this case, the hypersonic ﬂows impinging on a unit cylinder are tested to validate


robustness of the current scheme. The ﬁrst one the the inviscid ﬂow, which were also studied in [19] as comparison between GRP and GKS. This problem is initialized by the ﬂow moving towards to a cylinder with diﬀerent Mach numbers. The reﬂective boundary condition is imposed on the surface of cylinder, and the outﬂow boundary condition is set on the right boundary. In the computation, the 60 × 100 mesh points are used, which is

###### Ma=5 Ma=10 Ma=20

- Figure 10: Hypersonic inviscid ﬂow past a cylinder: the Mach number distributions for the ﬂow with Mach number Ma = 5, 10 and 20.


shown in Fig.10. The Mach number distributions for the ﬂows with Ma = 5, 10, and 20 are also presented in Fig.10, which show that the current scheme can capture strong shocks very well without carbuncle phenomenon [27]. The robustness of the scheme is well validated.

The viscous and heat conducting case at high Mach number is also tested. The ﬂow condition is given as Ma∞ = 8.03, T∞ = 124.94K for the far ﬁeld, the wall temperature is TW = 294.44K, and the Reynolds number is Re = 1.835 × 105 with cylinder radius and the far ﬁeld ﬂow parameters. This test case is taken from the experiment done by Wieting [32]. A non-uniform mesh of 60×160 cells is used with the near-wall cell width of 1/2000 to resolve the boundary layer. The mesh, pressure, temperature, and Mach number distributions are given in Fig.11. The pressure and heat ﬂux along the cylindrical surface are presented in Fig.12, where the numerical results agree well with the experimental data [32].

- 4.7. Laminar boundary layer A laminar boundary layer is tested over a ﬂat plate. The Mach number of the free-


stream is Ma = 0.15 and the Reynolds number is Re = U∞L/ν = 105, ν is the viscous coeﬃcient. The non-slip adiabatic boundary condition at the plate is used and a symmetric condition is imposed at the bottom boundary before the ﬂat plate. The non-reﬂecting boundary condition based on the Riemann invariants is adopted for the other boundaries. A uniform mesh 260× 90 points is adopted with ∆x = ∆y = 1/200, including 60× 90 mesh points before the plate. At steady state, the non-dimensional U and V velocity at diﬀerent locations are presented in Fig.13, as well as the wall friction coeﬃcient. In all locations, the numerical solutions match with the exact Blasius solution very well. At the upstream location, the boundary layer proﬁle can be accurately captured with only four grid points within the layer.

###### pressure temperature Mach number

- Figure 11: Hypersonic viscous ﬂow past a cylinder with Ma = 8.03: the mesh, pressure, temperature, and Mach number distributions.

angel (θ)

pressurep/p0

-50 0 50

0

0.2

0.4

0.6

- 0.8

- 1


1.2

fourth-order GKS experiment data

| | |
|---|---|
| | |


| | |
|---|---|
| | |


| | |
|---|---|


| | |
|---|---|
| | |


| | |
|---|---|
| | |
| | |


| | |
|---|---|
| | |


angel (θ)

heatfluxq/q0

-50 0 50

0

0.2

0.4

0.6

- 0.8

- 1


1.2

fourth-order GKS experiment data

- Figure 12: Hypersonic viscous ﬂow past a cylinder with Ma = 8.03. Comparison of the computed pressure and heat ﬂux along the cylindrical surface with the experimental data [32].


- 4.8. Lid-driven cavity ﬂow In order to further test the scheme in the capturing of vortex ﬂow, the lid-driven cavity


problem is one of the most important benchmarks for validating incompressible low speed Navier-Stokes ﬂow solvers. The ﬂuid is bounded by a unit square and is driven by a uniform translation of the top boundary. In this case, the ﬂow is simulated with Mach number Ma = 0.15 and all boundaries are isothermal and nonslip. The computational domain [0, 1] × [0, 1] is covered with 65 × 65 mesh points. Numerical simulations are conducted for two diﬀerent Reynolds numbers, i.e., Re = 1000 and 3200. The streamlines in Fig.14, the U-velocities along the center vertical line, and V -velocities along the center horizontal line, are shown in Fig.15. The benchmark data [9] for Re = 1000 and 3200 are also presented, and the simulation results match well with these benchmark data. The higher-order accuracy

- 0.8

- 1


+ + + + + +

- 0.8

- 1


+ + + +

+

+

+

+

+

+

0.6

+

|1/2νV/(U/x)∞|
|---|


1/2νV/(U/x)∞

0.6

U/U∞

|U/U∞|
|---|


+

Rex= 975 Rex= 2475 Rex= 5975 Blasius

Rex= 975 Rex= 2475 Rex= 5975 Blasius

0.4

+

0.4

+

+

+

+

0.2

0.2

+

+

+

0

0

0 2 4 6 8

0 2 4 6 8

y/(νx/U∞)1/2

y/(νx/U∞)1/2

Present Blasius

10-1

cf

10-2

101 102 103 104

Rex

- Figure 13: Laminar boundary layer: the U and V velocity proﬁles at diﬀerent locations and wall friction coeﬃcient distribution.

of the scheme is clearly demonstrated from the Reynolds number 3200 case, where only 65 uniform mesh points are used in each direction.

x y

0.2 0.4 0.6 0.8

0.2

0.4

0.6

0.8

x

y

0.2 0.4 0.6 0.8

0.2

0.4

0.6

0.8

- Figure 14: Lid-driven cavity ﬂow: the streamlines with 65 × 65 mesh points from the fourth-order GKS at Re = 1000 (left) and 3200 (right).


1.2

0.6

##### ∆x=∆y=1/65 Ghia’s data

##### ∆x=∆y=1/65 Ghia’s data

0.9

0.3

0.6

0

u

v

###### Re=1000

0.3

Re=1000

0

- -0.6

- -0.3


-0.3

0 0.2 0.4 0.6 0.8 1

0 0.2 0.4 0.6 0.8 1

y

x

1.2

0.6

##### ∆x=∆y=1/65 Ghia’s data

##### ∆x=∆y=1/65 Ghia’s data

0.9

0.3

0.6

0

u

v

###### Re=3200

0.3

###### Re=3200

0

- -0.6

- -0.3


-0.3

0 0.2 0.4 0.6 0.8 1

0 0.2 0.4 0.6 0.8 1

y

x

- Figure 15: Lid-driven cavity ﬂow: U-velocity along vertical centerline line and V -velocity along horizontal centerline with 65 mesh points in each direction from the fourth-order GKS at Re = 1000 and 3200.


- 4.9. Viscous shock tube problems


This problem was introduced to test the performances of diﬀerent schemes for viscous ﬂows [7]. In this case, an ideal gas is at rest in a two-dimensional unit box [0, 1] × [0, 1]. A membrane located at x = 0.5 separates two diﬀerent states of the gas and the dimensionless initial states are

(120, 0, 120/γ), 0 < x < 0.5, (1.2, 0, 1.2/γ), 0.5 < x < 1,

(ρ, U, p) =

where γ = 1.4 and Prandtl number Pr = 0.73. Scheme AUSMPW+ M-AUSMPW+ fourth-order GKS

![image 121](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile121.png>)

![image 122](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile122.png>)

height 0.163 0.168 0.171

![image 123](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile123.png>)

Table 5: Comparison of the heights of primary vortex among gas kinetic scheme and other reference methods [15] for the reﬂecting shock-boundary layer interaction with ∆x = ∆y = 1/500.

0.3

fourth-order GKS ∆x=∆x=1/500

0.2

y

0.1

h

0.4 0.6 0.8

x

0.3

###### fourth-order GKS ∆x=∆x=1/750

0.2

y

0.1

0.4 0.6 0.8

x

- Figure 16: Reﬂecting shock-boundary layer interaction: density distributions at t = 1 with Re = 200 from the fourth-order GKS with ∆x = ∆y = 1/500,1/750.

x

density

0.4 0.6 0.8 1

40

60

80

100

120

fourth-order GKS ∆x=∆y=1/500 fourth-order GKS ∆x=∆y=1/750

- Figure 17: Reﬂecting shock-boundary layer interaction: density distribution along the lower wall with diﬀerent mesh sizes for Re = 200.


The membrane is removed at time zero and wave interaction occurs. A shock wave, followed by a contact discontinuity, moves to the right with Mach number Ma = 2.37 and reﬂects at the right end wall. After the reﬂection, it interacts with the contact discontinuity. The contact discontinuity and shock wave interact with the horizontal wall and create a thin boundary layer during their propagation. The solution will develop complex two-dimensional shock/shear/boundary-layer interactions. This case is tested in the computational domain [0, 1] × [0, 0.5], a symmetric boundary condition is used on the top boundary x ∈ [0, 1], y = 0.5, and non-slip boundary condition, and adiabatic condition for temperature are imposed

- at solid wall boundaries. The case with Re = 200 is tested ﬁrst. The density distributions are presented in Fig.16 with two diﬀerent mesh resolutions. The results match well with


0.3

#### fourth-order GKS ∆x=∆x=1/1500

0.2

y

0.1

0.4 0.6 0.8

x

0.3

#### fourth-order GKS ∆x=∆x=1/2000

0.2

y

0.1

0.4 0.6 0.8

x

- Figure 18: Reﬂecting shock-boundary layer interaction. The density distribution at t = 1 with Re = 1000 with ∆x = ∆y = 1/1500 and 1/2000.

x

density

0.4 0.6 0.8 1

20

40

60

80

100

120

fourth-order ∆x=∆y=1/1500 fourth-order ∆x=∆y=1/2000

- Figure 19: Reﬂecting shock-boundary layer interaction: density distribution along the lower wall with diﬀerent mesh sizes for Re = 1000.


each other. The density proﬁles along the lower wall with Re = 200 are also presented in Fig.19. A mesh-convergent solution is observed for Re = 200. As shown in Table.5, the height of primary vortex predicted by the current scheme agrees well with the reference data [15]. For the case with Re = 1000, the ﬂow structure becomes more complicated. The density distributions from the current scheme are given in Fig.18, and the density proﬁles along the lower wall are presented in Fig.19 with the mesh size ∆x = ∆y = 1/1500 and 1/2000. The ﬂow structure is complicated, and the mesh convergence is basically obtained with the mesh size decreasing to 1/1500. The current results agree well with the reference data very well. More studies for this problem can be found in [7].

5. Conclusion

In this paper, based on the two-stage time stepping method a fourth-order gas-kinetic scheme is proposed for both inviscid and viscous ﬂow computations. With the ﬁfth-order WENO reconstruction, a GKS with a ﬁfth order accuracy in space and a fourth order accuracy in time is developed. In comparison with the classical methods based on the ﬁrstorder Riemann solver, for a fourth-order accuracy in time the current GKS only uses two stages instead of four stages in the conventional methods. Therefore, the current GKS should be much more eﬃcient than these higher-order methods based on the Riemann solutions, especially for the NS solutions. The current ﬁnite volume scheme can use a CFL number on the order of 0.5. The further development of the GKS to even higher-order accuracy can be achieved with the inclusion of the second-order time derivative of the ﬂux function, such as the ﬁfth-order scheme presented in the Appendix. The fourth-order GKS not only has the expected order of accuracy for the smooth ﬂow, but also has favorable shock capturing property for the discontinuous solutions. Most importantly, the numerical tests clearly demonstrate that the current fourth-order scheme is as robust as the second-order one.

By taking advantage of the time-accurate gas evolution model in the ﬂux evaluation, an eﬃcient and accurate fourth-order gas-kinetic scheme has been constructed. The advantage of the time accurate evolution model can be further explored for the construction of higherorder compact schemes [25, 26], where not only the ﬂux at the cell interface, the conservative ﬂow variables at the cell interface can be updated as well to construct compact stencils for the ﬂow reconstruction in the next time level. Based on the current study, we can conclude that the adaptation of a higher-order gas evolution model for the ﬂux evaluation has an indispensable advantage in the development of higher-order schemes. The real bottleneck which hinders the progress for the development of higher-order accurate and robust schemes for the compressible ﬂows is due to the use of ﬁrst-order Riemann solver.

Acknowledgements

The research of K. Xu is supported by Hong Kong Research Grant Council (620813, 16211014, 16207715) and HKUST research fund (PROVOST13SC01, IRS15SC29, SBI14SC11). The research of Q. Li is partially supported by NSFC (11172154). The work of J. Li is supported by NSFC (91130021, 11371063), and the doctoral program from the Education Ministry of China (20130003110004).

Appendix: Extension to higher order

The key point for developing a two-stage fourth-order temporal accurate schemes is the use of a time-dependent ﬂux function. The third-order GRP and GKS have both ﬁrst- and second-order time derivatives in the ﬂux function [28, 21, 24, 25]. Thus, with a two-stage temporal discretization and the third-order GRP and GKS ﬂux solvers, it is possible to develop schemes with ﬁfth-order accuracy in time.

We consider the time-dependent equation Eq.(1) with the initial condition Eq.(2). Introducing an intermediate state at t∗ = tn + A∆t,

w∗ = wn + A∆tL(wn) +

1 6

∂ ∂tL(wn) +

- 1

![image 124](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile124.png>)

- 2


A2∆t2

![image 125](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile125.png>)

![image 126](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile126.png>)

∂2 ∂t2L(wn), (17)

A3∆t3

![image 127](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile127.png>)

∂2 ∂t2L(w∗) at t∗. Then, the update scheme can be written

∂ ∂tL(w∗) and

we will have L(u∗),

![image 128](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile128.png>)

![image 129](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile129.png>)

as

∂ ∂tL(wn) + C1

∂ ∂tL(w∗)

- 1

![image 130](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile130.png>)

- 2


∆t2 C0

wn+1 = wn + ∆t(B0L(wn) + B1L(w∗)) +

![image 131](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile131.png>)

![image 132](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile132.png>)

∂2 ∂t2L(wn) + D1

∂2 ∂t2L(w∗) . (18)

1 6

∆t3 D0

+

![image 133](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile133.png>)

![image 134](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile134.png>)

![image 135](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile135.png>)

It can be proved that Eq.(17) and Eq.(18) can provide a ﬁfth-order temporal accurate approximation to the solution w(t) at t = tn + ∆t with the following coeﬃcients

2 5

, B0 = 1, B1 = 0, C0 = 1, C1 = 0, D0 =

A =

![image 136](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile136.png>)

3 8

, D1 =

![image 137](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile137.png>)

5 8

. (19)

![image 138](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile138.png>)

To prove this proposition, the following equation needs to be satisﬁed, using the same approach as in [18],

wn+1 = wn +

tn+∆t

L(w(t))dt + O(∆t6).

tn

According to the Taylor expansion of the operator L at tn, the integral can be expressed as

tn+∆t

∆t2 2

∆t3 6

∆t4 24

∆t5 120

∂2L ∂t2

∂3L ∂t3

∂4L ∂t4

∂L ∂t

+ O(∆t6), (20)

L(w(t))dt = ∆tL +

+

+

+

![image 139](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile139.png>)

![image 140](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile140.png>)

![image 141](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile141.png>)

![image 142](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile142.png>)

![image 143](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile143.png>)

![image 144](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile144.png>)

![image 145](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile145.png>)

![image 146](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile146.png>)

tn

where the time derivatives for the operator L can be given by the chain rule, for example

∂2L ∂t2

∂L ∂t

= L2wL + LwwL2, ...

= LwL,

![image 147](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile147.png>)

![image 148](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile148.png>)

∂2 ∂t2L(w), and expand L(w), G(w) and H(w) in the

∂ ∂tL(w) and H(w) =

Denote G(w) =

![image 149](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile149.png>)

![image 150](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile150.png>)

neighboring of u∗ to the corresponding order, we have

(w∗ − wn)2 + Lwww 6

(w∗ − wn)3 + Lwwww 24

L(w∗) = L(wn) + Lw(w∗ − wn) + Lww 2

(w∗ − wn)4,

![image 151](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile151.png>)

![image 152](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile152.png>)

![image 153](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile153.png>)

- G(w∗) = G(wn) + Gw(w∗ − wn) + Gww 2

![image 154](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile154.png>)

(w∗ − wn)2 + Gwww 6

![image 155](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile155.png>)

(w∗ − wn)3,

- H(w∗) = H(wn) + Hw(w∗ − wn) + Hwww 2


(w∗ − wn)2,

![image 156](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile156.png>)

where obvious higher order terms are ignored, w∗ is given by Eq.(17). Substituting L(w∗), G(w∗), H(w∗) into Eq.(18) and comparing the coeﬃcients of Eq.(20), a system of equations will be obtained, and Eq.(19) is its unique solution for this system.

To develop the gas-kinetic scheme with ﬁfth-order temporal accuracy, the time-dependent ﬂux should by approximated by the quadratic function, which is expressed as follows

Fi+1/2(Wn, t) = Fin+1/2 + ∂tFin+1/2t +

- 1

![image 157](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile157.png>)

- 2


∂ttFin+1/2t2. (21)

In a time step, the coeﬃcients Fin+1/2, ∂tFjn+1/2 and ∂ttFin+1/2 can be determined as follows

- 1

![image 158](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile158.png>)

- 2


1 6

∂tFi+1/2∆t2 +

∂ttFi+1/2∆t3 = Fi+1/2(Wn, ∆t),

Fi+1/2∆t +

![image 159](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile159.png>)

2 9

4 81

2 3

∂tFi+1/2∆t2 +

∂ttFi+1/2∆t3 = Fi+1/2(Wn, 2∆t/3),

Fi+1/2∆t +

![image 160](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile160.png>)

![image 161](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile161.png>)

![image 162](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile162.png>)

1 3

1 18

1 162

∂ttFi+1/2∆t3 = Fi+1/2(Wn, ∆t/3), where

∂tFi+1/2∆t2 +

Fi+1/2∆t +

![image 163](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile163.png>)

![image 164](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile164.png>)

![image 165](<2016-pan-efficient-accurate-two-stage-fourth-order_images/imageFile165.png>)

Fi+1/2(Wn, δ) =

tn+δ

tn

uf(xi+1/2, t, u, v, ξ)dudξdt.

The formulation for the gas distribution f(xi+1/2, t, u, v, ξ) can be found in [21, 24, 25]. By solving the linear system, all coeﬃcients can be determined.

References

- [1] M. Ben-Artzi, J. Falcovitz, A second-order Godunov-type scheme for compressible uid dynamics, J. Comput. Phys. 55 (1984), 1-32.
- [2] M. Ben-Artzi, J. Li, G. Warnecke, A direct Eulerian GRP scheme for compressible uid ows, J. Comput. Phys. 218 (2006), 19-43.
- [3] M. Ben-Artzi, J. Li, Hyperbolic conservation laws: Riemann invariants and the generalized Riemann problem, Numerische Mathematik, 106 (2007) 369-425.
- [4] P.L. Bhatnagar, E.P. Gross, M. Krook, A Model for Collision Processes in Gases I: Small Amplitude Processes in Charged and Neutral One-Component Systems, Phys. Rev. 94 (1954) 511-525.
- [5] S. Chapman, T.G. Cowling, The Mathematical theory of Non-Uniform Gases, third edition, Cambridge University Press, (1990).
- [6] B. Cockburn, C. W. Shu, Runge-Kutta Discontinuous Galerkin Methods for Convection-Dominated Problems, Journal of Scientiﬁc Computing, Vol. 16 (2001), No. 3, pp. 173-261.
- [7] V. Daru, C. Tenaud, Numerical simulation of the viscous shock tube problem by using a high resolution monotonicity-preserving scheme, Computers & Fluids 38 (2009) 664-676.
- [8] M. Dumbser, D.S. Balsara, E.F. Toro, C.D. Munz, A uniﬁed framework for the construction of one-step ﬁnite volume and discontinuous Galerkin schemes on unstructured meshes, J. Comput. Phys. 227 (2008) 8209-8253.
- [9] U. Ghia, K. N. Ghia, C.T Shin, High-Re solutions for incompressible ﬂow using the Navier-Stokes equations and a multigrid method, J. Comput. Phys. 48 (1982) 387-411.
- [10] S. Gottlieb, C. W. Shu, Total variation diminishing runge-kutta schemes, Mathematics of computation, 67 (1998) 73-85.


- [11] E. Han, J. Li and H. Tang, Accuracy of the adaptive GRP scheme and the simulation of 2-D Riemann problem for compressible Euler equations, Comm. Comput. Phys., Vol. 10 (2011), 577-606.
- [12] A. Harten, B. Engquist, S. Osher and S. R. Chakravarthy, Uniformly high order accurate essentially non-oscillatory schemes, III. J. Comput. Phys. 71 (1987) 231-303.
- [13] S. Ii and F. Xiao, High order multi-moment constrained ﬁnite volume method. Part I: Basic formulation, J. Comput. Phys. 228 (2009), pp. 3669C3707.
- [14] G.S. Jiang, C. W. Shu, Eﬃcient implementation of Weighted ENO schemes, J. Comput. Phys. 126

(1996) 202-228.

- [15] K.H. Kim, C. Kim, Accurate, eﬃcient and monotonic numerical methods for multi-dimensional compressible ﬂows Part I: Spatial discretization, J. Comput. Phys. 208 (2005) 527-569.
- [16] G. Kumar, S.S. Girimaji, J. Kerimo, WENO-enhanced gas-kinetic scheme for direct simulations of compressible transition and turbulence, J. Comput. Phys. 234 (2013) 499-523.
- [17] P. D. Lax, X.D. Liu, Solution of two-dimensional riemann problems of gas dynamics by positive schemes, SIAM J. Sci. Comput. 19 (1998) 319-340.
- [18] J. Li, Z. Du, A two-stage fourth order time-accurate discretization for Lax-Wendroﬀ type ﬂow solvers

I. hyperbolic conservation laws, preprint, http://arxiv.org/abs/1512.03664, 2015.

- [19] J. Li, Q. Li, K. Xu, Comparison of the generalized Riemann solver and the gas-kinetic scheme for inviscid compressible ﬂow simulations, J. Comput. Phys. 230 (2011) 5080-5099.
- [20] J. Li, T. Zhang and S. Yang, The Two-dimensional Riemann Problem in Gas Dynamics, Pitmann Monographs and Surveys in Pure and Applied Mathematics 98, Longman Scientiﬁc & Technical, Harlow

(1998).

- [21] Q. Li, K. Xu, S. Fu, A high-order gas-kinetic Navier-Stokes ﬂow solver, J. Comput. Phys. 229 (2010) 6715-6731.
- [22] N. Liu and H.Z. Tang, A high-order accurate gas-kinetic scheme for one- and two-dimensional ﬂow simulation, Commun. Comput. Phys., 15 (2014), 911-943.
- [23] X.D. Liu, S. Osher, T. Chan, Weighted essentially non-oscillatory schemes, J. Comput. Phys. 115 (1994) 200-212.
- [24] J. Luo, K. Xu, A high-order multidimensional gas-kinetic scheme for hydrodynamic equations, SCIENCE CHINA Technological Sciences, 56 (2013) 2370-2384.
- [25] L. Pan, K. Xu, A compact third-order gas-kinetic scheme for compressible Euler and Navier-Stokes equations, Commun. Comput. Phys. 18 (2015) 985-1011.
- [26] L.Pan, K. Xu, A third-order compact gas-kinetic scheme on unstructured meshes for compressible Navier-Stokes solutions, arXiv:1602:003941v1 [math.NA] February (2016).
- [27] M. Pandolﬁ, and D. D’Ambrosio, Numerical Instabilities in Upwind Methods: Analysis and Cures for the “Carbuncle” Phenomenon, J. Comput. Phys. 166 (2001) 271-301.
- [28] J. Qian, J. Li and S. Wang, The generalized Riemann problems for compressible ﬂuid ﬂows: Towards high order, J. Comput. Phys. 259 (2014) 358-389.
- [29] X. Ren, K. Xu, W. Shyy, C. Gu, A multi-dimensional high-order discontinuous Galerkin method based on gas kinetic theory for viscous ﬂow computations, J. Comput. Phys. 292 (2015) 176-193.
- [30] C.W. Shu and S. Osher, Eﬃcient implementation of essentially nonoscillatory shock-capturing schemes II, J. Comput. Phys., 83 (1989), pp. 32-78.
- [31] E. Toro, Riemann Solvers and Numerical Methods for Fluid Dynamics, Springer, (1997).
- [32] A.R. Wieting, Experimental study of shock wave interface heating on a cylindrical leading edge, No. NASA TM-100484 1987.
- [33] P. Woodward and P. Colella, Numerical simulations of two-dimensional ﬂuid ﬂow with strong shocks, J. Comput. Phys. 54 (1984) 115-173.
- [34] K. Xu, A gas-kinetic BGK scheme for the Navier-Stokes equations and its connection with artiﬁcial dissipation and Godunov method, J. Comput. Phys. 171 (2001) 289-335.
- [35] K. Xu, Super-Burnett solutions for Poiseuille ﬂow, Physics of Fluids, Vol. 15 (2003), pp. 2077-2080.
- [36] K. Xu, Direct modeling for computational ﬂuid dynamics: construction and application of unﬁed gas kinetic schemes, World Scientiﬁc (2015).


## [37] K. Xu, Z.H. Li, Microchannel ﬂow in the slip regime: gas-kinetic BGK-Burnett solutions, J. Fluid Mech. 513 (2004) 87-110.

