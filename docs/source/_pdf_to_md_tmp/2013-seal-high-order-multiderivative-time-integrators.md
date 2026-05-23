|Journal of Scientiﬁc Computing manuscript No. (will be inserted by the editor)|
|---|


### High-order multiderivative time integrators for hyperbolic conservation laws

#### David C. Seal · Yaman G¨u¸cl¨u · Andrew J. Christlieb

# arXiv:1304.2817v3[math.NA]28Sep2013

Received: date / Accepted: date

Abstract Multiderivative time integrators have a long history of development for ordinary differential equations, and yet to date, only a small subset of these methods have been explored as a tool for solving partial differential equations (PDEs). This large class of time integrators include all popular (multistage) Runge-Kutta as well as single-step (multiderivative) Taylor methods. (The latter are commonly referred to as Lax-Wendroff methods when applied to PDEs.) In this work, we offer explicit multistage multiderivative time integrators for hyperbolic conservation laws. Like Lax-Wendroff methods, multiderivative integrators permit the evaluation of higher derivatives of the unknown in order to decrease the memory footprint and communication overhead. Like traditional Runge-Kutta methods, multiderivative integrators admit the addition of extra stages, which introduce extra degrees of freedom that can be used to increase the order of accuracy or modify the region of absolute stability. We describe a general framework for how these methods can be applied to two separate spatial discretizations: the discontinuous Galerkin (DG) method and the ﬁnite difference essentially non-oscillatory (FD-WENO) method. The two proposed implementations are substantially different: for DG we leverage techniques that are closely related to generalized Riemann solvers; for FD-WENO we construct higher spatial derivatives with central differences. Among multiderivative time integrators, we argue that multistage two-derivative

David C. Seal Department of Mathematics Michigan State University 619 Red Cedar Road East Lansing, MI 48824, USA Tel.: +1(517) 884-1456 Fax.: +1(517) 432-1562 E-mail: seal@math.msu.edu

Yaman G¨uc¸l¨u Department of Mathematics Michigan State University East Lansing, MI 48824, USA

Andrew J. Christlieb Department of Mathematics and Department of Electrical and Computer Engineering Michigan State University East Lansing, MI 48824, USA

methods have the greatest potential for multidimensional applications, because they only require the ﬂux function and its Jacobian, which is readily available. Numerical results indicate that multiderivative methods are indeed competitive with popular strong stability preserving time integrators.

Keywords Hyperbolic conservation laws · Multiderivative Runge-Kutta · Discontinuous Galerkin · Weighted essentially non-oscillatory · Lax-Wendroff · Taylor

#### 1 Introduction

In this work we revisit classical ordinary differential equation (ODE) solvers known as multiderivative (Obreshkoff [44]) methods. It will be shown that this large class of time integrators include all explicit Runge-Kutta and Taylor methods1 as special cases. In particular, we demonstrate how a multiderivative ODE method can be used to solve hyperbolic conservation laws. We begin by presenting the deﬁnitions and notation used throughout this work.

A conservation law is a partial differential equation (PDE) deﬁned by a ﬂux function R of the form

q,t +∇x ·R(q) = 0, q(0,x) = q0(x), x ∈ Ω ⊆ Rd, (1)

where the solution q(t,x) : R+ ×Rd → Rm is a vector of m conserved quantities. In dimension d, this initial value problem is deﬁned by m equations with prescribed initial conditions q0 : Rd → Rm. We denote the ﬂux function R : Rm → Rd ×Rm with R = [f(1), f(2),..., f(d)]T. We say (1) is hyperbolic if the matrix

∂ f(1) ∂q

∂ f(2) ∂q

∂ f(d) ∂q

n(1)

(q)+n(2)

(q)+···n(d)

(q) (2)

is diagonalizable for every n ∈ Rd satisfying n = 1 and q in the domain of interest.

Numerical methods for solving (1) require a discretization technique for space as well as a (possibly coupled) discretization technique for time. The vast majority of time stepping discretizations fall into one of two distinct categories:

#### – Method of lines formulation.

A method of lines (MOL) solver for (1) separates the spatial discretization from the time evolution. Starting with q,t = −∇x ·R(q), one deﬁnes a spatial discretization qh of the continuous variable q, which could be tracking point values (ﬁnite difference, spectral methods), cell averages (ﬁnite volume methods), or coefﬁcients of basis functions (ﬁnite element methods). This operation deﬁnes a function L (qh) = −∇x ·R(qh), that in turn deﬁnes a large ODE system of the form:

qh,t = L (qh). (3)

Once this discretization has been parsed, one may apply an appropriate ODE integrator to this problem: for hyperbolic conservation laws, explicit time-stepping methods are usually preferred.

- 1 When applied to partial differential equations, Taylor methods are commonly referred to as Lax-


Wendroff methods.

#### – Lax-Wendroff (Taylor) formulation.

The Lax-Wendroff [36] procedure is a numerical scheme that updates the solution using ﬁnitely many terms from the Taylor series of the function. Here, one ﬁrst expands q(t,x) in time about t = tn:

(t −tn)2 2!

q(t,x) = qn +(t −tn)qn,t +

qn,tt +··· , (4)

and then each time derivative is replaced with a spatial derivative via the CauchyKowalewski procedure:

q,t = −∇x ·R(q), q,tt = −∇x ·R(q)t = −∇x · R (q)q,t = ∇x · R (q)·∇x ·R(q) ,

.

(5)

Further derivatives are required for higher order variants, and of course, one still needs to choose a spatial discretization. Inserting t = tn +∆t produces a single-stage, single-step method. In addition, this is fundamentally different than the MOL discretization, because the physical and temporal variables are intimately intertwined through the choice of the spatial discretization of the right hand side of (4).

Multiderivative Runge-Kutta time integrators form the bridge that uniﬁes these two disparate families of methods by deﬁning a framework that includes each of them as special cases. We will see that the generalization presented in this work makes use of techniques used in the development of high-order method of lines formulations as well as high-order Lax-Wendroff type time discretizations.

- 1.1 High-order method of lines formulation for PDEs

The most popular high-order time integrators for hyperbolic problems fall into the method of lines category. By and large, the predominant viewpoint from the community is to develop spatial discretizations separate from time integrators. This is incredibly attractive from a software engineering perspective: one can envision developing a code that completely decouples the ODE technology from the spatial discretization. In addition, the MOL formulation invites developers to concentrate efforts on ODE integrators as a separate entity from the PDE. However, this idealization is lacking given that a numerical scheme is intended to solve a PDE, and therefore one needs to respect the choice of spatial discretization not only when selecting an ODE integrator, but also when developing one. In contrast, Taylor methods require a recognition of the particular choice of spatial discretization.

- 1.2 High-order Lax-Wendroff methods for PDEs


The Lax-Wendroff procedure is much older than either Lax or Wendroff. Indeed, a more appropriate name would be the Cauchy-Kowalewski procedure, where Cauchy and Kowalewski sought methods that could aid them in proving existence and uniqueness for solutions to PDEs. Their combined method, known as the Cauchy-Kowalewski procedure, was presented in equation (5), and is derived from Brook Taylor’s method, who invented equation (4) in the 1700’s. For a modern (mid-20th century) proof and review of the Cauchy-Kowalewski

procedure see Friedman [15] or Fusaro [16] and references therein. In 1960, Peter Lax and Burton Wendroff [36] realized the Cauchy-Kowalewski procedure could be used as a numerical method. They started with the theoretical groundwork developed by Cauchy and Kowalewski and derived a numerical scheme for solving PDEs. Therefore, this entire procedure is often cited as the Lax-Wendroff method within the numerical analysis community.

The original Lax-Wendroff method was a second-order numerical discretization of the Cauchy-Kowalewski procedure, and over the past decade, much work has been put forth to deﬁne high-order variants of this method. In 2002, Toro and Titarev started work on a series of papers that became the basis for the so-called ADER (Arbitrary DERivative) methods that deﬁne high-order versions of the Lax-Wendroff procedure [65,68,69,66,70]. During that same time period, Daru and Tenaud [10] explored high-order monotonicity preserving single-step methods, and they derived TVD ﬂux limiters to control spurious oscillations. In 2003, Jianxian Qiu and his collaborators demonstrated a high-order extension of the LaxWendroff procedure using ﬁnite difference weighted essentially non-oscillatory (WENO) methods [49]. Later on, they applied the same procedure to Hamilton-Jacobi systems as well as the shallow water equations [47,39]. Additionally, Qiu, Dumbser and Shu showed how to apply the Lax-Wendroff scheme to the discontinuous Galerkin (DG) method [48], and shortly thereafter, Dumbser and Munz followed a similar procedure for constructing DG methods to arbitrarily high orders of accuracy using generalized Riemann solvers [12]. High-order versions of a Lax-Wendroff discontinuous Galerkin method have been investigated for ideal magnetohydrodynamic equations [64], and explorations into various numerical ﬂux functions for the Lax-Wendroff DG method has also been carried out [46]. It has already been noted that high-order schemes with Lax-Wendroff type time discretizations can be implemented to carry a low-memory footprint [38].

Much of the difﬁculty when constructing high-order versions of the Lax-Wendroff scheme

comes from the necessity of deﬁning higher spatial derivatives of the solution. After producing the Jacobian of the ﬂux function, the next time derivative produces the Hessian of the ﬂux function. Further derivatives require tensors which grow vastly in size, and therefore, one of the primary concerns with a high-order Lax-Wendroff method is the burden of implementing higher derivatives, especially in higher dimensions.

- 1.3 High-order multistage multiderivative methods for PDEs


In this work, we advocate the use of multistage multiderivative integrators for solving hyperbolic conservation laws. These time integrators are the natural generalization of MOL formulations as well as pure Taylor (Lax-Wendroff) methods. The introduction of higher derivatives allows one to design compact stencils, and the introduction of degrees of freedom to Taylor methods allows one to explore closely related alternatives. We argue that the beneﬁts of exploring multiderivative time integrators include, but are not limited to the following:

- – High-order accuracy [3rd-order or higher]. Explicit multiderivative schemes can be constructed to arbitrarily high orders of accuracy. We focus on a single fourth-order method as our demonstrative example.
- – Portability. Access to the eigen-decomposition of a hyperbolic problem is a necessity. Therefore, multistage multiderivative integrators that stop at the second derivative do not require anything above and beyond anything that is already called for, and therefore, they are more portable than pure Lax-Wendroff (Taylor) methods.


- – Low-storage. Multiderivative integrators carry a small memory footprint. By design, these integrators exchange storage for extra FLOPs in order to attain high-order accuracy. This feature is a desirable trait for high performance computing given than the current trend is towards inexpensive FLOPs and expensive memory.


The primary purpose of the present work is to demonstrate how multistage multiderivative integrators can be used to solve PDEs. Given the plethora of multiderivative methods from the ODE community, we choose to select demonstrative examples that can be easily modiﬁed to accommodate all explicit multiderivative methods. In particular, most of our numerical results will focus on simulations for a particular fourth-order example that serves as a representative example of a method that falls outside the conﬁnes of the Runge-Kutta and Taylor families.

The outline of this paper is as follows: we begin in §2 with a historical review of multiderivative integrators. In §3, we describe the ﬁnite difference WENO scheme, and we demonstrate how multiderivative technology can be applied to the WENO framework. In §4, we continue by looking at multiderivative integrators for the discontinuous Galerkin method. In §5 we present numerical results for our numerous numerical test problems, and in §6 we draw up conclusions and point to future work.

#### 2 High-order explicit multiderivative ODE integrators

Multistage multiderivative integrators for PDEs require a blend of both the the method of lines (MOL) formulation as well as the Lax-Wendroff formulation of (1), and in addition, one needs to select a method for the spatial discretization. We begin our description of multistage multiderivative PDE solvers with a historical overview of these methods within the conﬁnes of ODEs. In particular, we focus on explicit multiderivative Runge-Kutta integrators, which include single-derivative methods (e.g. classical Runge-Kutta) as well as single-stage methods (e.g. Taylor) as special cases. We begin with a review of multiderivative methods in §2.1, and then continue in §2.2 by deﬁning a large class of explicit multiderivative Runge-Kutta methods. In §2.3, we present model examples of methods from this class.

- 2.1 Multiderivative methods: a review


Numerical methods using multiderivative technology have a long history dating back to at least the early 1940’s, and some of the pioneering work for explicit schemes share a common ancestry with implicit schemes. In 1963, Stroud and Stancu [63] applied the quadrature method of Tur´an [71], which generated an implicit, high-order multiderivative ODE solver. Prior to Tur´an’s work, in 1940, Obreshkoff [44] derived discrete quadrature formulae for integrating functions, and much like Tur´an did, Obreshkoff used extra derivatives of the function for his quadrature rules. When extra derivatives are included, one can obtain methods with excellent properties for the numerical integration of ODEs, including high-order accuracy involving fewer quadrature points than would otherwise be required. In 1972, Kastlunger and Wanner [31] used the theory of Butcher trees to show that Tur´an’s quadrature method could be written as an implicit multiderivative Runge-Kutta scheme. The following year, Hairer and Wanner [25] deﬁned “multistep multistage multiderivative methods”, that to date, has stood the test of time as being a broad categorical deﬁnition of

|Runge−Kutta Taylor<br><br>Multistage multiderivative<br><br>Multistep multistage multiderivative|
|---|


- Fig. 1 A simple taxonomy of ODE solvers. Multistep multistage multiderivative methods as deﬁned by Hairer and Wanner [25] are the most inclusive class presented in this diagram. Our focus is on multistage multiderivative methods that include Runge-Kutta (a.k.a. multistage) and Taylor (a.k.a. multiderivative) as special cases.


numerical methods for solving ODEs. A concise taxonomy of this large class of methods is presented in Figure 1. In particular, their deﬁnition contains all Runge-Kutta and all linear multistep methods as well as additional combinations, including so-called general linear methods (c.f. John Butcher’s extensive review papers [4,5,6] for a description of general linear methods). The textbooks of Hairer, Nørsett, and Wanner [24,23] contain excellent references.

Our current focus is on explicit versions of multiderivative Runge-Kutta schemes, which needless to say, also have a long history of development. Despite their age, these methods have seen little to no attention outside the ODE community, yet given the direction of modern computer architecture, many of these methods may see use for solving PDEs in the near future. In 1952, Rudolf Zurm¨uhl [74] investigated multiderivative Runge-Kutta integrators, and later on, Erwin Fehlberg [13,14] derived an explicit multiderivative Runge-Kutta methods. Early versions of Fehlberg’s method applied a single-derivative Runge-Kutta method to the modiﬁed variable that is constructed by subtracting out m-derivatives of the original variable. A decade later, Kastlunger and Wanner [32] extended Butcher’s method to multiderivative Runge-Kutta methods. In their work, they deﬁned the order conditions for the coefﬁcients in a multiderivative Butcher tableau, and in addition, they showed that Fehlberg’s method [13,14] can be written as a multiderivative Runge-Kutta process with m-derivatives taken at a single node. During that same decade, Shintani [56,57] worked on multiderivative Runge-Kutta methods. Also in the 1970’s, Bettis and Horn [1] revisited Fehlberg’s scheme and reformulated it as an embedded Taylor method: for their celestial mechanics problem, they describe how the necessary Taylor series coefﬁcients can be generated with little to no additional cost. A decade later and unaware of the full history of the methods, Mutsui [40] also worked on Runge-Kutta methods that leveraged extra information with extra derivatives.

The most recent work on explicit multiderivative integrators appears to focus on redeﬁning order conditions and demonstrating examples of methods from this class, much of which has been carried out independently from previous work. In 1986, Gekeler and Widmann [17] used the theory of Butcher trees to deﬁne the correct order conditions for multiderivative Runge-Kutta methods. In their work, they presented families of methods with orders ranging between four and seven. Goeken and Johnson [18,19] were unaware

of the long standing history of explicit multiderivative methods, and they derived their own versions of explicit methods that are sub-optimal. Within the past decade, Yoshida and Ono [73,45] and Chan and Tsai [8] used the theory of Butcher trees to deﬁne order conditions and presented numerous examples. The primary difference between the latter two works is the following: Chan and Tsai used multiple stages for their methods, and they restrict their attention to using two derivatives of the unknown function; Yoshida and Ono restrict their attention to two-stage methods, and they admit arbitrarily many derivatives of the unknown function to be evaluated at every quadrature point. In other very recent work, Nguyen-Ba, Boˇzi´c, Kengne and Vaillancourt [42] derived a nine-stage explicit multiderivative RungeKutta scheme that makes use of extra derivatives at a single quadrature point only, much like the schemes Fehlberg originally investigated [13,14]. In doing so, the order conditions become simpler to navigate.

For the purposes of solving hyperbolic conservation laws, we view using at most twoderivatives of the function as the most appropriate choice given the opportunity to retain portable code. Hyperbolic problems require a deﬁnition of the Jacobian of the ﬂux function, which is precisely the term required to deﬁne a two-derivative scheme. Investigations into methods using extra derivatives would make for interesting future research.

- 2.2 Multistage multiderivative methods: some deﬁnitions Consider a system of ODEs, deﬁned by


y˙ = L(y), y(0) = y0, t > 0. (6)

We use the letter L in place of f to avoid conﬂict with the ﬂux function deﬁned later on in equation (19). Without loss of generality, we assume the system is autonomous. Multiderivative methods make use of extra derivatives of (6). If we take a single time derivative of (6), we see that

y¨ = L˙ = L (y)y˙ =

∂L ∂y

L(y), (7)

where ∂∂Ly denotes the partial derivative of L with respect to y. Higher derivatives can be computed recursively. Deﬁne the mth derivative of y as y(m) :=

dmy dtm , and observe that y(m+1) = L(m)(y). Using the chain rule, we see that

∂L(m−1) ∂y

y(m+1) = L(m)(y) =

y˙ =

∂L(m−1) ∂y

L(y), m ∈ Z≥1. (8)

We note that these functions can be computed analytically for ODEs, especially given access to symbolic differentiation software. For PDEs, these higher derivatives will require the use of the Cauchy Kowalewski procedure from equation (5), together with deﬁnitions for higherorder spatial derivatives. It will be shown in §§3.2 and 4.2 that WENO and DG make use of very different techniques for deﬁning these higher time derivatives.

- Deﬁnition 1 Given a collection {a(ijm),b(im)} of real scalars, a multiderivative Runge-Kutta scheme with s-stages and r-derivatives is any update of the form


r

## ∑

yn+1 = yn +

m=1

s

## ∑

b(im)L(m−1)(y(i)), (9)

∆tm

i=1

- Table 1 Butcher tableau for a multiderivative Runge-Kutta method. Each ci,a(ijm) and b(im) are real coefﬁcients that deﬁne the method using Deﬁnition 1. For simplicity, we assume time independence, and so the ci play no factor in the discretization. In addition, we have ci = c(im), which in general, does not need to be the case.

Classical Runge-Kutta methods are special cases of this form, where r = 1, and a(ij0) = aij where the aij are the coefﬁcients for the (single-derivative) Runge-Kutta method. Explicit Taylor methods have no degrees of

freedom, nor stages.

|c1 . cs|a(111) ··· a(11s)<br><br>.<br><br>... .<br><br>a(s11) ··· a(ss1)|···<br><br>|a(11r) ··· a(1rs) ... a(sr1) ··· a(ssr)<br><br>|
|---|---|---|---|
| |b(11) ··· b(s1)<br><br>|···|b(1r) ··· b(sr)|


- Table 2 Butcher tableau for the explicit Taylor method. Here, we present the Butcher coefﬁcients for the


rth-order explicit Taylor method: yn+1 = yn + ∑rm=1 ∆tmL(m−1)(yn), where the L(m−1) describe total time derivatives of equation (6) given by equation (8). Note that there are no degrees of freedom for choosing the

b(im), because they are prescribed by b(1m) = 1/m!.

|0| | | | | | |
|---|---|---|---|---|---|---|
| |1|1/2!<br><br>|···<br><br>|1/m!|···|1/r!|


where intermediate stage values are given by

r

s

## ∑

## ∑

y(i) = yn +

∆tm

m=1

a(ijm)L(m−1)(y(j)), (10)

j=1

and the total time derivatives of L are given by equation (8). If a(ijm) = 0 whenever i ≤ j, the method is explicit, otherwise it is implicit.

We remark that both Taylor and traditional Runge-Kutta methods are special cases Deﬁnition 1: setting r = 1 produces traditional Runge-Kutta methods, and setting s = 1 produces the Taylor class of methods, with no degrees of freedom for choosing the b(im). In Table 1, we present the complete Butcher tableau for a multiderivative Runge-Kutta method, and in

- Table 2, we present the Butcher tableau for the rth-order explicit Taylor method. Our deﬁnition is an equivalent, yet distinctly different version of what can be found in


other sources (c.f. [24]). It is possible to deﬁne intermediate stages through deﬁning and saving L(m)(y(i)), but we prefer Deﬁnition 1 because of the potential for a low storage implementation, at the cost of recomputing previously observed values. For hyperbolic conservation laws, we consider methods that use at most two-derivatives to be the most portable given that users must have access to the eigen-decomposition of their problem.

- Deﬁnition 2 Given a collection {a(ij1),a(ij2),b(i1)b(i2)} of real scalars, an s-stage, two-derivative Runge-Kutta (TDRK) scheme is any update of the form


yn+1 = yn +∆t

s

## ∑

b(i1)L(y(i))+∆t2

i=1

where intermediate stage values are given by

s

## ∑

b(i2)L˙(y(i)), (11)

i=1

y(i) = yn +∆t

s

## ∑

a(ij1)L(y(j))+∆t2

j=1

s

## ∑

a(ij2)L˙(y(j)). (12)

j=1

If a(ijm) = 0 for all i ≤ j, the method is explicit.

Before presenting examples of methods from this class, we would like to draw some comparisons between the popular special cases of the multistep multistage multiderivative methods. Our aim is to discuss advantages each method has for being coupled with numerical PDE solvers, and in particular, we would like to focus on which methods have promise for working well with new computer architectures.

Traditional Runge-Kutta methods are far and wide the most popular for solving hyperbolic conservation laws, yet we see room for improvement given the current direction of computer architecture. Runge-Kutta methods are easy to implement, and therefore, they are the most portable of all multistage multiderivative methods. They are self-starting and can easily change their time step size, which is an important characteristic to have for solving hyperbolic conservation laws. In addition, when compared with their natural counterpart, the Adams family of methods (e.g. linear multistep methods), Runge-Kutta methods have stability regions that are more favorable for hyperbolic problems. For example, on a purely oscillatory problem, the maximum stable time step for classical fourth-order Runge-Kutta is given by |z| ≤

√8 ≈ 2.8, where z = λ∆t is purely imaginary. For the same cost and identical storage, one would be able to take four time steps with fourth-order Adams Bashforth. Even after rescaling, the maximum stable time step for the equivalent Adams method would be restricted to |z| 1.72. It would seem that Runge-Kutta methods are ideally suited for solving hyperbolic conservation laws. They can be derived to require low-storage [72,33,34, 43], can be designed to acquire strong stability preserving (SSP) properties [22,20,33], and are very portable, especially given that they are self starting. However, traditional RungeKutta methods are not optimal with their memory usage, and to date, even the low-storage Runge-Kutta methods require many stages, and therefore they may require considerable communication overhead when compared to pure Taylor schemes.

Taylor methods lie on the other extreme of the multistage multiderivative methods: we claim that they can be implemented to have optimally low-storage for hyperbolic problems, and can contain minimal communication overhead. However, pure Taylor methods are the least portable of the time integrators discussed here. In order to implement a high-order Taylor (e.g. Lax-Wendroff) method for solving a PDE, one needs to have access to high derivatives of the unknown, which puts them out of reach from many scientists. We recognize that this can certainly be done for very complicated problems [64], but it is difﬁcult to convince users of legacy codes to modify them in order to reach high-order accuracy. On the plus side, high-order Taylor methods contain favorable stability regions for hyperbolic conservation laws, and given that they’re single-step methods, they have nominal communication overhead. However, the only degrees of freedom allowed when choosing these methods is the spatial discretization, given that the time coefﬁcients come directly from the Taylor series.

Given that multiderivative Runge-Kutta methods are a generalization of traditional Runge-

Kutta and pure Taylor methods, it is possible to design methods from this class that can retain desirable qualities from each sub-class. In order to retain portability, we view multiderivative Runge-Kutta methods that use at most two-derivatives as optimal for hyperbolic conservation laws, especially given that most codes already have access to, or at least users would be willing to implement the Jacobian of the ﬂux function. Beyond two-derivatives, we would argue the “many”-derivative Runge-Kutta methods start to lose their portability. However, given the large size of this class, there is much room for investigation into what methods work “best” with modern architectures.

- 2.3 Multistage multiderivative methods: building blocks and examples


Our aim is to describe how to take a multiderivative method from the ODE literature and formulate a hyperbolic solver using that method. In this subsection, we describe a simple building block that can be generalized to accommodate all explicit multistage multiderivative methods.

The building block we will focus on for the remainder of this paper is given by the following:

y = yn + α∆tL(yn)+β∆t2L˙(yn) + α∗∆tL(y∗)+β∗∆t2L˙(y∗) . (13)

In this equation, y could be the full update, as in y = yn+1 from equation (11) or a stage value y = y(i) from equation (12). The key to using this equation to solve PDEs is to provide a deﬁnition for L and L˙.

We prefer introducing α and β over a(ijm) and b(im) from Deﬁnitions 1 and 2 because these letters delete unnecessary indices and the upcoming descriptions for the PDE methods will introduce further indices that would become cumbersome.

Remark 1 Extensions to multistage, ‘many’-derivative methods follow by adding extra terms to equation (13).

More stages require more terms to be added to (13). For example, a three stage, twoderivative method is entirely deﬁned after deﬁning updates of the form:

y = yn + α∆tL(yn)+β∆t2L˙(yn) + α∗∆tL(y∗)+β∗∆t2L˙(y∗)

+ α∗∗∆tL(y∗∗)+β∗∗∆t2L˙(y∗∗)

(14)

for arbitrary values of α and β. Again, the y in this equation can be a single stage value y = y(i) as in equation (12), or a full update, as in equation (11).

We point out that three-derivative, two-stage methods can be formulated with y = yn + α∆tL(yn)+β∆t2L˙(yn)+γ∆t3L¨(yn)

(15)

+ α∗∆tL(y∗)+β∗∆t2L˙(y∗)+γ∗∆t3L¨(y∗) .

Note that setting α = 1, β = 1/2 and α∗ = β∗ = 0 in equation (13) produces the secondorder Taylor method, and setting α = 1, β = 1/2, γ = 1/6 and α∗ = β∗ = γ∗ = 0 in equation (15) produces the third order Taylor method.

- 2.3.1 Multistage multiderivative methods: some examples


We now describe how equation (13) can be used to construct multiderivative methods. We assert that these methods have not necessarily been optimized for hyperbolic problems; our chief objective is to demonstrate how to implement these methods. An investigation into optimized schemes will be pursued in the future.

A third order, two-stage, two-derivative method (TDRK3) [8] is given by:

(∆t)2 2

L˙(yn),

y∗ = yn +∆tL(yn)+

- 2

- 3


1 3

yn+1 = yn +∆t

L(y∗) +

L(yn)+

∆t2 6

L˙(yn).

(16)

- Table 3 Butcher tableau for a third-order two-derivative method. Presented here are the coefﬁcients as in Table 1 for an explicit, third-order method [8]. Note that all diagonal and upper-triangular entries are zero, meaning that the scheme is explicit.


|0<br><br>1<br><br><br>|0 0 1/2 0<br><br>|0 0 1/8 0|
|---|---|---|
| |2/3 1/3<br><br>|1/6 0|


| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


- TDRK3

- TDRK4

- TDRK5


3.0

1.0

2.5

0.8

2.0

0.6

Im( z )

1.5

0.4

1.0

0.2

0.5

0.0

0.0

−3.5 −3.0 −2.5 −2.0 −1.5 −1.0 −0.5 0.0 0.5

−1.0 −0.5 0.0 0.5 1.0

Re( z ) ×10−4

Re( z )

- Fig. 2 Regions of absolute stability. Here, we plot the regions of absolute stability for three different twoderivative methods that are derived in Chan and Tsai [8]: TDRK3 (16), TDRK4 (18) and TDRK5 (17) which are in order of smallest to largest. The picture on the right is a zoomed in picture of the imaginary axis. Note that the third and fourth-order methods have regions of absolute stability identical to classical three and four stage, respectively, RK methods. Of particular importance for hyperbolic problems is the fact that each of these integrators contain part of the imaginary axis [37].


This method can be constructed by ﬁrst inserting

##### α = 1, β = 1/2, α∗ = β∗ = 0,

- into equation (13) to construct the intermediate stage, and the ﬁnal update is given by selecting


α = 1, β = 1/6, α∗ = 0 and β∗ = 1/3.

- The Butcher tableau for this method is provided in Table 3, and the region of absolute stability is plotted in Figure 2, which is identical to any three stage classical Runge-Kutta method.


A ﬁfth-order, three-stage, two-derivative method [8] is given by:

2 5

2 25

∆t2L˙(yn),

∆tL(yn)+

y∗ = yn +

1 4

L˙(yn)+

y∗∗ = yn +∆tL(yn)+∆t2 −

25 72

1 8

L˙(yn)+

yn+1 = yn +∆tL(yn)+∆t2

- 3

- 4


##### L˙(y∗) ,

1 36

L˙(y∗)+

L˙(y∗∗) .

(17)

- Table 4 Butcher tableau for a ﬁfth-order, three-stage, two-derivative method. Presented here are the coefﬁcients as in Table 1 for an explicit, ﬁfth-order method [8]. Note that all diagonal and upper-triangular entries are zero, meaning that the scheme is explicit. We remark that this scheme has not necessarily been optimized given that some entries were zeroed out by choice in order to reduce the complexity of the order conditions. However, we present this example given that it contains a favorable stability region because it contains part of the imaginary axis (c.f. Figure 2).


|0<br><br>2/5<br><br>1<br><br><br>|0 0 0<br><br>2/5 0 0<br><br>1 0 0<br>|0 0 0 2/25 0 0 −1/4 3/4 0<br><br>|
|---|---|---|
| |1 0 0<br><br>|1/8 25/72 1/36|


This method can be constructed by ﬁrst inserting α = 2/5, β = 2/25, α∗ = β∗ = 0, α∗∗ = β∗∗ = 0

- into equation (14) to produce y∗, followed by inserting α = 1, β = −1/4, α∗ = 0, β∗ = 3/4, α∗∗ = β∗∗ = 0,


into (14) to produces a third stage, y∗∗. The ﬁnal update is then given by selecting

25 72

α = 1, β = 1/8, α∗ = α∗∗ = 0, β∗ =

1 36

and β∗∗ =

##### .

- The Butcher tableau for this method is provided in Table 4, and the region of absolute stability is plotted in Figure 2.


- 2.3.2 Multistage multiderivative methods: the canonical example


The example used for the remainder of this work will now be presented. There is a unique combination for an s = 2-stage method that produces fourth-order accuracy [32,45,8]. This method, which we refer to as TDRK4, can be written as

(∆t/2)2 2

∆t 2

L˙(yn),

y∗ = yn +

Ln +

∆t2 2

1 3

L ˙(yn)+2L˙(y∗) ,

yn+1 = yn +∆tLn +

(18)

The Butcher tableau for this method is presented in Table 5, and the region of absolute stability is plotted in Figure 2. Note that the region of absolute stability is identical to any four-stage, fourth-order Runge-Kutta method.

We choose to use this method as our canonical example for three reasons. First, this example is the simplest scheme that does not fall under the Taylor or Runge-Kutta umbrella, and therefore serves as a demonstrative example of new methods that can be found from this class. Second, this method has been optimized for low storage and high-order accuracy given two stages, and two-derivatives, and thirdly, this method works well for hyperbolic problems.

Given that our goal is to describe how to implement the large class of explicit multistage multiderivative methods for solving PDEs, for simplicity of exposition, we use this method as our canonical example of a method from this class. In addition, we claim that a complete

- Table 5 Butcher tableau for the multiderivative method investigated in this work. Presented here are the coefﬁcients as in Table 1 for the explicit, fourth-order method, TDRK4 presented in equation (18). Note that all diagonal and upper-triangular entries are zero, meaning that the scheme is explicit.


|0<br>1/2<br>|0 0 1/2 0<br><br>|0 0 1/8 0|
|---|---|---|
| |1 0<br><br>|1/6 1/3|


description for this scheme will provide the necessary mechanisms for extension and investigation into integrators containing extra stages. These integrators can be constructed to be even higher order accurate and contain favorable stability regions. For example, all of the methods presented in Chan and Tsai [8] can be implemented using our description with a straight-forward extension of what follows.

Observe that the TDRK4 method in equation (18) can be constructed from of equation

(13), with the ﬁrst stage given by

α = 1/2, β = 1/8, α∗ = β∗ = 0, and the update given by

α = 1, β = 1/6, α∗ = 0 and β∗ = 1/3.

This completes our description of the multiderivative Runge-Kutta scheme, and it bears repeating that without loss of generality, we will use method (18) as our canonical example of a method from this class. Given that the focus of this work is how to implement this scheme for solving hyperbolic PDEs, we still need to describe how to discretize in space.

#### 3 The ﬁnite difference WENO method

The ﬁnite difference weighted essentially non-oscillatory (WENO) method has many variations and a long history of development. The original method was developed by Shu and Osher [61,62], and later analyzed and further developed by Shu and his collaborators [30,58, 59]. For a recent comprehensive review of the many variations of WENO schemes, see ChiWang Shu’s extensive review paper [60]. In this work, we consider the ﬁfth-order WENO-Z scheme [29,2,7], that is an improvement of the classical ﬁfth-order Jiang and Shu (WENOJS) scheme [30]. The underlying choice of the reconstruction procedure is not central to this work and our description will be generic enough to accommodate most variations of the classical WENO method. However, given that there are many options, we explain the minimal details necessary to reproduce the present work.

In §3.1 we present the classical MOL formulation for the WENO method. In §3.2 we describe the extension of multiderivative ODE integrators presented in §§2.2–2.3, to formulate the multiderivative WENO method that is the subject of this section. In §4.2 we will see that the extension of multiderivative ODE methods from §2 to the DG method requires a very different approach.

- 3.1 The ﬁnite difference WENO method: MOL formulation We begin our description with a reduction of (1) to a 1D conservation law:


q,t + f(q)x = 0, q(0,x) = q0(x), x ∈ Ω = [a,b]. (19)

Here, we follow the standard convention of naming our ﬂux function f in place of R. Moreover, (19) is hyperbolic if the Jacobian f (q) = RΛR−1 is diagonalizable with real eigenvalues for all q in the domain of interest.

The spatial discretization for a ﬁnite difference method seeks a point-wise approximation to the exact solution of (19) at a ﬁnite collection of points. We start with a uniform discretization of [a,b] using mx points:

##### ∆x = (b−a)/mx, xi = a+(i−1/2)∆x, i ∈ {1,2,...,mx}, (20)

and we seek values qi that approximate the exact solution at each grid point, qi(t) ≈ q(t,xi).

In order to write (19) in discrete ﬂux-difference form so we can have a conservative method2, we begin by deﬁning an implicit sliding function h through

1 ∆x

f (q(t,x)) =

x+∆x/2 x−∆x/2

h(t,x)dx. (21)

With this deﬁnition in place, we have the nice result that

∂ f ∂x

1 ∆x

(q(t,xi)) =

h t,xi+1/2 −h t,xi−1/2 , (22)

which is precisely what is needed to deﬁne a discrete ﬂux difference formulation of qt =−fx. The MOL formulation for the ﬁnite difference scheme deﬁnes interpolated values hi+1/2 that approximate h t,xi+1/2 to high-order accuracy,

1 ∆x

hi+1/2 −hi−1/2 =

∂ f ∂x

(q(t,xi))+O ∆xM . (23)

Moreover, an astute observation means that h need never be computed [58,60]: deﬁne cell averages of h(t,x) as

xi+1/2 xi−1/2

1 ∆x

h¯i :=

h(t,x)dx, (24)

then observe that f(qi(t)) = h¯i, and therefore point values of f can be interpreted as cell averages of h. After deﬁning an appropriate interpolating algorithm for producing high-

order interface values hi+1/2 from cell averages h¯i, the full MOL formulation is given by,

d dt

1 ∆x

qi(t) = −

hi+1/2 −hi−1/2 . (25)

This scheme is automatically conservative as it is written in ﬂux difference form. Usually one applies a high-order explicit Runge-Kutta integrator to (25), which results in what is normally called the Runge-Kutta WENO (RK-WENO) method.

2 A ﬁnite difference method is conservative if the method satisﬁes dtd (∑i qi(t)) = 0 on a periodic (or inﬁnite) domain.

- 3.1.1 The ﬁnite difference WENO method: the reconstruction procedure


A conservative reconstruction procedure requires a single value hi+1/2 for equation (25) to be deﬁned at each grid interface. In the ensuing discussion, we suppress the time dependence

of h, and assume that we have known cell averages h¯i for a function h = h(x). The ﬁfth-order WENO method uses a ﬁve point stencil shifted to the left or right of the interface:

- h+i+1/2 := WENO5+[h¯i−2,h¯i−2,h¯i−1,h¯i,h¯i+2], h−
- i+1/2 := WENO5−[h¯i−1,h¯i,h¯i+1,h¯i+2,h¯i+3].


Here, we deﬁne coefﬁcients for the function WENO5+, and note that by symmetry, the reconstruction procedure weighted in the other direction can be observed by ﬂipping the stencil:

WENO5−[h¯i−1,h¯i,...h¯i+3] := WENO5+[h¯i+3,h¯i+2,...h¯i−1]. (26)

Three sub-stencils S0 = {h¯i−2,h¯i−1,h¯i}, S1 = {h¯i−1,h¯i,h¯i+1}, and S2 = {h¯i,h¯i+1,h¯i+2} uniquely deﬁne three quadratic polynomials pj(x) that have the same cell averages for each element in their stencil. Each polynomial deﬁnes a competing value for h(xi+1/2) with

h(i+j)1/2 = pj(xi+1/2):

1 3

##### h(i+0)1/2 =

1 6

##### h(i+1)1/2 = −

1 3

##### h(i+2)1/2 =

h¯i−2 −

h¯i−1 +

h¯i +

7 6

h¯i−1 +

- 5

- 6


h¯i +

- 5

- 6


h¯i+1 −

11 6

h¯i, (27a)

1 3

h¯i+1, (27b)

1 6

h¯i+2. (27c)

The linear weights γj = {1/10, 3/5, 3/10} are deﬁned as the unique linear combination of equations (27a)-(27c) that yields a ﬁfth-order accurate point value for h(xi+1/2):

hi+1/2 = γ0h(i+0)1/2 +γ1h(i+1)1/2 +γ2h(i+2)1/2. (28)

The WENO procedure replaces the linear weights γj with nonlinear weights ωj that are necessary in regions with strong shocks. The Jiang and Shu smoothness indicators βj place a quantitative measure on the smoothness of each stencil based on a Sobolev norm:

- k

∑

- l=1


∆x2l−1

βj :=

xi+1/2 xi−1/2

which for our ﬁfth order method, are given by

dl dxl

pj(x)

2

dx, (29)

- β0 =

13 12

h ¯i−2 −2h¯i−1 +h¯i 2 +

1 4

h ¯i−2 −4h¯i−1 +3h¯i 2,

- β1 =

13 12

h ¯i−1 −2h¯i +h¯i+1 2 +

1 4

h ¯i−1 −h¯i+1 2,

- β2 =


13 12

1 4

h ¯i −2h¯i+1 +h¯i+2 2 +

3h¯i −4h¯i+1 +h¯i+2 2.

(30)

The non-linear WENO-Z weights ωzj are a slight modiﬁcation of the classical weights ωj. The new weights require the computation of a single additional parameter τ5 = |β2 −β0|:

p

ω˜kz ∑2l=0ω˜lz

τ5 βk +ε

γk βkz

ωkz =

, ω˜kz =

, βkz = 1+

. (31)

We use the power parameter p = 2 and regularization parameter ε = 10−12 for all of our simulations. With these deﬁnitions in place, the ﬁnal interpolated value is deﬁned as

WENO5+[h¯i−2,...h¯i+2] := ω0zh(i+0)1/2 +ω1zh(i+1)1/2 +ω2zh(i+2)1/2. (32)

- 3.1.2 The ﬁnite difference WENO method: MOL formulation for systems


For a system of conservation laws, the reconstruction procedure described in §3.1.1 is carried out locally on each of the scalar characteristic variables:

#### Finite difference WENO procedure for 1D systems

- 1. For each i, evaluate fi = f(qi) at each mesh point and compute average values of q at the half grid points

q∗

i−1/2 =

- 1

- 2


(qi +qi−1). (33)

Roe averages [51] may be used in place of (33), but all the results presented in this work use this arithmetic average.

- 2. Compute the left and right eigenvalue decomposition of f (q) = RΛR−1 at the half-grid points:

Ri−1/2 = R(q∗

i−1/2), R−1

i−1/2 = R−1(q∗

i−1/2). (34)

Compute α := maxi|f (q∗i−1/2)| as the fastest wave speed in the entire system. For stability, we follow the common practice of increasing α by exactly 10% in order to com-

pletely contain the fastest wave speed, that is, we set α = 1.1 · maxi|f (q∗i−1/2)|. The value |f (q)| is the maximum absolute value of all eigenvalues of the Jacobian, f (q).

- 3. For each i, determine the weighted ENO stencil {i + r} surrounding i. In ﬁfth order WENO, the full stencil is given by r ∈ {−3,−2,−1,0,1,2}. Project each qi+r and ﬂux


values fi+r onto the characteristic variables using R−1

i−1/2: wi+r = R−1

i−1/2 ·qi+r, (35a) gi+r = R−1

i−1/2 · fi+r. (35b) Apply Lax-Friedrichs ﬂux splitting on gi+r:

- 1

- 2


(gi+r ±α wi+r). (36) As an alternative, one could use a local wave speed. Note that for each component, these deﬁnitions automatically satisfy dgdw+ ≥ 0 and dgdw− ≤ 0.

g±

i+r =

###### 4. Perform a WENO reconstruction on the characteristic variables. Use the stencil which uses an extra point on the upwind direction for deﬁning g±:

gˆ+i−1/2 = WENO5+ g+i−3,g+i−2,g+i−1,g+i ,g+i+1 , gˆ−

i−1/2 = WENO5− g−

i−2,g−

i−1,g−

i ,g−

i+1,g−

i+2 . Deﬁne gˆi−1/2 := gˆ+i−1/2 +gˆ−

i−1/2.

###### 5. Using same projection matrix, Ri−1/2, project characteristic variables back onto the conserved variables:

fˆi−1/2 := Ri−1/2 ·gˆi−1/2. (37)

- 3.2 The ﬁnite difference WENO method: a multiderivative formulation


In order to implement multiderivative methods into the WENO framework, we closely follow previous work on Lax-Wendroff WENO methods [49], but in place of relying on a single-step Taylor series, we build intermediate stages of the form given by (13). Consider two ‘stages’, qn and q∗ that provide a pointwise approximation to the exact solution. If we apply (5) to each qn and q∗ and insert the result into (13), we see that the starting point for putting together a multiderivative WENO integrator is to deﬁne the following for arbitrary values of α, α∗, β and β∗:

q = qn −α∆t f (qn),x −α∗∆t f (q∗),x

(38)

−β∆t2 f (qn)qn,t ,x −β∗∆t2 f (q∗)q∗

,t ,x.

Note that we have retained the value q,t in place of substituting q,t = −f,x into the last two terms. This is different than what will be done in §4.2 for the multiderivative DG method. The complete multiderivative WENO method is given by the following:

#### Multistage multiderivative WENO procedure

- 1. Given two pointwise approximations qn and q∗, perform a single WENO reconstruction on each piece to construct the following values:

qni,t := −

1 ∆x

f ˆin+1/2 − fˆin−1/2 , q∗i,t := −

1 ∆x

f ˆ∗

i+1/2 − fˆ∗

i−1/2 . (39)

- 2. Deﬁne the pointwise values Gni := f (qni )qni,t and G∗i := f (q∗i )q∗i,t. Note that we do not need to decompose q onto the characteristic variables.
- 3. For each Gn and G∗ in Step 2, compute a ﬁnite difference approximation to Gn,x and G∗,x. Given that this term inherits an extra factor of ∆t, we can use the fourth-order centered ﬁnite difference:


1 12∆x

DxGi :=

(Gi−2 −8Gi−1 +8Gi+1 −Gi+2). (40)

Using a centered stencil means that the method will automatically be conservative. The complete WENO discretization of (38) is now,

qi = qni +α∆tqni,t +α∗∆tq∗i,t −β∆t2DxGni −β∗∆t2DxG∗i . (41)

This equation deﬁnes the building block for creating any two-derivative Runge-Kutta method, because the deﬁnitions for L and L˙ from Deﬁnition 2 are now in place.

We now summarize the entire multiderivative WENO procedure. Given a multiderivative Runge-Kutta scheme, we use a WENO reconstruction procedure to deﬁne q,t. Higher derivatives q,tt, etc. are deﬁned by ﬁrst using the Cauchy-Kowalewski procedure in (5) to deﬁne exact formulas for these terms. The spatial derivatives that show up in these terms are then discretized by using ﬁnite differences. Once q,t,q,tt, etc., have been deﬁned, one uses the coefﬁcients from the multiderivative scheme to construct stages as well as a ﬁnal update. This entire procedure generalizes both the Lax-Wendroff and RK-WENO methods. For completeness, we prove that the proposed scheme is conservative by showing that equation (41) is conservative for any choice of α, α∗, β and β∗ that are deﬁned by the selected multiderivative scheme.

Theorem 1 The proposed multistage multiderivative WENO scheme is mass conservative.

Proof The ﬁnal update, qni+1 is given by equation (41) for a collection of coefﬁcients α, α∗, β and β∗ that depend on the selected scheme. Summing over i produces

qin+1 =∑

## ∑

qni +α∆tqni,t +α∗∆tq∗i,t −β∆t2DxGni −β∗∆t2DxG∗i (42a)

i

i

## =∑

qni +α∆t∑

qni,t+α∗∆t∑

q∗i,t+β∆t2∑

DxGi+β∗∆t2∑

DxG∗i . (42b)

i

i

i

i

i

Conservation will follow after showing that the last four terms in equation (42b) are zero. First, observe that

1

## ∑

∆x∑

qni,t = −

i

i

1

∆x ∑

fˆin+1/2−∑

f ˆin+1/2 − fˆin−1/2 = −

fˆin−1/2 (43a)

i

i

1

∆x ∑

fˆin+1/2−∑

fˆin+1/2 = 0. (43b)

= −

i

i

Similarly, ∑iq∗i,t = 0. The last two terms sum to zero because a central difference stencil is used:

1

## ∑

12∆x∑

DxGni =

Gni−2 −8Gni−1 +8Gni+1 −Gni+2 (44a)

i

i

1

12∆x ∑

Gni−2−8∑

Gni−1+8∑

Gni+1−∑

Gni+2 (44b)

=

i

i

i

i

1

12∆x ∑

Gni −8∑

Gni +8∑

Gni −∑

Gni = 0. (44c)

=

i

i

i

i

Similarly, ∑iDxG∗i = 0, and therefore ∑iqni+1 = ∑iqni for all n. Remark 2 Various multistage multiderivative WENO methods can be built by repeated application of (41) with different values of α,α∗,β and β∗.

The procedure for constructing multiderivative WENO methods using (41) is identical to that already presented in §2.3 for ODEs. For example, setting β = β∗ = 0 reproduces Runge-Kutta methods, and setting α∗ = β∗ = 0 reproduces the second-order Lax-Wendroff WENO method, provided we deﬁne α = 1, and β = 1/2. The s = 3-stage analogue of equation (15) for PDEs is given by

qi = qni +α∆tqni,t +α∗∆tq∗i,t +α∗∗∆tq∗∗i,t

−β∆t2DxGni −β∗∆t2DxG∗i −β∗∗∆t2DxG∗∗i .

(45)

In addition, further derivatives can be included, but one would need to revisit (5) before inserting these terms. We would expect that higher derivatives can be approximated using smaller centered ﬁnite difference stencils because they get multiplied by increasing powers of ∆t (c.f. [49] for further details).

We repeat that equation (41) ﬁnishes the spatial discretization of (13). If we appeal to this equation twice we can construct the unique two-stage, fourth-order method, TDRK4 that is the PDE analogue of (18):

∆t 2∆x

q∗i = qni −

∆t ∆x

qni+1 = qni −

(∆t/2)2 2

f ˆin+1/2 − fˆin−1/2 −

(DxGi); (46a)

∆t2 6

f ˆin+1/2 − fˆin−1/2 −

(DxGi +2DxG∗i ). (46b)

Numerous examples of this WENO scheme are provided in §5, where we compare this method with classical fourth-order Runge-Kutta (RK4), as well as the third-order strong stability preserving (SSP) method of Shu and Osher [61]. Before presenting results, we ﬁrst describe an implementation of a multistage multiderivative discontinuous Galerkin method that will require a different approach to deﬁne the higher temporal derivatives.

#### 4 The discontinuous Galerkin (DG) method

The discontinuous-Galerkin (DG) method dates back to 1973 when Reed & Hill [50] developed the scheme for solving a neutron transport equation. The theoretical framework for the DG method was solidiﬁed by Bernardo Cockburn and Chi-Wang Shu through a lengthy series of papers. We refer the reader to their extensive review article and references therein [9]. In this section, we deﬁne the notation used for the remainder of this paper and provide minimal details necessary for reproducing this body of work. This section focuses on describing the Runge-Kutta discontinuous Galerkin (RKDG) scheme, and in §4.2, we introduce the multiderivative technology to the DG framework. We use similar notation to that was previously introduced [53], and for further details on the DG method, we direct the reader the references (e.g. [9,55]).

Similar to the layout of §3, we begin this section with the classical MOL formulation in §4.1, and continue in §4.2 with the proposed multiderivative DG method. We repeat that much like the material from §3.2, the multiderivative DG formulation relies on the multiderivative ODE methods from §2 but requires a very different application of the Cauchy Kowalewski procedure from equation (5).

- 4.1 The discontinuous Galerkin (DG) method: a MOL formulation


The DG method solves a discretization of the weak formulation of the hyperbolic conservation law (19). The continuous weak formulation can be realized by multiplying (19) with a test function ϕ, and integrating by parts over a control volume T = [x ,xr]:

xr x

ϕq,t dx =

xr x

ϕ,x f(q)dx− ϕ f(q)|xr − ϕ f(q)|x . (47)

We begin our discretization by deﬁning a grid containing mx cells for the domain [a,b], each of whose width is ∆x = (b−a)/mx. The ith grid cell is denoted by Ti = [xi−1/2,xi+1/2], where the cell edges are given by xi−1/2 = a+(i−1)∆x, for i = 1,2,...,mx+1, and the cell centers are given by xi = a+(i−1/2)∆x, for i = 1,2,...,mx. For simplicity of exposition, we will restrict our attention to a uniform grid. On this grid we deﬁne the broken ﬁnite element space

Wh = wh ∈ L∞(Ω) : wh|T ∈ Pp, ∀T ∈ Th , (48)

where h = ∆x. The above expression means that on each element T , wh will be a polynomial of degree at most p, and no continuity is assumed across element edges. Each element Ti can be mapped to the canonical element ξ ∈ [−1,1] via the linear transformation

∆x 2

x = xi +ξ

. (49)

Note that after a change of variables, spatial derivatives obey the following rule: ∂∂x = ∆2x ∂ξ∂ . For the canonical element, we construct a set of basis functions that are orthonormal with respect to the following inner product:

1 −1

- 1

- 2


ϕ( ), ϕ(k) :=

ϕ( )(ξ)ϕ(k)(ξ) dξ = δ k, (50)

where δ k is the Kronecker delta function. This deﬁnes the Legendre basis functions:

√5 2

√7 2

√3ξ,

3ξ2 −1 ,

(5ξ3 −3ξ), ... . (51)

ϕ( ) = 1,

We consider approximate solutions of the hyperbolic conservation law (19) that are deﬁned by a ﬁnite set of coefﬁcients Q(ik) of the basis functions ϕ(k) . When restricted to a single cell Ti, the approximate solution qh is

qh(t,x)

:= qhi (t,ξ) =

Ti

M

## ∑

Q(ik)(t)ϕ(k)(ξ), (52)

k=1

where M is the order of accuracy. The initial conditions are determined from the L2-projection of qh(0,x) onto the basis functions,

Q(ik)(0) := qhi (0,ξ), ϕ(k)(ξ) , (53) which we evaluate using M standard Gaussian quadrature points.

The semi-discrete weak formulation of (19) is given by discretizing (47) with a ﬁnite set of basis functions and a ﬁnite set of control volumes. Inserting our discrete spatial representation (52) into the continuous weak formulation (47) and using ϕ = ϕ(k) for our test function, we produce the semi-discrete weak formulation

2 ∆x

f qhi (t,ξ) ,ϕξ(k)(ξ) −

qhi,t(t,ξ),ϕ(k)(ξ) =

1 ∆x

ϕ(k)(ξ = +1)f↓(qh(t,xi+1/2)

(54)

1 ∆x

ϕ(k)(ξ = −1)f↓(qh(t,xi−1/2)),

+

where the ﬂux values f↓(qh(t,xi−1/2)) will be deﬁned through an appropriate Riemann solver. These terms will become responsible for all inter-cell communication.

Before going into the details of the Riemann solver, we seek a simpler representation of (54). We start by deﬁning the ﬁrst term on the right hand side of (54) as the interior integral

1 −1

1 ∆x

ϕξ(k)(ξ) f qhi (t,ξ) dξ, (55) and after rescaling, we deﬁne the last two terms as

Ni(k) :=

Fp(,ki)+1/2 := ϕ(k)(ξ = +1)f↓(qh(t,xi+1/2)), (56a) Fm(k,i)−1/2 := ϕ(k)(ξ = −1)f↓(qh(t,xi−1/2)). (56b)

With these deﬁnitions in place, the discrete weak formulation can now be compactly written as a large MOL system:

1 ∆x

d dt

##### Q(ik)(t) = Ni(k)(t)

Fp(,ki)+1/2(t)−Fm(k,i)−1/2(t)

. (57)

−

Interior

Edge

The only remaining piece to describe is how we compute the inter-cell ﬂux values, f↓(qh(t,xi−1/2)).

- 4.1.1 The discontinuous Galerkin (DG) method: a choice of Riemann solvers


Given that the representation of the solution, qh, is not forced to be continuous at the cell interfaces, care must be taken when deﬁning the ﬂux values f↓ qh(t,xi−1/2) . One could work with the so-called generalized Riemann solvers which take into account spatially varying function to the left and right of the discontinuity. One could also work with exact solutions for a classical Riemann problem in which one assumes constant states to the left and right of a discontinuity. In this work, we use Rusanov’s method [54], which is an approximate Riemann solver that is commonly called the local Lax-Friedrichs (LLF) Riemann solver given its similarity to the Lax-Friedrichs method. Much like the Lax-Friedrichs method, this solver approximates each Riemann problem with two waves with equal speeds traveling in opposite directions, but LLF uses a local speed in place of a global speed to do so.

Evaluating the basis functions to the left and right of a single interface located at xi−1/2 provides artiﬁcially constant states, deﬁned by a ﬁnite sum,

√5Q(i3) −

√7Q(i4) +··· (58a) Q = Q(i−1)1 +

√3Q(i2) +

Qr = Q(i1) −

√5Q(i−3)1 +

√7Q(i−4)1 +··· . (58b)

√3Q(i−2)1 +

The LLF solver deﬁnes a single value based on these two constant states:

- 1

- 2


(f (Ql)+ f (Qr))−α (Qr −Ql) . (59)

f↓(Ql,Qr) :=

We use a local value of α, deﬁned by α = max s1 , s2 , where s1 and s2 are the HLL(E) speeds [28] deﬁned by

- s1 = min min p

λ(p) Q ˆ , min

p

λ(p)(Ql) , (60a)

- s2 = max max p


λ(p) Q ˆ , max

λ(p)(Qr) , (60b)

p

and λ(p) are the eigenvalues of f . For this work, we take the simple arithmetic average Qˆ = 21 (Ql +Qr), but we point out that Roe averages could also be used [51].

This completes the DG method of lines (MOL) discretization for our PDE. The only remaining part is to evolve the discrete coefﬁcients through time. This is usually performed by explicit, high-order Runge-Kutta methods, resulting in a Runge-Kutta discontinuous Galerkin (RKDG) method. In principle, one may potentially work with this discretization to form a multiderivative integrator, which would require taking a second derivative of (57). However, difﬁculty will ensue when trying to compute the Jacobian of the complex system of ODEs in (54). Instead, we turn towards the Lax-Wendroff/Cauchy-Kowalewski discontinuous Galerkin methods to deﬁne a discrete second derivative.

- 4.2 The discontinuous Galerkin (DG) method: a multiderivative formulation


In this section, we extend the work of Qiu, Dumbser and Shu [48] to accommodate multiderivative technology. An investigation into other ﬂuxes would be an interesting topic of future study, including a comparison of various approximate Riemann solvers using multiderivative technology [47]; moreover, an investigation into generalized Riemann solvers [12,11,41] may yield some interesting results. At present, our current goal is to lay the foundation that would be necessary for such investigations.

Starting with the aim of deﬁning a single stage value (or full update) for a multiderivative integrator, a DG implementation of equation (13) from §2.3 requires the deﬁnition of q,tt

- as well as the deﬁnition of q ,tt. Here, we use q,tt = (f (q)fx)x in place of q,tt = −(f (q)qt)x which was used in §3.2 for the second derivative. After factoring out a single spatial derivative, we can write (13) as


q = qn −∆t α fn +α∗ f∗ −∆tβ f (qn)fxn −∆tβ∗ f (q∗)fx∗

, (61) where we have made use of the shorthand deﬁnitions

x

fn := f(qn), f∗ := f(q∗). (62)

We remark that after deﬁning the appropriate spatial discretization, equation (61) will look strikingly similar to the semi-discrete weak formulation already presented in equation (57).

Before proceeding onward, we argue that a complete understanding of how to discretize (61) will provide the necessary building block for arbitrary multiderivative Runge-Kutta integrators. For example, setting α∗ = β∗ = 0, we can view this as a single-step method, and therefore equation (61) is nothing other than the Lax-Wendroff DG scheme already

presented in the literature, provided the correct coefﬁcients are inserted. Moreover, setting β = β∗ = 0, this produces a two-stage Runge-Kutta method. Further stages can be included by adding in additional terms which introduces cumbersome notation. For clarity, we restrict our attention towards deﬁning the discrete formulation of (61) which is general enough to accommodate more complicated multiderivative time integrators.

The ﬁrst step is to construct a Galerkin representation of the ﬂux function fh as well as necessary coefﬁcients for the second time derivative, gh := f (qh)f(qh)x. These two functions are the ﬁrst and second, respectively, time derivatives of q before taking the ﬁnal spatial derivative. The Galerkin coefﬁcients for these spatial derivatives can be constructed by taking advantage of the basis functions:

#### Procedure 1.1

INPUT:

Q(ik) − a list of Galerkin coefﬁcients of qh. OUTPUT:

Fi(k) − a list of Galerkin coefﬁcients of f(qh), and G(ik) − a list of Galerkin coefﬁcients of f (qh)fx.

- 1. For each element Ti, evaluate the ﬂux function, fi(ξ) := f(qhi (ξ)) and the Jacobian Ji(ξ) := f (qhi (ξ)) at a list of M quadrature points, {ξ1,...ξM}. Here, ξ is the canonical variable for grid element Ti related to x through (49).
- 2. Compute the projection of fi(ξ) onto the basis functions using the point values from Step 1:

Fi(k) := fi(ξ), ϕ(k)(ξ) . (63)

This projection step produces a Galerkin expansion of the ﬂux function on grid element Ti, that when written in the canonical variable is given by,

fi(ξ) :=

M

∑

k=1

Fi(k)(t)ϕ(k)(ξ). (64)

- 3. Differentiate the ﬂux function fi(ξ) on the interior of cell Ti to produce

∂x fi(ξ) :=

2 ∆x

M

∑

k=1

Fi(k)

∂ϕ ∂ξ

(k)

(ξ). (65)

Note that this differentiation step is only valid on the interior of each cell. Evaluate this function at the interior quadrature points, {ξ1,ξ2,...,ξM}.

- 4. Deﬁne the Galerkin coefﬁcients of gh as, G(ik) := Ji(ξ)·∂x fi(ξ), ϕ(k)(ξ) . (66)


The required point values for the integration for Ji(ξm) were computed in Step 1, and the required point values of ∂x fi(ξm) were computed in Step 3 by differentiating the basis functions.

We remark that differentiating the basis functions loses a single order of accuracy, but given that those terms involving gh are multiplied by ∆t = O(∆x), we recover the desired order of accuracy. We are now prepared to describe the full multistage multiderivative DG method.

#### Multistage multiderivative DG procedure

- 1. Given a pair of Galerkin expansions qh and q∗, we compute four Galerkin expansions fh,gh, f∗ and g∗ using Procedure 1.1.
- 2. Deﬁne a modiﬁed ﬂux function f˜h via f˜h := α fh +α∗ f∗ +∆t βgh +β∗g∗ . (67)

We remark that we have a full Galerkin expansion of this modiﬁed ﬂux function, that when restricted to a single element, is given by

f˜h(x)

Ti

=

M

∑

k=1

F˜i(k)ϕ(k)(ξ), (68)

F˜i(k) := αFi(k) +α∗F∗(k)

i +∆t βGi(k) +β∗G∗(k)

i . (69) We can now simplify equation (61) by compactly writing it as

q = qn −∆t f˜hx. (70)

- 3. Construct the time integrated weak formulation by multiplying (70) by a test function ϕ(k) and integrate by parts over a grid cell Ti:

Q(ik)(t) = Q(ik)(tn)+∆tN˜i(k)(tn)−

∆t ∆x

F ˜p(,ki)+1/2(tn)−F˜m(k,i)−1/2(tn) . (71) The only remaining piece is to deﬁne the ﬂux values, as well as deﬁne a proper left and right ﬂux value for the Riemann solver. The interior integrals N˜i(k) are given by integration of the Galerkin expansion of f˜h:

N˜i(k) :=

1 ∆x

1 −1

ϕξ(k) f˜h(ξ) dξ. (72) Once we have the Galerkin expansion of f˜h, these integrals can be evaluated exactly.

- 4. Solve Riemann problems for the modiﬁed ﬂux function. In place of using equations


(58a) and (58b) to deﬁne the left and right hand side F and Fr of the Riemann problem, we insert the extra time derivatives drawn from f˜h and tuck them into this evaluation.

That is, at the grid interface located at xi−1/2, we redeﬁne the left and right values of fh to be the left hand side and right hand side evaluations of f˜h:

F :=fˆh(x−

i−1/2) =

Fr :=fˆh(xi+−1/2) =

M

M

## ∑

## ∑

F˜i(−k1)ϕ(k)(ξ = +1) =

k=1

k=1

M

## ∑

F˜i(k)ϕ(k)(ξ = −1),=

k=1

√2k−1F˜i(−k1), (73a)

M

√2k−1F˜i(k). (73b)

## ∑

(−1)k

k=1

This completes the multiderivative description of the method within the discontinuous Galerkin framework. Extensions to multiderivative integrators that require more stages or more derivatives are a tedious, yet straight-forward extension of what has already been presented in this section together with the methods presented in §2.3 for ODEs. Extensions to methods with more stages would require adding more values of α∗ and β∗ to the deﬁnition of the modiﬁed ﬂux function, f˜h in equation (67). For example, deﬁning the modiﬁed ﬂux function by

f˜h := α fh +α∗ f∗ +α∗∗ f∗∗ +∆t βgh +β∗g∗ +β∗∗g∗∗ (74)

allows us to use any ODE solver derived from (14) in §2.3, such as the ﬁfth-order twoderivative method presented in (17).

Extensions to methods with more derivatives require bootstrapping previous Lax-Wendroff

DG work [48], much like what has already been performed here. This would involve the appropriate extension of Procedure 1.1 using the Cauchy-Kowalewski procedure from equation (5), which would deﬁne an appropriate modiﬁcation f˜ of the ﬂux function f that contains extra time information of the PDE.

- 4.3 The discontinuous Galerkin (DG) method: a choice of limiters


The one detail that has been left out of this discussion has been the choice of limiting options. It is a well known fact that high-order linear methods exhibit oscillatory behavior near discontinuities, and therefore to obtain physically relevant results, one needs to choose a limiter that ideally retains high order accuracy in smooth regions, and reduces to ﬁrst order accuracy locally at the location of the shock. In this work, we use the moment based limiter developed by Krivodonova [35] for our numerical simulations, although other limiters may certainly be used as well, with no change to the general framework presented thus far. This limiter is applied after each stage of the (multiderivative) Runge-Kutta method, and it

modiﬁes the higher order terms Q(ik),k ≥ 2 after each time step. One advantage of using multiderivative methods is that expensive limiters need to be applied less often when compared to high-order, single-derivative counterparts because of the reduction in the number of stages.

#### 5 Numerical examples

In this section, we present results of the proposed method on a variety of hyperbolic conservation laws. In §§5.1 – 5.2, we consider scalar examples: constant coefﬁcient advection, and the Buckley-Leverett two-phase ﬂow model. In §§5.3 – 5.4, we present results for the shallow water and Euler equations. All discontinuous Galerkin solutions were run using the open-source software DoGPack [52].

Unless otherwise noted, we use the following parameters:

- – The time integrator is the unique two-stage, two-derivative, fourth-order Runge-Kutta method (TDRK4) from equation (18).
- – All ﬁnite difference WENO simulations use the ﬁfth order WENO5-Z reconstruction from §3 and a constant CFL number of ν = 0.4 = maxq∗ |f (q∗)| ∆∆xt .


- Table 6 CFL parameters used for DG simulations that compare time integrators. The SSP-RK3 method is the optimal third order SSP method developed by Shu and Osher [61] and described by Gottlieb and Shu [21]. SSP-RK4 is a fourth-order, low-storage method with ten stages developed by Ketcheson [33]. The maximum


allowable CFL number, νmax is near the maximum possible stable time step that each method permits for fourth-order spatial accuracy. We note that SSP-RK4 has a much higher CFL limit when compared to either TDRK4 or SSP-RK3 because it incorporates many more stages, but each stage requires expensive applications of limiters. It would be interesting to investigate optimized versions of TDRK4 using (13) as a building block that allow taking larger time steps without adding extra storage.

|DG time stepping parameters| |ν<br><br>|νmax|
|---|---|---|---|


|Third-order (SSP-RK3)| |0.125|0.130|
|---|---|---|---|
|Low-storage SSP Runge-Kutta (SSP-RK4)| |0.44<br><br>|0.45|
|Two-derivative Runge-Kutta (TDRK4)| |0.08<br><br>|0.085|


– Every DG result is fourth-order accurate in space, and uses a desired CFL number of ν = 0.08. If the maximum allowable CFL number deﬁned by νmax = 0.085 is violated, a smaller time step is chosen. For visualization, we plot exactly 4 uniformly spaced points per grid cell.

For the two problems where other time integrators are compared against the TDRK4 method, we use coefﬁcients in Table 6 for the DG simulations.

- 5.1 Linear advection


Our ﬁrst examples are variations on the scalar linear advection equation with periodic boundary conditions:

q,t +q,x = 0, x ∈ [−1,1]. (75)

- 5.1.1 Linear advection: a smooth example For a smooth example, we use initial conditions


q(0,x) = q0(x) = sin(πx), (76)

and we run the simulation up to t = 2.0, at which point the exact solution is given by the initial conditions. This is one of two problems where we compare popular time integrators against the new method. Convergence studies are presented in Tables 7 and 8. For the WENO scheme and for this problem only, we run this problem with a large CFL number of ν = 0.9 in order to make the temporal error the preponderant part of the total error; accordingly, in Table 1 we observe the fourth-order time accuracy of RK4 and TDRK4.

Relative errors for the WENO scheme are deﬁned by an L2 norm based on point-wise values:

∆x∑mi=x1(qni −q(tn,xi))2 ∆x∑mi=x1q(tn,xi)2

Error :=

. (77)

Errors for the DG simulations likewise use a relative L2-norm, but this can be based on integration against the exact solution using moments of the solution (c.f. [53]).

- Table 7 Advection equation: smooth example. Convergence analysis for the WENO scheme applied to the advection equation (75) with periodic boundary conditions and smooth initial conditions (76). The table shows a comparison of the relative L2-norm of the errors in the numerical solutions obtained with WENO5Z spatial discretization and different time integrators: 3rd-order strong stability preserving Runge-Kutta (SSP-RK3) [61], classical 4th-order Runge-Kutta (RK4), and the new two-derivative 4th-order Runge-Kutta (TDRK4) method. The Courant parameter chosen for this problem was a constant CFL of ν = 0.9 = ∆t/∆x. In order to observe fourth-order accuracy for the fourth-order methods, we needed to increase the CFL number and therefore increase the temporal error. Results for smaller CFL numbers reached machine precision before announcing their accuracy, where both RK4 and TDRK4, indicated convergence orders between 4th and 5th order. The ‘Order’ columns refer to the algebraic order of convergence, computed as the base-2 logarithm of the ratio of two successive error norms. We remark that for all CFL numbers and weighting schemes tested, including WENO-Z, WENO-JS and linear weights, both time integrators RK4 and TDRK4 have comparable errors.

|Mesh| |SSP-RK3<br><br>|Order| |RK4<br><br>|Order| |TDRK4<br><br>|Order|
|---|---|---|---|---|---|---|---|---|---|


|25| |3.09×10−03|—| |2.00×10−04|—| |1.52×10−04<br><br>|—|
|---|---|---|---|---|---|---|---|---|---|
|50| |3.79×10−04<br><br>|3.03| |9.68×10−06|4.37| |8.77×10−06<br><br>|4.11|
|100| |4.74×10−05|3.00| |5.54×10−07<br><br>|4.13| |5.39×10−07|4.02|
|200| |5.92×10−06|3.00| |3.37×10−08<br><br>|4.04| |3.35×10−08<br><br>|4.01|
|400| |7.39×10−07<br><br>|3.00| |2.09×10−09<br><br>|4.01| |2.09×10−09|4.00|
|800| |9.24×10−08<br><br>|3.00| |1.31×10−10<br><br>|4.00| |1.31×10−10|4.00|
|1600| |1.16×10−08<br><br>|3.00| |8.33×10−12<br><br>|3.97| |8.33×10−12|3.97|


- Table 8 Advection equation: smooth example. We present DG-results comparing the new multiderivative scheme TDRK4 against third-order SSP-RK3 [61,21] and a state of the art low-storage fourth-order RungeKutta method (SSP-RK4) [33]. The CFL numbers chosen for each scheme are presented in Table 6, which are near the maximum stable CFL limit for each scheme.


|Mesh| |SSP-RK3|Order| |SSP-RK4<br><br>|Order| |TDRK4<br><br>|Order|
|---|---|---|---|---|---|---|---|---|---|


|5| |1.17×10−03|—| |6.18×10−04|—| |8.21×10−04<br><br>|—|
|---|---|---|---|---|---|---|---|---|---|
|10| |1.32×10−04<br><br>|3.16| |3.87×10−05|4.00| |5.99×10−05|3.78|
|20| |1.60×10−05|3.04| |2.43×10−06|3.99| |3.91×10−06<br><br>|3.94|
|40| |1.99×10−06<br><br>|3.01| |1.52×10−07|4.00| |2.47×10−07|3.98|
|80| |2.48×10−07<br><br>|3.00| |9.51×10−09|4.00| |1.55×10−08<br><br>|4.00|
|160| |3.10×10−08|3.00| |5.94×10−10|4.00| |9.69×10−10|4.00|
|320| |3.87×10−09<br><br>|3.00| |3.72×10−11|4.00| |6.03×10−11|4.01|
|640| |4.84×10−10<br><br>|3.00| |2.24×10−12|4.05| |4.39×10−12<br><br>|3.78|


5.1.2 Linear advection: a challenging example

The second example we test is more challenging. The initial conditions are a combination of four bell-like shapes with different degrees of smoothness, that was originally proposed

by Jiang and Shu [30]:



1 6 [G(x,β,z−δ)+G(x,β,z+δ)+4G(x,β,z)], −0.8 ≤ x ≤ −0.6; 1, −0.4 ≤ x ≤ −0.2;



q0(x) =

(78a)

1−|10(x−0.1)|, 0 ≤ x ≤ 0.2;

1 6 [F(x,α,a−δ)+F(x,α,a+δ)+4F(x,α,a)], 0.4 ≤ x ≤ 0.6;



0, otherwise.

G(x,β,z) = e−β(x−z)2; (78b) F(x,α,a) = max(1−α2(x−a)2,0). (78c)

The constants are a = 0.5, z = −0.7, δ = 0.005, α = 10 and β = log10(2)/(36δ2). With this choice of constants, the Gaussian curve centered at x = −0.7 contains two discontinuities, and the bump centered at x = 0.5 also has two discontinuities. Moreover, this last bump has no derivative at x = 0.405 and x = 0.595.

After testing many different reconstruction procedures of varying orders, many different time integrators and a large range of parameters, our observations indicate that all WENO methods are sensitive to the parameters used for this test problem. It has already been observed that WENO schemes may require tuning in order to achieve good results [2]; this is not the subject of this work, but we ﬁnd it necessary to point out that WENO simulations do not emulate robust behavior for this problem. A numerical investigation into their behavior on linear problems with difﬁcult initial conditions such as (78a)-(78c) would be interesting.

Results for this problem are presented in Figure 3. The under-resolved DG simulations tend to be quite diffusive when compared to the WENO schemes, but behave much more predictably.

- 5.2 Buckley-Leverett


The Buckley-Leverett equation is a non-linear scalar problem with a non-convex ﬂux function. Years past its invention, it has become a standard benchmark problem for many hyperbolic solvers. The model describes two-phase ﬂow through porous media, where the application is oil recovery from a reservoir containing an oil-water or oil-gas mixture of ﬂuids [3]. In rescaled units, the ﬂux function for this problem is deﬁned through a single free parameter M with

q2 q2 +M(1−q)2

f(q) =

. (79)

We use M = 1/3, and we take the computational domain to be [−1,1] with initial conditions prescribed through

q(0,x) =

1, if −1/2 ≤ x ≤ 0, 0, otherwise.

(80)

For small time values, the exact solution to this problem can be found by solving two Riemann problems, where each pair of states produces a typical ‘compound wave’ that is

WENO solution at t = 8.0

WENO solution at t = 8.0

1.0

Exact

Exact

1.02

mx = 150 mx = 450

mx = 150 mx = 450

0.8

1.00

0.6

q(x)

q(x)

0.98

0.4

0.96

0.2

0.94

0.0

−1.0 −0.5 0.0 0.5 1.0

−0.40 −0.35 −0.30 −0.25 −0.20

x

x

DG solution at t = 8.0

DG solution at t = 8.0

1.0

Exact

Exact

1.02

mx = 80

mx = 80

mx = 120

mx = 120

0.8

1.00

0.6

q(x)

q(x)

0.98

0.4

0.96

0.2

0.94

0.0

−1.0 −0.5 0.0 0.5 1.0

−0.40 −0.35 −0.30 −0.25 −0.20

x

x

- Fig. 3 Advection equation: a discontinuous example. Results for the two-derivative (TDRK4) method for WENO and DG spatial discretizations. Simulations are run to a ﬁnal time of t = 8.0 for a total of four full revolutions. The two images on the right are zoomed in images of the top of the square wave. WENO simulations use a CFL number of ν = 0.4, and the DG simulations use a constant CFL number of ν = 0.08. We again plot four points per cell for the DG solutions.


the combination of a leading shock and a trailing rarefaction. Each shock propagates with a speed dictated by the Rankine-Hugoniot conditions

f(q∗)− f(qc) q∗ −qc

f (q∗) =

, (81)

where qc is the constant value that does not change. For the Riemann problem located at x = −0.5, we have qc = 1, and q∗ ≈ 0.1339745962155613, and for the Riemann problem located

- at x = 0.0, we have qc = 0 and q∗ = 0.5. Characteristics between q∗ and qc propagate with speed f (q), and therefore to ﬁll the rarefaction fan, we plot a range of values (s+t f (q),q),


where q is a sampling of values between qc and q∗, and s ∈ {−0.5,0.0} is the location of each Riemann problem. Results for the two spatial discretizations are presented in Figures

- 4 and 5 at a ﬁnal time of t = 0.4. In addition, we compare three different two-derivative methods that were presented in §2.3 in Figure 6.


As a ﬁnal note, we remark that for this problem only, we modify our scheme to deal with some pathological issues. Given that the ﬂux function is non-convex, the WENO simulations use the analytical value for α, which is approximately α := maxq∈[0,1]|f (q)| ≈ 2.205737062. For the DG simulations, we use the HLL(E) Riemann solver [28]. In this case, the HLL(E) solver performs better than the local Lax-Friedrichs (LLF) solver given that f (q) ≥ 0 for

all q in our domain. The LLF solver approximates this problem with two waves traveling in opposite directions, whereas the exact solution travels in one direction only, which the HLL(E) correctly accounts for.

WENO solution (mx = 100)

WENO solution (mx = 100)

1.02

1.0

Exact

Exact

SSP-RK3

SSP-RK3

1.00

RK4

RK4

0.8

0.98

TDRK4

TDRK4

0.96

0.6

0.94

q(x)

q(x)

0.92

0.4

0.90

0.2

0.88

0.86

0.0

−1.0 −0.5 0.0 0.5 1.0

−0.10 −0.05 0.00 0.05 0.10

x

x

WENO solution (mx = 600)

WENO solution (mx = 600)

1.015

1.0

Exact

Exact

SSP-RK3

SSP-RK3

1.010

RK4

RK4

0.8

TDRK4

TDRK4

1.005

0.6

1.000

q(x)

q(x)

0.995

0.4

0.990

0.2

0.985

0.0

0.980

−1.0 −0.5 0.0 0.5 1.0

−0.08 −0.06 −0.04 −0.02 0.00 0.02

x

x

- Fig. 4 Buckley-Leverett double Riemann problem: WENO solutions. WENO results at the ﬁnal time of t = 0.4. All time integrators compared for this method are giving similar results. We remark that for this problem, the WENO schemes tend to be more diffusive where the rarefactions form when compared to the DG schemes.


- 5.3 Shallow water


The shallow water equations deﬁne a hyperbolic system with two conserved quantities: the water height h, and velocity u. The system is deﬁned by

h hu ,t

+

hu hu2 + 12gh2 ,x

= 0. (82)

For our simulation, we take g = 1. We demonstrate our method on the dam break Riemann problem [37] with initial conditions deﬁned by

(3,0)T, if x ≤ 0.5, (1,0)T, otherwise.

(h,u)T =

(83)

DG solution (mx = 40)

DG solution (mx = 40)

1.02

1.0

Exact

Exact

- SSP-RK3

- SSP-RK4


- SSP-RK3

- SSP-RK4


1.00

0.8

0.98

TDRK4

TDRK4

0.96

0.6

0.94

q(x)

q(x)

0.92

0.4

0.90

0.2

0.88

0.86

0.0

−1.0 −0.5 0.0 0.5 1.0

−0.10 −0.05 0.00 0.05 0.10

x

x

DG solution (mx = 80)

DG solution (mx = 80)

1.015

1.0

Exact

Exact

- SSP-RK3

- SSP-RK4


- SSP-RK3

- SSP-RK4


1.010

0.8

TDRK4

TDRK4

1.005

0.6

1.000

q(x)

q(x)

0.995

0.4

0.990

0.2

0.985

0.0

0.980

−1.0 −0.5 0.0 0.5 1.0

−0.08 −0.06 −0.04 −0.02 0.00 0.02

x

x

- Fig. 5 Buckley-Leverett double Riemann problem: DG solutions. DG results at the ﬁnal time of t = 0.4. We plot exactly four uniformly spaced grid points per cell. The top row uses mx = 40 grid cells, and the bottom row uses mx = 80 grid cells. The two frames on the right are zoomed in images of the solution near x = 0.0, one of the few places where we were able to ﬁnd differences in the solutions. We note that the coarse solution is under resolved because it only has a single cell to capture the structure at the top of the solution. CFL numbers are chosen as in Table 6, which are close to the maximum stable time step allowed. All time integrators are qualitatively giving the same result.


We use a computational domain of [0,1] with outﬂow boundary conditions, and stop the simulation at a ﬁnal time of t = 0.2. Results for the two-derivative time integrators are presented in Figure 7 for the WENO method, and in Figure 8 for the discontinuous Galerkin scheme. Exact solutions for this problem can be found in textbooks [37].

- 5.4 Euler equations


The Euler equations describe the evolution of density ρ, momentum ρu and energy E of an ideal gas:

 

 

 

 

ρu ρu2 + p (E + p)u

ρ ρu E

= 0, (84)

+

,t

,x

where p is the pressure. The energy E is related to the primitive variables ρ, u and p by E =

p γ −1

- 1

- 2


ρu2, (85)

+

WENO solution (mx=100)

WENO solution (mx=100)

1.0

Exact

Exact

1.00

- TDRK3

- TDRK4

- TDRK5


- TDRK3

- TDRK4

- TDRK5


0.98

0.8

0.96

0.6

0.94

q(x)

q(x)

0.92

0.4

0.90

0.2

0.88

0.86

0.0

1.0 0.5 0.0 0.5 1.0 x

0.10 0.05 0.00 0.05 0.10 x

WENO solution (mx=600)

WENO solution (mx=600)

1.0

Exact

Exact

1.002

- TDRK3

- TDRK4

- TDRK5


- TDRK3

- TDRK4

- TDRK5


1.000

0.8

0.998

0.6

0.996

q(x)

q(x)

0.994

0.4

0.992

0.2

0.990

0.988

0.0

1.0 0.5 0.0 0.5 1.0 x

0.07 0.06 0.05 0.04 0.03 0.02 0.01 0.00 x

- Fig. 6 Buckley-Leverett double Riemann problem: WENO solutions. WENO results at the ﬁnal time of t = 0.4. Here, we compare three different two-derivative methods that are presented in §2.3: TDRK3 (16), TDRK4 (18) and TDRK5 (17). The only noticeable difference is given by the third-order scheme, and we attribute this to the lower order temporal accuracy.


where γ is the ratio of speciﬁc heats. For all of our simulations, we take γ = 1.4.

- 5.4.1 Euler equations: a shock tube Riemann problem


We present a classic test case of a difﬁcult shock tube, which is commonly referred to as the Lax shock tube. The initial conditions are those deﬁned by Harten [26,27]:

(ρ,ρu,E )T =

(0.445,0.3111,8.928)T, if x ≤ 0.5, (0.5,0,1.4275)T, otherwise.

(86)

Exact solutions for this problem are well understood, and there are many textbooks that describe how to construct them [37,67]. For this set of data, the solution contains a left rarefaction, a contact discontinuity and a shock wave traveling to the right.

We select t = 0.16 for the ﬁnal time of our simulation [49], and we use a computational domain of [0,1] with outﬂow boundary conditions. Results for this problem are presented in Figures 9 and 10. For the WENO simulations, we additionally compare the two-derivative two-derivative time integrator TDRK4 against the SSP-RK3 with two different CFL numbers, ν = 0.01 and then ν = 0.4. We present results for the time integrator comparison in Figure 11.

mx = 50

mx = 50

2.15

mx = 150

mx = 150

2.5

2.10

2.05

h

h

2.0

2.00

1.95

1.5

1.90

1.85

1.0

0.0 0.2 0.4 0.6 0.8 1.0

0.30 0.32 0.34 0.36 0.38 0.40

x

x

Momentum at t = 0.2

Momentum at t = 0.2

Exact

Exact

1.4

1.45

mx = 50

mx = 50

mx = 150

mx = 150

1.2

1.40

1.0

0.8

1.35

hu

hu

0.6

1.30

0.4

1.25

0.2

0.0

1.20

0.0 0.2 0.4 0.6 0.8 1.0

0.76 0.78 0.80 0.82 0.84

x

x

- Fig. 7 Shallow water Riemann problem: WENO solutions. Here we present two resolutions on top of each other using the new multiderivative scheme presented in §3.2. We use mx = 50 points for a coarse resolution and mx = 150 points for a ﬁner solution. Top row: water height h at the ﬁnal time with a zoom in of the rarefaction to the right. Bottom row: momentum hu, with a zoom in of the shock to the right.


- 5.4.2 Euler equations: shock entropy


Our ﬁnal test case is another problem that is popular in the literature [62]. The initial conditions are

(ρ,u, p) =(3.857143,2.629369,10.3333), x < −4, (ρ,u, p) =(1+ε sin(5x),0,1), x ≥ −4,

with a computational domain of [−5,5]. The ﬁnal time for this simulation is t = 1.8. With ε = 0, this is a pure Mach 3 shock moving to the right. We follow the common practice of setting ε = 0.2.

Results for WENO simulations are presented in Figure 12, and DG results are presented in Figure 13. For a reference solution, we plot a WENO simulation that uses the SSP-RK3 method described in Gottlieb and Shu [21], with mx = 6000 points and a small CFL number of ν = 0.1.

mx = 20 mx = 60

mx = 20 mx = 60

2.15

2.5

2.10

2.05

h

h

2.0

2.00

1.95

1.5

1.90

1.85

1.0

0.0 0.2 0.4 0.6 0.8 1.0

0.30 0.32 0.34 0.36 0.38 0.40

x

x

Momentum at t = 0.2

Momentum at t = 0.2

Exact

Exact

1.4

1.45

mx = 20 mx = 60

mx = 20 mx = 60

1.2

1.40

1.0

0.8

1.35

hu

hu

0.6

1.30

0.4

1.25

0.2

0.0

1.20

0.0 0.2 0.4 0.6 0.8 1.0

0.76 0.78 0.80 0.82 0.84

x

x

- Fig. 8 Shallow water Riemann problem: DG solutions. Here we present two resolutions on top of each other using the new multiderivative scheme presented in §4.2. We use mx = 20 cells for a coarse resolution and mx = 60 cells for a ﬁner solution, and we plot exactly four uniformly spaced points per cell. Top row: water height h at the ﬁnal time with a zoom in of the rarefaction to the right. Bottom row: momentum hu, with a zoom in of the shock to the right.


#### 6 Conclusions and future work

We have presented a family of methods that generalize popular high-order time integration methods for hyperbolic conservation laws. The explicit multistage multiderivative (multiderivative Runge-Kutta) time integrators that are the subject of this work provide the ability to access to higher temporal derivatives for an explicit (single-derivative) Runge-Kutta method, and they introduce degrees of freedom by adding stages to high-order (single-stage) Taylor methods. Numerous numerical examples were presented that included multiderivative schemes for high-order discontinuous Galerkin and WENO methods. In order to implement the multiderivative technology, we leveraged recent work on Lax-Wendroff type time integrators for the two aforementioned spatial discretizations investigated; each method required a very different procedure for deﬁning the higher derivatives. Numerical results for the new multiderivative schemes are promising: they are demonstrably comparable to those obtained from popular high-order SSP integrators, they introduce greater portability to high-order Lax-Wendroff methods, and they decrease the memory footprint for RungeKutta methods by introducing higher time derivatives.

Future work will focus on extensions to higher dimensions, as well as a mathematical exploration into the numerical properties of multiderivative schemes for PDEs. In addition,

mx = 100 mx = 300

1.0

1.2

ρ

ρ

0.8

1.1

0.6

1.0

0.4

0.0 0.2 0.4 0.6 0.8 1.0

0.75 0.80 0.85 0.90

Velocity at t = 0.16

Velocity at t = 0.16

1.65

1.5

1.60

1.55

1.0

1.50

u

u

1.45

0.5

1.40

1.35

0.0

0.0 0.2 0.4 0.6 0.8 1.0

0.22 0.24 0.26 0.28 0.30

Pressure at t = 0.16

Pressure at t = 0.16

| | | | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |


2.70

3.5

2.65

3.0

2.5

2.60

p

p

2.0

2.55

1.5

2.50

1.0

2.45

0.5

0.0 0.2 0.4 0.6 0.8 1.0

0.22 0.24 0.26 0.28 0.30

x

x

- Fig. 9 Shock-tube Riemann problem: WENO solutions. Shown here are WENO simulations with Harten’s initial conditions (86) for the shock tube problem. We plot observable quantities from top to bottom: density ρ, velocity u, and pressure p. Left columns are the full solution, and right columns are zoomed in parts of


the same data points. We present a coarse solution with mx = 100 points and a ﬁner solution of mx = 300 points. The zoomed in image of the density indicates the top part of the square section between the contact discontinuity and the right traveling shock. The zoomed in images for the velocity and pressure focus in on the right foot of the rarefaction fan.

an investigation into the optimization of these methods for modern computer architectures such as graphics processing units (GPUs) should be conducted. This will include implementation and timing comparison tests of these methods on GPUs. We would like to explore developing multiderivative methods with SSP properties, as well as low-storage ‘many’-stage variations of the two-derivative method presented in this work. Additionally, we would like to investigate implicit and explicit multistage multiderivative methods for solving parabolic partial differential equations.

Acknowledgements This work has been supported in part by Air Force Ofﬁce of Scientiﬁc Research grants FA9550-11-1-0281, FA9550-12-1-0343 and FA9550-12-1-0455, and by National Science Foundation grant number DMS-1115709. We would like to thank Matthew F. Causley for discussing multiderivative methods with us, and Qi Tang for useful discussions on the WENO method.

mx = 70

mx = 210

1.0

1.2

ρ

ρ

0.8

1.1

0.6

1.0

0.4

0.0 0.2 0.4 0.6 0.8 1.0

0.75 0.80 0.85 0.90

Velocity at t = 0.16

Velocity at t = 0.16

1.65

1.5

1.60

1.55

1.0

1.50

u

u

1.45

0.5

1.40

1.35

0.0

0.0 0.2 0.4 0.6 0.8 1.0

0.22 0.24 0.26 0.28 0.30

Pressure at t = 0.16

Pressure at t = 0.16

| | | | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |


2.70

3.5

2.65

3.0

2.5

2.60

p

p

2.0

2.55

1.5

2.50

1.0

2.45

0.5

0.0 0.2 0.4 0.6 0.8 1.0

0.22 0.24 0.26 0.28 0.30

x

x

- Fig. 10 Shock-tube Riemann problem: DG solutions. We present two DG simulations for the physical observables, which from top to bottom are: density ρ, velocity u, and pressure p. Left columns are the full solution, and right columns are zoomed in parts of the same data points. We present a coarse solution with


mx = 70 grid cells and a ﬁner solution of mx = 210 grid cells, and we plot four uniformly spaced points per cell. The axes are identical to those in Figure 9.

#### References

- 1. Bettis, D.G., Horn, M.K.: An optimal (m + 3)[m + 4] Runge Kutta algorithm. In: Proceedings of the Fifth Conference on Mathematical Methods in Celestial Mechanics (Oberwolfach, 1975), Part I, vol. 14, pp. 133–140 (1976)
- 2. Borges, R., Carmona, M., Costa, B., Don, W.S.: An improved weighted essentially non-oscillatory scheme for hyperbolic conservation laws. J. Comput. Phys. 227(6), 3191–3211 (2008)
- 3. Buckley, S.E., Leverett, M.C.: Mechanism of ﬂuid displacement in sands. Trans. AIME 146 (1942)
- 4. Butcher, J.C.: General linear methods: a survey. Appl. Numer. Math. 1(4), 273–284 (1985)
- 5. Butcher, J.C.: General linear methods. Comput. Math. Appl. 31(4-5), 105–112 (1996). Selected topics in numerical methods (Miskolc, 1994)
- 6. Butcher, J.C.: General linear methods. Acta Numer. 15, 157–256 (2006)
- 7. Castro, M., Costa, B., Don, W.S.: High order weighted essentially non-oscillatory WENO-Z schemes for hyperbolic conservation laws. J. Comput. Phys. 230(5), 1766–1792 (2011)
- 8. Chan, R.P.K., Tsai, A.Y.J.: On explicit two-derivative Runge-Kutta methods. Numer. Algorithms 53(23), 171–194 (2010)
- 9. Cockburn, B., Shu, C.W.: Runge-Kutta discontinuous Galerkin methods for convection-dominated problems. J. Sci. Comput. 16(3), 173–261 (2002)
- 10. Daru, V., Tenaud, C.: High order one-step monotonicity-preserving schemes for unsteady compressible ﬂow calculations. J. Comput. Phys. 193(2), 563–594 (2004)
- 11. Dumbser, M., Balsara, D.S., Toro, E.F., Munz, C.D.: A uniﬁed framework for the construction of one-step ﬁnite volume and discontinuous Galerkin schemes on unstructured meshes. J. Comput. Phys. 227(18), 8209–8253 (2008)


SSP-RK3 (ν = 0.40) SSP-RK3 (ν = 0.01) TDRK4

1.0

1.2

ρ

ρ

0.8

1.1

0.6

1.0

0.4

0.0 0.2 0.4 0.6 0.8 1.0

0.75 0.80 0.85 0.90

Velocity at t = 0.16

Velocity at t = 0.16

1.65

1.5

1.60

1.55

1.0

1.50

u

u

1.45

0.5

1.40

1.35

0.0

0.0 0.2 0.4 0.6 0.8 1.0

0.22 0.24 0.26 0.28 0.30

Pressure at t = 0.16

Pressure at t = 0.16

2.70

3.5

2.65

3.0

2.5

2.60

p

p

2.0

2.55

1.5

2.50

1.0

2.45

0.5

0.0 0.2 0.4 0.6 0.8 1.0

0.22 0.24 0.26 0.28 0.30

x

x

- Fig. 11 Shock-tube Riemann problem: WENO solutions. Shown here are WENO simulations comparing two different time integrators: the third-order SSP method of Osher and Shu against the new two-stage, twoderivative method (TDRK4). We repeat that all WENO simulations with the TDRK4 time integrator use a CFL number of ν = 0.4. Here, we observe that the third-order SSP method with CFL numbers of ν = 0.4 and ν = 0.01 behaves qualitatively the same as the TDRK4 method. We plot observable quantities from top to bottom: density ρ, velocity u, and pressure p. Left columns are the full solution, and right columns are

zoomed in parts of the same data points. The resolution for this picture is the coarse solution of mx = 100 identical to the coarse solution used in Figure 9. Again, we remark that the accepted time integrator is in close agreement with the proposed method.

- 12. Dumbser, M., Munz, C.D.: Building blocks for arbitrary high order discontinuous Galerkin schemes. J. Sci. Comput. 27(1-3), 215–230 (2006)
- 13. Fehlberg, E.: Neue genauere Runge-Kutta-Formeln f¨ur Differentialgleichungen n-ter Ordnung. Z. Angew. Math. Mech. 40, 449–455 (1960)
- 14. Fehlberg, E.: New high-order Runge-Kutta formulas with step size control for systems of ﬁrst- and second-order differential equations. Z. Angew. Math. Mech. 44, T17–T29 (1964)
- 15. Friedman, A.: A new proof and generalizations of the Cauchy-Kowalewski theorem. Trans. Amer. Math. Soc. 98, 1–20 (1961)
- 16. Fusaro, B.A.: The Cauchy-Kowalewski theorem and a singular initial value problem. SIAM Rev. 10, 417–421 (1968)
- 17. Gekeler, E., Widmann, R.: On the order conditions of Runge-Kutta methods with higher derivatives. Numer. Math. 50(2), 183–203 (1986)
- 18. Goeken, D., Johnson, O.: Fifth-order Runge-Kutta with higher order derivative approximations. In: Proceedings of the 15th Annual Conference of Applied Mathematics (Edmond, OK, 1999), Electron. J. Differ. Equ. Conf., vol. 2, pp. 1–9 (electronic). Southwest Texas State Univ., San Marcos, TX (1999)
- 19. Goeken, D., Johnson, O.: Runge-Kutta with higher order derivative approximations. Appl. Numer. Math. 34(2-3), 207–218 (2000). Auckland numerical ordinary differential equations (Auckland, 1998)
- 20. Gottlieb, S.: On high order strong stability preserving Runge-Kutta and multi step time discretizations. J. Sci. Comput. 25(1-2), 105–128 (2005)


- 0.0

0.5

1.0

- 1.5

mx = 100 mx = 300

0.0 0.5 1.0 1.5 2.0 2.5

2.4

2.5

2.6

−4 −2 0 2 4

x

0

- 2


−4 −2 0 2 4

Pressure at t = 1.8

Pressure at t = 1.8

4.5

12

4.0

10

3.5

8

3.0

p

p

6

2.5

2.0

4

1.5

1.0

2.35 2.40 2.45 2.50 2.55 2.60 2.65 2.70 2.75

x

- Fig. 12 Shock-entropy: WENO solutions. Shown here are WENO solutions to the shock-entropy interaction problem presented in §5.4.2. We plot observable quantities from top to bottom: density ρ, velocity u, and pressure p. Left columns are the full solution, and right columns are zoomed in parts of the same data points. We present a coarse solution with mx = 100 points and a ﬁner solution of mx = 300 points.


- 21. Gottlieb, S., Shu, C.W.: Total variation diminishing Runge-Kutta schemes. Math. Comp. 67(221), 73–85

(1998)

- 22. Gottlieb, S., Shu, C.W., Tadmor, E.: Strong stability-preserving high-order time discretization methods. SIAM Rev. 43(1), 89–112 (electronic) (2001)
- 23. Hairer, E., Nørsett, S.P., Wanner, G.: Solving Ordinary Differential Equations II: Stiff and DifferentialAlgebraic Problems, 2nd revised edition edn. Springer, Berlin (1991)
- 24. Hairer, E., Nørsett, S.P., Wanner, G.: Solving Ordinary Differential Equations I: Nonstiff Problems (Springer Series in Computational Mathematics) (v. 1), 3rd edn. Springer (2009)
- 25. Hairer, E., Wanner, G.: Multistep-multistage-multiderivative methods of ordinary differential equations. Computing (Arch. Elektron. Rechnen) 11(3), 287–303 (1973)
- 26. Harten, A.: The artiﬁcial compression method for computation of shocks and contact discontinuities. III. Self-adjusting hybrid schemes. Math. Comp. 32(142), 363–389 (1978)
- 27. Harten, A., Engquist, B., Osher, S., Chakravarthy, S.R.: Uniformly high-order accurate essentially nonoscillatory schemes. III. J. Comput. Phys. 71(2), 231–303 (1987)
- 28. Harten, A., Lax, P.D., van Leer, B.: On upstream differencing and Godunov-type schemes for hyperbolic conservation laws. SIAM Rev. 25(1), 35–61 (1983)
- 29. Henrick, A.K., Aslam, T.D., Powers, J.M.: Mapped weighted essentially non-oscillatory schemes: Achieving optimal order near critical points. J. Comput. Phys. 207(2), 542–567 (2005)
- 30. Jiang, G.S., Shu, C.W.: Efﬁcient implementation of weighted ENO schemes. J. Comput. Phys. 126(1), 202–228 (1996)
- 31. Kastlunger, K., Wanner, G.: On Turan type implicit Runge-Kutta methods. Computing (Arch. Elektron. Rechnen) 9, 317–325 (1972). 10.1007/BF02241605
- 32. Kastlunger, K.H., Wanner, G.: Runge Kutta processes with multiple nodes. Computing (Arch. Elektron. Rechnen) 9, 9–24 (1972)


- 0.0

0.5

1.0

- 1.5

mx = 70

mx = 210

0.0 0.5 1.0 1.5 2.0 2.5

2.4

2.5

2.6

−4 −2 0 2 4

x

0

- 2


−4 −2 0 2 4

Pressure at t = 1.8

Pressure at t = 1.8

4.5

12

4.0

10

3.5

8

3.0

p

p

6

2.5

2.0

4

1.5

1.0

2.35 2.40 2.45 2.50 2.55 2.60 2.65 2.70 2.75

x

- Fig. 13 Shock entropy. Shown here are DG solutions to the shock-entropy interaction problem presented in


§5.4.2. We use a coarse mesh of mx = 70 and a ﬁner mesh of mx = 210. The reference solution is identical to the one used in Figure 12 that is a WENO simulation with 6000 points, and CFL number of ν = 0.1 with the third-order SSP-RK3 time integrator. Again, the DG schemes tend to be more diffusive on this problem when compared to the WENO method, and the limiter used in this work tends to clip the peaks for the coarse resolutions. We repeat that we are plotting exactly four points per cell, and therefore, the observable oscillations for the coarse resolution are happening on a sub-cell level. Although not shown, plots of cell averages only do not visibly demonstrate these oscillations. Results for other time integrators are found to be comparable.

- 33. Ketcheson, D.I.: Highly efﬁcient strong stability-preserving Runge-Kutta methods with low-storage implementations. SIAM J. Sci. Comput. 30(4), 2113–2136 (2008)
- 34. Ketcheson, D.I.: Runge-Kutta methods with minimum storage implementations. J. Comput. Phys. 229(5), 1763–1773 (2010)
- 35. Krivodonova, L.: Limiters for high-order discontinuous Galerkin methods. J. Comput. Phys. 226(1), 879–896 (2007)
- 36. Lax, P., Wendroff, B.: Systems of conservation laws. Comm. Pure Appl. Math. 13, 217–237 (1960)
- 37. LeVeque, R.: Finite Volume Methods for Hyperbolic Problems. Cambridge University Press (2002)
- 38. Liu, W., Cheng, J., Shu, C.W.: High order conservative Lagrangian schemes with Lax-Wendroff type time discretization for the compressible Euler equations. J. Comput. Phys. 228(23), 8872–8891 (2009)
- 39. Lu, C., Qiu, J.: Simulations of shallow water equations with ﬁnite difference Lax-Wendroff weighted essentially non-oscillatory schemes. J. Sci. Comput. 47(3), 281–302 (2011)
- 40. Mitsui, T.: Runge-Kutta type integration formulas including the evaluation of the second derivative. I. Publ. Res. Inst. Math. Sci. 18(1), 325–364 (1982)
- 41. Montecinos, G., Castro, C.E., Dumbser, M., Toro, E.F.: Comparison of solvers for the generalized Riemann problem for hyperbolic systems with source terms. J. Comput. Phys. 231(19), 6472–6494 (2012)
- 42. Nguyen-Ba, T., Boˇzi´c, V., Kengne, E., Vaillancourt, R.: Nine-stage multi-derivative Runge-Kutta method of order 12. Publ. Inst. Math. (Beograd) (N.S.) 86(100), 75–96 (2009)


- 43. Niegemann, J., Diehl, R., Busch, K.: Efﬁcient low-storage Runge-Kutta schemes with optimized stability regions. J. Comput. Phys. 231(2), 364–372 (2012)
- 44. Obreschkoff, N.: Neue Quadraturformeln. Abh. Preuss. Akad. Wiss. Math.-Nat. Kl. 1940(4), 20 (1940)
- 45. Ono, H., Yoshida, T.: Two-stage explicit Runge-Kutta type methods using derivatives. Japan J. Indust. Appl. Math. 21(3), 361–374 (2004)
- 46. Qiu, J.: A numerical comparison of the Lax-Wendroff discontinuous Galerkin method based on different numerical ﬂuxes. J. Sci. Comput. 30(3), 345–367 (2007)
- 47. Qiu, J.: WENO schemes with Lax-Wendroff type time discretizations for Hamilton-Jacobi equations. J. Comput. Appl. Math. 200(2), 591–605 (2007)
- 48. Qiu, J., Dumbser, M., Shu, C.W.: The discontinuous Galerkin method with Lax-Wendroff type time discretizations. Comput. Methods Appl. Mech. Eng. 194(42-44), 4528–4543 (2005)
- 49. Qiu, J., Shu, C.W.: Finite difference WENO schemes with Lax-Wendroff-type time discretizations. SIAM J. Sci. Comput. 24(6), 2185–2198 (2003)
- 50. Reed, W., Hill, T.: Triangular mesh methods for the neutron transport equation. Tech. Rep. LA-UR-73479, Los Alamos Scientiﬁc Laboratory (1973)
- 51. Roe, P.L.: Approximate Riemann solvers, parameter vectors, and difference schemes. J. Comput. Phys. 43(2), 357–372 (1981)
- 52. Rossmanith, J.: DOGPACK software (2013). Available from http://www.dogpack-code.org
- 53. Rossmanith, J.A., Seal, D.C.: A positivity-preserving high-order semi-Lagrangian discontinuous Galerkin scheme for the Vlasov-Poisson equations. J. Comput. Phys. 230(16), 6203–6232 (2011)
- 54. Rusanov, V.V.: The calculation of the interaction of non-stationary shock waves with barriers. Z.ˇ Vyˇcisl. Mat. i Mat. Fiz. 1, 267–279 (1961)
- 55. Seal, D.C.: Discontinuous Galerkin methods for Vlasov models of plasma. Ph.D. thesis, Madison, WI, University of Wisconsin, Madison, WI (2012)
- 56. Shintani, H.: On one-step methods utilizing the second derivative. Hiroshima Math. J. 1, 349–372 (1971)
- 57. Shintani, H.: On explicit one-step methods utilizing the second derivative. Hiroshima Math. J. 2, 353– 368 (1972)
- 58. Shu, C.W.: Essentially non-oscillatory and weighted essentially non-oscillatory schemes for hyperbolic conservation laws. In: Advanced numerical approximation of nonlinear hyperbolic equations (Cetraro, 1997), Lecture Notes in Math., vol. 1697, pp. 325–432. Springer, Berlin (1998)
- 59. Shu, C.W.: High-order ﬁnite difference and ﬁnite volume WENO schemes and discontinuous Galerkin methods for CFD. Int. J. Comput. Fluid Dyn. 17(2), 107–118 (2003)
- 60. Shu, C.W.: High order weighted essentially nonoscillatory schemes for convection dominated problems. SIAM Rev. 51(1), 82–126 (2009)
- 61. Shu, C.W., Osher, S.: Efﬁcient implementation of essentially nonoscillatory shock-capturing schemes. J. Comput. Phys. 77(2), 439–471 (1988)
- 62. Shu, C.W., Osher, S.: Efﬁcient implementation of essentially nonoscillatory shock-capturing schemes. II. J. Comput. Phys. 83(1), 32–78 (1989)
- 63. Stancu, D.D., Stroud, A.H.: Quadrature formulas with simple Gaussian nodes and multiple ﬁxed nodes. Math. Comp. 17, 384–394 (1963)
- 64. Taube, A., Dumbser, M., Balsara, D.S., Munz, C.D.: Arbitrary high-order discontinuous Galerkin schemes for the magnetohydrodynamic equations. J. Sci. Comput. 30(3), 441–464 (2007)
- 65. Titarev, V.A., Toro, E.F.: ADER: arbitrary high order Godunov approach. In: Proceedings of the Fifth International Conference on Spectral and High Order Methods (ICOSAHOM-01) (Uppsala), vol. 17, pp. 609–618 (2002)
- 66. Titarev, V.A., Toro, E.F.: ADER schemes for three-dimensional non-linear hyperbolic systems. J. Comput. Phys. 204(2), 715–736 (2005)
- 67. Toro, E.F.: Riemann Solvers and Numerical Methods for Fluid Dynamics: A Practical Introduction, 2nd edn. Springer, Berlin (1999)
- 68. Toro, E.F., Titarev, V.A.: Solution of the generalized Riemann problem for advection-reaction equations. R. Soc. Lond. Proc. Ser. A Math. Phys. Eng. Sci. 458(2018), 271–281 (2002)
- 69. Toro, E.F., Titarev, V.A.: ADER schemes for scalar non-linear hyperbolic conservation laws with source terms in three-space dimensions. J. Comput. Phys. 202(1), 196–215 (2005)
- 70. Toro, E.F., Titarev, V.A.: TVD ﬂuxes for the high-order ADER schemes. J. Sci. Comput. 24(3), 285–309

(2005)

- 71. Tur´an, P.: On the theory of the mechanical quadrature. Acta Sci. Math. Szeged 12(Leopoldo Fejer et Frederico Riesz LXX annos natis dedicatus, Pars A), 30–37 (1950)
- 72. Williamson, J.H.: Low-storage Runge-Kutta schemes. J. Comput. Phys. 35(1), 48–56 (1980)
- 73. Yoshida, T., Ono, H.: Two stage explicit Runge-Kutta type method using second and third derivatives. IPSJ J. 44(1), 82–87 (2003)
- 74. Zurm¨uhl, R.: Runge-Kutta-Verfahren unter Verwendung h¨oherer Ableitungen. Z. Angew. Math. Mech. 32, 153–154 (1952)


