---
type: source
kind: paper
title: Two-derivative error inhibiting schemes with post-processing
authors: Adi Ditkowski, Sigal Gottlieb, Zachary J. Grant
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/1912.04159v1
source_local: ../raw/2019-ditkowski-two-derivative-error-inhibiting-schemes.pdf
topic: general-knowledge
cites:
---

arXiv:1912.04159v1[math.NA]9Dec2019

TWO-DERIVATIVE ERROR INHIBITING SCHEMES WITH POST-PROCESSING

ADI DITKOWSKI∗, SIGAL GOTTLIEB†, AND ZACHARY J. GRANT‡

Abstract. High order methods are often desired for the evolution of ordinary diﬀerential equations, in particular those arising from the semi-discretization of partial diﬀerential equations. In prior work in we investigated the interplay between the local truncation error and the global error to construct error inhibiting general linear methods (GLMs) that control the accumulation of the local truncation error over time. Furthermore we deﬁned suﬃcient conditions that allow us to post-process the ﬁnal solution and obtain a solution that is two orders of accuracy higher than expected from truncation error analysis alone. In this work we extend this theory to the class of two-derivative GLMs. We deﬁne suﬃcient conditions that control the growth of the error so that the solution is one order higher than expected from truncation error analysis, and furthermore deﬁne the construction of a simple post-processor that will extract an additional order of accuracy. Using these conditions as constraints, we develop an optimization code that enables us to ﬁnd explicit two-derivative methods up to eighth order that have favorable stability regions, explicit strong stability preserving methods up to seventh order, and A-stable implicit methods up to ﬁfth order. We numerically verify the order of convergence of a selection of these methods, and the total variation diminishing performance of some of the SSP methods. We conﬁrm that the methods found perform as predicted by the theory developed herein.

1. Introduction. The celebrated Lax-Richtmeyer equivalence theorem ([21], [12], [29]) states that if the numerical scheme is stable then its global error is at least of the same order as its local truncation error. Indeed, it is the common experience that the frequently used methods produce solutions that have global error of the same order as the normalized local truncation error. Indeed, the Dahlquists Equivalence Theorem [35] states this fact for linear multistep methods. In fact, this behavior is so expected for all one-step and multistep methods that we typically deﬁne the order of a stable numerical method solely by the order conditions derived by Taylor series analysis of the local truncation error. This relationship between the order of the local truncation error and global error is also seen in ﬁnite diﬀerence schemes for partial diﬀerential equations (PDEs) [12, 29]. Work over the past decade reminds us that, while for a stable scheme the global error must at least of the same order as its local truncation error, it may in fact be of higher order.

In this paper we consider numerical solvers for ordinary diﬀerential equations (ODEs) of the form

ut = F(t,u) , t ≥ 0 u(t0) = u0.

(where we assume F(t,u) is at least continuous with respect to t and Lipschitzcontinuous with respect to u, and typically much smoother). Without loss of generality [14], we focus our attention on the autonomous ODE

- (1) ut = F(u) , t ≥ 0 u(t0) = u0.


![image 1](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile1.png>)

∗School of Mathematical Sciences, Tel Aviv University, Tel Aviv 69978, Israel. Email: adid@post.tau.ac.il

†Mathematics Department, University of Massachusetts Dartmouth, 285 Old Westport Road, North Dartmouth MA 02747. Email: sgottlieb@umassd.edu

‡Department of Computational and Applied Mathematics, Oak Ridge National Laboratory, Oak Ridge TN 37830. Email: grantzj@ornl.gov

The canonical numerical method for this problem is the forward Euler method vn+1 = vn + ∆tF(vn) ,

where vn approximates the exact solution at time tn and we let v0 = u0. The forward Euler method has local truncation error LTEn and its approximation error τn at any given time tn deﬁned by

τn = ∆tLTEn = u(tn−1) + ∆tF(u(tn−1)) − u(tn) ≈ O(∆t2) and it produces a global error which is ﬁrst order accurate

en = vn − u(tn) ≈ O(∆t).

To develop methods that have higher order, we can add steps and deﬁne a linear multistep method [3], use multiple stages as in a Runge–Kutta methods [3], or include higher derivatives as we do in Taylor series methods [3]. We can also combine the approaches above: the combination of multiple steps and stages is commonly see as in the general linear methods described in [2, 14], and multiple derivatives and stages have also been used [4, 5, 10, 23, 24, 27, 30]. In all these cases the goal is to increase the order of the local truncation error and therefore of the global error. All these approaches typically produce methods that have global errors that are of the same order as their local truncation errors.

It is, however, possible in some cases to devise schemes that have global errors that are higher order than predicted by the local truncation errors. Kulikov (for Nordsiek methods) [18] and by Weiner and colleagues [40] (for explicit two-step peer methods) followed along the lines of the quasi-consistency theory ﬁrst introduced by Skeel in 1978 [31] to ﬁnd methods that have solution of order p + 1 although their truncation errors are of order p. In [6] Ditkowski and Gottlieb derived suﬃcient conditions for a family of general linear methods (GLMs) of any number of steps and stages under which one can control the accumulation of the local truncation error over time evolution and produce methods that are one order higher than expected from the truncation error alone. A similar theory was developed for implicit-explicit methods in [34]. In [19], [39], and [20], it was shown that under additional conditions on the method the precise form of the ﬁrst surviving term in the global error (the vector multiplying ∆tp+1) can be computed explicitly and leveraged for error estimation. In [7] Ditkowski, Gottlieb, and Grant showed that under less restrictive conditions the form of the ﬁrst surviving term in the global error can be computed explicitly and exploited to enhance the accuracy to order p + 2, using post-processing.

In this paper, we extend the error inhibiting approach to methods that have multiple steps, multiple stages, and two derivatives. In Section 3.1 we show that the theory developed in [7] carries through easily to such methods, and by imposing the same EIS+ conditions as in [7] on on the two-derivative GLMs we consider we can not only produce solutions with accuracy one order higher than predicted by truncation error analysis but also precisely describe the leading coeﬃcients of the error term. This allows us to post-process the ﬁnal time solution and obtain a global error that is two orders higher than the local truncation error. The construction of the postprocessor is exactly the same as in [7] and we review it in Section 3.2. We proceed to devise error inhibiting two-step GLMs this new EIS approach, present these methods

- in Section 4, and in Section 5 we test a selection of these methods on numerical examples to demonstrate their enhanced accuracy properties.


2. Two-derivative methods. Multiderivative Runge–Kutta methods, particularly two-derivative methods, were ﬁrst considered in [25, 38, 36, 32, 33, 15, 16, 23, 27, 4], and later explored for use with partial diﬀerential equations (PDEs) [30, 37, 22, 28, 8]. Recent interest in exploring the strong-stability properties of multiderivative Runge–Kutta methods, (also known as multistage multiderivative methods) is evident in [5, 10, 24]. A 2015 work by Okuonghae and Ikhile [26] discussed twoand three-derivatives methods with multiple stages and steps. These two-derivative general linear methods (GLMs) are similar to those in this work. (Also cite the paper Zack refereed and look in there for references)

2.1. Essentials. In this work we consider the class of two-derivative general linear methods (GLMs) of the form

- (2) V n+1 = DV n + ∆tAF(V n) + ∆tRF(V n+1) + ∆t2AˆF˙(V n) + ∆t2RˆF˙(V n+1),

where V n is a vector of length s that contains the numerical solution at times (tn + cj∆t) for j = 1,...,s:

- (3) V n = (v(tn + c1∆t)),v(tn + c2∆t),...,v(tn + cs∆t))T .

The function F(V n) is deﬁned as the component-wise function evaluation on the vector V n:

- (4) F(V n) = (F(v(tn + c1∆t)),F(v(tn + c2∆t)),...,F(v(tn + cs∆t)))T , and, similarly, the function F˙(V n) is
- (5) F˙(V n) =

dF dt

![image 2](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile2.png>)

(v(tn + c1∆t)),

dF dt

![image 3](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile3.png>)

(v(tn + c2∆t)),...,

dF dt

![image 4](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile4.png>)

(v(tn + cs∆t))

T

.

For convenience, we select c1 = 0 so that the ﬁrst element in the vector V n approximates the solution at time tn, and the abscissas are non-decreasing c1 ≤ c2 ≤ ... ≤ cs. To initialize these methods, we deﬁne the ﬁrst element in the initial solution vector V10 = u(t0) and the remaining elements v(t0 + cj∆t) are computed using some highly accurate method.

We deﬁne the corresponding projection of the exact solution of the ODE (1) onto the temporal grid:

- (6) Un = (u(tn + c1∆t),u(tn + c2∆t),...,u(tn + cs∆t))T ,

where F(Un) and F˙(Un) are the component-wise function evaluation on the vector Un. We deﬁne the global error as the diﬀerence between the vectors of the exact and the numerical solutions at some time tn

- (7) En = V n − Un.

Methods of the form (2) have a local truncation error at time tn that is related to the approximation error τn

- (8) ∆t LTEn = τn = DUn−1 + ∆tAF(Un−1) + ∆tRF(Un) − Un where
- (9) τn =


∞

∞

dju dtj t=t

τj∆tj

τnj ∆tj =

![image 5](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile5.png>)

j=0

j=0

3 n

where the truncation error vectors τj have the form

- (10a) τ0 = (D − I)1


1 j

1 (j − 1)!

- (10b) D(c − 1)j + A(c − 1)j−1 + (j − 1)Aˆ (c − 1)j−2

+ Rcj−1 + (j − 1)Rcˆ j−2 −

1 j

![image 6](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile6.png>)

cj for j=1,2, ....

Here, c = (c1,c2,...,cs)T is the vector of abscissas and 1 = (1,1,...,1)T is the vector of ones, and the terms cj are understood component-wise cj = (cj1,cj2,...,cjs)T. For a method to have order p it must satisfy the order conditions

τj = 0 j ≤ p.

Note that the form (2) includes both explicit and implicit schemes, as V n+1 appears on both sides of the equation. However, if R and Rˆ are both strictly lower triangular the scheme is explicit. We are only interested in zero-stable methods. A suﬃcient condition for this is that the coeﬃcient matrix D is a rank one matrix that has row sum one (i.e. satisﬁes the consistency condition). For simplicity we assume this to be the case in this the remainder of this work.

2.2. Preliminaries. In this subsection we make some observations that will be useful in the remainder of the paper. In all the following we assume suﬃcient smoothness of all the quantities such as F,F˙ etc. Furthermore, we assume that he order conditions τj = 0 hold for all j = 0,...,p, and that we are in the asymptotic regime so that the errors are small and we can say that En ≤ O(∆tp) << 1.1

- Observation 1 We observe that


- (11) F(Un + En) = F(Un) + FynEn + O(∆t)En,


τj =

![image 7](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile7.png>)

![image 8](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile8.png>)

where Fyn = Fy(u(tn)).

Proof. This is simply due to the fact that F is smooth enough that it can be expanded:





Fy(u(tn + c1∆t))en+c

- 1

Fy(u(tn + c2∆t))en+c

- 2


+ O En 2 ,

F(Un + En) = F(Un) +

 

 

. Fy(u(tn + cs∆t))en+c

s





Fn+c

y 1 0 ··· 0 0 Fn+c y 2 ··· 0

En + O En 2 ,

= F(Un) +

 

 

... . 0 0 ··· Fn+c

. .

y s

)T, and we use the notation Fyn+cj = Fy(u(tn + cj∆t)). Each term can be expanded as

where the error vector is En = (en+c

,...,en+c

,en+c

s

2

1

y = Fy(u(tn + cj∆t)) = Fy(u(tn)) + cj∆tFyy(u(tn)) + O(∆t2)

Fn+c

j

![image 9](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile9.png>)

1We will verify that this is reasonable in Lemma 2

so that, exploiting the smoothness of Fyy we have

F(Un + En) = F(Un) + FynI + O(∆t) En + O En 2 , which, due to the fact that En ≤ O(∆tp) becomes

F(Un + En) = F(Un) + FynEn + O(∆t)En.

![image 10](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile10.png>)

![image 11](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile11.png>)

![image 12](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile12.png>)

![image 13](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile13.png>)

- Observation 2 Given the smoothness of F˙, we observe that


- (12) F˙(Un + En) = F˙(Un) + F˙ynEn + O(∆t)En,

where F˙yn = F˙y(u(tn)).

Proof. The proof of this observation is exactly the same as above, with the assumption that F˙ is smooth enough to be expanded.

![image 14](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile14.png>)

![image 15](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile15.png>)

![image 16](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile16.png>)

![image 17](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile17.png>)

We use these observations to develop an equation that describes the growth of the error:

Lemma 1. Given a zero-stable method of the form (2) which satisﬁes the order conditions

τj = 0 for j = 0,...,p

and where the functions F and F˙ are smooth, the evolution of the error can be described by:

- (13) I − ∆tRFyn + O(∆t2) En+1 = D + ∆tAFyn + O(∆t2) En + τn+1. Proof. Recall that


τn+1 = DUn + ∆tAF(Un) + ∆t2AˆF˙(Un) + ∆tRF(Un+1) + ∆t2RˆF˙(Un+1) − Un+1. and use this equation to subtract Un+1 from

V n+1 = DV n + ∆tAF(V n) + ∆t2AˆF˙(V n) + ∆tRF(V n+1) + ∆t2RˆF˙(V n+1) obtaining

V n+1 − Un+1 = DV n − DUn + ∆tA(F(V n) − F(Un))

+∆t2Aˆ F ˙(V n) − F˙(Un) + ∆tR F(V n+1) − F(Un+1)

+∆t2Rˆ F ˙(V n+1) − F˙ (Un+1) + τn+1 using Observations 1 and 2 we have

En+1 = D(Un + En) − DUn + ∆tA(F(Un + En) − F(Un))

+∆t2Aˆ F ˙(Un + En) − F˙(Un) + ∆tR F(Un+1 + En+1) − F(Un+1)

+∆t2Rˆ F ˙(Un+1 + En+1) − F˙(Un+1) + τn+1

= DEn + ∆t AFyn + O(∆t) En + ∆t2 F ˙ynAˆ + O(∆t) En

+∆t RFyn+1 + O(∆t) En+1 + ∆t2 F ˙yn+1Rˆ + O(∆t) En+1 + τn+1,

so that

En+1 = DEn + ∆tAFynEn + ∆tRFyn+1En+1 + ∆t2Aˆ F˙ynEn + ∆t2Rˆ F˙yn+1En+1

+O(∆t2)En + O(∆t2)En+1 + τn+1.

Note that Fyn,F˙yn,Fyn+1, and F˙yn+1 are all scalars. Now recall that O(∆t)O( En ) < O(∆t2) since p ≥ 1, and that terms of the form Rˆ Fyn+1 and Aˆ Fyn are all bounded, so we have

En+1 = DEn + ∆tAFynEn + ∆tRFyn+1En+1 + O(∆t2)En + O(∆t2)En+1. Now move the En+1 terms to the left side:

I − ∆tRFyn+1 + O(∆t2) En+1 = DEn + ∆tAFynEn + O(∆t2) + τn+1. Noting that Fyn+1 = Fyn + O(∆t) we have the desired result

I − ∆tRFyn + O(∆t2) En+1 = D + ∆tAFyn + O(∆t2) En + τn+1.

![image 18](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile18.png>)

![image 19](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile19.png>)

![image 20](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile20.png>)

![image 21](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile21.png>)

We now turn to verifying that the assumption we made in the ﬁrst paragraph of this subsection, that we can assume that the error En is small:

Lemma 2. Given a zero-stable scheme (2), if the order conditions τj = 0 are satisﬁed for j = 0,...,p, and R and Fyn are bounded, then there is some time interval

- [0,T] such that the error En (given by (13) ) satisﬁes En ≤ O(∆tp) << 1.


The proof of this Lemma is given in [7], Lemma 3.

3. Designing multi-derivative error inhibiting schemes that can be postprocessed to order p + 2. In this section we show how to construct two-derivative GLMs of the form (2) that are error inhibiting and so produce a solution of order p + 1 even though one would only expect order p from their truncation errors. We further show that under additional conditions we can express the exact form of the error and deﬁne an associated post-processor that allow us to recover order p+2 from a scheme that would otherwise be only pth order accurate.

3.1. Two-derivative error inhibiting schemes that have p + 1 order. In this section we consider a multi-derivative GLM of the form (2) where we assume that D is a rank one matrix that satisﬁes the consistency condition D1 = 1 so that this scheme is zero-stable. Furthermore, we assume that the coeﬃcient matrices D, A, R, Aˆ, Rˆ are such that the order conditions τj = 0 are satisﬁed for all j ≤ p, so that the method will give us a numerical solution that has error that is guaranteed of order p. In the following theorem we show that if the truncation error vector τp+1 lives in the null-space of the operator D the order of the error can be shown to be of order p + 1. Furthermore, the theorem shows that under additional conditions on the coeﬃcient matrices D, A, R, Aˆ, Rˆ, we can determine precisely what the leading term of this error will look like and therefore remove it by post-processing.

Theorem 1. Given a zero-stable two-derivative general linear method of the form V n+1 = DV n + ∆tAF(V n) + ∆tRF(V n+1) + ∆t2AˆF˙(V n) + ∆t2RˆF˙(V n+1)

where D is a rank one matrix that satisﬁes the consistency condition D1 = 1, and the coeﬃcient matrices D, A, R, Aˆ, Rˆ satisfy the order conditions

τj = 0 for j = 1,...,p, where

1 (j − 1)!

1 j

D(c − 1)j + A(c − 1)j−1 + (j − 1)Aˆ (c − 1)j−2

τj =

![image 22](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile22.png>)

![image 23](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile23.png>)

1 j

+ Rcj−1 + (j − 1)Rcˆ j−2 −

cj for j=1,2, ..., if the error inhibiting condition

![image 24](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile24.png>)

- (14a) Dτp+1 = 0 is satisﬁed, then the numerical solution produced by this method will have error

En = O(∆tp+1). Furthermore, if the conditions

- (14b) Dτp+2 = 0
- (14c) D(A + R)τp+1 = 0 are also satisﬁed, then error vector will have the more precise form:


- (15) En = ∆tp+1τnp+1 + O(∆tp+2). Proof. Using Lemma 1 we obtain the equation for the evolution of the error
- (16) En+1 = I − ∆tRFyn + O(∆t2) −1 D + ∆tAFyn + O(∆t2) En + τn+1

the fact F is smooth assures us that ∆tRFyn << O(1) so that we can expand the ﬁrst term to obtain

En+1 = I + ∆tRFyn + O(∆t2) [ D + ∆tAFyn + O(∆t2) En + τn+1]

= D + ∆tFyn(RD + A) + O(∆t2) En

+∆t ∆tpτnp+1+1 + ∆tp+1(τnp+2+1 + FynRτnp+1+1) + O(∆t2)

= QnEn + ∆tTen. The discrete Duhamel principle (given as Lemma 5.1.1 in [12]) states that given an iterative process of the form

En+1 = QnEn + ∆tTen where Qn is a linear operator, we have

- (17) En =


n−1

n−1

n−1

QµE0 + ∆t

Qµ Teν .

µ=ν+1

µ=0

ν=0

To analyze the error, we separate it into four parts:

En =

n−1

+ ∆tTen−1

QµE0

+ ∆tQn−1Ten−2

![image 25](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile25.png>)

![image 26](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile26.png>)

![image 27](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile27.png>)

![image 28](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile28.png>)

µ=0

II

III

![image 29](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile29.png>)

![image 30](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile30.png>)

I

and discuss each part separately:

n−3

+ ∆t

ν=0

![image 31](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile31.png>)

IV

n−1

Qµ Teν

µ=ν+1

![image 32](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile32.png>)

- I. The method is initialized so that the numerical solution vector V 0 is accurate enough to ensure that the initial error E0 is negligible and we can ignore the ﬁrst term.
- II. The ﬁnal term in the summation is ∆tTen−1. Recall that Ten−1 = ∆tpτnp+1 + ∆tp+1(τnp+2 + Fyn−1Rτnp+1) + O(∆tp+2)

so that this term contributes to the ﬁnal time error the term ∆tTen−1 = ∆tp+1τnp+1 + O(∆tp+2).

- III. The term ∆tQn−1Ten−2 is a product of the operator Qn−1 = D + ∆tFyn−1(RD + A) + O(∆t2)

and the approximation error

Ten−2 = ∆tpτpn+1−1 + ∆tp+1(τpn+2−1 + Fyn−2Rτpn+1−1) + O(∆tp+2) , so we obtain

Qn−1Ten−2 = ∆tpDτpn+1−1 + O(∆tp+1) = O(∆tp+1),

due to the condition (14a) that states that Dτp+1 = 0. Looking more closely at the O(∆tp+1) terms that remain in this product and applying (14a) again

D(τpn+2−1 + Fyn−2Rτpn+1−1) + Fyn−1(RD + A)τpn+1−1 + O(∆t) = D(τpn+2−1 + Fyn−2Rτpn+1−1) + Fyn−1Aτpn+1−1 + O(∆t) = D(τpn+2−1 + Fyn−1Rτpn+1−1) + Fyn−1Aτpn+1−1 + O(∆t) = Dτpn+2−1 + Fyn−1(DR + A)τpn+1−1 + O(∆t)

where we used the observation that Fyn−2 = Fyn−1 + O(∆t). The product is then

Qn−1Ten−2 = ∆tp+1 Dτpn+2−1 + Fyn−1(DR + A)τpn+1−1 + O(∆tp+2), we now use the two error inhibiting conditions (14b) and (14c) to obtain

Qn−1Ten−2 = O(∆tp+2).

- IV. Finally we look at the rest of the sum and use the boundedness of the operator Qn to observe


n−3

∆t

ν=0

n−1

Qµ Teν = ∆t

µ=ν+1

n−3

≤ ∆t

ν=0

n−3

ν=0

n−1

Qˆµ Q ˆν+2Qˆν+1Teν

µ=ν+3

n−1

Qµ Qν+2Qν+1Teν

µ=ν+3

n−3

(1 + c ∆t)n−ν−3 Qν+2Qν+1Teν

≤ ∆t

ν=0

exp(ctn) − 1 c

Qν+2Qν+1Teν .

=

max

![image 33](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile33.png>)

ν=0,...,n−3

Clearly, the ﬁrst term here is a constant that depends only on the ﬁnal time, so it is the product Qν+2Qν+1Teν we need to bound. Using the deﬁnition of the operators Qµ

Qν+2Qν+1 = D2 + ∆t Fyν+2 (RD + A)D + Fyν+1D(RD + A) + O(∆t2) and the approximation error

Teν = ∆tpτνp+1+1 + ∆tp+1(τνp+2+1 + FyνRτνp+1+1) + O(∆tp+2) we have

Qν+2Qν+1Teν = ∆tp D + ∆tFyν+2 (RD + A) + ∆tFyν+1DR Dτνp+1+1

+ ∆tp+1 Fyν+1D2R + Fyν+1DA τνp+1+1 + ∆tp+1D2τνp+2+1 + O(∆tp+2).

Using the fact that in our case D2 = D and that Fyν+2 = Fyν+1 + O(∆t) we obtain

Qν+2Qν+1Teν = ∆tp D + ∆tFyν+2 (RD + A) + ∆tFyν+1DR Dτνp+1+1

+ ∆tp+1Fyν+1D(R + A) τνp+1+1 + ∆tp+1Dτνp+2+1 + O(∆tp+2). The ﬁrst term and third terms disappear because of (14a) and (14b)

Dτp+1 = 0 and Dτp+2 = 0. The second term is eliminated by (14c)

D(R + A) τp+1 = 0. So that

Qν+2Qν+1Teν = O(∆tp+2). All these parts together give us the result

n−1

n−1

+ ∆tQn−1Ten−2

QµE0

+ ∆tTen−1

En =

+ ∆t

![image 34](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile34.png>)

![image 35](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile35.png>)

![image 36](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile36.png>)

![image 37](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile37.png>)

ν=0

µ=0

II

III

![image 38](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile38.png>)

![image 39](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile39.png>)

![image 40](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile40.png>)

I

IV

= 0 + ∆tp+1τnp+1

+ O(∆tp+2)

+ O(∆tp+2)

![image 41](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile41.png>)

![image 42](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile42.png>)

![image 43](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile43.png>)

![image 44](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile44.png>)

![image 45](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile45.png>)

![image 46](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile46.png>)

III

IV

II

- (18) = ∆tp+1τnp+1 + O(∆tp+2).


n−3

Qµ Teν

µ=ν+1

![image 47](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile47.png>)

![image 48](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile48.png>)

![image 49](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile49.png>)

![image 50](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile50.png>)

![image 51](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile51.png>)

Remark 1. We note that generalizing this approach from our work in [7] to include a second derivative was quite simple. This is due to the fact that the second derivative appears with a ∆tp+2 term multiplying it, so that the operator Qn is in fact exactly the same for a two-derivative method of the form (2) as for the methods considered in [7]. For this reason, expanding this approach to higher derivatives will be simple: the only change would be in the deﬁnition of the order conditions (10).

3.2. Designing a post-processer to recover p+2 order. At every time-step

- tn the error vector En has the particular form (15) En = ∆tp+1τnp+1 + O(∆tp+2),


so that the leading order term ∆tp+1τnp+1 can be removed by post-processing at the end of the computation and a ﬁnal time solution of order p + 2 can be obtained, as we showed in [7]. We notice that the form of the error for multi-derivative method (2) is exactly the same as that of the error of the EIS methods presented in [7], the only diﬀerence being the deﬁnition of the truncation error vector. The theoretical discussion of this post-processor is presented in [7] and we refer the reader to the presentation there. We review one such construction below:

- 1. Select the number of computation steps m that will be used, requiring that ms ≥ p + 3

where s is the number of steps and p the truncation-error order of the timestepping method.

- 2. Deﬁne the time vector of all the temporal grid points in the last m computation steps:

˜t = (tn−m+1 + c1∆t,...,tn−m+1 + cs∆t,...,tn + c1∆t,...,tn + cs∆t)T

- 3. Correspondingly, concatenate the ﬁnal m solution vectors

V˜n =

  

V n−m+1 . V n

   , and U˜n =

  

Un−m+1 . Un

   .

- 4. Stack m copies of the ﬁnal truncation error vector τp+1

τ˜ =

  τTp+1,...,τTp+1

![image 52](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile52.png>)

![image 53](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile53.png>)

m

  

T

- 5. Deﬁne the vertically ﬂipped Vandermonde interpolation matrix T on the vector ˜t, and replace the ﬁrst column (the one corresponding to the highest polynomial term) by τ˜:

T = τ ˜,˜tms−1,˜tms−2,...,˜t2,˜t,1

where terms of the form ˜tq are understood as component-wise exponentiation. Note that T is a square matrix of dimension ms × ms.

- 6. Deﬁne the post-processing ﬁlter

Φ = T diag

 0,1,...,1

![image 54](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile54.png>)

![image 55](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile55.png>)

ms−1

,

  T−1.

- 7. Finally, left-multiply the solution vector V˜n by the post-processing ﬁlter Φ to obtain the post-processed solution


Vˆn = ΦV˜n, which will be of order p + 2, as shown in [7].

As in [7] we remark that this process may break down if the matrix T is not invertible, and that numerical instabilities may result if Φ is large. This should be veriﬁed while building these matrices.

4. New error inhibiting GLM schemes. In this section we present the new general linear methods (GLMs) that satisfy the error inhibiting conditions (14a)– (14c). We divide these methods into three types: explicit methods that have good linear stability regions, explicit strong stability preserving methods, and implicit methods that are A-stable. The coeﬃcients of all the methods mentioned in this section can be downloaded from our GitHub site [11].

4.1. Explicit EIS methods with favorable linear stability regions. We used the optimization procedure to produce a number of explicit methods with relatively large regions of linear stability. As is usual in this ﬁeld, the linear stability region is deﬁned as the value of the complex number λ so that the method applied to the problem y′ = λy (and so y′′ = λy′ = λ2y) is stable.

We consider two types of explicit methods in this section, and denote them eEIS(s,P)2 and eEIS+(s,P)2. The eEIS(s,P)2 methods have s stages and satisfy the order conditions to some order p and the EIS condition (14a) so that the overall order is P = p + 1. The eEIS+(s,P)2 methods also have s stages and satisfy the order conditions to some order p but they satisfy all three error inhibiting conditions (14a) – (14c) so that the overall order is P = p +2. In this section we present and compare the linear stability regions of some of these methods. Due to space constraints we do not present the coeﬃcients of all the methods. However, in Appendix A we present the coeﬃcients of a selection of the methods that will be used in the numerical tests

- in Section 5, and the coeﬃcients of all methods mentioned in this section can be downloaded from our GitHub site [11].


We begin with an explicit EIS GLM that has s = 2 stages and satisﬁes the truncation error conditions to p = 2 and the EIS condition (14a) so that the overall order is P = 3, and refer to this method as eEIS(2,3)2. In Figure 1 we compare the stability region of this method to that of the ﬁve-stage third order KinmarkGray method eKG(5,3) [17]. The linear stability region of the Kinmark-Gray method eKG(5,3) method, which has ﬁve function evaluations, is shown with the y-axis going from (−5,5), while the eEIS(2,3)2 method, which has four total function evaluations (two evaluations of F and two of F˙), is shown with the y-axis going from (−2s,2s) = (−4,4). Clearly, it seems that the Kinmark-Gray method is more eﬃcient, even considering the extra cost of computing ﬁve function evaluations over four for the eEIS(2,3)2 method. However, the argument for using two-derivative methods is that frequently the second derivative is often needed for other parts of the simulation (e.g. the spatial derivative), and is computed whether or not it is used in the time-stepping. Thus, we can consider the cost of the eEIS(2,3)2 method to be that of two function evaluations rather than four. In this case, the eEIS(2,3)2 has a larger eﬀective linear stability region than the eKG(5,3) method. The coeﬃcients of the eEIS2(2,3) are given in Appendix A while the coeﬃcients of the well-known eKG(5,3) method can be found in [17] or downloaded from our GitHub site [11].

Next, we compare the linear stability regions of EIS(s,P)2 and EIS+(s,P)2 methods we found using our optimization method. In Figure 2 on the left we show the linear stability regions of the two-stage ﬁfth order methods eEIS(2,5)2 method (in

- blue) and the eEIS+(2,5)2 method (in red). In Figure 2 on the right we show the linear stability regions of the three-stage seventh order methods eEIS(3,7)2 method (in
- blue) and the eEIS+(3,7)2 method (in red). In both cases we can see that the linear


4

5

3

2

1

0

- -5 -3 -1 1 3 5

- -5
- -3
- -1


- -4 -2 0 2 4

- -4
- -2


Fig. 1. The linear stability region of the EIS method eEIS(2,3)2 on left compared to that of the Kinmark-Gray method eKG(5,3) on the right.

stability region of the EIS+(s,P)2 is larger than that of the corresponding EIS(s,P)2 method. This suggests that the additional order condition that the EIS(s,P)2 method must satisfy (the EIS(s,P)2 method must satisfy P − 1 conditions instead of P − 2 conditions for the EIS+(s,P)2) play more of a role in constraining the linear stability region than the additional error inhibiting conditions (14b) and (14c) that the EIS+(s,P)2 conditions must satisfy. These results show that from a linear stability perspective, it is more eﬃcient to use the EIS+ methods than the corresponding EIS methods. This is because the cost of one-time post-processing is negligible compared

- to the cost incurred by a restricted time-step which will require many more time-steps to reach the same ﬁnal time.


- 0

- 0.5
- 1


- 1.5
- 2


- 0
- 1
- 2
- 3


- -2 -1.5 -1 -0.5 0 0.5 1 1.5 2

- -2
- -1.5
- -1
- -0.5


- -3
- -2
- -1


-3 -2 -1 0 1 2

Fig. 2. The linear stability region of the EIS(s,P)2 compared to the EIS+(s,P)2 methods. On the left: the stability region of the eEIS(2,5)2 in blue and eEIS+(2,5)2 in red. On the right: the stability region of the and eEIS(3,7)2 in blue and eEIS+(3,7)2 in red.

We now focus on the linear stability regions of some very high order EIS+(s,P)2 methods. These methods are further explored in Section 5 where we test these methods for convergence. The coeﬃcients of these methods are found in Appendix A. Figure 3 shows the linear stability regions of the eEIS+(2,6)2 (left), eEIS+(3,7)2 (middle), and eEIS+(4,8)2 (right) methods. The axis limits are in all cases (−s,s), to account for the increased cost of function evaluations that is proportional to the number of stages. The high order methods eEIS+(3,7)2, and eEIS+(4,8)2 clearly have very favorable regions of linear stability.

- 0
- 1
- 2


- 0
- 1
- 2
- 3
- 4


- 0
- 1
- 2
- 3


- -4 -3 -2 -1 0 1 2 3 4

- -4
- -3
- -2
- -1


- -3
- -2
- -1


- -2
- -1


-2 -1 0 1 2

-3 -2 -1 0 1 2

Fig. 3. The linear stability regions of the eEIS+(2,6)2 (left), eEIS+(3,7)2 (middle), and eEIS+(4,8)2 (right) methods. Note that both the x-axis and y-axis limits are proportional to the number of stages, so that the graph is on (−s, s) × (−s, s). This accounts for the increased cost of function evaluations that is proportional to the number of stages.

4.2. Explicit strong stability preserving EIS methods. The solution to a hyperbolic conservation law may develop sharp gradients or discontinuities, which requires careful handling to ensure that the numerical solution is stable. For this purpose, a spatial discretization is carefully designed to satisfy some nonlinear stability properties (such as total variation diminishing, maximum norm preserving, or positivity preserving properties) to ensure that it can handle the presence of a discontinuity. However, this spatial discretization method must be paired with an appropriate timestepping method to ensure preservation of these nonlinear non-inner-product stability properties [9]. Such time-stepping methods are known as strong stability preserving (SSP) time discretizations [9].

SSP time-stepping methods preserve the nonlinear non-inner-product stability properties of the spatial discretization when coupled with forward Euler, under some time-step restriction

- (19) un + ∆tF(un) ≤ un for ∆t ≤ ∆tFE.

For two derivative methods, preserving the forward Euler condition is not enough: we need to augment this with a condition that includes the second derivative. In this work we consider, as we did in [10] the Taylor series condition

un + ∆tF(un) +

- 1

![image 56](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile56.png>)

- 2


- (20) ∆t2F˙(un) ≤ un for ∆t ≤ K∆tFE,


where K is some constant. (This condition is more general than the one we considered in [5]) The explicit SSP two-derivative GLM methods that we develop in this work can be decomposed into a convex combination of (19) and (20) with K = 1, and thus preserve their strong stability properties under the time-step restriction

∆t ≤ C∆tFE.

Using the optimization code we found a number of two-derivative error inhibiting strong stability preserving (SSP) methods with optimized SSP coeﬃcient C. We denote by eSSP-EIS(s,P)2 the methods that satisfy the order conditions to order

- p = P − 1 and the error inhibiting condition (14a). The methods that satisfy the order conditions to order p = P −2 and satisfy the error inhibiting conditions (14a) –


(14c) are denoted eSSP-EIS(s,P)+2. We present three SSP error inhibiting methods in this section.

Explicit strong stability preserving eSSP-EIS(2,3)2 with C = 1.5. This method satisﬁes the truncation error conditions up to order p = 2 and the EIS condition (14a) so that we obtain third order convergence (P = 3). The coeﬃcients of this

Table 1

A table of SSP coeﬃcients of the error inhibiting methods found and the comparable methods in [1]. A dash denotes that no such method was obtained. The asterisk indicates that the code searching for a method of the type eSSP-EIS+(s,P)2 actually converged to a method of the type eSSP-EIS(s,P)2.

![image 57](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile57.png>)

![image 58](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile58.png>)

![image 59](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile59.png>)

s P eSSP-EIS(s,P)2 eSSP-EIS+(s,P)2 eSSP-MSRK(s,s,P)

![image 60](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile60.png>)

- 2 3 1.500 * 0.732

![image 61](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile61.png>)

![image 62](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile62.png>)

- 2 4 0.990 1.000 –

![image 63](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile63.png>)

![image 64](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile64.png>)

- 2 5 – 0.555 –


![image 65](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile65.png>)

![image 66](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile66.png>)

![image 67](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile67.png>)

- 3 4 1.811 1.896 1.163

![image 68](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile68.png>)

![image 69](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile69.png>)

- 3 5 1.369 1.548 0.638

![image 70](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile70.png>)

![image 71](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile71.png>)

- 3 6 0.546 1.078 0.029

![image 72](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile72.png>)

![image 73](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile73.png>)

- 3 7 – 0.129 –


![image 74](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile74.png>)

![image 75](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile75.png>)

method are rational and given by:

1 16

D =

![image 76](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile76.png>)

7 9 7 9

1 8

, A =

![image 77](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile77.png>)

2 3 2 3

1 8

, Aˆ =

![image 78](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile78.png>)

0 1 0 1

, R2,1 =

- 2

![image 79](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile79.png>)

- 3


2 9

, Rˆ 2,1 =

.

![image 80](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile80.png>)

The remaining coeﬃcients of R and Rˆ are zero, as this method is explicit. It is interesting to note that the optimization procedure converged to this EIS method even when we requested a method that satisﬁes the truncation error condition only up to order p = 1 and all the EIS+ conditions (14a) – (14c).

The SSP coeﬃcient of this method is C = 1.5. We compare this to the SSP coeﬃcient of the standard third order GLM method with two steps and two stages given in

- [1], we denote this one-derivative method by eSSP-MSRK(2,2,3), indicating that it has two steps, two stages, and is order 3. The SSP coeﬃcient of the eSSP-MSRK(2,2,3)


method is C ≈ 0.73. Our two derivative error inhibiting method eSSP-EIS(2,3)2 (with C = 1.5) has 4 function evaluations and the eSSP-MSRK(2,2,3) method has two function evaluations, so the two method would seem to be equally eﬃcient; however, if we consider applications in which the second derivative is available with no additional cost, then the two-step method eSSP-EIS(2,3)2 has an eﬀective SSP timestep that is twice as large.

We found a number of other SSP methods, and present their SSP coeﬃcients in Table 1. The ﬁrst column gives the number of stages s, the second column gives the overall order P that the solutions can be expected to be: for EIS methods this is P = p + 1 and for EIS+ methods this is P = p + 2, which is the order after postprocessing. We note that we did not ﬁnd an eSSP-EIS+(2,3)2 method because the optimization scheme converged to the eSSP-EIS(2,3)2 method instead, and that we could not obtain an eSSP-EIS(2,5)2 or an eSSP-EIS(3,7)2 method and believe they do not exist.

In Table 1 we compare the SSP coeﬃcients of the eSSP-EIS(s,P)2 and eSSPEIS+(s,P)2 methods to that of the comparable SSP GLM methods of [1]. These methods are denoted eSSP-MSRK(s,s,P) to indicate that they have s-steps and sstages and are of order P. This is a fair comparison in such cases where the derivative evaluation does not incur any additional cost. This table shows that for a given s and P, the EIS+ methods have larger allowable SSP coeﬃcients and so are more eﬃcient, assuming that the second derivative is available for no additional cost and that the cost of post-processing is negligible. The coeﬃcients of all the EIS and EIS+ methods in Table 1 can be downloaded from our GitHub directory [11]. Below we list the

coeﬃcients of two featured methods.

- Explicit strong stability preserving eSSP-EIS+(2,4) with C = 1.0: This method has coeﬃcients

D =

0.435605756635718 0.564394243364282 0.435605756635718 0.564394243364282

,

A =

0.232303428413552 0.564394243364282 0.216263460427852 0.564394243364282

,

Aˆ =

0.000000005124887 0.260081562620613 0.000000001928255 0.146835746492061

, where the non-zero elements of R and Rˆ are

R2,1 = 0.376253295127924, and Rˆ 2,1 = 0.162082671864920. The truncation error vector (needed for postprocessing) is

τ3 =

−0.063938362828511 0.049348339827035

.

- Explicit strong stability preserving eSSP-EIS+(3,6) with C = 1.0782: This method has coeﬃcients


- D1,i = 0.235787420033905, D2,i = 0.332249926343388, D3,i = 0.431962653622707,


 

 ,

0.179040619183497 0 0.400647796399945 0.147616987633695 0.118289307755180 0.400647796399945 0.194101834261448 0.212027154638658 0.400647796399945

A =

 

 ,

0.032860477842919 0 0.068024553668439 0.024965463148830 0.034155124171981 0.021087452933654 0.011487692416560 0.092903917927740 0.124915188800131

Aˆ =

 

 ,

0 0 0 0.287524583705647 0 0 0.214948333287866 0.243023557774243 0

R =

 

  ,

0 0 0 0.133340336145235 0 0 0.050250968106130 0.112702859933545 0.

Rˆ =

The truncation error vector (needed for postprocessing) is

 

 .

−0.010752778908703 −0.021534888908005

τ5 =

0.022433270953649

We note that only the method itself is guaranteed to be SSP, we do not expect the post-processed solution to be SSP as well. The post-processor is only designed to extract a higher order solution but not to preserve the strong stability properties. This does not typically pose a problem concern because preserving the nonlinear stability properties is generally only important for the stability of the time evolution: once we reach the ﬁnal time solution these properties are no longer needed. If we still desire some properties that are destroyed by the post-processor we can opt to use the non-post-processed solution instead.

4.3. Implicit A-stable EIS methods. The implicit A-stable methods that we found treat both F and F˙ implicitly. We tried to ﬁnd methods that treat F implicitly and F˙ explicitly, but were not able to ﬁnd A-stable methods of this type. In this section we present two A-stable implicit methods iEIS+(s,P)2 methods. Both R and Rˆ are diagonal matrices and so the method can be implemented eﬃciently in parallel, as each stage is computed independently. The coeﬃcients of the methods as well as the τP − 1 vector needed for post-processing are given below.

- A-stable parallel-eﬃcient iEIS+(2,4)2: D1,i = 0.594710614896760, D2,i = 0.405289385103240,

A =

−2.187376304427630 −0.964459220078949 −1.117865907067007 2.067845436796621

,

Aˆ =

0.778080609332642 −1.088765766927099 −2.898999040140121 1.440243113199464

,

R =

3.949190831954959 0 0 0.347375777718766

,

Rˆ =

−2.706937237458932 0 0 0.978108368826293

. The truncation error vector (needed for postprocessing) is

τ3 =

−3.111010490530440 4.565012136457357

.

- A-stable parallel-eﬃcient iEIS+(3,5)2:


 

 ,

0.439087264857344 0.700945256500558 −0.140032521357901 0.439087264857344 0.700945256500558 −0.140032521357901 0.439087264857344 0.700945256500558 −0.140032521357901

D =

 

 ,

2.507826539020301 3.279683213077780 −1.170881137598611

A =

- −0.334032190141782 −4.031402321497854 0.685583668720811
- −1.750770284075905 −4.999999998880823 3.295317723260540


 

  ,

2.333968082671988 0.419378200972933 −2.408406401605122 −2.145600247202041 0.897829295036851 −0.721006948644857 −4.988816152192916 3.020756581381562 −1.533772624102988

Aˆ =

 

 ,

−3.756922019094389 0 0 0 4.872890771657239 0 0 0 4.981825821767937

R =

 

  .

3.591518759368352 0 0 0 −2.760598976218027 0 0 0 −3.950356833416136

Rˆ =

The truncation error vector (needed for postprocessing) is

 

  .

3.466008686399261 −4.575755330149971

τ4 =

−12.036302018622621

5. Numerical Results. In this section we focus on testing the numerical methods found and presented in Section 4. We ﬁrst verify the convergence properties of the methods presented in Sections 4.1 and 4.3, on a system on nonlinear ODEs. We ﬁnd that these methods achieve the desired convergence rates. Next, we explore the behavior of the SSP methods presented in Section 4.2 in terms of preserving the total variation diminishing properties of spatial discretizations, and show that these methods behave as expected on a standard test-case (see [10]).

5.1. Convergence of high order explicit and implicit schemes. We focus on verifying the convergence of the explicit high order methods eEIS+(2,6)2, eEIS+(3,7)2), and eEIS+(4,8)2 presented in Section 4.1 and the implicit high order methods iEIS+(2,4)2 and iEIS+(3,5)2 presented in Section 4.3 . We show that these methods show the predicted order before and after post-processing on a nonlinear system of ordinary diﬀerential equations.

Non-stiﬀ Van der Pol oscillator: The nonlinear system of ODEs is given by

- y1
- y2


′

=

y2 a(1 − y12)y2 − y1

with a = 2 and initial condition y(0) = (2,0)T. We use the explicit methods eEIS+(2,6)2, eEIS+(3,7)2, eEIS+(4,8)2 to evolve this problem to the ﬁnal time Tf =

- 3.0 and postprocess the solution at the ﬁnal time as described in Section 3.2. We use three repeats of the truncation error vector (m = 3) for all methods except the

eEIS2+(2,6) method for which we used m = 4. (We note that the iEIS+(3,5)2 method only requires m = 2 but m = 3 works well so we use it for consistency with the other methods).

In Figure 4 we show the square-root of the sum of squares of the errors in each component for diﬀerent values of ∆t. The slopes of these lines are computed using MATLAB’s polyfit function and are as follows:

![image 81](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile81.png>)

![image 82](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile82.png>)

![image 83](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile83.png>)

eEIS2+(s,P) = iEIS2+(s,P) = (2,6) (3,7) (4,8) (2,4) (3,5)

![image 84](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile84.png>)

![image 85](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile85.png>)

![image 86](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile86.png>)

![image 87](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile87.png>)

![image 88](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile88.png>)

![image 89](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile89.png>)

![image 90](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile90.png>)

![image 91](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile91.png>)

without post processing 4.7 5.8 7.0 3.0 3.9 after post processing 5.8 6.6 7.7 4.0 5.0

![image 92](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile92.png>)

![image 93](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile93.png>)

![image 94](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile94.png>)

![image 95](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile95.png>)

![image 96](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile96.png>)

![image 97](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile97.png>)

![image 98](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile98.png>)

![image 99](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile99.png>)

Clearly, the orders without postprocessing are of order P −1 and after post-processing are of order P for the eEIS+(s,P)2 and iEIS+(s,P)2 methods found in Section 4.1 and

- 4.3, respectively . This example veriﬁes that numerical solutions from the explicit and implicit error inhibiting methods attain the expected orders of convergence with and without post-processing. These examples conﬁrm that the mathematical conditions and the methods we found work as expected in practice.


5.2. Comparison of explicit strong stability preserving schemes. SSP time-stepping methods are useful for evolving in time hyperbolic PDEs with discontinuities. We focused on ﬁnding SSP methods of the form (2) that preserve the nonlinear non-inner-product stability properties of the spatial discretization methods when coupled with forward Euler and the Taylor series methods, as in [10]. The eSSP-EIS(s,P)2 and eSSP-EIS+(s,P)2 methods we presented in Section 4.2 are tested here on a problem where the spatial discretization is total variation diminishing when coupled with forward Euler time-stepping and when coupled with a Taylor series method. To verify that the methods satisfy the SSP property we examine the maximal rise in total variation when this problem is evolved forward with the eSSP-EIS+(s,p)2 scheme. We further investigate the eﬀect of post-processing on the total variation of this problem.

- -2.45 -2.4 -2.35 -2.3 -2.25 -2.2

- -7
- -6.5
- -6
- -5.5
- -5
- -4.5
- -4


- -2.4 -2.2 -2 -1.8 -1.6 -1.4

- -11
- -10.5
- -10
- -9.5
- -9


Fig. 4. Convergence of the solution (in solid line) and post-processed solution (dashed line) from evolving the Van der Pol system to time Tf = 3.0 for the non-stiﬀ Van der Pol system. On the y-axis is the log10 of the square-root of the sum of squares of the errors; on the x-axis is log10(∆t). Left: The explicit methods eEIS2+(2,6) (in blue), eEIS2+(3,7) (in red), and eEIS2+(4,8) (in black). Right: The implicit methods eEIS2+(2,4) (in blue), eEIS2+(3,5) (in red).

We consider the linear advection equation with step function initial conditions:

ut + ux = 0 u(0,x) =

- 0, if 0 ≤ x ≤ 1/2
- 1, if x > 1/2


on the domain [−1,1] with periodic boundary conditions. We use the fact that utt = −uxt = −utx = uxx to approximate F˙. For the spatial discretization we use a ﬁrst order forward diﬀerence for the ﬁrst and second derivatives with 200 spatial points:

unj − unj−1 ∆x

F(un)j := −

≈ −Ux(xj),

![image 100](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile100.png>)

unj − 2unj−1 + unj−2 ∆x2

F˙(un)j :=

≈ Uxx(xj). These spatial discretizations satisfy:

![image 101](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile101.png>)

Forward Euler condition

∆t ∆x

unj+1 = unj +

unj−1 − unj which is TVD for ∆t ≤ ∆x,

![image 102](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile102.png>)

Taylor series condition

2

∆t ∆x

- 1

![image 103](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile103.png>)

- 2


∆t ∆x

unj+1 = unj +

unj−2 − 2unj−1 + unj which is TVD for ∆t ≤ ∆x.

unj−1 − unj +

![image 104](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile104.png>)

![image 105](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile105.png>)

So that ∆tFE = ∆x and in this case we have K = 1 in (20).

We evolve the solution 10 time-steps using the SSP methods eSSP-EIS(2,3)2, eSSP-EIS+(2,4)2 and eSSP-EIS+(3,6)2 for diﬀerent values of ∆t. At each time-level yn we compute the total variation of the solution at time un,

un TV =

unj+1 − unj .

j

10

5

0

- -15
- -10
- -5


0 0.5 1 1.5 2 2.5

Fig. 5. SSP study: the maximal rise in total variation of the explicit SSP methods SSPEIS+(2,4)2 (red line), eSSP-EIS(2,3)2 (blue line), and eSSP-EIS+(3,6)2 (magenta line) when used to evolve forward the solution in time of the linear advection equation with a step function initial conditions. On the y-axis is log10 of the maximal rise in total variation, and on the x-axis the CFL number λ. The circles mark the diﬀerence between the total variation of the un-processed solution and that of the post-processed solution.

The maximal rise in total variation (solid line) is graphed against λ = ∆∆xt in Figure

![image 106](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile106.png>)

- 5. As we can see, the value of λ for which the total variation begins to rise is always greater that the guaranteed SSP value.


![image 107](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile107.png>)

We then post-process the solution from the eSSP-EIS+(2,4)2 and eSSP-EIS+(3,6)2 methods at the ﬁnal time for all values of ∆t, and compute the diﬀerence between the total variation of the solution at the ﬁnal time and the postprocessed solution

un TV − un TV

We see in Figure 5 that the diﬀerence between the total variation of the solution at the ﬁnal time and the post-processed solution (circle markers) is minimal for all the values of ∆t for which the maximal rise in total variation remains bounded. In particular, for values of λ for which the total variation has not started to rise, we observe that the maximal diﬀerence between the total variation of the solution and the post-processed solution remains very small (≈ 10−15). Although the post-processor is only designed to extract a higher order solution but not to preserve the strong stability properties, it is reassuring that the total variation is not adversely impacted by the post-processor in this case.

6. Conclusions. In this paper we extended the theory developed in [7] to the case of two-derivative GLMs. In [7] we showed, for a one-derivative GLM, the exact form of the error in the case that three error inhibiting conditions hold, and that this error is one order higher than expected by the truncation error analysis and the next error term is multiplied by a truncation error vector with a known form. Furthermore, we designed a post-processor that can eliminate the next term in the error, thus extracting an addition order of accuracy. In this work we extend this theory to two-derivative GLMs of the form (2) and prove that under the suﬃcient conditions (14a)–(14c) we have an error of the form (15). This form is very exactly the same as the form in [7], except that the value of τp+1 is diﬀerent for the twoderivative GLMs than for the one-derivative GLMs. For this reason, the construction of a post-processor (in Section 3.2) follows immediately from the theory in [7].

Using this theory, we programmed an optimization code in Matlab that uses

the order conditions and error inhibiting conditions as constraints and aims to maximize some stability properties. We generated a number of methods that satisfy the order conditions and the error inhibiting condition (14a) or all the error inhibiting conditions (14a)–(14c). The coeﬃcients of all the methods can be downloaded on our GitHub repository [11]. The explicit methods found by the optimizer either have favorable regions of linear stability or are SSP in the sense of [10]. The implicit methods are A-stable. We test a selection of these methods for convergence, and show that they demonstrate the predicted order before and after post-processing on a nonlinear system of ordinary diﬀerential equations. We test the SSP methods for the preservation of the total variation diminishing properties on a PDE with discontinuities, and show that they produce TVD results beyond the guaranteed SSP time-step, and that furthermore post-processing does not adversely aﬀect the total variation. These results validate the methods we found, as well as the theory that we developed.

Appendix A. Coeﬃcients of some methods. In this appendix we list the coeﬃcients of some of the methods mentioned in Section 4.1. The coeﬃcients for all the methods in this paper can be downloaded from our GitHub repository [11].

Explicit two-stage third-order EIS method (eEIS(2,3)2): D1,i = 1.347635863512091, D2,i = −0.347635863512091, A =

1.110588320380528 0.206278390370703 1.160801319467423 0.191968442856969

,

Aˆ =

0.376508598017949 0.079881117612918 0.424704932282709 0.083778591655645

,

R =

0 0 0.875587228946215 0

, Rˆ =

0 0 0.412259887079832 0

Explicit two-stage ﬁfth-order EIS+ method (eEIS+(2,5)2): D1,i = 0.500023658051142, D2,i = 0.499976341948858, A =

0.627069692131650 0.151022064558538 0.709712162750524 0.848963643214302

,

,

Aˆ =

0.058142153689242 0.325582994094698 0.108273930132603 0.477624731406111

,

0 0 −0.336746561995068 0

0 0 0.367133756538675 0

, Rˆ =

R =

. The truncation error vector (needed for postprocessing) is

τ4 = (−0.039533847641586,0.039537588993770)T. Explicit two-stage sixth-order EIS+ method (eEIS+(2,6)2): D1,i = 0.193021555206000, D2,i = 0.806978444794000, A =

1.089589263420254 −0.469532861646008 1.011690204056872 1.112307786855907

A ˆ =

0.196914195858807 0.434709438834146 0.130811273979010 0.871687677021200

,

R =

0 0 −1.033119102271808 0

, Rˆ =

0 0 0.499137031946415 0

The truncation error vector (needed for postprocessing) is τ5 = (−0.037857689452761,0.009055198613815)T. Explicit three-stage seventh-order EIS+ method (eEIS+(3,7)2):

.

- D1,i = 1.581021525561460, D2,i = −0.598751979308602, D3,i = 0.017730453747142,


 

  ,

0.931591460185742 0.379244369981835 −0.172141957956410 0.938547162180577 0.508131122095280 −0.363857858559788 0.504648760586788 1.046850936001111 −0.659275924405796

A =

 

  ,

0.057154143906362 0.302522642478094 0.175689200743141 0.045099335357263 0.359020777972142 0.164798140168151 −0.060217523878309 0.456569929293375 −0.005615338892051

Aˆ =

 

 ,

0 0 0

- 0.307438691150295 0 0
- 1.789973573982305 −0.870575633439973 0


R =

 

 .

0 0 0 0.038804362951013 0 0 0.227157707727078 0.276283023303938 0

Rˆ =

The truncation error vector (needed for postprocessing) is τ6 = (−0.003599790543666,−0.012406980352919,−0.097987210664809)T. Explicit four-stage eighth-order EIS+ method (eEIS+(4,8)2):

D1,i = 1.126765222628176, D2,i = 0.808129178515260, D3,i = −0.107647150078402, D4,i = −0.827247251065033,

   ,

  

![image 108](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile108.png>)

0.567574025309926 0.723999455772069 0.208196137734782 0.023532165559543 0.749691669482323 0.430151531239573 0.359568096205409 −0.030974711893773

A =

- 0.602555996794216 0.745759221902972 0.048559187429251 −0.267889537378177
- 1.051588361923041 −0.047355340428569 0.863960642835203 0.214102220881218


   ,

  

0.041975696597772 0.205746598967380 0.137652258393657 0.039122406247340 0.064927843091523 0.213465637934016 0.160720650985361 −0.047428374982532 0.056975020786010 0.171669459177575 0.226994033551341 −0.021617692260293 0.095018403341495 0.263066907087928 0.147903147440657 −0.036525606967693

Aˆ =

  

  ,

0 0 0 0 0.296825313241825 0 0 0 0.379857836431130 0.610459020171445 0 0 0.079086170545983 0.114409044614819 0.077980998192235 0

R =

   .

  

0 0 0 0 0.095598816350501 0 0 0 −0.143446089841412 0.076113483149991 0 0 0.309290513515929 0.063106409144583 0.076129207423402 0

Rˆ =

21

The truncation error vector (needed for postprocessing) is

  .

  

−0.000997109517747 −0.006485724807936 −0.023117224006582 −0.004685791946531

τ7 =

Acknowledgment. This publication is based on work supported by AFOSR grant FA9550-18-1-0383 and ONR-DURIP Grant N00014-18-1-2255. A part of this research is sponsored by the Oﬃce of Advanced Scientiﬁc Computing Research; US Department of Energy, and was performed at the Oak Ridge National Laboratory, which is managed by UT-Battelle, LLC under Contract no. De-AC05-00OR22725. This manuscript has been authored by UT-Battelle, LLC, under contract DE-AC0500OR22725 with the US Department of Energy. The United States Government retains and the publisher, by accepting the article for publication, acknowledges that the United States Government retains a non-exclusive, paid-up, irrevocable, worldwide license to publish or reproduce the published form of this manuscript, or allow others to do so, for United States Government purposes.

REFERENCES

- [1] C. Bresten, S. Gottlieb, Z. Grant, D. Higgs, D.I. Ketcheson, and A. Nemeth, Explicit strong stability preserving multistep Runge-Kutta methods, Mathematics of Computation 86 (2017) 747–769.
- [2] J. C. Butcher, Diagonally-implicit multi-stage integration method, Applied Numerical Mathematics 11 (1993), 347–363.
- [3] J. C. Butcher, Numerical methods for ordinary diﬀerential equations, John Wiley & Sons, 2008.
- [4] R. P. K. Chan and A. Y. J. Tsai, On explicit two-derivative Runge-Kutta methods, Numerical Algorithms, 53 (2010), pp. 171–194.
- [5] A. Christlieb, S. Gottlieb, Z. Grant, and D. C. Seal, Explicit strong stability preserving multistage two-derivative time-stepping schemes, Journal of Scientiﬁc Computing, 68 (2016), pp. 914–942.
- [6] A. Ditkowski and S. Gottlieb, Error Inhibiting Block One-step Schemes for Ordinary Diﬀerential Equations, Journal of Scientiﬁc Computing 73(2) (2017) 691–711.
- [7] Adi Ditkowski, Sigal Gottlieb, Zachary J. Grant, ”Explicit and implicit error inhibiting schemes with post-processing.” arxiv.org/abs/1910.02937
- [8] Z. Du and J. Li, A Hermite WENO reconstruction for fourth order temporal accurate schemes based on the GRP solver for hyperbolic conservation laws, Journal of Computational Physics 355 (2018), pp. 385–396
- [9] S. Gottlieb, D. I. Ketcheson, and C.-W. Shu, Strong Stability Preserving RungeKutta and Multistep Time Discretizations, World Scientiﬁc Press, 2011.
- [10] S. Gottlieb, Z. Grant, and D. C. Seal, Explicit strong stability preserving multistage twoderivative time-stepping schemes, Journal of Scientiﬁc Computing, 68 (2016), pp. 914–942.
- [11] Z. Grant, S. Gottlieb, and A. Ditkowski, Explicit and implicit two-derivative EIS methods with post-processing, (2019), GitHub repository, https://github.com/EISmethods/EIS 2derivative

![image 109](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile109.png>)

- [12] B. Gustafsson, H.-O. Kreiss, and J. Oliger, Time dependent problems and diﬀerence methods, vol. 24, John Wiley & Sons, 1995.
- [13] E. Hairer, G. Wanner, and S. P. Norsett, Solving Ordinary Diﬀerential Equations I: Nonstiﬀ Problems, Springer Series in Computational Mathematics, Springer-Verlag Berlin Heidelberg (1993).
- [14] Z. Jackiewicz, General linear methods for ordinary diﬀerential equations, John Wiley & Sons, 2009.
- [15] K. Kastlunger and G. Wanner, On Turan type implicit Runge-Kutta methods, Computing (Arch. Elektron. Rechnen), 9 (1972), pp. 317–325.
- [16] K. H. Kastlunger and G. Wanner, Runge Kutta processes with multiple nodes, Computing (Arch. Elektron. Rechnen), 9 (1972), pp. 9–24.
- [17] I.P.E. Kinnmark and W.G. Gray, One step integration methods with maximum stability regions, Mathematics and Computers in Simulation 26 (2) (1984), pp. 8792.
- [18] G.Yu. Kulikov, On quasi-consistent integration by Nordsieck methods, Journal of Computational and Applied Mathematics 225 (2009) 268–287.
- [19] G. Yu. Kulikov and R. Weiner, Variable-Stepsize Interpolating Explicit Parallel Peer Methods with Inherent Global Error Control, SIAM Journal on Scientiﬁc Computing, 32(4) (2010) 1695–1723.
- [20] G.Yu. Kulikov and R. Weiner, Doubly quasi-consistent ﬁxed-stepsize numerical integration of stiﬀ ordinary diﬀerential equations with implicit two-step peer methods, Journal of Computational and Applied Mathematics, 340 (2018) 256–275.
- [21] P. D. Lax and R. D. Richtmyer, Survey of the stability of linear ﬁnite diﬀerence equations, Communications on pure and applied mathematics 9 (1956), no. 2, 267–293.
- [22] J. Li and Z. Du, A two-stage fourth order time-accurate discretization for Lax-Wendroﬀ type ﬂow solvers I. hyperbolic conservation laws, SIAM J. Sci. Computing, 38 (2016) pp. 3046– 3069.
- [23] T. Mitsui, Runge-Kutta type integration formulas including the evaluation of the second derivative. i., Publications of the Research Institute for Mathematical Sciences, 18 (1982), pp. 325–364.
- [24] T. Nguyen-Ba, H. Nguyen-Thu, T. Giordano, and R. Vaillancourt, One-step strong-stabilitypreserving Hermite-Birkhoﬀ-Taylor methods, Scientiﬁc Journal of Riga Technical University, 45 (2010), pp. 95–104.
- [25] N. Obreschkoﬀ, Neue quadraturformeln, Abh. Preuss. Akad. Wiss. Math.-Nat. Kl., 4 (1940).
- [26] R. I. Okuonghae and M. N. O. Ikhile, L(α)-stable Multi-derivative GLM, Journal of Algorithms & Computational Technology Vol. 9 (2015) No. 4, pp. 339 – 376.


- [27] H. Ono and T. Yoshida, Two-stage explicit Runge-Kutta type methods using derivatives., Japan Journal of Industrial and Applied Mathematics, 21 (2004), pp. 361–374.
- [28] L. Pan, K. Xu, Q. Li, and J. Li, An eﬃcient and accurate two-stage fourth-order gas-kinetic scheme for the Euler and Navier–Stokes equations, Journal of Computational Physics 326

(2016), pp. 197–221.

- [29] A. Quarteroni, R. Sacco, and F. Saleri, Numerical mathematics, vol. 37, Springer Science & Business Media, 2010.
- [30] D. C. Seal, Y. Guclu, and A. J. Christlieb, High-order multiderivative time integrators for hyperbolic conservation laws, Journal of Scientiﬁc Computing, 60 (2014), pp. 101–140.
- [31] R.D. Skeel, Analysis of ﬁxed-stepsize methods, SIAM Journal on Numerical Analysis 13 (1976) 664–685.
- [32] H. Shintani, On one-step methods utilizing the second derivative, Hiroshima Mathematical Journal, 1 (1971), pp. 349–372.
- [33] , On explicit one-step methods utilizing the second derivative, Hiroshima Mathematical Journali, 2 (1972), pp. 353–368.

![image 110](<2019-ditkowski-two-derivative-error-inhibiting-schemes_images/imageFile110.png>)

- [34] B. Soleimani, R. Weiner A class of implicit peer methods for stiﬀ systems, Journal of Computational and Applied Mathematics 316 (2017) 358–368
- [35] E. Sli and D.F. Mayers, An Introduction to Numerical Analysis, Cambridge University Press, Cambridge, 2003.
- [36] D. D. Stancu and A. H. Stroud, Quadrature formulas with simple Gaussian nodes and multiple ﬁxed nodes, Mathematics of Computation, 17 (1963), pp. 384–394.
- [37] A. Y. J. Tsai, R. P. K. Chan, and S. Wang, Two-derivative Runge–Kutta methods for PDEs using a novel discretization approach, Numerical Algorithms, 65 (2014), pp. 687–703.
- [38] P. Tura´n, On the theory of the mechanical quadrature, Acta Universitatis Szegediensis. Acta Scientiarum Mathematicarum, 12 (1950), pp. 30–37.
- [39] R. Weiner, G.Yu. Kulikov, and H. Podhaiskya, Variable-stepsize doubly quasi-consistent parallel explicit peer methods with global error control, Applied Numerical Mathematics 62 (2012) 1591–1603.
- [40] R. Weiner, B. A. Schmitt, H.Podhaiskya, and S. Jebensc, Superconvergent explicit two-step peer methods, Journal of Computational and Applied Mathematics 223 (2009) 753–764.


