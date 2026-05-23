arXiv:1512.03664v1[math.NA]11Dec2015

A TWO-STAGE FOURTH ORDER TIME-ACCURATE DISCRETIZATION FOR LAX-WENDROFF TYPE FLOW SOLVERS

I. HYPERBOLIC CONSERVATION LAWS

JIEQUAN LI AND ZHIFANG DU

Abstract. In this paper we develop a novel two-stage fourth order time-accurate discretization for time-dependent ﬂow problems, particularly for hyperbolic conservation laws. Diﬀerent from the classical Runge-Kutta (R-K) temporal discretization for ﬁrst order Riemann solvers as building blocks, the current approach is solely associated with Lax-Wendroﬀ (L-W) type schemes as the building blocks. As a result, a two-stage procedure can be constructed to achieve a fourth order temporal accuracy, rather than using well-developed four stages for R-K methods. The generalized Riemann problem (GRP) solver is taken as a representative of L-W type schemes for the construction of a two-stage fourth order scheme.

Key Words. Lax-Wendroﬀ Method, two-stage fourth order temporal accuracy, hyperbolic conservation laws, GRP solver.

1. Introduction

The design of high order accurate CFD methods has attracted much attention in the past decades. Successful examples include ENO [11, 18, 2], WENO [15, 12], DG [7], residual distribution (RD) method [1], spectral methods [19] etc., and references therein. Most of these methods use the Runge-Kutta (R-K) approach to achieve high order temporal accuracy starting from the ﬁrst order numerical ﬂux functions, such as ﬁrst order Riemann solvers. In order to achieve a fourth order temporal accuracy, four stages of R-K type iterations in time are usually adopted.

In this paper we develop a novel fourth order temporal discretization for time-dependent problems, particularly for hyperbolic conservation laws

- (1.1)


∂u ∂t

+ ∇ · f(u) = 0,

![image 1](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile1.png>)

where u = (u1, · · · , um)⊤ is a conservative vector, f(u) = (f1(u), · · · , fd(u)) is the associated ﬂux vector function, m ≥ 1, d ≥ 1. The approach under investigation is based on the second order Lax-Wendroﬀ (L-W) methodology and uses a two-stage procedure to achieve a fourth order accuracy, which is diﬀerent from the classical R-K approach. This approach can be easily extended to many other time-dependent ﬂow problems [8].

The Lax-Wendroﬀ methodology [13], i.e., the Cauchy-Kovalevskaya method in the context of PDEs, is fundamental in the sense that it has second order accuracy both in space and time, and the underlying governing equations are fully incorporated into approximations of

1

spatial and temporal evolution. In a ﬁnite volume framework, Eq. (1.1) is discretized as

- (1.2) unj+1 = unj −

![image 2](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile2.png>)

![image 3](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile3.png>)

ℓ

∆t |Ωj|

![image 4](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile4.png>)

Fjℓ(u(·, tn +

∆t 2

![image 5](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile5.png>)

), Γjℓ, njℓ)

where unj is the solution averaged over the control volume Ωj at time t = tn, tn+1 = tn + ∆t, Γjℓ is the ℓ-th side of Ωj, and njℓ is the unit outward normal direction. The numerical ﬂux Fjℓ along the time-space surface Γjℓ is based on the half time-step value u(·, t + ∆t/2), or an equivalent approximation. The L-W method achieves the time accuracy through the formulae

![image 6](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile6.png>)

- (1.3)

u(x, tn +

∆t 2

![image 7](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile7.png>)

) = u(x, tn) +

∆t 2 ·

![image 8](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile8.png>)

∂u ∂t

![image 9](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile9.png>)

(x, tn) + O(∆t2), x ∈ Γjℓ,

∂u ∂t

![image 10](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile10.png>)

(x, tn) = −∇ · f(u)(x, tn),

which adopt two instantaneous values u(x, tn) and ∂∂tu(x, tn) at any point (x, tn) on the boundary of a control volume. In particular, the time variation is related to the spatial

![image 11](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile11.png>)

derivatives of the solutions. The ﬁrst order Riemann solvers [9, 21] and second order L-W solvers have distinguishable procedures to deﬁne the two instantaneous values, respectively. The L-W method is a one-stage spatial-temporal coupled second order accurate method, which utilizes the information only at time t = tn. If a R-K approach is preferred, usually two stages are needed to achieve a second order accuracy in time.

Our goal is to extend the L-W type schemes to even higher order accuracy. Based on a

second order L-W type solver with the information u and ∂∂tu, a two-stage procedure can be designed to obtain a fourth order temporal accurate approximation for u(·, tn+1): one stage

![image 12](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile12.png>)

at t = tn and the other stage at tn + ∆2t. The algorithm is stated below.

![image 13](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile13.png>)

(i) Lax-Wendroﬀ step. Given an initial data un(x) to (1.1) at t = tn, construct instantaneous values u(x, tn +0) and ∂∂tu(x, tn +0), which are symbolically denoted as

![image 14](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile14.png>)

- (1.4) u(·, tn + 0) = M(un),

∂ ∂t

![image 15](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile15.png>)

u(·, tn + 0) = L(un). Then ∂t∂ L(u)(·, tn + 0) is subsequently obtained using the chain rule,

![image 16](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile16.png>)

- (1.5)

∂ ∂tL(un) =

![image 17](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile17.png>)

∂ ∂uL(un)

![image 18](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile18.png>)

∂ ∂t

![image 19](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile19.png>)

u(·, tn + 0).

(ii) Solution advancing step. Deﬁne the intermediate data u∗(x)

- (1.6) u∗ = un +

- 1

![image 20](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile20.png>)

- 2


∆tL(un) +

1 8

![image 21](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile21.png>)

∆t2

∂ ∂tL(un),

![image 22](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile22.png>)

which can be used to reconstruct new initial data u∗(x) and get the solution ∂t∂ L(u∗). Then the solution to the next time level tn+1 = tn + ∆t can be updated by

![image 23](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile23.png>)

- (1.7) un+1 = un + ∆tL(un) +


1 6

∆t2

![image 24](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile24.png>)

∂ ∂tL(u∗) .

∂ ∂tL(un) + 2

![image 25](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile25.png>)

![image 26](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile26.png>)

The above updating scheme distinguishes from the traditional R-K approach in the following aspects.

- (i) The above approach is based on a second order L-W type solver to achieve a fourth

order temporal accuracy, which is diﬀerent from traditional R-K methods for (1.1) based on ﬁrst order solvers. It is a two-stage approach, while the R-K approach usually needs four stages to attain the same accuracy. With the data reconstruction in the middle stage, this new approach removes two stages of data reconstruction from the standard R-K approach. Together with numerical ﬂux evaluation, at least about 20% computational cost can be saved for 1-D problems, and 30% cost saved for 2-D problems in the current method.

- (ii) The governing equation (1.1) is explicitly used in the L-W solver so that all useful


information can be included in the solution approximation. More importantly, we stick to the utilization of the time derivatives of solutions ∂u/∂t to advance the solution, which seems more eﬀective to capture discontinuities sharply. See Remark 3.1 in Section 3 for the explanation.

(iii) This approach can be applied in other frameworks, such as DG or ﬁnite diﬀerence methods etc. Not only for hyperbolic conservation laws (1.1), other time-dependent problems can be solved by the above approach as well once there is a corresponding CauchyKovalevskaya theorem.

Since this method is based on L-W type solvers, the generalized Riemann problem (GRP) solver [3, 4, 5, 6] is used as the building block. The GRP solver is an extension of the ﬁrst order Godunov solver to the second order time accuracy from the MUSCL-type initial data [23]. Its simpliﬁed acoustic version reduces to the so-called ADER solver [22], which can of course be used as the building block too. Other alternative choice could be the gas kinetic solvers (GKS) [16, 24]. Numerical experiments from the GRP solver demonstrate the suitability to design such a fourth order method.

This paper is organized in the following. After the introduction section, a two-stage temporal discretization is presented in Section 2. In Section 3, this approach is applied to hyperbolic conservation laws in 1-D and 2-D, respectively. In Section 4, numerical experiments for scalar conservation laws and the compressible Euler equations are taken to validate the performance of the proposed approach. The last section presents discussions and some prospectives of this approach.

2. A high order temporal discretization for time-dependent problems

In order to advance the solution of (1.1) with a fourth order temporal accuracy for the L-W type solvers, consider the following time-dependent equations,

- (2.1)

∂u ∂t

![image 27](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile27.png>)

= L(u), subject to the initial data at t = tn,

- (2.2) u(t)|t=tn

= un,

where L is an operator for spatial derivatives. It is evident that the initial time variation of the solution at t = tn can be obtained using the chain rule and the Cauchy-Kovalevskaya method,

- (2.3)


∂2 ∂t2

∂ ∂tL(un) =

∂ ∂uL(un)L(un).

∂ ∂t

u(tn) = L(un),

u(tn) =

![image 28](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile28.png>)

![image 29](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile29.png>)

![image 30](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile30.png>)

![image 31](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile31.png>)

Let’s consider a high order accurate approximation to un+1 := u(tn +∆t). We write (2.1) as

- (2.4) un+1 = un +

tn+∆t

tn

L(u(t))dt.

Introduce an intermediate value at time t = tn + A∆t with a parameter A, within a third order accuracy,

- (2.5) u∗ = un + A∆tL(un) +

- 1

![image 32](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile32.png>)

- 2


A2∆t2

∂ ∂tL(un),

![image 33](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile33.png>)

which subsequently determines the solution at the middle stage,

- (2.6)

∂u∗ ∂t

![image 34](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile34.png>)

= L(u∗),

∂ ∂tL(u∗) =

![image 35](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile35.png>)

∂

![image 36](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile36.png>)

∂uL(u∗)L(u∗). Set

- (2.7) un+1 = un + ∆t(B0L(un) + B1L(u∗)) +

- 1

![image 37](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile37.png>)

- 2


∆t2 C0

∂ ∂tL(un) + C1

![image 38](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile38.png>)

∂ ∂tL(u∗) ,

![image 39](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile39.png>)

where B0, B1, C0 and C1, together with A, are determined according to accuracy requirement. We formulate this approximation in the form of a proposition.

Proposition 2.1. If the following parameters are taken,

- (2.8) A =

- 1

![image 40](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile40.png>)

- 2


, B0 = 1, B1 = 0, C0 =

1 3

![image 41](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile41.png>)

, C1 =

- 2

![image 42](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile42.png>)

- 3


,

the iterations (2.5)–(2.7) provide a fourth order accurate approximation to the solution u(t) at t = tn + ∆t. These parameters are uniquely determined for the fourth order accuracy requirement.

Proof. The proof uses the standard Taylor series expansion, as usually done for the R-K approach. For notational simplicity, we denote

- (2.9) G(u) := Lu(u)L(u), Lu(u) :=

∂ ∂uL(u),

![image 43](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile43.png>)

and similarly for Luu, Luuu, Gu, and Guu. Then we have the following expansions around un,

- (2.10) L(u∗) = L(un) + Lu(u∗ − un) + Luu 2

![image 44](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile44.png>)

(u∗ − un)2 + Luuu 6

![image 45](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile45.png>)

(u∗ − un)3 + O(u∗ − un)4,

and

- (2.11) G(u∗) = G(un) + Gu(u∗ − un) + Guu 2


(u∗ − un)2 + O(u∗ − un)3.

![image 46](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile46.png>)

Using (2.5) and (2.6), as well as substituting the above two expansions into (2.7), we obtain

- (2.12)

∆t(B0L(un) + B1L(u∗)) + 21∆t2 C0∂t∂ L(un) + C1∂t∂ L(u∗)

![image 47](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile47.png>)

![image 48](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile48.png>)

![image 49](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile49.png>)

= ∆t(B0 + B1)L(un) +

∆t2 2

![image 50](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile50.png>)

AB1 +

- 1

![image 51](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile51.png>)

- 2


(C0 + C1) Lu(un)L(un)

+

∆t3 6

![image 52](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile52.png>)

3(A2B1 + AC1) · [L2u(un)L(un) + Luu(un)L2(un)]

+

∆t4 24

![image 53](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile53.png>)

6A2C1L3u(un)L(un) + (12A3B1 + 24A2C1)(Luu(un)Lu(un)L2(un)

+ (4A3B1 + 6A2C1)Luuu(un)L(un) + O(∆t5). Taking the Taylor series expansion directly for the time integration in (2.4) yields

- (2.13)

tn+∆t

tn

L(u(t))dt

= ∆tL(un) +

∆t2 2 Lu(un)L(un) +

![image 54](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile54.png>)

∆t3 6

![image 55](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile55.png>)

[L2u(un)L(un) + Luu(un)L2(un)]

+

∆t4 24

![image 56](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile56.png>)

[L3u(un)L(un) + 4Luu(un)Lu(un)L2(un) + Luuu(un)L(un)] + O(∆t5). The comparison of (2.12) and (2.13) gives

- (2.14)

B0 + B1 = 1, AB1 + 21(C0 + C1) = 21, A2B1 + AC1 = 13, A2C1 = 16, A3B1 + 2A2C1 = 13, 2A3B1 + 3A2C1 = 21.

![image 57](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile57.png>)

![image 58](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile58.png>)

![image 59](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile59.png>)

![image 60](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile60.png>)

![image 61](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile61.png>)

![image 62](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile62.png>)

The above equations uniquely determine A, B0, B1, C0 and C1 with the values in (2.8).

Thus we present the algorithm for (2.1) explicitly. Algorithm-general.

- Step 1. Deﬁne intermediate values

(2.15)

u∗ = un + 12∆tL(un) +

![image 63](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile63.png>)

1 8

![image 64](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile64.png>)

∆t2

∂ ∂tL(un),

![image 65](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile65.png>)

∂ ∂tL(u∗) =

![image 66](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile66.png>)

∂ ∂uL(u∗)L(u∗).

![image 67](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile67.png>)

- Step 2. Advance the solution using the formula


- (2.16) un+1 = un + ∆tL(un) +


1 6

∆t2

![image 68](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile68.png>)

∂ ∂tL(u∗) .

∂ ∂tL(un) + 2

![image 69](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile69.png>)

![image 70](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile70.png>)

- Remark 2.2. Note that A = 12. The time tn + A∆t is in the middle of interval [tn, tn + ∆t] and u∗ is the mid-point value of u. Therefore, the iterations (2.5)–(2.7) can be actually regarded as an Hermite-type approximation to (2.4). In contrast, the classical R-K iteration


![image 71](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile71.png>)

method is written as

i−1

αkiu(k) + ∆tβkiL(u(k)), i = 1, ..., m, u(0) = un, u(m) = un+1,

u(i) =

- (2.17)


k=0

where αki ≥ 0, βki > 0 are the integration weights, satisfying the compatibility condition

i−1

αki = 1. Since the approximation (2.17) does not involve the derivative of L, it is regarded as the Simpson-type approximation to (2.4).

k=0

3. Fourth order accurate temporal discretization for hyperbolic conservation laws

In this section, we will extend the approach in the last section to hyperbolic conservation laws (1.1) to design a time-space fourth order accurate method. This extension is based on L-W type solvers with the instantaneous solution and its temporal derivative through the governing equation (1.1). We will ﬁrst discuss the one-dimensional case, and then go to the two-dimensional case.

- 3.1. One-dimensional hyperbolic conservation laws. Let us start with one-dimensional hyperbolic conservation laws


- (3.1) ut + f(u)x = 0, where u is, as in (1.1), a conserved variable and f(u) is the associated ﬂux function. We integrate it over the cell (xj−1

![image 72](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile72.png>)

2

, xj+1

![image 73](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile73.png>)

2

) to obtain the semi-discrete form

- (3.2)

d dt

![image 74](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile74.png>)

u¯j(t) = Lj(u) := −

1 ∆xj

![image 75](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile75.png>)

[fj+1

![image 76](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile76.png>)

2

− fj−1

![image 77](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile77.png>)

2

],

where fj+1

![image 78](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile78.png>)

2

is the numerical ﬂux through the cell boundary x = xj+1

![image 79](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile79.png>)

2

at time t, ∆xj = xj+1

![image 80](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile80.png>)

2

− xj−1

![image 81](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile81.png>)

2

. We construct initial data for (3.2) through a ﬁfth order WENO or HWENO interpolation technology [12, 17],

- (3.3) u(x, tn) = un(x).

Based on this initial condition, with possible discontinuities at the cell boundaries, the instantaneous solution can be obtained,

- (3.4) unj+1

![image 82](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile82.png>)

2

:= lim

t→tn+0

u(xj+1

![image 83](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile83.png>)

2

, t),

∂u ∂t

![image 84](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile84.png>)

n

j+21

![image 85](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile85.png>)

:= lim

t→tn+0

∂ ∂t

![image 86](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile86.png>)

u(xj+1

![image 87](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile87.png>)

2

, t).

There is an analytical solution for the generalized Riemann problem (GRP) solver [5, 6]; or approximately as ADER solvers [22]. Intrinsically, the temporal derivative (∂u/∂t)nj+1

![image 88](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile88.png>)

2

is replaced by the spatial derivative at time t = tn using the governing equation (3.1),

- (3.5)


n

∂ ∂x

∂u ∂t

= − lim

f(u(xj+1

, t)),

![image 89](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile89.png>)

![image 90](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile90.png>)

![image 91](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile91.png>)

t→tn+0

2

j+21

![image 92](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile92.png>)

where the spatial derivative takes account of the wave propagation. This approach is called the L-W approach numerically or the Cauchy-Kovalevskaya approach in the context of PDE theory. In the numerical experiments in Section 4, we use the GRP solver developed in [5, 6] and construct the corresponding algorithm for (3.1). This two-stage approach for (3.1) is proposed as follows.

- Algorithm 1-D.


- Step 1. With the initial data un(x) in (3.3) obtained by the HWENO interpolation, we compute the instantaneous values unj+1

![image 93](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile93.png>)

2

and (∂u/∂t)nj+1

![image 94](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile94.png>)

2

analytically or approximately using a L-W type solver.

- Step 2. Construct the intermediate values u∗(x) at t∗ = tn + 12∆t using the formulae,

![image 95](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile95.png>)

(3.6)

u¯∗j = u¯nj −

∆t 2∆xj

![image 96](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile96.png>)

[fj∗+1

![image 97](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile97.png>)

2

− fj∗−1

![image 98](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile98.png>)

2

],

fj∗+1

![image 99](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile99.png>)

2

= f(u(xj+1

![image 100](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile100.png>)

2

, tn +

1 4

![image 101](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile101.png>)

∆t)),

u(xj+1

![image 102](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile102.png>)

2

, tn +

- 1

![image 103](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile103.png>)

- 2


∆t) := unj+1

![image 104](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile104.png>)

2

+

∆t 2

![image 105](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile105.png>)

∂u ∂t

![image 106](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile106.png>)

n

j+21

![image 107](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile107.png>)

.

Then we use the HWENO interpolation again to construct u∗(x) and ﬁnd the values u∗j+1

![image 108](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile108.png>)

2

and (∂u/∂t)∗j+1

![image 109](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile109.png>)

2

at stage t = tn + ∆2t, as done in Step 1.

![image 110](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile110.png>)

- Step 3. Advance the solution to the next time level tn + ∆t,


- (3.7)

unj+1 = u¯nj −

∆t ∆xj

![image 111](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile111.png>)

[fj4+th1

![image 112](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile112.png>)

2

− fj4−th1

![image 113](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile113.png>)

2

],

fj4+th1

![image 114](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile114.png>)

2

= f(unj+1

![image 115](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile115.png>)

2

) +

∆t 6

![image 116](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile116.png>)

  ∂f(u)

![image 117](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile117.png>)

∂t (x

j+ 1 2

![image 118](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile118.png>)

,tn)

+ 2

∂f(u) ∂t (x

![image 119](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile119.png>)

j+ 1 2

![image 120](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile120.png>)

,t∗)

 .

This is exactly a two-stage method: One stage at t = tn and the other at t = tn + ∆2t. We

![image 121](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile121.png>)

only need to reconstruct data and use the L-W solver twice, at t = tn and t = tn + 21∆t, respectively. The procedure to reconstruct the intermediate state u∗(x) and get the GRP

![image 122](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile122.png>)

solution at time t = tn + ∆2t is the same as that at time t = tn.

![image 123](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile123.png>)

Remark 3.1. The utilization of the time derivative (∂u/∂t)nj+1

![image 124](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile124.png>)

2

is one of central points in our algorithm. Indeed, the fully explicit form of (3.1) is,

- (3.8) u¯nj+1 = unj −

![image 125](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile125.png>)

∆t ∆xj

![image 126](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile126.png>)

1 ∆t

![image 127](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile127.png>)

tn+1

tn

f(u(xj+1

![image 128](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile128.png>)

2

, t))dt −

1 ∆t

![image 129](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile129.png>)

tn+1

tn

f(u(xj−1

![image 130](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile130.png>)

2

, t))dt .

It is crucial to approximate the ﬂux at x = xj+1

![image 131](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile131.png>)

2

in the sense that

- (3.9) Numerical ﬂux at xj+1


1 ∆t

−

![image 132](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile132.png>)

![image 133](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile133.png>)

2

tn+1

, t))dt = O(∆tr), r > 1.

f(u(xj+1

![image 134](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile134.png>)

2

tn

Many algorithms approximate the ﬂux with error measured by ∆u, the jump across the interface,

- (3.10) Numerical ﬂux at xj+1

![image 135](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile135.png>)

2

−

1 ∆t

![image 136](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile136.png>)

tn+1

tn

f(u(xj+1

![image 137](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile137.png>)

2

, t))dt = O( ∆u r),

which is not proportional to the mesh size ∆xj or the time step length ∆t when the jump is large, e.g., strong shocks,

- (3.11) ∆u  ≈ O(∆xj).

It turns out that there is a large discrepancy when strong discontinuities present in the solutions. In order to overcome this diﬃculty, we have to solve the associated generalized

Riemann problem (GRP) analytically and derive the value (∂u/∂t)nj+1

![image 138](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile138.png>)

2

and subsequently (∂u/∂t)∗j+1

![image 139](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile139.png>)

2

.

Remark 3.2. Without using the data reconstruction for u∗(x), the above procedure could be regarded as the Hermite-type approximation to the total ﬂux in the sense

- (3.12) 1

![image 140](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile140.png>)

∆t

tn+1

tn

f(u(xj+1

![image 141](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile141.png>)

2

, t))dt =

2

k=1

Ckf(u(xj+1

![image 142](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile142.png>)

2

, tn + αk∆t)) + ∆tDk

∂f ∂t

![image 143](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile143.png>)

(u(xj+1

![image 144](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile144.png>)

2

, tn + αk∆t)) ,

where tn + αk∆t are the quadrature nodes, Ck, Dk are the quadrature weights. For linear equations, the formula is exact. We can further verify through numerical examples that this two-stage method indeed provides a temporal discretization with fourth order accuracy.

- 3.2. Multidimensional hyperbolic conservation laws. For multidimensional cases of (1.1), we still use the ﬁnite volume framework to develop a two-stage temporal-spatial fourth order accurate method. For simplicity of presentation, we only consider the two-dimensional (2-D) case with rectangular meshes in the present paper. All other cases can be treated analogously, e.g., over unstructured meshes.


We write the 2-D case of (1.1) as

- (3.13)

∂u ∂t

![image 145](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile145.png>)

+

∂f(u) ∂x

![image 146](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile146.png>)

+

∂g(u) ∂y

![image 147](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile147.png>)

= 0.

The computational domain Ω is divided into rectangular meshes Kij, Ω = ∪i∈I,j∈JKij, Kij = (xi−1

![image 148](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile148.png>)

2

, xj+1

![image 149](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile149.png>)

2

) × (yj−1

![image 150](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile150.png>)

2

, yj+1

![image 151](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile151.png>)

2

) with (xi, yj) as the center. Then (3.13) reads over Kij

- (3.14)

du¯i,j(t) dt

![image 152](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile152.png>)

= Li,j(u) := −

1 ∆xi

![image 153](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile153.png>)

[fi+1

![image 154](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile154.png>)

2,j − fi−1

![image 155](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile155.png>)

2,j] −

1 ∆yj

![image 156](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile156.png>)

[gi,j+1

![image 157](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile157.png>)

2

− gi,j−1

![image 158](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile158.png>)

2

], where ∆xi = xi+1

![image 159](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile159.png>)

2

− xi−1

![image 160](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile160.png>)

2

, ∆yj = yj+1

![image 161](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile161.png>)

2

− yj−1

![image 162](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile162.png>)

2

, and as convention,

- (3.15)


1 ∆xi∆yj K

u¯i,j =

u(x, y, t)dxdy,

![image 163](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile163.png>)

ij

yj+1 2

1 ∆yj

![image 164](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile164.png>)

2,j(t) =

, y, t))dy,

f(u(xi+1

fi+1

![image 165](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile165.png>)

![image 166](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile166.png>)

![image 167](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile167.png>)

2

yj−1 2

![image 168](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile168.png>)

xi+1 2

1 ∆xi

![image 169](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile169.png>)

(t) =

, t))dx.

g(u(x, yj+1

gi,j+1

![image 170](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile170.png>)

![image 171](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile171.png>)

![image 172](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile172.png>)

2

2

xi−1 2

![image 173](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile173.png>)

We use the Gauss quadrature to evaluate the above integrals to obtain numerical ﬂuxes in order to guarantee the accuracy in space. For example, we evaluate fi+1

2,j(t) for any time t,

![image 174](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile174.png>)

- (3.16)

1 ∆yj

![image 175](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile175.png>)

yj+1 2

![image 176](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile176.png>)

yj−1 2

![image 177](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile177.png>)

f(u(xi+1

![image 178](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile178.png>)

2

, y, t))dy ≈

k

ℓ=0

ωℓf(u(xi+1

![image 179](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile179.png>)

2

, yℓ, t)),

where yℓ ∈ (yj−1

![image 180](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile180.png>)

2

, yj+1

![image 181](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile181.png>)

2

), ℓ = 1, · · · , k, are Gauss points and ωℓ are corresponding weights. At each Gauss point (xi+1

![image 182](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile182.png>)

2

, yℓ, tn), we solve the quasi 1-D generalized Riemann problem (GRP) for (3.13) ,

- (3.17) u(x, yℓ, tn) =

uni,j(x, yℓ), x < xi+1

![image 183](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile183.png>)

2

, uni,j+1(x, yℓ), x > xi+1

![image 184](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile184.png>)

2

.

In analogy with the 1-D case in (3.4), we obtain

- (3.18) uni+1

![image 185](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile185.png>)

2,jℓ := lim

t→tn+0

u(xi+1

![image 186](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile186.png>)

2

, yℓ, t),

∂u ∂t

![image 187](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile187.png>)

n

i+12,jℓ

![image 188](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile188.png>)

= lim

t→tn+0

∂u ∂t

![image 189](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile189.png>)

(xi+1

![image 190](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile190.png>)

2

, yℓ, t),

and similarly for others. The GRP solver for (3.13) and (3.17) is put in Appendix (A). Thus we propose the following two-stage algorithm for 2-D hyperbolic conservation laws (3.13).

- Algorithm 2-D.


- Step 1. With the initial data un(x, y) obtained by the HWENO interpolation, we com-

pute the instantaneous values uni

ℓ,j+21, uni+1

![image 191](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile191.png>)

![image 192](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile192.png>)

2,jℓ, (∂u/∂t)ni

ℓ,j+21and (∂u/∂t)ni+1

![image 193](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile193.png>)

![image 194](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile194.png>)

2,jℓ at every Gauss point.

- Step 2. Construct the intermediate values u∗(x, y) at t∗ = tn + 12∆t using the formulae,


![image 195](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile195.png>)

- (3.19)


∆t 2∆yj

∆t 2∆xi

2,j − fi∗−1

[fi∗+1

[gi,j∗ +1

u¯∗i,j = u¯ni,j −

2,j] −

![image 196](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile196.png>)

![image 197](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile197.png>)

![image 198](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile198.png>)

![image 199](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile199.png>)

![image 200](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile200.png>)

2

k

1 4

∆t)), gi∗

fi∗+1

ωℓf(u(xi+1

2,j =

, yℓ, tn +

ℓ,j+21 =

![image 201](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile201.png>)

![image 202](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile202.png>)

![image 203](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile203.png>)

![image 204](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile204.png>)

2

ℓ=0

n

∆t 2

- 1

![image 205](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile205.png>)

- 2


∂u ∂t

∆t) := uni+1

u(xi+1

2,jℓ +

, yℓ, tn +

![image 206](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile206.png>)

![image 207](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile207.png>)

![image 208](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile208.png>)

![image 209](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile209.png>)

2

i+21,jℓ

![image 210](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile210.png>)

n

∂u ∂t

∆t 2

- 1

![image 211](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile211.png>)

- 2


∆t) := uni

u(xℓ, yj+1

ℓ,j+21 +

, tn +

![image 212](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile212.png>)

![image 213](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile213.png>)

![image 214](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile214.png>)

![image 215](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile215.png>)

2

iℓ,j+21

![image 216](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile216.png>)

− gi,j∗ −1

],

![image 217](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile217.png>)

2

k

ωℓg(u(xℓ, yj+1

, tn +

![image 218](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile218.png>)

2

ℓ=0

,

1 4

∆t)),

![image 219](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile219.png>)

.

Then we use the HWENO interpolation to reconstruct u∗(x, y) and ﬁnd the values u∗i

2,jℓ at t = tn + ∆2t as done in Step 1.

ℓ,j+21, u∗i+1

2,jℓ, (∂u/∂t)∗i

ℓ,j+21and (∂u/∂t)∗i+1

![image 220](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile220.png>)

![image 221](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile221.png>)

![image 222](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile222.png>)

![image 223](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile223.png>)

![image 224](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile224.png>)

- Step 3. Advance the solution to the next time level tn + ∆t,

(3.20)

u¯ni,j+1 = u¯ni,j −

∆t ∆xj

![image 225](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile225.png>)

[fi4+th1

![image 226](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile226.png>)

2,j − fi4−th1

![image 227](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile227.png>)

2,j] −

∆t ∆yj

![image 228](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile228.png>)

[gi,j4th+1

![image 229](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile229.png>)

2

− gi,j4th−1

![image 230](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile230.png>)

2

],

fi4+th1

![image 231](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile231.png>)

2,j =

k

ℓ=0

ωℓfi4+th1

![image 232](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile232.png>)

2,jℓ, gi,j4th+1

![image 233](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile233.png>)

2

=

k

ℓ=0

ωℓgi4th

ℓ,j+21;

![image 234](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile234.png>)

fi4+th1

![image 235](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile235.png>)

2,jℓ = f(uni+1

![image 236](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile236.png>)

2,jℓ) +

∆t 6

![image 237](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile237.png>)

∂f ∂t

![image 238](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile238.png>)

(uni+1

![image 239](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile239.png>)

2,jℓ) + 2

∂f ∂t

![image 240](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile240.png>)

(u∗i+1

![image 241](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile241.png>)

2,jℓ) , gi4th

ℓ,j+21 = g(uni

![image 242](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile242.png>)

ℓ,j+21) +

![image 243](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile243.png>)

∆t 6

![image 244](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile244.png>)

∂g ∂t

![image 245](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile245.png>)

(uni

ℓ,j+21) + 2

![image 246](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile246.png>)

∂g ∂t

![image 247](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile247.png>)

(u∗i

ℓ,j+21) .

![image 248](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile248.png>)

4. Numerical Examples

In this section we provide several examples to validate the performance of the proposed approach. The examples include linear and nonlinear scalar conservation laws, 1-D Euler equations and 2-D Euler equations. The order of accuracy will be tested. All results are obtained with CFL number 0.5 except the large density ratio problem for which the CFL number is taken to be 0.2. We use GRP4-HWENO5 to denote the algorithm with the GRP solver and the HWENO ﬁfth order accurate spatial reconstruction, and use RK4-WENO5 to denote the algorithm with the WENO ﬁfth order accurate spatial reconstruction and fourth order accurate temporal R-K iteration.

- 4.1. Scalar conservation laws. We use our approach to solve two examples of scalar conservation laws.


- Example 1. The ﬁrst example is a linear advection equation with a periodic boundary condition,


- (4.1) ut + ux = 0, u(x, 0) = sin(πx).


The solution is computed over the space interval [0, 2] and the results are displayed in Table

1. We can see that the accuracy is achieved as expected.

![image 249](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile249.png>)

![image 250](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile250.png>)

![image 251](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile251.png>)

![image 252](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile252.png>)

![image 253](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile253.png>)

![image 254](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile254.png>)

![image 255](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile255.png>)

m RK4-WENO5 GRP4-HWENO5

![image 256](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile256.png>)

![image 257](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile257.png>)

![image 258](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile258.png>)

![image 259](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile259.png>)

![image 260](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile260.png>)

![image 261](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile261.png>)

![image 262](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile262.png>)

![image 263](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile263.png>)

![image 264](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile264.png>)

![image 265](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile265.png>)

![image 266](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile266.png>)

L1 error order L∞ error order L1 error order L∞ error order 40 4.47(-4) 4.91 3.81(-4) 4.73 1.67(-4) 5.07 1.60(-4) 4.91 80 1.40(-5) 5.00 1.27(-5) 4.91 5.28(-6) 4.99 5.10(-6) 4.97 160 4.37(-7) 5.00 3.97(-7) 5.00 1.79(-7) 4.88 1.60(-7) 4.99 320 1.37(-8) 5.00 1.25(-8) 4.99 7.19(-9) 4.64 5.68(-9) 4.82 640 4.30(-10) 4.99 3.77(-10) 5.05 3.60(-10) 4.32 2.86(-10) 4.31

![image 267](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile267.png>)

![image 268](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile268.png>)

![image 269](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile269.png>)

![image 270](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile270.png>)

![image 271](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile271.png>)

![image 272](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile272.png>)

![image 273](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile273.png>)

![image 274](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile274.png>)

![image 275](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile275.png>)

![image 276](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile276.png>)

![image 277](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile277.png>)

![image 278](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile278.png>)

![image 279](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile279.png>)

![image 280](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile280.png>)

![image 281](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile281.png>)

![image 282](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile282.png>)

![image 283](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile283.png>)

![image 284](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile284.png>)

![image 285](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile285.png>)

![image 286](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile286.png>)

![image 287](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile287.png>)

![image 288](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile288.png>)

![image 289](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile289.png>)

![image 290](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile290.png>)

![image 291](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile291.png>)

![image 292](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile292.png>)

![image 293](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile293.png>)

![image 294](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile294.png>)

![image 295](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile295.png>)

![image 296](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile296.png>)

![image 297](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile297.png>)

![image 298](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile298.png>)

![image 299](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile299.png>)

![image 300](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile300.png>)

![image 301](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile301.png>)

![image 302](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile302.png>)

![image 303](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile303.png>)

![image 304](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile304.png>)

![image 305](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile305.png>)

![image 306](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile306.png>)

![image 307](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile307.png>)

![image 308](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile308.png>)

![image 309](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile309.png>)

![image 310](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile310.png>)

![image 311](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile311.png>)

![image 312](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile312.png>)

![image 313](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile313.png>)

![image 314](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile314.png>)

![image 315](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile315.png>)

![image 316](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile316.png>)

![image 317](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile317.png>)

![image 318](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile318.png>)

Table 1. The comparison of L1, L∞ errors and convergence order for a convection equation. The schemes are RK4-WENO5 and GRP4-HWENO5 with m cells. The results are shown at time t = 10.

- Example 2. The second example is taken for the Burgers equation with a periodic boundary condition [7],


- (4.2) ut +

u2 2 x

![image 319](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile319.png>)

= 0, u(x, 0) =

1 4

![image 320](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile320.png>)

+

1 2

![image 321](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile321.png>)

sin(πx).

The solution is smooth up to the time t = 2/π and develops a shock that moves to interact with a rarefaction, as shown in Figure 4.1 . The errors and convergence order are shown in Table 2.

0 0.5 1 1.5 2

−0.4

−0.2

0

0.2

0.4

0.6

- 0.8

- 1


| | | |
|---|---|---|


| | |
|---|---|


| | |
|---|---|
| | |


x

u

t=1/π

|exact<br><br>GRP4−HWENO5 RK4−WENO5<br><br>| |
|---|
|
|---|


0 0.5 1 1.5 2

−0.4

−0.2

0

0.2

0.4

0.6

- 0.8

- 1


| | |
|---|---|


| | | | |
|---|---|---|---|
| | | | |


x

u

t=2/π

|exact<br><br>GRP4−HWENO5 RK4−WENO5<br><br>| |
|---|
|
|---|


0 0.5 1 1.5 2

−0.4

−0.2

0

0.2

0.4

0.6

- 0.8

- 1


| | |
|---|---|


| | |
|---|---|


x

u

t=3/π

|exact<br><br>GRP4−HWENO5 RK4−WENO5<br><br>| |
|---|
<br><br>|
|---|


Figure 4.1. Numerical solutions of the Burgers equation. The schemes are RK4-WENO5 and GRP4-HWENO5 which are implemented with 40 cells. The results are shown at t = 1/π (left), t = 2/π (middle), t = 3/π (right), respectively.

![image 322](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile322.png>)

![image 323](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile323.png>)

m RK4-WENO5 GRP4-HWENO5

![image 324](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile324.png>)

![image 325](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile325.png>)

![image 326](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile326.png>)

![image 327](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile327.png>)

![image 328](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile328.png>)

![image 329](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile329.png>)

![image 330](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile330.png>)

![image 331](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile331.png>)

L1 error order L∞ error order L1 error order L∞ error order 40 3.60(-5) 3.79 1.74(-4) 2.94 9.07(-6) 4.39 4.32(-5) 3.58 80 1.84(-6) 4.29 8.17(-6) 4.41 5.53(-7) 4.03 3.01(-6) 3.84 160 7.06(-8) 4.71 4.31(-7) 4.25 2.48(-8) 4.48 1.83(-7) 4.05 320 1.84(-9) 5.26 9.53(-9) 5.50 8.91(-10) 4.80 2.97(-9) 5.94 640 4.63(-11) 5.31 2.94(-10) 5.02 4.93(-11) 4.17 1.96(-10) 3.91

![image 332](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile332.png>)

![image 333](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile333.png>)

![image 334](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile334.png>)

![image 335](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile335.png>)

![image 336](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile336.png>)

![image 337](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile337.png>)

![image 338](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile338.png>)

![image 339](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile339.png>)

![image 340](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile340.png>)

![image 341](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile341.png>)

![image 342](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile342.png>)

![image 343](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile343.png>)

![image 344](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile344.png>)

![image 345](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile345.png>)

![image 346](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile346.png>)

![image 347](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile347.png>)

![image 348](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile348.png>)

![image 349](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile349.png>)

![image 350](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile350.png>)

![image 351](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile351.png>)

![image 352](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile352.png>)

![image 353](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile353.png>)

![image 354](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile354.png>)

![image 355](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile355.png>)

![image 356](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile356.png>)

![image 357](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile357.png>)

![image 358](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile358.png>)

![image 359](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile359.png>)

![image 360](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile360.png>)

![image 361](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile361.png>)

![image 362](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile362.png>)

![image 363](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile363.png>)

![image 364](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile364.png>)

![image 365](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile365.png>)

![image 366](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile366.png>)

![image 367](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile367.png>)

![image 368](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile368.png>)

![image 369](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile369.png>)

![image 370](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile370.png>)

![image 371](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile371.png>)

![image 372](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile372.png>)

![image 373](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile373.png>)

![image 374](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile374.png>)

![image 375](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile375.png>)

![image 376](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile376.png>)

![image 377](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile377.png>)

![image 378](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile378.png>)

![image 379](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile379.png>)

![image 380](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile380.png>)

![image 381](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile381.png>)

![image 382](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile382.png>)

![image 383](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile383.png>)

![image 384](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile384.png>)

![image 385](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile385.png>)

![image 386](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile386.png>)

![image 387](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile387.png>)

![image 388](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile388.png>)

![image 389](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile389.png>)

![image 390](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile390.png>)

![image 391](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile391.png>)

Table 2. The comparison of L1, L∞ errors and convergence order for the Burgers equation. The schemes are RK4-WENO5 and GRP4-HWENO5 with m cells. The results are shown at time t = 1/π.

4.2. One-dimensional Euler equations. We provide several examples for 1-D compressible Euler equations,

- (4.3) u = (ρ, ρv, ρE)⊤, f(u) = (ρv, ρv2 + p, v(ρE + p))⊤,


where ρ is the density, v is the velocity, p is the pressure and E = v2/2+e is the total energy, e = (γ−p1)ρ is the internal energy for polytropic gases. We test several standard examples to validate the proposed scheme.

![image 392](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile392.png>)

- Example 3. Smooth problem. In order to verify the numerical accuracy of the present fourth order accurate scheme, we check the numerical results for a smooth problem whose initial data is

- (4.4) ρ(x, 0) = 1 + 0.2sin(x), v(x, 0) = 1, p(x, 0) = 1.

The periodic boundary conditions are used again. The results are shown in Table 3, which veriﬁes the expected accuracy order.

![image 393](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile393.png>)

![image 394](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile394.png>)

m RK4-WENO5 GRP4-HWENO5

![image 395](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile395.png>)

![image 396](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile396.png>)

![image 397](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile397.png>)

![image 398](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile398.png>)

![image 399](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile399.png>)

![image 400](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile400.png>)

![image 401](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile401.png>)

![image 402](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile402.png>)

L1 error order L∞ error order L1 error order L∞ error order 40 8.92(-5) 4.91 7.64(-5) 4.72 3.33(-5) 5.07 3.13(-5) 4.90 80 2.78(-6) 5.00 2.53(-6) 4.91 1.04(-6) 5.01 9.86(-7) 4.97 160 8.61(-8) 5.01 7.83(-8) 5.02 3.31(-8) 4.97 3.05(-8) 5.01 320 2.59(-9) 5.06 2.23(-9) 5.13 1.12(-9) 4.88 1.01(-9) 4.91 640 7.07(-11) 5.19 6.15(-11) 5.18 4.37(-11) 4.68 4.19(-11) 4.60

![image 403](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile403.png>)

![image 404](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile404.png>)

![image 405](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile405.png>)

![image 406](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile406.png>)

![image 407](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile407.png>)

![image 408](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile408.png>)

![image 409](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile409.png>)

![image 410](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile410.png>)

![image 411](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile411.png>)

![image 412](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile412.png>)

![image 413](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile413.png>)

![image 414](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile414.png>)

![image 415](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile415.png>)

![image 416](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile416.png>)

![image 417](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile417.png>)

![image 418](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile418.png>)

![image 419](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile419.png>)

![image 420](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile420.png>)

![image 421](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile421.png>)

![image 422](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile422.png>)

![image 423](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile423.png>)

![image 424](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile424.png>)

![image 425](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile425.png>)

![image 426](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile426.png>)

![image 427](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile427.png>)

![image 428](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile428.png>)

![image 429](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile429.png>)

![image 430](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile430.png>)

![image 431](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile431.png>)

![image 432](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile432.png>)

![image 433](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile433.png>)

![image 434](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile434.png>)

![image 435](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile435.png>)

![image 436](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile436.png>)

![image 437](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile437.png>)

![image 438](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile438.png>)

![image 439](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile439.png>)

![image 440](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile440.png>)

![image 441](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile441.png>)

![image 442](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile442.png>)

![image 443](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile443.png>)

![image 444](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile444.png>)

![image 445](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile445.png>)

![image 446](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile446.png>)

![image 447](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile447.png>)

![image 448](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile448.png>)

![image 449](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile449.png>)

![image 450](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile450.png>)

![image 451](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile451.png>)

![image 452](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile452.png>)

![image 453](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile453.png>)

![image 454](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile454.png>)

![image 455](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile455.png>)

![image 456](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile456.png>)

![image 457](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile457.png>)

![image 458](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile458.png>)

![image 459](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile459.png>)

![image 460](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile460.png>)

![image 461](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile461.png>)

![image 462](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile462.png>)

Table 3. The comparison of L1, L∞ errors and convergence order for the Euler equations in Example 3. The schemes are RK4-WENO5 and GRP4HWENO5 with m cells. The results are shown at time t = 10.

Example 4. Shock-turbulence interaction problem. This example was proposed in [18] to model shock-turbulence interactions. The initial data is take as

- (4.5) (ρ, v, p)(x, 0) = 


- Example 5. Woodward-Colella problem. This is the Woodward-Colella interacting blast wave problem. The gas is at rest and ideal with γ = 1.4, and the density is everywhere unit. The pressure is p = 1000 for 0 ≤ x < 0.1 and p = 100 for 0.9 < x ≤ 1.0, while it is only p = 0.01 in 0.1 < x < 0.9. Reﬂecting boundary conditions are applied at both ends. Both the GRP4-HWENO5 scheme and the RK4-WENO5 scheme could give a well-resolved solution using 800 grids. See Figure 4.3. The reference solution is computed with 4000 grids.
- Example 6. Large pressure ratio problem. The large pressure ratio problem is ﬁrst presented in [20] to test the ability to capture extremely strong rarefaction waves and its inﬂuence on the shock location. In the original paper [20], it shows that most MUSCL–type schemes have defects in resolving, even with very ﬁne mesh, the correct wave structures. In this problem, initially the pressure and density ratio between two neighboring states are very high. The initial data is (ρ, v, p) = (10000, 0, 10000) for 0 ≤ x < 0.3 and (ρ, v, p) = (1, 0, 1)


(3.857143, 2.629369, 10.333333), for x < −4, (1 + 0.2 sin(5x), 0, 1), for x ≥ −4.

 

The result is shown in Figure 4.2 and it is comparable with those by other schemes.

- 0.5

- 1

- 1.5

- 2

2.5

3

- 3.5

- 4


- 4.5

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


| | |
|---|---|
| | |
| | |


| |
|---|
| |


| | |
|---|---|


| | |
|---|---|
| | |
| | |


| | |
|---|---|
| | |


| | |
|---|---|
| | |
| | |


| |
|---|
| |


| | |
|---|---|


| | |
|---|---|
| | |


| |
|---|
| |
| |


| | | |
|---|---|---|
| | | |
| | | |


Density

Density

| | |
|---|---|
| | |


| | |
|---|---|
| | |
| | |


|exact<br><br>GRP4−HWENO5 RK4−WENO5<br><br>| |
|---|
|
|---|


|exact<br><br>GRP4−HWENO5 RK4−WENO5<br><br>| |
|---|
<br><br>|
|---|


−5 0 5 x

0 0.5 1 1.5 2 2.5 x

Figure 4.2. The comparison of the density proﬁle for the shock-turbulence interaction problem. The schemes used are RK4-WENO5 and GRP4HWENO5 with 400 cells. The solid lines are the reference solution.

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


|exact<br><br>GRP4−HWENO5 RK4−WENO5<br><br>| |
|---|
|
|---|


|exact<br><br>GRP4−HWENO5 RK4−WENO5<br><br>| |
|---|
<br><br>|
|---|


Density

Density

0 0.2 0.4 0.6 0.8 1 x

0 0.2 0.4 0.6 0.8 1 x

Figure 4.3. The comparison of the density proﬁle for the Woodward-Colella problem. The schemes are RK4-WENO5 and GRP4-HWENO5 with 200 cells (left) and 800 cells (right, 400 are shown), respectively. The solid lines are the reference solution.

for 0.3 ≤ x ≤ 1.0. The results with 400 points are shown in Figure 4.4, by GRP4-HWENO5 and RK4-WENO5, respectively. With 400 grid points, the GRP4-HWENO scheme gives perfect results, while the RK4-WENO5 fails to achieve that.

- 0

- 0.5

- 1

1.5

2

- 2.5

- 3


- 3.5

- 4


Density

Density

- 0

- 0.5

- 1

1.5

2

- 2.5

- 3

3.5

4

- 4.5




−0.5

−0.5

0 0.2 0.4 0.6 0.8 1

0 0.2 0.4 0.6 0.8 1

x

x

Figure 4.4. The comparison of the density for the large pressure ratio problem. The magnitude is scaled by 104. The schemes are GRP4-HWENO5 (left) and RK4-WENO5 (right) with 300 cells. The solid lines are the reference solution.

4.3. 2-D Examples. We provide several two-dimensional examples to validate the proposed approach. The governing equations are the 2-D Euler equations,

u = (ρ, ρu, ρv, ρE)⊤,

- (4.6)


- f(u) = (ρu, ρu2 + p, ρuv, u(ρE + p))⊤,
- g(u) = (ρv, ρuv, ρv2 + p, v(ρE + p))⊤,


where (u, v) is the velocity, E = u2+2v2 + e, e = (γ−p1)ρ. The ﬁrst example is about the isentropic vortex problem to test the accuracy. The other examples aim to verify the expected performance of this approach.

![image 463](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile463.png>)

![image 464](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile464.png>)

- Example 7. Isentropic vortex problem. In this ﬁrst 2-D isentropic vortex example we want to verify the numerical accuracy of our scheme. Initially the mean ﬂow is given with ρ = 1, p = 1, and (u, v) = (1, 1). Then an isentropic vortex is put on this mean ﬂow

(δu, δv) = 2ǫπe0.5(1−r2)(−y,¯ x¯), δT = −(γ−1)ǫ

![image 465](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile465.png>)

2

![image 466](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile466.png>)

8γπ2 e1−r2, δS = 0,

where (¯x, y¯) = (x−5, y −5), r2 = x¯2 +y¯2, and the vortex strength is often set to be ǫ = 5.0. The computation is performed in the domain [0, 10] × [0, 10], extended periodically in both directions. The accuracy is achieved with the expected order 4.

- Example 8. Two-dimensional Riemann problems. We provide three examples for two-dimensional Riemann problems, as shown in Figure 4.5. These examples are taken from [10] and involve the interactions of shocks, the interaction of shocks with vortex sheets and


![image 467](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile467.png>)

![image 468](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile468.png>)

![image 469](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile469.png>)

![image 470](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile470.png>)

![image 471](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile471.png>)

![image 472](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile472.png>)

![image 473](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile473.png>)

m RK4-WENO5 GRP4-HWENO5

![image 474](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile474.png>)

![image 475](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile475.png>)

![image 476](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile476.png>)

![image 477](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile477.png>)

![image 478](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile478.png>)

![image 479](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile479.png>)

![image 480](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile480.png>)

![image 481](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile481.png>)

![image 482](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile482.png>)

![image 483](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile483.png>)

![image 484](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile484.png>)

L1 error order L∞ error order L1 error order L∞ error order 40 1.79(-4) 3.80 3.29(-3) 3.76 7.70(-3) 3.87 1.92(-3) 3.71 80 6.92(-6) 4.69 1.96(-4) 4.07 3.47(-4) 4.47 1.26(-4) 3.93 160 2.03(-7) 5.09 4.95(-6) 5.31 1.05(-5) 5.05 3.26(-6) 5.28 320 7.83(-9) 4.70 1.96(-7) 4.66 3.47(-7) 4.92 1.54(-7) 4.40 640 - - - - 1.03(-8) 5.08 5.33(-9) 4.86

![image 485](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile485.png>)

![image 486](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile486.png>)

![image 487](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile487.png>)

![image 488](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile488.png>)

![image 489](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile489.png>)

![image 490](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile490.png>)

![image 491](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile491.png>)

![image 492](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile492.png>)

![image 493](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile493.png>)

![image 494](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile494.png>)

![image 495](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile495.png>)

![image 496](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile496.png>)

![image 497](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile497.png>)

![image 498](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile498.png>)

![image 499](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile499.png>)

![image 500](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile500.png>)

![image 501](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile501.png>)

![image 502](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile502.png>)

![image 503](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile503.png>)

![image 504](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile504.png>)

![image 505](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile505.png>)

![image 506](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile506.png>)

![image 507](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile507.png>)

![image 508](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile508.png>)

![image 509](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile509.png>)

![image 510](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile510.png>)

![image 511](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile511.png>)

![image 512](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile512.png>)

![image 513](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile513.png>)

![image 514](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile514.png>)

![image 515](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile515.png>)

![image 516](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile516.png>)

![image 517](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile517.png>)

![image 518](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile518.png>)

![image 519](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile519.png>)

![image 520](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile520.png>)

![image 521](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile521.png>)

![image 522](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile522.png>)

![image 523](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile523.png>)

![image 524](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile524.png>)

![image 525](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile525.png>)

![image 526](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile526.png>)

![image 527](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile527.png>)

![image 528](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile528.png>)

![image 529](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile529.png>)

![image 530](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile530.png>)

![image 531](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile531.png>)

![image 532](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile532.png>)

![image 533](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile533.png>)

![image 534](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile534.png>)

![image 535](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile535.png>)

![image 536](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile536.png>)

Table 4. The comparison of L1, L∞ errors and convergence order for the isentropic vortex problem of the Euler equations. The schemes are RK4-WENO5 and GRP4-HWENO5 with m × m cells. The results are given at time t = 2.

the interaction of vortices. Here we use S represents a shock, J a vortex sheet and R a rarefaction wave. The computation is implemented over the domain [0, 1] × [0, 1]. The output time is speciﬁed below case by case.

- a. Interaction of shocks and vortex sheets S12+J23−J34+S41−. The initial data are

(4.7)

(ρ, u, v, p)(x, y, 0) =

 



(1.4, 8, 20, 8), 0.5 < x < 1.0, 0.5 < y < 1.0, (−4.125, 4.125, −4.125, −4.125), 0 < x < 0.5, 0.5 < y < 1.0, (−4.125, −4.125, −4.125, 4.125), 0 < x < 0.5, 0 < y < 0.5, (1, 116.5, 116.5, 116.5), 0.5 < x < 1.0, 0 < y < 0.5.

The output time is 0.26.

- b. Interaction of shocks, rarefaction waves and vortex sheets J12+S23−J34−R41+ . The initial data are

(4.8) (ρ, u, v, p)(x, y, 0) =

 



(1, 2, 1.0625, 0.5179), 0.5 < x < 1.0, 0.5 < y < 1.0,

- (0, 0, 0, 0), 0 < x < 0.5, 0.5 < y < 1.0, (0.3, −0.3, 0.2145, −0.4259), 0 < x < 0.5, 0 < y < 0.5,
- (1, 1, 0.4, 0.4), 0.5 < x < 1.0, 0 < y < 0.5.


The output time is t = 0.055.

- c. Interaction of rarefaction waves and vortex sheets R12+ J23+J34−R41− . The initial data are


 

(1, 0.5197, 0.8, 0.5197), 0.5 < x < 1.0, 0.5 < y < 1.0, (0.1, −0.6259, 0.1, 0.1), 0 < x < 0.5, 0.5 < y < 1.0, (0.1, 0.1, 0.1, −0.6259), 0 < x < 0.5, 0 < y < 0.5, (1, 0.4, 0.4, 0.4), 0.5 < x < 1.0, 0 < y < 0.5.

- (4.9) (ρ, u, v, p)(x, y, 0) =




The output time is 0.3.

From the results we can see that this scheme can capture very small scaled vortices resulting from the interaction of vortex sheets. The resolution of vortices is comparable to that by the adaptive moving mesh GRP method (cf. [10]).

# b

# a

| |
|---|


| |
|---|


0.9

0.9

0.8

0.8

0.7

0.7

0.6

0.6

0.5

0.5

y

y

0.4

0.4

0.3

0.3

0.2

0.2

0.1

0.1

0.2 0.4 0.6 0.8

0.2 0.4 0.6 0.8

x

x

# c

# d

0.9

0.55

0.8

0.7

0.5

0.6

0.5

0.45

y

y

0.4

0.4

0.3

0.2

0.35

0.1

0.3

0.2 0.4 0.6 0.8

0.3 0.35 0.4 0.45 0.5 0.55 0.6

x

x

Figure 4.5. The density contours of three 2-D Riemann problems computed with GRP4-HWENO5. a. [J12+S23−J34−R41+ ] with 200×200 cells. b. [S12+J23−J34+S41−] with 300 × 300 cells. c. [R12+ J23+J34−R41− ] with 500 × 500 cells. d. Local enlargement of c.

- Example 9. The double mach reﬂection problem. This is again a standard test problem to display the performance of high resolution schemes. The computational domain for this problem is [0, 4] × [0, 1], and [0, 3] × [0, 1] is shown. The reﬂection wall lies at the


bottom of the computaional domain starting from x = 16. Initially a right-moving Mach 10 shock is positioned at x = 16, y = 0 and makes a π3 angle with the x-axis. The results are shown in Figures 4.6 and 4.7 with excellent performance.

![image 537](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile537.png>)

![image 538](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile538.png>)

![image 539](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile539.png>)

0.9

0.8

0.7

0.6

0.5

y

0.4

0.3

0.2

0.1

0.5 1 1.5 2 2.5

x

Figure 4.6. The contours of the density for the double mach reﬂection problem. GRP4-HWENO5 is implemented with 960 × 240 cells and the result is shown at t = 0.2. 30 contours are drawn.

1

0.9

0.8

0.7

0.6

0.5

y

0.4

0.3

0.2

0.1

0.5 1 1.5 2 2.5

x

Figure 4.7. The contours of the density of the double mach reﬂection problem. GRP2-HWENO5 is implemented with 1920 × 480 cells and the result is shown at t = 0.2. 30 contours are drawn.

- Example 10. The shock vortex interaction problem This example describes the interaction between a stationary shock and a vortex, the computational domain is taken to be [0, 2] × [0, 1]. A stationary Mach 1.1 shock is positoned at x = 0.5 and normal to the xaxis. Its left state is (ρ, u, v, p) = (1, √γM, 0, 1), where M is the mach number of the shock.


![image 540](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile540.png>)

A small vortex is superposed to the ﬂow left to the shock and centers at (xc, yc) = (0.25, 0.5). The vortex can be considered as a perturbation to the mean ﬂow. The perturbations to the

velocity (u, v), the temperature (T = pρ) and the entropy (S = ρp

) are: (δu, δv) = rǫ

![image 541](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile541.png>)

![image 542](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile542.png>)

γ

eα(1−τ2)(¯y, −x¯),

![image 543](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile543.png>)

c

2

δT = −(γ−1)ǫ

4αγ e2α(1−τ2), δS = 0. In our case, we set ǫ = 0.3 and α = 0.204. The computation is performed on a 400 × 100 uniform mesh. The results (the pressure contours) are shown in Figure 4.8.

![image 544](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile544.png>)

t=0.05

t=0.20

- 0.8

- 1


- 0.8

- 1


- 0.6


0.6

y

y

0.4

0.4

0.2

0.2

0

0

0 0.2 0.4 0.6 0.8 1

0 0.2 0.4 0.6 0.8 1

x

x

t=0.35

- 0.8

- 1


0.6

y

0.4

0.2

0

0 0.2 0.4 0.6 0.8 1

x

Figure 4.8. The contours of the pressure for the shock vortex interaction problem. GRP4-HWENO5 with 400×200 cells is implemented and 30 contours are drawn.

5. Discussions and Prospectives

This paper proposes a two-stage fourth order accurate temporal discretization for timedependent problems based on the L-W type ﬂow solvers. The particular applications are given for hyperbolic conservation laws. Based on HWENO interpolation technology [17], a scheme with a ﬁfth order accuracy in space and a fourth order accuracy in time is developed. A number of numerical examples are provided to validate the accuracy of the scheme and its computational performance for complex ﬂow problems.

The current temporal discretization is diﬀerent from the classical R-K approach. As discussed in Sections 2 and 3, the present approach is of the Hermite type while the R-K approach is of Simpson type. The L-W approach with coupled space and time evolution is the basis for the development of the current high order method. Our approach can be viewed as the extension of the L-W method from second order to even higher order accuracy, without using successive replacement of temporal derivatives by spatial derivatives in the one-stage method. This technique is particularly useful for nonlinear systems.

In this paper we just apply this approach to hyperbolic conservation laws in the ﬁnite volume framework over rectangular meshes. However, this approach can be applied to any time-dependent problems as long as L-W type solvers are available over any type of computational mesh. In the future studies, we will extend this approach to other formulations, e.g., DG formulation [14], to other systems e.g., the Navier-Stokes equations [8].

This work is just a starting point for the design of high order accurate methods and a lot of theoretical problems remain for the further study, such as numerical stability. Nevertheless, the numerical experiments clearly show that the current fourth order scheme can use a CFL number as large as that for the second order GRP scheme. Indeed, the CFL number can be taken even larger than 1/2 if the waves computed are not very strong. The large time step, in comparison with other high order schemes, does not decrease the accuracy of the scheme. So this approach will be eﬃcient for the simulation of turbulence ﬂows with multiscale structures by taking a large time step and the coupling of the spatial and temporal numerical ﬂow evolution.

Appendix A. The GRP solver

This appendix includes the GRP solver used in the coding process just for completeness and readers’ convenience. The details can be found in [5] for the Euler equations and [6] for general hyperbolic systems,

- (A.1) ut + f(u)x = g(u, x),


where g(u, x) is a source term. This paper focuses on the homogeneous case, g(u, x) ≡ 0 for 1-D case. As far as 2-D case is concerned with, the eﬀect tangential to cell interfaces can be regarded as a source and therefore the 2-D GRP solver can be derived using the similar idea to that for 1-D GRP solver.

- A.1. 1-D GRP. The 1-D GRP solver assumes that the initial data consist of two pieces of polynomials,


- (A.2) u(x, 0) = 

 

u−(x), x < 0, u+(x), x > 0,

where u±(x) are two polynomials with limiting states

- (A.3)

uℓ = lim

x→0−0

u−(x), ur = lim

x→0+0

u+(x); u′ℓ = lim

x→0−0

u′−(x), u′r = lim

x→0+0

u′+(x).

In the present study, we use the HWENO method in [17] to construct the initial data and therefore u±(x) are two pieces of polynomials of order ﬁve.

The GRP solver has two versions: (i) Acoustic version; (ii) Genuinely nonlinear version.

- A.1.1. Acoustic GRP solver. The acoustic GRP deals with weak discontinuities or smooth ﬂows and assumes that

(A.4) uℓ − ur ≪ 1. However, we emphasize that the diﬀerence u′ℓ − u′r is not necessarily small. Then we denote by (A.5) u0 ≈ uℓ ≈ ur, and linearize (A.1) around u0 as (A.6) ut + A(u0)ux = 0, A(u0) :=

∂f(u0) ∂u

![image 545](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile545.png>)

.

Then the instantaneous time derivative of u is computed as, (A.7)

∂u ∂t 0

![image 546](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile546.png>)

:= lim

t→0+0

∂u ∂t

![image 547](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile547.png>)

(0, t) = −[RΛ+R−1u′ℓ + RΛ−R−1u′r],

where Λ = diag(λ1, · · · , λm), λi, i = 1, · · · , m are the eigenvalues of A(u0), R is the (left) eigenmatrix of A(u0), Λ+ = diag(max(λi, 0)), Λ− = diag(min(λi, 0)).

The acoustic GRP is named as the G1 scheme in the series of GRP papers and it is consistent with the ADER solver by Toro [22].

- A.1.2. Nonlinear GRP solver. As the jump at x = 0 is large, the acoustic GRP is not suﬃcient to resolve the resulting strong discontinuities. Any “rough” approximation is dangerous




since the error is measured with jump ur − ur , which is not proportional to the mesh size in the practical computation and may lead to large numerical discrepancy. Therefore, we have to analytically solve the associated generalized Riemann problem (A.1)-(A.2) and derive the “genuinely” nonlinear GRP solver, which is named as the G∞ GRP. This version is interpreted as the L-W approach plus the tracking of strong discontinuities.

Here we include the resolution of GRP (A.1)-(A.2) for the Euler equations (4.3). The instantaneous value u0 is obtained by the Riemann solver and (∂u/∂t)0 is obtained by solving a pair of algebraic equations essentially,

- (A.8)

aℓ

∂v ∂t 0

![image 548](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile548.png>)

+ bℓ

∂p ∂t 0

![image 549](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile549.png>)

= dℓ,

ar

∂v ∂t 0

![image 550](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile550.png>)

+ br

∂p ∂t 0

![image 551](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile551.png>)

= dr,

where the coeﬃcients ai, bi, di, i = 1, 2, are given explicitly in terms of the initial data (A.2), and their formulae can be found in [5].

Since the variation of entropy s is precisely quantiﬁed, the instantaneous time derivative of the density is then obtained using the equation of state p = p(ρ, s),

- (A.9) dp = c2dρ +

∂p ∂s

![image 552](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile552.png>)

ds.

- A.2. Quasi-1-D GRP solver. As the two-dimensional case are dealt with, we need to solve a so-called quasi-1-D GRP


- (A.10)

ut + f(u)x + g(u)y = 0,

u(x, y, 0) =

uℓ(x, y), x < 0, ur(x, y) x > 0,

where uℓ(x, y) and ur(x, y) are two polynomials deﬁned on the two neighboring computational cells, respectively. Since we just want to construct the ﬂux normal to cell interfaces, the tangential eﬀect can be regarded as a source. Therefore, we rewrite (A.10) as

- (A.11)


ut + f(u)x = −g(u)y,

uℓ(x, y˜), x < 0, ur(x, y˜) x > 0,

u(x, y,˜ 0) =

by ﬁxing a y-coordinate. That is, we solve 1-D GRP at a point (0, y˜) on the interface, by considering the eﬀect tangential to the interface x = 0. The value g(u)y at (0, y˜) takes account of the local wave propagation.

Again, the quasi 1-D GRP solver for solving (A.10), particularly for the Euler equations (4.6), has the following two versions. The diﬀerence from 1-D version is that the multidimensional eﬀect is included.

- A.2.1. Quasi-1-D acoustic case. At any point (0, y˜), if uℓ(0−0, y˜) ≈ ur(0+0, y˜) and  ∇uℓ =  ∇ur , we view it as a quai-1-D acoustic case. Denote u0 := uℓ(0 − 0, y˜) ≈ ur(0 + 0, y˜) and A(u0) = ∂∂uf (u0). We make the decomposition A(u0) = RΛR−1, where Λ = diag{λi}, R is


![image 553](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile553.png>)

the (left) eigenmatrix of A(u0). Then the acoustic GRP solver takes

- (A.12)

∂u ∂t (0,y,˜ 0)

![image 554](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile554.png>)

= −RΛ+R−1

∂uℓ ∂x (0−0,y˜) − RI+R−1

![image 555](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile555.png>)

∂g(uℓ)

![image 556](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile556.png>)

∂y (0−0,y˜) −RΛ−R−1

∂ur ∂x (0+0,y˜) − RI−R−1

![image 557](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile557.png>)

∂g(ur) ∂y (0+0,y˜)

![image 558](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile558.png>)

,

where Λ+ = diag{max(λi, 0)}, Λ− = diag{min(λi, 0)}, I+ = 21diag{1 + sign(λi)}, I− =

![image 559](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile559.png>)

- 1

![image 560](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile560.png>)

- 2diag{1 − sign(λi)}.


- A.2.2. Quasi-1-D nonlinear GRP solver. At any point (0, y˜), if the diﬀerence uℓ(0−0, y˜)− ur(0+0, y˜) is large, we regard it as the genuinely nonlinear case and have to solve the quasi 1-D GRP analytically. A key ingredient is how to understand g(u)y. Here we construct the quasi 1-D GRP solver by two steps.


(i) We solve the local 1-D planar Riemann problem for

- (A.13)

vt + f(v)x = 0, t > 0,

v(x, y,˜ 0) =

uℓ(0 − 0, y˜), x < 0, ur(0 + 0, y˜), x > 0,

to obtain the local Riemann solution u0 = v(0, y,˜ 0 + 0). Just as in the acoustic case, we decompose A(u0) = ∂∂uf (u0) = RΛR−1. Then we set

![image 561](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile561.png>)

- (A.14) h(x, y˜) =

 



−RI+R−1

∂g(uℓ) ∂y (0−0,y˜)

![image 562](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile562.png>)

, x < 0,

−RI−R−1

∂g(ur) ∂y (0+0,y˜)

![image 563](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile563.png>)

, x > 0,

where I± are deﬁned the same as in (A.12). (ii) We solve the quasi 1-D GRP

- (A.15)


ut + f(u)x = h(x, y˜), t > 0,

uℓ(x, y˜), x < 0, ur(x, y˜), x > 0,

u(x, y,˜ 0) =

to obtain ∂∂tu(0, y,˜ 0 + 0). The details can be found in [6].

![image 564](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile564.png>)

Acknowlegement

The authors appreciate Yue Wang and Kun Xu for their careful reading, which greatly improves the English presentation. Jiequan Li is supported by by NSFC (No. 11371063, 91130021), the doctoral program from the Education Ministry of China (No. 20130003110004) and the Innovation Program from Beijing Normal University (No. 2012LZD08).

References

- [1] R. Abgrall, Residual distribution schemes: current status and future trends, Comput. & Fluids, 35

(2006), 641–669.

- [2] T. J. Barth and H. Deconinck, Herman (Eds.), High-Order Methods for Computational Physics, Lecture Notes in Computational Science and Engineering, Springer-Verlag, 1999.
- [3] M. Ben-Artzi and J. Falcovitz, A second-order Godunov-type scheme for compressible ﬂuid dynamics, J. Comput. Phys. , 55 (1984), 1–32.
- [4] M. Ben-Artzi and J. Falcovitz, Generalized Riemann problems in computational ﬂuid dynamics, Cambridge Monographs on Applied and Computational Mathematics, 11, Cambridge University Press, Cambridge, 2003.
- [5] M. Ben-Artzi, J. Q. Li and G. Warnecke, A direct Eulerian GRP scheme for compressible ﬂuid ﬂows, J. Comp. Phys., 218 (2006), 19–43.
- [6] M. Ben-Artzi and J. Q. Li, Hyperbolic conservation laws: Riemann invariants and the generalized Riemann problem, Numerische Mathematik, 106 (2007), 369–425.
- [7] B. Cockburn and C.-W. Shu, TVB Runge-Kutta local projection discontinuous Galerkin ﬁnite element method for conservation laws. II. General framework, Math. Comp., 52 (1989), 411–435.
- [8] Z. F. Du and J. Q. Li, A Novel Two-Stage Fourth Order Temporal Discretization Based on the LaxWendroﬀ Approach, II. Viscous compressible ﬂuid ﬂows, work in preparation, 2016.
- [9] S. K. Godunov, A ﬁnite diﬀerence method for the numerical computation and disontinuous solutions of the equations of ﬂuid dynamics, Mat. Sb. 47 (1959), 271–295.
- [10] E. Han, J. Q. Li and H. Z. Tang, Accuracy of the adaptive GRP scheme and the simulation of 2D Riemann problem for compressible Euler equations, Comm. Comp. Phys., Vol. 10, no. 3 (2011), 577–606.
- [11] A. Harten, B. Engquist, S. Osher, and S. Chakravarthy, Uniformly high-order accurate essentially nonoscillatory schemes, III. J. Comput. Phys., 71 (1987), no. 2, 231–303.
- [12] G. S. Jiang, and C-W. Shu, Eﬃcient implementation of weighted ENO schemes, J. Comput. Phys., 126

(1996), 202–228.

- [13] P. Lax and B. Wendroﬀ, Systems of Conservation Laws, Comm. Pure Appl. Math., Vol. XIII (1960), 217–237.
- [14] J. Q. Li and Y. Wang, A two-stage fourth order time-accurate discretization of DG-GRP method for hyperbolic conservation laws, submitted, 2015.
- [15] X. D. Liu, S. Osher and T. Chan, Weighted essentially non-oscillatory schemes, J. Comput. Phys., 115

(1994), no. 1, 200–212.

- [16] K. Prendergast and K. Xu, Numerical hydrodynamics from gas-kinetic theory, J. Comput. Phys., 109

(1993), no. 1, 53–66.

- [17] J. X. Qiu, and C-W. Shu, Hermite WENO schemes and their application as limiters for Runge-Kutta discontinuous Galerkin method: one-dimensional case, J. Comput. Phys. 193 (2004), 115–135; II. Two dimensional case, Comput. & Fluids, 34 (2005), 642–663.
- [18] C.-W. Shu and S. Osher, Eﬃcient implementation of essentially nonoscillatory shock-capturing schemes, II. J. Comput. Phys., 83 (1989), 32–78.
- [19] J. Shen, T. Tang and L.-L. Wang, Spectral methods. Algorithms, analysis and applications, Springer Series in Computational Mathematics, 41, Springer, Heidelberg, 2011.
- [20] H. Z. Tang and T. G. Liu, A note on the conservative schemes for the Euler equations, J. Comp. Phys., 218 (2006), no.1, 451–459.
- [21] E. F. Toro, Riemann solvers and numerical methods for ﬂuid dynamics: A practical introducition, Springer, 1997.
- [22] E. F. Toro and V. A. Titarev, Derivative Riemann solvers for systems of conservation laws and ADER methods. J. Comput. Phys., 212 (2006), 150–165.
- [23] B. van Leer, Towards the ultimate conservative diﬀerence scheme. V. A second-order sequel to Godunov’s method, J. Comp. Phys., 32 (1979), 101–136.
- [24] K. Xu and J. C. Huang, A uniﬁed gas-kinetic scheme for continuum and rareﬁed ﬂows. J. Comput. Phys., 229 (2010), no. 20, 7747–7764.


Jiequan Li: Laboratory of Computational Physics, Institute of Applied Physics and Computational Mathematics, Beijing, P. R. China; Email: li jiequan@iapcm.ac.cn

![image 565](<2015-li-two-stage-fourth-order-time-accurate_images/imageFile565.png>)

Zhifang Du: School of Mathematical Sciences, Beijing Normal University, 100875, P. R. China; Email: du@mail.bnu.edu.cn

