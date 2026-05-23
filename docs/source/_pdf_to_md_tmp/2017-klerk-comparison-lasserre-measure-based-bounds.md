# arXiv:1703.00744v1[math.OC]2Mar2017

## Comparison of Lasserre’s measure–based bounds for polynomial optimization to bounds obtained by simulated annealing

Etienne de Klerk ∗ Monique Laurent † March 3, 2017

Abstract

We consider the problem of minimizing a continuous function f over a compact set K. We compare the hierarchy of upper bounds proposed by Lasserre in [SIAM J. Optim. 21(3) (2011), pp. 864 − 885] to bounds that may be obtained from simulated annealing.

We show that, when f is a polynomial and K a convex body, this comparison yields a faster rate of convergence of the Lasserre hierarchy than what was previously known in the literature.

Keywords: Polynomial optimization; Semideﬁnite optimization; Lasserre hierarchy; simulated annealing AMS classiﬁcation: 90C22; 90C26; 90C30

### 1 Introduction

We consider the problem of minimizing a continuous function f : Rn → R over a compact set K ⊆ Rn. That is, we consider the problem of computing the parameter:

fmin,K := min x∈K

f(x).

Our goal is to compare two convergent hierarchies of upper bounds on fmin,K, namely measurebased bounds introduced by Lasserre [10], and simulated annealing bounds, as studied by Kalai and Vempala [6]. The bounds of Lasserre are obtained by minimizing over measures on K with sum-ofsquares polynomial density functions with growing degrees, while simulated annealing bounds use Boltzman distributions on K with decreasing temparature parameters.

In this note we establish a relationship between these two approaches, linking the degree and temperature parameters in the two bounds (see Theorem 4.1 for a precise statement). As an application, when f is a polynomial and K is a convex body, we can show a faster convergence rate for the measure-based bounds of Lasserre. The new convergence rate is in O(1/r) (see Corollary 4.3),

∗Tilburg University and Delft University of Technology, E.deKlerk@uvt.nl †Centrum Wiskunde & Informatica (CWI), Amsterdam and Tilburg University, monique@cwi.nl

where 2r is the degree of the sum-of-squares polynomial density function, while the dependence was in O(1/√r) in the previously best known result from [4].

Polynomial optimization is a very active research area in the recent years since the seminal works of Lasserre [8] and Parrilo [13] (see also, e.g., the book [9] and the survey [11]). In particular, hierarchies of (lower and upper) bounds for the parameter fmin,K have been proposed, based on sum-of-squares polynomials and semideﬁnite programming.

For a general compact set K, upper bounds for fmin,K have been introduced by Lasserre [10], obtained by searching for a sum-of-squares polynomial density function of given maximum degree 2r, so as to minimize the integration of f with respect to the corresponding probability measure on K. When f is Lipschitz continuous and under some mild assumption on K (which holds, e.g., when K is a convex body), estimates for the convergence rate of these bounds have been proved in [4] that are in order O(1/√r). Improved rates have been subsequently shown when restricting to special sets K. Related stronger results have been shown for the case when K is the hypercube [0,1]n or [−1,1]n. In [3] the authors show a hierarchy of upper bounds using the Beta distribution, with the same convergence rate in O(1/√r), but whose computation needs only elementary operations; moreover an improved convergence in O(1/r) can be shown, e.g., when f is quadratic. In addition, a convergence rate in O(1/r2) is shown in [2], using distributions based on Jackson kernels and a larger class of sum-of-squares density functions.

In this paper we investigate the hierarchy of measure-based upper bounds of [10] and show that when K is a convex body, convexity can be exploited to show an improved convergence rate in O(1/r), even for nonconvex functions. The key ingredient for this is to establish a relationship with upper bounds based on simulated annealing and to use a known convergence rate result from [6] for simulated annealing bounds in the convex case.

Simulated annealing was introduced by Kirkpatrick et al. [7] as a randomized search procedure for general optimization problems. It has enjoyed renewed interest for convex optimization problems since it was shown by Kalai and Vempala [6] that a polynomial-time implementation is possible. This requires so-called hit-and-run sampling from K, as introduced by Smith [14], that was shown to be a polynomial-time procedure by Lov´sz [12]. Most recently, Abernethy and Hazan [1] showed formal equivalence with a certain interior point method for convex optimization.

This unexpected equivalence between seemingly diﬀerent methods has motivated this current work to relate the bounds by Lasserre [10] to the simulating annealing bounds as well.

In what follows, we ﬁrst introduce the measure-based upper bounds of Lasserre [10]. Then we recall the bounds based on simulated annealing and the known convergence results for a linear objective function f, and we give an explicit proof of their extension to the case of a general convex function f. After that we state our main result and the next section is devoted to its proof. In the last section we conclude with numerical examples showing the quality of the two types of bounds and some ﬁnal remarks.

### 2 Lasserre’s hierarchy of upper bounds

Throughout, R[x] = R[x1,...,xn] is the set of polynomials in n variables with real coeﬃcients and, for an integer r ∈ N, R[x]r is the set of polynomials with degree at most r. Any polynomial f ∈ R[x]r can be written f = α∈N(n,r) fαxα, where we set xα = ni=1 xα

i for α ∈ Nn and

i

N(n,r) = {α ∈ Nn : ni=1 αi ≤ r}. We let Σ[x] denote the set of sums of squares of polynomials, and Σ[x]r = Σ[x] ∩ R[x]2r consists of all sums of squares of polynomials with degree at most 2r.

We recall the following reformulation for fmin,K, established by Lasserre [10]:

h(x)f(x)dx s.t. K h(x)dx = 1. By bounding the degree of the polynomial h ∈ Σ[x] by 2r, we can deﬁne the parameter:

fmin,K = inf

h∈Σ[x] K

f(Kr) := inf

h(x)f(x)dx s.t. K h(x)dx = 1. (1)

h∈Σ[x]r K

Clearly, the inequality fmin,K ≤ f(Kr) holds for all r ∈ N. Lasserre [10] gave conditions under which the inﬁmum is attained in the program (1). De Klerk, Laurent and Sun [4, Theorem 3] established

the following rate of convergence for the bounds f(Kr).

- Theorem 2.1 (De Klerk, Laurent, and Sun [4]). Let f ∈ R[x] and K a convex body. There exist constants Cf,K (depending only on f and K) and rK (depending only on K) such that


Cf,K √r

f(Kr) − fmin,K ≤

for all r ≥ rK. (2)

That is, the following asymptotic convergence rate holds: f(Kr) − fmin,K O √ 1r .

This result of [4] holds in fact under more general assumptions, namely when f is Lipschitz continuous and K satisﬁes a technical assumption (Assumption 1 in [4]), which says (roughly) that around any point in K there is a ball whose intersection with K is at least a constant fraction of the unit ball.

As explained in [10] the parameter f(Kr) can be computed using semideﬁnite programming, assuming one knows the moments mα(K) of the Lebesgue measure on K, where

mα(K) :=

xαdx for α ∈ Nn.

K

Indeed suppose f(x) = β∈N(n,d) fβxβ has degree d. Writing h ∈ Σ[x]r as h(x) = α∈N(n,2r) hαxα, the parameter f(Kr) from (1) can be reformulated as follows:

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

Since the sum-of-squares condition on h may be written as a linear matrix inequality, this is a semideﬁnite program. In fact, since it only has one linear equality constraint, it may even be

rewritten as a generalised eigenvalue problem. In particular, f(Kr) is equal to the the smallest generalized eigenvalue of the system:

Ax = λBx (x = 0),

where the symmetric matrices A and B are of order n+r r with rows and columns indexed by N(n,r), and

Aα,β =

fδ

δ∈N(n,d)

For more details, see [10, 4, 3].

xα+β+δdx, Bα,β =

K

xα+βdx α,β ∈ N(n,r). (4)

K

### 3 Bounds from simulated annealing

Given a continuous function f, consider the associated Boltzman distribution over the set K, deﬁned by the density function:

Pf(x) := exp(−f(x))

K exp(−f(x ))dx .

Write X ∼ Pf if the random variable X takes values in K according to the Boltzman distribution.

The idea of simulated annealing is to sample X ∼ Pf/t where t > 0 is a ﬁxed ‘temperature’ parameter, that is subsequently decreased. Clearly, for any t > 0, we have

fmin,K ≤ EX∼P

[f(X)]. (5)

f/t

The point is that, under mild assumptions, these bounds converge to the minimum of f over K (see, e.g., [15]):

EX∼P

lim

[f(X)] = fmin,K.

f/t

t↓0

The key step in the practical utilization of theses bounds is therefore to perform the sampling of X ∼ Pf/t.

Example 3.1. Consider the minimization of the Motzkin polynomial

f(x1,x2) = 64(x41x22 + x21x42) − 48x21x22 + 1

over K = [−1,1]2, where there are four global minimizers at the points ±21,±12 , and fmin,K = 0. Figure 1 shows the corresponding Boltzman density function for t = 12. Note that this density has four modes, roughly positioned at the four global minimizers of f in [−1,1]2. The corresponding upper bound on fmin,K = 0 is EX∼P

[f(X)] ≈ 0.7257 (t = 12). To obtain a better upper bound on fmin,K from the Lasserre hierarchy, one needs to use a degree

f/t

14 s.o.s. polynomial density; in particular, one has f(6)K = 0.8010 (degree 12) and f(7)K = 0.7088 (degree 14). More detailed numerical results are given in Section 5.

When f is linear and K a convex body, Kalai and Vempala [6, Lemma 4.1] show that the rate of convergence of the bounds in (5) is linear in the temperature t.

![image 1](<2017-klerk-comparison-lasserre-measure-based-bounds_images/imageFile1.png>)

![image 2](<2017-klerk-comparison-lasserre-measure-based-bounds_images/imageFile2.png>)

Figure 1: Graph and contours of the Boltzman density with t = 12 for the Motzkin polynomial.

- Theorem 3.2 (Kalai and Vempala [6]). Let f(x) = cTx where c is a unit vector, and let K be a convex body. Then, for any t > 0, we have


E

[f(X)] − min

f(x) ≤ nt.

x∈K

X∼Pf/t

We indicate how to extend the result of Kalai and Vempala in Theorem 3.2 to the case of an arbitrary convex function f. This more general result is hinted at in §6 of [6], where the authors write

“... a statement analogous to [Theorem 2] holds also for general convex functions ...”

but no precise statement is given there. In any event, as we will now show, the more general result may readily be derived from Theorem 3.2 (in fact, from the special case of a linear coordinate function f(x) = xi for some i).

- Corollary 3.3. Let f be a convex function and let K ⊆ Rn be a convex body. Then, for any t > 0, we have


E

[f(X)] − min

f(x) ≤ nt.

x∈K

X∼Pf/t

Proof. Set

f(x)e−f(x)/tdx

[f(X)] = K

EK := E

.

−f(x)

X∼Pf/t

t dx

K e

Then we have

f(x) ≤ EK. Deﬁne the set

fmin,K = min x∈K

K := {(x,xn+1) ∈ Rn+1 : x ∈ K, f(x) ≤ xn+1 ≤ EK}. Then K is a convex body and we have

Accordingly, deﬁne the parameter

min

f(x) = min

xn+1.

x∈K

(x,xn+1)∈ K

xn+1e−x

n+1/tdxn+1dx K e−xn+1/tdxn+1dx

E K := K

.

- Corollary 3.3 will follow if we show that


E K = EK + t. (6) To this end set EK = N

DK and E K = N

D K , where we deﬁne

K

K

NK :=

f(x)e−f(x)/tdx, DK :=

K

e−f(x)/tdx,

K

N K :=

xn+1e−x

n+1/tdxn+1dx, D K :=

K

e−x

n+1/tdxn+1dx.

K

We work out the parameters N K and D K (taking integrations by part):

D K =

K

EK

e−x

n+1/tdxn+1 dx =

f(x)

K

K/t dx = tDK − te−E

te−f(x)/t − te−E

K/tvol(K),

N K =

K

EK

xn+1e−x

n+1/tdxn+1 dx

f(x)

=

K

−tEKe−E

K/t + tf(x)e−f(x)/t + t

= −tEKe−E

K/tvol(K) + tNK + tD K. Then, using the fact that EK = N

DK , we obtain:

K

EK

e−x

n+1/tdxn+1 dx

f(x)

NK − EKe−E

K/tvol(K) DK − e−EK/tvol(K)

N K D K

NK DK

,

= t +

= t +

which proves relation (6).

We can now derive the result of Corollary 3.3. Indeed, using Theorem 2 applied to K and the linear function xn+1, we get

E

[f(X)]−min

f(x) = EK−min x∈K

f(x) = (E K− min

xn+1)+(EK−E K) ≤ t(n+1)−t = tn.

x∈K

X∼Pf/t

(x,xn+1)∈ K

The bound in the corollary is tight asymptotically, as the following example shows.

Example 3.4. Consider the univariate problem minx{x | x ∈ [0,1]}. Thus, in this case, f(x) = x, K = [0,1] and minx∈K f(x) = 0. For given temperature t > 0, we have

1 0 xe−x/tdx

e−1/t 1 − e−1/t ∼ t for small t.

E

− 0 = t −

[f(X)] − min

f(x) =

0 e−x/tdx

x∈K

X∼Pf/t

### 4 Main results

We will prove the following relationship between the sum-of-squares based upper bound (1) of Lasserre and the bound (5) based on simulated annealing.

- Theorem 4.1. Let f be a polynomial of degree d, let K be a compact set and set fmax = maxx∈K |f(x)|. Then we have


fmax 2r

f(Krd) ≤ E

[f(X)] +

X∼Pf/t

e · fmax t

for any integer r ≥

and any t > 0.

For the problem of minimizing a convex polynomial function over a convex body, we obtain the following improved convergence rate for the sum-of-squares based bounds of Lasserre.

- Corollary 4.2. Let f ∈ R[x] be a convex polynomial of degree d and let K be a convex body. Then for any integer r ≥ 1 one has


c r

f(Krd) − min

f(x) ≤

, for some constant c > 0 that does not depend on r. (For instance, c = (ne + 1) fmax.) Proof. Let r ≥ 1 and set t = e· f

x∈K

r . Combining Theorems 3.2 and 4.1, we get

max

f(Krd) − min

f(x) = fK(rd) − E

[f(X)] + E

[f(X)] − fmin,K

x∈K

X∼Pf/t

X∼Pf/t

ne · fmax r ≤

fmax 2r

fmax 2r

(ne + 1) fmax r

≤

+ nt =

+

.

For convex polynomials f, this improves on the known O(1/√r) result from Theorem 2.1. One may in fact use the last corollary to obtain the same rate of convergence in terms of r for all polynomials, without the convexity assumption, as we will now show.

- Corollary 4.3. If f be a polynomial and K a convex body, then there is a c > 0 depending on f and K only, so that


c r

f(2Kr) − min

f(x) ≤

. A suitable value for c is

x∈K

c = (ne + 1) fmin,K + Cf1 · diam(K) + Cf2 · diam(K)2 ,

- where Cf1 = maxx∈K  ∇f(x) 2 and Cf2 = maxx∈K  ∇2f(x) 2. We ﬁrst deﬁne a convex quadratic function q that upper bounds f on K as follows:

q(x) = f(a) + ∇f(a) (x − a) + Cf2 x − a 22,

- where Cf2 = maxx∈K  ∇2f(x) 2, and a is the minimizer of f on K. Note that q(x) ≥ f(x) for all x ∈ K by Taylor’s theorem, and minx∈K q(x) = f(a).


By deﬁnition of the Lasserre hierarchy,

f(2Kr) := inf

h(x)f(x)dx s.t. K h(x)dx = 1 ≤ inf

h∈Σ[x]2r K

h(x)q(x)dx s.t. K h(x)dx = 1 ≡ q(2Kr). Invoking Corollary 4.2 and using that the degree of q is 2, we obtain:

h∈Σ[x]2r K

(ne + 1)ˆqmax r

f(2Kr) ≤ q(2Kr) ≤ f(a) +

,

where qˆmax = maxx∈K q(x) ≤ fmin,K + Cf1 · diam(K) + Cf2 · diam(K)2. The last result improves on the known O √ 1r rate in Theorem 2.1.

| |
|---|


#### Proof of Theorem 4.1

The key idea in the proof of Theorem 4.1 is to replace the Boltzman density function by a polynomial approximation.

To this end, we ﬁrst recall a basic result on approximating the exponential function by its truncated Taylor series.

- Lemma 4.4 (De Klerk, Laurent and Sun [4]). Let φ2r(λ) denote the (univariate) polynomial of degree 2r obtained by truncating the Taylor series expansion of e−λ at the order 2r. That is,


2r

(−t)k k!

φ2r(λ) :=

.

k=0

Then φ2r is a sum of squares of polynomials. Moreover, we have

λ2r+1 (2r + 1)!

0 ≤ φ2r(λ) − e−λ ≤

for all λ ≥ 0. (7)

We now deﬁne the following approximation of the Boltzman density Pf/t:

φ2r(f(x)/t)

ϕ2r,t(x) :=

. (8)

K φ2r(f(x)/t)dx

By construction, ϕ2r,t is a sum-of-squares polynomial probability density function on K, with degree 2rd if f is a polynomial of degree d. Moreover, by relation (7) in Lemma 4.4, we obtain

φ2r(f(x)/t)

ϕ2r,t(x) ≤

(9)

K exp(−f(x)/t)dx

(f(x)/t)2r+1 (2r + 1)! K exp(−f(x)/t)dx

≤ Pf/t(x) +

. (10)

From this we can derive the following result.

- Lemma 4.5. For any continuous f and scalar t > 0 one has


f(Krd) ≤

f(x)ϕ2r,t(x)dx ≤ E

X∼Pf/t

K

(f(x) − fmin,K)(f(x))2r+1dx t2r+1(2r + 1)! K exp(−f(x)/t)dx

[f(X)] + K

. (11)

Proof. As ϕ2r,t(x) is a polynomial of degree 2rd and a probability density function on K (by (8)), we have:

f(Krd) ≤

(f(x) − fmin,K)ϕ2r,t(x)dx + fmin,K. (12) Using the above inequality (10) for ϕ2r,t(x) we can upper bound the integral on the right hand side:

f(x)ϕ2r,t(x)dx =

K

K

(f(x) − fmin,K)ϕ2r,t(x)dx ≤

K

= E

(f(x) − fmin,K)(f(x)/t)2r+1 (2r + 1)! K exp(−f(x)/t)dx

(f(x) − fmin,K)Pf/t(x)dx +

dx

K

K

(f(x) − fmin)(f(x)/t)2r+1 (2r + 1)! K exp(−f(x)/t)dx

[f(X)] − fmin,K +

dx.

X∼Pf/t

K

Combining with the inequality (12) gives the desired result.

We now proceed to the proof of Theorem 4.1. In view of Lemma 4.5, we only need to bound the last right-hand-side term in (11):

(f(x) − fmin)(f(x))2r+1dx

T := K

t2r+1(2r + 1)! K exp(−f(x)/t)dx and to show that T ≤ f

2r . By the deﬁninition of fmax we have

max

(f(x) − fmin)(f(x))2r+1 ≤ 2 fmax2(r+1) and exp(−f(x)/t) ≥ exp( fmax/t) on K, which implies

2 fmax2(r+1) exp( fmax/t) t2r+1(2r + 1)!

T ≤

. Combining with the Stirling approximation inequality,

√

r! ≥

2πr

r e

r

(r ∈ N),

applied to (2r + 1)!, we obtain:

2 fmax 2π(2r + 1)

T ≤

fmaxe t(2r + 1)

2r+1

##### exp( fmax/t).

Consider r ≥ e· f

t , so that fmax/t ≤ r/e. Then, using the fact that r/(2r + 1) ≤ 1/2, we obtain

max

2r+1

2 fmax √2π

exp(r/e) √2r + 1

r 2r + 1

T ≤

r

exp(1/e)r √2r + 1

1 4

fmax √2π

≤

r

fmax √2π√2r + 1

exp(1/e) 4

=

<

fmax 2r

.

This concludes the proof of Theorem 4.1.

### 5 Concluding remarks

We conclude with a numerical comparison of the two hierarchies of bounds. By Theorem 4.1, it is reasonable to compare the bounds f(Kr) and EX∼Pf/t[f(X)], with t = e·d· f

r and d the degree of f. Thus we deﬁne, for the purpose of comparison:

max

[f(X)], with t = e·d· f

SA(r) = E

r .

max

X∼Pf/t

We calculated the bounds for the polynomial test functions listed in Table 1.

Table 1: Test functions, all with n = 2, domain K = [−1,1]2, and minimum fmin,K = 0.

|Name|f(x)<br><br>|fmax|d|Convex?|
|---|---|---|---|---|
|Booth function|(10x1 + 20x2 − 7)2 + (20x1 + 10x2 − 5)2<br><br>|2594|2|yes|
|Matyas function|26(x21 + x22) − 48x1x2<br><br>|100|2|yes|
|Motzkin polynomial|64(x41x22 + x21x42) − 48x21x22 + 1<br><br>|81<br><br>|6<br><br>|no|
|Three-Hump Camel function<br><br>|56 6 x61 − 54 · 1.05x41 + 50x21 + 25x1x2 + 25x22<br><br>|2048|6<br><br>|no|


The bounds are shown in Table 2. The bounds f(Kr) were taken from [2], while the bounds SA(r) were computed via numerical integration, in particular using the Matlab routine sum2 of the package Chebfun [5].

The results in the table show that the bound in Theorem 4.1 is far from tight for these examples.

In fact, it may well be that the convergence rates of f(Kr) and SA(r) are diﬀerent for convex f. We know that SA(r) − fmin,K = Θ(1/r) is the exact convergence rate for the simulated annealing bounds for convex f (cf. Example 3.4), but it was speculated in [2] that one may in fact have

f(Kr) − fmin,K = O(1/r2), even for non-convex f. Determining the exact convergence rate f(Kr) remains an open problem.

Table 2: Comparison of the upper bounds SA(r) and f(Kr) for the test functions.

|r<br><br>|Booth Function| |Matyas Function| |Three–Hump Camel Function<br><br>| |Motzkin Polynomial| |
|---|---|---|---|---|---|---|---|---|
| |f(Kr)<br><br>|SA(r)<br><br>|fK(r)<br><br>|SA(r)|f(Kr)<br><br>|SA(r)|f(Kr)<br><br>|SA(r)|
|3<br><br>|118.383|367.834<br><br>|4.2817|15.4212<br><br>|29.0005|247.462|1.0614<br><br>|4.0250|
|4|97.6473|356.113<br><br>|3.8942<br><br>|14.8521|9.5806<br><br>|241.700<br><br>|0.8294<br><br>|3.9697|
|5<br><br>|69.8174|345.043<br><br>|3.6894<br><br>|14.3143|9.5806<br><br>|236.102|0.8010|3.9157|
|6|63.5454<br><br>|334.585|2.9956<br><br>|13.8062|4.4398<br><br>|230.663<br><br>|0.8010|3.8631|
|7|47.0467<br><br>|324.701|2.5469<br><br>|13.3262|4.4398<br><br>|225.381<br><br>|0.7088|3.8118|
|8<br><br>|41.6727<br><br>|315.354|2.0430|12.8726|2.5503|220.251<br><br>|0.5655<br><br>|3.7618|
|9<br><br>|34.2140|306.510|1.8335<br><br>|12.4441<br><br>|2.5503|215.269<br><br>|0.5655|3.7130|
|10<br><br>|28.7248|298.138<br><br>|1.4784<br><br>|12.0390|1.7127|210.431|0.5078<br><br>|3.6654|
|11<br><br>|25.6050|290.206<br><br>|1.3764<br><br>|11.6560|1.7127<br><br>|205.734|0.4060|3.6190|
|12|21.1869<br><br>|282.687|1.1178|11.2938<br><br>|1.2775<br><br>|201.173<br><br>|0.4060<br><br>|3.5737|
|13|19.5588<br><br>|275.554<br><br>|1.0686|10.9511|1.2775<br><br>|196.745<br><br>|0.3759<br><br>|3.5296|
|14<br><br>|16.5854|268.782|0.8742<br><br>|10.6267<br><br>|1.0185|192.446<br><br>|0.3004<br><br>|3.4865|
|15<br><br>|15.2815|262.348<br><br>|0.8524|10.3195<br><br>|1.0185|188.272|0.3004<br><br>|3.4444|
|16|13.4626<br><br>|256.230|0.7020|10.0284<br><br>|0.8434<br><br>|184.220<br><br>|0.2819<br><br>|3.4034|
|17<br><br>|12.2075|250.408<br><br>|0.6952<br><br>|9.75250|0.8434|180.287|0.2300<br><br>|3.3633|
|18<br><br>|11.0959|244.863<br><br>|0.5760<br><br>|9.49071|0.7113<br><br>|176.469<br><br>|0.2300|3.3242|
|19|9.9938<br><br>|239.577|0.5760<br><br>|9.24220|0.7113<br><br>|172.762<br><br>|0.2185|3.2860|
|20|9.2373<br><br>|234.534|0.4815<br><br>|9.00615|0.6064<br><br>|169.164<br><br>|0.1817|3.2487|


Finally, one should point out that it is not really meaningful to compare the computational complexities of computing the two bounds f(Kr) and SA(r), as explained below.

For any polynomial f and convex body K, f(Kr) may be computed by solving a generalised eigenvalue problem with matrices of order n+r r , as long as the moments of the Lebesgue measure on K are known. The generalised eigenvalue computation may be done in O n+r r 3 operations; see [3] for details. Thus this is a polynomial-time procedure for ﬁxed values of r.

For non-convex f, the complexity of computing EX∼Pf/t[f(X)] is not known. When f is linear,

it is shown in [1] that EX∼Prf[f(X)] with t = O(1/r) may be obtained in O∗ n4.5 log(r) oracle membership calls for K, where the O∗(·) notation suppresses logarithmic factors.

Since the assumptions on the available information is diﬀerent for the two types of bounds, there is no simple way to compare these respective complexities.

### References

- [1] J. Abernethy and E. Hazan. Faster Convex Optimization: Simulated Annealing with an Eﬃcient Universal Barrier. arXiv 1507.02528, July 2015.
- [2] E. de Klerk, R. Hess and M. Laurent. Improved convergence rates for Lasserre-type hierarchies of upper bounds for box-constrained polynomial optimization. SIAM J. Optim. (to appear),


- arXiv:1603.03329v1 (2016)
- [3] E. de Klerk, J.-B. Lasserre, M. Laurent, and Z. Sun. Bound-constrained polynomial optimization using only elementary calculations. Mathematics of Operations Research (to appear), arXiv:1507.04404v2 (2016)
- [4] E. de Klerk, M. Laurent, Z. Sun. Convergence analysis for Lasserre’s measure-based hierarchy of upper bounds for polynomial optimization, Math. Program. Ser. A, (2016). doi:10.1007/s10107016-1043-1.
- [5] T. A. Driscoll, N. Hale, and L. N. Trefethen, editors, Chebfun Guide, Pafnuty Publications, Oxford, 2014.
- [6] A. T. Kalai and S. Vempala. Simulated annealing for convex optimization. Mathematics of Operations Research, 31(2), 253–266 (2006)
- [7] S. Kirkpatrick, C.D. Gelatt, Jr., M.P. Vecchi. Optimization by simulated annealing. Science 220, 671-680, 1983.
- [8] Lasserre, J.B.: Global optimization with polynomials and the problem of moments. SIAM J. Optim. 11, 796–817 (2001)
- [9] Lasserre, J.B.: Moments, Positive Polynomials and Their Applications. Imperial College Press

(2009)

- [10] Lasserre, J.B.: A new look at nonnegativity on closed sets and polynomial optimization. SIAM J. Optim. 21(3), 864–885 (2011)
- [11] Laurent, M.: Sums of squares, moment matrices and optimization over polynomials. In Emerging Applications of Algebraic Geometry, Vol. 149 of IMA Volumes in Mathematics and its Applications, M. Putinar and S. Sullivant (eds.), Springer, pages 157–270 (2009)
- [12] L. Lov´sz. Hit-and-run mixes fast, Mathematical Programming, 86(3), 443–461, 1999.
- [13] P. Parrilo. Structured Semideﬁnite Programs and Semialgebraic Geometry Methods in Robustness and Optimization, PhD thesis, California Institute of Technology (2000)
- [14] R. Smith. Eﬃcient Monte Carlo procedures for generating points uniformly distributed over bounded regions, Operations Research 32(6), 1296-1308, 1984.
- [15] J. Spall. Introduction to Stochastic Search and Optimization. Wiley, New York, 2003.


