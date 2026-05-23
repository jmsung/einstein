## Explicit Strong Stability Preserving Multistage Two-Derivative Time-Stepping Schemes

# arXiv:1504.07599v3[math.NA]23Mar2016

Andrew J. Christlieb1, Sigal Gottlieb2, Zachary Grant2∗, David C. Seal3

1Department of Computational Mathematics Science and Engineering, Department of Electrical Engineering, and Department of Mathematics, Michigan State University 2Department of Mathematics, University of Massachusetts, Dartmouth 3Department of Mathematics, U.S. Naval Academy.

###### Abstract

High order strong stability preserving (SSP) time discretizations are advantageous for use with spatial discretizations with nonlinear stability properties for the solution of hyperbolic PDEs. The search for high order strong stability time-stepping methods with large allowable strong stability time-step has been an active area of research over the last two decades. Recently, multiderivative time-stepping methods have been implemented with hyperbolic PDEs. In this work we describe suﬃcient conditions for a two-derivative multistage method to be SSP, and ﬁnd some optimal SSP multistage two-derivative methods. While explicit SSP Runge–Kutta methods exist only up to fourth order, we show that this order barrier is broken for explicit multi-stage two-derivative methods by designing a three stage ﬁfth order SSP method. These methods are tested on simple scalar PDEs to verify the order of convergence, and demonstrate the need for the SSP condition and the sharpness of the SSP time-step in many cases.

### 1 Introduction

#### 1.1 SSP methods

When numerically approximating the solution to a hyperbolic conservation law of the form Ut + f(U)x = 0, (1)

diﬃculties arise when the exact solution develops sharp gradients or discontinuities. Signiﬁcant eﬀort has been expended on developing spatial discretizations that can handle discontinuities [7], especially for high-order methods. These discretizations have special nonlinear non-inner-product stability properties, such as total variation stability or positivity, which ensure that when the semi-discretized equation

ut = F(u), (2)

(where u is a vector of approximations to U) is evolved using a forward Euler method, the numerical solution satisﬁes the desired strong stability property,

un + ∆tF(un) ≤ un , 0 ≤ ∆t ≤ ∆tFE, (3) where · is any desired norm, semi-norm, or convex functional.

In place of the ﬁrst order time discretization (3), we typically require a higher-order time integrator, but we still wish to ensure that the strong stability property un+1 ≤ un is satisﬁed, perhaps under a modiﬁed time-step restriction, where un is a discrete approximation to U at time tn. In [32] it was observed that some Runge– Kutta methods can be decomposed into convex combinations of forward Euler steps, so that any convex functional

∗Corresponding author: zgrant@umassd.edu

property satisﬁed by (3) will be preserved by these higher-order time discretizations. For example, the s-stage explicit Runge–Kutta method [33],

y(0) = un, y(i) =

- i−1
- j=0


un+1 = y(s)

αi,jy(j) + ∆tβi,jF(y(j)) , i = 1, ..., s (4)

can be rewritten as convex combination of forward Euler steps of the form (3). If all the coeﬃcients αi,j and βi,j are non-negative, and provided αi,j is zero only if its corresponding βi,j is zero, then each stage is bounded by

y(i) =

- i−1
- j=0


αi,jy(j) + ∆tβi,jF(y(j)) ≤

- i−1
- j=0


βi,j αi,j

αi,j y(j) + ∆t

F(y(j) .

F(y(j)) ≤ y(j) for αβi,j

Noting that each y(j) + ∆tαβi,j

∆t ≤ ∆tFE, and by consistency j i−=01 αi,j = 1, we have un+1 ≤ un as long as

i,j

i,j

∆t ≤ C∆tFE ∀i, j, (5) where C = min αβi,j

. (We employ the convention that if any of the β’s are equal to zero, the corresponding ratios are considered inﬁnite.) The resulting time-step restriction is a combination of two distinct factors: (1) the term ∆tFE that depends on the spatial discretization, and (2) the SSP coeﬃcient C that depends only on the timediscretization. Any method that admits such a decomposition with C > 0 is called a strong stability preserving (SSP) method.

i,j

This convex combination decomposition was used in the development of second and third order explicit Runge– Kutta methods [33] and later of fourth order methods [34, 16] that guarantee the strong stability properties of any spatial discretization, provided only that these properties are satisﬁed when using the forward Euler (ﬁrst derivative) condition in (3). Additionally, the convex combination approach also guarantees that the intermediate stages in a Runge–Kutta method satisfy the strong stability property as well.

The convex combination approach clearly provides a suﬃcient condition for preservation of strong stability. Moreover, it has also be shown that this condition is necessary [4, 5, 11, 12]. Much research on SSP methods focuses on ﬁnding high-order time discretizations with the largest allowable time-step ∆t ≤ C∆tFE by maximizing the SSP coeﬃcient C of the method. It has been shown that explicit Runge–Kutta methods with positive SSP coeﬃcient cannot be more than fourth-order accurate [20, 28]; this led to the study of other classes of explicit SSP methods, such as methods with multiple steps. Explicit multistep SSP methods of order p > 4 do exist, but have severely restricted time-step requirements [7]. Explicit multistep multistage methods that are SSP and have order p > 4 have been developed as well [17, 2].

Recently, multi-stage multiderivative methods have been proposed for use with hyperbolic PDEs [29, 37]. The question then arises as to whether these methods can be strong stability preserving as well. Nguyen-Ba and colleagues studied the SSP properties of the Hermite-Birkoﬀ-Taylor methods with a set of simpliﬁed base conditions in [23]. In this work we consider multistage two-derivative methods and develop suﬃcient conditions for strong stability preservation for these methods, and we show that explicit SSP methods within this class can break this well-known order barrier for explicit Runge–Kutta methods. Numerical results demonstrate that the SSP condition is useful in preserving the nonlinear stability properties of the underlying spatial discretization and that the allowable time-step predicted by the SSP theory we developed is sharp in many cases.

#### 1.2 Multistage multiderivative methods

To increase the possible order of any method, we can use more steps (e.g. linear multistep methods), more stages (e.g. Runge–Kutta methods), or more derivatives (Taylor series methods). It is also possible to combine these

approaches to obtain methods with multiple steps, stages, and derivatives. Multistage multiderivative integration methods were ﬁrst considered in [24, 38, 35], and multiderivative time integrators for ordinary diﬀerential equations have been developed in [30, 31, 14, 15, 22, 25, 3], but only recently have these methods been explored for use with partial diﬀerential equations (PDEs) [29, 37]. In this work, we consider explicit multistage two-derivative time integrators as applied to the numerical solution of hyperbolic conservation laws.

We consider the system of ODEs (2) resulting from the spatial discretization of a hyperbolic PDE of the form (1). We deﬁne the one-stage, two-derivative building block method un+1 = un + α∆tF(un) + β∆t2F˙ (un) where α ≥ 0 and β ≥ 0 are coeﬃcients chosen to ensure the desired order. This method can be at most second order, with coeﬃcients α = 1 and β = 12. This is the second-order Taylor series method. To obtain higher order explicit methods, we can add more stages:

- i−1
- j=1


y(i) = un + ∆t

s

un+1 = un + ∆t

j=1

aijF(y(j)) + ∆taˆijF˙ (y(j)) , i = 1, ..., s (6)

bjF(y(j)) + ∆tˆbjF˙ (y(j)) .

We can write the coeﬃcients in matrix vector form, where

















- ˆb1
- ˆb2


- b1
- b2


0 0 . 0 a21 0 . 0 . . . .

0 0 . 0 aˆ21 0 . 0 . . . .

, ˆb =

, Aˆ =

.

A =

, b =

 

 

 

 

 

 

. bs

. ˆbs

 

 

as1 as2 . 0

aˆs1 aˆs2 . 0

We let c = Ae and cˆ = Aˆe, where e is a vector of ones. These coeﬃcients are then selected to attain the desired order, based on the order conditions written in Table 1 as described in [3, 6].

- Remark 1. In this work, we focus on multistage two-derivative methods as time integrators for use with hyperbolic PDEs. In this setting, the operator F is obtained by a spatial discretization of the term Ut = −f(U)x to obtain the system ut = F(u). This is the typical method-of-lines approach, and SSP methods were introduced in the context of this approach. The computation of the second derivative term F˙ should follow directly from the deﬁnition of F, where we compute F˙ = F(u)t = Fuut = FuF. In practice, the calculation of Fu may be computationally prohibitive, as for example in the popular WENO method where F has a highly nonlinear dependence on u.


Instead, we adopt a Lax-Wendroﬀ type approach, where we use the fact that the system of ODEs arises from the PDE (1) to replace the time derivatives by the spatial derivatives, and discretize these in space. This approach begins with the observation that F(u) = ut = Ut + O(∆xm) (for some integer m). The term F(u) is typically computed using a conservative spatial discretization Dx applied to the ﬂux:

F(u) = Dx(−f(u)). Next we approximate

F(u)t = utt ≈ Utt = −f(U)xt = (−f(U)t)x = −f (U)Ut x ≈ D˜x −f (u)ut , where a (potentially diﬀerent) spatial approximation D˜x is used. This means that

F(u)t = utt = Utt + O(∆xn) = F˙ + O(∆xr) (for some integers n and r).

Since Ft = F˙ + O(∆xr), we will not necessarily obtain the time order ∆tp when we satisfy the order conditions in Table 1, as our temporal order is polluted by spatial errors as well. The concern about the Lax-Wendroﬀ approach is that the order conditions in Table 1 are based on the assumption that F˙ = Ft, which is not exactly correct in our case, thus introducing additional errors. However, these errors are of order r in space, so that in practice, as long as the spatial errors are smaller than the temporal errors, we expect to see the correct order of accuracy in time.

To verify this, in Section 4.2 we perform numerical convergence studies of these temporal methods where F˙ is approximated by high order spatial schemes and compare the errors from these methods to those from well-known SSP Runge–Kutta methods. We observe that if the spatial and temporal grids are reﬁned together, the expected order of accuracy is demonstrated. Furthermore, if the spatial grid is held ﬁxed but the spatial discretization is highly accurate, the correct time-order is observed until the time error falls below the spatial error. We conclude that in practice, it is not necessary to compute Ft exactly, and that the use of a Lax-Wendroﬀ type procedure that replaces the temporal derivatives by spatial derivatives and discretizes each of these independently, does not destroy the temporal accuracy.

This observation is not new: many other methods have adopted this type of approach and obtained genuine high-order accuracy. Such methods include the original Lax-Wendroﬀ method [21], ENO methods [9], ﬁnite volume ADER methods [36], the ﬁnite diﬀerence WENO Schemes in [27], and the Lax-Wendroﬀ discontinuous Galerkin schemes [26].

In the next section we will discuss how to ensure that a multistage two-derivative method will preserve these strong stability properties.

|p = 1<br><br>|bTe = 1|
|---|---|
|p = 2<br><br>|bTc + ˆbTe = 12<br><br>|
|p = 3|bTc2 + 2ˆbTc = 31 bTAc + bTcˆ+ ˆbTc = 61<br><br>|
|p = 4|bTc3 + 3ˆbTc2 = 41 bTcAc + bTccˆ+ ˆbTc2 + ˆbTAc + ˆbTcˆ = 81 bTAc2 + 2bTAcˆ + ˆbTc2 = 121 bTA2c + bTAcˆ+ bTAcˆ + ˆbTAc + ˆbTcˆ = 241<br><br>|
|p = 5<br><br>|bTc4 + 4ˆbTc3 = 51 bTc2Ac + bTc2cˆ+ ˆbTc3 + 2ˆbTcAc + 2ˆbTccˆ = 101 bTcAc2 + 2bTcAcˆ + ˆbTc3 + ˆbTAc2 + 2ˆbTAcˆ = 151 bTcA2c + bTcAcˆ+ bTcAcˆ + ˆbTcAc + ˆbTccˆ+ ˆbTA2c + ˆbTAcˆ+ ˆbTAcˆ = 301 bT(Ac)(Ac) + 2bTcAcˆ + bTcˆ2 + 2ˆbTcAc + 2ˆbTccˆ = 201 bTAc3 + 3bTAcˆ 2 + ˆbTc3 = 201 bTA(cAc) + bTA(ccˆ) + bTAcˆ 2 + bTAAcˆ + bTAˆcˆ+ ˆbTcAc + ˆbTccˆ = 401<br><br>bTA2c2 + 2bTAAcˆ + bTAcˆ 2 + ˆbTAc2 + 2ˆbTAcˆ = 601<br><br>bTA3c + bTA2cˆ+ bTAAcˆ + bTAAcˆ + bTAˆcˆ+ ˆbTA2c + ˆbTAcˆ+ ˆbTAcˆ = 1201<br><br><br>|


###### Table 1: Order conditions for multi-stage multiderivative methods of the form (6) as in [3].

### 2 The SSP condition for multiderivative methods

#### 2.1 Motivating Examples

To understand the strong stability condition for multiderivative methods, we consider the strong stability properties of a multiderivative building block of the form

un+1 = un + α∆tF(un) + β∆t2F˙ (un),

and begin with the simple linear one-way wave equation Ut = Ux. This equation has the property that its second derivative in time is, with the assumption of suﬃcient smoothness, also the second derivative in space:

Utt = (Ux)t = (Ut)x = Uxx.

We will use this convenient fact in a Lax-Wendroﬀ type approach to deﬁne F˙ (un) by a spatial discretization of Uxx.

For this problem, we deﬁne F by the original ﬁrst-order upwind method

1 ∆x

F(un)j :=

unj+1 − unj ≈ Ux(xj), (7a)

and F˙ by the second order centered discretization to Uxx:

1 ∆x2

F˙ (un)j :=

unj+1 − 2unj + unj−1 ≈ Uxx(xj). (7b)

These spatial discretizations are total variation diminishing (TVD) in the following sense: un+1 = un + ∆tF(un) is TVD for ∆t ≤ ∆x, (8a) un+1 = un + ∆t2F˙ (un) is TVD for ∆t ≤

√2 2

∆x. (8b)

- Remark 2. Note that we chose a second derivative F˙ in space that is not an exact derivative Ft(un) of F(un) in the method-of-lines formulation. However, as noted in Remark 1 and will be shown in the convergence studies, if the spatial and temporal grids are co-reﬁned, this provides a suﬃciently accurate approximation to F˙ (un). The exact derivative can be obtained by applying the upwind diﬀerentiation operator to the solution twice, which produces


1 ∆x2

Ft :=

unj+2 − 2unj+1 + unj .

However, computing F˙ = Ft using this formulation does not satisfy the condition (8b) for any value of ∆t. To establish the TVD properties of the multiderivative building block we decompose it:

un+1 = un + α∆tF(un) + β∆t2F˙ (un) = aun + α∆tF(un) + (1 − a)un + β∆t2F˙ (un)

β 1 − a

α a

∆t2F˙ (un) .

∆tF(un) + (1 − a) un +

= a un +

It follows that for any 0 ≤ a ≤ 1 this is a convex combination of terms of the form (8a) and (8b), and so

α a

β 1 − a

∆t2F˙ (un)

un+1 TV ≤ a un +

+ (1 − a) un +

∆tF(un)

TV

TV ≤ a un TV + (1 − a) un TV ≤ un TV

for time-steps satisfying ∆t ≤ αa ∆x and ∆t2 ≤ 12−βa∆x2. The ﬁrst restriction relaxes as a increases while the second becomes tighter as a increases, so that the value of a that maximizes these conditions occurs when these are equal.

This is given by

α α2 + 8β − α2 4β

α2 2β

α2 2β

a2 +

a −

= 0, =⇒ a =

. Using this SSP analysis, we conclude that

un + α∆tF(un) + β∆t2F˙ (un)

α2 + 8β − α 4β

≤ un TV for ∆t ≤

∆x. (9)

TV

Of course, for this simple example we can directly compute the value of ∆t for which the multiderivative building block is TVD. That is, with λ := ∆∆xt ≥ 0, we observe that

un+1 TV = (1 − αλ − 2βλ2)unj + (αλ + βλ2)unj+1 + βλ2unj−1 TV ≤ un TV , provided that

α2 + 8β − α 4β

1 − αλ − 2βλ2 ≥ 0 ⇐⇒ λ ≤

.

We see that for this case, the SSP bound is sharp: the convex combination approach provides us exactly the same bound as directly computing the requirements for total variation.

We wish to generalize this for cases in which the second derivative condition (8b) holds for ∆t ≤ K∆tFE where K can take on any positive value, not just

√2

2 . For the two-derivative building block method this can be done quite easily:

- Theorem 1. Given F and F˙ such that un + ∆tF(un) ≤ un for ∆t ≤ ∆tFE,


and

un + ∆t2F˙ (un) ≤ un for ∆t ≤ K∆tFE, the two-derivative building block

un+1 = un + α∆tF(un) + β∆t2F˙ (un) satisﬁes the monotonicity condition un+1 ≤ un under the time-step restriction

K 2β

α2K2 + 4β − αK ∆tFE.

∆t ≤

Proof. As above, we rewrite

α a

β 1 − a

∆t2F˙ (un) ,

un+1 = a un +

∆tF(un) + (1 − a) un +

which is a convex combination provided that 0 ≤ a ≤ 1. The time-step restriction that follows from this convex combination must satisfy αa ∆t ≤ ∆tFE and 1−βa∆t2 ≤ K2∆t2FE. The ﬁrst condition becomes ∆t ≤ αa ∆tFE while the second is ∆t ≤ 1−βaK∆tFE. We observe that on 0 ≤ a ≤ 1 the ﬁrst term encourages a larger a while the second term is less restrictive with a smaller a. The two conditions are balanced, and thus the allowable time-step is maximized, when we equate the right hand sides:

a α

=

1 − a β

αK 2β

K → a =

α2K2 + 4β − αK .

Now using the ﬁrst condition, ∆t ≤ αa ∆tFE we obtain our result.

| |
|---|


A more realistic motivating example is the unique two-stage fourth order method

∆t 2

u∗ = un +

F(un) +

∆t2 6

un+1 = un + ∆tF(un) +

∆t2 8

F˙ (un),

(F˙ (un) + 2F˙ (u∗)). (10)

The ﬁrst stage of the method is a Taylor series method with ∆2t, while the second stage can be written

∆t2 6

(F˙ (un) + 2F˙ (u∗))

un+1 = un + ∆tF(un) +

∆t2 8

∆t2 6

∆t 2

= a u∗ −

(F˙ (un) + 2F˙ (u∗))

F˙ (un) + (1 − a)un + ∆tF(un) +

F(un) −

1 − a2 1 − a

1 6 − a8 1 − a

∆t2 3a

∆t2F˙ (un) + a u∗ +

F˙ (u∗) .

= (1 − a) un +

∆tF(un) +

For 0 ≤ a ≤ 1 this is a convex combination of two terms. The ﬁrst term is of the form (9), which gives the time-step restriction

5 4

10 3

7 3 − 1 +

a 2

6 4 − 3a

a2 −

∆t ≤

a +

∆tFE.

The second is of the form (8b), so we have ∆t ≤ 32a∆tFE. We plot these two in Figure 1, and we observe that the ﬁrst term is decreasing in a (blue line) while the second term is increasing in a (red line). As a result, we obtain the optimal allowable time-step by setting these two equal, which yields a ≈ 0.3072182638002141 and the corresponding SSP coeﬃcient, C ≈ 0.6788426884782078. A direct computation of the TVD time-step for this case, which takes advantage of the linearity of the problem and the spatial discretization, gives the bound ∆t ≤ (√3 − 1) > 0.6788. This shows that, as we expect, the SSP condition is not always sharp.

The convex combination approach becomes more complicated when dealing with multi-stage methods. It is the most appropriate approach for developing an understanding of the strong stability property of a given method. However, it is not computationally eﬃcient for ﬁnding optimal SSP methods. In the following section, we show how to generalize the convex combination decomposition approach and we use this generalization to formulate an SSP optimization problem along the lines of [16, 19].

#### 2.2 Formulating the SSP optimization problem

As above, we begin with the hyperbolic conservation law (1) and adopt a spatial discretization so that we have the system of ODEs (2). The spatial discretization F is specially designed so that it satisﬁes the forward Euler (ﬁrst derivative) condition

Forward Euler condition un + ∆tF(un) ≤ un for ∆t ≤ ∆tFE, (11)

for the desired stability property indicated by the convex functional   ·  . For multiderivative methods, in addition to the ﬁrst derivative, we need to appropriately approximate the second derivative in time utt, to which we represent the discretization as F˙ . It is not immediately obvious what should be the form of a condition that would account for the eﬀect of the ∆t2F˙ term. Motivated by the examples in the previous sections, we choose the

Second derivative condition un + ∆t2F˙ (un) ≤ un for ∆t ≤ K∆tFE, (12)

where K is a scaling factor that compares the stability condition of the second derivative term to that of the forward Euler term. Given conditions (11) and (12), we wish to formulate suﬃcient conditions so that the multiderivative

method (6) satisﬁes the desired monotonicity condition under a given time-step. First, we write the method (6) in an equivalent matrix-vector form

y = eun + ∆tSF(y) + ∆t2SˆF˙ (y), (13) where

A ˆ 0 ˆbT 0

A 0 bT 0

and Sˆ =

S =

and e is a vector of ones. We are now ready to state our result:

- Theorem 2. Given spatial discretizations F and F˙ that satisfy (11) and (12), a two-derivative multistage method of the form (13) preserves the strong stability property un+1 ≤ un under the time-step restriction ∆t ≤ r∆tFE if satisﬁes the conditions


−1

r2 K2

Sˆ

e ≥ 0 (14a)

I + rS +

−1

r2 K2

Sˆ

S ≥ 0 (14b) r2 K2

r I + rS +

−1

r2 K2

Sˆ ≥ 0 (14c) for some r > 0. In the above conditions, the inequalities are understood component-wise. Proof. We begin with the method (13), and add the terms rSy and rˆSˆy to both sides to obtain

Sˆ

I + rS +

I + rS + rˆSˆ y = une + rS y +

∆t2 rˆ

∆t r

F(y) + rˆSˆ y +

y = R(eun) + P y +

∆t r

F(y) + Q y +

F˙ (y) ,

∆t2 rˆ

F˙ (y) ,

where

R = I + rS + rˆSˆ

−1

, P = rRS, Q = rRˆ S.ˆ

If the elements of P, Q, and Re are all non-negative, and if R + P + Q = I, then these three terms describe a convex combination of terms which are SSP, and the resulting value is SSP as well

∆t2 rˆ

∆t r

F˙ (y) ,

y ≤ R eun + P y +

F(y) + Q y +

√

rˆ∆tFE. As we observed above, the optimal time-step is given when these two are set equal, so we require r = K

under the time-step restrictions ∆t ≤ r∆tFE and ∆t ≤ K

√

rˆ. Conditions (14a)–(14c) now ensure that P ≥ 0, Q ≥ 0, and Re ≥ 0 component-wise for rˆ = Kr22 , and our method (13) preserves the strong stability condition

un+1 ≤ un under the time-step restriction ∆t ≤ r∆tFE.

| |
|---|


This theorem gives us the conditions for the method (13) to be SSP for any the time-step ∆t ≤ r∆tFE. This allows us to formulate the search for optimal SSP two-derivative methods as an optimization problem, similar to [16, 18, 7], where the aim is to ﬁnd C = max r such that the relevant order conditions (from Section 1.2) and SSP conditions (14a)-(14b) are all satisﬁed. Based on this, we wrote a Matlab optimization code for ﬁnding optimal two-derivative multistage methods [8], formulated along the lines of David Ketcheson’s code [19] for ﬁnding optimal SSP multistage multistep methods in [17, 2]. We used this to ﬁnd optimal SSP multistage two-derivative methods of order up to p = 5. However, we also used our observations on the resulting methods to formulate closed form representations of the optimal SSP multistage two-derivative methods. We present both the numerical and closed-form optimal methods in the following section.

- Remark 3. An alternative approach to deﬁning a MSMD SSP method is to begin with spatial discretization that satisﬁes the “Taylor series” condition, deﬁned by


un + ∆tF(un) +

- 1

- 2


∆t2F˙ (un) ≤ un for ∆t ≤ ∆tTS = K2∆tFE. (15)

This condition replaces (12), and allows us to rewrite (6) as convex combinations of forward Euler and Taylor series steps of the form (15). A similar optimization problem can be deﬁned based on this condition. This approach was adopted in [23].

This condition is more restrictive than what we consider in the present work. Indeed, if a spatial discretization satisﬁes conditions (11) as well as (12), then it will also satisfy condition (15), with K2 = K√K2 + 2−K. However, some methods of interest cannot be written using a Taylor series decomposition, including the two-stage fourth order method in (10). For these reasons, we do not explore this approach further, but we point out that we have experimented with this alternative formulation to generate some optimal SSP methods. Henceforth, we restrict our attention to spatial discretizations that satisfy (11) and (12).

### 3 Optimal SSP multiderivative methods

#### 3.1 Second order methods

Although we do not wish to use second order methods in our computations, it is interesting to consider the strong stability properties of these methods both as building blocks of higher order methods and as simple example that admit optimal formulations with simple formulas.

One stage methods. The second-order Taylor series method,

un+1 = un + ∆tF(un) +

- 1

- 2


∆t2F˙ (un), (16)

is the unique one-stage second-order method. Theorem 1 for the building block (9) with coeﬃcients α = 1 and β = 12 gives the condition ∆t ≤ C∆tFE with C = K√K2 + 2 − K2. Unlike the SSP single derivative Runge–Kutta methods, the SSP coeﬃcient is not just dependent on the time-stepping method, but also on the value K which comes from the second derivative condition (12). As noted above, the Taylor series method can serve as the basic building block for two-derivative methods, just as the ﬁrst-order FE can be used to build higher-order RK integrators.

Two stage methods. The optimal SSP two stage second order methods depends on the value of K in (12). A straightforward SSP analysis via convex combinations, and solving the equations for the order conditions allows us to formulate the optimal methods without using the optimization code [8]. However, we used the optimization code to verify our results.

If K ≤ 23 the optimal methods are of the form

1 r

u∗ = un +

∆tF(un), un+1 = un +

r − 1 2r

- 1

- 2


∆t (F(un) + F(u∗)) +

∆t2F˙ (un), (17) where

- 1

- 2


1 − K2 + 1 + 6K2 + K4 .

r =

These methods are SSP for C = r, where r > 1 whenever K > 0. Notice that if K = 0 we have r = 1 and our method reduces to the standard two stage second order Runge–Kutta method.

As K increases, the time-step restriction imposed by the condition (12) is alleviated, and consequently the optimal method includes more of the second derivative terms. If K ≥ 23 we get an optimal method

- 1

- 2


1 8

u∗ = un +

∆t2F˙ (un), un+1 = u∗ +

∆tF(un) +

- 1

- 2


1 8

∆tF(u∗) +

∆t2F˙ (u∗), (18)

which is simply two Taylor series steps with 12∆t in each one, and so has C = 2K√K2 + 2−2K2. We see in Figure 2 the SSP coeﬃcient C vs. K for the two methods above (in green and red respectively), and for many numerically

optimal methods in blue.

- 0

0.2

0.4

0.6

- 0.8

- 1


1.2

1.4

1.6

- 1.8

- 2


1.2

- 0.8
- 1


Timesteprestriction

SSPCoefficient

0.6

0.4

0.2

0

0 0.5 1 1.5 2 2.5 3 3.5 4 4.5 5

0 0.2 0.4 0.6 0.8 1

K

a

Figure 1: The time-step restriction for the two-stage fourth order method is the minimum of two terms, one of which is decreasing while the other is increasing in a.

Figure 2: The SSP coeﬃcient C as a function of the coeﬃcient K in (12) for the optimal two-stage two-derivative second order methods given in Section 3.1.

Note that (18) has four function evaluations compared to the three function evaluations above in (17). If we assume all the function evaluations cost the same, it will never pay oﬀ to use the second method, as the ﬁrst method is always more eﬃcient. However, if one has a special case where the cost of computing F˙ is negligible the second method may still be worthwhile.

For this method and all others, once we have the optimal Butcher arrays and the SSP coeﬃcient C = r, we can easily convert them to the Shu-Osher form as follows: % Given A, Ahat, b, bhat, and r, the Shu-Osher matrices are given by

z=0.0*b; I=eye(3);e=ones(3,1); S=[A,z; b’,0]; Shat=[Ahat,z; bhat’,0]; Ri=(I+r*S+(r^2/k^2)*Shat); v=Ri\e;

- P = r*(Ri\S);
- Q= r^2/k^2*(Ri\Shat);


#### 3.2 Third order methods

Many two-stage two-derivative third order methods exist. As above, the optimal C depends on the value of K in (12). Through numerical search using our optimization code [8], we found optimal methods for the range 0.1 ≤ K ≤ 5. Figure 3 (blue line) shows the SSP coeﬃcient C vs. K. We also solved the order conditions explicitly and analyzed the SSP conditions (14a)-(14c) to ﬁnd the values of the coeﬃcients of these methods as functions of r = C and K. These methods all have the form

u∗ = un + a∆tF(un) + aˆ∆t2F˙ (un),

un+1 = un + b1∆tF(un) + b2∆tF(u∗) + bˆ1∆t2F˙ (un) + bˆ2∆t2F˙ (u∗), (19) where the coeﬃcients satisfy

- a = r1 K√K2 + 2 − K2 a ˆ =

- 1

- 2


a2

- b2 = 2K


2(1− r1 )+r K

− 3rK22 b1 = 1 − b2 (20)

√

K2+2+K2

- 1

- 2


1 6a −

ˆb1 = 21 − 21ab2 − 61a ˆb2 =

ab2 Note that the ﬁrst stage is always a Taylor series method with ∆t replaced by a∆t, which is underscored by

the fact that SSP coeﬃcient is given by r = a1 K√K2 + 2 − K2 . The SSP conditions (14a)-(14c) provide the restrictions on the size of r, and thus on C = r. We observe that the condition that restricts us most here is the

non-negativity of Q3,1, and so we must select a value of r such that this value is zero. To do this, we select r to be the smallest positive root of p0 + p1r + p2r2 + p3r3 where the coeﬃcients pi are all functions of K

- p0 = 2K( K2 + 2 − 3K) + 4K3( K2 + 2 − K)

- p1 = −a0, p2 = (1 − a0)/(2K2), p3 = −


a0 2K + K

.

6K3

Some examples of the value of r as a function of K are given in Table 2. The Matlab script for this method is found in Appendix B.

|K 0.25 0.4 0.5 0.6 0.7 0.8 1.0 1.25 1.5 1.75 2.5 3 3.5 4 r 0.48 0.71 0.84 0.94 1.03 1.11 1.23 1.33 1.39 1.44 1.51 1.54 1.55 1.56<br><br>|
|---|


Table 2: The SSP coeﬃcient C = r for each K in the two-stage third order method (19).

The Shu-Osher representations of the methods can be easily obtained by using r and K to solve for rˆ, R, P, and Q. For example, for K = √12 we have r = 1.04 and the method in Butcher form has

a = 0.594223212099088, aˆ = 0.176550612898679,

b =

0.693972512991841 0.306027487008159

, ˆb =

0.128597465450411 0.189553898228989

.

The optimal Shu Osher formulation for these values is given by Re = (1, 0, 0)T,

- P =

 

0 0 0 0.618033988749895 0 0 0.271611333775367 0.318290138472780 0

 

- Q =


 

  .

0 0 0 0.381966011250105 0 0 0 0.410098527751853 0

1.6

1.4

1.2

SSPCoefficient

- 0.8

- 1


0.6

0.4

0.2

0

0 1 2 3 4 5

K

Figure 3: The SSP coeﬃcient vs. K for two stage methods. Third order methods are in blue, the fourth order methods are red.

- 0

- 0.5

- 1


- 1.5

- 2


SSPCoefficient

0 0.5 1 1.5 2 2.5

K

Figure 4: The SSP coeﬃcient vs. K for three stage methods. Fourth order methods are in blue (top line), the ﬁfth order methods in red (bottom line).

- 3.3 Fourth order methods


- 3.3.1 Fourth order methods: The two-stage fourth-order method

The two-stage two-derivative fourth order method (10) is unique; there is only one set of coeﬃcients that satisfy the fourth order conditions for this number of stages and derivatives. The method is

u∗ = un +

∆t 2

F(un) +

∆t2 8

F˙ (un)

un+1 = un + ∆tF(un) +

∆t2 6

(F˙ (un) + 2F˙ (u∗)).

The ﬁrst stage of the method is a Taylor series method with ∆2t, while the second stage can be written as a linear combination of a forward Euler and a second-derivative term (but not a Taylor series term). The SSP coeﬃcient

of this method is larger as K increases, as can be seen in Figure 3.

To ensure that the SSP conditions (14a)-(14c) are satisﬁed, we need to select the largest r so that all the terms are non-negative. We observed from numerical optimization that in the case of the two-stage fourth order method the term (Re)3 gives the most restrictive condition: if we choose r to ensure that this term is non-negative, all the other conditions are satisﬁed. Satisfying this condition, the SSP coeﬃcient C = r is given by the smallest positive root of the polynomial:

(Re)3 = r4 + 4K2r3 − 12K2r2 − 24K4r + 24K4. The Shu-Osher decomposition for the optimal method corresponding to this value of K is

u∗ = 1 −

4rK2 + r2 8K2

un +

r 2

un +

∆t r

F(un) +

r2 8K2

un +

K2 r2

∆t2F˙ (un) (21)

un+1 = r 1 −

r2 6K2

un +

∆t r

F(un) +

r2(4K2 − r2) 24K4

un +

K2 r2

∆t2F˙ (un) +

r2 3K2

u∗ +

K2 r2

∆t2F˙ (u∗) .

- 3.3.2 Fourth order methods: Three stage methods


If we increase the number of stages to three, we can construct entire families of methods that obtain fourth-order accuracy, and are SSP with a larger allowable time-step. For these methods, we were not able to ﬁnd closed

form solutions, but our optimization code [8] produced methods for various values of K. The SSP coeﬃcient as a function of K for these methods is given in Figure 3, and we give the coeﬃcients for selected methods in both Butcher array and Shu-Osher form in Appendix A.

#### 3.4 Fifth order methods

As mentioned above, it was shown that explicit SSP Runge–Kutta methods cannot have order p > 4 [20, 28]. This order barrier is broken by multiderivative methods. If we allow three stages and two-derivative we can obtain a ﬁfth order SSP method. The explicit three-stage ﬁfth order method has twelve coeﬃcients and sixteen order conditions that need to be satisﬁed. This is possible if some of the coeﬃcients are set to zero, which allows several of the order conditions to be repetitive and satisﬁed automatically. The methods resulting from our optimization routine all had the simpliﬁed form

u∗ = un + a21∆tF(un) + aˆ21∆t2F˙ (un)

u∗∗ = un + a31∆tF(un) + aˆ31∆t2F˙ (un) + aˆ32∆t2F˙ (u∗) (22) un+1 = un + ∆tF(un) + ∆t2 ˆb1F˙ (un) + ˆb2F˙ (u∗) + ˆb3F˙ (u∗∗) .

The coeﬃcients of the three-stage ﬁfth order method are then given as a one-parameter system, depending only on a21, that are related through

aˆ21 =

aˆ32 =

ˆb2 =

3/5 − a21 1 − 2a21

1 2

a221, a31 =

,

(35 − a21)2 a21(1 − 2a21)3 −

(35 − a21)2 (1 − 2a21)2 − aˆ32,

3 5 − a21

1 10

- 1

- 2


, aˆ31 =

(1 − 2a21)2

1 − 2a21 12a31(a31 − a21)

2a31 − 1 12a21(a31 − a21)

- 1

- 2 − ˆb2 − ˆb3.


, ˆb3 =

, ˆb1 =

To satisfy the SSP conditions (14a)-(14c), we must ensure that (Re)3 is non-negative. Based on the optimization code we observed that the extreme case of (Re)3 = 0 gives the optimal methods, and we can obtain a21 as a function of K and r through

K6 r6 −

2 K4

10 K4

40 K2

120 K2

r5 +

r4 +

r3 −

r2 − 240r + 240 .

a21 =

Now, we wish to ensure that Q3,1 is nonnegative. The SSP coeﬃcient C = r is then chosen as the largest positive root of

Q3,1 = 10r2a421 − (100K2 + 10r2)a321 + (130K2 + 3r2)a221 − 50K2a21 + 6K2. The Matlab script in Appendix C solves for the largest r that satisﬁes the SSP conditions (14a)-(14c), and then computes the coeﬃcients of the optimal methods both in Butcher array and Shu-Osher form. This approach yields the same optimal methods as those obtained by our optimization code [8]. In Figure 5 we show values of a21 and r for given values of K.

Once again, the Shu-Osher decomposition is needed for the method to be SSP, and is easily obtained. For example, for K = √12 we have r = 0.6747 and the method becomes

  

   , P =

  

  

1.0 0.2369970626512336 0.7810723816004148 0.0

0 0 0 0 0.5064804704259125 0 0 0 0.1862033791874200 0 0 0 0.5769733539128722 0 0 0

Re =

(23)

1

0.8

SSPCoefficient

0.6

- 0.4


0.2

0

0 0.5 1 1.5 2 2.5

K

|K a21 C| |K a21 C|
|---|---|---|
|0.1 0.7947 0.1452<br>0.2 0.7842 0.2722<br>0.3 0.7751 0.3814<br>0.4 0.7674 0.4741<br>0.5 0.7609 0.5520<br>0.6 0.7555 0.6171<br>0.7 0.7510 0.6712<br>0.8 0.7472 0.7162<br>0.9 0.7441 0.7537 1.0 0.7415 0.7851<br>| |1.1 0.7393 0.8114<br>1.2 0.7374 0.8335<br>1.3 0.7359 0.8523<br>1.4 0.7346 0.8683<br>1.5 0.7334 0.8819<br>1.6 0.7324 0.8937<br>1.7 0.7316 0.9039<br>1.8 0.7309 0.9127<br>1.9 0.7302 0.9205 2.0 0.7296 0.9273<br>|


- Figure 5: SSP coeﬃcients for three-stage ﬁfth-order methods. Left: the SSP coeﬃcient as a function of K for three stage ﬁfth order methods. Right: a table of a21 and the SSP coeﬃcient C, for diﬀerent values of K as deﬁned in (22). The code to generate the coeﬃcients in Butcher and Shu-Osher form is given in the appendix.


  

   .

0 0 0 0 0.2565224669228537 0 0 0 0 0.0327242392121651 0 0 0.0615083849004797 0.0803574544380432 0.2811608067486047 0

Q =

These coeﬃcients as well as the coeﬃcients for the optimal method for any value of K can be easily obtained to high precision by the Matlab code in Appendix C.

### 4 Numerical Experiments

- 4.1 Numerical veriﬁcation of the SSP properties of these methods


- 4.1.1 Example 1: Linear advection with ﬁrst order TVD spatial discretization


As a ﬁrst test case, we consider linear advection, Ut − Ux = 0, with a ﬁrst order ﬁnite diﬀerence for the ﬁrst derivative and a second order centered diﬀerence for the second derivative deﬁned in (7)

unj+1 − 2unj + unj−1 ∆x2 ≈ Uxx(xj).

unj+1 − unj ∆x ≈ Ux(xj), and F˙ (un)j :=

F(un)j :=

Recall from (8) that this ﬁrst-order spatial discretization satisﬁes the Forward Euler condition unj +1 = unj + ∆∆xt unj+1 − unj is TVD for ∆t ≤ ∆tFE = ∆x, and the Second Derivative condition unj +1 = unj + ∆ ∆xt 2 unj+1 − 2unj + unj−1 is TVD for ∆t ≤ √12∆tFE.

Fo initial conditions, we use a step function

u0(x) =

1 if 14 ≤ x ≤ 12, 0 otherwise,

(24)

with a domain x ∈ [0, 1] and periodic boundary conditions. This simple example is chosen as our experience has shown [7] that this problem often demonstrates the sharpness of the SSP time-step.

|Stages<br><br>|Order<br><br>|Predicted C|Observed C| |Stages|Order<br><br>|Predicted C<br><br>|Observed C|
|---|---|---|---|---|---|---|---|---|
|1<br><br>2 2<br><br><br>|2<br><br>2<br>3<br>|0.6180 1.2807 1.0400<br><br>|0.6180 1.2807 1.0400| |2<br><br>3 3<br><br><br>|4<br><br>4<br><br>5<br><br><br>|0.6788 1.3927 0.6746|0.7320 1.3927 0.7136<br><br>|


###### Table 3: Comparison of the theoretical and observed SSP coeﬃcients that preserve the nonlinear stability properties in Example 1.

For all of our simulations, we use a ﬁxed grid of size ∆x = 16001 , and a time-step ∆t = λ∆x where we vary time-stepping methods constructed earlier in this work, for K =

- 0.05 ≤ λ ≤ 1. We step each method forward by N = 50 time-steps and compare the performance of the various


√2

2 . We test this problem using the two stage third order method (19), the two stage fourth order method (10) and the three stage fourth order method in Appendix A, the ﬁfth order method (23). We also consider the non-SSP two stage third order method,

1 2

u∗ = un − ∆tF(un) +

∆t2F˙ (un), un+1 = un −

4 3

4 3

- 1

- 2


1 3

∆tF(u∗) +

∆t2F˙ (u∗), (25)

∆t2F˙ (un) +

∆tF(un) +

To measure the eﬀectiveness of these methods, we consider the maximum observed rise in total variation, deﬁned by

un+1 TV − un TV . (26)

max

0≤n≤N−1

We are interested in the time-step in which this rise becomes evident (i.e. well above roundoﬀ error). Another measure that we use is the rise in total variation compared to the total variation of the initial solution:

un+1 TV − u0 TV . (27)

max

0≤n≤N−1

Figure 6 (top) shows the maximal rise in total variation for each CFL value ∆∆xt . On the left we have the maximal per-step rise in TV (26) and on the right, the maximal rise in TV compared to the TV of the initial solution (27). We clearly see that once the CFL value passes a certain limit, there is a sharp jump in the total variation of the solution. We are interested in the value of ∆∆xt at which the time-stepping method no longer maintains the nonlinear stability. The ﬁfth order method (black) has the most restrictive value of ∆t before the total variation begins to rise. The next most restrictive is the two-stage fourth order method, followed by the two stage third order method. The two-stage second order methods have more freedom than these methods, and so have a much larger allowable ∆t, while the three stage fourth order, having the most freedom in the choice of coeﬃcients, outperforms all the other methods. Figure 6 (bottom) compares the performance of the non-SSP method to the SSP method. This graph clearly shows the need for the SSP property of the time-stepping, as the absence of this property results in the loss of the TVD property for any time-step.

We notice that controlling the maximal rise of the total variation compared to the initial condition (27) requires a smaller allowable time-step, so we use this condition as our criterion for maximal allowable time-step. A comparison of the predicted (i.e. theoretical) values of the SSP coeﬃcient and the observed value for the Taylor series method, the two stage methods of order p = 2, 3, 4, and the three-stage fourth and ﬁfth order methods are shown in Table 3 We note that for the Taylor series method, the two-stage second order method, the two stage third order method, and three stage fourth order method, the observed SSP coeﬃcient matches exactly the theoretical value. On the other hand, the two-stage fourth order and the three-stage ﬁfth order, both of which have the smallest SSP coeﬃcients (both in theory and practice), have a larger observed SSP coeﬃcient than predicted. For the two-stage fourth order case this is expected, as we noted in Section 2.1 that the TVD time-step for this particular case is (as we observe here) (√3 − 1), larger than the more general SSP timestep C = 0.6788.

n0log10(max(||U||−||U||))TVTV

2

- 2s3p

- 2s4p


0

- 3s4p

- 3s5p


−2

−4

−6

−8

−10

−12

−14

−16

0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6

∆t ∆x

))n0log10(max(||U||−||U||TVTV

))n+1nlog10(max(||U||−||U||TVTV

2

2

2s3p SSP

2s3p SSP

2s3p Non SSP

2s3p Non SSP

0

0

−2

−2

−4

−4

−6

−6

−8

−8

−10

−10

−12

−12

−14

−14

−16

−16

0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6

0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6

∆t ∆x

∆t ∆x

- Figure 6: The rise in total variation as a function of the CFL number. On the left is the maximal per time-step rise (26) and on the right the maximal TV rise above the initial TV (27). Top: Comparison of a variety of SSP methods. Bottom: Comparison of two-stage third order SSP and non-SSP methods.


##### 4.1.2 Example 2: MSMD methods with weighted essentially non-oscillatory (WENO) methods

The major use of MSMD time-stepping would be in conjunction with high order methods for problems with shocks. In this section we consider two scalar problems: the linear advection equation

Ut + Ux = 0 (28) and the nonlinear Burgers’ equation

- 1

- 2


U2

= 0 (29)

Ut +

x

on x ∈ (−1, 1). In both cases we use the step function initial conditions (24), and periodic boundaries. We use N = 201 points in the domain, so that ∆x = 1001 .

n0log10(max))(||U||−||U||TVTV

n0log10(max(||U||−||U||))TVTV

- 2s3p

- 2s4p


2

- 2s3p

- 2s4p


0

- 3s4p

- 3s5p


0

- 3s4p

- 3s5p


−2

−2

−4

−4

−6

−6

−8

−10

−8

−12

−10

−14

−12

−16

0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6

0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6

∆t ∆x

∆t ∆x

n0log10(max(||U||−||U||))TVTV

n0log10(max(||U||−||U||))TVTV

2

2

2s3p SSP

2s3p SSP

2s3p Non SSP

2s3p Non SSP

0

0

−2

−2

−4

−4

−6

−6

−8

−8

−10

−10

−12

−14

−12

−16

0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6

−14

∆t ∆x

0 0.2 0.4 0.6 0.8 1 1.2

∆t ∆x

###### Figure 7: Comparison of the rise in total variation as a function of the CFL number for Example 2. Linear advection on left and Burgers’ equation on right. The top graphs compare the performance of diﬀerent SSP methods, while the bottom graphs compare the two-stage third order SSP and non-SSP methods.

We follow our previous work [29] with a minor modiﬁcation for the spatial discretization. The spatial discretization is performed as follows: at each iteration we take the known value un and compute the ﬂux f(un) = un in the linear case and f(un) = 12 (un)2 for Burgers’ equation. Now to compute the spatial derivative f(un)x we use the WENO method [13]. In our test cases, we can avoid ﬂux splitting, as f (u) is strictly non-negative (below, we refer to the WENO method on a ﬂux with f (u) ≥ 0 as WENO+ and to to the corresponding method on a ﬂux with f (u) ≤ 0 as WENO−).

Now we have the approximation to Ut at time tn, and wish to compute the approximation to Utt. In previous work we deﬁned the higher order derivative using central diﬀerences, but we have found that additional limiting, in the form of the WENO− diﬀerentiation operator, is needed to achieve a pseudo-TVD like property. For the linear ﬂux, this is very straightforward as Utt = Uxx. To compute this, we take ux as computed before, and diﬀerentiate it using the WENO− method. Now we can compute the building block method.

For Burgers’ equation, we have Utt = − (UUt)x. We take the approximation to Ut that we obtained above

using WENO+, we multiply it by un and diﬀerentiate in space using WENO−. The choice of WENO+ followed by WENO− is made by analogy to the ﬁrst order ﬁnite diﬀerence for the linear advection case, where we use a diﬀerentiation operator D+ followed by the downwind diﬀerentiation operator D− to produce a centered diﬀerence for the second derivative. The second derivative condition (12) was satisﬁed by this approach. Now we compute the building block method with the approximations to Ut and Utt. In pseudocode, the building block calculation takes the form:

- 1

- 2


f(un) =

(un)2; unt = WENO+(f(un)); f (un) = un; f(un)t = f (un)unt untt = WENO−(f(un)t) un+1 = un + α∆tunt + β∆t2untt.

We use the two stage third order SSP method (19), and the non-SSP method (25) the two stage fourth order method (10) and the three stage fourth order method in Appendix A, the ﬁfth order method (23). In these simulations, we use ∆t = λ∆x where 0.05 ≤ λ ≤ 1.6, and step up to Tfinal = 1.0. At each time-step we compute (27), the maximal rise in total variation compared to the total variation of the initial solution. In Figure 7 we observe similar behavior to those of the linear advection with ﬁrst order time-stepping, and once again see that the SSP method is needed to preserve the nonlinear stability of WENO as well.

#### 4.2 Convergence studies

As a ﬁnal test case, we investigate the accuracy of the proposed schemes in conjunction with various high order spatial discretization operators. We perform several tests that demonstrate that these methods converge with the correct order for linear and nonlinear problems. In the ﬁrst study (Example 3), we reﬁne the grid only in time, and show that if the spatial discretization is suﬃciently accurate the multi-derivative methods exhibit the design-order of convergence. We also compare the performance of the third order multi-derivative method to the three stage third order explicit SSP Runge–Kutta method (SSPRK3,3) [32] and show that the convergence properties are the same, indicating that the additional error in approximating Ft does not aﬀect the accuracy of the method. In the second study (Example 4) we co-reﬁne the spatial and temporal grid by setting ∆t = λ∆x for a ﬁxed λ, and shrink ∆x. We observed that since the order of the spatial method is higher than the order of the temporal discretization, the time-stepping method achieves the design-order of accuracy both for linear and nonlinear problems.

- Example 3a: temporal grid reﬁnement with pseudospectral approximation of the spatial derivative. We begin with a linear advection problem Ut + Ux = 0 with periodic boundary conditions and initial conditions u0(x) = 0.5 + 0.5 sin(x) on the spatial domain x ∈ [0, 2π]. We discretize the spatial grid with N = 41 equidistant points and use the Fourier pseudospectral diﬀerentiation matrix D [10] to compute F ≈ −Ux ≈ −Du. We use a Lax-Wendroﬀ approach to approximate Ft ≈ Uxx ≈ D2u. In this case, the solution is a sine wave, so that the pseudospectral method is exact. For this reason, the spatial discretization of F is exact and contributes no errors, and the second derivative Ft is also exact Ft = utt = −Dut = −DF = D2u = F˙ . We use a range of time steps, ∆t = λ∆x where we pick λ = 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, and 0.05 to compute the solution to ﬁnal time

Tf = 2.0. In Table 4 we list the errors for the SSPRK3,3, the two derivative two stage third order method in Section 3.2

with K = √12 (listed as 2s3p in the table), the unique the two derivative two stage fourth order method (2s4p), and the the two derivative three stage ﬁfth order method (22) (3s5p). We observe that the design-order of each

method is veriﬁed. It is interesting to note that the SSPRK3,3 method has larger errors than the multiderivative method 2s3p, demonstrating that the additional computation of F˙ does improve the quality of the solution.

- Example 3b: temporal grid reﬁnement with WENO approximations of the spatial derivative. Using the same problem as above we discretize the spatial grid with N = 101 equidistant points and use the ninth order weighted essentially non-oscillatory method (WENO9) [1] to diﬀerentiate the spatial derivatives. It is interesting to note that although the PDE we solve is linear, the use of the nonlinear method WENO9 results in a non-linear


| | |SSPRK 3,3| | |2s3p| | |2s4p| | |3s5p| |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|λ| |error<br><br>|Order| |error<br><br>|Order| |error<br><br>|Order| |error|Order|
|0.8 0.7 0.6 0.5 0.4 0.3 0.2 0.1<br><br>0.05| |7.99 × 10−5 5.24 × 10−5<br><br>3.27 × 10−5 1.93 × 10−5 9.70 × 10−6<br><br>4.09 × 10−6 1.21 × 10−6 1.50 × 10−7 1.88 × 10−8<br><br><br>|3.16 3.04 2.87 3.10 3.00 2.99 3.01 2.99| |1.86 × 10−5<br><br>1.21 × 10−5 7.61 × 10−6 4.50 × 10−6<br><br>2.25 × 10−6 9.50 × 10−7<br><br><br>2.81 × 10−7<br><br>3.49 × 10−8<br><br>4.36 × 10−9<br><br><br>|3.17 3.05 2.88 3.10 3.00 3.00 3.01 3.00| |1.96 × 10−6<br><br>1.12 × 10−6<br><br>6.02 × 10−7<br><br>2.97 × 10−7<br><br>1.18 × 10−7<br><br>3.76 × 10−8 7.43 × 10−9 4.61 × 10−10<br><br>2.88 × 10−11<br><br><br><br><br><br><br>|4.17 4.04 3.87 4.10 3.99 4.01 4.00 3.97| |6.47 × 10−8<br><br>3.24 × 10−8 1.49 × 10−8<br><br>6.12 × 10−9 1.96 × 10−9<br><br>4.66 × 10−10<br><br>6.13 × 10−11 1.90 × 10−12<br><br><br>5.97 × 10−14<br><br><br>|5.17 5.04 4.87 5.09 5.00 5.00 5.01 4.99|


- Table 4: Convergence study for Example 3a, the linear advection problem with pseudospectral diﬀerentiation of the spatial derivatives. Here we use N = 41 equidistant points between (0,2π), and ∆t = λ∆x. The


solution is evolved forward to time Tf = 2.0 using the explicit SSP Runge–Kutta method (SSPRK3,3), the two-stage third order two derivative method (2s3p), the two-stage fourth order two derivative method (2s4p), and three-stage ﬁfth order two derivative method (3s5p).

ODE. To evolve this ODE in time we use a range of time steps deﬁned by ∆t = λ∆x for λ = 0.9, 0.8, 0.7, 0.6, 0.5, 0.4 to compute the solution to ﬁnal time Tf = 2.0 In Table 5 we list the errors for the SSPRK3,3, the two derivative two stage third order method in Section 3.2 with K = √12 (listed as 2s3p in the table), the unique the two derivative two stage fourth order method (2s4p), and the the two derivative three stage ﬁfth order method (22) (3s5p). We observe that the design-order of each method is veriﬁed and that once again the SSPRK3,3 method has larger errors than the multiderivative method 2s3p. These results indicate that the approximation of the second derivative term Ft via a Lax-Wendroﬀ procedure and discretization in space does not aﬀect the observed order of the time-stepping method, as long as the spatial errors do not dominate.

To see what happens if the spatial discretization errors dominate over the time errors, we compare two diﬀerent WENO spatial discretizations: the ﬁfth order method WENO5 and the ninth order method WENO9. Here, we use N = 301 points in space, and we choose ∆t = λ∆x for λ = 0.8, 0.6, 0.4, 0.2, 0.1, 0.05. We evolve the solution in time to Tf = 2.0 using the 2s3p and SSPRK3,3 methods. The log-log graph of the errors vs. ∆t is given in Figure

- 8 We observe that the errors from both time discretizations with the WENO5 spatial discretization (dotted lines) have the correct orders when ∆t is larger and the time errors dominate, but as ∆t gets smaller the spatial errors dominate convergence is lost. On the other hand, for the range of ∆t studied, the time-errors dominate over the spatial errors when using the highly accurate WENO9 (solid line) and so convergence is not lost. We note that to see this behavior, the spatial approximation must be suﬃciently accurate. In this case this is attained by using 301 points in space and a high order spatial discretization. We also studied this problem with a co-reﬁnement of


the spatial and temporal grids, where we use ∆t = 0.8∆x for ∆x = N2−π1 and N = 41, 81, 161, 321. Figure 9 shows that while for larger ∆t the errors for WENO5 are larger than for WENO9, and this is more pronounced for the

multi-derivative methods than for the explicit Runge–Kutta, once the grid is suﬃciently reﬁned the temporal error dominates and we see the third order convergence in time.

It is interesting to note that in all these studies the explicit SSP Runge–Kutta method SSPRK3,3 and the two-derivative method 2s3p behave similarly, indicating that the approximation of the second derivative does not play a role in the loss of accuracy. Example 4: co-reﬁnement of the spatial and temporal grids on linear advection with WENO7

- Example 4a: In this example, we compare the errors and order of convergence of the multiderivative methods on


−6.5

WENO5 2s3p WENO9 2s3p

−7

WENO5 SSP RK 33 WENO9 SSP RK 33

−7.5

−8

−8.5

−9

−9.5

−10

−10.5

−11

−3 −2.8 −2.6 −2.4 −2.2 −2 −1.8 −1.6

Figure 8: WENO5 vs WENO9 with grid reﬁnement in time but not space Example 3b. On the x-axis are log10(∆t) and on the y-axis are log10(error). The errors from both time discretizations with the WENO5 spatial discretization (dotted lines) have the correct orders when ∆t is larger and the time errors dominate, but as ∆t gets smaller the spatial errors dominate convergence is lost.

−4

WENO5 2s3p WENO9 2s3p

−4.5

WENO5 SSP RK 33 WENO9 SSP RK 33

−5

−5.5

−6

−6.5

−7

−7.5

−1.8 −1.7 −1.6 −1.5 −1.4 −1.3 −1.2 −1.1 −1 −0.9

Figure 9: Example 3b: WENO5 vs WENO9 with reﬁnement in both space and time, ∆t = 0.8∆x . On the x-axis are log10(∆t) and on the y-axis are log10(error). Here we see that for larger ∆t the errors for WENO5 are larger than for WENO9 (especially for the multiderivative method) but once the grid is suﬃciently reﬁned the temporal order dominates and third order convergence in time is observed.

- a linear and nonlinear problem. For the linear problem, we use the linear advection problem Ut + Ux = 0 on x ∈ [−1, 1]


with the initial condition

u0(x) = 0.5 + 0.5 sin(πx), x ∈ [−1, 1], (30) We compute both F and F˙ using a seventh order WENO (WENO7) [1] spatial derivative. We set ∆t = 0.8∆x and evolve the solution to ﬁnal time of Tfinal = 2.0, at which point the exact solution is identical to the initial state. For time-stepping, we use the same three multiderivative schemes 2s3p, 2s4p, and 3s5p and the explicit SSP Runge–Kutta method SSPRK3,3. In Table 6, where we compare the errors and orders of these three methods. These numerical experiments show that once the mesh is suﬃciently reﬁned, the design-order of accuracy is reached. The results verify that the proposed schemes are genuinely high-order accurate despite the fact that the second derivative is not an exact second derivative of the method of lines formulation.

- Example 4b: Next, we present results for the more diﬃcult non-linear Burgers equation, with initial conditions prescribed by


U0(x) = 1.0 + 0.2 sin(πx), x ∈ [−1, 1], (31) and periodic boundary conditions. Once again, F and F˙ are computed via the WENO7 spatial discretization. We use a constant time-step ∆t = 0.8max ∆x

i |u0(xi)| and run this problem with a ﬁnal time of Tfinal = 1.4, before a shock forms. Since the solution at this point the solution remains smooth, we can use the method of characteristics to compute the the exact solution by

U(t, x) = U0 (x − t · U0(ξ)) , ξ = x − t · U0(ξ). (32)

| | |SSPRK 3,3| | |2s3p| | |2s4p| | |3s5p| |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|λ| |error|Order| |error|Order| |error<br><br>|Order| |error|Order|
|0.9 0.8 0.7 0.6 0.5 0.4| |7.37 × 10−6<br><br>5.24 × 10−6 3.44 × 10−6 2.18 × 10−6 1.27 × 10−6<br><br>6.47 × 10−7<br><br><br>|2.89 3.14 2.96 2.98 3.01| |1.71 × 10−6<br><br>1.22 × 10−6 7.99 × 10−7 5.08 × 10−7<br>2.94 × 10−7 1.50 × 10−7<br>|2.89 3.14 2.96 2.98 3.01<br><br>| |8.25 × 10−8 5.21 × 10−8 3.00 × 10−8 1.63 × 10−8 7.89 × 10−9 3.22 × 10−9<br><br>|3.89 4.14 3.96 3.98 4.01| |1.24 × 10−9 6.99 × 10−10 3.52 × 10−10<br><br>1.64 × 10−10 6.61 × 10−11<br><br>2.18 × 10−11<br><br><br>|4.89 5.14 4.96 4.97 4.97|


- Table 5: Convergence study for Example 3b, the linear advection problem with WENO9 diﬀerentiation of the spatial derivatives. Here we use N = 101 equidistant points between (0,2π), and ∆t = λ∆x.

| | |SSPRK 3,3| | |2s3p| | |2s4p| | |3s5p| |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|N| |error<br><br>|order| |error<br><br>|order| |error|order| |error<br><br>|order|
|41 81<br><br>161 321 641<br><br>1281| |3.00 × 10−04<br><br>3.75 × 10−05<br><br>4.69 × 10−06<br><br>5.86 × 10−07 7.32 × 10−08 9.15 × 10−09<br><br><br>|3.00 3.00 3.00 3.00 3.00| |5.94 × 10−05 7.39 × 10−06 9.23 × 10−07 1.15 × 10−07 1.44 × 10−08 1.80 × 10−09|3.01 3.00 3.00 3.00 3.00<br><br>| |7.54 × 10−06 4.71 × 10−07 2.94 × 10−08 1.84 × 10−09 1.15 × 10−10 7.19 × 10−12<br><br>|− − − 4.00 4.00 4.00 4.00 4.00| |2.59 × 10−06 8.03 × 10−08 2.51 × 10−09 7.82 × 10−11 2.45 × 10−12 7.75 × 10−14<br><br>|5.01 5.00 5.00 5.00 4.98|


- Table 6: Convergence study for Example 4a: linear advection with WENO7 spatial diﬀerentiation and reﬁnement of both spatial and temporal grids. Here we use N points in space and ∆t = 0.8∆x. The

four methods used to evolve the solution to time Tf = 2.0 are the explicit SSP Runge–Kutta method SSPRK3,3 and the three multiderivative methods 2s3p, 2s4p, and 3s5p. Despite the fact that the second derivative F˙ is not the exact second derivative Ft, we still observe high-order accuracy for all methods once the grids are suﬃciently reﬁned.

| | |SSPRK 3,3| | |2s3p| | |2s4p| | |3s5p| |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|N| |error<br><br>|order| |error|order| |error|order| |error|order|
|161 321 641<br><br>1281 2561 5121<br><br>10241| |3.09 × 10−04<br><br>5.11 × 10−05<br>6.96 × 10−06 8.80 × 10−07 1.10 × 10−07 1.38 × 10−08 1.72 × 10−09<br>|2.60 2.88 2.98 3.00 3.00 3.00<br><br>| |1.91 × 10−04<br><br>2.00 × 10−05<br><br><br>1.70 × 10−06<br><br>1.81 × 10−07<br><br>2.22 × 10−08<br><br><br>2.76 × 10−09<br><br>3.44 × 10−10<br><br><br>|3.25 3.56 3.23 3.03 3.01 3.00| |1.58 × 10−04 1.33 × 10−05 7.12 × 10−07 3.38 × 10−08 1.99 × 10−09 1.24 × 10−10 7.75 × 10−12<br><br>|3.57 4.22 4.39 4.09 4.01 4.00| |1.67 × 10−04<br><br>1.76 × 10−05 9.34 × 10−07<br>2.73 × 10−08 7.49 × 10−10<br><br><br>2.21 × 10−11 7.04 × 10−13<br>|3.25 4.23 5.09 5.19 5.08 4.97<br><br>|


- Table 7: Convergence study for Example 4b: Burgers’ equation with WENO7 spatial diﬀerentiation and reﬁnement of both spatial and temporal grids. Here we use N points in space and ∆t = 0.8∆x. The


four methods used to evolve the solution to time Tf = 2.0 are the explicit SSP Runge–Kutta method SSPRK3,3 and the three multiderivative methods 2s3p, 2s4p, and 3s5p. A more reﬁned grid is needed in this example compared to the linear example, but for a suﬃciently reﬁned grid we still observe high-order accuracy for all methods.

We solve for the implicit variable ξ using Netwon iteration with a tolerance of 10−14. The errors and order are presented in Table 7. We see that it takes an even smaller mesh size than the linear problem before the errors reach the asymptotic regime, but that once this happens we achieve the expected order. Again, these numerical experiments further validate the fact that if the spatial error is not allowed to dominate, the high-order designaccuracy of the time discretization attained despite the fact that we do not directly diﬀerentiate the method of lines formulation to deﬁne the second derivative.

### 5 Conclusions

With the increasing popularity of multi-stage multiderivative methods for use as time-stepping methods for hyperbolic problems, the question of their strong stability properties needs to be addressed. In this work we presented an SSP formulation for multistage two-derivative methods. We assumed that, in addition to the forward Euler condition, the spatial discretization of interest satisﬁes a second derivative condition of the form (12). With these assumptions in mind, we formulated an optimization problem which enabled us to ﬁnd optimal explicit SSP multistage two-derivative methods of up to order ﬁve, thus breaking the SSP order barrier for explicit SSP Runge–Kutta methods. Numerical test cases verify the convergence of these methods at the design-order, show that sharpness of the SSP condition in many cases, and demonstrate the need for SSP time-stepping methods in simulations where the spatial discretization is specially designed to satisfy certain nonlinear stability properties. Future work will involve building SSP multiderivative methods while assuming diﬀerent base conditions (as in Remark 1) and with higher derivatives. Additional work will involve developing new spatial discretizations suited for use with SSP multiderivative time stepping methods. These methods will be based on WENO or discontinuous Galerkin methods and will satisfy pseudo-TVD and similar properties for systems of equations.

Acknowledgements This work was supported by: AFOSR grants FA9550-12-1-0224, FA9550-12-1-0343, FA9550-12-1-0455, FA9550-15-1-0282, and FA9550-15-1-0235; NSF grant DMS-1418804; New Mexico Consortium grant NMC0155-01; and NASA grant NMX15AP39G.

### A Coeﬃcients of three stage fourth order methods

- 1. For K = 12 we obtain an SSP coeﬃcient C = r = 1.1464. The Butcher array coeﬃcients are given by


 

  , b =

 

 

0 0 0 0.436148675945340 0 0 0.546571371212865 0.156647174804152 0

0.528992280543542 0.105732787708912 0.365274931747546

A =

 

  , ˆb =

 

  .

0 0 0 0.095112833764436 0 0 0.071032477596813 0.107904226252921 0

0.074866026156687 0.073410341982927 0.048740310097159

Aˆ =

The Shu-Osher arrays are Re = (1, 0, 0, 0)T,

- P =

  

0 0 0 0 0.5000 0 0 0 0.253176729307242 0.179580018745470 0 0 0.181986129712082 0.000000001889650 0.418750476492704 0

  

- Q =


  

  

0 0 0 0 0.5 0 0 0 0 0.567243251947287 0 0 0.140002406985210 0.003037359947341 0.256223624973014 0

- 2. For K = 12 we obtain an SSP coeﬃcient C = r = 1.3927 Butcher formulation

A =

 

0 0 0 0.443752012194422 0 0 0.543193299768317 0.149202742858795 0

  , b =

 

0.515040964378407 0.178821699719783 0.306137335901811

 

Aˆ =

 

0 0 0 0.098457924163299 0 0 0.062758211639901 0.110738910914425 0

  , ˆb =

 

0.072864982225864 0.073840478463180 0.061973770357455

  .

The Shu-Osher arrays are Re = (1, 0, 0, 0)T,

- P =

  

0 0 0 0 0.618033988749895 0 0 0 0.362588515112176 0.207801573327953 0 0 0.144580879241747 0.110491604448675 0.426371652664792 0

  

- Q =


  

0 0 0 0 0.381966011250105 0 0 0 0 0.429609911559871 0 0 0.078129569197367 0 0.240426294447419 0

   .

- 3. For K = 1 we obtain an SSP coeﬃcient C = r = 1.6185. The Butcher array coeﬃcients are given by


 

  , b =

 

 

0 0 0 0.452297224196082 0 0 0.528050722182308 0.159236998008155 0

0.502519798444212 0.210741084344740 0.286739117211047

A =

 

  , ˆb =

 

  .

0 0 0 0.102286389507741 0 0 0.055482128781494 0.108677624192402 0

0.071256397204544 0.069475972085130 0.066877749079721

Aˆ =

The Shu-Osher arrays are Re = (1, 0, 0, 0)T,

- P =

  

0 0 0 0 0.732050807568877 0 0 0 0.457580533944888 0.257727809835459 0 0 0.137886171629970 0.176326540063367 0.464092174540814 0

   ,

- Q =


  

   .

0 0 0 0 0.267949192431123 0 0 0 0 0.284691656219654 0 0 0.046502314960818 0 0.175192798805030 0

### B Two stage third order method

This code gives the SSP coeﬃcient and the Butcher and Shu Osher arrays for the optimal explicit SSP two stage third order method given the value K.

clear all k=sqrt(0.5); % Choose K tab=[]; % Set up the polynomial for Q(3,1) to solve for SSP coefficient r AA=sqrt(k^2+2) - k;

- p0=2*k*(AA-2*k) + 4*k^3*AA;
- p1=-p0;
- p2=(1-p0)/(2*k^2);
- p3= -(p0/(2*k) + k)/(6*k^3); CC=[p3,p2,p1,p0]; % polynomial coefficients RC=roots(CC); r=RC(find(abs(imag(RC))<10^-15)); % SSP coefficient is the only real root. %-------------------------------------------------------------------------% Once we have the k and r we want we define the method following (21) a= (k*sqrt(k^2+2)-k^2)/r;


- b2 = ((k^2*(1-1/r)) + r*(.5-1/(6*a)))/(k^2+.5*r*a); b1=1-b2; ahat=.5*a^2;


- bhat1=.5*(1-b2*a)-1/(6*a);
- bhat2=1/(6*a)-.5*b2*a; % The Butcher arrays are given by A=zeros(2,2); Ahat=A; A(2,1)=a; b=[b1,b2]; Ahat(2,1)=ahat; bhat=[bhat1,bhat2]; S=[0 0 0 ; a 0 0; b1 b2 0]; Shat=[0 0 0 ; ahat 0 0 ; bhat1 bhat2 0]; % The Shu-Osher matrices are given by I=eye(3);e=ones(3,1); Ri=I+r*S+(r^2/k^2)*Shat; v=Ri\e;


- P = r*(Ri\S);
- Q= r^2/k^2*(Ri\Shat); violation=min(min([v, S, Shat, P, Q])) % use this to check that all these are positive tab=[tab;[k,r,violation]]; % build the table of values


### C Three stage ﬁfth order method

This code gives the SSP coeﬃcient and the Butcher and Shu Osher arrays for the optimal explicit SSP three stage ﬁfth order method given the value K.

clear all format long syms r tab=[]; k=sqrt(0.5) %The second derivative condition coefficient K

% Find the SSP coefficient C given K a21= 240*k^6*(1 -r - r^2/(2*k^2) + r^3/(6*k^2) + r^4/(24*k^4) - r^5/(120*k^4))/r^6; Q31=10*r^2*a21^4 - 100*k^2*a21^3 - 10*r^2*a21^3 + 130*k^2*a21^2 + 3*r^2*a21^2 - 50*k^2*a21 +6*k^2; RC=vpasolve(simplify(r^22*Q31)==0); rr=RC(find(abs(imag(RC))<10^-15)); C= max(rr) %The SSP coefficient % ------------------------------------------------------------------------% The Butcher array coefficients given K and C a21= 240*k^6*(1 -C - C^2/(2*k^2) + C^3/(6*k^2) + C^4/(24*k^4) - C^5/(120*k^4))/C^6; ah32= ( (3/5 -a21)^2/(a21*(1-2*a21)^3) - (3/5 -a21)/(1-2*a21)^2 )/10; ah31= ( (3/5 -a21)^2/(1-2*a21)^2)/2 -ah32; a31= (3/5 -a21)/(1-2*a21);

- bh2=(2*a31-1)/(12*a21*(a31-a21));
- bh3=(1-2*a21)/(12*a31*(a31-a21)); bh1=1/2-bh2-bh3; ah21=(1/24 - bh3*(ah31+ah32) )/bh2; % Build the Butcher matrices


- a= C*a21+ah21*C^2/k^2;
- b= C*a31+ah31*C^2/k^2;
- c= ah32*C^2/k^2;
- d= C+ bh1*C^2/k^2;
- e= bh2*C^2/k^2;
- f = bh3*C^2/k^2; Ri=([1 0 0 0; a 1 0 0 ; b c 1 0; d e f 1]); S=[0 0 0 0; a21 0 0 0; a31 0 0 0 ;1 0 0 0]; Shat=[0 0 0 0; ah21 0 0 0; ah31 ah32 0 0 ;bh1 bh2 bh3 0]; % The Shu Osher matrices given C eone=ones(4,1) v=Ri\eone;


- P = C*(Ri\S);
- Q= C^2/k^2*(Ri\Shat); % Double check that there are no violations of the SSP conditions: violation=min(min([v, S, Shat, P, Q])) % use this to check that all these are positive tab=[tab;[k,a21,C,violation]]; % build the table of values


### References

- [1] D. S. Balsara and C.-W. Shu, Monotonicity preserving weighted essentially non-oscillatory schemes with increasingly high order of accuracy, Journal of Computational Physics, 160 (2000), pp. 405–452.
- [2] C. Bresten, S. Gottlieb, Z. Grant, D. Higgs, D. I. Ketcheson, and A. Németh, Strong stability preserving multistep Runge-Kutta methods. Accepted for publication in Mathematics of Computation.
- [3] R. P. K. Chan and A. Y. J. Tsai, On explicit two-derivative Runge-Kutta methods, Numerical Algorithms, 53 (2010), pp. 171–194.
- [4] L. Ferracina and M. N. Spijker, Stepsize restrictions for the total-variation-diminishing property in general Runge–Kutta methods, SIAM Journal of Numerical Analysis, 42 (2004), pp. 1073–1093.


- [5] , An extension and analysis of the Shu–Osher representation of Runge–Kutta methods, Mathematics of Computation, 249 (2005), pp. 201–219.

- [6] E. Gekeler and R. Widmann, On the order conditions of Runge-Kutta methods with higher derivatives, Numer. Math., 50 (1986), pp. 183–203.
- [7] S. Gottlieb, D. I. Ketcheson, and C.-W. Shu, Strong Stability Preserving Runge–Kutta and Multistep Time Discretizations, World Scientiﬁc Press, 2011.
- [8] Z. J. Grant, Explicit SSP multistage two-derivative SSP optimization code. https://github.com/ SSPmethods/SSPMultiStageTwoDerivativeMethods, February 2015.
- [9] A. Harten, B. Engquist, S. Osher, and S. R. Chakravarthy, Uniformly high-order accurate essentially nonoscillatory schemes. III, J. Comput. Phys., 71 (1987), pp. 231–303.
- [10] J. Hesthaven, S. Gottlieb, and D. Gottlieb, Spectral methods for time dependent problems, Cambridge Monographs of Applied and Computational Mathematics, Cambridge University Press, 2007.
- [11] I. Higueras, On strong stability preserving time discretization methods, Journal of Scientiﬁc Computing, 21

(2004), pp. 193–223.

- [12] , Representations of Runge–Kutta methods and strong stability preserving methods, SIAM Journal On Numerical Analysis, 43 (2005), pp. 924–948.

- [13] G.-S. Jiang and C.-W. Shu, Eﬃcient implementation of weighted ENO schemes, J. Comput. Phys., 126

(1996), pp. 202–228.

- [14] K. Kastlunger and G. Wanner, On Turan type implicit Runge-Kutta methods, Computing (Arch. Elektron. Rechnen), 9 (1972), pp. 317–325. 10.1007/BF02241605.
- [15] K. H. Kastlunger and G. Wanner, Runge Kutta processes with multiple nodes, Computing (Arch. Elektron. Rechnen), 9 (1972), pp. 9–24.
- [16] D. I. Ketcheson, Highly eﬃcient strong stability preserving Runge–Kutta methods with low-storage implementations, SIAM Journal on Scientiﬁc Computing, 30 (2008), pp. 2113–2136.
- [17] D. I. Ketcheson, S. Gottlieb, and C. B. Macdonald, Strong stability preserving two-step Runge-Kutta methods, SIAM Journal on Numerical Analysis, (2012), pp. 2618–2639.
- [18] D. I. Ketcheson, C. B. Macdonald, and S. Gottlieb, Optimal implicit strong stability preserving Runge–Kutta methods, Applied Numerical Mathematics, 52 (2009), p. 373.
- [19] D. I. Ketcheson, M. Parsani, and A. J. Ahmadia, Rk-opt: Software for the design of Runge–Kutta meththods, version 0.2. https://github.com/ketch/RK-opt.
- [20] J. F. B. M. Kraaijevanger, Contractivity of Runge–Kutta methods, BIT, 31 (1991), pp. 482–528.
- [21] P. Lax and B. Wendroff, Systems of conservation laws, Communications in Pure and Applied Mathematics, 13 (1960), pp. 217–237.
- [22] T. Mitsui, Runge-Kutta type integration formulas including the evaluation of the second derivative. i., Publ. Res. Inst. Math. Sci., 18 (1982), pp. 325–364.
- [23] T. Nguyen-Ba, H. Nguyen-Thu, T. Giordano, and R. Vaillancourt, One-step strong-stabilitypreserving Hermite-Birkhoﬀ-Taylor methods, Scientiﬁc Journal of Riga Technical University, 45 (2010), pp. 95– 104.
- [24] N. Obreschkoff, Neue Quadraturformeln, Abh. Preuss. Akad. Wiss. Math.-Nat. Kl., 4 (1940).
- [25] H. Ono and T. Yoshida, Two-stage explicit Runge-Kutta type methods using derivatives., Japan J. Indust. Appl. Math., 21 (2004), pp. 361–374.


- [26] J. Qiu, M. Dumbser, and C.-W. Shu, The discontinuous Galerkin method with Lax–Wendroﬀ type time discretizations, Computer Methods in Applied Mechanics and Engineering, 194 (2005), pp. 4528–4543.
- [27] J. Qiu and C.-W. Shu, Finite Diﬀerence WENO schemes with Lax–Wendroﬀ-type time discretizations, SIAM Journal on Scientiﬁc Computing, 24 (2003), pp. 2185–2198.
- [28] S. J. Ruuth and R. J. Spiteri, Two barriers on strong-stability-preserving time discretization methods, Journal of Scientiﬁc Computation, 17 (2002), pp. 211–220.
- [29] D. C. Seal, Y. Guclu, and A. J. Christlieb, High-order multiderivative time integrators for hyperbolic conservation laws, Journal of Scientiﬁc Computing, 60 (2014), pp. 101–140.
- [30] H. Shintani, On one-step methods utilizing the second derivative, Hiroshima Mathematical Journal, 1 (1971), pp. 349–372.
- [31] , On explicit one-step methods utilizing the second derivative, Hiroshima Mathematical Journali, 2 (1972), pp. 353–368.

- [32] C.-W. Shu, Total-variation diminishing time discretizations, SIAM J. Sci. Stat. Comp., 9 (1988), pp. 1073– 1084.
- [33] C.-W. Shu and S. Osher, Eﬃcient implementation of essentially non-oscillatory shock-capturing schemes, Journal of Computational Physics, 77 (1988), pp. 439–471.
- [34] R. J. Spiteri and S. J. Ruuth, A new class of optimal high-order strong-stability-preserving time discretization methods, SIAM J. Numer. Anal., 40 (2002), pp. 469–491.
- [35] D. D. Stancu and A. H. Stroud, Quadrature formulas with simple Gaussian nodes and multiple ﬁxed nodes, Math. Comp., 17 (1963), pp. 384–394.
- [36] E. Toro and V. Titarev, Solution of the generalized Riemann problem for advection–reaction equations, Proceedings of the Royal Society of London A: Mathematical, Physical and Engineering Sciences, 458 (2002), pp. 271–281.
- [37] A. Y. J. Tsai, R. P. K. Chan, and S. Wang, Two-derivative Runge–Kutta methods for PDEs using a novel discretization approach, Numerical Algorithms, 65 (2014), pp. 687–703.
- [38] P. Turán, On the theory of the mechanical quadrature, Acta Sci. Math. Szeged, 12 (1950), pp. 30–37.


