|manuscript No.<br><br>(will be inserted by the editor)|
|---|


# arXiv:1411.6867v4[math.OC]8Sep2015

## Convergence analysis for Lasserre’s measure–based hierarchy of upper bounds for polynomial optimization

### Etienne de Klerk · Monique Laurent · Zhao Sun

Received: date / Accepted: date

Abstract We consider the problem of minimizing a continuous function f over a compact set K. We analyze a hierarchy of upper bounds proposed by Lasserre in [SIAM J. Optim. 21(3) (2011), pp. 864−885], obtained by searching for an optimal probability density function h on K which is a sum of squares of polynomials, so that the expectation K f(x)h(x)dx is minimized. We show that the rate of convergence is no worse than O(1/√r), where 2r is the degree bound on the density function. This analysis applies to the case when f is Lipschitz continuous and K is a full-dimensional compact set satisfying some boundary condition (which is satisﬁed, e.g., for convex bodies). The rth upper bound in the hierarchy may be computed using semideﬁnite programming if f is a polynomial of degree d, and if all moments of order up to 2r + d of the Lebesgue measure on K are known, which holds, for example, if K is a simplex, hypercube, or a Euclidean ball.

Keywords Polynomial optimization · Semideﬁnite optimization · Lasserre hierarchy

### Mathematics Subject Classiﬁcation (2000) 90C22 · 90C26 · 90C30

Etienne de Klerk Tilburg University PO Box 90153, 5000 LE Tilburg, The Netherlands E-mail: E.deKlerk@uvt.nl

Monique Laurent Centrum Wiskunde & Informatica (CWI), Amsterdam and Tilburg University CWI, Postbus 94079, 1090 GB Amsterdam, The Netherlands E-mail: M.Laurent@cwi.nl

Zhao Sun Ecole´ Polytechnique de Montr´eal GERAD–HEC Montreal 3000, Cˆote-Sainte-Catherine Rd, Montreal, QC H3T 2A7, Canada E-mail: Zhao.Sun@polymtl.ca

### 1 Introduction and Preliminaries

- 1.1 Background

We consider the problem of minimizing a continuous function f : Rn → R over a compact set K ⊆ Rn. That is, we consider the problem of computing the parameter:

fmin,K := min x∈K

f(x).

Our main interest will be in the case where f is a polynomial, and K is deﬁned by polynomial inequalities and equations. For such problems, active research has been done in recent years to construct tractable hierarchies of (upper and lower) bounds for fmin,K, based on using sums of squares of polynomials and semideﬁnite programming (SDP). The starting point is to reformulate fmin,K as the problem of ﬁnding the largest scalar λ for which the polynomial f − λ is nonnegative over K and then to replace the hard positivity condition by a suitable sum of squares decomposition. Alternatively, one may reformulate fmin,K as the problem of ﬁnding a probability measure µ on K minimizing the integral K fdµ. These two dual points of view form the basis of the approach developed by Lasserre [15] for building hierarchies of semideﬁnite programming based lower bounds for fmin,K (see also [16,19] for an overview). Asymptotic convergence to fmin,K holds (under some mild conditions on the set K). Moreover, error estimates have been shown in [26,24] when K is a general basic closed semi-algebraic set, and in [4,5,6,7,9,11,27] for simpler sets like the standard simplex, the hypercube and the unit sphere. In particular, [26] shows that the rate of convergence of the hierarchy of lower bounds based on Schmu¨dgen’s Positivstellensatz is in the order O(1/√c 2r), while [24] shows a convergence rate in O(1/

c

log(2r/c )) for the (weaker) hierarchy of bounds based on Putinar’s Positivstellensatz. Here, c,c are constants (not explicitly known) depending only on K, and 2r is the selected degree bound. For the case of the hypercube, [4] shows (using Bernstein approximations) a convergence rate in O(1/r) for the lower bounds based on Schmu¨dgen’s Positivstellensatz.

On the other hand, by selecting suitable probability measures on K, one obtains upper bounds for fmin,K. This approach has been investigated, in particular, for minimization over the standard simplex and when selecting some discrete distributions over the grid points in the simplex. The multinomial distribution is used in [23,6] to show convergence in O(1/r) and the multivariate hypergeometric distribution is used in [7] to show convergence in O(1/r2) for quadratic minimization over the simplex (and in the general case assuming a rational minimizer exists).

Additionnally, Lasserre [17] shows that, if we ﬁx any measure µ on K, then it suﬃces to search for a polynomial density function h which is a sum of squares and minimizes the integral K fhdµ in order to compute the minimum fmin,K over K (see Theorem 1 below). By adding degree constraints on the polynomial density h we get a hierarchy of upper bounds for fmin,K and our main objective in this paper is to analyze the quality of this hierarchy of upper bounds for fmin,K. Next we will recall this result of Lasserre [17] and then we describe our main results.

- 1.2 Lasserre’s hierarchy of upper bounds


Throughout, R[x] = R[x1,...,xn] is the set of polynomials in n variables with real coeﬃcients, and R[x]r is the set of polynomials with degree at most r. Σ[x] is the set of sums of squares of polynomials, and Σ[x]r = Σ[x]∩R[x]2r consists of all sums of squares of polynomials with degree at

most 2r. We now recall the result of Lasserre [17], which is based on the following characterization for nonnegative continuous functions on a compact set K.

- Theorem 1 [17, Theorem 3.2] Let K ⊆ Rn be compact, let µ be an arbitrary ﬁnite Borel measure supported by K, and let f be a continuous function on Rn. Then, f is nonnegative on K if and only if

K

g2fdµ ≥ 0 ∀g ∈ R[x].

Therefore, the minimum of f over K can be expressed as

fmin,K = inf

h∈Σ[x] K

hfdµ s.t.

K

hdµ = 1. (1)

Note that formula (1) does not appear explicitly in [17, Theorem 3.2], but one can derive it easily from it. Indeed, one can write fmin,K = sup{λ : f(x) − λ ≥ 0 over K}. Then, by the ﬁrst part of Theorem 1, we have fmin,K = sup λ : K h(f − λ)dµ ≥ 0 ∀h ∈ Σ[x] . As K h(f − λ)dµ =

K hfdµ − λ K hdµ, after normalizing K hdµ = 1, we can conclude (1). If we select the measure µ to be the Lebesgue measure in Theorem 1, then we obtain the following reformulation for fmin,K, which we will consider in this paper:

fmin,K = inf

h∈Σ[x] K

h(x)f(x)dx s.t.

K

h(x)dx = 1.

By bounding the degree of the polynomial h ∈ Σ[x] by 2r, we can deﬁne the parameter:

f(Kr) := inf

h∈Σ[x]r K

h(x)f(x)dx s.t.

K

h(x)dx = 1. (2)

Clearly, the inequality fmin,K ≤ f(Kr) holds for all r ∈ N. Lasserre [17] gives conditions under which the inﬁmum is attained in the program (2).

- Theorem 2 [17, Theorems 4.1 and 4.2] Assume K ⊆ Rn is compact and has nonempty interior and let f be a polynomial. Then, the program (2) has an optimal solution for every r ∈ N and


f(Kr) = fmin,K.

lim

r→∞

We now recall how to compute the parameter f(Kr) in terms of the moments mα(K) of the Lebesgue measure on K, where

and xα := ni=1 xα

i .

i

mα(K) :=

xαdx for α ∈ Nn,

K

Let N(n,r) := {α ∈ Nn : ni=1 αi ≤ r}, and suppose f(x) = β∈N(n,d) fβxβ has degree d. If we write h ∈ Σ[x]r as h(x) = α∈N(n,2r) hαxα, then the parameter f(Kr) from (2) can be reformulated as follows:

f(Kr) = min

fβ

hαmα+β(K) (3)

β∈N(n,d)

α∈N(n,2r)

s.t.

hαmα(K) = 1,

α∈N(n,2r)

hαxα ∈ Σ[x]r.

α∈N(n,2r)

Hence, if we know the moments mα(K) for all α ∈ Nn with |α| := ni=1 αi ≤ d + 2r, then we can compute the parameter f(Kr) by solving the semideﬁnite program (3) which involves a LMI of size n+22r r . So the bound f(Kr) can be computed in polynomial time for ﬁxed d and r (to any ﬁxed precision).

When K is the standard simplex ∆n = {x ∈ Rn+ : ni=1 xi ≤ 1}, the unit hypercube Qn = [0,1]n, or the unit ball B1(0) = {x ∈ Rn : x ≤ 1}, there exist explicit formulas for the moments mα(K). Namely, for the standard simplex, we have

n i=1 αi!

mα(∆n) =

, (4)

(|α| + n)!

see e.g., [14, equation (2.4)] or [12, equation (2.2)]. From this one can easily calculate the moments for the hypercube Qn:

mα(Qn) =

n

xαdx =

Qn

i=1

n

1

1 αi + 1

xα

.

i dxi =

i

0

i=1

To state the moments for the unit Euclidean ball, we will use the notation [n] := {1,...,n}, the Euler gamma function Γ(·), and the notation for the double factorial of an integer k:

 

- k · (k − 2)···3 · 1, if k > 0 is odd,
- k · (k − 2)···4 · 2, if k > 0 is even, 1 if k = 0 or k = −1.


k!! =



In terms of this notation, the moments for the unit Euclidean ball are given by:

mα(B1(0)) =

(n−1)/22(n+1)/2 ni=1(αi−1)!!

πn/2 ni=1(αi−1)!! Γ(1+n+2|α|)2|α|/2

= π

(n+|α|)!! if αi is even for all i ∈ [n], 0 otherwise.

(5)

One may prove relation (5) using

xαdx =

B1(0)

1 Γ(1 + (n + |α|)/2) Rn

xαexp − x 2 dx

#### (see, e.g., [18, Theorem 2.1]), together with the fact (see, e.g., page 872 in [17]) that

√2π(p − 1)!! if p is even, 0 if p is odd,

+∞

tp exp −t2/2 dt =

−∞

√π for all integers k ∈ N (see e.g., [1, Section 6.1.12]).

and the identity Γ(1 + k2) = 2 k!!

(k+1)/2

For a general polytope K ⊆ Rn, it is a hard problem to compute the moments mα(K). In fact, the problem of computing the volume of polytopes of varying dimensions is already #P-hard [10]. On the other hand, any polytope K ⊆ Rn can be triangulated into ﬁnitely many simplices (see e.g., [8]) so that one could use (4) to obtain the moments mα(K) of K. The complexity of this method depends on the number of simplices in the triangulation. However, this number can be exponentially large (e.g., for the hypercube) and the problem of ﬁnding the smallest possible triangulation of a polytope is NP-hard, even in ﬁxed dimension n = 3 (see e.g., [8]).

Example

Consider the minimization of the Motzkin polynomial f(x1,x2) = x41x22 +x21x42 −3x21x22 +1 over the hypercube K = [−2,2]2, which has four global minimizers at the points (±1,±1), and fmin,K = 0. Figure 1 shows the computed optimal sum of squares density function h∗, for r = 12, corresponding

to f(12)K = 0.406076. We observe that the optimal density h∗ shows four peaks at the four global minimizers and thus, it appears to approximate the density of a convex combination of the Dirac

measures at the four minimizers.

- 0

- 0.5

- 1


- 1.5

- 2


0.8

0.6

*h(x,x)12

0.4

0.2

−0.5

0

−1

2

1

2

−1.5

1

0

0

−1

−1

−2

−2

−2 −1.5 −1 −0.5 0 0.5 1 1.5 2

−2

x2 x1

Fig. 1 Graph and contour plot of h∗(x) on [−2, 2]2 (r = 12 and deg(h∗) = 24) for the Motzkin polynomial.

We will present several additional numerical examples in Section 4.

- 1.3 Our main results


In this paper we analyze the quality of the upper bounds f(Kr) from (2) for the minimum fmin,K of f over K. Our main result is an upper bound for the range f(Kr) − fmin,K, which applies to the

a

##### K

b

Fig. 2 This set K does not satisfy Assumption 1 at the points a and b.

case when f is Lipschitz continuous on K and when K is a full-dimensional compact set satisfying the additional condition from Assumption 1, see Theorem 3 below. We will use throughout the following notation about the set K.

We let D(K) = maxx,y∈K x − y 2 denote the (squared) diameter of the set K, where x = n i=1 xi2 is the 2-norm. Moreover, wmin(K) is the minimal width of K, which is the minimum distance between two distinct parallel supporting hyperplanes of K. Throughout, B (a) := {x ∈ Rn : x − a ≤ } denotes the Euclidean ball centered at a ∈ Rn and with radius > 0. With γn denoting the volume of the n-dimensional unit ball, the volume of the ball B (a) is given by volB (a) = nγn.

We now formulate our geometric assumption about the set K which says (roughly) that around any point a ∈ K there is a ball intersecting a constant fraction of the unit ball. Assumption 1 For all points a ∈ K there exist constants ηK > 0 and K > 0 such that

vol(B (a) ∩ K) ≥ ηKvolB (a) = ηK nγn for all 0 < ≤ K. (6)

Note that Assumption 1 implies that the set K has positive Lebesgue density at all points a ∈ K. For all sets K satisfying Assumption 1, we also deﬁne the parameter

rK := max

D(K)e 2 3K

D(K)e 2

,n if K ≤ 1, and rK :=

if K ≥ 1. (7)

Here, e = 2.71828... denotes the base of the natural logarithm. Note that the parameters ηK, K and rK depend not only on the set K but also on the point a ∈ K; we omit the dependance on a to simplify notation. Assumption 1 will be used in the case when the point a is a global minimizer in K of the polynomial to be analyzed.

For instance, convex bodies and, more generally, compact star-shaped sets satisfy Assumption 1 (see Section 5.1). We now give an example of a set K that does not satisfy Assumption 1 and refer to Section 5.1 for more discussion about Assumption 1.

Example 1 Consider the following set K ⊆ R2, displayed in Figure 2:

K = {x ∈ R2 : x ≥ 0,(x1 − 1)2 + (x2 − 1)2 ≥ 1}.

One can easily check that Assumption 1 is not satisﬁed, since the condition (6) does not hold for the two points a and b.

We now present our main result.

- Theorem 3 Assume that K ⊆ Rn is compact and satisﬁes Assumption 1. Then there exists a constant ζ(K) (depending only on K) such that, for all Lipschitz continuous functions f with Lipschitz constant Mf on K, the following inequality holds:


ζ(K)Mf √r

f(Kr) − fmin,K ≤

for all r ≥ rK + 1. (8)

Moreover, if f is a polynomial of degree d and K is a convex body, then

2d2ζ(K)supx∈K |f(x)| wmin(K)

1 √r

f(Kr) − fmin,K ≤

for all r ≥ rK + 1. (9)

The key idea to show this result is to select suitable sums of squares densities which we are able to analyse. For this, we will select a global minimizer a of f over K and consider the Gaussian distribution with mean a and, as sums of squares densities, we will select the polynomials Hr,a obtained by truncating the Taylor series expansion of the Gaussian distribution, see relation (14).

Remark 1 When the polynomial f has a root in K (which can be assumed without loss of generality), the parameter supx∈K |f(x)| involved in relation (9) can easily be upper bounded in terms of the range of values of f; namely,

|f(x)| ≤ fmax,K − fmin,K,

sup

x∈K

where fmax,K denotes the maximum value of f over K. Hence relation (9) also implies an upper bound on f(Kr)−fmin,K in terms of the range fmax,K−fmin,K, as is commonly used in approximation analysis (see, e.g., [3,5]).

- 1.4 Contents of the paper Our paper is organized as follows. In Section 2, we give a constructive proof for our main result in


- Theorem 3. In Section 3 we show how to obtain feasible points in K that correspond to the bounds


f(Kr) through sampling. This is followed by a section with numerical examples (Section 4). Finally, in the concluding remarks (Section 5), we revisit Assumption 1, and discuss perspectives for future

research.

### 2 Proof of our main result in Theorem 3

In this section we prove our main result in Theorem 3. Our analysis holds for Lipschitz continuous functions, so we start by reviewing some relevant properties in Section 2.1. In the next step we indicate in Section 2.2 how to select the polynomial density function h as a special sum of squares that we will be able to analyze. Namely, we let a denote a global minimizer of the function f over the set K ⊆ Rn. Then we consider the density function Ga in (12) of the Gaussian distribution with mean a (and suitable variance) and the polynomial Hr,a in (14), which is obtained from the truncation at degree 2r of the Taylor series expansion of the Gaussian density function Ga. The ﬁnal step will be to analyze the quality of the bound obtained by selecting the polynomial Hr,a and this will be the most technical part of the proof, carried out in Section 2.3.

- 2.1 Lipschitz continuous functions

A function f is said to be Lipschitz continuous on K, with Lipschitz constant Mf, if it satisﬁes: |f(y) − f(x)| ≤ Mf y − x for all x,y ∈ K.

If f is continuous and diﬀerentiable on K, then f is Lipschitz continuous on K with respect to the constant

Mf = max x∈K

 ∇f(x) . (10)

Furthermore, if f is an n-variate polynomial with degree d, then the Markov inequality for f on a convex body K reads as

max

x∈K

 ∇f(x) ≤

2d2 wmin(K)

sup

x∈K

|f(x)|,

see e.g., [3, relation (8)]. Thus, together with (10), we have that f is Lipschitz continuous on K with respect to the constant

Mf ≤

2d2 wmin(K)

sup

x∈K

|f(x)|. (11)

- 2.2 Choosing the polynomial density function Hr,a Consider the function


x − a 2 2σ2

1 (2πσ2)n/2

exp −

Ga(x) :=

, (12)

which is the probability density function of the Gaussian distribution with mean a and standard variance σ (whose value will be deﬁned later). Let the constant CK,a be deﬁned by

CK,aGa(x)dx = 1. (13)

K

2

2)n/2e−t evaluated at the point t = x−a

Observe that Ga(x) is equal to the function (2πσ1

2σ2 . Denote by Hr,a the Taylor series expansion of Ga truncated at the order 2r. That is,

1 (2πσ2)n/2

Hr,a(x) =

2r

x − a 2 2σ2

1 k! −

k=0

k

. (14)

Moreover consider the constant crK,a, deﬁned by

crK,aHr,a(x)dx = 1. (15)

K

The next step is to show that Hr,a is a sum of squares of polynomials and thus Hr,a ∈ Σ[x]2r. This follows from the next lemma.

Lemma 1 Let φ2r(t) denote the (univariate) polynomial of degree 2r obtained by truncating the Taylor series expansion of e−t at the order 2r. That is,

2r

(−t)k k!

φ2r(t) :=

.

k=0

Then φ2r is a sum of squares of polynomials. Moreover, we have

t2r+1 (2r + 1)!

0 ≤ φ2r(t) − e−t ≤

for all t ≥ 0. (16)

Proof First, we show that φ2r is a sum of squares. As φ2r is a univariate polynomial, by Hilbert’s Theorem (see e.g., [19, Theorem 3.4]), it suﬃces to show that φ2r(t) ≥ 0 for all t ∈ R. As φ2r(−∞) = φ2r(+∞) = +∞, it suﬃces to show that φ2r(t) ≥ 0 at all the stationary points t where φ 2r(t) = 0. For this, observe that φ 2r(t) = 2kr=1(−1)k t

k−1

(k−1)!, so that it can be written as φ 2r(t) = −φ2r(t) + t2r

2r

(2r)!. Hence, for all t with φ 2r(t) = 0, we have φ2r(t) = t

(2r)! ≥ 0. Next, we show that φ2r(t) ≥ e−t for all t ≥ 0. Fix t ≥ 0. Then, by Taylor Theorem (see e.g., [29]), one has e−t = φ2r(t) + φ

(2r+1)(ξ)t2r+1

(2r+1)! for some ξ ∈ [0,t]. As φ(2r+1)(ξ) = −e−ξ, one can conclude that e−t − φ2r(t) = −e

−ξt2r+1 (2r+1)! ≤ 0 and e−t − φ2r(t) ≥ − t

2r+1

(2r+1)!.

We now consider the parameter fK(r,a) deﬁned as

fK(r,a) :=

f(x)crK,aHr,a(x)dx. (17)

K

Our main technical result is the following upper bound for the range fK(r,a) − fmin,K.

- Theorem 4 Assume K ⊆ Rn is compact and satisﬁes Assumption 1, and consider the parameter rK from (7). Then there exists a constant ζ(K) (depending only on K) such that, for all Lipschitz continuous functions f with Lipschitz constant Mf on K, the following inequality holds:


ζ(K)Mf √2r + 1

fK(r,a) − fmin,K ≤

, for all r ≥

rK 2

. (18)

Moreover, if f is a polynomial of degree d and K is a convex body, then

2d2ζ(K)supx∈K |f(x)| wmin(K)√2r + 1

fK(r,a) − fmin,K ≤

, for all r ≥

rK 2

. (19)

We will give the proof of Theorem 4, which has lengthy technical details, in Section 2.3 below. We now show how to derive Theorem 3 as a direct application of Theorem 4.

Proof (of Theorem 3) Assume f is Lipschitz continuous with Lipschitz constant Mf on K and a is a minimizer of f over the set K. Using the deﬁnitions (2) and (17) of the parameters and the fact that Hr,a is a sum of squares with degree 4r, it follows that

f(2Kr+1) ≤ f(2Kr) ≤ fK(r,a) , for all r ∈ N. Then, from inequality (18) in Theorem 4, one obtains

ζ(K)Mf √2r + 1

f(2Kr+1) − fmin,K ≤ f(2Kr) − fmin,K ≤ fK(r,a) − fmin,K ≤

rK 2

for all r ≥

.

Hence, for all r ≥ rK + 1,

ζ(K)Mf √r

ζ(K)Mf √r + 1 ≤

f(Kr) − fmin,K ≤

ζ(K)Mf √r

f(Kr) − fmin,K ≤

for odd r.

for even r,

This concludes the proof for relation (8), and relation (9) follows from (19) in an analogous way. This ﬁnishes the proof of Theorem 3.

2.3 Analyzing the polynomial density function Hr,a In this section we prove the result of Theorem 4. Recall that a is a global minimizer of f over K. For the proof, we will need the following four technical lemmas. Lemma 2 Assume K ⊆ Rn is compact and satisﬁes Assumption 1. Then, for all 0 < ≤ K and r ∈ N, we have:

2

(2πσ2)n/2 exp

2σ2 ηK nγn

crK,a ≤ CK,a ≤

. (20)

Proof By Lemma 1, φ2r(t) ≥ e−t for all t ≥ 0, which implies Hr,a(x) ≥ Ga(x) for all x ∈ Rn. Together with the relations (13) and (15) deﬁning the constants CK,a and crK,a, we deduce that crK,a ≤ CK,a. Moreover, by the deﬁnition (13) of the constant CK,a, one has

x − a 2 2σ2

1 (2πσ2)n/2

1 CK,a

exp −

=

Ga(x)dx =

dx

K

K

x − a 2 2σ2

1 (2πσ2)n/2

exp −

≥

dx

K∩B (a)

2

1 (2πσ2)n/2

vol(K ∩ B (a)).

≥

exp −

2σ2

We now use relation (6) from Assumption 1 in order to conclude that vol(K ∩ B (a)) ≥ ηK nγn, which gives the desired upper bound on CK,a.

- Lemma 3 Given x˜ ∈ Rn and a function F : R+ → R, deﬁne the function f : Rn → R by f(x) = F( x − x˜ ) for all x ∈ Rn. Then, for all ρ2 ≥ ρ1 ≥ 0, one has

Bρ2(˜x)\Bρ1(˜x)

f(x)dx = nγn

ρ2

ρ1

zn−1F(z)dz,

where γn = π

(n−1)/22(n+1)/2

n!! is the volume of the unit Euclidean ball in Rn. Proof Apply a change of variables using spherical coordinates as explained, e.g., in [2].

- Lemma 4 For all positive integers r and n, one has 2r 1+1

− 4(2r+1)+2n n

< 6n. Proof Let n ∈ N be given. Denote

g(r) :=

- 1

- 2r + 1


− 4(2r+1)+2n n

= (2r + 1)

n 4(2r+1)+2n

(r ≥ 0).

Observe that, g(0) = 1, g(r) > 0 for all r ≥ 0, ln(g(r)) = 8r+4+2n n ln(2r+1), and thus limr→∞ g(r) =

1. It suﬃces to show g(r∗) < 6n for all stationary points r∗. Since

dln(g(r)) dr

= −8nln(2r + 1) (8r + 4 + 2n)2

+

2n (2r + 1)(8r + 4 + 2n)

,

and g (r) = g(1r) dln(drg(r)), any stationary point r∗ satisﬁes

dln(g(r∗)) dr

= 0 ⇐⇒ (2r∗ + 1)[ln(2r∗ + 1) − 1] =

n 2

. Since

(2r∗ + 1)(ln(3) − 1) ≤ (2r∗ + 1)[ln(2r∗ + 1) − 1] =

n 2

,

one has 2r∗+1 ≤ 2(ln(3)n −1) < 6n. Since g(r) ≤ 2r+1 for all r ≥ 0, one has g(r∗) ≤ 2r∗+1 < 6n.

- Lemma 5 Assume K ⊆ Rn is compact and satisﬁes Assumption 1. Then, for all 0 < ≤ K, one has


nσn+1p(n) nηK

2 2σ2

CK,a x − a Ga(x)dx ≤ +

e

,

K

where p(n) := 0 +∞ tne−t

2/2dt is a constant depending on n, given by

 

1 if n = 1,

k j=1 (2j − 1) if n = 2k and k ≥ 1,

π 2

p(n) =

(21)



k j=1 (2j) if n = 2k + 1 and k ≥ 1.

Proof Let ϕ := K CK,a x − a Ga(x)dx denote the integral that we need to upper bound. We split the integral ϕ as ϕ = ϕ1 + ϕ2, depending on whether x lies in the ball B (a) or not. First, we upper bound the term ϕ1 as

ϕ1 :=

K∩B (a)

x − a CK,aGa(x)dx ≤

Second, we bound the integral

CK,aGa(x)dx ≤

K∩B (a)

CK,aGa(x)dx =  .

K

ϕ2 := CK,a

Since K ⊆ B√

D(K)(a), one has

K\B (a)

x − a Ga(x)dx.

ϕ2 ≤ CK,a

B√

D(K)(a)\B (a)

x − a Ga(x)dx,

where the right hand side, by Lemma 3, is equal to

√

D(K)

z2 2σ2

CK,anγn (2πσ2)n/2

zn exp −

dz.

By a change of variable t = σz , one obtains

CK,anγnσ (2π)n/2

ϕ2 ≤

√

D(K)/σ

t2 2

tn exp −

 /σ

dt,

and thus

CK,anγnσ (2π)n/2

ϕ2 ≤

+∞

t2 2

tn exp −

0

CK,anγnσ (2π)n/2

dt =

p(n).

2

Here we have set p(n) := 0 +∞ tne−t

2 dt which can be checked to be given by (21) (e.g., using induction on n). Now, combining with the upper bound for CK,a from (20), we obtain

nσn+1p(n) nηK

ϕ2 ≤

2 2σ2

.

e

Therefore, we have shown:

nσn+1p(n) nηK

2 2σ2

ϕ = ϕ1 + ϕ2 ≤ +

, which shows the lemma.

e

We are now ready to prove Theorem 4.

Proof (of Theorem 4) Observe that, if f is a polynomial, then we can use the upper bound (11) for its Lipschitz constant and thus the inequality (19) follows as a direct consequence of the inequality (18). Therefore, it suﬃces to show the relation (18).

Recall that a is a minimizer of f over K. As f is Lipschitz continuous with Lipschitz constant Mf on K, we have

f(x) − f(a) ≤ Mf x − a ∀x ∈ K. This implies

fK(r,a) − fmin,K =

crK,aHr,a(x)(f(x) − f(a))dx ≤ Mf

K

K

x − a crK,aHr,a(x)dx.

Our objective is now to show the existence of a constant ζ(K) such that

ψ :=

ζ(K) √2r + 1

crK,a x − a Hr,a(x)dx ≤

, for all r ≥ rK, (see (7))

K

by which we can then conclude the proof for (18). For this, we split the integral ψ as the sum of two terms:

ψ =

crK,a x − a Ga(x)dx

+

K

=:ψ1

crK,a x − a (Hr,a(x) − Ga(x))dx.

K

=:ψ2

First, we upper bound the term ψ1. As crK,a ≤ CK,a (by (20)), we can use Lemma 5 to conclude that, for all 0 < ≤ K,

nσn+1p(n) nηK

nσn+1p(n) n+1ηK

2 2σ2

2 2σ2

ψ1 ≤

CK,a x − a Ga(x)dx ≤ +

=  µ1. (22)

= 1 +

e

e

K

=:µ1

Second we bound the integral

ψ2 =

crK,a x − a (Hr,a(x) − Ga(x))dx.

K

We can upper bound the function Hr,a(x) − Ga(x) using the estimate from (16) and we get

x − a 4r+2 (2σ2)2r+1(2r + 1)!

1 (2πσ2)n/2

Hr,a(x) − Ga(x) ≤

.

Then we have

1 (2πσ2)n/2 K

ψ2 ≤

x − a 4r+3 (2σ2)2r+1(2r + 1)!

crK,a

dx =

crK,a (2σ2)2r+1(2r + 1)! K

1 (2πσ2)n/2

x − a 4r+3dx.

Now we upper bound the integral K x − a 4r+3dx. Since K ⊆ B√

D(K)(a), one has

K

x − a 4r+3dx ≤

B√

D(K)(a)

x − a 4r+3dx,

where the right hand side, by Lemma 3, is equal to

√

4r+n+3 2

D(K)

nγnD(K)

4r+n+3

z4r+n+2dz =

4r + n + 3 ≤ nγnD(K)

2 .

nγn

0

Thus, we obtain

crK,a (2σ2)2r+1(2r + 1)!

1 (2πσ2)n/2

4r+n+3

ψ2 ≤

2 .

nγnD(K)

We now use the upper bound for crK,a from (20):

and we obtain

2

(2πσ2)n/2 exp

2σ2 ηK nγn

crK,a ≤

2

4r+n+3 2

nexp

2σ2 D(K)

ψ2 ≤

.

ηK n(2r + 1)!(2σ2)2r+1

Finally we use the Stirling’s inequality:

(2r + 1)! ≥ 2π(2r + 1)

2r + 1 e

2r+1

,

and obtain

2

n+1 2

nexp

2σ2 D(K)

D(K)e 2σ2 n/(2r+1)(2r + 1)

ψ2 ≤

ηK =:µ2

2r+1

µ2 2π(2r + 1)

D(K)e 2σ2 n/(2r+1)(2r + 1)

=

.

2r+1 1 2π(2r + 1)

(23)

We can now upper bound the quantity ψ = ψ1 + ψ2, by combining the upper bound for ψ1 in (22) with the above upper bound (23) for ψ2. That is,

µ2 2π(2r + 1)

ψ ≤  µ1 +

D(K)e 2σ2 n/(2r+1)(2r + 1)

2r+1

.

We now indicate how to select the parameters and σ. First we select σ = , so that both parameters µ1 and µ2 appearing in (22) and (23) are constants depending on n and K, namely

np(n)e1/2 ηK

µ1 = 1 +

n+1 2

ne1/2D(K)

and µ2 =

.

ηK

Next we select so that 2 D(K)e

2+n/(2r+1)(2r+1) = 1, i.e.,

=

D(K)e 2(2r + 1)

2r+1 2(2r+1)+n

=

D(K)e 2

2r+1 2(2r+1)+n

- 1

- 2r + 1


- 1

- 2 − 4(2r+1)+2n n


.

Summarizing, we have shown that

ψ ≤

≤

- 1

- 2r + 1


- 1

- 2r + 1


- 1

- 2−4(2r+1)+2n n D(K)e 2


2r+1 2(2r+1)+n

- 1

- 2


6n µ1 max 1,

D(K)e 2

+

µ2 √2π

µ1 +

- 1

- 2r + 1


n 4(2r+1)+2n

µ2 √2π

. (24)

− 4(2r+1)+2n n

To obtain the last inequality (24), we use the inequality 2r 1+1

< 6n (recall Lemma 4),

2r+1 2(2r+1)+n

n 4(2r+1)+2n

together with the two inequalities D(K2 )e

≤ max 1, D(K2 )e and 2r 1+1

≤ 1.

(2+2rn+1)

Since we have assumed ≤ K (recall Lemma 2), this implies the condition r ≥ D(K4 )e −

K − 21, i.e., the inequality (24) holds for all r ≥ D(K4 )e −

(2+2rn+1)

K − 12. If K ≤ 1 and r ≥ n/2, then we have

−(2+ 2rn+1 ) K ≤ −K3 and thus the inequality (24) holds for all r ≥ max D4(K 3)e

, n2 . If K ≥ 1 then

K

−(2+ 2rn+1 ) K ≤ 1 and thus (24) holds for all integers r ≥ D(K4 )e. Hence, the inequality (24) holds for

all r ≥ rK/2, where rK is as deﬁned in (7). Finally, by deﬁning the constant

ζ(K) := 6n µ1 max 1,

D(K)e 2

µ2 √2π

+

,

which indeed depends only on K and its dimension n, we can conclude the proof for (18).

Remark 2 Note that in the proof of Theorem 4, we use Assumption 1 only for the selected minimizer a ∈ K (and we use it only in the proof of Lemma 2). Hence, if the selected point a lies in the interior of K, i.e., if there exists δ > 0 such that Bδ(a) ⊆ K, then the result of Theorem 4 (and thus Theorem 3) holds when selecting ηK = 1 and K = δ. Our results extend also to unconstrained global minimization:

f∗ := min x∈Rn

f(x),

if we know that f has a global minimizer a and we know a ball Bδ(0) containing a. We can then indeed minimize f over a compact set K, which can be chosen to be the ball Bδ(0) or a suitable hypercube containing a.

### 3 Obtaining feasible solutions through sampling

In this section we indicate how to sample feasible points in the set K from the optimal density function obtained by solving the semideﬁnite program (2).

Let f ∈ R[x] be a polynomial. Suppose h∗(x) ∈ Σ[x]r is an optimal solution of the program (2), i.e., f(Kr) = K f(x)h∗(x)dx and K h∗(x)dx = 1. Then h∗ can be seen as the probability density function of a probability distribution on K, denoted as TK and, for all random vector X = (X1,...,Xn) ∼ TK, the expectation of f(X) is given by:

E[f(X)] =

f(x)h∗(x)dx = f(Kr). (25)

K

As we now recall one can generate random samples x ∈ K from the distribution TK using the well known method of conditional distributions (see e.g., [20, Section 8.5.1]). Then we will observe that

with high probability one of these sample points satisﬁes (roughly) the inequality f(x) ≤ f(Kr) (see Theorem 5 for details).

In order to sample a random vector X = (X1,...,Xn) ∼ TK, we assume that, for each i = 2,...,n, we know the cumulative conditional distribution of Xi given that Xj = xj for j = 1,...,i − 1, deﬁned in terms of probabilities as

Fi(xi | x1,...,xi−1) := Pr[Xi ≤ xi | X1 = x1,...,Xi−1 = xi−1].

Additionally, we assume that we know the cumulative marginal distribution function of Xi, deﬁned as:

Fi(xi) := Pr[Xi ≤ xi].

Then one can generate a random sample x = (x1,...,xn) ∈ K from the distribution TK by the following algorithm:

- • Generate x1 with cumulative distribution function F1(·).
- • Generate x2 with cumulative distribution function F2 (·|x1).

.

- • Generate xn with cumulative distribution function Fn (·|x1,...,xn−1).

Then return x = (x1,x2,...,xn)T.

There remains to explain how to generate a (univariate) sample point x with a given cumulative distribution function F(·), since this operation is carried out at each of the n steps of the above algorithm. For this one can use the classical inverse-transform method (see e.g., [20, Section 8.2.1]), which reduces to sampling from the uniform distribution on [0,1] and can be described as follows:

- • Generate a sample u from the uniform distribution over [0,1].
- • Return x = F−1(u) (if F is strictly monotone increasing, or x = min{y : F(y) ≥ u} otherwise).


Hence, in order to be able to apply the method of conditional distributions for sampling from K we need to solve the equation x = F−1(u). For instance, when F(·) is a univariate polynomial, solving the equation x = F−1(u) reduces to computing the eigenvalues of the corresponding companion matrix (see, e.g., [19, Section 2.4.1]). This applies, e.g., when K is the hypercube or the simplex, as we see below.

As an illustration, we ﬁrst indicate how to compute the cumulative marginal and conditional distributions Fi(·) and Fi(· | x1 ...xi−1) for the case of the hypercube K = Qn = [0,1]n. As before we are given a sum of squares density function h∗(x) on [0,1]n. For i = 1,...,n, deﬁne the polynomial function f1...i ∈ R[x1,...,xi] by

1

1

h∗(x1,...,xn)dxi+1 ···dxn. (26)

···

f1...i(x1,...,xi) =

0

0

Then the cumulative marginal distribution function F1(·) is given by

x1

f1(y)dy

F1(x1) =

0

and, for i = 2,...,n, the cumulative conditional distribution function Fi(· | x1 ...xi−1) is given by

xi 0 f1...i(x1,...,xi−1,y)dy

Fi(xi | x1 ...xi−1) =

.

f1...(i−1)(x1,...,xi−1)

The computation of the cumulative marginal and conditional distributions can be carried out in the same way for the simplex K = ∆n, after replacing the function f1...i ∈ R[x1,...,xi] in (26) by

1−xi−xi+1−···−xn−1

1−xi−···−xn−2

1−xi

h∗(x1,...,xn)dxi+1 ···dxn.

···

f1...i(x1,...,xi) =

0

0

0

Note that in both cases the functions Fi(xi | x1 ...xi−1) are indeed univariate polynomials. We will apply this sampling method to several examples of polynomial minimization over the hypercube and the simplex in the next section.

We now observe that if we generate suﬃciently many samples from the distribution TK then, with high probability, one of these samples is a point x ∈ K satisfying (roughly) f(x) ≤ f(Kr). Theorem 5 Let X ∼ TK. For all > 0,

1 1 +

Pr f(X) ≥ f(Kr) + f(Kr) − fmin,K ≤

.

Proof Let X ∼ TK so that E[f(X)] = f(Kr). Deﬁne the nonnegative random variable Y := f(X) − fmin,K.

Then, one has E[Y ] = f(Kr) − fmin,K. Given > 0, the Markov Inequality (see e.g., [22, Theorem 3.2]) implies

1 1 +

Pr[Y ≥ (1 + )E[Y ]] ≤

.

This completes the proof. For given > 0, if one samples N times independently from TK, one therefore obtains an x ∈ K such that

f(x) < f(Kr) + f(Kr) − fmin,K

N

. For example, if N ≥ 1 + 1 then this probability is at least 1 − 1/e.

with probability at least 1 − 1+ 1

### 4 Numerical examples

In this section, we consider several well-known polynomial test functions from global optimization that are listed in Table 1.

Table 1 Test functions

|Name<br><br>|Formula|Minimum (fmin,K)|Search domain (K)|
|---|---|---|---|
|Booth Function|f = (x1 + 2x2 − 7)2 + (2x1 + x2 − 5)2<br><br>|f(1, 3) = 0|[−10, 10]2|
|Matyas Function|f = 0.26(x21 + x22) − 0.48x1x2<br><br>|f(0, 0) = 0<br><br>|[−10, 10]2|
|Three–Hump Camel Function|f = 2x21−1.05x41+16x61+x1x2+ x22<br><br>|f(0, 0) = 0|[−5, 5]2|
|Motzkin Polynomial<br><br>|f = x41x22 + x21x42 − 3x21x22 + 1|f(±1, ±1) = 0<br><br>|[−2, 2]2|
|Styblinski–Tang Function (n-variate)<br><br>|f = ni=1 12x4i − 8x2i + 52xi<br><br>|f(−2.093534, . . . , −2.093534) = −39.16599n|[−5, 5]n|
|Rosenbrock Function (n-variate)<br><br>|f = ni=1−1 100(xi+1 − x2i )2 + (xi − 1)2|f(1, . . . , 1) = 0<br><br>|[−2.048, 2.048]n|
|Matyas Function (Modiﬁed-S)<br><br>|f = 0.26[(20x1−10)2+(20x2− 10)2] − 0.48(20x1 − 10)(20x2 − 10)|f(0.5, 0.5) = 0<br><br>|∆2|
|Three-Hump Camel Function (Modiﬁed-S)|f = 2(10x1 −5)2 −1.05(10x1 − 5)4 + 16(10x1 − 5)6 + (10x1 − 5)(10x2 − 5) + (10x2 − 5)2<br><br>|f(0.5, 0.5) = 0<br><br>|∆2|
|Matyas Function (Modiﬁed-B)<br><br>|f = 0.26[(20x21−10)2+(20x22− 10)2] − 0.48(20x21 − 10)(20x22 − 10)<br><br>|f(±<br><br>√2<br><br>2 , ±<br><br>√2<br><br>2 ) = 0<br><br>|B1(0)|
|Three-Hump Camel Function (Modiﬁed-B)<br><br>|f = 2(10x21 −5)2 −1.05(10x21 − 5)4 + 16(10x21 − 5)6 + (10x21 − 5)(10x22 − 5) + (10x22 − 5)2<br><br>|f(±<br><br>√2<br><br>2 , ±<br><br>√2<br><br>2 ) = 0<br><br>|B1(0)|


For these functions, we calculate the parameter f(Kr) by solving the SDP (3) for increasing values of the order r. As already mentioned by Lasserre [17, Section 4], this computation may be done as

a generalised eigenvalue problem — one does not actually have to use an SDP solver. This follows from the fact that the SDP (3) only has one constraint. In particular, f(Kr) is equal to the largest scalar λ for which A − λB 0, i.e., the smallest generalized eigenvalue of the system:

Ax = λBx (x = 0),

where the symmetric matrices A and B are of order n+r r with rows and columns indexed by N(n,r), and

xα+β+δdx, Bα,β =

xα+βdx α,β ∈ N(n,r). (27)

Aα,β =

fδ

K

K

δ∈N(n,d)

We performed the computation on a PC with Intel(R) Core(TM) i7-4600U CPU (2.10 GHz) and with 8 GB RAM. The generalized eigenvalue computation was done in Matlab using the eig function.

We record the values f(Kr) as well as the CPU times in Tables 2, 3, 4, 5, and 6 for minimization over the hypercube, the simplex and the ball. Note that we only list the time for solving the generalised

eigenvalue problem, and not for constructing the matrices A and B in (27). In other words, we assume the necessary moments are computed beforehand, and that the time needed to construct the matrices A and B in (27) is negligible if the relevant moments are known.

For instance, in Table 2, we have n = 2 and we can compute the parameter f(Kr) up to order r = 20 for four test functions. Moreover, in Tables 3, 4 and 5, we have n = 10,15,20, respectively, and the parameter f(Kr) can be computed up to order r = 5, r = 4 and r = 3, respectively. Note that in all cases the computation is very fast (at most a few seconds). However, for larger values of n or r we sometimes encountered numerical instability. This may be due to inaccurate calculation of the moments, or to inherent ill-conditioning of the matrices A and B in (27). These issues are of practical importance, but beyond the scope of the present study. Also, one must bear in mind that the order of the matrices A and B grows as n+r r , and this imposes a practical limit on how large the values of n and r may be when computing f(Kr).

Table 2 f(Kr) for Booth, Matyas, Three–Hump Camel and Motzkin Functions over the hypercube

|r|Booth Function| |Matyas Function| |Three–Hump Camel Function| |Motzkin Polynomial| |
|---|---|---|---|---|---|---|---|---|
| |Value|Time (sec.)<br><br>|Value|Time (sec.)<br><br>|Value|Time (sec.)|Value<br><br>|Time (sec.)|
|1<br><br>|244.680<br><br>|0.000666|8.26667<br><br>|0.000739|265.774<br><br>|0.000742<br><br>|4.2<br><br>|0.000719|
|2<br><br>|162.486<br><br>|0.000061|5.32223<br><br>|0.000072|29.0005<br><br>|0.000062|1.06147|0.000088|
|3|118.383<br><br>|0.000083<br><br>|4.28172<br><br>|0.000072|29.0005|0.000066<br><br>|1.06147<br><br>|0.000080|
|4|97.6473|0.000079|3.89427<br><br>|0.000119|9.58064<br><br>|0.000117<br><br>|0.829415<br><br>|0.000118|
|5<br><br>|69.8174|0.000171|3.68942<br><br>|0.000208|9.58064<br><br>|0.000177|0.801069|0.000189|
|6<br><br>|63.5454<br><br>|0.000277<br><br>|2.99563|0.000263<br><br>|4.43983|0.000263<br><br>|0.801069<br><br>|0.000208|
|7|47.0467|0.000423<br><br>|2.54698|0.000343<br><br>|4.43983|0.001146<br><br>|0.708889<br><br>|0.000395|
|8<br><br>|41.6727<br><br>|0.000587<br><br>|2.04307|0.000417<br><br>|2.55032|0.000647|0.565553<br><br>|0.000584|
|9<br><br>|34.2140|0.000657|1.83356<br><br>|0.000655|2.55032<br><br>|0.000586<br><br>|0.565553|0.000766|
|10<br><br>|28.7248<br><br>|0.000997<br><br>|1.47840|0.000780<br><br>|1.71275|0.000782<br><br>|0.507829<br><br>|0.001210|
|11|25.6050|0.001181<br><br>|1.37644|0.009241<br><br>|1.71275|0.001026<br><br>|0.406076<br><br>|0.001261|
|12|21.1869<br><br>|0.001942<br><br>|1.11785<br><br>|0.001753|1.2775|0.001693<br><br>|0.406076<br><br>|0.001712|
|13<br><br>|19.5588|0.002352<br><br>|1.0686<br><br>|0.001857|1.2775<br><br>|0.002031<br><br>|0.3759|0.003427|
|14|16.5854<br><br>|0.002829<br><br>|0.8742<br><br>|0.002253|1.0185<br><br>|0.002629|0.3004|0.003711|
|15<br><br>|15.2815<br><br>|0.003618|0.8524|0.002270<br><br>|1.0185<br><br>|0.002936|0.3004<br><br>|0.002351|
|16<br><br>|13.4626|0.003452|0.7020<br><br>|0.003580|0.8434<br><br>|0.003452<br><br>|0.2819|0.003672|
|17|12.2075|0.004248<br><br>|0.6952|0.004662<br><br>|0.8434|0.004652|0.2300<br><br>|0.004349|
|18<br><br>|11.0959|0.005217|0.5760<br><br>|0.005510|0.7113<br><br>|0.004882<br><br>|0.2300|0.006060|
|19|9.9938|0.007200<br><br>|0.5760<br><br>|0.005610|0.7113|0.006752<br><br>|0.2185|0.007641|
|20<br><br>|9.2373|0.009707<br><br>|0.4815|0.006975<br><br>|0.6064|0.007031<br><br>|0.1817|0.007686|


Furthermore, we use the method described in Section 3 to generate samples that are feasible solutions of (2). We report results for the bivariate Rosenbrock and the Three–Hump Camel functions over the hypercube, and for the Matyas and Three-Hump Camel functions (Modiﬁed-S) over the simplex. For each order r ≥ 1, the sample sizes 20 and 1000 are used. We also generate samples uniformly from the feasible set, for comparison. We give the results in Tables 7, 8, 9 and 10, where

we record the mean, variance and the minimum value of these samples together with f(Kr) (which equals the sample mean by (25)).

- Table 3 f(Kr) for Styblinski–Tang and Rosenbrock Functions (with n = 10) over the hypercube

|r<br><br>|Sty.–Tang (n = 10)| |Rosenb. (n = 10)| |
|---|---|---|---|---|
| |Value|Time (sec.)<br><br>|Value|Time (sec.)|
|1|−57.1688<br><br>|0.098|3649.85|0.0005|
|2|−94.5572<br><br>|0.001|2813.66<br><br>|0.0009|
|3<br><br>|−108.873<br><br>|0.011|2393.63<br><br>|0.0156|
|4|−132.8810<br><br>|0.349<br><br>|1956.81|0.4004|
|5<br><br>|−146.7906|9.245<br><br>|1701.85|12.997|


- Table 4 f(Kr) for Styblinski–Tang and Rosenbrock Functions (with n = 15) over the hypercube

|r<br><br>|Sty.–Tang (n = 15)| |Rosenb. (n = 15)| |
|---|---|---|---|---|
| |Value<br><br>|Time (sec.)|Value|Time (sec.)|
|1|−82.8311|0.001071|5887.5<br><br>|0.094693|
|2|−130.464<br><br>|0.001707|4770.71<br><br>|0.002282|
|3<br><br>|−148.5594|0.170907|4160.78<br><br>|0.157897|
|4<br><br>|−180.9728|16.796383<br><br>|3552.04<br><br>|24.696591|


- Table 5 f(Kr) for Styblinski–Tang and Rosenbrock Functions (with n = 20) over the hypercube

|r|Sty.–Tang (n = 20)<br><br>| |Rosenb. (n = 20)| |
|---|---|---|---|---|
| |Value|Time (sec.)|Value|Time (sec.)|
|1<br><br>|−107.875<br><br>|0.972741|8158.36|0.000949|
|2<br><br>|−164.11<br><br>|0.344403<br><br>|6806.74<br><br>|0.011370|
|3<br><br>|−185.6488|2.655447|6029.02<br><br>|2.955319|


- Table 6 f(Kr) for Matyas and Three-Hump Camel Functions (Modiﬁed) over the Simplex and the Euclidean ball.


|r<br><br>|Matyas (Modiﬁed-S)| |Th.-H. C. (Modiﬁed-S)<br><br>| |Matyas (Modiﬁed-B)<br><br>| |Th.-H. C. (Modiﬁed-B)| |
|---|---|---|---|---|---|---|---|---|
| |Value|Time (sec.)<br><br>|Value<br><br>|Time (sec.)|Value|Time (sec.)<br><br>|Value<br><br>|Time (sec.)|
|1<br><br>|7.2243<br><br>|0.222604|84.354<br><br>|0.000457|18.000<br><br>|0.000379|146.41<br><br>|0.000454|
|2<br><br>|4.6536<br><br>|0.000085<br><br>|22.398<br><br>|0.000081|6.3995<br><br>|0.000049|138.91<br><br>|0.000052|
|3<br><br>|3.9404<br><br>|0.000124|12.353|0.000115<br><br>|6.3995|0.000054|48.508|0.000069|
|4<br><br>|3.7067<br><br>|0.000176|3.9153<br><br>|0.000112|4.4091<br><br>|0.000133|39.673<br><br>|0.000111|
|5<br><br>|3.2317|0.000696<br><br>|2.9782|0.000489<br><br>|4.4091|0.000187<br><br>|18.045|0.000264|
|6|2.7328<br><br>|0.000275<br><br>|1.3303|0.000255|3.9652<br><br>|0.000292<br><br>|13.881<br><br>|0.000309|
|7|2.2985|0.000511|1.1773<br><br>|0.000334<br><br>|3.9652<br><br>|0.000323|7.7876<br><br>|0.000300|
|8<br><br>|1.9536<br><br>|0.001432|0.77992|0.000560<br><br>|3.8536|0.000395|5.7685<br><br>|0.000608|
|9|1.6639|0.000709<br><br>|0.73202<br><br>|0.000666|3.8536|0.000517<br><br>|3.8699<br><br>|0.000636|
|10|1.4293<br><br>|0.003370|0.60846<br><br>|0.001034|3.4943<br><br>|0.000687|2.8359|0.000704|


Note that the average of the sample function values approximate f(Kr) reasonably well for sample size 1000, but poorly for sample size 20. Moreover, the average sample function value for uniform

sampling from K is much higher than f(Kr). Also, the minimum function value for sampling from TK is signiﬁcantly lower than the minimum function value obtained by uniform sampling for most

values of r. In terms of generating “good” feasible solutions, sampling from TK therefore outperforms uniform sampling from K for these examples, as one would expect.

Table 7 Sampling results for the Rosenbrock Function (n = 2) over the hypercube

|r<br><br>|f(Kr)<br><br>|Mean<br><br>|Variance|Minimum<br><br>|Sample Size|
|---|---|---|---|---|---|
|1<br><br>|214.648|121.125<br><br>|14005.5<br><br>|0.00451826<br><br>|20|
| | |209.9|80699.0|0.0008754|1000|
|2|152.310|184.496<br><br>|58423.9|4.94265<br><br>|20|
| | |149.6<br><br>|54455.0|0.02805<br><br>|1000|
|3|104.889<br><br>|146.618<br><br>|64611.2|0.0113339<br><br>|20|
| | |110.1<br><br>|26022.0|0.0665|1000|
|4<br><br>|75.6010|62.4961<br><br>|5803.21<br><br>|0.0542813|20|
| | |75.65|45777.0|0.007285<br><br>|1000|
|5<br><br>|51.5037|58.4032<br><br>|4397.0|0.668679<br><br>|20|
| | |50.64<br><br>|6285.0<br><br>|0.01382<br><br>|1000|
|6<br><br>|41.7878|35.4183<br><br>|2936.24|1.16154|20|
| | |37.64<br><br>|3097.0|0.06188<br><br>|1000|
|7|30.1392<br><br>|29.6545|1022.2<br><br>|1.05813<br><br>|20|
| | |27.11<br><br>|1332.0<br><br>|0.02044|1000|
|8<br><br>|25.8329<br><br>|19.5392|301.334<br><br>|0.505628<br><br>|20|
| | |34.32<br><br>|4106.0<br><br>|0.074|1000|
|9<br><br>|19.4972<br><br>|20.8982|328.475|0.564992<br><br>|20|
| | |18.65<br><br>|593.6<br><br>|0.07951<br><br>|1000|
|10|17.3999<br><br>|9.37959<br><br>|146.496|0.562473|20|
| | |15.33<br><br>|685.7<br><br>|0.1448|1000|
|11|13.6289<br><br>|8.74923|52.1436<br><br>|0.75774<br><br>|20|
| | |15.7<br><br>|7498.0<br><br>|0.1719|1000|
|12|12.5024<br><br>|5.43151<br><br>|66.561|0.438172<br><br>|20|
| | |12.7<br><br>|764.7|0.0945<br><br>|1000|
|Uniform Sample<br><br>| |489.722|433549.0|9.0754<br><br>|20|
| | |465.729|361150.0<br><br>|0.0771463<br><br>|1000|


### 5 Concluding remarks

We conclude with some additional remarks on Assumption 1, and some discussion on perspectives for future work.

5.1 Revisiting Assumption 1

In this section we consider in more detail Assumption 1, the geometric assumption which we made about the set K. First we recall another condition, known as the interior cone condition, which is classically used in approximation theory (see, e.g., Wendland [28]).

- Deﬁnition 1 [28, Deﬁnition 3.1] A set K ⊆ Rn is said to satisfy an interior cone condition if there exist an angle θ ∈ (0,π/2) and a radius ρ > 0 such that, for every x ∈ K, a unit vector ξ(x) exists such that the set


C(x,ξ(x),θ,ρ) := {x + λy : y ∈ Rn, y = 1,yTξ(x) ≥ cosθ,λ ∈ [0,ρ]} (28) is contained in K.

For instance, as we now recall, Euclidean balls and star-shaped sets satisfy the interior cone condition.

###### Table 8 Sampling results for the Three–Hump Camel Function over the hypercube

|r|fK(r)<br><br>|Mean|Variance<br><br>|Minimum|Sample Size|
|---|---|---|---|---|---|
|1<br><br>|265.774|216.773<br><br>|177142.0<br><br>|0.106854|20|
| | |261.23|193466.0<br><br>|0.11705|1000|
|2<br><br>|29.0005<br><br>|28.0344|2964.85|1.1718<br><br>|20|
| | |27.712<br><br>|6712.8|0.014255<br><br>|1000|
|3|29.0005<br><br>|14.9951|523.904<br><br>|0.452655<br><br>|20|
| | |32.363|16681.0|0.0088426<br><br>|1000|
|4|9.58064<br><br>|2.99756|14.1201|0.175016<br><br>|20|
| | |10.364<br><br>|1944.0<br><br>|0.010013|1000|
|5<br><br>|9.58064|4.41907<br><br>|14.1358|0.419394|20|
| | |9.1658<br><br>|643.88|0.0015924<br><br>|1000|
|6<br><br>|4.43983|7.98481<br><br>|245.089|0.126147<br><br>|20|
| | |4.5791<br><br>|493.12|0.0035581|1000|
|7<br><br>|4.43983<br><br>|3.96711<br><br>|20.3193|0.260331<br><br>|20|
| | |3.7911<br><br>|57.847|0.0076111|1000|
|8<br><br>|2.55032|2.18925<br><br>|3.87943|0.0310113|20|
| | |2.2302|8.3767<br><br>|0.0028817<br><br>|1000|
|9<br><br>|2.55032|1.38102<br><br>|2.27433<br><br>|0.138641<br><br>|20|
| | |3.2217<br><br>|812.18|0.00014805<br><br>|1000|
|10<br><br>|1.71275|1.03179<br><br>|0.992636|0.0645815|20|
| | |1.5069<br><br>|3.9581|0.0014225|1000|
|11<br><br>|1.71275<br><br>|1.30757|1.90985|0.0320489<br><br>|20|
| | |1.6379<br><br>|7.2518|0.0021144<br><br>|1000|
|12<br><br>|1.27749|0.841194<br><br>|0.914514|0.0369565|20|
| | |1.2105|2.3|0.0005154<br><br>|1000|
|Uniform Sample| |304.032<br><br>|163021.0|1.65885|20|
| | |243.216<br><br>|183724.0|0.00975034<br><br>|1000|


###### Table 9 Sampling results for the Matyas Function (Modiﬁed-S) over the simplex

|r<br><br>|fK(r)<br><br>|Mean<br><br>|Variance|Minimum<br><br>|Sample Size|
|---|---|---|---|---|---|
|1<br><br>|7.2243<br><br>|6.3018|37.373<br><br>|1.2448|20|
| | |7.0542<br><br>|64.863|0.31812<br><br>|1000|
|2|4.6536<br><br>|5.7252|34.964<br><br>|1.8924|20|
| | |4.5932<br><br>|8.293|0.91671<br><br>|1000|
|3|3.9404<br><br>|3.5187<br><br>|0.31411|2.4465<br><br>|20|
| | |3.7544<br><br>|1.3576|0.071075|1000|
|4|3.7067|3.4279<br><br>|1.7187|0.92913<br><br>|20|
| | |3.8679|6.5113<br><br>|0.027508|1000|
|5|3.2317<br><br>|3.8273<br><br>|10.173|0.40131<br><br>|20|
| | |3.1485|6.1263<br><br>|0.035796|1000|
|6<br><br>|2.7328<br><br>|2.2606|3.3343<br><br>|0.2595<br><br>|20|
| | |2.5997<br><br>|10.8|0.0016761<br><br>|1000|
|7|2.2985<br><br>|2.4568|4.1652|0.18947<br><br>|20|
| | |2.1541<br><br>|12.868<br><br>|0.002669|1000|
|8<br><br>|1.9536|0.9223|0.94139|0.064404<br><br>|20|
| | |1.9418|9.5627<br><br>|0.0000037429|1000|
|9<br><br>|1.6639<br><br>|1.4446|1.9372<br><br>|0.048915|20|
| | |1.7266<br><br>|16.738<br><br>|0.0019792|1000|
|10|1.4293<br><br>|2.0005<br><br>|2.0226|0.016453<br><br>|20|
| | |1.4917|16.035<br><br>|0.00015252|1000|
|Uniform Sample| |26.428<br><br>|641.59|0.085716<br><br>|20|
| | |11.905<br><br>|256.0<br><br>|0.010946|1000|


Table 10 Sampling results for the Three-Hump Camel Function (Modiﬁed-S) over the simplex

|r<br><br>|f(Kr)<br><br>|Mean<br><br>|Variance|Minimum<br><br>|Sample Size|
|---|---|---|---|---|---|
|1<br><br>|84.354|104.93<br><br>|122488.0<br><br>|0.33441<br><br>|20|
| | |89.732|48238.0|0.0011036|1000|
|2|22.398|37.036<br><br>|9864.0|0.57012<br><br>|20|
| | |22.292<br><br>|10102.0|0.0022204<br><br>|1000|
|3|12.353<br><br>|3.4161<br><br>|49.898|0.28108<br><br>|20|
| | |11.707<br><br>|1515.9|0.00065454|1000|
|4<br><br>|3.9153|2.4193<br><br>|9.0182<br><br>|0.16865|20|
| | |3.6768|592.96|0.0016775<br><br>|1000|
|5<br><br>|2.9782|1.8336<br><br>|6.3414|0.11311<br><br>|20|
| | |2.5237<br><br>|47.619<br><br>|0.00097905<br><br>|1000|
|6<br><br>|1.3303|2.355<br><br>|26.176|0.0092016|20|
| | |1.2134<br><br>|8.7253|0.00040725<br><br>|1000|
|7|1.1773<br><br>|1.0385|1.0569<br><br>|0.053695<br><br>|20|
| | |1.092<br><br>|6.718<br><br>|0.00050329|1000|
|8<br><br>|0.77992<br><br>|0.9737|0.73522<br><br>|0.10604<br><br>|20|
| | |0.72927<br><br>|0.73641<br><br>|0.00048517|1000|
|9<br><br>|0.73202<br><br>|0.69755|0.19107|0.051634<br><br>|20|
| | |0.65302<br><br>|0.28537<br><br>|0.00024601<br><br>|1000|
|10|0.60846<br><br>|0.67575<br><br>|0.17453|0.010351|20|
| | |0.5616<br><br>|0.17821<br><br>|0.00044175|1000|
|Uniform Sample<br><br>| |518.48|354855.0<br><br>|0.9165<br><br>|20|
| | |485.77<br><br>|391577.0<br><br>|0.32713|1000|


- Lemma 6 [28, Lemma 3.10] Every Euclidean ball with radius r > 0 satisﬁes an interior cone condition with radius ρ = r and angle θ = π/3.

Deﬁnition 2 [28, Deﬁnition 11.25] A set K is said to be star-shaped with respect to a ball Br(xc) if, for every x ∈ K, the closed convex hull of {x} ∪ Br(xc) is contained in K.

Proposition 1 [28, Proposition 11.26] If K is bounded, star-shaped with respect to a ball Br(xc), then K satisﬁes an interior cone condition with radius ρ = r and angle θ = 2arcsin r

2

√

D(K)

.

In fact, any set satisfying the interior cone condition also satisﬁes the following stronger version of Assumption 1.

Assumption 2 There exist constants ηK > 0 and K > 0 such that, for all points a ∈ K,

vol(B (a) ∩ K) ≥ ηKvolB (a) = ηK nγn for all 0 < ≤ K. (29)

Hence the only diﬀerence with Assumption 1 is that the constants ηK and K now depend only on the set K and not on the choice of a ∈ K. Clearly, Assumption 2 implies Assumption 1. Moreover, any set satisfying the interior cone condition satisﬁes Assumption 2.

- Lemma 7 If a set K ⊆ Rn satisﬁes the interior cone condition (28) then K also satisﬁes Assumption 2 (and thus Assumption 1), where we set


ηK =

sinθ 1 + sinθ

n

and K = ρ.

Proof Assume that K satisﬁes the interior cone condition (28). Then, using [28, Lemma 3.7], we know that, for every x ∈ K and h ≤ ρ/(1 + sinθ), the closed ball Bhsinθ(x + hξ(x)) is contained in C(x,ξ(x),θ,ρ) and thus in K. Then, for all x0 ∈ K and ∈ (0,ρ], after setting h =  /(1 + sinθ), one can obtain

vol(B (x0) ∩ K) volB (x0) ≥

volC(x0,ξ(x0),θ, ) volB (x0) ≥

volBhsinθ(x0 + hξ(x0)) volB (x0)

=

sinθ 1 + sinθ

n

.

Thus, Assumption 2 holds after setting ηK = 1+sin sinθθ

n

and K = ρ.

As any convex body (i.e., full-dimensional convex and compact) is star-shaped with respect to any ball it contains, the next result follows as a direct application of Proposition 1 and Lemma 7.

Corollary 1 Any convex body satisﬁes the interior cone condition and thus Assumptions 1 and 2.

As an illustration we now consider the parameters ηK, K, and rK (from relation (7)) when K is the hypercube, the simplex and the Euclidean ball.

Remark 3 Consider ﬁrst the case when K is the hypercube Qn = [0,1]n. By Proposition 1, it satisﬁes the interior cone condition with radius ρ = 1/2 and angle θ = 2arcsin 4√ 1n . Hence, Assumption 2 holds with K = 1/2 and ηK =

√16n−1 8n+√16n−1

n

n

(which is ∼ 2√ 1n

for n large).

Moreover, as D(K) = n, it follows that rK = 4ne. Consider now the case when K is the full-dimensional simplex ∆n. By Proposition 1, it satisﬁes the interior cone condition with radius ρ = n+1√n and angle θ = 2arcsin 2√2(n 1+√n) (since the ball with center ρ(1,...,1)T and radius ρ is contained in ∆n). Hence Assumption 2 holds with

√

n

8(n+√n)2−1 4(n+√n)2+

n

K = n+1√n and ηK =

(which is ∼ √ 12n

#### √

for n large). As D(K) = 2, it follows that rK = e(n + √n)3.

8(n+√n)2−1

√3 2+√3

n

Finally, for the Euclidean ball K = B1(0), we have K = 1, ηK =

and rK = max{2e,n}.

5.2 Perspectives

The sampling approach of Section 3 often provides good feasible solutions for the examples in Section 4, even for small values of r. One may therefore explore using the sampling technique (for small r) as a way of generating starting points for multi-start global optimization algorithms.

Another possibility to enhance computation would be to investigate other suﬃcient conditions for nonnegativity of h on K, more general than the sum-of-squares condition studied here. This may result in a faster rate of convergence than for f(Kr).

Finally, understanding the exact rate of convergence of the upper bounds f(Kr) remains an open problem. In particular we do not know whether 1/√r is the right rate of convergence.

### Acknowledgements

We thank Jean Bernard Lasserre for bringing our attention to his work [17] and for several valuable suggestions, and Dorota Kurowicka for valuable discussions on multivariate sampling techniques.

### References

- 1. Abramowitz, M., Stegun, I.A.: Handbook of Mathematical Functions with Formulas, Graphs, and Mathematical Tables. National Bureau of Standards Applied Mathematics Series 55 (1972)
- 2. Blumenson, L.E.: A Derivation of n-Dimensional Spherical Coordinates. The American Mathematical Monthly 67(1), 63–66 (1960)
- 3. De Klerk, E., Den Hertog, D., Elabwabi, G.. On the complexity of optimization over the standard simplex. European journal of operational research, 191, 773–785 (2008)
- 4. De Klerk, E., Laurent, M.: Error bounds for some semideﬁnite programming approaches to polynomial minimization on the hypercube. SIAM Journal on Optimization, 20(6), 3104–3120 (2010)
- 5. De Klerk, E., Laurent, M., Parrilo, P.: A PTAS for the minimization of polynomials of ﬁxed degree over the simplex. Theory of Computer Science 361(2-3), 210–225 (2006)
- 6. De Klerk, E., Laurent, M., Sun, Z.: An alternative proof of a PTAS for ﬁxed-degree polynomial optimization over the simplex. Mathmatical Programming, 151(2), 433–457 (2015)
- 7. De Klerk, E., Laurent, M., Sun, Z.: An error analysis for polynomial optimization over the simplex based on the multivariate hypergeometric distribution. SIAM Journal on Optimization, 25(3), 1498–1514 (2015)
- 8. De Loera, J., Rambau, J., Santos, F.: Triangulations: Structures and algorithms, Book manuscript (2008)
- 9. Doherty, A.C., Wehner, S.: Convergence of SDP hierarchies for polynomial optimization on the hypersphere. arXiv:1210.5048v2 (2013)
- 10. Dyer, M.E., Frieze, A.M.: On the Complexity of Computing the Volume of a Polyhedron. SIAM J. Comput., 17(5), 967–974 (1988)
- 11. Faybusovich, L.: Global optimization of homogeneous polynomials on the simplex and on the sphere. In C. Floudas and P. Pardalos, editors, Frontiers in Global Optimization. Kluwer Academic Publishers (2003)
- 12. Grundmann, A., Moeller, H.M.: Invariant integration formulas for the n-simplex by combinatorial methods. SIAM J. Numer. Anal. 15, 282–290 (1978)
- 13. Henrion, D., Lasserre, J.B., Loefberg, J.: GloptiPoly 3: moments, optimization and semideﬁnite programming. Optim. Method. Softw. 24(4–5) 761–779 (2009)
- 14. Lasserre, J.B., Zeron, E.S.: Solving a class of multivariate integration problems via Laplace techniques. Applicationes Mathematicae, 28(4), 391–405 (2001)
- 15. Lasserre, J.B.: Global optimization with polynomials and the problem of moments. SIAM J. Optim. 11, 796–817

(2001)

- 16. Lasserre, J.B.: Moments, Positive Polynomials and Their Applications. Imperial College Press (2009)
- 17. Lasserre, J.B.: A new look at nonnegativity on closed sets and polynomial optimization. SIAM J. Optim. 21(3), 864–885 (2011)
- 18. Lasserre, J.B.: Unit balls of constant volume: which one has optimal representation? Preprint at arXiv: 1408.1324

(2014)

- 19. Laurent, M.: Sums of squares, moment matrices and optimization over polynomials. In Emerging Applications of Algebraic Geometry, Vol. 149 of IMA Volumes in Mathematics and its Applications, M. Putinar and S. Sullivant (eds.), Springer, pages 157–270 (2009)
- 20. Law, A.M.: Simulation Modeling and Analysis (4th edition). Mc Graw-Hill (2007)
- 21. Mattila, P.: Geometry of Sets and Measures in Euclidean Spaces: Fractals and Rectiﬁability. Cambridge University Press (1999)
- 22. Motwani, R., Raghavan, P.: Randomized Algorithms. Cambridge University Press (1995)
- 23. Nesterov, Y.: Random walk in a simplex and quadratic optimization over convex polytopes. CORE Discussion Paper 2003/71, CORE-UCL, Louvain-La-Neuve (2003)
- 24. Nie, J., Schweighofer, M.: On the complexity of Putinar’s Positivstellensatz. Journal of Complexity, 23(1), 135– 150 (2007)
- 25. Nie, J.: Certifying convergence of Lasserre’s hierarchy via ﬂat truncation. Math. Program. 142(1–2), 485–510

(2013)

- 26. Schweighofer, M.: On the complexity of Schmu¨dgen’s Positivstellensatz. Journal of Complexity, 20, 529–543


(2004)

- 27. Sun, Z.: A reﬁned error analysis for ﬁxed-degree polynomial optimization over the simplex. Journal of the Operations Research Society of China, 2(3), 379–393 (2014)
- 28. Wendland, H.: Scattered Data Approximation. Cambridge University Press (2005)
- 29. Whittaker, E.T., Watson, G.W.: A course of modern analysis (4ed). Cambridge University Press, New York


(1996)

