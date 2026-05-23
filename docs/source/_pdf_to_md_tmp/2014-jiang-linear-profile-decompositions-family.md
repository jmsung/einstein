arXiv:1410.7520v2[math.AP]18Apr2017

LINEAR PROFILE DECOMPOSITIONS FOR A FAMILY OF FOURTH ORDER SCHRODINGER¨ EQUATIONS

JIN-CHENG JIANG, SHUANGLIN SHAO, AND BETSY STOVALL

Abstract. We establish linear proﬁle decompositions for the fourth order Schr¨odinger equation and for certain fourth order perturbations of the Schr¨odinger equation, in dimensions greater than or equal to two. We apply these results to prove dichotomy results on the existence of extremizers for the associated Stein–Tomas/Strichartz inequalities; along the way, we also obtain lower bounds for the norms of these operators.

1. Introduction We consider the family of fourth order Schro¨dinger equations

iut + ∆2u − µ∆u = 0, µ ≥ 0, u(0) = u0 ∈ L2x(Rd)

- (1)


where u : R × Rd → C, d ≥ 2. For µ = 0, this is the free form of the nonlinear Schro¨dinger equation with a fourth order perturbation; this equation was introduced by Karpman [10] (see also [13, 11, 12, 14]) to study the eﬀects of higher order dispersion in the propagation of solitary waves in plasmas.

The main result of this article (Theorem 3.1) is a linear proﬁle decomposition for the equations given by (1). The theorem roughly states that, after passing to a subsequence, an L2x-bounded sequence of initial data may be decomposed as sum of asymptotically orthogonal pieces that are compact modulo symmetries, plus an error term with arbitrarily small dispersion. We then use this result to obtain dichotomy results on the existence of extremizers to the inequalities

d

2(d+2)eit(∆2−µ∆)f

(µ + |∇|2)

![image 1](<2014-jiang-linear-profile-decompositions-family_images/imageFile1.png>)

2(d+2) d t,x

![image 2](<2014-jiang-linear-profile-decompositions-family_images/imageFile2.png>)

L

≤ Cd,µ f L2

,

x

in the spirit of Shao [28]. Our results generalize those of Jiang, Pausader and Shao [9], wherein the analogous theorems were proved in the one dimensional case. Though the results we obtain are similar, we encounter new challenges in higher dimensions. One reason for this is that the propagator eit(∆2−µ∆) may be viewed as a Fourier extension operator, and the analysis of such operators seems to be much more diﬃcult in dimensions greater than or equal to two.

We are additionally motivated by recent applications of linear proﬁle decompositions to the study of other dispersive equations, including wave [1, 17], Schro¨dinger [2, 23, 4, 16, 20, 22], KdV [28, 18], and Klein–Gordon [19].

Finally, much of the argument seems amenable to an extension to more general perturbations of the Schro¨dinger equation, for instance with ∆2 replaced by |∇|α for α > 0, but the authors have not investigated the extent to which this argument would need to be changed.

We now turn to a brief outline of the proof. For the remainder of this article, we let Sµ(t) denote the data-to-solution map,

Sµ(t) = eit(∆2−µ∆)

![image 3](<2014-jiang-linear-profile-decompositions-family_images/imageFile3.png>)

Date: May 5, 2021.

1

and let Dµ denote the diﬀerential operator Dµ = µ + |∇|2.

![image 4](<2014-jiang-linear-profile-decompositions-family_images/imageFile4.png>)

Section 2 is devoted to a proof of a reﬁnement (Proposition 2.2) of the Strichartz/Stein–Tomas inequality

d

![image 5](<2014-jiang-linear-profile-decompositions-family_images/imageFile5.png>)

µd+2Sµ(t)f

- (2) D


2(d+2) d t,x

![image 6](<2014-jiang-linear-profile-decompositions-family_images/imageFile6.png>)

L

f L2

.

x

Roughly, this result states that if the left side of this inequality is greater than a constant times the right side, the function f must contain a nontrivial wave packet that is concentrated on a small ‘cap’ on the Fourier side. To overcome the diﬃculty of vanishing Gaussian curvature at the origin of the quartic surface, we reduce estimating it to an annulus {|ξ| ∼ 1}, where after standard normalizations the results of Tao on bilinear paraboloid restriction can be applied. This result is stronger than the annular reﬁnement obtained in Chae, Hong and Lee [5, Proposition 2.3] (and necessary for our ﬁner-scale decomposition), and its proof strongly relies on Tao’s bilinear restriction theorem for elliptic hypersurfaces from Tao [30]. One challenge that we face in proving the reﬁned Strichartz inequality for these fourth order equations (compared with wave, Schro¨dinger, or Klein–Gordon) is the lack of scale invariance when µ = 0, coupled with the absence of any natural analogue of the Lorentz or Galilei boosts. (The phase shifts Sµ(t)f  → Sµ(t)ei(·)af will provide a rough stand-in.)

Once we have obtained this reﬁnement, we turn in Section 3 to the proof of the linear proﬁle decomposition. This result, Theorem 3.1, follows by a familiar inductive argument. If (un) is an L2x-bounded sequence such that D

d

![image 7](<2014-jiang-linear-profile-decompositions-family_images/imageFile7.png>)

µd+2Sµ(t)un

does not tend to 0, by the reﬁned

2(d+2) d t,x

![image 8](<2014-jiang-linear-profile-decompositions-family_images/imageFile8.png>)

L

Strichartz estimate, there exists a sequence {gn1} of pseudo-symmetries (true symmetries, i.e. spacetime translations, composed with scalings and phase shifts) such that the sequence (gn1)−1un has a nonzero weak limit φ1 ∈ L2x. The ﬁrst proﬁle is φ1n = gn1φ1, and we then repeat the argument on the sequence un −φ1n. In fact, the reﬁned Strichartz estimate gives a quantitative lower bound on the L2x norm of φ1, and it is this that allows us to eventually show that for large l, the error terms wnl are negligible. Having established the linear proﬁle decomposition, for our application, we need to prove that the pieces Sµ(t)φjn and Sµ(t)φkn are asymptotically orthogonal for j = k. This is the content of Proposition 3.2.

Finally, in Section 4, we apply the linear proﬁle decomposition to prove Theorems 4.1 and 4.2, which give lower bounds for the operator norms and dichotomy results on the existence of extremizers to (2) when µ = 0 or 1 (by scaling, this extends to the general case). Very roughly, because of the asymptotic orthogonality of the proﬁles in the decomposition, after passing to a subsequence, an extremizing sequence to (2) must contain a single proﬁle. After passing to a subsequence, there are three possibilities: compactness, convergence to a free Schro¨dinger wave, or convergence to a free S0 wave. In the ﬁrst case, extremizers exist. In the latter two, extremizers may fail to exist, but these cases give us the desired lower bounds on the operator norms.

Acknowledgements. The research of the ﬁrst author was supported by National Science Council Grant NSC100-2115-M-007-009-MY2. The second author was supported by NSF DMS1160981 and KU 2016-2017 general research fund. The third author was supported by NSF DMS-0902667 and 1266336.

2. The refined Strichartz inequality

Fix d ≥ 2 and µ ≥ 0. For the remainder of the article, let φ : Rd → [0,1] be a smooth, radial, decreasing bump function with φ ≡ 1 on {|ξ| ≤ 1} and φ ≡ 0 on {|ξ| ≥ 2}.

In this section, we prove the reﬁned Strichartz inequality, which is crucial to our proﬁle decomposition. Before stating it, we need a little notation. Deﬁnition 2.1. A µ-cap is a ball κ = {ξ : |ξ − ξ0| < r}, for some ξ0 ∈ Rd and r > 0 satisfying 8r ≤ |ξ0| + √µ.

![image 9](<2014-jiang-linear-profile-decompositions-family_images/imageFile9.png>)

Given a cap κ with center ξ0 and radius r, we deﬁne an associated cutoﬀ φκ(ξ) = φ

ξ − ξ0 r

. Given f we denote by fκ the function whose Fourier transform is given by fκ = φκ f.

![image 10](<2014-jiang-linear-profile-decompositions-family_images/imageFile10.png>)

With this notation in place, our reﬁned Strichartz inequality is the following. Proposition 2.2 (Reﬁned Strichartz). Let q = 2(d

2+3d+1)

d2 and θ = (d+2)2 2 . If f ∈ L2x(Rd), then

![image 11](<2014-jiang-linear-profile-decompositions-family_images/imageFile11.png>)

![image 12](<2014-jiang-linear-profile-decompositions-family_images/imageFile12.png>)

2 q µ fκ Lq

d

d+2

dq −12 Sµ(t)D

)θ f 1L−2θ

![image 13](<2014-jiang-linear-profile-decompositions-family_images/imageFile13.png>)

![image 14](<2014-jiang-linear-profile-decompositions-family_images/imageFile14.png>)

µd+2f

sup

|κ|

- (3) Sµ(t)D


.

![image 15](<2014-jiang-linear-profile-decompositions-family_images/imageFile15.png>)

![image 16](<2014-jiang-linear-profile-decompositions-family_images/imageFile16.png>)

2(d+2)

t,x

x

![image 17](<2014-jiang-linear-profile-decompositions-family_images/imageFile17.png>)

κ

d t,x

L

Here the supremum is taken over all µ-caps κ as in Deﬁnition 2.1, and the implicit constant depends only on d.

Propositions of this kind have appeared in many places in the literature, and the outline we follow is a familiar one (cf. [2, 21]). The main new ingredient here is the parameter µ. When µ = 0, the graph of the function µ|ξ|2 + |ξ|4 has vanishing curvature at 0, while in the case µ > 0, the curvature never vanishes, but the scaling symmetry is broken. To deal with these issues, we begin by proving a reﬁned Strichartz estimate associated to the decoupling of dyadic frequency annuli. By this and scaling, it suﬃces to establish a reﬁnement of the Stein–Tomas inequality for the Fourier extension operator associated to the surfaces {(|ξ|2 + |ξ|4,ξ) : |ξ| 1} and {(ε|ξ|2 +|ξ|4,ξ) : |ξ| ∼ 1}, where 0 ≤ ε 1. These surfaces are uniformly well-curved; indeed, they are elliptic on small (but uniform) frequency scales. We can thus apply Tao’s bilinear restriction theorem, and use methods developed in the context of the linear proﬁle decomposition for Schro¨dinger to obtain reﬁned estimates on these frequency localized regions. Finally, it is a simple matter to undo the scaling and glue the pieces back together, thereby obtaining (3).

We begin by noting that it suﬃces to prove Proposition 2.2 when µ = 0,1. Indeed, if µ > 0, a simple computation shows that

Sµ(t)f = [S1(µ2t)f(√·µ)](√µ · ), and Dµf = [√µD1f(√·µ)](√µ · ). Furthermore, if κ = {ξ : |ξ −ξ0| < r} is a 1-cap, √µκ = {ξ : |ξ −

![image 18](<2014-jiang-linear-profile-decompositions-family_images/imageFile18.png>)

![image 19](<2014-jiang-linear-profile-decompositions-family_images/imageFile19.png>)

![image 20](<2014-jiang-linear-profile-decompositions-family_images/imageFile20.png>)

![image 21](<2014-jiang-linear-profile-decompositions-family_images/imageFile21.png>)

![image 22](<2014-jiang-linear-profile-decompositions-family_images/imageFile22.png>)

![image 23](<2014-jiang-linear-profile-decompositions-family_images/imageFile23.png>)

![image 24](<2014-jiang-linear-profile-decompositions-family_images/imageFile24.png>)

√µξ0| < √µr} is a µ-cap. Thus Proposition 2.2 for any µ > 0 follows from Proposition 2.2 in the case µ = 1 by scaling. For the remainder of this section, we will consider only the cases µ = 0,1.

![image 25](<2014-jiang-linear-profile-decompositions-family_images/imageFile25.png>)

![image 26](<2014-jiang-linear-profile-decompositions-family_images/imageFile26.png>)

![image 27](<2014-jiang-linear-profile-decompositions-family_images/imageFile27.png>)

We will employ two diﬀerent Littlewood–Paley decompositions, depending on whether µ = 0 or µ = 1. Deﬁne

ψ01(ξ) = φ(2ξ), ψN1 (ξ) = φ(Nξ ) − φ(2Nξ), for N ∈ 2N, ψN0 (ξ) = φ(Nξ ) − φ(2Nξ), for N ∈ 2Z.

![image 28](<2014-jiang-linear-profile-decompositions-family_images/imageFile28.png>)

![image 29](<2014-jiang-linear-profile-decompositions-family_images/imageFile29.png>)

![image 30](<2014-jiang-linear-profile-decompositions-family_images/imageFile30.png>)

![image 31](<2014-jiang-linear-profile-decompositions-family_images/imageFile31.png>)

Regardless of the value of µ, the ψNµ form a partition of unity. We deﬁne the Littlewood–Paley projections PNµ by fNµ = PNµf = ψNµ f, µ = 0,1.

Lemma 2.3. If f ∈ L2x, then

- (4) Sµ(t)D

d

![image 32](<2014-jiang-linear-profile-decompositions-family_images/imageFile32.png>)

µd+2f

L

2(d+2)

![image 33](<2014-jiang-linear-profile-decompositions-family_images/imageFile33.png>)

d t,x

sup

N

Sµ(t)D

d

![image 34](<2014-jiang-linear-profile-decompositions-family_images/imageFile34.png>)

µd+2fNµ

2 d+2

![image 35](<2014-jiang-linear-profile-decompositions-family_images/imageFile35.png>)

L

2(d+2) d t,x

![image 36](<2014-jiang-linear-profile-decompositions-family_images/imageFile36.png>)

f

d d+2

![image 37](<2014-jiang-linear-profile-decompositions-family_images/imageFile37.png>)

L2x ,

for µ = 0,1. Here, the supremum is taken over frequencies N ∈ {0} ∪ 2N or N ∈ 2Z, depending on the value of µ.

In the proof of Lemma 2.3, we will use the following Strichartz estimates, which may be proved using the methods of stationary phase together with the main theorem of Keel and Tao [15]. See Pausader [25] for further details.

Proposition 2.4. Let µ ≥ 0. For all (q,r) satisfying 2 ≤ q,r ≤ ∞, (q,r) = (2,∞), and 2q +dr = d2,

![image 38](<2014-jiang-linear-profile-decompositions-family_images/imageFile38.png>)

![image 39](<2014-jiang-linear-profile-decompositions-family_images/imageFile39.png>)

![image 40](<2014-jiang-linear-profile-decompositions-family_images/imageFile40.png>)

- (5) D


2 q µSµ(t)f Lq

![image 41](<2014-jiang-linear-profile-decompositions-family_images/imageFile41.png>)

tLrx(R×Rd) f L2

x(Rd).

The implicit constant may be taken to depend only on d,q,r and, in particular, may be chosen independently of µ.

Proof. Let d = 2. By the Littlewood–Payley square function estimate, simple arithmetic, H¨older’s inequality, and the Strichartz inequality, for µ = 0,1,

1

1

1

µ2fMµ |2)(

µ2fNµ|2)dxdt

µ2f 4L4

![image 42](<2014-jiang-linear-profile-decompositions-family_images/imageFile42.png>)

![image 43](<2014-jiang-linear-profile-decompositions-family_images/imageFile43.png>)

![image 44](<2014-jiang-linear-profile-decompositions-family_images/imageFile44.png>)

∼ (

|Sµ(t)D

|Sµ(t)D

Sµ(t)D

t,x

M

N

1

1

µ2fMµ )(Sµ(t)D

µ2fNµ) 2L2

![image 45](<2014-jiang-linear-profile-decompositions-family_images/imageFile45.png>)

![image 46](<2014-jiang-linear-profile-decompositions-family_images/imageFile46.png>)

(Sµ(t)D

∼

t,x

M≥N

1

1

1

1

µ2fMµ L4

µ2fMµ L3

µ2fNµ L4

µ2fNµ L6

![image 47](<2014-jiang-linear-profile-decompositions-family_images/imageFile47.png>)

![image 48](<2014-jiang-linear-profile-decompositions-family_images/imageFile48.png>)

![image 49](<2014-jiang-linear-profile-decompositions-family_images/imageFile49.png>)

![image 50](<2014-jiang-linear-profile-decompositions-family_images/imageFile50.png>)

Sµ(t)D

Sµ(t)D

tL6x Sµ(t)D

Sµ(t)D

tL3x

t,x

t,x

M≥N

1

1

1

D−

µ2fKµ 2L4

µ 6fMµ L2

µ6fNµ L2

![image 51](<2014-jiang-linear-profile-decompositions-family_images/imageFile51.png>)

![image 52](<2014-jiang-linear-profile-decompositions-family_images/imageFile52.png>)

![image 53](<2014-jiang-linear-profile-decompositions-family_images/imageFile53.png>)

D

.

sup

Sµ(t)D

x

x

t,x

K

M≥N

If µ = 0, this implies by Plancherel that

1

µ2f 4L4

![image 54](<2014-jiang-linear-profile-decompositions-family_images/imageFile54.png>)

Sµ(t)D

t,x

while if µ = 1,

sup

K

1

µ2fK0 2L4

![image 55](<2014-jiang-linear-profile-decompositions-family_images/imageFile55.png>)

Sµ(t)D

t,x

M−61N 16 fM0 L2

![image 56](<2014-jiang-linear-profile-decompositions-family_images/imageFile56.png>)

![image 57](<2014-jiang-linear-profile-decompositions-family_images/imageFile57.png>)

x

M≥N

fN0 L2

,

x

1

µ2f1 4L4

![image 58](<2014-jiang-linear-profile-decompositions-family_images/imageFile58.png>)

Sµ(t)D

t,x

sup

K

1

µ2fK1 2L4

![image 59](<2014-jiang-linear-profile-decompositions-family_images/imageFile59.png>)

Sµ(t)D

t,x

M≥N

M −16 N 16 fM1 L2

![image 60](<2014-jiang-linear-profile-decompositions-family_images/imageFile60.png>)

![image 61](<2014-jiang-linear-profile-decompositions-family_images/imageFile61.png>)

x

fN1 L2

.

x

In either case, (4) follows from an application of Schur’s test.

If d > 2, then by the square function estimate, the triangle inequality, H¨older’s inequality, and the endpoint Strichartz inequality, for µ = 0,1,

d

d

d

2(d+2) d

d+2 2d

d+2

µd+2fMµ |2

µd+2fNµ|2

![image 62](<2014-jiang-linear-profile-decompositions-family_images/imageFile62.png>)

![image 63](<2014-jiang-linear-profile-decompositions-family_images/imageFile63.png>)

![image 64](<2014-jiang-linear-profile-decompositions-family_images/imageFile64.png>)

µd+2f

![image 65](<2014-jiang-linear-profile-decompositions-family_images/imageFile65.png>)

![image 66](<2014-jiang-linear-profile-decompositions-family_images/imageFile66.png>)

![image 67](<2014-jiang-linear-profile-decompositions-family_images/imageFile67.png>)

|Sµ(t)D

|Sµ(t)D

2d dxdt

∼

Sµ(t)D

2(d+2)

![image 68](<2014-jiang-linear-profile-decompositions-family_images/imageFile68.png>)

d t,x

L

N

M

d

d

d+2 d

µd+2fMµ Sµ(t)D

µd+2fNµ

![image 69](<2014-jiang-linear-profile-decompositions-family_images/imageFile69.png>)

![image 70](<2014-jiang-linear-profile-decompositions-family_images/imageFile70.png>)

![image 71](<2014-jiang-linear-profile-decompositions-family_images/imageFile71.png>)

Sµ(t)D

d+2 d t,x

![image 72](<2014-jiang-linear-profile-decompositions-family_images/imageFile72.png>)

L

M≥N

d

d

2 d

µd+2fMµ

µd+2fMµ

![image 73](<2014-jiang-linear-profile-decompositions-family_images/imageFile73.png>)

![image 74](<2014-jiang-linear-profile-decompositions-family_images/imageFile74.png>)

![image 75](<2014-jiang-linear-profile-decompositions-family_images/imageFile75.png>)

Sµ(t)D

Sµ(t)D

2(d+2)

2d d−2 x

![image 76](<2014-jiang-linear-profile-decompositions-family_images/imageFile76.png>)

![image 77](<2014-jiang-linear-profile-decompositions-family_images/imageFile77.png>)

d t,x

L2tL

L

M≥N

d

d

2 d

µd+2fNµ

µd+2fNµ

![image 78](<2014-jiang-linear-profile-decompositions-family_images/imageFile78.png>)

![image 79](<2014-jiang-linear-profile-decompositions-family_images/imageFile79.png>)

![image 80](<2014-jiang-linear-profile-decompositions-family_images/imageFile80.png>)

Sµ(t)D

× Sµ(t)D

2(d+2)

2d(d+2)

2(d+2) d−2

![image 81](<2014-jiang-linear-profile-decompositions-family_images/imageFile81.png>)

d t,x

L

![image 82](<2014-jiang-linear-profile-decompositions-family_images/imageFile82.png>)

d2+4 x

![image 83](<2014-jiang-linear-profile-decompositions-family_images/imageFile83.png>)

L

t L

2

d

2

4 d

2 d

2 d

2 d

2 d

L2x D−

L2x fNµ 1−

fMµ 1−

µd+2fKµ

µ d+2fMµ

µd+2fNµ

![image 84](<2014-jiang-linear-profile-decompositions-family_images/imageFile84.png>)

![image 85](<2014-jiang-linear-profile-decompositions-family_images/imageFile85.png>)

![image 86](<2014-jiang-linear-profile-decompositions-family_images/imageFile86.png>)

![image 87](<2014-jiang-linear-profile-decompositions-family_images/imageFile87.png>)

![image 88](<2014-jiang-linear-profile-decompositions-family_images/imageFile88.png>)

![image 89](<2014-jiang-linear-profile-decompositions-family_images/imageFile89.png>)

![image 90](<2014-jiang-linear-profile-decompositions-family_images/imageFile90.png>)

![image 91](<2014-jiang-linear-profile-decompositions-family_images/imageFile91.png>)

sup

Sµ(t)D

L2x. By Plancherel, if µ = 0,

L2x D

2(d+2) d

K

![image 92](<2014-jiang-linear-profile-decompositions-family_images/imageFile92.png>)

L

t,x M≥N

d

2(d+2) d

d

4 d

M−

µd+2fK0

![image 93](<2014-jiang-linear-profile-decompositions-family_images/imageFile93.png>)

![image 94](<2014-jiang-linear-profile-decompositions-family_images/imageFile94.png>)

µd+2f

![image 95](<2014-jiang-linear-profile-decompositions-family_images/imageFile95.png>)

![image 96](<2014-jiang-linear-profile-decompositions-family_images/imageFile96.png>)

sup

Sµ(t)D

Sµ(t)D

2(d+2) d t,x

2(d+2) d

K

![image 97](<2014-jiang-linear-profile-decompositions-family_images/imageFile97.png>)

![image 98](<2014-jiang-linear-profile-decompositions-family_images/imageFile98.png>)

L

L

t,x M≥N

while if µ = 1, Sµ(t)D

d

d

2(d+2) d

4 d

M −

µd+2fK1

![image 99](<2014-jiang-linear-profile-decompositions-family_images/imageFile99.png>)

![image 100](<2014-jiang-linear-profile-decompositions-family_images/imageFile100.png>)

µd+2f

![image 101](<2014-jiang-linear-profile-decompositions-family_images/imageFile101.png>)

![image 102](<2014-jiang-linear-profile-decompositions-family_images/imageFile102.png>)

sup

Sµ(t)D

2(d+2) d t,x

2(d+2) d

K

![image 103](<2014-jiang-linear-profile-decompositions-family_images/imageFile103.png>)

![image 104](<2014-jiang-linear-profile-decompositions-family_images/imageFile104.png>)

L

L

t,x M≥N

As in the d = 2 case, (3) follows by Schur’s test.

4

4

d(d+2) fM0 L2

d(d+2)N

![image 105](<2014-jiang-linear-profile-decompositions-family_images/imageFile105.png>)

![image 106](<2014-jiang-linear-profile-decompositions-family_images/imageFile106.png>)

x

fN0 L2

,

x

4

d(d+2) N

![image 107](<2014-jiang-linear-profile-decompositions-family_images/imageFile107.png>)

4

d(d+2) fM1 L2

![image 108](<2014-jiang-linear-profile-decompositions-family_images/imageFile108.png>)

x

fN1 L2

.

x

We now rescale one more time, to frequencies |ξ| ∼ 1. We claim that the proposition follows from the following. Lemma 2.5. Let q = 2(d

2+3d+1)

d2 . For f ∈ L2x(Rd), at scale 1 we have

![image 109](<2014-jiang-linear-profile-decompositions-family_images/imageFile109.png>)

- (6) Sε(t)P10f L

2(d+2)

![image 110](<2014-jiang-linear-profile-decompositions-family_images/imageFile110.png>)

d t,x

sup

κ

|κ|

d+2

![image 111](<2014-jiang-linear-profile-decompositions-family_images/imageFile111.png>)

dq −21 Sε(t)fκ Lq

![image 112](<2014-jiang-linear-profile-decompositions-family_images/imageFile112.png>)

t,x

1

![image 113](<2014-jiang-linear-profile-decompositions-family_images/imageFile113.png>)

d+2 f

- d+1

![image 114](<2014-jiang-linear-profile-decompositions-family_images/imageFile114.png>)

- d+2


L2x , 0 ≤ ε ≤ 1,

where the supremum is taken over caps κ = {ξ : |ξ − ξ0| < r}, with 21 ≤ |ξ0| ≤ 2 and r < 161 . Additionally, at scale 0,

![image 115](<2014-jiang-linear-profile-decompositions-family_images/imageFile115.png>)

![image 116](<2014-jiang-linear-profile-decompositions-family_images/imageFile116.png>)

- (7) S1(t)P01f L

2(d+2) d t,x

![image 117](<2014-jiang-linear-profile-decompositions-family_images/imageFile117.png>)

sup

κ

|κ|

d+2

![image 118](<2014-jiang-linear-profile-decompositions-family_images/imageFile118.png>)

dq −21 S1(t)fκ Lq

![image 119](<2014-jiang-linear-profile-decompositions-family_images/imageFile119.png>)

t,x

1

![image 120](<2014-jiang-linear-profile-decompositions-family_images/imageFile120.png>)

d+2 f

- d+1

![image 121](<2014-jiang-linear-profile-decompositions-family_images/imageFile121.png>)

- d+2


L2x ,

where the supremum is taken over caps κ = {ξ : |ξ − ξ0| < r}, with |ξ0| ≤ 1 and r < 161 .

![image 122](<2014-jiang-linear-profile-decompositions-family_images/imageFile122.png>)

Assuming the lemma for the moment, we complete the proof of Proposition 2.2. Proof of Proposition 2.2. By scaling, (6) implies that

- (8) N


- d+1

![image 123](<2014-jiang-linear-profile-decompositions-family_images/imageFile123.png>)

- d+2


1

d+2

dq −12N

2

d

d+2 SNε(t)PN0 f

![image 124](<2014-jiang-linear-profile-decompositions-family_images/imageFile124.png>)

sup

|κ|

d+2 f

q SNε(t)fκ Lq

L2x ,

![image 125](<2014-jiang-linear-profile-decompositions-family_images/imageFile125.png>)

![image 126](<2014-jiang-linear-profile-decompositions-family_images/imageFile126.png>)

![image 127](<2014-jiang-linear-profile-decompositions-family_images/imageFile127.png>)

![image 128](<2014-jiang-linear-profile-decompositions-family_images/imageFile128.png>)

2(d+2) d t,x

t,x

![image 129](<2014-jiang-linear-profile-decompositions-family_images/imageFile129.png>)

κ

L

for 0 ≤ ε 1 and N ∈ 2Z, where the supremum is taken over caps κ = {|ξ − ξ0| < r}, where N 4 ≤ |ξ0| ≤ 4N and r < 32N . We note that if µ = 0 or µ = 1 and N ≥ 1, these are µ-caps.

![image 130](<2014-jiang-linear-profile-decompositions-family_images/imageFile130.png>)

![image 131](<2014-jiang-linear-profile-decompositions-family_images/imageFile131.png>)

- In the case µ = 0, the reﬁned Strichartz estimate (3) just follows from (4) followed by (8) (with


ε = 0) and Bernstein’s inequality.

- In the case µ = 1, we ﬁrst apply (4). Then we use Bernstein’s inequality together with (7) for


the scale 0 term and (8) with ε = N1 for the scale N term. (Note that if N ∈ 2N, PN0 = PN1 .)

![image 132](<2014-jiang-linear-profile-decompositions-family_images/imageFile132.png>)

The proof of Lemma 2.5 reduces to Lemma 2.8 . The reduction is similar as in Guth [7, p. 386]. We consider a function with Fourier support in a small cap in {|ξ| ∼ 1}.

Fix 14 < |ξ0| < 4 and deﬁne σε,ξ0 = {(ε|ξ|2 + |ξ|4,ξ) : |ξ − ξ0| ≤ 3cd}.

![image 133](<2014-jiang-linear-profile-decompositions-family_images/imageFile133.png>)

Suppose that the Fourier transform f is supported on σε,ξ0. We consider 4th order Schro¨dinger operator. Let φ(ξ) = |ξ|4 + ε|ξ|2.

eix·ξ+it(|ξ|4+ε|ξ|2) f(ξ)dξ =: eitφ(|∇|)f(x),

Sε,ξ0(t)f(x) =

σε,ξ0

where x · ξ or xξ denotes the inner product of x and ξ. Then by translation invariance,

Sε,ξ0(t)f(x) = eix·ξ0+itφ(ξ0)

ei(x−t∇φ(ξ0))·(ξ−ξ0)+it(φ(ξ)−φ(ξ0)−∇φ(ξ0)·(ξ−ξ0)) f(ξ)dξ.

σε,ξ0

Let h(ξ) = φ(ξ) − φ(ξ0) − ∇φ(ξ0) · (ξ − ξ0). Then

= eith(|∇|)f

- (9) Sε,ξ0(t)f(x) L


2(d+2) d t,x

![image 134](<2014-jiang-linear-profile-decompositions-family_images/imageFile134.png>)

2(d+2) d t,x

![image 135](<2014-jiang-linear-profile-decompositions-family_images/imageFile135.png>)

L

The function h satisﬁes that h(ξ0) = 0 and ∇h(ξ0) = 0. Recall that the elliptic condition in Guth [7, Condition 2.1], see also Tao, Vargas and Vega [31]. Suppose that S ⊂ R3 is a smooth compact surface given as the graph of a function h : B(0,1) → R which satisﬁes the following conditions for some large L:

- • 0 < 12 ≤ ∇2h ≤ 2, namely, all the eigenvalues of ∇2h is comparable to 1.

![image 136](<2014-jiang-linear-profile-decompositions-family_images/imageFile136.png>)

- • 0 = h(0), ∇h(0) = 0.
- • h is CL, and
- • for 3 ≤ l ≤ L,  ∇lh C0 ≤ 10−9.


The function h is not in elliptic type. However since the Strichartz inequality is scaling-invariant, h can be normalized to satisfy the elliptic condition above by Taylor’s expansion, change of variables, and parabolic scalings, see for instance Guth [7, p. 386]. We remark that it may necessarily change the value of cd. Then the remarks in Tao [30, Section 9] applies.

- Theorem 2.6 ([30]). Let h be as above. Then the operator Eh deﬁned by


ei(t,x)·(h(ξ),ξ) f(ξ)dξ

Ehf(t,x) =

{|ξ| 1}

satisﬁes the following. Let ρ1,ρ2 ⊂ {|ξ| 1} satisfy diam(ρ1) ∼ diam(ρ2) ∼ dist(ρ1,ρ2) ∼ 1. If f1,f2 are L2x functions whose Fourier transforms are supported on ρ1,ρ2, respectively, then Ehf1) Ehf2) Lp

, p > dd+3+1, where the implicit constant depends only on d,p.

f1 L2

f2 L2

![image 137](<2014-jiang-linear-profile-decompositions-family_images/imageFile137.png>)

x

x

t,x

Taking advantage of the symmetries of the Fourier transform, we have the following corollary.

Corollary 2.7. For cd suﬃciently small, if κ1 and κ2 are two caps contained in {14 < |ξ| < 32} satisfying

![image 138](<2014-jiang-linear-profile-decompositions-family_images/imageFile138.png>)

![image 139](<2014-jiang-linear-profile-decompositions-family_images/imageFile139.png>)

diam(κ1) ∼ diam(κ2) ∼ dist(κ1,κ2) ∼ r < cd, then for any f ∈ L2x and p > dd+3+1,

![image 140](<2014-jiang-linear-profile-decompositions-family_images/imageFile140.png>)

d + 3 d + 1

d+2

t,x d,p rd−

p fκ1 L2

fκ2 L2

, p >

Ehfκ1 Ehfκ2 Lp

.

![image 141](<2014-jiang-linear-profile-decompositions-family_images/imageFile141.png>)

![image 142](<2014-jiang-linear-profile-decompositions-family_images/imageFile142.png>)

x

x

Then the following reﬁned Strichartz estimate follows similarly as in Be´gout and Vargas [2], see also Proposition 4.23 of Killip and Visan [21].

2+3d+1)

- Lemma 2.8. Let q = 2(d


d2 . If f ∈ L2x and Fourier supported in a cap σε,ξ0 of size cd in the annulus {|ξ| ∼ 1}, then

![image 143](<2014-jiang-linear-profile-decompositions-family_images/imageFile143.png>)

- (10) Sε,ξ0(t)f L

2(d+2) d t,x

![image 144](<2014-jiang-linear-profile-decompositions-family_images/imageFile144.png>)

sup

κ

|κ|

d+2

![image 145](<2014-jiang-linear-profile-decompositions-family_images/imageFile145.png>)

dq −21 Sε,ξ0(t)fκ Lq

![image 146](<2014-jiang-linear-profile-decompositions-family_images/imageFile146.png>)

t,x

1

![image 147](<2014-jiang-linear-profile-decompositions-family_images/imageFile147.png>)

d+2 f

- d+1

![image 148](<2014-jiang-linear-profile-decompositions-family_images/imageFile148.png>)

- d+2


L2x , where the supremum may be taken over caps κ with

- (11) κ ⊂ {|ξ| ∼ 1} and diam(κ) < .01.

Now we are ready to prove Lemma 2.5 by a decomposition of unit of {|ξ| ∼ 1} into many caps with diameters comparable to cd. The cardinality of these caps depends on the spatial dimension only. More precisely, we recall that P10f = ψ10 f, where ψ10 is supported on {12 ≤ |ξ| ≤ 2}. There exists a ﬁnite decomposition

![image 149](<2014-jiang-linear-profile-decompositions-family_images/imageFile149.png>)

- (12) ψ10 =

Cd

j=1

ψ1,j,

with ψ1,j = ψ10φj, for smooth bump functions φj : Rd → [0,1] whose supports have diameter equal to a small dimensional constant cd’ Cd > 0 depends on d only.

- By (12), for any f ∈ L2x,

(13) P10f =

Cd

j=1

f1,j, where f1,j = ψ1,j f, i = 1,2.

- By (13) and the triangle inequality,


- (14) Sε(t)f1 L


Cd

Sε(t)f1,j

≤

≤ Cd max

Sε(t)f1,j

2(d+2) d t,x

2(d+2) d t,x

j

![image 150](<2014-jiang-linear-profile-decompositions-family_images/imageFile150.png>)

![image 151](<2014-jiang-linear-profile-decompositions-family_images/imageFile151.png>)

L

j=1

.

2(d+2) d t,x

![image 152](<2014-jiang-linear-profile-decompositions-family_images/imageFile152.png>)

L

The proof of Lemma 2.5. Since |ψ1,j| ≤ 1, by Plancherel, f1,j L2

. Furthermore, we have Sε(t)[(f1,j)κ] = (Sε(t)fκ)1,j. By construction, ψ ˇ1,j L1

≤ f L2

x

x

1, so by Young’s convolution inequality (in the x-variable), Sε(t)(f1,j)κ Lq

x

Sε(t)fκ Lq

. So ﬁnally, by combining (14) and (10), we obtain (6). The inequality (7) follows in a similar manner (but is simpler because there is no ε). Therefore Lemma 2.5 is proved.

t,x

t,x

3. Linear profile decomposition

- Theorem 3.1 (Linear proﬁle decomposition). Let (un)n≥1 be a bounded sequence of L2x functions. After passing to a subsequence, the following hold. For each j ≥ 1 there exist φj ∈ L2x, a sequence


of parameters (hjn,ξnj ,xjn,tjn) ∈ (0,∞) × Rd × Rd × R, and a sequence of L2x errors (wnl )l,n≥1 such that for each l ≥ 1,

- (15) un =

l

j=1

Sµ(−tjn)gnj [ei(·)h

j

nξnj φj] + wnl ,

where gnj (φ) := (hj1

![image 153](<2014-jiang-linear-profile-decompositions-family_images/imageFile153.png>)

n)d/2φ(x−x

j n

![image 154](<2014-jiang-linear-profile-decompositions-family_images/imageFile154.png>)

hjn ), and for each j, either |hjnξnj| → ∞ or ξnj ≡ 0. The errors satisfy

- (16) limsup l→∞

limsup

n→∞

Dµ1/2Sµ(t)wnl

L

2(d+2) d

![image 155](<2014-jiang-linear-profile-decompositions-family_images/imageFile155.png>)

t,x (R×Rd)

= 0.

For j = k, (hjn,ξnj,xjn,tjn)n≥1 and (hkn,ξnk,xkn,tkn)n≥1 are pairwise orthogonal in the sense that

- (17)

lim

n→∞

hjn hkn

![image 156](<2014-jiang-linear-profile-decompositions-family_images/imageFile156.png>)

+

hkn hjn

![image 157](<2014-jiang-linear-profile-decompositions-family_images/imageFile157.png>)

+ |hjnξnj − hknξnk| + |tkn − tjn| (hjn)4

![image 158](<2014-jiang-linear-profile-decompositions-family_images/imageFile158.png>)

+ |tkn − tjn|(µ + 2|ξnj |2) (hjn)2

![image 159](<2014-jiang-linear-profile-decompositions-family_images/imageFile159.png>)

+ |xjn − xkn + 2(tjn − tkn)(2|ξnj |2 + µ)ξnj| hjn

![image 160](<2014-jiang-linear-profile-decompositions-family_images/imageFile160.png>)

= ∞.

Furthermore, if limn→∞(h

j n

![image 161](<2014-jiang-linear-profile-decompositions-family_images/imageFile161.png>)

hkn + h

k n

![image 162](<2014-jiang-linear-profile-decompositions-family_images/imageFile162.png>)

hjn) = ∞, then hjn = hkn for all n, and if limn→∞ |hknξnk −hjnξnj| = ∞, then hjnξnj = hknξnk for all n. Finally, for each l ≥ 1,

- (18) lim

n→∞

un 2L2

x

− (

l

j=1

φj 2L2

x

+ wnl 2L2

x

) = 0

The orthogonality condition of parameters implies the following. Proposition 3.2 (Orthogonality of proﬁles). For j = k, along the subsequence satisfying (17),

- (19) lim n→∞

D

d

![image 163](<2014-jiang-linear-profile-decompositions-family_images/imageFile163.png>)

µd+2Sµ(t)Sµ(−tjn)gnj [ei(·)h

j

nξnj φj] D

d

![image 164](<2014-jiang-linear-profile-decompositions-family_images/imageFile164.png>)

µd+2Sµ(t)Sµ(−tkn)gnk[ei(·)hknξnkφk]

L

d+2 d t,x

![image 165](<2014-jiang-linear-profile-decompositions-family_images/imageFile165.png>)

= 0.

Thus by (16),

- (20) lim l→∞

limsup

n→∞

D

d

![image 166](<2014-jiang-linear-profile-decompositions-family_images/imageFile166.png>)

µd+2Sµ(t)un

2(d+2) d

![image 167](<2014-jiang-linear-profile-decompositions-family_images/imageFile167.png>)

L

2(d+2) d t,x

![image 168](<2014-jiang-linear-profile-decompositions-family_images/imageFile168.png>)

−

l

j=1

D

d

![image 169](<2014-jiang-linear-profile-decompositions-family_images/imageFile169.png>)

µd+2Sµ(t − tjn)gnj [ei(·)h

j

nξnj φj]

2(d+2) d

![image 170](<2014-jiang-linear-profile-decompositions-family_images/imageFile170.png>)

L

2(d+2) d t,x

![image 171](<2014-jiang-linear-profile-decompositions-family_images/imageFile171.png>)

= 0.

We begin with the linear proﬁle decomposition.

Proof of Theorem 3.1. The proof follows a familiar outline (cf. [1, 4, 9]). We construct the linear proﬁle decomposition inductively. At each stage we will pass to a further subsequence, but to avoid a proliferation of sub- and superscripts, we will denote each subsequence by (un). For each n,j, let Bnj denote the L2x isometry

Bnj = Sµ(−tjn)gnj ei(·)h

j

nξnj .

Set wn0 = un and assume that for some l ≥ 0 we have found a subsequence of (un), L2x functions φj, and sequences (hjn,ξnj,xjn,tjn), 1 ≤ j ≤ l such that for all 1 ≤ k ≤ l, we have the following: (18) holds (with k in place of l); (17) holds for all k = j ∈ {1,... ,l}; either |hknξnk| → ∞ or ξnk ≡ 0;

un =

k

j=1

- (21) Bnjφj + wnk;
- (22) (Bnk)−1wnk−1 ⇀ φk, weakly in L2x.


Deﬁne

d

Al = limsup

wnl L2

, εl = limsup

µd+2Sµ(t)wnl

![image 172](<2014-jiang-linear-profile-decompositions-family_images/imageFile172.png>)

. By the Strichartz inequality, εl Al. If εl = 0, then we are done, so we may assume that εl > 0. Passing to a subsequence, we may assume that wnl L2

D

2(d+2)

x

![image 173](<2014-jiang-linear-profile-decompositions-family_images/imageFile173.png>)

n→∞

n→∞

d t,x

L

d

∼ εl, for all n.

∼ Al and D

µd+2Sµ(t)wnl

![image 174](<2014-jiang-linear-profile-decompositions-family_images/imageFile174.png>)

2(d+2) d t,x

x

![image 175](<2014-jiang-linear-profile-decompositions-family_images/imageFile175.png>)

L

By Proposition 2.2 and a little arithmetic, there exists a sequence (κn) of µ-caps such that for all suﬃciently large n,

- (23) Al A εll

![image 176](<2014-jiang-linear-profile-decompositions-family_images/imageFile176.png>)

1

![image 177](<2014-jiang-linear-profile-decompositions-family_images/imageFile177.png>)

θ |κn|

d+2

![image 178](<2014-jiang-linear-profile-decompositions-family_images/imageFile178.png>)

dq −12 Sµ(t)D

![image 179](<2014-jiang-linear-profile-decompositions-family_images/imageFile179.png>)

2 q µ (wnl )κn Lq

![image 180](<2014-jiang-linear-profile-decompositions-family_images/imageFile180.png>)

t,x

.

By H¨older’s inequality, Bernstein’s inequality (since (wnl )κn is frequency localized), and Young’s convolution inequality (since φκ L1

x

∼ 1),

Sµ(t)D

2 q µ(wnl )κn Lq

![image 181](<2014-jiang-linear-profile-decompositions-family_images/imageFile181.png>)

t,x

Sµ(t)D

d

![image 182](<2014-jiang-linear-profile-decompositions-family_images/imageFile182.png>)

µd+2(wnl )κn

2(d+2) dq

![image 183](<2014-jiang-linear-profile-decompositions-family_images/imageFile183.png>)

L

2(d+2)

![image 184](<2014-jiang-linear-profile-decompositions-family_images/imageFile184.png>)

d t,x

Sµ(t)(wnl )κn 1−

2(d+2) dq L∞t,x

![image 185](<2014-jiang-linear-profile-decompositions-family_images/imageFile185.png>)

(Al)

2(d+2)

![image 186](<2014-jiang-linear-profile-decompositions-family_images/imageFile186.png>)

dq Sµ(t)(wnl )κn 1−

2(d+2) dq

![image 187](<2014-jiang-linear-profile-decompositions-family_images/imageFile187.png>)

L∞t,x .

Combining this with (23) and the fact that (wnl )κn is smooth (since it has compact Fourier support), there exist parameters (xn,tn) such that

- (24) Al A εll θ

![image 188](<2014-jiang-linear-profile-decompositions-family_images/imageFile188.png>)

′

|κn|−1

![image 189](<2014-jiang-linear-profile-decompositions-family_images/imageFile189.png>)

2

|Sµ(tn)(wnl )κn(xn)|, where θ′ = 1θ.

![image 190](<2014-jiang-linear-profile-decompositions-family_images/imageFile190.png>)

Write κn = {ξ : |ξ − ξn| < h−n1}, and set

(hln+1,ξnl+1,xln+1,tln+1) = (hn,ξn,xn,tn). The sequence

(Bnl+1)−1wnl = e−ixhnξngn−1Sµ(tn)wnl is bounded in L2x, so after passing to a subsequence, we may extract a weak limit; say

- (25) (Bnl+1)−1wnl ⇀ φl+1, weakly in L2x. Thus we have
- (26)


− wnl − Bnl+1φl+1 2L2

− φl+1 2L2

wnl 2L2

lim

n→∞

x

x

x

2 (Bnl+1)−1wnl ,φl+1 − 2 φl+1 2L2

= 0, which implies that (18) holds with l replaced by l + 1 and

= lim

n→∞

x

wnl+1 = wnl − Bnl+1φl+1. In addition, by (24), the deﬁnition of (wnl )κn, and a quick computation,

d

Al A εll)θ′ h−

n 2| eixnξeitn(|ξ|4+µ|ξ|2)φ(hn(ξ − ξn)) wnl (ξ)dξ|

![image 191](<2014-jiang-linear-profile-decompositions-family_images/imageFile191.png>)

![image 192](<2014-jiang-linear-profile-decompositions-family_images/imageFile192.png>)

= | e−i(·)hnξngn−1Sµ(tn)wnl ,φˇ |. Taking the limit as n → ∞,

Al A εll)θ′ | φl+1,φ | φl+1 L2

,

![image 193](<2014-jiang-linear-profile-decompositions-family_images/imageFile193.png>)

x

so by (26),

- (27) limsup


n→∞

![image 194](<2014-jiang-linear-profile-decompositions-family_images/imageFile194.png>)

′

≤ Al 1 − c A εll 2θ

wnl+1 L2

.

![image 195](<2014-jiang-linear-profile-decompositions-family_images/imageFile195.png>)

x

Thus by the Strichartz inequality, after iterating, we obtain (16). (Indeed for (16) to fail, εl must stay large, but in this case (27) implies that Al must decrease to 0, a contradiction to the Strichartz inequality.)

By changing φl+1 if necessary, we may assume that either |hln+1ξnl+1| → ∞ or ξnl+1 ≡ 0. Indeed, if |hln+1ξnl+1|  → ∞, after passing to a subsequence, hln+1ξnl+1 → ξ0 ∈ Rd, and so we may replace φl+1 with eixξ0φl+1 and ξnl+1 with 0. Similar arguments justify the assertions that for each k < l + 1, either h

l+1 n

k n

hln+1 + h

hkn → ∞ or hkn ≡ hln+1 and that either |hknξnk −hln+1ξnl+1| → ∞ or hknξnk ≡ hln+1ξnl+1. Finally, we turn to (17). The crux of the argument will be the following.

![image 196](<2014-jiang-linear-profile-decompositions-family_images/imageFile196.png>)

![image 197](<2014-jiang-linear-profile-decompositions-family_images/imageFile197.png>)

- Lemma 3.3. If the limit in (17) is inﬁnite, (Bnk)−1Bnj → 0 in the weak operator topology on B(L2x). Otherwise, after passing to a subsequence, there exists an L2x isometry Bkj such that (Bnk)−1Bnj → Bkj in the strong operator topology on B(L2x). Proof. Let Bnkj = (Bnk)−1Bnj. It suﬃces to prove that if the limit in (17) is inﬁnite,


Bnkjφ,ψ = 0,

lim

n→∞

for all Schwartz functions φ,ψ with compact frequency support, and that otherwise after passing to a subsequence, Bnkjφ → Bkjφ in L2x for all φ ∈ L2x.

A simple computation shows that

k n

x ≤ h

Bnkjφ L∞

![image 198](<2014-jiang-linear-profile-decompositions-family_images/imageFile198.png>)

hjn

d

j n

x ≤ h

, (Bnkj)−1ψ L∞

![image 199](<2014-jiang-linear-profile-decompositions-family_images/imageFile199.png>)

2 φ L1

![image 200](<2014-jiang-linear-profile-decompositions-family_images/imageFile200.png>)

hkn

ξ

d

![image 201](<2014-jiang-linear-profile-decompositions-family_images/imageFile201.png>)

.

2 ψ L1

ξ

By H¨older’s inequality, and Plancherel,

k n

| Bnkjφ,ψ | min{ h

![image 202](<2014-jiang-linear-profile-decompositions-family_images/imageFile202.png>)

hjn

d

![image 203](<2014-jiang-linear-profile-decompositions-family_images/imageFile203.png>)

2 φ L1

ξ

j n

, h

ψ L∞

![image 204](<2014-jiang-linear-profile-decompositions-family_images/imageFile204.png>)

hkn

ξ

d

![image 205](<2014-jiang-linear-profile-decompositions-family_images/imageFile205.png>)

2 ψ L1

ξ

},

φ L∞

ξ

j n

k n

and since φ,ψ are Schwartz, if h

hjn + h

hkn → ∞, the right hand side of the above inequality tends to 0. Thus we may henceforth assume that hjn ≡ hkn ≡ hn.

![image 206](<2014-jiang-linear-profile-decompositions-family_images/imageFile206.png>)

![image 207](<2014-jiang-linear-profile-decompositions-family_images/imageFile207.png>)

Now assume that |hnξnk − hnξnj| → ∞. By assumption, φ, ψ have compact support; say Supp φ,Supp ψ ⊂ {|ξ| ≤ R}. Then

Supp Bnjφ ⊂ {|ξ − ξnj| < h−n1R}, Supp Bnkψ ⊂ {|ξ − ξnk| < h−n1R}. For suﬃciently large n, these sets are disjoint, so

Bnkjφ,ψ = Bnjφ, Bnkψ → 0. Thus we may assume that ξnj ≡ ξnk ≡ ξn.

With these assumptions in place, we compute

Bnkjφ = ωnkjTnkjSnkjRnkjPnkjφ,

where

ωnkj = exp[i(ξn(xkn − xjn) + (tkn − tjn)(|ξn|4 + µ|ξn|2))], Tnkjψ(x) = ψ(x + x

k n−xjn+(tkn−tjn)(4|ξn|2ξn+2µξn)

hn ), Snkjψ = exp[i(xξ + t

![image 208](<2014-jiang-linear-profile-decompositions-family_images/imageFile208.png>)

k n−tjn

h2n (2|ξ|2|ξn|2 + 4(ξξn)2 + µ|ξ|2))] ψ(ξ)dξ, Rnkjψ(x) = exp[i(xξ + 4(t

![image 209](<2014-jiang-linear-profile-decompositions-family_images/imageFile209.png>)

k n−tjn)

- h3n |ξ|2ξξn)] ψ(ξ)dξ,

Pnkjψ = exp[i(t

k n−tjn)

![image 210](<2014-jiang-linear-profile-decompositions-family_images/imageFile210.png>)

- h4n ∆2]ψ.


![image 211](<2014-jiang-linear-profile-decompositions-family_images/imageFile211.png>)

After passing to a subsequence, ωnkj → ω ∈ S1, so Bnjkφ − ωTnkjSnkjRnkjPnkjφ → 0 in L2x. Thus it suﬃces to show that the conclusions of the lemma hold for TnkjSnkjRnkjPnkj instead of Bnkj.

We write

kj

TnkjSnkjRnkjPnkjφ(x) = eiΦ

n (x,ξ) φ(ξ)dξ, where

(tkn − tjn)|ξ|4 h4n

xkn − xjn + (tkn − tjn)(4|ξn|2ξn + 2µξn) hn

Φkjn (x,ξ) = ξ · x +

+

![image 212](<2014-jiang-linear-profile-decompositions-family_images/imageFile212.png>)

![image 213](<2014-jiang-linear-profile-decompositions-family_images/imageFile213.png>)

4(tkn − tjn)|ξ|2ξnξ h3n

(tkn − tjn)(2|ξn|2|ξ|2 + 4(ξnξ)2 + µ|ξ|2) h2n

+

.

+

![image 214](<2014-jiang-linear-profile-decompositions-family_images/imageFile214.png>)

![image 215](<2014-jiang-linear-profile-decompositions-family_images/imageFile215.png>)

k n−tjn)

Φkjn (x,ξ) = 24(t

Since ∂ξ4

h4n , by the method of stationary phase ([29, Chapter VIII.2.2]), |TnkjSnkjRnkjPnkjφ(x)| (1 + |t

![image 216](<2014-jiang-linear-profile-decompositions-family_images/imageFile216.png>)

1

k n−tjn|

h4n )−14. Thus if |t

![image 217](<2014-jiang-linear-profile-decompositions-family_images/imageFile217.png>)

![image 218](<2014-jiang-linear-profile-decompositions-family_images/imageFile218.png>)

k n−tjn|

k n−tjn|

h4n → ∞, TnkjSnkjRnkjPnkjφ ⇀ 0, weakly in L2x. Thus we may assume that |t

h4n  → ∞. Passing to a subsequence, t

![image 219](<2014-jiang-linear-profile-decompositions-family_images/imageFile219.png>)

![image 220](<2014-jiang-linear-profile-decompositions-family_images/imageFile220.png>)

k n−tjn

h4n → skj, so Pnkjφ − eiskj∆2φ L2

![image 221](<2014-jiang-linear-profile-decompositions-family_images/imageFile221.png>)

→ 0,

x

for every φ ∈ L2x. Thus it suﬃces to show that the conclusions of the lemma hold for TnkjSnkjRnkj instead of Bnkj.

Passing to a subsequence, either ξn ≡ 0 or |ξξn

n| → ξ0 ∈ Sd−1. The case when ξn ≡ 0 is much easier, so we assume henceforth that |ξξn

![image 222](<2014-jiang-linear-profile-decompositions-family_images/imageFile222.png>)

n| → ξ0 ∈ Sd−1. Passing to a further subsequence, 0 < ξn · ξ0 ∼ |ξn| for all n. We write

![image 223](<2014-jiang-linear-profile-decompositions-family_images/imageFile223.png>)

kj

TnkjSnkjRnkjφ(x) = eiΦ

n (x,ξ) ψ(x)dξ, where now we set

xkn − xjn + (tkn − tjn)(4|ξn|2ξn + 2µξn) hn

Φkjn (x,ξ) = ξ · x +

+

![image 224](<2014-jiang-linear-profile-decompositions-family_images/imageFile224.png>)

4(tkn − tjn)|ξ|2ξnξ h3n

(tkn − tjn)(2|ξn|2|ξ|2 + 4(ξnξ)2 + µ|ξ|2) h2n

. Since

+

+

![image 225](<2014-jiang-linear-profile-decompositions-family_images/imageFile225.png>)

![image 226](<2014-jiang-linear-profile-decompositions-family_images/imageFile226.png>)

k n−tjn)|ξn|

k n−tjn||ξn|

|(ξ0 · ∇ξ)3Φkjn (x,ξ)| = |24(t

ξnξ0 |ξn| | ∼ |t

h3n ,

![image 227](<2014-jiang-linear-profile-decompositions-family_images/imageFile227.png>)

![image 228](<2014-jiang-linear-profile-decompositions-family_images/imageFile228.png>)

![image 229](<2014-jiang-linear-profile-decompositions-family_images/imageFile229.png>)

h3n

k n−tjn||ξn|

if |t

h3n → ∞, by stationary phase (as above), TnkjSnkjRnkjφ L∞

x → 0, so TnkjSnkjRnkjφ ⇀ 0, weakly in L2x. Otherwise, as above, after passing to a subsequence, Rnkjφ → Rkjφ in L2x, for some unitary operator Rkj. Thus it suﬃces to consider TnkjSnkj.

![image 230](<2014-jiang-linear-profile-decompositions-family_images/imageFile230.png>)

k n−tjn|(2|ξn|2+µ)

Similar arguments show that TnkjSnkjφ ⇀ 0, weakly in L2x if |t

h2n → ∞, so we may assume that this term is bounded, and after passing to a subsequence, Snkjφ → Skjφ in L2x. This reduces matters to proving that the conclusions of the lemma hold for Tnkj, and since Tnkj is just a translation, elementary arguments show that if |x

![image 231](<2014-jiang-linear-profile-decompositions-family_images/imageFile231.png>)

k n−xjn+(tkn−tjn)(4|ξn|2ξn+2µξn)|

hn → ∞, then Tnkjφ ⇀ 0, weakly in L2x and if x

![image 232](<2014-jiang-linear-profile-decompositions-family_images/imageFile232.png>)

k n−xjn+(tkn−tjn)(4|ξn|2ξn+2µξn)

hn → ykj ∈ Rd, then Tnkjφ → φ(· + ykj) in L2x. This completes the proof of the lemma.

![image 233](<2014-jiang-linear-profile-decompositions-family_images/imageFile233.png>)

Now we complete the proof of the linear proﬁle decomposition by showing that (17) holds for all 1 ≤ k < j = l + 1. Suppose (17) failed for some 1 ≤ k < j = l + 1. Then

((Bnk)−1wnk−1 − φk) = wk-lim

(Bnk)−1wnk

0 = wk-lim

n→∞

n→∞

(Bnk)−1 Bnk+1φk+1 + ··· + Bnl φl + wnl ]. We have assumed that (17) holds for all k < j ≤ l, so by Lemma 3.3,

= wk-lim

n→∞

(Bnk)−1 Bnk+1φk+1 + ··· + Bnl φl] = 0, which implies that

wk-lim

n→∞

(Bnk)−1wnl = 0.

wk-lim

n→∞

On the other hand, by Lemma 3.3, there exists a unitary operator Bl+1,k such that after passing to a subsequence, (Bnl+1)−1Bnk → Bl+1,k in the strong operator topology on L2x; thus for any test function ψ,

(Bl+1,k)−1φl+1,ψ = φl+1,Bl+1,kψ = lim

Bnl+1wnl ,Bl+1,kψ

n→∞

Bnl+1wnl ,(Bnl+1)−1Bnkψ = lim

(Bnk)−1wnl ,ψ = 0.

= lim

n→∞

n→∞

Since Bl+1,k is unitary and φl+1  ≡ 0, this is a contradiction. Thus (17) must hold for all 1 ≤ k < j ≤ l + 1, and this completes the proof of Theorem 3.1.

Next we prove Proposition 3.2. Proof of Proposition 3.2. Since

d

j

nξnj ψ]

µd+2Sµ(t)Sµ(−tjn)gnj [ei(·)h

![image 234](<2014-jiang-linear-profile-decompositions-family_images/imageFile234.png>)

ψ  → D

2(d+2) d

is a bounded linear operator from L2x → L

![image 235](<2014-jiang-linear-profile-decompositions-family_images/imageFile235.png>)

t,x , with operator norm bounded by a constant independent of µ, hjn, ξnj, xjn, tjn, by standard approximation arguments, it suﬃces to prove (19) for φj and φk lying in some dense subclass of L2x. We will assume henceforth that they are Schwartz functions whose Fourier transforms are supported on a compact set that does not contain 0.

d

![image 236](<2014-jiang-linear-profile-decompositions-family_images/imageFile236.png>)

µd+2Sµ(t)ei(·)aψ(x)|.

Our proof will use the following pointwise upper bounds for |D

- Lemma 3.4. Fix µ ≥ 0 and let ψ be a Schwartz function with compact frequency support that


2(d+2) d

![image 237](<2014-jiang-linear-profile-decompositions-family_images/imageFile237.png>)

t,x function v = vψ, depending only on ψ, such that

does not contain 0. There exists an L

d

d

![image 238](<2014-jiang-linear-profile-decompositions-family_images/imageFile238.png>)

µd+2Sµ(t)ψ(x)| ≤ (1 + µ)

- (28) |D


2(d+2)v((1 + µ)t,x),

![image 239](<2014-jiang-linear-profile-decompositions-family_images/imageFile239.png>)

and such that if |a| ≫ max{ ξ : ξ ∈ Supp ψ},

- (29) |D

d

![image 240](<2014-jiang-linear-profile-decompositions-family_images/imageFile240.png>)

µd+2Sµ(t)ei(·)aψ(x)| ≤ (2|a|2 + µ)

d

![image 241](<2014-jiang-linear-profile-decompositions-family_images/imageFile241.png>)

2(d+2)v((2|a|2 + µ)t,x + (4|a|2 + 2µ)at)

- Proof of Lemma 3.4. We give the details for the second case, when |a| ≫ max{ ξ : ξ ∈ Supp ψ}. The case when a = 0 is similar, but a little simpler.


Consider the function wa,µ(ξ) =

√ √µ+|ξ+a|2

![image 242](<2014-jiang-linear-profile-decompositions-family_images/imageFile242.png>)

![image 243](<2014-jiang-linear-profile-decompositions-family_images/imageFile243.png>)

![image 244](<2014-jiang-linear-profile-decompositions-family_images/imageFile244.png>)

µ+2|a|2

d

![image 245](<2014-jiang-linear-profile-decompositions-family_images/imageFile245.png>)

d+2. Then wa,µ and all of its derivatives are

bounded on the support of ψ, uniformly in a and µ. This follows from a simple induction argument and the fact that

cψ ≤ |ξ + a| ≤ µ + |ξ + a|2 ≤ µ + |a|2 + |ξ| ≤ 2 µ + 2|a|2, for all ξ ∈ Supp ψ.

![image 246](<2014-jiang-linear-profile-decompositions-family_images/imageFile246.png>)

![image 247](<2014-jiang-linear-profile-decompositions-family_images/imageFile247.png>)

![image 248](<2014-jiang-linear-profile-decompositions-family_images/imageFile248.png>)

Fix x and deﬁne y = x + t(4|a|2a + 2µa). Then |D

d

![image 249](<2014-jiang-linear-profile-decompositions-family_images/imageFile249.png>)

µd+2Sµ(t)ei(·)aψ(x)| = (µ + 2|a|2)

d 2(d+2)

![image 250](<2014-jiang-linear-profile-decompositions-family_images/imageFile250.png>)

Rd

ei(xξ+t(|ξ|4+µ|ξ|2)wa,µ(ξ − a) ψ(ξ − a)dξ

= (µ + 2|a|2)

d 2(d+2)

![image 251](<2014-jiang-linear-profile-decompositions-family_images/imageFile251.png>)

Rd

- (30) ei(yξ+t(|ξ|4+4|ξ|2ξa+2|ξ|2|a|2+4(ξa)2+µ|ξ|2)wa,µ(ξ) ψ(ξ)dξ .

Deﬁne Φ = Φt,y,a,µ by

Φ(ξ) = yξ + t(|ξ|4 + 4|ξ|2ξ · a + 2|ξ|2|a|2 + 4(ξa)2 + µ|ξ|2). We compute the gradient and Hessian of Φ:

- (31) ∇Φ(ξ) = y + t(4|ξ|2ξ + 8(ξa)ξ + 4|ξ|2a + 4|a|2ξ + 8(ξa)a + 2µξ),
- (32) HΦ = Φij(ξ) = t 8ξiξj + 4|ξ|2δij + 8ξiaj + 8(ξa)δij + 8aiξj + 4|a|2δij + 8aiaj + 2µδij ,

where δij equals 1 if i = j and 0 otherwise.

We now prove the estimate (29) by standard techniques from harmonic analysis (see Stein [29, Chapter 8]). By H¨older’s inequality and (30),

- (33) |D

d

![image 252](<2014-jiang-linear-profile-decompositions-family_images/imageFile252.png>)

µd+2Sµ(t)ei(·)aψ(x)| ≤ (µ + 2|a|2)

d

![image 253](<2014-jiang-linear-profile-decompositions-family_images/imageFile253.png>)

2(d+2) wa,µ L∞

ξ

ψ L1

ξ

(µ + 2|a|2)

d

![image 254](<2014-jiang-linear-profile-decompositions-family_images/imageFile254.png>)

2(d+2), for all (t,x) ∈ R1+d.

On the support of ψ, 4|ξ|2ξ + 8(ξa)ξ + 4|ξ|2a + 4|a|2ξ + 8(ξa)a + 2µξ µ + 2|a|2,

so if (µ + 2|a|2)|t| ≪ |y|, |∇Φ(ξ)| |y| throughout the support of ψ. Therefore for any N ≥ 1, integrating by parts N times in the right side of (30),

- (34) |D

d

![image 255](<2014-jiang-linear-profile-decompositions-family_images/imageFile255.png>)

µd+2Sµ(t)ei(·)aψ(x)| ≤ Cψ,N(µ + 2|a|2)

d

![image 256](<2014-jiang-linear-profile-decompositions-family_images/imageFile256.png>)

2(d+2) 1 1+|y|

![image 257](<2014-jiang-linear-profile-decompositions-family_images/imageFile257.png>)

N, whenever (µ + 2|a|2)|t| ≪ |y|.

If (µ + 2|a|2)|t| |y|, then ∇Φ may vanish on the support of ψ, so we examine the Hessian of

Φ. Since |a| ≫ ξ for all ξ ∈ Supp ψ, t−1HΦ(ξ) ≥ cψ(µ + 2|a|2) (i.e. t−1HΦ − cψ(µ + 2|a|2) is a positive deﬁnite matrix). Thus by stationary phase

- (35) |D


d

−d2, whenever (µ + 2|a|2)|t| |y|.

d

µd+2Sµ(t)ei(·)aψ(x)| ≤ Cψ(µ + 2|a|2)

2(d+2) 1 1+(µ+2|a|2)|t|

![image 258](<2014-jiang-linear-profile-decompositions-family_images/imageFile258.png>)

![image 259](<2014-jiang-linear-profile-decompositions-family_images/imageFile259.png>)

![image 260](<2014-jiang-linear-profile-decompositions-family_images/imageFile260.png>)

![image 261](<2014-jiang-linear-profile-decompositions-family_images/imageFile261.png>)

Combining (33), (34), and (35), and recalling the deﬁnition of y, (28) holds with v(s,y) = Cψ 1+ 1|y|

d

d

2χ|y|≫|s| + 1+ 1|s|

![image 262](<2014-jiang-linear-profile-decompositions-family_images/imageFile262.png>)

![image 263](<2014-jiang-linear-profile-decompositions-family_images/imageFile263.png>)

2χ|y| |s| , and it is easy to check that v ∈ L

![image 264](<2014-jiang-linear-profile-decompositions-family_images/imageFile264.png>)

![image 265](<2014-jiang-linear-profile-decompositions-family_images/imageFile265.png>)

2(d+2)

![image 266](<2014-jiang-linear-profile-decompositions-family_images/imageFile266.png>)

s,yd . This completes the proof of Lemma 3.4.

Now we return to estimating the quantity in (19), where we recall that may assume that φk,φj are Schwartz functions with compact frequency supports that do not contain zero. We will use two families of L

2(d+2) d

![image 267](<2014-jiang-linear-profile-decompositions-family_images/imageFile267.png>)

t,x isometries: Gjnu(t,x) = (hjn)−

d(d+4)

j n

j n

(hjn)4, x−x

2(d+2)u( t−t

hjn ),

![image 268](<2014-jiang-linear-profile-decompositions-family_images/imageFile268.png>)

![image 269](<2014-jiang-linear-profile-decompositions-family_images/imageFile269.png>)

![image 270](<2014-jiang-linear-profile-decompositions-family_images/imageFile270.png>)

d

(1 + µ)

2(d+2)u((1 + µ)t,x), if a = 0 (2|a|2 + µ)

![image 271](<2014-jiang-linear-profile-decompositions-family_images/imageFile271.png>)

La,µu(t,x) =

d

2(d+2)u((2|a|2 + µ)t,x + (4|a|2 + 2µ)at), if a = 0.

![image 272](<2014-jiang-linear-profile-decompositions-family_images/imageFile272.png>)

If we consider ajn = hjnξnj, after passing to a subsequence, either ajn = 0 for all n, or |ajn| ≫ max{ ξ : ξ ∈ Supp φj} for all n. In either case, we can apply Lemma 3.4 once we move the translation/scaling isometries across the diﬀerential operators:

d

d d+2

j

nξnj φj](x)| = |GjnD

j

µd+2Sµ(t − tjn)gnj [ei(·)h

nφj](x)| ≤ GjnLaj

(t)[ei(·)a

![image 273](<2014-jiang-linear-profile-decompositions-family_images/imageFile273.png>)

![image 274](<2014-jiang-linear-profile-decompositions-family_images/imageFile274.png>)

|D

µjn Sµj

n

n,µjnvj(t,x), and similarly,

d

µd+2Sµ(t − tkn)gnk[ei(·)hknξnkφk](x)| ≤ GknLak

n,µknvk(t,x), where vj ∈ L

![image 275](<2014-jiang-linear-profile-decompositions-family_images/imageFile275.png>)

|D

2(d+2) d

t,x , ajn = hjnξnj, µjn = (hjn)2µ, and similarly with j replaced by k. The proof of the proposition will thus be complete once we prove the following.

![image 276](<2014-jiang-linear-profile-decompositions-family_images/imageFile276.png>)

2(d+2) d

- Lemma 3.5. If vj,vk are any L


![image 277](<2014-jiang-linear-profile-decompositions-family_images/imageFile277.png>)

t,x functions and the orthogonality condition (17) holds, then

- (36) lim

n→∞

[GjnLaj

n,µjnvj][GknLak

n,µknvk]

L

d+2 d t,x

![image 278](<2014-jiang-linear-profile-decompositions-family_images/imageFile278.png>)

= 0.

- Proof of Lemma 3.5. Since the G(n·) and La,µ operators are uniformly bounded on L


2(d+2) d

![image 279](<2014-jiang-linear-profile-decompositions-family_images/imageFile279.png>)

t,x , it sufﬁces to prove this for vj and vk lying in some dense subclass of L

2(d+2) d

![image 280](<2014-jiang-linear-profile-decompositions-family_images/imageFile280.png>)

t,x . We assume henceforth that they are compactly supported Schwartz functions; say Suppvj,Suppvk ⊆ {(t,x) : |(t,x)| ≤ R}.

Passing to a subsequence, we may assume that each of the summands in (17) has a limit. (This passage is harmless because to prove (36), it suﬃces to prove that every subsequence has a further subsequence along which the limit is zero.)

We ﬁrst consider the case when h

j n

![image 281](<2014-jiang-linear-profile-decompositions-family_images/imageFile281.png>)

hkn → ∞. Using the L

2(d+2) d

![image 282](<2014-jiang-linear-profile-decompositions-family_images/imageFile282.png>)

t,x isometry properties and H¨older’s inequality,

- (37)


n,µknvk]

n,µjnvj][GknLak

[GjnLaj

d+2 d t,x

![image 283](<2014-jiang-linear-profile-decompositions-family_images/imageFile283.png>)

L

≤ vj

2(d+2) d

t,x (Supp(L−1

![image 284](<2014-jiang-linear-profile-decompositions-family_images/imageFile284.png>)

L

j n,µ

a

= vj

2(d+2) d

t,x (Supp(L−1

![image 285](<2014-jiang-linear-profile-decompositions-family_images/imageFile285.png>)

L

j n,µ

a

= [vj][L−aj1

n,µknvk]

n,µjn(Gjn)−1GknLak

d+2 d t,x

![image 286](<2014-jiang-linear-profile-decompositions-family_images/imageFile286.png>)

L

L−aj1

n,µknvk

n,µjn(Gjn)−1GknLak

(Gjn)−1GknLak

vk))

n,µk

j n

n

vk

.

2(d+2) d t,x

(Gjn)−1GknLak

![image 287](<2014-jiang-linear-profile-decompositions-family_images/imageFile287.png>)

vk))

L

n,µk

j n

n

.

2(d+2) d t,x

![image 288](<2014-jiang-linear-profile-decompositions-family_images/imageFile288.png>)

L

n,µjn(Gjn)−1GknLak

The exact computation of L−aj1

n,µknvk is elementary but tedious; however it is painless to verify that

j n

n,µknvk(t,x) = cjkn vk(djkn t − sjkn , h

L−aj1

n,µjn(Gjn)−1GknLak

hknx − ynjk(t)), for positive constants cjkn ,djkn , real numbers sjkn , and functions ynjk : R → Rd. Fix t. If (t,x) ∈ Supp(L−aj1 n,µjn(Gjn)−1GknLak

![image 289](<2014-jiang-linear-profile-decompositions-family_images/imageFile289.png>)

n,µknvk), then |x − h

k n

k n

hjnynjk(t)| ≤ h

hjnR. By H¨older, vj(t,·)

![image 290](<2014-jiang-linear-profile-decompositions-family_images/imageFile290.png>)

![image 291](<2014-jiang-linear-profile-decompositions-family_images/imageFile291.png>)

2(d+2) d

hkn hjnR d vj L∞

![image 292](<2014-jiang-linear-profile-decompositions-family_images/imageFile292.png>)

.

![image 293](<2014-jiang-linear-profile-decompositions-family_images/imageFile293.png>)

2(d+2) d

t,x

k n

x ({|x−ynj (t)|≤h

![image 294](<2014-jiang-linear-profile-decompositions-family_images/imageFile294.png>)

R})

L

![image 295](<2014-jiang-linear-profile-decompositions-family_images/imageFile295.png>)

j n

h

j n

Integrating the above estimate with respect to t and recalling that h

hkn → ∞, vj

![image 296](<2014-jiang-linear-profile-decompositions-family_images/imageFile296.png>)

2(d+2) d

k n

hjnR d → 0.

R(h

![image 297](<2014-jiang-linear-profile-decompositions-family_images/imageFile297.png>)

![image 298](<2014-jiang-linear-profile-decompositions-family_images/imageFile298.png>)

2(d+2) d

(Gjn)−1GknLak

t,x (Supp(L−1

![image 299](<2014-jiang-linear-profile-decompositions-family_images/imageFile299.png>)

vk))

L

n,µk

j n,µ

j n

n

a

k n

By (37), this implies (36). By a similar argument, (36) also holds if h

hjn → ∞.

![image 300](<2014-jiang-linear-profile-decompositions-family_images/imageFile300.png>)

Henceforth, we may assume that hjn ≡ hkn ≡ hn, so µjn ≡ µkn ≡ µn as well. Using a change of variables, we may now remove the dilations from the G(n·):

- (38) [GjnLaj

n,µjnvj][GknLak

n,µknvk]

L

d+2 d t,x

![image 301](<2014-jiang-linear-profile-decompositions-family_images/imageFile301.png>)

= [Laj

n,µjnvj][Gjkn Lak

n,µknvk]

L

d+2 d t,x

![image 302](<2014-jiang-linear-profile-decompositions-family_images/imageFile302.png>)

,

where Gjkn v(t,x) = v(t − t

k n−tjn

![image 303](<2014-jiang-linear-profile-decompositions-family_images/imageFile303.png>)

h4n ,x − x

k n−xjn

![image 304](<2014-jiang-linear-profile-decompositions-family_images/imageFile304.png>)

hn ). We now break into three cases: ajn ≡ akn ≡ 0; ajn ≡ 0 and |akn| → ∞; and |ajn|,|akn| → ∞. We deal with the easiest of the three cases, ajn ≡ akn ≡ 0, ﬁrst. In this case,

Laj

n,µnvj(t,x) = (1 + µn)

d

![image 305](<2014-jiang-linear-profile-decompositions-family_images/imageFile305.png>)

2(d+2)vj((1 + µn)t,x), Gjkn Lak

n,µnvk(t,x) = (1 + µn)

d

![image 306](<2014-jiang-linear-profile-decompositions-family_images/imageFile306.png>)

2(d+2)vk((1 + µn)[t − t

k n−tjn

![image 307](<2014-jiang-linear-profile-decompositions-family_images/imageFile307.png>)

h4n ],x − x

k n−xjn

![image 308](<2014-jiang-linear-profile-decompositions-family_images/imageFile308.png>)

hn ). By our assumptions on the various parameters, including the assumption that the orthogonality condition (17) holds, either t

k n−tjn

![image 309](<2014-jiang-linear-profile-decompositions-family_images/imageFile309.png>)

h4n → ∞ or x

k n−xjn

![image 310](<2014-jiang-linear-profile-decompositions-family_images/imageFile310.png>)

hn → ∞. In either case, Supp(Laj

n,µnvj) ∩ Supp(Gjkn Lak

n,µnvk) is empty for suﬃciently large n, so the right hand side of (38) is eventually zero. By the identity (38), this establishes (36).

We turn now to the case when ajn ≡ 0, |akn| → ∞. (By symmetry, this argument also covers the case when the roles of j and k are reversed.) Arguing similarly to (37),

- (39) [Laj


n,µnvk]

n,µnvj][Gjkn Lak

vj

.

d+2 d

d+2 d t,x

Gjkn Lak

t,x (Supp L−1

![image 311](<2014-jiang-linear-profile-decompositions-family_images/imageFile311.png>)

![image 312](<2014-jiang-linear-profile-decompositions-family_images/imageFile312.png>)

n,µnvk)

L

L

j n,µn

a

We compute:

n,µnvk(t,x) = 2|a

L−aj1

n,µnGjkn Lak

= 2|a

d

k n−tjn)(1+µn)

k n|2+µn

k n|2+µn

1+µn (t − (t

2(d+2)vk(2|a

![image 313](<2014-jiang-linear-profile-decompositions-family_images/imageFile313.png>)

h4n ), x − x

![image 314](<2014-jiang-linear-profile-decompositions-family_images/imageFile314.png>)

![image 315](<2014-jiang-linear-profile-decompositions-family_images/imageFile315.png>)

![image 316](<2014-jiang-linear-profile-decompositions-family_images/imageFile316.png>)

1+µn

k n−xjn

k n−tjn)(1+µn)

k n|2+2µn

hn + 4|a

1+µn akn(t − (t

h4n ))

![image 317](<2014-jiang-linear-profile-decompositions-family_images/imageFile317.png>)

![image 318](<2014-jiang-linear-profile-decompositions-family_images/imageFile318.png>)

![image 319](<2014-jiang-linear-profile-decompositions-family_images/imageFile319.png>)

d

k n|2+µn

k n|2+2µn

k n|2+µn

1+µn (t − sjkn ),x + 4|a

2(d+2)vk(2|a

1+µn aknt − ynjk),

![image 320](<2014-jiang-linear-profile-decompositions-family_images/imageFile320.png>)

![image 321](<2014-jiang-linear-profile-decompositions-family_images/imageFile321.png>)

![image 322](<2014-jiang-linear-profile-decompositions-family_images/imageFile322.png>)

![image 323](<2014-jiang-linear-profile-decompositions-family_images/imageFile323.png>)

1+µn

where

k n−tjn)(1+µn)

sjkn = (t

![image 324](<2014-jiang-linear-profile-decompositions-family_images/imageFile324.png>)

h4n ynjk = x

k n−xjn

k n|2+2µn

hn + 4|a

1+µn aknsjkn . Fix x. If (t,x) ∈ (Suppvj)∩(SuppL−aj1

![image 325](<2014-jiang-linear-profile-decompositions-family_images/imageFile325.png>)

![image 326](<2014-jiang-linear-profile-decompositions-family_images/imageFile326.png>)

k n|2+2µn

nµnvk), it satisﬁes |x| ≤ R and |x+4|a

n,µnGjkn Lak

1+µn aknt− ynjk| ≤ R. Therefore

![image 327](<2014-jiang-linear-profile-decompositions-family_images/imageFile327.png>)

k n|2+2µn

|4|a

1+µn aknt − ynjk| ≤ 2R, so recalling that |akn| 1 for all n,

![image 328](<2014-jiang-linear-profile-decompositions-family_images/imageFile328.png>)

|t − rnjk| ≤ (4|a2kR(1+µn)

R |akn|, where

![image 329](<2014-jiang-linear-profile-decompositions-family_images/imageFile329.png>)

![image 330](<2014-jiang-linear-profile-decompositions-family_images/imageFile330.png>)

n|2+2µn)|akn|

jk n ·akn

rnjk = (1+µn)y

(4|akn|2+2µn)|akn|2. Integrating in t,

![image 331](<2014-jiang-linear-profile-decompositions-family_images/imageFile331.png>)

2(d+2) d

vj L∞

vj(·,x)

R |akn|. Integrating this in x,

![image 332](<2014-jiang-linear-profile-decompositions-family_images/imageFile332.png>)

![image 333](<2014-jiang-linear-profile-decompositions-family_images/imageFile333.png>)

2(d+2) d

t,x

t ({|t+rnjk| R

![image 334](<2014-jiang-linear-profile-decompositions-family_images/imageFile334.png>)

})

L

![image 335](<2014-jiang-linear-profile-decompositions-family_images/imageFile335.png>)

|ak

n|

2(d+2) d

Rd|aRk

vj L∞

vj

![image 336](<2014-jiang-linear-profile-decompositions-family_images/imageFile336.png>)

n| → 0.

![image 337](<2014-jiang-linear-profile-decompositions-family_images/imageFile337.png>)

d+2 d

t,x

Gjkn Lak

t,x (Supp L−1

![image 338](<2014-jiang-linear-profile-decompositions-family_images/imageFile338.png>)

nµnvk)

L

j n,µn

a

This implies (36), and completes the case when ajn ≡ 0, |akn| → ∞. Finally we turn to the case when |ajn|,|akn| → ∞. We compute

d

L−aj1

n,µnGjkn Lak

n,µnvk(t,x) = (cjkn )

2(d+2)vk(cjkn (t − sjkn ),x − ynjk − bjkn t), where

![image 339](<2014-jiang-linear-profile-decompositions-family_images/imageFile339.png>)

k n|2+µn

cjkn = 2|a

2|ajn|2+µn, sjkn = (t

![image 340](<2014-jiang-linear-profile-decompositions-family_images/imageFile340.png>)

k n−tjn)(2|ajn|2+µn)

h4n , ynjk = x

![image 341](<2014-jiang-linear-profile-decompositions-family_images/imageFile341.png>)

k n|2+2µn)(tkn−tjn)

k n−xjn

hn + akn(4|a

h4n , bjkn = (2|a

![image 342](<2014-jiang-linear-profile-decompositions-family_images/imageFile342.png>)

![image 343](<2014-jiang-linear-profile-decompositions-family_images/imageFile343.png>)

j n|2+µn)ajn−(2|akn|2+µn)akn

2|ajn|2+µn . Suppose that |ajn − akn| → ∞. We claim that |bjkn | → ∞. Indeed,

![image 344](<2014-jiang-linear-profile-decompositions-family_images/imageFile344.png>)

akn − ajn |ajn − akn|

|bjkn | ≥ bjkn ·

![image 345](<2014-jiang-linear-profile-decompositions-family_images/imageFile345.png>)

5[ajn · (akn − ajn)]2 + 6|akn − ajn|2ajn · (akn − ajn) + 2|akn − ajn|4 + |akn − ajn|2(|ajn|2 + µn) (2|ajn|2 + µn)|akn − ajn| ≥

=

![image 346](<2014-jiang-linear-profile-decompositions-family_images/imageFile346.png>)

|akn − ajn|2(|ajn|2 + µn) (2|ajn|2 + µn)|akn − ajn|

≥ 12|akn − ajn|, where for the second inequality, we used Cauchy–Schwartz and the elementary inequality 5(ab)2 + 2b4 ≥ 92(ab)2 + 2b4 ≥ 6|ab3|,

![image 347](<2014-jiang-linear-profile-decompositions-family_images/imageFile347.png>)

![image 348](<2014-jiang-linear-profile-decompositions-family_images/imageFile348.png>)

![image 349](<2014-jiang-linear-profile-decompositions-family_images/imageFile349.png>)

for all a,b ∈ R. Since |bjkn | → ∞, arguing exactly as we did in the case ajn ≡ 0, |akn| → ∞, we can establish (36).

Henceforth, we may assume that ajn ≡ akn. Thus cjkn ≡ 1 and bjkn ≡ 0. If |sjkn | → ∞ or |ynjk| → ∞, the (compact) supports of vj and L−aj1

nµnGjkn Lak

nµnvk are disjoint for suﬃciently large n, so (36) holds. Since |sjkn | ≥ |t

j n−tkn|

h4n , this completes the proof in the case |ajn|,|akn| → ∞. Finally, the proposition is proved.

![image 350](<2014-jiang-linear-profile-decompositions-family_images/imageFile350.png>)

4. Application: Dichotomy result on the existence of extremizers

As an application of the proﬁle decomposition in Theorem 3.1, we establish lower bounds for the operator norms and a dichotomy result on existence of extremizers. Similar results have previously appeared in Jiang, Pausader and Shao [9]. We begin by deﬁning

- (40) Aµ := sup

φ∈L2x, φ =0

D

d

![image 351](<2014-jiang-linear-profile-decompositions-family_images/imageFile351.png>)

µd+2Sµ(t)φ

L

2(d+2) d

![image 352](<2014-jiang-linear-profile-decompositions-family_images/imageFile352.png>)

t,x (R×Rd) φ L2

![image 353](<2014-jiang-linear-profile-decompositions-family_images/imageFile353.png>)

x

, µ ≥ 0,

and

- (41) B := sup

ψ∈L2x, ψ =0

eit∆ψ

L

d d+2 t,x (R×Rd)

![image 354](<2014-jiang-linear-profile-decompositions-family_images/imageFile354.png>)

![image 355](<2014-jiang-linear-profile-decompositions-family_images/imageFile355.png>)

ψ L2

x

.

These are ﬁnite by the Strichartz inequalities for the fourth order Schro¨dinger and Schro¨dinger equations.

We say that a function φ is an extremizer for Aµ (resp. B) if φ L2

x

= 0 and φ maximizes the ratio in (40) (resp. (41)). A sequence {φn} is an extremizing sequence for Aµ if

Aµ = lim

n→∞

D

d

![image 356](<2014-jiang-linear-profile-decompositions-family_images/imageFile356.png>)

µd+2Sµ(t)φn

L

2(d+2) d t,x

![image 357](<2014-jiang-linear-profile-decompositions-family_images/imageFile357.png>)

![image 358](<2014-jiang-linear-profile-decompositions-family_images/imageFile358.png>)

φn L2

x

;

{φn} is L2x-normalized if φn L2

x

= 1 for all n.

Extremizers are known to exist for B ([6, 8] for d = 1,2, [27] for d ≥ 3). In dimensions 1 and 2, it is known in addition that the extremizers are only Gaussian functions, modulo symmetries of the Schro¨dinger equation [6, 8].

- Theorem 4.1. The operator norms A0 and B satisfy:


- (42) A0 ≥ 3−

- 1

![image 359](<2014-jiang-linear-profile-decompositions-family_images/imageFile359.png>)

- 2(d+2)2−


d

![image 360](<2014-jiang-linear-profile-decompositions-family_images/imageFile360.png>)

2(d+2)B.

If the inequality is strict in (42), then extremizers exist for A0. If extremizers do not exist and {φn} is an L2x-normalized extremizing sequence for A0, there exist a sequence of parameters (hn,ξn,xn,tn) with |hnξn| → ∞ and an extremizer ψ for B such that after passing to a subsequence,

- (43) lim

n→∞

φn − S0(tn)gn(ei(·)hnξnψ ◦ ℓ−h1

nξn) L2

x

= 0, where for a ∈ Rd, ℓa denotes the transformation

- (44) ℓa(ξ) =


√

![image 361](<2014-jiang-linear-profile-decompositions-family_images/imageFile361.png>)

6 proja(ξ) +

√

![image 362](<2014-jiang-linear-profile-decompositions-family_images/imageFile362.png>)

2(ξ − proja(ξ)),

where proja(ξ) := (ξ · |aa|)|aa|. Conversely, if equality holds in (42), any sequence {φn} satisfying (43) for a sequence of parameters (hn,ξn,xn,tn)n≥1 with |hnξn| → ∞ and an extremizer ψ for B is an extremizing sequence for A0.

![image 363](<2014-jiang-linear-profile-decompositions-family_images/imageFile363.png>)

![image 364](<2014-jiang-linear-profile-decompositions-family_images/imageFile364.png>)

If µ > 0, then by scaling, Aµ = A1; scaling also gives a natural correspondence between extremizing sequences (and, if they exist, extremizers) for Aµ and those for A1. Thus we only state the dichotomy result in the case µ = 1.

- Theorem 4.2. The operator norms satisfy A1 ≥ max{A0,B}, and if this inequality is strict, extremizers exist for A1. If extremizers do not exist and {φn} is an L2x-normalized extremizing


sequence for A1, then there exist a sequence of parameters (hn,ξn,xn,tn) and a function φ ∈ L2x such that after passing to a subsequence,

- (45) lim

n→∞

φn − S1(tn)gnei(·)hnξnψ L2

x

= 0.

Moreover, in this case, one of the following occurs: either A1 = B, hn → ∞, |ξn| → 0, and ψ is an extremizer for B, or A1 = A0, hn → 0, ξn ≡ 0, and ψ is an extremizer for A0.

The analogue of the ﬁnal conclusion of Theorem 4.1 for A1 is the following. If A1 = B, hn → ∞, |ξn| → 0, ψ is an extremizer for B, and φn satisﬁes (45), then φn is an extremizing sequence for A1. If A1 = A0, then A0 ≥ B, so the inequality is strict in (42), which implies that extremizers exist for A0. Furthermore, in this case, if hn → 0, ξn ≡ 0, ψ is an extremizer for A0, and φn satisﬁes (45), then φn is an extremizing sequence for A1.

The proofs of these theorems will rely on the linear proﬁle decomposition and the following lemmas.

- Lemma 4.3. Let φ ∈ L2x(Rd). If (an) is a sequence in Rd with |an| → ∞, then

(46)

lim

n→∞

 |∇|

d

![image 365](<2014-jiang-linear-profile-decompositions-family_images/imageFile365.png>)

d+2eit∆2(ei(·)anφ) − |an|

d

![image 366](<2014-jiang-linear-profile-decompositions-family_images/imageFile366.png>)

d+2ei(x·an+t|an|4)e−i|an|2t∆(φ ◦ ℓan)(ℓ−an1(x + 4t|an|2an))

L

2(d+2)

![image 367](<2014-jiang-linear-profile-decompositions-family_images/imageFile367.png>)

d t,x

= 0,

with ℓa as in (44).

- Lemma 4.4. Let φ ∈ L2x(Rd). Let (hn,ξn) be a sequence in (0,∞) × Rd. Deﬁne gnφ(x) =


- (47) lim n→∞

  ∇ 

d

![image 368](<2014-jiang-linear-profile-decompositions-family_images/imageFile368.png>)

d+2S1(t)gnei(·)hnξnφ − |∇|

d

![image 369](<2014-jiang-linear-profile-decompositions-family_images/imageFile369.png>)

d+2eit∆2gnφ

L

2(d+2)

![image 370](<2014-jiang-linear-profile-decompositions-family_images/imageFile370.png>)

d t,x

= 0.

If hn → ∞ and ξn ≡ 0,

- (48) lim n→∞

  ∇ 

d

![image 371](<2014-jiang-linear-profile-decompositions-family_images/imageFile371.png>)

d+2S1(t)gnei(·)hnξnφ − e−it∆gnφ

L

2(d+2) d t,x

![image 372](<2014-jiang-linear-profile-decompositions-family_images/imageFile372.png>)

= 0.

If |ξn| 1 for all n and |hnξn| → ∞,

- (49)


d

h−

n 2φ(hx

![image 373](<2014-jiang-linear-profile-decompositions-family_images/imageFile373.png>)

). If hn → 0 and ξn ≡ 0,

![image 374](<2014-jiang-linear-profile-decompositions-family_images/imageFile374.png>)

n

d

d+2S1(t)gnei(·)hnξnφ − ξn

lim

  ∇ 

![image 375](<2014-jiang-linear-profile-decompositions-family_images/imageFile375.png>)

n→∞

d

d+2ei(xξn+t|ξn|4+t|ξn|2)e−it∆[gn(φ ◦ ℓ˜n)](ℓ˜−n1(x + 4t|ξn|2ξn + 2tξn))

![image 376](<2014-jiang-linear-profile-decompositions-family_images/imageFile376.png>)

2(d+2)

![image 377](<2014-jiang-linear-profile-decompositions-family_images/imageFile377.png>)

d t,x

L

= 0,

where ℓ˜n(ξ) = 6|ξn|2 + 1 (projξnξ) + 2|ξn|2 + 1(ξ − projξnξ). If |ξn| → ∞ and |hnξn| → ∞,

![image 378](<2014-jiang-linear-profile-decompositions-family_images/imageFile378.png>)

![image 379](<2014-jiang-linear-profile-decompositions-family_images/imageFile379.png>)

- (50)

lim

n→∞

  ∇ 

d

![image 380](<2014-jiang-linear-profile-decompositions-family_images/imageFile380.png>)

d+2S1(t)gnei(·)hnξnφ

− |ξn|

d

![image 381](<2014-jiang-linear-profile-decompositions-family_images/imageFile381.png>)

d+2ei(xξn+t|ξn|4+t|ξn|2)e−i

|ξn|2 h2

![image 382](<2014-jiang-linear-profile-decompositions-family_images/imageFile382.png>)

n

t∆[gn(φ ◦ ℓn)](ℓ−n1(x + 4t|ξn|2ξn + 2tξn))

L

2(d+2) d t,x

![image 383](<2014-jiang-linear-profile-decompositions-family_images/imageFile383.png>)

= 0,

with ℓn = ℓξn, using the notation from (44).

The lemmas will be proved at the end of this section. Before proceeding to their proofs, we show how Theorem 4.1 can be proved from Lemma 4.3 and indicate how to adapt this proof for Theorem 4.2.

Proof of Theorem 4.1. Let (hn,ξn,xn,tn) be a sequence of parameters with |hnξn| → ∞ and let ψ be an extremizer for B. Assume that the sequence {φn} ⊂ L2x satisﬁes

lim

n→∞

φn − eitn∆2gn(ei(·)hnξnψ ◦ ℓ−h1

nξn) L2

x

= 0.

By the Strichartz inequality (5), changes of variables, Lemma 4.4, and the assumption that ψ is an extremizer,

- (51)


d

d

d+2eit∆2φn

d+2ei(t+tn)∆2gn(ei(·)hnξn(ψ ◦ ℓ−h1

nξn))

 |∇|

 |∇|

![image 384](<2014-jiang-linear-profile-decompositions-family_images/imageFile384.png>)

![image 385](<2014-jiang-linear-profile-decompositions-family_images/imageFile385.png>)

2(d+2) d t,x

2(d+2) d t,x

![image 386](<2014-jiang-linear-profile-decompositions-family_images/imageFile386.png>)

![image 387](<2014-jiang-linear-profile-decompositions-family_images/imageFile387.png>)

L

L

= lim

A0 ≥ lim

![image 388](<2014-jiang-linear-profile-decompositions-family_images/imageFile388.png>)

![image 389](<2014-jiang-linear-profile-decompositions-family_images/imageFile389.png>)

eitn∆2gn(ei(·)hnξnψ ◦ ℓ−h1

φn L2

nξn) L2

n→∞

n→∞

x

x

d

= 3−142−d4 ψ −L21

d+2eit∆2ei(·)hnξn(ψ ◦ ℓ−h1

lim

 |∇|

nξn)

![image 390](<2014-jiang-linear-profile-decompositions-family_images/imageFile390.png>)

![image 391](<2014-jiang-linear-profile-decompositions-family_images/imageFile391.png>)

![image 392](<2014-jiang-linear-profile-decompositions-family_images/imageFile392.png>)

2(d+2)

n→∞

x

![image 393](<2014-jiang-linear-profile-decompositions-family_images/imageFile393.png>)

d t,x

L

d

= 3−142−d4 ψ −L21

d+2e−i|hnξn|2t∆ψ) ◦ ℓ−h1

lim

(|hnξn|

![image 394](<2014-jiang-linear-profile-decompositions-family_images/imageFile394.png>)

![image 395](<2014-jiang-linear-profile-decompositions-family_images/imageFile395.png>)

![image 396](<2014-jiang-linear-profile-decompositions-family_images/imageFile396.png>)

2(d+2) d t,x

nξn

n→∞

x

![image 397](<2014-jiang-linear-profile-decompositions-family_images/imageFile397.png>)

L

- 1

![image 398](<2014-jiang-linear-profile-decompositions-family_images/imageFile398.png>)

- 2(d+2)2−


d

d

- 1

![image 399](<2014-jiang-linear-profile-decompositions-family_images/imageFile399.png>)

- 2(d+2)2−


= 3−

= 3−

2(d+2) ψ −L21

e−it∆ψ

2(d+2)B.

![image 400](<2014-jiang-linear-profile-decompositions-family_images/imageFile400.png>)

![image 401](<2014-jiang-linear-profile-decompositions-family_images/imageFile401.png>)

2(d+2) d t,x

x

![image 402](<2014-jiang-linear-profile-decompositions-family_images/imageFile402.png>)

L

This veriﬁes (42). Conversely, if equality holds in (42), then it holds everywhere in the computation above, establishing the ﬁnal conclusion of the theorem.

In the other direction, let {φn} be an L2x-normalized extremizing sequence for A0. By Theorem 3.1, there exist sequences {φj}j≥1, {wnj }j≥1,n≥1, and parameters (hjn,ξnj,tjn)j≥1,n≥1 such that for each j, |hjnξnj| → ∞ or hjnξnj ≡ 0 and such that after passing to a subsequence,

l

φn =

j=1

j

j

nξnj φj) + wnl ,

n∆2gnj (ei(·)h

eit

where (16), (18), and (20) hold.

Therefore, A

2(d+2) d

d

d+2eit∆2φn

![image 403](<2014-jiang-linear-profile-decompositions-family_images/imageFile403.png>)

0 = lim

 |∇|

![image 404](<2014-jiang-linear-profile-decompositions-family_images/imageFile404.png>)

n→∞

≤ limsup

limsup

n→∞ 1≤j≤l

l→∞

≤ limsup

limsup

n→∞ 1≤j≤l

l→∞

2(d+2) d

4 d

φj

![image 405](<2014-jiang-linear-profile-decompositions-family_images/imageFile405.png>)

![image 406](<2014-jiang-linear-profile-decompositions-family_images/imageFile406.png>)

≤ A

0 sup

L2x

j

2(d+2) d

![image 407](<2014-jiang-linear-profile-decompositions-family_images/imageFile407.png>)

2(d+2)

![image 408](<2014-jiang-linear-profile-decompositions-family_images/imageFile408.png>)

d t,x

L

j

j

nξnj φj)

d

n)∆2gnj (ei(·)h

d+2ei(t+t

 |∇|

![image 409](<2014-jiang-linear-profile-decompositions-family_images/imageFile409.png>)

2(d+2) d

nξnj φj

j

0 ei(·)h

![image 410](<2014-jiang-linear-profile-decompositions-family_images/imageFile410.png>)

A

2(d+2) d

![image 411](<2014-jiang-linear-profile-decompositions-family_images/imageFile411.png>)

L2x =

j

φj 2L2

.

x

j

2(d+2) d

![image 412](<2014-jiang-linear-profile-decompositions-family_images/imageFile412.png>)

2(d+2) d t,x

![image 413](<2014-jiang-linear-profile-decompositions-family_images/imageFile413.png>)

L

2(d+2) d

0 φj

![image 414](<2014-jiang-linear-profile-decompositions-family_images/imageFile414.png>)

A

2(d+2) d L2x

![image 415](<2014-jiang-linear-profile-decompositions-family_images/imageFile415.png>)

By (18), the right hand side is strictly less than the left hand side (a contradiction) unless there exists j such that φj L2

= 1. In this case, there is only one proﬁle and the error terms tend to zero in L2x:

x

- (52) φn = eitn∆2gn(ei(·)hnξnφ) + wn, lim n→∞

wn L2

x

= 0. If hnξn ≡ 0, since

eitn∆2gn(φ) L2

x

= φ L2

x

,  |∇|

d

![image 416](<2014-jiang-linear-profile-decompositions-family_images/imageFile416.png>)

d+2ei(t+tn)∆2gn(φ)

L

2(d+2)

![image 417](<2014-jiang-linear-profile-decompositions-family_images/imageFile417.png>)

d t,x

=  |∇|

d

![image 418](<2014-jiang-linear-profile-decompositions-family_images/imageFile418.png>)

d+2eit∆2φ

L

2(d+2)

![image 419](<2014-jiang-linear-profile-decompositions-family_images/imageFile419.png>)

d t,x

,

φ is an extremizer for A0. Thus if A0 does not have an extremizer, every L2x-normalized extremizing sequence must satisfy (after passing to a subsequence)

- (53) φn − eitn∆2gn(ei(·)hnξnφ) L2


→ 0,

x

for some function φ ∈ L2x and parameters (hn,ξn,tn,xn) with |hnξn| → ∞. By the essentially the same computation as (51), this implies that A0 ≤ 3−

- 1

![image 420](<2014-jiang-linear-profile-decompositions-family_images/imageFile420.png>)

- 2(d+2)2−


d

2(d+2)B, and hence that equality holds in (42).

![image 421](<2014-jiang-linear-profile-decompositions-family_images/imageFile421.png>)

Thus it remains to show that if {φn} is an L2x-normalized extremizing sequence for A0, (42) holds with equality, and (53) holds for some φ and (hn,tn,xn,ξn) with |hnξn| → ∞, then (43) holds with ψ an extremizer for B.

Passing to a further subsequence, there exists ω ∈ Sd−1 such that |hhnξn

nξn| → ω. Let ψ = φ ◦ ℓω. For a = 0, ℓa depends only on |aa|, so φ − ψ ◦ ℓ−h1

![image 422](<2014-jiang-linear-profile-decompositions-family_images/imageFile422.png>)

nξn → 0 in L2x. Therefore eitn∆2gn(ei(·)hnξnφ) − eitn∆2gn(ei(·)hnξn(ψ ◦ ℓ−h1

![image 423](<2014-jiang-linear-profile-decompositions-family_images/imageFile423.png>)

→ 0, which implies by (52) that

nξn)) L2

x

φn − eitn∆2gn(ei(·)hnξn(ψ ◦ ℓ−h1

nξn)) L2

→ 0.

x

That ψ is an extremizer for B follows from the same computations as in (51). This completes the proof of Theorem 4.1.

Adapting the argument for Theorem 4.2. There are two relatively minor diﬀerences in the proof of Theorem 4.2. First, A1 must be compared to two operator norms, A0 and B. To obtain the estimate A1 ≥ B, we simply take an extremizer ψ for B and use (48), arguing similarly to (51). Given ε > 0, we can show that A1 ≥ (1−ε)A0 by selecting an L2x-normalized function ψ satisfying  |∇|

d

d+2eit∆2ψ ≥ (1 − ε)A0 and using (47); letting ε → 0, we see that A1 ≥ A0.

![image 424](<2014-jiang-linear-profile-decompositions-family_images/imageFile424.png>)

Second, we must rule out the case in which (45) holds for some ψ ∈ L2x and some sequence of parameters (hn,ξn,tn,xn) with ξn  → 0. Passing to a subsequence and using the fact that

spacetime translations do not aﬀect any of the relevant operator norms, it suﬃces to consider the cases when (tn,xn) ≡ (0,0), |hnξn| → ∞, and either ξn → ξ0 = 0 or |ξn| → ∞. If |ξn| → ∞, we apply (50) and compute

d

d+2ei(xξn+th2n|ξn|4+t|ξn|2)e−i|ξn|2t∆[gn(φ ◦ ℓn)](ℓ−n1(x + th2n|ξn|2ξn + 2tξn))

 |ξn|

![image 425](<2014-jiang-linear-profile-decompositions-family_images/imageFile425.png>)

2(d+2) d t,x

![image 426](<2014-jiang-linear-profile-decompositions-family_images/imageFile426.png>)

L

d

- 1

![image 427](<2014-jiang-linear-profile-decompositions-family_images/imageFile427.png>)

- 2(d+2)2−


≤ 3−

< B, provided ξn = 0, ℓn = ℓξn is as in (44), and φ L2

2(d+2)B φ L2

![image 428](<2014-jiang-linear-profile-decompositions-family_images/imageFile428.png>)

x

≤ 1. If ξn → ξ0 = 0 and φ L2

≤ 1, we use

x

x

(49) and compute limsup

d

d+2ei(xξn+th2n|ξn|4+t|ξn|2)e−it∆[gn(φ ◦ ℓ˜n)](ℓ˜−n1(x + 4th2n|ξn|2ξn + 2tξn))

ξn

![image 429](<2014-jiang-linear-profile-decompositions-family_images/imageFile429.png>)

2(d+2) d t,x

![image 430](<2014-jiang-linear-profile-decompositions-family_images/imageFile430.png>)

n→∞

L

d−1

d

1

d+2(6|ξn|2 + 1)−

d+2(2|ξn|2 + 1)−

(|ξn|2 + 1)

≤ limsup

d+2B φ L2

![image 431](<2014-jiang-linear-profile-decompositions-family_images/imageFile431.png>)

![image 432](<2014-jiang-linear-profile-decompositions-family_images/imageFile432.png>)

![image 433](<2014-jiang-linear-profile-decompositions-family_images/imageFile433.png>)

x

n→∞

d−1

1

d

d+2(6|ξ0|2 + 1)−

d+2(2|ξ0|2 + 1)−

= (|ξ0|2 + 1)

< B, so this case can be ruled out as well.

d+2B φ L2

![image 434](<2014-jiang-linear-profile-decompositions-family_images/imageFile434.png>)

![image 435](<2014-jiang-linear-profile-decompositions-family_images/imageFile435.png>)

![image 436](<2014-jiang-linear-profile-decompositions-family_images/imageFile436.png>)

x

Finally, we prove the lemmas.

Proof of Lemmas 4.3 and 4.4. We begin by observing that by the change of variables formula and the Strichartz inequality for Schro¨dinger,

d

d+2ei(x·an+t|an|4+tµ|an|2)e−i|an|2t∆(φ ◦ ℓan)(ℓ−an1(x + 4t|an|2an))

 |an|

![image 437](<2014-jiang-linear-profile-decompositions-family_images/imageFile437.png>)

d2

d

4(d+2) e−it∆φ ◦ ℓan

4(d+2)2

= 3

![image 438](<2014-jiang-linear-profile-decompositions-family_images/imageFile438.png>)

![image 439](<2014-jiang-linear-profile-decompositions-family_images/imageFile439.png>)

2(d+2) d t,x

![image 440](<2014-jiang-linear-profile-decompositions-family_images/imageFile440.png>)

L

d2

d

- 1

![image 441](<2014-jiang-linear-profile-decompositions-family_images/imageFile441.png>)

- 2(d+2)2−


d

= 3−

. Similar computations give:

4(d+2)2

4(d+2)B φ ◦ ℓan L2

2(d+2)B φ L2

≤ 3

![image 442](<2014-jiang-linear-profile-decompositions-family_images/imageFile442.png>)

![image 443](<2014-jiang-linear-profile-decompositions-family_images/imageFile443.png>)

![image 444](<2014-jiang-linear-profile-decompositions-family_images/imageFile444.png>)

x

x

2(d+2) d t,x

![image 445](<2014-jiang-linear-profile-decompositions-family_images/imageFile445.png>)

L

d

d+2eit∆2gnφ

, e−it∆gnφ

 |∇|

≤ A0 φ L2

≤ B φ L2

,

![image 446](<2014-jiang-linear-profile-decompositions-family_images/imageFile446.png>)

2(d+2)

2(d+2)

x

x

![image 447](<2014-jiang-linear-profile-decompositions-family_images/imageFile447.png>)

![image 448](<2014-jiang-linear-profile-decompositions-family_images/imageFile448.png>)

d t,x

d t,x

L

L

d

d+2ei(xξn+th2n|ξn|4+t|ξn|2)e−it∆[gn(φ ◦ ℓ˜n)](ℓ˜−n1(x + 4th2n|ξn|2ξn + 2tξn))

ξn

![image 449](<2014-jiang-linear-profile-decompositions-family_images/imageFile449.png>)

2(d+2) d t,x

![image 450](<2014-jiang-linear-profile-decompositions-family_images/imageFile450.png>)

L

d−1

1

d

d+2(6|ξn|2 + 1)−

d+2(2|ξn|2 + 1)−

≤ (|ξn|2 + 1)

,  |ξn|

d+1B φ L2

![image 451](<2014-jiang-linear-profile-decompositions-family_images/imageFile451.png>)

![image 452](<2014-jiang-linear-profile-decompositions-family_images/imageFile452.png>)

![image 453](<2014-jiang-linear-profile-decompositions-family_images/imageFile453.png>)

x

d

d+2ei(xξn+th2n|ξn|4+t|ξn|2)e−i|ξn|2t∆[gn(φ ◦ ℓn)](ℓ−n1(x + 4th2n|ξn|2ξn + 2tξn))

![image 454](<2014-jiang-linear-profile-decompositions-family_images/imageFile454.png>)

2(d+2)

![image 455](<2014-jiang-linear-profile-decompositions-family_images/imageFile455.png>)

d t,x

L

- 1

![image 456](<2014-jiang-linear-profile-decompositions-family_images/imageFile456.png>)

- 2(d+2)2−


d

≤ 3−

. In addition, by the Strichartz inequality (5) for 4th order Schro¨dinger, the operator φ  → D

2(d+2)B φ L2

![image 457](<2014-jiang-linear-profile-decompositions-family_images/imageFile457.png>)

x

d

µd+2Sµ(t)gn(ei(·)anφ) is also uniformly bounded from L2x to L

![image 458](<2014-jiang-linear-profile-decompositions-family_images/imageFile458.png>)

2(d+2) d

![image 459](<2014-jiang-linear-profile-decompositions-family_images/imageFile459.png>)

t,x , so it suﬃces to prove the lemmas when φ is in some

dense subset of L2x. Thus we may assume that φ is a Schwartz function with compact frequency support that does not contain 0:

Supp φ ⊆ {R−1 ≤ |ξ| ≤ R}.

Under the hypotheses of Lemma 4.3, we assume |an| ≥ 2R and |ξ − an| ≤ R. Then |ξ| ∼ |an|, so by the fundamental theorem of calculus,

d d+2

d d+2

2

d d+2

d d+2

d d+2

![image 460](<2014-jiang-linear-profile-decompositions-family_images/imageFile460.png>)

|an|

|an|−

|an|−

− 1 ∼ |an|−

− |ξ|

d+2R.

|an|

![image 461](<2014-jiang-linear-profile-decompositions-family_images/imageFile461.png>)

![image 462](<2014-jiang-linear-profile-decompositions-family_images/imageFile462.png>)

![image 463](<2014-jiang-linear-profile-decompositions-family_images/imageFile463.png>)

![image 464](<2014-jiang-linear-profile-decompositions-family_images/imageFile464.png>)

![image 465](<2014-jiang-linear-profile-decompositions-family_images/imageFile465.png>)

![image 466](<2014-jiang-linear-profile-decompositions-family_images/imageFile466.png>)

d d+2

![image 467](<2014-jiang-linear-profile-decompositions-family_images/imageFile467.png>)

|ξ|

Since the function ei(·)anφ has frequency support on {|ξ − an| ≤ R}, ei(·)anφ − |an|

d

d+2D−

d

µ d+2ei(·)anφ

|an|−1R → 0.

![image 468](<2014-jiang-linear-profile-decompositions-family_images/imageFile468.png>)

![image 469](<2014-jiang-linear-profile-decompositions-family_images/imageFile469.png>)

L2x

d

2(d+2) d

µd+2Sµ(t) is a bounded operator from L2x to L

![image 470](<2014-jiang-linear-profile-decompositions-family_images/imageFile470.png>)

![image 471](<2014-jiang-linear-profile-decompositions-family_images/imageFile471.png>)

t,x , (46) would follow from

Therefore, since D

- (54) |an|

d

![image 472](<2014-jiang-linear-profile-decompositions-family_images/imageFile472.png>)

d+2 eit∆2(ei(·)anφ) − ei(x·an+t(|an|4−|an|2∆))(φ ◦ ℓan)(ℓ−an1(x + 4t|an|2an))

L

2(d+2) d t,x

![image 473](<2014-jiang-linear-profile-decompositions-family_images/imageFile473.png>)

→ 0.

Changing variables in t, the left hand side of (54) equals ei

t |an|2

![image 474](<2014-jiang-linear-profile-decompositions-family_images/imageFile474.png>)

∆2ei(·)anφ − ei(xan+t|an|2)e−it∆(φ ◦ ℓan)(ℓ−an1(x + 4ant))

L

2(d+2) d t,x

![image 475](<2014-jiang-linear-profile-decompositions-family_images/imageFile475.png>)

.

Next, we compute ei

t |an|2

![image 476](<2014-jiang-linear-profile-decompositions-family_images/imageFile476.png>)

∆2ei(·)anφ(x) = ei(xξ+

t

![image 477](<2014-jiang-linear-profile-decompositions-family_images/imageFile477.png>)

|an|2|ξ|4) φ(ξ − an)dξ = eix(ξ+an)ei

t

![image 478](<2014-jiang-linear-profile-decompositions-family_images/imageFile478.png>)

|an|2|ξ+an|4 φ(ξ)dξ

= ei(x·an+t|an|2) ei(x+4tan)ξeit(

|ξ|4

![image 479](<2014-jiang-linear-profile-decompositions-family_images/imageFile479.png>)

|an|2 +4|ξ|

2ξan

![image 480](<2014-jiang-linear-profile-decompositions-family_images/imageFile480.png>)

|an|2 +2|ξ|2+4(anξ)

2

![image 481](<2014-jiang-linear-profile-decompositions-family_images/imageFile481.png>)

|an|2 ) φ(ξ)dξ

= ei(xan+t|an|2) ei(x+4tan)ξeit(

|ξ|4

![image 482](<2014-jiang-linear-profile-decompositions-family_images/imageFile482.png>)

|an|2 +4|ξ|

2ξan

![image 483](<2014-jiang-linear-profile-decompositions-family_images/imageFile483.png>)

|an|2 +|ℓan(ξ)|2) φ(ξ)dξ. Thus (54) would follow from

- (55) eit(

∆2

![image 484](<2014-jiang-linear-profile-decompositions-family_images/imageFile484.png>)

|an|2 +4i|∆a∇an

![image 485](<2014-jiang-linear-profile-decompositions-family_images/imageFile485.png>)

n|2 +|ℓan(−i∇)|2)φ(x) − e−it∆(φ ◦ ℓan) ◦ ℓ−an1(x)

L

2(d+2)

![image 486](<2014-jiang-linear-profile-decompositions-family_images/imageFile486.png>)

d t,x

→ 0.

Since

- (56) (e−it∆(φ ◦ ℓan)) ◦ ℓ−an1 = eit|ℓan(−i∇)|2φ, the limit in (55) equals zero if and only if
- (57) lim n→∞

[eit(

∆2

![image 487](<2014-jiang-linear-profile-decompositions-family_images/imageFile487.png>)

|an|2 +4i|∆a∇an

![image 488](<2014-jiang-linear-profile-decompositions-family_images/imageFile488.png>)

n|2 ) − 1]eit|ℓan(−i∇)|2φ

L

2(d+2) d t,x

![image 489](<2014-jiang-linear-profile-decompositions-family_images/imageFile489.png>)

= 0, if |an| → ∞.

Similar computations show that (47), (48), (49), and (50) would (respectively) follow from lim

n→∞

[e−ith2n∆ − 1]eit∆2φ

L

2(d+2) d t,x

![image 490](<2014-jiang-linear-profile-decompositions-family_images/imageFile490.png>)

- (58) = 0, if hn → 0,

lim

n→∞

[ei

t h2

![image 491](<2014-jiang-linear-profile-decompositions-family_images/imageFile491.png>)

n

∆2 − 1]e−it∆φ

L

2(d+2) d t,x

![image 492](<2014-jiang-linear-profile-decompositions-family_images/imageFile492.png>)

- (59) = 0, if hn → ∞,

lim

n→∞

[eit(

∆2 h2

![image 493](<2014-jiang-linear-profile-decompositions-family_images/imageFile493.png>)

n

+4i∆h∇nξn) − 1]eit|ℓ˜ξn(−i∇)|2φ

![image 494](<2014-jiang-linear-profile-decompositions-family_images/imageFile494.png>)

L

2(d+2)

![image 495](<2014-jiang-linear-profile-decompositions-family_images/imageFile495.png>)

d t,x

- (60) = 0, if |ξn| 1, hn → ∞,

lim

n→∞

[eit(

∆2

![image 496](<2014-jiang-linear-profile-decompositions-family_images/imageFile496.png>)

|hnξn|2 +4|ih∆n∇ξnξn| −|ξ∆

![image 497](<2014-jiang-linear-profile-decompositions-family_images/imageFile497.png>)

![image 498](<2014-jiang-linear-profile-decompositions-family_images/imageFile498.png>)

n|2) − 1]eit|ℓξn(−i∇)|2φ

L

2(d+2) d t,x

![image 499](<2014-jiang-linear-profile-decompositions-family_images/imageFile499.png>)

- (61) = 0, if |ξn|,|hnξn| → ∞.


Since φ is smooth with compact support, [eit(

∆2

n|2 −|aµ∆

|an|2 +4i|∆a∇an

n|2) − 1]eit|ℓan(−i∇)|2φ → 0

![image 500](<2014-jiang-linear-profile-decompositions-family_images/imageFile500.png>)

![image 501](<2014-jiang-linear-profile-decompositions-family_images/imageFile501.png>)

![image 502](<2014-jiang-linear-profile-decompositions-family_images/imageFile502.png>)

pointwise in t,x, so (57) will follow from the dominated convergence theorem if we show that there exists a function that dominates each term in the sequence.

Let

2ξan

2

4

|an|2 + 4|ξ|

|an|2 + µ|ξ|

Φn(t,x,ξ) = t( |ξ|

|an|2 + |ℓan(ξ)|2) + xξ, Ψn(t,x,ξ) = t|ℓan(ξ)|2 + xξ.

![image 503](<2014-jiang-linear-profile-decompositions-family_images/imageFile503.png>)

![image 504](<2014-jiang-linear-profile-decompositions-family_images/imageFile504.png>)

![image 505](<2014-jiang-linear-profile-decompositions-family_images/imageFile505.png>)

2(d+2) d

![image 506](<2014-jiang-linear-profile-decompositions-family_images/imageFile506.png>)

Then the left hand side of (57) is the L

t,x norm of (t,x)  → [eiΦn(t,x,ξ) − eiΨn(t,x,ξ))] φ(ξ)dξ.

Since φ is smooth with compact support, this quantity is uniformly bounded. The gradients of the phases are

2an

2ξ

n|2 + 4|ξ|

∇ξΦn(t,x,ξ) = t(4|ξ|

|an|2 + 8|ξa·anξ

|an|2 + |a2µξ

n|2 + 2∇ℓan ◦ ℓan(ξ)) + x, ∇ξΨn(t,x,ξ) = 2tℓan ◦ ℓan(ξ) + x,

![image 507](<2014-jiang-linear-profile-decompositions-family_images/imageFile507.png>)

![image 508](<2014-jiang-linear-profile-decompositions-family_images/imageFile508.png>)

![image 509](<2014-jiang-linear-profile-decompositions-family_images/imageFile509.png>)

![image 510](<2014-jiang-linear-profile-decompositions-family_images/imageFile510.png>)

and for |an| ≫ (1 +R)2 and |x| > 100Rt, these are nonvanishing for ξ ∈ Supp φ ⊂ {R1 ≤ |ξ| ≤ R}. In particular,

![image 511](<2014-jiang-linear-profile-decompositions-family_images/imageFile511.png>)

- (62) |∇ξΦn(t,x,ξ)|,|∇ξΨn(t,x,ξ)| |x|, |x| > 100Rt. Furthermore, the Hessian matrices of the phases satisfy
- (63) Dξ2Φn(t,x,ξ),Dξ2Ψn(t,x,ξ) = t(Oξ,an(|aR2


n|2) + 2ℓ2an), where Oξ,an(|aR2

![image 512](<2014-jiang-linear-profile-decompositions-family_images/imageFile512.png>)

n|2) is a matrix whose coeﬃcients are uniformly bounded by |aR2

n|2, and we are

![image 513](<2014-jiang-linear-profile-decompositions-family_images/imageFile513.png>)

![image 514](<2014-jiang-linear-profile-decompositions-family_images/imageFile514.png>)

identifying the transformation ℓan with its matrix. Since 2ℓ2an is uniformly positive deﬁnite (indeed, its eigenvalues are 12,4,... ,4), for |an| suﬃciently large (depending on R), the critical points of the phases must be nondegenerate. Thus by (62), (63), and the principle of stationary phase (cf. Stein [29, Ch. VIII]),

d

d

| [eiΦn(t,x,ξ) − eiΨn(t,x,ξ))]φ(ξ)dξ| 1+ 1|x| Nχ{|x|≫t} + 1+ 1|t|

2χ{|x| t} 1+|t 1|+|x|

![image 515](<2014-jiang-linear-profile-decompositions-family_images/imageFile515.png>)

![image 516](<2014-jiang-linear-profile-decompositions-family_images/imageFile516.png>)

2.

![image 517](<2014-jiang-linear-profile-decompositions-family_images/imageFile517.png>)

![image 518](<2014-jiang-linear-profile-decompositions-family_images/imageFile518.png>)

![image 519](<2014-jiang-linear-profile-decompositions-family_images/imageFile519.png>)

2(d+2) d

![image 520](<2014-jiang-linear-profile-decompositions-family_images/imageFile520.png>)

The right hand side of the above inequality is in L

t,x , so (57) does indeed follow by the dominated convergence theorem.

The limits in (58), (59), (60), and (61) may be veriﬁed in a similar manner. (For (58) and (60), one also uses that 0 ∈/ Supp φ.) This completes the proof of Lemmas 4.3 and 4.4.

References

- [1] H. Bahouri and P. Ge´rard. High frequency approximation of solutions to critical nonlinear wave equations. Amer. J. Math., 121(1) (1999):131–175.
- [2] P. Be´gout and A. Vargas. Mass concentration phenomena for the L2-critical nonlinear Schr¨odinger equation. Trans. Amer. Math. Soc., 359(11) 2007: 5257–5282.
- [3] J. Bourgain. Reﬁnements of Strichartz’ inequality and applications to 2D-NLS with critical nonlinearity. Internat. Math. Res. Notices, (5) (1998):253–283.
- [4] R. Carles and S. Keraani. On the role of quadratic oscillations in nonlinear Schr¨odinger equations. II. The L2-critical case. Trans. Amer. Math. Soc., 359(1) (2007): 33–62 (electronic),.


- [5] M. Chae, S. Hong, S. Lee, Mass concentration for the L2-critical nonlinear Schr¨odinger equations of higher orders. Discrete Contin. Dyn. Syst. 29 (2011), no. 3, 909–928.
- [6] D. Foschi. Maximizers for the Strichartz inequality. J. Eur. Math. Soc. (JEMS), 9(4) (2007):739–774.
- [7] L. Guth. A restriction estimate using polynomial partitioning. Journal of the American Mathematical Society, 29(2) (2016):371–413.
- [8] D. Hundertmark and V. Zharnitsky. On sharp Strichartz inequalities in low dimensions. Int. Math. Res. Not., 18 pages Art. ID 34080, 2006.
- [9] J. Jiang, B. Pausader, and S. Shao. The linear proﬁle decomposition for the fourth order Schr¨odinger equation. J. Diﬀerential Equations, 249:2521–2547, 2010.
- [10] V. I. Karpman, Inﬂuence of high-order dispersion on self-focusing. I. Qualitative investigation. Physics Letters A. 160 (1991), 531–537.
- [11] V. I. Karpman, Lyapunov approach to the soliton stability in highly dispersive systems. I. Fourth order nonlinear Schr¨odinger equations. Physics Letters A. 215 (1996), 254–256.
- [12] V. I. Karpman, Stabilization of soliton instabilities by higher-order dispersion: Fourth-order nonlinear Schr¨odinger-type equations. Physical Review E. 53 (1996) no. 2, 1336–1339.
- [13] V. I. Karpman, A. G. Shagalov, Inﬂuence of high-order dispersion on self-focusing. II. Numerical investigation. Physics Letters A. 160 (1991), 538–540.
- [14] V. I. Karpman, A. G. Shagalov, Stability of solitons described by nonlinear Schr¨odinger-type equations with higher-order dispersion. Physica D. 144 (2000), 194–210.
- [15] M. Keel, T. Tao, Endpoint Strichartz estimates. Amer. J. Math. (1998), no. 5, 955–980.
- [16] C. E. Kenig, F. Merle, Global well-posedness, scattering and blow-up for the energy-critical, focusing, non-linear Schr¨odinger equation in the radial case. Invent. Math. 166 (2006), no. 3, 645–675.
- [17] C. E. Kenig, F. Merle, Global well-posedness, scattering and blow-up for the energy-critical focusing non-linear wave equation. Acta Math. 201 (2008), no. 2, 147–212.
- [18] R. Killip, S. Kwon, S. Shao, M. Visan, On the mass-critical generalized KdV equation. Discrete Contin. Dyn. Syst. 32 (2012), no. 1, 191–221.
- [19] R. Killip, B. Stovall, M. Visan, Scattering for the cubic Klein–Gordon equation in two space dimensions. Trans. Amer. Math. Soc. 364 (2012), 1571–1631.
- [20] R. Killip, T. Tao, M. Visan, The cubic nonlinear Schrdinger equation in two dimensions with radial data. J. Eur. Math. Soc. (2009), no. 6, 1203–1258.
- [21] R. Killip and M. Visan. Nonlinear Schr¨odinger equations at critical regularity. Lecture notes for the summer school of Clay Mathematics Institute, 2008.
- [22] R. Killip, M. Visan, X. Zhang, The mass-critical nonlinear Schr¨odinger equation with radial data in dimensions three and higher. Anal. PDE (2008), no. 2, 229–266.
- [23] F. Merle and L. Vega. Compactness at blow-up time for L2 solutions of the critical nonlinear Schr¨odinger equation in 2D. Internat. Math. Res. Notices, (8) (1998):399–425.
- [24] A. Moyua, A. Vargas, and L. Vega. Restriction theorems and maximal operators related to oscillatory integrals in R3. Duke Math. J., 96(3) (1999):547–574.
- [25] B. Pausader. Global well-posedness for energy critical fourth-order Schr¨odinger equations in the radial case. Dyn. Partial Diﬀer. Equ. 4 (2007), no. 3, 197–225.
- [26] B. Pausader and S. Shao. The mass critical fourth-order Schr¨odinger equation in high dimensions. Journal of Hyperbolic Diﬀerential Equations (JHDE), 7(4) (2010):651–705.
- [27] S. Shao. Maximizers for the Strichartz and the Sobolev-Strichartz inequalities for the Schr¨odinger equation. Electron. J. Diﬀerential Equations (2009), No. 3, 13 pp.
- [28] S. Shao, The linear proﬁle decomposition for the airy equation and the existence of maximizers for the airy Strichartz inequality. Anal. PDE 2 (2009), no. 1, 83–117.
- [29] E. M. Stein. Harmonic analysis: real-variable methods, orthogonality, and oscillatory integrals, volume 43 of Princeton Mathematical Series. Princeton University Press, Princeton, NJ, 1993. With the assistance of Timothy S. Murphy, Monographs in Harmonic Analysis, III.
- [30] T. Tao. A sharp bilinear restriction estimate for paraboloids. Geom. Funct. Anal., 13(6) (2003):1359–1384.
- [31] T. Tao, A. Vargas, and L. Vega. A bilinear approach to the restriction and Kakeya conjectures. J. Amer. Math. Soc., 11(4) (1998):967–1000.


Department of Mathematics, National Tsing Hua University, Hsinchu, Taiwan 30013, R.O.C. E-mail address: jcjiang@math.nthu.edu.tw

Department of Mathematics, University of Kansas, Lawrence, KS 66045 E-mail address: slshao@ku.edu

Department of Mathematics, University of Wisconsin, Madison, WI 53706 E-mail address: stovall@math.wisc.edu

