---
type: source
kind: paper
title: An extremal problem and inequalities for entire functions of exponential type
authors: Andrés Chirre, Dimitar K. Dimitrov, Emily Quesada-Herrera, Mateus Sousa
year: 2023
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2304.05337v2
source_local: ../raw/2023-chirre-extremal-problem-inequalities-entire.pdf
topic: general-knowledge
cites:
---

arXiv:2304.05337v2[math.CA]30Oct2023

AN EXTREMAL PROBLEM AND INEQUALITIES FOR ENTIRE FUNCTIONS OF EXPONENTIAL TYPE

ANDRES´ CHIRRE, DIMITAR K. DIMITROV, EMILY QUESADA-HERRERA, AND MATEUS SOUSA

Abstract. We study two variations of the classical one-delta problem for entire functions of exponential type, known also as the Carath´eodory–Fej´er–Tura´n problem. The ﬁrst variation imposes the additional requirement that the function is radially decreasing while the second one is a generalization which involves derivatives of the entire function. Various interesting inequalities, inspired by results due to Duﬃn and Schaeﬀer, Landau, and Hardy and Littlewood, are also established.

1. Introduction

In the present note we study some extremal problems concerning certain quantities over speciﬁc families of entire functions of exponential type. For ∆ > 0, we say that an entire function G : C → C has exponential type at most 2π∆ if, for all ε > 0, there exists a positive constant Cε such that

|G(z)| ≤ Cε e(2π∆+ε)|z|, for all z ∈ C. We adopt the usual convention that an entire function f : C → C is said to be real if its restriction to R is real-valued, as well as, that the function g∗(z) is deﬁned by g∗(z) = g(z). For f,g ∈ L1(R) we denote by f ∗ g their convolution, which is deﬁned by (f ∗ g)(x) =

![image 1](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile1.png>)

![image 2](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile2.png>)

∞

f(y)g(x − y)dy.

−∞

- 1.1. The one-delta problem. The classical one-delta problem is to determine the inﬁmum


∞

A = inf

g(x)dx,

g∈G

−∞

where the class G consists of real entire functions g : C → C of exponential type at most 2π which are majorants of a one-delta function at the origin over the real line, i.e, g(x) ≥ 0 for all x ∈ R and g(0) ≥ 1. By scaling, this is equivalent

f 1 f(0)

,

A = inf

![image 3](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile3.png>)

f∈F f(0) =0

where the family F consists of real entire functions f : C → C of exponential type at most 2π such that f ∈ L1(R), and f(x) ≥ 0 for all x ∈ R. This is a classical problem, and several of its variations are named after Carath´eodory, Fej´er and Tur´an. We refer to [10, 12, 20, 23] for comprehensive information about its

![image 4](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile4.png>)

2010 Mathematics Subject Classiﬁcation. 42A38, 30D15, 41A17. Key words and phrases. One-delta problem, extremal problem, extremal function, entire function of exponential type.

Research supported by the Brazilian Science Foundations FAPESP under Grants 2016/09906-0, 2019/12413-4 and 2021/13340-0 and CNPq under Grant 309955/2021-1, the Bulgarian National Research Fund through Contract KP-06-N62/4, and the Austrian Science Fund (FWF) via Project P-35322. MS is supported by the grant Juan de la Cierva incorporacio´n 2019 IJC2019-039753-I, the Basque Government through the BERC 2022-2025 program, by the Spanish State Research Agency project PID2020-113156GB-100/AEI/10,13039/501100011033 and through BCAM Severo Ochoa excellence accreditation SEV2023-2026.

history and for some recent contributions. It is known that A = 1, and the unique extremal solution of the one-delta problem is the Fej´er kernel, given by

2

sinπz πz

K(z) =

. (1.1) To obtain an equivalent formulation of this problem, we may consider a decomposition result due to Krein

![image 5](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile5.png>)

- [1, p. 154]. It states that if f : C → C is an entire function of exponential type at most 2π such that f ∈ L1(R) and f(x) ≥ 0 for all x ∈ R, then there exists an entire function g : C → C in the Paley–Wiener space PW2 such that f(z) = g(z)g∗(z). Here, PW2 is the subspace of L2(R) consisting of entire functions of exponential type at most π. Therefore, the one-delta problem can also be stated as ﬁnding


A = inf

g∈PW2 g(0) =0

g 22 |g(0)|2

. (1.2)

![image 6](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile6.png>)

Other Lp−variations of this problem have also been studied in [4, 7, 19]. Note that (1.2) can be stated in yet another alternative way as follows: the inequality

∞

|g(x)|2 dx, (1.3)

1 ≤

−∞

holds for every g ∈ PW2 such that g(0) = 1, and (1.3) reduces to an equality if and only if g(z) =

sinπz πz

. Our main goal is to study some natural variations of each of the above versions of the one-delta problem.

![image 7](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile7.png>)

- 1.2. Monotone-delta problem. The monotone-delta problem is to ﬁnd


A1 = inf

f∈F1 f(0) =0

f 1 f(0)

, (1.4)

![image 8](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile8.png>)

- where the family F1 consists of real entire functions f : C → C of exponential type at most 2π, such that f ∈ L1(R), f(x) ≥ 0 for all x ∈ R, and f is radially decreasing, that is, f is increasing on (−∞,0) and decreasing on (0,∞). To the best of our knowledge, this problem was posed explicitly by Jeﬀrey Vaaler. It is a variant, with additional constraints, of another problem, solved by Holt and Vaaler in [16]. Another minimization problem with monotonicity restrictions was considered in [6] by Carneiro and Littmann, in the setting of one-sided majorants for the signum function.


In the following theorem, we present some qualitative and quantitative information about this problem.

- Theorem 1. The following statements about the monotone-delta problem hold:


- (a) There exists an even function F ∈ F1 with F(0) = 1 that extremizes (1.4).
- (b) All the zeros of any even extremizer F lie in the set S = {z ∈ C : |Re z| > |Imz| > 0}.
- (c) The constant A1 satisﬁes 1.2750 < A1 < 1.27714.


Part (a) follows from standard compactness arguments. For part (b) we will show that zeros outside of S will either force a function to be zero, by analytic continuation and the constraints in the class F1, or one can carefully remove said zero and arrive at a contradiction. Part (c) of Theorem 1 is constructive, and although our lower bound only coincides up the two ﬁrst digits, we conjecture that the upper bound in part (c) is sharp, at least up the ﬁrst four signiﬁcant digits of A1 shown above. As evidence, we exhibit concrete examples for which the value 1.2771...is attained. To estimate A1, we ﬁrst reformulate the monotone-delta

problem (see Lemma 6 below) to the one of determining the inﬁmum

A1 = inf

h∈F2 h ≡0

∞

|x|2|h(x)|2 dx ∞ −∞

2

−∞

, (1.5)

![image 9](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile9.png>)

|x||h(x)|2 dx

- where the family F2 consists of entire functions h : C → C of exponential type at most π such that xh ∈ L2(R) and |h(x)| = |h(−x)|. We then introduce an L2 approach to generate upper and lower bounds


that converge to A1 (see Theorem 8), and we use this approach to computationally obtain high precision numerical bounds, with rigorous computations in Ball arithmetic – see Section 3. Furthermore, we also ﬁnd an explicit, relatively simple example of a function h0 ∈ F2 (see (4.8)). For this h0, we compute explicitly the quotient in (1.5), which turns out to be 1.2771 .... Despite that h0 is not the extremal function for (1.5), our conjecture is that the value 1.2771 ... is so close to the inﬁmum A1, that they diﬀer only in the decimal digits after the fourth one. Section 3 is dedicated to prove part (c). See also [14, 17] for works involving similar problems with computational approaches to solutions.

The monotone-delta problem has also been considered in Rd, for d ≥ 2. In [5], using techniques from the theory of de Branges spaces, the authors found the exact solution of the monotone-delta problem when d is even. Nonetheless, the authors state that the case when d is odd seems more subtle and remains open.

Despite that Lemma 6 below provides an integral representation of any function in F1, the ﬁrst interesting explicit example of a function in this class we constructed was based on the classical method of Sonin, which was itself invented with the intention to obtain information about the monotonicity of the successive relative minima and maxima of certain oscillatory solutions of ordinary diﬀerential equations (see [25, Section 7.31]). If g : C → C is a real entire function in PW2 and satisﬁes a second-order diﬀerential equation of the form y′′ + (B/x)y′ + Cy = 0, with constants B,C > 0, Sonin’s method suggests to construct the function

(g′(z))2 C

f(z) = (g(z))2 +

. (1.6)

![image 10](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile10.png>)

By the Plancherel-Po´lya theorem, since g ∈ PW2 we have that g′ ∈ PW2, and therefore f ∈ F1. Moreover f(x) is a “lid” of g2(x) in the sense that f(x) ≥ g2(x) for every x ∈ R and f interpolates g2 and possesses inﬂection points at its local maxima. Figure 1 shows Fej´er’s kernel K(x) and its lid f(x).

1.0

0.8

0.6

0.4

0.2

-3 -2 -1 1 2 3

Figure 1. The Fej´er kernel K(x) deﬁned in (1.1) and its lid f(x).

- 1.3. The one-delta problem with derivatives. The function in (1.6) appears in a classical inequality for entire functions. Duﬃn and Schaeﬀer [9, p. 239] proved that if a real entire function g : C → C of


exponential type at most π is such that |g(x)| ≤ 1 for all x ∈ R, then

|g(x)|2 + |g′(x)|2 π2 ≤ 1, for all x ∈ R.

![image 11](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile11.png>)

Inspired by this inequality, we prove that speciﬁc sums of the L2−norms of a function g ∈ PW2, normalized by g(0) = 1, and its consecutive derivatives, are bounded from below. Our result may be considered a variation of the one-delta problem where one wishes to minimize sums of L2−norms of an entire function and of its derivatives, and reads as follows:

- Theorem 2. Let N be a nonnegative integer and the real polynomial


N

anxn

P(x) =

n=0

be positive for every x ∈ [0,1]. Then the inequality

−1

N

∞

1

an π2n

1 P(t2)

g(n)(x) 2 dx (1.7)

dt

≤

![image 12](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile12.png>)

![image 13](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile13.png>)

−∞

0

n=0

holds for every g ∈ PW2 which obeys the normalization g(0) = 1. Moreover, equality in (1.7) is attained if and only if

−1 1

1

1 P(t2)

cos(πzt) P(t2)

g(z) =

dt

dt. (1.8)

![image 14](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile14.png>)

![image 15](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile15.png>)

0

0

Note that when N = 0 and a0 = 1, we recover the inequality (1.3), which once again shows that the latter is a natural result in the spirit of the one-delta problem. Moreover, choosing the polynomial P(x) = 1+aπ2x, we obtain the following corollary.

- Corollary 3. Fix a > 0. Then the inequality π√a

![image 16](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile16.png>)

![image 17](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile17.png>)

arctan(π√a) ≤

![image 18](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile18.png>)

∞

−∞

|g(x)|2 + a |g′(x)|2 dx, (1.9)

holds for every g ∈ PW2 with g(0) = 1 and the unique extremal function for which (1.9) reduces to an equality is

g(z) =

π√a arctan(π√a)

![image 19](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile19.png>)

![image 20](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile20.png>)

![image 21](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile21.png>)

1

- 0

cos(πzt)

![image 22](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile22.png>)

- 1 + aπ2t2


dt. Observe that for a = 1/π2 (1.9) reduces to the following estimate:

∞

−∞

|g(x)|2 + |g′(x)|2 π2

![image 23](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile23.png>)

dx ≥

4 π

![image 24](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile24.png>)

, g ∈ PW2, g(0) = 1.

Diﬀerent choices of the polynomial P(x) allow us to obtain other interesting inequalities.

- Corollary 4. Fix 0 < a < 1/π2. Then


1 + √aπ 1 −

−1

∞

∞

![image 25](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile25.png>)

- 1

![image 26](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile26.png>)

- 2π√a


g′(x) 2dx +

|g(x)|2 dx. (1.10)

√aπ

a

≤

log

![image 27](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile27.png>)

![image 28](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile28.png>)

![image 29](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile29.png>)

−∞

−∞

for every g ∈ PW2 which obeys g(0) = 1. In particular, letting a → 1/π2 in (1.10) we obtain

∞

∞

g′(x) 2 dx ≤ π2

|g(x)|2 dx, g ∈ PW2, g(0) = 1,

−∞

−∞

which is exactly the L2−version of the classical Bernstein inequality that holds for every Lp(R), p ≥ 1 (see

- [2, Theorem 11.3.3]). Observe that the Bernstein inequality follows from Theorem 2 if we set P(t) = 1 + ε − t and let ε → 0.


Applying the same reasoning with P(t) = (1 + ε − t)N, we obtain:

- Corollary 5. Let N be a nonnegative integer. Then the inequality N


∞

(−1)k σ2k

N k

f(k)(x) 2 dx ≥ 0

![image 30](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile30.png>)

−∞

k=0

holds for every function of exponential type at most σ such that f ∈ L2(R). In particular, for N = 2,

∞

∞

∞

- 1

![image 31](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile31.png>)

- 2


1 σ2

f′(x) 2 dx ≤

f(x) 2 dx +

f′′(x) 2 dx .

σ2

![image 32](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile32.png>)

−∞

−∞

−∞

The latter is a curious result that resembles some classical ones, due to Landau and Hardy and Littlewood. In 1913, Landau [21] proved that if f is a real function, f ∈ C2(R), and the inequalities f ∞ ≤ 1 and

√2. Hardy and Littlewood [15, Theorem 6] proved that, if y and y′′ are in L2[0,∞), then

f′′ ∞ ≤ 1 for the uniform norms of f and f′′ on the real line hold, so does f′ ∞ ≤

![image 33](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile33.png>)

2

∞

∞

∞

[y′(x)]2 dx

[y′′(x)]2 dx.

[y(x)]2 dx

≤ 4

0

0

0

Moreover, the constant 4 is the best possible. The equality is attained if and only if y(x) = c Y (ax), where c and a are real constants and

√3 2

![image 34](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile34.png>)

π 3

Y (x) = e−x/2 sin

.

x −

![image 35](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile35.png>)

![image 36](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile36.png>)

- Theorem 7 in [15] states that, under the same requirements, the inequality ∞


(y2(x) + [y′′(x)]2 − [y′(x)]2)dx ≥ 0 holds with equality as before, but with a = 1.

0

2. Proof of Theorem 1: Qualitative aspects For f ∈ L1(R), we normalize the Fourier transform f of f as

∞

f(x)e−2πixξ dx.

f(ξ) =

−∞

- 2.1. Proof of a). Replacing f(x) by (f(x) + f(−x))/2, we see that we may restrict our search for the inﬁmum (1.4) to the even functions in F1. Consider an extremizing sequence {fn}n≥1 ⊂ F1 such that fn is even, fn(0) = fn ∞ = 1, and fn 1 → A1. It follows from [22, Theorem 3.3.6], by passing to a subsequence if necessary, that there is F : C → C of exponential type at most 2π such that F ∈ L1(R) and

fn(x) → F(x) as n → ∞ uniformly on any compact set of C. Therefore, F is even, F ∈ F1 and F(0) = 1. Fatou’s lemma implies that

F 1 ≤ A1, and by the deﬁnition of A1 as an inﬁmum we conclude that F is an extremizer for (1.4).

- 2.2. Proof of b). Let F be an even extremizer with F(0) = 1. Clearly, it has no real zeros. Indeed, since


F is real, nonnegative and decreasing on the positive real axis, if it vanishes at x0 > 0, it does for all x > x0 which is impossible because F is entire and F(0) = 1. Since F is even, also it does not vanish at a negative

x0. Therefore, all the zeros of F satisfy |Imz| > 0. Now, assume that F has a zero at z = ib, for b ∈ R. Since F is real-valued, it also has z = −ib as a zero. Consider the entire function

b2F(z) z2 + b2

G(z) =

. Note that G(0) = 1 and G ∈ F1. Since

![image 37](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile37.png>)

∞

∞

F(x)dx

G(x)dx <

−∞

−∞

we get a contradiction. Therefore, all the zeros of F satisfy |Re z| > 0. Now, assume that z = a + ib is a zero of F with |b| ≥ |a| > 0. Since F is real-valued and even, we have that z = a − ib, z = −a + ib, and z = −a − ib are also zeros. Note that all these zeros are diﬀerent. Then, the entire function

(a2 + b2)2F(z) ((z − a)2 + b2) ((z + a)2 + b2) is in F1, and using that |b| ≥ |a|, it is easy to see that

H(z) =

![image 38](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile38.png>)

∞

∞

H(x)dx <

F(x)dx

−∞

−∞

which gives a contradiction. We conclude that |b| < |a|.

3. Proof of Theorem 1: quantitative aspects

- 3.1. Representation lemma. The following lemma gives a representation for any even function in F1.


Lemma 6. If f ∈ F1 is even, then it can be represented in R in the form f(x) =

x

−t|h(t)|2 dt, (3.1)

−∞

where h : C → C is an entire function of exponential type at most π such that |h(x)| = |h(−x)| for all x ∈ R, and xh ∈ L2(R). Conversely, if f is a function of the form (3.1), then it has an analytic extension to C which is an even function in F1.

Proof. Let f ∈ F1 be even. Integration by parts yields

x

f(t)dt = xf(x) +

0

x

t|f′(t)|dt. (3.2)

0

Since the integrals on both sides of (3.2) are increasing functions of x, and f ∈ L1(R), when x → +∞ we can conclude that lim

xf(x) exists). The fact that f ∈ L1(R) forces these limits to be zero and one can also conclude that xf′(x) ∈ L1(R). By the Plancherel-Po´lya theorem, f′(z) has exponential type 2π and so does −zf′(z). From the Krein decomposition theorem [1, p. 154], it follows that −zf′(z) = g(z)g∗(z) for some g ∈ PW2. Moreover, since f attains its maximum at x = 0, then f′(0) = 0. Deﬁning h(z) = g(z)/z, we rewrite the latter in the form

xf(x) exists (similarly lim

x→∞

x→−∞

−zf′(z) = z2h(z)h∗(z), (3.3)

where h is an entire function of exponential type at most π and xh ∈ L2(R). Since f′ is odd, then |h(x)| = |h(−x)| for x ∈ R. Finally, integrating (3.3) appropriately, we arrive at (3.1). Conversely, assume the

representation (3.1). Note that f has an analytic extension on C (also denoted by f) of the form

f(z) =

0

−t|h(t)|2 dt +

−∞

−s h(s)h∗(s)ds,

[0,z]

where [0,z] denotes the straight segment connecting 0 and z. Since h is an entire function of exponential type at most π, f is an entire function of exponential type at most 2π. From (3.1) it follows that lim

f(x) = 0, and using the fact that |h(x)| = |h(−x)|, we conclude that f is also even and lim

x→−∞

f(x) = 0. On the other hand, diﬀerentiating (3.1) we derive

x→∞

f′(x) = −x|h(x)|2 for x ∈ R, (3.4) which implies that f is radially decreasing and f(x) ≥ 0. Moreover, (3.4) and xh ∈ L1(R) imply lim

xf(x) =

x→±∞

0. Integration by parts shows that

∞

∞

x2|h(x)|2 dx,

f(x)dx =

−∞

−∞

which yields f ∈ L1(R).

From Lemma 6, we can reformulate the monotone-delta problem as the one to determine

∞

|x|2|h(x)|2 dx ∞ −∞

2

−∞

A1 = inf

, (3.5)

![image 39](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile39.png>)

h∈F2 h ≡0

|x||h(x)|2 dx

where the family F2 consists of those entire functions h : C → C of exponential type at most π such that xh ∈ L2(R) and |h(x)| = |h(−x)|.

- 3.2. An L2−computational approach. A natural approach for constructing functions in F2 (and therefore in F1), and computationally solving (3.5), starts by ﬁnding an orthonormal system for the space L2(R,x2dx). Note that F2 is a Hilbert space with the inner product


= xf,xg L2(R), and norm

f,g F

2

- 1

![image 40](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile40.png>)

- 2


∞

|x|2|f(x)|2 dx

. (3.6) For positive integers k, we deﬁne the even functions

=

f F

2

−∞

4√2 π ·

![image 41](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile41.png>)

cosπx (2k − 1)2 − 4x2

, (3.7)

hk(x) =

![image 42](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile42.png>)

![image 43](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile43.png>)

and note that hk ∈ F2 for all positive integers k. Gorbachev [11] previously considered this family of functions to obtain ﬁne numerical estimates for other Fourier extremal problems, and it has also been used in [8] for similar purposes in related extremal problems introduced by Carneiro, Milinovich, and Soundararajan [4]. Regarding this system, we can say the following:

Proposition 7. The family (hk)k≥1 is a complete orthonormal system in the closed subspace {h ∈ F2 : h is even.}.

Proof. Note that, if h ∈ F2 is even, then xh ∈ L2(R) is odd. Furthermore, we have that (xhk)(t) = i(−1)k

√

![image 44](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile44.png>)

2 sin(π(2k − 1)t)χI(t) =: sk(t), (3.8)

where I = [−1/2,1/2] and χI denotes the characteristic function of the interval I. To see this, since sk ∈ L1(R) ∩ L2(R), we may compute sk in a straightforward manner to verify that sk(x) = −xhk(x), and then we conclude (3.8) by Fourier inversion in L2(R). Now consider the operator

T : F2 → L2(I) deﬁned by Th(t) := (xh)(t)eπit. By Plancherel’s theorem and the Paley-Wiener theorem, T is a linear isometry, that is, f,g F

= Tf,Tg L2(I). Therefore, for positive integers k and j, we ﬁnd that hk,hj F

2

= sk,sj L2(I) = δkj,

2

where δkj = 1 if k = j, and 0 otherwise. Here, to compute the inner product over L2(I), we may apply the identity 2 sin(π(2k − 1)t)sin(π(2j − 1)t) = cos(2π(k − j)t) − cos(2π(k + j − 1)t). This shows that hk is orthonormal.

= 0 for all positive integers k. We must show that h ≡ 0. First, denote H(t) = (xh)(t), and note that, by Plancherel’s theorem and (3.8), the condition h,hk F

We now show that it is complete. Let h ∈ F2 be even, such that h,hk F

2

= 0 implies that

2

H(t)sin(π(2j − 1)t)dt = 0 (3.9) for all positive integers j. Actually, since sin(−x) = − sinx, (3.9) holds for all integers j.

I

Now, since T is an isometry into L2(I), by the theory of Fourier series on L2(I), it is enough to show that Th,ej L2(I) = 0 for all integers j, where ej(t) = e2πijt. In fact, for an integer j, we have

- H(t)eπite−2πitj dt

=

- I


Th,ej L2(I) =

I

H(t)sin(π(2j − 1)t)dt. The ﬁrst integral in the last line is 0 since H is odd, and the second integral is 0 by (3.9). Therefore, Th,ej L2(I) = 0 for all integers j, and then Th ≡ 0 and h ≡ 0, as desired.

H(t)cos(π(2j − 1)t)dt − i

I

More general orthogonality results can also be obtained from the theory of de Branges spaces; see [5, Section 2.2] and the references therein. See also [13, Theorem 4.2] for a similar general orthogonality result.

- 3.3. Proof of c): Generating bounds. Once we have a complete orthonormal system, we proceed to


obtain numerical examples as follows. For a positive integer d, let F2,d = span {hk : 1 ≤ k ≤ d} ⊂ F2. Let Q ∈ Rd×d be the matrix deﬁned by

∞

Qkj =

xhk(x)hj(x)dx. (3.10)

0

Then, since hk are orthonormal, one can see that the reciprocal of the inﬁmum in (3.5), when taken over the space F2,d, satisﬁes

∞

x|h(x)|2 dx ∞

0

|λd| = max

,

![image 45](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile45.png>)

h∈F2,d h ≡0

|x|2|h(x)|2 dx

−∞

where λd is the largest eigenvalue (in absolute value) of Q, and the maximum is attained when h = a · (h1,h2,...,hd), (3.11)

for a ∈ Rd an eigenvector of Q associated to λd. In particular, we have that A1 ≤ |λd|−1. Moreover, we now proceed to prove that as d → ∞, we have |λd|−1 → A1. Furthermore, we are able to explicitly estimate the speed of convergence, yielding lower bounds that also converge to A1 (see Theorem 8 below). With that goal in mind, we proceed to study the coeﬃcients Qkj deﬁned in (3.10). Our ﬁrst observation is that they can be made more explicit. When k > j, we expand in partial fractions and use the trigonometric identity 2 cos2(x) = 1 + cos(2x) to see that

∞

32(k − j)(k + j − 1)xcos2(πx) π2(4x2 − (2k − 1)2)(4x2 − (2j − 1)2)

(k − j)(k + j − 1)Qkj =

dx

![image 46](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile46.png>)

0

∞

1 2x − (2k − 1)

1 2x + (2k − 1) −

1 2x − (2j − 1) −

1 2x + (2j − 1)

1 + cos(2πx) π2

+

dx.

=

![image 47](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile47.png>)

![image 48](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile48.png>)

![image 49](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile49.png>)

![image 50](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile50.png>)

![image 51](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile51.png>)

0

By carefully splitting the integral, changing variables by translations and dilations, and regrouping all the pieces, one obtains

2k−1

Qkj = −1 π2 (k − j)(k + j − 1)

1 − cos(πx) x

dx. When k = j, a similar argument leads to the expression

![image 52](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile52.png>)

![image 53](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile53.png>)

2j−1

2k−1

dx = −4 + 2(2k − 1)π Si(π(2k − 1)) π2 (2k − 1)2

1 − cos(πx) x2

2 π2(2k − 1)

,

Qkk =

![image 54](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile54.png>)

![image 55](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile55.png>)

![image 56](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile56.png>)

0

where Si(x) = 0 x sin(t)/tdt is the standard sine integral function. These expressions readily imply that |Qkj|

1 d(k − j)

1 (2k − 1)

, and |Qkk|

, when d ≤ j < k.

![image 57](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile57.png>)

![image 58](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile58.png>)

These inequalities, with eﬀective constants, lead to bounds that can be used to explicitly estimate the speed of convergence of |λd|−1 to A1. By taking a particular value of d, we obtain the bounds stated in Theorem 1. Before we state our general bounds, we brieﬂy remark that, from the aforementioned work [5] (see Theorem 2 therein), we may restrict the search for the inﬁmum in (1.5) to even functions h ∈ F2.

- Theorem 8. Let h ∈ F2 be even and not identically 0. Deﬁne hk as in (3.7), and for a positive integer d,


let λd be the maximum eigenvalue (in absolute value) of the matrix Q deﬁned in (3.10). Then, for d ≥ 1000,

√log d d

∞

∞

![image 59](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile59.png>)

1 d

|x||h(x)|2 dx < 2

|x|2|h(x)|2 dx |λd| +

. In particular, for any d ≥ 1000, we have

+

![image 60](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile60.png>)

![image 61](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile61.png>)

−∞

−∞

√log d d

−1

![image 62](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile62.png>)

1 d

< A1 ≤ |λd|−1. When d = 3010, one obtains1

+

|λd| +

![image 63](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile63.png>)

![image 64](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile64.png>)

1.2750 < A1 < 1.27714.

![image 65](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile65.png>)

1These numerical computations were rigorously veriﬁed by using ball arithmetic with the Arb library [18].

![image 66](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile66.png>)

Proof. Write h = ∞k=1 akhk, with ak ∈ C. Denote a = (ak)k≥1 and a 2 := k≥1 |ak|2, so that h F

= a 2 (see (3.6)). Now, consider the functional J : F2\{0} → R given by

2

∞

x|h(x)|2 dx ∞

0

.

J(h) :=

![image 67](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile67.png>)

|x|2|h(x)|2 dx

−∞

First note that J is continuous on {h ∈ F2 : h  ≡ 0}. Indeed, from the classical one-delta problem, we have the trivial lower bound A1 ≥ 1. For f1, f2 ∈ F2, the triangle inequality yields

![image 68](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile68.png>)

![image 69](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile69.png>)

![image 70](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile70.png>)

∞

∞

∞

|x||f1(x)|2 dx −

|x||f2(x)|2 dx ≤

|x||f1(x) − f2(x)|2 dx ≤ f1 − f2 F

,

2

0

0

0

which implies the desired continuity. Here, we used that A1 ≤ 1 in the last inequality. Now, ﬁx d ≥ 1000, and for a parameter M ≥ d, consider HM = Mk=1 akhk. One has

J(HM) · |a1|2 + |a2|2 + ... + |aM|2 =

d

akaj Qkj + 2 Re

![image 71](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile71.png>)

k,j=1

M

akaj Qkj +

akaj Qkj

![image 72](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile72.png>)

![image 73](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile73.png>)

k,j=d+1

d<k≤M 1≤j≤d

= J(Hd) · |a1|2 + |a2|2 + ... + |ad|2 + J1 + J2 (3.12)

Here, Qkj is deﬁned as in equation (3.10). By deﬁnition of λd, we have |J(Hd)| ≤ |λd|. We now estimate |J1| and |J2|. One can verify that Qkk > 0 and that Qkj < 0 for k = j. To obtain upper bounds for |Qkj|, note that, since the local maxima of Si(x) form a decreasing sequence, we have 0 < Si(π(2k − 1)) ≤ Si(2001π) for all k > 1000. Additionally, since |cos(πx)| ≤ 1, we have that, for 1 ≤ j < k:

2k−1

2k−1

2(k − j) 2j − 1

2 x

1 − cos(πx) x

.

dx ≤

dx = 2 log 1 +

0 <

![image 74](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile74.png>)

![image 75](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile75.png>)

![image 76](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile76.png>)

2j−1

2j−1

This yields the inequalities

2 log 1 + 2(2kj−−1j) π2 (k − j)(k + j − 1)

2 Si(2001π) π(2k − 1)

![image 77](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile77.png>)

, and |Qkk| ≤

|Qkj| ≤

![image 78](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile78.png>)

![image 79](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile79.png>)

for 1 ≤ j < k, and for k > 1000 respectively. To estimate |J1| we use the triangle inequality, extend the sum over k to inﬁnity and apply the Cauchy-Schwarz inequality in both variables, which yields

log 1 + 2(2kj−−1j) (k − j)(k + j − 1)|akaj|

4 π2 d<k

![image 80](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile80.png>)

|J1| ≤

![image 81](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile81.png>)

![image 82](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile82.png>)

1≤j≤d

  

  

- 1

![image 83](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile83.png>)

- 2 


 

- 1

![image 84](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile84.png>)

- 2


log2 1 + 2(2kj−−1j) (k − j)2(k + j − 1)2

∞

4 π2

![image 85](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile85.png>)



|ak|2|aj|2

≤

![image 86](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile86.png>)

![image 87](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile87.png>)

k,j=1

d<k 1≤j≤d

 

 

- 1

![image 88](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile88.png>)

- 2


log2 1 + 2(2kj−−1j) (k − j)2

d

∞

1 (j + d)2

4 π2

![image 89](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile89.png>)

a 22. (3.13)

≤

![image 90](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile90.png>)

![image 91](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile91.png>)

![image 92](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile92.png>)

j=1

k=d+1

Since k − j ≥ 1, by applying estimates (5.5) and (5.6) with n = d and t = 2/(2j − 1) in (3.13), we obtain

 

 

- 1

![image 93](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile93.png>)

- 2


d

d

π2 3

4 π2

2 (j + d)2(2j − 1)

4 (j + d)2(2j − 1)2

a 22

|J1| ≤

+

![image 94](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile94.png>)

![image 95](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile95.png>)

![image 96](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile96.png>)

![image 97](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile97.png>)

j=1

j=1

 

 

- 1

![image 98](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile98.png>)

- 2


∞

d

π2 3

4 (2j − 1)2

2 (2j − 1)

4 π2d

a 22

+

≤

![image 99](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile99.png>)

![image 100](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile100.png>)

![image 101](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile101.png>)

![image 102](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile102.png>)

j=1

j=1

- 1

![image 103](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile103.png>)

- 2


π2 2

π2 2

4 π2d

a 22. In particular, when d ≥ 1000,

+

log d

≤

![image 104](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile104.png>)

![image 105](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile105.png>)

![image 106](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile106.png>)

2√2 π

√log d d

√log d d

- 1

![image 107](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile107.png>)

- 2


![image 108](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile108.png>)

![image 109](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile109.png>)

![image 110](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile110.png>)

1 log 1000

a 22 <

a 2. (3.14)

|J1| ≤

1 +

![image 111](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile111.png>)

![image 112](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile112.png>)

![image 113](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile113.png>)

![image 114](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile114.png>)

To estimate |J2|, we ﬁrst separate the diagonal term k = j. On the other terms, we use the fact that x  → log(1 + ax)/x is decreasing when x ∈ [0,∞) for any a > 0, and the Cauchy-Schwarz inequality, to obtain

log 1 + 2j2−1 k + j − 1

4 π2 k>j

2 Si(2001π) π(2d + 1) ·

![image 115](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile115.png>)

|ak|2 +

|ak||aj|

|J2| ≤

![image 116](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile116.png>)

![image 117](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile117.png>)

![image 118](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile118.png>)

k>d

k, j>d

  

  

- 1

![image 119](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile119.png>)

- 2


Si(2001π) π d

8 π2

1 (k + j − 1)2(2j − 1)2

a 22

a 22 +

≤

![image 120](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile120.png>)

![image 121](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile121.png>)

![image 122](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile122.png>)

k>j k, j>d

By applying (5.4) with n = 2j followed by (5.7) with n = d + 1, one arrives at

 

 

- 1

![image 123](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile123.png>)

- 2


- 1

![image 124](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile124.png>)

- 2


∞

1 1000

8 π2

Si(2001π) π d

1 d

1 2j(2j − 1)2

a 22 +

a 2. (3.15)

a 22 <

1 +

|J2| ≤

![image 125](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile125.png>)

![image 126](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile126.png>)

![image 127](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile127.png>)

![image 128](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile128.png>)

![image 129](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile129.png>)

j=d+1

Since (3.14) and (3.15) do not depend on M, applying these estimates on (3.12), sending M → ∞, and using the continuity of J concludes the proof. Finally, to obtain numerical bounds, we calculate the eigensystems numerically for d ≤ 3010, and ﬁnd that 0.783002554179 < λ3010 < 0.783002554181. We thereby obtain the numerical bounds in Theorem 8, and we highlight here our best, rigorous upper bound:

A1 < 1.277135042105.

4. Some functions in F1

- 4.1. The lid function. In this subsection, we apply Sonin’s method to construct a nice sequence of functions in F1. For any positive real numbers B and C, consider the diﬀerential equation


B

y′′ +

- x
- y′ + Cy = 0. (4.1)


![image 130](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile130.png>)

Let y = g, g : R → R be a solution of the equation (4.1). The lid of g2 is the function deﬁned by

(g′(x))2 C

f(x) = (g(x))2 +

. (4.2) Note that f(x) ≥ 0 for all x ∈ R, and

![image 131](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile131.png>)

2B(g′(x))2 xC

f′(x) = −

.

![image 132](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile132.png>)

This implies that f is radially decreasing. Moreover, if we suppose that the solution g has an analytic extension on C of exponential type at most π, and g ∈ L2(R), we conclude that f ∈ F1.

Let us show some examples of lids. For α > 0, consider the Bessel function of the ﬁrst kind of order α, which is deﬁned by

∞

(−1)ν(z/2)α+2ν ν!Γ(ν + α + 1)

.

Jα(z) =

![image 133](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile133.png>)

ν=0

Let us remark some properties of the Bessel functions mentioned in [25, Section 1.71]. It is known (see [25, Equation 1.71.3]) that Jα satisﬁes the diﬀerential equation

y′′ + x−1y′ + (1 − α2x−2)y = 0. (4.3) Now, deﬁne the function

Jα(πz) (πz)α

. A straightforward change of variables in (4.3) shows that gα satisﬁes the diﬀerential equation y′′ +

gα(z) =

![image 134](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile134.png>)

2α + 1 x

y′ + π2y = 0.

![image 135](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile135.png>)

The function gα is an even entire function of exponential type π. Moreover, using the decay of Jα (see [25, Equations 1.71.10 and 1.71.11] we see that gα ∈ L2(R). Therefore, inserting gα in (4.2) we actually construct the lid of gα2, with B = 2α + 1 and C = π2. In the particular case α = 1/2 we known that

sin(πx) πx

, and therefore

g1/2(x) =

![image 136](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile136.png>)

(g1′/2(x))2 π2

f1/2(x) = (g1/2(x))2 +

![image 137](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile137.png>)

is the lid of K(x). Straightforward calculations show that the Fourier transform of f1/2 is f1/2(ξ) = max{1 − |ξ|,0} +

1 π2

(g1′/2)2(ξ). (4.4) Then the Fourier transform - convolution de Margan type law yields

![image 138](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile138.png>)

∞

(g1′/2)2(ξ) = ( g1′/2 ∗ g1′/2)(ξ) = (2πix g1/2) ∗ (2πix g1/2) (ξ) = −4π2

x g1/2(x)(ξ − x) g1/2(ξ − x)dx,

−∞

where we used the fact that g1/2(x) = χI(x). This, together with (4.4), implies

 

- 2

![image 139](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile139.png>)

- 3


(1 − |ξ|)2(|ξ| + 2), if |ξ| ≤ 1; 0, if |ξ| > 1.

f1/2 (ξ) =



In particular, this example allows us to obtain the bound A1 ≤ 1.333 .... In fact, one can repeat the same argument for the function fα, for any α > 0. The Fourier transform of fα can be computed using [25, Equation 1.71.6]. Finally, we minimize the ratio fα(0)/fα(0) with respect to α, and obtain that it is attained for α0 = 0.787 ... and fα

(0) = 1.284 .... Hence A1 ≤ 1.284 ....

(0)/fα

0

0

4.2. Polynomial examples. As mentioned in the introduction, we now transform the optimization problem

- (3.5) over F2 in into another unrestricted, smooth optimization problem over Rd+1, so that we may construct functions h in a systematic way with standard numerical optimization methods. For this purpose, we make


a couple of helpful observations. First, note that if h ∈ F2 then h ∈ L1(R). In fact, by the Cauchy-Schwarz inequality, we have

∞

|h(x)| dx =

1

∞

|xh(x)| ·

1

1 x

dx ≤

![image 140](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile140.png>)

![image 141](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile141.png>)

∞

x2|h(x)|2 dx ·

1

![image 142](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile142.png>)

∞

1 x2

dx < ∞.

![image 143](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile143.png>)

1

Therefore, h is continuous in R, and in particular h(±1/2) = 0. Denoting I = [−1/2,1/2] we have that supp h ⊂ I. Therefore, by the Stone-Weierstrass theorem we may approximate h uniformly by a polynomial times χI.

With the previous observations in mind, we consider functions of the form h(x) =

1 4 − x2 g(x)χI(x), (4.5)

![image 144](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile144.png>)

where

d

aixi ∈ R[x]

g(x) =

i=0

is a polynomial of degree d. Note that the factor 4 1 − x2 means that h (±1/2) = 0. Denoting a = (a0,a1,...,ad) ∈ Rd+1, the inﬁmum in (3.5), restricted to this class, becomes

![image 145](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile145.png>)

2a · Na a · Da

, (4.6)

A1,d := min

![image 146](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile146.png>)

a∈Rd+1\0

where N, D ∈ R(d+1)×(d+1) are deﬁned by

∧

∞

∞

1 4 − y2 yiχI

|x|2fi(x)fj(x) dx; Dij =

![image 147](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile147.png>)

![image 148](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile148.png>)

|x|fi(x)fj(x) dx; fi(x) =

(−x).

Nij =

![image 149](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile149.png>)

−∞

−∞

For all d ≤ 20 and 0 ≤ i ≤ d, it is easy to see by direct computation of fi that xfi ∈ L2(R), so that h = a · (f0,...,fd) ∈ F2 for all a ∈ Rd+1. The matrices N and D may be computed explicitly for a given d, and this is then a smooth optimization problem over Rd+1. Solving it numerically for d = 2, we ﬁnd

1 4 − x2 1 −

9 5

x2 χI(x), (4.7) which yields

h0(x) =

![image 150](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile150.png>)

![image 151](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile151.png>)

108 − 25π2x2 sin(πx) − πx 11π2x2 + 108 cos(πx) 40π5x5

h0(x) =

. (4.8) By direct computation in exact rational arithmetic, this gives

![image 152](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile152.png>)

49484 38745

= 1.27717...

A1 ≤

![image 153](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile153.png>)

This gives another proof of an upper bound for A1, which coincides up to four decimal digits with our best bounds. Moreover, using the representation (3.1) we obtain the function in F1

P(πx) + Q(πx)sin(2πx) + R(πx)cos(2πx) 738π8x8

, (4.9) where

f0(x) =

![image 154](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile154.png>)

see Figure 2.

- P(x) = 242x6 + 3001x4 + 4176,
- Q(x) = −242x5 − 576x3 − 11664x,
- R(x) = 1463x4 + 7488x2 − 5832;


1.0

0.8

0.6

0.4

0.2

-3 -2 -1 1 2 3

Figure 2. The function f0(x) deﬁned in equation (4.9).

Additionally, we solve (4.6) for all d ≤ 20 and observe that, as the degree d increases, the sequence A1,d decreases very slowly, showing only a tiny improvement from 1.27717... only in the ﬁfth decimal digit. More precisely, we recover the bound A1 ≤ 1.27713505... with those much more detailed calculations performed with large degree d of the polynomials g. Below, we will show some tables with the results of these computations (see Table 1), and compare the results with those of our L2-approach from Section 3.2. In Figure 3 and Figure 4, we plot the functions 4 h0 and 60091 h0, respectively, where, since h0(0) = 60091 and h0(0) = 41, we renormalized the plots accordingly.

![image 155](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile155.png>)

![image 156](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile156.png>)

![image 157](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile157.png>)

1.0

0.9

0.8

0.7

0.6

-0.4 -0.2 0.2 0.4

1.0

0.8

0.6

0.4

0.2

-6 -4 -2 2 4 6

Figure 3. The function h0(x)/ h0(0) deﬁned in equation (4.7).

# Figure 4. The function h0(x)/h0(0) deﬁned in equation (4.8).

In Table 1, we compare the speed of convergence of the two numerical approaches we have presented. The ﬁrst approach is described above in the present section , with functions h deﬁned as in (4.5), via polynomials

- g of some degree d. The second approach is the L2−approach described in Section 3.2, with functions h deﬁned by (3.11). In both cases, the parameter d is the number of degrees of freedom in the construction of the function h. In both cases, the upper bounds for A1 appear to quickly converge to the ﬁrst few decimal digits, yet we observe that in the polynomial approach, the bound for A1 seems to converge much faster to more decimal digits with small values of d. Together, all of this gives evidence to the conjecture that the sharp value of A1, up to its ﬁrst 9 signiﬁcant digits, is

A1 = 1.277135042... (4.10)

Furthermore, the normalized plot of the function h we constructed by using (3.11) with d = 1000 is almost indistinguishable from the plot of h0 shown in Figure 4. Since the explicit function h0 deﬁned in (4.8) already agrees with our conjecture (4.10) to four signiﬁcant digits, we might expect it to behave close to an extremizer for A1. Indeed, in Table 2, we compare the ﬁrst 10 zeros of the functions h0 in (4.8) and

- h in (3.11) (the latter with d = 1000). Note that there is a good agreement up to the second decimal digit. We remark that the latter do not change with respect to the values with d = 500, up to the digits shown, except for a minor change in the last digit of x10 = 10.5240... (for d = 500).


![image 158](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile158.png>)

![image 159](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile159.png>)

![image 160](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile160.png>)

![image 161](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile161.png>)

![image 162](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile162.png>)

![image 163](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile163.png>)

![image 164](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile164.png>)

d A1 (polynomials) d A1 (L2)

![image 165](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile165.png>)

![image 166](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile166.png>)

![image 167](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile167.png>)

![image 168](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile168.png>)

![image 169](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile169.png>)

![image 170](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile170.png>)

![image 171](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile171.png>)

![image 172](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile172.png>)

2 1.277171240 10 1.2771993500 4 1.277148060 50 1.2771360175 6 1.277137688 100 1.2771351946 8 1.277135865 150 1.2771350931

![image 173](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile173.png>)

![image 174](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile174.png>)

![image 175](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile175.png>)

![image 176](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile176.png>)

![image 177](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile177.png>)

![image 178](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile178.png>)

![image 179](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile179.png>)

![image 180](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile180.png>)

![image 181](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile181.png>)

![image 182](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile182.png>)

![image 183](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile183.png>)

![image 184](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile184.png>)

![image 185](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile185.png>)

![image 186](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile186.png>)

![image 187](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile187.png>)

![image 188](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile188.png>)

![image 189](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile189.png>)

![image 190](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile190.png>)

![image 191](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile191.png>)

![image 192](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile192.png>)

![image 193](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile193.png>)

![image 194](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile194.png>)

![image 195](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile195.png>)

![image 196](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile196.png>)

![image 197](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile197.png>)

![image 198](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile198.png>)

![image 199](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile199.png>)

![image 200](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile200.png>)

10 1.277135348 200 1.2771350654 12 1.277135173 300 1.2771350498 14 1.277135104 500 1.2771350440 16 1.277135074 1000 1.2771350424 20 1.277135052 3010 1.2771350422

![image 201](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile201.png>)

![image 202](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile202.png>)

![image 203](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile203.png>)

![image 204](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile204.png>)

![image 205](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile205.png>)

![image 206](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile206.png>)

![image 207](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile207.png>)

![image 208](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile208.png>)

![image 209](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile209.png>)

![image 210](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile210.png>)

![image 211](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile211.png>)

![image 212](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile212.png>)

![image 213](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile213.png>)

![image 214](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile214.png>)

![image 215](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile215.png>)

![image 216](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile216.png>)

![image 217](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile217.png>)

![image 218](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile218.png>)

![image 219](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile219.png>)

![image 220](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile220.png>)

![image 221](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile221.png>)

![image 222](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile222.png>)

![image 223](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile223.png>)

![image 224](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile224.png>)

![image 225](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile225.png>)

![image 226](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile226.png>)

![image 227](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile227.png>)

![image 228](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile228.png>)

![image 229](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile229.png>)

- Table 1. Comparison of the numerical bounds for A1 in the polynomial construction of Section 4.2 and in the L2−construction of Section 3.2, as the corresponding parameter d grows.

![image 230](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile230.png>)

![image 231](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile231.png>)

. x1 x2 x3 x4 x5 x6 x7 x8 x9 x10

![image 232](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile232.png>)

![image 233](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile233.png>)

![image 234](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile234.png>)

![image 235](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile235.png>)

![image 236](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile236.png>)

![image 237](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile237.png>)

![image 238](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile238.png>)

![image 239](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile239.png>)

![image 240](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile240.png>)

![image 241](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile241.png>)

![image 242](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile242.png>)

![image 243](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile243.png>)

![image 244](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile244.png>)

![image 245](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile245.png>)

![image 246](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile246.png>)

Pol 1.5839 2.5715 3.5573 4.5470 5.5395 6.5340 7.5297 8.5264 9.5238 10.5220 L2 1.5866 2.5648 3.5525 4.5444 5.5387 6.5344 7.5311 8.5284 9.5261 10.5243

![image 247](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile247.png>)

![image 248](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile248.png>)

![image 249](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile249.png>)

![image 250](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile250.png>)

![image 251](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile251.png>)

![image 252](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile252.png>)

![image 253](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile253.png>)

![image 254](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile254.png>)

![image 255](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile255.png>)

![image 256](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile256.png>)

![image 257](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile257.png>)

![image 258](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile258.png>)

![image 259](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile259.png>)

![image 260](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile260.png>)

![image 261](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile261.png>)

![image 262](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile262.png>)

![image 263](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile263.png>)

![image 264](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile264.png>)

![image 265](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile265.png>)

![image 266](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile266.png>)

![image 267](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile267.png>)

![image 268](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile268.png>)

![image 269](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile269.png>)

![image 270](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile270.png>)

![image 271](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile271.png>)

![image 272](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile272.png>)

![image 273](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile273.png>)

- Table 2. First positive zeros of the function h0 via polynomials of degree 2 given in (4.8), and via the L2−approach as in (3.11) with d = 1000.


5. Proof of Theorem 2

Let g ∈ PW2. By Paley-Wiener’s theorem, g has compact support in [−21, 12], and using Plancherel’s theorem, we obtain

![image 274](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile274.png>)

![image 275](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile275.png>)

N

∞

an π2n

![image 276](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile276.png>)

−∞

n=0

Since g ∈ PW2, then

g(n)(x) 2 dx =

- 1

![image 277](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile277.png>)

- 2


−21

![image 278](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile278.png>)

g(z) =

N

an(4t2)n g(t) 2 dt =

n=0

- 1

![image 279](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile279.png>)

- 2


P(4t2) g(t) 2 dt. (5.1)

− 21

![image 280](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile280.png>)

- 1

![image 281](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile281.png>)

- 2


g(t)e2πizt dt. (5.2)

− 12

![image 282](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile282.png>)

Then the fact that g(0) = 1, the positivity of P(x), the Cauchy-Schwarz inequality and (5.1) yield

2

2

- 1

![image 283](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile283.png>)

- 2


- 1

![image 284](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile284.png>)

- 2


1 2

- 1

![image 285](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile285.png>)

- 2


1 P(4t2)

1 P(4t2)

![image 286](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile286.png>)

P(4t2) g(t) 2 dt

![image 287](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile287.png>)

dt , (5.3)

P(4t2) g(t) ·

1 =

=

g(t)dt

≤

dt

![image 288](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile288.png>)

![image 289](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile289.png>)

![image 290](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile290.png>)

−12

− 21

− 12

− 21

![image 291](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile291.png>)

![image 292](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile292.png>)

![image 293](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile293.png>)

![image 294](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile294.png>)

which implies (1.7). Note that equality in (5.3) holds if and only if there is λ ∈ C, such that g(t) =

λ P(4t2)

![image 295](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile295.png>)

almost everywhere in [−21, 12]. Hence, from (5.2) we conclude that

![image 296](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile296.png>)

![image 297](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile297.png>)

- 1

![image 298](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile298.png>)

- 2


1

e2πizt P(4t2)

cos(πzt) P(t2)

g(z) = λ

dt = λ

dt.

![image 299](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile299.png>)

![image 300](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile300.png>)

− 12

0

![image 301](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile301.png>)

Since g(0) = 1, then the extremal function is unique and it is is given by (1.8).

Remark 9. Since P(x) > 0 for all x ∈ [0,1], the expression in (5.1) is nonnegative. Thus we obtain a norm in PW2, deﬁned by

- 1

![image 302](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile302.png>)

- 2


N

∞

an π2n

g(n)(x) 2dx

, which can be viewed as a Sobolev-type norm.

g P =

![image 303](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile303.png>)

−∞

n=0

Appendix

Here, we record the following elementary estimates, which are useful in the proof of Theorem 8. Given 0 < t < ∞ and n ≥ 1000, one has

∞

1 n

1 n2

1 n ≤ 1 +

1 1000

1 k2

<

+

(5.4)

![image 304](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile304.png>)

![image 305](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile305.png>)

![image 306](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile306.png>)

![image 307](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile307.png>)

![image 308](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile308.png>)

k=n

n

log n 2 ≤

- 3 logn

![image 309](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile309.png>)

- 4


- 1

![image 310](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile310.png>)

- 2k − 1


< 1 + log 2 +

(5.5)

![image 311](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile311.png>)

k=1

∞

log2(1 + tx) x2

log2(1 + tk) k2

∞

π2 3

< t2 +

dx ≤ t2 +

t (5.6)

![image 312](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile312.png>)

![image 313](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile313.png>)

![image 314](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile314.png>)

0

k=1

∞

1 (2k − 1)3

1 (2n − 1)2

1 (2n − 1)3

1 4(2n − 1)2 ≤

1 1999

1 4

<

+

(5.7)

+

![image 315](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile315.png>)

![image 316](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile316.png>)

![image 317](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile317.png>)

![image 318](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile318.png>)

![image 319](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile319.png>)

![image 320](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile320.png>)

k=n

Acknowledgements

Part of this paper was written while A.C. was a Visiting Researcher in Department of Mathematics at the State University of Sa˜o Paulo UNESP. He is grateful for their kind hospitality. We are thankful to Emanuel Carneiro for helpful discussions related to the material of this paper.

References

- [1] N. I. Achieser, Theory of Approximation, Frederick Ungar Publishing, New York, 1956.
- [2] R. P. Boas, Jr., Entire Functions, Academic Press, New York, 1954.
- [3] H. Brezis, Functional Analysis, Sobolev Spaces and Partial Diﬀerential Equations, Springer, New York, 2011.
- [4] E. Carneiro, M. B. Milinovich and K. Soundararajan, Fourier optimization and prime gaps, Comment. Math. Helv. 94, no. 3 (2019), 533–568.
- [5] E. Carneiro, C. Gonz´lez-Riquelme, L. Oliveira, A. Olivo, S. Ombrosi, A. P. Ramos and M. Sousa, Sharp embeddings between weighted Paley–Wiener spaces, preprint at https://arxiv.org/pdf/2304.06442.pdf
- [6] E. Carneiro and F. Littmann, Monotone extremal functions and the weighted Hilbert’s inequality, preprint at https://arxiv.org/abs/2302.14658.
- [7] A. Chirre, O. F. Brevig, J. Ortega-Cerda and K. Seip, Point evaluation in Paley–Wiener spaces, preprint at https://arxiv.org/abs/2210.13922.
- [8] A. Chirre and E. Quesada-Herrera, Fourier optimization and quadratic forms, Q. J. Math. 73 (2022), no. 2, 539–577.
- [9] R. J. Duﬃn and A. C. Schaeﬀer, Some properties of functions of exponential type, Bull. Amer. Math. Soc. 44 (1938), no. 4, 236–240.
- [10] D. V. Gorbachev, Extremum problem for periodic functions supported in a ball, Mat. Zametki 69 (2001) 346–352.
- [11] D. V. Gorbachev, An integral problem of Konyagin and the (C,L)-constants of Nikolaskii, Trudy Inst. Mat. i Mekh. UrO RAN, 11, (2005), no. 2, 72–91.
- [12] D. V. Gorbachev and V. I. Ivanov, Tura´n’s and Fej´er’s extremal problems for Jacobi transform, Anal. Math. 44 (2018), 419–432.
- [13] D. V. Gorbachev and V. I. Ivanov, Tura´n, Fej´er and Bohman extremal problems for the multivariate Fourier transform in terms of the eigenfunctions of a Sturm–Liouville problem, Sb. Math., 210:6 (2019), 809–835.
- [14] D. V. Gorbachev and I.A. Martyanov, On interrelation of Nikolskii constants for trigonometric polynomials and entire functions of exponential type, Chebyshevskii Sb., 19:2 (2018), 80–89.
- [15] G. H. Hardy and J. E. Littlewood, Some integral inequalities connected with the calculus of variations, The Quarterly Journal of Mathematics, 3 (1932), 241–252.
- [16] J. Holt and J. D. Vaaler, The Beurling-Selberg extremal functions for a ball in the Euclidean space, Duke Math. Journal 83 (1996), 203–247.
- [17] L. H¨ormander and B. Bernhardsson, An extension of Bohr’s inequality Boundary value problems for partial diﬀerential equations and applications, RMA Res. Notes Appl. Math., 29 (1993), 179–194.
- [18] F. Johansson, Arb: eﬃcient arbitrary-precision midpoint-radius interval arithmetic, IEEE Transactions on Computers, 66 (2017), no. 8, 1281–1292.
- [19] J. Korevaar, An inequality for entire functions of exponential type, Nieuw Arch. Wiskunde (2) 23 (1949), 55–62.
- [20] S. Krenedits and S. Gy. R´ev´esz, Carath´eodory Fej´er type extremal problems on locally compact Abelian groups, J. Approx. Theory 194 (2015), 108–131.
- [21] E. Landau, Ungleichungen fu¨r zweimal diﬀerenzierbare Funktionen, Proc. London Math. Soc. 13 (1913), 43–49.
- [22] S. M. Nikolskii, Approximation of functions of several variables and imbedding theorems, Berlin; Heidelberg; New York: Springer, 1975.
- [23] S. Gy. R´ev´esz, Tura´n extremal problems on locally compact abelian groups, Anal. Math. 37 (2011), 15–50.
- [24] E. Stein and G. Weiss, Introduction to Fourier analysis on Euclidean spaces, Princeton University Press, Princeton, 1971.
- [25] G. Szego¨, Orthogonal polynomials, Fourth edition. American Mathematical Society, Colloquium Publications, Vol. XXIII. American Mathematical Society, Providence, R.I., 1975.


Departamento de Ciencias - Seccion´ Matematicas,´ Pontificia Universidad Catolica´ del Peru,´ Lima, Peru´ Email address: cchirre@pucp.edu.pe

Departamento de Matematica,´ IBILCE, Universidade Estadual Paulista UNESP, Sao˜ Jos´e do Rio Preto 15054, Brazil

Email address: d k dimitrov@yahoo.com

![image 321](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile321.png>)

![image 322](<2023-chirre-extremal-problem-inequalities-entire_images/imageFile322.png>)

Graz University of Technology, Institute of Analysis and Number Theory, Kopernikusgasse 24/II, 8010 Graz, Austria

Email address: quesada@math.tugraz.at

BCAM - Basque Center for Applied Mathematics, Alameda de Mazarredo 14, 48009 Bilbao, Bizkaia, Spain Email address: mcosta@bcamath.org

