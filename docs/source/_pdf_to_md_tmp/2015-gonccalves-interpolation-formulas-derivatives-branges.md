arXiv:1503.05178v1[math.CV]17Mar2015

INTERPOLATION FORMULAS WITH DERIVATIVES IN DE BRANGES SPACES

FELIPE GONC¸ALVES

Abstract. The purpose of this paper is to prove an interpolation formula involving derivatives for entire functions of exponential type. We extend the interpolation formula derived by J. Vaaler in [37, Theorem 9] to general Lp de Branges spaces. We extensively use techniques from de Branges’ theory of Hilbert spaces of entire functions as developed in [6], but a crucial passage involves the Hilbert–type inequalities as derived in [15]. We give applications to homogeneous spaces of entire functions that involve Bessel functions and we prove a uniqueness result for extremal one-sided band-limited approximations of radial functions in Euclidean spaces.

1. Introduction

- 1.1. Background. An entire function F : C → C, not identically zero, is said to be of exponential type if


|z|−1 log |F(z)| < ∞.

τ(F) = limsup

|z|→∞

In this case, the non-negative number τ(F) is called the exponential type of F.

In [37, Theorem 9], J. Vaaler proved that if F(z) is an entire function of exponential type at most 2π that belongs to Lp(R,dx) for some p ∈ (0,∞) then

sin2(πz) π2 n∈Z

F′(n) (z − n)

F(n) (z − n)2

, (1.1)

+

F(z) =

![image 1](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile1.png>)

![image 2](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile2.png>)

![image 3](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile3.png>)

where the sum converges uniformly on compact sets of C. Furthermore, in the case p = 2, it can be proven using Paley-Wiener spaces techniques that the formula also converges in the L2(R,dx)-norm. Also, a similar formula holds if we substitute the integers by any translation of them.

Given a number τ > 0 and p ∈ (0,∞] the classical Paley-Wiener space PW(τ,p) is deﬁned as the space of entire functions F(z) of exponential type at most τ that belong to Lp(R,dx). In the case p = 2 this is a Hilbert space with the standard L2(R,dx)-inner product and it can be proven that convergence in the space implies uniform convergence on compact sets of C. Based on the Hilbert space setting, the natural environment to extend the interpolation formula (1.1) would be the de Branges spaces of entire functions as developed by L. de Branges in [6], since they generalize the Paley-Wiener spaces.

Intuitively, a de Branges space can be seen as a weighted Paley-Wiener space. Given a Hermite-Biehler function E(z) (see the deﬁnition in §1.2) and a number p ∈ (0,∞], the space Hp(E) is a space of entire functions F(z) that satisﬁes a certain growth condition relatively to E(z) and such that F/E belongs to Lp(R,dx).

![image 4](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile4.png>)

Date: August 27, 2018. 2010 Mathematics Subject Classiﬁcation. 46E22, 30D10, 41A05, 41A30, 33C10. Key words and phrases. De Branges spaces, Hilbert Spaces of Entire Functions, Exponential Type, Interpolation Formulas,

Bessel Functions, Homogeneous Spaces, Extremal Functions.

Formula (1.1) is useful in applications to approximation theory. In [23], S. Graham and J. Vaaler used this formula to construct extremal one-sided approximations of exponential type to a given real-valued function g(x). Under certain restrictions on g(x), they characterized the pair of entire functions M(z) and L(z) of exponential type at most 2π that satisﬁes L(x) ≤ g(x) ≤ M(x) for all real x minimizing the quantities

{M(x) − g(x)} dx and

R

{g(x) − L(x)} dx.

R

In [15], E. Carneiro, F. Littmann and J. Vaaler applied the same methods to produce extremal one-sided band-limited approximations for functions g(x) that are in some sense subordinated to the Gaussian function. Later in [22], F. Gon¸calves, M. Kelly and J. Madrid extended their results to the several variables regime. Other important works that apply such interpolation formulas are [12, 16, 37].

If, instead of the L1(R,dx)-norm, one decides to minimize a weighted norm L1(R,dµ(x)), where µ(x) is a non-decreasing function on the real line, the Fourier transform tools are no longer available. The alternative theory to approach these new extremal problems is the theory of de Branges spaces. Several works have been done in this direction, see [8, 11, 13, 14, 24, 29, 30]. The methods used in these later works were very diﬀerent than the previous ones, since generalizations of the formula (1.1) to de Branges spaces were not known at the time. These special functions M(z) and L(z) have been used in a variety of interesting applications in number theory and analysis, for instance in connection to: large sieve inequalities [24, 37], Erdo¨s-Tur´an inequalities [16, 37], Hilbert-type inequalities [13, 15, 16, 23, 28, 37], Tauberian theorems [23] and bounds in the theory of the Riemann zeta-function and general L-functions [7, 8, 9, 10, 18, 20, 21].

- 1.2. De Branges Spaces. In order to properly state our results we need to brieﬂy review the main concepts and terminology of the theory of Lp de Branges spaces (see [3, 6]).


Throughout the text we denote by

U = {z ∈ C; Im(z) > 0}

the open upper half-plane. An analytic function F : U → C has bounded type if it can be written as a quotient of two functions that are analytic and bounded in U (or equivalently, if log |F(z)| admits a positive harmonic majorant in U). If F : U → C is not identically zero and has bounded type, from its Nevanlinna factorization [6, Theorems 9 and 10], the number

y−1 log |F(iy)|,

v(F) = limsup

y→∞

called the mean type of F, is ﬁnite. It can be proven that the set of functions of bounded type in U is an algebra and

v(FG) = v(F) + v(G) and v(F + G) ≤ max{v(F),v(G)}, (1.2) if F(z) and G(z) are of bounded type in U (see [6, Problem 29]).

![image 5](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile5.png>)

If E : C → C is entire, we deﬁne the entire function E∗ : C → C by E∗(z) = E(z). A Hermite-Biehler

![image 6](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile6.png>)

- function E : C → C is an entire function that satisﬁes the basic inequality |E∗(z)| < |E(z)|


for all z ∈ U. Associated to E(z), we deﬁne the companion functions A(z) :=

i 2

- 1

![image 7](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile7.png>)

- 2


E(z) + E∗(z) and B(z) :=

E(z) − E∗(z) .

![image 8](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile8.png>)

Note that A(z) and B(z) are real entire functions with only real zeros and E(z) = A(z) − iB(z). Similarly, if α is a real number, we write

eiαE(z) = Aα(z) − iBα(z) (1.3) where Aα(z) and Bα(z) are real entire functions. Note that Bα−π/2(z) = Aα(z).

We denote by ϕ(z) the phase function associated to E(z). This function is deﬁned by the condition eiϕ(x)E(x) ∈ R for all real x. It can be shown that ϕ(z) is analytic on a neighborhood of R, any two of such functions diﬀer by an integer multiple of π, and ϕ′(t) > 0 for all real t (see [6, Problem 48] and [24]). For a given real number α we deﬁne

T (α) = {x ∈ R : ϕ(x) ≡ α(mod π)} and we note that T (α) is the set of all real zeros of Bα(z)/E(z).

If E(z) is a Hermite-Biehler function and p ∈ (0,∞], we deﬁne the Lp de Branges space Hp(E) as the space of entire functions F : C → C such that F/E and F∗/E have bounded type in U with non-positive mean type and

1/p

|F(x)/E(x)|pdx

< ∞ if p is ﬁnite, and

F E,p =

R

|F(x)/E(x)| < ∞

F E,∞ = sup x∈R

if p = ∞. When p ≥ 1 these are Banach spaces (see Section 3) and when p = 2 (we write H(E) = H2(E) and · E,2 = · E) this forms a Hilbert space with inner product given by

∞

F(x)G(x) |E(x)|−2 dx.

![image 9](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile9.png>)

F,G E =

−∞

The remarkable property about these spaces is that, for each w ∈ C, the evaluation map F  → F(w) is a continuous linear functional. It can be shown, using Cauchy’s formula for the upper half-plane (see [6, Theorems 12 and 19]), that the function

E(z)E∗(w) − E∗(z)E(w) 2πi(w − z)

B(z)A(w) − A(z)B(w) π(z − w)

![image 10](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile10.png>)

![image 11](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile11.png>)

![image 12](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile12.png>)

![image 13](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile13.png>)

K(w,z) =

=

(1.4)

![image 14](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile14.png>)

![image 15](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile15.png>)

![image 16](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile16.png>)

![image 17](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile17.png>)

is a reproducing kernel for these spaces. That is, for any w ∈ C and any p ∈ [1,∞) the function K(w,·) belongs to Hp

′

(E), where 1/p + 1/p′ = 1, and

∞

F(x)K(w,x) |E(x)|−2 dx, (1.5)

![image 18](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile18.png>)

F(w) = F,K(w,·) E =

−∞

for each F ∈ Hp(E). Note that, by Cauchy-Schwarz inequality, we obtain |F(w)| ≤ F E,p K(w,·) E,p′. (1.6)

It can be shown that w  → K(w,·) E,p′ is continuous, hence we see that convergence in the space implies uniform convergence on compact sets of C.

From the reproducing kernel property we have K(w,w) = K(w,·),K(w,·) E = K(w,·) E ≥ 0 ,

and one can easily show that K(w,w) = 0 if and only if w ∈ R and E(w) = 0 (see for instance [24, Lemma 11] or [6, Problem 45]).

For a given a > 0, we deﬁne the Paley-Wiener space PW(a,p) = Hp(e−iaz). By Krein’s theorem (see [26] and [24, Lemma 12]) this space coincides with the space of entire functions F(z) of exponential type at most a such that F ∈ Lp(R,dx).

In Section 3 we give a diﬀerent approach for deﬁning the spaces Hp(E) connecting with the theory of Hardy spaces in the upper half-plane. Also in Section 3 we comment about the proof of completeness of these spaces.

- 1.3. Main Results. We say that a de Branges space Hp(E) is closed by diﬀerentiation if F′ ∈ Hp(E) whenever F ∈ Hp(E). By (1.6) we conclude that for p ∈ [1,∞) convergence in the space implies uniform convergence on compacts sets of C, hence the diﬀerentiation operator is always a closed operator. Thus, by the Closed Graph Theorem, it is continuous whenever it is everywhere deﬁned.


Recall that we omit the superscript p in Hp(E) only when p = 2, that is, we write H(E) = H2(E). The crucial idea for the main result of the paper is to proof an interpolation formula with derivatives for functions in the space H(E2), not in H(E). As in the Vaaler’s proof, the natural space for the correct interpolation formula was PW(2π,2) = H([e−iπz]2). Also note that E(z)2 = A(z)2 − B(z)2 − 2iA(z)B(z), thus the condition AB ∈/ H(E2) will be necessary for the main result (see formula (2.2)).

The following theorem is the main result of the paper.

Theorem 1. Let E(z) be a Hermite-Biehler function such that H(E2) is a de Branges space closed by diﬀerentiation. Suppose that for a real number α we have AαBα ∈/ H(E2) and ϕ′(x) is bounded away from zero over T (α). Then, if p ∈ [1,2] and F ∈ Hp(E2), we have

F′(t)Bα′ (t) − F(t)Bα′′(t) Bα′ (t)3(z − t)

F(t) Bα′ (t)2(z − t)2

F(z) = Bα(z)2

, (1.7)

+

![image 19](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile19.png>)

![image 20](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile20.png>)

t∈T (α)

where the sum converges uniformly on compact sets of C. This formula is also valid for p ∈ (2,∞) if we additionally assume that v(E∗/E) < 0.

Remark: We note that there exists at most one α modulo π/2 such that AαBα ∈ H(E2) otherwise E2(z) would belong to H(E2), which is an absurd. In the paper [2], A. Baranov proved that if E′/E belongs to the Hardy space H∞(U) (see Section 3) then the diﬀerentiation operator is continuous in H(E). He also concluded that this condition is necessary if we assume v(E∗/E) < 0 (see also [3]).

We highlight the fact that Vaaler’s proof of (1.1) in [37] relies heavily on Fourier analysis, a tool that is not available in this general setting. Thus, our main challenge here (and motivation to consider this problem) is two-fold: (i) to ﬁnd a Fourier analysis-free proof of (1.1); (ii) to extend this proof to the general setting. This is carried out in Sections 2 and 3.

We present here a corollary of this result related to sampling theory.

Corollary 2. Let E(z) = A(z)−iB(z) be an Hermite-Biehler function such that PW(a,2) = H(E2) as sets. Suppose that for some constant M > 0, |A(t)| ≤ M whenever B(t) = 0. Then there exists a constant C > 0 such that

{|F(t)|2 + |F′(t)|2} ≤ C

|F(t)|2dt (1.8)

C−1

|F(t)|2dt ≤

R

R

B(t)=0

for every F ∈ PW(a,2). Furthermore, if {tn}n∈N is an enumeration of the real zeros of B(z) then for every pair (pn) ∈ l2(N) and (qn) ∈ l2(N) of complex sequences there exists an unique function F ∈ PW(a,2) such that F(tn) = pn and F′(tn) = qn for all n.

Remark: Following the ideas of J. Ortega-Cerd` and K. Seip in [34], Corollary 2 gives a suﬃcient condition for a sequence of points to be sampling with derivates for PW(a,2). We say that a discrete set of real points Λ is sampling with derivatives for PW(a,2) if there exists a constant C > 0 such that

C−1

|F(t)|2dt ≤

|F(t)|2dt

{|F(t)|2 + |F′(t)|2} ≤ C

R

R

t∈Λ

for every F ∈ PW(a,2). Also, in the paper [31], Y. Lyubarskii and K. Seip give necessary and suﬃcient conditions for a Hermite-Biehler function E(z) to satisfy PW(a,2) = H(E2).

- 1.4. Organization of the Paper. In Section 2 we prove Theorem 1 for the case p = 2 using de Branges space techniques. In Section 3 we review the aspects of Lp de Branges spaces and provide the full proof of Theorem 1. In Part 1 of Section 4 we give a quick review of homogeneous spaces and derive interpolation formulas for these spaces, which fully generalize the interpolation results derived in [37]. Finally, in Part 2 of Section 4 we provide a direct application of our formulas, proving a uniqueness result concerning best one-sided approximations by band-limited functions in Euclidean spaces.
- 1.5. Notation Remark. Given two positive quantities Q and Q′ and N real quantities r1,...,rN we write


1,...,rN Q′ when Q ≤ C(r1,...,rN)Q′ where C : Ω ⊂ RN → (0,∞) is some positive function. We also write Q ≃r1,...,rN Q′ when both Q <<r

Q <<r

1,...,rN Q hold. Often, the quantities Q and Q′ will depend on a function F, that is Q = Q(F) and Q′ = Q′(F). We write Q(F) << Q′(F) when there exists a constant C > 0, which does not depend on F, such that Q(F) ≤ CQ′(F).

1,...,rN Q′ and Q′ <<r

2. Interpolation Formulas in de Branges Spaces

Without the Fourier transform theory we need to use a diﬀerent approach than that used by J. Vaaler in [37]. The recipe to extend formula (1.1) is

- (1) Substitute the function sin(πz) by the companion function Bα(z) deﬁned in (1.3) associated with a Hermite-Biehler function E(z).
- (2) Prove that formula (1.7) is valid for a dense set of functions in H(E2).
- (3) Deduce inequalities that guarantee that the formula will remain valid when we pass to the limit.


In the last step of this recipe we shall use the Hilbert-type inequalities as derived in [15].

- 2.1. Preliminary Results. Let E(z) be an Hermite-Biehler function and recall that we write ϕ(z) for the phase function. If t and α are real numbers such that ϕ(t) ≡ α (mod π) we have


Bα′ (t) Aα(t)

ϕ′(t) = πK(t,t)/|E(t)|2 =

> 0, (2.1) where K(w,z) is deﬁned in (1.4) (see [6, Problem 48]). We also have

![image 21](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile21.png>)

0 < |E(z)|2 − |E∗(z)|2 2y|B(z)|2

- A(z)

![image 22](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile22.png>)

- B(z)


= Re i if y > 0. In a similar way Re[−iB(z)/A(z)] > 0 if y > 0.

![image 23](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile23.png>)

Throughout the rest of this paper we will always denote by {tn} the points such that ϕ(tn) = πn for all n ∈ Z and {sn} the points such that ϕ(sn) = π/2 + nπ for all n ∈ Z. These points are respectively all the real zeros of B(z)/E(z) and A(z)/E(z). Also these zeros are simple.

To see this, suppose that tn is a zero of E(z) of order m ≥ 0 and of B(z) of order m + l ≥ 1. We claim that l = 1. If m = 0, then by (2.1) and (1.3) we trivially have l = 1. If not, then E˜(z) = E(z)/(z − tn)m is a Hermite-Biehler function and E˜(tn) = 0, hence by the previous argument tn is a simple zero of B(z)/(z−tn)m and thus l = 1. We conclude that the points {tn} and {sn} are respectively simple zeros and simple poles of B(z)/A(z).

According to [6, Theorem 22], for every real number α the set of functions

is an orthogonal set in H(E) and

F 2E ≥

Bα(z) (z − t) t∈T (α)

![image 24](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile24.png>)

|F(t)|2 K(t,t)

|F(t)|2 Bα′ (t)Aα(t)

= π

, (2.2)

![image 25](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile25.png>)

![image 26](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile26.png>)

t∈T (α)

t∈T (α)

where equality holds if and only if Bα ∈/ H(E). We have the following lemma.

- Lemma 3. Let E(z) be a Hermite-Biehler function with no real zeros. If A ∈/ H(E) then


- (1) For all complex numbers z and w not equal to any sn we have B(z)/A(z) − B(w)/A(w)

![image 27](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile27.png>)

![image 28](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile28.png>)

![image 29](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile29.png>)

![image 30](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile30.png>)

w − z

=

n

B(sn) A′(sn)(z − sn)(w − sn)

![image 31](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile31.png>)

![image 32](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile32.png>)

. (2.3)

- (2) For all sj we have B(z)

![image 33](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile33.png>)

A(z)

=

B′(sj) A′(sj) −

![image 34](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile34.png>)

B(sj)A′′(sj) 2A′(sj)2

![image 35](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile35.png>)

+

B(sj) A′(sj)(z − sj)

![image 36](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile36.png>)

+

n =j

B(sn) A′(sn)

![image 37](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile37.png>)

1 z − sn

![image 38](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile38.png>)

+

1 sn − sj

![image 39](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile39.png>)

. (2.4)

- (3) For all tj we have B(z)


1 z − sn

1 sn − tj

B(sn) A′(sn)

. (2.5)

+

=

![image 40](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile40.png>)

![image 41](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile41.png>)

![image 42](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile42.png>)

![image 43](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile43.png>)

A(z)

n

These series converge uniformly on compact sets of C away from their respective singularities since the following summability condition holds

|B(sn)| |A′(sn)|(1 + s2n)

< ∞. (2.6)

![image 44](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile44.png>)

n

Proof. The function f(z) = B(z)/A(z) satisﬁes Re[−if(z)] > 0 if y > 0 with simple poles at the points z = sn. By the Stieltjes inversion formula (see [6, Problem 47 and Theorem 3]) the condition (2.6) holds and there exists some non-positive number p such that

B(z)/A(z) − B(w)/A(w) w − z

B(sn) A′(sn)(z − sn)(w − sn)

![image 45](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile45.png>)

![image 46](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile46.png>)

= p +

.

![image 47](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile47.png>)

![image 48](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile48.png>)

![image 49](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile49.png>)

![image 50](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile50.png>)

n

By the proof of [6, Theorem 22], if we multiply the last equality by A(z), both sides would be functions in H(E). Since A ∈/ H(E) we conclude that p = 0 and this proves (1). To ﬁnish, we only prove (2) since (3) is analogous. For this, deﬁne

1 z − sn

1 sn − sj and note that

B(sn) A′(sn)

B(sj) A′(sj)(z − sj)

+

+

g(z) =

![image 51](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile51.png>)

![image 52](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile52.png>)

![image 53](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile53.png>)

![image 54](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile54.png>)

n =j

B(z)/A(z) − B(w)/A(w) w − z

g(z) − g(w) w − z

![image 55](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile55.png>)

![image 56](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile56.png>)

![image 57](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile57.png>)

=

.

![image 58](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile58.png>)

![image 59](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile59.png>)

![image 60](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile60.png>)

![image 61](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile61.png>)

Thus g(z) diﬀers from B(z)/A(z) by a constant, that is g(z) + C = B(z)/A(z). We conclude that (for instance, via the Laurent expansions around sj) C = lim

B′(sj) A′(sj) −

B(sj)A′′(sj) 2A′(sj)2

B(z) − g(z)A(z) A′(sj)(z − sj)

.

=

![image 62](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile62.png>)

![image 63](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile63.png>)

![image 64](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile64.png>)

z→sj

Remark: A similar lemma holds if we change A(z) by B(z) and sn by tn.

- Lemma 4. Let E(z) be a Hermite-Biehler function with no real zeros. If B ∈/ H(E) then

- (1) If sk = sl we have A′(sk)

![image 65](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile65.png>)

B(sk)(sk − sl)

=

n

A(tn) B′(tn)(sk − tn)2(sl − tn)

![image 66](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile66.png>)

(2.7)

and

−

A′(sk) B(sk)(sk − sl)2 −

![image 67](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile67.png>)

A′(sl) B(sl)(sk − sl)2

![image 68](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile68.png>)

=

n

A(tn) B′(tn)(sk − tn)2(sl − tn)2

![image 69](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile69.png>)

. (2.8)

- (2) For all sk we have


−

1 6

![image 70](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile70.png>)

∂3 ∂z3

![image 71](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile71.png>)

- A(z)

![image 72](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile72.png>)

- B(z) z=s


k

=

n

A(tn) B′(tn)(sk − tn)4

![image 73](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile73.png>)

. (2.9)

Proof. We can change the roles of A(z) and B(z) in Lemma 3 to obtain

A(z)/B(z) − A(w)/B(w) w − z

![image 74](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile74.png>)

![image 75](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile75.png>)

![image 76](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile76.png>)

![image 77](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile77.png>)

=

n

A(tn) B′(tn)(z − tn)(w − tn)

![image 78](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile78.png>)

![image 79](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile79.png>)

. (2.10)

Thus, the ﬁrst part of assertion (1) follows if we diﬀerentiate the above formula with respect to z and evaluate at the points z = sk and w = sl. For the second formula in (1) we diﬀerentiate (2.10) with respect to z and w and then evaluate at the points z = sk and w = sl. For (2) we diﬀerentiate (2.10) with respect to z and w but now we evaluate at the points z = w = sk.

![image 80](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile80.png>)

![image 81](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile81.png>)

![image 82](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile82.png>)

![image 83](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile83.png>)

![image 84](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile84.png>)

Let E(z) be a Hermite-Biehler function and deﬁne for every n the following auxiliary functions

Pn(z) =

A(z)2 (z − sn)2

![image 85](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile85.png>)

and Qn(z) =

A(z)2 (z − sn)

![image 86](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile86.png>)

. (2.11)

These are the interpolating functions for the formula (1.7) if we take α = −π/2. Note that Pn,Qn ∈ H(E2) for all n. The next lemma computes the norms and inner products associated with these functions in the space H(E2) under the assumption AB ∈/ H(E2). We note that we can always substitute E(z) by eiαE(z) = Aα(z) − iBα(z) for some real number α such that H(E2) = H(e2iαE2) isometrically and the new functions satisfy AαBα ∈/ H(e2iαE2). In fact there is at most one α modulo π/2 such that AαBα ∈ H(E2) (see the remark after Theorem 1).

- Lemma 5. Let E(z) = A(z) − iB(z) be a Hermite-Biehler function with no real zeros and suppose that AB ∈/ H(E2).


Then, if sk = sl, we have

- A′(sk)

![image 87](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile87.png>)

- B(sk)


- A′(sl)

![image 88](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile88.png>)

- B(sl)


π 2(sk − sl)2

Pk,Pl E2 = −

(2.12) and

+

![image 89](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile89.png>)

Qk,Ql E2 = 0. (2.13) We also have

∂3 ∂z3

- A′(sk)3

![image 90](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile90.png>)

- B(sk)3


π 2

- A(z)

![image 91](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile91.png>)

- B(z) z=s


1 6

Pk 2E2 = −

+

(2.14) and

![image 92](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile92.png>)

![image 93](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile93.png>)

![image 94](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile94.png>)

k

- A′(sk)

![image 95](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile95.png>)

- B(sk)


π 2

Qk 2E2 = −

. (2.15)

![image 96](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile96.png>)

Proof. Denote by K2(w,z) the reproducing kernel of H(E2). A simple calculation would show that K2(w,z) =

![image 97](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile97.png>)

![image 98](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile98.png>)

- K(w,z)J(w,z) where J(w,z) = 2{A(w)A(z) + B(w)B(z)} and K(w,z) is deﬁned in (1.4). We obtain K2(tn,tn) = 2A(tn)3B′(tn)/π and K2(sn,sn) = −2B(sn)3A′(sn)/π. (2.16)


Fix sk = sl. Since AB ∈/ H(E2) we can apply [6, Theorem 22] to conclude that the set of functions A(z)B(z) (z − tn) ∪

A(z)B(z) (z − sn)

![image 99](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile99.png>)

![image 100](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile100.png>)

forms an orthogonal basis of H(E2). Note that the above functions are multiples of K2(tn,z) and K2(sn,z) respectively. Hence, we can calculate inner products using this orthogonal basis. We obtain

A(tn)4 (tn − sk)2(tn − sl)2

1 K2(tn,tn)

π 2 n

A(tn) B′(tn)(sk − tn)2(sl − tn)2

Pk,Pl 2E2 =

=

![image 101](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile101.png>)

![image 102](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile102.png>)

![image 103](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile103.png>)

![image 104](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile104.png>)

n

- A′(sk)

![image 105](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile105.png>)

- B(sl)


- A′(sk)

![image 106](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile106.png>)

- B(sl)


π 2(sk − sl)2

= −

,

+

![image 107](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile107.png>)

- where the last equality is due to (2.8). In the same way we obtain

Qk,Ql E2 =

n

A(tn)4 (tn − sk)(tn − sl)

![image 108](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile108.png>)

1 K2(tn,tn)

![image 109](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile109.png>)

=

π 2 n

![image 110](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile110.png>)

A(tn) B′(tn)(tn − sk)(tn − sl)

![image 111](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile111.png>)

= 0,

where the last equality is due to (2.3), since we can change the roles of A and B in Lemma 3.

To calculate the norms of Pk(z) and Qk(z) we use the same method, but an additional term will appear due to the function A(z)B(z)/(z − sk). We obtain

Pk 2E2 = −

π 2

![image 112](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile112.png>)

- A′(sk)3

![image 113](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile113.png>)

- B(sk)3


+

π 2 n

![image 114](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile114.png>)

A(tn) B′(tn)(sk − tn)4

![image 115](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile115.png>)

= −

π 2

![image 116](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile116.png>)

- A′(sk)3

![image 117](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile117.png>)

- B(sk)3


+

1 6

![image 118](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile118.png>)

∂3 ∂z3

![image 119](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile119.png>)

- A(z)

![image 120](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile120.png>)

- B(z) z=s


k

,

- where the last equality is due to (2.9). Analogously, by formula (2.3), we have


π 2 n

Qk 2E2 =

![image 121](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile121.png>)

π 2

A(tn) B′(tn)(sk − tn)2

= −

![image 122](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile122.png>)

![image 123](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile123.png>)

- A′(sk)

![image 124](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile124.png>)

- B(sk)


.

We say that an entire function E(z) is of Po´lya class if it satisﬁes the following conditions

- (i) E(z) = 0 for every z ∈ U.
- (ii) |E∗(z)| ≤ |E(z)| for every z ∈ U.
- (iii) Re [iE′(z)/E(z)] ≥ 0 for every z ∈ U.


If E(z) is of Po´lya class and real entire we say that it is of Laguerre-P´olya class. The usual deﬁnition of the Laguerre-Po´lya class is via uniform limits on compact sets of polynomials having only real zeros, but these two deﬁnitions are equivalent (see [6, Theorem 7 and Problems 11,12 and 13]).

If a de Branges space H(E2) is closed by diﬀerentiation it should have some special properties. The next lemma groups together those that are relevant for our purposes.

- Proposition 6. Let H(E2) be a de Branges space closed by diﬀerentiation, then


- (1) E(z) is a function of exponential type with no real zeros.
- (2) The real zeros of the functions Aα(z) are separated and the width of separation depends only on the norm of the diﬀerentiation operator in H(E2).
- (3) The functions Aα(z) are of Laguerre-P´olya class.
- (4) Let D denote the norm of the diﬀerentiation operator in H(E2). Then for every real number α we have

A′′α(s)2 + 4A′α(s)2 ≤ (D2 + D4)Bα(s)2, (2.17) whenever Aα(s) = 0.

- (5) The function ϕ′(x) is bounded.


- Proof. First we prove (1). If F ∈ H(E2) then for any w ∈ C we have


|F(n)(w)| n! |z − w|n ≤ F E2K2(w,w)1/2

Dn|z − w|n n!

= F E2K2(w,w)1/2eD|z−w| ,

|F(z)| ≤

![image 125](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile125.png>)

![image 126](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile126.png>)

n≥0

n≥0

where we have used (1.6) and D denotes the norm of the diﬀerentiation operator. We conclude that every

- function F ∈ H(E2) is of exponential type at most D. Fix a function F ∈ H(E2) with F(i) = 0. We conclude that G(z) = [F(i)E(z)2 − E(i)2F(z)]/(z − i) belongs to H(E2) and


E(z)2 = [(z − i)G(z) + E(i)2F(z)]/F(i).

Hence, E(z) is of exponential type at most D/2. E(z) cannot have real zeros since the diﬀerentiation reduces the order of the zeros (this argument is due to A. Baranov see [3]).

Now we prove (4). Since (eiαE(z))2 generates the same space that E(z)2 generates, we can assume that α = 0. We have the following Taylor’s expansion for the function Qn(z)

Qn(z) = A′(sn)2(z − sn) + A′(sn)A′′(sn)(z − sn)2 + ... Letting K2(w,z) be the reproducing kernel of H(E2) and using the Cauchy-Schwarz inequality, we obtain

A′(sn)4 + 4A′(sn)2A′′(sn)2 = |Q′n(sn)|2 + |Q′′n(sn)|2 ≤ (D2 + D4) Qn 2E2K2(sn,sn). Since

K2(sn,sn) = −2A′(sn)B(sn)3/π and

Qn 2E2 ≤ A(z)/(z − sn) 2E = −π[A′(sn)/B(sn)] (2.18) we obtain the desired inequality (2.17).

Now we prove (3). First assume that α = 0 and A ∈/ H(E). Take F ∈ H(E2) such that F(0) = 1 and write a = E(0). We conclude that

E(z)2 − F(z)a2 z

∂ ∂z

= [2E′(z)E(z) − F′(z)a2]/z − [E(z)2 − F(z)a2]/z2

![image 127](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile127.png>)

![image 128](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile128.png>)

belongs to the space H(E2). Using (1.2) we conclude that E′(z)/E(z) is of bounded type in U with nonpositive mean type. Also,

dt 1 + t2

|E′(t)/E(t)|2

< ∞. Applying the same argument with E∗(z) we obtain that

![image 129](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile129.png>)

R

E(z)E∗(z) − F(z)|a|2 z

∂ ∂z

= [E′(z)E∗(z) + E(z)E′∗(z) − F′(z)|a|2]/z − [E(z)E∗(z) − F(z)|a|2]/z

![image 130](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile130.png>)

![image 131](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile131.png>)

belongs to the space H(E2), hence E′∗(z)/E(z) is of bounded type in U with non-positive mean type. We conclude that A′(z)/E(z) is of bounded type in U with non-positive mean type.

Now take b ∈ R such that A(b) = 0 and F ∈ H(E) with F(b) = 1. Then [A′(z) − A′(b)F(z)]/(z − b) belongs to H(E) and, since A ∈/ H(E), we can apply [6, Theorem 22] to obtain

A′(z) − A′(b)F(z) A(z)(z − b)

1 − A′(b)F(sm)/A′(sm) (sm − b)(z − sm)

=

.

![image 132](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile132.png>)

![image 133](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile133.png>)

m

By the same theorem we have

F(sm) A′(sm)(z − sm)

. We conclude that

F(z)/A(z) =

![image 134](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile134.png>)

m

A′(z) A(z)

1 |z − sm|2

> 0

Re i

= y

![image 135](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile135.png>)

![image 136](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile136.png>)

m

for y > 0. Hence A(z) is of Po´lya class (see [6, Section 7]). Since A(z) is real entire, it belongs to the LaguerrePo´lya class. A similar argument would show that Aα(z) is of Laguerre-Po´lya class whenever Aα ∈/ H(E). Since the Laguerre-Po´lya class is closed by pointwise limits and there exists at most one α modulo π/2 such that Aα ∈ H(E), item (3) follows.

We now prove (2). Assume ﬁrst that AB ∈/ H(E2). By inequality (2.18) we get, for all m and n,

A(tm)4/(tm − sn)2 = |Qn(tm)|2 ≤ Qn 2E2K2(tm,tm) = −2[A′(sn)/B(sn)]B′(tm)A(tm)3. (2.19) Recalling that Bα−π/2 = Aα, by item (4) we obtain

(tm − sn)−2 <<D 1 , (2.20) which proves item (2), since the points {tn} and {sn} are interlaced.

Finally, for item (5), note that

ϕ′(sn) = −[A′(sn)/B(sn)], which is bounded by item (4). In general, if we take a real point s such that ϕ(s) ≡ α − π/2 (mod π) then

ϕ′(s) = −[A′α(s)/Bα(s)] <<D 1.

Remark: In [2, Section 4.1] A. Baranov constructed spaces H(E) that are closed by diﬀerentiation, but ϕ′(x) is unbounded. Thus, for a space H(E2) to be closed by diﬀerentiation we have to require stronger restrictions on the function E(z). For instance, the boundedness of ϕ′(x) will play an important role in the proof of Theorem 1, since it implies that the points of interpolation T (α) are separated.

For the sake of completeness we state here a result about Hilbert-type inequalities proved in [15, Corollary 22].

- Proposition 7. Let ξ1,ξ2,...,ξN be real numbers such that 0 < σ ≤ |ξn − ξm| whenever m = n. Let a1,a2,...,aN be complex numbers. Then


N

N

π2 6σ2

π2 3σ2

anam (ξn − ξm)2 ≤

![image 137](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile137.png>)

|an|2 ≤

−

![image 138](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile138.png>)

![image 139](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile139.png>)

![image 140](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile140.png>)

n=1

m,n=1

m =n

N

|an|2.

n=1

The constants appearing in these inequalities are the best possible.

- 2.2. Proof of Theorem 1 - The case p = 2. The idea of the proof is to show that (1.7) holds for a dense set of functions in H(E2) and then argue that we can interchange limits and summation. In fact we will show convergence of the formula in the space H(E2), which implies convergence on compact sets of C.


First of all, we can assume α = −π/2 which is no restriction since H(E2) = H(e2iαE2) isometrically. Also, note that B−π/2(z) = A(z) and A−π/2(z) = −B(z). We will denote by D the norm of the diﬀerentiation operator in H(E2). By the hypothesis of the theorem there exists a number δ > 0 such that

|A′(sn)/B(sn)| = ϕ′(sn) ≥ δ for all n. (2.21) We divide the proof in a few steps.

- Step 1. We show that the quantities in (2.14) and (2.15) are uniformly bounded. By (2.15) and Proposition


- 6 item (4), we have


- A′(sk)

![image 141](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile141.png>)

- B(sk)


π 2

Qk 2E2 = −

<<D 1. (2.22) By (2.14) we have

![image 142](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile142.png>)

π 2

Pk 2E2 = −

![image 143](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile143.png>)

A′(sk)3 B(sk)3

1 6

+

![image 144](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile144.png>)

![image 145](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile145.png>)

A′′′(sk) B(sk) − 3

A′(sk)B′′(sk) B(sk)2

A′′(sk)B′(sk) B(sk)2 − 3

![image 146](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile146.png>)

![image 147](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile147.png>)

![image 148](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile148.png>)

A′(sk)B′(sk)2 B(sk)3

+ 6

![image 149](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile149.png>)

.

Again, by Proposition 6 item (4), we obtain

Pk 2E2 <<D 1 +

A′′′(sk) B(sk)

![image 150](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile150.png>)

+

B′(sk) B(sk)

![image 151](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile151.png>)

+

B′′(sk) B(sk)

![image 152](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile152.png>)

+

B′(sk) B(sk)

![image 153](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile153.png>)

2

. (2.23)

We claim that each quantity appearing on the right hand side of the last inequality is bounded independently of sk. By deﬁnition (2.11), identities (2.15) and (2.16) we have

|2A′′′(sk)A′(sk) + 3A′′(sk)2/2|2 = |Q′′′k (sk)|2 ≤ D6 Qk 2E2K2(sk,sk)

= D6|A′(sk)2B(sk)2|. Hence, by Proposition 6 item (4) and hypothesis (2.21) we obtain

A′′′(sk) B(sk)

![image 154](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile154.png>)

<<D,δ 1. (2.24)

If we write Rk(z) = A(z)B(z)/(z − sk) for every k, we obtain |Rk′ (sk)|2 + |Rk′′(sk)|2 ≤ (D2 + D4) Rk 2E2K2(sk,sk)

≤ (D2 + D4) A(z)/(z − sk) 2EK2(sk,sk), which is equivalent to

|A′′(sk)B(sk)/2 + A′(sk)B′(sk)|2 + |A′′′(sk)B(sk)/3 + A′′(sk)B′(sk) + A′(sk)B′′(sk)|2

≤ 2(D2 + D4)|A′(sk)B(sk)|2. Dividing both sides by |A′(sk)B(sk)|2 we obtain

B′(sk) B(sk)

A′′(sk) 2A′(sk)

+

<<D 1 (2.25) and

![image 155](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile155.png>)

![image 156](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile156.png>)

A′′′(sk) 3A′(sk)

A′′(sk)B′(sk) A′(sk)B(sk)

B′′(sk) B(sk)

+

+

<<D 1. (2.26) Using (2.25) we obtain

![image 157](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile157.png>)

![image 158](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile158.png>)

![image 159](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile159.png>)

B′(sk) B(sk)

A′′(sk) A′(sk)

A′′(sk)/B(sk) A′(sk)/B(sk)

<<D,δ 1, (2.27) where the last inequality is due to Proposition 6 item (4) and (2.21). Using (2.26) we obtain

<<D 1 +

= 1 +

![image 160](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile160.png>)

![image 161](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile161.png>)

![image 162](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile162.png>)

B′′(sk) B(sk)

![image 163](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile163.png>)

<<D 1 +

A′′′(sk)/B(sk) A′(sk)/B(sk)

![image 164](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile164.png>)

+

A′′(sk)B′(sk) A′(sk)B(sk)

.

![image 165](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile165.png>)

Hence, by (2.21), (2.24) and (2.27) we obtain

B′′(sk) B(sk)

<<D,δ 1. (2.28) Thus, by (2.23), (2.24), (2.27) and (2.28) we obtain

![image 166](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile166.png>)

Pk 2E2 <<D,δ 1.

- Step 2. Since E(z)2 = A(z)2 − B(z)2 − i2A(z)B(z) and, by hypothesis, AB ∈/ H(E2) we conclude that A,B ∈/ H(E) and the functions

{A(z)B(z)/(z − sj)} ∪ {A(z)B(z)/(z − tj)} form an orthogonal basis of H(E2). We show that formula (1.7) holds for any of these functions, hence it holds for any ﬁnite linear combination of them. If we put F(z) = A(z)B(z)/(z − sj) on the right hand side of formula (1.7) we obtain

A(z)2

B(sj) A′(sj)(z − sj)2 −

![image 167](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile167.png>)

B(sj)A′′(sj) 2A′(sj)2(z − sj)

![image 168](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile168.png>)

+

B′(sj) A′(sj)(z − sj)

![image 169](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile169.png>)

+

n =j

B(sn) A′(sn)(z − sn)(sn − sj)

![image 170](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile170.png>)

.

This is equal to A(z)B(z)/(z −sj) by Lemma 3 formula (2.4). A similar argument would show that formula

- (1.7) holds for F(z) = A(z)B(z)/(z − tj), but now using Lemma 3 formula (2.5).


- Step 3. Now we prove that formula (1.7) converges in the norm of H(E2) for every F ∈ H(E2). Since AB ∈/ H(E2), by (2.2) and (2.16), if F ∈ H(E2) we have


+ |F(tn)|2 K2(tn,tn)

+ |F(tn)|2 B′(tn)A(tn)3

|F(sn)|2 |A′(sn)B(sn)3|

|F(sn)|2 K2(sn,sn)

π 2 n

F 2E2 =

=

. (2.29)

![image 171](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile171.png>)

![image 172](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile172.png>)

![image 173](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile173.png>)

![image 174](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile174.png>)

![image 175](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile175.png>)

n

Hence, to prove the convergence of formula (1.7) in the space H(E2), it is suﬃcient to show the following inequality

n∈I

znA′′(sn) A′(sn)3

zn A′(sn)2

wn A′(sn)2

Qn(z) −

Pn(z) +

Qn(z)

![image 176](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile176.png>)

![image 177](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile177.png>)

![image 178](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile178.png>)

2

E2

<<D,δ

n∈I

+ |wn|2 |A′(sn)B(sn)3|

|zn|2 |A′(sn)B(sn)3|

![image 179](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile179.png>)

![image 180](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile180.png>)

(2.30)

for every ﬁnite set I ⊂ Z and complex numbers {zn,wn}n∈I. This would show, together with (2.29), that the partial sums of formula (1.7) form a Cauchy sequence in the norm · E2 for all F ∈ H(E2).

By Lemma 5 formula (2.13) the functions {Qn(z)} are orthogonal, thus

2

znA′′(sn) A′(sn)3

+ |znA′′(sn)|2 |A′(sn)|6

|wn|2 |A′(sn)|4

wn A′(sn)2

Qn(z) −

Qn(z)

<<D

![image 181](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile181.png>)

![image 182](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile182.png>)

![image 183](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile183.png>)

![image 184](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile184.png>)

E2

n∈I

n∈I

|wn|2 |A′(sn)B(sn)3|

+ |zn|2 |A′(sn)B(sn)3|

<<D,δ

,

![image 185](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile185.png>)

![image 186](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile186.png>)

n∈I

where the ﬁrst inequality is due to orthogonality and estimate (2.22) of Step 1. The last inequality is due to

- (2.21) and Proposition 6 item (4). Analogously, by Lemma 5 formula (2.12) and Step 1, we obtain


zn A′(sn)2

Pn(z)

![image 187](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile187.png>)

n∈I

2

E2

=

<<D

znzm A′(sn)2A′(sm)2

![image 188](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile188.png>)

![image 189](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile189.png>)

n,m∈I

Pn,Pm E2

|znzm| A′(sn)2A′(sm)2(sn − sm)2

+

![image 190](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile190.png>)

{n =m}⊂I

|zn|2 A′(sn)4

.

![image 191](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile191.png>)

n∈I

The ﬁrst term on the right hand side of the last inequality is in the form of a Hilbert-type sum as in Proposition 7, at the points ξn = sn and an = |zn|/A′(sn)2. By Proposition 6, the zeros of A(z) are separated with width of separation depending only on D. Hence we can apply Proposition 7 to obtain

zn A′(sn)2

Pn(z)

![image 192](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile192.png>)

n∈I

2

|zn|2 A′(sn)4

<<D,δ

<<D

![image 193](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile193.png>)

E2

n∈I

n∈I

This proves the desired inequality (2.30). Also note that if we deﬁne

|zn|2 |A′(sn)B(sn)3|

.

![image 194](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile194.png>)

A(z)2

F0(z) = lim

N→∞

|k|≤N

then by (2.29) and (2.30) we have

F(sk) A′(sk)2(z − sk)2

+

![image 195](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile195.png>)

F′(sk)A′(sk) − F(sk)A′′(sk) A′(sk)2(z − sk)

![image 196](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile196.png>)

, (2.31)

F0 2E2 <<D,δ

k

|F(sk)|2 + |F′(sk)|2 K2(sk,sk) ≤ (1 + D2) F 2E2. (2.32)

![image 197](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile197.png>)

- Step 4. Now we ﬁnish the proof. Take F ∈ H(E2) and denote by F0 ∈ H(E2) the function given by the formula (2.31). Note that the F0(z) is well deﬁned due to Step 3. We claim that F = F0. Given ε > 0, by Steps 2 and 3 there exists a function G ∈ H(E2) such that the formula holds and F − G E2 < ε, which implies F′ − G′ E2 < Dε. We obtain


|F(sn) − G(sn)|2 |A′(sn)B(sn)3|

+ |F′(sn) − G′(sn)|2 |A′(sn)B(sn)3|

F − F0 2E2 < 2ε2 + 2 F0 − G 2E2 <<D,δ 2ε2 +

![image 198](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile198.png>)

![image 199](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile199.png>)

n

≤ 2ε2 + F − G 2E2 + F′ − G′ 2E2 < 3ε2 + D2ε2,

where the second inequality is due to (2.32) and the third due to (2.29). Since ε > 0 is arbitrary, we conclude the proof.

- 2.3. Proof of Corollary 2. By the Plancherel-Po´lya Theorem (see [35]) PW(a,2) is closed by diﬀeren-


tiation. Denote by K2(w,z) the reproducing kernel of H(E2) and note that H(w,z) = sin(π(az(−z−ww))) is the reproducing kernel of PW(a,2). Since PW(a,2) = H(E2) as sets, by the Closed Graph Theorem there exists

![image 200](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile200.png>)

![image 201](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile201.png>)

![image 202](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile202.png>)

a constant C > 0 such that

C−1 F L2(R) ≤ F E2 ≤ C F L2(R), (2.33) for every F ∈ PW(a,2). The reproducing kernel property implies that

K2(w,w) = sup{|F(w)|2 : F ∈ PW(a,2), F E2 ≤ 1} and

sin(a(w − w)) π(w − w)

![image 203](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile203.png>)

= sup{|F(w)|2 : F ∈ PW(a,2), F L2(R) ≤ 1} for every w ∈ C. We conclude that

![image 204](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile204.png>)

![image 205](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile205.png>)

K2(t,t) ≃a,C 1 (2.34) for all real t. Since |E(t)|4ϕ′(t) = π2K2(t,t), and |A(t)| ≤ M whenever B(t) = 0, we conclude that

![image 206](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile206.png>)

1 <<C,a,M ϕ′(t) whenever B(t) = 0.

We claim that AB ∈/ PW(a,2). Since H(E2) = PW(a,2) we easily obtain that H(Ea2) = PW(π,2) where Ea(z) = E(πaz). Since PW(π,2) is closed by diﬀerentiation, by Proposition 6, the real zeros of

![image 207](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile207.png>)

- L(z) = A(πaz)B(πaz) are separated. Hence, we can apply [34, Theorem 1] to conclude that the sequence {t ∈ R : L(t) = 0} is sampling for PW(π,2), that is


![image 208](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile208.png>)

![image 209](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile209.png>)

|F(t)|2

|F(x)|2dx ≃

R

L(t)=0

for every F ∈ PW(π,2). Thus AB ∈/ PW(a,2), otherwise L(z) would belong to PW(π,2) and have zero norm, a contradiction. We conclude that all the conditions of Theorem 1 are satisﬁed for H(E2) and α = 0. By the interpolation formula (1.7), the proof of Theorem 1 and estimates (2.32), (2.33) and (2.34), the corollary easily follows.

Remark: By Proposition 6 item (5) and inequalities (2.19) and (2.34) we conclude that

|A(t)|4 ≤ π|t − s|2ϕ′(s)K2(t,t) << |t − s|2, whenever B(t) = 0 and A(s) = 0. Hence, the condition

|t − s| < ∞

sup

inf

A(s)=0

B(t)=0

ensures the existence of a number M > 0 such that |A(t)| ≤ M whenever B(t) = 0.

3. Lp de Branges spaces

- 3.1. Preliminaries. Recall that we denote by U the open upper half-plane. For a given p ∈ (0,∞] we deﬁne the Hardy space Hp(U) as the space of functions F : U → C analytic in U such that


F(· + iy) p < ∞,

sup

y>0

where · p stands for the standard Lp(R,dx)-norm. In the case p ∈ [1,∞] it can be proven that for every F ∈ Hp(U) the limit

F(x) = lim

F(x + iy)

y→0

exists for almost every real x and deﬁnes a function in Lp(R,dx). Moreover, the following Poisson representation holds

y π R

Re F(t) (x − t)2 + y2

Re F(z) =

dt. Using this representation and Young’s inequality for convolutions, one can deduce that supy>0 F(·+iy) p = F p and Hp(U) is a Banach space for p ≥ 1. All these facts are contained in [1]. The next proposition provides a diﬀerent deﬁnition of the spaces Hp(E).

![image 210](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile210.png>)

![image 211](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile211.png>)

- Proposition 8. Let F(z) be an analytic function on the upper half-plane that has a continuous extension to the closed upper half-plane. The following are equivalent:


- (1) supy>0 F(· + iy) p < ∞
- (2) F(z) is of bounded type in U with non-positive mean type and F p < ∞.


- Proof. First we prove (2) =⇒ (1). Since F(z) is of bounded type with non-positive mean type we have (see [6, Problem 27])


log |F(t)| (x − t)2 + y2

y π R

log |F(z)| ≤

dt. Jensen’s inequality implies that

![image 212](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile212.png>)

![image 213](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile213.png>)

|F(t)| (x − t)2 + y2

y π R

|F(z)| ≤

dt. Applying Young’s inequality for convolutions and Fatou’s lemmma we conclude that sup

![image 214](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile214.png>)

![image 215](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile215.png>)

F(· + iy) p = F p. For (1) =⇒ (2) we use the fact that

y>0

y π R

ReF(t) (x − t)2 + y2

Re F(z) =

dt

![image 216](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile216.png>)

![image 217](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile217.png>)

in U (see [1, Theorem 7.14]). Write Re F(t) = g(t) − h(t), where g(t) = max{ReF(t),0} and h(t) = max{−ReF(t),0}. Let G(z) and H(z) be analytic functions in U such that

y π R

g(t) (x − t)2 + y2

dt and

Re G(z) =

![image 218](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile218.png>)

![image 219](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile219.png>)

h(t) (x − t)2 + y2

y π R

dt.

Re H(z) =

![image 220](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile220.png>)

![image 221](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile221.png>)

Since Re H(z) > 0 and Re G(z) > 0 in U, we conclude that G(z) and H(z) are of bounded type with nonpositive mean type (see [6, Problem 20]). Since F(z) diﬀers from G(z) − H(z) by a constant, we conclude that F(z) is of bounded type with non-positive mean type.

Remark: The above proposition implies that F ∈ Hp(E) if and only if sup

F(· + iy)/E(· + i|y|) p < ∞,

y∈R

or equivalently, if F/E and F∗/E belong to Hp(U). It can be proven, using the completeness of Hardy spaces and the reproducing kernel property (1.5) that the spaces Hp(E) are Banach spaces for p ≥ 1.

The next three lemmas are technical tools needed for the full proof of Theorem 1.

- Lemma 9. Let E(z) be a Hermite-Biehler function such that ϕ′(x) is bounded. Then Hp(E) ⊂ Hq(E) continuously if 1 ≤ p < q < ∞.

Proof. First we show that Hp(E) ⊂ H∞(E) if p ∈ [1,2].

Recall that ϕ′(x) = πK(x,x)/|E(x)|2 and denote by C its supremum. By the reproducing kernel property we obtain

K(t,·) 2E = K(t,t) ≤ C|E(t)|2/π for all real t. In the same way, noting that

K(t,·) 2E,∞ = sup x∈R

K(t,x) E(x)

![image 222](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile222.png>)

2

,

and K(t,x)2 ≤ K(x,x)K(t,t), we conclude that

K(t,·) 2E,∞ ≤ C2|E(t)|2/π2. Hence, we obtain that for all q ∈ [2,∞]

K(t,·) E,q ≤ (C/π)1−1/q|E(t)|. (3.1) If p ∈ [1,2] and F ∈ Hp(E), then for all t ∈ R

|F(t)/E(t)| ≤ F E,p K(t,·) E,p′/|E(t)| ≤ F E,p(C/π)1/p.

This implies the proposed inclusions for 1 ≤ p < q ≤ ∞ and p ≤ 2. By [3, Proposition 1.1] and [19, Lemma 4.2] the dual space of Hp(E) can be identiﬁed with Hp

′

(E) if 1 < p < ∞. This implies the remaining inclusions. Since convergence in the space implies convergence on compacts sets of C we conclude that the identity map from Hp(E) to Hq(E) is closed, hence continuous by the Closed Graph Theorem.

- Lemma 10. Let E(z) be a Hermite-Biehler function such that ϕ′(x) is bounded. Let α ∈ R be such that

- Bα ∈/ H(E). Then the linear span of the following set of functions {Bα(z)/(z − t)}t∈T (α)


is dense in Hp(E) for every p ∈ [2,∞).

Proof. Denote by S the closure of this span in Hp(E). Suppose by contradiction that S = Hp(E). By the Hahn-Banach Theorem there exists a non-zero functional Λ ∈ Hp(E)′ that vanishes on S. Since Hp(E)′ = Hp

′

(E), we conclude that Λ = Λ(z) is an entire function that belongs to Hp

′

(E) and Λ(t) = Λ,K(t,·) E = 0

for every t ∈ T (α), since K(t,z) is a multiple of Bα(z)/(z − t) for every t ∈ T (α). By Lemma 9, Hp

′

(E) ⊂ H(E). Since Bα ∈/ H(E), the set {Bα(z)/(z − t)}t∈T (α) forms an orthogonal basis of H(E) and we conclude by (2.2) that Λ ≡ 0, a contradiction.

- Lemma 11. Let E(z) be a Hermite-Biehler function such that ϕ′(x) ≤ C for every real x. Then for every p ∈ [1,2], every real number α and every F ∈ Hp(E) we have


|F(t)| (1 + |t|)K(t,t)1/2

<<C,p F E,p. (3.2)

![image 223](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile223.png>)

t∈T (α)

This inequality is also valid for p ∈ (2,∞) if we additionally assume that v(E∗/E) < 0.

Proof. By hypothesis, if t < t′ are two consecutive points in T (α), we have π = (t′ − t)ϕ′(r) for some r ∈ (t,t′). We conclude that the points T (α) are π/C-separated. We divide the proof in steps.

- Step 1. The inequality (3.2) is valid for p ∈ [1,2].

By Lemma 9 we have Hp(E) ⊂ H(E) continuously, thus the case p < 2 follows directly from the case p = 2. Let F ∈ H(E), by the Cauchy-Schwarz inequality we have

t∈T (α)

|F(t)| (1 + |t|)K(t,t)1/2 ≤

![image 224](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile224.png>)

t∈T (α)

|F(t)|2 K(t,t)

![image 225](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile225.png>)

1/2

t∈T (α)

(1 + |t|)−2

1/2

<<C F E,

where the last inequality is due to (2.2) and the separability of T (α).

- Step 2. The case p > 2.

By hypothesis, let v(E∗/E) = −2a < 0. Fix a real number ν such that ν ∈ (−1/p,0). Let Eν(z) be the function deﬁned in Section 4.1 and deﬁne the operator L : Hp(E) → H(E2) by LF(z) = e−iazEν(az)E∗(z)F(z). By the properties described in Section 4.1 we have

- (i) v(Eν∗) ≤ v(Eν) = τ(Eν) = 1;
- (ii) |Eν(t)| ≃ 1/|t|ν+1/2 , for |t| ≥ 1.


Hence, if G(z) = LF(z) we obtain

v(G/E2) = v(F/E) + v(E∗/E) + v(Eν(az)) + v(e−iaz) ≤ 0 − 2a + a + a = 0 and

v(G∗/E2) = v(F∗/E) + v(Eν∗(az)) + v(eiaz) ≤ 0 + a − a = 0. We also have

R

|G(t)/E(t)2|2 dt ≤

R

|Eν(at)|qdt

2/q

F 2E,p <<a,p F 2E,p, (3.3) where 1/2 = 1/q+1/p. Note that q > 2 and q(ν +1/2) > 1. We conclude that the operator L is well-deﬁned and continuous. Denoting by K2(w,z) the reproducing kernel of H(E2) and K(w,z) the reproducing kernel of H(E) we obtain K2(t,t) = 2|E(t)|2K(t,t). We have

t∈T (α)

|F(t)| (1 + |t|)K(t,t)1/2

![image 226](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile226.png>)

=

t∈T (α)

√2|G(t)| |Eν(at)|(1 + |t|)K2(t,t)1/2

![image 227](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile227.png>)

![image 228](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile228.png>)

≤

t∈T (α)

2|G(t)|2 K2(t,t)

![image 229](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile229.png>)

1/2

t∈T (α)

1 |Eν(at)|2(1 + |t|)2)

![image 230](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile230.png>)

1/2

<<C,a,p G E2 <<C,a,p F E,p ,

where the ﬁrst inequality is due to the Cauchy-Schwarz inequality, the second inequality due to (2.2) and the last one due to (3.3).

- 3.2. Proof of Theorem 1 - The general case.


- Step 1. The case p ∈ [1,2].


As in the proof for the case p = 2 we can assume that α = −π/2, which implies Bα(z) = A(z). Since the space H(E2) is closed by diﬀerentiation we can apply Proposition 6 to conclude that ϕ′(x) is bounded. By Lemma 9 we have Hp(E2) ⊂ H(E2). Hence, formula (1.7) holds for every F ∈ Hp(E2), where the convergence is taken in H(E2).

- Step 2. Preparation for the case p ∈ (2,∞).

For 2 < p < ∞ note that if F ∈ Hp(E2) then Gw(z) = [F(z)A(w)2 − A(z)2F(w)]/(z − w) belongs to H(E2) for every w ∈ C. By Step 1, we can apply formula (1.7) to obtain

F(z) A(z)2 −

![image 231](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile231.png>)

F(w) A(w)2

![image 232](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile232.png>)

=

n

F(sn) A′(sn)2(z − sn)2

![image 233](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile233.png>)

+

F′(sn) A′(sn)2(z − sn) −

![image 234](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile234.png>)

F(sn)A′′(sn) A′(sn)3(z − sn) −

![image 235](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile235.png>)

F(sn) A′(sn)2(w − sn)2 −

![image 236](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile236.png>)

F′(sn) A′(sn)2(w − sn)

![image 237](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile237.png>)

+

F(sn)A′′(sn) A′(sn)3(w − sn)

![image 238](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile238.png>)

(3.4)

for every w,z ∈ C. Note that, for every w ∈ C \ {sn} the sum converges uniformly on compact sets of C \ {sn}. If we denote by K2(w,z) the reproducing kernel of H(E2) and use the hypothesis that ϕ′(sn) = |A′(sn)/B(sn)| ≥ δ for every n, together with (2.16), we obtain

K2(sn,sn)1/2 <<δ A′(sn)2 for every n. (3.5) Since H(E2) is closed by diﬀerentiation and v(E∗/E) < 0, we can apply [3, Theorem A] to conclude that

- E′/E ∈ H∞(U). Again by [3, Theorem A] the space Hp(E2) is closed by diﬀerentiation. Since ϕ′(x) is bounded, we can apply Lemma 11 together with estimate (3.5), to obtain


n

|F(sn)| + |F′(sn)| (1 + |sn|)A′(sn)2

![image 239](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile239.png>)

< ∞ (3.6)

for every F ∈ Hp(E2). Since |A′(sn)/B(sn)| ≥ δ for every n we can apply Proposition 6 item (4) to conclude that |A′′(sn)/A′(sn)| <<D,δ 1 for all n. These facts imply that the series

n

F(sn) A′(sn)2(z − sn)2

![image 240](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile240.png>)

+

F′(sn) A′(sn)2(z − sn) −

![image 241](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile241.png>)

F(sn)A′′(sn) A′(sn)3(z − sn) converges uniformly on compact sets contained in C \ {sn}.

![image 242](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile242.png>)

By (3.4) we deduce that F(z) = c(F)A(z)2 + A(z)2

n

F(sn) A′(sn)2(z − sn)2

![image 243](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile243.png>)

+

F′(sn) A′(sn)2(z − sn) −

![image 244](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile244.png>)

F(sn)A′′(sn) A′(sn)3(z − sn)

![image 245](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile245.png>)

(3.7)

for some complex number c(F).

- Step 3. Finishing the proof for p ∈ (2,∞).


To ﬁnish the proof we will show that c(F) is a continuous linear functional over Hp(E2) that vanishes in a dense set of functions, hence it is identically zero. By (1.6) we have |F(i)| << F E2,p and by Lemma 11 we have

F′(sn) A′(sn)2(i − sn) −

F(sn)A′′(sn) A′(sn)3(i − sn)

F(sn) A′(sn)2(i − sn)2

+

<< F E2,p.

![image 246](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile246.png>)

![image 247](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile247.png>)

![image 248](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile248.png>)

n

- By (3.7) we conclude that |c(F)| << F E2,p, hence c(·) is a bounded linear functional over Hp(E2). Since AB ∈/ H(E2) we can apply Lemma 10 to deduce that the set of functions


{A(z)B(z)/(z − tn)} ∪ {A(z)B(z)/(z − sn)}

is dense in Hp(E2). Using formulas (2.3) - (2.5) we see that c(F) = 0 for any of the above functions, hence c(·) ≡ 0. This concludes the proof.

Remark: Note that, by the previous proof for the case p ∈ (2,∞), the additional assumption v(E∗/E) < 0 can be replaced by the following assumption

|F(t)| + |F′(t)| (1 + |t|)K2(t,t)1/2

<< F E2,p for every F ∈ Hp(E2). (3.8)

![image 249](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile249.png>)

t∈T (α)

In the next section we shall use condition (3.8) to obtain the Theorem 1 in the range p ∈ (2,∞) for homogeneous spaces of entire functions.

4. Applications

- 4.1. Homogeneous de Branges Spaces. There is a variety of examples of de Branges spaces [6, Chapter 3] for which Theorem 1 may be applied. A basic example would be the classical Paley-Wiener space H(e−iτz) which gives us the previous results obtained by J. Vaaler in [37, Theorem 9]. Another interesting family arises in the discussion of [24, Section 5]. In the terminology of de Branges [6, Section 50], these are examples of homogeneous spaces, and we brieﬂy review their construction below (see also [5]).


Let ν > −1 be a parameter and consider the real entire functions Aν(z) and Bν(z) given by

(−1)n 12z 2n n!(ν + 1)(ν + 2)...(ν + n)

∞

= Γ(ν + 1) 12z −ν Jν(z) (4.1) and

![image 250](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile250.png>)

Aν(z) =

![image 251](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile251.png>)

![image 252](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile252.png>)

n=0

(−1)n 12z 2n+1 n!(ν + 1)(ν + 2)...(ν + n + 1)

∞

= Γ(ν + 1) 2 1z −ν+1 Jν+1(z), (4.2) where Jν(z) denotes the classical Bessel function of the ﬁrst kind given by

![image 253](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile253.png>)

Bν(z) =

![image 254](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile254.png>)

![image 255](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile255.png>)

n=0

(−1)n(12z)2n+ν n!Γ(ν + n + 1)

![image 256](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile256.png>)

Jν(z) =

.

![image 257](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile257.png>)

n≥0

If we write z = x + iy then, for every ν > −1, we have

![image 258](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile258.png>)

2 πz

cos(z − νπ/2 − π/4) + e|y|O(1/|z|) (4.3)

Jν(z) =

![image 259](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile259.png>)

for x > 0. This estimate can be found in [38, Section 7.21]. If we write

Eν(z) = Aν(z) − iBν(z), then the function Eν(z) is a Hermite-Biehler function with no real zeros. Moreover, it is of bounded type in U and of exponential type in C, with v(Eν) = τ(Eν) = 1. Observe that when ν = −1/2 we have simply A−1/2(z) = cosz and B−1/2(z) = sinz.

These special functions also satisfy the following diﬀerential equations

- A′ν(z) = −Bν(z)
- Bν′ (z) = Aν(z) − (2ν + 1)Bν(z)/z.


(4.4)

- By (4.1), (4.2) and (4.3) we have |Eν(x)|−2 ≃ν |x|2ν+1 (4.5)


and

|x|2ν+1|Aν(x)Bν(x)| = Cν |sin(2x − νπ)| + O(1/|x|) (4.6)

for |x| ≥ 1. We conclude that AνBν ∈/ H(Eν2). Also, by (4.4) we have i

Eν′ (z) Eν(z)

Bν(z) zEν(z)

= 1 − (2ν + 1)

. (4.7)

![image 260](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile260.png>)

![image 261](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile261.png>)

for all real z ∈ U. Hence [Eν′ (z)/Eν(z)] ∈ H∞(U).

Denoting by ϕν(z) the phase function associated with Eν(z) and using the fact that ϕ′ν(t) = Re [iEν′ (t)/Eν(t)] for all real t, we can use (4.7) to obtain

(2ν + 1)Aν(t)Bν(t) t|Eν(t)|2

ϕ′ν(t) = 1 −

. Hence,

![image 262](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile262.png>)

ϕ′ν(t) ≃ν 1 for all real t. (4.8) For each F ∈ H(Eν) we have the remarkable identity

∞

∞

|F(x)|2 |Eν(x)|−2 dx = cν

|F(x)|2 |x|2ν+1 dx, (4.9)

−∞

−∞

with cν = π 2−2ν−1 Γ(ν +1)−2. Using the fact that Eν(z) is of bounded type, we can apply Krein’s Theorem (see [26] and [24, Lemma 12]) together with (4.5) and (4.9) to conclude that F ∈ H(Eν) if and only if F has exponential type at most 1 and either side of (4.9) is ﬁnite. Again, by Krein’s Theorem, F ∈ Hp(Eν2) if and only if F(z) has exponential type at most 2 and F/Eν2 ∈ Lp(R,dx).

For ν > −1/2, the Hankel’s integral for Jν(z) is given by

(z/2)ν Γ(ν + 1/2)√π

1

- 1

![image 263](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile263.png>)

- 2 ds.


eisz(1 − s2)ν−

Jν(z) =

![image 264](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile264.png>)

![image 265](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile265.png>)

−1

This formula can be found in [4, Section 93]. Using (4.1) - (4.2) and an integration by parts, we deduce the following integral representation

Γ(ν + 1) Γ(ν + 1/2)√π

Eν(z) =

![image 266](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile266.png>)

![image 267](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile267.png>)

1

- 1

![image 268](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile268.png>)

- 2(1 − s)ds.


eisz(1 − s2)ν−

−1

By simple estimates, we deduce from the above representation that v(Eν∗) = 1 for ν > −1/2. Thus, we cannot directly apply Theorem 1 for homogeneous spaces in the case p > 2. Nevertheless, we will prove Theorem 1 for these homogeneous spaces by verifying that the alternative condition (3.8) holds.

- Lemma 12. Let ν > −1. The space Hp(Eν2) satisﬁes the following properties:


- (1) Hp(Eν2) ⊂ Hq(Eν2) if 0 < p < q ≤ ∞.
- (2) Hp(Eν2) is closed by diﬀerentiation for every p ∈ [1,∞].
- (3) If p ∈ [1,∞) there exists a constant Cν,p > 0 such that


|F(t)| + |F′(t)| (1 + |t|)K2,ν(t,t)1/2 ≤ Cν,p F E2 ν,p for every F ∈ Hp(Eν2),

![image 269](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile269.png>)

t∈Tν(α)

where the function K2,ν(w,z) denotes the reproducing kernel of H(Eν2) and Tν(α) = {t ∈ R : ϕν(t) ≡ α(mod π)}.

Proof. First we prove item (1). Deﬁne an auxiliary function Ψ(z) in the following way. If 2ν + 1 < 1 write Ψ(z) = Eσ(z)2 where 2ν + 1 = −(2σ + 1). If 2ν + 1 ≥ 1, let k ≥ 1 be a positive integer such that k ≤ 2ν +1 < k +1 and deﬁne Ψ(z) = E−3/4(z)4kEσ(z)2 where 2σ +1 = (k −2ν −1). We conclude that Ψ(z) is of exponential type and, by (4.5), |Ψ(x)| ≃ν |x|2ν+1 for |x| ≥ 1. By (4.7) and some simple calculations we have |Ψ′(t)| << |Ψ(t)| for all real t. Also, by redeﬁning Ψ(˜ z) = Ψ(az) for some a > 0, we can suppose that Ψ(z) has exponential type 1.

We conclude that F ∈ Hp(Eν2) if and only if F(z) is of exponential type at most 2 and FΨ ∈ Lp(R,dx). Thus, Ψ(z)Hp(Eν2) ⊂ PW(3,p), where PW(3,p) is the Paley-Wiener space deﬁned in Subsection 1.2. The Plancherel-Po´lya Theorem (see [35]) implies that PW(a,p) ⊂ PW(a,q) for every a > 0 and 0 < p < q ≤ ∞. We conclude that FΨ ∈ PW(3,q) for every F ∈ Hp(Eν). This proves item (1).

Now we prove item (2). If F ∈ Hp(Eν2) does not have zeros then, since it is of exponential type at most 2, we deduce that F(z) = aebz for some a,b ∈ C with |b| ≤ 2. Then F′ = bF and trivially F′ ∈ Hp(Eν2). If F(z) has a zero z = w then G(z) = F(z)/(z −w) is of exponential type at most 2 and G ∈ Lp(R,dx). By the Plancherel-Po´lya Theorem, G′ ∈ Lp(R,dx) and has exponential type at most 2. Hence F′(z) has exponential type at most 2. On the other hand, FΨ ∈ Lp(R,dx) and again this implies that (FΨ)′ ∈ Lp(R,dx). Since F′Ψ = (FΨ)′ − FΨ′ and |Ψ′(t)| << |Ψ(t)| for all real t, we conclude that F′Ψ ∈ Lp(R,dx). Hence

- F′ ∈ Hp(Eν2). Finally we prove item (3). By item (2) it is suﬃcient to prove that


|F(t)| (1 + |t|)K2,ν(t,t)1/2

ν,p, for every F ∈ Hp(Eν2).

<<p,ν F E2

![image 270](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile270.png>)

t∈Tν(α)

By (4.8) we conclude that K2,ν(t,t)1/2 ≃ |Eν(t)|2 for all real t and Tν(α) is separated with width of separation depending only on ν. We can use Ho¨lder’s inequality to conclude that

|F(t)| (1 + |t|)K2,ν(t,t)1/2

<<p,ν

![image 271](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile271.png>)

t∈Tν(α)

Hence, we only need to show that

t∈Tν(α)

F(t) Eν(t)2

![image 272](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile272.png>)

p

<<p,ν

t∈Tν(α)

p 1/p

F(t) Eν(t)2

.

![image 273](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile273.png>)

R

F(t) Eν(t)2

![image 274](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile274.png>)

p

dt (4.10)

for all F ∈ Hp(Eν2). Since ΨF ∈ Lp(R,dx) and Tν(α) is separated, we can apply the Plancherel-Po´lya Theorem to obtain

|F(t)Ψ(t)|p <<p,ν

|F(t)Ψ(t)|p dt

R

t∈Tν(α)

for every F ∈ Hp(Eν2). This implies (4.10) and concludes the lemma.

Remark: The proof of item (2) is inspired in the proof of [13, Theorem 20].

From Lemma 12 and condition (3.8) we conclude the validity of the interpolation formula (1.7) for these homogeneous spaces of entire functions, summarized in the next theorem (with E(z) = Eν(z) for α = 0 and α = −π/2). Due to identities (4.1) - (4.2), this can also be seen as an independent contribution to the theory of Bessel functions.

- Theorem 13. Let p ∈ (0,∞) and ν > −1. Let F(z) be an entire function of exponential type at most 2 such that


F(t)|t|2ν+1 p dt < ∞. Then

|t|≥1

F′(s) A′ν(s)2(z − s)

F(z) Aν(z)2

F(s) sA′ν(s)2(z − s) and

F(s) A′ν(s)2(z − s)2

+ (2ν + 1)

=

+

![image 275](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile275.png>)

![image 276](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile276.png>)

![image 277](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile277.png>)

![image 278](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile278.png>)

Aν(s)=0

Aν(s)=0

F′(t) Bν′ (t)2(z − t)

F(t) Bν′ (t)2(z − t)2

F(t) tBν′ (t)2(z − t)

F(z) Bν(z)2

+ (2ν + 1)

=

+

,

![image 279](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile279.png>)

![image 280](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile280.png>)

![image 281](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile281.png>)

![image 282](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile282.png>)

Bν(t)=0

Bν(t)=0

t =0

where these series converge uniformly on compact sets of C away from their respective singularities.

- 4.2. Extremal Functions. The purpose of this subsection is to prove a uniqueness result for some extremal problems described below. Let d denote the dimension. A set K ⊂ Rd is called a convex body if it is compact, convex, symmetric around the origin and has the origin as an interior point. Let | · | denote the Euclidean norm in Rd and B the compact Euclidean unit ball. Given a non-negative Borel measure µ on Rd and a real-valued function g(x) we denote by P+(g,K,µ) the set of measurable real-valued functions M(x) deﬁned on Rd satisfying the following conditions:


- (1) M(x) deﬁnes a tempered distribution such that its distributional Fourier transform M is supported on K.
- (2) g(x) ≤ M(x) for all x ∈ Rd.
- (3) M − g ∈ L1(Rd,µ).


In this case, we say that M(x) is a band-limited majorant of g(x). In an analogous way we deﬁne P−(g,K,µ) as the set of minorants. We are asked to minimize the quantities

Rd

M(x) − g(x) dµ(x) and

Rd

g(x) − L(x) dµ(x) (4.11)

among all functions M ∈ P+(g,K,µ) and L ∈ P−(g,K,µ). And, if the minimum is attained, characterize the set of extremal functions. We call M(x) (or L(x)) an extremal function if it minimizes the quantity (4.11).

The problem becomes treatable if we consider radial functions. For instance, we consider the situation where K = B, the function g(x) is radial, and

−1

dµE(x) = 2 |E(|x|)|2|x|d−1 Sd−1

dx, (4.12)

where Sd−1 denotes the area of the (d − 1)-dimensional sphere. Also, in this subsection, E(z) will always denote a Hermite-Biehler function of bounded type and mean type equal to π such that H(E2) is closed by diﬀerentiation and ϕ′(t) is bounded away from zero over the zero set of A(z) and B(z). We also assume that E∗(−z) = E(z) and AB ∈/ H(E2). This implies that the companion functions A(z) and B(z) are respectively even and odd and A,B ∈/ H(E). By Krein’s Theorem, E(z) is of exponential type with τ(E) = v(E) = π, and F ∈ H(E) if and only if F(z) is of exponential type at most π and F/E ∈ L2(R,dx) (see [24, Lemmas

- 9 and 12]).


These restrictions reduce the multidimensional problem to a one-dimensional problem and allow us to use de Branges space techniques. Constructions of extremal band-limited approximations of radial functions in

several variables were studied in [13, 14, 24]. In particular, E. Carneiro and F. Littmann [13, 14] were able to explicitly construct a pair of radial functions M ∈ P+(g,B,µE) and L ∈ P−(g,B,µE) that minimize the quantities in (4.11), where µE is given by (4.12), E(z) = Eν(z) and g(x) belongs to a vast class of radial functions with exponential or Gaussian subordination.

For the sake of completeness we state here a classical theorem about tempered distributions with Fourier transform supported on a ball. This result can be found in [25, Theorem 7.3.1].

- Theorem 14 (Paley–Wiener–Schwartz). Let F be a tempered distribution such that the support of F is contained in B. Then F : Cd → C is an entire function and there exist N,C > 0 such that


|F(x + iy)| ≤ C(1 + |x + iy|)Ne2π|y| for every x + iy ∈ Cd.

Conversely, every entire function F : Cd → C satisfying an estimate of this form deﬁnes a tempered distribution with Fourier transform supported on B.

The next propositions give an interpolation condition for a band-limited majorant or minorant to be extremal and unique in radial case. We highlight the fact that the uniqueness part below is a novelty in this multidimensional theory, and makes a crucial use of our interpolation formulas. This enhances the extremal results obtained in [13, 14].

- Proposition 15. Let g(x) = g(|x|) be a radial function that is diﬀerentiable for x = 0. Suppose that P+(g,B,µE) = ∅ and there exists a radial function L ∈ P−(g,B,µE) such that L(x) = g(x) whenever

- A(|x|) = 0. Then L is extremal and unique among the set of entire functions on Cd whose restriction to Rd is radial.

Proposition 16. Let g(x) = g(|x|) be a radial function that is diﬀerentiable for x = 0. Suppose that P−(g,B,µE) = ∅ and there exists a radial function M ∈ P+(g,B,µE) such that M(x) = g(x) whenever

- B(|x|) = 0. Then M is extremal and unique among the set of entire functions on Cd whose restriction to Rd is radial.




We only prove Proposition 16 since the other is analogous. Proof. Optimality.

Fix L ∈ P−(g,B,dµE). Let SO(d) denote the compact topological group of real orthogonal d×d matrices with determinant 1, with associated probability Haar measure σ. If R ∈ P+(g,B,µE), then

R˜(x) =

R(ρx)dσ(ρ)

SO(d)

is radial, belongs to P+(g,B,µE) and

R ˜(x) − M(x) dµE(x) =

Rd

Rd

R(x) − M(x) dµE(x). (4.13)

In the same way, we deﬁne L˜(x) as the radial symmetrization of L(x). Again we have L˜ ∈ P−(g,B,dµE). Deﬁne m(t) = M(te1), l(t) = L˜(te1) and r(t) = R˜(te1) for all real t, where e1 = (1,0,...,0). We can apply the Paley-Wiener-Schwartz Theorem to conclude that these functions extend to C as entire functions of exponential type at most 2π. By (4.12) we obtain that

Rd

R ˜(x) − M(x) dµE(x) =

{r(t) − m(t)}/|E(t)|2 dt. (4.14)

R

We claim that r − m = pp∗ − qq∗ for p,q ∈ H(E). Since m(x) − l(x) ≥ 0 and r(x) − l(x) ≥ 0 for all real x, we conclude that there exists two entire functions p(z) and q(z) of exponential type at most π such that m(z) − l(z) = p(z)p∗(z) and r(z) − l(z) = q(z)q∗(z) (see [6, Theorem 13]). Since m − l and r − l belong to L1(R,|E(x)|−2dx) we conclude that p,q ∈ H(E). We can apply formula (2.2) to obtain that

|p(t)|2 − |q(t)|2 K(t,t)

|p(t)|2 − |q(t)|2 |E(t)|2

{r(t) − m(t)}|E(t)|−2dt =

dt =

![image 283](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile283.png>)

![image 284](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile284.png>)

R

R

B(t)=0

r(t) − g(|t|) K(t,t) ≥ 0 ,

r(t) − m(t) K(t,t)

(4.15)

=

=

![image 285](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile285.png>)

![image 286](<2015-gonccalves-interpolation-formulas-derivatives-branges_images/imageFile286.png>)

B(t)=0

B(t)=0

where the last equality is due to the interpolation condition of M(x), that is, M(x) = g(x) whenever B(|x|) = 0. By (4.13), (4.14) and (4.15) we conclude that M(x) is extremal. Uniqueness.

Inequality (4.15) implies that if R ∈ P+(g,B,µE) is radial and extremal, then r(t) = g(|t|) whenever B(t) = 0. Since x ∈ Rd  → g(x) = g(|x|) is radial and diﬀerentiable for x = 0 we conclude that r′(t) = sgn(t)g′(|t|) if B(t) = 0 and t = 0. Also r′(0) = 0. Since f := (m − r) ∈ H1(E2) and f(t) = f′(t) = 0 whenever B(t) = 0, by Theorem 1 we conclude that f ≡ 0. Hence, M(x) is unique.

Remark: In some cases g(x) may have a singularity at x = 0, for instance if limx→0 g(x) = ∞. Thus, only the minorant problem is well-posed, that is P+(g,B,µE) = ∅. However, in the case of homogeneous spaces the previous proposition will still hold. In [13, Corollary 23], E. Carneiro and F. Littmann proved that every f ∈ H1(Eν2), not necessarily non-negative on the real axis, can be represented as f = pp∗ − qq∗ for p,q ∈ H(Eν). We can easily see that this representation is suﬃcient to prove the previous propositions for E(z) = Eν(z) in the case when g(x) has a singularity.

Acknowledgements

I am deeply grateful to my advisor Emanuel Carneiro for encouraging me to work on this problem and for all the fruitful discussions on the elaboration of this paper.

The author also acknowledges the support from CNPq–Brazil and FAPERJ–Brazil.

References

- [1] S. Axler, P. Bourdon and W. Ramey, Harmonic Function Theory, Graduated Texts in Mathematics 137, 1992.
- [2] A. Baranov, Diﬀerentiation in De Branges Spaces and Embedding Theorems, Journal of Mathematical Sciences 101, No. 2 (2000), 2881–2913.
- [3] A. Baranov, Estimates of the Lp-Norms of Derivatives in Spaces of Entire Functions, Journal of Mathematical Sciences 129, No. 4 (2005), 3927–2943.
- [4] F. Bowman, Introduction to Bessel Functions, Dover Publications, 1958.
- [5] L. de Branges, Homogeneous and Periodic Spaces of Entire Functions, Duke Math. Journal 29 (1962), 203–224.
- [6] L. de Branges, Hilbert Spaces of Entire Functions, Prentice-Hall Series in Modern Analysis, 1968.
- [7] E. Carneiro and V. Chandee, Bounding ζ(s) in the Critical Strip, J. Number Theory 131 (2011), 363–384.
- [8] E. Carneiro, V. Chandee, F. Littmann and M. B. Milinovich, Hilbert Spaces and the Pair Correlation of Zeros of the Riemann Zeta-Function, J. Reine Angew. Math (to appear).


- [9] E. Carneiro, V. Chandee and M. B. Milinovich, Bounding S(t) and S1(t) on the Riemann Hypothesis, Math. Ann. 356

(2013), 939–968.

- [10] E. Carneiro, V. Chandee and M. Milinovich, A note on the zeros of zeta and L-functions, Preprint.
- [11] E. Carneiro and F. Gon¸calves, Extremal Problemas in de Branges Spaces: The Case of Truncated and Odd Functions, Preprint.
- [12] E. Carneiro and F. Littmann, Bandlimited approximations to the truncated Gaussian and applications, Constr. Approx. 38 (2013), 19–57.
- [13] E. Carneiro and F. Littmann, Extremal Functions in de Branges and Euclidean Spaces, Adv. Math. 260 (2014), 281–349.
- [14] E. Carneiro and F. Littmann, Extremal functions in de Branges and Euclidean Spaces II, Preprint.
- [15] E. Carneiro, F. Littmann, and J. D. Vaaler, Gaussian Subordination for the Beurling-Selberg Extremal Problem, Trans. Amer. Math. Soc. 365 (2013), 3493–3534.
- [16] E. Carneiro and J. D. Vaaler, Some Extremal Functions in Fourier Analysis II, Trans. Amer. Math. Soc. 362 (2010), 5803–5843.
- [17] E. Carneiro and J. D. Vaaler, Some Extremal Functions in Fourier Analysis III, Constr. Approx. 31, No. 2 (2010), 259–288.
- [18] V. Chandee and K. Soundararajan, Bounding |ζ(1/2 + it)| on the Riemann Hypothesis, Bull. London Math. Soc. 43, No. 2 (2011), 243–250.
- [19] W. S. Cohn, Radial Limits and Star–Invariant Subspaces of Bounded Mean Oscillation, Amer. J. Math. 108 (1986), 719–749.
- [20] P. X. Gallagher, Pair Correlation of Zeros of the Zeta Function, J. Reine Angew. Math. 362 (1985), 72–86.
- [21] D. A. Goldston and S. M. Gonek, A Note on S(t) and The Zeros of the Riemann Zeta-function, Bull. London Math. Soc. 39 (2007), 482–486.
- [22] F. Gon¸calves, M. Kelly and J. Madrid, One-Sided Band-Limited Approximations in Euclidean Spaces of Some Radial Functions, Preprint.
- [23] S. W. Graham and J. D. Vaaler, A Class of Extremal Functions for the Fourier Transform, Transactions of the American Mathematical Society 265, No. 1 (1985), 283–302.
- [24] J. Holt and J. D. Vaaler, The Beurling-Selberg Extremal Functions for a Ball in the Euclidean space, Duke Mathematical Journal 83 (1996), 203–247.
- [25] L. H¨ormander, The Analysis of Linear Partial Diﬀerential Operators I, Springer-Verlag, 1983.
- [26] M. G. Krein, A Contribution to the Theory of Entire Functions of Exponential Type, Bull. Acad. Sci. URSS S´er. Math. [Izvestiya Akad. Nauk. SSSR] 11 (1947), 309–326.
- [27] F. Littmann, Entire Approximations to the Truncated Powers, Constr. Approx. 22, No. 2 (2005), 273–295.
- [28] F. Littmann, Entire majorants via Euler-Maclaurin summation, Trans. Amer. Math. Soc. 358, No. 7 (2006), 2821–2836.
- [29] F. Littmann, Quadrature and Extremal Bandlimited Functions, SIAM J. Math. Anal. 45, No. 2 (2013), 732–747.
- [30] F. Littmann and M. Spanier, Extremal functions with vanishing condition, preprint at http://arxiv.org/abs/1311.1157.
- [31] Y. Lyubarskii and K. Seip, Weighted Paley-Wiener Spaces, J. Amer. Math. Soc. 15, No. 4 (2002), 979–1006.
- [32] H. L. Montgomery, Ten Lectures on the Interface Between Analytic Number Theory and Harmonic Analysis, CBMS No. 84, Amer. Math. Soc., Providence, 1994.
- [33] H. L. Montgomery and R. C. Vaughan, Hilbert’s Inequality, J. London Math. Soc. 8, No. 2 (1974), 73–81.
- [34] J. Ortega-Cerd`a and K. Seip, Fourier frames, Ann. of Math. (2) 155, No. 3 (2002), 789–806.
- [35] M. Plancherel and G. Polya, Fonctions Enti´eres et Int´egrales de Fourier Multiples (Seconde partie), Comment. Math. Helv. 10 (1938), 110–163.
- [36] A. Selberg, Lectures on Sieves, Atle Selberg: Collected Papers, Vol. II, Springer-Verlag, 1991.
- [37] J. D. Vaaler, Some Extremal Functions in Fourier analysis, Bull. Amer. Math. Soc. 12 (1985), 183–215.
- [38] G. N. Watson, A Treatise on the Theory of Bessel Functions, Cambridge Mathematical Library Edition, 1995.


IMPA - Instituto de Matematica´ Pura e Aplicada - Estrada Dona Castorina, 110, Rio de Janeiro, RJ, Brazil 22460-320

E-mail address: ffgoncalves@impa.br

