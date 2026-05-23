arXiv:1701.08568v1[math.NA]30Jan2017

Error Inhibiting Block One-Step Schemes for Ordinary Diﬀerential Equations

A. Ditkowski

School of Mathematical Sciences, Tel Aviv University, Tel Aviv 69978, Israel

# S. Gottlieb

Department of Mathematics, University of Massachusetts, Dartmouth, 285 Old Westport Road, North Dartmouth, MA 02747

![image 1](<2017-ditkowski-error-inhibiting-block-one-step_images/imageFile1.png>)

Abstract

The commonly used one step methods and linear multi-step methods all have a global error that is of the same order as the local truncation error (as deﬁned in [6,13,1,8,15]). In fact, this is true of the entire class of general linear methods. In practice, this means that the order of the method is typically deﬁned solely by order conditions which are derived by studying the local truncation error. In this work we investigate the interplay between the local truncation error and the global error, and develop a methodology which deﬁnes the construction of explicit error inhibiting block one-step methods (alternatively written as explicit general linear methods [2]). These error inhibiting schemes are constructed so that the accumulation of the local truncation error over time is controlled, which results in a global error that is one order higher than the local truncation error. In this work, we delineate how to carefully choose the coeﬃcient matrices so that the growth of the local truncation error is inhibited. We then use this theoretical understanding to construct several methods that have higher order global error than local truncation error, and demonstrate their enhanced order of accuracy on test cases. These methods demonstrate that the error inhibiting concept is realizable. Future work will further develop new error inhibiting methods and will analyze the computational eﬃciency and linear stability properties of these methods.

Key words: ODE solvers, General linear methods, One-step methods, Global error, local truncation error, Error inhibiting schemes.

![image 2](<2017-ditkowski-error-inhibiting-block-one-step_images/imageFile2.png>)

![image 3](<2017-ditkowski-error-inhibiting-block-one-step_images/imageFile3.png>)

Email addresses: adid@post.tau.ac.il (A. Ditkowski), sgottlieb@umassd.edu (S. Gottlieb).

Preprint submitted to Journal of Scientiﬁc Computing 5 November 2018

- 1 Introduction


When solving an ordinary diﬀerential equation (ODE) of the form

ut = F(t, u) , t ≥ 0 (1) u(t = 0) = u0

One can evolve the solution forward in time using the ﬁrst order forward Euler method

vn+1 = vn + ∆tF(tn, vn) . To obtain a more accurate solution, one can use methods with multiple steps:

vn+1 =

s

aj vn+1−j + ∆t

j=1

s

bjF(tn+1−j, vn+1−j), (2)

j=0

known as linear multistep methods [3]. Alternatively, one can use multiple stages, such as Runge–Kutta methods [3]:

m

yi = F(vn +

j=1

vn+1 = vn + ∆t

aijy(j), tn + ∆t

m

bjyj.

j=1

m

aij) for j = 1, ..., m

j=1

The class of general linear methods described in [2,9] combines the use of multiple steps and stages, constructing methods of the form:

s

U˜ijvn + ∆t

yi =

j=1

m

s

V˜ijvni + ∆t

vni+1 =

j=1

j=1

m

A˜ijf(yj)

j=1

B˜ijf(yj) . (3)

The inclusion of multiple derivatives, such as Taylor series methods [3],

vn+1 = vn + ∆tF(tn, vn) +

∆t2 2

F′(tn, vn) +

![image 4](<2017-ditkowski-error-inhibiting-block-one-step_images/imageFile4.png>)

∆t3 3!

F′′(vn),

![image 5](<2017-ditkowski-error-inhibiting-block-one-step_images/imageFile5.png>)

is another possibility, and multiple stages and derivatives have also been developed and used successfully [17], [18], [11], [10], [4]. For time-dependent problems the global error, which is the diﬀerence between the numerical and exact solution at any given time tn = n∆t:

En = vn − u(tn),

depends on the local truncation error which, roughly speaking, is the accuracy over one time step. In our case we deﬁne the local truncation error as the error

of the method over one time-step, normalized by ∆t. For example, the local truncation error for Euler’s method is (following [6,13,1,8,15])

u(tn+1) − u(tn) − ∆tF(tn, u(tn)) ∆t

τ =

≈ O(∆t).

![image 6](<2017-ditkowski-error-inhibiting-block-one-step_images/imageFile6.png>)

(To avoid confusion it is important to note that sometimes the truncation error is deﬁned a little diﬀerently than we deﬁne it above and is not normalized by ∆t).

A well known theoretical result, known as the Lax-Richtmeyer equivalence theorem (see e.g. [12], [6], [13]) states that if the numerical scheme is stable then the global error is at least of the same order as the local truncation error. In all the schemes for numerically solving ordinary diﬀerential equations (ODEs) that we are familiar with from the literature, the global errors are indeed of the same order as their local truncation errors1 . This is common to other ﬁelds in numerical mathematics, such as for ﬁnite diﬀerence schemes for partial diﬀerential equations (PDEs), see e.g. [6,13]. It was recently demonstrated, however, that ﬁnite diﬀerence schemes for PDEs can be constructed such that their convergence rates, or the order of their global errors, are higher than the order of the truncation errors [5]. In this work we adopt and adapt the ideas presented in [5] to show that it is possible to construct numerical methods for ODEs where the the global error is one order higher than the local truncation error. As we discuss below, these schemes achieve this higher order by inhibiting the lowest order term in the local error from accumulating over time, and so we name them Error Inhibiting Schemes.

Following an idea in [14], an interesting paper by Shampine and Watt in 1969 [16] describes a class of implicit one-step methods that obtain a block of s new step values at each step. These methods take s initial step values and generate the next s step values, and so on, all in one step. These methods are in fact explicit block one-step methods, and can be written as general linear methods of the form (3) above. Inspired by this form, we construct explicit block onestep methods which are in the form (3), but where the matrix U˜ is an identity matrix, and the matrix A˜ is all zeros; these are known as Type 3 methods in [2]. The major feature of our methods is that in addition to satisfying the appropriate order conditions listed in [2], they have a special structure that mitigates the accumulation of the truncation error, so we obtain a global error that is one order higher than predicted by the order conditions in [2], which describe the local truncation error.

- In Section 2 we motivate our approach by describing how typical multistep methods can be written and analyzed as block one-step methods: these methods obtain a block of s new step values at each step. We show how this form allows us to precisely describe the growth of the error over the time-evolution.


![image 7](<2017-ditkowski-error-inhibiting-block-one-step_images/imageFile7.png>)

- 1 In the case where the truncation error is deﬁned without the ∆t normalization the global error is one order lower than the truncation error.


- In Section 3 we then exploit this understanding to develop explicit error inhibiting block one-step methods that produce higher order global errors than possible for typical multistep methods. In Section 4 we present some methods developed according to the theory in Section 3 and we test these methods on several numerical examples to demonstrate that the order of convergence is indeed one order higher than the local truncation error. We also show that, in contrast to our error inhibiting Type 3 method, a typical Type 3 method developed by Butcher in [2] does not satisfy the critical condition for a method to be error inhibiting and therefore produces a global error that is of the same order as the local truncation error. Finally, we present our conclusions in Section 5, and suggest that further investigation of error inhibiting methods shall include the analysis of their linear stability properties, storage implications, and computational eﬃciency.


- 2 Motivation


In this section we present the analysis of explicit multistep methods in a block one-step form for a simple linear problem. In this familiar setting we deﬁne the local truncation error, the global error, and the solution operator that connects them. We also discuss the stability of a method of this form. We limit our analysis to the linear case so that we can clearly observe the process by which the solution operator interacts with the local truncation error, and results in a global error that is of the same order as the local truncation error. Although we are dealing for the moment with standard multistep methods, this will set the stage for the construction and analysis of error inhibiting block one-step methods.

In order to illustrate the main idea we start with a linear ordinary diﬀerential equation (ODE)

ut = f(t) u , t ≥ 0 (4) u(t = 0) = u0

where f(t) < M , ∀t ≥ 0 and f(t) is analytic. An s-step explicit multistep method applied to (4) takes the form

s−1

s−1

s−1

s−1

bjf(tn+j) vn+j

aj vn+j + ∆t

bjF(tn+j, vn+j) =

aj vn+j + ∆t

vn+s =

j=0

j=0

j=0

j=0

(5) where the time domain is discretized by the sequence tn = n∆t, and vn denotes the numerical approximation of u(tn). The method (5) is deﬁned by its coeﬃcients {aj}js=0−1 and {bj}js=0−1, which are constant values. Following [6] we rewrite the method (5) in its block form. To do this, we ﬁrst

introduce the exact solution vector

Un = (u(tn+s−1), . . ., u(tn))T (6) and similarly, the numerical solution vector is

Vn = (vn+s−1, . . ., vn)T . (7) Now (5) can be written in block form so that it looks like a one step scheme

Vn+1 = QnVn (8) where





as−1 + ∆tbs−1f(tn+s−1) as−2 + ∆tbs−2f(tn+s−2) . . . a0 + ∆tb0f(tn) I

.

Qn =

...

 

 

I 0

(9) From repeated applications of equation (8) we observe that the numerical solution vector Vn at any time tn can be related to Vν for any previous time tν

Vn = S∆t (tn, tν)Vν , ν ≤ n (10)

where S∆t is the discrete solution operator. This operator can be expressed explicitly by

S∆t (tn, tν) = Qn−1 . . .Qν+1Qν , S∆t (tn, tn) = I. (11) For simplicity we can deﬁne this by

n−1

Qµ ≡ Qn−1 . . .Qν+1Qν ,

µ=ν

n−1

Qµ ≡ I. (12)

µ=n

Note that if each matrix Qµ is independent of µ (in other words, in the constant coeﬃcient case where f is independent of t), we simply have a product of matrices Q, and the discrete solution operator becomes

S∆t (tn, tν) = Qn−ν. (13)

The behavior of a method depends in large part on the accuracy of its solution operator. We begin by deﬁning the local truncation error as the error of the method over one time-step, normalized by ∆t:

- Deﬁnition 1: The local truncation error τn is given by [6,13,1,8,15] ∆tτn = Un+1 − QnUn (14)


Note that in the case of the standard multistep method, where Qn is given by the matrix (9), the truncation error has only one non-zero element:

τn = (τn, 0, . . ., 0)T . (15)

The error that we are most interested in is the diﬀerence between the exact error vector and the numerical error vector at time tn,

En = Un − Vn , (16)

known as the global error. At the initial time, we have the error E0 which is based on the starting values a method of this sort requires: the values vj, j = 0, . . ., s − 1 that are prescribed or somehow computed. Typically, v0 is the initial condition deﬁned in (1) and vj, j = 1, . . ., s − 1 are computed to suﬃcient accuracy using some other numerical scheme. Thus, the value of E0 is assumed to be as small as needed.

The evolution of the global error (16) depends on the local truncation error deﬁned by (14) and the discrete solution operator given in (8):

En+1 = QnEn + ∆tτn . (17) Unraveling this equality all the way back to E0 gives

En = S∆t (tn, 0)E0 + ∆t

or, equivalently

n−1

S∆t (tn, tν+1)τν , (18)

ν=0

En =

 

n−1

n−1

QµE0 + ∆t

ν=0

µ=0

n−1

µ=ν+1

 τν . (19)

Qµ

(This formula is obtained from the discrete version of Duhamel’s principle, see Lemma 5.1.1 in [6]).

It is clear from (18) that the behavior of the discrete solution operator S∆t(tn, tν+1) must be controlled for this error to converge. This property deﬁnes the stability of the method. Also here we use the stability deﬁnition presented in [6], namely:

- Deﬁnition 2: The scheme (8) is called stable if there are constants αs and Ks, independent of ∆t, such that for all 0 < ∆t ≤ ∆t0


S∆t (tn, tν) ≤ Kseα

s(tn−tν) (20)

If the scheme is stable, we can use (20) and (18) to bound the growth of the error:

En ≤ Ks eα

stn E0 + max

τν φ∗h(αs, tn) . (21) where

0≤ν≤n−1

 

eαs tn−1

n−1

αs αs = 0 tn αs = 0

tn 0

![image 8](<2017-ditkowski-error-inhibiting-block-one-step_images/imageFile8.png>)

eα

s(tn−ζ)dζ =

eα

s(tn−tν+1) ≈

φ∗∆t(αs, tn) = ∆t



ν=0

(22) Equation (21) means that stability implies convergence:2 if the scheme is stable than the global error is controlled by the local truncation error for any given ﬁnal time. In the formula above it is clear that the global error must have order at least as high as the local truncation error, but the possibility of having a higher order global error is left open.

The ﬁrst Dahlquist barrier [7,3] states that any explicit s step linear multistep method can be of order p no higher than s. It is the common experience that methods have global error of the same order as the local truncation error. These two together greatly limit the accuracy of the methods we can derive.

- Remark 1 In an Adams-Bashforth scheme the entry in the ﬁrst row and ﬁrst


column in the term S∆t (tn, tν) = µ n=−ν1 Qµ is equal to 1+O(∆t). Therefore the error, due to the accumulation of the contributions from the truncation errors, becomes:

n−1

(1 + O(∆t))τν (23)

en+s = ∆t

ν=0

which is approximately the average value of τν over ν = 0, .., n − 1. This suggests that we may need to look outside the family of linear multistep methods to attain a higher order global error.

The analysis in this section suggests that if the operator Qn is properly constructed, the growth of the global error described in Equation (19) may be controlled through the properties of the operator Qn and its relationship with the local truncation error τn. However, as implied by the example of the Adams-Bashforth scheme above, we need to construct methods where the operator Qn is not limited by the structure in this section. In the next section we present the construction of block one-step methods that are error inhibiting. The class of methods described by this block one-step structure is very broad: while all classical multistep methods can be written in this block form, not every such block one-step method can be written as a classical multistep method. Thus, we rely on the discussion in this section with one main change: the structure of the operator Qn.

.

![image 9](<2017-ditkowski-error-inhibiting-block-one-step_images/imageFile9.png>)

- 2 For partial diﬀerential equations this result is known as one part of the celebrated Lax-Richtmeyer equivalence theorem. See e.g. [12], [6], [13].


- 3 An Error Inhibiting Methodology


In Section 2 we rewrote explicit linear multistep methods in a block one-step form, and expressed the relationship between its local and global error. We observed that the growth of the local errors is driven by the behavior of the discrete solution operator Qn, and in particular its interaction with the local truncation error. Using this insight we show in this section that it is possible to construct such explicit block one-step methods (which are also known as Type 3 DIMSIM methods in [2]) that inhibit the growth of the truncation error so that the global error (16) gains an order of accuracy over the local truncation error (14).

We begin in Section 3.1 by describing the construction and analysis of error inhibiting block one-step schemes for the case of linear constant coeﬃcient equations. We then show that this approach yields methods that are also error inhibiting for variable coeﬃcient linear equations in Section 3.2 and nonlinear equations in Section 3.3.

- 3.1 Error inhibiting schemes for linear constant coeﬃcient equations


Given a linear ordinary diﬀerential equation with constant coeﬃcients:

ut = f · u , for t ≥ 0, (24) u(t = 0) = u0

where f ∈ . We deﬁne a vector of length s that contains the exact solution of (24) at times (tn + j∆t/s) for j = 0, . . ., s − 1

Un = u(tn+(s−1)/s), . . ., u(tn+1/s), u(tn) T , (25) and the corresponding vector of numerical approximations

Vn = vn+(s−1)/s, . . ., vn+1/s, vn T . (26)

Note that although we are assuming that the solution u at any given time is a scalar, this entire discussion easily generalizes to the case where u is a vector, with only some cumbersome notation needed. Thus without loss of generality we continue the discussion with scalar notation.

- Remark 2 The notation above emphasizes that this scheme uses s terms for generating the next s terms, unlike the explicit linear multistep methods in the section above which use s terms to generate one term. To match with the notation in Section 2 above, we can replace ∆t′ = s∆t thus deﬁning this scheme on integer grid points. We deﬁne the block one-step method for the linear constant coeﬃcient problem


(24)

Vn+1 = QVn (27) where

Q = A + ∆tBf (28) and A, B ∈ s×s. Unlike in the case of classical multistep methods, here we do not restrict the structure of the matrices A and B. Thus, any multistep method of the form (5) can be written in this form (as we saw above), but not every method of the form (28) can be written as a multistep method. In fact, this methods is a general linear method of the DIMSIM form (3) with A˜ is all zeroes, U˜ is the identity matrix, V˜ = A, and B˜ = B. This particular formulation is, as we mentioned above, called a Type 3 DIMSIM in Butcher’s 1993 paper [2].

At any time tn, we know that u(tn + ∆t) = u(tn) + O(∆t), so that for the numerical solution Vn to converge to the analytic solution Un one of the eigenvalues of Q must be equal to 1 + O(∆t), and its eigenvector must have the form:

(1 + O(∆t), . . ., 1 + O(∆t))T . (29) The structure of the eigensystem of A, which is the leading part of Q, is critical to the stability of the scheme and the dynamics of the error. Suppose A is constructed such that:

- (1) rank(A) = 1.
- (2) Its non-zero eigenvalue is equal to one and its corresponding eigenvector is (1, . . ., 1)T
- (3) A can be diagonalized.


Property (2) assures that the method produces the exact solution for the case f = 0. Now, since the term ∆tBf is only an O(∆t) perturbation to A, the matrix Q will have one eigenvalue, z1 = 1 + O(∆t) whose eigenvector has the form

ψ1 = (1 + O(∆t), . . ., 1 + O(∆t))T (30) and the rest of the eigenvalues satisfy zj = O(∆t) for j = 2, . . ., s. Since the Q = 1 + O(∆t), we can conclude that there exist constants Ks and αs such that

S∆t (tn, tν) = Qn−ν ≤ Kseα

s(tn−tν) (31)

where αs = B  |f|. Therefore, according to Deﬁnition 2, the scheme (27) is stable. By the same argument used above, we can show that the global error will have order that is no less than the order of the local truncation error.

We now turn to the task of investigating the truncation error, τn. The deﬁnition of the local truncation error in this case is still

∆tτn = Un+1 − QnUn as deﬁned in the previous section in Equation (14).

- Remark 3 Since Q = A + ∆tBf and ut = fu the local truncation error can be written as


d Un dt

∆tτn = Un+1 − AUn + ∆tB

.

![image 10](<2017-ditkowski-error-inhibiting-block-one-step_images/imageFile10.png>)

Therefore τn does not explicitly depend on f. This observation is valid for the variable coeﬃcients and the nonlinear case as well.

The deﬁnition of the error is

En = Un − Vn , as in Equation (16). The evolution of the error is still described by Equation

(19)

 

 τν ,

n−1

n−1

n−1

Qµ

QµE0 + ∆t

En =

ν=0

µ=ν+1

µ=0

which in the linear constant coeﬃcient case becomes

En = QnE0 + ∆t

n−1

Qn−ν−1τν . (32)

ν=0

The main diﬀerence between this case and the linear multistep method in Section 2 is that the structure of Q is diﬀerent, and that unlike (15), in this case all the entries in τn are typically non-zero. Equation (32) indicates that there are several sources for the error at the time tn:

- (1) The initial error E0 which is the error in the initial condition V0: This error is caused primarily by the numerical scheme used to compute the ﬁrst s − 1 elements in V0. We assume these errors can be made arbitrary small. The initial value, which is the ﬁnal element of V0, is taken from the analytic initial condition and is considered to be accurate to machine precision.
- (2) The term ∆tτn−1, which is the last term in the sum in the right hand side of (32): This term is clearly, by deﬁnition, of the size O(∆t) τn−1 .
- (3) The summation


n−2

Qn−ν−1τν, (33)

∆t

ν=0

which are all the rest of the terms in the sum in the right hand side of (18): This is the term we need to bound to control the growth of the truncation error.

The terms in the sum (33) are all comprised of the discrete solution operator Q multiplying the local truncation error. This leads us to the major observation that is the key to constructing error inhibiting methods: if the local truncation error lives in the subspace of eigenvectors that correspond

to the eigenvalues of O(∆t), then the growth of the truncation error will be inhibited, and the global error will be one order higher than the local truncation error.

Recall that Q has one dominant eigenvalue that has the form 1 + O(∆t) and all the others are O(∆t). Correspondingly, two subspaces can be deﬁned

Ψ1 = span{ψ1} and Ψc1 = span{ψ2, ..., ψs}

where ψj is the eigenvector associated with each eigenvalue zj. As ψj can be normalized, we assume that ψj = O(1). It should be noted that while Ψ1 and Ψc1 are linearly independent, they are not orthogonal subspaces. Furthermore, since the matrix A is diagonalizable by construction, its eigenvectors span s. Since τν ∈ s, it can be written as

τν = γ1ψ1 +

s

γjψj (34)

j=2

where γ1ψ1 ∈ Ψ1 and sj=2 γjψj ∈ Ψc1. Of course, the truncation error τν is determined by the entries of Q. To ensure that the local truncation error is mostly in the space Ψc1 of eigenvectors which correspond to the eigenvalues of size O(∆t), we choose the entries of Q (i.e. the entries of A and B) such that γ1 = O(∆t), which will mean that

γ1ψ1 = O(∆t) τν . (35)

Using this, we can bound product of the discrete solution operator and the truncation error,

Qτν = γ1Qψ1 +

s

γjQψj ≤ γ1Qψ1 +

j=2

s

γjQψj

j=2

s

s

γjψj ≤|z1|  γ1ψ1 + max

γjzjψj ≤ |z1|  γ1ψ1 + max

|zj|

= γ1z1ψ1 +

j=2,...s

j=2

j=2

|zj|  τν − γ1ψ1 ≤(1 + O(∆t))O(∆t) τν + O(∆t) τν = O(∆t) τν

j=2,...s

where zj are the eigenvalues of Q. Therefore we have

Qτν ≤ O(∆t) τν . (36)

Whenever the condition (36) is satisﬁed, we can show that the sum (33) above is bounded:

n−2

n−2

n−2

Qn−ν−2 Qτν

Qn−ν−1τν ≤ ∆t

Qn−ν−1τν = ∆t

∆t

ν=0

ν=0

ν=0

n−2

Q n−ν−2 O(∆t) τν

≤∆t

ν=0

n−2

(1 + c∆t)n−ν−2O(∆t)

≤∆t max

τν

ν=0,...,n−2

ν=0

n−2

ec∆t 1 + O(∆t2) n−ν−2 O(∆t)

≤∆t max

τν

ν=0,...,n−2

ν=0

n−2

ec(t

n−2−tν) (1 + O(∆t)) O(∆t)

≤∆t max

τν

ν=0,...,n−2

ν=0

≤O(∆t) max

ν=0,...,n−2

τν φ∗∆t(c, T). (37)

(Recall (22) for the deﬁnition of of φ∗∆t(c, T).) In the ﬁnal equation, T is the ﬁnal time, and the term φ∗∆t(c, T) is therefore a constant. Thus we have the bound

n−2

Qn−ν−1τν ≤ O(∆t) max

∆t

ν=0,...,n−2

ν=0

τν . (38)

Putting this all together into (32), we obtain En = O(∆t) max

ν=0,...,n−1

τν . (39)

Thus, if the coeﬃcients of A and B are chosen so that we can control the size of Qτν in (36), we can obtain a scheme that inhibits the growth of the local truncation error, so that the global error is one order more accurate than its truncation error.

- 3.2 Linear variable-coeﬃcient equations


In the previous section we showed how to construct an error inhibiting method by choosing the coeﬃcients in A and B so that the local truncation error lives (mostly) in the space that is spanned by the eigenvectors corresponding to eigenvalues that are of O(∆t). In this section we show that under the same criteria as above, these methods are also error inhibiting when applied to a variable coeﬃcient linear ordinary diﬀerential equation:

ut = f(t)u , t ≥ 0 u(t = 0) = u0 (40)

where f(t) assumed to be analytic or as smooth as needed, and bounded. In this case the scheme is given by a time-dependent evolution operator Qn which

may change each time-step:

Vn+1 = QnVn (41) where





f tn+(s−1)/s

f tn+(s−2)/s

Qn = A + ∆tB

(42)

...

 

 

f (tn)

and the matrices A and B are the same as described above for the constant coeﬃcient scheme.

Since f(t) is an analytic function, Qn can be written as





((s − 1)/s)

((s − 2)/s)

+O(∆t3)

Qn = A+∆tBf(tn)+∆t2Bf′(tn)

...

 

 

0

(43) We can also say then that

Qn = A + ∆tBf(tn) + O(∆t2)Bf′(tn) = Q˜n + O(∆t2). (44)

Each Q˜n has the same structure as Q in the constant coeﬃcient case. In particular

Q ˜n = (1 + O(∆t)) ≤ 1 + c∆t, ∀n . (45) Furthermore, as was pointed out in Remark 3, since the local truncation error τn does not depend explicitly on f(t) at any time tn, we can write τn as a linear combination of the eigenvectors of A that correspond to the zero eigenvalues. Thus, τn lives (mostly) in the space that is spanned by the eigenvectors of any matrix Q˜n corresponding to eigenvalues that are of O(∆t). We can then follow the same analysis as in (35)–(36), to obtain the bound

Q ˜n+1τn = O(∆t) τn , ∀n . (46) In this case, Equation (18) takes the modiﬁed form (for n ≥ 1)

 

n−1

n−1

QµE0 + ∆t

En =

ν=0

µ=0

n−2

n−1

QµE0 + ∆t

=

ν=0

µ=0

 τν

n−1

Qµ

µ=ν+1

n−1

Q ˜µ + O(∆t2) τν + ∆tτn−1

µ=ν+1

The ﬁrst term is negligible because we assume that the initial error can be made arbitrarily small, and the ﬁnal term is clearly of order ∆tτn−1. Using (45), (46) and the same analysis as in (35)–(38) we have

 

n−2

n−1

∆t

ν=0

µ=ν+1

 τν = ∆t

n−2

Q˜µ

ν=0

n−2

≤∆t

ν=0

  Q ˜ν+1τν

 

n−1

Q˜µ

µ=ν+2

n−1

Q˜µ Q ˜ν+1τν

µ=ν+2

n−2

O (1 + O(∆t))n−ν−2 O(∆t) τν ≤O(∆t) max

≤∆t

ν=0

τν .

ν=0,...,n−2

Putting these all together we have

En = O(∆t) max

ν=0,...,n−1

τν . (47)

This simple proof shows that even for the variable coeﬃcient case, the schemes constructed as described above have a higher order error than would be expected from the truncation error. In the next subsection we extend this analysis to the general nonlinear case.

- 3.3 Nonlinear equations


Finally, we analyze the behavior of methods satisfying the assumptions in Section 3.1 when applied to nonlinear problems. Consider the nonlinear equation

ut = f(u(t), t) , t ≥ 0 u(t = 0) = u0 (48)

where f(u, t) assumed to be analytic in u and t. We now use the scheme





f vn+(s−1)/s, tn+(s−1)/s

Vn+1 = AVn + ∆tB

(49)

. f (vn, tn)

 

 

where the matrices A and B are as constructed above for the constant coeﬃcients problem. As deﬁned in (14), the exact solution to (48) and the truncation error are

related by





f un+(s−1)/s, tn+(s−1)/s

+ ∆tτn. (50)

Un+1 = AUn + ∆tB

. f (un, tn)

 

 

Note that by Taylor expansion f (vν, tν) = f (uν, tν) + fu (uν, tν)(vν − uν) + r(vν − uν) ,

wherefu(u, t) = ∂f(u, t)/∂u and |r(vν − uν)| ≤ c1|vν − uν|2. Subtracting (49) from (50) and assuming that En = Un − Vn ≪ 1 gives





fu un+(s−1)/s, tn+(s−1)/s

...

En+1 = AEn−∆tB

En+∆tτn+∆tR(En)

 

 

fu (un, tn)

(51)

where R(En) ≤ c1 En 2. Equation (51) means that as long as O(En2) ≪ O(τn), the equation for the error En can be analyzed in essentially the same way as for the linear variable coeﬃcient case, and the same estimates hold.

In order to evaluate the time interval in which O(En2) ≪ O(τn) we note that although the term R(En) in (51) is not a non-homogeneous term but rather a function of En, we can still use the approach used in [6, Theorem 5.1.2]) to prove stability for a perturbed solution operator. As in [6, Theorem 5.1.2]), we use the discrete version of Duhamel’s principle to obtain

 

 R(Eν)

 

 τν + ∆t

n−1

n−1

n−1

n−1

n−1

Qˆµ

Qˆµ

QˆµE0 + ∆t

En =

ν=0

µ=ν+1

ν=0

µ=ν+1

µ=0

(52) where





fu un+(s−1)/s, tn+(s−1)/s

...

Qˆn = A − ∆tB

. (53)

 

 

fu (un, tn)

Taking the norm of (52) and using the triangle inequality we obtain

En  ≤

 

n−1

n−1

QˆµE0 + ∆t

ν=0

µ=0

  τν + ∆t

n−1

n−1

Qˆµ

ν=0

µ=ν+1

 R(Eν) .

 

n−1

Qˆµ

µ=ν+1

(54)

As in the linear case we assume that the initial error, E0 is arbitrary small, so the ﬁrst term is negligible. If Qˆν+1 is constructed such that Q ˆν+1τν = ∆tO(τν) then using the same analysis as in variable coeﬃcient case the second term in (54) is less or equal to ∆tc0φ∗h(c, tn) maxν=0,...,n−1 τν . As to the third term, the same arguments can be used to show that it is bounded by

 

 R(Eν) ≤ c1φ∗h(c, tn) En 2 , (55)

n−1

n−1

Qˆµ

∆t

ν=0

µ=ν+1

so that (54) (with the substitution of (55) for the ﬁnal term) can be re-arranged to obtain

En (1 − c1φ∗h(c, tn) En )≤∆tc0φ∗h(c, tn) max

ν=0,...,n−1

τν . (56)

If c1φ∗h(c, tn) En < 1/2, we obtain En  ≤2∆tc0φ∗h(c, tn) max

τν (57) This estimate holds as long as

ν=0,...,n−1

c1φ∗h(c, tn) En ≤ 2∆tc0c1 (φ∗h(c, tn))2 max

ν=0,...,n−1

τν ≤

- 1

![image 11](<2017-ditkowski-error-inhibiting-block-one-step_images/imageFile11.png>)

- 2


, (58)

which is satisﬁed for all times tn such that ∆tφ∗h(c, tn) = O(1). Therefore

τν . for the nonlinear case as well.

En = O(∆t) max

ν=0,...,n−1

- 4 Some Error Inhibiting Explicit Schemes


In the previous section we deﬁne suﬃcient conditions for methods of the form

Vn+1 = QVn (59) where

Q = A + ∆tBf to be error inhibiting. These are C1. rank(A) = 1. C2. Its non-zero eigenvalue is equal to 1 and its corresponding eigenvector is

(1, . . ., 1)T . C3. A can be diagonalized.

C4. The matrices A and B are constructed such that when the local truncation error is multiplied by the discrete solution operator we have the bound:

Qτν ≤ O(∆t) τν .

This is accomplished by requiring the local truncation error to live in the space of the eigenvectors of A that correspond to the zero eigenvalues.

In this section we present several schemes which were constructed using the approach presented in the previous section. In Section 4.1, we present a block one-step method that evolves two steps (vn and vn+1

) to obtain the next two steps (vn+1 and vn+3

![image 12](<2017-ditkowski-error-inhibiting-block-one-step_images/imageFile12.png>)

2

). This method has truncation error (14) that is second order, while its global order (16) is third order. We demonstrate that the expected convergence rate is attained on several sample nonlinear problems. In this section we also show that a typical Type 3 DIMSIM method (derived in [2]) that satisﬁes the ﬁrst three conditions above but not the fourth, has truncation error of order two, and its global error is of the same order. This demonstrates the importance of condition C4.

![image 13](<2017-ditkowski-error-inhibiting-block-one-step_images/imageFile13.png>)

2

Next, in Section 4.2 we present a block one-step method that evolves three steps vn, vn+1

. This method has truncation error (14) that is third order, while its global order (16) is fourth order,

andvn+2

to obtain vn+1, vn+4

and vn+5

![image 14](<2017-ditkowski-error-inhibiting-block-one-step_images/imageFile14.png>)

![image 15](<2017-ditkowski-error-inhibiting-block-one-step_images/imageFile15.png>)

![image 16](<2017-ditkowski-error-inhibiting-block-one-step_images/imageFile16.png>)

![image 17](<2017-ditkowski-error-inhibiting-block-one-step_images/imageFile17.png>)

3

3

3

3

- as we demonstrate on several sample problems. Finally, to show that the methods in each class are not unique, we present two other methods of this type and show that their global error is of one order higher than the local truncation error on a sample nonlinear system.

4.1 A third order error inhibiting method with s = 2.

In this subsection we deﬁne an explicit block one-step with s = 2 that satisﬁes the conditions C1 – C4 above. This method takes the values of the solution

- at the times tn and tn+1


and obtains the solution at the time-level tn+1 and tn+3

![image 18](<2017-ditkowski-error-inhibiting-block-one-step_images/imageFile18.png>)

2

. The exact solution vector for this problem is

![image 19](<2017-ditkowski-error-inhibiting-block-one-step_images/imageFile19.png>)

2

Un = u(tn+1/2), u(tn) T and, similarly, the corresponding vector of numerical approximations is

Vn = vn+1/2, vn T . The scheme is given by:

Vn+1 =

  Vn +

  

−1 7 −1 7

∆t 24

1 6

![image 20](<2017-ditkowski-error-inhibiting-block-one-step_images/imageFile20.png>)

![image 21](<2017-ditkowski-error-inhibiting-block-one-step_images/imageFile21.png>)

  

  

55 −17 25 1

  

f vn+1/2, tn+1/2 f (vn, tn)

   , (60)

and has truncation error

τn =

  

  

d3 dt3

7 1

23 576

u(tn) ∆t2 + O(∆t3) . (61)

![image 22](<2017-ditkowski-error-inhibiting-block-one-step_images/imageFile22.png>)

![image 23](<2017-ditkowski-error-inhibiting-block-one-step_images/imageFile23.png>)

The matrix A can be diagonalized as follows:

  

  

  

  

   . (62)

  

   =

  

−1 7 1 −1

1

−1 7 −1 7

1 7 1 1

1 6

1 6

A =

![image 24](<2017-ditkowski-error-inhibiting-block-one-step_images/imageFile24.png>)

![image 25](<2017-ditkowski-error-inhibiting-block-one-step_images/imageFile25.png>)

0

Observe that the leading order of the truncation error (61) is in the space of the second eigenvector of A, the one that corresponds to the zero eigenvalue. Also, as was pointed out in Remark 3, τn depends only on this eigenvector of A and a multiple that is not directly dependent on f but only on the third derivative of the solution u. This underscores the analysis in Sections 3.2 and

- 3.3 that demonstrates that the error inhibiting property carries through for variable coeﬃcient and nonlinear problems. To study the behavior of the global error we use the fact shown in Section 3.3 that even for a nonlinear equation it is suﬃcient to analyze the matrix


Q = A + ∆tB f (63) where f is a constant. In this case:

  

  

2∆t2 8 + O(∆t3) 7 + 36f∆t + 228f2∆t2 + O(∆t3) 1 1

1 + f∆2 t + f

1 6

![image 26](<2017-ditkowski-error-inhibiting-block-one-step_images/imageFile26.png>)

![image 27](<2017-ditkowski-error-inhibiting-block-one-step_images/imageFile27.png>)

Q=

![image 28](<2017-ditkowski-error-inhibiting-block-one-step_images/imageFile28.png>)

  

  

2∆t2

3∆t3

1 + f∆t + f

2 + f

6 + O(∆t4)

![image 29](<2017-ditkowski-error-inhibiting-block-one-step_images/imageFile29.png>)

![image 30](<2017-ditkowski-error-inhibiting-block-one-step_images/imageFile30.png>)

2∆t2

3∆t3

4f∆t

3 − f

2 − f

6 + O(∆t4)

![image 31](<2017-ditkowski-error-inhibiting-block-one-step_images/imageFile31.png>)

![image 32](<2017-ditkowski-error-inhibiting-block-one-step_images/imageFile32.png>)

![image 33](<2017-ditkowski-error-inhibiting-block-one-step_images/imageFile33.png>)

  

  

2∆t2

2∆t2

−1 + 7112f∆t + 107f

36 + O(∆t3) 7 − 6512fk − 209f

36 + O(∆t3) 1 − 7112f∆t − 107f

![image 34](<2017-ditkowski-error-inhibiting-block-one-step_images/imageFile34.png>)

![image 35](<2017-ditkowski-error-inhibiting-block-one-step_images/imageFile35.png>)

![image 36](<2017-ditkowski-error-inhibiting-block-one-step_images/imageFile36.png>)

![image 37](<2017-ditkowski-error-inhibiting-block-one-step_images/imageFile37.png>)

2∆t2

2∆t2

36 + O(∆t3) −1 + 6512fk + 209f

36 + O(∆t3)

![image 38](<2017-ditkowski-error-inhibiting-block-one-step_images/imageFile38.png>)

![image 39](<2017-ditkowski-error-inhibiting-block-one-step_images/imageFile39.png>)

![image 40](<2017-ditkowski-error-inhibiting-block-one-step_images/imageFile40.png>)

![image 41](<2017-ditkowski-error-inhibiting-block-one-step_images/imageFile41.png>)

(64)

Recall that, neglecting the initial error E0, we can say that the global error is

(16)

n−1

Qn−ν−1τν

En = ∆t

ν=0

Putting together equations (61) and (64) we see that each term Qτν contributes to the error in two ways:

- • The ﬁrst contribution is due to the fact that τν is almost co-linear with the second eigenvector ψ2. The order of this contribution is

|z2| ψ2τν = O(∆t) · O( ∆tτν ) = O(∆t3) where the term |z2| is the second eigenvalue which is of order O(∆t).

- • The second contribution to the error comes from the component of τν that is a multiple γ1 of the ﬁrst eigenvector ψ1,


|z1| γ1ψ1τν = O(∆t) · O( τν ) = O(∆t3) the term γ1 is of O(∆t) because τν lives mostly in the space of ψ2.

While each of the terms in ∆tQτν has order O(∆t2) · O( τν ) = O(∆t4), as the method is evolved forward, the errors accumulate over time, and sum of all contributions from all the times gives us a global error of order O(∆t) · O( τn ) = O(∆t3).

- Example 1a: To demonstrate that this method indeed performs as designed we study its behavior on a nonlinear scalar equation of the form:

ut = −u2 = f(u) , t ≥ 0 u(t = 0) = 1 . (65)

We evolve the solution of this equation to time T = 1 using the scheme (60). The initial steps are computed exactly. The plots of the errors and the truncation errors are presented in Figure 1(a). Both errors are shown for the ﬁrst component, vn+1/2 (denoted v(1) in the legend) and the second component, vn (denoted v(2) in the legend). Clearly, although the truncation error is only second order (denoted tr err v(1) and tr err v(2) in the legend), the global error is third order, as predicted by the theory.

- Example 1b: It is important that the method will perform as designed on a nonlinear system as well. To demonstrate this, we solve the the van der Pol system


- u(1)t =u(2)
- u(2)t =0.1[1 − (u(1))2]u(2) − u(1) (66)


using the same scheme (60). As this is a system, it is important that both components are examined. Thus, the vector of the numerical solution has two components for the time level tn, denoted by v(2), and two components for the time level tn+1

, denoted by v(1). In Figure 1(b) the convergence plot of the components of u(1) and u(2) are presented. Once again, we see that the convergence rate is indeed third order.

![image 42](<2017-ditkowski-error-inhibiting-block-one-step_images/imageFile42.png>)

2

Remark 4 It is important to note that not all Type 3 DIMSIM methods have the EIS property! The property that the local truncation error lives in the space spanned by the eigenvectors of A that correspond to the zero eigenvalues

10−3

10-6

10−4

10-7

10−5

10-8

||E||n

##### ||E||

10−6

10-9

10−7

10-10

|err v(1), slope: 2.95536<br><br>err v(2), slope: 2.96259<br><br><br>tr err v(1),slope: 1.93739<br><br>tr err v(2),slope: 1.94015<br><br><br>|
|---|


10-11

10−8

v(2) first component, slope=2.99511

v(2) second component, slope2.99412

v(1) first component, slope=2.96890

v(1) second component, slope=3.20035

10−9

10-12

10-3 10-2

10−2 10−1

∆ t

∆ t

(a)

(b)

- Fig. 1. Convergence plots using the scheme (60). (a) The errors and truncation errors vs. ∆t, for several values of ∆t, for the numerical solution of (65). (b) The errors vs. ∆t for each component of the solution, computed for several values of ∆t, for the numerical solution of the van der Pol equation (66).


is needed for the error inhibiting behavior to occur, and this property is not generally satisﬁed. To observe this, we study the DIMSIM scheme of types 3 presented by J. C. Butcher in [2].

Consider the scheme

  

  

  

  +

  

  

  

   =

vn+1 vn

7 −3 7 −3

9 −7 −3 −3

vn+2 vn+1

∆t 8

1 4

![image 43](<2017-ditkowski-error-inhibiting-block-one-step_images/imageFile43.png>)

![image 44](<2017-ditkowski-error-inhibiting-block-one-step_images/imageFile44.png>)

given in [2]. This scheme has truncation error

  

   (67)

f (vn+1, tn+1) f (vn, tn)

  

  

23 3

d3 dt3

1 48

u(tn) ∆t2 + O(∆t3) . (68)

τn =

![image 45](<2017-ditkowski-error-inhibiting-block-one-step_images/imageFile45.png>)

![image 46](<2017-ditkowski-error-inhibiting-block-one-step_images/imageFile46.png>)

The matrix A can be diagonalized as follows:

  

  

  

   =

   . (69)

  

  

  

7 −3 7 −3

7 −3 −7 7

1

1 3/7 1 1

1 4

1 4

A =

![image 47](<2017-ditkowski-error-inhibiting-block-one-step_images/imageFile47.png>)

![image 48](<2017-ditkowski-error-inhibiting-block-one-step_images/imageFile48.png>)

0

The truncation error τn can be written as a linear combination of the two eigenvectors of A as follows:

  

  

  

  

   −

  

d3 dt3

1 1

3/7 1

19 24

35 48

u(tn) ∆t2 + O(∆t3) . (70)

τn =

![image 49](<2017-ditkowski-error-inhibiting-block-one-step_images/imageFile49.png>)

![image 50](<2017-ditkowski-error-inhibiting-block-one-step_images/imageFile50.png>)

![image 51](<2017-ditkowski-error-inhibiting-block-one-step_images/imageFile51.png>)

Unlike the EIS scheme (60), here the ﬁrst term in this expansion is of the order of O(τn) = O(∆t2). Therefore a term of the order of ∆tO(τn) = O(∆t3) is accumulated at each time step, so that the global error is second order.

10−2

10−3

10−4

||E||n

### ||E||

10−5

|err v(1), slope: 2.00403<br><br>err v(2), slope: 2.01850<br><br><br>tr err v(1),slope: 1.92748<br><br>tr err v(2),slope: 1.94065<br><br><br>|
|---|


10−6

10−7

10−2 10−1

∆ t

(a)

10-3

||v(2) first component, slope=1.97144<br><br>v(2) second component, slope1.97803<br><br>v(1) first component, slope=2.00454<br><br>v(1) second component, slope=2.00191|
|---|
|
|---|


10-4

10-5

10-6

10-7

10-3 10-2

∆ t

(b)

- Fig. 2. Convergence plots using Butcher’s scheme (67). (a) The errors and truncation errors vs. ∆t, for several values of ∆t, for the numerical solution of (65). Note that the errors for v(1) and v(2) are virtually identical so these error lines coincide. (b) The errors vs. ∆t for each component of the solution, computed for several values of ∆t, for the numerical solution of the van der Pol equation (66). Note that for this problem as well the behavior of this method on both components is virtually identical, so the error lines for each component of the solution coincide. Both the local truncation errors and the global errors are second order: this is not an error inhibiting scheme.


We note that both this method (67) and our error inhibiting method (60) satisfy the order conditions in Theorem 3.1 of [2] only up to second order (p = 2). However, as we see in Figure 2, when the method (67) is used to simulate the solution of the problems (65) and (66) we have second order accuracy, while the error inhibiting method (60) gave third order accuracy (Figure 1).

- 4.2 A fourth order error inhibiting method with s = 3.


In this subsection we present an error inhibiting method with s = 3 that takes the values of the solution at the times tn, tn+1

and uses these three values to obtain the solution at the time-level tn+1, tn+4

, and tn+2

![image 52](<2017-ditkowski-error-inhibiting-block-one-step_images/imageFile52.png>)

![image 53](<2017-ditkowski-error-inhibiting-block-one-step_images/imageFile53.png>)

3

3

. The exact solution vector is given by

, and tn+5

![image 54](<2017-ditkowski-error-inhibiting-block-one-step_images/imageFile54.png>)

![image 55](<2017-ditkowski-error-inhibiting-block-one-step_images/imageFile55.png>)

3

3

Un = u(tn+2/3), u(tn+1/3), u(tn) T , and the corresponding vector of numerical approximations is

Vn = vn+2/3, vn+1/3, vn T . Consider the error inhibiting scheme





467 −1996 2297 467 −1996 2297 467 −1996 2297

1 768

Vn+1 =

Vn +

![image 56](<2017-ditkowski-error-inhibiting-block-one-step_images/imageFile56.png>)

 

 







f vn+2/3, tn+2/3 f vn+1/3, tn+1/3

5439 −6046 3058 2399 −1694 1362 703 354 626

∆t 1152

![image 57](<2017-ditkowski-error-inhibiting-block-one-step_images/imageFile57.png>)

 

 

 

f (vn, tn)

which has a local truncation error of third order,



, (71)

 





43699 12787 2227

d4 dt4

1 373248

u(tn) ∆t3 + O(∆t4)

τn =

![image 58](<2017-ditkowski-error-inhibiting-block-one-step_images/imageFile58.png>)

![image 59](<2017-ditkowski-error-inhibiting-block-one-step_images/imageFile59.png>)

 

 





0.117078 0.0342587 0.00596654

d4 dt4

u(tn) ∆t3 + O(∆t4) . (72)

≈

![image 60](<2017-ditkowski-error-inhibiting-block-one-step_images/imageFile60.png>)

 

 

However, it can be veriﬁed that for the linear case, the product

Qnτn = O(∆tτn) = O(∆t4) .

Given the analysis in Section 3.3 above, this result will carry over to the nonlinear case, and thus this method will have a fourth order global error, despite the third order truncation error.

To demonstrate this result we revisit the two examples (65) and (66) in the previous subsection and use the scheme (71) to evolve them forward in time. The results, shown in Figure 3, are exactly as we expect: although the truncation errors (seen for the problem (65) in Figure 3(a)) are only third order, the errors are fourth order for both problems (65) and the van der Pol problem (66).

4.2.1 Other fourth order error inhibiting methods with s = 3.

The methods above are not unique, in fact other methods can be derived using this approach. In this section we present two additional error inhibiting methods with s = 3 that have local truncation error that is third order but demonstrate fourth order global error on a nonlinear system.

The ﬁrst method is

10−4

10-6

10-7

10-8

10−6

10-9

||E||n

#### ||E||

10-10

10−8

10-11

|err v(1), slope: 3.96530<br><br>err v(2), slope: 3.98577<br><br>err v(3), slope: 4.00815<br><br><br>tr err v(1),slope: 2.93687<br><br>tr err v(2),slope: 2.93971<br><br>tr err v(3),slope: 2.94414<br><br><br>|
|---|


10−10

10-12

|v(3) first component, slope=3.75686<br><br>v(3) second component, slope=3.91367<br><br>v(2) first component, slope=3.86984<br><br>v(2) second component, slope=4.74651<br><br>v(1) first component, slope=3.95006<br><br>v(1) second component, slope=4.06228|
|---|


10-13

10−12

10-14

0.005 0.01 0.02 0.05

10−3 10−2 10−1

∆ t

∆ t

(a)

(b)

- Fig. 3. Convergence plots using the scheme (71). (a) The errors and truncation errors vs. ∆t, for several values of ∆t, for the numerical solution of (65). (b) The errors vs. ∆t for each component of the solution, computed for several values of ∆t, for the numerical solution of the van der Pol equation (66). As expected, we observe fourth order accuracy for the errors, although the truncation errors are third order.


1 1020

Vn+1 =

![image 61](<2017-ditkowski-error-inhibiting-block-one-step_images/imageFile61.png>)





449 −1966 2537 449 −1966 2537 449 −1966 2537

Vn +

 

 





29123 −32576 15789 12973 −9456 6779

∆t 6120

![image 62](<2017-ditkowski-error-inhibiting-block-one-step_images/imageFile62.png>)

 

 

3963 1424 2869



f vn+2/3, tn+2/3 f vn+1/3, tn+1/3

 

f (vn, tn)



, (73)

 

and has a local truncation error of third order,





115733 33623 5573

1 991440

τn =

![image 63](<2017-ditkowski-error-inhibiting-block-one-step_images/imageFile63.png>)

 

 





0.116732 0.0339133 0.00562112

≈

 

 

The second method is

d4 dt4

u(tn) ∆t3 + O(∆t4)

![image 64](<2017-ditkowski-error-inhibiting-block-one-step_images/imageFile64.png>)

d4 dt4

u(tn) ∆t3 + O(∆t4) . (74)

![image 65](<2017-ditkowski-error-inhibiting-block-one-step_images/imageFile65.png>)

10-9

10-10

10-11

###### ||E||

10-12

v(3) first component, slope=3.87999

10-13

v(3) second component, slope=3.96044

v(2) first component, slope=3.97624

v(2) second component, slope=4.00708

v(1) first component, slope=3.99351

v(1) second component, slope=4.00387

10-14

3 4 5 6 7 8 9 10 11

∆ t ×10-3

(a)

10-8

||v(3) first component, slope=3.96358<br><br>v(3) second component, slope=4.00837<br><br>v(2) first component, slope=3.96163<br><br>v(2) second component, slope=4.00746<br><br>v(1) first component, slope=3.94122<br><br>v(1) second component, slope=4.00530|
|---|
|
|---|


10-9

###### ||E||

10-10

10-11

10-12

3 4 5 6 7 8 9 10 11

∆ t ×10-3

(b)

- Fig. 4. Convergence plots van der Pol equation (66). The plots show the errors vs. ∆t for each component of the solution, computed for several values of ∆t for (a) the scheme (73) and (b) the scheme (75). As expected, we observe fourth order accuracy for the errors, although the truncation errors computed above are third order.




Vn+1 =

 

−10196 9724 −19196 −10196 9724 −19196 −10196 9724 −19196

![image 66](<2017-ditkowski-error-inhibiting-block-one-step_images/imageFile66.png>)

![image 67](<2017-ditkowski-error-inhibiting-block-one-step_images/imageFile67.png>)

![image 68](<2017-ditkowski-error-inhibiting-block-one-step_images/imageFile68.png>)

![image 69](<2017-ditkowski-error-inhibiting-block-one-step_images/imageFile69.png>)

![image 70](<2017-ditkowski-error-inhibiting-block-one-step_images/imageFile70.png>)

![image 71](<2017-ditkowski-error-inhibiting-block-one-step_images/imageFile71.png>)

![image 72](<2017-ditkowski-error-inhibiting-block-one-step_images/imageFile72.png>)

![image 73](<2017-ditkowski-error-inhibiting-block-one-step_images/imageFile73.png>)

![image 74](<2017-ditkowski-error-inhibiting-block-one-step_images/imageFile74.png>)





Vn + ∆t

 

 



144 −43172 2312

733

![image 75](<2017-ditkowski-error-inhibiting-block-one-step_images/imageFile75.png>)

![image 76](<2017-ditkowski-error-inhibiting-block-one-step_images/imageFile76.png>)

![image 77](<2017-ditkowski-error-inhibiting-block-one-step_images/imageFile77.png>)

353

144 −2453 49

![image 78](<2017-ditkowski-error-inhibiting-block-one-step_images/imageFile78.png>)

![image 79](<2017-ditkowski-error-inhibiting-block-one-step_images/imageFile79.png>)

![image 80](<2017-ditkowski-error-inhibiting-block-one-step_images/imageFile80.png>)

 

- 47

![image 81](<2017-ditkowski-error-inhibiting-block-one-step_images/imageFile81.png>)

- 48 −7231 −367


![image 82](<2017-ditkowski-error-inhibiting-block-one-step_images/imageFile82.png>)

![image 83](<2017-ditkowski-error-inhibiting-block-one-step_images/imageFile83.png>)





f vn+2/3, tn+2/3 f vn+1/3, tn+1/3

.

 

 

f (vn, tn)

(75)

The truncation error is also third order





5303 46656

![image 84](<2017-ditkowski-error-inhibiting-block-one-step_images/imageFile84.png>)

d4 dt4

u(tn) ∆t3 + O(∆t4) (76)

1439 46656

τn =

![image 85](<2017-ditkowski-error-inhibiting-block-one-step_images/imageFile85.png>)

![image 86](<2017-ditkowski-error-inhibiting-block-one-step_images/imageFile86.png>)

 

 

119 46656

![image 87](<2017-ditkowski-error-inhibiting-block-one-step_images/imageFile87.png>)





0.113662 0.0308428 0.00255058

d4 dt4

u(tn) ∆t3 + O(∆t4)

=

![image 88](<2017-ditkowski-error-inhibiting-block-one-step_images/imageFile88.png>)

 

 

Both these methods satisfy

Qnτn = O(∆tτn) = O(∆t4)

as well. As above, this property results in an error inhibiting mechanism that produced a global error of order four. This can be seen once again in Figure

- 4, using the nonlinear problem (66) above. The results of method (73) are on the left and of (75) are on the right.


- 5 Conclusions


While it is generally assumed that the global error will be of the order of the local truncation error, in this work we presented an approach to creating methods that have a global error of higher order than predicted by the local truncation error. To accomplish this, we used the block formulation of a method Vn+1 = QnVn where the discrete solution operator Qn = A + ∆tBFn is comprised of matrices of coeﬃcients A and B, and the matrix operator Fn. We show that if A is a diagonalizable matrix of rank one, that has only one nonzero eigenvalue, z1 = 1, that corresponds to the eigenvector of all ones, then the error inhibiting property will occur if the leading part of the local truncation error error for the linear constant coeﬃcient case (Fn = F = a constant) is spanned by the eigenvectors corresponding to the zero eigenvalues of A (to the leading order). We show that a method that has these properties will have a global error that has higher order than the local error, on nonlinear problems.

After presenting the concept behind these methods we use the theoretical properties above to develop block one-step methods that are in the family of Type 3 DIMSIM methods presented in [2]. We demonstrate in numerical examples on nonlinear problems (including a nonlinear system) that these methods have global error that is one order higher than the local truncation errors. We also show that this is in contrast to another Type 3 DIMSIM method which has a matrix A that satisﬁes the ﬁrst three properties C1 – C3, but does not satisfy the error inhibiting property C4, that the local truncation error is in the space spanned by the eigenvectors of A that correspond to the zero eigenvalues, and indeed does not give us a global error that is higher than the local truncation error on nonlinear test problems.

The major development in this work is the concept of an error inhibiting method and the new approach for developing methods that are constructed to control the growth of the local truncation error. While the newly developed methods presented in this work can be used in place of currently standard methods (particularly in place of type 3 DIMSIM methods) to obtain higher order accuracy, it is not yet known how they compare to other methods in terms of other important properties. In future work we intend to the study of the computational eﬃciency and storage requirements of these methods and the analysis of their linear stability regions. We expect that this will also lead to further development of error inhibiting methods that have other favorable properties.

Acknowledgements: The authors wish to thank Professor John Butcher for a very helpful discussion, and in particular for his valuable advice on general linear methods, especially the Type 3 DIMSIM methods. The work of Sigal Gottlieb was supported by AFOSR grant FA9550-15-1-0235.

## References

- [1] Myron B. Allen and Eli L. Isaacson, Numerical analysis for applied science, John Wiley & Sons, 1998.
- [2] John C. Butcher, Diagonally-implicit multi-stage integration method, Applied Numerical Mathematics 11 (1993), 347–363.
- [3] John C Butcher, Numerical methods for ordinary diﬀerential equations, John Wiley & Sons, 2008.
- [4] Robert PK Chan and Angela YJ Tsai, On explicit two-derivative Runge–Kutta methods, Numerical Algorithms 53 (2010), no. 2-3, 171–194.
- [5] A Ditkowski, High order ﬁnite diﬀerence schemes for the heat equation whose convergence rates are higher than their truncation errors, Spectral and High Order Methods for Partial Diﬀerential Equations ICOSAHOM 2014, Springer, 2015, pp. 167–178.
- [6] Bertil Gustafsson, Heinz-Otto Kreiss, and Joseph Oliger, Time dependent problems and diﬀerence methods, vol. 24, John Wiley & Sons, 1995.
- [7] Ernst Hairer, SP N¨orsett, and Gerhard Wanner, Solving ordinary, diﬀerential equations i, nonstiﬀ problems, 2Ed. Springer-Verlag, 2000, 2000.
- [8] Eugene Isaacson and Herbert Bishop Keller, Analysis of numerical methods, Dover Publications, Inc, 1994.
- [9] Zdzislaw Jackiewicz, General linear methods for ordinary diﬀerential equations, John Wiley & Sons, 2009.
- [10] K Kastlunger and Gerhard Wanner, On turan type implicit Runge–Kutta methods, Computing 9 (1972), no. 4, 317–325.
- [11] KH Kastlunger and Gerhard Wanner, Runge–Kutta processes with multiple nodes, Computing 9 (1972), no. 1, 9–24.
- [12] Peter D Lax and Robert D Richtmyer, Survey of the stability of linear ﬁnite diﬀerence equations, Communications on pure and applied mathematics 9

(1956), no. 2, 267–293.

- [13] Alﬁo Quarteroni, Riccardo Sacco, and Fausto Saleri, Numerical mathematics, vol. 37, Springer Science & Business Media, 2010.
- [14] J Barkley Rosser, A Runge-Kutta for all seasons, SIAM Review 9 (1967), 41717452.
- [15] Granville Sewell, The numerical solution of ordinary and partial diﬀerential equations, World Scientiﬁc, 2015.
- [16] Larry F Shampine and H A Watts, Block implicit one-step methods, Math. Comp 23 (1969), 73117740.


- [17] Hisayoshi Shintani et al., On one-step methods utilizing the second derivative, Hiroshima Mathematical Journal 1 (1971), no. 2, 349–372.
- [18] , On explicit one-step methods utilizing the second derivative, Hiroshima Mathematical Journal 2 (1972), no. 2, 353–368.


![image 89](<2017-ditkowski-error-inhibiting-block-one-step_images/imageFile89.png>)

