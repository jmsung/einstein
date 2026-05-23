arXiv:2103.05738v1[math.NA]9Mar2021

Multiple Zeros of Nonlinear Systems

Barry H. Dayton∗ Tien-Yien Li† Zhonggang Zeng‡

March 11, 2021

Abstract

As an attempt to bridge between numerical analysis and algebraic geometry, this paper formulates the multiplicity for the general nonlinear system at an isolated zero, presents an algorithm for computing the multiplicity structure, proposes a depth-deﬂation method for accurate computation of multiple zeros, and introduces the basic algebraic theory of the multiplicity. Furthermore, this paper elaborates and proves some fundamental properties of the multiplicity, including local ﬁniteness, consistency, perturbation invarance, and depth-deﬂatability. As a justiﬁcation of this formulation, the multiplicity is proved to be consistent with the multiplicity deﬁned in algebraic geometry for the special case of polynomial systems. The proposed algorithms can accurately compute the multiplicity and the multiple zeros using ﬂoating point arithmetic even if the nonlinear system is perturbed.

2000 Mathematics Subject Classiﬁcation: Primary 65H10, Secondary 68W30

- 1 Introduction Solving a system of nonlinear equations in the form f(x) = 0, or


f1(x1,... ,xs) = f2(x1,... ,xs) = ··· = ft(x1,... ,xs) = 0 (1)

with f = [f1,... ,ft]H and x = (x1,... ,xs), is one of the most fundamental problems in scientiﬁc computing, and one of the main topics in most numerical analysis textbooks. In the literature outside of algebraic geometry, however, an important question as well as its answer seem to be absent over the years: What is the multiplicity of an isolated zero to the system and how to identify it accurately.

For a single equation f(x) = 0, it is well known that the multiplicity of a zero x∗ is m if f(x∗) = f′(x∗) = ··· = f(m-1)(x∗) = 0 and f(m)(x∗) = 0. (2)

![image 1](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile1.png>)

∗Department of Mathematics, Northeastern Illinois University, Chicago, IL 60625 (email: bhdayton@neiu.edu). †Department of Mathematics, Michigan State University, East Lansing, MI 48824 (li@math.msu.edu). Research

supported in part by NSF under Grant DMS-0811172.

‡Department of Mathematics, Northeastern Illinois University, Chicago, IL 60625 (zzeng@neiu.edu). Research supported in part by NSF under Grant DMS-0715127.

The multiplicity of a polynomial system at a zero has gone through rigorous formulations since Newton’s era [8, pp. 127-129] as one of the oldest subjects of algebraic geometry. Nonetheless, the standard multiplicity formulation and identiﬁcation via Gro¨bner bases for polynomial systems are somewhat limited to symbolic computation, and largely unknown to numerical analysts.

As an attempt to bridge between algebraic geometry and numerical analysis, we propose a rigorous formulation for the multiplicity structure of a general nonlinear system at a zero. This multiplicity structure includes, rather than just a single integer for the multiplicity, several structural invariances that are essential in providing characteristics of the system and accurate computation of the zero. For instance, at the zero x∗ = (0,0) of the nonlinear system

sin x1 cos x1 − x1 = sin x2 sin2 x1 + x42 = 0 (3) we shall have:

- • The multiplicity m = 12.
- • Under a small perturbation to the system (3), there is a cluster of exactly 12 zeros (counting multiplicities) in a neighborhood of x∗ = (0,0).
- • The Hilbert function {1,2,3,2,2,1,1, 0, 0,· ·· } forms a partition of the multiplicity 12.
- • There exist 12 linearly independent diﬀerential operators ∂00, ∂10, ... , ∂05 −∂22, ∂06 −∂23, grouped by the diﬀerential orders and counted by the Hilbert function as shown in Figure 1 below. They induce 12 diﬀerential functionals that span the dual space associated with system (3). These functionals satisfy a closedness condition and vanish on the two functions in (3) at the zero (0,0). Here, the diﬀerential operator

∂j1···js ≡ ∂xj1

1 ···xjss ≡ j 1

![image 2](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile2.png>)

1! · · · js!

∂j1+···+js ∂xj11 · · · ∂xjss

![image 3](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile3.png>)

(4)

of order j1 + ··· + js naturally induces a linear functional

∂j1···js[x∗] : f −→ (∂j1···jsf)(x∗) (5) on functions f whose indicated partial derivative exists at the zero x∗.

- • The breadth, or the nullity of the Jacobian at x∗, is 2.
- • The depth, which is the highest diﬀerential order of the functionals at x∗, is 6.


![image 4](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile4.png>)

Figure 1: Illustration of the multiplicity structure including dual basis, Hilbert function, breadth and depth of the system (3) at the zero (0, 0)

Such a multiplicity structure at an isolated zero of a general nonlinear system will be introduced in §2. We prove the so-deﬁned multiplicity agrees with the intersection multiplicity of polynomial

systems in algebraic geometry. It is ﬁnite if and only if the zero is isolated, and more importantly, this ﬁniteness ensures termination of the multiplicity identiﬁcation algorithm NonlinearSystemMultiplicity given in §2.3, and it also provides a mechanism for determining whether a zero is isolated [2]. Furthermore, the multiplicity structure of the given nonlinear system can be computed by constructing the Macaulay matrices [21] together with the numerical rank revealing [20]. As a result, we developed numerical algorithms that accurately calculate the multiplicity structure even if the system data are inexact at a zero that is given approximately (c.f. §2.3 and §3.3).

It is well documented that multiple zeros are diﬃcult to compute accurately even for a single equation. There is a perceived barrier of “attainable accuracy”: The number of correct digits attainable for a multiple zero is bounded by the number of digits in the hardware precision divided by the multiplicity. For instance, only three correct digits can be expected in computing a ﬁvefold zero using the double precision (16 digits) ﬂoating point arithmetic. Such a barrier has been overcome for univariate polynomial equations [34]. Based on the multiplicity theory established in this article, we shall derive a depth-deﬂation algorithm in §3 for computing multiple zeros of general nonlinear systems, which can accurately compute the multiple zeros without extending the arithmetic precision even when the nonlinear system is perturbed. The depth deﬁned in the multiplicity structure actually bounds the number of deﬂation steps. A related multiplicity deﬂation method is used in [17], in which the main goal is to speed up Newton’s iteration.

As mentioned above, the study of the multiplicity for a polynomial system at an isolated zero can be traced back to Newton’s time [8, pp. 127-129]. Besides polynomial systems, multiple zeros of a nonlinear system occur frequently in scientiﬁc computing. For instance, when a system depends on certain parameters, a multiple zero emerges when the parameters reach a bifurcation point [3, §1.1]. Accurate computation of the multiple zero and reliable identiﬁcation of the multiplicity structure may have a profound ramiﬁcation in scientiﬁc computing. This paper furnishes the theoretical details of the preliminary results on polynomial systems announced in an abstract [5], and in addition, the scope of this work has been substantially expanded to general nonlinear systems.

# 2 Formulation and computation of the multiplicity structure

## 2.1 The notion and fundamental theorems of the multiplicity

The general nonlinear system (1) is represented by either the mapping f : s −→ t or the set F = {f1,... ,ft} of functions in the variables x1,... ,xs. We assume functions f : s −→

in this paper have all the relevant partial derivatives arising in the elaboration. The multiplicity which we shall formulate in this section will extend both the multiplicity (2) of a single equation and the Macaulay-Gr¨bner duality formulation of multiplicity for polynomial systems.

Denote N = {0,±1,±2,...}. For an integer array j = (j1,... ,js) ∈ Ns, write j ≥ 0 if ji ≥ 0 for all i ∈ {1,... ,s}. For every j = (j1,··· ,js) ∈ Ns with j ≥ 0, denote xj = xj11 ··· xjss and (x − y)j = (x1 − y1)j1 ··· (xs − ys)js, and diﬀerential functional monomial ∂j[xˆ] at xˆ ∈ s as in (5), with order |j| = j1 + ··· + js. For simplicity, we adopt the convention

∂j[xˆ](f) ≡ 0 for all f whenever j  ≥ 0 (6)

throughout this paper. A linear combination c = cj1∂j1[xˆ] + ··· + cjk∂jk[xˆ] is called a diﬀerential functional, which will produce a set of numbers c(F) = {c(f1),... ,c(ft)} when applied to the system F = {f1,... ,ft}. For diﬀerential functionals, the linear anti-diﬀerentiation transformation

φi is deﬁned by φi j cj∂j[xˆ] = j cjφi ∂j[xˆ] with

ji if σ = i ji−1 if σ = i

1...js′[xˆ] where jσ′ =

φi ∂j1...js[xˆ] = ∂j′

(7)

for i = 1,... ,s. From (6), we have φi(∂j[xˆ]) = 0 if ji = 0. With these diﬀerential functionals and the linear transformations, we now formulate the multiplicity at a zero xˆ of the nonlinear system (1) as follows.

- Deﬁnition 1 Let F = {f1,... ,ft} be a system of functions having derivatives of order γ ≥ 1 at a zero xˆ ∈ s. Let Dx0ˆ(F) = span{∂0...0} and


cj∂j[xˆ] c(F) = {0}, φi(c) ∈ Dxαˆ-1(F), ∀ i = 1,... ,s (8)

Dxαˆ(F) = c =

j∈Ns, cj∈ , |j|≤α

for α = 1,... ,γ. We call such sets dual subspaces. If Dxγˆ(F) = Dxγˆ-1(F), then the vector space Dxˆ(F) = Dx0ˆ(F) ∪ Dx1ˆ(F) ∪ ··· ∪ Dxγˆ−1(F) = Dxγˆ(F) (9)

is called the dual space of the system F at xˆ. The dimension of Dxˆ(F), i.e. dim Dxˆ(F) , is called the multiplicity of F at xˆ.

Notice that dual subspaces Dxαˆ(F)’s strictly enlarge as the diﬀerential order α increases until reaching certain α = δ at which Dxδˆ(F) = Dδ

+1

+1

xˆ (F), and thus all functionals in Dδ

xˆ (F) are of diﬀerential orders up to δ. As a result, there are no functionals in the subsequent dual subspaces with diﬀerential orders δ + 2, δ + 3,... since φi Dxαˆ(F) ⊂ Dα

+1

xˆ (F) for i = 1,... ,s. Thus Dx0ˆ(F) Dx1ˆ(F) ··· Dxδˆ(F) = Dδ

+1

xˆ (F) = ··· = Dxγˆ(F) = Dxˆ(F).

The integer δ, called the depth which will be deﬁned later, is the highest order of diﬀerential functionals in the dual space.

We may also denote the dual space as Dxˆ(f) when the nonlinear system is represented as a mapping f = [f1,... ,ft]⊤. It is important to note that vanishing at the system c(F) = {0} is insuﬃcient for the functional c to be in the dual space Dxˆ(F). This becomes more transparent in single equation f(x) = 0 where the multiplicity is not the number of vanishing derivatives f(k)(x) = 0 at a zero x∗. For instance, inﬁnite number of functionals ∂0[0], ∂2[0], ∂4[0], ... vanish at the (1 × 1)-system {sin x}, since derivatives sin(2k) 0 = 0 for all integers k ≥ 0. Among these functionals, however, only ∂0[0] ∈ D0({sin x}) since

k-1

φ1(∂2k[0])(sin x) = ∂2k−1[0](sin x) = (−1)

(2k−1)! cos 0 = 0,

![image 5](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile5.png>)

namely ∂2k[0]  ∈ D0({sin x}) for all k ≥ 1, therefore the multiplicity of sinx is one at x = 0. The crucial closedness condition

φi(c) ∈ Dxˆ(F) for all c ∈ Dxˆ(F) and i = 1,... ,s (10)

in Deﬁnition 1 requires the dual space Dxˆ(F) to be invariant under the anti-diﬀerentiation transformation φi’s. The following lemma is a direct consequence of the closedness condition.

- Lemma 1 A diﬀerential functional c is in the dual space Dxˆ(F) of the nonlinear system F = {f1,... ,ft} at the zero xˆ if and only if


c (x − xˆ)jfi(x) = 0 for any i ∈ {1,... ,t} and j ∈ Ns with j ≥ 0. (11)

Proof. For any j = (j1,... ,js), k = (k1,... ,ks), and function f, the Leibniz rule of derivatives yields

∂j[xˆ] (x − xˆ)kf(x) = ∂j-k[xˆ](f) ≡ φk11 ◦ φk22 ◦ ··· ◦ φkss (∂j[xˆ])(f). (12) The equation (11) holds because of the closedness condition (10) and the linearity of c.

The dual space Dxˆ(F) itself actually contains more structural invariants of the multiple zero beyond the multiplicity for the system F. Via dual subspaces Dxαˆ(F), a Hilbert function h : N → N can be deﬁned as follows:

h(0) = dim Dx0ˆ(F) ≡ 1, h(α) = dim Dxαˆ(F) − dim Dxαˆ−1(F) for α ∈ {1,2,... }. (13)

This Hilbert function is often expressed as a inﬁnite sequence {h(0),h(1),...}, with which we introduce the breadth and the depth of Dxˆ(F), denoted by βxˆ(F) and δxˆ(F) respectively, as

βxˆ(F) = h (1) and δxˆ(F) = max{α | h (α) > 0}.

In other words, the breadth is the nullity of the Jacobian at xˆ for the system (1) and the depth is the highest diﬀerential order of functionals in Dxˆ(F). They are important components of the multiplicity structure that dictate the deﬂation process for accurate computation of the multiple zero (c.f. §3).

In contrast to system (3), the system {x21 sin x1, x22−x22 cos x2} also has a zero (0,0) of multiplicity 12 but having a diﬀerent Hilbert function {1,2,3,3,2,1,0,· ·· } and a diﬀerent dual space

span

1

∂00 ,

2 ∂10, ∂01,

![image 6](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile6.png>)

![image 7](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile7.png>)

3 ∂20, ∂11, ∂02,

![image 8](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile8.png>)

![image 9](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile9.png>)

3 ∂21, ∂12, ∂03,

![image 10](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile10.png>)

![image 11](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile11.png>)

2 ∂13, ∂22,

![image 12](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile12.png>)

![image 13](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile13.png>)

1

∂23 . (14)

The polynomial system {x32, x2 − x23, x3 − x21} at origin is again 12-fold with Hilbert function {1,··· ,1,0,··· } and a dual space basis

1 ∂000,

1 ∂100,

1

1 ∂400 + ∂201 + ∂002 + ∂010,

![image 14](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile14.png>)

![image 15](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile15.png>)

![image 16](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile16.png>)

![image 17](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile17.png>)

![image 18](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile18.png>)

![image 19](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile19.png>)

![image 20](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile20.png>)

![image 21](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile21.png>)

∂200 + ∂001, · · · ,

1 ∂800 + ∂601 + ∂402 + ∂203 + ∂410 + ∂004 + ∂211 + ∂012 + ∂020

![image 22](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile22.png>)

![image 23](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile23.png>)

· · · ,

1

![image 24](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile24.png>)

![image 25](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile25.png>)

∂11,00 + ∂901 + ∂702 + ∂710 + ∂503 + ∂511 + ∂304 + ∂312 + ∂105 + ∂320 + ∂113 + ∂121 .

· · · ,

(15)

The last example is of special interest because, as a breadth-one case, its dual space can be computed via a simple recursive algorithm (c.f. §2.3). The dual bases in (14) and (15) are calculated by applying the algorithm NonlinearSystemMultiplicity provided in §2.3 and implemented in ApaTools [35].

We now provide justiﬁcations for our multiplicity formulation in Deﬁnition 1 from its basic properties. First of all, the multiplicity is a direct generalization of the multiplicity (2) of univariate functions, where the dual space at an m-fold zero x∗ is Dx∗(f) = span{∂0[x∗], ∂1[x∗], ... , ∂m-1[x∗]}

with Hilbert function {1,1,... ,1,0,...} as well as breadth one and depth m−1. Secondly, the multiplicity is well deﬁned for analytic systems as a ﬁnite positive integer at any isolated zero xˆ, as asserted by the Local Finiteness Theorem below. Thus, the process of calculating the multiplicity of an isolated zero will always terminate at certain γ when Dxγˆ(F) = Dxγˆ-1(F). The dual subspace dimensions dim Dx0ˆ(F) ≤ dim Dx1ˆ(F) ≤ dim Dx2ˆ(F) ≤ ··· can be unbounded if the zero lies in a higher dimensional set of zeros. For example, the dual subspaces D(0α,0)({sin(x2), x cos(y)}) never stop expanding since inﬁnitely many linearly independent functionals ∂y[(0,0)], ∂y2[(0,0)], ∂y3[(0,0)], ... satisfy the closedness condition and vanish at the zero (0,0). Obviously, (0,0) lies in the zero set {(0,y)}, the entire y-axis, of the system {sin(x2), x cos y}.

- Deﬁnition 2 A point xˆ is an isolated zero of a system F = {f1,... ,ft} if there is a neighborhood ∆ of xˆ in s such that xˆ is the only zero of F in ∆.


We now establish some fundamental properties of the multiplicity for systems of analytic functions. An (multivariate) analytic function, also called holomorphic function, in an open set Ω is commonly deﬁned as a function f that possesses a power series expansion converging to f at every point x ∈ Ω [30, p.25].

- Theorem 1 (Local Finiteness Theorem) For a system F of functions that are analytic in an open set Ω ⊂ s, a zero xˆ ∈ Ω is isolated if and only if supα≥0 dim Dxαˆ(F) is ﬁnite.

This theorem ensures that the multiplicity is well deﬁned at every isolated zero, and the multiplicity computation at an isolated zero will terminate in ﬁnitely many steps. It also provides a mechanism for identifying nonisolated zeros [2] for polynomial systems solved by homotopy method where a multiplicity upper bound is available. The method in [15] can be used to identify nonisolated zeros for general nonlinear systems even though it is intended for polynomial systems.

When the nonlinear system P consists of polynomials p1,... ,pt in the variables x1,... ,xs, the multiplicity theory, i.e. the intersection multiplicity at a zero of such a special system, has been well studied in algebraic geometry. The following theorem asserts that the multiplicity dim Dxˆ(P) formulated in Deﬁnition 1 in this special case is identical to the intersection multiplicity of polynomial systems in algebraic geometry.

- Theorem 2 (Multiplicity Consistency Theorem) For a system P of polynomials with com-

plex coeﬃcients, the multiplicity dim Dxˆ(P) is identical to the intersection multiplicity of P at an isolated zero xˆ.

The following Perturbation Invariance Theorem asserts that the multiplicity as deﬁned equals to the number of zeros “multiplied” from a multiple zero when the system is perturbed. As a result,

- Deﬁnition 1 is intuitively justiﬁed.


- Theorem 3 (Perturbation Invariance Theorem) Let F = {f1,... ,fs} be a system of functions that are analytic in a neighborhood Ω of an m-fold zero xˆ ∈ s and F-1(0) ∩ Ω = {xˆ}.


Then, for any functions g1,... ,gs that are analytic in Ω and Fε = {f1 + εg1,... ,fs + εgs}, there exists a θ > 0 such that, for all 0 < ε < θ,

m = dim Dxˆ(F) =

dim Dx˜(Fε) .

x ˜∈Fε−1(0)∩Ω

In other words, multiplicities of zeros are invariant under small perturbation to the system of analytic functions. An m-fold zero becomes a cluster of exactly m zeros counting multiplicities. The proof of Theorem 3 follows from [26, Lemma 6]. We may illustrate this theorem by a computing experiment on the following example.

- Example 1 Consider the system F = {sin x cos y−x, sin y sin2 x−y2} having multiplicity 6 at the zero (0,0). In a small neighborhood of (0,0), we compute the zeros of the perturbed system


Fǫ = {sin x cos y − x − ǫ, siny sin2 x − y2 + ǫ} (16)

for small values of ǫ. A cluster of exactly 6 zeros of Fǫ near (0,0) are found by Newton’s iteration using zeros of the truncated Taylor series of Fǫ as the initial iterates, matching the multiplicity of the system F at (0,0). Table 1 shows the zeros of Fǫ for ǫ = 10-8 and 10-12. The cluster as shown shrinks to (0,0) when the perturbation decreases in magnitude.

![image 26](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile26.png>)

ǫ = 10−8

![image 27](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile27.png>)

![image 28](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile28.png>)

![image 29](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile29.png>)

![image 30](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile30.png>)

![image 31](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile31.png>)

![image 32](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile32.png>)

x1, x2 (−0.0039173928 ∓0.0000003908i, − 0.0000076728 ± 0.0000997037i) x3, x4 ( 0.0019584003 ±0.0033883580i, 0.0000035695 ± 0.0000935115i) x5, x6 ( 0.0019590795 ∓0.0033879671i, 0.0000040733 ± 0.0001067848i)

![image 33](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile33.png>)

![image 34](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile34.png>)

![image 35](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile35.png>)

![image 36](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile36.png>)

![image 37](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile37.png>)

![image 38](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile38.png>)

![image 39](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile39.png>)

![image 40](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile40.png>)

![image 41](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile41.png>)

ǫ = 10−12 x1, x2 (−0.000181717560 ∓ 0.000000000182i, − 0.000000016511 ±0.000000999864i) x3, x4 ( 0.000090858627 ± 0.000157362584i, 0.000000008136 ±0.000000985770i) x5, x6 ( 0.000090858942 ∓ 0.000157362403i, 0.000000008372 ±0.000001014366i)

![image 42](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile42.png>)

![image 43](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile43.png>)

![image 44](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile44.png>)

![image 45](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile45.png>)

![image 46](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile46.png>)

![image 47](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile47.png>)

![image 48](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile48.png>)

![image 49](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile49.png>)

![image 50](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile50.png>)

![image 51](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile51.png>)

![image 52](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile52.png>)

![image 53](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile53.png>)

![image 54](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile54.png>)

![image 55](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile55.png>)

![image 56](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile56.png>)

Table 1: Zeros of the perturbed system Fǫ in (16) near (0,0) for ǫ = 10-8 and 10-12.

The proofs of the above three fundamental theorems on multiplicities will be given in §2.4, in which the algebraic foundation of the multiplicity will be established.

Remark on the history of multiplicity: A discussion on the history of the multiplicity formulations for a polynomial system at a zero is given in [8, p.127] from algebraic geometry. As Fulton points out there have been many diﬀering concepts about multiplicity. Mathematicians who have worked on this include Newton, Leibniz, Euler, Cayley, Schubert, Salmon, Kronecker and Hilbert. The dual space approach was ﬁrst formulated by Macaulay [21] in 1916 for polynomial ideals. Samuel developed this viewpoint with his Characteristic functions and polynomials now called Hilbert functions and polynomials. More than the multiplicity at a zero of a polynomial system he deﬁnes the multiplicity of an arbitrary local ring [33, Ch. VIII §10], which, in the case of a 0-dimensional local ring, is the sum of the Hilbert function values as in Corollary 1. As we show in §2.4, this multiplicity is also the -dimension of the local ring which is now generally accepted as the standard deﬁnition of multiplicity in commutative algebra for isolated zeros of systems of equations, see Chapter 4 of [4] for a discussion similar to that of this paper. Symbolic computation of Gr¨obner duality on polynomial ideals was initiated by Marinari, Mora and M¨oller [22], as well

as Mourrain [24]. Stetter and Thallinger introduced numerical computation of the dual basis for a polynomial ideal in [28, 31] and in Stetter’s book [29]. Other computational algorithms on the multiplicity problem have recently been proposed in [1], [13], [19], [32], and [36], etc.

## 2.2 The Macaulay matrices

Based on the multiplicity formulation, computing the multiplicity structure can be converted to the rank/kernel problem of matrices. Consider the dual subspace Dxαˆ(F) as deﬁned in (8) for the nonlinear system F = {f1,... ,ft} in s ≤ t variables x = (x1,... ,xs). Similar to Lemma 1, one can show that a functional c = |j|≤α cj ∂j[xˆ] is in the dual subspace Dxαˆ(F) if and only if

c (x − xˆ)kfi(x) ≡

cj · ∂j[xˆ] (x − xˆ)kfi(x) = 0 (17)

|j|≤α

for all |k| ≤ α − 1 and i ∈ {1,... ,s}. By a proper ordering of indices j and (k,i), equation

- (17) can be written in matrix form Sα c = 0 (18)

where c is the vector formed by ordering cj in (17) for j ∈ Ns, j ≥ 0 and |j| ≤ α. The equation

- (18) determines the dual subspace Dxαˆ(F) that is naturally isomorphic to the kernel K(Sα) of the matrix Sα, which we call the α-th order Macaulay matrix.


To construct the Macaulay matrices, we choose the negative degree lexicographical ordering [12], denoted by ≺, on the index set Iα ≡ j ∈ Ns j ≥ 0, |j| ≤ α :

,i ≺ j if |i| < |j|, or

(|i| = |j| and ∃ 1 ≤ σ ≤ s : i1 = j1,... , iσ-1 = jσ-1, iσ < jσ). The Macaulay matrix Sα is of size mα × nα where

α − 1 + s α − 1

α + s α

mα =

and nα =

.

We view the rows to be indexed by (x − xˆ)k fi for (k,i) ∈ Iα−1 × {1,··· ,t} with ordering (k,i) ≺ (k′,i′) if k ≺ k′ in Iα−1 or k = k′ but i < i′, and the columns are indexed by the diﬀerential functionals ∂j for j ∈ Iα. The entry of Sα, at the intersection of the row and column indexed by (x−xˆ)k fi and ∂j respectively, is the value of ∂j[xˆ] (x − xˆ)k fi . With this arrangement, Sα is the upper-left mα ×nα submatrix of subsequent Macaulay matrices Sσ, for σ ≥ α, as illustrated in Example 2. The following corollary is thus straightforward.

- Corollary 1 Let F = {f1,... ,ft} be a system of functions in variables x = (x1,... ,xs) with a


zero xˆ. Then for each α > 0, the dual subspace Dxαˆ(F) is isomorphic to the kernel K(Sα) of the Macaulay matrix Sα. In particular, with S0 ≡ [f1(xˆ),... ,ft(xˆ)]⊤ = 0, the Hilbert function

h(α) = nullity ( Sα ) − nullity ( Sα-1 ) for α = 1,2,··· . (19)

Notice that for an obvious ordering ≺ of I1 and f(xˆ) = [f1(xˆ),... ,ft(xˆ)]⊤, we can arrange

S1 = f(xˆ) J(xˆ) ≡ 0 J(xˆ) (20) where J(xˆ) is the Jacobian of the system {f1,... ,ft} at xˆ.

- Example 2 Consider the system F = {x1 − x2 + x21, x1 − x2 + x22} at xˆ = (0,0). Figure 2 shows the expansion of the Macaulay matrices from S1 to S2, then S3. The table beneath the Macaulay matrices in Figure 2 shows the bases for the kernels as row vectors using the same column indices. It is instructive to compare this pair of arrays to those in [21, §65] or the reconstruction of Macaulay’s arrays in [23, Example 30.4.1]. For this example, the kernels can be converted to bases of dual subspaces using the indices in the table:


D(00 ,0)(F) = span{∂00}, D(01 ,0)(F) = span{∂00, ∂10 + ∂01} D(02 ,0)(F) = span{∂00, ∂10 + ∂01, − ∂10 + ∂20 + ∂11 + ∂02}.

Since nullity (S3 ) = nullity ( S2 ) = 3, the Hilbert function h(N) = {1,1,1,0,··· }. The multiplicity equals 3. The dual space D(0,0)(F) = D(02 ,0)(F) with breadth β(0,0)(F) = h(1) = 1 and depth δ(0,0)(F) = max{α |h(α) > 0} = 2. The complete multiplicity structure is in order.

Macaulay |j| = 0 |j| = 1 |j| = 2 |j| = 3 matrices ց ∂00 ∂10 ∂01 ∂20 ∂11 ∂02 ∂30 ∂21 ∂12 ∂03

![image 57](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile57.png>)

![image 58](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile58.png>)

![image 59](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile59.png>)

![image 60](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile60.png>)

![image 61](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile61.png>)

![image 62](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile62.png>)

![image 63](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile63.png>)

![image 64](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile64.png>)

![image 65](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile65.png>)

![image 66](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile66.png>)

![image 67](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile67.png>)

![image 68](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile68.png>)

![image 69](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile69.png>)

![image 70](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile70.png>)

||=0k

![image 71](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile71.png>)

![image 72](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile72.png>)

![image 73](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile73.png>)

![image 74](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile74.png>)

![image 75](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile75.png>)

![image 76](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile76.png>)

f1 0 1 −1 1 0 0 0 0 0 0

![image 77](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile77.png>)

- S0 f2 0 1 −1 0 0 1 0 0 0 0

![image 78](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile78.png>)

![image 79](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile79.png>)

![image 80](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile80.png>)

![image 81](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile81.png>)

![image 82](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile82.png>)

![image 83](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile83.png>)

![image 84](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile84.png>)

- S1

![image 85](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile85.png>)

![image 86](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile86.png>)

![image 87](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile87.png>)

![image 88](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile88.png>)

![image 89](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile89.png>)

![image 90](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile90.png>)

![image 91](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile91.png>)

![image 92](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile92.png>)

||=1k

- x1f1 0 0 0 1 −1 0 1 0 0 0

![image 93](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile93.png>)

![image 94](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile94.png>)

![image 95](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile95.png>)

![image 96](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile96.png>)

- x1f2 0 0 0 1 −1 0 0 0 1 0 x2f1 0 0 0 0 1 −1 0 1 0 0


![image 97](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile97.png>)

![image 98](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile98.png>)

![image 99](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile99.png>)

![image 100](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile100.png>)

![image 101](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile101.png>)

![image 102](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile102.png>)

![image 103](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile103.png>)

![image 104](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile104.png>)

- S2 x2f2 0 0 0 0 1 −1 0 0 0 1

![image 105](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile105.png>)

![image 106](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile106.png>)

![image 107](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile107.png>)

![image 108](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile108.png>)

![image 109](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile109.png>)

- x21f1 0 0 0 0 0 0 1 −1 0 0

![image 110](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile110.png>)

![image 111](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile111.png>)

![image 112](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile112.png>)

![image 113](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile113.png>)

![image 114](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile114.png>)

||=2k

- x21f2 0 0 0 0 0 0 1 −1 0 0


![image 115](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile115.png>)

![image 116](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile116.png>)

![image 117](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile117.png>)

- x1x2f1 0 0 0 0 0 0 0 1 −1 0

![image 118](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile118.png>)

![image 119](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile119.png>)

![image 120](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile120.png>)

- x1x2f2 0 0 0 0 0 0 0 1 −1 0 x22f1 0 0 0 0 0 0 0 0 1 −1


![image 121](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile121.png>)

![image 122](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile122.png>)

![image 123](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile123.png>)

![image 124](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile124.png>)

![image 125](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile125.png>)

![image 126](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile126.png>)

- S3 x22f2 0 0 0 0 0 0 0 0 1 −1 bases for kernels (transposed as row vectors)


![image 127](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile127.png>)

![image 128](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile128.png>)

![image 129](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile129.png>)

![image 130](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile130.png>)

![image 131](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile131.png>)

![image 132](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile132.png>)

![image 133](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile133.png>)

![image 134](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile134.png>)

![image 135](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile135.png>)

- K(S0) 1 0 0 0 0 0 0 0 0 0

![image 136](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile136.png>)

![image 137](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile137.png>)

![image 138](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile138.png>)

![image 139](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile139.png>)

![image 140](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile140.png>)

![image 141](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile141.png>)

![image 142](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile142.png>)

- K(S1) 0 1 1 0 0 0 0 0 0 0

![image 143](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile143.png>)

![image 144](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile144.png>)

![image 145](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile145.png>)

![image 146](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile146.png>)

![image 147](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile147.png>)

![image 148](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile148.png>)

- K(S2) 0 −1 0 1 1 1 0 0 0 0


![image 149](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile149.png>)

![image 150](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile150.png>)

![image 151](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile151.png>)

![image 152](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile152.png>)

![image 153](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile153.png>)

![image 154](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile154.png>)

![image 155](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile155.png>)

![image 156](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile156.png>)

K(S3)

![image 157](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile157.png>)

Figure 2: Expansion of the Macaulay matrices for the polynomial system in Example 2

By identifying the multiplicity structure of a nonlinear system with the kernels and nullities of Macaulay matrices, the multiplicity computation can be reliably carried out by matrix rankrevealing, as we shall elaborate in §2.3.

## 2.3 Computing the multiplicity structure

The multiplicity as well as the multiplicity structure can be computed using symbolic, symbolicnumeric or ﬂoating point computation based on Corollary 1. The main algorithm can be outlined in the following pseudo-code.

Algorithm: NonlinearSystemMultiplicity Input: system F = {f1,··· ,ft} and isolated zero xˆ ∈ s

- – initialize S0 = Ot×1, K(S0) = span{[1]}, h(0) = 1
- – for α = 1,2,··· do ∗ expand Sα-1 to Sα, and embed K(Sα-1) into K(Sα) ∗ find K(Sα) by expanding K(Sα-1) ∗ if nullity (Sα ) = nullity (Sα-1 ) then

δ = α − 1, h(α) = 0, break the loop otherwise, get h(α) by (19)

end if end do

- – convert K(Sδ) to Dxˆ(F)


Output: multiplicity m = α h(α), the Hilbert function h, Dxˆ(F) basis, depth δxˆ(F), and breadth βxˆ(F) = h(1)

This algorithm turns out to be essentially equivalent to Macaulay’s procedure of 1916 for ﬁnding inverse arrays of dialytic arrays [21, 23], except that Macaulay’s algorithm requires construction of dialytic arrays with full row rank, which is somewhat diﬃcult and costly to implement with inexact systems or the approximate zeros. Implementation of the algorithm NonlinearSystemMultiplicity is straightforward for symbolic computation when the system and zero are exact and properly represented. Applying this multiplicity-ﬁnding procedure on approximate zeros and/or inexact systems requires the notions and algorithms of numerical rank-revealing at the step “ﬁnd K(Sα)” in Algorithm NonlinearSystemMultiplicity.

The numerical rank of a matrix A is deﬁned as the minimum rank of matrices within a threshold θ [9, §2.5.5]: rank θ (A) = min A−B 2≤θ rank (B ). The numerical kernel Kθ (A) of A is the (exact) kernel K(B) of B that is nearest to A with rank ( B ) = rank θ (A). With this reformulation, numerical rank/kernel computation becomes well-posed. We refer to [20] for details.

Numerical rank-revealing applies the iteration [20]

 

† A ∞(uHkuk − 1)

uk+1 = uk − 2 AA ∞uk

Auk ςk+1 = Auk

(21)

+1 2

uk+1 2 , k = 0,1,···



![image 158](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile158.png>)

where (·)† denotes the Moore-Penrose inverse. From a randomly chosen u0, this iteration virtually guarantees convergence to a numerical null vector u, and {ςk} will converge to the distance ς between A and the nearest rank-deﬁcient matrix.

With a numerical null vector u, applying (21) on Aˆ = A A ∞uH yields another sequence {uˆk} that converges to a numerical null vector v of A orthogonal to u, and the sequence {ςˆk} converges to the distance between A and the nearest matrix with nullity 2. This process can be continued by stacking A ∞vH on top of Aˆ and applying (21) on the new stacked matrix.

We now describe the numerical procedure for the step of computing K(Sα) in Algorithm NonlinearSystemMultiplicity. The kernel Kθ (S0 ) = span{[1]}. Assume an orthonormal basis

Y = y1,··· ,yµ for Kθ (Sα-1 ) and the QR decomposition TYS H

= Qα-1 ROα-1 are available,

α-1

- where Qα-1 is unitary, Rα-1 is square upper-triangular and T is a diagonal scaling matrix.


Embedding yi’s into nα by appending zeros at the bottom to form zi for i = 1,··· ,µ, it is clear that the columns of Z = z1,··· ,zµ form a subset of an orthonormal basis for Kθ (Sα ). Also, we have matrix partitions

where FF1

2

Sα =

Sα-1 F O G

,

TZH Sα

=

 

TY H O Sα-1 F

O G

 

  Qα-1

Rα-1 F1

- O F2

![image 159](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile159.png>)

- O G


= QHα-1 OF . Let Qˆ OR ˆ = FG2 be a QR decomposition. Then

 

TZH Sα

= Qα

  = Qα

 

Rα-1 F1 O Rˆ O O

Rα O

with a proper accumulation of Qα-1 and Qˆ into Qα. This implies K(Rα) = K(Sα) K(ZH) = K(Sα) Kθ (Sα-1 )⊥ .

(22)

Therefore Kθ (Rα ) consists of numerical null vectors of Sα that are approximately orthogonal to those of Sα-1. The procedure below produces the numerical kernel Kθ (Rα ).

- • let A = Rα
- • for i = 1,2,··· do


- – apply iteration (21), stop at u and ς with proper criteria
- – if ς > θ, exit, end if
- – get zµ+i = u, reset A with A A ∞uH
- – update the QR decomposition A = QR


end for

Upon exit, vectors zµ+1, ··· , zµ+ν are remaining basis vectors of Kθ (Sα ) aside from previously obtained z1, ··· , zµ. Furthermore, the QR decomposition of T ˆSZˆH

is a by-product from a

α

proper accumulation of orthogonal transformations. Here Zˆ = z1,··· ,zµ+ν with a column permutation and Tˆ is again a scaling matrix.

Algorithm NonlinearSystemMultiplicity is implemented as a function module in the software package ApaTools [35]. For an isolated zero of a given system along with a rank threshold, the software produces the multiplicity, breadth, depth, Hilbert function, and a basis for the dual space. The software performs symbolic (exact) computation when the rank threshold is set to zero, and carries out numerical computation otherwise. An example of computing the multiplicity structure for an inexact system at an approximate zero will be shown as Example 3 in §3.1.

Remarks on computational issues: For an exact system, the accuracy of a zero xˆ can be arbitrarily high using multiprecision or a deﬂation method described in §3. As a result, numerical rank-revealing with suﬃcient low threshold will ensure accurate multiplicity identiﬁcation. For

inexact systems, the approximate zeros may carry substantial errors due to the inherent sensitivity. In this case, setting a proper threshold θ for the numerical rank revealing may become diﬃcult. The depth-deﬂation method given in §3 is eﬀective in calculating the zeros to the highest possible accuracy that may allow accurate identiﬁcation of the multiplicity. However, there will always be intractable cases. For those systems with obtainable multiplicity structure at an approximate solution, the rank threshold needs to be set by users according to the magnitude of errors on the system and solution. Generally, the threshold should be set higher than the size of error.

The size increase of Macaulay matrices may become an obstacle when the number of variables is large, compounding with high depth δxˆ(F). Most notably, when the breadth βxˆ(F) = 1, the depth will reach the maximum: δxˆ(F) = m − 1. In this situation, high order α’s and large sizes of Sα are inevitable. A special case algorithm BreadthOneMultiplicity in §3.3 is developed to deal with this diﬃculty. A recently developed closedness subspace strategy [36] improves the eﬃciency of multiplicity computation substantially by reducing the size of the matrices.

## 2.4 Proofs of Theorem 1 and Theorem 2

Theorem 1 and Theorem 2 are well known for zero-dimensional polynomial systems. Since a zero-dimensional system has only ﬁnitely many zeros, each zero must be isolated in the sense of

- Deﬁnition 2 so the content of these theorems is simply the classical result that dim Dxˆ(F) is identical to the intersection multiplicity, c.f. [10, 16, 21], along with more recent expositions by Emsalem [7], Mourrain [24] and Stetter [29].


However these results in the case of analytic systems and nonzero-dimensional polynomial systems with isolated zeros are well known mainly in the folklore of the theory of analytic functions of several complex variables. We are not aware of an explicit reference in this generality. The results do follow easily, however, from the considerations of the last two sections and accessible facts from the literature (e.g. [30]). Therefore this section is a short digression sketching our proof of Theorems 1 and 2 and stating a few useful corollaries of these Theorems.

We will assume in this section that xˆ = 0 is the origin. The local ring of system F = {f1,... ,ft} of analytic functions at 0 is A = {x1,... ,xs}/F {x1,... ,xs} where {x1,... ,xs} is the ring of all complex analytic functions in the variables x1,... ,xs which converge in some neighborhood of 0 (c.f. [4, 30]). This last ring has a unique maximal ideal M generated by {x1,... ,xs}, the image of which in A is the unique maximal ideal m of A.

We will need some notations and lemmas. For an analytic or polynomial function deﬁne jet(f,k) = |j|≤k cjxj (23)

where cj xj is the term involving xj in the Taylor series expansion of f at 0. We say that a homogeneous polynomial h of total degree α is the initial form of order α of analytic or polynomial function f if h = jet(f,α).

- Lemma 2 Let R be the ring of analytic functions on open set U ⊆ s and assume xˆ = 0 ∈ U.


Let F = {f1,... ,ft} ⊂ R be a system of analytic functions with common zero xˆ. Then the following are equivalent:

- (i) The point xˆ = 0 ∈ U is an isolated zero of F.
- (ii) The local ring A is a ﬁnite dimensional -algebra.


- (iii) There is a positive integer δ such that for all |j| > δ the monomial xj is the initial form of order |j| of some element in F [x1,... ,xs].


Proof. To prove (i) implies (ii), use Ru¨kert’s Nullstellensatz [30] to conclude that a power of the maximal ideal M lies in F {x1,... ,xs}, i.e. mα = 0 for large α. But in the ﬁltration

A = m0 ⊇ m1 ⊇ m2 ⊇ ... (24)

each quotient mα/mα+1 is a vector space of ﬁnite dimension. In this case the ﬁltration is ﬁnite, hence dim(A) is ﬁnite.

Assuming (ii) then (24) must terminate and, by Nakayama’s Lemma [30], some mδ+1 = 0. Consequently xj ∈ F {x1,... ,xs} for all |j| > δ. Then each such xj ∈ F {x1,... ,xs} satisﬁes xj = g1f1 + ··· + gtft for some g1,... ,gt in {x1,... ,xs}. A straightfoward argument shows that xj is the initial form of jet(g1,α)f1 + jet(g2,α)f2 + ··· + jet(gt,α)ft ∈ F [x1,... ,xs] where α = |j|, proving (iii).

Finally an argument using Schwartz’s Lemma [30, Exercise 4, p.35] gives (iii) implies (i).

- Lemma 3 The Macaulay matrix Sα of the system F is row equivalent to a matrix with linearly independent rows 




![image 160](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile160.png>)

rowspace Sα−1 Bα

 . (25)

 

![image 161](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile161.png>)

![image 162](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile162.png>)

0 Cα

Moreover, every row of the matrix block Cα can be associated with the intitial form of certain element of F [x1,... ,xs] by multiplying the entries by their column index and adding, and these forms give a basis of the space of all initial forms of order α on F [x1,... ,xs].

The proof follows from the construction of Sα. We can now prove Theorem 1 and Theorem 2.

- Proof of Theorem 1: By Lemma 2, xˆ is an isolated zero if and only if there exists δ with

each monomial xj with |j| > δ being an initial form of some element of F [x1,... ,xs]. Since the product of a monomial and an initial form is again an initial form, it is necessary and suﬃcient that all monomials of speciﬁc degree α = δ + 1 are initial forms of F [x1,... ,xs]. By

- Lemma 3 this will happen if and only if Cα in (25) is of full column rank. This is equivalent to nullity (Sα ) = nullity (Sα−1 ) which by Corollary 1 is equivalent to dim(Dxαˆ−1(F)) = dim(Dxαˆ(F)). By the closedness condition this is equivalent to dim(Dxαˆ−1(F)) = dim(Dxβˆ(F)) for all β ≥ α or supα≥0 dim(Dxαˆ(F)) < ∞.


- Proof of Theorem 2: From (24), dim(A) = ∞α=0 mα/mα+1. On the other hand, from Corollary


1 and Lemma 3, dim(Dxαˆ(F)) is the sum of the dimensions of the space of initial forms of order α, α = 0,1,... . From the proof of [11, Prop. 5.5.12], it follows that mα/mα+1 is isomorphic to the

space of initial forms of order α and so dim(Dxαˆ(F)) = dim(A) where A is the local ring of the system F at xˆ = 0. This latter dimension is commonly known as the intersection multiplicity.

Furthermore, the proof above leads to the following Depth Theorem for an isolated zero.

- Corollary 2 (Depth Theorem) Let F = {f1,... ,ft} be a system of analytic functions in an open set of s at an isolated zero xˆ = 0. Then there is a number δ = δxˆ(F) called the depth of the isolated zero xˆ satisfying the following equivalent conditions.

- (i) δ is the highest diﬀerential order of a functional in Dxˆ(F).
- (ii) δ is the smallest integer so that the Macaulay matrix Sδ+1 is row equivalent to a matrix

R B 0 C where C is the n × n identity matrix, where n = s δ−+1s .

- (iii) δ is the smallest integer such that xj is the initial form of some element of F [x1,... ,xs] for all |j| > δ.


Remark: In commutative algebra the term regularity index, nil-index or just index is used instead of our depth. In particular the index of the ideal of the system F is δxˆ(F) + 1.

- Corollary 3 As in Deﬁnition 1, let F = {f1,... ,ft} be a system of functions having derivatives


of order γ ≥ 1 at the zero xˆ ∈ s. If Dxγˆ(F) = Dxγˆ-1(F), then the polynomial system jet(F,γ) has the same multiplicity structure, and hence the same multiplicity at xˆ as F.

Proof. The system jet(F,γ) has the same Macaulay matrices up to γ = δxˆ(jet(F,γ)) as the system F and hence Dxαˆ(F) = Dxαˆ(jet(F,γ) by Corollary 1. Note, in particular, that this Corollary applies to any analytic system with an isolated zero, so such a system is locally equivalent to a polynomial system.

# 3 Accurate computation of a multiple zero by deﬂating its depth

It is well known that multiple zeros are highly sensitive to perturbations and are therefore diﬃcult to compute accurately using ﬂoating point arithmetic. Even for a single univariate equation f(x) = 0, as mentioned before, there is a perceived barrier of “attainable accuracy”: The number of attainable digits at a multiple zero is bounded by the hardware precision divided by the multiplicity. This accuracy barrier is largely erased recently in [34] for univariate polynomial equations. For general nonlinear multivariate systems, we propose a general depth-deﬂation method as well as its special case variation for breadth one systems in this section for accurate computation of multiple zeros without extending hardware precision even when the given system is perturbed.

## 3.1 The depth-deﬂation method

The hypersensitivity in calculating an approximation x˜∗ to an m-fold zero x∗ can be illustrated by solving f(x) = xm = 0. When the function is perturbed slightly to fε(x) = xm − ε, the error becomes |x˜∗ − x∗| = |f − fε|m1 . The asymptotic condition number is supε>0 |x|˜f∗−−fx∗|

ε| = ∞ when the multiplicity m > 1. Consequently, multiple zeros are referred to as “singular” or “inﬁnitely sensitive” to perturbations in the literature. On the other hand, a simple zero is considered “regular” with a ﬁnite condition number as stated in the following lemma.

![image 163](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile163.png>)

![image 164](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile164.png>)

- Lemma 4 Let f be a system of s-variate functions that are twice diﬀerentiable in a neighborhood of xˆ ∈ s. If the Jacobian J(xˆ) of f(x) at xˆ is injective so that J(xˆ)+ 2 < ∞, then


x ˜ − xˆ 2 ≤ J(xˆ)+ 2 f(x˜) − f(xˆ) 2 + O f(x˜) − f(xˆ) 22 (26)

for x˜ suﬃciently close to xˆ.

Proof. The injectiveness of J(xˆ) implies t ≥ s and rank ( J(xˆ)) = s. Without loss of generality, we assume the submatrix of J(xˆ) consists of its ﬁrst s rows is invertible. By the Inverse Function Theorem, the function [y1,... ,ys]H = [f1(x),... ,fs(x)]H has a continuously diﬀerentiable inverse x = g(y1,... ,ys) in a neighborhood of [ˆy1,... ,yˆs]H = [f1(xˆ),... ,fs(xˆ)]H, permitting x − xˆ 2 ≤ C f(x) − f(xˆ) 2 for x in a neighborhood of xˆ. Since

f(x) − f(xˆ) = J(xˆ)(x − xˆ) + r(x) or x − xˆ = J(xˆ)+ f(x) − f(xˆ) − r(x) where r(x) 2 = O x − xˆ 22 = O f(x) − f(xˆ) 22 , we thus have (26). In light of Lemma 4, we may deﬁne the condition number of the system f at a zero xˆ:

J(xˆ)+ 2 if J(xˆ) is injective ∞ otherwise.

κf(xˆ) =

This condition number serves as a sensitivity measurement in the error estimate

(27)

x ˜ − xˆ 2 ≈ κf(x˜) · f(x˜) 2 (28) of the approximate zero x˜ using the residual f(x˜) 2.

Solving a nonlinear system for a multiple zero is an ill-posed problem in the sense that its condition number is inﬁnity [6, Deﬁnition 1.1, p.17]. The straightforward Newton’s iteration attains only a few correct digits of the zero besides losing its quadratic convergence rate, if it converges at all. Similar to other ill-posed problems, accurate computation of a multiple zero needs a regularization procedure. An eﬀective regularization approach is deﬂation [17, 18, 25]. For instance, Leykin, Verschelde and Zhao [17] propose a deﬂation method and a higher-order deﬂation method [18] which successfully restore the quadratic convergence of Newton’s iteration. From our perspective, perhaps the most important feature of deﬂation strategy should reside in transforming an ill-posed zero-ﬁnding into a well-posed least squares problem. As a result, the multiple zero can be calculated to high accuracy.

We hereby propose two new versions of the deﬂation method, both are refered to as depth-deﬂation methods, with one for the general cases and the other for the cases where the breadth of the system is one at the zero. We ﬁrst derive our general depth-deﬂation method here. The version for breadth-one systems follows in §3.3.

Let f : s −→ t represent a nonlinear system f(x) = 0 where f(x) = [f1(x),··· ,ft(x)]⊤, x = (x1,... ,xs) ∈ s with t ≥ s, and xˆ be an isolated zero of f(x). Denote J(x) as the Jacobian of f(x). If xˆ is a simple zero, then J(xˆ) is injective with pseudo-inverse J(xˆ)+ = [J(xˆ)HJ(xˆ)]-1J(xˆ)H, and the Gauss-Newton iteration

x(n

+1) = x(n) − J(x(n))+ f(x(n)) for n = 0,1,... (29)

locally converges to xˆ at a quadratic rate. More importantly in this regular case, solving f(x) = 0 for the solution xˆ is a well-posed problem and the condition number J(xˆ)+ < ∞.

- When xˆ is a multiple zero of the system f, however, the Jacobian J(xˆ) is rank-deﬁcient. In this singular case, the zero xˆ is underdetermined by the system f(x) = 0 because it is also a


solution to J(x)y = 0 for some y = 0. In order to eliminate the singularity and thus to curb the hypersensitivity, perhaps further constraints should be imposed.

Let n1 = nullity (J(xˆ)) which is strictly positive at the multiple zero xˆ. Denote x1 = x and xˆ1 = xˆ. Then, for almost all choices of an n1 ×s random matrix R1, the matrix J(Rxˆ1)

is of full (column) rank. It is easy to see that the linear system JR(xˆ1)

1

0 e1 has a unique solution

x2 =

1

x2 = xˆ2 = 0. Here e1 is the ﬁrst canonical vector [1,0,... ,0]⊤ of a proper dimension. As a result, (xˆ1,xˆ2) is an isolated zero of a new (2t + k) × (2s) system

 

 . (30)

f(x1) J(x1) R1

f1(x1,x2) ≡

0 e1

x2 −

If (xˆ1,xˆ2) is a simple zero of f1(x1,x2), then the singularity of f(x) at xˆ is “deﬂated” by solving f1(x1,x2) = 0 for (xˆ1,xˆ2) as a well-posed problem using the Gauss-Newton iteration (29) on f1. However, (xˆ1,xˆ2) may still be a multiple zero of f1(x1,x2) and, in this case, we can repeat the depth-deﬂation method above on f1. Generally, assume (xˆ1,... ,xˆ2α) is an isolated multiple zero of fα(x0,... ,x2α) after α steps of depth-deﬂation with a Jacobian Jα(xˆ1,... ,xˆ2α) of nullity nα > 0. The next depth-deﬂation step expands the system to

fα+1(x1,... ,x2α+1) ≡



 

fα(x1, . . . , x2α) Jα(x1, . . . , x2α) Rα+1

  

x2α+1

. .

x2α+1

   −

0 e1



  (31)

- where Rα+1 is a randomly selected matrix of nα+1 rows and the same number of columns as Jα(x1,... ,x2α). The depth-deﬂation process continues by expanding f(x1) to f1(x1,x2), f2(x1,... ,x4), ... until reaching an expanded system fσ(x1,x2,... ,x2σ) with an isolated zero (xˆ1,... ,xˆ2σ) that is no longer singular. The following Depth Deﬂation Theorem ensures the deﬂation process will terminate and the number of deﬂation steps is bounded by the depth δxˆ(f).


- Theorem 4 (Depth Deﬂation Theorem) Let xˆ be an isolated zero of a system f with depth δxˆ(f). Then there is an integer σ ≤ δxˆ(f) such that the depth-deﬂation process terminates at the expanded system fσ(x1,... ,x2σ) with a simple zero (xˆ1,... ,xˆ2σ) where xˆ1 = xˆ. Furthermore, the depth-deﬂation method generates 2σ diﬀerential functionals in the dual space Dxˆ(f).


We shall prove this Depth Deﬂation Theorem via multiplicity analysis in §3.2.

For polynomial systems, Leykin, Verschelde and Zhao proved that each deﬂation step of their method deﬂates intersection multiplicity by at least one [17, Theorem 3.1]. Theorem 4 improves the deﬂation bound substantially since the depth is much smaller than the multiplicity when the breath is larger than one. The computing cost increases exponentially as the depth-deﬂation continues since each depth-deﬂation step doubles the number of variables. Fortunately, computing experiments suggest that, for a multiple zero of breadth larger than one, very few depth-deﬂation steps are required. At breadth-one zeros, we shall derive a special case deﬂation method in §3.3. The high accuracy achieved by applying the depth-deﬂation method can be illustrated in the following examples.

- Example 3 Consider the system

 



- (x − 1)3 + .416146836547142 (z − 3)sin y + .909297426825682 (z − 3)cos y = 0
- (y − 2)3 + .989992496600445 (x − 1)sin z + .141120008059867 (x − 1)cos z = 0
- (z − 3)3 − .540302305868140 (y − 2)sin x + .841470984807897 (y − 2)cos x = 0


(32)

which is a perturbation of magnitude 10-15 from an exact system {u3 + w sin v = v3 + u sin w = w3 + v sin u = 0} with u = x − 1, v = y − 2 and w = z − 3. This system has a zero (1,2,3) of multiplicity 11, depth 4 and breadth 3. Using 16-digit arithmetic in Maple to simulate the hardware precision, Newton’s iteration without depth-deﬂation attains only 4 correct digits, whileas a single depth-deﬂation step eliminates the singularity and obtains 15 correct digits, as shown in the following table. The error estimates listed in the table are calculated using (28) which provides an adequate accuracy measurement for the computed zeros.

![image 165](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile165.png>)

![image 166](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile166.png>)

![image 167](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile167.png>)

![image 168](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile168.png>)

![image 169](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile169.png>)

without deﬂation with deﬂation exact value x 1.0003 0.999999999999999 1.0

![image 170](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile170.png>)

![image 171](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile171.png>)

![image 172](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile172.png>)

![image 173](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile173.png>)

![image 174](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile174.png>)

![image 175](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile175.png>)

![image 176](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile176.png>)

![image 177](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile177.png>)

![image 178](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile178.png>)

![image 179](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile179.png>)

![image 180](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile180.png>)

![image 181](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile181.png>)

![image 182](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile182.png>)

![image 183](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile183.png>)

![image 184](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile184.png>)

![image 185](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile185.png>)

zero y 1.9997 1.999999999999999 2.0

![image 186](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile186.png>)

![image 187](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile187.png>)

![image 188](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile188.png>)

![image 189](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile189.png>)

![image 190](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile190.png>)

![image 191](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile191.png>)

![image 192](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile192.png>)

![image 193](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile193.png>)

![image 194](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile194.png>)

z 3.0003 3.000000000000000 3.0 error estimate 0.00027 0.000000000000019

![image 195](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile195.png>)

![image 196](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile196.png>)

![image 197](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile197.png>)

![image 198](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile198.png>)

![image 199](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile199.png>)

![image 200](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile200.png>)

![image 201](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile201.png>)

![image 202](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile202.png>)

![image 203](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile203.png>)

![image 204](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile204.png>)

![image 205](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile205.png>)

![image 206](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile206.png>)

![image 207](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile207.png>)

![image 208](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile208.png>)

![image 209](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile209.png>)

Since the estimated error of the approximate zero is 1.94 × 10-14, we set the rank threshold to be slightly larger: 10−12. Algorithm NonlinearSystemMultiplicity accurately produces the multiplicity 11, breadth 3, depth 4, Hilbert function {1,3,3,3,1,0,.. . ,} and (approximate) dual basis

∂000, ∂100, ∂010, ∂001, ∂200, ∂020, ∂002, .707106781186544 ∂101 + .707106781186543 ∂030,

.707106781186544 ∂011 + .707106781186545 ∂300, .707106781186545 ∂110 + .707106781186545 ∂003,

.500000000000008 ∂111 + .500000000000007 ∂400 + .500000000000009 ∂040 + .500000000000008 ∂004.

- Example 4 Consider the system


ez − .944956946314738 cos y + .327194696796152 sin y = 0 z2 − y3 − y2 − .333333333333333 y − .0370370370370370 = 0

y2 + .666666666666667 y + .148148148148148 − x3 + x2 − .333333333333333 x = 0.

This is a perturbation of magnitude 10-15 from an exact system ez−cos y+ 13 = z2−(y+ 13 3 = (y + 13 2 −(x− 31 3 = 0 with zero (1/3,−1/3,0) of multiplicity 9, depth 5, breadth 2 and Hilbert function {1,2,2,2,1,1,0, .. .}. Again, using 16-digits arithmetic in Maple, Newton’s iteration diverges from the initial iterate (0.31,−0.31,0.01). In contrast, our depth-deﬂation method takes three deﬂation steps to eliminate the singularity and obtains 15 correct digits of the multiple zero:

![image 210](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile210.png>)

![image 211](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile211.png>)

![image 212](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile212.png>)

![image 213](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile213.png>)

![image 214](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile214.png>)

![image 215](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile215.png>)

![image 216](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile216.png>)

![image 217](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile217.png>)

![image 218](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile218.png>)

![image 219](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile219.png>)

![image 220](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile220.png>)

![image 221](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile221.png>)

![image 222](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile222.png>)

![image 223](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile223.png>)

![image 224](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile224.png>)

without deﬂation with deﬂation exact value x diverges 0.3333333333333336 1/3

![image 225](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile225.png>)

![image 226](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile226.png>)

![image 227](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile227.png>)

![image 228](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile228.png>)

![image 229](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile229.png>)

![image 230](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile230.png>)

![image 231](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile231.png>)

![image 232](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile232.png>)

![image 233](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile233.png>)

![image 234](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile234.png>)

![image 235](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile235.png>)

![image 236](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile236.png>)

![image 237](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile237.png>)

![image 238](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile238.png>)

![image 239](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile239.png>)

![image 240](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile240.png>)

![image 241](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile241.png>)

zero y diverges -0.3333333333333334 −1/3

![image 242](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile242.png>)

![image 243](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile243.png>)

![image 244](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile244.png>)

![image 245](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile245.png>)

![image 246](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile246.png>)

![image 247](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile247.png>)

![image 248](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile248.png>)

![image 249](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile249.png>)

z diverges 0.0000000000000002 0 error estimate —– 0.0000000000001950

![image 250](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile250.png>)

![image 251](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile251.png>)

![image 252](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile252.png>)

![image 253](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile253.png>)

![image 254](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile254.png>)

![image 255](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile255.png>)

![image 256](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile256.png>)

![image 257](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile257.png>)

![image 258](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile258.png>)

## 3.2 Multiplicity analysis of the depth-deﬂation method

We shall use some additional diﬀerential notations and operations. The original variables x = [x1,··· ,xs]⊤ will be denoted by x1 in accordance with the notation for the auxiliary (vector) variables x2, x3, ... etc. For any ﬁxed or variable vector y = [y1,··· ,ys]⊤, the directional diﬀerentiation operator along y is deﬁned as

+ ··· + ys∂x∂

∇y ≡ y1∂x∂

. (33)

![image 259](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile259.png>)

![image 260](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile260.png>)

s

1

- When y is ﬁxed in s, ∇y induces a functional ∇y[xˆ] : p −→ (∇yp)(xˆ). For any variable


⊤

- u = [u1,··· ,us]⊤, the gradient operator ∆u ≡ ∂u ∂1, ··· , ∂u∂


, whose “dot product” with a vector v = [v1,··· ,vs]⊤ is deﬁned as

![image 261](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile261.png>)

![image 262](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile262.png>)

s

+ ··· + vs∂u∂

v · ∆u ≡ v1∂u∂

. (34)

![image 263](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile263.png>)

![image 264](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile264.png>)

s

1

In particular, ∇y ≡ y · ∆x ≡ y · ∆x1 for any y of dimension s. Let y and z be auxiliary variables. Then, for any function f(x),

(y · ∆x1)(∇zf(x1)) = ∇y∇zf(x1), z · ∆yf(x1) ≡ 0, (z · ∆y)(∇yf(x1)) = (z · ∆y)(y · ∆x1)f(x1) = ∇zf(x1).

(35)

Let f0(x1) ≡ f(x) = [f1(x),··· ,ft(x)]⊤ be a nonlinear system in variable vector x and J0(x) be its Jacobian matrix. Then

J0(x)z =

  z =

  

∆xf1(x)⊤ . ∆xft(x)⊤

   = ∇zf(x1).

  

z · ∆xf1(x) . z · ∆xft(x)

The ﬁrst depth-deﬂation step expands the system to f1(x1,x2) = 0 with

f1(x1,x2) ≡

 

f0(x1) J0(x1) R1

x2 −

0 e1

  ≡

 

 , (36)

f0(x1) ∇x2f0(x1) R1x2 − e1

- where R1 is a random matrix whose row dimension equals to the nullity of J0(x1). The values of

x2 = xˆ2 = 0 induce a functional ∇xˆ2[xˆ1] ∈ Dxˆ(f). If the zero (xˆ1,xˆ2) of f1 remains multiple, then the Jacobian J1(xˆ1,xˆ2) of f1(x1,x2) at (xˆ1,xˆ2) has a nullity k1 > 0 and a nontrivial kernel. The depth-deﬂation process can be applied to f1 the same way as (36) applied to f0. Namely, we seek a zero (xˆ1,xˆ2,xˆ3,xˆ4) to the system

f2(x1,x2,x3,x4) =

 

f1(x1, x2) J1(x1, x2) R2

x3 x4 −

0 e1

 

- where R2 is any matrix of size k1 × 2s that makes


J1(x1,x2) R2

full rank. By (33) – (35), equation J1 x1,x2

x3 x4 = 0 implies

 

  =

(x3 · ∆x1)f0(x1) + (x4 · ∆x2)f0(x1) (x3 · ∆x1)∇x2f0(x1) + (x4 · ∆x2)∇x2f0(x1) (x3 · ∆x1)(R1x2 − e1) + (x4 · ∆x2)(R1x2 − e1)

  = 0. (37)

 

∇x3f0(x1) (∇x3∇x2 + ∇x4)f0(x1)

R1x4

Thus, the second depth-deﬂation seeks a solution (xˆ1,xˆ2,xˆ3,xˆ4) to equations

f0(x1) = 0, ∇x2f0(x1) = 0, ∇x3f0(x1) = 0, (∇x3∇x2 + ∇x4)f0(x1) = 0. (38) It is important to note that xˆ3 = 0. Otherwise, from (37)

∇xˆ4f0(xˆ1)

R1xˆ4 ≡ J0R(xˆ1)

x ˆ4 = 0,

1

which would lead to xˆ4 = 0, making it impossible for R2 xxˆ ˆ3

4

= e1.

After α depth-deﬂation steps, in general, we have an isolated zero (xˆ1,··· ,xˆ2α) to the expanded system fα(x1,··· ,x2α) with Jacobian Jα(x1,··· ,x2α) of rank rα. If rα < 2αs, then the next depth-deﬂation step seeks a zero to fα+1(x1,··· ,x2α+1) = 0 deﬁned in (31).

- Lemma 5 Let f0(x1) ≡ f(x) be a system of t functions of s variables with a multiple zero xˆ1 = xˆ. Assume the depth-deﬂation process described above reaches the extended system fα+1 in


(31) with isolated zero (xˆ1,··· ,xˆ2α+1). Then xˆ2j+1 = 0, j = 0,1,··· ,α.

Proof. The assertion is true for j = 0 and j = 1 as shown above. Let

Then

  

- x1 . .
- x2α−1


y =

  

  , z =

- x2α−1+1

. .

- x2α−1+2α−1


Jα(y,z) uv =

together with u = 0 would imply

  , u =

  

- x2α+1

. .

- x2α+2α−1


  

  , v =

- x2α+2α−1+1

. .

- x2α+2α−1+2α−1


  .

 

  = 0 (39)

u · ∆yfα-1(y) [(u · ∆y)(z · ∆y) + (v · ∆y)]fα-1(y) Rα-1v

Jα(yˆ,zˆ) v 0 =

and thereby v = 0 since JαR-1(yˆ)

α-1

 

  =

0 (v · ∆yˆ)fα-1(yˆ)

Rα-1v

 

 v = 0

0 Jα-1(yˆ) Rα-1

is of full column rank. Therefore

⊤

uˆ = x ˆ⊤2α+1,··· ,xˆ⊤2α+2α−1

= 0. (40) Moreover, from (39)

0 = uˆ · ∆yfα-1(yˆ) ≡ Jα-1(yˆ)uˆ. (41) It now suﬃces to show that for all η,

  

Jη(xˆ1,··· ,xˆ2η)

   = 0 and

- w1

.

- w2η


  

   = 0 (42)

- w1

.

- w2η


would imply w1 = 0. Obviously, this is true for η = 1. Assume it is true up to η − 1. Then, using the same argument for (40) and (41), we have (42) implying

  

- w1

.

- w2η−1


   = 0 and Jη−1

  

- w1

.

- w2η−1


   = 0.

Thus w1 = 0 from the induction assumption. It is clear that the third depth-deﬂation, if necessary, adds variables x5, x6, x7, x8 and equations

∇x5f(x1) = 0, (∇x5∇x2 + ∇x6)f(x1) = 0, (∇x5∇x3 + ∇x7)f(x1) = 0, (∇x5∇x3∇x2 + ∇x5∇x4 + ∇x3∇x6 + ∇x7∇x2 + ∇x8)f(x1) = 0.

(43)

Any solution (xˆ1,··· ,xˆ8) ∈ 8s to (38) and (43) induces eight diﬀerential functionals

1, ∇xˆ2, ∇xˆ3, ∇xˆ5, ∇xˆ3∇xˆ2 + ∇xˆ4, ∇xˆ5∇xˆ2 + ∇xˆ6, ∇xˆ5∇xˆ3 + ∇xˆ7, ∇xˆ5∇xˆ3∇xˆ2 + ∇xˆ5∇xˆ4 + ∇xˆ3∇xˆ6 + ∇xˆ7∇xˆ2 + ∇xˆ8

that vanish on f at xˆ1. In general, the α-th depth-deﬂation step produces a collection of 2α diﬀerential functionals of order α or less that vanish on the system f at xˆ1. Also notice that the highest order diﬀerential terms are

∇xˆ2 ≡ ∇xˆ

, ∇xˆ3∇xˆ2 ≡ ∇xˆ

∇xˆ

, ∇xˆ5∇xˆ3∇xˆ2 ≡ ∇xˆ

∇xˆ

∇xˆ

20+1

21+1

20+1

22+1

21+1

20+1

for depth-deﬂation steps 1, 2 and 3, respectively. Actually these functionals induced by the depth-deﬂation method all belong to the dual space Dxˆ(f). To show this, we deﬁne diﬀerential operators Φα, α = 1,2,··· as follows.

2ν

Φν+1 =

x2ν+ζ · ∆xζ, ν = 0,1,··· . (44)

ζ=1

Speciﬁcally, Φ1 = x2·∆x1, Φ2 = x3·∆x1+x4·∆x2 and Φ3 = x5·∆x1+x6·∆x2+x7·∆x3+x8·∆x4. For convenience, let Φ0 represent the identity operator. Thus

Φ0f(x1) = f(x1), Φ1f(x1) = ∇x2f(x1), Φ2f(x1) = ∇x3f(x1), Φ2 ◦ Φ1f(x1) = (x3 · ∆x1)∇x2f(x1) + (x4 · ∆x2)∇x2f(x1) = (∇x3∇x2 + ∇x4)f(x1)

etc. For any expanded system fα(x1,··· ,x2α) generated in the depth-deﬂation process, its Jacobian Jα(x1,··· ,x2α) satisﬁes

   = Φα+1fα(x1,··· ,x2α).

  

- x2α+1

.

- x2α+2α


Jα(x1,··· ,x2α)

It is easy to see that (38) and (43) can be written as

Φ0f(x1) = 0, Φ1f(x1) = 0, Φ2f(x1) = 0, Φ2 ◦ Φ1f(x1) = 0, Φ3f(x1) = 0, Φ3 ◦ Φ1f(x1) = 0, Φ3 ◦ Φ2f(x1) = 0, Φ3 ◦ Φ2 ◦ Φ1f(x1) = 0.

As a consequence, Theorem 4 given in §3.1 provides an upper bound, the depth, on the number of depth-deﬂation steps required to regularize the singularity at the multiple zero. This bound substantially improves the result in [17, Theorem 3.1]. In fact, our version of the deﬂation method deﬂates depth rather than the multiplicity as suggested in [17].

Proof of Theorem 4. We ﬁrst claim that the α-th depth-deﬂation step induces all diﬀerential functionals

f −→ Φµ1 ◦ ··· ◦ Φµk f (x

1,···,x2α)=(xˆ1,···,xˆ2α) with α ≥ µ1 > µ2 > ··· > µk ≥ 0 (45)

and 1 ≤ k ≤ α that vanish on f. This is clearly true for α = 1 since f1(x1,x2) = 0 induces Φ0f(x1) = Φ1f(x1) ≡ Φ1Φ0f(x1) = 0 at (x1,x2) = (xˆ1,xˆ2). Assume the claim is true for α − 1. At the α-th depth-deﬂation, consider a functional (45). If µ1 < α, then such a functional has already been induced from solving fα−1 = 0. On the other hand, if µ1 = α, then Φµ2 ◦ ··· ◦ Φµkf(x1) = 0, for α − 1 ≥ µ2 > ··· > µk ≥ 0 is in fα−1 = 0. Therefore Φαfα−1 induces the functional in (45). Next, the functional in (45) satisﬁes closedness condition (11). To show this, let p be any polynomial in variables x. By applying the product rule Φα(f g) = (Φα f)g + (Φα g)f in an induction,

pη1···ηjΦη1 ◦ ··· ◦ Φηjfi

Φµ1 ◦ ··· ◦ Φµk(pfi) =

{η1,···,ηj}⊂{µ1,···,µk}

where η1 > ··· > ηj and pη1···ηj is a polynomial generated by applying Φj’s on p. Therefore Φµ1◦···◦Φµk(pfi) = 0 at (xˆ1,··· ,xˆ2α) since Φη1◦···◦Φηjfi = 0, showing that functionals (45) all belong to Dxˆ(f). Finally, the highest order part of the diﬀerential functional Φα ◦ Φα−1 ◦ ··· ◦ Φ1 is αj=0−1(xˆ2j+1 · ∆x) ≡ αj=0−1 ∇xˆ

which is of order α since xˆ2j+1 = 0 by Lemma 5. However, diﬀerential orders of all functionals in Dxˆ(f) are bounded by δxˆ(f), so is α.

2j+1

In general, Theorem 4 does not guarantee those 2k functionals are linearly independent. From computing experiments, the number k of depth-deﬂation steps also correlates to the breadth βxˆ(f). Especially when βxˆ(f) = 1, it appears that k always reaches its maximum. This motivates the special case breadth-one algorithm which will be presented in §3.3. On the other hand, when breadth βxˆ(f) > 1, very frequently the depth-deﬂation process pleasantly terminates only after one depth-deﬂation step regardless of the depth or multiplicity. A possible explanation for such a phenomenon is as follows. At each depth-deﬂation step, say the ﬁrst, the isolated zero zˆ to the system (36) is multiple only if there is a diﬀerential functional in the form of ∇x3∇x2 + ∇x4 in Dx2ˆ(f) while R1x2 = e1 and R1x4 = 0 for a randomly chosen R1. In most of the polynomial systems we have tested, functionals in this special form rarely exist in Dx2ˆ(f) when βxˆ(f) > 1. If no such functionals exist in Dx2ˆ(f), the zero zˆ must be a simple zero of F˜ in (36) according to

- Theorem 4, therefore the depth-deﬂation ends at k = 1 step.


## 3.3 Special case: dual space of breadth one

Consider a nonlinear system f = [f1,··· ,ft]⊤ having breadth one at an isolated zero xˆ, namely βxˆ(f) = 1. The Hilbert function is {1,1,··· ,1,0,··· }, making the depth one less than the multiplicity: δxˆ(f) = dim Dxˆ(f) − 1. This special case includes the most fundamental univariate equation f(x) = 0 at a multiple zero. As mentioned above, the general depth-deﬂation method derived in §3.1 always exhausts the maximal number of steps in this case, and the ﬁnal system is expanded undesirably from t×s to over (2m−1t)×(2m−1s) at an m-fold zero. To overcome this exponential growth of the system size, we shall modify the depth-deﬂation process for breadth-one system in this section so that the regularized system is of size close to (mt) × (ms), and upon solving the system, a complete basis for the dual space Dxˆ(f) is obtained as a by-product.

Denote x = x1 and the zero xˆ = xˆ1 as in §3.1. It follows from (20), the breadth βxˆ(f) = h(1) = nullity (J0(xˆ1)) = 1 implies system (36), simplifying to J0b(xˆH1) x2 = 01 in the variable vector x2, has a unique solution xˆ2 ∈ s for randomly chosen vector b ∈ s. Similar to the

general depth-deﬂation method in § 3.1, the ﬁrst step of depth-deﬂation is to expanded the system:

g1 (x1,x2) = hh0(x1)

1(x1,x2) (46) where h0(x1) ≡ f(x) and h1(x1,x2) = Jb0H(xx1)x2

2f(x1) bHx2 − 1 .

2 −1 ≡ ∇x

The system g1(x1,x2) has an isolated zero (xˆ1,xˆ2). If the Jacobian J1(x1,x2) of g1(x1,x2) is of full rank at (xˆ1,xˆ2), then the system is regularized and the depth-deﬂation process terminates. Otherwise, there is a nonzero vector (v1,v2) ∈ 2s such that

 

  = 0. (47)

∇v1f(xˆ1) (∇v1∇xˆ2 + ∇v2)f(xˆ1) bHv2

J1(xˆ1,xˆ2) vv1

≡

2

Since the Jacobian J0(xˆ) of f at xˆ1 is of nullity one, there is a constant γ ∈ such that

- v1 = γxˆ2. Equation (47) together with βxˆ0(f) = 1 and (v1,v2) = (0,0) imply γ = 0. Consequently we may choose γ = 1, namely v1 = xˆ2. Setting xˆ3 = v2, the system


g2(x1,x2,x3) ≡

 





f(x1) ∇x2f(x1) bHx2 − 1

  =

- h0(x1)
- h1(x1, x2)
- h2(x1, x2, x3)


 

 

(∇x2∇x2 + ∇x3)f(x1) bHx3

2∇x2 + ∇x3)f(x1) bHx3

where h2(x1,x2,x3) = (∇x

(48)

has an isolated zero (xˆ1,xˆ2,xˆ3). In general, if an isolated zero (xˆ1,··· ,xˆγ+1) to the system





- h0(x1)
- h1(x1, x2)


gγ(x1,··· ,xγ+1) =

 

 

. hγ(x1, · · · , xγ+1)

remains singular, or the Jacobian Jγ(xˆ1,··· ,xˆγ+1) is rank-deﬁcient, then there is a non-zero solution to the homogeneous system



  

  



u1

  

   ≡

u1 .

Jγ−1(xˆ1, · · · , xˆγ)

. .

Jγ(xˆ1,··· ,xˆγ+1)

  = 0.

 

uγ

uγ+1

∗

Therefore, by setting uj = xˆj+1 for j = 1,... ,γ, we take its unique solution uγ+1 as xˆγ+2. The pattern of this depth-deﬂation process can be illustrated by deﬁning

Ψ =

∞

xη+1 · ∆xη. (49)

η=1

When applying Ψ to any function f in (vector) variables, say x1,··· ,xσ, the resulting Ψf is a ﬁnite sum since ∆xµf = 0 for µ ≥ σ + 1. Thus,

2 − 1 , h2(x1,x2,x3) = ΨbhH1x(x1,x2)

h1(x1,x2) = b ΨHhx0(x1)

3 − 1 and

hν(x1,··· ,xν) =

  

ν−1

![image 265](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile265.png>)

![image 266](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile266.png>)

Ψ ◦ Ψ ◦ · · · ◦ Ψ h1(x1, x2),

bHxν+1

  , for ν ≥ 2. (50)

For instance, with h1 and h2 in (46) and (48) respectively, we have h3(x1,x2,x3,x4) = (∇x

2∇x2∇x2 + 3∇x2∇x3 + ∇x4)h0(x1)

bHx4 .

If, say, h3 = 0 at (xˆ1,xˆ2,xˆ3,xˆ4), a functional f −→ (∇xˆ2∇xˆ2∇xˆ2 + 3∇xˆ2∇xˆ3 + ∇xˆ4) f(x1) is obtained and it vanishes on the system f. The original system f(x) = 0 provides a trivial

functional ∂0···0 : f → f(xˆ1). By the following lemma those functionals are all in the dual space.

- Lemma 6 Let f = [f1,··· ,ft]⊤ be a nonlinear system with an isolated zero xˆ ∈ s. Write g0 = f, xˆ1 = xˆ and x1 = x. For any γ ∈ {1,2,··· }, let (xˆ1, xˆ2, ··· , xˆγ+1) be a zero of


  . (51)

  

h0(x1)

gγ(x1,x2,··· ,xγ+1) =

hγ(x1, · · · , xγ+1)

Then the functionals derived from gγ(xˆ1,··· ,xˆγ+1) = 0 constitutes a linearly independent subset of the dual space Dxˆ0(f).

Proof. By a rearrangement, ﬁnding a zero of gγ(x1,x2,··· ,xγ+1) is equivalent to solving

f(x1) = 0, bHx2 = 1, Ψf(x1) = 0, bHx3 = 0,

(52)

. . Ψ ◦ ··· ◦ Ψf(x1) = 0, bHxγ+1 = 0.

for (x1,··· ,xγ+1) ∈ (γ

+1)s. Let (xˆ1,··· ,xˆγ+1) be an isolated zero. Then each Ψ◦···◦Ψ induces a diﬀerential functional

α

![image 267](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile267.png>)

![image 268](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile268.png>)

ρα : f −→

Ψ ◦ ··· ◦ Ψf

, for α = 0,1,··· ,γ. (53)

(x1,···,xα+1)=(xˆ1,···,xˆα+1)

Those functionals vanish on f1,··· ,ft because of (52). Since Ψ satisﬁes product rule Ψ(fg) = (Ψf)g + f(Ψg) for any functions f and g in ﬁnitely many variables among x1,x2,··· , for any polynomial p ∈ [x1], we have, for α = 0,1,··· ,γ and i = 1,··· ,t,

α−j

j

α

α j

![image 269](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile269.png>)

![image 270](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile270.png>)

![image 271](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile271.png>)

![image 272](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile272.png>)

Ψ ◦ ··· ◦ Ψp)(

Ψ ◦ ··· ◦ Ψfi)

= 0.

ρα(pfi) =

(

(x1,··· ,xα+1)=(xˆ1,···,xˆα+1)

j=0

Namely, ρα’s satisfy the closedness condition (11), so they belong to Dxˆ1(f).

α

![image 273](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile273.png>)

![image 274](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile274.png>)

The leading (i.e., the highest order diﬀerential) term of ρα is

∇xˆ2 ··· ∇xˆ2 which is of order α since xˆ2 = 0. Therefore, they are linearly independent.

- Theorem 5 (Breadth-one Deﬂation Theorem) Let xˆ be an isolated multiple zero of the nonlinear system f = [f1,··· ,ft]⊤ with breadth βxˆ(f) = 1. Then there is an integer γ ≤ δxˆ(f) such that, for almost all b ∈ s, the system gγ in (51) has a simple zero (xˆ1, xˆ2, ··· , xˆγ+1) which induces γ+1 linearly independent functionals in Dxˆ(f).


Proof. A straightforward consequence of Lemma 6.

While the general depth-deﬂation method usually terminates with one or two steps of system expansion for systems of breadth higher than one, the breadth one depth-deﬂation always terminates at step γ = δxˆ(f) exactly. Summarizing the above elaboration, we give the pseudo-code of an eﬃcient algorithm for computing the multiplicity structure of the breadth one case as follows:

Algorithm BreadthOneMultiplicity Input: Nonlinear system f = [f1,... ,ft]H, zero xˆ1 ∈ s

- – set random vectors b ∈ s and obtain xˆ2 by solving J(bxˆH1) x2 =

- 0
- 1


- – initialize p2(x1,x2) = J(x1)x2
- – for k = 2,3,... do


∗ set dk(x1,... ,xk) = − j k=1−1 xˆj+1 · ∆xj pk(x1,... ,xk) ∗ solve for xk+1 = xˆk+1 in the system

J(xˆ1) bH

dk(xˆ1, . . . , xˆk)

0 (54) ∗ if the equation (54) has no solution, set γ = k − 1 and

xk+1 =

break the loop; otherwise, set

pk+1(x1,... ,xk+1) = Ψpk(x1,... ,xk) ≡ dk(x1,... ,xk) + J(x1)xk+1 end do

Output: multiplicity γ + 1 and functionals ρ0, ρ1, ... , ργ as in (53)

Example 5 One of the main advantages of our algorithms is the capability of accurate identiﬁcation of multiplicity structures even if the system data are given with perturbations and the zero is approximate. Consider the sequence of nonlinear systems

˜fk(x,y,z) = [x2 sin y, y − z2, z − 1.772453850905516 cos xk ]⊤, (55) which is an inexact version of the system fk(x,y,z) = [x2 siny, y−z2, z−

√π cos xk]⊤ with breadth

![image 275](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile275.png>)

one and isolated zero (0,π,√π). The multiplicity is 2(k+1) and the depth is δ(0,π,√π)(fk) = 2k+1 for k = 1,2,.... Our code BreadthOneMultiplicity running on ﬂoating point arithmetic accurately identiﬁes the multiplicity structure with the approximate dual basis

![image 276](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile276.png>)

![image 277](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile277.png>)

1, ∂x, ∂x2, ... ,∂x2k-1, ∂y + 0.2820947917738781 ∂z − 0.3183098861837908 ∂x2k, ∂xy + 0.2820947917738781 ∂xz − 0.3183098861837908 ∂x2k+1

at the numerical zero (0, 3.141592653589793, 1.772453850905516). The computing time is shown in Table 2 for Algorithm BreadthOneMultiplicity.

In our extensive computing experiments, Algorithm BreadthOneMultiplicity always produces a complete dual basis without premature termination. We believe the following conjecture is true.

Conjecture 1 Under the assumptions of Theorem 5, Algorithm BreadthOneMultiplicity terminates at γ = δxˆ(f) and generates a complete basis for the dual space

Dxˆ(f) = span{ρ0,ρ1,... ,ργ}.

![image 278](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile278.png>)

![image 279](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile279.png>)

![image 280](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile280.png>)

![image 281](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile281.png>)

![image 282](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile282.png>)

![image 283](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile283.png>)

![image 284](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile284.png>)

![image 285](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile285.png>)

![image 286](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile286.png>)

![image 287](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile287.png>)

![image 288](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile288.png>)

![image 289](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile289.png>)

![image 290](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile290.png>)

![image 291](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile291.png>)

![image 292](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile292.png>)

![image 293](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile293.png>)

k: 2 4 6 8 10

![image 294](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile294.png>)

![image 295](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile295.png>)

![image 296](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile296.png>)

![image 297](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile297.png>)

![image 298](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile298.png>)

![image 299](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile299.png>)

![image 300](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile300.png>)

![image 301](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile301.png>)

![image 302](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile302.png>)

![image 303](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile303.png>)

computed depth : 5 9 13 17 21 computed multiplicity : 6 10 14 18 22

![image 304](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile304.png>)

![image 305](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile305.png>)

![image 306](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile306.png>)

![image 307](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile307.png>)

![image 308](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile308.png>)

![image 309](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile309.png>)

![image 310](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile310.png>)

![image 311](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile311.png>)

![image 312](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile312.png>)

![image 313](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile313.png>)

![image 314](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile314.png>)

![image 315](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile315.png>)

![image 316](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile316.png>)

![image 317](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile317.png>)

![image 318](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile318.png>)

![image 319](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile319.png>)

![image 320](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile320.png>)

![image 321](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile321.png>)

![image 322](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile322.png>)

![image 323](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile323.png>)

BreadthOneMultiplicity elapsed time 0.34 1.45 3.58 18.22 63.42

![image 324](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile324.png>)

![image 325](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile325.png>)

Table 2: Results of BreadthOneMultiplicity in ﬂoating point arithmetic on the inexact systems ˜fk in (55) at the approximate zero (0, 3.141592653589793, 1.772453850905516).

Acknowledgements. The authors wish to thank following scholars: Along with many insightful discussions, Andrew Sommese provided a preprint [2] which presented an important application of this work, Hans Stetter provided the diploma thesis [31] of his former student, Teo Mora pointed out Macaulay’s original contribution [21] elaborated in his book [23], and Lihong Zhi pointed out the reference [19].

# References

- [1] D. J. Bates, C. Peterson, and A. J. Sommese, A numerical-symbolic algorithm for computing the multiplicity of a component of an algebraic set, J. of Complexity, 22 (2006), pp.475-489.
- [2] D. J. Bates, C. Peterson, and A. J. Sommese, A numerical local dimension test for points on the solution set of a system of polynomial equations, SIAM J. Numer. Anal. 47

(2009), pp. 3608-3623.

- [3] S.-N. Chow and J. K. Hale, Methods of Bifurcation Theory, Springer-Verlag, 1982.
- [4] D. Cox, J. Little, and D. O’shea, Using Algebraic Geometry, Springer, New York, 2005.
- [5] B. H. Dayton and Z. Zeng,Computing the Multiplicity Structure in Solving Polynomial systems, Proc. of ISSAC ’05, ACM Press, pp 116–123, 2005.
- [6] J. W. Demmel, Applied Numerical Linear Algebra, SIAM Publications, 1997.
- [7] J. Emsalem, Ge´ome´trie des points e´spais, Bull. Soc. Math. France, 106 (1978), pp. 399–416.
- [8] W. Fulton, Intersection Theory, Springer Verlag, Berlin, 1984.
- [9] G. H. Golub and C. F. Van Loan, Matrix Computations, 3rd ed., The John Hopkins Univ. Press, Baltimore and London, 1996.
- [10] W. Grobner¨ , Algebrische Geometrie II, vol. 737 of Bib. Inst. Mannheim, Hochschultaschenbu¨cher, 1970.
- [11] G.-M. Greuel and G. Pfister, A Singular Introduction to Commutative Algebra, SpringerVerlag Berlin Heidelberg 2008
- [12] G.-M. Greuel, G. Pfister, and H. Schonemann¨ , Singular 3.0. A Computer Algebra System for Polynomial Computations, Centre for Computer Algebra, Univ. of Kaiserslautern, 2005.
- [13] H. Kobayashi, H. Suzuki and Y. Sakai, Numerical calculation of the multiplicity of a solution to algebraic equations, Math. Comp., 67(1998), pp. 257–270.
- [14] M. Kreuzer and L. Robbiano, Computational Commutative Algebra 2, Springer, 2005.


- [15] Y. C. Kuo and T. Y. Li, Determining dimension of the solution component that contains a computed zero of a polynomial system, J. Math. Anal. Appl., 338 (2008), pp. 840–851.
- [16] E. Lasker, Zur theorie der moduln und ideale, Math. Ann. 60, pp. 20-116, 1905.
- [17] A. Leykin, J. Verschelde, and A. Zhao, Newton’s method with deﬂation for isolated singularities of polynomial systems, Theoretical Computer Science, (2006), pp. 111–122.
- [18] A. Leykin, J. Verschelde, and A. Zhao, Higher-order deﬂation for polynomial systems with isolated singular solutions, in IMA Volume 146: Algorithms in Algebraic Geometry, A. Dickenstein, F.-O. Schreyer, and A.J. Sommese, eds., Springer, New York, 2008, pp. 79–97
- [19] B.-H. Li, A method to solve algebraic equations up to multiplicities via Ritt-Wu’s characteristic sets, Acta Analysis Functionalis Applicata, 5(2003), pp. 97-109.
- [20] T. Y. Li and Z. Zeng, A rank-revealing method with updating, downdating and applications, SIAM J. Matrix Anal. Appl., 26 (2005), pp. 918–946.
- [21] F. S. Macaulay, The Algebraic Theory of Modular Systems, Cambridge Univ. Press, 1916.
- [22] M. G. Marinari, T. Mora and H. M. Moller¨ , On multiplicities in polynomial system solving, Trans. AMS, 438(1996), pp. 3283–3321.
- [23] T. Mora, Solving Polyonmial Equation Systems II, Cambridge Univ. Press, London, 2004.
- [24] B. Mourrain, Isolated points, duality and residues, J. of Pure and Applied Algebra, 117 & 118 (1996), pp. 469–493.
- [25] T. Ojika, Modiﬁed deﬂation algorithm for the solution of singular problems, J. Math. Anal. Appl., 123 (1987), pp. 199–221.
- [26] A.J. Sommese and J. Verschelde, Numerical Homotopies to Compute Generic Points on Positive Dimensional Algebraic Sets, J. of Complexity 16 (2000), pp. 572-602.
- [27] R. P. Stanley, Hilbert functions of graded algebras, Advances in Math., 28 (1960), pp. 57–83.
- [28] H. J. Stetter and G. H. Thallinger, Singular Systems of Polynomials, Proc. ISSAC ’08, ACM Press, pp. 9–16, 1998.
- [29] H. J. Stetter, Numerical Polynomial Algebra, SIAM publications, 2004.
- [30] J. Taylor, Several Complex Variables with Connections to Algebraic Geometry and Lie Groups, American Mathematical Society, Providence, Rhode Island, 2000.
- [31] G. H. Thallinger, Analysis of Zero Clusters in Multivariate Polynomial Systems, Diploma Thesis, Tech. Univ. Vienna, 1996.
- [32] X. Wu and L. Zhi, Computing the multiplicity structure from geometric involutive form, Proc. ISSAC’08, ACM Press, pp.325–332, 2008.
- [33] O. Zariski and P. Samuel, Commutative Algebra, vol. II, Springer-Verlag (reprinted), Berlin, 1960.
- [34] Z. Zeng, Computing multiple roots of inexact polynomials, Math. Comp., 74 (2005), pp. 869– 903.
- [35] , ApaTools: A Maple and Matlab toolbox for approximate polynomial algebra, in Software for Algebraic Geometry, IMA Volume 148, M. Stillman, N. Takayama, and J. Verschelde, eds., Springer, 2008, pp. 149–167.

![image 326](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile326.png>)

- [36] , The closedness subspace method for computing the multiplicity structure of a polynomial system. to appear: Interactions between Classical and Numerical Algebraic Geometry, Contemporary Mathematics series, American Mathematical Society, 2009.


![image 327](<2011-dayton-multiple-zeros-nonlinear-systems_images/imageFile327.png>)

