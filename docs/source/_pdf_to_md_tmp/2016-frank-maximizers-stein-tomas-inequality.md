arXiv:1603.07658v1[math.CA]23Mar2016

MAXIMIZERS FOR THE STEIN–TOMAS INEQUALITY

RUPERT L. FRANK, ELLIOTT H. LIEB, AND JULIEN SABIN

Abstract. We give a necessary and suﬃcient condition for the precompactness of all optimizing sequences for the Stein–Tomas inequality. In particular, if a wellknown conjecture about the optimal constant in the Strichartz inequality is true, we obtain the existence of an optimizer in the Stein–Tomas inequality. Our result is valid in any dimension.

1. Main result

A fundamental result in harmonic analysis is the Stein–Tomas theorem [30, 36], which states that if f ∈ L2(SN−1), N ≥ 2, then the inverse Fourier transform fˇ of

- f dω, with dω the surface measure on SN−1, that is,


1 (2π)N/2 SN−1

fˇ(x) :=

eix·ωf(ω) dω ,

![image 1](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile1.png>)

belongs to Lq(RN) with

q := 2(N + 1)/(N − 1) (1.1)

and its Lq(RN) norm is bounded by a constant times the L2(SN−1) norm of f. Moreover, it is well known that the exponent q is optimal (smallest possible) for this to hold for any f ∈ L2(SN−1).

In this paper we are interested in the optimal Stein–Tomas constant,

RN |fˇ|q dx f q

RN := sup

,

![image 2](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile2.png>)

0 ≡f∈L2(SN−1)

where   ·   denotes the norm in L2(SN−1). The value of RN and optimizing functions are only known in dimension N = 3 due to a remarkable work of Foschi [15]; see

- [11] for partial progress in N = 2. Our main concern here is whether the supremum deﬁning RN is attained and, more generally, the description of maximizing sequences for RN. These questions were recently considered in fundamental papers by Christ and Shao, where the existence of a maximizer for N = 3 [12] and N = 2 [29] was shown, as well as a precompactness result for maximizing sequences for N = 3 [13]. What makes dimensions N = 2 and 3 special is that the exponent q in (1.1) is an even integer, so that one can multiply out |fˇ|q. Our results will be valid in any dimension.


![image 3](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile3.png>)

c 2016 by the authors. This paper may be reproduced, in its entirety, for non-commercial purposes.

1

Christ and Shao discovered that for the problem of existence of an maximizer for RN a key role is played by the Strichartz inequality [32]. The optimal constant in this inequality is

R×Rd |eit∆/2ψ(x)|2+4/d dxdt ψ 2+4/d

Sd := (2π)−(d+2)/d sup

.

![image 4](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile4.png>)

0 =ψ∈L2(Rd)

(Here · denotes the norm in L2(Rd).) Note that 2 + 4/d = q when d = N − 1. The overall factor (2π)−(d+2)/d and the factor 1/2 in front of the Laplacian are not important, but simplify some formulas below.

We say that a sequence (fn) ⊂ L2(SN−1) is precompact in L2(SN−1) up to modulations if there is a subsequence (fn

) and a sequence (ak) ⊂ RN such that e−iak·ωfn

k

k

converges in L2(SN−1).

The following is our main result. Theorem 1.1. Let N ≥ 2. If

Γ(q+12 ) Γ(q+22 ) SN−1 , (1.2)

2q/2 √π

![image 5](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile5.png>)

RN >

![image 6](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile6.png>)

![image 7](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile7.png>)

![image 8](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile8.png>)

![image 9](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile9.png>)

then maximizing sequences for RN, normalized in L2(SN−1), are precompact in L2(SN−1) up to modulations and, in particular, there is a maximizer for RN.

Clearly, the optimization problem for RN is invariant under modulations, so precompactness up to modulations is the best one can expect. Our theorem says that assumption (1.2) is suﬃcient for this. In fact, it is easy to see that (1.2) is also necessary for the precompactness modulo modulations of all maximizing sequences. We will comment on this in Remark 2.5, where we will also see that (1.2) holds with ≥ instead of >.

As we will argue below, in dimensions N = 2 and N = 3, the strict inequality (1.2) holds and so we recover the Christ–Shao results on the existence of optimizers [12, 29] and precompactness in N = 3 [13] and we obtain, for the ﬁrst time, precompactness of maximizing sequences for N = 2.

We believe, but cannot prove, that the strict inequality (1.2) holds in any dimension. To verify it, it seems natural to ﬁrst compute SN−1 and then to use a perturbation argument to establish (1.2). In fact, by a remarkable work of Foschi [14] (see also [21, 5]), the value of SN−1 is known for N = 2 and N = 3. We cite the following conjecture from [14]; see also [21].

Conjecture 1.2. Let d ≥ 3. Then the supremum deﬁning Sd is attained for ψ(x) = e−x2/2, x ∈ Rd.

Assuming that this conjecture is true we can generalize an argument from [12, 29] and obtain existence of a maximizer for the Rd+1 problem.

- Proposition 1.3. Let N ≥ 4. If Conjecture 1.2 holds for d = N −1, then (1.2) holds and therefore the conclusions of Theorem 1.1 hold.


In connection with Conjecture 1.2 we would like to mention that the existence and precompactness problem for the optimization corresponding to Sd was solved by Kunze [23] in d = 1 and by Shao [28] in d ≥ 1. As we will explain next, this problem is considerably easier than that for RN since on the paraboloid {(ξ, ω) ∈ Rd × R : |ξ|2 = ω}, no points have parallel normal vectors (which is also a consequence of the fact that the paraboloid can be written globally as a graph and has non-vanishing curvature). In fact, our proof technique allows one to simplify the proofs in [23, 28].

Let us discuss some of the challenges in proving Theorem 1.1. As in most optimization problems the key diﬃculty here is to ﬁnd a weak limit of an optimizing sequence which is non-zero. There is an obvious way how a maximizing sequence can go weakly to zero, namely by modulations. However, potentially there is another way, namely by concentration and, in fact, the largest part of our proof is concerned with showing that concentration does not occur. If a sequence would concentrate at a point, we could approximate the sphere close to this concentration point by a paraboloid and we are in the setting of the Strichartz inequality. (Note that the Strichartz inequality is invariant under dilations.) Therefore, if a maximizing sequence concentrates at a point, one could naively expect that the largest possible ‘energy’ it can have is SN−1. What makes this problem interesting is that a maximizing sequence can do better than concentrating at a single point! Namely, it can concentrate at a pair of antipodal points. What we will show is that the largest possible ‘energy’ in this case is 2√q/π2 Γ(

q+1

2 )

![image 10](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile10.png>)

Γ(q+22 ) SN−1 with a factor

![image 11](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile11.png>)

![image 12](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile12.png>)

![image 13](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile13.png>)

![image 14](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile14.png>)

Γ(q+12 ) Γ(q+22 )

2q/2 √π

![image 15](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile15.png>)

> 1 .

![image 16](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile16.png>)

![image 17](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile17.png>)

![image 18](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile18.png>)

![image 19](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile19.png>)

From this and our assumption (1.2) we will deduce that maximizing sequences cannot concentrate at two antipodal points and therefore will be precompact.

The fact that a strict ‘energy’ inequality leads to precompactness of minimizing sequences is frequently used in the calculus of variations, for instance, in the linear Schro¨dinger operator theory. In a non-linear context it seems to appear for the ﬁrst time in the Br´ezis–Nirenberg problem [9, Lem. 1.2]. (Existence of minimizers, but not precompactness of minimizing sequences, under a strict ‘energy’ inequality was shown earlier in the Yamabe problem [3].) We emphasize that both in the Yamabe and in the Br´ezis–Nirenberg problem one has to deal with the loss of compactness due to concentration around a point.

However, the fact that concentration at two points is better than concentration at a single point is a non-local phenomenon and is a novel feature of the optimization problem RN. As far as we know, it does not appear in optimization problems related to Sobolev spaces (for instance, the Yamabe problem or the Br´ezis–Nirenberg problem mentioned before – not even in non-local versions of these problems) or in the optimization problem related to the Strichartz inequality. In order to deal with this non-local eﬀect we have to modify existing strategies in the calculus of variations and

we hope that our techniques will be useful in problems with a similar ﬂavor. In particular, our method should allow to solve the case of a general manifold with positive Gauss curvature. In this case the role of antipodal points is played by pairs of points with opposite normal vectors. For earlier results in the case of general curves (N = 2), but with pairs of points with opposite normal vectors excluded, we refer to [27].

The mechanism of antipodal concentration was discovered by Christ and Shao in

- [12]. In their analysis, however, the fact that q is even plays a major role. First, it allows them to restrict their attention to non-negative functions, which eliminates the loss of compactness due to modulations. More importantly, however, it also allows


- them to restrict their attention to antipodally symmetric functions. In this way the concentration at antipodal points is built into their proof automatically and, for instance, it is trivial in their case that the concentration happens with the same proﬁle at both points, whereas this is a non-trivial step in our proof.


In order to prove Theorem 1.1 we use the method of the missing mass (MMM) which was invented in [24] and [9, Lem. 1.2]; see also [8, 18] for early and [16, 17] for more recent applications of this method. The basic idea is to decompose a maximizing sequence into a main piece, which converges in a strong sense, and a remainder piece, which vanishes in a suitable sense. The goal of the decomposition is that each of the quantities involved in the maximization problem splits into a contribution of the main piece and the remainder piece, without any interaction between them. The crucial point is to not ignore the remainder piece (i.e., the missing mass), but to treat it as a potential optimizer. Because of the non-linear nature of the optimization problem, one can then conclude that the missing mass is either everything (which is impossible, since the main piece does not vanish) or nothing, which means that the maximizing sequence converges, in fact, strongly.

The MMM can deal both with exact symmetries (as in [8]) and with almost symmetries (as in [9]). One novelty of our work is that we need to apply the method twice, once to deal with the exact modulation symmetry (Proposition 2.2) and once to deal with the almost dilation symmetry (Proposition 2.4).

The method relies on two main ingredients which have to be veriﬁed in each problem. First, one needs to identify a main piece which does not vanish in the limit. This usually comes from a compactness theorem. In our case we prove a reﬁnement of the Stein–Tomas inequality (Proposition 5.1) which relies on a deep bilinear restriction theorem of Tao [33]. Our strategy here is reminiscent of Tao’s proof of what he calls the ‘inverse Strichartz theorem’ [34]. We feel that this approach is more direct than earlier approaches using Xp spaces, which were used in connection with reﬁned Strichartz inequalities (and were also an ingredient in [23, 28]). Reﬁnements of the Stein–Tomas inequality in terms of these spaces also play an important role in the works of Christ–Shao [12] and Shao [29].

The second ingredient in the MMM is the decoupling of the main and the remainder piece. While for a Hilbertian norm involved in the maximization problem this follows

simply from weak convergence, one usually uses almost everywhere convergence and the Br´ezis–Lieb lemma [24, 7] for an Lq norm. Indeed, we are able to verify almost everywhere convergence in our setting by proving an analogue of the local smoothing property of the Schro¨dinger equation (Lemma 4.4). However, we need a generalization of the Br´ezis–Lieb lemma (Lemma 3.1) since in our second application of MMM the main piece will not be convergent. Nevertheless, we will be able to separate its contribution from that of the remainder piece. The fact that the main piece is not convergent is ultimately a consequence of the non-local interaction between concentration points.

The outline of this paper is as follows. In Section 2 we present the overall strategy of our argument in more detail and explain how the MMM works. Section 3 contains the new generalization of the Br´ezis–Lieb lemma, Section 4 the results on almost everywhere convergence and Section 5 (and Appendix A) the compactness result mentioned before. In Section 6 we complete the computation of the compactness level by showing that, if concentration at antipodal points happens, then it is energetically favorable to have the same concentration proﬁle on both points. Finally, Section 7 is devoted to the proof of Proposition 1.3.

Acknowledgement. R.L.F. and J.S. would like to thank D. Oliveira e Silva and C. Thiele for the summer school ‘Sharp inequalities in harmonic analysis’ in August 2015 which stimulated our interest in this project. Partially support by U.S. National Science Foundation DMS-1363432 (R.L.F.) and PHY-1265118 (E.H.L.) is acknowledged.

2. Outline of the proof. Method of the missing mass

In this section we explain the main steps in the proof of Theorem 1.1. In Proposition 2.2 we will show that the conclusions of Theorem 1.1 hold if 2√q/π2 Γ(

q+1

2 )

![image 20](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile20.png>)

Γ(q+22 ) SN−1 on the right side of (1.2) is replace by a certain quantity R∗N, which is abstractly deﬁned through certain sequences in L2(SN−1) that converge weakly to zero. In a second step in Proposition 2.4 we will show that

![image 21](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile21.png>)

![image 22](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile22.png>)

![image 23](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile23.png>)

![image 24](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile24.png>)

R∗N = S˜N−1 , (2.1)

where S˜N−1 is a quantity deﬁned in terms of pairs of functions in L2(RN−1) and is a generalization of the Strichartz constant SN−1. Finally, in Section 6 we will show that

Γ(q+12 ) Γ(q+22 ) Sd , (2.2)

2q/2 √π

![image 25](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile25.png>)

S˜d =

![image 26](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile26.png>)

![image 27](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile27.png>)

![image 28](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile28.png>)

![image 29](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile29.png>)

which will complete the proof of Theorem 1.1. We now present these steps in more detail.

Deﬁnition 2.1. Let (fn) ⊂ L2(SN−1). We write fn ⇀mod 0

if for every sequence (an) ⊂ RN one has e−ia

n·ωfn ⇀ 0 in L2(SN−1) .

(Here and in the following, we slightly abuse notation and write e−ian·ωf for the function ω  → e−ian·ωf(ω).)

Deﬁne

R∗N := sup limsup

|fˇn|q dx : fn = 1 , fn ⇀mod 0 .

RN

- Proposition 2.2. If RN > R∗N ,


- then maximizing sequences for RN, normalized in L2(SN−1), are precompact in L2(SN−1) up to modulations and, in particular, there is a maximizer for RN. Proof. Let (fn) ⊂ L2(SN−1) be a maximizing sequence with fn = 1. Since


|fˇn|q dx = RN > R∗N ,

lim

RN

we infer that fn ⇀mod 0. That is, there is an h ∈ L2(SN−1) and a sequence (an) ⊂ RN such that limsupn→∞ he−ia

n·ωfn dω > 0. After passing to a subsequence we may assume that infn he−ian·ωfn dω > 0. By weak compactness, after passing to another subsequence, we may assume that e−ian·ωfn ⇀ g in L2(SN−1). Then he−ian·ωfn dω →

hg dω and this is non-zero, so we conclude that g  ≡ 0. Let us denote rn := e−ian·ωfn − g. Then rn ⇀ 0 in L2(SN−1) and therefore

rn 2 exists and satisﬁes 1 = g 2 + m.

m := lim

n→∞

Moreover, since eix·ω ∈ L2(SN−1), weak convergence implies that rˇn → 0 pointwise and therefore, by the Br´ezis–Lieb lemma [24, 7],

r ˇn qq exists and satisﬁes RN = g ˇ qq + µ . Since r ˇn qq ≤ RN rn q, we have µ ≤ RNmq/2 and therefore

µ := lim

n→∞

RN = g ˇ qq + µ ≤ g ˇ qq + RNmq/2 = g ˇ qq + RN(1 −  g 2)q/2 ≤ g ˇ qq + RN − RN g q , where we used the elementary inequality (1 − t)q/2 ≤ 1 − tq/2 for t ∈ [0, 1]. Thus, we have shown that 0 ≤ g ˇ qq − RN g q, which means that g is a maximizer (recall that

- g  ≡ 0) and that equality must hold everywhere. Since the elementary inequality is strict unless t ∈ {0, 1}, we conclude that g 2 = 1. Thus, m = 0, which means that e−ian·ωfn converges to g strongly in L2(SN−1). This completes the proof.


This proposition reduces the proof of our main theorem to showing that

Γ(q+12 ) Γ(q+22 ) SN−1 ,

2q/2 √π

![image 30](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile30.png>)

R∗N =

![image 31](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile31.png>)

![image 32](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile32.png>)

![image 33](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile33.png>)

![image 34](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile34.png>)

which we will verify in two steps. Let S˜d := (2π)−(d+2)/d

e−it∆/2ψ−(x) 2+4/d dxdt ( ψ+ 2 + ψ− 2)1+2/d

eit∆/2ψ+(x) + eiλx

limλ→∞ R×R

N

d

.

× sup

![image 35](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile35.png>)

(0,0) =(ψ+,ψ−)∈L2(Rd)2

It is easy to see that the limit λ → ∞ exists. We discuss this in some more detail before Lemma 6.1.

Our next goal is to prove equality (2.1). Intuitively, this equality says that for the

computation of R∗N we only need to consider sequences which concentrate on a pair of antipodal points. Approximating the sphere near the concentration points by a pa-

raboloid, we arrive at S˜N−1. (The factor of (2π)−(d+2)/d comes from the normalization of the Fourier transform.)

In order to make this intuition precise we have to quantify the notion of concentration. We will introduce a family of maps BR,δ with R ∈ O(N) and δ > 0 which identiﬁes pairs of functions on L2(RN−1) with a function on L2(SN−1). The orthogonal matrix R ∈ O(N) will determine the equator along which we cut the function in L2(SN−1) into two pieces. The parameter δ > 0 corresponds to a scaling in L2(RN−1).

We begin with the case R = Id, in which the equator along which we cut is the standard equator. For ϕ+, ϕ− ∈ L2(RN−1) and δ > 0 we deﬁne a function Bδ(ϕ+, ϕ−) ∈ L2(SN−1) by  

1 1 + ξ2

ξ 1 + ξ2

:= (1 + ξ2)N/4 δ−(N−1)/2 ϕ+(ξ/δ),

Bδ(ϕ+, ϕ−)

,

![image 36](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile36.png>)

![image 37](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile37.png>)

![image 38](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile38.png>)

![image 39](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile39.png>)

(2.3)

, −1 1 + ξ2

ξ 1 + ξ2

:= (1 + ξ2)N/4 δ−(N−1)/2 ϕ−(ξ/δ)

Bδ(ϕ+, ϕ−)



![image 40](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile40.png>)

![image 41](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile41.png>)

![image 42](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile42.png>)

![image 43](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile43.png>)

for ξ ∈ RN−1. (It is inessential that Bδ(ϕ+, ϕ−) is not deﬁned on the set {ω ∈ SN−1 : ωN = 0} of measure zero.) A simple change of variables shows that

 Bδ(ϕ+, ϕ−) 2 = ϕ+ 2 + ϕ− 2 . (2.4)

The map Bδ will be BR,δ with R = Id. Now for any R ∈ O(N), ϕ+, ϕ− ∈ L2(RN−1), and δ > 0 we deﬁne a function BR,δ(ϕ+, ϕ−) ∈ L2(SN−1) by

BR,δ(ϕ+, ϕ−)(ω) = Bδ(ϕ+, ϕ−)(R−1ω) . (2.5)

Since Bδ concentrates as δ → 0 around the north pole (0, . . ., 0, 1) and the south pole (0, . . ., 0, −1), BR,δ concentrates around R(0, . . ., 0, 1) and R(0, . . ., 0, −1) as δ → 0.

Deﬁnition 2.3. Let (fn) ⊂ L2(SN−1). We write fn ⇀conc 0

if for all sequences (an) ⊂ RN, (Rn) ⊂ O(N) and (δn) ⊂ (0, ∞) with supδn < ∞ one has

BR−n1,δn e−ia

n·ωfn ⇀ (0, 0) in L2(RN−1) × L2(RN−1) .

(Recall that, with our slight abuse of notation, e−ian·ωf denotes the function ω  → e−ian·ωf(ω).)

Let us brieﬂy comment on this deﬁnition. At ﬁrst sight it might look unnecessary to include a sequence of orthogonal maps (Rn) in this deﬁnition since the space O(N) is compact and hence, up to a subsequence, (Rn) will converge to a ﬁxed orthogonal map. However, if δn → 0, the sphere gets ‘blown-up’ and the maps (Rn) might move a point on the sphere on a distance 1/δn when looking around the concentration point at the scale 1/δn. As a consequence, the (Rn) play the role of the v-translations (modulation symmetry) in the symmetries of the Strichartz inequality (see the appendix of [34]). The importance of keeping these rotations will become clear in the proof of Lemma 5.2. Let us also remark that the analogue of our (an) are (tn, xn)-translations in the Strichartz case.

Our deﬁnition of the convergence fn ⇀conc 0 is speciﬁc to the sphere: we used that any rotation stabilizes the sphere. If one tries to adapt our approach to a general compact manifold with positive Gauss curvature one probably needs to work with local versions of the B operators.

We introduce two auxiliary functions ζ1, ζ2 on [0, ∞) by ζ1(k) =

1 √1 + k2

2 k2

1 √1 + k2

1 −

, ζ2(k) =

.

![image 44](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile44.png>)

![image 45](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile45.png>)

![image 46](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile46.png>)

![image 47](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile47.png>)

![image 48](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile48.png>)

For ψ ∈ L2(RN−1) we deﬁne with x = (x′, xN) ∈ RN−1 × R (Tδψ)(x) :=

ψ(ξ)ei(ξ·x′ζ1(δ|ξ|)−12ξ2xNζ2(δ|ξ|)) dξ (1 + δ2ξ2)N/4

1 (2π)(N−1)/2

. (2.6)

![image 49](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile49.png>)

![image 50](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile50.png>)

![image 51](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile51.png>)

RN−1

The operators Tδ arise naturally in this context since for any pair of functions ψ+, ψ− ∈ L2(RN−1) and any δ > 0, setting

f := Bδ( ψ+, ψ−) ,

we ﬁnd δ−(N−1)/2fˇ(x′/δ, xN/δ2) = (2π)−1/2 eix

N/δ2 Tδψ+ (x) + e−ix

N/δ2 Tδψ− (x′, −xN) .

(2.7) This follows by a simple change of variables.

We are now able to carry out the second step in the proof of Theorem 1.1, which is a variation of the argument used to prove Proposition 2.2 combined with a compactness theorem for the fn ⇀conc 0 convergence (Corollary 5.3) and two convergence theorems for the operators Tδ (Propositions 4.1 and 4.3).

Proposition 2.4. R∗N = S˜N−1 Proof. We begin with the proof of ≤. Let (fn) ⊂ L2(SN−1) be a sequence with

fn = 1, fn ⇀mod 0 and f ˇn qq → R∗N. We may assume that R∗N > 0, for otherwise there is nothing to prove, and therefore fˇn  → 0 in Lq(RN). According to Corollary 5.3

and weak compactness, after passing to a subsequence, we may assume that there are sequences (an) ⊂ RN, (Rn) ⊂ O(N) and (δn) ⊂ (0, ∞) with sup δn < ∞ and functions ψ+, ψ− ∈ L2(RN−1) with

ψ+ 2 + ψ− 2 = 0 (2.8)

such that BR−n1,δn (e−ian·ωfn) ⇀ ( ψ+, ψ−) in L2(RN−1) × L2(RN−1). Since fn ⇀mod 0, we have δn → 0. Because of rotation and modulation invariance of the problem, we may assume that Rn = Id and an = 0 for all n and we write Bδn

instead of BRn,δn. We deﬁne

( ψ+, ψ−) . We shall show that

( ψ+, ψ−) and rn := fn − Bδn

pn := Bδn

rn 2 exists and satisﬁes 1 = ψ+ 2 + ψ− 2 + m (2.9) and

m := lim

n→∞

|rˇn|q dx exists and satisﬁes R∗N = P + µ , (2.10) where

µ := lim

n→∞ RN

|πn|q dx and

P := lim

n→∞ RN

N/δn2 eix

N/δn2 e−ix

πn(x) := (2π)−1/2 eix

N∆/2ψ+ (x′) + e−ix

N∆/2ψ− (x′) .

(The fact that the limit deﬁnining P exists is again a consequence of the arguments before Lemma 6.1. In fact, we do not really need here the existence of the limit, but could simply work with the limsup in the deﬁnitions of both µ and P.)

Before proving (2.9) and (2.10), let us show that they imply the proposition. Since δn → 0 we have Bδn

( ψ+, ψ−) ⇀mod 0, and since fn ⇀mod 0 by assumption, we have rn ⇀mod 0. Thus,

µ ≤ R∗N mq/2 . (2.11) (In fact, if m = 0, this follows from the Stein–Tomas inequality and, if 0 < m < 1, it follows by using the deﬁnition of R∗N for the sequence rn/ rn .) Combining (2.9), (2.10) and (2.11) and recalling the elementary inequality used in the proof of Proposition 2.2 we obtain

R∗N = P + µ ≤ P + R∗Nmq/2 = P + R∗N 1 − ψ+ 2 − ψ− 2 q/2

≤ P + R∗N 1 − ψ+ 2 + ψ− 2 q/2 , that is,

R∗N ψ+ 2 + ψ− 2 q/2 ≤ P . Because of (2.8) this is the claimed upper bound on R∗N.

It remains to prove (2.9) and (2.10). For the proof of (2.9) we recall the unitarity relation (2.4) for Bδn

. Thus, the weak convergence Bδ−n1rn ⇀ 0 implies

2

2

+ Bδ−n1rn 2 + o(1) . Using once again  Bδ−n1rn 2 = rn 2, we obtain (2.9).

1 = fn 2 = Bδ−n1fn 2 = ( ψ+, ψ−) + Bδ−n1rn

= ( ψ+, ψ−)

For the proof of (2.10) we denote ( ψn+, ψn−) := Bδ−n1fn and decompose, using (2.7), δn−(N−1)/2fˇn(x′/δn, xN/δn2) = πn(x) + ρn(x) + σn(x) , where we have set

N/δn2ρ−n (x′, −xN) with

N/δn2ρ+n(x′, xN) + e−ix

ρn(x) := (2π)−1/2 eix

ψn± − ψ± (x) and

ρ±n (x) := Tδn

N/δn2σn−(x′, −xN) with

N/δn2σn+(x′, xN) + e−ix

σn(x) := (2π)−1/2 eix

N∆/2ψ± (x′) . It follows from Proposition 4.3 that, after passing to a subsequence if necessary, ρ±

ψ± (x) − eix

σn±(x) := Tδn

n → 0 almost everywhere and from Proposition 4.1 that σ±

n → 0 in Lq. Moreover, |πn(x)| ≤ (2π)−1/2 eix

N∆/2ψ− (x′) ∈ Lqx(RN) . Therefore, the generalized Br´ezis–Lieb Lemma 3.1 implies

N∆/2ψ+ (x′) + e−ix

RN

δn−(N−1)/2fˇn(x′/δn, xN/δn2) q dx =

|πn(x)|q dx +

RN

RN

By scaling, the left side equals f ˇn qq and, since ρn(x) = δn−(N−1)/2rˇn(x′/δn, xN/δn2) ,

|ρn(x)|q dx + o(1) .

the second term on the right side equals r ˇn qq. Taking the limit as n → ∞ and using the fact that the limit deﬁnining P exists we obtain (2.11). This completes the proof of the inequality ≤ in the proposition.

The proof of the inequality ≥ is similar, but simpler. Indeed, pick any pair of functions (ψ+, ψ−) ∈ L2(RN−1)2 such that ψ+ 2 + ψ− 2 = 1 and any sequence (δn) of positive numbers converging to zero. Then, the sequence fn := Bδn

( ψ+, ψ−) satisﬁes fn = 1 and fn ⇀mod 0. As a consequence,

|fˇn|q dx ≤ R∗N.

limsup

n→∞ RN

On the other hand, by the same method as in the proof of the inequality ≤, we have liminf

|fˇn|q dx

n→∞ RN

q

N/δn2 e−ix

N∆/2ψ− (x′)

≥ (2π)−q/2 lim

eix

N∆/2ψ+ (x′) + e−2ix

dx,

n→∞ RN

showing that S˜N−1 ≤ R∗N.

To complete the proof of Theorem 1.1 it suﬃces to show equality (2.2). This is the content of Corollary 6.2. Remark 2.5. Similar arguments to those used before show that

Γ(q+12 ) Γ(q+22 ) SN−1 , (2.12)

2q/2 √π

![image 52](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile52.png>)

RN ≥

![image 53](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile53.png>)

![image 54](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile54.png>)

![image 55](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile55.png>)

![image 56](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile56.png>)

which is the non-strict version of (1.2). In fact, we clearly have RN ≥ R∗N, so that (2.12) follows from Proposition 2.4 and (2.2). Moreover, by deﬁnition there is a se-

quence (fn) ⊂ L2(SN−1) with fn = 1 and f ˇn qq → R∗N which is not precompact in L2(SN−1). Thus, the strict inequality (1.2) is necessary for the precompactness of all maximizing sequences.

3. A generalization of the Br´ezis–Lieb lemma

The following abstract lemma decouples the main piece from a remainder piece that converges to zero almost everywhere.

- Lemma 3.1. Let (X, dx) be a measure space and p > 0. Let (αn) be a bounded sequence in Lp(X) such that


αn = πn + ρn + σn , where, for some Π ∈ Lp(X),

|πn| ≤ Π for all n and where

ρn → 0 almost everywhere and σn → 0 in Lp(X) . Then

|αn|p dx =

|πn|p dx +

|ρn|p dx + o(1) as n → ∞ .

X

X

X

Note that, if πn is independent of n and σn = 0, this is the result from [24] which was generalized in [7]. Our lemma follows by similar arguments as in [7]. Proof. As a preliminary step we show that the asymptotics are independent of σn. By the triangle inequality we have for p ≥ 1,

αn p − πn + ρn p ≤ σn p

and for 0 < p ≤ 1

αn pp − πn + ρn pp ≤ σn pp . We conclude that

|αn|p dx =

|πn + ρn|p dx + o(1) .

X

X

(For p > 1 we also use the fact that supn αn p and supn πn + ρn p are ﬁnite; see the proof below.) Thus, the lemma will follow if we can prove that

||πn + ρn|p − |πn|p − |ρn|p|dx = o(1) as n → ∞ . (3.1) Let ε > 0 and put

X

Rn := (||πn + ρn|p − |πn|p − |ρn|p| − ε |ρn|p)+ . Then

||πn + ρn|p − |πn|p − |ρn|p| dx ≤ ε

|ρn|p dx +

Rn dx, and asymptotics (3.1) will follow if we can prove that

X

X

X

|ρn|p dx < ∞ (3.2) and

limsup

n→∞ X

Rn dx = o(1) as n → ∞ . (3.3) For the proof of (3.2) we simply bound

X

|ρn|p ≤ Cp (|αn|p + |πn|p + |σn|p) ≤ Cp (|αn|p + Πp + |σn|p) with Cp = 3p−1 if p ≥ 1 and Cp = 1 if p < 1. Thus, by assumption,

(|αn|p + Πp) dx < ∞ , which gives (3.2).

|ρn|p dx ≤ Cp limsup

limsup

n→∞ X

n→∞ X

We will prove (3.3) by dominated convergence. Clearly, there is a Cε,p such that for all a, b ∈ C,

||a + b|p − |b|p| ≤ ε |b|p + Cε,p |a|p . Thus,

||πn + ρn|p − |πn|p − |ρn|p| ≤ ||πn + ρn|p − |ρn|p| + |πn|p ≤ ε |ρn|p + (Cε,p + 1)|πn|p and so

Rn ≤ (Cε,p + 1)|πn|p ≤ (Cε,p + 1) Πp . By assumption, the right side is integrable.

To complete the proof we show that Rn → 0 almost everywhere. Note that ρn → 0 almost everywhere and that |πn| ≤ Π. The set {ρn → 0} ∩ {Π < ∞} has full measure and on this set we have Rn → 0 almost everywhere. This simply follows from

the fact that for sequences (an), (bn) ⊂ C with sup|an| < ∞ and bn → 0, we have |an + bn|p − |an|p → 0 for any p > 0. This proves the lemma.

4. Some a-priori estimates and convergence results

In this section we discuss the convergence properties of the operators Tδ from (2.6) as δ → 0. These properties were used in the proof of Proposition 2.4. As we have already seen in Section 2, the operators Tδ appear naturally in our problem for functions on SN−1 which concentrate near the north pole with the parameter δ denoting the scale on which the functions live.

- 4.1. Lq convergence. We recall that we always assume q = 2(N + 1)/(N − 1). The purpose of this subsection is to prove the following convergence result. Proposition 4.1. Let ψ ∈ L2(RN−1). Then, as δ → 0,


N∆/2ψ (x′) in Lq(RN) . We begin with an a-priori bound for Tδ.

(Tδψ) (x) → eix

- Lemma 4.2. Tδ is a bounded operator from L2(RN−1) to Lq(RN) and  Tδ L2→Lq is independent of δ > 0. Proof of Lemma 4.2. We claim that for all ψ ∈ L2(RN−1) and for all x ∈ RN,


N/δ2(VδF−1BUδFψ)(x) . (4.1)

(Tδψ)(x) = (2π)1/2e−ix

where Vδ and Uδ are isometric isomorphisms in Lq(RN) and L2(RN), respectively, F denotes the Fourier transform and B is a unitary operator from L2(RN−1) to L2(SN−1

+ ) (SN−1

+ denoting the northern hemisphere). Thus,  Tδ L2→Lq = (2π)1/2 F−1 L2(SN+−1)→Lq(RN) ,

which is ﬁnite by the Stein–Tomas theorem. The operators Vδ−1 and Uδ are simply deﬁned by

(VδF)(x) = δ−(N+1)/qF(x′/δ, xN/δ2) , (Uδϕ)(ξ) = δ−(N−1)/2ϕ(ξ/δ) . The operator B is deﬁned by

1 1 + ξ2

ξ 1 + ξ2

= (1 + |ξ|2)N/4ϕ(ξ) . (4.2)

(Bϕ)

,

![image 57](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile57.png>)

![image 58](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile58.png>)

![image 59](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile59.png>)

![image 60](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile60.png>)

The fact that B is a unitary operator from L2(RN−1) to L2(SN−1

+ ) follows by a simple change of variables. The claimed identity (4.1) follows by the same change of variables.

We now use this lemma to prove the proposition.

Proof of Proposition 4.1. Because of Lemma 4.2 it suﬃces to prove the proposition for ψ ∈ L2(RN−1) with ψ ∈ C∞

c (RN−1). For such ψ we shall show that for all (x′, xN) ∈ RN,

(Tδψ) (x′, xN) = eix

N∆/2ψ (x′) , (4.3)

lim

δ→0

|(Tδψ) (x′, xN)| + eix

N∆/2ψ (x′) ≤ C|x|−(N−1)/2 (4.4)

for some constant C > 0 independent of δ (but dependent of ψ). The limit (4.3) follows immediately from Lebesgue’s dominated convergence theorem, since we have the correct limit under the integral and ψ ∈ L1(RN−1). Assume for the moment the decay estimate (4.4) and let us show that this implies the claimed Lq convergence. We have for some C′ and all δ > 0

C′ R

N∆/2ψ (x′) q dx ≤

|(Tδψ) (x)|q + eix

.

![image 61](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile61.png>)

|x|≥R

This can be made arbitrarily small, uniformly in δ > 0, by choosing R > 0 large. Thus, it suﬃces to prove that for any ﬁxed R > 0

(x) eix

N∆/2ψ (x′) in Lq(RN) ,

χB

(x) (Tδψ) (x) → χB

R

R

where BR denotes the ball of radius R > 0. This follows immediately by dominated convergence from the pointwise convergence (4.3) together with the uniform bound

|(Tδψ) (x)| ≤ (2π)−(N−1)/2

| ψ(ξ)| dξ < ∞ .

RN−1

Thus, it thus remains to prove the decay estimate (4.4), which follows from stationary phase estimates as in Stein [31, p.349]. Let us recall how it is done when there is no dependence on δ. The integral

1 (2π)(N−1)/2

′·ξ−ixNξ2/2 ψ(ξ) dξ can be written as an oscillatory integral

eix

N∆/2ψ (x′) =

eix

![image 62](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile62.png>)

RN−1

eiλΦ(ω,ξ)a(ξ) dξ

RN−1

with a large parameter λ = |x|, a smooth phase function Φ(ω, ξ) = ω′ · ξ − ωNξ2/2, where ω = (ω′, ωN) ∈ SN−1, and an amplitude a = ψ/(2π)N−1 ∈ C∞

c (RN−1). We distinguish two cases: when ω is close to the poles, then the phase has critical points but we have a uniform lower bound on the determinant of the Hessian, so we may use stationary phase. Away from the poles, there is no critical point and we have a uniform lower bound on |∇Φ|, so that we may use integration by parts.

First, when |ωN| ≥ b for some 0 < b < 1 to be determined later (that is, when ω is close to the poles), then the phase is stationary at the points where

∇ξΦ(ω, ξ) = ω′ − ωNξ = 0,

that is for ξ = ω′/ωN. Furthermore, we have Dξ2Φ(ω, ξ) = ωN, meaning that

| detDξ2Φ(ω, ξ)| = |ωN|N−1 ≥ bN−1. All the ξ-derivatives of a and Φ are uniformly bounded in ω in this region, so that we may use the uniform stationary phase estimates of Alazard, Burq, and Zuily [1] to infer that

eiλΦ(ω,ξ)a(ξ) dξ ≤ Ca,bλ−(N−1)/2

RN−1

for all ω such that |ωN| ≥ b. In the region |ωN| ≤ b, we have |ω′| ≥ (1 − b2)1/2 and hence

√

![image 63](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile63.png>)

1 − b2 − bR,

|∇ξΦ(ω, ξ)| ≥

where√1 − bR2/b>>0 isR,suchthenthatthe suppphaseahas⊂ Bno(0, Rcritical). Hence,pointif andb is suﬃcientlywe have bysmallintegrationsuch thatby parts

![image 64](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile64.png>)

eiλΦ(ω,ξ)a(ξ) dξ ≤ Cn(a)λ−n

RN−1

for any n ∈ N, where Cn(a) is uniform in ω such that |ωN| ≤ b, since we have a uniform lower bound on |∇ξΦ| in this region and uniform upper bounds on higher ξ-derivatives of Φ.

We have to do the same thing when δ > 0, and all the bounds that were uniform in ω should now be uniform in (ω, δ). In this case, the new phase function has the form

ξ2 2

Φ(δ, ω, ξ) = ω′ · ξζ1(δ|ξ|) − ωN

ζ2(δ|ξ|) , and the amplitude has the form

![image 65](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile65.png>)

ψ(ξ) (1 + δ2ξ2)N/4

.

a(δ, ξ) =

![image 66](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile66.png>)

The functions ξ  → ζ1(δ|ξ|) and ξ  → ζ2(δ|ξ|), and a are C∞ and satisfy ζ1(0) = 1 = ζ2(0). All the ξ-derivatives of Φ and a are uniformly bounded in (δ, ω), on the support of a. First, consider the case |ωN| ≥ b. We have

Dξ2Φ(δ, ω, ξ) = ωNζ2(δ|ξ|) + O(δ),

where the O(δ) is uniform in (ω, ξ) ∈ SN−1×supp(a). Hence, there exists δ0 = δ0(R) > 0 such that

N−1

b 2

| detDξ2Φ(δ, ω, ξ)| ≥

,

![image 67](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile67.png>)

for all |ωN| ≥ b, 0 ≤ δ ≤ δ0, ξ ∈ supp(a). Using again the result of Alazard–Burq– Zuily (notice here that we do not need to describe where the critical points are, a lower bound on the determinant of the Hessian is enough to apply their result - we could have done the same in the δ = 0 case actually), we obtain again that

eiλΦ(δ,ω,ξ)a(δ, ξ) dξ ≤ Ca,bλ−(N−1)/2

RN−1

for all ω such that |ωN| ≥ b and all 0 ≤ δ ≤ δ0. In the region |ωN| ≤ b, we use the fact that

∇ξΦ(δ, ω, ξ) = ω′ζ1(δ|ξ|) − ωNξζ2(δ|ξ|) + O(δ) , and hence

√

3 2

- 1

![image 68](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile68.png>)

- 2


![image 69](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile69.png>)

1 − b2 −

bR

|∇ξΦ(δ, ω, ξ)| ≥

![image 70](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile70.png>)

for all 0 ≤ δ < δ1(b, R), |ωN| ≤ b, ξ ∈ supp(a). For b = b(R) small enough, this lower bound is positive. Using again integration by parts with this uniform lower bound on |∇Φ|, we deduce

eiλΦ(ω,ξ)a(δ, ξ) dξ ≤ Cn(a)λ−n

RN−1

for any n ∈ N, where Cn(a) is uniform in (ω, δ) such that |ωN| ≤ b and 0 ≤ δ ≤ δ1. This ﬁnishes the proof of (4.4) and the proof of Proposition 4.1.

- 4.2. Almost everywhere convergence. While in the previous subsection we dealt


with Lq convergence of Tδn

ψ when δn → 0, we will now deal with almost everywhere convergence of Tδn

ψn when δn → 0 and ψn ⇀ 0 in L2(RN−1). The purpose of this subsection is to prove the following convergence result.

- Proposition 4.3. Let ψn ⇀ 0 in L2(RN−1) and δn → 0 in (0, ∞). Then Tδn


ψn → 0 in L2loc(RN) and, in particular, there is a subsequence such that Tδnk

k → 0 almost everywhere on RN.

ψn

The key ingredient in the proof of this proposition is the following analogue of the local smoothing property of the Schro¨dinger equation.

- Lemma 4.4. Let a ∈ S(RN−1) be radial. Then there is a constant Ca such that for all ψ ∈ L2(RN−1) and all δ > 0


2

1/4

−∆ −δ2∆ + 1

dx ≤ Ca ψ 2 . Let us show that this lemma implies the proposition.

a(x′) Tδ

ψ

![image 71](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile71.png>)

RN

- Proof of Proposition 4.3. Let K ⊂ RN be compact and let a ∈ S(RN−1) be radial with infx∈K a(x′) > 0 (for instance a Gaussian). Moreover, let Λ > 0 and denote by PΛ multiplication by the characteristic function of BΛ, the ball of radius Λ, in Fourier


space. We decompose, with P⊥

Λ = 1 − PΛ, χKTδn

PΛ⊥ψn . According to Lemma 4.4 we have

PΛψn + χKTδn

ψn = χKTδn

PΛ⊥ψn ≤ inf

a(x′)

χKTδn

x∈K

a(x′)

≤ inf

x∈K

1/4 −δn2∆ + 1 −∆

−1

−∆ −δn2∆ + 1

aTδ

![image 72](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile72.png>)

![image 73](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile73.png>)

−1

Ca12/2 δn2 + Λ−2 1/4 sup

ψn .

n

1/4

PΛ⊥ ψn

The right side can be made arbitrarily small by choosing Λ large, uniformly for large n. Therefore it suﬃces to prove that χKTδn

PΛψn tends to zero for each ﬁxed Λ. We will deduce this using dominated convergence. In fact, we have for each ﬁxed x ∈ RN,

(ξ)ei(ξ·x′−12ξ2xN)

(ξ)ei(ξ·x′ζ1(δ|ξ|)−12ξ2xNζ2(δ|ξ|))(1 + δ2ξ2)−N/4 → χB

χB

![image 74](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile74.png>)

![image 75](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile75.png>)

Λ

Λ

strongly in L2ξ(RN−1). (This can also be proved with the help of dominated convergence.) Thus, ψn ⇀ 0 implies that for any ﬁxed x ∈ RN,

e−i(ξ·x′ζ1(δ|ξ|)−21ξ2xNζ2(δ|ξ|))(1 + δ2ξ2)−N/4, ψn → 0 . Moreover, we have

PΛψn(x) = χB

Tδn

![image 76](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile76.png>)

Λ

e−i(ξ·x′ζ1(δ|ξ|)−21ξ2xNζ2(δ|ξ|))(1 + δ2ξ2)−N/4 ψn ≤ |BΛ|1/2 sup

PΛψn(x)| ≤ χB

|Tδn

![image 77](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile77.png>)

Λ

ψn .

n

PΛψn → 0 in L2(RN), which proves the ﬁrst part of the proposition.

Thus, dominated convergence implies χKTδn

The second part follows by a standard diagonalization argument using a sequence of balls with diverging radii and the fact that an L1 convergent sequence has an almost everywhere convergent subsequence.

It remains to give the

Proof of Lemma 4.4. Expanding the square, the left side of the term in the lemma reads

2π

ψ(ξ) |ξ|1/2 (1 + δ2ξ2)(N+1)/4

![image 78](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile78.png>)

a(ξζ1(δ|ξ|) − ξ′ζ1(δ|ξ′|))×

![image 79](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile79.png>)

RN−1×RN−1

ξ′2 2

ζ2(δ|ξ′|) |ξ′|1/2 (1 + δ2ξ′2)(N+1)/4

ξ2 2

ψ(ξ′) dξ dξ′.

ζ2(δ|ξ|) −

× δ

![image 80](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile80.png>)

![image 81](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile81.png>)

![image 82](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile82.png>)

By the Schur test for boundedness, the lemma will follow if we can bound

|ξ|1/2|ξ′|1/2 (1 + δ2ξ2)(N+1)/4(1 + δ2ξ′2)(N+1)/4| a(ξζ1(δ|ξ|) − ξ′ζ1(δ|ξ′|))|×

sup

![image 83](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile83.png>)

ξ RN−1

ξ′2 2

ξ2 2

ζ2(δ|ξ′|) dξ′

ζ2(δ|ξ|) −

× δ

![image 84](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile84.png>)

![image 85](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile85.png>)

independently of δ. In order to perform the ξ′ integral we write ξ′ = kω with ω ∈ SN−2 and k > 0. The functions Φδ(k) = k2ζ2(δk)/2 = δ−2 1 − 1/√1 + δ2k2 is a strictly increasing function, so we can change variables κ = Φδ(k). We use the fact that

![image 86](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile86.png>)

∞

F(k) δ(Φδ(|ξ|)−Φδ(k)) dk =

0

δ−2

dκ |Φ′

F(Φ−δ 1(κ)) δ(Φδ(|ξ|)−κ)

=

![image 87](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile87.png>)

δ(Φ−δ 1(κ))|

0

F(|ξ|) |Φ′

![image 88](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile88.png>)

δ(|ξ|)|

with Φ′

δ(k) = k(1 + δ2k2)−3/2. So Schur’s test amounts to estimating sup

|ξ|N−2 (1 + δ2ξ2)(N−2)/2

| a((ξ − |ξ|ω)ζ1(δ|ξ|))| dω . When N = 2, this is equal to

![image 89](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile89.png>)

ξ

SN−2

(| a(0)| + | a(2ξζ1(δ|ξ|))|), which is bounded since a is bounded.

sup

ξ

In the remainder of the proof we assume N ≥ 3. Since a is assumed to be radial, by rotation invariance we may choose ξ = |ξ|(0, . . ., 0, 1) and then the integral over the sphere becomes

|SN−3|

π

| a(2 sin(θ/2)|ξ|ζ1(δ|ξ|))|(sinθ)N−3 dθ .

0

We distinguish between two regions: when 2 sin(θ/2)|ξ|ζ1(δ|ξ|) ≥ 1, then we estimate | a(ξ′)| ≤ cn|ξ′|−n for any n ∈ N and obtain

| a(2 sin(θ/2)|ξ|ζ1(δ|ξ|))|(sinθ)N−3 dθ

2 sin(θ/2)|ξ|ζ1(δ|ξ|)≥1

(sinθ)N−3 (sin(θ/2))n

≤ cn(2|ξ|ζ1(δ|ξ|))−n

dθ,

![image 90](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile90.png>)

sin(θ/2)≥(2|ξ|ζ1(δ|ξ|))−1

Fix n ≥ N − 4. Then for large |ξ|, the integral blows up as

(sinθ)N−3 (sin(θ/2))n

θN−3−n dθ

dθ ∼ 2n

![image 91](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile91.png>)

θ≥(|ξ|ζ1(δ|ξ|))−1

sin(θ/2)≥(2|ξ|ζ1(δ|ξ|))−1

2n n − N + 3

(|ξ|ζ1(δ|ξ|))−(N−2−n). Thus, we ﬁnd that

=

![image 92](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile92.png>)

| a(2 sin(θ/2)|ξ|ζ1(δ|ξ|))|(sinθ)N−3 dθ n (|ξ|ζ1(δ|ξ|))−(N−2).

2 sin(θ/2)|ξ|ζ1(δ|ξ|)≥1

In the region 2 sin(θ/2)|ξ|ζ1(δ|ξ|) ≤ 1, we estimate | a| ≤ c and obtain

| a(2 sin(θ/2)|ξ|ζ1(δ|ξ|))|(sinθ)N−3 dθ

2 sin(θ/2)|ξ|ζ1(δ|ξ|)≤1

|θ|N−3 dθ (|ξ|ζ1(δ|ξ|))−(N−2). Inserting this bound into the supremum in Schur’s test, we obtain

≤ c

θ≤(|ξ|ζ1(δ|ξ|))−1

1 (1 + δ2ξ2)(N−2)/2

1

sup

ζ1(δ|ξ|)N−2 = 1 . This proves the lemma.

![image 93](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile93.png>)

![image 94](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile94.png>)

ξ

5. Compactness

In this section we prove a reﬁnement of the Stein–Tomas inequality and deduce a compactness theorem modulo modulations and concentrations. We recall that the convergence fn ⇀conc was introduced in terms of the operators BR,δ with R ∈ O(N) and δ > 0 which identify pairs of functions on L2(RN−1) with functions on L2(SN−1). The parameter R ∈ O(N) determines the equator along which we cut the function in L2(SN−1) into two pieces. The parameter δ > 0 corresponds to a scaling in L2(RN−1). The precise deﬁnition of these operators is given in (2.5). The reﬁned Stein–Tomas inequality is stated in Subsection 5.1, where we also use it to deduce the compactness theorem, and is proved in Subsection 5.2 (see also Appendix A).

- 5.1. Reﬁnement of the Stein–Tomas inequality. Our reﬁned Stein–Tomas inequality depends on a parameter ε ∈ (0, 1) that will be chosen small enough and that will not always be reﬂected in the notation. Given this parameter we consider for any θ ∈ SN−1 the cap


√

C(θ) := ω ∈ SN−1 : θ · ω >

![image 95](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile95.png>)

1 − ε2 , and we also pick an orthogonal matrix Rθ ∈ O(N) mapping the north pole to θ: Rθ(0, . . ., 0, 1) = θ.

To formulate our reﬁnement of the Stein–Tomas inequality we need an analogue of dyadic cubes on the sphere. Let D denotes the set of all dyadic cubes in RN−1, that is, the union over j ∈ Z of all cubes of side length 2j with corners on (2jZ)N−1. For θ ∈ SN−1 and Q ∈ D we let

Lθ(Q) := Rθ(L(Q)) , where L stands for “lift” and

L(Q) := {ω ∈ SN−1 : ω′ ∈ Q, ωN > 0}. Notice that

Lθ(Q) = {ω ∈ SN−1 : Pθ⊥(ω) ∈ Q, ω · θ > 0},

where Pθ⊥ : RN → RN is the orthogonal projection on θ⊥. By compactness of the sphere, there is a ﬁnite A ∈ N and points θα ∈ SN−1, α = 1, . . ., A, such that

A

C(θα) = SN−1 .

α=1

Correspondingly, we choose non-negative continuous functions χα, α = 1, . . ., A, with

A

χα = 1 and supp χα ⊂ C(θα) for all α = 1, . . ., A.

α=1

- Proposition 5.1. There are ε ∈ (0, 1), C > 0 and σ ∈ (0, 1) such that for any f ∈ L2(SN−1),


1−σ

θα(Q)χαf ∨

f ˇ Lq(RN) ≤ C sup

|Q|−1/2 1L

f σ . (5.1)

sup

L∞(RN)

α

Q∈D

Note that this proposition implies the standard Stein–Tomas inequality: indeed, for any α ∈ {1, . . ., A} and Q ∈ D we have

θα(Q)χαf ∨

≤ (2π)−N/2|Q|−1/2 1L

|Q|−1/2 1L

θα(Q)χαf L

1(SN−1)

L∞(RN)

≤ (2π)−N/2|Q|−1/2 1L

2(SN−1) f L2(SN−1) ≤ CN f L2(SN−1) ,

θα(Q)χα L

so the right side of (5.1) is bounded by a constant times f .

Other reﬁnements of the Stein–Tomas inequality can be found in [26, Thm. 4.2] in the case N = 3 or in [27, Prop. 2], [29, Prop. 4.1] in the case N = 2. These reﬁnements involve Xp-norms on f, but it is not obvious how to deduce our compactness result (Corollary 5.3) from these Xp estimates. The key feature of our reﬁnement is the L∞ norm of the Fourier transform on the right side of (5.1), leads almost immediately to Corollary 5.3. This is reminiscent of the route taken in [34, 22] in connection with the Strichartz inequality, where also L∞ bounds on the Fourier transform are used instead of the original Xp-spaces approach of [6, 25, 10, 4].

We also point out a certain similarity with the description of lack of compactness in homogeneous Sobolev spaces [19]. In this case analogous bounds in terms of L∞ norms of the Fourier transform are due to [20] (see also [22, Prop. 4.8]) and have been used to establish compactness results [19] (see also [22, Prop. 4.9]).

We defer the proof of Proposition 5.1 to Subsection 5.2 and use it now to deduce our compactness theorem. The relation between our convergence notion fn ⇀conc 0 and the norm appearing in Proposition 5.1 is clariﬁed in the following lemma.

- Lemma 5.2. The following holds provided ε > 0 is suﬃciently small. If (fn) is a bounded sequence in L2(SN−1) with fn ⇀conc 0, then


θα(Q)χαfn ∨

|Q|−1/2 1L

lim

sup

sup

= 0. (5.2)

n→∞

L∞(RN)

α

Q∈D

Proof. We argue by contradiction: assume that there exists ε′ > 0, α ∈ {1, . . ., A}, sequences (xk) ⊂ RN, (Qk) ⊂ D and a subsequence (fn

) such that for all k |Qk|−1/2 1L

k

∨ (xk) ≥ ε′. (5.3) We show that the left side converges to zero, obtaining the desired contradiction. In the sequel, we forget about the subsequence and write (fn)n instead of (fn

θα(Qk)χαfn

k

)k. We may also assume that θα = (0, . . ., 0, 1) up to replacing fn by fn ◦ Rθ

k

, which does not change the assumption fn ⇀conc 0. We thus write L(Q) and χ instead of Lθ

α

(Q) and χα. We may assume that the sets L(Qn) intersect {ω ⊂ SN−1 : ωN > √1 − ε2}

α

![image 96](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile96.png>)

(which contains the support of χ), for otherwise the left side of (5.3) vanishes, and therefore the cubes Qn all intersect {ξ ⊂ RN−1 : |ξ| < ε}. Let Q˜n be the smallest dyadic cube with 1L(Q˜

n)χ = 1L(Q

n)χ. Since

|Q˜n|−1/2 1L(Q˜

n)χfn

∨

n)χfn ∨ (xn) ,

(xn) ≥ |Qn|−1/2 1L(Q

it suﬃces to prove the convergence to zero with Q˜n in place of Qn. From now on we will write again Qn instead of Q˜n. Let kn ∈ ZN−1 and δn ∈ 2Z such that

Qn = δnkn + [0, δn)N−1 , and note that |Qn| = δN−1

n . The above redeﬁnition of Qn guarantees that the sequence (δnkn) ⊂ RN−1 belongs to a compact set (of diameter O(ε)) and that the sequence (δn) ⊂ (0, ∞) is bounded (by O(ε)). Thus, after passing to a subsequence if necessary, we may assume that (δnkn) and (δn) converge.

For any θ ∈ C(0, . . ., 0, 1), we deﬁne a rotation Oθ ∈ O(N) that sends (0, . . ., 0, 1) to θ in the following fashion: if θ = (0, . . ., 0, 1), we take Oθ = Id, and if θ = (0, . . ., 0, 1), we take Oθ = Id on the orthogonal complement of H = span((0, . . ., 0, 1), θ) and on H we take

ωN −|ω′| |ω′| ωN

Oθ =

in the orthonormal basis ((0, . . ., 0, 1), ω′/|ω′|) of H (with the notation ω = ω′ + ωN(0, . . ., 0, 1), ω′ ∈ RN−1 × {0}). This deﬁnition ensures that θ  → Oθ is continuous on C(0, . . ., 0, 1). Next, we deﬁne

![image 97](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile97.png>)

θn := (δnkn, 1 − δn2|kn|2) ∈ SN−1 and

(ϕ+n, ϕ−n) := BO−θ1n,δn(eix

n·ωfn) .

By choosing ε > 0 small enough (depending only on N) we can guarantee that θn·ω > 0 for all n and all ω ∈ SN−1 with ωN > √1 − ε2. We conclude that

![image 98](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile98.png>)

n)χfn ∨ (xn) = (2π)−N/2

(ω′) dω

eix

n·ωfn(ω)χ(ω)1Q

1L(Q

n

SN−1

ϕ+n(ξ)hn(ξ) dξ with

= (2π)−N/2

RN−1

(δnξ, 0) 1 + δn2|ξ|2

θn + Oθ

(δnξ, 0) 1 + δn2|ξ|2

θn + Oθ

hn(ξ) := (1 + δn2|ξ|2)−N/4 χ

n

n

P

.

1Q

![image 99](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile99.png>)

![image 100](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile100.png>)

n

![image 101](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile101.png>)

![image 102](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile102.png>)

and with the projection P : RN → RN−1 deﬁned by P(η′, ηN) := η′.

Since ϕ+n ⇀ 0 in L2(RN−1) by assumption, our claim (5.3) will follow if we can prove that (hn) converges strongly in L2(RN−1). To do so, we prove that (hn) converges

almost everywhere and that 0 ≤ hn ≤ 1B for a centered ball B with (ﬁnite) radius independent of n.

We begin with the almost everywhere convergence. Since (θn) and (δn) converge and χ and θ  → Oθ are continuous, the sequence

(δnξ, 0) 1 + δn2|ξ|2

θn + Oθ

(1 + δn2|ξ|2)−N/4 χ

n

![image 103](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile103.png>)

![image 104](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile104.png>)

converges for all ξ. If the limit of (δn) is positive, then the cube Qn converges towards a ﬁxed cube, and thus the sequence

(δnξ, 0) 1 + δn2|ξ|2

θn + Oθ

n

P

1Q

![image 105](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile105.png>)

n

![image 106](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile106.png>)

converges almost everywhere in ξ. If limn δn = 0, then we use the fact that

if and only if

P

(δnξ, 0) 1 + δn2|ξ|2

θn + Oθ

n

![image 107](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile107.png>)

![image 108](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile108.png>)

∈ Qn

1 1 + δn2|ξ|2

kn + [0, 1)N−1 . (5.4) Since

(ξ, 0)) ∈ 1 −

P(Oθ

![image 109](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile109.png>)

n

![image 110](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile110.png>)

1 1 + δn2|ξ|2

1 −

kn = 0 , we also have almost everywhere convergence in the case limn δn = 0.

lim

![image 111](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile111.png>)

![image 112](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile112.png>)

n→∞

Let us now show that 0 ≤ hn ≤ 1B for a centered ball B with (ﬁnite) radius independent of n. Since Oθ → Id as θ → (0, . . ., 0, 1) and |θn − (0, . . ., 0, 1)| = O(ε) uniformly in n, we choose ε > 0 small enough such that for all ξ ∈ RN−1 and all n,

- 1

![image 113](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile113.png>)

- 2|ξ| .


(ξ, 0)| ≥

|POθ

n

Now assume that ξ ∈ supp hn. Then (5.4) and the fact that 1−(1+x)−1/2 ≤ min{1, x} for all x ≥ 0 implies that

- 1

![image 114](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile114.png>)

- 2|ξ| ≤ |POθ


1 1 + δn2|ξ|2

|kn| + O(1) ≤ min{1, δn2|ξ|2} |kn| + O(1)

(ξ, 0)| ≤ 1 −

![image 115](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile115.png>)

n

![image 116](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile116.png>)

= min{δn−1|ξ|−1, δn|ξ|} δn|kn||ξ| + O(1) ≤ δn|kn||ξ| + O(1) ,

Recalling that δn|kn| ≤ Cε and choosing ε < 1/(2C), we conclude that |ξ| = O(1) uniformly in n, which is what we want to prove. This concludes the proof of Lemma 5.2.

Combining Proposition 5.1 with Lemma 5.2 we obtain immediately the following compactness result.

- Corollary 5.3. Let (fn) ⊂ L2(SN−1) with fn = 1 satisfy fn ⇀conc 0. Then fˇn → 0 in Lq(RN).


5.2. Proof of Proposition 5.1. Our goal in this subsection is to prove the reﬁned Stein–Tomas inequality (5.1). We will deduce this inequality from a reﬁnement of a ‘perturbed Strichartz inequality’, which we state next. We use the notation

√1 − E for 0 ≤ E ≤ 1 .

![image 117](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile117.png>)

T(E) := 1 −

and deﬁne ψQ by ψQ = χQ ψ for Q ∈ D, the collection of all dyadic cubes. Moreover, it is more natural to write d instead of N − 1, so that q = 2 + 4/d.

Proposition 5.4. There are ε ∈ (0, 1), C > 0 and σ ∈ (0, 1) such that for any ψ ∈ L2(Rd) with supp ψ ⊂ {|ξ| ≤ ε},

1−σ

|Q|−1/2 e−itT(−∆)ψQ L∞

e−itT(−∆)ψ Lq

ψ σL2

≤ C sup

. (5.5)

t,x

t,x

x

Q∈D

This should be viewed as a perturbed Strichartz inequality since T(ξ2) ∼ ξ2/2 as ξ → 0. The analogue of Proposition 5.4 with T(−∆) replaced by −∆/2 is essentially due to [34] and appears in a slightly stronger form in [22]. (In this case the restriction on the support of ψ is not necessary.) Proposition 5.4 follows in the same way, but for the sake of completeness we provide the details in the appendix. As in [34, 22] the crucial ingredient is Tao’s bilinear restriction estimate [33].

With the reﬁnement of the perturbed Strichartz inequality, Proposition 5.4, at hand it is easy to give the

- Proof of Proposition 5.1. We ﬁx ε > 0 as given by Proposition 5.4. Let f ∈ L2(SN−1) have support in the cap {ω : ωN > √1 − ε2} and deﬁne a function ψ ∈ L2(RN−1) by


![image 118](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile118.png>)

![image 119](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile119.png>)

f(ξ, 1 − ξ2) 1 − ξ2

ψ(ξ) :=

,

![image 120](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile120.png>)

![image 121](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile121.png>)

so that

fˇ(x) = (2π)−1/2eix

NT(−∆)ψ (x′) Since supp ψ ⊂ {|ξ| > ε} we can apply Proposition 5.4 and obtain

e−ix

N

1−σ

f ˇ Lq(RN) ≤ (2π)−1/2C sup

|Q|−1/2 e−itT(−∆)ψQ L∞

ψ σL2

.

t,x

ξ

Q∈D

We bound

1 √1 − ε2

ψ 2L2

f 2 and note that

≤

![image 122](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile122.png>)

![image 123](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile123.png>)

ξ

(1L(Q)f)∨(x) = (2π)−1/2eix

N

NT(−∆)ψQ (x′) .

e−ix

Thus we conclude that

1−σ

f ˇ Lq(RN) ≤ C′ sup

f σL2(SN−1) .

|Q|−1/2 (1L(Q)f)∨ L∞(RN)

Q∈D

By rotation invariance of the sphere we obtain for f ∈ L2(SN−1) with suppf ⊂ C(θα) the same inequality with L(Q) replaced by Lθ

(Q). Thus, for an arbitrary function f ∈ L2(SN−1) we obtain

α

A

A

f ˇ Lq(RN) =

(χαf)∨ Lq(RN)

(χαf)∨

≤

α=1

α=1

Lq(RN)

A

≤ C′

α=1

sup

Q∈D

≤ C′ sup

α

θα(Q)χαf)∨ L∞(RN)

|Q|−1/2 (1L

θα(Q)χαf)∨ L∞(RN)

|Q|−1/2 (1L

sup

Q∈D

1−σ

χαf σL2(SN−1)

1−σ A

α=1

χαf σL2(SN−1)

A

1−σ

χαf 2L2(SN−1)

θα(Q)χαf)∨ L∞(RN)

|Q|−1/2 (1L

A1−σ/2

≤ C′ sup

sup

α

Q∈D

α=1

1−σ

θα(Q)χαf)∨ L∞(RN)

|Q|−1/2 (1L

≤ C′ sup

A1−σ/2 f σL2(SN−1) . This is the claimed inequality.

sup

α

Q∈D

σ/2

6. Equal profiles

Our goal in this section is to prove (2.2), that is, we want to express the solution of the minimization problem S˜d in terms of the solution of the minimization problem Sd. This will follow from a general inequality that we describe next. For f, g ∈ Lq(RN) (in this section q can be any number ≥ 2) let

g(x) q dx. It is easy to see that this limit exists and is given by

f(x) + eiλx

Φq(f, g) := lim

N

λ→∞ RN

π

- 1

![image 124](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile124.png>)

- 2π RN


f(x) + eiθg(x) q dθ dx.

Φq(f, g) =

−π

A simple proof of this fact can be found, for instance, in [2, Lem. 5.2]. Note that for ﬁxed x ∈ RN, the function

q/2

θ  → f(x) + eiθg(x) q = |f(x)|2 + |g(x)|2 + 2 Reeiθf(x)g(x)

![image 125](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile125.png>)

is continuous and has maximum (|f(x)|+ |g(x)|)q. This maximum belongs to L1(RN) as function of x. Therefore, Allaire’s result applies in the above setting.

- Lemma 6.1. If q ≥ 2, then


Φq(f, g) ≤

Γ(q+12 ) Γ(q+22 )

2q/2 √π

![image 126](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile126.png>)

![image 127](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile127.png>)

![image 128](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile128.png>)

![image 129](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile129.png>)

![image 130](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile130.png>)

f 2q + g 2q q/2 .

The importance of the constant on the right side is that we get equality if |f| = |g|. In fact, the proof below shows that if q > 2, then the inequality is strict unless |f| = |g| almost everywhere.

Proof. Let us write the above formula for Φq(f, g) as Φq(f, g) =

|f(x)|2 + |g(x)|2 q/2 ϕ(|α(x)|) dx with

RN

![image 131](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile131.png>)

2f(x)g(x) |f(x)|2 + |g(x)|2

α(x) :=

. and, for t ∈ [0, 1],

![image 132](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile132.png>)

π

1 π

(1 + tcosθ)q/2 dθ . We claim that ϕ is increasing in [0, 1]. In fact,

ϕ(t) =

![image 133](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile133.png>)

0

q 2

1 π

ϕ′(t) =

![image 134](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile134.png>)

![image 135](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile135.png>)

1 π

q 2

=

![image 136](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile136.png>)

![image 137](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile137.png>)

π

(1 + tcosθ)(q−2)/2 cosθ dθ

0

π/2

(1 + tcosθ)(q−2)/2 − (1 − tcosθ)(q−2)/2 cosθ dθ .

0

For q ≥ 2, the integrand on the right side is pointwise non-negative, which proves the monotonicity.

Since |α(x)| ≤ 1, we deduce that Φq(f, g) ≤ ϕ(1)

|f(x)|2 + |g(x)|2 q/2 dx and therefore, by the triangle inequality in Lq/2,

RN

Φq(f, g)2/q ≤ ϕ(1)2/q |f|2 + |g|2 q/2 ≤ ϕ(1)2/q |f|2 q/2 + |g|2 q/2

= ϕ(1)2/q f 2q + g 2q .

Thus, to complete the proof of the lemma it remains to compute the value of ϕ(1). Using the integral representation of the beta function, we ﬁnd

π

π

π/2

2q/2 π

2(q+2)/2 π

1 π

(1 + cosθ)q/2 dθ =

cosq(θ/2) dθ =

cosq θ dθ

ϕ(1) =

![image 138](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile138.png>)

![image 139](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile139.png>)

![image 140](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile140.png>)

0

0

0

Γ(q+12 ) Γ(q+22 )

2q/2 π

2q/2 √π

- 1

![image 141](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile141.png>)

- 2


q + 1 2

![image 142](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile142.png>)

. (6.1) This completes the proof.

=

B(

,

) =

![image 143](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile143.png>)

![image 144](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile144.png>)

![image 145](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile145.png>)

![image 146](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile146.png>)

![image 147](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile147.png>)

![image 148](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile148.png>)

q+1

- Corollary 6.2. S˜d = 2√q/π2 Γ(


2 )

![image 149](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile149.png>)

Γ(q+22 ) Sd with q = 2 + 4/d. Proof. Let ψ+, ψ− ∈ L2(Rd). By the lemma (with N = d + 1) and the Strichartz inequality,

![image 150](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile150.png>)

![image 151](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile151.png>)

![image 152](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile152.png>)

![image 153](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile153.png>)

e−it∆/2ψ−(x) q dxdt

eit∆/2ψ+(x) + eiλx

lim

N

λ→∞ R×Rd

Γ(q+12 ) Γ(q+22 )

2q/2 √π

eit∆/2ψ+ 2q + e−it∆/2ψ− 2q q/2

![image 154](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile154.png>)

≤

![image 155](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile155.png>)

![image 156](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile156.png>)

![image 157](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile157.png>)

![image 158](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile158.png>)

Γ(q+12 ) Γ(q+22 )

2q/2 √π

(2π)(d+2)/dSd ψ+ 2 + ψ− 2 q/2 .

![image 159](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile159.png>)

≤

![image 160](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile160.png>)

![image 161](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile161.png>)

![image 162](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile162.png>)

![image 163](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile163.png>)

This proves the inequality ≤ in the corollary. The opposite inequality follows by choosing ψ+ = ψ− to be almost maximizers for Sd and recalling that equality holds in Lemma 6.1 if f = g.

![image 164](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile164.png>)

![image 165](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile165.png>)

7. Perturbative analysis

In this section we prove Proposition 1.3 which veriﬁes the main assumption of Theorem 1.1 provided Conjecture 1.2 holds. Let

2/2

ψG(x) := e−x

and

d |eit∆/2ψG(x)|2+4/d dxdt ψG 2+4/d

SdG := (2π)−(d+2)/d R×R

,

![image 166](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile166.png>)

so that Conjecture 1.2 is equivalent to the identity Sd = SdG. In view of this identity, Proposition 1.3 is an immediate consequence of Proposition 7.1 below.

As explained in Remark 2.5, the non-strict analogue of inequality (1.2) is obtained by glueing two Gaussians on the sphere that concentrate on two antipodal points. We now compute the next order of the ‘energy’ of this trial function. Thus, for any ε > 0, consider the trial function

1+ωN ε2

1−ωN

ε2 + χ(−ωN)e−

fε(ω) := χ(ωN)e−

∀ω ∈ SN−1, where χ ∈ C∞

![image 167](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile167.png>)

![image 168](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile168.png>)

c (R) is such that χ ≡ 1 in a neighborhood of 1 and χ ≡ 0 in a neighborhood of (−∞, 0]. As ε → 0, the functions (fε) concentrate on the north and south pole and the limiting proﬁles are, indeed, Gaussians.

Proposition 7.1. We have

log RN |fˇε|q dx fε q

Γ q+12 Γ q+22 SdG +

2q/2 √π

1 4

![image 169](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile169.png>)

ε2 + oε→0(ε2) . (7.1) In particular, for all suﬃciently small ε > 0,

= log

![image 170](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile170.png>)

![image 171](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile171.png>)

![image 172](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile172.png>)

![image 173](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile173.png>)

![image 174](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile174.png>)

![image 175](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile175.png>)

RN |fˇε|q dx fε q

Γ q+12 Γ q+22 SdG .

2q/2 √π

![image 176](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile176.png>)

>

![image 177](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile177.png>)

![image 178](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile178.png>)

![image 179](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile179.png>)

![image 180](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile180.png>)

![image 181](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile181.png>)

An ingredient in the proof of this proposition is the following result about the simpler trial function

1−ωN ε2

gε(x) := χ(ωN)e−

∀ω ∈ SN−1 , (7.2)

![image 182](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile182.png>)

which concentrates only at the north pole. Similar results appear in [12, 29] for N = 2, 3.

- Lemma 7.2. We have


log RN |gˇε|q dx gε q

1 4

ε2 + oε→0(ε2) . (7.3) Before proving the lemma, let us use it to give the

= log SdG +

![image 183](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile183.png>)

![image 184](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile184.png>)

Proof of Proposition 7.1. With gε from (7.2) we shall show that

RN |fˇε|q dx fε q

Γ q+12 Γ q+22

RN |gˇε|q dx gε q

2q/2 √π

![image 185](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile185.png>)

+ O(ε4) . (7.4) This, together with Lemma 7.2, implies the proposition.

=

![image 186](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile186.png>)

![image 187](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile187.png>)

![image 188](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile188.png>)

![image 189](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile189.png>)

![image 190](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile190.png>)

![image 191](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile191.png>)

Clearly, we have

- fε q = 2q/2 gε q . (7.5)

We also note the rough bound

- gε q ≥ cεd+2 . (7.6)


(We will prove something much more precise in the proof of Lemma 7.2.) Moreover, let

√

![image 192](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile192.png>)

1−ε2|η|2)(1+ixN)χ( 1 − ε2|η|2) 1 − ε2|η|2

1 (2π)N/2 Rd

![image 193](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile193.png>)

′·η−ε−2(1−

eix

dη (7.7) and note that

ϕε(x) :=

![image 194](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile194.png>)

![image 195](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile195.png>)

![image 196](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile196.png>)

N/ε2ϕε(x) . We claim that

N/ε2ϕε(x) and ε−dgˇε(x′/ε, xN/ε2) = eix

ε−dfˇε(x′/ε, xN/ε2) = 2 Re eix

π

- 1

![image 197](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile197.png>)

- 2π Rd


q

Re eiθϕε(x) q dθ dx + O(ε4) . (7.8) Since, as in (6.1), for any a ∈ C, 2π

N/ε2ϕε(x)

Re eix

dx =

RN

−π

Γ(q+12 ) Γ(q+22 ) |a|q ,

π

- 1

![image 198](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile198.png>)

- 2π


1 √π

- 1

![image 199](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile199.png>)

- 2π


Re eiθa q dθ =

![image 200](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile200.png>)

| cosθ|q dθ |a|q =

![image 201](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile201.png>)

![image 202](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile202.png>)

![image 203](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile203.png>)

0

−π

![image 204](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile204.png>)

we infer from (7.8) that after scaling

Γ(q+12 ) Γ(q+22 ) RN

2q √π

|fˇε|q dx =

![image 205](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile205.png>)

|gˇε|q dx + O(ε4+(d+2)) . This, together with (7.5) and (7.6), implies (7.4).

![image 206](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile206.png>)

![image 207](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile207.png>)

![image 208](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile208.png>)

RN

![image 209](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile209.png>)

Let us prove (7.8). We introduce the function a(x, θ) = Re eiθϕε(x) q ∀(x, θ) ∈ RN × [−π, π] .

Diﬀerentiating in θ, we ﬁnd that there is a C > 0 such that for all x ∈ RN and all ε > 0,

≤ C|ϕε(x)|q . (7.9) As a consequence, we may expand a as an absolutely convergent Fourier series

+ ∂θ2a(x, ·) L∞

a(x, ·) L∞

θ

θ

cn(x)einθ, ∀(x, θ) ∈ RN × [−π, π]

a(x, θ) =

n∈Z

with

π

dθ 2π

a(x, θ)e−inθ

cn(x) :=

. By integration by parts and (7.9), we ﬁnd the bound

![image 210](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile210.png>)

−π

C 1 + n2|ϕε(x)|q .

|cn(x)| ≤

![image 211](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile211.png>)

By standard stationary phase arguments one can show that ϕε is bounded in Lq(RN) uniformly for small ε > 0 and we obtain

q

N/ε2ϕε(x)

Re eix

a(x, xN/ε2) dx =

dx =

n∈Z RN

RN

RN

Hence, in order to prove (7.8) we will prove

N/ε2cn(x) dx.

einx

n =0 RN

N/ε2cn(x) dx = O(ε4) . (7.10)

einx

Integrating by parts, we have

ε4 n2 RN

N/ε2cn(x) dx = −

N/ε2∂x2

einx

einx

cn(x) dx, and thus it is suﬃcient to bound ∂x2

![image 212](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile212.png>)

N

RN

uniformly in n and ε. This bound again follows from stationary phase arguments, which imply that ϕε, ∂x

cn L1

x

N

ϕε, and ∂x2

ϕε are bounded in Lq(RN), uniformly for small ε > 0. In this way we obtain (7.10) and therefore (7.8) and (7.4).

N

N

Finally, we prove Lemma 7.2. We will make repeated use of the Gaussian integrals

′·η−2s|η|2 dη =

eix

![image 213](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile213.png>)

Rd

2π s

![image 214](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile214.png>)

d/2

- 1

![image 215](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile215.png>)

- 2s|x′|2 , (7.11)


e−

d/2

|x′|2 s2

d s −

2π s

′·η−2s|η|2|η|2 dη =

- 1

![image 216](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile216.png>)

- 2s|x′|2 , (7.12)


eix

e−

![image 217](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile217.png>)

![image 218](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile218.png>)

![image 219](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile219.png>)

![image 220](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile220.png>)

Rd

d/2

2(d + 2)|x′|2 s3

+ |x′|4 s4

2π s

d(d + 2) s2 −

′·η−2s|η|2|η|4 dη =

- 1

![image 221](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile221.png>)

- 2s|x′|2 , (7.13)


eix

e− as well as the identities

![image 222](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile222.png>)

![image 223](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile223.png>)

![image 224](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile224.png>)

![image 225](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile225.png>)

![image 226](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile226.png>)

Rd

dxN (1 + x2N)2

π 2

dxN 1 + x2N

= π and

=

. (7.14)

![image 227](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile227.png>)

![image 228](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile228.png>)

![image 229](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile229.png>)

R

R

Proof of Lemma 7.2. With ϕε from (7.7) we note that Ψ(ε2) := log RN |gˇε|q dx gε q

= log RN |ϕε|q dx ε−d/2gε q

.

![image 230](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile230.png>)

![image 231](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile231.png>)

We begin by studying ε−d/2gε q. Expanding ε−2(1 − 1 − ε2|η|2) =

- 1

![image 232](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile232.png>)

- 2|η|2 +


1 8

![image 233](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile233.png>)

ε2|η|4 + O(ε4|η|6) (7.15) and

![image 234](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile234.png>)

![image 235](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile235.png>)

χ( 1 − ε2|η|2) 1 − ε2|η|2

- 1

![image 236](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile236.png>)

- 2


ε2|η|2 + O(ε4|η|4) (7.16) (with the same expansion when χ is replaced by χ2), we obtain

= 1 +

![image 237](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile237.png>)

![image 238](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile238.png>)

ε−d

|gε(ω)|2 dω =

Sd

=

√

![image 239](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile239.png>)

1−ε2|η|2)χ( 1 − ε2|η|2)2 1 − ε2|η|2

![image 240](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile240.png>)

−2(1−

e−2ε

dη

![image 241](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile241.png>)

![image 242](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile242.png>)

Rd

2 1 2|η|2 −

1 4|η|4 dη + O(ε4) .

2

e−|η|

e−|η|

dη + ε2

![image 243](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile243.png>)

![image 244](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile244.png>)

Rd

Rd

Using the formulas for Gaussian integrals (7.11), (7.12) and (7.13) we ﬁnd that ε−d

d(2 − d) 16

πd/2ε2 + O(ε4) . (7.17) Note that the leading term coincides with

|gε(ω)|2 dω = πd/2 +

![image 245](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile245.png>)

Sd

|ψG(x)|2 dx =

Rd

2

e−x

dx = πd/2 . (7.18)

Rd

Next, we discuss the asymptotics of ϕε q. Using expansions (7.15) and (7.16) and routine stationary phase arguments we obtain

1 (2π)N/2 Rd

′·η−21|η|2(1+ixN) dη + oLq

eix

x(RN)(1)

ϕε(x) =

![image 246](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile246.png>)

![image 247](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile247.png>)

d/2

|x′|2 2(1+ixN )

1 (2π)1/2

1 1 + ixN

e−

+ oLq

x(RN)(1) . The last identity used again (7.11). Thus,

=

![image 248](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile248.png>)

![image 249](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile249.png>)

![image 250](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile250.png>)

q|x′|2 2(1+x2

1 (2π)q/2 RN

(1 + x2N)−dq/4e−

![image 251](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile251.png>)

|ϕε(x)|q dx =

dx

lim

)

N

![image 252](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile252.png>)

ε2→0 RN

1 (2π)q/2 R×Rd

eit∆/2ψG (y) q dy dt, (7.19)

=

![image 253](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile253.png>)

where the last identity used the Gaussian integral (7.11). Note that (7.17), (7.18) and (7.19) imply that

Ψ(ε2) = log SdG , which gives us the leading term in the lemma.

lim

ε2→0

We claim that ε2  → RN |ϕε(x)|q dx is diﬀerentiable at ε2 = 0 and that

d/2 πqd 2(d + 2)

d2 16

- 1

![image 254](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile254.png>)

- 2 −


2π q

1 (2π)q/2

|ϕε|q dx |ε2=0 =

. (7.20)

∂ε2

![image 255](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile255.png>)

![image 256](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile256.png>)

![image 257](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile257.png>)

![image 258](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile258.png>)

RN

We will discuss this below in some detail. Once this claim is shown, it is easy to complete the proof of the lemma. In fact, we note that

∂ε2 RN |ϕε|q dx |ε2=0 limε2→0 RN |ϕε|q dx −

∂ε2Ψ(ε2)|ε2=0 =

![image 259](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile259.png>)

and we recall from (7.17) that

∂ε2 ε−d/2gε 2 |ε2=0 limε2→0 ε−d/2gε 2

q 2

, (7.21)

![image 260](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile260.png>)

![image 261](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile261.png>)

∂ε2 ε−d/2gε 2 |ε2=0 limε2→0 ε−d/2gε 2

=

![image 262](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile262.png>)

d(2 − d) 16

. (7.22)

![image 263](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile263.png>)

By the ﬁrst identity in (7.14) and the Gaussian integral (7.11), we compute from (7.19)

1 (2π)q/2

|ϕε|q dx =

lim

![image 264](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile264.png>)

ε2→0 RN

which, combined with (7.20), gives

2π q

![image 265](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile265.png>)

d/2

π , (7.23)

∂ε2 RN |ϕε|q dx |ε2=0 limε2→0 RN |ϕε|q dx

q 2

d d + 2

=

![image 266](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile266.png>)

![image 267](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile267.png>)

![image 268](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile268.png>)

Inserting (7.22) and (7.24) into (7.21) leads to

d2 16

- 1

![image 269](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile269.png>)

- 2 −


![image 270](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile270.png>)

- 1

![image 271](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile271.png>)

- 2 −


=

d2 16

. (7.24)

![image 272](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile272.png>)

d2 16 −

d2 16 −

4 − d2 16

q 2

- 1

![image 273](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile273.png>)

- 2 −


1 4

d(2 − d) 16

1 2 −

∂ε2Ψ(ε2)|ε2=0 =

, which is the result stated in the lemma.

=

=

![image 274](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile274.png>)

![image 275](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile275.png>)

![image 276](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile276.png>)

![image 277](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile277.png>)

![image 278](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile278.png>)

![image 279](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile279.png>)

![image 280](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile280.png>)

Thus, it remains to justify the claim (7.20). Using stationary phase arguments one can show that, for any σ > 0,

|ϕε(x)| ≤ Cσ(1 + |x|)−d/2+σ for all x ∈ RN , ε > 0 and

|Re(ϕε∂ε2ϕε(x))| ≤ Cσ(1 + |x|)−d+2σ for all x ∈ RN , ε > 0 . (The crucial point here is the real part which leads to a cancellation. Without the real part one can only obtain a similar bound with an additional factor of |xN|, which is not good enough to prove diﬀerentiability.) These bounds imply by dominated convergence that ε2  → RN |ϕε(x)|q dx is diﬀerentiable at any ε2 ≥ 0 and that

![image 281](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile281.png>)

∂ε2

|ϕε|q dx = q

RN

|ϕε|q−2 Re(ϕε∂ε2ϕε) dx. (7.25)

![image 282](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile282.png>)

RN

Recalling (7.7), (7.15) and (7.16) we expand pointwise ϕε(x) =

1 (2π)N/2 Rd

′·η−12|η|2(1+ixN) dη

eix

![image 283](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile283.png>)

![image 284](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile284.png>)

ε2 (2π)N/2 Rd

1 8|η|4(1 + ixN) dη + o(ε2)

′·η−12|η|2(1+ixN) 1 2|η|2 −

eix

+

![image 285](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile285.png>)

![image 286](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile286.png>)

![image 287](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile287.png>)

![image 288](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile288.png>)

d/2

|x′|2 2(1+ixN )

1 (2π)1/2

1 1 + ixN

e−

=

![image 289](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile289.png>)

![image 290](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile290.png>)

![image 291](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile291.png>)

d/2

d|x′|2 4(1 + ixN)2 −

|x′|4 8(1 + ixN)3

ε2 (2π)1/2

|x′|2 2(1+ixN )

d(2 − d) 8(1 + ixN)

1 1 + ixN

e−

+

+

![image 292](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile292.png>)

![image 293](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile293.png>)

![image 294](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile294.png>)

![image 295](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile295.png>)

![image 296](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile296.png>)

![image 297](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile297.png>)

+ o(ε2) . Here we used the Gaussian integral formulas (7.11), (7.12) and (7.13). We obtain

q

d/2

|x′|2 2(1+ixN )

1 1 + ixN

1 (2π)1/2

e−

|ϕε|q−2 Re(ϕε∂ε2ϕε)|ε2=0 =

![image 298](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile298.png>)

![image 299](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile299.png>)

![image 300](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile300.png>)

![image 301](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile301.png>)

d|x′|2 4(1 + ixN)2 −

|x′|4 8(1 + ixN)3

d(2 − d) 8(1 + ixN)

+

× Re

![image 302](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile302.png>)

![image 303](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile303.png>)

![image 304](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile304.png>)

dq/4

q|x′|2 2(1+x2

1 (2π)q/2

1 1 + x2N

e−

![image 305](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile305.png>)

=

)

N

![image 306](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile306.png>)

![image 307](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile307.png>)

d|x′|2(1 − x2N) 4(1 + x2N)2 −

|x′|4(1 − 3x2N) 8(1 + x2N)3

d(2 − d) 8(1 + x2N)

.

+

×

![image 308](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile308.png>)

![image 309](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile309.png>)

![image 310](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile310.png>)

Finally, we integrate this identity over x ∈ Rd and recall (7.25). We change variables x′ = (1 + x2N)1/2y, compute Gaussian integrals and use (7.14) to obtain

q (2π)q/2 R×RN−1

q

2|y|2×

|ϕε|q dx |ε2=0 =

dxN dy (1 + x2N)−2e−

∂ε2

![image 311](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile311.png>)

![image 312](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile312.png>)

RN

d|y|2(1 − x2N) 4 −

|y|4(1 − 3x2N) 8

d(2 − d) 8

×

+

![image 313](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile313.png>)

![image 314](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile314.png>)

![image 315](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile315.png>)

d/2

2π q

q (2π)q/2

dxN(1 + x2N)−2×

=

![image 316](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile316.png>)

![image 317](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile317.png>)

R

d2(1 − x2N) 4q −

d(d + 2)(1 − 3x2N) 8q2

d(2 − d) 8

×

+

![image 318](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile318.png>)

![image 319](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile319.png>)

![image 320](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile320.png>)

d/2

d2 16

- 1

![image 321](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile321.png>)

- 2 −


πqd 2(d + 2)

2π q

1 (2π)q/2

. This proves (7.20).

×

=

![image 322](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile322.png>)

![image 323](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile323.png>)

![image 324](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile324.png>)

![image 325](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile325.png>)

Appendix A. Refinement of a perturbed Strichartz inequality

In this appendix we show that the method from [34, 22] can be used to prove the reﬁnement of the perturbed Strichartz inequality in Proposition 5.4. We actually

prove it in the setting of elliptic-type phases as deﬁned in [35], thus we do not restrict ourselves to the case of the sphere with the function T. Instead, let Φ a smooth real function deﬁned on a neighborhood of the origin in Rd, satisfying Hess Φ(0) = Id. We consider the general phase ξ  → Φ(ξ) instead of ξ  → T(|ξ|2) = 1 − 1 − |ξ|2. We also recall that we denote the dimension by d ≥ 1 and that

![image 326](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile326.png>)

q = 2 + 4/d .

As we mentioned before, the main ingredient is a deep bilinear restriction estimate due to Tao. To state this result we introduce the notation

Q ∼ Q′ for two dyadic cubes Q, Q′ ∈ D to mean that they have the same side length and are not adjacent (i.e., their closures do not intersect), but their parents are adjacent. In the sequel, we use the shortcut notation for any ψ ∈ L2x(Rd) and any (t, x) ∈ R × Rd, ΨQ(t, x) := e−itΦ(−i∇)ψQ (x), where we recall that ψQ := 1Q ψ. Theorem A.1. Let dd+1+3 < p < d+2d . There are ε > 0 and C > 0 such that for all ψ ∈ L2(Rd) with supp ψ ⊂ {|ξ| ≤ ε} and for all Q ∼ Q′ we have

![image 327](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile327.png>)

![image 328](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile328.png>)

d+2

ΨQΨQ′ Lpt,x ≤ C|Q|1−

ψQ′ L2x . (A.1)

pd ψQ L2

![image 329](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile329.png>)

x

This theorem follows by a rather standard parabolic rescaling argument from Tao’s sharp bilinear estimates on the paraboloid [33] and from earlier bilinear estimates due to Tao–Vargas–Vega [35]. We present this derivation for the sake of completeness. We also remark that the assumption p > dd+3+1 is sharp, but that for our purpose the inequality with any p satisfying p < d+2d would be suﬃcient.

![image 330](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile330.png>)

![image 331](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile331.png>)

Proof. Let Q = δk+[0, δ)d and Q′ = δk′+[0, δ)d with δ ∈ 2Z, k, k′ ∈ Zd, 0 < |k−k′| = O(1) and δk = O(ε), δk′ = O(ε), δ = O(ε). The parabolic rescaling leads to

−2Φ(δ(k+ξ))uQ(ξ) dξ,

eix·ξ−itδ

δ−d/2ΨQ(t/δ2, x/δ) = (2π)−d/2

Rd

−2Φ(δ(k+ξ))uQ′(ξ) dξ, where

eix·ξ−itδ

δ−d/2ΨQ′(t/δ2, x/δ) = (2π)−d/2

Rd

uQ(ξ) := δd/2 ψ(δ(k + ξ))1[0,1)d(ξ), uQ′(ξ) := δd/2 ψ(δ(k + ξ))1k′−k+[0,1)d(ξ). As a consequence, we may write

d+2

ΨQΨQ′ Lpt,x = δd−

p TuQTuQ′ Lpt,x, where

![image 332](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile332.png>)

eix·ξ−itΦ

δ,k(ξ)g(ξ) dξ,

Tg(t, x) =

Q0

Q0 is some big cube independent of Q and Q′ containing both [0, 1)d and k′−k+[0, 1)d, and

Φδ,k(ξ) = δ−2 [Φ(δ(k + ξ)) − Φ(δk) − δ∇Φ(δk) · ξ]. By a Taylor formula and the fact that δk = O(ε), δ = O(ε), all the smooth norms of Φδ,k are bounded uniformly in (δ, k) on Q0. Furthermore,

Hess Φδ,k − Id = O(ε),

also uniformly in (δ, k) on Q0. We are thus in the setting the bilinear estimates of Tao [33] (see the third remark at the end of the article), for elliptic-type compact surfaces as deﬁned in [35, Sec. 2]. We deduce that if ε > 0 is small enough, there exists C > 0 independent of Q, Q′ and g such that

d+2

ΨQΨQ′ Lpt,x ≤ Cδd−

p uQ L2(Rd) uQ′ L2(Rd). Undoing all the change of variables that we performed, we ﬁnd that uQ L2(Rd) uQ′ L2(Rd) = ψQ L2

![image 333](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile333.png>)

ψQ′ L2x, which implies the desired estimate.

x

The next ingredient in the proof of Proposition 5.1 is the following improvement over the triangle inequality.

- Lemma A.2. For ε > 0 small enough, there is a C > 0 such that for all ψ ∈ L2(Rd) with supp ψ ⊂ {|ξ| ≤ ε},


q∗

q∗ Lq/t,x2

(A.2)

ΨQΨQ′

≤ C

ΨQΨQ′

Q∼Q′

Q∼Q′

Lq/t,x2

with q∗ := min{q/2, (q/2)′}.

Proof of Lemma A.2. We apply the result of Tao–Vargas–Vega [35], or more precisely the version of [22, Lem. A.9 & Proof of Prop. 4.24]. The space-time Fourier transform Ft,x of ΨQΨQ′ satisﬁes

supp Ft,x[ΨQΨQ′] ⊂ {(η + η′, Φ(η) + Φ(η′)), η ∈ Q, η′ ∈ Q′}.

We include this last set into a similar parallelepided as in Killip-Visan [Proof of Prop. 4.24], which is then enough to obtain orthogonality. Taylor expansions leads to the formula

η + η′ 2

Φ(η) + Φ(η′) = 2Φ

+ a(η, η′)|η − η′|2,

![image 334](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile334.png>)

Φ

η + η′ 2

![image 335](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile335.png>)

= Φ

c(Q + Q′) 2

![image 336](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile336.png>)

c(Q + Q′)

- 1

![image 337](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile337.png>)

- 2∇Φ


2 · (η + η′ − c(Q + Q′)) + b(η + η′, c(Q + Q′))|η + η′ − c(Q + Q′)|2,

+

![image 338](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile338.png>)

where c(Q + Q′) denotes the center of the cube Q + Q′, for two functions a and b satisfying

3/8 ≤ a(η, η′) ≤ 1/8, 3/16 ≤ b(η + η′, c(Q + Q′)) ≤ 1/16, assuming that ε > 0 is small enough. We deduce that

supp Ft,x[ΨQΨQ′] ⊂ R(Q + Q′),

where R(Q′′) = (η, ω), η ∈ Q′′,

ω − 2Φ 12c(Q′′) − ∇Φ 12c(Q′′) · (η − c(Q′′)) (diamQ′′)2 ≤

869 64 ≤

- 1

![image 339](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile339.png>)

- 2


![image 340](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile340.png>)

![image 341](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile341.png>)

![image 342](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile342.png>)

![image 343](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile343.png>)

Again by a Taylor formula, we have c(Q′′) −Φ

- 3

![image 344](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile344.png>)

- 4|c(Q′′)−η|2 ≤ Φ


- 1

![image 345](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile345.png>)

- 2


- 1

![image 346](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile346.png>)

- 2


η −∇Φ

- 1

![image 347](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile347.png>)

- 2


We deduce that for any (η, ω) ∈ R(Q′′), we have

- 1

![image 348](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile348.png>)

- 2


3 2

869 64

(diamQ′′)2 ≤ ω −

+

Φ

![image 349](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile349.png>)

![image 350](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile350.png>)

c(Q′′) ·

- 1

![image 351](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile351.png>)

- 2


1 4|c(Q′′)−η|2.

(c(Q′′)−η) ≤

![image 352](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile352.png>)

1 2

η ≤ (diamQ′′)2.

![image 353](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile353.png>)

This means that if two pairs of close cubes Q ∼ Q′, Q˜ ∼ Q˜′ are such that R(Q + Q′) and R(Q˜ + Q˜′) intersect, they must have a similar diameter. The same holds for the dilates (1 + α)R(Q + Q′) for some small α, by the same argument. If the diameters are in a ﬁnite number, the cubes are also in a ﬁnite number since their centers verify

|c(Q′′) − c(Q˜′′)| ≤ |c(Q′′) − η| + |c(Q˜′′) − η| ≤ diamQ′′.

We are thus in the same situation as in Killip-Visan [Proof of Prop. 4.24], and Lemma A.2 follows.

As a ﬁnal ingredient in the proof of Proposition 5.1 we cite a bound of sums of local norms over dyadic cubes in terms a global norm. For a simple proof we refer to [34, Proof of Thm. A.1]; see also [4, Thm. 1.3] and [22, Proof of Prop. 4.24].

.

- Lemma A.3. Let d ≥ 1 and 1 < µ < ν. Then there is a constant Cd,µ,ν such that for all f ∈ Lµ(Rd),


1/ν

′

|Q|−ν/µ

f νL1(Q)

≤ Cd,µ,ν f Lµ(Rd) .

Q∈D

After these preliminaries we are in position to give the

Proof of Proposition 5.4. We follow rather closely Tao’s arguments [34, Proof of Thm. A.1]; see also Killip-Visan [22, proof of Prop. 4.24]. We observe that for any ξ, ξ′ ∈ Rd there is a pair of cubes Q, Q′ ∈ D with Q ∼ Q′ such that ξ ∈ Q and ξ′ ∈ Q′. Consequently, if we let

Ψ(t, x) := e−itΦ(−i∇)ψ (x),

we ﬁnd

Ψ2 =

ΨQΨQ′ . Therefore Lemma A.2 yields

Q∼Q′

1/q∗

q∗ Lq/t,x2

∗

Ψ 2Lq

≤ C1/q

= Ψ2 Lq/2

ΨQΨQ′

=

ΨQΨQ′

t,x

t,x

Q∼Q′

Q∼Q′

Lq/t,x2

1/q∗

q∗−r Lq/t,x2

∗

r Lq/t,x2

≤ C1/q

(A.3)

ΨQΨQ′

ΨQΨQ′

sup

Q∼Q′

Q∼Q′

for every r ≤ q∗. We will later choose r > 1. We now estimate ΨQΨQ′ Lq/t,x2 in two diﬀerent ways. They both rely on the bilinear estimate from Theorem A.1. Since

, the bilinear estimate (A.1) implies that for all NN+2 < p < NN+1−1 and all Q ∼ Q′, ΨQΨQ′ Lq/t,x2 ≤ |Q|−1 ΨQΨQ′ L∞t,x

x ≤ ψ L2

ψQ L2

x

![image 354](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile354.png>)

![image 355](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile355.png>)

1−2qp

2p q

![image 356](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile356.png>)

![image 357](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile357.png>)

|Q|q/(2p)−1 ΨQΨQ′ Lpt,x

1−2qp

1−2qp

4p q

2p q

![image 358](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile358.png>)

![image 359](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile359.png>)

|Q′|−1/2 ΨQ′ L∞t,x

N,p,ε |Q|−1/2 ΨQ L∞

![image 360](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile360.png>)

![image 361](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile361.png>)

ψ

≤ C

L2x . This bound implies

t,x

2(1−2qp)

4p q

2p q

![image 362](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile362.png>)

|Q′′|−1/2 ΨQ′′ L∞t,x

![image 363](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile363.png>)

![image 364](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile364.png>)

ψ

N,p,ε sup

L2x . (A.4) On the other hand, one can also interpolate the bilinear estimate (A.1) with the

ΨQΨQ′ Lq/t,x2 ≤ C

sup

Q′′∈D

Q∼Q′

trivial estimate

ΨQΨQ′ L∞t,x ≤ (2π)−d ψQ L1

ψQ′ L1ξ to obtain

ξ

2

ΨQΨQ′ Lq/t,x2 ≤ CN,ε′ |Q|1−

ψQ′ Lsξ for some 1 < s < 2 (whose value is not important here). This implies that

s ψQ Ls

![image 365](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile365.png>)

ξ

Q∼Q′

ΨQΨQ′

r

Lq/t,x2 ≤ C

Q∼Q′

= C′

Q

2

|Q|1−

s ψQ Ls

![image 366](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile366.png>)

ξ

2

|Q|1−

s ψQ 2Ls

![image 367](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile367.png>)

ξ

r

r

2

|Q|1−

s ψQ 2Ls

≤ C

ψQ′ Lsξ

![image 368](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile368.png>)

ξ

Q∼Q′

r

. (A.5)

In the last equality we used the fact that the number of Q′ ∈ D satisfying Q′ ∼ Q is ﬁnite and independent of Q. Finally, according to Lemma A.3 (with f = | ψ|s, µ = 2/s and ν = 2r/s; note 1 < µ < ν since s < 2 and r > 1), the right side of (A.5) is bounded by a constant times ψ 2Lr2

= ψ 2Lr2

. Combining this with (A.3) and (A.4) completes the proof of Proposition 5.4.

x

ξ

References

- [1] T. Alazard, N. Burq, and C. Zuily, A stationary phase type estimate, arXiv preprint arXiv:1511.01439, (2015).
- [2] G. Allaire, Homogenization and two-scale convergence, SIAM J. Math. Anal., 23 (1992), pp. 1482–1518.
- [3] T. Aubin, Equations´ diﬀe´rentielles non line´aires et proble`me de Yamabe concernant la courbure scalaire, J. Math. Pures Appl., 55 (1976), pp. 269–296.
- [4] P. B´egout and A. Vargas, Mass concentration phenomena for the L2-critical nonlinear Schro¨dinger equation, Trans. Amer. Math. Soc., 359 (2007), pp. 5257–5282.
- [5] J. Bennett, N. Bez, A. Carbery, and D. Hundertmark, Heat-ﬂow monotonicity of Strichartz norms, Anal. PDE, 2 (2009), pp. 147–158.
- [6] J. Bourgain, Reﬁnements of Strichartz’ inequality and applications to 2D-NLS with critical nonlinearity, Internat. Math. Res. Notices, (1998), pp. 253–283.
- [7] H. Br´ezis and E. H. Lieb, A relation between pointwise convergence of functions and convergence of functionals, Proceedings of the American Mathematical Society, 88 (1983), pp. 486–490.
- [8] H. Br´ezis and E. H. Lieb, Minimum action solutions of some vector ﬁeld equations, Comm. Math. Phys., 96 (1984), pp. 97–113.
- [9] H. Br´ezis and L. Nirenberg, Positive solutions of nonlinear elliptic equations involving critical Sobolev exponents, Comm. Pure Appl. Math., 36 (1983), pp. 437–477.
- [10] R. Carles and S. Keraani, On the role of quadratic oscillations in nonlinear Schro¨dinger equations. II. The L2-critical case, Trans. Amer. Math. Soc., 359 (2007), pp. 33–62 (electronic).
- [11] E. Carneiro, D. Foschi, D. Oliveira e Silva, and C. Thiele, A sharp trilinear inequality related to Fourier restriction on the circle, arXiv preprint arXiv:1509.06674, (2015).
- [12] M. Christ and S. Shao, Existence of extremals for a Fourier restriction inequality, Anal. PDE, 5 (2012), pp. 261–312.
- [13] , On the extremizers of an adjoint Fourier restriction inequality, Adv. Math., 230 (2012), pp. 957–977.

![image 369](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile369.png>)

- [14] D. Foschi, Maximizers for the Strichartz inequality, J. Eur. Math. Soc. (JEMS), 9 (2007), pp. 739–774.
- [15] , Global maximizers for the sphere adjoint Fourier restriction inequality, J. Funct. Anal., 268 (2015), pp. 690–702.

![image 370](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile370.png>)

- [16] R. L. Frank and E. H. Lieb, Sharp constants in several inequalities on the Heisenberg group, Ann. of Math. (2), 176 (2012), pp. 349–381.
- [17] , A compactness lemma and its application to the existence of minimizers for the liquid drop model, SIAM J. Math. Anal., 47 (2015), pp. 4436–4450.

![image 371](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile371.png>)

- [18] J. Frohlich,¨ E. H. Lieb, and M. Loss, Stability of Coulomb systems with magnetic ﬁelds. I. The one-electron atom, Comm. Math. Phys., 104 (1986), pp. 251–270.
- [19] P. G´erard, Description du de´faut de compacite´ de linjection de Sobolev, ESAIM Control Optim. Calc. Var., 3 (1998), pp. 213–233.
- [20] P. G´erard, Y. Meyer, and F. Oru, Ine´galite´s de Sobolev pre´cise´es, S´eminaire E.D.P.,´ (1996 1997), Exp. No. IV, 11 pp.
- [21] D. Hundertmark and V. Zharnitsky, On sharp Strichartz inequalities in low dimensions, Int. Math. Res. Not., (2006), pp. Art. ID 34080, 18.
- [22] R. Killip and M. Visan, Nonlinear Schro¨dinger equations at critical regularity, Evolution equations, 17 (2013), pp. 325–437.
- [23] M. Kunze, On the existence of a maximizer for the Strichartz inequality, Commun. Math. Phys., 243 (2003), pp. 137–162.


- [24] E. H. Lieb, Sharp constants in the Hardy–Littlewood–Sobolev and related inequalities, Ann. Math., 118 (1983), pp. 349–374.
- [25] F. Merle and L. Vega, Compactness at blow-up time for L2 solutions of the critical nonlinear Schro¨dinger equation in 2D, Internat. Math. Res. Notices, (1998), pp. 399–425.
- [26] A. Moyua, A. Vargas, and L. Vega, Restriction theorems and maximal operators related to oscillatory integrals in R3, Duke Math. J., 96 (1999), pp. 547–574.
- [27] D. Oliveira e Silva, Extremizers for Fourier restriction inequalities: convex arcs, J. Anal. Math., 124 (2014), pp. 337–385.
- [28] S. Shao, Maximizers for the Strichartz inequalities and the Sobolev-Strichartz inequalities for the Schro¨dinger equation, Electronic J. of Diﬀerential Equations, (2009), pp. 1–13.
- [29] S. Shao, On existence of extremizers for the Tomas–Stein inequality for S1, J. Func. Anal.,

(2015). To appear.

- [30] E. M. Stein, Oscillatory integrals in Fourier analysis, in Beijing lectures in harmonic analysis (Beijing, 1984), vol. 112 of Ann. of Math. Stud., Princeton Univ. Press, Princeton, NJ, 1986, pp. 307–355.
- [31] E. M. Stein, Harmonic analysis: real-variable methods, orthogonality, and oscillatory integrals, vol. 43 of Princeton Mathematical Series, Princeton University Press, Princeton, NJ, 1993. With the assistance of Timothy S. Murphy, Monographs in Harmonic Analysis, III.
- [32] R. Strichartz, Restrictions of Fourier transforms to quadratic surfaces and decay of solutions of wave equations, Duke Math. J., 44 (1977), pp. 705–714.
- [33] T. Tao, A sharp bilinear restriction estimate for paraboloids, Geom. Funct. Anal., 13 (2003), pp. 1359–1384.
- [34] , A pseudoconformal compactiﬁcation of the nonlinear Schro¨dinger equation and applications, New York J. Math., 15 (2009), pp. 265–282.

![image 372](<2016-frank-maximizers-stein-tomas-inequality_images/imageFile372.png>)

- [35] T. Tao, A. Vargas, and L. Vega, A bilinear approach to the restriction and Kakeya conjectures, J. Amer. Math. Soc., 11 (1998), pp. 967–1000.
- [36] P. A. Tomas, A restriction theorem for the Fourier transform, Bull. Amer. Math. Soc., 81


(1975), pp. 477–478.

Rupert L. Frank, Mathematics 253-37, Caltech, Pasadena, CA 91125, USA E-mail address: rlfrank@caltech.edu

Elliott H. Lieb, Departments of Mathematics and Physics, Princeton University,

Princeton, NJ 08544, USA E-mail address: lieb@princeton.edu Julien Sabin, Laboratoire de Math´ematiques d’Orsay, Univ. Paris-Sud, CNRS, Uni-

versit´e Paris-Saclay, 91405 Orsay, France. E-mail address: Julien.Sabin@math.u-psud.fr

