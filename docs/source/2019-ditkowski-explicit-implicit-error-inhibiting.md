---
type: source
kind: paper
title: Explicit and implicit error inhibiting schemes with post-processing
authors: Adi Ditkowski, Sigal Gottlieb, Zachary J. Grant
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/1910.02937v2
source_local: ../raw/2019-ditkowski-explicit-implicit-error-inhibiting.pdf
topic: general-knowledge
cites:
---

arXiv:1910.02937v2[math.NA]12Mar2020

EXPLICIT AND IMPLICIT ERROR INHIBITING SCHEMES WITH POST-PROCESSING

ADI DITKOWSKI∗, SIGAL GOTTLIEB†, AND ZACHARY J. GRANT‡

Abstract. Eﬃcient high order numerical methods for evolving the solution of an ordinary diﬀerential equation are widely used. The popular Runge–Kutta methods, linear multi-step methods, and more broadly general linear methods, all have a global error that is completely determined by analysis of the local truncation error. In prior work we investigated the interplay between the local truncation error and the global error to construct error inhibiting schemes that control the accumulation of the local truncation error over time, resulting in a global error that is one order higher than expected from the local truncation error. In this work we extend our error inhibiting framework introduced in [6] to include a broader class of time-discretization methods that allows an exact computation of the leading error term, which can then be post-processed to obtain a solution that is two orders higher than expected from truncation error analysis. We deﬁne suﬃcient conditions that result in a desired form of the error and describe the construction of the post-processor. A number of new explicit and implicit methods that have this property are given and tested on a variety of ordinary and partial diﬀerential equations. We show that these methods provide a solution that is two orders higher than expected from truncation error analysis alone.

1. Introduction. Eﬃcient high order time evolution methods are of interest in many simulations, particularly when evolving in time a system of ordinary diﬀerential equations (ODEs) resulting from a semi-discretized partial diﬀerential equation. In this work we consider an approach to developing methods that are of higher order than expected from truncation error analysis. We ﬁrst present some background on numerical methods for ODEs and deﬁne all the relevant terms.

We consider numerical solvers for ODEs. Without loss of generality, we can consider the autonomous equation of the form

- (1) ut = F(u) , t ≥ t0 u(t0) = u0.


The most basic of these numerical solvers is the forward Euler method vn+1 = vn + ∆tF(vn) ,

where vn approximates the exact solution vn ≈ u(tn) at some time tn = t0 + n∆t. The forward Euler method has local truncation error LTEn and approximation error τn at any given time tn deﬁned by

τn = ∆tLTEn = u(tn−1) + ∆tF(u(tn−1)) − u(tn) ≈ O(∆t2) and a global error which is ﬁrst order accurate

En = vn − u(tn) ≈ O(∆t).

We note that while we follow the convention in [9, 18, 1, 12, 20] and deﬁne the local truncation error as the normalized approximation error,

1 ∆t

τn,

LTEn =

![image 1](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile1.png>)

![image 2](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile2.png>)

∗School of Mathematical Sciences, Tel Aviv University, Tel Aviv 69978, Israel. Email: adid@post.tau.ac.il

†Mathematics Department, University of Massachusetts Dartmouth, 285 Old Westport Road, North Dartmouth MA 02747. Email: sgottlieb@umassd.edu

‡Department of Computational and Applied Mathematics, Oak Ridge National Laboratory, Oak Ridge TN 37830. Email: grantzj@ornl.gov

an alternative notation in common use is to deﬁne the local truncation error to be the approximation error. Using our notation, the local truncation error and the global error are of the same order for the forward Euler method. Using the alternative notation, the local truncation error is one order higher than the global error.

If we want a more accurate method than forward Euler, we can add steps and deﬁne a linear multistep method [4]

- (2) vn+1 =

s

j=1

αj vn+1−j + ∆t

s

j=0

βjF(vn+1−j),

or we can use multiple stages as in Runge–Kutta methods [4]:

yi = vn + ∆t

m

j=1

aijF (yj) for j = 1,...,m

vn+1 = vn + ∆t

m

j=1

- (3) bjF (yj).

It is also possible to combine the approaches above, by starting with a Runge– Kutta method of the form (3) but including older time-steps as in linear multistep methods (2). These are the general linear methods described in [3, 13] and may be written in the form

yi =

s

j=1

αijvn−j+1 + ∆t

s−1

j=1

aˆijF(vn−j+1) + ∆t

m

j=1

aijF(yj)

for j = 1,...,m vn+1 =

s

j=1

ωjvn−j+1 + ∆t

s−1

j=1

ˆbjF(vn−j+1) + ∆t

m

j=1

- (4) bjF(yj) .


In all these cases, we aim to increase the order of the local truncation error and therefore to increase the order of the global error.

The relationship between the local truncation error and the global error is wellknown. The Dahlquist Equivalence Theorem [22] states that any zero-stable, consistent linear multistep method with local truncation error LTEn = O(∆tp) will have global error O(∆tp), provided that the solution has at least (p+1) smooth derivatives. (Note that this statement depends on the normalized deﬁnition of the local truncation error where LTEn = ∆1tτn. If the non-normalized deﬁnition is used, then the global order is one lower than the local truncation error). Indeed, all the familiar schemes for numerically solving ODEs have global errors that are of the same order as their local truncation errors. In fact, this relationship between local truncation error and global error is common not only for ODE solvers, but is typically seen in other ﬁelds in numerical mathematics, such as for ﬁnite diﬀerence schemes for partial diﬀerential equations (PDEs) [9, 18].

![image 3](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile3.png>)

It is, however, possible to devise schemes that have global errors that are higher order than the local truncation errors. In particular, it was shown in [5] that ﬁnite diﬀerence schemes for PDEs can be constructed such that their convergence rates are higher than the order of the truncation errors. A similar approach was adopted in [6] for time evolution methods, where we described the conditions under which general linear methods (GLMs) can have global error is one order higher than the

normalized local truncation error, and devise a number of GLM schemes that feature this behavior. These schemes achieve this higher-than-expected order by inhibiting the lowest order term in the local error from accumulating over time, and so we named

- them Error Inhibiting Schemes (EIS). As we have since discovered, our EIS schemes have the same conditions as the quasi-consistent schemes of Kulikov, Weiner, and colleagues [14, 21, 24].


In this paper, we extend the error inhibiting approach in two ways. First, we consider a broader formulation of the GLM that allows for implicit methods as well as more general explicit methods than considered in [6]. Next, we show that by imposing additional conditions on the methods we are able to precisely describe the coeﬃcients of the error term and we then devise a post-processing approach that removes this error term, thus obtaining a global error that is two orders higher than the normalized local truncation error. We proceed to devise error inhibiting methods using this new EIS approach, and investigate their linear stability properties, strong stability preserving (SSP) properties, and computational eﬃciency. Finally, we test these methods on a number of numerical examples to demonstrate their enhanced accuracy and, where appropriate, stability properties. In Appendix A we present an alternative approach to understanding the growth of the errors and describing the coeﬃcients of the error term. Note that the analysis in this paper is performed for the scalar equation (1), but can be easily extended to the vector case, as shown in Appendix B.

1.1. Preliminaries. We begin with a scheme of the form

- (5) V n+1 = DV n + ∆tAF(V n) + ∆tRF(V n+1),

where V n is a vector of length s that contains the numerical solution at times (tn + cj∆t) for j = 1,...,s:

- (6) V n = (v(tn + c1∆t)),v(tn + c2∆t),...,v(tn + cs∆t))T .

The function F(V n) is deﬁned as the component-wise function evaluation on the vector V n:

- (7) F(V n) = (F(v(tn + c1∆t)),F(v(tn + c2∆t)),...,F(v(tn + cs∆t)))T .

For convenience, c1 ≤ c2 ≤ ... ≤ cs. Also, we pick cs = 0 so that the ﬁnal element in the vector approximates the solution at time tn. This notation was chosen to match the notation widely used in the ﬁeld of general linear methods. To start these methods, we need to build an initial vector: to do so we artiﬁcially redeﬁne the timegrid so that t0 := t0 − c1∆t. Now the ﬁrst element in the initial solution vector V 0 is v(t0 + c1∆t) = u0 and the remaining elements v(t0 + cj∆t) are computed using a highly accurate one-step method. Note that we consider only the case where ∆t is ﬁxed.

Remark 1. The form (5) includes implicit schemes, as V n+1 appears on both sides of the equation. However, if R is strictly lower triangular the scheme is, in fact, explicit. If R is a diagonal matrix then we can compute each element of the vector V n+1 concurrently.

We deﬁne the corresponding exact solution of the ODE (1):

- (8) Un = (u(tn + c1∆t),u(tn + c2∆t),...,u(tn + cs∆t))T ,


with F(Un) deﬁned similarly.

The global error of the method is deﬁned as the diﬀerence between the vectors of the exact and the numerical solutions at some time tn

- (9) En = V n − Un.

For the method (5), we deﬁne the normalized local truncation error LTEn and approximation error τn by

- (10) ∆t LTEn = τn = DUn−1 + ∆tAF(Un−1) + ∆tRF(Un) − Un. Taylor expansions on (10) allow us to compute these terms
- (11) ∆t LTEn = τn =

∞

j=0

τnj ∆tj =

∞

j=0

τj∆tj

dju dtj t=t

![image 4](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile4.png>)

n

where the term d

ju dtj

![image 5](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile5.png>)

t=tn

is the jth derivative of the solution at time t = tn, the value

∆tj is the time-step raised to the power j, and the truncation error vectors τj are given by:

- (12a) τ0 = (I − D) 1


1 j

1 j

1 (j − 1)!

D(c − 1)j + A(c − 1)j−1 + Rcj−1 −

- (12b) cj for j=1,2, . . .


τj =

![image 6](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile6.png>)

![image 7](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile7.png>)

![image 8](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile8.png>)

Here, c is the vector of abscissas (c1,c2,...,cs)T and 1 = (1,1,...,1)T is the vector of ones. Terms of the form cj are understood component-wise cj = (cj1,cj2,...,cjs)T.

If the truncation error vectors τj satisfy the order conditions τj = 0 for j = 0,...,p then we have local truncation error LTEn = O(∆tp) and (correspondingly) approximation error τn = O(∆tp+1). In such a case we typically observe a global order of En = O(∆tp) at any time tn. Note once again that our deﬁnition of the local truncation error LTEn is the normalized deﬁnition. According to this deﬁnition, we sww that we expect the global error to be of the same order as the local truncation error LTEn. If the local truncation error LTEn is not normalized, then it is equal to τn, and we expect the global error to be one order lower than τn. We reiterate that we use the local truncation error LTEn to indicate the normalized deﬁnition, and the approximation error τn to indicate the non-normalized deﬁnition.

As shown in [6], if we add conditions on D,A (and R), we can ﬁnd methods that exhibit a global order of En = O(∆tp+1) even though they only satisfy τj = 0 for j = 0,...,p. In addition, as we show in Section 3.2, certain conditions on D,A,R allow us to precisely understand the form of the ∆tp+1 term in the global error, so we can design a postprocessor that gives us a numerical solution which has an error of order O(∆tp+2), as we show in Section 3.3.

2. Review of error inhibiting and related schemes. The Dahlquist Equivalence Theorem [22] states that any zero-stable, consistent linear multistep method with truncation error O(∆tp) will have global error O(∆tp), provided that the solution has at least (p + 1) smooth derivatives. All the one step methods and linear multistep methods that are commonly used feature a global error that is of the same order as the normalized local truncation error. This is so common that the order of

the method is typically deﬁned solely by the order conditions derived by Taylor series analysis of the local truncation error. However, recent work [6] has shown that one can construct general linear methods so that the accumulation of the local truncation error over time is controlled. These schemes feature a global error that is one order higher than the local truncation error. In this section we review prior work on such error inhibiting schemes by Ditkowski and Gottlieb [6], and show that similar results were obtained in the work of Kulikov, Weiner, and colleagues [14, 21, 24]. This body of work serves as the basis for our current work which will be presented in Section 3.

In [6], Gottlieb and Ditkowski considered numerical methods of the form

- (13) V n+1 = DV n + ∆tAF(V n)

(i.e. 5 with R = 0), where D is a diagonalizable rank one matrix, whose non-zero eigenvalue is equal to one and its corresponding eigenvector is (1,...,1)T. They showed that if the method satisﬁes the order conditions

- (14) τj = 0, for j = 0,...,p and the error inhibiting condition
- (15) Dτp+1 = 0

hold, then the resulting global error satisﬁes En = O ∆tp+1 . Our work in [6] showed how condition (15) mitigates the accumulation of the truncation error, so we obtain a global error that is one order higher than predicted by the order conditions that describe the local truncation error. Furthermore, we developed several block one-step methods and demonstrated in numerical examples on nonlinear problems that these methods have global error that is one order higher than the local truncation error analysis predicts.

As we later found out, although the underlying approach is diﬀerent, the conditions in [6] are along the lines of the theory of quasi-consistency ﬁrst introduced by Skeel in 1978 [19]. This work was then generalized and further developed by Kulikov for Nordsiek methods in [14], as well as Weiner and colleagues [24]. In [24], a theory of superconvergence for explicit two-step peer methods was deﬁned, and in [21] the theory was extended to implicit methods. In these papers, the authors showed that if the method satisﬁes order conditions (14) and conditions that are equivalent to the EIS conditions in [6] then the global error satisﬁes En = O ∆tp+1 .

In [15], [23], and [16], the authors show that by requiring the order conditions

- (14) and EIS condition (15) as well as additional conditions

(16a) Dτp+2 = 0

- (16b) DAτp+1 = 0
- (16c) DRτp+1 = 0


the resulting global error satisﬁes En = O ∆tp+1 but, in addition, the form of the ﬁrst surviving term in the global error (the vector multiplying ∆tp+1) is known explicitly, and is leveraged for error estimation. While the error inhibiting condition

- (15) requires the p + 1 truncation error vector τp+1 to live in the nullspace of D the additional conditions (16) require that the p + 2 truncation error vector τp+2 also lives in the nullspace of D, and that the p + 1 truncation error vector τp+1 lives in the nullspace of DA and DR. These conditions inhibit the buildup of the truncation




error so that we not only get a solution that is of order ∆tp+1, but also control the vector multiplying this error term.

In this work we can show that under less restrictive conditions than (16) we can explicitly compute the form of the ﬁrst surviving term in the global error. Furthermore, having this error term explicitly deﬁned enables us to deﬁne a postprocessor that allows us to extract a ﬁnal-time solution that is accurate to two orders higher than predicted by truncation error analysis alone. We proceed to demonstrate these two facts and design a post-processor that allows us to extract a solution of O(∆tp+2).

3. Designing explicit and implicit error inhibiting schemes with postprocessing. In this section we consider the improved error inhibiting schemes and the associated post-processor that allow us to recover order p + 2 from a scheme that would otherwise be only pth order accurate. In Subsection 3.2, we show that the method must satisfy additional conditions so that the form of the ﬁnal error is controlled and can be post-processed to extract higher order. In Subsection 3.3, we show how this post-processing is done. Before we begin, we make some observations in Subsection 3.1 that will be essential for Subsection 3.2. We note that our discussion in this section focuses, for simplicity of presentation, on a scalar function F. The vector case follows directly without diﬃculty, but the notation is more messy. We brieﬂy discuss the extension to the vector case in Appendix B.

3.1. Essentials. In this subsection we present two observations that will be used in the next subsection. The ﬁrst observation uses the smoothness of the time evolution operator to bound the growth of the error at each step:

Lemma 1. The scheme (5) can be written in the form:

- (17) V n+1 = (I − ∆tRF)−1 (D + ∆tAF) V n ≡ QnV n If the order conditions are satisﬁed to j = 0,....,p, the scheme (5) (or equivalently


- (17)) is zero–stable, the operator (I − ∆tRF)−1 is bounded and the (nonlinear) operator Qn is Lipschitz continuous in the sense that there is some constant L > 0 such that
- (18) QnV n − QnUn ≤ L V n − Un

then the error accumulated in one step gets no worse than O(∆tp+1) i.e.

- (19) En+1 = O Ek ) + O(∆tp+1). Proof. The exact solution satisﬁes the equation
- (20) Un+1 = QnUn − (I − ∆tRF)−1 τn+1 . By subtracting (20) from (17) we obtain


En+1 = V n+1 − Un+1 ≤ QnV n − QnUn + (I − ∆tRF)−1 τn+1 ≤ L V n − Un + O(∆tp+1)

= O Ek ) + O(∆tp+1).

![image 9](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile9.png>)

![image 10](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile10.png>)

![image 11](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile11.png>)

![image 12](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile12.png>)

The next observation will be needed for the expansion of F(Un+En). In the following, we assume that F is a scalar function operating on the vector V n = Un + En. The extension of this to the case where F is a vector function is straightforward, and will be addressed in Appendix B.

Lemma 2. Given a smooth enough function F, we have

- (21) F(Un + En) = F(Un) + FunEn + O(∆t)O ( En ), where Fun = ∂F∂u (u(tn)).

![image 13](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile13.png>)

Proof. We expand

F(Un + En) = F(Un) +



 

Fu(u(tn + c1∆t))en+c

- 1

Fu(u(tn + c2∆t))en+c

- 2


. Fu(u(tn + cs∆t))en+c

s



 

+ O En 2 ,

where the error vector is En = (en+c

1

,en+c

2

,...,en+c

s

)T. Using the deﬁnition Fun+cj = ∂F∂u (u(tn + cj∆t)) we re-write this as

![image 14](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile14.png>)

F(Un + En) = F(Un) +



 

Fn+c

u 1 0 ··· 0 0 Fn+c u 2 ··· 0

. .

... . 0 0 ··· Fn+c

u s



 

En + O En 2 .

Each term can be expanded as Fn+c

j

u = Fu(u(tn + cj∆t)) = Fu(u(tn)) + cj∆tFuu(u(tn)) + O(∆t2) so that we can say that

Fn+c

j

u = Fu(u(tn + cj∆t)) = Fu(u(tn)) + C∆t + O(∆t2) so that

F(Un + En) = F(Un) + FunI + C∆t + O(∆t2) En + O En 2

= F(Un) + FunEn + C∆tEn + O(∆t2)O ( En ) + O En 2 .

= F(Un) + FunEn + O(∆t)O ( En ).

![image 15](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile15.png>)

![image 16](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile16.png>)

![image 17](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile17.png>)

![image 18](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile18.png>)

Corollary 1. If the error is of the form En = O(∆tp+1), then

- (22) F(Un + En) = F(Un) + FunEn + O ∆tp+2 .

3.2. Improved error inhibiting schemes that have p + 1 order. In this section we consider a method of the form (5), where D is a rank one matrix that satisﬁes the consistency condition D1 = 1, and D, A and R are matrices that satisfy the order conditions

- (23) τj = 0, for j = 1,...,p, and the EIS+ conditions
- (24a) Dτp+1 = 0


- (24b) Dτp+2 = 0
- (24c) D(A + R)τp+1 = 0.


We initialize the method with a numerical solution vector V 0 that is accurate enough so that we ensure that the error is negligible. This means that taking one step forward using (5) has no accumulation error, only the truncation error:

V 1 = U1 + τ1 = U1 + ∆tp+1τ1p+1 + ∆tp+2τ1p+2 + O(∆tp+3), and

E1 = ∆tp+1τ1p+1 + ∆tp+2τ1p+2 + O(∆tp+3). The conditions Dτp+1 = 0 and Dτp+2 = 0 from (24) mean that

DE1 = O(∆tp+3).

From Lemma 1 we know that the error that accumulates in only one step is no worse than order ∆tp+1 so that O(Ek+1) = O(Ek) + O(∆tp+1) and thus we know that

V 2 = U2 + O(∆tp+1). We use these facts about V 1 and V 2 to write:

V 2 = DV 1 + ∆tAF(V 1) + ∆tRF(V 2)

= D U1 + E1 + ∆tAF U1 + E1 + ∆tRF U2 + E2

= DU1 + ∆tAF(U1) + ∆tRF(U2) + DE1

+ ∆tAFu1E1 + ∆tAFu2E2 + O ∆tp+3 Note that the ﬁrst three terms are, by the deﬁnition of the local truncation error

DU1 + ∆tAF(U1) + ∆tRF(U2) = U2 + ∆tp+1τ2p+1 + ∆tp+2τ2p+2 + O(∆tp+3), so that

V 2 = U2 + τ2 + C∆tp+2 + O(∆tp+3), which means that

E2 = τ2 + C∆tp+2 + O(∆tp+3). Using this more reﬁned understanding of the order term, we repeat the process above

- to write:


V 2 = D U1 + E1 + ∆tAF U1 + E1 + ∆tRF U2 + E2

= DU1 + ∆tAF(U1) + ∆tRF(U2) + DE1

+ ∆tAE1Fu1 + ∆tRE2Fu2 + C∆t2En + O(∆t3)O ( En )

= U2 + τ2 + ∆tAτ1Fu1 + ∆tRτ2Fu2 + C∆tp+3 + O ∆tp+4

where C is a constant that depends on the truncation error vectors and the values of higher derivatives of a solution, and whose value is diﬀerent at each line. This means that

- (25) E2 = ∆tp+1τ2p+1 + ∆tp+2τ2p+2 + ∆tp+2 (A + R)τ2p+1Fu2


+ 2C2∆tp+3 + O(∆tp+4), and so conditions (24) imply that

DE2 = C˜∆tp+3 + O(∆tp+4).

This precise form of E2 can be extended to the error at any time-level tn. In the following theorem we show that the conditions (24) allow us to determine the precise form of the ∆tp+1 term in the global error En resulting from the scheme (5). In the next section we use this precise form to extract higher order accuracy by post-processing.

Theorem 1. For a method of the form (5), if we choose a rank one matrix D such that the consistency condition D1 = 1 is satisﬁed, and matrices A and R such that the order conditions (23) are satisﬁed and furthermore the EIS conditions (24) hold, then the resulting global error at any time tn has the form

- (26) En = ∆tp+1τnp+1+∆tp+2τnp+2+∆tp+2(A+R)τnp+1Fun+Cnn∆tp+3+O(∆tp+3),


where Cn is a constant.

Proof. We showed above that the base case (25) has the correct form (26). We proceed by induction: assume that the numerical solution at time tk has an error of the form (26):

Ek = ∆tp+1τkp+1 +∆tp+2τkp+2 +∆tp+2(A+R)τkp+1Fu(Uk)+Ckk∆tp+3 +O(∆tp+3). The form of the error means that, using conditions (24), we have

DEk = Ck∆tp+3 + O(∆tp+3).

We wish to show that under the conditions in the theorem, Ek+1 has a similar form. We split our argument into two steps:

- (1) First step: We know from Lemma 1 that the error that accumulates in only one step is no worse than order ∆tp+1 so that since Ek = C∆tp+1 + O(∆tp+1) we know that we also have Ek+1 = C˜∆tp+1 + O(∆tp+1). Now we look at the evolution of the error from one time-step to the next:

V k+1 = DV k + ∆tAF(V k) + ∆tRF(V k+1)

= D Uk + Ek + ∆tAF Uk + Ek + ∆tRF Uk+1 + Ek+1

= DUk + ∆tAF(Uk) + ∆tRF(Uk+1) + DEk

+ ∆tAFukEk + ∆tRFuk+1Ek+1 + C∆t2O( Ek ) + O(∆tp+3).

= Uk+1 + τk+1 + C∆tp+2 + O(∆tp+3) so that

Ek+1 = ∆tp+1τkp+1+1 + C˜∆tp+2 + O(∆tp+3).

- (2) Second step: This analysis allowed us to obtain a more precise understanding of the growth of the error over one step from V k to V k+1. The error is still of order O(∆tp+1), but the leading term in the error is now explicitly deﬁned. With this new understanding of V k+1, we repeat the analysis:


V k+1 = DV k + ∆tAF(V k) + ∆tRF(V k+1)

= D Uk + Ek + ∆tAF Uk + Ek + ∆tRF Uk+1 + Ek+1

= DUk + ∆tAF(Uk) + ∆tRF(Uk+1) + DEk

+ ∆tAEkFuk + ∆tREk+1Fuk+1 + C∆t2O( Ek ) + O(∆t3)O( Ek )

= Uk+1 + τk+1 + DEk + ∆tAEkFuk + ∆tREk+1Fuk+1 + C∆t2O( Ek ) + O(∆t3)O( Ek )

= Uk+1 + τk+1 + Ck∆tp+3 + ∆tAEkFuk + ∆tREk+1Fuk+1 + O(∆tp+3).

We now use what we know about Ek from the base-case and Ek+1 from step 1:

V k+1 = Uk+1 + τk+1 + Ck∆tp+3 + ∆tA ∆tp+1τkp+1 Fuk

+ ∆tR ∆tp+1τkp+1+1 Fuk+1 + C˜∆tp+3 + O(∆tp+3).

= Uk+1 + τk+1 + ∆tp+2Aτkp+1Fuk + ∆tp+2Rτkp+1+1Fuk+1

+ Ckk∆tp+3 + Cˆ∆tp+3 + O(∆tp+3).

= Uk+1 + ∆tp+1τkp+1+1 + ∆tp+2τkp+2+1 + ∆tp+2(A + R)τkp+1+1Fuk+1

+ Ckk∆tp+3 + C∆tp+3 + O(∆tp+3), using the fact that

τkp+1+1 = τkp+1 + O(∆t) and Fuk+1 = Fuk + O(∆t), and that

τk+1 = ∆tp+1τkp+1+1 + ∆tp+2τkp+2+1 + C˜∆tp+3 + O(∆tp+4). Clearly, each time-step accumulates a few terms of the form ∆tp+3, so that

V k+1 = Uk+1 + ∆tp+1τkp+1+1 + ∆tp+2τkp+2+1 + ∆tp+2 (A + R)τkp+1+1Fuk+1

+ (Ckk + C)∆tp+3 + O ∆tp+3 .

Setting Ck+1 = max{Ck,C} we obtain the desired result. Note that the constants Ck are uniformly bounded, since they are constants that depend on some combinations of the truncation error vectors τj, the higher order derivatives of u at times (t0,tn), and the bounded matrix operators in the problem.

![image 19](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile19.png>)

![image 20](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile20.png>)

![image 21](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile21.png>)

![image 22](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile22.png>)

The conditions τj = 0 for j = 1,...,p give us a method of order p, while the additional condition Dτp+1 = 0 allow us to get a p + 1 order method, just as in previous EIS methods. Adding the conditions Dτp+2 = 0 and D(A + R)τp+1 = 0 does not give us a higher order scheme. However, it allows us to control the growth of the error so that we can identify the error terms as in (26). This, in turn, allows us to design a postprocessor that extracts order p + 2, as we show in the next subsection.

3.3. Post-processing to recover p + 2 order. In Theorem 1 we showed that the at every time-step tn the error En has the form (26). The leading order term ∆tp+1τnp+1 can be ﬁltered at the end of the computation in a post-processing stage

- as long as τnp+1 lies in a subspace which is “distinct enough” from the exact solution. First we note that for the error to be of order ∆tp+2 the exact solution of the

ODE must have at least p + 2 smooth derivatives, i.e. u(t) ∈ Cp+2. Therefore, up to an error of order p + 2, we can expand the solution as a polynomial of degree p + 1

(27) u(t) =

p+1

j=0

aj(t − tν)j + O(∆tp+2)

- at any point in the interval [tν − ∆t,tν + ∆t]. It is then reasonable to expect that the numerical solution, V n, can be similarly expanded. Our post-processor is built on these observations.


To build the post-processor, we deﬁne the time vector to be the temporal grid points in the last two computation steps:

- (28) ˜t = (tn−1 + c1∆t,...,tn−1 + cs∆t,tn + c1∆t,...,tn + cs∆t)T

=

1tn + (c − 1)∆t 1tn + c∆t

.

The last term in (28) states that the vectors 1tn + (c − 1)∆t and 1tn + c∆t are concatenated into one 2s long vector. Correspondingly, we let

V˜n =

V n−1 V n

and U˜n =

Un−1 Un

i.e., as for the temporal grid, the numerical solutions V n−1 and V n are concatenated into one long vector, and the same is done for the exact solutions Un−1 and Un. Similarly we deﬁne a concatenation of the leading truncation error terms

- (29) τ˜ =

τp+1 τp+1

,

where τp+1 was deﬁned in (12). Note that by (26),

- (30) E˜n =

En−1 En

= τ˜∆tp+1

dju dtj t=t

![image 23](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile23.png>)

n

+ O ∆tp+2 .

Let P0(t − tn),...,Pp+1(t − tn) be a set of polynomials of degree less or equal to p + 1 such that

- (31) span{P0(t − tn),...,Pp+1(t − tn)} = span 1,(t − tn),...,(t − tn)p+1

and that the vectors P0,...,Pp+1 are the projections of P0(t−tn),...,Pp+1(t−tn) onto the temporal grid points ˜t.

Deﬁne the matrix T ∈ C2s×2s as follows; The ﬁrst column is τ˜, the next p + 2 columns are P0,...,Pp+1, and the remaining 2s−(p+3) columns are selected such that T can be inverted. A convenient way to accomplish this is to deﬁne the Vandermonde interpolation matrix on the points in the 2s-length vector ˜t and replace the highest order column (in Matlab the ﬁrst column) by τ˜. The post-processing ﬁlter is then given by

- (32) Φ = T diag

  0,1,...,1

![image 24](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile24.png>)

![image 25](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile25.png>)

p+2

, ∗,...,∗

![image 26](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile26.png>)

![image 27](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile27.png>)

2s−(p+3)

   T−1

Where we select ∗ to be either 1 or 0, if it is desired to keep this subspace or eliminate it, respectively. Note that, by construction, the matrix Φ multiplied to the error vector E˜n eliminates the leading order term τp+1 so that

- (33) ΦE˜n = O ∆tp+2 .


Also by construction, the matrix Φ includes the Vandermonde interpolation matrix up to order p+1 so that if it operates on a polynomial, it will replicate the polynomial

exactly, up to order p + 1. Using the polynomial expansion of U˜n assumed in (27) we then obtain

- (34) ΦU˜n = U˜n + O ∆tp+2 ,

and therefore the numerical solution obtained after the post-processing stage is of order p + 2:

- (35) ΦV˜n = Φ U ˜n + E˜n = U˜n + O ∆tp+2 .


Remark 2. We note that is important that the leading term of the error does not live in the span of these polynomials. In other words, we need τ˜ ∈/ span{P0,...,Pp+1}. It is also important that the leading term of the error does not live too close to the space spanned by these polynomials. The coeﬃcient in the O ∆tp+2 term of (35) depends on the norm of the matrix Φ. This norm, in turn, is related to how far τ˜ is from its projection into the subspace span{P0,...,Ps+1}. To avoid numerical instability, it should be veriﬁed during the design stage that Φ is not “too large”.

Despite the verbose description above, the design of the post-processor matrix is computationally simple. The following Matlab code shows how this postprocessing matrix P is computed: m = 2; % # of intervals TAU = repmat(tau(:,p-1),m,1) ; % truncation error vector gp = c-(m-1:-1:0); % Gridpoints S = (vander(gp(:))); % Polynomial basis S(:,1) = TAU; % Put TAU into basis DD = diag([0,ones(1,length(S)-1)]);% Zero out truncation error Phi = S*DD*inv(S); % Build post-processing matrix

In the preceding discussion we assumed that there are enough points in time in each interval to produce a high enough order polynomial: in other words, we assumed that

2s ≥ p + 3.

When this is not correct (e.g. when we have a scheme with s = 2 that has p = 2, or a scheme with s = 3 that has p = 4) we need to use three repeats of each vector so that

3s ≥ p + 3. In the Matlab code above this is equivalent to choosing m = 3.

4. New error inhibiting schemes with post-processing. Using MATLAB we coded an optimization problem [8] that ﬁnds the coeﬃcients D,A,R that satisfy the consistency and order conditions (23) and the error inhibiting conditions (24) while maximizing such properties as the linear stability region or the strong stability preserving coeﬃcient [11]. In this section we present some new methods obtained by the optimization code. These methods are error inhibiting (i.e. they satisfy (24a)) and one order higher can be extracted by postprocessing (i.e. they satisfy (24b) and (24c) as well).

4.1. Explicit Methods. In this section we present the explicit error inhibiting methods that can be post-processed. For each method we present the coeﬃcients D,A,R. We also give values of the abscissas and the truncation error vector that must be used to construct the postprocessor. We denote an explicit s-step method that

satisﬁes the conditions (24) and can be postprocessed to order p as eEIS+(s,p). If, in addition, the method is also strong stability preserving, we denote it eSSP-EIS+(s,p).

- Explicit error inhibiting method eEIS+(2,4): This explicit two stage error inhibiting method is fourth order if it is post processed, otherwise it gives third order accurate solutions. The coeﬃcients are:

D =

- 1

![image 28](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile28.png>)

- 2


1 1 1 1

, A =

1 12

![image 29](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile29.png>)

−7 17 7 −5

, R =

- 0 0
- 1 0


.

The abscissas are c1 = −13,c2 = 0. The truncation error vector is τ3 = 32455 (1,−1)T . The imaginary axis stability for this method is (−0.6452,0.6452). To post-process

![image 30](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile30.png>)

![image 31](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile31.png>)

this method we take a linear combination of several solutions vˆn = w1vn−2+c

1

+ w2vn−2 + w3vn−1+c

1

+ w4vn−1 + w5vn+c

1

+ w6vn with weights

w1 =

5 108

![image 32](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile32.png>)

, w2 = −

7 54

![image 33](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile33.png>)

, w3 =

35 108

![image 34](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile34.png>)

, w4 =

35 108

![image 35](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile35.png>)

, w5 =

7 54

![image 36](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile36.png>)

, w6 =

103 108

![image 37](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile37.png>)

.

These methods were constructed to maximize the linear stability region. In Figure 1 we show the stability regions of these methods, and compare them to stability regions of the Adams-Bashforth linear multistep methods with corresponding orders given in [10]. When comparing these regions of stability, we need to keep in mind that while the linear multistep methods require only one function evaluation per time step, the general linear methods have intermediate stages at which the function evaluation is computed, which increases the computational cost to get to the ﬁnal time. For example, when looking at the eEIS+(2,4) method we need to compute two stages, so that we require two function evaluations at each time-step. For a fair comparison, the stability regions need to be scaled as well: for this reason, in Figure 1 the ﬁgure presented is visually scaled by the length of V n, in that while for the eEIS+(2,4) method we show the axes as (−1,1), for the fourth order Adams-Bashforth method the axes are (−0.5,0.5). Similarly, the axes for the eEIS+(3,6) are (−1,1) while for the corresponding sixth order Adams-Bashforth method the axes are (−0.33,0.33), and for the eEIS+(5,7) the axes are (−2.5,2.5) and the corresponding seventh order Adams-Bashforth method has axes (−0.5,0.5). (Note that for an explicit method, we also may have some elements of F(V n+1) to compute at an intermediate stage, but these will be needed anyway at the next time-step so they do not add to the computational cost.)

- Explicit error inhibiting method eEIS+(3,6): This explicit three stage error inhibiting method is sixth order if it is post processed, otherwise it gives ﬁfth order accurate solutions. The coeﬃcients are:


 

  where

 

  =

 

 

d1 d2 d3 d1 d2 d3 d1 d2 d3

d1 d2 d3

0.844429704970785 0.183161240819666

D =

−0.027590945790451

 

  ,

0.119782131013886 0.530075444729337 0.295068834365335 0.034108245281186 0.972302193339061 −2.090901330553469

A =

−0.067206259640574 1.216836100819247 −0.661223528969050

and

![image 38](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile38.png>)

![image 39](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile39.png>)

![image 40](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile40.png>)

![image 41](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile41.png>)

![image 42](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile42.png>)

![image 43](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile43.png>)

![image 44](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile44.png>)

![image 45](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile45.png>)

![image 46](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile46.png>)

![image 47](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile47.png>)

![image 48](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile48.png>)

![image 49](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile49.png>)

![image 50](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile50.png>)

![image 51](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile51.png>)

![image 52](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile52.png>)

![image 53](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile53.png>)

![image 54](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile54.png>)

![image 55](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile55.png>)

![image 56](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile56.png>)

![image 57](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile57.png>)

![image 58](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile58.png>)

![image 59](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile59.png>)

![image 60](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile60.png>)

![image 61](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile61.png>)

![image 62](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile62.png>)

![image 63](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile63.png>)

![image 64](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile64.png>)

![image 65](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile65.png>)

![image 66](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile66.png>)

![image 67](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile67.png>)

![image 68](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile68.png>)

![image 69](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile69.png>)

![image 70](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile70.png>)

![image 71](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile71.png>)

![image 72](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile72.png>)

![image 73](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile73.png>)

![image 74](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile74.png>)

![image 75](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile75.png>)

![image 76](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile76.png>)

![image 77](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile77.png>)

![image 78](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile78.png>)

![image 79](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile79.png>)

![image 80](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile80.png>)

![image 81](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile81.png>)

![image 82](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile82.png>)

![image 83](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile83.png>)

![image 84](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile84.png>)

![image 85](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile85.png>)

![image 86](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile86.png>)

![image 87](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile87.png>)

![image 88](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile88.png>)

![image 89](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile89.png>)

![image 90](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile90.png>)

![image 91](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile91.png>)

Fig. 1. Stability regions os the eEIS+(2,4) (left), eEIS+(3,6) (middle), and eEIS+(5,7) (left). Bottom: stability regions of Adams Bashforth methods of the corresponding orders.

 

 .

0 0 0 2.464399360954857 0 0 0.210685805002394 1.137368201889378 0

R =

The abscissas are c1 = −0.891535334604278, c2 = −0.456552374616537, c3 = 0. The truncation error vector is:

τ5 = (0.002851625181111,−0.041196333074551,−0.186205087415322)T . The imaginary axis stability for this method is (−0.5985,0.5985) To post-process this method we take a linear combination of several numerical solutions:

+ w5vn+c

+ w3vn−1 + w4vn+c

+ w2vn−1+c

vˆn = w1vn−1+c

+ w6vn

2

1

2

1

with weights: w1 = −0.022895756757277 w2 = 0.147460773700033 w3 = −1.004504454589247 w4 = 1.014066366026382 w5 = −0.155617960794494 w6 = 1.021491032414602.

Explicit error inhibiting method eEIS(5,7): This explicit three stage error inhibiting method is seventh order if it is post processed, otherwise it gives sixth order accurate solutions. The coeﬃcients are given in the full 5 × 5 matrices D,A, and the strictly lower triangular matrix R. The coeﬃcients in these matrices are:













d1 d2 d3 d4 d5 d1 d2 d3 d4 d5 d1 d2 d3 d4 d5 d1 d2 d3 d4 d5 d1 d2 d3 d4 d5

d1 d2 d3 d4 d5

−1.011623735666550 1.095449867712963 1.789431260361622

D =

where

=

 

 

 

 

 

 

−0.872726291980225 −0.000531100427809

a11 = 0.542403428557849, a12 = −0.760948514260222, a13 = 0.540150963081669, a14 = 0.159072579950024, a15 = 0.391433932478452, a21 = 0.156488609423175, a22 = −0.242186890762633, a23 = 0.247855775765120, a24 = 0.363064760009647, a25 = 0.314695085548473,

a31 = −0.052321607410313, a32 = 0.097345632885763, a33 = −0.221816006761698, a34 = 0.900744500805372, a35 = −0.013037891925596, a41 = 0.396379418407651, a42 = −0.498665400266501, a43 = 0.102234339427055, a44 = 0.658422701253808, a45 = −0.027557926231150, a51 = 1.449809317440111, a52 = −1.855043289819523, a53 = 0.795025316417296, a54 = 0.015237452869142, a55 = 0.383077291565467.

r21 = .067750736449434, r31 = −0.970866150021656, r32 = 1.411026181526863, r41 = 1.110541182884615, r42 = −0.861259710862469, r43 = 0.461581912124537, r51 = 0.142695702867824, r52 = 0.803890471392162, r53 = −1.532866050532452, r54 = 1.507618973979455, and rij = 0 whenever j ≥ i.

The abscissas are c1 = −0.837332796371710, c2 = −0.801777109746265, c3 = −0.558370527080746, c4 = −0.367768669441936, with c5 = 0. The truncation error vector is:





−2.452136279362326× 10−3 −9.952624484663908× 10−4 −6.583335089187866× 10−3 −1.186500759891287× 10−2 −6.616898102859160× 10−2

τp+1 =

 

 

The imaginary axis stability for this method is (−2.0047,2.0047). To post-process this method we take a linear combination of several numerical solutions: vˆn = w1vn−1+c

+w7vn+c

+w5vn+w6vn+c

+w4vn−1+c

+w3vn−1+c

+w2vn−1+c

+ w8vn+c

2

1

4

3

2

1

+ w9vn+c

+ w10vn

4

3

with weights: w1 = −0.108041130714896, w2 = 0.161475977012818, w3 = −0.205996099378955, w4 = 0.317344948221968, w5 = −1.213968428247239, w6 = 6.439151511599838, w7 = −5.691821046332016, w8 = 0.366796920786556, w9 = −0.066491551558718, w10 = 1.001548898610644.

Strong stability preserving methods [11] are of interest for the time evolution of hyperbolic problems with shocks or sharp gradients. These high order time-stepping methods preserve the nonlinear, non-inner-product strong stability properties of the spatial discretization coupled with forward Euler time-stepping. The following two methods show that it is possible to combine the EIS+ and SSP properties in a given method.

- Explicit SSP error inhibiting method eSSP-EIS(3,4) This explicit three step error inhibiting method is fourth order if it is post processed, otherwise it gives third order accurate solutions. This method is strong stability preserving (SSP) with SSP coeﬃcient C = 0.7478. The coeﬃcients of this method are:


 

d1 d2 d3 d1 d2 d3 d1 d2 d3

D =

  where

 

 

0.481236169483274 0 0.518763830516726

 

 

0 0 0.693711877859443 0.081596114968722 0 0.333227135691426 0.167078858485521 0 0.331269986340461

A =

 

 

0 0 0 0.642348436974698 0 0 0.254975180593489 0.530807045380761 0

R =

The abscissas are c1 = −0.590419192940789, c2 = −0.226959383165386, c3 = 0. The truncation error vector is

τp+1 = 10−2 × (−5.591881250375826,−5.080104811229902,5.187361482884723). To post-process this method we take a linear combination of several numerical solutions: vˆn = w1vn−1+c

+ w2vn−1+c

+ w3vn−1 + w4vn+c

+ w5vn+c

+ w6vn

1

2

1

2

with weights: w1 = −0.052886551536914, w2 = 0.381993090397787, w3 = −0.580050146506483 w4 = 0.439879549713232, w5 = −0.283052417950462, w6 = 1.094116475882841.

The SSP coeﬃcient of this method compares favorably to the SSP coeﬃcients of linear multistep methods: to obtain a fourth order linear multistep method we need ﬁve steps and the SSP coeﬃcient is small: C = 0.021. Even a linear multistep method with ﬁfty steps has a smaller SSP coeﬃcient C = 0.561. However, a comparison with Runge–Kutta methods is less favorable: the low storage three-stage third order ShuOsher SSP Runge–Kutta method has SSP coeﬃcient C = 1 with the same number of function evaluations and lower storage. Scaled by the number of function evaluations we obtain an eﬀective SSP coeﬃcient of C/3 ≈ 0.33, whereas our current method has an eﬀective SSP coeﬃcient C/3 ≈ 0.25. Our method is still competitive here because it is fourth order rather than third. However, if we compare to the ﬁve stage fourth order SSP Runge–Kutta method which has SSP coeﬃcient C = 1.5, (C/5 = 0.3), or to the low storage ten stage fourth order SSP Runge–Kutta method has SSP coeﬃcient C = 6 (C/10 = 0.6), our method is not as eﬃcient. The more correct comparison is to multi-step Runge–Kutta methods in [2]: the three-stage, three-step fourth order method here has an eﬀective SSP coeﬃcient C/3 ≈ 0.39, which is higher than the eSSP-EIS(3,4).

- Explicit SSP error inhibiting method eSSP-EIS(4,5) This four stage error inhibiting methods is ﬁfth order if it is post processed, otherwise it gives fourth order accurate solutions. This method is strong stability preserving (SSP) with SSP coeﬃcient C = 0.643897 (or an eﬀective SSP coeﬃcient C/4 ≈ 0.16). This method is interesting because all SSP multistep methods require at least seven steps for ﬁfth order and have very small SSP coeﬃcients which make them ineﬃcient. There are no ﬁfth order SSP Runge–Kutta methods [11], however we can compare this method with the SSP multistep multistage methods in [2]: where the corresponding four step four stage method has eﬀective SSP coeﬃcient C/4 = 0.38436, which is more eﬃcient.


The coeﬃcients of the eSSP-EIS(4,5) are:

  

D =

d1 d2 d3 d4 d1 d2 d3 d4 d1 d2 d3 d4 d1 d2 d3 d4

   where

  

d1 d2 d3 d4

  

   =

0.391361993111787 0.065690723540339 0.209839489692975 0.333107793654898

  

  

A =

0.111982379086567 0 0 0.517330861095791 0.144956804626331 0 0 0.200688177229557 0.039506390225419 0.074215962133829 0.237072128025406 0.190419328868168 0.013111528886920 0.067038414113032 0.296412681422031 0.277723998040954

16

  

  

R =

  

0 0 0 0 0.602472175831079 0 0 0 0.164197196121254 0.423264977696018 0 0 0.054494380980164 0.140474767505132 0.515429866206022 0

The abscissas are c1 = −0.735372396971898, c2 = −0.416568479467288, c3 = −0.236009654084161, and c4 = 0. The truncation error vector is

  

   × 10−2

−1.648864820077294 −4.617774532209270 0.7007842214544382 2.406415533885425

τp+1 =

To post-process this method we take a linear combination of several numerical solutions:

+w7vn+c

+w6vn+c

+w4vn−1+w5vn+c

+w3vn−1+c

+w2vn−1+c

vˆn = w1vn−1+c

+w8vn

![image 92](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile92.png>)

3

2

1

3

2

1

with weights: w1 = −0.052886551536914, w2 = 0.381993090397787, w3 = −0.580050146506483

- w4 = 0.439879549713232, w5 = −0.283052417950462, w6 = 1.094116475882841.


Remark 3. It is important to note that although these methods are SSP, the postprocessor is not guaranteed to preserve the strong stability properties of the solution. It is entirely possible that the O(∆tp+1) accurate solution at the ﬁnal time will satisfy the strong stability property of interest and the post-processed solution will not. In practice, this is not a major concern for the following reasons:

- 1. The post-processor is applied only once at the end of the simulation, and only impacts the solution at the ﬁnal time. Typically, the strong stability properties we require are only important for the stability of the time evolution, but not necessarily needed at the ﬁnal time. In such cases, the nonlinear strong stability properties that we are concerned about (e.g. positivity or totalvariation boundedness) are critical to the time-evolution itself. If the timestepping method is not SSP, the code may crash due to non-physical negative values in some of the quantities (such as pressure or density), or the method may become unstable due to non-physical oscillations which grow and destroy the solution. However, a post-processor that is applied only once at the end of the time-simulation will not impact the nonlinear stability of the timeevolution and so is not of concern. Furthermore, if the ﬁnal post-processing step results in a solution that has undesired characteristics, this higher order solution can be ignored.
- 2. The post-processing step is a simple projection that, as we saw above, changes the solution only on the order of ∆tp+1. Thus, any violation of the strong stability properties are only at the level of O(∆tp+1), which is very small and thus will not have major impact on the strong stability properties of the solution.


These arguments are validated in our numerical tests, where we see that the postprocessing does not have an adverse impact on the simulations and leads to very small diﬀerences in the strong stability properties of interest between the ﬁnal time solution and the post-processed solution.

4.2. Implicit Methods. In this section we present several implicit error inhibiting methods that can be post-processed. For each method we present the coeﬃcients D,A,R, as well as values of the abscissas and the truncation error vector that must be used to construct the postprocessor. We denote an implicit s-step method that satisﬁes the conditions (24) and can be postprocessed to order p as iEIS+(s,p). All the methods we present are A-stable, so we do not show their stability regions here.

A-stable implicit method iEIS+(2,3). This A-stable implicit two stage error inhibiting method is third order if it is post processed, otherwise it gives second order accurate solutions. The coeﬃcients are given in:

D =

2 −1 2 −1

1 12

, A =

![image 93](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile93.png>)

13 −14 16 −24

1 12

, R =

![image 94](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile94.png>)

19 0 24 8

.

Here the abscissas are c1 = −21,c2 = 0, and the truncation error vector is τ = 8 3, 34 T . To post-process this method we take a linear combination of several numerical solu-

![image 95](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile95.png>)

![image 96](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile96.png>)

![image 97](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile97.png>)

tions:

3 2

- 1

![image 98](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile98.png>)

- 2


- 1

![image 99](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile99.png>)

- 2


3 2

3

- 1

![image 100](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile100.png>)

- 2 +


vn−1 +

vˆn =

vn−

vn−

vn.

2 −

![image 101](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile101.png>)

![image 102](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile102.png>)

![image 103](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile103.png>)

The cost of the implicit solve is often non-trivial, and the computation can be speeded up if the method admits an eﬃcient parallel implementation. For this reason, we added the requirement in our optimization code that R is a diagonal matrix. All the following methods are eﬃcient when implemented in parallel.

- Parallel-eﬃcient A-stable implicit method iEIS+(2,3). This two stage error inhibiting method is third order if it is post processed, otherwise it gives second order accurate solutions. This method is A-stable implicit with diagonal R allowing the implicit solves to be performed concurrently. The coeﬃcients are given in:

D =

1 15

![image 104](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile104.png>)

16 −15 16 −15

, A =

1 480

![image 105](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile105.png>)

75 106 −1440 736

, R =

1 32

![image 106](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile106.png>)

21 0 0 96

.

Here the abscissas are c1 = −21,c2 = 0, and the truncation error vector is τ =

![image 107](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile107.png>)

1 120,(31,496)T . To post-process this method we take a linear combination of several numerical solutions:

![image 108](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile108.png>)

vˆn =

4 15

![image 109](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile109.png>)

vn−

3

![image 110](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile110.png>)

2 −

- 4

![image 111](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile111.png>)

- 5


vn−1 +

- 4

![image 112](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile112.png>)

- 5


vn−

- 1

![image 113](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile113.png>)

- 2 +


11 15

![image 114](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile114.png>)

vn.

- Parallel-eﬃcient A-stable implicit method iEIS+(3,4) This three stage error inhibiting method is fourth order if it is post processed, otherwise it gives third order accurate solutions. This method is A-stable implicit with diagonal R allowing the implicit solves to be performed concurrently. The coeﬃcients are given in:


 

  where

 

 

d1 d2 d3 d1 d2 d3 d1 d2 d3

1.100594730800523 −0.335370831614021 0.234776100813498

D =

 

 

- 0.806950212712456 −0.386181733528596 −0.182046279153154 2.687898652721551 −1.944296251569286 −1.165162710461159
- 1.052813949541399 −0.265689012035030 −0.052553462549502


A =

 

0.716550676631637 0 0 0 1.710166519304569 0 0 0 0.887368068372141

R =

 

Here the abscissas are c1 = −23,c2 = −31,c3 = 0, and the truncation error vector is τ = (0.278446186799822,1.535336949555884,0.887870711092943)T .

![image 115](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile115.png>)

![image 116](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile116.png>)

To post-process this method we take a linear combination of several numerical solutions: vˆn = w1vn−1+c

+ w2vn−1+c

+ w3vn−1 + w4vn+c

+ w5vn+c

+ w6vn

1

2

1

2

with weights: w1 = −0.133267324186142, w2 = 0.666336620930711, w3 = −1.332673241861424,

- w4 = 1.332673241861424, w5 = −0.666336620930712, w6 = 1.133267324186142.


- Parallel-eﬃcient A-stable implicit method iEIS+(4,5). This four stage error inhibiting method is ﬁfth order if it is post processed, otherwise it gives fourth order accurate solutions. This method is A-stable implicit with diagonal R allowing the implicit solves to be performed concurrently. The coeﬃcients are given in:


  

D =

  

R =

and:

  

A =

   where

d1 d2 d3 d4 d1 d2 d3 d4 d1 d2 d3 d4 d1 d2 d3 d4

   where

r1 0 0 0 0 r2 0 0 0 0 r3 0 0 0 0 r4

  

   =

d1 d2 d3 d4

  

  

   =

- r1
- r2
- r3
- r4


  

  

−2.189053680903935

3.606949225806165 −0.710842571233197

0.292947026330966

  

0.243205109444297 0.428641943283907 1.223508778356526 0.861606621761651

0.542633235622690 0.572906890966515 −0.147775065138658 0.108270009767368 −0.935354930827541 1.187517922840311 0.040246733851822 −0.237077959731666 −3.856502347754360 5.000000000000000 3.366967278814666 −5.000000000000000 −3.605680346039871 4.951687114045852 1.612027197556519 −2.835666877907317

  

Here the abscissas are c1 = −43,c2 = −21,c3 = −41,c4 = 0, and the truncation error vector is

![image 117](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile117.png>)

![image 118](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile118.png>)

![image 119](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile119.png>)

   .

  

0.044949370534240 0.165996341680758 1.268926100495425 1.371111036428543

τp =

To post-process this method we take a linear combination of several numerical solutions:

7

3

5

- 3

![image 120](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile120.png>)

- 4 + w6vn−


- 1

![image 121](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile121.png>)

- 2 + w7vn−


1

4 + w4vn−1 + w5vn−

vˆn = w1vn−

4 + w2vn−

2 + w3vn−

4 + w8vn

![image 122](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile122.png>)

![image 123](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile123.png>)

![image 124](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile124.png>)

![image 125](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile125.png>)

with weights: w1 = 0.081324340500950, w2 = −0.569270383506653, w3 = 1.707811150519959, w4 = −2.846351917533271, w5 = 2.846351917533285, w6 = −1.707811150519988, w7 = 0.569270383506672, w8 = 0.918675659499045.

5. Numerical Results. In this section we test the methods presented in Section 4 on a selection of numerical test cases. Most of the numerical studies are designed to show that the methods achieve the desired convergence rates on nonlinear scalar and systems of ODEs, as well as systems of ODEs resulting from semi-discretizations of PDEs. We also explore the behavior of the SSP methods in terms of preserving the total variation diminishing properties of the spatial discretizations, and the issue of order reduction that occurs in implicit methods.

5.1. Comparison of explicit schemes. In Section 4.1 we presented several explicit EIS schemes that can be post-processed to attain higher order. Here we demonstrate that these methods attain the design order of convergence on several standard test cases. From the point of view of practical implementation, we are interested in the computational cost needed to attain a certain level of accuracy. To compute this, we look at the number of time-steps needed with and without postprocessing to attain an error of a given size. Since the cost of post-processing is a linear combination of some solutions, we consider this cost to be at most that of one function evaluation. We comment on the the relative cost to achieve a certain accuracy, and show that using the post-processor enables a far more eﬃcient computation.

Nonlinear scalar ODE: We compare the performance of several two-step schemes on the nonlinear ODE

y′ = −y2 with initial condition y(0) = 2. The methods we consider here are:

- • A non-EIS two step second order method presented by Butcher in [3]

V n+1 =

1 4

![image 126](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile126.png>)

−3 7 −3 7

V n +

∆t 8

![image 127](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile127.png>)

−3 −3 −7 9

F(V n)

abscissas are c1 = 1,c2 = 2. (Note that the abscissas are diﬀerent in John Butcher’s formulation).

- • An eEIS(2,3) method presented in [6]

V n+1 =

1 6

![image 128](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile128.png>)

7 −1 7 −1

V n +

∆t 24

![image 129](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile129.png>)

1 125 −17 55

F(V n)

abscissas are c1 = −21,c2 = 0.

![image 130](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile130.png>)

- • The eEIS+(2,4) method presented in Section 4.1.


Figure 2 shows the convergence history of each of these methods. The non-EIS method by Butcher (in cyan) shows clear second order, while the EIS method (in green) shows third order. The eEIS+(2,4) method (blue, denoted EIS+ in legend) is third order as well, but with a smaller error constant. Finally, when the results of the eEIS+(2,4) method for the ﬁnal time Tf = 1.0 are postprocessed ( dashed blue line), fourth order convergence is obtained (denoted EIS+1 and EIS+2 in legend, respectively).

Non-stiﬀ Van der Pol oscillator: The nonlinear system of ODEs is given by

- y1
- y2


′

=

y2 (1 − y12)y2 − y1

with initial condition y(0) = (2,0)T. We use the explicit methods eEIS+(2,4), eEIS+(3,6), eEIS+(5,7) to evolve this problem to the ﬁnal time Tf = 2.0 and postprocess the solution at the ﬁnal time as described in Section 3.3. In Figure 3 we show the errors for diﬀerent values of ∆t for y1 on the left and y2 on the right. The errors before post-processing are in solid lines, after post-processing are dashed lines. The slopes of these lines are computed using MATLAB’s polyfit function and are shown in the legend. This example veriﬁes that numerical solutions from the eEIS+ methods attain the expected orders of convergence with and without post-processing.

- -2.8 -2.6 -2.4 -2.2 -2 -1.8 -1.6 -1.4

- -10
- -8
- -6
- -4
- -2


Fig. 2. Convergence of several two-step schemes on a nonlinear scalar test problem. On the x-axis is log10 of time-step and on the y-axis is log10 of the errors. The non-EIS method by Butcher (in cyan solid) shows second order convergence , while the EIS method (in green solid) shows third order. The eEIS+(2,4) method (blue solid) is third order as well, but with a smaller error constant. Finally, when the results of the eEIS+(2,4) method for the ﬁnal time Tf = 1 are post-processed (blue dashed), fourth order convergence is obtained.

We also see the impact of post-processing here: to attain an accuracy of 10−6 the eEIS+(2,4) method with no post-processing requires a stepsize ∆t ≈ 0.0137, or approximately 145 time-steps which constitute 290 function evaluations. In comparison, the eEIS+(2,4) method with post-processing will attain an accuracy of 10−6 with a stepsize ∆t ≈ 0.0317, or approximately 63 time-steps which means 126 function evaluations. The additional cost of post-processing is less than one function evaluation, so we obtain a speedup of a factor of about 2.28. For the eEIS+(3,6) method to attain a level of accuracy of 10−9, we require 158 time-steps without post-processing and 91 time-steps with the post-processor. If we count the cost of the post-processing as one function evaluation, using the post-processor gives us a speedup of a factor of 1.72. For the eEIS+(5,7) method to attain a level of accuracy of 10−11, we require 132 time-steps without post-processing and 75 time-steps with post-processor. Once again, if we count the cost of the post-processing as one function evaluation, using post-processor gives us a speedup of a factor of 1.75.

Advection-diﬀusion problem: We solve the advection–diﬀusion problem ut + aux = buxx with periodic boundary conditions u(0,t) = u(2π,t) and initial condition

u(x,0) = sin(5x). Here we use a = 1.0 and b = 0.1. We discretize the problem in space with N = 41

0

- -12
- -10
- -8
- -6
- -4
- -2


- -2 -1.8 -1.6 -1.4 -1.2 -1 -0.8
- -12
- -10
- -8
- -6
- -4
- -2


-2 -1.8 -1.6 -1.4 -1.2 -1 -0.8

Fig. 3. Convergence of the postprocessed solution from evolving the Van der Pol system to

time Tf = 2.0 using eEIS+(2,4) (blue), eEIS+(3,6) (red), and eEIS+(5,7) (green) methods for the non-stiﬀ Van der Pol system. The errors before post-processing are in solid lines (slopes given by

m), after post-processing are dashed lines. Left: the log10 errors in the ﬁrst element, y1, for various time-steps. Right: the same for the second element y2.

points using a Fourier spectral method to obtain the ODE

y′ = −Dx +

1 10

Dx2 y,

![image 131](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile131.png>)

where Dx is the ﬁrst order Fourier diﬀerentiation matrix and Dx2 is the second order Fourier diﬀerentiation matrix. Due to the periodicity of this problem, the spatial diﬀerentiation is exact and so the errors arise only from the time evolution of this ODE.

We evolve this problem forward to ﬁnal time Tf = 1.0 using the eEIS+(s,p) methods presented in Section 4.1 with ∆t = Tf/M, and postprocess the solution at the ﬁnal time as described in Section 3.3. In Table 1 we show the errors for diﬀerent values of M = 1/∆t before and after postprocessing. We observe that the errors are of the predicted EIS order (which is one order higher than predicted by a truncation error analysis) before post-processing and gain an order after postprocessing, as expected.

Notice that post-processing gives us much better accuracy for a very small price: for example, using the eEIS+(2,4) method without post-processing with 300 timesteps (∆t ≈ 0.0033) we obtain an error of 2.16 × 10−7. but if we use the eEIS+(2,4) method with post-processoring, we need only 150 time-steps (∆t ≈ 0.0066) to obtain an even smaller error of 1.96 × 10−7. Clearly, using the post-processor speeds up our time to a solution of desired accuracy by slightly more than a factor of two. Similarly, using the eEIS+(3,6) we can obtain a ﬁnal-time solution of accuracy 6.90 × 10−12 without post-processing using 300 time-steps, while with post-processing we require only 200 time-steps to obtain a ﬁnal-time solution of accuracy 7.34 × 10−12. Finally, using the eEIS+(5,7) we can obtain a ﬁnal-time solution of accuracy 2.22 × 10−10 without post-processing using 55 time-steps, while with post-processing we require only 45 time-steps to obtain a better ﬁnal-time solution of accuracy 1.43 × 10−10. Using these methods with time-stepping allows for a more eﬃcient production of an accurate solution.

Next, we study the SSP properties of the eSSP-EIS+ schemes presented in Section 4.1. To do so, we look at a problem where the spatial discretization is total variation

![image 132](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile132.png>)

![image 133](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile133.png>)

![image 134](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile134.png>)

![image 135](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile135.png>)

![image 136](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile136.png>)

![image 137](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile137.png>)

at ﬁnal time post-processessor method M error order error order

![image 138](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile138.png>)

![image 139](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile139.png>)

![image 140](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile140.png>)

![image 141](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile141.png>)

![image 142](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile142.png>)

![image 143](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile143.png>)

![image 144](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile144.png>)

- eEIS+(2,4) 100 6.52×10−6 – 1.01×10−6 – 150 1.83×10−6 3.13 1.96×10−7 4.04 200 7.52×10−7 3.09 6.16×10−8 4.03 250 3.78×10−7 3.07 2.50×10−8 4.02 300 2.16×10−7 3.06 1.20×10−8 4.02

![image 145](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile145.png>)

![image 146](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile146.png>)

![image 147](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile147.png>)

![image 148](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile148.png>)

![image 149](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile149.png>)

![image 150](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile150.png>)

![image 151](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile151.png>)

![image 152](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile152.png>)

![image 153](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile153.png>)

![image 154](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile154.png>)

![image 155](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile155.png>)

![image 156](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile156.png>)

![image 157](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile157.png>)

![image 158](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile158.png>)

![image 159](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile159.png>)

![image 160](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile160.png>)

![image 161](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile161.png>)

![image 162](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile162.png>)

![image 163](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile163.png>)

![image 164](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile164.png>)

![image 165](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile165.png>)

![image 166](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile166.png>)

![image 167](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile167.png>)

![image 168](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile168.png>)

![image 169](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile169.png>)

![image 170](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile170.png>)

- eEIS+(3,6) 100 1.94×10−9 – 4.90×10−10 – 150 2.37×10−10 5.18 4.19×10−11 6.06 200 5.44×10−11 5.12 7.34×10−12 6.05 250 1.74×10−11 5.09 1.91×10−12 6.02 300 6.90×10−12 5.08 6.52×10−13 5.90


![image 171](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile171.png>)

![image 172](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile172.png>)

![image 173](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile173.png>)

![image 174](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile174.png>)

![image 175](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile175.png>)

![image 176](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile176.png>)

![image 177](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile177.png>)

![image 178](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile178.png>)

![image 179](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile179.png>)

![image 180](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile180.png>)

![image 181](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile181.png>)

![image 182](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile182.png>)

![image 183](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile183.png>)

![image 184](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile184.png>)

![image 185](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile185.png>)

![image 186](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile186.png>)

![image 187](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile187.png>)

![image 188](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile188.png>)

![image 189](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile189.png>)

![image 190](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile190.png>)

![image 191](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile191.png>)

![image 192](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile192.png>)

![image 193](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile193.png>)

![image 194](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile194.png>)

![image 195](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile195.png>)

![image 196](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile196.png>)

eEIS+(5,7) 35 3.34×10−9 – 8.27×10−10 –

![image 197](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile197.png>)

![image 198](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile198.png>)

![image 199](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile199.png>)

![image 200](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile200.png>)

![image 201](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile201.png>)

40 1.50×10−9 6.00 3.25×10−10 6.97 45 7.41×10−10 5.99 1.43×10−10 6.98 50 3.94×10−10 5.99 6.86×10−11 6.98 55 2.22×10−10 5.99 3.52×10−11 6.99

![image 202](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile202.png>)

![image 203](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile203.png>)

![image 204](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile204.png>)

![image 205](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile205.png>)

![image 206](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile206.png>)

![image 207](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile207.png>)

![image 208](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile208.png>)

![image 209](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile209.png>)

![image 210](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile210.png>)

![image 211](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile211.png>)

![image 212](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile212.png>)

![image 213](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile213.png>)

![image 214](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile214.png>)

![image 215](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile215.png>)

![image 216](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile216.png>)

![image 217](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile217.png>)

![image 218](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile218.png>)

![image 219](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile219.png>)

![image 220](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile220.png>)

![image 221](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile221.png>)

![image 222](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile222.png>)

Table 1

Convergence of the solution from evolving the advection-diﬀusion equation problem to time Tf = 1 using diﬀerent eEIS methods with and without post-processing.

diminishing when coupled with forward Euler time-stepping, and examine the maximal rise in total variation when this problem is evolved forward with an eSSP-EIS+ scheme.

SSP study: As two of our explicit methods are strong stability preserving, we demonstrate their ability to preserve the total variation diminishing property of a ﬁrst-order upwind spatial diﬀerence applied to Burgers’ equation with step function initial conditions:

ut +

- 1

![image 223](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile223.png>)

- 2


u2

= 0 u(0,x) =

x

1, if 0 ≤ x ≤ 1/2 0, if x > 1/2

on the domain [0,1] with periodic boundary conditions. We used a ﬁrst-order upwind diﬀerence to semi-discretize, with 200 spatial points, the nonlinear spatial terms

- N(u) ≈ − 12u2 x. We evolve the solution 10 time-steps using the SSP methods eSSP-EIS(3,4) and


![image 224](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile224.png>)

eSSP-EIS(4,5) for diﬀerent values of ∆t. At each time-level yn we compute the total variation of the solution at time un,

un TV =

j

unj+1 − unj .

The maximal rise in total variation (solid line with circle markers) is graphed against λ = ∆∆xt in Figure 4. We then post-process the solution at the ﬁnal time for all values of ∆t before the total variation begins to rise, and compute the diﬀerence between the total variation of the solution at the ﬁnal time and the postprocessed solution

![image 225](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile225.png>)

un TV − un TV

In the left graph of Figure 4 we see that the eSSP-EIS(3,4) preserves the total variation diminishing property up to λ ≈ 1.2 (larger than the predicted value of

5

5

0

0

- -15
- -10
- -5


- -15
- -10
- -5


0 0.2 0.4 0.6 0.8 1 1.2 1.4

0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6

Fig. 4. SSP study: the eSSP-EIS methods were used to evolve forward the solution in time of Burgers’ equation with a step function initial conditions. On the y-axis is log10 of the maximal rise in total variation, and on the x-axis the CFL number λ. The blue solid line is the maximal rise in total variation from the eSSP-EIS method without post-processing. The cyan dotted line is the maximal rise in total variation from the non-SSP method. The red dashed line is the diﬀerence between the total variation of the un-processed solution and that of the post-processed solution. Left: eSSP-EIS+(3,4) compared to the eEIS+(2,4) method. Right: eSSP-EIS+(4,5) compared to the implicit eEIS+(4,5) method.

λ ≤ 0.75). We compare the maximal rise in total variation from the eSSP-EIS(3,4) method (blue solid line) to the maximal rise in total variation from the eEIS(2,4) method (cyan dashed line), which is not SSP, and indeed we see that the total variation is comparatively large for even small values of ∆t. The maximal diﬀerence between the total variation of the solution and the post-processed solution (red dashed line) also remains small (≈ 10−14).

On the right graph of Figure 4 we see that the eSSP-EIS(4,5) preserves the total variation diminishing property up to λ ≈ 1.16 (larger than the predicted value of λ ≤ 0.63). We compare the eSSP-EIS(4,5) method to the implicit non-SSP iEIS+(4,5) method presented in Section 4.2. Clearly, the maximal rise in total variation of the implicit non-SSP method (dotted cyan line) is large for any ∆t, while the maximal rise in total variation from the eSSP-EIS(4,5) method (blue solid line) remains very small (≈ 10−15) up to λ ≈ 1.16. The maximal diﬀerence between the total variation of the solution and the post-processed solution (red dashed line) also remains small (≈ 10−14).

We see that the diﬀerence between the total variation of the solution at the ﬁnal time and the postprocessed solution is minimal for almost all the values of ∆t for which the maximal rise in total variation remains bounded. We observe a jump in total variation of the post-processed solution occurs for a slightly smaller ∆t than the value at which we observe the jump in the total variation of the un-processed solution un. Although the method itself was designed to be SSP, the post-processor is only designed to extract a higher order solution but not to preserve the strong stability properties. This is not a concern because preserving the nonlinear stability properties is generally only important for the stability of the time evolution: once we reach the ﬁnal time solution these properties are no longer needed. Although we do not expect the post-processor to preserve the nonlinear stability properties that the time-evolution does preserve, it is pleasant to see that for this case it does indeed do so for most relevant values of ∆t.

5.2. Comparison of implicit schemes. In Section 4.2 we presented implicit EIS schemes that can be post-processed to attain higher order. Here we demonstrate that these methods attain the design order of convergence on several standard test cases, and show that although these methods suﬀer from order reduction (as expected from implicit schemes that have lower stage order than overall order) the size of the errors is still small.

![image 226](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile226.png>)

![image 227](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile227.png>)

![image 228](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile228.png>)

![image 229](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile229.png>)

![image 230](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile230.png>)

![image 231](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile231.png>)

![image 232](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile232.png>)

at ﬁnal time post-processor at ﬁnal time post-processor iEIS+(2,3) iEIS+(2,3)p

![image 233](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile233.png>)

![image 234](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile234.png>)

![image 235](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile235.png>)

![image 236](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile236.png>)

![image 237](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile237.png>)

![image 238](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile238.png>)

![image 239](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile239.png>)

![image 240](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile240.png>)

![image 241](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile241.png>)

![image 242](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile242.png>)

![image 243](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile243.png>)

![image 244](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile244.png>)

![image 245](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile245.png>)

![image 246](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile246.png>)

M error order error order error order error order 100 8.95×10−4 – 8.49×10−5 – 4.48×10−3 – 3.20×10−4 – 150 3.95×10−4 2.02 2.50×10−5 3.01 2.04×10−3 1.94 9.79×10−5 2.92

![image 247](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile247.png>)

![image 248](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile248.png>)

![image 249](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile249.png>)

![image 250](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile250.png>)

![image 251](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile251.png>)

![image 252](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile252.png>)

![image 253](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile253.png>)

![image 254](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile254.png>)

![image 255](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile255.png>)

![image 256](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile256.png>)

![image 257](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile257.png>)

![image 258](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile258.png>)

![image 259](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile259.png>)

![image 260](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile260.png>)

- 200 2.21×10−4 2.02 1.05×10−5 3.01 1.16×10−3 1.96 4.20×10−5 2.95

![image 261](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile261.png>)

![image 262](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile262.png>)

![image 263](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile263.png>)

![image 264](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile264.png>)

![image 265](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile265.png>)

![image 266](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile266.png>)

![image 267](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile267.png>)

- 250 1.41×10−4 2.01 5.38×10−6 3.01 7.95×10−4 1.97 2.17×10−5 2.96 300 9.78×10−5 2.01 3.11×10−6 3.01 5.23×10−4 1.98 1.26×10−5 2.97

![image 268](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile268.png>)

![image 269](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile269.png>)

![image 270](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile270.png>)

![image 271](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile271.png>)

![image 272](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile272.png>)

![image 273](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile273.png>)

![image 274](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile274.png>)

![image 275](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile275.png>)

![image 276](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile276.png>)

![image 277](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile277.png>)

![image 278](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile278.png>)

iEIS+(3,4)p iEIS+(4,5)p 100 3.29×10−5 – 4.33 ×10−6 – 8.32×10−7 – 5.13×10−8 – 150 9.51×10−6 3.06 8.60×10−7 3.99 1.64×10−7 4.01 7.24×10−9 4.83 200 3.96×10−6 3.04 2.73×10−7 3.99 5.17×10−8 4.00 1.78×10−9 4.88

![image 279](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile279.png>)

![image 280](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile280.png>)

![image 281](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile281.png>)

![image 282](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile282.png>)

![image 283](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile283.png>)

![image 284](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile284.png>)

![image 285](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile285.png>)

![image 286](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile286.png>)

![image 287](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile287.png>)

![image 288](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile288.png>)

![image 289](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile289.png>)

![image 290](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile290.png>)

![image 291](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile291.png>)

![image 292](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile292.png>)

![image 293](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile293.png>)

![image 294](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile294.png>)

![image 295](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile295.png>)

![image 296](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile296.png>)

![image 297](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile297.png>)

![image 298](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile298.png>)

![image 299](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile299.png>)

![image 300](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile300.png>)

![image 301](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile301.png>)

![image 302](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile302.png>)

![image 303](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile303.png>)

- 250 2.01×10−6 3.03 1.12×10−7 3.99 2.12×10−8 4.00 5.94×10−10 4.91 300 1.16×10−6 3.03 5.40×10−8 3.99 1.02×10−8 4.00 2.42×10−10 4.93




![image 304](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile304.png>)

![image 305](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile305.png>)

![image 306](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile306.png>)

Table 2

Implicit solvers on Advection diﬀusion problem. The step-size is ∆t = 1/M where M is given in the table. Four methods from Section 4.1 are tested. The reference solution is computed by Matlab’s ode45 subroutine.

Advection-diﬀusion problem: We repeat the advection-diﬀusion problem above and evolve the ODE

1 10

Dx2 y,

y′ = −Dx +

![image 307](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile307.png>)

where Dx is the ﬁrst order Fourier diﬀerentiation matrix and Dx2 is the second order Fourier diﬀerentiation matrix based on N = 41 points in space. We use the im-

plicit methods iEIS+(2,3), iEIS+(2,3)p, iEIS+(3,4)p, and iEIS+(4,5)p to evolve this problem to the ﬁnal time Tf = 1.0 and postprocess the solution at the ﬁnal time as described in Section 3.3. Note that ∆t = M1 can be much larger here than when using explicit methods. We compute the reference solution using Matlab’s ode45 subroutine. The numerical tests conﬁrm that we observe the order of accuracy predicated by the EIS theory for the solution and the post-processed solution.

![image 308](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile308.png>)

Prothero–Robinson problem: This problem has been used to reveal the error reduction phenomenon that aﬀects implicit methods. We test our implicit methods on the non-autonomous ODE

dy dt

= −a(y − sin(t)) + cos(t)

![image 309](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile309.png>)

with initial condition y0 = 0. We use the values a = 10 and a = 1000, to show the order reduction phenomenon. We run this problem to ﬁnal time Tf = 1.0 using the iEIS+(s,p)p methods. Note that this problem has the solution y = sin(t) regardless of the value of a, making the comparison easy.

Figure 5 (left) shows that the order of convergence for the case a = 10 is close to the p + 1 design order without post-processing and the enhanced p + 2 with postprocessing. In contrast, the right graph shows that when a = 1000 the convergence rate without post-processing is just what is expected from a truncation error analysis,

0

- -2.2 -2 -1.8 -1.6 -1.4 -1.2 -1 -0.8

- -11
- -10
- -9
- -8
- -7
- -6
- -5
- -4
- -3


- -8
- -6
- -4
- -2


-10

-2.2 -2 -1.8 -1.6 -1.4 -1.2 -1 -0.8 -0.6

Fig. 5. Convergence test on the Prothero Robinson problem. The x-axis has log10 of the timestep while the y-axis has log10 of the errors. On the left is a = 10 and on the right a = 1000.

while after post-processing there is improvement, but the order reduction is still apparent. However, it is important to note that the magnitude of the errors is smaller in the case a = 1000 than when a = 10. In this case, we observe that the order reduction phenomenon is apparent but does not result in an increase of the errors.

6. Conclusions. In this work we extended the EIS framework in [6] to explicit methods that use function evaluations of newly computed values and to implicit methods. More signiﬁcantly, we presented additional conditions on the coeﬃcients of the method that allow the ﬁnal solution to be post-processed in order to extract higher order accuracy. The new EIS conditions (24) not only control the growth of the errors (as we showed in [6]) but also allow us to precisely deﬁne the leading error term. Knowing the form of the leading error term we can compute the post-processor deﬁned in 3.3, and apply it to the solution to extract a solution that is two orders of accuracy higher.

We used the new EIS+ framework to formulate an optimization code in Matlab to ﬁnd methods that satisfy the order and the EIS+ conditions. We presented some of these EIS+ methods and their stability regions and we tested them on sample problems to show their convergence properties. We conﬁrmed that the numerical solutions coming from these methods are indeed one order higher than expected from a truncation error analysis, and two orders higher when post-processed. In future work, we plan to consider other conditions on D,A,R that allow the error inhibiting behavior to occur, to extend this approach to multi-derivative and implicit-explicit methods, and to create variable step-size methods with EIS properties.

Appendix A. An alternative error analysis.

In this section we provide an alternative proof for the accuracy of the proposed schemes. This proof is similar to the the one given in [6]. This proof directly tracks the dynamics of the error, rather than tracking the behavior of the solution, as we did in Section 3.2.

We write the scheme as

- (36) (I − ∆tRF)V n+1 = (D + ∆tAF)V n ,


where we assume, as we did above, that the scheme (5) (equivalently (36) ) is zero– stable, so that the operator (I − ∆tRF)−1 is bounded. In order to evaluate the

operator (I − ∆tRF) we use Lemma 2 to obtain: F(V n+1) = F(Un+1 + En+1)

= F(Un+1) + Fyn+1En+1 + O(∆t)O En+1 + O En+1 2

- (37) = F(Un) + FynEn+1 + O(∆t)O En+1 ,

where, Fyn = Fy(u(tn)) and Fyn+1 = Fy(u(tn+1)).

We now subtract (10) from (36), and use (37) to obtain an equation for the relationship between the errors at two successive time-steps:

- (38) I − ∆tRFyn + O(∆t2) En+1 = D + ∆tAFyn + O(∆t2) En + τn+1 .

For the accuracy analysis we assume that |Fyn| = O(1), and therefore ∆tRFyn = O(∆t) ≪ 1. This observation is then used for approximating

- (39) I − ∆tRF + O(∆t2) −1 = I + ∆tRFyn + O(∆t2). We then plug this into (38) to obtain a linear recursion relation for the error:

En+1 = I − ∆tRFyn + O(∆t2) −1 D + ∆tAFyn + O(∆t2) En + τn+1 ,

= D + ∆tFyn (RD + A) + O(∆t2) En + I + ∆tFynR + O(∆t2) τn+1

- (40) ≡ QˆnEn + ∆tTen , where
- (41) Ten = ∆tpτnp+1+1 + ∆tp+1 τnp+2+1 + FynRτnp+1+1 + O ∆tp+2


Lemma 3. The equation which governs the dynamics of En, (40), is essentially linear in the sense that there is a time interval, 0 ≤ t ≤ T, such that the nonlinear terms are of higher order, and thus much smaller, than the leading terms in the equation.

Proof. It is assumed that the initial numerical condition, V 0, which is derived by the initial condition of the ODE and other schemes, is either accurate to machine precision or, at least accurate as desired. Thus, at n = 0, the scheme is essentially linear.

By assumption, the scheme is zero–stable, therefore

D + ∆tFyn (RD + A) + O(∆t2) ≤ 1 + c∆t ≤ exp(c∆t) and, due to the boundedness of Fyn and R

I + ∆tFynR + O(∆t2) ≤ 2 . Therefore,

exp(c tn) − 1 c∆t

En ≤ 2

τν .

max

![image 310](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile310.png>)

0≤ν≤n

This estimate holds as long as En 2 ≪ O(∆t2)max0≤ν≤n τν .

![image 311](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile311.png>)

![image 312](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile312.png>)

![image 313](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile313.png>)

![image 314](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile314.png>)

As the error equation satisﬁes an iterative process of the form (40), we state the following Lemma that we will use later to understand the dynamics of the growth in the error.

Lemma 4. Given an iterative process of the form

- (42) Wn+1 = QnWn + ∆tF(Wn,tn)

where Qn is a linear operator, the Discrete Duhamel principle states that

- (43) Wn =

n−1

µ=0

QµW0 + ∆t

n−1

ν=0

n−1

µ=ν+1

Qµ F(Wν,tν) .

This is Lemma 5.1.1 in [9] and the proof is given there.

Using the observation that Equation (40), which governs the dynamics of En, is essentially linear, we can use the Discrete Duhamel principle, (43) to calculate En.

- (44) En =


n−1

n−1

n−1

Qˆµ Teν .

QˆµE0 + ∆t

µ=ν+1

ν=0

µ=0

The ﬁrst term in (44) is negligible because we assume that the initial error can be made arbitrarily small. In order to evaluate the second term we divide the sum into three parts:

- 1. The ﬁnal term, ν = n − 1, is ∆tTen−1 which is clearly of order ∆t Ten−1 = τn+1 = O(∆tp+1). This term is the one ﬁltered in the postprocessing stage.
- 2. The next term, ν = n − 2, is ∆tQˆn−1Ten−2. This term can be made of order ∆t2 Ten−2 provided that Q ˆn−1Ten−2 = O (∆t)O Ten−2 which is true due to (24a): Dτp+1 = 0.
- 3. The rest of the sum;


n−1

n−3

n−1

n−3

Qˆµ Q ˆν+2Qˆν+1Teν

Qˆµ Teν = ∆t

∆t

µ=ν+3

ν=0

µ=ν+1

ν=0

n−1

n−3

Qˆµ Q ˆν+2Qˆν+1Teν

≤ ∆t

µ=ν+3

ν=0

n−3

(1 + c ∆t)n−ν−3 Q ˆν+2Qˆν+1Teν

≤ ∆t

ν=0

exp(ctn) − 1 c

(45) Q ˆν+2Qˆν+1Teν .

max

=

![image 315](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile315.png>)

ν=0,...,n−3

Using the deﬁnition of the operators Qˆµ we have:

Qˆν+2Qˆν+1 = D2 + ∆t Fyν+2 (RD + A)D + Fyν+1D(RD + A) + O(∆t2)

so that Qˆν+2Qˆν+1Teν becomes

D2 + ∆t Fyν+2 (RD + A)D + Fyν+1D(RD + A) + O(∆t2) Teν = D2Teν + ∆tFyν+2 (RD + A)DTeν + Fyν+1D(RD + A)Teν + O(∆t2)Teν

= ∆tpD2τνp+1+1 + ∆tp+1D2 τνp+2+1 + Fyν+1Rτνp+1+1

+ ∆tp+1Fyν+2 (RD + A)Dτνp+1+1 + ∆tp+1Fyν+1D(RD + A) τνp+1+1 + O(∆tp+2)

= ∆tp D + ∆tFyν+2 (RD + A) + ∆tFyν+1DR Dτνp+1+1

+ ∆tp+1D2 τνp+2+1 + Fyν+1Rτνp+1+1 + ∆tp+1Fyν+1DAτνp+1+1 + O(∆tp+2)

= ∆tp D + ∆tFyν+2 (RD + A) + ∆tFyν+1DR Dτνp+1+1

+ ∆tp+1 Fyν+1D2R + Fyν+1DA τνp+1+1 + ∆tp+1D2τνp+2+1 + O(∆tp+2).

Using the fact that in our case D2 = D and that Fyν+1 = Fyν + O(∆t) we obtain

Qˆν+2Qˆν+1Teν = ∆tp D + ∆tFyν+2 (RD + A) + ∆tFyν+1DR Dτνp+1+1

+ ∆tp+1Fyν+1D(R + A) τνp+1+1 + ∆tp+1Dτνp+2+1 + O(∆tp+2). The ﬁrst term and third terms disappear because of (24a) and (24b)

Dτp+1 = 0 and Dτp+2 = 0. The second term is eliminated by (24c)

D(R + A) τp+1 = 0. So that

Qˆν+2Qˆν+1Teν = O(∆tp+2) = O(∆t2)O( Teν ). Putting this all back together we see that

En = ∆tTen−1 + O(∆t2)O( Ten−2 ) + O(∆t2)O( Ten ).

Appendix B. From scalar to vector notation. In Section 3 we developed the theory for EIS methods with post-processing. In that section we used, for simplicity, scalar notation. In this appendix we show in detail how the vector case is similarly developed. For ease of explanation, we consider the equation

u(t) ω(t) t

=

- f(u(t),ω(t))
- g(u(t),ω(t))


.

This is only a vector of two components, but it will be clear from this explanation why the theory developed for the scalar case is suﬃcient for vectors of any number of components.

The method still has a similar form to (5)

(46) V n+1 = D ⊗ V n + ∆tA ⊗ F(V n) + ∆tR ⊗ F(V n+1), but here V n is a vector of length 2s that contains the numerical solutions at times (tn + cj∆t) for j = 1,...,s:

V n = (v(tn + c1∆t)),...,v(tn + cs∆t),w(tn + c1∆t)),...,w(tn + cs∆t))T ,

which are approximations to the exact solutions

Un = (u(tn + c1∆t)),...,u(tn + cs∆t),ω(tn + c1∆t)),...,ω(tn + cs∆t))T . Correspondingly, we deﬁne





- f(v(tn + c1∆t),w(tn + c1∆t))

- f(v(tn + c2∆t),w(tn + c2∆t))

.

- f(v(tn + cs∆t),w(tn + cs∆t))
- g(v(tn + c1∆t),w(tn + c1∆t))


- g(v(tn + c2∆t),w(tn + c2∆t))


.

- g(v(tn + cs∆t),w(tn + cs∆t))


F(Un) =

.

 

 

We see that the vectors Un and V n are simply concatenations of the two solution vectors, and the vector function F contains two diﬀerent functions, each operating on the two diﬀerent solution vectors.

We use the Kronecker product ⊗ notation to mean that the s × s matrices which operate separately on the ﬁrst set of s elements and on the second set of s elements. Thus, the local truncation error and approximation errors are now deﬁned exactly as in (10) but the Taylor expansions give us

 

 

ju dtj

∞ j=0 τj∆tj d

∞

![image 316](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile316.png>)

τnj ∆tj =

∆t LTEn = τn =

t=tn

jω dtj t=tn

∞ j=0 τj∆tj d

![image 317](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile317.png>)

j=0

The observation in Lemma 2 can be re-cast in this vector form as follows: given smooth enough functions f and g,





- f(u(tn + c1∆t) + e(tn + c1∆t),ω(tn + c1∆t) + ǫ(tn + c1∆t))

- f(u(tn + c2∆t) + e(tn + c2∆t),w(tn + c2∆t) + ǫ(tn + c2∆t))

.

- f(u(tn + cs∆t) + e(tn + cs∆t),ω(tn + cs∆t) + ǫ(tn + cs∆t))
- g(u(tn + c1∆t) + e(tn + c1∆t),ω(tn + c1∆t) + ǫ(tn + c1∆t))


- g(u(tn + c2∆t) + e(tn + c2∆t),ω(tn + c2∆t) + ǫ(tn + c2∆t))


.

- g(u(tn + cs∆t) + e(tn + cs∆t),ω(tn + cs∆t) + ǫ(tn + cs∆t))


F(Un + En) =

 

 

can be Taylor expanded term by term, so that the ﬁrst s terms are (F(Un + En))j = f(u(tn + cj∆t) + e(tn + cj∆t),ω(tn + cj∆t) + ǫ(tn + cj∆t))

= f(u(tn + cj∆t),w(tn + cj∆t))

+ e(tn + cj∆t)fu(u(tn + cj∆t),ω(tn + cj∆t))

+ ǫ(tn + cj∆t)fω(u(tn + cj∆t),ω(tn + cj∆t)) + O( en 2, ǫn 2, enǫn ).

fωn + C˜∆tǫn+c

+ O(∆tp+3). and similarly the next s terms are

+ ǫn+c

fun + C∆ten+c

+ en+c

= fn+c

j

j

j

j

j

(F(Un + En))j = gn+c

j

gun + Cˆ∆ten+c

+ en+c

j

j

+ ǫn+c

gωn + C∆tǫn+c

![image 318](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile318.png>)

j

j

+ O(∆tp+3).

The main occurrence of the derivative term Fy is in the second step of the proof. We can look at the ﬁrst half of the vector, denoting it V[1:k+1s] :

V[1:k+1s] = DV[1:k s] + ∆tAF(V k)[1:s] + ∆tRF(V k+1)[1:s]

= D Uk + Ek [1:s] + ∆tAF Uk + Ek [1:s] + ∆tRF Uk+1 + Ek+1 [1:s]

= DU[1:k s] + DE[1:k s] + ∆tAF(Uk)[1:s] + ∆tRF(Uk+1)[1:s]

+ ∆t fukAE[1:k s] + fωkAE[ks+1:2s]) + ∆t2A CE[1:k s] + CE˜ [ks+1:2s]

+ ∆t fuk+1RE[1:k+1s] + fωk+1RE[ks+1:2s]) + ∆t2R CE[1:k+1s] + CE˜ [ks+1+1:2s] + O(∆tp+3)

We can write a similar formula (but using g) for the second half of the vector. Despite the additional terms, this is similar to the proof in Section 3, because the additional terms are of similar form. The top half and bottom half of the error vectors Ek a nd Ek+1 each contain the vectors τp+1 and τp+2, and the error inhibiting conditions act on these parts. Thus the proof goes through seamlessly.

Acknowledgment. This publication is based on work supported by AFOSR grant FA9550-18-1-0383. ONR-DURIP Grant N00014-18-1-2255. A part of this research is sponsored by the Oﬃce of Advanced Scientiﬁc Computing Research; US Department of Energy, and was performed at the Oak Ridge National Laboratory, which is managed by UT-Battelle, LLC under Contract no. De-AC05-00OR22725. This manuscript has been authored by UT-Battelle, LLC, under contract DE-AC0500OR22725 with the US Department of Energy. The United States Government retains and the publisher, by accepting the article for publication, acknowledges that the United States Government retains a non-exclusive, paid-up, irrevocable, worldwide license to publish or reproduce the published form of this manuscript, or allow others to do so, for United States Government purposes.

REFERENCES

- [1] M. B. Allen and E. L. Isaacson, Numerical analysis for applied science, John Wiley & Sons, 1998.
- [2] C. Bresten, S. Gottlieb, Z. Grant, D. Higgs, D.I. Ketcheson, and A. Nemeth, Explicit strong stability preserving multistep Runge-Kutta methods, Mathematics of Computation 86 (2017) 747–769.
- [3] J. C. Butcher, Diagonally-implicit multi-stage integration method, Applied Numerical Mathematics 11 (1993), 347–363.
- [4] J. C. Butcher, Numerical methods for ordinary diﬀerential equations, John Wiley & Sons, 2008.
- [5] A Ditkowski, High order ﬁnite diﬀerence schemes for the heat equation whose convergence rates are higher than their truncation errors, Spectral and High Order Methods for Partial Diﬀerential Equations ICOSAHOM 2014, Springer, 2015, pp. 167–178.
- [6] A. Ditkowski and S. Gottlieb, Error Inhibiting Block One-step Schemes for Ordinary Diﬀerential Equations, Journal of Scientiﬁc Computing 73(2) (2017) 691–711.
- [7] A. Ditkowski Error inhibiting schemes for diﬀerential equations, lecture given at ICERM on August 2018, https://icerm.brown.edu/video archive/?play=1669.

![image 319](<2019-ditkowski-explicit-implicit-error-inhibiting_images/imageFile319.png>)

- [8] S. Gottlieb, Z.J. Grant, A. Ditkowski, Explicit and Implicit EIS methods with post-processing,

(2019), GitHub repository, https://github.com/EISmethods/EISpostprocessing.

- [9] B. Gustafsson, H.-O. Kreiss, and J. Oliger, Time dependent problems and diﬀerence methods, vol. 24, John Wiley & Sons, 1995.
- [10] E. Hairer, G. Wanner, and S. P. Norsett, Solving Ordinary Diﬀerential Equations I: Nonstiﬀ Problems, Springer Series in Computational Mathematics, Springer-Verlag Berlin Heidelberg (1993).


- [11] J. S. Hesthaven, S. Gottlieb, D. Gottlieb, Spectral Methods for Time Dependent Problems. Cambridge Monographs on Applied and Computational Mathematics (No. 21) , Cambridge University Press (2006).
- [12] E. Isaacson and H. Keller, Analysis of numerical methods, Dover Publications, Inc, 1994.
- [13] Z. Jackiewicz, General linear methods for ordinary diﬀerential equations, John Wiley & Sons, 2009.
- [14] G.Yu. Kulikov, On quasi-consistent integration by Nordsieck methods, Journal of Computational and Applied Mathematics 225 (2009) 268–287.
- [15] G. Yu. Kulikov and R. Weiner, Variable-Stepsize Interpolating Explicit Parallel Peer Methods with Inherent Global Error Control, SIAM Journal on Scientiﬁc Computing, 32(4) (2010) 1695–1723.
- [16] G.Yu. Kulikov and R. Weiner, Doubly quasi-consistent ﬁxed-stepsize numerical integration of stiﬀ ordinary diﬀerential equations with implicit two-step peer methods, Journal of Computational and Applied Mathematics, 340 (2018) 256–275.
- [17] P. D. Lax and R. D. Richtmyer, Survey of the stability of linear ﬁnite diﬀerence equations, Communications on pure and applied mathematics 9 (1956), no. 2, 267–293.
- [18] A. Quarteroni, R. Sacco, and F. Saleri, Numerical mathematics, vol. 37, Springer Science & Business Media, 2010.
- [19] R.D. Skeel, Analysis of ﬁxed-stepsize methods, SIAM Journal on Numerical Analysis 13 (1976) 664–685.
- [20] G. Sewell, The numerical solution of ordinary and partial diﬀerential equations, World Scientiﬁc, 2015.
- [21] B. Soleimani, R. Weiner A class of implicit peer methods for stiﬀ systems, Journal of Computational and Applied Mathematics 316 (2017) 358–368
- [22] E. Suli and D.F. Mayers, An Introduction to Numerical Analysis, Cambridge University Press, Cambridge, 2003.
- [23] R. Weiner, G.Yu. Kulikov, and H. Podhaiskya, Variable-stepsize doubly quasi-consistent parallel explicit peer methods with global error control, Applied Numerical Mathematics 62 (2012) 1591–1603.
- [24] R. Weiner, B. A. Schmitt, H.Podhaiskya, and S. Jebensc, Superconvergent explicit two-step peer methods, Journal of Computational and Applied Mathematics 223 (2009) 753–764.


