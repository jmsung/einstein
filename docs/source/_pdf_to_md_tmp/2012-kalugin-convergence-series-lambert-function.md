arXiv:1208.0754v1[math.CA]2Aug2012

# Convergence in C of series for the Lambert W Function

G. A. Kalugin and D. J. Jeﬀrey Department of Applied Mathematics The University of Western Ontario, London, Canada

May 21, 2018

Abstract

We study some series expansions for the Lambert W function. We show that known asymptotic series converge in both real and complex domains. We establish the precise domains of convergence and other properties of the series, including asymptotic expressions for the expansion coeﬃcients. We introduce an new invariant transformation of the series. The transformation contains a parameter whose eﬀect on the domain and rate of convergence is studied theoretically and numerically. We also give alternate representations of the expansion coeﬃcients, which imply a number of combinatorial identities.

## 1 Introduction

The equation yαey = x was solved by de Bruijn and by Comtet [5, 7], as an asymptotic expansion:

1 − τ σ

y = Φα(x) = lnx − α lnlnx + αu = α

+ u , (1.1) where

![image 1](<2012-kalugin-convergence-series-lambert-function_images/imageFile1.png>)

α lnx

lnlnx lnx

σ =

, (1.2) and

, τ = α

![image 2](<2012-kalugin-convergence-series-lambert-function_images/imageFile2.png>)

![image 3](<2012-kalugin-convergence-series-lambert-function_images/imageFile3.png>)

∞

n

σn−mτm m!

n n − m + 1

(−1)n−m

, (1.3)

u(σ, τ) =

![image 4](<2012-kalugin-convergence-series-lambert-function_images/imageFile4.png>)

n=1

m=1

and where n−m n+1 denotes a Stirling cycle number [11, 10]. The function u obeys the fundamental relation

1 − e−u + σu − τ = 0 . (1.4) By rewriting (1.4) in terms of ζ = 1/(1+σ), a second series for u was obtained by [17] in terms of 2-associated Stirling partition numbers [11], also called Stirling subset numbers or Stirling numbers of the 2nd kind.

∞

m−1

ζp+mτm m!

p + m − 1 p ≥2

(−1)p+m−1

u =

. (1.5)

![image 5](<2012-kalugin-convergence-series-lambert-function_images/imageFile5.png>)

m=1

p=0

Since yαey = x can be solved in terms of the Lambert W function, as y = αW(x1/α/α), the series solutions above are also series for the principal branch of W. We recall that branches are denoted Wk, and of these only W0 and W−1 take real values, obeying the inequalities [8]

− 1 ≤ W0(x) < ∞ for − 1/e ≤ x < ∞ , − ∞ < W−1(x) < −1 for − 1/e < x < 0 .

Here, we are concerned only with the principal branch k = 0, although some discussion of series expansions for branch k = −1 is given in section 5.

The convergence properties of the asymptotic series (1.3) and (1.5) were ﬁrst studied in the real case in [17], and bounds on the domains of convergence obtained. Here we establish the precise domains of convergence of the series both on the real line and in the complex plane. We analyze the diﬀerences in the properties of the series and ﬁnd asymptotic expressions for the expansion coeﬃcients in (1.5). We also consider invariant transformations of the above series. The transformations contain a parameter p (related to α above) and retain the basic series structure while p varies. The parameter changes the convergence domains of the series as well as the rates of convergence.

A third series is studied, derived from one for the Wright ω function [9].

∞

W(x) = ω0 +

m=1

m−1

1 m!σm(1 + ω0)2m−1

![image 6](<2012-kalugin-convergence-series-lambert-function_images/imageFile6.png>)

k=0

m − 1 k

(−1)kω0k+1 , (1.6)

where σ = 1/ lnx and ω0 denotes the Omega constant W(1) = 0.56714329... The notation and deﬁnition of the second-order Eulerian numbers may be found in [11, 10]. We give three new representations of the expansion coeﬃcients of this series as well as their asymptotic estimates. It is also shown that the series (1.5) can also be expressed using the second-order Eulerian numbers. Some combinatorial identities follow from the diﬀerent forms for coeﬃcients, including the Carlitz-Riordan identities.

## 2 First series expansion (1.3)

It is convenient to consider separately the case in which x > 1, making σ, τ and u all real. This was the case studied in [17], where bounds on the convergence domain were given, and is the subject of the next subsection.

- 2.1 Convergence for real values We begin by stating a convergence criterion in terms of the variables σ and τ.


- Theorem 1. The domain of convergence of the series (1.3) is deﬁned by the inequality


τ σ

lnσ < 1 −

τ

σ−1 . (2.1)

+ ℜW−1 −e

![image 7](<2012-kalugin-convergence-series-lambert-function_images/imageFile7.png>)

![image 8](<2012-kalugin-convergence-series-lambert-function_images/imageFile8.png>)

Proof. We rewrite the fundamental relation (1.4) by introducing λ = τ/σ to play the role of a parameter.

Gλ(σ, u) = 1 − e−u + σu − σλ = 0 . (2.2)

By the implicit function theorem [21], for ﬁxed λ ∈ R, equation (2.2) determines a function

uλ(σ) =

m

cm(λ)σm (2.3)

with initial condition uλ(0) = 0 in a domain where ∂Gλ(σ, u)/∂u = e−u + σ = 0. The radius of convergence of this power series equals the distance from the origin in the complex σ-plane to the closest singular point [26],[3, p.175, Theorem 4.3.2]. The critical points in the complex σ-plane, where ∂Gλ(σ, u)/∂u = 0, satisfy the relations, after using (2.2),

e−u = −σ , (2.4) λ − u − 1 = 1/σ , (2.5)

−eλ−1σ = e1/σ . (2.6) From these, σ can be written in terms of the Lambert W function

σm = 1/Wm(−eλ−1) , (2.7)

where the mth root is deﬁned by the mth branch of W. Further, by (2.5), ℑ(1/σ) = ℑ(−u), and for the principal branch ℑ(u) ∈ (−π, π). Thus we conclude that there are only two acceptable values for m, i.e. m = −1, 0. We now write (2.6) as

σm = −exp 1 − λ + Wm(−eλ−1) (m = −1, 0) , (2.8) which deﬁnes the domain of convergence by the inequality

−exp 1 − λ + Wm(−eλ−1) . or

|σ| < min

m∈{−1,0}

ℜWm(−eλ−1) . (2.9)

ln|σ| < 1 − ℜλ + min

m∈{−1,0}

Since ℜW−1(x) ≤ ℜW0(x) for all x ∈ R [8], after substituting λ = τ/σ the condition (2.1) follows.

![image 9](<2012-kalugin-convergence-series-lambert-function_images/imageFile9.png>)

![image 10](<2012-kalugin-convergence-series-lambert-function_images/imageFile10.png>)

![image 11](<2012-kalugin-convergence-series-lambert-function_images/imageFile11.png>)

![image 12](<2012-kalugin-convergence-series-lambert-function_images/imageFile12.png>)

To express the condition (2.1) of convergence of the series (1.3) in terms of independent variable x in (1.2) it is convenient to prove the following lemma. Lemma 1. Solution of inequality ℜW−1(x) > a for x < 0, where a is constant, is given by

x < b =

aea, a ≤ −1 −eaη0 csc η0, a > −1

(2.10)

where η0 ∈ (0, π) is the root of equation η0 cot η0 = −a. Proof. We set W−1(x) = ξ + iη for real negative x where ξ ≤ −1, η = 0 for −1/e ≤ x < 0 and ξ > −1, −π < η < 0 for x < −1/e. Then ξ, η obey [8]

x = eξ(ξ cosη − η sinη), 0 = eξ(η cosη + ξ sin η) .

From these equations, one can ﬁnd the dependence of ξ on x explicitly for −1/e ≤ x < 0

ξ = W−1(x) (2.11) and parametrically for x < −1/e

x = −η csc(η)e−ηcotη , (2.12)

ξ = −η cot η , (2.13) where −π < η < 0.

Now we consider inequality ξ > a in two cases comparing a with value −1. When a ≤ −1 the inequality ξ > a holds for all x < −1/e because in this case ξ > −1 by

- (2.13). For −1/e ≤ x < 0 we solve inequality W−1(x) > a due to (2.11) with the result −1/e ≤ x < aea. Thus ξ > a for x < aea. When a > −1 the inequality ξ > a can have a solution only for x < −1/e because ξ ≤ −1 for the rest x. According to (2.12) and (2.13) the solution is given by x < −η0 csc(η0) exp(−η0 cotη0) where η0 ∈ (−π, 0) satisﬁes the equation −η0 cotη0 = a due to which the solution can also be written as x < −eaη0 csc η0 and η0 ∈ (0, π). Joining both cases, the lemma follows.


![image 13](<2012-kalugin-convergence-series-lambert-function_images/imageFile13.png>)

![image 14](<2012-kalugin-convergence-series-lambert-function_images/imageFile14.png>)

![image 15](<2012-kalugin-convergence-series-lambert-function_images/imageFile15.png>)

![image 16](<2012-kalugin-convergence-series-lambert-function_images/imageFile16.png>)

Note that in the formula (2.10), when a > −1 but a = 0, we can also write b = aea/ cosη0.

- Theorem 2. The series (1.3) is convergent when


x > xα =

(e/α)α , 0 < α ≤ 1 eαη

0cscη0, α > 1

(2.14)

where η0 satisﬁes the equation η0 cot η0 = 1 − lnα (0 < η0 < π), and the series is divergent otherwise.

Proof. We consider the condition of convergence of the series (1.3) established by Theorem 1 in the real case, i.e. when α > 0 and x > 1. Substituting the expressions (1.2) in (2.1) we obtain

lnx e

ℜW−1 −

![image 17](<2012-kalugin-convergence-series-lambert-function_images/imageFile17.png>)

> lnα − 1 . (2.15)

Applying Lemma 1 to the inequality (2.15) we come to (2.14), where xα > 1, which justiﬁes the assumption x > 1. Thus the theorem is completely proved.

![image 18](<2012-kalugin-convergence-series-lambert-function_images/imageFile18.png>)

![image 19](<2012-kalugin-convergence-series-lambert-function_images/imageFile19.png>)

![image 20](<2012-kalugin-convergence-series-lambert-function_images/imageFile20.png>)

![image 21](<2012-kalugin-convergence-series-lambert-function_images/imageFile21.png>)

Note. The statement of Theorem 2 was independently reported by A.J.E.M. Janssen and J.S.H. van Leeuwaarden [16].

- Remark 3. In the formula (2.14), when α > 1 but α = e, we can also write xα = (e/α)αsecη0.
- Remark 4. It follows from (2.14) that xα → 1 as α → 0 and xα → ∞ as α → ∞. In addition, one can show that a function of α deﬁned by (2.14) is monotone increasing. Therefore, the larger α, the less the domain of convergence of the series (1.3).


Corollary 5. Series (1.3) for α = 1, i.e. for W function, is convergent when

lnx e

ℜ W−1 −

![image 22](<2012-kalugin-convergence-series-lambert-function_images/imageFile22.png>)

> −1 , (2.16)

which is equivalent to x > e, and divergent when the opposite inequalities hold. Proof. Follows immediately from (2.15) and (2.14). Remark 6. In terms of variable σ = 1/ lnx series (1.3) is convergent for 0 < σ < 1.

![image 23](<2012-kalugin-convergence-series-lambert-function_images/imageFile23.png>)

![image 24](<2012-kalugin-convergence-series-lambert-function_images/imageFile24.png>)

![image 25](<2012-kalugin-convergence-series-lambert-function_images/imageFile25.png>)

![image 26](<2012-kalugin-convergence-series-lambert-function_images/imageFile26.png>)

We now prove a statement, relating to divergence of the series (1.3), which was found by us earlier than the conditions (2.14) but unlike Theorem 2 concerning positive α it deals with any α = 0. In addition, the statement demonstrates an interesting application of the ratio test to the series (1.3).

- Theorem 7. The series (1.3) is divergent at least for e−|α| < x < eb|α| (2.17)


where

b =

W (1/ |α|) when |α| < 1/e , 1 when |α| ≥ 1/e .

Proof. Changing indices for summing the expansion (1.3) can be written through a double series [17]

∞

∞

cm,l, (2.18) where

u =

m=1

l=0

(−1)l m!

l + m l + 1

σlτm

cm,l = cm,l(σ, τ) =

![image 27](<2012-kalugin-convergence-series-lambert-function_images/imageFile27.png>)

For the column-series m cm,l the ratio test gives

lim

m→∞

cm+1,l cm,l

![image 28](<2012-kalugin-convergence-series-lambert-function_images/imageFile28.png>)

l + m + 1 l + 1 (m + 1)

= |τ| lim

= |τ|

![image 29](<2012-kalugin-convergence-series-lambert-function_images/imageFile29.png>)

l + m l + 1

m→∞

- as according to [1]


p + 1 l + 1

= 1 for ﬁxed l

lim

![image 30](<2012-kalugin-convergence-series-lambert-function_images/imageFile30.png>)

p l + 1

p→∞

p

in our notations. For the row-series l cm,l we have

lim

l→∞

cm,l+1 cm,l

![image 31](<2012-kalugin-convergence-series-lambert-function_images/imageFile31.png>)

l + m + 1 l + 2 l + m l + 1

= |σ| lim

= |σ|

![image 32](<2012-kalugin-convergence-series-lambert-function_images/imageFile32.png>)

l→∞

because by [1]

l + m l + 1 (l + 1)2m−2

1 2m−1(m − 1)!

lim

=

for ﬁxed m.

![image 33](<2012-kalugin-convergence-series-lambert-function_images/imageFile33.png>)

![image 34](<2012-kalugin-convergence-series-lambert-function_images/imageFile34.png>)

l→∞

According to [20, Theorem 2.7] the series (2.18) (and therefore (1.3)) is divergent when |τ| > 1 or |σ| > 1. Expressing these inequalities in terms of x by (1.2) and uniting the obtained sets we come to the stated inequality (2.17).

![image 35](<2012-kalugin-convergence-series-lambert-function_images/imageFile35.png>)

![image 36](<2012-kalugin-convergence-series-lambert-function_images/imageFile36.png>)

![image 37](<2012-kalugin-convergence-series-lambert-function_images/imageFile37.png>)

![image 38](<2012-kalugin-convergence-series-lambert-function_images/imageFile38.png>)

By Theorem 7 for α = 1 the series (1.3) is divergent at least for e−1 < x < e, which is consistent with Corollary 5.

For comparison, the curves described by equations (2.14) and (2.17) are shown in Figure 1 by solid and dash-dotted lines respectively, together with the bound given in [17].

- Figure 1: Boundary of domain of convergence of series (1.3) given by (2.14) is depicted by solid line; dashed and dash-dotted lines are described by equations given in reference [17] and (2.17) respectively.


- 2.2 Convergence in complex case In this subsection we consider equations (1.1), (1.2) only for α = 1 (under the same relation


- (1.4)) and derive convergence conditions for the series (1.3) in the complex case using the results obtained in Section 2.1 in the real case and providing a continuous continuation of the latter. We set


σ = 1/lnz, τ = lnlnz/lnz , (2.19)

where z = x + iy is a complex variable and lnz denotes the principal branch of the natural logarithm. Then the right-hand side of the series (1.3) represents a function of the complex variable z and the following theorem holds.

- Theorem 8. The domain of convergence of the series (1.3) in the complex z-plane is deﬁned by


lnz e

ℜWm −

![image 39](<2012-kalugin-convergence-series-lambert-function_images/imageFile39.png>)

where the branch Wm is chosen as follows

> −1, (2.20)

m = −1, −π < arg z ≤ 0 1, 0 < arg z ≤ π

Proof. Repeating the proof of Theorem 1 under assumption λ ∈ C we come to an equation which is diﬀerent from (2.9) only by that m ∈ Z. Then substituting (2.19) in there we obtain (cf. (2.16))

ln z e

min

ℜWm −

> −1 . (2.21)

![image 40](<2012-kalugin-convergence-series-lambert-function_images/imageFile40.png>)

m∈Z

Now we cut the complex z-plane along the negative real axis and set arg z ∈ (−π, π]. We consider inequality (2.21) in domain D = {z ∈ C| − π < arg z ≤ 0} and assume that there exists some value m = q such that the domain of convergence in D is deﬁned by equation

ℜWq (−lnz/e) > −1 (2.22) and its continuous boundary L is given by

ℜWq (−lnz/e) = −1 . (2.23)

The domain of convergence found in real case is deﬁned in a similar way. Speciﬁcally, in domain {z ∈ R| z > 0} we have q = −1 and the boundary z = e (see Corollary 5). We require that in the limiting case arg z → 0− equation (2.22) become equation (2.16) and show that there is an unique value q = −1 satisfying this requirement. (If there were several such values of q, it would mean that the boundary L is composed of several pieces of diﬀerent curves, and to identify them one should reduce domain D, i.e. consider its subdomains.) Separating the real and imaginary parts of Wq (−lnz/e) = −1 + iη in the usual way, we ﬁnd

sin η − η cosη = arg z (2.24a) cos η + η sinη = ln|z| (2.24b)

These equations describe a set of the boundary points which can be found in the following way. Given a value for arg z one can ﬁnd η from (2.24a) which being substituted in (2.24b) yields the corresponding value of ln|z|. However, for ﬁxed arg z ∈ (−π, 0] the equation (2.24a) has an inﬁnite number of solutions. We select a solution to provide a continuous transition to the real case when arg z → 0− and when the boundary of the domain of convergence is deﬁned by ℜW−1(−lnz/e) = −1 (cf. (2.16)). An elementary analysis of the equation (2.24a) shows that

to meet these requirements one needs to choose a solution of this equation from the interval η ∈ (−π, 0] and set q = −1 in (2.23). Since by (2.24a) such solution exists if and only if z ∈ D, the above assumption is approved and the domain of convergence in D is described by (2.22) with q = −1, i.e.

ℜW−1(−lnz/e) > −1 .

![image 41](<2012-kalugin-convergence-series-lambert-function_images/imageFile41.png>)

Due to the near conjugate symmetry property of W function [8], i.e. Wk(z) = W−k(¯z) when z is not on the branch cut, we obtain the convergence condition ℜW1(−lnz/e) > −1 in the domain {z ∈ C| 0 < arg z ≤ π}. Thus the theorem is completely proved.

![image 42](<2012-kalugin-convergence-series-lambert-function_images/imageFile42.png>)

![image 43](<2012-kalugin-convergence-series-lambert-function_images/imageFile43.png>)

![image 44](<2012-kalugin-convergence-series-lambert-function_images/imageFile44.png>)

![image 45](<2012-kalugin-convergence-series-lambert-function_images/imageFile45.png>)

- Remark 9. The ’branch splitting’ in the proved formula (2.20) is due to the branch choices for the Lambert W function and similar to the eﬀect that occurs in the series for W about the branch point [10, Sec.3].
- Remark 10. The inequality opposite to (2.20) deﬁnes the domain where the series (1.3) is divergent. This domain is ﬁnite (it encloses the origin z = 0) and contains a subdomain deﬁned by inequality |σ| > 1. Therefore, unlike the real case (see Corollary 5) in the complex case the condition |σ| < 1 is only necessary but not suﬃcient for convergence of the series (1.3).


## 3 Series (1.5)

### 3.1 Convergence in real case

We regard the expansion (1.5) as a power series around τ = 0 where variable σ plays a role of a parameter.

Theorem 11. For α > 0 and σ > 0, the radius of convergence of the series (1.5) is exactly

τ∗(σ) = |1 + σ − σ lnσ ± iπσ| . (3.1) which is equiavalent to the condition of convergence of the series (1.5) as

![image 46](<2012-kalugin-convergence-series-lambert-function_images/imageFile46.png>)

|σ(lnα − lnσ)| < (1 + σ − σ lnσ)2 + π2σ2. (3.2) Proof. We rewrite the fundamental relation (1.4) in the form of equation

Fσ(τ, u) = 0, (3.3) where

Fσ(τ, u) = 1 − e−u + σu − τ , (3.4) and analyse this equation similarly to that in the proof of Theorem 1. By Implicit Function Theorem [21] the equation (3.3) determines a function uσ(τ) = m cm(σ)τm with initial condition uσ(0) = 0 in a domain where ∂Fσ(τ, u)/∂u = e−u +σ = 0. The initial condition is justiﬁed by ∂Fσ(0, 0)/∂u = 1 + σ = 0. Since the critical points are deﬁned by the same equation as in Theorem 1, they are given by (2.4) and the corresponding values of τ are

(k) ∗

τ∗(k) = 1 − e−u

+ σu(∗k) = 1 + σ − σ lnσ + iπσ(2k − 1), k ∈ Z (3.5)

The radius of convergence is equal to the distance from the origin in the complex τ-plane to the closest singular point [3, Theorem 4.3.2]. Among the critical points (3.5) there are two the nearest to the origin equidistant points which correspond to k = 0 and k = 1:

- τ∗(0) = 1 + σ − σ lnσ − iπσ, (3.6a)
- τ∗(1) = 1 + σ − σ lnσ + iπσ. (3.6b)


The corresponding values of u(∗k) are

- u(0)∗ = −lnσ − iπ, (3.7a)
- u(1)∗ = −lnσ + iπ. (3.7b)


Since the expansion coeﬃcients of the series (1.5) are real, the closest singularities can appear as a conjugate pair only [15]. Based on the Weierstrass’s preparation theorem [21, 2] we will show that the points (3.6) are singular, each corresponding to a square-root branch point of function u = uσ(τ) in the complex τ-plane. We will also ﬁnd a behavior of function u = uσ(τ) near the points (3.6) used then for a study of an asymptotic behaviour of the expansion coeﬃcients of the series (1.5).

Let us consider, for example, point τ = τ∗(0). Expanding the left-hand side of equation (3.3) into a Taylor series near the point S τ∗(0), u(0)∗ we obtain

∂Fσ(S) ∂τ

Fσ(S) +

![image 47](<2012-kalugin-convergence-series-lambert-function_images/imageFile47.png>)

∂Fσ(S) ∂u

τ − τ∗(0) +

![image 48](<2012-kalugin-convergence-series-lambert-function_images/imageFile48.png>)

2

τ − τ∗(0)

∂2Fσ(S) ∂τ2

u − u(0)∗ +

![image 49](<2012-kalugin-convergence-series-lambert-function_images/imageFile49.png>)

![image 50](<2012-kalugin-convergence-series-lambert-function_images/imageFile50.png>)

2

2

u − u(0)∗

∂2Fσ(S) ∂τ∂u

∂2Fσ(S) ∂u2

τ − τ∗(0) u − u(0)∗ +

+

+ · · · = 0, where dots denote the skipped terms of the higher order. Since

![image 51](<2012-kalugin-convergence-series-lambert-function_images/imageFile51.png>)

![image 52](<2012-kalugin-convergence-series-lambert-function_images/imageFile52.png>)

![image 53](<2012-kalugin-convergence-series-lambert-function_images/imageFile53.png>)

2

∂2Fσ(S) ∂u2

∂Fσ

∂Fσ(S) ∂u

= −exp −u(0)∗ , and

∂τ ≡ −1 the last equation becomes

= 0,

Fσ(S) = 0,

![image 54](<2012-kalugin-convergence-series-lambert-function_images/imageFile54.png>)

![image 55](<2012-kalugin-convergence-series-lambert-function_images/imageFile55.png>)

![image 56](<2012-kalugin-convergence-series-lambert-function_images/imageFile56.png>)

− τ − τ∗(0) − exp −u(0)∗

2

u − u(0)∗

+ · · · = 0.

![image 57](<2012-kalugin-convergence-series-lambert-function_images/imageFile57.png>)

2

Thus, in accordance with the Weierstrass’s preparation theorem [21, p.111], equation (3.3) is locally equivalent to the equation

τ∗(0) − τ ∼ exp −u(0)∗

2

u − u(0)∗

.

![image 58](<2012-kalugin-convergence-series-lambert-function_images/imageFile58.png>)

2

It follows that at τ = τ∗(0) function u = uσ(τ) has a singularity corresponding to a square-root branch point as near this point

u ∼ u(0)∗ ± exp

u(0)∗ 2

![image 59](<2012-kalugin-convergence-series-lambert-function_images/imageFile59.png>)

![image 60](<2012-kalugin-convergence-series-lambert-function_images/imageFile60.png>)

2 τ∗(0) − τ

or substituting (3.7a)

u ∼ −lnσ − iπ ± i

![image 61](<2012-kalugin-convergence-series-lambert-function_images/imageFile61.png>)

2τ∗(0) σ

![image 62](<2012-kalugin-convergence-series-lambert-function_images/imageFile62.png>)

τ τ∗(0)

1 −

![image 63](<2012-kalugin-convergence-series-lambert-function_images/imageFile63.png>)

- 1

![image 64](<2012-kalugin-convergence-series-lambert-function_images/imageFile64.png>)

- 2


. (3.8)

It is not diﬃcult to show that if we consider the values of the function (3.8) in the interior of the circle of radius (3.1) remaining in the vicinity of τ = τ∗(0) then the function (3.8) taken with the plus sign only satisﬁes the condition −π < ℑu < 0, which corresponds to ℑu(0)∗ = −π < 0

- at point τ = τ∗(0) itself by (3.7a). Moreover, since in the mentioned vicinity −π < ℑτ/σ < 0, we have −π < ℑW < π, which corresponds to the principal branch of W function [8]. Thus we come to conclusion that the function u = uσ(τ) behaves near the singularity (3.6a) like


u ∼ −lnσ − iπ + i

![image 65](<2012-kalugin-convergence-series-lambert-function_images/imageFile65.png>)

2τ∗(0) σ

![image 66](<2012-kalugin-convergence-series-lambert-function_images/imageFile66.png>)

τ τ∗(0)

1 −

![image 67](<2012-kalugin-convergence-series-lambert-function_images/imageFile67.png>)

- 1

![image 68](<2012-kalugin-convergence-series-lambert-function_images/imageFile68.png>)

- 2


as τ → τ∗(0). (3.9a)

One can show in a similar way that near the singularity (3.6b) the function u = uσ(τ) behaves like

![image 69](<2012-kalugin-convergence-series-lambert-function_images/imageFile69.png>)

- 1

![image 70](<2012-kalugin-convergence-series-lambert-function_images/imageFile70.png>)

- 2


2τ∗(1) σ

τ τ∗(1)

as τ → τ∗(1). (3.9b) Thus the points (3.6) are singular and we immediately obtain expression (3.1); the inequality

1 −

u ∼ −lnσ + iπ − i

![image 71](<2012-kalugin-convergence-series-lambert-function_images/imageFile71.png>)

![image 72](<2012-kalugin-convergence-series-lambert-function_images/imageFile72.png>)

- (3.2) follows from (3.1) as τ = −σ(lnσ − lnα) due to (1.2). The theorem is completely proved.


![image 73](<2012-kalugin-convergence-series-lambert-function_images/imageFile73.png>)

![image 74](<2012-kalugin-convergence-series-lambert-function_images/imageFile74.png>)

![image 75](<2012-kalugin-convergence-series-lambert-function_images/imageFile75.png>)

![image 76](<2012-kalugin-convergence-series-lambert-function_images/imageFile76.png>)

Remark 12. From the values (3.6) and (3.7), we ﬁnd W(x) = −1 for both k = 0 and k = 1. Although it is well-known that this value of the Lambert W function corresponds to its branch point and asymptotics (3.9) can be obtained immediately from the results in [8, 10], we derived these asymptotic formulae to demonstrate a method based on the Weierstrass’s preparation theorem.

The inequality (3.2) can be written in the form |lnα − lnσ| < g(σ), where

![image 77](<2012-kalugin-convergence-series-lambert-function_images/imageFile77.png>)

g(σ) = π2 + (1 + 1/σ − lnσ)2 , (3.10) and solved with respect to α. Then the following theorem follows.

![image 78](<2012-kalugin-convergence-series-lambert-function_images/imageFile78.png>)

Theorem 13. Let σc = 1.059945... is the unique root of equation g(σ) (1 + 1/σ)2 − 1/(1 + 1/σ) = π and αc = σc exp(g(σc)) = 41.349171..., where function g(σ) is deﬁned by (3.10). Then the domain of convergence of series (1.5) depending on α is deﬁned as follows.

- (i) For 0 < α < e, the series (1.5) is convergent when 0 < σ < σα, where σα is the only root of the equation

lnσ − g(σ) = lnα, (3.11) which is equivalent to

x > xα = eα/σ

α

. (3.12) The series is divergent when σ > σα or 1 < x < xα.

- (ii) For e < α < αc, the series (1.5) is convergent for any σ > 0 or for any x > 1.
- (iii) For α > αc, the series (1.5) is convergent when σ < µα or σ > να, where µα and να are


roots of equation |lnσ − lnα| = g(σ), which is equivalent to x > eα/µ

or x < eα/ν

. The series is divergent when µα < σ < να or eα/ν

α

α

< x < eα/µ

.

α

α

Proof. We give details only for the ﬁrst part (i). In a particular case α < σ, equation (3.1) can be written as (3.11) with g(σ) deﬁned by (3.10). The left-hand side of equation (3.11), being a monotone increasing function for positive σ, goes to −∞ and 1 when σ tends to 0 and ∞ respectively. Therefore, for 0 < α < e the equation has the unique solution. Applying Theorem 11 the theorem follows.

![image 79](<2012-kalugin-convergence-series-lambert-function_images/imageFile79.png>)

![image 80](<2012-kalugin-convergence-series-lambert-function_images/imageFile80.png>)

![image 81](<2012-kalugin-convergence-series-lambert-function_images/imageFile81.png>)

![image 82](<2012-kalugin-convergence-series-lambert-function_images/imageFile82.png>)

Corollary 14. The series (1.5) for W function is convergent for 0 < σ < σ1, where σ1 = 224.790951... is the only root of the equation

![image 83](<2012-kalugin-convergence-series-lambert-function_images/imageFile83.png>)

|−σ lnσ| = (1 + σ − σ lnσ)2 + π2σ2, (3.13) which is equivalent to

x > x1 = e1/σ

= 1.004458... . (3.14) The series (1.5) is divergent for σ > σ1 or for 1 < x < x1. Proof. Follows from Theorem 13(i) for α = 1.

1

![image 84](<2012-kalugin-convergence-series-lambert-function_images/imageFile84.png>)

![image 85](<2012-kalugin-convergence-series-lambert-function_images/imageFile85.png>)

![image 86](<2012-kalugin-convergence-series-lambert-function_images/imageFile86.png>)

![image 87](<2012-kalugin-convergence-series-lambert-function_images/imageFile87.png>)

- Remark 15. In terms of the variable x the series (1.5) for W function is convergent for x > x1 > 1 rather than for x > 1 though x1 is very close to unit.
- Remark 16. Elementary analysis of equation (3.11) with substituting σ = α/ lnx(α) therein shows that x(α) > 1 for 0 < α < e and has one maximum ee−π = 1.044161... at point α =

e−π/W(1/e) = 0.155186.... This means the dependence x(α) to be a very weak and xα = x(α) can be evaluated with a good precision (with the relative error less than 5%) by a simple approximate equality xα ≈ x1 (0 < α < e) which becomes accurate when α = 1.

- Remark 17. The solution σ = σ1 of the equation (3.13) is much more than unit and can be found approximately with a good precision. Speciﬁcally, taking square of the both sides of (3.13) and leaving the main terms we obtain σ2 −2σ2 lnσ +π2σ2 −2σ lnσ ≈ 0. Searching for a


solution of the approximate equation in the form σ = exp(1+2π2)(1 + δ), where the exponential factor is an exact solution of the approximate equation with neglected last term and a correction

![image 88](<2012-kalugin-convergence-series-lambert-function_images/imageFile88.png>)

term δ is to be determined, we obtain an approximate value in deﬁcit σ1 ≈ exp(1+2π2) − 1+2π2 = 223.8126969.... Taking into consideration of the terms of higher powers in δ in a similar way,

![image 89](<2012-kalugin-convergence-series-lambert-function_images/imageFile89.png>)

![image 90](<2012-kalugin-convergence-series-lambert-function_images/imageFile90.png>)

one can obtain a more accurate value.

- Remark 18. For ﬁxed σ > 0 and α = 1, the singular points (3.6) of function uσ(τ) correspond to those of the Wright function ω = ω(s), which are s∗ = ξ ± iπ, where ξ ≤ −1 (see subsection 6.2). Indeed, we have τ∗ = 1 − σ lnσ − σs∗, i.e. τ∗ = 1 − σ lnσ − ξσ ∓ iπσ. Since ℜτ∗ has the minimum at ξ = −1, the closest singular points are deﬁned by equations, which are exactly

- (3.6).


- Remark 19. The convergence condition (3.2) has a clear geometrical interpretation in (σ, τ)plane. For example, for α = 1 one can show that in accordance with the inequality (3.2), when


σ < σ1 the curve L described by τ = −σ lnσ is located inside the region S bounded by curves τ = ± (1 + σ − σ lnσ)2 + π2σ2 , which expresses the condition of convergence of the series

![image 91](<2012-kalugin-convergence-series-lambert-function_images/imageFile91.png>)

- (1.5). However, at point σ = σ1 the curve L leaves the region S through the lower boundary curve that can be described for large σ by the asymptotic expression


- 1 + π2

![image 92](<2012-kalugin-convergence-series-lambert-function_images/imageFile92.png>)

- 2


![image 93](<2012-kalugin-convergence-series-lambert-function_images/imageFile93.png>)

τ(σ) = − (1 + σ − σ lnσ)2 + π2σ2 = −σ lnσ + σ −

σ lnσ

+ 1 + O

![image 94](<2012-kalugin-convergence-series-lambert-function_images/imageFile94.png>)

1 lnσ

![image 95](<2012-kalugin-convergence-series-lambert-function_images/imageFile95.png>)

.

It follows that afterwards the curve L remains below the lower boundary of S, which corresponds to the divergence of the series (1.5) for σ > σ1.

Now we consider case σ < 0, which should be done carefully as by Implicit Function Theorem it should be ∂Fσ(0, 0)/∂u = 0 due to the initial condition uσ(0) = 0 and therefore the value σ = −1 should be excluded. It follows from (3.5) that when σ < 0 and σ = −1, i.e. σ = |σ|eiπ and |σ| = 1 there is only one the nearest to the origin singularity given by (3.6b)

τ∗(1) = 1 + σ − σ ln|σ| (3.15)

that lies on the positive real axis. Correspondingly the radius of convergence instead of (3.1) is the modulus of the right-hand side of (3.15).

Finally, when σ = 0 the series following from (1.4)

∞

τm m

u = −ln(1 − τ) =

![image 96](<2012-kalugin-convergence-series-lambert-function_images/imageFile96.png>)

m=1

(3.16)

is convergent for |τ| < 1.

Note. When σ = −1, τ∗(1) = 0 by (3.15), i.e. the series diverges everywhere. We also note that in all cases considered above the condition of convergence of the series (1.5) is described in an uniform manner, particularly, the radius of convergence is given by (3.1).

### 3.2 Comparison with series (1.3)

Let us compare the domain of convergence for the series (1.3) and (1.5). Both can be represented in the form

∞

cm(σ)τm (3.17)

u =

m=1

(see (2.18) for the series (1.3)). However, by Corollary 14 and Corollary 5 the series (1.5) has a much wider domain of convergence than the series (1.3) (not only in the real case but also

in the complex case, see Figure 2 below). To undestand this phenomenon we note that both series (1.3) and (1.5) are deﬁned for x > 1, therefore the closer the boundary of a domain of convergence to 1, the wider domain of convergence. However, the expansion coeﬃcients cm(σ) in the series (1.3) are given by power series near σ = 0 whereas in the series (1.5), the expansion coeﬃcients are deﬁned through function ζ = ζ(σ), i.e. cm(σ) = cm(ζ(σ)), where ζ(σ) = 1/(1+σ), and are given by power series near ζ = 0. Since σ = 1/ lnx becomes larger as x is approaching 1, the series (1.5) has a wider domain of convergence. This corresponds to the fact that the function ζ = ζ(σ) maps the interior of the unit circle |σ| = 1 into an unbounded domain which is the right half-plane Rζ > 1/2. We also note that the series (1.3) and (1.5) have common values in the domain where they are both convergent, therefore the series (1.5) is an analytic continuation of the series (1.3).

In terms of variable ζ the series (1.5) becomes [17]

∞

m−1

τm m!

u =

![image 97](<2012-kalugin-convergence-series-lambert-function_images/imageFile97.png>)

m=1

p=0

p + m − 1 p ≥2

(−1)p+m−1ζp+m (3.18)

and can be regarded as a result of applying the Euler’s transformation for improvement of convergence of series [12]. Indeed, the standard Euler’s transformation associated with changing variable to extend a domain of convergence of the series (1.3) is ρ = σ/(1 + σ) [22]. Since in terms of a new varibale the fundamental relation (1.4) is written as

u e−u + u + τ − 1

,

1 − ρ =

![image 98](<2012-kalugin-convergence-series-lambert-function_images/imageFile98.png>)

it would be natural to introduce variable ζ = 1 − ρ = 1/(1 + σ) rather than ρ. The series (1.5),(3.18) were ﬁrst found in [17].

One can also show that a representation of W function through the function uτ(σ) =

∞

m=1 cm(τ)σm, where τ plays a role of parameter, can not extend the domain of convergence established for series (1.5). Indeed, in this case equation (3.3) changes to Fτ(σ, u) = 0 where Fτ(σ, u) is still deﬁned by the right-hand side of (3.4) but with initial condition uτ(0) = −ln(1− τ). By the Implicit Function Theorem it should be ∂Fτ(0, −ln(1 − τ))/∂u = 0, which gives τ = 1, i.e. |τ| < 1, and substituting τ = −σ lnσ yields 0 < σ < 1/ω0 as a necessary condition for convergence (cf. 0 < σ < σ1 in Corollary 14).

Thus among the series with the considered structures the series (1.5) has as wide as possible domain of convergence.

### 3.3 Asymptotics of expansion coeﬃcients

Once the behavior of function u = uσ(τ) near the nearest to the origin singularities has been established one can ﬁnd an asymptotic formula for the expansion coeﬃcients of the series (1.5) using the Darboux’s theorem about expansions at algebraic singularities [7, 4]. The similar approach, based on the Weierstrass’s preparation theorem and the Darboux’s theorem, was applied to asymptotic enumeration of trees in [23].

According to the Darboux’s theorem and found estimates (3.9) for σ > 0 the expansion

coeﬃcients in the series (3.17) have an asymptotic formula for large m as

![image 99](<2012-kalugin-convergence-series-lambert-function_images/imageFile99.png>)

![image 100](<2012-kalugin-convergence-series-lambert-function_images/imageFile100.png>)

 i

 

  + o 

2τ∗(0) σ

2τ∗(1) σ

1 Γ −12 τ∗(0)

1 Γ −12 τ∗(1)

1 m

 1 m

cm(σ) =

− i

m

m

m

![image 101](<2012-kalugin-convergence-series-lambert-function_images/imageFile101.png>)

![image 102](<2012-kalugin-convergence-series-lambert-function_images/imageFile102.png>)

![image 103](<2012-kalugin-convergence-series-lambert-function_images/imageFile103.png>)

![image 104](<2012-kalugin-convergence-series-lambert-function_images/imageFile104.png>)

![image 105](<2012-kalugin-convergence-series-lambert-function_images/imageFile105.png>)

![image 106](<2012-kalugin-convergence-series-lambert-function_images/imageFile106.png>)

- 1

![image 107](<2012-kalugin-convergence-series-lambert-function_images/imageFile107.png>)

- 2


- 1

![image 108](<2012-kalugin-convergence-series-lambert-function_images/imageFile108.png>)

- 2


3

2 τ∗(1)

m

m

![image 109](<2012-kalugin-convergence-series-lambert-function_images/imageFile109.png>)

![image 110](<2012-kalugin-convergence-series-lambert-function_images/imageFile110.png>)

![image 111](<2012-kalugin-convergence-series-lambert-function_images/imageFile111.png>)

or

  

  , (3.19)

1 τ∗(1)

1 τ∗(0)

i √2πσm

m−12 −

cm(σ) ∼

![image 112](<2012-kalugin-convergence-series-lambert-function_images/imageFile112.png>)

![image 113](<2012-kalugin-convergence-series-lambert-function_images/imageFile113.png>)

![image 114](<2012-kalugin-convergence-series-lambert-function_images/imageFile114.png>)

m−12

3 2

![image 115](<2012-kalugin-convergence-series-lambert-function_images/imageFile115.png>)

![image 116](<2012-kalugin-convergence-series-lambert-function_images/imageFile116.png>)

![image 117](<2012-kalugin-convergence-series-lambert-function_images/imageFile117.png>)

![image 118](<2012-kalugin-convergence-series-lambert-function_images/imageFile118.png>)

- as Γ −21 = −2√π. Setting τ∗(1) = τ∗(1) eiθ


![image 119](<2012-kalugin-convergence-series-lambert-function_images/imageFile119.png>)

we ﬁnd

1

![image 120](<2012-kalugin-convergence-series-lambert-function_images/imageFile120.png>)

cm(σ) ∼

sin m − 12 θ1 τm−

![image 121](<2012-kalugin-convergence-series-lambert-function_images/imageFile121.png>)

2 πσ

![image 122](<2012-kalugin-convergence-series-lambert-function_images/imageFile122.png>)

, as m → ∞ (3.20)

![image 123](<2012-kalugin-convergence-series-lambert-function_images/imageFile123.png>)

![image 124](<2012-kalugin-convergence-series-lambert-function_images/imageFile124.png>)

1

3 2

![image 125](<2012-kalugin-convergence-series-lambert-function_images/imageFile125.png>)

∗ 2m

![image 126](<2012-kalugin-convergence-series-lambert-function_images/imageFile126.png>)

where τ∗ = τ∗(σ) is deﬁned by (3.1) and θ1 = arg(1 + σ − σ lnσ + iπσ). Speciﬁcally, for σ > 0

1 W (1/e)

π 1 − lnσ + 1/σ

 

, if 0 < σ <

,

arctan

![image 127](<2012-kalugin-convergence-series-lambert-function_images/imageFile127.png>)

![image 128](<2012-kalugin-convergence-series-lambert-function_images/imageFile128.png>)

θ1 =

π 1 − lnσ + 1/σ

1 W (1/e)

π + arctan

, if σ >

.



![image 129](<2012-kalugin-convergence-series-lambert-function_images/imageFile129.png>)

![image 130](<2012-kalugin-convergence-series-lambert-function_images/imageFile130.png>)

It follows from (3.20) that for large m the expansion coeﬃcients in the series (1.5) disclose their oscillatory behavior due to sin function though the amplitude decays as τ∗(σ) > 1 for any σ > 0. Since the series (1.5) can be interpreted as a result of applying the Euler’s transformation to the series (1.3) (cf. (3.18)), we note that some cases of oscillatory coeﬃcients resulting from the Euler’s transformation are studied in [14].

In order to ﬁnd an asymptotic formula in case when σ < 0, suﬃce it to take in (3.19) only the ﬁrst term with (3.15)

1 2π |σ|m

cm(σ) ∼ −

![image 131](<2012-kalugin-convergence-series-lambert-function_images/imageFile131.png>)

- 1

![image 132](<2012-kalugin-convergence-series-lambert-function_images/imageFile132.png>)

- 2


3

2 (1 − |σ| + |σ|ln|σ|)m−

![image 133](<2012-kalugin-convergence-series-lambert-function_images/imageFile133.png>)

![image 134](<2012-kalugin-convergence-series-lambert-function_images/imageFile134.png>)

as m → ∞ (3.21)

Finally, for case σ = 0, it follows from (3.16) that for any m ∈ N

1 m

cm(0) =

. (3.22)

![image 135](<2012-kalugin-convergence-series-lambert-function_images/imageFile135.png>)

- 3.4 Convergence in complex case Theorem 11 is extended to the complex case. Theorem 20. For complex σ, the radius of convergence of the series (1.5) for α = 1 is


τ∗(σ) = |1 + σ − σ lnσ − iπσ| when ℑσ < 0 , (3.23a)

τ∗(σ) = |1 + σ − σ lnσ + iπσ| when ℑσ > 0 . (3.23b) In the complex z-plane this is equiavalent to the series (1.5) for W function is convergent everywhere in the exterior of the boundary line deﬁned by equation

|−σ lnσ| = |1 + σ − σ lnσ ± iπσ| , (3.24) where σ = 1/ lnz and sign minus or plus is taken respectively in the upper or lower half-plane. Proof. Repeating the proof of Theorem 11 under assumption σ ∈ C we obtain the same equations (2.4) and (3.5) for singular points u(∗k) and τ∗(k) respectively, where k ∈ Z. However, many of the singular points do not correspond to the principal branch of W function and relate to the other branches. We are going to ﬁnd acceptable values of k for which singular points relate to the principal branch of W.

To ﬁnd acceptable values of k, we utilize a relation τ = −σ lnσ following from (1.2) to obtain

u = W(es) − 1/σ − lnσ , (3.25)

- where s = 1−στ − lnσ. Let us consider values of u in the ǫ-vicinity of the point u(∗k). Comparing between (3.25) and (2.4) gives


![image 136](<2012-kalugin-convergence-series-lambert-function_images/imageFile136.png>)

iπ(2k − 1) + ǫeiϕ = W(es) − 1/σ ,

where −π < ϕ ≤ π. Setting z = |z| eiθ (−π < θ < π) in σ = 1/ lnz and separating the imaginary part in the last equation we obtain

π(2k − 1) + ǫsinϕ = ℑW − θ . (3.26)

Since for the principal branch −π < ℑW < π, we ﬁnd −1/2 − ǫsin ϕ/(2π) < k < 3/2 − ǫsinϕ/(2π), i.e. acceptable values are k = 0 and k = 1.

Now we note that both points τ∗(0) and τ∗(1) are singular, particularly, they correspond to a square-root branch point of function u = uσ(τ) for the same reason as in the real case (see proof of Theorem 11). Taking into account this result we consider equation (3.26) for ǫ = 0 in two cases k = 0 and k = 1. When k = 0, we have ℑW = θ −π. Since −π < ℑW < π, only positive θ satisfy this equation, i.e. 0 < θ < π. Similarly when k = 1 we have ℑW = θ + π which holds for −π < θ < 0. Thus we conclude that the curve |−σ lnσ| = τ∗(0)(σ) is located in the upper z-half-plane and the curve |−σ lnσ| = τ∗(1)(σ) is located in the lower z-half-plane, these curves being symmetric with respect to the real axis. Hence, the equation (3.24) describes the boundary of domain of convergence of the series (1.5) in the complex case. In addition, since σ = (ln|z| − iθ)/ |lnz|2, θ and ℑσ are of opposite signs and the equations (3.23) follow. The theorem is completely proved.

![image 137](<2012-kalugin-convergence-series-lambert-function_images/imageFile137.png>)

![image 138](<2012-kalugin-convergence-series-lambert-function_images/imageFile138.png>)

![image 139](<2012-kalugin-convergence-series-lambert-function_images/imageFile139.png>)

![image 140](<2012-kalugin-convergence-series-lambert-function_images/imageFile140.png>)

The curve deﬁned by equation (3.24) in the complex z-plane is depicted in Figure 2 by solid line in the upper half-plane only (corresponding to the negative sign) as it is symmetric with respect to the real axis. The exterior of this boundary line can be regarded as the domain of analytic continuation of the series (1.5) from the part of the real axis x > x1 (see Corollary 14) to the complex z-plane. For comparison in the same ﬁgure it is shown (by dashed line) the boundary line of the domain of convergence of the series (1.3) deﬁned by equation (2.20).

- Figure 2: The domains of convergence of series (1.5) and (1.3) in the complex z-plane are located in the exterior of the curves depicted by solid and dashed lines respectively.


Remark 21. We note that the case |σ| < 1 reveals a connection between the series (1.5) and (1.3). In particular, the case permits to expand 1/(1 + σ) in powers of σ in the former that after some rearrangments can be reduced to the latter [17]. In accordance with Theorem 8 the series (1.3) is convergent in domain V in the complex σ-plane deﬁned by (2.20) (written in terms of σ = 1/ lnz). One can show that the domain V is contained in the unit disc U = {σ ∈ C | |σ| < 1} (cf. Remark 10) with the boundaries of V and U having one common point σ = 1 (where both series are convergent). The series (1.5) is also convergent in V but has a wider domain of convergence being convergent (for |σ| < 1) in U ∩ H where a domain H bounded by curve (3.24).

In the end of this subsection we give asymptotics for the expansion coeﬃcients of the series

- (1.5) as m → ∞ when ℑσ = 0. It follows from the proof of Theorem 20 that in this case there


is only one singularity τ = τ∗(0) when ℑσ < 0 and τ = τ∗(1) when ℑσ > 0. Therefore, one can use formula (3.19) keeping only one corresponding term (unlike case of real σ when there occur two singularities and both terms constitute the asymptotic formula (3.20)). Thus, taking (3.6) we ﬁnd

±i (1 + σ − σ lnσ ± iπσ)m−1/2

1 √2πσm3/2

cm(σ) ∼

as m → ∞,

![image 141](<2012-kalugin-convergence-series-lambert-function_images/imageFile141.png>)

![image 142](<2012-kalugin-convergence-series-lambert-function_images/imageFile142.png>)

![image 143](<2012-kalugin-convergence-series-lambert-function_images/imageFile143.png>)

where sign ”+” (”−”) is taken in case of positive (negative) ℑσ.

### 3.5 Representation in terms of Eulerian numbers

The expansion coeﬃcients of the series (1.5) can be expressed in terms of the second-order Eulerian numbers [11, 10]. To show that we combine

1 − τ σ

u = W(es) −

, (3.27) where

![image 144](<2012-kalugin-convergence-series-lambert-function_images/imageFile144.png>)

1 − τ σ − lnσ . (3.28)

s = s(σ, τ) =

![image 145](<2012-kalugin-convergence-series-lambert-function_images/imageFile145.png>)

- and (3.17), then the coeﬃcients cm(σ) in the right-hand side of (3.17) are


1 m!

cm(σ) =

![image 146](<2012-kalugin-convergence-series-lambert-function_images/imageFile146.png>)

dm dτm

W (es)

=

![image 147](<2012-kalugin-convergence-series-lambert-function_images/imageFile147.png>)

τ=0

1 m! −

1 σ

![image 148](<2012-kalugin-convergence-series-lambert-function_images/imageFile148.png>)

![image 149](<2012-kalugin-convergence-series-lambert-function_images/imageFile149.png>)

m dm dsm

W (es)

![image 150](<2012-kalugin-convergence-series-lambert-function_images/imageFile150.png>)

s=−ln σ+1/σ

(3.29)

- as ∂s/∂τ = −1/σ by (3.28). Because of (3.27) the formula (3.29) is valid for m ≥ 2, for m = 1 we have


1 σ

d dτ

W (es)

c1(σ) =

. (3.30)

+

![image 151](<2012-kalugin-convergence-series-lambert-function_images/imageFile151.png>)

![image 152](<2012-kalugin-convergence-series-lambert-function_images/imageFile152.png>)

τ=0

Since [8, 10]

qm (W (es)) (1 + W (es))2m−1

dm dsm

W (es) =

,

![image 153](<2012-kalugin-convergence-series-lambert-function_images/imageFile153.png>)

![image 154](<2012-kalugin-convergence-series-lambert-function_images/imageFile154.png>)

where the polynomials qn(r) can be expressed in terms of the second-order Eulerian numbers [11, 10]

m−1

m − 1 k

(−1)krk+1,

qm(r) =

k=0

and

1 σ

1 σ

W (es)|s=−lnσ+1/σ = W

e1/σ =

, we ﬁnally obtain

![image 155](<2012-kalugin-convergence-series-lambert-function_images/imageFile155.png>)

![image 156](<2012-kalugin-convergence-series-lambert-function_images/imageFile156.png>)

m−1

(−1)mσm−1 m!(1 + σ)2m−1

1 1 + σ

, cm(σ) =

c1(σ) =

![image 157](<2012-kalugin-convergence-series-lambert-function_images/imageFile157.png>)

![image 158](<2012-kalugin-convergence-series-lambert-function_images/imageFile158.png>)

k=0

m − 1 k

(−1)k σk+1

, m ≥ 2. (3.31)

![image 159](<2012-kalugin-convergence-series-lambert-function_images/imageFile159.png>)

Substituting (3.31) into the right-hand side of (3.17) results in a desireable formula

τ 1 + σ

u =

![image 160](<2012-kalugin-convergence-series-lambert-function_images/imageFile160.png>)

m−1

∞

τm m!(1 + σ)2m−1

+

![image 161](<2012-kalugin-convergence-series-lambert-function_images/imageFile161.png>)

m=2

k=0

m − 1 k

(−1)m−kσm−k−2. (3.32)

By introducing the variable ζ = 1/(1 + σ) the series (3.32) can also be written as

∞

m−1

τm m!

u = τζ +

![image 162](<2012-kalugin-convergence-series-lambert-function_images/imageFile162.png>)

m=2

k=0

m − 1 k

(−1)m+kζm+k+1(1 − ζ)m−k−2. (3.33)

We note that the expansion (3.33) does not contain terms of the second order in ζ.

The series (1.5),(3.18),(3.32), and (3.33) have the same properties including the domain of convergence and the asymtotic estimates for the expansion coeﬃcients studied in Section 3.3. This fact leads to some combinatorial consequences considered in Section 7.

## 4 Transformed series

### 4.1 An invariant transformation

The above studied expansions (1.3) and (1.5) are limited in their domain of applicability by the fact that σ and τ are each singular at z = 1, restricting their utility to z > 1. In addition to the domain of validity of the variables, there is the question of the domain of convergence of the series ascertained in theorems 2, 8, 11 and 20.

In this section we consider transformations of the series (1.3) and (1.5) referred as to transformed series. Our aims are to improve the convergence properties with respect to domain of convergence and rate of convergence. Some results are obtained in [19] employing experimental approach; we supplement them with a theoretical study of convergence of the transformed series.

We reconsider the derivation of (1.3), trying the ansatz

W = lnz − ln(p + lnz) + u . (4.1) Substituting into the deﬁning equation WeW = z, we obtain

lnz − ln(p + lnz) + u

zeu p + lnz

= z

![image 163](<2012-kalugin-convergence-series-lambert-function_images/imageFile163.png>)

From this, it is clear that if we deﬁne

1 p + lnz

σ =

![image 164](<2012-kalugin-convergence-series-lambert-function_images/imageFile164.png>)

p + ln(p + lnz) p + lnz

and τ =

![image 165](<2012-kalugin-convergence-series-lambert-function_images/imageFile165.png>)

, (4.2)

then we recover the equation (1.4) originally given by de Bruijn for u and leading to the series (1.3). Thus the fundamental relation (1.4) is invariant with respect to p, with only the deﬁnitions of σ and τ being changed. This remarkable property is due to a similarity property of the solution (1.1) of the original transcendental equation yαey = x and explained by the following theorem.

- Theorem 22. An untransformed series solution of equation yαey = x and the corresponding transformed series for the Lambert W function, deﬁned by (4.2), are connected by relations


x = (αz)α, α = ep . (4.3)

Proof. The solution (1.1) of equation yαey = x possesses a similarity property with respect to parameter α > 0 in the sense [17]

Φα(x) = αΦ1

x1/α α

![image 166](<2012-kalugin-convergence-series-lambert-function_images/imageFile166.png>)

= αW

x1/α α

![image 167](<2012-kalugin-convergence-series-lambert-function_images/imageFile167.png>)

. (4.4)

It follows from (1.1) and (4.4) that

W

x1/α α

![image 168](<2012-kalugin-convergence-series-lambert-function_images/imageFile168.png>)

1 − τ σ

=

+ u , (4.5)

![image 169](<2012-kalugin-convergence-series-lambert-function_images/imageFile169.png>)

where σ and τ are deﬁned by (1.2). The right-hand side of (4.5) does not include α explicitly. On the other hand, α is included in the left-hand side through a combination z = x1/α/α. Therefore, the fundamental relation (1.4) will retain if we change variable x = (αz)α. Substituting this formula into (1.2) and introducing parameter p = lnα we obtain exactly equations (4.2) and the theorem follows.

![image 170](<2012-kalugin-convergence-series-lambert-function_images/imageFile170.png>)

![image 171](<2012-kalugin-convergence-series-lambert-function_images/imageFile171.png>)

![image 172](<2012-kalugin-convergence-series-lambert-function_images/imageFile172.png>)

![image 173](<2012-kalugin-convergence-series-lambert-function_images/imageFile173.png>)

Thus introducing the invariant parameter p generates an inﬁnite one-parameter family of series formed by replacement of variables τ and σ in the original series by expressions (4.2). Similar series for W are associated with an invariance observed in [17] and studied in [10].

We now consider the properties of the transformations (4.2) for z ∈ R. We shall start with p ∈ R and later consider brieﬂy one complex value of p. Both σ and τ are singular at zs = e−p, with the special case p = 0 recovering the previous observations regarding the singularities

- at z = 1. We note σ is monotonically decreasing on z > zs. For τ, we have τ(z0) = 0 at z0 = exp(zs − p), with τ positive for larger z and negative for smaller. Also we note that τ has a maximum at z = exp(ezs − p). In Figure 3, we plot σ and τ, deﬁned by (4.2), for diﬀerent values of p. We see that for all z > zs, σ decreases with increasing p, but τ increases. In view of the form of the double sums above it is not obvious whether convergence is increased or decreased as a result of these opposed changes. This is what we wish to investigate here.


| | | | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |


Figure 3: Dependence σ and τ on z for diﬀerent values of parameter p.

### 4.2 Domain of convergence

We wish to investigate ﬁrst the domains of z ∈ R for which the series (1.3) and (1.5) converge, and how the domains vary with p. We begin with theoretical results.

For p = 0 the domains of convergence are known from theorems 2 and 11. Speciﬁcally, the series (1.3) converges for z > e and the series (1.5) converges for z > z0 = 1.004458... (see Corollary 14). For arbitrary real p the following statement can be proved for the series (1.3).

- Theorem 23. The domain of convergence of the transformed series (1.3) is deﬁned by equations ℜW−1 −ep−1(p + lnz) > p − 1 and z > e−p , (4.6)


which is equivalent to

e1−2p, p ≤ 0 e−p+η

(4.7)

z > zp =

0cscη0, p > 0

where η0 ∈ (0, π) is the root of equation η0 cot η0 = 1 − p.

Proof. The proof of the theorem is similar to that of Theorem 2 and based on an application of Theorem 1 to the transformed series (1.3). In particular, substituting the expressions (4.2) in

- (2.1) we obtain in the real case, i.e. under assumption p+lnz > 0, the inequality (4.6). Applying


Lemma 1 to the latter we get (4.7), where zp > e−p, which justiﬁes the above assumption and the theorem follows.

![image 174](<2012-kalugin-convergence-series-lambert-function_images/imageFile174.png>)

![image 175](<2012-kalugin-convergence-series-lambert-function_images/imageFile175.png>)

![image 176](<2012-kalugin-convergence-series-lambert-function_images/imageFile176.png>)

![image 177](<2012-kalugin-convergence-series-lambert-function_images/imageFile177.png>)

- Remark 24. The formula (4.7) can be obtained by substituting equations (4.3) in (2.14).

However, in contrast to xα deﬁned by (2.14), zp is monotone decreasing with p. Thus, the larger p, the wider domain of convergence of the transformed series (1.3) (cf. Remark 4).

- Remark 25. In the formula (4.7), when p > 0 but p = 1, we can also write zp = e−p+(1−p)secη

0

.

- Remark 26. The convergence condition (4.6) can be extended to the case of complex z similar to the extension of the condition (2.16) for the untransformed series (1.3) by Theorem 8.


To ﬁnd out the domain of convergence of the transformed series (1.5) one should substitute

- (4.2) in (3.1) and solve the obtained equation for z as a function of p. As a result, we obtain formulae to compute zp similar to those stated in Theorem 13. We also can ﬁnd a very good approximation for zp for p < 1 using equation xα ≈ x1, stated in Remark 16, and Theorem 22. Speciﬁcally, substituting (4.3) in this equation we obtain


−p

zp ≈ e−p (z

)e

. (4.8) The accurate and approximate values of zp are depicted in Figure 4 by solid line and circles

0

respectively together with curve (4.7) (dashed line). It follows from Figure 4 as well as from (4.7)

- and (4.8) that with increase of parameter p the domain of convergence of the transformed series monotonely extends. To illustrate and qualitatively verify this result we design an appropriate numerical procedure. The method is simply to compute the partial sum of a series to a high number of terms, using extended ﬂoating-point precision as necessary, and then to plot the ratio of the partial sum to the exact value (the exact value is obtained using a built-in Maple function LambertW(k,x), where a method diﬀerent from series summation is used). The edge of the domain of convergence is then signaled by rapid oscillations and by marked deviations from the desired ratio of 1. (To make a graph be readable we depict only the relevant part of each curve.)


For the series (1.3) we have plotted in Figure 5 the partial sum to 40 terms for diﬀerent values of p. For p = 0, we see a nice illustration of Theorem 2, with the partial sum becoming unstable in the vicinity of z = e. For positive p, we see the domain of convergence increased and for negative p it is decreased, in accordance with Theorem 23. Similar eﬀects can be

Figure 4: Behavior of boundary of convergence domain as a function of p for series (1.3) (dashed line) and (1.5) (solid line) in real case.

seen for (1.5), we plot in Figure 6 the partial sums for 40 terms as p varies. The domain of convergence for each p is clearly seen, and conﬁrms that the point of divergence moves to larger z for decreasing p and to the left for increasing p. For p = 0 this point is very close to 1, which sharp demonstrates the result in Theorem 11.

We can summarize the above ﬁndings by noting that series (1.5) has a wider domain of convergence, and a better behaviour with p, while the domain of convergence for series (1.3) becomes worse in that order.

The fact that the domain of convergence of the transformed series is extending while the parameter p is increasing can also be found in the complex case based on the results of theorems 20 and 23. To make certain of this it is suﬃcient for the series (1.5), to substitute expressions (4.2) (with z ∈ C) into equation (3.1) and for the series (1.3), to consult Remark 26. The results are presented for p = −1, −1/2, 0, 1/2 and 1 in Figure 7 and Figure 8 for the series (1.3) and (1.5) respectively where the curves for p = 0 are the same as in Figure 2 and the points of intersection of the curves with the positive real axis correspond to points on the curves depicted in Figure 4.

### 4.3 Rate of convergence

By rate of convergence, we are referring to the accuracy obtained by partial sums of a series. Given two series, each summed to N terms, the series giving on average a closer approximation to the converged value is said to converge more quickly. The qualiﬁcation ‘on average’ is needed because it will be seen in the plots below that the error regarded as a function of z can show ﬁne structure which confuses the search for a general trend. Further, the comparison of rate of convergence between diﬀerent series can vary with z and p. For some ranges of z, one series will be best, while for other ranges of z a diﬀerent series will be best. Although one series may converge on a wider domain than another, there is no guarantee that the same series

| | | | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |


- Figure 5: For series (1.3), the ratio W(40)(z, p)/W(z) as functions of z for p = −1/2, 0, 1.


will converge more quickly on the part of the domain they have in common. The practical application of these series is to obtain rapid estimates for W using a small number of terms, and for this the quickest convergence is best, but this will be dependent on the domain of z.

The previous section showed that positive values of the parameter p extend the domain of convergence of the series, but its eﬀect on rate of convergence is diﬀerent. Figures 9 and 10 show the dependence on z of the accuracy of computations of the series (1.3) and (1.5) respectively with N = 10 for p = −1, −1/2, 0 and 1. One can see that the behaviour of the accuracy is non-monotone with respect to both z and p although some particular conclusions can be made. For example, one can observe that for the series (1.3) at least for z < 30 within the common domain of convergence the accuracy for p = −1/2, 0 and 1 is higher than for p = −1. For the

- series (1.5) an increase of positive values of p reduces a rate of convergence within the common domain of convergence i.e. for z > 1.5. However, at the same time for z > 11 computations with p = −1 are more accurate than those with positive p and for 5 < z < 18 the highest accuracy occurs when p = −1/2.


The next two ﬁgures 11 and 12 display the dependence of convergence properties of the series (1.3) and (1.5) respectively on parameter p for diﬀerent numbers of terms N = 10, 20 and 40. Again, the curves in these ﬁgures conﬁrm that the accuracy strongly depends on parameter p and is non-monotone and show that on the whole an increase of the number of terms improves the accuracy. It is also interesting that there exists a value of p for which the accuracy at the given point is maximum; this value depends very slightly on N and approximately is p ≈ −0.75 in Figure 11 and p ≈ −0.5 in Figure 12.

The explained behaviour of the accuracy depending on parameter p shows that introducing parameter p in the series can result in signiﬁcant changes in accuracy. The pointed out nonmonotone eﬀects of parameter p on a rate of convergence can be due to the aforementioned non-monotone behaviour of τ.

- Figure 6: For series (1.5), the ratio W(40)(z, p)/W(z) as functions of z for p = −1, 0, 1. Compared with Figure 5, this shows convergence down to smaller z.

- Figure 7: Domains of convergence of series (1.3) in complex z-plane for p = −1, −1/2, 0, 1/2 and 1.


## 5 Branch −1 and complex p

The above discussion has considered only real values for the parameter p. We brieﬂy shift our consideration to complex p and to branch −1. For z in the domain −1/e < z < 0 function W−1(z) takes real values in the range [−1, −∞). The general asymptotic expansion takes the form [8]

W−1(z) = ln(z) − 2πi − ln(ln(z) − 2πi) + u , (5.1)

- where u denotes the remaining terms similar to (1.1). This will clearly be very ineﬃcient for z ∈ [−1/e, 0) because each term in the series will be complex, and yet the series must sum to a real number. If, however, we utilize the parameter p, we can improve convergence enormously.


We again adopt the ansatz used above to write

p + ln(p + ln−1 z) p + ln−1 z

W−1(z) = [ln−1 z + p] − [p + ln(p + ln−1 z)] +

+ v , (5.2)

![image 178](<2012-kalugin-convergence-series-lambert-function_images/imageFile178.png>)

| | | | | |
|---|---|---|---|---|
| | | | | |


- Figure 8: Domains of convergence of series (1.5) in complex z-plane for p = −1, −1/2, 0, 1/2 and 1.

- Figure 9: For series (1.3) with N = 10, changes in accuracy in z for p = −1, −1/2, 0 and 1.


- where v stands for the remaining series which will not be pursued here. By setting p = iπ,


we can rewrite [ln−1 z + iπ] as ln(−z). When p = 0, (5.2) is equivalent to (5.1). A numerical comparison of partial sums can be used to show the improvement. Speciﬁcally, we compare the following ﬁrst terms in (5.1) and (5.2)

ln(ln(z) − 2πi) ln(z) − 2πi

W−(1)1 = ln(z) − 2πi − ln(ln(z) − 2πi) +

, (5.3)

![image 179](<2012-kalugin-convergence-series-lambert-function_images/imageFile179.png>)

ln(−ln(−z)) ln(−z)

Wˆ−1 = ln(−z) − ln(−ln(−z)) +

. (5.4)

![image 180](<2012-kalugin-convergence-series-lambert-function_images/imageFile180.png>)

The results are shown in Table 1 and graphically in Figure 13. One can see that both transformed (p = iπ) and untransformed (p = 0) series have an error that increases as z → −1/e. Although the maximum error occurs at z = −1/e + 0, the transformed series is exactly correct

- Figure 10: For series (1.5) with N = 10, changes in accuracy in z for p = −1, −1/2, 0 and 1.

- Figure 11: For series (1.3), the accuracy as a function of p at ﬁxed point z = 18 for N = 10, 20 and 40.


- Figure 12: For series (1.5), the accuracy as a function of p at ﬁxed point z = 9 for N = 10, 20 and 40.


![image 181](<2012-kalugin-convergence-series-lambert-function_images/imageFile181.png>)

![image 182](<2012-kalugin-convergence-series-lambert-function_images/imageFile182.png>)

![image 183](<2012-kalugin-convergence-series-lambert-function_images/imageFile183.png>)

z W−1(z) Wˆ−1(z) W−(1)1 (z) −0.01 −6.4728 −6.4640 −6.3210 − 0.04815i

![image 184](<2012-kalugin-convergence-series-lambert-function_images/imageFile184.png>)

![image 185](<2012-kalugin-convergence-series-lambert-function_images/imageFile185.png>)

![image 186](<2012-kalugin-convergence-series-lambert-function_images/imageFile186.png>)

![image 187](<2012-kalugin-convergence-series-lambert-function_images/imageFile187.png>)

- −0.1 −3.5772 −3.4988 −3.4124 − 0.3223i

![image 188](<2012-kalugin-convergence-series-lambert-function_images/imageFile188.png>)

![image 189](<2012-kalugin-convergence-series-lambert-function_images/imageFile189.png>)

![image 190](<2012-kalugin-convergence-series-lambert-function_images/imageFile190.png>)

- −0.2 −2.5426 −2.3810 −2.5182 − 0.5153i

![image 191](<2012-kalugin-convergence-series-lambert-function_images/imageFile191.png>)

![image 192](<2012-kalugin-convergence-series-lambert-function_images/imageFile192.png>)

![image 193](<2012-kalugin-convergence-series-lambert-function_images/imageFile193.png>)

- −0.3 −1.7813 −1.5438 −2.0087 − 0.6621i −1/e −1 −1 −1.7597 − 0.7450i


![image 194](<2012-kalugin-convergence-series-lambert-function_images/imageFile194.png>)

![image 195](<2012-kalugin-convergence-series-lambert-function_images/imageFile195.png>)

![image 196](<2012-kalugin-convergence-series-lambert-function_images/imageFile196.png>)

![image 197](<2012-kalugin-convergence-series-lambert-function_images/imageFile197.png>)

![image 198](<2012-kalugin-convergence-series-lambert-function_images/imageFile198.png>)

![image 199](<2012-kalugin-convergence-series-lambert-function_images/imageFile199.png>)

Table 1: Numerical comparison of series transformation with p = iπ.

- at z = −1/e. This is due to a diﬀerence in the local behaviour of W−1 and approximation Wˆ−1 when z → −1/e+0, particularly, the former has a square-root singularity, while Wˆ−1 is regular there. We also note that the transformed series is asymptotically correct as z → 0.


#### Figure 13: Errors in approximations (5.3) and (5.4) for W−1.

## 6 Series (1.6)

### 6.1 Diﬀerent representations

The series development (1.6) was obtained in [10, 9] and represents an expansion of W(x) in powers of σ−1 = lnx

∞

an(lnx)n (6.1) or

W(x) = ω0 +

n=1

∞

antn, (6.2)

W(et) = ω0 +

n=1

- where t = lnx and [9]


n−1

1 n!(1 + ω0)2n−1

an =

![image 200](<2012-kalugin-convergence-series-lambert-function_images/imageFile200.png>)

k=0

n − 1 k

(−1)kω0k+1. (6.3)

The formula (6.3) expresses the expansion coeﬃcients an in terms of the second-order Eulerian numbers [11, 10]. We now show that these coeﬃcients can also be represented through the unsigned associated Stirling numbers of the ﬁrst kind d(m, k) given by [7]

∞

vm m!

(−1)m+k d(m, k)

[ln(1 + v) − v]k = k!

![image 201](<2012-kalugin-convergence-series-lambert-function_images/imageFile201.png>)

m=2k

(6.4)

and the 2-associated Stirling numbers of the second kind used in the series (1.5). Both representations can be obtained on the basis of a relation [18]

W(et) + lnW(et) = t (6.5)

and the Lagrange Inversion Theorem [6]. To apply this theorem it is convenient to introduce a function that is zero at t = 0. We consider function

v = v(t) = W(et)/ω0 − 1 (6.6) and write (6.5) as

t = ω0 v + ln(1 + v). Then by the Lagrange Inversion Theorem we obtain

∞

v =

n=1

tn n

ln(1 + v) v

[vn−1] ω0 +

![image 202](<2012-kalugin-convergence-series-lambert-function_images/imageFile202.png>)

![image 203](<2012-kalugin-convergence-series-lambert-function_images/imageFile203.png>)

−n

(6.7)

where the operator [vp] represents the coeﬃcient of vp in a series expansion in v. Comparing (6.6),(6.2) and (6.7) leads to a formula for the coeﬃcients an, which after applying the binomial theorem becomes

ω0 n(1 + ω0)n

[vn−1]

an =

![image 204](<2012-kalugin-convergence-series-lambert-function_images/imageFile204.png>)

∞

(−1)k

k=0

n − 1 + k n − 1

[ln(1 + v) − v]k vk(1 + ω0)k

![image 205](<2012-kalugin-convergence-series-lambert-function_images/imageFile205.png>)

or by (6.4)

ω0 n!

an =

![image 206](<2012-kalugin-convergence-series-lambert-function_images/imageFile206.png>)

If instead of function (6.6) to take

n−1

(−1)n+k−1 d(n + k − 1, k) (1 + ω0)n+k

. (6.8)

![image 207](<2012-kalugin-convergence-series-lambert-function_images/imageFile207.png>)

k=0

h = h(t) = W(et) − ω0 − t (6.9) and apply the Lagrange Inversion Theorem to invert a relation

t = ω0(e−h − 1) − h coming from (6.5), then we ﬁnd in a similar way

n−1

1 n!

an =

![image 208](<2012-kalugin-convergence-series-lambert-function_images/imageFile208.png>)

k=0

(−1)k+1ω0k (1 + ω0)n+k

n + k − 1 k ≥2

. (6.10)

![image 209](<2012-kalugin-convergence-series-lambert-function_images/imageFile209.png>)

Finally, one more representation for the coeﬃcients an can be found in the following way. Let us consider a function

ψ = ψ(t) = W(et) − t (6.11) which is a simpliﬁed version of functions (6.6) and (6.9): now one does not need to provide the zero function value at t = 0 and here ψ(0) = ω0. Then it follows from (6.5) that

t = e−ψ − ψ. (6.12) This equation can also be obtained from the fundamental relation (1.4) by transformation

- u = ψ + lnt, σ = 1/t, τ = lnt/t which follow from (1.2). Diﬀerentiating (6.12) in t and excluding the term e−ψ from the result again using (6.12)


result in an initial value problem for ordinary diﬀerential equation

1 1 + t + ψ

dψ dt

. Searching a solution in the form of series

= −

![image 210](<2012-kalugin-convergence-series-lambert-function_images/imageFile210.png>)

![image 211](<2012-kalugin-convergence-series-lambert-function_images/imageFile211.png>)

ψ(t) = ω0 +

∞

cntn (6.13)

n=1

by substituting it into the diﬀerential equation and equating coeﬃcients of the same power in t one can ﬁnally ﬁnd

1 n(1 + ω0)

1 1 + ω0

, cn = −

c1 = −

![image 212](<2012-kalugin-convergence-series-lambert-function_images/imageFile212.png>)

![image 213](<2012-kalugin-convergence-series-lambert-function_images/imageFile213.png>)

(n − 1)cn−1 +

n−1

kckcn−k , n = 2, 3, 4, . . . (6.14a)

k=1

At length combining (6.13),(6.11) and (6.2) gives a1 = 1 + c1, an = cn for n ≥ 2. (6.14b)

In practice computing the expansion coeﬃcients in (6.1) using recurrence (6.14a) is faster and takes less digits to obtain a required level of accuracy than using either of (6.3), (6.8) or (6.10) which, however, being diﬀerent representations of the same expansion coeﬃcients, lead to some combinatorial relations considered in Section 7.

### 6.2 Convergence properties

The expansion (1.6) in fact represents a series of the Wright ω function [10, 9] ω(z) = WK(z)(ez), where K(z) = ⌈(ℑz − π)/(2π)⌉ is the unwinding number of z. The Wright ω function was introduced by Corless and Jeﬀrey [9] and studied in [27, 9]. When z = ξ ± iπ for ξ ≤ −1, ω = ω(z) satisﬁes equation f(z, ω) = 0 where f(z, ω) = ω + lnω − z (cf. (6.5)). Applying the same approach as in Section 3.1 to this equation one can obtain the same results as in [27, 10, 9]. Speciﬁcally, the nearest to the origin singularities are [10]

z1 = −1 − iπ and z2 = −1 + iπ. (6.15)

Note that they are connected with the singularities (3.6) of function u = uσ(τ), deﬁned by (1.4) or (3.27), through function (3.28) (cf. Remark 18)

z1 = s(σ, τ∗(1)) and z2 = s(σ, τ∗(0)). Thus the radius of convergence is √1 + π2 [10] and the domain of convergence is deﬁned by

![image 214](<2012-kalugin-convergence-series-lambert-function_images/imageFile214.png>)

1 √1 + π2

|σ| >

. (6.16)

![image 215](<2012-kalugin-convergence-series-lambert-function_images/imageFile215.png>)

![image 216](<2012-kalugin-convergence-series-lambert-function_images/imageFile216.png>)

The estimation of ω in the vicinity of the singularities (6.15) is [27, 9]

ω ∼ −1 − sgn(ℑzk)√2zk 1 −

z zk

![image 217](<2012-kalugin-convergence-series-lambert-function_images/imageFile217.png>)

![image 218](<2012-kalugin-convergence-series-lambert-function_images/imageFile218.png>)

- 1

![image 219](<2012-kalugin-convergence-series-lambert-function_images/imageFile219.png>)

- 2


as z → zk, (k = 1, 2)

As in Section 3.3, using the Darboux’s theorem one can ﬁnd the asymptotic expression for the expansion coeﬃcients in (6.1)

an ∼

2n − 1 2

(−1)n sin

arctanπ n32(1 + π2)

![image 220](<2012-kalugin-convergence-series-lambert-function_images/imageFile220.png>)

![image 221](<2012-kalugin-convergence-series-lambert-function_images/imageFile221.png>)

2 π

![image 222](<2012-kalugin-convergence-series-lambert-function_images/imageFile222.png>)

![image 223](<2012-kalugin-convergence-series-lambert-function_images/imageFile223.png>)

2n−1 4

![image 224](<2012-kalugin-convergence-series-lambert-function_images/imageFile224.png>)

![image 225](<2012-kalugin-convergence-series-lambert-function_images/imageFile225.png>)

as n → ∞. (6.17)

Thus, as in case of the series (1.5) for positive σ (see (3.20)), the expansion coeﬃcients in the

- series (1.6) disclose decaying oscillations in their behavior for large n.

In real case inequality (6.16) read as exp(−

√1 + π2) < x < exp(√1 + π2). Thus from the point of view of the domain of convergence the series (1.6) takes an intermediate place between the expansion of W(x) at the origin [8] W(x) = ∞n=1(−n)n−1xn/n!, which is valid for −e−1 < x < e−1, and the series (1.5) which is valid for x > x1 = 1.004458... (see Corollary 14). These three expansions put together cover the entire region of deﬁnition of W(x).

![image 226](<2012-kalugin-convergence-series-lambert-function_images/imageFile226.png>)

![image 227](<2012-kalugin-convergence-series-lambert-function_images/imageFile227.png>)

- 7 Combinatorial consequences


In this section we collect some combinatorial consequences resulting from the above obtained expressions for the expansion coeﬃcients.

Equating the right-hand sides of (3.18) and (3.33) one can ﬁnd

n

k=0

n k

(1 + λ)n−k−1λk =

n

k=1

n + k k ≥2

λk−1, (7.1a)

where summation in the right-hand side starts with one as n0

= 0 [11]. Setting µ = λ/(1−λ) in (7.1a) we also ﬁnd

≥2

n

k=0

n k

µk =

n

k=1

n + k k ≥2

µk−1(1 − µ)m−k. (7.1b)

The identities (7.1) were obtained by L.M. Smiley in a diﬀerent way in [24], where notation

{{}} was used instead of ≥2, and referred to as the Carlitz-Riordan identities [25]. Applying the binomial theorem to (7.1) leads to a pair of identities expressing the 2-associated Stirling numbers of the second kind through the second-order Eulerian numbers and inversely [24]

n

n + q q ≥2

=

p=0

n − p − 1 q − p − 1

n p

n

n + p + 1 p + 1 ≥2

n − p − 1 q − p

n q

(−1)q−p

=

p=0

Some estimates can also be obtained by comparing the found asymptotic formulas (3.20) and (3.21) with the explicit expressions for the expansion coeﬃcients in (1.5). For example, taking estimate (3.21) and the expansion coeﬃcients in (1.5) at σ = −2 we obtain

m−1

(m − 1)! 2√πm(2 ln2 − 1)m−

p + m − 1 p ≥2 ∼

as m → ∞ (7.2)

![image 228](<2012-kalugin-convergence-series-lambert-function_images/imageFile228.png>)

- 1

![image 229](<2012-kalugin-convergence-series-lambert-function_images/imageFile229.png>)

- 2


![image 230](<2012-kalugin-convergence-series-lambert-function_images/imageFile230.png>)

p=1

where the term with p = 0 is skipped (cf. (7.1a). This result is consistent with the formula given in [7, Ex.10(7), p.224].

Another consequence is obtained by taking the expansion coeﬃcients in (1.5) at σ = 0 together with (3.22)

m−1

p + m − 1 p ≥2

(−1)p+m−1

= (m − 1)! (7.3)

p=0

Further, comparing (6.3), (6.8) and (6.10) between one another we come to the following three identities

n−1

1 (1 + ω0)n−1

![image 231](<2012-kalugin-convergence-series-lambert-function_images/imageFile231.png>)

k=0

n − 1 k

(−1)kω0k =

n−1

(−1)n+k−1 d(n + k − 1, k) (1 + ω0)k

![image 232](<2012-kalugin-convergence-series-lambert-function_images/imageFile232.png>)

k=0

(7.4a)

n−1

1 (1 + ω0)n−1

![image 233](<2012-kalugin-convergence-series-lambert-function_images/imageFile233.png>)

k=0

n − 1 k

n−1

(−1)k+1ω0k+1 =

k=0

(−1)kω0k (1 + ω0)k

n + k − 1 k ≥2

![image 234](<2012-kalugin-convergence-series-lambert-function_images/imageFile234.png>)

(7.4b)

n−1

n−1

(−1)n+k d(n + k − 1, k) (1 + ω0)k

=

ω0

![image 235](<2012-kalugin-convergence-series-lambert-function_images/imageFile235.png>)

k=0

k=0

(−1)kω0k (1 + ω0)k

n + k − 1 k ≥2

![image 236](<2012-kalugin-convergence-series-lambert-function_images/imageFile236.png>)

(7.4c)

Finally, combining either of (6.3), (6.8) or (6.10) with (6.17) gives an asymptotic expression for the sum involved there.

Thus studying expansion series for W function we, on the way, derived the Carlitz-Riordan identities (7.1) as well as found a formula for an alternating sum of 2-associated Stirling numbers of the second kind (7.3) and conﬁrmed the asymptotic formula (7.2) for summation of the same numbers without the alternating factor. We also found formulas (7.4) where the Omega constant ω0 plays a role of a ‘magic’ number which connects sums involving the second-order Eulerian numbers, the associated Stirling numbers of the ﬁrst kind and the 2-associated Stirling numbers of the second kind.

## 8 Concluding remarks

We ascertained the domain of convergence of the series (1.3) and (1.5) in real and complex cases and found that the series (1.5) has a much wider domain of convergence than that of the series (1.3) in both cases and provided an analysis of this fact in real case. We found asymptotic expressions for the expansion coeﬃcients and obtained a representation of the series (1.5) in terms of the second-order Eulerian numbers.

We considered an invariant transformation deﬁned by the parameter p and applied it to the above series. We studied an eﬀect of parameter p on the convergence properties of the transformed series theoretically and numerically and found that an increase of p results in an extension of the domain of convergence of the series. Thus the series obtained under the transformation with positive values of p have a wider domain of convergence than the original series does. However, at the same time a rate of convergence can be found to be reduced when the parameter p increases. Therefore in such a case within the common domain of convergence of the series with diﬀerent positive values of p the series with the minimum value of p would be the most eﬀective.

We also considered the well-known expansion of W(x) in powers of lnx and gave an asymptotic estimate for the expansion coeﬃcients. We found three more forms for a representation of the expansion coeﬃcients of the series in terms of the associated Stirling numbers of the ﬁrst kind (6.8), the 2-associated Stirling subset numbers (6.10) and iterative formulas (6.14). Finally we presented some combinatorial consequences, including the Carlitz-Riordan identities, which result from the found diﬀerent forms of the expansion coeﬃcients of the above series.

## References

- [1] M. Abramowitz and I.A. Stegan, Handbook of mathematical functions with formulas, graphs amd mathematical tables, 9th printing, U.S. Department of Commerce, National Bureau of Standards, Applied Mathematics 55, 1970, 24.1.3 (III), p. 824.


- [2] K. Adachi, Several Complex Variables and Integral Formulas, World Scientiﬁc, Singapore, 2007.
- [3] M.Ya. Antimirov, A.A. Kolyshkin, and R. Vaillancourt, Complex Variables, Academic Press, 1998.
- [4] E.A. Bender, Asymptotic methods in enumeration, SIAM Review, 16, No.4, 1974, 485-515.
- [5] N.G. de Bruijn, Asymptotic Methods in Analysis, North-Holland, 1961.
- [6] C. Carath´eodory, Theory of Functions of a Complex Variable, Chelsea, 1954.
- [7] L. Comtet, C. R. Acad. Sc., Paris, 270, 1970, 1085-1088.
- [8] R.M. Corless, G.H. Gonnet, D.E.G. Hare, D.J. Jeﬀrey, and D.E. Knuth, On the Lambert W Function, Advances in Computational Mathematics, Vol. 5, 1996, 329-359.
- [9] R.M. Corless and D.J. Jeﬀrey, The Wright w function, AISC-Calculemus 2002, Eds: J. Calmet et al., LNAI 2385, Springer-Verlag, 2002, 76-89.
- [10] R.M. Corless, D.J. Jeﬀrey, and D.E. Knuth, A Sequence of Series for The Lambert W Function, In Proceedings of the ACM ISSAC, Maui, 1997, 195-203.
- [11] R.L. Graham, D.E. Knuth, and O. Patashnik, Concrete Mathematics, Addison-Wesley, 1994.
- [12] G.H. Hardy, Divergent series, Oxford University Press, London, 1949.
- [13] P. Henrici, Applied and Computational Complex Analysis, Vol.1, 1974, John Wiley & Sons, New York.
- [14] C. Hunter, Oscillations in the Coeﬃcients of Power Series, SIAM Journal on Applied Mathematics, Vol.47, No.3, 483-497.
- [15] C. Hunter and B. Guerrieri, Deducing the Properties of Singularities of Functions From Their Taylor Series Coeﬃcients, SIAM J. Appl. Math., Vol. 39, No. 2, 1980, 248-263, URL: http://www.jstor.org/stable/2101048.
- [16] A.J.E.M. Janssen and J.S.H. van Leeuwaarden, Some remarks on Φα(x), Private communication, November, 2007.
- [17] D.J. Jeﬀrey, R.M. Corless, D.E.G. Hare, and D.E. Knuth, Sur l’inversion de yaey au moyen des nombres de Stirling associes, C. R. Acad. Sc., Paris, 320, 1995, 1449-1452.
- [18] D.J. Jeﬀrey, D.E.G. Hare, and R.M. Corless, Unwinding the branches of the Lambert W function, Mathematical Scientist, 21, 1996, 1-7.
- [19] G.A. Kalugin and D.J. Jeﬀrey, Series Transformations to Improve and Extend Convergence, CASC 2010, Eds. V.P.Gerdt et al., LNCS 6244, 2010, 134-147.


- [20] B.V. Limaye and M. Zeltser, On the Pringsheim convergence of double series, Proceedings of the Estonian Academy of Sciences, 58, 2, 2009, 108-121.
- [21] A.I. Markushevich, Theory of functions of a complex variable, Vol.II, Prentice-Hall, Inc., Englewood Cliﬀs, N.J., 1965.
- [22] P.M. Morse and H.Feshbach, Methods of theoretical physics, Part I, McGraw-Hill Book Company, Inc., 1953.
- [23] P. Savick´y and A.R. Woods, The number of Boolean functions computed by formulas of a given size, Proceedings of the 8th Int. Conf. Random Structures and Algorithms, Vol. 13, Issue 3-4,1998, 349-382.
- [24] L.M. Smiley, Completion of a Rational Function Sequence of Carlitz, eprint arXiv:math/0006106, available on web site http://www.math.uaa.alaska.edu/ ∼smiley/cscarx.pdf, 2000, 8 pages.
- [25] L.M. Smiley, Carlitz-Riordan Identities, Web site http://www.math.uaa.alaska.edu/ ∼smiley/stir2eul2.html,Last modiﬁed: Wed Nov 21 03:23:23 AKST 2001.
- [26] E.C. Titchmarsh, Theory of functions, 2nd ed., Oxford, 1939.
- [27] E.M. Wright, Solution of the equation zez=a, Bull. Amer. Math. Soc., 65, 1959, 89-93.


