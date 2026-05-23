# arXiv:1708.03826v1[math.CA]12Aug2017

## EXTREMIZERS FOR FOURIER RESTRICTION ON HYPERBOLOIDS

EMANUEL CARNEIRO, DIOGO OLIVEIRA E SILVA, AND MATEUS SOUSA

Abstract. The L2 → Lp adjoint Fourier restriction inequality on the d-dimensional hyperboloid Hd ⊂ Rd+1 holds provided 6 ≤ p < ∞, if d = 1, and 2(d + 2)/d ≤ p ≤ 2(d + 1)/(d − 1), if d ≥ 2. Quilodr´an [35] recently found the values of the optimal constants in the endpoint cases (d, p) ∈ {(2, 4), (2, 6), (3, 4)} and showed that the inequality does not have extremizers in these cases. In this paper we answer two questions posed in [35], namely: (i) we ﬁnd the explicit value of the optimal constant in the endpoint case (d, p) = (1, 6) (the remaining endpoint for which p is an even integer) and show that there are no extremizers in this case; and (ii) we establish the existence of extremizers in all non-endpoint cases in dimensions d ∈ {1, 2}. This completes the qualitative description of this problem in low dimensions.

1. Introduction

The connection between Fourier restriction estimates on smooth hypersurfaces and Strichartz estimates for linear partial diﬀerential equations has been understood for a while. For instance, Strichartz inequalities for the Schr¨dinger and wave equations correspond to Fourier restriction estimates on the paraboloid and the cone, respectively. These are not compact manifolds, but satisfy a scaling symmetry which makes the usual Tomas–Stein argument work. While the hyperboloid does not possess such a scaling symmetry, it is in some sense well-approximated by the paraboloid and the cone (see Figure 1) and it serves as an interesting intermediate case where new phenomena emerge. In this paper, we explore some of these phenomena in the context of sharp Fourier restriction theory.

Sharp adjoint Fourier restriction inequalities on the hyperboloid were ﬁrst studied by Quilodr´n [35], who further developed methods from earlier seminal work of Foschi [19] in the context of paraboloids and cones. These works serve as motivation for much of the present paper, and we try to follow the notation and terminology of [35] to facilitate the references. The hyperboloid Hd ⊂ Rd+1 is deﬁned by1

Hd = (y,y ) ∈ Rd × R : y = 1 + |y|2 ,

Date: August 15, 2017. 2010 Mathematics Subject Classiﬁcation. 42B10. Key words and phrases. Sharp Fourier restriction theory, extremizers, optimal constants, convolution of singular measures, concentration-compactness, Strichartz inequalities, Klein–Gordon equation, hyperboloid. 1A simple rescaling argument transfers all the results of this paper to the hyperboloid Hds = (y, y ) ∈ Rd × R : y =

s2 + |y|2 .

1

2

Figure 1. The paraboloid y = 1 + |x|

2 osculates the hyperboloid y = 1 + |x|2 at its vertex. The cone y = |x| approximates the same hyperboloid at inﬁnity.

and comes equipped with the Lorentz invariant measure dσ(y,y ) = δ y − 1 + |y|2

dy dy 1 + |y|2

which is deﬁned by duality on an appropriate dense class via

, (1.1)

dy 1 + |y|2

ϕ(y, 1 + |y|2)

ϕ(y,y )dσ(y,y ) =

.

Hd

Rd

We normalize the Fourier transform in Rd+1 in the following way: g(ζ) =

e−iz·ζ g(z)dz. (1.2)

Rd+1

With this normalization, the convolution and the L2(Rd+1)-norm satisfy g ∗ h = g · h; and g L2(Rd+1) = (2π)

d+1

2 g L2(Rd+1).

The Fourier restriction operator on the hyperboloid Hd maps a function g on the ambient space Rd+1 to the restriction of its Fourier transform to Hd. The Fourier extension operator on Hd is the adjoint of the Fourier restriction operator, and is given by

√

dy 1 + |y|2

1+|y|2f(y)

eix·yeit

,

Tf(x,t) =

Rd

where (x,t) ∈ Rd × R and f belongs to the Schwartz class in Rd. Here we are identifying a function f : Hd → C with a complex-valued function on Rd. Its norm in Lp(Hd) = Lp(Hd,σ) is

1 p

dy 1 + |y|2

|f(y)|p

f Lp(Hd) =

.

Rd

With the normalization (1.2) observe that Tf(x,t) = fσ(−x,−t). (1.3)

The classical work of Strichartz [40] establishes that

Tf Lp(Rd+1) ≤ Hd,p f L2(Hd) , (1.4) with a ﬁnite constant Hd,p (independent of f), provided that

 

6 ≤ p < ∞, if d = 1;

(1.5)



2(d+2)

d ≤ p ≤ 2(dd−+1)1 , if d ≥ 2.

For a ﬁxed dimension d ≥ 1, the lower and upper bounds in the admissible range of exponents p given by (1.5) correspond to the unique exponents for which the extension operator is bounded on the paraboloid and the cone, respectively, each equipped with the appropriate measure (projection measure on the paraboloid and Lorentz invariant measure on the cone).

In this paper we investigate sharp instances of the extension inequality on the hyperboloid. More precisely, given a pair (d,p) in the admissible range (1.5), we study extremizers and extremizing sequences for inequality (1.4), and are interested in the value of the optimal constant

Tf Lp(Rd+1) f L2(Hd)

Hd,p := sup

.

0 =f∈L2(Hd)

Quilodr´n [35] studied the endpoint cases (d,p) ∈ {(2,4),(2,6),(3,4)}. More precisely, he computed the values

- 5

- 6, and H3,4 = (2π)


5

- 3

- 4 π, H2,6 = (2π)


4 ,

H2,4 = 2

and established the nonexistence of extremizers for the inequality (1.4) associated to these three cases, which are the only ones for which d > 1 and p is an even integer. The arguments in [35] rely on explicit computations of the n-fold convolution of the measure σ with itself, and these are computationally challenging if n ≥ 3 and d = 2.

Here we answer two questions raised by Quilodr´n [35, p. 39], regarding: (i) the value of the sharp constant and existence of extremizers in the endpoint case (d,p) = (1,6); (ii) the existence of extremizers in the non-endpoint cases in dimensions d ∈ {1,2}. Our results below, together with the previous results of Quilodr´n [35], provide a complete qualitative description of this problem in low dimensions.

- Theorem 1. The value of the optimal constant in the case (d,p) = (1,6) is


- 1

- 2 .


1

H1,6 = 3−

12(2π) Moreover, extremizers for inequality (1.4) do not exist in this case. From Plancherel’s Theorem it follows that

Tf 3L6(R2) = ( fσ)3 L2(R2) = (fσ ∗ fσ ∗ fσ) L2(R2) = 2π fσ ∗ fσ ∗ fσ L2(R2), which in particular implies that

fσ ∗ fσ ∗ fσ L2(R2) f 3L2(H1)

H31,6 = 2π sup

. (1.6)

0 =f∈L2(H1)

We are thus led to studying convolution measure σ ∗σ ∗σ, a task which we will undertake in greater generality in §3 below. The rigidity of the endpoint lies at the heart of the mechanism responsible for the lack of compactness in these situations (with p even). It would be interesting to investigate if, in all the other endpoint cases (d,p) (now with p not an even integer), one still has lack of extremizers for (1.4).

On the other hand, recent works of Fanelli, Vega and Visciglia [17, 18] indicate that concentrationcompactness arguments may ensure the existence of extremizers in non-endpoint cases for certain families of restriction/extension estimates. It is important to remark that the problem considered here does not fall under the scope of the methods of [17, 18], since the hyperboloid is a non-compact surface which lacks dilation homogeneity (although many ideas from [17, 18] shall be useful). Our next result establishes that extremizers do exist in every non-endpoint case of the one- and twodimensional settings.

- Theorem 2. Extremizers for inequality (1.4) do exist in the following cases:


- (a) d = 1 and 6 < p < ∞.
- (b) d = 2 and 4 < p < 6.


As suggested, our proof of Theorem 2 relies on concentration-compactness arguments. The heart of the matter lies in the construction of a special cap, i.e. a cap that contains a positive universal proportion of the total mass in an extremizing sequence, possibly after applying the symmetries of the problem. This rules out the possibility of “mass concentration at inﬁnity” and is the missing part in [35, Proposition 2.1], which originally outlined the proof of a dichotomy statement for extremizing sequences. The successful quest for a special cap, carried out in §5, relies partly on the fact that the lower endpoint p is an even integer in these dimensions, and that the corresponding (p/2)-fold convolution of the measure σ with itself, when properly parametrized, decays to zero at inﬁnity. In this regard, our argument does not generalize to dimensions d ≥ 3. Other tools (e.g. coming from bilinear restriction theory, as in [8, 22, 36]) may be required to address the existence of extremizers in this general non-endpoint setting. In order to present elementary and self-contained arguments that exploit the convolution structure of the problem, we focus in this paper on the lower dimensional cases d ∈ {1,2}. We plan to address the higher dimensional situation in a later work.

- 1.1. Klein–Gordon propagator. As already pointed out, estimates for Fourier extension operators are related to estimates for dispersive partial diﬀerential equations. In our case, the operator T is related to the following Klein–Gordon equation


∂t2u = ∆xu − u, (x,t) ∈ Rd × R; u(x,0) = u0(x), ∂tu(x,0) = u1(x).

(1.7)

The connection comes from the following operator, the Klein–Gordon propagator, eit

√

√1−∆g(x) :=

1 (2π)d Rd

1+|ξ|2dξ.

g(ξ)eix·ξ eit

Indeed, one can see that solutions to (1.7) can be written as u(·,t) =

√

√1−∆u0(·) − ieit

√1−∆(

- 1

- 2


1 − ∆)−1u1(·) + e−it

eit

√

√1−∆u0(·) + ie−it

√1−∆(

- 1

- 2


1 − ∆)−1u1(·) , and that

√1−∆g(x), (1.8) where

Tf(x,t) = (2π)d eit

f(y) 1 + |y|2

. (1.9) This relation implies that the estimate (1.4) is equivalent to

g(y) :=

√1−∆g Lp

x,t(Rd×R) ≤ (2π)−d Hd,p g H 1

eit

2 (Rd), where Hs(Rd), for s ≥ 0, is the nonhomogeneous Sobolev space deﬁned by

Hs(Rd) = {g ∈ L2(Rd) : g 2Hs(Rd) :=

| g(ξ)|2(1 + |ξ|2)sdξ < ∞}.

Rd

This equivalent formulation will be very useful in this paper. In our concentration-compactness arguments, we explore the fact that convergence of an extremizing sequence {fn} in L2(Hd) is equivalent to convergence in H 21 (Rd) of the sequence {gn} determined by (1.9), and, once on the Sobolev side, we may use local compact embeddings. Observe also that, for each t ∈ R, the operator eit

√1−∆ is unitary in H 21(Rd).

Historical remarks. Our results complement the recent, vast and very interesting body of work concerning sharp Fourier restriction and Strichartz estimates. Sharp Fourier restriction theory has a relatively short history, with the ﬁrst works on the subject going back to Kunze [29], Foschi [19] and Hundertmark–Zharnitsky [25]. These works concern extremizers and optimal constants for the Strichartz inequality for the homogeneous Schr¨dinger equation in the lower dimensional cases. These are the cases for which the Strichartz exponent is an even integer, and one can rewrite the left-hand side of the Strichartz inequality as an L2-norm, and invoke Plancherel’s Theorem in order to reduce the problem to a multilinear convolution estimate. This subject is becoming increasingly more popular, as shown by the large body of work that appeared in the last decade, and in particular in the last few years. We mention a few interesting works that deal with sharp Fourier restriction theory on spheres [11, 12, 14, 15, 20, 22, 39], paraboloids [2, 10, 13, 23, 37], and cones [6, 7, 34, 36]. Perturbations of these manifolds have been considered in [17, 27, 30, 31, 32]. Sharp bilinear Fourier restriction theory is the subject of [4, 5, 26, 33], whereas other instances of sharp Strichartz inequalities [3], sharp Sobolev–Strichartz inequalities [18] and sharp Airy–Strichartz inequalities [24, 38] have been considered as well. Finally, we mention a recent survey [21] on sharp Fourier restriction theory which may be consulted for information complementary to that on this Introduction, including a discussion on delta calculus, and further references.

Structure of the paper. The paper is organized as follows. In §2 we discuss Lorentz transformations and their relevance to the problem. In particular, we decompose the hyperboloid as a disjoint union of caps, and study how these interact with certain Lorentz transformations. In §3 we study properties of the n-fold convolution of the measure σ with itself, explicitly computing some particular instances. In §4 we prove Theorem 1. The ﬁrst step is to exhibit an explicit extremizing sequence. Once this is done, we appeal to geometric properties of the convolution measure to guarantee that extremizers do not exist. Finally, §5 and §6 are devoted to the proof of Theorem 2. In §5 we proceed with a detailed construction of a special cap which contains a non-negligible universal amount of the total mass in an extremizing sequence (properly symmetrized). Once a special cap is available, in §6 we feed this information into the concentration-compactness machinery of Fanelli– Vega–Visciglia [17, 18] to ensure that extremizers exist. It is interesting to note that this latter part of the argument works in all dimensions.

A word on forthcoming notation. If x,y are real numbers, we will write x = O(y) or x y if there exists a ﬁnite constant C such that |x| ≤ C|y|, and x y if C−1|y| ≤ |x| ≤ C|y| for some ﬁnite constant C = 0. If we want to make explicit the dependence of the constant C on some parameter α, we will write x = Oα(y) or x α y. As is customary, the constant C is allowed to change from line to line. The set of natural numbers is N := {1,2,3,...}. Real and imaginary parts of a complex number z ∈ C will be denoted by (z) and (z), respectively. The usual inner product between vectors x,y ∈ Rd will continue to be denoted by x·y, and we deﬁne x := 1 + |x|2. Given a ﬁnite set A, we will denote its cardinality by |A|. Finally, E will stand for the indicator function of a given set E.

2. Lorentz invariance

The measure σ deﬁned in (1.1) has been referred to as the Lorentz invariant measure on the hyperboloid. This section is meant to explain and expand on this terminology. The Lorentz group, denoted by L, is deﬁned as the group of invertible linear transformations in Rd+1 that preserve the bilinear form

B(x,y) = xd+1yd+1 − xdyd − ... − x1y1. In particular, if L ∈ L, we have |detL| = 1. We denote the subgroup of L that preserves the hyperboloid Hd by L+. The measure σ is likewise preserved under the action of L+, in the sense that

f ◦ L dσ =

f dσ, for every f ∈ L1(Hd) and L ∈ L+. This can be readily seen by writing

Hd

Hd

dσ(y,y ) = 2δ y 2 − |y|2 − 1 {y >0}(y,y )dy dy . Now, given t ∈ (−1,1), deﬁne the linear map Lt : Rd+1 → Rd+1 via Lt(ξ1,...,ξd,τ) =

ξ1 + tτ √1 − t2

τ + tξ1 √1 − t2

,ξ2,...,ξd,

.

The family {Lt}t∈(−1,1) deﬁnes a one-parameter subgroup of L+. In particular, the inverse of Lt is L−t. Further notice that, given an orthogonal matrix A ∈ O(d), the transformation (ξ,τ)  → ρA(ξ,τ) = (Aξ,τ) belongs to L+.

As already observed in [35, §3], given (ξ,τ) ∈ Rd+1 satisfying τ > |ξ|, a suitable composition of transformations of the form Lt and ρA as deﬁned above produces a map L ∈ L+, such that

L(ξ,τ) = (0, τ2 − |ξ|2).

This observation will simplify several computations involving convolutions of the measure σ with itself, which we explore in the next section. Given p ∈ [1,∞], L ∈ L+ and f ∈ Lp(Hd), deﬁne the composition L∗f = f ◦ L. The considerations made so far imply that

L∗f Lp(Hd) = f Lp(Hd), and T(L∗f) Lp(Rd+1) = Tf Lp(Rd+1). (2.1)

In particular, if {fn}n∈N is an extremizing sequence for inequality (1.4) and {Ln}n∈N ⊂ L+, then {L∗nfn}n∈N is still an extremizing sequence for inequality (1.4).

The Lorentz invariance just discussed will be crucial in several of our arguments, as it allows to localize the action to a ﬁxed bounded region. We now detail this principle in the lower dimensional setting d ∈ {1,2}.

- 2.1. One-dimensional tessellations. Let us deﬁne a one-dimensional cap to be a set of the form Ck := {(ξ,τ) ∈ H1 : sinh(k − 1/2) ≤ ξ < sinh(k + 1/2)}


(2.2)

= {(sinh(u),cosh(u)) ∈ R2 : k − 1/2 ≤ u < k + 1/2},

for some k ∈ Z. The following simple result already illustrates the main point.

- Lemma 3. Let k ∈ Z, and let Ck ⊂ H1 be the corresponding one-dimensional cap. Then:


- (a) σ(Ck) = 1.
- (b) There exists tk ∈ (−1,1), such that Lt


(Ck) = C0. Proof. The proof of part (a) amounts to a straightforward change of variables: σ(Ck) =

k

sinh(k+ 21 )

k+ 12

dy 1 + y2

cosh(u)du 1 + sinh(u)2

=

= 1.

sinh(k− 12 )

k− 12

For part (b), let tk = −tanh(k) ∈ (−1,1). Then the Lorentz transformation Lt

### provides a bijection between the caps Ck and C0. That Lt

k

### (Ck) = C0 follows from

k

 

 

sinh(u) + cosh(sinh(kk)) cosh(u) 1 − sinh

cosh(u) + cosh(sinh(kk)) sinh(u) 1 − sinh

L−t

(sinh(u),cosh(u)) =

,

k

2(k) cosh2(k)

2(k) cosh2(k)

= (sinh(u + k),cosh(u + k)). This concludes the proof of the lemma.

![image 1](<2017-carneiro-extremizers-fourier-restriction-hyperboloids_images/imageFile1.png>)

Figure 2. The one-dimensional cap movement: a carefully chosen Lorentz transformation interchanges the caps. Here, Lt(C−2) = C0 for t = tanh(2).

2.2. Two-dimensional tessellations. We now deﬁne a two-dimensional cap to be a set of the form

2π(j + 1) 2n

2πj 2n ≤ θ <

Cn,j := (r cosθ,r sinθ, r ) ∈ H2 : 2n ≤ r < 2n+1 and

, (2.3) for some n ∈ N and 0 ≤ j < 2n, and additionally we consider

C0,0 := {(ξ,τ) ∈ H2 : |ξ| < 2}. (2.4)

Grouping together the caps of the n-th generation, we notice that the hyperboloid H2 is partitioned into a disjoint union of annuli,

∞

H2 =

An, where An :=

n=0

2n−1

Cn,j. (2.5)

j=0

See Figure 3 for an illustration of these decompositions. Given ϕ ∈ [0,2π), denote by Rϕ the rotation in R3 by angle ϕ around the vertical τ−axis:

Rϕ(ξ1,ξ2,τ) = (ξ1 cosϕ + ξ2 sinϕ,−ξ1 sinϕ + ξ2 cosϕ,τ).

The next result is the two-dimensional equivalent of Lemma 3, and in particular shows that any cap can be mapped into the ball of radius 2√2π centered at the origin by an appropriate composition of Lorentz transformations. See Figure 4 for an illustration of these movements.

- Lemma 4. Let n ∈ N0 and 0 ≤ j < 2n, and let Cn,j ⊂ H2 be the corresponding two-dimensional cap. Then:


- (a) σ(Cn,j) 1.
- (b) There exists t ∈ [0,1) and ϕ ∈ [0,2π), such that


√

(L−t ◦ Rϕ)(Cn,j) ⊆ {(ξ,τ) ∈ H2 : |ξ| ≤ 2

2π}.

Figure 3. Projection of the tessellation of H2 into caps {Cn,j} onto the horizontal plane τ = 0.

Proof. Let n ∈ N and 0 ≤ j < 2n. A computation in polar coordinates shows that

2π(j+1) 2n

2n+1

√1 + 4n ,

rdr √1 + r2

2π 2n

1 + 4n+1 −

σ(Cn,j) =

dθ

=

2πj 2n

2n

from which one easily checks that

σ(Cn,j)

- 9

- 10 ≤


2π ≤ 1. Moreover, σ(C0,0) = 2π(√5 − 1), and so one sees that the σ-measure of any two-dimensional cap is comparable to 1. This establishes part (a).

For part (b), we lose no generality in assuming n ≥ 3, for otherwise we can simply take t = ϕ = 0. Given such n, and 0 ≤ j < 2n, choose ϕ ∈ [0,2π) so that

π 2n

Rϕ(Cn,j) ⊆ (r cosθ,r sinθ, r ) ∈ H2 : 2n ≤ r < 2n+1 and |θ| ≤

.

Let t := 1 − (2πn)2, which is nonnegative since n ≥ 3. Noting that (L−t ◦ Rϕ)(Cn,j) ⊆

r cosθ − t r √1 − t2

r − tr cosθ √1 − t2 ∈ H2 : 2n ≤ r < 2n+1 and |θ| ≤

π 2n

, it suﬃces to check that

,r sinθ,

r cosθ − t r

√1 − t2 ≤ 2π, and |r sinθ| ≤ 2π. Observe that r ≤ r and cosθ ≥ cos(2πn) ≥ 1 − 21(2πn)2 > t. We ﬁrst claim that r cosθ − t r ≥ 0. In fact, using the fact that 1 + x2 ≥

√1 + x, we have cosθ

1 − 12(2πn)2 1 − (2πn)2 ≥ 1 +

1 22n+1 ≥ 1 +

1 22n ≥ 1 +

1 r2

r r

t ≥

=

.

Figure 4. Projection of the two-dimensional cap movement: a rotation followed by a Lorentz transformation moves the cap inside the set {(ξ,τ) ∈ H2 : |ξ| ≤ 2√2π}.

Therefore it follows that r cosθ − t r √1 − t2 ≤

r(cosθ − t) √1 − t2 ≤

r(1 − t) √1 − t2

Noting that sin(xx) ≤ 1, we similarly have that |r sinθ| < 2n+1 sin

π 2n

This concludes the proof of the lemma.

= r

1 − t 1 + t ≤ r√1 − t < 2n+1

π 2n

= 2π.

sin(2πn) π 2n

≤ 2π.

= 2π

3. Convolutions

In this section, we collect some facts about convolution measures that will be relevant in the sequel. We start with some general considerations which hold in arbitrary dimensions d ≥ 1. Let σ(∗n) = σ ∗ ... ∗ σ denote the n-fold convolution of the Lorentz invariant measure σ deﬁned in (1.1) with itself. If n ≥ 2, then the convolution measure σ(∗n) is absolutely continuous with respect to Lebesgue measure on Rd+1, and it is supported in the closure of the region

Pd,n := {(ξ,τ) ∈ Rd × R : τ > n2 + |ξ|2}. (3.1) The Lorentz invariance discussed in the previous section implies that σ(∗n) is constant along certain hyperboloids. More precisely, if (ξ,τ) ∈ Pd,n, then

σ(∗n)(ξ,τ) = σ(∗n)(0, τ2 − |ξ|2). (3.2)

The next result establishes some basic convolution properties on the one-dimensional hyperbola (H1,σ).

- Lemma 5. Let σ denote the Lorentz invariant measure on the hyperbola H1. Then, for every (ξ,τ) ∈ R × R,


- (a) The convolution measure σ ∗ σ is given by

(σ ∗ σ)(ξ,τ) =

4 τ2 − ξ2 τ2 − ξ2 − 4 {τ≥

√

22+ξ2}(ξ,τ).

- (b) The following recursive formula holds for n ≥ 2:


√

τ2−ξ2−1

x σ(∗n)(0,x) ( τ2 − ξ2 + 1)2 − x2)21 ( τ2 − ξ2 − 1)2 − x2)21

σ(∗(n+1))(ξ,τ) = 4

dx.

n

Proof. We start with part (a). By the Lorentz invariance (3.2), it suﬃces to prove that (σ ∗ σ)(0,τ) =

4 τ√τ2 − 4 {τ≥2}

(τ). (3.3) This can be obtained as follows: ﬁrst of all,

∞

dy y 2

dy y 2

(σ ∗ σ)(0,τ) =

δ τ − 2 y

= 2

.

δ τ − 2 y

R

0

- Changing variables u = y , and then v = 2u, we have that


δ τ − v v√v2 − 4

∞

∞

1 u2

u √u2 − 1

(σ ∗ σ)(0,τ) = 2

dv. This implies (3.3) at once, and ﬁnishes the proof of part (a).

δ τ − 2u

du = 4

1

2

We now turn to the proof of part (b). Again by Lorentz invariance, it suﬃces to establish

τ−1

x σ(∗n)(0,x) (τ + 1)2 − x2 (τ − 1)2 − x2

σ(∗(n+1))(0,τ) = 4

dx. (3.4)

n

We proceed by induction on n. Since σ(∗n) is a function by hypothesis, the (n + 1)-fold convolution can be obtained by convolving that function with the measure σ, as follows:

σ(∗(n+1))(0,τ) =

=

= 2

σ(∗n)((0,τ) − (y,y ))dσ(y,y )

H1

dy y

σ(∗n)(−y,τ − y )

R

∞

dy y

σ(∗n)(0, τ2 − 2τ y + 1)

,

0

where the Lorentz invariance (3.2) was again used in the last identity. Changing variables u = y as before, we have that:

σ(∗n)(0,√τ2 − 2τu + 1) √u2 − 1

τ2+1−n2 2τ

σ(∗(n+1))(0,τ) = 2

du,

1

where the upper limit in the region of integration is due to support considerations involving (3.1).

- Changing variables v = τ2 − 2τu + 1, we continue to compute:


σ(∗n)(0,√v) (τ2 − v + 1)2 − (2τ)2

(τ−1)2

σ(∗(n+1))(0,τ) = 2

dv.

n2

A ﬁnal change of variables x = √v yields the desired formula (3.4). This ﬁnishes the proof.

Identities (3.3) and (3.4) for n = 2 imply the following integral formula for the 3-fold convolution measure which should be compared to [11, Lemma 8]: If τ > 3, then

τ−1

1 (τ + 1)2 − x2 (τ − 1)2 − x2

dx √x2 − 4

σ(∗3)(0,τ) = 16

. (3.5)

2

This integral representation is amenable to a robust numerical treatment with Mathematica, see Figure 5 below. It is also the starting point for the study of the basic properties of the convolution measure σ(∗3), which are summarized in the following result.

- Lemma 6. Let σ denote the Lorentz invariant measure on the hyperbola H1. Then the function τ  → σ(∗3)(0,τ) is continuous on the half-line τ > 3. It extends continuously to the boundary of its support, in such a way that


2π √3

σ(∗3)(0,τ) = σ(∗3)(0,3) =

, (3.6) and this global maximum is strict, i.e.

sup

τ>3

2π √3

σ(∗3)(0,τ) <

, for every τ > 3. (3.7) In particular, this implies that

1

- 1

- 2 . (3.8)


H1,6 ≤ 3−

12(2π)

Proof. An application of Lebesgue’s Dominated Convergence Theorem to the integral (3.5) establishes that the function τ  → σ(∗3)(0,τ) is continuous for τ > 3. We can appeal to the same formula to crudely estimate:

σ(∗3)(0,τ) ≥ L(τ), for every τ > 3, (3.9) where L denotes the lower bound

16 I(τ) (τ + 1)2 − 22 (τ − 1) + (τ − 1) (τ − 1) + 2

,

L(τ) :=

and I(τ) denotes the integral

τ−1

dx √x − 2

1 (τ − 1) − x

.

I(τ) :=

2

Via the aﬃne change of variables x  → (τ−3)x+2, we see that I(τ) = π, for every τ > 3. Substituting in (3.9), we have that

2π √3

σ(∗3)(0,τ) ≥

liminf

. (3.10)

τ→3+

- 1

- 2

- 3


4 5 6 7 8 9 10

Figure 5. The lower bound L(τ) and the upper bound U(τ) for the function τ  → σ(∗3)(0,τ) on the half-line τ > 3.

Crude upper bounds of similar ﬂavor yield

σ(∗3)(0,τ) ≤ U(τ), for every τ > 3, (3.11) where the upper bound U is given by

16π (τ + 1)2 − (τ − 1)2 (τ − 1) + 2√2 + 2

U(τ) :=

.

Incidentally, note that this implies σ(∗3)(0,τ) τ−1, for large values of τ. It follows from (3.11) that

2π √3

σ(∗3)(0,τ) ≤

. (3.12) Estimates (3.10) and (3.12) together imply

limsup

τ→3+

2π √3

σ(∗3)(0,τ) =

.

lim

τ→3+

Noting that the upper bound U satisﬁes U(3) = √2π3, and that U (τ) = −

2π(2τ + 1) τ 32 (τ + 1)23

< 0 for every τ > 3,

we arrive at (3.7). Finally, letting δ2 denote the two-dimensional Dirac delta, we have

fσ ∗ fσ ∗ fσ 2L2(R2) =

f(x1)f(x2)f(x3)f(x4)f(x5)f(x6)dΣ,

(R2)6

where dΣ = dΣ(x1,...,x6) = δ2(x1 + x2 + x3 − x4 − x5 − x6)dσ(x1)...dσ(x6). An application of the Cauchy–Schwarz inequality leads to

fσ ∗ fσ ∗ fσ 2L2(R2) ≤

|f(x1)|2 |f(x2)|2 |f(x3)|2 dΣ

(R2)6

|f(x1)|2 |f(x2)|2 |f(x3)|2 σ(∗3)(x1 + x2 + x3)dσ(x1)dσ(x2)dσ(x3) ≤ sup

(3.13)

=

(R2)3

σ(∗3)(x) f 6L2(H1).

x∈R2

Estimate (3.8) now follows from (1.6), (3.6) and (3.13). This completes the proof of the lemma.

Two-dimensional counterparts of the results from this section were obtained in [35, Lemma 5.1]. We record them here.

- Lemma 7 (cf. [35]). Let σ denote the Lorentz invariant measure on the hyperboloid H2. Then, for every (ξ,τ) ∈ R2 × R,


- (a) (σ ∗ σ)(ξ,τ) = √ 2π τ2−|ξ|2 {τ≥

√

22+|ξ|2}(ξ,τ),

- (b) (σ ∗ σ ∗ σ)(ξ,τ) = (2π)2 1 − √ 3 τ2−|ξ|2 {τ≥


√

32+|ξ|2}(ξ,τ).

4. Nonexistence of extremizers at the endpoint (d,p) = (1,6)

This section is devoted to the proof of Theorem 1. After studying the behavior of σ(∗3) in §3, the material in this section is partly motivated by the outline of [35, Appendices B and C]. The heart of the matter lies in the construction of an explicit extremizing sequence for inequality (1.4), which is the content of the next result.

Proposition 8. Let σ denote the Lorentz invariant measure on the hyperbola H1. Given a > 0, let fa(y) = e−a y , y ∈ R. Then:

- (a) For every n ∈ N we have (faσ)(∗n)(ξ,τ) = e−aτσ(∗n)(ξ,τ).
- (b) The function a  →

√ae2a fa 2L2(H1) is bounded on the half-line a > 0, and satisﬁes

lim

a→∞

√ae2a fa 2L2(H1) = √π. (4.1)

- (c) The sequence {fa}a∈N satisﬁes


faσ ∗ faσ ∗ faσ 2L2(R2) fa 6L2(H1)

2π √3

lim

, (4.2)

=

a→∞

and is extremizing for inequality (1.4) when (d,p) = (1,6), as a → ∞. In particular,

1

- 1

- 2 .


H1,6 = 3−

12(2π)

### Proof. The proof of (a) is analogous to part of the proof of [35, Lemma B.1]. We present the details for the convenience of the reader. Letting ga(ξ,τ) = e−aτ, we have that (faσ)(∗n) = (gaσ)(∗n).

Therefore,

(faσ)(∗n)(ξ,τ) = (gaσ)(∗n)(ξ,τ) = ga(ξ,τ)σ(∗n)(ξ,τ) = e−aτσ(∗n)(ξ,τ), where the second identity follows from the fact that ga is the exponential of a linear function. For part (b), change variables y = cosht to compute fa 2L2(H1) =

∞

dy y

e−2a y

e−2acoshtdt = 2K0(2a). (4.3) Here, the modiﬁed Bessel function of the second kind Kν is given for (z) > 0 by

= 2

R

0

∞

exp(−z cosht)cosh(νt)dt. Claim (4.1) boils down to the well-known fact

Kν(z) =

0

√π 2

√ae2aK0(2a) =

lim

, (4.4)

a→∞

see e.g. [41, §7.34 (1)]. We ﬁnish the proof of part (b) by invoking the facts that K0(x) |log(x)| as x → 0+ (see e.g. [1, formula (9.6.8) on p. 375]), and that K0 monotonically decreases on the positive half-axis, which follows directly from the deﬁnition of K0. Figure 6 illustrates these facts.

We next turn to part (c). Part (a) implies

e−2aτ(σ(∗3)(ξ,τ))2 dξ dτ,

faσ ∗ faσ ∗ faσ 2L2(R2) =

P1,3

where the support region P1,3 was deﬁned in (3.1). We perform the change of variables φ(ξ,τ) = (ξ, τ2 + ξ2), which has Jacobian determinant

 

  =

1 √ ξ

τ τ2 + ξ2

τ2+ξ2 0 √ τ

J(φ)(ξ,τ) = det

.

τ2+ξ2

As a consequence,

√

2 τ τ2 + ξ2

τ2+ξ2 σ(∗3) ξ, τ2 + ξ2

e−2a

faσ ∗ faσ ∗ faσ 2L2(R2) =

dξ dτ

φ−1(P1,3)

√

∞

τ2+ξ2 τ2 + ξ2

e−2a

τ σ(∗3)(0,τ) 2

=

dξ dτ, (4.5)

R

3

where in the last identity we used the Lorentz invariance (3.2) of the convolution σ(∗3), together with the fact that φ−1(P1,3) = R × (3,∞). Deﬁne H(a) := fa 2L2(H1). Recognizing the inner integral in (4.5) as the quantity H(aτ), we have that

faσ ∗ faσ ∗ faσ 2L2(R2) fa 6L2(H1)

∞

H(aτ) H(a)3

τ(σ(∗3)(0,τ))2

dτ. (4.6)

=

3

We will be interested in the regime where a → ∞, for which the approximation

e−2a(τ−3) √τ

a π

H(aτ) H(a)3

lim

= 1 (4.7)

a→∞

1.0

0.8

0.6

0.4

0.2

0 1 2 3 4 5 6

1.0

0.8

0.6

0.4

0.2

0 1 2 3 4 5 6

√xe2xK0(2x) together with its horizontal asymptote y =

Figure 6. The function x  → K0(x), and the function x  →

√π

2 .

follows from (4.3) and (4.4). On the other hand, we have noted in the course of the proof of Lemma 6 that

1 τ

σ(∗3)(0,τ)

, for τ > 3. From this and support considerations, it follows that the function τ  →

√τ(σ(∗3)(0,τ))2 is bounded on the positive half-axis. It is also continuous there, except for a jump discontinuity at τ = 3. Given an even function ϕ : R → [0,∞) satisfying R ϕ = 1, we have

√

(σ(∗3)(0,3−))2 + (σ(∗3)(0,3+))2 2

|τ|(σ(∗3)(0,τ))2 aϕ(a(τ − 3))dτ =

3

lim

a→∞ R

02 + (√2π3)2 2

√

2π2 √3

=

3

=

.

This follows from the fact that {aϕ(a ·)}a∈N constitutes an approximate identity sequence, as a → ∞. Specializing to ϕ(t) = e−2|t|, and using (4.6) and (4.7), we check that (4.2) holds. From (1.6) and (3.8) it follows that the sequence {fa}a∈N is extremizing for inequality (1.4), and

1

- 1

- 2 .


H1,6 = 3−

12(2π) This completes the proof of the proposition (and of part of Theorem 1).

To prove that extremizers do not exist, we invoke the useful observation from [35, Corollary 4.3], which we record here.

- Lemma 9 (cf. [35]). Let (d,p) satisfy (1.5), and suppose that p = 2n is an even integer. Suppose that


1 p

d+1

p σ(∗n)

Hd,p = (2π)

L∞(Rd+1),

and that σ(∗n)(ξ,τ) < σ(∗n) L∞(Rd+1) for a.e. (ξ,τ) in the support of σ(∗n). Then extremizers for inequality (1.4) do not exist for the pair (d,p).

Armed with Lemma 6, Proposition 8 (c) and Lemma 9, it is now an easy matter to ﬁnish the proof of Theorem 1.

We end this section with the following remark. The extremizing sequence {fa}a∈N deﬁned in the statement of Proposition 8 concentrates at the vertex of the hyperbola. It is sensible to ask about the behaviour of general extremizing sequences. Following the arguments from [35, §6] or [32, Theorem 1.5], one can show that every extremizing sequence for inequality (1.4) when (d,p) = (1,6) concentrates at the vertex of the hyperbola, possibly after applying the symmetries of the problem and after extracting a subsequence. We omit the details.

5. Special cap

In this section, we seek to locate a distinguished cap which carries a non-trivial amount of L2 mass. This is essential to start gaining some control on compactness properties of extremizing sequences. In the one-dimensional situation, we establish a reﬁnement of the Fourier extension inequality. In the two-dimensional setting, we reduce matters to the study of bilinear interactions in the lower endpoint case.

- 5.1. One-dimensional setting. This subsection in partially inspired by [34, §3] (see also [28, §4]).


To study the interaction between the distinct caps from the family {Ck}k∈Z, deﬁned in (2.2), we make use of the following standard result on fractional integration.

- Lemma 10 (Hardy–Littlewood–Sobolev). Given r,s ∈ (1,∞) with 1r + 1s > 1, let α = 2 − 1r − 1s. For any f ∈ Lr(R) and g ∈ Ls(R),

∞

−∞

∞

−∞

|f(x)||x − y|−α|g(y)|dxdy r,s f Lr(R) g Ls(R).

The following result shows that distant caps interact weakly.

- Lemma 11. Let 2 < q < ∞. For any k,  ∈ Z, if supp(f) ⊂ Ck and supp(g) ⊂ C , then


|k− |

Tf · Tg Lq(R2) q e−

2q f

g

.

2q

2q

2q−3 (H1)

2q−3 (H1)

L

L

Proof. Deﬁne the auxiliary function h(ξ1,ξ2) := (f(ξ1)g(ξ2) + f(ξ2)g(ξ1)) {ξ

1≥ξ2}(ξ1,ξ2), for which

dξ2 ξ2

dξ1 ξ1

eix(ξ

1+ξ2)eit( ξ

1 + ξ2 )h(ξ1,ξ2)

(Tf · Tg)(x,t) =

. Following an argument that goes back to early work of Carleson–Sj¨lin [9], we change variables (ξ1,ξ2)  → (u,v) = (ξ1 + ξ2, ξ1 + ξ2 )

R2

in the region of integration {(ξ1,ξ2) ∈ R2 : ξ1 ≥ ξ2}. Note that this is a bijective map onto the region {(u,v) ∈ R × R+ : v2 − u2 ≥ 4}. It follows that

h(ξ1,ξ2) J(ξ1,ξ2)

du ξ1

dv ξ2

ei(x,t)·(u,v)

(Tf · Tg)(x,t) =

,

R2

where J denotes the Jacobian of this transformation, given by

J(ξ1,ξ2) =

∂(u,v) ∂(ξ1,ξ2)

=

ξ1 ξ1 −

ξ2 ξ2

.

The Hausdorﬀ–Young inequality on R2 implies that, for every q ≥ 2,

q q−1

h(ξ1,ξ2) J(ξ1,ξ2)

1 ξ1 ξ2

Tf · Tg Lq(R2) ≤

dudv

R2

q−1 q

.

Changing back to the original variables (ξ1,ξ2), we obtain

Tf · Tg Lq(R2) ≤

q q−1

|h(ξ1,ξ2)|

dξ1 ξ1

dξ2 ξ2

1 q−1

(J(ξ1,ξ2) ξ1 ξ2 )

R2

q−1 q

.

In order to invoke Lemma 10, it is convenient to perform another change of variables (ξ1,ξ2) = (sinh(θ1),sinh(θ2)). Noting that

J(ξ1,ξ2) ξ1 ξ2 = |sinh(θ1 − θ2)|, Minkowski’s inequality yields

q−1 q

q q−1

|h(sinh(θ1),sinh(θ2))|

Tf · Tg Lq(R2) ≤

dθ1 dθ2

1 q−1

|sinh(θ1 − θ2)|

R2

(5.1)

q−1 q

q q−1

|f(sinh(θ1))g(sinh(θ2))|

dθ1 dθ2

.

1 q−1

|sinh(θ1 − θ2)|

R2

We now use the lower bound

exp |θ| 2

|θ| 2

|sinh(θ)| ≥

,

which is valid for any θ ∈ R, together with Lemma 10 with the choices α = q−11 and r = s = 22qq−−23 (which are admissible since 2 < q < ∞). From (5.1) we get

q−1 q

q q−1

|f(sinh(θ1))g(sinh(θ2))|

Tf · Tg Lq(R2)

dθ1 dθ2

|θ1−θ2| 2(q−1)

1

R2

|θ1 − θ2|

q−1 e

|k− |

q e−

2q f

g

,

2q

2q

2q−3 (H1)

2q−3 (H1)

L

L

where we have used that |(θ1 −θ2)−(k − )| ≤ 1, since |θ1 −k| ≤ 12 and |θ2 − | ≤ 12. This completes the proof of the lemma.

Lemma 11 is the key ingredient in order to establish the following reﬁnement of the inequality

(1.4) in the case d = 1. In what follows, given f ∈ L2(H1), we shall decompose f = k∈Z fk with fk := f C

### .

k

### Proposition 12. Let 3 ≤ q < ∞. For any f ∈ L2(H1) we have

Tf L2q(R2) q

k∈Z

fk 3 L

2q

2q−3 (H1)

1 3

. (5.2)

When 3 ≤ q ≤ ∞, note that 1 ≤ 2q2−q3 ≤ 2. In this case, the estimates

Tf L6(R2) f L2(H1), and Tf L∞(R2) ≤ f L1(H1) can be interpolated to yield

Tf L2q(R2) q f

. (5.3)

2q

2q−3 (H1)

L

Proof of Proposition 12. Writing

(Tf)3 =

Tfk · Tf · Tfm,

k, ,m∈Z

Minkowski’s triangle inequality plainly implies that Tf 3L2q(R2) = (Tf)3

≤

Tfk · Tf · Tfm

. (5.4)

2q

2q

3 (R2)

3 (R2)

L

L

k, ,m∈Z

Given a triplet (k, ,m) ∈ Z3, we lose no generality in assuming that |k − | = max{|k − |,| − m|,|m − k|}.

H¨lder’s inequality, Lemma 11 (recall that q < ∞) and estimate (5.3), together with the maximality of |k − |, imply

Tfk · Tf · Tfm

≤ Tfk · Tf Lq(R2) Tfm L2q(R2) q e−

2q

3 (R2)

L

|k− |

2q fk

f

fm

(5.5)

2q

2q

2q

2q−3 (H1) ≤ e−

2q−3 (H1)

2q−3 (H1)

L

L

L

|k− |

| −m|

|m−k|

6q e−

6q e−

6q fk

f

fm

.

2q

2q

2q

2q−3 (H1)

2q−3 (H1)

2q−3 (H1)

L

L

L

Putting together (5.4) and (5.5), we conclude that

|k− |

| −m|

|m−k|

e−

6q e−

6q e−

Tf 3L2q(R2) q

6q fk

f

fm

.

2q

2q

2q

2q−3 (H1)

2q−3 (H1)

2q−3 (H1)

L

L

L

k, ,m∈Z

|k− |

| −m|

|m−k|

e−

6q e−

6q e−

6q fk 3 L

≤

,

2q

2q−3 (H1)

k, ,m∈Z

where the last line follows from the inequality between the arithmetic and the geometric means. Summing two geometric series, we ﬁnally have that

fk 3 L

Tf 3L2q(R2) q

k∈Z

as desired. This completes the proof of the proposition.

,

2q

2q−3 (H1)

We have the following immediate but useful consequence.

Corollary 13. Let 6 ≤ p < ∞. Then there exists Cp < ∞ such that, for any f ∈ L2(H1),

1 3

- 2

- 3


Tf Lp(R2) ≤ Cp sup k∈Z

fk

L2(H1) f

L2(H1). (5.6)

Proof. Using estimate (5.2) with p = 2q we get

1 3

1 3

fk 2 L

Tf Lp(R2) ≤ Cp sup k∈Z

fk

, (5.7)

p

p

p−3 (H1)

p−3 (H1)

L

k∈Z

for some constant Cp < ∞. Applying H¨lder’s inequality, and recalling that σ(Ck) = 1, fk

≤ Ck L

fk L2(H1) = fk L2(H1).

p

2p

p−3 (H1)

p−6 (H1)

L

Plugging this into the right-hand side of (5.7), and appealing to the disjointness of the supports of the {fk}, yields the desired conclusion.

- Proposition 14. Let d = 1 and 6 ≤ p < ∞. Let {fn}n∈N ⊂ L2(H1) be an extremizing sequence


- for inequality (1.4), normalized so that fn L2(H1) = 1 for each n ∈ N. There exists a universal


- constant η1,p > 0 and n0 ∈ N, such that for any n ≥ n0 there exists sn ∈ (−1,1) verifying


- 1

- 2


)∗fn L2(Ck) ≥ η1,p.

)∗fn L2(C0) ≥

(Ls

(Ls

sup

n

n

k∈Z

Proof. Let n0 ∈ N be such that, for n ≥ n0, we have Tfn Lp(R2) ≥

H1,p 2

. (5.8) Fix n ≥ n0. Using (5.8) and the cap bound (5.6), we have that

3

H1,p 2Cp

fn,k L2(H1) ≥

sup

,

k∈Z

### , and Cp is the constant from inequality (5.6). Let k(n) ∈ Z be such that

where fn,k := fn C

k

3

H1,p 2Cp

- 1

- 2


fn,k(n) L2(H1) ≥ η1,p :=

.

Choose sn := tanh(k(n)). Since Ls

### (C0) = Ck(n) (recall Lemma 3 (b)), we then have by (2.1) that supp (Ls

n

)∗fn,k(n) L2(H1) ≥ η1,p. This concludes the proof of the proposition.

### )∗fn,k(n) ⊆ C0, and (Ls

n

n

- 5.2. Two-dimensional setting. In order to study the interaction between the distinct caps from


the family {Cn,j} deﬁned in (2.3) and (2.4), we try to relate the non-endpoint problem to the lower endpoint problem. Log-convexity of Lebesgue norms readily implies the following: given p ∈ (4,6), there exists θ ∈ (0,1) such that

Tf Lp(R3) ≤ Tf θL4(R3) Tf 1L−6(θR3). (5.9)

In particular, if {fn}n∈N is an extremizing sequence for inequality (1.4) when d = 2 and p ∈ (4,6), normalized so that fn L2(H2) = 1 for each n ∈ N, then both quantities on the right-hand side of inequality (5.9) cannot be too small, in the sense that there exists a universal constant γp > 0, depending on p but not on n, and n0 ∈ N such that

min{ Tfn L4(R3), Tfn L6(R3)} ≥ γp, for any n ≥ n0.

The idea will be to exploit the convolution structure of the lower endpoint problem (d,p) = (2,4) to derive some nontrivial information about the non-endpoint case. The crux of the matter lies in the following result.

- Proposition 15. Let f ∈ L2(H2), normalized so that f L2(H2) = 1. Let ε > 0 and assume that


f L2(Cn,j) ≤ ε, where the supremum is taken over all n ∈ N ∪ {0} and 0 ≤ j < 2n. Then Tf 4L4(R3) εlog2(ε−1). (5.10)

sup

n,j

Remark: The relevant feature of the function Φ(ε) = εlog2(ε−1) is that Φ(ε) → 0, as ε → 0+. Any other Φ with the same property would serve our purpose equally well.

Proof. Recalling (1.3), the usual application of Plancherel’s Theorem and the Cauchy–Schwarz inequality (the latter as in (3.13)) yields

dξ ξ

dη η

Tf 4L4(R3) fσ ∗ fσ 2L2(R3) ≤

|f(ξ)|2|f(η)|2(σ ∗ σ)(ξ + η, ξ + η )

.

R2×R2

Abusing notation slightly, and still denoting by {Cn,j} the projection of the caps deﬁned in (2.3) and (2.4) onto the ξ-plane, we have that

Tf 4L4(R3)

dξ ξ

|f(ξ)|2|f(η)|2(σ ∗ σ)(ξ + η, ξ + η )

(m, ),(n,j) Cm,  Cn,j

dη η

. (5.11)

Here, the sum is taken over all pairs (m, ),(n,j) with 0 ≤ n ≤ m, and 0 ≤ < 2m, 0 ≤ j < 2n. We seek to obtain some control over the height s, deﬁned via the equation

s2 := ( ξ + η )2 − |ξ + η|2 = 2(1 + ξ η − ξ · η). (5.12)

With this purpose in mind, we split the sum in (5.11) into two pieces, depending on whether or not the direction of the caps is approximately the same. In the former case, the bound will be in terms of the distance between the centers of the caps, whereas in the latter case one obtains an improved bound in terms of the angular separation between the caps. See Figure 7 for an illustration of two extreme cases of this separation.

Let S ⊂ R. In what follows, we say that x ∈ S mod1 if x + k ∈ S for some k ∈ Z. Analogously, for m ∈ N ∪ {0}, we say that x ∈ S mod2m if x + k2m ∈ S for some k ∈ Z. We also deﬁne

x := min{|x − k| : k ∈ Z} (5.13)

for the distance of x to the nearest integer.

- Case 1. 2m − 2jn ∈ −22n, 22n mod1. In this case, we are considering indices belonging to A(m,nj) := 0 ≤ < 2m : ∈ 2m−n(j − 2),2m−n(j + 2) mod2m ,


a set of cardinality A(m,nj) = 2m−n+2. We seek to estimate the sum

dξ ξ

dη η

|f(ξ)|2|f(η)|2(σ ∗ σ)(ξ + η, ξ + η )

S1 :=

.

n≥0 m≥n 0≤j<2n ∈A(m,nj) Cm,  Cn,j

Note that x  → x |x|−1 is a decreasing function of |x|. For ξ ∈ Cn,j and η ∈ Cm, , we can estimate the height s deﬁned in (5.12) from below, as follows:

2n+1 2m+1

ξ η |ξ||η|

- 1 4

- 2n+1 2m+1


s2 ξ η − ξ · η ≥ |ξ||η|

2n+12m+1 − 1 . Writing 2n+1 = sinh(sinh−1(2n+1)) and 2n+1 = cosh(sinh−1(2n+1)), and similarly for m, we have that

− 1 ≥

s2 cosh sinh−1(2m+1) − sinh−1(2n+1) . Since sinh−1(x) = log(x + √x2 + 1) and cosh(x) exp(x), we can further estimate s2 cosh(log(2m+1 + 22m+2 + 1) − log(2n+1 + 22n+2 + 1)) exp(log(2m+1 + 22m+2 + 1) − log(2n+1 + 22n+2 + 1))

- 2m+1 + √22m+2 + 1

- 2n+1 + √22n+2 + 1


2m−n.

=

Under the same assumptions on ξ,η, it follows from the Lorentz invariance (3.2) and Lemma 7 (a) that

m−n

(σ ∗ σ)(ξ + η, ξ + η ) = (σ ∗ σ)(0,s) s−1 2−

2 . The sum S1 can then be estimated by

S1

f 2L2(C

n,j)

m−n 2

2

n≥0 m≥n 0≤j<2n

### where the inner sum is trivially bounded by

∈Am,n(j)

f 2L2(Cm, ) ,

f 2L2(Cm, ) ≤ min 1,ε2 2m−n+2 .

∈A(m,nj)

It follows that

 

 , (5.14)

min{1,ε2 2m−n+2} 2

f 2L2(An)

S1

m−n 2

n≥0

m≥n

where An denotes the annulus deﬁned in (2.5). We estimate the inner sum on the right-hand side of (5.14) by breaking it up in two pieces, according to whether or not the integer κ := m − n + 2

### satisﬁes ε22κ < 1, or equivalently κ < 2log2(ε−1). We obtain

min{1,ε2 2m−n+2} 2

κ

κ

2−

ε2 2

2+1 +

2+1 ε,

### =

m−n 2

m≥n

κ<2 log2(ε−1)

κ≥2 log2(ε−1)

where both geometric sums were estimated by their largest terms. Plugging this back into (5.14), and recalling that f L2(H2) = 1 and that the annuli in the family {An}n∈N are disjoint, we ﬁnally obtain S1 ε.

- Case 2. 2m − 2jn ∈ −12, 12 \ −22n, 22n mod1. Note that this case is non-empty only if n ≥ 3. Let ξ ∈ Cn,j and η ∈ Cm, . Setting θn,j := arg(ξ) and θm,  := arg(η), we note that, since n ≤ m,


θn,j − θm,  2π −

- 1

- 2n


j 2n − 2m

<

. (5.15) Before we move on, let us make a useful observation. Let

kπ 2 ≤ arg(ξ) <

(k + 1)π 2

Γk = ξ ∈ R2 :

, for 0 ≤ k ≤ 3,

be the four quadrants of the ξ-plane. We may split the function f into four pieces writing f = 3 k=0 f(k), where f(k) = f Γ

. Since Tf 4L4(R3) 3k=0 Tf(k) 4L4(R3) it suﬃces to prove (5.10) for each function f(k) separately. In particular, throughout the rest of this proof we may assume that our f is supported in one of the quadrants, say Γ0. Note that this yields |θn,j − θm, | ≤ π2 in the support of f and hence

k

1 − cos(θn,j − θm, ) |θn,j − θm, |2. As a consequence,

s2 ξ η − ξ · η ≥ |ξ||η|(1 − cos(θn,j − θm, )) 2m+n|θn,j − θm, |2 in the support of f. Invoking Lemma 7 (a) as before, we have that

m+n 2

|θn,j − θm, |−1. (5.16) We seek to estimate the sum

(σ ∗ σ)(ξ + η, ξ + η ) 2−

dη η

dξ ξ

|f(ξ)|2|f(η)|2(σ ∗ σ)(ξ + η, ξ + η )

S2 :=

. (5.17)

n≥0 m≥n 0≤j<2n  /∈A(m,nj) Cm,  Cn,j

For ﬁxed indices 0 ≤ n ≤ m and 0 ≤ j < 2n, we consider the block Bm,n(j,k) := 0 ≤ < 2m : ∈ 2m−n(j + k),2m−n(j + k + 1) mod2m , (5.18)

for −2 ≤ k ≤ 2n − 3. Note that Bm,n(j,k) = 2m−n. Moreover, since A(m,nj) can be partitioned as a disjoint union,

A(m,nj) = Bm,n(j,−2) ∪ Bm,n(j,−1) ∪ Bm,n(j,0) ∪ Bm,n(j,1) ,

the fact that ∈ / A(m,nj) is equivalent to ∈ Bm,n(j,k), for some 2 ≤ k ≤ 2n − 3. If ∈ Bm,n(j,k) \ A(m,nj) , then condition (5.18) can be rewritten as

j 2n ∈

2m −

k 2n

,

k + 1 2n

mod1,

and it follows from (5.15) that

k 2n

|θn,j − θm, |

, (5.19) where x was deﬁned in (5.13). Associated to these index blocks, we deﬁne the set

Bm,n(j,k) :=

- From (5.16), (5.17) and (5.19) we get


Cm, .

∈Bm,n(j,k)

2n−3

m+n 2

f 2L2(Cm, ) f 2L2(Cn,j)2−

|θn,j − θm, |−1

S2

n≥0 m≥n 0≤j<2n

k=2 ∈Bm,n(j,k)

2n−3

−1

k 2n

m+n 2

f 2L2(Cn,j)2−

f 2

L2 Bm,n(j,k)

n≥0 m≥n 0≤j<2n

k=2

2n−1−1

−1

k 2n

m+n 2

f 2L2(Cn,j)2−

f 2

### + f 2

≤

.

L2 Bm,n(j,2n−k−1)

L2 Bm,n(j,k)

n≥0 m≥n 0≤j<2n

k=2

In order to make use of the trivial bound f 2

≤ min{1,ε22m−n}, (5.20) we invoke the Cauchy–Schwarz inequality on the innermost sum of

L2 Bm,n(j,k)

 

 

### f 2

### + f 2

2n−1−1

L2 Bm,n(j,2n−k−1)

L2 Bm,n(j,k)

m−n 2

2−

f 2L2(Cn,j)

S2

k

0≤j<2n

n≥0 m≥n

k=2

- 1

- 2


- 1

- 2 2n−1−1


2n−3

1 k2

m−n 2

2−

f 2L2(Cn,j)

f 4

.

L2 Bm,n(j,k)

0≤j<2n

n≥0 m≥n

k=2

k=2

Recalling (5.20), and noting that the unions

2n−1

2n−3

Bm,n(j,k) ⊆ Am

Cn,j = An, and

j=0

k=2

are disjoint, we have that S2

2−

n≥0 m≥n

m−n 2

m−n

2 min{1,ε2

} f L2(Am) f 2L2(An).

![image 2](<2017-carneiro-extremizers-fourier-restriction-hyperboloids_images/imageFile2.png>)

![image 3](<2017-carneiro-extremizers-fourier-restriction-hyperboloids_images/imageFile3.png>)

Figure 7. For a ﬁxed j, the regions of Case 1 (on the left) and Case 2 (on the right) of the proof of Proposition 15.

We use f L2(Am) ≤ 1 and estimate the inner sum on the right-hand side of

m−n

m−n 2

2−

f 2L2(An)

2 min{1,ε2

} (5.21)

S2

n≥0

m≥n

as before. In more detail, set κ := m−n and break up the sum in two pieces, depending on whether or not the condition ε2κ2 < 1 is satisﬁed. This yields:

m−n

m−n 2

κ

κ

κ

2−

2−

2−

2 εlog2(ε−1).

≤

2 min 1,ε2

2 ε2

2 +

m≥n

κ<2 log2(ε−1)

κ≥2 log2(ε−1)

Plugging this back into (5.21), we ﬁnally obtain that S2 εlog2(ε−1). This completes the proof.

- Proposition 16. Let d = 2 and 4 ≤ p < 6. Let {fn}n∈N ⊂ L2(H2) be an extremizing sequence


- for inequality (1.4), normalized so that fn L2(H2) = 1 for each n ∈ N. There exists a universal


- constant η2,p > 0 and n0 ∈ N, such that for any n ≥ n0 there exist sn ∈ (−1,1) and ϕn ∈ [0,2π) verifying


)∗fn L2(D) ≥ η2,p , where D := {(ξ,τ) ∈ H2 : |ξ| ≤ 2√2π}.

(Ls

### ◦ Rϕ

n

n

Proof. Let n0 ∈ N be such that, for n ≥ n0, we have Tfn Lp(R3) ≥

H2,p 2

. Fix n ≥ n0. We claim that there exists γp > 0, depending only on p, such that sup

fn L2(Cm, ) ≥ γp > 0, (5.22)

m, 

where the supremum is taken over integers m ≥ 0 and 0 ≤ < 2m. For otherwise we could appeal to Proposition 15 to ensure

H2,p

θ

2 ≤ Tfn Lp(R3) ≤ Tfn θL4(R3) Tfn 1L−6(θR3) (εlog2(ε−1))

4 ,

which is a contradiction provided θ > 0 and ε > 0 is suﬃciently small. Knowing (5.22), it is now a simple matter to invoke Lemma 4 (b) and conclude the proof of the proposition.

6. Concentration Compactness

In this section, we adapt parts of the work of Fanelli, Vega and Visciglia [17, 18] in order to complete the proof of Theorem 2. We rely on the following key result from [17, Proposition 1.1].

Lemma 17 (cf. [17]). Let H be a Hilbert space and S : H → Lp(Rd) be a bounded linear operator with p ∈ (2,∞). Consider {hn}n∈N ⊂ H such that

- (i) limn→∞ hn H = 1;
- (ii) limn→∞ S(hn) Lp(Rd) = S H→Lp(Rd);
- (iii) hn h = 0;
- (iv) S(hn) → S(h) almost everywhere in Rd.


Then hn → h in H. In particular, h H = 1 and S(h) Lp(Rd) = S H→Lp(Rd).

The argument which we will present next works as long as one can produce a special cap, as was done in §5 in the lower dimensional cases d ∈ {1,2}. We state the next two results in general dimensions d, thereby guaranteeing the existence of extremizers, conditionally on the existence of a special cap.

- Proposition 18. Let d ≥ 1 and let p be such that  


6 < p < ∞, if d = 1;



2(d+2)

d < p ≤ 2(dd−+1)1 , if d ≥ 2.

Assume the existence of two universal constants η = ηd,p > 0 and r = rd,p > 0 verifying the following property: for any extremizing sequence {fn}n∈N ⊂ L2(Hd) for inequality (1.4), normalized so that

fn L2(Hd) = 1 for each n ∈ N, there exists n0 ∈ N such that fn L2(D) ≥ η

for any n ≥ n0, where D := {(ξ,τ) ∈ Hd : |ξ| ≤ r}. Then there exists (xn,tn) ∈ Rd × R such that the sequence {gn}n∈N deﬁned by

n·yeit

n y fn(y) admits a subsequence that converges weakly to a nonzero limit in L2(Hd).

gn(y) := eix

- Proof. We follow the outline of the proof of [17, Theorem 1.1, p = ∞]. Setting fn,0 := fn D we have, for n ≥ n0,


- 1

- 2. (6.1)


η ≤ fn,0 L2(Hd) ≤ 1, and fn Hd\D L2(Hd) ≤ (1 − η2) Moreover,

dy y is a smooth function of x,t, satisfying

eix·yeit y fn(y)

T(fn,0)(x,t) =

{|y|≤r}

T(fn,0) L∞(Rd+1) fn,0 L2(Hd) ≤ 1, (6.2)  ∇x,tT(fn,0) L∞(Rd+1) fn,0 L2(Hd) ≤ 1. (6.3)

Since 2(dd+2) < p, the log-convexity of Lebesgue norms, together with the sharp inequality (1.4) and the ﬁrst upper bound in (6.1), yields

T(fn,0) Lp(Rd+1) ≤ T(fn,0)

2(d+2) dp

2(d+2)

d (Rd+1)

L

d(p−2)−4 dp

d(p−2)−4 dp

2(d+2) dp

L∞(Rd+1) ≤ H

T(fn,0)

L∞(Rd+1). (6.4)

d,2(dd+2) T(fn,0)

Since the sequence {fn}n∈N is extremizing and L2-normalized, there exists δ = δd,p > 0, depending only on d and p, for which

- 1

- 2 Hd,p ,


Tfn Lp(Rd+1) ≥ δ + (1 − η2) for every suﬃciently large n ∈ N. Together with the second upper bound in (6.1), this implies T(fn,0) Lp(Rd+1) ≥ Tfn Lp(Rd+1) − T(fn Hd\D) Lp(Rd+1) ≥ δ + (1 − η2)

- 1

- 2 Hd,p − (1 − η2)


- 1

- 2 Hd,p = δ Hd,p. (6.5)


- From (6.4) and (6.5) we get


2(d+2) d(p−2)−4

dp d(p−2)−4

d,p H−

dp

T(fn,0) L∞(Rd+1) ≥ γ := δ

d,2(dd+2) . This readily implies the existence of (xn,tn) ∈ Rd × R, for which

d(p−2)−4 H

γ 2

|T(fn,0)(xn,tn)| ≥

. (6.6) Setting

n·yeit

n y fn,0(y), (6.7) we have that gn L2(Hd) = fn,0 L2(Hd). Moreover, T( gn) amounts to a space-time translation of the function T(fn,0). From (6.2), (6.3) and (6.6), it then follows that

gn(y) := eix

γ 2

T( gn) L∞(Rd+1) 1,  ∇x,tT( gn) L∞(Rd+1) 1, and |T( gn)(0,0)| ≥

. (6.8) The implicit constants in the ﬁrst and second estimates in (6.8) are independent of n, and so the sequence {T( gn)}n∈N is uniformly bounded and equicontinuous on the unit cube [−12, 21]d+1. The Arzel`–Ascoli Theorem on Rd+1 then implies that the sequence {T( gn)}n∈N has a subsequence which

converges uniformly to a limit. That this limit is nonzero follows at once from the third estimate in (6.8).

Now, since the sequence { gn}n∈N is bounded on L2(Hd), it has a weakly convergent subsequence. In other words, we may thus assume, possibly after extraction, that there exists a function g ∈ L2(Hd), such that gn g weakly in L2(Hd), as n → ∞. Since the operator T is bounded from L2(Hd) to Lp(Rd+1), it follows that T( gn) T( g) weakly in Lp(Rd+1), as n → ∞. From the previous paragraph we conclude that T( g) is nonzero, and so the function g is itself nonzero.

This implies that the sequence {gn}n∈N deﬁned by gn(y) := eix

n·yeit

n y fn(y),

where the parameters (xn,tn) are those from (6.7), has a subsequence which converges weakly to a nonzero limit. Indeed, if g ∈ L2(Hd) is such that gn g weakly in L2(Hd), as n → ∞, then gn D g D weakly in L2(Hd), as n → ∞. Therefore, in order to prove that g is nonzero, it suﬃces to show that it has nonzero mass inside D. This follows from the fact that g is nonzero, which we checked in the last paragraph. The proof of the proposition is now complete.

- Proposition 19. Let d ∈ N, and let p be such that  


6 < p < ∞, if d = 1;



2(d+2)

d < p ≤ 2(dd−+1)1 , if d ≥ 2.

Let {fn}n∈N ⊂ L2(Hd) be an extremizing sequence for inequality (1.4), normalized so that fn L2(Hd) = 1 for each n ∈ N, which converges weakly to a nonzero limit f ∈ L2(Hd). Then, possibly after passing to a subsequence,

Tfn(x,t) → Tf(x,t), as n → ∞, for almost every (x,t) ∈ Rd × R.

- Proof. We follow the outline of the proof of [18, Theorem 1.1]. For each n ∈ N, deﬁne the auxiliary functions


f(y) y

fn(y) y

, and also g(y) :=

.

gn(y) :=

As it has been pointed out in (1.8), the extension operator on the hyperboloid and the Klein–Gordon propagator are related by

√1−∆gn(x), and it suﬃces to show that, pointwise for almost every (x,t) ∈ Rd × R, eit

Tfn(x,t) = (2π)d eit

√1−∆gn(x) → eit

√1−∆g(x), as n → ∞, possibly after extraction of a subsequence. For t ∈ R and R > 0, we deﬁne Fn(t,R) :=

√1−∆(gn − g)(x) 2dx,

eit

{|x|≤R}

and we claim that

lim

Fn(t,R) = 0 (6.9)

n→∞

In order to prove this claim, ﬁrst recall that {gn}n∈N is bounded on the Sobolev space H 12 (Rd), with

2 (Rd) = fn L2(Hd) = 1. (6.10) Let BR ⊂ Rd denote the ball centered at the origin of radius R. The hypothesis fn f weakly in L2(Hd) can be equivalently restated as gn g weakly in H 12 (Rd). Since, for ﬁxed t ∈ R, the operator eit

gn H 1

√1−∆ is unitary on H 12 (Rd), it follows that eit

√1−∆g weakly in H 12 (Rd), which in turn implies that eit

√1−∆gn eit

√1−∆g weakly in H 12 (BR). As a consequence of (6.10) and of Rellich’s Theorem, see e.g. [16, Theorem 7.1 and Proposition 3.4], we ﬁnd

√1−∆gn eit

√1−∆gn → eit

√1−∆g strongly in L2(BR), as n → ∞. In other words, (6.9) holds as claimed. We further note, since the operator eit

eit

√1−∆ is unitary on L2(Rd), that

√1−∆(gn − g) 2L

2(Rd) = gn − g 2L2(Rd) gn − g 2

Fn(t,R) ≤ eit

1.

H 12 (Rd)

This justiﬁes the applicability of Lebesgue’s Dominated Convergence Theorem which, together with (6.9), implies

R

R

√1−∆(gn − g)(x) 2 dxdt = 0. As a consequence, up to a subsequence,

eit

lim

Fn(t,R)dt = lim

n→∞

n→∞

−R

−R {|x|≤R}

√1−∆(gn − g)(x) → 0, as n → ∞, for a.e. (x,t) ∈ BR × (−R,R).

eit

The extraction of the subsequence depends on the radius R. To remedy this, repeat the argument on a discrete sequence of radii {Rj}j∈N satisfying Rj → ∞, as j → ∞, to conclude, via a standard diagonal argument, that there exists a subsequence {gn

k}k∈N ⊂ {gn}n∈N such that eit

√1−∆(gn

k − g)(x) → 0, as k → ∞, for a.e. (x,t) ∈ Rd × R. This concludes the proof of the proposition.

It is now an easy matter to ﬁnish the proof of Theorem 2.

Proof of Theorem 2. Let us start by considering the case d = 1 and p ∈ (6,∞). The strategy is to invoke Lemma 17 with S = T and H = L2(H1). With that purpose in mind, let {fn}n∈N be an extremizing sequence for the inequality

Tf Lp(R2) ≤ H1,p f L2(H1), (6.11) normalized so that fn L2(H1) = 1 for each n ∈ N. In particular, conditions (i) and (ii) from Lemma

- 17 are automatically met. We will be done once we check that conditions (iii) and (iv) hold as well.


### )∗fn}n∈N, which is still extremizing for (6.11), veriﬁes (Ls

### By Proposition 14, the sequence {(Ls

n

)∗fn L2(C0) ≥ η1,p > 0, for every n ∈ N. By Proposition 18, the sequence {gn}n∈N deﬁned by gn(y) = eix

n

)∗fn)(y), which is still extremizing for (6.11), is such that

nyeit

### n y ((Ls

n

gn g = 0 weakly in L2(H1), as n → ∞, possibly after passing to a subsequence. By Proposition 19, we then know that T(gn) → T(g) pointwise a.e. on R2, as n → ∞,

again possibly after passing to a subsequence. By Lemma 17, we ﬁnally conclude that gn → g in L2(H1), as n → ∞. In other words, g is an extremizer for inequality (6.11). This concludes the proof of the one-dimensional case. The two-dimensional case d = 2 and p ∈ (4,6) can be handled in an analogous way. One just invokes Proposition 16 instead of Proposition 14, the rest of the argument being identical. This concludes the proof.

Acknowledgements

We thank Rene´ Quilodr´n, Betsy Stovall and Christoph Thiele for stimulating discussions. This work was accomplished during visits to the Hausdorﬀ Research Institute for Mathematics (Bonn), the International Centre for Theoretical Physics (Trieste) and Stanford University, whose hospitality is greatly appreciated. E.C. acknowledges support from CNPq-Brazil, FAPERJ-Brazil and the Fulbright Junior Faculty Award. D.O.S. was partially supported by the Hausdorﬀ Center for Mathematics and DFG grant CRC 1060. M.S. acknowledges support from FAPERJ-Brazil.

References

- [1] M. Abramowitz and I. A. Stegun, Handbook of mathematical functions with formulas, graphs, and mathematical tables, Dover Publications, 1970.
- [2] J. Bennett, N. Bez, A. Carbery and D. Hundertmark, Heat-ﬂow monotonicity of Strichartz norms, Anal. PDE 2 (2009), no. 2, 147–158.
- [3] J. Bennett, N. Bez and M. Iliopoulou, Flow monotonicity and Strichartz inequalities, Int. Math. Res. Not. IMRN 2015, no. 19, 9415–9437.
- [4] J. Bennett, N. Bez, C. Jeavons and N. Pattakos, On sharp bilinear Strichartz estimates of Ozawa–Tsutsumi type, J. Math. Soc. Japan 69 (2017), no. 2, 459–476.
- [5] N. Bez, C. Jeavons and T. Ozawa, Some sharp bilinear space-time estimates for the wave equation, Mathematika 62 (2016), no. 3, 719–737.
- [6] N. Bez and K. Rogers, A sharp Strichartz estimate for the wave equation with data in the energy space, J. Eur. Math. Soc. (JEMS) 15 (2013), no. 3, 805–823.
- [7] A. Bulut, Maximizers for the Strichartz inequalities for the wave equation, Diﬀerential Integral Equations 23

(2010), no. 11–12, 1035–1072.

- [8] T. Candy, Multi-scale bilinear restriction estimates for general phases, Preprint, 2017. arXiv:1707.08944.


- [9] L. Carleson and P. Sjolin¨ , Oscillatory integrals and a multiplier problem for the disc, Studia Math. 44 (1972), 287–299.
- [10] E. Carneiro, A sharp inequality for the Strichartz norm, Int. Math. Res. Not. IMRN (2009), no. 16, 3127–3145.
- [11] E. Carneiro, D. Foschi, D. Oliveira e Silva and C. Thiele, A sharp trilinear inequality related to Fourier restriction on the circle, Preprint, 2015. arXiv:1509.06674. To appear in Rev. Mat. Iberoam.
- [12] E. Carneiro and D. Oliveira e Silva, Some sharp restriction inequalities on the sphere, Int. Math. Res. Not. IMRN (2015), no. 17, 8233–8267.
- [13] M. Christ and R. Quilodran´ , Gaussians rarely extremize adjoint Fourier restriction inequalities for paraboloids, Proc. Amer. Math. Soc. 142 (2014), no. 3, 887–896.
- [14] M. Christ and S. Shao, Existence of extremals for a Fourier restriction inequality, Anal. PDE. 5 (2012), no. 2, 261–312.
- [15] M. Christ and S. Shao, On the extremizers of an adjoint Fourier restriction inequality, Adv. Math. 230 (2012), no. 3, 957–977.
- [16] E. Di Nezza, G. Palatucci and E. Valdinoci, Hitchhiker’s guide to the fractional Sobolev spaces, Bull. Sci. Math. 136 (2012), no. 5, 521–573.
- [17] L. Fanelli, L. Vega and N. Visciglia, On the existence of maximizers for a family of restriction theorems, Bull. Lond. Math. Soc. 43 (2011), no. 4, 811–817.
- [18] L. Fanelli, L. Vega and N. Visciglia, Existence of maximizers for Sobolev–Strichartz inequalities, Adv. Math. 229 (2012), no. 3, 1912–1923.
- [19] D. Foschi, Maximizers for the Strichartz inequality, J. Eur. Math. Soc. (JEMS) 9 (2007), no. 4, 739–774.
- [20] D. Foschi, Global maximizers for the sphere adjoint Fourier restriction inequality, J. Funct. Anal. 268 (2015), 690–702.
- [21] D. Foschi and D. Oliveira e Silva, Some recent progress in sharp Fourier restriction theory, Preprint, 2017. arXiv:1701.06895. To appear in Analysis Math.
- [22] R. Frank, E. H. Lieb and J. Sabin, Maximizers for the Stein–Tomas inequality, Geom. Funct. Anal. 26 (2016), no. 4, 1095–1134.
- [23] F. Gon¸calves, Orthogonal polynomials and sharp estimates for the Schro¨dinger equation, Preprint, 2017. arXiv:1702.08510.
- [24] D. Hundertmark and S. Shao, Analyticity of extremizers to the Airy–Strichartz inequality, Bull. Lond. Math. Soc. 44 (2012), no. 2, 336–352.
- [25] D. Hundertmark and V. Zharnitsky, On sharp Strichartz inequalities in low dimensions, Int. Math. Res. Not. IMRN (2006), Art. ID 34080, 1–18.
- [26] C. Jeavons, A sharp bilinear estimate for the Klein–Gordon equation in arbitrary space-time dimensions, Differential Integral Equations 27 (2014), no. 1-2, 137–156.
- [27] J.-C. Jiang, S. Shao and B. Stovall, Linear proﬁle decompositions for a family of fourth order Schr¨odinger equations, Preprint, 2014. arXiv:1410.7520.
- [28] R. Killip, B. Stovall and M. Visan, Scattering for the cubic Klein–Gordon equation in two space dimensions, Trans. Amer. Math. Soc. 364 (2012), no. 3, 1571–1631.
- [29] M. Kunze, On the existence of a maximizer for the Strichartz inequality, Comm. Math. Phys. 243 (2003), no. 1, 137–162.
- [30] D. Oliveira e Silva, Extremals for Fourier restriction inequalities: convex arcs, J. Anal. Math. 124 (2014), 337–385.
- [31] D. Oliveira e Silva, Nonexistence of extremizers for certain convex curves, Preprint, 2012. arXiv:1210.0585. To appear in Math. Res. Lett.
- [32] D. Oliveira e Silva and R. Quilodran´ , On extremizers for Strichartz estimates for higher order Schr¨odinger equations, Preprint, 2016. arXiv:1606.02623. To appear in Trans. Amer. Math. Soc.


- [33] T. Ozawa and K. Rogers, A sharp bilinear estimate for the Klein–Gordon equation in R1+1, Int. Math. Res. Not. IMRN (2014), no. 5, 1367–1378.
- [34] R. Quilodran´ , On extremizing sequences for the adjoint restriction inequality on the cone, J. Lond. Math. Soc.

(2) 87 (2013), no. 1, 223–246.

- [35] R. Quilodran´ , Nonexistence of extremals for the adjoint restriction inequality on the hyperboloid, J. Anal. Math. 125 (2015), 37–70.
- [36] J. Ramos, A reﬁnement of the Strichartz inequality for the wave equation with applications, Adv. Math. 230

(2012), no. 2, 649–698.

- [37] S. Shao, Maximizers for the Strichartz and the Sobolev–Strichartz inequalities for the Schr¨odinger equation, Electron. J. Diﬀerential Equations (2009), No. 3, 13 pp.
- [38] S. Shao, The linear proﬁle decomposition for the Airy equation and the existence of maximizers for the Airy– Strichartz inequality, Anal. PDE 2 (2009), no. 1, 83–117.
- [39] S. Shao, On existence of extremizers for the Tomas–Stein inequality for S1, J. Funct. Anal. 270 (2016), 3996– 4038.
- [40] R. S. Strichartz, Restrictions of Fourier transforms to quadratic surfaces and decay of solutions of wave equations, Duke Math. J. 44 (1977), no. 3, 705–714.
- [41] G. N. Watson, A Treatise on the Theory of Bessel Functions, Second Edition. Cambridge University Press, Cambridge, 1966.


IMPA - Instituto de Matematica´ Pura e Aplicada, Rio de Janeiro - RJ, Brazil, 22460-320.

E-mail address: carneiro@impa.br E-mail address: mateuscs@impa.br

Hausdorff Center for Mathematics, 53115 Bonn, Germany E-mail address: dosilva@math.uni-bonn.de

