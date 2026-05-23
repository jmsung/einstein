arXiv:1601.07119v3[math.AP]4May2018

ON SMOOTHNESS OF EXTREMIZERS OF THE TOMAS-STEIN INEQUALITY FOR S1

SHUANGLIN SHAO

Abstract. We prove that the extremizers to the Tomas-Stein inequality for the one dimension sphere are smooth. This is achieved by studying the associated generalized Euler-Lagrange equation.

1. Introduction

To understand the Fourier transform of functions on the Euclidean space, Stein [31] proposed the restriction problem. Let d ≥ 1 be a ﬁxed integer. Let S be a smooth compact hypersurface with boundary in the space Rd+1 = R × Rd and σ be the induced Lebesgue measure on S. Stein’s restriction problem asks for which 1 ≤ p,q ≤ ∞ is the following estimate true,

fσ Lq(R×Rd) ≤ Cp,q,d,S f Lp(S),

for all test functions, where F is the space time Fourier transform. It is not hard to see that p,q satisfy the following necessary conditions

d p′ ≥

d + 2 q

2(d + 1) d

,

,

q >

![image 1](<2016-shao-smoothness-extremizers-tomas-stein-inequality_images/imageFile1.png>)

![image 2](<2016-shao-smoothness-extremizers-tomas-stein-inequality_images/imageFile2.png>)

![image 3](<2016-shao-smoothness-extremizers-tomas-stein-inequality_images/imageFile3.png>)

where p′ is the conjugate exponent of p. This problem is related to several outstanding conjectures in harmonic analysis such as the Bochner-Riesz conjecture and the Kakeya conjecture; for the references, see for instance [31, 4, 6, 18, 19, 33, 35].

Let S = Sd, the unit sphere in R×Rd, and σ be the surface measure. The Tomas-Stein inequality for the sphere is

- (1) fσ L2+

4 d (Rd+1)

![image 4](<2016-shao-smoothness-extremizers-tomas-stein-inequality_images/imageFile4.png>)

≤ Rd f L2(Sd) where d ≥ 1, Rd denotes the optimal constant

- (2) Rd = sup f∈L2


fσ

4 d

L2+

![image 5](<2016-shao-smoothness-extremizers-tomas-stein-inequality_images/imageFile5.png>)

.

![image 6](<2016-shao-smoothness-extremizers-tomas-stein-inequality_images/imageFile6.png>)

f L2(Sd)

f =0

The Tomas-Stein inequality belongs to the family of Fourier restriction inequalities. It can be regarded as an estimate of the Fourier transform of a measure supported on the sphere Sd. The non-endpoint estimate was established by Tomas while the endpoint was established by Stein by complex interpolation [31]. Its variants, the Strichartz inequalities, are useful in the partial diﬀerential equations, see for instance [34].

![image 7](<2016-shao-smoothness-extremizers-tomas-stein-inequality_images/imageFile7.png>)

2010 Mathematics Subject Classiﬁcation. 42A38, 45E10. Key words and phrases. The Tomas-Stein inequality, extremizers, smoothness.

1

Recently the study of the extremal problem for the Fourier restriction inequality or the Strichartz inequalities has attracted a lot of attention. It includes the questions of proving existence of extremizers and establishing characterization of extremizers such as regularity or uniqueness for these inequalities.

A variant of (1) is the Strichartz inequality for the Schro¨dinger equation,

- (3) eit∆f L2+

4 d

![image 8](<2016-shao-smoothness-extremizers-tomas-stein-inequality_images/imageFile8.png>)

t,x (R×Rd)

≤ C f L2(Rd)

where eit∆f(x) = (2π1)d/2 Rd eix·ξ+it|ξ|2fˆ(ξ)dξ and d ≥ 1. This can be viewed as an estimate of the Fourier transform of a measure supported on the paraboloid in R×Rd. For d = 1 in (3), Kunze is the ﬁrst to prove the existence of extremizers in [24] by an elaborate concentration-compactness argument. Foschi [14], Hundertmark and Zharnitsky [21] show that Gaussian functions are the only extremizers for (3) when d = 1,2. Bennett, Bez, Carbery and Hundertmark [3] give a diﬀerent proof of this fact by using the heat-ﬂow method. In [8], Carneiro establishes some sharp Strichartz inequalities for the Schro¨dinger equation. When d ≥ 3, we [27] have proved the existence of extremizers by using the proﬁle decompositions developed in [2]. For the wave equation, Bulut [7] has proved the existence of extremizers by using the proﬁle decompositions in the spirit of [1].

![image 9](<2016-shao-smoothness-extremizers-tomas-stein-inequality_images/imageFile9.png>)

An extremizer f to the Tomas-Stein inequality (1) is a nonzero function f ∈ L2 such that fσ

L2+

4 d (Rd+1)

![image 10](<2016-shao-smoothness-extremizers-tomas-stein-inequality_images/imageFile10.png>)

= Rd f L2(Sd). In this note, we specify the dimension d = 1 and write R = R1. In [28], we have proved there exists an extremizer when d = 1. Here we establish the smoothness property of extremizers. The work [28] and this note follow roughly similar lines as in [11, 12]. In the previous work [11, 12], Christ and the author prove the existence of extremizers and established some characterization for the Tomas-Stein inequality (1) when d = 2. In this case, Foschi [15] settles down the problem by proving that constants are the only extremizers up to the complex modulation. In [9], for (1) when d = 1, Carneiro, Foschi, Silva and Thiele recently prove a conditional result that constants are the only extremizers up to the complex modulation. This relies on the earlier work of Silva and Thiele [29] about the inequality of a 6-fold product of Bessel functions and the study of a functional equation of Cauchy-Pexider type on the sphere in Charalambides [10]. Very recently Frank, Lieb and Sabin [17] prove that extremizers always exist for the Tomas-Stein inequality (1) in all dimensions provided that a well-known conjecture the Strichartz inequalities for the Schro¨dinger equations is true.

The work [11, 12, 28] are partly motivated by the recent progress of application of the concentration compactness method or the proﬁle decompositions in critical dispersive partial diﬀerential equations, see for instance Bourgain [5], Colliander, Keel, Staﬃlani, Takaoka and Tao [13], Kenig and Merle [22, 23] for radial or general data. In Lemma 3.4 below establishing smoothness of extremizers, the analysis resembles some feature in the works of critical equations. We need to show that the critical points break the L2 approximate scaling and hence gain certain regularity.

In this note, we chacterize the extremizers in hope of ﬁnding the exact forms. We will prove that solutions to the following generalized Euler-Lagrange equation, which the extremizers satisfy, are smooth. The equation to the inequality (1) is that, for f ∈ L2(S1),

- (4) fσ ∗ fσ ∗ fσ ∗ fσ˜ ∗ fσ˜ (x) = λf(x), for almost everywhere x ∈ S1,


where λ = R6 f 4L2 and f˜(x) = f¯(−x), f¯ denotes the complex conjugate of f. The main result is the following.

Theorem 1.1. Any L2 solution to the Euler-Lagrange equation (4) is smooth on S1.

The proof of this theorem follows roughly the similar lines as in [12]. The ﬁrst step is to show that solutions to the generalized Euler-Lagrange equation gain some regularity depending on the critical points themselves; the second step is a bootstrap argument upgrading the regularity to inﬁnity, see Section 3. The diﬃculty is that there is no useful formula for the convolution σ ∗ σ ∗ σ ∗ σ ∗ σ, see also [9, Section 2]. However it is uniformly bounded by a simple application of the Hausdorﬀ-Young inequality, which is enough for us to upgrade the regularity to inﬁnity in the second step of our argument. This approach could also used to replace a key step in [12] in proving smoothness of extremizers for the Tomas-Stein inequality for the two dimensional sphere S2 as σ2 ∗ σ2 ∗ σ2, where σ2 denotes the surface measure of S2, is uniformly bounded by an easy computation.

This paper is organized as follows. In Section 2, we set up some notations. In Section 3, we give the main argument showing that the extremizers to (1) are smooth.

Acknowledgement. The author was supported in part by the NSF grant DMS-1160981 and KU 2016 -2017 general research fund. The author is deeply grateful to the hospitality of Wuhan center for mathematical sciences at Huazhong University of Science and Technology in China while part of this work was done. I am also indebted to A. Stefanov for pointing out an error in the bootstrap argument.

2. Notation

For s ≥ 0, Hs = Hs(S1) denotes the usual Sobolev space of functions having s ≥ 0 derivatives in L2. We also write H0 by L2. Consider the action of the group O(2) of all rotations of R2 acting on S1. This action gives rise in a natural way to actions on functions by

Θ(f) = f ◦ Θ

and on ﬁnite Borel measures on R2 by Θ∗(µ)(E) = µ(Θ(E)). The extension satisﬁes the basic identity

Θ∗(µ ∗ ν) = Θ∗(µ) ∗ Θ∗(ν).

Let {Xj : j = 1,2} be two C∞ vector ﬁelds on S1 which generate rotations about the two coordinate axes, where Xj is along the xj direction on R2; thus exp(tXj), the exponential map acting on Xj [25, Page 130], is obtained by rotating x ∈ R2 by t radians about the j-th coordinate axis. These two vector ﬁelds span the one dimension tangent space to S1 at each of its points. So H1(S1) is equal to the set of all f ∈ L2(S1) for all Xj(f) ∈ L2(S1) for all indices j ∈ {1,2}.

For α ∈ (0,1), we denote by Λα the space of all H¨older continuous functions of order α on S1, with norm

|f(x) − f(y)| |x − y|α

.

f Λα = f C0 + sup x =y

![image 11](<2016-shao-smoothness-extremizers-tomas-stein-inequality_images/imageFile11.png>)

For α ∈ (0,1), Λα equals the set of all continuous functions f for which there exists C < ∞ such that

|exp(tXj)f(x) − f(x)| ≤ C|t|α

for all t ∈ R and x ∈ S1 for j = 1,2, with a corresponding equivalence of norms. We denote by Lip(S1) the space of all Lipschitz continuous functions from S1 to C, equipped with the norm

|f(x) − f(y)| |x − y|

.

f C0 + sup x =y

![image 12](<2016-shao-smoothness-extremizers-tomas-stein-inequality_images/imageFile12.png>)

For 0 ≤ s ∈/ Z, we write s = k + α, where k ∈ Z and α ∈ (0,1). For s ∈ (0,1), we deﬁne Hs to be the set of all f ∈ L2(S1) for which

2

exp(tXj)f − f L2(S1) |t|s

sup

f Hs = f L2(S1) +

![image 13](<2016-shao-smoothness-extremizers-tomas-stein-inequality_images/imageFile13.png>)

0<|t|≤1

j=1

is ﬁnite. For s = 0, we deﬁne H0 = L2. For s = k + α with k ∈ Z+ and α ∈ (0,1), Hs is the set of all f ∈ L2(S1) for which

2

Y f ◦ exp(tXj)f − Y f L2(S1) |t|s

sup

f Hs = f L2(S1) +

![image 14](<2016-shao-smoothness-extremizers-tomas-stein-inequality_images/imageFile14.png>)

0<|t|≤1

j=1

Y

is ﬁnite, where Y ranges over the ﬁnite set of all compositions Xi1 ◦Xi2 ◦···◦Xim with 0 ≤ m ≤ k factors. Here f = Y f, where Y has zero factors. The mapping f  → Θ(f) = f ◦ Θ maps Hs isometrically to Hs, uniformly for all Θ ∈ O(2). For any 0 < t < s, it is not hard to see that Hs is contained in the Sobolev space Ht, and

- (5) f Ht ≤ C(s,t) f Hs for all f ∈ Hs, see for instance [30, Chapter 5, Proposition 10 and Theorem 5].

3. the proof

In this section, we prove Theorem 1.1. We ﬁrst show that solutions to the generalized EulerLagrange equation (4) gain some regularity, see Lemma 3.4. Then we upgrade the regularity to inﬁnity, see Lemma 3.5. We begin with a trivial interpolation result.

- Lemma 3.1. For 0 < β < α,

f Hβ ≤ C f 1−

β α H0 f

![image 15](<2016-shao-smoothness-extremizers-tomas-stein-inequality_images/imageFile15.png>)

β α Hα ∼ f 1−

![image 16](<2016-shao-smoothness-extremizers-tomas-stein-inequality_images/imageFile16.png>)

β α L2 f

![image 17](<2016-shao-smoothness-extremizers-tomas-stein-inequality_images/imageFile17.png>)

β α Hα.

![image 18](<2016-shao-smoothness-extremizers-tomas-stein-inequality_images/imageFile18.png>)

Proof. The inequality follows from

(6) f L2 ≤ f 1−

β α L2 f

![image 19](<2016-shao-smoothness-extremizers-tomas-stein-inequality_images/imageFile19.png>)

β α Hα

![image 20](<2016-shao-smoothness-extremizers-tomas-stein-inequality_images/imageFile20.png>)

and for 0 < |t| ≤ 1, exp(tXj)f − f L2 |t|β

![image 21](<2016-shao-smoothness-extremizers-tomas-stein-inequality_images/imageFile21.png>)

= exp(tXj)f − f 1−

β α

![image 22](<2016-shao-smoothness-extremizers-tomas-stein-inequality_images/imageFile22.png>)

L2

exp(tXj)f − f L2 |t|α

![image 23](<2016-shao-smoothness-extremizers-tomas-stein-inequality_images/imageFile23.png>)

β α

![image 24](<2016-shao-smoothness-extremizers-tomas-stein-inequality_images/imageFile24.png>)

≤ C f 1−

β α L2 f

![image 25](<2016-shao-smoothness-extremizers-tomas-stein-inequality_images/imageFile25.png>)

β α Hα.

![image 26](<2016-shao-smoothness-extremizers-tomas-stein-inequality_images/imageFile26.png>)

- Lemma 3.2. Let µ = σ ∗ σ ∗ σ ∗ σ ∗ σ. Then µ L∞({|x|≤5}) ≤ C for some constant C > 0.




Proof. Recall that for 0 < |x| < 2, f0(x) := σ ∗ σ(x) = C

√

for some C > 0, see for instance [16]. Then we have

![image 27](<2016-shao-smoothness-extremizers-tomas-stein-inequality_images/imageFile27.png>)

![image 28](<2016-shao-smoothness-extremizers-tomas-stein-inequality_images/imageFile28.png>)

4−|x|2

|x|

µ = f0 ∗ f0 ∗ σ.

Then since f0 L1(R2) < ∞, µ ∈ L1(R2) by Funibi’s theorem and Young’s inequality. On the other hand, µ = σ5 ∈ L1 from the decay estimate of σ, i.e., | σ(x)| ≤ |x|−1/2, for suﬃciently large |x|. Thus from the Fourier inversion formula [32, Corollary 1.21], we have

µ(x) = eixξ˙ µ(ξ)dξ.

Thus an application of the L1 → L∞ Hausdorﬀ-Young inequality or the Riemann-Lebesgue lemma concludes the proof.

- Lemma 3.3. Suppose that fi ∈ Hs for i = 1,··· ,5 and s ≥ 0. Then


5

f1σ ∗ f2σ ∗ f3σ ∗ f4σ ∗ f5σ Hs ≤ C

fi Hs.

i=1

Proof. By the Cauchy-Schwarz inequality,

- (7) |f1σ ∗ ··· ∗ f5σ(x)| ≤ |f1|2σ ∗ ··· ∗ |f5|2σ(x) 1/2 (σ ∗ ··· ∗ σ(x))1/2 . If we integrate both sides, by Lemma 3.2,

f1σ ∗ ··· ∗ f5σ 2L2(S1) ≤

S1

|f1|2σ ∗ ··· ∗ |f5|2σ(x) |σ ∗ ··· ∗ σ(x)| dσ

≤ sup

x∈S1

|σ ∗ ··· ∗ σ(x)|

S1

|f1|2σ ∗ ··· ∗ |f5|2σ(x) dσ

≤ C

5

i=1

fi 2L2.

- (8)

This proves the lemma when s = 0. Let s > 0. For 0 < |t| ≤ 1, we just need to prove

exp(tXj) f1σ ∗ ··· ∗ f5σ − f1σ ∗ ··· ∗ f5σ 2L2 |t|2s

![image 29](<2016-shao-smoothness-extremizers-tomas-stein-inequality_images/imageFile29.png>)

=

S1

| f1σ ∗ ··· ∗ f5σ ◦ exp(tXj)(y) − f1σ ∗ ··· ∗ f5σ (y)|2 |t|2s

![image 30](<2016-shao-smoothness-extremizers-tomas-stein-inequality_images/imageFile30.png>)

dσ(y)

≤ C

5

i=1

fi 2Hs.

- (9)

We compute that, for j = 1,2 and 0 < |t| ≤ 1,

f1σ ∗ ··· ∗ f5σ ◦ exp(tXj) − f1σ ∗ ··· ∗ f5σ

= f1 ◦ exp(tXj) − f1 σ ∗ (exp(tXj)f2)σ ∗ (exp(tXj)f3)σ ∗ (exp(tXj)f4)σ ∗ (exp(tXj)f5)σ+ + (exp(tXj)f1)σ ∗ f2 ◦ exp(tXj) − f2 σ ∗ (exp(tXj)f3)σ ∗ (exp(tXj)f4)σ ∗ (exp(tXj)f5)σ+ + ··· + (exp(tXj)f1)σ ∗ (exp(tXj)f2)σ ∗ (exp(tXj)f3)σ ∗ (exp(tXj)f4)σ ∗ f5 ◦ exp(tXj) − f5 .

- (10)


For the ﬁrst term in (10), by the Cauchy-Schwarz inequality, f1 ◦ exp(tXj) − f1 σ ∗ (exp(tXj)f2)σ ∗ (exp(tXj)f3)σ ∗ (exp(tXj)f4)σ ∗ (exp(tXj)f5)σ

|f1 ◦ exp(tXj) − f1|2σ ∗ |exp(tXj)f2|2σ ∗ |exp(tXj)f3|2σ ∗ |exp(tXj)f4|2σ∗ ∗|exp(tXj)f5|2σ 1/2 × (σ ∗ ··· ∗ σ)1/2 .

- (11)

Applying the same reasoning to other terms in (11) and going back to (9), we see the claim in

- Lemma 3.3 for s > 0 is proved. Thus we ﬁnish the proof of Lemma 3.3.

Next we show that solutions to the Euler-Lagrange equation (4) gain some regularity.

- Lemma 3.4. Suppose that f ∈ L2 satisﬁes the Euler-Lagrange equation (4). Then f ∈ Hs for some s > 0. In particular, f ∈ Ht for all 0 ≤ t < s.


Proof. For any ǫ > 0, we decompose f such that f = φǫ + gǫ such that gǫ L2 < ǫ and φǫ ∈ C∞. Recall that

φǫ Hs = φǫ L2 +

2

j=1

sup

0<|t|≤1

exp(tXj)f − f L2(S1) |t|s

![image 31](<2016-shao-smoothness-extremizers-tomas-stein-inequality_images/imageFile31.png>)

,

and

φǫ Λs = φǫ L∞ + sup x =y

|φǫ(x) − φǫ(y)| |x − y|s

![image 32](<2016-shao-smoothness-extremizers-tomas-stein-inequality_images/imageFile32.png>)

. Then since φǫ ∈ C∞,

- (12) φǫ Hs ≤ C φǫ Λs < Cǫ < ∞. We remark that this bound depends on ǫ. From the Euler-Lagrange equation (4) and f = φǫ + gǫ, we have
- (13) gǫ = L(φǫ,gǫ) + N(φǫ,gǫ), where L is linear in gǫ and N is nonlinear in gǫ. More precisely,

L = −φǫ + φǫσ ∗ φǫσ ∗ φǫσ ∗ φ˜ǫσ ∗ φ˜ǫσ+

+ 2φǫσ ∗ φǫσ ∗ φǫσ ∗ φ˜ǫσ ∗ g˜ǫσ + 3φǫσ ∗ φǫσ ∗ φ˜ǫσ ∗ φ˜ǫσ ∗ gǫσ; and

N = gǫσ ∗ gǫσ ∗ gǫσ ∗ g˜ǫσ ∗ g˜ǫσ

+ 3gǫσ ∗ gǫσ ∗ g˜ǫσ ∗ g˜ǫσ ∗ φǫσ + 2gǫσ ∗ gǫσ ∗ gǫσ ∗ g˜ǫσ ∗ φ˜ǫσ+

+ 3gǫσ ∗ g˜ǫσ ∗ g˜ǫσ ∗ φǫσ ∗ φǫσ + 6gǫσ ∗ gǫσ ∗ g˜ǫσ ∗ φǫσ ∗ φ˜ǫσ+

+ gǫσ ∗ gǫσ ∗ gǫσ ∗ φ˜ǫσ ∗ φ˜ǫσ + g˜ǫσ ∗ g˜ǫσ ∗ φǫσ ∗ φǫσ ∗ φǫσ

+ 6gǫσ ∗ g˜ǫσ ∗ φǫσ ∗ φǫσ ∗ φ˜ǫσ + 3gǫσ ∗ gǫσ ∗ φǫσ ∗ φ˜ǫσ ∗ φ˜ǫσ. For any α > 0,

- (14)  L(φǫ,gǫ) Λα ≤ φǫ Λα + C φǫ 5Λα + C φǫ 4Λα gǫ L2 Since φǫ Λα < Cǫ < ∞ and gǫ L2 ≤ f L2,
- (15)  L(φǫ,gǫ) Λα < Cǫ < ∞.


- Together with  L(φǫ,gǫ) Hα ≤  L(φǫ,gǫ) Λα, this implies
- (16)  L(φǫ,gǫ) Hα ≤ Cǫ < ∞. On the other hand, by Lemma 3.3,

 N(φǫ,gǫ) H0 gǫ 5H0 + gǫ 4H0 φǫ H0 + gǫ 3H0 φǫ 2H0 + gǫ 2H0 φǫ 3H0 ǫ5 + ǫ4 + ǫ3 + ǫ2 ǫ2,

- (17)

as gǫ H0 ∼ gǫ L2 ≤ ǫ and φǫ H0 ∼ φǫ L2 ≤ 1. By the triangle inequality we have

- (18)  L(φǫ,gǫ) H0 ≤ Cǫ.

Choosing ǫ suﬃciently small, and interpolating between (16) and (18), we see that there exists s(ǫ) depending on ǫ such that

- (19)  L(φǫ,gǫ) Hs(ǫ) ǫ78.

![image 33](<2016-shao-smoothness-extremizers-tomas-stein-inequality_images/imageFile33.png>)

From the two bounds φǫ H0 ≤ 1 and φǫ Hα < C(ǫ) < ∞, again choosing s(ǫ) suﬃciently small, we see that

- (20) φǫ Hs(ǫ) < ǫ−1/5. Next we use the argument of Picard’s iteration to show that f will gain some regularity. Fixing

the small ǫ > 0 above, we know that gǫ ∈ L2 and φǫ ∈ C∞. Deﬁne the iteration mapping and the ball in Hs(ǫ),

Lǫ(h) = L(φǫ,gǫ) + N(φǫ,h), B = B(L(φǫ,gǫ),ǫ34).

![image 34](<2016-shao-smoothness-extremizers-tomas-stein-inequality_images/imageFile34.png>)

- (21)

In the following two steps, we show that Lǫ is a contraction map on B. The ﬁrst step is to show that Lǫ maps B to itself. The second step is to show that Lǫ Lipschitz with the Lipschitz constant strictly less than 1.

- Step 1. For any h ∈ B, by the triangle inequality and (19),

- (22) h Hs(ǫ) ≤ h − L(φǫ,gǫ) Hs(ǫ) +  L(φǫ,gǫ) Hs(ǫ) ǫ34 + ǫ87 ǫ34. Then similarly as in proving (17), by (20),

![image 35](<2016-shao-smoothness-extremizers-tomas-stein-inequality_images/imageFile35.png>)

![image 36](<2016-shao-smoothness-extremizers-tomas-stein-inequality_images/imageFile36.png>)

![image 37](<2016-shao-smoothness-extremizers-tomas-stein-inequality_images/imageFile37.png>)

- (23)  N(φǫ,h) Hs(ǫ) ǫ34×5 + ǫ43×4ǫ−51 + ǫ43×3ǫ−51×2 + ǫ43×2ǫ−15×3 ≤ ǫ34/10. Then for h ∈ B,

![image 38](<2016-shao-smoothness-extremizers-tomas-stein-inequality_images/imageFile38.png>)

![image 39](<2016-shao-smoothness-extremizers-tomas-stein-inequality_images/imageFile39.png>)

![image 40](<2016-shao-smoothness-extremizers-tomas-stein-inequality_images/imageFile40.png>)

![image 41](<2016-shao-smoothness-extremizers-tomas-stein-inequality_images/imageFile41.png>)

![image 42](<2016-shao-smoothness-extremizers-tomas-stein-inequality_images/imageFile42.png>)

![image 43](<2016-shao-smoothness-extremizers-tomas-stein-inequality_images/imageFile43.png>)

![image 44](<2016-shao-smoothness-extremizers-tomas-stein-inequality_images/imageFile44.png>)

![image 45](<2016-shao-smoothness-extremizers-tomas-stein-inequality_images/imageFile45.png>)

- (24)  Lǫ(h) − L(φǫ,gǫ) Hs(ǫ) =  N(φǫ,h) Hs(ǫ) ≤ ǫ43. This proves that Lǫ is a map from B to B.


![image 46](<2016-shao-smoothness-extremizers-tomas-stein-inequality_images/imageFile46.png>)

- Step 2. We take h1,h2 ∈ B. Then by (22),


- (25) h1 Hs(ǫ) ǫ34, and h2 Hs(ǫ) ǫ43. Note that by (20), φǫ Hs(ǫ) ≤ ǫ−15, then by Lemma 3.3,

![image 47](<2016-shao-smoothness-extremizers-tomas-stein-inequality_images/imageFile47.png>)

![image 48](<2016-shao-smoothness-extremizers-tomas-stein-inequality_images/imageFile48.png>)

![image 49](<2016-shao-smoothness-extremizers-tomas-stein-inequality_images/imageFile49.png>)

Lǫ(h2) − Lǫ(h1) = N(φǫ,h2) − N(φǫ,h1) h2 − h1 Hs(ǫ) 5ǫ34×4 + 5 × 5ǫ43×3−15 + 10 × 3ǫ34×2−51×2 + 10 × 2ǫ34−51×3 .

![image 50](<2016-shao-smoothness-extremizers-tomas-stein-inequality_images/imageFile50.png>)

![image 51](<2016-shao-smoothness-extremizers-tomas-stein-inequality_images/imageFile51.png>)

![image 52](<2016-shao-smoothness-extremizers-tomas-stein-inequality_images/imageFile52.png>)

![image 53](<2016-shao-smoothness-extremizers-tomas-stein-inequality_images/imageFile53.png>)

![image 54](<2016-shao-smoothness-extremizers-tomas-stein-inequality_images/imageFile54.png>)

![image 55](<2016-shao-smoothness-extremizers-tomas-stein-inequality_images/imageFile55.png>)

![image 56](<2016-shao-smoothness-extremizers-tomas-stein-inequality_images/imageFile56.png>)

- (26)

To conclude, if taking ǫ suﬃciently small,

- (27)  Lǫ(h2) − Lǫ(h1) Hs(ǫ) ≤ α h2 − h1 Hs(ǫ)


- for some 0 < α < 1. So Lǫ is a contraction mapping on B. Therefore there exists a unique hǫ ∈ B ⊂ Hs(ǫ) such that
- (28) hǫ = Lǫ(hǫ) = L(φǫ,gǫ) + N(φǫ,hǫ). Moreover hǫ Hs(ǫ) ǫ34. When Hs(ǫ) is replaced by L2, the same argument implies that there exists a unique solution in L2. Since Hs(ǫ) ⊂ H0 = L2, if ǫ is suﬃciently small, then hǫ is also the unique L2 solution with small L2 norm. We know that in L2 there holds

![image 57](<2016-shao-smoothness-extremizers-tomas-stein-inequality_images/imageFile57.png>)

gǫ = L(φǫ,gǫ) + N(φǫ,gǫ),

and gǫ has small L2 norm. So gǫ agrees with hǫ in L2. This upgrades gǫ ∈ Hs(ǫ). It in turn shows that f ∈ Hs(ǫ). Note that s(ǫ) depends on f.

The second main ingredient is a bootstrap lemma.

- Lemma 3.5. For any ǫ > 0, there exists δ > 0 such that for any s ∈ [ǫ,∞) \ Z and any function f ∈ Hs(S1), then


- (29) fσ ∗ fσ ∗ fσ ∗ fσ ∗ fσ|S1 ∈ Ht(S1) for all t ∈ [0,s + δ] \ Z.

This proof is similar to [12, Lemma 3.2] and so will be omitted. It relies on the following proposition, which is in the same spirit as [12, Lemma 2.6].

Proposition 3.6. For any ǫ > 0, there exists δ > 0 such that

f1σ ∗ f2σ ∗ f3σ ∗ f4σ ∗ hσ ∈ Hδ whenever fi ∈ Hǫ(S1),1 ≤ i ≤ 4, and h ∈ H0(S1), and

- (30) f1σ ∗ f2σ ∗ f3σ ∗ f4σ ∗ hσ Hδ ≤ Cǫ

4

j=1

fi Hǫ h H0.

Proof. Without loss of generality, we suppose that

fi Hǫ = 1, for 1 ≤ i ≤ 4, and h H0 = 1. We divide the proof in the following 3 steps.

- Step 1. We establish the inequality (30) for any 0 < δ < 1 under the hypothesis that fi ∈ Lip(S1), for 1 ≤ i ≤ 4.


Let F(x) = f1σ ∗ f2σ ∗ f3σ ∗ f4σ ∗ hσ(x), ν = σ ∗ σ ∗ σ ∗ σ and I be the identity operator. We claim that F ∈ Hδ.

For 0 < |t| ≤ 1 and j = 1,2, we consider exp(tXj)(|Ft|)(δ x)−F(x)| . By a similar expansion as in (10), exp(tXj)F(x) − F(x) = exp(tXj)(f1σ ∗ f2σ ∗ f3σ ∗ f4σ ∗ hσ) − f1σ ∗ f2σ ∗ f3σ ∗ f4σ ∗ hσ

![image 58](<2016-shao-smoothness-extremizers-tomas-stein-inequality_images/imageFile58.png>)

= (exp(tXj) − I)f1σ ∗ exp(tXj)f2σ ∗ exp(tXj)f3σ ∗ exp(tXj)f4σ ∗ exp(tXj)hσ+

+ ··· + f1σ ∗ f2σ ∗ f3σ ∗ (exp(tXj) − I)f4σ ∗ exp(tXj)hσ+

+ f1σ ∗ f2σ ∗ f3σ ∗ f4σ ∗ exp(tXj)hσ − f1σ ∗ f2σ ∗ f3σ ∗ f4σ ∗ hσ.

- (31)


For the last line above in (31), it equals exp(tXj)(f1σ ∗ f2σ ∗ f3σ ∗ f4σ) ∗ hσ − f1σ ∗ f2σ ∗ f3σ ∗ f4σ ∗ hσ

= [(exp(tXj) − I)f1σ ∗ exp(tXj)f2σ ∗ exp(tXj)f3σ ∗ exp(tXj)f4σ] ∗ hσ+

+ ··· + [f1σ ∗ f2σ ∗ f3σ ∗ (exp(tXj) − I)f4σ] ∗ hσ Thus we see that all terms in (31) are bounded by

 

 

4

≤ C

dν(x − y)|h(y)|dσ

fi Lip(S1)

S1

j=1

 sup

 

4

(σ ∗ σ ∗ σ ∗ σ ∗ σ(x))1/2 σ ∗ σ ∗ σ ∗ σ ∗ |h|2σ(x) 1/2

≤ C

fi Lip(S1)

x

j=1

≤ C σ ∗ σ ∗ σ ∗ σ ∗ |h|2σ(x) 1/2 .

Here the second to last inequality follows from the Cauchy-Schwarz inequality and the last follows from Lemma 3.2.

Thus for j = 1,2, for 0 < |t| ≤ 1, by Fubini’s theorem, exp(tXj)F − F L2(S1) |t|δ

(σ ∗ σ ∗ σ ∗ σ ∗ σ(x)) h L2(S1). This leads to

sup

![image 59](<2016-shao-smoothness-extremizers-tomas-stein-inequality_images/imageFile59.png>)

x

2

exp(tXj)F − F L2(S1) |t|δ

< ∞.

sup

![image 60](<2016-shao-smoothness-extremizers-tomas-stein-inequality_images/imageFile60.png>)

0<|t|≤1

j=1

From Lemma 3.3, F ∈ L2(S1). So h ∈ Hδ(S1). Fix δ.

- Step 2. For any f ∈ Hǫ(S1) and η > 0, there exists a decomposition that f = f♯ + fb, where f♯ ∈ Lip(S1) and


fb H0 ≤ η f Hǫ,

f♯ Lip(S1) ≤ η−C(ǫ) f Hǫ, f♯ H0 ≤ C f Hǫ,

where C,C(ǫ) independent of f. The existence of such decomposition follows from the inclusion that Hǫ ⊂ Hτ for some τ = τ(ǫ) > 0, together with standard properties of Hτ. We perform such decompositions to each fi, 1 ≤ i ≤ 4. Step 1 implies that

- (32) f1♯σ ∗ f2♯σ ∗ f3♯σ ∗ f4♯σ ∗ hσ ∈ Hδ(S1), with the operator norm O(η−4C(ǫ)). On the other hand,
- (33) f1bσ ∗ f2bσ ∗ f3bσ ∗ f4bσ ∗ hσ L2(S1) ≤ C


4

fib L2(S1) h L2 ≤ Cη4.

j=1

Similarly the contributions of the pairs (fi♯,fjb), 1 ≤ i,j ≤ 4, belong to L2(S1) with norms O(η), since fi♯ ∈ H0 is of O(1).

So far we have shown that for any η > 0, F = f1σ ∗ f2σ ∗ f3σ ∗ f4σ ∗ hσ can be decomposed as the sum of two functions

- (34) F = Fη + Fη,

where Fη ∈ L2 and Fη L2 ≤ η, and Fη ∈ Hδ, and Fη Hδ ≤ Cη−C(ǫ). Then we claim that F ∈ Hδ for some δ depending on ǫ.

- Step 3. Let 0 < |t| ≤ 1 and η > 0 be a parameter to be determined. For F = Fη + Fη, then


- (35) exp(tXj)Fη − Fη L2(S1) ≤ C|t|δ Fη Hδ ≤ C|t|δη−C(ǫ); and
- (36) exp(tXj)Fη − Fη L2(S1) ≤ 2 Fη L2(S1) ≤ 2η. Then by the triangle inequality
- (37) exp(tXj)F − F L2(S1) ≤ C|t|δη−C(ǫ) + 2η. Deﬁne η by C|t|δη−C(ǫ) = 2η. Then

η =

C|t|δ 2

![image 61](<2016-shao-smoothness-extremizers-tomas-stein-inequality_images/imageFile61.png>)

1 1+C(ǫ)

![image 62](<2016-shao-smoothness-extremizers-tomas-stein-inequality_images/imageFile62.png>)

. Therefore

- (38) exp(tXj)F − F L2(S1) ≤ 4


1 1+C(ǫ)

C 2

![image 63](<2016-shao-smoothness-extremizers-tomas-stein-inequality_images/imageFile63.png>)

δ

δ

|t|

1+C(ǫ) = Cǫ|t|

1+C(ǫ).

![image 64](<2016-shao-smoothness-extremizers-tomas-stein-inequality_images/imageFile64.png>)

![image 65](<2016-shao-smoothness-extremizers-tomas-stein-inequality_images/imageFile65.png>)

![image 66](<2016-shao-smoothness-extremizers-tomas-stein-inequality_images/imageFile66.png>)

We re-deﬁne δ to be 1+Cδ (ǫ). This ﬁnishes the proof of Proposition 3.6.

![image 67](<2016-shao-smoothness-extremizers-tomas-stein-inequality_images/imageFile67.png>)

Therefore from Lemma 3.4 and 3.5, the proof of Theorem 1.1 is complete.

References

- [1] H. Bahouri and P. Ge´rard. High frequency approximation of solutions to critical nonlinear wave equations. Amer. J. Math., 121(1):131–175, 1999.
- [2] P. Be´gout and A. Vargas. Mass concentration phenomena for the L2-critical nonlinear Schr¨odinger equation. Trans. Amer. Math. Soc., 359(11): 5257–5282, 2007.
- [3] J. Bennett, N. Bez, A. Carbery, and D. Hundertmark. Heat-ﬂow monotonicity of Strichartz norms. Analysis and PDE, Vol. 2, No. 2: 147–158, 2009.
- [4] J. Bourgain. Besicovitch type maximal operators and applications to Fourier analysis. Geom. Funct. Anal., 1(2): 147–187, 1991.
- [5] J. Bourgain. Global wellposedness of defocusing critical nonlinear Schr¨odinger equation in the radial case. J. Amer. Math. Soc., 12(1): 145–171, 1999.
- [6] J. Bourgain, L. Guth. Bounds on oscillatory integral operators based on multilinear estimates. Geom. Funct. Anal., 21(6): 1239–1295, 2011.
- [7] A. Bulut. Maximizers for the Strichartz inequalities for the Wave Equation. Diﬀerential and Integral Equations, 23: 1035-1072, 2010.
- [8] E. Carneiro. A sharp inequality for the Strichartz norm. Int. Math. Res. Not. IMRN, (16): 3127–3145, 2009.
- [9] E. Carneiro, D. Foschi, D. Silva and C. Thiele. A sharp trilinear inequality related to Fourier restriction on the circle. arXiv:1509.06674.
- [10] M. Charalambides. On Restricting Cauchy-Pexider Equations to Submanifolds. Aequationes Math. 86: 231253,2013.
- [11] M. Christ and S. Shao. Existence of extremals for a Fourier restriction inequality. Analysis and PDE. 5(2): 261–312, 2012.


- [12] M. Christ and S. Shao. On the extremisers of an adjoint Fourier restriction inequality. Advance in Mathematics. 230 (3): 957–977, 2012.
- [13] J. Colliander, M. Keel, G. Staﬃlani, H. Takaoka, and T. Tao. Global well-posedness and scattering for the energy-critical nonlinear Schr¨odinger equation in R3. Ann. of Math. (2), 167(3):767–865, 2008.
- [14] D. Foschi. Maximizers for the Strichartz inequality. J. Eur. Math. Soc. (JEMS), 9(4): 739–774, 2007.
- [15] D. Foschi. Global maximizers for the sphere adjoint Fourier restriction inequality. J. Funct. Anal. 268(3): 690–702, 2015.
- [16] D. Foschi and S. Klainerman. Bilinear space-time estimates for homogeneous wave equations. Ann. Sci. Ecole´ Norm. Sup. (4), 33 (2) (2000), 211–274.
- [17] R. L. Frank, E. H. Lieb, J. Sabin. Maximizers for the Stein-Tomas Inequality. GAFA. 26(4): 1095–1134, 2016.
- [18] L. Guth. A restriction estimate using polynomial partitioning. Journal of the American Mathematical Society, 29(2): 371–413,2016.
- [19] L. Guth. Restriction estimates using polynomial partitioning II. arXiv:1603.04250.
- [20] D. Hundertmark and S. Shao. Analyticity of extremals to the Airy-Strichartz inequality. Bull. London Math. Soc. 44(2): 336-352, 2012.
- [21] D. Hundertmark and V. Zharnitsky. On sharp Strichartz inequalities in low dimensions. Int. Math. Res. Not., pages Art. ID 34080, 18, 2006.
- [22] C. Kenig and F. Merle. Global well-posedness, scattering and blow-up for the energy-critical, focusing, nonlinear Schr¨odinger equation in the radial case. Invent. Math., 166(3): 645–675, 2006.
- [23] C. Kenig and F. Merle. Global well-posedness, scattering and blow-up for the energy-critical focusing non-linear wave equation. Acta Math., 201(2): 147–212, 2008.
- [24] M. Kunze. On the existence of a maximizer for the Strichartz inequality. Comm. Math. Phys., 243(1): 137–162, 2003.
- [25] P. Petersen. Riemannian geometry. Graduate Texts in Mathematics 171, Second Edition, Springer.
- [26] S. Shao. The linear proﬁle decomposition for the Airy equation and the existence of maximizers for the Airy Strichartz inequality. Anal. PDE, 2(1): 83–117, 2009.
- [27] S. Shao. Maximizers for the Strichartz and the Sobolev-Strichartz inequalities for the Schr¨odinger equation. Electron. J. Diﬀerential Equations, 3: 1-13, 2009.
- [28] S. Shao. On existence of extremizers for the Tomas-Stein inequality for S1. Journal of Functional Analysis, 270: 3996-4038, 2016.
- [29] D. Silva and C. Thiele. Estimates for certain integrals of products of six Bessel functions. arXiv:1509.06309.
- [30] E. Stein. Singular integrals and diﬀerentiability properties of functions. Princeton Mathematical Series, No. 30, Princeton, NJ, 1970.
- [31] E. M. Stein. Harmonic analysis: real-variable methods, orthogonality, and oscillatory integrals, volume 43 of Princeton Mathematical Series. Princeton University Press, Princeton, NJ, 1993. With the assistance of Timothy S. Murphy, Monographs in Harmonic Analysis, III.
- [32] E. Stein and G. Weiss. Introduction to Fouerier Analysis on Euclidean Spaces. Princeton Mathematical Series, No. 32, Princeton, NJ, 1971.
- [33] T. Tao. A sharp bilinear restrictions estimate for paraboloids. Geom. Funct. Anal., 13(6): 1359–1384, 2003.
- [34] T. Tao. Nonlinear dispersive equations, local and global analysis. CBMS Regional Conference Series in Mathematics, 106, 2006.
- [35] T. Wolﬀ. A sharp bilinear cone restriction estimate. Ann. of Math. (2), 153(3): 661–698, 2001.


Department of Mathematics, KU, Lawrence, KS 66045

E-mail address: slshao@ku.edu

