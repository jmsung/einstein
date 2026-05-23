arXiv:1804.05524v1[math.OC]16Apr2018

Worst-case examples for Lasserre’s measure–based hierarchy for polynomial optimization on the hypercube

Etienne de Klerk ∗ Monique Laurent † November 5, 2018

Abstract

We study the convergence rate of a hierarchy of upper bounds for polynomial optimization problems, proposed by Lasserre [SIAM J. Optim. 21(3) (2011), pp. 864 − 885], and a related hierarchy by De Klerk, Hess and Laurent [SIAM J. Optim. 27(1), (2017) pp. 347 − 367]. For polynomial optimization over the hypercube we show a reﬁned convergence analysis for the ﬁrst hierarchy. We also show lower bounds on the convergence rate for both hierarchies on a class of examples. These lower bounds match the upper bounds and thus establish the true rate of convergence on these examples. Interestingly, these convergence rates are determined by the distribution of extremal zeroes of certain families of orthogonal polynomials.

Keywords: Polynomial optimization; Semideﬁnite optimization; Lasserre hierarchy; extremal roots of orthogonal polynomials; Jacobi polynomials AMS classiﬁcation: 90C22; 90C26; 90C30

# 1 Introduction

We consider the problem of minimizing a polynomial f : Rn → R over a compact set K ⊆ Rn. That is, we consider the problem of computing the parameter:

f(x). We recall the following reformulation for fmin,K, established by Lasserre [12]: fmin,K = inf

fmin,K := min x∈K

σ(x)f(x)dµ(x) s.t. K σ(x)dµ(x) = 1,

σ∈Σ[x] K

where Σ[x] denotes the set of sums of squares of polynomials, and µ is a signed Borel measure supported on K. Given an integer d ∈ N, by bounding the degree of the polynomial σ ∈ Σ[x] by 2d, Lasserre [12] deﬁned the parameter:

![image 1](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile1.png>)

∗Tilburg University and Delft University of Technology, E.deKlerk@uvt.nl †Centrum Wiskunde & Informatica (CWI), Amsterdam and Tilburg University, monique@cwi.nl

f(Kd) := inf

σ(x)f(x)dµ(x) s.t. K σ(x)dµ(x) = 1, (1)

σ∈Σ[x]d K

![image 2](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile2.png>)

where Σ[x]d consists of the polynomials in Σ[x] with degree at most 2d.

The inequality fmin,K ≤ f(Kd) holds for all d ∈ N and, in view of the identity (1), it follows that the sequence f(Kd) converges to fmin,K as d → ∞. De Klerk and Laurent [2] established the following rate of convergence for the sequence fK(d), when µ is the Lebesgue measure and K is a convex body. Theorem 1.1. [2] Let f ∈ R[x], K a convex body, and µ the Lebesgue measure on K. There exist constants Cf,K (depending only on f and K) and dK ∈ N (depending only on K) such that

![image 3](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile3.png>)

![image 4](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile4.png>)

![image 5](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile5.png>)

Cf,K d

f(Kd) − fmin,K ≤

for all d ≥ dK. (2)

![image 6](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile6.png>)

![image 7](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile7.png>)

That is, the following asymptotic convergence rate holds: fK(d) − fmin,K = O 1d .

![image 8](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile8.png>)

![image 9](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile9.png>)

This result was an improvement on an earlier result by De Klerk, Laurent and Sun [5, Theorem 3], who showed a convergence rate in O(1/

√

![image 10](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile10.png>)

d) (for K convex body or, more generallly, compact under a mild assumption).

As explained in [12] the parameter fK(d) can be computed using semideﬁnite programming, assuming one knows the (generalised) moments of the measure µ on K with respect to some polynomial basis. Set

![image 11](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile11.png>)

mα(K) :=

bα(x)dµ(x), mα,β(K) :=

K

bα(x)bβ(x)dµ(x) for α,β ∈ Nn,

K

where the polynomials {bα} form a basis for the space R[x1,...,xn]2d of polynomials of degree at most 2d, indexed by N(n,2d) = {α ∈ Nn : ni=1 αi ≤ 2d}. For example, the standard monomial basis in R[x1,...,xn]2d is bα(x) = xα := ni=1 xα

i for α ∈ N(n,2d), and then mα,β(K) = mα+β(K). If f(x) = β∈N(n,d

i

0) fβbβ(x) has degree d0, and writing σ ∈ Σ[x]d as σ(x) = α∈N(n,2d) σαbα(x), then the parameter f(Kd) in (1) can be computed as follows:

![image 12](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile12.png>)

f(Kd) = min

σαmα,β(K) (3)

fβ

![image 13](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile13.png>)

α∈N(n,2d)

β∈N(n,d0)

σαmα(K) = 1,

s.t.

α∈N(n,2d)

σαbα(x) ∈ Σ[x]d.

α∈N(n,2d)

Since the sum-of-squares condition on σ may be written as a linear matrix inequality, this is a semideﬁnite program. In fact, since the program (3) has only one linear equality constraint, using semideﬁnite programming duality it can be rewritten as a generalised eigenvalue problem. In

particular, f(Kd) is equal to the the smallest generalised eigenvalue of the system: Ax = λBx (x = 0),

![image 14](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile14.png>)

where the symmetric matrices A and B are of order n+dd with rows and columns indexed by

- N(n,d), and


bα(x)bβ(x)dµ(x) for α,β ∈ N(n,d).

fδ

bα(x)bβ(x)bδ(x)dµ(x), Bα,β =

Aα,β =

K

K

δ∈N(n,d0)

(4) For more details, see [12, 5]. In particular, if the basis {bα} is orthonormal with respect to the measure µ, then B is the identity matrix, and fK(d) is the smallest eigenvalue of the above matrix A. For further reference we summarize this result, which will play a central role in our approach.

![image 15](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile15.png>)

- Lemma 1.2. Assume {bα : α ∈ N(n,2d)} is a basis of the space R[x1,...,xn]2d, which is or-


thonormal w.r.t. the measure µ on K, i.e., K bα(x)bβ(x)dµ(x) = δα,β. Then the parameter fK(d) is equal to the smallest eigenvalue of the matrix A in (4).

![image 16](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile16.png>)

Under the conditions of the lemma, note in addition that, if the vector u = (uα)α∈N(n,d) is an eigenvector of the matrix A in (4) for its smallest eigenvalue, then the (square) polynomial σ(x) = ( α∈N(n,d) uαxα)2 is an optimal density function for the parameter fK(d). Related hierarchy by De Klerk, Hess and Laurent

![image 17](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile17.png>)

For the hypercube K = [−1,1]n, De Klerk, Hess and Laurent [3] considered a variant on the Lasserre hierarchy (1), where the density function σ is allowed to take the more general form

σI(x)

σ(x) =

I⊆{1,...,n}

(1 − x2i) (5)

i∈I

and the polynomials σI are sum-of-squares polynomials with degree at most 2d − 2|I| (to ensure that the degree of σ is at most 2d), and I = ∅ is included in the summation. Moreover the measure µ is ﬁxed to be

−1

n

![image 18](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile18.png>)

1 − x2i

dx1 ···dxn. (6)

dµ(x) =

i=1

As we will recall below, this measure is associated with the Chebyshev orthogonal polynomials. We let f(d) denote the parameter1 obtained by using in (1) these choices (5) of density functions σ(x) and (6) of measure µ. By construction, we have

fmin,K ≤ f(d) ≤ fK(d). De Klerk, Hess and Laurent [3] proved a stronger convergence rate for the bounds f(d).

![image 19](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile19.png>)

- Theorem 1.3. [3] Let f ∈ R[x] be a polynomial and K = [−1,1]n. We have


1 d2

f(d) − fmin,K = O

.

![image 20](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile20.png>)

![image 21](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile21.png>)

1We drop the dependence on K which is implictly selected to be the box [−1, 1]n.

Contribution of this paper

In this paper we investigate the rate of convergence of the hierarchies fK(d) and f(d) to fmin,K for the case of the box K = [−1,1]n. The above discussion raises naturally the following questions:

![image 22](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile22.png>)

- • Is the sublinear convergence rate f(d)−fmin,K = O d 12 tight, or can this result be improved?

![image 23](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile23.png>)

- • Does this convergence rate extend to the Lasserre bounds, where we restrict to sums-of-squares density functions?


We give a positive answer to both questions. Regarding the ﬁrst question we show that the convergence rate is Ω(1/d2) when f is a linear polynomial, which implies that the convergence analysis in Theorem 1.3 for the bounds f(d) is tight. This relies on the eigenvalue reformulation of the bounds (from Lemma 1.2) and an additional link to the extremal zeros of the associated Chebyshev polynomials. We also show that the same lower bound holds for the convergence rate of the

Lasserre bounds f(Kd) when considering measures on the hypercube corresponding to general Jacobi polynomials.

![image 24](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile24.png>)

Regarding the second question we show that also the Lasserre bounds have a O(1/d2) convergence rate when using the Chebyshev type measure from (6). The starting point is again the reformulation from Lemma 1.2 in terms of eigenvalues, combined with some further analytical arguments.

The paper is organised as follows. In Section 2 we group preliminary results about orthogonal polynomials and their extremal roots. Then, in Section 3.1 we analyse the convergence rate of the Lasserre bounds f(Kd) when f is a linear polynomial and, in Section 3.2, we analyse the bounds f(d). In both cases we show a Ω(1/d2) lower bound. In Section 4 we show a O(1/d2) upper bound for the convergence rate of the Lasserre bounds fK(d), and this analysis is tight in view of the previously shown lower bounds.

![image 25](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile25.png>)

![image 26](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile26.png>)

Notation

We recap here some notation that is used throughout. For an integer d ∈ N, R[x]d denotes the set of n-variate polynomials in the variables x = (x1,...,xn) with degree at most d and Σ[x]d denotes the set of polynomials with degree at most 2d that can be written as a sum of squares of polynomials.

We use the classical Landau notation. For two functions f,g : N → R+, the notation f(n) =

- O(g(n)) (resp., f(n) = Ω(g(n)), f(n) = o(g(n))) means limsupn→∞ f(n)/g(n) < ∞ (resp., liminfn→∞ f(n)/g(n) > ∞, limn→∞ f(n)/g(n) = 0), and f(n) = Θ(g(n)) means f(n) = O(g(n)) and f(n) = Ω(g(n)). We also use this notation when f,g are functions of a continuous variable x and we want to indicate the behavior of f(x) and g(x) in the neighbourhood of a given scalar x0


f(x)/g(x) < ∞, etc.

when x → x0. So, f(x) = O(g(x)) as x → x0 means limsupx→x

0

# 2 Preliminaries on orthogonal polynomials

In what follows we review some known facts on classical orthogonal polynomials that we need for our treatment. Unless we give detailed references, the relevant results may be found in the classical text by Szego¨ [16] (see also [8]).

We consider families of univariate polynomials {pk(x)} (k = 0,1,...,d), that satisfy a three-term recursive relation of the form:

xpk(x) = akpk+1(x) + bkpk(x) + ckpk−1(x) (k = 1,...,d − 1), (7)

where p0 is a constant, p1(x) = (x − b0)p0/a0, and ak, bk and ck are real values that satisfy ak−1ck > 0 for k = 1,...,d − 1. If we set c0 = 0 then relation (7) also holds for k = 0). Deﬁning the k × k tri-diagonal matrix





b0 a0 0 ··· 0 c1 b1 a1 0

...

...

...

0

Ak :=

, (8)

one has the classical relation:

 

. ck−2 bk−2 ak−2 0 0 ··· ck−1 bk−1

 

aj

 

k−1

 pk(x) = det(xIk − Ak)p0 for k = 1,...,d, (9)

j=0

which can be easily veriﬁed using induction on k ≥ 1 and the relation (7) (see, e.g., [11]). Therefore, the roots of the polynomial pk are precisely the eigenvalues of the matrix Ak in (8).

Recall that the polynomials pk (k = 0,1,...,d) are orthogonal with respect to a weight function w : [−1,1] → R, that is continuous and positive on (−1,1), if

1

pi(x)pj(x)w(x)dx = 0 for all i = j.

pi,pj :=

−1

![image 27](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile27.png>)

We denote by pˆk := pk/ pk,pk the corresponding normalized polynomial, so that p ˆk,pˆk = 1.

As is well known, if the polynomials pk are degree k polynomials that are pairwise orthogonal with respect to such a weight function then they satisfy a three-terms recurrence relation of the form (7) (see, e.g., [8, §1.3]). Of course, the corresponding orthonormal polynomials pˆk also satisfy such a three-terms recurrence relation (for diﬀerent scaled parameters ak,bk,ck).

By taking the inner product of both sides in (7) with pk−1 and pk+1 one gets the relations ck pk−1,pk−1 = pk,xpk−1 and ak pk+1,pk+1 = pk+1,xpk , which imply ck pk−1,pk−1 = ak−1 pk,pk and thus ak−1ck > 0. Moreover, when considering the recurrence relations associated with the orthonormal polynomials pˆk, we have ak−1 = ck for any k ≥ 1, i.e., the matrix Ak in (8) is symmetric. We will use later the following fact.

- Lemma 2.1. Let {pˆk} be orthonormal polynomials for the measure dµ(x) = w(x)dx on [−1,1], where w(x) is continuous and positive on (−1,1), and assume they satisfy the three-terms recurrence relation (7). Then, the matrix


xpˆi,pˆj =

1

xpˆi(x)ˆpj(x)w(x)dx

−1

k−1

i,j=0

(10)

is equal to the matrix Ak in (8). In particular, its smallest eigenvalue is the smallest root of the polynomial pk.

Proof. Using the recurrence relation (7) we obtain xpˆi,pˆj = aipˆi+1 + bipˆi + cipˆi−1,pˆj

 

ai if j = i + 1 bi if j = i ci if j = i − 1 0 otherwise.

=



Hence the matrix in (10) is equal to Ak and the last claim follows from (9).

![image 28](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile28.png>)

![image 29](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile29.png>)

![image 30](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile30.png>)

![image 31](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile31.png>)

It is also known that the roots of pk are all real, simple and lie in (−1,1), and that they interlace the roots of pk+1 (see, e.g., [8, §1.2]). In what follows we will use the smallest (and largest) roots to give closed-form expressions for the bounds fK(d) and f(d) in some examples.

![image 32](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile32.png>)

We now recall several classical univariate orthogonal polynomials on the interval [−1,1] and some information on their smallest roots.

Chebyshev polynomials

We will use the univariate Chebyshev polynomials (of the ﬁrst kind), deﬁned by:

Tk(x) = cos(k arccos(x)), for x ∈ [−1,1], k = 0,1,.... (11) They satisfy the following three-terms recurrence relationships:

T0(x) = 1, T1(x) = x, Tk+1(x) = 2xTk(x) − Tk−1(x) for k ≥ 1. (12)

The Chebyshev polynomials are orthogonal with respect to the weight function w(x) = √1−1 x

and the roots of Tk are given by

![image 33](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile33.png>)

![image 34](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile34.png>)

2

cos

2i − 1 2k

π for i = 1,...,k. (13)

![image 35](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile35.png>)

Jacobi polynomials

The Jacobi polynomials, denoted by {Pkα,β} (k = 0,1,...), are orthogonal with respect to the weight function

wα,β(x) := (1 − x)α(1 + x)β, x ∈ (−1,1) (14) where α > −1 and β > −1 are given parameters. The normalized Jacobi polynomials are denoted by Pˆkα,β, so that − 11(Pˆkα,β(x))2wα,β(x)dx = 1.

Thus the Chebyshev polynomials may be seen as the special case corresponding to α = β = −12. Likewise, the Legendre polynomials are the orthogonal polynomials w.r.t. the constant weight

![image 36](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile36.png>)

function (w(x) = 1), so they correspond to the special case α = β = 0.

There is no closed-form expression for the roots of Jacobi polynomials in general. But some bounds are known for the smallest root of Pkα,β, denoted by ξkα,β, that we recall in the next theorem.

- Theorem 2.2. The smallest root, denoted ξkα,β, of the Jacobi polynomial Pkα,β satisﬁes the following inequalities:


- (i) ([7]) ξkα,β ≤ −1 + 2(k−1)(k+α2(+ββ+1)(+2)+(β+3)β+3)(α+β+2).

![image 37](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile37.png>)

- (ii) ([6]) ξkα,β ≥ F−4(k−1)


√

![image 38](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile38.png>)

∆

E , where F = (β − α)((α + β + 6)k + 2(α + β)) , E = (2k + α + β)(k(2k + α + β) + 2(α + β + 2)) ∆ = k2(k + α + β + 1)2 + (α + 1)(β + 1)(k2 + (α + β + 4)k + 2(α + β)).

![image 39](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile39.png>)

The smallest roots ξkα,β of the Jacobi polynomials Pkα,β converge to −1 as k → ∞. Using the above bounds we see that the rate of convergence is O(1/k2).

- Corollary 2.3. The smallest roots of the Jacobi polynomials Pkα,β satisfy


ξkα,β = −1 + Θ

1 k2

![image 40](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile40.png>)

as k → ∞.

Proof. The upper bound in Theorem 2.2(i) gives directly ξkα,β = −1 + O k 12 . We now use the lower bound in Theorem 2.2(ii) to show ξkα,β = −1 +Ω k 12 . For this we give asymptotic estimates for the quantities E,F,∆. First, using the expansion √1 + x = 1 + x2 − x

![image 41](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile41.png>)

![image 42](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile42.png>)

2

8 + o(x2) as x → 0 we obtain

![image 43](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile43.png>)

![image 44](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile44.png>)

![image 45](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile45.png>)

√

α + β + 1 k

1 k2

(α + 1)(β + 1) 2k2

![image 46](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile46.png>)

∆ = k2 1 +

+

+ o

.

![image 47](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile47.png>)

![image 48](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile48.png>)

![image 49](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile49.png>)

Second, using the expansion 1+1x = 1 − x + x2 + o(x2) as x → 0 we obtain

![image 50](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile50.png>)

1 4k3

1 E

=

![image 51](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile51.png>)

![image 52](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile52.png>)

α + β k −

4(α + β + 2) k2

1 −

+ o

![image 53](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile53.png>)

![image 54](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile54.png>)

1 k2

![image 55](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile55.png>)

.

Combining these two relations gives

4(k−1)√∆

![image 56](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile56.png>)

E = 1 − k1 1 + α+kβ+1 + (α+1)(2k2β+1) + o k 12 1 − α+kβ − 4(α+kβ2+2) + o k 12

![image 57](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile57.png>)

![image 58](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile58.png>)

![image 59](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile59.png>)

![image 60](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile60.png>)

![image 61](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile61.png>)

![image 62](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile62.png>)

![image 63](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile63.png>)

![image 64](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile64.png>)

= 1 + 2Ck2 + o k 12 , where we set C = (α + 1)(β + 1) − 8(α + β + 2) − 2(α + β)(α + β + 1) − 2. Finally, using

![image 65](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile65.png>)

![image 66](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile66.png>)

(β − α)(β + α + 6) 4k2

1 k2

F E

,

+ o

=

![image 67](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile67.png>)

![image 68](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile68.png>)

![image 69](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile69.png>)

we obtain

F − 4(k − 1)√∆ E

![image 70](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile70.png>)

1 k2

= −1 +

![image 71](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile71.png>)

![image 72](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile72.png>)

(β − α)(β + α + 6) 4 −

C 2

![image 73](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile73.png>)

![image 74](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile74.png>)

+ o

1 k2

![image 75](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile75.png>)

,

where the coeﬃcient of 1/k2 can be veriﬁed to be strictly positive, which thus implies the estimate ξkα,β = −1 + Ω(1/k2).

![image 76](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile76.png>)

![image 77](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile77.png>)

![image 78](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile78.png>)

![image 79](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile79.png>)

It is also known that Pkα,β(x) = (−1)kPkβ,α(−x). Therefore the largest root of Pkα,β(x) is equal to −ξkβ,α = 1 − Θ(1/k2).

# 3 Tight lower bounds for a class of examples

In this section we consider the following simple examples

min

n

cixi : x ∈ [−1,1]n , (15)

i=1

asking to minimize the linear polynomial f(x) = ni=1 cixi over the box K = [−1,1]n. Here ci ∈ R are given scalars for i ∈ [n]. Hence, fmin,K = − ni=1 |ci|. For these examples we can obtain explicit closed-form expressions for the Lasserre bounds fK(d) when using product measures with weight functions wα,β on [−1,1], and also for the strengthened bounds f(d) considered by De Klerk, Hess and Laurent, which use product measures with weight functions w−1/2,−1/2. These closed-form expressions are in terms of extremal roots of Jacobi polynomials.

![image 80](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile80.png>)

- 3.1 Tight lower bound for the Lasserre hierarchy


Here we consider the bounds f(Kd) for the example (15), when the measure µ on K = [−1,1]n is a product of univariate measures given by weight functions.

![image 81](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile81.png>)

First we consider the univariate case n = 1. When the measure µ on K = [−1,1] is given by a

continuous positive weight function w on (−1,1), one can obtain a closed form expression for f(Kd) in terms of the smallest root of the corresponding orthogonal polynomials.

![image 82](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile82.png>)

Theorem 3.1. Consider the measure dµ(x) = w(x)dx on K = [−1,1], where w is a positive, continuous weight function on (−1,1), and let pk be univariate degree k polynomials that are orthogonal with respect to this measure. For the univariate polynomial f(x) = x (resp., f(x) = −x), the parameter f(Kd) is equal to the smallest root (resp., the opposite of the largest root) of the polynomial pd+1.

![image 83](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile83.png>)

![image 84](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile84.png>)

Proof. Let pˆ0,...,pˆd+1 denote the corresponding orthonormal polynomials, with pˆi = pi/ pi,pi . Consider ﬁrst f(x) = x. Using Lemma 1.2, we see that fK(d) is equal to the smallest eigenvalue of the matrix A in (10) (for k = d + 1), which coincides with the matrix Ad+1 in (8), so that its smallest eigenvalue is equal to the smallest root of pd+1. Assume now f(x) = −x. Then f(Kd) is equal to λmin(−A) = −λmax(A), which in turn is equal to the opposite of the largest root of pd+1.

![image 85](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile85.png>)

![image 86](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile86.png>)

![image 87](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile87.png>)

![image 88](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile88.png>)

![image 89](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile89.png>)

![image 90](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile90.png>)

Recall that ξdα,β+1 denotes the smallest root of the Jacobi polynomial Pdα,β+1 and that the largest root of Pdα,β+1 is equal to −ξdβ,α+1.

- Corollary 3.2. Consider the measure dµ(x) = wα,β(x)dx on K = [−1,1] with the weight function wα,β(x) = (1 − x)α(1 + x)β and α,β > −1. For the univariate polynomial f(x) = x (resp., f(x) = −x), the parameter f(Kd) is equal to ξdα,β+1 (resp., to ξdβ,α+1) and thus we have


![image 91](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile91.png>)

fK(d) − fmin,K = Θ(1/d2). In particular, f(Kd) = − cos 2d π+2 when α = β = −1/2.

![image 92](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile92.png>)

![image 93](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile93.png>)

![image 94](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile94.png>)

Proof. This follows directly using Theorem 3.1, Corollary 2.3, the fact that the largest root of Pdα,β+1 is equal to −ξdβ,α+1, and the closed form expression (13) for the roots of the Chebyshev polynomials of the ﬁrst kind.

![image 95](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile95.png>)

![image 96](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile96.png>)

![image 97](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile97.png>)

![image 98](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile98.png>)

We now use the above result to show fK(d) − fmin,K = Ω(1/d2) for the example (15) in the multivariate case n ≥ 2. Corollary 3.3. Consider the measure dµ(x) = ni=1 wα

![image 99](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile99.png>)

i,βi(xi)dxi on the hypercube K = [−1,1]n, with the weight functions wα

(1 + xi)β

i,βi(xi) = (1 − xi)α

and αi,βi > −1 for i ∈ [n]. For the polynomial f(x) = nl=1 clxl, we have

i

i

clξα

l,βl

|cl|ξβ

l,αl d+1 ,

f(Kd) ≥

d+1 +

![image 100](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile100.png>)

l:cl>0

l:cl<0

and thus f(Kd) − fmin,K = Ω(1/d2). Proof. Assume f(Kd) = K( nl=1 clxl)σ(x)dµ(x), where σ ∈ R[x1,...,xn]2d is a sum of squares of polynomials and K σ(x)dµ(x) = 1. For each l ∈ [n] consider the univariate polynomial

![image 101](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile101.png>)

![image 102](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile102.png>)

i,βi(xi)dxi,

wα

σ(x1,...,xn)

σl(xl) :=

[−1,1]n−1

i∈[n]\{l}

where we integrate over all variables xi with i ∈ [n]\{l}. Then we have − 11 σl(xl)wα

l,βl(xl)dxl = 1. Moreover, σl has degree at most 2d and, as it is a univariate polynomial which is nonnegative on R, it is a sum of squares of polynomials. Hence, using Corollary 3.2, we can conclude that

1

l,βl(xl)dxl ≥ ξα

l,βl d+1 ,

xlσl(xl)wα

−1

Combining with the deﬁnition of f(Kd) we obtain

![image 103](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile103.png>)

1

l,βl(xl)dxl ≥ ξβ

l,αl d+1 .

(−xl)σl(xl)wα

−1

n

f(Kd) =

cl

![image 104](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile104.png>)

l=1

1

l,βl(xl)dxl ≥

xlσl(xl)wα

−1

l:cl>0

clξα

l,βl

|cl|ξβ

l,αl d+1

d+1 +

l:cl<0

and thus f(Kd) − fmin,K ≥ l:cl>0 cl(ξα

l,βl

l<0 |cl|(ξβ

l,αl

d+1 + 1) = Ω(1/d2).

d+1 + 1) + l:c

![image 105](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile105.png>)

![image 106](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile106.png>)

![image 107](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile107.png>)

![image 108](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile108.png>)

![image 109](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile109.png>)

- 3.2 Tight lower bound for the De Klerk, Hess and Laurent hierarchy In this section we consider the hierarchy of bounds f(d) studied by De Klerk, Hess and Laurent [3],


which are potentially stronger than the bounds fK(d) since they involve the wider class of density functions in (5). Their convergence rate is known to be O(1/d2) ([3], recall Theorem 1.3).

![image 110](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile110.png>)

For the example (15) we can also give an explicit expression for the bounds f(d) and we will show that their convergence rate to fmin,K is also in the order Ω(1/d2), which shows that the analysis in [3] is tight.

We ﬁrst treat the univariate case, in order to introduce the main ideas, and then we extend to the multivariate case.

- Theorem 3.4. For the univariate polynomial f(x) = ±x, we have f(d) = min{ξd−+11/2,−1/2,ξd1/2,1/2},


the smallest value among the smallest roots of the Jacobi polynomials Pd−+11/2,−1/2 and Pd1/2,1/2. In particular, we have f(d) − fmin,K = Θ(1/d2).

Proof. Consider ﬁrst f(x) = x. We ﬁrst recall how to compute f(d) as an eigenvalue problem. By deﬁnition, it is the minimum value of − 11 x(σ0(x) + σ1(x)(1 − x2))w−1/2,−1/2(x)dx, where σ0 ∈ Σ[x]2d, σ1 ∈ Σ[x]2d−2 and − 11(σ0(x) + σ1(x)(1 − x2))w−1/2,−1/2(x)dx = 1. We express the polynomial σ0 in the normalized Jacobi (Chebychev) basis {Pˆk−1/2,−1/2} as

d

Mij(0)Pˆi−1/2,−1/2Pˆj−1/2,−1/2

σ0 =

i,j=0

- for some matrix M(0) of order d+1, constrained to be positive semideﬁnite. Based on the observation that (1 − x2)w−1/2,−1/2(x) = w1/2,1/2(x), we express the polynomial σ1 in the normalized Jacobi basis {Pˆk1/2,1/2} as

σ1 =

d−1

i,j=0

Mij(1)Pˆi1/2,1/2Pˆj1/2,1/2

- for some matrix M(1) of order d, also constrained to be positive semideﬁnite. Then, we obtain f(d) = min{ A−d 1/2,−1/2,M(0) + A1d/−21,1/2,M(1) : Tr(M(0)) + Tr(M(1)) = 1, M(0) 0,M(1) 0}, where A1d/2,1/2 and A−d−1/12,−1/2 are instances of (10) deﬁned as follows:


d

1

Aα,βd :=

xPˆhα,β(x)Pˆkα,β(x)wα,β(x)dx

−1

h,k=0

for any α,β > −1 and d ∈ N. Since strong duality holds we obtain f(d) = max{t : A−d 1/2,−1/2 − tI 0, A1d/−21,1/2 − tI 0} = min{λmin(A−d 1/2,−1/2),λmin(A1d/−21,1/2)}.

By Lemma 2.1, we have λmin(A−d 1/2,−1/2) = ξd−+11/2,−1/2 and λmin(A1d/−21,1/2) = ξd1/2,1/2 and thus f(d) = min{ξd−+11/2,−1/2,ξd1/2,1/2}. The same result holds when f(x) = −x. Finally, by Corollary 2.3, these two smallest roots are both equal to −1 + Θ(1/d2), which concludes the proof.

![image 111](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile111.png>)

![image 112](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile112.png>)

![image 113](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile113.png>)

![image 114](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile114.png>)

We now extend this result to the multivariate case of example (15):

- Corollary 3.5. For the linear polynomial f(x) = nl=1 clxl, we have


f(d) ≥

n

|cl| min{ξd−+11/2,−1/2,ξd1/2,1/2}

l=1

and thus f(d) − fmin,K = Ω(1/d2).

Proof. The proof is analogous to that of Corollary 3.3, with some more technical details. Assume f(d) = K( nl=1 xl)σ(x)dµ(x), where σ(x) = I⊆[n] σI(x) i∈I(1 − x2i), σI(x) is a sum of squares of degree at most 2d − 2|I| and K σ(x)dµ(x) = 1.

Fix l ∈ [n]. Then we can write σ(x) =

(1 − x2i ).

(1 − x2i ) + (1 − x2l )

σI(x)

σI(x)

i∈I

i∈I\{l}

I⊆[n]:l∈I

I⊆[n]\{l}

Next, deﬁne the univariate polynomials in the variable xl:

- σl,0(xl) := I⊆[n]\{l} [−1,1]n−1

σI(x)

i∈I

(1 − x2i)

i∈[n]\{l}

w−1/2,−1/2(xi)dxi,

- σl,1(xl) := I⊆[n]:l∈I [−1,1]n−1


σI(x)

(1 − x2i )

w−1/2,−1/2(xi)dxi,

i∈[n]\{l}

i∈I\{l}

σl(xl) :=

σ(x)

[−1,1]n−1

By construction, we have

w−1/2,−1/2(xi)dxi = σl,0(xl) + (1 − x2l )σl,1(xl).

i∈[n]\{l}

1

1

xlσ(x)dµ(x) =

xlσl(xl)w−1/2,−1/2(xl)dxl,

σl(xl)w−1/2,−1/2(xl)dxl =

σ(x)dµ(x) = 1.

−1

−1

K

K

Moreover, the polynomial σl,0 is a sum of squares (since it is univariate and nonnegative on R) and its degree is at most 2d, and the polynomial σl,1 is a sum of squares of degree at most 2d − 2. Hence, using Theorem 3.4, we can conclude that

1

(±xl)σl(xl)w−1/2,−1/2(xl)dxl ≥ min{ξd−+11/2,−1/2,ξd1/2,1/2}. This implies that

−1

f(d) =

n

n

(

clxl)σ(x)dµ(x) =

cl

K

l=1

l=1

1

xlσl(xl)w−1/2,−1/2(xl)dxl

−1

is at least ( l |cl|)min{ξd−+11/2,−1/2,ξd1/2,1/2} and the proof is complete.

![image 115](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile115.png>)

![image 116](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile116.png>)

![image 117](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile117.png>)

![image 118](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile118.png>)

# 4 Tight upper bounds for the Lasserre hierarchy

In this section we analyze the rate of convergence of the Lasserre bounds fK(d) when using the measure dµ(x) = ni=1 w−1/2,−1/2(xi)dxi on the box K = [−1,1]n (corresponding to the Chebyshev orthogonal polynomials). For this measure, it is known that the stronger bounds f(d) - that use a much richer class of density functions - enjoy a O(1/d2) rate of convergence ([3], see Theorem 1.3).

![image 119](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile119.png>)

We show that the convergence rate remains O(1/d2) for the weaker bounds fK(d), which thus also implies Thoerem 1.3.

![image 120](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile120.png>)

- Theorem 4.1. Consider the measure dµ(x) = ni=1 w−1/2,−1/2(xi)dxi on the hypercube K =


[−1,1]n, with the weight function w−1/2,−1/2(xi) = (1 − x2i )−1/2 for i ∈ [n]. For any polynomial f we have

fK(d) − fmin,K = O(1/d2). It turns out that we can reduce the general result to the univariate quadratic case. In what follows we consider ﬁrst the special case when f is univariate and quadratic (see Lemma 4.2) and then we indicate how to derive the result for an arbitrary multivariate polynomial f. A key tool we use for

![image 121](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile121.png>)

this reduction is the existence of a quadratic upper estimator for f having the same minimum as f over K. In the quadratic univariate case we exploit again the formulation of fK(d) in terms of the smallest eigenvalue of the associated matrix Ad in (16) (recall Lemma 1.2). This matrix Ad is now 5-diagonal, but a key feature is that it contains a large Toeplitz submatrix, whose eigenvalues can be estimated by embedding it into a circulant matrix for which closed form expressions exist for the eigenvalues. This nice structure, which allows a simple analysis, follows from the choice of the Chebyshev type measure. We expect that a similar convergence rate should hold when selecting any measure of Jacobi type, but the analysis seems more complicated.

![image 122](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile122.png>)

- 4.1 The quadratic univariate case


Here we consider the case when K = [−1,1] and f is a univariate quadratic polynomial of the form f(x) = x2 + αx, for some scalar α ∈ R.

We can ﬁrst easily deal with the case when α  ∈ (−2,2). Indeed then we have f(x) ≤ g(x) := αx + 1 for all x ∈ [−1,1],

and both f and g have the same minimum value on [−1,1]. Namely, fmin,K = gmin,K is equal to 1 − α if α ≥ 2, and to 1 + α if α ≤ −2. Therefore we have

f(Kd) − fmin,K ≤ gK(d) − gmin,K = O(1/d2),

![image 123](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile123.png>)

![image 124](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile124.png>)

- where we use Corollary 3.3 for the last estimate.


We may now assume that f(x) = x2 + αx, where α ∈ [−2,2]. Then, fmin,K = −α2/4, which is attained at x = −α/2. After scaling the measure µ by 2/π, the Chebyshev polynomials Ti satisfy

1

2 π√1 − x2

dx = 0 if i = j, 2 if i = j = 0, 1 if i = j ≥ 1.

Ti(x)Tj(x)

![image 125](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile125.png>)

![image 126](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile126.png>)

−1

So with respect to this scaled measure the normalized Chebyshev polynomials are Tˆ0 = 1/√2 and Tˆi = Ti for i ≥ 1, and they satisfy the 3-terms relation:

![image 127](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile127.png>)

- 1

![image 128](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile128.png>)

- 2


1 √2

- 1

![image 129](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile129.png>)

- 2


- 1

![image 130](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile130.png>)

- 2


Tˆ0 and xTˆk =

Tˆ2 +

Tˆk+1 +

Tˆk−1 for k ≥ 2.

xTˆ1 =

![image 131](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile131.png>)

![image 132](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile132.png>)

In view of Lemma 1.2 we know that the parameter fK(d) is equal to the smallest eigenvalue of the following matrix

![image 133](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile133.png>)

d

1

2 π√1 − x2

(x2 + αx)Tˆi(x)Tˆj(x)

Ad =

dx

.

![image 134](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile134.png>)

![image 135](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile135.png>)

−1

i,j=0

Using the above 3-terms relations one can verify that the matrix Ad has the following form:

- 1

![image 136](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile136.png>)

- 2√2


1 2

√α2 √α2





![image 137](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile137.png>)

![image 138](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile138.png>)

![image 139](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile139.png>)

![image 140](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile140.png>)

- 3

![image 141](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile141.png>)

- 4


α 2

1 4

![image 142](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile142.png>)

![image 143](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile143.png>)

![image 144](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile144.png>)

![image 145](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile145.png>)

- 1

![image 146](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile146.png>)

- 2√2


α 2 a b c 1 4 b a b c

![image 147](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile147.png>)

![image 148](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile148.png>)

![image 149](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile149.png>)

... c

...

...

c b

, (16)

Ad =

...

...

...

...

...

...

...

... c

...

...

... b c b a

 

 

where we set a = 1/2, b = α/2 and c = 1/4.

Observe that if we remove the ﬁrst two rows and columns of A then we obtain a principal submatrix, denoted B, which is a symmetric 5-diagonal Toeplitz matrix. Now we may embed B into a symmetric circulant matrix of size d + 1, denoted Cd, by suitably deﬁning the ﬁrst two rows and columns. Namely,

- a b c c b
- b a b c c
- c b a b c c b a b c






... c

...

...

c b

Cd =

.

...

...

...

...

... c c

...

...

...

... b b c c b a

...

...

 

 

Recall that the eigenvalues of a circulant matrix are known in closed form, see, e.g., [9]. In particular, the eigenvalues of Cd are given by

a + 2b cos(2πj/(d + 1)) + 2c cos(2π2j/(d + 1), j = 0,...,d, (d ≥ 5). (17) By the Cauchy interlacing theorem for eigenvalues (see, e.g., Corollary 2.2 in [10]), we have f(Kd) = λmin(Ad) ≤ λmin(B) ≤ λ3(Cd),

![image 150](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile150.png>)

where λ3(Cd) is the third smallest eigenvalue of Cd. As noted above the eigenvalues of Cd are known in closed form as in (17) and this is the key fact which enables us to conclude the analysis.

Lemma 4.2. For any α ∈ [−2,2], the third smallest eigenvalue of the matrix Cd satisﬁes

α2 4

1 d2

λ3(Cd) = −

.

+ O

![image 151](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile151.png>)

![image 152](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile152.png>)

Therefore, if f(x) = x2 + αx with α ∈ [−2,2] then fK(d) − fmin,K = O(1/d2).

![image 153](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile153.png>)

Proof. Setting ϑj = d2+1πj for j ∈ N, then by (17) the eigenvalues of the matrix Cd are the scalars

![image 154](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile154.png>)

- 1

![image 155](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile155.png>)

- 2


- 1

![image 156](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile156.png>)

- 2


cos(2ϑj) = cos2(ϑj) + αcos(ϑj) for 0 ≤ j ≤ d.

+ αcos(ϑj) +

Consider the function f(ϑ) = cos2(ϑ)+α cos(ϑ) for ϑ ∈ [0,2π]. Then f satisﬁes: f(ϑ) = f(2π −ϑ), and its minimum value is equal to −α2/4, which is attained at ϑ = arccos(−α/2) ∈ [0,π] and 2π−ϑ. Let j be the integer such that ϑj ≤ ϑ < ϑj+1. Then the smallest eigenvalue of Cd is λmin(Cd) = min{f(ϑj),f(ϑj+1)} and its third smallest eigenvalue is given by λ3(Cd) = min{f(ϑj−1),f(ϑj+1)} if λmin(Cd) = f(ϑj), and λ3(Cd) = min{f(ϑj),f(ϑj+2)} if λmin(Cd) = f(ϑj+1). Therefore, λ3(Cd) = f(ϑk) for some k ∈ {j − 1,j,j + 1,j + 2}.

Using Taylor theorem (and the fact that f′(ϑ) = 0) we can conclude that

α2 4

λ3(Cd) +

![image 157](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile157.png>)

= f(ϑk) − f(ϑ) =

- 1

![image 158](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile158.png>)

- 2


f′′(ξ)(ϑ − ϑk)2,

for some scalar ξ ∈ (ϑ,ϑk) (or (ϑk,ϑ)). Finally, f′′(ξ) = −2 cos(ξ) − αcos(ξ) and thus we have |f′′(ξ)| ≤ 2 + |α|. Also |ϑ− ϑk| ≤ |ϑj+2 − ϑj−1| = d6+1π . The claimed result now follows directly.

![image 159](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile159.png>)

![image 160](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile160.png>)

![image 161](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile161.png>)

![image 162](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile162.png>)

![image 163](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile163.png>)

- 4.2 The general case As a direct application we can also deal with the case when f is multivariate quadratic and separable.


- Corollary 4.3. Consider the box K = [−1,1]n and a multivariate polynomial of the form f(x) = n i=1 x2i + αixi for some scalars αi ∈ R. Then we have fK(d) − fmin,K = O(1/d2).


![image 164](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile164.png>)

Proof. The polynomial f is separable: f(x) = ni=1 fi(xi), after setting fi(xi) = x2i + αixi. Hence its minimum over the box K is fmin,K = ni=1(fi)min,[−1,1]. Suppose σi ∈ Σ[xi]d is an optimal density function for the bound fi([−d)1,1] and consider the polynomial σ(x) = ni=1 σi(xi) ∈ Σ[x]nd, which is a density function over K. Then we have

![image 165](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile165.png>)

f(Knd) − fmin,K ≤

![image 166](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile166.png>)

n

f(x)σ(x)dµ(x) =

K

i=1

1

fi(xi)dµ(xi) − (fi)min,[−1,1] = O(1/d2),

−1

where we use Lemma 4.2 for the last estimate. This implies the claimed convergence rate for the bounds f(Kd).

![image 167](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile167.png>)

![image 168](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile168.png>)

![image 169](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile169.png>)

![image 170](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile170.png>)

![image 171](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile171.png>)

Assume now f is an arbitrary polynomial and let a ∈ K = [−1,1]n be a minimizer of f over K. Consider the following quadratic polynomial

g(x) = f(a) + ∇f(a)T(x − a) + Cf x − a 22,

where we set Cf = maxx∈K  ∇2f(x) 2. By Taylor’s theorem we know that f(x) ≤ g(x) for all x ∈ K and that the minimum value of g(x) over K is gmin,K = f(a) = fmin,K. This implies

f(Kd) − fmin,K ≤ gK(d) − gmin,K = O(1/d2),

![image 172](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile172.png>)

![image 173](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile173.png>)

- where we use Corollary 4.3 for the last estimate. This concludes the proof of Theorem 4.1.


# 5 Concluding remarks

Some other hierarchical upper bounds for polynomial optimization over the hypercube have been investigated in the literature. In particular, bounds are proposed in [4], that rely on selecting density functions arising from beta distributions:

f(x)xα(1 − x)β dx

fdH := min

K

,

![image 174](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile174.png>)

(α,β)∈N(2n,d)

xα(1 − x)β dx

K

where, K = [−1,1]n, and (1 − x)β = ni=1(1 − xi)β

for β ∈ Nn. These bounds can be computed

i

via elementary operations only and their rate of convergence is fdH −fmin,K = O(1/√d) (or O(1/d) for quadratic polynomials with rational data).

![image 175](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile175.png>)

Other hierarchies involve selecting discrete measures. They rely on polynomial evaluations at rational grid points [1] or at polynomial meshes like Chebyshev grids [14]. The grids in [14] are given by the Chebyshev-Lobatto points:

Cd := cos

jπ d

![image 176](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile176.png>)

j = 0,...,d.

f(x) − fmin,K = O d 12 , where Cdn = Cd × ··· × Cd ⊂ [−1,1]n.

In particular the authors of [14] show that minx∈Cn

![image 177](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile177.png>)

d

Note that |Cdn| = (d + 1)n, which is of course exponential in n even for ﬁxed d.

The same O d 12 rate of convergence was shown in [1] for the regular grid (using d + 1 evenly spaced points). We also refer to the recent work [15] where polynomial meshes are investigated for polynomial optimization over general convex bodies.

![image 178](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile178.png>)

Thus the Lasserre bound f(Kd) has the same O d 12 asymptotic rate of convergence as the grid searches, but with the advantage that the computation may be done in polynomial time for ﬁxed d.

![image 179](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile179.png>)

![image 180](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile180.png>)

Of course, the problem studied in this paper falls in the general framework of bound-constrained global optimization problems, and many other algorithms are available for such problems; a recent survey is given in the thesis [13]. The point is that the

methods we studied in this paper allow analysis of the convergence rate to the global minimum. We conclude with some unresolved questions:

- • Does the O d 12 rate of convergence still hold for the Lasserre bounds if K is a general convex body? (The best known result is the O(1/d) rate from [2].)

![image 181](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile181.png>)

- • What is the precise inﬂuence of the choice of reference measure µ in (1) on the convergence rate?
- • Is is possible to show a ‘saturation’ result for the Lasserre bounds of the type:


1 d2 ⇐⇒ f is a constant polynomial?

f(Kd) − fmin,K = o

![image 182](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile182.png>)

![image 183](<2018-klerk-worst-case-examples-lasserre-measure-based_images/imageFile183.png>)

In other words, is O(1/d2) the fastest possible convergence rate for nonconstant polynomials?

Acknowledgements. The authors would like to thank Jean-Bernard Lasserre for useful discussions.

# References

- [1] E. de Klerk, M. Laurent. Error bounds for some semideﬁnite programming approaches to polynomial optimization on the hypercube. SIAM Journal on Optimization 20(6), (2010) 3104– 3120.
- [2] E. de Klerk and M. Laurent. Comparison of Lasserre’s measure-based bounds for polynomial optimization to bounds obtained by simulated annealing. Mathematics of Operations Research, to appear. arXiv:1703.00744
- [3] E. de Klerk, R. Hess and M. Laurent. Improved convergence rates for Lasserre-type hierarchies of upper bounds for box-constrained polynomial optimization. SIAM Journal on Optimization 27(1), (2017) 347-367.
- [4] E. de Klerk, J.-B. Lasserre, M. Laurent, and Z. Sun. Bound-constrained polynomial optimization using only elementary calculations. Mathematics of Operations Research 42(3), (2017) 834–853.
- [5] E. de Klerk, M. Laurent, Z. Sun. Convergence analysis for Lasserre’s measure-based hierarchy of upper bounds for polynomial optimization, Mathematical Programming Ser. A 162(1), (2017) 363-392.
- [6] D.K. Dimitrov, G.P. Nikolov. Sharp bounds for the extreme zeros of classical orthogonal polynomials, Journal of Approximation Theory 162 (2010), 1793–1804.
- [7] K. Driver, K. Jordaan. Bounds for extreme zeros of some classical orthogonal polynomials. Journal of Approximation Theory 164 (2012), 1200–1204.
- [8] W. Gautsch. Orthogonal Polynomials - Computation and Approximation. Oxford University Press, 2004.
- [9] R.M. Gray. Toeplitz and circulant matrices: A review. Foundations and Trends in Communications and Information Theory 2(3) (2006), 155–239.
- [10] W.H. Haemers. Interlacing eigenvalues and graphs. Linear Algebra and its Applications 227-228

(1995), 593–616.

- [11] M.E.H. Ismail, X. Li. Bounds on the extreme zeros of orthogonal polynomials. Proc. Amer. Math. Soc. 115 (1992), 131–140.
- [12] J.B. Lasserre. A new look at nonnegativity on closed sets and polynomial optimization. SIAM Journal on Optimization 21(3) (2011), 864–885.
- [13] Pa´l, L.: Global Optimization Algorithms for Bound Constrained Problems. PhD thesis, University of Szeged (2010). Available at http://www2.sci.u-szeged.hu/fokozatok/PDF/Pal_Laszlo/Diszertacio_PalLaszlo.pdf


- [14] F. Piazzon, M. Vianello. A note on total degree polynomial optimization by Chebyshev grids. Optimization Letters 12 (2018), 63–71.
- [15] F. Piazzon and M. Vianello. Markov inequalities, Dubiner distance, norming meshes and polynomial optimization on convex bodies. Preprint, 2018. Available at http://www.math.unipd.it/~marcov/pdf/convbodies.pdf
- [16] G. Szego¨. Orthogonal Polynomials, fourth ed., vol. XXIII, American Mathematical Society Colloquium Publications, Providence, RI, 1975.


