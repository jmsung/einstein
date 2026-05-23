# arXiv:2207.10587v1[math.CA]21Jul2022

## EXISTENCE OF EXTREMALS FOR A FOURIER RESTRICTION INEQUALITY ON THE ONE–SHEETED HYPERBOLOID

RENE´ QUILODRAN´

Abstract. We prove the existence of functions that extremize the endpoint L2 to L4 adjoint Fourier restriction inequality on the one-sheeted hyperboloid in Euclidean space 4 and that, taking symmetries into consideration, any extremizing sequence has a subsequence that converges to an extremizer.

Contents

- 1. Introduction ................................................ 1
- 2. Lorentz invariance, symmetrization and caps ................ 8
- 3. Calculation of a double convolution ......................... 13
- 4. Comparison with the cone .................................. 19
- 5. The upper half of the one-sheeted hyperboloid .............. 21
- 6. The full one-sheeted hyperboloid............................ 25
- 7. The Tomas–Stein inequality for S2 and reﬁnements.......... 25
- 8. Lifting to the hyperboloid the inequality for the sphere...... 30
- 9. A concentration-compactness lemma ........................ 39
- 10. Bilinear estimates and discarding dichotomy ............... 40
- 11. Dyadic reﬁnements and discarding vanishing ............... 42
- 12. Convergence to the cone ................................... 44
- 13. Proof of Theorem 1.3 ...................................... 49
- 14. Scaling .................................................... 53 Appendix A. Computation of a limit........................... 54 Acknowledgments............................................... 61 References ...................................................... 61


1. Introduction

In seminal paper [37] R. Strichartz addressed the adjoint restriction problem of the Fourier transform to d − 1 dimensional quadric submanifolds of Euclidean space

d, establishing the necessary and suﬃcient conditions on p such that an L2 → Lp estimate holds. Recently, there has been interest in studying the existence of extremizers and the sharp L2 → Lp estimates for adjoint Fourier restriction operators and progress has been made in the case of quadric curves and surfaces: the paraboloid

Date: July, 2022. 2010 Mathematics Subject Classiﬁcation. 42B10, 42B37, 51M16. Key words and phrases. Sharp Fourier Restriction Theory, maximizers, convolution of singular

measures.

1

and parabola [15,20], the cone [1,15,34], the sphere and circle [3,4,9,16,18,30,36], the two-sheeted hyperboloid and hyperbola [6,7,33] and the saddle [5,12]. The study of such sharp L2 to Lp estimates is intimately related to the study of extremizers and sharp constants for Strichartz estimates for classical partial diﬀerential equations, such as the Schro¨dinger, hyperbolic Schro¨dinger, wave and Klein–Gordon equations. In this note we address the case of the one-sheeted hyperboloid in 4, which is related to the so called Klein–Gordon equation with imaginary mass.

Let H3 denote the upper half of the three dimensional one-sheeted hyperboloid in 4,

H3 = (x, |x|2 − 1): x ∈ 3, |x| 1 , equipped with the measure µ with density {|x|>1}(x)δ t − |x|2 − 1 √ dtdx

, deﬁned by duality as

|x|2−1

dy |y|2 − 1

g(y, |y|2 − 1)

g(x,t)dµ(x,t) =

(1.1)

{y∈ 3:|y|>1}

H3

for all g ∈ S( 4).

A function f : H3 → can be identiﬁed with a function from 3 to , using the orthogonal projection from1 H3 to 3 × {0}, and in what follows we do so. We denote the Lp(H3,µ) norm of a function f on H3 by f Lp(H3), f Lp(µ) or simply

f Lp, f p if it is clear from context.

The Fourier extension operator on the hyperboloid H3, also known as the adjoint Fourier restriction operator, is given by

√

dy |y|2 − 1

|y|2−1f(y, |y|2 − 1)

eix·yeit

Tf(x,t) =

, (1.2)

{y∈ 3:|y|>1}

where (x,t) ∈ 3 × and f ∈ S( 4). Note that Tf(x,t) = fµ(−x,−t), with the Fourier transform in 4 deﬁned by gˆ(x,t) =

e−i(x·y+ts)g(y,s)dy ds.

4

Strichartz proved in [37] that for all 103 p 4 there exists Cp < ∞ such that for all f ∈ L2(H3) the following estimate for Tf holds

Tf Lp( 4) Hp f L2(H3), (1.3) where Hp < ∞ denotes the best constant in (1.3),

Tf Lp( 4) f L2(H3)

Hp = sup

. (1.4)

0 =f∈L2(H3)

The (full) one-sheeted hyperboloid is deﬁned by H3 := {(x,t) ∈ 3 × : t2 = |x|2 − 1, |x| 1},

1Strictly speaking, it is identiﬁed with a function with domain {x ∈ 4: |x| 1} but we will ignore this minor point and, whenever necessary, it will be understood that f is extended to be equal to zero inside the unit ball. We could have chosen to write our operator as acting on a weighted L2 space of Euclidean space, but we will take this geometric point of view instead.

and we endow it with the Lorentz invariant measure µ¯ with density d¯µ(x,t) = {|x|>1} δ t − |x|2 − 1

dtdx |x|2 − 1

dtdx |x|2 − 1

+ {|x|>1} δ t + |x|2 − 1

=: dµ+(x,t) + dµ−(x,t).

Here µ+ equals µ as in (1.1), and µ− equals the reﬂection of µ via the reﬂection map (x,t)  → (−x,−t). The adjoint Fourier restriction operator on H3 is

ei(x·y+ts)f(y,s)d¯µ(y,s)

Tf(x,t) = fµ¯(−x,−t) =

H3

√

dy |y|2 − 1

|y|2−1f+(y)

eix·yeit

=

(1.5)

{y∈ 3:|y|>1}

√

dy |y|2 − 1

|y|2−1f−(y)

eix·ye−it

,

+

{y∈ 3:|y|>1}

where f = f+ +f−, the function f+ is supported on the upper half of the one-sheeted hyperboloid, H3, and the function f−, on the lower half, −H3, and we have identiﬁed their domains with 3 via the orthogonal projection as stated before. We see that Tf(x,t) = Tf+(x,t) + Tf−(x,−t).

The triangle inequality and (1.3) imply that for 103 p 4 the following estimate holds

2(H3), (1.6) where Hp < ∞ is the sharp constant

Tf Lp( 4) Hp f L

Tf Lp( 4) f L

. (1.7)

Hp = sup

2(H3)

0 =f∈L2(H3)

The Lorentz group on 4, denoted L, preserves H3, µ¯, and acts on functions on H3 by composition: L∗f(x,t) := f(L(x,t)), L ∈ L (see Section 2 for more details). In particular, we have f L

q(H3) and Tf Lp( 4) = T(L∗f) Lp( 4), for all p,q ∈ [1,∞].

q(H3) = L∗f L

Deﬁnition 1.1. An extremizer (or maximizer) for (1.3) is a function 0 = f ∈ L2(H3) that satisﬁes Tf Lp( 4) = Hp f L2(H3). An L2-normalized extremizing sequence for (1.3) {fn}n ⊂ L2(H3) is such that fn L2(H3) = 1 and Tfn Lp( 4) → Hp, as n → ∞. A corresponding deﬁnition holds for extremizers and extremizing sequences for (1.6).

This paper is devoted to the study of the sharp instances of (1.3) and (1.6) in the endpoint case p = 4, that is, the inequalities

- Tf L4( 4) H4 f L2(H3), (1.8)

- Tg L4( 4) H4 g L


2(H3), (1.9) and our main results concern the existence of extremizers as well as the precompactness of extremizing sequences. The statements of the main results of this paper are as follows.

- Theorem 1.2. There exists an extremizer in L2(H3) for inequality (1.8). Moreover, for every L2-normalized complex valued extremizing sequence {fn}n for

(1.8), there exist a subsequence {fn

k}k and a sequence {(xk,tk)}k ⊂ 4 such that {eix

k·yeit

k

√

|y|2−1fn

k}k is convergent in L2(H3).

- Theorem 1.3. There exists an extremizer in L2(H3) for inequality (1.9). Moreover, for every L2-normalized complex valued extremizing sequence {fn}n for (1.9), there


k}k and sequences {ξk}k ⊂ 4 and {Lk}k ⊂ L such that {eiξ

exist a subsequence {fn

k}k is convergent in L2(H3). In the statement of the theorems we are writing eix

k·ξL∗kfn

√

|y|2−1fn

k·yeit

for the function y  → eix

k

√

k

|y|2−1fn

k·yeit

k·ξfn

k·ξL∗kfn

for the function ξ  → eiξ

(y) and eiξ

(Lkξ).

k

k

k

k

Remark 1.4. Note the qualitative diﬀerence regarding existence of extremizers between the one-sheeted hyperboloid and the two-sheeted hyperboloid (or its upper sheet) equipped with its Lorentz invariant measure, which are deﬁned respectively by

dtdx |x|2 + 1

{(x,t) ∈ 4 × : t2 = |x|2 + 1}, δ(t − |x|2 + 1) + δ(t + |x|2 + 1)

,

both of which can be considered as ”perturbations” of the cone. It was shown in [33] that for the L2 to L4( 4) inequality on the two-sheeted hyperboloid and on its upper sheet, extremizers do not exist and the best constant was calculated explicitly. On the other hand, for the L2 to L4( 4) inequality on the cone, extremizers exist, their exact form was obtained and the best constant was calculated (see [1]).

We note that the results in [14] do not apply to the case of the hyperboloid due to the lack of scale invariance, but information can be obtained from the arguments therein, although we will not go that route. See the discussion in [33, Section 2] for some details in the related context of the two-sheeted hyperboloid.

We take this opportunity to indicate a correction to [33, Theorem 1.2 & Proposition 7.5], where the best constant for the two-sheeted hyperboloid in 2 in the L2 → L6 adjoint Fourier restriction inequality, there denoted H¯ 2,6, is incorrect. Details can be found in version 3 of [33] available at www.arxiv.org.

The convolution form of inequalities (1.8) and (1.9), obtained via Plancherel’s theorem, tells us that in both cases, H3 and H3, there exist nonnegative real valued extremizers, and the symmetrization method used in [16], or the one in [29], can be adapted to show that if a function f is a nonnegative real valued extremizer for T on H3 then f is necessarily an even function: f(x,t) = f(−x,−t), for µ¯-a.e. (x,t) ∈ H3. We discuss the details in Section 2.

It would be of interest to treat the endpoint p = 103 as well, and more generally to study the existence of extremizers at the endpoint and non-endpoint cases for all2

2When d = 1 the one-sheeted hyperboloid coincides with the two-sheeted hyperboloid after a 90◦ rotation, and the later has been studied in [6]. They consider only one of the two branches but it is not diﬃcult to see that the existence argument in the non-endpoint case carries through to the two

d 2, as was recently done for non-endpoint cases of the two-sheeted hyperboloid in [6, 7]. Our analysis here extends the known results on sharp Fourier extension inequalities for quadric manifolds as studied in Strichartz paper [37].

- 1.1. Organization of the paper and outline of the proofs of the main theorems. From now on, references to the sharp inequalities (1.3) and (1.6) are understood with p = 4, unless it is explicitly said otherwise.


An important tool in our proofs is [13, Proposition 1.1] which we include next for the convenience of the reader. Proposition 1.5. Let be a Hilbert space and S : → Lp( d) be a continuous linear operator, for some p ∈ (2,∞). Let {fn}n ⊂ be such that:

- (i) fn = 1,
- (ii) lim

n→∞

Sfn Lp( d) = S →Lp( d),

- (iii) fn f and f = 0,
- (iv) Sfn → Sf a.e. in d.


Then fn → f in . In particular, f = 1 and Sf Lp( d) = S →Lp( d).

To prove Theorem 1.2 we apply Proposition 1.5 with p = d = 4, equals to L2(H3) and S equals T. We need to verify (iii) and (iv), as (i) and (ii) are immediate for a normalized extremizing sequence. We handle (iv) as in [32, Prop. 8.3], [14]. To prove (iii) we will see that the only way it can fail, the failure being that a weak limiting function equals zero, is that the extremizing sequence concentrates at inﬁnity, which is deﬁned as follows for H3, with an analogous deﬁnition for H3.

Deﬁnition 1.6. We say that the sequence {fn}n ⊂ L2(H3) concentrates at inﬁnity if

fn L2(H3) > 0 and for every ε,R > 0 there exists N ∈ such that for all n N

- inf


n

fn {|y| R} L2(H3) < ε, where, as mentioned before, we are identifying a function on H3 with a function on {y ∈ 3 : |y| 1}.

Finally, to discard the possibility of concentration at inﬁnity we will use a comparison argument with the cone.

In the case of the full one-sheeted hyperboloid H3 there is the addition of Lorentz invariance, and our proof will require additional steps when compared to the case of the upper half, H3. Because of this, in addition to the use of Proposition 1.5 and a comparison to the double cone, we will use a concentration-compactness argument to be able to discard concentration at inﬁnity.

More in detail, the organization of the paper is as follows. In Section 3 we explicitly calculate the double convolution µ ∗ µ which we use in Section 4 to prove the strict lower bounds

3 2

1/4

(2π)5/4, (1.10)

H4 > (2π)5/4, H4 >

branches. On the other hand, an argument is needed to settle the endpoint p = 6 for two branches (this is also the case when d = 2 and p = 6 as clariﬁed in the correction to [33] alluded to before).

which tell us that the best constant for the adjoint Fourier restriction operator on the (resp. full) one-sheeted hyperboloid is strictly greater than that for the (resp. double) cone.

In Section 5 we prove Theorem 1.2 by collecting the necessary ingredients to use

- Proposition 1.5. Here the ﬁrst inequality in (1.10) is used to show that the L2 mass of an extremizing sequence can not tend to inﬁnity (i.e. there is no concentration at inﬁnity).


From Section 6 onward we focus on the full one-sheeted hyperboloid H3. The existence of Lorentz invariance adds complexity to the proof of Theorem 1.3, compared to the much simpler proof of Theorem 1.2. We will use a concentration-compactness type argument that we discuss in Section 9. In short, given an L2 normalized extremizing sequence {fn}n for T, three possibilities hold (possibly after passing to a further subsequence): compactness, vanishing or dichotomy. In Section 10 we prove bilinear estimates at dyadic scales and show that they imply that dichotomy can not occur. In Section 11 we obtain a dyadic reﬁnement of (1.6) and used it to show that vanishing can not occur.

To treat the compactness case, it will be necessary to study so called ”cap bounds” or reﬁnements of the L2 → L4 estimate for the adjoint Fourier restriction operators T and T and this we achieve in Section 8 by ”lifting” to the hyperboloid the results for the sphere in 3, as proved in [9], and recalled in Section 7.

In Section 13 we show that if an extremizing sequence satisﬁes compactness and does not concentrate at inﬁnity then it is precompact in L2(H3), modulo multiplication by characters and composition with Lorentz transformations.

Finally, in Section 12 we study some limiting relationships between the hyperboloid and the cone. The results of this section together with the second strict inequality

- in (1.10) are used to show that, in the case of H3, the L2 mass of an extremizing sequence satisfying compactness does not tend to inﬁnity. When this is done, the proof of Theorem 1.3 is complete.


## 1.2. Notation and some deﬁnitions. The set of natural numbers is

= {0,1,2,...} and ∗ = {1,2,3,...}. For s > 0, we let Hs3 := {(x,t): x ∈ 3, t = |x|2 − s2}, equipped with the

measure

dµs(x,t) = {|x|>s} δ t − |x|2 − s2

dxdt |x|2 − s2

, (1.11)

and adjoint Fourier restriction operator Ts, Tsf(x,t) = fµs(−x,−t). There are corresponding deﬁnitions of H3s, µ¯s and Ts in analogy with the case s = 1.

The cone in 3 is denoted Γ3 := {(y,|y|) : y ∈ 3} which comes with its Lorentz and scale invariant measure σc,

f dσc =

Γ3

dy |y|

f(y,|y|)

.

3

### The adjoint Fourier restriction operator on the cone, Tc, is given by the expression Tcf(x,t) =

dy |y|

eix·yeit|y|f(y)

. (1.12)

3

which acts, a priori, on functions f ∈ S( 3). The adjoint Fourier restriction operator on the double cone, Γ3 := Γ3 ∪ −Γ3, denoted by Tc, is given by the expression

dy |y|

dy |y|

eix·yeit|y|f(y,|y|)

eix·ye−it|y|f(y,−|y|)

Tcf(x,t) =

+

, (1.13)

3

3

f ∈ S( 4). We let C4,C4 < ∞ denote the best constants in the inequalities Tcf L4( 4) C4 f L2(Γ3), Tcf L4( 4) C4 f L

2(Γ3), respectively. We sometimes use the alternative notation T = H4, T = H4, Tc = C4 and Tc = C4.

The sphere of radius r > 0 on 3 is S2r := {y ∈ 3 : |y| = r}. The sphere of radius 1 is denoted simply S2. On S2r we consider the measure σr,

f dσr =

f(rω)r dσ(ω), (1.14)

S2r

S2

where σ is the surface measure on S2. With this choice, σr(S2r) = rσ(S2), for all r > 0. For r > 0 and a function f : 3 → C we set fr : S2 → by fr(·) = f(r ·).

We let S denote the best constant in the convolution form of the Tomas–Stein inequality for the sphere S2,

fσ ∗ fσ L2( 3) S2 f 2L2(S2).

We also use the following convention. For f : H3 → we write f = f++f−, where f+ is supported on H3 and f− on the reﬂection of H3 with respect to the origin, −H3, and we further identify their domains with 3 via the orthogonal projection. For A ⊆ 3 we deﬁne

f dµ, f ∈ L1(H3), while for H3,

f dµ :=

{(x,t)∈H3 : x∈A}

A

f d¯µ,

fdµ¯ :=

{(x,t)∈H3 : x∈A}

A

f ∈ L1(H3), so that in both cases the integral over A ⊂ 3 equals to the integral over the ”lift” of A to H3 or H3, as it corresponds.

An element R ∈ SO(4) that preserves the t-axis, R(0,0,0,1) = (0,0,0,1), is canonically identiﬁed with an element of SO(3), and as such we will just write R ∈ SO(3).

We let ψs(r) = √r2 − s2 {r s}, φs(t) = ψs−1(t) = √t2 + s2 {t 0}. The (closed) ball of radius r > 0 centered at y ∈ 3 is B(y,r). For a set A, A denotes the characteristic function of A and A , the complement of A with respect to a set containing A that will be understood from context, usually 3, H3 or H3. We sometimes slightly abuse

notation and use |A| to denote the measure of a set A, where the measure used must be understood from context, for instance, if A is an interval it refers to the Lebesgue measure, if A ⊆ S2, it refers to the surface measure, etc. The support of a function f is denoted supp(f).

We will use the usual asymptotic notation X Y, Y X if there exists a constant C (independent of X,Y ) such that |X| CY ; we use X Y if X Y and Y X; when such constants depend on parameters of the problem that we want to make explicit, such as α,... etc., we write α,..., α,... and α,.... At times we will use the common asymptotic notation o(·) and O(·). Thus, gn = o(fn) if gn/fn → 0 as n → ∞, while gn = O(fn) if |gn| C|fn| for all n. If there is more than one parameter, say n ∈ and s > 0, then gn(s) = on(fs(s)) means the limit of gn/fn → 0 is taken with respect to n and is uniform in s, that is sups |gn(s)|/|fn(s)| → 0 as n → ∞.

2. Lorentz invariance, symmetrization and caps

- 2.1. Lorentz invariance. Recall that the Lorentz group on 4, denoted L, is deﬁned as the group of invertible linear transformations in 4 that preserve the bilinear form

B(x,y) = x4y4 − x3y3 − x2y2 − x1y1, for x = (x1,x2,x3,x4) ∈ 4 and y = (y1,y2,y3,y4) ∈ 4. If L ∈ L then |detL| = 1. Given that we can write H3 = {(x,t) ∈ 3+1: B((x,t),(x,t)) = −1} it is direct that L preserves the hyperboloid: L(H3) = H3, for every L ∈ L. Moreover, L preserves the measure µ¯, in the sense that for every f ∈ L1(H3) and L ∈ L

H3

f(x,t)d¯µ(x,t) =

H3

f(L(x,t))d¯µ(x,t). (2.1) To see this note that a simple calculation shows that we can write

µ¯(x,t) = δ t2 − |x|2 + 1 dxdt so that

4

f(x,t)d¯µ(x,t) =

4

f(x,t)δ t2 − |x|2 + 1 dtdx.

Then, if L is a Lorentz transformation and f ∈ L1(H3), (2.1) can be seen to hold by the change of variable formula.

For t ∈ (−1,1) the Lorentz boost Lt ∈ L is the linear map

Lt(ξ1,ξ2,ξ3,τ) =

ξ1 + tτ √1 − t2

,ξ2,ξ3,

tξ1 + τ √1 − t2

, (2.2)

while Lt denotes the rescaling Lt := (1 − t2)1/2Lt, so that (Lt)−1 = (1 − t2)−1/2L−t.

- 2.2. Convolution form. With the Fourier transform in d normalized as F(x) =


- d
- e−ix·yF(y)dy we have the identities F ∗ G = F G, F L2( d) = (2π)d/2 F L2( d),


so that using Tf(x,t) = fµ(−x,−t) and Tg(x,t) = gµ¯(−x,−t) we ﬁnd the equalities Tf L4( 4) = 2π fµ ∗ fµ 1L/22( 4), Tg L4( 4) = 2π gµ¯ ∗ gµ¯ 1L/22( 4). (2.3) Using this convolution form of the L4 norm and the triangle inequality we see that

Tf L4( 4) T|f| L4( 4) and Tg L4( 4) T|g| L4( 4), so that if f is an extremizer for (1.3) (resp. g for (1.6)), then so is |f| (resp. |g|), showing that if extremizers exist then there are nonnegative real valued extremizers.

- 2.3. Symmetrization. Let f ∈ L2(H3) be a complex valued function. Denote the reﬂection of f by f(x,t) = f(−x,−t) and the nonnegative L2-symmetrization of f by


1/2

f (x,t) = |f(x,t)|2 + |f(−x,−t)|2 2

. Regarding the relationship between f and f we have the following lemma.

- Lemma 2.1. Let f ∈ L2(H3) be a complex valued function. Then fµ¯ ∗ fµ¯ L2( 4) f µ ¯ ∗ f µ ¯ L2( 4). (2.4)


Proof. As in [16, Proof of Prop. 3.2] we write fµ¯ ∗ fµ¯(ξ,τ) = f(y,s)f(−x,−t)δ (ξ,τ) − (y,s) − (x,t) d¯µ(y,s)d¯µ(x,t)

- 1

- 2


(f(y,s)f(−x,−t) + f(−y,−s)f(x,t))

=

· δ (ξ,τ) − (y,s) − (x,t) d¯µ(y,s)d¯µ(x,t), and apply the Cauchy-Schwarz inequality

|f(y,s)f(−x,−t) + f(−y,−s)f(x,t)| 2f (y,s)f (x,t) to obtain that for all (ξ,τ) ∈ 4

|fµ¯ ∗ fµ¯(ξ,τ)| f µ ¯ ∗ f µ ¯(ξ,τ). Then

fµ¯ ∗ fµ¯ L4( 4) = fµ¯ ∗ fµ¯ L4( 4) f µ ¯ ∗ f µ ¯ L4( 4).

Since we also have

f L2(¯µ) = f L2(¯µ),

it follows that there exist real valued extremizers for T which are nonnegative even functions on H3. Moreover, any nonnegative real valued extremizer is necessarily even. This can be explained by studying the cases of equality in (2.4) by following the proof of the inequality (see [4] for a detailed discussion in the case of the sphere) or, alternatively, by using the same method as in the proof of [29, Lemma 6.1] where a diﬀerent approach to symmetrization is used and the cases of equality were studied. Therefore, we have the following result.

- Proposition 2.2. Let f ∈ L2(H3) be a nonnegative real valued extremizer for (1.6), then f(x,t) = f(−x,−t) for µ¯-a.e. (x,t) ∈ H3.


There are some interesting problems that we do not address in this article:

- (i) the nonnegativity of all real valued extremizers,
- (ii) the relationship between complex and real valued extremizers,
- (iii) the smoothness of extremizers.


We provide the following comments in the context of the L2(Sd−1) → Lp( d) adjoint Fourier restriction inequality on the sphere. Christ and Shao [10] showed that for the case of the the sphere S2 in 3 and p = 4 each complex valued extremizer is of the form ceix·ξF(x), for some ξ ∈ 3, some c ∈ C and some nonnegative extremizer F, and that extremizers are of class C∞; this results were later expanded to all dimensions d 2 and even integers p in [30, Lemma 2.2 and Theorem 1.2] and [31]. Note that the answer obtained for (ii) resolves (i). By using the outline in [10,30,31], the Euler–Lagrange equation, which can be obtained as in [8], and the results in [2] we expect similar relationships for the case of H3 and H3, but have not investigated the extent to which the arguments would need to be changed.

A related question is that of the rate of decay at inﬁnity of an extremizer for which the argument in [19] gives a possible route; see also [29].

We remark that Theorems 1.2 and 1.3 are stated for general (possibly complex valued) extremizing sequences, that is, we do not assume nonnegativity and/or symmetry.

- 2.4. Caps. A (closed) spherical cap C ⊆ S2 is a set of the form C = {x ∈ S2: |x − x0| t} for some x0 ∈ S2 and t > 0. If we want to be explicit about the dependence on x0 and t we write C(x0,t).


A cap C of Hs3 is a set of the form C = {(rω,

√

r2 − s2) : r ∈ [a,b], ω ∈ C}, (2.5)

where s a < b ∞ and C ⊆ S2 is a spherical cap. When a = s2k and b = s2k+1 for some k ∈ we say that C is a dyadic cap. We identify a cap C as before with its orthogonal projection to 3 × {0}, and moreover we use spherical coordinates and write the cap in (2.5) as C = [a,b] × C, where the hyperboloid it belongs to will be

understood from context. A cap C of H3s is such that either C ⊆ Hs3 or its reﬂection with respect to the origin (−C) ⊆ Hs3 is a cap on Hs3.

The µs-measure of a cap is easily calculated µs(C) =

√

√

b

r2 √r2 − s2

σ(C) 2

b a

s2 ln r +

r2 − s2 + r

r2 − s2

.

dµs = σ(C)

dr =

C

a

(2.6) For a cap C = [a,b] × C in Hs3 and t > 0 we deﬁne the rescaled cap tC = [ta,tb] × C as the cap in Hts3 given by

tC = {(rω, r2 − (ts)2): r ∈ [ta,tb], ω ∈ C},

and note that

µts(tC) = t2µs(C). (2.7)

We also note that for such a cap C ⊂ Hs3 there exist R ∈ SO(3) and ε ∈ [0,π] such that

√

R−1(C) = {(rω,

r2 − s2): a r b, ω = (cosϕ,cosθ sinϕ,sinθ sinϕ), θ ∈ [0,2π], ϕ ∈ [0,ε]}. (2.8)

Keeping this notation in mind for the rest of the section we study the use of Lorentz transformations and scaling in the regimes when µ(C) is large and small. The follow-

- ing two lemmas will be useful in later sections.


- Lemma 2.3. Let s 2 1, C ⊆ S2 be a spherical cap and C = [1,2] × C be a cap in the hyperboloid Hs3. Let R and ε be as in (2.8) and suppose that ε ∈ [0, π2] and


s−2 sin2 ε 8. Then there exist 0 t < 1 such that L−t 1R−1(C) ⊂ H3√ s

### satisﬁes

1−t2

(L−t 1R−1(C)) π2 and L−t 1R−1(C) ⊆ [167 , 3316] × S2. Moreover, if ε ∈ [0, π3], we can take t = cosε, while if ε ∈ (π3, π2] we can take t = 0. Proof. With R ∈ SO(3) and ε ∈ [0, π2] satisfying (2.8), note that L−t 1R−1(C) = (1 − t2)−1/2L−tR−1(C) ⊆ Hs3(1−t2)−1/2

µ√ s

1−t2

, for every t ∈ (−1,1). According to (2.6), the µs-measure of C satisﬁes

√

√

s2 2

r 2

2 1

r2 − s2 + r +

r2 − s2

µs(C) = 2π(1 − cosε)

ln

√

√

4 − s2 −

1 − s2) π(1 − cosε),

π(1 − cosε)(

so that in what follows we can assume cosε 1/2, otherwise we are done by taking t = 0. From (2.7), for t ∈ (0,1),

(Lt−1R−1(C)) = (1 − t2)−1µs(C),

µ√ s

1−t2

so that choosing t = cosε gives µs(1−t2)−1/2(L−t 1R−1(C)) 1+cos π ε π2. On the other hand, we have

r cosϕ − t√r2 − s2 (1 − t2)1/2

L−t 1R−1(C) = (1 − t2)−1/2

,

√r2 − s2 − tr cosϕ (1 − t2)1/2

: r ∈ [1,2],θ ∈ [0,2π],ϕ ∈ [0,ε] ,

r cosθ sinϕ,r sinθ sinϕ,

and since cosϕ cosε and 1 r 2 we obtain that the fourth coordinate of any point in L−t 1R−1(C) is bounded as follows

√r2 − s2 − tr cosϕ 1 − t2

1 − cos2 ε 1 − cos2 ε

r( 1 − (s/r)2 − tcosϕ) 1 − t2

=

2

= 2

and

r( 1 − (s/r)2 − tcosϕ) 1 − t2

r sin2 ε

( 1 − (s/r)2 − cosεcosϕ) r sin2 ε

=

( 1 − (s/r)2 − cosε)

r

=

- 1 − (s/r)2 + cosε

1 −

1 r2s−2 sin2 ε r

- 2


1 8r2

7 16

1 −

. Therefore

L−t 1R−1(C) ⊆ [φ√ s

(2)] × S2. Now, from the deﬁnition of t and the assumption that s−2 sin2 ε 8 we obtain

### (167 ),φ√ s

1−t2

1−t2

√2 4

s √1 − t2

s sinε

, so that the following inequalities hold

=

### (r) = r2 + s2(1 − t2)−1 r2 + 1/8, from where φ√ s

r φ√ s

1−t2

(2) 16 33 and then we ﬁnd L−t 1R−1(C) ⊆ [167 , 3316] × S2.

### (167 ) 16 7 and φ√ s

1−t2

1−t2

As noted in [6, Lemma 4] for the two-sheeted hyperboloid, a Lorentz transformation can map caps of uniformly bounded measure into a bounded ball. This we record in the next lemma.

- Lemma 2.4. Let s > 0, k ∈ and Ck ⊂ H3s be a dyadic cap of the form Ck = [s2k,s2k+1] × Ck, for some spherical cap Ck ⊆ S2. Let R and ε be associated to Ck as


- in (2.8), then


- (i) The µ¯s-measure of Ck satisﬁes µ¯s(Ck) = 3πs2(1 + ok(1))22k(1 − cosε)

=

3πs2 1 + cosε

(1 + ok(1))22k sin2 ε.

(2.9)

- (ii) Suppose ε ∈ [0, π2]. Then, there exists t ∈ [0,1) such that the orthogonal


projection of L−tR−1(Ck) ⊂ H3s to 3 is contained in a ball of 3 of radius comparable to s + s−1µ¯s(Ck) + µ¯s(Ck)1/2.

Proof. Without loss of generality, we may assume that Ck is contained in the upper half Hs3. For part (i), (2.6) implies that the µ¯s-measure of Ck is given by the expression

√

2k+1 +

22(k+1) − 1 2k + √22k − 1

µ¯s(Ck) = πs2(1−cosε) ln

+2k+1 22(k+1) − 1−2k 22k − 1 .

The expression involving the logarithm converges to ln(2) as k → ∞, while

22(k+1)(22(k+1) − 1) − 22k(22k − 1) 2k+1

2k+1 22(k+1) − 1 − 2k 22k − 1 =

√

22(k+1) − 1 + 2k√22k − 1

15 − 3 · 2−2k 4

= 22k

√

1 − 2−2(k+1) + √1 − 2−2k

= 3 · 22k(1 + ok(1)).

For part (ii), let R ∈ SO(3) and ε ∈ [0, π2] be such that (2.8) holds. The image of R−1(Ck) under the Lorentz boost L−t is

r cosϕ − t√r2 − s2 (1 − t2)1/2

√r2 − s2 − tr cosϕ (1 − t2)1/2

L−tR−1(Ck) =

,r cosθ sinϕ,r sinθ sinϕ,

r ∈ [s2k,s2k+1],θ ∈ [0,2π],ϕ ∈ [0,ε] . (2.10) Let t =

√

1 − 2−2(k+1), so that the ﬁrst coordinate of a point in the set on the right hand side of (2.10) is bounded as follows

r cosϕ − t√r2 − s2 (1 − t2)1/2

= 2k+1r|cosϕ − 1 − 2−2(k+1) 1 − (s/r)2| 22(k+1)s(1 − cosϕ) + 22(k+1)s(1 − (1 − 2−2(k+1)))

= 22(k+1)s(1 − cosε) + s

µ ¯s(Ck) s

+ s, where in the last line we used (2.9). The second and third coordinates are bounded

- as follows |r cosθ sinϕ|, |r sinθ sinϕ| 2k+1ssinε µ¯(Ck).


Then L−tR−1(Ck) is contained in the set

µ¯s(Ck) s

(x,t) ∈ H3s : |x| C µ¯s(Ck) +

+ s , for some constant C independent of k and s.

:

3. Calculation of a double convolution

In previous studies of quadric surfaces and curves and their perturbations it has become clear the importance of the double or triple, and more generally the n-th fold, convolution of the underlying measure. Its properties may determine existence or nonexistence of extremizers and in some cases it can be used to ﬁnd their explicit form and/or the value of the best constant in the corresponding adjoint Fourier restriction inequality. In the case of the one-sheeted hyperboloid and its upper half, the double convolution will be used to prove that extremizing sequences do not concentrate at inﬁnity.

Let µs ∗ µs denote the double convolution of µs with itself, deﬁned by duality µs ∗ µs,f =

f(x + x ,t + t )dµs(x,t)dµs(x ,t ),

( 4)2

for all f ∈ S( 4). It is not diﬃcult to see that µs ∗ µs is absolutely continuous with respect to the Lebesgue measure in 4, indeed this follows from (1.3) since e−τ(µs∗µs) ∈ L2( 4), it being the (inverse) Fourier transform of the L2( 4) function ( e−τµs)2 (see also [28, Proposition 2.1]). In what follows we identify µs ∗ µs with its Radon–Nicodym derivative with respect to the Lebesgue measure in 4.

- Proposition 3.1. Let µs be the measure on Hs3 deﬁned in (1.11). Then


- (i) The support of the convolution measure µs ∗ µs is

supp(µs ∗ µs) = {(ξ,τ) ∈ 4: τ 0, |ξ|

√

τ2 + s2 + s}.

- (ii) For every (ξ,τ) ∈ 4 with τ 0 we have the formula


4s2 τ2 − |ξ|2

- 1

- 2


2π |ξ|

√

{|ξ|<√τ2+s2−s} + τ {√τ

µs ∗ µs(ξ,τ) =

|ξ| 1 +

2+s2−s |ξ|

τ2+(2s)2}

4s2 τ2 − |ξ|2

- 1

- 2


√

+ τ − |ξ| 1 +

√τ2+s2+s} .

τ2+(2s)2<|ξ|

{

(3.1) When ξ = 0 and τ > 0 we understand that in (3.1) µs ∗ µs(0,τ) = 2π(1 + 4τs2

)1/2.

2

We postpone the proof of Proposition 3.1 and study the behavior of µs ∗ µs(ξ,τ) for large τ.

## Lemma 3.2. For all τ > 0,

4s2 τ2

2s τ

1/2

µs ∗ µs(ξ,τ) 2π 1 +

2π 1 +

. In particular

sup

ξ∈ 3

µs ∗ µs(ξ,τ) = 2π. Proof. We start by noting that

lim

sup

τ→∞

ξ∈ 3

µs ∗ µs(sξ,sτ) = µ ∗ µ(ξ,τ),

hence it is enough to consider the case s = 1. We analyze the diﬀerent cases in formula (3.1).

- Case 1. |ξ| < √τ2 + 1 − 1. Then

1 +

4 τ2

1/2

1 +

4 τ2 − |ξ|2

1/2

√τ2 + 1 + 1 √τ2 + 1 − 1

1/2

=

τ √τ2 + 1 − 1

.

- Case 2. √τ2 + 1 − 1 |ξ|


√τ2 + 4. Then τ √τ2 + 4

τ |ξ|

τ √τ2 + 1 − 1

.

- Case 3. √τ2 + 4 < |ξ|


√τ2 + 1 + 1. Then |ξ|2 − τ2 > 4 and

τ |ξ|

4 τ2 − |ξ|2

1/2

|ξ|  →

− 1 +

is a decreasing function of |ξ|. Then

τ |ξ|

4 τ2 − |ξ|2

1/2 τ √τ2 + 4

− 1 +

,

and

τ |ξ|

4 τ2 − |ξ|2

1/2 τ √τ2 + 1 + 1 − 1 −

2 √τ2 + 1 + 1

1/2

− 1 +

= 0.

As a conclusion, for all τ > 0 and x ∈ 3

2πτ √τ2 + 1 − 1

1 τ

2 τ

1 τ2

1/2

µ ∗ µ(ξ,τ)

+

2π 1 +

,

= 2π 1 +

and for τ > 0

4 τ2

1/2

µ ∗ µ(ξ,τ) 2π 1 +

sup

.

ξ∈ 3

We now turn to the proof of Proposition 3.1.

Proof of Proposition 3.1. Part (i) is a simple calculation and is left to the reader. For part (ii) we start by discussing a change of coordinates that was used in the proof of [15, Lemma 5.1] in the arxiv’s second version of [15]; see also Appendix 3 on the arxiv’s version of [33] where an outline of the computation of the double convolution of the Lorentz invariant measure on the two-sheeted hyperboloid was given using the same technique.

For each ﬁxed ξ = 0 we consider a spherical coordinate system with axis ξ, that is, each η ∈ 3 is described as η = (ρcosθ sinϕ,ρsinθ sinϕ,ρcosϕ), where ρ = |η| 0, ϕ ∈ [0,π] is the angle between ξ and η and θ ∈ [0,2π] is a polar coordinate angle on the plane orthogonal to ξ. Then dη = ρ2 sinϕdρdθ dϕ.

Deﬁne the new variable ς = |ξ − η|, which corresponds to the size of the side opposite to the origin, 0, in the triangle whose vertices are located at 0, ξ and η. Then

ς2 = |ξ|2 + ρ2 − 2|ξ|ρcosϕ. Changing variables from ϕ to ς, gives ς dς = |ξ|ρsinϕdϕ, so that in the variables (ρ,ς,θ) we have dη = |ρςξ| dρdς dθ. The range of ς can be seen by using that ς, |ξ| and ρ are the sizes of the sides of a triangle, so |ρ − ς| |ξ| ρ + ς, which translates into ||ξ| − ρ| ς |ξ| + ρ.

Using delta calculus (see for instance the survey article [17]) and the previous change of variables we have

δ τ − |ξ − η|2 − s2 − |η|2 − s2

µs ∗ µs(ξ,τ) = η∈ 3

dη

|ξ − η|2 − s2 |η|2 − s2

|η| s |ξ−η| s

√ς2 − s2 − ρ2 − s2 √ς2 − s2 ρ2 − s2

δ τ −

2π |ξ| |ρρ+−ςς| |ξ |ξ||

=

ρς dρdς

ρ s, ς s

2π |ξ| Rs

δ τ − u − v dudv,

=

where we changed variables u = ρ2 − s2, v = √ς2 − s2 and Rs = Rs(ξ) is the image of the region {(ρ,ς): |ρ − ς| |ξ|,ρ + ς |ξ|,ρ s,ς s} under the transformation (ρ,ς)  → (u,v). Using the change of variables a = u−v, b = u+v, so that 2dudv = dadb, we obtain

√

π |ξ| Rs

π |ξ|

π |ξ|

| Rs ∩ ˜ τ| =

δ τ − b dadb =

µs ∗ µs(ξ,τ) =

2|Rs ∩ τ|. (3.2)

where Rs = Rs(ξ) is the image of Rs(ξ) under the map (u,v)  → (a,b), ˜ τ is the horizontal line {(a,b) ∈ 2 : b = τ}, τ is the line {(u,v) ∈ 2 : u + v = τ} and |Rs ∩ τ| denotes the measure of Rs ∩ τ as a subset of τ with the induced Lebesgue measure. In order to calculate |Rs ∩ τ| we divide the analysis into two cases.

Case 1: |ξ| 2s. The boundary of the region

{(ρ,ς): |ρ − ς| |ξ|,ρ + ς |ξ|,ρ s,ς s}

consists of two (bounded) line segments and two half lines. Its image in the (u,v)plane, Rs, is bounded by two line segments and two curves and is symmetric with respect to the diagonal u = v. The line segments have equations

{(u,v): u = 0, 0 v (|ξ| + s)2 − s2},{(u,v): 0 u (|ξ| + s)2 − s2, v = 0} and the curves have equations

√

u2 + s2 + |ξ|)2 − s2 1/2 , (u,v): u (|ξ| + s)2 − s2 1/2, v = (

(u,v): u 0, v = (

(3.3)

√

u2 + s2 − |ξ|)2 − s2 1/2 .

Then |Rs ∩ τ| is given by

√2τ , if 0 τ (|ξ| + s)2 − s2 1/2 √2|u − v| , if τ > (|ξ| + s)2 − s2 1/2,

|Rs ∩ τ| =

where in the last expression u and v are related to (ξ,τ) by the equations u + v = τ and v = (√u2 + s2 + |ξ|)2 − s2 1/2. Therefore

√

2|Rs ∩ τ| = 2τ {τ √

(|ξ|+s)2−s2}

- 1

- 2


− u1(ξ,τ)) {τ>√

+ 2(( u1(ξ,τ)2 + s2 + |ξ|)2 − s2)

(|ξ|+s)2−s2}, where u1(ξ,τ) and (ξ,τ) are related by the expression

τ = u1(ξ,τ) + ( u1(ξ,τ)2 + s2 + |ξ|)2 − s2 1/2, (3.4)

- and 0 u1(ξ,τ) τ2. Case 2: |ξ| > 2s. Now the boundary of the region {(ρ,ς): |ρ − ς| |ξ|,ρ + ς

|ξ|,ρ s,ς s} consists of three (bounded) line segments and two half lines and the region Rs is now bounded by two line segments and three curves. The line segments have equations

{(u,v): u = 0, (|ξ| − s)2 − s2 v (|ξ| + s)2 − s2}, {(u,v): (|ξ| − s)2 − s2 u (|ξ| + s)2 − s2, v = 0}.

The next two curves have equations as in (3.3). The last boundary curve is the image of the segment {(ρ,ς): ρ + ς = |ξ|, s ρ |ξ| − s}. Its equation is

{(u,v): 0 u (|ξ| − s)2 − s2 1/2, v = (|ξ| −

√

u2 + s2)2 − s2 1/2},

and note that it is the graph of a strictly decreasing and concave function of u. It follows that

|Rs ∩ τ| =

 



√2(τ − |u2 − v2|) , if (|ξ| − s)2 − s2 τ |ξ|2 − (2s)2, √2τ , if |ξ|2 − (2s)2 τ (|ξ| + s)2 − s2

√2|u1 − v1| , if τ (|ξ| + s)2 − s2 1/2,

,

where (u1,v1), (u2,v2) are the solutions to the equations u1 + v1 = τ, u2 + v2 = τ, v1 = ( u21 + s2 + |ξ|)2 − s2 1/2 and v2 = (|ξ| − u22 + s2)2 − s2 1/2.

Then √

2|Rs ∩ τ| = 2 τ − ((|ξ| − u2(ξ,τ)2 + s2)2 − s2)1/2 − u2(ξ,τ) {√

(|ξ|−s)2−s2 τ<

√

|ξ|2−(2s)2}

+ 2τ {√

|ξ|2−(2s)2 τ

√

(|ξ|+s)2−s2}

+ 2 (( u1(ξ,τ)2 + s2 + |ξ|)2 − s2)1/2 − u1(ξ,τ) {τ>√

(|ξ|+s)2−s2}, where u1(ξ,τ) is as in (3.4) and u2(ξ,τ) and (ξ,τ) are related by the expression

τ = u2(ξ,τ) + ( u2(ξ,τ)2 + s2 − |ξ|)2 − s2 1/2,

- and 0 u2(ξ,τ) τ2. Algebraic manipulation shows that for (ξ,τ) in their respective domains of deﬁnition


4s2 τ2 − |ξ|2

1/2

τ − 2ui(ξ,τ) = |ξ| 1 +

, i = 1,2. (3.5)

Collecting all in one expression we have √

2|Rs ∩ τ| = 2τ {τ √

(|ξ|+s)2−s2} {|ξ| 2s}

### + 4u2(ξ,τ) {√

√

|ξ|2−(2s)2} {|ξ|>2s}

(|ξ|−s)2−s2 τ<

### + 2τ {√

√

(|ξ|+s)2−s2} {|ξ|>2s}

|ξ|2−(2s)2 τ

+ 2(τ − 2u1(ξ,τ)) {τ>√

(|ξ|+s)2−s2}. Replacing u1(ξ,τ) and u2(ξ,τ) using (3.5) we obtain using (3.2) µs ∗ µs(τ,ξ) =

2π |ξ|

τ {τ √

(|ξ|+s)2−s2} {|ξ| 2s}

4s2 τ2 − |ξ|2

1/2

√

√

+ τ − |ξ| 1 +

|ξ|2−(2s)2} {|ξ|>2s}

(|ξ|−s)2−s2 τ<

{

### + τ √

√

(|ξ|+s)2−s2 {|ξ|>2s}

|ξ|2−(2s)2 τ

4s2 τ2 − |ξ|2

1/2

√

+ |ξ| 1 +

(|ξ|+s)2−s2} .

{τ>

(3.6) Rearranging (3.6) we ﬁnd that µs∗µs can be written in the equivalent form (3.1).

More generally, the same method used in the proof of Proposition 3.1 allows us to write an explicit formula for µs ∗µt, for any s, t 0. For instance, as it will be useful in Section 12, we have

π |ξ| Qs(ξ)

δ τ − b dadb, (3.7)

µs ∗ µ0(ξ,τ) =

where Qs(ξ) is the image of the set {(ρ,ς): |ρ − ς| |ξ|, ρ + ς |ξ|, ρ 0, ς s} under the transformations (ρ,ς)  → (u,v) = (ρ,√ς2 − s2)  → (a,b) = (u − v,u + v). Here µ0 equals σc, the Lorentz invariant measure on the cone. A calculation similar to the one for µs ∗ µs gives the following explicit formula

|ξ|(τ2 − |ξ|2 + s2) τ2 − |ξ|2 {τ s} {|ξ|<τ−s}

2π |ξ|

µs ∗ σc(ξ,τ) =

(τ + |ξ|)2 − s2 2(τ + |ξ|) {τ 0} {|τ−s| |ξ|<

√τ2+s2}

(3.8)

+

s2 − (|ξ| − τ)2 2(|ξ| − τ) {τ 0} {

√τ2+s2 |ξ| τ+s} .

+

Using (3.8) we see that for each τ 0

 

√τ2τ+s2 ,0 τ 2 s 2(√5 − 1) 1 + (s−

τ2 , 2s 2(√5 − 1) τ s 1 + 2τs−s ,τ s

√s2−τ2)2

µs ∗ σc(ξ,τ) = 2π ·

sup

(3.9)



ξ∈ 3

and µs ∗ σc L∞( 4) = 4π.

4. Comparison with the cone

Recall that σc denotes the scale and Lorentz invariant measure on the cone Γ3 and Tc denotes its associated adjoint Fourier restriction operator. From [1] we know the value of the sharp constant

fσc ∗ fσc 2L4( 4) f 4L2(σ

= 2π. (4.1)

sup

0 =f∈L2(σc)

c)

We had deﬁned the numerical constants

fσc ∗ fσc 1L/42( 4) f L2(σc)

Tcf L4( 4) f L2(σc)

C4 = sup

= 2π sup

,

0 =f∈L2(σc)

0 =f∈L2(σ)

fµ ∗ fµ L 1/42( 4) f L2(µ)

Tf L4( 4) f L2(µ)

H4 = sup

= 2π sup

.

0 =f∈L2(µ)

0 =f∈L2(µ)

The next proposition gives a comparison between C4 and H4 and its role is the analog of the comparison of the best constant for the sphere and the paraboloid in 3 as used in [9] where an strict inequality was needed to rule out concentration

- at a pair of antipodal points. In our present case, an strict inequality will rule out concentration at inﬁnity.


## Proposition 4.1. H4 > C4.

√

a 2

|y|2−s2, a > 0, and claim that

Proof. We consider the family of trial functions fa(y) = e−

Tsfa L4( 4) fa L2(Hs3)

Tcf L4( 4) f L2(σc)

sup

> sup

.

a>0

0 =f∈L2(σc)

Using spherical coordinates, the L2(Hs3)-norm of fa is given by the expression

√

∞

√r2−s2 r2 √r2 − s2

|x|2−s2 dx |x|2 − s2

e−a

e−a

fa 2L2(Hs3) =

= 4π

dr

3

s

√

∞

e−aτ

τ2 + s2 dτ.

= 4π

0

It is easier to estimate Tsfa L4( 4) if we use the convolution form (2.3), Tsfa L4( 4) = 2π faµs ∗ faµs L 1/22( 4).

As in [33, Appendix 2], using that fa is the restriction to Hs3 of the exponential of the linear function in 4, (ξ,τ)  → e−

a

2τ, we obtain faµs ∗ faµs(ξ,τ) = e−

a

2τ µs ∗ µs(ξ,τ) . It will be enough for our purpose to use

µs ∗ µs(ξ,τ)

2π |ξ|

4s2 τ2 − |ξ|2

|ξ| 1 +

- 1

- 2


{|ξ|<√τ2+s2−s} + τ {√τ

2+s2−s |ξ|

√

τ2+(2s)2} ,

as obtained from (3.1). In this way faµs ∗ faµs(ξ,τ)

4s2 τ2 − |ξ|2

- 1

- 2


2π |ξ|

a

√

e−

2τ |ξ| 1 +

{|ξ|<√τ2+s2−s} + τ {√τ

τ2+(2s)2} , so that using spherical coordinates we obtain

2+s2−s |ξ|

4s2 τ2 − |ξ|2 {|ξ|<

e−aτ |ξ|2 1 +

faµs ∗ faµs 2L2( 4) (2π)2

√τ2+s2−s}

3×

dξ |ξ|2

√

+ τ2 {√τ

τ2+(2s)2} dτ

2+s2−s |ξ|

√

√

∞

1 3

e−aτ τ2( τ2 + (2s)2 −

= 16π3

τ2 + s2 − s)3

τ2 + s2 + s) +

(

0

τ + √τ2 + s2 s

√

− 4s2(

τ2 + s2 − s) + 2s2τ log

dτ

√

√

∞

8s3 3

- 2

- 3


e−aτ τ2

= 16π3

(τ2 + 4s2)

τ2 + 4s2 −

τ2 + s2 +

0

τ + √τ2 + s2 s

+ 2s2τ log

dτ. Since by scaling it is enough to consider s = 1 (see Section 14) we let

- I(a) = 16π3

∞

0

e−aτ τ2

√

τ2 + 4 − 32(τ2 + 4)

√

τ2 + 1 + 83

+ 2τ log τ +

√

τ2 + 1 dτ,

- II(a) = 16π2


2

√

∞

e−aτ

τ2 + s2 dτ

, then

0

faµ ∗ faµ 2L2( 4) fa 4L2(µ)

- I(a)

- II(a)


.

Form Lemma A.1 in the appendix, we conclude that for all a > 0 small enough faµ ∗ faµ 2L2( 4) fa 4L2(µ)

> 2π. (4.2)

This ﬁnishes the proof in view of (4.1).

Remark 4.2. The easy lower bound we can obtain for faµ ∗ faµ 2L2( 4) fa −L24(µ) using the analog of [28, Lemma 6.1] is not good enough in this case to obtain (4.2).

Let us now move to the full one-sheeted hyperboloid H3. Recall that Tc denotes the adjoint Fourier restriction operator on the double cone Γ3. An argument in [15]

can be used to show that

1

3 2

4 Tc , (4.3)

Tc =

see for instance [33, Proposition 7.3]. We now compare the best constant for T and Tc.

- Proposition 4.3. For the one-sheeted hyperboloid H3 and its adjoint Fourier restriction operator T we have

T > Tc . Proof. Let fa(y) = e−

a 2

√

|y|2−1 be as in the proof of Proposition 4.1 and set ga = fa,+ + fa,−, where fa,+ = cfa and fa,− = cfa (here there are domain identiﬁcations through projections to 3), in other words, ga(ξ,τ) = ce−

a 2 |τ|

H3(ξ,τ), where c is such that ga is L2 normalized. Expanding and using the positivity of fa,+ and fa,− (which for brevity we simply call f+ and f−, respectively) we see that

Tga 4L4 = Tf+ 4L4( 3) + Tf− 4L4( 3) + 4 (Tf+)(Tf−(·,−·)) 2L2

+ 4(2π)4 f+µ ∗ f+µ,f+µ ∗ f−µ−

+ 4(2π)4 f+µ ∗ f−µ−,f−µ− ∗ f−µ− Tf+ 4L4( 3) + T−f− 4L4( 3) + 4 (Tf+)(Tf−(·,−·)) 2L2.

On the other hand Tf−(·,−·) = Tf+, the complex conjugate, since f−(y) = f+(−y). Then (Tf+)(Tf−(·,−·)) 2L2 = Tf+ 4L4( 3) = Tf− 4L4( 3) and we obtain

Tga 4L4 6 Tfa,+ 4L4( 3). If a > 0 is small enough, then from (4.2) in the proof of Proposition 4.1 and using fa,+ L2(µ) = √2/2, we obtain

Tga 4L4 6 Tfa,+ 4L4( 3) > 6 Tc 4 fa,+ 4L2(µ) =

3 2

Tc 4. The conclusion follows using (4.3).

5. The upper half of the one-sheeted hyperboloid

In this section we present the proof of Theorem 1.2. The proof of precompactness of extremizing sequences, modulo multiplication by characters, is much simpler for the upper half of the one-sheeted hyperboloid as the full Lorentz invariance of H3 is absent for H3.

In what follows we collect the necessary results to invoke Proposition 1.5 and the ﬁrst such step is to show that, with enumeration as in Proposition 1.5, (i) and (iii) imply (iv), possibly after passing to a subsequence.

- Proposition 5.1. Let {fn}n be a sequence in L2(H3) satisfying supn fn L2(H3) < ∞. Suppose that there exists f ∈ L2(H3) such that fn f as n → ∞. Then, there exists


k → Tf a.e. in 4.

a subsequence {fn

k}k such that Tfn

The previous result implies an analogous one for the full two-sheeted hyperboloid H3. Recall the Fourier multiplier notation

√

√

1 (2π)3 {y∈ 3: |y| s}

−∆−s2u(x) =

|y|2−s2uˆ(y)dy, (5.1)

eix·yeit

eit

and the homogeneous H˙ 1/2( 3) Sobolev norm and inner product

u 2H˙

1/2( 3) :=

### |uˆ(y)|2|y|dy, u,v H ˙ 1/2( 3) :=

3

uˆ(y)vˆ(y)|y|dy. (5.2)

3

Proof of Proposition 5.1. The proof follows similar lines to the proofs of [14, Theorem 1.1] and [32, Proposition 8.3]. We start by splitting fn = fn B(0,2) + fn B(0,2) =: fn,1 +fn,2, respectively, and f = f B(0,2) +f B(0,2) =: f1 +f2. The conclusion of the proposition will follow if we show that there exists a subsequence {fn

k}k such that Tfn

k,2 → Tf2 a.e. in 4.

k,1 → Tf1 and Tfn

Since fn,1 f1 in L2(H3) and the support of fn,1 is contained on the compact set B(0,2), it follows that Tfn,1(x,t) → Tf1(x,t) for all (x,t) ∈ 4 given that the function (y,s)  → eix·yeits B(0,2)(y) belongs to L2(H3).

To study the pointwise convergence of Tfn,2 deﬁne gn and g by their Fourier transforms as follows

fn,2(y) |y|2 − 1

f2(y) |y|2 − 1

gˆn(y) =

. Because

, gˆ(y) =

dy |y|2 − 1

fn,2 2L2(H3) =

|fn(y)|2

fk 2L2(H3) =: c,

sup

k

{y∈ 3:|y| 2}

we see that the norms of the gn’s in the homogeneous Sobolev space H˙ 1/2( 3) are uniformly bounded

2 √3 {y∈ 3:|y| 2}

dy |y|2 − 1

2c √3

|fn,2(y)|2

gn 2H˙

|gˆn(y)|2|y|dy

.

1/2( 3) =

3

The weak convergence of {fn,2}n to f2 in L2(H3) easily implies gn g as n → ∞ in H˙ 1/2( 3). On the other hand

|fn,2(y)|2 ( |y|2 − 1)2

dy |y|2 − 1

c √3

(2π)3 gn 2L2( 3) = gn 2L2( 3) =

,

{y∈ 3:|y| 2}

so {gn}n is uniformly bounded in L2( 3). The operator T applied to fn,2 equals (2π)3eit

√

√

−∆−1 is understood in the Fourier multiplier sense as in (5.1). Let t ∈ be ﬁxed. By the continuity of eit

−∆−1gn, where the operator eit

√

−∆−1 in H˙ 1/2( 3) we obtain eit

√

√

−∆−1gn eit

−∆−1g

weakly in H˙ 1/2( 3), as n → ∞. Then, by the Rellich-Kondrashov Theorem ([11, Theorem 7.1]), for any R > 0

√

√

−∆−1gn → eit

−∆−1g

eit

strongly in L2(B(0,R)), as n → ∞. Denote by

2

√

√

−∆−1(gn − g) 2L2(B(0,R)). By H¨older’s inequality and Sobolev embedding, [11, Theorem 6.5], we obtain Fn(t) = eit

−∆−1(gn − g)

dx = eit

eit

Fn(t) :=

|x|<R

√

√

−∆−1(gn − g) 2L3(B(0,R)) CR eit

−∆−1(gn − g) 2L2(B(0,R)) CR eit

√

8 √3

−∆−1(gn − g) 2H˙

cCR, then, by the Fubini and Dominated Convergence Theorems we have that

1/2( 3)

2

R

R

√

−∆−1(gn − g)

eit

dxdt → 0, as n → ∞. This implies that, up to a subsequence,

Fn(t)dt =

−R |x|<R

−R

√

√

−∆−1gn(x) − eit

−∆−1g(x) → 0 a.e. (x,t) ∈ B(0,R) × (−R,R).

eit

Repeating the argument on a discrete sequence of radii Rn such that Rn → ∞, as n → ∞ we conclude, by a diagonal argument, that there exists a subsequence {gn

k}k of {gn}n such that

√

√

−∆−1g(x) → 0 a.e. for (x,t) ∈ 4, or equivalently, in terms of the sequence {fn,2}n and the operator T,

−∆−1gn

eit

(x) − eit

k

k,2(x,t) → Tf2(x,t) a.e. (x,t) ∈ 4.

Tfn

We now show that the only obstruction to precompactness of extremizing sequences is the possibility of concentration at inﬁnity, as in Deﬁnition 1.6.

- Proposition 5.2. Let {fn}n ⊂ L2(H3) be an L2 normalized extremizing sequence for T. Suppose that {fn}n does not concentrate at inﬁnity. Then there exist a subsequence


√

|y|2−1fn

k·yeit

k}k and a sequence {(xk,tk)}k ⊂ 4 such that {eix

{fn

k}k is convergent

k

in L2(H3). Proof. If {fn}n does not concentrate at inﬁnity, then there exist ε,R > 0 with the property that for all N ∈ there exists n N such that

fn B(0,R) L2(H3) ε. We can generate a subsequence, {fn

k B(0,R) L2(H3) ε for all k ∈ . Rename the subsequence as {fn}n, if necessary. Writing fn = fn B(0,R)+fn B(0,R) =: fn,1 + fn,2, respectively, we have

k}k, such that fn

Tfn,1 L4( 4) = T(fn − fn,2) L4( 4) Tfn L4( 4) − Tfn,2 L4( 4) Tfn L4( 3) − H4 fn,2 L2(H3)

= Tfn L4( 3) − H4(1 − fn,1 2L2(H3))1/2 Tfn L4( 3) − H4

√

1 − ε2. (5.3)

As the right hand side in (5.3) converges to c := H4 − H4√1 − ε2 > 0 as n → ∞ we see that

c 2

> 0, (5.4) for all large n.

Tfn,1 L4( 4)

We may use the argument in the proof of [13, Theorem 1.1] to construct the sequence {(xn,tn)}n. In brief, the argument goes as follows. Taking any p¯ ∈ [103 ,4), interpolating the L4 norm of Tfn,1 between Lp¯ and L∞ and using (5.4) together with the boundedness of T in Lp¯ imply that Tfn,1 L∞( 4) 1, so that there exists a sequence {(xn,tn)}n ⊂ 4 such that |Tfn,1(xn,tn)| C > 0, that is, |(T(eix

√

|y|2−1fn,1))(0,0)| C > 0. The compact support of fn,1 implies that Tfn,1 belongs to C∞( 4) and Tfn,1 L∞( 4) fn,1 L1 1,  ∇x,tTfn,1 L∞( 4)

n·yeit

n

√

|y|2−1fn,1)}n is precompact in the space of continuous functions on the unit ball of 4. On the other hand, passing to a subsequence, we may assume Fn := eix

n·yeit

fn,1 L1 1. By the Arzela´–Ascoli Theorem, it follows that {T(eix

n

√

|y|2−1fn,1 f1 weakly in L2(H3), for some f1 ∈ L2(H3), and then T(Fn)(x,t) → Tf1(x,t) for all

n·yeit

n

- (x,t) ∈ 4. Moreover, T(Fn) → Tf1 uniformly in the unit ball, so that |Tf1(0,0)| C > 0, which implies that f1 = 0.


Compactness of the unit ball in L2(H3) in the weak topology implies that, after passing to a further subsequence, eix

√

|y|2−1fn f, for some f ∈ L2(H3). Since f1 = f B(0,R) a.e. in 3 we conclude that f = 0. Therefore condition (iii) of Proposition 1.5 is satisﬁed. Proposition 5.1 implies that condition (iv) is also satisﬁed. As (i) and (ii) are immediate, we conclude that eix

n·yeit

n

√

|y|2−1fn → f in L2(H3), and we are done.

n·yeit

n

To conclude the precompactness of extremizing sequences we need to discard the possibility of concentration at inﬁnity. For this we use a comparison argument with the cone where the upper bound for µs ∗ µs as found in Lemma 3.2 will be useful. Lemma 5.3. Let a > 1 and f ∈ L2(H3) be supported in the region where |y| a. Then

1 √a2 − 1

f 4L2(µ).

fµ ∗ fµ 2L2( 4) 2π 1 +

Proof. If f is supported where |y| a, then the support of fµ ∗ fµ is contained in the region {(ξ,τ) ∈ 4: τ 2√a2 − 1}. The Cauchy-Schwarz inequality provides the a.e. pointwise bound

|fµ ∗ fµ|2(ξ,τ) |f|2µ ∗ |f|2µ (ξ,τ) µ ∗ µ (ξ,τ), which together with the upper bound in Lemma 3.2 imply

1

√a2 − 1 |f|2µ ∗ |f|2µ (ξ,τ), for a.e. (ξ,τ) ∈ 4. Integrating over (ξ,τ) ∈ 4 yields the result.

|fµ ∗ fµ|2(ξ,τ) 2π 1 +

It is now direct to prove our ﬁrst main theorem.

Proof of Theorem 1.2. We start by noting that if an L2-normalized sequence {fn}n concentrates at inﬁnity, then for any a > 1, fn B(0,a) L2(µ) → 0 as n → ∞, therefore, for such a sequence we obtain, using Lemma 5.3, that

fnµ ∗ fnµ 2L2( 4) fn 4L2(µ)

limsup

2π.

n→∞

Using Proposition 4.1 we conclude that an extremizing sequence for T does not concentrate at inﬁnity. We apply Proposition 5.2 to conclude.

6. The full one-sheeted hyperboloid

Our task in the sections to come is to prove Theorem 1.3, the existence of extremals for the adjoint Fourier restriction inequality on the one-sheeted hyperboloid H3. In the L4 case, there is an argument available for the cone Γ3 that allows to relate the best constant and extremizers for Γ3 with that for the double cone Γ3. It relies on the observation that the algebraic sums Γ3 + Γ3 and Γ3 + (−Γ3) intersect on a null set of 3, namely, (Γ3 + Γ3) ∩ (Γ3 + (−Γ3)) = Γ3, so that for any f+,g+,h+ ∈ L2(Γ3) and f− ∈ L2(−Γ3) one has

f+σc ∗ g+σc,h+σc ∗ f− σc L

2( 4) = 0,

where σc denotes the reﬂection of σc, supported on −Γ3. An analogous property in the L4 case applies to the two-sheeted hyperboloid in 4 and allows one to obtain its best constant from that of the upper sheet only (see [33, Proposition 7.3, Corollary 7.4]). This approach is not applicable to H3 because here H3 + H3 and H3 + (−H3) intersect on a set of inﬁnite Lebesgue measure.

The argument we use to prove precompactness of extremizing sequences (modulo multiplication by characters and Lorentz transformations) is close to that of Christ and Shao [9] and of [32] using a concentration-compactness argument, a reﬁned cap estimate, comparison to the cone and the use of Lorentz invariance.

In the next section we review a cap reﬁnement for the Tomas–Stein inequality for S2 that will be used in the subsequent section to obtain a corresponding cap reﬁnement for the adjoint Fourier restriction inequality on the hyperboloid via a lifting method. In later sections we consider the concentration-compactness argument.

7. The Tomas–Stein inequality for S2 and refinements

The sharp convolution form of the Tomas–Stein inequality for S2 states that for all f ∈ L2(S2) we have

fσ ∗ fσ L2( 3) S2 f 2L2(S2), (7.1) where S = (2π)1/4 is the sharp constant, as obtained in [15].

In this section we review some reﬁnements of (7.1) that will be useful in the next section. The exposition here follows that of [9, Section 6]. We start by setting things up to deﬁne the Xp spaces, p ∈ [1,∞), and the ﬁrst step is to generate increasingly ﬁner ”grids” for the sphere S2. With this in mind, for each integer k 0 choose a maximal subset {ykj}j ⊂ S2 satisfying |ykj − ykl | 2−k, for all j = l. Then, for each

k 0, the spherical caps Cjk := C(ykj,2−k+1) have ﬁnite overlap and cover S2, that is, ∪jCjk = S2, and there exists a constant C, independent of k, such that any point in S2 belongs to no more than C caps in {Cjk}j, for every k 0. For p ∈ [1,∞), the Xp norm of f is deﬁned by the expression

4/p

1 |Cjk| C

2−4k

f 4X

|f|p dσ

### =

. (7.2)

p

- j
- k


k 0 j

Moyua, Vargas and Vega showed in [25] that there is a continuous inclusion L2(S2) ⊂ Xp for all p ∈ (1,2) and that for any p 127 there exists C < ∞ such that for all f ∈ L2(S2)

. (7.3) Let us deﬁne

fσ L4( 3) C f X

p

Λk,j(f) = |Cjk|−1

|f|dσ |Cjk|−1

Cjk

|f|2 dσ

S2

−1/2

,

which by Ho¨lder’s inequality satisﬁes Λk,j(f) 1. It was shown in [9, Lemma 6.1] that for any p ∈ [1,2), there exists C < ∞ and γ > 0 such that for any f ∈ L2(S2),

(Λk,j(f))γ. (7.4)

C f L2(S2) sup

f X

p

k,j

Combining the two results, (7.3) and (7.4), by choosing any p ∈ [127 ,2), we obtain the following ”cap reﬁnement” of (7.1): there exists C < ∞ and γ > 0 such that for

all f ∈ L2(S2)

(Λk,j(f))γ. (7.5) A δ-quasi-extremal for the sphere is a function f = 0 that satisﬁes fσ∗fσ L4( 3)

fσ L4( 3) C f L2(S2) sup

k,j

δ2S2 f 2L2(S2). With the aid of the previous inequality, Christ and Shao proved the following result regarding δ-quasi-extremals.

- Lemma 7.1 ([9, Lemma 2.9]). For any δ > 0 there exists Cδ > 0 and ηδ > 0 with


the following property. If f ∈ L2(S2) satisﬁes fσ ∗fσ 2 δ2S2 f 22 then there exist a decomposition f = g + h and a spherical cap C ⊆ S2 satisfying

0 |g|,|h| |f|, (7.6) g,h have disjoint supports, (7.7) |g(x)| Cδ f 2|C|−1/2 C(x) for all x, (7.8)

g 2 ηδ f 2. (7.9)

Moreover (7.8) and (7.9) hold with constants that satisfy Cδ δ−1/γ and ηδ δ1/γ, where γ > 0 is a universal constant3.

3The power dependence of Cδ and ηδ on δ can be found in the proof of the lemma in [9, pp. 277-278]

It will be our task in the next section to obtain an analogous result for the hyperboloid and for this it will be convenient to brieﬂy discuss the construction of the function g and the cap C in the conclusion of the previous lemma. Letting f ∈ L2(S2) be a δ-quasi-extremal, inequality (7.5) implies that there is a constant c0 ∈ (0,∞), independent of f, such that

Λk,j(f) 2c0δ1/γ.

sup

k,j

It follows that there exist k and j such that Λk,j(f) c0δ1/λ. Let C := Cjk. Then,

|f|dσ c0δ1/γ|C|1/2 f L2(S2). (7.10)

C

Let R = (21c0δ1/γ|C|1/2 f L2(S2))−1, A = {x ∈ C: |f| R}, g = f A and h = f −f A. It is now a simple exercise to prove that g, h and C satisfy the conditions stated in

the lemma. Remark 7.2. Let us consider the following scenario: a measurable set E ⊆ and a measurable function F : E×S2 → C that satisﬁes F ∈ L2(E×S2), Frσ∗Frσ L2( 3) δ2S2 Fr 2L2(S2) > 0 for all r ∈ E, where Fr(x) = F(r,x), (r,x) ∈ E × S2. Applying

- Lemma 7.1 to Fr for each r ∈ E generates caps Cr ⊆ S2 and functions Gr and Hr, and in this way functions G,H : E × S2 → C, which a priori may not be measurable in the product space E × S2. This can be overcome if we are careful with the choice of the caps as we now proceed to explain. For a collection of spherical caps {Cr}r∈E satisfying (7.10) with C = Cr and f = Fr, for all r ∈ E, denote


- G0 = {(r,x): r ∈ E, x ∈ Cr},
- G1 = (r,x) ∈ G0: |Fr(x)| 12c0δ1/γ|Cr|1/2 Fr L2(S2)


−1 . Then, as explained following (7.10), we can take G = F G

### and H = F − F G

. We need to argue that we can have G0 and G1 measurable, by choosing the collection {Cr}r∈E appropriately. When r ∈ E, then supk,j Λk,j(Fr) 2c(δ), for some universal constant c(δ). The cap Cr = Cjk is to be chosen so that Λk,j(Fr) c(δ), that is,

1

1

|Cr|−1/2

|Fr|dσ c(δ) Fr L2(S2).

Cr

The set of caps {Cjk : k,j} in S2 is parametrized by indices k and j where k ∈ and j ∈ {1,2,...,Jk}, for some Jk < ∞. Let Z = {(k,j): k ∈ , j ∈ {1,...,Jk}} and deﬁne the function Θ: E × Z → by

Θ(r,k,j) = |Cjk|−1/2 Fr −L21(S2)

|Fr|dσ. By Fubini’s theorem, for each ﬁxed (k,j) ∈ E × Z, Θ(·,k,j) is a measurable

Cjk

function. By assumption, for each r ∈ E, supk,j Θ(r,k,j) 2c(δ). We want to ﬁnd a measurable function τ : E → Z such that

Θ(r,k,j) − c(δ) c(δ),

Θ(r,τ(r)) sup

k,j

a so called c(δ)-maximizer. That this is possible is a consequence of measurable selection theorems, see for instance [35, Theorem 4.1].

For such a measurable selection function τ write τ(r) = (k(r),j(r)) ∈ Z, then the function E → S2, r  → ykj((rr)), is measurable and we can write G0 = {(x,r) : r ∈ E,|x − ykj((rr))| 2−k(r)+1}. We can therefore assume that the sets G0 and G1 are measurable sets in E × S2, so that G and H are measurable functions. In this way, we have the following lemma.

- Lemma 7.3. Let E ⊆ be a measurable set and F : E × S2 → C be a measurable

function satisfying F ∈ L2(E × S2), Frσ ∗ Frσ L2( 3) δ2S2 Fr 2L2(S2) > 0 for all r ∈ E, where Fr(x) = F(r,x), (r,x) ∈ E × S2. Then, there are spherical caps {Cr}r∈E and measurable functions G,H satisfying: F = G + H, G and H have disjoint supports, 0 |G|,|H| |F|, and for all r ∈ E:

|Gr(x)| Cδ Fr 2|Cr|−1/2 Cr

(x), x ∈ S2 and Gr 2 ηδ Fr 2.

We now prove a slight improvement of Lemma 7.1 that adds one more restriction to the function g. It tells us that we can replace a δ-quasi-extremal for the sphere for a better controlled one at the expense of powers of δ.

- Lemma 7.4. For any δ > 0 there exists Cδ > 0, ηδ > 0 and λδ > 0 with the


following property. If f ∈ L2(S2) satisﬁes fσ ∗ fσ 2 δ2S2 f 22 then there exist a decomposition f = g + h and a spherical cap C satisfying (7.6), (7.7), (7.8), 7.9 and

gσ ∗ gσ 2 λδS2 f 22. (7.11)

Moreover (7.8), (7.9) and (7.11) hold with constants that satisfy Cδ δ−1/γ, ηδ δ1+1/γ and λδ δ6+4/γ, where γ > 0 is a universal constant.

- Remark 7.5. It is not diﬃcult to see (e.g. [32, Lemma 6.2]) that for a function g satisfying (7.8) and (7.9) there is a lower bound for the L1 norm of the form


|g|dσ

C

ηδ2 Cδ

f 2|C|1/2. (7.12)

Note that the sharp estimate (7.1) for S2 implies that for g satisfying (7.11) we have

S g 2 gσ ∗ gσ 2 1/2 λδ1/2S f 2, so that

g L2(S2) λδ1/2 f L2(S2). (7.13)

- Proof of Lemma 7.4. Take Cδ and ηδ as in the conclusion of Lemma 7.1. We claim that the lemma at hand holds with respective constants Cδ, δηδ/√2 and λδ =


(δ3ηδ2/8)2. To see this we employ a decomposition algorithm, reminiscent of that in [9, Section 8, step 6A], deﬁned in the following inductive way.

Let G0 = f and f0 = 0 and suppose that for N 0 we have deﬁned GN and fk, for 0 k N, satisfying:

f = GN + f0 + ··· + fN, (7.14) supp(GN),supp(f0),...,supp(fN) are pairwise disjoint, (7.15)

- 1

- 2


δ2S2 f 22. (7.16)

GNσ ∗ GNσ 2

The previous conditions are satisﬁed if N = 0. We now deﬁne the inductive step of the algorithm. If (7.14), (7.15) and (7.16) hold for N we deﬁne GN+1 and fN+1 in the following way.

Given that GNσ ∗ GNσ 2 12δ2S2 f 22 12δ2S2 GN 22 we can apply Lemma 7.1 to GN to obtain a decomposition GN = gN + hN and a cap CN. Deﬁne GN+1 = hN and fN+1 = gN. The functions GN+1 and fN+1 therefore have disjoint supports and satisfy

|fN+1(x)| Cδ GN 2|CN|−1/2 CN

(x) Cδ f 2|CN|−1/2 CN

(x) for all x, (7.17) fN+1 2 ηδ GN 2

1 √2

ηδδ f 2, (7.18) where the second inequality in (7.18) follows as in (7.13).

The algorithm terminates at N 1 when either fNσ ∗ fNσ 2 λδS2 f 22 or

GNσ ∗ GNσ 2 < 12δ2S2 f 22. In the former case we say the algorithm stops in a win and set g = fN, h = GN + f0 + ··· + fN−1, C = CN and the Lemma is proved.

Let Nδ := 2ηδ−2δ−2 . We claim that the algorithm stops in a win for some N Nδ. We ﬁrst show that the algorithm can not run for more than Nδ steps, otherwise, using

- (7.18) we have


f 2

Nδ+1

k=1

fk 22

1/2 1 √2

(Nδ + 1)1/2ηδδ f 2 > f 2,

which is impossible.

Second, we show that if the algorithm has not stopped in a win during the ﬁrst N steps for some N 2Nδ, then we can perform the step N + 1. More precisely, if

fkσ∗fkσ 2 < λδS2 f 22 for all 1 k N, for some N 2Nδ, then GNσ∗GNσ 2

- 1

- 2δ2S2 f 22. Indeed, using Plancherel’s theorem and then the triangle inequality we obtain


N

GNσ ∗ GNσ 12/2 fσ ∗ fσ 2 1/2 −

fkσ ∗ fkσ 2 1/2 δS f 2 − Nλδ1/2S f 2

k=1

(δ − 2Nδλδ1/2)S f 2 δS f 2.

- 1

- 2


If follows that the algorithm stops in a win for some N Nδ. This ﬁnishes the proof.

The next topic we review is that of ”weak interaction between distant caps”. For spherical caps C, C ⊆ S2 there is a notion of distance. Let (y,a), (y ,a ) ∈ S2×(0,∞) denote the centers and radii of the spherical caps C, C ,

C = {x ∈ S2: |x − y| a}, C = {x ∈ S2: |x − y | a }. The distance between C and C is deﬁned by the expression

(C,C ) = min(d(C,C ),d(C,−C )), (7.19) where, as in [27], we can take d to be the hyperbolic distance between (y,a) and

- (y ,a ) in the upper half space model, that is 4


(a − a )2 + |y − y |2 2aa

d(C,C ) = arccosh 1 +

. The following lemma quantiﬁes the notion of weak interaction between distant caps.

- Lemma 7.6 ([9, Lemma 7.6]). For any ε > 0 there exists ρ < ∞ such that Cσ ∗ C σ L2( 3) < ε|C|1/2|C |1/2, whenever (C,C ) > ρ.

An inspection of the proof of the previous statement in [9, Lemma 7.6] shows that an analog result holds if we have caps C ⊆ S2r and C ⊆ S2t, with r, t ∈ [1,2], that is, denoting 1rC the rescale of C to S2,

1

rC = {x ∈ 3: rx ∈ C}, we have the following lemma.

- Lemma 7.7. Let r,t ∈ [1,2], C ⊆ S2r and C ⊆ S2t. Then for any ε > 0 there exists ρ < ∞ such that Cσr ∗ C σt L2( 3) < ε|C|1/2|C |1/2, whenever (1rC, 1tC ) > ρ.


8. Lifting to the hyperboloid the inequality for the sphere

The aim of this section is to use the Tomas–Stein inequality for the sphere S2 to obtain qualitative properties of δ-quasi-extremals for the hyperboloid. The connection here between the hyperboloid and the sphere is that the latter corresponds to horizontal traces of the former. This connection between the adjoint Fourier restriction operator on a hypersurface and on its traces appears, for instance, in the work of Nicola [26]. An alternative approach to the methods in this section can be developed using reﬁned bilinear estimates, but we choose to give a diﬀerent argument. The main result of this section is the following lemma.

4We point out that for the two lemmas that follow we don’t need d to be a distance. It would be perfectly ﬁne to consider instead the expression

(a − a )2 aa

+ |y − y |2 a2

+ |y − y |2 (a )2

,

so that caps are far apart if either a/a or a /a is large or the distance from y to y is much larger than either a or a .

- Lemma 8.1. Let 0 s 12. For any δ > 0 there exists Cδ > 0, ηδ > 0 and νδ > 0 with the following property. If f(x,t) ∈ L2(Hs3) supported where 1 |x| 2 satisﬁes


fµs∗fµs L2( 4) δ2H24 f 2L2 then there exist a decomposition f = g+h, a spherical cap C ⊆ S2 and a cap C = [1,2] × C ⊂ Hs3 satisfying

0 |g|,|h| |f|, (8.1) g,h have disjoint supports, (8.2) supp(g) ⊆ C, (8.3) |g(x,t)| Cδ f L2µs(C)−1/2 C(x,t) for all (x,t), (8.4)

g L2 ηδ f L2, (8.5) g L1 νδµs(C)1/2 f L2. (8.6)

The constants Cδ, ηδ and νδ are uniform in s 12.

- Remark 8.2. The previous lemma is equivalent to the analog result for H3s. Indeed, that the result for H3s implies a similar one for Hs3 is immediate. On the other direction, if f ∈ L2(H3s) is a δ-quasi-extremal for (1.9), that is


Tsf 4L4( 4) = (2π)4 fµ¯s ∗ fµ¯s 2L2( 4) (2π)4δ4H44 f 4L

2(H3s), then, writing f = f+ + f− so that Tsf = Tsf+ + Tsf−(·,−·) and f 2L

2(H3s) = f+ 2L2(H3

s) + f− 2L2(H3

s) we obtain that

f µs ∗ f µs 2L2( 4) 2−4δ4H44 f 4L2(Hs3) for = + or for = −, so that if both f+ 2L2(H3

2(H3s) and f− 2L2(H3

s) δ2 f 2L

s)

δ2 f 2L

2(H3s), then we obtain the conclusions in Lemma 8.1 for f from the ones for f+ or f−, as it corresponds. On the other hand, if say f− 2L2(H3

s) < δ2 f 2L

2(H3s), then f+ 2L2(H3

s) (1 − δ2) f 2L

2(H3s) and Tf+ L4 Tf L4 − Tf− L4 2πδ(H4 − H4) f L

2(H3s) cδH4 f+ L2(Hs3), so that Lemma 8.1 applied to f+ yields the result for f.

The support condition 1 |x| 2 can be changed to a |x| b for any a s and b < ∞, understanding that the implicit constants may depend on a,b. We can alternatively state the previous lemma for f ∈ L2(H3) supported where 2N |x| 2N+1, N 1, the implicit constants independent of N, as can be easily checked by the use of scaling.

Recall that we write ψs(r) = √r2 − s2 {r s} and φs(t) = ψs−1(t) = √t2 + s2 {t 0} and for f ∈ S( 3) and r > 0 we denote by fσr the measure supported on S2r := {y ∈

3 : |y| = r} given by

fσr,ϕ =

f(ry)ϕ(ry)r dσ(y).

S2

We denote fr the function x  → f(rx), which we consider as a function from S2 to C.

In the next lemma we show that we can write the double convolution of functions on the hyperboloid Hs3 as an integral of convolutions of sliced spheres.

- Lemma 8.3. Let s 0. For f,g ∈ L2(Hs3) we have the representation formula


t

s(t ) ∗ gσφ

fµs ∗ gµs (x,t) =

fσφ

s(t−t ) (x)dt , (8.7)

0

for a.e. (x,t) ∈ 3 × +. Proof. Let ϕ ∈ Cc∞( 4). Using spherical coordinates we have

dxdy |x|2 − s2 |y|2 − s2

fµs ∗ gµs,ϕ =

ϕ(x + y,ψs(x) + ψs(y))f(x)g(y)

|x|,|y| s

∞

∞

r2r 2 dω dω dr dr √r2 − s2√r 2 − s2

=

ϕ(rω + r ω ,ψs(r) + ψs(r ))f(rω)g(r ω )

.

s S2 S2

s

We change variables (r,r )  → (u,u ) = (ψs(r),ψs(r )) = (√r2 − s2,√r 2 − s2) and obtain

∞

∞

fµs ∗ gµs,ϕ =

ϕ(φs(u)ω + φs(u )ω ,u + u )

0 S2 S2

0

· f(φs(u)ω)g(φs(u )ω )φs(u)φs(u )dω dω dudu . We change variables (u,u )  → (t,t ) = (u + u ,u) and obtain

∞

t

fµs ∗ gµs,ϕ =

ϕ(φs(t )ω + φs(t − t )ω ,t) · f(φs(t )ω)g(φs(t − t )ω )φs(t )φs(t − t )dω dω dt dt

0 S2 S2

0

∞

t

s(t ) ∗ gσφ

ϕ(x,t) fσφ

s(t−t ) (x)dx dt dt

=

0 3

0

t

s(t ) ∗ gσφ

=

fσφ

s(t−t ) (x)dt ,ϕ , where we used Fubini’s Theorem and that for any r,r > 0, fσr ∗ gσr ,ϕ(·,t) =

0

ϕ(x,t) fσr ∗ gσr (x)dx

3

=

=

ϕ(x + x ,t)f(x)g(x )dσr(x)dσr (x )

S2r×S2s

ϕ(rω + r ω ,t)f(rω)g(r ω )rr dσ(ω)dσ(ω ).

S2×S2

Next, we record a formula for the Lp(Hs3) norm in terms of the Lp norm of the slices.

- Lemma 8.4. Let f ∈ Lp(Hs3). Then


∞

p

f pLp(H3

Lp(S2)φs(t)dt. (8.8) Proof. Using spherical coordinates we have

fφ

s) =

s(t)

0

∞

∞

r2 √r2 − s2

f pLp(H3

|f(rω)|p

|f(φs(t)ω)|pφs(t)dω dt

s) =

dω dr =

s S2

0 S2

∞

p

Lp(S2)φs(t)dt.

fφ

=

s(t)

0

We now analyze the dependence of fσr ∗ gσr L2( 3) in (r,r ). We start with the scaling property of fσr as a function of r. We have

e−irx·yf(ry)r dσ(y) = r( frσ)(rx). Thus

e−ix·yf(y)dσr(y) =

( fσr)(x) =

S2

S2r

fσr L4( 3) = r1/4 frσ L4( 3) (2π)3/4r1/4S fr L2(S2). Then, the Cauchy–Schwarz inequality implies that for any r,r > 0

fσr gσr L2( 3) fσr L4 gσr L4 (2π)3/2S2(rr )1/4 fr L2(S2) gr L2(S2), so that

fσr ∗ gσr L2( 3) S2(rr )1/4 fr L2(S2) gr L2(S2) (8.9) and in particular, when r = r we obtain

fσr ∗ gσr L2( 3) = r1/2 frσ ∗ grσ L2( 3) S2r1/2 fr L2(S2) gr L2(S2). (8.10)

Deﬁnition 8.5. A quasi-cap of Hs3 is a measurable set G ⊆ Hs3 for which there exist E ⊆ and spherical caps Ct ⊆ S2, for t ∈ E, such that

G = {(x,t) ∈ 4 : t ∈ E, x ∈ φs(t)Ct}. (8.11)

We note that a cap is also a quasi-cap; the diﬀerence in a generic quasi-cap is that the spherical caps may not be the same as in the case of a cap, and the set E may not be an interval.

In our main result of the section, Lemma 8.1, we want to obtain an analog of Lemma

- 7.1 for a compact subset of the hyperboloid. The idea is to use the cap Lemma 7.1 for the sphere on horizontal slices of the hyperboloid via (8.7) in a measurable way (recall Remark 7.2), and show that there are enough aligned sliced caps of similar size to obtain a cap for the hyperboloid. We do it for the upper sheet as the full one-sheeted hyperboloid follows from this as already noted in Remark 8.2. The proof of Lemma
- 8.1 is accomplished in the following way. First, we show that on a large subset of t’s


in [ψs(1),ψs(2)] we can apply Lemma 7.4 to the function x ∈ S2  → f(φs(t)x) in a measurable way. This will allow us to prove a version of Lemma 8.1 where instead of a cap we have a quasi-cap. Next, we show that a subset of the quasi-cap of large relative measure is comparable to a cap and satisﬁes the requirements of Lemma 8.1, which then are shown to be satisﬁed by the cap itself. To prove this last point, we

will make use of the quantitative version of the statement that ”distant spherical caps interact weakly” as stated in Lemmas 7.6 and 7.7.

- Proof of Lemma 8.1. In what follows, c(δ) denotes a constant that depends only on δ and is allowed to change from line to line5. Recall from Remark 7.5 that (8.6) can


be obtained from (8.4) and (8.5) with νδ = ηδ2/Cδ.

We ﬁrst argue that we can assume that the support of f(·,t) does not contain antipodal points for each t ∈ [ψs(1),ψs(2)]. We can cover S2 as the union of ﬁnitely many spherical caps {Ck}k=1,...,κ each of radius 14, whose centers form a maximally 4-separated set on S2, and induce a decomposition of Hs3 as the union of the caps {[s,∞) × Ck}k=1,...,κ. By the triangle inequality we can therefore assume that f is supported on the cap [s,∞) × Ck, for some k, at the expense of changing δ by δ/κ. The reason for doing this is to ensure that there are no nearly antipodal spherical caps later on.

- 1


Let us start by noting that for (x,t) in the support of f and s ∈ [0, 12] we have |x| ∈ [1,2] and t = ψs(x) ∈ [ψs(1),ψs(2)] = [√1 − s2,√4 − s2] ⊆ [

√3

2 ,2], and that from Lemma 8.4

ψs(2)

ψs(1)

fφ

s(t)

2

L2(S2) dt f 2L2(Hs3) 2

ψs(2)

ψs(1)

fφ

s(t)

2

L2(S2) dt.

On the other hand (fµs ∗ fµs)(x,t) is supported where 2ψs(1) t 2ψs(2). From

- Lemma 8.3 for a.e. (x,t) ∈ 4 we have


fµs ∗ fµs(x,t) =

ψs(2)

s(t ) ∗ fσφ

(fσφ

s(t−t ))(x)dt , (8.12)

ψs(1)

(recall that φs(τ) = 0 for τ < 0). Let

s(t) L2( 3) γ2δ2H24S2 fφ

2

s(t) ∗ fσφ

fσφ

2, fφ

s(t)

Eγ = t ∈ [ψs(1),ψs(2)]:

s(t) 2 γδH4 f 2 and

Eγ,λ = t ∈ [ψs(1),ψs(2)]:

s(t) L2( 3) γ2δ2H24S2 fφ

2

s(t) ∗ fσφ

2, λδH4 f 2 fφ

fσφ

s(t)

s(t) 2 γδH4 f 2

.

s(t) 2 = f(φs(t)·,t) L2(S3), while f 2 = f L2(Hs3). We claim that |Eγ|

Here, fφ

c(δ) and |Eγ,λ| c(δ) if γ and λ are chosen small and large enough depending on δ, respectively. Let us ﬁrst analyze |Eγ|. From (8.12), using Fubini’s theorem and

5Reviewing the argument one can see that such constants can be taken to depend only on powers, positive and negative, of δ.

Minkowski’s integral inequality we have

δ2H24 f 22

ψs(2)

+

- ψs(1)

(fσφ

s(t ) ∗ fσφ

s(t−t ))(x)dt

L2t,x

- ψs(2)


ψs(1)

ψs(2)

ψs(1)

s(t ) ∗ fσφ

fσφ

s(t−t ) L2x E γ(t )dt

L2t

s(t ) ∗ fσφ

(fσφ

s(t−t ))(x) E

γ

### (t )dt

.

L2x,t

Plancherel’s theorem and the Cauchy–Schwarz inequality give fσφ

1/2

1/2

s(t ) ∗ fσφ

s(t ) ∗ fσφ

s(t−t ) ∗ fσφ

L2x , so that using the sharp estimate for fσφ

s(t−t ) L2x fσφ

L2x fσφ

s(t−t )

s(t )

s(t−t ) ∗ fσφ

s(t−t ) L2x as in (8.10), recalling that φs(t ), φs(t − t ) ∈ [1,2], we obtain

ψs(2)

s(t ) ∗ fσφ

fσφ

s(t−t ) L2x E γ(t )dt

L2t

ψs(1)

ψs(2)

2γδH4S2

fφ

s(t ) 2 fφ

s(t−t ) 2 dt

L2t

ψs(1)

ψs(2)

+ 2γδH4S2 f 2

fφ

s(t−t ) 2 dt

L2t

ψs(1)

8γδH4S2 f 22. Therefore, choosing γ = δH4/(16S2) we obtain

ψs(2)

- 1

- 2


δ2H24 f 22. For this choice of γ we then obtain δ2H24 f 22

s(t ) ∗ fσφ

### (t )dt

(fσφ

s(t−t ))(x) E

γ

L2x,t

ψs(1)

ψs(2)

- 1

- 2


- ψs(1)

(fσφ

s(t ) ∗ fσφ

s(t−t ))(x) E

γ

(t )dt

L2x,t

- ψs(2)


s(t ) ∗ fσφ

fσφ

s(t−t ) L2x Eγ(t )dt

L2t

ψs(1)

ψs(2)

2S2

s(t ) L2x fφ

s(t−t ) L2x Eγ(t )dt

fφ

L2t

ψs(1)

ψs(2)

L2x dt 2S2 f 22|Eγ|1/2, and therefore |Eγ| H44δ4/(16S4).

2

2S2|Eγ|1/2

fφ

s(t)

ψs(1)

To analyze |Eγ,λ| we use Eγ,λ = Eγ ∩ {t ∈ [ψs(1),ψs(2)] : fφ

s(t) 2 λδH4 f 2}.

Chebyshev’s and H¨older’s inequalities imply

- 1

λδH4 f 2

ψs(2)

ψs(1)

fφ

s(t) 2 dt

- 2


|{t ∈ [ψs(1),ψs(2)] : fφ

s(t) 2 > λδH4 f 2}|

.

λδH4

Therefore, choosing λ = 64S4/(H54δ5) we obtain |Eγ,λ| |Eγ| − |{t ∈ [ψs(1),ψs(2)] : fφ

H44 32S4

δ4.

s(t) 2 > λδH4 f 2}|

From now on, let us ﬁx such values of γ and λ and let E := Eγ,λ. From the deﬁnition of E and (8.10), we have that for t ∈ E

s(t)σ L2( 3) cφs(t)−1/2δ4 fφ

2

s(t)σ ∗ fφ

L2(S2), so that Lemma 7.1 imply that for t ∈ E there are caps Ct ⊆ S2 and a decomposition

fφ

s(t)

- fφ

s(t) = Gφ

s(t) + Hφ

s(t). In this way we obtain a decomposition f = g + h, where

- g(φs(t)x,t) = Gφ


s(t)(x) E(t), x ∈ S2, t ∈ [ψs(1),ψs(2)]. As argued in Remark 7.2 and recorded in Lemma 7.3, by using a measurable selection theorem we can perform this decomposition in such a way that g and h are measurable functions and G0 := {(x,t) ∈ 4 : t ∈ E, x ∈ φs(t)Ct} is a measurable subset of Hs3, so that G0 is a quasicap. According to Lemma 7.1, g and h satisfy the following conditions: f = g + h, 0 |g|,|h| |f|, g and h have disjoint supports, g(x,t) = 0 if t ∈/ E,

s(t) 2|Ct|−1/2 Ct

(x), for all t ∈ E, x ∈ S2, gφ

|g(φs(t)x,t)| Cδ fφ

ηδ2 Cδ|Ct|1/2 fφ

s(t) 2, for all t ∈ E. (8.13) Note that Lemma 8.4 and (8.13) imply

s(t) 2 ηδ fφ

s(t) 2, gφ

s(t) 1

g 2 ηδ f 2. Given that for t ∈ E we have δ2H4 f 2 fφ

s(t) 2 δ−4H4 f 2 we conclude, possibly by changing the constants that depend on δ, that the function g satisﬁes

|g(φs(t)x,t)| Cδ f 2|Ct|−1/2 Ct

(x) E(t), for all t ∈ [ψs(1),ψs(2)], x ∈ S2 (8.14) and

ηδ2 Cδ|Ct|1/2 f 2, for each t ∈ E. (8.15)

gφ

s(t) L2(S2) ηδ f 2 and gφ

s(t) L1(S2)

Summing up, we can restate what has been done so far in the following way: If f ∈ L2(Hs3) satisﬁes fµs ∗ fµs 2 δ2H24 f 22 and is supported where 1 |x| 2 then there exist a decomposition f = g + h, a set E ⊆ [ψs(1),ψs(2)] satisfying |E| δ4 and a quasi-cap G0 (associated to E as in (8.11)) such that g and h have disjoint supports,

|g(x,t)| Cδ f 2|Ct|−1/2 G0

(x,t), for all (x,t) ∈ Hs3 and (8.15) holds. This is the analog of Lemma 8.1 with a quasi-cap instead of a cap.

Using the quasi-cap analog of Lemma 8.1, as described in the previous paragraph, we can argue exactly as in Lemma 7.4 for the sphere to ensure, possibly after changing the constants that depend on δ, that there exist a quasi-cap, which we continue to denote G0, associated to a set E ⊆ [ψs(1),ψs(2)] with |E| δ4, and functions g and h with the properties of the previous paragraph and additionally

gµs ∗ gµs L2( 4) cδ f 22. (8.16)

The next and ﬁnal step is to show that the caps Ct, t ∈ E, which deﬁne G0 are aligned for a large fraction of the t’s, and by this we mean that they have close radii and centers, up to powers of δ.

Recall that for caps C, C ⊆ S2 there is a distance function (C,C ), deﬁned in

- (7.19), that is relevant in Lemmas 7.6 and 7.7. For ρ > 0 deﬁne


Aρ = {(t,t ) ∈ E × E: (Ct,Ct ) ρ}. Then, starting from (8.16) we have the estimate

ψs(2)

cδ f 22 gµs ∗ gµs 2 =

s(t ) ∗ gσφ

(gσφ

s(t−t ))(x)dt

L2x,t ψs(2)

ψs(1)

s(t ) ∗ gσφ

s(t−t ) L2x Aρ(t ,t − t )dt

gσφ

L2t

ψs(1)

ψs(2)

s(t ) ∗ gσφ

s(t−t ) L2x A ρ(t ,t − t )dt

gσφ

+

L2t ψs(2)

ψs(1)

+ Cδ2 f 22

s(t ) ∗ gσφ

s(t−t ) L2x Aρ(t ,t − t )dt

gσφ

L2t

ψs(1)

ψs(2)

|Ct |−1/2

ψs(1)

· |Ct−t |−1/2 φs(t )Ct σφ

s(t ) ∗ φs(t−t )Ct−t σφ

s(t−t ) L2x (E×E)∩A ρ(t ,t − t )dt

L2t ψs(2)

cδ 2

f 22,

s(t ) ∗ gσφ

s(t−t ) L2x Aρ(t ,t − t )dt

+

gσφ

L2t

ψs(1)

where in the second to last line we used (8.14) and the last line holds if ρ is large enough as a function of6 δ, by the use of Lemma 7.7. For such choice of ρ we can therefore ensure that

ψs(2)

ψs(1)

s(t ) ∗ gσφ

s(t−t ) L2x Aρ(t ,t − t )dt

gσφ

L2t

cδ 2

f 22. (8.17)

6From the proof of Lemma 7.6 in [9] one can see that coshρ can be taken to be a power of δ−1.

s(t) 2 Cδ f 2 for all t ∈ E. This and (8.17) imply that

Note that (8.14) implies gφ

ψs(2)

cδ 2

f 22 2S2

s(t−t ) 2 Aρ(t ,t − t )dt

gφ

s(t ) 2 gφ

L2t

ψs(1)

ψs(2)

2S2Cδ2 f 22

Aρ(t ,t − t ) L2

dt

t

ψs(1)

4S2Cδ2 f 22 |Aρ|1/2,

where ρ = ρ(δ) is the already ﬁxed function of δ and |Aρ| denotes the Lebesgue measure of Aρ ⊆ 2. As |Aρ| 2 we conclude that |Aρ| c(δ). By Fubini’s theorem, the ﬁbers Aρ(t) := {t ∈ E : (t,t ) ∈ Aρ} = {t ∈ E : (Ct,Ct ) ρ} are a.e. measurable, the function t ∈ E  → |Aρ(t)| = |{t ∈ E : (Ct,Ct ) ρ}| is measurable and |Aρ| 2esssupt∈E |Aρ(t)|. We then obtain the following estimate

|{t ∈ E : (Ct,Ct ) ρ}| sup

|{t ∈ E : (C(y,a),Ct ) ρ}|,

c(δ) esssup

(y,a)∈S2×(0,∞)

t∈E

from where we conclude the existence of a spherical cap C(y0,a0) such that |{t ∈ E : (C(y0,a0),Ct) ρ}| c(δ).

Denote C0 = C(y0,a0) and Bρ = {t ∈ E : (C0,Ct) ρ}. For t ∈ Bρ, the radii and the distance between the centers of the caps C0 and Ct are of the same order modulo powers of δ. More precisely, if we let (y,a) denote the center and radius of a cap Ct, t ∈ Bρ, then the deﬁnition of the distance function ensures that

c(δ)a0 a c (δ)a0, and |y0 − y| c (δ)a0. (8.18) This is the only place where we used the assumption that f is supported on a cap [1,2] × C, were the radius of C is 41, because this implies that the centers of the caps associated to gφ

s(t), t ∈ E, can be chosen to be at distance at most 12 from each other and therefore any two caps Ct, Ct for t, t ∈ E are not nearly antipodal.

From (8.18) we conclude that for t ∈ Bρ we have |Ct| δ |C0| and there exists c(δ) 1 such that the c(δ)-enlargement of C0, denoted Cδ0 and deﬁned by

Cδ0 := {x ∈ S2: |x − y0| c(δ)a0},

contains Ct for all t ∈ Bρ, and hence the cap C := [1,2] × Cδ0 ⊆ Hs3 contains the quasi-cap G1 := {(x,t) ∈ G0: t ∈ Bρ}. Note also that |Ct| δ |Cδ0|, for all t ∈ Bρ.

s(t)|dσ c(δ)|Ct|1/2 f 2,

Now, for each t ∈ E, gφ

|gφ

s(t) is supported on Ct and C

t

- as stated in (8.15). If in addition t ∈ Bρ, then


|gφ

s(t)|dσ =

Cδ0

s(t)|dσ c(δ)|Ct|1/2 f 2 c (δ)|Cδ0|1/2 f 2,

|gφ

Ct

and so integrating in t ∈ Bρ and using that φs(t) 1 if t ψs(1) gives

s(t)|φs(t)dσ dt c(δ)|Cδ0|1/2|Bρ| f 2 c (δ)|Cδ0|1/2 f 2.

|gφ

Bρ Cδ0

Given that µs(C) = µs([1,2] × Cδ0) |Cδ0| we obtain

s(t)|φs(t)dσ dt c(δ)µs(C)1/2 f 2. Then g G

|g G

1|dµs =

|gφ

Bρ Cδ0

C

) ⊆ G1 ⊆ C, G1 ⊆ G0, |Ct| δ µs(C) for all t ∈ Bρ, and thus

### , f − g G

### and C satisfy all of our requirements, given that supp(g G

1

1

1

### (x,t) c(δ) f L2(Hs3)µs(C)1/2 C(x,t), for all (x,t), g G

g G

1

1 L2(Hs3) c(δ) f L2(Hs3), g G

1 L1(Hs3) c(δ)µs(C)1/2 f L2(Hs3).

9. A concentration-compactness lemma

The result of this section is stated for H3s but a similar statement and proof also hold for Hs3.

- Lemma 9.1. Let {ρn}n be a sequence in L2(H3s) satisfying


|ρn|2 d¯µs = λ, where λ > 0 is ﬁxed. Then there exists a subsequence {ρn

H3s

k|2}k satisﬁes one of the following three possibilities:

k}k such that {|ρn

- (i) (compactness) there exists k ∈ such that

∀ε > 0, ∃R < ∞,

s2 k−R |y| s2 k+R

|ρn

k|2 d¯µs λ − ε;

- (ii) (vanishing) lim

k→∞

sup

∈ s2 −R |y| s2 +R

|ρn

k|2 d¯µs = 0, for all R < ∞;

- (iii) (dichotomy) There exists α ∈ (0,λ) such that for all ε > 0, there exist R ∈ , k0 1 and nonnegative functions ρk,1,ρk,2 ∈ L2(H3s) satisfying for k k0:


k − (ρk,1 + ρk,2) L

ρn

2(H3s) ε, (9.1)

|ρk,2|2 d¯µs − (λ − α) ε, (9.2) supp(ρk,1) ⊆ {y ∈ 3: s2

|ρk,1|2 d¯µs − α ε,

H3s

H3s

k−R |y| s2

k+R}, (9.3) supp(ρk,2) ⊆ {y ∈ 3: |y| s2

k−Rk} ∪ {y ∈ 3: |y| s2

k+Rk}, (9.4) for certain sequences { k}k and {Rk}k, where Rk → ∞ as k → ∞.

Proof. The proof is identical to the proof of Lemma I.1 in [23], by deﬁning the sequence of functions

|ρn(y)|2 d¯µs(y). We omit the details.

Qn: [0,∞) → +, Qn(t) = sup

∈ s2 −t |y| s2 +t

In the forthcoming sections, we will be working with an L2 normalized extremizing sequence {fn}n and will apply the preceding lemma to with λ = 1. We will slightly abuse notation and say that {fn}n satisﬁes either concentration, vanishing or dichotomy, when the sequence {|fn|2}n satisﬁes the respective alternative.

10. Bilinear estimates and discarding dichotomy

In this section we show that an extremizing sequence for T can not satisfy the dichotomy condition (iii) of Lemma 9.1. This will be a consequence of bilinear estimates

- at dyadic scales.


- Proposition 10.1. There exists a constant C < ∞ with the following property.


Let s > 0, k,k ∈ and f,g ∈ L2(Hs3) supported where 2ks |y| 2k+1s and

- 2k s |y| 2k +1s respectively. Then


1

Tsf · Tsg L2( 4) C2−

4|k−k | f L2(Hs3) g L2(Hs3). Proof. Without loss of generality we can assume k k. Using Lemma 8.3 we write

t

fµs ∗ gµs(x,t) =

s(t ) ∗ gσφ

s(t−t ))(x)dt , so that by Minkowski’s integral inequality

(fσφ

0

fµs ∗ gµs L2

x,t

t

0

s(t ) ∗ gσφ

fσφ

s(t−t ) L2x dt

L2t

. (10.1)

Recalling (8.9), the right hand side of (10.1) satisﬁes

t

0

s(t ) ∗ gσφ

fσφ

s(t−t ) L2x dt

L4t

t

φs(t )1/4 fφ

s(t ) 2 φs(t − t )1/4 gφ

s(t−t ) 2 dt

C

L2t

0

∞

φs(t )1/4 fφ

s(t ) 2 {t t }(t )φs(t − t )1/4 gφ

C

s(t−t ) 2

0

ψs(2k+1s)

φs(t )1/4 fφ

C φs(t)1/4 gφ

s(t ) 2 dt ,

s(t) 2

L2t

ψs(2ks)

dt

L2t

where in the last line we used the support condition for f. Recalling the support condition for g

φs(t)1/4 gφ

s(t) L2(S2)

ψs(2k +1s)

2

φs(t)1/2 gφ

=

L2t

ψs(2k s)

∞

φs(ψs(2k s)) −1/2

0

= (2k s)−1/2 g 2L2(Hs3),

s(t)

2

L2(S2) dt

φs(t) gφ

s(t)

2

L2(S2) dt

### where in the last line we used Lemma 8.4. Similarly

ψs(2k+1s)

ψs(2k+1s)

1/2

φs(t )1/4 fφ

φs(t )1/2 fφ

2

s(t ) 2 dt

2 dt

s(t )

ψs(2ks)

ψs(2ks)

ψs(2k+1s)

1/2

·

1dt

ψs(2ks)

(2ks)−1/4(ψs(2k+1s) − ψs(2ks))1/2 f L2(Hs3) (2ks)−1/4(2ks)1/2 f L2(Hs3)

= (2ks)1/4 f L2(Hs3). We conclude that

t

2k/4 f L2(Hs3)2−k /4 g L2(Hs3)

s(t ) ∗ gσφ

fµs ∗ gµs L2

fσφ

s(t−t ) L2x dt

x,t

L4t

0

1

= 2−

4|k −k| f L2(Hs3) g L2(Hs3).

- Proposition 10.2. Let f,g ∈ L2(H3) and suppose that their supports are separated in the sense that there exist k,k ∈ , k k , such that supp(f) ⊆ {|y| 2k} and supp(g) ⊆ {|y| 2k }. Then


1

4|k−k | f L2(H3) g L2(H3).

Tf · Tg L2( 4) C2−

Similarly, if there exist k,R,R ∈ , R R , such that supp(f) ⊆ {2k−R |y| 2k+R} and supp(g) ⊆ {|y| 2k−R } ∪ {|y| 2k+R }, then

1

Tf · Tg L2( 4) C2−

4|R−R | f L2(H3) g L2(H3).

Proof. We decompose f = m∈ fm and g = m ∈ gm where fm,gm are supported where 2m |y| 2m+1, m 0. Then

Tf · Tg L2( 4) =

Tfm · Tgm

m,m

L2

m,m

Tfm · Tgm L2

m,m

1

2−

4|m−m | fm L2 gm L2

1 4|k −k+1|

1

= 2−

2−

4|m−m | fm+k−1 L2 gm +k L2

m 0,m 0

1

C2−

4|k −k| f L2(H3) g L2(H3). The second part of the proposition follows from the ﬁrst and the triangle inequality.

Decomposing a function f ∈ L2(H3) as the sum of a function f+ ∈ L2(H3) and f− ∈ L2(−H3), f = f+ + f−, using that Tf(·,·) = Tf+(·,·) + Tf−(·,−·) and the triangle inequality we can obtain a statement analog to the previous proposition for

functions on the full one-sheeted hyperboloid H3: if f,g belong to L2(H3) and satisfy for some k,R,R ∈ , R R :

supp(f) ⊆ {2k−R |y| 2k+R}, supp(g) ⊆ {|y| 2k−R } ∪ {|y| 2k+R }, then

1

Tf · Tg L2( 4) C2−

4|R−R | f L

2(H3) g L

2(H3). (10.2)

- Proposition 10.3. An extremizing sequence for the adjoint Fourier restriction inequality (1.9) on H3 does not satisfy dichotomy.


Proof. Let us argue by contradiction. Let {fn}n be an extremizing sequence such that {|fn|2}n satisﬁes condition (iii), dichotomy, in Lemma 9.1. Let ε > 0 be given and fn,1,fn,2, n0 be as in the conclusion of the dichotomy condition. Then, for n n0

Tfn − Tfn,1 − Tfn,2 L4 H4 fn − (fn,1 + fn,2) L2 H4 ε, therefore

Tfn L4 H4 ε + T(fn,1 + fn,2) L4, (10.3) Expanding, using Proposition 10.2 (or the comment thereafter) and the support condition for fn,1 and fn,2 as in (9.1)–(9.4), there exists C < ∞ independent of ε such that for all n large enough

T(fn,1 + fn,2) 4L4 = (T(fn,1 + fn,2))2 2L2 = (Tfn,1)2 + 2Tfn,1 · Tfn,2 + (Tfn,2)2 2L2

= Tfn,1 4L4 + Tfn,2 4L4 + 2 (Tfn,1)2,(Tfn,2)2

+ 4 (Tfn,1)2,Tfn,1 · Tfn,2 + 4 (Tfn,2)2,Tfn,1 · Tfn,2

Tfn,1 4L4 + Tfn,2 4L4 + ε. H44 fn,1 42 + H44 fn,2 42 + ε H44(α2 + (1 − α)2) + Cε,

so that using (10.3) and taking n → ∞ we ﬁnd that for any ε > 0

H44 H44(α2 + (1 − α)2) + Cε, for some constant C < ∞ independent of ε.

We conclude 1 α2 + (1 − α)2. We reach a contradiction since α ∈ (0,1) and the numerical inequality α2 + (1 − α)2 < 1 holds.

The proof we just gave to discard dichotomy can be seen in the context of the strict superaditivity condition as proposed by Lions [23, Section I.2]; see for instance the comment at the end of Appendix A in [29].

11. Dyadic refinements and discarding vanishing

In this section we prove a dyadic improvement of the L2 → L4 inequality (1.3) that will imply that extremizing sequences for T do not satisfy the vanishing condition (ii) of Lemma 9.1. We start with the following proposition.

Proposition 11.1. There exists a constant C < ∞ with the following property. Let f ∈ L2(H3) and for k ∈ let fk(y) = f(y) {2k |y|<2k+1}. Then

1/3

fk 3L

Tf L4( 4) C

. (11.1)

2(H3)

k 0

Proof. We follow [32, Proof of Proposition 3.4]. We have Tf 3L4( 4) = Tf·Tf·Tf L4/3 =

Tfk·Tfl·Tfm

L4/3

k,l,m

k,l,m

Tfk·Tfl·Tfm L4/3.

Fix a triplet (k,l,m). We can assume without loss of generality that |k − l| = max{|k − l|,|k − m|,|l − m|} so that the use of Ho¨lder’s inequality and Proposition

- 10.1 give


Tfk · Tfl · Tfm L4/3 Tfk · Tfl L2 Tfm L4 2−

- 1

4|k−l| fk L2 fl L2 fm L2

- 2−|k−l|/122−|k−m|/122−|l−m|/12 fk L2 fl L2 fm L2.


We conclude that Tf 3L4( 4)

2−|k−l|/122−|k−m|/122−|l−m|/12 fk L2 fl L2 fm L2.

k,l,m

Applying H¨older’s inequality to the last estimate we obtain Tf 3L4( 4)

2−|k−l|/122−|k−m|/122−|l−m|/12 fk 3L2

k,l,m

k

fk 3L2.

As an application we have the following corollary.

Corollary 11.2. There exists a constant C < ∞ with the following property. Let f ∈ L2(H3) and for k ∈ let fk(y) = f(y) {2k |y|<2k+1}. Then

fk L 1/23(H3) f L 2/23(H3). (11.2) Proof. From Proposition 11.1 we obtain

Tf L4( 4) C sup

k∈

Tf L4( 4) C

k 0

fk 3L2(H3)

1/3

### = C

k 0

fk 1L/23(H3)

fk 2L2(H3)

C sup

k∈

k 0

fk 1L/23(H3) f 2L/23(H3). The same previous argument and (10.2) gives Tf L4( 4) sup

### = C sup

k∈

fk 1/3

L2(H3)

k∈

fk L2(H3) · fk 2L2(H3)

1/3

1/3

f 2/3

. (11.3)

L2(H3)

and thus it is immediate that for an extremizing sequence for T the vanishing alternative does not hold.

Proposition 11.3. Extremizing sequences for the adjoint Fourier restriction inequality (1.9) on H3 do not satisfy vanishing.

12. Convergence to the cone

The content of this section is important in the study of the compactness alternative of Lemma 9.1, in the case in which, in addition, the extremizing sequences concentrate at inﬁnity.

Formally, we can write Γ3 = H03, σc = µ0 and Tc = T0. It is natural then to study relationships between the adjoint Fourier restriction operator on cone (Γ3,σc) and on each member of the family {(Hs3,µs)}s>0, in the limit s → 0+, and this is the content of this section (see also [22, Lemma 2.9] for related results for the case of the two-sheeted hyperboloid).

Note that if 0 t s and |y| s, then the inequality |y|2 − s2 |y|2 − t2 implies that for f ∈ L2(µs)

f {|y| s} L2(σc) f {|y| s} L2(µt) f L2(µs), and for f ∈ L2(µs), extended to be zero in the region where |y| s, lim

f L2(µt) = f L2(σc). Throughout this section we will commonly encounter the situation of having f ∈

t→0+

L2(Hs3) and regard it as a function in L2(Ht3), 0 t s, via the orthogonal projection to 3 × {0}. In this case, it will be understood that f is extended by zero in the region where7 |y| s.

Let us consider the following situation. Let a > 0, {sn}n ⊂ satisfying sn → 0 as n → ∞. Let {fn}n be a family of functions with fn ∈ L2(Hs3n), supported where |y| a and satisfying supn fn L2(µsn) < ∞. As already noted, fn L2(µsn) fn L2(σc), therefore {fn {|y| s

n}}n is a bounded sequence in L2(σc). We can assume, possibly after passing to a subsequence, that fn f in L2(σc). The aim of this section is to compare fσc ∗ fσc 2 and the limiting behavior of fnµs

n 2, as n → ∞, in the case f = 0. We have some preliminary results.

n ∗ fnµs

- Lemma 12.1. Let a > 0 and f ∈ L2(Hs3) for all small s > 0 and supported where |y| a, then


Tsf − Tcf L4( 4) → 0 as s → 0+.

One possible way to prove Lemma 12.1 can be to follow the outline in the proof of [22, Lemma 2.9 (d)] for which we would need some mixed norm Strichartz estimates, but we try a diﬀerent approach using that we are working with even integers.

Proof of Lemma 12.1. From the uniform in s bound Ts = T and density arguments, it suﬃces to consider the case when f ∈ Cc∞( 3). Let b ∈ (a,∞) be such that the support of f is contained in the region where a |y| b.

7Alternatively, we can think of f as a function living in L2( 3,w dx), for diﬀerent weights w.

By Plancherel’s theorem, to show Tsf → Tf in L4( 4), as s → 0+, it suﬃces to show that fµs ∗ fµs → fσc ∗ fσc and fµs ∗ fσc → fσc ∗ fσc in L2( 4), as s → 0+.

First, we claim that there is pointwise convergence fµs∗fµs(ξ,τ) → fσc∗fσc(ξ,τ) and fµs ∗ fσc(ξ,τ) → fσc ∗ fσc(ξ,τ), a.e. (ξ,τ) ∈ 4, as s → 0+. Indeed, as in the proof of the explicit formula for µs∗µs in Section 3, we can write integral formulas for fµs ∗ fµs, fµs ∗ fσc and fσc ∗ fσc for any s 0. Unwinding the change of variables used in the proof of Proposition 3.1, for ξ = 0 we let

αs(u,v,θ) = |ξ|2 + uv |ξ| (u + v)2 + 4s2

, βs(u,v,θ) = |ξ|2 + uv − s2 |ξ|(u + v)

,

ωs(u,v,θ) = 1 − αs(u,v,θ)2 cosθ, 1 − αs(u,v,θ)2 sinθ,αs(u,v,θ) ,

ϑs(u,v,θ) = 1 − βs(u,v,θ)2 cosθ, 1 − βs(u,v,θ)2 sinθ,βs(u,v,θ) , and

2π

f (u+2v)2 + s2 ωs(u,v,θ) f (u−2v)2 + s2 ωs(u,v,θ) dθ,

Fs(u,v) =

0

2π

f u+2v ϑs(u,v,θ) f (u−2v)2 + s2 ϑs(u,v,θ) dθ,

Gs(u,v) =

0

2π

f v+2v ω0(u,v,θ) f v−2u ω0(u,v,θ) dθ. Recalling the sets Rs(ξ) and Qs(ξ) from (3.2) and (3.7) we have fµs ∗ fµs(ξ,τ) =

H0(u,v) =

0

- 1

- 2|ξ| Rs(ξ)


Fs(u,v)δ τ − v dudv, (12.1)

- 1

- 2|ξ| Qs(ξ)


Gs(u,v)δ τ − v dudv, (12.2)

fµs ∗ fσc(ξ,τ) =

and

|ξ|

- 1

- 2|ξ|


fσc ∗ fσc(ξ,τ) =

H0(u,τ)du {τ |ξ|}(ξ,τ). (12.3)

−|ξ|

Given that Rs(ξ) and Qs(ξ) are explicit, we can spell out (12.1) and (12.2) and integrate the Dirac delta from where it becomes clear that there is a.e. pointwise convergence to fσc ∗ fσc as s → 0+. Alternatively, note that for each ﬁxed ξ = 0,

Rs(ξ)(u,v) → {|u| |ξ| v}(u,v) and Q

s(ξ)(u,v) → {|u| |ξ| v}(u,v) a.e. pointwise as

- s → 0+. We omit further details. By the Dominated Convergence Theorem, to ﬁnish it suﬃces to show that there


exists F ∈ L2( 4) such that |fµs∗fµs(ξ,τ)| F(ξ,τ) and |fµs∗fσc(ξ,τ)| F(ξ,τ), for a.e. (ξ,τ) ∈ 4. We use the inequalities

|fµs ∗ fµs(ξ,τ)|2 f 4L∞ µs ∗ µs 2(ξ,τ), |fµs ∗ fσc(ξ,τ)|2 f 4L∞ µs ∗ σc 2(ξ,τ).

On the supports of fµs ∗ fµs and fµs ∗ fσc, the functions µs ∗ µs and µs ∗ σc are uniformly bounded in s ∈ (0,1), as can be seen from Lemma 3.2 and formula (3.9). It follows that we can take

F(ξ,τ) = 4π f 2L∞ 1 + a−1 {a τ 2b} {|ξ| 2b}(ξ,τ).

Recall the Fourier multiplier notation and the H˙ 1/2( 3) homogeneous Sobolev norm and inner product from (5.1) and (5.2). We have the following lemma.

- Lemma 12.2. Let a > 0, then for each ﬁxed t ∈

lim

s→0

sup

u∈H˙ 1/2( 3) supp(ˆu)⊆{ξ∈ 3:|ξ| a}

eit

√

−∆−s2u − eit

√

−∆u H ˙ 1/2( 3) u H ˙ 1/2( 3)

= 0.

Proof. For any s 0 we have eit

√

−∆−s2u H ˙ 1/2( 3) = u H ˙ 1/2. Now eit

√

|y|2−s2 − eit|y| =

s

0

d dr

eit

√

|y|2−r2 dr = −it

s

0

eit

√

|y|2−r2 r |y|2 − r2

dr. Then,

(eit

√

−∆−s2 − eit

√

−∆)u H ˙ 1/2( 3) |t|

s

0

eit

√

−∆−r2 r

√

−∆ − r2

u ˙

H1/2( 4)

dr

= |t|

s

0

r √

−∆ − r2

u ˙

H1/2( 3)

dr. If 0 s < a and supp(ˆu) ⊆ {|ξ| a}, then

r √

−∆ − r2

u ˙

H1/2( 3)

r √a2 − r2

u H ˙ 1/2( 3), so that

(eit

√

−∆−s2 − e−it

√

−∆)u H ˙ 1/2( 3) |t|(a −

√

a2 − s2) u H ˙ 1/2( 3), and the conclusion follows.

We now address the pointwise convergence of Ts

n

fn to Tcf.

- Lemma 12.3. Let a > 0 and {sn}n be a sequence of positive real numbers converging to zero. Let f ∈ L2(Γ3) and {fn}n be a sequence satisfying fn ∈ L2(Hs3n),


supn fn L2(µsn) < ∞ and supported where |y| a, for all n. Suppose that fn f in L2(Γ3), as n → ∞. Then, as n → ∞

fn(x,t) → Tcf(x,t) for a.e. (x,t) ∈ 4. Proof. Following the argument in the proof of Proposition 5.1, we start by deﬁning vn and v by their Fourier transforms

Ts

n

f(y) |y|

fn(y) |y|2 − s2n

, vˆ(y) =

.

vˆn(y) =

Since supn fn L2(Γ3) supn fn L2(µsn) < ∞ and the functions are supported where |y| a > 0 we see that

a a2 − s2n

|vˆn(y)|2|y|dy sup

vn 2H˙

fn 2L2(µsn) < ∞ and

1/2( 3) = sup

sup

n 3

n

n

1 a2 − s2n

vn 2L2( 3) = (2π)−3 sup

|vˆn(y)|2 dy (2π)−3 sup

fn 2L2(µsn) < ∞.

sup

n

n 3

n

If ϕ ∈ H˙ 1/2( 3), then ϕˆ(·)| · | ∈ L2(Γ3), from where we can deduce that vn v in H˙ 1/2( 3), as n → ∞. The operator Ts

√

−∆−s2nvn. Fix

applied to fn equals (2π)3eit

√

n

√

−∆−s2n − eit

- t ∈ . From Lemma 12.2 we know (eit


−∆) {√

−∆ a} → 0 as n → ∞, the norm being as operators on H˙ 1/2( 3). This, added to the continuity of eit

√

−∆ in H˙ 1/2( 3) implies

√

√

−∆−s2nvn eit

−∆v weakly in H˙ 1/2( 3), as n → ∞. Then, by the Rellich-Kondrashov Theorem, for any R > 0

eit

√

√

−∆−s2nvn → eit

−∆v strongly in L2(B(0,R)), as n → ∞. Denote by

eit

√

√

2

√

√

−∆−s2nvn − eit

−∆−s2nvn − eit

−∆v 2L2(B(0,R)). Since we have v ˆn L2( 3) a fn L2(µsn) and v ˆ L2( 3) a f L2(σc), we obtain

−∆v

eit

dx = eit

Fn(t) :=

|x|<R

√

√

−∆−s2nvn − eit

−∆v 2L2( 3) ( vn L2( 3) + v L2( 3))2 C( v ˆn 2L2( 3) + v ˆ 2L2( 3))

Fn(t) eit

fn 2L2(µs) + f 2L2(σc). We can now ﬁnish exactly as in the proof of Proposition 5.1 and conclude that there exists a subsequence {nk}k such that

k − Tcf → 0 a.e. in 4.

Ts

fn

nk

Finally, we prove that the existence of a nonzero weak limit of an extremizing sequence that concentrates at inﬁnity implies that the operator norm of T is upper bounded by that of Tc (which in the end we will pair with Proposition 4.1 to rule out this scenario).

- Lemma 12.4. Let {sn}n be a sequence of positive real numbers converging to zero. Let f ∈ L2(Γ3) be a nonzero function and {fn}n be a sequence satisfying fn ∈ L2(Hs3n), for all n. Suppose that:


- (i) fn L2(µsn) = 1,
- (ii) Ts

n

fn L4 → T (= T1 ),

- (iii) fn f = 0 in L2(Γ3),


If there exists a > 0 such that

- (iv) supp(f),supp(fn) ⊆ {y ∈ 3: |y| a}, for all n,


then

T Tc . If condition (iv) is relaxed to

(v) supn∈ fn {|y| a} L2(µsn) ε, for some ε > 0, then

T 2 f {|y| a} 2L2(σc) Tc 2 f {|y| a} 2L2(σc) + Cε,

for some universal constant C. In particular, if we have supn∈ fn {|y| a} L2(µsn) → 0 as a → 0+, then T Tc .

An analog statement applies if we change T and Tc by T and Tc, respectively, the proof being identical.

Proof. We argue as in [13]. By the weak convergence condition (iii),

fn − f 2L2(σc) = fn 2L2(σc) − f 2L2(σc) + o(1). (12.4)

Now consider that (iv) holds. By (i) and (iv), fn 2L2(σ

c) − fn 2L2(µ

sn) → 0. Indeed,

1 |y|2 − s2n −

1 |y|

|fn(y)|2

0 fn 2L2(µsn) − fn 2L2(σc) =

dy

|y| a

|y| − |y|2 − s2n |y| {|y| a} L∞y ( 3)

fn 2L2(µsn)

= 1 − 1 − s2na−2 → 0,

(12.5)

as n → ∞. Then, (12.4) implies

fn − f 2L2(σc) = fn 2L2(µsn) − f 2L2(σc) + o(1). (12.6) Because of conditions (iii) and (iv) and Lemma 12.3, Ts

### fn → Tcf a.e. pointwise in 4, as n → ∞, and we can apply the Br´ezis-Lieb lemma to the sequence {Ts

n

fn}n ⊂ L4( 4) to obtain

n

### fn − Tcf 4L4( 4) = Ts

Ts

n

n

### fn 4L4( 4) − Tcf 4L4( 4) + o(1).

### Because by scaling the norm of the operators Ts

is independent of n (see Section

n

fn L4( 4) → T as n → ∞, we obtain

14) and by (ii) Ts

n

fn 2L4( 4) fn 2L2(µ

Ts

n

2 = T 2 =

Ts

+ o(1) (12.7)

n

sn)

fn − Tcf 4L4 + Tcf 4L4 + o(1))1/2 fn − f 2L2(σ

( Ts

n

+ o(1)

=

c) + f 2L2(σ

c) + o(1)

fn − Tcf 2L4 + Tcf 2L4 + o(1) fn − f 2L2(σ

Ts

n

+ o(1)

c) + f 2L2(σ

c) + o(1)

f 2L4 + Tcf 2L4 + o(1) fn − f 2L2(σ

### fn − Ts

Ts

n

n

+ o(1),

c) + f 2L2(σ

c) + o(1)

f−Tcf L4 → 0 as n → ∞, from Lemma 12.1. Then

where in the last inequality we used the triangle inequality and that Ts

n

sn) + Tcf 2L4 + o(1) fn − f 2L2(σ

2 fn − f 2L2(µ

2 Ts

n

Ts

+ o(1) and hence

c) + f 2L2(σ

n

c) + o(1)

2 fn − f 2L2(µsn) + Tcf 2L4 + o(1) which is equivalent to

### 2( fn − f 2L2(σc) + f 2L2(σc) + o(1)) Ts

Ts

n

n

2( fn − f 2L2(µsn) − fn − f 2L2(σc)) + o(1). Arguing as in (12.5) we obtain fn − f 2L2(µ

2 f 2L2(σc) Tcf 2L4 + Ts

Ts

n

n

sn) − fn − f 2L2(σ

c) → 0, and therefore, T = Ts

Tcf L4 f L2(σc)

Tc .

n

Finally, if we relax the support condition (iv) to the ε-small norm condition (v), it will be enough if in (12.7) we use

fn 2L4( 4) fn 2L2(µ

(fn {|y| a}) 2L4( 4) fn {|y| a} 2L2(µ

Ts

### Ts

n

n

+ Cε,

sn)

sn)

where C < ∞ is independent of n and a, together with fn {|y| a} f {|y| a} in L2(Γ3) and Ts

(fn {|y| a}) → Tc(f {|y| a}) a.e. in 4, as n → ∞, the latter property being a consequence of the former and Lemma 12.3.

n

13. Proof of Theorem 1.3

In previous Sections 10 and 11, we proved that if {fn}n is an extremizing sequence for T, then subsequences of {|fn|2}n can not satisfy vanishing nor dichotomy of Lemma 9.1, which as we saw, were a consequence of bilinear estimates for T. In this section we prove that, as a consequence of the compactness alternative and Lemma 12.4 of the previous section, extremizing sequences posses convergent subsequences and, as a result, extremizers exist.

Proof of Theorem 1.3. Let {fn}n ⊂ L2(H3) be an L2 normalized complex valued extremizing sequence for T. After passing to a subsequence if necessary we can assume that alternative (i) in Lemma 9.1 holds for {|fn|2}n, that is, there exists { n}n ⊂ with the property that for all ε > 0 there exists Rε < ∞ such that for all R Rε and n ∈

|fn(y)|2 d¯µ(y) 1 − ε. (13.1)

2 n−R |y| 2 n+R

If there exists a subsequence {nk}k ⊂ such that { nk}k is bounded above, then we can apply the same method provided in the proof of Proposition 5.2 for the upper

half of the hyperboloid, H3, to conclude that there exists a subsequence {fn

k}k that satisﬁes the conclusion of the theorem with all Ln

’s equal to the identity matrix. Therefore, in what follows we will assume that n → ∞ as n → ∞.

k

Passing to a subsequence if necessary we can assume then that {fn}n satisﬁes the following: fn L2 = 1, Tfn L4 → H4 and there exists a sequence { n}n∈ ⊂ such that n → ∞ as n → ∞ and for any ε > 0 there exists Rε < ∞ such that for all R Rε and all n ∈ equation (13.1) holds. Therefore, with Rε as before, we have that for all R Rε there exists Nn ∈ [ n − R, n + R] ∩ such that for all n ∈

1 − ε 2R

|fn(y)|2 d¯µ(y)

.

2Nn |y| 2Nn+1

Denote PN the dyadic cut oﬀ at scale 2N, that is, PNf(y) := f(y) {2N |y|<2N+1}. Using the continuity of T and the triangle inequality we obtain

1 − ε 2R

1/2

### fn) L4 Tfn L4 − H4 fn − PN

fn L2(¯µ) Tfn L4 − H4 1 −

T(PN

n

n

1 − ε 2R

1/2

= H4 − H4 1 −

### + on(1). Choosing ε = ε0 close to 0 and R = Rε

### + 1, we obtain a sequence {Nn}n ⊂ , with |Nn − n| Rε

0

+ 1, so that Nn → ∞ as n → ∞, and a constant c > 0 such that for all n large enough 8

0

### fn) L4 > c. We rescale fn deﬁning gn by gn(y) = 2N

### fn L2(¯µ) > c, T(PN

PN

n

n

### y). Letting sn = 2−N

### f(2N

we have sn → 0 as n → ∞, gn ∈ L2(H3sn),

n

n

n

gn L2(¯µsn) = fn L2(¯µ) = 1, Ts

### gn L4 = Tfn L4 → H4 as n → ∞, P1gn L2(¯µsn) = PN

n

### fn L2(¯µ) > c and (13.2) Ts

n

### (P1gn) L4 = T(PN

### fn) L4 > c, (13.3)

n

n

8By redeﬁning the sequence {fn}n we will assume that the property holds for all n 1.

### as obtained by simple rescaling (see Section 14). Moreover, from (13.1) for any small ε > 0, R > 2Rε and n ∈

|gn(y)|2 d¯µs

(y) 1 − ε, (13.4)

n

2−R |y| 2R

so that the gn’s are ”localized at scale 1”. Using Lemma 8.1 applied to Ts

and P1gn, which is possible given (13.2) and (13.3), we obtain that for all n ∈ there exist caps Cn ⊂ H3sn, which we may consider all to be contained in the upper half , Hs3n, possibly after passing to a subsequence9, Cn = [1,2] × Cn ⊂ Hs3n, for some spherical caps Cn ⊆ S2, such that

n

### (Cn)1/2, as a consequence of (8.6). Equivalently

(Cn)1/2 P1gn L2(¯µsn) µ ¯s

### |gn(y)|d¯µs

### |P1gn(y)|d¯µs

### (y) =

### (y) cµ¯s

n

n

n

n

Cn

Cn

Let α = limsupn→∞ µ¯s

n

### |fn(y)|d¯µ(y) µ ¯(2N

n

2NnCn

(Cn). Two cases arise.

Cn)1/2. (13.5)

- Case 1: α > 0. Passing to a subsequence if necessary, we can assume that there exists a constant c > 0 such that for all n


### |gn(y)|d¯µs

(y) c > 0.

n

Cn

We can view gn as a function on the double cone via the usual identiﬁcation using the orthogonal projection onto 3, where we extend it to be zero in the region where

|y| sn. Since gn L2(¯σc) gn L2(¯µsn) = 1 and 0 < c <

|gn(y)|d¯σc(y), (13.6)

### |gn(y)|d¯µs

### (y)

n

Cn

Cn

for all n large enough (as a consequence of (13.4)), there is weak convergence of {|gn|}n in L2(¯σc) after the possible extraction of a subsequence, |gn| g, for some g ∈ L2(¯σc) which satisﬁes g = 0 by (13.6). Inequality (13.4) implies that

gn {|y| a} L2(¯µsn) = 0. Because Ts

lim

sup

a→0+

n∈

(|gn|) L4 → H4, so that we can use part (v) of Lemma 12.4 applied to {|gn|}n to conclude

### (|gn|) L4, it is then also the case that Ts

### (gn) L4 Ts

n

n

n

T Tc , which is in contradiction with Proposition 4.3. Therefore, this case does not arise.

9Otherwise we reﬂect the fn’s and gn’s with respect to the origin, as necessary, by considering the sequences {L∗fn}n and {L∗gn}n where L ∈ L is the reﬂection map L(x,t) = (−x,−t)

- Case 2: α = 0. Let {γn}n ⊂ [0,π] and {Rn}n ⊂ SO(3) be such that


Rn−1(Cn) = {(rω, r2 − s2n): 1 r 2,

ω = (cosϕ,cosθ sinϕ,sinθ sinϕ),θ ∈ [0,2π], ϕ ∈ [0,γn]}. The condition α = 0 implies γn → 0 as n → ∞. Let β = limsupn→∞ µ¯(2N

### Cn) = limsupn→∞ 22N

n

### (Cn). Two subcases arise. Subcase 2a: β < ∞. This implies that the sequence {µ¯(2N

### µ¯s

n

n

Cn)}n is bounded. We may assume that the angles γn are less that π/2 as {γn}n tends to zero. Form Lemma 2.4 with s = 1, there exists {tn}n ⊂ [0,1) such that the caps {L−t

n

Rn−1(2N

Cn) : n ∈ } are contained in a ﬁxed bounded ball of 4. It therefore follows from (13.5)

n

n

)∗fn}n ⊂ L2(H3) is an extremizing sequence with L2 norm uniformly bounded below by a constant c > 0 in a ﬁxed ball. We can then conclude the precompactness modulo characters of the sequence {(RnLt

and the Cauchy–Schwarz inequality that {(RnLt

n

)∗fn}n using the argument in the proof of Proposition 5.2.

n

Subcase 2b: β = ∞. From (2.9) in Lemma 2.4 with s = 1, after passing to a subsequence if necessary, limn→∞ 22N

### sin2(γn) = ∞. Set tn = cosγn, so that tn → 1 as n → ∞. From Lemma 2.3 with s = sn, the set Cn := L−t 1

n

### Rn−1(Cn) ⊂ H3sn(1−t2n)−1/2 satisﬁes, for all n large enough for which 22N

n

sin2(γn) 8 and γn π/3, µ¯ sn √

n

π 2

and Cn ⊆ [167 , 3316] × S2.

( Cn)

1−t2

n

### sinγn)−1 → 0, as n → ∞. Let f˜n = (RnLt

### )∗fn so that {f˜n}n ⊂ L2(H3) is also an L2-normalized extremizing sequence which satisﬁes

Set an = sn(1 − t2n)−1/2 = (2N

n

n

### |f˜n(y)|d¯µ(y) cµ¯(a−n1 Cn)1/2,

a−n1 Cn

|f˜n(y)|2 d¯µ(y) c2.

a−n1 Cn

] × S2.

and a−n1 Cn ⊆ [167a

, 1633a

n

n

Deﬁne the rescale g˜n(·) := a−n1f˜n(a−n1 ·), so that for each n we have g˜n ∈ L2(H3an), g ˜n L

2(H3an) = 1 and

### |g˜n(y)|d¯µa

n

Cn

### (y) cµ¯a

n

( Cn)1/2 > c > 0.

We are almost in the same situation as in Case 1, but we need the analog of (13.4) for the sequence {g˜n}n. After passing to a subsequence if necessary, {f˜n}n satisﬁes the compactness alternative in Lemma 9.1. Denoting {˜ n}n the corresponding sequence associated to {f˜n}n as in (13.1) we then necessarily have that {˜ n − log2(a−n1)}n is bounded. This implies the desired analog of (13.4) for {g˜n}n. Therefore the argument in Case 1 applies showing that this subcase does not arise.

As a result, only Subcase 2a of Case 2 is possible, proving the theorem.

14. Scaling

Here we record scaling properties of the family of operators {Ts}s>0. Recall from Section 3 that for s > 0, Hs3 = {(y, |y|2 − s2) : y ∈ 3}, equipped with the measure µs with density dµs(y,t) = {|y|>s}δ(t − |y|2 − s2)√dydt

. The operator Ts, deﬁned on S( 3), is given by

|y|2−s2

√

dy |y|2 − s2

|y|2−s2f(y)

eix·yeit

Tsf(x,t) = fµs(−x,−t) =

.

y∈ 3,|y| s

We want to study the scaling of the quantity Hp,s deﬁned by

Tsf Lp( 4) f L2(Hs3)

Hp,s := sup

.

0 =f∈L2(Hs3)

Changing variables y sy in the expression deﬁning Tf(x,t) = T1f(x,t) we obtain Tf(x,t) =

√

dy |y|2 − 1

|y|2−1f(y)

eix·yeit

y∈ 3,|y| 1

√

s−3 dy s−2|y|2 − 1

−1x·yeit

s−2|y|2−1f(s−1y)

eis

=

y∈ 3,|y| s

√

dy |y|2 − s2

−1x·yeis

−1t

|y|2−s2s−1f(s−1y)

= s−1

eis

,

y∈ 3,|y| s

from where sTf(sx,st) = Ts(s−1f(s−1·))(x,t) and it follows that

s1−4/p Tf Lp( 4) = Tss−1f(s−1·) Lp( 4). On the other hand

s−3 dy s−2|y|2 − 1

dy |y|2 − 1

|f(s−1y)|q

|f(y)|q

=

y∈ 3, |y| 1

y∈ 3, |y| s

dy |y|2 − s2

|s−2/qf(s−1y)|q

=

,

y∈ 3, |y| s

that is f Lq(µ) = s−2/qf(s−1·) Lq(µs). Thus s1−4/p Tf Lp( 4) f −L21(µ) = Tss−1f(s−1·) Lp( 4) s−1f(s−1·) −L21(µ

s), and it follows that for all s > 0

Hp,s = s1−4/pHp. In particular, if p = 4,

H4,s = H4, for all s > 0.

Appendix A. Computation of a limit Let

√

√

∞

2 3

8 3

e−aτ τ2

(τ2 + 4)

I(a) = 16π3

τ2 + 4 −

τ2 + 1 +

0

√

τ2 + 1) dτ

+ 2τ log(τ +

and

2

√

∞

e−aτ

II(a) = 16π2

τ2 + 1dτ

.

0

The ratio I(a)/II(a) appeared in the proof of Proposition 4.1 while establishing that the best constant for the hyperboloid H3 is strictly greater than the best constant for the cone Γ3 in their respective L2 → L4( 4) adjoint Fourier restriction inequalities. The purpose of this appendix is to prove the following lemma.

## Lemma A.1.

d da

- I(a)

- II(a)


= 2π, lim

lim

a→0+

a→0+

and

d3 da3

- I(a)

- II(a)


lim

= 8π.

a→0+

Therefore there exists a0 > 0 such that

I(a) II(a)

for all 0 < a < a0.

d2 da2

I(a) II(a)

I(a) II(a)

= 0, lim

= 0

a→0+

> 2π,

Throughout this section we use the asymptotic notation oa(f(a)) and Oa(f(a)) as a → 0+ in the usual way, namely g(a) = oa(f(a)) if g(a)/f(a) → 0 as a → 0+, and g(a) = Oa(f(a)) if there exists a constant C, independent of a, such that |g(a)| C|f(a)| for all a > 0 small enough.

Changing variable u = aτ we obtain I(a) =

√

√

∞

16π3 a4

8a3 3

- 2

- 3


e−u u2

(u2 + 4a2)

u2 + 4a2 −

u2 + a2 +

0

√

+ 2a2u log(u +

u2 + a2) − log(a) dτ

√

√

∞

16π3 a4

- 2

- 3


e−u u2

(u2 + 4a2)

u2 + 4a2 −

u2 + a2

=

0

√

8a3 3 − 2a2 log(a)

+ 2a2u log(u +

u2 + a2) dτ +

6.2855

6.285

6.2845

6.284

6.2835

6.283

6.2825

6.282

0 0.05 0.1 0.15 0.2 0.25

Figure 1. Graph of the ratio I(a)/II(a) and the constant 2π for 0 < a < 0.25, illustrating the content of Lemma A.1.

and

2

√

∞

16π2 a4

e−u

u2 + a2 du

II(a) =

### . Using the Dominated Convergence Theorem it is direct to check that lim

0

a4I(a) = 32π3 and lim

a4II(a) = 16π2, so that

a→0+

a→0+

I(a) II(a)

= 2π.

lim

a→0+

To address the limit of the derivatives of the ratio I(a)/II(a) it will be convenient to introduce a rescaling. Let

N(a) := a4/3I(a1/3) = 16π3

∞

- 2

- 3


e−u u2 u2 + 4a2/3 −

(u2 + 4a2/3) u2 + a2/3

0

8a 3 −

2 3

+ 2a2/3u log(u + u2 + a2/3) dτ +

a2/3 log(a)

and

D(a) := a4/3II(a1/3) = 16π2

∞

e−u u2 + a2/3 du

0

2

.

As we already know, and can readily check, N(a) → 32π3, D(a) → 16π2 and N(a)/D(a) → 2π as a → 0+. The remaining properties of the derivatives of

I(a)/II(a) in Lemma A.1 will follow if we show that dda(N(a)/D(a)) → 43π as a → 0+.

In what follows we write (·) as a short for the derivative with respect to a. Given that both N (a) and D (a) diverge to +∞ as a → 0+ it will be convenient to write the derivative of N(a)/D(a) in the following way

16π2N (a) − 32π3D (a) D(a)2

d da

N(a) D(a)

=

(D(a) − 16π2)N (a) − (N(a) − 32π3)D (a) D(a)2

+

.

(A.1)

We have the following lemma.

## Lemma A.2.

N(a) D(a)

4π 3

d da

=

.

### (i) lim

a→0+

### (ii) As a → 0+,

log a a1/3

log a a1/3

N (a) = Oa

and D (a) = Oa

.

(N(a) − 32π3)D (a) = 0 and lim

(D(a) − 16π2)N (a) = 0.

### (iii) lim

a→0+

a→0+

Proof. In the course of the proof of this lemma we will make repeated use of the asymptotic behavior of some integrals as contained in Lemma A.3 below. We start with property (ii). For a > 0 the derivative of N is as follows,

N (a) = 16π3

2 9

−

- 2

- 3


+

= 16π3

∞

4 3a1/3

e−u u2

√

u2 + 4a2/3 −

0

1 a1/3

4 3a1/3

(u2 + 4a2/3)

√

+

u2 + a2/3

1 (u +

a1/3u

√

√

u2 + a2/3)

u2 + a2/3

4 3a1/3 −

4 9a1/3

4 3a1/3

8 3 −

log(a) +

16 9a1/3

u2 + a2/3

u log(u + u2 + a2/3)

4 9a1/3

2 3a1/3

8 3 −

log(a) −

du +

∞

e−uulog(u + u2 + a2/3)du

0

(A.2)

+ oa(1)

log a a1/3

= Oa

,

where we used (A.5),(A.8),(A.7),(A.10) and (A.11). The derivative of the function D is as follows

∞

∞

32π2 3

1 a1/3

e−u u2 + a2/3 du ·

e−u

√

du, so that (A.4) and (A.5) imply

D (a) =

u2 + a2/3

0

0

D (a) = Oa

1 a1/3

Oa(log a) = Oa

log a a1/3

,

and more explicitly using (A.13), as we will need later,

32π2 3a1/3

D (a) =

∞

e−u log(u + u2 + a2/3)du −

0

1 3

log a + oa(1). (A.3)

We now turn to the proof of part (iii). Using that 0 ∞ e−uu3 du = 6 we can write

∞

- 2

- 3


e−u u2( u2 + 4a2/3 − u) −

N(a) − 32π3 = 16π3

u2( u2 + a2/3 − u)

0

8 3

a2/3 u2 + a2/3 + 2a2/3u log(u + u2 + a2/3) du

−

- 2

- 3


8a 3 −

a2/3 log(a)

+

∞

4a1/3 √

a1/3 √

2 3

e−u u2

= 16π3a1/3

u2

u2 + 4a2/3 + u −

u2 + a2/3 + u −

0

8 3

a1/3 u2 + a2/3 + 2a2/3u log(u + u2 + a2/3) du

8a2/3 3 −

- 2

- 3


a1/3 log(a)

+

= Oa(a2/3 log a). Then

log a a1/3

= Oa(a1/3 log2 a) = oa(1). On the other hand

(N(a) − 32π3) · D (a) = Oa(a2/3 log a)Oa

∞

e−u u2 + a2/3 du + 1

D(a) − 16π2 = 16π2

0

∞

e−u( u2 + a2/3 − u)du

= Oa(1)

0

∞

a2/3 √

e−u

= Oa(1)

du

u2 + a2/3 + u

0

= Oa(a2/3 log a), where in the last line we used (A.9). Then

∞

e−u u2 + a2/3 du − 1

0

(D(a) − 16π2) · N (a) = Oa(a2/3 log a)Oa

log a a1/3

= Oa(a1/3 log2 a) = oa(1).

We now turn to the proof of (i). By (iii), the limit as a → 0+ of the second summand on the right hand side of (A.1) equals zero. We proceed to calculate the limit of the

ﬁrst summand. Combining (A.2) and (A.3) we obtain

16π2N (a) − 32π3D (a) =

4(16)2π5 3a1/3

8(16)2π5 3 −

∞

(32)2π5 3a1/3

e−u(u − 1)log(u + u2 + a2/3)du + oa(1)

+

0

∞

2(32)2π5 3

(32)2π5 3a1/3

e−u (u − 1)log(u + u2 + a2/3) − 1 du

=

+

0

+ oa(1). Using (A.12) to treat the integral in the previous expression we obtain

(32)2π5 3

(16π2N (a) − 32π3D (a)) =

, therefore

lim

a→0+

(32)2π5 3(16π2)2

d da

N(a) D(a)

4π 3

lim

=

=

.

a→0+

Finally, we state the asymptotic behavior of the many integrals used during the proof of the previous lemma.

- Lemma A.3. We have the following identities as a → 0+


∞

1 √

e−u

du = Oa(log a), (A.4)

u2 + a2/3

0

√

∞

u2 + a2/3 a1/3

1 a1/3

e−u

+ Oa(a1/3 log a), (A.5)

du =

0

√

∞

u2 + a2/3 a1/3

2 a1/3

u

e−u

+ Oa(a1/3), (A.6)

du =

0

∞

u2 a1/3

1 a1/3

e−u

+ Oa(a1/3 log a), (A.7)

√

du =

u2 + 4a2/3

0

∞

u2 + 4a2/3 a1/3

1 a1/3

e−u

+ Oa(a1/3 log a), (A.8)

√

du =

u2 + a2/3

0

∞

a2/3 u +

e−u

du = Oa(a2/3 log a), (A.9)

√

u2 + a2/3

0

∞

a1/3u (u +

e−u

du = Oa(a1/3 log a), (A.10)

√

√

u2 + 4a2/3)

u2 + 4a2/3

0

∞

u a1/3

1 a1/3

e−u

log(u + u2 + a2/3)du = Oa

, (A.11) 1 a1/3

0

∞

e−u (u − 1)log(u + u2 + a2/3) − 1 du = −1 + oa(1). (A.12)

0

Proof. The identities are elementary but we choose to give details for the sake of completeness.

Veriﬁcation of (A.4) and (A.5): Integration by parts shows that

∞

∞

1 √

1 3

e−u

e−u log(u+ u2 + a2/3)du−

du =

log a = Oa(1)+Oa(log a),

u2 + a2/3

0

0

(A.13) and

∞

∞

1 a1/3

- 1

- 2a1/3


e−u u2 + a2/3 du =

e−u(a2/3 log(u + u2 + a2/3)

0

0

1 3

a2/3 log a)du

+ u u2 + a2/3 −

∞

- 1

- 2


u a1/3

e−u(a1/3 log(u + u2 + a2/3) +

u2 + a2/3

=

0

1 3

a1/3 log a)du

−

∞

1 a1/3

1 2

u a1/3

e−u

= Oa(a1/3) + Oa(a1/3 log a) +

( u2 + a2/3 − u)du

+

0

∞

a1/3 2

u √

1 a1/3

e−u

+ Oa(a1/3 log a) +

=

du

u2 + a2/3 + u

0

1 a1/3

+ Oa(a1/3 log a) + Oa(a1/3).

=

- Veriﬁcation of (A.6): Using that 0 ∞ e−uu2 du = 2 we have

∞

0

e−u

u

√

u2 + a2/3 a1/3

du =

2 a1/3

+

1 a1/3

∞

0

e−uu( u2 + a2/3 − u)du

=

2 a1/3

+ a1/3

∞

0

e−u

u √

u2 + a2/3 + u

du

=

2 a1/3

+ Oa(a1/3).

- Veriﬁcation of (A.7):

∞

0

e−u

u2 a1/3

√

u2 + 4a2/3

du =

∞

0

e−u

√

u2 + 4a2/3 a1/3

du − 4a1/3

∞

0

e−u

1 √

u2 + 4a2/3

du

=

1 a1/3

+ Oa(a1/3 log a) + a1/3Oa(log a),

- where we used (A.4) and (A.5).


- Veriﬁcation of (A.8):


∞

u2 + 4a2/3 a1/3

e−u

√

du =

u2 + a2/3

0

=

∞

1 a1/3

e−u u2 + a2/3 du + 3a1/3

0

1 a1/3

+ Oa(a1/3 log a) + Oa(a1/3),

∞

1 √

e−u

du

u2 + a2/3

0

where in the last line we used (A.4) and (A.5).

- Veriﬁcation of (A.9):

∞

0

e−u

a2/3 u +

√

u2 + a2/3

du =

∞

0

e−u( u2 + a2/3 − u)du

= 1 + a1/3Oa(a1/3 log a) − 1

= Oa(a2/3 log a),

- where we used (A.5).


- Veriﬁcation of (A.10):

∞

0

e−u

a1/3u (u +

√

u2 + 4a2/3)

√

u2 + 4a2/3

du =

∞

0

e−u

a1/3 √

u2 + 4a2/3

du

−

∞

0

e−u

a1/3 u +

√

u2 + 4a2/3

du

= Oa(a1/3 log a), where we used (A.4) and (A.9).

- Veriﬁcation of (A.11): The identity is immediate since e−uulog(u) ∈ Lp([0,∞)) for all p ∈ [1,∞].

- Veriﬁcation of (A.12): For a > 0, integration by parts shows


∞

∞

u √

e−u(u − 1)log(u + u2 + a2/3)du =

e−u

du, so that to prove the last identity we need to show lim

u2 + a2/3

0

0

∞

u √u2 + a2

1 a

e−u 1 −

du = 1. Changing variable u au gives

a→0+

0

1 a

∞

u √u2 + a2

e−u 1 −

0

du =

=

∞

u √u2 + 1

e−au 1 −

du

0

∞

1 (u + √u2 + 1)√u2 + 1

e−au

du,

0

hence

1 a

lim

a→0+

∞

u √u2 + a2

e−u 1 −

0

du =

Changing variable u = sinht we obtain

∞

1 (u + √u2 + 1)√u2 + 1

du.

0

∞

1 (u + √u2 + 1)√u2 + 1

du =

0

∞

1 sinht + cosht

dt =

0

∞

e−t dt = 1

0

Acknowledgments

We thank Michael Christ for comments and suggestions during the initial stage of this project (2012), and Diogo Oliveira e Silva for comments on a preliminary version of this manuscript. Part of this work was carried out at Universidad de los Lagos (Osorno, Chile).

References

- [1] E. Carneiro, A sharp inequality for the Strichartz norm, Int. Math. Res. Not. 16 (2009), 3127–3145.
- [2] M. Charalambides, On restricting Cauchy-Pexider functional equations to submanifolds, Aequationes Math. 86 (2013), no. 3, 231–253.
- [3] E. Carneiro, D. Foschi, D. Oliveira e Silva, and C. Thiele, A sharp trilinear inequality related to Fourier restriction on the circle, Rev. Mat. Iberoam. 33 (2017), no. 4, 1463–1486.
- [4] E. Carneiro and D. Oliveira e Silva, Some sharp restriction inequalities on the sphere, Int. Math. Res. Not. 17 (2015), 8233–8267.
- [5] E. Carneiro, L. Oliveira, and M. Sousa, Gaussians never extremize Strichartz inequalities for hyperbolic paraboloids, arXiv:1911.11796 [math.CA] (2019).
- [6] E. Carneiro, D. Oliveira e Silva, and M. Sousa, Extremizers for Fourier Restriction on hyperboloids, Ann. Inst. H. Poincare´ Anal. Non Lin´eaire 36 (2019), no. 2, 389–415.
- [7] E. Carneiro, D. Oliveira e Silva, M. Sousa, and B. Stoval, Extremizers for adjoint Fourier restriction on hyperboloids: the higher dimensional case, Indiana Univ. Math. J. 70

(2021), no. 2, 535–559.

- [8] M. Christ and R. Quilodran´ , Gaussians rarely extremize adjoint Fourier restriction inequalities for paraboloids, Proc. Amer. Math. Soc. 142 (2014), no. 3, 887–896.
- [9] M. Christ and S. Shao, Existence of extremizers for a Fourier restriction inequality, Anal. PDE 5 (2012), no. 2, 261–312.
- [10] , On the extremizers of an adjoint Fourier restriction inequality, Adv. Math. 230 (2012), 957–977.

- [11] E. Di Nezza, G. Palatucci, and E. Valdinoci, Hitchhiker’s guide to the fractional Sobolev spaces, Bull. Sci. math. 136 (2012), no. 5, 521–573.
- [12] B. Dodson, J. Marzuola, B. Pausader, and D. Spirn, The proﬁle decomposition for the hyperbolic Shcr¨odinger equation, Illinois J. Math. 62 (2018), no. 1-4, 293–320.
- [13] L. Fanelli, L. Vega, and N. Visciglia, On the existence of maximizers for a family of restriction theorems, Bull. London Math. Soc. 43 (2011), no. 4, 811-817.
- [14] , Existence of maximizers for Sobolev-Strichartz inequalities, Adv. Math. 229 (2012), no. 3, 1912-1923.

- [15] D. Foschi, Maximizers for the Strichartz inequality, J. Eur. Math. Soc. 9 (2007), no. 4, 739–774.
- [16] , Global maximizers for the sphere adjoint Fourier restriction inequality, J. Funct. Anal. 268 (2015), no. 3, 690–702.

- [17] D. Foschi and D. Oliveira e Silva, Some recent progress in sharp Fourier restriction theory, Anal. Math. 43 (2017), no. 2, 241–265.
- [18] R. L. Frank, E. Lieb, and J. Sabin, Maximizers for the Stein-Tomas inequality, Geom. Funct. Anal. 26 (2016), 1095–1134.
- [19] D. Hundertmark and S. Shao, Analyticity of extremizers to the Airy–Strichartz inequality, Bull. Lond. Math. Soc. 44 (2012), no. 2, 336–352.
- [20] D. Hundertmark and V. Zharnitsky, On sharp Strichartz inequalities in low dimensions, Int. Math. Res. Not. ID 34080 (2006), 1–18.
- [21] J. Kato and T. Ozawa, Endpoint Strichartz estimates for the Klein–Gordon equation in two space dimensions and some applications, J. Math. Pures Appl. 95 (2011), 48–71.


- [22] R. Killip, B. Stovall, and M. Vinsan, Scattering for the cubic Klein–Gordon equation in two space dimensions, Trans. Amer. Math. Soc. 364 (2012), no. 3, 1571–1631.
- [23] P.-L. Lions, The concentration-compactness principle in the calculus of variations. The locally compact case. I, Ann. Inst. H. Poincare´ Anal. Non Lin´eaire 1 (1984), no. 2, 109–145.
- [24] S. Machihara, K. Nakanishi, and T. Ozawa, Small global solutions and the nonrelativistic limit for the nonlinear Dirac equation, Rev. Mat. Iberoam. 19 (2003), no. 1, 179–194.
- [25] A. Moyua, A. Vargas, and L. Vega, Restriction theorems and maximal operators related to oscillatory integrals in 3, Duke Math. J. 96 (1999), no. 3, 547–574.
- [26] F. Nicola, Slicing surfaces and the Fourier restriction conjecture, Proc. Edinburgh Math. Soc. 52 (2009), 515–527.
- [27] D. Oliveira e Silva, Extremizers for Fourier restriction inequalities: convex arcs, J. Anal. Math. 124 (2014), 337–385.
- [28] D. Oliveira e Silva and R. Quilodran´ , On extremizers for Strichartz estimates for higher order Schro¨dinger equations, Trans. Amer. Math. Soc. 370 (2018), no. 10, 6871–6907.
- [29] , Sharp Strichartz inequalities for fractional and higher order Schr¨odinger equations, Anal. PDE 13 (2020), no. 2, 477–526.

- [30] , Global maximizers for adjoint Fourier restriction inequalities on low dimensional spheres, J. Funct. Anal. 280 (2021), no. 7, 73pp. 108825.

- [31] , Smoothness of solutions of a convolution equation of restricted-type on the sphere, Forum Math. Sigma 9 (2021), no. E12, 40pp.

- [32] R. Quilodran´ , On extremizing sequences for the adjoint restriction inequality on the cone, J. Lond. Math. Soc. (2) 87 (2013), no. 1, 223–246.
- [33] , Nonexistence of extremals for the adjoint restriction inequality on the hyperboloid, J. Anal. Math. 125 (2015), 37–70.

- [34] J. Ramos, A reﬁnement of the Strichartz inequality for the wave equation with applications, Adv. Math. 230 (2012), no. 2, 649–698.
- [35] U. Rieder, Measurable selection theorems for optimization problems, Manuscripta Math. 24

(1978), 115-131.

- [36] S. Shao, On existence of extremizers for the Thomas-Stein inequality for S1, J. Funct. Anal. 270 (2016), no. 10, 3996–4038.
- [37] R. S. Strichartz, Restrictions of Fourier transforms to quadratic surfaces and decay of solutions of wave equations, Duke Math. J. 44 (1977), no. 3, 705–714.


Rene´ Quilodran.´ Email address: rquilodr@dim.uchile.cl

