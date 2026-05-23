---
type: source
kind: paper
title: High order strong stability preserving multi-derivative implicit and IMEX Runge--Kutta methods with asymptotic preserving properties
authors: Sigal Gottlieb, Zachary J. Grant, Jingwei Hu, Ruiwen Shu
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2102.11939v3
source_local: ../raw/2021-gottlieb-high-order-strong-stability.pdf
topic: general-knowledge
cites:
---

# arXiv:2102.11939v3[math.NA]9Aug2021

## HIGH ORDER STRONG STABILITY PRESERVING MULTI-DERIVATIVE IMPLICIT AND IMEX RUNGE–KUTTA METHODS WITH ASYMPTOTIC PRESERVING PROPERTIES

SIGAL GOTTLIEB∗, ZACHARY J. GRANT†, JINGWEI HU‡, AND RUIWEN SHU§

Abstract. In this work we present a class of high order unconditionally strong stability preserving (SSP) implicit two-derivative Runge–Kutta schemes, and SSP implicit-explicit (IMEX) multiderivative Runge–Kutta schemes where the time-step restriction is independent of the stiﬀ term. The unconditional SSP property for a method of order p > 2 is unique among SSP methods, and depends on a backward-in-time assumption on the derivative of the operator. We show that this backward derivative condition is satisﬁed in many relevant cases where SSP IMEX schemes are desired. We devise unconditionally SSP implicit Runge–Kutta schemes of order up to p = 4, and IMEX Runge– Kutta schemes of order up to p = 3. For the multi-derivative IMEX schemes, we also derive and present the order conditions, which have not appeared previously. The unconditional SSP condition ensures that these methods are positivity preserving, and we present suﬃcient conditions under which such methods are also asymptotic preserving when applied to a range of problems, including a hyperbolic relaxation system, the Broadwell model, and the Bhatnagar-Gross-Krook (BGK) kinetic equation. We present numerical results to support the theoretical results, on a variety of problems.

1. Introduction. Explicit strong stability preserving (SSP) Runge–Kutta methods were ﬁrst developed for use with total variation diminishing spatial discretizations for hyperbolic conservation laws with discontinuous solutions [22, 23]. They have proven useful in a wide variety of problems where we need to evolve an ODE, as they preserve any convex functional property satisﬁed by the forward-Euler method, while giving higher order solutions. Given a system of ODEs, generally resulting from a spatial discretization of a PDE, of the form

- (1) ut = G(u) that satisﬁes some forward Euler condition

Forward Euler condition:

- (2) u + ∆tG(u) ≤ u for all ∆t ≤ ∆tFE,


where · is some convex functional (e.g. positivity). In practice, we don’t want to use Euler’s method. Instead, we desire a higher order method that preserves the forward Euler condition, perhaps under a modiﬁed time-step restriction ∆t ≤ C∆tFE. Higher order methods that can be written as convex combinations of forward Euler

∗Mathematics Department, University of Massachusetts Dartmouth, North Dartmouth, MA

02747. Email: sgottlieb@umassd.edu. SG’s research was supported in part by AFOSR Grant No. FA9550-18-1-0383.

†Multiscale Methods and Dynamics Group, Mathematics in Computation subsection, Oak Ridge National Laboratory, Oak Ridge, TN 37830. Email: grantzj@ornl.gov. This manuscript has been authored by UT-Battelle, LLC, under contract DE-AC05-00OR22725 with the US Department of Energy (DOE). The US government retains and the publisher, by accepting the article for publication, acknowledges that the US government retains a nonexclusive, paid-up, irrevocable, worldwide license to publish or reproduce the published form of this manuscript, or allow others to do so, for US government purposes. DOE will provide public access to these results of federally sponsored research in accordance with the DOE Public Access Plan (http://energy.gov/downloads/doe-public-accessplan).

‡Department of Mathematics, Purdue University, West Lafayette, IN 47907. Email: jingweihu@purdue.edu. JH’s research was supported in part by NSF CAREER grant DMS-1654152.

§Department of Mathematics, University of Maryland, College Park, MD 20742. Email: rshu@cscamm.umd.edu.

steps with C > 0 will preserve the forward Euler condition, and are called SSP. The value C is called the SSP coeﬃcient, and we generally want to devise methods that have a large C.

When concerned with linear stability properties, we turn to implicit methods, or to implicit-explicit methods, to alleviate the time-step restriction. When considering the more strict SSP property, even implicit methods suﬀer from a step-size restriction that is quite severe: the SSP coeﬃcient is usually bounded by twice the number of stages for a Runge–Kutta method [20]. This is true for all implicit methods that have been tested: Runge–Kutta, multistep methods, and general linear methods. However, by using a second operator G˜ that approximates G and satisﬁes a downwind condition

## Downwind condition:

- (3) u − ∆tG˜(u) ≤ u for all ∆t ≤ ∆tFE,

Ketcheson found a family of implicit second order methods that are unconditionally SSP [20].

In [6, 12] the SSP properties of multi-derivative Runge–Kutta methods were studied. For such methods, in addition to the forward Euler condition (2), we need some condition on the second derivative G˙ = dGdt = G G. One candidate was a second derivative condition [6]:

Second derivative condition:

- (4) u + ∆t2G˙ (u) ≤ u for all ∆t2 ≤ k˜ ∆t2FE,

where k˜ > 0. The other possibility was a Taylor series condition [12]: Taylor series condition:

- (5) u + ∆tG(u) +

- 1

- 2


∆t2G˙ (u) ≤ u for all ∆t ≤ kˆ ∆tFE,

where kˆ > 0. Previously, explicit SSP two-derivative methods were developed that preserved the forward Euler (2) and second derivative (4) conditions [6] or the forward Euler (2) and Taylor series (5) conditions [12]. However, unconditionally implicit methods that preserve the forward Euler condition (2) cannot exist [11]. Furthermore, the proof in [11] can be easily applied to the two-derivative case, to show that there are no unconditionally implicit methods that preserve (2) and (4), or (2) and (5) (see Appendix A). This leads us to consider the backward derivative condition as an alternative to (4) and (5).

To obtain unconditional SSP methods, we consider in this work a new condition on the second derivative: Backward derivative condition:

- (6) u − ∆t2G˙ (u) ≤ u for all ∆t2 ≤ k˙ ∆t2FE,


for some k˙ > 0. Under this condition, we require negative coeﬃcients on the derivative, and in this way are able to obtain unconditionally SSP two-derivative Runge–Kutta methods. In Subsection 2.2, we show the conditions under which such an implicit two derivative method is unconditionally SSP, in the sense that it preserves the strong stability condition (6) for any positive time-step ∆t. In Subsection 2.3 we proceed to present unconditionally SSP methods of this type of order up to p = 4.

After establishing that unconditionally SSP implicit two derivative Runge–Kutta methods of up to fourth order exist in Subsection 2.3, we proceed to expand the

theory in Subsection 2.2 to implicit-explicit multi-derivative Runge–Kutta methods. We devise IMEX methods that are SSP under a time-step restriction resulting only from the operator treated explicitly. We consider equations of the type

- (7) ut = F(u) + G(u),

where F and G satisfy a forward Euler condition, and G˙ satisﬁes a backward derivative condition. Here, the condition on F requires a reasonable size time-step, but the condition on G requires an inconveniently small time-step. To alleviate this restriction, we present the multi-derivative IMEX approach in Section 3, and give suﬃcient conditions under which we can ensure the method is SSP under a time-step that depends only on F. We then derive the order conditions for multi-derivative IMEX methods. In Subsection 3.3 we present our new second and third order methods. A rich area of applications is described in Subsection 3.4.1, where the backward derivative condition appears throughout.

One property that is desired in the problems presented in Subsection 3.4.1 is positivity for time-steps that depend only on F. Being SSP, the methods in Subsection 3.3 automatically preserve this positivity property. Furthermore, our methods satisfy an additional condition: that either or both G and G˙ appear in each stage. This condition is not needed for SSP (or, equivalently, positivity), but it is valuable for an additional property that is of interest: they are asymptotic preserving, as we prove in Subsection 3.4.2.

Taken together, we present unconditionally SSP – and thus positivity preserving – methods: both implicit two-derivative Runge–Kutta methods and IMEX multiderivative Runge–Kutta methods, where the time-step restriction comes from the explicit part. The IMEX methods are also asymptotic preserving, which is valuable for the problems in Subsection 3.4.1. These results are signiﬁcant, in that unconditionally SSP methods of order p > 1 are rare. We are limited only by the fact that the function and its derivative must satisfy a forward Euler (2) and backward derivative (6) conditions, respectively. While the forward Euler condition (2) seems standard, the backward derivative condition (6) seems, at ﬁrst glance, to be a bit unusual. However, there is a similarity between it and the downwinding condition (3). Furthermore, it turns out that it is a natural condition, and quite useful for a variety of problems, as we show in Subsection 3.4.1.

2. SSP implicit two-derivative Runge–Kutta methods. In this section, we consider two-derivative Runge–Kutta methods for the ODE

ut = G(u).

As discussed in [6], the two-derivative Runge–Kutta method can be written in the Butcher form

u(i) = un + ∆t

- i
- j=1


aijG(u(j)) + ∆t2

- i
- j=1


- (8a) a˙ijG˙ (u(j)), i = 1,...,s,


- (8b) un+1 = u(s). In matrix form, this becomes
- (9) U = eun + ∆tAG(U) + ∆t2A˙ G˙ (U),


where e is a vector of ones. We proceed to deﬁne the order conditions of such a method in the next subsection.

## 2.1. Formulating the order conditions. Given the Butcher form (9), the

vectors b and b˙ are given by the last row of A and A˙ , respectively. The vectors c = Ae and c˙ = Ae˙ deﬁne the time-levels at which the stages are happening; these values are known as the abscissas. The order conditions for methods of this form are given in [6] up to sixth order. We repeat them here up to fourth order.

- p = 1: bTe = 1,
- p = 2: bTc + b˙ Te = 21,

- p = 3: bTc2 + 2b˙ Tc = 31, bTAc + bTc˙ + b˙ Tc = 16,

- p = 4: bTc3 + 3b˙ Tc2 = 41, bTcAc + bTcc˙ + b˙ Tc2 + b˙ TAc + b˙ Tc˙ = 81, bTAc2 + 2bTA˙c + b˙ Tc2 = 121 , bTA2c + bTAc˙ + bTA˙c + b˙ TAc + b˙ Tc˙ = 241 .


## 2.2. Strong stability preserving properties. To ensure that a method of the

form (8) does not result in an SSP time-step restriction, we write the method in a special Shu-Osher form with only implicit computations

- i−1
- j=1


- (10a) piju(j) + ∆tdiiG(u(i)) + ∆t2d˙iiG˙ (u(i)), i = 1,...,s,


u(i) = riun +

- (10b) un+1 = u(s).

This form ensures that only implicit evaluations of G and G˙ are present, so that we do not have a time-step restriction due to a forward Euler, second derivative, or Taylor series term. The form (10) ensures that any explicit terms in the method (8) enter only after they were introduced implicitly in a prior stage. This is a necessary (but not suﬃcient) condition so that an SSP time-step restriction will not occur [10].

In matrix form, this becomes

- (11) U = Reun + PU + ∆tDG(U) + ∆t2D˙ G˙ (U),


where P and R = I − P are s × s matrices, ri are the ith row sum of R, and D and D˙ are s×s diagonal matrices. The numerical solution un+1 is then given by the ﬁnal element of the vector U. Note that the relationship between the Butcher form (9) and the Shu-Osher form (11) is given by

## A = R−1D, A˙ = R−1D˙ .

Note that given a method of the form (9), it is not always possible to select some matrix of coeﬃcients R and thus obtain matrices P, D and D˙ where the matrices D and D˙ are diagonal. (However, if A has only nonzero elements on the diagonal then it is possible). On the other hand, is always possible to start from a two derivative method of the form (11) and write it in the form (9).

A method of the form (10) will be unconditionally SSP under the following conditions:

Theorem 1. Let the operators G and G˙ satisfy the forward Euler condition

u + ∆tG(u) ≤ u for all ∆t ≤ ∆tFE and the backward derivative condition

u − ∆t2G˙ (u) ≤ u for all ∆t2 ≤ k˙ ∆t2FE,

for some ∆tFE > 0 and k˙ > 0, and for some convex functional · . A method given by (11) which satisﬁes the conditions

- (12) Re ≥ 0, P ≥ 0, D ≥ 0, D˙ ≤ 0,


(where the inequalities are understood componentwise), will preserve the strong stability property

un+1 ≤ un for any positive time-step ∆t > 0.

Proof. The ﬁrst stage of the method is given by

u(1) = un + ∆td11G(u(1)) + ∆t2d˙11G˙ (u(1)). Using the forward Euler and backward derivative conditions, we can show that u(1) ≤

un , whenever d11 ≥ 0 and d˙11 ≤ 0. To see this add (α + β)u(1) to both sides and rearrange

un 1 + α + β

α 1 + α + β

1 α

∆td11G(u(1))

u(1) =

u(1) +

+

β 1 + α + β

1 β

∆t2|d˙11|G˙ (u(1)) .

u(1) −

+

Assuming that α ≥ 0 and β ≥ 0 we have (from the forward Euler condition and backward derivative condition)

1 1 + α + β

α 1 + α + β

β 1 + α + β

u(1) , hence

u(1) ≤

un +

u(1) +

u(1) ≤ un ,

for any ∆t such that α1 ∆td11 ≤ ∆tFE and β1|d˙11|∆t2 ≤ k˙∆t2FE. Since we can choose α and β to be arbitrarily large then this is true for any ∆t.

Each subsequent stage of the method is given by

 riun +

  + ∆tdiiG(u(i)) + ∆t2d˙iiG˙ (u(i)),

- i−1
- j=1


u(i) =

piju(j)

where we can now assume that u(j) ≤ un , for all j < i. The explicitly computed terms are

- i−1
- j=1


u(ei) = riun +

≤ ri un +

= un .

piju(j) ≤ riun +

 ri +

- i−1
- j=1


- i−1
- j=1


pij u(j) ≤

- i−1
- j=1


piju(j)

  un

pij

due to the non-negativity of ri and pij, and the fact that they sum to one. Note that this condition is independent of ∆t. Finally we write each stage as

u(i) = u(ei) + ∆tdiiG(u(i)) + ∆t2d˙iiG˙ (u(i)), and use the same argument as for the ﬁrst stage above to show that u(i) ≤ u(ei) ≤

un under any time-step ∆t, provided only that dii ≥ 0 and d˙ii ≤ 0.

| |
|---|


2.3. New SSP implicit two-derivative Runge–Kutta methods up to order p = 4. We found second, third, and fourth order methods that satisfy the conditions above, and are unconditionally SSP. Second order The one-stage, second order method is simply the implicit Taylor series method

- 1

- 2


∆t2G˙ (un+1).

un+1 = un + ∆tG(un+1) −

Third order A two-stage, third order unconditionally SSP implicit two-derivative Runge–Kutta method is given by the Shu-Osher coeﬃcients

, D˙ = −61 0 0 −13

- 0 0
- 1 0


1 0

- 0 0
- 0 1


, and the Butcher coeﬃcients

, P =

, Re =

D =

, A˙ = −61 0 −16 −31

- 0 0
- 0 1


A =

.

Fourth order A ﬁve-stage, fourth order unconditionally SSP implicit two-derivative Runge–Kutta method is given by the Shu-Osher coeﬃcients









−0.177750705279127 −0.354733903778084 −0.403963513682271 −0.161628266349058 −0.218859021269943

0.660949255604937 0.242201390400848 1.137542996287740 0.191388711018110 0.625266691721946

, diag(D˙ ) =

,

diag(D) =

 

 

 

 





- 0 0 0 0 0
- 1 0 0 0 0


0.084036809261019 0.915963190738981 0 0 0 0.001511648458457 0 0.090254853867587 0 0

,

P =

 

 

0 0 0 1 0

Re = [1,0,0,0.908233497673956,0]T . And Butcher coeﬃcients

aii = dii, a12 = a13 = a11, a14 = a15 = 0.060653001401867, a23 = 0.221847558352979, a24 = a25 = 0.020022818960029,

a34 = a35 = 0.102668776898047, a45 = a44, and

a˙ii = d˙ii, a˙12 = a13 = a˙11, a˙14 = a˙15 = −0.016311560509453, a˙23 = −0.324923198367868, a˙24 = a˙25 = −0.029325895786881, a˙34 = a˙35 = −0.036459667895230, a˙45 = a˙44.

We were unable to ﬁnd any ﬁfth order methods that satisfy the conditions in Theorem 1.

10

10

8

8

6

6

4

4

2

2

0

0

- -4
- -2


-2

0 0.5 1 1.5 2

0 0.5 1 1.5 2

Fig. 1. The solution of u = −10u2 for the DIRK (dashed lines) and SSP-iMDRK (solid

lines) compared to the correct solution (dash-dot line) for ∆t = n1 where n = 4, 8, 16, 32, 64 in blue, red, green, magenta, and cyan, respectively. We see that if ∆t is not small enough the qualitative

behavior of the numerical solution using the DIRK methods is poor. However, the SSP-iMDRK methods converge to a solution that is qualitatively correct for all values of ∆t tested. Left: second order methods. Right: third order methods.

2.4. Numerical tests. We test all three of our methods on the nonlinear scalar problem

ut = −10u2,

with initial condition u(0) = 10, with Tfinal = 2. Here, G = −10u2 and G˙ = 200u3. This problem satisﬁes the forward Euler condition for positivity:

0.1 un

un > 0 ⇒ un+1 = un + ∆tG(un) = un (1 − 10∆tun) > 0, for ∆t ≤

, and the backward derivative conditions for positivity:

0.005 (un)2

un > 0 ⇒ un+1 = un − ∆t2G˙ (un) = un 1 − 200∆t2(un)2 > 0, for ∆t2 ≤

.

Note that these restrictions induce a severe time-constraint, especially as un is large, on an explicit method. However, as long as these (explicit-type) conditions hold for non-zero ∆t, we preserve this positivity property unconditionally for the implicit methods we found above.

We compare our second and third order methods in the subsection above to diagonally implicit stiﬄy stable methods in the literature, with Butcher tableau [19]

### Third order DIRK

Second order DIRK

|0 3 2 7 5<br><br>1<br><br><br>|0 0 0 0<br><br>3<br><br>4<br><br><br>3<br><br>4 0 0<br><br><br>447 675 −357675 855675 0<br><br>13 42<br><br>84 42 −12542 7042<br><br>|
|---|---|
| |13 84 125 70<br><br>|


|0<br>1<br>|0 0<br><br>1<br><br>2<br><br><br>1<br><br>2<br>|
|---|---|
| | |


- 1

- 2


- 1

- 2


42 42 − 42 42

As expected, the SSP methods preserve positivity up to a large time-step, while the DIRK methods lose positivity for relatively small time-steps. The second order DIRK method loses positivity for ∆t > 501 and the third order for ∆t > 751 . This loss

of positivity has signiﬁcant consequences to the convergence of the schemes. We see in Figure 1 that the DIRK methods converge to a solution that is qualitatively poor if the time-step is not small. On the other hand, the unconditionally SSP methods converge to a solution that is qualitatively correct even for much larger time-steps.

3. Multi-derivative IMEX methods. In this section we consider equations of the form (7):

ut = F(u) + G(u),

where the time-step restriction coming from F is of a reasonable size (i.e. F is nonstiﬀ), but the time-step restriction coming from G is very small (i.e. G is stiﬀ). We wish to alleviate this time-step restriction. When dealing with linear stability, we typically turn to IMEX methods to alleviate the time-step restriction coming from G. However, when we consider more general norms, semi-norms, or convex functionals, the use of IMEX schemes does not result in the removal of the time step restriction caused by the operator G, as shown in [13, 7]. Now that we have showed that unconditional multi-derivative SSP methods exist under the backward derivative conditions, we wish to leverage this knowledge to develop SSP IMEX methods that avoid a time-step restriction coming from G. We do this by using an explicit SSP solver for the non-stiﬀ term F, coupled with a purely (or diagonally) implicit solver for the stiﬀ term G.

We assume that the operators F and G preserve some nonlinear stability properties under a convex functional · :

- Condition 1: u + ∆tF(u) ≤ u for all ∆t ≤ ∆tFE,

for some ∆tFE > 0, and

- Condition 2: u + ∆tG(u) ≤ u for all ∆t ≤ k∆tFE


for some k > 0, which may be very small.

The backward derivative condition is natural and relevant in many cases (see Subsection 3.4.1); we assume that G˙ (u) = G (u)G(u) satisﬁes:

Condition 3: u − ∆t2G˙ (u) ≤ u for all ∆t2 ≤ k˙ ∆t2FE,

(where k˙ > 0 can be of any size). Just as above for the implicit methods, we can devise SSP IMEX methods where there is no time-step restriction coming from G or G˙ , so that the time-step restriction depends only on F.

For problem (7), we propose an s-stage multi-derivative IMEX method, written in the Shu-Osher formulation, as follows

- i−1
- j=1


- i−1
- j=1


∆t r

- (13a) F(u(j)) +∆tdiiG(u(i)) + ∆t2d˙iiG˙ (u(i)), i = 1,...,s,
- (13b) un+1 = u(s).


u(i) = riun +

piju(j) +

wij u(j) +

The value of r > 0 in the canonical Shu-Osher formulation gives us the SSP coeﬃcient of the explicit method. While at ﬁrst glance it seems that requiring all the forward Euler steps in the method to have the same time-step ∆rt is restrictive, in fact this form does not result in loss of generality, as discussed in [10]. Note that the terms

G and G˙ appear only implicitly, so that there is no SSP restriction arising from the implicit method.

The intermediate stages can be conveniently written in a matrix form:

∆t r

- (14) F(U) + ∆tDG(U) + ∆t2D˙ G˙ (U),

where P, W, and R = I − P − W are s × s matrices, ri are the ith row sum of R, D and D˙ are s × s diagonal matrices, and e is a vector of ones. The numerical solution un+1 is then given by the ﬁnal element of the vector U.

3.1. SSP properties of multi-derivative IMEX Runge–Kutta. The ShuOsher form allows us to easily observe the strong stability preserving properties of the method:

Theorem 2. Given operators F and G that satisfy Conditions 1, 2, and 3, with values ∆tFE > 0, k > 0, k˙ > 0, for some convex functional · , and if the method given by (14) with r > 0 satisﬁes the componentwise conditions

- (15) Re ≥ 0, P ≥ 0, W ≥ 0, D ≥ 0, D˙ ≤ 0,


U = Reun + PU + W U +

then it preserves the strong stability property

un+1 ≤ un

under the time-step condition

∆t ≤ r∆tFE. Proof. Each stage of the method is

 riun +

- i−1
- j=1


- i−1
- j=1


piju(j) +

wij u(j) +

u(i) =

+ ∆tdiiG(u(i)) + ∆t2d˙iiG˙ (u(i)) .

∆t r

F(u(j))

 

In particular, the ﬁrst stage is

u(1) = un + ∆td11G(u(i)) + ∆t2d˙11G˙ (u(i)) .

Following the argument in the Proof of Theorem 1, we easily show that u(1) ≤ un .

Now we assume that for the ith stage, we start with the i−1 previous stage values, each of which satisfy u(j) ≤ un .The explicit part of the ith stage is deﬁned by

- i−1
- j=1


uie = riun +

piju(j) +

- i−1
- j=1


wij u(j) +

∆t r

F(u(j)) .

We note that this value depends only on previous stages and the operator F. Given

the non-negativity of all the coeﬃcients (12) we can show that

- i−1
- j=1


uie = riun +

≤ ri un +

≤ ri un +

piju(j) +

- i−1
- j=1


∆t r

wij u(j) +

F(u(j))

- i−1
- j=1


pij u(j) +

- i−1
- j=1


pij u(j) +

- i−1
- j=1


∆t r

wij u(j) +

F(u(j))

- i−1
- j=1


wij u(j) ,

for all ∆t ≤ r∆tFE. Now, recalling that u(j) ≤ un for j < i, we obtain uie ≤ un , from the condition R + W + P = I.

We now have u(i) = uie + ∆tdiiG(u(i)) + ∆t2d˙iiG˙ (u(i)) where uie ≤ un . Using Conditions 2 and 3 and the argument in the proof of Theorem 1 above, we can show

that u(i) ≤ uie , whenever dii ≥ 0 and d˙ii ≤ 0, and so u(i) ≤ un under the time-step ∆t ≤ r∆tFE.

| |
|---|


In Subsection 3.3 we will show that it is indeed possible to ﬁnd second and third order methods that satisfy the requirements in Theorem 2. However, we ﬁrst present the order conditions a method of this form must satisfy.

3.2. Formulating order conditions. The order conditions for a method (13) are generally easier to formulate if the method is written in its Butcher form:

- i−1
- j=1


- i
- j=1


i

- (16a) a˙ijG˙ (u(j)), i = 1,...,s,


u(i) = un + ∆t

aˆijF(u(j)) + ∆t

aijG(u(j)) + ∆t2

j=1

- i−1
- j=1


- i
- j=1


- i
- j=1


- (16b) b˙jG˙ (u(j)).

To be consistent with (13), we require that un+1 = u(s), so that ˆbj = aˆsj, bj = asj, b˙j = a˙sj. The intermediate stages of this method can be written in a matrix form:

- (17) U = eun + ∆t AF(U) + ∆tAG(U) + ∆t2A˙ G˙ (U).

The conversion between the two formulations (14) and (17) is given by:

A =

1 r

- (18) R−1W, A = R−1D, A˙ = R−1D˙ .


ˆbjF(u(j)) + ∆t

un+1 = un + ∆t

bjG(u(j)) + ∆t2

The vectors b, b, and b˙ are given by the last row of A, A, and A˙ , respectively. The vectors c = Ae, c˙ = Ae˙ , and c = Ae deﬁne the time-levels at which the stages are happening; these values are known as the abscissas. The order conditions for methods of this form are:

|For p ≥ 1 bte = 1 bte = 1<br><br>|
|---|
|For p ≥ 2 btc + b˙ te = 21<br><br>bt c = 12 btc = 12 btc = 12<br><br>|
|For p ≥ 3 btAc + b˙ tc + btc˙ = 61<br><br>btA c + b˙ t c = 61 btAc = 61 btAc = 61<br><br>|


|For p ≥ 3 btAc + btc˙ = 16 (continued) btA c = 16 bt Ac = 16 bt A c = 16 bt(c · c) + 2b˙ tc = 31 bt(c · c) + b˙ t c = 13 bt( c · c) = 13 bt(c · c) = 13 bt(c · c) = 13 bt(c · c) = 13<br><br>|
|---|


3.3. New SSP IMEX multi-derivative Runge–Kutta methods. Given functions F and G that satisfy Conditions 1-3, these IMEX methods have an explicit part that is SSP for a time-step that depends only on F, and an implicit part that is unconditionally SSP. We will later show that these methods are positivity preserving and also asymptotic preserving for the problems described in Subsection 3.4.1.

3.3.1. Second order method. We begin with a method that has Shu-Osher coeﬃcients

 , P =

 

 , Re =

 

 ,

 

0 0 0 0 0 0 1/2 0 0

1 0 0

- 0 0 0
- 1 0 0 0 1/2 0


W =

and

 

 ,

 , diag(D˙ ) = −

 

- 1

- 2


- 0
- 1

- 2 0


- 0
- 1

- 2


diag(D) =

with r = 1. In Butcher form, these become

 .

 , A˙ =

 

 , A =

 

 

0 0 0 0 −1/2 0 0 −1/4 0

1/2 0 0

- 0 0 0
- 1 0 0 1/2 1/2 0


- 1/2 0 0
- 1/2 0 1/2


A =

The beneﬁt of this method over the one in [16] is that the positivity preserving coeﬃcient r = 1 for this method is larger than the positivity preserving coeﬃcient r = 0.8125 in the method given in Subsection 2.6.2 of [16]. The two methods each require the implicit solution of three stages.

3.3.2. Third order method. We found a third order method of this form, as well. This method has r = 0.904402174130635 with coeﬃicients:









0 2 0.388820513661584 0.083529464436389 1.793313488277995 0

0.871358934880525 0.856842702601821 0 0 2 0.205134529930013

, diag(D˙ ) = −

diag(D) =

.

 

 

 

 

Note that dii + d ˙ii > 0 for each stage i.





0 0 0 0 0 0 0.058453072749259 0 0 0 0 0 0.764266518291495 0 0 0 0 0

,

W =

0 0 0.292520982667463 0 0 0 0.173788618990251 0 0 0.281050180194829 0 0 0.016811671845949 0 0 0.448630511341543 0 0

 

 





0 0 0 0 0 0

0.253395246357353 0 0 0 0 0 0 0.235733481708505 0 0 0 0 0 0.123961833526104 0 0 0 0

,

P =

 

 

0.409037644509411 0.136123556305509 0 0 0 0 0.203353399602184 0 0 0 0.331204417210324 0





1 0.688151680893388 0 0.583517183806433 0 0

.

Re =

 

 

We have the Butcher form coeﬃcient matrices:





0 0 0 0 0 0 0.064631725156397 0 0 0 0 0 0.860287477078593 0 0 0 0 0 0.259664005325885 0 0.323441264334256 0 0 0 0.273935075266107 0 0.090903225623586 0.310757966128278 0 0 0.225810414773773 0 0.175213169672431 0.598976415553796 0 0

Aˆ =

,

 

 





0 0 0 0 0 0 0 2 0 0 0 0 0 0.471466963417009 0.388820513661584 0 0 0 0 0.385837646486197 0.113738158737554 0.083529464436389 0 0 0 0.380686852681912 0.031966130008218 0.023475971031425 1.793313488277995 0 0 0.299183707820065 0.061613731773316 0.045249211646092 0.593953348760527 0

A =

,

 

 

and





0.871358934880525 0 0 0 0 0 0.271731819181020 0.856842702601821 0 0 0 0 0.730006747169852 0.201986513560852 0 0 0 0 0.247226665569066 0.165301085890380 0 0 0 0 0.614323072678900 0.163094375848475 0 0 2 0 0.506222742811925 0.128176688391489 0 0 0.662408834420649 0.205134529930013

A˙ = −

.

 

 

To achieve a third order method we required six stages. However, this allowed us to design a third order method that is SSP with a time-step restriction that does not depend on G.

3.4. Applications. The new SSP multi-derivative IMEX methods developed in Subsection 3.3 are of particular use for a number of models we describe in Subsection 3.4.1. These are all problems that lead to ODE systems of the form:

- (19)


du dt

= T(u) +

1 ε

Q(u),

where the solution u(t) ∈ RN, and the operators T, Q: RN → RN, N ≥ 2. The parameter 0 < ε ≤ O(1) indicates the regime of the problem: ε = O(1) corresponds to the non-stiﬀ regime; ε 1 to the stiﬀ regime. For such systems, we require a high order time discretization that preserves the physical properties at the discrete level, in particular positivity and the asymptotic limit.

Positivity: Problems of the form (19) that are of interest to us have positive solutions. It is preferable that the numerical solution will preserve this positivity property, for a time-step not dependent on ε. It should be pointed out that positivity is an important property when solving kinetic equations. For example, the Bhatnagar-Gross-Krook (BGK) model (see equation (41) below) requires the macroscopic quantities to be positive, and even small negative values of the solution f may cause some macroscopic quantities, especially the temperature, to fail to be well-deﬁned. In such cases, the requirement that the numerical solution remains positive for time-steps independent of ε is critical to the success of the simulation. Strong stability preserving methods are also positivity preserving, so the multi-derivative IMEX methods given in Subsection 3.3 will preserve these properties, with a time-step independent of ε.

Asymptotic limit: Very often the operator Q satisﬁes the following properties: Q is “conservative” in the sense that there exists a linear operator R: RN → Rn, n < N, s.t. RQ(u) = 0, ∀ u; Q is dissipative and has a unique local equilibrium of the form E(Ru), where E: Rn → RN is some operator. Using these properties, applying R to

- (19) yields
- (20)

dω dt

= RT(u), ω := Ru,

which is not a closed system. However, if ε → 0, (19) implies Q(u) → 0, hence u → E(ω). Substituting this u into (20) gives a closed (reduced) system:

- (21)

dω dt

= RT(E(ω)).

The above simple analysis reveals that when ε → 0, (19) is not only stiﬀ but also possesses a non-trivial asymptotic limit. (Recall that n < N and note that the original variable u is in RN while the reduced variable ω is in Rn.)

Systems of the form (19) arise (after the method of lines discretization of a PDE) from many physical problems in multi-scale modeling. A prominent example is the Boltzmann equation in kinetic theory [4]:

- (22) ∂tf + v · ∇xf =


1 ε

Q(f), x,v ∈ Rd,

where f = f(t,x,v) ≥ 0 is the probability density function of time t, position x, and velocity v. The term v · ∇xf describes the particle transport, and Q(f) describes the collisions between particles, which is a complicated nonlinear integral operator. The dimensionless parameter ε, called the Knudsen number, is deﬁned as the ratio of the mean free path and characteristic length scale. When ε = O(1), the transport and collision balance so the system is in the fully kinetic regime. When ε 1, the collision eﬀect dominates, i.e., collisions happen so frequently that the overall system is close to the local equilibrium or ﬂuid regime. In this case, one can derive the limiting ﬂuid equations (the compressible Euler equations) as ε → 0 from (22). The process is similar to the abstract model reduction procedure described above for (19).

We require a time-stepping method that preserves the asymptotic limit of the equation. That is, for a ﬁxed ∆t, when ε → 0, the scheme for (19) automatically reduces to a high order time discretization for the limiting system (21). A numerical scheme with this property is called asymptotic preserving (AP) as initially coined in [18]. To insure the AP property, the time step ∆t should not be limited by the small parameter ε. This necessitates some implicit treatment of the stiﬀ collision term

1

εQ(u). The need for the AP property further motivates the use of implicit-explicit (IMEX) methods. There is an extensive literature on development of IMEX schemes

that possess the AP property, see, for instance, [21, 8, 2, 9] for the application to hyperbolic and kinetic equations.

The need for a high order numerical integrator that is both asymptotic preserving and positivity preserving motivated the work in this paper. We will show that the second and third order methods we presented above are asymptotic preserving high order time discretization methods that preserve the positivity of the solution for arbitrary ε. Previously, designing a time-stepping scheme with both positivity and AP property has proven diﬃcult. First order IMEX schemes with these properties exist, but methods above ﬁrst order may violate positivity unless the time-step is restricted by ε [13, 14].

Second order IMEX schemes that preserve the AP property and positivity for arbitrary ε have been previously found, by incorporating a derivative correction term at the ﬁnal stage of each time-step. Such an approach was successfully considered in [17, 16] (note that the method in [17] only works for a special relaxation system and can preserve the positivity of one component of the solution vector, while [16] works for a general class of equations and the scope is similar to what we consider in this work); however, this strategy failed to ﬁnd methods of order three. By formulating IMEX multi-derivative Runge–Kutta methods that allow the use of Q˙ at every stage, we are able to obtain a third order IMEX method that is AP and positivity preserving independent of ε. Furthermore, the second order method improves upon the previously presented method in [16], in the sense that we obtain a 23% larger allowable time-step.

We present a a summary of the model equations and their properties in Subsection 3.4.1. In Subsection 3.4.2 we prove the positivity and asymptotic preserving properties of the multi-derivative IMEX Runge–Kutta methods. Finally, in Subsection 3.5 we demonstrate the numerical performance of these methods on sample problems.

3.4.1. A summary of the models and properties. We assume that the operators T and Q in (19) satisfy the following properties:

- Property 1 The operator T is conditionally positivity preserving under a forward Euler step:

(23) u > 0 =⇒ u + ∆tT(u) > 0, ∀ 0 ≤ ∆t ≤ ∆tFE, for some time step ∆tFE > 0.

- Property 2 The operator Q is unconditionally positivity preserving under a backward Euler step:


(24) u > 0, v = u + ∆tQ(v) =⇒ v > 0, ∀ ∆t ≥ 0.

We observe that the ﬁrst two properties essentially concern the positivity preserving property of the operators T and Q in equation (19).

Remark 1. Property 2 plays a similar role to that of Condition 2 in Section

- 3. Condition 2 is a forward Euler condition (2), which we then use to show that the backward Euler method unconditionally preserves this strong stability property.


- Property 2 states that backward Euler preserves positivity unconditionally. This is necessary because positivity may be preserved under the forward Euler condition but be violated (for certain ∆t) for the backward Euler method.
- Property 3 Conservation of Q: there exists a linear operator R : RN → Rn, n < N, s.t.

- (25) RQ(u) = 0, ∀ u.

Property 4

Equilibrium of Q: there exists an (possibly nonlinear) operator E : Rn → RN, s.t.

- (26) Q(u) = 0 =⇒ u = E(Ru).


- Property 5 The Fr´echet derivative of Q satisﬁes


Moreover, E satisﬁes RE(Ru) = Ru, ∀ u.

Note that Properties 3 and 4 together imply that (19) has a limiting system (21). Properties 1–4 are satisﬁed by a large class of kinetic equations of the form (22), where the collision operator Q can be the full Boltzmann collision operator (an integral type operator), the kinetic Fokker-Planck operator (a diﬀusion type operator), the BGK operator (a relaxation type operator), or its generalized version such as the ES-BGK operator. For more details about these operators, we refer the readers to [15].

- (27) Q˙ (u) := Q (u)Q(u) = −CRuQ(u),

where CRu is some positive function depending only on Ru. The Fre´chet derivative of Q at u is deﬁned by

- (28) Q (u)v = lim δ→0


Q(u + δv) − Q(u) δ

.

Property 5 means the operator Q is dissipative in some sense. This property is not generic but it is satisﬁed by quite a few kinetic models including the BGK operator and the Broadwell model. Some stiﬀ ODE systems and hyperbolic relaxation systems also satisfy this property, though for these problems positivity is usually not a big concern compared to the kinetic equations. Since our proposed multi-derivative methods highly depend on Property 5, we list below a few examples.

## • An ODE model:

- (29)

 



u 1 = u2, u 2 =

1 ε

f(u1)(g(u1) − u2), where f and g are some functions of u1, and f(u1) > 0. Deﬁne

- (30) u = (u1,u2)T, T(u) = (u2,0)T, Q(u) = (0,f(u1)(g(u1) − u2))T ,


- then (29) falls into the general form (19). It is easy to see that (29) has a limit as ε → 0:
- (31) u 1 = g(u1).

Indeed, one can just take Ru = u1 and E(Ru) = E(u1) := (u1,g(u1))T. It can also be veriﬁed by direct calculation that

- (32) Q˙ (u) = −f(u1)Q(u).

• A PDE model: the hyperbolic relaxation system [5]:

- (33)

 



- ∂tu1 + ∂xu2 = 0,
- ∂tu2 + ∂xu1 =


1 ε

(F(u1) − u2),

where F is some function of u1. Equation (33) again has the form of (19) if we deﬁne u = (u1,u2)T, T(u) = −(∂xu2,∂xu1)T, Q(u) = (0,F(u1) − u2)T. Note that we abused the notation a bit: u, T and Q should be deﬁned for the system after spatial discretization. It is easy to see that (33) has a limit as ε → 0:

- (34) ∂tu1 + ∂xF(u1) = 0.

Indeed, one can just take Ru = u1 and E(Ru) = E(u1) := (u1,F(u1))T. Similarly to the previous model, it can be veriﬁed that

- (35) Q˙ (u) = −Q(u).

• The Broadwell model [3]: The Broadwell model is a simple discrete velocity kinetic model:

- (36)

 



∂tf+ + ∂xf+ =

1 ε

(f02 − f+f−), ∂tf0 = −

1 ε

(f02 − f+f−), ∂tf− − ∂xf− =

1 ε

(f02 − f+f−),

where f+ = f+(t,x), f0 = f0(t,x), and f− = f−(t,x) denote the densities of particles with speed 1, 0, and −1, respectively. Deﬁne f = (f+,f0,f−)T, T(f) = (−∂xf+,0,∂xf−)T, and Q(f) = (f02 − f+f−,−(f02 − f+f−),f02 − f+f−)T (again these should be deﬁned for the system after spatial discretization). Then (36) falls into the general form (19). To see its limit as ε → 0, we rewrite (36) using moment variables:

- (37)


 

∂tρ + ∂xm = 0, ∂tm + ∂xz = 0,



- 1

- 2ε


(ρ2 + m2 − 2ρz),

∂tz + ∂xm =

where ρ := f+ + 2f0 + f−, m := f+ − f−, and z := f+ + f−. From (37), it is clear that when ε → 0, z → ρ

2+m2

2ρ . This, when substituted into the ﬁrst two

equations, yields a closed hyperbolic system:

- (38)

 



∂tρ + ∂xm = 0, ∂tm + ∂x

ρ2 + m2 2ρ

= 0.

Indeed, the operators R and E in Properties 3–4 can be taken as

- (39) Rf = (ρ,m)T,

E(Rf) = E((ρ,m)T) :=

(ρ + m)2 4ρ

,

ρ2 − m2 4ρ

,

(ρ − m)2 4ρ

T

.

Furthermore, it can be veriﬁed that

- (40) Q˙ (f) = −ρQ(f).

• The Bhatnagar-Gross-Krook (BGK) model [1]: The BGK model is a widely used kinetic model introduced to mimic the full Boltzmann equation:

- (41) ∂tf + v · ∇xf =

1 ε

(M − f), x,v ∈ Rd,

where f = f(t,x,v) is the probability density function and M is the so-called Maxwellian given by

- (42) M(t,x,v) =

ρ(t,x) (2πT(t,x))d/2

exp −

|v − u(t,x)|2 2T(t,x)

,

where the density ρ, bulk velocity u and temperature T are given by the moments of f:

- (43) ρ = Rd

f dv, ρu =

Rd

fv dv,

- 1

- 2


ρdT =

- 1

- 2 Rd


f|v − u|2 dv.

To see its asymptotic limit, we multiply (41) by (1,v,|v|2/2)T and integrate w.r.t. v to obtain







∂tρ + ∇x ·

Rd

vf dv = 0,

∂t(ρu) + ∇x ·

Rd

v ⊗ vf dv = 0,

∂tE + ∇x ·

Rd

- 1

- 2


v|v|2f dv = 0,

- (44)

where E = 21ρu2 + 12ρdT is the total energy. This system is not closed. However, if ε → 0, (41) implies f → M. Substituting this f into (44), we can

get a closed system

 



∂tρ + ∇x · (ρu) = 0, ∂t(ρu) + ∇x · (ρu ⊗ u + pI) = 0, ∂tE + ∇x · ((E + p)u) = 0,

- (45)


where I is the identity matrix and p = ρT is the pressure. Equation (45) is nothing but the compressible Euler equations. To write the BGK model into the form (19), we deﬁne T(f) = −v · ∇xf and Q(f) = M − f (these should be deﬁned for (41) after spatial and velocity discretization). Moreover, the operators R and E are given by

- (46) f(1,v,|v|2/2)T dv = (ρ,ρu,E)T,
- (47) E(Rf) = E((ρ,ρu,E)T) = M. Furthermore, it can be veriﬁed that
- (48) Q˙ (f) = −Q(f).


Rf =

Rd

To summarize, we have introduced four diﬀerent models (including both ODE and PDEs) which all satisfy Properties 3–5. For the Broadwell model and BGK model, one can check that they also satisfy the positivity-preserving Properties 1–2 provided a positivity preserving spatial discretization is used for the transport/convection term, see [16] for more details.

## 3.4.2. Properties of the numerical scheme. A multi-derivative IMEX method

that is SSP as shown in Subsection 3.1 will also be positivity preserving. This is because the SSP property holds for any convex functional, and positivity is preserved under a convex functional. In Proposition 1 we show this explicitly, and we also prove that under a mild additional condition satisﬁed by the methods in Subsection 3.3, the asymptotic preserving property is satisﬁed as well.

Proposition 1. Assume that the problem (19) satisﬁes the Properties 1–5 listed in Subsection 3.4.1. Then the scheme (13) that satisﬁes the inequalities (element-wise)

- (49) Re ≥ 0, P ≥ 0, W ≥ 0, D ≥ 0, D˙ ≤ 0,

will preserve the positivity of the solution for all ∆t ≤ r∆tFE. Furthermore, if we require that at least one of Q or Q˙ appear at every stage, i.e. the strict inequality

- (50) dii + d ˙ii > 0, for all i = 1,...,s,

is also satisﬁed, then the scheme is AP, i.e. when ∆t is ﬁxed, as ε → 0, (13) automatically reduces to an explicit Runge-Kutta scheme, with the same order as the original scheme, applied to the limiting system (21).

Proof. We consider each stage of (13),

u(i) = riun +

- i−1
- j=1


piju(j) +

- i−1
- j=1


wij u(j) +

∆t r

- (51) T(u(j))


∆t2 ε2

∆t ε

d˙iiQ˙ (u(i))

diiQ(u(i)) +

+

- i−1
- j=1


- i−1
- j=1


∆t r

= riun +

piju(j) +

wij u(j) +

∆t2 ε2

∆t ε

d˙iiCRu(i) Q(u(i)),

dii −

+

T(u(j))

where we applied Property 5 to the last term Q˙ (u(i)). At the ﬁrst stage, we have

u(1) = un +

∆t2 ε2

∆t ε

d˙11CRu(1) Q(u(1)).

d11 −

Given a positive un, and since d11 ≥ 0, d˙11 ≤ 0, and CRu(1) > 0, using Property 2 we obtain u(1) > 0.

Now, given a positive un and positive stages u(j) for j < i, Property 1 gives us the positivity of the explicit terms

u(j) +

∆t r

T(u(j)) > 0, for all

∆t r ≤ ∆tFE.

Consequently, the non-negativity of ri, pij, and wij, together with the fact that ri + i−1 j=1(pij + wij) = 1 ensures the positivity of the explicit terms in u(i)

- i−1
- j=1


riun +

piju(j) +

- i−1
- j=1


wij u(j) +

∆t r

T(u(j)) > 0.

Finally, since dii ≥ 0, d˙ii ≤ 0, and CRu(i) > 0, Property 2 assures that u(i) > 0.

To see the AP property, we apply R to (51) to obtain (deﬁne ωn = Run, ω(i) = Ru(i))

- i−1
- j=1


- i−1
- j=1


∆t

- (52) r RT(u(j)) ,

where the collision terms are gone due to Property 3. On the other hand, when ∆t is ﬁxed and ε → 0, since dii + |d˙ii| > 0 and CRu(i) > 0, we have from (51) that Q(u(i)) → 0, hence u(i) → E(ω(i)) by Property 4. Note that this holds for every i = 1,...,s. Replacing u(j) by E(ω(j)) in (52) yields

ω(i) = riωn +

- i−1
- j=1


pijω(j) +

- i−1
- j=1


wij ω(j) +

∆t r RT(E(ω(j))) , i = 1,...,s;

together with ωn+1 = ω(s), this is a high order explicit Runge-Kutta scheme applied to the limiting system (21). In fact, it is the explicit part of (13) applied to (21).

| |
|---|


- Remark 2. Following the classiﬁcation of various IMEX Runge-Kutta schemes

in [2], the multi-derivative IMEX schemes introduced in this paper are both type A and GSA. In other words, since dii + d ˙ii > 0 for all i, we are solving an implicit collision step at every stage of the scheme, hence any initial condition is allowed to guarantee the AP property.

- Remark 3. In the case of the Broadwell model and BGK equation, Theorem 2


can be used to prove the discrete entropy decay property of the numerical method. Taking the following 1D BGK equation as an example,

- (53) ∂tf + v∂xf =


ω(i) = riωn +

pijω(j) +

wij ω(j) +

1 ε

(M − f).

We set G to be the BGK operator and F be the transport operator discretized by the ﬁrst order upwind method (k is the spatial index):

- (54) (v∂xf)k =

v + |v| 2

fk − fk−1 ∆x

+

v − |v| 2

fk+1 − fk ∆x

,

together with the periodic or compactly supported boundary condition. The convex functional · is taken as the discrete entropy

- (55) S[f] = ∆x k

fk log fk dv.

Then it can be veriﬁed that F and G satisfy the Conditions 1–3 (for more details see [16]). Therefore, the numerical solution obtained by method (14) satisﬁes

- (56) S[fn+1] ≤ S[fn],

under the conditions listed in Theorem 2.

3.5. Numerical results. In this subsection, we verify the accuracy of the proposed second and third order methods in Subsection 3.3 on the ODE model, the Broadwell model, and the BGK equation. We will see that the methods exhibit the design accuracy in the kinetic regime ε = O(1) as well as the ﬂuid regime ε 1. This latter behavior is exactly due to the AP property of the methods. For completeness, we also report the results of the methods in the intermediate regime (i.e., ε lies between 0 and 1), where the methods may exhibit some order reduction as expected. A careful study of this behavior is beyond the scope of the current work and left for future work.

Remark 4. Note that the order conditions in Subsection 3.2 do not guarantee that we will not observe order reduction. When ε = O(1) we expect to see the design accuracy predicted by the order conditions. When ε 1 design accuracy may not be evident due to the order reduction phenomenon. However, the AP property allows us to recover full accuracy in the asymptotic limit ε → 0.

3.5.1. An ODE model. We consider the ODE model (29) with

- (57) f(u1) = 1 + u21, g(u1) = sinu1.

We take the initial data as u(0) = (2,0)T (which is inconsistent initial data, i.e., we do not start from equilbrium), and solve (29) by the second and third order methods in Subsection 3.3, up to ﬁnal time T = 1, with various ε and ∆t. To calculate the error of a numerical solution U = [U1,U2]T, we compare with a reference solution Uref obtained by the MATLAB solver ode15s with relative tolerance RelTol = 1e − 13 and absolute tolerance AbsTol = 1e − 15, and compute the error by

- (58) error = |U1(T) − U1ref(T)| + |U2(T) − U2ref(T)|.


The results are shown in Figures 2 and 3. For both methods, one can see the design order accuracy in the kinetic regime (ε = O(1) and ∆t is relatively small) and the ﬂuid regime (ε 1 and ∆t is not very small), while in the intermediate regime (when ε and ∆t are comparable) one can see some order reduction. In Figure 3 with ε = 1 (and similar for ε = 0.01,1e−10), one can see that the error increases as ∆t decreases

when ∆t is less than 5e−5, and this is a consequence of the accumulation of round-oﬀ errors.

We note that the intermediate plateaus that are seen in Figures 2 and 3 are not an indication of the order reduction phenomena that is usually observed in the AP literature, as we observe the errors are not converging at a rate of O(∆t), but leveling oﬀ at the order of ε. This result is not caused by numerical round oﬀ errors, as the schemes are still converging to a “solution” at the designed order of accuracy. Indeed, if we compare the solution at time-step ∆t to the ∆t/2 solution, we observe designorder of convergence. The explanation for these O(ε) plateaus can likely be found by looking at the higher order asymptotic expansion. In practice, these errors are of O(ε) which are typically much smaller than other sources of errors in simulations thus not typically exhibited in practice.

10-2

10-2

10-4

10-4

10-6

10-6

error

error

10-8

10-8

10-10

10-10

|=1<br><br>=0.01<br><br>=0.0001<br><br>=1e-06 =1e-08 =1e-10<br><br><br>slope=2|
|---|


|=1<br><br>=0.01<br><br>=0.0001<br><br>=1e-06 =1e-08 =1e-10<br><br><br>slope=3|
|---|


10-12

10-12

10-7 10-6 10-5 10-4 10-3 10-2 10-1

10-7 10-6 10-5 10-4 10-3 10-2 10-1

t

t

Fig. 2. Accuracy test of the new second order IMEX scheme for an ODE model.

Fig. 3. Accuracy test of the new third order IMEX scheme for an ODE model.

3.5.2. The Broadwell model. We consider the Broadwell model (36) on the domain x ∈ [0,2] with periodic boundary condition, with inconsistent initial data

f+(0,·) = 1 + 0.2exp(0.3sin(πx)), f−(0,·) = exp(0.2cos(2πx)), f0(0,·) =

1 1 + 0.3sin(πx)

.

We discretize in space by the ﬁfth order ﬁnite volume WENO scheme, and the collision operator Q is evaluated pointwise on the Gauss quadrature points in each cell, as described in Subsection 3.3.2 of [16]. We ﬁx the the CFL number as ∆t = 12∆x, and solve (36) by the second and third order methods in Subsection 3.3 up to ﬁnal time T = 0.1. The error is computed by the L2 norm of the diﬀerence between the numerical solution and one with a reﬁned mesh. Note that in order for the fully discrete numerical scheme to be positivity-preserving, one has to use the positivity-preserving spatial discretization, for example, the positivity-preserving ﬁnite volume WENO scheme [24], which requires a smaller CFL condition and a positivity-preserving limiter. Here since our main focus is to verify the order in time discretization and the AP property, we choose a larger time step and neglect the limiter.

The results are shown in Figures 4 and 5, and one can see similar behavior as in the previous subsection.

3.5.3. The BGK model. We consider the 1D BGK model (41) on the physical domain x ∈ [0,2] with periodic boundary condition, and inconsistent initial data given

10-2

10-2

10-4

10-4

10-6

10-6

error

error

10-8

10-8

|=1<br><br>=0.01<br><br>=0.0001<br><br>=1e-06 =1e-08 =1e-10<br><br><br>slope=2|
|---|


|=1<br><br>=0.01<br><br>=0.0001<br><br>=1e-06 =1e-08 =1e-10<br><br><br>slope=3|
|---|


10-10

10-10

10-12

10-12

10-4 10-3 10-2 10-1

10-4 10-3 10-2 10-1

t

t

Fig. 4. Accuracy test of the new second order IMEX scheme for the Broadwell model.

Fig. 5. Accuracy test of the new third order IMEX scheme for the Broadwell model.

by

- (59) f(0,x,v) = 0.7M[˜ρ(x),u˜(x),T˜(x)](v) + 0.3M[˜ρ(x),−0.5˜u(x),T˜(x)](v), with
- (60) ρ˜(x) = 1 + 0.2sin(2πx), u˜(x) = 1, T˜(x) =


1 1 + 0.2sin(πx)

.

The velocity domain is truncated into [−vmax,vmax] with vmax = 15 and discretized with Nv = 150 grid points, and the physical space is discretized in the same way as

10-2

10-2

10-3

10-3

10-4

10-4

10-5

10-5

10-6

10-6

error

error

10-7

10-7

10-8

10-8

10-9

10-9

|=1<br><br>=0.01<br><br>=0.0001<br><br>=1e-06 =1e-08 =1e-10<br><br><br>slope=2|
|---|


|=1<br><br>=0.01<br><br>=0.0001<br><br>=1e-06 =1e-08 =1e-10<br><br><br>slope=3|
|---|


10-10

10-10

10-11

10-11

10-12

10-12

10-4 10-3 10-2

10-4 10-3 10-2

t

t

Fig. 6. Accuracy test of the new second order IMEX scheme for the BGK model.

Fig. 7. Accuracy test of the new third order IMEX scheme for the BGK model.

### the previous subsection. We ﬁx the the CFL number as ∆t = 21 v∆x

, and solve (41) by the second and third order methods in Subsection 3.3 up to ﬁnal time T = 0.1. The error is computed by the L2 norm (in the (x,v) space) of the diﬀerence between the numerical solution and one with a reﬁned mesh. Note that the velocity space discretization may introduce some additional error such that the Properties 3 and 4 in Subsection 3.4.1 may not hold exactly. Here we chose a large velocity domain truncation and many grid points to make sure that the error from the velocity space discretization is negligible.

max

The results are shown in Figures 6 and 7. For the second order scheme, one can see clearly the second order accuracy when ∆t is small enough (so that the temporal

error dominates) for both ε = O(1) and ε 1, and order reduction is observed in the intermediate regime. For the third order scheme, when ε = O(1) or ε 1, the error converges at a higher than expected rate even for the smallest ∆t in the simulation, which suggests that the spatial error is still dominating. By comparing with the results of the second order scheme we see that the third order scheme indeed gives a much smaller error under the same time-step size.

Finally, to check the AP as well as the positivity-preserving properties, we use the second and third order multi-derivative IMEX methods in Subsection 3.3 to solve a mixed regime problem, i.e., (41) with a variable Knudsen number ε = ε(x) speciﬁed as below. This numerical example is comparable to the numerical result in Section 5.3 of [16].

We take the physical domain as x ∈ [0,2] with periodic boundary condition, and the variable Knudsen number

- (61) ε(x) = ε0 + (tanh(1 − 11(x − 1)) + tanh(1 + 11(x − 1))), ε0 = 10−5,


so that the problem is in the kinetic regime (ε(x) = O(1)) near x = 1, and in the ﬂuid regime (ε(x) ≈ 10−5) for x away from 1. The initial data is taken the same as eqs. (5.1)-(5.2) in [16]. The ﬁnal time is taken as T = 0.5. For the new multiderivative IMEX methods, we discretize the physical space by the ﬁfth order ﬁnite volume WENO scheme with positivity-preserving limiters in [24], and the velocity space is discretized in the same way as before. The variable Knudsen number is treated by a Gauss-Legendre quadrature in each spatial cell in the same way as Section 3.3.3 of [16]. We take Nx = 40 and ∆t = 241 v∆x

to satisfy the positivity-preserving CFL condition.

max

In the simulation we tracked the numerical values (cell averages in the physical space) of f, and no negative cell is observed. The numerical solutions are compared with a reference solution obtained by the explicit second-order SSP-RK scheme with Nx = 80 and ∆t = 2401 v∆x

≈ 7 × 10−6, for which the smallest value of the Knudsen number (around 10−5) is resolved. The result is shown in Figure 8, in terms of the macroscopic quantities. One can see good agreement between the solution by the new schemes and the reference solution. This veriﬁes the AP and positivity-preserving properties of the new multi-derivative IMEX methods.

max

4. Conclusions. In this work, we presented a class of unconditionally SSP implicit multi-derivative Runge–Kutta schemes. The unconditional SSP methods of order p > 2 are novel, and is enabled by the backward derivative condition. This condition is an alternative to the second derivative conditions given in [6, 12], and is highly relevant to a range of problems, as shown in Section 3.4.1.

The new backward derivative condition, which enabled the unconditionally SSP schemes, were inspired by the work in [16] which derived positivity preserving and asymptotic preserving IMEX Runge–Kutta methods with a derivative correction term. We formulate multi-derivative implicit-explicit (IMEX) Runge–Kutta methods that allow us to obtain order p > 2 and to ensure that the method is positivity preserving and asymptotic preserving when applied to problems that satisfy the ﬁve properties in Subsection 3.4.1. In particular, we focus on an application area that includes a hyperbolic relaxation model, the Broadwell model, and the BGK kinetic equation. Such methods require treatment with an implicit-explicit (IMEX) time-stepping approach, and it is desired that the method be AP and positivity preserving.

We derived and presented order conditions for SSP IMEX multi-derivative Runge– Kutta methods, and devised implicit methods that achieve fourth order, and IMEX

0.88

0.55

|reference 2nd order 3rd order<br><br>|
|---|


0.86

0.84

0.5

0.82

0.8

0.45

0.78

0.76

0.4

0.74

0.72

0.7

0.35

0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2

0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2

u

2.1

2

1.9

1.8

1.7

1.6

1.5

| | | |
|---|---|---|
| | | |


1.4

1.3

1.2

1.1

0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2

T

Fig. 8. The mixed regime problem for the BGK model. Top left: density ρ; top right: bulk velocity u; bottom: temperature T. Asterisks/circles: numerical solutions by the new second/third order schemes. Solid line: the reference solution. The numerical solutions of the two new schemes are very close to each other because the spatial error is dominating.

methods that are third order, and are SSP under a time-step restriction independent of the stiﬀ term. The SSP condition ensures that the multi-derivative IMEX schemes are positivity preserving, and we present suﬃcient conditions under which such methods are also asymptotic preserving when applied to the problems of interest. While we focused in the numerical examples on the IMEX schemes applied to a hyperbolic relaxation system, the Broadwell model, and the BGK equation, we stress that the results in this paper are of broad use. Any problems with operators that satisfy the forward Euler and – if handled implicitly – the backward derivative condition can beneﬁt from these methods which are SSP with a time-step that does not depend on the function handled implicitly.

Appendix A. Unconditionally SSP implicit methods. Previously, explicit SSP two-derivative methods were developed that preserved the forward Euler (2) and second derivative (4) conditions [6] or the forward Euler (2) and Taylor series (5) conditions [12]. Methods that preserve the strong stability properties of these conditions require nonnegative coeﬃcients on the prior stages, the function, and its derivative [6, 12]. In other words, we require that (elementwise)

- (62) Re ≥ 0, P ≥ 0, D ≥ 0, D˙ ≥ 0.


We show here that a method of the form (10) that satisﬁes the conditions (62) cannot be second order. This is simply a restatement of the proof in [11] in the current notation.

The ﬁrst and second order conditions are

1 2

bTe = 1, bTc + b˙ Te =

.

Recall that bT is the ﬁnal row of A, and that c is the row sum of A. Note that the matrix A = R−1D = (I − P)−1 D can be written as

A = (I + P + P2 + ... + Ps−1)D, a consequence of the fact that P is strictly lower triangular and so Ps becomes zero. Let’s look at each row of Ae and Ac using the recursive nature of the matrix multiplication: The ﬁrst row is simply (Ae)1 = D11 and (Ac)1 = D211, the other rows are:

- i−1
- j=1


- i−1
- j=1


pij (Ac)j .

pij (Ae)j (Ac)i = Dii(Ae)i +

(Ae)i = Dii +

For any real number a the ﬁrst row satisﬁes

(1 − a)(Ae)1 − (Ac)1 = (1 − a)D11 − D211 ≤ k1(1 − a)2 where k1 = 41. We deﬁne

1 4(1 − ki−1)

ki =

,

and observe that 14 = k1 < k2 < ...ks < 12. Now we can show recursively that if

(1 − a)(Ae)j − (Ac)j ≤ kj(1 − a)2, ∀j < i then

 Dii +

  −

 Dii(Ae)i +

 

- i−1
- j=1


- i−1
- j=1


(1 − a)(Ae)i − (Ac)i = (1 − a)

pij (Ae)j

pij (Ac)j

- i−1
- j=1


= (1 − a)Dii − Dii(Ae)i +

pij (1 − a)(Ae)j − (Ac)j

- i−1
- j=1


- i−1
- j=1


= (1 − a)Dii − D2ii − Dii

pij (1 − a)(Ae)j − (Ac)j

pij (Ae)j +

- i−1
- j=1


= (1 − a)Dii − D2ii +

pij (1 − a − Dii)(Ae)j − (Ac)j

< (1 − a − Dii)Dii + ki−1 (1 − a − Dii)2 .

We look at this ﬁnal term and observe that it obtains a minimum at

(1 − a)(2ki−1 − 1) ki−1 − 1

- 1

- 2


Dii =

,

so that

1 4(1 − ki−1)

(1 − a)2 = ki(1 − a)2. Using the value a = 0 and looking at the ﬁnal row i = s we obtain

(1 − a)(Ae)i − (Ac)i ≤

- 1

- 2


bTe − bTc = (Ae)s − (Ac)s ≤ ks <

. If the method is at least ﬁrst order, we must then have

- 1

- 2


- 1

- 2


bTc > bTe −

. We can then conclude that if

=

- 1

- 2


bTc + b˙ Te =

and all the coeﬃcients of A are non-negative, then b˙ must have negative coeﬃcients or the method cannot be second order.

This argument above shows that the conditions on the method lead to negative coeﬃcients, and as both the forward Euler condition and either the second derivative or Taylor series condition require positive coeﬃcients on both the function and its derivative, the resulting method is not SSP. Thus, implicit multi-derivative Runge– Kutta methods cannot be unconditionally SSP in the sense of preserving the forward Euler and one of the derivative conditions above. This leads us to consider the backward derivative condition.

REFERENCES

- [1] P. Bhatnagar, E. Gross, and M. Krook, A model for collision processes in gases. I. Small amplitude processes in charged and neutral one-component systems, Phys. Rev., 94 (1954), pp. 511–525.
- [2] S. Boscarino, L. Pareschi, and G. Russo, Implicit-explicit Runge-Kutta schemes for hyperbolic systems and kinetic equations in the diﬀusion limit, SIAM J. Sci. Comput., 35 (2013), pp. A22–A51.
- [3] J. Broadwell, Shock structure in a simple discrete velocity gas, Phys. Fluids, 7 (1964), pp. 1013–1037.
- [4] C. Cercignani, The Boltzmann Equation and Its Applications, Springer-Verlag, New York, 1988.
- [5] G.-Q. Chen, C. D. Levermore, and T.-P. Liu, Hyperbolic conservation laws with stiﬀ relaxation terms and entropy, Commun. Pure Appl. Math., XLVII (1994), pp. 787–830.
- [6] A. Christlieb, S. Gottlieb, Z. Grant, and D. C. Seal, Explicit strong stability preserving multistage two-derivative time-stepping schemes, Journal of Scientiﬁc Computing, 68(3)

(2016), pp. 914–942.

- [7] S. Conde, S. Gottlieb, Z. Grant, and J. Shadid, Implicit and implicit-explicit strong stability preserving Runge–Kutta methods with high linear order, Journal of Scientiﬁc Computing, 73(2) (2017), pp. 667–690.
- [8] G. Dimarco and L. Pareschi, Asymptotic preserving implicit-explicit Runge-Kutta methods for nonlinear kinetic equations, SIAM J. Numer. Anal., 51 (2013), pp. 1064–1087.
- [9] , Implicit-explicit linear multistep methods for stiﬀ kinetic equations, SIAM J. Numer. Anal., 55 (2017), pp. 664–690.

- [10] S. Gottlieb, D. Ketcheson, and C.-W. Shu, Strong Stability Preserving Runge-Kutta and Multistep Time Discretizations, World Scientiﬁc, 2011.


- [11] S. Gottlieb, C.-W. Shu, and E. Tadmor, Strong stability-preserving high-order time discretization methods, SIAM Rev., 43 (2001), pp. 89–112.
- [12] Z. Grant, S. Gottlieb, and D. Seal, A strong stability preserving analysis for explicit multistage two-derivative time-stepping schemes based on taylor series conditions, Communications on Applied Mathematics and Computation, 1 (2019), pp. 21–59.
- [13] I. Higueras, Strong stability for additive Runge-Kutta methods, SIAM J. Numer. Anal., 44

(2006), pp. 1735–1758.

- [14] I. Higueras and T. Roldan, Positivity-preserving and entropy-decaying IMEX methods, Monograﬁas del Seminario Matematico Garcia de Galdeano, 33 (2006), pp. 129–136.
- [15] J. Hu and R. Shu, A second-order asymptotic-preserving and positivity-preserving exponential Runge-Kutta method for a class of stiﬀ kinetic equations, Multiscale Model. Simul., 17

(2019), pp. 1123–1146.

- [16] J. Hu, R. Shu, and X. Zhang, Asymptotic-preserving and positivity-preserving implicit-explicit schemes for the stiﬀ BGK equation, SIAM J. Numer. Anal., 56 (2018), pp. 942–973.
- [17] J. Huang and C.-W. Shu, A second-order asymptotic-preserving and positivity-preserving discontinuous Galerkin scheme for the Kerr-Debye model, Math. Models Methods Appl. Sci., 27 (2017), pp. 549–579.
- [18] S. Jin, Eﬃcient asymptotic-preserving (AP) schemes for some multiscale kinetic equations, SIAM J. Sci. Comput., 21 (1999), pp. 441–454.
- [19] C. A. Kennedy and M. H. Carpenter, Diagonally implicit runge-kutta methods for ordinary diﬀerential equations. a review, NASA Technical Report, NASA/TM–2016–219173 (2016).
- [20] D. I. Ketcheson, Step sizes for strong stability preserving with downwind-biased operators, SIAM Journal on Numerical Analysis, 49 (2011), pp. 1649–1660.
- [21] L. Pareschi and G. Russo, Implicit-explicit Runge-Kutta methods and applications to hyperbolic systems with relaxation, J. Sci. Comput., 25 (2005), pp. 129–155.
- [22] C.-W. Shu, Total-variation diminishing time discretizations, SIAM Journal on Scientiﬁc Statistical Computing, 9 (1988), p. 1073–1084.
- [23] C.-W. Shu and S. Osher, Eﬃcient implementation of essentially non-oscillatory shockcapturing schemes, Journal of Computational Physics, 77 (1988), p. 439–471.
- [24] X. Zhang and C.-W. Shu, On maximum-principle-satisfying high order schemes for scalar conservation laws, J. Comput. Phys., 229 (2010), pp. 3091–3120.


