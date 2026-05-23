arXiv:1707.08944v2[math.CA]9Apr2018

MULTI-SCALE BILINEAR RESTRICTION ESTIMATES FOR GENERAL PHASES

TIMOTHY CANDY

Abstract. We prove (adjoint) bilinear restriction estimates for general phases at diﬀerent scales in the full non-endpoint mixed norm range, and give bounds with a sharp and explicit dependence on the phases. These estimates have applications to high-low frequency interactions for solutions to partial diﬀerential equations, as well as to the linear restriction problem for surfaces with degenerate curvature. As a consequence, we obtain new bilinear restriction estimates for elliptic phases and wave/Klein-Gordon interactions in the full bilinear range, and give a reﬁned Strichartz inequality for the Klein-Gordon equation. In addition, we extend these bilinear estimates to hold in adapted function spaces by using a transference type principle which holds for vector valued waves.

1. Introduction

Let n 2 and for j = 1,2 take phases Φj : Λj → R with Λj ⊂ Rn. We consider the problem of obtaining (adjoint) bilinear restriction estimates of the form

eitΦ

1(−i∇)feitΦ

2(−i∇)g Lq

tLrx(R1+n) C f L2

x(Rn) (1.1) with an explicit dependence of the constant C on the phases Φj and sets Λj. Here 1 q,r 2, supp f ⊂ Λ1, supp g ⊂ Λ2, and f(ξ) =

x(Rn) g L2

Rn f(x)e−ix·ξdx is the spatial Fourier transform of f. This problem is interesting for two key reasons. Firstly, in applications to PDE, the dependence on Φj and Λj reﬂects the derivative cost required to place the product into LqtLrx. Controlling the number of derivatives required in (1.1) leads to, for instance, sharp null form estimates in the case of the wave equation Φ = |ξ| [21, 13, 12], reﬁned Strichartz estimates for the wave and Klein-Gordon equations [2, 8, 17], as well as scattering for the Wave Maps equation [19], and Dirac-Klein-Gordon equation [5, 6]. Secondly, bilinear restriction estimates of the form (1.1) have played an important role in the classical linear restriction problem in harmonic analysis, see for instance [15, 20]. In particular, understanding the dependence of the constant C on the phases Φj, has led to improved linear restriction estimates for surfaces with curvature that may degenerate in certain directions [3, 20].

´

We now consider some concrete examples. In the case of the wave equation Φ1 = Φ2 = |ξ|, the estimate (1.1) has a long history and is now essentially well understood. More precisely, if Λ1 ⊂ {|ξ| ≈ 1} is at scale 1, Λ2 ⊂ {|ξ| ≈ λ} is at scale λ 1, and Λ1 and Λ2 have angular separation of size 1, then it is known

1

q−12+ǫ for every ǫ > 0. This is sharp up to the ǫ frequency loss, and in the unit scale (λ = 1), non-endpoint case q = r > nn+3+1, is due to the breakthrough work of Wolﬀ [27]. The endpoint case q = r = nn+3+1 for general scales λ 1 was obtained by

that (1.1) holds in the range 1q + n2+1r n+12 and we have C ≈ λ

![image 1](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile1.png>)

![image 2](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile2.png>)

![image 3](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile3.png>)

![image 4](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile4.png>)

![image 5](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile5.png>)

![image 6](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile6.png>)

![image 7](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile7.png>)

- Tao [21]. In the mixed exponents case, q = r, the bilinear estimate for general scales is due to Tataru [24] for the non-constant coeﬃcient wave equation, and Lee-Vargas [13], Lee-Rogers-Vargas [12] in the constant coeﬃcient case. The endpoint estimate for q = r is also known, and was proven by Temur [25].

On the other hand, in the case of the Schr¨odinger equation, Φ1 = Φ2 = |ξ|2, if Λ1 is a ball of radius 1, and Λ2 is a ball of radius λ 1 such that the sets Λ1 and Λ2 are separated by a distance λ, then work of

- Tao [22] shows that for q = r > nn+3+1 the bilinear estimate (1.1) holds with C ≈ λr1−1+ǫ for every ǫ > 0. In the case of general phases which are both at unit scale, under suitable transversality and curvature


![image 8](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile8.png>)

![image 9](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile9.png>)

assumptions, Lee-Vargas [14] and Bejenaru [1] have shown that (1.1) again holds in the non-endpoint range q = r > nn+3+1. For general phases which are not at unit scale, only in certain special cases is the dependence of C in (1.1) on the phases Φj and sets Λj known. In particular, if Φ1 and Φ2 are elliptic phases with curvature

![image 10](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile10.png>)

![image 11](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile11.png>)

Financial support by the DFG through the CRC “Taming uncertainty and proﬁting from randomness and low regularity in analysis, stochastics and their applications” is acknowledged.

at diﬀerent scales, then (1.1) was obtained by Stovall [20] with an almost sharp dependence on the scale. If n = 2, and Φ1 = Φ2 = ξm

1 + ξm

2 are surfaces of ﬁnite type with rectangular sets Λj ⊂ {0 < ξ1,ξ2 < 1}, then the essentially optimal dependence of the constant C on the rectangles Λj and parameters mj 2 has been obtained in recent work of Buschenhenke-M¨uller-Vargas [3].

1

2

In the current article we unify and improve the above examples, and show that in fact for general phases Φj, under certain transversality and curvature assumptions on the surfaces Sj = {(Φj(ξ),ξ)|ξ ∈ Λj} ⊂ R1+n, if (for instance) Λ1 is contained in a ball of radius 1, then the bilinear restriction estimate (1.1) holds in the full, non-endpoint, bilinear range 1q + n2+1r < n+12 with constant

![image 12](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile12.png>)

![image 13](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile13.png>)

![image 14](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile14.png>)

1 r −1 max min{H1,H2}

![image 15](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile15.png>)

C ≈ V

where we introduce the notation

- 1

![image 16](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile16.png>)

- 2−1q max{H1,H2}


![image 17](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile17.png>)

- 1

![image 18](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile18.png>)

- 2−1r (1.2)


![image 19](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile19.png>)

|∇Φ1(ξ) − ∇Φ2(η)|, Hj =  ∇2Φj L∞(Λj),

Vmax = sup ξ∈Λ1 η∈Λ2

see Theorem 1.2 below for a more precise statement. Moreover, we show that this dependence on the phases Φj is sharp. The estimate (1.2) recovers all examples mentioned above without an epsilon loss. For instance, in the case of the wave equation, a computation shows that provided the sets Λ1 and Λ2 are at scales 1 and λ 1 respectively, and are angularly separated by a distance 1, then we have Vmax ≈ 1 and

- H1 = 1, H2 ≈ λ−1. In particular, for the bilinear restriction estimate for the cone, (1.2) recovers the optimal dependence on the frequency λ without an ǫ loss. Similarly (1.2) also recovers the correct dependence on the frequency parameter λ in the Schr¨odinger case, after observing that if Λ1 and Λ2 are separated by a distance λ, then Vmax ≈ λ and H1 = H2 = 1.


As a concrete application of the general formula (1.2), we obtain new bilinear restriction estimates for elliptic phases, and Klein-Gordon interactions with diﬀering masses, see Theorem 1.8 and Theorem 1.10 respectively. In particular, we obtain sharp (non-endpoint) estimates for wave Klein-Gordon interactions. Further, we give two additional consequences of the general bilinear restriction estimate. The ﬁrst, stated in Theorem 1.12 below, is a reﬁned Strichartz estimate for the Klein-Gordon equation which shows that, for n 2 there exists θ > 0 such that

eit ∇ f

2 n+1 n−1

![image 20](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile20.png>)

t,x (R1+n)

L

f θX f 1−θ

, (1.3)

H 12

![image 21](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile21.png>)

where · X is a norm which detects concentration of the Fourier support of f to certain rectangular sets, and satisﬁes f X f H1

. The classical Strichartz estimate for the Klein-Gordon equation corresponds to θ = 0. The estimate (1.3) gives the Klein-Gordon version of a reﬁned Strichartz estimate for the wave equation due to Ramos [17] and extends a similar estimate of Killip-Stovall-Visan [8]. Bounds of the form (1.3) are a closely related to proﬁle decompositions, see for instance [8, 17] for further details.

![image 22](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile22.png>)

2

The second consequence is an extension of (1.1) from free waves eitΦ(−i∇)f, to more general functions belonging to certain adapted function spaces UΦ2, see Corollary 1.6 below. This corresponds to a multi-scale version of recent work of the author and Herr [4]. The new bilinear bounds we obtain here, are applied in [5, 6] to obtain conditional scattering results for the Dirac-Klein-Gordon system. The application to the Dirac-Klein-Gordon equation, which includes Klein-Gordon interactions with diﬀerent masses, formed a key motivation to study general bilinear restriction estimates of the form (1.1).

- 1.1. Main Theorem. Let ℓ2c(Z) denote the collection of all compactly supported sequences in ℓ2(Z), thus every sequence in ℓ2c(Z) has only ﬁnitely non-zero components. By a slight abuse of notation, the standard norm on ℓ2 is denoted by | · |. We deﬁne the product of two ℓ2c(Z)-valued functions u and v as simply the tensor product uv = u ⊗ v. Thus |uv| = |u||v|. We say that u(t,x) : R1+n → ℓ2c(Z) is a Φj-wave if


j(−i∇)f(x) with f : Rn → ℓ2c(Z) and supp f ⊂ Λj. Note that, if u is a Φj-wave, then supp u is independent of time, u L∞ t L2x = u(0) L2

u(t,x) = eitΦ

, and u is a solution to the equation i∂tu + Φj(−i∇)u = 0.

x

Alternatively, up to a Jacobian factor, u can be viewed as the extension operator associated to the surface Sj = {(Φj(ξ),ξ) | ξ ∈ Λj} ⊂ R1+n.

It is well-known that to obtain bilinear restriction estimates in the full bilinear range q1 + n2+1r n+12 requires ﬁrstly that the surfaces Sj are transverse, in the sense that |∇Φ1(ξ) − ∇Φ2(η)| > 0, and secondly that there is some curvature along the n − 1 dimensional surfaces of intersection S1 ∩ (h − S2) for h ∈ R1+n. These conditions are suﬃcient in the case of the wave or Schr¨odinger equation, but in the general case, a stronger condition is required that ensures that the normals to the surface Sk intersect transversally with the conic surface formed by taking the normal directions to the surface Sj at points in Sj ∩ (h − Sk), see for instance [14, 1, 4] for assumptions of this type. In the current article, we use a normalised version of the conditions appearing in [4]. To describe the precise conditions we impose on the phases Φj, we require some additional notation. Given h = (a,h) ∈ R1+n and {j,k} = {1,2} we deﬁne the surfaces

![image 23](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile23.png>)

![image 24](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile24.png>)

![image 25](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile25.png>)

Σj(h) = {ξ ∈ Λj ∩ (h − Λk) | Φj(ξ) + Φk(h − ξ) = a}.

Note that Σj(h) ⊂ Λj ⊂ Rn and these surfaces are related to the intersection of the surfaces Sj ∩ (h − Sk) through the formula

Sj ∩ (h − Sk) = {(Φj(ξ),ξ)|ξ ∈ Σj(h)}. The sets Σj(h) play a crucial role in what follows. The key curvature, transversality, and smoothness assumptions we make on the phases Φj are the following.

Assumption 1.1. Fix constants C0,d0 > 0. For j = 1,2 we let Λj ⊂ Rn be an open set, and Φj : Λj → R satisfy the conditions:

- (A1) for every {j,k} = {1,2}, h ∈ R1+n, ξ,ξ′ ∈ Σj(h), and η ∈ Λk we have ∇Φj(ξ) − ∇Φj(ξ′) ∧ ∇Φj(ξ) − ∇Φk(η) C0VmaxHj|ξ − ξ′|

and

C0 ∇Φj(ξ) − ∇Φj(ξ′) Hj|ξ − ξ′|,

- (A2) for j ∈ {1,2} we have Φj ∈ C5n(Λj) and moreover


1 m−2

d0, Vmax Hj

Hj  ∇mΦj L∞(Λj)

![image 26](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile26.png>)

d0.

min

![image 27](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile27.png>)

![image 28](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile28.png>)

3 m 5n

The key assumption (A1) is essentially equivalent to the conditions appearing previously in the literature [14, 1, 4], except that we require a normalised version to correctly determine the dependence of the constant on the phases Φj. To gain a better geometric understanding of (A1), we observe that letting ξ′ → ξ and taking η = h − ξ, since ∇Φj(ξ) − ∇Φk(h − ξ) is normal to Σj(h), (A1) implies the local condition

∇2Φj(ξ)v ∧ n C0Hj|v| (1.4) for all v ∈ TξΣj(h), where n is the unit normal to Σj(h), and TξΣj(h) is the tangent plane at ξ ∈ Σj(h). Under certain conditions, the local condition (1.4) is in fact equivalent to the global assumption (A1), see Lemma 2.1 below. In view of (1.4), (A1) states that the Hessian ∇2Φj(ξ) can not rotate tangent vectors in Σj(h) to normal vectors. A similar observation was made to [1] where the assumption (A1) was replaced with a condition on the shape operator associated to the surface Sj. We should emphasise here that in the general phase case, it is not suﬃcient to simply assume the surfaces Sj intersect transversally, and a stronger condition of the form (A1) is necessary [11, 26].

There are two immediate consequences of (A1) which we wish to highlight. The ﬁrst, is that for every ξ ∈ Λ1 and η ∈ Λ2 we have the transversality bound

∇Φ1(ξ) − ∇Φ2(η) C0Vmax (1.5)

which follows by observing that for every ξ ∈ Λj there exists h ∈ R1+n such that ξ ∈ Σj(h). The second, is that for every j ∈ {1,2}, h ∈ R1+n, and ξ,ξ′ ∈ Σj(h) we have the (global) curvature type bound

∇Φj(ξ) − ∇Φj(ξ′) C0Hj|ξ − ξ′|. (1.6)

The bounds (1.5) and (1.6) play a key role in the proof of Theorem 1.2, and in fact the stronger bound contained in (A1) is only directly required in the proof of Lemma 7.2 below.

The smoothness assumption (A2) requires that the phases to lie in C5n(Λj), this can probably be improved, but we do not consider this issue here. While the constant C0 should be thought of as a universal constant, it is important to keep track of the parameter d0 as it encodes the size of the Fourier support of the underlying waves, and scales like the frequency ξ. For instance, if Φ1(ξ) = |ξ|s for some s > 0, then (A2) essentially requires d0 |ξ| on Λ1. More generally, we observe that both the assumptions (A1) and (A2) are invariant under the rescaling

Λj,Φj(ξ),d0  → µ−1Λj,λΦj(µξ),µ−1d0 (1.7) and linear translations

Φj  → Φj + ξ · ξ0. (1.8) These invariances signiﬁcantly simplify the arguments to follow, as we can then reduce to the case where the maximum velocity and curvature are normalised to be one. In fact the precise assumptions (A1) and (A2) were carefully chosen with the scaling (1.7) and translation invariance (1.8) in mind.

We are now ready to state our ﬁrst main theorem.

Theorem 1.2. Let n 2, C0 > 0, 1 q,r 2, and 1q + n2+1r < n+12 . There exists a constant C > 0, such that for any d0 > 0, any open sets Λ1,Λ2 ⊂ Rn, any phases Φ1 and Φ2 satisfying Assumption 1.1 with

![image 29](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile29.png>)

![image 30](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile30.png>)

![image 31](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile31.png>)

- H2 H1, and any Φ1-waves u, and Φ2-waves v satisfying the support conditions supp u + d0 ⊂ Λ1, supp v + d0 ⊂ Λ2, min{diam(supp u),diam(supp v)} d0,


we have

1 q − 12

- H1

![image 32](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile32.png>)

- H2


n+1

1 q − 1r

r − 2q

1 r −1

max H1−

tLrx(R1+n) Cdn+1−

![image 33](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile33.png>)

![image 34](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile34.png>)

![image 35](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile35.png>)

![image 36](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile36.png>)

![image 37](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile37.png>)

![image 38](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile38.png>)

![image 39](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile39.png>)

0 V

t L2x. (1.9)

uv Lq

u L∞

t L2x v L∞

1

The proof of Theorem 1.2 follows the strategy used by Tao in the proof of the endpoint bilinear restriction estimate for the cone [21]. In particular, we replace the combinatorial Kakeya type arguments used by Wolﬀ in the seminal paper [27] and further exploited in, for instance, [22, 14, 4, 20], with energy estimates across transverse hypersurfaces. A similar argument was used by Bejenaru [1] to obtain a bilinear restriction estimate with q = r for general phases at unit scale. For our purposes, arguing via energy estimates has a number of advantages, ﬁrstly it avoids the ǫ loss that occurs when using the pigeon hole type arguments that arise in the combinatorial approach, and secondly it can be adapted without too much eﬀort to handle interactions with waves at very diﬀerent scales by using the wave table construction of Tao.

Remark 1.3. The extension of the bilinear restriction estimates to vector valued waves, was ﬁrst obtained by Tao [21] where the vector valued nature of the waves played an important technical role in the induction argument. As the proof of Theorem 1.2 follows the argument used by Tao, the fact that we may take vector valued waves in Theorem 1.2 also plays an important technical role here. However, there is an additional gain that comes from working with vector valued waves, which turns out to be very useful for applications of Theorem 1.2 to problems in nonlinear PDE. This gain comes from the simple observation that if we have an estimate for vector valued waves, then we can immediately deduce that the same bound holds in the atomic Banach space UΦ2

. In particular, Theorem 1.2 also holds in UΦ2

, see Corollary 1.6 below. The fact that Theorem 1.2 holds for vector valued waves, is a reﬂection of the fact that the proof essentially only exploits bilinear estimates in L2, for which the theory for scalar valued and vector valued waves is identical. A previous joint work of the author and Herr [4], used a similar observation, although phrased in terms of UΦ2

j

j

atoms, to prove a unit scale bilinear restriction in the adapted function space VΦ2

. The work [4] provided a strong motivation to consider the case of non-unit scale waves, however it is important to note that the argument used in [4] follows the combinatorial Kakeya type approach to bilinear restriction estimates, in contrast to the energy type approach used here. In particular, it is also possible to prove estimates for vector valued waves via the combinatorial approach.

j

j

Theorem 1.2 is optimal up to endpoints, in the sense that the restriction q1 + n2+1r n+12 is necessary, and the dependence on Φj and d0 in (1.9) cannot be improved, see Section 3. In particular, if the Fourier support of u or v is contained in a ball of radius d0, then the dependence of (1.9) on d0 is sharp. However,

![image 40](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile40.png>)

![image 41](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile41.png>)

![image 42](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile42.png>)

if the support of u (or v) is not well approximated by a ball, then certain improvements are possible. One possibility is the following. Given sets Λ∗j ⊂ Λj, we deﬁne the quantity

1 n−1

![image 43](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile43.png>)

1(h) Σ1(h) ∩ Λ∗1 ∩ h − Λ∗2

d[Λ∗1,Λ∗2] = sup

(1.10)

σΣ

h=(a,h)∈R1+n

j(h) denotes the (induced) Lebesgue surface measure on the surface Σj(h) ⊂ Rn. It easy to check that, under the transversality assumption (1.5), we have the bound d[Λ∗1,Λ∗2] min{diam(Λ∗1),diam(Λ∗2)}. However d[Λ∗1,Λ∗2] can potentially be much smaller as it only requires the intersection of supp u, the surface Σ1(h), and translates of supp v to be small. The quantity d[Λ∗1,Λ∗2] arises precisely in the bilinear L2t,x estimate. In fact, under the transversality assumption (1.5) we have for every Φ1-wave u, and Φ2-wave v,

where σΣ

n−1

- 1

![image 44](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile44.png>)

- 2 (d[supp u,supp v])


(C0Vmax)−

uv L2

2 u L∞

t L2x v L∞

t L2x, see Theorem 5.2 below. Exploiting this observation leads to the following improvement of Theorem 1.2.

![image 45](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile45.png>)

t,x

Theorem 1.4. Let n 2, C0 > 0, 1 q,r 2, and 1q + n2+1r < n+12 . There exists a constant C > 0, such that for any d0 > 0, any open sets Λ1,Λ2 ⊂ Rn, any phases Φ1 and Φ2 satisfying Assumption 1.1 with H2 H1, and any Φ1-waves u, and Φ2-waves v satisfying the support conditions

![image 46](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile46.png>)

![image 47](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile47.png>)

![image 48](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile48.png>)

d0 C0

supp u + d0 ⊂ Λ1, supp v + d0 ⊂ Λ2, d supp u + d0,supp v + d0

, we have

![image 49](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile49.png>)

1 q − 12

- H1

![image 50](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile50.png>)

- H2


n+1

1 q − 1r

r − 2q

1 r −1

max H1−

tLrx(R1+n) Cdn+1−

![image 51](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile51.png>)

![image 52](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile52.png>)

![image 53](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile53.png>)

![image 54](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile54.png>)

![image 55](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile55.png>)

![image 56](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile56.png>)

![image 57](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile57.png>)

0 V

uv Lq

u L∞

t L2x v L∞

t L2x.

1

Remark 1.5. It is clear that if min{diam(supp u),diam(supp v)} d0, then since one of supp u + d0 or supp v + d0 is again contained in a ball of radius d0, a computation gives

d supp u + d0,supp v + d0 d0. In particular, after potentially choosing C0 slightly smaller, we see that Theorem 1.4 implies Theorem 1.2. We note here that the d0 thickening of the Fourier supports, namely supp u + d0 and supp v + d0, arises as the induction on scales argument used in the proof of Theorem 1.4 involves numerous decompositions of u and v into wave packets, each of which may have slightly larger Fourier support. Thus we require some room to increase the Fourier support in the induction argument, which eventually manifests itself in the assumptions in Theorem 1.4 applying to a d0 neighbourhood of the Fourier supports of u and v.

We now give a number a number of consequences of Theorem 1.4. Namely, we state a version of Theorem

1.4 in the adapted function space UΦ2, and give a concrete application to the case of elliptic and Klein-Gordon waves. Moreover, we prove a new reﬁned Strichartz estimate for the Klein-Gordon equation.

- 1.2. Bilinear Restriction in Adapted Function spaces. Theorem 1.4 has a number of applications to linear PDE, for instance, we give a new bilinear restriction estimate for wave/Klein-Gordon interactions, together a reﬁned Strichartz type estimate for the Klein-Gordon equation, see Theorem 1.10 and Theorem 1.12 below. However, in applications to nonlinear PDE, it is useful to have a version of Theorem 1.4 which


holds for more general functions than just Φj-waves. Often the function spaces which arise in applications satisfy some version of the transference principle. This principle roughly asserts that if we have an estimate for Φj-waves, then we immediately deduce that the estimate also holds in some more general function space. For instance the well-known Xs,b type spaces satisfy the transference principle, essentially since elements of Xs,b type spaces can be written as averages of free waves. On the other hand, other function spaces of interest, such as the adapted function spaces UΦp

and VΦp

, do not generally satisfy such a strong property, and signiﬁcant additional work can be required to extend estimates for free waves, to estimates in UΦp

j

j

, see for instance [4] for further discussion.

j

However, the adapted function space UΦ2

does satisfy a slightly weaker transference type principle: if an estimate holds for vector valued waves, then it also holds in UΦ2

j

. Consequently, the fact that Theorem 1.4 holds for vector valued waves, immediately implies that bilinear restriction type estimates for functions in UΦ2

j

, see the proof of Corollary 1.6 below or [4, Remark 5.2] for details of this argument. Bilinear restriction

j

type estimates in the adapted function spaces UΦp

and VΦp

ﬁrst appeared in work of Sterbenz-Tataru [19, Lemma 5.7], and the full bilinear range for general phases at unit scale was obtained recently in [4]. The atomic function spaces UΦp

j

j

have proven to be extremely useful in obtaining endpoint well-posedness results for dispersive PDE, see for instance [9, 10, 7] and the references therein.

j

Before we can state our next result, we require the deﬁnition of UΦp

. Let 1 < p < ∞. We say that φ is a UΦp

j

atom, if there exists a ﬁnite partition I of R, and a collection of Φj-waves (φI)I∈I such that φ = I∈I 1I(t)φI and

j

1 p

![image 58](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile58.png>)

φI pL∞

1.

t L2x

I∈I

The atomic Banach space UΦp

is then deﬁned as

j

UΦp

=

j

m

cmφm (cm)m∈N ∈ ℓ1(N), φm are UΦp

j

atoms

with the induced norm

= inf

|cm|

u Up

Φj

u= m cmφm

m

atoms φm. Note that functions in UΦp

where the inf is over all representations of u in terms of UΦp

take values in ℓ2(Z), in particular, every Φj-wave with norm of size one, is a (trivial) example of a UΦp

j

j

atom.

j

Corollary 1.6. Let n 2, C0 > 0, 1 q,r 2, and q1 + n2+1r < n+12 . There exists a constant C > 0, such that for any d0 > 0, any open sets Λ1,Λ2 ⊂ Rn, any phases Φ1 and Φ2 satisfying Assumption 1.1 with H2 H1, and any u ∈ UΦ2

![image 59](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile59.png>)

![image 60](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile60.png>)

![image 61](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile61.png>)

, v ∈ UΦ2

satisfying the support conditions

1

2

d0 C0

supp u + d0 ⊂ Λ1, supp v + d0 ⊂ Λ2, d supp u + d0,supp v + d0

, we have

![image 62](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile62.png>)

1 q −12

- H1

![image 63](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile63.png>)

- H2


n+1

1 q − r1

r − 2q

1 r −1 max H1−

tLrx(R1+n) Cdn+1−

![image 64](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile64.png>)

![image 65](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile65.png>)

![image 66](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile66.png>)

![image 67](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile67.png>)

![image 68](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile68.png>)

![image 69](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile69.png>)

![image 70](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile70.png>)

0 V

uv Lq

u U2

v U2

.

1

Φ1

Φ2

Proof. We exploit the transference type principle mentioned above. It is enough to consider the case where

- u = I∈I 1I(t)uI and v = J∈J 1J(t)vI are atoms. Deﬁne the vector valued waves U = (uI)I∈I and V = (vJ)J∈J . Then since u and v are atoms, U is a Φ1-wave, V is a Φ2-wave, we have the energy estimate


t L2x 1, and the pointwise bounds

U L∞

t L2x, V L∞

1I(t)|uI|

1I(t)|U| |U|,

I∈I

I∈I

J∈J

Therefore corollary follows from an application of Theorem 1.4.

1J(t)|vJ| |V |. (1.11)

The bound (1.11) is somewhat crude, and in fact Corollary 1.6 can be improved by further exploiting the time localisation of the UΦp

atoms directly in the proof of Theorem 1.4. More precisely, by reﬁning the

j

argument used to prove Theorem 1.4, and interpolating with an “linear” version of the bilinear L2t,x inside the induction on scales argument, we obtain the following improvement of Corollary 1.6.

- Theorem 1.7. Let n 2, C0 > 0, 1 q,r 2 and 1q + n2+1r < n+12 . Let (n+1)2 q < 1b a 1 12 and 1 a + 1b min{ 1q,r}. There exists a constant C > 0, such that for any d0 > 0, any open sets Λ1,Λ2 ⊂ Rn,


![image 71](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile71.png>)

![image 72](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile72.png>)

![image 73](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile73.png>)

![image 74](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile74.png>)

![image 75](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile75.png>)

![image 76](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile76.png>)

![image 77](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile77.png>)

![image 78](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile78.png>)

![image 79](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile79.png>)

![image 80](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile80.png>)

any phases Φ1 and Φ2 satisfying Assumption 1.1 with H2 H1, and any u ∈ UΦa

, v ∈ UΦb

satisfying the support conditions

1

2

supp u + d0 ⊂ Λ1, supp v + d0 ⊂ Λ2, d supp u + d0,supp v + d0

d0 C0

,

![image 81](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile81.png>)

we have uv Lq

tLrx(R1+n) Cdn+1−

(1.12)

1

(1− 1r − 1b )+

q−12+(n+1)(12−a1) µnVmax dn0+1H1

- H1

![image 82](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile82.png>)

- H2


n+1

1 q − r1

r − 2q

1 r −1 max H1−

![image 83](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile83.png>)

![image 84](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile84.png>)

![image 85](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile85.png>)

![image 86](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile86.png>)

![image 87](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile87.png>)

![image 88](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile88.png>)

![image 89](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile89.png>)

![image 90](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile90.png>)

![image 91](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile91.png>)

![image 92](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile92.png>)

![image 93](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile93.png>)

0 V

v Ub

u Ua

![image 94](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile94.png>)

1

Φ1

Φ2

where µ = min{diam(supp u),diam(supp v),d0} and s+ = s if s > 0, and zero otherwise.

The bound (1.12) has the useful consequence that we may place v into the weaker VΦ2 space without the standard high-low frequency loss. To make this claim more precise, deﬁne the space VΦ2 as all right continuous functions such that

- 1

![image 95](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile95.png>)

- 2


e−it

kΦ(−i∇)u(tk) − e−it

k−1Φ(−i∇)u(tk−1) 2L2

< ∞

= u L∞

t L2x + sup

u V2

Φ

x

(tk)∈Z k∈Z

where Z = {(tj)j∈Z | tj ∈ R and tj < tj+1}. Thus functions in VΦ2 have ﬁnite quadratic variation along the ﬂow eitΦ(−i∇). An application of the continuous embedding VΦ2 ⊂ UΦa for a > 2 [9, Lemma 6.4], together with (1.12) implies that we then have

1 q − 12

- H1

![image 96](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile96.png>)

- H2


n+1

1 q − 1r

r −q2

1 r −1

max H1−

tLrx(R1+n) Cdn+1−

![image 97](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile97.png>)

![image 98](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile98.png>)

![image 99](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile99.png>)

![image 100](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile100.png>)

![image 101](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile101.png>)

![image 102](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile102.png>)

![image 103](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile103.png>)

0 V

uv Lq

u U2

v V2

1

Φ1

Φ2

provided that 1 < q 2, 1 < r < 2, and q1 + n2+1r < n+12 . This bound is precisely the same as the case of free solutions. In particular, we avoid the high-low frequency loss which would come from simply deducing

![image 104](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile104.png>)

![image 105](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile105.png>)

![image 106](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile106.png>)

a VΦ2 bound from Corollary 1.6 via an interpolation argument. In the special case q = r = 2, we get a loss, and only obtain

µnVmax dn0+1H1

ǫ

n−1 2

1

0 V−

t,x(R1+n) Cd−

![image 107](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile107.png>)

![image 108](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile108.png>)

max2

uv L

u U2

v V2

.

![image 109](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile109.png>)

2

Φ1

Φ2

This bilinear L2t,x bound is particularly interesting in the case of the wave or Klein-Gordon equation, as it allows us to place the high frequency wave into the weaker VΦ2

space without losing any high-frequency derivatives.

2

- 1.3. The Elliptic Case. We say that a phase Φ : Λ → R is elliptic on Λ, if for all ξ ∈ Λ and v ∈ Rn we have


∇2Φ(ξ)v · v ≈  ∇2Φ L∞(Λ)|v|2.

Equivalently, the eigenvalues of ∇2Φ all have the same sign, and are essentially of the size  ∇2Φj L∞(Λ). A typical example of an elliptic phase is the Schrodinger phase Φ = 12|ξ|2, or the Klein-Gordon phase (m2 + |ξ|2)12 in the region |ξ| ≪ m. Bilinear restriction estimates for elliptic phases was recently exploited by Stovall [20] to deduce new results for the linear restriction problem. Applying Theorem 1.4 to the case of elliptic phases, gives the following improvement to [20, Theorem 2.1].

![image 110](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile110.png>)

![image 111](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile111.png>)

- Theorem 1.8. Let 1 q,r 2, 1q + n2+1r < n+12 , and d0 > 0. Let Λj ⊂ Rn be convex, and Φj ∈ C5n(Λj) be elliptic phases such that H2 H1,


![image 112](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile112.png>)

![image 113](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile113.png>)

![image 114](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile114.png>)

1 m−2

Hj  ∇mΦj L∞(Λj)

diam(Λj) Vmax Hj

![image 115](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile115.png>)

, diam(Λj) min

, and for all ξ ∈ Λ1, η ∈ Λ2

![image 116](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile116.png>)

![image 117](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile117.png>)

2 m 5n

∇Φ1(ξ) − ∇Φ2(η) Vmax. Then for any Φ1-waves u, and Φ2-waves v satisfying the support conditions

d0 C0

supp u + d0 ⊂ Λ1, supp v + d0 ⊂ Λ2, d supp u + d0,supp v + d0

, we have

![image 118](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile118.png>)

1 q − 12

- H1

![image 119](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile119.png>)

- H2


n+1

1 q − r1

r − 2q

1 r −1

max H1−

tLrx(R1+n) dn+1−

![image 120](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile120.png>)

![image 121](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile121.png>)

![image 122](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile122.png>)

![image 123](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile123.png>)

![image 124](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile124.png>)

![image 125](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile125.png>)

![image 126](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile126.png>)

0 V

u L∞

t L2x v L∞

t L2x.

uv Lq

1

Remark 1.9. The precise assumptions used in the Theorem 1.8 can be weakened slightly (in particular the convexity assumption). See the proof of Lemma 2.1 below.

- 1.4. Bilinear Restriction for the Klein-Gordon equation. We now turn to the case of the Klein-Gordon equation. Let

ξ m = (m2 + |ξ|2) Note that when m = 0 this is simply the wave phase |ξ|. If we have the support assumptions

- 1

![image 127](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile127.png>)

- 2 .


supp f ⊂ {|ξ| ≈ λ,θ(ξ,ω0) ≪ α}, supp g ⊂ {|ξ| ≈ λ,θ(ξ,ω1) ≪ α} with θ(ω0,ω1) ≈ α (here θ(x,y) denotes the angle between vectors x,y ∈ Rn) then it is known that for

- 1 q + n2+1r < n+12 , 1 q,r 2, and λ µ we have the bilinear estimate for the wave equation


![image 128](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile128.png>)

![image 129](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile129.png>)

![image 130](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile130.png>)

eit|∇|feit|∇|g Lq

tLrx αn−1−

n−1

![image 131](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile131.png>)

r −2q µn−

![image 132](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile132.png>)

n

![image 133](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile133.png>)

r −q1 λ µ

![image 134](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile134.png>)

![image 135](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile135.png>)

1 q − 21

![image 136](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile136.png>)

![image 137](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile137.png>)

f L2 g L2, see [21, 24, 13, 12]. An application of Theorem 1.4 gives the following Klein-Gordon counterpart. Theorem 1.10 (Bilinear extension for K-G). Let 1 q,r 2, q1 + n2+1r < n+12 , m1,m2 0, and λ µ > 0. Let 0 < α 1, and suppose we have ξ0,η0 ∈ Rn such that ξ0 m

![image 138](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile138.png>)

![image 139](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile139.png>)

![image 140](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile140.png>)

1

≈ λ, η0 m

2

≈ µ, and m2|ξ0| − m1|η0| λµ

![image 141](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile141.png>)

+ |ξ0||η0| ∓ ξ0 · η0 λµ

![image 142](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile142.png>)

- 1

![image 143](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile143.png>)

- 2


≈ α. Deﬁne β = (m

1

![image 144](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile144.png>)

αλ + m

2

![image 145](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile145.png>)

αµ + 1)−1. If supp f ⊂ |ξ|−|ξ0| ≪ βλ, |ξ||ξ0|−ξ·ξ0

- 1

![image 146](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile146.png>)

- 2


≪ αλ , supp g ⊂ |ξ|−|η0| ≪ βµ, |ξ||η0|−ξ·η0

- 1

![image 147](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile147.png>)

- 2


≪ αµ then we have the bilinear estimate

eit −i∇ 

m1fe±it −i∇ 

m2g Lq

tLrx αn−1−

n−1

![image 148](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile148.png>)

r −2q β1−

![image 149](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile149.png>)

1

![image 150](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile150.png>)

r µn−

n

![image 151](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile151.png>)

r −1q λ µ

![image 152](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile152.png>)

![image 153](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile153.png>)

1 q −12

![image 154](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile154.png>)

![image 155](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile155.png>)

f L2

x

g L2

x

where the implied constant is independent of m1,m2.

Note that Theorem 1.10 contains both wave like regimes (when β ≈ 1), and Schr¨odinger like regimes (when β ≪ 1). In particular, if β = 1, then the support assumptions on f and g are the same as in the case of the wave equation, while if β ≈ α, then the support assumptions reduce to simply requiring that

supp f ⊂ {|ξ − ξ0| ≪ αλ}, supp g ⊂ {|ξ − η0| ≪ αµ,} which matches the standard assumptions used in the Schr¨odinger case (see for instance Theorem 1.8 above).

- Remark 1.11. If we apply the atomic bilinear restriction estimate, Theorem 1.7, in place of Theorem 1.2, under the same assumptions as those in Theorem 1.10, we arrive at the stronger bounds


uv Lq

tLrx αn−1−

n−1

![image 156](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile156.png>)

r −2q β1−

![image 157](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile157.png>)

1

![image 158](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile158.png>)

r µn−

n

![image 159](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile159.png>)

r −1q λ µ

![image 160](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile160.png>)

![image 161](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile161.png>)

1 q − 12

![image 162](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile162.png>)

![image 163](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile163.png>)

u U2

 ∇ m1

v V2

± ∇ m2

.

In particular, in the special case q = r = 2, we may place v ∈ V± ∇ 2

m2

without a high frequency loss.

- 1.5. A Reﬁned Strichartz Estimates for the Klein-Gordon Equation. The standard H 12 Strichartz estimate for the Klein-Gordon equation states that


![image 164](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile164.png>)

eit ∇ f

n+1 n−1

2

![image 165](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile165.png>)

t,x (R1+n)

L

f H1

.

![image 166](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile166.png>)

2

It is of interest to understand the concentration properties of solutions which come close to maximising this inequality, for instance, understanding these concentrating solutions is a key step in obtaining a proﬁle decomposition. In the case of the Schr¨odinger equation, this concentration type property is a consequence of a reﬁned Strichartz estimate introduced by Bourgain [2] and extended in work of Moyua-Vargas-Vega [15, 16]. A version of the reﬁned Strichartz estimate for the Klein-Gordon equation was proved by Killip-Stovall-Visan [8] with data in the Klein-Gordon regime (in other words, the bound included a loss of derivatives when compared to the wave regime). Here we use Theorem 1.2 together with an argument used by Ramos [17] to obtain a reﬁned Strichartz estimate for the Klein-Gordon equation without any derivative loss.

Before we state the reﬁned Strichartz estimate for the Klein-Gordon equation, we require some notation. Given λ 1, and 0 < α < 1, we deﬁne Aλ,α to the collection of sets A ⊂ Rn of the form

- 1

![image 167](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile167.png>)

- 2


A = A(ξ0) = ξ ≈ λ, |ξ| − |ξ0| ≪ 1+αλαλλ, |ξ||ξ0| − ξ · ξ0

≪ αλ

![image 168](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile168.png>)

where the points ξ0 ∈ Rn satisfy ξ0 ≈ λ and are chosen to ensure that the sets A ∈ Aλ,α form a ﬁnitely overlapping cover of the annulus/ball { ξ ≈ λ}. In the wave like region α λ 1, the elements of Aλ,α are radial sectors of the annuli ξ ≈ λ, while in the Klein-Gordon (or Schr¨odinger) like case α ≪ λ1, the elements of Aλ,α are angular sectors with some additional radial restrictions which degenerate to cubes if λ 1.

![image 169](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile169.png>)

![image 170](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile170.png>)

Theorem 1.12 (Reﬁned Strichartz). Let n 2. There exists 0 < θ < 1 and 1 < r < 2 such that eit ∇ f

1 n+1

θ

![image 171](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile171.png>)

- 1

![image 172](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile172.png>)

- 2−r1 f Lr


- 1

![image 173](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile173.png>)

- 2


f 1−θ

αλ 1+αλ

|A|

sup

sup

λ

.

![image 174](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile174.png>)

2 n+1 n−1

ξ(A)

![image 175](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile175.png>)

H 12

![image 176](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile176.png>)

![image 177](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile177.png>)

t,x (R1+n)

A∈Aλ,α

λ∈2N,α∈2−N

L

This estimate is the Klein-Gordon counterpart to the estimate for the wave equation obtain by Ramos [17]. Applications of Theorem 1.12 to the H appear elsewhere.

- 1

![image 178](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile178.png>)

- 2 proﬁle decomposition for the Klein-Gordon equation will


- 1.6. Outline. In Section 2 we ﬁrst show that the global condition (A1) is equivalent to the local condition

- (1.4), and adapt an argument from [4] to give a simpliﬁcation of the transversality/curvarture condition (A1). We then give the proof of the main consequences of Theorem 1.4, namely the elliptic case Theorem


- 1.8, the Klein-Gordon case, Theorem 1.10, and the reﬁned Strichartz estimate, Theorem 1.12. In Section 3 we give a counter example which shows that the dependence on the phases Φj, and the


frequency parameter d0 in Theorem 1.2 is sharp. The counter example is based on constructing waves u and

- v which are sums of wave packets concentrating on an ǫ−1 neighbourhood of the space-time rectangle s + s′,−s∇Φ1(ξ0) − s′∇Φ2(η0) 0 s (ǫ2H1)−1, 0 s′ (ǫ2H2)−1


with ξ0 ∈ Λ1 and η0 ∈ Λ2. In Section 4, we run the induction on scales argument, which reduces the proof of Theorem 1.4 to showing

that we may control the LqtLrx norm on a cube of diameter R, by a cube of diameter R2 . The induction argument applied here is slightly diﬀerent to that used in Lee-Vargas [13], and in particular it is here where

![image 179](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile179.png>)

we are able to avoid the ǫ loss in the scale factors that occurred in previous works.

In Section 5 we apply localisation arguments to further reduce the proof of Theorem 1.4 to obtaining a key wave table type decomposition, Theorem 5.1, which decomposes the product uv into a term which is concentrated at scale R2 , together with a term that satisﬁes an improved bilinear estimate. The proof of the decomposition contained in Theorem 5.1 is the key step in the proof of Theorem 1.4.

![image 180](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile180.png>)

Section 6 contains the general wave packet decomposition used in the present article, while, in Section 7, closely following [4], we give the key geometric consequences of (A1). The energy estimates across transverse surfaces we require are given in Section 8. These estimates rely heavily on the geometric consequences of the curvature and transversality assumption (A1) contained in Section 7.

- In Section 9 we give the main step in the wave table construction, namely, following Wolﬀ [27] and Tao [21], we use the wave packet decomposition, together with an energy argument, to decompose u into wave packets such that v restricted to the corresponding tube is concentrated on a small cube.
- In Section 10 we use the construction in Section 9 to give the proof of Theorem 5.1 and construct the general wave tables that are required in the proof of the localised bilinear restriction estimate.


Finally, in Sections 11 and 12, we give the proof of Theorem 1.7. This relies on developing an “atomic” version of the wave table construction used in Section 9, together with an additional interpolation argument with a “linear” version of the classical bilinear L2t,x estimate.

- 1.7. Notation. Throughout this article, we use the notation a b if a CB for some constant C > 0 which may depend only on C0, q, r, and the dimension n. In particular, all implied constants will otherwise be independent of the phases Φj. Similarly we write a ≈ b if a b and b a, and a ≫ b if a Cb with C 100n. For a ∈ R, we let a+ = a if a > 0, and a+ = 0 otherwise.


Given a set Ω ⊂ Rn and a vector h ∈ Rn, we let Ω+h = {x+h | x ∈ Ω} denote the translation of Ω by h. At a risk of causing some minor confusion, for a positive constant c > 0 we let Ω+c = {x+y | x ∈ Ω, |y| < c}

be the Minkowski sum of Ω and the ball {|x| < c}. We also let diam(Ω) = supx,y∈Ω |x − y|. For a function f ∈ L1(Rn), we let f(ξ) =

Rn f(x)e−ix·ξdx denote the spatial Fourier transform. Similarly, if u ∈ L1(R1+n), we deﬁne the space-time Fourier transform of u as u˜(τ,ξ) =

´

R1+n u(t,x)e−i(t,x)·(τ,ξ) dtdx and let u(t) be the Fourier transform of u in the spatial variable x ∈ Rn.

´

Let R 1 and 0 < ǫ 1. The constant R will denote the large space-time scale and 0 < ǫ 1 will be a small ﬁxed parameter used to control the various error terms that arise. Given a scale r > 0, we decompose phase space into the grid Xr,ǫ = ǫr2Zn × 1rZn. Given a point γ = (x0,ξ0) ∈ Xr,ǫ in phase-space, we let x(γ) = x0 and ξ(γ) = ξ0 denote the projections onto the ﬁrst and second components respectively.

![image 181](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile181.png>)

![image 182](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile182.png>)

Associated to a phase Φj, and a scale R, we let rj = (HjR)21 denote the scale of the corresponding wave packets. Deﬁne

![image 183](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile183.png>)

Γj = (x0,ξ0) ∈ Xrj,ǫ ξ0 + 41d0 ⊂ Λj .

![image 184](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile184.png>)

Thus Γj contains those phase space points inside Λj, which are at least 41d0 from the boundary of Λj. Given a point γj = (x0,ξ0) ∈ Γj we deﬁne the associated tubes

![image 185](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile185.png>)

= {(t,x) ∈ R1+n | |x − x0 + t∇Φj(ξ0)| rj}.

Tγ

j

The geometric condition (A1) plays an important role in the proof of Theorem 1.2 by restricting the intersections of various tubes to certain transverse hypersurfaces. However, to exploit the curvature hypothesis in (A1), we need to restrict points in Γj to those close to Σj(h). To this end, given h ∈ R1+n and a set Λ ⊂ Rn, we deﬁne

Γj(h,Λ) = γj ∈ Γj ξ(γj) ∈ Σj(h) ∩ Λ + rC

![image 186](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile186.png>)

j

where the constant C will depend on the dimension n and C0, but will otherwise be independent of the phase Φj. We also deﬁne the conic hypersurface

Cj(h) = s,−s∇Φj(ξ) s ∈ R,ξ ∈ Σj(h) .

All cubes in this article are oriented parallel to the coordinate axis. Let Q be a cube side length R, and take a subscale 0 < r R. We deﬁne Qr(Q) to be a collection of disjoint subcubes of width 2−j

R which form a cover of Q, where j0 is the unique integer such that 2−1−j

0

R < r 2−j

R. Thus all cubes in Qr(Q) have side lengths ≈ r, and moreover, if r r′ R and q ∈ Qr(Q), q′ ∈ Qr′(Q) with q ∩ q′ = ∅, then q ∈ Qr(q′). To estimate various error terms which arise, we will need to create some separation between cubes. To this end, following Tao, we introduce the following construction. Given 0 < ǫ ≪ 1 and a subscale 0 < r R, we let

0

0

Iǫ,r(Q) =

(1 − ǫ)q.

q∈Qr(Q)

Note that we have the crucial property, that if q ∈ Qr(Q), and (t,x)  ∈ Iǫ,r(Q) ∩ q, then dist (t,x),q ǫr. We require smoothed out bump functions adapted to cubes q ∈ Qr(Q). To this end, given q ∈ Qr(Q) we

let χq ∈ C∞(R1+n) be a positive function such that χq 1 on q, supp χq ⊂ {|(τ,ξ)| r 1}, and we have the decay bound, for every N ∈ N,

![image 187](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile187.png>)

−N

dist((t,x),q) r

χq(t,x) N 1 +

. Given a point γj = (x0,ξ0) ∈ Γj, and a cube q ∈ Qrj

![image 188](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile188.png>)

(Q), we deﬁne the weights

5n

j,q = 1 + |xq − x0 + tq∇Φj(ξ0)| rj

wγ

![image 189](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile189.png>)

j ∩q = ∅, and are very large when q and the tube Tγ

where (tq,xq) denotes the centre of the cube q. Thus the weights wγ

j,q are essentially one when Tγ

are far apart.

j

For a subset Ω ⊂ R1+n we let 1Ω denote the indicator function of Ω. Let E be a ﬁnite collection of subsets

of R1+n, and suppose we have a collection of (ℓ2c-valued) functions (u(E))E∈E. We then deﬁne the associated quilt

[u(·)](t,x) =

1E(t,x)|u(E)(t,x)|.

E∈E

This notation was introduced by Tao [21], and plays a key technical role in localising the product uv into smaller scales.

2. Applications

- 2.1. Alternative conditions on phases. The key assumption (A1) is a global condition, in the sense that it depends on the behaviour of the phase Φj at two points ξ,ξ′ ∈ Σj(h). In certain cases, it can instead be convenient to have a local version of (A1) which only depends on the behaviour of Φj in a neighbourhood of ξ ∈ Σj(h). Clearly a suitable candidate for such a local condition can be found by simply taking ξ′ → ξ in (A1). More precisely, we can state a local version of (A1) as:


(A1’) for every {j,k} = {1,2}, ξ ∈ Λj, η ∈ Λk, and v ∈ Rn with v · (∇Φj(ξ) − ∇Φk(η)) = 0, we have ∇2Φj(ξ)v ∧ ∇Φj(ξ) − ∇Φk(η) C′0HjVmax|v|.

Note that if h = (Φj(ξ) + Φk(η),ξ + η), then ∇Φj(ξ) − ∇Φk(η) is the normal vector to the tangent space TξΣj(h). Thus the condition on v in (A1’) can be written as v ∈ TξΣj(h). In particular, letting ξ′ → ξ in Σj(h), we see that (A1) implies (A1′). To prove the converse implication requires making an additional global assumption on the behavior of the phases Φj on the sets Λj. One possibility is the following.

- Lemma 2.1 (Local implies global). Let C′0 > 0. Assume that for all h ∈ R1+n we have ConvexHull[Σ1(h)] ⊂ Λ1 ∩ (h − Λ2), (2.1)


and the small variation bounds sup

1 4

C′0Vmax (2.2) and, for all ξ,ξ′ ∈ Σj(h),

∇Φ2(η) − ∇Φ2(η′)

∇Φ1(ξ) − ∇Φ1(ξ′) + sup

![image 190](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile190.png>)

η,η′∈Λ2

ξ,ξ′∈Λ1

1 4

∇Φj(ξ) − ∇Φj(ξ′) − ∇2Φj(ξ)(ξ − ξ′)

C′0Hj|ξ − ξ′|. (2.3)

![image 191](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile191.png>)

If (A1′) holds, then (A1) also holds with constant C0 = 41C′0. Proof. Let h = (a,h) ∈ R1+n, ξ,ξ′ ∈ Σj(h), and η ∈ Λ2. For ease of notation, we let N = ∇Φj(ξ) − ∇Φk(η) and v = (ξ − ξ′) − [(ξ − ξ′) · |NN|]|NN|. Suppose for the moment that we have

![image 192](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile192.png>)

![image 193](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile193.png>)

![image 194](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile194.png>)

1 4

|(ξ − ξ′) · N|

C′0Vmax|ξ − ξ′|. (2.4) As v · N = 0, an application of (A1′) and (2.3) then gives

![image 195](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile195.png>)

∇Φj(ξ) − ∇Φj(ξ′) ∧ N

∇2Φj(ξ)v ∧ N − Vmax ∇Φj(ξ) − ∇Φj(ξ′) − ∇2Φ(ξ)(ξ − ξ′)| − Hj (ξ − ξ′) · N C′0HjVmax |v| −

1 4

- 1

![image 196](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile196.png>)

- 2|ξ − ξ′|


C′0HjVmax|ξ − ξ′|

![image 197](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile197.png>)

and hence (A1) follows. Thus it remains to verify the bound (2.4). We start by observing that the deﬁnition of the surface Σj(h) implies that Φj(ξ)−Φj(ξ′) = Φk(h−ξ)−Φk(h−ξ′). On the other hand, as Σj(h) = h−Σk(h),

- (2.1) gives ξ′ + t(ξ − ξ′) ∈ Λj ∩ (h − Λk) for 0 t 1. Consequently we have the identity ˆ 1


∇Φj ξ′ + t(ξ − ξ′) · (ξ − ξ′)dt = ˆ 1

∇Φk h − ξ′ + t(ξ′ − ξ) · (ξ′ − ξ)dt

0

0

and hence, by an application of (2.2), we have

ξ − ξ′ |ξ − ξ′|

N ·

![image 198](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile198.png>)

ˆ 1

∇Φj(ξ) − ∇Φj ξ′ + t(ξ − ξ′) dt + ˆ 1

0

0

1 4

C′0Vmax.

H1 + H2 d0

![image 199](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile199.png>)

∇Φk(η) − ∇Φk h − ξ′ + t(ξ′ − ξ) dt

Strictly speaking, the above argument shows that to move from the local condition (A1′) to the global condition (A1), it is enough to verify the bounds (2.3) and (2.4). However, in most applications of Lemma

- 2.1, the conditions (2.1), (2.2), and (2.3) can always be imposed by perhaps shrinking the sets Λj slightly. Thus it generally suﬃces to simply check (A1′).


In some applications of Theorem 1.2, it can be convenient to replace the assumption (A1) with a stronger suﬃcient condition.

- Lemma 2.2 ([4, Lemma 2.1]). Assume that (2.1) and (2.2) hold. If for all ξ,ξ′ ∈ Σj(h) we have the curvature type bound


∇Φj(ξ) − ∇Φj(ξ′) · (ξ − ξ′) C(1)0 Hj|ξ − ξ′|2, (2.5) and for ξ ∈ Λ1 and η ∈ Λ2 the transversality bound

∇Φ1(ξ) − ∇Φ2(η) C(2)0 Vmax (2.6) then (A1) holds with constant C0 = 21C(1)0 C(2)0 . Proof. We adapt the argument in [4] to the current setup. Let η ∈ Λk, ξ,ξ′ ∈ Σj(h) and take ω = ξ−ξ

![image 200](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile200.png>)

′

|ξ−ξ′|. The convexity condition (2.1) implies that |∇Φj(ξ) − ∇Φj(ξ′)| Hj|ξ − ξ′|. Hence the assumptions (2.5) and (2.6) give

![image 201](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile201.png>)

∇Φj(ξ)−∇Φj(ξ′) ∧ ∇Φj(ξ) − ∇Φk(η) | |∇Φj(ξ) − ∇Φk(η)| ∇Φj(ξ) − ∇Φj(ξ′) · ω − |∇Φj(ξ) − ∇Φj(ξ′)| ∇Φj(ξ) − ∇Φk(η) · ω

| ∇Φj(ξ) − ∇Φk(η) · ω| Vmax

HjVmax|ξ − ξ′| C(1)0 C(2)0 −

![image 202](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile202.png>)

where we used the elementary bound |x ∧ y| |y||x · ω| − |x||y · ω|. Consequently (A1) holds provided that for every ξ,ξ′ ∈ Σj(h), η ∈ Λk we have

C(1)0 C(2)0 2 Vmax.

ξ − ξ′ |ξ − ξ′|

∇Φj(ξ) − ∇Φk(η) ·

![image 203](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile203.png>)

![image 204](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile204.png>)

But this follows from the argument used to prove (2.4) together with the small variation condition (2.2).

- Remark 2.3. To better understand the connection between the conditions in Lemma 2.2, and the assumptions (A1) and (A1’), we observe that the later conditions are roughly equivalent to


∇2Φj(ξ)v ∧ N HjVmax|v|

for all v ∈ TξΣj(h), where N is the unit normal to Σj(h), and TξΣj(h) is the tangent plane at ξ ∈ Σj(h). On the other hand, letting ξ′ → ξ, we see that (2.5) is essentially equivalent to the lower bound

∇2Φj(ξ)v · v Hj|v|2 (2.7)

for all v ∈ TξΣj(h) (more precisely, it is easy to check that under an assumption like (2.3), the global condition (2.5) is equivalent to (2.7)). Consequently, (A1) and (A1’) state that the Hessian ∇2Φj(ξ) can not rotate tangent vectors in TξΣj(h) to normal vectors, while (2.5) imposes the much stronger condition, that ∇2Φj(ξ)v remains roughly parallel to v ∈ TξΣj(h). A similar remark, although phrased slightly diﬀerently, was made in [1].

In general, even with the use of the previous simpliﬁcations, it can be somewhat involved to apply Theorem

- 1.2 as the dependence on Φj is only sharp when applied phase which behave essentially uniformly on Λj. However a rough strategy is as follows. Suppose we are given phases Φ∗j on some (large) subset of Rn. The ﬁrst step is to restrict the domain until the gradients ∇Φ∗j have “small” variation. The second step is to rescale the domain, and hence replace Φ∗j with a rescaled version Φj, to ensure that the (nonzero) components of the Hessian ∇2Φj are all of a similar size. The ﬁnal step is then to restrict the rescaled domain further, to ensure that the transversality and curvature conditions hold. Clearly each of these steps depends heavily on the precise phases under consideration, and thus some amount of trial and error is needed to ﬁnd appropriate domains.
- 2.2. Elliptic Phases: Proof of Theorem 1.8. A short computation shows that, after potentially partitioning the sets Λj into smaller sets, the conditions (2.2) and (2.2) in Lemma 2.1 hold. Hence, using the ellipticity assumption, since for all ξ ∈ Λj, η ∈ Λk, and v · (∇Φj(ξ) − ∇Φk(η)) = 0 we have

∇2Φ(ξ)v ∧ ∇Φj(ξ) − ∇Φk(η) ∇2Φj(ξ)v · v Vmax HjVmax|v|2 we see that (A1) holds and thus result follows by an application of Theorem 1.4.

- 2.3. The Wave/Klein-Gordon case: Proof of Theorem 1.10. We only consider the case α ≪ 1, the case α ≈ 1 is easier and follows directly from Theorem 1.2 (via Lemma 2.2). Applying a rotation, we may


assume that ξ0 = (a,0,...,0), η0 = (√1 − δ2b,δb,0,...,0) with 0 < δ < 1, a m

![image 205](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile205.png>)

≈ µ, and |m2a − m1b| λµ

≈ λ, b m

2

1

- 1

![image 206](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile206.png>)

- 2


ab λµ

δ ≈ α. (2.8)

+

![image 207](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile207.png>)

![image 208](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile208.png>)

After rescaling, and perhaps decomposing u and v into slightly smaller sets if necessary, it is enough to prove that if supp f ⊂ Λ1, supp g ⊂ Λ2 we have

1 q − 12

r −q1 λ µ

![image 209](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile209.png>)

![image 210](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile210.png>)

2

n

tLrx(R1+n) α−

q µn−

feitΦ

eitΦ

(2.9) where we deﬁne the phases

g Lq

f L2

g L2

2

1

![image 211](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile211.png>)

![image 212](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile212.png>)

![image 213](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile213.png>)

![image 214](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile214.png>)

x

x

- 1

![image 215](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile215.png>)

- 2, Φ2(ξ) = ±(m22 + β2ξ12 + α2|ξ′|2)


- 1

![image 216](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile216.png>)

- 2


Φ1(ξ) = (m21 + β2ξ12 + α2|ξ′|2)

with ξ = (ξ1,ξ′) ∈ R×Rn−1, ξ′ = (ξ2,ξ′′) ∈ R×Rn−2, and take ξ0 = (a,0,...,0), η0 = (√1 − δ2b,δb,0,...,0) and the sets Λj to be

![image 217](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile217.png>)

![image 218](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile218.png>)

Λ1 = βξ1 − a ≪ βλ, |ξ′| ≪ λ , Λ2 = βξ1 ∓ 1 − δ2b ≪ βµ, |αξ2 ∓ δb| ≪ αµ, |ξ′′| ≪ µ}.

Note that (2.8) implies that if (λµab )12δ ≪ α then the sets Λj must have some radial separation, while if (λµab ) transversality condition (2.8) implies that µb δ α, this follows by observing that in the fully elliptic case, when λ ≈ m1 and µ ≈ m2, (2.8) becomes η

![image 219](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile219.png>)

![image 220](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile220.png>)

- 1

![image 221](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile221.png>)

- 2 δ α the sets are angularly separated. To simplify the computations to follow, we note that the


![image 222](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile222.png>)

![image 223](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile223.png>)

m1 − ξ

m2 ≈ α. Similarly, by the deﬁnition of β, if either λ ≈ m1 or µ ≈ m2, then we have β ≈ α.

0

0

![image 224](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile224.png>)

![image 225](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile225.png>)

To obtain the bound (2.9), we apply Theorem 1.2. Thus we have to check the conditions (A1) and (A2). There a number of ways to do this, here we argue via Lemma 2.2. To this end, we start by noting that

(β2ξ1,α2ξ′) (m2j + β2ξ12 + α2|ξ′|2)12

∇Φj =

![image 226](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile226.png>)

![image 227](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile227.png>)

and hence a computation using the deﬁnitions of β and Λj, gives the derivative bounds sup

(β√1 − δ2b,αδb,0,...,0) b m

α2 10

![image 228](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile228.png>)

(βa,0,...,0) a m

∇Φ1(ξ) −

∇Φ2(ξ) −

+ sup

≈

. (2.10)

![image 229](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile229.png>)

![image 230](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile230.png>)

![image 231](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile231.png>)

ξ∈Λ1

ξ∈Λ2

1

2

Similarly, to estimate ∇2Φj, we observe that

β2((mαj )2 + |ξ′|2) (m2j + β2ξ12 + α2|ξ′|2)32

β4ξ12 (m2j + β2ξ12 + α2|ξ′|2)32

β2 (m2j + β2ξ12 + α2|ξ′|2)12

![image 232](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile232.png>)

= α2

∂12Φj =

−

![image 233](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile233.png>)

![image 234](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile234.png>)

![image 235](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile235.png>)

![image 236](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile236.png>)

![image 237](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile237.png>)

![image 238](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile238.png>)

and for k,k′ > 1,

∂1∂kΦj = α2 −β2ξ1ξk (m2j + β2ξ1 + α2|ξ′|)23

α2ξkξk′ (m2j + β2ξ12 + α2|ξ′|2)23

δk,k′ (m2j + β2ξ12 + α2|ξ′|2)12

, ∂k∂k′Φj = α2

−

.

![image 239](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile239.png>)

![image 240](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile240.png>)

![image 241](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile241.png>)

![image 242](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile242.png>)

![image 243](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile243.png>)

![image 244](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile244.png>)

2

2

In particular, applying the deﬁnition of β, we have the Hessian bounds H1 ≈ α

λ , H2 ≈ α

µ . Thus we see that the condition (A2) holds with d0 = µ. It remains to show that (A1) holds, which will follow by checking the conditions in Lemma 2.2. To this end, the transversality condition (2.8) together with the deﬁnition of β gives

![image 245](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile245.png>)

![image 246](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile246.png>)

(β√1 − δ2b,αδb,0,...,0) b m

![image 247](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile247.png>)

(βa,0,...,0) a m

≈ α2

−

![image 248](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile248.png>)

![image 249](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile249.png>)

1

2

The estimate (2.10) then gives the transversality bound |∇Φ1(ξ) − ∇Φ2(η)| ≈ Vmax ≈ α2.

Since we clearly have the ﬁnal condition in Lemma 2.2, it only remains to show that we have the curvature condition

α2

λ |ξ − η|2 (2.11) for all ξ,η ∈ Σ1(h), together with a similar bound for ∇Φ2. This follows by adapting the argument in [4, Corollary 6.4]). We only consider the case j = 1, as the remaining case is identical. Suppose that ξ,η ∈ Σ1(h) with h = (a∗,h). Let x = (mj,βξ1,αξ′), y = (mj,βη1,αη′), and h∗ = (m2 − m1,βh1,αh′). Then the condition ξ ∈ Σ1(h) becomes |x| ± |x − h∗| = a∗. Consequently, for every ξ,η ∈ Σ1(h) we have

∇Φ1(ξ) − ∇Φ1(η) · (ξ − η)

![image 250](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile250.png>)

∇Φ1(ξ)−∇Φ1(η) · (ξ − η)

2

(m1,βη1,αη′) |(m1,βξ1,αξ′)|

(m1,βξ1,αξ′) |(m1,βξ1,αξ′)|

= |(m1,βξ1,αξ′)| + |(m1,βη1,αη′)| 2

−

![image 251](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile251.png>)

![image 252](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile252.png>)

![image 253](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile253.png>)

2

x |x|

y |y|

≈ λ

−

![image 254](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile254.png>)

![image 255](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile255.png>)

2

2

x − h∗ |x − h∗|

y − h∗ |y − h∗|

1 λ

x |x|

y |y|

λ2

+ µ2

(2.12)

−

−

≈

![image 256](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile256.png>)

![image 257](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile257.png>)

![image 258](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile258.png>)

![image 259](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile259.png>)

![image 260](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile260.png>)

where the last line follows by observing that ξ,η ∈ Σ1(h) implies that we have the identity |x||y|

2

y |y|

x |x|

= |x − y|2 − |x| − |y| 2 = (x − h∗) − (y − h∗) 2 − |x − h∗| − |y − h∗| 2

−

![image 261](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile261.png>)

![image 262](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile262.png>)

y − h∗ |y − h∗|

x − h∗ |x − h∗|

2

= |x − h∗||y − h∗|

−

.

![image 263](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile263.png>)

![image 264](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile264.png>)

If either λ ≈ m1 or µ ≈ m2, then since z,w ∈ Rn with z m ≈ w m implies we have z z m −

- 1

![image 265](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile265.png>)

- 2


2 |z| − |w| z m

+ |z||w| − z · w z 2m

m z m

x x m ≈

,

![image 266](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile266.png>)

![image 267](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile267.png>)

![image 268](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile268.png>)

![image 269](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile269.png>)

![image 270](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile270.png>)

the required bound (2.11) follows directly from (2.12) together with the fact that α ≈ β in the case λ ≈ m1 or µ ≈ m2. On the other hand, if λ ≫ m1 and µ ≫ m2, then we consider separately the cases |ξ1−η1| |ξ′−η′| and |ξ′ −η′| ≪ |ξ1 −η1|. In the former case, if α ≫ m

λ + m

µ , then from the deﬁnition of β and the condition (2.8) we must have β ≈ δ ≈ 1. Hence we deduce that as ξ − h,η − h ∈ Λ2 we have

2

1

![image 271](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile271.png>)

![image 272](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile272.png>)

|(x − h∗) ∧ (y − h∗)| α|β(ξ1 − η1)(η′ − h′) − β(η1 − h1)(η′ − ξ′)| ≈ αµ|ξ1 − η1| ≈ αµ|ξ − η|

which, together with the elementary bound |ω − ω′| |ω ∧ ω′| for ω,ω′ ∈ Sn−1 gives (2.11). On the other hand, if α m

λ + m

µ , we have again using the deﬁnition of β |x ∧ y| λ

1

2

![image 273](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile273.png>)

![image 274](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile274.png>)

+ |(x − h∗) ∧ (y − h∗)| µ

m1|ξ1 − η1| λ

m2|ξ1 − η1| µ ≈ α|ξ − η|.

+ β

β

![image 275](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile275.png>)

![image 276](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile276.png>)

![image 277](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile277.png>)

![image 278](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile278.png>)

Thus we have (2.11) when |ξ1 − η1| |ξ′ − η′|. Finally, if |ξ′ − η′| ≫ |ξ1 − η1|, then we simply observe that |x ∧ y| α βξ1(ξ′ − η′) − ξ′β(ξ1 − η1) ≈ αλ|ξ′ − η′| ≈ αλ|ξ − η|. Therefore (2.11) follows as required.

- 2.4. A Reﬁned Strichartz estimate for the Klein-Gordon equation: Proof of Theorem 1.12. The proof closely follows the argument of Ramos in [17], with the key bilinear estimate Theorem 1.10 replacing


the bilinear estimate of Tao [21] used in [17], thus we shall be somewhat brief. Let p = nn−+11 and u = eit ∇ f, and decompose

![image 279](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile279.png>)

u 2L2p

uλuℓλ

Lpt,x

t,x

ℓ∈2N λ∈2N

where u = λ∈2N uλ and supp uλ ⊂ { ξ ≈ λ}. Since the sum is essentially orthogonal as λ varies, by applying the weak orthogonality in Lp (see for instance [17, Lemma 2.2]) we have

1 min{p,p′}

′} Lpt,x

![image 280](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile280.png>)

uλuℓλ min{p,p

uλuℓλ

Lpt,x

λ∈2N

λ∈2N

where p′ = p−p1 denotes the dual exponent to p. Given A = A(ξ0) ∈ Aλ,α, and B = B(η0) ∈ Aℓλ,α, we say A ∼ B if we have the transversality type condition

![image 281](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile281.png>)

- 1

![image 282](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile282.png>)

- 2


|ξ0| − |η0| ℓλ2

+ |ξ0||η0| − ξ0 · η0 ℓλ2

≈ α. Applying a Whitney type decomposition, we can write

![image 283](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile283.png>)

![image 284](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile284.png>)

uλuℓλ =

uAuB

α∈2−N A∈Aλ,α B∈Aℓλ,α A∼B

≈ u Lr(A). An application of Theorem 1.10 gives for all nn+1+3 < q 2

≈ u Lr(A), uA Lr

where supp uA ⊂ A, and uA Lr

ξ

ξ

![image 285](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile285.png>)

1− 1q

q−12 αλ 1 + αλ

n+1

n+1

![image 286](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile286.png>)

1

λn−

αn−1−

q ℓ

q f L2

ξ(A) f L2

ξ(B). Interpolating with the trivial bound

uAuB Lq

![image 287](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile287.png>)

![image 288](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile288.png>)

![image 289](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile289.png>)

![image 290](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile290.png>)

![image 291](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile291.png>)

t,x

f L1

ξ(A) f L1

uAuB L∞

ξ(B) we deduce that for all max{21, n+12 } r 1 < 21 + (n+1)2 2 we have

t,x

![image 292](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile292.png>)

![image 293](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile293.png>)

![image 294](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile294.png>)

![image 295](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile295.png>)

![image 296](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile296.png>)

2− r2 − nn−+11

n+1+1r−1 αλ 1 + αλ

2(n−1)

n−1

![image 297](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile297.png>)

![image 298](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile298.png>)

2n

αn−1−

λn+1−

uAuB Lp

r ℓ

r f Lr

![image 299](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile299.png>)

![image 300](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile300.png>)

![image 301](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile301.png>)

![image 302](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile302.png>)

![image 303](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile303.png>)

t,x

2 n+1

n+1+n+1r −n+32 αλ 1 + αλ

n−1

![image 304](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile304.png>)

- 1

![image 305](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile305.png>)

- 2


- 1

![image 306](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile306.png>)

- 2


- 1

![image 307](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile307.png>)

- 2−1r f Lr


≈ ℓ

ξ(A)(ℓλ)

|A|

λ

![image 308](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile308.png>)

![image 309](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile309.png>)

![image 310](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile310.png>)

![image 311](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile311.png>)

![image 312](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile312.png>)

ξ(A) f Lr

ξ(B)

- 1

![image 313](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile313.png>)

- 2−r1 g Lr


ξ(B). (2.13)

|B|

![image 314](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile314.png>)

The bound (2.13) is the key bilinear input, and replaces the corresponding estimate for the wave equation [17, Corollary 2.1] used in the work of Ramos. We now apply the Whitney decomposition to deduce that

sup

sup

sup

uλuℓλ Lp

uAuB Lp

t,x

t,x

α≈1

A∈Aλ,α

B∈Aℓλ,α

+

+

(2.14)

uAuB

uAuB

Lpt,x

Lpt,x

1 λ α≪1 A∈Aλ,α B∈Aℓλ,α

α≪λ1 A∈Aλ,α B∈Aℓλ,α A∼B

![image 315](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile315.png>)

![image 316](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile316.png>)

A∼B

where the ﬁrst term follows from simply observing that for α ≈ 1 we have #Aλ,α 1. For the second and third term in (2.14), we again follow [17] and apply the weak orthogonality in Lp. More precisely, we claim that for ﬁxed ℓ and λ, the sets

{( ξ + η ,ξ + η) |ξ ∈ A, η ∈ B } ⊂ R1+n.

for A ∈ Aλ,α, B ∈ Aℓλ,α with A ∼ B, are essentially disjoint as α and A vary. This follows by observing that if A = A(ξ0) ∈ Aλ,α and B = B(η0) ∈ Aℓλ,α with A ∼ B, then we have for every ξ ∈ A and η ∈ B

αλ 1 + αλ

- 1

![image 317](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile317.png>)

- 2


| ξ + η 2− ξ − η | ≈ λα2, |ξ+η|−|ξ0+η0|

ℓλ, (|ξ+η||ξ0+η0|−(ξ+η)·(ξ0+η0)

αℓλ.

![image 318](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile318.png>)

In particular, for the second term in (2.14), as this sum only covers the wave like regime where the sets A are simply angular sectors of the annuli, we can bound this contribution by using (2.13) together with the weak orthogonality and delicate summation arguments used in [17]. Note that these arguments only use the fact that we are summing up over angular sectors of the annuli, in particular, after using (2.13), the diﬀerence between the wave and Klein-Gordon equation no longer plays any role.

On the other hand, for the third term in (2.14), which comprises the main Klein-Gordon type contribution, we start by observing that due to the restriction A ∼ B, this contribution is only non-vanishing if ℓ ≈ 1. An application of [17, Lemma 2.2], together with the ﬁnite overlap observation made above and (2.13) then gives

1 min{p,p′}

min{p,p′}

![image 319](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile319.png>)

uAuB

Lpt,x

λ α≪ λ1 A∈Aλ,α B∈Aℓλ,α A∼B

![image 320](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile320.png>)

′} Lpt,x

uAuB min{p,p

λ α≪λ1 A∈Aλ,α B∈Aℓλ,α A∼B

![image 321](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile321.png>)

1 min{p,p′}

![image 322](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile322.png>)

2

- 1

![image 323](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile323.png>)

- 2


- 1

![image 324](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile324.png>)

- 2−r1 f Lr


- 1

![image 325](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile325.png>)

- 2


(αλ)

|A|

|B|

n+1λ

ξ(A)λ

![image 326](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile326.png>)

![image 327](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile327.png>)

λ α≪λ1 A∈Aλ,α B∈Aℓλ,α A∼B

![image 328](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile328.png>)

1 n+1

![image 329](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile329.png>)

- 1

![image 330](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile330.png>)

- 2

|A|

- 1

![image 331](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile331.png>)

- 2−1r f Lr


![image 332](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile332.png>)

ξ(A)

2 min{p,p′}−1

![image 333](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile333.png>)

min{p,p′} f

2 min{p,p′} H 21

![image 334](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile334.png>)

![image 335](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile335.png>)

.

- 3. Optimality of Theorem 1.2


αλ 1+αλ

sup

sup

λ

![image 336](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile336.png>)

A∈Aλ,α

λ,α

- 1

![image 337](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile337.png>)

- 2−r1 f Lr


![image 338](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile338.png>)

ξ(B)

min{p,p′}

1 min{p,p′}

![image 339](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile339.png>)

In this section, our goal is to show that the conclusion of Theorem 1.2 is sharp. We ﬁrst observe that, by exploiting the dilation and translation invariance of LqtLrx, is enough to consider the case

1  ∇Φ1 L∞ +  ∇Φ2 L∞ 3, Vmax = 1, H2 H1 = 1. (3.1) More precisely, since

Vmax inf

 ∇Φ1 − ξ0 L∞(Λ1) +  ∇Φ2 − ξ0 L∞(Λ2) 3Vmax

ξ0∈Rn

after a linear translation of the phases (this corresponds to the spatial translation x  → x + tξ0) we may assume that

Vmax  ∇Φ1 L∞(Λ1) +  ∇Φ2 L∞(Λ2) 3Vmax. To obtain the claimed bounds in (3.1), we now apply the rescaling

Φj Vmax H1

H1 Vmax

H1 Vmax2

d0.

ξ , d0  →

Φj(ξ)  →

![image 340](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile340.png>)

![image 341](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile341.png>)

![image 342](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile342.png>)

It is important to note that this rescaling and translation leaves the assumptions (A1) and (A2), and the bilinear estimate in Theorem 1.2, unchanged.

Fix ξ0 ∈ Λ1, η0 ∈ Λ2, and 0 < ǫ ≪ 1. It is enough to construct Φ1-wave u, and a Φ2-wave v, such that supp u ⊂ {|ξ − ξ0| ǫ}, supp v ⊂ {|ξ − η0| ǫ}, we have the energy bounds

- 1

![image 343](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile343.png>)

- 2


t L2x H−

n+1

n+1

2 ǫ−

t L2x ǫ−

u L∞

2 , and both u and v are concentrated on the ǫ−1 thickened space-time rectangle

2 , v L∞

![image 344](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile344.png>)

![image 345](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile345.png>)

Ω = s 1,−∇Φ1(ξ0) + s′ 1,−∇Φ2(η0) 0 s ǫ−2, 0 s′ (ǫ2H2)−1 + ǫ−1

in the sense that uv Lq

tLrx. Assuming the existence of u and v for the moment, we easily deduce that the estimate

tLrx(Ω) ≈ 1Ω Lq

tLrx C u L∞

uv Lq

t L2x v L∞

t L2x

together with the transversality assumption (1.5) implies that C ǫn+1−

- 1

![image 346](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile346.png>)

- 2− 1q 2 .


n+1

r −q2 H

![image 347](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile347.png>)

![image 348](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile348.png>)

![image 349](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile349.png>)

Thus we see that d0 ǫ, we have the correct dependence on Hj, and letting ǫ → 0, we must have 1q + n2+1r n+1

![image 350](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile350.png>)

![image 351](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile351.png>)

2 .

![image 352](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile352.png>)

It remains to construct u and v satisfying the required properties. One approach is to adapt the example used by Tao in [21]. Let ρ be a Schwartz function such that ρ(x) ≈ 1 for |x| 1, and supp ρ ⊂ {|ξ| 1}, and deﬁne

2(η0))·ξ0ρ ǫx + ǫNk∇Φ2(η0) , ρ2,k = ei(x+Nk∇Φ

1(ξ0))·η0ρ ǫx + ǫNk∇Φ1(ξ0)

ρ1,k(x) = ei(x+Nk∇Φ

where N is some ﬁxed quantity independent of ǫ, which is needed to create some separation between the resulting wave packets. The waves u and v are then deﬁned as

ei(t−Nk)Φ

1(−i∇)ρ1,k(x), v(t,x) =

eitΦ

2(−i∇)ρ2,k(x).

u(t,x) =

0 k (ǫ2H2)−1

0 k ǫ−2

It is clear that u and v satisfy the required Fourier support properties by the deﬁnition of ρ. Roughly speaking, v is deﬁned as the sum of wave packets concentrated on (space-time) tubes of size (ǫ2H2)−1 × ǫ−n which are oriented in the direction (1,−∇Φ2(η0)) and centered along the points (0,−kN∇Φ1(ξ0)), and essentially cover the set Ω. Similarly, u is the sum of wave packets concentrated on tubes of size ǫ−2 × ǫ−n oriented in the direction (1,−∇Φ1(ξ0)) and centered along the (space-time) points (kN,−kN∇Φ2(η0)), which again essentially covers the set Ω. In particular, we expect that the product |uv| is essentially concentrated on Ω. These heuristics can be made rigorous by a somewhat standard integration by parts argument (and potentially choosing N large enough to absorb any absolute constants which arise), see for instance Section 6 for similar arguments. On the other hand, the claimed L2x bounds follow by noting that as the wave packets are essentially disjoint for ﬁxed times, we have

t L2x ≈

v L∞

0 k ǫ−2

ρ2,k 2L2

x

- 1

![image 353](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile353.png>)

- 2


n+1

≈ ǫ−

2 .

![image 354](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile354.png>)

The argument to bound u L∞

t L2x is slightly more involved as the wave packets are not centered on a ﬁxed time slice t = 0, but instead centred along a tube oriented in the direction (1,−∇Φ2(η0)). In general, wave packets centered along space-time lines need not be orthogonal, however, since the wave packets making up u are transverse to the direction (1,−∇Φ2(η0)), we retain orthogonality of the wave packets. This can be seen by an application of Plancheral which gives

ˆ

′)[ξ·∇Φ2(η0)−ǫ−1Φ1(ǫξ−ξ0)]|ρ(ξ)|2dξ ǫ−n

1 ≈ H2−1ǫ−n−1

u(t) 2L2

= ǫ−n

eiN(k−k

x

Rn

0 k,k′ (ǫ2H2)−1

0 k (ǫ2H2)−1

where we used integration by parts together with (1.5) to control the oﬀ diagonal terms. It is worth observing that the above argument already foreshadows a number of the ingredients in the proof of Theorem 1.2, namely the orthogonality properties of wave packets together with energy type estimates across transverse surfaces.

4. Induction on Scales

In this section we reduce the proof of Theorem 1.4 to proving local estimates on cubes Q ∈ R1+n. This follows the argument of Tao [21] which was adapted by Bejenaru [1] and Lee-Vargas [13], but we reﬁne the induction somewhat to remove the epsilon derivative loss that appears in the previous bounds of Tao and Lee-Vargas.

Fix constants d0,C0 > 0, and open sets Λj ⊂ Rn. Let Φ1 and Φ2 be phases satisfying (A1) and (A2).

After exploiting the dilation and translation invariance of LqtLrx as in Section 3, it is enough to consider the case

1  ∇Φ1 L∞ +  ∇Φ2 L∞ 3, Vmax = 1, H2 H1 = 1. (4.1) Take sets Λ∗j + d0 ⊂ Λj such that d[Λ∗1 + d0,Λ∗2 + d0] d

C0, and ﬁx R0 ≫ d201H2 with d Λ∗1 + d0,Λ∗2 + d0 H2R0 −

0

![image 355](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile355.png>)

![image 356](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile356.png>)

- 1

![image 357](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile357.png>)

- 2


d Λ∗1 + d0,Λ∗2 + d0 .

The constant R0 will denote the smallest scale of cubes we consider, while the sets Λ∗j will contain the supports of u and v. The proof of Theorem 1.4 is based on an induction on scales argument. This requires the following deﬁnition.

Deﬁnition 4.1. For any R R0 and 1 q,r 2, we deﬁne Aq,r(R) to the best constant for which the inequality

tLrx(Q) Aq,r(R) u L∞

uv Lq

t L2x v L∞

t L2x holds for all cubes Q ⊂ R1+n of radius R, and all Φ1-waves u and Φ2-waves v satisfying the support assumption

- 1

![image 358](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile358.png>)

- 2, supp v ⊂ Λ∗2 + 4(H2R)−


- 1

![image 359](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile359.png>)

- 2 .


supp u ⊂ Λ∗1 + 4(H2R)−

It is easy to check that Aq,r(R) is always ﬁnite, and, since R R0 ≫ (d20H2)−1, that the required support conditions on v and v imply that we always have

d0 2 ⊂ Λ2.

d0 2 ⊂ Λ1, supp v +

supp u +

![image 360](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile360.png>)

![image 361](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile361.png>)

It is also worth noting that the support condition becomes stricter as R becomes large, in other words, for large R, the Fourier supports must be smaller. Roughly this can be explained as follows. Our goal will be to obtain a bound for Aq,r(2R), in terms of Aq,r(R). At each scale 2R, we will need to decompose u and v into wave packets, this will enlarge the Fourier support slightly, and thus to apply the bound at scale R to the wave packets of u and v, we will need Aq,r(R) to apply to functions with slightly larger support. The support conditions we use play the same role as the margin type conditions used in [21].

The proof of Theorem 1.4 will rely on two key propositions. The ﬁrst gives a good bound for Aq,r(R) for R close to R0, and is needed to begin the induction argument.

- Proposition 4.2. Let C0 > 0, 1 q,r 2, and q1 + n2+1r < n+12 . Assume we have d0 > 0, open sets Λj ⊂ Rn, and phases Φj satisfying Assumption 1.1 with the normalisation conditions (4.1). Then for any

![image 362](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile362.png>)

![image 363](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile363.png>)

![image 364](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile364.png>)

sets Λ∗j + d0 ⊂ Λj with d[Λ∗1 + d0,Λ∗2 + d0] d

0

![image 365](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile365.png>)

C0 , and every R R0 we have Aq,r(R) dn+1−

n+1

![image 366](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile366.png>)

r − 2q

![image 367](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile367.png>)

0 H

- 1 2 − q1

![image 368](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile368.png>)

![image 369](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile369.png>)

- 2


R R0

![image 370](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile370.png>)

1 q

![image 371](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile371.png>)

.

The second implies that we can control Aq,r(2R) in terms of Aq,r(R).

- Proposition 4.3. Let C0 > 0, 1 q,r 2, and q1 + n2+1r < n+12 . There exists a constant C > 0, such that for any d0 > 0, any open sets Λj ⊂ Rn, any phases Φj satisfying Assumption 1.1 with the normalisation


![image 372](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile372.png>)

![image 373](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile373.png>)

![image 374](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile374.png>)

(4.1), and any sets Λ∗j + d0 ⊂ Λj with d[Λ∗1 + d0,Λ∗2 + d0] d

C0, we have for every R R0 and 0 < ǫ ≪ 1 Aq,r(2R) (1 + Cǫ)Aq,r(R) + ǫ−CH

0

![image 375](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile375.png>)

n+1

2r −n2

q+n2+1r −n+12 .

1

![image 376](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile376.png>)

![image 377](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile377.png>)

2 R

![image 378](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile378.png>)

![image 379](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile379.png>)

![image 380](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile380.png>)

We leave the proof of Propositions 4.2 and 4.3 till Section 5, and now turn to the proof of Theorem 1.4. Proof of Theorem 1.4. We begin by observing that an application of Proposition 4.3 with R = 2mR0 and ǫ = C1 2

2C(q1+n2+1r −n+12 ) implies that Aq,r 2mR0 (1 + 2

m

![image 381](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile381.png>)

![image 382](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile382.png>)

![image 383](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile383.png>)

![image 384](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile384.png>)

![image 385](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile385.png>)

1 q + n2+1r − n+12

n+1

2r − n2

4C(q1+n2+1r −n+12 ))Aq,r 2m−1R0 + CCH

2 (q1+n2+1r −n+12 ).

m

m

![image 386](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile386.png>)

![image 387](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile387.png>)

![image 388](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile388.png>)

![image 389](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile389.png>)

![image 390](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile390.png>)

0 2

2 R

![image 391](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile391.png>)

![image 392](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile392.png>)

![image 393](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile393.png>)

![image 394](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile394.png>)

![image 395](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile395.png>)

![image 396](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile396.png>)

![image 397](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile397.png>)

![image 398](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile398.png>)

Since 1q + n2+1r < n+12 both error terms decay in m. In particular, after m applications of Proposition 4.3 we have1

![image 399](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile399.png>)

![image 400](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile400.png>)

![image 401](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile401.png>)

1 q + n2+1r − n+12

n+1

2r − n2

Aq,r 2mR0 Aq,r(R0) + H

![image 402](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile402.png>)

![image 403](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile403.png>)

![image 404](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile404.png>)

![image 405](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile405.png>)

![image 406](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile406.png>)

2 R

0 where the implied constant depends only on q, r, the dimension n, and C0. Applying Proposition 4.2 and using the deﬁnition of R0, we conclude that for every m ∈ N

n+1

- 1

![image 407](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile407.png>)

- 2− 1q 2 .


r − 2q

Aq,r 2mR0 dn+1−

![image 408](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile408.png>)

![image 409](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile409.png>)

![image 410](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile410.png>)

0 H Unpacking the deﬁnition of Aq,r 2mR0 , and letting m → ∞ we obtain Theorem 1.4.

5. The localisation argument

In this section we reduce the proof of Propositions 4.2 and 4.3 to obtaining a decomposition of the Φjwaves, into waves which are concentrated at smaller scales, in the sense that the LqtLrx norm on a cube of diameter R, can be controlled by the same norm at the smaller scale R2 . This decomposition requires a variant of the wave table construction introduced by Tao in [21]. Recall that, given a collection of functions (u(B))B∈Q

![image 411](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile411.png>)

r(Q) (or a wave table in the notation of Tao), we deﬁned the corresponding quilt [u(·)] to be the sum

1B|u(B)|.

[u(·)] =

B∈Qr(Q)

r(Q) u(B) into waves which are “concentrated” in B. The portion of u(B) away from the cube B has additional decay, and can be treated as an error term. On the other hand, the quilt [u(·)] contains the part of u which is concentrated on B, and does not decay in R. However it is concentrated at a smaller scale than u, and this allows us to exploit the induction assumption.

Roughly speaking, we decompose u = B∈Q

The key bound, and the part of Theorem 1.4 which requires the most work, is the following theorem.

- Theorem 5.1. Let C0 > 0, 1 q,r 2, and q1 + n2+1r < n+12 . Assume that we have d0 > 0, open sets Λj ⊂ Rn, and phases Φj satisfying (A1), (A2), and the normalisation (4.1). Let QR be a cube of diameter R R0. Then for any 0 < ǫ ≪ 1, any Φ1-wave u, and any Φ2-wave v with


![image 412](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile412.png>)

![image 413](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile413.png>)

![image 414](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile414.png>)

d0

d0 2 ⊂ Λ1, supp v +

2 ⊂ Λ2 there exist a cube Q of diameter 2R such that we have a decomposition

supp u +

![image 415](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile415.png>)

![image 416](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile416.png>)

′)

v(B

u(B), v =

u =

B′∈QR 2

B∈Q 2R 4M

(Q)

(Q)

![image 417](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile417.png>)

![image 418](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile418.png>)

′) is a Φ2-wave, with the support properties supp u(B) ⊂ supp u + 2 2H2R −

where M ∈ N with 4−M < H2 41−M, and u(B) is a Φ1-wave, v(B

- 1

![image 419](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile419.png>)

- 2


- 1

![image 420](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile420.png>)

- 2


′) ⊂ supp v + 2 2H2R −

, supp v(B

. Moreover we have the energy bounds

- 1

![image 421](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile421.png>)

- 2


u(B) 2L∞

(1 + Cǫ) u L∞

t L2x

t L2x

(Q)

B∈Q 2R 4M

![image 422](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile422.png>)

- 1

![image 423](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile423.png>)

- 2


′) 2 L∞t L2x

v(B

(1 + Cǫ) v L∞

t L2x

B′∈QR 2

(Q)

![image 424](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile424.png>)

and bilinear estimate uv Lq

n+1

2r − n2

q+n2+1r −n+12 u L∞

1

tLrx(QR) (1 + Cǫ) u(·) v(·) Lq

tLrx(Q) + ǫ−CH

![image 425](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile425.png>)

![image 426](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile426.png>)

t L2x v L∞

2 R

![image 427](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile427.png>)

![image 428](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile428.png>)

![image 429](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile429.png>)

t L2x

![image 430](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile430.png>)

1This exploits the bound

(1 + C2−Cα m) × (1 + C2−Cα (m−1)) × · · · × (1 + C) 1 which follows by taking logs, and recalling the elementary estimate log(1 + x) x.

![image 431](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile431.png>)

![image 432](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile432.png>)

where the constant C depends only on C0, q, r, and n.

The proof of Theorem 5.1 will take up a large part of the remaining sections to follow, and is left to Section 10.

The proof of the initial induction bound, also requires the following somewhat classical bilinear L2t,x estimate.

- Theorem 5.2. Let j ∈ {1,2}, Λj ⊂ Rn, and assume that the phases Φj ∈ C1(Λj) satisfy the transversality condition (1.5) for some C0 > 0. If u is a Φ1-wave, and v is a Φ2-wave we have


n−1 2

- 1

![image 433](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile433.png>)

- 2


t,x(R1+n) C0Vmax −

![image 434](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile434.png>)

d[supp u,supp v]

uv L2

u L∞

t L2x v L∞

t L2x. Proof. A computation gives the identities

f(η) g(ξ − η) |∇Φ1(η) − ∇Φ2(ξ − η)|

(uv)(τ,ξ) = ˆ

dσ(η)

![image 435](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile435.png>)

Σ1(τ,ξ)

and

| f(η) g(ξ − η)|2 |∇Φ1(η) − ∇Φ2(ξ − η)|

ˆ

ˆ

dσ(η)dτ = f(η) g(ξ − η) 2L

![image 436](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile436.png>)

2 η(Rn)

Σ1(τ,ξ)

R

where dσ(η) denotes the surface measure2 on Σ1(τ,ξ). Consequently bound follows by an application of Ho¨lder’s inequality and the transversality condition (1.5).

The proof of the Propositions 4.2 and 4.3 is now a consequence of Theorems 5.1 and 5.2.

- Proof of Proposition 4.2. By deﬁnition of Aq,r(R) and R0, it is enough to prove that for every cube Q of diameter R R0 and any Φ1-wave u, and Φ2-wave v satisfying the support conditions


d0 2 we have

d0 2

, supp v ⊂ Λ∗2 +

supp u ⊂ Λ∗1 +

![image 437](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile437.png>)

![image 438](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile438.png>)

n+1

1 r )

- 1 r − 12

![image 439](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile439.png>)

![image 440](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile440.png>)

- 2 R


2r − n2

q+n2+1r −n+12 u L∞

tLrx(Q) d(n−1)(1−

q+r1−1 + H

1

1

![image 441](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile441.png>)

![image 442](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile442.png>)

![image 443](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile443.png>)

t L2x. (5.1) An application of Theorem 5.1 gives

0 H

uv Lq

t L2x v L∞

2 R

![image 444](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile444.png>)

![image 445](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile445.png>)

![image 446](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile446.png>)

![image 447](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile447.png>)

![image 448](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile448.png>)

n+1

2r − n2

q+n2+1r −n+12 u L∞

1

tLrx(Q) [u(·)][v(·)] Lq

![image 449](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile449.png>)

![image 450](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile450.png>)

tLrx(Q′) + CH

uv Lq

t L2x v L∞

2 R

![image 451](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile451.png>)

![image 452](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile452.png>)

![image 453](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile453.png>)

t L2x

where Q′ is a cube of diameter 2R. To control the quilt term, we ﬁrst observe that Theorem 5.2 together with the energy estimate for u(B) and v(B) implies the L2 bound

′) 2 L2t,x

[u(·)][v(·)] 2L

u(B)v(B

2 t,x(Q′)

(Q′) B′∈Q R 2

(Q′)

B∈QH2R

![image 454](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile454.png>)

![image 455](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile455.png>)

2

d0n−1 u 2L∞

t L2x v 2L∞

t L2x where we used the Fourier support conditions on u(B) and v(B

′) to deduce that d supp u(B),supp v(B

′) d Λ∗1 + d0,Λ∗2 + d0 d0.

![image 456](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile456.png>)

2 Explicitly, in the region |∂1Φ1 − ∂1Φ2| ≈ |∇Φ1 − ∇Φ2|, there exists a function ψ(τ, ξ, η′) : R × Rn × Rn−1 → R such that

Φ1 ξ − (ψ, η′) + Φ2(ψ, η′) = τ. Thus we can write the surface as a graph Σ2(h) = {(ψ(η′), η′) ∈ (h − Λ1) ∩ Λ2}, and hence the surface measure is then dσ(η) = 1 + |∇η′ψ|2dη′ = ||∇∂ Φ1−∇Φ2|

![image 457](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile457.png>)

1Φ1−∂1Φ2|dη′.

![image 458](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile458.png>)

On the other hand, simply applying Ho¨lder’s inequality gives [u(·)][v(·)] L

t,x(Q′) [v(·)] L

tL1x(Q′) [u(·)] L

∞ t L2x(Q′)

2

2

1 2

- 1

![image 459](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile459.png>)

- 2


′) 2 L∞t L2x

![image 460](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile460.png>)

- 1

![image 461](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile461.png>)

- 2 u(B) 2L∞


v(B

(RH2)

t L2x

- 1

![image 462](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile462.png>)

- 2 u L∞


(RH2)

t L2x v L∞

t L2x. Applying Holder in the t variable, and interpolating between the L2tL1x and L2t,x bounds, then gives

1 r )

- 1 r − 12

![image 463](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile463.png>)

![image 464](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile464.png>)

- 2 R


tLrx(Q′) d(n−1)(1−

q−12 [u(·)][v(·)] L

q+1r−1 u L∞

1

1

[u(·)][v(·)] Lq

![image 465](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile465.png>)

0 H

t L2x v L∞

t L2x. Therefore (5.1) follows.

tLrx(Q′) R

![image 466](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile466.png>)

![image 467](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile467.png>)

![image 468](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile468.png>)

![image 469](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile469.png>)

2

A similar application of Theorem 5.1 gives Proposition 4.3.

- Proof of Proposition 4.3. Let R ≫ (d20H2)−1. Let u be a Φ1-wave and v be a Φ2-wave with the support condition


- 1

![image 470](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile470.png>)

- 2, supp v ⊂ Λ∗2 + 4(H22R)−


- 1

![image 471](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile471.png>)

- 2.


supp u ⊂ Λ∗1 + 4(H22R)− It is enough to consider the normalised case u L∞ t L2x = v L∞

t L2x = 1. Our goal is to show that for every cube Q of diameter 2R we have

n+1

2r − n2

q+n2+1r −n+12 . (5.2) An application of Theorem 5.1 gives a cube Q′ of diameter 4R, and wave tables (u(B))B∈Q

1

tLrx(Q) (1 + Cǫ)Aq,r(R) + ǫ−CH

![image 472](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile472.png>)

![image 473](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile473.png>)

2 R

uv Lq

![image 474](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile474.png>)

![image 475](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile475.png>)

![image 476](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile476.png>)

′))B′∈QR(Q′) such that

H2R(Q′), (v(B

n+1

2r − n2

1 q + n2+1r − n+12

tLrx(Q) (1 + Cǫ) [u(·)][v(·)] Lq

tLrx(Q′) + ǫ−CH

![image 477](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile477.png>)

![image 478](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile478.png>)

2 R

uv Lq

![image 479](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile479.png>)

![image 480](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile480.png>)

![image 481](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile481.png>)

and the support properties supp u(B) ⊂ Λ∗1 + 4(H2R)−

′) ⊂ Λ∗2 + 4(H2R)−

- 1

![image 482](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile482.png>)

- 2, supp v(B


- 1

![image 483](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile483.png>)

- 2 (5.3)


where we used the support assumptions on u and v. Let B′ ∈ QR(Q′) and deﬁne the vector valued Φ1-wave U(B

′) is a Φ1-wave (since u(B) are maps into ℓ2c(Z), after relabeling, U(B

′) = (u(B))B∈Q

H2R(B′). It is easy to check that U(B

′) and a Φ2-wave v(B

′) is also a map into ℓ2c(Z)). In particular, for every B′ ∈ QR(Q′) we have a Φ1-wave U(B

′) satisfying the correct support assumptions to apply the deﬁnition of Aq,r(R). Hence, if we observe that

1B|u(B)|

[u(·)] =

B′∈QR(Q′) B∈QH2R(B′)

- 1

![image 484](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile484.png>)

- 2


′)|

|u(B)|2

1B′|U(B

=

1B′

B∈QH2R(B′)

B′∈QR(Q′)

B′∈QR(Q′)

then, applying the deﬁnition of Aq,r(R), we deduce that [u(·)][v(·)] Lq

′)v(B

′)

U(B

LqtLrx(B′)

tLrx(Q′)

B′∈QR(Q′)

- 1

![image 485](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile485.png>)

- 2


′) 2 L∞t L2x

′) 2 L∞t L2x

U(B

v(B

Aq,r(R)

B′∈QR(Q′)

B′∈QR(Q′)

Aq,r(R)(1 + Cǫ)2 where the last line follows by using the energy inequalities in Theorem 5.1.

- 1

![image 486](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile486.png>)

- 2


- Remark 5.3. Note that proof of Proposition 4.3 exploited the fact that the deﬁnition of Aq,r(R) applies to vector valued waves. In fact, this is essentially the only step in the proof of Theorem 1.4 in which the freedom to use vector valued waves is crucial.


We have now reduce the problem of proving Theorem 1.4 to obtaining the decomposition contained in Theorem 5.1. The proof of Theorem 5.1 requires the full range of tools used to prove bilinear restriction estimates, namely a sharp wave packet decomposition, the wave table construction due to Tao, geometric information on the conic surfaces Cj(h), and energy estimates across transverse surfaces (which can be thought of as a replacement for the combinatorial Kakeya type inequalities used in the original argument of Wolﬀ).

6. Wave Packets

The standard approach to constructing wave packets is to localise on both the spatial and Fourier side, up to the scale given by the uncertainty principle. However, as we need to carefully control the constants in the energy estimates, we use a more reﬁned construction originally due to Tao [21] and extended to the case of general phases by Bejenaru [1]. Let ν ∈ S(Rn) be a positive smooth function, such that supp ν ⊂ {|ξ| 1}, and for all x ∈ Rn

ν(x − k) = 1.

k∈Zn

Let A = {ξ = (ξ1,...,ξn) ∈ Rn | |ξj| 2 1,j = 1,...,n} denote the unit cube centered at the origin, and deﬁne

![image 487](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile487.png>)

1A(ξ − z)dz where we take

ρ(ξ) =

|z|<1

Ω = |Ω1|

Q. To a phase space point γ = (x0,ξ0) ∈ Xr,ǫ and f ∈ L2x(Rn), deﬁne the phase-space localisation operator

´

ﬄ

![image 488](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile488.png>)

ǫ2 r

Lγf (x) = ν

(x − x0) ρ r(−i∇ − ξ0) f (x). (6.1) We have the following basic properties.

![image 489](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile489.png>)

- Lemma 6.1 (Properties of Lγ [21, Lemma 15.2], [1, Lemma 4.1]). Let r > 0, 0 < ǫ 1, and f ∈ L2(Rn). Then


1 r

Lγf = f, supp Lγf ⊂ |ξ − ξ(γ)| n+1r supp f +

.

![image 490](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile490.png>)

![image 491](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile491.png>)

γ∈Xr,ǫ

Moreover, if (mk,γ)k,γ is a positive sequence with supγ k mk,γ 1, then

1 2

2

![image 492](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile492.png>)

(1 + Cǫ) f L2

mk,γLγf

L2x

k γ∈Xr,ǫ

where the constant C depends only on the dimension n. Proof. As in [1], we adapt the method of Tao [21]. However, as we use a slightly more direct argument, we include the details. Clearly, by construction we have

Lγf = cn ˆ

1A r(ξ − ξ0) − z dz f(ξ)eiξ·xdξ = f.

Rn |z|< 21

ξ0∈r1 Zn

γ∈Xr,ǫ

![image 493](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile493.png>)

![image 494](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile494.png>)

√n 2 }, we have supp Lγf ⊂ ǫ

2

![image 495](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile495.png>)

On the other hand, since supp ν ⊂ {|ξ| 1} and supp ρ ⊂ {|ξ| 2+

r + supp f ∩

![image 496](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile496.png>)

![image 497](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile497.png>)

{|ξ − ξ0| nr }. It remains to prove the more delicate energy type estimate. To simplify the notation somewhat, we take

![image 498](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile498.png>)

ǫ2 r

0,z = 1A(r(ξ − ξ0) − z) f, PA(ξ∗0,z)g(ξ) = 1A∗(r(ξ − ξ0) − z) g(ξ) where

(x − x0)), fξ

= ν(

νx

![image 499](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile499.png>)

0

A∗ = {ξ = (ξ1,...,ξn) ∈ Rn | |ξj| 2 1 − 2ǫ2,j = 1,...,n}.

![image 500](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile500.png>)

Applying Minkowski’s inequality and decomposing f(ξ

0,z) gives

- 1

![image 501](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile501.png>)

- 2


- 1

![image 502](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile502.png>)

- 2


2

2

dz (6.2)

fξ

mk,(x

0,ξ0)νx

mk,γLγf

0,z

0

L2x

L2x

|z|<1 k x0 ξ0

k γ

1 2

2

![image 503](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile503.png>)

PA(ξ∗0,z)fξ

mk,(x

0,ξ0)νx

dz

0,z

0

L2x

|z|<1 k x0 ξ0

- 1

![image 504](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile504.png>)

- 2


2

- 0
- 1 − PA(ξ∗0,z) fξ


+

mk,(x

0,ξ0)νx

dz.

0,z

L2x

|z|<1 k x0 ξ0

PA(ξ∗0,z)fξ

A computation shows that the Fourier supports of the functions νx

0,z are disjoint as ξ0 varies. Consequently we have the identity

0

- 1

![image 505](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile505.png>)

- 2


1 2

2

2

![image 506](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile506.png>)

PA(ξ∗0,z)fξ

PA(ξ∗0,z)fξ

=

.

mk,(x

0,ξ0)νx

mk,(x

0,ξ0)νx

0,z

0,z

0

0

L2x

L2x

k ξ0 x0

k x0 ξ0

and mk,(x

0,ξ0) are positive, we have

As νx

0

2

2

PA(ξ∗0,z)fξ

|PA(ξ∗0,z)fξ

|PA(ξ∗0,z)fξ

0,z| and therefore

0,z|

mk,(x

0,ξ0)νx

mk,(x

νx

0,z

0,ξ0)

0

0

k x0

x0

k

1 2

2

![image 507](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile507.png>)

PA(ξ∗0,z)fξ

dz f L2.

mk,(x

0,ξ0)νx

0,z

0

L2x

|z|<1 k x0 ξ0

It remains to estimate the second term in (6.2). Repeating the above argument, but applying almost orthogonality instead of orthogonality, we see that

- 1

![image 508](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile508.png>)

- 2


- 1

![image 509](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile509.png>)

- 2


2

2

1 − PA(ξ∗0,z) fξ

- 0
- 1 − PA(ξ∗0,z) fξ


dz Cn

dz.

mk,(x

0,ξ0)νx

0,z

0,z

L2x

L2x

|z|<1 ξ0

|z|<1 k x0 ξ0

An application of Holder’s inequality in the dz integral, together with Plancheral reduces the problem to proving that

1 − 1A∗ r(ξ − ξ0) − z 1A r(ξ − ξ0) − z dz Cnǫ. But this follows from a short computation. Thus lemma follows.

ξ0 |z| 1

We can now deﬁne the wave packets we use in the proof of Theorem 1.4. As is more or less standard, see for instance [1, 4], to deﬁne the wave packet associated to a phase space point γ ∈ Γj, we conjugate the phase-space localisation operator Lγ with the ﬂow eitΦ

j(−i∇). More precisely: Deﬁnition 6.2 (Wave Packets). Let j = 1,2, and rj ≫ d−0 1. If u ∈ L∞t L2x and γj ∈ Γj, we deﬁne Pγj

j(−i∇)u(t) . Lemma 6.1 has an immediate extension to the wave packets Pγj

e−itΦ

u (t) = eitΦ

j(−i∇)Lγ

j

.

- Lemma 6.3 (Orthogonality Properties of Wave Packets). Let j = 1,2, 0 < ǫ 1, and rj ≫ d−0 1. Let


u ∈ L∞t L2x with supp u(t) + d

2 ⊂ Λj. Then u =

0

![image 510](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile510.png>)

u(t) ⊂ {|ξ − ξ(γj)| nr+1

} supp u + r1

Pju, supp Pγj

.

![image 511](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile511.png>)

![image 512](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile512.png>)

j

j

γj∈Γj

1, then

is a positive sequence with supγ

)k,γ

Moreover, if (mk,γ

j∈Γj k mk,γ

j

j

j

- 1

![image 513](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile513.png>)

- 2


2

(1 + Cǫ) u L∞

u(t)

jPγj

t L2x (6.3)

mk,γ

L2x

L∞t

k γj∈Γj

where the constant C depends only on the dimension n. Proof. If we observe that the Fourier multiplier eitΦ

j(−i∇) is unitary on L2x, and clearly leaves the Fourier support invariant, then all the required properties follow from Lemma 6.1 together with the identity

u =

Pju =

Pju

γj∈Xrj,ǫ

γj∈Γj

which is a consequence of the deﬁnition of Γj and the support assumption on u. More reﬁned properties of the wave packets Pγj

u are possible if we make further assumptions on u. In particular, if u = eitΦ(−i∇)f is a free solution, then the associated wave packets are concentrated on the tubes Tγ

. One possible formulation of this statement, which will prove extremly useful in practise, gives a bound in terms of the Hardy-Littlewood maximal function

j

1 sn

ˆ

M[f](x) = sup

|f(y)|dy.

![image 514](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile514.png>)

s>0

|x−y|<s

- Lemma 6.4 (Concentration of wave packets I). Let N 2, 0 < ǫ 1, and j ∈ {1,2}. Assume that the phase Φj ∈ CN(Λj) satisﬁes for every 2 m N the bound


 ∇mΦj L∞(Λj) d20−mHj. Let rj ≫ d−0 1, γj = (x0,ξ0) ∈ Γj, and let u = eitΦ

j(−i∇)f be a Φj-wave. Then for all (t,x) ∈ R1+n we have

−N

1 + |t| R

u(t,x)| ǫ−2(N+n) 1 + |x − x0 + t∇Φj(ξ0)| rj

N

(x0) (6.4)

M fξ

|Pγj

![image 515](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile515.png>)

![image 516](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile516.png>)

0

= ρ(rj(−i∇ − ξ0))f, and the implied constant depends only on n and N (in particular it is independent of the phase Φj and d0). Proof. We start by writing

where fξ

0

u(t,x) = ˆ

Pγj

Rn

= ˆ

Rn

f)(ξ)eitΦ

j(ξ)eix·ξdξ

(Lγ

j

f)(y)dy

(t,x − y)(Lγ

Kξ

0

j

j(ξ)eix·ξdξ and ζ ∈ C0∞(|ξ| < 2) is a cutoﬀ satisfying ζ(ξ)ρ(ξ) = ρ(ξ). The spatial localisation properties of Lγ

Rn ζ rj(ξ − ξ0) eitΦ

´

(t,x) =

where the kernel is given by Kξ

0

f, together with the standard maximal function inequality

j

ˆ

(1 + s|x − y|)−(n+1)|g(y)|sn dy M[g](x) implies that it suﬃces to prove the kernel bound

Rn

(t,x) rj−n 1 + |x + t∇Φ(ξ0)| rj

Kξ

![image 517](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile517.png>)

0

−N

1 + |t| R

![image 518](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile518.png>)

N

. (6.5)

This bound is clearly true when |x + t∇Φ(ξ0)| rj by the Fourier support assumption on ζ. On the other hand, an application of integration by parts gives for every 1 k n

(t,x) = ˆ

ζ rj(ξ − ξ0) eit[Φ

j(ξ)−Φj(ξ0)−(ξ−ξ0)·∇Φj(ξ0)]ei(x+t∇Φ

j(ξ0))·ξdξ

Kξ

0

Rn

|xk + t∂kΦj(ξ0)|−N ˆ

∂kN ζ rj(ξ − ξ0) eit[Φ

j(ξ)−Φj(ξ0)−(ξ−ξ0)·∇Φj(ξ0)] dξ.

Rn

In particular, it suﬃces to show that for every |ξ − ξ0| 2rj−1 we have

j(ξ)−Φj(ξ0)−(ξ−ξ0)·∇Φj(ξ0)] rjN 1 + |t|

∂kN ζ rj(ξ − ξ0) eit[Φ

![image 519](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile519.png>)

R

N

.

This bound is consequence of a somewhat tedious induction argument. For completeness, we sketch the proof here. Let F = it(Φj(ξ) − Φj(ξ0) − (ξ − ξ0) · ∇Φj(ξ0)) and

IN = e−F∂kN ζ rj(ξ − ξ0) eF .

To compute IN explicitly, we observe that IN = ∂kIN−1 + IN−1∂kF, which via an induction argument, implies that

N

∂kN−mI0

IN = ∂kNI0 +

...(∂kmF)ℓ

cm,ℓ(∂kF)ℓ

1

m

ℓ∈Nm ℓ1+2ℓ2+···+mℓm=m

m=1

for some constants cm,ℓ ∈ N. The assumption (A2) together with rj ≫ d0 implies that

|t| R

|t| R

rj2 and for any 3 m N

rj, |∂k2F| |t||∇2Φj(ξ)|

|∂kF| |t||∇Φj(ξ) − ∇Φj(ξ0)|

![image 520](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile520.png>)

![image 521](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile521.png>)

(6.6)

|t| |R|

d20−mR ∇2Φj L∞

|∂kmF| |t||∇mΦj(ξ)|

![image 522](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile522.png>)

Therefore the bound (6.5) follows from the identity (6.6).

|t| R

rjm.

![image 523](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile523.png>)

- Remark 6.5. If we restrict attention to the case |t| R and ǫ = 1, then Lemma 6.4 is essentially equivalent to the wave packet type decompositions used frequently in previous works. See for instance [21, 14, 1, 4]. It is also important to note that the assumption (A2) is essentially the weakest condition for the required concentration bound (6.4) to hold. This can easily be seen from the identity (6.6), since if we want to obtain (6.4), then we essentially require


 ∇mΦj L∞ rjm−2 which is equivalent to having a uniform bound on the quantity

1 m−2

 ∇mΦj L∞  ∇2Φj L∞

![image 524](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile524.png>)

.

![image 525](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile525.png>)

and this is precisely the condition appearing in (A2). Recall that, given a phase space point γj ∈ Γj, we have deﬁned the associated weight wγ

j,q, which penalises the distance from the cube q ∈ Qrj

, by

(Q) and tube Tγ

j

5n

j,q = 1 + |xq − x0 + tq∇Φj(ξ0)| rj

.

wγ

![image 526](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile526.png>)

We now come to the main property of wave packets which we exploit in the sequel.

Proposition 6.6 (Concentration of wave packets II). Let j = 1,2 and 0 < ǫ 1. Assume that the phase Φj ∈ C5n(Λj) satisﬁes (A2). Let R rj ≫ d−0 1 and assume that u is a Φj-wave with supp u + d

2 ⊂ Λj. Then for any cube Q of diameter R we have the concentration/orthgonality type estimate

0

![image 527](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile527.png>)

sup

q∈Qrj (Q)

γj∈Γj

u 2L2

wγ2

j,q χqPγj

t,x

ǫ−14nrj u 2L∞

t L2x. (6.7)

Proof. Let N = 5n and Q be a cube of diameter R. By translation invariance, we may assume that Q is centred at the origin. Write u = eitΦ

j(−i∇)f for some ℓ2c(Z) valued map f. The identity |x − x0 + t∇Φj(ξ0)| = |(t,x) − (0,x0) − t(1,−∇Φj(ξ0))|,

(Q) and γj = (x0,ξ0) ∈ Γj χqPγj

together with an application of Lemma 6.4 implies that for any q ∈ Qrj

u 2L2

t,x

N 2

−N

](x0)|2 χq(t,x) 1 + |x − x0 + t∇Φj(ξ0)| rj

1 + |t| R

ǫ−(N+n)|M[fξ

![image 528](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile528.png>)

![image 529](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile529.png>)

0

L2t,x ǫ−(N+n)|M[fξ

](x0)|2 1 + |xq − x0 + tq∇Φj(ξ0)| rj

χq(t,x) 1 + |(t,x) − (tq,xq)| rj

−2N

2N 2

![image 530](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile530.png>)

![image 531](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile531.png>)

0

L2t,x ǫ−(N+n)rjn+1|M[fξ

−2N

](x0)|2 1 + |xq − x0 + tq∇Φj(ξ0)| rj

![image 532](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile532.png>)

0

where we used (4.1), the rapid decay of χq, and the bound

1 + |t| R

![image 533](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile533.png>)

2 1 + |t − tq| R

![image 534](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile534.png>)

1 + |t − tq| rj

![image 535](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile535.png>)

which follows directly from the conditions |tq| R and rj R. Therefore, we deduce that

rjn+1ǫ−2(N+n)

](x0)|2.

u 2L2

wγ2

|M[fξ

sup

j,q χqPγj

0

t,x

q∈Qrj (Q)

γj∈Γj

(x0,ξ0)∈Γj

together with the maximal inequality gives

To complete the proof of (6.7), we recall that the Fourier localisation of fξ

0

rjn

(x0,ξ0)∈Γj

](x0) 2 ǫ−2n

M[fξ

0

ξ0

] 2L2

 M[fξ

0

x

ǫ−2n

ξ0

fξ

0

2 L2x ≈ ǫ−2n f 2L2

.

x

- Remark 6.7. Note that technical condition rj R is natural since (6.7) only controls u on (essentially) a cube of size R. If rj ≫ R (which corresponds to R ≪  ∇2Φj L∞) then each wave packet is supported in an area larger than Q. In other words, u cannot be localised to scales R ≪  ∇2Φj L∞.
- Remark 6.8. It is worth comparing (6.7) to previous results in the literature where a local in time version


was proven, in the sense that the function χq was replaced by the sharp cutoﬀ 1Cq. The slightly more reﬁned global version (6.7) (which also contains the region |t| ≫ R, albeit with a rapidly decaying weight t−N) allows us to avoid a number of additional error estimates, which would otherwise complicate the analysis, particularly in the general phase case that we consider here.

7. Geometric Consequences of Assumptions on Phases

In this section, following the approach in [4], we give two important consequences of the transversality/curvature assumption (A1). The ﬁrst concerns the surfaces Σj(h) and only requires the transverality condition (1.5), while the second gives a crucial transverality condition concerning the conical set Cj(h) and requires the full strength of the assumption (A1). In fact, this is the only place where the full generality of (A1) is required, rather than just the immediate consequences (1.5) and (1.6).

Recall that give h ∈ R1+n we have deﬁned the surfaces Σj(h) = {ξ ∈ Λj∩(h−Λk) | Φj(ξ)+Φk(h−ξ) = a}. The transversality assumption (1.5) implies that these surfaces are well-behaved.

- Lemma 7.1 (Foliation Properties of Σj(h)). Let h = (a,h) ∈ R1+n and 0 < C0 < 1. Suppose that Λj is open, and that Φj ∈ C2(Λj) satisﬁes the transverality condition (1.5) and the normalisation condition (4.1).


0r ∈ Λ1 and η + C3

Assume ξ + C3

0r ∈ Λ2 with |ξ + η − h|

![image 536](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile536.png>)

![image 537](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile537.png>)

1 r

1 r

, Φ1(ξ) + Φ2(η) − a

.

![image 538](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile538.png>)

![image 539](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile539.png>)

0r and η ∈ Σ2(h) + C3

Then ξ ∈ Σ1(h) + C3

0r.

![image 540](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile540.png>)

![image 541](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile541.png>)

Proof. Let F(ξ) = Φ1(ξ) + Φ2(h − ξ) − a, we may assume that F(ξ) 0 since otherwise we can simply replace F with −F in the argument below. Let ξ(s) be the solution to

∇F(ξ(s)) |∇F(ξ(s))| ξ(0) = ξ.

∂sξ(s) = −

![image 542](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile542.png>)

The conditions on ξ and η imply that t(h − ξ) + (1 − t)η ∈ Λ2 for 0 < t < 1, and hence F(ξ) = |Φ1(ξ) + Φ2(η) − a + Φ2(h − ξ) − Φ2(η)| 3r. Therefore the transversality condition (1.5) gives the bound

![image 543](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile543.png>)

F(ξ(s)) = F(ξ) − ˆ s

3 r − sC0

|∇F(ξ(s′))|ds′

![image 544](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile544.png>)

0

. Since |ξ(s∗) − ξ| s∗ rC 3

and consequently we see that F(ξ(s∗)) = 0 for some 0 s∗ rC 3

and ξ(s∗) ∈ Σ1(h) we have ξ ∈ Σ1(h) + rC3

![image 545](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile545.png>)

![image 546](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile546.png>)

0

0

as required. Replacing Φ1 with Φ2 in the above argument, gives η ∈ Σ2(h) + rC3

![image 547](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile547.png>)

0

. Recall that, given h ∈ R1+n, we have deﬁned the conical hypersurface Cj(h) = s,−s∇Φj(ξ) s ∈ R,ξ ∈ Σj(h) .

![image 548](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile548.png>)

0

The next result we require shows that the normal direction to the surface τ = ∇Φk always intersects the conic surface Cj(h) transversely.

- Lemma 7.2 (Transversality of Cj(h)). Let h ∈ R1+n. Suppose that Λj ⊂ Rn is an open set, and that Φj ∈ C2(Λj) satisﬁes (A1) and the normalisation condition (4.1). For {j,k} = {1,2}, p,q ∈ Cj(h), and η ∈ Λk we have


C0 3 |p − q|.

(p − q) ∧ 1,−∇Φk(η)

![image 549](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile549.png>)

Proof. We follow/repeat the argument given in [4, Lemma 2.7]. Let w,w′,w′′ ∈ Rn. A computation shows that for every v ∈ span{(1,w),(0,w − w′)} we have

|(w − w′) ∧ (w − w′′)| (1 + |w|)|w − w′|

|v ∧ (1,w′′)|

|v|.

![image 550](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile550.png>)

Let ξ,ξ′ ∈ Σj(h) and η ∈ Λk. If we take w = −∇Φj(ξ), w′ = −∇Φj(ξ′), and w′′ = −∇Φk(η) in the above bound, we deduce that

v ∧ 1,−∇Φk(η) |(∇Φj(ξ) − ∇Φj(ξ′)) ∧ (∇Φj(ξ) − ∇Φk(η))| (1 +  ∇Φj L∞(Λj))|∇Φj(ξ) − ∇Φj(ξ′)|

|v|

![image 551](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile551.png>)

for every v ∈ span{(1,−∇Φj(ξ)),(0,∇Φj(ξ)−∇Φj(ξ′))}. The claimed bound now follows by applying (A1), and observing that given any p,q ∈ Cj(h) we can write

(p − q) = (r − r′)(1,−∇Φj(ξ)) + r′(0,∇Φj(ξ) − ∇Φj(ξ′)), for some ξ,ξ′ ∈ Σj(h) and r,r′ ∈ R.

8. Energy Estimates Across Cj(h)

In this section we prove a key energy bound across the conic surface Cj(h). This is the key step in the proof of Theorem 1.4 where the full strength of (A1) is required, elsewhere it is essentially enough to instead consider the weaker conditions (1.5) and (1.6). As noted earlier, the following estimate is roughly a continuous counterpart to the “bush” type arguments used in the combinatorial approach to bilinear restriction estimates.

Recall that given h ∈ R1+n we have deﬁned the conical surfaces Cj(h) = {(s,−s∇Φj(ξ)) | s ∈ R,ξ ∈ Σj(h)}.

We deﬁne a weight χ∗j,r(t,x) associated to Cj(h) by

−(n+2)

dist((t,x),Cj(h)) r

χ∗j,r(t,x) = 1 +

.

![image 552](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile552.png>)

Thus χ∗j,r is essentially concentrated on a r-neighbourhood of the conic surface Cj(h). The geometric condition

- (A1) implies that the wave packets associated to the phase Φk intersect the surface Cj(h) transversally. A rigorous version of this heuristic is the following.

- Theorem 8.1. Let {j,k} = {1,2}, h ∈ R1+n and r ≫ d−0 1 Hj. Assume the phases Φj satisfy (A1),


- (A2), and the normalisation condition (4.1). If v is a Φk-wave with supp v contained in a ball of radius r−1


and supp v + d

8 ⊂ Λk then we have

0

![image 553](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile553.png>)

χ∗j,rv 2L

r v 2L∞

t L2x.

2 t,x

Proof. As in [21, 1] by the TT∗ argument, the required bound is equivalent to proving that for every F ∈ L2t,x, we have ˆ

ˆ

χ∗r(t)U(t)U(−s) χ∗r(s)F(s) ,F(t) L

dtds r F 2L2

2 x

t,x

R

R

where we let

U(t)[f](x) = ˆ

k(ξ)+x·ξ) f(ξ)dξ with supp ρ ⊂ Λj, |supp ρ| r−n, and |∇mρ| rm. Deﬁne

ρ(ξ)ei(tΦ

Rn

K(t,x) = ˆ

ρ2(ξ)ei(tΦ

j(ξ)+x·ξ)dξ.

Rn

By an application of Young’s inequality, and using the assumption |supp ρ| r−n, it is enough to prove the pointwise bound

−(n+2)

1 + |(t − s,x − y)| r

χ∗r(t,x)K(t − s,x − y)χ∗r(s,y) ˆ

dξ. (8.1)

![image 554](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile554.png>)

supp ρ

To this end, take p,p∗ ∈ Cj(h) such that |(t,x) − p| ≈ dist (t,x),Cj(h) , |(s,y) − p∗| ≈ dist (s,y),Cj(h) .

If |(t,x) − p| + |(s,y) − p∗| |p − p∗| then (8.1) follows from the decay of χ∗r away from the surface Cj(h), together with the the observation that

|(t − s,x − y)| |p − p∗| + |(t,x) − p| + |(s,y) − p∗| |(t,x) − p| + |(s,y) − p∗|. On the other hand, if |(t,x) − p| + |(s,y) − p∗| ≪ |p − p∗|, then an application of Lemma 7.2 together with (A1) implies that for every ξ ∈ Λk

(t − s,x − y) ∧ (1,−∇Φk(ξ) (p − p∗) ∧ (1,−∇Φk(ξ) − |(t,x) − p| − |(s,y) − p∗| |p − p∗| |(t − s,x − y)|

where the last inequality follows by writing (t − s,x − y) = p − p∗ + (t,x) − p + (s,y) − p∗. In particular, we have

|x − y + (t − s)∇Φk(ξ)| ≈ |(t − s,x − y)|. (8.2)

We now exploit the decay of the kernel K(t,x) in directions orthogonal to (1,−∇Φk(ξ)). More precisely, integrating by parts in the kernel K(t,x) and applying (A2) implies that for every N < 5n

|K(t,x)| ˆ

...(t ∇N+1Φk )ℓ

(t ∇3Φk )ℓ

(t ∇2Φk )ℓ

1 |x + t∇Φk(ξ)|

2

1

N

ρ2|

|∇ℓ

1+···+ℓN dξ ˆ

0

![image 555](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile555.png>)

![image 556](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile556.png>)

|x + t∇Φk(ξ)|ℓ

supp ρ

ℓ∈N1+N ℓ0+ℓ1+2ℓ2+···+NℓN=N

N

N

1 + |t| |x + t∇Φk(ξ)|

r |x + t∇Φk(ξ)|

dξ

![image 557](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile557.png>)

![image 558](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile558.png>)

supp ρ

where we applied (A2), (4.1), and the assumption r d−0 1 Hj. Therefore (8.1) follows from (8.2). Recall that, given a cube q ∈ Qrj

(Q), we have deﬁned χq ∈ C∞(R1+n) to be a positive function such that χq 1 on q, supp χq ⊂ {|(τ,ξ)| 1r}, and we have the decay bound, for every N ∈ N,

![image 559](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile559.png>)

−N

dist((t,x),q) r

χq(t,x) N 1 +

.

![image 560](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile560.png>)

To exploit the previous theorem, we require the following crucial consequence of the curvature of Φj on Σj(h).

- Lemma 8.2. Let h ∈ R1+n and rj ≫ d−0 1 Hj. Assume that Φj ∈ C2(Λj) satisﬁes (A1) and the


(Q). Then provided that

normalisation condition (4.1). Let {j,k} = {1,2}, Q be a cube of diameter R and q0 ∈ Qrj

j(h) Σj(h) ∩ Λ d0n−1 we have for all (t,x) ∈ R1+n

σΣ

−(n+2)

),Cj(h)] rj

,x − xq

dist[(t − tq

χq(t,x) wγ

ǫ−C 1 +

0

0

.

![image 561](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile561.png>)

![image 562](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile562.png>)

j,q0wγ

j,q

γj∈Γj(h,Λ)

q∈Qrj (B) |q−q0| ǫR

Proof. We start by observing that, for every (x0,ξ0) ∈ Γj(h,Λ), we have dist[(t − tq

),Cj(h)] rj + |(t,x) − (tq,xq)| + |xq − x0 + tq∇Φj(ξ0)| + |xq

,x − xq

0

0

0∇Φj(ξ0)|. In particular, as q(1+ |(t,x)−r(tq,xq)|

0 − x0 + tq

)n+2χq(t,x) 1, it is enough to show that for ﬁxed q,q0 ∈ Qrj

(Q) with |q − q0| ǫR, we have

![image 563](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile563.png>)

j

−3n

0∇Φj(ξ0)| rj

0 − x0 + tq

1 + |xq − x0 + tq∇Φj(ξ0)| + |xq

1.

![image 564](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile564.png>)

(x0,ξ0)∈Γj(h,Λ)

0∇Φj(ξ0)|, thus σ is small when the tube T(x

0 − x0 + tq

For ease of reading, we let σ(x0,ξ0) = |xq − x0 + tq∇Φj(ξ0)| + |xq

0,ξ0) passes through the cubes q and q0, and is large otherwise. Let (x0,ξ0) ∈ Γj(h,Λ) denote the phase space point with the associated tube passing closest to the cubes q and q′, in other words, we take

{σ(x′0,ξ0′ )}. Suppose for the moment that σ(x0,ξ0) ≪ ǫR, thus the tube T(x

σ(x0,ξ0) = min

(x′0,ξ0′ )∈Γj(h,Λ)

0,ξ0) passes “close” to the cubes q and q0. In particular, writing

0∇Φj(ξ0) the separation of the cubes q and q0 implies that |tq − tq

0 − x0 + tq

) − 0,xq − x0 + tq∇Φj(ξ0) + 0,xq

) 1,−∇Φj(ξ0) = (tq,xq) − (tq

(tq − tq

,xq

0

0

0

0| ≈ ǫR. Consequently, as

x0 − x′0 = xq − x′0 + tq∇Φj(ξ0′ ) − xq − x0 + tq∇Φj(ξ0) + tq ∇Φj(ξ0) − ∇Φj(ξ0′ ) , and |tq| R we have by deﬁnition of σ(x0,ξ0),

|x0 − x′0| + R|∇Φj(ξ0) − ∇Φj(ξ0′ )| σ(x0,ξ0) + σ(x′0,ξ0′) + 2R|∇Φj(ξ0) − ∇Φj(ξ0′ )| σ(x0,ξ0) + σ(x′0,ξ0′) +

1 ǫ

) ∇Φj(ξ0) − ∇Φj(ξ0′)

(tq − tq

![image 565](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile565.png>)

0

1 ǫ

σ(x′0,ξ0′ ). We now use the fact that ξ0,ξ0′ ∈ Σj(h) + rC

![image 566](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile566.png>)

, together with (A1) to deduce that

![image 567](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile567.png>)

j

|∇Φj(ξ0) − ∇Φj(ξ0′ )| Hj

1 rj

|ξ0 − ξ0′|

+

.

![image 568](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile568.png>)

![image 569](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile569.png>)

Therefore, since σ(x0,ξ0) σ(x′0,ξ0′ ), we obtain

−3n

σ(x′0,ξ0′) rj

1 +

![image 570](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile570.png>)

(x′0,ξ0′ )∈Γj(h,Λ)

(x0,ξ0)∈Γj(h,Λ)

ǫ−C.

ǫ rj |x0 − x′0| + ǫrj|ξ0 − ξ0′|

1 +

![image 571](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile571.png>)

−3n

On the other hand, if σ(x0,ξ0) ǫR, then we gain a power of R, and can simply discard the ξ0 sum, and sum up over the points x0. More precisely, the assumption on the set Λ, together with the condition d0Hj 1, implies that

Σj(h) ∩ Λ rj−1 + rj−n rj−n

σΣ

n−1

R rj

(1 + d0rj)n−1 1 +

# ξ0 ∈ r1

j

Zn ξ0 ∈ Σj(h) ∩ Λ + rC

![image 572](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile572.png>)

![image 573](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile573.png>)

![image 574](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile574.png>)

![image 575](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile575.png>)

j

j

and hence, as σ(x0,ξ0) ǫR, we obtain

−3n

σ(x′0,ξ0′) rj

1 +

![image 576](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile576.png>)

(x′0,ξ0′ )∈Γj(h,Λ)

ǫ−C sup

ξ0′ x′0

1 + |xq − x′0 + tq∇Φj(ξ0′ )| rj

![image 577](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile577.png>)

−2n

ǫ−C.

9. The Wave Table Construction

As implicitly used in the work of Wolﬀ [27], and more explicitly in the work of Tao [21], we need to decompose u depending on v. Roughly speaking we will decompose u into wave packets, and keep the wave packets where v and Pγj

(Q). We adapt the following

u simultaneously concentrate on the same cube B ∈ QR

![image 578](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile578.png>)

4

construction from Tao, but change notation slightly. Deﬁnition 9.1 (Φj-Wave Tables). Let 0 < ǫ < 1. Let 0 < F L∞

t L2x < ∞, and Q be a cube of diameter R ≫ (d20Hj)−1. Let u be a Φj-wave. The Φj-wave table of u, relative to F and Q, is the collection of (vector valued) functions (Wj,ǫ(B))B∈Q

(Q) where

R 4

![image 579](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile579.png>)

j,B(F) mγ

mγ

Wj,ǫ(B) = Wj,ǫ(B)(u;F,Q) =

(F) Pγj

u

![image 580](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile580.png>)

j

γj∈Γj

where the coeﬃcients are deﬁned as mγ

1 wγ

χqF 2L2

(F) =

1,B(F).

j,B(F) =

t,x(R1+n), mγ

mγ

![image 581](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile581.png>)

j

j,q

B∈QR 4

q∈Qrj (B)

(Q)

![image 582](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile582.png>)

t L2x < ∞ implies that3 0 < χqF L2

- Remark 9.2. The assumption 0 < F L∞


< ∞, and hence the coeﬃcients mγ

t,x

j,B(F) < ∞. Note that we essentially have mγ

j,B(F) are well-deﬁned and satisfy 0 < mγ

t,x(Tγj∩Q). Thus Wj,ǫ(B) contains all wave packets Pγj

j,B(F) ≈ F 2L2

(F) ≈ F 2L2

t,x(Tγj∩B) and mγ

u such that F|Tγj

j

is concentrated on B. Recall that if Q is a cube of diameter R, 0 < r R, and (u(B))B∈Q

r(Q) is a collection of (ℓ2c(Z) valued) functions, we deﬁned the quilt [u(·)] as

1B|u(B)|

[u(·)] =

B∈Qr(Q)

and the ǫ separated cubes

Iǫ,r(Q) =

(1 − ǫ)q.

q∈Qr(Q)

The deﬁnition of the wave tables Wj,ǫ(B) gives the following key bilinear estimate.

![image 583](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile583.png>)

3Since χq has compact Fourier support, it can only have countable number of zeros. In particular, χq > 0 almost everywhere.

- Theorem 9.3. Let {j,k} = {1,2}, 0 < ǫ ≪ 1, and R ≫ (d20Hj)−1. Assume that the phases Φ1 and Φ2 satisfy Assumption 1.1. Let u be a Φj-wave and v be a Φk-wave with


2 ⊂ Λj, supp v + d

supp u + d

2 ⊂ Λk, d[supp u,supp v] d0. Let Q be a cube of diameter R, and for B ∈ QR

0

0

![image 584](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile584.png>)

![image 585](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile585.png>)

(Q), take Wj,ǫ(B) = Wj,ǫ(B)(u;v,Q). Then Wj,ǫ(B) is again a Φj-wave, is linear in u, satisﬁes the support condition

![image 586](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile586.png>)

4

supp Wj,ǫ(B) ⊂ supp u + r1

, and we have the energy estimate

![image 587](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile587.png>)

j

1 2

![image 588](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile588.png>)

2 L∞t L2x

Wj,ǫ(B)

(1 + Cǫ) u L∞

t L2x.

B∈QR 4

(Q)

![image 589](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile589.png>)

Moreover, we have the bilinear estimate |u| − Wj,ǫ(·) v

n−1 2

ǫ−Cr−

![image 590](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile590.png>)

j u L∞

t L2x v L∞

t L2x.

L2t,x(Iǫ, R4 (Q))

![image 591](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile591.png>)

Proof. For ease of notation, for the remainder of the proof, we let u(B) = Wj,ǫ(B)(u;v,Q). By construction, we have B∈Q

mγj,B(v)

(Q) u(B). The initial claims follow immediately from the deﬁnition of the wave table (Wj,ǫ(B))B∈Q

mγj(v) = 1 and hence u = B∈Q

![image 592](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile592.png>)

(Q)

R 4

R 4

![image 593](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile593.png>)

![image 594](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile594.png>)

(Q), together with Lemma 6.3 and Proposition 6.6 (note that, since u is a Φj-wave, we have u L∞

R 4

![image 595](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile595.png>)

t L2x = u(0) L2

). We now turn to the proof of the bilinear estimate. The identity u = B∈Q

x

(Q) u(B) implies that |u|1Q − [u(·)]

R 4

![image 596](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile596.png>)

|u(B)|1Q\B.

(Q)

B∈QR 4

![image 597](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile597.png>)

R

Consequently, as there are only 4n+1 cubes in QR

(Q), the separation of cubes inside Iǫ,

4 implies that |u| − u(·) v

![image 598](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile598.png>)

![image 599](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile599.png>)

4

u(B)v 2L2

u(B)v L

sup

t,x(q).

2 t,x(Iǫ, R4 (Q)\B)

L2t,x(Iǫ, R4 (Q))

![image 600](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile600.png>)

![image 601](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile601.png>)

(Q)

B∈QR 4

q∈Qrj (Q) |q−B| ǫR

![image 602](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile602.png>)

For h = (a,h) ∈ R1+n, we let Hh be a Fourier projection onto the set {|τ − a| r 1

,|ξ − h| r 1

} such that F 2L2

![image 603](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile603.png>)

![image 604](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile604.png>)

j

j

HhF 2L2

≈

.

t,x

t,x

h∈ r1

Z1+n

![image 605](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile605.png>)

j

Observe that given γj = (x0,ξ0) ∈ Γj and h = (a,h) ∈ R1+n, we only have Hh(χqPγj

uχqv) = 0 if there exists ξ ∈ Λj, η ∈ Λk such that

1 rj

1 rj

1 rj

, |ξ + η − h|

, |Φj(ξ) + Φk(η) − a|

|ξ0 − ξ|

.

![image 606](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile606.png>)

![image 607](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile607.png>)

![image 608](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile608.png>)

uχqv) = 0 we must have ξ0 ∈ Σj(h)∩Λ+ rC

Therefore, an application of Lemma 7.1 implies that if Hh(χqPγj

![image 609](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile609.png>)

j

with Λ = supp u ∩ (h − supp v). Consequently we have u(B)v 2L2 t,x(q) χqu(B)χqv 2L2

t,x

mγ

2

j,B mγ

Hh χqPγj

uχqv

.

![image 610](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile610.png>)

L2t,x

j

h∈ r1

Z1+n γj∈Γj(h,Λ)

![image 611](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile611.png>)

j

Since mmγj,B(v)

γj(v) (mmγj,B(v)

- 1

![image 612](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile612.png>)

- 2 , an application of Ho¨lder’s inequality gives


γj(v) )

![image 613](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile613.png>)

![image 614](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile614.png>)

j,B(v) mγ

mγ

Hh χqPγj

uχqv

![image 615](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile615.png>)

(v)

j

γj∈Γj(h,Λ)

2

L2t,x

wγ

j,q mγ

![image 616](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile616.png>)

(v)

j

γj∈Γj

Hh χqPγ1

uχqv

j,B(v) wγ

mγ

2

sup

.

![image 617](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile617.png>)

L2t,x

h∈R1+n γj∈Γj(h,Λ)

j,q

Hence summing up over h ∈ r1

Z1+n, and noting that the product χqPγj

u has Fourier support in a set of size rj−(n+1), we deduce that

![image 618](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile618.png>)

j

u(B)v 2L2

t,x(q)

q∈Qrj |q−B| ǫR

j,B(v) wγ

mγ

wγ

j,q mγ

uχqv 2L2

× sup

χqPγj

![image 619](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile619.png>)

![image 620](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile620.png>)

(v)

t,x

h∈R1+n

j,q

j

q∈Qrj (Q) γj∈Γj

γj∈Γj(h,Λ)

q∈Qrj (Q), |q−B| ǫR

j,B(v) wγ

wγ

mγ

j,q mγ

rj−(n+1)

χqv 2L2

u 2L2

× sup

. (9.1)

χqPγj

![image 621](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile621.png>)

![image 622](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile622.png>)

(v)

t,x

t,x

h∈R1+n

j,q

j

q∈Qrj (Q) γj∈Γj

γj∈Γj(h,Λ)

q∈Qrj (Q), |q−B| ǫR

(v) together with Proposition 6.6 gives

We now estimate the ﬁrst term in (9.1). The deﬁnition of the coeﬃcients mγ

j

wγ

j,q mγ

u 2L2

χqv 2L2

χqPγj

![image 623](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile623.png>)

(v)

t,x

t,x

j

q∈Qrj (Q) γj∈Γj

1 wγ

1 mγ

χqv 2L2

u 2L2

wγ2

× sup

sup

j,q χqPγj

![image 624](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile624.png>)

![image 625](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile625.png>)

(v)

t,x

t,x

γj∈Γj

j,q

q∈Qrj (Q)

j

γj∈Γj

q∈Qrj (Q)

rjǫ−C u 2L∞

t L2x. On the other hand, to estimate the second term in (9.1), expanding the sum over the mγ

j,B(v), we have

j,B(v) wγ

mγ

1 wγ

v 2L2

=

t,x(R1+n).

χq

![image 626](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile626.png>)

![image 627](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile627.png>)

0

j,qwγ

j,q

j,q0

γj∈Γj(h,Λ)

q0∈Qrj (B) γj∈Γj(h,Λ)

has Fourier support in a ball of radius rj−1, by orthogonality, we may assume that v is also supported

Since χq

0

in a ball of radius rj−1. Consequently, an application of Lemma 8.2, translation invariance, and Theorem 8.1 implies that

j,B(v) wγ

mγ

rj v L∞

t L2x. Therefore the required bilinear estimate follows.

![image 628](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile628.png>)

j,q

γj∈Γj(h,Λ)

10. Proof of Theorem 5.1

We are now ready to give the proof of Theorem 5.1. Roughly the idea is that, given R ≫ (d20Hj)−1, Theorem 9.3 allows us to essentially replace the (low frequency) term u with pieces concentrated on R4 cubes. However, since Theorem 9.3 applied to u only requires scales ≫ d−0 2 (as H1 = 1) we can continue decomposing u until we get terms concentrated on the much smaller H2R cubes. We then decompose v, but as Theorem 9.3 applied to v requires R ≫ (d20Hj)−1, we can only apply it once before we start to lose logarithmic factors. The immediate obstruction to applying the above strategy, is that Theorem 9.3 only applies to the separated cubes Iǫ,r(Q). To create the required separation, we use an averaging argument due to Tao.

![image 629](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile629.png>)

Suppose Q is a cube of radius R, and let (ǫm) and (rm) be strictly positive sequences with rm R. We then deﬁne

X[Q] = ∩Mm=1Iǫ

m,rm(Q)

where we recall that Iǫ,r(Q) = ∪q∈Qr(Q)(1 − ǫ)q. Thus cubes inside X[Q] are separated at multiple scales (which is needed as we apply Theorem 9.3 at multiple scales). We will need to move from integrating over Q, to integrating over the smaller X[Q]. The key tool is the following averaging lemma due to Tao.

Lemma 10.1 ([13, Lemma 4.1], [21, Lemma 6.1]). Let 1 q,r ∞, R > 0 and let QR be a cube of diameter R. If ǫ = Mm=1 ǫj 2−(n+2) then there exists a cube Q ⊂ 4QR of side lengths 2R such that

tLrx(QR) 1 + 2n+2ǫ F Lq

tLrx(QR∩X[Q]). (10.1) Proof. We start by considering the case q = r = 1. Let Q(t,x) denote the cube of side lengths 2R centered at the point (t,x) ∈ QR. It is enough to prove that

F Lq

1 |QR|

ˆ

F L1(QR) (1 + 2n+2ǫ)

F L1(QR∩X[Q(t,x)]) dtdx. (10.2) To this end, we begin by observing that since4

![image 630](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile630.png>)

QR

(t′,x′) ∈ X[Q(t,x)] ⇐⇒ (t,x) ∈ X[Q(t′,x′)] we have for every (t′,x′) ∈ QR

ˆ

1X[Q(t,x)](t′,x′)dtdx = |{(t,x) ∈ QR | (t′,x′) ∈ X[Q(t,x)]}| = |QR ∩ X[Q(t′,x′)]|. Thus by an application of Fubini we have

QR

F L1(QR∩X[Q(t,x)]) dtdx = ˆ

ˆ

ˆ

1X[Q(t,x)](t′,x′)dtdx|F(t′,x′)|dt′ dx′

QR

QR

QR

= ˆ

|QR ∩ X[Q(t′,x′)]||F(t′,x′)|dt′ dx′ Consequently the required bound (10.2) would follow from the inequality

QR

|QR| (1 + 2n+2ǫ) QR ∩ X[Q(t,x)] . (10.3) Let Xk = ∩Mm=kIǫ

j,rj(Q(t,x)). Noting the inclusion QR ⊂ Q(t,x), we deduce that |QR ∩ X1| = |QR ∩ Iǫ

1,r1(Q(t,x)) ∩ X2|

|(1 − ǫ1)q ∩ QR ∩ X2|

=

q∈Qr1(Q(t,x))

|q \ (1 − ǫ1)q|

|q ∩ QR ∩ X2| −

q∈Qr1(Q(t,x))

q∈Qr1(Q(t,x))

= |QR ∩ X2| − 1 − (1 − ǫ1)n (2R)n. Since 1 − (1 − ǫ1)n nǫ1, repeating the above argument eventually gives

M

ǫm (1 − 2n+1ǫ)|QR|

|QR ∩ X[Q(t,x)]| |QR| − n2nRn

m=1

and so, provided that ǫ 2−(n+2) we obtain (10.3). Thus the case q = r = 1 follows. The general case follows by observing that there exists G ∈ Lq

′

′

t Lr

x (QR) with G Lq′

t Lrx′(QR) 1 such that F Lq

rLrx(QR) FG L1

t,x(QR) together with an application of the L1t,x case obtained above.

We now come to the proof of Theorem 5.1. Proof. It is enough to consider the case u L∞

t L2x = 1. Fix a cube QR of diameter R ≫ (d20H2)−1 and let M ∈ N such that

t L2x = v L∞

4−M < H2 41−M. An application of Lemma 10.1 implies that there exists a cube Q of radius 2R such that

tLrx(QR) (1 + Cǫ) uv Lq

uv Lq

tLrx(X[Q])

![image 631](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile631.png>)

4Just use the identities X[Q(t, x)] = X[Q(0)] + (t, x) and −X[Q(0)] = X[−Q(0)] = X[Q(0)].

where we take

m,4−m2R(Q), ǫm = 4δ(m−M)ǫ

Iǫ

X[Q] =

m=1,...,M

and δ > 0 is some ﬁxed constant to be chosen later (which will depend only on the dimension n, and the constant C appearing in Theorem 9.3). We start by decomposing u. Given B1 ∈ QR

(Q) we deﬁne the

![image 632](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile632.png>)

2

- Φ1-wave u1(B1) = W1(B,ǫ11)(u;v,Q)


and assuming we have constructed um(Bm), Bm ∈ Q 2R

(Q), we deﬁne for Bm+1 ∈ Q 2R

(Bm) u(mB+1m+1) = W1(B,ǫmm+1+1) u(B

4m

![image 633](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile633.png>)

![image 634](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile634.png>)

4m+1

m)

m ;v,Bm and ﬁnally take u(B) = u(MB) for B ∈ Q 2R

(Q). Note that each u(mBm) is well-deﬁned, since the diameter of the cube Bm−1 is 4−m2R 4−M2R ≫ d20. To construct v, we start by deﬁning U = (u(B))B∈Q

![image 635](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile635.png>)

4M

(Q).

2R 4M

![image 636](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile636.png>)

Clearly, as each u(B) is a Φ1-wave, after relabeling, U is also a Φ1-wave. We now decompose v relative to U and the cube Q, in other words for B′ ∈ QR

(Q) we deﬁne v(B

![image 637](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile637.png>)

2

′)

′) = W(B

2,ǫ v;U,Q . It is easy to check that, by construction, Theorem 9.3 implies that we have the identities

′)

u(B), v =

v(B

u =

B′∈Q R 2

(Q)

B∈Q 2R 4M

(Q)

![image 638](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile638.png>)

![image 639](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile639.png>)

together with the support conditions supp uB

− 12

2R 4m−1

1 2

′) ⊂ supp v + 2H2R −

![image 640](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile640.png>)

m ⊂ supp uBmm−−11 +

, supp v(B

![image 641](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile641.png>)

. Moreover, v(B

m

![image 642](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile642.png>)

′) satisﬁes the required energy estimate, and by iterating the estimate

(Q)

Bm∈Q 2R 4m

![image 643](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile643.png>)

u(B

m) m

2 L∞t L2x =

u(B

m) m

2 L∞t L2x

Bm−1∈Q 2R

(Q) Bm∈Q 2R 4m

(Bm−1)

![image 644](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile644.png>)

![image 645](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile645.png>)

4m−1

um(B−m1−1) 2L∞

(1 + ǫmC)2

t L2x.

Bm−1∈Q 2R

(Q)

![image 646](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile646.png>)

4m−1

and using the elementary inequality ΠMm=1(1 + ǫmC) 1 + e ǫ

mCC ǫm and the deﬁnition of ǫm, a short computation shows that u(B) satisﬁes the correct energy bound. We now turn to the proof of the bilinear estimate. Writing

|uv| = [u(·)][v(·)] + |u| − [u(·) |v| + [u(·)] |v| − [v(·)] ,

after an application of Holder’s inequality in the t variable, it is enough to show that for every 2 r > n+1n we have

![image 647](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile647.png>)

n+1

2r −n2 (10.4) We start by estimating the ﬁrst term. An application of Theorem 9.3 gives

|u| − [u(·)] v L

tLrx(X[Q]) + [u(·)] |v| − [v(·)] L

tLrx(X[Q]) ǫ−C H2R

![image 648](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile648.png>)

![image 649](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile649.png>)

2

2

2

u(m·)−1 − u(m·) v

L2t,x(X[Q])

2

|um(B−m1−1)| − W1(,ǫ·)m(um(B−m1−1)) v

L2t,x(Iǫm, 42mR (Bm−1))

![image 650](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile650.png>)

(Q)

Bm−1∈Q 2R

![image 651](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile651.png>)

4m−1

n−1 2

4m−1 2R

![image 652](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile652.png>)

um(B−m1−1) 2L∞

ǫ−m2C

t L2x

![image 653](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile653.png>)

Bm−1∈Q 2R

(Q)

![image 654](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile654.png>)

4m−1

n−1 2

ǫ−m2C 4−mR −

![image 655](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile655.png>)

where we used the deﬁnition of M. On the other hand, an application of Holder’s inequality together with the energy bound for u(m·) and u(m·)−1 implies that

um(·)−1 − um(·)

u(m·)−1 − u(m·) v

v L∞

t L2x(Q)

L2t,x(Q)

L2tL1x(X[Q])

1 2

![image 656](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile656.png>)

um(B−m1−1) 2L2

u(B

m) m

2 L2t,x(Bm)

t,x(Bm−1) +

Bm

Bm−1

- 1

![image 657](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile657.png>)

- 2


4−mR Hence interpolating gives for any 1 r 2

n+1

1 r ) m 4−mR

2r −n2 . The deﬁnition of ǫm and M implies that we can write

ǫ−2C(1−

u(m·)−1 − u(m·) v

![image 658](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile658.png>)

![image 659](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile659.png>)

![image 660](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile660.png>)

L2tLrx(X[Q])

n+1

1 r )

2r − n2

ǫ−Cn(1−

∗(m−M)

2 (n−n+1r ) ǫ−CH

m

2 4δ

![image 661](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile661.png>)

![image 662](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile662.png>)

![image 663](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile663.png>)

m 4

![image 664](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile664.png>)

![image 665](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile665.png>)

where δ∗ = n2 − n2+1r − Cδ(1 − r1) > 0 provided r > n+1n and we choose δ suﬃciently small. Therefore, telescoping the sum over m and letting u0(Q) = u, we deduce that

![image 666](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile666.png>)

![image 667](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile667.png>)

![image 668](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile668.png>)

![image 669](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile669.png>)

M

n+1

2r −n2 .

[um(·)−1] − [um(·)] v L

tLrx(X[Q]) ǫ−C H2R

|u| − [u(·)] v L

![image 670](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile670.png>)

![image 671](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile671.png>)

2

2 tLrx(X[Q])

m=1

′)

Thus it only remains to estimate the second term in (10.4). To this end, applying the deﬁnition of v(B

together with Theorem 9.3, we have

n−1 4

t,x(Iǫ1,R2 ) ǫ−C H2R −

t,x(X[Q]) U |v| − [v(·)] L

[u(·)] |v| − [v(·)] L

![image 672](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile672.png>)

2

2

![image 673](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile673.png>)

- 1

![image 674](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile674.png>)

- 2 = |U|. On the other hand an application of Holder’s inequality together with the energy estimates gives


where we used the inequality [u(·)] ( B |u(B)|2)

[u(·)] |v| − [v(·)] L

2 tL1x(X[Q])

B∈Q 2R 4M

![image 675](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile675.png>)

u(B) 2L2

t,x(B)

- 1

![image 676](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile676.png>)

- 2


t L2x + [v(·)] L∞

t L2x H2R

v L∞

- 1

![image 677](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile677.png>)

- 2


.

Therefore, interpolating between these bounds gives

and hence (10.4) follows.

[u(·)] |v| − [v(·)] L

tLrx(X[Q]) ǫ−C H2R

2

n+1

2r −n2

![image 678](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile678.png>)

![image 679](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile679.png>)

11. Atomic Wave Tables and the proof of Theorem 1.7

In this section we give the proof of Theorem 1.7, namely the extension of Corollary 1.6 to the atomic spaces UΦa

and UΦb

with a,b 2. As the proof closely follows the argument used to prove Theorem 1.4, we will be somewhat brief.

1

2

We start by deﬁning an atomic Φj-wave to be a function of the form u(t,x) =

1I(t)uI(t,x)

I∈I

where I is a ﬁnite partition of R, 1I(t) is the indicator function adapted to the interval I ⊂ R, and uI is a Φj-wave. Given an atomic Φj-wave u, we use the shorthand

u ℓaL2x =

I∈I

uI aL∞

t L2x

1 a

![image 680](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile680.png>)

.

In particular, if u ℓaL2x 1, then u is simply a UΦa

atom. Note that an atomic Φj-wave is essentially a special case of a Φj-wave, since if we let U = (uI)I∈I then perhaps after relabeling, U is clearly a Φj-wave, and moreover, as in the proof of Corollary 1.6 we have the pointwise bound

j

- 1

![image 681](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile681.png>)

- 2


|uI(t,x)|2

|u(t,x)|

= |U(t,x)|.

I∈I

However, by exploiting the time localisation, atomic Φj-waves satisfy slightly stronger bilinear estimates than those that hold for Φj-waves. More precisely, we may replace Theorem 5.1 with the following.

Theorem 11.1. Let C0 > 0, 12 q 1 1, 12 1r < n+1n , and n+11 < 1b a 1 12. Assume that we have d0 > 0, open sets Λj ⊂ Rn, and phases Φj satisfying (A1), (A2), and the normalisation (4.1). Let QR be

![image 682](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile682.png>)

![image 683](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile683.png>)

![image 684](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile684.png>)

![image 685](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile685.png>)

![image 686](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile686.png>)

![image 687](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile687.png>)

![image 688](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile688.png>)

![image 689](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile689.png>)

![image 690](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile690.png>)

- a cube of diameter R ≫ (d20H2)−1. Then for any 0 < ǫ ≪ 1, any atomic Φ1-wave u = I∈I 1IuI, and any atomic Φ2-wave v = J∈J 1JvJ with


d0 2 ⊂ Λ1, supp v +

d0

supp u +

2 ⊂ Λ2 there exist a cube Q of diameter 2R such that we have a decomposition

![image 691](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile691.png>)

![image 692](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile692.png>)

′)

v(B

u(B), v =

u =

B′∈QR 2

B∈Q 2R 4M

(Q)

(Q)

![image 693](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile693.png>)

![image 694](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile694.png>)

′) = J∈J 1Jv(B

where M ∈ N with 4−M < H2 41−M, and u(B) = I∈I 1Iu(IB) is an atomic Φ1-wave, v(B

′)

J is an atomic Φ2-wave, with the support properties supp u(B) ⊂ supp u + 2 2H2R −

1 2

1 2

′) ⊂ supp v + 2 2H2R −

, supp v(B

![image 695](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile695.png>)

![image 696](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile696.png>)

. Moreover, for any a0,b0 2 we have the energy bounds

1

![image 697](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile697.png>)

a0 (1 + Cǫ) u ℓa0L2x

u(B) a

0

ℓa0L2x

(Q)

B∈Q 2R 4M

![image 698](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile698.png>)

1

′) b0 ℓb0L2x

![image 699](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile699.png>)

b0 (1 + Cǫ) v ℓb0L2x

v(B

B′∈QR 2

(Q)

![image 700](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile700.png>)

and the bilinear estimate uv Lq

tLrx(QR) (1 + Cǫ) u(·) v(·) Lq

tLrx(Q)

(1− r1 − 1b )+

n+1

2r − n2 +(n+1)( a1 − 21)

q+n2+1r −n+12 H

n+1

![image 701](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile701.png>)

![image 702](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile702.png>)

1

+ Cǫ−CR

2 (µ + d0)n

![image 703](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile703.png>)

![image 704](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile704.png>)

![image 705](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile705.png>)

![image 706](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile706.png>)

2 (H2R)

u ℓaL2x v ℓbL2x where the constant C depends only on C0, q, r, and n and we let µ = min{diam(supp u),diam(supp v)}.

![image 707](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile707.png>)

![image 708](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile708.png>)

![image 709](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile709.png>)

![image 710](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile710.png>)

Note that by taking a1 = 21 and 1b 1 − r1, we essentially recover Theorem 5.1.

![image 711](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile711.png>)

![image 712](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile712.png>)

![image 713](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile713.png>)

![image 714](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile714.png>)

We leave the proof of Theorem 11.1 till Section 12, and now turn to the proof of Theorem 1.7. Fix constants d0,C0 > 0, and open sets Λ1,Λ2 ⊂ Rn. Let Φj be phases satisfying (A1) and (A2). As previously, by exploiting dilation and translation invariance, we may assume H2 H1 and the normalisation conditions (4.1). Take sets Λ∗j +d0 ⊂ Λj such that d[Λ∗1 +d0,Λ∗2 +d0] d

- 1

![image 715](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile715.png>)

- 2


C0 , and ﬁx R0 ≫ d201H2 with (R0H2)−

≈ d0.

0

![image 716](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile716.png>)

![image 717](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile717.png>)

The constant R0 will denote the smallest scale of cubes we consider, while the sets Λ∗1 and Λ∗2 will contain the support of u and v respectively.

Deﬁnition 11.2. For any R R0 and 1 a,b,q,r 2, we deﬁne A∗(R) to the best constant for which the inequality

tLrx(Q) A∗(R) u ℓaL2x v ℓbL2x holds for all cubes Q ⊂ R1+n of radius R, and all atomic Φ1-waves u and atomic Φ2-waves v satisfying the support assumption

uv Lq

- 1

![image 718](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile718.png>)

- 2 .


- 1

![image 719](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile719.png>)

- 2, supp v ⊂ Λ∗2 + 4(H2R)−


supp u ⊂ Λ∗1 + 4(H2R)−

As in the proof of Theorem 1.4 in Section 4, the key step in the proof of Theorem 1.7 is to prove the following bounds on A∗(R).

Proposition 11.3. Let C0 > 0, 12 1q 1, 21 1r < n+1n , n+11 < 1b a 1 2 1 and a1 + 1b min{ 1q,r}. There exists a constant C > 0, such that for any d0 > 0, any open sets Λj ⊂ Rn, any phases Φj satisfying (A1) and (A2) with the normalisation (4.1), and any sets Λ∗j + d0 ⊂ Λj with d[Λ∗1 + d0,Λ∗2 + d0] d

![image 720](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile720.png>)

![image 721](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile721.png>)

![image 722](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile722.png>)

![image 723](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile723.png>)

![image 724](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile724.png>)

![image 725](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile725.png>)

![image 726](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile726.png>)

![image 727](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile727.png>)

![image 728](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile728.png>)

![image 729](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile729.png>)

![image 730](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile730.png>)

![image 731](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile731.png>)

C0, we have for every R R0 and 0 < ǫ ≪ 1

0

![image 732](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile732.png>)

A∗(2R) (1+Cǫ)A∗(R) + Cǫ−CR

(1−r1−1b)+ (11.1)

n+1

2r − n2 +(n+1)(a1 −21 )

q+n2+1r −n+12 H

n+1

![image 733](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile733.png>)

![image 734](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile734.png>)

1

2 (µ + d0)n

![image 735](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile735.png>)

![image 736](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile736.png>)

![image 737](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile737.png>)

![image 738](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile738.png>)

2 (H2R)

![image 739](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile739.png>)

![image 740](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile740.png>)

![image 741](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile741.png>)

![image 742](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile742.png>)

and

(1−1r−1b)+ R R0

1 q

n+1

- 1 2− 1q +(n+1)( a1 − 21)

![image 743](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile743.png>)

![image 744](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile744.png>)

![image 745](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile745.png>)

![image 746](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile746.png>)

- 2 d0−(n+1)(µ + d0)n


r − q2

A∗(2R) Cdn+1−

![image 747](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile747.png>)

![image 748](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile748.png>)

![image 749](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile749.png>)

![image 750](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile750.png>)

![image 751](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile751.png>)

(11.2)

0 H

![image 752](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile752.png>)

where µ = min{diam(Λ∗1),diam(Λ∗2)}. Proof. Let Q be a cube of diameter 2R, and let u = I∈I 1I(t)uI be a UΦa

atom, and v = J∈J 1J(t)vJ be a UΦb

1

atom satisfying the support conditions

2

- 1

![image 753](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile753.png>)

- 2, supp v ⊂ Λ∗2 + 4(H22R)−


- 1

![image 754](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile754.png>)

- 2.


supp u ⊂ Λ∗1 + 4(H22R)− An application of Theorem 11.1 gives a cube Q′ of diameter 4R, and atomic waves (u(B))B∈Q

(Q), (v(B

R 4M−1

![image 755](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile755.png>)

′))B′∈QR(Q) such that uv Lq

tLrx(Q) (1+Cǫ) [u(·)][v(·)] Lq

tLrx(Q′)

(1−r1−1b)+ (11.3)

n+1

2r − n2 +(n+1)( a1 − 12)

q+n2+1r −n+12 H

n+1

![image 756](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile756.png>)

![image 757](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile757.png>)

1

+ Cǫ−CR

2 (µ + d0)n

![image 758](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile758.png>)

![image 759](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile759.png>)

![image 760](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile760.png>)

![image 761](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile761.png>)

2 (H2R)

![image 762](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile762.png>)

![image 763](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile763.png>)

![image 764](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile764.png>)

![image 765](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile765.png>)

and the support properties supp u(B) ⊂ Λ∗1 + 4(H2R)−

′) ⊂ Λ∗2 + 4(H2R)− where we used the support assumptions on u and v.

- 1

![image 766](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile766.png>)

- 2, supp v(B


- 1

![image 767](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile767.png>)

- 2


′)

′) = I∈I 1I(t)U(B

To prove (11.1), we let B′ ∈ QR(Q′) and deﬁne the atomic Φ1-wave U(B

I with U(B

′)

′) and an atomic ′) satisfying the correct support assumptions to apply the deﬁnition of A∗(R). Thus

I = (uI(B))B∈Q

(B′). Then for every B′ ∈ QR(Q) we have an atomic Φ1-wave U(B

R 4M−1

![image 768](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile768.png>)

- Φ2-wave v(B


[u(·)][v(·)] Lq

tLrx(Q′)

′)v(B

′) min{q,r} LqtLrx(B′)

U(B

B′∈QR(Q′)

1 a

′) a ℓaL2x

![image 769](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile769.png>)

U(B

A∗(R)

B′∈QR(Q′)

(1 + Cǫ)A∗(R)

1 min{q,r}

![image 770](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile770.png>)

B′∈QR(Q′)

′) b ℓbL2x

v(B

1 b

![image 771](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile771.png>)

where the second line used the assumption a1 + 1b min{ 1q,r} and the last applied the energy inequalities in Theorem 11.1. Therefore the induction bound (11.1) follows from an application of (11.3).

![image 772](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile772.png>)

![image 773](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile773.png>)

![image 774](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile774.png>)

We now turn to the proof of (11.2). We begin by observing that again using the bound (11.3) with ǫ ≈ 1,

the deﬁnition of R0, and using the nesting properties of the ℓp spaces, it is enough to prove that for every 1

1 a

- 1

![image 775](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile775.png>)

- 2 and 1b 1 − 1r we have the quilt bound


![image 776](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile776.png>)

![image 777](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile777.png>)

![image 778](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile778.png>)

![image 779](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile779.png>)

- b


n−1 b

1 a− 21)

r−1b)H(n+1)(

- 1

![image 780](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile780.png>)

- 2−1b (µ + d0)n(1−


1

[u(·)][v(·)] L

![image 781](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile781.png>)

![image 782](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile782.png>)

![image 783](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile783.png>)

0 (RH2)

2 u ℓaL2 v ℓbL2. (11.4)

tLrx(Q′) d

![image 784](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile784.png>)

![image 785](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile785.png>)

![image 786](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile786.png>)

2

To this end, we ﬁrst note that applying Ho¨lder’s inequality gives for any a0 2 [u(·)][v(·)] L

t,x(Q′) [v(·)] L

tL1x(Q′) [u(·)] L

∞ t L2x(Q′)

2

2

1

a0 − 21) 2

1

H(n+1)(

′)

![image 787](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile787.png>)

1 2

a0 sup B′∈QR 2

u(B) a

v(B

![image 788](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile788.png>)

![image 789](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile789.png>)

(RH2)

0

![image 790](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile790.png>)

L∞t L2x

L∞t L2x

(Q′)

(Q′)

B∈Q 2R 4M

![image 791](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile791.png>)

![image 792](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile792.png>)

1

a0 − 21)

H(n+1)(

1 2

![image 793](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile793.png>)

![image 794](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile794.png>)

(RH2)

2 u ℓa0L2 v ℓ∞L2. (11.5) Similarly, we have the L2t,x bound

![image 795](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile795.png>)

1 a0

![image 796](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile796.png>)

a0 − 21) 2 (RH2)

1

t,x(Q′) H(n+1)(

′) a0 L∞t L2x(B)

- 1

![image 797](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile797.png>)

- 2 sup


u(B)v(B

[u(·)][v(·)] L

![image 798](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile798.png>)

![image 799](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile799.png>)

2

B′

B

1 a0

![image 800](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile800.png>)

1

a0 − 21) 2 (RH2)

H(n+1)(

′)

- 1

![image 801](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile801.png>)

- 2(µ + d0)


n 2

u(B) a

v(B

![image 802](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile802.png>)

![image 803](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile803.png>)

sup

0

![image 804](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile804.png>)

L∞t L2x

L∞t L2x

B′

B

a0 − 21) 2 (RH2)

1

H(n+1)(

- 1

![image 805](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile805.png>)

- 2(µ + d0)


n

![image 806](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile806.png>)

![image 807](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile807.png>)

2 u ℓa0L2 v ℓ∞L2. (11.6) On the other hand, as in the proof of Proposition 4.2, an application of Theorem 5.2 gives

![image 808](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile808.png>)

[u(·)][v(·)] L

2 t,x(Q′)

(Q′) B′∈QR 2

(Q′)

I∈I J∈J B∈Q 2R 4M

![image 809](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile809.png>)

![image 810](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile810.png>)

′) J

u(IB)v(B

2 L2t,x

- 1

![image 811](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile811.png>)

- 2


n−1 2

![image 812](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile812.png>)

0 u ℓ2L2 v ℓ2L2. (11.7)

d

Therefore the required bound (11.4) follows by interpolating5 between (11.5), (11.6), and the bilinear estimate (11.7).

Finally we come to the proof of Theorem 1.7.

Proof of Theorem 1.7. After rescaling, we may assume the normalisation (4.1). The atomic deﬁnition of the UΦa spaces, together with the deﬁnition of A∗(R), implies that it is enough to show that for every m ∈ N we have

(1− r1 −1b )+

n+1

r − 2q

- 1 2− 1q +(n+1)( a1 − 21)

![image 813](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile813.png>)

![image 814](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile814.png>)

![image 815](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile815.png>)

![image 816](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile816.png>)

- 2 d0−(n+1)µn


A∗(2mR0) dn+1−

![image 817](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile817.png>)

![image 818](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile818.png>)

![image 819](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile819.png>)

![image 820](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile820.png>)

0 H

, (11.8) with the implied constant independent of m. We now essentially repeat the proof of Theorem 1.4, but use Proposition 11.3 in place of Proposition 4.3 and Proposition 4.2. Let δ = n+12 − 1q − n2+1r − n+12 (1 − 1r − 1b)+, note that by assumption, we have δ > 0. An application of Proposition 11.3 with R = 2mR0 and ǫ = C1 2−

![image 821](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile821.png>)

![image 822](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile822.png>)

![image 823](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile823.png>)

![image 824](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile824.png>)

![image 825](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile825.png>)

![image 826](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile826.png>)

m 2C δ

![image 827](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile827.png>)

![image 828](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile828.png>)

implies that

(1− r1 − 1b )+

n+1

r − 2q

- 1

![image 829](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile829.png>)

- 2 −q1+(n+1)( a1 − 21) 2 d0−(n+1)µn


2 δdn+1−

![image 830](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile830.png>)

![image 831](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile831.png>)

m

m

2Cδ)A∗(2m−1R0)+CC+12−

A∗(R)(2mR0) (1+2−

![image 832](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile832.png>)

![image 833](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile833.png>)

![image 834](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile834.png>)

![image 835](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile835.png>)

![image 836](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile836.png>)

0 H

. In particular, since δ > 0, after m applications of the bound (11.1) we have

![image 837](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile837.png>)

![image 838](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile838.png>)

(1− r1 −1b )+

n+1

r − 2q

- 1

![image 839](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile839.png>)

- 2− 1q +(n+1)( a1 − 21) 2 d0−(n+1)µn


A∗(2mR0) A∗(R0) + dn+1−

![image 840](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile840.png>)

![image 841](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile841.png>)

![image 842](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile842.png>)

![image 843](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile843.png>)

![image 844](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile844.png>)

![image 845](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile845.png>)

![image 846](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile846.png>)

0 H

where the implied constant depends only on the exponents q,r,a,b, the dimension n, and C0. The required inequality (11.8) now follows from another application of Proposition 11.3.

![image 847](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile847.png>)

5This is simply an application of complex interpolation. In more detail, we just repeat the proof of the Riesz-Thorin interpolation theorem, thus given a functions g ∈ L2t(R) and G ∈ L∞t Lrx′(R1+n), we deﬁne the function ρ(z) for z ∈ C as

+ 1−2z )−1

+ 1−2z )−1

a( az

b( bz

ρ(z) = ˆ

L∞t L2x |vJ| g(t)|G|r′(21+z2)−1Gdt dx

L∞t L2x [u(I,m·) ] 2R

![image 848](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile848.png>)

![image 849](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile849.png>)

![image 850](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile850.png>)

![image 851](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile851.png>)

0

0

1I(t) uI

1J(t) vJ

![image 852](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile852.png>)

![image 853](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile853.png>)

4m

![image 854](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile854.png>)

X[Q] I∈I

J∈J

- 1 r + a1 −1

![image 855](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile855.png>)

![image 856](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile856.png>)

![image 857](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile857.png>)

- 2


- 1 r + 1b −1

![image 858](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile858.png>)

![image 859](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile859.png>)

![image 860](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile860.png>)

- 2 r −1 . It is easy to check that ρ is complex analytic when 0 ℜ(z) 1, is at most of


where a1

r−1 and b1

=

=

![image 861](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile861.png>)

![image 862](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile862.png>)

0

0

![image 863](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile863.png>)

![image 864](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile864.png>)

exponential growth, and ρ(0) can be bounded by the L2t,x estimate, ρ(1) by the L2tL1x estimate. Hence interpolated bound follows from the Hadamard Three-Lines Theorem or Lindel¨of’s Theorem.

12. Proof of Theorem 11.1

Here we give the proof of the atomic wave table decomposition in Theorem 11.1. The argument follows that used to prove Theorem 5.1 but, as in the proof of Proposition 11.3, we interpolate with an improved L2tL1x estimate, and an additional L2t,x estimate to gain the ℓa and ℓb sums over intervals. Since ℓb

⊂ ℓb

2

1

for b1 b2, it is enough to consider the case n+11 < 1b 1 − r1. Fix a cube QR of diameter R ≫ (d20H2)−1 and let u = I∈I 1I(t)uI be an atomic Φ1-wave, and v = J∈J 1J(t)vJ be an atomic Φ2-wave with the support conditions

![image 865](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile865.png>)

![image 866](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile866.png>)

![image 867](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile867.png>)

d0 2 ⊂ Λ1, supp v +

d0 2 ⊂ Λ2. An application of Lemma 10.1 implies that there exists a cube Q of radius 2R such that

supp u +

![image 868](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile868.png>)

![image 869](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile869.png>)

tLrx(QR) (1 + Cǫ) uv Lq

uv Lq

tLrx(X[Q])

where as in Theorem 5.1 we take X[Q] =

m=1,...,M

m,4−m2R(Q), ǫm = 4δ(m−M)ǫ

Iǫ

and δ > 0 is some ﬁxed constant to be chosen later (which will depend only on the dimension n, and the constant Cn appearing in Theorem 9.3) and we take M ∈ N such that 4−(M+1) < H2 4−M.

We start by decomposing the components uI of u. Let V = (vJ)J∈J , thus V is a Φ2-wave such that |v| |V |. Given B1 ∈ QR

(Q) we let

![image 870](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile870.png>)

2

uI,(B11) = W1(B,ǫ11)(uI;V,Q) (where W is as in Deﬁnition 9.1) and assuming we have constructed uI,m(Bm), Bm ∈ Q 2R

(Q), we deﬁne for Bm+1 ∈ Q 2R

4m

![image 871](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile871.png>)

(Bm)

![image 872](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile872.png>)

4m+1

uI,m(Bm+1+1) = W1(,ǫBmm+1+1) u(I,mBm);V,Bm . To extend this to the atomic waves, we simply take um(Bm) = I∈I 1I(t)u(I,mBm). Finally, for B ∈ Q 2R

(Q),

![image 873](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile873.png>)

4M

we let u(B) = u(MB). Clearly u(B) is again an atomic Φ1-wave, and as in the proof Theorem 5.1, from an application of Theorem 9.3, the pointwise decomposition and support properties of u(B) follow immediately. On the other hand, the energy inequality follows by exchanging the order of summation, using the fact that

- a 2, and applying the energy estimate in Theorem 9.3


1 a

1 a

a 2

![image 874](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile874.png>)

![image 875](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile875.png>)

![image 876](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile876.png>)

u(IB) 2L

u(B) aℓaL2x

∞ t L2x

I∈I B∈Q 2R 4M

B∈Q 2R 4M

(Q)

(Q)

![image 877](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile877.png>)

![image 878](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile878.png>)

(1 + Cǫ) u ℓaL2x. The next step is to decompose v = J∈J 1J(t)vJ. Let U = (u(IB))I∈I,B∈Q

. Then U is a Φ1-wave with the pointwise bound [u(·)] |U| and the energy bound U L∞

2R 4M

![image 879](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile879.png>)

t L2x u ℓ2L2x. We now decompose each vJ relative to U and the cube Q, in other words for every B′ ∈ Q2R

(Q) we take

![image 880](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile880.png>)

4

′)

′)

J = W(B

v(B

2,ǫ vJ;U,Q and ﬁnally deﬁne v(B

′)

′) is an atomic Φ2-wave and that v(B

′) = J∈J 1J(t)v(B

J . An application of Theorem 9.3 implies that v(B

′) satisﬁes the correct Fourier support conditions. Furthermore, by a similar argument to the u(B) case, the required energy inequality also holds.

We now turn to the proof of the bilinear estimate. After observing that uv Lq

tLrx(X[Q]) [u(·)][v(·)] Lq

tLrx(X[Q]) + |u| − [u(·)] v Lq

tLrx(X[Q]) + [u(·)] |v| − [v(·)] Lq

tLrx(X[Q]),

an application of Holder’s inequality implies that it is enough to show that for n+11 < 1b 1 − r1, and 1

![image 881](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile881.png>)

![image 882](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile882.png>)

![image 883](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile883.png>)

1 a

1 2 we have

![image 884](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile884.png>)

![image 885](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile885.png>)

![image 886](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile886.png>)

- b


|u| − [u(·)] v L

tLrx(X[Q])+ [u(·)] |v| − [v(·)] L

2

2 tLrx(X[Q])

(12.1)

- 1

![image 887](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile887.png>)

- 2−n2+1b (µ + d0)n(1−


1 a− 21 )

r−1b)H(n+1)(

1

ǫ−C H2R

![image 888](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile888.png>)

![image 889](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile889.png>)

![image 890](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile890.png>)

2 u ℓaL2 v ℓbL2

![image 891](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile891.png>)

![image 892](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile892.png>)

with µ = min{diam(supp u),diam(supp v)}. We start by estimating the ﬁrst term. The point is to interpolate between a “bilinear” L2t,x estimate which decays in R, and “linear” L2tL1x and L2t,x estimates which can lose powers of R. The bilinear L2t,x bound follows from an application of Theorem 9.3

2

u(m·)−1 − u(m·) v

L2t,x(X[Q])

2

|uI,m(Bm−−11)| − W1(·,ǫ)m(uI,m(Bm−−11);V,Q) V

L2t,x(Iǫm, 42mR (Bm−1))

![image 893](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile893.png>)

I∈I Bm−1∈Q 2R

(Q)

![image 894](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile894.png>)

4m−1

n−1 2

4m−1 2R

![image 895](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile895.png>)

uI,m(Bm−−11) 2L∞

ǫ−2C

t L2x V 2L∞

n

t L2x

![image 896](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile896.png>)

m

I∈I Bm−1∈Q 2R

(Q)

![image 897](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile897.png>)

4m−1

n−1 2

4 −δCn) H2R −

n−1

u 2ℓ2L2 v 2ℓ2L2 (12.2)

4−2(M−m)(

ǫ−2C

![image 898](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile898.png>)

n

![image 899](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile899.png>)

where we used the deﬁnition of ǫm and M. To obtain the L2tL1x bound, we start by noting that for any 1 m M, and a0 2 we have

1 2

- 1

![image 900](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile900.png>)

- 2


![image 901](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile901.png>)

u(mB) 2L

u(mB) 2L

∞ t L2x

∞ t L2x

(Q)

(Q)

B∈Q 2R 4m

B∈Q 2R 4m

![image 902](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile902.png>)

![image 903](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile903.png>)

1 a0

![image 904](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile904.png>)

n+1

2 − na+10 )

u(mB) aℓ0

4m(

![image 905](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile905.png>)

![image 906](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile906.png>)

a0L2x

B∈Q 2R 4m

(Q)

![image 907](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile907.png>)

a0 − 12)

1

H(n+1)(

![image 908](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile908.png>)

![image 909](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile909.png>)

2 u ℓa0L2x (12.3)

where we applied the energy inequality for u(mB). Therefore, an application of Holder’s inequality gives for any a0 2

u(m·)−1 − u(m·) v

u(m·)−1 − um(·)

v L∞

t L2x(Q)

L2tL1x(X[Q])

L2t,x(Q)

- 1

![image 910](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile910.png>)

- 2


1 2

R 4m

![image 911](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile911.png>)

um(B−m1−1) 2L∞

u(B

m) m

2 L∞t L2x(Bm)

t L2x(Bm−1) +

v ℓ∞L2

![image 912](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile912.png>)

Bm−1

Bm

1

a0 − 12)

H(n+1)(

1 2

- 1

![image 913](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile913.png>)

- 2 u ℓa0L2 v ℓ∞L2. (12.4)


2 4(M−m) On the other, for the linear L2t,x bound, we can apply a similar argument to deduce that

![image 914](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile914.png>)

![image 915](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile915.png>)

![image 916](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile916.png>)

H2R

- 1

![image 917](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile917.png>)

- 2


- 1

![image 918](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile918.png>)

- 2


R 4m

um(B−m1−1)v 2L∞

u(m·)−1 − u(m·) v

m v 2L∞

u(B

m)

t L2x(Bm−1) +

t L2x(Bm)

![image 919](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile919.png>)

L2t,x(X[Q])

Bm−1

Bm

- 1

![image 920](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile920.png>)

- 2


um(B−m1−1) 2L∞

n 2

u(B

m) m

2 L∞t L2x

(µ + d0)

t L2x +

v L∞

![image 921](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile921.png>)

t L2x

Bm−1

Bm

a0 − 12)

1

H(n+1)(

- 1

![image 922](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile922.png>)

- 2


- 1

![image 923](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile923.png>)

- 2 u ℓa0L2 v ℓ∞L2 (12.5)


n 2

2 4(M−m) where we used the fact that at least one of u(B) of v(B

![image 924](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile924.png>)

![image 925](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile925.png>)

(µ + d0)

H2R

![image 926](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile926.png>)

′) has Fourier support contained in a set of diameter d0 + µ. Interpolating between (12.2), (12.4), and (12.5) then gives for any 12 r 1 1, 1b 1 − r1, and

![image 927](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile927.png>)

![image 928](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile928.png>)

![image 929](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile929.png>)

![image 930](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile930.png>)

1 b

![image 931](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile931.png>)

1 a

![image 932](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile932.png>)

1 2,

![image 933](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile933.png>)

u(m·)−1 2R

− u(m·) 2R

v

L2tLrx(X[Q]) ǫ−C4−(M−m)δ

4m

![image 934](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile934.png>)

![image 935](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile935.png>)

4m−1

- 1

![image 936](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile936.png>)

- 2−n2+1b (µ + d0)n(1−


1 a− 12)

r−1b)H(n+1)(

∗

1

![image 937](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile937.png>)

![image 938](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile938.png>)

![image 939](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile939.png>)

H2R

2 u ℓaL2x v ℓbL2x

![image 940](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile940.png>)

![image 941](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile941.png>)

where δ∗ = n2+1b − 12 − 2δCn1b. Consequently, provided that n+11 < 1b 1 − r1, and we choose δ suﬃciently small depending only on Cn, b, and n, we have δ∗ > 0. Thus by telescoping the sum over m and letting

![image 942](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile942.png>)

![image 943](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile943.png>)

![image 944](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile944.png>)

![image 945](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile945.png>)

![image 946](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile946.png>)

![image 947](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile947.png>)

u0(Q) = u, we deduce that

M

[um(·)−1] − [um(·)] v L

|u| − [u(·)] v L

2 tLrx(X[Q])

2 tLrx(X[Q])

m=1

- 1

![image 948](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile948.png>)

- 2−n2+1b (µ + d0)n(1−


1 a− 12)

r−1b)H(n+1)(

1

ǫ−C H2R

![image 949](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile949.png>)

![image 950](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile950.png>)

![image 951](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile951.png>)

2 u ℓaL2x v ℓbL2x. It only remains to estimate the second term on the left hand side of (12.1). To this end, applying the deﬁnition of v(B

![image 952](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile952.png>)

![image 953](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile953.png>)

′) together with Theorem 9.3, we have

n−1 2

H2R −

[u(·)] |v| − [v(·)] 2L

U |vJ| − [vJ(·)] 2L

u 2ℓ2L2 v 2ℓ2L2.

t,x(Iǫ1,R2 (Q)) ǫ−2C

![image 954](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile954.png>)

n

2 t,x(X[Q])

2

![image 955](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile955.png>)

J∈J

On the other hand an application of Holder’s inequality together with the energy estimates and (12.3) gives for any a0 2 the bounds

- 1

![image 956](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile956.png>)

- 2


t L2x + [vJ(·)] L∞

[u(·)] |v| − [v(·)] L

u(B) 2L2

sup

vJ L∞

t L2x

t,x(B)

2 tL1x(X[Q])

J∈J

B∈Q 2R 4M

![image 957](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile957.png>)

1

a0 − 21)

H(n+1)(

- 1

![image 958](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile958.png>)

- 2


![image 959](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile959.png>)

![image 960](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile960.png>)

H2R

2 u ℓa0L2 v ℓ∞L2 (12.6) and

1 2

![image 961](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile961.png>)

t L2x + [vJ(·)] L∞

n 2

u(B) 2L2

[u(·)] |v| − [v(·)] L

sup

t,x(X[Q]) (µ + d0)

vJ L∞

![image 962](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile962.png>)

t L2x

t,x(B)

2

J∈J

B∈Q 2R 4M

![image 963](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile963.png>)

a0 − 12)

1

H(n+1)(

1 2

n 2

![image 964](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile964.png>)

![image 965](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile965.png>)

![image 966](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile966.png>)

2 u ℓa0L2 v ℓ∞L2. (12.7) Therefore, by interpolation, we deduce that for 21 r 1 1, 1b 1 − r1, and 1b a 1 12, we have

(µ + d0)

H2R

![image 967](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile967.png>)

![image 968](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile968.png>)

![image 969](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile969.png>)

![image 970](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile970.png>)

![image 971](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile971.png>)

![image 972](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile972.png>)

![image 973](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile973.png>)

![image 974](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile974.png>)

- 1

![image 975](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile975.png>)

- 2−n2+1b (µ + d0)n(1−


1 a− 12)

r−1b)H(n+1)(

1

[u(·)] |v| − [v(·)] L

tLrx(X[Q]) ǫ−C H2R

![image 976](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile976.png>)

![image 977](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile977.png>)

![image 978](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile978.png>)

2 u ℓaL2 v ℓbL2 and consequently (12.1) follows.

![image 979](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile979.png>)

![image 980](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile980.png>)

2

References

- 1. I. Bejenaru, Optimal bilinear restriction estimates for general hypersurfaces and the role of the shape operator, Internat. Math. Res. Notices 2017 (2017), no. 23, 7109–7147.
- 2. J. Bourgain, Reﬁnements of Strichartz’ inequality and applications to 2D-NLS with critical nonlinearity, Internat. Math. Res. Notices (1998), no. 5, 253–283.
- 3. S. Buschenhenke, D. Mu¨ller, and A. Vargas, A Fourier restriction theorem for a two-dimensional surface of ﬁnite type, Anal. PDE 10 (2017), no. 4, 817–891.
- 4. T. Candy and S. Herr, Transference of bilinear restriction estimates to quadratic variation norms and the Dirac-KleinGordon system, to appear in Anal. PDE, arXiv:1605.04882[math.AP].
- 5. T. Candy and S. Herr, Conditional large data scattering results for the Dirac-Klein-Gordon system, arXiv:1709.09556[math.AP].
- 6. T. Candy and S. Herr, On the Majorana condition for nonlinear Dirac systems, to appear in Annales de l’Institut Henri Poincar C, Analyse non linaire (2018), arXiv:1709.09568[math.AP].
- 7. M. Hadac, S. Herr, and H. Koch, Well-posedness and scattering for the KP-II equation in a critical space, Ann. Inst. H. Poincar´e Anal. Non Lin´eaire 26 (2009), no. 3, 917–941.
- 8. R. Killip, B. Stovall, and M. Visan, Scattering for the cubic Klein-Gordon equation in two space dimensions, Trans. Amer. Math. Soc. 364 (2012), no. 3, 1571–1631.


- 9. H. Koch and D. Tataru, Dispersive estimates for principally normal pseudodiﬀerential operators, Comm. Pure Appl. Math. 58 (2005), no. 2, 217–284.
- 10. , A priori bounds for the 1d cubic NLS in negative sobolev spaces, Internat. Math. Res. Notices 2007 (2007), rnm053.

![image 981](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile981.png>)

- 11. S. Lee, Bilinear restriction estimates for surfaces with curvatures of diﬀerent signs, Trans. Amer. Math. Soc. 358 (2006), no. 8, 3511–3533 (electronic).
- 12. S. Lee, K.M. Rogers, and A. Vargas, Sharp null form estimates for the wave equation in R3+1, Internat. Math. Res. Notices

(2008), Art. ID rnn 096, 18.

- 13. S. Lee and A. Vargas, Sharp null form estimates for the wave equation, Amer. J. Math. 130 (2008), no. 5, 1279–1326.
- 14. , Restriction estimates for some surfaces with vanishing curvatures, Journal of Functional Analysis 258 (2010), no. 9, 2884 – 2909.

![image 982](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile982.png>)

- 15. A. Moyua, A. Vargas, and L. Vega, Schr¨odinger maximal function and restriction properties of the Fourier transform, Internat. Math. Res. Notices (1996), no. 16, 793–815.
- 16. , Restriction theorems and maximal operators related to oscillatory integrals in R3, Duke mathematical journal 96

![image 983](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile983.png>)

(1999), no. 3, 547–574.

- 17. J. Ramos, A reﬁnement of the Strichartz inequality for the wave equation with applications, Adv. Math. 230 (2012), no. 2, 649–698.
- 18. E.M. Stein, Harmonic analysis: real-variable methods, orthogonality, and oscillatory integrals, Princeton Mathematical Series, vol. 43, Princeton University Press, Princeton, NJ, 1993, With the assistance of Timothy S. Murphy, Monographs in Harmonic Analysis, III.
- 19. J. Sterbenz and D. Tataru, Regularity of wave-maps in dimension 2 + 1, Comm. Math. Phys. 298 (2010), no. 1, 231–264.
- 20. B. Stovall, Linear and bilinear restriction to certain rotationally symmetric hypersurfaces, Trans. Amer. Math. Soc. 369

(2017), no. 6, 4093–4117.

- 21. T. Tao, Endpoint bilinear restriction theorems for the cone, and some sharp null form estimates, Math. Z. 238 (2001), no. 2, 215–268.
- 22. , A sharp bilinear restrictions estimate for paraboloids, Geom. Funct. Anal. 13 (2003), no. 6, 1359–1384.

![image 984](<2017-candy-multi-scale-bilinear-restriction-estimates_images/imageFile984.png>)

- 23. T. Tao, A. Vargas, and L. Vega, A bilinear approach to the restriction and Kakeya conjectures, J. Amer. Math. Soc. 11

(1998), no. 4, 967–1000.

- 24. D. Tataru, Null form estimates for second order hyperbolic operators with rough coeﬃcients, Harmonic analysis at Mount Holyoke (South Hadley, MA, 2001), Contemp. Math., vol. 320, Amer. Math. Soc., Providence, RI, 2003, pp. 383–409.
- 25. F. Temur, An endline bilinear cone restriction estimate for mixed norms, Math. Z. 273 (2013), no. 3-4, 1197–1214.
- 26. Ana Vargas, Restriction theorems for a surface with negative curvature, Math. Z. 249 (2005), no. 1, 97–111.
- 27. T. Wolﬀ, A sharp bilinear cone restriction estimate, Ann. of Math. (2) 153 (2001), no. 3, 661–698.


(T. Candy) Universitat¨ Bielefeld, Fakultat¨ fur¨ Mathematik, Postfach 100131, 33501 Bielefeld, Germany E-mail address: tcandy@math.uni-bielefeld.de

