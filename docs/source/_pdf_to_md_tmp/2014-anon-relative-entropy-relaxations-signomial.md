arXiv:1409.7640v1[math.OC]26Sep2014

Relative Entropy Relaxations for Signomial Optimization

Venkat Chandrasekaranc and Parikshit Shahw ∗

c Departments of Computing and Mathematical Sciences and of Electrical Engineering California Institute of Technology Pasadena, CA 91125

w Wisconsin Institutes for Discovery University of Wisconsin Madison, WI 53715 September 25, 2014

Abstract

Signomial programs (SPs) are optimization problems speciﬁed in terms of signomials, which are weighted sums of exponentials composed with linear functionals of a decision variable. SPs are non-convex optimization problems in general, and families of NP-hard problems can be reduced to SPs. In this paper we describe a hierarchy of convex relaxations to obtain successively tighter lower bounds of the optimal value of SPs. This sequence of lower bounds is computed by solving increasingly larger-sized relative entropy optimization problems, which are convex programs speciﬁed in terms of linear and relative entropy functions. Our approach relies crucially on the observation that the relative entropy function – by virtue of its joint convexity with respect to both arguments – provides a convex parametrization of certain sets of globally nonnegative signomials with eﬃciently computable nonnegativity certiﬁcates via the arithmetic-geometricmean inequality. By appealing to representation theorems from real algebraic geometry, we show that our sequences of lower bounds converge to the global optima for broad classes of SPs. Finally, we also demonstrate the eﬀectiveness of our methods via numerical experiments.

Keywords: arithmetic-geometric-mean inequality; convex optimization; geometric programming; global optimization; real algebraic geometry.

# 1 Introduction

A signomial is a weighted sum of exponentials composed with linear functionals of a variable x ∈ Rn:

ℓ

cj exp α(j)′x (1)

f(x) =

j=1

Here cj ∈ R and α(j) ∈ Rn are ﬁxed parameters.1 A signomial program (SP) is an optimization problem in which a signomial is minimized subject to constraints on signomials, all in a decision

![image 1](<2014-anon-relative-entropy-relaxations-signomial_images/imageFile1.png>)

∗Email: venkatc@caltech.edu, pshah@discovery.wisc.edu

1In the literature [9], signomials are typically parametrized somewhat diﬀerently as weighted sums of generalized “monomials.” A monomial consists of a product of variables, each raised to an arbitrary real power, and the variables only take on positive values. It is straightforward to transform such functions to sums of exponentials of the type (1) discussed in this paper; see [2, 9].

1

variable x [8, 9]. SPs are non-convex in general, and they include NP-hard problems as special cases [4]. Consequently, we do not expect to obtain globally optimal solutions of general SPs in a computationally tractable manner. This paper describes a hierarchy of convex relaxations based on relative entropy optimization for obtaining lower bounds of the optimal value of an SP.

Geometric programs (GPs) constitute a prominent subclass of SPs in which a posynomial – a signomial with positive coeﬃcients, i.e., the cj’s are all positive – is minimized subject to upperbound constraints on posynomials [2, 9]. GPs are convex optimization problems that can be solved eﬃciently, and they have been successfully employed in a wide range of applications such as power control in communication systems [4], circuit design [1], approximations to the matrix permanent [14], and the computation of capacities of point-to-point communication channels [5]. However, the additional ﬂexibility provided by SPs via constraints on arbitrary signomials rather than just posynomials is useful in a range of problems to which GPs are not directly applicable. Examples include resource allocation in networks [4], control problems involving chemical processes (see the extensive reference list in [15]), spatial frame design [29], and certain nonlinear ﬂow problems in graphs [19].

## 1.1 Our Contributions

Central to the development in this paper is a view of global minimization that is grounded in duality: globally minimizing a signomial is computationally equivalent to the problem of certifying global nonnegativity of a signomial. Although certifying global nonnegativity of a general signomial is a computationally intractable problem, one can appeal to GP duality [9] to show that certifying nonnegativity of a signomial with all but one coeﬃcient being positive can be accomplished in a computationally tractable manner. These observations suggest a natural suﬃcient condition for certifying nonnegativity of general signomials via certiﬁcates that can be computed eﬃciently. Speciﬁcally, if a signomial f(x) can be decomposed as f(x) = ki=1 fi(x), where each fi(x) is a globally nonnegative signomial with at most one negative coeﬃcient, then f(x) is clearly nonnegative. We refer to a decomposition of this form as a sum-of-AM/GM-exponentials (SAGE) decomposition, and to the associated functions f(x) that are decomposable in this manner as SAGE functions. The reason for this terminology is that certifying global nonnegativity of each of the functions fi(x) is accomplished by verifying an appropriate arithmetic-geometric-mean (AM/GM) inequality as described in Section 2.1.

The key insight underlying our approach in Section 2 is that computing a SAGE decomposition of f(x) can be cast as a feasibility problem involving a system of linear inequalities as well as inequalities specifying upper bounds on relative entropy functions. Recall that the relative entropy function is deﬁned as follows for ν,λ in the nonnegative orthant Rℓ+:

ℓ

νj log

D(ν,λ) =

j=1

νj λj

![image 2](<2014-anon-relative-entropy-relaxations-signomial_images/imageFile2.png>)

. (2)

This function is jointly convex in both arguments [3, p.90], and the associated feasibility problem of ﬁnding a SAGE decomposition can be solved eﬃciently via convex optimization. As discussed in Section 3.1, this method can be employed to obtain lower bounds on the original signomial f(x) by solving a tractable convex program involving linear as well as relative entropy functions.

In Section 3 we also describe a principled framework to obtain a family of increasingly tighter lower bounds for general (constrained and unconstrained) SPs. This family of bounds is obtained by solving hierarchies of successively larger convex programs based on relative entropy optimization; these hierarchies are derived by considering a sequence of tighter nonnegativity certiﬁcates for

a signomial over a set deﬁned by signomial constraints. A prominent example of hierarchies of tractable convex programs being employed for intractable problems is in the setting of polynomial optimization problems, for which SDP relaxations have been developed based on sum-of-squares techniques [13, 17, 18]. However, those methods are not directly relevant to SPs for several reasons, and we highlight these distinctions in Section 4.2.

The hierarchy of convex relaxations that we describe in Section 3 has several notable features. First, GPs are solved exactly by the ﬁrst level in this hierarchy; thus, our hierarchy has the desirable property that “easy problem instances remain easy.” Second, the family of lower bounds is invariant under a natural transformation of the problem data. Speciﬁcally, the optimal value of an SP remains unchanged under the application of a non-singular linear transformation simultaneously to all the parameters α(j) that appear in the exponents of the signomials in an SP (both in the objective and in the constraints). The hierarchy of relative entropy relaxations described in Section 3 leads to bounds that are invariant under such transformations. Third, it is desirable that any procedure for obtaining lower bounds of the optimal value of an SP be robust to small perturbations of the exponents α(j) in an SP. As discussed in Section 4.2, this is also a feature of our proposed approach. Fourth, for broad families of SPs our approach leads to a convergent sequence of lower bounds, i.e., our hierarchy approximates the optimal value of the SP arbitrarily well from below (see Theorems 15 and 16). Such a property of a hierarchy is usually referred to as completeness. At various stages in the paper we discuss numerical experiments that illustrate the eﬀectiveness of our methods.

Related work Several researchers have developed strategies for optimizing SPs based on variants of branch-and-bound methods [15] as well as heuristic techniques based on successive approximations that can be solved via linear or geometric programming [2, 4, 25, 26]. The framework presented in this paper is qualitatively diﬀerent as it is based on solving convex optimization problems involving linear and relative entropy functions to obtain guaranteed bounds on the optimal value of SPs. Our approach is founded on the insight that the joint convexity of the relative entropy function leads to an eﬀective convex parametrization of certain families of globally nonnegative signomials.

## 1.2 Paper Outline

Section 2 describes the SAGE decomposition for certifying nonnegativity of a signomial based on relative entropy optimization and its connection to the AM/GM inequality. This approach underlies the subsequent development in Section 3 in which a hierarchy of relative entropy relaxations is proposed for general SPs. In Section 4, we provide theoretical support for our hierarchies of relative entropy relaxations by proving that they provide a sequence of lower bounds that converges to the global minimum for a broad class of SPs. Throughout the paper, we describe numerical experiments in which relative entropy optimization techniques are employed to obtain bounds on some stylized SPs. These results were obtained using a basic interior-point solver written in MATLAB by following the discussions in [3]. We conclude with a discussion of potential future directions in Section 5. We prove Theorems 15 and 16 in the Appendix.

Notation In ℓ-dimensional space we denote the nonnegative orthant by Rℓ+, the positive orthant by Rℓ++, rational vectors by Qℓ, and nonnegative rational vectors by Qℓ+. We denote the nonnegative integers by Z+ and the positive integers by Z++. Given a vector w ∈ Rℓ, we denote the vector formed by removing the i’th coordinate from w by w\i ∈ Rℓ−1. By convention, we assume that 0log λ0 = 0 for any λ ∈ R+, and that ν log ν0 equals 0 if ν = 0 and ∞ if ν > 0. Given a collection

![image 3](<2014-anon-relative-entropy-relaxations-signomial_images/imageFile3.png>)

![image 4](<2014-anon-relative-entropy-relaxations-signomial_images/imageFile4.png>)

of vectors {α(j)}ℓj=1 ⊂ Rn, we deﬁne the set Ep({α(j)}ℓj=1) ⊂ Rn for p ∈ Z+ as follows:

λj ≤ p, λj ∈ Z+  

Ep({α(j)}ℓj=1) =   

ℓ

ℓ

λjα(j) |

.

j=1

j=1

# 2 SAGE Decomposition and Relative Entropy Optimization

In this section we describe a suﬃcient condition to certify global nonnegativity of a signomial f by decomposing it into a sum of terms f = i fi, where each fi has an eﬃciently computed nonnegativity certiﬁcate based on relative entropy optimization. This method serves as the basic building block in the next section on hierarchies of relative entropy relaxations for general SPs.

## 2.1 Signomials with One Negative Term and the AM/GM Inequality

The main observation underlying our methods is that certifying the nonnegativity of a signomial with at most one negative coeﬃcient can be accomplished eﬃciently.

- Deﬁnition 1. A globally nonnegative signomial with at most one negative coeﬃcient is called an AM/GM-exponential.


The reason for this terminology is that certifying the nonnegativity of an AM/GM-exponential

g(x) = β exp{α′x} + ℓj=1 cj exp{[Q′x]j} – here, c ∈ Rℓ+, β ∈ R, Q ∈ Rn×ℓ, and α ∈ Rn – is essentially equivalent to verifying an AM/GM inequality. To see this connection, suppose there

exists a ν ∈ Rℓ satisfying the following conditions: D(ν,ec) − β ≤ 0, ν ∈ Rℓ+, Qν = (1′ν)α. (3)

A ν ∈ Rℓ+\0 satisfying these conditions explicitly certiﬁes the nonnegativity of g(x) via the following two sequences of inequalities.2 First, we have that:

ℓ

cj exp{[Q′x]j}

j=1

(i)

≥

ℓ

j=1

cj exp{[Q′x]j} νj/(1′ν)

![image 5](<2014-anon-relative-entropy-relaxations-signomial_images/imageFile5.png>)

νj 1′ν (=ii)

ℓ

![image 6](<2014-anon-relative-entropy-relaxations-signomial_images/imageFile6.png>)

j=1

cj νj/(1′ν)

![image 7](<2014-anon-relative-entropy-relaxations-signomial_images/imageFile7.png>)

νj 1′ν

![image 8](<2014-anon-relative-entropy-relaxations-signomial_images/imageFile8.png>)

exp{α′x}.

Here inequality (i) is a consequence of the AM/GM inequality applied with weights 1ν′ν, and equation (ii) follows from (3). Next, we observe that:

![image 9](<2014-anon-relative-entropy-relaxations-signomial_images/imageFile9.png>)

ℓ

j=1

cj νj/(1′ν)

![image 10](<2014-anon-relative-entropy-relaxations-signomial_images/imageFile10.png>)

νj 1′ν (iii=) exp −D(1ν′ν,c)

![image 11](<2014-anon-relative-entropy-relaxations-signomial_images/imageFile11.png>)

![image 12](<2014-anon-relative-entropy-relaxations-signomial_images/imageFile12.png>)

(iv)

≥ −ξ[D(1ν′ν,c) + log(ξ) − 1], ∀ξ ∈ R+

![image 13](<2014-anon-relative-entropy-relaxations-signomial_images/imageFile13.png>)

(=v) −ξD(1ν′ν , ξec), ∀ξ ∈ R+ (=vi) −D(1ξ′νν ,ec), ∀ξ ∈ R+ (vii)

![image 14](<2014-anon-relative-entropy-relaxations-signomial_images/imageFile14.png>)

![image 15](<2014-anon-relative-entropy-relaxations-signomial_images/imageFile15.png>)

![image 16](<2014-anon-relative-entropy-relaxations-signomial_images/imageFile16.png>)

(viii)

≥ −β exp{α′x}.

≥ −D(ν,ec)

Here equation (iii) follows from the deﬁnition of the relative entropy function (2), inequality (iv) follows from the observation that the exponential function is the convex conjugate of the negative entropy function — i.e., exp{−ρ} = supξ∈R+ −ξ[ρ + log(ξ) − 1] — equations (v),(vi) follow from the properties of the relative entropy function (2) (in particular, by noting that this function is

![image 17](<2014-anon-relative-entropy-relaxations-signomial_images/imageFile17.png>)

2The conditions (3) being satisﬁed with ν = 0 corresponds to the situation that β ≥ 0.

positively homogenous), inequality (vii) follows by setting ξ = 1′ν, and ﬁnally inequality (viii) follows from (3). Hence the existence of ν ∈ Rℓ satisfying (3) certiﬁes the nonnegativity of the signomial g(x). The preceding discussion parallels some of the early expositions on GP duality based on the AM/GM inequality [9], although our formulation (3) is parametrized diﬀerently compared to the following formulation in the GP literature [4, 9]:

D(ν,c) + log(−β) ≤ 0, ν ∈ Rℓ+,1′ν = 1, Qν = α. (4)

In comparison to (3), the parametrization (4) is not jointly convex in (ν,c,β). As discussed after Lemma 2, the joint convexity of the inequality D(ν,ec) − β ≤ 0 in (3) with respect to (ν,c,β) plays a crucial role in our subsequent development.

Example 1. Consider the function g(x) = exp{x1} + exp{x2} − exp{(21 + ǫ)x1 + (21 − ǫ)x2} for a ﬁxed ǫ ∈ [−12, 12]. It is easily seen that ν = (12 + ǫ, 21 − ǫ)′ satisﬁes the conditions (3):

![image 18](<2014-anon-relative-entropy-relaxations-signomial_images/imageFile18.png>)

![image 19](<2014-anon-relative-entropy-relaxations-signomial_images/imageFile19.png>)

![image 20](<2014-anon-relative-entropy-relaxations-signomial_images/imageFile20.png>)

![image 21](<2014-anon-relative-entropy-relaxations-signomial_images/imageFile21.png>)

![image 22](<2014-anon-relative-entropy-relaxations-signomial_images/imageFile22.png>)

![image 23](<2014-anon-relative-entropy-relaxations-signomial_images/imageFile23.png>)

D((21 + ǫ, 21 − ǫ)′,e1) − (−1) = D((12 + ǫ, 12 − ǫ)′,1) ≤ 0 I2×2 ν = (12 + ǫ, 21 − ǫ)′

![image 24](<2014-anon-relative-entropy-relaxations-signomial_images/imageFile24.png>)

![image 25](<2014-anon-relative-entropy-relaxations-signomial_images/imageFile25.png>)

![image 26](<2014-anon-relative-entropy-relaxations-signomial_images/imageFile26.png>)

![image 27](<2014-anon-relative-entropy-relaxations-signomial_images/imageFile27.png>)

![image 28](<2014-anon-relative-entropy-relaxations-signomial_images/imageFile28.png>)

![image 29](<2014-anon-relative-entropy-relaxations-signomial_images/imageFile29.png>)

Here I2×2 is the 2 × 2 identity matrix and the ﬁrst inequality follows from the fact that D((21 + ǫ, 12 − ǫ)′,1) is the negative entropy of a probability vector, which is always nonpositive [6, p.15]. Consequently, ν certiﬁes the nonnegativity of g(x).

![image 30](<2014-anon-relative-entropy-relaxations-signomial_images/imageFile30.png>)

![image 31](<2014-anon-relative-entropy-relaxations-signomial_images/imageFile31.png>)

Next, we show the converse result: if g is an AM/GM-exponential, then there exists a certiﬁcate ν satisfying (3). This follows as a consequence of strong duality applied to a suitable convex program.

Lemma 2. Let g(x) = β exp{α′x} + ℓj=1 cj exp{[Q′x]j}, where c ∈ Rℓ+, β ∈ R, Q ∈ Rn×ℓ, and α ∈ Rn. If g(x) ≥ 0 for all x ∈ Rn then there exists ν ∈ Rℓ satisfying the conditions (3).

Proof. The signomial g(x) being globally nonnegative is equivalent to the signomial g(x)exp{−α′x} being globally nonnegative, which in turn is equivalent to ℓj=1 cj exp{[Q′x]j − α′x} ≥ −β for all x ∈ Rn. To certify a lower bound on the convex function ℓj=1 cj exp{[Q′x]j − α′x}, consider the following convex program:

c′t s.t. exp [Q′x]j − α′x ≤ tj, j = 1,... ,ℓ.

inf

x∈Rn, t∈Rℓ

This primal problem satisﬁes Slater’s conditions [23], and its Lagrangian dual is: sup

−D(ν,ec) s.t. ν ∈ Rℓ+, Qν = (1′ν)α.

ν∈Rℓ

The result follows as strong duality holds and the dual optimum is attained.

![image 32](<2014-anon-relative-entropy-relaxations-signomial_images/imageFile32.png>)

![image 33](<2014-anon-relative-entropy-relaxations-signomial_images/imageFile33.png>)

![image 34](<2014-anon-relative-entropy-relaxations-signomial_images/imageFile34.png>)

![image 35](<2014-anon-relative-entropy-relaxations-signomial_images/imageFile35.png>)

In describing these results, we have implicitly viewed c ∈ Rℓ+,β ∈ R as ﬁxed coeﬃcients. However, the conditions (3) are convex with respect to c,β by virtue of the joint convexity of the relative entropy function. Consequently, the set of AM/GM-exponentials with respect to a collection of exponents can be eﬃciently parametrized as a convex set given by linear and relative

3 2.5 2 1.5 1 0.5 0

![image 36](<2014-anon-relative-entropy-relaxations-signomial_images/imageFile36.png>)

b

0 0.5 1 1.5 2 2.5 3

a

Figure 1: The locations in white denote those values of (a,b) ∈ R2+ for which the signomial fa,b(x1,x2) = exp{x1} + exp{x2} − aexp{δx1 + (1 − δ)x2} − bexp{(1 − δ)x1 + δx2} with δ = π/4 is a SAGE function. The intercept is around 1.682.

entropy inequalities: CAGE α(1),... ,α(ℓ);α(0)

= (c,β) ∈ Rℓ+ × R | g(x) = β exp{α(0)′x} +

ℓ

cj exp{α(j)′x},

j=1

g(x) an AM/GM-exponential

= (c,β) ∈ Rℓ+ × R | ∃ν ∈ Rℓ+ s.t. D(ν,ec) ≤ β,

ℓ

α(j)νj = (1′ν)α(0) . (5)

j=1

Based on this representation, one can see that the set CAGE α(1),... ,α(ℓ);α(0) is a convex cone. This parametrization plays a crucial role in the next subsection and beyond as we describe computationally eﬃcient methods based on relative entropy optimization (jointly over both arguments) to obtain bounds for SPs.

## 2.2 SAGE Decomposition of a General Signomial

If a signomial consists of more than one negative term, a natural suﬃcient condition for certifying nonnegativity is to express the signomial as a sum of AM/GM-exponentials:

- Deﬁnition 2. Given a ﬁnite collection of vectors M ⊂ Rn, the set of sum-of-AM/GM-exponentials with respect to M is deﬁned as:


SAGE(M) = f | f =

m

fi, fi an AM/GM-exponential with exponents in M .

i=1

A signomial f ∈ SAGE(M) is called a SAGE function with respect to M, and a decomposition of f as a sum of AM/GM-exponentials is called a SAGE decomposition.

As each term in a SAGE decomposition is globally nonnegative, it is easily seen that SAGE functions are globally nonnegative signomials.

- Example 3. Consider a signomial f(x) = i pi(x)gi(x), where each pi(x) is a posynomial and each gi(x) is an AM/GM-exponential. If each pi(x),gi(x) is deﬁned with respect to exponents {α(j)}ℓj=1, one can check that f is a SAGE function with respect to exponents E2({α(j)}ℓj=1).
- Example 4. As another example, consider the parametrized family of signomials fa,b(x1,x2) = exp{x1} + exp{x2} − aexp{δx1 + (1 − δ)x2} − bexp{(1 − δ)x1 + δx2}, where we set δ = π/4.


Figure 1 shows a plot of the values of (a,b) ∈ R2+ for which fa,b(x1,x2) is a SAGE function with respect to the exponents {(1,0)′,(0,1)′,(δ,1 − δ)′,(1 − δ,δ)′}.

Although SAGE functions are globally nonnegative, not all nonnegative signomials are decomposable as SAGE functions. The following simple example illustrates the point that SAGE decomposability is only a suﬃcient condition for nonnegativity:

- Example 5. Consider f(x1,x2,x3) = exp{2x1}+exp{2x2}+exp{2x3}−2exp{x1+x2}−2exp{x1+ x3} + 2exp{x2 + x3}. This function is not a SAGE function with respect to the six exponents in the expression. One can check that f(x1,x2,x3) = (exp{x1}−exp{x2}−exp{x3})2, which demonstrates its nonnegativity. In Section 4.2, we contrast sum-of-squares methods from the polynomial optimization literature [13, 17, 18] with the methods developed in this paper, highlighting the beneﬁts of convex relaxations based on SAGE decompositions for SPs.


For M = {α(j)}ℓj=1, we have that:

SAGE {α(j)}ℓj=1 = f | f(x) =

fi(x) =

ℓ

fi(x), each fi(x) ≥ 0 for all x ∈ Rn

i=1

ℓ

c˜(ji) exp α(j)′x with c˜(\ii) ∈ R+ℓ−1 .

j=1

(6)

In order to obtain an eﬃcient description of SAGE {α(j)}ℓj=1 we consider the following set of coeﬃcients (analogous to CAGE α(1),... ,α(ℓ);α(0) in (5)):

CSAGE α(1),... ,α(ℓ) = c ∈ Rℓ |

ℓ

cj exp{α(j)′x} ∈ SAGE {α(j)}ℓj=1 . (7)

j=1

The next proposition summarizes the relevant properties of SAGE functions by giving an explicit representation of the set CSAGE α(1),... ,α(ℓ) .

Proposition 6. Fix a collection of exponents {α(j)}ℓj=1 ⊂ Rn. Then we have: CSAGE α(1),... ,α(ℓ)

ℓ

c(j),

= c ∈ Rℓ | ∃c(j) ∈ Rℓ, j = 1,... ,ℓ s.t. c =

j=1

c(\jj) c(jj)

∈ CAGE α(1),... ,α(j−1),α(j+1),... ,α(ℓ);α(j)

ℓ

c(j)

= c ∈ Rℓ | ∃c(j) ∈ Rℓ,ν(j) ∈ Rℓ, j = 1,... ,ℓ s.t. c =

j=1

ℓ

α(i)ν(ij) = 0, ν(jj) = −1′ν(\jj), j = 1,... ,ℓ

i=1

D ν(\jj),ec(\jj) − c(jj) ≤ 0, ν(\jj) ∈ Rℓ−1, j = 1,... ,ℓ . (8) The set CSAGE α(1),... ,α(ℓ) is a convex cone, and its dual is given by:

CSAGE⋆ α(1),... ,α(ℓ) = v ∈ Rℓ+ | ∃τ(j) ∈ Rn, j = 1,... ,ℓ s.t. vi log

′

vi vj

≤ α(i) − α(j)

τ(i), ∀i,j .

![image 37](<2014-anon-relative-entropy-relaxations-signomial_images/imageFile37.png>)

(9)

Proof. For a coeﬃcient vector c ∈ Rℓ to belong to CSAGE α(1),... ,α(ℓ) , we have from (7) that f(x) = ℓj=1 cj exp α(j)′x must be a SAGE function with respect to the exponents {α(j)}ℓj=1. The description of CSAGE α(1),... ,α(ℓ) in (8) then follows directly from Lemma 2 and from (6).

It is also clear that CSAGE α(1),... ,α(ℓ) is a convex cone, because it can be viewed as the

projection of a convex cone from (8). Speciﬁcally, the inequality D ν(\jj),ec(\jj) − c(jj) ≤ 0 deﬁnes a convex cone because the relative entropy function is positively homogenous and convex jointly in both arguments, and all the other constraints deﬁne convex cones in the variables c,c(j),ν(j).

Finally, the description of the dual cone CSAGE⋆ α(1),... ,α(ℓ) follows from a straightforward calculation based on the observation that CSAGE α(1),... ,α(ℓ) is a sum of convex cones CAGE α(1),... ,α(j−1),α(j+1),... ,α(ℓ);α(j) corresponding to AM/GM exponentials; therefore, the dual CSAGE⋆ α(1),... ,α(ℓ) is the intersection of the duals CAGE⋆ α(1),... ,α(j−1),α(j+1),... , α(ℓ);α(j) .

![image 38](<2014-anon-relative-entropy-relaxations-signomial_images/imageFile38.png>)

![image 39](<2014-anon-relative-entropy-relaxations-signomial_images/imageFile39.png>)

![image 40](<2014-anon-relative-entropy-relaxations-signomial_images/imageFile40.png>)

![image 41](<2014-anon-relative-entropy-relaxations-signomial_images/imageFile41.png>)

Thus, the set of SAGE functions with respect to a set of exponents can be eﬃciently characterized based on this proposition. In Section 3, we employ this result to develop computationally tractable methods for obtaining lower bounds on signomials. The characterization of the cone CSAGE α(1),... ,α(ℓ) in Proposition 6 also clariﬁes an appealing invariance property of SAGE functions:

Corollary 7. Fix a collection of exponents {α(j)}ℓj=1 ⊂ Rn. For any non-singular matrix M ∈ Rn×n, we have that

CSAGE α(1),... ,α(ℓ) = CSAGE Mα(1),... ,Mα(ℓ) .

Proof. This result follows by noting that the only appearance of the exponents {α(j)}ℓj=1 in the description of CSAGE α(1),... ,α(ℓ) in (8) is in the equation ℓi=1 α(i)ν(ij) = 0. A ν(j) ∈ Rℓ satisﬁes this constraint if and only if the same ν(j) also satisﬁes ℓi=1 Mα(i)ν(ij) = 0. This concludes the proof.

![image 42](<2014-anon-relative-entropy-relaxations-signomial_images/imageFile42.png>)

![image 43](<2014-anon-relative-entropy-relaxations-signomial_images/imageFile43.png>)

![image 44](<2014-anon-relative-entropy-relaxations-signomial_images/imageFile44.png>)

![image 45](<2014-anon-relative-entropy-relaxations-signomial_images/imageFile45.png>)

Notice that the nonnegativity of a signomial is preserved under the application of a non-singular linear transformation simultaneously to all the exponents; more generally, the optimal value of an SP is unchanged under a non-singular transformation applied simultaneously to all the exponents in the objective and all the constraints. The above invariance property of CSAGE α(1),... ,α(ℓ) ensures that our lower bounds for SPs in Section 3 based on SAGE decompositions are also similarly invariant under a simultaneous linear transformation applied to all the exponents in the SP.

## 2.3 Remarks on Nonnegative Signomials

Consider a signomial f(x) = ℓj=1 cj exp{α(j)′x} with respect to exponents {α(j)}ℓj=1, and let the coeﬃcients cj be nonzero for each j = 1,... ℓ. If f(x) ≥ 0 for all x ∈ Rn, then we can make some observations about the coeﬃcients cj’s based on the structure of the set of exponents. Speciﬁcally, suppose α(1) is an extreme point of the convex hull of the exponents conv({α(j)}ℓj=1); we will denote such an exponent as an extremal exponent. Then we can conclude from the separation theorem in convex analysis [23] that there exists u ∈ Rn such that u′α(1) = 1 and u′α(j) < 1 for j = 2,... ,ℓ. Consequently, exp{γα(1)′u} dominates exp{γα(j)′u} for j = 2,... ,ℓ as γ → ∞. Based on the nonnegativity of f(x), we conclude that c1 > 0. Thus, a coeﬃcient cj must be positive if the corresponding exponent α(j) is an extremal exponent.

These observations imply that the cone of coeﬃcients of AM/GM-exponentials CAGE(α(1),... , α(ℓ);α(0)) = Rℓ++1 if α(0) ∈/ conv({α(j)}ℓj=1; this follows from the point that AM/GM-exponentials exactly correspond to nonnegative signomials with at most one negative coeﬃcient. Consequently, one can exclude such posynomials in the description of SAGE functions in (6), which also leads to simpler representations in Proposition 6. These modiﬁcations may provide computational beneﬁts if one wishes to certify nonnegativity of a signomial with the property that many of the exponents are extremal exponents.

# 3 Hierarchies of Relative Entropy Relaxations for SPs

In this section we describe hierarchies of convex relaxations to obtain lower bounds for SPs. Our development parallels the literature on convex relaxations for polynomial optimization [13, 17, 18], but with an important distinction – our approach for SPs is based on relative entropy optimization derived via SAGE decompositions, while relaxations for polynomial optimization are based on SDPs derived via sum-of-squares decompositions. Relative entropy relaxations are better suited than SDP relaxations for SPs, and we comment on these points in greater detail in Section 4.2. We also give theoretical support for our hierarchies in Section 4.1 by showing that they provide convergent sequences of lower bounds to the optimal value for broad classes of SPs. Finally, we present a dual perspective of our methods, which leads to a technique for recognizing when our lower bounds are tight and for extracting optimal solutions.

- 3.1 A Hierarchy for Unconstrained SPs Globally minimizing a signomial f(x) is equivalent to maximizing a lower bound of f(x):


f⋆ = inf

x∈Rn

f(x) = sup

γ∈R

γ s.t. f(x) − γ ≥ 0 ∀x ∈ Rn. (10)

Replacing the global nonnegativity condition on f(x)−γ by a suﬃcient condition for nonnegativity gives lower bounds on the optimal value f⋆. SAGE functions provide a natural suﬃcient condition for global nonnegativity leading to a computationally tractable approach for obtaining lower bounds, and we describe this relaxation next.

To state things concretely, ﬁx a set of exponentials {α(j)}ℓj=1 ⊂ Rn with α(1) = 0, and consider a signomial f(x) = ℓj=1 cj exp{α(j)′x} deﬁned with respect to these exponents. (If f contains no constant term, then set the corresponding coeﬃcient c1 = 0.) In order to produce a lower bound on the global minimum f⋆ of f, we consider the following convex relaxation based on SAGE decompositions:

γ s.t. f(x) − γ ∈ SAGE {α(j)}ℓj=1 . (11)

fSAGE = sup γ∈R

Based on the preceding discussion, it is clear that fSAGE ≤ f⋆. Furthermore, computing fSAGE can be reformulated as follows via Proposition 6:

fSAGE = sup γ∈R

γ s.t. (c1 − γ,c2,... ,cℓ) ∈ CSAGE(α(1),... ,α(ℓ)), (12)

where CSAGE(α(1),... ,α(ℓ)) is speciﬁed in (8). Thus, the bound fSAGE is the optimal value of a tractable convex program with linear and joint relative entropy constraints.

If f(x) is a posynomial then fSAGE = f⋆; this follows from the fact that f(x) − γ is a SAGE function if and only if f(x)−γ ≥ 0 for all x ∈ Rn because f(x)−γ has all but one coeﬃcient being

positive. Consequently, the SAGE relaxation is exact for unconstrained GPs, which is reassuring as tractable problem instances (GPs are convex optimization problems that be solved eﬃciently) can be computed eﬀectively in our framework. More generally, we illustrate the utility of SAGE relaxations for minimizing signomials with multiple negative coeﬃcients in the following examples.

Example 8. We consider signomials in three variables with seven terms of the form f(x) =

j=1 cj exp{α(j)′x} with x ∈ R3 and the following parameters ﬁxed: c1 = 0, c2 = c3 = c4 = 10, α(1) = (0,0,0)′, α(2) = (10.2,0,0)′, α(3) = (0,9.8,0)′, and α(4) = (0,0,8.2)′. The exponents α(5),α(6),α(7) ∈ R3 are chosen to be random vectors with entries distributed uniformly in [0,3], and the coeﬃcients c5,c6,c7 are chosen to be random Gaussians with mean 0 and standard deviation 10. This construction — relatively large exponents α(2),α(3),α(4) in comparison to α(5),α(6),α(7), and the corresponding positive coeﬃcients c2 = c3 = c4 = 10 — is an attempt to obtain signomials that are bounded below. An example of a signomial generated in this manner is:

7

f(x) =10 exp{10.2x1} + 10 exp{9.8x2} + 10 exp{8.2x3} − 14.6794 exp{1.5089x1 + 1.0981x2 + 1.3419x3} − 7.8601 exp{1.0857x1 + 1.9069x2 + 1.6192x3}

+ 8.7838 exp{1.0459x1 + 0.0492x2 + 1.6245x3}.

(13)

The SAGE relaxation (12) applied to f(x) gives the lower bound fSAGE ≈ −0.9747. By applying a technique presented in Section 3.4, we obtain the point x⋆ = (−0.3020,−0.2586,−0.4010)′ with

f(x⋆) ≈ −0.9747. Consequently, the lower bound fSAGE is tight in this case. As another instance of the construction described here, consider the randomly generated signomial:

f(x) =10 exp{10.2x1} + 10 exp{9.8x2} + 10 exp{8.2x3}

+ 7.5907 exp{1.9864x1 + 0.2010x2 + 1.0855x3} − 10.9888 exp{2.8242x1 + 1.9355x2 + 2.0503x3} − 13.9164 exp{0.1828x1 + 2.7772x2 + 1.9001x3}.

(14)

In this case the SAGE relaxation (12) is not tight: the SAGE lower bound is −1.426, and the technique from Section 3.4 gives the upper bound −0.739. More generally, we generated 80 random signomials according to the above description, and the SAGE relaxation was tight in 63% of the cases, while there was a gap in the remaining cases.

These examples demonstrate that there are several cases in which the lower bound fSAGE equals the global minimum f⋆. There are also situations in which the lower bound fSAGE does not equal f⋆, which is not unexpected as global minimization of signomials is in general a computationally intractable problem. Motivated by such cases, we describe next a methodology for obtaining a sequence of increasingly tighter lower bounds based on improved suﬃcient conditions for the global nonnegativity of the signomial f(x) − γ. These improved lower bounds require solution of successively larger-sized relative entropy optimization problems.

Speciﬁcally, for a set of exponents {α(j)}ℓj=1 ⊂ Rn with α(1) = 0 and a signomial f(x) =

ℓ j=1 cj exp{α(j)′x} deﬁned with respect to these exponents, we replace the SAGE condition in

(11) by a stronger suﬃcient condition for the global nonnegativity of f(x) − γ, leading to the following lower bound for each p ∈ Z+:

fSAGE(p) = sup γ∈R

γ s.t.

ℓ

exp{α(j)′x}

j=1

p

[f(x) − γ] ∈ SAGE(Ep+1({α(j)}ℓj=1)). (15)

p

The multiplier term ℓj=1 exp{α(j)′x}

is globally nonnegative for all x ∈ Rn, and consequently the constraint above is a suﬃcient condition for the global nonnegativity of f(x) − γ.

This in turn implies that fSAGE(p) ≤ f⋆ for all p ∈ Z+. One can check that the bound fSAGE of (12) is equal to fSAGE(0) in (15). Computing fSAGE(p) for each p can be recast as a relative entropy optimization problem by appealing to Proposition 6 and to the fact that the coeﬃcients of the signomial ℓj=1 exp{α(j)′x}

p

[f(x) − γ] are linear functionals of γ. For example for the

case p = 1, the signomial ˜ ℓj=1 exp{α(˜j)′x} [f(x) − γ] ∈ SAGE(E2({α(j)}ℓj=1)) is equivalent to ℓ j,˜j=1 cj,˜j exp{[α(j) + α(˜j)]′x} ∈ SAGE(E2({α(j)}ℓj=1)), with cj,˜j = c1 − γ whenever j = 1 and cj,˜j = cj otherwise; the latter SAGE condition can be reformulated using linear and relative entropy constraints on cj,˜j, and in turn on γ, via Proposition 6. The next result states that fSAGE(p) is a non-decreasing function of p; this improvement carries a computational cost as the size of the associated relative entropy program grows with p.

Lemma 9. Fix a collection of exponents {α(j)}ℓj=1 ⊂ Rn with α(1) = 0, and consider a signomial f(x) deﬁned with respect to these exponents. We have that fSAGE(p) ≤ fSAGE(p+1) for all p ∈ Z+.

Proof. For a ﬁxed value of γ, let gp(x) = ℓj=1 exp{α(j)′x}

p+1

ℓ j=1 exp{α(j)′x}

[f(x) − γ]. We observe that:

p

[f(x) − γ] and let gp+1(x) =

gp+1(x) =

ℓ

exp{α(j)′x}gp(x),

j=1

and that gp(x) ∈ SAGE(Ep+1({α(j)}ℓj=1)) implies exp{α(j)′x}gp(x) ∈ SAGE(Ep+2({α(j)}ℓj=1)). Consequently, gp(x) ∈ SAGE(Ep+1({α(j)}ℓj=1)) implies that gp+1(x) ∈ SAGE(Ep+2({α(j)}ℓj=1)) as SAGE(Ep+2({α(j)}ℓj=1)) is closed under addition. Since this implication is true for each ﬁxed γ, we have the desired result.

![image 46](<2014-anon-relative-entropy-relaxations-signomial_images/imageFile46.png>)

![image 47](<2014-anon-relative-entropy-relaxations-signomial_images/imageFile47.png>)

![image 48](<2014-anon-relative-entropy-relaxations-signomial_images/imageFile48.png>)

![image 49](<2014-anon-relative-entropy-relaxations-signomial_images/imageFile49.png>)

In Section 4.1, we prove that the sequence {fSAGE(p) } converges to f⋆ as p → ∞ for suitable families of signomials. Consequently, the methodology described in this section leads to a convergent sequence of lower bounds, computed by solving increasingly larger relative entropy optimization problems.

Example 10. Consider the signomial f(x) from (14) in Example 8. The lower bound fSAGE(0) = −1.426, and this is not tight. The next level of the hierarchy presented above leads to the improved

bound fSAGE(1) = −1.395.

## 3.2 From Unconstrained SPs to Constrained SPs: Algebraic Certiﬁcates of Compactness

Our approach to developing relaxations for constrained SPs is qualitatively diﬀerent from that in the unconstrained case. Speciﬁcally, the hierarchy of relaxations that we develop for constrained SPs in Section 3.3 does not directly specialize to the hierarchy developed for unconstrained SPs in Section 3.1. The reason for this discrepancy is that our development in the constrained setting is based on the assumption that the constraint set is a compact set. Concretely, ﬁx a collection of exponents {α(j)}ℓj=1 ⊂ Rn, and let f(x) and C = {gi(x)}mi=1 be signomials with respect to these exponents. Consider the constrained SP:

f⋆ = inf

x∈Rn

f(x) s.t. gi(x) ≥ 0, i = 1,... ,m. (16)

The hierarchy we propose in Section 3.3 is shown to be complete in Section 4.1 (see Theorem 16) under the premise that the constraint set KC = {x ∈ Rn | g(x) ≥ 0 ∀g ∈ C} is compact. Crucially, the proof of completeness relies on the assumption that the compactness of KC is explicitly enforced via inequalities of the form U ≥ exp{α(j)′x} ≥ L, j = 1,... ,ℓ (for appropriate U,L ∈ R++) in the list of constraints C = {gi(x)}mi=1. Such explicit enforcements of compactness enable us to appeal to representation theorems from real algebraic geometry that require appropriate Archimedeanity assumptions (see the survey [16]), a point that is also signiﬁcant in the development of hierarchies of SDP relaxations based on sum-of-squares decompositions for polynomial optimization problems [13, 17, 18, 21, 24].

As such a natural “unconstrained” counterpart of the constrained case is a setting in which we wish to minimize a signomial subject to a constraint set of the form {x ∈ Rn | U ≥ exp{α(j)′x} ≥ L, j = 1,... ,ℓ} for some ﬁxed U,L ∈ R++. Alternatively, if we have some additional knowledge that a global minimizer of a signomial belongs to a set of this form for some known U,L, then the methods developed in Section 3.3 provide an alternative hierarchy of convergent lower bounds to those in Section 3.1.

## 3.3 A Hierarchy for Constrained SPs

Here we describe a hierarchy of relative entropy relaxations based on SAGE decompositions for constrained SPs. In analogy with the unconstrained case, we can recast (16) as:

f⋆ = sup γ∈R

γ s.t. f(x) − γ ≥ 0 ∀x ∈ KC. (17)

As the original constrained SP is computationally intractable to solve in general, certifying nonnegativity of a signomial over a constraint set deﬁned by signomials is also intractable. In order to obtain lower bounds on f⋆ that are tractable to compute, our approach is again to proceed by employing eﬃciently computable suﬃcient conditions for certifying nonnegativity of a signomial f(x) − γ over a constraint set KC deﬁned by signomial inequalities.

A basic approach based on weak duality for bounding (17) is to replace the constraint by the following suﬃcient condition for nonnegativity:

fWD = sup

γ∈R,µ∈Rm+

γ s.t. f(x) − γ −

m

µigi(x) ≥ 0 ∀x ∈ Rn.

i=1

As the nonnegativity condition here is a suﬃcient condition for the constraint in (17), we note that fWD ≤ f⋆; this is the standard argument underlying weak duality. However, there are two diﬃculties with this approach. The ﬁrst is that the constraint still involves the computationally intractable problem of checking nonnegativity of an arbitrary signomial. The second diﬃculty, independent of the ﬁrst one, is that the underlying SP is nonconvex, and therefore we do not expect strong duality to hold; as such, even if one could compute fWD it is in general the case that fWD < f⋆. To remedy the ﬁrst diﬃculty, we replace the nonnegativity condition by one based on SAGE decomposability. To address the second challenge we add valid inequalities that are consequences of the original set of constraints; although this idea of adding appropriate redundant constraints is an old one, it has been employed to particularly powerful eﬀect in polynomial optimization problems [13, 17, 18].

Formally, consider the set of signomials deﬁned as products of the original set of constraint functions C = {gi(x)}mi=1 in (17):

q

Rq(C) =

hk | hk ∈ {1} ∪ C . (18)

k=1

Here 1 represents the signomial that is identically equal to one for all x ∈ Rn. Based on this deﬁnition, we consider the following relaxation of (17):

fSAGE(p,q) = sup

γ∈R, sh(x)∈SAGE(Ep({α(j)}ℓj=1))

γ

s.t. f(x) − γ −

sh(x)h(x)

h(x)∈Rq(C)

∈ SAGE(Ep+q({α(j)}ℓj=1)).

(19)

For a ﬁxed q, the number of terms in the set Rq(C) is at most (ℓ + 1)q, and consequently the sum consists of a ﬁnite number of terms. Moreover, computing fSAGE(p,q) can be recast as a relative entropy optimization problem via Proposition 6 as the coeﬃcients of the signomial f(x) − γ −

h∈Rq(C) sh(x)h(x) are linear functionals of γ and the coeﬃcients of the SAGE functions sh(x). Note that for h ∈ Rq(C) and sh(x) ∈ SAGE(Ep), the signomial sh(x)h(x) is nonnegative on the set KC, thus corresponding to a valid constraint. Hence, for a ﬁxed value of γ and ﬁxed SAGE functions sh(x), the condition f(x)−γ − h∈R

q(C) sh(x)h(x) ∈ SAGE(Ep+q) is a suﬃcient condition for the

nonnegativity of f(x) − γ on the constraint set KC. Consequently we have that fSAGE(p,q) ≤ f⋆ for all p,q ∈ Z+.

The next result records the fact that fSAGE(p,q) provides increasingly tighter bounds as p,q grow larger. This improvement comes at the expense of solving larger relative entropy optimization problems for bigger values of p,q.

Lemma 11. Fix a set of exponents {α(j)}ℓj=1 ⊂ Rn with α(1) = 0, and let f(x) and C = {gi(x)}mi=1 be signomials with respect to these exponents. Then we have that fSAGE(p,q) ≤ f(p

′,q′)

SAGE for p ≤ p′,q ≤ q′

with p,p′,q,q′ ∈ Z+. Proof. This result follows from the observations that SAGE(Ep) ⊂ SAGE(Ep′), Rq(C) ⊂ Rq′(C), and SAGE(Ep+q) ⊂ SAGE(Ep′+q′) if p ≤ p′,q ≤ q′.

![image 50](<2014-anon-relative-entropy-relaxations-signomial_images/imageFile50.png>)

![image 51](<2014-anon-relative-entropy-relaxations-signomial_images/imageFile51.png>)

![image 52](<2014-anon-relative-entropy-relaxations-signomial_images/imageFile52.png>)

![image 53](<2014-anon-relative-entropy-relaxations-signomial_images/imageFile53.png>)

In Section 4.1 we show that for SPs with compact constraint sets, fSAGE(p,q) → f⋆ as p,q → ∞.

These results demonstrate the value in the redundant constraints employed in the bounds fSAGE(p,q) . We also note that GPs are solved exactly at the ﬁrst level of the hierarchy, i.e., the lower bound

fSAGE(0,1) equals the global minimum for GPs.

- Example 12. As our ﬁrst example, consider a constrained SP in which the objective to be minimized is the signomial (13) from Example 8, and the constraint set is convex as follows:

{x ∈ R3 | 8 exp{10.2x1} + 8 exp{9.8x2} + 8 exp{8.2x3}

+6.4 exp{1.0857x1 + 1.9069x2 + 1.6192x3} ≤ 1}.

Notice that the exponents in f(x) in (13) and ones in the constraint here are common. Although this constraint set is a convex set, this problem is not a GP because the objective function is a signomial consisting of two negative coeﬃcients. Applying the ﬁrst level of the SAGE hierarchy

described in this subsection gives the lower bound fSAGE(0,1) = −0.6147. This bound is tight and it is achieved at the feasible point x⋆ = (−0.4312,−0.3823,−0.6504)′.

- Example 13. As our next example, consider a constrained SP in which the objective to be minimized is again the signomial (13) from Example 8, and the constraint is given by following signo-


mial:

g(x) = − 8 exp{10.2x1} − 8 exp{9.8x2} − 8 exp{8.2x3}

- + 0.7410 exp{1.5089x1 + 1.0981x2 + 1.3419x3} − 0.4492 exp{1.0857x1 + 1.9069x2 + 1.6192x3}
- + 1.4240 exp{1.0459x1 + 0.0492x2 + 1.6245x3}.


(20)

This constraint was chosen in a similar manner to the signomials in Example 8. Keeping the exponents ﬁxed to the same values as those in (13), the ﬁrst three coeﬃcients are chosen to be equal to −8 and the last three are chosen to be random Gaussians with mean 0 and standard deviation 1. Thus, we wish to minimize f(x) from (13) subject to the constraint that g(x) ≥ 0. The ﬁrst level

of the hierarchy for constrained SPs gives us the lower bound fSAGE(0,1) = −0.7372. This bound is also tight and it is achieved at x⋆ = (0.0073,0.0065,0.0130)′.

## 3.4 Dual Perspectives and Extracting Optimal Solutions

The hierarchies of relaxations described in the previous subsections have an appealing dual perspective. Focussing on the unconstrained case for simplicity, the problem of minimizing a signomial f(x) = ℓj=1 cj exp{α(j)′x} with α(1) = 0 can be recast as:

f⋆ = inf

v∈Rℓ

c′v s.t. v ∈ {(1,... ,exp{α(ℓ)′x}) | x ∈ Rn}.

As the objective is linear, this problem can equivalently be expressed as a convex program by convexifying the constraint set to conv{(1,... ,exp{α(ℓ)′x}) | x ∈ Rn}. However, checking membership in conv{(1,... ,exp{α(ℓ)′x}) | x ∈ Rn} is in general an intractable problem.

The methods described in Section 3.1 can be viewed as providing a sequence of tractable outer convex approximations to the set {(1,... ,exp{α(ℓ)′x}) | x ∈ Rn}. Speciﬁcally, the dual corresponding to the SAGE lower bound fSAGE(p) (15) is:

fSAGE(p) = inf

v∈Rℓ

c′v s.t. v ∈ Wp(0,... ,α(ℓ)), (21)

where each Wp(0,... ,α(ℓ)) ⊂ Rℓ is a convex set that contains {(1,... ,exp{α(ℓ)′x}) | x ∈ Rn}. The set W0(0,... ,α(ℓ)) corresponding to fSAGE(0) (15) is:

W0(0,... ,α(ℓ)) = v ∈ Rℓ+ | v1 = 1 and v ∈ CSAGE⋆ (0,... ,α(ℓ)) , (22)

where CSAGE⋆ (0,... ,α(ℓ)) is characterized in (9). The next result shows that W0(0,... ,α(ℓ)) is an outer approximation of the set {(1,... ,exp{α(ℓ)′x}) | x ∈ Rn}:

Lemma 14. Fix a set of exponents {α(j)}ℓj=1 ⊂ Rn with α(1) = 0, and consider the convex set W0(0,... ,α(ℓ)) described in (22). Then we have that {(1,... ,exp{α(ℓ)′x}) | x ∈ Rn} ⊆

- W0(0,... ,α(ℓ)).


Proof. For each x ∈ Rn, we note that v = (1,... ,exp{α(ℓ)′x})′ ∈ W0(0,... ,α(ℓ)) by setting τ(i) = exp{α(i)′x} x in the characterization (9) of CSAGE⋆ (0,... ,α(ℓ)).

![image 54](<2014-anon-relative-entropy-relaxations-signomial_images/imageFile54.png>)

![image 55](<2014-anon-relative-entropy-relaxations-signomial_images/imageFile55.png>)

![image 56](<2014-anon-relative-entropy-relaxations-signomial_images/imageFile56.png>)

![image 57](<2014-anon-relative-entropy-relaxations-signomial_images/imageFile57.png>)

This lemma gives an alternative justiﬁcation via duality that fSAGE(0) ≤ f⋆. The higher levels of the hierarchy in Section 3.1 corresponding to the improved bounds fSAGE(p) provide tighter convex

approximations of the set {(1,... ,exp{α(ℓ)′x}) | x ∈ Rn}. For example, one can check that the set

- W1(0,... ,α(ℓ)) is given as follows:


ℓ

λ(i) = v,

W1(0,... ,α(ℓ)) = v ∈ Rℓ+ | v1 = 1 and ∃λ(i) ∈ Rℓ,i = 1,... ,ℓ, s.t.

i=1

[λ(1)′,... ,λ(ℓ)′]′ ∈ CSAGE⋆ ζ(1,1),... ,ζ(ℓ,ℓ) ,

where ζ(i,j) = α(i) + α(j) for i,j = 1,... ,ℓ. The dual perspective presented here also provides a method to check whether the lower bound

fSAGE(p) is tight, i.e., fSAGE(p) = f⋆. Focussing on the ﬁrst level of the hierarchy with p = 0, suppose an optimal solution vˆ ∈ Rℓ+ of the convex program (21) is such that there exists a corresponding point

- xˆ ∈ Rn so that vˆj = exp{α(j)′xˆ} for each j = 1,... ,ℓ. Then it follows that fSAGE(0) = f⋆ because the optimal solution vˆ belongs to the set {(1,... ,exp{α(ℓ)′x}) | x ∈ Rn}, and the point xˆ ∈ Rn is the optimal solution of the original SP (10). If vˆ ∈/ {(1,... ,exp{α(ℓ)′x}) | x ∈ Rn}, then a natural heuristic to attempt to obtain a good approximation of a minimizer of the original SP is to project log(vˆ) onto the image of the ℓ×n matrix formed by setting the rows to be the α(j)’s. Denoting this


projection by δ ∈ Rℓ, we obtain an upper bound of the optimal value of the SP (10) by computing ℓ j=1 cj exp{δj}. This is the technique employed in Example 8 to produce upper bounds.

The dual perspective in the constrained case is conceptually similar. Fix a set of exponents {α(j)}ℓj=1 ⊂ Rn with α(1) = 0, let f(x) = ℓj=1 cj(f) exp{α(j)′x} be the objective, and let C = {gi(x)}mi=1 specify the set of signomials deﬁning the constraints with gi(x) = ℓj=1 cj(gi) exp{α(j)′x}. One can recast the constrained SP (16) as:

f⋆ = inf

v∈Rℓ+

c(f)′v s.t. v ∈ {(1,... ,exp{α(ℓ)′x}) | x ∈ Rn}, c(gi)′v ≥ 0, i = 1,... ,m.

As the objective function is linear, the constraint set can be replaced by its convex hull. By considering the duals of the convex programs (19) corresponding to fSAGE(p,q) , one can again interpret SAGE relaxations as providing a sequence of computationally tractable convex outer approximations of the above constraint set:

fSAGE(p,q) = inf

v∈Rℓ

c(f)′v s.t. v ∈ Wp,q(0,... ,α(ℓ);c(g1),... ,c(gm)). (23)

That is, Wp,q(0,... ,α(ℓ);c(g1),... ,c(gm)) can be viewed as a convex outer approximation of the set {(1,... ,exp{α(ℓ)′x}) | x ∈ Rn} ∩ {v | c(gi)′v ≥ 0, i = 1,... ,m}. For example, the ﬁrst level of the hierarchy corresponding to f(0,1) is given by:

W0,1(0,... ,α(ℓ);c(g1),... ,c(gm)) = v ∈ Rℓ+ | v1 = 1, v ∈ CSAGE⋆ (0,... ,α(ℓ)), v′c(gi) ≥ 0, i = 1,... ,m .

Analogous to Lemma 14, one can show that W0,1(0,... ,α(ℓ);c(g1),... ,c(gm)) is indeed a convex outer approximation of the set {(1,... ,exp{α(ℓ)′x}) | x ∈ Rn}∩{v | c(gi)′v ≥ 0, i = 1,... ,m}. As

with the unconstrained setting, one can check whether fSAGE(p,q) = f⋆ by verifying that the optimal solution of the dual problem (23) lies in the set {(1,... ,exp{α(ℓ)′x}) | x ∈ Rn} ∩ {v | c(gi)′v ≥

- 0, i = 1,... ,m}.


# 4 Completeness of Hierarchies

In this section, we show that the hierarchies of lower bounds presented in the previous section converge to the optimal value for suitable classes of SPs. We also contrast the methods developed in this paper with those based on SDPs for polynomial optimization problems [13, 17, 18], highlighting the point that relative entropy relaxations based on SAGE decompositions are better suited to SPs than SDP relaxations based on sum-of-squares techniques.

- 4.1 Completeness of Relative Entropy Hierarchies for SPs with Rational Exponents


Our completeness results are stated for SPs in which the signomials consist of rational exponent vectors. Speciﬁcally, the high-level idea behind our proofs is as follows: We transform the SPs to appropriate polynomial optimization problems over the nonnegative orthant by suitably clearing denominators in the exponents of the SP, then apply Positivstellensatz results from real algebraic geometry to obtain representations of positive polynomials [12, 16, 28] in terms of SAGE functions (which can be viewed as nonnegative polynomials over the orthant modulo an ideal), and ﬁnally transform the results back to derive a consequence in terms of signomials. We emphasize that the transformation of an SP to a polynomial optimization problem by clearing denominators in the exponents is purely an element of our proof technique due to the appeal to representation theorems from real algebraic geometry. Our algorithmic methodology described in Section 3 does not require such clearing of denominators, and we highlight the signiﬁcance of this point in Section 4.2.

Unconstrained SPs Our transformation of SPs with rational exponents leads to polynomial optimization problems over the positive orthant intersected with an algebraic variety. However, our appeal to Positivstellensatz results from real algebraic geometry gives representations of polynomials over the nonnegative orthant intersected with an algebraic variety. Further, these representation theorems also entail certain Archimedeanity conditions as discussed in Appendix A.1. In order to overcome both these issues, we require an additional condition on the exponents as elaborated in the following result.

- Theorem 15. Let {α(j)}ℓj=1 ⊂ Qn be a collection of rational exponents with the following properties: (a) the ﬁrst n exponents {α(j)}nj=1 are linearly independent, (b) α(n+1) = 0, and (c) the


remaining exponents {α(j)}ℓj=n+2 lie in the convex hull conv({α(i)}ni=1+1), and α(j) ∈/ conv({α(i)}ni=1) for j = n + 2,... ,ℓ. Suppose f(x) is a signomial with respect to these exponents such that

- infx∈Rn f(x) > 0 and that cj > 0 for each j ∈ {1,... ,n}. Then there exists p ∈ Z+ such


p

that ℓj=1 exp{α(j)′x}

f(x) ∈ SAGE(Ep+1({α(j)}ℓj=1)).

Note The condition that cj > 0 for each j = 1,... ,n is not restrictive because nonzero coeﬃcients corresponding to extremal exponents must be positive for any globally nonnegative signomial; indeed, if any of these cj’s for j = 1,... ,n is negative then the signomial f(x) is unbounded below (see Section 2.3).

This theorem is similar in spirit to Polya-Reznick type results on rational sum-of-squares representations of positive polynomials with uniform denominators [20, 22]. Without loss of generality one can take the ﬁrst n exponent vectors {α(j)}ℓj=1 to be linearly independent to satisfy condition (a); generalizing our discussion to address the case in which there are fewer than n linearly independent vectors in {α(j)}ℓj=1 is straightforward. Further, one can also add the zero vector to the collection of exponents {α(j)}ℓj=1 to satisfy condition (b). Condition (c) is the key assumption

in this theorem as it enables us to overcome the two diﬃculties described above preceding the statement of Theorem 15 (see Appendix A.4); note that one cannot simply add vectors to the collection of exponents to satisfy this condition because each of the coeﬃcients cj for j = 1,... ,n must be nonzero. Observe also that the structure of the exponents in the signomials considered in Example 8 satisfy the conditions of Theorem 15.

To see that Theorem 15 yields completeness for unconstrained SPs, suppose f(x) is a signomial with respect to a set of exponents {α(j)}ℓj=1 satisfying the assumptions of Theorem 15, and let f⋆ denote the global minimum of f(x). For each ǫ < f⋆, the signomial f(x) − ǫ is strictly positive for all x ∈ Rn. Theorem 15 asserts that there exists a suﬃciently large pǫ ∈ Z+ such that

pǫ

ℓ j=1 exp{α(j)′x}

[f(x) − ǫ] ∈ SAGE(Epǫ+1({α(j)}ℓj=1)). Combined with the monotonicity result of Lemma 9, one can conclude that fSAGE(p) → f⋆ as p → ∞.

Constrained SPs Our next result states that the hierarchy of lower bounds fSAGE(p,q) for constrained SPs also converges to the global optimum if the constraint set is compact. Consider an SP speciﬁed

in terms of an objective signomial f(x) and constraint signomials C = {gi(x)}mi=1, all deﬁned with respect to a collection of exponents {α(j)}ℓj=1 ⊂ Rn. As discussed in Section 3.2, the compactness of the constraint set KC = {x | gi(x) ≥ 0, i = 1,... ,m} must be explicitly certiﬁed via the presence of redundant inequalities of the form U ≥ exp{α(j)′x} ≥ L, j = 1,... ,ℓ for suitable U,L ∈ R++ in the list of constraints C. If KC is a compact set, then such redundant constraints can always be added for appropriately large U and small L. (The compactness of the constraint set ensures that some of the diﬃculties in the unconstrained case – the Archimedeanity requirement and the distinction between positive versus nonnegative orthant in appealing to representation theorems – do not present obstacles in the constrained setting; speciﬁcally, we do not require additional conditions on the exponents beyond the assumption that they are rational vectors).

- Theorem 16. Fix a set of rational exponents {α(j)}ℓj=1 ⊂ Qn, and let f(x) and C = {gi(x)}mi=1 be signomials with respect to these exponents. Let Rq(C) be as deﬁned in (18), and let the constraint set be KC = {x | gi(x) ≥ 0, i = 1,... ,m}. Suppose inequalities of the form U ≥ exp{α(j)′x} ≥ L, j = 1,... ,ℓ for U,L ∈ R++ are formally speciﬁed in the list of constraints C (explicitly serving as witnesses of the compactness of KC), and suppose f(x) is strictly positive for all x ∈ KC. Then there exist p,q ∈ Z+ and SAGE functions sh(x) ∈ SAGE(Ep({α(j)}ℓj=1)) indexed by h ∈ Rq(C)


q(C) sh(x)h(x) ∈ SAGE(Ep+q({α(j)}ℓj=1)). By proceeding with a line of reasoning as in the unconstrained case, one can check that the

such that f(x) − h(x)∈R

sequence of lower bounds fSAGE(p,q) converges to the global optimum of a constrained SP with rational exponents and a compact constraint set. Note that Theorem 16 also implies that the methods

described in Section 3.3 can be employed to ﬁnd a minimizer of a signomial over a constraint set of the form {x ∈ Rn | U ≥ exp{α(j)′x} ≥ L, j = 1,... ,ℓ} for U,L ∈ R++ (or for unconstrained SPs when bounds on the location of a global minimizer are known).

Remarks The proof of Theorem 15 uses the fact that the set of posynomials forms a preprime (i.e., closed under addition and multiplication) and that posynomials are SAGE functions. The proof of Theorem 16 appeals to the property that the set of SAGE functions is closed under multiplication by posynomials (formally, that the set of SAGE functions forms a module over the preprime of posynomials). Although these results provide theoretical support for the methods proposed in Section 3, our proof techniques do not reﬂect the full strength of relative entropy relaxations. For example, one of the appealing features of relative entropy relaxations for SPs – not revealed by the

proofs of Theorems 15 and 16 – is that they are robust to small perturbations of the exponents of the underlying SP. We discuss these points in Section 4.2; see Proposition 17 and Example 18.

## 4.2 Contrast with Polynomial Optimization

A natural point of comparison with the framework presented in this paper is the literature on polynomial optimization, which involves the minimization of a multivariate polynomial subject to constraints speciﬁed by multivariate polynomials. As with SPs, polynomial optimization problems are also non-convex in general, and they include families of NP-hard problems. Parrilo [17, 18] and Lasserre [13] describe computationally feasible methods to obtain lower bounds for polynomial optimization problems. These techniques rely on nonnegativity certiﬁcates for polynomials based on sum-of-squares decompositions [12, 16, 28], and the observation by Shor [27] that checking if a polynomial is a sum-of-squares can be recast as an SDP feasibility problem.

SPs with rational exponents can be transformed to polynomial optimization problems over the nonnegative orthant by clearing denominators in the exponents. This transformation generally leads to polynomials of very large degrees, thus making sum-of-squares techniques ill-suited for general SPs. Example 1 gives a concrete illustration of this point. The signomial f(x) = exp{x1}+ exp{x2} − exp{(12 + ǫ)x1 + (21 − ǫ)x2} for a ﬁxed ǫ ∈ [−21, 12] can be eﬃciently certiﬁed as being globally nonnegative by solving a suitable relative entropy feasibility problem. Now suppose that ǫ = pq is a rational number in [−21, 21]. One can then transform the question of nonnegativity of f(x) to a problem of polynomial nonnegativity. In particular by setting z1 = exp{x1},z2 = exp{x2},z3 = exp{(21 + pq)x1 + (12 − pq)x2}, we would like to certify the nonnegativity of the polynomial f˜(z1,z2,z3) = z1+z2−z3 over the nonnegative orthant R3+ modulo the ideal generated by the polynomial z23q − z1q+2pz2q−2p. If q is large, the corresponding certiﬁcates based on sum-ofsquares methods can be of very large degree (see [13, 17, 18] for more details about constructing these certiﬁcates), which in turn require solution of large SDPs. On the other hand, there exists a short certiﬁcate for the nonnegativity of f(x) via the AM/GM inequality, which is the basic insight we exploit to develop tractable convex relaxations for SPs.

![image 58](<2014-anon-relative-entropy-relaxations-signomial_images/imageFile58.png>)

![image 59](<2014-anon-relative-entropy-relaxations-signomial_images/imageFile59.png>)

![image 60](<2014-anon-relative-entropy-relaxations-signomial_images/imageFile60.png>)

![image 61](<2014-anon-relative-entropy-relaxations-signomial_images/imageFile61.png>)

![image 62](<2014-anon-relative-entropy-relaxations-signomial_images/imageFile62.png>)

![image 63](<2014-anon-relative-entropy-relaxations-signomial_images/imageFile63.png>)

![image 64](<2014-anon-relative-entropy-relaxations-signomial_images/imageFile64.png>)

![image 65](<2014-anon-relative-entropy-relaxations-signomial_images/imageFile65.png>)

![image 66](<2014-anon-relative-entropy-relaxations-signomial_images/imageFile66.png>)

![image 67](<2014-anon-relative-entropy-relaxations-signomial_images/imageFile67.png>)

![image 68](<2014-anon-relative-entropy-relaxations-signomial_images/imageFile68.png>)

More broadly, relative entropy relaxations for SPs also have the virtue that the bounds they provide are generally robust to small perturbations of the exponents. Speciﬁcally, given a set of exponents {α(j)}ℓj=1 ⊂ Rn, we say that a SAGE cone CSAGE α(1),... ,α(ℓ) is robust to small perturbations of the exponents {α(j)}ℓj=1 when the following condition holds: if a coeﬃcient vector c ∈ Rℓ belongs to the interior of the cone CSAGE α(1),... ,α(ℓ) for a collection of exponents {α(j)}ℓj=1, then c also belongs to the cone CSAGE α ˜(1),... ,α˜(ℓ) for all suﬃciently small perturbations α˜(j) of each α(j). As the SAGE cone CSAGE is a direct sum of AM/GM exponential cones CAGE, robustness of each of the component AM/GM exponential cones CAGE implies the robustness of CSAGE. The following proposition shows that cones of AM/GM exponentials are robust to small perturbations of the exponents for a broad class of exponents. The basic observation underlying this result is that the exponents {α(j)}ℓj=1 appear only as linear constraints in the characterization of the cones CSAGE and CAGE based on (5) and Proposition 6.

Proposition 17. Fix a set of exponents {α(j)}ℓj=0 ⊂ Rn, and let A denote the R(ℓ+1)×n matrix with the α(j)’s as the columns. Let (c,β) ∈ Rℓ+ × R be any point in the interior of the cone CAGE(α(1),... ,α(ℓ);α(0)). Suppose α(0) is not contained in the convex hull of any subset of k ≤ n of the exponents {α(j)}ℓj=1. Then there exists an open set S ⊂ R(ℓ+1)×n containing A with the following property: For any A˜ ∈ S with columns {α˜(j)}ℓj=0, we have that (c,β) belongs to CAGE(α˜(1),... ,α˜(ℓ);α˜(0)).

Proof sketch We provide a brief outline of the proof. As (c,β) belongs to the interior of the cone CAGE(α(1),... ,α(ℓ);α(0)), the entries of c must be strictly positive. Further, we have from Lemma 2 that there exists a ν ∈ Rℓ+ such that D(ν,ec) < β and that ℓj=1 α(j)νj = (1′ν)α(0). Due to the assumption that α(0) is not contained in the convex hull of any subset of k ≤ n of the exponents {α(j)}ℓj=1, we have that ν must contain at least n + 1 nonzeros. Therefore, for all suﬃciently small perturbations {α˜(j)}ℓj=0, there exists a corresponding ν˜ close to ν such that

ℓ j=1(α˜(j) − α˜(0))ν˜j = 0. (If some of the coordinates of the original ν are zero, then there exists a nearby ν˜ with zeros in the same coordinates satisfying ℓj=1(α˜(j) − α˜(0))ν˜j = 0 for all suﬃciently small perturbations {α˜(j)}ℓj=0.) The relative entropy function D(·,ec) is continuous with respect to the ﬁrst argument if the second argument c is ﬁxed and contains strictly positive entries. Consequently, we have that D(ν˜,ec) < β.

![image 69](<2014-anon-relative-entropy-relaxations-signomial_images/imageFile69.png>)

![image 70](<2014-anon-relative-entropy-relaxations-signomial_images/imageFile70.png>)

![image 71](<2014-anon-relative-entropy-relaxations-signomial_images/imageFile71.png>)

![image 72](<2014-anon-relative-entropy-relaxations-signomial_images/imageFile72.png>)

This result demonstrates that the bounds fSAGE(0) (15) and fSAGE(0,1) (19) based on SAGE decompositions are robust to small perturbations of the exponents in the underlying SPs; one can also carry out a similar analysis to show that the bounds fSAGE(p) (15) and fSAGE(p,q) (19) corresponding to higher levels of the hierarchies are robust to small perturbations of the exponents in the underlying SPs.

Example 18. Consider the following signomial obtained by perturbing the exponents of the signomial (13) in Example 8 (but leaving the coeﬃcients unchanged):

f(x) = 10 exp{10.2070x1 + 0.0082x2 − 0.0039x3}

+10 exp{−0.0081x1 + 9.8024x2 − 0.0097x3}

+10 exp{0.0070x1 − 0.0156x2 + 8.1923x3} −14.6794 exp{1.5296x1 + 1.0927x2 + 1.3441x3} −7.8601 exp{1.0750x1 + 1.9108x2 + 1.6339x3}

+8.7838 exp{1.0513x1 + 0.0571x2 + 1.6188x3}.

The SAGE lower bound is tight for the perturbed signomial speciﬁed here, with the optimal value being equal to −0.9458, and the optimal solution being x⋆ = (−0.3016,−0.2605,−0.4013)′. Recall that the SAGE lower bound was also tight for the signomial (13) of Example 8, with the optimal value being equal to −0.9747 and the optimal solution being x⋆ = (−0.3020,−0.2586,−0.4010)′. Hence, this example provides numerical evidence for the robustness of our relative entropy relaxation methods with respect to small perturbations of the exponents.

Approaching this SP as a polynomial optimization problem clearly illustrates the shortcomings of that viewpoint, as small changes in the exponents can lead to very diﬀerent polynomials after clearing denominators in the exponents. In turn, the quality of the bounds and amount of computation required to obtain them via SDP relaxations based on sum-of-squares techniques can vary dramatically for small changes in the exponents. However, relative entropy relaxations for SPs based on SAGE decompositions are well-behaved under such small perturbations of the exponents.

# 5 Discussion

A number of directions for further investigation arise from this work, and we mention some of these here.

Implications for polynomial optimization The methods developed in this paper may oﬀer a useful addition to SDP relaxation frameworks based on sum-of-squares decompositions for poly-

nomial optimization problems over the nonnegative orthant (equivalently, polynomial optimization problems involving even polynomials). For example, the Motzkin polynomial p(y1,y2,y3) = y12y24 + y14y22 + y36 − 3y12y22y32 is certiﬁed as being globally nonnegative via the AM/GM inequality – equivalently, p˜(x1,x2,x3) = p(exp{x1},exp{x2},exp{x3}) is an AM/GM-exponential – although this polynomial cannot directly be expressed as a sum-of-squares. More generally, the methods in this paper may oﬀer eﬀective certiﬁcates of global nonnegativity for certain “sparse” polynomials of large degree, which are sometimes referred to as “fewnomials” in the literature [11]; this point is also exploited in [10], where the authors employ GPs to compute lower bounds on certain multivariate polynomials more eﬃciently than SDPs based on sum-of-squares techniques. In fact one can combine the SDP and the relative entropy relaxation frameworks, based on sum-of-squares and SAGE decompositions respectively, to obtain alternative hierarchies for polynomial optimization problems. Such a combined hierarchy would provide bounds that are at least as good as those produced by SDP relaxations, although this improvement comes at an increased computational cost; it is of interest to investigate and quantify these comparisons.

Eﬃcient transcendental representations of semialgebraic sets Consider the set Sd = {(a,b) ∈ R2 | x2d +ax2 +b ≥ 0 ∀x ∈ R} for d ∈ Z++. This set is convex and semialgebraic for each d ∈ Z++, and it is SDP representable (i.e., expressible as the projection of a slice of the cone of wd×wd positive semideﬁnite matrices, where wd ∈ Z++ may depend on d) based on the observation that a nonnegative univariate polynomial can be expressed as a sum-of-squares. However, these sum-of-squares decompositions consist of many terms for large d; thus, we do not know of SDP descriptions of Sd in which wd does not grow with d. On the other hand, Sd can be represented eﬃciently via relative entropy inequalities as Sd = {(a,b) ∈ R × R+ | ∃ν ∈ R2+ s.t. D(ν,e(1,b)′) ≤ a, (d − 1)ν1 = ν2}. Note that the size of this description does not grow with d. Consequently, there may be semialgebraic sets (indeed, SDP representable sets) that are more eﬃciently speciﬁed via transcendental representations. Underlying this discussion is the insight that the AM/GM inequality oﬀers a diﬀerent proof system than sum-of-squares methods for certifying nonnegativity. Speciﬁcally, the length of a sum-of-squares proof of the AM/GM inequality for a ﬁxed set of rational weights can be very large depending on the denominators of the rational weights. On the other hand, relative entropy methods oﬀer an eﬀective approach for computing a set of weights that certiﬁes nonnegativity via the AM/GM inequality. Investigating the respective power of these diﬀerent proof systems may yield new insights into the possibility of eﬃcient transcendental representations of convex semialgebraic sets.

Eﬀective bounds on quality of approximation A third direction is to provide useful bounds on the size of a relaxation required in order to achieve a speciﬁed quality of approximation to the global minimum. An important step towards addressing this question is to achieve a deeper understanding of the eﬀect of perturbations in the exponents of an SP on the eventual bounds computed at a certain level of our hierarchy. As discussed in Section 4.1, the techniques employed in our proofs of Theorems 15 and 16 do not provide guidance on the eﬀects of such perturbations, and consequently a diﬀerent set of ideas may be required to address this question.

# Acknowledgements

We wish to thank Bill Helton, Pablo Parrilo, and Bernd Sturmfels for helpful conversations at various stages of this project. This work was supported in part by the following grants: National

Science Foundation Career award CCF-1350590 and Air Force Oﬃce of Scientiﬁc Research grant FA9550-14-1-0098.

# A Appendix

We begin by brieﬂy stating the relevant representation theorems from the real algebraic geometry literature – the one we use is due to Krivine [12]; see [21, 24, 28] for other prominent examples. Then we describe a transformation of SPs with rational exponent vectors to polynomial optimization problems. Finally, we put these steps together to give proofs of Theorems 15 and 16.

## A.1 Representation Theorems for Archimedean Modules over Preprimes

We primarily draw from the wonderful exposition in [16]. Let R[Y1,... ,Yℓ] denote the polynomial ring in indeterminates Y with real coeﬃcients, and let Q denote the rational numbers. The ﬁrst object that plays a critical role in our development is a preprime in a polynomial ring:

- Deﬁnition 3. A preprime P ⊂ R[Y1,... ,Yℓ] is a subset containing Q that is closed under addition and multiplication. Further, a preprime P is Archimedean if for each r ∈ R[Y1,... ,Yℓ] there exists m ∈ Z such that r + m ∈ P.

For a preprime P ⊂ R[Y1,... ,Yℓ], the ring of bounded elements of P with respect to R[Y1,... , Yℓ] is deﬁned as:

HP = {r ∈ R[Y1,... ,Yℓ] | ∃m ∈ Z s.t. m ± r ∈ P}.

From [16, Prop 5.1.3], the preprime P is Archimedean if and only if HP = R[Y1,... ,Yℓ]. The next algebraic structure that is central to our discussion is a module over a preprime:

- Deﬁnition 4. Let P ⊂ R[Y1,... ,Yℓ] be a preprime. Then M ⊂ R[Y1,... ,Yℓ] is a P-module if it is closed under addition, is closed under multiplication by an element of P, and contains 1. As


with preprimes, a P-module M is Archimedean if for each r ∈ R[Y1,... ,Yℓ] there exists m ∈ Z such that r + m ∈ M.

Note that 1 ∈ M for a P-module M implies that P ⊂ M. Consequently, if a preprime P is Archimedean, then any P-module M is also Archimedean. Finally, P itself is a P-module. The following result due, in various forms, to several authors is the main foundation for our proofs of Theorems 15 and 16:

Theorem 19. [12, 16] Let P ⊂ R[Y1,... ,Yℓ] be an Archimedean preprime and let M be a Pmodule. Let KM denote the set of points in Rℓ on which every element of M is nonnegative:

KM = {y ∈ Rℓ | r(y) ≥ 0 for all r ∈ M}. If s ∈ R[Y1,... ,Yℓ] is strictly positive on the set of points KM, then s ∈ M: s(y) > 0 for all y ∈ KM ⇒ s ∈ M.

The converse direction, i.e., s ∈ M implies s(y) ≥ 0 for all y ∈ KM, follows directly from the deﬁnition of KM. Results of the form of Theorem 19 are known as representation theorems because the P-module M is usually constructed explicitly, and the positivity of a polynomial s on the nonnegativity set KM associated to M implies that s has an explicit representation.

## A.2 Implicitization and Parametrization of SPs with Rational Exponents

In this section, we present an elementary result that allows us to transform certain families of SPs with rational exponents to polynomial optimization problems over the nonnegative orthant. This result is employed in our proofs of Theorems 15 and 16. Speciﬁcally, consider the problem of verifying positivity of infx∈S f(x) for S = {x ∈ Rn | gi(x) ≥ 0, i = 1,... ,m}, where f(x),{gi(x)}mi=1 are signomials with respect to exponents {α(j)}ℓj=1 ⊂ Qn. Letting f(x) = ℓj=1 cj(f)

′

exp{α(j)′x}

and letting each gi(x) = ℓj=1 cj(gi)′ exp{α(j)′x}, the positivity of infx∈S f(x) with S = {x ∈ Rn | gi(x) ≥ 0, i = 1,... ,m} is equivalent to infy∈T++ c(f)′y > 0 for

T++ ={y ∈ Rℓ | c(gi)′y ≥ 0, i = 1,... ,m} ∩ {y ∈ Rℓ++ | ∃x ∈ Rn s.t. yj = exp{α(j)′x}, j = 1,... ,ℓ}.

(24)

- A.2.1 Implicitization


For rational exponents {α(j)}ℓj=1 ∈ Qn, the set {y ∈ Rℓ++ | ∃x ∈ Rn s.t. yj = exp{α(j)′x}, j =

- 1,... ,ℓ} can be implicitized via polynomial equations as follows. Suppose without loss of generality that the ﬁrst n of the exponent vectors {α(j)}ℓj=1 are linearly independent. Consequently, the remaining exponents {α(j)}ℓj=n+1 can be expressed as linear combinations with rational coeﬃcients


(j) k

of the ﬁrst n exponents. As a result, each yj for j = n+1,... ,ℓ can be expressed as yj = nk=1 yγ

k

for rational vectors γ(j) ∈ Qn, j = n + 1,... ,ℓ. By moving terms involving negative powers from the right to the left side of each of these equations and then suitably clearing denominators in the exponents (valid manipulations over the positive orthant Rℓ++), the set T++ from (24) can be characterized as

T++ ={y ∈ Rℓ | c(gi)′y ≥ 0, i = 1,... ,m} ∩ {y ∈ Rℓ++ | vj(y) − wj(y) = 0, j = n + 1,... ,ℓ}

(25)

for monomials vj(y),wj(y),j = n + 1,... ,ℓ. The restriction to the positive orthant Rℓ++ in the second set here is crucial as the manipulations we describe are only valid over the positive orthant.

In our appeal to Theorem 19, we consider the positivity of infy∈T+ c(f)′y for T+ ={y ∈ Rℓ | c(gi)′y ≥ 0, i = 1,... ,m}

(26)

∩ {y ∈ Rℓ+ | vj(y) − wj(y) = 0, j = n + 1,... ,ℓ}.

However, the implicitization operation is, in general, only valid over the positive orthant Rℓ++. Consequently, we require that the closure of the set T++ is equal to T+, as this would imply that

- infy∈T+ c(f)′y = infy∈T++ c(f)′y. The next two results give conditions under which T+ = cl(T++); these correspond to the assumptions in Theorems 15 and 16.


- Lemma 20. Fix a set of exponents {α(j)}ℓj=1 ∈ Qn with {α(j)}nj=1 being linearly independent, and consider an SP with transformed constraint sets T++ and T+ as deﬁned in (25), (26) for some


set of coeﬃcients c(gi) ∈ Rℓ,i = 1,... ,m. If {y ∈ Rℓ | c(gi)′y ≥ 0, i = 1,... ,m} ⊂ Rℓ++, then cl(T++) = T+.

Proof. One can check that T++ = T+. The result then follows from the observation that T+ is a closed set.

![image 73](<2014-anon-relative-entropy-relaxations-signomial_images/imageFile73.png>)

![image 74](<2014-anon-relative-entropy-relaxations-signomial_images/imageFile74.png>)

![image 75](<2014-anon-relative-entropy-relaxations-signomial_images/imageFile75.png>)

![image 76](<2014-anon-relative-entropy-relaxations-signomial_images/imageFile76.png>)

- Lemma 21. Fix a set of exponents {α(j)}ℓj=1 ∈ Qn with {α(j)}nj=1 being linearly independent. If


the remaining vectors {α(j)}ℓj=n+1 lie in the cone generated by {α(j)}nj=1, then cl(T++) = T+, where these sets are deﬁned in (25), (26).

Proof. As {α(j)}ℓj=n+1 lie in the cone generated by {α(j)}nj=1, the constraint set T++ = {y ∈ Rℓ++ | vj(y) − wj(y) = 0, j = n + 1,... ,ℓ} is speciﬁed via monomials vj(y),wj(y),j = n + 1,... ,ℓ with the property that each vj(y) is a monomial consisting only of the variable yj (i.e., just yj raised to a positive integer) and each wj(y) is a monomial consisting of (a subset of) the variables y1,... ,yn. This follows directly from the assumption that {α(j)}ℓj=n+1 lie in the cone generated by {α(j)}nj=1, and from the construction of the monomials vj(y),wj(y) preceding (25). Consequently, one can check that for each point in T+ that lies on a face of the nonnegative orthant Rℓ+, the point can be approached as a limit of a sequence in T++. Hence, cl(T++) = T+.

![image 77](<2014-anon-relative-entropy-relaxations-signomial_images/imageFile77.png>)

![image 78](<2014-anon-relative-entropy-relaxations-signomial_images/imageFile78.png>)

![image 79](<2014-anon-relative-entropy-relaxations-signomial_images/imageFile79.png>)

![image 80](<2014-anon-relative-entropy-relaxations-signomial_images/imageFile80.png>)

After the implicitization step and the appeal to Theorem 19 to obtain representations of positive polynomials, we ﬁnally derive a conclusion in terms of signomials as follows. We apply the reverse transformation yj ← exp{α(j)′x} for each j = 1,... ,ℓ, which is a valid parametrization of the system of polynomial equations vj(y) − wj(y) = 0,j = n + 1,... ,ℓ for y ∈ Rℓ++. The validity of this step relies on the fact that {α(j)}nj=1 are linearly independent.

- A.2.2 SAGE functions and redundant constraints as polynomials

The above discussion implies that a nonnegative signomial ℓj=1 cj exp{α(j)′x} deﬁned with respect to rational exponents {α(j)}ℓj=1 ⊂ Qn can also be viewed as a linear function c′y that is nonnegative over cl(T++), where T++ = {y ∈ Rℓ++ | vj(y) = wj(y),j = n + 1,... ,ℓ} is constructed as in the description preceding (25). A SAGE function is simply a nonnegative linear function over cl(T++) with an eﬃciently computable nonnegativity certiﬁcate. In a similar vein, nonnegative signomials (SAGE functions) deﬁned with respect to exponents in Ep({α(j)}ℓj=1) can be viewed as degreep polynomials that are nonnegative (eﬃciently certiﬁed as being nonnegative) over cl(T++) and vice-versa. As a result of this correspondence, we use overloaded terminology to refer to SAGE functions both in the domain of signomials (distinguished by the use of the variable x) and in the domain of polynomials (using the variable y). In an analogous manner, we also view elements of the set of redundant constraints Rq(C) as degree-q polynomials in the variables y1,... ,yℓ that are constrained to be nonnegative over cl(T++).

- A.3 Proof of Theorem 16


Let f(x) = ℓj=1 cj(f) exp{α(j)′x} and let each gi(x) = ℓj=1 c(jgi) exp{α(j)′x} for i = 1,... ,m. Set yj = exp{α(j)′x} for j = 1,... ,ℓ. The assumption that constraints of the form U ≥ exp{α(j)′x} ≥ L for each j = 1,... ,ℓ with U,L ∈ R++ are explicitly speciﬁed in C implies that {y ∈ Rℓ | c(gi)′y ≥

- 0, i = 1,... ,m} ⊂ Rℓ++. Hence, we appeal to Lemma 20 to conclude that infy∈T++ c(f)′y = infx∈KC f(x) > 0 is equivalent to infy∈T+ c(f)′y > 0, where the set T+ = {y ∈ Rℓ | c(gi)′y ≥ 0, i =
- 1,... ,m} ∩ {y ∈ Rℓ+ | vj(y) − wj(y) = 0, j = n + 1,... ,ℓ} for suitable monomials vj,wj (26). Let P˜ ⊂ R[Y1,... ,Yℓ] be the preprime generated by R+, y1,... ,yℓ, and c(g1)′y,... ,c(gm)′y.


We note that P˜ is Archimedean as it contains yj and U − yj for each j = 1,... ,ℓ, and hence the generators of the preprime are in the ring of bounded elements. Consider the preprime P = P˜ + I, where I is the ideal generated by the polynomials vj(y) − wj(y) for j = n + 1,... ,ℓ. As P˜ is Archimedean, so is P.

Next consider the set M˜ formed by taking ﬁnite sums of elements from the set {s(y)h(y) | s(y) ∈ SAGE(Ep({α(j)}ℓj=1)), h(y) ∈ Rq(C), p,q ∈ Z+}; see Section A.2.2 for discussion on this overloaded notation. The set of SAGE functions is closed under addition, and also under multiplication by posynomials; thus, one can check that M˜ is a P˜-module. Consequently, M = M˜ + I is a P-module. Further, M is Archimedean as P is Archimedean. Finally, we observe that the nonnegativity set KM = {y ∈ Rℓ | r(y) ≥ 0 for all r ∈ M} is equal to T+ as the constraints speciﬁed by the polynomials in M are implied by those that specify the constraints in T+. Hence, we apply Theorem 19 to conclude that c(f)′y ∈ M. By substituting back yj ← exp{α(j)′x}, the term corresponding to the ideal I vanishes and we obtain the desired result.

![image 81](<2014-anon-relative-entropy-relaxations-signomial_images/imageFile81.png>)

![image 82](<2014-anon-relative-entropy-relaxations-signomial_images/imageFile82.png>)

![image 83](<2014-anon-relative-entropy-relaxations-signomial_images/imageFile83.png>)

![image 84](<2014-anon-relative-entropy-relaxations-signomial_images/imageFile84.png>)

## A.4 Proof of Theorem 15

We begin with the following result on a constrained analog of Polya’s theorem [16, 20] regarding representations of forms that are positive on the simplex; a generalization of this statement is proved in [7], but the specialization stated here suﬃces for our purposes.

Proposition 22. [7] Let uk(y) for k = 0,... ,s be a collection of homogenous polynomials in R[Y1,... ,Yℓ]. Let V = {y ∈ Rℓ+ | uk(y) = 0,k = 1,... ,s}. If u0(y) > 0 for all y ∈ V\{0}, then there exists p ∈ Z+ such that ( ℓj=1 yi)pu0(y) = τ(y) +θ(y) where τ(y) is a polynomial consisting of all nonnegative coeﬃcients and θ(y) lies in the ideal generated by the polynomials {uk(y)}sk=1.

We use this result after suitably transforming our unconstrained SP to a polynomial optimization problem over the nonnegative orthant.

Proof of Theorem 15 The main idea in this proof is to transform the signomial f(x) = j=1 cj exp{α(j)′x} appropriately so that we can apply Proposition 22.

The unconstrained SP infx∈Rn f(x) can be transformed to infy∈T+ c′y based on Lemma 21, where T+ = {y ∈ Rℓ+ | vj(y) = w(y),j = n + 1,... ,ℓ} and the construction of the monomials vj(y),wj(y) is described in the discussion preceding (25). We note that the monomials vj(y),wj(y) for j = n + 1,... ,ℓ satisfy several properties:

- (i) We have that vn+1(y) = yn+1 and wn+1(y) = 1 because α(n+1) = 0.
- (ii) For each j = n + 2,... ,ℓ, the monomial vj(y) is only a function of yj and the monomial wj(y) is only a function of y1,... ,yn. This follows because each α(j) is a convex combination with rational weights of the exponents {α(i)}ni=1+1 for j = n + 2,... ,ℓ.
- (iii) Finally, deg(vj) > deg(wj) for each j = n + 2,... ,ℓ, where deg(·) denotes the degree of a


polynomial. This is a consequence of the assumption that α(j) ∈/ conv({α(i)}ni=1) for each j = n + 2,... ,ℓ.

Now deﬁne modiﬁed monomials:

w˜j(y) = wj(y)yndeg(+1vj)−deg(wj), j = n + 2,... ,ℓ, (27)

and consider the set T˜+ = {y ∈ Rℓ+ | vj(y) = w˜j(y),j = n + 2,... ,ℓ}. The diﬀerence between T˜+ and T+ is that each wj(y) is replaced by w˜j(y), and there is no constraint corresponding to j = n + 1 (i.e., the constraint yn+1 = 1 from property (i) above is removed). Further, note that the polynomials vj(y) − w˜j(y) for j = n + 2,... ,ℓ are homogenous polynomials based on property (iii) above.

As the polynomials vj(y) − w˜j(y) for j = n + 2,... ,ℓ are homogenous, we intend to apply Proposition 22 to the polynomial optimization problem infy∈T˜

c′y. In order to do so, we need to verify that c′y > 0 for all y ∈ T˜+\{0}.

+

First, suppose that y ∈ T˜+\{0} with yn+1 > 0. As the polynomials vj(y) − w˜j(y) for j = n+2,...,ℓ and the linear function c′y are homogenous, we may scale y so that yn+1 = 1 since this not aﬀect our conclusions about the positivity of c′y. Setting yn+1 = 1 corresponds to verifying the positivity of c′y over T+. As infy∈T+ c′y = infx∈Rn f(x) > 0, we have that c′y > 0 for all

- y ∈ T˜+\{0} whenever yn+1 = 0. Next, suppose that y ∈ T˜+\{0} with yn+1 = 0. The deﬁnition of T˜+ directly implies that each


yj = 0 for j = n + 2,... ,ℓ, because vj(y) for j = n + 2,... ,ℓ is only a monomial consisting of yj raised to a positive integer (from property (ii) above) and w˜j(y) consists of yn+1 raised to a positive integer (from property (ii) above and from (27)). Consequently, we need to verify the positivity of c′y with y ∈ Rℓ+\{0} and with yj = 0 for j = n + 1,... ,ℓ. Since cj > 0 for j = 1,... ,n by assumption, it follows that c′y > 0 for all y ∈ T˜+\{0} with yn+1 = 0.

Combining these observations, we appeal to Proposition 22 to conclude that ( ℓj=1 yi)pc′y = τ(y) + θ(y) where τ(y) is a polynomial consisting of all nonnegative coeﬃcients and θ(y) lies in the ideal generated by the polynomials {vj(y) − w˜j(y)}ℓj=n+2. By substituting yn+1 ← 1 and yj ← exp{α(j)′y} for j = n + 2,... ,ℓ, and by noting that posynomials are SAGE functions, we have the desired result.

![image 85](<2014-anon-relative-entropy-relaxations-signomial_images/imageFile85.png>)

![image 86](<2014-anon-relative-entropy-relaxations-signomial_images/imageFile86.png>)

![image 87](<2014-anon-relative-entropy-relaxations-signomial_images/imageFile87.png>)

![image 88](<2014-anon-relative-entropy-relaxations-signomial_images/imageFile88.png>)

# References

- [1] S. Boyd, S. J. Kim, D. Patil, and M. Horowitz. Digital Circuit Optimization via Geometric Programming. Operations Research, 53:899–932, 2005.
- [2] S. Boyd, S. J. Kim, L. Vandenberghe, and A. Hassibi. A Tutorial on Geometric Programming. Optimization and Engineering, 8:67–127, 2007.
- [3] S. P. Boyd and L. Vandenberghe. Convex Optimization. Cambridge University Press, 2004.
- [4] M. Chiang. Geometric Programming for Communication Systems. Foundations and Trends in Communications and Information Theory, 2:1–154, 2005.
- [5] M. Chiang and S. Boyd. Geometric Programming Duals of Channel Capacity and Rate Distortion. IEEE Transactions on Information Theory, 50:245–258, 2004.
- [6] T. Cover and J. Thomas. Elements of Information Theory. Wiley, 2006.
- [7] P. J. C. Dickinson and J. Povh. On an Extension of Polya’s Positivstellensatz. Journal of Global Opimization, 2014.
- [8] R. J. Duﬃn and E. L. Peterson. Geometric Programming with Signomials. Journal of Optimization Theory and Applications, 11:3–35, 1973.
- [9] R. J. Duﬃn, E. L. Peterson, and C. M. Zener. Geometric Programming: Theory and Application. John Wiley and Sons, 1967.
- [10] M. Ghasemi and M. Marshall. Lower Bounds for Polynomials using Geometric Programming. SIAM Journal on Optimization, 22:460–473, 2012.


- [11] A. G. Khovanskii. Fewnomials. American Mathematical Society, 1991.
- [12] J. L. Krivine. Anneaux Prordonns. Journal d’Analyse Mathmatique, 12:307–326, 1964.
- [13] J. B. Lasserre. Global Optimization with Polynomials and the Problem of Moments. SIAM Journal on Optimization, 11:796–817, 2001.
- [14] N. Linial, A. Samorodnitsky, and A. Wigderson. A Deterministic Strongly Polynomial Algorithm for Matrix Scaling and Approximate Permanents. Combinatorica, 20, 2000.
- [15] C. D. Maranas and C. A. Floudas. Global Optimization in Generalized Geometric Programming. Computers and Chemical Engineering, 21:351–369, 1997.
- [16] M. Marshall. Positive Polynomials and Sums of Squares. American Mathematical Society, 2008.
- [17] P. A. Parrilo. Structured Semideﬁnite Programs and Semialgebraic Geometry Methods in Robustness and Optimization. PhD thesis, California Institute of Technology, 2000.
- [18] P. A. Parrilo. Semideﬁnite Programming Relaxations for Semialgebraic Problems. Mathematical Programming, 96:293–320, 2003.
- [19] E. L. Peterson. Geometric Programming. SIAM Review, 18:1–51, 1976.
- [20] G. Polya. Uber Positive Darstellung von Polynomen. Vierterhartschrift d. Naturforschenden Gessellschaft in Zurich, 73:141–145, 1928.
- [21] M. Putinar. Positive Polynomials on Compact Semi-algebraic Sets. Indiana University Mathematics Journal, 42:969–984, 1993.
- [22] B. Reznick. Uniform Denominators in Hilbert’s Seventeenth Problem. Mathematische Zeitschrift, 220:75–97, 1995.
- [23] R. T. Rockafellar. Convex Analysis. Princeton University Press, 1970.
- [24] K. Schmudgen. The K-moment Problem for Compact Semi-algebraic Sets. Annals of Mathematics, 289:203–206, 1991.
- [25] P. Shen. Linearization Method of Global Optimization for Generalized Geometric Programming. Applied Mathematics and Computation, 162:353–370, 2005.
- [26] H. D. Sherali. Global Optimization of Nonconvex Polynomial Programming Problems having Rational Exponents. Journal of Global Optimization, 12:267–283, 1998.
- [27] N. Z. Shor. Class of Global Minimum Bounds of Polynomial Functions. Cybernetics, 23:731– 734, 1987.
- [28] G. Stengle. A Nullstellensatz and a Positivstellensatz in Semialgebraic Geometry. Annals of Mathematics, 207:87–97, 1974.
- [29] K. Yun and C. Xi. Second-order Method of Generalized Geometric Programming for Spatial Frame Optimization. Computer Methods in Applied Mechanics and Engineering, 141:117–123, 1997.


