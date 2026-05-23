arXiv:1507.04302v2[math.CA]26Jan2016

ON EXISTENCE OF EXTREMIZERS FOR THE TOMAS-STEIN INEQUALITY FOR S1

SHUANGLIN SHAO

Abstract. The Tomas-Stein inequality or the adjoint Fourier restriction inequality for the sphere S1 states that the mapping f  → fσ is bounded from L2(S1) to L6(R2). We prove that there exists an extremizer for this inequality. We also prove that any extremizer satisﬁes |f(−x)| = |f(x)| for almost every x ∈ S1.

1. Introduction

The Tomas-Stein inequality or the adjoint Fourier restriction inequality for the sphere S1 asserts that

- (1) fσ L6(R2) ≤ R f L2(S1,σ) where the constant R > 0 is deﬁned to be the optimal constant
- (2) R := sup{  fσ L6(R2) : f L2(S1,σ) = 1},

and σ denotes the surface measure on the unit sphere S1, and the Fourier transform is deﬁned by

- (3) f(ξ) := e−iξ·xf(x)dx.

- Deﬁnition 1.1. A function f ∈ L2(S1) is said to be an extremizer or an extremal for (1) if f = 0 a. e., and


- (4) fσ L6(R2) = R f L2(S1).


An extremizing sequence for the inequality (1) is a sequence {fν} ∈ L2(S1) satisﬁes

fν L2(S1) = 1 and limν→∞ fνσ L6(R2) = R. An extremizing sequence is said to be precompact if any subsequence has a sub-subsequence which is Cauchy in L2(S1).

This paper is devoted to studying the existence of extremals for this basic inequality and to characterizing some properties of extremizers. The main result is the following

- Theorem 1.2. There exists an extremal function for (1).

Moreover we show that the extremizers enjoy the following symmetry.

- Theorem 1.3. Every extremizer satisﬁes |f(−x)| = |f(x)| for almost every x ∈ S1. 1


In [12], for the adjoint Fourier restriction inequality for the sphere S2, we prove the existence of extremals by showing that any extremizing sequence of nonnegative functions is precompact in L2(S2); and the extremals satisfy |f(−x)| = |f(x)| for almost every x ∈ S2. We are also able to prove that constants are local extremals. Furthermore in [13], we show that nonnegative extremizers are indeed smooth, and completely characterize complex extremals: Any complex extremizer is of the form eixξf(x) for some nonnegative extremizer f and some ξ ∈ R3, and if {fν} is a complex extremizing sequence then there exists {ξν} such that {e−ix·ξνfν} is precompact. Recently, in [16], Foschi proves that constant functions are extremizers for the two dimensional sphere. In [14], Fanelli, Vega and Visciglia consider similar questions and establish existence for a family of non-endpoint Fourier restriction operators.

In the context of the adjoint Fourier restriction inequality for the paraboloid (or the Strichartz inequality for the Schro¨dinger equation), Kunze [18] proves the existence of extremals when the spatial dimension is one by a concentration-compactness argument. Foschi [15] proves that Gaussian functions are explicit extremals in spatial dimensions one and two by two successive applications of the Cauchy-Schwarz inequalities; independently Hundertmark and Zharnitsky [17] obtain similar results. Bennett, Bez, Carbery and Hundertmark [2] show that Gaussians are extremizers from the perspective of the heat-ﬂow deformation method [3, 4]. For non-L2 adjoint Fourier restriction inequality for paraboloids, Christ and Quilodra´n [11] show that Gaussians are rarely extremizers by studying the corresponding Euler-Lagrange equations. In higher dimensions, the existence result of extremizers is known, which is achieved by using the tool of proﬁle decompositions by the author [25]. In the context of a convolution inequality with the surface measures of the paraboloids, the existence of quasi-extremals and extremals was studied by Christ [8, 9].

The main results Theorem 1.2 and Theorem 1.3 are proven by following the framework designed in the paper [12]. To be more precise, the ﬁrst part of the analysis in this paper, Step 1 to Step 4, follows similarly as in [12] to obtain a nonnegative extremizing sequence fν which is “even upper normalized” with respect to a sequence of caps Cν. In the second part of the analysis, i.e., at the last Step 5, we develop a proﬁle decomposition for the adjoint sphere restriction operator in the spirit of [5, 7]. When f is supported on suﬃciently small caps on the sphere, we approximate fσ by linear Schro¨dinger waves. This idea appeared previously in [10] where the authors approximate the Airy wave at high frequency by a Schro¨dinger wave.

The analysis in this paper can be viewed as a manifestation of the the concentrationcompactness approach developed in a series of works by Lions [19, 20, 21, 22], which is however adapted to our case to cope with the nonlocal characteristics of the adjoint Fourier restriction operator.

We present the outline and results in detail in Section 2. Acknowledgements. The research of the author was supported by NSF DMS-1160981.

2. Outline of the proof and definitions

This section consists of notations, deﬁnitions and statements of some intermediate results which are not repeated subsequently. We start with several deﬁnitions. Let σP be the canonical measure on the parabola P = {(x, y) ∈ R2 : y = 12|x|2}, and set

![image 1](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile1.png>)

fσP L6(R2) f L2(P,σP)

- (5) ,

S := sup

fσ ∗ fσ ∗ fσ 1L/23(R3) f L2(S1,σ)

![image 2](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile2.png>)

- (6)

P := sup

fσP ∗ fσP ∗ fσP 1L/23(R3) f L2(P,σP)

![image 3](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile3.png>)

- (7) .

Note that by Plancherel’s theorem, R = 2πS, RP = 2πP. There holds that |fσ∗fσ∗fσ| ≤ |f|σ ∗ |f|σ ∗ |f|σ. If f is an extremizer to (1), so if |f|. This applies to any extremizing sequence {fν}. Thus in order to prove the existence of extermizers, we will restrict our attention to nonnegative functions and nonnegative extremizing sequences.

- Step 1, A strict comparison. By a dilation argument, we see that the sharp constants for the adjoint Fourier restriction inequalities for the sphere and the paraboloid satisfy,

- R ≥ RP, where RP is deﬁned in (5). This reasoning appears previously in [12]. Indeed, we take an extremizer for the paraboloid, which is known as Gaussians from [15] and [17], dilate it so that it is essentially supported in a suﬃciently small set of the paraboloid; we paste the extremizer onto the sphere in an obvious way and then osculate the sphere by the parabolic scaling (x′, xd) → (λx′, λ2xd) where x = (x′, xd) ∈ Rd and λ > 0. In the limits, we see that the relation R ≥ RP holds. So there arises the most severe obstruction to the existence of extremizers that, for an extremizing sequence {fν} satisfying fν 2 = 1, any subsequential weak limit of |fν|2 could conceivably converge to a Dirac mass at a point of S1. If it were the case, then R = RP. To rule out this scenery, an essential step is to prove R > RP. Because any extremal enjoys a symmetry |f(x)| = |f(−x)|, there is a possibility that the extremizing sequence might converge weakly to a linear combination of two Dirac masses at antipodal points of S1. To rule it out, one needs a strict comparison
- S > (5/2)1/6P, which is achieved by using a perturbation argument, which we sketch in Appendix A. Proposition 2.1.


(8) R > (5/2)1/6RP.

- Step 2, Antipodal symmetrization. We will show that “extremals” to (1) enjoy a symmetry |f(−x)| = |f(x)|.




RP := sup

![image 4](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile4.png>)

![image 5](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile5.png>)

- Deﬁnition 2.2. A complex-valued function f ∈ L2(S1) is said to be even if f(−x) = f(x) for almost every x ∈ S1. For nonnegative functions, this condition is simpliﬁed to f(−x) = f(x).


- Deﬁnition 2.3. Let f be nonnegative L2(S1) function. The antipodally symmetric rearrangement f⋆ is the unique non-negative element of L2(S1) which satisﬁes


- (9) f⋆(x) = f⋆(−x), for all x ∈ S1,
- (10) f⋆(x)2 + f⋆(−x)2 = f(x)2 + f(−x)2, for all x ∈ S1. In other words, f⋆ = f(x)

![image 6](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile6.png>)

2+f(−x)2

![image 7](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile7.png>)

2 and f⋆ 2 = f 2. Proposition 2.4. For any nonnegative function f ∈ L2(S1),

- (11) fσ ∗ fσ ∗ fσ 2 ≤ f⋆σ ∗ f⋆σ ∗ f⋆σ 2,

with strict inequality if and only if f = f⋆ almost everywhere. Consequently any extremizer for the inequality (1) satisﬁes |f(−x)| = |f(x)| for almost every x ∈ S1.

The analogue for S2 is establish in [12]. We remark that Foschi [16] has provided a much shorter proof for that by using the Cauchy-Schwarz inequality.

- Step 3, A reﬁnement of Tomas-Stein’s inequality. Similarly as in [12], we deﬁne what caps mean on S1.


Deﬁnition 2.5. The cap C = C(z, r) with center z ∈ S1 and radius r ∈ (0, 1] is the set of all points y ∈ S1 which lie in the same hemisphere as z and are centered at z, and which satisfy πH

z

(y) < r, where the subspace Hz ⊂ R2 is the orthogonal complement of z and πH

z

denotes the orthogonal projection onto Hz.

In [12], the reﬁnement of Tomas-Stein’s inequality for S2 developed by Bourgain [6] and Moyua, Vargas and Vega [23] provides some useful information on the near-extremals for the adjoint Fourier restriction inequality for S2: Any near extremal can be decomposed into a major part, which obey some upper bound in the point-wise sense, and a lower L2-norm bound, plus an error term. For S1, we have the following reﬁnement

Lemma 2.6. For f ∈ L2(S1). There exists α ∈ (0, 1) such that

- (12) fσ 6 ≤ sup


α

1 |C|1/2 C

f 1L−2(αS1), where C denotes a cap on S1.

|f|dσ

![image 8](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile8.png>)

C

We establish this lemma by using the bilinear restriction estimates for functions on S1 whose supports are “transverse”, i.e., the unit normals to each set are separated by an angle > 0. The argument is similar to that for [1, Theroem 1.3].

As a consequence of the reﬁnement in Lemma 2.6, we have

Proposition 2.7. For any δ > 0 there exists Cδ < ∞ and ηδ > 0 with the following properties. If f ∈ L2(S1) satisﬁes fσ 6 ≥ δR f 2, then there exists a decomposition

- f = g + h and a cap C satisfying that

- (13) 0 ≤ |g|, |h| ≤ |f|,
- (14) g, h have disjoint supports,
- (15) |g(x)| ≤ Cδ f 2|C|−1/2χC(x), ∀x,
- (16) g 2 ≥ ηδ f 2. Here both Cδ−1 and ηδ are proportional to δO(1). If f ≥ 0, g and h can be chosen such that


- g, h ≥ 0 almost everywhere.


- Step 4, Upper even normalized w.r.s.t the caps. As in [12], we introduce the notion of rescaling maps that pull back functions on S1 to R and obtain some preliminary control on the near-extremals.


- Deﬁnition 2.8 (Rescaling map φC). Let B ⊂ R denote the unit ball. To any cap of radius ≤ 1 is associated a rescaling map φC : B → C. For z = (0, 1), φC(y) = (ry, 1 − r2y2). For general z, deﬁne ψz(y) = r−1L(π(y)) where π is again the orthogonal projection onto Hz,

![image 9](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile9.png>)

L : Hz → R is an arbitrary linear isometry and φC = ψ−1

z .

For a cap C = C(z, r), we remark that φC is naturally extended to deﬁned on the set {y : |y| < r}.

- Deﬁnition 2.9 (Pullbacks). Deﬁne the pullbacks φ∗


C = r1/2(f ◦φC)(y) where r is the radius

of the cap C. Remark 2.10. This deﬁnition of pullbacks makes sense if f is supported in the cap of radius 1 concentric with C.

- Deﬁnition 2.11 (Upper normalized w.r.t. caps and balls). Let Θ : [1, ∞) → (0, ∞) satisfy Θ(R) → 0 as R → ∞. A function f ∈ L2(S1) is said to be upper normalized with respect to a cap C = C(z, r) ⊂ S1 of radius r and center z if the following hold


- (17) f 2 ≤ C < ∞,

|f|>Rr−1/2

- (18) |f|2dσ(x) ≤ Θ(R), ∀R ≥ 1,

|x−z|≥Rr

- (19) |f|2dσ(x) ≤ Θ(R), ∀R ≥ 1.

An even function f is said to be upper even-normalized with respect to Θ, and C if f can be decomposed into f = f+ + f− where f−(x) = f+(−x), and f+ is upper normalized with respect to Θ and C. A function f ∈ L2(R) is said to be upper normalized with respect to the unit ball in R if

![image 10](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile10.png>)

- (20) f 2 ≤ C < ∞,

|f|>R

- (21) |f|2dx ≤ Θ(R), ∀R ≥ 1,

|x|≥R

- (22) |f|2dx ≤ Θ(R), ∀R ≥ 1.


- Deﬁnition 2.12 (Near-extremal). A nonzero function f ∈ L2(S1) is said to be δ-nearly extremal for the inequality (1) if


- (23) fσ ∗ fσ ∗ fσ 2 ≥ (1 − δ)3S3 f 32. The following proposition provides a preliminary decomposition for nearly extremals.


- Proposition 2.13. There exists a function Θ : [1, ∞) → (0, ∞) satisfying Θ(R) → 0 as R → ∞ with the following property. For any ε > 0, there exists δ > 0 such that any

nonnegative even functions f ∈ L2(S1) satisfying f 2 = 1 which is a δ-nearly extremal may be decomposed as f = F + G, where F and G are even and nonnegative with disjoint supports, G 2 ≤ ε and there exists a cap C such that F is upper even-normalized with respect to C.

It follows from two crucial facts: the reﬁnement of Tomas-Stein’s inequality for S1 in Proposition 2.7, and a geometric fact that “distant caps interact weakly” we will establish in Section 4. The latter asserts, roughly speaking, that χCσ ∗ χCσ ∗ χC′σ 2 ≪ |C||C′|1/2 unless the caps C and C′ have comparable radii and nearby centers.

Step 5, Ruling out small caps and existence of extremals. In [10], the authors observe that the linear Airy evolution at high frequency is well approximated by a linear Schro¨digner evolution, which is used in [24] to establish the linear proﬁle decomposition for the Airy equation. In this paper, we have observed that a similar phenomena occurs for fσ when f is supported on a very small cap. More precisely, given any extremizing sequence {fν} which is upper even normalized with respect to caps Cν with radii rν → 0, fνσ can be written as a superposition of “orthogonal” linear Schro¨dinger waves, plus a small error term. In this case, there follows that

R ≤ (5/2)1/6RP.

But it is a contradiction to the strict inequality that R > (5/2)1/6RP. Thus infν rν > 0. Then for “large caps”, one can indeed prove fν is precompact, which leads to the existence of extremals for (1).

- Proposition 2.14. Let {fν} ⊂ L2(S1) be an extremizing sequence for the inequality (1) satisfying fν 2 = 1 and |f(−x)| = |f(x)| for a.e. x ∈ S1. Suppose that each |fν| is upper even-normalized with respect to a cap Cν ∪(−Cν) where Cν = C(zν, rν), with constants uniform in ν. Then


rν > 0. In this case, an extremal for (1) is obtained.

inf

ν

The strict comparison on the optimal constants for Tomas-Stein’s inequalities for the sphere and the paraboloid is essential to obtain existence of extremals to Tomas-Stein’s inequality for the sphere. In high dimensions, it is the lack of the strict comparison on the optimal constants and the algebraic property of the even integer 6 that prevent us from obtaining the existence of extremals.

Step 1 is established in the Appendix. We present Step 2 through Step 5 in what follows.

3. Step 2. Antipodal symmetrization

In this section, we will prove the functional fσ ∗ fσ ∗ fσ 22/ f 62 is non-decreasing under the antipodal symmetrization deﬁned in Deﬁnition 2.2.

Proof of Proposition 2.4. For f ≥ 0,

- (24) fσ ∗ fσ ∗ fσ 22 = f(a1) × · · · × f(a6)dλ(a1, · · · , a6) for a certain non-negative measure λ which is supported by the set
- (25) {(a1, · · · , a6) ∈ (R2)6 : a1 + a2 + a3 = a4 + a5 + a6}, and which is invariant under the following transformations

(a1, a2, a3, a4, a5, a6)  → (a4, a5, a6, a1, a2, a3), (a1, a2, a3, a4, a5, a6)  → aτ(1), aτ(2), aτ(3), a4, a5, a6 , (a1, a2, a3, a4, a5, a6)  → (a1, a2, −a4, −a3, a5, a6), (a1, a2, a3, a4, a5, a6)  → (a1, −a4, −a5, −a2, −a3, a6),

- (26)

where τ ∈ S3, the permutation group of order 3. We denote by G the ﬁnite group of symmetries of (R2)6 generated by these symmetries. The cardinality of G is 2 × 6! since there holds a short exact sequence

- (27) 1  → {±1}  → G  → S6  → 1.

Note that in order for a sequence (a1, a2, a3, a4, a5, a6) of ﬁxed order to satisfy the requirement (25), the only way is to add “−” sign. Hence from basic algebra, there holds that |G/{±1}| = |S6| = 6!; thus |G| = 2 × 6! follows.

By the orbit of a point we mean its image under G; by a generic point we mean one whose orbit has cardinality 2 × 6!. In (24), it suﬃces to integrate only over all generic 6-tuples (a1, · · · , a6) satisfying (25), since they form a set of full λ-measure.

To the orbit O we associate the functions F(O) =

(a1,··· ,a6)∈O

f(a1) × · · · × f(a6),

F⋆(O) =

(a1,··· ,a6)∈O

f⋆(a1) × · · · × f⋆(a6)

- (28)

Let Ω denote the set of all orbits of generic points. We can write

f ∗ f ∗ f 22 =

Ω

F(O)dµ(O),

f⋆ ∗ f⋆ ∗ f⋆ 22 =

Ω

F⋆(O)dµ(O)

- (29)


- for a certain nonnegative measure µ. Therefor it suﬃces to prove that for any generic orbit O,
- (30)

(a1,··· ,a6)∈O

f(a1) × · · · × f(a6) ≤

(a1,···,a6)∈O

f⋆(a1) × · · · × f⋆(a6).

Fix any generic orbit 6-tuple (a1, · · · , a6) satisfying (25), we prove (30) for its orbit. By homogeneity, we may assume that f(a1)2 + f(−a1)2 = 1 and that the same holds simultaneously for ai for i = 2, · · · , 6. Thus we may write

f(a1) = cos(θ1), f(a2) = cos(θ2), · · · , f(a6) = cos(θ6), f(−a1) = sin(θ1), f(−a2) = sin(θ2), · · · , f(−a6) = sin(θ6)

- (31)

for θi ∈ [0, π2] for i = 1, . . ., 6. Thus by deﬁnition

![image 11](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile11.png>)

- (32) f⋆ = 2−1/2.

Before writing out (a

1,···,a6)∈O f(a1) × · · · × f(a6) for a generic orbit of (a′

1, · · · , a′

6), we note that there will be 2 × 6! summands, which can be organized into 20 terms. Here 20 comes out because 20 = 2×23!××6!3!. Below we will write out a long formula,

![image 12](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile12.png>)

1 2 × 3! × 3!

![image 13](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile13.png>)

(a1,··· ,a6)∈O

f(a1) × · · · × f(a6)

= cos(θ1) cos(θ2) cos(θ3) cos(θ4) cos(θ5) cos(θ6)

+ sin(θ1) sin(θ2) sin(θ3) sin(θ4) sin(θ5) sin(θ6)

+

 



cos(θ1) cos(θ2) sin(θ3) cos(θ1) sin(θ2) cos(θ3) sin(θ1) cos(θ2) cos(θ3)

×

 



sin(θ4) cos(θ5) cos(θ6) cos(θ4) sin(θ5) cos(θ6) cos(θ4) cos(θ5) sin(θ6)

+

 



cos(θ1) sin(θ2) sin(θ3) sin(θ1) cos(θ2) sin(θ3) sin(θ1) sin(θ2) cos(θ3)

×

 



sin(θ4) sin(θ5) cos(θ6) sin(θ4) cos(θ5) sin(θ6) cos(θ4) sin(θ5) sin(θ6)

=: Γ(θ1, · · · , θ6).

- (33)

We will organize terms according to cos(θ5) cos(θ6), sin(θ5) sin(θ6), sin(θ5) cos(θ6) and cos(θ5) sin(θ6) and rewrite Γ as

Γ = cos(θ5) cos(θ6)A + sin(θ5) sin(θ6)B + sin(θ5) cos(θ6) + cos(θ5) sin(θ6) C

= cos(θ5) cos(θ6)A + sin(θ5) sin(θ6)B + sin(θ5 + θ6)C

- (34)

where A and B contain 4 terms, respectively, and C contains 6 terms. For the sake of simplicity, we will not explicitly write out A, B and C; we will do so whenever it is necessary.

We aim to show that

- (35) max


5 2

.

Γ = Γ(π/4, · · · , π/4) =

![image 14](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile14.png>)

(θ1,··· ,θ6)∈[0,π/2]6

This maximal value of Γ matches values taken by

1 2 × 3! × 3!

20 8

5 2

f⋆(a1) × · · · × f⋆(a6) =

=

.

![image 15](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile15.png>)

![image 16](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile16.png>)

![image 17](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile17.png>)

(a1,···,a6)

Suppose that (α1, · · · , α6) is a critical point of Γ, then at this point, there holds that

- (36)

dΓ dθ5

![image 18](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile18.png>)

=

dΓ dθ6

![image 19](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile19.png>)

= 0, which implies that, at this critical point,

- (37) 0 =

dΓ dθ5 −

![image 20](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile20.png>)

dΓ dθ6

![image 21](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile21.png>)

. We expand the right hand side of (37) out to see

- (38) sin(α5 − α6)(A + B) = 0.

We will show that A+B|(α1,...,α6) > 0; otherwise, since every term in A+B is nonnegative, that A + B = 0 will imply that every term is actually zero. This further implies that

- (39) Γ(α1, · · · , α6) <

5 2

![image 22](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile22.png>)

,

which contradicts to the deﬁnition that (α1, · · · , α6) is a critical point. Indeed, We writes out

- A = cos(θ1) cos(θ2) cos(θ3 − θ4) + sin(θ1 + θ2) cos(θ3) sin(θ4),
- B = sin(θ1) sin(θ2) cos(θ3 − θ4) + sin(θ1 + θ2) sin(θ3) cos(θ4).


- (40) Hence
- (41) 0 = A + B = cos(θ1 − θ2) cos(θ3 − θ4) + sin(θ1 + θ2) sin(θ3 + θ4). This implies that
- (42)

cos(θ1 − θ2) cos(θ3 − θ4) = 0, sin(θ1 + θ2) sin(θ3 + θ4) = 0.

So we have the following four combinations,

- (43) θ1 − θ2 = π/2, θ3 + θ4 = 0, or π.


θ1 − θ2 = −π/2, θ3 + θ4 = 0, or π.

θ1 + θ2 = 0, or π, θ3 − θ4 = −π/2.

θ1 + θ2 = 0, or π, θ3 − θ4 = π/2.

In all cases, we can show that

5 2

Γ <

. For instance, assume the ﬁrst instance with

![image 23](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile23.png>)

θ1 − θ2 = π/2, θ3 + θ4 = 0. Then by the fact that all θi ∈ [0, π/2], we have

θ1 = π/2, θ2 = θ3 = θ4 = 0.

Then Γ is simpliﬁed to

Γ = sin(θ5 + θ6) ≤ 1 < 5/2. Thus (38) forces that

- (44) θ5 = θ6. By symmetry it immediately follows that

θ4 = θ5 = θ6 := β, θ1 = θ2 = θ3 := α

- (45)

Observing that by symmetry we may exchange, say, f(a3) = cos(θ3) = cos(α) and f(−a4) = sin(θ4) = sin(β) = cos(π2 − β) in Γ, we conclude that

![image 24](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile24.png>)

- (46) α + β = π/2. Combining (45) and (46), we see that
- (47) Γ(α1, · · · , α6) = 20 cos3(α) cos3(β) =

20 8

![image 25](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile25.png>)

2 sin(α) cos(α) 3 =

5 2

![image 26](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile26.png>)

sin3(2α) ≤

5 2

![image 27](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile27.png>)

with “=” if and only if α = π4. Hence the only choice for critical points is

![image 28](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile28.png>)

- (48) α = β =

π 4

![image 29](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile29.png>)

.

To conclude, we have established the claim (35). Hence (30) follows. Therefore the proof of Theorem (2.4) is complete.

4. Step 3. A refined estimate and a geometric fact

In this section we ﬁrst establish the reﬁnement of Tomas-Stein inequality for S1 in Lemma

- 2.6, which easily implies Proposition 2.7, see e.g. [7, 24]. In the end of this section, we establish a geometric fact that “distant caps interact weakly”. We aim to prove the following Proposition 4.1. For f ∈ L2(S1). There exists α ∈ (0, 1) such that


fσ 6 ≤ sup

C

1 |C|1/2 C

![image 30](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile30.png>)

|f|dσ

α

f 1L−2(αS1), where C denotes a cap on S1.

We recall two lemmas: The ﬁrst is on the bilinear restriction estimates for functions whose supports are transverse.

- Lemma 4.2. Let f, g ∈ L2(S1) and assume that f and g are supported on the caps C1 and C2, which are separated by 2j for j ≤ 0. Then


- (49) fσ gσ 2 ≤ C2−j/2 f 2 g 2.


The proof of this lemma follows from Cauchy-Schwarz’s inequality and the geometric estimate σ ∗ σ′

∞ ≤ C2−j where σ and σ′ denote the surface measures supported on the two caps on the sphere S1 which are separated by an angle 2j, j ≤ 0. The second is on the “almost orthogonality” for functions which have disjoint supports in the Fourier space, see for instance [28, Lemma 6.1].

- Lemma 4.3. Let {Rk} be a collection of rectangles and c > 0 such that the dilates (1+c)Rk


are almost disjoint (i.e., k χ(1+c)R

k ≤ C < ∞), and suppose that {fk} is a collection of functions supported by {Rk}. Then for all 1 ≤ p ≤ ∞,

- (50)

k

fk p

k

fk p

0

p

1/p0

where p0 = min{p, p/(p − 1)}.

Proof of Proposition 4.1. For j ≤ 0, we partition S1 into a union of caps Ckj of length ∼ 2j. For a given cap Ckj, we partition it into two equal caps Cmj−1 and Cnj−1 of length 2j−1; we say Ckj is the “parent” of Cmj−1 and Cnj−1. We deﬁne a relation Ckj1 ∼ Ckj2 if they are not adjoint but their parents are adjoint. Then

- (51) fσ fσ =

j k l: Clj∼Ckj

fkσ flσ,

where fk := fχCj

k

and fl := fχCj

l

. We write j (k,l) := j k l:Cj

l∼Ckj. By Lemma 4.2,

fkσ flσ 2 ≤ C2−j/2 fk 2 fl 2. On the other hand,

fkσ flσ ∞ ≤ C fk 1 fl 1. Then by interpolation,

- (52) fkσ flσ 3 ≤ C2−

j

![image 31](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile31.png>)

3 fk 3/2 fl 3/2. From (51) and (52), and Lemma 4.3,

fσ 26 = fσ fσ 3 =

j (k,l)

fkσ flσ 3 

 j (k,l)

fkσ flσ 33/2

 

2/3



 j (k,l)

2−j/2 fk 33//22 fl 33//22

 

2/3

j k

2−j/2 fk 33/2

2/3

;

- (53)


to pass to the last inequality, we have used that for given k, there are at most O(1)’s Clj ∼ Ckj. By interpolation, for any 3/2 < p < 2,

2−j/2 fk 33/2 ≤ 2−j/2 fk 3(11 −θ) fk 3pθ ≤ 2−j/2 fk 1 3(1−θ) 2−j(−1+3θ/2) fk 3pθ,

where θ = p/3(p − 1). So if normalizing f 2 = 1 and taking α = 1 − θ, it suﬃces to show that

2−j(3θ/2−1) fk 3pθ 1.

j k

We decompose fk = fkχ|f|≤2−j/2 + fkχ|f|>2−j/2 =: fk− + fk+. For fk−,

2−j(3θ/2−1) fk− 3pθ 1.

j k

Indeed, we apply H¨older’s inequality with (3θ/p, 3θ/(3θ − p)),

3θ−p p

3θ−p

fk− 3pθ ≤

|f|3θ(2j)

≤ |f|3θ(2j)

p .

![image 32](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile32.png>)

![image 33](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile33.png>)

k Ck

k

Since 3θ/2 − 1 − 3θp−p < 0 as p < 2,

![image 34](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile34.png>)

3θ−p

2−j(3θ/2−1−

p )

2−j(3θ/2−1) fk− 3pθ ≤ |f|3θ

![image 35](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile35.png>)

j k

j≤0:|f|<2−j/2

1 p−21)

2j3θ(

= C |f|3θ ×

![image 36](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile36.png>)

![image 37](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile37.png>)

- (54)

For fk+, we estimate it as follows: as p < 2 and 3θ = p′, then 3θ/p = p′/p > 1; then

j,k

2−j(

3θ

![image 38](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile38.png>)

2 −1) fk+ 3pθ =

j,k

2−j(

p′

![image 39](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile39.png>)

2 −1) fk+ p

′

p

≤

j,k

2−jp(

- 1

![image 40](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile40.png>)

- 2−p1′) fk+ pp


![image 41](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile41.png>)

p′/p

=

j,k

2−j

2−p

![image 42](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile42.png>)

2 fk+ pp

p′/p

=

j

2−j

2−p 2

![image 43](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile43.png>)

|f|>2−j/2

|f|p

p′/p

=

  |f|p

j≤0: |f|>2−j/2

2−

j 2(2−p)

![image 44](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile44.png>)

 

p′/p

≤ C |f|2

p′/p

≤ C.

- (55)


j≤0:2j<|f|−2

6θ p

6θ p

≤ C |f|3θ × |f|3θ−

≤ C |f|6θ−

![image 45](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile45.png>)

![image 46](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile46.png>)

= C |f|2 < ∞.

Hence Proposition 4.1 follows.

Then Proposition 2.7 follows by a similar argument as in [12, 24]. Now we turn to show that “distant caps interact weakly”. We start with deﬁning the distance between caps. The distance ρ between two given caps C(z, r) and C′(z′, r′) is

r′ r

+ |z − z′| r

r r′ +

.

![image 47](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile47.png>)

![image 48](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile48.png>)

![image 49](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile49.png>)

For any metric space (X, ρ) and any equivalence relation ≡ on X, recall from the basic algebra the function ρ([x], [y]) = infx′∈[x],y′∈[y] ρ(x′, y′) is a metric on the set of equivalence classes X/ ≡. Let M be the set of all caps C ⊂ S1 modulo the equivalence relation C ≡ −C, where −C = {−x, x ∈ C}. Then a metric on M can be deﬁned in the following way.

Deﬁnition 4.4. For any two caps C, C′ ∈ S1,

- (56) ̺([C], [C′]) = min ρ(C, C′), ρ(−C, C′) , where [C] denotes the equivalence class [C] = {C, −C} ∈ M.

We will write ̺(C, C′) = ̺([C], [C′]).

- Lemma 4.5. For any ε > 0 there exists ρ < ∞ such that


- (57) χCσ ∗ χCσ ∗ χC′σ L2 ≤ ε|C||C′|1/2 whenever
- (58) ̺(C, C′) > ρ.

Proof. Set

f = |C|−1/2χC ≤ Cr−1/2χC, f˜= |C|˜ −1/2χC˜ ≤ Cr˜−1/2χC˜. Assume r˜ ≤ r and r˜ ≪ 1 and consider the case where no points are nearly antipodals. The case where the points are antipodals can be reduced to the previous case by using the identity

- (59) f1σ ∗ f2σ ∗ f3σ, f4σ ∗ f5σ ∗ f6σ = f1σ ∗ f2σ ∗ f˜4σ, f˜3σ ∗ f5σ ∗ f6σ

for any non-negative functions fj ∈ L2(S1), j = 1, · · · , 6. Let ε be given. It suﬃces to show, if ̺(C, C′) ≥ ρ,

- (60) χCσ ∗ χC′σ L3/2 ≤ ε|C|1/2|C′|1/2.

- Case I. Assume r ∼ r˜ and |x − x˜| ≥ 10r. Observe that


- (61) fσ ∗ fσ˜ ∞ ≤ (rr˜)−1/2

C |x − x˜|

![image 50](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile50.png>)

,

and fσ ∗ fσ˜ is supported in a rectangle with width r and height r|x − x˜|. Then

- (62) fσ ∗ fσ˜ L3/2(R2) ≤ (rr˜)−1/2


1/3

r |x − x˜|

C |x − x˜|

(r2|x − x˜|)2/3 = C

≪ 1.

![image 51](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile51.png>)

![image 52](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile52.png>)

- Case II. Assume r˜ ≪ r and |x − x˜| ≥ 10r. Still there holds

(63) fσ ∗ fσ˜ ∞ ≤ (rr˜)−1/2

C |x − x˜|

![image 53](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile53.png>)

, but fσ ∗ fσ˜ is supported in a tube with base length r and width r˜|x − x˜|. Then

(64) fσ ∗ fσ˜ L3/2(R2) ≤ (rr˜)−1/2

C |x − x˜|

![image 54](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile54.png>)

(rr˜|x − x˜|)2/3 ≤ C

(rr˜)1/6 |x − x˜|1/3

![image 55](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile55.png>)

≤ C(˜r/r)1/6 ≪ 1.

- Case III. Assume that r˜ ≪ r and |x − x˜| ≤ 10r. The analysis in Case II almost applies if |x − x˜| ≥ cr for some universal constant c > 0, while it breaks down when their centers are very close. To cope with this diﬃculty, we employ the trick in [12]: we replace f by its restriction F to the complement of the cap C˜⋆ centered at x˜ of radius 10r3/4r˜1/4. Then


- (65) f − F 2 ≤ Cr−1/2(r3/4r˜1/4)1/2 ≤ C(˜r/r)1/8 ≪ 1. Then we observe that
- (66) Fσ ∗ fσ˜ ∞ ≤ (rr˜)−1/2

C |x − x˜|

![image 56](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile56.png>)

,

but Fσ ∗ fσ˜ is supported in a tube with base length r and width r˜|x − x˜|, whose area is less than Crr˜|x − x˜|. Then

Fσ ∗ fσ˜ L3/2(R2) ≤ (rr˜)−1/2

C |x − x˜|

![image 57](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile57.png>)

(rr˜|x − x˜|)2/3

≤ C

(rr˜)1/6 |x − x˜|1/3

![image 58](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile58.png>)

≤ C

(rr˜)1/6 r3/4r˜1/4 1/3

![image 59](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile59.png>)

≤ C

r ˜ r

![image 60](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile60.png>)

1/12 ≪ 1.

- (67)

5. Step 4. On near-extremals: Proposition 2.13.

In this section, we aim to prove Proposition 2.13, which roughly speaking states that any nearly extremal to the inequality satisﬁes some appropriately scaled upper bounds relative to some cap up to a small error in L2. As remarked in [12], its proof is largely a formal argument relying on two inputs, Lemma 2.7 and Lemma 4.5 which are already established in the previous step. We begin with

- Lemma 5.1. Let f = g + h ∈ L2(S1). Suppose that g, h = 0 and g = 0, and that f is a δ-nearly extremal for some δ ∈ (0, 41]. Then


![image 61](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile61.png>)

- (68)


hσ ∗ hσ ∗ hσ 12/3 h 2

h 2 f 2 ≤ C max

, δ1/2 ,

![image 62](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile62.png>)

![image 63](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile63.png>)

where 0 < C < ∞ is a constant independent of g and h.

The proof of this lemma is similar to [12, Lemma 7.1] and will be omitted.

- 5.2. A decomposition algorithm. Let f ∈ L2(S1) be a nonnegative function with positive norm. The same algorithm in [12] applies:


f =

with the following properties.

fk + Gν+1, ν = 0, 1, . . .

0≤k≤ν

• G0 := f and ε0 = 1/2. The inputs for Step ν are a nonnegative function Gν ∈ L2(S1) and a positive number εν. The outputs are functions fν and Gν+1 and nonnegative numbers ε∗

ν and εν+1.

- – If Gνσ ∗ Gνσ ∗ Gνσ 2 = 0, then Gν = 0 almost everywhere. The algorithm

then terminates and we deﬁne ε∗ν = 0, fν = 0, and Gν = 0, fµ = 0 and εµ = 0 for µ > ν.

- – If 0 < Gνσ ∗Gνσ ∗Gνσ 2 < ε3νS3 f 32, we replace εν by εν/2, and repeat until


the ﬁrst time that Gνσ ∗ Gνσ ∗ Gνσ 2 ≥ ε3νS3 f 32. Deﬁne ε∗

ν to be this value of εν. Then

- (69) (ε∗ν)3S3 f 32 ≤ Gνσ ∗ Gνσ ∗ Gνσ 2 ≤ 8(ε∗ν)3S3 f 32.


Then an application of Lemma 2.7 yields a decomposition for Gν: namely we obtain a cap Cν and Gν = fν + Gν+1, where fν and Gν+1 satisfy the properties listed in that Lemma. We remark that the constants Cν ≤ C(ε∗

ν)−O(1) and ην ≥ C(ε∗

ν)O(1). Deﬁne εν+1 = ε∗

ν and move on to the next step ν + 1.

- • If f is even, then fν may likewise be chosen to be even.
- • If the algorithm terminates at some ﬁnite step ν, then we have a ﬁnite decomposition

f = 0≤k≤ν fk and ε∗

k = 0 for k ≥ ν + 1.

- • If the algorithm never terminates, then νN∗ → 0 and 0≤ν≤N fν → f in L2(S1) as N → ∞.


The algorithm yields some useful information when the decomposition algorithm is applied to nearly extremals. This is a consequence of Lemma 2.7 and Lemma 5.1.

- Lemma 5.3. There exists a continuous function θ : (0, 1] → (0, ∞) such that for any ε > 0,


there exists a δ > 0 such that for any nonnegative δ-nearly extremal f with f L2(S1) = 1. Then

fν 2 ≥ θ( Gν 2) for any index ν such that Gν 2 ≥ ε.

Proof. Let C be the exact constant appearing in Lemma 5.1. Given ε > 0. We choose δ > 0 such that Cδ1/2 < ε/2. Then the second alternative in Lemma 5.1 yields that

C Gνσ ∗ Gνσ ∗ Gνσ 12/3 Gν 2

Gν 2 f 2 ≤

, that is to say,

![image 64](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile64.png>)

![image 65](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile65.png>)

Gνσ ∗ Gνσ ∗ Gνσ 2 ≥ C−1 Gν 32 Gν 32.

Then an application of Lemma 2.7 yields that, there exists a function θ : (0, 1] → (0, ∞) such that

Gν 2 =: θ( Gν 2) where η is as in Lemma 2.7 and θ(x) can be regarded as O(xO(1)).

fν 2 ≥ η G

ν 2

Moreover, if f is nearly extremal, the norms of fν and Gν enjoy upper bounds independent of f for all except for large ν.

- Lemma 5.4. There exists a sequence of positive constants γν → 0 and a function N :


(0, 12] → Z+ satisfying N(δ) → ∞ as δ → 0 such that for any nonnegative f ∈ L2(S1), if f is δ-nearly extremal then the quantities ε∗ν obtained when the decomposition algorithm is applied to f satisfy

![image 66](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile66.png>)

- (70) Gν 2 ≤ γν f 2 for all ν ≤ N(δ),
- (71) ε∗ν ≤ γν for all ν ≤ N(δ),
- (72) fν 2 ≤ γν f 2 for all ν ≤ N(δ).

Proof. The proof will be similar to that in [12, Lemma 8.3]. We normalize f 2 = 1. Since fν 2 ≤ Gν 2, and (69) yields that

(ε∗ν)3S3 ≤ Gνσ ∗ Gνσ ∗ Gνσ 2 ≤ S3 Gν 32, we see that (70) will imply both (71) and (72). Hence we focus on proving (70). Let η be the function appearing in Lemma 2.7 and we know that η(δ) = O(δO(1)).

We ﬁrst choose γν such that it tends to zero so slowly that

- (73) νγν2η2(c0γν3) > 2 for all ν,


where c0 will be clear below; it is possible since η(δ) is in form of O(δO(1)). Then given δ > 0, we choose N(δ) to be the least ν such that

γν ≤ Cδ1/2, where C is the exact constant appearing in Lemma 5.1; we see that N(δ) → ∞ as δ → 0 and that γν > Cδ1/2 for all ν ≤ N(δ). Obviously the choices of γν and N are independent of f.

Now let f and δ > 0 be given. If there were ν such that ν ≤ N(δ) and Gν 2 ≥ γν, then

Gν 2 ≥ γν > Cδ1/2. Then Lemma 5.1 yields that

C Gνσ ∗ Gνσ ∗ Gνσ 2 Gν 2

Gν 2 ≤

. In other words,

![image 67](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile67.png>)

Gνσ ∗ Gνσ ∗ Gνσ 2 ≥ c0 Gν 32 Gν 32 ≥ c0γν3 Gν 32. where c0 = C−1. Then Lemma 2.7 yields that

fν 22 ≥ η2(c0γν3) Gν 22 ≥ η2(c0γν3)γν2.

Since Gµ 2 ≥ Gν 2 for µ ≤ ν, there also holds that Gµ 2 > Cδ1/2 for µ ≤ ν. So one may repeat the procedure above and ﬁnd that

fµ 22 ≥ η2(c0γν3)γν2 for µ ≤ ν. On the other hand, we have 0≤µ≤ν fµ 22 ≤ f 22 = 1, which gives

η2(c0γν3)γν2 ≤ 1, ⇒ νγν2η2(c0γν3) ≤ 1.

µ≤ν

This is a contradiction to the choice of γν in (73). So we ﬁnish the proof of this lemma.

- 5.5. A geometric property of the decomposition. In the previous subsection, based


on the single analytic fact Lemma 2.7, we have established that the L2-norms of fν and Gν obtained when the decomposition algorithm is applied to nearly extremals f satisfy some uniform upper bounds as in Lemma 5.3 and Lemma 5.4. On the other hand, in Lemma 4.5, we have proved that “distant caps interact weakly”; this will provide us some additional information on near extremals. We ﬁrst recall a lemma in [12, Lemma 9.1], which follows easily from the pigeonhole principle.

- Lemma 5.6. In any metric space, for any N and r, any ﬁnite set S of cardinality N and diameter equal to r may be partitioned into two disjoint non-empty subsets S = S1∪S2 such that the distance of S1 and S2 is no less than r/2N. Moreover, given two points s1, s2 ∈ S satisfying distance(s1, s2) = r, this partition may be constructed such that s1 ∈ S1 and s2 ∈ S2.

As a consequence, we have

- Lemma 5.7. For any ε > 0, there exists δ > 0 and 0 < λ < ∞ such that for any nonnegative δ-nearly extremal f, the summands fν obtained from the decomposition algorithm and the associated caps Cν satisfy


- (74) ̺(Cj, Ck) ≤ λ, whenever fj 2 ≥ ε f 2 and fk 2 ≥ ε f 2.


Proof. We follow the proof from [12]. We normalize f 2 = 1 and let ε be given; also suppose that fj

0 2 ≥ ε. Let N be the smallest integer such that GN+1 2 < ε3. This choice of N may depend on f but it will not aﬀect our ﬁnal choice of λ. Since

0 2, fk

fν 2 ≤ Gν 2 and Gν 2 is a non-increasing function of ν, we see that j0, k0 ≤ N. Moreover Lemma 5.4 yields that there exists a Mε which depends only on ε such that N ≤ Mε. If we choose δ to be suﬃciently small but depending on ε, we see that Proposition

- 2.7 yields that fν ≤ θ(ε)|Cν|−1/2χC


ν∪−Cν, where θ is a continuous, strictly positive function on (0, 1]. For those ν ≤ N, we have Gν 2 ≥ ε3.

Now let 0 < λ < ∞ to be a large quantity to be speciﬁed. It suﬃces to show that if δ(ε) is suﬃciently small, an assumption that ̺(Cj, Ck) > λ would lead to a contradiction that f is a δ-nearly extremal.

We apply the previous Lemma 5.6 to see that F = F1 + F2 :=

fν,

fν +

ν∈S2

ν∈S1

where [0, N] = S1 ∪ S2, j0 ∈ S1 and k0 ∈ S2; also we have ̺(Cj, Ck) ≥ 2λN ≥ 2Mλ

for all

![image 68](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile68.png>)

![image 69](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile69.png>)

ε

- j ∈ S1, k ∈ S2. For i, j ∈ {1, 2} and i = j,


λ 2Mε

)θ3(ε),

fjσ ∗ fjσ ∗ fkσ 2 ≤ Mε3γ(

Fiσ ∗ Fiσ ∗ Fjσ 2 ≤

![image 70](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile70.png>)

j∈S1,k∈S2

where γ(t) → 0 as t → ∞ as in Lemma 4.5. Therefore, Fσ ∗ Fσ ∗ Fσ 22 ≤ F1σ ∗ F1σ ∗ F1σ 22 + F2σ ∗ F2σ ∗ F2σ 22 +

Fiσ ∗ Fiσ ∗ Fjσ 22 f 32

i =j, i,j∈{1,2}

λ 2Mε

≤ S6 F1 62 + F2 62 + CMε3γ(

)θ3(ε)

- (75)

where we have used F1 2 ≥ ε and F2 2 ≥ ε in passing to the last inequality. On the other hand,

(1 − δ)6S6 ≤ fσ ∗ fσ ∗ fσ 22 ≤ Fσ ∗ Fσ ∗ Fσ 22 + C f 42 f − F 22 ≤ Fσ ∗ Fσ ∗ Fσ 22 + Cε6.

- (76)

So from (75) and (76), we see that

- (77) (1 − δ)6S6 ≤ Cε6 + S6(1 − ε4) + CMε3γ(


![image 71](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile71.png>)

λ 2Mε

)θ3(ε)

≤ S6 F1 22 + F2 22 max{ F1 42, F2 42} + CMε3γ(

![image 72](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile72.png>)

λ 2Mε

≤ S6(1 − ε4) + CMε3γ(

)θ3(ε),

![image 73](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile73.png>)

λ 2Mε

)θ3(ε).

![image 74](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile74.png>)

Recall that γ(t) → 0 as t → ∞. So given ε > 0 which is small, if we chose a suﬃciently small δ = δ(ε), then (77) will result in a contradiction if λ is allowed to be suﬃciently large. Hence the conclusion of the lemma follows.

- 5.8. Upper bounds for extremizing sequences. In this subsection, we prove Proposition 2.13.


- Lemma 5.9. There exists a function Θ : [1, ∞) → (0, ∞) satisfying limR→∞ Θ(R) = 0 such that the following holds: given any ε > 0 and R¯ > 0, there exists δ > 0 such that for any nonnegative δ-nearly extremal f with f 2 = 1, we have a decomposition


f = F + G

where F and G are even and nonnegative with disjoint supports. Moreover this decomposition satisﬁes G 2 ≤ ε and there exists a cap C = C(z, r) such that for any R ∈ [1, R¯], we

have

- (78) F2(x)dσ(x) ≤ Θ(R),

{F(x)≥Rr−1/2}

- (79) F2(x)dσ(x) ≤ Θ(R).

Let us postpone the proof of this lemma; now we prove Proposition 2.13 by using it.

Proof of Proposition 2.13 from Lemma 5.9. Let ε and f be given. We assume that the Θ given by Lemma 5.9 is a continuous, strictly decreasing function. Deﬁne R¯ = R¯(ε) by the equation Θ(R¯) = (ε/2)2. Let C = C(z, r) and δ = δ(ε, R¯(ε)) along with F and G satisfy the conclusions in Lemma 5.9. We re-deﬁne

- (80) f = ((1 − χ)F) + (χF + G) =: F˜ + G,˜ where χ(x) = 1 if min{|x − z|, |x + z|} ≥ Rr¯ or F(x) ≥ Rr¯ −1/2. Then it easily follows that
- (81) G ˜ 2 ≤ G 2 + χF 2 ≤ ε + 2 × ε/2 = 2ε. On the other hand, we also have

min{|x+z|,|x−z|}≥Rr

F˜2(x)dσ(x) ≤ Θ(R),

{F˜(x)≥Rr−1/2}

F˜2(x)dσ(x) ≤ Θ(R).

- (82)

Indeed, when R ≤ R¯, F˜ ≤ F,

min{|x+z|,|x−z|}≥Rr

F˜2(x)dσ(x) ≤

min{|x+z|,|x−z|}≥Rr

F2(x)dσ(x) ≤ Θ(R),

{F˜(x)≥Rr−1/2}

F˜2(x)dσ(x) ≤

{F(x)≥Rr−1/2}

F2(x)dσ(x) ≤ Θ(R);

- (83)

when R ≥ R¯, from the support information of χ,

min{|x+z|,|x−z|}≥Rr

F˜2(x)dσ(x) ≤

min{|x+z|,|x−z|}≥Rr¯

(1 − χ)F2(x)dσ(x) = 0,

{F˜(x)≥Rr−1/2}

F˜2(x)dσ(x) ≤

{F(x)≥Rr¯ −1/2}

(1 − χ)F2(x)dσ(x) = 0.

- (84)


min{|x+z|,|x−z|}≥Rr

Hence the proof of Proposition 2.13 is complete if we assume Lemma 5.9.

We are left with proving Lemma 5.9.

Proof of Lemma 5.9. Let ε > 0 and f ≥ 0 be given with f 2 = 1 and also R ∈ [1, R¯]. Let {fν, Gν} be the pairs obtained from the decomposition algorithm. Choose δ = δ(ε)

suﬃciently small and M = M(ε) suﬃciently large such that GM+1 2 ≤ ε/2, fν, Gν satisfy the conclusions in Lemma 5.4 for all ν ≤ M.

- (85)

Set F = 0≤ν≤M fν. Then f − F 2 = GM+1 2 ≤ ε/2. Let η : [1, ∞) → (0, ∞) be a function to be chosen in the end of the proof satisfying that η(t) → 0 as t → ∞. This function will not depend on R¯.

Let A(η) := inf{ν : fν 2 < η}. Then set N := min{M, A(η)}. Clearly from the upper bound on A(η), N is majorized by a quantity depending only on η by Lemma 5.4. Set

F = FN := 0≤ν≤N fν. Then it follows from Lemma 5.4 that

- (86) F − F 2 ≤ γ(η), where γ(η) → 0 as η → 0. The function η is independent of ǫ and R¯.

Let C0 = C0(z0, r0) be the cap associated to f0 in the decomposition of f, and C0 will be the desired cap in Lemma 5.9. Then we need to ﬁnd a function Θ to guarantee that both (78) and (79) hold; in this process, we need to choose a suitable function η. Suppose that the functions R  → η(R) and R  → Θ(R) are chosen such that

η(R) → 0, as R → ∞, γ(η(R)) ≤ Θ(R), for all R.

- (87)

Then by (86), F − F satisﬁes the desired estimates (78) and (79). Then it suﬃces to show that

- (88) F(x) = 0, whenever min{|x + z0|, |x − z0|} ≥ Rr0,
- (89)  F ∞ ≤ Rr0−1/2.

Before proving (88), we recall several facts. Firstly each summand fk ≤ C(η)|Ck|−1/2χC

k∪−Ck

where C(η) < ∞ depends only on η, and fk is supported by Ck ∪ −Ck. Moreover, for all

- k ≤ N, fk 2 ≥ η by the deﬁnition of N. Then an application of Lemma 5.7 implies that there exists a function η  → λ(η) such that, if δ is suﬃciently small as a function of η, we


have ̺(Ck, C0) ≤ λ(η) for all k ≤ N. This is needed for η = η(R) for all R in the compact set [1, R¯] so that δ can be chosen as a function of R¯ alone. Hence δ may be chosen as a function of R¯ in addition to the previous dependence on ε.

We are ready to prove (88). Given x ∈ S1 with min{|x−z0|, |x+z0|} ≥ Rr0, either fk(x) = 0 or Ck has radius ≥ 41Rr0, or the center zk of Ck satisﬁes that min{|zk+z0|, |zk−z0|} ≥ 41Rr0. In the latter two cases, there always holds that ̺(Ck, C0) ≥ CR. So

![image 75](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile75.png>)

![image 76](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile76.png>)

- (90) R ≤ Cλ(η(R)).

This is a contradiction to the choice of η if η(R) → 0 slowly enough as R → ∞. Then we have F(x) ≡ 0 when min{|x + z|, |x − z|} ≥ Rr0. With the choice of η, Θ can be deﬁned by

- (91) Θ(R) := γ(η(R)). Then (78) holds for all R ∈ [1, R¯].


Next we prove (89). We claim that  F ∞ ≤ Rr0−1/2 if R is taken suﬃciently large as a function of η. Indeed, because the summands fk have pairwise disjoint supports, it suﬃces to control maxk≤N fk ∞. For this, Lemma 2.7 implies that

fk ∞ ≤ C(η)rk−1/2, C(η) = O(η−O(1)).

If η(R) is chosen to go to zero suﬃciently slowly to ensure that C(η(R))λ(η(R)) < R for all k ≤ N, then (79) holds provided that Θ is deﬁned as in (91). Indeed, given any k ≤ N,

fk ∞ ≤ Rr0−1/2 would follow if C(η(R))rk−1/2 ≤ Rr0−1/2; then it reduces to show that

- (92) C(η(R))λ(η(R)) ≤ R


However (92) is guaranteed if we choose η(R) → 0 suﬃciently slow as R → ∞. Finally η must be chosen to tend to zero slowly enough to satisfy the requirements in (90) and (92). With this choice of η, the proof of Lemma 5.9 is complete.

6. Step 5. Ruling out small caps and existence of extremals

This step aims to establish the Proposition 2.14. We split the proof into 3 subsections,

- 6.1, 6.5 and 6.6. In Subsection 6.1, we prove two propositions, one on the decomposition


of fνσ into “proﬁles”, and the other on orthogonality of such proﬁles. Then in Subsection

- 6.5, we rule out the “small caps” case where limν→∞ rν = 0 with the additional information that R > (5/2)1/6RP. Then we are left with “large caps” case, i.e., where infν rν > 0. In Subsection 6.6, we show that an extremal is obtained for (1).


Let {fν} be an even nonnegative extremizing sequence, uniformly upper even normalized with respect to the caps {Cν ∪ (−Cν)}. Without loss of generality, we may assume that Cν is supported on the upper hemisphere of S1, S+1 := {y ∈ S1 : y · (0, 1) > 0}. The sequence {fν} satisﬁes that fν L2(S1) = 1. Suppose that infν rν = 0. Then up to a subsequence, we may assume that limν→∞ rν = 0.

Decompose

21/2fν(x) = fν+(x) + fν+(−x) + fνb(x),

where fν+ is real, fν+ is supported on C(zν, rν1/2), and fνb L2 → 0 as ν → ∞. Set

gν := φ∗ν(fν+) = rν1/2fν+(φC

ν

1

)/(1 − rν2y2)

4,

![image 77](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile77.png>)

where φ∗

ν is the rescaling map associated to Cν ∪ (−Cν). It is not hard to see that gν is upper normalized with respect to the unit ball B ⊂ R, i.e.,

gν ≥ 0, gν 2 → 1, as ν → ∞,

|gν|2dx ≤ Θ(R), ∀R ≥ 1,

- (93)

Since fν is even and fν L2 = 1, we have fν+ L2 → 1 as ν → ∞. Moreover the function Fν := fν+(x) + fν+(−x) satisﬁes

Fνσ ∗ Fνσ ∗ Fνσ 2L2 Fν 6L2

![image 78](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile78.png>)

=

20 8

![image 79](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile79.png>)

fν+σ ∗ fν+σ ∗ fν+σ 2L2 fν+ 6L2

![image 80](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile80.png>)

.

So we have

- (94) limsup

ν→∞

fνσ ∗ fνσ ∗ fνσ 2L2 =

5 2

![image 81](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile81.png>)

limsup

ν→∞

fν+σ ∗ fν+σ ∗ fν+σ 2L2.

We will show that the right hand side of (94) is less than 52P6 by developing a proﬁle decomposition for fν+. For simplicity of notations, in the subsection 6.1 below, we will write fν as fν+.

![image 82](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile82.png>)

- 6.1. Key propositions. Recall that we write fν+ as fν and fν+ is supported on C(zν, rν1/2). By rotation invariance, we may assume that zν = (0, 1) for all ν. The decomposition for fνσ is motivated by the rescaling relation,


fνσ(x, t) =

Cν

ei(x,t)·ξfν(ξ)dσ(ξ)

=

|y|≤1/2

eixy+it

√

![image 83](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile83.png>)

1−y2 fν(y, 1 − y2) 1 − y2

![image 84](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile84.png>)

![image 85](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile85.png>)

![image 86](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile86.png>)

dy

= rν1/2 eir

νxy+it

√

![image 87](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile87.png>)

1−rν2y2 rν1/2fν(rνy, 1 − rν2y2) 1 − rν2y2

![image 88](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile88.png>)

![image 89](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile89.png>)

![image 90](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile90.png>)

dy

= rν1/2 eir

νxy−itr

2 νy2

![image 91](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile91.png>)

2 eir

2 νt

√

![image 92](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile92.png>)

1−r2

νy2−1 r2

![image 93](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile93.png>)

ν

+y

2 2

![image 94](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile94.png>)

1 (1 − rν2y2)

![image 95](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile95.png>)

1 4

![image 96](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile96.png>)

rν1/2fν(rνy, 1 − rν2y2) (1 − rν2y2)

![image 97](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile97.png>)

![image 98](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile98.png>)

1 4

![image 99](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile99.png>)

dy

= rν1/2e

ir2

νt∆

![image 100](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile100.png>)

2 hν(rν2t, y)gν(y) (rνx) ,

- (95)


|x|≥R

|gν|2dx ≤ Θ(R), ∀R ≥ 1, Θ(R) → 0, as R → ∞.

gν≥R

- where
- (96) hν(t, y) := e

it

√

![image 101](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile101.png>)

1−r2

ν|y|2−1 r2

![image 102](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile102.png>)

ν

+|y|

2 2

![image 103](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile103.png>)

.

So a decomposition for fνσ immediately follows once we have a decomposition for {gν}. Set h−1

ν = 1/hν.

- Proposition 6.2. Let {gν} and {hν} be deﬁned as above. Then there exists a sequence (xkν, tkν) ∈ R2 and elν ∈ L2(R) such that

(97) gν(y) =

l

j=1

e

it

j νy2

![image 104](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile104.png>)

2 e−ix

j

νyh−ν 1(tjν, y)φj + elν(y)

with the following properties: The parameters {(xkν, tkν)} satisfy, for k = j,

- (98) |xkν − xjν| + |tkν − tjν| → ∞, as ν → ∞. For each l ≥ 1,
- (99) fν 2L2(S1) =


l

j=1

φj 22 + elν 22 as ν → ∞.

The function elν satisﬁes

(100) limsup

l→∞

limsup

ν→∞

rν1/2e

itr2

ν∆

![image 105](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile105.png>)

2 hν(rν2t, y)

elν (1 − rν2y2)

![image 106](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile106.png>)

1 4

![image 107](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile107.png>)

(rνx)

L6t,x(R2)

= 0.

where

e

it∆

![image 108](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile108.png>)

2 f(x) = eixy−

ity2

![image 109](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile109.png>)

2 f(y)dy.

- Proposition 6.3 (Orthogonality). Let {(xjν, tjν)} be as above and set


- (101) νyh−ν 1(tkν, y)φk,

Gjν := e

it

j νy2

![image 110](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile110.png>)

2 e−ix

j

- (102) νyh−ν 1(tjν, y)φj. Then for k = j,

lim

ν→∞

rν1/2e

itr2

ν∆

![image 111](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile111.png>)

2 hν(rν2t, y)

Gkν (1 − rν2y2)

![image 112](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile112.png>)

1 4

![image 113](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile113.png>)

(rνx) rν1/2e

itr2

ν∆

![image 114](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile114.png>)

2 hν(rν2t, y)

Gjν (1 − rν2y2)

![image 115](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile115.png>)

1 4

![image 116](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile116.png>)

(rνx)

L3t,x(R2)

= 0.

- (103)


itk

νy2

k

2 e−ix

Gkν := e

![image 117](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile117.png>)

We state a useful lemma on a localized linear restriction estimate., which will be used in the proof of Proposition 6.2.

- Lemma 6.4. Let 4 < q < 6 and hν be deﬁned as in (96). Assume that limν→∞ rν = 0.


Then if |(1 − rν2y2)1/4f| ≤ M for some M > 0 and for all |y| ≤ R and all suﬃciently large ν,

f(y) (1 − rν2y2)1/4

it∆

] Lq

≤ CM, uniformly in suﬃciently large ν,

2 [hν(t, y)

e

![image 118](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile118.png>)

![image 119](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile119.png>)

t,x

where the constant may depend on R, but not on ν.

Proof. Choose rν suﬃciently small such that B(0, R) ⊂ {|y| ≤ 21r−1

ν }. We write e

![image 120](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile120.png>)

√

![image 121](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile121.png>)

1−|rνy|2−1 r2 ν

f(y) (1 − rν2y2)1/4

1 (1 − |rνy|2)

](x) = eixy+it

it∆

![image 122](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile122.png>)

f(y)dy

2 [hν(t, y)

![image 123](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile123.png>)

![image 124](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile124.png>)

![image 125](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile125.png>)

1 4

![image 126](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile126.png>)

√

dy 1 − |y|2

![image 127](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile127.png>)

rν y+irt2

x

1−|y|2rν−1f(rν−1y)(1 − |y|2)

= ei

1 4

![image 128](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile128.png>)

![image 129](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile129.png>)

.

![image 130](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile130.png>)

ν

![image 131](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile131.png>)

![image 132](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile132.png>)

Then

√

dy 1 − |y|2 Lq

![image 133](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile133.png>)

x

rν y+irt2

1−|y|2rν−1f(rν−1y)(1 − |y|2)

ei

1 4

![image 134](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile134.png>)

![image 135](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile135.png>)

![image 136](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile136.png>)

ν

![image 137](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile137.png>)

![image 138](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile138.png>)

t,x

√

3 q

= r−1+

![image 139](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile139.png>)

1

1−|y|2f(rν−1y)(1 − |y|2)

eixy+it

![image 140](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile140.png>)

4dσ

![image 141](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile141.png>)

ν

S+1

Lqt,x

3 q

≤ r−1+

ν f(rν−1y)(1 − y2)1/4 Lp(σ,+),

![image 142](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile142.png>)

where p satisﬁes 3q = 1−1p, p < 2, and Lp(σ, +) is understood as integrating over S+1 ; we have also regarded f(y) as a function on the upper hemisphere S+1 := {z ∈ S1 : z · (0, 1) > 0}.

![image 143](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile143.png>)

![image 144](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile144.png>)

Then continuing the above inequality, we have

1/p

dy 1 − y2

3 q

r−1+

1 4

|p

ν |f(rν−1y)(1 − y2)

![image 145](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile145.png>)

![image 146](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile146.png>)

![image 147](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile147.png>)

![image 148](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile148.png>)

dy 1 − rν2y2

3 q +p1

≤ r−1+

1 4

|p

|f(y)(1 − rν2y2)

![image 149](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile149.png>)

![image 150](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile150.png>)

![image 151](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile151.png>)

ν

![image 152](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile152.png>)

![image 153](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile153.png>)

|y|≤R

≤ CMR1/p, for all suﬃciently large ν. This ﬁnishes the proof of Lemma 6.4.

1/p

Now we will ﬁrst prove Proposition of 6.2, and then Proposition 6.3.

- The proof of Proposition 6.2. We split the proof into two steps.


- Step 1. For (xν, tν) ∈ R2, we deﬁne


itνy2

Tν(g)(y) = e−

νyhν(tν, y)g(y); analogously Tνi for (xiν, tiν) for i ≥ 1, and T−1

2 eix

![image 154](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile154.png>)

itνy2

ν (tν, y)g(y). Let P0 denote the sequence {gν}ν≥1. Then we deﬁne the set

2 e−ixνyh−1

ν (g)(y) = e

![image 155](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile155.png>)

W(P0) = {w − lim

Tν(Pν0)(y) in L2(R) : (xν, tν) ∈ R2},

ν→∞

where w−limfν denotes a weak limit of {fν} in L2. Deﬁne the blow-up criterion associated to W(P0):

µ(P0) := sup{ φ L2(R) : φ ∈ W(P0)}. Then for any φ ∈ W(P0),

rν1/2fν(rνy, 1 − rν2y2) (1 − |rνy|2)1/4 2

![image 156](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile156.png>)

Tν(gν) L2 = limsup

φ L2 ≤ limsup

= limsup fν L2(σ,+),

![image 157](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile157.png>)

ν→∞

ν→∞

where the integral in L2(σ, +) should be understood as integrating over the upper hemisphere.

If µ(P0) = 0, then we set l = 0, and e0ν = gν for all ν ≥ 1. Otherwise, µ(P0) > 0, then up

- to a subsequence, there exists nontrivial φ1 ∈ L2 and (x1ν, t1ν)ν≥1 such that

φ1 = w − lim

ν→∞

- (104) Tν1(Pν0)(y), φ1 2 ≥

- 1

![image 158](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile158.png>)

- 2


- (105) µ(P0). Let P1 denote the sequence {gν(y) − (Tν1)−1(φ1)(y)}ν≥1 and set


e1ν := gν(y) − (Tν1)−1(φ1)(y). It is not hard to see that

w − lim

ν→∞

- (106) Tν1(Pν1) = 0,
- (107) fν 2L2(S1) − φ1 22 = elν 22, as ν → ∞.


For P1 = {gν(y) − (Tν1)−1(φ1)(y)}ν≥1, we iteratively consider the set W(P1) = {w − lim

ν→∞

Tν(Pν1) in L2(R) : (tν, xν) ∈ R2}. Then we test whether µ(P1) > 0: if µ(P1) = 0, then the algorithm stops. If not, then up

- to a subsequence, there exists nontrivial φ2 ∈ L2 and and (x2ν, t2ν)ν≥1 such that


- (108) Tν2(Pν1)(y), φ2 2 ≥

- 1

![image 159](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile159.png>)

- 2


- (109) µ(P1).


φ2 = w − lim

ν→∞

By a similar consideration as in (106) and (107), if setting P2 = {Pν1 − (Tν2)−1(φ2)} and assuming (98), then

Tν2(Pν2) = 0,

w − lim

ν→∞

2

fν 22 −

φj 22 = e2ν 22, as ν → ∞,

j=1

where

e2ν := gν − (Tν1)−1φ1 − (Tν2)−1φ2.

The orthogonality in the L2 norm above needs an input, namely, (98). Otherwise, up to a subsequence we may assume that

|t2ν − t1ν| + |x2ν − x1ν| → c, as ν → ∞, for some 0 ≤ c < ∞. In this case, the dominated convergence theorem gives, up to a subsequence,

Tν2(Tν1)−1 converges strongly in L2. This will imply that

- (110) Tν2(Pν1) → 0, weakly in L2, as Tν1(Pν1) → 0 weakly in L2 and the following relation holds,

Tν2(Pν1) = Tν2(Tν1)−1 Tν1(Pν1) . But the claim in (110) is a contradiction to the existence of nontrivial φ2. So (98) holds.

Iterating this argument, a diagonalization process produces a family of pairwise orthogonal sequences (xjν, tjν) and φj satisfying (97), (98) and (99). Since j φj 22 ≤ supν fν 22 < ∞ and µ(Pl+1) ≤ 2 φl 2, we have

- (111) µ(Pl) → 0, as l → ∞.

To conclude this step, we deduce some information on elν. Firstly, the orthogonality condition (98) implies that, for any ψ ∈ L∞, the orthogonality (98) implies that, for each

- l ≥ 1,


- (112) gνψ 22 =


l

φjψ 22 + elνψ 22 as ν → ∞. In particular, this holds for ψ ∈ S, the Schwartz class on R. Let R ≫ 1. Deﬁne a set

j=1

E = {y ∈ R : |y| ≤ R and |gν(y)| ≤ R for all suﬃciently large ν}. Then (112) implies that, for any l ≥ 1,

elν1E L∞ ≤ CR for some C > 0. This further implies that,

limsup

ν→∞

limsup

ν→∞

(1 − rν2y2)1/4elν1E L∞ ≤ CR.

- Step 2. At this step, we show that the localized restriction estimate L∞ → Lqt,x for some q < 6 in Lemma 6.4, together with the information that limµ(Pl) = 0, will imply (100). To do it, by scaling, the norm on the left hand side of (100) is equivalent to


√

![image 160](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile160.png>)

1−r2

νy2−1 r2

elν(y) (1 − rν2y2)1/4

eixy+it

![image 161](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile161.png>)

dy L6

.

ν

![image 162](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile162.png>)

t,x

For each R ≫ 1, recall the deﬁnition of the set E. We split elν = elν1E + elν(1 − 1E). Since the following operator is uniformly bounded from L2(R) to L6t,x(R × R),

√

![image 163](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile163.png>)

1−r2

νy2−1 r2

φ(y) (1 − rν2y2)1/4

φ  → eixy+it

![image 164](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile164.png>)

dy,

ν

![image 165](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile165.png>)

and fν is upper normalized with respect to C(zν, rν), up to a subsequence, we may conclude that by (112)

√

![image 166](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile166.png>)

1−r2

νy2−1 r2

elν(y)(1 − 1E) (1 − rν2y2)1/4

eixy+it

≤ C elν(y)(1 − 1E) 2 ≤ C gν(1 − 1E) 2 ≤ Θ(R)

![image 167](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile167.png>)

dy L6

ν

![image 168](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile168.png>)

t,x

as ν → ∞. So we may restrict our attention to elν on E. By the discussion at the end of Step 1, we may assume that, for all l ≥ 1,

- (113) limsup

ν→∞

(1 − rν2y2)

1

![image 169](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile169.png>)

4elν1E ∞ ≤ CR. Then by Lemma 6.4,

limsup

ν→∞

e

it∆

![image 170](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile170.png>)

2 hν(t)

elν1E (1 − rν2y2)1/4 L

![image 171](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile171.png>)

q t,x

≤ C

for some C > 0 independent of ν and l. Then by the interpolation, establishing (100) is reduced to

- (114) limsup

l→∞

limsup

ν→∞

e

it∆

![image 172](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile172.png>)

2 hν(t)

elν(y) (1 − rν2y2)1/4 L

![image 173](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile173.png>)

∞ t,x

= 0.

This will follow from the fact that µ(Pl) → 0 as l → ∞. Indeed, there exists (xlν, tlν) such that, up to a subsequence,

- (115) e

itl

ν∆

![image 174](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile174.png>)

2 hν(tlν))

elν1E (1 − rν2y2)1/4

![image 175](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile175.png>)

(xlν) ∼ e

it∆

![image 176](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile176.png>)

2 hν(t))

elν1E (1 − rν2y2)1/4 L

![image 177](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile177.png>)

∞ t,x

.

On the other hand, since elν is compactly supported, e−

itl

νy2

![image 178](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile178.png>)

2 eix

l

νyhν(tlν, y))

elν1E (1 − rν2y2)1/4

![image 179](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile179.png>)

= e−

itl

νy2

![image 180](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile180.png>)

2 eix

l

νyhν(tlν, y))

elν1E (1 − rν2y2)1/4

![image 181](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile181.png>)

φR(y)

for some suitable bump function φR adapted to the ball B(0, R); taking integration in y on both sides, we have

- (116) e

itl

ν∆

![image 182](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile182.png>)

2 hν(tlν, y))

elν1E (1 − rν2y2)1/4

![image 183](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile183.png>)

(xlν) = e−

itl

νy2

![image 184](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile184.png>)

2 eix

l

νyhν(tlν, y)elν,

φR1E (1 − rν2y2)1/4 L

![image 185](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile185.png>)

2 y

.

Since Pl = {elν}ν≥1, by the deﬁnition of µ(Pl),

- (117) LHS (115) ≤ µ(Pl)


φR1E (1 − rν2y2)1/4 L

2 ≤ µ(Pl) φR1E L2 → 0, as l → ∞, since µ(Pl) → 0 as l → ∞. This ﬁnishes the proof of (100). Therefore the proof of Proposition 6.2 is complete.

![image 186](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile186.png>)

Next we show that (98) implies the orthogonality result (103) in Proposition 6.3.

- The proof of Proposition 6.3. To begin, we may assume that φj and φk are smooth functions with compact supports. Also we recall that


√

![image 187](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile187.png>)

1−r2

νy2−1 r2

+y22 φk(y) (1 − rν2y2)1/4

Gkν (1 − rν2y2)1/4

k ν)y2

k ν)

k ν)−i(t−t

2 ei(t−t

it∆

= ei(x−x

![image 188](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile188.png>)

![image 189](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile189.png>)

dy.

e

2 hν(t, y)

![image 190](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile190.png>)

![image 191](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile191.png>)

ν

![image 192](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile192.png>)

![image 193](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile193.png>)

j ν

it∆

2 hν(t, y) G

(1−rν2y2)1/4 . Then by a change of variables, we need to show

Likewise for e

![image 194](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile194.png>)

![image 195](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile195.png>)

√

![image 196](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile196.png>)

1−r2

νy2−1 r2

φj (1 − rν2y2)1/4

2 2

j ν−tk

j ν−tkν)

+y

t−(t

ν)

2 ∆ ei t−(t

ei

x − (xjν − xkν) ×

![image 197](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile197.png>)

![image 198](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile198.png>)

![image 199](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile199.png>)

ν

![image 200](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile200.png>)

√

- (118)

as ν goes to inﬁnity. For a large N ≫ 1, set

ΩN := {(t, x) : |t| + |x| ≤ N}, ΩN,ν = ΩN − (tjν − tkν, xjν − xkν). We ﬁrst claim that, for Ω = ΩN or ΩN,ν,

Ωc

ei

t−(t

j ν−tk

ν)

![image 201](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile201.png>)

2 ∆ ei t−(t

j ν−tkν)

√

![image 202](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile202.png>)

1−r2

νy2−1 r2

![image 203](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile203.png>)

ν

+y22 φj (1 − rν2y2)1/4

![image 204](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile204.png>)

![image 205](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile205.png>)

x − (xjν − xkν) ×

× e

it∆

![image 206](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile206.png>)

2 eit

√

![image 207](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile207.png>)

1−r2

νy2−1 r2

![image 208](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile208.png>)

ν

+y22 φk (1 − rν2y2)1/4

![image 209](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile209.png>)

![image 210](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile210.png>)

3

dxdt → 0

- (119)

as N goes to inﬁnity uniformly in ν. Here Ωc := R2 \ Ω. We write

e

it∆

![image 211](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile211.png>)

2 eit

√

![image 212](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile212.png>)

1−r2

νy2−1 r2

![image 213](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile213.png>)

ν

+y

2 2

![image 214](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile214.png>)

φk (1 − rν2y2)1/4

![image 215](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile215.png>)

(x) = eixy+it

√

![image 216](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile216.png>)

1−|rνy|2−1 r2 ν

![image 217](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile217.png>)

φk(y) (1 − rν2y2)1/4

![image 218](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile218.png>)

dy.

For y in a compact set in R and all suﬃciently small rν > 0, we have

- (120) ∂y2

![image 219](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile219.png>)

1 − |rνy|2 − 1 rν2 ∼ 1/4, uniformly in all suﬃciently large ν.

![image 220](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile220.png>)

We state three important estimates uniformly in all suﬃciently large ν. The ﬁrst is by the stationary phase estimate [26, p.334]:

- (121) e


![image 221](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile221.png>)

1−r2

νy2−1 r2

φk (1 − rν2y2)1/4

2 2

+y

2 eit

it∆

![image 222](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile222.png>)

![image 223](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile223.png>)

× e

→ 0

![image 224](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile224.png>)

ν

![image 225](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile225.png>)

L3t,x

√

![image 226](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile226.png>)

1−r2

νy2−1 r2

+y22 φk (1 − rν2y2)1/4

2 eit

it∆

(x) ≤ Cφk|t|−1/2.

![image 227](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile227.png>)

![image 228](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile228.png>)

![image 229](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile229.png>)

ν

![image 230](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile230.png>)

Secondly by integration by parts, if |x| ≥ C|t| for a large constant C > 0 depending on the size of the compact support of φk, for all suﬃciently large ν,

- (122) e

it∆

![image 231](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile231.png>)

2 eit

√

![image 232](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile232.png>)

1−r2

νy2−1 r2

![image 233](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile233.png>)

ν

+y

2 2

![image 234](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile234.png>)

φk (1 − rν2y2)1/4

![image 235](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile235.png>)

(x) ≤ Cφk|x|−1. Thirdly there always holds a trivial bound, for all x, t,

- (123) e

it∆

![image 236](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile236.png>)

2 eit

√

![image 237](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile237.png>)

1−r2

νy2−1 r2

![image 238](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile238.png>)

ν

+y22 φk (1 − rν2y2)1/4

![image 239](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile239.png>)

![image 240](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile240.png>)

(x) ≤ Cφk.

Here all constants Cφk depends on the function φk but independent of ν. We are now ready to prove (119) when Ω = ΩN; the case where Ω = ΩN,ν is similar and so will be omitted. By the Cauchy-Schwarz inequality,

LHS of (119) ≤ C ei

t−(t

j ν−tk

ν)

![image 241](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile241.png>)

2 ∆ ei t−(t

j ν−tkν)

√

![image 242](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile242.png>)

1−r2

νy2−1 r2

![image 243](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile243.png>)

ν

+y

2 2

![image 244](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile244.png>)

φj (1 − rν2y2)1/4

![image 245](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile245.png>)

x − (xjν − xkν)

3

L6(R2)

× e

it∆

![image 246](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile246.png>)

2 eit

√

![image 247](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile247.png>)

1−r2

νy2−1 r2

![image 248](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile248.png>)

ν

+y

2 2

![image 249](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile249.png>)

φk (1 − rν2y2)1/4

![image 250](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile250.png>)

3

L6t,x(ΩcN)

≤ C e

it∆

![image 251](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile251.png>)

2 eit

√

![image 252](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile252.png>)

1−r2

νy2−1 r2

![image 253](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile253.png>)

ν

+y

2 2

![image 254](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile254.png>)

φj (1 − rν2y2)1/4

![image 255](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile255.png>)

3

L6(R2)

×

× e

it∆

![image 256](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile256.png>)

2 eit

√

![image 257](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile257.png>)

1−r2

νy2−1 r2

![image 258](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile258.png>)

ν

+y

2 2

![image 259](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile259.png>)

φk (1 − rν2y2)1/4

![image 260](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile260.png>)

3

L6t,x(ΩcN)

.

- (124)

The ﬁrst term is bounded by the Tomas-Stein inequality and a change of variables. For the second term, by using estimates (121), (122) and (123), we see that

- (125) e

it∆

![image 261](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile261.png>)

2 eit

√

![image 262](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile262.png>)

1−r2

νy2−1 r2

![image 263](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile263.png>)

ν

+y

2 2

![image 264](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile264.png>)

φk (1 − rν2y2)1/4

![image 265](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile265.png>)

3

L6t,x(ΩcN)

→ 0, as N → ∞, uniform in ν.

Therefore we have established (119). To ﬁnish the proof (118), we need to show that, for a ﬁxed N ≫ 1,

ΩN∩ΩN,ν

ei

t−(t

j ν−tk

ν)

![image 266](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile266.png>)

2 ∆ ei t−(t

j ν−tkν)

√

![image 267](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile267.png>)

1−r2

νy2−1 r2

![image 268](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile268.png>)

ν

+y

2 2

![image 269](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile269.png>)

φj (1 − rν2y2)1/4

![image 270](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile270.png>)

x − (xjν − xkν) ×

× e

it∆

![image 271](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile271.png>)

2 eit

√

![image 272](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile272.png>)

1−r2

νy2−1 r2

![image 273](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile273.png>)

ν

+y

2 2

![image 274](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile274.png>)

φk (1 − rν2y2)1/4

![image 275](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile275.png>)

3

→ 0

- (126)


as ν goes to inﬁnity. It actually holds as measure(ΩN ∩ ΩN,ν) → 0, when lim

|tjν − tkν| + |xjν − xkν| = ∞,

ν→∞

t,x-bounds to both integrals, which are controlled as φj and φk are assumed to be bounded and compactly supported. Therefore the proof of (103) is complete.

and we can apply L∞

- 6.5. Ruling out small caps. By the discussion at the beginning of Section 6, we aim to show that

(127) lim

ν→∞

fν+σ 66 ≤ R6P,

which leads to R ≤ (5/2)1/6RP. However, it is a contradiction to the strict inequality in Proposition 2.1.

By Propositions 6.2 and 6.3,

lim

ν→∞

fν+σ 66 ≤

∞

j=1

lim

ν→∞

e

it∆

![image 276](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile276.png>)

2 hν(t, y)

Gjν (1 − rν2y2)1/4

![image 277](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile277.png>)

6 6

=

j

lim

ν→∞

ei(x−x

j ν)y−(t−t

j ν)y2

![image 278](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile278.png>)

2 ei(t−t

j ν)

√

![image 279](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile279.png>)

1−r2

νy2−1 r2

![image 280](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile280.png>)

ν

+y22 φj(y) (1 − rν2y2)1/4

![image 281](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile281.png>)

![image 282](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile282.png>)

dy

6

6

=

j

lim

ν→∞

eixy−

ty2

![image 283](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile283.png>)

2 eit

√

![image 284](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile284.png>)

1−r2

νy2−1 r2

![image 285](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile285.png>)

ν

+y

2 2

![image 286](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile286.png>)

φj(y) (1 − rν2y2)1/4

![image 287](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile287.png>)

dy

6

6

=

j

e

it∆

![image 288](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile288.png>)

2 φj 66 ≤ R6P

j

φj 62

≤ R6P

j

φj 22 3

≤ R6P lim

ν→∞

fν+ 62 = R6P.

(128)

This proves (127). Here we have used

lim

ν→∞

eixy−

ty2

![image 289](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile289.png>)

2 eit

√

![image 290](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile290.png>)

1−r2

νy2−1 r2

![image 291](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile291.png>)

ν

+y22 φj(y) (1 − rν2y2)1/4

![image 292](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile292.png>)

![image 293](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile293.png>)

dy − e

it∆

![image 294](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile294.png>)

2 φj(x)

6

= 0.

This follows from the stationary phase analysis and the dominated convergence theorem. So far we have proved that the ﬁrst half of Proposition 2.14 that infν rν > 0.

- 6.6. Big caps; existence of extremals. In this section we aim to prove the second half of Proposition 2.14: There exists an extremal function for the Tomas-Stein inequality


(1). The proof is similar to the process of ruling out small caps above. Let {fν} be an extremizing sequence of nonnegative functions supported on the whole sphere and even upper normalized with respect to caps Cν ∪ (−Cν). We have proved that infν rν > 0. Then up to a subsequence, the uniform upper normalization means simply that fν L2(S1) ≤ 1, and there exists a function Θ independent of ν and satisfying that Θ(R) → 0 as R → ∞,

such that

|fν(x)|2dσ(x) ≤ Θ(R) for all ν. The radii no longer enter into the discussion. We denote f±

|fν(x)|>R

ν the restrictions of fν to the upper hemisphere S+1 and the lower. Then we see that fν+(x) = fν−(−x), for x ∈ S+1 , and fν 22 = 2 fν+ 22. Moreover, by a simple change of variables,

- (129) fν−σ(t, x) = fν+σ(−t, −x) = fν+σ(t, x). Then

![image 295](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile295.png>)

- (130) fνσ(t, x) = fν+σ(t, x) + fν−σ(t, x) = 2ℜ fν+σ(t, x), where ℜf denotes the real part of f. Write

fν+(x, t) =

S+1

ei(x,t)·zfν+(z)dσ(z)

= eixy+it

√

![image 296](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile296.png>)

1−y2fν+(y, 1 − y2)

![image 297](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile297.png>)

dy 1 − y2

![image 298](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile298.png>)

![image 299](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile299.png>)

.

Similar to Propositions 6.2 and 6.3 in the subsection 6.1, we will develop a proﬁle decomposition for fν+(y, 1 − y2)/(1 − y2)1/4.

![image 300](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile300.png>)

- Proposition 6.7. Let {fν+} be deﬁned above. Then there exists a sequence (xkν, tkν) ∈ R2 and elν ∈ L2(R) such that

(131)

fν+(y) (1 − y2)1/4

![image 301](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile301.png>)

=

l

j=1

e−ix

j νy−itjν

√

![image 302](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile302.png>)

1−y2φj(y) + elν(y)

with the following properties: The parameters {(xkν, tkν)} satisfy, for k = j,

- (132) |xkν − xjν| + |tkν − tjν| → ∞, as ν → ∞. For each l ≥ 1,
- (133) fν+ 2L2(S1) =


l

j=1

φj 22 + elν 22, as ν → ∞.

The function elν satisﬁes, if Eνl = (1 − y2)1/4elν

(134) limsup

l→∞

limsup

ν→∞

Eνl σ

L6t,x(R2)

= 0.

- Proposition 6.8 (Orthogonality). Let {(xjν, tjν)} be as above and set


- (135) 4φk,

Gjν := e−ix

j νy−itjν

√

![image 303](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile303.png>)

1−y2(1 − y2)

1

![image 304](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile304.png>)

- (136) 4φj.


√

![image 305](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile305.png>)

1

k νy−itkν

1−y2(1 − y2)

Gkν := e−ix

![image 306](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile306.png>)

Then for k = j,

Gkνσ Gjνσ

- (137) = 0.

The proofs are similar and so we omit the details. Now we are ready to prove the existence of extremals for (1).

R6 = lim

ν→∞

fνσ 66 = 26 limsup

l→∞

lim

ν→∞

 ℜ

l

j=1

Gjνσ + Eνlσ 66

≤ 26 limsup

l→∞

lim

ν→∞

 ℜ

l

j=1

Gjνσ 66

=

j

ei(x,t)·z(1 − y2)1/4[φj(y)1S1

+

(z) + φ¯j(y)1−S1

+

(z)]dσ(y)

6

6

≤ R6

j

(1 − y2)1/4[φj(y)1S1

+

(z) + φ¯j(y)1−S1

+

(z)] 6L2(S1,σ)

≤ R6

j

2 φj 22 3 ≤ R6

j

2 φj 22

3

≤ R6 2 fν+ 22 3 = R6 fν 62 = R6.

- (138)

where z = (y, ·) ∈ S1, and 1S1

+

and 1−S1

+

denotes the indicator functions of the upper and the lower hemispheres of S1, respectively.

Then R6 = R6 forces all the inequalities above to be equal. On the other hand, because 2 j φj 2L2 ≤ fν L2(S1,σ) = 1, there will be only one j left from the sharpness of embedding of ℓ3 into ℓ1. Thus for this j, there exists an extremal

φ(y)1S1

+

+ φ¯j(y)1−S1

+

(1 − y2)1/4. This completes the proof of Proposition 2.14 and hence Theorem 1.2.

Appendix A. A strict comparison, S > (5/2)1/6P.

In this section, we aim to establish the strict comparison inequality in Proposition 2.1 by using a similar perturbation argument in [12, Section 17] on

fεσ 66/ fε 62,

where fε is deﬁned in (141). We list several deﬁnitions.

- (139) y, (1 − |y|2)1/2 = y, 1 −


lim

L3t,x(R2)

ν→∞

- 1

![image 307](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile307.png>)

- 2|y|2 −


1 8|y|4 + O(|y|6) ,

![image 308](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile308.png>)

- (140) dσε := 1 +

- 1

![image 309](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile309.png>)

- 2|y|2 + O(|y|4) dy,


- (141) fε(z) := ε−1/4e(z

2−1)/εχ|z

1|≤21χz

![image 310](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile310.png>)

2>0. uε(t, x) :=

S1

fε(z)e−i(x,t)·zdσ(z)

= ε−1/4e−it

R

e −

- 1

![image 311](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile311.png>)

- 2|y|2−18|y|4+O(|y|6) ε−1×


![image 312](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile312.png>)

× e−ix·ye−it −

- 1

![image 313](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile313.png>)

- 2|y|2−18|y|4+O(|y|6) 1 +


![image 314](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile314.png>)

1 2|y|2 + O(|y|4) χ|y|≤1/2(y)dy

![image 315](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile315.png>)

= ε1/4e−it

R

e−iε

1/2x·ye−(1−iεt) × 1 +

- 1

![image 316](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile316.png>)

- 2|y|2+8ε|y|4+O(ε2|y|6) ×


![image 317](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile317.png>)

ε 2|y|2 + O(ε2|y|4) χ|y|≤1/2(ε1/2y)dy,

![image 318](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile318.png>)

- (142)

where a change of variables is applied in passing to the last inequality. We continue to set vε(t, x) := ε−1/4uε(ε−1t, ε−1/2x)

= e−iε

−1t

R

e−ix·ye−(1−it) × 1 +

- 1

![image 319](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile319.png>)

- 2|y|2+8ε|y|4+O(ε2|y|6) ×


![image 320](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile320.png>)

ε 2|y|2 + O(ε2|y|4) χ(ε1/2y)dy,

![image 321](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile321.png>)

- (143)
- (144) wε(t, x) :=

R

e−ix·ye−(1+it)

- 1

![image 322](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile322.png>)

- 2|y|2+8ε|y|4 1 +


![image 323](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile323.png>)

ε 2|y|2 dy.

![image 324](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile324.png>)

- (145) gε(y) := e−

- 1

![image 325](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile325.png>)

- 2|y|2−8ε|y|4,


![image 326](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile326.png>)

- (146) dσε(y) = 1 +

ε 2|y|2 dy.

![image 327](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile327.png>)

Note that 1 − it → 1 + it when passing vε to wε, which amounts to a complex conjugation. Then we see that

- (147) vε 6L6(R2) = uε 6L6(R2), wε 6L6(R2) = vε 6L6(R2) + O(ε2)

= uε 6L6(R2) + O(ε2), as ε → 0+.

- (148)
- (149) fε 2L2(S1,σ) = gε 2L2(R,σε) + O(ε2), as ε → 0+. We consider the functional
- (150) Ψ(ε) = log

uε 66 fε 62

![image 328](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile328.png>)

,

which is initially deﬁned for ε > 0 and extends continuously and diﬀerentially to ε = 0. The derivative is

- (151) ∂ε|ε=0Ψ(ε) =


∂ε|ε=0 wε 66 w0 66 − 3

∂ε|ε=0 gε 22 g0 22

.

![image 329](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile329.png>)

![image 330](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile330.png>)

We observe that,

- (152) Ψ(0) = log(R6P). We will calculate that Lemma A.1.
- (153) ∂ε|ε=0Ψ(ε) > 0.

Proof.

∂ε|ε=0wε =

- 1

![image 331](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile331.png>)

- 2


(1 + it)∂t2 + i∂t

R

e−ix·y−

1+it

![image 332](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile332.png>)

2 |y|2dy

=

- 1

![image 333](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile333.png>)

- 2


(1 + it)∂t2 + i∂t c0(1 + it)−1/2e−

|x|2 2(1+it)

![image 334](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile334.png>)

=

- 1

![image 335](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile335.png>)

- 2


(1 + it)∂t2 + i∂t w0(t, x),

- (154)

where c0 > 0 is some universal constant and w0 := c0(1 + it)−1/2e−

|x|2

![image 336](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile336.png>)

2(1+it). Deﬁne

- (155) φ(t, x) := −

- 1

![image 337](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile337.png>)

- 2|x|2(1 + it)−1 −


- 1

![image 338](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile338.png>)

- 2


log(1 + it). Then

- (156) w0(t, x) = c0(1 + it)−1/2e−

|x|2

![image 339](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile339.png>)

2(1+it) = c0eφ. Continuing the computation in (154),

- (157)

- 1 + it

![image 340](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile340.png>)

- 2


(φ2t + φtt) + iφt w0. We compute

φt =

i 2|x|2(1 + it)−2 −

![image 341](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile341.png>)

i 2

![image 342](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile342.png>)

- (158) (1 + it)−1,

φtt = |x|2(1 + it)−3 −

- 1

![image 343](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile343.png>)

- 2


- (159) (1 + it)−2,

φ2t = −

1 4|x|4(1 + it)−4 +

![image 344](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile344.png>)

- 1

![image 345](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile345.png>)

- 2|x|2(1 + it)−3 −


1 4

![image 346](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile346.png>)

- (160) (1 + it)−2. Thus
- (161) φ2t + φtt = −

1 4|x|4(1 + it)−4 +

![image 347](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile347.png>)

3 2|x|2(1 + it)−3 −

![image 348](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile348.png>)

- 3

![image 349](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile349.png>)

- 4


(1 + it)−2. Then

- 1 + it

![image 350](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile350.png>)

- 2


(φ2t + φtt) + iφt =

= −

1 8|x|4(1 + it)−3 +

![image 351](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile351.png>)

1 4|x|2(1 + it)−2 +

![image 352](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile352.png>)

1 8

![image 353](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile353.png>)

(1 + it)−1.

- (162)


Taking the real part in (162), we have ℜ

- 1 + it

![image 354](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile354.png>)

- 2


(φ2t + φtt) + iφt

- (163)

Since

- (164) ∂ε wε 66 = ∂ε |wε|6 = ∂ε wεwε 3 = 6 |wε|6ℜ

![image 355](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile355.png>)

∂εwε wε

![image 356](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile356.png>)

, we have

∂ε|ε=0 wε 66 = 6 ℜ

- 1 + it

![image 357](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile357.png>)

- 2


(φ2t + φtt) + iφt |w0|6dxdt

= c60 −

- 3

![image 358](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile358.png>)

- 4|x|4(1 + t2)−3(1 − 3t2) +


3 2|x|2(1 + t2)−2(1 − t2) +

![image 359](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile359.png>)

3 4

![image 360](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile360.png>)

(1 + t2)−1 ×

× (1 + t2)−3/2e−3

|x|2 1+t2

![image 361](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile361.png>)

dxdt

= c60 −

- 3

![image 362](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile362.png>)

- 4|x|4(1 − 3t2) +


3 2|x|2(1 − t2) +

![image 363](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile363.png>)

- 3

![image 364](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile364.png>)

- 4


(1 + t2)−2e−3|x|

2

dxdt

= c60 −

- 3

![image 365](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile365.png>)

- 4


(1 − 3t2)

√π 12√3

![image 366](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile366.png>)

![image 367](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile367.png>)

![image 368](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile368.png>)

+

3 2

![image 369](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile369.png>)

(1 − t2)

√π 6√3

![image 370](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile370.png>)

![image 371](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile371.png>)

![image 372](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile372.png>)

+

- 3√π

![image 373](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile373.png>)

![image 374](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile374.png>)

- 4√3


![image 375](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile375.png>)

(1 + t2)−2dt,

- (165)

where we have used that

R

e−3|x|

2

dx =

√π √3

![image 376](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile376.png>)

![image 377](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile377.png>)

![image 378](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile378.png>)

,

R

|x|2e−3|x|

2

dx =

√π 6√3

![image 379](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile379.png>)

![image 380](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile380.png>)

![image 381](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile381.png>)

, and

R

|x|4e−3|x|

2

dx =

√π 12√3

![image 382](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile382.png>)

![image 383](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile383.png>)

![image 384](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile384.png>)

. Hence we continue (165),

=c60 −

√π 16√3 R

![image 385](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile385.png>)

![image 386](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile386.png>)

![image 387](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile387.png>)

(t2 − 3)(1 + t2)−2dt +

- 3√π

![image 388](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile388.png>)

![image 389](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile389.png>)

- 4√3 R


![image 390](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile390.png>)

(1 + t2)−2dt

= c60

√π 16√3 −

![image 391](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile391.png>)

![image 392](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile392.png>)

![image 393](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile393.png>)

R

t2(1 + t2)−2dt + 15

R

(1 + t2)−2dt

= c60

7π√π 16√3

![image 394](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile394.png>)

![image 395](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile395.png>)

![image 396](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile396.png>)

- (166)

where we have used that

R

t2(1 + t2)−2dt = π/2, and

R

(1 + t2)−2dt = π/2. To conclude so far, we obtain,

∂ε|ε=0 wε 66 = c60

7π√π 16√3

![image 397](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile397.png>)

![image 398](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile398.png>)

![image 399](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile399.png>)

. On the other hand,

- (167) w0 66 = c60 (1 + t2)−3/2e−


1 8|x|4(1 + t2)−3(1 − 3t2) +

1 4|x|2(1 + t2)−2(1 − t2) +

= −

![image 400](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile400.png>)

![image 401](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile401.png>)

π√π 2√3

3|x|2 1+t2

![image 402](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile402.png>)

dxdt = c60

![image 403](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile403.png>)

![image 404](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile404.png>)

![image 405](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile405.png>)

1 8

(1 + t2)−1.

![image 406](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile406.png>)

.

Therefore we conclude that

- (168)

∂ε|ε=0 wε 66 w0 66

![image 407](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile407.png>)

=

- 7

![image 408](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile408.png>)

- 8


.

We are left with computing 3∂ε|ε=0 gε

2 2

![image 409](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile409.png>)

g0 22 : ∂ε|ε=0 gε 22 =

R

−

1 4

![image 410](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile410.png>)

y4 +

- 1

![image 411](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile411.png>)

- 2


y2 e−y

2

dy

= −

1 4 ×

![image 412](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile412.png>)

- 3√π

![image 413](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile413.png>)

![image 414](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile414.png>)

- 4


+

- 1

![image 415](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile415.png>)

- 2 ×


√π 2

![image 416](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile416.png>)

![image 417](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile417.png>)

=

√π 16

![image 418](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile418.png>)

![image 419](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile419.png>)

.

g0 22 =

R

e−y

2

dy = √π.

![image 420](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile420.png>)

- (169)

Note that in the ﬁrst inequality we have used that

R

y4e−y

2

dy =

- 3√π

![image 421](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile421.png>)

![image 422](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile422.png>)

- 4


, and

R

y2e−y

2

dy =

√π 2

![image 423](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile423.png>)

![image 424](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile424.png>)

. So we have

- (170) 3

∂ε|ε=0 gε 22 g0 22

![image 425](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile425.png>)

=

3 16

![image 426](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile426.png>)

.

Combining (151), (168) and (170), we see that

- (171) ∂ε|ε=0Ψ(ε) =

- 7

![image 427](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile427.png>)

- 8 −


3 16

![image 428](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile428.png>)

=

11 16

![image 429](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile429.png>)

> 0,

which establishes the claim in Lemma A.1. Then the following symmetry consideration completes the proof of Proposition 2.1: Let fε be deﬁned in (141), and f˜ε(x) := fε(−x), Fε := (fε + f˜ε)/√2. Then Fε 2 = fε 2 and

![image 430](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile430.png>)

- (172)

Fεσ ∗ Fεσ ∗ Fεσ 2 Fε 32 ≥ (5/2)1/2

![image 431](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile431.png>)

fεσ ∗ fεσ ∗ fεσ 2 fε 32

![image 432](<2015-shao-existence-extremizers-tomas-stein-inequality_images/imageFile432.png>)

.

We focus on proving (172).

- (173) Fεσ ∗ Fεσ ∗ Fεσ = 2−3/2(fεσ + f˜εσ) ∗ (fεσ + f˜εσ) ∗ (fσ + f˜εσ). Because of the identity (59),

fεσ ∗ fεσ ∗ fεσ, fεσ ∗ fεσ ∗ fεσ = fεσ ∗ fεσ ∗ f˜εσ, f˜εσ ∗ fεσ ∗ fεσ

= fεσ ∗ f˜εσ ∗ fσ,˜ f˜εσ ∗ f˜εσ ∗ fεσ

= f ˜εσ ∗ f˜εσ ∗ f˜εσ, f˜εσ ∗ f˜εσ ∗ f˜εσ .

- (174)

So by nonnegativity, we see that

- (175) Fεσ ∗ Fεσ ∗ Fεσ 22 ≥ 2−3(1 + 9 + 9 + 1) fεσ ∗ fεσ ∗ fεσ 22 = (5/2) fεσ ∗ fεσ ∗ fεσ 22, which yields (172).


References

- [1] P. B´egout and A. Vargas. Mass concentration phenomena for the L2-critical nonlinear Schr¨odinger equation. Trans. Amer. Math. Soc., 359(11):5257–5282, 2007.
- [2] J. Bennett, N. Bez, A. Carbery, and D. Hundertmark. Heat-ﬂow monotonicity of Strichartz norms. Analysis and PDE, Vol. 2 (2009), No. 2, 147–158.
- [3] J. Bennett, A. Carbery, M. Christ, and T. Tao. The Brascamp-Lieb inequalities: ﬁniteness, structure and extremals. Geom. Funct. Anal., 17(5):1343–1415, 2008.
- [4] J. Bennett, A. Carbery, and T. Tao. On the multilinear restriction and Kakeya conjectures. Acta Math., 196(2):261–302, 2006.
- [5] H. Bahouri and P. G´erard. High frequency approximation of solutions to critical nonlinear wave equations. Amer. J. Math., 121(1):131–175, 1999.
- [6] J. Bourgain. On the restriction and multiplier problems in R3. In Geometric aspects of functional analysis (1989–90), volume 1469 of Lecture Notes in Math., pages 179–191. Springer, Berlin, 1991.
- [7] R. Carles. and S. Keraani. On the role of quadratic oscillations in nonlinear Schr¨odinger equations. II. The L2-critical case. Trans. Amer. Math. Soc., 359(1):33–62, 2007.
- [8] M. Christ. On extremizers for a Radon-like transform. Preprint.
- [9] M. Christ. Quasi-extremals for a Radon-like transform. Preprint.
- [10] M. Christ, J. Colliander, and T. Tao. Asymptotics, frequency modulation, and low regularity illposedness for canonical defocusing equations. Amer. J. Math., 125(6):1235–1293, 2003.
- [11] M. Christ and R. Quilodr´an. Gaussians rarely extremize adjoint Fourier restriction inequalities for paraboloids. Proc. Amer. Math. Soc. 142 (3): 887–896, 2014.
- [12] M. Christ and S. Shao. Existence of extremals for a Fourier restriction inequality. Anal.PDE. 5(2): 261–312, 2012.
- [13] M. Christ and S. Shao. On the extremizers of an adjoint Fourier restriction inequality. Adv. Math. 230

(3): 957–977, 2012.

- [14] L. Fanelli, L. Vega and N. Visciglia. On the existence of maximizers for a family of restriction theorems. Bull. Lond. Math. Soc., 43(4):811–817, 2011.
- [15] D. Foschi. Maximizers for the Strichartz inequality. J. Eur. Math. Soc. (JEMS), 9(4):739–774, 2007.
- [16] D. Foschi. Global maximizers for the sphere adjoint Fourier restriction inequality. J. Funct. Anal., 268(3):690–702, 2015.
- [17] D. Hundertmark and V. Zharnitsky. On sharp Strichartz inequalities in low dimensions. Int. Math. Res. Not., pages Art. ID 34080, 18, 2006.
- [18] M. Kunze. On the existence of a maximizer for the Strichartz inequality. Comm. Math. Phys., 243(1):137–162, 2003.
- [19] P.-L. Lions. The concentration-compactness principle in the calculus of variations. The locally compact case. I. Ann. Inst. H. Poincare´ Anal. Non Line´aire, 1(2):109–145, 1984.
- [20] P.-L. Lions. The concentration-compactness principle in the calculus of variations. The locally compact case. II. Ann. Inst. H. Poincare´ Anal. Non Line´aire, 1(4):223–283, 1984.
- [21] P.-L. Lions. The concentration-compactness principle in the calculus of variations. The limit case. I.

- Rev. Mat. Iberoamericana, 1(1):145–201, 1985.

[22] P.-L. Lions. The concentration-compactness principle in the calculus of variations. The limit case. II.

- Rev. Mat. Iberoamericana, 1(2):45–121, 1985.


- [23] A. Moyua, A. Vargas, and L. Vega. Restriction theorems and maximal operators related to oscillatory integrals in R3. Duke Math. J., 96(3):547–574, 1999.
- [24] S. Shao. The linear proﬁle decomposition for the Airy equation and the existence of maximizers for the Airy Strichartz inequality. Analysis and PDE, Vol. 2 (2009), No. 1, 83-117.
- [25] S. Shao. Maximizers for the Strichartz inequalities and the Sobolev-Strichartz inequalities for the Schr¨odinger equation. Electronic Journal of Diﬀerential Equations, Vol. 2009(2009), No. 03, pp. 1-13.
- [26] E. M. Stein. Harmonic analysis: real-variable methods, orthogonality, and oscillatory integrals, volume 43 of Princeton Mathematical Series. Princeton University Press, Princeton, NJ, 1993. With the assistance of Timothy S. Murphy, Monographs in Harmonic Analysis, III.


- [27] B. Stovall. Quasi-extremals for convolution with the surface measure on the sphere. Illinois J. Math. 53(2): 391–412, 2009.
- [28] T. Tao, A. Vargas, and L. Vega. A bilinear approach to the restriction and Kakeya conjectures. J. Amer. Math. Soc., 11(4):967–1000, 1998.


Department of Mathematics, University of Kansas, Lawrence, KS 66045 E-mail address: slshao@ku.edu

