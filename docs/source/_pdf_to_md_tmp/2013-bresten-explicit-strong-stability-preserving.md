arXiv:1307.8058v2[math.NA]29Jan2014

# Explicit Strong Stability Preserving Multistep Runge–Kutta Methods

Christopher Bresten∗, Sigal Gottlieb∗, Zachary Grant∗, Daniel Higgs∗, David I. Ketcheson†, and Adrian Németh‡

January 30, 2014

Abstract

High-order spatial discretizations with strong stability properties (such as monotonicity) are desirable for the solution of hyperbolic PDEs. Methods may be compared in terms of the strong stability preserving (SSP) time-step. We prove an upper bound on the SSP coeﬃcient of explicit multistep Runge–Kutta methods of order two and above. Order conditions and monotonicity conditions for such methods are worked out in terms of the method coeﬃcients. Numerical optimization is used to ﬁnd optimized explicit methods of up to ﬁve steps, eight stages, and tenth order. These methods are tested on the advection and Buckley-Leverett equations, and the results for the observed total variation diminishing and positivity preserving time-step are presented.

## 1 Introduction

The numerical solution of hyperbolic conservation laws Ut + f(U)x = 0, is complicated by the fact that the exact solutions may develop discontinuities. For this reason, signiﬁcant eﬀort has been expended on ﬁnding spatial discretizations that can handle discontinuities [13]. Once the spatial derivative is discretized, we obtain the system of ODEs

ut = F(u), (1)

![image 1](<2013-bresten-explicit-strong-stability-preserving_images/imageFile1.png>)

∗Mathematics Department, University of Massachusetts Dartmouth. Supported by AFOSR grant number FA-

9550-12-1-0224 and KAUST grant FIC/2010/05 †King Abdullah University of Science & Technology (KAUST). ‡Department of Mathematics and Computational Sciences, Széchenyi István University, Győr, Hungary

where u is a vector of approximations to U, uj ≈ U(xj). This system of ODEs can then be evolved in time using standard methods. The spatial discretizations used to approximate f(U)x are carefully designed so that when (1) is evolved in time using the forward Euler method the solution at time un satisﬁes the strong stability property

un + ∆tF(un) ≤ un under the step size restriction 0 ≤ ∆t ≤ ∆tFE. (2)

Here and throughout, · represents a norm, semi-norm, or convex functional, determined by the design of the spatial discretization. For example, for total variation diminishing methods the relevant strong stability property is in the total variation semi-norm, while when using a positivity preserving limiter we are naturally interested in the positivity of the solution.

The spatial discretizations satisfy the desired property when coupled with the forward Euler time discretization, but in practice we want to use a higher-order time integrator rather than forward Euler, while still ensuring that the strong stability property

un+1 ≤ un (3) is satisﬁed.

In [33] it was observed that some Runge–Kutta methods can be decomposed into convex combinations of forward Euler steps, and so any convex functional property satisﬁed by forward Euler will be preserved by these higher-order time discretizations, generally under a diﬀerent time-step restriction. This approach was used to develop second and third order Runge–Kutta methods that preserve the strong stability properties of the spatial discretizations developed in that work. In fact, this approach also guarantees that the intermediate stages in a Runge–Kutta method satisfy the strong stability property as well.

For multistep methods, where the solution value un+1 at time tn+1 is computed from previous solution values un−k+1, . . ., un, we say that a k-step numerical method is strong stability preserving (SSP) if

un+1 ≤ max un , un−1 , . . ., un−k+1 . (4) for any time-step

0∆t ≤ C∆tFE, (5)

(for some C > 0), assuming only that the spatial discretization satisﬁes (2). An explicit multistep method of the form

un+1 =

k

i=1

αiun+1−i + ∆tβiF(un+1−i) (6)

has ki=1 αi = 1 for consistency, so if all the coeﬃcients are non-negative (αi, βi ≥ 0) the method can be written as convex combinations of forward Euler steps:

un+1 =

k

αi un+1−i +

i=1

βi αi

∆tF(un+1−i) .

![image 2](<2013-bresten-explicit-strong-stability-preserving_images/imageFile2.png>)

Clearly, if the forward Euler condition (2) holds then the solution obtained by the multistep method

(6) is strong stability preserving under the time-step restriction (5) with C = mini α

βi∆tFE, (where if any βi is equal to zero, the corresponding ratio is considered inﬁnite) [33].

i

![image 3](<2013-bresten-explicit-strong-stability-preserving_images/imageFile3.png>)

The convex combination approach has also been applied to obtain suﬃcient conditions for strong stability for implicit Runge–Kutta methods and implicit linear multistep methods. Furthermore, it has be shown that these conditions are not only suﬃcient, but necessary as well [8, 9, 16, 17]. Much research on SSP methods focuses on ﬁnding high-order time discretizations with the largest allowable time-step ∆t ≤ C∆tFE. Our aim is to maximize the SSP coeﬃcient C of the method, relative to the number of function evaluations at each time-step (typically the number of stages of a method). For this purpose we deﬁne the eﬀective SSP coeﬃcient Ceﬀ = Cs where s is the number of stages. This value allows us to compare the eﬃciency of explicit methods of a given order.

![image 4](<2013-bresten-explicit-strong-stability-preserving_images/imageFile4.png>)

Explicit Runge–Kutta methods with positive SSP coeﬃcients cannot be more than fourth-order accurate [23, 32], while explicit SSP linear multistep methods of high-order accuracy must use very many steps, and therefore impose large storage requirements [13, 25]. These characteristics have led to the design of explicit methods with multiple steps and multiple stages in the search for higher-order SSP methods with large eﬀective SSP coeﬃcients. In [14] Gottlieb et. al. considered a class of two-step, two-stage methods. Huang [18] considered two-stage hybrid methods with many steps, and found methods of up to seventh order (with seven steps) with reasonable SSP coeﬃcients. Constantinescu and Sandu [5] found multistep Runge–Kutta with up to four stages and four steps, with a focus on ﬁnding SSP methods with order up to four. Multistep Runge–Kutta SSP methods with order as high as twelve have been developed in [28] and numerous similar works by the same authors, using suﬃcient conditions for monotonicity and focusing on a single set of parameters in each work. Spijker [34] developed a complete theory for strong stability preserving multi-step multistage methods and found new second order and third order methods with optimal SSP coeﬃcients. In [22], Spijker’s theory (including necessary and suﬃcient conditions for monotonicity) is applied to two-step Runge–Kutta methods to develop two-step multi-stage explicit methods with optimized SSP coeﬃcients. In the present work we present a general application of the same theory to multistep Runge–Kutta methods with more steps. We determine necessary and suﬃcient conditions for strong stability preservation and prove sharp upper bounds on C for second order methods. We also ﬁnd and test optimized methods with up to ﬁve steps and up to tenth order. The approach we employ ensures that the intermediate stages of each method also satisfy a strong stability property.

In Section 2 we extend the order conditions and SSP conditions from two step Runge–Kutta methods [22] to MSRK methods with arbitrary numbers of steps and stages. In Section 3 we recall an upper bound on C for general linear methods of order one and prove a new, sharp upper bound on C for general linear methods of order two. These bounds are important to our study because the explicit MSRK methods we consider are a subset of the class of general linear methods. In Section 4 we formulate and numerically solve the problem of determining methods with the largest C for a given order and number of stages and steps. We present the eﬀective SSP coeﬃcients of optimized methods of up to ﬁve steps and tenth order, thus surpassing the order-eight barrier established in [22] for two-step methods. Most of the methods we ﬁnd have higher eﬀective SSP coeﬃcients than methods previously found, though in some cases we had trouble with the optimization subroutines for higher orders. Finally, in Section 5 we explore how well these methods perform in practice, on a series of well-established test problems. We highlight the need for higher-order methods and the behavior of these methods in terms of strong stability and positivity preservation.

## 2 SSP Multistep Runge–Kutta Methods

In this work we study methods in the class of multistep Runge-Kutta methods with optimal strong stability preservation properties. These multistep Runge–Kutta methods are a simple generalization of Runge–Kutta methods to include the numerical solution at previous steps. These methods are Runge–Kutta methods in the sense that they compute multiple stages based on the initial input; however, they use the previous k solution values un−k+1, un−k, ..., un−1, un to compute the solution value un+1.

A class of two-step Runge–Kutta methods was studied in [22]. Here we study the generalization of that class to an arbitrary number of steps:

y1n = un (7a)

- k
- l=1


- k−1
- l=1


- i−1
- j=1


yin =

dilun−k+l + ∆t

aˆilF(un−k+l) + ∆t

aijF(yjn) 2 ≤ i ≤ s (7b)

un+1 =

- k
- l=1


θlun−k+l + ∆t

- k−1
- l=1


ˆblF(un−k+l) + ∆t

s

bjF(yjn). (7c)

j=1

Here the values un−k+j denote the previous steps and yjn are intermediate stages used to compute the next solution value un+1. The form (7) is convenient for identifying the computational cost of the method: it is evident that s new function evaluations are needed to progress from un to un+1.

To study the strong stability preserving properties of method (7), we write it in the form [34]

w = Sx + ∆tTf. (8) To accomplish this, we stack the last k steps into a column vector:

x = un−k+1, un−k+2; . . ., un−1; un . We deﬁne a column vector of length k + s that contains these steps and the stages:

w = un−k+1; un−k+2; . . ., un−1; y1 = un; y2; . . .; ys; un+1 , and another column vector containing the derivative of each element of w:

f = F un−k+1 ; F un−k+2 ; . . .; F un−1 , F (y1); . . .; F (ys) ; F un+1 T .

Here we have used the semi-colon to denote (as in MATLAB) vertical concatenation of vectors. Thus, each of the above is a column vector.

Now the method (7) can be written in the matrix-vector form (8) where the matrices S and T are

0 0 0 Aˆ A 0 bˆT bT 0

 . (9)

  T = 

S = 

I(k−1)×(k−1) 01×(k−1) D θT





The matrices D, A, Aˆ and the vectors θ, bˆ, b contain the coeﬃcients dil, aˆil, aij and θl,ˆbl, bj from (7); note that the ﬁrst row of D is (0, 0, . . ., 0, 1) and the ﬁrst row of A, Aˆ is identically zero. Consistency requires that

- k
- l=1


θl = 1,

- k
- l=1


dil = 1 1 ≤ i ≤ s.

We also assume that (see [34, Section 2.1.1])

Se = e, (10)

where e is a column vector with all entries equal to unity. This condition is similar to the consistency conditions, and implies that every stage is consistent when viewed as a quadrature rule.

In the next two subsections we use representation (8) to study monotonicity properties of the method (7). The results in these subsections are a straightforward generalization of the corresponding results in [22], and so the discussion below is brief and the interested reader is referred to [22] for more detail.

### 2.1 A review of the SSP property for multistep Runge–Kutta methods

To write (8) as a linear combination of forward Euler steps, we add the term rTw to both sides of

(8), obtaining

(I + rT)w = Sx + rT w +

∆t r

f .

![image 5](<2013-bresten-explicit-strong-stability-preserving_images/imageFile5.png>)

We now left-multiply both sides by (I + rT)−1 (assuming it exists) to obtain

∆t r

w = (I + rT)−1Sx + r(I + rT)−1T w +

f

![image 6](<2013-bresten-explicit-strong-stability-preserving_images/imageFile6.png>)

∆t r

f , (11)

= Rx + P w +

![image 7](<2013-bresten-explicit-strong-stability-preserving_images/imageFile7.png>)

where

P = r(I + rT)−1T, R = (I + rT)−1S = (I − P)S. (12) In consequence of the consistency condition (10), the row sums of [R P] are each equal to one:

Re + Pe = (I − P)Se + Pe = e − Pe + Pe = e.

Thus if R and P have no negative entries, then each stage wi is a convex combination of the inputs xj and the forward Euler quantities wj +(∆t/r)F(wj). It is then simple to show (following [34]) that any strong stability property of the forward Euler method is preserved by the method (8) under the time-step restriction ∆t ≤ C(S, T)∆tFE where C(S, T) is deﬁned as

C(S, T) = sup

r

r : (I + rT)−1 exists and P ≥ 0, R ≥ 0 .

Hence the SSP coeﬃcient of method (11) is greater than or equal to C(S, T). In fact, following [34, Remark 3.2]) we can conclude that if the method is row-irreducible, then the SSP coeﬃcient is, in fact, exactly equal to C(S, T). (For the deﬁnition of row reducibility, see [34, Remark 3.2]) or [22]).

### 2.2 Order conditions

In [22] we derived order conditions for methods of the form (7) with two steps. Those conditions extend in a simple way to method (7) with any number of steps. For convenience, we rewrite (7) in the form

yn = Du˜ n + ∆tAf˜ n (13a) un+1 = θTun + ∆tb˜Tfn (13b)

where

D˜ =

I(k−1)×(k−1) 01×(k−1) D

A ˜ =

0 0 Aˆ A

b ˜ = b ˆ b , (14)

and yn = [un−k+1; un−k+2; . . .un−1; y1n; . . .; ysn], and fn = F(yn) are the vector of stage values and stage derivatives, respectively, and un = [un−k+1, un−k+2, . . ., un] is the vector of previous step values.

The derivation of the order conditions closely follows Section 3 of [22] with the following changes: (1) the vector d, is replaced by the matrix D; (2) the scalar θ is replaced by the vector θ; and (3) the vector l = (k − 1, k − 2, . . ., 1, 0)T appears in place of the number 1 in the expression for the stage residuals, which are thus:

1 k!

τk =

![image 8](<2013-bresten-explicit-strong-stability-preserving_images/imageFile8.png>)

1 (k − 1)!

1 k!

ck − D˜ (−l)k −

Ac˜ k−1, τk =

![image 9](<2013-bresten-explicit-strong-stability-preserving_images/imageFile9.png>)

![image 10](<2013-bresten-explicit-strong-stability-preserving_images/imageFile10.png>)

1 (k − 1)!

b˜Tck−1,

1 − θT(−l)k −

![image 11](<2013-bresten-explicit-strong-stability-preserving_images/imageFile11.png>)

where c = Ae˜ − D˜ l and exponents are to be interpreted element-wise. The derivation of the order conditions is identical to that in [22] except for these changes.

A method is said to have stage order q if τk and τk vanish for all k ≤ q. The following result is a simple extension of Theorem 2 in [22].

- Theorem 1. Any irreducible MSRK method (7) of order p with positive SSP coeﬃcient has stage order at least ⌊p−21⌋.


![image 12](<2013-bresten-explicit-strong-stability-preserving_images/imageFile12.png>)

Note that the approach used in [22], which is based on the work of Albrecht [1], produces a set of order conditions that are equivalent to the set of conditions derived using B-series. However, the two sets have diﬀerent equations. Albrecht’s approach has two advantages over that based on B-series in the present context. First, it leads to algebraically simpler conditions that are almost identical in appearance to those for one-step RK methods. Second, it leads to conditions in which the residualts τk appear explicitly. As a result, very many of the order conditions are a priori satisﬁed by methods with high stage order, due to Theorem 1. This simpliﬁes the numerical optimization problem that is formulated in Section 4.

## 3 Upper bounds on the SSP coeﬃcient

In this section we present upper bounds on the SSP coeﬃcient of general linear methods of ﬁrst and second order. These upper bounds apply to all explicit multistep multistage methods, not just those of form (7). They are obtained by considering a relaxed optimization problem. Speciﬁcally, we consider monotonicity and order conditions for methods applied to linear problems only.

Given a function ψ : C → C, let R(ψ) denote the radius of absolute monotonicity: R(ψ) = sup{r ≥ 0 | ψ(j)(z) ≥ 0 for all z ∈ [−r, 0]}. (15)

Here the ψ(j)(z) denotes the jth derivative of ψ at z. Any explicit general linear method applied to the linear, scalar ODE u′(t) = λu results in an iteration of the form

un+1 = ψ1(z)un + ψ2(z)un−1 + · · · + ψk(z)un−k+1, (16)

where z = ∆tλ and {ψ1, . . ., ψk} are polynomials of degree at most s. The method is strong stability preserving for linear problems under the stepsize restriction ∆t ≤ R(ψ1, . . ., ψk)∆tFE where

![image 13](<2013-bresten-explicit-strong-stability-preserving_images/imageFile13.png>)

![image 14](<2013-bresten-explicit-strong-stability-preserving_images/imageFile14.png>)

R(ψi). (17)

R(ψ1, . . ., ψk) = min

i

![image 15](<2013-bresten-explicit-strong-stability-preserving_images/imageFile15.png>)

The constant R(ψ1, . . ., ψk) is commonly referred to as the threshold factor [35]. We also refer to the optimal threshold factor

![image 16](<2013-bresten-explicit-strong-stability-preserving_images/imageFile16.png>)

Rs,k,p = sup R(ψ1, . . ., ψk) | (ψ1, . . ., ψk) ∈ Πs,k,p (18)

where Πs,k,p denotes the set of all stability functions of k-step, s-stage methods satisfying the order conditions up to order p. Clearly the SSP coeﬃcient of any s-stage, k-step, order p MSRK method is no greater than the corresponding Rs,k,p. Optimal values of Rs,k,p are given in [20].

The following result is proved in Section 2.3 of [12].

- Theorem 2. The threshold factor of a ﬁrst-order accurate explicit s-stage general linear method is at most s.

Methods consisting of s iterated forward Euler steps achieve this bound (with both threshold factor and SSP coeﬃcient equal to s). Clearly it provides an upper bound on the threshold factor and SSP coeﬃcient also for methods of higher order. For second order methods, a tighter bound is given in the next theorem. We will see in Section 4 that it is sharp, even over the smaller class of MSRK methods.

- Theorem 3. For any s ≥ 0, k > 1 the optimal threshold factor for explicit s-stage, k-step, second order general linear methods is


![image 17](<2013-bresten-explicit-strong-stability-preserving_images/imageFile17.png>)

(k − 2)s + (k − 2)2s2 + 4s(s − 1)(k − 1) 2(k − 1)

. (19)

Rs,k,2 :=

![image 18](<2013-bresten-explicit-strong-stability-preserving_images/imageFile18.png>)

Proof. It is convenient to write the stability polynomials in the form

ψi =

j

z r

γij 1 +

![image 19](<2013-bresten-explicit-strong-stability-preserving_images/imageFile19.png>)

j

![image 20](<2013-bresten-explicit-strong-stability-preserving_images/imageFile20.png>)

where we assume r ∈ [0, R(ψ1, . . ., ψk)], which implies

(20)

γij ≥ 0. (21) The conditions for second order accuracy are:

k

i=1

s

γij = 1, (22a)

j=0

k

i=1

s

γij(j + (k − i)r) = kr, (22b)

j=0

k

i=1

s

γij((k − i)2r2 + 2(k − i)jr + j(j − 1)) = k2r2. (22c)

j=0

We will show that conditions (21) and (22) cannot be satisﬁed for r greater than the claimed value

(19), which we denoted in the rest of the proof simply by R2.

By way of contradiction, suppose r > R2. Multiply (22b) by kr and subtract (22c) from the result to obtain

k

s

γij(i(k − i)r2 − (k − 2i)jr − j(j − 1)) = 0. (23)

i=1

j=0

Let us ﬁnd the maximal root of this equation, which is an upper bound on r. We introduce the following notation:

- a(γ) = +

k

i=1

s

j=0

γiji(k − i), (24a)

- b(γ) = −

k

i=1

s

j=0

γij(k − 2i)j, (24b)

- c(γ) = −


k

i=1

s

γijj(j − 1). (24c)

j=0

Case 1: a(γ) = 0. In this case we have γij = 0 for all i = k, so (23) simpliﬁes to

s

γkjj(kr − (j − 1)) = 0. (25)

j=0

This implies that either γkj = 0 for j = 0 or that r ≤ (s − 1)/k. The ﬁrst option fails to satisfy (22b), while the second contradicts our assumption r > R2.

Case 2: a(γ) = 0. The largest root always exists due to the positivity of a(γ) and the nonpositivity of c(γ), and it can be expressed as

−b(γ) 2a(γ)

+

r(γ) =

![image 21](<2013-bresten-explicit-strong-stability-preserving_images/imageFile21.png>)

![image 22](<2013-bresten-explicit-strong-stability-preserving_images/imageFile22.png>)

2

−c(γ) a(γ)

−b(γ) 2a(γ)

, (26)

+

![image 23](<2013-bresten-explicit-strong-stability-preserving_images/imageFile23.png>)

![image 24](<2013-bresten-explicit-strong-stability-preserving_images/imageFile24.png>)

which simpliﬁes to the desired r = R2 in case γ1s = 1, γij = 0 for all (i, j) = (1, s). (27)

We now show that any positive coeﬃcients γij can be transformed into the choice (27) without decreasing the largest root of (23).

Diﬀerentiating r(γ) with respect to γkj yields

∂ ∂γkj

r(γ) =

![image 25](<2013-bresten-explicit-strong-stability-preserving_images/imageFile25.png>)

=

−kj 2a(γ)

2b(γ)kj + 4a(γ)j(j − 1) 4a(γ) b(γ)2 − 4a(γ)c(γ)

+

![image 26](<2013-bresten-explicit-strong-stability-preserving_images/imageFile26.png>)

![image 27](<2013-bresten-explicit-strong-stability-preserving_images/imageFile27.png>)

![image 28](<2013-bresten-explicit-strong-stability-preserving_images/imageFile28.png>)

−r(γ)kj + j(j − 1) b(γ)2 − 4a(γ)c(γ)

, (28)

![image 29](<2013-bresten-explicit-strong-stability-preserving_images/imageFile29.png>)

![image 30](<2013-bresten-explicit-strong-stability-preserving_images/imageFile30.png>)

which is non-positive by our assumption r > R2. Thus the largest root of (23) will not decrease if we set

γkj := 0 (29) and then renormalize all the remaining γij so that (22a) holds. Next we apply the transformation

k 2

γij := γij + γk−i,j for all 1 ≤ i <

, (30a)

![image 31](<2013-bresten-explicit-strong-stability-preserving_images/imageFile31.png>)

k 2

γij := 0 for all

< i < k. (30b)

![image 32](<2013-bresten-explicit-strong-stability-preserving_images/imageFile32.png>)

which leaves a(γ) and c(γ) invariant, ensures b(γ) is nonpositive and increases its absolute value, thus increases the largest root. Now only negative terms contribute to b(γ), c(γ) and only positive terms contribute to a(γ). It follows that for ﬁxed (i, j) = (1, s) the transformation

γ1s := γ1s + γij, (31a) γij := 0 (31b)

increases the largest root as it decreases the positive a(γ) and increases the absolute value of the nonpositive b(γ), c(γ). Applying the transformation for all i, j we obtain (27).

We have shown that the claimed value is an upper bound on R2. This upper bound is achieved by taking

kR2 s − R2 + kR2

s − R2 s − R2 + kR2

, γij = 0 for all (i, j) ∈/ {(1, s), (k, 0)}, (32) which not only satisfy condition (23) but also (21) since R2 < s.

γ1s =

, γk0 =

![image 33](<2013-bresten-explicit-strong-stability-preserving_images/imageFile33.png>)

![image 34](<2013-bresten-explicit-strong-stability-preserving_images/imageFile34.png>)

![image 35](<2013-bresten-explicit-strong-stability-preserving_images/imageFile35.png>)

![image 36](<2013-bresten-explicit-strong-stability-preserving_images/imageFile36.png>)

![image 37](<2013-bresten-explicit-strong-stability-preserving_images/imageFile37.png>)

![image 38](<2013-bresten-explicit-strong-stability-preserving_images/imageFile38.png>)

## 4 Optimized explicit MSRK methods

In this section we present an optimization problem for ﬁnding MSRK methods with the largest possible SSP coeﬃcient. This optimization problem is implemented in a MATLAB code and solved using the fmincon function for optimization (code is available at our website [11]). This implementation recovers the known optimal methods of ﬁrst and second order mentioned above. For high order methods with large numbers of stages and steps, numerical solution of the optimization problem is diﬃcult due to the number of coeﬃcients and constraints. Despite the extensive numerical optimization searches, we do not claim that all of the methods found are truly optimal; we refer to them only as optimized. Some of the higher-order methods are known to be optimal because they achieve known upper bounds based on a relaxation of the optimization problem (presented in Section 3) or on certiﬁed computations in earlier work [5].

In Section 4.2 we present the eﬀective SSP coeﬃcients of the optimized methods. The coeﬃcients dil, aˆil, aij, θl,ˆbl and bj can be downloaded (as MATLAB ﬁles) from [11]. The SSP coeﬃcients of methods known to be optimal are printed in boldface in the corresponding tables. The coeﬃcients of methods that are known not to be optimal (e.g. when better methods have been found in the literature) are printed in the table in a light grey. We chose to include these to show the issues with the performance of the optimizer. We discuss these issues in the relevant sections below.

A major issue in the implementation and the performance of the optimized time integrators is the choice of starting methods to obtain the initial k step values. Typically exact values are not available, and we recommend the use of many small steps of a lower order SSP method to generate the starting values. A discussion of starting procedures appears in [22].

### 4.1 The optimization problem

Based on the results above, the problem of ﬁnding optimal SSP multistep Runge–Kutta methods can be formulated algebraically. We wish to ﬁnd coeﬃcients S and T (corresponding to (9)) that maximize the value of r subject to the following conditions:

- 1. (I + rT)−1 exists
- 2. r(I+rT)−1T ≥ 0 and (I+rT)−1S ≥ 0, where the inequalities are understood component-wise.
- 3. S and T satisfy the relevant order conditions.

This is a non-convex, nonlinear constrained optimization problem in many variables. The second constraint above implies some useful bounds on the coeﬃcients. Extending Theorem 3 of [22], one ﬁnds that if method (7) has positive SSP coeﬃcient then

0 ≤ D ≤ 1, 0 ≤ θ ≤ 1, (33a) A ≥ 0, Aˆ ≥ 0, (33b)

b ≥ 0 bˆ ≥ 0. (33c)

This problem was used to formulate a MATLAB optimization code that uses fmincon. We ran this extensively, and when needed used methods with lower number of steps as starting values. We note that for a large number of coeﬃcient and constraints, this optimization process was slow and seemed to get stuck in local minima.

- 4.2 Eﬀective SSP coeﬃcients of the optimized methods


We now discuss the optimized SSP coeﬃcients among methods with prescribed order, number of stages, and number of steps. For a given order, the SSP coeﬃcient is larger for methods with more stages, and usually the eﬀective SSP coeﬃcient is also larger. Comparing optimized SSP coeﬃcients among classes of methods with the same number of stages and order, but diﬀerent number of steps, we see the following behavior:

- • For methods of even order, the SSP coeﬃcient increases monotonically with k, and the marginal increase from k to k + 1 is smaller for larger k.
- • For methods of odd order up to ﬁve, for a large enough number of stages there exists k0 such that optimized methods never use more than k0 steps (hence the optimized SSP coeﬃcient remains the same as the allowed number of steps is increased beyond k0). The value of k0 depends on the order and number of stages.


This behavior seems to generalize that seen for multistep methods [25]. The behavior described for odd orders is observed here up to order ﬁve. Since the value of k0 increases with p, we expect that a study including larger k values would show the same behavior for optimized methods of higher (odd) order as well. Overall, the eﬀective SSP coeﬃcient tends to increase more quickly with the number of stages than with the number of steps.

Where relevant, we compare the methods we found to those of Constantinescu [5], Huang [18], and Vaillancourt [26, 27, 30].

- 4.2.1 Second-order methods

The second-order methods were ﬁrst found by the numerical optimization procedure above. We observed that the coeﬃcients of the optimal second-order methods have a clear structure, which we were then able to generalize and prove optimal in Theorem 3 above.

Table 1: Ceﬀ for second-order methods s\k 2 3 4 5

![image 39](<2013-bresten-explicit-strong-stability-preserving_images/imageFile39.png>)

![image 40](<2013-bresten-explicit-strong-stability-preserving_images/imageFile40.png>)

![image 41](<2013-bresten-explicit-strong-stability-preserving_images/imageFile41.png>)

![image 42](<2013-bresten-explicit-strong-stability-preserving_images/imageFile42.png>)

![image 43](<2013-bresten-explicit-strong-stability-preserving_images/imageFile43.png>)

![image 44](<2013-bresten-explicit-strong-stability-preserving_images/imageFile44.png>)

![image 45](<2013-bresten-explicit-strong-stability-preserving_images/imageFile45.png>)

![image 46](<2013-bresten-explicit-strong-stability-preserving_images/imageFile46.png>)

![image 47](<2013-bresten-explicit-strong-stability-preserving_images/imageFile47.png>)

- 2 0.70711 0.80902 0.86038 0.89039

![image 48](<2013-bresten-explicit-strong-stability-preserving_images/imageFile48.png>)

![image 49](<2013-bresten-explicit-strong-stability-preserving_images/imageFile49.png>)

![image 50](<2013-bresten-explicit-strong-stability-preserving_images/imageFile50.png>)

![image 51](<2013-bresten-explicit-strong-stability-preserving_images/imageFile51.png>)

![image 52](<2013-bresten-explicit-strong-stability-preserving_images/imageFile52.png>)

![image 53](<2013-bresten-explicit-strong-stability-preserving_images/imageFile53.png>)

![image 54](<2013-bresten-explicit-strong-stability-preserving_images/imageFile54.png>)

- 3 0.81650 0.87915 0.91068 0.92934

![image 55](<2013-bresten-explicit-strong-stability-preserving_images/imageFile55.png>)

![image 56](<2013-bresten-explicit-strong-stability-preserving_images/imageFile56.png>)

![image 57](<2013-bresten-explicit-strong-stability-preserving_images/imageFile57.png>)

![image 58](<2013-bresten-explicit-strong-stability-preserving_images/imageFile58.png>)

![image 59](<2013-bresten-explicit-strong-stability-preserving_images/imageFile59.png>)

![image 60](<2013-bresten-explicit-strong-stability-preserving_images/imageFile60.png>)

![image 61](<2013-bresten-explicit-strong-stability-preserving_images/imageFile61.png>)

- 4 0.86603 0.91144 0.93426 0.94782

![image 62](<2013-bresten-explicit-strong-stability-preserving_images/imageFile62.png>)

![image 63](<2013-bresten-explicit-strong-stability-preserving_images/imageFile63.png>)

![image 64](<2013-bresten-explicit-strong-stability-preserving_images/imageFile64.png>)

![image 65](<2013-bresten-explicit-strong-stability-preserving_images/imageFile65.png>)

![image 66](<2013-bresten-explicit-strong-stability-preserving_images/imageFile66.png>)

![image 67](<2013-bresten-explicit-strong-stability-preserving_images/imageFile67.png>)

![image 68](<2013-bresten-explicit-strong-stability-preserving_images/imageFile68.png>)

- 5 0.89443 0.93007 0.94797 0.95863

![image 69](<2013-bresten-explicit-strong-stability-preserving_images/imageFile69.png>)

![image 70](<2013-bresten-explicit-strong-stability-preserving_images/imageFile70.png>)

![image 71](<2013-bresten-explicit-strong-stability-preserving_images/imageFile71.png>)

![image 72](<2013-bresten-explicit-strong-stability-preserving_images/imageFile72.png>)

![image 73](<2013-bresten-explicit-strong-stability-preserving_images/imageFile73.png>)

![image 74](<2013-bresten-explicit-strong-stability-preserving_images/imageFile74.png>)

![image 75](<2013-bresten-explicit-strong-stability-preserving_images/imageFile75.png>)

- 6 0.91287 0.94222 0.95694 0.96573

![image 76](<2013-bresten-explicit-strong-stability-preserving_images/imageFile76.png>)

![image 77](<2013-bresten-explicit-strong-stability-preserving_images/imageFile77.png>)

![image 78](<2013-bresten-explicit-strong-stability-preserving_images/imageFile78.png>)

![image 79](<2013-bresten-explicit-strong-stability-preserving_images/imageFile79.png>)

![image 80](<2013-bresten-explicit-strong-stability-preserving_images/imageFile80.png>)

![image 81](<2013-bresten-explicit-strong-stability-preserving_images/imageFile81.png>)

![image 82](<2013-bresten-explicit-strong-stability-preserving_images/imageFile82.png>)

- 7 0.92582 0.95076 0.96327 0.97074

![image 83](<2013-bresten-explicit-strong-stability-preserving_images/imageFile83.png>)

![image 84](<2013-bresten-explicit-strong-stability-preserving_images/imageFile84.png>)

![image 85](<2013-bresten-explicit-strong-stability-preserving_images/imageFile85.png>)

![image 86](<2013-bresten-explicit-strong-stability-preserving_images/imageFile86.png>)

![image 87](<2013-bresten-explicit-strong-stability-preserving_images/imageFile87.png>)

![image 88](<2013-bresten-explicit-strong-stability-preserving_images/imageFile88.png>)

![image 89](<2013-bresten-explicit-strong-stability-preserving_images/imageFile89.png>)

- 8 0.93541 0.95711 0.96798 0.97448


![image 90](<2013-bresten-explicit-strong-stability-preserving_images/imageFile90.png>)

![image 91](<2013-bresten-explicit-strong-stability-preserving_images/imageFile91.png>)

![image 92](<2013-bresten-explicit-strong-stability-preserving_images/imageFile92.png>)

![image 93](<2013-bresten-explicit-strong-stability-preserving_images/imageFile93.png>)

![image 94](<2013-bresten-explicit-strong-stability-preserving_images/imageFile94.png>)

![image 95](<2013-bresten-explicit-strong-stability-preserving_images/imageFile95.png>)

Let Q = 2(k − 1)Rs,k,2. The non-zero coeﬃcients of these methods are:

dik = 1 1 ≤ i ≤ s, bj = β :=

kQ s(k − 1) (2(s − 1) + Q)

![image 96](<2013-bresten-explicit-strong-stability-preserving_images/imageFile96.png>)

1 ≤ j ≤ s,

aij = =

1 Rs,k,2

![image 97](<2013-bresten-explicit-strong-stability-preserving_images/imageFile97.png>)

1 ≤ j < i ≤ s

θk =

k − βs k − 1

![image 98](<2013-bresten-explicit-strong-stability-preserving_images/imageFile98.png>)

θ1 = 1 − θk.

These methods have C = Rs,k,2, which is proven optimal in Theorem 3 above. In Table 1 these values appear for s = 2, ..., 8 and k = 2, ..., 5. While the second-order methods are not so useful from a practical point of view, as many good low-order SSP methods are known, they are of great interest because the the optimal SSP coeﬃcient among 2nd-order methods with k steps and s stages is an upper bound on the SSP coeﬃcient for higher-order methods with the same values of k and s.

- 4.2.2 Third-order methods Table 2: Ceﬀ for third-order methods


![image 99](<2013-bresten-explicit-strong-stability-preserving_images/imageFile99.png>)

![image 100](<2013-bresten-explicit-strong-stability-preserving_images/imageFile100.png>)

![image 101](<2013-bresten-explicit-strong-stability-preserving_images/imageFile101.png>)

![image 102](<2013-bresten-explicit-strong-stability-preserving_images/imageFile102.png>)

![image 103](<2013-bresten-explicit-strong-stability-preserving_images/imageFile103.png>)

![image 104](<2013-bresten-explicit-strong-stability-preserving_images/imageFile104.png>)

![image 105](<2013-bresten-explicit-strong-stability-preserving_images/imageFile105.png>)

s\k 2 3 4 5

The eﬀective SSP coeﬃcients of optimized thirdorder methods are shown in Table 2 and plotted in Figure 1(a). All methods with four or more stages turn out to be two-step methods (i.e., k0 = 2 for this case). For s = 3, there is no advantage to increasing the number of steps beyond k0 = 3, and for s = 2, k0 = 4. Note that although we report only values up to ﬁve steps, this pattern was veriﬁed up to k = 8. All methods up to k = 4, s = 4 are optimal (to two decimal places) according to results of [5], and the Ceﬀ values for (s, k) = (2, 2), (3, 2), (2, 3) are provably optimal because they achieve the optimal value Rs,k,3, as described above.

![image 106](<2013-bresten-explicit-strong-stability-preserving_images/imageFile106.png>)

![image 107](<2013-bresten-explicit-strong-stability-preserving_images/imageFile107.png>)

- 2 0.36603 0.55643 0.57475 0.57475

![image 108](<2013-bresten-explicit-strong-stability-preserving_images/imageFile108.png>)

![image 109](<2013-bresten-explicit-strong-stability-preserving_images/imageFile109.png>)

![image 110](<2013-bresten-explicit-strong-stability-preserving_images/imageFile110.png>)

![image 111](<2013-bresten-explicit-strong-stability-preserving_images/imageFile111.png>)

![image 112](<2013-bresten-explicit-strong-stability-preserving_images/imageFile112.png>)

![image 113](<2013-bresten-explicit-strong-stability-preserving_images/imageFile113.png>)

![image 114](<2013-bresten-explicit-strong-stability-preserving_images/imageFile114.png>)

- 3 0.55019 0.57834 0.57834 0.57834

![image 115](<2013-bresten-explicit-strong-stability-preserving_images/imageFile115.png>)

![image 116](<2013-bresten-explicit-strong-stability-preserving_images/imageFile116.png>)

![image 117](<2013-bresten-explicit-strong-stability-preserving_images/imageFile117.png>)

![image 118](<2013-bresten-explicit-strong-stability-preserving_images/imageFile118.png>)

![image 119](<2013-bresten-explicit-strong-stability-preserving_images/imageFile119.png>)

![image 120](<2013-bresten-explicit-strong-stability-preserving_images/imageFile120.png>)

![image 121](<2013-bresten-explicit-strong-stability-preserving_images/imageFile121.png>)

- 4 0.57567 0.57567 0.57567 0.57567

![image 122](<2013-bresten-explicit-strong-stability-preserving_images/imageFile122.png>)

![image 123](<2013-bresten-explicit-strong-stability-preserving_images/imageFile123.png>)

![image 124](<2013-bresten-explicit-strong-stability-preserving_images/imageFile124.png>)

![image 125](<2013-bresten-explicit-strong-stability-preserving_images/imageFile125.png>)

![image 126](<2013-bresten-explicit-strong-stability-preserving_images/imageFile126.png>)

![image 127](<2013-bresten-explicit-strong-stability-preserving_images/imageFile127.png>)

![image 128](<2013-bresten-explicit-strong-stability-preserving_images/imageFile128.png>)

- 5 0.59758 0.59758 0.59758 0.59758

![image 129](<2013-bresten-explicit-strong-stability-preserving_images/imageFile129.png>)

![image 130](<2013-bresten-explicit-strong-stability-preserving_images/imageFile130.png>)

![image 131](<2013-bresten-explicit-strong-stability-preserving_images/imageFile131.png>)

![image 132](<2013-bresten-explicit-strong-stability-preserving_images/imageFile132.png>)

![image 133](<2013-bresten-explicit-strong-stability-preserving_images/imageFile133.png>)

![image 134](<2013-bresten-explicit-strong-stability-preserving_images/imageFile134.png>)

![image 135](<2013-bresten-explicit-strong-stability-preserving_images/imageFile135.png>)

- 6 0.62946 0.62946 0.62946 0.62946

![image 136](<2013-bresten-explicit-strong-stability-preserving_images/imageFile136.png>)

![image 137](<2013-bresten-explicit-strong-stability-preserving_images/imageFile137.png>)

![image 138](<2013-bresten-explicit-strong-stability-preserving_images/imageFile138.png>)

![image 139](<2013-bresten-explicit-strong-stability-preserving_images/imageFile139.png>)

![image 140](<2013-bresten-explicit-strong-stability-preserving_images/imageFile140.png>)

![image 141](<2013-bresten-explicit-strong-stability-preserving_images/imageFile141.png>)

![image 142](<2013-bresten-explicit-strong-stability-preserving_images/imageFile142.png>)

- 7 0.64051 0.64051 0.64051 0.64051

![image 143](<2013-bresten-explicit-strong-stability-preserving_images/imageFile143.png>)

![image 144](<2013-bresten-explicit-strong-stability-preserving_images/imageFile144.png>)

![image 145](<2013-bresten-explicit-strong-stability-preserving_images/imageFile145.png>)

![image 146](<2013-bresten-explicit-strong-stability-preserving_images/imageFile146.png>)

![image 147](<2013-bresten-explicit-strong-stability-preserving_images/imageFile147.png>)

![image 148](<2013-bresten-explicit-strong-stability-preserving_images/imageFile148.png>)

![image 149](<2013-bresten-explicit-strong-stability-preserving_images/imageFile149.png>)

- 8 0.65284 0.65284 0.65284 0.65284

![image 150](<2013-bresten-explicit-strong-stability-preserving_images/imageFile150.png>)

![image 151](<2013-bresten-explicit-strong-stability-preserving_images/imageFile151.png>)

![image 152](<2013-bresten-explicit-strong-stability-preserving_images/imageFile152.png>)

![image 153](<2013-bresten-explicit-strong-stability-preserving_images/imageFile153.png>)

![image 154](<2013-bresten-explicit-strong-stability-preserving_images/imageFile154.png>)

![image 155](<2013-bresten-explicit-strong-stability-preserving_images/imageFile155.png>)

![image 156](<2013-bresten-explicit-strong-stability-preserving_images/imageFile156.png>)

- 9 0.67220 0.67220 0.67220 0.67220

![image 157](<2013-bresten-explicit-strong-stability-preserving_images/imageFile157.png>)

![image 158](<2013-bresten-explicit-strong-stability-preserving_images/imageFile158.png>)

![image 159](<2013-bresten-explicit-strong-stability-preserving_images/imageFile159.png>)

![image 160](<2013-bresten-explicit-strong-stability-preserving_images/imageFile160.png>)

![image 161](<2013-bresten-explicit-strong-stability-preserving_images/imageFile161.png>)

![image 162](<2013-bresten-explicit-strong-stability-preserving_images/imageFile162.png>)

![image 163](<2013-bresten-explicit-strong-stability-preserving_images/imageFile163.png>)

- 10 0.68274 0.68274 0.68274 0.68274


![image 164](<2013-bresten-explicit-strong-stability-preserving_images/imageFile164.png>)

![image 165](<2013-bresten-explicit-strong-stability-preserving_images/imageFile165.png>)

![image 166](<2013-bresten-explicit-strong-stability-preserving_images/imageFile166.png>)

![image 167](<2013-bresten-explicit-strong-stability-preserving_images/imageFile167.png>)

![image 168](<2013-bresten-explicit-strong-stability-preserving_images/imageFile168.png>)

![image 169](<2013-bresten-explicit-strong-stability-preserving_images/imageFile169.png>)

- 4.2.3 Fourth-order methods Eﬀective coeﬃcients are given in Figure 1(b) and Table 3. All methods up to k = 4, s = 4 are optimal (to two decimal places) according to the certiﬁed optimization performed in [5]. The (2, 5, 4) method we found has an SSP coeﬃcient that matches that of [18].

Table 3: Ceﬀ for fourth-order methods s\k 2 3 4 5

![image 170](<2013-bresten-explicit-strong-stability-preserving_images/imageFile170.png>)

![image 171](<2013-bresten-explicit-strong-stability-preserving_images/imageFile171.png>)

![image 172](<2013-bresten-explicit-strong-stability-preserving_images/imageFile172.png>)

![image 173](<2013-bresten-explicit-strong-stability-preserving_images/imageFile173.png>)

![image 174](<2013-bresten-explicit-strong-stability-preserving_images/imageFile174.png>)

![image 175](<2013-bresten-explicit-strong-stability-preserving_images/imageFile175.png>)

![image 176](<2013-bresten-explicit-strong-stability-preserving_images/imageFile176.png>)

![image 177](<2013-bresten-explicit-strong-stability-preserving_images/imageFile177.png>)

![image 178](<2013-bresten-explicit-strong-stability-preserving_images/imageFile178.png>)

- 2 – 0.24767 0.34085 0.39640

![image 179](<2013-bresten-explicit-strong-stability-preserving_images/imageFile179.png>)

![image 180](<2013-bresten-explicit-strong-stability-preserving_images/imageFile180.png>)

![image 181](<2013-bresten-explicit-strong-stability-preserving_images/imageFile181.png>)

![image 182](<2013-bresten-explicit-strong-stability-preserving_images/imageFile182.png>)

![image 183](<2013-bresten-explicit-strong-stability-preserving_images/imageFile183.png>)

![image 184](<2013-bresten-explicit-strong-stability-preserving_images/imageFile184.png>)

![image 185](<2013-bresten-explicit-strong-stability-preserving_images/imageFile185.png>)

- 3 0.28628 0.38794 0.45515 0.48741

![image 186](<2013-bresten-explicit-strong-stability-preserving_images/imageFile186.png>)

![image 187](<2013-bresten-explicit-strong-stability-preserving_images/imageFile187.png>)

![image 188](<2013-bresten-explicit-strong-stability-preserving_images/imageFile188.png>)

![image 189](<2013-bresten-explicit-strong-stability-preserving_images/imageFile189.png>)

![image 190](<2013-bresten-explicit-strong-stability-preserving_images/imageFile190.png>)

![image 191](<2013-bresten-explicit-strong-stability-preserving_images/imageFile191.png>)

![image 192](<2013-bresten-explicit-strong-stability-preserving_images/imageFile192.png>)

- 4 0.39816 0.46087 0.48318 0.49478

![image 193](<2013-bresten-explicit-strong-stability-preserving_images/imageFile193.png>)

![image 194](<2013-bresten-explicit-strong-stability-preserving_images/imageFile194.png>)

![image 195](<2013-bresten-explicit-strong-stability-preserving_images/imageFile195.png>)

![image 196](<2013-bresten-explicit-strong-stability-preserving_images/imageFile196.png>)

![image 197](<2013-bresten-explicit-strong-stability-preserving_images/imageFile197.png>)

![image 198](<2013-bresten-explicit-strong-stability-preserving_images/imageFile198.png>)

![image 199](<2013-bresten-explicit-strong-stability-preserving_images/imageFile199.png>)

- 5 0.47209 0.50419 0.50905 0.51221

![image 200](<2013-bresten-explicit-strong-stability-preserving_images/imageFile200.png>)

![image 201](<2013-bresten-explicit-strong-stability-preserving_images/imageFile201.png>)

![image 202](<2013-bresten-explicit-strong-stability-preserving_images/imageFile202.png>)

![image 203](<2013-bresten-explicit-strong-stability-preserving_images/imageFile203.png>)

![image 204](<2013-bresten-explicit-strong-stability-preserving_images/imageFile204.png>)

![image 205](<2013-bresten-explicit-strong-stability-preserving_images/imageFile205.png>)

![image 206](<2013-bresten-explicit-strong-stability-preserving_images/imageFile206.png>)

- 6 0.50932 0.51214 0.51425 0.51550

![image 207](<2013-bresten-explicit-strong-stability-preserving_images/imageFile207.png>)

![image 208](<2013-bresten-explicit-strong-stability-preserving_images/imageFile208.png>)

![image 209](<2013-bresten-explicit-strong-stability-preserving_images/imageFile209.png>)

![image 210](<2013-bresten-explicit-strong-stability-preserving_images/imageFile210.png>)

![image 211](<2013-bresten-explicit-strong-stability-preserving_images/imageFile211.png>)

![image 212](<2013-bresten-explicit-strong-stability-preserving_images/imageFile212.png>)

![image 213](<2013-bresten-explicit-strong-stability-preserving_images/imageFile213.png>)

- 7 0.53436 0.53552 0.53610 0.53646

![image 214](<2013-bresten-explicit-strong-stability-preserving_images/imageFile214.png>)

![image 215](<2013-bresten-explicit-strong-stability-preserving_images/imageFile215.png>)

![image 216](<2013-bresten-explicit-strong-stability-preserving_images/imageFile216.png>)

![image 217](<2013-bresten-explicit-strong-stability-preserving_images/imageFile217.png>)

![image 218](<2013-bresten-explicit-strong-stability-preserving_images/imageFile218.png>)

![image 219](<2013-bresten-explicit-strong-stability-preserving_images/imageFile219.png>)

![image 220](<2013-bresten-explicit-strong-stability-preserving_images/imageFile220.png>)

- 8 0.56151 0.56250 0.56317 0.56362

![image 221](<2013-bresten-explicit-strong-stability-preserving_images/imageFile221.png>)

![image 222](<2013-bresten-explicit-strong-stability-preserving_images/imageFile222.png>)

![image 223](<2013-bresten-explicit-strong-stability-preserving_images/imageFile223.png>)

![image 224](<2013-bresten-explicit-strong-stability-preserving_images/imageFile224.png>)

![image 225](<2013-bresten-explicit-strong-stability-preserving_images/imageFile225.png>)

![image 226](<2013-bresten-explicit-strong-stability-preserving_images/imageFile226.png>)

![image 227](<2013-bresten-explicit-strong-stability-preserving_images/imageFile227.png>)

- 9 0.58561 0.58690 0.58871 0.58927

![image 228](<2013-bresten-explicit-strong-stability-preserving_images/imageFile228.png>)

![image 229](<2013-bresten-explicit-strong-stability-preserving_images/imageFile229.png>)

![image 230](<2013-bresten-explicit-strong-stability-preserving_images/imageFile230.png>)

![image 231](<2013-bresten-explicit-strong-stability-preserving_images/imageFile231.png>)

![image 232](<2013-bresten-explicit-strong-stability-preserving_images/imageFile232.png>)

![image 233](<2013-bresten-explicit-strong-stability-preserving_images/imageFile233.png>)

![image 234](<2013-bresten-explicit-strong-stability-preserving_images/imageFile234.png>)

- 10 0.61039 0.61415 0.61486 0.61532


![image 235](<2013-bresten-explicit-strong-stability-preserving_images/imageFile235.png>)

![image 236](<2013-bresten-explicit-strong-stability-preserving_images/imageFile236.png>)

![image 237](<2013-bresten-explicit-strong-stability-preserving_images/imageFile237.png>)

![image 238](<2013-bresten-explicit-strong-stability-preserving_images/imageFile238.png>)

![image 239](<2013-bresten-explicit-strong-stability-preserving_images/imageFile239.png>)

![image 240](<2013-bresten-explicit-strong-stability-preserving_images/imageFile240.png>)

Table 4: Ceﬀ for ﬁfth-order methods s\k 2 3 4 5

![image 241](<2013-bresten-explicit-strong-stability-preserving_images/imageFile241.png>)

![image 242](<2013-bresten-explicit-strong-stability-preserving_images/imageFile242.png>)

![image 243](<2013-bresten-explicit-strong-stability-preserving_images/imageFile243.png>)

![image 244](<2013-bresten-explicit-strong-stability-preserving_images/imageFile244.png>)

![image 245](<2013-bresten-explicit-strong-stability-preserving_images/imageFile245.png>)

![image 246](<2013-bresten-explicit-strong-stability-preserving_images/imageFile246.png>)

![image 247](<2013-bresten-explicit-strong-stability-preserving_images/imageFile247.png>)

![image 248](<2013-bresten-explicit-strong-stability-preserving_images/imageFile248.png>)

![image 249](<2013-bresten-explicit-strong-stability-preserving_images/imageFile249.png>)

- 2 – – 0.18556 0.26143

![image 250](<2013-bresten-explicit-strong-stability-preserving_images/imageFile250.png>)

![image 251](<2013-bresten-explicit-strong-stability-preserving_images/imageFile251.png>)

![image 252](<2013-bresten-explicit-strong-stability-preserving_images/imageFile252.png>)

![image 253](<2013-bresten-explicit-strong-stability-preserving_images/imageFile253.png>)

![image 254](<2013-bresten-explicit-strong-stability-preserving_images/imageFile254.png>)

![image 255](<2013-bresten-explicit-strong-stability-preserving_images/imageFile255.png>)

![image 256](<2013-bresten-explicit-strong-stability-preserving_images/imageFile256.png>)

- 3 – 0.21267 0.33364 0.38735

![image 257](<2013-bresten-explicit-strong-stability-preserving_images/imageFile257.png>)

![image 258](<2013-bresten-explicit-strong-stability-preserving_images/imageFile258.png>)

![image 259](<2013-bresten-explicit-strong-stability-preserving_images/imageFile259.png>)

![image 260](<2013-bresten-explicit-strong-stability-preserving_images/imageFile260.png>)

![image 261](<2013-bresten-explicit-strong-stability-preserving_images/imageFile261.png>)

![image 262](<2013-bresten-explicit-strong-stability-preserving_images/imageFile262.png>)

![image 263](<2013-bresten-explicit-strong-stability-preserving_images/imageFile263.png>)

- 4 0.21354 0.34158 0.38436 0.39067

![image 264](<2013-bresten-explicit-strong-stability-preserving_images/imageFile264.png>)

![image 265](<2013-bresten-explicit-strong-stability-preserving_images/imageFile265.png>)

![image 266](<2013-bresten-explicit-strong-stability-preserving_images/imageFile266.png>)

![image 267](<2013-bresten-explicit-strong-stability-preserving_images/imageFile267.png>)

![image 268](<2013-bresten-explicit-strong-stability-preserving_images/imageFile268.png>)

![image 269](<2013-bresten-explicit-strong-stability-preserving_images/imageFile269.png>)

![image 270](<2013-bresten-explicit-strong-stability-preserving_images/imageFile270.png>)

- 5 0.32962 0.38524 0.40054 0.40461

![image 271](<2013-bresten-explicit-strong-stability-preserving_images/imageFile271.png>)

![image 272](<2013-bresten-explicit-strong-stability-preserving_images/imageFile272.png>)

![image 273](<2013-bresten-explicit-strong-stability-preserving_images/imageFile273.png>)

![image 274](<2013-bresten-explicit-strong-stability-preserving_images/imageFile274.png>)

![image 275](<2013-bresten-explicit-strong-stability-preserving_images/imageFile275.png>)

![image 276](<2013-bresten-explicit-strong-stability-preserving_images/imageFile276.png>)

![image 277](<2013-bresten-explicit-strong-stability-preserving_images/imageFile277.png>)

- 6 0.38489 0.40386 0.40456 0.40456

![image 278](<2013-bresten-explicit-strong-stability-preserving_images/imageFile278.png>)

![image 279](<2013-bresten-explicit-strong-stability-preserving_images/imageFile279.png>)

![image 280](<2013-bresten-explicit-strong-stability-preserving_images/imageFile280.png>)

![image 281](<2013-bresten-explicit-strong-stability-preserving_images/imageFile281.png>)

![image 282](<2013-bresten-explicit-strong-stability-preserving_images/imageFile282.png>)

![image 283](<2013-bresten-explicit-strong-stability-preserving_images/imageFile283.png>)

![image 284](<2013-bresten-explicit-strong-stability-preserving_images/imageFile284.png>)

- 7 0.41826 0.42619 0.42619 0.42619

![image 285](<2013-bresten-explicit-strong-stability-preserving_images/imageFile285.png>)

![image 286](<2013-bresten-explicit-strong-stability-preserving_images/imageFile286.png>)

![image 287](<2013-bresten-explicit-strong-stability-preserving_images/imageFile287.png>)

![image 288](<2013-bresten-explicit-strong-stability-preserving_images/imageFile288.png>)

![image 289](<2013-bresten-explicit-strong-stability-preserving_images/imageFile289.png>)

![image 290](<2013-bresten-explicit-strong-stability-preserving_images/imageFile290.png>)

![image 291](<2013-bresten-explicit-strong-stability-preserving_images/imageFile291.png>)

- 8 0.44743 0.44743 0.44743 0.44743

![image 292](<2013-bresten-explicit-strong-stability-preserving_images/imageFile292.png>)

![image 293](<2013-bresten-explicit-strong-stability-preserving_images/imageFile293.png>)

![image 294](<2013-bresten-explicit-strong-stability-preserving_images/imageFile294.png>)

![image 295](<2013-bresten-explicit-strong-stability-preserving_images/imageFile295.png>)

![image 296](<2013-bresten-explicit-strong-stability-preserving_images/imageFile296.png>)

![image 297](<2013-bresten-explicit-strong-stability-preserving_images/imageFile297.png>)

![image 298](<2013-bresten-explicit-strong-stability-preserving_images/imageFile298.png>)

- 9 0.43794 0.43806 0.43806 0.43806

![image 299](<2013-bresten-explicit-strong-stability-preserving_images/imageFile299.png>)

![image 300](<2013-bresten-explicit-strong-stability-preserving_images/imageFile300.png>)

![image 301](<2013-bresten-explicit-strong-stability-preserving_images/imageFile301.png>)

![image 302](<2013-bresten-explicit-strong-stability-preserving_images/imageFile302.png>)

![image 303](<2013-bresten-explicit-strong-stability-preserving_images/imageFile303.png>)

![image 304](<2013-bresten-explicit-strong-stability-preserving_images/imageFile304.png>)

![image 305](<2013-bresten-explicit-strong-stability-preserving_images/imageFile305.png>)

- 10 0.42544 0.43056 0.43098 0.43098


![image 306](<2013-bresten-explicit-strong-stability-preserving_images/imageFile306.png>)

![image 307](<2013-bresten-explicit-strong-stability-preserving_images/imageFile307.png>)

![image 308](<2013-bresten-explicit-strong-stability-preserving_images/imageFile308.png>)

![image 309](<2013-bresten-explicit-strong-stability-preserving_images/imageFile309.png>)

![image 310](<2013-bresten-explicit-strong-stability-preserving_images/imageFile310.png>)

![image 311](<2013-bresten-explicit-strong-stability-preserving_images/imageFile311.png>)

- 4.2.4 Fifth-order methods

The eﬀective SSP coeﬃcients of the ﬁfth-order methods are displayed in Figure 1(c) and Table 4. Although the optimized SSP coeﬃcient is a strictly increasing function of the number of stages, in some cases the eﬀective SSP coeﬃcient decreases. Our (s, k) = (2, 4) and (s, k) = (2, 5) methods have eﬀective SSP coeﬃcients that match the ones in [18]. Our (s, k) = (8, 2), (3, 3), (3, 4), (3, 5), and (7, 3) methods have eﬀective SSP coeﬃcient that match those in [30, 26, 27].

- 4.2.5 Sixth-order methods


Table 5: Ceﬀ for sixth-order methods s\k 2 3 4 5

![image 312](<2013-bresten-explicit-strong-stability-preserving_images/imageFile312.png>)

![image 313](<2013-bresten-explicit-strong-stability-preserving_images/imageFile313.png>)

![image 314](<2013-bresten-explicit-strong-stability-preserving_images/imageFile314.png>)

![image 315](<2013-bresten-explicit-strong-stability-preserving_images/imageFile315.png>)

![image 316](<2013-bresten-explicit-strong-stability-preserving_images/imageFile316.png>)

![image 317](<2013-bresten-explicit-strong-stability-preserving_images/imageFile317.png>)

![image 318](<2013-bresten-explicit-strong-stability-preserving_images/imageFile318.png>)

![image 319](<2013-bresten-explicit-strong-stability-preserving_images/imageFile319.png>)

![image 320](<2013-bresten-explicit-strong-stability-preserving_images/imageFile320.png>)

- 2 – – – 0.10451

![image 321](<2013-bresten-explicit-strong-stability-preserving_images/imageFile321.png>)

![image 322](<2013-bresten-explicit-strong-stability-preserving_images/imageFile322.png>)

![image 323](<2013-bresten-explicit-strong-stability-preserving_images/imageFile323.png>)

![image 324](<2013-bresten-explicit-strong-stability-preserving_images/imageFile324.png>)

![image 325](<2013-bresten-explicit-strong-stability-preserving_images/imageFile325.png>)

![image 326](<2013-bresten-explicit-strong-stability-preserving_images/imageFile326.png>)

![image 327](<2013-bresten-explicit-strong-stability-preserving_images/imageFile327.png>)

- 3 – 0.00971 0.11192 0.21889

![image 328](<2013-bresten-explicit-strong-stability-preserving_images/imageFile328.png>)

![image 329](<2013-bresten-explicit-strong-stability-preserving_images/imageFile329.png>)

![image 330](<2013-bresten-explicit-strong-stability-preserving_images/imageFile330.png>)

![image 331](<2013-bresten-explicit-strong-stability-preserving_images/imageFile331.png>)

![image 332](<2013-bresten-explicit-strong-stability-preserving_images/imageFile332.png>)

![image 333](<2013-bresten-explicit-strong-stability-preserving_images/imageFile333.png>)

![image 334](<2013-bresten-explicit-strong-stability-preserving_images/imageFile334.png>)

- 4 – 0.17924 0.27118 0.31639

![image 335](<2013-bresten-explicit-strong-stability-preserving_images/imageFile335.png>)

![image 336](<2013-bresten-explicit-strong-stability-preserving_images/imageFile336.png>)

![image 337](<2013-bresten-explicit-strong-stability-preserving_images/imageFile337.png>)

![image 338](<2013-bresten-explicit-strong-stability-preserving_images/imageFile338.png>)

![image 339](<2013-bresten-explicit-strong-stability-preserving_images/imageFile339.png>)

![image 340](<2013-bresten-explicit-strong-stability-preserving_images/imageFile340.png>)

![image 341](<2013-bresten-explicit-strong-stability-preserving_images/imageFile341.png>)

- 5 – 0.27216 0.32746 0.34142

![image 342](<2013-bresten-explicit-strong-stability-preserving_images/imageFile342.png>)

![image 343](<2013-bresten-explicit-strong-stability-preserving_images/imageFile343.png>)

![image 344](<2013-bresten-explicit-strong-stability-preserving_images/imageFile344.png>)

![image 345](<2013-bresten-explicit-strong-stability-preserving_images/imageFile345.png>)

![image 346](<2013-bresten-explicit-strong-stability-preserving_images/imageFile346.png>)

![image 347](<2013-bresten-explicit-strong-stability-preserving_images/imageFile347.png>)

![image 348](<2013-bresten-explicit-strong-stability-preserving_images/imageFile348.png>)

- 6 0.09928 0.32302 0.33623 0.34453

![image 349](<2013-bresten-explicit-strong-stability-preserving_images/imageFile349.png>)

![image 350](<2013-bresten-explicit-strong-stability-preserving_images/imageFile350.png>)

![image 351](<2013-bresten-explicit-strong-stability-preserving_images/imageFile351.png>)

![image 352](<2013-bresten-explicit-strong-stability-preserving_images/imageFile352.png>)

![image 353](<2013-bresten-explicit-strong-stability-preserving_images/imageFile353.png>)

![image 354](<2013-bresten-explicit-strong-stability-preserving_images/imageFile354.png>)

![image 355](<2013-bresten-explicit-strong-stability-preserving_images/imageFile355.png>)

- 7 0.18171 0.34129 0.34899 0.35226

![image 356](<2013-bresten-explicit-strong-stability-preserving_images/imageFile356.png>)

![image 357](<2013-bresten-explicit-strong-stability-preserving_images/imageFile357.png>)

![image 358](<2013-bresten-explicit-strong-stability-preserving_images/imageFile358.png>)

![image 359](<2013-bresten-explicit-strong-stability-preserving_images/imageFile359.png>)

![image 360](<2013-bresten-explicit-strong-stability-preserving_images/imageFile360.png>)

![image 361](<2013-bresten-explicit-strong-stability-preserving_images/imageFile361.png>)

![image 362](<2013-bresten-explicit-strong-stability-preserving_images/imageFile362.png>)

- 8 0.24230 0.33951 0.34470 0.34680

![image 363](<2013-bresten-explicit-strong-stability-preserving_images/imageFile363.png>)

![image 364](<2013-bresten-explicit-strong-stability-preserving_images/imageFile364.png>)

![image 365](<2013-bresten-explicit-strong-stability-preserving_images/imageFile365.png>)

![image 366](<2013-bresten-explicit-strong-stability-preserving_images/imageFile366.png>)

![image 367](<2013-bresten-explicit-strong-stability-preserving_images/imageFile367.png>)

![image 368](<2013-bresten-explicit-strong-stability-preserving_images/imageFile368.png>)

![image 369](<2013-bresten-explicit-strong-stability-preserving_images/imageFile369.png>)

- 9 0.28696 0.34937 0.34977 0.35033

![image 370](<2013-bresten-explicit-strong-stability-preserving_images/imageFile370.png>)

![image 371](<2013-bresten-explicit-strong-stability-preserving_images/imageFile371.png>)

![image 372](<2013-bresten-explicit-strong-stability-preserving_images/imageFile372.png>)

![image 373](<2013-bresten-explicit-strong-stability-preserving_images/imageFile373.png>)

![image 374](<2013-bresten-explicit-strong-stability-preserving_images/imageFile374.png>)

![image 375](<2013-bresten-explicit-strong-stability-preserving_images/imageFile375.png>)

![image 376](<2013-bresten-explicit-strong-stability-preserving_images/imageFile376.png>)

- 10 0.31992 0.35422 0.35643 0.35665


Eﬀective SSP coeﬃcients of optimized sixthorder methods are given in Figure 1(d) and Table

- 5. Once again, the eﬀective SSP coeﬃcient occasionally decreases with increasing stage number. Our (s, k) = (2, 5) method has an eﬀective SSP coeﬃcient that matches the one in [18], and our values for (s, k) = (8, 3), (8, 4), and (8, 5) improve upon the values obtained in [30]. Our values for


![image 377](<2013-bresten-explicit-strong-stability-preserving_images/imageFile377.png>)

![image 378](<2013-bresten-explicit-strong-stability-preserving_images/imageFile378.png>)

![image 379](<2013-bresten-explicit-strong-stability-preserving_images/imageFile379.png>)

![image 380](<2013-bresten-explicit-strong-stability-preserving_images/imageFile380.png>)

![image 381](<2013-bresten-explicit-strong-stability-preserving_images/imageFile381.png>)

- (s, k) = (7, 3), (7, 4) match those of [27] and our (s, k) = (7, 5) value improves on that in [27]. The (s, k) = (3, 4), (3, 5) values illustrate the challenges in using our general numerical optimization formulation for this problem: we were not able to match


![image 382](<2013-bresten-explicit-strong-stability-preserving_images/imageFile382.png>)

0.68

0.66

0.64

0.62

Ceff

0.6

0.58

Three step methods

0.56

Four step methods Five step methods

0.54

2 3 4 5 6 7 8 9 10

stages

(a) Third-order methods

0.45

0.4

0.35

Ceff

0.3

0.25

|Three step methods<br><br>Four step methods Five step methods<br><br>|
|---|


0.2

2 3 4 5 6 7 8 9 10

stages

(c) Fifth-order methods

0.3

0.25

0.2

Ceff

0.15

0.1

|Three step methods<br><br>Four step methods Five step methods<br><br>|
|---|


0.05

0

3 4 5 6 7 8 9 10

stages

(e) Seventh-order methods

0.6

0.55

0.5

0.45

Ceff

0.4

0.35

|Three step methods<br><br>Four step methods Five step methods<br><br>|
|---|


0.3

0.25

2 3 4 5 6 7 8 9 10

stages

(b) Fourth-order methods

0.35

0.3

0.25

0.2

stages Ceff

0.15

0.1

|Three step methods<br><br>Four step methods Five step methods<br><br>|
|---|


0.05

0

2 3 4 5 6 7 8 9 10

(d) Sixth-order methods

0.25

|Three step methods<br><br>Four step methods Five step methods<br><br>|
|---|


0.2

0.15

Ceff

0.1

0.05

0

5 6 7 8 9 10

stages

(f) Eighth-order methods

Figure 1: Eﬀective SSP coeﬃcients of optimized methods.

the methods in [26] from a "cold start" (with random initial guesses). However, converting their methods to our form we were able to replicate their results while tightening the optimizer parameters TolCon, TolFun and TolX from 10−12 in their work to 10−14. This suggests that the approach used in [26] which focuses on one set of parameters at a time may make the optimization problem more manageable. However, this same approach was used in [27] and led to a (s, k) = (7, 5) method that had a smaller SSP coeﬃcient than that found with our approach.

- 4.2.6 Seventh order methods

The eﬀective SSP coeﬃcients for the seventh order case show consistent increase as both the steps and stages increase. There is more beneﬁt to increasing stages rather than steps once the number of steps is large enough, though for small k relative to s an an increase in steps is preferable. The behavior of the eﬀective SSP coeﬃcient is also summarized in Figure 1(e) and Table 6. Compared to the seven-step two-stage method in [18], which has C = 0.234 and Ceﬀ = 0.117, our ﬁve step methods with s ≥ 3, four step with k ≥ 5, three step with k ≥ 6 and two step with k ≥ 9 all have larger eﬀective SSP coeﬃcient. Our (7, 4), (7, 5), (3, 5) methods have SSP coeﬃcients that match those in [27] and [26], while our (7, 3) and (8, 3), (8, 4), (8, 5) have larger SSP coeﬃcients that those in [27] and [30].

Table 6: Ceﬀ for seventh order methods Ceﬀ for seventh order methods

![image 383](<2013-bresten-explicit-strong-stability-preserving_images/imageFile383.png>)

![image 384](<2013-bresten-explicit-strong-stability-preserving_images/imageFile384.png>)

![image 385](<2013-bresten-explicit-strong-stability-preserving_images/imageFile385.png>)

![image 386](<2013-bresten-explicit-strong-stability-preserving_images/imageFile386.png>)

![image 387](<2013-bresten-explicit-strong-stability-preserving_images/imageFile387.png>)

s\k 2 3 4 5

![image 388](<2013-bresten-explicit-strong-stability-preserving_images/imageFile388.png>)

![image 389](<2013-bresten-explicit-strong-stability-preserving_images/imageFile389.png>)

![image 390](<2013-bresten-explicit-strong-stability-preserving_images/imageFile390.png>)

![image 391](<2013-bresten-explicit-strong-stability-preserving_images/imageFile391.png>)

![image 392](<2013-bresten-explicit-strong-stability-preserving_images/imageFile392.png>)

![image 393](<2013-bresten-explicit-strong-stability-preserving_images/imageFile393.png>)

![image 394](<2013-bresten-explicit-strong-stability-preserving_images/imageFile394.png>)

- 2 – – – –

![image 395](<2013-bresten-explicit-strong-stability-preserving_images/imageFile395.png>)

![image 396](<2013-bresten-explicit-strong-stability-preserving_images/imageFile396.png>)

![image 397](<2013-bresten-explicit-strong-stability-preserving_images/imageFile397.png>)

![image 398](<2013-bresten-explicit-strong-stability-preserving_images/imageFile398.png>)

![image 399](<2013-bresten-explicit-strong-stability-preserving_images/imageFile399.png>)

![image 400](<2013-bresten-explicit-strong-stability-preserving_images/imageFile400.png>)

![image 401](<2013-bresten-explicit-strong-stability-preserving_images/imageFile401.png>)

- 3 – – – 0.12735

![image 402](<2013-bresten-explicit-strong-stability-preserving_images/imageFile402.png>)

![image 403](<2013-bresten-explicit-strong-stability-preserving_images/imageFile403.png>)

![image 404](<2013-bresten-explicit-strong-stability-preserving_images/imageFile404.png>)

![image 405](<2013-bresten-explicit-strong-stability-preserving_images/imageFile405.png>)

![image 406](<2013-bresten-explicit-strong-stability-preserving_images/imageFile406.png>)

![image 407](<2013-bresten-explicit-strong-stability-preserving_images/imageFile407.png>)

![image 408](<2013-bresten-explicit-strong-stability-preserving_images/imageFile408.png>)

- 4 – – 0.04584 0.22049

![image 409](<2013-bresten-explicit-strong-stability-preserving_images/imageFile409.png>)

![image 410](<2013-bresten-explicit-strong-stability-preserving_images/imageFile410.png>)

![image 411](<2013-bresten-explicit-strong-stability-preserving_images/imageFile411.png>)

![image 412](<2013-bresten-explicit-strong-stability-preserving_images/imageFile412.png>)

![image 413](<2013-bresten-explicit-strong-stability-preserving_images/imageFile413.png>)

![image 414](<2013-bresten-explicit-strong-stability-preserving_images/imageFile414.png>)

![image 415](<2013-bresten-explicit-strong-stability-preserving_images/imageFile415.png>)

- 5 – 0.06611 0.23887 0.28137

![image 416](<2013-bresten-explicit-strong-stability-preserving_images/imageFile416.png>)

![image 417](<2013-bresten-explicit-strong-stability-preserving_images/imageFile417.png>)

![image 418](<2013-bresten-explicit-strong-stability-preserving_images/imageFile418.png>)

![image 419](<2013-bresten-explicit-strong-stability-preserving_images/imageFile419.png>)

![image 420](<2013-bresten-explicit-strong-stability-preserving_images/imageFile420.png>)

![image 421](<2013-bresten-explicit-strong-stability-preserving_images/imageFile421.png>)

![image 422](<2013-bresten-explicit-strong-stability-preserving_images/imageFile422.png>)

- 6 – 0.15811 0.28980 0.30063

![image 423](<2013-bresten-explicit-strong-stability-preserving_images/imageFile423.png>)

![image 424](<2013-bresten-explicit-strong-stability-preserving_images/imageFile424.png>)

![image 425](<2013-bresten-explicit-strong-stability-preserving_images/imageFile425.png>)

![image 426](<2013-bresten-explicit-strong-stability-preserving_images/imageFile426.png>)

![image 427](<2013-bresten-explicit-strong-stability-preserving_images/imageFile427.png>)

![image 428](<2013-bresten-explicit-strong-stability-preserving_images/imageFile428.png>)

![image 429](<2013-bresten-explicit-strong-stability-preserving_images/imageFile429.png>)

- 7 – 0.24269 0.28562 0.29235

![image 430](<2013-bresten-explicit-strong-stability-preserving_images/imageFile430.png>)

![image 431](<2013-bresten-explicit-strong-stability-preserving_images/imageFile431.png>)

![image 432](<2013-bresten-explicit-strong-stability-preserving_images/imageFile432.png>)

![image 433](<2013-bresten-explicit-strong-stability-preserving_images/imageFile433.png>)

![image 434](<2013-bresten-explicit-strong-stability-preserving_images/imageFile434.png>)

![image 435](<2013-bresten-explicit-strong-stability-preserving_images/imageFile435.png>)

![image 436](<2013-bresten-explicit-strong-stability-preserving_images/imageFile436.png>)

- 8 – 0.26988 0.28517 0.28715

![image 437](<2013-bresten-explicit-strong-stability-preserving_images/imageFile437.png>)

![image 438](<2013-bresten-explicit-strong-stability-preserving_images/imageFile438.png>)

![image 439](<2013-bresten-explicit-strong-stability-preserving_images/imageFile439.png>)

![image 440](<2013-bresten-explicit-strong-stability-preserving_images/imageFile440.png>)

![image 441](<2013-bresten-explicit-strong-stability-preserving_images/imageFile441.png>)

![image 442](<2013-bresten-explicit-strong-stability-preserving_images/imageFile442.png>)

![image 443](<2013-bresten-explicit-strong-stability-preserving_images/imageFile443.png>)

- 9 0.12444 0.29046 0.29616 0.29759

![image 444](<2013-bresten-explicit-strong-stability-preserving_images/imageFile444.png>)

![image 445](<2013-bresten-explicit-strong-stability-preserving_images/imageFile445.png>)

![image 446](<2013-bresten-explicit-strong-stability-preserving_images/imageFile446.png>)

![image 447](<2013-bresten-explicit-strong-stability-preserving_images/imageFile447.png>)

![image 448](<2013-bresten-explicit-strong-stability-preserving_images/imageFile448.png>)

![image 449](<2013-bresten-explicit-strong-stability-preserving_images/imageFile449.png>)

![image 450](<2013-bresten-explicit-strong-stability-preserving_images/imageFile450.png>)

- 10 0.17857 0.29522 0.30876 0.30886


![image 451](<2013-bresten-explicit-strong-stability-preserving_images/imageFile451.png>)

![image 452](<2013-bresten-explicit-strong-stability-preserving_images/imageFile452.png>)

![image 453](<2013-bresten-explicit-strong-stability-preserving_images/imageFile453.png>)

![image 454](<2013-bresten-explicit-strong-stability-preserving_images/imageFile454.png>)

![image 455](<2013-bresten-explicit-strong-stability-preserving_images/imageFile455.png>)

![image 456](<2013-bresten-explicit-strong-stability-preserving_images/imageFile456.png>)

Table 7: Ceﬀ for eighth order methods Ceﬀ for eighth order methods s\k 2 3 4 5

![image 457](<2013-bresten-explicit-strong-stability-preserving_images/imageFile457.png>)

![image 458](<2013-bresten-explicit-strong-stability-preserving_images/imageFile458.png>)

![image 459](<2013-bresten-explicit-strong-stability-preserving_images/imageFile459.png>)

![image 460](<2013-bresten-explicit-strong-stability-preserving_images/imageFile460.png>)

![image 461](<2013-bresten-explicit-strong-stability-preserving_images/imageFile461.png>)

![image 462](<2013-bresten-explicit-strong-stability-preserving_images/imageFile462.png>)

![image 463](<2013-bresten-explicit-strong-stability-preserving_images/imageFile463.png>)

![image 464](<2013-bresten-explicit-strong-stability-preserving_images/imageFile464.png>)

![image 465](<2013-bresten-explicit-strong-stability-preserving_images/imageFile465.png>)

![image 466](<2013-bresten-explicit-strong-stability-preserving_images/imageFile466.png>)

![image 467](<2013-bresten-explicit-strong-stability-preserving_images/imageFile467.png>)

![image 468](<2013-bresten-explicit-strong-stability-preserving_images/imageFile468.png>)

- 2 – – – –

![image 469](<2013-bresten-explicit-strong-stability-preserving_images/imageFile469.png>)

![image 470](<2013-bresten-explicit-strong-stability-preserving_images/imageFile470.png>)

![image 471](<2013-bresten-explicit-strong-stability-preserving_images/imageFile471.png>)

![image 472](<2013-bresten-explicit-strong-stability-preserving_images/imageFile472.png>)

![image 473](<2013-bresten-explicit-strong-stability-preserving_images/imageFile473.png>)

![image 474](<2013-bresten-explicit-strong-stability-preserving_images/imageFile474.png>)

![image 475](<2013-bresten-explicit-strong-stability-preserving_images/imageFile475.png>)

- 3 – – – –

![image 476](<2013-bresten-explicit-strong-stability-preserving_images/imageFile476.png>)

![image 477](<2013-bresten-explicit-strong-stability-preserving_images/imageFile477.png>)

![image 478](<2013-bresten-explicit-strong-stability-preserving_images/imageFile478.png>)

![image 479](<2013-bresten-explicit-strong-stability-preserving_images/imageFile479.png>)

![image 480](<2013-bresten-explicit-strong-stability-preserving_images/imageFile480.png>)

![image 481](<2013-bresten-explicit-strong-stability-preserving_images/imageFile481.png>)

![image 482](<2013-bresten-explicit-strong-stability-preserving_images/imageFile482.png>)

- 4 – – – –

![image 483](<2013-bresten-explicit-strong-stability-preserving_images/imageFile483.png>)

![image 484](<2013-bresten-explicit-strong-stability-preserving_images/imageFile484.png>)

![image 485](<2013-bresten-explicit-strong-stability-preserving_images/imageFile485.png>)

![image 486](<2013-bresten-explicit-strong-stability-preserving_images/imageFile486.png>)

![image 487](<2013-bresten-explicit-strong-stability-preserving_images/imageFile487.png>)

![image 488](<2013-bresten-explicit-strong-stability-preserving_images/imageFile488.png>)

![image 489](<2013-bresten-explicit-strong-stability-preserving_images/imageFile489.png>)

- 5 – – 0.04781 0.10007

![image 490](<2013-bresten-explicit-strong-stability-preserving_images/imageFile490.png>)

![image 491](<2013-bresten-explicit-strong-stability-preserving_images/imageFile491.png>)

![image 492](<2013-bresten-explicit-strong-stability-preserving_images/imageFile492.png>)

![image 493](<2013-bresten-explicit-strong-stability-preserving_images/imageFile493.png>)

![image 494](<2013-bresten-explicit-strong-stability-preserving_images/imageFile494.png>)

![image 495](<2013-bresten-explicit-strong-stability-preserving_images/imageFile495.png>)

![image 496](<2013-bresten-explicit-strong-stability-preserving_images/imageFile496.png>)

- 6 – – 0.07991 0.22574

![image 497](<2013-bresten-explicit-strong-stability-preserving_images/imageFile497.png>)

![image 498](<2013-bresten-explicit-strong-stability-preserving_images/imageFile498.png>)

![image 499](<2013-bresten-explicit-strong-stability-preserving_images/imageFile499.png>)

![image 500](<2013-bresten-explicit-strong-stability-preserving_images/imageFile500.png>)

![image 501](<2013-bresten-explicit-strong-stability-preserving_images/imageFile501.png>)

![image 502](<2013-bresten-explicit-strong-stability-preserving_images/imageFile502.png>)

![image 503](<2013-bresten-explicit-strong-stability-preserving_images/imageFile503.png>)

- 7 – – 0.14818 0.22229

![image 504](<2013-bresten-explicit-strong-stability-preserving_images/imageFile504.png>)

![image 505](<2013-bresten-explicit-strong-stability-preserving_images/imageFile505.png>)

![image 506](<2013-bresten-explicit-strong-stability-preserving_images/imageFile506.png>)

![image 507](<2013-bresten-explicit-strong-stability-preserving_images/imageFile507.png>)

![image 508](<2013-bresten-explicit-strong-stability-preserving_images/imageFile508.png>)

![image 509](<2013-bresten-explicit-strong-stability-preserving_images/imageFile509.png>)

![image 510](<2013-bresten-explicit-strong-stability-preserving_images/imageFile510.png>)

- 8 – 0.09992 0.16323 0.19538

![image 511](<2013-bresten-explicit-strong-stability-preserving_images/imageFile511.png>)

![image 512](<2013-bresten-explicit-strong-stability-preserving_images/imageFile512.png>)

![image 513](<2013-bresten-explicit-strong-stability-preserving_images/imageFile513.png>)

![image 514](<2013-bresten-explicit-strong-stability-preserving_images/imageFile514.png>)

![image 515](<2013-bresten-explicit-strong-stability-preserving_images/imageFile515.png>)

![image 516](<2013-bresten-explicit-strong-stability-preserving_images/imageFile516.png>)

![image 517](<2013-bresten-explicit-strong-stability-preserving_images/imageFile517.png>)

- 9 – 0.14948 0.21012 0.23826

![image 518](<2013-bresten-explicit-strong-stability-preserving_images/imageFile518.png>)

![image 519](<2013-bresten-explicit-strong-stability-preserving_images/imageFile519.png>)

![image 520](<2013-bresten-explicit-strong-stability-preserving_images/imageFile520.png>)

![image 521](<2013-bresten-explicit-strong-stability-preserving_images/imageFile521.png>)

![image 522](<2013-bresten-explicit-strong-stability-preserving_images/imageFile522.png>)

![image 523](<2013-bresten-explicit-strong-stability-preserving_images/imageFile523.png>)

![image 524](<2013-bresten-explicit-strong-stability-preserving_images/imageFile524.png>)

- 10 – 0.20012 0.21517 0.24719


![image 525](<2013-bresten-explicit-strong-stability-preserving_images/imageFile525.png>)

![image 526](<2013-bresten-explicit-strong-stability-preserving_images/imageFile526.png>)

![image 527](<2013-bresten-explicit-strong-stability-preserving_images/imageFile527.png>)

![image 528](<2013-bresten-explicit-strong-stability-preserving_images/imageFile528.png>)

![image 529](<2013-bresten-explicit-strong-stability-preserving_images/imageFile529.png>)

![image 530](<2013-bresten-explicit-strong-stability-preserving_images/imageFile530.png>)

- 4.2.7 Eighth order methods


Explicit eighth order two-step RK methods found in [22] require at least 11 stages and have Ceﬀ ≤ 0.078. Much larger values of Ceﬀ can be achieved with fewer stages by using additional steps,

- as shown in Figure 1(f) and Table 7. The best method has Ceﬀ ≈ 0.247; to achieve the same eﬃciency with a linear multistep method requires the use of more than thirty steps [21]. Once


again, due to the number of coeﬃcients and constraints this was a diﬃcult optimization problem and we were not able to converge to the best methods from a "cold start". This is evident in our

- (s, k) = (7, 4), (7, 5), (8, 3), (8, 4), (8, 5) methods which have a smaller SSP coeﬃcient than those in [27, 30]. However, converting the methods in [29] to our form we were able to replicate their results while tightening the optimizer parameters TolCon, TolFun and TolX from 10−12 in their work to 10−14.


- 4.2.8 Ninth order methods

Explicit two-step RK methods with positive SSP coeﬃcient and order nine cannot exist [22]. For orders higher than eight, ﬁnding practical multistep or Runge–Kutta methods is a challenge even when the SSP property is not required. Numerical optimization of such high order MSRK methods is computationally intensive, so we have restricted our search to a few combinations of stage and step number. We are able to break the order barrier of the two step methods by ﬁnding a (s, k) = (10, 3) method. Investigating methods with four steps, we obtain a (s, k) = (8, 4) method with Ceﬀ = 0.1276, and a (s, k) = (9, 4) method with Ceﬀ = 0.1766. We also found a (9, 5) method with Ceﬀ = 0.1883. By comparison, a multistep method requires 23 steps for Ceﬀ = 0.116 and 28 steps for Ceﬀ = 0.175. These methods also compare favorably to the (s, k) = (8, 5) method in [29], that has Ceﬀ = 0.153. However, based on our experience with eighth order methods we do not claim that our new methods are optimal.

- 4.2.9 Tenth order methods


The search for tenth order methods is complicated by the large number of constraints and the large number of steps and stages required, and so we did not pursue optimization of these methods in general. However, we obtained an (s, k) = (20, 3) with Ceﬀ = 0.0917 which demonstrates that 3-step methods with order 10 exist. We also obtained a (k, s) = (8, 6) method with Ceﬀ = 0.839. Once again, we do not claim that this methods are optimal. While these method have small eﬀective coeﬃcients, they demonstrate that it is possible to ﬁnd tenth order SSP methods with much less than the 22 steps required for linear multistep methods. For comparison, the optimal multistep method with 22 steps and order 10 has Ceﬀ = 0.10 [13].

## 5 Numerical Results

In this section we present numerical tests of the optimized MSRK methods identiﬁed above. The numerical tests have three purposes: (1) to verify that the methods have the designed order of accuracy; (2) to demonstrate the value of high order time-stepping methods when using high-order

spatial discretizations; and (3) to study the strong stability properties of the newly designed MSRK methods in practice, on test cases for which the forward Euler method is known to be total variation diminishing or positivity preserving. The scripts for many of these tests can be found at [10].

- 5.1 Order Veriﬁcation Convergence studies for ordinary diﬀerential equations were performed using the van der Pol oscillator, a nonlinear system, to conﬁrm the design orders of the methods. As these methods were designed for use as time integrators for partial diﬀerential equations, we include a convergence study for a PDE with high order spatial discretization. The van der Pol oscillator problem. The van der Pol problem is:


u′1 = u2 (34)

u′2 = 1ǫ(−u1 + (1 − u21)u2) (35) We use ǫ = 10 and initial conditions u0 = (0.5; 0). This was run to ﬁnal time Tfinal = 4.0, with ∆t =

![image 531](<2013-bresten-explicit-strong-stability-preserving_images/imageFile531.png>)

Tfinal

N−1 where N = 15, 19, 23, 27, 31, 35, 39, 43. Starting values and exact solution (for error calculation) were calculated by the highly accurate MATLAB ODE45 routine with tolerances set to 10−14. In Figure 2(a) we show the convergence of the selected (s, k, p) = (6, 3, 4), (7, 4, 5), (8, 3, 6), (8, 3, 7),(9, 4, 8), and (9, 4, 9) methods for u1. Due to space limitations, we present only the results for a few methods,

![image 532](<2013-bresten-explicit-strong-stability-preserving_images/imageFile532.png>)

−4

−3

−5

−4

−6

−5

−7

−6

−8

log10(error)

log10(error)

−9

−7

−10

−8

−11

−9

−12

- 6s3k4p slope=3.73

- 7s4k5p slope=4.92

- 8s3k6p slope=5.73

- 8s3k7p slope=7.12

- 9s4k8p slope=8.25


- 9s4k9p slope=8.98


−10

|6s3k4p slope=4.18<br><br>7s4k5p slope=5.13<br><br>8s3k6p slope=6.28<br><br>8s4k7p slope=7.27<br><br>9s4k8p slope=8.35<br><br><br>9s4k9p slope=9.3<br><br><br>|
|---|


−13

−11

−14

−12

−15

−13

1.1 1.2 1.3 1.4 1.5 1.6

1.1 1.2 1.3 1.4 1.5 1.6

log10(N)

log10(N)

(a) van der Pol

(b) linear advection

Figure 2: Order veriﬁcation of multistep Runge–Kutta methods on ordinary diﬀerential equations (left) and partial diﬀerential equation (right).

one of each order up to p = 9. The new multistep Runge–Kutta methods exhibit the correct order of accuracy.

Linear advection with a Fourier spectral method. For the PDE convergence test, we chose the Fourier spectral method on the advection equation with sine wave initial conditions and periodic boundaries:

ut = −ux x ∈ [0, 1] (36) u(0, x) = sin(4πx) u(t, 0) = u(t, 1)

The exact solution to this problem is a sine wave with period 4 that travels in time. Due to the periodicity of the exact solution, the Fourier spectral method gives us an exact solution in space [15] once we have two points per wavelength, allowing us to isolate the eﬀect of the temporal discretization on the error. We run this problem with N = (11, 15, 21, 25, 31, 35, 41, 45) to Tfinal = 1 with ∆t = 0.4∆x, where ∆x = N1−1. For each multi-step Runge–Kutta method of order p we generated the k − 1 initial values using the third order Shu-Osher SSP Runge–Kutta method with a very small time-step ∆tp/3. Errors are computed at the ﬁnal time, compared to the exact solution. Figure 2(b) contains the l2 norm of the errors, and demonstrates that the methods achieved the expected convergence rates.

![image 533](<2013-bresten-explicit-strong-stability-preserving_images/imageFile533.png>)

### 5.2 Beneﬁts of high order time discretizations

High-order spatial discretizations for hyperbolic PDEs have usually been paired with lower-order time discretizations; e.g. [2, 3, 4, 6, 7, 19, 24, 31, 36]. Although spatial truncation errors are often observed to be larger than temporal errors in practice, this discrepancy can lead to loss of accuracy unless the time-step is signiﬁcantly reduced. If the order of the timestepping method is p1 and the order of the spatial method is p2 then asymptotic convergence

0

−1

−2

−3

log(error)

−4

|5s3k3p<br><br>6s3k4p<br><br>7s3k5p<br><br>8s3k6p<br><br>9s3k7p<br><br>10s3k8p<br><br><br>|
|---|


−5

−6

- at rate p2 is assured only if ∆t = O(∆xp


2/p1). For hyperbolic PDEs, one typically wishes to take ∆t = O(∆x) for accuracy reasons.

−7

−8

1 1.2 1.4 1.6 1.8 2

log(N)

In the following example we solve the twodimensional advection equation

Figure 3: Convergence of a 2D advection equation with 9th order WENO in space and MSRK in time.

ut + ux + uy = 0

over the unit square with periodic boundary conditions in each direction and initial data u(0, x) = sin(2π(x + y)). We take ∆x = ∆y = N1−1. We solve for 0 ≤ t ≤ 81 with ∆t = 14∆x. We use

![image 534](<2013-bresten-explicit-strong-stability-preserving_images/imageFile534.png>)

![image 535](<2013-bresten-explicit-strong-stability-preserving_images/imageFile535.png>)

![image 536](<2013-bresten-explicit-strong-stability-preserving_images/imageFile536.png>)

ninth-order WENO ﬁnite diﬀerences in space. For each multi-step Runge–Kutta method of order p we generated the k − 1 initial values using the third order Shu-Osher SSP Runge–Kutta method with a very small time-step ∆tp/3. Figure 3 shows the accuracy of several of our high order multistep Runge–Kutta methods applied to this problem. Observe that while methods of order p ≤ 6 exhibit an asymptotic convergence rate of less than 9th order, our newly found methods of order p ≥ 7 allow the high order behavior of the WENO to become apparent.

### 5.3 Strong stability performance of the new MSRK methods

In this section we discuss the strong stability performance of the new methods in practice. The SSP condition is a very general condition: it holds for any convex functional and any starting value, for arbitrary nonlinear non-autonomous equations, assuming only that the forward Euler method satisﬁes the corresponding monotonicity condition. In other words, it is a bound based on the worst-case behavior. Hence it should not be surprising that larger step sizes are possible when one considers a particular problem and a particular convex functional.

Here we explore the behavior of these methods in practice on the linear advection and nonlinear Buckley-Leverett equations, looking only at the total variation and positivity properties. The scripts for these tests can be found at [10].

- Example 1: Advection. Our ﬁrst example is the advection equation with a step function initial condition:

ut + ux = 0 u(0, x) =

1, if 0 ≤ x ≤ 1/2 0, if x > 1/2

on the domain [0, 1) with periodic boundary conditions. The problem was semi-discretized using a ﬁrst-order forward diﬀerence on a grid with N = 101 points and evolved to a ﬁnal time of t = 18. We used the exact solution for the k−1 initial values. Euler’s method is TVD and positive for step sizes up to ∆tFE = ∆x. Table 8 shows the normalized observed time step ∆t

![image 537](<2013-bresten-explicit-strong-stability-preserving_images/imageFile537.png>)

TV D

![image 538](<2013-bresten-explicit-strong-stability-preserving_images/imageFile538.png>)

∆x for which each method

maintains the total variation diminishing property and the observed time step ∆∆tx+ for which each method maintains positivity. We compare these values to the normalized time-step guaranteed by

![image 539](<2013-bresten-explicit-strong-stability-preserving_images/imageFile539.png>)

the theory, C∆t

FE

![image 540](<2013-bresten-explicit-strong-stability-preserving_images/imageFile540.png>)

∆x . The table also compares the eﬀective observed TVD time-step 1s ∆t

![image 541](<2013-bresten-explicit-strong-stability-preserving_images/imageFile541.png>)

TV D

![image 542](<2013-bresten-explicit-strong-stability-preserving_images/imageFile542.png>)

∆x , and the eﬀective positivity time step 1s ∆∆tx+, with the eﬀective time-step given by the theory Ceﬀ∆t

![image 543](<2013-bresten-explicit-strong-stability-preserving_images/imageFile543.png>)

![image 544](<2013-bresten-explicit-strong-stability-preserving_images/imageFile544.png>)

FE

![image 545](<2013-bresten-explicit-strong-stability-preserving_images/imageFile545.png>)

∆x . These examples conﬁrm that the observed positivity preserving time-step correlates well with the size of the SSP coeﬃcient, and these methods compare favorably with the baseline methods. Also, the methods perform in practice as well or better than the lower bound guaranteed by the theory.

- Example 2: Buckley-Leverett Problem: We solve the Buckley-Leverett equation, a nonlinear


![image 546](<2013-bresten-explicit-strong-stability-preserving_images/imageFile546.png>)

method ∆t∆TVxD 1s ∆t∆TVxD C∆∆tFEx Ceﬀ∆∆tFEx ∆∆tx+ 1s ∆∆tx+ SSPRK 3,3 1.000 0.333 1.000 0.333 1.028 0.342

![image 547](<2013-bresten-explicit-strong-stability-preserving_images/imageFile547.png>)

![image 548](<2013-bresten-explicit-strong-stability-preserving_images/imageFile548.png>)

![image 549](<2013-bresten-explicit-strong-stability-preserving_images/imageFile549.png>)

![image 550](<2013-bresten-explicit-strong-stability-preserving_images/imageFile550.png>)

![image 551](<2013-bresten-explicit-strong-stability-preserving_images/imageFile551.png>)

![image 552](<2013-bresten-explicit-strong-stability-preserving_images/imageFile552.png>)

![image 553](<2013-bresten-explicit-strong-stability-preserving_images/imageFile553.png>)

![image 554](<2013-bresten-explicit-strong-stability-preserving_images/imageFile554.png>)

![image 555](<2013-bresten-explicit-strong-stability-preserving_images/imageFile555.png>)

![image 556](<2013-bresten-explicit-strong-stability-preserving_images/imageFile556.png>)

![image 557](<2013-bresten-explicit-strong-stability-preserving_images/imageFile557.png>)

![image 558](<2013-bresten-explicit-strong-stability-preserving_images/imageFile558.png>)

![image 559](<2013-bresten-explicit-strong-stability-preserving_images/imageFile559.png>)

![image 560](<2013-bresten-explicit-strong-stability-preserving_images/imageFile560.png>)

![image 561](<2013-bresten-explicit-strong-stability-preserving_images/imageFile561.png>)

![image 562](<2013-bresten-explicit-strong-stability-preserving_images/imageFile562.png>)

![image 563](<2013-bresten-explicit-strong-stability-preserving_images/imageFile563.png>)

![image 564](<2013-bresten-explicit-strong-stability-preserving_images/imageFile564.png>)

![image 565](<2013-bresten-explicit-strong-stability-preserving_images/imageFile565.png>)

![image 566](<2013-bresten-explicit-strong-stability-preserving_images/imageFile566.png>)

- (2,3,3) 1.113 0.556 1.113 0.556 1.113 0.556

![image 567](<2013-bresten-explicit-strong-stability-preserving_images/imageFile567.png>)

![image 568](<2013-bresten-explicit-strong-stability-preserving_images/imageFile568.png>)

![image 569](<2013-bresten-explicit-strong-stability-preserving_images/imageFile569.png>)

![image 570](<2013-bresten-explicit-strong-stability-preserving_images/imageFile570.png>)

![image 571](<2013-bresten-explicit-strong-stability-preserving_images/imageFile571.png>)

- (6,3,3) 3.777 0.629 3.777 0.629 3.777 0.629

![image 572](<2013-bresten-explicit-strong-stability-preserving_images/imageFile572.png>)

![image 573](<2013-bresten-explicit-strong-stability-preserving_images/imageFile573.png>)

![image 574](<2013-bresten-explicit-strong-stability-preserving_images/imageFile574.png>)

![image 575](<2013-bresten-explicit-strong-stability-preserving_images/imageFile575.png>)

![image 576](<2013-bresten-explicit-strong-stability-preserving_images/imageFile576.png>)

- (7,3,3) 6.300 0.900 4.484 0.641 6.300 0.900


![image 577](<2013-bresten-explicit-strong-stability-preserving_images/imageFile577.png>)

![image 578](<2013-bresten-explicit-strong-stability-preserving_images/imageFile578.png>)

![image 579](<2013-bresten-explicit-strong-stability-preserving_images/imageFile579.png>)

![image 580](<2013-bresten-explicit-strong-stability-preserving_images/imageFile580.png>)

![image 581](<2013-bresten-explicit-strong-stability-preserving_images/imageFile581.png>)

![image 582](<2013-bresten-explicit-strong-stability-preserving_images/imageFile582.png>)

- (2,3,4) 0.495 0.248 0.495 0.248 0.495 0.248 (3,4,4) 1.365 0.455 1.365 0.455 1.365 0.455


![image 583](<2013-bresten-explicit-strong-stability-preserving_images/imageFile583.png>)

![image 584](<2013-bresten-explicit-strong-stability-preserving_images/imageFile584.png>)

![image 585](<2013-bresten-explicit-strong-stability-preserving_images/imageFile585.png>)

![image 586](<2013-bresten-explicit-strong-stability-preserving_images/imageFile586.png>)

![image 587](<2013-bresten-explicit-strong-stability-preserving_images/imageFile587.png>)

![image 588](<2013-bresten-explicit-strong-stability-preserving_images/imageFile588.png>)

![image 589](<2013-bresten-explicit-strong-stability-preserving_images/imageFile589.png>)

![image 590](<2013-bresten-explicit-strong-stability-preserving_images/imageFile590.png>)

![image 591](<2013-bresten-explicit-strong-stability-preserving_images/imageFile591.png>)

![image 592](<2013-bresten-explicit-strong-stability-preserving_images/imageFile592.png>)

![image 593](<2013-bresten-explicit-strong-stability-preserving_images/imageFile593.png>)

![image 594](<2013-bresten-explicit-strong-stability-preserving_images/imageFile594.png>)

![image 595](<2013-bresten-explicit-strong-stability-preserving_images/imageFile595.png>)

![image 596](<2013-bresten-explicit-strong-stability-preserving_images/imageFile596.png>)

non-SSP RK4,4 1.000 0.250 0.000 0.000 1.031 0.258 SSP RK10,4 6.00 0.600 6.000 0.600 6.032 0.603 (7,3,4) 3.749 0.536 3.749 0.536 4.001 0.572

![image 597](<2013-bresten-explicit-strong-stability-preserving_images/imageFile597.png>)

![image 598](<2013-bresten-explicit-strong-stability-preserving_images/imageFile598.png>)

![image 599](<2013-bresten-explicit-strong-stability-preserving_images/imageFile599.png>)

![image 600](<2013-bresten-explicit-strong-stability-preserving_images/imageFile600.png>)

![image 601](<2013-bresten-explicit-strong-stability-preserving_images/imageFile601.png>)

![image 602](<2013-bresten-explicit-strong-stability-preserving_images/imageFile602.png>)

![image 603](<2013-bresten-explicit-strong-stability-preserving_images/imageFile603.png>)

![image 604](<2013-bresten-explicit-strong-stability-preserving_images/imageFile604.png>)

![image 605](<2013-bresten-explicit-strong-stability-preserving_images/imageFile605.png>)

![image 606](<2013-bresten-explicit-strong-stability-preserving_images/imageFile606.png>)

![image 607](<2013-bresten-explicit-strong-stability-preserving_images/imageFile607.png>)

![image 608](<2013-bresten-explicit-strong-stability-preserving_images/imageFile608.png>)

- (3,3,5) 0.641 0.214 0.638 0.213 0.663 0.221

![image 609](<2013-bresten-explicit-strong-stability-preserving_images/imageFile609.png>)

![image 610](<2013-bresten-explicit-strong-stability-preserving_images/imageFile610.png>)

![image 611](<2013-bresten-explicit-strong-stability-preserving_images/imageFile611.png>)

![image 612](<2013-bresten-explicit-strong-stability-preserving_images/imageFile612.png>)

![image 613](<2013-bresten-explicit-strong-stability-preserving_images/imageFile613.png>)

- (3,4,5) 1.001 0.334 1.001 0.334 1.001 0.334

![image 614](<2013-bresten-explicit-strong-stability-preserving_images/imageFile614.png>)

![image 615](<2013-bresten-explicit-strong-stability-preserving_images/imageFile615.png>)

![image 616](<2013-bresten-explicit-strong-stability-preserving_images/imageFile616.png>)

![image 617](<2013-bresten-explicit-strong-stability-preserving_images/imageFile617.png>)

![image 618](<2013-bresten-explicit-strong-stability-preserving_images/imageFile618.png>)

- (3,5,5) 1.162 0.387 1.162 0.387 1.162 0.387

![image 619](<2013-bresten-explicit-strong-stability-preserving_images/imageFile619.png>)

![image 620](<2013-bresten-explicit-strong-stability-preserving_images/imageFile620.png>)

![image 621](<2013-bresten-explicit-strong-stability-preserving_images/imageFile621.png>)

![image 622](<2013-bresten-explicit-strong-stability-preserving_images/imageFile622.png>)

![image 623](<2013-bresten-explicit-strong-stability-preserving_images/imageFile623.png>)

- (6,3,5) 2.423 0.404 2.423 0.404 2.423 0.404

![image 624](<2013-bresten-explicit-strong-stability-preserving_images/imageFile624.png>)

![image 625](<2013-bresten-explicit-strong-stability-preserving_images/imageFile625.png>)

![image 626](<2013-bresten-explicit-strong-stability-preserving_images/imageFile626.png>)

![image 627](<2013-bresten-explicit-strong-stability-preserving_images/imageFile627.png>)

![image 628](<2013-bresten-explicit-strong-stability-preserving_images/imageFile628.png>)

![image 629](<2013-bresten-explicit-strong-stability-preserving_images/imageFile629.png>)

- (3,5,6) 0.657 0.219 0.657 0.219 0.657 0.219

![image 630](<2013-bresten-explicit-strong-stability-preserving_images/imageFile630.png>)

![image 631](<2013-bresten-explicit-strong-stability-preserving_images/imageFile631.png>)

![image 632](<2013-bresten-explicit-strong-stability-preserving_images/imageFile632.png>)

![image 633](<2013-bresten-explicit-strong-stability-preserving_images/imageFile633.png>)

![image 634](<2013-bresten-explicit-strong-stability-preserving_images/imageFile634.png>)

- (4,4,6) 0.985 0.246 0.971 0.243 0.985 0.246

![image 635](<2013-bresten-explicit-strong-stability-preserving_images/imageFile635.png>)

![image 636](<2013-bresten-explicit-strong-stability-preserving_images/imageFile636.png>)

![image 637](<2013-bresten-explicit-strong-stability-preserving_images/imageFile637.png>)

![image 638](<2013-bresten-explicit-strong-stability-preserving_images/imageFile638.png>)

![image 639](<2013-bresten-explicit-strong-stability-preserving_images/imageFile639.png>)

- (5,3,6) 1.361 0.272 1.361 0.272 1.361 0.272

![image 640](<2013-bresten-explicit-strong-stability-preserving_images/imageFile640.png>)

![image 641](<2013-bresten-explicit-strong-stability-preserving_images/imageFile641.png>)

![image 642](<2013-bresten-explicit-strong-stability-preserving_images/imageFile642.png>)

![image 643](<2013-bresten-explicit-strong-stability-preserving_images/imageFile643.png>)

![image 644](<2013-bresten-explicit-strong-stability-preserving_images/imageFile644.png>)

- (6,5,6) 2.067 0.345 2.067 0.345 2.139 0.357

![image 645](<2013-bresten-explicit-strong-stability-preserving_images/imageFile645.png>)

![image 646](<2013-bresten-explicit-strong-stability-preserving_images/imageFile646.png>)

![image 647](<2013-bresten-explicit-strong-stability-preserving_images/imageFile647.png>)

![image 648](<2013-bresten-explicit-strong-stability-preserving_images/imageFile648.png>)

![image 649](<2013-bresten-explicit-strong-stability-preserving_images/imageFile649.png>)

- (9,3,6) 3.146 0.350 3.144 0.349 3.578 0.398 (4,5,7) 0.901 0.225 0.882 0.220 0.917 0.229

![image 650](<2013-bresten-explicit-strong-stability-preserving_images/imageFile650.png>)

![image 651](<2013-bresten-explicit-strong-stability-preserving_images/imageFile651.png>)

![image 652](<2013-bresten-explicit-strong-stability-preserving_images/imageFile652.png>)

![image 653](<2013-bresten-explicit-strong-stability-preserving_images/imageFile653.png>)

![image 654](<2013-bresten-explicit-strong-stability-preserving_images/imageFile654.png>)

![image 655](<2013-bresten-explicit-strong-stability-preserving_images/imageFile655.png>)

![image 656](<2013-bresten-explicit-strong-stability-preserving_images/imageFile656.png>)

![image 657](<2013-bresten-explicit-strong-stability-preserving_images/imageFile657.png>)

![image 658](<2013-bresten-explicit-strong-stability-preserving_images/imageFile658.png>)

![image 659](<2013-bresten-explicit-strong-stability-preserving_images/imageFile659.png>)

![image 660](<2013-bresten-explicit-strong-stability-preserving_images/imageFile660.png>)

(7,3,7) 1.699 0.243 1.699 0.243 1.699 0.243 (7,4,7) 1.999 0.286 1.999 0.286 1.999 0.286 (8,3,8) 0.898 0.112 0.799 0.100 0.898 0.112 (9,5,8) 2.058 0.229 2.058 0.229 2.222 0.247

![image 661](<2013-bresten-explicit-strong-stability-preserving_images/imageFile661.png>)

![image 662](<2013-bresten-explicit-strong-stability-preserving_images/imageFile662.png>)

![image 663](<2013-bresten-explicit-strong-stability-preserving_images/imageFile663.png>)

![image 664](<2013-bresten-explicit-strong-stability-preserving_images/imageFile664.png>)

![image 665](<2013-bresten-explicit-strong-stability-preserving_images/imageFile665.png>)

![image 666](<2013-bresten-explicit-strong-stability-preserving_images/imageFile666.png>)

![image 667](<2013-bresten-explicit-strong-stability-preserving_images/imageFile667.png>)

![image 668](<2013-bresten-explicit-strong-stability-preserving_images/imageFile668.png>)

![image 669](<2013-bresten-explicit-strong-stability-preserving_images/imageFile669.png>)

![image 670](<2013-bresten-explicit-strong-stability-preserving_images/imageFile670.png>)

![image 671](<2013-bresten-explicit-strong-stability-preserving_images/imageFile671.png>)

![image 672](<2013-bresten-explicit-strong-stability-preserving_images/imageFile672.png>)

![image 673](<2013-bresten-explicit-strong-stability-preserving_images/imageFile673.png>)

![image 674](<2013-bresten-explicit-strong-stability-preserving_images/imageFile674.png>)

![image 675](<2013-bresten-explicit-strong-stability-preserving_images/imageFile675.png>)

![image 676](<2013-bresten-explicit-strong-stability-preserving_images/imageFile676.png>)

![image 677](<2013-bresten-explicit-strong-stability-preserving_images/imageFile677.png>)

![image 678](<2013-bresten-explicit-strong-stability-preserving_images/imageFile678.png>)

![image 679](<2013-bresten-explicit-strong-stability-preserving_images/imageFile679.png>)

![image 680](<2013-bresten-explicit-strong-stability-preserving_images/imageFile680.png>)

![image 681](<2013-bresten-explicit-strong-stability-preserving_images/imageFile681.png>)

![image 682](<2013-bresten-explicit-strong-stability-preserving_images/imageFile682.png>)

- (9,4,9) 1.638 0.182 1.590 0.177 1.672 0.186






![image 683](<2013-bresten-explicit-strong-stability-preserving_images/imageFile683.png>)

![image 684](<2013-bresten-explicit-strong-stability-preserving_images/imageFile684.png>)

![image 685](<2013-bresten-explicit-strong-stability-preserving_images/imageFile685.png>)

![image 686](<2013-bresten-explicit-strong-stability-preserving_images/imageFile686.png>)

![image 687](<2013-bresten-explicit-strong-stability-preserving_images/imageFile687.png>)

![image 688](<2013-bresten-explicit-strong-stability-preserving_images/imageFile688.png>)

![image 689](<2013-bresten-explicit-strong-stability-preserving_images/imageFile689.png>)

![image 690](<2013-bresten-explicit-strong-stability-preserving_images/imageFile690.png>)

![image 691](<2013-bresten-explicit-strong-stability-preserving_images/imageFile691.png>)

![image 692](<2013-bresten-explicit-strong-stability-preserving_images/imageFile692.png>)

(20,3,10) 2.146 0.107 1.835 0.092 2.209 0.110

![image 693](<2013-bresten-explicit-strong-stability-preserving_images/imageFile693.png>)

#### Table 8: Observed total variation diminishing (TVD) and positivity time-step and eﬀective TVD and positivity time-step (normalized by the spatial step) compared with the theoretical values for Example 1.

PDE used to model two-phase ﬂow through porous media:

u2 u2 + a(1 − u)2

ut + f(u)x = 0, where f(u) =

,

![image 694](<2013-bresten-explicit-strong-stability-preserving_images/imageFile694.png>)

on x ∈ [0, 1), with periodic boundary conditions. We take a = 31 and initial condition

![image 695](<2013-bresten-explicit-strong-stability-preserving_images/imageFile695.png>)

u(x, 0) =

1/2, if x ≥ 1/2 0, otherwise.

(37)

The problem is semi-discretized using a conservative scheme with a Koren Limiter as in [22] with ∆x = 1001 , and run to tf = 18. For this problem the theoretical TVD time-step is ∆tFE = 14∆x = 0.0025. For each multi-step Runge–Kutta method of order p we generated the k − 1 initial values using the third order Shu-Osher SSP Runge–Kutta method with a very small time-step ∆tp/3.

![image 696](<2013-bresten-explicit-strong-stability-preserving_images/imageFile696.png>)

![image 697](<2013-bresten-explicit-strong-stability-preserving_images/imageFile697.png>)

![image 698](<2013-bresten-explicit-strong-stability-preserving_images/imageFile698.png>)

0.02

0.025

0.014

0.018

0.012

0.02

0.016

0.01

0.014

0.015

0.008

0.012

0.01

0.006

0.01

0.008

0.004

0.006

|k=3 Order (Observed)<br><br>k=3 Order (Theoretical)<br><br>k=4 Order (Observed)<br><br>k=4 Order (Theoretical)<br><br>k=5 Order (Observed)<br><br><br>k=5 Order (Theoretical)<br><br><br><br><br>|
|---|


|k=3 Order (Observed)<br><br>k=3 Order (Theoretical)<br><br>k=4 Order (Observed)<br><br>k=4 Order (Theoretical)<br><br>k=5 Order (Observed)<br><br><br>k=5 Order (Theoretical)<br><br><br><br><br>|
|---|


|k=3 Order (Observed)<br><br>k=3 Order (Theoretical)<br><br>k=4 Order (Observed)<br><br>k=4 Order (Theoretical)<br><br>k=5 Order (Observed)<br><br><br>k=5 Order (Theoretical)<br><br><br><br><br>|
|---|


0.005

0.002

0.004

0.002

0

0

2 3 4 5 6 7 8 9 10

2 3 4 5 6 7 8 9 10

3 4 5 6 7 8 9 10

(a) Third order methods

(b) Fourth order methods

(c) Fifth order methods

0.012

0.01

0.012

0.009

0.01

0.01

0.008

0.007

0.008

0.008

0.006

0.006

0.005

0.006

0.004

0.004

0.004

0.003

|k=3 Order (Observed)<br><br>k=3 Order (Theoretical)<br><br>k=4 Order (Observed)<br><br>k=4 Order (Theoretical)<br><br>k=5 Order (Observed)<br><br><br>k=5 Order (Theoretical)<br><br><br><br><br>|
|---|


|k=3 Order (Observed)<br><br>k=3 Order (Theoretical)<br><br>k=4 Order (Observed)<br><br>k=4 Order (Theoretical)<br><br>k=5 Order (Observed)<br><br><br>k=5 Order (Theoretical)<br><br><br><br><br>|
|---|


|k=3 Order (Observed)<br><br>k=3 Order (Theoretical)<br><br>k=4 Order (Observed)<br><br>k=4 Order (Theoretical)<br><br>k=5 Order (Observed)<br><br><br>k=5 Order (Theoretical)<br><br><br><br><br>|
|---|


0.002

0.002

0.002

0.001

0

0

0

3 4 5 6 7 8 9 10

3 4 5 6 7 8 9 10

5 5.5 6 6.5 7 7.5 8 8.5 9 9.5 10

(d) Sixth order methods

(e) Seventh order methods

(f) Eighth order methods

Figure 4: The observed normalized TVD time-step (∆t/∆x) compared to the theoretical for multistep Runge–Kutta methods of order p = 3, ..., 8 using Example 2.

The plots in Figure 4 show the observed normalized timestep for TVD (∆t/∆x) for the number of stages, for each family of k-step methods. The dotted lines are the corresponding theoretical TVD time-step for these methods. We see that the observed values are signiﬁcantly higher than the theoretical values, but the observed values generally increase with the number of stages as predicted. In Table 9 we compare the positivity preserving time-step to the TVD time-step. We note that the TVD time step is always smaller than the positivity time-step, demonstrating the dependence of the observed time-step on the particular property desired.

![image 699](<2013-bresten-explicit-strong-stability-preserving_images/imageFile699.png>)

method ∆4∆tTVxD ∆4∆t+x (3,1,3) 0.114 0.226

![image 700](<2013-bresten-explicit-strong-stability-preserving_images/imageFile700.png>)

![image 701](<2013-bresten-explicit-strong-stability-preserving_images/imageFile701.png>)

![image 702](<2013-bresten-explicit-strong-stability-preserving_images/imageFile702.png>)

![image 703](<2013-bresten-explicit-strong-stability-preserving_images/imageFile703.png>)

![image 704](<2013-bresten-explicit-strong-stability-preserving_images/imageFile704.png>)

![image 705](<2013-bresten-explicit-strong-stability-preserving_images/imageFile705.png>)

![image 706](<2013-bresten-explicit-strong-stability-preserving_images/imageFile706.png>)

![image 707](<2013-bresten-explicit-strong-stability-preserving_images/imageFile707.png>)

![image 708](<2013-bresten-explicit-strong-stability-preserving_images/imageFile708.png>)

![image 709](<2013-bresten-explicit-strong-stability-preserving_images/imageFile709.png>)

- (3,3,3) 0.133 0.235

![image 710](<2013-bresten-explicit-strong-stability-preserving_images/imageFile710.png>)

![image 711](<2013-bresten-explicit-strong-stability-preserving_images/imageFile711.png>)

![image 712](<2013-bresten-explicit-strong-stability-preserving_images/imageFile712.png>)

- (6,3,3) 0.254 0.621

![image 713](<2013-bresten-explicit-strong-stability-preserving_images/imageFile713.png>)

![image 714](<2013-bresten-explicit-strong-stability-preserving_images/imageFile714.png>)

![image 715](<2013-bresten-explicit-strong-stability-preserving_images/imageFile715.png>)

![image 716](<2013-bresten-explicit-strong-stability-preserving_images/imageFile716.png>)

(4,1,4) 0.185 0.302 (10,1,4) 0.419 0.754

![image 717](<2013-bresten-explicit-strong-stability-preserving_images/imageFile717.png>)

![image 718](<2013-bresten-explicit-strong-stability-preserving_images/imageFile718.png>)

![image 719](<2013-bresten-explicit-strong-stability-preserving_images/imageFile719.png>)

![image 720](<2013-bresten-explicit-strong-stability-preserving_images/imageFile720.png>)

![image 721](<2013-bresten-explicit-strong-stability-preserving_images/imageFile721.png>)

![image 722](<2013-bresten-explicit-strong-stability-preserving_images/imageFile722.png>)

- (2,3,4) 0.044 0.089

![image 723](<2013-bresten-explicit-strong-stability-preserving_images/imageFile723.png>)

![image 724](<2013-bresten-explicit-strong-stability-preserving_images/imageFile724.png>)

![image 725](<2013-bresten-explicit-strong-stability-preserving_images/imageFile725.png>)

- (3,4,4) 0.106 0.179

![image 726](<2013-bresten-explicit-strong-stability-preserving_images/imageFile726.png>)

![image 727](<2013-bresten-explicit-strong-stability-preserving_images/imageFile727.png>)

![image 728](<2013-bresten-explicit-strong-stability-preserving_images/imageFile728.png>)

(7,3,4) 0.298 0.565

![image 729](<2013-bresten-explicit-strong-stability-preserving_images/imageFile729.png>)

![image 730](<2013-bresten-explicit-strong-stability-preserving_images/imageFile730.png>)

![image 731](<2013-bresten-explicit-strong-stability-preserving_images/imageFile731.png>)

![image 732](<2013-bresten-explicit-strong-stability-preserving_images/imageFile732.png>)

- (3,3,5) 0.087 0.175

![image 733](<2013-bresten-explicit-strong-stability-preserving_images/imageFile733.png>)

![image 734](<2013-bresten-explicit-strong-stability-preserving_images/imageFile734.png>)

![image 735](<2013-bresten-explicit-strong-stability-preserving_images/imageFile735.png>)

- (6,3,5) 0.190 0.375

![image 736](<2013-bresten-explicit-strong-stability-preserving_images/imageFile736.png>)

![image 737](<2013-bresten-explicit-strong-stability-preserving_images/imageFile737.png>)

![image 738](<2013-bresten-explicit-strong-stability-preserving_images/imageFile738.png>)

(3,4,5) 0.086 0.173 (3,5,5) 0.085 0.195 (5,3,6) 0.131 0.262 (9,3,6) 0.255 0.501 (4,4,6) 0.090 0.191

![image 739](<2013-bresten-explicit-strong-stability-preserving_images/imageFile739.png>)

![image 740](<2013-bresten-explicit-strong-stability-preserving_images/imageFile740.png>)

![image 741](<2013-bresten-explicit-strong-stability-preserving_images/imageFile741.png>)

![image 742](<2013-bresten-explicit-strong-stability-preserving_images/imageFile742.png>)

![image 743](<2013-bresten-explicit-strong-stability-preserving_images/imageFile743.png>)

![image 744](<2013-bresten-explicit-strong-stability-preserving_images/imageFile744.png>)

![image 745](<2013-bresten-explicit-strong-stability-preserving_images/imageFile745.png>)

![image 746](<2013-bresten-explicit-strong-stability-preserving_images/imageFile746.png>)

![image 747](<2013-bresten-explicit-strong-stability-preserving_images/imageFile747.png>)

![image 748](<2013-bresten-explicit-strong-stability-preserving_images/imageFile748.png>)

![image 749](<2013-bresten-explicit-strong-stability-preserving_images/imageFile749.png>)

![image 750](<2013-bresten-explicit-strong-stability-preserving_images/imageFile750.png>)

![image 751](<2013-bresten-explicit-strong-stability-preserving_images/imageFile751.png>)

![image 752](<2013-bresten-explicit-strong-stability-preserving_images/imageFile752.png>)

![image 753](<2013-bresten-explicit-strong-stability-preserving_images/imageFile753.png>)

![image 754](<2013-bresten-explicit-strong-stability-preserving_images/imageFile754.png>)

- (3,5,6) 0.057 0.117

![image 755](<2013-bresten-explicit-strong-stability-preserving_images/imageFile755.png>)

![image 756](<2013-bresten-explicit-strong-stability-preserving_images/imageFile756.png>)

![image 757](<2013-bresten-explicit-strong-stability-preserving_images/imageFile757.png>)

(6,5,6) 0.160 0.349 (7,3,7) 0.148 0.286 (8,3,7) 0.183 0.346 (7,4,7) 0.167 0.353

![image 758](<2013-bresten-explicit-strong-stability-preserving_images/imageFile758.png>)

![image 759](<2013-bresten-explicit-strong-stability-preserving_images/imageFile759.png>)

![image 760](<2013-bresten-explicit-strong-stability-preserving_images/imageFile760.png>)

![image 761](<2013-bresten-explicit-strong-stability-preserving_images/imageFile761.png>)

![image 762](<2013-bresten-explicit-strong-stability-preserving_images/imageFile762.png>)

![image 763](<2013-bresten-explicit-strong-stability-preserving_images/imageFile763.png>)

![image 764](<2013-bresten-explicit-strong-stability-preserving_images/imageFile764.png>)

![image 765](<2013-bresten-explicit-strong-stability-preserving_images/imageFile765.png>)

![image 766](<2013-bresten-explicit-strong-stability-preserving_images/imageFile766.png>)

![image 767](<2013-bresten-explicit-strong-stability-preserving_images/imageFile767.png>)

![image 768](<2013-bresten-explicit-strong-stability-preserving_images/imageFile768.png>)

![image 769](<2013-bresten-explicit-strong-stability-preserving_images/imageFile769.png>)

![image 770](<2013-bresten-explicit-strong-stability-preserving_images/imageFile770.png>)

- (4,5,7) 0.085 0.172


- (8,3,8) 0.168 0.353

![image 771](<2013-bresten-explicit-strong-stability-preserving_images/imageFile771.png>)

![image 772](<2013-bresten-explicit-strong-stability-preserving_images/imageFile772.png>)

![image 773](<2013-bresten-explicit-strong-stability-preserving_images/imageFile773.png>)

(6,4,8) 0.086 0.195 (6,5,8) 0.124 0.256

![image 774](<2013-bresten-explicit-strong-stability-preserving_images/imageFile774.png>)

![image 775](<2013-bresten-explicit-strong-stability-preserving_images/imageFile775.png>)

![image 776](<2013-bresten-explicit-strong-stability-preserving_images/imageFile776.png>)

![image 777](<2013-bresten-explicit-strong-stability-preserving_images/imageFile777.png>)

![image 778](<2013-bresten-explicit-strong-stability-preserving_images/imageFile778.png>)

![image 779](<2013-bresten-explicit-strong-stability-preserving_images/imageFile779.png>)

- (9,5,8) 0.172 0.348








- (9,4,9) 0.166 0.360


![image 780](<2013-bresten-explicit-strong-stability-preserving_images/imageFile780.png>)

![image 781](<2013-bresten-explicit-strong-stability-preserving_images/imageFile781.png>)

![image 782](<2013-bresten-explicit-strong-stability-preserving_images/imageFile782.png>)

![image 783](<2013-bresten-explicit-strong-stability-preserving_images/imageFile783.png>)

![image 784](<2013-bresten-explicit-strong-stability-preserving_images/imageFile784.png>)

![image 785](<2013-bresten-explicit-strong-stability-preserving_images/imageFile785.png>)

![image 786](<2013-bresten-explicit-strong-stability-preserving_images/imageFile786.png>)

![image 787](<2013-bresten-explicit-strong-stability-preserving_images/imageFile787.png>)

![image 788](<2013-bresten-explicit-strong-stability-preserving_images/imageFile788.png>)

![image 789](<2013-bresten-explicit-strong-stability-preserving_images/imageFile789.png>)

![image 790](<2013-bresten-explicit-strong-stability-preserving_images/imageFile790.png>)

![image 791](<2013-bresten-explicit-strong-stability-preserving_images/imageFile791.png>)

![image 792](<2013-bresten-explicit-strong-stability-preserving_images/imageFile792.png>)

![image 793](<2013-bresten-explicit-strong-stability-preserving_images/imageFile793.png>)

(20,3,10) 0.356 0.630

Table 9: Observed positivity preserving normalized time-step compared with the TVD normalized time-step for Example 2.

Acknowledgment. This publication is based on work supported by Award No. FIC/2010/05 2000000231, made by King Abdullah University of Science and Technology (KAUST) and on AFOSR grant FA-9550-12-1-0224.

## References

- [1] P. Albrecht, The Runge–Kutta theory in a nutshell, SIAM Journal on Numerical Analysis, 33 (1996), pp. 1712–1735.
- [2] J. Carrillo, I. M. Gamba, A. Majorana, and C.-W. Shu, A WENO-solver for the transients of Boltzmann–Poisson system for semiconductor devices: performance and comparisons with Monte Carlo methods, Journal of Computational Physics, 184 (2003), pp. 498–525.
- [3] L.-T. Cheng, H. Liu, and S. Osher, Computational high-frequency wave propagation using the level set method, with applications to the semi-classical limit of Schrödinger equations, Comm. Math. Sci., 1 (2003), pp. 593–621.
- [4] V. Cheruvu, R. D. Nair, and H. M. Turfo, A spectral ﬁnite volume transport scheme on the cubed-sphere, Applied Numerical Mathematics, 57 (2007), pp. 1021–1032.
- [5] E. Constantinescu and A. Sandu, Optimal explicit strong-stability-preserving general linear methods, SIAM Journal on Scientiﬁc Computing, 32 (2009), pp. 3130–3150.
- [6] D. Enright, R. Fedkiw, J. Ferziger, and I. Mitchell, A hybrid particle level set method for improved interface capturing, Journal of Computational Physics, 183 (2002), pp. 83–116.
- [7] L. Feng, C. Shu, and M. Zhang, A hybrid cosmological hydrodynamic/N-body code based on a weighted essentially nonoscillatory scheme, The Astrophysical Journal, 612 (2004), pp. 1–13.
- [8] L. Ferracina and M. N. Spijker, Stepsize restrictions for the total-variation-diminishing property in general Runge–Kutta methods, SIAM Journal of Numerical Analysis, 42 (2004), pp. 1073–1093.
- [9] , An extension and analysis of the Shu–Osher representation of Runge–Kutta methods, Mathematics of Computation, 249 (2005), pp. 201–219.

![image 794](<2013-bresten-explicit-strong-stability-preserving_images/imageFile794.png>)

- [10] S. Gottlieb and D. Higgs, Strong stability preserving tools test suite. http://sspsite.org/ssp_tools/.
- [11] S. Gottlieb, D. Higgs, and D. I. Ketcheson, Strong stability preserving site. http:www.sspsite.org/msrk.html.
- [12] S. Gottlieb, D. I. Ketcheson, and C.-W. Shu, High Order Strong Stability Preserving Time Discretizations, Journal of Scientiﬁc Computing, 38 (2009), pp. 251–289.


- [13] , Strong Stability Preserving Runge–Kutta and Multistep Time Discretizations, World Scientiﬁc Press, 2011.

![image 795](<2013-bresten-explicit-strong-stability-preserving_images/imageFile795.png>)

- [14] S. Gottlieb, C.-W. Shu, and E. Tadmor, Strong Stability Preserving High-Order Time Discretization Methods, SIAM Review, 43 (2001), pp. 89–112.
- [15] J. Hesthaven, S. Gottlieb, and D. Gottlieb, Spectral methods for time dependent problems, Cambridge Monographs of Applied and Computational Mathematics, Cambridge University Press, 2007.
- [16] I. Higueras, On strong stability preserving time discretization methods, Journal of Scientiﬁc Computing, 21 (2004), pp. 193–223.
- [17] , Representations of Runge–Kutta methods and strong stability preserving methods, SIAM Journal On Numerical Analysis, 43 (2005), pp. 924–948.

![image 796](<2013-bresten-explicit-strong-stability-preserving_images/imageFile796.png>)

- [18] C. Huang, Strong stability preserving hybrid methods, Applied Numerical Mathematics, 59

(2009), pp. 891–904.

- [19] S. Jin, H. Liu, S. Osher, and Y.-H. R. Tsai, Computing multivalued physical observables for the semiclassical limit of the Schrödinger equation, Journal of Computational Physics, 205

(2005), pp. 222–241.

- [20] D. I. Ketcheson, Highly eﬃcient strong stability preserving Runge–Kutta methods with lowstorage implementations, SIAM Journal on Scientiﬁc Computing, 30 (2008), pp. 2113–2136.
- [21] D. I. Ketcheson, Computation of optimal monotonicity preserving general linear methods, Mathematics of Computation, 78 (2009), pp. 1497–1513.
- [22] D. I. Ketcheson, S. Gottlieb, and C. B. Macdonald, Strong stability preserving twostep runge-kutta methods, SIAM Journal on Numerical Analysis, (2012), pp. 2618–2639.
- [23] J. F. B. M. Kraaijevanger, Contractivity of Runge–Kutta methods, BIT, 31 (1991), pp. 482– 528.
- [24] S. Labrunie, J. Carrillo, and P. Bertrand, Numerical study on hydrodynamic and quasineutral approximations for collisionless two-species plasmas, Journal of Computational Physics, 200 (2004), pp. 267–298.
- [25] H. W. J. Lenferink, Contractivity-preserving explicit linear multistep methods, Numerische Mathematik, 55 (1989), pp. 213–223.


- [26] T. Nguyen-Ba, H. Nguyen-Thu, T. Giordano, and R. Vaillancourt, Strong-stabilitypreserving 3-stage Hermite-Birkhoﬀ time-discretization methods, Appl. Numer. Math., 61

(2011), pp. 487–500.

- [27] T. Nguyen-Ba, H. Nguyen-Thu, T. Giordano, and R. Vaillancourt, Strong-stabilitypreserving 7-stage Hermite–Birkhoﬀ time-discretization methods, Journal of Scientiﬁc Computing, 50 (2012), pp. 63–90.
- [28] T. Nguyen-Ba, H. Nguyen-Thu, and R. Vaillancourt, Strong-stability-preserving, kstep, 5-to 10-stage, Hermite-Birkhoﬀ time-discretizations of order 12., American J. Computational Mathematics, 1 (2011), pp. 72–82.
- [29] H. Nguyen-Thu, Strong-stability-preserving Hermite-Birkhoﬀ time-discretization methods., Dissertation, University of Ottawa, Canada, (2012).
- [30] H. Nguyen-Thu and R. Nguyen-Ba, Truong Vaillancourt, Strong-stability-preserving, Hermite Birkhoﬀ time-discretization based on step methods and 8-stage explicit runge–kutta methods of order 5 and 4, Journal of Computational and Applied Mathematics, 263 (2014), pp. 45–58.
- [31] D. Peng, B. Merriman, S. Osher, H. Zhao, and M. Kang, A PDE-based fast local level set method, Journal of Computational Physics, 155 (1999), pp. 410–438.
- [32] S. J. Ruuth and R. J. Spiteri, Two barriers on strong-stability-preserving time discretization methods, Journal of Scientiﬁc Computation, 17 (2002), pp. 211–220.
- [33] C.-W. Shu, Total-variation diminishing time discretizations, SIAM J. Sci. Stat. Comp., 9

(1988), pp. 1073–1084.

- [34] M. Spijker, Stepsize conditions for general monotonicity in numerical initial value problems, SIAM Journal on Numerical Analysis, 45 (2007), pp. 1226–1245.
- [35] M. N. Spijker, Contractivity in the numerical solution of initial value problems, Numerische Mathematik, 42 (1983), pp. 271–290.
- [36] M. Tanguay and T. Colonius, Progress in modeling and simulation of shock wave lithotripsy (SWL), in Fifth International Symposium on cavitation (CAV2003), 2003.


